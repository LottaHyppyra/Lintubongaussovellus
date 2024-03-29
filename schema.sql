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
    user_id INTEGER REFERENCES users,
    visible BOOLEAN
);

CREATE TABLE species (
    id SERIAL PRIMARY KEY,
    latin_name TEXT,
    name TEXT,
    family TEXT
);

CREATE TABLE family (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE followed_species (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    species TEXT,
    UNIQUE (user_id, species)
)