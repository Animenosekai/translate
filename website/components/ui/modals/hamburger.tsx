import { useEffect, useState } from "react";

import { CloseIcon } from "components/icons/close";
import Link from "next/link";
import { TOC } from "pages/documentation/[...path]";
import classNames from "classnames";
import { useLanguage } from "contexts/language";
import { useRouter } from "next/router";

export const HamburgerMenuElement = ({ href, name, ...props }: any) => {
    return <Link passHref={true} href={href}>
        <a>
            <div className="w-full h-16 p-5 text-xl items-center flex cursor-pointer hover:bg-slate-100 transition" {...props}>
                {name}
            </div>
        </a>
    </Link>
}

export const HamburgerModal = ({ onClose, ...props }) => {
    const { strings } = useLanguage();
    const [exit, setExit] = useState(true);
    const { pathname } = useRouter();
    const [showTOC, setShowTOC] = useState(false);

    useEffect(() => {
        if (["/documentation", "/documentation/[...path]"].includes(pathname)) {
            setShowTOC(true);
        } else {
            setShowTOC(false);
        }
    }, [pathname])

    useEffect(() => {
        setExit(false);
    }, [])

    const clickHandler = () => { setExit(true); setTimeout(onClose, 300); }
    return <div onClick={clickHandler} className={classNames(
        "h-screen transition-all duration-300 w-screen fixed bg-white z-10 sm:hidden",
        {
            "bg-opacity-40": !exit,
            "bg-opacity-0": exit
        }
    )}>
        <div onClick={(ev) => ev.stopPropagation()} className={classNames(
            "h-screen transition-all duration-300 w-4/5 z-20 top-0 right-0 fixed bg-white shadow-xl flex flex-col space-y-5 items-center sm:hidden",
            {
                "opacity-100": !exit,
                "opacity-0": exit,
                "translate-x-0": !exit,
                "translate-x-full": exit,
                // "animate-exit-menu": exit,
                // "animate-enter-menu": !exit
            }
        )} >
            <CloseIcon className="absolute top-0 right-0 mx-10 my-5 cursor-pointer opacity-60 hover:opacity-100 transition" onClick={clickHandler} />
            {/* <span className="text-xl justify-center">Menu</span> */}
            <div className="h-12"></div>
            <div className="w-full overflow-y-auto">
                <hr />
                <HamburgerMenuElement onClick={clickHandler} href="/translate" name={strings.pages.translate} />
                <hr />
                <HamburgerMenuElement onClick={clickHandler} href="/documentation" name={strings.pages.documentation} />
                {
                    showTOC && <TOC onClick={clickHandler} className="ml-6" />
                }
                <hr />
                <HamburgerMenuElement onClick={clickHandler} href="/stats" name={strings.pages.stats} />
                <hr />
            </div>
            <div></div>
            <span>🧃 Anime no Sekai, 2022</span>
        </div>
    </div>
}