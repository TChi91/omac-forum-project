import models
import stores


def create_members():
    member1 = models.Member("Mohammed", 20)
    member2 = models.Member("Omar", 22)
    member3 = models.Member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)
    return member1, member2, member3


def create_posts():
    post1 = models.Post('Post1', 'This is the first Post model example')
    post2 = models.Post('Post2', 'Another post example. it is getting exciting')
    post3 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task')
    post4 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task')
    return post1, post2, post3, post4


def store_add_models(instances, store):
    for instance in instances:
        store.add(instance)


def stores_should_be_similar():
    member_store1 = stores.MemberStore()
    member_store2 = stores.MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print "same stores elements"
    else:
        print "not the same stores elements"


def print_all(store):
    print "="*30
    for e in store.get_all():
        print e
    print "="*30


def get_by_id_should_retrieve_same_object(store, member2):
    member2_retrieved = store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


member_instances = create_members()

member1, member2, member3 = member_instances

member_store = stores.MemberStore()

store_add_models(member_instances, member_store)

print_all(member_store)

post_instances = create_posts()

post_store = stores.PostStore()

store_add_models(post_instances, post_store)

stores_should_be_similar()

print_all(post_store)

update_should_modify_object(member_store, member3)

get_by_id_should_retrieve_same_object(member_store, member2)

catch_exception_when_deleting()
