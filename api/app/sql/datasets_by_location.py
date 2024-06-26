_bounds_query = "SELECT ST_GeomFromGeoJSON(CAST(:location AS TEXT)) bounds"

# TODO: make this less redundant
location_fill = f"""
WITH bounds AS (
  {_bounds_query}
)
SELECT h3_polygon_to_cells((SELECT bounds FROM bounds), :resolution) fill_index
"""

location_fill_res2 = f"""
WITH bounds AS ({_bounds_query}),
res3 AS (
  SELECT h3_polygon_to_cells((SELECT bounds FROM bounds), 3) res3
)
SELECT DISTINCT fill_index FROM res3,
LATERAL h3_cell_to_parent(res3, :resolution) AS fill_index
WHERE ST_Contains((SELECT bounds FROM bounds), h3_cell_to_geometry(fill_index))
"""

datasets_by_location = """
WITH fill AS ({fill_query}),
with_parents AS (
  SELECT fill_index, ARRAY[{parents_array}] parents FROM fill GROUP BY fill_index
),
{candidate_datasets_cte}
located_datasets AS (
  SELECT DISTINCT(id) FROM (
    SELECT dataset_id id FROM h3_data JOIN with_parents ON h3_index = ANY(parents)
    UNION ALL
    SELECT dataset_id id FROM h3_children_indicators JOIN fill ON h3_index = fill_index
  ) parent_children_datasets
)
SELECT
  id,
  name,
  ST_AsEWKT(bbox) bbox,
  source_org,
  regexp_replace(description, '\n', '\n', 'g') description,
  files,
  url,
  accessibility,
  date_start,
  date_end
FROM datasets JOIN located_datasets USING (id)
"""

# TODO: filter located_datasets by candidate_datasets_cte
datasets_by_location_w_ordinality = """
WITH fill AS ({fill_query}),
with_parents AS (
  SELECT fill_index, ARRAY[{parents_array}] parents FROM fill GROUP BY fill_index
),
{candidate_datasets_cte}
located_datasets AS (
  SELECT DISTINCT(id) FROM (
    SELECT dataset_id id FROM h3_data JOIN with_parents ON h3_index = ANY(parents)
    UNION ALL
    SELECT dataset_id id FROM h3_children_indicators JOIN fill ON h3_index = fill_index
  ) parent_children_datasets
)
SELECT * FROM (
  SELECT
    id,
    name,
    ST_AsEWKT(bbox) bbox,
    source_org,
    regexp_replace(description, '\n', '\n', 'g') description,
    files,
    url,
    accessibility,
    date_start,
    date_end
  FROM datasets JOIN located_datasets USING (id)
) unfiltered
JOIN candidate_datasets USING (id)
ORDER BY ordinality
"""

def get_datasets_by_location_query(resolution: int, candidate_datasets_cte=None, has_ordinality=False) -> str:
    from app.services import build_h3_parents_expression

    q = datasets_by_location_w_ordinality if has_ordinality else datasets_by_location
    return q.format(
        fill_query=location_fill_res2 if resolution == 2 else location_fill,
        parents_array=build_h3_parents_expression(resolution),
        candidate_datasets_cte=candidate_datasets_cte or "",
    )
