# Python3 (3.x) package and config #

```
pip install -r requirements.txt
export COOKBOOK_ENV="path/to/config.cfg"
```

# Documentation # 
https://apidocjs.com/
```
npm install apidoc -g
apidoc -i ../Flask/ -o ../apidoc/
```

# Populate #
```
python populate.py
```

# Launch #
sur linux
```
source ./launcher.sh
python run.py
```
sur windows
```
sh launcher_w.sh
```

# Test #
```
python -W ignore -m pytest
```