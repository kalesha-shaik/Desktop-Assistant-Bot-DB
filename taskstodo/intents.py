name=''
mailto=''
mailcontent=''
def get_intent(data):
    global name
    global mailto
    global mailcontent
    m=data['message'].lower()
    if data['key'] =="name":
        name=m
        return "next"
    elif data['key']=="Email-Id":
        mailto=m
        return "content"
    elif data['key']=="content" :
        mailcontent=m
        return "sendemail"
    elif data['key']=="Question":
        return "wikipedia"
    elif any(x in m for x in ["search" , "wikipedia"]):
        return "search"
    elif any(x in m for x in ["send","mail","inform","email"]):
        return "email"
    elif any(x in m for x in ["time","currenttime"]):
        return "time"
    elif any(x in m for x in ["Thank you","thankyou","thanks","thank you"]):
        return "thank"
    elif any(x in m for x in ["game","play","hangman","playing","games"]):
        return "game"
    else :
        return "echo"

def handle(data):
    global name
    from flask import render_template
    intent=get_intent(data)
    if intent == "search":
        return render_template('messages/mail.html',
        question={"key":"Question","text":"What do you want to search?"})
    elif intent =="wikipedia":
        from .wikipedia import getdata
        searchdata=getdata(data)
        return render_template('messages/wikiresult.html',
        searchdata=searchdata,
        question={"key":"task","text":""})
    elif intent == "email":
        return render_template('messages/mail.html',
        question={"key":"Email-Id","text":"Please enter the recipient Email ID"})
    elif intent == "content" :
        return render_template('messages/mail.html',
        question={"key":"content","text":"Please enter the content that you want to send to the recipient"})
    elif intent == "sendemail" :
        from .mail import sendmailto
        mailmsg = sendmailto(mailto,mailcontent)
        return render_template('messages/sendemail.html',
        mailmsg=mailmsg,
        question={"key":"task","text":""})
    elif intent == "next":
        return render_template('messages/greet.html',
        name=name,
        question={"key":"task","text":"Please let me know which task you would like to perform"})
    elif intent == "time" :
        from .time import gettime
        timemsg=gettime()
        return render_template('messages/sendtime.html',
        timemsg="The current time is "+timemsg,
        question={"key":"task","task":""})
    elif intent=="thank":
        return render_template('messages/thank.html',
        question={'key':'','text':''})
    elif intent == "game" :
        return render_template('gameinput.html',
        question={"key":"task","task":""})
    else:
        return render_template('messages/reply.html',
        question={'key':'','text':''})
        