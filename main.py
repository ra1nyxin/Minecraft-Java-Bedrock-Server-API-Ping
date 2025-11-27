import requests
import argparse
import json

def get_java_server_info(ip, port):
    url = f"https://ping.cornbread2100.com/ping?ip={ip}&port={port}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        
        text = response.text
        if text == 'Error: timeout':
            return {"error": "Timeout", "message": "Server did not respond within the expected time."}
        elif text.startswith('Error: '):
            return {"error": "API Error", "message": text[7:]}
        else:
            return json.loads(text)
    except requests.exceptions.Timeout:
        return {"error": "Request Timeout", "message": "The request timed out."}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection Error", "message": "Could not connect to the API server."}
    except requests.exceptions.HTTPError as err:
        return {"error": "HTTP Error", "message": f"HTTP error occurred: {err}"}
    except json.JSONDecodeError:
        return {"error": "JSON Parse Error", "message": "Could not parse JSON response from API."}
    except Exception as e:
        return {"error": "Unknown Error", "message": str(e)}

def get_bedrock_server_info(ip, port):
    url = f"https://ping.cornbread2100.com/bedrockping?ip={ip}&port={port}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        text = response.text
        if text == 'timeout':
            return {"error": "Timeout", "message": "Server did not respond within the expected time."}
        else:
            parts = text.split(';')
            if len(parts) >= 10:
                return {
                    "edition": "Bedrock",
                    "protocol": parts[2],
                    "version": parts[3],
                    "online_players": parts[4],
                    "max_players": parts[5],
                    "motd1": parts[1],
                    "motd2": parts[7],
                    "gamemode": parts[8],
                    "gamemode_id": parts[9],
                    "education_edition": parts[0] == 'MCEE'
                }
            else:
                return {"error": "Parse Error", "message": f"Unexpected API response format: {text}"}
    except requests.exceptions.Timeout:
        return {"error": "Request Timeout", "message": "The request timed out."}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection Error", "message": "Could not connect to the API server."}
    except requests.exceptions.HTTPError as err:
        return {"error": "HTTP Error", "message": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": "Unknown Error", "message": str(e)}

def print_java_info(server_info, ip, port):
    if "error" in server_info:
        print(f"Error fetching Java server info for {ip}:{port}:")
        print(f"  Type: {server_info['error']}")
        print(f"  Message: {server_info['message']}")
    else:
        print(f"Minecraft Java Edition Server Info for {ip}:{port}:")
        print(f"  Version: {server_info.get('version', {}).get('name', 'N/A')} (Protocol: {server_info.get('version', {}).get('protocol', 'N/A')})")
        print(f"  Players: {server_info.get('players', {}).get('online', 'N/A')}/{server_info.get('players', {}).get('max', 'N/A')}")
        description = server_info.get('description', 'N/A')
        if isinstance(description, dict) and 'text' in description:
            description = description['text']
        print(f"  Description: {description}")
        favicon = server_info.get('favicon', 'N/A')
        if favicon != 'N/A' and len(favicon) > 50:
            favicon = favicon[:50] + "..." # Truncate long base64 strings
        print(f"  Favicon (base64, truncated): {favicon}")
        if 'sample' in server_info.get('players', {}) and server_info['players']['sample']:
            print("  Sample Players:")
            for player in server_info['players']['sample']:
                print(f"    - Name: {player.get('name', 'N/A')}, ID: {player.get('id', 'N/A')}")
        else:
            print("  Sample Players: N/A")

def print_bedrock_info(server_info, ip, port):
    if "error" in server_info:
        print(f"Error fetching Bedrock server info for {ip}:{port}:")
        print(f"  Type: {server_info['error']}")
        print(f"  Message: {server_info['message']}")
    else:
        print(f"Minecraft Bedrock Edition Server Info for {ip}:{port}:")
        print(f"  Version: {server_info.get('version', 'N/A')} (Protocol: {server_info.get('protocol', 'N/A')})")
        print(f"  Players: {server_info.get('online_players', 'N/A')}/{server_info.get('max_players', 'N/A')}")
        print(f"  Description Line 1: {server_info.get('motd1', 'N/A')}")
        print(f"  Description Line 2: {server_info.get('motd2', 'N/A')}")
        print(f"  Game Mode: {server_info.get('gamemode', 'N/A')} (ID: {server_info.get('gamemode_id', 'N/A')})")
        print(f"  Education Edition: {server_info.get('education_edition', 'N/A')}")

def main():
    parser = argparse.ArgumentParser(description="Scan Minecraft server status without Discord.")
    parser.add_argument("--ip", required=True, help="The IP address of the Minecraft server.")
    parser.add_argument("--port", type=int, help="The port of the Minecraft server. Defaults to 25565 for Java, 19132 for Bedrock.",
                        default=None)
    parser.add_argument("--edition", choices=["java", "bedrock"], default="java",
                        help="The edition of Minecraft server (java or bedrock). Defaults to 'java'.")

    args = parser.parse_args()

    ip = args.ip
    edition = args.edition

    if edition == "java":
        port = args.port if args.port is not None else 25565
        print(f"Scanning Java Edition server at {ip}:{port}...")
        info = get_java_server_info(ip, port)
        print_java_info(info, ip, port)
    elif edition == "bedrock":
        port = args.port if args.port is not None else 19132
        print(f"Scanning Bedrock Edition server at {ip}:{port}...")
        info = get_bedrock_server_info(ip, port)
        print_bedrock_info(info, ip, port)

if __name__ == "__main__":
    main()
