deploy : 
	python2.5 manage.py update $(DEPLOY)

clean :
	find . -name \*.pyc | xargs -n 100 rm
