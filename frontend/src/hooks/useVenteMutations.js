import { useMutation, useQueryClient } from "@tanstack/react-query";

import { cancelVente, createVente } from "../api/ventesApi";

export const useVenteMutations = () => {
  const queryClient = useQueryClient();

  const invalidate = () => {
    queryClient.invalidateQueries({ queryKey: ["ventes"] });
    queryClient.invalidateQueries({ queryKey: ["medicaments"] });
  };

  const createMutation = useMutation({
    mutationFn: createVente,
    onSuccess: invalidate,
  });

  const cancelMutation = useMutation({
    mutationFn: cancelVente,
    onSuccess: invalidate,
  });

  return {
    createVente: createMutation.mutateAsync,
    cancelVente: cancelMutation.mutateAsync,
    creating: createMutation.isPending,
    cancelling: cancelMutation.isPending,
  };
};