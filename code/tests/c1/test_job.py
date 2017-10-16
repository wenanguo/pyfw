#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Andrew Wen'

from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print('hello world')


sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()


if __name__ =='__main__':
    pass

