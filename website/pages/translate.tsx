import { MainResult, MainResultCard, MainResultLoader } from 'components/ui/cards/mainResult'
import { SubResult, SubResultLoader } from 'components/ui/cards/subResult'
import { useEffect, useState } from 'react'

import Configuration from 'config'
import Head from 'next/head'
import type { NextPage } from 'next'
import { TranslateRequest } from 'types/translate'
import { generateRandomID } from 'utils/random'
import { services } from 'lib/services'
import { useLanguage } from 'contexts/language'

const Translate: NextPage = () => {
    const { strings } = useLanguage();
    const [toLoad, setToLoad] = useState(Object.keys(services).length);
    const [results, setResults] = useState<TranslateRequest[]>([]);
    let URLParams: URLSearchParams
    if (typeof window !== "undefined") {
        URLParams = new URLSearchParams(location.search);
    } else {
        URLParams = new URLSearchParams();
    }
    const [currentTranslation, setCurrentTranslation] = useState<{
        text: string,
        source: string,
        dest: string
    }>({
        text: URLParams.get("text") || "Hello world",
        source: URLParams.get("source") || "auto",
        dest: URLParams.get("dest") || "eng"
    })
    const [streamID, setStreamID] = useState(null);

    useEffect(() => {
        const currentID = streamID;
        setTimeout(() => {
            if (!currentID || currentID != streamID) { return }
            console.log("Connecting to stream...", currentID, streamID);
            console.log(`Translate: ${currentTranslation.text} from ${currentTranslation.source} to ${currentTranslation.dest}`);
            const stream = new EventSource(`${Configuration.request.host}/stream?text=${encodeURIComponent(currentTranslation.text)}&dest=${currentTranslation.dest}&source=${currentTranslation.source}`)
            setResults([])
            setToLoad(Object.keys(services).length);
            stream.onmessage = (event) => {
                if (!event) {
                    stream.close();
                    return
                }
                const data = JSON.parse(event.data)
                setResults(results => {
                    if (results.length > 0 && !results[0].success) {
                        return [data, ...results]
                    }
                    return [...results, data]
                })
                setToLoad(toLoad => toLoad - 1)
            }
            stream.onerror = (event) => {
                if (event.eventPhase === EventSource.CLOSED) {
                    stream.close();
                }
            }
        }, 1000)
    }, [streamID]);

    useEffect(() => {
        const currentID = generateRandomID(12);
        setStreamID(currentID);
    }, [currentTranslation])

    return <div className='h-full'>
        <Head>
            <title>translate — Use multiple services to translate your texts!</title>
            <meta name="description" content="Use multiple services to translate your texts!" />
            <link rel="icon" href="/favicon.ico" />
        </Head>
        <div className="p-16">
            {
                (results.length > 0 && results[0].success)
                    ? <MainResult onNewTranslation={setCurrentTranslation} result={results[0]} />
                    : <MainResultLoader />
            }
            <div className="mx-3 mt-16">
                <h2 className="font-semibold text-xl mb-5">{strings.heading.otherTranslations}</h2>
                <div className='flex flex-row flex-wrap w-full'>
                    {results.slice(1).map((result, index) => <SubResult key={index} result={result} />)}
                    {
                        toLoad > 0
                            ? Array(toLoad).fill(0).map((_, i) => <SubResultLoader key={i} />)
                            : ""
                    }
                </div>
            </div>
        </div>
    </div>
}

export default Translate
