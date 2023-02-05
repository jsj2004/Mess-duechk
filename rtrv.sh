#!/bin/bash
echo "data in form: [ROLLNO,NAME,dues up and including previous month,mess bill for current month,hostel chrg,tathva/ragam,fine,fine_wea,payment,dues up and including current month,rollno,remark"
curl -X 'GET' 'http://127.0.0.1:8000/rinp?rno='$1 -H 'accept: application/json'

