import os
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
index_path = os.path.join(base_dir, 'index.html')
analytics_path = os.path.join(base_dir, 'analytics.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Remove the tabs
index_content = re.sub(r'<button id="tab-marketing" class="window-tab">Marketing Window</button>', '', index_content)
index_content = re.sub(r'<button id="tab-insights" class="window-tab">Insights Window</button>', '', index_content)

# 2. Extract the sections
marketing_window_match = re.search(r'(<section class="management-panel window-panel marketing-window" id="marketing-window">.*?</section>\n)', index_content, re.DOTALL)
insights_window_match = re.search(r'(<section class="management-panel window-panel insights-window" id="insights-window">.*?</section>\n)', index_content, re.DOTALL)

marketing_window_html = marketing_window_match.group(1) if marketing_window_match else ""
insights_window_html = insights_window_match.group(1) if insights_window_match else ""

# Remove them from index.html
if marketing_window_match:
    index_content = index_content.replace(marketing_window_html, '')
if insights_window_match:
    index_content = index_content.replace(insights_window_html, '')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# 3. Append them to analytics.html
with open(analytics_path, 'r', encoding='utf-8') as f:
    analytics_content = f.read()

# Find footer start to inject
footer_marker = "  </div> <!-- end page-shell -->"
if footer_marker not in analytics_content:
    footer_marker = "  <script src=\"app.js\">"

divider = "\n<!-- ================== WINDOW PANELS ================== -->\n<br><hr style=\"border-color: #334155; margin: 40px 0;\"><br>\n"

# Since these were "window-panel" and hidden by default unless active, let's remove the "window-panel" class so they show up normally on the analytics page!
marketing_window_html = marketing_window_html.replace('window-panel ', '').replace('marketing-window', 'marketing-window-analytics')
insights_window_html = insights_window_html.replace('window-panel ', '').replace('insights-window', 'insights-window-analytics')

new_analytics_content = analytics_content.replace(footer_marker, divider + marketing_window_html + "\n\n" + insights_window_html + "\n" + footer_marker)

with open(analytics_path, 'w', encoding='utf-8') as f:
    f.write(new_analytics_content)

print("Shifted Marketing Window and Insights Window successfully!")
