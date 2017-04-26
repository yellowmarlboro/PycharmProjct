amount = eval(input("请输入初始水的水量（以千克为单位）"))
initial = eval(input("请输入水的初始温度（以摄氏温度为单位）"))
final = eval(input("请输入睡得最终温度（以摄氏温度为单位）"))
print("所需要的能量是",amount * (final - initial) * 4184 )
