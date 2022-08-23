import seeed_dht
import precursor_database as pc_db
from grove_dht import Dht # from a custom made grovepi-based library import our needed class
from time import sleep # we need to use the sleep function to delay readings
from datetime import datetime  # that's for printing the current date
import consts as cn

def main():

    dht_pin = cn.SENSOR_PIN # use Digital Port 4 found on GrovePi
    dht_sensor = Dht(dht_pin) # instantiate a dht class with the appropriate pin
    dht_sensor.start() # start collecting from the DHT sensor

    try:
        print("TEMP SENSOR - ALLOW TIME FOR BUFFER TO FILL...")
        while True:
            temperature, humidity = dht_sensor.feedMe() # try to read values
            if(temperature is None or humidity is None):
                sleep(5)
            else:
                humidity = format(humidity, '.0f')
                temperature = format(temperature, '.0f')
                result, msg = pc_db.insertTempHumi(cn.TABLE_NAME, temperature, humidity)
                if(result == False):
                    print(msg)
                else:
                    print("Added to DB")
                print(cn.SENSOR_LOCATION_NAME + ":: Humidity(%)", humidity, " Temperature(C)", temperature)
                sleep(5) # wait around 800 ms before the next iteration
    except KeyboardInterrupt:
        dht_sensor.stop() # stop gathering data

            
if __name__ == "__main__":
    main()



