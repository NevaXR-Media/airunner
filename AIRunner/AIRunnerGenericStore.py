from typing import Any, Dict, TypeVar, Generic

T = TypeVar("T")


class AIRunnerGenericStore(Generic[T]):
    store: Dict[str, T]

    def __init__(self) -> None:
        super().__setattr__("store", {})

    def get(self, key: str) -> Any:
        return self.store[key]

    def set(self, key: str, value: T) -> T:
        self.store[key] = value
        return value

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "store":
            super().__setattr__(key, value)
        else:
            self.store[key] = value

    def __getattr__(self, key: str) -> Any:
        try:
            return self.store[key]
        except KeyError:
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{key}'"
            )
