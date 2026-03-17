import { useQuery } from "@tanstack/react-query";

import { fetchVentes } from "../api/ventesApi";

export const useVentes = (filters = {}) => {
  const query = useQuery({
    queryKey: ["ventes", filters],
    queryFn: () => fetchVentes(filters),
  });

  return {
    data: query.data,
    ventes: query.data?.results || [],
    total: query.data?.count || 0,
    hasNextPage: Boolean(query.data?.next),
    hasPreviousPage: Boolean(query.data?.previous),
    loading: query.isLoading,
    error: query.error,
    refetch: query.refetch,
  };
};