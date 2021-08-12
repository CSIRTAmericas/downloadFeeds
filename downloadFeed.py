# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:42:57 2021

@author: Nelson Guanilo (nguanilo@csirtamericas.org)
"""
import os, ftplib, ast 
from datetime import datetime
from pytz import timezone

FTPUSER = "" # User provided by CSIRTAmericas teams
FTPPASS = "" # Password provided by CSIRTAmericas teams
FTPSERVER = "" # En caso no la sepa, consultar con el equipo
DSTFOLDER = "" # Destination folder for feeds. Ex: /home/user/python || D:\\python


path=["/"]


def savedDictionary(dict_file):
    # Saving the data of downloaded feeds and their modification date
    dict_file = str(dict_file)
    with open('feed.csv', mode='w') as f:
        f.write(dict_file)
    f.close()

def openFileSaved(today):
    # Open saved feed data
    if not os.path.exists('feed.csv'):
        f = open("feed.csv", "x")
        f.close()
    
    with open('feed.csv') as fd:
        reader=fd.readlines()
    fd.close()
    dict_file = {}
    if reader:
        dict_file = ast.literal_eval(str(reader[0]))
        if dict_file.get("date"):
            if dict_file["date"] != today:
                dict_file = {}
                dict_file["date"] = today
        else:
            dict_file["date"] = today
    else:
        dict_file["date"] = today
    return dict_file


def timezoneDateTime():
    # Get the time the server works with
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    eastern = timezone('US/Eastern')
    loc_dt = datetime.now(eastern)
    today = (loc_dt).strftime('%Y%m%d')
    return today

def checkUpdate(file,ftp,dict_file):
    # Check if there are any updated files
    cmd_command = "MDTM " + ftp.pwd() + "/" + file
    timestamp = ftp.voidcmd(cmd_command)[4:].strip()
    if file not in dict_file:
        dict_file[file] = timestamp
        downloadFiles(file,ftp)

    elif dict_file.get(file) != timestamp:
        dict_file[file] = timestamp
        downloadFiles(file,ftp)

def downloadFiles(file,ftp):
    # Direct feeds from your country and trends related with subregions (South, North, Central, Caribbean)
    print("[*] Download = ", file, " [*] " )
    with open(os.path.join(DSTFOLDER,file), 'wb') as f:
        ftp.retrbinary('RETR ' + file, f.write)

def getTodayFiles(list_file,ftp,dict_file,today,dire):
    for file in list_file:
        if "-" in file and "csv" in file:
            file_date = file.split("-")
            try:
                if int(file_date[0]) >= int(today):
                    checkUpdate(file,ftp,dict_file)
                else:
                    break
            except Exception as e:
                print("Error: ", e)

        elif "_" in file and "csv" in file:
            file_date = file.split("_")
            try:
                if int(file_date[0]) == int(today[0:6]):
                    checkUpdate(file,ftp,dict_file)
                else:
                    break
            except Exception as e:
                print("Error: ", e)
        
        elif "csv" in file:
            continue

        else:
            if dire == "/":
                new_dire = "/" + file
            else:
                new_dire = dire + "/" + file
            path_dic = [new_dire]
            main(dict_file,today, path_dic, ftp)

def main(dict_file,today,path,ftp):
    try:    
        for dire in path:
            if dire != "/" and "discontinued" not in dire:
                ftp.cwd('/'+dire+'/')
            list_file =  ftp.nlst()
            list_file = sorted(list_file,reverse=True)
            if list_file:
                getTodayFiles(list_file,ftp,dict_file,today,dire)

    except Exception as e:
        print("Error: ", e)

    

if __name__ == '__main__':
    print("[!] Starting the process [!]")
    today = timezoneDateTime()
    dict_file = openFileSaved(today)
    try:    
        ftp = ftplib.FTP(FTPSERVER, FTPUSER, FTPPASS)
        main(dict_file,today, path, ftp)
    except Exception as e:
        print("Error: ", e)
    ftp.close()
    savedDictionary(dict_file)
    print("[!] End the process [!]")
