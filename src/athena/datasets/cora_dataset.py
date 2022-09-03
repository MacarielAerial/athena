from enum import Enum
from logging import Logger
from typing import Dict

import networkx as nx
from dgl import DGLHeteroGraph
from dgl.data import CoraGraphDataset
from networkx import DiGraph, Graph
from numpy import ndarray

from athena.nodes.schema_nx_g import NodeAttrKey
from athena.nodes.torch_device import get_device


class NodeType(Enum):
    paper: str = "Paper"


class EdgeType(Enum):
    citation: str = "Citation"


class CoraDataSet:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def load(self) -> DGLHeteroGraph:  # type: ignore[no-any-unimported]
        cora_graph_dataset = CoraGraphDataset(reverse_edge=False)
        dgl_g = cora_graph_dataset[0]

        return dgl_g

    @staticmethod
    def cora_dgl_g_to_nx_g(  # type: ignore[no-any-unimported]
        cora_dgl_g: DGLHeteroGraph, logger: Logger
    ) -> Graph:
        logger.info(f"Cora data's metadata info:\n{cora_dgl_g}")

        # Parse arrays from dgl graph
        device = get_device()
        nfeats: ndarray = cora_dgl_g.ndata.pop("feat").to(device).numpy()
        labels: ndarray = cora_dgl_g.ndata.pop("label").to(device).numpy()
        adj: ndarray = cora_dgl_g.adjacency_matrix().to_dense().numpy()
        num_nodes: int = cora_dgl_g.num_nodes()

        # Initiate networkx graph from adjacency matrix
        nx_g = nx.from_numpy_matrix(A=adj, create_using=DiGraph)

        # Map 0-indexed node ids to node attributes
        nid_to_nfeat: Dict[int, ndarray] = dict(zip(range(num_nodes), nfeats))
        nid_to_label: Dict[int, ndarray] = dict(zip(range(num_nodes), labels))

        # Set node attributes
        nx.set_node_attributes(
            G=nx_g, values=nid_to_nfeat, name=NodeAttrKey.nfeat.value
        )
        nx.set_node_attributes(
            G=nx_g, values=nid_to_label, name=NodeAttrKey.label.value
        )

        logger.info(
            f"{nx_g.__class__} with {len(nx_g.nodes())} nodes and "
            f"{len(nx_g.edges())} edges is parsed from {type(cora_dgl_g)}"
        )

        return nx_g
