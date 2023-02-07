# 1、导入模块
import yagmail
# 2、设置smtp服务信息
yag = yagmail.SMTP(user="2247124474@qq.com", password="xoqivkzaipbqecdh", host='smtp.qq.com')
# 3、设置邮件主题与邮件内容
subject = 'Python邮件测试'
content = ['Python邮件测试']
# 4、发送邮件
yag.send('453650969@qq.com', subject, content)
