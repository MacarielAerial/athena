import torch
from torch._C import device


def get_device(gpu_id: int = 0) -> device:
    device = torch.device(
        "cuda:{}".format(gpu_id) if torch.cuda.is_available() else "cpu"
    )

    return device
