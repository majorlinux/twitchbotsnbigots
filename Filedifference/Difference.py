with open("new_list.txt", "r", encoding="UTF-8") as new_file, open("old_list.txt", "r", encoding="UTF-8") as old_file:
    new_set = set([name.strip().lower() for name in new_file.readlines()])
    old_set = set([name.strip().lower() for name in old_file.readlines()])

added = new_set.difference(old_set)
removed = old_set.difference(new_set)

with open("!added_names.txt", "w", encoding="UTF-8") as added_file, open("!removed_names.txt", "w", encoding="UTF-8") as removed_file:
    added_file.writelines([f"{name}\n" for name in sorted(added)])
    removed_file.writelines([f"{name}\n" for name in sorted(removed)])