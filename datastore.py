import sys
import mysql.connector as mariadb
import logging
import json
username = 'web'
password = '00039jp3jcx'
database = 'fridge'
try:
      mariadb_connection = mariadb.connect(user=username, password = password, database=database)
except:
      print("Error:123")
#Items = '[{'name':'Hussam','date':'2010-03-11','quantity':'2'}]'

def insertitem(Item):
      try:
              cursor = mariadb_connection.cursor()
              query = ("INSERT INTO item (itemname,quantity,expdate)" "VALUES (%s,%s,%s)")
              decode = json.loads(Item)
              data = (decode[0]['name'], decode[0]['quantity'], decode[0]['date'])
              cursor.execute(query,data)
              mariadb_connection.commit()
      except mariadb.Error as error:
              logging.error("Error: {}".format(error))
              return False
      except IOError as e:
              logging.error("I/O error({0}): {1}".format(e.errno,e.strerror))
              return Fasle
      except:
              logging.error("Unexpected Error:",sys.exc_info()[0])
              return False
      cursor.close()


def getitem(item):
        render = ""
        try:
                cursor = mariadb_connection.cursor()
                query = "SELECT * FROM fridge.item Where itemname = '%s'" %(item)
                cursor.execute(query)
                output = cursor.fetchall()
                render = output
        except:
                logging.error("Unexpected Error:",sys.exc_info()[0])
                return False
        cursor.close()
        return render

print(getitem('hus'))
