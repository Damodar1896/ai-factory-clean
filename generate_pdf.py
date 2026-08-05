from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def add_footer(canvas, doc):
    if doc.page == 1:
        return
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#718096'))
    footer_text = f"Damodar Tech & AI Ecosystem Hub  |  Confidential VIP Bonus  |  Page {doc.page}"
    canvas.drawRightString(572, 30, footer_text)
    canvas.setStrokeColor(colors.HexColor('#E2E8F0'))
    canvas.setLineWidth(0.5)
    canvas.line(40, 42, 572, 42)
    canvas.restoreState()

def create_pdf():
    filename = "masterguide.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=36, leftMargin=36,
                            topMargin=36, bottomMargin=36)
    story = []
    styles = getSampleStyleSheet()

    bg_deep_navy = colors.HexColor('#090D16')
    accent_blue = colors.HexColor('#38BDF8')
    text_white = colors.HexColor('#FFFFFF')
    text_muted = colors.HexColor('#94A3B8')
    
    card_bg = colors.HexColor('#F8FAFC')
    border_color = colors.HexColor('#E2E8F0')
    accent_bar = colors.HexColor('#2563EB')

    cover_title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Heading1'],
        fontSize=26, textColor=text_white,
        alignment=1, spaceAfter=12, fontName="Helvetica-Bold", leading=32
    )
    
    cover_sub_style = ParagraphStyle(
        'CoverSub', parent=styles['Normal'],
        fontSize=11, textColor=text_muted,
        alignment=1, fontName="Helvetica", leading=18
    )

    mod_heading_style = ParagraphStyle(
        'ModHeading', parent=styles['Heading2'],
        fontSize=14, textColor=colors.HexColor('#0F172A'),
        spaceBefore=10, spaceAfter=12, fontName="Helvetica-Bold"
    )

    prompt_title_style = ParagraphStyle(
        'PromptTitle', parent=styles['Normal'],
        fontSize=9.5, textColor=accent_bar,
        fontName="Helvetica-Bold", spaceAfter=3
    )

    prompt_desc_style = ParagraphStyle(
        'PromptDesc', parent=styles['Normal'],
        fontSize=9, textColor=colors.HexColor('#1E293B'),
        fontName="Helvetica", leading=13
    )

    # ==================== PAGE 1: LUXURY FULL COVER ====================
    cover_elements = [
        Spacer(1, 90),
        Paragraph("💎 THE ULTIMATE VIP BONUS PACKAGE", ParagraphStyle('Badge', parent=styles['Normal'], fontSize=11, textColor=accent_blue, alignment=1, fontName="Helvetica-Bold", spaceAfter=20)),
        Paragraph("100+ AI Business & Automation Prompts Masterguide", cover_title_style),
        Spacer(1, 10),
        Paragraph("The exact engineering frameworks and high-performance prompts used to scale digital operations, programmatic SEO, and automated revenue streams.", cover_sub_style),
        Spacer(1, 130),
        Paragraph("<b>CURATED & PUBLISHED EXCLUSIVELY BY:</b>", ParagraphStyle('PubTop', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#64748B'), alignment=1)),
        Spacer(1, 5),
        Paragraph("Damodar Tech & AI Ecosystem Hub", ParagraphStyle('PubBot', parent=styles['Normal'], fontSize=14, textColor=text_white, alignment=1, fontName="Helvetica-Bold")),
        Spacer(1, 40)
    ]
    
    # Safe height of 680 to fit perfectly on Page 1 without spilling over
    cover_table = Table([[cover_elements]], colWidths=[540], rowHeights=[680])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_deep_navy),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 30),
        ('RIGHTPADDING', (0,0), (-1,-1), 30),
    ]))
    
    story.append(cover_table)
    story.append(PageBreak())

    # ==================== PROMPTS DATA ====================
    modules = [
        ("MODULE 1: pSEO & Programmatic Content Scaling", [
            ("1. Keyword Clustering Prompt", "Act as an expert SEO architect. Group the following 50 keywords into logical content silos."),
            ("2. Automated Article Outline Generator", "Create a high-converting SEO-optimized article outline for long-tail keywords."),
            ("3. Meta Description Booster", "Write 5 compelling meta descriptions under 150 characters with high CTA."),
            ("4. FAQ Schema Builder", "Generate 10 FAQs with concise answers optimized for Google Snippets."),
            ("5. Internal Linking Strategy Prompt", "Suggest 5 contextual internal linking anchor texts and placements."),
            ("6. Programmatic URL Mapping", "Create a clean URL slug structure combining locations and service terms."),
            ("7. Search Intent Classification", "Categorize keyword lists into informational, transactional, and navigational intent."),
            ("8. Content Cannibalization Check", "Write a prompt to identify overlapping keyword targets across pages."),
            ("9. AI Overview Optimization", "Format content sections specifically to rank inside Google's AI Overview boxes."),
            ("10. Title Tag Multiplier", "Generate 20 high-CTR title tag variations using dynamic variable injection."),
            ("11. Localized Intro Writer", "Write localized hook paragraphs targeting regional service areas seamlessly."),
            ("12. Featured Snippet Extractor", "Convert long paragraphs into bulleted lists for immediate snippet capture."),
            ("13. Image Alt Text Generator", "Write descriptive SEO-friendly alt text for technical and business graphics."),
            ("14. Orphan Page Recovery", "Outline a strategy to find and interlink unlinked pages on a large site."),
            ("15. Keyword Gap Prompt", "Analyze competitor keyword profiles to find untapped programmatic opportunities."),
            ("16. Content Freshness Prompt", "Draft update notes to refresh outdated statistics in legacy blog posts."),
            ("17. XML Sitemap Strategy", "Structure priorities and change frequencies for thousands of programmatic pages."),
            ("18. Category Silo Architecture", "Map out parent-child relationships for massive software directories."),
            ("19. Redirect Mapping Prompt", "Create bulk 301 redirect mapping rules during URL restructuring."),
            ("20. Core SEO Audit Checklist", "Generate a quick programmatic check for broken links and missing tags.")
        ]),
        ("MODULE 2: Business Operations & Workflow Automation", [
            ("21. Client Onboarding Email Template", "Write a welcoming and structured onboarding email for new clients."),
            ("22. Meeting Agenda Creator", "Create a strict 30-minute agenda for a weekly sprint review meeting."),
            ("23. Bug Reporting Template", "Design a clear and standardized bug reporting template for software testing."),
            ("24. Project Scope Document", "Draft a concise project scope summary outline for a custom tech project."),
            ("25. Vendor Evaluation Matrix", "Create criteria points to evaluate software and cloud hosting vendors."),
            ("26. Client Feedback Form Questions", "Write 5 high-response questions for post-project surveys."),
            ("27. Remote Team Check-in Prompt", "Draft an asynchronous daily stand-up update template for developers."),
            ("28. Risk Management Assessment", "List 5 potential technical risks in web launches and quick fixes."),
            ("29. Refund and Cancellation Policy", "Write a professional and clear refund policy for digital services."),
            ("30. Task Prioritization Matrix", "Explain how to use the Eisenhower Matrix for daily business tasks."),
            ("31. Invoice Follow-up Message", "Write a polite yet firm payment reminder message for overdue invoices."),
            ("32. Password Security Guidelines", "Draft a quick team security policy for managing API keys securely."),
            ("33. API Integration Documentation Outline", "Create a structured outline to document custom integrations."),
            ("34. Server Migration Checklist", "Generate a pre and post-migration checklist for hosting moves."),
            ("35. Performance Review Template", "Write a constructive quarterly performance review template."),
            ("36. Standard Operating Procedure (SOP)", "Write step-by-step instructions for recurring tasks."),
            ("37. Customer Support FAQ Script", "Draft polite resolution-oriented responses for helpdesks."),
            ("38. Expense Reduction Audit", "Provide practical strategies to cut software overhead costs."),
            ("39. Team Delegation Framework", "Create a weekly task delegation matrix for remote teams."),
            ("40. Automated Nurture Sequence", "Write a 5-part email sequence for onboarding new leads.")
        ]),
        ("MODULE 3: High-Converting Sales & Affiliate Copywriting", [
            ("41. Affiliate Product Review Outline", "Write a high-converting product review focusing on pros and cons."),
            ("42. Cold Outreach Email for B2B", "Write a short cold email offering custom automation solutions."),
            ("43. Flash Sale Urgency Script", "Create a high-urgency Telegram broadcast message for discount deals."),
            ("44. Landing Page Hero Section", "Write headlines and CTA button text for high-converting landing pages."),
            ("45. Webinar Registration Copy", "Write persuasive invitation copy for online training sessions."),
            ("46. Cart Abandonment Reminder", "Write short reminder texts for users who dropped off."),
            ("47. Social Proof Integration", "Draft a template on weaving customer testimonials naturally."),
            ("48. Feature-to-Benefit Translator", "Translate technical specs into customer benefits."),
            ("49. High-Ticket Closing Script", "Write polite negotiation messages for high-value deals."),
            ("50. Product Launch Teaser", "Create a 3-day teaser campaign sequence for digital assets."),
            ("51. Cross-sell Recommendation Copy", "Write suggestion messages for related tools."),
            ("52. Discount Code Announcement", "Draft exciting promotional messages for coupon codes."),
            ("53. FAQ Objection Buster", "Write answers to top pricing objections."),
            ("54. Value Stacking Copy", "Structure product components into an irresistible value offer."),
            ("55. Re-engagement Copy", "Write friendly wake-up messages for inactive subscribers."),
            ("56. Exclusive VIP Club Invitation", "Draft invite messages for private communities."),
            ("57. Comparison Table Copy", "Write punchy points showing why recommended tools win."),
            ("58. Urgency Timer Prompt Text", "Write catchy copy to accompany countdown timers."),
            ("59. Affiliate Disclosure Statement", "Write FTC-compliant affiliate disclosure notes."),
            ("60. Call-to-Action Variations", "Generate 10 different high-converting button texts.")
        ]),
        ("MODULE 4: Social Media & Viral Traffic Generation", [
            ("61. LinkedIn Carousel Content Plan", "Outline a 5-slide carousel explaining passive income."),
            ("62. Short-Form Video Hook Generator", "Write 10 attention-grabbing hooks for Reels and Shorts."),
            ("63. Reddit Community Value Post", "Draft a helpful non-promotional case study post."),
            ("64. Medium / Blog Article Introduction", "Write storytelling intros for escaping the 9-to-5."),
            ("65. Quora Answer Framework", "Draft detailed answers on starting affiliate marketing."),
            ("66. Telegram Poll Question Builder", "Create interactive engagement poll questions."),
            ("67. Viral Meme Concept Ideas", "Suggest relatable tech humor meme concepts."),
            ("68. Infographic Data Structure", "Organize data points for software growth graphics."),
            ("69. Podcast Episode Show Notes", "Write structured show notes and timestamps."),
            ("70. Community Welcome Message", "Draft automated welcome notes for new members."),
            ("71. Weekly Roundup Post", "Create summary posts highlighting top tech news."),
            ("72. Behind-the-Scenes Post", "Share transparency journeys of building digital startups."),
            ("73. User Success Spotlight", "Showcase and celebrate community milestones."),
            ("74. Interactive Q&A Prompt", "Write announcement messages for AMA sessions."),
            ("75. Content Repurposing Framework", "Turn 1 article into multiple posts and broadcasts."),
            ("76. Influencer Collaboration Pitch", "Write professional outreach DMs for partnerships."),
            ("77. Giveaway Campaign Rules", "Draft terms and entry steps for software license giveaways."),
            ("78. Trend Jacking Post Idea", "Connect trending tech news with affiliate products."),
            ("79. Day-in-the-Life Outline", "Show workflows of automated business owners."),
            ("80. Motivational Monday Post", "Write inspiring messages for aspiring tech entrepreneurs.")
        ]),
        ("MODULE 5: Advanced Growth & Ultimate Scaling", [
            ("81. Cross-Platform Promo Text", "Adapt long text into punchy WhatsApp/Telegram status copy."),
            ("82. Visual Quote Graphics Text", "Generate impactful quote statements about AI and work."),
            ("83. Feedback Request Post", "Ask audiences what tools or tutorials they need next."),
            ("84. Milestone Celebration Post", "Celebrate community subscriber and user targets."),
            ("85. Resource Sharing Post", "List top free developer and creator tools."),
            ("86. Programmatic Content Matrix", "Combine variables into massive SEO spreadsheets."),
            ("87. Search Intent Analysis", "Map user pain points for specific commercial queries."),
            ("88. Duplicate Content Prevention", "Use variable injections to avoid thin content penalties."),
            ("89. Long-tail Keyword Expansion", "Turn seed terms into high-intent variations."),
            ("90. Schema Markup Guide", "Generate structured JSON-LD code for reviews."),
            ("91. Core Web Vitals Fixes", "List technical solutions for mobile speed."),
            ("92. Backlink Gap Strategy", "Replicate competitor backlink sources systematically."),
            ("93. Broken Link Outreach", "Offer replacement links for dead web resources."),
            ("94. Content Refresh Strategy", "Update legacy posts for higher Google positioning."),
            ("95. Site Architecture Blueprint", "Design clean URL silo structures for portals."),
            ("96. CTR Booster Script", "Rewrite title tags to lift search engine click-through rates."),
            ("97. Zero-Click Search Capture", "Format text sections to lock AI overview rankings."),
            ("98. Analytics Event Mapping", "Track affiliate clicks cleanly using custom parameters."),
            ("99. Passive Income Funnel Blueprint", "Connect organic traffic, bots, and high-ticket offers."),
            ("100. The Ultimate Exit Strategy", "Build digital assets ready for future business acquisition.")
        ])
    ]

    for idx, (mod_title, prompts) in enumerate(modules):
        story.append(Paragraph(mod_title, mod_heading_style))
        story.append(Spacer(1, 4))

        for title, desc in prompts:
            p_title = Paragraph(title, prompt_title_style)
            p_desc = Paragraph(desc, prompt_desc_style)
            
            card_table = Table([[ [p_title, p_desc] ]], colWidths=[540])
            card_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), card_bg),
                ('TOPPADDING', (0,0), (-1,-1), 6),
                ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                ('LEFTPADDING', (0,0), (-1,-1), 10),
                ('RIGHTPADDING', (0,0), (-1,-1), 10),
                ('BOX', (0,0), (-1,-1), 0.5, border_color),
                ('LINELEFT', (0,0), (0,-1), 3.5, accent_bar),
            ]))
            story.append(card_table)
            story.append(Spacer(1, 5))
        
        if idx < len(modules) - 1:
            story.append(PageBreak())

    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=add_footer)
    print("Success! Clean full-bleed luxury cover PDF generated.")

if __name__ == '__main__':
    create_pdf()
