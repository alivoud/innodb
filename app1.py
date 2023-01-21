from flask import Flask
import psutil
from flask import jsonify
from flask import request
import datetime
import mysql.connector



data = {}


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="retretTRD$56d$%^D45d6456d354534"
)

mycursor = mydb.cursor()

mycursor.execute("show variables like 'innodb%';")

myresult = mycursor.fetchall()

for x in myresult:
    data[str(x[0])] = str(x[1])
#	print(x[0] ,":" , x[1])





app = Flask(__name__)

@app.route("/" , methods=["GET"])






def hello_world():

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory()._asdict()



    # data = {
    #     "CPU": cpu_usage,
    #     "RAM": ram_usage,

    # }
    
    # data1 = [1,2,3,4]



    return jsonify(data)


if __name__ == '__main__':
    app.run(host="localhost", port=8001, debug=True)
