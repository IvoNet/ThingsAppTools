__author__ = 'ivonet'

import datetime


class MyTzinfo(datetime.tzinfo):
    def __init__(self, *args, **kwargs):
        super(MyTzinfo, self).__init__(*args, **kwargs)

        # def dst(self, date_time):
    #     return 2

    def utcoffset(self, date_time):
        return datetime.timedelta(hours=2)
