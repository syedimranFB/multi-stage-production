import json
from uuid import uuid4

def read_sql_file(file_path):
    # Read the SQL file
    with open(file_path, "r") as file:
        sql_code = file.read()
    return sql_code

# Specify the path to your SQL script
sql_file_path = "/home/runner/work/multi-stage-test/multi-stage-test/multi-stage-sender/SQL script 1.sql"

# Read the SQL script content
sql_code = read_sql_file(sql_file_path)

# Load the JSON structure
json_data = {
    "name": "convertosql",
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
with open("/home/runner/work/multi-stage-test/multi-stage-test/multi-stage-test/sqlscript/convertosql.json", "w") as output_file:
    json.dump(json_data, output_file, indent=4)
