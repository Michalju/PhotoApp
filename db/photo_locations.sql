DROP TABLE IF EXISTS photos;
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
    description TEXT,
    visited BOOLEAN,
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE photos(
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    mine BOOLEAN,
    location_id INT REFERENCES locations(id) ON DELETE CASCADE,
    camera_model VARCHAR(255),
    lens_model VARCHAR(255),
    aperture VARCHAR(255),
    iso VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255)
);