# -*-  coding: utf-8  -*-

import web
from xml.dom import minidom
import logging,time
import json

urls = ("/allfortest/(.*)", "JustTest")

app = web.application(urls, globals())

logger = logging.getLogger(__name__)

class JustTest():
    finalvalue = None
    def GET(self,data):
        logging.basicConfig(filename='/data/VirtualBusiness_Data/test_Jenkins.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                            datefmt='%Y/%m/%d %I:%M:%S %p')
        logging.Formatter.converter = time.gmtime
        #input_data = web.input()
        #logger.debug(input_data)
        #for key, value in input_data.items():
            # print value
            # print key
            #self.finalvalue = value

        return 'test_sucess'

        # return '<Response service="RT_INVENTORY_PUSH_SERVICE" lang="zh-CN"><Head>OK</Head><Body><RTInventoryPushResponse><Result>1</Result><Note></Note></RTInventoryPushResponse></Body></Response>'
    def POST(self,data):
        data = web.data()
        # if data == None :
        #     return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + \
        #            "<Response service=\"OrderConfirmService\">" + \
        #            "<Head>Failure</Head><Body></Body></Response>"
        #xml_data = minidom.parse(data)

        logging.basicConfig(filename='/data/VirtualBusiness_Data/testSF.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                            datefmt='%Y/%m/%d %I:%M:%S %p')
        logging.Formatter.converter = time.gmtime
        input_data = web.input()
        logger.debug(input_data)

        # for key, value in input_data.items():
            # print value
            # print key
            # self.finalvalue = value
        print input_data.values()
        return input_data

        # return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+ \
        #        "<Response service=\"ITEM_SERVICE\">" + \
        #        "<Head>OK|PART</Head>" + \
        #        "<Body><ItemResponse>" + \
        #        "<Items>"+ \
        #        "<Item><SkuNo>F18M291</SkuNo><Result>1</Result><Note>成功</Note></Item>" + \
        #        "<Item><SkuNo>FE0577</SkuNo><Result>2</Result><Note>失敗</Note></Item>" + \
        #        "</Items>" + \
        #        "</ItemResponse></Body>" + "</Response>"

if __name__ == "__main__":
    app.run()
