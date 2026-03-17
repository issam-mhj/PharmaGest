import React, { useEffect, useState } from "react";
import { useIsFetching, useIsMutating, useQueryClient } from "@tanstack/react-query";

const normalizeErrorMessage = (error) => {
  if (!error) return null;
  return error?.response?.data?.detail || error?.message || "Une erreur réseau est survenue.";
};

const GlobalRequestStatus = () => {
  const isFetching = useIsFetching();
  const isMutating = useIsMutating();
  const queryClient = useQueryClient();
  const [lastError, setLastError] = useState(null);

  useEffect(() => {
    const unsubscribeQuery = queryClient.getQueryCache().subscribe((event) => {
      const error = event?.query?.state?.error;
      if (error) setLastError(normalizeErrorMessage(error));
    });

    const unsubscribeMutation = queryClient.getMutationCache().subscribe((event) => {
      const error = event?.mutation?.state?.error;
      if (error) setLastError(normalizeErrorMessage(error));
    });

    return () => {
      unsubscribeQuery();
      unsubscribeMutation();
    };
  }, [queryClient]);

  const hasPendingRequests = isFetching + isMutating > 0;

  if (!hasPendingRequests && !lastError) return null;

  return (
    <>
      {hasPendingRequests ? (
        <div className="status-banner status-loading">Chargement en cours...</div>
      ) : null}
      {lastError ? <div className="status-banner status-error">{lastError}</div> : null}
    </>
  );
};

export default GlobalRequestStatus;