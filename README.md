# Site Testing Automation Attempt

- [Table Of Contents]()
    - [Features To Test](#features-to-test)
    - [Diary & Ideas - 2020-10-23 15:45:08](#diary--ideas---2020-10-23-154508)

</br>

### Features To Test
### Diary & Ideas - 2020-10-23 15:45:08

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