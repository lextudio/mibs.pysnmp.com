sudo apt update
sudo apt upgrade
sudo ./deploy.sh


Verify nginx configuration
sudo nginx -t
cat /etc/nginx/nginx.conf
ls /etc/nginx/sites-available
cat /etc/nginx/sites-available/mibs.pysnmp.com

Restart nginx
sudo systemctl restart nginx
