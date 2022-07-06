
########### Código para las figuras del Trabajo de Fin de Grado Física de los Ecostistemas ###########
######################################## Arturo Abril Martínez #######################################
#################################### Facultad de C.C. Físicas UCM ####################################
############################################## 6/6/2022 ##############################################

***********************************************FIGURA 1***********************************************

Para obtener los perfiles de biomasa de la figura 1 del texto se utiliza la macro nombrada fig1.py. 
La sintaxis para llamarla es:

$ python3 fig1.py r d L (rho) (sigma) (Nx)

Donde r es el ratio de crecimiento, d el coeficiente de difusión, L el tamño del sistema, rho la inten-
sidad de la perturbación, sigma la extensión de la perturbación y Nx el número de divisiones de la red
unidimensional. Los únicos valores necesarios son los que no están entre paréntesis. 

Para probar por ejemplo hacer: 

$ python3 fig1.py 1 1 100 

Lo que correspondería a la figura 1c del texto. 

*********************************************** FIGURA 2 **********************************************

Se utiliza también la macro fig1.py. 
Para obtener las figuras del texto se hace:

$ python3 fig1.py 1 1 100 1 0.4
$ python3 fig1.py 1 1 100 0.4 1 

*********************************************** FIGURA 3 **********************************************

Para la figura 3 del texto se utiliza fig3.py. Los archivos con los datos necesarios para sacar la fi-
gura se encuentran en la carperta ./out. Para ver la figura 3b del texto hacer: 

$ python3 fig3.py 

Si se quieren usar otros datos, la macro que genera los archivos necesarios es rettime_make.py

************************************************ FIGURA 4 *********************************************

Para la figura 4 del texto se utilizan las macros fig4_l.py, fig4_gamma.py y fig4_rho.py. 
Los datos que leen estas macros están en ./out y se generan con las macros l_make.py, r_make.py y g_make.py. 

Para ver las figuras del texto hacer: 

$ python3 fig4_l.py
$ python3 fig4_rho.py
$ python3 fig4_gamma.py