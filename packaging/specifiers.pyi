import abc
from .utils import canonicalize_version as canonicalize_version
from .version import LegacyVersion as LegacyVersion, Version as Version, parse as parse
from typing import Callable, FrozenSet, Iterable, Iterator, Optional, Union

ParsedVersion = Union[Version, LegacyVersion]
UnparsedVersion = Union[Version, LegacyVersion, str]
CallableOperator = Callable[[ParsedVersion, str], bool]

class InvalidSpecifier(ValueError): ...

class BaseSpecifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __hash__(self) -> int: ...
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool: ...
    @abc.abstractmethod
    def __ne__(self, other: object) -> bool: ...
    @property
    @abc.abstractmethod
    def prereleases(self) -> Optional[bool]: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...
    @abc.abstractmethod
    def contains(self, item: str, prereleases: Optional[bool] = ...) -> bool: ...
    @abc.abstractmethod
    def filter(self, iterable: Iterable[UnparsedVersion], prereleases: Optional[bool] = ...) -> Iterable[UnparsedVersion]: ...

class _IndividualSpecifier(BaseSpecifier):
    def __init__(self, spec: str = ..., prereleases: Optional[bool] = ...) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def operator(self) -> str: ...
    @property
    def version(self) -> str: ...
    @property
    def prereleases(self) -> Optional[bool]: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...
    def __contains__(self, item: str) -> bool: ...
    def contains(self, item: UnparsedVersion, prereleases: Optional[bool] = ...) -> bool: ...
    def filter(self, iterable: Iterable[UnparsedVersion], prereleases: Optional[bool] = ...) -> Iterable[UnparsedVersion]: ...

class LegacySpecifier(_IndividualSpecifier): ...

class Specifier(_IndividualSpecifier):
    @property
    def prereleases(self) -> bool: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...

class SpecifierSet(BaseSpecifier):
    def __init__(self, specifiers: str = ..., prereleases: Optional[bool] = ...) -> None: ...
    def __hash__(self) -> int: ...
    def __and__(self, other: Union[SpecifierSet, str]) -> SpecifierSet: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[FrozenSet[_IndividualSpecifier]]: ...
    @property
    def prereleases(self) -> Optional[bool]: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...
    def __contains__(self, item: Union[ParsedVersion, str]) -> bool: ...
    def contains(self, item: Union[ParsedVersion, str], prereleases: Optional[bool] = ...) -> bool: ...
    def filter(
        self, iterable: Iterable[Union[ParsedVersion, str]], prereleases: Optional[bool] = ...
    ) -> Iterable[Union[ParsedVersion, str]]: ...

