# Coding Exercise 5

def members_list():

    # get new member
    new_member = input("Add a new member: ")
    print(f"{new_member}")

    # open file and read current members
    file = open('../files/members.txt', 'r')
    current_members = file.readlines()
    file.close()

    # add new member to file
    current_members.append(new_member)
    file = open('../files/members.txt', 'w')
    file.writelines(current_members)
    file.close()


if __name__ == '__main__':
    members_list()