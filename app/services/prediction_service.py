import random

def predict_risk(symptomes, ier):
    score = 0

    if symptomes.toux:
        score += 20
    if symptomes.respiration_difficile:
        score += 40
    if symptomes.fatigue:
        score += 10

    score += ier * 0.5

    probability = min(score, 100)

    # classification
    if probability < 30:
        level = "LOW"
    elif probability < 60:
        level = "MEDIUM"
    elif probability < 80:
        level = "HIGH"
    else:
        level = "CRITICAL"

    return probability, level