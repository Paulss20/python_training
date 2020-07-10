# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + " "*10
     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
     Group(name=name, header=header, footer=footer)
     for name in ["", random_string("name", 10)]
     for header in ["", random_string("header", 15)]
     for footer in ["", random_string("footer", 15)]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
     pass
     #old_groups = app.group.get_group_list()
     #app.group.create(group)
     #assert len(old_groups) + 1 == app.group.count() # you need to specify not the length but just the value that the count method returns
     #new_groups = app.group.get_group_list()
     #old_groups.append(group)
     #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




