import math
import sys
import smtplib

class Util:
  def __init__(self):
    pass

  def mail(self,sender,recipient,message,password):
    self.s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    self.s.starttls()
    self.s.login(sender, password)
    self.s.sendmail(sender,recipient,message)
    self.s.quit()

  def scrub(self,txt):
    if "<" in txt and ">" in txt:
      return txt.split('<')[1].split(">")[0]
    return txt
