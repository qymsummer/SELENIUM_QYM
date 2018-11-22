from page.register_page import Register_Page
#from util.get_code import GetCode
class Register_Handle(object):

    def __init__(self,driver):
        self.driver = driver
        self.register_p = Register_Page(self.driver)
    def send_user_mail(self,email):
        self.register_p.get_email_element().send_keys(email)
    def send_user_name(self,name):
        self.register_p.get_username_element().send_keys(name)
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    def send_user_code(self,code):
        #get_code_text = GetCode(self.driver)
        #code = get_code_text.code_photo(filename)
        self.register_p.get_code_element().send_keys(code)

    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info == 'user_password_error':
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_error_elemenet().text
        except:
            text = None
        return text
    def click_register_button(self):
        self.register_p.get_butten_element().click()

    def get_register_text(self):
        return self.register_p.get_butten_element().text