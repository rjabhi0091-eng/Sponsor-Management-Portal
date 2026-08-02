import re
import os

filepath = 'admin.html'
html = open(filepath, 'r', encoding='utf-8').read()

# 1. Add "Entity Management" tab to sidebar
sidebar_link = """        <a href="#" class="sidebar-link" onclick="switchTab('entity-management', this)"><ion-icon name="business-outline"></ion-icon> Entity Management</a>"""
html = html.replace('        <a href="#" class="sidebar-link" onclick="switchTab(\'feedback\', this)"><ion-icon name="chatbubbles-outline"></ion-icon>\n            Feedback Review</a>', 
                    '        <a href="#" class="sidebar-link" onclick="switchTab(\'feedback\', this)"><ion-icon name="chatbubbles-outline"></ion-icon>\n            Feedback Review</a>\n' + sidebar_link)

# 2. Add Entity Management Tab Content
entity_management_tab = """
        <!-- Entity Management Tab -->
        <div id="entity-management" class="tab-content">
            <h1 style="color: #fff; margin-bottom: 20px;">Entity Management</h1>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px;">
                <div class="glass-panel" style="padding: 25px; border-radius: 16px;">
                    <h3 style="color: #8b5cf6; margin-top: 0; margin-bottom: 20px;"><ion-icon name="business-outline"></ion-icon> Add/Edit Sponsor</h3>
                    <form id="admin-sponsor-form" onsubmit="submitAdminSponsor(event)">
                        <input type="hidden" id="admin-sponsor-id">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Name</label>
                        <input type="text" id="admin-sponsor-name" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Email</label>
                        <input type="email" id="admin-sponsor-email" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Phone</label>
                        <input type="text" id="admin-sponsor-phone" style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Password</label>
                        <input type="password" id="admin-sponsor-password" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <button type="submit" style="width: 100%; padding: 12px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">Save Sponsor</button>
                    </form>
                </div>
                <div class="glass-panel" style="padding: 25px; border-radius: 16px;">
                    <h3 style="color: #10b981; margin-top: 0; margin-bottom: 20px;"><ion-icon name="person-outline"></ion-icon> Add/Edit Client</h3>
                    <form id="admin-client-form" onsubmit="submitAdminClient(event)">
                        <input type="hidden" id="admin-client-id">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Name</label>
                        <input type="text" id="admin-client-name" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Email</label>
                        <input type="email" id="admin-client-email" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Company</label>
                        <input type="text" id="admin-client-company" style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Password</label>
                        <input type="password" id="admin-client-password" required style="width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        <button type="submit" style="width: 100%; padding: 12px; background: #10b981; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">Save Client</button>
                    </form>
                </div>
            </div>
        </div>
"""
# Insert before <!-- Settings Tab -->
html = html.replace('        <!-- Settings Tab -->', entity_management_tab + '\n        <!-- Settings Tab -->')


# 3. Add Campaign Builder Card to Marketing Hub Grid
campaign_card = """
                <!-- Campaign Builder Card -->
                <div class="glass-panel" style="padding: 25px; border-radius: 16px; grid-column: span 2;">
                    <h3 style="color: #ec4899; margin-top: 0; display: flex; align-items: center; gap: 10px;">
                        <ion-icon name="rocket-outline"></ion-icon> Campaign Builder
                    </h3>
                    <form id="admin-campaign-form" onsubmit="submitAdminCampaign(event)" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                        <div>
                            <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Campaign Title</label>
                            <input type="text" id="admin-campaign-title" required style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                        </div>
                        <div>
                            <label style="color: #a1a1aa; display: block; margin-bottom: 5px; font-size: 14px;">Platform</label>
                            <select id="admin-campaign-platform" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); background: #18181b; color: #fff;">
                                <option value="Instagram">Instagram</option>
                                <option value="LinkedIn">LinkedIn</option>
                                <option value="Twitter">Twitter</option>
                                <option value="YouTube">YouTube</option>
                            </select>
                        </div>
                        <div style="grid-column: span 2;">
                            <button type="submit" style="width: 100%; padding: 12px; background: #ec4899; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">Create Campaign</button>
                        </div>
                    </form>
                </div>
"""
html = html.replace('            </div>\n        </div>\n\n    </div>', campaign_card + '            </div>\n        </div>\n\n    </div>')


# 4. Add JS functions for handling submissions
js_functions = """
        async function submitAdminSponsor(event) {
            event.preventDefault();
            const payload = {
                name: document.getElementById('admin-sponsor-name').value,
                email: document.getElementById('admin-sponsor-email').value,
                phone: document.getElementById('admin-sponsor-phone').value,
                password: document.getElementById('admin-sponsor-password').value,
                status: "active"
            };
            try {
                const res = await fetch(BASE_URL + '/sponsors/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if (res.ok) {
                    alert('Sponsor added successfully');
                    document.getElementById('admin-sponsor-form').reset();
                    fetchRegistrations(); // Refresh registrations table
                } else {
                    const data = await res.json();
                    alert('Failed to add sponsor: ' + (data.detail || 'Unknown error'));
                }
            } catch(e) { console.error(e); alert('Error connecting to server'); }
        }

        async function submitAdminClient(event) {
            event.preventDefault();
            const payload = {
                name: document.getElementById('admin-client-name').value,
                email: document.getElementById('admin-client-email').value,
                company: document.getElementById('admin-client-company').value,
                password: document.getElementById('admin-client-password').value,
                status: "active"
            };
            try {
                const res = await fetch(BASE_URL + '/clients/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if (res.ok) {
                    alert('Client added successfully');
                    document.getElementById('admin-client-form').reset();
                    fetchRegistrations();
                } else {
                    const data = await res.json();
                    alert('Failed to add client: ' + (data.detail || 'Unknown error'));
                }
            } catch(e) { console.error(e); alert('Error connecting to server'); }
        }

        async function submitAdminCampaign(event) {
            event.preventDefault();
            const payload = {
                title: document.getElementById('admin-campaign-title').value,
                platform: document.getElementById('admin-campaign-platform').value,
                status: "active"
            };
            try {
                const res = await fetch(BASE_URL + '/marketing/campaigns', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
                    body: JSON.stringify(payload)
                });
                if (res.ok) {
                    alert('Campaign created successfully');
                    document.getElementById('admin-campaign-form').reset();
                } else {
                    const data = await res.json();
                    alert('Failed to create campaign: ' + (data.detail || 'Unknown error'));
                }
            } catch(e) { console.error(e); alert('Error connecting to server'); }
        }
"""
html = html.replace('// Load data on page load', js_functions + '\n        // Load data on page load')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated admin.html")
