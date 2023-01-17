*** Settings ***
Documentation        Resources for Product Detail page
Library        SeleniumLibrary


*** Variables ***
${SHOPPING_CART}          //a[@class='action showcart']
${PROCEED_TO_CHECKOUT}    //button[@id='top-cart-btn-checkout']

*** Keywords ***
Proceed To Checkout
    Click Element    ${SHOPPING_CART}
    Click Element    ${PROCEED_TO_CHECKOUT}
