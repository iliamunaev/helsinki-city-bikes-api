-- Enable PostGIS extension if it's not already enabled
CREATE EXTENSION IF NOT EXISTS postgis;

-- Create stations table
CREATE TABLE IF NOT EXISTS stations (
    station_id INTEGER PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    geog GEOGRAPHY(Point) NOT NULL
);

-- Create indexes for the stations table
CREATE UNIQUE INDEX IF NOT EXISTS stations_name_idx ON stations (station_name);
CREATE INDEX IF NOT EXISTS stations_geog_idx ON stations USING GIST(geog);

-- Create trips table with foreign key constraints
CREATE TABLE IF NOT EXISTS trips (
    trip_id INTEGER PRIMARY KEY,
    departure_station_id INTEGER NOT NULL REFERENCES stations(station_id) ON DELETE RESTRICT,
    return_station_id INTEGER NOT NULL REFERENCES stations(station_id) ON DELETE RESTRICT,
    departure_year INTEGER,
    departure_month VARCHAR(20),
    departure_day INTEGER,
    departure_hour INTEGER,
    departure_min INTEGER,
    departure_weekday VARCHAR(10),
    return_year INTEGER,
    return_month VARCHAR(20),
    return_day INTEGER,
    return_hour INTEGER,
    return_min INTEGER,
    return_weekday VARCHAR(10),
    distance_m INTEGER,
    duration_min INTEGER,
    speed_avg_km_h FLOAT,
    air_temperature_deg_c FLOAT
);

-- Create indexes for the trips table to enhance query performance
CREATE UNIQUE INDEX IF NOT EXISTS trips_departure_station_id_idx ON trips (departure_station_id);
CREATE INDEX IF NOT EXISTS trips_departure_year_idx ON trips (departure_year);
CREATE INDEX IF NOT EXISTS trips_departure_month_idx ON trips (departure_month);
CREATE INDEX IF NOT EXISTS trips_departure_day_idx ON trips (departure_day);
CREATE INDEX IF NOT EXISTS trips_departure_hour_idx ON trips (departure_hour);
CREATE INDEX IF NOT EXISTS trips_departure_weekday_idx ON trips (departure_weekday);

CREATE UNIQUE INDEX IF NOT EXISTS trips_return_station_id_idx ON trips (return_station_id);
CREATE INDEX IF NOT EXISTS trips_return_year_idx ON trips (return_year);
CREATE INDEX IF NOT EXISTS trips_return_month_idx ON trips (return_month);
CREATE INDEX IF NOT EXISTS trips_return_day_idx ON trips (return_day);
CREATE INDEX IF NOT EXISTS trips_return_hour_idx ON trips (return_hour);
CREATE INDEX IF NOT EXISTS trips_return_weekday_idx ON trips (return_weekday);

CREATE INDEX IF NOT EXISTS trips_distance_m_idx ON trips (distance_m);
CREATE INDEX IF NOT EXISTS trips_duration_min_idx ON trips (duration_min);
CREATE INDEX IF NOT EXISTS trips_speed_avg_km_h_idx ON trips (speed_avg_km_h);
CREATE INDEX IF NOT EXISTS trips_air_temperature_deg_c_idx ON trips (air_temperature_deg_c);
