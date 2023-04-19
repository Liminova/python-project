def clustering(entries: tuple[str], size: int) -> tuple[tuple[str]]:
    # """Takes a list of entries and returns a list of clusters"""
    """Takes a tuple of entries and returns a tuple of clusters"""
    clusters = []
    for cluster in range(0, len(entries), size):
        clusters.append(tuple(entries[cluster : cluster + size]))
    return tuple(clusters)
