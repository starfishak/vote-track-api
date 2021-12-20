from dataclasses import dataclass


@dataclass
class Precinct:
    name: str
    votes: int


@dataclass
class GeoData:
    type: str
    data: dict
    generateID: str
