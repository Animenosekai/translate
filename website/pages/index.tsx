import { Button } from '@nextui-org/button'
import { LanguageIcon } from 'components/icons/language'
import type { NextPage } from 'next'
import { SEO } from 'components/common/seo'
import { TranslationTextArea } from 'components/ui/textareas/translation'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'
import { useState } from 'react'

const Home: NextPage = () => {
    const { strings } = useLanguage();
    const [text, setText] = useState<string>("");
    const router = useRouter();

    const translate = () => {
        router.push(`/translate?text=${encodeURIComponent(text)}&dest_lang=${strings.language}`)
    }

    return <div className='h-full'>
        <SEO description='Use multiple services to translate your texts!' />

        <div className="flex items-center flex-col md:w-1/2 w-3/4 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 -mt-10">
            <LanguageIcon size={100} />
            <div className='w-full flex items-end flex-col'>
                <TranslationTextArea onKeyDown={(ev) => {
                    if ((ev.key === "Enter" || ev.keyCode === 13) && !ev.shiftKey) {
                        translate()
                        ev.preventDefault()
                        return false
                    }
                }} onChange={el => setText(el.target.value)} />
                <Button onClick={translate} type="submit" color={text ? "primary" : "default"} disabled={text ? false : true} variant='flat'>{strings.buttons.translate}</Button>
            </div>
        </div>
    </div>
}

export default Home
