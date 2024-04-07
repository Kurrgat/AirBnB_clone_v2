#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

set -e  # Exit on error

echo "Updating packages..."
sudo apt-get update

echo "Installing Nginx..."
sudo apt-get -y install nginx

echo "Allowing Nginx through firewall..."
sudo ufw allow 'Nginx HTTP'

echo "Creating necessary directories..."
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "Populating index.html with content..."
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

echo "Creating or recreating symbolic link..."
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

echo "Setting ownership of /data/..."
sudo chown -R ubuntu:ubuntu /data/

echo "Updating Nginx configuration..."
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

echo "Restarting Nginx..."
sudo service nginx restart

echo "Web server setup completed successfully."
