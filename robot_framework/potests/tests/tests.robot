*** Settings ***
Documentation    Tests for ecommerce website
Library        SeleniumLibrary
Library        ../customLibraries/AddProduct.py
Test Setup         generic.Open Browser At Main Page
Test Teardown      Close Browser
Resource    ../pageobjects/MainPage.robot
Resource    ../pageobjects/Generic.robot
Resource    ../pageobjects/ProductsPage.robot
Resource    ../pageobjects/ProductDetail.robot
Resource    ../pageobjects/CheckoutPage.robot



*** Variables ***
${product}        Proteus Fitness Jackshirt


*** Test Cases ***
Check If Website Is Rejecting Invalid Email
    MainPage.Fill The Email And Click Subscribe

Adding Product To Cart
    Generic.Go To Products Page
    AddProduct.Add Items To Cart    ${product}


Adding Product To Cart And Checkout
    Generic.Go To Products Page
    AddProduct.Add Items To Cart    ${product}
    ProductDetail.Proceed To Checkout
    CheckoutPage.Added Product Should Be In Checkout Page    ${product}

    