
# coding: utf-8

# In[ ]:


# Producto de numeros complejos
### ncproducto

from modulos import *

def Granumproducto(producto,malla,
               actilim, xmin, xmax, ymin,\
              ymax, real1=1.5,imag1=-2.5,real2=-1,imag2=-0.5,guarda=False):
    
    ancho_cuadro=1.4
    marcador="o"
    tam_marcador=6
    
    z=real1+imag1*I
    z2=real2+imag2*I
    fig=plt.figure(figsize=(8,4))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    #ax = plt.axes()
    ax = fig.add_subplot(121)
    
    
    sns.set()
    cp=sns.color_palette("Set2", 10)

    ax.plot([0, re(z)],[0,im(z)],color=cp[0],lw=3,label="$z_1=(%s$" % latex(re(z))+                                                        "$,%s)$" % latex(im(z)))
    ax.plot(re(z),im(z),color=cp[0], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    ax.plot([0, re(z2)],[0,im(z2)],color=cp[1],lw=3,label="$z_2=(%s$" % latex(re(z2))+                                                        "$,%s)$" % latex(im(z2)))
    ax.plot(re(z2),im(z2), color=cp[1], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    
    ax.grid(malla) 
    
        
    if producto==True:
        zpro=z*z2
        zpro=round(re(zpro), 2)+round(im(zpro),2)*I
    
                
    #########################
    # Posiciones de los Ejes
    ########################
    
        
            
    if producto==True:
        ax.plot([0, re(zpro)],[0,im(zpro)],color=cp[2], lw=3,                label=r"Producto: $z_1*z_2= (%s$" % latex(re(zpro))+                                                        "$,%s)$" % latex(im(zpro)))
        ax.plot(re(zpro),im(zpro), color=cp[2], marker=marcador,markersize=tam_marcador)
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
    ax.set_xlabel(r"$a,c$ ",fontsize=20)
    ax.set_ylabel(r"$b,d$",fontsize=20)
    title=ax.set_title("Operacion para \n"+r"$z_1=(a,b)$ y $z_2=(c,d)$", y=1.05,        fontsize=14, color="k")
          
    #ax.axis([x0,x1,y0,y1])
    if  actilim==False or xmin>=xmax or ymin>=ymax :
        xlim=ax.get_xlim()
        ylim=ax.get_ylim()
        ax.set_xlim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
        ax.set_ylim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
    else:
        ax.set_xlim(xmin,xmax)
        ax.set_ylim(ymin,ymax)
        
    if guarda:
        plt.savefig("ncproducto.png")
        plt.savefig("ncproducto.svg")
        plt.savefig("ncproducto.pdf")
        # no se soporta en Binder
        # plt.savefig("ncproducto.jpg")
        plt.close()
    guardanota.value=""

        
    

def ncproducto(real1=1.5,imaginario1=-2.5,real2=-1,imaginario2=-0.5):
    style = {'description_width': 'initial'}
    global guardanota
    guardanota=widgets.Label(
        value=""
    )

    r1=widgets.FloatText(
        value=1.5,
        description=r'\(a\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima1=widgets.FloatText(
        value=-2.5,
        description=r'\(b\)',
        step=0.5,
        continuous_update=False,
        style=style
    )


    r2=widgets.FloatText(
        value=-1,
        description=r'\(c\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima2=widgets.FloatText(
        value=-0.5,
        description=r'\(d\)',
        step=0.5,
        continuous_update=False,
        style=style
    )



    #c=widgets.jslink((r1, 'value'), (b, 'value'))
    ut = Layout(
    display='flex',
    flex_flow='row',
    width='50px',
    height='100px')

    Producto=widgets.Checkbox(
        value=False,
        description=r'\(z_1*z_2\)'
    )

    

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
        Box([ima1])
        ]

    form_items2 = [
        Box([r2]),
        Box([ima2])]
    
    form_items3 = [Box([Producto])]
       # Box([Label(value='Age of the captain'), IntSlider(min=40, max=60)], layout=form_item_layout),
    
    form_items5 = [Box([Actilim]),Box([Malla]), Box([Guardar])]
    form_items6 = [Box([Xmin]),Box([Xmax]),Box([guardanota])]
    form_items7 = [Box([Ymin]),Box([Ymax])]


    
    box1 = widgets.VBox(form_items1)
    box2 = widgets.VBox(form_items2)
    box3 = widgets.VBox(form_items3)
    
    box5 = widgets.VBox(form_items5)
    box6 = widgets.VBox(form_items6)
    box7 = widgets.VBox(form_items7)

    

    caja=Layout(
        border='solid 2px',
        width='100%'
    )

    aa=widgets.HBox([box1, box2, box3], layout=caja)
    bb=widgets.HBox([box5,box6, box7], layout=caja)

    
    children = [aa, bb]
    tab = widgets.Tab(layout=caja)
    tab.children = children
    tab.set_title(0,'Operaciones')
    tab.set_title(1, 'Vista')

    r1.value=real1
    ima1.value=imaginario1
    r2.value=real2
    ima2.value=imaginario2
    
    #display(titulo)
    display(interactive_output(Granumproducto,{'real1':r1,         'imag1':ima1, 'real2':r2,'imag2':ima2, 'producto':Producto,         'malla':Malla,'actilim':Actilim, 'xmin':Xmin, 'xmax':Xmax, 'ymin':Ymin,                                           'ymax':Ymax, }))
    
    
    display(tab)
    
    def on_guardar_clicked(b):
        guardanota.value="IMAGEN GUARDADA"
        Granumproducto(producto=Producto.value, malla=Malla.value,               actilim=Actilim.value, xmin=Xmin.value, xmax=Xmax.value, ymin=Ymin.value,              ymax=Ymax.value, real1=r1.value,imag1=ima1.value,real2=r2.value,imag2=ima2.value,
               guarda=True)
        
        


    Guardar.on_click(on_guardar_clicked)

