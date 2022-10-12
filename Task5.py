from datetime import datetime
import random


class News:
    def __init__(self, news_text, city):
        self.news_text = news_text
        self.city = city

    def date_and_time(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M")

    def add_publ_news(self):
        f = open('newsfeed.txt', 'a')
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
        f = open('newsfeed.txt', 'a')
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

    def add_publ_news(self):
        f = open('newsfeed.txt', 'a')
        f.write('Book Advise ------------------')
        f.write(f'\n{self.book_name}')
        f.write(f'\nGoodreads.com rating: {self.random_rate()}/5')
        f.write('\n------------------------------')
        f.write('\n')
        f.write('\n')


class Publication(News, PrivateAd, BookAdvise):
    def __init__(self):
        self.i = input('Please write what you want to add to the feed: News, Ad, Book: ')

    def publish(self):
        if self.i == 'News':
            publ = News(news_text=input('Please write the text of the news: '), city=input('Please write city: '))
            publ.add_publ_news()
        elif self.i == 'Ad':
            publ = PrivateAd(ad_text=input('Please write the text of the advertising: '), expiration_date=input('Please write the expiration date in d/m/y format: '))
            publ.add_publ_ad()
        elif self.i == 'Book':
            publ = BookAdvise(book_name=input('Please write the name of the book: '), rate=input('Please write your rate from 1 to 5: '))
            publ.add_publ_news()
        else:
            print('Choose another option')


newsfeed = Publication()
newsfeed.publish()
