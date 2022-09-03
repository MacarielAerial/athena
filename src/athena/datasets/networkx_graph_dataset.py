from logging import Logger
from pathlib import Path

import networkx as nx
import orjson
from networkx import Graph


class NetworkXGraphDataSet:
    def __init__(self, filepath: Path, logger: Logger) -> None:
        self.filepath = filepath
        self.logger = logger

    def save(self, nx_g: Graph) -> None:  # type: ignore[no-any-unimported]
        self._save(nx_g=nx_g, filepath=self.filepath, logger=self.logger)

    @staticmethod
    def _save(  # type: ignore[no-any-unimported]
        nx_g: Graph, filepath: Path, logger: Logger
    ) -> None:
        with open(filepath, "wb") as f:
            data = nx.node_link_data(G=nx_g)
            b_data = orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY)
            f.write(b_data)

            logger.info(f"Saved a {type(nx_g)} object to {filepath}")

    @staticmethod
    def _load(  # type: ignore[no-any-unimported]
        filepath: Path, logger: Logger
    ) -> Graph:
        with open(filepath, "rb") as f:
            data = orjson.loads(f.read())
            nx_g = nx.node_link_graph(data=data)

            logger.info(f"Loaded a {type(nx_g)} object from {filepath}")

            return nx_g
