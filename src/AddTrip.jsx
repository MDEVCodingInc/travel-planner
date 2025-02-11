import { useState } from "react";
import useTravelStore from "../store/travelStore";

const AddTrip = () => {
  const [trip, setTrip] = useState({
    title: "",
    type: "transport",
    cost: 0,
    location: "",
  });

  const addTrip = useTravelStore((state) => state.addTrip);

  const handleSubmit = (e) => {
    e.preventDefault();
    addTrip({ ...trip, id: Date.now() });
    setTrip({ title: "", type: "transport", cost: 0, location: "" });
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded-lg shadow-md">
      <input
        type="text"
        placeholder="Titel"
        value={trip.title}
        onChange={(e) => setTrip({ ...trip, title: e.target.value })}
        className="border p-2 rounded w-full mb-2"
      />
      <select
        value={trip.type}
        onChange={(e) => setTrip({ ...trip, type: e.target.value })}
        className="border p-2 rounded w-full mb-2"
      >
        <option value="transport">Transport</option>
        <option value="accommodation">Accommodatie</option>
        <option value="activity">Activiteit</option>
        <option value="food">Eten</option>
      </select>
      <input
        type="number"
        placeholder="Kosten"
        value={trip.cost}
        onChange={(e) => setTrip({ ...trip, cost: Number(e.target.value) })}
        className="border p-2 rounded w-full mb-2"
      />
      <button className="bg-blue-500 text-white p-2 rounded w-full">
        Toevoegen
      </button>
    </form>
  );
};

export default AddTrip;
