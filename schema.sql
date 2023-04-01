CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    sightings INTEGER
);

CREATE TABLE sightings (
    id SERIAL PRIMARY KEY,
    species TEXT,
    location TEXT,
    date DATE,
    user_id INTEGER REFERENCES users
);