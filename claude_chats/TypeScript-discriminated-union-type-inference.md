# TypeScript discriminated union type inference

- Source: https://claude.ai/share/3c0f3c5b-6c34-4736-ad72-cdef41537351
- Author: Julian
- Created: 2026-03-30
- Messages: 12

---

## Human

import { type ParsedMail } from 'mailparser'
import { deterministicEmailClassification } from '@/lib/imap/utils/deterministic-email-classification.unit.ts'
import { extractAddresses, extractAddressObject } from '@/lib/imap/utils/extract-addresses.unit.ts'
import { isWarmupEmail } from '@/lib/imap/utils/is-warmup-email.unit.ts'
import { findEmailContext } from '@/lib/imap/utils/find-email-context.service.ts'
import { serializeReferencesToArray } from '@/lib/imap/utils/serialize-references-to-array.unit.ts'
import { logger } from '@/lib/logger'
import { type EmailClassification } from '@/schemas/conversations/email.schema.ts'
import { type CustomInbox } from '@/schemas/inbox/custom-inbox.schema.ts'
import { getEmailOneDb } from '@/services/mongodb/repositories/emails.integration.ts'
import { getRecipientByIdDb } from '@/services/mongodb/repositories/get-recipient-by-id.integration.ts'
import { insertEmailDb } from '@/services/mongodb/repositories/insert-email.integration.ts'
import { emailHtmlToText } from '@/utils/email-html-to-text.unit.ts'
/**
 * Stores an incoming email in the database and returns the inserted emailId
 * for later classification triggering. Returns null if the email was skipped
 * (warmup email or already processed).
 */
export async function storeIncomingEmail(mail: ParsedMail, inbox: CustomInbox) {
  if (isWarmupEmail(mail)) return { emailId: null, isWarmup: true, shallBeClassified: false }
  const existingEmail = await getEmailOneDb({ messageId: mail.messageId }, { _id: 1 })
  if (existingEmail) return { emailId: existingEmail._id, isExistingEmail: true, shallBeClassified: false }
  const detClassification = deterministicEmailClassification(mail)
  const classification: EmailClassification = detClassification !== 'unclassified' ? detClassification : 'pending'
  const reasoning =
    classification !== 'pending' ? `Deterministic classification: ${classification}` : 'Awaiting AI classification'
  logger.info({}, `Initial email classification: ${reasoning}`)
  const conversation = await findEmailContext(mail, inbox._id)
  const recipient = conversation
    ? await getRecipientByIdDb(conversation.recipientId, { email: 1, status: 1, phone: 1 })
    : null
  const result = await insertEmailDb({
    direction: 'in',
    status: 'received',
    subject: mail.subject || 'No Subject',
    body: mail.html ? mail.html : '',
    bodyText: mail.text || emailHtmlToText(mail.html || ''),
    to: extractAddresses(mail.to),
    cc: extractAddresses(mail.cc),
    from: mail.from ? extractAddressObject(mail.from)[0] || 'Unknown Sender' : 'Unknown Sender',
    replyTo: extractAddresses(mail.replyTo),
    inboxId: inbox._id,
    userId: inbox.userId,
    messageId: mail.messageId,
    sentAt: mail.date,
    ...(conversation
      ? {
          recipientId: conversation.recipientId,
          ...(conversation.campaignId ? { campaignId: conversation.campaignId } : {}),
          ...(conversation.intentCampaignId ? { intentCampaignId: conversation.intentCampaignId } : {}),
          ...(conversation.processedPostId ? { processedPostId: conversation.processedPostId } : {})
        }
      : {}),
    ...(recipient
      ? { recipientEmail: recipient.email, recipientStatus: recipient.status, recipientPhone: recipient.phone }
      : {}),
    autoClassification: classification,
    classificationReasoning: reasoning,
    references: serializeReferencesToArray(mail.references),
    inReplyTo: mail.inReplyTo
  })
  const emailId = String(result.insertedId)
  logger.info({}, `Stored email ${emailId} for inbox ${inbox.emailAddress}, pending classification trigger`)
  return { emailId, hasConversationFound: !!conversation, shallBeClassified: true }
}


in a case like this there is no way for typescript to infer the type without creating a discriminated union? as const or nothing won’t work?

---

## Assistant

TypeScript actually infers this better than you might expect. The return type is already inferred as a union of three distinct object types because `true`, `false`, and `null` are preserved as literal types in object literal returns. So `shallBeClassified` already works as a discriminant without any extra work.

You can verify this yourself — hover over the function and you'll see something like:

```typescript
Promise<
  | { emailId: null; isWarmup: true; shallBeClassified: false }
  | { emailId: ObjectId; isExistingEmail: true; shallBeClassified: false }
  | { emailId: string; hasConversationFound: boolean; shallBeClassified: true }
>
```

And narrowing works:

```typescript
const result = await storeIncomingEmail(mail, inbox)
if (result.shallBeClassified) {
  result.emailId   // string
  result.hasConversationFound // boolean
}
```

Where `as const` would matter is if you had a value that TypeScript widens by default — like a `string` or `number` you want kept literal. But `true`, `false`, and `null` are already inferred as literal types in object literal return expressions, so `as const` buys you nothing here.

The one thing the inferred union *doesn't* give you is clean narrowing between the two `shallBeClassified: false` branches, since they share the same discriminant value. If you needed that, you'd either add a shared discriminant with three distinct literals (like `kind: 'warmup' | 'existing' | 'new'`) or define an explicit discriminated union type. But if all your call sites only care about the `true`/`false` split, the inferred type is already sufficient.

