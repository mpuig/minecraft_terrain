# minecraft_terrain
Creating "real" terrain in Minecraft from DEM files

# Setup

## Create the Python virtual environment and install needed packages

mkvirtualenv minecraft_terrain
pip install -r requirements.txt


## Download and install Canarymod Minecraft Server

- Create a folder for Canarymod.
- Download https://canarymod.net/releases/CanaryMod-1.2.0_0.zip
- Unzip it
- Edit the file eula.txt and set eula=true
- Run java -jar CanaryMod-1.8.0-1.2.0.jar


## Download and Install Raspberry Juice Plugin
This is necessary to run your Minecraft with an API.

- Download the source code from https://github.com/martinohanlon/CanaryRaspberryJuice/archive/master.zip
- Open the zip file and copy the latest version of the plugin CanaryRaspberryJuice-#.#.jar from the jars folder to the  plugins folder in the Canarymod folder.

## Download DEM files
For example, in Barcelona Area, the ICGC has 5x5 Elevation Models
http://www.icgc.cat/appdownloads/

![alt tag](https://raw.githubusercontent.com/mpuig/minecraft_terrain/main/screenshots/dem_selector.png)

- build a VRT from all downloaded datasets
gdalbuildvrt -te 395000 4603000 405500 4607180 montserrat.vrt dems/*.txt


## Run everything

- Start up Canarymod
- Run the terrain.py script
- Start minecraft

![alt tag](https://raw.githubusercontent.com/mpuig/minecraft_terrain/main/screenshots/flying1.png)

![alt tag](https://raw.githubusercontent.com/mpuig/minecraft_terrain/main/screenshots/flying2.png)
