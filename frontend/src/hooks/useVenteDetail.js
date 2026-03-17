import { useQuery } from "@tanstack/react-query";

import { fetchVenteDetail } from "../api/ventesApi";

export const useVenteDetail = (venteId) => {
  const query = useQuery({
    queryKey: ["ventes", "detail", venteId],
    queryFn: () => fetchVenteDetail(venteId),
    enabled: Boolean(venteId),
  });

  return {
    vente: query.data,
    loading: query.isLoading,
    error: query.error,
  };
};