import models
import stores


def print_a_list(list):
    for element in list:
        print element


def stores_should_be_similar():
    print "< Check if stores are similare >"
    members_store1 = stores.MemberStore()
    members_store2 = stores.MemberStore()
    if members_store1.get_all() is members_store2.get_all():
        print "Stores are similar"
    else:
        print "Stores are not similar"
    print "="*30


def store_should_get_members_by_name(members_store):
    print "< get_by_name fuction TEST >"
    members_by_name_retrieved = members_store.get_by_name2("Fethi")
    print_a_list(members_by_name_retrieved)
    print("=" * 30)


def get_by_id_should_retrieve_same_object(store, member2):
    print "< get_by_id fuction TEST >"
    member2_retrieved = store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")
    print "="*30


def update_should_modify_object(member_store, member3):
    print "< update fuction TEST >"
    member3_copy = models.Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))
    print("=" * 30)


def catch_exception_when_deleting():
    print "< Delete fuction TEST >"
    try:
        members_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")
    print("=" * 30)


def create_members():
    print "< Create members >"
    member1 = models.Member("Fethi", 26)
    member2 = models.Member("Fethi", 24)
    member3 = models.Member("Manou", 3)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)
    return member1, member2, member3


def stores_should_add_members(members_instance, members_store):
    for member in members_instance:
        members_store.add(member)


def print_all_members(members_store):
    print "< print_all_members after adding stores >"
    for member in members_store.get_all():
        print member
    print "="*30


######################################################################


def create_posts(members_instances):
    print "< Create posts >"
    post1 = models.Post("Agriculture", "Agriculture is amazing", members_instances[0].id)
    post2 = models.Post("Engineering", "I love engineering", members_instances[0].id)
    post3 = models.Post("Medicine", "Medicine is great", members_instances[1].id)
    post4 = models.Post("Architecture", "Spectacular art", members_instances[1].id)
    post5 = models.Post("Astronomy", "Space is awesome", members_instances[1].id)
    post6 = models.Post("Geology", "Earth is our friend", members_instances[2].id)
    post7 = models.Post("ComputerSci", "Our passion", members_instances[2].id)
    post8 = models.Post("Algorithms", "Yeah, more of that", members_instances[2].id)
    post9 = models.Post("Operating Systems", "Ewww", members_instances[2].id)

    print(post1)
    print(post2)
    print(post3)
    print("=" * 30)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9


def stores_should_add_posts(posts_instance, posts_store):
    for post in posts_instance:
        posts_store.add(post)
    print("=" * 30)


def print_all_posts():
    print "< print_all_Posts after adding stores >"
    for post in posts_store.get_all():
        print post
    print("=" * 30)

######################################################################


members_instance = create_members()
member1, member2, member3 = members_instance
members_store = stores.MemberStore()
stores_should_add_members(members_instance, members_store)

print_all_members(members_store)

posts_instance = create_posts(members_instance)
post1, post2, post3, post4, post5, post6, post7, post8, post9 = posts_instance
posts_store = stores.PostStore()
stores_should_add_posts(posts_instance, posts_store)

print_all_posts()

stores_should_be_similar()

get_by_id_should_retrieve_same_object(members_store, member1)

update_should_modify_object(members_store, member3)

catch_exception_when_deleting()

store_should_get_members_by_name(members_store)
