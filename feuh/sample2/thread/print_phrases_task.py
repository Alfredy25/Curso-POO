import dataclasses
from feuh.sample2.thread.functions import print_phrases


@dataclasses.dataclass
class PrintPhrasesTask:
    phrase1: str
    phrase2: str

    def __call__(self) -> None:
        print_phrases(self.phrase1, self.phrase2)
