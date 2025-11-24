# Frontend Installation Troubleshooting

## Common Issues and Solutions

### Issue 1: EACCES Permission Denied

**Error:**
```
npm error EACCES: permission denied, rename...
```

**Solutions:**

#### Option 1: Clear npm cache and reinstall (Recommended)
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Option 2: Fix npm permissions
```bash
# Fix ownership of npm directories
sudo chown -R $USER:$(id -gn $USER) ~/.npm
sudo chown -R $USER:$(id -gn $USER) $(pwd)

# Try installing again
npm install
```

#### Option 3: Use a different cache location
```bash
npm install --cache /tmp/npm-cache
```

#### Option 4: Run the setup script
```bash
chmod +x setup.sh
./setup.sh
```

### Issue 2: Deprecated Package Warnings

The warnings about deprecated packages are non-critical and expected:

**Why these warnings appear:**
- `eslint@8` - Next.js 15.1.3 requires ESLint 8. ESLint 9 would break compatibility.
- `inflight`, `rimraf`, `glob` - Transitive dependencies from Next.js that we don't control directly.
- `@humanwhocodes/*` - Transitive dependencies from ESLint.

**Solution:**
We've added `overrides` in package.json to force newer versions where possible. However, some warnings may persist due to Next.js requirements.

**Note:** These warnings are informational only and don't affect functionality. They will be resolved when Next.js upgrades to newer versions of these packages.

**To suppress warnings during install:**
```bash
npm install --legacy-peer-deps --silent
```

### Issue 3: Module Not Found After Installation

If you get "Module not found" errors:

```bash
# Clear Next.js cache
rm -rf .next

# Reinstall
npm install

# Start dev server
npm run dev
```

### Issue 4: Port Already in Use

If port 3000 is already in use:

```bash
# Use a different port
PORT=3001 npm run dev
```

Or kill the process using port 3000:
```bash
# Find process
lsof -ti:3000

# Kill it
kill -9 $(lsof -ti:3000)
```

## Quick Start (After Fixing Installation)

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Create environment file:**
   ```bash
   cp .env.local.example .env.local
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

4. **Open browser:**
   Navigate to http://localhost:3000

## Alternative: Use Yarn or pnpm

If npm continues to have issues, try an alternative package manager:

### Using Yarn:
```bash
# Install yarn (if not installed)
npm install -g yarn

# Install dependencies
yarn install

# Run dev server
yarn dev
```

### Using pnpm:
```bash
# Install pnpm (if not installed)
npm install -g pnpm

# Install dependencies
pnpm install

# Run dev server
pnpm dev
```

## System Requirements

- **Node.js**: 18.x or higher
- **npm**: 9.x or higher (or yarn/pnpm)
- **Operating System**: macOS, Linux, or Windows

## Verification

After successful installation, verify with:

```bash
# Check Node version
node --version  # Should be 18.x or higher

# Check npm version
npm --version   # Should be 9.x or higher

# Check if dependencies are installed
ls node_modules # Should show installed packages

# Try running dev server
npm run dev
```

## Still Having Issues?

1. **Update Node.js:**
   - Visit https://nodejs.org/
   - Download and install the latest LTS version

2. **Clear all caches:**
   ```bash
   npm cache clean --force
   rm -rf ~/.npm
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Check for conflicting global packages:**
   ```bash
   npm list -g --depth=0
   ```

4. **Try in a fresh terminal:**
   - Close and reopen your terminal
   - Ensure no old environment variables are set

## Contact

If issues persist, please check:
- The main README.md for general setup instructions
- Next.js documentation: https://nextjs.org/docs
- Node.js documentation: https://nodejs.org/docs
