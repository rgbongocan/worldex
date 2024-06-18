import axios from 'axios';

export const stripEntities = (query: string, entities: any[]): string => {
  if (!Array.isArray(entities) || entities.length === 0) {
    return query;
  }
  let strippedQ = '';
  entities.forEach((entity, idx) => {
    const prevEntity = entities[idx - 1];
    const nextEntity = entities[idx + 1];
    if (!prevEntity) {
      strippedQ += query.slice(0, entity.start);
    } else {
      strippedQ += query.slice(prevEntity.end, entity.start);
    }
    if (!nextEntity) {
      strippedQ += query.slice(entity.end);
    }
  });
  return strippedQ.trim();
};

// TODO: type entities
export const prepSearchKeyword = async (entities: any[], query: string, skipLocation: boolean) => {
  const hasNoEntities = Array.isArray(entities) && entities.length === 0;
  let keyword;
  if (hasNoEntities) {
    // will only be used if the user skips location search
    return query;
  } else {
    let labelsToKeep = ['statistical indicator'];
    if (skipLocation) {
      // reconsider region and country entities for keyword search
      labelsToKeep = [...labelsToKeep, 'region', 'country'];
    }
    const entitiesToStrip = entities.filter((e) => !labelsToKeep.includes(e.label));
    keyword = stripEntities(query, entitiesToStrip);
    try {
      const { data } = await axios.get(
        `${import.meta.env.VITE_API_URL}/search/strip_stop_words`,
        { params: { query: keyword } },
      );
      const { tokens } = data;
      return tokens.map((t: any) => t.token).join(' ');
    } catch (err) {
      console.error(err.toJSON());
    }
  }
};

export const getDatasetsByKeyword = async (params?: any) => {
  const { data } = await axios.get(
    `${import.meta.env.VITE_API_URL}/search/keyword`,
    { params },
  );
  return data;
};
