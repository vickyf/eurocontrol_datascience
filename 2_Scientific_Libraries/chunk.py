data_chunks = pd.read_csv("data/microbiome.csv", chunksize=15)
mean_tissue = {chunk.Taxon.values[0]:chunk.Tissue.mean() for chunk in data_chunks}
mean_tissue