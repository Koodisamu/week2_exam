import psycopg2 as psycopg2
from config import config
from datetime import datetime
    
# 5.Function to insert data into the flight table

def insert_row(flight_number = str, departure_time = datetime, arrival_time = datetime, departure_airport = str, destination_airport = str):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        INSERT INTO flights
        (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
        VALUES (%s, %s, %s, %s, %s);
        """
        data = (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
        cursor.execute(SQL,data)
        con.commit()
        cursor.close()
        print('Data inserted successfully')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 6.Function to select all data from the flight table ordered by departure time

def select_and_order():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT *FROM flights ORDER BY departure_time;'
        cursor.execute(SQL)
        row = cursor.fetchall()
        for row in row:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 9. Function that prints flights rows ordered by airline name

def select_flights_by_airline():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        SELECT f.flight_number, f.departure_time, f.arrival_time, f.departure_airport, f.destination_airport, a.name AS airlane
        FROM flights f
        JOIN airline a
        ON f.id = a.flights_id
        ORDER BY a.name;
        """
        cursor.execute(SQL)
        row = cursor.fetchall()
        for row in row:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# 10. Function that removes a flight by id

def remove_flight(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'DELETE FROM flights WHERE id = %s;'
        cursor.execute(SQL, (id,))
        con.commit()
        cursor.close()
        print('Data deleted successfully')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def main():
    # insert_row('AB123', datetime(2024,12,17,5,45), datetime(2024,12,17,7,10), 'BGY', 'PMO')
    # insert_row('AB456', datetime(2024,12,22,13,20), datetime(2024,12,22,18,10), 'RKV', 'HEL')
    # insert_row('AB789', datetime(2025,1,1,19), datetime(2025,1,1,22,25), 'LHR', 'BGY')
    # select_flights_by_airline()
    remove_flight(4)

if __name__ == '__main__':
    main()