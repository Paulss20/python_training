
from model.add_new import AddNew
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [AddNew(my_f_name="", my_l_name="", work_address="", my_h_telefon="", my_mobile="", my_work_telefon="",
                    my_company_mail="", my_second_mail="", my_third_mail="", my_home_address="", my_secondary_phone="")] + [
    AddNew(my_f_name=random_string("firstname", 10), my_l_name=random_string("lastname", 10),
            work_address=random_string("address", 10),
            my_h_telefon=random_string("home_phone", 10), my_mobile=random_string("mobile_phone", 10),
            my_work_telefon=random_string("work_phone", 10),
            my_company_mail=random_string("email", 10), my_second_mail=random_string("email2", 10),
            my_third_mail=random_string("email3", 10),
            my_home_address=random_string("address2", 10), my_secondary_phone=random_string("phone2", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
     jsonpickle.set_encoder_options("json", indent=2)
     out.write(jsonpickle.encode(testdata))
