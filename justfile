build:
  @git pull
  @pip install --upgrade pip
  @python -m pip install -r requirements.txt --upgrade
  @python -m pip install .
  @rm "pyproject.toml"

pypi:
  @git pull
  @pip install --upgrade pip
  @rm dist/* && python -m build
  @twine upload dist/*
  @python -m pip install -r requirements.txt --upgrade
  @python -m pip install .
  @rm "pyproject.toml"

git:
  @git pull
  @git add *
  @git commit -m "Automated pdtmp commit"
  @git push