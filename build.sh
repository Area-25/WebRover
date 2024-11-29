rm -rf build/ dist/ *.egg-info/
python -m build
# python -m twine upload --repository testpypi dist/*

# main pypi upload
python -m twine upload dist/*