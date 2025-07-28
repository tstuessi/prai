import type { paths } from "../types/api";

export type UserInfo = paths["/api/github/user"]["get"]["responses"]["200"]["content"]["application/json"];
