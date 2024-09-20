先说明一下啊！使用 tampermonkey 请不要安装别人的代码，这很容易泄露你的敏感信息，网页对 UserScript 是透明的。

tampermonkey 是一个可以将 UserScript 注入到网页中的 chrome 插件，为什么我要写它？

我举一个场景，你就明白它有什么用了。

很多朋友是专门做零撸测试网的，如果你的号很多，领水就很不方便，但是你注入 UserScript 并且结合 metamask 的 多 wallet 的 event 就能快速半自动的给不同的钱包完成领水的工作。

当然，不止领水，还有很多有意思的事情，你可以探索一下。

我说一个我想到的思路，由于 metamask 注入了 ethereum 对象，你可以在切换地址时候发出事件，在 UserScript 里监听，然后配合你做好的一套自动登录，签名的流程，再配合 Proxy SwitchyOmega 来管理的网络，大部分场景都能完成，只需要一点点手动，比如签名会调起来 metamask 的界面，你要手动的点一下。

[https://chromewebstore.google.com/detail/%E7%AF%A1%E6%94%B9%E7%8C%B4/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=zh-CN&utm_source=ext_sidebar](https://chromewebstore.google.com/detail/%E7%AF%A1%E6%94%B9%E7%8C%B4/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=zh-CN&utm_source=ext_sidebar)


[https://developer.chrome.com/docs/extensions/reference/api/userScripts](https://developer.chrome.com/docs/extensions/reference/api/userScripts)