#!/usr/bin/python

import os
import errno
from bs4 import BeautifulSoup
import urllib2

URL_FILE = "urls.txt"

# Params : urls_path, the path of the file containing urls you want to read.
# Returns: Array of parsed urls.

def get_urls(urls_path):
    urls = []
    file = open(urls_path)
    # Read each line and append it to the array urls, minus the newline char
    for line in file:
        urls.append(line.replace("\n", ""))

    return urls

# Description: Creates directory if it doesn't exist already.
#            : Includes checking for race conditions (raises exception).
# Params     : The path you want the folder to be at.
# Returns    : The path.

def create_folder(path):
    print "Creating folder: " + path

    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    return path

# Description: Creates song file in the directory of the artist with lyrics.
# Params     : song_text (the lyrics)
#            : artist_path (the path of the artist's folder)
#            : song_name (the extracted name of the song)
# Returns    : the path to the song

def create_file(artist_path, song_name, song_text):
    print "Creating file: " + artist_path + " " + song_name

    # Function decides for us whether to use "/" or "\".
    path = os.path.join(artist_path, song_name + ".txt")
    # Good practice to use "with" when dealing with file objects. Terse and
    # closes file properly.
    with open(path, "w") as song_file:
        # TODO: Figure out if BeautifulSoup returns a string or a list of
        # strings
        song_file.write(song_text)

    return path

# Description: Extracts name of artist/song from URL.
# Params     : url to extract data from
# Returns    : File name (not including extension).

def get_name_from_url(url):
    return url.split("/")[-1][0:-5]

# Description: Gets song text from song url.
# Params     : song url and relevant artist path.
# Returns    : song lyrics.

def scrape_song_lyrics(song_url, artist_path):
    print "Scraping song lyrics: " + song_url

    song_name = get_name_from_url(song_url)
    soup = BeautifulSoup(urllib2.urlopen(song_url).read())
    song_text = soup.get_text()
    print song_text

    return song_text

# Description: Scrapes lyrics from a list of urls of artists.
# Params: List of artist URLs
# Returns: Nothing

def scrape_lyrics(artist_urls):
    for artist in artists:
        artist_name = get_name_from_url(artist)
        print "Artist: " + artist_name
        create_folder(artist_name)
        temp_songs = []
       # items = driver.find_elements_by_xpath("//div[@id='listAlbum']/a")
        for item in items:
            print "Found item"
            url = item.get_attribute("href")
            if url != None:
                scrape_song_lyrics(url, artist_name)

        # Add to return dict keyed by artist if content was found
        if (len(temp_songs) > 0):
            songs[artist_name] = temp_songs
