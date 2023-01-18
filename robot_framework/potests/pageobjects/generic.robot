*** Settings ***
Documentation        Resource file for generic keywords and variables
Library        SeleniumLibrary


*** Variables ***
${BROWSER}        chrome
${URL}            https://magento.softwaretestingboard.com/
${MEN_NAVBAR}     //span[normalize-space()='Men']
${TOPS_NAVBAR}    //a[@id='ui-id-17']//span[contains(text(),'Tops')]
${JACKET_NAVBAR}  //a[@id='ui-id-19']//span[contains(text(),'Jackets')]

*** Keywords ***
Open Browser At Main Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    # Set Screenshot Directory    screenshots

Go To Products Page
    Sleep  2
    Mouse Over    ${MEN_NAVBAR}
    Mouse Over    ${TOPS_NAVBAR}
    Click Element  ${JACKET_NAVBAR}
    Sleep  2
