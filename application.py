from flask import Flask, request
import json
import pickle
from calculate import get_ratio, count

app = Flask(__name__)
model = pickle.load(open('model2.pkl', 'rb'))
app.secret_key = "detectform"

#@app.route("/")
#def home():
    #return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def predictfile():

    global fn, mn, ln, fn2, mn2, ln2, d, d2, ssn01, ssn02, acc, acc2, s, st, z, z2, st2, c2, s2, c01, ass2, m, sub, sub2
    json1 = request.args['json1']
    json2 = request.args['json2']
    #url1 = url1.replace(" ", "%20")
    #url2 = url2.replace(" ", "%20")
    #a = urllib.request.urlopen("https://classification123-service.azurewebsites.net/?blob=%s" % url1).read().decode('UTF-8')
    data1 = json.loads(json1)
    #b = urllib.request.urlopen("https://classification123-service.azurewebsites.net/?blob=%s" % url2).read().decode('UTF-8')
    data2 = json.loads(json2)

    #print(data1)
    #print(data2)
    if data1["DETAILS"]["First Name"]:
        fn = data1["DETAILS"]["First Name"]
    else:
        fn = "Not present"
    if data1["DETAILS"]["Middle Name"]:
        mn = data1["DETAILS"]["Middle Name"]
    else:
        mn = "Not present"
    if data1["DETAILS"]["Last Name"]:
        ln = data1["DETAILS"]["Last Name"]
    else:
        ln = "Not present"
    if data1["DETAILS"]["DOB"]:
        d = data1["DETAILS"]["DOB"]
    else:
        d = "Not present"
    if data1["DETAILS"]["SSN"]:
        ssn01 = data1["DETAILS"]["SSN"]
    else:
        ssn01 = "Not present"
    if data1["DETAILS"]["Street"]:
        s = data1["DETAILS"]["Street"]
    else:
        s = "Not present"
    if data1["DETAILS"]["City"]:
        c01 = data1["DETAILS"]["City"]
    else:
        c01 = "Not present"
    if data1["DETAILS"]["State"]:
        st = data1["DETAILS"]["State"]
    else:
        st = "Not present"
    if data1["DETAILS"]["Zip-code"]:
        z = data1["DETAILS"]["Zip-code"]
    else:
        z = "Not present"
    if data1["DETAILS"]["Account No."]:
        acc = data1["DETAILS"]["Account No."]
    else:
        acc = "Not present"
    if data1["Sub-Category"]:
        sub = data1["Sub-Category"]
    else:
        sub = "Not present"


    if data2["DETAILS"]["First Name"]:
        fn2 = data2["DETAILS"]["First Name"]
    else:
        fn2 = "Not present"
    if data2["DETAILS"]["Middle Name"]:
        mn2 = data2["DETAILS"]["Middle Name"]
    else:
        mn2 = "Not present"
    if data2["DETAILS"]["Last Name"]:
        ln2 = data2["DETAILS"]["Last Name"]
    else:
        ln2 = "Not present"
    if data2["DETAILS"]["DOB"]:
        d2 = data2["DETAILS"]["DOB"]
    else:
        d2 = "Not present"
    if data2["DETAILS"]["SSN"]:
        ssn02 = data2["DETAILS"]["SSN"]
    else:
        ssn02 = "Not present"
    if data2["DETAILS"]["Street"]:
        s2 = data2["DETAILS"]["Street"]
    else:
        s2 = "Not present"
    if data2["DETAILS"]["City"]:
        c2 = data2["DETAILS"]["City"]
    else:
        c2 = "Not present"
    if data2["DETAILS"]["State"]:
        st2 = data2["DETAILS"]["State"]
    else:
        st2 = "Not present"
    if data2["DETAILS"]["Zip-code"]:
        z2 = data2["DETAILS"]["Zip-code"]
    else:
        z2 = "Not present"
    if data2["DETAILS"]["Account No."]:
        acc2 = data2["DETAILS"]["Account No."]
    else:
        acc2 = "Not present"
    if data2["Sub-Category"]:
        sub2 = data2["Sub-Category"]
    else:
        sub2 = "Not present"
    cat = data2["DETAILS"]["Category"]
    if cat is "Client Account Transfer Form ":
        m = 1
    else:
        m = 0
    if data2["Mutual Funds"]:
        ass2 = data2["Mutual Funds"]
    else:
        ass2 = "Not present"

    name1 = fn + " " + mn + " " + ln
    #print(name1)
    name2 = fn2 + " " + mn2 + " " + ln2
    #print(name2)
    c, c1 = count(name1, name2)
    if name1=="Not present" or name2=="Not present":
        name="---"
    else:
        if c >= 2 and c1 >= 2:
            ra = get_ratio(name1, name2)
            feat = [[ra]]
            name = model.predict(feat)
            if name == 1:
                name = "Matched"
            if name == 0:
                name = "Mismatched"
        else:
            name = "Mismatched"

    dob1 = d
    #print(dob1)
    dob2 = d2
    #print(dob2)
    if dob1=="Not present" or dob2=="Not present":
        dob="---"
    else:
        ra1 = get_ratio(dob1, dob2)
        feat = [[ra1]]
        dob = model.predict(feat)
        if dob == 1:
            dob = "Matched"
        if dob == 0:
            dob = "Mismatched"

    ssn1 = ssn01
    ssn2 = ssn02
    #print(ssn1)
    #print(ssn2)
    if ssn1=="Not present" or ssn2=="Not present":
        ssn="---"
    else:
        ra3 = get_ratio(ssn1, ssn2)
        feat = [[ra3]]
        ssn = model.predict(feat)
        if ssn == 1:
            ssn = "Matched"
        if ssn == 0:
            ssn = "Mismatched"

    accno1 = acc
    accno2 = acc2
    #print(accno1)
    #print(accno2)
    if accno1=="Not present" or accno2=="Not present":
        accno="---"
    else:
        ra4 = get_ratio(accno1, accno2)
        feat = [[ra4]]
        accno = model.predict(feat)
        if accno == 1:
            accno = "Matched"
        if accno == 0:
            accno = "Mismatched"

    add1 = s + " " + c01 + " " + st + " " + z
    add2 = s2 + " " + c2 + " " + st2 + " " + z2
    #print(add1)
    #print(add2)
    if add1=="Not present Not present Not present Not present" or add2=="Not present Not present Not present Not present":
        add="---"
    else:
        ra2 = get_ratio(add1, add2)
        feat = [[ra2]]
        add = model.predict(feat)
        if add == 1:
            add = "Matched"
        if add == 0:
            add = "Mismatched"

    if m is 1:
        mutual1 = ass2
        mutual2 = "AHYMX" or "ADNYX" or "GPRIX" or "NSDVX" or "PRIJX" or "VMSXX" or "SGARX" or "ARBIX" or "AWMIX" or "GPGIX" or "BIVIX" or "MSCFX" or "RAIIX" or "IOFIX" or "PTIAX"
        ra4 = get_ratio(mutual1, mutual2)
        feat = [[ra4]]
        mutual = model.predict(feat)
        if mutual == 1:
            mutual = "Yes"
        if mutual == 0:
            mutual = "---"
    else:
        mutual = '---'

    subcat1 = sub
    subcat2 = sub2
    if subcat1 == "Not present" or subcat2 == "Not present":
        subcat = "---"
    else:
        ra5 = get_ratio(subcat1, subcat2)
        feat = [[ra5]]
        subcat = model.predict(feat)
        if subcat == 1:
            subcat = "Matched"
        if subcat == 0:
            subcat = "Mismatched"

    output = {"Full Name": name, "SSN": ssn, "DOB": dob, "Address": add, "AccountNo": accno, "SubCategory": subcat, "Signature": "---", "DateofSignature": "---", "ViolationofMutualFund": mutual}
    o = json.dumps(output, indent=9)
    return o
    #return render_template('predict.html', name=name, dob=dob, ssn=ssn, accno=accno, add=add, mutual=mutual, subcat=subcat, sig="---")


if __name__ == "__main__":
    app.run(debug=True)

