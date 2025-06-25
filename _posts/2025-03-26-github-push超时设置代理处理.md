前提：自己有翻墙代理，开了代理并不意味git可以用到代理，要配置以下规则：

```
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```