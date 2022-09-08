import helium as h
from helium import *
import time
sleep = 5

def tool():
    b = h.start_firefox('https://siis.ia.supersociedades.gov.co/#/')

    h.wait_until(h.Text('Búsqueda de sociedades').exists)

    h.click('Ver filtro')

    h.wait_until(h.Text('Estados Financieros').exists)

    h.select(b.find_element_by_name('region'), 'Antioquia')

    h.select(b.find_element_by_name("departamento"), 'Antioquia')

    h.click('APLICAR FILTROS')

    return b

if __name__ == "__main__":
    print('command line not implemented yet')