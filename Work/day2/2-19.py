investment = eval(input("请输入投资额"))
annualInterestRate = eval(input("请输入年利率"))
years = eval(input("请输入年数"))
print("未来投资额为", investment * (1 + annualInterestRate/1200)**(years*12))