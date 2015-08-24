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

def get_artist_from_url(url):
    return url.split("/")[-1][0:-5]

def scrape_song_lyrics(song_url):
    pass

def scrape_song_urls(driver):
    artists = get_urls()
    songs = {}

    for artist in artists:
        artist_name = get_artist_from_url(artist)
        temp_songs = []
        driver.get(artist)
        items = driver.find_elements_by_xpath("//div[@id='listAlbum']/a")
        for item in items:
            temp_songs.append(item.get_attribute("href"))

        # Add to return dict keyed by artist if content was found
        if (len(temp_songs) > 0):
            songs[artist_name] = temp_songs

    return songs

def scrape_lyrics(driver):
    # Songs is a dict of artist to array of URLs of their songs.
    songs = scrape_song_urls(driver)
    for artist in songs:
        print artist

create_folder("drake")
scrape_lyrics(driver)
