from pandas._typing import Ordered as Ordered
from .base import ExtensionDtype as ExtensionDtype
from pandas._libs.tslibs import NaT as NaT, Period as Period, Timestamp as Timestamp #, timezones as timezones
from pandas.core.indexes.base import Index
from typing import Any, Optional, Sequence, Tuple, Type, Union

str_type = str

def register_extension_dtype(cls: Type[ExtensionDtype]) -> Type[ExtensionDtype]: ...

class Registry:
    dtypes = ...
    def __init__(self) -> None: ...
    def register(self, dtype: Type[ExtensionDtype]) -> None: ...
    def find(self, dtype: Union[Type[ExtensionDtype], str]) -> Optional[Type[ExtensionDtype]]: ...

registry = ...

class PandasExtensionDtype(ExtensionDtype):
    type = ...
    kind = ...
    subdtype = ...
    str: Optional[str_type] = ...
    num: int = ...
    shape: Tuple[int, ...] = ...
    itemsize: int = ...
    base = ...
    isbuiltin: int = ...
    isnative: int = ...
    def __hash__(self) -> int: ...
    @classmethod
    def reset_cache(cls) -> None: ...

class CategoricalDtypeType(type): ...

class CategoricalDtype(PandasExtensionDtype, ExtensionDtype):
    name: str = ...
    type: Type[CategoricalDtypeType] = ...
    kind: str_type = ...
    str: str = ...
    base = ...
    def __init__(self, categories: Optional[Sequence[Any]]=..., ordered: Ordered=...) -> None: ...
    @classmethod
    def construct_from_string(cls, string: str_type) -> CategoricalDtype: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def construct_array_type(cls): ...
    @staticmethod
    def validate_ordered(ordered: Ordered) -> None: ...
    @staticmethod
    def validate_categories(categories, fastpath: bool=...) : ...
    def update_dtype(self, dtype: Union[str_type, CategoricalDtype]) -> CategoricalDtype: ...
    @property
    def categories(self) -> Index: ...
    @property
    def ordered(self) -> Ordered: ...

class DatetimeTZDtype(PandasExtensionDtype):
    type: Type[Timestamp] = ...
    kind: str_type = ...
    str: str = ...
    num: int = ...
    base = ...
    na_value = ...
    def __init__(self, unit: str = ..., tz = ...) -> None: ...
    @property
    def unit(self): ...
    @property
    def tz(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string: str_type) : ...
    @property
    def name(self) -> str_type: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...

class PeriodDtype(PandasExtensionDtype):
    type: Type[Period] = ...
    kind: str_type = ...
    str: str = ...
    base = ...
    num: int = ...
    def __new__(cls, freq = ...): ...
    @property
    def freq(self): ...
    @classmethod
    def construct_from_string(cls, string): ...
    @property
    def name(self) -> str_type: ...
    @property
    def na_value(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def is_dtype(cls, dtype) -> bool: ...
    @classmethod
    def construct_array_type(cls): ...
    def __from_arrow__(self, array): ...

class IntervalDtype(PandasExtensionDtype):
    name: str = ...
    kind: str_type = ...
    str: str = ...
    base = ...
    num: int = ...
    def __new__(cls, subtype = ...): ...
    @property
    def subtype(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string): ...
    @property
    def type(self): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @classmethod
    def is_dtype(cls, dtype) -> bool: ...
    def __from_arrow__(self, array): ...
