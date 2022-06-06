import { CloseIcon } from "components/icons/close";
import Link from "next/link";
import { useLanguage } from "contexts/language";

export const HamburgerMenuElement = ({ href, name, ...props }: any) => {
    return <div className="w-full h-16 p-5 text-xl items-center flex cursor-pointer hover:bg-slate-100 transition" {...props}>
        <Link href={href}>
            {name}
        </Link>
    </div>
}

export const HamburgerModal = ({ onClose, ...props }) => {
    const { strings } = useLanguage();
    return <div className="h-screen animate-enter-menu w-4/5 z-10 right-0 absolute bg-white shadow-xl flex flex-col space-y-5 items-center sm:hidden">
        <CloseIcon className="absolute top-0 right-0 mx-10 cursor-pointer opacity-60 hover:opacity-100 transition" onClick={() => { onClose(); }} />
        {/* <span className="text-xl justify-center">Menu</span> */}
        <div className="h-5"></div>
        <div className="w-full">
            <hr />
            <HamburgerMenuElement onClick={onClose} href="/translate" name={strings.pages.translate} />
            <hr />
            <HamburgerMenuElement onClick={onClose} href="/documentation" name={strings.pages.documentation} />
            <hr />
            <HamburgerMenuElement onClick={onClose} href="/stats" name={strings.pages.stats} />
            <hr />
        </div>
        <div></div>
        <span>🧃 Anime no Sekai, 2022</span>
    </div>
}