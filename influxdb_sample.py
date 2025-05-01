from influxdb_client import InfluxDBClient
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime, time

bucket = "soil_moisture_bucket"
query = 'from(bucket: "soil_moisture_bucket")\
|> range(start: -10m)\
|> filter(fn: (r) => r._measurement == "soil_level_measurement")\
|> filter(fn: (r) => r._field == "soil_level")\
|> filter(fn: (r) => r.soil == "sensor_data")'

token = "LxT0hwaESudoDWMGpNofXVxKUfIcP5y4EaUE7ilKuAMGdAglOa2w6PK1_ZR3IwWJjo57DMd4_oz1jo-Uo2Ozig=="
org = "Student"

#establish a connection
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org, debug=True)

#instantiate the WriteAPI and QueryAPI
write_api = client.write_api()
query_api = client.query_api()

# write_api.write("soil_moisture_bucket", org, ["soil_level_measurement,soil=soil soil_level=5"])
#create and write the point
p = Point("soil_level_measurement").tag("soil", "sensor_data").field("soil_level", 5)
write_api.write(SYNCHRONOUS)
write_api.write(bucket=bucket, org=org, record=p)

time.sleep(5)
result = client.query_api().query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_value(), record.get_field()))
print(results)
# write_api.close()
client.close()