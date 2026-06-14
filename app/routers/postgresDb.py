from fastapi import APIRouter

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import sys
from datetime import datetime
from pathlib import Path

# Add the current working directory to sys.path
sys.path.append(str(Path.cwd()))

import os
from dotenv import load_dotenv

# Read in .env.postgres variables 
# and setup the Session
load_dotenv(dotenv_path='.env.postgres')
pg_usr = os.getenv('POSTGRES_USR')
pg_pwd = os.getenv('POSTGRES_PWD')
pg_db = os.getenv('POSTGRES_DB')

url = URL.create(
    drivername="postgresql",
    username=pg_usr,
    password=pg_pwd,
    host="localhost",
    database=pg_db,
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

# Import the ORMs 
from src.models import Base 
from src.models.orm import *

router = APIRouter()

def _map_table(target_table: str): 
    '''
    Map a string input to the API as the ORM object.
    There may be a better way? But this will work and can be expanded
    as needed.
    '''

    if target_table.upper() == "DEVICES":
        target_table = Devices
    elif target_table.upper() == "LOCATIONS":
        target_table = Locations
    elif target_table.upper() == "MEASUREMENTS":
        target_table = Measurements
    elif target_table.upper() == "PLANTS":
        target_table = Plants 

    return target_table 

#################
# Read / Delete 
#################
@router.get("/get")
async def get(target_table: str, target_id: int ):
    '''
    Get the entry from a table with some id. All tables use 
    integer pks.
    '''

    target_table = _map_table(target_table)
    entry = session.query(target_table).filter(
                          target_table.id == target_id).first()
    return entry

@router.post("/delete")
async def delete(target_table: str, target_id: int ):
    '''
    Delete an  entry from a table with some id. All tables use 
    integer pks.
    '''
    target_table = _map_table(target_table)
    entry = session.query(target_table).filter(
                          target_table.id==target_id).first() 
    session.delete(entry)
    session.commit()
    return {"Value deleted": entry.id}

#################
#### Devices ####
#################
@router.post("/create/devices")
async def create_devices(new_serial: str, new_type: int ):
    entry = Devices(serial=new_serial, type=new_type)
    session.add(entry)
    session.commit()
    return {"Device added": entry.id}

@router.post("/update/devices")
async def update_devices(target_id: int, 
                        new_serial: str = None, 
                        new_type: int = None):
    entry = session.query(Devices).filter(Devices.id == target_id).first()
    
    if new_serial is not None: 
        entry.serial = new_serial
    if new_type is not None: 
        entry.type = new_type
    session.add(entry)
    session.commit()
    return {"Device updated": entry.id}

@router.get("/get/device")
async def get_device(target_serial: str ):
    '''
    Get the device ID based on the serial number
    '''

    entry = session.query(Devices).filter(
                          Devices.serial == target_serial).first()
    return entry


#################
### Locations ###
#################
@router.post("/create/locations")
async def create_locations(new_plant_id: int ):
    entry = Locations(plant_id=new_plant_id)
    session.add(entry)
    session.commit()
    return {"Locations added": entry.id}

@router.post("/update/locations")
async def update_locations(target_id: int, 
                        new_plant_id: int = None):
    entry = session.query(Locations).filter(
                          Locations.id == target_id).first()
    
    if new_plant_id is not None: 
        entry.plant_id = new_plant_id
    session.add(entry)
    session.commit()
    return {"Locations updated": entry.id}

#################
### Locations ###
#################
@router.post("/create/locations")
async def create_locations(new_plant_id: int ):
    entry = Locations(plant_id=new_plant_id)
    session.add(entry)
    session.commit()
    return {"Locations added": entry.id}

@router.post("/update/locations")
async def update_locations(target_id: int, 
                        new_plant_id: int = None):
    entry = session.query(Locations).filter(
                          Locations.id == target_id).first()
    
    if new_plant_id is not None: 
        entry.plant_id = new_plant_id
    session.add(entry)
    session.commit()
    return {"Locations updated": entry.id}

#################
# Measurements ##
#################
@router.post("/create/measurements")
async def create_measurements(new_timestamp: datetime,
                              new_value: float,
                              new_device_id: int,
                              new_location_id: int):
    entry = Measurements(timestampe=new_timestamp,
                         value=new_value,
                         device_id=new_device_id,
                         location_id=new_location_id)
    session.add(entry)
    session.commit()
    return {"Measurements added": entry.id}

@router.post("/update/measurements")
async def update_measurements(target_id: int, 
                              new_timestamp: datetime = None,
                              new_value: float = None,
                              new_device_id: int = None,
                              new_location_id: int = None):
    entry = session.query(Measurements).filter(
                          Measurements.id == target_id).first()
    
    if new_timestamp is not None: 
        entry.timestamp = new_timestamp
    if new_value is not None: 
        entry.value = new_value
    if new_device_id is not None: 
        entry.device_id = new_device_id
    if new_location_id is not None: 
        entry.location_id = new_location_id
    session.add(entry)
    session.commit()
    return {"Peasurements updated": entry.id}

#################
#### Plants #####
#################
@router.post("/create/plants")
async def create_plants(new_type: int ):
    entry = Plants(type=new_type)
    session.add(entry)
    session.commit()
    return {"Plants added": entry.id}

@router.post("/update/plants")
async def update_plants(target_id: int, 
                        new_type: int = None):
    entry = session.query(Plants).filter(
                          Plants.id == target_id).first()
    
    if new_type is not None: 
        entry.type = new_type
    session.add(entry)
    session.commit()
    return {"Plants updated": entry.id}

