# Facebook-Spammer
Script that can comment on any number of posts of a Facebook page or profile.

This simple utility was developed out of the sheer frustration I had with the services provided by Airtel, like poor network coverage, call drops and low data speed. Since companies are now quite active on social media, it might prove useful for handling non-cooperative customer care services. You can also use it to spam your friend's profile, just for fun.

## Working

- Install the dependencies using pip install requirements.txt
- Download chromedriver.exe and copy its path in line 29 of Facebook Spammer.py. 
- The script takes following 5 inputs.
1. **emal_id :** Your Facebook Email ID.
2. **password :** Your Facebook password. (Don't worry. Your login credentials are safe.)
3. **page_link :** The page or profile link you want to spam. Eg. https://www.facebook.com/praneetk2704 or https://www.facebook.com/AirtelIndia
4. **number_of_times :** The number of posts you want to spam. For eg. if number_of_times = 150, the script will spam the most recent 150 posts by the page or user.
5. **frequency :** The number of times you want to spam each post. For example, if frequency = 3, then the script will spam thrice on each post. Do note that both number_of_times and frequency take integer arguments, so do not enclose them within single or double quotes.
6. **message :** The contents of your message which you want to spam.
- That's it. Run the script now. Happy spamming. :)

Here is a short demo video of the script in which I spammed Airtel's official Facebook page for 100 posts, twice on each post (a total of 200 times). 
