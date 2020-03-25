import re

pattern_tag_name = r"(?<=<)([A-Za-z0-9]*)(?=[> ])"
pattern_ignore_comment = r"(?<=<!--)(.*)(?=-->)"
pattern_opened_comment = r"\s*<!--.*"
pattern_closed_comment = r"(?<=\w|\s)(-->)"
pattern_attribute_name = r"(?<= )([a-z-]*)(?==)"
pattern_attribute_value = r"(?<=\")([A-Za-z0-9-_. /;:\\|]*)(?=\")"

tags = re.compile(pattern_tag_name)
comments = re.compile(pattern_ignore_comment)
opened_comm = re.compile(pattern_opened_comment)
closed_comm = re.compile(pattern_closed_comment)
attributes = re.compile(pattern_attribute_name)
attr_values = re.compile(pattern_attribute_value)

comment_opened = False

for i in range(int(input())):
    text = input()
    #print(text)

    # check if comment
    result = comments.search(text)
    if result:
        continue

    result = opened_comm.search(text)
    if result:
        comment_opened = True
        continue

    result = closed_comm.search(text)
    if result:
        comment_opened = False
        continue

    if comment_opened:
        continue
    
    # check tag name
    result = tags.findall(text)
    for r in result:
        print(r)

        # check attributes and values of them
        attr = attributes.findall(text)
        attr_v = attr_values.findall(text)

        if attr and attr_v:
            tuples = list(zip(attr, attr_v))
            for tp in tuples:
                print('->', tp[0], '>', tp[1])
    else:
        # check attributes and values of them
        attr = attributes.findall(text)
        attr_v = attr_values.findall(text)

        if attr and attr_v:
            tuples = list(zip(attr, attr_v))
            for tp in tuples:
                print('->', tp[0], '>', tp[1])
    
