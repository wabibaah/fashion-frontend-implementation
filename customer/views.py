
from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Contact

## these are done for sending emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.

def contact(request):
  if request.method == "POST":
    fname = request.POST.get('name')
    femail = request.POST.get('email')
    fphone = request.POST.get('phone')
    fdesc = request.POST.get('desc')

    query = Contact(name=fname, email=femail, phoneNumber=fphone, description=fdesc)
    query.save()
    # messages.info(request, "Thanks for Reaching Us! We will get back to you soon...")

    ### email sending start from here
    from_email = settings.EMAIL_HOST_USER

    connection = mail.get_connection()
    connection.open()

    ### the email will be sent from the wabismptp@gmail to the admins, let say moses and bilson email addresses

    ## this is for the admin(s) .. the email that will be sent to them
    email_message = mail.EmailMessage(f'Email from: {fname}', f'UserEmail: {femail}\nUserPhoneNumber: {fphone}\n\n\n QUERY: {fdesc}', from_email, ['wabisernproject@gmail.com', 'mwabibaah@gmail.com'], connection=connection )

    ## this is for the user's on our website / you can even set it up so that the user's email can be the request.user.email if he / she is indeed logged in .. the email that will be sent to them
    email_client = mail.EmailMessage(f'Sedem Coutour Response', f'Thanks for reaching us\n\nsedem_seanefu_coutour@gmail.com\n0244639729 .\n We will get to your soon via call, email or text message', from_email, [femail], connection=connection )

    connection.send_messages([email_message, email_client])
    connection.close()

    messages.info(request, "Thanks for Reaching Us! We will get back to you soon...")

    return redirect('contact')

  context = {}
  return render(request, 'customer/contact.html', context)



### we are not l
### super user is the smtp email wabisernsmtp
### admins can be more than one 
### if the superuser (smtp email guy) is the same as the admin, then you can send the message to yourself

