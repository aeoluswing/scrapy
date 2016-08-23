# -*- coding: utf-8 -*-
# author:jiangyu
# modify:2016-08-18
# gov_affair_detail.py

import pymongo
from settings import MONGO_URI, MONGO_DATABASE
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_result():
	client = pymongo.MongoClient(MONGO_DATABASE)
	db = client[MONGO_DATABASE]
	results = db["GovAffairDetails"].find()
	client.close()
	return render_template('result_index.html',p_results=results)

if __name__ == '__main__':
	app.run()