class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            temp = self.head
            self.head = temp.next
            temp = None
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next

        print("Element is not found")


get_list = LinkList()
get_list.insert_at_beginning(20)
get_list.insert_at_beginning(70)
get_list.insert_at_end(100)
get_list.insert_at_postion(10, 0)

get_list.display()
