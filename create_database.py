#Bikin database

 

import mysql.connector

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password=""

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Buat database

db_cursor.execute("CREATE DATABASE UAS_BIG_DATA")

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()