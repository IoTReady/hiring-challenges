### Cold Chain Monitoring System Challenge

Hey! We'd like you to build a system that monitors temperature sensors in cold storage facilities - think warehouses with different temperature zones like freezers, chillers, and regular storage areas.

**What you'll build:**
A simulation that generates realistic sensor data and then queries it to find interesting patterns, violations, and trends.

**Tech stack:**
- Use **Bun** as your JavaScript runtime (not Node.js - we want to see you work with Bun!)
- Stick to **Bun's built-in libraries** only (`bun:sqlite`, `bun:test`)
- No external npm packages for the core functionality - let's see what you can do with just Bun's native tools

### Part 1: Set Up the Database and Generate Data

**1. Design your database schema**

Create an SQLite database with these tables:
- `Locations` - where the warehouses are (id, location_id, description)
- `Temperature_Zones` - different zones in each location (id, zone_name, location_id)
- `Sensors` - one sensor per zone (id, sensor_id, zone_id)
- `Readings` - the actual temperature data (id, sensor_id, timestamp, temperature)

Make sure your foreign keys are set up correctly so everything connects properly.

**2. Generate realistic data**

Write a script that creates:
- 10 different warehouse locations
- 3 temperature zones in each location: **Tropical** (normal storage), **Chiller** (refrigerated), and **Freezer** (frozen storage)
- 1 sensor per zone
- Temperature readings every 30 seconds for a full month (that's roughly 2.6 million readings per sensor - yeah, it's a lot!)

**Temperature ranges** (keep it realistic):
- Tropical: 20°C to 35°C
- Chiller: 0°C to 5°C
- Freezer: -20°C to -5°C


### Part 2: Write SQL Queries to Analyze the Data

Write queries to answer these questions:

**1. Average Temperature by Zone**
What's the average temperature in each zone type across all locations for the entire month?

**2. Temperature Violations**
Find all the times when sensors recorded temperatures outside their acceptable ranges. When did it happen? Which sensors?

**3. Daily Summary**
Create a daily report showing the average temperature for each zone in each location. Make it easy to read with location ID, zone name, date, and average temp.

**4. Location-Based Analysis**
Which warehouse location runs the hottest in the Tropical zone?

**5. Trend Analysis**
What percentage of readings actually stayed within the acceptable range for each zone type? Are things running smoothly or are there issues?

**6. Bonus: Anomaly Detection**
Detect sudden temperature spikes or drops. You define what counts as an anomaly (maybe a change greater than 5°C between readings?). Document your reasoning.


### Part 3: Testing and Documentation

**Write tests**
Use `bun:test` to write unit tests for your data generation script. Make sure it's actually creating the right number of locations, zones, sensors, and readings. Show us some sample outputs from your queries too.


**Document everything**
Write a clear README that explains:
- How to set up and run your code
- What each SQL query does and why you wrote it that way
- Any assumptions you made
- How to run the tests with `bun test`

Think of it as onboarding documentation for a teammate who's never seen your code before.

### How to Submit

**Put your code on GitHub** with:
- Your Bun script for data generation (using `bun:sqlite`)
- Your SQL queries (in a script or Bun file)
- Test files (using `bun:test`)
- A good README with setup instructions

**Technical checklist:**
- ✅ Using Bun (not Node.js)
- ✅ Only using Bun's built-in libraries (`bun:sqlite`, `bun:test`)
- ✅ No external npm packages for core stuff
- ✅ Everything runs with `bun run <script.js>`

**Email your repo link to: work@iotready.co**

### Important Note

We want to see YOUR code and YOUR problem-solving approach. Please don't use ChatGPT, Copilot, or other AI tools to generate code for this challenge. We're not just looking at whether it works - we want to understand how you think and code.

Any submissions with AI-generated code will be disqualified. We can tell. 😊

---

This challenge lets us see your SQL chops, how you work with modern JavaScript runtimes like Bun, and how you approach database design and data analysis. Good luck, and have fun with it!
