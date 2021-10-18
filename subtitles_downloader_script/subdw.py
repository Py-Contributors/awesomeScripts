#!/bin/python
'''
Subtitle Searcher


'''
import requests
from bs4 import BeautifulSoup
import os,sys,re
import argparse
import tkinter as tk
from tkinter import filedialog
import zipfile


class podnapsi():
	titledict={}
	finalsoupdict={}
	def __init__(self):
		#self.headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
		sub_name=None
		queries=None
		movie_type=None
		seasons=None
		year=None
		self.titledict={}
		self.finalsoupdict={}


	def get_sublist(self,subname,episode,season,*args,**kwargs):
		website="https://www.podnapisi.net/subtitles/search/?movie_type=&episodes="+episode+"&year=&keywords="+subname+"&seasons="+season+"&type="
		#website="https://www.podnapisi.net/subtitles/search/?keywords="+subname
		#queries={'episodes':episode,'movie_type':movie_type,'season':seasons,'year':year}
		#queries={'episodes':episode,'season':season}
		#print(queries)
		try:
			podpage=requests.get(website)
			#print(podpage.url)
			podsoup=BeautifulSoup(podpage.text,"lxml")
			#print(podsoup)
			finalsoup=podsoup.find_all('span',{'class':'release'})
			finalsoup1=podsoup.find_all('a',{"alt":"Download subtitles."})#Finds the corresponding links
			#print(finalsoup1)
			self.titledict={}
			self.finalsoupdict={}
			for number,title in enumerate(finalsoup,start=1):
				#print(number,title['href'])
				self.titledict[number]=title['title']
				print(number,title['title'])
			if  len(self.titledict) == 0:
				print("No subtitles found\n Exiting...")
				sys.exit(1)
			for number,href in enumerate(finalsoup1,start=1):
				self.finalsoupdict[number]=href['href']
			if  len(self.finalsoupdict)==0:
				print("No subtitles found\n Exiting...")
				sys.exit(1)
		except ConnectionError :
			print("Error")
	def download_sub(self,path,subnum,*args,**kwargs):
		self.root=tk.Tk()
		self.root.withdraw()
		download_link="https://www.podnapisi.net"+self.finalsoupdict[subnum]
		def_title=self.titledict[subnum]

		if not path :
			path=filedialog.asksaveasfilename(defaultextension=".zip",filetypes=(("Zip","*.zip"),("all files","*.*")))
			if  not path :
				path=os.getcwd()+"/"+def_title
		while True:
			try:
				subdownload=requests.get(download_link,timeout=0.5)
			except requests.exceptions.Timeout:
				print("\n Retrying")
			else:
				break

		print("DIRECTORY",path)
		if subdownload.status_code == 200:
			with open(path,"wb") as req_file:
				req_file.write(subdownload.content)
				with zipfile.ZipFile(path,"r") as zip_ref:
					zip_ref.extractall(os.getcwd()+"/")
					os.remove(path)
#https://www.podnapisi.net/subtitles/en-quantico-2015-S02E02/L8RB/download
def main():
	try:
		ne=podnapsi()
		subparse=argparse.ArgumentParser(prog="main.py")
		subparse.add_argument('subtitle_name',metavar="subtitle name",help="Specify the subtitle name",type=str)
		subparse.add_argument('season_num',metavar="Season number",help="Specify the season number",type=str)
		subparse.add_argument('episode_num',metavar="Episode number",help="Specify the episode number",type=str)
		subparse.add_argument('-d','--directory',metavar="Directory",help="Specify the Directory",type=str)
		if len(sys.argv)<2:
			print("\rUse the -h or --help option with main.py ")
			subparse.exit(1)
		parsedopt=subparse.parse_args()
		sub_name=parsedopt.subtitle_name.replace(" ",'+')
		sub_episode=parsedopt.episode_num
		sub_season=parsedopt.season_num
		sub_directory=parsedopt.directory
		ne.get_sublist(sub_name,sub_episode,sub_season)
		while True:
			try:
				sub_number=int(input("\nPlease enter the subtitle number you want to download=> "))
			except ValueError:
				print("Invalid input")
			else:
				break
		ne.download_sub(sub_directory,sub_number)
	except KeyboardInterrupt :
		print("\nExited forcefully")
if __name__=="__main__":
    main()
