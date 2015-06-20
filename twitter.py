import re
import urllib2
from BeautifulSoup import BeautifulSoup
import MySQLdb
from datetime import datetime
from pytz import timezone

#This is for renewing the IP
while True:
   db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="open123", 
                      db="openbox_dj") 

   client_id = 1
   #This is to select DB and display the content
   pro = db.cursor()
   '''
   pro.execute("SELECT * FROM clients_client where id=%d;" %(client_id))
   for row in pro.fetchall():
      hashtag = row[7]
   '''
   hashtag = 'cnn'
   url = 'https://twitter.com/hashtag/'+hashtag
   try:
      response = request(url)
   except:
      request = urllib2.Request(url)
      response = urllib2.urlopen(request)

   soup = BeautifulSoup(response)

   try:
      image_tag = 'a'
      image_css = 'class'
      image_st_name = 'media media-thumbnail twitter-timeline-link media-forward is-preview '
      image = soup.find(image_tag, {image_css: image_st_name})['data-resolved-url-large'].encode("utf-8")
      img = urllib2.urlopen(image)
      localFile = open('twit.jpg', 'wb')
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

   sql = "INSERT INTO clients_twitter \
            (content_pic, time, hashtag, client_id, `read`) \
            VALUES('%s','%s','%s','%d','%d')" %\
            (image, now, hashtag, client_id, read)
   
   try:
      pro.execute(sql)
      db.commit()
   except:
      db.rollback()
   
   db.close()

   print image
   print "Success"
