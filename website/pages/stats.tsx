import { Chart } from 'components/ui/charts/chart'
import { ChartDataContextProvider } from 'contexts/chartData'
import type { NextPage } from 'next'
import { SEO } from 'components/common/seo'
import { ServicesColorContextProvider } from 'contexts/servicesColor'
import { useLanguage } from 'contexts/language'

const Stats: NextPage = () => {
    const { strings } = useLanguage();

    return <ServicesColorContextProvider>
        <div>
            <SEO title='Statistics' description="Look at translatpy's stats to determine which translation service is the best!" />

            <div className="flex items-center flex-col p-3 gap-5 w-screen">
                <div className='p-5 w-full'>
                    <h2 className='text-xl font-bold'>{strings.heading.timeTakenForTranslation}</h2>
                    <ChartDataContextProvider unit="ms" yLabel="Time (ms)">
                        <Chart endpoint='/stats/timings' />
                    </ChartDataContextProvider>
                </div>
                <div className='p-5 w-full'>
                    <h2 className='text-xl font-bold'>{strings.heading.errorsCount}</h2>
                    <ChartDataContextProvider unit="" yLabel="Count">
                        <Chart endpoint='/stats/errors' />
                    </ChartDataContextProvider>
                </div>
            </div>
        </div>
    </ServicesColorContextProvider>
}

export default Stats
