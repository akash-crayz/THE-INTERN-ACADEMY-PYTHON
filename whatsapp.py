
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com/")


def ask():
		print("Do you want to send more message to anyone")
		askUser = input("Press y for Yes and n for No : ")
		if (askUser == 'Y' or askUser == 'y'):
				sendMessage()
		elif (askUser == 'N' or askUser == 'n'):
				print("Thank you see you soon")
		else:
				print("Please Enter Valid option :\n")
				ask()
				
def sendMessage():
		receiverName = input('\nEnter Group/User Name: ')
		message = f'Happy Birthday to you { receiverName }'
		try:
				count = int(input("Enter the message count: "))
				timingInMinute = int(input("Enter the time in min: "))
				timing = (timingInMinute)*60

				receiver = driver.find_element_by_xpath(
						'//span[@title = "{}"]'.format(receiverName))
				
				receiver.click()
		
		except:
				sendMessage()

		sleep(timing)

		text_box = driver.find_element_by_class_name('p3_M1')

		for i in range(count):
				text_box.send_keys(message)
				driver.find_element_by_class_name("_4sWnG").click()

		ask()
		
sendMessage()