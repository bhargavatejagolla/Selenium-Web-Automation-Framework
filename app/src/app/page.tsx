import Link from 'next/link';
import { ArrowRight, ShieldCheck, Zap, Layers } from 'lucide-react';
import WebThreads from '@/components/ui/WebThreads';

export default function Home() {
  return (
    <div className="min-h-screen mesh-bg flex flex-col items-center justify-center p-4 overflow-hidden relative">
      <div style={{ width: '100%', height: '600px', position: 'relative' }}>
        <WebThreads
          color1="#5227FF"
          color2="#FF9FFC"
          color3="#FFFFFF"
          speed={0.2}
          threadCount={6}
          frequency={5}
          spread={0.18}
          taper={1}
          position={0.5}
          fanMode="center"
          glow={0.02}
          falloff={0.6}
          thickness={1.1}
          brightness={0.6}
          opacity={1}
          mirror
          shimmer={false}
          grain
          grainIntensity={0.05}
          mouseInteraction
          mouseStrength={0.3}
        />
      </div>

      <main className="z-10 w-full max-w-5xl mx-auto flex flex-col items-center text-center space-y-12">
        
        <div className="space-y-6 animate-in fade-in slide-in-from-bottom-8 duration-1000">
          <div className="inline-flex items-center rounded-full border border-white/10 bg-white/5 px-3 py-1 text-sm font-medium text-blue-300 backdrop-blur-sm mb-4">
            <span className="flex h-2 w-2 rounded-full bg-blue-400 mr-2 animate-pulse"></span>
            Enterprise Authentication System
          </div>
          
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight">
            Secure access, <br />
            <span className="gradient-text">beautifully designed.</span>
          </h1>
          
          <p className="text-lg md:text-xl text-zinc-400 max-w-2xl mx-auto leading-relaxed">
            A premium demonstration of Selenium automated testing against a modern, 
            Next.js App Router architecture. Experience the flawless integration.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-6 animate-in fade-in slide-in-from-bottom-12 duration-1000 delay-150">
          <Link 
            href="/login" 
            className="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white transition-all duration-200 bg-blue-600 font-pj rounded-xl focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 hover-lift overflow-hidden"
          >
            <span className="absolute inset-0 w-full h-full -mt-1 rounded-lg opacity-30 bg-gradient-to-b from-transparent via-transparent to-black"></span>
            <span className="relative flex items-center">
              Login to Account
              <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </span>
          </Link>
          
          <Link 
            href="/register" 
            className="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white transition-all duration-200 bg-white/5 border border-white/10 backdrop-blur-md rounded-xl hover:bg-white/10 hover-lift"
          >
            <span className="relative flex items-center">
              Create New Account
            </span>
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-16 w-full animate-in fade-in slide-in-from-bottom-16 duration-1000 delay-300">
          {[
            { icon: ShieldCheck, title: "Secure by Default", desc: "Enterprise-grade Bcrypt hashing and secure HttpOnly JWT sessions." },
            { icon: Zap, title: "Lightning Fast", desc: "Built on Next.js App Router for optimal performance and SEO." },
            { icon: Layers, title: "Fully Tested", desc: "100% automated test coverage via Selenium WebDriver." }
          ].map((feature, i) => (
            <div key={i} className="glass-panel rounded-2xl p-6 text-left hover:bg-white/[0.02] transition-colors">
              <div className="w-12 h-12 rounded-lg bg-blue-500/20 flex items-center justify-center mb-4 border border-blue-500/20">
                <feature.icon className="w-6 h-6 text-blue-400" />
              </div>
              <h3 className="text-xl font-semibold mb-2 text-white">{feature.title}</h3>
              <p className="text-zinc-400 leading-relaxed">{feature.desc}</p>
            </div>
          ))}
        </div>

      </main>
    </div>
  );
}
