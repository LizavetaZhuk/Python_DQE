from datetime import datetime
import random
import os
import sys
from normalization import normalize_func
import csv
import re
import json
import xml.etree.ElementTree as ET
import sqlite3

file_name = 'newsfeed.txt'  # in order to change file name in one place


class News:
    def __init__(self, news_text, city):
        self.news_text = news_text
        self.city = city

    def date_and_time(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M")

    def add_publ_news(self):
        f = open(file_name, 'a')
        f.write('News -------------------------')
        f.write(f'\n{self.news_text}')
        f.write(f'\n{self.city}, {self.date_and_time()}')
        f.write('\n------------------------------')
        f.write('\n')
        f.write('\n')


class PrivateAd:
    def __init__(self, ad_text, expiration_date):
        self.ad_text = ad_text
        self.expiration_date = expiration_date

    def day_left(self):
        now = datetime.now()
        self.now = now.strftime("%d/%m/%Y")
        date_format = "%d/%m/%Y"
        delta = datetime.strptime(self.expiration_date, date_format) - datetime.strptime(self.now, date_format)
        return delta.days

    def add_publ_ad(self):
        f = open(file_name, 'a')
        f.write('Private Ad ------------------')
        f.write(f'\n{self.ad_text}')
        f.write(f'\nActual until: {self.expiration_date}, {self.day_left()} days left')
        f.write('\n------------------------------')
        f.write('\n')
        f.write('\n')


class BookAdvise:
    def __init__(self, book_name, rate):
        self.book_name = book_name
        self.rate = rate

    def random_rate(self):
        book_rate = random.randint(1, 5)
        final_rate = (int(self.rate) + book_rate)//2
        return final_rate

    def add_publ_book(self):
        f = open(file_name, 'a')
        f.write('Book Advise ------------------')
        f.write(f'\n{self.book_name}')
        f.write(f'\nGoodreads.com rating: {self.random_rate()}/5')
        f.write('\n------------------------------')
        f.write('\n')
        f.write('\n')


class Publication(News, PrivateAd, BookAdvise):
    def __init__(self, i):
        self.i = i
        self.file_path = sys.path[1]

    def publish_write(self):
        if self.i.lower() == 'news':
            publ = News(news_text=input('Please write the text of the news: '), city=input('Please write city: '))
            publ.add_publ_news()
        elif self.i.lower() == 'ad':
            publ = PrivateAd(ad_text=input('Please write the text of the advertising: '), expiration_date=input('Please write the expiration date in d/m/y format: '))
            publ.add_publ_ad()
        elif self.i.lower() == 'book':
            publ = BookAdvise(book_name=input('Please write the name of the book "author - name of the book": '), rate=input('Please write your rate from 1 to 5: '))
            publ.add_publ_book()
        else:
            print('Choose another option')

    def file_path_func(self):
        if self.i.lower() == 'mine':
            input_path = input(r'Enter your file path: ')
        elif self.i.lower() == 'default':
            filename = input(r'Enter your file name: ')
            input_path = self.file_path + '/' + filename
        else:
            print('Choose another option')
        return input_path

    def publish_file(self):
        file_path = self.file_path_func()
        try:
            with open(file_path, "r") as file1:
                with open(file_name, "a") as file2:
                    new_text = normalize_func(file1.read())
                    file2.write(new_text)
                    file2.write('\n')
                    file2.write('\n')
            os.remove(file_path)
        except FileNotFoundError:
            print('There is no such file in the folder!')

    def word_count(self):
        with open(self.file_path + '/' + file_name, 'r') as newsfeed:
                readfile = newsfeed.read()
                unique_words = {}
                words = re.findall('[a-z]+', readfile, flags=re.IGNORECASE)
                lower_words = [word.lower() for word in words]
                for i in lower_words:
                    if i in unique_words:
                        unique_words[i] = unique_words[i] + 1
                    else:
                        unique_words[i] = 1
                return unique_words

    def word_write(self):
        unique_words = self.word_count()
        with open(self.file_path + '/' + 'word_count.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for key, value in unique_words.items():
                writer.writerow([key, value])

    def letter_count(self):
        with open(self.file_path + '/' + file_name, 'r') as newsfeed:
                readfile = newsfeed.read()
                unique_letters = {}  # {key = letter : value = [count lowercase, count uppercase]}
                all_letters = 0  # count all letters in the text
                for i in readfile.lower():
                    if i.isalpha():
                        all_letters += 1
                        if i in unique_letters:
                            unique_letters[i][0] = unique_letters[i][0] + 1  # count lowercase
                        else:
                            unique_letters[i] = [1, 0]
                for i in readfile:
                    if i.isupper():
                        i = i.lower()
                        unique_letters[i][1] = unique_letters[i][1] + 1  # count uppercase
                return unique_letters, all_letters

    def letter_write(self):
        unique_letters = self.letter_count()[0]
        all_letters = self.letter_count()[1]
        with open(self.file_path + '/' + 'letter_count.csv', 'w', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for key, value in unique_letters.items():
                writer.writerow({'letter': key, 'count_all': value[0], 'count_uppercase': value[1], 'percentage': (value[0]*100//all_letters)})

    def publish_json(self):
        file_path = self.file_path_func()
        try:
            json_file = json.load(open(file_path))
            for i in range(len(json_file)):
                dict = json_file[i]
                if dict['type'].lower() == 'news':
                    publ = News(news_text=dict['text'], city=dict['city'])
                    publ.add_publ_news()
                elif dict['type'].lower() == 'ad':
                    publ = PrivateAd(ad_text=dict['text'], expiration_date=dict['expiration_date'])
                    publ.add_publ_ad()
                elif dict['type'].lower() == 'book':
                    publ = BookAdvise(book_name=dict['book_name'], rate=dict['rate'])
                    publ.add_publ_book()
                else:
                    print('Choose another option')
            os.remove(file_path)
        except FileNotFoundError:
            print('There is no such file in the folder!')

    def publish_xml(self):
        file_path = self.file_path_func()
        try:
            xml_file = ET.parse(file_path)
            root = xml_file.getroot()
            x = int(input('How many rows do you want to process? '))
            elem_list = root.findall('./*')
            for i, element in enumerate(elem_list):
                if i > x - 1:
                    break
                if element.tag.lower() == 'news':
                    publ = News(news_text=element[0].text, city=element[1].text)
                    publ.add_publ_news()
                elif element.tag.lower() == 'ad':
                    publ = PrivateAd(ad_text=element[0].text, expiration_date=element[1].text)
                    publ.add_publ_ad()
                elif element.tag.lower() == 'book':
                    publ = BookAdvise(book_name=element[0].text, rate=element[1].text)
                    publ.add_publ_book()
                else:
                    print('Choose another option')
            os.remove(file_path)
        except FileNotFoundError:
            print('There is no such file in the folder!')


class DBConnection:
    def __init__(self):
        with sqlite3.connect('newsfeedDB.db') as self.connection:
            self.cursor = self.connection.cursor()

    def newsfeed_parse(self):
        with open(file_name, "r") as self.newsfeed:
            readfile = self.newsfeed.read()
            split_list = readfile.split('------------------------------')
            cleansed_list = [news.replace('\n\n', '') for news in split_list]
            final_list = [news.split('\n') for news in cleansed_list]
            return final_list

    def insert(self):
        final_list = self.newsfeed_parse()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS News (news_text text, city text, datetime text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Ads (ads_text text, expiration_date text, days_left real)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Books (author text, book_name text, rate text)')

        for i in final_list:

            if i[0].lower().startswith('news'):
                city_date = i[2].split(',')
                news_query = f"INSERT INTO News VALUES ('{i[1]}', '{city_date[0]}', '{city_date[1]}')"
                self.cursor.execute("SELECT rowid FROM News WHERE news_text = ? and city = ? and datetime = ?",
                                    (i[1], city_date[0], city_date[1],))
                db_result = self.cursor.fetchone()
                if db_result is None:
                    self.cursor.execute(news_query)
                else:
                    print('This news already exists!')

            elif i[0].lower().startswith('private ad'):
                date_days = i[2].split(',')
                date = re.findall('(((0[1-9])|([12][0-9])|(3[01]))\/((0[0-9])|(1[012]))\/((20[012]\d|19\d\d)|(1\d|2[0123])))',
                    date_days[0])
                expiration_date = re.findall('[0-9]+', date_days[1])
                ad_query = f"INSERT INTO Ads VALUES ('{i[1]}', '{date[0][0]}', '{expiration_date[0]}')"
                self.cursor.execute("SELECT rowid FROM Ads WHERE ads_text = ? and expiration_date = ? and days_left = ?",
                                    (i[1], date[0][0], expiration_date[0],))
                db_result = self.cursor.fetchone()
                if db_result is None:
                    self.cursor.execute(ad_query)
                else:
                    print('This ad already exists!')

            elif i[0].lower().startswith('book'):
                author_book = i[1].split(' - ')
                rate = re.findall('[0-5]\/[0-5]', i[2])
                book_query = f"INSERT INTO Books VALUES ('{author_book[1]}', '{author_book[0]}', '{rate[0]}')"
                self.cursor.execute("SELECT rowid FROM Books WHERE author = ? and book_name = ? and rate = ?",
                    (author_book[1], author_book[0], rate[0],))
                db_result = self.cursor.fetchone()
                if db_result is None:
                    self.cursor.execute(book_query)
                else:
                    print('This ad already exists!')

        self.connection.commit()


feed_input = ''
while feed_input != 'exit':
    feed_input = input("Choose action: create publication by hand (write), from file (file), json (json), xml (xml) or stop execution (exit): ")
    if feed_input.lower() == 'write':
        feed_input = input('Please write what you want to add to the feed: News, Ad, Book: ')
        newsfeed = Publication(feed_input)
        newsfeed.publish_write()
        newsfeed.word_write()
        newsfeed.letter_write()
        newsfeedDB = DBConnection()
        newsfeedDB.insert()
    elif feed_input.lower() == 'file':
        feed_input = input('Choose a path from where to take the file: mine or default: ')
        newsfeed = Publication(feed_input)
        newsfeed.publish_file()
        newsfeed.word_write()
        newsfeed.letter_write()
        newsfeedDB = DBConnection()
        newsfeedDB.insert()
    elif feed_input.lower() == 'json':
        feed_input = input('Choose a path from where to take the file: mine or default: ')
        newsfeed = Publication(feed_input)
        newsfeed.publish_json()
        newsfeed.word_write()
        newsfeed.letter_write()
        newsfeedDB = DBConnection()
        newsfeedDB.insert()
    elif feed_input.lower() == 'xml':
        feed_input = input('Choose a path from where to take the file: mine or default: ')
        newsfeed = Publication(feed_input)
        newsfeed.publish_xml()
        newsfeed.word_write()
        newsfeed.letter_write()
        newsfeedDB = DBConnection()
        newsfeedDB.insert()
    elif feed_input.lower() == 'exit':
        break
print('Goodbye!')
