import dataclasses
from os import pread
from flask import Flask, json, request
from domain_objects import GeoData
from uuid import uuid4

app = Flask(__name__)


@app.route("/<legislative_district>")
def hello_world(legislative_district: int) -> list[GeoData]:
    data = GeoData(
        type="geodata",
        data={"legislative_district": legislative_district},
        generateID=str(uuid4()),
    )
    return json.dumps([data])


# Launch the app
app.run(host="0.0.0.0", port=8080, debug=True)
