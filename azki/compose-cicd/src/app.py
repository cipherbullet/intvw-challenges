from flask import request
from flask import jsonify
from flask import Flask
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='mysql',
                                         database='mydatabase',
                                         user='candidate',
                                         password='challange')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("**************** Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("**************** You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

app = Flask(__name__)

@app.route("/ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
