baseball[['h','bb', 'hbp']].sum(axis=1).div(
        baseball[['bb', 'hbp','ab', 'sf']].sum(axis=1)
                            ).order(ascending=False)