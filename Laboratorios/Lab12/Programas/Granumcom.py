
# coding: utf-8

# In[ ]:

# Operaciones con un numero complejo
#nuco

def Granumcom(norma, fase, fp, conj, inverso, inversoa, mz, alpha, 
              raizn, n, potencia, p, malla, actilim, xmin, xmax, ymin,\
              ymax, real=1,imag=1):
    global Grafica
    ancho_cuadro=1.4
    marcador="o"
    tam_marcador=6
    
    z=real+imag*I
    plt.figure(figsize=(4,4))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    ax = plt.axes()
    
    s="$z=%s$"
    
    if fp==True:
        s="Forma polar: $z=%0.2f$"%Abs(z)+"$e^{%s i}$\n"%latex(round((arg(z)),3))+s
    
    
    if fase==True:
        if z==0:
            s="No es posible encontrar la fase si $z=%s$"
        else:
            if arg(z)<0:
                s=r"Fase: $\measuredangle z=%s$"%latex(round((arg(z)),3))+                " radianes \n o $\measuredangle z=%s$ "% latex(round((arg(z)+pi+pi).evalf(),3))+                " radianes\n "+s
            else:
                s=r"Fase: $\measuredangle z=%s$"%latex(round((arg(z)),3))+" radianes\n"+s

                
    
    if norma==True:
        s="Norma: $|z|=%0.2f$\n"%Abs(z)+s
    
    
    
    sns.set()
    cp=sns.color_palette("Set2", 10)
    print cp
    ax.plot([0, re(z)],[0,im(z)],color=cp[0],lw=3,label=s % latex(z))
    ax.plot(re(z),im(z), color=cp[0], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    ax.grid(malla) 
    
    if z==0 and inverso==True:
        inverso=False
        ax.axis([-0.3,1,-0.3,1])
        ax.text(0.05, 0.9, r"No es posible obtener el inverso"  ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')
        ax.text(0.05, 0.8, r"multiplicativo si $z=0$"  ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')
        
    if z==0 and p<=0  and potencia==True:
        potencia=False
        ax.axis([-0.3,1,-0.3,1])
        ax.text(0.05, 0.5, r"No es posible obtener la "   ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')
        ax.text(0.05, 0.4, r"potencia %s de $z$ si $z=0$"%latex(p)  ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')
        
    if conj==True:
        zc=conjugate(z);
    
    if inverso==True:
        zi=conjugate(z)/(Abs(z)**2);
        zi=round(re(zi), 2)+round(im(zi),2)*I
        
    if inversoa==True:
        zia=z*-1;
        
    
        
                
    #########################
    # Posiciones de los Ejes
    ########################
    
        
    if conj==True:
        ax.plot([0, re(zc)],[0,im(zc)],color=cp[1],lw=3,label=r"Conjugado: $\bar{z}=%s$" % latex(zc))
        ax.plot(re(zc),im(zc), color=cp[1], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1,ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    if inverso==True:
        ax.plot([0, re(zi)],[0,im(zi)],color=cp[2],lw=3,                label=r"Inverso multiplicativo: $z^{-1}=%s$" % latex(zi))
        ax.plot(re(zi),im(zi), color=cp[2], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)
        
    if inversoa==True:
        ax.plot([0, re(zia)],[0,im(zia)],color=cp[3],lw=3,label=r"Inverso Aditivo: $-z=%s$" % latex(zia))
        ax.plot(re(zia),im(zia), color=cp[3], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)
        
    if mz==True:
        ax.plot([0, re(alpha*z)],[0,im(alpha*z)],color=cp[4],lw=3,                label=r"Multiplo: $\alpha z=%s$" % latex(alpha*z))
        ax.plot(re(alpha*z),im(alpha*z), color=cp[4], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1,ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)

    
    if raizn==True:
        a=solve(t**n-z,t)
        j=0;
        for i in a:
            ax.plot([0, re(i)],[0,im(i)],color=cp[5],lw=3,label=r"raiz $z_{%d}$"%(j+1)+"$=%s$"                    % latex(round(re(a[j]),3)+round(im(a[j]),3)*I))
            ax.plot(re(i),im(i), color=cp[5], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
            plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
            j=j+1
            
    if potencia==True:
        
        zp=expand_complex(z**p).evalf()
        zp=round(re(zp),3)+round(im(zp),3)*I
        ax.plot([0, re(z**p)],[0,im(z**p)],color=cp[6],lw=3,label=r"Potencia: $z^p=%s$" % latex(zp))
        ax.plot(re(z**p),im(z**p), color=cp[6], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)

    
        
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


    #xlabel = ax.xaxis.get_label()                               
    #lpos = xlabel.get_position()
    #xlabel.set_position((1.04, lpos[1]))

    #ylabel = ax.yaxis.get_label()
    #lpos = ylabel.get_position()
    #ylabel.set_position((1.04, lpos[1]))

    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.08,0.5)
    #ax.
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlabel(r"$\mathbb{R}e$ ",fontsize=20)
    ax.set_ylabel(r"$\mathbb{I}m$",fontsize=20)
    title=ax.set_title(r"Operaciones unitarias para $z=%s$" %latex(z), y=1.05,        fontsize=14, color="k")
          
    #ax.axis([x0,x1,y0,y1])
    if  actilim==False or xmin>=xmax or ymin>=ymax :
        xlim=ax.get_xlim()
        ylim=ax.get_ylim()
        ax.set_xlim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
        ax.set_ylim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
    else:
        ax.set_xlim(xmin,xmax)
        ax.set_ylim(ymin,ymax)
        
        
    
    
    #plt.show()
    

