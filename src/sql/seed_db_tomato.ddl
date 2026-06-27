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
        'Tomato Better Bush',
        'vegetable',
        'Solanaceae',
        'Lycopersicon',
        'esculentum'
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
        'Dining Room',
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
        'Grove Resistive Moisture',
        'serial',
        'ohm'
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
    'grove-resistive-1',
    (SELECT * FROM devices_ref_id),
    (SELECT * FROM plant_id),
    (SELECT * FROM location_id)
);

