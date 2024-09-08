import csv
import json
outputfilename = 'sample_output.csv'
with open(outputfilename, 'a', newline='', encoding='utf-8') as csvFile:
    fields = ['Cheapest Lowest Shown Price','Room Type of Cheapest Lowest Shown Price','No. of Guest','Room_Type','Total Price (Net + Taxes)']
    writer1 = csv.DictWriter(csvFile,fieldnames=fields)
    writer1.writeheader()

file_path = 'Python-task.json'
with open(file_path, 'r') as file:
    data = json.load(file)
def SampleJson():
    print('Script Execution Started')
    prices_lst = list()
    shown_prices = data['assignment_results'][0]['shown_price']
    for valuess in shown_prices.values():
        price = float(valuess)
        prices_lst.append(price)
    cheapest_price = prices_lst[0]

    for number in prices_lst[1:]:
        if number < cheapest_price:
            cheapest_price = number
    print("The lowest shown price is:", cheapest_price)
    room_type_of_cp = [key for key, value in shown_prices.items() if value == str(int(cheapest_price))]
    room_type_of_cp = room_type_of_cp[0]
    number_of_guest = data['assignment_results'][0]['number_of_guests']
    dict1 = data['assignment_results'][0]['net_price']
    total_tax = data['assignment_results'][0]['ext_data']['taxes']
    tax_data = json.loads(total_tax)
    tax = tax_data["TAX"]
    city_tax = tax_data["City tax"]
    total_tax = float(tax)+float(city_tax)
    for key in dict1:
        total_cost = float(dict1[key]) + total_tax
        print('Total Cost for Room Type ', key ,' is ',total_tax)

        with open(outputfilename, 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow(
                [cheapest_price,room_type_of_cp,number_of_guest,key,total_cost
                ]
            )
    print('Output file is Creating with File name :- ',outputfilename)

sample_json = SampleJson()

