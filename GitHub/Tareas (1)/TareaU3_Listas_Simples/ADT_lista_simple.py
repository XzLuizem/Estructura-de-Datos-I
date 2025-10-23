class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Gets the data stored in the node."""
        return self.data

    def set_data(self, new_data):
        """Sets the data stored in the node.

        Args:
            new_data: The new data to be stored in the node.
        """
        self.data = new_data


class CareerList:
    """Manages a singly linked list of careers for FICCT."""

    def __init__(self):
        """Initializes an empty CareerList."""
        self.head = None

    def add(self, data):
        """Adds a new career to the end of the list.

        Args:
            data: The data (career name) for the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def search(self, data):
        """Searches for a specific career in the list.

        Args:
            data: The data (career name) to search for.

        Returns:
            True if the career is found, False otherwise.
        """
        current = self.head
        while current:
            if current.get_data() == data:
                return True
            current = current.next_node
        return False

    def delete(self, data):
        """Deletes a specific career from the list.

        Args:
            data: The data (career name) to delete.

        Returns:
            True if the career was deleted, False otherwise.
        """
        if self.head is None:
            return False  # List is empty, nothing to delete

        if self.head.get_data() == data:
            self.head = self.head.next_node
            return True  # Deleted the head node

        current = self.head
        previous = None

        while current:
            if current.get_data() == data:
                previous.next_node = current.next_node
                return True  # Deleted a node in the middle or end

            previous = current
            current = current.next_node

        return False  # Data not found in the list

    def display(self):
        """Prints the careers in the list."""
        current = self.head
        careers = []
        while current:
            careers.append(current.get_data())
            current = current.next_node
        print(" -> ".join(careers))

    def sort(self, order='asc'):
        """Sorts the list of careers in ascending or descending order.

        Args:
            order: The sorting order, 'asc' for ascending,
            'desc' for descending. Defaults to 'asc'.
        """
        if self.head is None:
            return  # Nothing to sort

        # Simple Bubble Sort for linked list
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next_node:
                if order == 'asc':
                    if current.get_data() > current.next_node.get_data():
                        # Swap data using getter and setter
                        temp_data = current.get_data()
                        current.set_data(current.next_node.get_data())
                        current.next_node.set_data(temp_data)
                        swapped = True
                elif order == 'desc':
                    if current.get_data() < current.next_node.get_data():
                        # Swap data using getter and setter
                        temp_data = current.get_data()
                        current.set_data(current.next_node.get_data())
                        current.next_node.set_data(temp_data)
                        swapped = True
                current = current.next_node

    def __len__(self):
        """Returns the number of careers in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def get_head(self):
        """Gets the head node of the list."""
        return self.head


# 1. Create an instance of the CareerList class.
ficct_careers = CareerList()

# 2. Add the careers "Informática", "Sistemas", "Redes", and "Robótica"
careers_to_add = ["Informática", "Sistemas", "Redes", "Robótica"]
print("Adding careers:")
for career in careers_to_add:
    ficct_careers.add(career)
    print(f"Added: {career}")

# 3. Display the current list of careers.
print("\nCurrent list of careers:")
ficct_careers.display()

# 4. Verify the length of the list and display the result.
list_length = len(ficct_careers)
print(f"\nLength of the list: {list_length}")

# 5. Search for an existing career (e.g., "Sistemas")
search_term_existing = "Sistemas"
found_existing = ficct_careers.search(search_term_existing)
print(
    f"\nSearching for '{search_term_existing}': {'Found' if found_existing else 'Not Found'}")

# 6. Search for a career that does not exist (e.g., "Civil")
search_term_non_existing = "Civil"
found_non_existing = ficct_careers.search(search_term_non_existing)
print(
    f"Searching for '{search_term_non_existing}': {'Found' if found_non_existing else 'Not Found'}")

# 7. Delete a career from the list (e.g., "Redes")
delete_term = "Redes"
deleted = ficct_careers.delete(delete_term)
print(f"\nDeleting '{delete_term}': {'Successful' if deleted else 'Failed'}")

# 8. Display the list after deletion.
print("\nList after deletion:")
ficct_careers.display()

# 9. Sort the list in ascending order.
print("\nSorting list in ascending order:")
ficct_careers.sort()

# 10. Display the list sorted ascendingly.
ficct_careers.display()

# 11. Sort the list in descending order.
print("\nSorting list in descending order:")
ficct_careers.sort(order='desc')

# 12. Display the list sorted descendingly.
ficct_careers.display()

# 13. Demonstrate the use of the get_head() method to access the head node's data using get_data().
head_node = ficct_careers.get_head()
if head_node:
    print(f"\nData of the head node: {head_node.get_data()}")
else:
    print("\nThe list is empty, no head node.")

# 14. Demonstrate the use of the set_data() method on a node (e.g., the head node) and then display the list again to show the change.
if head_node:
    print("\nChanging the data of the head node to 'New Career'")
    head_node.set_data("New Career")
    print("List after changing head node data:")
    ficct_careers.display()
else:
    print("\nCannot set data on head node as the list is empty.")
