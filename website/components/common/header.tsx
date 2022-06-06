import { HamburgerIcon } from "components/icons/hamburger"
import { HamburgerModal } from "components/ui/modals/hamburger"
import Link from "next/link"
import { Navbar } from "./navbar"
import { TranslateIcon } from "components/icons/translatepy"
import { useState } from "react"

export const Header = () => {
    const [showMenu, setShowMenu] = useState(false);

    return <nav className="flex flex-row w-screen h-max mt-5 mb-16">
        <div className="left-10 absolute my-auto cursor-pointer">
            <Link href="/">
                <TranslateIcon />
            </Link>
        </div>
        <HamburgerIcon onClick={() => {
            setShowMenu(true);
        }} className="sm:hidden block absolute right-10 cursor-pointer opacity-50 hover:opacity-100 transition" />
        {
            showMenu && <HamburgerModal onClose={() => { setShowMenu(false) }} />
        }
        <Navbar className="sm:flex hidden" />
    </nav>
}