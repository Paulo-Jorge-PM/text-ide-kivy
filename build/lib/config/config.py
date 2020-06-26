#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'config.ini')

config = configparser.ConfigParser()
config.read(file)

def writeConfig(section, var, value):
    config[section][var] = value
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

#getint
#getfloat
#getboolean

#Create python vars dinamicamente
for section in config.sections():
    for key in config[section]:
        #exec("%s='%s'" % (key,config[section][key]))
        globals()[key] = config[section][key]

#language = config['CORE']['lang']
#fullscreen = config['GUI'].getboolean('fullscreen')
