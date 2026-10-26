# ====================================================
# Project: Code with Paras Browser (First Project)
# Channel: @CodewithParas
# Open Source: github.com/CodewithParas/First-Project
# ====================================================

# Step 1: Lightweight GUI webview library ko import karein
import webview

# ----------------------------------------------------
# Step 2: Basic Variables Setup (Clean & Simple)
# ----------------------------------------------------
# Browser window ka naam
browser_title = "Code with Paras Browser"

# Humara custom search engine URL (No Google!)
browser_url = "https://find-search.onrender.com"

# Window dimensions (Pixels me)
window_width = 1000
window_height = 700

# Persistent data save karne ke liye database file
storage_file = "data.db"

# ----------------------------------------------------
# Step 3: Desktop Browser Window Create Karein
# ----------------------------------------------------
# create_window function me sabhi variables pass karte hain
webview.create_window(
    title=browser_title,
    url=browser_url,
    width=window_width,
    height=window_height
)

# ----------------------------------------------------
# Step 4: Browser Start & Data Storage Enable Karein
# ----------------------------------------------------
# private_mode=False: Cache aur login sessions on rahenge
# storage_path=storage_file: Sara session data 'data.db' me store hoga
webview.start(private_mode=False, storage_path=storage_file)
