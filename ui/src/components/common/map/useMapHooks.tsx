import { useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { styled } from '@mui/material/styles';
import { setViewState, ViewState } from '@carto/react-redux';
import { Typography } from '@carto/react-ui';
import { renderToStaticMarkup } from 'react-dom/server';
import { debounce } from '@mui/material';
import { MAXIMUM_ZOOM, MINIMUM_ZOOM } from 'constants/h3';
import { setPendingLocationCheck } from 'store/searchSlice';
import { RootState } from 'store/store';
import getSteppedZoomResolutionPair from 'utils/getSteppedZoomResolutionPair';
import { setSteppedZoom } from 'store/appSlice';

const TooltipContent = styled('div')(({ theme }) => ({
  color: theme.palette.common.white,
  position: 'relative',
  padding: theme.spacing(1, 1.5),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: theme.palette.grey[900],
  transform: `translate(-50%, calc(-100% - ${theme.spacing(2.5)}))`,
}));

const TooltipArrow = styled('div')(({ theme }) => ({
  display: 'block',
  position: 'absolute',
  top: 'calc(100% - 1px)',
  left: '50%',
  width: 0,
  height: 0,
  marginLeft: theme.spacing(-1),
  borderLeft: `${theme.spacing(1)} solid transparent`,
  borderRight: `${theme.spacing(1)} solid transparent`,
  borderTop: `${theme.spacing(1)} solid ${theme.palette.grey[900]}`,
}));

export function useMapHooks() {
  const dispatch = useDispatch();

  let isHovering = false;
  const { pendingLocationCheck } = useSelector((state: RootState) => state.search);

  const handleViewStateChange = ({ viewState }: { viewState: ViewState }) => {
    if (viewState.zoom != null) {
      viewState.zoom = Math.min(Math.max(viewState.zoom, MINIMUM_ZOOM), MAXIMUM_ZOOM);
    }
    // @ts-ignore
    dispatch(setViewState(viewState));

    if (viewState.zoom != null) {
      dispatch(setSteppedZoom(getSteppedZoomResolutionPair(viewState.zoom)[0]));
    }
    if (pendingLocationCheck) {
      dispatch(setPendingLocationCheck(false));
    }
  };

  const handleSizeChange = ({
    width,
    height,
  }: {
    width: number;
    height: number;
  }) => {
    // @ts-ignore
    dispatch(setViewState({ width, height }));
  };

  const handleHover = ({ object }: any) => (isHovering = !!object);
  const handleCursor = ({ isDragging }: { isDragging: boolean }) =>
    isDragging ? 'grabbing' : isHovering ? 'pointer' : 'grab';

  const handleTooltip = (info: any) => {
    // This is a very custom solution, to keep react working with the current deck.gl native tooltip, but other solutions could be done. Check tooltip documentation https://deck.gl/docs/api-reference/core/deck#gettooltip
    function createMarkup() {
      return { __html: info.object.html };
    }

    if (info?.object?.html) {
      return {
        /*
          This is a classic approach to set innerHtml.
          There are other options to consider though as https://deck.gl/docs/developer-guide/interactivity/#using-react
        */
        html: renderToStaticMarkup(
          <TooltipContent>
            <Typography
              variant='caption'
              component='div'
              dangerouslySetInnerHTML={createMarkup()}
            />
            <TooltipArrow />
          </TooltipContent>,
        ),
        style: info.object.style,
      };
    }
    return null;
  };

  return {
    handleViewStateChange,
    handleSizeChange,
    handleHover,
    handleCursor,
    handleTooltip,
  };
}
