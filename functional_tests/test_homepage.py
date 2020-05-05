from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
import pandas as pd
import time

class TestHomePage(StaticLiveServerTestCase):
    def setUp(self):
        """SET UP the web driver"""
        self.user = User.objects.create_user('ankur','ankur@friends.com','ankur1234')
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
        self.test_det = pd.read_csv("test1.csv")
        # print("**********",self.test_det.shape[0])

    def tearDown(self):
        """close web driver"""
        time.sleep(1)
        self.browser.close()


    def test_home_screen(self):
        """checks if home page is opening"""
        time.sleep(1)
        self.browser.get(self.live_server_url)
        # time.sleep(5)
        # print("nana\n")
        alert = self.browser.find_element_by_class_name("container-fluid")
        o = alert.text
        # print(o,"\n")
        self.assertEqual(alert.text,'You are a guest.')

    def test_login_redirects_to_loginpage(self):
        time.sleep(1)
        """Check login button redirects to login page"""
        self.browser.get(self.live_server_url)
        # print("***********************",reverse('/accounts/log-in/'))
        add_url = self.live_server_url+'/accounts/log-in/'
        print(add_url)
        # time.sleep(5)
        # print("nana\n")
        self.browser.find_element_by_link_text('Log in').click()
        self.assertEqual(self.browser.current_url,
                         add_url
                         )


    def test_create_a_account_redirects_to_signuppage(self):
        '''Check create account button redirects to sign up page'''
        time.sleep(1)
        self.browser.get(self.live_server_url)
        # print("***********************",reverse('/accounts/log-in/'))
        add_url = self.live_server_url+'/accounts/sign-up/'
        print(add_url)
        # time.sleep(5)
        # print("nana\n")
        self.browser.find_element_by_link_text('Create an account').click()
        self.assertEqual(self.browser.current_url,
                         add_url
                         )


    def test_change_language_redirects_to_languagepage(self):
        """Change language redirects to language page"""
        time.sleep(1)
        self.browser.get(self.live_server_url)
        # print("***********************",reverse('/accounts/log-in/'))
        add_url = self.live_server_url+'/language/'
        print(add_url)
        # time.sleep(5)
        # print("nana\n")
        self.browser.find_element_by_link_text('Change language').click()
        self.assertEqual(self.browser.current_url,
                         add_url+'2'
                         )


    # # def test_good_login(self):
    # #     """check if login is successful"""
    # #     expected_url = self.live_server_url
    # #     self.browser.get(f'{expected_url}/accounts/log-in/')
    # #     # time.sleep(2)
    # #     # print("password",self.user.password)
    # #     self.browser.find_element_by_id('id_email').send_keys(self.user.email)
    # #     self.browser.find_element_by_id('id_password').send_keys('ankur1234')
    # #     # time.sleep(2)
    # #     self.browser.find_element_by_class_name('btn').submit()
    # #     # time.sleep(5)
    # #     print("current url", self.browser.current_url, expected_url)
    # #     # time.sleep(2)
    # #     self.assertEqual(self.browser.current_url,expected_url+'/')


    def test_good_login(self):
        time.sleep(1)
        """check if login is successful"""
        flag = 1
        for i in range(self.test_det.shape[0]):
            expected_url = self.live_server_url
            self.browser.get(f'{expected_url}/accounts/log-in/')
            # time.sleep(2)
            # print("password",self.user.password)
            self.browser.find_element_by_id('id_email').send_keys(self.test_det.email[i])
            self.browser.find_element_by_id('id_password').send_keys(self.test_det.password[i])
            # time.sleep(2)
            self.browser.find_element_by_class_name('btn').submit()
            # time.sleep(5)
            print("current url", self.browser.current_url, expected_url)
            # time.sleep(2)
            print(f"test case {i} result {(self.browser.current_url == expected_url + '/')}")
            flag = flag and (self.browser.current_url == expected_url + '/')
            # self.test_det.result[i] = True
        if flag == 1:
            self.assertTrue(flag,"All tests successful")
        else:
            self.assertTrue(flag,"not all tests passed")



