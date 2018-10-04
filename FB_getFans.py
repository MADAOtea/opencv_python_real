'''
Created on 2018年5月3日

@author: user
'''

if __name__ == '__main__':
    pass

import facebook



token = 'EAACEdEose0cBAPnpPBFxooG1quSNEiQekcHQmB8vdG0QPn5WIHFZA7IiEgKH5hF5qeUnz7ZAHjZCQ7cxuUuDvcxZCJ4ttNX1MWlF93ICp1wXFiNvAHZB5w70AWZBZCx7x7JZBC9tbD7jwZB0PTBFUo3MP1EsMFQFnlwCihvSdiKKZAdMwmLEvJLkGjLEZB433bzviGTxxg1JVUYYgZDZD' #貼上前面拿到的Access token

 #貼上前面拿到的Access token
graph = facebook.GraphAPI(access_token = token) #套件會用你的token連接到facebook
fanpage_info = graph.get_object('hungtangdashiau', field = 'id')  #指定拿pyladies.tw 這個粉專的id和讚數
#print(fanpage_info)  #印出來看看長什麼樣子，會是JSON格式的資料
#print("Fanpage id = ", fanpage_info['id'])

posts = graph.get_connections(id = '120932038560635' , connection_name = 'posts', summary = True)
print(posts)   #這行會印出一大堆貼文的資料
print ("共有", len(posts), "篇PO文")