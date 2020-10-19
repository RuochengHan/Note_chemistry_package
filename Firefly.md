1. run command:
```bash
mpirun -np $ncores $FFHOME/firefly820 -r -f -p -stdext -ex $FFHOME -i $input -o $output &
```
2. With external basis library:
```bash
mpirun -np $ncores $FFHOME/firefly820 -b /path-to-lib/ -r -f -p -stdext -ex $FFHOME -i $input -o $output &
```
3. Remove the previous OUTPUT file if you want to restart from scratch
```bash
rm *.ex OUTPUT
```
4. maximal MWORDS is 480, and it is better to prelocate in command line:
```bash
mpirun -np $ncores $FFHOME/firefly820 -prealloc:485 -r -f -p -stdext -ex $FFHOME -i $input -o $output &
```
