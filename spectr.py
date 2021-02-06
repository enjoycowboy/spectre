import subprocess, sys, getopt
import matplotlib.pyplot as plt
import numpy as np

#def main():
#    time = int(sys.argv[1])
#    gain = int(sys.argv[2])
#    outfile = sys.argv[3]
#    read_dev(time,gain,outfile)

#def read_dev(time,gain,outfile):
#    freq_arg = '-f '+str(900e6)+':'+str(980e6)
#    gain_arg = '-g '+str(gain)
#    time_arg = '-e '+str(time)+'m'
#    file_arg = '-m '+str(outfile)
#    print ("executando fftw por " + str(time) +" minutos com ganho de "+str(gain/10)+" dB")
#    subprocess.run(["rtl_power_fftw", freq_arg, "-b 65536", gain_arg,time_arg,"-o 66" ,file_arg])
#    parse_meta(outfile)

#def parse_meta(infile): #analise dos metadados do scan
#    filedir = './'+infile+'.met'
#    meta = open("binout.met", "r")
#    propval = []
#    propname = [] #isso aqui pode ser criado com os nomes ja
#    for line in meta:
#        field = line.split(" # ")
#        propval.append(field[0])
#        propname.append(field[1].rstrip('\n')) #talvez as propriedades vem sempre na mesma ordem
#    meta.close()
#    props = dict(zip(propname,propval))

    #isso aqui eh pra puxar as fft
#    Fs = 2e6 #2MHz
#    NFFT = 65536
#    binfile = "./"+infile+".bin"
#    with open(binfile, 'rb') as f:
#        data = np.fromfile(f, dtype=np.float32)
#    print(data)
#    Pxx, freqs, bins, img = plt.specgram(data, NFFT=NFFT, Fs=Fs,Fc=900e6, scale='dB', mode='psd', scale_by_freq=False)
#    plt.grid(True)
#    plt.show()

#def display():
filename="test2"
with open(filename+".bin", 'rb') as f:
    data = np.fromfile(f, dtype=np.float32)
f = open(filename+".met", "r")

propval = []
propname = ["nbins","nscans","freqstart","freqend","stepfreq","int_time","duration","timestart","timeend"]

for line in f:
    field = line.split(" # ")
    propval.append(field[0])
f.close()
props = dict(zip(propname,propval))
data.shape=(-1,int(props["nbins"]))

fig,ax = plt.subplots()
CS = ax.contour(data, origin="upper", interpolation='bilinear')
colorbar = fig.colorbar(CS)
plt.show()
#if __name__ == '__main__':
   # main()
