# DigitalSky2 CTR File Generator
This tool generates *.ctr* files for use in planetarium software DigitalSky2 via JPL Horizons.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```pip install astroquery```.
5. Enter ```python main.py```.

# Usage
This program has one function, *query_horizons*.
To use *query_horizons*, run *main.py* via ```python main.py``` in Terminal.
```Body:``` will print.
Enter the ID of the solar system object (SSO).
After, ```Start time:``` will print.
Enter the time to start recording data on the body's orbit, in format YYYY/MM/DD,HH:MN:SC.
After, ```Stop time:``` will print.
Enter the time to stop recording data on the body's orbit in the same format as ```Start time:```.
After, ```Interval:``` will print.
Enter the time step of the body's orbit, in format INTunit, where INT is an integer, and unit is d, h, m, or s.
After all information on the body is entered, the code will create a *.ctr* file in the repository location.
The name of the file is the body entered, and is ready to be implemented into DigitalSky2.

# Example
Suppose user wants to generate a *.ctr* file for body **2008 TC3**.
Suppose the desired starting time is May 12th, 2006 (**2006/05/12**), at **16:00:00** UTC.
Suppose the desired stopping time is June 16th, 2006 (**2006/06/16**), at **16:00:00** UTC.
Suppose the desired interval is 1 day (**1d**).

Run *main.py* via ```python main.py``` in Terminal.
When ```Body:``` prints, enter ```2008 TC3```.
When ```Start time:``` prints, enter ```2006/05/12,16:00:00```.
When ```Stop time:``` prints, enter ```2006/06/16,16:00:00```.
When ```Interval:``` prints, enter ```1d```.
After ```CTR file generated.``` prints, the *.ctr* file is done generating.

The *.ctr* file is located in the same folder as *main.py*.
The *.ctr* file generated in this example is *2008TC3.ctr*, located in the repository.

# Errors
1. ```Unknown target. Maybe try different id_type?```
Solution: Enter correct SSO id. Body identification tool found at https://ssd.jpl.nasa.gov/tools/sb_ident.html#/.
2. ```Ambiguous target name; provide unique id:```
Solution: See error message for correct SSO id.
3. ```Cannot interpret date. Type "?!" or try YYYY-MMM-DD {HH:MN} format```
Solution: Enter date format YYYY/MM/DD,HH:MN:SC (year/month/day,hour:minute:second).
4. ```No ephemeris for target after```
Solution: Change starting and stopping dates to after the date the error message specifies.
5. ```No ephemeris for target prior to```
Solution: Change starting and stopping dates to before the date the error message specifies.
6. ```Bad dates -- start must be earlier than stop```
Solution: Switch starting and stopping dates.
7. ```Unknown units specification -- re-enter```
Solution: Enter integer (1, 2, etc.).
8. ```Could not convert string to float:```
Solution: Enter units ```d```, ```h```, ```m```, or ```s``` for day, hour, minute, and second, respectively, after integer.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
