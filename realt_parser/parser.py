from selenium import webdriver
from apartment import Apartment
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def generate_url(sale_or_rent, num_of_rooms):
    dict_of_room = {1: '1k', 2: '2k', 3: '3k', 4: '4k', 5: '5k', 6: '6k'}
    for key, value in dict_of_room.items():
        if num_of_rooms == key:
            if sale_or_rent == 'sale':
                return f'https://realt.by/sale/flats/{value}/'
            elif sale_or_rent == 'rent':
                return f'https://realt.by/rent/flat-for-long/{value}/'


def get_apartment(sale_or_rent, num_of_rooms):
    drive = webdriver.Chrome()
    drive.get(generate_url(sale_or_rent, num_of_rooms))
    # btn_actual = drive.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[2]/div['
    #                                           '2]/div/div/div[1]/div')
    # drive.execute_script('arguments[0].click();', btn_actual)
    # btn_cheap = drive.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[2]/div['
    #                                          '2]/div/div/div[1]/div')
    # drive.execute_script('arguments[0].click();', btn_cheap)
    html_source = drive.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    ads = soup.find_all('div', class_='sm:w-full w-full p-1.5 sm:p-2.5')
    apartments = []
    for i in ads:
        square = i.find('p', class_='flex flex-wrap text-headline items-center font-semibold md:font-bold -mr-2 '
                                    'mb-2.5 md:mb-4 -order-2 md:-order-none').find_all('span')[1].text

        num_of_storeys = i.find('p', class_='flex flex-wrap text-headline items-center font-semibold md:font-bold -mr-2 '
                           'mb-2.5 md:mb-4 -order-2 md:-order-none').find_all('span')[2].text
        price = i.find('span', class_='text-basic text-subhead').text
        update_date = i.find('span', class_='mr-1.5').text
        realtor = i.find('div', class_='text-caption text-basic flex justify-between').find_all('div')[1].text
        adress_ap = i.find('p', class_='text-basic w-full text-subhead md:text-body').text
        apartment = Apartment(square, num_of_storeys, price, update_date, realtor, adress_ap)
        apartments.append(apartment)

    for i in apartments:
        print(i.info())

    return apartments


print(get_apartment('sale', 2))
