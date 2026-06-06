from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import sys
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

app = FastAPI()

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

@app.get("/")
async def root():
    '''
    Sample response from root, left over from the tutorials
    '''
    return {"message": "FastAPI is up"}

#################
# Read / Delete 
#################
@app.get("/get")
async def get_devices(target_table: str, target_id: int ):
    '''
    Get the entry from a table with some id.
    '''

    target_table = _map_table(target_table)
    entry = session.query(target_table).filter(
                          target_table.id == target_id).first()
    return entry

@app.post("/delete")
async def delete_devices(target_table: str, target_id: int ):
    target_table = _map_table(target_table)
    entry = session.query(target_table).filter(
                          target_table.id==target_id).first() 
    session.delete(entry)
    session.commit()
    return {"Value deleted": entry.id}

#################
#### Devices ####
#################
@app.post("/create/devices")
async def create_devices(new_serial: str, new_type: int ):
    entry = Devices(serial=new_serial, type=new_type)
    session.add(entry)
    session.commit()
    return {"Device added": entry.id}

@app.post("/update/devices")
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

