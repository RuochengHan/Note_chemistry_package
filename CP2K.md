1. Install 
```bash
module load openmpi gcc
git clone https://github.com/cp2k/cp2k.git
cd cp2k/tools/toolchain
./install_cp2k_toolchain.sh -j 8 --install-all --enable-cuda=no --mpi-mode=openmpi
cp /pathto/cp2k/tools/toolchain/install/arch/* /pathto/cp2k/arch/
source /pathto/cp2k/tools/toolchain/install/setup
cd ../../
git submodule update --init --recursive # get dbcsr
make -j 8 ARCH=local VERSION="ssmp psmp"
```

2. all electron calculation needs GAPW, since the core electron makes larger gradients on potential. For peudopotential, GPW is fine.

3. in cp2py, if basis set is modified, do not change the name of the basis.
