#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import errno

def set_up_driver(width = 1200, height = 800):
    driver = webdriver.PhantomJS()
    driver.set_window_size(width, height)
    return driver

def tear_down_driver(driver):
    driver.quit()

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

def get_name_from_url(url):
    return url.split("/")[-1][0:-5]

def scrape_song_lyrics(driver, song_url):
    print song_url
    driver.get(song_url)
    # Wait until all elements have loaded (max 10 seconds).
    song_text = ""
    try:
        song_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(By.XPATH, "/html/body/div[3]/div/div[2]/div[6]")
        )
    finally:
        return song_text

def scrape_lyrics(driver):
    artists = get_urls()
    songs = {}

    for artist in artists:
        artist_name = get_name_from_url(artist)
        create_folder(artist_name)
        temp_songs = []
        driver.get(artist)
        items = driver.find_elements_by_xpath("//div[@id='listAlbum']/a")
        driver.implicitly_wait(10)
        for item in items:
            url = item.get_attribute("href")
            if url != None:
                scrape_song_lyrics(driver, url)

        # Add to return dict keyed by artist if content was found
        if (len(temp_songs) > 0):
            songs[artist_name] = temp_songs

    tear_down_driver(driver)
    return songs

scrape_lyrics(set_up_driver())
