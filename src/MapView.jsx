import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import useTravelStore from "../store/travelStore";

const MapView = () => {
  const trips = useTravelStore((state) => state.trips);

  return (
    <MapContainer center={[52.3676, 4.9041]} zoom={6} className="h-96 w-full mt-4">
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {trips.map((trip) => (
        <Marker key={trip.id} position={[52.3676, 4.9041]}>
          <Popup>{trip.title}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapView;
