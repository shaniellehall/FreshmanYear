def totalCalories(proteins = 0, carbohydrates = 0, fats = 0):
    if not isinstance(proteins, (int, float)) or proteins < 0:
        proteins = 0
    if not isinstance(carbohydrates, (int, float)) or carbohydrates < 0:
        carbohydrates = 0
    if not isinstance(fats, (int, float)) or fats < 0:
        fats = 0

    proteinCalories = proteins * 4
    carbCalories = carbohydrates * 4
    fatCalories = fats * 9

    return proteinCalories + carbCalories + fatCalories

if __name__ == "__main__":
    print(totalCalories(8, 8, 3.5))
    
