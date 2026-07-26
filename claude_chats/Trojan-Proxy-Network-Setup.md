# Trojan Proxy Network Setup

- Source: https://claude.ai/share/cb6b3acb-540a-4c13-84ee-e0c093eb6a3f
- Author: myf
- Created: 2025-08-29
- Messages: 2

---

## Human

Give me step by step instructions on how to setup trojan client/server to bypass censorship. Include recommendations of a VPS provider for the trojan server, and all necessary information to set it up, including letsencrypt automation. Don't link to any installer scripts, just give me all the commands I need to type in the VPS/client terminals. Assume Ubuntu 22.04 for both client and server.

---

## Assistant

I'll help you set up a Trojan proxy for censorship circumvention. Trojan is a legitimate privacy tool that disguises traffic as HTTPS, making it effective against deep packet inspection.

## VPS Provider Recommendations

For reliable service with good global connectivity:
- **Vultr**: Excellent performance, multiple locations, £4-6/month for basic VPS
- **DigitalOcean**: Reliable, good documentation, similar pricing
- **Linode**: Strong performance, £5/month entry level
- **Hetzner**: Budget-friendly European option, £3-4/month

Choose a location geographically close to your actual location but outside censorship zones.

## Server Setup (Ubuntu 22.04)

### 1. Initial Server Preparation

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y wget curl nginx certbot python3-certbot-nginx ufw

# Configure firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### 2. Domain Setup

You'll need a domain name. Point it to your VPS IP address via DNS A record.

### 3. SSL Certificate with Let's Encrypt

```bash
# Configure nginx for your domain (replace example.com)
sudo nano /etc/nginx/sites-available/default
```

Replace the contents with:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

```bash
# Enable site and restart nginx
sudo nginx -t
sudo systemctl restart nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Set up auto-renewal
sudo crontab -e
```

Add this line to crontab:
```
0 12 * * * /usr/bin/certbot renew --quiet
```

### 4. Install Trojan-Go

```bash
# Download trojan-go
cd /tmp
wget https://github.com/p4gefau1t/trojan-go/releases/latest/download/trojan-go-linux-amd64.zip
unzip trojan-go-linux-amd64.zip

# Move binary
sudo mv trojan-go /usr/local/bin/
sudo chmod +x /usr/local/bin/trojan-go

# Create trojan user
sudo useradd -r -s /bin/false trojan

# Create directories
sudo mkdir -p /etc/trojan-go
sudo mkdir -p /var/log/trojan-go
sudo chown trojan:trojan /var/log/trojan-go
```

### 5. Configure Trojan-Go Server

```bash
# Create server config
sudo nano /etc/trojan-go/server.json
```

Insert this configuration (replace placeholders):
```json
{
    "run_type": "server",
    "local_addr": "0.0.0.0",
    "local_port": 443,
    "remote_addr": "127.0.0.1",
    "remote_port": 80,
    "password": ["YOUR_STRONG_PASSWORD_HERE"],
    "ssl": {
        "cert": "/etc/letsencrypt/live/your-domain.com/fullchain.pem",
        "key": "/etc/letsencrypt/live/your-domain.com/privkey.pem",
        "sni": "your-domain.com"
    },
    "websocket": {
        "enabled": true,
        "path": "/your-secret-path",
        "host": "your-domain.com"
    },
    "log_level": 1,
    "log_file": "/var/log/trojan-go/server.log"
}
```

### 6. Create Systemd Service

```bash
sudo nano /etc/systemd/system/trojan-go.service
```

Insert:
```ini
[Unit]
Description=Trojan-Go Server
After=network.target

[Service]
Type=simple
User=trojan
ExecStart=/usr/local/bin/trojan-go -config /etc/trojan-go/server.json
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### 7. Start Trojan Service

```bash
# Set permissions
sudo chown -R trojan:trojan /etc/trojan-go

# Start and enable service
sudo systemctl daemon-reload
sudo systemctl enable trojan-go
sudo systemctl start trojan-go

# Check status
sudo systemctl status trojan-go
```

### 8. Update Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/default
```

Replace with this fallback configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 127.0.0.1:80;
    server_name your-domain.com;
    root /var/www/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

```bash
sudo nginx -t
sudo systemctl restart nginx
```

## Client Setup (Ubuntu 22.04)

### 1. Install Trojan-Go Client

```bash
# Download and install
cd /tmp
wget https://github.com/p4gefau1t/trojan-go/releases/latest/download/trojan-go-linux-amd64.zip
unzip trojan-go-linux-amd64.zip
sudo mv trojan-go /usr/local/bin/
sudo chmod +x /usr/local/bin/trojan-go

# Create directories
mkdir -p ~/.config/trojan-go
```

### 2. Create Client Configuration

```bash
nano ~/.config/trojan-go/client.json
```

Insert:
```json
{
    "run_type": "client",
    "local_addr": "127.0.0.1",
    "local_port": 1080,
    "remote_addr": "your-domain.com",
    "remote_port": 443,
    "password": ["YOUR_STRONG_PASSWORD_HERE"],
    "ssl": {
        "sni": "your-domain.com"
    },
    "websocket": {
        "enabled": true,
        "path": "/your-secret-path",
        "host": "your-domain.com"
    },
    "log_level": 1
}
```

### 3. Run Client

```bash
# Test connection
trojan-go -config ~/.config/trojan-go/client.json

# Create systemd service (optional)
sudo nano /etc/systemd/system/trojan-client.service
```

Service file content:
```ini
[Unit]
Description=Trojan-Go Client
After=network.target

[Service]
Type=simple
User=%i
ExecStart=/usr/local/bin/trojan-go -config /home/%i/.config/trojan-go/client.json
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### 4. Configure System Proxy

After starting the client, configure your applications to use SOCKS5 proxy at `127.0.0.1:1080`.

## Security Recommendations

1. **Use strong passwords**: Generate a long, random password for authentication
2. **Keep certificates updated**: Let's Encrypt handles this automatically
3. **Monitor logs**: Check `/var/log/trojan-go/server.log` regularly
4. **Update regularly**: Keep trojan-go updated to the latest version
5. **Firewall rules**: Only allow necessary ports

## Testing Connection

```bash
# Test SOCKS5 proxy (with client running)
curl --socks5 127.0.0.1:1080 https://httpbin.org/ip
```

This setup creates a robust censorship circumvention tool. Remember to comply with local laws and use responsibly. The Trojan protocol's strength lies in its ability to appear as regular HTTPS traffic, making detection difficult whilst maintaining good performance.
