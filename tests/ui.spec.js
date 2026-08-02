const { test, expect } = require('@playwright/test');

test.describe('Sponsor Portal UI Tests', () => {

  test('Index Page Load', async ({ page }) => {
    // Navigate to local backend (assumes it's running on 8000)
    await page.goto('http://127.0.0.1:8000/');
    
    // Check main title
    await expect(page.locator('h1').first()).toContainText('Sponsor Management');
    
    // Check if the dashboard metrics are visible
    await expect(page.locator('#hero-dashboard-sponsors')).toBeVisible();
  });

  test('Admin Page Load (Redirect to login)', async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/admin.html');
    
    // Without token, it should redirect to login.html
    await expect(page).toHaveURL(/.*login\.html/);
  });

  test('Open Login Modal from Index', async ({ page }) => {
    await page.goto('http://127.0.0.1:8000/');
    
    // Click on Admin Login or open modal button
    const adminLink = page.locator('a:has-text("Admin Login")').first();
    if(await adminLink.isVisible()) {
       await adminLink.click();
       // Depending on what UI element opens, we can check its visibility
    }
  });
});
