# json, csv
import json
import csv

# infa > 100 po alfavitu v result.csv
# name, русский, матан, инфа

# json.dump(obj, ensure_ascii=True, indent=None) -> file | json.dumps(obj) -> str - zapis

# json.load(filename) | json.loads(string) - read
with open("file.json", encoding='utf-8') as f:
    data = json.load(f)
    print(data)

# writing csv
# with open('files/ikea.csv', encoding="utf8") as csvfile:
#     reader = csv.reader(csvfile, delimiter=';', quotechar='"')
#     for index, row in enumerate(reader):
#         if index > 10:
#             break
#         print(row)
#
# with open('files/ikea.csv', encoding="utf8") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
#     expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)
#
# for record in expensive[:10]:
#     print(record)

# reading csv
with open("result.csv", "w", encoding="utf-8", newline="") as f:
    data.sort(key=lambda x: x["name"], reverse=True)

    writer = csv.writer(f, delimiter=",")
    writer.writerow(["name", "русский", "матан", "инфа"])
    for d in data:
        # writer.writerow([d["name"], d["русский"], d["матан"], d["инфа"]])
        writer.writerow(d)

    # wrtr = csv.DictWriter(
    #     f, fieldnames=list(data[0].keys()),
    #     delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    # wrtr.writeheader()
    # for d in data:
    #     wrtr.writerow(d)
