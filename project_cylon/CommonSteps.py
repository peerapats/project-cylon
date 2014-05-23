# -*- coding: utf-8 -*-
from behave import *
from project_cylon.WorldContext import *

##
## Given step definitions
##
@step ("User has [{PageName}] page opened") ##->given
@step ("User has [{PageName}] page open")
@step ("User has [{PageName}] open")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.Go()

##
## When step definitions
##
@step ("User enters '{Value}' to the [{ElementName}]") ##->when
@step ("User enters '{Value}' to [{ElementName}]")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.SendKeys(Value)

@step ("User enters date '{Value}' to the [{ElementName}]") ##->when
@step ("User enters date '{Value}' to [{ElementName}]")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.SendKeysByScript(Value)


@step ("User clears value on the [{ElementName}]") ##->when
@step ("User clears input [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeysByScript("")


@step ("User selects the [{ElementName}]") ##->when
@step ("User clicks the [{ElementName}]") ##->when
@step ("User clicks [{ElementName}] link")
@step ("User clicks [{ElementName}] button")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Click()


@step ("User selects '{Value}' on the [{ElementName}]") ##->when
@step ("User selects '{Value}' in [{ElementName}]")
def step_impl(context, Value, ElementName):
    Element = World.FindElement(ElementName)
    Element.Select(Value)


@step ("User checks the [{ElementName}]") ##->when
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Check()


@step ("User unchecks the [{ElementName}]") ##->when
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Uncheck()


@step ("User moves mouse over the [{ElementName}]") ##->when
@step ("User moves mouse over [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.MouseOver()


@step ("User uploads file '{FilePath}' to the [{ElementName}]") ##->when
@step ("User uploads file '{FilePath}' to [{ElementName}]")
def step_impl(context, FilePath, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeys(FilePath)


@step ("User enters '{Value}' to the popup")
def step_impl(context, Value):
    World.SendKeysToPopup(Value)


@step ("User accept the popup")
@step ('User clicks "OK" on the popup')
def step_impl(context):
    World.AcceptPopup()


@step ("User cancel the popup")
@step ('User clicks "Cancel" on the popup')
def step_impl(context):
    World.DismissPopup()

##
## Then step definitions
##
@step ("The browser shows [{PageName}] page") ##->then
@step ("The system displays [{PageName}]")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.VerifyPage()


@step ("The page url is '{URL}'") ##->then
@step ("The system URL is '{URL}'")
@step ("The system displays '{URL}'")
def step_impl(context, URL):
    World.VerifyURLIs(URL)


@step ("The page url contains '{URL}'") ##->then
@step ("The system URL contains '{URL}'")
def step_impl(context, URL):
    World.VerifyURLContains(URL)


@step ("The [{ElementName}] value is '{Value}'") ##->then
@step ("The [{ElementName}] shows '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIs(Value)


@step ("The [{ElementName}] value is not '{Value}'") ##->then
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIsNot(Value)


@step ("The [{ElementName}] value contains '{Value}'") ##->then
@step ("The [{ElementName}] contains '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueContains(Value)


@step ("The [{ElementName}] value is more than '{Value}'") ##->then
@step ("The [{ElementName}] more than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueMoreThan(Value)


@step ("The [{ElementName}] value is more than or equal '{Value}'") ##->then
@step ("The [{ElementName}] more than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueMoreThanOrEqual(Value)


@step ("The [{ElementName}] value is less than '{Value}'") ##->then
@step ("The [{ElementName}] less than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueLessThan(Value)


@step ("The [{ElementName}] value is less than or equal '{Value}'") ##->then
@step ("The [{ElementName}] less than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyValueLessThanOrEqual(Value)


@step ("The [{ElementName}] value is between '{Value1}' and '{Value2}'") ##->then
def step_impl(context, ElementName, Value1, Value2):
    Element = World.FindElement(ElementName)
    Element.VerifyValueBetween(Value1, Value2)


@step ("The [{ElementName}] value is empty") ##->then
@step ("The [{ElementName}] is blank")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyValueIsBlank()


@step ("The [{ElementName}] value is not empty") ##->then
@step ("The [{ElementName}] has a value")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyHasValue()


@step ("The [{ElementName}] exists") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyExists()


@step ("The [{ElementName}] does not exist") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyNotExists()


@step ("The [{ElementName}] is visible") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyVisible()


@step ("The [{ElementName}] is invisible") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyNotVisible()


@step ("The [{ElementName}] is selected") ##->then
@step ("The [{ElementName}] is checked")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyIsChecked()


@step ("The [{ElementName}] is not selected") ##->then
@step ("The [{ElementName}] is unchecked")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyIsUnchecked()


#@step ("The [browser list] has item 'Opera'") :TODO


@step ("The popup message shows '{Value}'") ##->then
@step ("The popup shows '{Value}'")
def step_impl(context, Value):
    World.VerifyPopupMessage(Value)


@step ("The page has '{Amount}' items of [{ElementName}]") ##->then
@step ("The system displays '{Amount}' items of [{ElementName}]")
def step_impl(context, Amount, ElementName):
    Element = World.FindElement(ElementName)
    Element.VerifyItemsCount(Amount)


@step ("The [{ElementName}] tooltip text is '{Value}'") ##->then
@step ("The [{ElementName}] tooltip is '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.VerifyTooltip(Value)
