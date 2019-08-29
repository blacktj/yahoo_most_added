#fantasy baseball free agent daily email

from datetime import datetime, date, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from functions import remove_non_ascii, list_to_name


def get_players_and_send_email():
    #get yesterday's date
    yesterday = date.today() - timedelta(1)

    url = 'https://baseball.fantasysports.yahoo.com/b1/buzzindex?date=' + str(yesterday) + '&pos=ALL&src=combined&bimtab=A&sort=BI_A&sdir=1'
    #get the page content and convert to beautifulsoup
    page_content= requests.get(url).text
    soup = BeautifulSoup(''.join(page_content), "lxml")

    #create empty list
    most_added = []
    #scrape all tables on the page
    for tables in soup.find_all('tbody'):
    #scrape all rows from the table individually
        for row in tables.find_all('tr'):
    #strip the html down to what we need
            detail = (row.get_text(strip=True, separator='|').split('|'))
            if detail[0] == 'New Player Note' or detail[0] == 'Player Note' or detail[0] == 'No new player Notes' and len(detail) > 3:
                temp = [list_to_name(remove_non_ascii(detail[1])),detail[2],detail[-4],detail[-3],detail[-2],detail[-1]]
                most_added.append(temp)
            else:
                next

    colnames = ['player_name', 'team_pos', 'drops', 'adds', 'trades', 'total_moves']
    df_most_added = pd.DataFrame(most_added, columns = colnames)

    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    to = ''
    subject = 'Most Added Players'
    email = "{df}"
    text = email.format(df=df_most_added.to_html())

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['To'] = to
    part1 = MIMEText(text, 'html')
    msg.attach(part1)

    # Send the message via local SMTP server.
    s = smtplib.SMTP("smtp.gmail.com:587")
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.sendmail(sent_from, to, msg.as_string())
    s.quit()

if __name__ == '__main__':
    get_players_and_send_email()
