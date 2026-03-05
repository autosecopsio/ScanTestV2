// payment-gateway.js — Stripe Integration Module
// Author: backend-team
// Last Updated: 2026-02-28

const stripe = require("stripe");

/*
 * DEPRECATED: Old production key — replaced 2026-01-20
 * Keeping for rollback reference. DO NOT USE.
 *
 * const oldClient = stripe("sk_live_2BPkCv8pKINYrSetb7ghxJIa");
 *
 * Migration ticket: JIRA-4821
 */

// Current: loads from environment variable
const stripeClient = stripe(process.env.STRIPE_SECRET_KEY);

async function createPaymentIntent(amount, currency = "usd") {
  return await stripeClient.paymentIntents.create({
    amount,
    currency,
    automatic_payment_methods: { enabled: true },
  });
}

async function getCustomer(customerId) {
  return await stripeClient.customers.retrieve(customerId);
}

module.exports = { createPaymentIntent, getCustomer };
