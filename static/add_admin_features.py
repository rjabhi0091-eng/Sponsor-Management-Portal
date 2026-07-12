import re
import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Export to PDF button next to Google Sheets button
export_html = """
                <button class="action-btn" style="background: #10b981; display: flex; align-items: center; gap: 8px;" onclick="alert('Connecting to Google Sheets...')"><ion-icon name="logo-google"></ion-icon> Connect Google Sheets</button>
                <button class="action-btn" style="background: #ef4444; display: flex; align-items: center; gap: 8px;" onclick="alert('Exporting to PDF...')"><ion-icon name="document-text-outline"></ion-icon> Export to PDF</button>
"""
content = content.replace(
    """<button class="action-btn" style="background: #10b981; display: flex; align-items: center; gap: 8px;" onclick="alert('Connecting to Google Sheets...')"><ion-icon name="logo-google"></ion-icon> Connect Google Sheets</button>""",
    export_html
)

# 2. Add Search/Filter bar above the Registrations table
search_html = """
                <h3 style="color: #fff; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
                    <span><ion-icon name="people-outline"></ion-icon> Recent Registrations</span>
                    <input type="text" id="tableSearch" placeholder="Search by name, ID or type..." onkeyup="filterTable()" style="padding: 8px 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: rgba(0,0,0,0.3); color: #fff; width: 300px; font-size: 14px;">
                </h3>
                <table id="registrationsTable" style="width: 100%; text-align: left; border-collapse: collapse;">
"""
content = content.replace(
    """<h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="people-outline"></ion-icon> Recent
                    Registrations</h3>
                <table style="width: 100%; text-align: left; border-collapse: collapse;">""",
    search_html
)

# 3. Add JS for the filter function
js_html = """
    <script>
        function filterTable() {
            let input = document.getElementById("tableSearch");
            let filter = input.value.toLowerCase();
            let table = document.getElementById("registrationsTable");
            let tr = table.getElementsByTagName("tr");

            for (let i = 1; i < tr.length; i++) {
                let match = false;
                let tds = tr[i].getElementsByTagName("td");
                for (let j = 0; j < tds.length; j++) {
                    if (tds[j]) {
                        if (tds[j].innerHTML.toLowerCase().indexOf(filter) > -1) {
                            match = true;
                            break;
                        }
                    }
                }
                if (match) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    </script>
</body>
"""
content = content.replace("</body>", js_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("admin.html updated with latest features successfully.")
