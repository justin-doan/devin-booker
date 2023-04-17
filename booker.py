import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui

driver = webdriver.Chrome()
driver.get('https://sportsbookings.liv.ac.uk/scuba6/stellar2/activityBooking.php#/select/1/-1')

log_in_button = driver.find_element(By.ID, 'dcs-login-btn-fixed')
log_in_button.click()

time.sleep(1)

input_email = driver.find_element(By.ID,'inputEmail')
input_password = driver.find_element(By.NAME,'inputPassword')

input_email.send_keys('sgjdoan')
input_password.send_keys('Pyraminx2002')

submit_login = driver.find_element(By.ID,'sc-btn-login')
submit_login.click()

time.sleep(1)

try:
    dont_remind_me = driver.find_element(By.ID, 'modal-ok-button')
    dont_remind_me.click()
except:
    print('No don\'t remind me message, continue')
# We're in

time.sleep(2)

try:
    select_membership = driver.find_element(By.ID,'cboFamilyMembers')
    select = Select(select_membership)
    select.select_by_index(1)
except:
    print("You are not a member")

try:
    make_booking_button = driver.find_element(By.ID, 'ScubaId668876661i')
    make_booking_button.click()
except:
    print('Into bookings page already')

# Activities Mapping
index = {
    'GB_Hardcourts': 3,
    'First_Floor' : 4,
    'Ground_Floor' : 5,
    'Cage' : 10
}

activities_menu = driver.find_element(By.ID, 'sc-start-controller')
activities = activities_menu.find_elements(By.CSS_SELECTOR, "div[role='button']")
activities[index['Cage']].click()
# Select Furthest Date 
# Since the times are always the same, perhaps hard code index if we can't select by id

# Select time index, select confirm now
# Select Furthest Date
select_date = driver.find_element(By.ID,'cboBookDate')
select = Select(select_date)
select.select_by_index(7) # Always one week in advance so index 0 will be today and -1 will be 1 week from today
                           # Should range from 0 to 7
# Before it selects the timeslot, have it take a snapshot of the options available/taken
# as well as print out the timeslots it's checking so that we can verify it worked correctly
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Justin\Desktop\Devin_Booker\screenshot\image1.png')

# TODO # 
# Determine which are the optimal timeslots. Perhaps we can find the unbooked
# timeslots (all the divs that are unbooked have a certain className) and then
# we can have a list maybe that's the order of all timeslots from most to
# least optimal. Then we just try in order and see if that number is the set of
# available, unbooked timeslots

# Need to be careful about accidentally running the program many times and booking all
# the timeslots -> just fix with some sort of boolean


# Probably just don't touch this or if so make sure to remove from cart before window closes
# seems like it could be an issue
'''
# Click Optimal Timeslot
booking_grid = driver.find_element(By.ID, "dcs-booking-grid")
timeslots = booking_grid.find_elements(By.CSS_SELECTOR, "div[role='button']")
timeslots[4].click()
print('confirmed')
time.sleep(100)

print('Confirmed')

# DO NOT TOUCH UNTIL READY TO GO

# try catch the "we changed your membership" -> Actually I think basketball will never have this
#confirm = driver.find_element(By.ID,'modal-ok-button')
#confirm.click()
'''




