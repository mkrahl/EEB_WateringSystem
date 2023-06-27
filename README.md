# Green Guardian

This repository contains the code for the prototype of a smart watering system, developed for the module Emerging Electronic Business. The watering_system directory contains the code which is supposed to be run on a microcontroller wired to the appropiate components as described in the installation instructions of our report. 
The code inside of the monitor_system directory can be run locally for demonstrative and debugging purposes.

## Technolgies
- RPi.GPIO: https://sourceforge.net/projects/raspberry-gpio-python/
- adafruit-circuitpython-mcp3xxx: https://docs.circuitpython.org/projects/mcp3xxx/en/latest/index.html
- Flask: https://flask.palletsprojects.com/en/2.3.x/
- Chart.js: https://www.chartjs.org/

## Installation and Running the system
After cloning the repository and changing direcotry into the EEB_WateringSystem folder execute the following steps for installing and running the systems.

### Watering System
1. cd watering_system
2. pip install -r requirements.txt
3. sh entrypoint.sh
4. Copy server url from console

### MonitorSystem
1. cd monitor_system
2. cd server
3. pip install -r requirements.txt
4. touch .env
   - MICROCONTROLLER_SERVER_URL="Paste previously copied URL"
6. sh entrypoint.sh
7. cd ..
8. cd frontend
9. Run webserver of your choice
10. View dashboard in browser
