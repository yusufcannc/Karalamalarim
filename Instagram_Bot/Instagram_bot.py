from selenium import webdriver
import time
import random
import sys

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self, user_name, password):

        self.user_name = user_name
        self.password = password
        self.browserProfile = webdriver.ChromeOptions()  # Bu ve altında ki özellikler ile tarayıcımız ingilizce olarak açılacaktır.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        #self.browserProfile.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.browserProfile)


    def signIn(self):
        print("burdayım1")
        self.browser.get("https://www.instagram.com/accounts/login/")
        print("burdayım2")
        self.browser.implicitly_wait(15)
        print("burdayım3")
        userInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        try:
            userInput.send_keys(self.user_name)  # Kullanıcı griniiz kısmına giriş verisini yazacak
            passwordInput.send_keys(self.password)  # Şifre giriniz kısmına giriş verisini yazacak
            passwordInput.send_keys(
                Keys.ENTER)  # Bunun sayesinde de şifre kısmında Enter'a basacak bu da giriş yap butonunu tetikleyecek.

        except:
            pass
        self.browser.implicitly_wait(10)
        print("burdayım4")
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.user_name}")  # başta ki soruda ki veriye göre giriş yapacak
        self.browser.implicitly_wait(10)
        followersLink = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()  # Profilde ki takipçi sayısı kısmına tıklayacak
        self.browser.implicitly_wait(10)

        dialog = self.browser.find_element_by_css_selector(
            "div[role=dialog] ul")  # Bunun sayesinde takipçi ekranına geleceğiz.
        followersCount = len(
            dialog.find_elements_by_css_selector("li"))  # Bunun sayesinde takipçilerin nicklerine erişeceğiz.

        print(f"Şu anda {followersCount} takipçi var.")  # Ekran da şu anda kaç takipçinin olduğunu gösteriyor.

        self.action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()  # Burada dialog ile takipçi penceresine bir kere tıklayacak ki Space tuşunu algılayabilsin.
            self.action.key_down(Keys.SPACE).key_up(
                Keys.SPACE).perform()  # key_down(Keys.SPACE) ile scroll aşağıya inecek ve up metodu ile de yukarıya çıkacak
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:  # followersCount newCount'a eşit değilse scroll aşağıya inmeye devam etsin.
                followersCount = newCount
                print(f"Toplam takipçi {newCount}")
                time.sleep(1)
            else:  # Eşitlenirse de bu döngüden çıkılsın.
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)

    def followUser(self, username):

        self.browser.get("https://instagram.com/" + username)  # Bu fonksiyon da ise instagram/username'e gitmektedir.
        self.browser.implicitly_wait(5)

        self.follow_button = self.browser.find_element_by_tag_name(
            "button")  # Butonun Html bilgisi button olduğu için ve sadece bir adet buton olduğu için direk button yazdım.
        if self.follow_button.text != "Following":  # Eğer takiptesin yazmıyorsa "Takip Et" butonuna tıklayacaktır.
            self.follow_button.click()
            self.browser.implicitly_wait(5)
        else:
            print("Kullanıcıyı zaten takip ediyorsunuz.")

    def unfollowUser(self, username):

        self.browser.get("https://instagram.com/" + username)
        time.sleep(2)
        self.follow_button = self.browser.find_element_by_tag_name("button")
        if self.follow_button.text == "Following":
            self.follow_button.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
            print(f"Artık {username}'i takip etmiyorsunuz.")
        else:
            print("Zaten takip etmiyorsunuz.")

    def likephoto(self, hashtag,href, photo_href):
        pass

print("-" * 30)
print("Instagram Bot'a Hoş Geldiniz! ")
print("-" * 30)

print("-" * 35)
print(""""1- Takipçileri göster.
2- Takipten Çık
3- Takip Et""")
print("-" * 35)

user_name = input("Kullanıcı adını giriniz: ")
password = input("Şifrenizi giriniz: ")
instgram = Instagram(user_name, password)
if user_name and password != "":
    instgram.signIn()
devam =""
while devam !="q":



    deger = input("Hangi değeri seçmek istersiniz: ")

    if deger == "1":
        instgram.getFollowers()
    elif deger == "2":
        kullanici = input("Hangi kullanıcıyı takipten çıkacaksınız: ")
        instgram.unfollowUser(kullanici)
    elif deger == "3":
        kullanici_ekle = input("Hangi kullanıcıyı takip edeceksiniz: ")
        instgram.followUser(kullanici_ekle)
    devam = input("Programı kapatmak için 'q' harfine basınız. Programı devam ettirmek için 'Enter' a basınız.")

