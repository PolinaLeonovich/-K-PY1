salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
a = money_capital
for i in range(months):
    difference = spend - salary
    a += difference
    spend *= 1 + increase

print(round(a))

