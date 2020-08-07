import numpy as np
import sys
import pandas.core.indexing as indexing
#from pandas._config import config as config
#from pandas._libs import Timestamp as Timestamp, iNaT as iNaT  #, lib as lib, properties as properties
from pandas._typing import Axis as Axis, Dtype as DType, FilePathOrBuffer as FilePathOrBuffer, FrameOrSeries as FrameOrSeries, JSONSerializable as JSONSerializable, Level as Level, Renamer as Renamer, ListLike as ListLike, Scalar as Scalar, SeriesAxisType as SeriesAxisType
#from pandas.compat import set_function_name as set_function_name
#from pandas.compat._optional import import_optional_dependency as import_optional_dependency
#from pandas.core import missing as missing, nanops as nanops
from pandas.core.base import PandasObject as PandasObject, SelectionMixin as SelectionMixin
#from pandas.core.construction import create_series_with_explicitDType as create_series_with_explicitDType
#from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_object as ensure_object, ensurestr_t as ensurestr_t, isbool_t as isbool_t, isbool_tDType as isbool_tDType, is_datetime64_anyDType as is_datetime64_anyDType, is_datetime64tzDType as is_datetime64tzDType, is_dict_like as is_dict_like, is_extension_arrayDType as is_extension_arrayDType, is_float as is_float, is_integer as is_integer, is_list_like as is_list_like, is_number as is_number, is_numericDType as is_numericDType, is_objectDType as is_objectDType, is_period_arraylike as is_period_arraylike, is_re_compilable as is_re_compilable, isScalar as isScalar, is_timedelta64DType as is_timedelta64DType, pandasDType as pandasDType
#from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
#from pandas.core.dtypes.inference import is_hashable as is_hashable
#from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.indexes.api import Index as Index
# , InvalidIndexError as InvalidIndexError, MultiIndex as MultiIndex, RangeIndex as RangeIndex
#from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
#from pandas.core.indexes.period import Period as Period, PeriodIndex as PeriodIndex
from pandas.core.internals import BlockManager as BlockManager
#from pandas.core.missing import find_valid_index as find_valid_index
#from pandas.errors import AbstractMethodError as AbstractMethodError
#from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter, format_percentiles as format_percentiles
#from pandas.io.formats.printing import pprint_thing as pprint_thing
#from pandas.tseries.frequencies import to_offset as to_offset
#from pandas.util._decorators import Appender as Appender, Substitution as Substitution, rewrite_axis_style_signature as rewrite_axis_style_signature
#from pandas.util._validators import validatebool_t_kwarg as validatebool_t_kwarg, validate_fillna_kwargs as validate_fillna_kwargs, validate_percentile as validate_percentile
from typing import Any, Callable, Dict, Hashable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

bool_t = bool
str_t = str


