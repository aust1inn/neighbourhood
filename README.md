# neighbourhood
Neighborhood Watch: You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it. This web application allows you to be in the loop about everything happening in your neighborhood.

**Users must log in with credible emails**

## User Stories
These are the behaviors/features that the application implements for use by a user.

Users would like to:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete hoods,posts,businesses
* Delete hoods,posts,businesses
* Manage the application.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Admin Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| Display all hoods,posts,businesses | **Home page** | Clickable links to open live hoods,posts,businesses in different sites |
| To add an hoods,posts,businesses  | **Admin/Users** | Click on add and upload respectively|
| To edit hoods,posts,businesses  | **Admin/Users** | Redirected to the  hoods,posts,businesses form details and editing happens|
| To delete an hoods,posts,businesses  | **Admin/Users** | click on hoods,posts,businesses object and confirm by delete button|
| To search hoods by id | **Enter text in search bar** | Users can search by Hoods by ID|
| View posts by neighbours | **Add posts** | Users can add posts to hoods they join|

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/aust1inn/neighborhood
        $ cd neighborhood

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test

## Technologies Used
* Python3.8
* Django  framework and postgresql database

## Known Bugs

* Occupants/resident count

## License

Copyright (c) 2022 aust1inn

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
