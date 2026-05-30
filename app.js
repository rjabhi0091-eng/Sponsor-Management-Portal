const sponsorSearch = document.getElementById("sponsor-search");
const clientSearch = document.getElementById("client-search");
const manageSponsorsBtn = document.getElementById("manage-sponsors-btn");
const manageClientsBtn = document.getElementById("manage-clients-btn");
const sponsorForm = document.getElementById("sponsor-form");
const clientForm = document.getElementById("client-form");
const sponsorStatus = document.getElementById("sponsor-status-message");
const clientStatus = document.getElementById("client-status-message");
const sponsorList = document.getElementById("sponsor-list");
const clientList = document.getElementById("client-list");
const sponsorRefresh = document.getElementById("sponsor-refresh");
const clientRefresh = document.getElementById("client-refresh");
const sponsorClear = document.getElementById("sponsor-clear");
const clientClear = document.getElementById("client-clear");
const heroSponsorCount = document.getElementById("hero-sponsor-count");
const heroClientCount = document.getElementById("hero-client-count");
const totalSponsorsEl = document.getElementById("total-sponsors");
const totalClientsEl = document.getElementById("total-clients");
const lastUpdated = document.getElementById("last-updated");
const sponsorFields = {
  id: document.getElementById("sponsor-id"),
  name: document.getElementById("sponsor-name"),
  email: document.getElementById("sponsor-email"),
  phone: document.getElementById("sponsor-phone"),
  status: document.getElementById("sponsor-status-select"),
  password: document.getElementById("sponsor-password"),
  notes: document.getElementById("sponsor-notes"),
};
const clientFields = {
  id: document.getElementById("client-id"),
  name: document.getElementById("client-name"),
  email: document.getElementById("client-email"),
  phone: document.getElementById("client-phone"),
  company: document.getElementById("client-company"),
  sponsor: document.getElementById("client-sponsor"),
  status: document.getElementById("client-status-select"),
  password: document.getElementById("client-password"),
  notes: document.getElementById("client-notes"),
};
const openSponsorLoginBtn = document.getElementById("open-sponsor-login");
const openClientLoginBtn = document.getElementById("open-client-login");
const loginModal = document.getElementById("login-modal");
const closeLoginBtn = document.getElementById("close-login");
const closeLoginSecondary = document.getElementById("close-login-secondary");
const loginForm = document.getElementById("login-form");
const loginRole = document.getElementById("login-role");
const loginEmail = document.getElementById("login-email");
const loginPassword = document.getElementById("login-password");
const loginStatus = document.getElementById("login-status");
const userWelcome = document.getElementById("user-welcome");
const contactUsBtn = document.getElementById("contact-us-btn");
const contactForm = document.getElementById("contact-form");
const contactStatus = document.getElementById("contact-status");
const contactName = document.getElementById("contact-name");
const contactEmailInput = document.getElementById("contact-email");
const contactMessageInput = document.getElementById("contact-message-input");
const apiBase = "/";
let sponsorsCache = [];
let clientsCache = [];
let currentUser = null;

function setStatus(el, message, type = "success") {
  el.textContent = message;
  el.style.color = type === "error" ? "#f87171" : "#a3e635";
}

function updateMetrics() {
  totalSponsorsEl.textContent = sponsorsCache.length;
  totalClientsEl.textContent = clientsCache.length;
  heroSponsorCount.textContent = sponsorsCache.length;
  heroClientCount.textContent = clientsCache.length;
  lastUpdated.textContent = new Date().toLocaleTimeString();
}

function switchTab(tab) {
  const target = tab === "sponsor" ? document.getElementById("management") : document.getElementById("clients");
  target.scrollIntoView({ behavior: "smooth" });
}

