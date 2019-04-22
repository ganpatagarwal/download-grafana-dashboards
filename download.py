"""
this program is written in python3
requires
    python selenium package
    chromedriver
works on
	grafana v5.1 and above
"""


import time
import os
from selenium import webdriver

FILENAME = "dashboard_links.txt"
XPATH_SHARE = "/html/body/grafana-app/div[2]/div/div/div/dashnav/div/div[3]/button[3]"

# create time string
named_tuple = time.localtime()
time_string = time.strftime("%m-%d-%Y_%H-%M-%S", named_tuple)
# create destination directory
dest_dir = os.path.join(os.getcwd(), "Dashboards-" + time_string)
# just making sure
if os.path.exists(dest_dir):
	os.rmdir(dest_dir)
os.mkdir(dest_dir)

# customize chrome driver
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : dest_dir}
options.add_experimental_option('prefs', prefs)

# parse text file for links
with open(FILENAME) as file:
	for entry in file:
		print(entry)
		# initialize driver
		driver = webdriver.Chrome(options=options)
		# go to link
		driver.get(entry)
		# sleep to make sure page is visible
		time.sleep(5)
		# find element for 'share' and click
		share = driver.find_elements_by_xpath(XPATH_SHARE)
		share[0].click()
		time.sleep(2)
		share_tab_elements = driver.find_elements_by_class_name("gf-tabs-item")
		for s_element in share_tab_elements:
			# find element for 'Export' option
			if s_element.text == "Export":
				s_element.click()
				time.sleep(2)
				export_tab_elements = driver.find_elements_by_class_name("btn-success")
				for e_element in export_tab_elements:
					# find element for "Save to File" option
					if e_element.text == "Save to file":
						e_element.click()
						time.sleep(5)
						break
		# quit driver
		driver.quit()
