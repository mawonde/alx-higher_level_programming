-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name -- Query to join cities and states
FROM cities
JOIN states ON cities.state_id = states.id;
