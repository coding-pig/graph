from src import graph


def toposort(nodes):
    output = []
    done = set()
    while len(done) != len(nodes):
        done_new = []
        for node in nodes:
            if node in done:
                continue
            if not [v for v in node._to if v not in done]:
                done_new.append(node)
        output.append(done_new)
        for n in done_new:
            done.add(n)
    return output
