from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractCleaner(ABC):
    path: str

    @abstractmethod
    def execute(self) -> None:
        pass
