import { Button } from '@nextui-org/react'
// import { Button } from 'components/ui/buttons/button'
import Head from 'next/head'
import { LanguageIcon } from 'components/icons/language'
import type { NextPage } from 'next'
import { TranslationTextArea } from 'components/ui/textareas/translation'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'
import { useState } from 'react'

const Home: NextPage = () => {
    const { strings } = useLanguage();
    const [text, setText] = useState<string>(null);
    const router = useRouter();

    const translate = () => {
        router.push(`/translate?text=${encodeURIComponent(text)}&dest=${strings.language}`)
    }

    return <div className='h-full'>
        <Head>
            <title>translate — Use multiple services to translate your texts!</title>
            <meta name="description" content="Use multiple services to translate your texts!" />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <div className="flex items-center flex-col md:w-1/2 w-3/4 h-full justify-center mx-auto -mt-20">
            <LanguageIcon size={100} />
            <div className='w-full flex items-end flex-col'>
                <TranslationTextArea onKeyDown={(ev) => {
                    if ((ev.key === "Enter" || ev.keyCode === 13) && !ev.shiftKey) {
                        translate()
                        ev.preventDefault()
                        return false
                    }
                }} onChange={el => setText(el.target.value)} />
                <Button onClick={translate} type="submit" hidden={text ? false : true} disabled={text ? false : true} auto flat>{strings.buttons.translate}</Button>
            </div>
        </div>

    </div>
}

export default Home
