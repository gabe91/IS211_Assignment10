import sqlite3 as lite 


con = lite.connect("pets.db")
cur = con.cursor()

def print_person(person_id:int, cur):
    try:
        data = cur.execute(f"SELECT * FROM person where id={person_id}")
        data = list(data)
        print(f"{data[0][1]}, {data[0][2]}, {data[0][3]} years old")
        pet_id_sql=cur.execute(f"SELECT * FROM person_pet where person_id{person_id}")
        pet_ids = list(pet_id_sql)
        for i in range(len(pet_ids)):
            pet_data = cur.execute(f"SELECT * FROM pet where id={pet_ids[i][1]}")
            pet_data = list(pet_data)
            if (pet_data != []):
                if (pet_data[0][4] == 0):
                    print(f"{data[0][1]} {data[0][2]} owns {pet_data[0][1]}, a {pet_data[0][2]}, that is {pet_data[0][3]} years old.")
                else:
                    print(f"{data[0][1]} {data[0][2]} owns {pet_data[0][1]}, a {pet_data[0][2]}, that is {pet_data[0][3]} years old.")
    except:
        print("Error! The Person ID is not found!")


while True:
    person_id = input("Enter person id number: ")
    if (person_id != "a1"):
        person_id = int(person_id)
        print_person(person_id, cur)
    else:
        break


