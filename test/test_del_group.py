from model.group import Group
import random
import re


def test_delete_some_group(app, db, check_ui):
     if len(db.get_group_list()) == 0:
          app.group.create(Group(name="test"))
     old_groups = db.get_group_list()
     group = random.choice(old_groups)
     app.group.delete_group_by_id(group.id)
     new_groups = db.get_group_list()
     assert len(old_groups) - 1 == len(new_groups)
     old_groups.remove(group)
     assert old_groups == new_groups
     if check_ui:    # for a disabled check, where we compare the database information with the UI,
                     # we need to transform the list taken from the database (we take only id and name)
          new_groups_ui = []
          for i in new_groups:
               new_groups_ui.append(Group(id=i.id, name=re.sub("  ", " ", i.name.strip())))
          assert sorted(new_groups_ui, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


