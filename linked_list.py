class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if (self.head is None):
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        # If we will use this then it'll keep on changing the head and all the previous value except the
        # last inserted and the second last will loose their addresses

        # while self.head.next:
        #     self.head = self.head.next

        # self.head.next = Node(data, None)

        itr.next = Node(data, None)

    # Function to create a different linked list all together
    def insert_val(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_val(self):
        if (self.head is None):
            print("The list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "----->"
            # print(str(itr.data) + "--->")
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head

        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next

            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head

        while itr.next:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            count += 1
            itr = itr.next


ll = Linked_list()
# ll.insert_at_start(90)
# ll.insert_at_start(60)
# ll.insert_at_start(30)
# ll.insert_at_end(9)
ll.insert_val(["Apple", "Banana", "Pear"])
print("length: ", ll.get_length())
ll.insert_at(1, "Kiwi")
# ll.remove_at(3)
ll.print_val()
