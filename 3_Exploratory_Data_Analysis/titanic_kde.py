surv = dict(list(titanic.groupby('survived')))
for s in surv:
    surv[s]['age'].dropna().plot(kind='kde', label=bool(s)*'survived' or 'died', grid=False, legend=True, xlim=(0,100))

for s in titanic.survived.unique():
    titanic[titanic['survived']==s].age.dropna().plot(kind='kde')
