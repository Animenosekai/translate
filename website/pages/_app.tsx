import '../styles/globals.css'

import type { AppProps } from 'next/app'
import { HeadingsContextProvider } from 'contexts/headings'
import { LanguageContextProvider } from 'contexts/language'
import { Layout } from 'components/common/layout'

function MyApp({ Component, pageProps }: AppProps) {
  return <LanguageContextProvider>
    <HeadingsContextProvider>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </HeadingsContextProvider>
  </LanguageContextProvider>
}

export default MyApp
