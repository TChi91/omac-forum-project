import models
import stores
member1 = models.Member("fethi", 25)
member2 = models.Member("Ahmed", 33)


post1 = models.Post('Post1', 'This is the first Post model example')
post2 = models.Post('Post2', 'Another post example. it is getting exciting')
post3 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task')

storeMember = stores.MemberStore()
storeMember.add(member1)
storeMember.add(member2)
print storeMember.get_all()

storePost = stores.PostStore()
storePost.add(post1)
storePost.add(post2)
storePost.add(post3)
print storePost.get_all()