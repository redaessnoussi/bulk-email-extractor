import glob
import csv
import os
import time
from termcolor import colored

from tqdm import tqdm

# popular isp array
ispTOP = ["gmail","hotmail","outlook","msn","live","yahoo","gmx","web","t-online","aol","arcor","online","orange","tiscali","alice","home","planet","icloud"]
countryTOP = ["com","co.uk","de","nl","se","no","dk","fi","fr","it","at","com.au","co.nz"]

def writeEmails(emailClean):
    #clean data from duplicates
    a_set = set(emailClean)
    no_duplicates = list(a_set)
    # getting email
    for email in tqdm(no_duplicates):
        try:
            # getting email service provider DNS
            ispEmailDNS = email.split('@', 1)
            # getting email service provider name
            ispName = ispEmailDNS[1].split('.', 1)
            country = ispName[1]
            if (country not in countryTOP):
                country = 'international'
            # getting isp name for file rename
            isp = ispName[0]
            if (ispName[0] == "live" or ispName[0] == "hotmail" or ispName[0] == "msn"):
                isp = 'outlook'
            if(ispName[0] not in ispTOP):
                isp = 'others'
            # creating data directory
            # Check whether the specified path exists or not
            isExist = os.path.exists("fetched_data/" + country)
            if not isExist:
                os.mkdir("fetched_data/" + country)
            directory = "fetched_data/"+country
            # creating data list from isp name
            dataList = open(directory+"/" + isp + ".txt", "a")
            dataList.write(email + "\n")

        except:
             pass
    print("\n")

def openTXT(filename):
    # open text file
    my_file = open(filename, "r")
    content = my_file.read()
    contentArray = content.splitlines()
    rows = []
    for row in contentArray:
        # converting email delimiters and spliting
        emailClean = row.replace(';', ',').replace(':', ',').split(',', 1)
        rows.append(emailClean[0])
    writeEmails(rows)

def openCSV(fileName):
    # open csv file
    file = open(fileName)
    csvreader = csv.reader(file)
    # getting header csv file
    header = next(csvreader)
    # getting index of email column
    emailIndex = header.index("rcpt")
    rows = []
    for row in csvreader:
        rows.append(row[emailIndex])
    writeEmails(rows)
    file.close()

# getting files from data directory
allFiles = glob.glob("data/*")
print("\n")
print (colored("█▓▒­░⡷⠂  "+str(len(allFiles)) +" data files available found... ⠐⢾░▒▓█ \n" ,'red'))
cpt = 1;

for file in allFiles:
    print (colored("File "+str(cpt)+"/"+str(len(allFiles))+ "  is cleaning...",'red'))
    # getting extension of file name
    name, extension = os.path.splitext(file)
    if (extension == ".csv"):
        openCSV(file)
    if (extension == ".txt"):
        openTXT(file)
    cpt+=1