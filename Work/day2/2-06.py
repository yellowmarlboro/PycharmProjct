num = eval(input("请输入一个0-1000的数字"))
num1 = num%10
num2 = num//10%10
num3 = num//100
print("这个整数的各位数字之和是",num1+num2+num3)
