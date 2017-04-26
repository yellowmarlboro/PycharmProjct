temperature = eval(input("请输入介于-58至41华氏摄氏度的温度"))
windSpeed = eval(input("请输入每小时风速（大于2公里每小时）"))
print("风寒温度为", 35.74 + 0.6215*temperature - 35.75*windSpeed + 0.4275*temperature*windSpeed)