savings = int(input("Enter Amount to Deposit ="))

onekyaw = savings // 1000
remainonekyaw = savings % 1000

fivedreds = remainonekyaw // 500
remainfivedreds = remainonekyaw % 500

twodreds = remainfivedreds// 200
remaintwodreds = remainfivedreds % 200

onedreds = remaintwodreds // 100
remainonedreds = remaintwodreds % 100

fifty = remainonedreds // 50
remainfifty = remainonedreds % 50

bente = remainfifty // 20
remainbente = remainfifty % 20

sampu = remainbente // 10
remainsampu = remainbente % 10


lima = remainsampu // 5
remainlima = remainsampu % 5

piso = remainlima // 1
remainosip = remainlima % 1



print("1000 =", onekyaw)
print("500 =", fivedreds)
print("200 =", twodreds)
print("100 =", onedreds)
print("50 =", fifty)
print("20 =", bente)
print("10 =", sampu)
print("5 =", lima)
print("1 = ", piso)
