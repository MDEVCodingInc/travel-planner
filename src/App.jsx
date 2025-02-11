import AddTrip from "./components/AddTrip";
import MapView from "./components/MapView";
import CostOverview from "./components/CostOverview";

function App() {
  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">✈️ Reisplanner</h1>
      <AddTrip />
      <CostOverview />
      <MapView />
    </div>
  );
}

export default App;