class NDFrame(PandasObject, SelectionMixin, indexing.IndexingMixin):
    def __init__(self, data: BlockManager, axes: Optional[List[Index]]=..., copy: bool=..., dtype: Optional[Dtype]=..., attrs: Optional[Mapping[Optional[Hashable], Any]]=..., fastpath: bool=...) -> None: ...
    @property
    def attrs(self) -> Dict[Optional[Hashable], Any]: ...
    @attrs.setter
    def attrs(self, value: Mapping[Optional[Hashable], Any]) -> None: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def axes(self) -> List[Index]: ...
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...
    @overload
    def set_axis(
        self, labels: Union[Index, ListLike], axis: SeriesAxisType = ..., *, inplace: Literal[True]
    ) -> None: ...
    @overload
    def set_axis(
        self, labels: Union[Index, ListLike], axis: SeriesAxisType = ..., inplace: Literal[False] = ...,
    ) -> Series[Dtype]: ...
    def swapaxes(self, axis1: SeriesAxisType, axis2: SeriesAxisType, copy: bool_t = ...) -> FrameOrSeries: ...
    def droplevel(self, level: Level, axis: SeriesAxisType = ...) -> FrameOrSeries: ...
    def pop(self, item: str_t) -> FrameOrSeries: ...
    def squeeze(self, axis: Optional[Any] = ...): ...
    def swaplevel(self, i: Any=..., j: Any=..., axis: Any=...) -> FrameOrSeries: ...
    def rename(self, mapper: Optional[Renamer]=..., *, index: Optional[Renamer]=..., columns: Optional[Renamer]=..., axis: Optional[Axis]=..., copy: bool=..., inplace: bool=..., level: Optional[Level]=..., errors: str=...) -> Optional[FrameOrSeries]: ...
    @overload
    def rename_axis(
        self,
        mapper: Union[Scalar, ListLike] = ...,
        index: Optional[Union[Scalar, ListLike, Callable, Dict]] = ...,
        columns: Optional[Union[Scalar, ListLike, Callable, Dict]] = ...,
        axis: Optional[SeriesAxisType] = ...,
        copy: bool_t = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        mapper: Union[Scalar, ListLike] = ...,
        index: Optional[Union[Scalar, ListLike, Callable, Dict]] = ...,
        columns: Optional[Union[Scalar, ListLike, Callable, Dict]] = ...,
        axis: Optional[SeriesAxisType] = ...,
        copy: bool_t = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> Series: ...
    def equals(self, other: Series[Dtype]) -> bool_t: ...
    def __neg__(self) -> None: ...
    def __pos__(self) -> None: ...
    def __invert__(self): ...
    def __nonzero__(self) -> None: ...
    _bool_t__: Any = ...
    def bool(self) -> bool_t: ...
    def __abs__(self) -> FrameOrSeries: ...
    def __round__(self, decimals: int=...) -> FrameOrSeries: ...
    def __hash__(self) -> Any: ...
    def __iter__(self) -> Iterator: ...
    def keys(self): ...
    def items(self) -> None: ...
    def iteritems(self): ...
    def __len__(self) -> int: ...
    def __contains__(self, key: Any) -> bool_t: ...
    @property
    def empty(self) -> bool_t: ...
    __array_priority__: int = ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def to_excel(
        self,
        excel_writer: Any,
        sheet_name: str_t = ...,
        na_rep: str_t = ...,
        float_format: Optional[str_t] = ...,
        columns: Optional[Union[str_t, Sequence[str_t]]] = ...,
        header: bool_t = ...,
        index: bool_t = ...,
        index_label: Optional[Union[str_t, Sequence[str_t]]] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[str_t] = ...,
        merge_cells: bool_t = ...,
        encoding: Optional[str_t] = ...,
        inf_rep: str_t = ...,
        verbose: bool_t = ...,
        freeze_panes: Optional[Tuple[int, int]] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        path_or_buf: Optional[FilePathOrBuffer],
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: bool_t = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[str_t, int, float, bool_t, List, Dict]]] = ...,
        lines: bool_t = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: bool_t = ...,
        indent: Optional[int] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: bool_t = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[str_t, int, float, bool_t, List, Dict]]] = ...,
        lines: bool_t = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: bool_t = ...,
        indent: Optional[int] = ...,
    ) -> str_t: ...
    def to_hdf(
        self,
        path_or_buf: FilePathOrBuffer,
        key: str_t,
        mode: str_t = ...,
        complevel: Optional[int] = ...,
        complib: Optional[str_t] = ...,
        append: bool_t = ...,
        format: Optional[str_t] = ...,
        index: bool_t = ...,
        min_itemsize: Optional[Union[int, Dict[str_t, int]]] = ...,
        nan_rep: Optional[Any] = ...,
        dropna: Optional[bool_t] = ...,
        data_columns: Optional[List[str_t]] = ...,
        errors: str_t = ...,
        encoding: str_t = ...,
    ) -> None: ...
    def to_sql(
        self,
        name: str_t,
        con: Any,
        schema: Optional[str_t] = ...,
        if_exists: str_t = ...,
        index: bool_t = ...,
        index_label: Optional[Union[str_t, Sequence[str_t]]] = ...,
        chunksize: Optional[int] = ...,
        dtype: Optional[Union[Dict, Scalar]] = ...,
        method: Optional[Union[str_t, Callable]] = ...,
    ) -> None: ...
    def to_pickle(
        self, path: str_t, compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ..., protocol: int = ...,
    ) -> None: ...
    def to_clipboard(self, excel: bool_t = ..., sep: Optional[str_t] = ..., **kwargs) -> None: ...
    def to_xarray(self): ...
    @overload
    def to_latex(
        self,
        buf: Optional[FilePathOrBuffer],
        columns: Optional[List[str_t]] = ...,
        col_space: Optional[int] = ...,
        header: bool_t = ...,
        index: bool_t = ...,
        na_rep: str_t = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[bool_t] = ...,
        index_names: bool_t = ...,
        bold_rows: bool_t = ...,
        column_format: Optional[str_t] = ...,
        longtable: Optional[bool_t] = ...,
        escape: Optional[bool_t] = ...,
        encoding: Optional[str_t] = ...,
        decimal: str_t = ...,
        multicolumn: Optional[bool_t] = ...,
        multicolumn_format: Optional[str_t] = ...,
        multirow: Optional[bool_t] = ...,
        caption: Optional[str_t] = ...,
        label: Optional[str_t] = ...,
    ) -> None: ...
    @overload
    def to_latex(
        self,
        columns: Optional[List[str_t]] = ...,
        col_space: Optional[int] = ...,
        header: bool_t = ...,
        index: bool_t = ...,
        na_rep: str_t = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[bool_t] = ...,
        index_names: bool_t = ...,
        bold_rows: bool_t = ...,
        column_format: Optional[str_t] = ...,
        longtable: Optional[bool_t] = ...,
        escape: Optional[bool_t] = ...,
        encoding: Optional[str_t] = ...,
        decimal: str_t = ...,
        multicolumn: Optional[bool_t] = ...,
        multicolumn_format: Optional[str_t] = ...,
        multirow: Optional[bool_t] = ...,
        caption: Optional[str_t] = ...,
        label: Optional[str_t] = ...,
    ) -> str_t: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[FilePathOrBuffer],
        sep: str_t = ...,
        na_rep: str_t = ...,
        float_format: Optional[str_t] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[bool_t, List[str_t]] = ...,
        index: bool_t = ...,
        index_label: Optional[Union[bool_t, str_t, Sequence[Hashable]]] = ...,
        mode: str_t = ...,
        encoding: Optional[str_t] = ...,
        compression: Union[str_t, Mapping[str_t, str_t]] = ...,
        quoting: Optional[int] = ...,
        quotechar: str_t = ...,
        line_terminator: Optional[str_t] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[str_t] = ...,
        doublequote: bool_t = ...,
        escapechar: Optional[str_t] = ...,
        decimal: str_t = ...,
    ) -> None: ...
    @overload
    def to_csv(
        self,
        sep: str_t = ...,
        na_rep: str_t = ...,
        float_format: Optional[str_t] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[bool_t, List[str_t]] = ...,
        index: bool_t = ...,
        index_label: Optional[Union[bool_t, str_t, Sequence[Hashable]]] = ...,
        mode: str_t = ...,
        encoding: Optional[str_t] = ...,
        compression: Union[str_t, Mapping[str_t, str_t]] = ...,
        quoting: Optional[int] = ...,
        quotechar: str_t = ...,
        line_terminator: Optional[str_t] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[str_t] = ...,
        doublequote: bool_t = ...,
        escapechar: Optional[str_t] = ...,
        decimal: str_t = ...,
    ) -> str_t: ...
    def take(self, indices: Any, axis: Any=..., is_copy: Optional[bool_t]=..., **kwargs: Any) -> FrameOrSeries: ...
    def xs(
        self,
        key: Union[str_t, Tuple[str_t]],
        axis: SeriesAxisType = ...,
        level: Optional[Level] = ...,
        drop_level: bool_t = ...,
    ) -> Series[Dtype]: ...
    def __getitem__(self, item: Any) -> None: ...
    def __delitem__(self, idx: Union[int, str_t]): ...
    def get(self, key: object, default: Optional[Dtype] = ...) -> Dtype: ...
    def reindex_like(self, other: Any, method: Optional[str]=..., copy: bool_t=..., limit: Any=..., tolerance: Any=...) -> FrameOrSeries: ...
    def drop(self, labels: Any=..., axis: Any=..., index: Any=..., columns: Any=..., level: Any=..., inplace: bool_t=..., errors: str=...) -> Any: ...
    def add_prefix(self, prefix: str) -> FrameOrSeries: ...
    def add_suffix(self, suffix: str) -> FrameOrSeries: ...
    def sort_values(self, by: Any=..., axis: Any=..., ascending: Any=..., inplace: bool_t=..., kind: str=..., na_position: str=..., ignore_index: bool_t=...) -> Any: ...
    def sort_index(self, axis: Any=..., level: Any=..., ascending: bool_t=..., inplace: bool_t=..., kind: str=..., na_position: str=..., sort_remaining: bool_t=..., ignore_index: bool_t=...) -> Any: ...
    def reindex(self, *args: Any, **kwargs: Any) -> FrameOrSeries: ...
    def filter(self, items: Any=..., like: Optional[str]=..., regex: Optional[str]=..., axis: Any=...) -> FrameOrSeries: ...
    def head(self, n: int=...) -> FrameOrSeries: ...
    def tail(self, n: int=...) -> FrameOrSeries: ...
    def sample(self, n: Any=..., frac: Any=..., replace: Any=..., weights: Any=..., random_state: Any=..., axis: Any=...) -> FrameOrSeries: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def __finalize__(self, other: Any, method: Any=..., **kwargs: Any) -> FrameOrSeries: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    @property
    def values(self) -> np.ndarray: ...
    @property
    def dtypes(self): ...
    def astype(self, dtype: Any, copy: bool_t=..., errors: str=...) -> FrameOrSeries: ...
    def copy(self, deep: bool_t=...) -> FrameOrSeries: ...
    def __copy__(self, deep: bool_t=...) -> FrameOrSeries: ...
    def __deepcopy__(self, memo: Any=...) -> FrameOrSeries: ...
    def infer_objects(self) -> FrameOrSeries: ...
    def convertDTypes(self, infer_objects: bool_t=..., convertstr_ting: bool_t=..., convert_integer: bool_t=..., convertbool_tean: bool_t=...) -> FrameOrSeries: ...
    def fillna(self, value: Any=..., method: Any=..., axis: Any=..., inplace: bool_t=..., limit: Any=..., downcast: Any=...) -> Optional[FrameOrSeries]: ...
    def ffill(self, axis: Any=..., inplace: bool_t=..., limit: Any=..., downcast: Any=...) -> Optional[FrameOrSeries]: ...
    def bfill(self, axis: Any=..., inplace: bool_t=..., limit: Any=..., downcast: Any=...) -> Optional[FrameOrSeries]: ...
    def replace(self, to_replace: Optional[Any] = ..., value: Optional[Any] = ..., inplace: bool_t = ..., limit: Optional[Any] = ..., regex: bool_t = ..., method: str_t = ...): ...
    def interpolate(self, method: str = ..., axis: int = ..., limit: Optional[Any] = ..., inplace: bool_t = ..., limit_direction: str = ..., limit_area: Optional[Any] = ..., downcast: Optional[Any] = ..., **kwargs: Any): ...
    def asof(self, where: Any, subset: Optional[Any] = ...): ...
    def isna(self) -> FrameOrSeries: ...
    def isnull(self) -> FrameOrSeries: ...
    def notna(self) -> FrameOrSeries: ...
    def notnull(self) -> FrameOrSeries: ...
    def clip(self, lower: Any=..., upper: Any=..., axis: Any=..., inplace: bool_t=..., *args: Any, **kwargs: Any) -> FrameOrSeries: ...
    def asfreq(self, freq: Any, method: Any=..., how: Optional[str]=..., normalize: bool_t=..., fill_value: Any=...) -> FrameOrSeries: ...
    def at_time(self, time: Any, asof: bool_t=..., axis: Any=...) -> FrameOrSeries: ...
    def between_time(self, start_time: Any, end_time: Any, include_start: bool_t=..., include_end: bool_t=..., axis: Any=...) -> FrameOrSeries: ...
    def resample(self, rule: Any, axis: Any=..., closed: Optional[str]=..., label: Optional[str]=..., convention: str=..., kind: Optional[str]=..., loffset: Any=..., base: int=..., on: Any=..., level: Any=...) -> Any: ...
    def first(self, offset: Any) -> FrameOrSeries: ...
    def last(self, offset: Any) -> FrameOrSeries: ...
    def rank(self, axis: Any=..., method: str=..., numeric_only: Optional[bool_t]=..., na_option: str=..., ascending: bool_t=..., pct: bool_t=...) -> FrameOrSeries: ...
    def align(self, other: Any, join: str = ..., axis: Optional[Any] = ..., level: Optional[Any] = ..., copy: bool_t = ..., fill_value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ..., fill_axis: int = ..., broadcast_axis: Optional[Any] = ...): ...
    def where(self, cond: Any, other: Any = ..., inplace: bool = ..., axis: Optional[Any] = ..., level: Optional[Any] = ..., errors: str = ..., try_cast: bool_t = ...): ...
    def mask(self, cond: Any, other: Any = ..., inplace: bool = ..., axis: Optional[Any] = ..., level: Optional[Any] = ..., errors: str = ..., try_cast: bool_t = ...): ...
    def shift(self, periods: Any=..., freq: Any=..., axis: Any=..., fill_value: Any=...) -> FrameOrSeries: ...
    def slice_shift(self, periods: int=..., axis: Any=...) -> FrameOrSeries: ...
    def tshift(self, periods: int=..., freq: Any=..., axis: Any=...) -> FrameOrSeries: ...
    def truncate(self, before: Any=..., after: Any=..., axis: Any=..., copy: bool_t=...) -> FrameOrSeries: ...
    def tz_convert(self, tz: Any, axis: Any=..., level: Any=..., copy: bool_t=...) -> FrameOrSeries: ...
    def tz_localize(self, tz: Any, axis: Any=..., level: Any=..., copy: bool_t=..., ambiguous: Any=..., nonexistent: str=...) -> FrameOrSeries: ...
    def abs(self) -> FrameOrSeries: ...
    def describe(self, percentiles: Any=..., include: Any=..., exclude: Any=...) -> FrameOrSeries: ...
    def pct_change(self, periods: Any=..., fill_method: Any=..., limit: Any=..., freq: Any=..., **kwargs: Any) -> FrameOrSeries: ...
    def transform(self, func: Any, *args: Any, **kwargs: Any): ...
    def first_valid_index(self): ...
    def last_valid_index(self): ...


from pandas.core.series import Series as Series