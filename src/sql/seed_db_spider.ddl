-- Create the plant entry 
WITH plant_id AS (
    INSERT INTO gaea.plants (
        name_common,
        class_common,
        name_family,
        name_genus,
        name_species
    )
    VALUES (
        'Spider Plant',
        'house',
        'Asparagaceae',
        'Chlorophytum',
        'comosum'
    )
    RETURNING id
),

-- Create the location 
location_id AS ( 
    INSERT INTO gaea.locations (
        nickname,
        type
    )
    VALUES (
        'Office',
        'indoor'
    )
    RETURNING id
),

-- Create the Devices Reference and Device
devices_ref_id AS (
    INSERT INTO gaea.devices_ref (
        description, 
        communication_type,
        reading_units)
    VALUES (
        'Grove Capacitive Moisture',
        'serial',
        'farad'
    ) 
    RETURNING id
)

INSERT INTO gaea.devices (
    serial,
    type,
    plant_id,
    location_id
)
VALUES (
    'grove-capacitive-1',
    (SELECT * FROM devices_ref_id),
    (SELECT * FROM plant_id),
    (SELECT * FROM location_id)
);

