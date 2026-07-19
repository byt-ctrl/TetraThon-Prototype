export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col items-center py-10 px-4">
      {/* Title */}
      <div className="text-center max-w-2xl mb-8">
        <h1 className="text-3xl font-extrabold text-slate-800 tracking-tight sm:text-4xl">
          ArgiTech
        </h1>
        <p className="text-slate-500 mt-2 font-medium">
          Precision Crop Advisory & Post-Harvest Decision Engine
        </p>
      </div>

      <main className="w-full flex flex-col items-center">
        {children}
      </main>

      <footer className="mt-16 text-center text-slate-400 text-xs font-semibold uppercase tracking-wider">
        Built for **ArgiTech** — AgriTech Track, Navrachana University.
      </footer>
    </div>
  )
}
