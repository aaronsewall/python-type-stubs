from numpy.typing import NDArray, ArrayLike
from numpy import float64, int64, ndarray
from collections.abc import Iterable
from sklearn.pipeline import Pipeline, FeatureUnion
from typing import (
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
    Any,
    Mapping,
    Sequence,
)

# Author: Edouard Duchesnay
#         Gael Varoquaux
#         Virgile Fritsch
#         Alexandre Gramfort
#         Lars Buitinck
# License: BSD

from collections import defaultdict
from itertools import islice

import numpy as np
from scipy import sparse
from joblib import Parallel

from .base import clone, TransformerMixin
from .preprocessing import FunctionTransformer
from .utils._estimator_html_repr import _VisualBlock
from .utils.metaestimators import available_if
from .utils import (
    Bunch,
    _print_elapsed_time,
)
from .utils.deprecation import deprecated
from .utils._tags import _safe_tags
from .utils.validation import check_memory
from .utils.validation import check_is_fitted
from .utils.fixes import delayed
from .exceptions import NotFittedError

from .utils.metaestimators import _BaseComposition
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.decomposition._pca import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection._univariate_selection import SelectKBest
from sklearn.utils._bunch import Bunch

__all__ = ["Pipeline", "FeatureUnion", "make_pipeline", "make_union"]

def _final_estimator_has(attr: str) -> Callable: ...

