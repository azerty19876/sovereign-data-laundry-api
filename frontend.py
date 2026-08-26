"""
==============================================================================
COMPONENT: STATELESS UI INTERFACE GATEWAY (frontend.py)
License: GNU Affero General Public License v3 (AGPLv3)
==============================================================================
"""

import streamlit as st
import requests
import sqlite3
import pandas as pd

DB_FILE = "sovereign_hardened_vault.db"
API_URL = "http://127.0.0"  # FIXED: Pointing dynamically to the exact server port

st.set_page_config(page_title="Sovereign Production Gateway", layout="wide")
st.title("🌐 Hardened Sovereign Data Laundry Engine")
st.caption("Ecosystem Blueprint: Decoupled Multi-Process Institutional Architecture")

try:
    connection = sqlite3.connect(DB_FILE)
    # FIXED: Added safe dataframe size handling to prevent empty database bootstrap crashes
    df_keys = pd.read_sql_query("SELECT COUNT(*) as count FROM token_vault", connection)
    total_vault_keys = df_keys["count"][0] if not df_keys.empty else 0
    df_ledger = pd.read_sql_query("SELECT * FROM compliance_ledger ORDER BY block_id DESC", connection)
    connection.close()
except Exception:
    total_vault_keys = 0
    df_ledger = pd.DataFrame()

col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Microservice Backend Target", "REST ENDPOINT: ACTIVE")
col_m2.metric("SQLite Locked Encryption Keys", int(total_vault_keys))
col_m3.metric("GDPR Cryptographic Logs Written", len(df_ledger))

st.divider()
col_input_panel, col_output_panel = st.columns(2)

with col_input_panel:
    st.write("### 📥 Hardened Ingestion Buffer")
    raw_user_input = st.text_area(
        "Paste Raw Institutional Files / Case Metadata Below:",
        value="CASE ALLOCATION: #990142. Passport Key: NB990214Z. Lead Officer: Elena Rostova. Node Network Hotline: +49176220911. Intranet Mail: elena.r@civil-node.de",
        height=180
    )
    cluster_node_tag = st.text_input("Active Cluster Node Instance:", value="LAN-ROUTER-NODE-01")
    
    if st.button("Execute Hardened Cleanse via Independent API 🚀"):
        try:
            api_payload = {"text": raw_user_input, "node": cluster_node_tag}
            response = requests.post(API_URL, json=api_payload, timeout=5.0)
            
            if response.status_code == 200:
                st.session_state["latest_json_ld"] = response.json()
                st.success("Subroutine completed via standalone microservice execution.")
                st.rerun()
            elif response.status_code == 413:
                st.error("Execution Refused: Data stream volume exceeds strict 1MB protection limit.")
            else:
                st.error(f"Backend Failure: {response.text}")
        except Exception as error_exception:
            st.error(f"API Connection Refused: Ensure backend.py is running. {str(error_exception)}")

with col_output_panel:
    st.write("### 📤 Standard JSON-LD Compliant Object")
    if "latest_json_ld" in st.session_state:
        st.warning("🔒 Standard European JSON-LD Semantic Web Data Package:")
        st.json(st.session_state["latest_json_ld"])
    else:
        st.info("Ingestion streaming layers are clear. Awaiting pipeline triggers.")

st.divider()
st.write("### 🔒 Persistent Cryptographic Append-Only Chain Ledger (Direct SQLite Connection)")
if not df_ledger.empty:
    st.dataframe(df_ledger, use_container_width=True)
else:
    st.caption("No blocks compiled to ledger. Database files are pristine.")
