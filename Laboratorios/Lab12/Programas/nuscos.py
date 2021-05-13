
# coding: utf-8

# In[ ]:

# Operaciones aritmeticas de numeros complejos
#nuscos
from modulos import *

def Granumscoms(suma, resta, multiplicacion, division,malla,
               actilim, xmin, xmax, ymin,\
              ymax, real1=1.5,imag1=-2.5,real2=-1,imag2=-0.5):
    
    ancho_cuadro=1.4
    marcador="o"
    tam_marcador=6
    
    z=real1+imag1*I
    z2=real2+imag2*I
    plt.figure(figsize=(4,4))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    ax = plt.axes()
    
    
    sns.set()
    cp=sns.color_palette("Set2", 10)

    ax.plot([0, re(z)],[0,im(z)],color=cp[0],lw=3,label="$z_1=%s$" % latex(z))
    ax.plot(re(z),im(z),color=cp[0], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    ax.plot([0, re(z2)],[0,im(z2)],color=cp[1],lw=3,label="$z_2=%s$" % latex(z2))
    ax.plot(re(z2),im(z2), color=cp[1], marker=marcador,markersize=tam_marcador)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.3, 0.5, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    
    ax.grid(malla) 
    
    if z==0 and division==True:
        division=False
        ax.axis([-0.3,1,-0.3,1])
        ax.text(0.05, 0.9, r"No es posible dividir"  ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')
        ax.text(0.05, 0.8, r"si el divisor es $0$"  ,                 horizontalalignment='left', rotation=0, fontsize=13, color='red')    
        
    if suma==True:
        zsuma=z+z2
    
        
    if resta==True:
        zresta=z-z2;
    
    if division==True:
        zdiv=z/z2;
        zdiv=round(re(zdiv), 2)+round(im(zdiv),2)*I
        
    if multiplicacion==True:
        zmul=z*z2;
        zmul=round(re(zmul), 2)+round(im(zmul),2)*I
        
    
        
                
    #########################
    # Posiciones de los Ejes
    ########################
    
        
    if suma==True:
        ax.plot([re(z), re(zsuma)],[im(z),im(zsuma)],'--',color=cp[1],lw=1)
        ax.plot([re(z2), re(zsuma)],[im(z2),im(zsuma)],'--',color=cp[0],lw=1)
        ax.plot([0, re(zsuma)],[0,im(zsuma)],color=cp[2],lw=3,label=r"Suma: $z_1+z_2= %s$" % latex(zsuma))
        ax.plot(re(zsuma),im(zsuma),color=cp[2], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1,ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
    
    if resta==True:
        ax.plot([0, re(-1*z2)],[0,im(-1*z2)],color=cp[3],lw=3,label=r"$-z_2= %s$" %                latex(-1*z2))
        ax.plot(re(-1*z2),im(-1*z2),color=cp[3], marker=marcador,markersize=tam_marcador)
        
        ax.plot([re(z), re(zresta)],[im(z),im(zresta)],'--',color=cp[3],lw=1)
        ax.plot([re(-1*z2), re(zresta)],[im(-1*z2),im(zresta)],'--',color=cp[0],lw=1)
        
        ax.plot([0, re(zresta)],[0,im(zresta)],color=cp[4],lw=3,label=r"Resta: $z_1-z_2= %s$" %                latex(zresta))
        ax.plot(re(zresta),im(zresta), color=cp[4], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)
        
    if division==True:
        ax.plot([0, re(zdiv)],[0,im(zdiv)],color=cp[5], lw=3,                label=r"Division: $\frac{z_1}{z_2}= %s$" % latex(zdiv))
        ax.plot(re(zdiv),im(zdiv), color=cp[5], marker=marcador,markersize=tam_marcador)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.3, 0.1, ancho_cuadro, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=13)
        #(x0, y0, width, height)
        
    if multiplicacion==True:
        ax.plot([0, re(zmul)],[0,im(zmul)],color=cp[6], lw=3,                label=r"Producto: $z_1*z_2= %s$" % latex(zmul))
        ax.plot(re(zmul),im(zmul), color=cp[6], marker=marcador,markersize=tam_marcador)
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
    title=ax.set_title("Operaciones para \n"+r"$z_1=%s$ y "%latex(z)+"$z_2=%s$" %latex(z2), y=1.05,        fontsize=14, color="k")
          
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
    


titulo=widgets.HTML(
    value='''<div class="alert alert-warning"><h2>Operaciones unitarias</h2></div>''',
    placeholder='Some HTML')


def nuscos(real1=1.5,imaginario1=-2.5,real2=-1,imaginario2=-0.5):
    style = {'description_width': 'initial'}
    r1=widgets.FloatText(
        value=1.5,
        description=r'\(\mathbb{R}e\text{(}z_1\text{)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima1=widgets.FloatText(
        value=-2.5,
        description=r'\(\mathbb{I}m\text{(}z_1\text{)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )


    r2=widgets.FloatText(
        value=-1,
        description=r'\(\mathbb{R}e\text{(}z_2\text{)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima2=widgets.FloatText(
        value=-0.5,
        description=r'\(\mathbb{I}m\text{(}z_2\text{)}\)',
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

    Suma=widgets.Checkbox(
        value=False,
        description=r'\(z_1+z_2\)'
    )

    Resta=widgets.Checkbox(
        value=False,
        description=r'\(z_1-z_2\)'
    )
    
    Multiplicacion=widgets.Checkbox(
        value=False,
        description=r'\(z_1*z_2\)'
    )
    
    Division=widgets.Checkbox(
        value=False,
        description=r'\(\frac{z_1}{z_2}\)'
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

    form_items2 = [
        Box([r2]),
        Box([ima2])]
    
    form_items3 = [Box([Suma]), Box([Resta])]
       # Box([Label(value='Age of the captain'), IntSlider(min=40, max=60)], layout=form_item_layout),
    form_items4  = [Box([Multiplicacion]), Box([Division])]
    
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

    r1.value=real1
    ima1.value=imaginario1
    r2.value=real2
    ima2.value=imaginario2
    
    #display(titulo)
    display(interactive_output(Granumscoms,{'real1':r1,         'imag1':ima1, 'real2':r2,'imag2':ima2, 'suma':Suma,         'resta':Resta, 'multiplicacion':Multiplicacion, 'malla':Malla,'division':Division,        'malla':Malla,'actilim':Actilim, 'xmin':Xmin, 'xmax':Xmax, 'ymin':Ymin,                                           'ymax':Ymax, }))
    
    
    display(tab)
    def on_button_clicked(b):
        Suma.value=False
        Resta.value=False
        Multiplicacion.value=False
        Division.value=False
        


    boton.on_click(on_button_clicked)

    

