segments_merged = pd.merge(vessels, segments, left_index=True, right_on='mmsi')
segments_merged.head()