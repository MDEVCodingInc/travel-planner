import { create } from "zustand";

const useTravelStore = create((set) => ({
  trips: [],
  addTrip: (trip) => set((state) => ({ trips: [...state.trips, trip] })),
  removeTrip: (id) =>
    set((state) => ({ trips: state.trips.filter((trip) => trip.id !== id) })),
}));

export default useTravelStore;
