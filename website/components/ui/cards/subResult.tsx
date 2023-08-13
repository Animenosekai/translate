import { Card } from "@nextui-org/react"
import ContentLoader from "react-content-loader";
import { CopyIcon } from "components/icons/copy";
import { Service } from "lib/services"
import { ServiceElement } from "components/common/service"
import { StarIcon } from "components/icons/star";
import { TTSButton } from "../buttons/tts";
import { TranslateRequest } from "types/translate"
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

export const SubResult = ({ result, onCopyNotification, starred, onStarChange, ...props }: {
    result: TranslateRequest,
    onCopyNotification?: () => any,
    starred?: boolean,
    onStarChange?: (translation: TranslateRequest, status: boolean) => any
}) => {
    const { strings } = useLanguage();
    const [expanded, setExpanded] = useState<boolean>(false);
    const service = new Service(result.data.service)
    return <div className="w-1/4 p-1 mx-1 min-w-[300px]">
        <Card clickable={result.success} shadow={false} className={result.success ? "opacity-100" : "opacity-50"}>
            <span onClick={() => { setExpanded(expanded => !expanded) }} className={expanded ? "h-max" : "max-h-[7.5rem]"}>
                {result.success ? result.data.result : strings.labels.translationFailure}
            </span>
            <Card.Footer className="flex-start z-[2]">
                <ServiceElement service={service} />
                {
                    result.success
                        ? <div className="ml-auto flex flex-row space-x-2">
                            <TTSButton text={result.data.result} sourceLang={result.data.destinationLanguage} />
                            <CopyIcon onClick={(ev) => { navigator.clipboard.writeText(result.data.result); onCopyNotification(); ev.stopPropagation(); }} className="opacity-70 hover:opacity-100 transition active:scale-95 cursor-pointer" />
                            {
                                (onStarChange)
                                    ? <StarIcon active={starred} onClick={() => { onStarChange(result, !starred) }} className="opacity-80 hover:opacity-100 transition active:scale-95 cursor-pointer" />
                                    : ""
                            }
                        </div>
                        : ""
                }
            </Card.Footer>
        </Card>
    </div>
}