#\!/bin/bash
# Copy the built index.html and update asset paths for the server

# Create a copy of the original index.html
cp dist/index.html dist/index.server.html

# Update the paths in the server version
sed -i '' 's|"/assets/|"/static/assets/|g' dist/index.server.html

echo "Created dist/index.server.html with server-compatible paths"
echo "Copy this file to frontend/index.html to update the server version"
