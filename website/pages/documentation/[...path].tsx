import { useEffect, useState } from 'react'

import { Colorful } from 'components/common/colorful'
import Configuration from 'config'
import Link from 'next/link'
import { MarkdownComponent } from 'components/ui/markdown'
import type { NextPage } from 'next'
import ReactMarkdown from 'react-markdown'
import { SEO } from 'components/common/seo'
import { TableOfContent } from 'components/common/toc'
import rehypeRaw from 'rehype-raw'
// import rehypeSanitize from 'rehype-sanitize'
import remarkGfm from 'remark-gfm'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'

const Documentation: NextPage = () => {
    const { strings } = useLanguage();
    const router = useRouter();
    const [path, setPath] = useState<string[]>((router.query.path as string[]) || []);

    const [content, setContent] = useState<string>();

    useEffect(() => {
        setPath((router.query.path as string[]) || [])
    }, [router.query])

    useEffect(() => {
        const __path__ = path.join("|")
        let documentationItems = strings.documentation
        let resultPath = ""
        for (const i in path) {
            const result = documentationItems.find(value => value.name === path[i])
            if (!result) { break }
            resultPath += `/${encodeURIComponent(result.name)}`
            if (!result.children) {
                resultPath += ".md"
                break
            }
            documentationItems = result.children
        }
        if (!resultPath.endsWith(".md")) {
            resultPath += "/README.md"
        }
        fetch(`https://cdn.jsdelivr.net/gh/Animenosekai/translate@${encodeURIComponent(Configuration.repo.branch)}/docs/${encodeURIComponent(strings.name)}${resultPath}`)
            .then(response => response.text())
            .then(text => {
                if (path.join("|") === __path__) {
                    setContent(text)
                }
            })
    }, [path, strings])

    return <div className='h-full'>
        <SEO title='translatepy — Documentation' description='Learn how to use translatepy!' />
        <div className='flex gap-2 w-screen'>
            <div className="p-5 ml-3 overflow-y-auto h-1/2 w-max flex flex-col -mt-5 gap-2 sticky top-0">
                <Link passHref={true} href="/documentation">
                    <a>
                        <span className='mx-auto self-center text-xl font-semibold m-5 cursor-pointer'>translatepy {<Colorful value='docs' />}</span>
                    </a>
                </Link>
                {
                    strings.documentation
                        ? strings.documentation.map((value, i) => {
                            return <TableOfContent data={value} key={i} level={1} query={path} />
                        })
                        : ""
                }
            </div>
            <div className='w-3/4 mb-5'>
                <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]} components={MarkdownComponent}>{content}</ReactMarkdown>
            </div>
        </div>
    </div>
}

export default Documentation
