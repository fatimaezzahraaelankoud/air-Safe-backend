

def normalize(value, min_val, max_val):
    return ((value - min_val) / (max_val - min_val)) * 100


def calculate_ier(data):
    weights = {
        "pm25": 0.30,
        "co": 0.25,
        "humidity": 0.25,
        "temperature": 0.20
    }

    normalized = {
        "pm25": normalize(data.pm25, 0, 100),
        "co": normalize(data.co, 0, 50),
        "humidity": normalize(data.humidity, 0, 100),
        "temperature": normalize(data.temperature, -10, 50)
    }

    ier = sum(weights[k] * normalized[k] for k in weights)
    return round(ier, 2)