<!-- note to self> 
- update interpreter in vscode to venv.
- cd into project root on vscode
<!-->

- [Enviroment Setup](#enviroment-setup)
  - [Virtual Environment](#virtual-environment)
  - [Dependencies](#dependencies)
- [Features To Test + Diary](#features-to-test--diary)
  - [Diary & Ideas - 2020-10-23 15:45:08](#diary--ideas---2020-10-23-154508)
  - [Eat The Frog - 2020-10-23 17:45:06](#eat-the-frog---2020-10-23-174506)
  - [Frog Eaten - 2020-10-24 14:37:27](#frog-eaten---2020-10-24-143727)
  - [Wasted Time - 2020-10-25 11:42:51](#wasted-time---2020-10-25-114251)
  - [DONE - Account creation form - 2020-10-25 14:59:29](#done---account-creation-form---2020-10-25-145929)
  - [DONE - Adding Items To Cart - 2020-10-25 20:20:04](#done---adding-items-to-cart---2020-10-25-202004)
  - [DONE - Placing an order - 2020-10-26 07:43:10](#done---placing-an-order---2020-10-26-074310)

</br>

# Enviroment Setup

</br>

## Virtual Environment

```
virtualenv venv --python=python3.9
```
```
source venv/bin/activate
```
```
pip list
```
Check that this is pretty much empty. I keep making the mistake of not activating my Venv but only realise when I see millions of modules in this list.

</br>

## Dependencies

```
pip3 install selenium
```

</br>

# Features To Test + Diary

## Diary & Ideas - 2020-10-23 15:45:08

</br>

**What actually needs to be done?**
No idea how to do this with UnitTest alone, so I'm probably going to use Selenium based off of a course I went through this week. Seems like a pretty straight forward way to get it done for a beginner.

The plan is to get this done without asking for help, but when / **if** I complete this, I'll deff ask for some feedback on the ideas that I've made work.

</br>

**Features To Test**

**Log in Features**

- Should be able to create a new account **DONE**
  - Probably need a way to fill out the new user form?
    - Would need a dictionary maybe to store data to fill
    - Might need a random UUID type mod to create fake emails while testing.
  - Check that page refreshes or alert shows up with confirmation to assert? 

- Should be able to log in with credentials. **DONE**
  - Manually create an account and save those creds?
  - Or use the one that was just made?

- Error message should be displayed to user, if they're creds aren't valid **DONE**
  - Manually save fake email and wrong password to send to **sign in** form 

</br>

**Cart Features**
- Search for an item AND add to cart **DONE**
- Cart should be updated with previously added item **DONE**
- Cart updated with Correct Values and Correct Items / Totals **DONE**

</br>

**Order Features**
- Shold be able to create a new order with items in cart
  - log in, add one item, and click away
- "My Account" -> "Order History" should be updated with new orders.
  - assert order number on orders page. 

</br>

## Eat The Frog - 2020-10-23 17:45:06

</br>

Honestly I think the most difficult part of this for me is going to be locating the css selectors. The website in question doesn't seem to have a single ID. They're all going to have to be ambiguous xpath selectors.

I'll probably need to create locators and save all the selectors that I THINK I'll need. Then move on to writing the base pages and base elements.

On another note I think that checking the cart quantities will be easier if I click on the cart and check the cart PAGE, not the dynamic mini at the top of the screen.

The payment method will have to be looked into as well. Maybe I can create some fake creds and see if it goes through.

I also think I might be easier to add items to the cart from the product page, that is if I can't figure out how to do it from the search page.

</br>

## Frog Eaten - 2020-10-24 14:37:27

</br>

So I think I have all of the selectors that I'll need now. I'll probably test the longest one first which will be the form. I'm not sure if there is a quick way to do it, so more research is required.

Now that I have all of the (What i think are) the selectors in a list with titles and general ideas of flow, I should be able to just copy and paste the findby functions and slap in the selector xpaths ONCE which will save time.

</br>

## Wasted Time - 2020-10-25 11:42:51

</br>

Couldn't figure out why none of my files were connecting to each other when they clearly linked to one another. Turns out in my test file, I forget to actually CREATE the object which kicked off the whole chain reaction of property usage.

Usual idiot mistake.

Let's Go

**2020-10-25 12:05:45** TIMEOUT ERROR - Radio buttons take ages to load so had to adjust wait timings

**2020-10-25 14:17:03** DROP DOWNS ARE HORRIBLE! 2 hours to figure out how to select a value. Nothing was working. So i had to select by xpath the exact option in the list. Now it works.

</br>

## DONE - Account creation form - 2020-10-25 14:59:29

</br>

So far just to achieve this, we're looking at 6 hours today DAMN!
An hour yesterday gathering xpaths and ID's
An hour just contemplating how to start on Friday

So we're at about 8 hours....too slow

</br>

## DONE - Adding Items To Cart - 2020-10-25 20:20:04

</br>

At around 11 hours - Took a two hour break. Things are getting a little messy, not sure how to organise these files that test across the entire site. System tests / integration tests?

It's getting a bit confusing but things are working. Able to add items to cart, check if they were added ...in two ways, check price of item when buying it and make sure that the price is correct on the file cart page.

</br>

## DONE - Placing an order - 2020-10-26 07:43:10

</br>

Roughly 13 hours to finish all the system tests. We can now check that an order has been placed, visit the order page and assert that the most recent order number appears on the page. Had to slice up to confirmation message and extract the order number, save as a variable and assert on it at the end.

It's rough, but for a first website test. I'm quite happy. Definately pushed me to do something I wasn't confident about.