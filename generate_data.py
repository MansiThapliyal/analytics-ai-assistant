import sqlite3, random
from faker import Faker

fake = Faker("en_IN")
conn = sqlite3.connect("rental.db")
c = conn.cursor()

c.execute("""CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY, city TEXT, region TEXT)""")
c.execute("""CREATE TABLE fleet (
    car_id INTEGER PRIMARY KEY, model TEXT, category TEXT,
    location_id INTEGER, daily_rate REAL)""")
c.execute("""CREATE TABLE rentals (
    rental_id INTEGER PRIMARY KEY, car_id INTEGER,
    start_date TEXT, end_date TEXT, total_amount REAL)""")

cities = [("Delhi","North"),("Mumbai","West"),("Bangalore","South"),
          ("Chennai","South"),("Kolkata","East"),("Pune","West")]
for i,(city,region) in enumerate(cities,1):
    c.execute("INSERT INTO locations VALUES (?,?,?)",(i,city,region))

models = [("Swift","Economy",1800),("City","Sedan",3200),
          ("Creta","SUV",4500),("Innova","SUV",5200),("i20","Economy",2100)]
for car_id in range(1,201):
    m = random.choice(models)
    c.execute("INSERT INTO fleet VALUES (?,?,?,?,?)",
              (car_id, m[0], m[1], random.randint(1,6), m[2]))

for rid in range(1,5001):
    start = fake.date_between("-12M","today")
    days = random.randint(1,10)
    car = random.randint(1,200)
    rate = c.execute("SELECT daily_rate FROM fleet WHERE car_id=?",(car,)).fetchone()[0]
    c.execute("INSERT INTO rentals VALUES (?,?,?,date(?, ?),?)",
              (rid, car, str(start), str(start), f"+{days} days", rate*days))

conn.commit(); conn.close()
print("Database created: rental.db")