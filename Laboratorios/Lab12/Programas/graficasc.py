
# coding: utf-8

# In[34]:


# Gráficas de funciones  complejas
# graficasc

from modulos import *
import numpy as np
from sympy.plotting import plot3d
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data


def Gragraficasc(figuras,mapeo,malla,
               actilim, xmin, xmax, ymin,\
              ymax,guarda=False):
    z= Symbol('z')
    x = Symbol("x", real=True)
    y = Symbol("y", real=True)
    ancho_cuadro=1.4
    marcador="o"
    tam_marcador=10
    fig=plt.figure(figsize=(20,10))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    #ax = plt.axes()

    
    
    axx1=fig.add_subplot(242,projection='3d',facecolor='w')
    axx3=fig.add_subplot(244,projection='3d',facecolor='w')
    axx2=fig.add_subplot(246,projection='3d',facecolor='w')
    axx4=fig.add_subplot(248,projection='3d',facecolor='w')
    
    at1=fig.add_subplot(241,facecolor='w')
    at2=fig.add_subplot(243,facecolor='w')
    at3=fig.add_subplot(245,facecolor='w')
    at4=fig.add_subplot(247,facecolor='w')
    
    
    
    
    f1=sympify(mapeo)
    f=lambdify(z,f1,("sympy",))
    u=lambdify((x,y),re(f(x+I*y).expand()),("numpy"))
    v=lambdify((x,y),im(f(x+I*y).expand()),("numpy"))
    u1=lambdify((x,y),re(f(x+I*y).expand()),("sympy"))
    v1=lambdify((x,y),im(f(x+I*y).expand()),("sympy"))
    w=lambdify((x,y),(((u1(x,y)**2+v1(x,y)**2)**0.5).expand()),("numpy"))
    zz=lambdify((x,y),simplify(atan(simplify(v1(x,y)/u1(x,y)))),("numpy"))
    
    
    if  actilim==False or xmin>=xmax or ymin>=ymax:
        xmin=-5
        xmax=5
        ymin=-5
        ymax=5
    
    
    X = np.arange(xmin, xmax, 0.25)
    Y = np.arange(ymin, ymax, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z=u(X,Y)
    axx1.plot_surface(X, Y, Z, rstride=1, cstride=1,linewidth=0, antialiased=False)
    
    axx1.contour(X, Y, Z, zdir='z', offset=np.min(Z)-0.4*abs(np.min(Z)))
    
    axx1.contour(X, Y, Z, zdir='y', offset=ymax+0.4*abs(ymax))
    
    axx1.contour(X, Y, Z, zdir='x', offset=xmin-0.4*abs(xmin))
    
    Z=v(X,Y)
    axx3.plot_surface(X, Y, Z, rstride=1, cstride=1,linewidth=0, antialiased=False)
    
    axx3.contour3D(X, Y, Z, 50)
    #axx3.plot_trisurf(X,Y,Z)
    
    
    Z=w(X,Y)
    #axx2.contour3D(X, Y, Z, 50)
    axx2.plot_surface(X, Y, Z, rstride=1, cstride=1,linewidth=0, antialiased=False)
    
    Z=zz(X,Y)
    #axx4.contour3D(X, Y, Z, 50)
    axx4.plot_surface(X, Y, Z, rstride=1, cstride=1,linewidth=0, antialiased=False)
    
    
    
    sns.set()
    cp=sns.color_palette("Set2", 10)
    
    
    
    #ax.grid(malla) 
    #axx.grid(malla)
    
    
      
    #at.axes([0.01, 0.01, 0.98, 0.90], axisbg="white", frameon=True)
    at1.set_xticklabels("", visible=False)
    at1.set_yticklabels("", visible=False)
    at1.grid(false)
    at1.set_xlim(0,1)
    at1.set_ylim(0,1)
    
    at1.text(0.2, 0.9, "El mapeo $f(z)=%s" % latex(f(z))+"$", fontsize=15)
    at1.text(0.2, 0.8, "con $z=%s" % latex(x+y*I)+"$ es", fontsize=15)
    at1.text(0.2, 0.7, "$f(z)=u(x,y)+v(x,y)i$", fontsize=15)
    at1.text(0.2, 0.6, "con", fontsize=10)
    at1.text(0, 0.5, "$u(x,y)=%s" % latex(u1(x,y))+"$", fontsize=10)
    at1.text(0, 0.4, "$v(x,y)=%s" % latex(v1(x,y))+"$", fontsize=10)
    at1.text(0, 0.3, "$\mathbb{R}e(f(z))=%s" % latex(u1(x,y))+"$", fontsize=15)

    at2.set_xticklabels("", visible=False)
    at2.set_yticklabels("", visible=False)
    at2.grid(false)
    at2.set_xlim(0,1)
    at2.set_ylim(0,1)
    
    at2.text(0.2, 0.9, "El mapeo $f(z)=%s" % latex(f(z))+"$", fontsize=15)
    at2.text(0.2, 0.8, "con $z=%s" % latex(x+y*I)+"$ es", fontsize=15)
    at2.text(0.2, 0.7, "$f(z)=u(x,y)+v(x,y)i$", fontsize=15)
    at2.text(0.2, 0.6, "con", fontsize=10)
    at2.text(0, 0.5, "$u(x,y)=%s" % latex(u1(x,y))+"$", fontsize=10)
    at2.text(0, 0.4, "$v(x,y)=%s" % latex(v1(x,y))+"$", fontsize=10)
    at2.text(0, 0.3, "$\mathbb{I}m(f(z))=%s" % latex(v1(x,y))+"$", fontsize=15)

    at3.set_xticklabels("", visible=False)
    at3.set_yticklabels("", visible=False)
    at3.grid(false)
    at3.set_xlim(0,1)
    at3.set_ylim(0,1)
    
    at3.text(0.2, 0.9, "El mapeo $f(z)=%s" % latex(f(z))+"$", fontsize=15)
    at3.text(0.2, 0.8, "con $z=%s" % latex(x+y*I)+"$ es", fontsize=15)
    at3.text(0.2, 0.7, "$f(z)=u(x,y)+v(x,y)i$", fontsize=15)
    at3.text(0.2, 0.6, "con", fontsize=10)
    at3.text(0, 0.5, "$u(x,y)=%s" % latex(u1(x,y))+"$", fontsize=10)
    at3.text(0, 0.4, "$v(x,y)=%s" % latex(v1(x,y))+"$", fontsize=10)
    at3.text(0, 0.3, "$\|f(z)\|=%s" % latex(simplify((u1(x,y)**2+v1(x,y)**2)**0.5))+"$", fontsize=15)
    
    at4.set_xticklabels("", visible=False)
    at4.set_yticklabels("", visible=False)
    at4.grid(false)
    at4.set_xlim(0,1)
    at4.set_ylim(0,1)
    
    at4.text(0.2, 0.9, "El mapeo $f(z)=%s" % latex(f(z))+"$", fontsize=15)
    at4.text(0.2, 0.8, "con $z=%s" % latex(x+y*I)+"$ es", fontsize=15)
    at4.text(0.2, 0.7, "$f(z)=u(x,y)+v(x,y)i$", fontsize=15)
    at4.text(0.2, 0.6, "con", fontsize=10)
    at4.text(0, 0.5, "$u(x,y)=%s" % latex(u1(x,y))+"$", fontsize=10)
    at4.text(0, 0.4, "$v(x,y)=%s" % latex(v1(x,y))+"$", fontsize=10)
    at4.text(0, 0.3, "$\measuredangle f(z)=%s"% latex(simplify(atan(simplify(v1(x,y)/u1(x,y)))))             +"$", fontsize=15)





    
    #at.arrow(0.2, 0.2, 0.6, 0, head_width=0.05, head_length=0.1, fc='k', ec='k',lw=3)  
    
    #########################
    # Posiciones de los Ejes
    ########################
    
            
    
    #ax.spines['bottom'].set_position('zero')
    #ax.spines['left'].set_position('zero')
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    
    #axx.spines['bottom'].set_position('zero')
    #axx.spines['left'].set_position('zero')
    #axx.spines['right'].set_visible(False)
    #axx.spines['top'].set_visible(False)
    
    


    #xlabel = ax.xaxis.get_label()                               
    #lpos = xlabel.get_position()
    #xlabel.set_position((1.04, lpos[1]))

    #ylabel = ax.yaxis.get_label()
    #lpos = ylabel.get_position()
    #ylabel.set_position((1.04, lpos[1]))

    #ax.xaxis.set_label_coords(0.5, -0.05)
    #ax.yaxis.set_label_coords(-0.08,0.5)
    #ax.
    #ax.spines['right'].set_color('none')
    #ax.spines['top'].set_color('none')
    #ax.set_xlabel(r"$x$ ",fontsize=20,color="b")
    #ax.set_ylabel(r"$y$",fontsize=20,color="b")
    #title=ax.set_title(r"Dominio de $f(z)$", y=1.05,fontsize=20, color="b")
    
    axx1.set_xlabel(r"$\mathbb{R}e(z)$ ",fontsize=10,color="b")
    axx1.set_ylabel(r"$\mathbb{I}m(z)$",fontsize=10,color="b")
    title=axx1.set_title(r"$\mathbb{R}e(f(z))$", y=1.1,fontsize=20, color="b")
    
    axx3.set_xlabel(r"$\mathbb{R}e(z)$ ",fontsize=10,color="b")
    axx3.set_ylabel(r"$\mathbb{I}m(z)$",fontsize=10,color="b")
    title=axx3.set_title(r"$\mathbb{I}m(f(z))$", y=1,fontsize=20, color="b")
    
    axx2.set_xlabel(r"$\mathbb{R}e(z)$ ",fontsize=10,color="b")
    axx2.set_ylabel(r"$\mathbb{I}m(z)$",fontsize=10,color="b")
    title=axx2.set_title(r"$\|f(z)\|$", y=1,fontsize=20, color="b")


    axx4.set_xlabel(r"$\mathbb{R}e(z)$ ",fontsize=10,color="b")
    axx4.set_ylabel(r"$\mathbb{I}m(z)$",fontsize=10,color="b")
    title=axx4.set_title(r"$\measuredangle f(z)$", y=1,fontsize=20, color="b")

    
    #axx.xaxis.set_label_coords(0.5, -0.05)
    #axx.yaxis.set_label_coords(-0.08,0.5)
    #ax.
    #axx.spines['right'].set_color('none')
    #axx.spines['top'].set_color('none')
    #axx.set_xlabel(r"$u(x,y)$ ",fontsize=20,color="b")
    #axx.set_ylabel(r"$v(x,y)$",fontsize=20,color="b")
    #title=axx.set_title(r"Rango de f(z)", y=1,fontsize=20, color="b")
          
    #ax.axis([x0,x1,y0,y1])
    #if  actilim==False or xmin>=xmax or ymin>=ymax :
    #    xlim=ax.get_xlim()
    #    ylim=ax.get_ylim()
    #    ax.set_xlim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
    #    ax.set_ylim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
        
    #    xlim=axx.get_xlim()
    #    ylim=axx.get_ylim()
    #    axx.set_xlim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)
    #    axx.set_ylim(min(xlim[0],ylim[0])*1.2,max(xlim[1],ylim[1])*1.2)


    #else:
    #    ax.set_xlim(xmin,xmax)
    #    ax.set_ylim(ymin,ymax)
        
    #    axx.set_xlim(xmin,xmax)
    #    axx.set_ylim(ymin,ymax)
        
    if guarda:
        plt.savefig("graficasc.png")
        plt.savefig("graficasc.svg")
        plt.savefig("graficasc.pdf")
        # No soporta en Binder
        # plt.savefig("graficasc.jpg")
        plt.close()
    guardanota.value=""
    
    #A=plot3d(re(f(x+I*y).expand()), (x, -5, 5), (y, -5, 5))
    #B=plot3d(im(f(x+I*y).expand()), (x, -5, 5), (y, -5, 5))
    #C=plot3d(Abs(f(x+I*y).expand()), (x, -5, 5), (y, -5, 5))
    #D=plot3d(arg(f(x+I*y).expand()), (x, -5, 5), (y, -5, 5))
    
    

def graficasc():
    
    style = {'description_width': 'initial'}
    global guardanota
    guardanota=widgets.Label(
        value="")

    
    Figuras=widgets.Select(
    options=['Cuadro', 'Arco', 'Recta'],
    value='Cuadro',
    # rows=10,
    # style=style,
    continuous_update=False,
    description='Conjunto:',
    disabled=False)



    #c=widgets.jslink((r1, 'value'), (b, 'value'))
    ut = Layout(
    display='flex',
    flex_flow='row',
    width='50px',
    height='100px')

    Mapeo=widgets.Textarea(
    value='exp(z)',
    placeholder='Escribe la funcion en terminos de z',
    description=r'\(f(z)\):',
    continuous_update=False,
    disabled=False
    )
    
    Enviar=widgets.Button(
    description='Enviar',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Enviar',
    icon='')

    

    Malla=widgets.Checkbox(
        value=True,
        description='Malla'
    )
    
    Actilim=widgets.Checkbox(
        value=False,
        description='Activar limites'
    )
    
    Xmin=widgets.FloatText(value=-1,
            description='Xmin',
            step=0.5,
            continuous_update=False)
    
    Xmax=widgets.FloatText(value=1,
            description='Xmax',
            step=0.5,
            continuous_update=False)
    
    Ymin=widgets.FloatText(value=-1,
            description='Ymin',
            step=0.5,
            continuous_update=False)
    
    Ymax=widgets.FloatText(value=1,
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
        Box([Figuras])
        ]

    form_items2 = [
        Box([Mapeo])]
    
    #form_items3 = [Box([Suma])]
       # Box([Label(value='Age of the captain'), IntSlider(min=40, max=60)], layout=form_item_layout),
    
    form_items5 = [Box([Actilim]),Box([Malla]), Box([Guardar])]
    form_items6 = [Box([Xmin]),Box([Xmax]),Box([guardanota])]
    form_items7 = [Box([Ymin]),Box([Ymax])]


    
    box1 = widgets.VBox(form_items1)
    box2 = widgets.VBox(form_items2)
    #box3 = widgets.VBox(form_items3)
    
    box5 = widgets.VBox(form_items5)
    box6 = widgets.VBox(form_items6)
    box7 = widgets.VBox(form_items7)

    

    caja=Layout(
        border='solid 2px',
        width='100%'
    )

    aa=widgets.HBox([box1, box2], layout=caja)
    bb=widgets.HBox([box5,box6, box7], layout=caja)

    
    children = [aa, bb]
    tab = widgets.Tab(layout=caja)
    tab.children = children
    tab.set_title(0,'Operaciones')
    tab.set_title(1, 'Vista')

    
                       
    #display(titulo)
    display(interactive_output(Gragraficasc,{'figuras':Figuras, 'mapeo':Mapeo,         'malla':Malla,'actilim':Actilim, 'xmin':Xmin, 'xmax':Xmax, 'ymin':Ymin,                                           'ymax':Ymax, }))
    
    
    display(tab)
    
    def on_guardar_clicked(b):
        guardanota.value="IMAGEN GUARDADA"
        Gragraficasc(figuras=Figuras.value, mapeo=Mapeo.value, malla=Malla.value,               actilim=Actilim.value, xmin=Xmin.value, xmax=Xmax.value, ymin=Ymin.value,              ymax=Ymax.value,guarda=True)
        
        


    Guardar.on_click(on_guardar_clicked)

#graficasc()

