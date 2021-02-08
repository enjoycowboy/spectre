import subprocess, sys, getopt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def main():
    time = int(sys.argv[1])
    dt = datetime.now()
    outfile = "scan_"+ dt.strftime("%Y-%m-%d_%Hh%Mm%Ss")
    read_dev(time,outfile)

def read_dev(time, outfile):
    gain = 496 # /10dB
    freq_arg = '-f '+str(900e6)+':'+str(980e6)
    gain_arg = '-g '+str(gain)
    time_arg = '-e '+str(time)+'m'
    file_arg = '-m '+str(outfile)
    print ("executando fftw por " + str(time) +" minutos com ganho de "+str(gain/10)+" dB")
    subprocess.run(["rtl_power_fftw", freq_arg, "-b 65536", gain_arg,time_arg,"-o 66" ,file_arg])
    render(outfile)

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

    fig,ax = plt.subplots()
    CS = ax.contour(data, origin="upper", interpolation='bilinear')
    colorbar = fig.colorbar(CS)
    plt.show()
if __name__ == '__main__':
    main()
