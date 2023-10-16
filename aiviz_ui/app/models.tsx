// pages/models.tsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Model {
  id: string;
  name: string;
  // add other fields here as needed
}

const Models: React.FC = () => {
  const [models, setModels] = useState<Model[]>([]);
  const [after, setAfter] = useState<number>(0);
  const pageSize = 10;

  useEffect(() => {
    const fetchModels = async () => {
      try {
        const response = await axios.get<{ models: Model[] }>(`http://34.168.248.101/api/models?after=${after}`);
        setModels(response.data.models);
      } catch (error) {
        console.error("There was an error fetching the models:", error);
      }
    };

    fetchModels();
  }, [after]);

  return (
    <div>
      <h1>AI Models</h1>
      <ul>
        {models.map((model) => (
          <li key={model.id}>{model.name}</li>
        ))}
      </ul>
      <button onClick={() => setAfter(after - pageSize)} disabled={after <= 0}>Previous</button>
      <button onClick={() => setAfter(after + pageSize)}>Next</button>
    </div>
  );
};

export default Models;

