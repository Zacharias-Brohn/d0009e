def adjustRecipe(ingredients, baseServing, desiredServing):
    
    # Räkna variabel för funktion
    ingredientScale = desiredServing / baseServing

    # Justera mängd av ingredienser
    adjustedIngredients = {}
    for ingredient, amount in ingredients.items():
        adjustedAmount = amount * ingredientScale
        # Se till att ägg blir heltal
        if 'ägg' in ingredient.lower():
            adjustedAmount = int(adjustedAmount)
        adjustedIngredients[ingredient] = adjustedAmount
    
    return adjustedIngredients

def calcStirTime(desiredServing):
    baseTime = 10  # Fast antal minuter för smet
    extraTime = 1  # Antal extra minuter per person

    totalTime = baseTime + (extraTime * desiredServing) # Räkna totala tiden för smet

    return totalTime

def calcBakeTime(desiredServing):
    baseTime = 30  # Fast antal minuter för smet
    extraTime = 3  # Antal extra minuter per person

    totalTime = baseTime + (extraTime * desiredServing) # Räkna totala tiden i ugn

    return totalTime

def calcRecipe(desiredServing):
    #Original recept
    baseRecipe = {
    'Antal ägg': 3,
    'Strösocker (dl)': 3,
    'Vaniljsocker (tsk)': 2,
    'Bakpulver (tsk)': 2,
    'Vetemjöl (dl)': 3,
    'Smör (g)': 75,
    'Vatten (dl)': 1,
    }
    # Antal portioner för originalrecept
    baseServing = 4
    # Räkna förändrat recept
    finalRecipe = adjustRecipe(baseRecipe, baseServing, desiredServing)
    stirTime = calcStirTime(desiredServing)
    ovenTime = calcBakeTime(desiredServing)
    # Skriv förändrat recept
    print(f"\nIngredienser som behövs för {desiredServing} portioner:")
    for ingredient, amount in finalRecipe.items():
        print(f"{ingredient}: {amount:.2f}" if isinstance(amount, float) else f"{ingredient}: {amount}")
    print(f"Total tid att baka: {stirTime + ovenTime} minuter")


# Skriv original recept för 4 portioner
calcRecipe(4)

# Skriv recept för 7 portioner
calcRecipe(7)
