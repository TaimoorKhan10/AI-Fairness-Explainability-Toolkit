"""
Core module for the AI Fairness and Explainability Toolkit (AFET).

This module provides the core functionality for fairness metrics, bias mitigation,
and model explainability.
"""

from .fairness_metrics import FairnessMetrics
from .bias_mitigation import PrejudiceRemover, Reweighing, CalibratedEqualizedOddsPostprocessing
from .model_comparison import ModelComparator
from .explainability import ModelExplainer
from .intersectional_fairness import IntersectionalFairnessMetrics

__all__ = [
    'FairnessMetrics',
    'PrejudiceRemover',
    'Reweighing',
    'CalibratedEqualizedOddsPostprocessing',
    'ModelComparator',
    'ModelExplainer',
    'IntersectionalFairnessMetrics'
]
