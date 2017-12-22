username = 'xxxx@xxxx.com'
password = 'xxxxx!1'

class login(object):
  
  
#username
  def UserName(self,username):
  driver.find_element_by_name("username").send_keys(username)
#Password
  def Password(self,password):
  driver.find_element_by_name("password").send_keys(password)

