import { Button, Divider, Stack, Typography } from "@mui/material";
import { UNITS, cellArea, getResolution } from "h3-js";
import { useDispatch, useSelector } from "react-redux";
import { setDatasets, setSelectedDataset, setH3Index as setSelectedH3Index } from 'store/selectedSlice';
import { RootState } from "store/store";
import groupBy from "utils/groupBy";
import { Dataset } from "../types";
import Datasets from "./Datasets";
import DeselectDatasetButton from "./DeselectDatasetButton";

const Selected = () => {
  const { h3Index, datasets }: { h3Index: string, datasets: Dataset[] } = useSelector((state: RootState) => state.selected);
  const { selectedDataset } = useSelector((state: RootState) => state.selected);
  const dispatch = useDispatch();
  const datasetsByOrgs = datasets ? groupBy(datasets, "source_org") : null;
  const handleDeselectClick = () => {
    dispatch(setSelectedH3Index(null));
    dispatch(setDatasets(null));
  }
  
  return (
    <>
      <div className="p-4">
          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Typography className="text-lg font-bold">Tile {h3Index}</Typography>
            <Button onClick={handleDeselectClick} size="small" variant="text" className="uppercase hover:bg-transparent">Deselect tile</Button>
          </Stack>
          <Typography className="text-sm">Resolution: {getResolution(h3Index)}</Typography>
          <Typography className="text-sm">Cell area: {cellArea(h3Index, UNITS.km2).toFixed(2)} km<sup className="sups">2</sup></Typography>
          <Typography className="text-sm">Dataset count: {datasets?.length} datasets</Typography>
          { selectedDataset && <DeselectDatasetButton /> }
      </div>
      <Divider />
      { datasets && <Datasets datasetsByOrgs={datasetsByOrgs} />}
    </>
  )
} 

export default Selected;