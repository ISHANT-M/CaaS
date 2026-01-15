import re


def check(row_num: int, hashed_cg: str):
    new_num = row_num
    new_hash = hashed_cg

    with open("data.txt", "r") as fp:
        line = fp.readline()
    extract_re = re.compile(r"(\d+):(.*)")
    matches = extract_re.match(line)

    old_num = -1
    old_hash = ""
    if matches:
        try:
            old_num = int(matches.group(1).strip())
        except Exception:
            old_num = -1

        old_hash = matches.group(2)

    if new_num in [-1, 0]:
        return False
    elif new_num > old_num or (new_num == old_num and new_hash != old_hash):
        update(f"{new_num}:{new_hash}")
        return True

    return False


def update(val: str):
    with open("data.txt", "w") as fp:
        fp.write(val)
