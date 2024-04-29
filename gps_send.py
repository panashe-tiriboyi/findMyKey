import pyrebase
import serial
import pynmea2

firebaseConfig={
"apiKey": "AIzaSyAjIHDM9LAPrUgHtzr0z5aGTCDOHRVXDu4",
 "authDomain": "findmykey-70c77.firebaseapp.com",
 "databaseURL": "https://findmykey-70c77-default-rtdb.firebaseio.com",
 "projectId": "findmykey-70c77",
 "storageBucket": "findmykey-70c77.appspot.com",
 "messagingSenderId": "202383497778",
 "appId": "1:202383497778:web:aae3125af933726419ba2b"

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