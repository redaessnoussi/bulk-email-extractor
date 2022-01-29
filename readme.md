# Email Extractor v1.0

#### Dependecies used:
- glob
- csv
- os
- termcolor
- tqdm

#### Overview:
The script will extract all emails from csv and text files and split them based on the country **(domain extension: .uk, .fr... etc)**

**What kind of text files can be used?**
You can use text files with emails only or you can use emails from combolist.

Basically, the combolist can be as format:
**(email@domain.com;password) or (email@domain.com:password)**

**What kind of CSV files can be used?**
Please note that only CSV files extracted from Powermta logs are working fine.
I will make a new version to work with all CSV files in the future.

**What can we expect when the extraction is done?**
Once the extraction is complete, you will get as result fetched email list splited by country extension **(.de, .co.uk...)** and email service provider **(Gmail, Hotmail, Gmx.. etc).**

These are the email service providers supported:
- Gmail
- Outlook
- Yahoo
- Web
- T-online
- Aol
- Arcor
- Online
- Orange
- Tiscali
- Alice
- Home
- Planet
- iCloud

All other ESPs that aren't included in the previous list will be added to text file called **(others.txt)**

**How can I add more ESP to the list?**
Just add domain to the array:

`ispTOP = ["gmail","hotmail","outlook","msn","live","yahoo","gmx","web","t-online","aol","arcor","online","orange","tiscali","alice","home","planet","icloud"]
`

**How can I add more country extension?**

You can add them to the array as well:

`countryTOP = ["com","co.uk","de","nl","se","no","dk","fi","fr","it","at","com.au","co.nz"]`

Finally you can run the script by adding emails list to **data** folder and insert the cmd: **py email-extractor.py**
**And make sure that: data and fetched_data folders are available.**