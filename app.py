import copy

from shopAssistant import advice
from shopAssistant import mealsTypes
from shopAssistant.yamlOperations import fileOperations
import random


def print_advice(adv):
    print(adv.name)
    print(adv.ingredients)
    print(adv.mealType.name)


def print_all(adv_l):
    i = 0
    for a in adv_l:
        print()
        print(i, ".:")
        print_advice(a)
        print()
        i += 1


def load_advices():
    adv_l = fileOperations.open_yaml("adviceList.yml")
    return adv_l


def save_advice(adv_l):
    fileOperations.save_yaml(adv_l, "adviceList.yml")


def chose_by_type(adv_l):
    print()
    i = 1
    for m in mealsTypes.MealType:
        print(i, " ", m.name)
        i += 1
    print()
    new_arr = []
    i = int(input("Chose type\n"))
    for a in adv_l:
        if a.mealType.value == i:
            new_arr.append(a)
    if len(new_arr) > 0:
        print_advice(random.choice(new_arr))
    else:
        print("new_arr null")


def remove_adv(adv_l):
    print_all(adv_l)
    i = int(input("What to delete? "))
    print()
    adv_l.pop(i)


def add_adv(adv_l):
    a = advice.Advice()
    a.name = input("Name:")
    q = input("Type ingredient:")
    a.ingredients.append(q)
    q = input("Type ingredient or `/q` or `/Q` for stop adding ingredients:")
    while q != "/q" and q != "/Q":
        a.ingredients.append(q)
        q = input("Type ingredient or `/q` or `/Q` for stop adding ingredients:")
    i = 1
    for m in mealsTypes.MealType:
        print(i, " ", m.name)
        i += 1
    i = int(input("Chose type\n"))
    for m in mealsTypes.MealType:
        if m.value == i:
            a.mealType = m
    adv_l.append(a)


def main():
    adviceList = []

    choseInt = 1

    while choseInt != "q" and choseInt != "0":
        print("1. Load\n2. Save\n3. Print All\n4. Chose something to eat!\n5. Chose type and get me meal\n"
              "6. Remove\n7. Add")
        choseInt = input()
        if choseInt == "1":
            adviceList = load_advices()
        if choseInt == "2" and len(adviceList) > 0:
            save_advice(adviceList)
        if choseInt == "3" and len(adviceList) > 0:
            print_all(adviceList)
        if choseInt == "4" and len(adviceList) > 0:
            print_advice(random.choice(adviceList))
        if choseInt == "5" and len(adviceList) > 0:
            chose_by_type(adviceList)
        if choseInt == "6" and len(adviceList) > 0:
            remove_adv(adviceList)
        if choseInt == "7":
            add_adv(adviceList)


main()
