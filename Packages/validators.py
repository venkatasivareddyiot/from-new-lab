import re
def emailValidator(email):
    pattern='[0-9a-z][0-9a-z_.]{4,20}[0-9a-z][@][0-9a-z]{4,13}[.][a-z]{2,5}'
    if re.match(pattern,str(email)):
        #print(email,"","is valid")
        return True
    else:
        #print(email,"","inValid")
        return False

import re 
def phoneNoValidator(phone):
    pattern='^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,str(phone)):
        return True
    else:
        return False