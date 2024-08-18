export default function RootLayout({
  children,
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Blog</title>
      </head>
      <body>
        <div id="root">{children}</div>
        <script type="module" src="/api-frontend/src/index.js"></script>
      </body>
    </html>
  )
}