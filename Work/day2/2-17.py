pounds = eval(input("请输入体重（磅）"))
height = eval(input("请输入身高（磅）"))
print("BMI为", pounds * 0.45359237 / (height * 0.0254) ** 2)