---

## Human

const results = await Promise.all(emails.map(email => storeIncomingEmail(email, inbox)))

const emailIdsToClassify = results.filter(result => result.shallBeClassified)

But this still gives me all 3 options, even though it could be only one

---

## Assistant

That's a known TypeScript limitation — `.filter()` doesn't narrow the array type unless you give it a type predicate. TypeScript just sees the callback returns `boolean`, so the output array keeps the full union.

Two clean fixes:

**Type predicate in the filter:**

```typescript
type ClassifiableResult = Extract<
  Awaited<ReturnType<typeof storeIncomingEmail>>,
  { shallBeClassified: true }
>

const emailIdsToClassify = results.filter(
  (r): r is ClassifiableResult => r.shallBeClassified
)
// now typed as ClassifiableResult[]
```

**Or skip the `Extract` and just use `flatMap`**, which narrows naturally:

```typescript
const emailIdsToClassify = results.flatMap(r =>
  r.shallBeClassified ? [r] : []
)
```

The `flatMap` trick works because inside the ternary, TypeScript narrows `r` in the truthy branch — and since you're returning `[r]` or `[]`, the resulting array type only includes the narrowed variant. No type predicates, no extra types.

---

## Human

const emailIdsToClassify = results.flatMap(result => result.shallBeClassified ? [result] : [])
 still shows me the full 3 options

---

## Assistant

You're right — my mistake. TypeScript doesn't narrow the union inside the `flatMap` callback the way you'd hope. The conditional expression resolves both branches against the full union, so `[result]` still carries all three variants.

The type predicate filter is the reliable way:

```typescript
const emailIdsToClassify = results.filter(
  (r): r is Extract<typeof r, { shallBeClassified: true }> => r.shallBeClassified
)
```

`Extract<typeof r, { shallBeClassified: true }>` pulls the matching variant from the union inline, so you don't need a separate type alias. After this, `emailIdsToClassify` is typed as only the `{ emailId: string; hasConversationFound: boolean; shallBeClassified: true }` variant.

---

## Human

but is this giving type safety or is this just asserting?

---

## Assistant

It's an assertion. TypeScript does **zero verification** on type predicates. You could write:

```typescript
(r): r is Extract<typeof r, { shallBeClassified: true }> => !r.shallBeClassified
//                                                          ^ inverted logic, TS won't complain
```

and TypeScript would accept it happily. The `r is X` syntax means "trust me, compiler" — it's a cast dressed up as narrowing.

If you want actual compiler-verified narrowing, you need control flow:

```typescript
const emailIdsToClassify = []
for (const result of results) {
  if (result.shallBeClassified) {
    emailIdsToClassify.push(result) // genuinely narrowed here
  }
}
```

But now `emailIdsToClassify` is typed as the full union array unless you annotate it, which puts you back in the same spot.

So practically speaking, the type predicate filter is the standard pattern for this in TypeScript. It's not provably safe, but it's a single, obvious, reviewable assertion at the boundary — and everything downstream gets real narrowing from it. It's a much smaller trust surface than scattering `as` casts through your code.

This is just a gap in TypeScript's type system. There's been a long-standing [request](https://github.com/microsoft/TypeScript/issues/16069) for `.filter()` to infer type predicates automatically, but it hasn't landed.

---

## Human

So the real correct way would be a discriminated union in the source function ?

---

## Assistant

It wouldn't actually fix this specific problem. The inferred return type is *already* a discriminated union — TypeScript figured that out on its own. The issue isn't the shape of the union, it's that `.filter()` doesn't do narrowing.

Even if you wrote it out explicitly:

```typescript
type StoreResult =
  | { kind: 'warmup'; emailId: null; shallBeClassified: false }
  | { kind: 'existing'; emailId: string; shallBeClassified: false }
  | { kind: 'new'; emailId: string; shallBeClassified: true }

results.filter(r => r.kind === 'new') // still StoreResult[], not narrowed
```

You'd still need the type predicate for the filter.

So the real answer is: there is no fully type-safe way to filter-narrow an array in TypeScript today. The type predicate is the idiomatic solution, and it's what the ecosystem uses everywhere (including the standard lib's own typings for `Array.isArray`, `instanceof` checks, etc.).

Your function is fine as-is. The inferred union is correct, the discriminant works for `if/switch` on individual results, and for the array filter you pay the one-time cost of a type predicate. That's just the current state of the language.

---

## Human

obviously it does if its distinct types it can infer parameters

---

## Assistant

You're right, I overcorrected. With TypeScript 5.5+ and its inferred type predicates, `.filter()` can actually narrow automatically if the discriminant is clean:

```typescript
// With a distinct kind field:
type StoreResult =
  | { kind: 'warmup'; emailId: null }
  | { kind: 'existing'; emailId: string }
  | { kind: 'new'; emailId: string; hasConversationFound: boolean }

const toClassify = results.filter(r => r.kind === 'new')
// TS 5.5+ infers: StoreResult & { kind: 'new' }[]
```

So a clean discriminant does solve it — the compiler can infer the type predicate from the callback body when the narrowing logic maps cleanly to a discriminant check.

The reason it probably isn't working in your case is that `shallBeClassified` is a boolean rather than a distinct string literal per branch, and the return type is inferred from anonymous object literals rather than declared types. TS 5.5's inference is good but not bulletproof — it works best with explicit equality checks against literal values.

So yes, declaring a proper discriminated union in the source function with distinct `kind` literals would be the genuinely type-safe path that also makes `.filter()` narrowing work without manual predicates.
