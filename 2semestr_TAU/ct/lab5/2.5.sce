loadXcosLibs(); loadScicos();
a1 = 2
a2 = -3
a3 = 1
b1 = 2
b2 = 1
t = 3
sigma = 10

//k2, k2, D

etta = 3 / t

mu = -%pi / log(sigma / 100)

a2_wished = etta * 2
a1_wished = (mu * etta) * (mu * etta) + etta * etta

k1 = a1_wished  - a1 / a3
k2 = a2_wished - a2 / a3

D = a1_wished / b1 / a3

//l1, l2

t = t / 5 // для наблюдаемой должна быть меньше в 5-8 раз

importXcosDiagram("C:\Users\User\Desktop\MironovBykova\lab5\2.5.zcos")

etta =  3 / t

mu = -%pi / log(sigma / 100)

a2_wished = etta * 2
a1_wished = (mu * etta) * (mu * etta) + etta * etta

system_M = [b1, b2; (b1 * a2 / a3 - b2 * a1 / a3), (b1)]
system_b = [-a2_wished + a2 / a3; a1 / a3 - a1_wished]
L = linsolve(system_M, system_b);  

Context.a1 = a1
Context.a2 = a2
Context.a3 = a3
Context.b1 = b1
Context.b2 = b2
Context.k1 = k1
Context.k2 = k2
Context.D = D
Context.l1 = L(1)
Context.l2 = L(2)
Context.s1 = 0 //3
Context.s2 = 0 //5
scicos_simulate(scs_m,Context);
filename = "C:/Users/User/Desktop/MironovBykova/lab5/res/" + "2.5"
xsave(filename + ".scg")
xs2png(20011, filename + ".png")



