import cProfile, pstats, io

def run_profiler(code: str):
    pr = cProfile.Profile()
    pr.enable()
    exec(code, {})
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(10)
    return s.getvalue()
