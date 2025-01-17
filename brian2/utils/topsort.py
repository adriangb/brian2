from graphlib2 import TopologicalSorter


def topsort(graph):
    """
    Topologically sort a graph

    The graph should be of the form ``{node: [list of nodes], ...}``.
    """
    return list(TopologicalSorter(graph).static_order())
