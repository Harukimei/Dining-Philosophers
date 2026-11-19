class Fork:
    def __init__(self):
        self._is_used = False
        self._is_clean = True

    @property
    def is_used(self) -> bool:
        return self._is_used

    @is_used.setter
    def is_used(self, state:bool):
        self._is_used = state

    @property
    def is_clean(self) -> bool:
        return self._is_clean

    @is_clean.setter
    def is_clean(self, state:bool):
        self._is_clean = state

    def clean(self):
        self.is_clean = True

    def __str__(self):
        return f"Fork({self.is_clean}, {self.is_used})"