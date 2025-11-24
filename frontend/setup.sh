#!/bin/bash

# Frontend Setup and Installation Script
# This script helps resolve npm installation issues

echo "🔧 Frontend Setup Script"
echo "======================="
echo ""

# Check if we're in the frontend directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: package.json not found. Please run this script from the frontend directory."
    exit 1
fi

echo "📦 Step 1: Cleaning npm cache..."
npm cache clean --force

echo ""
echo "🗑️  Step 2: Removing node_modules and package-lock.json..."
rm -rf node_modules package-lock.json

echo ""
echo "📥 Step 3: Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installation successful!"
    echo ""
    echo "You can now run:"
    echo "  npm run dev    - Start development server"
    echo "  npm run build  - Build for production"
    echo "  npm run lint   - Run linter"
else
    echo ""
    echo "❌ Installation failed. Please try one of these solutions:"
    echo ""
    echo "1. Run with sudo (if permission issues):"
    echo "   sudo npm install"
    echo ""
    echo "2. Fix npm permissions:"
    echo "   sudo chown -R \$USER:\$(id -gn \$USER) ~/.npm"
    echo "   sudo chown -R \$USER:\$(id -gn \$USER) ~/lexiden-tech-challenge/frontend"
    echo ""
    echo "3. Use a different npm cache:"
    echo "   npm install --cache /tmp/npm-cache"
    echo ""
    exit 1
fi
