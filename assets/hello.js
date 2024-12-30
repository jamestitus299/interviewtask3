import React, {useState, useEffect, useContext, useReducer, useRef, useMemo, useCallback} from "react";
import {
  LiveProvider,
  LiveEditor,
  LiveError,
  LivePreview,
} from "react-live-runner";

export function Hello({code}) {
  // const code = "<h1>James Titus</h1>";
  const scope = {React, useState, useEffect, useContext, useReducer, useRef, useMemo, useCallback};
  // console.log(code);
  return (
    <div>
      <LiveProvider code={code} scope={scope}>
        <LiveEditor />
        <LivePreview />
        <LiveError />
      </LiveProvider>
    </div>
  );
}
