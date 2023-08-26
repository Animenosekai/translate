import { Card } from "@nextui-org/react"
import { ClientTranslationResult } from "types/translate";
import ContentLoader from "react-content-loader";
import { CopyIcon } from "components/icons/copy";
import { Service } from "lib/services"
import { ServiceElement } from "components/common/service"
import { TextToSpeechButton } from "../buttons/tts";
import { useLanguage } from "contexts/language";
import { useState } from "react";

export const SubResultLoader = (props) => {
    return <div className="w-1/3 mb-2 p-1 mx-1 min-w-[300px]">
        <Card clickable shadow={false}>
            <ContentLoader
                speed={2}
                height={70}
                viewBox="0 0 320 70"
                backgroundColor="#f3f3f3"
                foregroundColor="#ecebeb"
                {...props}
            >
                <rect x="0" y="0" rx="3" ry="3" width={180 + (Math.random() * 100)} height="20" />
                <rect x="0" y="50" rx="3" ry="3" width={80 + (Math.random() * 50)} height="20" />
            </ContentLoader>
        </Card>
    </div>
}

export const SubResult = ({ result, onCopyNotification, ...props }: {
    result?: ClientTranslationResult,
    onCopyNotification?: () => any
}) => {
    const { strings } = useLanguage();
    const [expanded, setExpanded] = useState<boolean>(false);
    const service = new Service(result.service)
    return <div className="w-1/4 p-1 mx-1 min-w-[300px]">
        <Card clickable={result ? true : false} shadow={false} className={result ? "opacity-100" : "opacity-50"}>
            <span onClick={() => { setExpanded(expanded => !expanded) }} className={expanded ? "h-max" : "max-h-[7.5rem]"}>
                {result ? result.translation : strings.labels.translationFailure}
            </span>
            <Card.Footer className="flex-start z-[2]">
                <ServiceElement service={service} />
                {
                    result
                        ? <div className="ml-auto flex flex-row space-x-2">
                            <TextToSpeechButton text={result.translation} source_lang={result.dest_lang} />
                            <CopyIcon onClick={(ev) => { navigator.clipboard.writeText(result.translation); onCopyNotification(); ev.stopPropagation(); }} className="opacity-70 hover:opacity-100 transition active:scale-95 cursor-pointer" />
                        </div>
                        : ""
                }
            </Card.Footer>
        </Card>
    </div>
}