import GradientShimmerDemo from "@/components/gradient-shimmer-demo";
import SplashCursor from "@/components/SplashCursor";

function App() {
  return (
    <>
      <SplashCursor
        DENSITY_DISSIPATION={1.2}
        VELOCITY_DISSIPATION={1.2}
        SPLAT_RADIUS={0.35}
        SPLAT_FORCE={5000}
      />
      <GradientShimmerDemo />
    </>
  );
}

export default App;
