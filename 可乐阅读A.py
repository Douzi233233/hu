#   --------------------------------注释区--------------------------------
#   入口:http://230640607122241.asfuoqa.cn/r?upuid=2306406
#   走个头谢谢 不然没更新动力了呜呜呜
#   可乐现在是两套接口轮流换 2.13提示获取参数用2.12版本 同理2.12不行用2.13 都不行再反馈
#   变量:yuanshen_klyd
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   抓取Cookie中udtauth12的值填入 搜udtauth12
#   在抓取上面的参数时同时抓取请求头中的user-agent填入yuanshen_useragent
#   corn: 一小时一次即可

#   检测配置：
#   在yuanshen_apptoken，yuanshen_topicid分别填入你的wxpusher的apptoken和topicid
#   注意是填的topicid而不是你的uid 不要傻乎乎把uid填上去 填了不推送文章包黑号的
#   不懂看 https://wxpusher.zjiecode.com/docs/#/ 或 百度 或 打钱

withdrawal_money = 3000 #提现金币数量 1000金币=0.1r
Quantity_limit = 180  #阅读上限篇数 跑满(195篇左右)概率封号
fuck_list = [1,2,126] # 强制推送篇数 不懂默认别瞎改 需要新加的话在后面用 英文逗号加篇数 就行 
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   --------------------------------代码区--------------------------------
'''
Powered By Huaji
Create at [2024-07-30 14:28]

 __    __   __    __       ___             __   __  
|  |  |  | |  |  |  |     /   \           |  | |  | 
|  |__|  | |  |  |  |    /  ^  \          |  | |  | 
|   __   | |  |  |  |   /  /_\  \   .--.  |  | |  | 
|  |  |  | |  `--'  |  /  _____  \  |  `--'  | |  | 
|__|  |__|  \______/  /__/     \__\  \______/  |__|                                                

'''

import base64, zlib, lzma, bz2, gzip
exec((lambda c: compile(c, '<string>'， 'exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('H4sIAF2IqGYC/wGtH1LgQlpoOTFBWSZTWaz09SEADrV/////////////////////////////////////////////4BM/L7N89np77e33b7enpd99O67d776K3uevM199eL63XO3zbO+80V7z4uueu+63d987juX3vfPevb5xvXbzvvRCmD00RmST0wmj0CZGp6MJ6BDNNQYAamnohkmaepo2pqeJ6A0ATEwCYFPIyn6mJ6nom0JibU0xqNT9R6p5ManpG0mT0NNCejJqeiaejEGg1IhTekynpjRMmjTBMamDSnoxMDRMJ6j1HpTwjNEzSZoRg0hkyMpsamIngmTANQepgm0DTEDTJkDTJpqemmowmmJkZTxNMGiYmENMkOqe0mGU8ptSbCepgAEbUyMjRlPJjQnlBiGBJp7UnjSG0am0hgPRGRoYpjIwTINNU/UY0Q9TQZT2pPKfkp4p6ZNGIniMjT0RiNBpPao2psiIU8A1MaJ6ZR5TaJhNMU8RpkamwJpiekbTSeJPRpiIzEn6mjU9NT0YRimRkm01HkwDRo1MjNATBGTTRkaPUm0xqGhgjTQJsjU8SbRpPJtJDqn6aJlPFNlN6Jppk9NTI2gw1J6NGqenspoYnqaaaJjUbUT01PITaegnpNNNoieAptT9Jp6TSPQxqn5GpmpPGKGmmRpiNGFN6gh5TMp6MaTEynqPT00o2mRqaGVT/QmSeTSZMBgRhKZo9TGo9TU/VP1T1PaJoZop4mSP000TamFHhMRlPAIwU8SZkwU8k8JNkwaTRhI8JqZlPU080TCeqfo0JgFPap5qY1Js0p7UxE9QIfCAAMAJ8EBrfggF4ImN1IrWoOCoCb9RQ5LRYAKC53gM2zhe96cJYMBuhU8jiDNjWyFH2ryKgPQvx1673MS6jwRIYdwtzbmIX4Mx7nysUKBb9MMoy9W5XewlzqwniDmAONotBasShhJ4iZrxYfXU0drV6Gxz1gDagINdBBlG3hvg1NFfhrNIXTNpCR5gGtxbAX4z6mjXnv7JaGidEPGs463rPbZVkL4t1g70o8T/AMEfMQnvqDTsJY+GgeN+PicEi68VNiK/twGKnl2U3QM8GOn3a+XHc9S63NctSJObPbqpkRbC0bC0Ul06JhZQnIV/HNtN+pUgy2dkdHZFr6fXZYtvRvlJ/DK40GDHaWUKAh21T0IR55b1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')))))。decode()))
#!Look Your Mother! At the end there was nothing!
