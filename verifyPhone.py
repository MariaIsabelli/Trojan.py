import phonenumbers

from phonenumbers import geocoder 

phone = input('Digite o telefone no formato : +551140028922: ')

phone_number = phonenumbers.parse(phone)

print(goecode.description_for_number(phone_number, 'pt'))

