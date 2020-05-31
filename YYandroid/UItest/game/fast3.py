from time import sleep

import time
from UItest.gamementhod.hhh import hhhmenthod, dxds, s3g, s3s, d3dt, d2td, gametownchossenum, \
    gametownchooseserial2, gametownchooseserial1
from Utility.judge import asser_equal_nu, assert_equal_el
from common.component import Oneclickbetting, ruleoption, add_double, shadowcilck, returntopage, currentbalance, \
    rollbackC, addbetpageC, add5bet, addbet_comfire, officeswitchtogametown, pageamount, fast3_unitprice, \
    gain_lottey_phase, verify_betreocrd, totalphase
from common.fast3component import avaliable_num

now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


def enterfast3(driver, gametype, gameport):
    try:
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/more_title_text_1' and @text='%s']" % gametype).click()
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/item_text_view' and @text='%s']" % gameport).click()
        title = driver.find_element_by_id("com.yy.sport:id/tv_num_desc").text

        assert_equal_el(driver, expect=str(True), actual=str('快三' in title), case="%s游戏投注页面" % gameport,
                        scenes='进入%s游戏' % gametype)
    except:
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("./report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + '进入%s游戏' % gametype + ',' + '选择%s游戏' % gameport + ',' + result + ',' + filename + ',' + '\n')


# 和值-和值-和值玩法 专属方法
def hezhi_play(driver, methodtitle):
    driver.implicitly_wait(5)
    gametype = '快三'
    gameport = '安徽快三'
    if methodtitle == "和值":
        # 阴影三点
        shadowcilck(driver)
        # sleep(1)
        # 断言进入选号页面
        avaliable_num(driver, upmethodtitle=methodtitle)
        # sleep(1)
        # 选号
        hhhmenthod(driver)  # 选号
        # 加倍
        add_double(driver)

        # 一键投注
        res = Oneclickbetting(driver, methodtitle)
        A_balance = res[0]
        B_balance = res[1]
        # 返回上曾页面
        returntopage(driver, rule=methodtitle)

        # 验证金额
        C_balance = currentbalance(driver)
        asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                       case="金额验证",
                       scenes="玩法:%s" % methodtitle)
        # 回滚到投注页面

        rollbackC(driver, gametype=gametype, gameport=gameport)

        # 断言页面可选号和页面进入成功
        avaliable_num(driver, upmethodtitle=methodtitle)

        hhhmenthod(driver)
        addbetpageC(driver, methodtitle=methodtitle)

        # 选5注
        add5bet(driver, methodtitle=methodtitle)

        # 确认下注
        res2 = addbet_comfire(driver, methodtitle=methodtitle)

        A2_balance = res2[0]
        B2_balance = res2[1]

        # 返回上层页面
        returntopage(driver, rule=methodtitle)

        # 验证金额
        C2_balance = currentbalance(driver)
        asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                       case="金额验证",
                       scenes="玩法:%s" % methodtitle)
        # 回滚到投注页面
        print('返回')

        rollbackC(driver, gametype='快三', gameport='安徽快三')


