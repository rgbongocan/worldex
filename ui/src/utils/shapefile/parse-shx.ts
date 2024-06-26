// Lifted from https://github.com/visgl/loaders.gl/blob/ad75df5bd79d8ff21f3a598cc5d10e97786e47ba/modules/shapefile/src/lib/parsers/parse-shx.ts
import { parseSHPHeader } from './parse-shp-header';

export interface SHXOutput {
  offsets: Int32Array;
  lengths: Int32Array;
}

const SHX_HEADER_SIZE = 100;
const BIG_ENDIAN = false;

/**
 * @param arrayBuffer
 * @returns SHXOutput
 */
export function parseShx(arrayBuffer: ArrayBuffer): SHXOutput {
  // SHX header is identical to SHP Header
  const headerView = new DataView(arrayBuffer, 0, SHX_HEADER_SIZE);
  const header = parseSHPHeader(headerView);
  const contentLength = header.length - SHX_HEADER_SIZE;

  const contentView = new DataView(arrayBuffer, SHX_HEADER_SIZE, contentLength);

  const offsets = new Int32Array(contentLength);
  const lengths = new Int32Array(contentLength);

  // eslint-disable-next-line no-plusplus
  for (let i = 0; i < contentLength / 8; i++) {
    offsets[i] = contentView.getInt32(i * 8, BIG_ENDIAN);
    lengths[i] = contentView.getInt32(i * 8 + 4, BIG_ENDIAN);
  }

  return {
    offsets,
    lengths,
  };
}
