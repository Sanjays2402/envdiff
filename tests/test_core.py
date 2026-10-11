from envdiff import diff_envs, parse_env


def test_parse():
    env = parse_env('# c\nA=1\nexport B="two words"\nC=3 # note\n\nbad line\n')
    assert env == {"A": "1", "B": "two words", "C": "3"}


def test_diff():
    d = diff_envs({"A": "1", "B": "2", "C": "3"}, {"B": "2", "C": "x", "D": "4"})
    assert d == {"only_a": ["A"], "only_b": ["D"], "changed": ["C"]}
