import re

with open('d:/WebPortal/Sponsor-Management-Portal/static/analytics.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove duplicate tables
# Find all occurrences of REGISTRATION TABLES
parts = content.split('<!-- ================== REGISTRATION TABLES ================== -->')
if len(parts) > 2:
    # It was injected multiple times. Keep the first part, and the last part.
    # Actually, parts[0] is everything before the first injection.
    # parts[1] is the first injection block (down to the next injection or end).
    # Since the injection point was <!-- ================== WINDOW PANELS ================== -->
    # The duplicate is probably just stacked.
    pass

# A cleaner way: Just delete EVERYTHING between the first REGISTRATION TABLES and WINDOW PANELS, 
# then inject exactly ONE copy of the tables.
table_start = '<!-- ================== REGISTRATION TABLES ================== -->'
window_start = '<!-- ================== WINDOW PANELS ================== -->'

if table_start in content and window_start in content:
    before_tables = content[:content.find(table_start)]
    after_windows = content[content.find(window_start):]
    
    # Extract the actual tables from admin.html to ensure we have exactly one clean copy
    with open('d:/WebPortal/Sponsor-Management-Portal/static/admin.html', 'r', encoding='utf-8') as admin_f:
        admin_content = admin_f.read()
    
    wrapper1 = re.search(r'(<div class="admin-table-wrapper">\s*<h3>.*?Sponsor Registrations.*?</div>)', admin_content, re.DOTALL)
    wrapper2 = re.search(r'(<div class="admin-table-wrapper">\s*<h3>.*?Client Registrations.*?</div>)', admin_content, re.DOTALL)
    table1 = wrapper1.group(1) if wrapper1 else ""
    table2 = wrapper2.group(1) if wrapper2 else ""
    
    tables_combined = f'{table_start}\n<br><hr style="border-color: #334155; margin: 40px 0;"><br>\n<div id="registrations-tables" style="max-width: 1400px; margin: 0 auto;">\n{table1}\n{table2}\n</div>\n'
    
    content = before_tables + tables_combined + after_windows

# 2. Fix the marketing window and insights window centering
# The user says "Marketing Workflow isko frnot se hata kar analytics page pe shift karo dsabad ko" (dashboard ko center karo).
# The grid might be making it look side-aligned. Let's add a wrapper to `.marketing-window-analytics` to force it center.

# In style.css, .management-panel has `display: grid; gap: 2rem; margin-bottom: 2rem;`
# This applies to marketing-window-analytics because it has class "management-panel".
# When grid is applied without template columns, it acts like a block.
# Let's add a specific style in analytics.html head to override it.

center_styles = """
<style>
    /* Absolute Centering Fixes */
    .marketing-window-analytics, .insights-window-analytics {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        max-width: 1200px !important;
        margin: 0 auto 40px auto !important;
        width: 100% !important;
    }
    
    .marketing-window-analytics .window-panel-content,
    .insights-window-analytics .window-panel-content {
        width: 100% !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    .marketing-window-analytics .panel-heading,
    .insights-window-analytics .panel-heading {
        text-align: center !important;
        justify-content: center !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    .marketing-actions form {
        max-width: 800px;
        margin: 0 auto;
    }
</style>
"""

if '/* Absolute Centering Fixes */' not in content:
    content = content.replace('</head>', center_styles + '\n</head>')

with open('d:/WebPortal/Sponsor-Management-Portal/static/analytics.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Marketing workflow centered and tables deduplicated!")
