from cp_lib.multiset import MultiSet
from cp_lib.minmultiset import MinMultiSet, MaxMultiSet
from copy import deepcopy


test_bases = [
    [0, 1, 1, 2],
    [0, 1, 1, 2],
    [2, 4, 0, 2],
]

episodes = [
    [
        ("add", 3),
        ("add", 2),
        ("add", -1),
        ("add", -2),
    ],
    [
        ("remove", 1),
        ("remove", 2),
        ("remove", 0),
    ],
    [
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
]


def test_multiset():
    for test_base, episode in zip(test_bases, episodes):
        verify(MultiSet, test_base, episode, extremes=("min", "max"))


def test_minmultiset():
    for test_base, episode in zip(test_bases, episodes):
        verify(MinMultiSet, test_base, episode, extremes=("min"))


def test_maxmultiset():
    for test_base, episode in zip(test_bases, episodes):
        verify(MaxMultiSet, test_base, episode, extremes=("max"))


def verify(multiset_class, test_base, episode, extremes=("min", "max")):
    test_base = deepcopy(test_base)
    episode = deepcopy(episode)
    test_list = list(test_base)
    test_ms = multiset_class(list(test_base))

    def check_extremes():
        if "min" in extremes:
            assert test_ms.min == min(test_list)
        if "max" in extremes:
            assert test_ms.max == max(test_list)

    check_extremes()

    for action, value in episode:
        if action == "add":
            test_list.append(value)
            test_ms.add(value)
        elif action == "remove":
            test_list.remove(value)
            test_ms.remove(value)
        check_extremes()
