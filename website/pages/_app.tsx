import '../styles/globals.css'

import type { AppProps } from 'next/app'
import { LanguageContextProvider } from 'contexts/language'
import { Layout } from 'components/common/layout'
import { ServicesColorContextProvider } from 'contexts/servicesColor'

function MyApp({ Component, pageProps }: AppProps) {
  return <LanguageContextProvider>
    <ServicesColorContextProvider>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </ServicesColorContextProvider>
  </LanguageContextProvider>
}

export default MyApp
