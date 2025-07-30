import { createContext } from "react";
import type { UserInfo } from "../types/github/User";

export const UserContext = createContext<UserInfo | null>(null);
