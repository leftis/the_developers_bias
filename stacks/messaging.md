---
paths:
  - "**/*amqp*"
  - "**/*rabbit*"
  - "**/*queue*"
  - "**/*broker*"
  - "**/*.env"
  - "**/*.env.example"
---

# Messaging (RabbitMQ / AMQP)

## Queues split, exchanges copy

- A **queue** hands each message to one consumer. Two readers on one queue split the messages
  between them, and both see gaps.
- A **topic/fanout exchange** gives a copy to every queue bound to it. To read a feed without taking
  anything from anyone, bind your own queue to the exchange.
- A message published straight to a queue (default exchange, routing key = queue name) goes only to
  that queue. No binding can get you a copy. Your options are to ask the publisher to use an
  exchange, or to read that queue and own the fact that you're taking its messages.

## Which queue for what

| Need | Queue |
|---|---|
| A service that must not miss messages across restarts | its own **durable** queue, bound to the exchange |
| A live viewer or debugging tap | **exclusive, auto-delete, server-named** queue, `noAck` |
| A one-off look from the terminal | `amqp-consume -e <exchange> -r <key>` (makes its own temp queue) |

Never point a viewer at the real consumer's queue.

## Publish and consume settings

- Make input and output fully configurable: input queue, optional input exchange + routing key
  (binding only when the exchange is set), output exchange, output routing key, prefetch, reconnect
  delay.
- Name connections (`connection_name`) so they're easy to spot in the broker's connection list.
- Reconnect forever with a delay. A broker drop ("peer closed connection without TLS close_notify")
  is normal on hosted brokers. Log it once and reconnect.

## When "nothing is coming in"

Check in this order, read only, through the management API:

1. **The service's own counters.** Zero messages read means nothing is arriving. It's not a parsing
   problem.
2. **The queue:** consumers, messages ready, publish count and rate, `idle_since`. If the publish
   count isn't moving, nothing is routed to it. A consumer can't stop messages from *arriving*.
3. **The bindings** on your queue, and what's bound to the exchange.
4. **Every queue in the vhost:** look for one that's filling up with no consumer. That's often
   where the feed went.
5. **History:** ask for `msg_rates_age` / `lengths_age` samples to find *when* it changed. A table of
   counts per half hour settles arguments.
6. **Connections:** which clients are attached, from which IPs. Don't assume a connection is yours.

## Format errors

A parse error at a fixed position on every message ("position 13: attribute value must be
enclosed") usually means a different producer is publishing a different format into your queue.
Find that producer before changing the parser.
