import re

file_path = 'd:/WebPortal/Sponsor-Management-Portal/static/analytics.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Action table header
content = content.replace('<th>Action</th>', '')

# We need to remove the td that contains the action buttons in the tables.
# The structure is:
# <td>
#     <button class="action-btn btn-view">View Details</button>
# </td>
# or
# <td>
#     <button class="action-btn btn-approve">Approve</button>
#     <button class="action-btn btn-reject">Reject</button>
# </td>

# Since we only want to remove these from the registrations tables, let's target the exact td blocks.
pattern = r'<td>\s*(?:<button class="action-btn[^>]+>[^<]+</button>\s*)+</td>'
content = re.sub(pattern, '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Action buttons removed from analytics.html!")
