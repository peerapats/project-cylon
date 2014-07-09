# -*- coding: utf-8 -*-
from behave import *

from Logger import *
from WorldContext import *
from CustomOperators import *

import re
import datetime

"""
For create combination steps
"""

@step ("{Execution}, accept fail")
def step_impl(context, Execution):
    try:
        context.execute_steps(u"""When %s""" % Condition)
    except: pass


@step ("{Condition}, {Execution}")
def step_impl(context, Condition, Execution):
    try:
        runResult = False
        context.execute_steps(u"""When %s""" % Condition)
        runResult = True
    except: pass

    if runResult == True:
        context.execute_steps(u"""Then %s""" % Execution)


# @step ("[remote] {Statement}")
# def step_impl(context, Statement):
#     World.driver = World.secondary_driver
#     context.execute_steps(u"""When %s""" % Statement)
#     World.driver = World.primary_driver


"""
Given step definitions
"""

@step ("user has [{PageName}/{PathName}] page opened") ##->given
def step_impl(context, PageName, PathName):
    Page = World.FindPage(PageName)
    Page.Go(PathName)


@step ("user has [{PageName}] page opened") ##->given
@step ("user has [{PageName}] page open")
@step ("user has [{PageName}] open")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.Go()


@step ("user browse to url '{URL}'") ##->given
def step_impl(context, URL):
    Page = World.CreateDummyPage(URL)
    Page.Go()


"""
When step definitions
"""

@step ("user login with '{AccountName}' account")
def step_impl(context, AccountName):
    account = World.FindAccount(AccountName)

    page = World.CurrentPage
    page.WaitForPageLoaded()

    user_fields = "username input|username-input|username_input"
    pass_fields = "password input|password-input|password_input"
    login_buttons = "login button|login-button|login_button"

    World.FindElement(user_fields).SendKeys(account.username)
    World.FindElement(pass_fields).SendKeys(account.password)
    World.FindElement(login_buttons).Click()


@step ("user enters '{Value}' to the [{ElementName}]") ##->when
@step ("user enters '{Value}' to [{ElementName}]")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)
    Element.SendKeys(Value)


