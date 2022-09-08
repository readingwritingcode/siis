import helium as h
from helium import *
import time
sleep = 5

b = h.start_firefox('https://siis.ia.supersociedades.gov.co/#/')

h.wait_until(h.Text('Búsqueda de sociedades').exists)

h.click('Ver filtro')

h.wait_until(h.Text('Estados Financieros').exists)

h.select(b.find_element_by_name('region'), 'Antioquia')

h.select(b.find_element_by_name("departamento"), 'Antioquia')

h.click('APLICAR FILTROS')

time.sleep(sleep)

h.scroll_down(1080)
h.scroll_down(1080)
'''
# paginator
mui=b.find_elements_by_xpath('//ul[@class="MuiPagination-ul"]/li/button')
_next = mui[-1]

c = 0
for i in range(int(mui[-2].text)):
    # collect data from each card!
    # access pdf
    h.click(_next)
    c+=1
    time.sleep(sleep)
    h.scroll_down(2160)
    print('page:',c)
    h.wait_until(h.Text('Resultados').exists)
    mui=b.find_elements_by_xpath('//ul[@class="MuiPagination-ul"]/li/button')
    _next = mui[-1]
'''
# e = b.find_elements_by_class_name('card')
# e[0].find_elements_by_class_name("item-detail")[0]
    # -> o: title empresa
    # -> 1: ''
    # -> 2: 'NotImplemented
    # -> 3: 'ingresos actividades ordinarias'
    # -> 4: 'estado'
    # -> 5: button1: VISTA 360
    # -> 6: button2: COMPARAR
    # -> 7: button3: VER DETALLES
# VER DETALLE
#ee=e[0]
#ee.find_element_by_class_name('collapse')
# basic info
# economy info
# company actions
# -> ACTIVOS\n$5.368.455 M\nINGRESOS\n$460.851 M\nUTILIDAD NETA\n$39.900 M\nROA\n1.92%\nROE\n2.32%\nROS\n8.66%\nMARGEN BRUTO\n33.59%'

# e0v360=e[0].find_elements_by_class_name("item-detail")[5]
# h.click(e0v360)
# b.find_elements_by_class_name("card-body")
# 0
# -> 'Situación financiera\nACTIVOS\nActivos Totales\n$10.673.629 M\nVariación\n25.04 %\nPASIVOS\nPasivos Totales\n$6.219.684 M\nVariación\n-8.63 %\nPATRIMONIO\nPatrimonios Totales\n$4.453.945 M\nVariación\n157.62 %\nVer Situación Financiera\nResultado integral\nINGRESO\nTotal Último Año\n$3.940.137 M\nVariación\n-16.17 %\nGANANCIA .\nPerdida\n$76.041 M\nVariación\n36.83 %\nVer Resultado Integral\nIndicadores\nPRUEBA ÁCIDA\nUltimo Año\n3.73 Veces\nENDEUDAMIENTO\nUltimo Año\n58.27%\nROA\nUltimo Año\n3.80%\nROE\nUltimo Año\n3.97%\nVer Indicadores\nFlujo de Efectivo\nACT. OPERACIÓN\nTotal\n$-1.528.658 M\nVariación\n-\nACT. INVERSIÓN\nTotal\n$0 M\nInicial\n-\nACT. FINANCIANCIÓN\nTotal\n$1.519.876 M\nVariación\n-\nVer Flujo de efectivo\nOtro resultado integral\nGANANCIA\nPerdida\n$76.041 M\nVariación\n36.83 %\nRESULTADO INTEGRAL\nTotal\n$0 M\nInicial\n-\nVer Otro Resultado Integral\nProcesos en superintendencia\nACTIVOS\nTotales\n0\nCERRADOS\nTotales\n1\nVer Procesos'
# 1
# 
# ee = e.find_element_by_class_name('item-detail subtitles ")
