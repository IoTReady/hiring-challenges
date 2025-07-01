### Assessment: Cold Chain Monitoring System

**Objective:** Simulate a cold chain monitoring system that tracks temperature data from sensors in different temperature zones across multiple locations, and then perform complex SQL queries to analyze the data.

#### Part 1: Database Design and Data Generation

1. **Database Design:**
   - Create an SQLite database with the following tables:
     - `Locations` (id INTEGER PRIMARY KEY, location_id TEXT, description TEXT)
     - `Temperature_Zones` (id INTEGER PRIMARY KEY, zone_name TEXT, location_id TEXT, FOREIGN KEY(location_id) REFERENCES Locations(id))
     - `Sensors` (id INTEGER PRIMARY KEY, sensor_id TEXT, zone_id TEXT, FOREIGN KEY(zone_id) REFERENCES Temperature_Zones(id))
     - `Readings` (id INTEGER PRIMARY KEY, sensor_id TEXT, timestamp DATETIME, temperature REAL, FOREIGN KEY(sensor_id) REFERENCES Sensors(id))

2. **Data Generation:**
   - Write a Python script that:
     - Creates 10 unique locations.
     - For each location, creates three temperature zones: Tropical, Chiller, and Freezer.
     - For each temperature zone, simulates one sensor.
     - Generates synthetic temperature readings every 30 seconds for one month (approximately 2,592,000 readings per sensor).
     - Ensure that the temperature values are realistic for each zone:
       - Tropical: 20°C to 35°C
       - Chiller: 0°C to 5°C
       - Freezer: -20°C to -5°C

#### Part 2: SQL Queries

After generating the data, candidates should write complex SQL queries to analyze the data. Here are some example queries:

1. **Average Temperature by Zone:**
   - Write a query to calculate the average temperature for each temperature zone across all locations for the entire month.

2. **Temperature Violations:**
   - Identify sensors that recorded temperatures outside the acceptable range for their respective zones and list the timestamps of these violations.

3. **Daily Summary:**
   - Create a query that summarizes the daily average temperature for each temperature zone in each location. The result should include the location ID, zone name, date, and average temperature.

4. **Location-Based Analysis:**
   - Write a query to find the location with the highest average temperature in the Tropical zone.

5. **Trend Analysis:**
   - Identify trends in temperature over time for each temperature zone. For example, calculate the percentage of readings that fall within the acceptable range for each zone.

6. **Anomaly Detection:**
   - Create a query to detect anomalies in the readings, such as sudden spikes or drops in temperature. Define what constitutes an anomaly (e.g., a change greater than a certain threshold).

7. **Correlation Analysis:**
   - Write a query to analyze the correlation between temperature readings in the Tropical zone and the Chiller zone across all locations.

#### Part 3: Testing and Documentation

- **Testing:**
  - Include unit tests for the Python data generation script to ensure that it populates the database correctly.
  - Provide sample outputs for the SQL queries to demonstrate expected results.

- **Documentation:**
  - Candidates should include a README file with instructions on how to set up the environment, run the data generation script, and execute the SQL queries.
  - Document the SQL queries, explaining the logic behind each one and any assumptions made.

#### Submission Guidelines

- Candidates must submit their code in a GitHub repository.
- The repository should include:
  - The Python script for data generation.
  - SQL scripts or a notebook for executing the queries.
  - A README file with setup instructions and documentation.
- Email to work@iotready.co
- **Important:** No GPT-generated code is allowed. Any submission found to contain AI-generated code will result in immediate disqualification.

This assessment will thoroughly evaluate the candidates' SQL skills, their ability to generate realistic data, and their understanding of database design, while also ensuring they adhere to the requirement of writing their own code.
