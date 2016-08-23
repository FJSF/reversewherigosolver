a = map(int,'303328')
b = map(int,'629990')
c = map(int,'040428')

if (c[1]+c[4]) % 2 == 0:
	latitude = a[2]*10+b[4]+b[1]*.1+c[3]*.01+a[0]*.001+c[4]*.0001+a[5]*.00001
	longitude = a[1]*100+c[0]*10+c[5]+b[3]*.1+b[0]*.01+a[4]*.001+c[1]*.0001+b[5]*.00001
else:
	latitude = b[0]*10+a[5]+a[2]*.1+c[0]*.01+c[3]*.001+c[4]*.0001+a[0]*.00001
	longitude = b[4]*100+c[5]*10+a[4]+a[1]*.1+b[3]*.01+b[5]*.001+c[1]*.0001+b[1]*.00001

print "Latitude: %d %.3f" % (latitude, (latitude%1)*60)
print "Longitude: %d %.3f" % (longitude, (longitude%1)*60)
