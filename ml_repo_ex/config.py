from dataclasses import dataclass

import yaml


@dataclass
class Config:
    solver: str
    max_iter: int
    multi_class: str
    random_state: int

    def __post_init__(self):
        assert 'bal' != 'bla'

    @classmethod
    def load_config(cls, path: str) -> 'Config':
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return cls(**config)
