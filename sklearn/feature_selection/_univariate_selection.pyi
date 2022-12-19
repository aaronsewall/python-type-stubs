from typing import Dict, Tuple, Union, Callable, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: V. Michel, B. Thirion, G. Varoquaux, A. Gramfort, E. Duchesnay.
#          L. Buitinck, A. Joly
# License: BSD 3 clause

import numpy as np
import warnings

from scipy import special, stats
from scipy.sparse import issparse

from ..base import BaseEstimator
from ..preprocessing import LabelBinarizer
from ..utils import as_float_array, check_array, check_X_y, safe_sqr, safe_mask
from ..utils.extmath import safe_sparse_dot, row_norms
from ..utils.validation import check_is_fitted
from ._base import SelectorMixin
from numpy import matrix, ndarray

def _clean_nans(scores: ndarray) -> ndarray: ...

######################################################################
# Scoring functions

# The following function is a rewriting of scipy.stats.f_oneway
# Contrary to the scipy.stats.f_oneway implementation it does not
# copy the data while keeping the inputs unchanged.
def f_oneway(*args) -> tuple[float, float]: ...
def f_classif(X: NDArray | ArrayLike, y: NDArray) -> tuple[NDArray, NDArray]: ...
def _chisquare(f_obs: ndarray, f_exp: matrix) -> Tuple[ndarray, ndarray]: ...
def chi2(X: NDArray | ArrayLike, y: ArrayLike) -> tuple[NDArray, NDArray]: ...
def r_regression(
    X: NDArray | ArrayLike,
    y: ArrayLike,
    *,
    center: bool = True,
    force_finite: bool = True
) -> NDArray: ...
def f_regression(
    X: NDArray | ArrayLike,
    y: ArrayLike,
    *,
    center: bool = True,
    force_finite: bool = True
) -> tuple[NDArray, NDArray]: ...

######################################################################
# Base classes

class _BaseFilter(SelectorMixin, BaseEstimator):
    def __init__(self, score_func: Callable) -> None: ...
    def fit(
        self, X: ArrayLike, y: ArrayLike
    ) -> Union[SelectPercentile, SelectKBest]: ...
    def _check_params(self, X, y): ...
    def _more_tags(self) -> Dict[str, bool]: ...

######################################################################
# Specific filters
######################################################################
class SelectPercentile(_BaseFilter):
    def __init__(self, score_func: Callable = ..., *, percentile: int = 10) -> None: ...
    def _check_params(self, X: ndarray, y: ndarray) -> None: ...
    def _get_support_mask(self) -> ndarray: ...

class SelectKBest(_BaseFilter):
    def __init__(
        self, score_func: Callable = ..., *, k: int | Literal["all"] = 10
    ) -> None: ...
    def _check_params(self, X: ndarray, y: ndarray) -> None: ...
    def _get_support_mask(self) -> ndarray: ...

class SelectFpr(_BaseFilter):
    def __init__(self, score_func: Callable = ..., *, alpha: float = 5e-2): ...
    def _get_support_mask(self): ...

class SelectFdr(_BaseFilter):
    def __init__(self, score_func: Callable = ..., *, alpha: float = 5e-2): ...
    def _get_support_mask(self): ...

class SelectFwe(_BaseFilter):
    def __init__(self, score_func: Callable = ..., *, alpha: float = 5e-2): ...
    def _get_support_mask(self): ...

######################################################################
# Generic filter
######################################################################

# TODO this class should fit on either p-values or scores,
# depending on the mode.
class GenericUnivariateSelect(_BaseFilter):

    _selection_modes: dict = ...

    def __init__(
        self,
        score_func: Callable = ...,
        *,
        mode: Literal["percentile", "k_best", "fpr", "fdr", "fwe"] = "percentile",
        param: float | int = 1e-5
    ): ...
    def _make_selector(self): ...
    def _more_tags(self): ...
    def _check_params(self, X, y): ...
    def _get_support_mask(self): ...