class Pipeline(_BaseComposition):

    # BaseEstimator interface
    _required_parameters: list = ...

    def __init__(
        self,
        steps: List[Any],
        *,
        memory: str | Memory | None = None,
        verbose: bool = False
    ) -> None: ...
    def get_params(self, deep: bool = True) -> Mapping[str, Any]: ...
    def set_params(self, **kwargs) -> "Pipeline": ...
    def _validate_steps(self) -> None: ...
    def _iter(
        self, with_final: bool = True, filter_passthrough: bool = True
    ) -> Iterator[Any]: ...
    def __len__(self): ...
    def __getitem__(self, ind: Union[int, slice]) -> BaseEstimator: ...
    @property
    def _estimator_type(self) -> str: ...
    @property
    def named_steps(self) -> Bunch: ...
    @property
    def _final_estimator(self) -> BaseEstimator: ...
    def _log_message(self, step_idx: int) -> Optional[str]: ...
    def _check_fit_params(self, **fit_params) -> Dict[str, Dict[Any, Any]]: ...

    # Estimator interface

    def _fit(
        self,
        X: Union[DataFrame, ndarray, csr_matrix, List[str]],
        y: Optional[Union[List[int], Series, ndarray, List[int64]]] = None,
        **fit_params_steps
    ) -> Union[ndarray, csr_matrix, List[Dict[str, int]]]: ...
    def fit(
        self, X: Iterable, y: Iterable | None = None, **fit_params
    ) -> "Pipeline": ...
    def fit_transform(
        self, X: Iterable, y: Iterable | None = None, **fit_params
    ) -> np.ndarray: ...
    @available_if(_final_estimator_has("predict"))
    def predict(self, X: Iterable, **predict_params) -> NDArray: ...
    @available_if(_final_estimator_has("fit_predict"))
    def fit_predict(
        self, X: Iterable, y: Iterable | None = None, **fit_params
    ) -> NDArray: ...
    @available_if(_final_estimator_has("predict_proba"))
    def predict_proba(self, X: Iterable, **predict_proba_params) -> np.ndarray: ...
    @available_if(_final_estimator_has("decision_function"))
    def decision_function(self, X: Iterable) -> np.ndarray: ...
    @available_if(_final_estimator_has("score_samples"))
    def score_samples(self, X: Iterable) -> NDArray: ...
    @available_if(_final_estimator_has("predict_log_proba"))
    def predict_log_proba(
        self, X: Iterable, **predict_log_proba_params
    ) -> np.ndarray: ...
    def _can_transform(self) -> bool: ...
    @available_if(_can_transform)
    def transform(self, X: Iterable) -> np.ndarray: ...
    def _can_inverse_transform(self) -> bool: ...
    @available_if(_can_inverse_transform)
    def inverse_transform(self, Xt: ArrayLike) -> NDArray: ...
    @available_if(_final_estimator_has("score"))
    def score(
        self,
        X: Iterable,
        y: Iterable | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> float: ...
    @property
    def classes_(self) -> ndarray: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def get_feature_names_out(
        self, input_features: ArrayLike | None = None
    ) -> np.ndarray: ...
    @property
    def n_features_in_(self) -> int: ...
    @property
    def feature_names_in_(self): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def _sk_visual_block_(self): ...

def _name_estimators(estimators: Any) -> List[Any]: ...
def make_pipeline(
    *steps, memory: str | Memory | None = None, verbose: bool = False
) -> Pipeline: ...
def _transform_one(
    transformer: Union[PCA, Pipeline, SelectKBest, TfidfVectorizer],
    X: ndarray,
    y: None,
    weight: Optional[float],
    **fit_params
) -> Union[ndarray, csr_matrix]: ...
def _fit_transform_one(
    transformer: BaseEstimator,
    X: Union[DataFrame, ndarray, csr_matrix, List[str]],
    y: Optional[Union[Series, ndarray, List[int64], List[int]]],
    weight: Optional[float],
    message_clsname: str = "",
    message: Optional[str] = None,
    **fit_params
) -> Any: ...
def _fit_one(
    transformer: Union[PCA, SelectKBest],
    X: ndarray,
    y: ndarray,
    weight: None,
    message_clsname: str = "",
    message: None = None,
    **fit_params
) -> Union[PCA, SelectKBest]: ...

class FeatureUnion(TransformerMixin, _BaseComposition):

    _required_parameters: list = ...

    def __init__(
        self,
        transformer_list: Sequence[tuple[str, Transformer]],
        *,
        n_jobs: int | None = None,
        transformer_weights: Mapping | None = None,
        verbose: bool = False
    ) -> None: ...
    def get_params(self, deep: bool = True) -> Mapping[str, Any]: ...
    def set_params(self, **kwargs) -> "FeatureUnion": ...
    def _validate_transformers(self) -> None: ...
    def _validate_transformer_weights(self) -> None: ...
    def _iter(
        self,
    ) -> Iterator[Union[Tuple[str, PCA, None], Tuple[str, SelectKBest, None]]]: ...
    @deprecated(
        "get_feature_names is deprecated in 1.0 and will be removed "
        "in 1.2. Please use get_feature_names_out instead."
    )
    def get_feature_names(self) -> ArrayLike: ...
    def get_feature_names_out(
        self, input_features: ArrayLike | None = None
    ) -> np.ndarray: ...
    def fit(
        self, X: Iterable | ArrayLike, y: ArrayLike | None = None, **fit_params
    ) -> "FeatureUnion": ...
    def fit_transform(
        self, X: Iterable | ArrayLike, y: ArrayLike | None = None, **fit_params
    ) -> ArrayLike | NDArray: ...
    def _log_message(self, name: str, idx: int, total: int) -> None: ...
    def _parallel_func(
        self, X: ndarray, y: ndarray, fit_params: Dict[Any, Any], func: Callable
    ) -> List[
        Union[Tuple[ndarray, PCA], Tuple[ndarray, SelectKBest], PCA, SelectKBest]
    ]: ...
    def transform(self, X: Iterable | ArrayLike) -> ArrayLike | NDArray: ...
    def _hstack(self, Xs: Union[Tuple[ndarray, ndarray], List[ndarray]]) -> ndarray: ...
    def _update_transformer_list(
        self,
        transformers: Union[Tuple[PCA, SelectKBest], List[Union[PCA, SelectKBest]]],
    ) -> None: ...
    @property
    def n_features_in_(self): ...
    def __sklearn_is_fitted__(self): ...
    def _sk_visual_block_(self): ...

def make_union(
    *transformers, n_jobs: int | None = None, verbose: bool = False
) -> FeatureUnion: ...