function escapeText(value) {
  return String(value || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

function renderSponsors(sponsors) {
  sponsorList.innerHTML = sponsors
    .map(
      (sponsor) => `
      <tr>
        <td data-label="Name">${escapeText(sponsor.name)}</td>
        <td data-label="Email">${escapeText(sponsor.email)}</td>
        <td data-label="Phone">${escapeText(sponsor.phone || "—")}</td>
        <td data-label="Status">${escapeText(sponsor.status)}</td>
        <td data-label="Actions">
          <button class="action-button" data-icon="✏️" onclick="editSponsor(${sponsor.id})">Edit</button>
          <button class="action-button" data-icon="🗑️" onclick="deleteSponsor(${sponsor.id})">Delete</button>
        </td>
      </tr>
    `,
    )
    .join("");
}

function renderSponsorOptions() {
  clientFields.sponsor.innerHTML = [
    `<option value="">Unassigned</option>`,
    ...sponsorsCache.map((sponsor) => `<option value="${sponsor.id}">${escapeText(sponsor.name)}</option>`),
  ].join("");
}

function renderClients(clients) {
  clientList.innerHTML = clients
    .map(
      (client) => `
      <tr>
        <td data-label="Name">${escapeText(client.name)}</td>
        <td data-label="Email">${escapeText(client.email)}</td>
        <td data-label="Company">${escapeText(client.company || "—")}</td>
        <td data-label="Assigned Sponsor">${escapeText(client.sponsor_name || "—")}</td>
        <td data-label="Status">${escapeText(client.status)}</td>
        <td data-label="Actions">
          <button class="action-button" data-icon="✏️" onclick="editClient(${client.id})">Edit</button>
          <button class="action-button" data-icon="🗑️" onclick="deleteClient(${client.id})">Delete</button>
        </td>
      </tr>
    `,
    )
    .join("");
}

async function fetchSponsors() {
  try {
    const response = await fetch(`${apiBase}sponsors/`);
    sponsorsCache = await response.json();
    renderSponsors(sponsorsCache);
    renderSponsorOptions();
    updateMetrics();
    setStatus(sponsorStatus, `Loaded ${sponsorsCache.length} sponsors.`);
  } catch (err) {
    setStatus(sponsorStatus, "Unable to load sponsors.", "error");
  }
}

async function fetchClients() {
  try {
    const response = await fetch(`${apiBase}clients/`);
    clientsCache = await response.json();
    renderClients(clientsCache);
    updateMetrics();
    setStatus(clientStatus, `Loaded ${clientsCache.length} clients.`);
  } catch (err) {
    setStatus(clientStatus, "Unable to load clients.", "error");
  }
}

function openLogin(role) {
  loginRole.value = role;
  loginEmail.value = "";
  loginPassword.value = "";
  loginStatus.textContent = "";
  loginModal.classList.remove("hidden");
}

function closeLogin() {
  loginModal.classList.add("hidden");
}

function updateWelcome() {
  if (currentUser) {
    userWelcome.textContent = `Logged in as ${currentUser.role}: ${currentUser.name}`;
  } else {
    userWelcome.textContent = "Login as a sponsor or client to personalize your portfolio experience.";
  }
}

async function login(event) {
  event.preventDefault();
  const role = loginRole.value;
  const endpoint = `${apiBase}auth/${role}-login`;
  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: loginEmail.value.trim(),
        password: loginPassword.value.trim(),
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.detail || "Login failed");
    }
    currentUser = { role: payload.role, name: payload.name };
    updateWelcome();
    setStatus(loginStatus, payload.message);
    closeLogin();
  } catch (err) {
    setStatus(loginStatus, err.message, "error");
  }
}

function submitContact(event) {
  event.preventDefault();
  const name = contactName.value.trim();
  const email = contactEmailInput.value.trim();
  const message = contactMessageInput.value.trim();
  if (!name || !email || !message) {
    setStatus(contactStatus, "Please complete all fields.", "error");
    return;
  }
  setStatus(contactStatus, "Thanks for your message! We'll reach out soon.");
  contactForm.reset();
}

function applySponsorFilter() {
  const query = sponsorSearch.value.trim().toLowerCase();
  const filtered = sponsorsCache.filter((sponsor) => {
    return [sponsor.name, sponsor.email, sponsor.phone, sponsor.status, sponsor.notes]
      .filter(Boolean)
      .some((field) => field.toLowerCase().includes(query));
  });
  renderSponsors(filtered);
}

function applyClientFilter() {
  const query = clientSearch.value.trim().toLowerCase();
  const filtered = clientsCache.filter((client) => {
    return [client.name, client.email, client.company, client.phone, client.status, client.notes]
      .filter(Boolean)
      .some((field) => field.toLowerCase().includes(query));
  });
  renderClients(filtered);
}

