# Installation #
- install python3.8 (available in ubuntu software)
- install python3-env
```
> sudo apt-get install python3-venv
```
- create a virtual-env where you want
```
> sudo python3 -m venv /home/rhr/Workspace/venv/cookbook
```
- activate the virtual-env and 
```
> cd /home/rhr/Workspace/venv/cookbook/bin
> source activate
```
(cookbook) shoul be displayed at the start of the command line
- install package
in the same console where virtual-env is activated
```
> pip3 install -r requirements.txt
```
# Manual Launch #
make sure all requirements are installed and virtual-env is activated
```
> cd Flask
> python run.py
```
```
 * Serving Flask app "run" (lazy loading)
 * Environment: testing
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 137-343-485
```
# Scripted Launch #
you need to update Flask/start_server.sh with your config
```
> cd Flask
> source ./start_server.sh
```
# Raspberry Launch #
- power on raspberry (check ethernet is connected)
- get ip's raspberry  (bbox tools or cmd "arp -a" on linux)
- go to https://ip_raspberry:9090
- log in (ask for login/password)
- go in terminal tab
- lanch with script
```
> cd Workspace/Cookbook/Flask
> ./start_server.sh
```

# Documentation # 
https://apidocjs.com/
- install node.js
- install nodemodule apidoc
```
> sudo npm install -g apidoc
```
- generate the doc
```
> cd Flask
> apidoc -i ../Flask/ -o ../apidoc/
```
- see documentation
```
> cd Cookbook/apidoc
```
Open it with index.html
# Tests #
```
> cd Flask
> python -W ignore -m pytest tests/to/be/done
```
### TBD ###
- conf
``` 
export COOKBOOK_ENV="path/to/config.cfg"
```