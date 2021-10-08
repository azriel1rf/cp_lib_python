from copy import deepcopy
from itertools import product

import pytest
from tiny_algos.minmultiset import MaxMultiSet, MinMultiSet
from tiny_algos.multiset import MultiSet

PINF = 9223372036854775807  # 2 ** 63 - 1
NINF = -PINF
MIN_DEFAULT = PINF
MAX_DEFAULT = NINF


class ScenarioWrapper:
    def __init__(self, base, action, description):
        self.base = base
        self.action = action
        self.description = description

    def __repr__(self):
        return f'"{self.description}"'


scenarios = [
    ScenarioWrapper(
        base=[],
        action=[
            ("add", 1),
            ("add", 2),
            ("add", -1),
        ],
        description="construct with empty list",
    ),
    ScenarioWrapper(
        base=[1, -1],
        action=[
            ("remove", 1),
            ("remove", -1),
            ("add", 1),
            ("add", -1),
        ],
        description="Remove all and add",
    ),
    ScenarioWrapper(
        base=[0, 1, 1, 2],
        action=[
            ("add", 3),
            ("add", 2),
            ("add", -1),
            ("add", -2),
        ],
        description="add",
    ),
    ScenarioWrapper(
        base=[0, 1, 1, 2],
        action=[
            ("remove", 1),
            ("remove", 2),
            ("remove", 0),
        ],
        description="remove",
    ),
    ScenarioWrapper(
        base=[2, 4, 0, 2],
        action=[
            ("add", 3),
            ("remove", 4),
            ("add", 1),
            ("remove", 0),
            ("add", 1),
            ("add", 3),
            ("remove", 1),
            ("remove", 3),
            ("remove", 1),
            ("remove", 2),
        ],
        description="add and remove",
    ),
]


class MultiSetWrapper:
    def __init__(self, ms_cls, extremes):
        self.ms_cls = ms_cls
        self.extremes = extremes

    def __repr__(self):
        return self.ms_cls.__name__


multisets = [
    MultiSetWrapper(MultiSet, extremes=("min", "max")),
    MultiSetWrapper(MinMultiSet, extremes=("min")),
    MultiSetWrapper(MaxMultiSet, extremes=("max")),
]


@pytest.mark.parametrize(
    ["scenario_wrapper", "multiset_wrapper"],
    product(scenarios, multisets),
)
def test_multiset(scenario_wrapper, multiset_wrapper):
    ms_cls = multiset_wrapper.ms_cls
    extremes = multiset_wrapper.extremes
    base = deepcopy(scenario_wrapper.base)
    action = deepcopy(scenario_wrapper.action)
    test_list = list(base)
    test_ms = ms_cls(list(base))

    def check_extremes():
        if "min" in extremes:
            assert test_ms.min == min(test_list, default=MIN_DEFAULT)
        if "max" in extremes:
            assert test_ms.max == max(test_list, default=MAX_DEFAULT)

    check_extremes()

    for action, value in action:
        if action == "add":
            test_list.append(value)
            test_ms.add(value)
        elif action == "remove":
            test_list.remove(value)
            test_ms.remove(value)
        check_extremes()
