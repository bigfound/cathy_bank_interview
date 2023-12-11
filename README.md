the sheet 1 of the Auto_Senior_v1.xlsx:
./cathay_bank_interview/sheet1/測試案例心智圖.png

the sheet 2 of the Auto_Senior_v1.xlsx: 
./cathay_bank_interview/sheet2
logic_1.py
logic_2.py
logic_3.py

the sheet 3 of the Auto_Senior_v1.xlsx:  
1. .py file path: ./cathay_bank_interview/sheet3/test_automation_case.py
2. Run test_automation_case.py:
   Step1: pytest --alluredir=./allure-results -v -s test_automation_case.py --junitxml=./log/test_automation_case.xml
   
   Step2: Generate allure report(optional):
          allure generate -c -o allure-reports
   
   step3: Open allure report(optional):
          allure open allure-reports

3. Test log files path:
   ./[Eric]_cathay_bank_test_sheet3/log
   1. <Year-M-D_HH_MM_SS_console.log> the file is the pytest console log
   2. <step1_home_page_screenshot.png> the file is for the test step1 screenshot
   3. <step2_items_in_credit_card_list.png> the file is for the test step2 screenshot
   4. <./credit_cards_nums> the folder is for the test step3 screenshot 
   5. <test_automation_case.xml> the file is junitxml report, it can be used for Jenkins

4. Allure report:
   <./[Eric]_cathay_bank_test_sheet3/allure-reports/> 
    


