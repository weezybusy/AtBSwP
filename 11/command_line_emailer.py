#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a program that takes an email address and string of text on the command
# line and then, using Selenium, logs into your email account and sends an email
# of the string to the provided address. (You might want to set up a separate
# email account for this program.)
# 
# This would be a nice way to add a notification feature to your programs.
# You could also write a similar program to send messages from a Facebook or
# Twitter account.
# 
# My version doesn't use command line arguments because I think it's
# inconvenient, at least for me.

from selenium import webdriver
import re
import sys
import time

def is_valid(email):
    if re.match(r'[\w.%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,4}', email):
        return True
    return False


def main():

    while True:
        email = input('Send to: ')
        if not is_valid(email):
            print('Seems like you\'ve entered invalid email address.')
            continue
        break
    subject = input('Subject: ')
    message = input('Message: ')


    try:
        driver = webdriver.Firefox()
        driver.get('https://accounts.google.com/ServiceLogin#identifier')
        login = driver.find_element_by_id('Email')
        login.send_keys('weezybusybot')
        driver.find_element_by_id('next').click()
        driver.implicitly_wait(3)
        password = driver.find_element_by_id('Passwd')
        password.send_keys('Vito1130Bot')
        driver.find_element_by_id('signIn').click()
        driver.find_element_by_xpath('//a[@title="Google apps"]').click()
        driver.find_element_by_id('gb23').click()
        driver.find_element_by_xpath('//div[@class="T-I J-J5-Ji T-I-KE L3"]').click()
        driver.implicitly_wait(3)
        to = driver.find_element_by_id(':7j')
        to.send_keys(email)
        subj = driver.find_element_by_id(':73')
        subj.send_keys(subject)
        time.sleep(1)
        text = driver.find_element_by_id(':88')
        text.send_keys(message)
        driver.find_element_by_id(':6t').click()
        driver.quit()
        print('Message has been sent.')
    except:
        print('Sorry, something went wrong :(')
        sys.exit(1)


if __name__ == '__main__':
    main()
