from smartphone import Smartphone

catalog = [
         Smartphone('Honor', 'Magic8 Pro', '+79273456789'),
         Smartphone('Huawei', 'Huawei nova Flip S', '+79271234567'),
         Smartphone('Xiaomi', 'iaomi 17 Pro Max', '+79279876543'),
         Smartphone('Samsung', 'Samsung Galaxy S25+', '+79026543782'),
         Smartphone('Nokia', 'Nokia C210', '+79021234567')
]

for smartphone in catalog:
    print(f'{smartphone.Brand} - {smartphone.Model}. {smartphone.Number}')
