%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

testscores = np.random.normal(9.5, 2.5, 500)
print('describe = ', st.describe(testscores))
print('mean = ', np.mean(testscores))
print('mode = ', st.mode(testscores))
print('tmean = ', st.tmean(testscores,[5,15]))
print('variation = ', st.variation(testscores))
print('skewness = ', st.skew(testscores))
print('kurtosis = ', st.kurtosis(testscores))
print('zscore = ', st.zscore(testscores)[:20])

relfr = st.relfreq(testscores, 20)
print('relfreq = ', relfr)
x1 = relfr.lowerlimit + np.linspace(0, relfr.binsize*relfr.frequency.size, relfr.frequency.size)

cumfr = st.cumfreq(testscores, 20)
print('cumfreq = ', cumfr)
x2 = cumfr.lowerlimit + np.linspace(0, cumfr.binsize*cumfr.cumcount.size, cumfr.cumcount.size)

plt.subplot(2,2,1)
plt.hist(testscores, 20)
plt.title('Histogram')
plt.xticks(())

plt.subplot(2,2,2)
plt.bar(x1, relfr.frequency, width = relfr.binsize)
plt.title('Relative histogram')
plt.xlim([x1.min(),x1.max()])

plt.subplot(2,2,3)
plt.bar(x2, cumfr.cumcount, width = cumfr.binsize)
plt.title('Cumulative histogram')
plt.xlim([x2.min(),x2.max()])

plt.show()