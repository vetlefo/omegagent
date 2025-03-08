##############################
# 1) Redirect HTTP to HTTPS
##############################
server {
    listen 80;
    server_name singularity.wondercode.ai;
    
    # Redirect all requests on port 80 to HTTPS
    return 301 https://$host$request_uri;
}

##############################
# 2) HTTPS Reverse Proxy
##############################
server {
    listen 443 ssl;
    server_name singularity.wondercode.ai;

    # SSL certificate and key (these paths are examples from Certbot—adjust if different)
    ssl_certificate /etc/letsencrypt/live/singularity.wondercode.ai/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/singularity.wondercode.ai/privkey.pem;

    # Your reverse proxy to the huly app on port 1234 (adjust to your actual port)
    location / {
        proxy_pass http://127.0.0.1:1234;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}