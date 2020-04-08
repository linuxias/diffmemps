# diffmemps

This script checks the diff of memory information obtained by memps when an ELF file is executed.
I recommend python version 3 or upper.

### How to run?

1. Get memps information about pre-version elf
```bash
#memps {pid} > pre_memps.txt
```

2. Get memps information about current-version elf
```bash
#memps {pid} > cur_memps.txt
```

3. Run script
```bash
python3 diffmemps.py pre_memps.txt cur_memps.txt
```

### Result

```csv
Increased memory
OBJECT NAME	SUM	S(CODE)1	S(CODE)2	S(CODE) DIFF	S(DATA)1	S(DATA)2	S(DATA) DIFF	P(CODE)1	P(CODE)2	P(CODE) DIFF	P(DATA)1	P(DATA)2	P(DATA) DIFF
/usr/lib/libslive-dbus-proxy.so.0.1	4	16	20	-4	0	0	0	0	0	0	8	8	0
/usr/lib/libemanual.so	4	8	12	-4	0	0	0	0	0	0	4	4	0
/usr/lib/libfontconfig.so.1.12.0	40	144	184	-40	0	0	0	0	0	0	4	4	0

Decreased memory
OBJECT NAME	SUM	S(CODE)1	S(CODE)2	S(CODE) DIFF	S(DATA)1	S(DATA)2	S(DATA) DIFF	P(CODE)1	P(CODE)2	P(CODE) DIFF	P(DATA)1	P(DATA)2	P(DATA) DIFF
/usr/lib/libecore_ipc.so.1.23.99	-4	24	20	4	0	0	0	4	4	0	4	4	0
/usr/lib/libpulse.so.0.21.1	-4	44	40	4	0	0	0	0	0	0	4	4	0
/usr/lib/pulseaudio/libpulsecommon-13.0.so	-32	64	32	32	0	0	0	0	0	0	4	4	0

Additional component
OBJECT NAME	SUM	S(CODE)	S(DATA)	P(CODE)	P(DATA)

Removed component
OBJECT NAME	SUM	S(CODE)	S(DATA)	P(CODE)	P(DATA)
/usr/lib/libslive-framework.so.0.1.0	16	16	0	0	8
/usr/lib/libdlog.so.0.0.0	12	12	0	0	8
```
