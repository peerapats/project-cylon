# -*- coding: utf-8 -*-
from behave import *
from project_cylon.WorldContext import *

##
## Given step definitions
##
@step ("User has [{PageName}] page open")
@step ("User has [{PageName}] open")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.Go()

##
## When step definitions
##
@step ("User enters '{Value}' to the [{ElementName}]")
@step ("User enters '{Value}' to [{ElementName}]")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.SendKeys(Value)

@step ("User enters date '{Value}' to the [{ElementName}]")
@step ("User enters date '{Value}' to [{ElementName}]")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.SendKeysByScript(Value)


@step ("User clears value on the [{ElementName}]")
@step ("User clears input [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeysByScript("")


@step ("User selects the [{ElementName}]")
@step ("User clicks the [{ElementName}]")
@step ("User clicks [{ElementName}] link")
@step ("User clicks [{ElementName}] button")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Click()


@step ("User selects '{Value}' on the [{ElementName}]")
@step ("User selects '{Value}' in [{ElementName}]")
def step_impl(context, Value, ElementName):
    Element = World.FindElement(ElementName)
    Element.Select(Value)


@step ("User checks the [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Check()


@step ("User unchecks the [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Uncheck()


@step ("User moves mouse over the [{ElementName}]")
@step ("User moves mouse over [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.MouseOver()


@step ("User uploads file '{FilePath}' to the [{ElementName}]")
@step ("User uploads file '{FilePath}' to [{ElementName}]")
def step_impl(context, FilePath, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeys(FilePath)


@step ("User enters '{Value}' to the popup")
def step_impl(context, Value):
    World.SendKeysToPopup(Value)


@step ('User clicks "OK" on the popup')
def step_impl(context):
    World.AcceptPopup()


@step ('User clicks "Cancel" on the popup')
def step_impl(context):
    World.DismissPopup()

##
## Then step definitions
##
@step ("The browser shows [{PageName}] page")
@step ("The system displays [{PageName}]")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.VerifyPage()


@step ("The page url is '{URL}'")
@step ("The system URL is '{URL}'")
@step ("The system displays '{URL}'")
def step_impl(context, URL):
    World.VerifyURLIs(URL)


@step ("The page url contains '{URL}'")
@step ("The system URL contains '{URL}'")
def step_impl(context, URL):
    World.VerifyURLContains(URL)


@step ("The [{ElementName}] value is '{Value}'")
@step ("The [{ElementName}] shows '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIs(Value)


@step ("The [{ElementName}] value is not '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIsNot(Value)


@step ("The [{ElementName}] value contains '{Value}'")
@step ("The [{ElementName}] contains '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueContains(Value)


@step ("The [{ElementName}] value is more than '{Value}'")
@step ("The [{ElementName}] more than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueMoreThan(Value)


@step ("The [{ElementName}] value is more than or equal '{Value}'")
@step ("The [{ElementName}] more than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueMoreThanOrEqual(Value)


@step ("The [{ElementName}] value is less than '{Value}'")
@step ("The [{ElementName}] less than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueLessThan(Value)


@step ("The [{ElementName}] value is less than or equal '{Value}'")
@step ("The [{ElementName}] less than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueLessThanOrEqual(Value)


@step ("The [{ElementName}] value is between '{Value1}' and '{Value2}'")
def step_impl(context, ElementName, Value1, Value2):
    Element = World.FindElement(ElementName)
    Element.VerifyValueBetween(Value1, Value2)


@step ("The [{ElementName}] value is empty")
@step ("The [{ElementName}] is blank")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIsBlank()


@step ("The [{ElementName}] value is not empty")
@step ("The [{ElementName}] has a value")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyHasValue()


@step ("The [{ElementName}] exists")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyExists()


@step ("The [{ElementName}] does not exist")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyNotExists()


@step ("The [{ElementName}] is visible")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyVisible()


@step ("The [{ElementName}] is invisible")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyNotVisible()


@step ("The [{ElementName}] is selected")
@step ("The [{ElementName}] is checked")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyIsChecked()


@step ("The [{ElementName}] is not selected")
@step ("The [{ElementName}] is unchecked")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyIsUnchecked()


#@step ("The [browser list] has item 'Opera'") :TODO


@step ("The popup message shows '{Value}'")
@step ("The popup shows '{Value}'")
def step_impl(context, Value):
    World.VerifyPopupMessage(Value)


@step ("The page has '{Amount}' items of [{ElementName}]")
@step ("The system displays '{Amount}' items of [{ElementName}]")
def step_impl(context, Amount, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyItemsCount(Amount)


@step ("The [{ElementName}] tooltip text is '{Value}'")
@step ("The [{ElementName}] tooltip is '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyTooltip(Value)
