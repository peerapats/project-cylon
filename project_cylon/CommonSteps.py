# -*- coding: utf-8 -*-
from behave import *
from project_cylon.WorldContext import *

# 
# Given step definitions
#
@given("User has [{PageName}] open")
def step(context, PageName):
    Page = World.FindPage(PageName)
    Page.Go()

# 
# When step definitions
#
@when ("User enters '{Value}' to [{ElementName}]")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeys(Value)


@when ("User enters date '{Value}' to [{ElementName}]")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeysByScript(Value)


@when ("User clears input [{ElementName}]")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeysByScript("")


@when ("User clicks [{ElementName}] link")     
@when ("User clicks [{ElementName}] button")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.Click()


@when ("User selects '{Value}' in [{ElementName}]")
def step(context, Value, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.Select(Value)


@when ("User moves mouse over [{ElementName}]")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.MouseOver()


@when ("User uploads file '{FilePath}' to [{ElementName}]")
def step(context, FilePath, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.SendKeys(FilePath)


@when ("User enters '{Value}' to the popup")
def step(context, Value):
    World.SendKeysToPopup(Value)


@when ('User clicks "OK" on the popup')
def step(context):
    World.AcceptPopup()


@when ('User clicks "Cancel" on the popup')
def step(context):
    World.DismissPopup()

# 
# Then step definitions
#
@given ("The system displays [{PageName}]")
@then ("The system displays [{PageName}]")
def step(context, PageName):
    Page = World.FindPage(PageName)
    World.VerifyURL(Page.URL, False)
    #Page.VerifyURL()

@given ("The system displays '{URL}'")
@then ("The system displays '{URL}'")
def doit(context, URL):
    World.VerifyURL(URL, True)


@given ("The [{ElementName}] shows '{Value}'")
@then ("The [{ElementName}] shows '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueIs(Value)


@given ("The [{ElementName}] contains '{Value}'")
@then ("The [{ElementName}] contains '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueContains(Value)


@given ("The [{ElementName}] more than '{Value}'")
@then ("The [{ElementName}] more than '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueMoreThan(Value)


@given ("The [{ElementName}] more than or equal '{Value}'")
@then ("The [{ElementName}] more than or equal '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueMoreThanOrEqual(Value)


@given ("The [{ElementName}] less than '{Value}'")
@then ("The [{ElementName}] less than '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueLessThan(Value)


@given ("The [{ElementName}] less than or equal '{Value}'")
@then ("The [{ElementName}] less than or equal '{Value}'")
def step(context, ElementName, Value):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueLessThanOrEqual(Value)


@given ("The [{ElementName}] is blank")
@then ("The [{ElementName}] is blank")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyValueIsBlank()


@given ("The [{ElementName}] has a value")
@then ("The [{ElementName}] has a value")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyHasValue()


@given ("The [{ElementName}] exists")
@then ("The [{ElementName}] exists")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyExists()


@given ("The [{ElementName}] does not exist")
@then ("The [{ElementName}] does not exist")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyNotExists()


@given ("The [{ElementName}] is visible")
@then ("The [{ElementName}] is visible")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyVisible()


@given ("The [{ElementName}] is invisible")
@then ("The [{ElementName}] is invisible")
def step(context, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyNotVisible()


@given ("The popup shows '{Value}'")
@then ("The popup shows '{Value}'")
def step(context, Value):
    World.VerifyPopupMessage(Value)


@given ("The system displays '{Value}' items of [{ElementName}]")
@then ("The system displays '{Value}' items of [{ElementName}]")
def step(context, Value, ElementName):
    Element = World.CurrentPage.FindElement(ElementName)
    Element.VerifyItemsCount(Value)


