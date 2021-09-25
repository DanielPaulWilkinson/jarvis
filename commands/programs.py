import os
import subprocess

def openVisualStudio():
    codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
    os.startfile(codePath)
    
def OpenPostMan():
    codePath = "C:\\Users\\dpwde\\AppData\\Local\\Postman\\postman.exe"
    os.startfile(codePath)

def OpenWhatsApp():
    codePath = "C:\\Users\\dpwde\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
    os.startfile(codePath)

def OpenProgramVisualStudioCode():
    codePath = "C:\\Users\\dpwde\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    os.startfile(codePath)

def launchMinecraft():
    codePath = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"
    os.startfile(codePath)

def launchSteam():
    codePath = "C:\\Program Files (x86)\\Steam\\steam.exe"
    os.startfile(codePath)

def launchAndroidStudio():
    codePath = "D:\\Android Studio\\bin\\studio64.exe"
    os.startfile(codePath)

def UpdateDeveloperDependencies():
    subprocess.check_call('npm -v')
    subprocess.check_call('npm install -g npm@latest')
    subprocess.check_call('npm -v')
