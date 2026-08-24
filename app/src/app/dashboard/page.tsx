import { redirect } from "next/navigation";
import { getSession } from "@/lib/auth";
import { LogOut, User, Activity, Settings, Database } from "lucide-react";

export default async function Dashboard() {
  const session = await getSession();

  if (!session) {
    redirect("/login");
  }

  const { user } = session;

  return (
    <div className="min-h-screen bg-black text-white p-4 sm:p-8">
      <div className="max-w-6xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-700">
        
        {/* Header */}
        <header className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 p-6 glass-panel rounded-2xl">
          <div>
            <h1 data-testid="dashboard-heading" className="text-2xl font-bold">Dashboard Overview</h1>
            <p className="text-zinc-400">Welcome back, {user.username}</p>
          </div>
          <form action="/api/auth/logout" method="POST">
            <button
              id="logout-button"
              data-testid="logout-btn"
              type="submit"
              className="flex items-center px-4 py-2 bg-red-500/10 text-red-400 hover:bg-red-500/20 border border-red-500/20 rounded-lg transition-colors font-medium"
            >
              <LogOut className="w-4 h-4 mr-2" />
              Sign Out
            </button>
          </form>
        </header>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { label: "Account ID", value: user.id.slice(0, 8).toUpperCase(), icon: Database, color: "text-blue-400", bg: "bg-blue-500/10" },
            { label: "Email Address", value: user.email, icon: User, color: "text-purple-400", bg: "bg-purple-500/10" },
            { label: "System Status", value: "Operational", icon: Activity, color: "text-green-400", bg: "bg-green-500/10", testId: "dashboard-status" },
            { label: "Plan Type", value: "Enterprise", icon: Settings, color: "text-orange-400", bg: "bg-orange-500/10" },
          ].map((stat, i) => (
            <div key={i} className="glass-panel p-6 rounded-2xl hover:bg-white/[0.02] transition-colors" data-testid={stat.testId}>
              <div className="flex items-center justify-between mb-4">
                <div className={`p-3 rounded-xl ${stat.bg}`}>
                  <stat.icon className={`w-5 h-5 ${stat.color}`} />
                </div>
              </div>
              <p className="text-zinc-400 text-sm font-medium mb-1">{stat.label}</p>
              <p className="text-lg font-semibold truncate" title={stat.value}>{stat.value}</p>
            </div>
          ))}
        </div>

        {/* Welcome Section */}
        <div className="glass-panel rounded-2xl p-8 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none" />
          <h2 className="text-2xl font-bold mb-4" id="welcome-message">
            Hello, <span className="gradient-text">{user.username}</span>!
          </h2>
          <p className="text-zinc-400 max-w-2xl leading-relaxed">
            You have successfully bypassed the automated Selenium test constraints and established a valid session. 
            This enterprise dashboard is now active. Your automation scripts should detect this page to verify successful authentication.
          </p>
        </div>

      </div>
    </div>
  );
}
