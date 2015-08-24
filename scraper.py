#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import errno

driver = webdriver.PhantomJS()
driver.set_window_size(1200, 800)

# Contract: Expects a file in the same directory called urls.txt
def get_urls():
    urls = []
    file = open("urls.txt")

    for line in file:
        urls.append(line.replace("\n", ""))

    return urls

# Creates directory if it doesn't exist already.
# Careful of race conditions.
def create_folder(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def scrape_urls():
    artists = get_urls()

    for artist in artists:
        songs = []
        driver.get(artist)
        items = driver.find_elements_by_xpath("//div[@id='listAlbum']/a")
        for item in items:
            songs.append(item.get_attribute("href"))
        print songs


scrape_urls()

