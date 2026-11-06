# wazn-brand

هوية **Wazn — وزن** الكاملة: اللوجوهات، والألوان، والخطوط، والمكوّنات، ودليل البراند.

افتح `index.html` في المتصفح، هتلاقي معرض كامل يشتغل من غير إنترنت، وفيه زرار للتبديل بين الثيم الفاتح (Paper) والغامق (Graphite).

| المسار | المحتوى |
| --- | --- |
| `BRAND_BOOK.md` | دليل البراند: الفكرة، والنبرة، واللوجو، والألوان، والخطوط، وعائلة المنتجات، وقيود التسمية |
| `logos/svg/` | 16 ملف SVG متحوّلين لأشكال (outlined)، ومش محتاجين أي خط |
| `logos/png/` | نسخ PNG بخلفية شفافة (عرض 1600)، وأيقونة التطبيق 1024/512، والـ favicon بأحجام 32/64/180/512 |
| `design-system/tokens.json` | المصدر الأساسي لكل القيم (ألوان بثيمين، وخطوط، ومسافات، وزوايا، وظل) |
| `design-system/tokens.css` | نفس القيم كـ CSS variables، جاهزة للاستخدام في أي موقع أو dashboard |
| `design-system/components/` | `bundle.css` (كلاسات `wz-`)، ومع كل مكوّن preview وREADME |
| `fonts/` | Readex Pro وIBM Plex Sans Arabic وIBM Plex Mono بصيغة woff2، ومعاها الرخص (SIL OFL) |
| `tools/` | سكريبتات بتولّد كل اللوجوهات من الكود، وكمان معرض `index.html` |

## الاستخدام في أي مشروع

```html
<link rel="stylesheet" href="design-system/tokens.css">
<link rel="stylesheet" href="design-system/components/bundle.css">
<html data-theme="light">  <!-- أو dark -->
<button class="wz-btn wz-btn--primary">اعتماد</button>
<span class="wz-badge wz-badge--compliant">متوافق</span>
```

النسخة الحية من الـ design system موجودة على Claude باسم «Wazn». الفولدر ده نسخة كاملة منها.

## Installing as `@wazn-trade/brand` from GitHub Packages

`@wazn-trade/brand` is published to GitHub Packages (not npmjs) under the
`Wazn-Trade` org. Access needs a PAT or `GITHUB_TOKEN` with `read:packages`.
The npm scope `@wazn-trade` matches the GitHub org (lower-cased).

### 1. Authenticate npm against the GH Packages registry

Create `~/.npmrc` (or set it in CI):

```ini
@wazn-trade:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
```

In GitHub Actions:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: "20"
    registry-url: "https://npm.pkg.github.com"
    scope: "@wazn-trade"
- run: npm ci
  env: { NODE_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
```

### 2. Install

```bash
npm install @wazn-trade/brand
```

### 3. Consume

Pick the imports your tooling supports. The package exposes everything through
the `exports` map in `package.json`:

```html
<!-- Static HTML (wazn-site, wazn-docs deck): copy at build time. -->
<link rel="stylesheet" href="/node_modules/@wazn-trade/brand/design-system/tokens.css">
<link rel="stylesheet" href="/node_modules/@wazn-trade/brand/design-system/components/bundle.css">
```

```js
// Bundlers (Vite, esbuild): subpath imports.
import "@wazn-trade/brand/tokens.css";
import "@wazn-trade/brand/components.css";
import tokens from "@wazn-trade/brand/tokens.json";
```

```js
// SVG logos and raw fonts.
import logoAr from "@wazn-trade/brand/logos/wazn-logo-ar.svg";
```

### 4. Keep the version pinned

Commit `package-lock.json`. Bumping `@wazn-trade/brand` is a deliberate design-system
promotion — treat it like any other breaking library change.

### 5. Publishing (maintainers only)

```bash
# After updating "version" in package.json and committing:
git tag v0.1.0
git push origin v0.1.0
```

The `Publish @wazn-trade/brand` workflow runs on `v*` tags and pushes to GitHub
Packages. The committed `package.json` keeps `"private": true`; the workflow
flips it in CI only, after asserting the tag matches the version.
