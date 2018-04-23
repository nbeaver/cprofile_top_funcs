PY :=cprofile2_top_funcs.py cprofile3_top_funcs.py
PROF :=out2.prof out3.prof

.PHONY : all profile clean

all : $(PY) $(PROF)
	./cprofile2_top_funcs.py out2.prof
	./cprofile3_top_funcs.py out3.prof

cprofile2_top_funcs.py : cprofile_top_funcs.py
	printf '#! /usr/bin/env python2\n' > $@
	cat $< >> $@
	chmod +x $@

cprofile3_top_funcs.py : cprofile_top_funcs.py
	printf '#! /usr/bin/env python3\n' > $@
	cat $< >> $@
	chmod +x $@

profile : $(PROF)

out2.prof : run.py
	python2 -m cProfile -o $@ $<

out3.prof : run.py
	python3 -m cProfile -o $@ $<

readme.html : readme.rst
	rst2html $< $@

clean :
	rm -f -- $(PY) $(PROF) readme.html