def SBSSDchoosenum(driver, upmethodtitle):
    driver.implicitly_wait(5)
    if upmethodtitle == "和值":
        methodtitle = "和值-大小单双"
        gametype = '快三'
        gameport = '安徽快三'
        sleep(2)
        # 阴影三点
        shadowcilck(driver)
        # 断言进入选号页面
        avaliable_num(driver, upmethodtitle=methodtitle)

        # 打开玩法选项
        ruleoption(driver)

        # 选择大小单双
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='总和大小单双']").click()

        # 下注大小单双
        dxds(driver)

        # 加倍
        add_double(driver)
        # 一键投注
        res = Oneclickbetting(driver, methodtitle)
        A_balance = res[0]
        B_balance = res[1]

        # 返回上曾页面
        returntopage(driver, rule=methodtitle)

        # 验证金额
        C_balance = currentbalance(driver)
        asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                       case="金额验证",
                       scenes="玩法:%s" % methodtitle)
        # 回滚到投注页面

        rollbackC(driver, gametype=gametype, gameport=gameport)

        # 断言页面可选号和页面进入成功
        avaliable_num(driver, upmethodtitle=methodtitle)

        # 打开玩法选项
        ruleoption(driver)

        # 选择大小单双
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='总和大小单双']").click()

        # 下注大小单双
        dxds(driver)

        # 加注
        addbetpageC(driver, methodtitle=methodtitle)

        # 选5注
        add5bet(driver, methodtitle=methodtitle)

        # 确认下注
        res2 = addbet_comfire(driver, methodtitle=methodtitle)

        A2_balance = res2[0]
        B2_balance = res2[1]

        # 返回上层页面
        returntopage(driver, rule=methodtitle)

        # 验证金额
        C2_balance = currentbalance(driver)
        asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                       case="金额验证",
                       scenes="玩法:%s" % methodtitle)
        rollbackC(driver, gametype='快三', gameport='安徽快三')


def same3general(driver, methodtitle):
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法3不同通选
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号通选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号通选']")[1].click()
    # 选号
    s3g(driver)

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, methodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回滚到投注页面

    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号通选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号通选']")[1].click()
    # 选号
    s3g(driver)

    # 加注
    addbetpageC(driver, methodtitle=methodtitle)

    # 选5注
    add5bet(driver, methodtitle=methodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=methodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    # 断言
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def same3single(driver, methodtitle):
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择三同号单选
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号单选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号单选']")[1].click()

    # 选号
    s3s(driver)

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, methodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择三同号单选
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号单选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三同号单选']")[1].click()

    # 选号
    s3g(driver)

    # 加注
    addbetpageC(driver, methodtitle=methodtitle)

    # 选5注
    add5bet(driver, methodtitle=methodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=methodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def diff3(driver, methodtitle):
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号']").click()
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View["
                                 "3]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()

    # 选号,全大小单双,跟s3s方法一样
    """
    s3s是3相同单选的下注方法,采取下注大小单双的方式
    """
    s3s(driver)

    # wait to write 大小单双断言
    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, methodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=methodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号']").click()
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View["
                                 "3]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()

    # 选号,全大小单双,跟s3s方法一样
    """
    s3s是3相同单选的下注方法,采取下注大小单双的方式
    """
    s3s(driver)

    # wait to write 大小单双断言

    # 加注
    addbetpageC(driver, methodtitle=methodtitle)

    # 选5注
    add5bet(driver, methodtitle=methodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=methodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=methodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % methodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def diff3tuo(driver):
    menthodtitle = '三不同号胆拖'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号']").click()
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号胆拖']").click()

    # 选号
    d3dt(driver)

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号']").click()
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三不同号胆拖']").click()
    # 选号
    d3dt(driver)

    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def Consecutive3general(driver):
    menthodtitle = '三连号通选'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三连号通选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三连号通选']")[1].click()

    # 选号
    driver.find_element_by_id("com.yy.sport:id/tv_ball").click()

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三连号通选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='三连号通选']")[1].click()

    # 选号
    driver.find_element_by_id("com.yy.sport:id/tv_ball").click()

    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def same2repeat(driver):
    menthodtitle = '二同号复选'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号复选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号复选']")[1].click()

    # 选号
    s3s(driver)

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号复选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号复选']")[1].click()

    # 选号
    s3s(driver)

    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def same2single(driver):
    menthodtitle = '二同号单选'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号单选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号单选']")[1].click()

    # 选号
    d3dt(driver)

    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号单选']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二同号单选']")[1].click()
    # 选号
    d3dt(driver)

    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def diff2(driver):
    menthodtitle = '二不同号'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[2].click()

    # 选号
    s3s(driver)
    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[0].click()
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[2].click()
    # 选号
    s3s(driver)
    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回到游戏选号页面
    rollbackC(driver, gametype='快三', gameport='安徽快三')


def diff2tuo(driver):
    menthodtitle = '二不同号'
    gametype = '快三'
    gameport = '安徽快三'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    # 断言进入选号页面
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)
    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[0].click()
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号胆拖']").click()

    # 选号
    d2td(driver)
    # 加倍
    add_double(driver)
    # 一键投注
    res = Oneclickbetting(driver, menthodtitle)
    A_balance = res[0]
    B_balance = res[1]

    # 返回上曾页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)
    # 回滚到投注页面
    rollbackC(driver, gametype=gametype, gameport=gameport)

    # 断言页面可选号和页面进入成功
    avaliable_num(driver, upmethodtitle=menthodtitle)

    # 打开玩法选项
    ruleoption(driver)

    # 选择玩法
    driver.find_elements_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号']")[0].click()
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='二不同号胆拖']").click()

    # 选号
    d2td(driver)
    # 加注
    addbetpageC(driver, methodtitle=menthodtitle)

    # 选5注
    add5bet(driver, methodtitle=menthodtitle)

    # 确认下注
    res2 = addbet_comfire(driver, methodtitle=menthodtitle)
    A2_balance = res2[0]
    B2_balance = res2[1]

    # 返回上层页面
    returntopage(driver, rule=menthodtitle)

    # 验证金额
    C2_balance = currentbalance(driver)
    asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                   case="金额验证",
                   scenes="玩法:%s" % menthodtitle)

    rollbackC(driver, gametype='快三', gameport='安徽快三')
    # 完成所有游戏玩法
    # 将页面停在进入彩票的页面上
    # driver.find_elements_by_id("com.yy.sport:id/icon")[1].click()


