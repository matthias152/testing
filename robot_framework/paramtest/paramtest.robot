*** Settings ***
Documentation    Validating login form
Library          SeleniumLibrary
Test Setup       Open Website
Test Teardown    Close Browser
Test Template    Validate unsuccesful login

*** Variables ***
${BROWSER}          chrome
${URL}              http://the-internet.herokuapp.com/
${LOGIN_PAGE}       //a[normalize-space()='Form Authentication']
${USERNAME_INPUT}   //input[@id='username']
${PASSWORD_INPUT}   //input[@id='password']
${LOGIN_BUTTON}     //i[@class='fa fa-2x fa-sign-in']
${ERROR_MSG}        css:.flash


*** Test Cases ***    username    password
Invalid username        matt          learning
Invalid username        matt3         ploudfg
Invalid username        matt7         learning

*** Keywords ***
Validate unsuccesful login
    [Arguments]        ${username}        ${password}
    Check If Page Is Loaded
    Go To Login Page
    Fill The Login Form        ${username}        ${password}
    Verify flash error message

Fill The Login Form
    [Arguments]        ${username}        ${password}
    Input Text       ${USERNAME_INPUT}    ${username}    
    Input Text       ${PASSWORD_INPUT}    ${password}
    Click Element    ${LOGIN_BUTTON}

Open Website
    Open Browser  ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Screenshot Directory    screenshots

Check If Page Is Loaded
    Page Should Contain    Welcome to the-internet

Go To Login Page
    Click Element  ${LOGIN_PAGE}

Verify flash error message
    Element Should Contain    ${ERROR_MSG}    Your username is invalid!


