import { useQuery } from "@tanstack/react-query";

import { fetchMedicaments } from "../api/medicamentsApi";

export const useMedicaments = (filters = {}) => {
  const query = useQuery({
    queryKey: ["medicaments", filters],
    queryFn: () => fetchMedicaments(filters),
  });

  return {
    data: query.data,
    medicaments: query.data?.results || [],
    total: query.data?.count || 0,
    hasNextPage: Boolean(query.data?.next),
    hasPreviousPage: Boolean(query.data?.previous),
    loading: query.isLoading,
    error: query.error,
    refetch: query.refetch,
  };
};
