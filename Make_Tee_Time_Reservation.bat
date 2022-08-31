@ECHO OFF
ECHO -- Tee Time Scheduler --
CALL C:\Users\jhkon\Desktop\Dev\python_projects\TeeTime_bot\botenv\Scripts\activate.bat
cd /d C:\Users\jhkon\Desktop\Dev\python_projects\TeeTime_bot
robot --outputdir output -P C:\Users\jhkon\Desktop\Dev\python_projects\TeeTime_bot -P C:\Users\jhkon\Desktop\Dev\python_projects\TeeTime_bot\src tee_time.robot 
PAUSE