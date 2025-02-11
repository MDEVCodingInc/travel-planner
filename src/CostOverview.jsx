const CostOverview = () => {
    const trips = useTravelStore((state) => state.trips);
    const totalCost = trips.reduce((sum, trip) => sum + trip.cost, 0);
  
    return (
      <div className="p-4 bg-gray-100 rounded-lg mt-4">
        <h2 className="text-lg font-bold">💰 Totale kosten: €{totalCost}</h2>
      </div>
    );
  };
  
  export default CostOverview;
  