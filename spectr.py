# bloco de chamar o programa?
#import subprocess, sys, getopt
#import numpy as np
#argvs estao certos

#def main():
#    time = int(sys.argv[1])
#    gain = int(sys.argv[2])
#    outfile = sys.argv[3]
#    read_dev(time,gain,outfile)
#def output():

#essa parte eu sei que funciona

#def read_dev(time,gain,outfile): funcao de acesso ao dispositivo
#    freq_arg = '-f '+str(898e6)+':'+str(932e6)
#    gain_arg = '-g '+str(gain)
#    time_arg = '-e '+str(time)+'m'
#    file_arg = '-m '+str(outfile)
#    print ("executando fftw por " + str(time) +" minutos com ganho de "+str(gain/10)+" dB")
#    subprocess.run(["rtl_power_fftw", freq_arg, "-b 512", gain_arg, time_arg,"-o 66" ,file_args])
#    parse_meta(outfile)

#def parse_meta(infile): #analise dos metadados do scan

#filedir = './'+infile+'.met'
meta = open("binout.met", "r")
propval = []
propname = []
for line in meta:
    field = line.split(" # ")
    propval.append(field[0])
    propname.append(field[1].rstrip('\n'))
meta.close()
props = dict(zip(propname,propval))
print(props)
#    with open(filename, 'rb') as f: isso aqui eh pra puxar as fft
        #data = np.fromfile(f, dtype=np.float32)
        #array = np.reshape(data, [11000, 11000])

#if __name__ == '__main__':
#    main()
