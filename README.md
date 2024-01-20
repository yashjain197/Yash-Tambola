# Yash-Tambola Project

## Introduction

Welcome to the Yash-Tambola project! This Django-based application brings the classic Tambola (also known as Bingo or Housie) game into the digital realm, offering an exciting and interactive experience. Follow the steps below to set up and run the project on your local machine.

## Prerequisites

Before you begin, ensure that you have Python and pip installed on your machine.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Yash-Tambola.git
   
2. Navigate to the project directory:

   ```bash
   cd Yash-Tambola
   
3. Create a virtual environment:

     ```bash
     pip install virtualenv
     virtualenv venv

4. Activate the virtual environment:
   
      ```bash
      For Windows
      .\venv\Scripts\activate

      For Mac/Linux
      source venv/bin/activate
5. Install project dependencies:

      ```bash
      pip3 install -r requirements.txt

6. create the env file and add details accordingly


## Running project

   Once the setup is complete, you can run the Yash-Tambola project using the following command:
   
            python manage.py runserver

   or 
   Try it out on deployed version of it.

      GET: http://3.110.84.198:8000/api/generate-ticket/ #params are page and set_id or room_id
      ex: http://3.110.84.198:8000/api/generate-ticket/?set_id=ff2ac196-cb9f-4060-a7cd-7563d8970097&page=1
      
      POST: http://3.110.84.198:8000/api/generate-ticket/ #form data: no_of_set: 1 or 2 ...
      
   ## Enjoy playing Tambola digitally with Yash-Tambola!
