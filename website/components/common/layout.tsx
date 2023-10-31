import { Footer } from "./footer"
import { Header } from "./header"
// import { Navbar } from "./navbar"

export const Layout = ({ children }: { children }) => {
    return <div className="flex flex-col min-h-screen relative">
        <Header />
        <div className="main h-full pb-10">
            {children}
        </div>
        <Footer />
    </div>
}
