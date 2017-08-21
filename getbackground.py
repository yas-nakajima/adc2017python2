import sys
import numpy as np
from astropy.io import fits

data = fits.getdata(sys.argv[1])
med = np.median(data)
std = np.std(data)

for i in range(5):
    xx = np.where((data > med - 3 * std) & (data < med + 3 * std))
    med = np.median(data[xx])
    std = np.std(data[xx])
    print ('{:.2f} {:.2f}'.format(med, std))  
