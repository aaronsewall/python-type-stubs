from typing import Optional, Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Vincent Michel <vincent.michel@inria.fr>
#         Minor fixes by Fabian Pedregosa
#         Amit Aides <amitibo@tx.technion.ac.il>
#         Yehuda Finkelstein <yehudaf@tx.technion.ac.il>
#         Lars Buitinck
#         Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
#         (parts based on earlier work by Mathieu Blondel)
#
# License: BSD 3 clause
import warnings

from abc import ABCMeta, abstractmethod

import numpy as np
from scipy.special import logsumexp

from .base import BaseEstimator, ClassifierMixin
from .preprocessing import binarize
from .preprocessing import LabelBinarizer
from .preprocessing import label_binarize
from .utils import deprecated
from .utils.extmath import safe_sparse_dot
from .utils.multiclass import _check_partial_fit_first_call
from .utils.validation import check_is_fitted, check_non_negative
from .utils.validation import _check_sample_weight
from numpy import float64, ndarray
from scipy.sparse._csr import csr_matrix

__all__ = [
    "BernoulliNB",
    "GaussianNB",
    "MultinomialNB",
    "ComplementNB",
    "CategoricalNB",
]

class _BaseNB(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def _joint_log_likelihood(self, X): ...
    @abstractmethod
    def _check_X(self, X): ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def predict_log_proba(self, X: ArrayLike) -> ArrayLike: ...
    def predict_proba(self, X: ArrayLike) -> ArrayLike: ...

class GaussianNB(_BaseNB):
    def __init__(
        self, *, priors: ArrayLike | None = None, var_smoothing: float = 1e-9
    ) -> None: ...
    def fit(
        self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None
    ) -> "GaussianNB": ...
    def _check_X(self, X: ndarray) -> ndarray: ...
    @staticmethod
    def _update_mean_variance(
        n_past: float64,
        mu: ndarray,
        var: ndarray,
        X: ndarray,
        sample_weight: Optional[ndarray] = None,
    ) -> Tuple[ndarray, ndarray]: ...
    def partial_fit(
        self,
        X: ArrayLike,
        y: ArrayLike,
        classes: ArrayLike | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def _partial_fit(
        self,
        X: ndarray,
        y: ndarray,
        classes: Optional[ndarray] = None,
        _refit: bool = False,
        sample_weight: Optional[ndarray] = None,
    ) -> "GaussianNB": ...
    def _joint_log_likelihood(self, X: ndarray) -> ndarray: ...
    @deprecated(  # type: ignore
        "Attribute `sigma_` was deprecated in 1.0 and will be removed in"
        "1.2. Use `var_` instead."
    )
    @property
    def sigma_(self): ...

_ALPHA_MIN: float = ...

class _BaseDiscreteNB(_BaseNB):
    @abstractmethod
    def _count(self, X, Y): ...
    @abstractmethod
    def _update_feature_log_prob(self, alpha): ...
    def _check_X(self, X: csr_matrix) -> csr_matrix: ...
    def _check_X_y(
        self, X: csr_matrix, y: ndarray, reset: bool = True
    ) -> Tuple[csr_matrix, ndarray]: ...
    def _update_class_log_prior(self, class_prior: None = None) -> None: ...
    def _check_alpha(self) -> Union[float, float64]: ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        classes: ArrayLike | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "MultinomialNB": ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Union[BernoulliNB, ComplementNB]: ...
    def _init_counters(self, n_classes: int, n_features: int) -> None: ...
    def _more_tags(self): ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `n_features_` was deprecated in version 1.0 and will be "
        "removed in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...

class MultinomialNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_prior: bool = True,
        class_prior: ArrayLike | None = None
    ) -> None: ...
    def _more_tags(self): ...
    def _count(self, X: csr_matrix, Y: ndarray) -> None: ...
    def _update_feature_log_prob(self, alpha: float) -> None: ...
    def _joint_log_likelihood(self, X: csr_matrix) -> ndarray: ...

class ComplementNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_prior: bool = True,
        class_prior: ArrayLike | None = None,
        norm: bool = False
    ) -> None: ...
    def _more_tags(self): ...
    def _count(self, X: csr_matrix, Y: ndarray) -> None: ...
    def _update_feature_log_prob(self, alpha: Union[float, float64]) -> None: ...
    def _joint_log_likelihood(self, X: csr_matrix) -> ndarray: ...

class BernoulliNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        binarize: float | None = 0.0,
        fit_prior: bool = True,
        class_prior: ArrayLike | None = None
    ) -> None: ...
    def _check_X(self, X: csr_matrix) -> csr_matrix: ...
    def _check_X_y(
        self, X: csr_matrix, y: ndarray, reset: bool = True
    ) -> Tuple[csr_matrix, ndarray]: ...
    def _count(self, X: csr_matrix, Y: ndarray) -> None: ...
    def _update_feature_log_prob(self, alpha: float) -> None: ...
    def _joint_log_likelihood(self, X: csr_matrix) -> ndarray: ...

class CategoricalNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_prior: bool = True,
        class_prior: ArrayLike | None = None,
        min_categories: int | ArrayLike | None = None
    ): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        classes: ArrayLike | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> Any: ...
    def _more_tags(self): ...
    def _check_X(self, X): ...
    def _check_X_y(self, X, y, reset=True): ...
    def _init_counters(self, n_classes, n_features): ...
    @staticmethod
    def _validate_n_categories(X, min_categories): ...
    def _count(self, X, Y): ...
    def _update_feature_log_prob(self, alpha): ...
    def _joint_log_likelihood(self, X): ...