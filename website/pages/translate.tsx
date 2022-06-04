import { MainResult, MainResultCard } from 'components/ui/cards/mainResult'
import { SubResult, SubResultLoader } from 'components/ui/cards/subResult'

import Head from 'next/head'
import type { NextPage } from 'next'
import { TranslateRequest } from 'types/translate'
import { useState } from 'react'

const Translate: NextPage = () => {
    const [toLoad, setToLoad] = useState(4);
    const test: TranslateRequest = {
        success: true,
        message: "",
        error: null,
        data: {
            service: "Google",
            source: "Hello World",
            sourceLang: "eng",
            destLang: "jpa",
            result: "こんにちは世界"
        }

    }
    return <div className='h-full'>
        <Head>
            <title>translate — Use multiple services to translate your texts!</title>
            <meta name="description" content="Use multiple services to translate your texts!" />
            <link rel="icon" href="/favicon.ico" />
        </Head>
        <div className="p-16">
            <MainResult result={test} />
            <div className="mx-3 mt-16 w-full">
                <h2 className="font-semibold text-xl mb-5">Other translations</h2>
                <div className='flex flex-row flex-wrap w-3/4'>
                    <SubResult result={test} />
                    {
                        Array(toLoad).fill(0).map((_, i) => <SubResultLoader key={i} />)
                    }
                </div>
            </div>
        </div>
    </div>
}

export default Translate
