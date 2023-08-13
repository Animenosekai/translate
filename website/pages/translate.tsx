import { DefaultTranslateRequest, TranslateRequest } from 'types/translate'
import { SubResult, SubResultLoader } from 'components/ui/cards/subResult'
import { useEffect, useState } from 'react'

import Configuration from 'config'
import { CopyNotification } from 'components/ui/notifications/copy'
import { MainResult } from 'components/ui/cards/mainResult'
import type { NextPage } from 'next'
import { SEO } from 'components/common/seo'
import { StarRequest } from 'types/stars'
import { generateRandomID } from 'utils/random'
import { request } from 'lib/request'
import { services } from 'lib/services'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'

const Translate: NextPage = () => {
    const { strings } = useLanguage();
    const router = useRouter();
    const [toLoad, setToLoad] = useState(Object.keys(services).length);
    const [results, setResults] = useState<TranslateRequest[]>([DefaultTranslateRequest]);
    const [starred, setStarred] = useState<string[]>([]);

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
        text: URLParams.get("text"),
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
            setResults([{ ...DefaultTranslateRequest, loading: true, data: { ...DefaultTranslateRequest.data, source: currentTranslation.text } }])
            setToLoad(Object.keys(services).length);
            stream.onmessage = (event) => {
                if (!event) {
                    stream.close();
                    return
                }
                const data = JSON.parse(event.data)

                if (data?.data?.starred) {
                    setStarred(starred => [...starred.filter(val => val !== data.data.translationID), data.data.translationID])
                }
                
                setResults(results => {
                    const success = results.filter((val) => val.success)
                    const failed = results.filter((val) => !val.success)

                    if (success.length === 0) {
                        data.data.source = currentTranslation.text
                    }

                    if (results.length > 0) {
                        if (results[0].loading) {
                            return [data]
                        } else if (!results[0].success) {
                            return [data, ...results]
                        }
                    }
                    // return [...results, data]
                    return [...success, data, ...failed]
                })
                setToLoad(toLoad => toLoad - 1)
            }
            stream.onerror = (event) => {
                if (event.eventPhase === EventSource.CLOSED) {
                    stream.close();
                }
            }
        }, 200)
    }, [streamID]);

    useEffect(() => {
        if (!currentTranslation.text) { return }
        router.push(`/translate?text=${encodeURIComponent(currentTranslation.text)}&source=${encodeURIComponent(currentTranslation.source)}&dest=${encodeURIComponent(currentTranslation.dest)}`, undefined, { shallow: true })
        const currentID = generateRandomID(12);
        setStreamID(currentID);
    }, [currentTranslation])


    const [showCopyNotification, setShowCopyNotification] = useState(false);
    const [notificationTimeout, setNotificationTimeout] = useState(null);

    const copyNotificationDuration = 3000

    useEffect(() => {
        if (showCopyNotification) {
            clearTimeout(notificationTimeout);
            setNotificationTimeout(setTimeout(() => {
                setShowCopyNotification(false);
            }, copyNotificationDuration))
        }
    }, [showCopyNotification])

    const showCopyNotificationHandler = () => {
        setShowCopyNotification(true);
    }

    const onStarChange = (translation: TranslateRequest, star: boolean) => {
        setStarred(starred => {
            return star ? [...starred.filter(val => val !== translation.data.translationID), translation.data.translationID] : starred.filter(val => val !== translation.data.translationID)
        })

        request<StarRequest>("/stars/" + translation.data.translationID, {
            method: star ? "POST" : "DELETE",
            params: star ? {
                token:  translation.data.token
            } : {}
        })
            .then(response => {
                if (!response.success) {
                    setStarred(starred => {
                        return star ? [...starred.filter(val => val !== translation.data.translationID), translation.data.translationID] : starred.filter(val => val !== translation.data.translationID)
                    })
                }
            })
            .catch(error => {
                setStarred(starred => {
                    return star ? [...starred.filter(val => val !== translation.data.translationID), translation.data.translationID] : starred.filter(val => val !== translation.data.translationID)
                })
                console.error("Error starring translation", error)
            })
    }
    return <div className='h-full'>
        <SEO title={`translation from ${currentTranslation.source} to ${currentTranslation.dest}`} description='Use multiple services to translate your texts!' />
        {
            showCopyNotification && <CopyNotification duration={copyNotificationDuration} />
        }
        <div className="sm:p-16 p-5">
            {
                (results.length > 0 && results[0].success)
                    ? <MainResult
                        onCopyNotification={showCopyNotificationHandler}
                        onNewTranslation={setCurrentTranslation}
                        starred={starred.includes(results[0].data.translationID)}
                        onStarChange={onStarChange}
                        result={results[0]} />
                    : <MainResult
                        onCopyNotification={showCopyNotificationHandler}
                        onNewTranslation={setCurrentTranslation}
                        result={
                            {
                                ...DefaultTranslateRequest,
                                data: { ...DefaultTranslateRequest.data, source: currentTranslation.text }
                            }
                        } />
            }
            <div className="mx-3 mt-16">
                <h2 className="font-semibold text-xl mb-5">{strings.heading.otherTranslations}</h2>
                <div className='flex flex-row flex-wrap w-full justify-center md:justify-start'>
                    {
                        results.slice(1).map((result, index) => {
                            return <SubResult
                                starred={starred.includes(result.data.translationID)}
                                onStarChange={onStarChange}
                                onCopyNotification={showCopyNotificationHandler}
                                key={index}
                                result={result}
                            />
                        })
                    }
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
