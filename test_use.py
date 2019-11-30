from gpib_client import gpib_client
import matplotlib.pyplot as plt

keithley = gpib_client(13, "http://192.168.178.116", 8000, None, None)

ident = keithley.identify()
print ident

keithley.rst()
keithley.write(':INITiate:CONTinuous OFF;:ABORt')

data, time, epoch =keithley.write_read_bulk(":READ?", 20)

voltages = []

for d in data:
    voltages.append(float(d))

plt.plot(time, voltages)
