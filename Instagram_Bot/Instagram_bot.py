from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


user_name = input("Kullanıcı adını giriniz: ")
password = input("Şifrenizi giriniz: ")

class Instagram:
    def __init__(self,user_name,password):

        self.browser = webdriver.Chrome()
        self.user_name = user_name
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        userInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        userInput.send_keys(self.user_name) # Kullanıcı griniiz kısmına giriş verisini yazacak
        passwordInput.send_keys(self.password) # Şifre giriniz kısmına giriş verisini yazacak
        passwordInput.send_keys(Keys.ENTER) # Bunun sayesinde de şifre kısmında Enter'a basacak bu da giriş yap butonunu tetikleyecek.

        time.sleep(2)


    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.user_name}") #başta ki soruda ki veriye göre giriş yapacak
        time.sleep(1)
        followersLink = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click() # Profilde ki takipçi sayısı kısmına tıklayacak
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul") # Bunun sayesinde takipçi ekranına geleceğiz.
        followersCount = len(dialog.find_elements_by_css_selector("li")) # Bunun sayesinde takipçilerin nicklerine erişeceğiz.


        print(f"Şu anda {followersCount} takipçi var.") # Ekran da şu anda kaç takipçinin olduğunu gösteriyor.

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click() # Burada dialog ile takipçi penceresine bir kere tıklayacak ki Space tuşunu algılayabilsin.
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()  # key_down(Keys.SPACE) ile scroll aşağıya inecek ve up metodu ile de yukarıya çıkacak
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount: # followersCount newCount'a eşit değilse scroll aşağıya inmeye devam etsin.
                followersCount = newCount
                print(f"Toplam takipçi {newCount}")
                time.sleep(1)
            else:  #Eşitlenirse de bu döngüden çıkılsın.
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)






instgram = Instagram(user_name,password)
instgram.signIn()
instgram.getFollowers()

