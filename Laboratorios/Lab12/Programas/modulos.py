
# coding: utf-8

# In[1]:


##########################################################
##                                                      ##
##                    BITACORA                          ##
##             Días/horas de programación               ##
##    Día 1: viernes 01/septiembre/2017------7:00 horas ##
##    Día 2: sabado  02/septiembre/2017------2:00 horas ##
##    Día 3: domingo  03/septiembre/2017-----2:00 horas ##
##    Día 4: miercoles  06/septiembre/2017---5:30 horas ##
##    Día 5: jueves  07/septiembre/2017------3:00 horas ##
##    Día 6: viernes  08/septiembre/2017-----2:00 horas ##
##    Día 7: domingo  10/septiembre/2017-----1:00 horas ##
##    Día 8: lunes    11/septiembre/2017-----2:30 horas ##
##    Día 9: jueves    14/septiembre/2017----4:00 horas ##
##    Día 10: viernes  15/septiembre/2017----3:30 horas ##
##    Día 11: sabado  16/septiembre/2017---- 8:30 horas ##
##    Día 12: domingo 17/septiembre/2017---- 1:30 horas ##
##    Día 13: jueves  21/septiembre/2017---- 3:30 horas ##
##    Día 14: viernes  22/septiembre/2017----2:00 horas ##
##    Día 15: sabado   23/septiembre/2017----2:00 horas ##
##    Día 16: martes   26/septiembre/2017----3:00 horas ##
##    Día 17: miercoles 27/septiembre/2017---2:00 horas ##
##    Día 18: jueves    28/septiembre/2017---2:00 horas ##
##    Día 19: sabado    30/septiembre/2017---2:00 horas ##
##    Día 20: domingo      01/octubre/2017---2:00 horas ##
##    Día 21: Domingo    17/diciembre/2017---3:00 horas ##
##    Día 22: Lunes      18/diciembre/2017---5:00 horas ##
##    Dia 23: Viernes    9/marzo/2018--------8:00 horas ##
##    Dia 24: Domingo   11/marzo/2018--------2:00 horas ##
##    Día 25: Jueves    29/marzo/2018--------2:00 horas ##
##    Día 26: Martes    03/abril/2018--------2:00 horas ##
##    Dia 27 Lunes      10/dic/2018----------4:00 horas ##
##----------------------------------------------------- ##
##                                   TOTAL: 87:30 horas ##
##                                                      ##
##########################################################


get_ipython().magic(u'matplotlib inline')
#import sympy
from sympy import *
#import numpy as np
import matplotlib.pyplot as plt # importamos el submódulo para gráfica
import seaborn as sns
import matplotlib.image as mpimg

#import matplotlib as mpl
#print mpl.get_cachedir()
#from IPython.html import widgets
#from IPython.html.widgets import interact, interactive, fixed, 
from ipywidgets import interact, interactive, fixed, interactive_output, interact_manual, Layout, Button, Box,FloatText, Textarea, Dropdown, Label, IntSlider, HBox


import ipywidgets as widgets
from IPython.display import display, Latex, Math
from sympy.abc import x, y, mu, r, tau
#init_printing(use_latex='mathjax') # impresion en formato latex
#display(Math(r"""%s""" %latex(t**2)))

