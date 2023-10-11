# first option
a = "CPIFP Nuevo (Desglose IES Campanillas)"

b = ((a[:12]).upper())
c = a[12:]

print(b + c)

# second option
a = "CPIFP Nuevo (Desglose IES Campanillas)"

cpifp = a[:6]
nuevo = a[6:12].upper()
desglose = a [12:]

print(cpifp + nuevo + desglose)

