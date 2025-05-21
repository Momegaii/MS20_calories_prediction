from models_preds import *
import warnings
warnings.filterwarnings('ignore')

#the 1 Lb difference impact on burning for 1000 step

#lb_diff = 2.2 

#user input style 
"""def mainui():
	pred100 = model.predict()
	usrh = input("Hi, I am MS20(cal-pred) ,I can predict how much burned cals by steps but you need to give me first your height: 6 | 5.6 - 5.11 | 5.5 or less ? ")
	usrwr = input("To give you the accurate cals you burn ,Please choose a range :100Lb to 199Lb |200Lb to 299Lb  |300Lb  ")
	
	if usrh == "6"  and usrwr == "100 -  ":
		usrw = int(input("Thanks,Now please provide me with your weight by LB only pls : only numbers "))
		if usrw - 100 != 0 :
			print(usrw - 100 + pred100)
			usrst = int(input("Thank you,Now how many steps did you walk ? "))
			
			
	elif usrh == "5.6 - 5.11":
		usrw2 = int(input("Thanks,Now please provide me with your weight by LB only pls : only numbers "))
		if usrw2 >= 100 and usrw > 200 :
			usrst2 = int(input("Thank you,Now how many steps did you walk ? "))		
			
			
	elif usrh == "5.5 or less" or "5.5orless":
		usrw3 = int(input("Thanks,Now please provide me with your weight by LB only pls : only numbers "))
		if usrw3 >= 100 and usrw > 200 :
			usrst3 = int(input("Thank you,Now how many steps did you walk ? "))"""
			
def onehundred():
	
	inx = int(input("steps "))
	stcal = inx * 0.027542  # this is the value of burning by 1 step for the 100 - 199lb 6 height bcs if 275 is the 10000step so the 1step is 0.027542 or 90% near it 
	lbcal = 2.75 # and this is the value of the first col of the 100lb so the 200 lb is **2
	
	x100 =  [[inx]]
	
	pred100 = model.predict(x100)
	
	
	print(f"Your estimated burning range of cals will be : {pred100[0]} to {pred100[0] + stcal - 5 }")
	w100 = int(input("so lets get it more specifice give me your actual weight in LB only numbers please : "))
	w100ps = w100 - 100
	 
	if w100ps != 0 :
		optfx =  w100ps * lbcal * (inx * 0.01 * 3 )  + pred100[0]
		print(f"\nYour calculated burned cals in specifice step is : {optfx * 0.01 * 1.7  * 0.5 * 0.1 + pred100[0] * 0.5 + pred100[0] - pred100[0] * 0.1 + 2 }\n")	
	else: 
		print(f"\nYour burned cal is {pred100[0]}\n")
		
		
def twohundred():
		
	inx = int(input("steps "))
	stcal = inx * 0.027542  # this is the value of burning by 1 step for the 100 - 199lb 6 height bcs if 275 is the 10000step so the 1step is 0.027542 or 90% near it 
	lbcal = 2.75 # and this is the value of the first col of the 100lb so the 200 lb is **2
	
	x100 =  [[inx]]
	
	pred100 = model2.predict(x100)
	
	
	print(f"Your estimated burning range of cals will be : {pred100[0]} to {pred100[0] + stcal - 5 }")
	w100 = int(input("so lets get it more specifice give me your actual weight in LB only numbers please : "))
	w100ps = w100 - 200
	 
	if w100ps != 0 :
		optfx =  w100ps * lbcal * (inx * 0.01 * 3 )  + pred100[0]
		print(f"\nYour calculated burned cals in specifice step is : {optfx * 0.01 * 1.7  * 0.5 * 0.1 + pred100[0] * 0.5 + pred100[0] - pred100[0] * 0.1 + 2  }\n")	
	else: 
		print(f"\nYour burned cal is {pred100[0]}\n")
		
def threehundred():
	inx = int(input("steps "))
	stcal = inx * 0.027542  # this is the value of burning by 1 step for the 100 - 199lb 6 height bcs if 275 is the 10000step so the 1step is 0.027542 or 90% near it 
	lbcal = 2.75 # and this is the value of the first col of the 100lb so the 200 lb is **2
	
	x100 =  [[inx]]
	
	pred100 = model3.predict(x100)
	
	
	print(f"Your estimated burning range of cals will be : {pred100[0]} to {pred100[0] + stcal - 5 }")
	w100 = int(input("so lets get it more specifice give me your actual weight in LB only numbers please : "))
	w100ps = w100 - 300
	 
	if w100ps != 0 :
		optfx =  w100ps * lbcal * (inx * 0.01 * 3 )  + pred100[0]
		print(f"\nYour calculated burned cals in specifice step is : {optfx * 0.01 * 1.7  * 0.5 * 0.1 + pred100[0] * 0.5 + pred100[0] - pred100[0] * 0.1 + 2 + 30 }\n")	
	else: 
		print(f"\nYour burned cal is {pred100[0]}\n")



def mainui():
	usrwr1 = input("your weight range is from 100 - 199 : Yes | no ")
	if usrwr1 ==  "yes":
		onehundred()
	elif usrwr1 == "no":
		usrwr2 = input("your weight range is from 200 - 299 : Yes | no ")
		if usrwr2 == "yes":
			twohundred()
		elif usrwr2 == "no":
			usrwr3 = input("so you are 300 and more ?  ")
			if usrwr3 == "yes": 
				threehundred()
			else:
				print("sry i cant help if you dont give me a range.")
			
mainui()
