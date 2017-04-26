finalAccount = eval(input("请输入最终金额值"))
interestRate = eval(input("请输入百分比表示的年利率"))
years = eval(input("请输入年数"))
print("最初存款额应该是",finalAccount/(1+interestRate/1200)**(years*12))