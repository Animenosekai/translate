import { Button } from '@nextui-org/react'
// import { Button } from 'components/ui/buttons/button'
import Head from 'next/head'
import { LanguageIcon } from 'components/icons/language'
import type { NextPage } from 'next'
import { TranslationTextArea } from 'components/ui/textareas/translation'
import { useRouter } from 'next/router'
import { useState } from 'react'

const Home: NextPage = () => {
    const [text, setText] = useState<string>(null);
    const router = useRouter();
    return <div className='h-full'>
        <Head>
            <title>translate — Use multiple services to translate your texts!</title>
            <meta name="description" content="Use multiple services to translate your texts!" />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <div className="flex items-center flex-col w-1/2 h-full justify-center mx-auto -mt-20">
            <LanguageIcon size={100} />
            <div className='w-full flex items-end flex-col'>
                <TranslationTextArea onChange={el => setText(el.target.value)} />
                <Button onClick={() => {
                    router.push("/translate")
                }} hidden={text ? false : true} disabled={text ? false : true} auto flat>Translate</Button>
            </div>
        </div>

    </div>
}

export default Home
