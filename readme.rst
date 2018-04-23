Example usage::

    $ cat run.py
    import math
    if __name__ == '__main__':
        _ = [math.sqrt(i) for i in range(10**6)]
    $ python3 -m cProfile -o out3.prof run.py
    $ cprofile3_top_funcs.py out3.prof
    Fri Apr 13 12:14:52 2018    out3.prof

             1000060 function calls in 0.558 seconds

       Ordered by: internal time
       List reduced from 47 to 3 due to restriction <3>

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.321    0.321    0.557    0.557 run.py:3(<listcomp>)
      1000000    0.236    0.000    0.236    0.000 {built-in method math.sqrt}
            1    0.000    0.000    0.000    0.000 {built-in method _imp.create_builtin}

Python 2 and 3 are not compatible.
To work around this,
the Makefile generates two scripts,
one for Python 2 and one for Python 3.
They are identical except for the shebang and filename.

Example traceback::

    Traceback (most recent call last):
      File "./cprofile_top_funcs.py", line 35, in <module>
        stats = pstats.Stats(filepath)
      File "/usr/lib/python2.7/pstats.py", line 81, in __init__
        self.init(arg)
      File "/usr/lib/python2.7/pstats.py", line 95, in init
        self.load_stats(arg)
      File "/usr/lib/python2.7/pstats.py", line 110, in load_stats
        self.stats = marshal.load(f)
    ValueError: bad marshal data (unknown type code)

https://stackoverflow.com/questions/25999882/bad-marshal-error-runsnake

https://github.com/jiffyclub/snakeviz/issues/31
