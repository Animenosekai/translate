import { Card, CardBody, CardFooter } from "@nextui-org/card";

import { ClientTranslationResult } from "types/translate";
import ContentLoader from "react-content-loader";
import { CopyIcon } from "components/icons/copy";
import { Service } from "lib/services"
import { ServiceElement } from "components/common/service"
import { TextToSpeechButton } from "../buttons/tts";
import classNames from "classnames";
import { useLanguage } from "contexts/language";
import { useState } from "react";

export const SubResultLoader = (props) => {
    return <Card isPressable className="p-2 mx-1 min-w-[200px] flex-grow">
        <CardBody className="p-3">
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
        </CardBody>
    </Card>
}

export const SubResult = ({ result, onCopyNotification, ...props }: {
    result?: ClientTranslationResult,
    onCopyNotification?: () => any
}) => {
    const { strings } = useLanguage();
    const [expanded, setExpanded] = useState<boolean>(false);
    const service = new Service(result ? result.service : "")
    return <Card isPressable={result ? true : false} className={classNames({
        "opacity-100": result,
        "opacity-50": !result
    }, "p-2 mx-1 min-w-[200px] flex-grow")} allowTextSelectionOnPress>
        <CardBody className={classNames({
            "h-max": expanded,
            "max-h-[7.5rem]": !expanded
        }, "p-3")} onClick={() => { setExpanded(expanded => !expanded) }}>
            {result
                ? result.translation
                : strings.labels.translationFailure}
        </CardBody>
        <CardFooter className="flex-start z-[2]">
            <ServiceElement service={service} />
            {
                result
                    ? <div className="ml-auto flex flex-row space-x-2">
                        <TextToSpeechButton text={result.translation} source_lang={result.dest_lang} />
                        <CopyIcon onClick={(ev) => {
                            navigator.clipboard.writeText(result.translation);
                            if (onCopyNotification) {
                                onCopyNotification();
                            }
                            ev.stopPropagation();
                        }} className="opacity-70 hover:opacity-100 transition active:scale-95 cursor-pointer" />
                    </div>
                    : ""
            }
        </CardFooter>
    </Card>
}