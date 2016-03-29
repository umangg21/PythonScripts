import os,sys,glob
from tinytag import TinyTag
import shutil
fname="D:\Songs"   #first directory
dname1=os.chdir(fname)
songs1=glob.glob("*.mp3")
tags1=[]
list1={}
for file in songs1:
    m=TinyTag.get(file)
    list1[file]=m
    tags1.append([m.title,m.album,m.artist,m.filesize]);
    

sname="D:\Songs2"  #Second Directory
dname2=os.chdir(sname)
songs2=glob.glob("*.mp3")
tags2=[]
list2={}
for file in songs2:
    m=TinyTag.get(file)    
    list2[file]=m
    tags2.append([m.title,m.album,m.artist,m.filesize]);


search1=[]
search2=[]

for file in songs1:
    a=[list1[file].title,list1[file].album,list1[file].artist,list1[file].filesize];
    if a not in tags2:
        search1.append(file)      


for file in songs2:
    a=[list2[file].title,list2[file].album,list2[file].artist,list2[file].filesize];
    if a not in tags1:
        search2.append(file)

        
for file in search1:
    a=fname+"\\"+file
    b=sname
    shutil.copy2(a,b)

for file in search2:
    a=sname+"\\"+file
    b=fname
    shutil.copy2(a,b)

a=len(search1)+len(search2)
print(a,'songs successfully synced');
