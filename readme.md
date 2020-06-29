# Facebook Messenger Business Script
<img align="left" width="30" alt="facebook logo" src="http://www.vectorico.com/download/social_media/Facebook-Logo.jpg"> 

## Table of contents
* [The issue at hand](#the-issue-at-hand)
* [General info](#general-info)
* [How to run it?](#how-to-run-it)
* [Status](#status)
* [Time Complexity](#time-complexity)
* [Contact](#contact)

## The issue at hand
When using facebook for business purposes on other platforms like Hubspot and Drift, once a conversation is marked as 
completed it is not synchronized with facebook business messenger. Thus this script aims to solve that by checking the
most recent message and compared that to a certain message flag. If the two sentences are equal or contains a certain 
text then the script will mark the conversation as done


## General info
This script is written using Selenium, through the python programming language.


## How to run it?
1. Make sure you have the [chromedriver](https://chromedriver.chromium.org) installed in in the right directory: 
```./drivers```
2. Make sure you have selenium and python3 installed
3. Run the program through the terminal not IDE due to design choices for inputting the user password
4. You will be prompted with an email, followed by a password and finally the flag message to mark a conversation is 
deleted


## Status
Script is: **Completed**


## Time Complexity
Time complexity: ```O(n)```

Space complexity: ```O(n)```

*where n is the number of contacts in the list to be marked as completed


## Contact
Don't hesitate to ask me whatever you want. Feel free to reach me on my [LinkedIn](https://www.linkedin.com/in/mahirhiro/)
