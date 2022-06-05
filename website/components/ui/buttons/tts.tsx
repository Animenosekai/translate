import { useEffect, useState } from "react";

import { LanguageDetailsResult } from "types/languageDetails";
import { TTSIcon } from "components/icons/tts";
import { TTSRequest } from "types/tts";
import { request } from "lib/request";

export const TTSButton = ({ text, sourceLang, ...props }: { text: string, sourceLang: LanguageDetailsResult }) => {
    const [tts, setTTS] = useState(false);
    const [audio, setAudio] = useState<HTMLAudioElement>(null);

    useEffect(() => {
        if (!audio) { return }
        audio.play();
    }, [audio])

    useEffect(() => {
        if (tts) {
            request<TTSRequest>("/tts", {
                params: {
                    text: text,
                    lang: sourceLang.id
                }
            })
                .then(response => {
                    if (!response.success) { return }
                    const buffer = Buffer.from(response.data.base64, 'base64')
                    const blob = new Blob([buffer])
                    setAudio(new Audio(URL.createObjectURL(blob)))
                })
            setTTS(false);
        }
    }, [tts]);
    return <button className="opacity-70 hover:opacity-100 transition active:scale-95" onClick={(ev) => { setTTS(true); ev.stopPropagation(); }}>
        <TTSIcon />
    </button>
}