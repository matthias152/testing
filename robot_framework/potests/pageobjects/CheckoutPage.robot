*** Settings ***
Documentation        Resources for Checkout Page
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***
Added Product Should Be In Checkout Page
    [Arguments]    ${product}
    Page Should Contain    ${product}