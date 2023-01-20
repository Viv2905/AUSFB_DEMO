from pickletools import read_uint1
from re import template
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
import random
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
# import speech
# import sound
from django.core.serializers import serialize
from django.views.generic import View
from numpy import size
from .models import customerTable

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import pyttsx3
from fpdf import FPDF

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class database(View):

    def get(self, request):
        items_count = customerTable.objects.count()
        items = customerTable.objects.all()

        items_data = []
        for item in items:
            items_data.append({
            'f_name': item.first_name,
            'l_name': item.last_name,
            'mob': item.mobile,
            'adrs': item.address,
            'amt': item.amount,
            'cardNo': item.customerCardNumber
        })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)

    def post(self, request, cardNumber):
        data = json.loads(request.body.decode("utf-8"))
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        mobile = data.get('mobile')
        address = data.get('address')
        amount = data.get('amount')
        c_number = cardNumber

        product_data = {
            'f_name': first_name,
            'l_name': last_name,
            'mob': mobile,
            'adrs': address,
            'amt': amount,
            'c_num': c_number
        }

        cart_item = customerTable.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)


def customer(request):
    if request.method == 'GET':
        return render(request, 'customer.html')

    elif request.method == 'POST':
        data = request.POST
        enteredName = data['name']
        enteredCardNumber = data['customerCardNumber']

        # print(type(enteredCardNumber))

        users = customerTable.objects.values()

        customerRecords = []
        for user in users:
            customerRecords.append(user)

        found = 0
        for i in customerRecords:
            if i['first_name'] == enteredName and str(i['customerCardNumber']) == enteredCardNumber:
                found = 1
                requiredDetails = i
                break

        if found:
            pdf = FPDF()
            pdf.add_page()
            # pdf.set_title("Customer details")
            pdf.set_font("Arial", 'B', size = 20)
            # pdf.set_stretching(50)
            pdf.cell(190, 15, txt = "CUSTOMER DETAILS", border = 1, ln=1, align = 'C')
            pdf.cell(200, 10, txt = "", ln=2, align = 'C')
            pdf.cell(200, 10, txt = "", ln=2, align = 'C')

            # pdf.set_stretching(0)
            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "First Name : ", ln=0, align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = requiredDetails['first_name'], ln=1, align = 'L')

            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "Last Name : ", align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = requiredDetails['last_name'], ln=1, align = 'L')

            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "Address : ", align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = requiredDetails['address'], ln=1, align = 'L')

            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "Mobile : ", align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = str(requiredDetails['mobile']), ln=1, align = 'L')

            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "Amount : ", align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = str(requiredDetails['amount']), ln=1, align = 'L')

            pdf.set_font("Arial", 'I', size = 11)
            pdf.cell(100, 10, txt = "Card Number : ", align = 'R')
            pdf.set_font("Arial", 'B', size = 11)
            pdf.cell(100, 10, txt = str(requiredDetails['customerCardNumber']), ln=1, align = 'L')

            # pdf.output(name = '', dest = '')
            pdf.output("CUSTOMER_test.pdf")


            # Making password-protected pdf
            out = PdfFileWriter()
            file = PdfFileReader("CUSTOMER_test.pdf")
            num = file.numPages

            for i in range(num):
                page = file.getPage(i)
                out.addPage(page)

            password = "password1"
            out.encrypt(password)

            with open("cus_temp.pdf", "wb") as file:
                out.write(file)

            if os.path.exists("CUSTOMER_test.pdf"):
                os.remove("CUSTOMER_test.pdf")

            return JsonResponse({"Status": "Customer details successfully downloaded"})

        else:
            return JsonResponse({"ERROR": "Customer is not Registered!!"})

        # print(customerRecords)

        # records = {id: customerRecords[id] for id in range(len(customerRecords))}
        # print(records)

        # return render(request, "cus-test.html", records)
        # return JsonResponse(records)



