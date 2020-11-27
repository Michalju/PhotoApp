DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;

CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent_id INT REFERENCES continents(id) ON DELETE CASCADE
);
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    descirption TEXT,
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);