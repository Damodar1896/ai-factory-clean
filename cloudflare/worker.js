export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    const affiliateMapping = {
      "/wealth": "https://hop.clickbank.net/?aff=autonomous_wealth_2026",
      "/ai-agent": "https://gumroad.com/l/ai_agent_factory_2026",
      "/psychology": "https://payhip.com/b/shadow_influence_2026"
    };

    if (affiliateMapping[path]) {
      return Response.redirect(affiliateMapping[path], 301);
    }

    return new Response("Autonomous Empire Edge Node Active (2026)", {
      headers: { "content-type": "text/plain" },
    });
  },
};
