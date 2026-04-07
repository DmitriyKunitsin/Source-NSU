loadXcosLibs(); loadScicos();
a1 = 2
a2 = -3
a3 = 1
b1 = 2
b2 = 1
t = 3
sigma = 10

importXcosDiagram("C:\Users\User\Desktop\MironovBykova\lab5\2.4.zcos")

etta = 3 / t

mu = -%pi / log(sigma / 100)

a2_wished = etta * 2
a1_wished = (mu * etta) * (mu * etta) + etta * etta

k1 = a1_wished  - a1 / a3
k2 = a2_wished - a2 / a3

D = a1_wished / b1 / a3

Context.a1 = a1
Context.a2 = a2
Context.a3 = a3
Context.b1 = b1
Context.b2 = b2
Context.k1 = k1
Context.k2 = k2
Context.D = D
scicos_simulate(scs_m,Context);
filename = "C:/Users/User/Desktop/MironovBykova/lab5/res/" + "2.4"
xsave(filename + ".scg")
xs2png(20011, filename + ".png")



