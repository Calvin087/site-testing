- [Enviroment Setup](#enviroment-setup)
  - [Virtual Environment](#virtual-environment)
  - [Dependencies](#dependencies)
- [Features To Test + Diary](#features-to-test--diary)
  - [Diary & Ideas - 2020-10-23 15:45:08](#diary--ideas---2020-10-23-154508)
  - [Eat The Frog - 2020-10-23 17:45:06](#eat-the-frog---2020-10-23-174506)
  - [Frog Eaten - 2020-10-24 14:37:27](#frog-eaten---2020-10-24-143727)

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

- Should be able to create a new account
  - Probably need a way to fill out the new user form?
    - Would need a dictionary maybe to store data to fill
    - Might need a random UUID type mod to create fake emails while testing.
  - Check that page refreshes or alert shows up with confirmation to assert?

- Should be able to log in with credentials.
  - Manually create an account and save those creds?
  - Or use the one that was just made?

- Error message should be displayed to user, if they're creds aren't valid
  - Manually save fake email and wrong password to send to **sign in** form 

</br>

**Cart Features**
- Search for an item AND add to cart
- Cart should be updated with previously added item
- Cart updated with Correct Values and Correct Items / Totals

</br>

**Order Features**
- Shold be able to create a new order with items in cart
- "My Account" -> "Order History" should be updated with new orders.

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