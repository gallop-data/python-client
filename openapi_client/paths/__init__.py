# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DATA_ETH_GET_COLLECTIONS = "/data/eth/getCollections"
    DATA_ETH_GET_TOKENS = "/data/eth/getTokens"
    DATA_ETH_GET_COLLECTION_TRANSACTIONS = "/data/eth/getCollectionTransactions"
    DATA_ETH_GET_TOKEN_TRANSACTIONS = "/data/eth/getTokenTransactions"
    DATA_ETH_GET_MARKETPLACE_DATA = "/data/eth/getMarketplaceData"
    DATA_ETH_GET_MARKETPLACE_TRAIT_DATA = "/data/eth/getMarketplaceTraitData"
    DATA_ETH_GET_WALLET_NFTS = "/data/eth/getWalletNFTs"
    DATA_ETH_GET_WALLET_TRANSACTIONS = "/data/eth/getWalletTransactions"
    DATA_ETH_GET_HISTORICAL_TRANSACTIONS = "/data/eth/getHistoricalTransactions"
    DATA_ETH_GET_HISTORICAL_EVENTS = "/data/eth/getHistoricalEvents"
    DATA_ETH_GET_COLLECTION_OWNERS = "/data/eth/getCollectionOwners"
    DATA_ETH_GET_MARKETPLACE_FLOOR_PRICE = "/data/eth/getMarketplaceFloorPrice"
    DATA_ETH_GET_ENS_LOOKUP = "/data/eth/getEnsLookup"
    DATA_SOL_GET_COLLECTIONS = "/data/sol/getCollections"
    DATA_SOL_GET_TOKENS = "/data/sol/getTokens"
    DATA_SOL_GET_COLLECTION_TRANSACTIONS = "/data/sol/getCollectionTransactions"
    DATA_SOL_GET_TOKEN_TRANSACTIONS = "/data/sol/getTokenTransactions"
    DATA_SOL_GET_ACCOUNT_NFTS = "/data/sol/getAccountNFTs"
    DATA_SOL_GET_NFTACCOUNT = "/data/sol/getNFTAccount"
    DATA_SOL_GET_MARKETPLACE_DATA = "/data/sol/getMarketplaceData"
    DATA_SOL_GET_MARKETPLACE_TRAIT_DATA = "/data/sol/getMarketplaceTraitData"
    DATA_SOL_GET_COLLECTION_TRAITS = "/data/sol/getCollectionTraits"
    DATA_SOL_GET_HISTORICAL_TRANSACTIONS = "/data/sol/getHistoricalTransactions"
    DATA_SOL_GET_MARKETPLACE_FLOOR_PRICE = "/data/sol/getMarketplaceFloorPrice"
    DATA_POL_GET_COLLECTIONS = "/data/pol/getCollections"
    DATA_POL_GET_COLLECTION_TRANSACTIONS = "/data/pol/getCollectionTransactions"
    DATA_POL_GET_TOKEN_TRANSACTIONS = "/data/pol/getTokenTransactions"
    DATA_POL_GET_TOKENS = "/data/pol/getTokens"
    DATA_POL_GET_COLLECTION_TRAITS = "/data/pol/getCollectionTraits"
    DATA_POL_GET_WALLET_NFTS = "/data/pol/getWalletNFTs"
    DATA_POL_GET_COLLECTION_OWNERS = "/data/pol/getCollectionOwners"
    DATA_POL_GET_MARKETPLACE_DATA = "/data/pol/getMarketplaceData"
    DATA_POL_GET_MARKETPLACE_FLOOR_PRICE = "/data/pol/getMarketplaceFloorPrice"
    DATA_POL_GET_WALLET_TRANSACTIONS = "/data/pol/getWalletTransactions"
    DATA_POL_GET_HISTORICAL_TRANSACTIONS = "/data/pol/getHistoricalTransactions"
    DATA_SKN_GET_MARKETPLACE_FLOOR_PRICE = "/data/skn/getMarketplaceFloorPrice"
    DATA_SKN_GET_MARKETPLACE_DATA = "/data/skn/getMarketplaceData"
    ANALYTICS_ETH_GET_COLLECTION_SUMMARY = "/analytics/eth/getCollectionSummary"
    ANALYTICS_ETH_GET_TOKEN_SUMMARY = "/analytics/eth/getTokenSummary"
    ANALYTICS_ETH_GET_COLLECTION_PRICE_DIFF = "/analytics/eth/getCollectionPriceDiff"
    ANALYTICS_ETH_GET_WASH_TRANSACTIONS = "/analytics/eth/getWashTransactions"
    ANALYTICS_ETH_GET_WASH_TRADE = "/analytics/eth/getWashTrade"
    ANALYTICS_ETH_GET_RARITY = "/analytics/eth/getRarity"
    ANALYTICS_ETH_GET_COLLECTION_SALES_OHLC = "/analytics/eth/getCollectionSalesOHLC"
    ANALYTICS_ETH_GET_COLLECTION_FLOOR_PRICE_OHLC = "/analytics/eth/getCollectionFloorPriceOHLC"
    ANALYTICS_ETH_GET_COLLECTION_LISTINGS_OHLC = "/analytics/eth/getCollectionListingsOHLC"
    ANALYTICS_ETH_GET_LEADER_BOARD = "/analytics/eth/getLeaderBoard"
    ANALYTICS_SOL_GET_COLLECTION_SUMMARY = "/analytics/sol/getCollectionSummary"
    ANALYTICS_SOL_GET_TOKEN_SUMMARY = "/analytics/sol/getTokenSummary"
    ANALYTICS_SOL_GET_COLLECTION_PRICE_DIFF = "/analytics/sol/getCollectionPriceDiff"
    ANALYTICS_SOL_GET_WASH_TRANSACTIONS = "/analytics/sol/getWashTransactions"
    ANALYTICS_SOL_GET_WASH_TRADE = "/analytics/sol/getWashTrade"
    ANALYTICS_SOL_GET_RARITY = "/analytics/sol/getRarity"
    ANALYTICS_SOL_GET_COLLECTION_SALES_OHLC = "/analytics/sol/getCollectionSalesOHLC"
    ANALYTICS_POL_GET_COLLECTION_SUMMARY = "/analytics/pol/getCollectionSummary"
    ANALYTICS_POL_GET_TOKEN_SUMMARY = "/analytics/pol/getTokenSummary"
    ANALYTICS_POL_GET_COLLECTION_PRICE_DIFF = "/analytics/pol/getCollectionPriceDiff"
    ANALYTICS_POL_GET_WASH_TRANSACTIONS = "/analytics/pol/getWashTransactions"
    ANALYTICS_POL_GET_WASH_TRADE = "/analytics/pol/getWashTrade"
    ANALYTICS_POL_GET_RARITY = "/analytics/pol/getRarity"
    ANALYTICS_POL_GET_COLLECTION_SALES_OHLC = "/analytics/pol/getCollectionSalesOHLC"
    ANALYTICS_POL_GET_LEADER_BOARD = "/analytics/pol/getLeaderBoard"
    INSIGHTS_ETH_GET_CUSTOM_COLLECTION_RISK = "/insights/eth/getCustomCollectionRisk"
    INSIGHTS_ETH_GET_CUSTOM_TOKEN_RISK = "/insights/eth/getCustomTokenRisk"
    INSIGHTS_ETH_GET_DEFAULT_COLLECTION_RISK = "/insights/eth/getDefaultCollectionRisk"
    INSIGHTS_ETH_GET_DEFAULT_TOKEN_RISK = "/insights/eth/getDefaultTokenRisk"
    INSIGHTS_ETH_GET_COLLECTION_FORECASTS = "/insights/eth/getCollectionForecasts"
    INSIGHTS_ETH_GET_TOKEN_FORECASTS = "/insights/eth/getTokenForecasts"
    INSIGHTS_ETH_GET_TOKEN_APPRAISAL = "/insights/eth/getTokenAppraisal"
    INSIGHTS_ETH_GET_WALLET_LABELS = "/insights/eth/getWalletLabels"
    INSIGHTS_ETH_GET_WALLET_VALUATION = "/insights/eth/getWalletValuation"
    INSIGHTS_SOL_GET_CUSTOM_COLLECTION_RISK = "/insights/sol/getCustomCollectionRisk"
    INSIGHTS_SOL_GET_CUSTOM_TOKEN_RISK = "/insights/sol/getCustomTokenRisk"
    INSIGHTS_SOL_GET_DEFAULT_COLLECTION_RISK = "/insights/sol/getDefaultCollectionRisk"
    INSIGHTS_SOL_GET_DEFAULT_TOKEN_RISK = "/insights/sol/getDefaultTokenRisk"
    INSIGHTS_SOL_GET_COLLECTION_FORECASTS = "/insights/sol/getCollectionForecasts"
    INSIGHTS_SOL_GET_TOKEN_FORECASTS = "/insights/sol/getTokenForecasts"
    INSIGHTS_SOL_GET_TOKEN_APPRAISAL = "/insights/sol/getTokenAppraisal"
    INSIGHTS_POL_GET_CUSTOM_COLLECTION_RISK = "/insights/pol/getCustomCollectionRisk"
    INSIGHTS_POL_GET_CUSTOM_TOKEN_RISK = "/insights/pol/getCustomTokenRisk"
    INSIGHTS_POL_GET_DEFAULT_COLLECTION_RISK = "/insights/pol/getDefaultCollectionRisk"
    INSIGHTS_POL_GET_DEFAULT_TOKEN_RISK = "/insights/pol/getDefaultTokenRisk"
    INSIGHTS_POL_GET_COLLECTION_FORECASTS = "/insights/pol/getCollectionForecasts"
    INSIGHTS_POL_GET_TOKEN_FORECASTS = "/insights/pol/getTokenForecasts"
    INSIGHTS_POL_GET_TOKEN_APPRAISAL = "/insights/pol/getTokenAppraisal"
    INSIGHTS_POL_GET_WALLET_LABELS = "/insights/pol/getWalletLabels"
