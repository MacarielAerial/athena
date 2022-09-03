from logging import Logger

from dgl.heterograph import DGLHeteroGraph

from athena.datasets.cora_dataset import CoraDataSet


def test_cora_dataset_load(test_logger: Logger) -> None:
    cora_dataset = CoraDataSet(logger=test_logger)
    cora_dgl_g = cora_dataset.load()

    assert isinstance(cora_dgl_g, DGLHeteroGraph)
