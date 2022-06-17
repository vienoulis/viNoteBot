import telebot
from peewee import MySQLDatabase

from ru.vienoulis.service.state import State

db = MySQLDatabase('vi_note_db', user='root', passwd='12341234')
bot = telebot.TeleBot('855393784:AAGxBrLMZoVjzcWv6veIh2YyhQdt5UmfX6o')
current_state = State.empty
