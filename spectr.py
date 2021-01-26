# bloco de chamar o programa?
import subprocess, sys, getopt
import numpy as np
import matplotlib

def main():
    time = int(sys.argv[1])
    gain = int(sys.argv[2])
    outfile = sys.argv[3]
    read_dev(time,gain,outfile)

def read_dev(time,gain,outfile):
    freq_arg = '-f '+str(898e6)+':'+str(932e6)
    gain_arg = '-g '+str(gain)
    time_arg = '-e '+str(time)+'m'
    file_arg = '-m '+str(outfile)
    print ("executando fftw por " + str(time) +" minutos com ganho de "+str(gain/10)+" dB")
    subprocess.run(["rtl_power_fftw", freq_arg, "-b 512", gain_arg, time_arg,"-o 66" ,file_args])
    parse_meta(outfile)

def parse_meta(infile):
    filedir = './'+infile+'.met'

    with open(filename, 'rb') as f:
        data = np.fromfile(f, dtype=np.float32)


if __name__ == '__main__':
    main()
