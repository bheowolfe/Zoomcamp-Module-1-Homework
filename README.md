# Zoomcamp-Module-1-Homework

## Question 1

    @bheowolfe ➜ /workspaces/Zoomcamp-Module-1-Homework (main) $ docker run -it --rm --entrypoint=bash python:3.13
    root@130b972453fb:/# pip -V
    pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

    the image  has pip 25.3



## Question 2

    db:5432

## Question 3

    ny_taxi=# SELECT COUNT(*) FROM tripdata WHERE lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01' AND trip_distance <= 1;

        count 
        -------
        8007

## Question 4

    ny_taxi=# SELECT 
        DATE(lpep_pickup_datetime),
        MAX(trip_distance) as longest_trip
    FROM tripdata
    WHERE trip_distance < 100
    GROUP BY DATE(lpep_pickup_datetime)
    ORDER BY longest_trip DESC
    LIMIT 1;

            date    | longest_trip 
        ------------+--------------
        2025-11-14 |        88.03

## Question 5

    ny_taxi=# SELECT 
        taxi_zone."Zone",
        SUM(tripdata.total_amount) as total_amount
    FROM tripdata 
    JOIN taxi_zone ON tripdata."PULocationID" = taxi_zone."LocationID"
    WHERE DATE(tripdata.lpep_pickup_datetime) = '2025-11-18'
    GROUP BY taxi_zone."Zone"
    ORDER BY total_amount DESC

        LIMIT 1;
            Zone        |   total_amount    
        -------------------+-------------------
        East Harlem North | 9281.919999999991

## Question 6

    

