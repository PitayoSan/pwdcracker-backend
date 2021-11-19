pw = $1
mpiexec -f src/hosts -n 6 python3 src/cracker.py $pw
