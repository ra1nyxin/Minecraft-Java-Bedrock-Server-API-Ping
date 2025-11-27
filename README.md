# Minecraft Java/Bedrock Server API Ping

A simple Python script to ping Minecraft Java and Bedrock Edition servers using a public API, displaying their status and details in your terminal.
一个简单的 Python 脚本，通过公共 API 查询 Minecraft Java 版和基岩版服务器的状态信息并显示详细内容。

### Features
- Ping Java Edition servers and display version, player count, MOTD, and favicon.
- Ping Bedrock Edition servers and display version, player count, MOTD, and gamemode.

### 功能
- 查询 Java 版服务器，显示版本、玩家数量、MOTD 和服务器图标。
- 查询基岩版服务器，显示版本、玩家数量、MOTD 和游戏模式。

### Usage
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ra1nyxin/Minecraft-Java-Bedrock-Server-API-Ping.git
    cd Minecraft-Java-Bedrock-Server-API-Ping
    ```
2.  **Install dependencies:**
    ```bash
    pip install requests
    ```
3.  **Run the script:**

    *   **Ping a Java Edition server (default port 25565):**
        ```bash
        python main.py --ip <SERVER_IP>
        ```
        Example:
        ```bash
        python main.py --ip play.hypixel.net
        ```

    *   **Ping a Java Edition server (specify port):**
        ```bash
        python main.py --ip <SERVER_IP> --port <PORT_NUMBER>
        ```
        Example:
        ```bash
        python main.py --ip play.hypixel.net --port 25565
        ```

    *   **Ping a Bedrock Edition server (default port 19132):**
        ```bash
        python main.py --ip <SERVER_IP> --edition bedrock
        ```
        Example:
        ```bash
        python main.py --ip play.cubecraft.net --edition bedrock
        ```

    *   **Ping a Bedrock Edition server (specify port):**
        ```bash
        python main.py --ip <SERVER_IP> --port <PORT_NUMBER> --edition bedrock
        ```
        Example:
        ```bash
        python main.py --ip play.cubecraft.net --port 19132 --edition bedrock
        ```

### API Endpoints
This script utilizes the following public API endpoints:
- Java Edition: `https://ping.cornbread2100.com/ping`
- Bedrock Edition: `https://ping.cornbread2100.com/bedrockping`

### 使用教程
1.  **克隆仓库：**
    ```bash
    git clone https://github.com/ra1nyxin/Minecraft-Java-Bedrock-Server-API-Ping.git
    cd Minecraft-Java-Bedrock-Server-API-Ping
    ```
2.  **安装依赖：**
    ```bash
    pip install requests
    ```
3.  **运行脚本：**

    *   **查询 Java 版服务器 (默认端口 25565):**
        ```bash
        python main.py --ip <服务器IP地址>
        ```
        例如：
        ```bash
        python main.py --ip play.hypixel.net
        ```

    *   **查询 Java 版服务器 (指定端口):**
        ```bash
        python main.py --ip <服务器IP地址> --port <端口号>
        ```
        例如：
        ```bash
        python main.py --ip play.hypixel.net --port 25565
        ```

    *   **查询基岩版服务器 (默认端口 19132):**
        ```bash
        python main.py --ip <服务器IP地址> --edition bedrock
        ```
        例如：
        ```bash
        python main.py --ip play.cubecraft.net --edition bedrock
        ```

    *   **查询基岩版服务器 (指定端口):**
        ```bash
        python main.py --ip <服务器IP地址> --port <端口号> --edition bedrock
        ```
        例如：
        ```bash
        python main.py --ip play.cubecraft.net --port 19132 --edition bedrock
        ```

### API 端点
本脚本使用以下公共 API 端点：
- Java 版: `https://ping.cornbread2100.com/ping`
- 基岩版: `https://ping.cornbread2100.com/bedrockping`
