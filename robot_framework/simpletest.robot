*** Settings ***
Library          SeleniumLibrary

*** Variables ***
${BROWSER}          chrome
${URL}              http://the-internet.herokuapp.com/
${AB_TESTING}       //a[normalize-space()='A/B Testing']
${LOGIN_PAGE}       //a[normalize-space()='Form Authentication']
${USERNAME_INPUT}   //input[@id='username']
${PASSWORD_INPUT}   //input[@id='password']
${LOGIN_BUTTON}     //i[@class='fa fa-2x fa-sign-in']
${LOGOUT_BUTTON}    //i[@class='icon-2x icon-signout']


*** Test Cases ***
AB Testing page is loading properly test
    [Setup]       Open Website
    Check If Page Is Loaded
    Go to A/B Testing
    Page Should Contain    A/B Test Control
    [Teardown]    Close Browser

Login Testing
    [Setup]       Open Website
    Check If Page Is Loaded
    Go To Login Page
    Input Text    ${USERNAME_INPUT}    matt
    Input Text    ${PASSWORD_INPUT}    matt1
    Click Login Button
    Page Should Contain    Your username is invalid!
    Clear Element Text    ${USERNAME_INPUT}
    Clear Element Text    ${PASSWORD_INPUT}
    Input Text    ${USERNAME_INPUT}    tomsmith
    Input Text    ${PASSWORD_INPUT}    matt1
    Click Login Button
    Page Should Contain    Your password is invalid!
    Input Text    ${USERNAME_INPUT}    tomsmith
    Input Text    ${PASSWORD_INPUT}    SuperSecretPassword!
    Click Login Button
    Page Should Contain    You logged into a secure area!
    Click Logout Button
    Page Should Contain    You logged out of the secure area!
    [Teardown]    Close Browser

*** Keywords ***
Open Website
    Open Browser  ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Screenshot Directory    screenshots
Check If Page Is Loaded
    Page Should Contain    Welcome to the-internet

Go to A/B Testing
    Click Element  ${AB_TESTING}

Go To Login Page
    Click Element  ${LOGIN_PAGE}

Click Login Button
    Click Element  ${LOGIN_BUTTON}

Click Logout Button
    Click Element  ${LOGOUT_BUTTON}