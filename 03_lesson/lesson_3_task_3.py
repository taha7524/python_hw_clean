from Address import Address
from Mailing import Mailing


to_address = Address('156000', 'Кострома', 'Шаговая', '14', '5')
from_address = Address('433513', 'Димитровград', 'Димитрова', '6', '23')
track = 'RA-RZ123456789RU'
cost = 147

my_mailing = Mailing(to_address, from_address, 147, 'RA-RZ123456789RU')

print(my_mailing)
