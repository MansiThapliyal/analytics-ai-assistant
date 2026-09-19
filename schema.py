SCHEMA = """
Tables in SQLite database 'rental.db':

locations(location_id, city, region)
fleet(car_id, model, category, location_id, daily_rate)
rentals(rental_id, car_id, start_date, end_date, total_amount)

Notes:
- dates are TEXT in YYYY-MM-DD format
- fleet.location_id joins to locations.location_id
- rentals.car_id joins to fleet.car_id
- category values: Economy, Sedan, SUV
"""