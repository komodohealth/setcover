from src.cover import WeightedSetCoverProblem
from src.set import WeightedSet
import pytest

# TODO Move mock test data to another file
test_weighted_sets = [
    WeightedSet(set_id="A10", subset=["Glenn"], weight=100.0),
    WeightedSet(set_id="B20", subset=["Jeremy", "Ben"], weight=200.0),
    WeightedSet(set_id="C30", subset=["Jeremy"], weight=300.0),
    WeightedSet(set_id="D40", subset=["Jeremy", "Ben"], weight=400.0),
    WeightedSet(set_id="E50", subset=["Justin", "Vijay"], weight=500.0),
]


def test_wscp():
    cover_problem = WeightedSetCoverProblem(test_weighted_sets)
    assert cover_problem
    assert cover_problem.set_problem == {
        "Glenn": {"A10"},
        "Jeremy": {"B20", "D40", "C30"},
        "Ben": {"B20", "D40"},
        "Justin": {"E50"},
        "Vijay": {"E50"},
    }
    assert set(cover_problem.set_problem.keys()) == {
        "Glenn",
        "Jeremy",
        "Ben",
        "Justin",
        "Vijay",
    }
    assert cover_problem.subsets == {
        "A10": {"Glenn"},
        "B20": {"Jeremy", "Ben"},
        "C30": {"Jeremy"},
        "D40": {"Jeremy", "Ben"},
        "E50": {"Justin", "Vijay"},
    }
    assert cover_problem.weights == {
        "A10": 100,
        "B20": 200,
        "C30": 300,
        "D40": 400,
        "E50": 500,
    }
    q = cover_problem.set_queue
    assert q.pop_task() == "A10"
    assert q.pop_task() == "B20"
    assert q.pop_task() == "D40"
    assert q.pop_task() == "E50"
    assert q.pop_task() == "C30"


# @pytest.mark.skip
def test_solver():
    cover_problem = WeightedSetCoverProblem(test_weighted_sets)
    assert cover_problem
    assert cover_problem.cover_solution
    print(cover_problem.universe)
    print(cover_problem.cover_solution)
    print(cover_problem.covered)
    print(cover_problem.weight_total)