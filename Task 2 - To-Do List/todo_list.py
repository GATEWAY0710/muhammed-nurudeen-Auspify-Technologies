import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            return True
        except IOError:
            print("Error: Could not save tasks.")
            return False
    
    def add_task(self, task_description):
        """Add a new task."""
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        if self.save_tasks():
            print(f"\n✓ Task added successfully!")
        return task
    
    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nNo tasks yet. Add one to get started!")
            return
        
        print("\n" + "=" * 60)
        print("   YOUR TASKS")
        print("=" * 60)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']}. [{status}] {task['description']}")
            print(f"   Created: {task['created_at']}")
            print("-" * 60)
    
    def mark_complete(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                if self.save_tasks():
                    print(f"\n✓ Task '{task['description']}' marked as completed!")
                return True
        print(f"\nError: Task with ID {task_id} not found.")
        return False
    
    def delete_task(self, task_id):
        """Delete a task."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                # Reassign IDs
                for j, t in enumerate(self.tasks):
                    t["id"] = j + 1
                if self.save_tasks():
                    print(f"\n✓ Task '{removed_task['description']}' deleted!")
                return True
        print(f"\nError: Task with ID {task_id} not found.")
        return False

def main():
    todo = TodoList()
    
    while True:
        print("\n" + "=" * 40)
        print("   TO-DO LIST APPLICATION")
        print("=" * 40)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("=" * 40)
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                task_desc = input("\nEnter task description: ").strip()
                if task_desc:
                    todo.add_task(task_desc)
                else:
                    print("\nError: Task description cannot be empty!")
            
            elif choice == '2':
                todo.view_tasks()
            
            elif choice == '3':
                todo.view_tasks()
                if todo.tasks:
                    try:
                        task_id = int(input("\nEnter task ID to mark as completed: ").strip())
                        todo.mark_complete(task_id)
                    except ValueError:
                        print("\nError: Please enter a valid number.")
            
            elif choice == '4':
                todo.view_tasks()
                if todo.tasks:
                    try:
                        task_id = int(input("\nEnter task ID to delete: ").strip())
                        todo.delete_task(task_id)
                    except ValueError:
                        print("\nError: Please enter a valid number.")
            
            elif choice == '5':
                print("\nThank you for using To-Do List App! Goodbye!")
                break
            
            else:
                print("\nError: Invalid choice. Please select 1-5.")
            
            input("\nPress Enter to continue...")
            
        except EOFError:
            print("\n\nGoodbye!")
            break
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()