def admin1(request):
    if request.method == "GET":
        return render(request, 'admin.html')

    elif request.method == "POST":
        data = request.POST

        users = User.objects.all()
        # print(type(str(users[0])))
        origialAdmin = str(users[0])

        if data['name'] == origialAdmin and data['password'] == "vivek123":
            items_count = customerTable.objects.count()
            items = customerTable.objects.all()

            items_data = []
            for item in items:
                items_data.append({
                'first_name': item.first_name,
                'last_name': item.last_name,
                'mobile': item.mobile,
                'address': item.address,
                'amount': item.amount,
                'customerCardNumber': item.customerCardNumber
            })

            data = {
                'items': items_data,
                'count': items_count,
            }

            # Converting to PDF file
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=20)
            pdf.add_page()
            pdf.set_font("Arial", 'B', size = 20)

            pdf.cell(190, 15, txt = "DB Records", border = 1, ln=1, align = 'C')
            pdf.cell(200, 10, txt = "", ln=2, align = 'C')
            pdf.cell(200, 5, txt = "", ln=2, align = 'C')

            i = 1
            for item in items_data:
                pdf.set_font("Arial", size = 11)
                pdf.cell(190, 10, txt = "Customer Record: " + str(i), border=1, ln=1)

                pdf.set_font("Arial", 'I', size = 9.5)
                pdf.cell(100, 8, txt = "First Name : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = item['first_name'], ln=1, align = 'L')

                pdf.set_font("Arial", 'I')
                pdf.cell(100, 8, txt = "Last Name : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = item['last_name'], ln=1, align = 'L')

                pdf.set_font("Arial", 'I')
                pdf.cell(100, 8, txt = "Address : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = item['address'], ln=1, align = 'L')

                pdf.set_font("Arial", 'I')
                pdf.cell(100, 8, txt = "Mobile : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = str(item['mobile']), ln=1, align = 'L')

                pdf.set_font("Arial", 'I')
                pdf.cell(100, 8, txt = "Amount : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = str(item['amount']), ln=1, align = 'L')

                pdf.set_font("Arial", 'I')
                pdf.cell(100, 8, txt = "Card Number : ", align = 'R')
                pdf.set_font("Arial", 'B')
                pdf.cell(100, 8, txt = str(item['customerCardNumber']), ln=1, align = 'L')
                pdf.line(10, 41 + i*58, 200, 41 + i*58)
                i += 1

            pdf.output("ADMIN_test.pdf")


            # Making password-protected pdf
            out = PdfFileWriter()
            file = PdfFileReader("ADMIN_test.pdf")
            num = file.numPages

            for i in range(num):
                page = file.getPage(i)
                out.addPage(page)

            password = "password1"
            out.encrypt(password)

            with open("adm_temp.pdf", "wb") as file:
                out.write(file)

            if os.path.exists("ADMIN_test.pdf"):
                os.remove("ADMIN_test.pdf")
            
            # return JsonResponse(data)
            return JsonResponse({'Status': "Admin PDF successfully downloaded"})

        else:
            return JsonResponse({"Error":"INVALID user-id / password"})

        
def front(request):
    # METHOD-1
    # template = loader.get_template('frontPage.html')
    # return HttpResponse(template.render())


    # r = sound.Recorder("./welcome.mp3")
    # r.record(3)
    
    engine = pyttsx3.init()

    # For Zira, Voice ID:
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    
    # Voice changed -> female voice
    engine.setProperty('voice', voice_id)

    engine.setProperty('rate', 120)
    # engine.setProperty('volume', 1.0)
    
    # engine.say("..Namashkaar... Welcome to A U Small Finance Bank")
    engine.runAndWait()

    # METHOD-2
    return render(request, 'frontPage.html')

def push(request):
    if request.method == 'GET':
        return render(request, 'api_response.html')

    elif request.method =='POST':
        data = request.POST
        # print(data)
        first_name = data['name']
        last_name = data['eaddress']
        mobile = data['phone']
        address = data['street']
        amount = data['zip']

        customerCardNumber = random.randint(10000000, 99999999)

        product_data = {
            'address': address,
            'amount': amount,
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'customerCardNumber': customerCardNumber
        }

        cart_item = customerTable.objects.create(**product_data)
        
        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)
