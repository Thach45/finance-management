from datetime import datetime

data = [
    {"name": "Alice", "age": '10/3/2024'},
    {"name": "Bob", "age": '20/3/2024'},
    {"name": "Charlie", "age": '30/11/2024'}
]

# Sắp xếp giảm dần dựa trên ngày tháng
sorted_data_desc = sorted(
    data, 
    key=lambda x: datetime.strptime(x["age"], "%d/%m/%Y"), 
    reverse=True
)

print(sorted_data_desc)