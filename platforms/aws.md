---
paths:
  - "**/cdk/**"
  - "**/iac/**"
  - "**/cdk.json"
  - "**/lambda/**"
  - "**/template.yaml"
---

# AWS (CDK, Lambda, Cognito, CloudFront)

- **Pin region and profile on every command** (`--region`, `AWS_PROFILE`). Check
  `aws configure get region` before deploying. List the right ones in the project file.
- Never delete a stack unless told to.
- Some data has no backup. Resources listed as protected in the project file are not read, listed
  or written, not even for "sizing". Build against local fakes and let me run it.
- Before deploying: `cdk synth`, then grep for stale values (old CloudFront URLs, old client IDs,
  old CORS origins).
- CORS with credentials: exact origin, never `*`. Lambdas echo the request `Origin` and send
  `Access-Control-Allow-Credentials: true`. Don't add manual `OPTIONS` methods when CDK's default
  preflight is on.
- Frontend env vars are baked in at build time: rebuild after any env change, then check the bundle
  has the new values.
- After deploy: check distribution status, CORS headers on a preflight, and auth callback URLs match
  the live domain. They drift when distributions are recreated.
- If CDK skips an unchanged asset, update the function directly with `aws lambda
  update-function-code`.
