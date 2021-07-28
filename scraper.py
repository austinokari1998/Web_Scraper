from bs4 import BeautifulSoup as bs
import smtplib
import requests
import time
url = 'https://smis.uonbi.ac.ke/index.php'
#TO INPUT YOUR DETAILS OF THE REGISTRATION NUMBER AND THE PASSWORD TO THE PORTAL 
values = {'regNo': #'INPUT OFYOUR REGISTRATION NUMBER',
          'smisPass': # 'PASSWORD TO YOUR PORTAL ',
          'smisLogon':'Login'}
def fees_checker():
    with requests.Session() as s:
        p = s.post(url, data=values)
        # for a succeful login 
        print ("successful login ")

        # An authorised request.
        r = s.get('https://smis.uonbi.ac.ke/statement_summary.php')
        soup=bs(r.content, 'html.parser')
        cont_wished=soup.find("div",class_="left_articles")    
        for index, tr in enumerate(cont_wished.find_all("td", width="100%", align="left")):
            if index==2:
                fees_checker.variable=tr.text
                send_mail()
                print (fees_checker.variable)
                
                
                
            else:
                pass

               
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('austinokarikennedy@gmail.com', 'Okariokari1998')
    
    subject = 'YOUR SCHOOL FEES AS CHECKED '
    body = "Please.\n\n If the fee details you see are unsatisfactory, Please confirm with the department "

    msg = 'Subject: {} \n\n {}'.format(subject,body)

    server.sendmail(
        'austinokarikennedy@gmail.com',
        #'INPUT OF YOUR EMAIL ADDRESS ',
        msg
    )
    print('HEY! EMAIL HAS BEEN SENT')
    server.quit()

if __name__ == "__main__":
    while True:
        try:
            fees_checker()
            time.sleep(3600)
        except KeyboardInterrupt:
            print(' exiting from the program ...')
            break


