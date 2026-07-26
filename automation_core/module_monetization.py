import json
import os

class MonetizationFunnel:
    AFFILIATE_NETWORK = {
        "FINANCE": {
            "product": "Algorithmic Wealth Masterclass",
            "link": "https://hop.clickbank.net/?aff=autonomous_wealth_2026",
            "cpa_payout": "$147"
        },
        "AI_TECH": {
            "product": "Autonomous AI Agent Builder",
            "link": "https://gumroad.com/l/ai_agent_factory_2026",
            "cpa_payout": "$97"
        },
        "DARK_PSYCHOLOGY": {
            "product": "Conversational Dominance Blueprint",
            "link": "https://payhip.com/b/shadow_influence_2026",
            "cpa_payout": "$67"
        }
    }

    @staticmethod
    def inject_affiliate_funnel(niche_key, content_assets):
        funnel = MonetizationFunnel.AFFILIATE_NETWORK.get(niche_key, MonetizationFunnel.AFFILIATE_NETWORK["AI_TECH"])
        
        call_to_action = f"\n\n🔥 **Exclusive Resource Mentioned in Video:**\nGet instant access to the {funnel['product']} here: {funnel['link']}\n*(Secured via Autonomous Monetization Engine)*"
        
        content_assets["description"] += call_to_action
        content_assets["monetization_hook"] = funnel['link']
        
        print(f"[+] Monetization Funnel Injected: {funnel['product']} (Target Payout: {funnel['cpa_payout']})")
        return content_assets

if __name__ == "__main__":
    sample = {"description": "Check out this growth strategy."}
    print(MonetizationFunnel.inject_affiliate_funnel("FINANCE", sample))
