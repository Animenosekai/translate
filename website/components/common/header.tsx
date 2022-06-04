import Link from "next/link"
import { Navbar } from "./navbar"
import { TranslateIcon } from "components/icons/translatepy"

export const Header = () => {
    return <nav className="flex flex-row w-screen h-max mt-5 mb-16">
        <div className="left-10 absolute my-auto cursor-pointer">
            <Link href="/">
                <TranslateIcon />
            </Link>
        </div>
        <Navbar />
    </nav>
}