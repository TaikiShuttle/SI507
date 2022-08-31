"""
Lab 1 - Individual/Group Exercise
"""

"""
1. Write a function named CelsiusToFarenheit
   your function should ask the user for a temperature in celsius
   your function should convert the temperature to farenheit
   your function should print the Farenheit Temperature (no return statement)
   The formula for conversion is (°C × 9/5) + 32 = °F
   Check your answer 0°C should be 32°F and 100°C should be 212°F
"""
def CelsiusToFarenheit():
   celsius_temp = int(input("What is the temperature in Celsius?\n"))
   farenheit_temp = int(celsius_temp*9/5 +32)
   print("The farenheit_temp is: ", farenheit_temp, "°F.")
   return
   # it seems that lots of people use print with fstring(f'{temp} degree C is equal to {fahrenheit} degrees Fahrenheit').
   # Use try/except pair so that we can catch bad input. We should always consider this
   # Do it like:
   # while True:
   #    try:
   #       ...
   #       break
   #    expect:
   #       ...


# Extra Practice / Resources

# 2. Write a function named MarketingCampaign.
#    your function should accept the following parameters:
#        DigitalAds - an integer representing the budget for buying internet ads
#        TVAds - an integer representing the budget for buying television ads
#        PrintAds - an integer representing the budget for buying newspaper ads

#    Calculation: Assume that at your company a single marketing campaign consists of
#             7 digital ads (cost: 1 unit per ad = 7 units)
#             3 television ads (cost: 1 unit per ad = 3 units)
#             6 print ads. (cost: 1 unit per ad = 6 units)
#             and that ads of all types cost 1 unit.

#     Return Value:
#        An integer representing the number of full marketing campaigns you can run
def MarketingCampaign(DigitalAds, TVAds, PrintAds):
   # calculate the maximum campaign that can be applied conditioned by different campaign options
   max_DigitalAds = DigitalAds//7
   max_TVAds = TVAds//3
   max_PrintAds = PrintAds//6
   return min(max_DigitalAds, max_TVAds, max_PrintAds)


#    Hint: There is a built-in python function called min() that may be useful
#    Hint2: You can solve this without conditionals.
#    Self-check your function if you have budget of 400 for digital, 22 for TV and 125 for print your output should be 7

# 2B. Make a second function that also asks the user to input the current prices for the three
# types of ads before calculating the number of marketing campaigns that can be run at the new
# prices.

# NOTE: a single marketing campaign still consists of:
#     7 digital ads (cost per add to be input by user)
#     3 television ads (cost per add to be input by user)
#     6 print ads (cost per add to be input by user)
def UserDefineMarketCampaign(DigitalAds, TVAds, PrintAds):
   price_string = input("Please enter the price for DigitalAds, TVAds, PrintAds, seperated by blank spaces.\n")
   price_str_list = price_string.split(" ")
   prices = [int(price) for price in price_str_list]
   # Then we are able to deal with the number of campaigns
   max_DigitalAds = DigitalAds//(prices[0] * 7)
   max_TVAds = TVAds//(prices[1] * 3)
   max_PrintAds = PrintAds//(prices[2] * 6)
   return min(max_DigitalAds, max_TVAds, max_PrintAds)




# For extra practice (later) you can read through the following:
# 3. Read and work through examples in Chapter 4 Code Reuse: Functions & Modules in Head First Python:
# https://www.oreilly.com/library/view/head-first-python/9781491919521/ch04.html
# you can access for free as a UM student.
# See the U-M Library instructions https://search.lib.umich.edu/databases/record/10263
# or visit https://www.safaribooksonline.com/library/view/temporary-access/
# and log in with your U-M email address.


if __name__ == "__main__":
   # CelsiusToFarenheit()
   # num_campaign = MarketingCampaign(400,22,125)
   # print(num_campaign)
   num_campaign = UserDefineMarketCampaign(400,22,125)
   print(num_campaign)
   