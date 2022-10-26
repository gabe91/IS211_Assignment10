import sqlite3 as lite
import sys
#connect to database 

try:
    con = lite.connect("pets.db")

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS person;
        CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);
        INSERT INTO person (id, first_name, last_name, age ) VALUES (1, 'James', 'Smith', 41);
        INSERT INTO person (id, first_name, last_name, age ) VALUES (2, 'Diana', 'Greene', 23);
        INSERT INTO person (id, first_name, last_name, age ) VALUES (3, 'Sara', 'White', 27);
        INSERT INTO person (id, first_name, last_name, age ) VALUES (4, 'Williams', 'Gibson', 23);
        """)

    cur.executescript("""
        DROP TABLE IF EXISTS pet;
        CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Rusty', 'Dalmation', 4, 1);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Bella', 'Alaskan Malamute', 3, 0);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Max', 'Cocker Spaniel', 4, 1);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Rocky', 'Beagle', 7, 0);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (5, 'Rufus', 'Cocker Spanial', 1, 0);
        INSERT INTO pet (id, name, breed, age, dead) VALUES (6, 'Spot', 'Bloodhound', 2, 1); 
        """)

    cur.executescript("""
        DROP TABLE IF EXISTS person_pet;
        CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER);
        INSERT INTO person_pet (person_id, pet_id) VALUES (1, 1);
        INSERT INTO person_pet (person_id, pet_id) VALUES (1, 2);
        INSERT INTO person_pet (person_id, pet_id) VALUES (2, 3);
        INSERT INTO person_pet (person_id, pet_id) VALUES (2, 4);
        INSERT INTO person_pet (person_id, pet_id) VALUES (3, 5);
        INSERT INTO person_pet (person_id, pet_id) VALUES (4, 6);
        """)

    con.commit()

except lite.Error as e:
    if con:
        con.rollback()
    
    print("Error {}:".format(e.args[0]))
    sys.exit(1)

finally:
    if con:
        con.close()


    