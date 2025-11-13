
## Data model (suggested)
This is just a suggested data model, you’re free to modify it as you see fit.
User {
  id
  email
  username
  password 
}

Sensor {
  id
  owner
  name
  description (optional)
  model
}

Readings {
  id
  sensor
  temperature
  humidity
  timestamp
}

Indexes: add indexes on (sensor, timestamp) for performance.
Unique together: (sensor, timestamp)

## API endpoints
All endpoints are prefixed with /api.

### Auth

POST /api/auth/register/ — register. Request: email, username, password. Response: token + user summary.

POST /api/auth/token/ — login. Request: email, password. Response: token.

POST /api/auth/refresh/ — (if using JWT)

### Sensors (Auth required)
GET /api/sensors/ — list (paginated). Query: page, page_size, q (search by name and model).

POST /api/sensors/ — create. Body: name, model, description (optional).

GET /api/sensors/{sensor_id}/ — detail.

PUT /api/sensors/{sensor_id}/ — update.

DELETE /api/sensors/{sensor_id}/ — delete (cascade readings).

### Readings (Auth required)
GET /api/sensors/{sensor_id}/readings/ — list readings for a sensor. Filters: timestamp_from, timestamp_to.

POST /api/sensors/{sensors_id}/readings/ — create. Body: temperature, humidity, timestamp.

Response models should be Pydantic models with examples in docstrings so the generated OpenAPI looks helpful.
