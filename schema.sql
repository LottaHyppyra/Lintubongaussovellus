CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    admin_rights BOOLEAN,
    sightings INTEGER
);

CREATE TABLE sightings (
    id SERIAL PRIMARY KEY,
    species TEXT,
    location TEXT,
    date DATE,
    user_id INTEGER REFERENCES users
);

CREATE TABLE species (
    id SERIAL PRIMARY KEY,
    latin_name TEXT,
    name TEXT,
    family_id INTEGER REFERENCES family
);

CREATE TABLE family (
    id SERIAL PRIMARY KEY,
    name TEXT
);