### MCP  playwright-mcp-server
npm install -g @executeautomation/playwright-mcp-server

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@executeautomation/playwright-mcp-server"]
    }
  }
}
```


特定mcp-Server：专事专办，使用自然语言实现需求；结合大模型能力、可实现自动化流程；

基于长视频（爬取）进行概括、二次创作，自动生成字幕讲解

### MCP  playwright-mcp-server[https://www.firecrawl.dev/]
npm install -g firecrawl-mcp

```
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR-API-KEY"
      }
    }
  }
}
```
```

提示词：@https://cloud.tencent.com/developer/article/2516282  抓取其中的内容文章，整理成markdown格式
提示词2：@https://cloud.tencent.com/developer/article/2516282  获取上面全部链接，保存到link.txt
好用提示词：@https://movie.douban.com/top250  抓取豆瓣电影Top200，存储到dbtop250.xlsl，如果用到python脚本，请自动安装依赖并执行，不需要再询问我了
```

#### 豆包

功能：
AI 划词，让桌面上的每一个应用都接入 AI

截图提问

