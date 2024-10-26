# Program to check tenders in state database
#### Video Demo:  https://youtu.be/wTWspa7saJE
#### Description:
In Poland, public entities are obliged to issue a tender to gather bids and select the best one. Each type of service/commodity has its own CPV code. All tenders can be found in a government database. It is possible to access database by using government searching engine, however, it is not the most comfortable and fast way. If you do this every day (like I do) it takes some time to fill up every box needed to run searching. Hopefully, there’s possibility to access database using API to request specific data you are interested in. There are a few private sites which provides you with better searching engine and features like alerts but they are mostly paid. That's why I made a program to check database more easily and for free.
To search in database using API it is needed to format a link. Link need to contains various information to specify a criteria and narrow down searching. Based on this link gov site return information in text format.
The sake of program was to make searching quick and simple – that is why it takes only 1 argument: CPV code. Based on CPV code and current data it emerges a link, request date, format them and display for user.
Database contains not only information of announcements of tender but also information of result (who won the tender) and report of results. If you are not interested in checking correctness of whole process you are only interested in announcement.
Time of publication in program is formatted based on system time on user computer to display current date. Regardless of time to applicate (usually 2 weeks) I left on purpose only 7 days window because in practice you need 7 or more days to fill all requirements, so for most of cases it's impossible to applicate for tender older than 7 days.
Program have graphical user interface for simpler and user-friendly look.
Searching engine is run by pressing the “Search” button or by ENTER key.
Results are display in popout window. If user entered CPV code is incorrect program will check it and display the error message in popout window. If database is unreachable program will return a Timeout error and display relevant message.
#### Hope you enjoy it and find it helpful. 😊

