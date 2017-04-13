upload :
	python setup.py sdist upload -r pypi

reinstall2 :
	sudo pip uninstall vernam -y && sudo pip install vernam

reinstall3 :
	sudo pip3 uninstall vernam -y && sudo pip3 install vernam