async function editSponsor(id) {
  try {
    const response = await fetch(`${apiBase}sponsors/${id}`);
    if (!response.ok) throw new Error("Sponsor not found");
    const sponsor = await response.json();
    sponsorFields.id.value = sponsor.id;
    sponsorFields.name.value = sponsor.name;
    sponsorFields.email.value = sponsor.email;
    sponsorFields.phone.value = sponsor.phone || "";
    sponsorFields.status.value = sponsor.status;
    sponsorFields.notes.value = sponsor.notes || "";
    setStatus(sponsorStatus, "Editing sponsor. Save to update.");
    document.getElementById("management").scrollIntoView({ behavior: "smooth" });
  } catch (err) {
    setStatus(sponsorStatus, "Unable to load sponsor.", "error");
  }
}

async function editClient(id) {
  try {
    const response = await fetch(`${apiBase}clients/${id}`);
    if (!response.ok) throw new Error("Client not found");
    const client = await response.json();
    clientFields.id.value = client.id;
    clientFields.name.value = client.name;
    clientFields.email.value = client.email;
    clientFields.phone.value = client.phone || "";
    clientFields.company.value = client.company || "";
    clientFields.sponsor.value = client.sponsor_id || "";
    clientFields.status.value = client.status;
    clientFields.notes.value = client.notes || "";
    setStatus(clientStatus, "Editing client. Save to update.");
    document.getElementById("clients").scrollIntoView({ behavior: "smooth" });
  } catch (err) {
    setStatus(clientStatus, "Unable to load client.", "error");
  }
}

async function deleteSponsor(id) {
  if (!confirm("Delete this sponsor?")) return;
  try {
    const response = await fetch(`${apiBase}sponsors/${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error("Delete failed");
    setStatus(sponsorStatus, "Sponsor deleted.");
    await fetchSponsors();
    applySponsorFilter();
  } catch (err) {
    setStatus(sponsorStatus, "Unable to delete sponsor.", "error");
  }
}

async function deleteClient(id) {
  if (!confirm("Delete this client?")) return;
  try {
    const response = await fetch(`${apiBase}clients/${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error("Delete failed");
    setStatus(clientStatus, "Client deleted.");
    await fetchClients();
    applyClientFilter();
  } catch (err) {
    setStatus(clientStatus, "Unable to delete client.", "error");
  }
}

async function submitSponsor(event) {
  event.preventDefault();
  const payload = {
    name: sponsorFields.name.value.trim(),
    email: sponsorFields.email.value.trim(),
    phone: sponsorFields.phone.value.trim() || null,
    status: sponsorFields.status.value,
    notes: sponsorFields.notes.value.trim() || null,
  };
  const sponsorPassword = sponsorFields.password.value.trim();
  if (sponsorPassword) {
    payload.password = sponsorPassword;
  }
  const id = sponsorFields.id.value;
  const url = id ? `${apiBase}sponsors/${id}` : `${apiBase}sponsors/`;
  const method = id ? "PUT" : "POST";
  try {
    const response = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) {
      const body = await response.json();
      throw new Error(body.detail || "Request failed");
    }
    setStatus(sponsorStatus, `Sponsor ${id ? "updated" : "created"} successfully.`);
    clearSponsorForm();
    await fetchSponsors();
    applySponsorFilter();
  } catch (err) {
    setStatus(sponsorStatus, err.message, "error");
  }
}

async function submitClient(event) {
  event.preventDefault();
  const sponsorIdValue = clientFields.sponsor.value;
  const payload = {
    name: clientFields.name.value.trim(),
    email: clientFields.email.value.trim(),
    phone: clientFields.phone.value.trim() || null,
    company: clientFields.company.value.trim() || null,
    sponsor_id: sponsorIdValue ? Number(sponsorIdValue) : null,
    status: clientFields.status.value,
    notes: clientFields.notes.value.trim() || null,
  };
  const clientPassword = clientFields.password.value.trim();
  if (clientPassword) {
    payload.password = clientPassword;
  }
  const id = clientFields.id.value;
  const url = id ? `${apiBase}clients/${id}` : `${apiBase}clients/`;
  const method = id ? "PUT" : "POST";
  try {
    const response = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) {
      const body = await response.json();
      throw new Error(body.detail || "Request failed");
    }
    setStatus(clientStatus, `Client ${id ? "updated" : "created"} successfully.`);
    clearClientForm();
    await fetchClients();
    applyClientFilter();
  } catch (err) {
    setStatus(clientStatus, err.message, "error");
  }
}

