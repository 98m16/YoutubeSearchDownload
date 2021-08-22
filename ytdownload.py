#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:42:50 2021

@author: mischance
"""
import pafy # pip install pafy youtube-dl
import requests
from bs4 import BeautifulSoup
import re
import json


search = input(">> ").split(" ")
query = '+'.join(str(x) for x in search)
#query = "game+play"

file_names360 = dict()
file_names720 = []

def Search(query):
	r = requests.get(f"https://youtube.com/results?search_query={query}").text

	soup = BeautifulSoup(r, 'lxml')


	script = soup.find_all('script')[32]

	json_text = re.search('var ytInitialData = (.+)[,;]{1}', str(script)).group(1)
	json_data = json.loads(json_text)
	content = json_data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
	#print(content)
	i = 1
	for data in content:
		for key, value in data.items():
			for k, v in value.items():
				if (k=="title" and len(value["title"]) == 2) and "thumbnail" in value.keys():
					title = value["title"]["runs"][0]['text']
					print(f"{i}   Title: {title}")
					i+=1
				if k =="longBylineText"  and "runs" in value["longBylineText"]:	# Author
					print("Author: "+value["longBylineText"]["runs"][0]['text'])
				if k=="viewCountText":		# Nb Vues
					print("Vues: "+value["viewCountText"]["simpleText"])
				if k=="lengthText":	# Duration
					print("Duration: "+value["lengthText"]["accessibility"]["accessibilityData"]["label"])
				if k=="videoId" and len(v)==11:    # Video Id 
					title = value["title"]["runs"][0]['text']
					for number in range(len(value.keys())):
						file_names360[i] =  'https://youtube.com/watch?v='+v #p360
						
					print('\n')





#Playlist
def playlist_url(url):
	pass

#Video
def video_url(num):#url):
	"""
	result = pafy.new(url)
	bestmp4 = result.getbest(preftype="mp4")
	print (f"Downloading : {result.title}")
	bestmp4.download()
	print(f"{result.title} downloaded ;-)")
	"""
	global file_names
	for k, v in file_names360.items():
			for n in range(len(num)):
				try:
					if k==int(num[n]):
						result = pafy.new(file_names360[k])
						bestmp4 = result.getbest(preftype="mp4")
						print (f"Downloading : {result.title}")
						bestmp4.download()
						print(f"{result.title} downloaded ;-)")
				except:
					pass
	

#Audio
def audio_url(num):#url):
	"""
	result = pafy.new(url)
	bestmp3 = result.getbestaudio()
	print (f"Downloading : {result.title}")
	bestmp3.download()
	print(f"{result.title} downloaded ;-)")
	"""
	global file_names
	for k, v in file_names360.items():
			for n in range(len(num)):
				try:
					if k==int(num[n]):
						result = pafy.new(file_names360[k])
						bestmp3 = result.getbestaudio()
						print (f"Downloading : {result.title}")
						bestmp3.download()
						print(f"{result.title} downloaded ;-)")
				except:
					pass
	


# Downlad
def  Download():
	global file_names
	choice = input("Video(v) OR Audio(a) : ")
	if choice == "v" or choice =="V":
		number = input("Select the number of video(ex: 1,2,3) : ").split(",")
		audio_url(number)
		
	elif choice =="a" or choice=="A":
		number = input("Select the number of video(ex: 1,2,3) : ").split(",")
		video_url(number)
	else:
		print("Error !!!")
		Download()
	
# Main
def main():			
	Search(query)
	print("\n\n")
	Download()
	

main()
