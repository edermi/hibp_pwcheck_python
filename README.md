# hibp_pwcheck_python
Small python tool / library for checking passwords against [Have I Been Pwned](https://haveibeenpwned.com/) dataset

Easy to use as a library in your own projects or as simple CLI tool. Just provide a password candidate as first parameter and watch the output.
The script may also be included in other scripts. A zero return code indicates the password was not found, while 1 means that the password has 
been found in breaches. Other return codes indicate wrong usage or errors when querying the HIBP API.

## Disclaimer

[HIBP](https://haveibeenpwned.com/) is a service by Troy Hunt. For further info, check the [HIBP About Section](https://haveibeenpwned.com/About)
