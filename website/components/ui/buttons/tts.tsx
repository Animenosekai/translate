import { useEffect, useState } from "react";

import Configuration from "config";
import { Language } from "types/language";
import { TextToSpeechIcon } from "components/icons/tts";

export const TextToSpeechButton = ({ text, source_lang, ...props }: { text: string, source_lang: Language }) => {
    const [tts, setTextToSpeech] = useState(false);
    const [audio, setAudio] = useState<HTMLAudioElement | undefined>(undefined);

    useEffect(() => {
        if (!audio) { return }
        audio.play();
    }, [audio])

    useEffect(() => {
        if (tts) {
            setAudio(new Audio(`${Configuration.request.host}/tts?text=${encodeURIComponent(text)}&lang=${encodeURIComponent(source_lang.id)}&raw=true`))
            setTextToSpeech(false);
            // request<Request<TextToSpeechResult>>("/tts", {
            //     params: {
            //         text: text,
            //         lang: source_lang.id
            //     }
            // })
            //     .then(response => {
            //         if (!response.success) { return }
            //         const buffer = Buffer.from(response.data.result, 'base64')
            //         const blob = new Blob([buffer])
            //         setAudio(new Audio(URL.createObjectURL(blob)))
            //     })
            // setTextToSpeech(false);
        }
    }, [tts]);
    return <button className="opacity-70 hover:opacity-100 transition active:scale-95" onClick={(ev) => { setTextToSpeech(true); ev.stopPropagation(); }}>
        <TextToSpeechIcon />
    </button>
}