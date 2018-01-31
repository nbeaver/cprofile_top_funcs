Python 2 and 3 are not compatible.

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
