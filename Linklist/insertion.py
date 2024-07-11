class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def insert_at_postion(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print(f"Position {position} is out of range")

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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
        
    def search(self, value):
        current = self.head  
        position = 0 
        while current: 
            if current.data == value: 
                return f"Value '{value}' found at position {position}" 
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 


get_list = LinkList()
get_list.insert_at_beginning(20)
get_list.insert_at_beginning(70)
get_list.insert_at_end(100)
get_list.insert_at_postion(10, 0)

get_list.display()

get_list.delete(100)
get_list.display()


print(get_list.search(20))
print(get_list.search(100))
