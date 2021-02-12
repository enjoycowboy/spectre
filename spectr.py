import subprocess, sys, getopt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def read_dev(time):
    dt = datetime.now()
    outfile = "scan_"+ dt.strftime("%Y-%m-%d_%Hh%Mm%Ss")
    gain = 496 # /10dB
    freq_arg = '-f '+str(898e6)+':'+str(920e6)
    gain_arg = '-g '+str(gain)
    time_arg = '-e '+str(time)+'m'
    file_arg = '-m '+str(outfile)
    print ("executando fftw por " + str(time) +" minutos com ganho de "+str(gain/10)+" dB")
    subprocess.run(["rtl_power_fftw", freq_arg, "-b 8192", gain_arg,time_arg,"-o 70" ,file_arg])

def render(filename): #analise dos metadados do scan
    with open(filename+".bin", 'rb') as f:
        data = np.fromfile(f, dtype=np.float32)

    #ler o arquivo de metadados e criar o dicionário de propriedades
    f= open(filename+".met", "r")

    propval = []
    propname = ["nbins","nscans","freqstart","freqend","stepfreq","int_time","duration","timestart","timeend"]

    for line in f:
        field = line.split(" # ")
        try:
            propval.append(int(field[0]))
        except ValueError:
            try:
                propval.append(float(field[0]))
            except ValueError:
                propval.append(field[0])
    f.close()
    props = dict(zip(propname,propval))
    data.shape=(-1,props["nbins"])
    print (props)
    x = np.arange(props["freqstart"], props["freqend"],props["freqstep"])
    y = range(props['nscans'])
    xmesh, ymesh = np.meshgrid(x,y)
    fig,ax = plt.subplots()
    CS = ax.contourf(xmesh, ymesh, data, origin="upper", interpolation='bilinear')
    ax.set_xlabel("Frequência")
    colorbar = fig.colorbar(CS)
    plt.show()
