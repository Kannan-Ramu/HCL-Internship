import os
import random
import smtplib
from datetime import datetime, timedelta
from random import randrange
from uuid import uuid4

import pymongo as mongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
from flask import Flask, jsonify, request,render_template
from flask_cors import CORS

 # take environment variables from .env.


"""
█▀▄▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ 
█░▀░█ █░░█ █░░█ █░▀█ █░░█ 
▀░░░▀ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀▀
"""

url ="mongodb://localhost:27017"
client = mongo.MongoClient(url)

"""
█▀▀ █░░ █▀▀█ █▀▀ █░█ 
█▀▀ █░░ █▄▄█ ▀▀█ █▀▄ 
▀░░ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀
"""
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type, Access-Control-Allow-Origin'

@app.route("/", methods=["GET"])
def main():
	return "ok"
@app.route("/mainpage",methods=["GET"])
def mainpage():
    db=client['images']    
    db1=db['image']
    links=['https://lh3.googleusercontent.com/aIgSVn-emlwNIWjq7k_GbLPg7Wef1mja0Pc4EGk7YSvBsZj9vOmGWqjCJHNpOMpYeWwy1hEjdLUBTMPfZY__R1XtmvOee_l0dcHiOj5HtAJy0N4dzN6Q1jU5DZQeZedgyrIZxPgcT8Iyv7_IWzhNnJYpI59fUuGL_lM6J-ABOs4Zan6_m7qaYGc50xDM-ed97LjpxbMej4bCxi5qE8JWVqESmYOiWzhOGHC1MiU7cgRfWbH0ZlktXN_LkGNg7jZxIYofDPg00Q2P_zZBbNW2Wo21mj_o7buSuAieqmGwkv6zuiPtRkFoI1YWA1dUVyPWJliB2uyyZmLCtXqOdKjZyQ_EX1HTHlXYMOmjl0KLmqd9PrVwUI-cSTRJdeAuLoG82AEDItM-AAxB-xuMacSXWtcLhB2h919KAox-HjgFWhW-CNpJ3_XaaSTkbPKj4ybvDKCLSvPf2BWgQi0VwvtPSkvpVw50MXzY59EJ1p_JqFb5hLNafkWtKsqtmBl6wspB6kBiFQDvJoc3JC9m0XWDXjUptJ90PJkJAQK5wZTO4QswVJdfsYhdQtqH_r9LvQnUYDgJ_Y6Y8pNlERnW0L0GGJg6zLB7e_4mfrIPM42OZxg_kQVXu-revoeE--LRhpakgXK3Kri7DAXUB-bJT0dVr-wNvB1iPa7WNDQO6pEQBTdzzR6_WtdzdAVLeyeSnoqe0ofsI0W-XIdgRO-fwEiSccF-Q72KKRhvMC7o5AXo3-ZHO8FZIpCtH5XZ_x0aV4qCnH9vC9JA9kbWkHgHt2Xjidd_3H29ZGose7qTYZ3TU546c2BIP8skV-oWJH7rapkNxtW-5K2sdk95zCc-ta1xw34-Nsssy0oPo3wSU2DwFUwgTNBB2-RdF2An1ceQjU_SxmTDZu1Bw6MW088cKRHQDJg2nVMQ3HYuprYy8OfSl5Crl1qfwBnFedM-wRWTO60up2MNZFQxZ0bbmAcOSCCGLp2Npn1lZqj7bBdI1cZemsIfA6SZ9whaP4wW97fiGQdmhgVjIS1rRJPMy8gylyUzhxIYHWaiUGX3kAJk6QWAaR_htcdTLOZaG9Z77Y2neQ9xjCQc8EpO8A4lLyXYHhVGYr9ge_u-=w700-h933-no?authuser=4',"https://lh3.googleusercontent.com/kcHurNSflxIpPZ8ABnJUlI2kxa0peFMzuqiOcLaXlmzDWafFj_lYa2gd8h0xZ8p-g1h0_snqS3Uk_N3ZAMXND9MbPhzb6HC0cckYW0C2y6PqH3hP7wCQbnAcR1iydNbxPAOj72F4_HS7MwBCW8EzRn1T66J7sRl1SXBSOL1lsAY3AknmQZzNjgE92azlq6PTlkv4Yr3_szgTRIrsX1Urk43uAxgfxcisJBpgXePFy0OSi6C0EGvWlbsjgY-H3pStz3q8noBDb2KGsIkU6IL7Mm5A8yOuqPayz9GDP1F-lSpxyZ3WAZIPf4FSYsyfwqjhHkLxpOUpooyl5HOeoHqbTszK7WaUY2zT6F2qQYJnqsimEwrR5ugxgmrQPGnbPXBYCY3ljrXWdo78PmoK97EBpOS_NWkCdawSL5VUYzqmJPnYBVcifPyjN1VFj33UDLuJLPGH3UJhfaswamRzhJlJiYn6ZzW6NiKrivoXritQV0shoyOsgPe3ZLCViiiQeg23rRwzpC27yJHe_rON8_8TfNPyMndaM9uXDFpUgPJtNYyJJ3MR2nu6iixzIW1e21oTG3R0fDTlTHyxEvSxz8tOrIKqr4I9-Grt_ug2xIDvsP3P4PbKfyyzFdJP1Lsa4iHZ1FJ4gq5Rq1_k-b102sHaqvwoKajvzepxisO2WQm1rGj0R4_PUxLImRI7skOu3yrjnPutt5S1iVWLUlE5CerV-CN01qSU0Kg4qG-F-7FqADsfHmgyKDcxyVIoLrsKp2LycB-rTQ_tDna-G8qwnmjd3su9IVfHmYNwoxMtnT-iEvOOFEhLmcbZJt90IAN7qXZUKvwk0PsM4q3umQYXISZCbFutz1Hn0mD5Mt7Ir8CFbwVv6hdWfbNUsHxT-zwViCKLAxP1lBEhoPvbc3RThcDv0_gGTpfvOL_WIawbVZlSgPnCBb-nVWyUfP7IkUA9YPidQmUIkFmOYmQyfq_EOxZl00OCRSBa96lj07u-vOpeaU07NsCwoLi6JGO4VGqI7Uv_fwHG3WwFeZA60znjFrQ2SztmNl5slyzoKmjfV75r6ZKeuVajo7l98LK3694HeusR87FkP1GGaOIVKLJEwG5Tp_5OzkUf=w700-h933-no?authuser=4","https://lh3.googleusercontent.com/B75q83Z-DKID0pKv9_OaK6wqpDd0r1Cl-fIrg1I7YVPij5Tuk7rPJ8lPf8CeWPCGSph4AcdOsnpg5uNQME6acUdze9JsijUbiFy22vsk240jMvc6pmT0ZqgV9zVWi4YOu1BsFQedYx2m4nJNZDynUkU5b16hxnr5AiaeL1gFU0wFOP9avfsTL_7Bss-qbJOqvWPkTQ-sTFcKEu9-UJ2rqxrf8Njc0DHBKPUWUt1i1VPAio80S8Gjzf8XJxWFNC2mGdj8j1HDj4Tl5GxPcIO_ap-LDI-z_qduuL4wJIU4pJfQZ8ZUa-Dg9FIQdsjLSzf5j9QIkpePjRubMd99-sPdBFmdjPqZstiNUJba_Hcug_kgFKo9xkE6K1dDXJ82DXkwS4db_kNY2jxOUV4mUB3qp2zQXURVi8oVaX0xG7EvqhPEn6dpdGw5sorYlS9fIjm7WgNpqGSELZsELVtpj1tRvjWHUTXGrwxCSDXicBymbLKIDcbYcyygQ2fBqoBFSuFKXM6InyrJipN3KHbHR6i5wwBv55j_5HIDOopWY1cCSJMRLwrIBQq6vcqWgrVZUNQHLiNJa7XvuqPejk-TUYLrfSmo5Vj_dOhxDKhsoUMkUp1viq4Dd1qoYdmWfCh7NqCj2kHRuDd3bd1vml9ebCSGv9Ak35mpHXK6IBuV12vLYL5uv2PLmzZ9zJ73fiejeA_wdwJXPXrbhMNHChVhyTmZtCjpUFDVVVTgaSLpGUffxkYV1zLTh-AoA7DjbmpRbGMMvXXtCf8Zfv5q9A5L6IJWXXSkB6QmWHekOFcyG5ai7faj2E2NQvPEw26doNNhJBn8-x23IrzArPMd2CqJfJ8MfyRozKvIBALjUo9LtObK6uQjidQP70VIBI8e_GppiajZPb6vUznt7nefPYtO7KPFK6iTiMPO5uuSYcBrl4h9xhb6t1Ov-gsAnB33Gk1khWasKJdUTviETTgC1XL4JJE8e5QVjmCoEU8_2qbln7LAXr-bCyMRUK4y1dWmCElBFNgvfqMFQU450DS7OWon6Wlp7NA-wndQbCiYbkY4hM_o7kg71ybtxmVUWRa0BP3N4dyJIA3g6BonG1xReoRQlg8wKZum0leb=w700-h933-no?authuser=4"]
    linknames=['1st','2nd','3rd']
    db1.insert_one({'id1':1,"loc":"hnsdjnjhsduhhwui2hui2h2"})
    kaj='https://www.myindianart.com/uploads/banner/banner5.jpg'

    return render_template('index1.html',len=len(links),kaj=kaj,links=links,linknames=linknames)
if __name__ == "__main__":
	app.run(debug=True)
