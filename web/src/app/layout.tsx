import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'BotiFutbol - Fútbol en tiempo real',
  description: 'Noticias, estadísticas, partidos en vivo y competiciones de fútbol',
  manifest: '/manifest.json',
  icons: {
    icon: '/logo.png',
    apple: '/icon-192.png',
  },
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'BotiFutbol',
  },
  openGraph: {
    title: 'BotiFutbol - Fútbol en tiempo real',
    description: 'Seguí tus equipos, recibí notificaciones y competí con amigos',
    images: ['/logo.png'],
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head>
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        <meta name="theme-color" content="#0F172A" />
        <link rel="apple-touch-startup-image" href="/icon-512.png" />
      </head>
      <body className="min-h-screen bg-dark">
        {children}
        <script dangerouslySetInnerHTML={{
          __html: `
            if ('serviceWorker' in navigator) {
              window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
              })
            }
          `
        }} />
      </body>
    </html>
  )
}
