import feedparser
import re
import urllib2
from BeautifulSoup import BeautifulSoup
import MySQLdb
from datetime import datetime
from pytz import timezone


while True:
   db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="open123", 
                      db="openbox_dj") 

   client_id = 1
   pro = db.cursor()
   hashtag = "cnn"

   RSS = "http://widget.websta.me/rss/tag/"+hashtag

   d = feedparser.parse(RSS)

   html = d['entries'][0]['description']

   soup = BeautifulSoup(html)
   try:
      image = soup.findAll('img')[1].get('src')
      img = urllib2.urlopen(image)
      localFile = open('insta.jpg', 'wb')
      localFile.write(img.read())
      localFile.close()
   except:
      image = "None"
      pass

   fmt = "%Y-%m-%d %H:%M:%S"
   now_utc = datetime.now(timezone('UTC'))
   now_india = now_utc.astimezone(timezone('Asia/Kolkata'))
   now = now_india.strftime(fmt)

   read = 0
   sql = "INSERT INTO clients_instagram \
            (content_pic, time, hashtag, client_id, read) \
            VALUES('%s','%s','%s','%d','%d')" %\
            (image, now, hashtag, client_id, read)
   db.set_character_set('utf8')
   pro.execute('SET NAMES utf8;')
   pro.execute('SET CHARACTER SET utf8;')
   pro.execute('SET character_set_connection=utf8;')   

   try:
      pro.execute(sql)
      db.commit()
   except:
      db.rollback()

   db.close()
   print (image)
   print "Success"    
