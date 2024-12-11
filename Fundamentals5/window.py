from dataclasses import dataclass

@dataclass

class Config:
    host: str
    port: int

Config(host="localhost", port=8080)

print(Config.host)