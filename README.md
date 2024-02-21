# Email Outreach Script
1. Download VSCode and Python if you do not have them already.
   - VSCode: https://code.visualstudio.com/download
   - Python: https://www.python.org/downloads/
2. Once you have VSCode downloaded, git clone this repository onto your device.
3. Now that you have all the files, you can make changes to the email_template.txt file if necessary.
4. Upload a csv, with 3 columns that are labeled, "organization", "email", and "mission". (you can change these titles, but you would also have to change the code).
5. If you uploaded your own csv, on line 54 of main.py (with open('email_data.csv', 'r') as csv_file:), change 'email_data.csv' to the name of your csv file.
6. To run the script, go into the terminal and type: "python main.py"
  - this will send out emails to every email on the csv
  - it will attach the Sift PDF 1 pager, and also CC David and Tony automatically

# Components:
1. main.py - python script that logs into the Sift account and automates email sending process
2. email_template.txt - email template that is subject to change
