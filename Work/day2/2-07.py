minutes = eval(input("请输入要转换的分钟数"))
days = minutes//60//24%365
years = minutes//60//24//365
print(minutes,"分钟是",years,"年",days,"天")