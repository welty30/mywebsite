import requests
import numpy as np
import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
import pandas as pd



#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#TUCSON


url = "https://api.open-meteo.com/v1/forecast"    
params = {
    "latitude": 32.117,  # Latitude for Tokyo
    "longitude": -110.941,  # Longitude for Tokyo
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone":"GMT",
    "models": "ncep_gfs_seamless"
}

response = requests.get(url, params=params)
data = response.json()

current_temp = data['hourly']['temperature_2m'][:]  # Get the current temperature   
valid_times = data['hourly']['time']

fig,axs = plt.subplots(1,1,figsize=(10,10))
images = []

axs.plot(valid_times[::3], current_temp[::3], label='Temperature (°C)', color='tab:blue')
axs.set_xlabel('Time')
axs.set_ylabel('Temperature (°C)')
axs.legend()
axs.grid()
axs.tick_params(axis='x', rotation=45,size=1)
axs.set_title('Temperature Forecast for KTUS')
plt.savefig('/home/f74r5jsaf1p0/public_html/ktus_temp.png')


#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#IAH


url = "https://api.open-meteo.com/v1/forecast"    
params = {
    "latitude": 29.984,  # Latitude for Tokyo
    "longitude": -95.341,  # Longitude for Tokyo
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone":"GMT",
    "models": "ncep_gfs_seamless"
}

response = requests.get(url, params=params)
data = response.json()

current_temp = data['hourly']['temperature_2m'][:]  # Get the current temperature   
valid_times = data['hourly']['time']

fig,axs = plt.subplots(1,1,figsize=(10,10))
images = []

axs.plot(valid_times[::3], current_temp[::3], label='Temperature (°C)', color='tab:blue')
axs.set_xlabel('Time')
axs.set_ylabel('Temperature (°C)')
axs.legend()
axs.grid()
axs.tick_params(axis='x', rotation=45,size=1)
axs.set_title('Temperature Forecast for KIAH')
plt.savefig('/home/f74r5jsaf1p0/public_html/kiah_temp.png')


#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#MRY


url = "https://api.open-meteo.com/v1/forecast"    
params = {
    "latitude": 36.587,  # Latitude for Tokyo
    "longitude": -121.843,  # Longitude for Tokyo
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone":"GMT",
    "models": "ncep_gfs_seamless"
}

response = requests.get(url, params=params)
data = response.json()

current_temp = data['hourly']['temperature_2m'][:]  # Get the current temperature   
valid_times = data['hourly']['time']

fig,axs = plt.subplots(1,1,figsize=(10,10))
images = []

axs.plot(valid_times[::3], current_temp[::3], label='Temperature (°C)', color='tab:blue')
axs.set_xlabel('Time')
axs.set_ylabel('Temperature (°C)')
axs.legend()
axs.grid()
axs.tick_params(axis='x', rotation=45,size=1)
axs.set_title('Temperature Forecast for KMRY')
plt.savefig('/home/f74r5jsaf1p0/public_html/kmry_temp.png')