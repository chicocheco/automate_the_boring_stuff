#! python3
# email_utorrent.py - Remotely command to download torrents in uTorrent via email.
# Set up uTorrent to start downloading a '.torrent' file right away, without asking for more.

import email
import getpass
import imaplib
import os
import smtplib
import subprocess
import time
from email.mime.text import MIMEText


def email_torrent(user_name, password):
    # Log in to email account.
    imap_session = imaplib.IMAP4_SSL('imap.gmail.com')
    result, account_details = imap_session.login('chicocheco99', 'tanicka21')

    if result != 'OK':
        print('Not able to sign in!')
        raise NameError('Not able to sign in!')
    else:
        print('Login status: ' + result)

    # Search for emails with "torrent" in their subject field.
    imap_session.select('INBOX', readonly=False)
    result, email_data = imap_session.search(None, '(SUBJECT torrent)')

    # Get a list of their UIDs.
    email_uids = email_data[0].split()

    if len(email_uids) != int(0):
        print(f'Found {len(email_uids)} emails with subject "torrent":')
    else:
        print('No emails with subject "torrent" were found.')

    torr_files = []
    # Fetch each UID's entire raw message.
    for email_uid in email_uids:
        result, email_data = imap_session.fetch(email_uid, '(RFC822)')

        # Walk all parts of the raw message.
        email_body = email.message_from_bytes(email_data[0][1])
        for part in email_body.walk():
            if part.get('Date'):
                date = (email.utils.parsedate_to_datetime(part.get('Date'))).strftime('%A, %d.%m.%Y, %H:%M')
            if part.get('Sender'):
                sender = part.get('Sender')
            text_included = part.get_content_type() == 'text/plain'
            if text_included:
                uid_decoded = email_uid.decode('ascii')
                print(f'Message with UID {uid_decoded} from {sender}, received on {date}:'
                      f'\n\t{part.get_payload(decode=False)}')

            file_name = part.get_filename()
            if file_name:
                payload = part.get_payload(decode=True)  # Decode to get bytes-like object (False returns a string)
                print('\tRetrieving... ' + file_name)
                with open(file_name, 'wb') as fp:
                    fp.write(payload)
                print('\tOpening in uTorrent... ')
                new_file_name = os.path.abspath(file_name)
                torr_files.append(file_name)
                utorrent = subprocess.Popen(['C:\\Program Files (x86)\\uTorrent\\uTorrent.exe', new_file_name])
                if utorrent.poll() is None:
                    print('\tDownloading...')
        imap_session.store(email_uid, '+FLAGS', '\\Deleted')  # Deletes the mail completely on Gmail.
        uid_decoded = email_uid.decode('ascii')
        print(f'Email with UID {uid_decoded} was deleted.\n\n')

    imap_session.close()
    imap_session.logout()

    if torr_files:
        print('Sending cofirmation email back to the sender...')
        tf_string = '\n\t'.join(torr_files)
        smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_session.ehlo()
        smtp_session.starttls()
        smtp_session.login(user_name, password)
        usr_gmail = user_name + '@gmail.com'
        msg = MIMEText(f'Hi!\n\n'
                       f'The following file(s) have been accepted and processed to download:\n\t{tf_string}\n\n'
                       f'Have a nice day,\nyour Python Robot')
        msg['To'] = email.utils.formataddr(('', sender))
        msg['From'] = email.utils.formataddr(('Python Robot', usr_gmail))
        msg['Subject'] = 'Torrent file(s) accepted and processed to donwload'
        smtp_session.sendmail(usr_gmail, [sender], msg.as_string())
        smtp_session.quit()
        print('Done.\n')

    # Wait 15 minutes and repeat.
    for minute in range(-15, -2):
        print(f'Re-checking the mailbox in {abs(minute)} minutes.')
        time.sleep(60)
    else:
        print(f'Re-checking the mailbox in 1 minute.\n')
        time.sleep(60)

    print('Re-checking the mailbox nox...\n')
    email_torrent(user_name, password)


if __name__ == '__main__':
    user_name = input('Enter your GMail username: ')
    # password = input('Enter your password: ')
    password = getpass.getpass('Enter your password: ')
    email_torrent(user_name, password)
