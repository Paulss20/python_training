from model.group import Group
import random
import re


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Next Group"))

    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    id = group_old.id
    group_new = Group(id=id, name="Second Group", header="Groups Header", footer="Groups Footer")
    app.group.modify_group_by_id(id, group_new)
    new_groups = db.get_group_list()
    # ищем в старом списке группу с рабочим id, которую надо обновить, и обновляем
    for i in range(len(old_groups)):
        if old_groups[i].id == id:
            old_groups[i] = group_new
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# для отключаемой проверки, где сраниваем БД инфу с UI, надо преобразовать список, взятый из БД, - взять только id и name
    if check_ui:
        new_groups_ui = []
        for i in new_groups:
            new_groups_ui.append(Group(id=i.id, name=re.sub("  ", " ", i.name.strip())))
        assert sorted(new_groups_ui, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)

