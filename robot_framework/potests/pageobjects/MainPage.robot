*** Settings ***
Documentation        Resource for Main Page keywords and variables
Library        SeleniumLibrary


*** Variables ***
${NEWSLETTER_INPUT}        //input[@id='newsletter']
${NEWSLETTER_SUBSCRIBE_BUTTON}    //span[normalize-space()='Subscribe']
${NEWSLETTER_ERROR}        //div[@id='newsletter-error']


*** Keywords ***
Fill The Email And Click Subscribe
    Input Text    ${NEWSLETTER_INPUT}    invalidemail
    Sleep  2
    Click Element    ${NEWSLETTER_SUBSCRIBE_BUTTON}
    Wait Until Element Is Visible    ${NEWSLETTER_ERROR}
    Page Should Contain    Please enter a valid email address