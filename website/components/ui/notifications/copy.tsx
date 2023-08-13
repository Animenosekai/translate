import { useEffect, useState } from "react";

import { ClipboardOkIcon } from "components/icons/clipboard";
import classNames from "classnames";
import { useLanguage } from "contexts/language";

export const CopyNotification = ({ duration }: { duration?: number }) => {
    const { strings } = useLanguage();
    const [show, setShow] = useState(false);

    useEffect(() => {
        setShow(true);
        setTimeout(() => {
            setShow(false);
        }, duration ? duration - 1000 : 3000);
    }, [])

    return <div className="w-screen h-screen fixed flex z-40 justify-center pointer-events-none">
        <div className={classNames(
            "fixed text-white p-4 text-lg rounded items-center flex cursor-pointer bg-[#0072F5] transition-all duration-500 space-x-2",
            {
                "opacity-100": show,
                "bottom-4": show,
                "opacity-0": !show,
                "-bottom-16": !show
            }
        )}>
            <span>{strings.notifications.copied}</span>
            <ClipboardOkIcon />
        </div>
    </div>
}