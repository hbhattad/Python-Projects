def bubble_sort(data):
  """Sorts data in-place using the Bubble Sort algorithm."""
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(data) - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        swapped = True
  return data

def selection_sort(data):
  """Sorts data in-place using the Selection Sort algorithm."""
  for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:
        min_index = j
    if i != min_index:
      data[i], data[min_index] = data[min_index], data[i]
  return data

def insertion_sort(data):
  """Sorts data in-place using the Insertion Sort algorithm."""
  for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and key < data[j]:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data

def merge_sort(data):
  """Sorts data using the Merge Sort algorithm (recursive)."""
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])
  return merge(left, right)

def merge(left, right):
  """Merges two sorted lists (left and right) into a single sorted list."""
  merged = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged += left[i:]
  merged += right[j:]
  return merged

def quick_sort(data):
  """Sorts data using the Quick Sort algorithm (recursive)."""
  if len(data) <= 1:
    return data
  pivot = data[0]
  left = [i for i in data[1:] if i <= pivot]
  right = [i for i in data[1:] if i > pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)

def get_user_choice():
  """Prompts the user for a sorting algorithm choice and validates input."""
  while True:
    choice = input("Enter sorting algorithm (bubble, selection, insertion, merge, quick): ").lower()
    if choice in ["bubble", "selection", "insertion", "merge", "quick"]:
      return choice
    else:
      print("Invalid choice. Please enter a valid sorting algorithm.")

def main():
  """Prompts the user for data, displays the sorting algorithms, and calls the chosen algorithm."""
  data = [int(x) for x in input("Enter data (separated by spaces): ").split()]
  print("Available sorting algorithms:")
  print("1. Bubble Sort")
  print("2. Selection Sort")
  print("3. Insertion Sort")
  print("4. Merge Sort")
  print("5. Quick Sort")

  choice = get_user_choice()

  if choice == "bubble":
    sorted_data = bubble_sort(data.copy())
  elif choice == "selection":
    sorted_data = selection_sort(data.copy())
  elif choice == "insertion":
    sorted_data = insertion_sort(data.copy())
  elif choice == "merge":
    sorted_data = merge_sort(data.copy())
  else:
    sorted_data = quick_sort(data.copy())

  print("Sorted data:", sorted_data)

if __name__ == "__main__":
  main()
