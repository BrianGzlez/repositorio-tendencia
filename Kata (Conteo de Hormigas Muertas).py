def dead_ants_count(ants: str) -> int:
    ant_parts = {'a': 0, 'n': 0, 't': 0}
    for char in ants:
        if char in ant_parts:
            ant_parts[char] += 1
    return max(ant_parts.values())

def test_dead_ants_count():
    assert dead_ants_count("...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t") == 1
    assert dead_ants_count("ant.ant.ant") == 0
    assert dead_ants_count("ant...ant...ant....ant") == 0
    assert dead_ants_count("a.n.t...ant") == 1

test_dead_ants_count()
