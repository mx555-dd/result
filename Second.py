import re

def reg_search(text, regex_list):
    results = []
    for regex_dict in regex_list:
        result_dict = {}
        for key, pattern in regex_dict.items():
            # 处理单个正则表达式
            match = re.search(pattern, text)
            if match:
                if key == '换股期限':
                    # 对于换股期限，我们期望匹配两个日期，并用逗号分隔
                    groups = match.groups()
                    if groups:
                        result_dict[key] = [groups[0].strip(), groups[1].strip()]
                else:
                    result_dict[key] = match.group().strip()
        results.append(result_dict)
    return results

# 示例文本
text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023-06-02 至 2027-06-01 止。
'''

# 示例正则表达式列表
regex_list = [
    {
        '标的证券': r'股票代码：(\d{6}\.SH)',
        '换股期限': r'(\d{4}-\d{1,2}-\d{1,2})[^0-9]*(\d{4}-\d{1,2}-\d{1,2})'
    }
]

# 调用函数
result = reg_search(text, regex_list)
print(result)