// 1. Hide WebDriver property completely
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

    // 2. Mock missing plugins and languages to match a real user
    Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en;q=0.9'] });
    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });

    // 3. Inject fake extension runtime signatures
    window.chrome = {
        runtime: {
            id: "extension_runtime_active_mock",
            connect: function() {},
            sendMessage: function() {}
        }
    };