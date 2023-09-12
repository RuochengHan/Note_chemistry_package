# DP5-AI
## Required packages
```bash
sudo apt-get install libblas-dev liblapack-dev # For qml
pip3 install PyQt5 lmfit nmrglue pathos statsmodels qml -i https://pypi.douban.com/simple
conda install -c conda-forge openbabel # pip3 install has error
```

### Tinker
```bash
wget https://dasher.wustl.edu/tinker/downloads/bin-linux-8.10.5.tar.gz # for linux excutable
tar zxvf bin-linux-8.10.5.tar.gz
mv bin-linux bin
```

## Change example.cfg
Change Tinker path
Download parameter set from https://dasher.wustl.edu/tinker/
```bash
mkdir params
cd params
wget https://dasher.wustl.edu/tinker/distribution/params/mmff.prm
```

