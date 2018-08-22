# Converted to Python3
# Download ALL attachments from GMail
# 1. Script needs to be run via console not in an IDE, getpass.getpass() will fail otherwise.
#    https://docs.python.org/3/library/getpass.html
# 2. Make sure you have IMAP enabled in your GMail settings.
#    https://support.google.com/mail/troubleshooter/1668960?hl=en
# 3. If you are using 2 step verification you may need an APP Password.
#    https://support.google.com/accounts/answer/185833
# 4. Reference information for GMail IMAP extension can be found here.
#    https://developers.google.com/gmail/imap_extensions


import email
import hashlib
import getpass
import imaplib
import os
from collections import defaultdict, Counter
import platform

fileNameCounter = Counter()
fileNameHashes = defaultdict(set)
NewMsgIDs = set()
ProcessedMsgIDs = set()


def recover(resume_file):
    if os.path.exists(resume_file):
        print('Recovery file found resuming...')
        with open(resume_file) as f:
            processed_ids = f.read()
            for ProcessedId in processed_ids.split(','):
                ProcessedMsgIDs.add(ProcessedId)
    else:
        print('No Recovery file found.')
        open(resume_file, 'a').close()


def generate_mail_messages(gmail_user_name, p_word, resume_file):
    imap_session = imaplib.IMAP4_SSL('imap.gmail.com')

    typ, account_details = imap_session.login(gmail_user_name, p_word)

    print(typ)
    print(account_details)
    if typ != 'OK':
        print('Not able to sign in!')
        raise NameError('Not able to sign in!')
    imap_session.select('"[Gmail]/All Mail"')
    typ, data = imap_session.search(None, '(X-GM-RAW "has:attachment")')
    # typ, email_data = imapSession.search(None, 'ALL')
    if typ != 'OK':
        print('Error searching Inbox.')
        raise NameError('Error searching Inbox.')

    # Iterating over all emails
    for msgId in data[0].split():
        NewMsgIDs.add(msgId)
        typ, message_parts = imap_session.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print('Error fetching mail.')
            raise NameError('Error fetching mail.')
        email_body = message_parts[0][1]
        if msgId not in ProcessedMsgIDs:
            yield email.message_from_bytes(email_body)
            ProcessedMsgIDs.add(msgId)
            with open(resume_file, "a") as resume:
                resume.write(f'{msgId},')

    imap_session.close()
    imap_session.logout()


def save_attachments(message, directory):
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            # print(part.as_string())
            continue
        if part.get('Content-Disposition') is None:
            # print(part.as_string())
            continue
        file_name = part.get_filename()
        if file_name is not None:
            file_name = ''.join(file_name.splitlines())
        if file_name:
            # print('Processing: {file}'.format(file=fileName))
            payload = part.get_payload(decode=True)
            if payload:
                x_hash = hashlib.md5(payload).hexdigest()

                if x_hash in fileNameHashes[file_name]:
                    print(f'\tSkipping duplicate file: {file_name}')
                    continue
                fileNameCounter[file_name] += 1
                file_str, file_extension = os.path.splitext(file_name)
                if fileNameCounter[file_name] > 1:
                    new_file_name = f'{file_str}({fileNameCounter[file_name]}){file_extension}'
                    print(f'\tRenaming and storing: {file_name} to {new_file_name}')
                else:
                    new_file_name = file_name
                    print(f'\tStoring: {file_name}')
                fileNameHashes[file_name].add(x_hash)
                file_path = os.path.join(directory, new_file_name)
                if os.path.exists(file_path):
                    print(f'\tExists in destination: {new_file_name}')
                    continue
                try:
                    with open(file_path, 'wb') as fp:
                        fp.write(payload)
                except EnvironmentError:
                    print(f'Could not store: {file_path} it has a shitty file name or path under {platform.system()}.')
            else:
                print(f'Attachment {file_name} was returned as type: {type(payload)} skipping...')
                continue


if __name__ == '__main__':
    resumeFile = os.path.join('resume.txt')
    user_name = input('Enter your GMail username: ')
    password = getpass.getpass('Enter your password: ')
    recover(resumeFile)
    if 'attachments' not in os.listdir(os.getcwd()):
        os.mkdir('attachments')
    for msg in generate_mail_messages(user_name, password, resumeFile):
        save_attachments(msg, 'attachments')
os.remove(resumeFile)