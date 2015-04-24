import datetime
import re

import pytz


__all__ = ['Timeframe']


class Timeframe(object):
    tz = 'utc'

    def __init__(self, tz, target_tz='UTC'):
        self.tz = pytz.timezone(tz)
        self.target_tz = pytz.timezone(target_tz)
        self.now = self._gen_now()
        self.day_start = self._get_day_start()

    def span(self, frame):
        now = self._gen_now()
        now_date = self._get_day_start()

        this_n_days = self._get_n_unit(frame, 'this', 'days')
        this_n_weeks = self._get_n_unit(frame, 'this', 'weeks')
        this_n_months = self._get_n_unit(frame, 'this', 'months')
        this_n_years = self._get_n_unit(frame, 'this', 'years')
        previous_n_days = self._get_n_unit(frame, 'previous', 'days')
        previous_n_weeks = self._get_n_unit(frame, 'previous', 'weeks')
        previous_n_months = self._get_n_unit(frame, 'previous', 'months')
        previous_n_years = self._get_n_unit(frame, 'previous', 'years')

        if frame == 'today' or frame == 'this_day':
            return self.span('this_1_days')
        elif frame == 'this_week':
            start = self._get_week_start()
            return start, now
        elif frame == 'this_month':
            start = self._get_month_start()
            return start, now
        elif frame == 'this_year':
            start = now_date.replace(month=1, day=1)
            return start, now
        elif len(this_n_days) == 1:
            day = int(this_n_days[0])
            start = now_date - datetime.timedelta(days=day - 1)
            return start, now
        elif len(this_n_weeks) == 1:
            week = int(this_n_weeks[0])
            start = self._get_week_start() - datetime.timedelta(weeks=week - 1)
            return start, now
        elif len(this_n_months) == 1:
            months = self._get_month_start().month - (int(this_n_months[0]) - 1)
            start = self._get_month_start().replace(month=months)
            return start, now
        elif len(this_n_years) == 1:
            years = self._get_month_start().year - (int(this_n_years[0]) - 1)
            start = self._get_month_start().replace(month=1, year=years)
            return start, now
        elif frame == 'yesterday' or frame == 'previous_day':
            return self.span('previous_1_days')
        elif frame == 'previous_week':
            return self.span('previous_1_weeks')
        elif frame == 'previous_month':
            return self.span('previous_1_months')
        elif frame == 'previous_year':
            return self.span('previous_1_years')
        elif len(previous_n_days) == 1:
            days = previous_n_days[0]
            start = now_date - datetime.timedelta(days=days)
            end = now_date - datetime.timedelta(seconds=1)
            return start, end
        elif len(previous_n_weeks) == 1:
            weeks = previous_n_weeks[0]
            start = self._get_week_start() - datetime.timedelta(weeks=weeks)
            end = self._get_week_start() - datetime.timedelta(seconds=1)
            return start, end
        elif len(previous_n_months) == 1:
            months = self._get_month_start().month - previous_n_months[0]
            start = self._get_month_start().replace(month=months)
            end = self._get_month_start() - datetime.timedelta(seconds=1)
            return start, end
        elif len(previous_n_years) == 1:
            years = self._get_month_start().year - previous_n_years[0]
            start = self._get_month_start().replace(year=years, month=1)
            end = self._get_month_start().replace(month=1) - datetime.timedelta(seconds=1)
            return start, end

    def _gen_now(self):
        self.now = datetime.datetime.now(self.tz).astimezone(self.target_tz)
        return self.now

    def _get_day_start(self):
        today = datetime.datetime.now(self.tz).replace(hour=0, minute=0, second=0, microsecond=0)
        self.day_start = today.astimezone(self.target_tz)
        return self.day_start

    def _get_week_start(self):
        return self.day_start - datetime.timedelta(days=self.day_start.isoweekday())

    def _get_month_start(self):
        return self.day_start - datetime.timedelta(days=self.day_start.day - 1)

    @classmethod
    def _get_n_unit(cls, frame, period, unit):
        return map(int, re.findall(r'%s_([0-9]+)_%s' % (period, unit), frame))