def gametown_fast3(driver):
    global A_balance, B_balance
    menthodtitle = '快三投注基本页面'
    driver.implicitly_wait(5)
    # 阴影三点
    shadowcilck(driver)
    try:
        driver.find_element_by_class_name("android.widget.TextView").text == '整合'


    except:

        # 切换到娱乐城玩法并断言
        officeswitchtogametown(driver)
    finally:

        # 获取断言要素:整合
        title = driver.find_elements_by_class_name("android.widget.TextView")[1].text
        assert_equal_el(driver, expect="整合", actual=title, case="到达娱乐城页面", scenes="进入快三娱乐")

        # 获取断言需要的页面元素
        titlenum = driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='9']").text
        assert_equal_el(driver, expect="9", actual=titlenum, case="出现投注号码", scenes="进入快三娱乐城")

        # 选号
        gametownchossenum(driver)

        # 下拉
        driver.swipe(start_x=492, start_y=1300, end_x=448, end_y=320, duration=2000)

        # 选号
        gametownchooseserial1(driver)
        # 下拉
        driver.swipe(start_x=492, start_y=1300, end_x=448, end_y=320, duration=2000)
        driver.swipe(start_x=492, start_y=1300, end_x=448, end_y=1020, duration=2000)
        # 选号
        gametownchooseserial2(driver)
        # 获得当前奖期号码
        p = gain_lottey_phase(driver)
        # 投注单价器
        num_bets=fast3_unitprice(driver)
        # 投注前金额校验和断言
        pageamount(driver)
        # 一键投注
        res = Oneclickbetting(driver, menthodtitle)
        A_balance = res[0]
        B_balance = res[1]
        try:
            # 返回上曾页面
            returntopage(driver, rule=menthodtitle)
        except:
            filename = '%s.png' % now
            driver.get_screenshot_as_file("../report/screenshot/%s" % filename)
            with open('../data/result.csv', mode='a+')as f:
                f.write(
                    now + ',' + "玩法:快三娱乐城" + ',' + "一键投注" + ',' + "失败" + ',' + filename +'\n')
            driver.find_element_by_id("com.yy.sport:id/btn_sure").click()
        finally:


            # 验证金额
            C_balance = currentbalance(driver)
            asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance),
                           case="金额验证",
                           scenes="玩法:%s" % menthodtitle)


            #点击投注记录
            verify_betreocrd(driver)
            #获取当前页面奖期数目
            totalphase(driver,p)