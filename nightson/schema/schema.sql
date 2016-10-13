-- Enabling postgis extensions

-- Enable PostGIS (includes raster)
CREATE EXTENSION postgis;
-- Enable Topology
CREATE EXTENSION postgis_topology;
-- Enable PostGIS Advanced 3D
-- and other geoprocessing algorithms
-- sfcgal not available with all distributions
CREATE EXTENSION postgis_sfcgal;
-- fuzzy matching needed for Tiger
CREATE EXTENSION fuzzystrmatch;
-- rule based standardizer
CREATE EXTENSION address_standardizer;
-- example rule data set
CREATE EXTENSION address_standardizer_data_us;
-- Enable US Tiger Geocoder
CREATE EXTENSION postgis_tiger_geocoder;


CREATE TABLE Users(
  id INT PRIMARY KEY NOT NULL ,
  first_name VARCHAR(64) NOT NULL ,
  last_name VARCHAR(64) NOT NULL ,
  email VARCHAR(32) NOT NULL ,
  password VARCHAR(16) NOT NULL ,
  phone VARCHAR(12) ,
  location GEOGRAPHY(POINT,4326)
);


CREATE TABLE Events(
  id INT PRIMARY KEY NOT NULL ,
  name VARCHAR(64) NOT NULL ,
  start_time TIMESTAMP NOT NULL ,
  end_time TIMESTAMP NOT NULL ,
  location GEOGRAPHY(POINT,4326)
);

CREATE TABLE Sessions(
  user_id INT ,
  token VARCHAR (256) ,
  created_at TIMESTAMP ,
  expires_at TIMESTAMP ,
  FOREIGN KEY(user_id) REFERENCES Users(id)
);