function clearSponsorForm() {
  sponsorFields.id.value = "";
  sponsorFields.name.value = "";
  sponsorFields.email.value = "";
  sponsorFields.phone.value = "";
  sponsorFields.status.value = "prospect";
  sponsorFields.password.value = "";
  sponsorFields.notes.value = "";
}

function clearClientForm() {
  clientFields.id.value = "";
  clientFields.name.value = "";
  clientFields.email.value = "";
  clientFields.phone.value = "";
  clientFields.company.value = "";
  clientFields.sponsor.value = "";
  clientFields.status.value = "active";
  clientFields.password.value = "";
  clientFields.notes.value = "";
}

manageSponsorsBtn.addEventListener("click", () => { document.getElementById("management").scrollIntoView({ behavior: "smooth" }); });
manageClientsBtn.addEventListener("click", () => { document.getElementById("clients").scrollIntoView({ behavior: "smooth" }); });
openSponsorLoginBtn.addEventListener("click", () => openLogin("sponsor"));
openClientLoginBtn.addEventListener("click", () => openLogin("client"));
closeLoginBtn.addEventListener("click", closeLogin);
closeLoginSecondary.addEventListener("click", closeLogin);
contactUsBtn.addEventListener("click", () => document.getElementById("contact").scrollIntoView({ behavior: "smooth" }));
contactForm.addEventListener("submit", submitContact);

// Team carousel controls (responsive)
document.addEventListener("DOMContentLoaded", () => {
  const teamCarousel = document.querySelector(".team-carousel");
  if (!teamCarousel) return;
  const container = teamCarousel.querySelector(".team-grid");
  const prev = teamCarousel.querySelector(".team-prev");
  const next = teamCarousel.querySelector(".team-next");
  const scrollAmount = () => Math.min(container.clientWidth * 0.8, 900);
  prev.addEventListener("click", () => container.scrollBy({ left: -scrollAmount(), behavior: "smooth" }));
  next.addEventListener("click", () => container.scrollBy({ left: scrollAmount(), behavior: "smooth" }));
  // enable keyboard navigation
  prev.addEventListener("keyup", (e) => { if (e.key === "Enter") prev.click(); });
  next.addEventListener("keyup", (e) => { if (e.key === "Enter") next.click(); });

  const attachmentUpload = document.getElementById("attachment-upload");
  const attachmentFileList = document.getElementById("attachment-file-list");
  if (attachmentUpload && attachmentFileList) {
    attachmentUpload.addEventListener("change", () => {
      const files = Array.from(attachmentUpload.files || []);
      if (!files.length) {
        attachmentFileList.textContent = "No files selected.";
        return;
      }

      attachmentFileList.innerHTML = files
        .map(file => `<div>${file.name} (${Math.round(file.size / 1024)} KB)</div>`)
        .join("");
    });
  }
});
sponsorSearch.addEventListener("input", applySponsorFilter);
clientSearch.addEventListener("input", applyClientFilter);
sponsorForm.addEventListener("submit", submitSponsor);
clientForm.addEventListener("submit", submitClient);
loginForm.addEventListener("submit", login);
sponsorRefresh.addEventListener("click", fetchSponsors);
clientRefresh.addEventListener("click", fetchClients);
sponsorClear.addEventListener("click", () => {
  clearSponsorForm();
  setStatus(sponsorStatus, "Sponsor form cleared.");
});
clientClear.addEventListener("click", () => {
  clearClientForm();
  setStatus(clientStatus, "Client form cleared.");
});

window.addEventListener("load", async () => {
  await fetchSponsors();
  await fetchClients();
});

window.editSponsor = editSponsor;
window.deleteSponsor = deleteSponsor;
window.editClient = editClient;
window.deleteClient = deleteClient;
