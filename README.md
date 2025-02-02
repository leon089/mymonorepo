git clone git@github.com:leon089/mymonorepo.git
 1456  cd mymonorepo
 1457  code .
 1458  touch services
 1459  touch pyproject.toml README.md
 1460* ll
 1461  pwd
 1462* cp name_extractor /Users/lihuagao/test/mymonorepo/services
 1463* cp -r name_extractor /Users/lihuagao/test/mymonorepo/services
 1464  md  services
 1465* cp -r name_extractor /Users/lihuagao/test/mymonorepo/services
 1466  cd services
 1467  poetry new data-processor\n

 ** venv
on project root
python3 -m venv venv
source venv/bin/activate

===
cd services 

poetry new data-processor
pyenv: poetry: command not found

The `poetry' command exists in these Python versions:
  3.9.16

Note: See 'pyenv help global' for tips on allowing both
      python2 and python3 to be found.

pyenv --version
pyenv local 3.9.16

===
python services/data-processor/data_processor/processor.py

==
copied name-extractor
pytest under name-extractor OK