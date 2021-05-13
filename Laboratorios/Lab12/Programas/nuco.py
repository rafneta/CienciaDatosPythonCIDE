
# coding: utf-8

# In[ ]:


from modulos import *



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
    #print cp
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



def nuco(real=1,imaginario=1):
    style = {'description_width': 'initial'}
    r1=widgets.FloatText(
        value=1.5,
        description=r'\(\mathbb{R}e\text{(z)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima1=widgets.FloatText(
        value=-2.5,
        description=r'\(\mathbb{I}m\text{(z)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )


    #b = widgets.FloatSlider()

    #c=widgets.jslink((r1, 'value'), (b, 'value'))
    ut = Layout(
    display='flex',
    flex_flow='row',
    width='50px',
    height='100px')

    Norma=widgets.Checkbox(
        value=False,
        description=r'|z|'
    )

    Fase=widgets.Checkbox(
        value=False,
        description=r'\(\angle z\)'
    )

    FP=widgets.Checkbox(
        value=False,
        description='|z|'+r'\(e^{\angle z i}\)'
    )


    conj=widgets.Checkbox(
        value=False,
        description=r'\(\bar z\)'
    )

    inverm=widgets.Checkbox(
        value=False,
        description=r'\(\frac{1}{z}\)'
    )


    invera=widgets.Checkbox(
        value=False,
        description=r'\(-z\)'
    )




    rn0=widgets.Checkbox(
        value=False,
        description=r'\(\sqrt[r]{z}\)'
    )


    n=widgets.FloatText(value=2,
            description='r',
            step=0.5,
            continuous_update=False)

    MZ=widgets.Checkbox(
        value=False,
        description=r'\(\alpha z\)'
    )


    Alpha=widgets.FloatText(value=-0.5,
            description=r'\(\alpha\)',
            step=0.5,
            continuous_update=False)

    Potencia=widgets.Checkbox(
        value=False,
        description=r'\(z^p\)'
    )
    
    
    

    P=widgets.FloatText(value=-0.5,
            description=r'\(p\)',
            step=0.5,
            continuous_update=False)
    
    Malla=widgets.Checkbox(
        value=True,
        description='Malla'
    )
    
    Actilim=widgets.Checkbox(
        value=False,
        description='Activar limites'
    )
    
    Xmin=widgets.FloatText(value=-0.5,
            description='Xmin',
            step=0.5,
            continuous_update=False)
    
    Xmax=widgets.FloatText(value=0.5,
            description='Xmax',
            step=0.5,
            continuous_update=False)
    
    Ymin=widgets.FloatText(value=-0.5,
            description='Ymin',
            step=0.5,
            continuous_update=False)
    
    Ymax=widgets.FloatText(value=0.5,
            description='Ymax',
            step=0.5,
            continuous_update=False)

    
    
    boton=widgets.Button(
    description='Borrar seleccion',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Borrar',
    icon='')
    
    Guardar=widgets.Button(
    description='Guardar',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Guardar',
    icon='')
    
    lasx=widgets.FloatRangeSlider(
    value=[.1, 2],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',)
    
    lasy=widgets.FloatRangeSlider(
    value=[.1, 2],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='vertical',
    readout=True,
    readout_format='.1f',)

    
    form_items1 = [
        Box([r1]),
        Box([ima1]),
        Box([boton])
        ]

    form_items2 = [Box([Norma]), Box([Fase]), Box([FP])]
    form_items3 = [Box([conj]), Box([inverm]), Box([invera])]
       # Box([Label(value='Age of the captain'), IntSlider(min=40, max=60)], layout=form_item_layout),
    form_items4 = [

        HBox([MZ,Alpha]),
        HBox([rn0,n]),
        HBox([Potencia,P])
        
    ]
    
    form_items5 = [Box([Actilim]),Box([Malla]), Box([Guardar])]
    form_items6 = [Box([Xmin]),Box([Xmax])]
    form_items7 = [Box([Ymin]),Box([Ymax])]


    
    box1 = widgets.VBox(form_items1)
    box2 = widgets.VBox(form_items2)
    box3 = widgets.VBox(form_items3)
    box4 = widgets.VBox(form_items4)
    box5 = widgets.VBox(form_items5)
    box6 = widgets.VBox(form_items6)
    box7 = widgets.VBox(form_items7)

    

    caja=Layout(
        border='solid 2px',
        width='100%'
    )

    aa=widgets.HBox([box1, box2, box3,box4], layout=caja)
    bb=widgets.HBox([box5,box6, box7], layout=caja)

    
    children = [aa, bb]
    tab = widgets.Tab(layout=caja)
    tab.children = children
    tab.set_title(0,'Operaciones')
    tab.set_title(1, 'Vista')

    r1.value=real
    ima1.value=imaginario
    
    #display(titulo)
    display(interactive_output(Granumcom,{'real':r1,         'imag':ima1, 'norma':Norma, 'fase':Fase, 'fp':FP, 'conj':conj,          'inverso':inverm, 'inversoa':invera,  'mz':MZ, 'alpha':Alpha,         'raizn':rn0, 'n':n, 'potencia':Potencia, 'p':P, 'malla':Malla,         'actilim':Actilim, 'xmin':Xmin, 'xmax':Xmax, 'ymin':Ymin,                                           'ymax':Ymax, }))
    
    
    display(tab)
    def on_button_clicked(b):
        Norma.value=False
        Fase.value=False
        FP.value=False
        conj.value=False
        inverm.value=False
        invera.value=False
        MZ.value=False
        rn0.value=False
        Potencia.value=False
    


    boton.on_click(on_button_clicked)

