#Structure in python to store information in key value pairs
#value can be a number string, list, tuple, or another dictionary
#immutable
#curly braces to define a dictionary

#Word would be the key and the value is the definition

#converting three short abbreviated month to actual full month name

#inside use key ,value pairs

#Vefore the colon is the key, and thet y have to be unique... can't duplicate
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}
## can also be numbers for the dictionaries' keys


#print(monthConversions)
#access dictionary by name

# can access the keys and values with []
#print(monthConversions["Nov"])

#can access using .get
#Can specify a default value in case it is not found which is none or whatever elese you put if not found
#used in a lot of cases
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not found"))