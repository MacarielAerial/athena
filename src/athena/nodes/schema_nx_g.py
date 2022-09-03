from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Tuple


class NodeAttrKey(Enum):
    ntype: str = "ntype"
    nfeat: str = "nfeat"
    label: str = "label"


class EdgeAttrKey(Enum):
    etype: str = "etype"


@dataclass
class NodeTuple:
    nid: int
    node_attrs: Dict[str, Any]

    def to_native(self) -> Tuple[int, Dict[str, Any]]:
        return (self.nid, self.node_attrs)


@dataclass
class NodeTuples:
    list_node_tuples: List[NodeTuple]

    def to_native(self) -> List[Tuple[int, Dict[str, Any]]]:
        return [node_tuple.to_native() for node_tuple in self.list_node_tuples]


@dataclass
class EdgeTuple:
    src_nid: int
    dst_nid: int
    edge_attrs: Dict[str, Any]

    def to_native(self) -> Tuple[int, int, Dict[str, Any]]:
        return (self.src_nid, self.dst_nid, self.edge_attrs)


@dataclass
class EdgeTuples:
    list_edge_tuples: List[EdgeTuple]

    def to_native(self) -> List[Tuple[int, int, Dict[str, Any]]]:
        return [edge_tuple.to_native() for edge_tuple in self.list_edge_tuples]
