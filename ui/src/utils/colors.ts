export const hexToRgb = (hex: string): [number, number, number] => {
  const numericValue = parseInt(hex, 16);
  const r = (numericValue >> 16) & 0xFF;
  const g = (numericValue >> 8) & 0xFF;
  const b = numericValue & 0xFF;
  return [r, g, b];
};

export const colorBins = ({ attr, domains, colors }: { attr: string, domains: number[], colors: number[][] }) => ((d: any) => {
  for (const [idx, value] of domains.entries()) {
    if (d[attr] < value) {
      return [...colors[idx]];
    }
  }
  return [...colors.at(-1)];
});
