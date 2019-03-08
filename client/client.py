import mysql.connector
import json
import urllib.request
from mysql.connector import errorcode

# variables
URL = "http://territorial-valencia.gestiondecolasdeespera.com/appointment/api/appointments/"
DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWD = "root"
DATABASE_NAME = "qsystem"


try:
	print("triying to connect cli")
	cnx = mysql.connector.connect(user=DATABASE_USER, 
								  password=DATABASE_PASSWD,
                              	  host=DATABASE_HOST, 
								  port=3306,
                                  database=DATABASE_NAME)
	print("connected")
	# Recuperamos los elementos del servidor

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

else:
	cursor = cnx.cursor()
	# INSERT INTO `qsystem`.`advance` (`id`, `service_id`, `advance_time`) VALUES ('1111', '2', '2018-08-10 12:00:00');
	response = json.load(urllib.request.urlopen(URL))
	for element in response:
		advance_data = (element['dni'], element['service_id'], element['fecha'] + " "+ element['hora'] ,element['service_id'], element['fecha'] + " "+ element['hora']) 
		print(advance_data)
		print (element['fecha'])
		print (element['service_id'])
		print (element['hora'])
		print (element['email'])
		advance_query = ("INSERT INTO advance (id, service_id, advance_time) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE service_id=%s, advance_time=%s")
		print (advance_query)
		cursor.execute(advance_query, advance_data)
	cnx.commit()
	cursor.close()


cnx.close()