import json
from uuid import uuid4

def read_sql_file(file_path):
    # Read the SQL file
    with open(file_path, "r") as file:
        sql_code = file.read()
    return sql_code

# Specify the path to your SQL script
sql_file_path = "/home/runner/work/multi-stage-production/multi-stage-production/multi-stage-sender/Script 03 - Create Gold View.sql"

# Read the SQL script content
sql_code = read_sql_file(sql_file_path)

# Load the JSON structure
json_data = {
    "name": "Script 03 - Create Gold View",
    "properties": {
        "content": {
            "query": sql_code,
            "metadata": {
                "language": "sql"
            },
            "currentConnection": {
                "databaseName": "default",  # Adjust as needed
                "poolName": "Built-in"
            },
            "resultLimit": 5000  # Adjust as needed
        },
        "type": "SqlQuery"
    }
}

# Convert JSON to string
json_string = json.dumps(json_data, indent=4)

# Save the JSON string to a file
with open("/home/runner/work/multi-stage-production/multi-stage-production/multi-stage-production/sqlscript/Script 03 - Create Gold View.json", "w") as output_file:
    json.dump(json_data, output_file, indent=4)
