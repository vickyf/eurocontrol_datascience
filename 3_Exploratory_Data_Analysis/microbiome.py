metadata = pd.read_excel('data/microbiome/metadata.xls', sheetname='Sheet1')

i=0
chunks = []

for i in range(9):
    this_file = pd.read_excel('data/microbiome/MID{0}.xls'.format(i+1), sheetname='Sheet 1', index_col=0,
                              header=None)
    this_file.columns = ['Count']
    this_file.index.name = 'Taxon'
    for m in metadata.columns:
        this_file[m] = metadata.iloc[i][m]
    chunks.append(this_file)

pd.concat(chunks)