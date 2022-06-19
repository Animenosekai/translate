import { Chart } from 'components/ui/charts/chart'
import type { NextPage } from 'next'
import { SEO } from 'components/common/seo'
import { useLanguage } from 'contexts/language'

const Home: NextPage = () => {
    const { strings } = useLanguage();

    return <div>
        <SEO description='Use multiple services to translate your texts!' />

        <div className="flex items-center flex-col p-3 gap-5 w-screen">
            <div className='p-5 w-full'>
                <h2 className='text-xl font-bold'>{strings.heading.timeTakenForTranslation}</h2>
                <Chart endpoint='/stats/timings' />
            </div>
            <div className='p-5 w-full'>
                <h2 className='text-xl font-bold'>{strings.heading.errorsCount}</h2>
                <Chart endpoint='/stats/errors' />
            </div>
        </div>
    </div>
}

export default Home
