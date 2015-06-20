import re
import urllib2
from BeautifulSoup import BeautifulSoup
import MySQLdb
from datetime import datetime
from pytz import timezone

'''
#This is to select DB and display the content

pro.execute("SELECT * FROM clients_client where id=%d;" %(client_id))
for row in pro.fetchall():
   hashtag = row[7]
'''

while True:
   db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="open123", 
                      db="openbox_dj") 

   client_id = 1
   pro = db.cursor()
   hashtag = 'cnn'
   url = 'https://www.facebook.com/hashtag/'+hashtag
   request = urllib2.Request(url)
   response = urllib2.urlopen(request)
   soup = BeautifulSoup(response)

   try:
      comment = soup.find('code').contents[0]
      image = BeautifulSoup(comment).findAll('img')[1].get('src')
      #urllib.urlretrieve(image, "pic.jpg")
      img = urllib2.urlopen(image)
      localFile = open('pic.jpg', 'wb')
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
   sql = "INSERT INTO clients_facebook \
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

   print image
   print now
   print "Success"
