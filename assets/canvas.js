import React from 'react';
import LiveProvider, { LiveEditor, LiveError, LivePreview } from 'react-live';

const code = `<strong>Hello World!</strong>`;
export function Canvas() {
  return (
    <LiveProvider code={code}>
      <LiveEditor />
      <LiveError />
      <LivePreview />
    </LiveProvider>
  );
};