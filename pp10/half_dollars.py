denver = [1_700_000, 4_600_000, 2_100_000 ]
philadelphia =[]
philadelphia.append(1_800_000)
philadelphia.append( 5_000_000)
philadelphia.append(2_500_000)

print(philadelphia)
print(denver)

total=[0, 0, 0]
total[0]= philadelphia[0] + denver[0]
total[1]= philadelphia[1] + denver[1]
total[2]= philadelphia[2] + denver[2]
print(total)

avarage =(total[0] + total[1] + total[2]) / len(total)
print(avarage)

print(" Produkacja w roku 2012 wyniosła ", "{:,d}".format( total[0]).replace(",", " "), " sztuk.")
print(" Produkacja w roku 2013 wyniosła ", "{:,d}".format( total[1]).replace(",", " "), " sztuk.")
print(" Produkacja w roku 2014 wyniosła ","{:,d}".format( total[2]).replace(",", " "), " sztuk.")
print(" Srednia produkacja wyniosła  ", "{:,.0f}".format(avarage).replace(",", " "), " sztuk.")
