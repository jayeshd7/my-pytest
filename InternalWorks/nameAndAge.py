

def name_and_age(name, age):
    print(f"I am {name} and I am {age} years old!")

name_and_age("jayesh", 33)


def in_both(wd1, wd2):
    common = []
    for c in wd1:
        if c in wd2:
            common.append(c)
    print(sorted(common))
    return sorted(common)

in_both("peer","apple")