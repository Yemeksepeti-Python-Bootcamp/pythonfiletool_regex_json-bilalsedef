#!/usr/bin/env python

from Database_Modifier.database_modifier import DbModifier
from Data_Modifiers.json_modifier import DataParser
from Data_Modifiers.regex_modifiers import regex_check
from argparse import ArgumentParser

argparser = ArgumentParser()
argparser.add_argument("--json_path", "--file", type=str, required=True)
argparser.add_argument("--db_path", "--db", type=str, required=True)
args = argparser.parse_args()

json_path = args.json_path
db_path = args.db_path

dp = DataParser(json_path)
allusers = dp.jsontolist()

dbops = DbModifier(db_path)
dbops.createTable()
dbops.insertUserList(allusers)
