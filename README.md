# Data-Entry-Automation
<p>Example application to showcase Data Entry Job automation capability using Python.<br>
It automate the action of searching for rental real estate date in zillow and saving this data to a form/ sheet. 
</p>
<br>
<h2><u>How Does it Work ?</u></h2>
<p>The application scrape rental real estate data from zillow's website (Addresses, Prices and URLs) using Python's <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup</a> Library.<br>
The application then loop on the retrieved data and starts adding them to a google form using <a href="https://www.selenium.dev/documentation/" target="_blank">Selenium</a> for interaction with the browser.
</p>
<br>

<h2><u>Run</u></h3>
 <p>Before running the program You first need to:<br>
 <ul><li>Download the chrome webdriver from <a href="https://chromedriver.chromium.org/downloads">Chromium</a> and change the "chrome_driver_path" variable to point at the driver path.</li>
 <li>Change the "google_form_url" to point at your google form URL.</li>
 <li>Change the "driver.findelement" function to point at each form element xpath</li>
 <li>Optimally you will need the program to run automatically in a desired time interval (Daily, Weekly, Monthly...etc) to do the check.<br>
 So you can either upload the program to a python hosting service like <a href="https://www.pythonanywhere.com/" target="_blank">PythonAnywhere</a> and set a scheduler to run to your liking,<br>Or you can generate an exe file using <a href="https://pyinstaller.org/en/stable/" target="_blank">Pyinstaller</a> and setup a windows task scheduler to run it at the selected intervals or at will.</li>
 </ul></p>
 
 
<br>

<h2><u>Libraries Used</u></h3>
<ul>
<li>The URL/ API calls is done using Python's <a href="https://requests.readthedocs.io/en/latest/" target="_blank">Requests</a> Library</li>
<li>The web scrapping is done using Python's <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup</a> Library</li>
<li>The user interaction emulation with the browser is done using Python's <a href="https://www.selenium.dev/documentation/" target="_blank">Selenium</a> Library</li>
</ul>

