from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Next Group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="New Header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Next header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="New Header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="Next footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

