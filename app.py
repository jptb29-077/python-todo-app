import streamlit as st

st.title("My Python To-Do List")

# Load tasks from session state (like memory that persists while app is open)
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Added: {new_task}")
    else:
        st.warning("Type something first!")

# Display tasks
st.write("### Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(task)
    if col2.button("Delete", key=i):
        st.session_state.tasks.pop(i)
        st.rerun()  # Refresh the app to update list

# Fun extra: Clear all
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.rerun()