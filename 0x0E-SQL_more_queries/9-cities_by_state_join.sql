-- Show all the cities contained in  hbtn_0d_usa (db)
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
