def retire(salary, age, savingPercent):
    yearsRemaining = 65 - age  # Age remaining to reach retirement
    goal = (salary * 0.7) * yearsRemaining  # Goal set for retirement (FIRE)

    moneySaving = salary * (savingPercent / 100)
    savedAt65 = int(moneySaving) * yearsRemaining  # How much money saved at 65

    print(
        f"Salary: {salary}\nPercent: {savingPercent}\nMoney Needed: {moneySaving}\n")


print(retire(10000, 27, 70))
