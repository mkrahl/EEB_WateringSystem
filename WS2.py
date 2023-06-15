from machine import ADC, Pin
import utime

def get_cpacitator_measurements():
    soil_adc = ADC(Pin(21))
    while True:
        print("ADC: %d" % soil_adc.read_u16() )
        utime.sleep(0.5)
get_cpacitator_measurements()