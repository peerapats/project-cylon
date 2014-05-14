# -*- coding: utf-8 -*-
from behave import *
from project_cylon.WorldContext import *

#
# Given step definitions
#
@given ("User has [{PageName}] page open") #prefered
@given ("User has [{PageName}] open")
def step(context, PageName):
    Page = World.FindPage(PageName)
    Page.Go()

#
# When step definitions
#
@when ("User enters '{Value}' to the [{ElementName}]") #prefered
@when ("User enters '{Value}' to [{ElementName}]")
def step(context, ElementName, Value):
    #Element = World.CurrentPage.FindElement(ElementName)
    Element = World.FindElement(ElementName)
    Element.SendKeys(Value)

@when ("User enters date '{Value}' to the [{ElementName}]") #prefered
@when ("User enters date '{Value}' to [{ElementName}]")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeysByScript(Value)


@when ("User clears value on the [{ElementName}]") #prefered
@when ("User clears input [{ElementName}]")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeysByScript("")


@when ("User selects the [{ElementName}]") #prefered
@when ("User clicks the [{ElementName}]") #prefered
@when ("User clicks [{ElementName}] link")
@when ("User clicks [{ElementName}] button")
def step(context, ElementName):
    #Element = World.CurrentPage.FindElement(ElementName)
    Element = World.FindElement(ElementName)
    Element.Click()


@when ("User selects '{Value}' on the [{ElementName}]") #prefered
@when ("User selects '{Value}' in [{ElementName}]")
def step(context, Value, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.Select(Value)


#@when ("User selects the [{RadioOption}]")
@when ("User checks the [{ElementName}]")
def step(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Check()


@when ("User unchecks the [{ElementName}]")
def step(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Uncheck()


@when ("User moves mouse over the [{ElementName}]") #prefered
@when ("User moves mouse over [{ElementName}]")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.MouseOver()


@when ("User uploads file '{FilePath}' to the [{ElementName}]") #prefered
@when ("User uploads file '{FilePath}' to [{ElementName}]")
def step(context, FilePath, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeys(FilePath)


@when ("User enters '{Value}' to the popup") #prefered
def step(context, Value):
    World.SendKeysToPopup(Value)


@when ('User clicks "OK" on the popup') #prefered
def step(context):
    World.AcceptPopup()


@when ('User clicks "Cancel" on the popup') #prefered
def step(context):
    World.DismissPopup()

#
# Then step definitions
#
@then ("The browser shows [{PageName}] page") #prefered
@given ("The system displays [{PageName}]")
@then ("The system displays [{PageName}]")
def step(context, PageName):
    Page = World.FindPage(PageName)
    Page.VerifyPage()


@then ("The page url is '{URL}'") #prefered
@given ("The system displays '{URL}'")
@then ("The system displays '{URL}'")
@given ("The system URL is '{URL}'")
@then ("The system URL is '{URL}'")
def step(context, URL):
    World.VerifyURLIs(URL)


@then ("The page url contains '{URL}'") #prefered
@given ("The system URL contains '{URL}'")
@then ("The system URL contains '{URL}'")
def step(context, URL):
    World.VerifyURLContains(URL)


@given ("The [{ElementName}] value is '{Value}'") #prefered
@then ("The [{ElementName}] value is '{Value}'") #prefered
@given ("The [{ElementName}] shows '{Value}'")
@then ("The [{ElementName}] shows '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueIs(Value)


@then ("The [{ElementName}] value is not '{Value}'") #prefered
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIsNot(Value)


@then ("The [{ElementName}] value contains '{Value}'") #prefered
@given ("The [{ElementName}] contains '{Value}'")
@then ("The [{ElementName}] contains '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueContains(Value)


@then ("The [{ElementName}] value is more than '{Value}'") #prefered
@given ("The [{ElementName}] more than '{Value}'")
@then ("The [{ElementName}] more than '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueMoreThan(Value)


@then ("The [{ElementName}] value is more than or equal '{Value}'") #prefered
@given ("The [{ElementName}] more than or equal '{Value}'")
@then ("The [{ElementName}] more than or equal '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueMoreThanOrEqual(Value)


@then ("The [{ElementName}] value is less than '{Value}'") #prefered
@given ("The [{ElementName}] less than '{Value}'")
@then ("The [{ElementName}] less than '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueLessThan(Value)


@then ("The [{ElementName}] value is less than or equal '{Value}'") #prefered
@given ("The [{ElementName}] less than or equal '{Value}'")
@then ("The [{ElementName}] less than or equal '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueLessThanOrEqual(Value)


@given ("The [{ElementName}] value is empty") #prefered
@then ("The [{ElementName}] value is empty") #prefered
@given ("The [{ElementName}] is blank")
@then ("The [{ElementName}] is blank")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueIsBlank()


@then ("The [{ElementName}] value is not empty") #prefered
@given ("The [{ElementName}] has a value")
@then ("The [{ElementName}] has a value")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyHasValue()


@given ("The [{ElementName}] exists") #prefered
@then ("The [{ElementName}] exists")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyExists()


@given ("The [{ElementName}] does not exist") #prefered
@then ("The [{ElementName}] does not exist")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyNotExists()


@given ("The [{ElementName}] is visible") #prefered
@then ("The [{ElementName}] is visible")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyVisible()


@given ("The [{ElementName}] is invisible") #prefered
@then ("The [{ElementName}] is invisible")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyNotVisible()


@given ("The [{ElementName}] is selected") #prefered
@then ("The [{ElementName}] is selected") #prefered
@given ("The [{ElementName}] is checked") #prefered
@then ("The [{ElementName}] is checked") #prefered
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyIsChecked()


@given ("The [{ElementName}] is not selected") #prefered
@then ("The [{ElementName}] is not selected") #prefered
@given ("The [{ElementName}] is unchecked") #prefered
@then ("The [{ElementName}] is unchecked") #prefered
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyIsUnchecked()


#@then ("The [browser list] has item 'Opera'") :TODO


@then ("The popup message shows '{Value}'") #prefered
@given ("The popup shows '{Value}'")
@then ("The popup shows '{Value}'")
def step(context, Value):
    World.VerifyPopupMessage(Value)


@then ("The page has '{Amount}' items of [{ElementName}]") #prefered
@given ("The system displays '{Amount}' items of [{ElementName}]")
@then ("The system displays '{Amount}' items of [{ElementName}]")
def step(context, Amount, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyItemsCount(Amount)


@then ("The [{ElementName}] tooltip text is '{Value}'") #prefered
@then ("The [{ElementName}] tooltip is '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyTooltip(Value)
