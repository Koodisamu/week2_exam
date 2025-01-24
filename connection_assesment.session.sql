-- #1. Create a database named 'assesment'

CREATE DATABASE assesment;

-- #2. Create a table named 'flights' with the following columns:

CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  flight_number VARCHAR(5) NOT NULL,
  departure_time TIMESTAMP NOT NULL,
  arrival_time TIMESTAMP NOT NULL,
  departure_airport VARCHAR(3) NOT NULL,
  destination_airport VARCHAR(3) NOT NULL
);

-- #3. Adding 3 rows to the 'flights' table

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
VALUES ('AY123', '2024-10-27 12:55', '2024-10-27 14:35', 'HEL', 'LHR');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
VALUES ('AY456', '2024-11-02 17:00', '2024-11-03 00:25', 'LHR', 'DXP');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
VALUES ('AY789', '2024-12-15 08:00', '2024-12-15 11:40', 'BGY', 'HEL');

-- #7. Create a table named 'airline' with the following columns:

CREATE TABLE airline (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  flights_id INT NOT NULL,
  CONSTRAINT fk_flights
  FOREIGN KEY (flights_id) REFERENCES flights (id)
  ON DELETE CASCADE
);

-- #8. Adding 6 rows to the 'airline' table to match the 6 rows in the 'flights' table

INSERT INTO airline (name, flights_id)
VALUES ('Finnair', 1);

INSERT INTO airline (name, flights_id)
VALUES ('Emirates', 2);

INSERT INTO airline (name, flights_id)
VALUES ('Ryanair', 3);

INSERT INTO airline (name, flights_id)
VALUES ('Wizz Air', 4);

INSERT INTO airline (name, flights_id)
VALUES ('Finnair', 5);

INSERT INTO airline (name, flights_id)
VALUES ('Ryanair', 6);