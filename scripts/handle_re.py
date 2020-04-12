import re

from scripts.handle_mysql import HandleMysql
# 正则表达式相当于一个模子，可以拿这个模子去把符合这个模子的内容全部找出来


# 1.创建待替换的字符串
str='{"mobile_phone":"{not_existed_mobile}","pwd":"12345678","type":1,"reg_name":"sunny"}'
# 2.创建正则表达式
# 正则表达式中一定要r，如果有些字符有特殊含义，需要在前面加\
# one_re=r"\${not_existed_mobile}"

# match方法
# match方法第一个参数为正则表达式，第二个参数为待查询的字符串
# match方法只能从头开始匹配
# 如果匹配不上会返回None
# 如果匹配上，返回match对象
# 可以使用match.group()获取匹配的值
# match=re.match(r"\${not_existed_mobile}",str)
# match_1=re.match(r'{"mobile_phone":"{not_existed_mobile}"',str)
# match_1.group()

# search
# search方法第一个参数为正则表达式，第二个参数为待查询的字符串
# search方法不用从头开始匹配，只要能匹配得上，直接返回
# 如果匹配得上返回match对象，匹配不上返回None
# 可以使用match.search()获取匹配的值
# match=re.search(r'{not_existed_mobile}',str)

# sub
# sub方法第一个参数为正则表达式字符串，第二个参数为新的值（字符串），第三个参数为待替换的字符串（原始字符串）
# 如果能匹配得上，返回替换后的值（一定是字符串）
# 如果匹配不上，返回的是原始字符串
match = re.sub(r'{not_existed_mobile}', '18716402362', str)

# 在项目中一般将search和sub结合起来用
if re.search(r'{not_existed_mobile}', str):
    res = re.sub(r'{not_existed_mobile}', '18716402362', str)

# split
# 找到匹配的内容后，再进行分割

# findall
# 把所有满足条件的内容找出来，返回一个列表

# finditer
# 将所有满足条件的内容构建成一个生成器，再返回一个生成器

do_mysql = HandleMysql()

mobile_phone=do_mysql.creat_no_existed_mobile()

do_mysql.close()