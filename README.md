# replicant_hw_pytest
Dear Replicant Team! 

This WAS FUN ! I thank you for that. 
Please review allure screenshots as well . 

To execute pytest and generate files required for allure report use 

use --alluredir flag to create pytest reports for allure 

"pytest -v --alluredir=/home/iidwuurliik/Desktop/py_dev/replicant/report" <---change home folder 

To execute only positive tests use 
pytest -v -m "positive" 

To execute only sms bot tests use 
pytest -v -m "sms" 

To spin up allure local server use 
allure serve {YOURHOME/pytest/report}
