*** Settings ***
Documentation    Tests for ecommerce website
Library        SeleniumLibrary
Library        ../customLibraries/AddProduct.py
Test Setup         generic.Open Browser At Main Page
Test Teardown      Close Browser
Resource    ../pageobjects/MainPage.robot
Resource    ../pageobjects/generic.robot
Resource    ../pageobjects/ProductsPage.robot
Resource    ../pageobjects/ProductDetail.robot
Resource    ../pageobjects/CheckoutPage.robot



*** Variables ***
${product}        Proteus Fitness Jackshirt


*** Test Cases ***
Check If Website Is Rejecting Invalid Email
    MainPage.Fill The Email And Click Subscribe

Adding Product To Cart
    Go To Products Page
    Add Items To Cart    ${product}


Adding Product To Cart And Checkout
    Go To Products Page
    Add Items To Cart    ${product}
    Proceed To Checkout
    Added Product Should Be In Checkout Page    dsadsa
    Sleep  10


    