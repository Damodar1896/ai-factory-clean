import os

import cashflow_01_content
import cashflow_02_clipping
import cashflow_03_microtasks
import cashflow_04_digitalstore
import cashflow_05_gmb
import cashflow_06_affiliate
import cashflow_07_graphics
import cashflow_08_messaging
import cashflow_09_landingpages
import cashflow_10_cpa

def run_central_hub():
    print("=" * 60)
    print("    🔥 DAMODAR TECH CRAZE - CENTRAL CASHFLOW PIPELINE 🔥")
    print("=" * 60)
    
    cashflow_01_content.run_module()
    cashflow_02_clipping.run_module()
    cashflow_03_microtasks.run_module()
    cashflow_04_digitalstore.run_module()
    cashflow_05_gmb.run_module()
    cashflow_06_affiliate.run_module()
    cashflow_07_graphics.run_module()
    cashflow_08_messaging.run_module()
    cashflow_09_landingpages.run_module()
    cashflow_10_cpa.run_module()
    
    print("-" * 60)
    print("[Success] All 10 Day-1 Cashflow modules successfully connected and running!")
    print("=" * 60)

if __name__ == "__main__":
    run_central_hub()
