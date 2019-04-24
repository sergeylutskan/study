def diet(foods):
    global food
    ans = []
    foods = foods.split()
    for f in foods:
        if f in food['диетическое']:
            ans.append(1)
        else:
            ans.append(0)
    if ans.count(0) == 0:
        return 'Так держать, Воин Дракона!'
    else:
        if ans.count(1)/ans.count(0) >= 0.5:
            
            return 'Так держать, Воин Дракона!'
        else:
            return 'Не ешь столько, По!'

food = {'диетическое':['творог','фрукты','мед']}
print(diet("творог"))
print(diet("печенье, чай, сахар, фрукты, мед"))
