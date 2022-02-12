import re
import shutil

email_pattern = '(?P<email>[\w]+@[\w-]+[.][\w]{3,5})'
phone_pattern = '((?![.+])[((\d+)?[\d.]+[-.][x\d-]+)' 

phone_regex = re.compile(phone_pattern, flags= re.I | re.M)
email_regex = re.compile(email_pattern, flags= re.I | re.M)

with open('./assets/potential-contacts.txt', 'r') as file:
  text = file.read()

phone_numbers = set(phone_regex.findall(text))
emails = set(email_regex.findall(text))

emails_sorted = sorted(list(emails))
phone_numbers_sorted = sorted(list(phone_numbers))


with open ('phone_numbers.txt', 'w+') as f:
  for line in phone_numbers_sorted:
    f.write(f'{line}\n')

shutil.copy('phone_numbers.txt', 'assets')


with open ('emails.txt', 'w+') as f:
  for line in emails_sorted:
    f.write(f'{line}\n')

shutil.copy('emails.txt', 'assets')
