# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:36:39 2022

@author: Mitch.Burke
"""

# Install spotipy and lyricsgenius libraries
# pip install spotipy 
# pip install lyricsgenius

# Import necessary libraries
import lyricsgenius

# Gain access to the api
genius = lyricsgenius.Genius("me-MXmuCTyJWDZ1MmERAAyivlY61EvPSD7KX2lBynV60vCOlEheYc6HVfPGlQ0ru")

########## EXAMPLE FROM DOCS
#song = genius.search_song("All I Want for Christmas", artist.name)
#print(song.lyrics)

########## GRAB SONGS FOR PARTICULAR ARTIST
# Set variables for access token, artist and max_songs
art = 'Pearl Jam'
max_sngs = 7

# Use api to pull artists and lyrics for their songs
artist = genius.search_artist(art, max_songs = max_sngs, sort = "title")

# Print results
print(artist.songs)


########## GRAB LYRICS FOR A PARTICULAR SONG
song = genius.search_song("Lady Madonna", "The Beatles")

#print(song.lyrics)


########## Loop through song list & save lyrics for all songs in new list

# Create song list & empty list for results
song_list = [('A Letter from Janelle', 'Chiodos'), ('Hey Jude', 'The Beatles'), ('Empire State of Mind', 'Jay-Z')]
res_list = []

# Loop over the song and artist tuples to pull song lyrics for each tune & append to result list
for sng, atst in song_list:
    song = genius.search_song(sng, atst)
    res_list.append(song.lyrics)

# Print each lyric set from results list
[print(lyric) for lyric in res_list]