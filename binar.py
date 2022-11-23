bin_x = (input ("Ведите двоичное x:  "))
bin_y = (input ("Введите двоичное y: "))
x = int(bin_x,2)
y = int(bin_y,2)
z=x*y
bin_z=bin(z)[2:]
print ("Произведение", bin_z)         