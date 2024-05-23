
def wspm_conversion(m):
    km = m * 3.6
    return km

def pressure_conversion(p):
    atm = p * 0.000987
    return atm

def get_pm25_color(value):
    if value > 86:
        return 'red'
    if value > 55 and value <=110:
        return 'orange'
    if value >30 and value <= 55:
        return 'yellow'
    if value <= 30:
        return 'green'

def get_pm10_color(value):
    if value > 120:
        return 'red'
    if value > 90 and value <=180:
        return 'orange'
    if value >50 and value <= 90:
        return 'yellow'
    if value <= 50:
        return 'green'

