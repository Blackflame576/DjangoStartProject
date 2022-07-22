#Modules
import os
import time
import subprocess
import json
import random
import shutil

#Variables
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&','*','(',')','+','-','=','_','?']
ScriptDir = os.path.dirname(os.path.abspath(__file__))
ProjectDir = ''
Settings = {}
NameProject = ''
PathProject = ''
Database = ''
Databases = '\n' + '1. SQLite 3' + '\n' + '2. PostgreSQL'
SECRET_KEY = ''
DEBUG = True
Debugs = '\n' + '1. True' + '\n' + '2. False'

#Code
def CreateProject(NameProject,PathProject):
  pass

def CreateApp(NameApp):
  pass

def GitInit(PathProject):
  os.chdir(PathProject)
  os.system('git init')
  
def GenerateSecretKey(NameProject):
  global SECRET_KEY
  SECRET_KEY = f'{NameProject}_SecretKey_'
def EditSettings(NameProject,PathProject):
#   os.chdir(os.path.join(PathProject,NameProject))
  if Database == 2:
    shutil.copy(os.path.join(ScriptDir,'SettingsPostgresql.py'),os.path.join(PathProject,NameProject))
  else:
    shutil.copy(os.path.join(ScriptDir,'SettingsSQLite.py'),os.path.join(PathProject,NameProject))
def Start():
  global NameProject
  global PathProject
  global Database
  global SECRET_KEY
  
  NameProject = input('Название проекта:')
  PathProject = input('Местоположение проекта(путь):')
  Database = input('Выберите базу данных:' + Databases)
  SECRET_KEY = 

if __name__ == '__main__':
  Start()
