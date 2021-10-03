import pygame
import sys
import random
from tkinter import *
import sqlite3


def gameregister():
    root = Toplevel()
    # connect to database
    connector = sqlite3.connect("Login.db")
    # we created cursor to invoke methods that execute sqlite statements,
    # which fetch data from the result sets of the quries.
    cur = connector.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS  login_page (
                   username text,
                   password text) """)

    print("Table has been created successfully.")

