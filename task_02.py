#!/usr/bin/env pytho
#-*- coding: utf-8 -*-
"""This will format an e mail."""


def prepare_email():
    appointments = [('Wiley', 'Monday October 5, 2015'), ('Big Daddy', 
                   'Tuesday, October 6, 2015')]
    form_letter = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'                                                                  
for values in prepare_email:
    form_letter.format()
print prepare_email
