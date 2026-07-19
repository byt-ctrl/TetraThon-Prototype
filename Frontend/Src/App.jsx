import { useEffect, useState } from 'react'
import { api } from './api'
import AdvisoryForm from './components/AdvisoryForm'
import AdvisoryResult from './components/AdvisoryResult'
import Layout from './components/Layout'
import HealthCheck from './components/HealthCheck'
import LocationList from './components/LocationList'
import CropList from './components/CropList'

export default function App() {
  const [health, setHealth] = useState(null)
  const [locations, setLocations] = useState([])
  const [crops, setCrops] = useState([])
  const [error, setError] = useState(null)
  
  // Navigation view state: 'home' | 'form' | 'results'
  const [view, setView] = useState('home')
  const [lastResult, setLastResult] = useState(null)
  const [inputs, setInputs] = useState(null)

  useEffect(() => {
    Promise.all([api.health(), api.locations(), api.crops()])
      .then(([h, loc, crp]) => {
        setHealth(h)
        setLocations(loc)
        setCrops(crp)
      })
      .catch((e) => setError(e.message))
  }, [])

  return (
    <Layout>
      {error && (
        <div className="bg-red-50 border-l-4 border-red-500 text-red-700 p-4 rounded-xl text-sm font-medium max-w-2xl w-full mb-6">
          Could not reach backend: {error}
        </div>
      )}

      {/* Conditional View Rendering */}
      {view === 'home' && (
        <div className="flex flex-col items-center w-full max-w-2xl">
          {/* Main Action Button */}
          <div className="w-full bg-gradient-to-r from-emerald-600 to-teal-700 rounded-2xl shadow-lg p-6 text-white text-center mb-8 transform transition duration-300 hover:scale-[1.01]">
            <h2 className="text-xl font-bold">Need agronomy recommendations?</h2>
            <p className="text-emerald-100 text-sm mt-1 mb-4">
              Get stage-specific water, fertilizer, and pest advisories based on your local weather conditions.
            </p>
            <button
              onClick={() => setView('form')}
              className="inline-flex items-center justify-center bg-white text-emerald-800 font-bold px-6 py-3 rounded-xl shadow hover:bg-emerald-50 transition duration-200 gap-2"
            >
              <span>🌾</span> Get Crop Advisory
            </button>
          </div>

          {/* Health check card */}
          <HealthCheck health={health} />

          {/* Locations and Crops Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
            <LocationList locations={locations} />
            <CropList crops={crops} />
          </div>
        </div>
      )}

      {view === 'form' && (
        <AdvisoryForm
          locations={locations}
          crops={crops}
          onSubmitSuccess={(res, inp) => {
            setLastResult(res)
            setInputs(inp)
            setView('results')
          }}
          onCancel={() => setView('home')}
        />
      )}

      {view === 'results' && (
        <AdvisoryResult
          result={lastResult}
          inputs={inputs}
          onNewAdvisory={() => setView('form')}
          onGoHome={() => setView('home')}
        />
      )}
    </Layout>
  )
}