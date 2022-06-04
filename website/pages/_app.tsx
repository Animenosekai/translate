import '../styles/globals.css'

import type { AppProps } from 'next/app'
import { LanguageContextProvider } from 'contexts/language'
import { Layout } from 'components/common/layout'

function MyApp({ Component, pageProps }: AppProps) {
  return <LanguageContextProvider>
    <Layout>
      <Component {...pageProps} />
    </Layout>
  </LanguageContextProvider>
}

export default MyApp
