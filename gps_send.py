import pyrebase
import serial
import pynmea2

firebaseConfig={
"apiKey": "",
 "authDomain": "<>.firebaseapp.com",
 "databaseURL": "https://<>.firebaseio.com",
 "projectId": "<>",
 "storageBucket": "<>.appspot.com",
 "messagingSenderId": "<>",
 "appId": "1:<>"

    }

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                print(gps)
                data = {"LAT": lat, "LNG": lng}
                db.update(data)
                print("Data sent")
