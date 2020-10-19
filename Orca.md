## Others
1. Orca cannot use RI approaximation on Pople family basis set.
2. Orca will automatically use the tmp file from last calculation, delete them if a fresh calculation is needed:
```bash
rm -v !(*.dat|*.log)
```
