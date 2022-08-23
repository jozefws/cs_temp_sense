import mysql.connector
import consts as cn


def conn():
    try:
        db = mysql.connector.connect(
            host="precursor.cs.nott.ac.uk",
            user="rasbpi_entry",
            password=cn.MYSQL_ENTRY_PWD,
            database="CS_SERVER_MONITORING",
            port="3306"
        )
        cursor = db.cursor(buffered=True)
        return db, cursor
    except Exception as e:
        return False, "MYSQL Exception in precursor_database.py:conn - " + str(e)
        
def insertTempHumi(tablename, temp, humi):
    db, cursor = conn()
    if(db == False):
        print(cursor)
    try:
        sql = "INSERT INTO "+tablename+" (temperature, humidity) VALUES (%s, %s)"
        cursor.execute(sql, (temp, humi))
        db.commit()
        if(cursor.rowcount > 0):
            return True, cursor.lastrowid
        else: 
            return False, "Unable to add data to " + tablename
    except Exception as e:
        return False, "Exception in precursor_database.py:insertTempHumi - " + str(e)