@step ("user enters following lines to the [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeys(context.text)


@step ("user enters date '{Value}' to the [{ElementName}]") ##->when
@step ("user enters date '{Value}' to [{ElementName}]")
def step_impl(context, Value, ElementName):
    inputdate = Value
    today = datetime.date.today()

    if Value.lower() == 'today':
        inputdate = "%s 00:00:00" % today
    elif Value.lower() == 'tomorrow':
        tomorrow = today + datetime.timedelta(days=1)
        inputdate = "%s 00:00:00" % tomorrow

    Element = World.FindElement(ElementName)
    Element.SendKeysByScript(inputdate)


@step ("user enters date next '{Value}' days to the [{ElementName}]") ##->when
def step_impl(context, Value, ElementName):
    today = datetime.date.today()

    next_n_days = today + datetime.timedelta(days=int(Value))
    inputdate = "%s 00:00:00" % next_n_days

    Element = World.FindElement(ElementName)
    Element.SendKeysByScript(inputdate)


@step ("user clears value on the [{ElementName}]") ##->when
@step ("user clears input [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeysByScript("")


@step ("user selects the [{ElementName}]") ##->when
@step ("user clicks the [{ElementName}]") ##->when
@step ("user clicks [{ElementName}] link")
@step ("user clicks [{ElementName}] button")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Click()


@step ("user selects '{Value}' on the [{ElementName}]") ##->when
@step ("user selects '{Value}' in [{ElementName}]")
def step_impl(context, Value, ElementName):
    Element = World.FindElement(ElementName)
    Element.Select(Value)


@step ("user checks the [{ElementName}]") ##->when
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Check()


@step ("user unchecks the [{ElementName}]") ##->when
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.Uncheck()


@step ("user moves mouse over the [{ElementName}]") ##->when
@step ("user moves mouse over [{ElementName}]")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)
    Element.MouseOver()


@step ("user uploads file '{FilePath}' to the [{ElementName}]") ##->when
@step ("user uploads file '{FilePath}' to [{ElementName}]")
def step_impl(context, FilePath, ElementName):
    Element = World.FindElement(ElementName)
    Element.SendKeys(FilePath)


#@step ("ผู้ใช้กรอกข้อมูล '{Value}' ลงในหน้าต่างแจ้งเตือน")
@step ("user enters '{Value}' to the popup")
def step_impl(context, Value):
    World.SendKeysToPopup(Value)


@step ("user accept the popup")
@step ('user clicks "OK" on the popup')
def step_impl(context):
    World.AcceptPopup()


@step ("user cancel the popup")
@step ('user clicks "Cancel" on the popup')
def step_impl(context):
    World.DismissPopup()

"""
Then step definitions
"""

@step ("the browser shows [{PageName}/{PathName}] page") ##->then
def step_impl(context, PageName, PathName):
    Page = World.FindPage(PageName)
    Page.VerifyPage(PathName)


@step ("the browser shows [{PageName}] page") ##->then
@step ("the system displays [{PageName}]")
def step_impl(context, PageName):
    Page = World.FindPage(PageName)
    Page.VerifyPage()


@step ("the page url is '{URL}'") ##->then
@step ("the system URL is '{URL}'")
@step ("the system displays '{URL}'")
def step_impl(context, URL):
    World.VerifyURLIs(URL)


@step ("the page url contains '{URL}'") ##->then
@step ("the system URL contains '{URL}'")
def step_impl(context, URL):
    World.VerifyURLContains(URL)

    ## using regex
    # actual = World.driver.current_url
    # expect = re.compile(URL)
    #
    # if expect.match(actual):
    #     return True
    # else:
    #     Log.Failed("Verify url contains?", actual, URL)


@step ("the [{ElementName}] value is '{Value}'") ##->then
@step ("the [{ElementName}] shows '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value == Value:
        return True
    else:
        Log.Failed("Verify value is?", Element.Value, Value)


@step ("the [{ElementName}] value is") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Value == context.text:
        return True
    else:
        Log.Failed("Verify value is? (multi-line)", Element.Value, context.text)


@step ("the [{ElementName}] value is not '{Value}'") ##->then
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value != Value:
        return True
    else:
        Log.Failed("Verify value is not?", Element.Value, Value)


@step ("the [{ElementName}] value contains '{Value}'") ##->then
@step ("the [{ElementName}] contains '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Value in Element.Value:
        return True
    else:
        Log.Failed("Verify value contains?", Element.Value, Value)


@step ("the [{ElementName}] value contains") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if context.text in Element.Value:
        return True
    else:
        Log.Failed("Verify value contains? (multi-line)", Element.Value, Value)


@step ("the [{ElementName}] value is more than '{Value}'") ##->then
@step ("the [{ElementName}] more than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value |more_than| Value:
        return True
    else:
        Log.Failed(
            "Verify value is more than?",
            "value = %s" % Element.Value,
            "value > %s" % Value
        )


@step ("the [{ElementName}] value is more than or equal '{Value}'") ##->then
@step ("the [{ElementName}] more than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value |more_than_or_equal| Value:
        return True
    else:
        Log.Failed(
            "Verify value is more than or equal?",
            "value = %s" % Element.Value,
            "value >= %s" % Value
        )


@step ("the [{ElementName}] value is less than '{Value}'") ##->then
@step ("the [{ElementName}] less than '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value |less_than| Value:
        return True
    else:
        Log.Failed(
            "Verify value is less than?",
            "value = %s" % Element.Value,
            "value < %s" % Value
        )


@step ("the [{ElementName}] value is less than or equal '{Value}'") ##->then
@step ("the [{ElementName}] less than or equal '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.Value |less_than_or_equal| Value:
        return True
    else:
        Log.Failed(
            "Verify value is less than or equal?",
            "value = %s" % Element.Value,
            "value <= %s" % Value
        )


@step ("the [{ElementName}] value is between '{Value1}' and '{Value2}'") ##->then
def step_impl(context, ElementName, Value1, Value2):
    Element = World.FindElement(ElementName)

    if (Element.Value |more_than_or_equal| Value1) and (Element.Value |less_than_or_equal| Value2):
        return True
    elif (Element.Value |less_than_or_equal| Value1) and (Element.Value |more_than_or_equal| Value2):
        return True
    else:
        Log.Failed(
            "Verify value is between?",
            "value = %s" % Element.Value,
            "value is between %s and %s" % (Value1, Value2)
        )


@step ("the [{ElementName}] value is empty") ##->then
@step ("the [{ElementName}] is blank")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Value == "":
        return True
    else:
        Log.Failed("Verify value is empty?", Element.Value, "<blank>")


@step ("the [{ElementName}] value is not empty") ##->then
@step ("the [{ElementName}] has a value")
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Value != "":
        return True
    Log.Failed("Verify value is not empty?", Element.Value, "<any value>")


@step ("the [{ElementName}] exists") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Exists:
        return True
    else:
        Log.Failed("Verify element '%s' exists?" % Element.Name, "not exists", "exists")


@step ("the [{ElementName}] does not exist") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if not Element.Exists:
        return True
    else:
        Log.Failed("Verify element '%s' exists?" % Element.Name, "not exists", "exists")


@step ("the [{ElementName}] is visible") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Visible:
        return True
    else:
        Log.Failed("Verify element '%s' visible?" % Element.Name, "not visible", "visible")


@step ("the [{ElementName}] is invisible") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if not Element.Visible:
        return True
    else:
        Log.Failed("Verify element '%s' not visible?" % Element.Name, "visible", "not visible")


@step ("the [{ElementName}] is selected") ##->then
@step ("the [{ElementName}] is checked") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Selected:
        return True
    else:
        Log.Failed("Verify element '%s' checked?" % Element.Name, "unchecked", "checked")


@step ("the [{ElementName}] is not selected") ##->then
@step ("the [{ElementName}] is unchecked") ##->then
def step_impl(context, ElementName):
    Element = World.FindElement(ElementName)

    if not Element.Selected:
        return True
    else:
        Log.Failed("Verify element '%s' unchecked?" % Element.name, "checked", "unchecked")


@step ("the popup message shows '{Value}'") ##->then
@step ("the popup shows '{Value}'")
def step_impl(context, Value):
    #World.VerifyPopupMessage(Value)
    Message = World.GetPopupMessage()

    if Message == Value:
        return True
    else:
        Log.Failed("Verify popup message is?", Message, Value)


@step ("the page has '{Amount}' items of [{ElementName}]") ##->then
@step ("the system displays '{Amount}' items of [{ElementName}]")
def step_impl(context, Amount, ElementName):
    Element = World.FindElement(ElementName)

    if Element.Count == int(Amount):
        return True
    else:
        Log.Failed(
            "Verify amount of '%s' is?" % Element.Name,
            "amount = %s" % Element.Count,
            "amount = %s" % Amount
        )


@step ("the [{ElementName}] tooltip text is '{Value}'") ##->then
@step ("the [{ElementName}] tooltip is '{Value}'")
def step_impl(context, ElementName, Value):
    Element = World.FindElement(ElementName)

    if Element.TooltipText == Value:
        return True
    else:
        Log.Failed("Verify tooltip text is?", Element.TooltipText, Value)
