import telebot
from peewee import MySQLDatabase

db = MySQLDatabase('vi_note_db', user='root', passwd='12341234')
bot = telebot.TeleBot('855393784:AAGxBrLMZoVjzcWv6veIh2YyhQdt5UmfX6o')