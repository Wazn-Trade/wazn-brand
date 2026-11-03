# wazn-brand

هوية **Wazn — وزن** الكاملة: اللوجوهات، والألوان، والخطوط، والمكوّنات، ودليل البراند.

افتح `index.html` في المتصفح، هتلاقي معرض كامل يشتغل من غير إنترنت، وفيه زرار للتبديل بين الثيم الفاتح (Ivory) والغامق (Night).

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
