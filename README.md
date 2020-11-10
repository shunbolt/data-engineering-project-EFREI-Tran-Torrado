# Data engineering project
### By Raphaël Tran & Yoann Torrado

### Requirements :
- Docker 
- docker-compose
- Selenium library to run the tests on your machine : `pip install selenium`

### Installation :
- `git clone https://github.com/shunbolt/data-engineering-project-EFREI-Tran-Torrado.git`
- `cd data-engineering-project-EFREI-Tran-Torrado`

### Starting the app
`./run_and_test.sh` or `docker-compose up`

You can then access the webapp on http://localhost:5000. 

### Running tests
`python test_webapp.py`

If you have an issue regarding Geckodriver, you can follows these steps on a Unix/Ubuntu machine :

1. Download Geckodriver :

`wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`

2. Extract it :

`tar -xvzf geckodriver*`

3. Give execution permissions :

`chmod +x geckodriver`

4. Move it to binaries directory :

`sudo mv geckodriver /usr/local/bin/`
