import random

def simulate_sensor():
    return {
        "temperature": random.uniform(15, 35),
        "humidity": random.uniform(30, 80),
        "pm25": random.uniform(5, 150),
        "co": random.uniform(0, 20),
        "co2": random.uniform(400, 2000),
        "no2": random.uniform(0, 100)
        
    }   