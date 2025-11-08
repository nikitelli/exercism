def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    queue = []
    if ticket_type == 1:
        for item in express_queue:
            queue.append(item)
        queue.append(person_name)
        return queue
    # else:
    #     for item in normal_queue:
    #         queue.append(item)
    #         queue.append(person_name)
    #     return queue
    

#r = add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich")
#print(r)
#r = add_me_to_the_queue(["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye")
#print(r)
#r = add_me_to_the_queue(['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 1, 'Okoye')
#print(r)

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    return queue.index(friend_name)

#find_my_friend(["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], "Steve")

def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person_name) 
    return queue

#r = add_me_with_my_friends(['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky')
#print(r)