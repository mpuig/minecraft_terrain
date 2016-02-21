# Minecraft Terrain
This is a Sunday test to create some real terrain into the great game Minecraft.
The idea was to use DEM files (Digital Elevation Model) to get the real elevations of a known place. DEM files can be found around internet.
The next step was to be able to send the information to Minecraft. To solve this, I choose to install the Canarymod Minecraft Server with a plugin that allows to send commands via python.


# Setup
These are the main steps:
1. Python virtual environment
2. Canarymod
3. Raspberry Juice Plugin
4. DEM files
5. Run script
6. Play

## Step 1. Create the Python virtual environment and install needed packages
mkvirtualenv minecraft_terrain
pip install -r requirements.txt

## Step 2. Download and install Canarymod Minecraft Server
- Create a folder for Canarymod.
- Download https://canarymod.net/releases/CanaryMod-1.2.0_0.zip
- Unzip it
- Edit the file eula.txt and set eula=true
- Run java -jar CanaryMod-1.8.0-1.2.0.jar

## Step 3. Download and Install Raspberry Juice Plugin
This is necessary to run your Minecraft with an API.
- Download the source code from https://github.com/martinohanlon/CanaryRaspberryJuice/archive/master.zip
- Open the zip file and copy the latest version of the plugin CanaryRaspberryJuice-#.#.jar from the jars folder to the  plugins folder in the Canarymod folder.

## Step4. Download DEM files
For example, in Barcelona Area, the ICGC has 5x5 Elevation Models
http://www.icgc.cat/appdownloads/

![alt tag](https://raw.githubusercontent.com/mpuig/minecraft_terrain/main/screenshots/dem_selector.png)

- build a VRT from all downloaded datasets
gdalbuildvrt -te 395000 4603000 405500 4607180 montserrat.vrt dems/*.txt


## Step 5. Run everything together
- Start up Canarymod (with the Raspberry Juice Plugin)
- Run the terrain.py script to read the DEM file and create the terrain
- Start minecraft
- Fly and enjoy the tour (/gamemode 1 <username>)

## Step6. Run Minecraft and fly

![alt flying](https://raw.githubusercontent.com/mpuig/minecraft_terrain/master/screenshots/flying1.png)

![alt flying](https://raw.githubusercontent.com/mpuig/minecraft_terrain/master/screenshots/flying2.png)
