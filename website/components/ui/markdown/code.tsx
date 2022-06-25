import 'highlight.js/styles/default.css'
import 'lowlight/lib/common.js'

import Lowlight from 'react-lowlight'

const common = ['arduino', 'bash', 'c', 'cpp', 'csharp', 'css', 'diff', 'go', 'ini', 'java', 'javascript', 'json', 'kotlin', 'less', 'lua', 'makefile', 'markdown', 'objectivec', 'perl', 'php', 'php-template', 'plaintext', 'python', 'python-repl', 'r', 'ruby', 'rust', 'scss', 'shell', 'sql', 'swift', 'typescript', 'vbnet', 'xml', 'yaml']

export const CodeBlock = ({ node, inline, className, children, ...props }) => {
    const match = /language-(\w+)/.exec(className || '')
    // console.log(node, match)
    return inline ?
        <code className="rounded bg-slate-100 m-0 text-[85%] py-[0.2em] px-[.4em]">{children}</code>
        : <div className='rounded-sm overflow-hidden w-max h-max'>
            <Lowlight
                className="overflow-x-auto w-[80vw] text-[85%] my-4"
                value={String(children).replace(/\n$/, '')}
                language={common.includes(match[1]) ? match[1] : undefined}
                inline={inline}
                {...props}
            />
        </div>
}