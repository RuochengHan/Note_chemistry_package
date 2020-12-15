1. Sometimes from `.sdf` file, number of bonds not correct (like C have 5).
Then use openbabel need to convert to `.xyz` and back to `.sdf` to let it be correct:
```bash
obabel -isdf input.sdf -oxyz -O input.xyz
obabel -ixyz input.xyz -osdf -O output.sdf
```

2. When using c++ rdkit on MacOS, one need to use ```bash brew install```, and at the same time modify the ` .rb ` file to turn on the static lib.
