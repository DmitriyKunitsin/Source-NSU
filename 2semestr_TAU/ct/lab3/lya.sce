loadXcosLibs(); loadScicos();
K1=5
K2=0.8
T2=0.2
K3=3
T3=1
d=1

K1_kol_kr = 6
K1_ap_kr = -0.417
changed_k1=[0.8, 1, 1.2] 

// апериод когда по экспоненте в бесконечность

function[] = makeGraphK1(nameZCos, nameDirect, start_k)
    importXcosDiagram(nameZCos)
    for i = 1:(size(changed_k1)(2))
        Context.K1=start_k * changed_k1(i)
        Context.K2=K2
        Context.T2=T2
        Context.K3=K3
        Context.T3=T3
        Context.d=d
        scicos_simulate(scs_m,Context);
        filename = nameDirect + "/K_" + string(Context.K1)
        xsave(filename + ".scg")
        xs2png(20011, filename + ".png")
    end
endfunction

function[] = makeGraphD(nameZCos, nameDirect, start_d)
    importXcosDiagram(nameZCos)
    Context.K1=K1
    Context.K2=K2
    Context.T2=T2
    Context.K3=K3
    Context.T3=T3
    Context.d=start_d
    scicos_simulate(scs_m,Context);
    filename = nameDirect + "/d_" + string(Context.d)
    xsave(filename + ".scg")
    xs2png(20011, filename + ".png")
endfunction

function[] = makeGraphT2(nameZCos, nameDirect, start_t2)
    importXcosDiagram(nameZCos)
    Context.K1=K1
    Context.K2=K2
    Context.T2=start_t2
    Context.K3=K3
    Context.T3=T3
    Context.d=d
    scicos_simulate(scs_m,Context);
    filename = nameDirect + "/t2_" + string(Context.t2)
    xsave(filename + ".scg")
    xs2png(20011, filename + ".png")
endfunction

//makeGraphK1("C:/Users/User/Desktop/MironovBykova/lab2/schema.zcos", "C:/Users/User/Desktop/MironovBykova/lab2/graph/k1", K1_kol_kr)
//makeGraphK1("C:/Users/User/Desktop/MironovBykova/lab2/schema.zcos", "C:/Users/User/Desktop/MironovBykova/lab2/graph/k1", K1_ap_kr)
makeGraphD("C:/Users/User/Desktop/MironovBykova/lab2/schema.zcos", "C:/Users/User/Desktop/MironovBykova/lab2/graph/d", 0.864)

//makeGraphT2("C:/Users/User/Desktop/MironovBykova/lab2/schema.zcos", "C:/Users/User/Desktop/MironovBykova/lab2/graph/t2", 3.732)


