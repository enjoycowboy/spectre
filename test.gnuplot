set datafile separator ' '

set key autotitle columnhead
set ylabel "dB"
set xlabel "Frequencia (MHz)"
set grid ls 100
set xtics rotate
set xtics 1
set ytics 1
set style line 100 lt 1 lc rgb "grey" lw 0.5

plot "out.csv" using ($1/1e6):2 with lines, '' using 1:3 with lines
