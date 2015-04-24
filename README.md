PyTimeframe
===========
Time frame spans the date range (start date and end date) from the given time frame string. This 
also supports the source timezone and target timezone.

For eg. You have data set in UTC time zone but your client is in PST time zone and want data 
accordingly.

## Installation

    python setup.py install
    
the pip way

    pip install pytimeframe
    

## Time frame string
The time frame string reference is taken from keen.io. Below are the supported relative timeframes:

* **this_hour** - Creates a timeframe starting from the beginning of the current hour until now.
* **today** or **this_day** - Creates a timeframe starting from the beginning of the current day 
until now.
* **this_week** - Creates a timeframe starting from the beginning of the current week until now.
* **this_month** - Creates a timeframe starting from the beginning of the current month until now.
* **this_year** - Creates a timeframe starting from the beginning of the current year until now.
* **this_n_days** - All of the current day and the previous completed n-1 days.
* **this_n_weeks** - All of the current week and the previous completed n-1 weeks.
* **this_n_months** - All the current month and previous completed n-1 months.
* **this_n_years** - All the current year and previous completed n-1 years.
* **previous_minute** - convenience for “previous_1_minute”
* **previous_hour** - convenience for “previous_1_hour”
* **yesterday** or **previous_day** - convenience for “previous_1_day”
* **previous_week** - convenience for “previous_1_week”
* **previous_month** - convenience for “previous_1_months”
* **previous_year** - convenience for “previous_1_years”
* **previous_n_days** - Gives a starting point of n-days before the most recent complete day and an 
end at the most recent complete day. (For example: If right now it is Friday at 9:00am and I specify a timeframe of “previous_3_days”, the timeframe would stretch from Tuesday morning at 12:00am until Thursday night at midnight.)
* **previous_n_weeks** - Gives a start of n-weeks before the most recent complete week and an end at 
the most recent complete week. (For example: If right now it is Monday, and I specify a timeframe of “previous_2_weeks”, the timeframe would stretch from three Sunday mornings ago at 12:00am until the most recent Sunday at 12:00am (yesterday morning).)
* **previous_n_months** - Gives a start of n-months before the most recent completed month and an end 
at the most recent completed month. (For example: If right now is the 5th of the month, and I specify a timeframe of “previous_2_months”, the timeframe would stretch from the start of two months ago until the end of last month.)
* **previous_n_years** - Gives a start of n-years before the most recent completed year and an end at 
the most recent completed year. (For example: If right now is the June 5th, and I specify a timeframe of “previous_2_years”, the timeframe would stretch from the start of two years ago until the end of last year.)

## How to use

    from pytimeframe import Timeframe
    
    tf = Timeframe('Asia/Calcutta', 'UTC') # Timeframe(<Local_TZ>, <Target_TZ>)
    
    print 'today', tf.span('today')
    print 'this_week', tf.span('this_week')
    print 'this_month', tf.span('this_month')
    print 'this_year', tf.span('this_year')
    print 'this_4_days', tf.span('this_4_days')
    print 'this_2_weeks', tf.span('this_2_weeks')
    print 'this_2_months', tf.span('this_2_months')
    print 'this_2_years', tf.span('this_2_years')
    print 'yesterday', tf.span('yesterday')
    print 'previous_2_days', tf.span('previous_2_days')
    print 'previous_week', tf.span('previous_week')
    print 'previous_3_weeks', tf.span('previous_3_weeks')
    print 'previous_month', tf.span('previous_month')
    print 'previous_2_months', tf.span('previous_2_months')
    print 'previous_year', tf.span('previous_year')
    print 'previous_4_years', tf.span('previous_4_years')
    
    # today (datetime.datetime(2015, 4, 23, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 4, 24, 
    7, 16, 49, 624260, tzinfo=<UTC>))
    # this_week (datetime.datetime(2015, 4, 19, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 4, 
    24, 7, 16, 49, 624375, tzinfo=<UTC>))
    # this_month (datetime.datetime(2015, 4, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 4, 
    24, 7, 16, 49, 624465, tzinfo=<UTC>))
    # this_year (datetime.datetime(2015, 1, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 4, 
    24, 7, 16, 49, 624547, tzinfo=<UTC>))
    # this_4_days (datetime.datetime(2015, 4, 20, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 
    4, 24, 7, 16, 49, 624624, tzinfo=<UTC>))
    # this_2_weeks (datetime.datetime(2015, 4, 12, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 
    4, 24, 7, 16, 49, 624705, tzinfo=<UTC>))
    # this_2_months (datetime.datetime(2015, 3, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 
    4, 24, 7, 16, 49, 624790, tzinfo=<UTC>))
    # this_2_years (datetime.datetime(2014, 1, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 
    4, 24, 7, 16, 49, 624878, tzinfo=<UTC>))
    # yesterday (datetime.datetime(2015, 4, 22, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 4, 
    23, 18, 29, 59, tzinfo=<UTC>))
    # previous_2_days (datetime.datetime(2015, 4, 21, 18, 30, tzinfo=<UTC>), 
    datetime.datetime(2015, 4, 23, 18, 29, 59, tzinfo=<UTC>))
    # previous_week (datetime.datetime(2015, 4, 12, 18, 30, tzinfo=<UTC>), datetime.datetime(2015,
     4, 19, 18, 29, 59, tzinfo=<UTC>))
    # previous_3_weeks (datetime.datetime(2015, 3, 29, 18, 30, tzinfo=<UTC>), 
    datetime.datetime(2015, 4, 19, 18, 29, 59, tzinfo=<UTC>))
    # previous_month (datetime.datetime(2015, 3, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015,
     4, 1, 18, 29, 59, tzinfo=<UTC>))
    # previous_2_months (datetime.datetime(2015, 2, 1, 18, 30, tzinfo=<UTC>), 
    datetime.datetime(2015, 4, 1, 18, 29, 59, tzinfo=<UTC>))
    # previous_year (datetime.datetime(2014, 1, 1, 18, 30, tzinfo=<UTC>), datetime.datetime(2015, 
    1, 1, 18, 29, 59, tzinfo=<UTC>))
    # previous_4_years (datetime.datetime(2011, 1, 1, 18, 30, tzinfo=<UTC>), 
    datetime.datetime(2015, 1, 1, 18, 29, 59, tzinfo=<UTC>))


## To Do:

* Test case
