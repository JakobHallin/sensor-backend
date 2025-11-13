class Sensor:
    def __init__(self, id, owner, name, description, model):
        self.id = id
        self.owner = owner
        self.name = name
        self.description = description
        self.model = model
        #Unique together: (sensor, timestamp)

def create_sensor(id, owner, name, description, model):
    return Sensor(id, owner, name, description, model)
def get_sensor_info(sensor): #get details
    return { 
        "id": sensor.id,
        "owner": sensor.owner,
        "name": sensor.name,
        "description": sensor.description,
        "model": sensor.model
    } 
def update_sensor_description(sensor, new_description): #update
    sensor.description = new_description
    return sensor
def delete_sensor(sensor): #delete sensor
    del sensor

def list_sensors(sensors): #list (paginated) fix it later
    return [get_sensor_info(sensor) for sensor in sensors]

#from spec: GET /api/sensors/ — list (paginated). Query: page, page_size, q (search by name and model).
#POST /api/sensors/ — create. Body: name, model, description (optional).
#GET /api/sensors/{sensor_id}/ — detail.
#PUT /api/sensors/{sensor_id}/ — update.
#DELETE /api/sensors/{sensor_id}/ — delete (cascade readings).