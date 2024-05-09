COPY stations(
              station_id,
              station_name,
              geog
             )
FROM 'db/data/stations.csv'
DELIMITER ','
CSV HEADER;

COPY trips(
           trip_id,
           departure_station_id,
           return_station_id,
           departure_year,
           departure_month,
           departure_day,
           departure_hour,
           departure_min,
           departure_weekday,
           return_year,
           return_month,
           return_day,
           return_hour,
           return_min,
           return_weekday,
           distance_m,
           duration_min,
           speed_avg_km_h,
           air_temperature_deg_c
          )
FROM 'db/data/trips.csv'
DELIMITER ','
CSV HEADER;
