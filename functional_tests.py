from selenium import webdriver
import unittest

browser = webdriver.Firefox()


class NewVisitorTest(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)


        def tearDown(self):
            self.browser.quit()
        
        def test_can_start_a_list_and_retrieve_it_later(self):
        ##  #edith has heard about a cool new online to-do app. She goes 
            #checkout its homepage
            self.browser.get('http://localhost:8000')    

            # she notices the page title and header mention to-do lists

            self.assertIn('To-Do', self.browser.title)   
            self.fail('Finish the test!')


            #```she is invited to enter a to-do item straight away

if __name__== '__main__':
    unittest.main(warnings='ignore')




#she types "Buy peacock feathers" into a text box ("Edith's hobby 
# is flying -fishing lures")


#when she hits enter , the page updates and now the page lists

#: buy peaacock feathers" as an item in a to-do list


#There is still a text box inviting hr to add anoher item. She
#enters "Use peacock feathers to make a fly" ( Edit is very methodical)


#the page updates again and now shows both items  on her list



#edith wonders wether the site will remember her list.  Then she sees


#that the site has generated a unique URL for her -- there is some 
#explanatory text to that efect.


#she isits that URL - her to-do list is still there.

#satisfied , She goes back to sleep.

browser.quit()

