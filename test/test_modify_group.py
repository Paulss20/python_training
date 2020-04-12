from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Next Group"))
    else:
        app.group.modify_first_group(Group(name=""))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="New Header"))
    else:
        app.group.modify_first_group(Group(header="Next header"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="New Header"))
    else:
        app.group.modify_first_group(Group(footer="Next footer"))
