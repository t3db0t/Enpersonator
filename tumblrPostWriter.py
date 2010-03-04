from tumblr import Api
import sys, random
from enpersonator import Enpersonator

BLOG='soniayuditskaya.tumblr.com'
USER='marysghost@gmail.com'
PASSWORD='graphicdesign'

api = Api(BLOG,USER,PASSWORD)
enp = Enpersonator()
lines = []

title = enp.generateLine(2, 8)
for i in range(random.randint(3, 12)):
    lines.append(enp.generateLine(random.randint(2, 3), random.randint(50, 300)))

postBody = "\n\n".join(lines)

print "TITLE: ",title, "\n"
print postBody

post = api.write_regular(title, postBody)
print "Published: ", post['url']
