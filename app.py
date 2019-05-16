import copy

from shopAssistant import advice
from shopAssistant import mealsTypes
from shopAssistant.yamlOperations import fileOperations


def main():
    adviceList = []
    adv = advice.Advice()
    adv.name = "all"
    adv.ingredients = ["ing1", "ing2"]
    adv.mealType = mealsTypes.MealType.All
    adv2 = advice.Advice()
    adv2.name = "dinner"
    adv2.ingredients = ["ing4", "ing9"]
    adv2.mealType = mealsTypes.MealType.Dinner
    adv3 = advice.Advice()
    adv3.name = "lunch"
    adv3.ingredients = ["ing3", "ing7"]
    adv3.mealType = mealsTypes.MealType.Lunch
    adv4 = advice.Advice()
    adv4.name = "breakfast"
    adv4.ingredients = ["ing5", "ing8"]
    adv4.mealType = mealsTypes.MealType.Breakfast
    adviceList.append(adv)
    adviceList.append(adv2)
    adviceList.append(adv3)
    adviceList.append(adv4)
    print(adviceList)
    fileOperations.save_yaml(adviceList, "test.yml")


main()
