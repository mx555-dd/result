import pandas as pd

# 完整的数据列表，模拟从API获取的数据
data = {
    "resultList": [
        {
            "bondDefinedCode": "jidha39983",
            "bondName": None,
            "bondCode": "239983",
            "issueStartDate": "2023-12-22",
            "issueEndDate": "2023-12-22",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND10007C4N2",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jhhaj39982",
            "bondName": None,
            "bondCode": "239982",
            "issueStartDate": "2023-12-22",
            "issueEndDate": "2023-12-22",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND10007C3L8",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jhhai30028",
            "bondName": None,
            "bondCode": "230028",
            "issueStartDate": "2023-12-22",
            "issueEndDate": "2023-12-22",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND10007C3M6",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jhfcj39981",
            "bondName": None,
            "bondCode": "239981",
            "issueStartDate": "2023-12-15",
            "issueEndDate": "2023-12-15",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND10007C3B9",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jhcji39980",
            "bondName": None,
            "bondCode": "239980",
            "issueStartDate": "2023-12-14",
            "issueEndDate": "2023-12-14",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND10007C2Y3",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jgebe30027",
            "bondName": None,
            "bondCode": "230027",
            "issueStartDate": "2023-12-14",
            "issueEndDate": "2023-12-14",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000776R0",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jgebf39979",
            "bondName": None,
            "bondCode": "239979",
            "issueStartDate": "2023-12-08",
            "issueEndDate": "2023-12-08",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000776S8",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jfjcj39978",
            "bondName": None,
            "bondCode": "239978",
            "issueStartDate": "2023-12-06",
            "issueEndDate": "2023-12-06",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000775V4",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jfeej39977",
            "bondName": None,
            "bondCode": "239977",
            "issueStartDate": "2023-12-01",
            "issueEndDate": "2023-12-01",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000774F0",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jejgj39976",
            "bondName": None,
            "bondCode": "239976",
            "issueStartDate": "2023-12-01",
            "issueEndDate": "2023-12-01",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000764D6",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jegji39975",
            "bondName": None,
            "bondCode": "239975",
            "issueStartDate": "2023-11-24",
            "issueEndDate": "2023-11-24",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND100076488",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jebce30026",
            "bondName": None,
            "bondCode": "230026",
            "issueStartDate": "2023-11-24",
            "issueEndDate": "2023-11-24",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND100076348",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jdifg39974",
            "bondName": None,
            "bondCode": "239974",
            "issueStartDate": "2023-11-17",
            "issueEndDate": "2023-11-17",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND1000762Z3",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jdahh39973",
            "bondName": None,
            "bondCode": "239973",
            "issueStartDate": "2023-11-17",
            "issueEndDate": "2023-11-17",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND100076280",
            "inptTp": "0"
        },
        {
            "bondDefinedCode": "jceeb30025",
            "bondName": None,
            "bondCode": "230025",
            "issueStartDate": "2023-11-14",
            "issueEndDate": "2023-11-14",
            "bondTypeCode": "100001",
            "bondType": "Treasury Bond",
            "entyFullName": "Ministry of Finance of the People’s Republic of China",
            "entyDefinedCode": "300001",
            "debtRtng": "---",
            "isin": "CND100074JJ4",
            "inptTp": "0"
        }
        # Add more items from your data here
    ]
}

# 提取需要的字段并存储到列表中
columns = ["isin", "bondCode", "entyFullName", "bondType", "issueStartDate", "debtRtng"]
data_list = []
for item in data["resultList"]:
    data_list.append([item.get(col, "") for col in columns])

# 转换为DataFrame
df = pd.DataFrame(data_list, columns=columns)

# 保存DataFrame为CSV文件
df.to_csv("treasury_bonds_2023_from_api.csv", index=False)

print("数据已保存为 treasury_bonds_2023_from_api.csv 文件。")
