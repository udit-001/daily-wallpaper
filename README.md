# Daily-Wallpaper

A python script to update desktop wallpaper on a Windows machine from a tumblr blog.

## Inspiration
I was tired of seeing the same boring Wallpaper on my Desktop everyday. After learning a little bit of Python, I decided to design a script that would update my wallpaper on it's own by fetching an image from a [Tumblr Blog](http://fuckinghomepage.com/).

## Usage
This script can be scheduled to run daily by using they Task Scheduler utility present on Windows. You will require a BAT script to run the script from the task.

```
@echo off 
cd <path to wall.pyw>
pythonw wall.pyw
```

Now copy the above code and paste it into notepad and save it as "dailywall.bat"

If you want your script to work silently in the background without having a command prompt window opening up, then you'll also need to create a .VBS script.

```
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "<path to dailywall.bat>" & Chr(34), 0
Set WshShell = Nothing
```
Copy the above code and save it as "dailywall.vbs".  
Now add the above script in the Windows Task that you'll schedule to run daily.

## Features 
It also displays a notification on your computer when the wallpaper gets updated.

![Notifications Screenshot](https://raw.githubusercontent.com/udit-001/daily-wallpaper/master/img/notification.jpg)



