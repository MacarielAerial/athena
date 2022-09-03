from logging import Logger
from pathlib import Path

from athena.datasets.cora_dataset import CoraDataSet
from athena.datasets.networkx_graph_dataset import NetworkXGraphDataSet


def cora_to_nx_g_pipeline(path_output_nx_g: Path, logger: Logger) -> None:
    # Data Access - Input
    cora_dataset = CoraDataSet(logger=logger)
    cora_dgl_g = cora_dataset.load()

    # Task Processing
    cora_nx_g = cora_dataset.cora_dgl_g_to_nx_g(cora_dgl_g=cora_dgl_g, logger=logger)

    # Data Access - Output
    cora_nx_g_dataset = NetworkXGraphDataSet(filepath=path_output_nx_g, logger=logger)
    cora_nx_g_dataset.save(nx_g=cora_nx_g)


if __name__ == "__main__":
    import argparse

    from athena.nodes.base_logger import get_base_logger

    logger = get_base_logger()

    parser = argparse.ArgumentParser(
        description="Load Cora citation data in the form of a networkx graph"
    )

    parser.add_argument(
        "-pong",
        "--path_output_nx_g",
        type=Path,
        required=True,
        help="Path to a networkx graph that contains Cora citation data",
    )

    args = parser.parse_args()

    cora_to_nx_g_pipeline(path_output_nx_g=args.path_output_nx_g, logger=logger)
