import React from 'react';
import LiveProvider, { LiveEditor, LiveError, LivePreview } from 'react-live';

export function Canvas() {
  return (
    <LiveProvider code={code}>
      <LiveEditor />
      <LiveError />
      <LivePreview />
    </LiveProvider>
  );
};