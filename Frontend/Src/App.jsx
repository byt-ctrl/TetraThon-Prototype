import { useEffect, useState } from 'react'
import { api } from './api'

export default function App() {
  const [health, setHealth] = useState(null)
  const [locations, setLocations] = useState([])
  const [crops, setCrops] = useState([])
  const [error, setError] = useState(null)

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
    <div className="min-h-screen bg-slate-50 flex flex-col items-center py-10 px-4">
      <h1 className="text-2xl font-bold text-slate-800">
        TetraTHON — Precision Crop Advisory & Post-Harvest Planner
      </h1>
      <p className="text-slate-500 mt-1">Chunk 1: Foundation skeleton</p>

      {error && (
        <div className="mt-6 bg-red-100 text-red-700 px-4 py-2 rounded">
          Could not reach backend: {error}
        </div>
      )}

      <div className="mt-6 bg-white shadow rounded-xl px-6 py-4 text-center">
        <p className="text-sm text-slate-500">Backend health check</p>
        <p className="text-xl font-semibold text-green-600">
          {health ? health.status : 'checking...'}
        </p>
      </div>

      <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-2xl">
        <div className="bg-white shadow rounded-xl p-4">
          <h2 className="font-semibold text-slate-700 mb-2">Locations ({locations.length})</h2>
          <ul className="text-slate-600 text-sm space-y-1">
            {locations.map((l) => (
              <li key={l.id}>{l.name}, {l.state}</li>
            ))}
          </ul>
        </div>
        <div className="bg-white shadow rounded-xl p-4">
          <h2 className="font-semibold text-slate-700 mb-2">Crops ({crops.length})</h2>
          <ul className="text-slate-600 text-sm space-y-1">
            {crops.map((c) => (
              <li key={c.id}>{c.name} — {c.category} ({c.typical_duration_days} days)</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}