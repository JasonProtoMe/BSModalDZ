# BSModalDZ
Simple integration example of Bootstrap Modal & Dronzone.js.
Open modal, click and drop file(s), and see it uploaded (upon success) in your Django project's media file.
My purpose of this very simple, but functional project was because I had spent an unnecessary amount of time trying to
troubleshoot and get it working under the Dropzone/Bootstrap/Django framework and I wanted to make the day of people
who also wanted to integrated this way simple. 

### Installation
This project uses the following systems and libraries:
- Django
- jQuery
- Bootstrap
- Crispy Forms

Please make sure you have those downloaded and for available use (through pip)

### Usage
Currently, the project shows successful integration between Dropzone.JS inside a Boostrap Modal with transfer of files in a Django backend. Any and all code can be used for your own purpose :) Additional functionalities will be added in future; check Backlog for more information.

To mimic usage of this exact project:
1. Type in py manage.py runserver locally on your terminal
2. Open your preferred browser and navigate to: 127.0.0.1:8000/ModalDZ to access the app's webpage

3. Click the 'Open Modal' button, drop file(s) onto the Dropzone area
4. Press 'Next' and fill in the form areas of First Name and Last Name to be considered a valid form
5. Press submit and see the file transfer onto your media file

For modifications to your own page, make sure you change the url that Dropzone is transferring the files to.

### Backlog
- Success/error messages
- Taking requests :)

### License & Copyright
I've simply compiled and integrated Django, Bootstrap, and Dropzone. Sectional rights go to them respectfully.
- Django: https://www.djangoproject.com/
- Bootstrap: https://getbootstrap.com/docs/4.0/components/modal/
- Dropzone: https://www.dropzonejs.com/#usage

**bold**
_italic_
`code`
