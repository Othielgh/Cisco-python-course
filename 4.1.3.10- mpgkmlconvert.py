def l100kmtompg(liters):
   
    mpg = liters / 3.785411784
    miles = 100 * .621371192237334
    return miles / mpg


def mpgtol100km(miles):
    
    kml = 3.785411784
    kilom = miles * 1.609344 / 100
    return kml / kilom

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))