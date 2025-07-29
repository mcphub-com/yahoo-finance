import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/enclout/api/yahoo-finance'

mcp = FastMCP('yahoo-finance')

@mcp.tool()
def auto_complete(q: Annotated[str, Field(description='Any familiar term or phrase to get auto complete suggestions')],
                  region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get auto complete suggestions by term or phrase'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_fundamentals(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                           modules: Annotated[str, Field(description='One of the followings (Separated by comma for multiple options) : assetComponents,assetProfile,balanceSheetHistory,balanceSheetHistoryQuarterly,calendarEvents,cashflowStatementHistory,cashflowStatementHistoryQuarterly,components,defaultKeyStatistics,earnings,earningsHistory,earningsTrend,equityPerformance,esgScores,financialData,financialsTemplate,fundOwnership,fundPerformance,fundProfile,futuresChain,incomeStatementHistory,incomeStatementHistoryQuarterly,indexTrend,industryTrend,insiderHolders,insiderTransactions,institutionOwnership,majorDirectHolders,majorHoldersBreakdown,netSharePurchaseActivity,recommendationTrend,secFilings,sectorTrend,summaryDetail,summaryProfile,topHoldings,upgradeDowngradeHistory,pageViews,financialsTemplate,quoteUnadjustedPerformanceOverview')],
                           region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                           lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get fundamentals data'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-fundamentals'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'modules': modules,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_recommendations(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')]) -> dict: 
    '''Get similar symbols relating to specified one'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_upgrades_downgrades(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                               region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                               lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get upgrades downgrades histories related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-upgrades-downgrades'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_chart(interval: Annotated[str, Field(description='One of the following is allowed 1m|2m|5m|15m|30m|60m|1d|1wk|1mo')],
                 symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                 range: Annotated[str, Field(description='One of the following is allowed 1d|5d|1mo|3mo|6mo|1y|2y|5y|10y|ytd|max. Do not use together with period1 and period2.')],
                 region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                 period1: Annotated[Union[int, float, None], Field(description="Epoch timestamp in seconds, such as 1556816400, must be different from period2, and the value must be starting of a day to get whole data in day. Don't use together with range parameter. Default: 0")] = None,
                 period2: Annotated[Union[int, float, None], Field(description="Epoch timestamp in seconds, such as 1562170150, must be different from period1, and the value must be starting of the next day to get whole data in previous day. Don't use together with range parameter. Default: 0")] = None,
                 comparisons: Annotated[Union[str, None], Field(description='The symbols for comparison separated by comma. Ex : ^GDAXI,^FCHI')] = None,
                 includePrePost: Annotated[Union[bool, None], Field(description='Whether or not including pre post')] = None,
                 useYfid: Annotated[Union[bool, None], Field(description='Whether or not using Yfid')] = None,
                 includeAdjustedClose: Annotated[Union[bool, None], Field(description='Whether or not including adjusted Close')] = None,
                 events: Annotated[Union[str, None], Field(description='One of the followings : capitalGain|div|split|earn|history. Separated by comma for multiple events. Ex : capitalGain,split')] = None) -> dict: 
    '''Get data to draw full screen chart'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-chart'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'interval': interval,
        'symbol': symbol,
        'range': range,
        'region': region,
        'period1': period1,
        'period2': period2,
        'comparisons': comparisons,
        'includePrePost': includePrePost,
        'useYfid': useYfid,
        'includeAdjustedClose': includeAdjustedClose,
        'events': events,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_chart(interval: Annotated[str, Field(description='One of the following is allowed 1m|2m|5m|15m|60m|1d')],
                 symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                 range: Annotated[str, Field(description='One of the following is allowed 1d|5d|1mo|3mo|6mo|1y|2y|5y|10y|ytd|max. Do not use together with period1 and period2.')],
                 region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                 period1: Annotated[Union[int, float, None], Field(description="Epoch timestamp in seconds, such as 1556816400, must be different from period2, and the value must be starting of a day to get whole data in day. Don't use together with range parameter. Default: 0")] = None,
                 period2: Annotated[Union[int, float, None], Field(description="Epoch timestamp in seconds, such as 1562170150, must be different from period1, and the value must be starting of the next day to get whole data in previous day. Don't use together with range parameter. Default: 0")] = None) -> dict: 
    '''Get data to draw full screen chart'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'interval': interval,
        'symbol': symbol,
        'range': range,
        'region': region,
        'period1': period1,
        'period2': period2,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v4_get_statistics(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                      region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                      lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get statistics related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v4/get-statistics'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_profile(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                   lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get ticker's profile'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-profile'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_timeseries(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                      period2: Annotated[str, Field(description='Epoch timestamp in seconds (ex : 1571590800), must be different from period1, and the value must be starting of next day to get whole data in previous day.')],
                      period1: Annotated[Union[int, float], Field(description='Epoch timestamp in seconds (ex : 493578000), must be different from period2, and the value must be starting of a day to get whole data in day. Default: 0')],
                      region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                      type: Annotated[Union[str, None], Field(description='Specify returned fields, one of the following is allowed (Separated by comma for multiple values, ex : ...&type=quarterlyEbitda,trailingEbitda,quarterlyWeighteAverageShare,...) : annualTaxEffectOfUnusualItems|trailingTaxEffectOfUnusualItems|annualTaxRateForCalcs|trailingTaxRateForCalcs|annualNormalizedEBITDA|trailingNormalizedEBITDA|annualNormalizedDilutedEPS|trailingNormalizedDilutedEPS|annualNormalizedBasicEPS|trailingNormalizedBasicEPS|annualTotalUnusualItems|trailingTotalUnusualItems|annualTotalUnusualItemsExcludingGoodwill|trailingTotalUnusualItemsExcludingGoodwill|annualNetIncomeFromContinuingOperationNetMinorityInterest|trailingNetIncomeFromContinuingOperationNetMinorityInterest|annualReconciledDepreciation|trailingReconciledDepreciation|annualReconciledCostOfRevenue|trailingReconciledCostOfRevenue|annualEBITDA|trailingEBITDA|annualEBIT|trailingEBIT|annualNetInterestIncome|trailingNetInterestIncome|annualInterestExpense|trailingInterestExpense|annualInterestIncome|trailingInterestIncome|annualContinuingAndDiscontinuedDilutedEPS|trailingContinuingAndDiscontinuedDilutedEPS|annualContinuingAndDiscontinuedBasicEPS|trailingContinuingAndDiscontinuedBasicEPS|annualNormalizedIncome|trailingNormalizedIncome|annualNetIncomeFromContinuingAndDiscontinuedOperation|trailingNetIncomeFromContinuingAndDiscontinuedOperation|annualTotalExpenses|trailingTotalExpenses|annualRentExpenseSupplemental|trailingRentExpenseSupplemental|annualReportedNormalizedDilutedEPS|trailingReportedNormalizedDilutedEPS|annualReportedNormalizedBasicEPS|trailingReportedNormalizedBasicEPS|annualTotalOperatingIncomeAsReported|trailingTotalOperatingIncomeAsReported|annualDividendPerShare|trailingDividendPerShare|annualDilutedAverageShares|trailingDilutedAverageShares|annualBasicAverageShares|trailingBasicAverageShares|annualDilutedEPS|trailingDilutedEPS|annualDilutedEPSOtherGainsLosses|trailingDilutedEPSOtherGainsLosses|annualTaxLossCarryforwardDilutedEPS|trailingTaxLossCarryforwardDilutedEPS|annualDilutedAccountingChange|trailingDilutedAccountingChange|annualDilutedExtraordinary|trailingDilutedExtraordinary|annualDilutedDiscontinuousOperations|trailingDilutedDiscontinuousOperations|annualDilutedContinuousOperations|trailingDilutedContinuousOperations|annualBasicEPS|trailingBasicEPS|annualBasicEPSOtherGainsLosses|trailingBasicEPSOtherGainsLosses|annualTaxLossCarryforwardBasicEPS|trailingTaxLossCarryforwardBasicEPS|annualBasicAccountingChange|trailingBasicAccountingChange|annualBasicExtraordinary|trailingBasicExtraordinary|annualBasicDiscontinuousOperations|trailingBasicDiscontinuousOperations|annualBasicContinuousOperations|trailingBasicContinuousOperations|annualDilutedNIAvailtoComStockholders|trailingDilutedNIAvailtoComStockholders|annualAverageDilutionEarnings|trailingAverageDilutionEarnings|annualNetIncomeCommonStockholders|trailingNetIncomeCommonStockholders|annualOtherunderPreferredStockDividend|trailingOtherunderPreferredStockDividend|annualPreferredStockDividends|trailingPreferredStockDividends|annualNetIncome|trailingNetIncome|annualMinorityInterests|trailingMinorityInterests|annualNetIncomeIncludingNoncontrollingInterests|trailingNetIncomeIncludingNoncontrollingInterests|annualNetIncomeFromTaxLossCarryforward|trailingNetIncomeFromTaxLossCarryforward|annualNetIncomeExtraordinary|trailingNetIncomeExtraordinary|annualNetIncomeDiscontinuousOperations|trailingNetIncomeDiscontinuousOperations|annualNetIncomeContinuousOperations|trailingNetIncomeContinuousOperations|annualEarningsFromEquityInterestNetOfTax|trailingEarningsFromEquityInterestNetOfTax|annualTaxProvision|trailingTaxProvision|annualPretaxIncome|trailingPretaxIncome|annualOtherIncomeExpense|trailingOtherIncomeExpense|annualOtherNonOperatingIncomeExpenses|trailingOtherNonOperatingIncomeExpenses|annualSpecialIncomeCharges|trailingSpecialIncomeCharges|annualGainOnSaleOfPPE|trailingGainOnSaleOfPPE|annualGainOnSaleOfBusiness|trailingGainOnSaleOfBusiness|annualOtherSpecialCharges|trailingOtherSpecialCharges|annualWriteOff|trailingWriteOff|annualImpairmentOfCapitalAssets|trailingImpairmentOfCapitalAssets|annualRestructuringAndMergernAcquisition|trailingRestructuringAndMergernAcquisition|annualSecuritiesAmortization|trailingSecuritiesAmortization|annualEarningsFromEquityInterest|trailingEarningsFromEquityInterest|annualGainOnSaleOfSecurity|trailingGainOnSaleOfSecurity|annualNetNonOperatingInterestIncomeExpense|trailingNetNonOperatingInterestIncomeExpense|annualTotalOtherFinanceCost|trailingTotalOtherFinanceCost|annualInterestExpenseNonOperating|trailingInterestExpenseNonOperating|annualInterestIncomeNonOperating|trailingInterestIncomeNonOperating|annualOperatingIncome|trailingOperatingIncome|annualOperatingExpense|trailingOperatingExpense|annualOtherOperatingExpenses|trailingOtherOperatingExpenses|annualOtherTaxes|trailingOtherTaxes|annualProvisionForDoubtfulAccounts|trailingProvisionForDoubtfulAccounts|annualDepreciationAmortizationDepletionIncomeStatement|trailingDepreciationAmortizationDepletionIncomeStatement|annualDepletionIncomeStatement|trailingDepletionIncomeStatement|annualDepreciationAndAmortizationInIncomeStatement|trailingDepreciationAndAmortizationInIncomeStatement|annualAmortization|trailingAmortization|annualAmortizationOfIntangiblesIncomeStatement|trailingAmortizationOfIntangiblesIncomeStatement|annualDepreciationIncomeStatement|trailingDepreciationIncomeStatement|annualResearchAndDevelopment|trailingResearchAndDevelopment|annualSellingGeneralAndAdministration|trailingSellingGeneralAndAdministration|annualSellingAndMarketingExpense|trailingSellingAndMarketingExpense|annualGeneralAndAdministrativeExpense|trailingGeneralAndAdministrativeExpense|annualOtherGandA|trailingOtherGandA|annualInsuranceAndClaims|trailingInsuranceAndClaims|annualRentAndLandingFees|trailingRentAndLandingFees|annualSalariesAndWages|trailingSalariesAndWages|annualGrossProfit|trailingGrossProfit|annualCostOfRevenue|trailingCostOfRevenue|annualTotalRevenue|trailingTotalRevenue|annualExciseTaxes|trailingExciseTaxes|annualOperatingRevenue|trailingOperatingRevenue|annualTreasurySharesNumber|annualPreferredSharesNumber|annualOrdinarySharesNumber|annualShareIssued|annualNetDebt|annualTotalDebt|annualTangibleBookValue|annualInvestedCapital|annualWorkingCapital|annualNetTangibleAssets|annualCapitalLeaseObligations|annualCommonStockEquity|annualPreferredStockEquity|annualTotalCapitalization|annualTotalEquityGrossMinorityInterest|annualMinorityInterest|annualStockholdersEquity|annualOtherEquityInterest|annualGainsLossesNotAffectingRetainedEarnings|annualOtherEquityAdjustments|annualFixedAssetsRevaluationReserve|annualForeignCurrencyTranslationAdjustments|annualMinimumPensionLiabilities|annualUnrealizedGainLoss|annualTreasuryStock|annualRetainedEarnings|annualAdditionalPaidInCapital|annualCapitalStock|annualOtherCapitalStock|annualCommonStock|annualPreferredStock|annualTotalPartnershipCapital|annualGeneralPartnershipCapital|annualLimitedPartnershipCapital|annualTotalLiabilitiesNetMinorityInterest|annualTotalNonCurrentLiabilitiesNetMinorityInterest|annualOtherNonCurrentLiabilities|annualLiabilitiesHeldforSaleNonCurrent|annualRestrictedCommonStock|annualPreferredSecuritiesOutsideStockEquity|annualDerivativeProductLiabilities|annualEmployeeBenefits|annualNonCurrentPensionAndOtherPostretirementBenefitPlans|annualNonCurrentAccruedExpenses|annualDuetoRelatedPartiesNonCurrent|annualTradeandOtherPayablesNonCurrent|annualNonCurrentDeferredLiabilities|annualNonCurrentDeferredRevenue|annualNonCurrentDeferredTaxesLiabilities|annualLongTermDebtAndCapitalLeaseObligation|annualLongTermCapitalLeaseObligation|annualLongTermDebt|annualLongTermProvisions|annualCurrentLiabilities|annualOtherCurrentLiabilities|annualCurrentDeferredLiabilities|annualCurrentDeferredRevenue|annualCurrentDeferredTaxesLiabilities|annualCurrentDebtAndCapitalLeaseObligation|annualCurrentCapitalLeaseObligation|annualCurrentDebt|annualOtherCurrentBorrowings|annualLineOfCredit|annualCommercialPaper|annualCurrentNotesPayable|annualPensionandOtherPostRetirementBenefitPlansCurrent|annualCurrentProvisions|annualPayablesAndAccruedExpenses|annualCurrentAccruedExpenses|annualInterestPayable|annualPayables|annualOtherPayable|annualDuetoRelatedPartiesCurrent|annualDividendsPayable|annualTotalTaxPayable|annualIncomeTaxPayable|annualAccountsPayable|annualTotalAssets|annualTotalNonCurrentAssets|annualOtherNonCurrentAssets|annualDefinedPensionBenefit|annualNonCurrentPrepaidAssets|annualNonCurrentDeferredAssets|annualNonCurrentDeferredTaxesAssets|annualDuefromRelatedPartiesNonCurrent|annualNonCurrentNoteReceivables|annualNonCurrentAccountsReceivable|annualFinancialAssets|annualInvestmentsAndAdvances|annualOtherInvestments|annualInvestmentinFinancialAssets|annualHeldToMaturitySecurities|annualAvailableForSaleSecurities|annualFinancialAssetsDesignatedasFairValueThroughProfitorLossTotal|annualTradingSecurities|annualLongTermEquityInvestment|annualInvestmentsinJointVenturesatCost|annualInvestmentsInOtherVenturesUnderEquityMethod|annualInvestmentsinAssociatesatCost|annualInvestmentsinSubsidiariesatCost|annualInvestmentProperties|annualGoodwillAndOtherIntangibleAssets|annualOtherIntangibleAssets|annualGoodwill|annualNetPPE|annualAccumulatedDepreciation|annualGrossPPE|annualLeases|annualConstructionInProgress|annualOtherProperties|annualMachineryFurnitureEquipment|annualBuildingsAndImprovements|annualLandAndImprovements|annualProperties|annualCurrentAssets|annualOtherCurrentAssets|annualHedgingAssetsCurrent|annualAssetsHeldForSaleCurrent|annualCurrentDeferredAssets|annualCurrentDeferredTaxesAssets|annualRestrictedCash|annualPrepaidAssets|annualInventory|annualInventoriesAdjustmentsAllowances|annualOtherInventories|annualFinishedGoods|annualWorkInProcess|annualRawMaterials|annualReceivables|annualReceivablesAdjustmentsAllowances|annualOtherReceivables|annualDuefromRelatedPartiesCurrent|annualTaxesReceivable|annualAccruedInterestReceivable|annualNotesReceivable|annualLoansReceivable|annualAccountsReceivable|annualAllowanceForDoubtfulAccountsReceivable|annualGrossAccountsReceivable|annualCashCashEquivalentsAndShortTermInvestments|annualOtherShortTermInvestments|annualCashAndCashEquivalents|annualCashEquivalents|annualCashFinancial|annualForeignSales|trailingForeignSales|annualDomesticSales|trailingDomesticSales|annualAdjustedGeographySegmentData|trailingAdjustedGeographySegmentData|annualFreeCashFlow|trailingFreeCashFlow|annualRepurchaseOfCapitalStock|trailingRepurchaseOfCapitalStock|annualRepaymentOfDebt|trailingRepaymentOfDebt|annualIssuanceOfDebt|trailingIssuanceOfDebt|annualIssuanceOfCapitalStock|trailingIssuanceOfCapitalStock|annualCapitalExpenditure|trailingCapitalExpenditure|annualInterestPaidSupplementalData|trailingInterestPaidSupplementalData|annualIncomeTaxPaidSupplementalData|trailingIncomeTaxPaidSupplementalData|annualEndCashPosition|trailingEndCashPosition|annualOtherCashAdjustmentOutsideChangeinCash|trailingOtherCashAdjustmentOutsideChangeinCash|annualBeginningCashPosition|trailingBeginningCashPosition|annualEffectOfExchangeRateChanges|trailingEffectOfExchangeRateChanges|annualChangesInCash|trailingChangesInCash|annualOtherCashAdjustmentInsideChangeinCash|trailingOtherCashAdjustmentInsideChangeinCash|annualCashFlowFromDiscontinuedOperation|trailingCashFlowFromDiscontinuedOperation|annualFinancingCashFlow|trailingFinancingCashFlow|annualCashFromDiscontinuedFinancingActivities|trailingCashFromDiscontinuedFinancingActivities|annualCashFlowFromContinuingFinancingActivities|trailingCashFlowFromContinuingFinancingActivities|annualNetOtherFinancingCharges|trailingNetOtherFinancingCharges|annualInterestPaidCFF|trailingInterestPaidCFF|annualProceedsFromStockOptionExercised|trailingProceedsFromStockOptionExercised|annualCashDividendsPaid|trailingCashDividendsPaid|annualPreferredStockDividendPaid|trailingPreferredStockDividendPaid|annualCommonStockDividendPaid|trailingCommonStockDividendPaid|annualNetPreferredStockIssuance|trailingNetPreferredStockIssuance|annualPreferredStockPayments|trailingPreferredStockPayments|annualPreferredStockIssuance|trailingPreferredStockIssuance|annualNetCommonStockIssuance|trailingNetCommonStockIssuance|annualCommonStockPayments|trailingCommonStockPayments|annualCommonStockIssuance|trailingCommonStockIssuance|annualNetIssuancePaymentsOfDebt|trailingNetIssuancePaymentsOfDebt|annualNetShortTermDebtIssuance|trailingNetShortTermDebtIssuance|annualShortTermDebtPayments|trailingShortTermDebtPayments|annualShortTermDebtIssuance|trailingShortTermDebtIssuance|annualNetLongTermDebtIssuance|trailingNetLongTermDebtIssuance|annualLongTermDebtPayments|trailingLongTermDebtPayments|annualLongTermDebtIssuance|trailingLongTermDebtIssuance|annualInvestingCashFlow|trailingInvestingCashFlow|annualCashFromDiscontinuedInvestingActivities|trailingCashFromDiscontinuedInvestingActivities|annualCashFlowFromContinuingInvestingActivities|trailingCashFlowFromContinuingInvestingActivities|annualNetOtherInvestingChanges|trailingNetOtherInvestingChanges|annualInterestReceivedCFI|trailingInterestReceivedCFI|annualDividendsReceivedCFI|trailingDividendsReceivedCFI|annualNetInvestmentPurchaseAndSale|trailingNetInvestmentPurchaseAndSale|annualSaleOfInvestment|trailingSaleOfInvestment|annualPurchaseOfInvestment|trailingPurchaseOfInvestment|annualNetInvestmentPropertiesPurchaseAndSale|trailingNetInvestmentPropertiesPurchaseAndSale|annualSaleOfInvestmentProperties|trailingSaleOfInvestmentProperties|annualPurchaseOfInvestmentProperties|trailingPurchaseOfInvestmentProperties|annualNetBusinessPurchaseAndSale|trailingNetBusinessPurchaseAndSale|annualSaleOfBusiness|trailingSaleOfBusiness|annualPurchaseOfBusiness|trailingPurchaseOfBusiness|annualNetIntangiblesPurchaseAndSale|trailingNetIntangiblesPurchaseAndSale|annualSaleOfIntangibles|trailingSaleOfIntangibles|annualPurchaseOfIntangibles|trailingPurchaseOfIntangibles|annualNetPPEPurchaseAndSale|trailingNetPPEPurchaseAndSale|annualSaleOfPPE|trailingSaleOfPPE|annualPurchaseOfPPE|trailingPurchaseOfPPE|annualCapitalExpenditureReported|trailingCapitalExpenditureReported|annualOperatingCashFlow|trailingOperatingCashFlow|annualCashFromDiscontinuedOperatingActivities|trailingCashFromDiscontinuedOperatingActivities|annualCashFlowFromContinuingOperatingActivities|trailingCashFlowFromContinuingOperatingActivities|annualTaxesRefundPaid|trailingTaxesRefundPaid|annualInterestReceivedCFO|trailingInterestReceivedCFO|annualInterestPaidCFO|trailingInterestPaidCFO|annualDividendReceivedCFO|trailingDividendReceivedCFO|annualDividendPaidCFO|trailingDividendPaidCFO|annualChangeInWorkingCapital|trailingChangeInWorkingCapital|annualChangeInOtherWorkingCapital|trailingChangeInOtherWorkingCapital|annualChangeInOtherCurrentLiabilities|trailingChangeInOtherCurrentLiabilities|annualChangeInOtherCurrentAssets|trailingChangeInOtherCurrentAssets|annualChangeInPayablesAndAccruedExpense|trailingChangeInPayablesAndAccruedExpense|annualChangeInAccruedExpense|trailingChangeInAccruedExpense|annualChangeInInterestPayable|trailingChangeInInterestPayable|annualChangeInPayable|trailingChangeInPayable|annualChangeInDividendPayable|trailingChangeInDividendPayable|annualChangeInAccountPayable|trailingChangeInAccountPayable|annualChangeInTaxPayable|trailingChangeInTaxPayable|annualChangeInIncomeTaxPayable|trailingChangeInIncomeTaxPayable|annualChangeInPrepaidAssets|trailingChangeInPrepaidAssets|annualChangeInInventory|trailingChangeInInventory|annualChangeInReceivables|trailingChangeInReceivables|annualChangesInAccountReceivables|trailingChangesInAccountReceivables|annualOtherNonCashItems|trailingOtherNonCashItems|annualExcessTaxBenefitFromStockBasedCompensation|trailingExcessTaxBenefitFromStockBasedCompensation|annualStockBasedCompensation|trailingStockBasedCompensation|annualUnrealizedGainLossOnInvestmentSecurities|trailingUnrealizedGainLossOnInvestmentSecurities|annualProvisionandWriteOffofAssets|trailingProvisionandWriteOffofAssets|annualAssetImpairmentCharge|trailingAssetImpairmentCharge|annualAmortizationOfSecurities|trailingAmortizationOfSecurities|annualDeferredTax|trailingDeferredTax|annualDeferredIncomeTax|trailingDeferredIncomeTax|annualDepreciationAmortizationDepletion|trailingDepreciationAmortizationDepletion|annualDepletion|trailingDepletion|annualDepreciationAndAmortization|trailingDepreciationAndAmortization|annualAmortizationCashFlow|trailingAmortizationCashFlow|annualAmortizationOfIntangibles|trailingAmortizationOfIntangibles|annualDepreciation|trailingDepreciation|annualOperatingGainsLosses|trailingOperatingGainsLosses|annualPensionAndEmployeeBenefitExpense|trailingPensionAndEmployeeBenefitExpense|annualEarningsLossesFromEquityInvestments|trailingEarningsLossesFromEquityInvestments|annualGainLossOnInvestmentSecurities|trailingGainLossOnInvestmentSecurities|annualNetForeignCurrencyExchangeGainLoss|trailingNetForeignCurrencyExchangeGainLoss|annualGainLossOnSaleOfPPE|trailingGainLossOnSaleOfPPE|annualGainLossOnSaleOfBusiness|trailingGainLossOnSaleOfBusiness|annualNetIncomeFromContinuingOperations|trailingNetIncomeFromContinuingOperations|annualCashFlowsfromusedinOperatingActivitiesDirect|trailingCashFlowsfromusedinOperatingActivitiesDirect|annualTaxesRefundPaidDirect|trailingTaxesRefundPaidDirect|annualInterestReceivedDirect|trailingInterestReceivedDirect|annualInterestPaidDirect|trailingInterestPaidDirect|annualDividendsReceivedDirect|trailingDividendsReceivedDirect|annualDividendsPaidDirect|trailingDividendsPaidDirect|annualClassesofCashPayments|trailingClassesofCashPayments|annualOtherCashPaymentsfromOperatingActivities|trailingOtherCashPaymentsfromOperatingActivities|annualPaymentsonBehalfofEmployees|trailingPaymentsonBehalfofEmployees|annualPaymentstoSuppliersforGoodsandServices|trailingPaymentstoSuppliersforGoodsandServices|annualClassesofCashReceiptsfromOperatingActivities|trailingClassesofCashReceiptsfromOperatingActivities|annualOtherCashReceiptsfromOperatingActivities|trailingOtherCashReceiptsfromOperatingActivities|annualReceiptsfromGovernmentGrants|trailingReceiptsfromGovernmentGrants|annualReceiptsfromCustomers|trailingReceiptsfromCustomers|quarterlyAccountsPayable|quarterlyAccountsReceivable|quarterlyAccumulatedDepreciation|quarterlyAmortization|quarterlyAmortizationOfIntangiblesIncomeStatement|quarterlyAverageDilutionEarnings|quarterlyBasicAccountingChange|quarterlyBasicAverageShares|quarterlyBasicContinuousOperations|quarterlyBasicDiscontinuousOperations|quarterlyBasicEPS|quarterlyBasicEPSOtherGainsLosses|quarterlyBasicExtraordinary|quarterlyBeginningCashPosition|quarterlyCapitalExpenditure|quarterlyCapitalStock|quarterlyCashAndCashEquivalents|quarterlyCashCashEquivalentsAndShortTermInvestments|quarterlyCashDividendsPaid|quarterlyCashFlowFromContinuingFinancingActivities|quarterlyChangeInAccountPayable|quarterlyChangeInCashSupplementalAsReported|quarterlyChangeInInventory|quarterlyChangeInWorkingCapital|quarterlyChangesInAccountReceivables|quarterlyCommonStockIssuance|quarterlyContinuingAndDiscontinuedBasicEPS|quarterlyContinuingAndDiscontinuedDilutedEPS|quarterlyCostOfRevenue|quarterlyCurrentAccruedExpenses|quarterlyCurrentAssets|quarterlyCurrentDebt|quarterlyCurrentDeferredRevenue|quarterlyCurrentLiabilities|quarterlyDeferredIncomeTax|quarterlyDepletionIncomeStatement|quarterlyDepreciationAmortizationDepletionIncomeStatement|quarterlyDepreciationAndAmortization|quarterlyDepreciationAndAmortizationInIncomeStatement|quarterlyDepreciationIncomeStatement|quarterlyDilutedAccountingChange|quarterlyDilutedAverageShares|quarterlyDilutedContinuousOperations|quarterlyDilutedDiscontinuousOperations|quarterlyDilutedEPS|quarterlyDilutedEPSOtherGainsLosses|quarterlyDilutedExtraordinary|quarterlyDilutedNIAvailtoComStockholders|quarterlyDividendPerShare|quarterlyEarningsFromEquityInterest|quarterlyEarningsFromEquityInterestNetOfTax|quarterlyearningsPerShare|quarterlyEBIT|quarterlyEbitda|quarterlyEndCashPosition|quarterlyEnterprisesValueEBITDARatio|quarterlyEnterprisesValueRevenueRatio|quarterlyEnterpriseValue|quarterlyExciseTaxes|quarterlyForwardPeRatio|quarterlyFreeCashFlow|quarterlyGainOnSaleOfBusiness|quarterlyGainOnSaleOfPPE|quarterlyGainOnSaleOfSecurity|quarterlyGainsLossesNotAffectingRetainedEarnings|quarterlyGeneralAndAdministrativeExpense|quarterlyGoodwill|quarterlyGrossPPE|quarterlyGrossProfit|quarterlyImpairmentOfCapitalAssets|quarterlyIncomeTaxPayable|quarterlyInsuranceAndClaims|quarterlyInterestExpense|quarterlyInterestExpenseNonOperating|quarterlyInterestIncome|quarterlyInterestIncomeNonOperating|quarterlyInventory|quarterlyInvestingCashFlow|quarterlyInvestmentsAndAdvances|quarterlyLongTermDebt|quarterlyMarketCap|quarterlyMinorityInterests|quarterlyNetIncome|quarterlyNetIncomeCommonStockholders|quarterlyNetIncomeContinuousOperations|quarterlyNetIncomeDiscontinuousOperations|quarterlyNetIncomeExtraordinary|quarterlyNetIncomeFromContinuingAndDiscontinuedOperation|quarterlyNetIncomeFromContinuingOperationNetMinorityInterest|quarterlyNetIncomeFromTaxLossCarryforward|quarterlyNetIncomeIncludingNoncontrollingInterests|quarterlyNetInterestIncome|quarterlyNetNonOperatingInterestIncomeExpense|quarterlyNetOtherInvestingChanges|quarterlyNetPPE|quarterlyNonCurrentDeferredRevenue|quarterlyNonCurrentDeferredTaxesLiabilities|quarterlyNormalizedBasicEPS|quarterlyNormalizedDilutedEPS|quarterlyNormalizedEBITDA|quarterlyNormalizedIncome|quarterlyOperatingCashFlow|quarterlyOperatingExpense|quarterlyOperatingIncome|quarterlyOperatingRevenue|quarterlyOtherCurrentAssets|quarterlyOtherCurrentLiabilities|quarterlyOtherGandA|quarterlyOtherIncomeExpense|quarterlyOtherIntangibleAssets|quarterlyOtherNonCashItems|quarterlyOtherNonCurrentAssets|quarterlyOtherNonCurrentLiabilities|quarterlyOtherNonOperatingIncomeExpenses|quarterlyOtherOperatingExpenses|quarterlyOtherShortTermInvestments|quarterlyOtherSpecialCharges|quarterlyOtherTaxes|quarterlyOtherunderPreferredStockDividend|quarterlyPbRatio|quarterlyPegRatio|quarterlyPeRatio|quarterlyPreferredStockDividends|quarterlyPretaxIncome|quarterlyProvisionForDoubtfulAccounts|quarterlyPsRatio|quarterlyPurchaseOfBusiness|quarterlyPurchaseOfInvestment|quarterlyReconciledCostOfRevenue|quarterlyReconciledDepreciation|quarterlyRentAndLandingFees|quarterlyRentExpenseSupplemental|quarterlyRepaymentOfDebt|quarterlyReportedNormalizedBasicEPS|quarterlyReportedNormalizedDilutedEPS|quarterlyRepurchaseOfCapitalStock|quarterlyResearchAndDevelopment|quarterlyRestructuringAndMergernAcquisition|quarterlyRetainedEarnings|quarterlySalariesAndWages|quarterlySaleOfInvestment|quarterlySecuritiesAmortization|quarterlySellingAndMarketingExpense|quarterlySellingGeneralAndAdministration|quarterlySpecialIncomeCharges|quarterlyStockBasedCompensation|quarterlyStockholdersEquity|quarterlyTaxEffectOfUnusualItems|quarterlyTaxLossCarryforwardBasicEPS|quarterlyTaxLossCarryforwardDilutedEPS|quarterlyTaxProvision|quarterlyTaxRateForCalcs|quarterlyTotalAssets|quarterlyTotalExpenses|quarterlyTotalLiabilitiesNetMinorityInterest|quarterlyTotalNonCurrentAssets|quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest|quarterlyTotalOperatingIncomeAsReported|quarterlyTotalOtherFinanceCost|quarterlyTotalRevenue|quarterlyTotalUnusualItems|quarterlyTotalUnusualItemsExcludingGoodwill|quarterlyWeighteAverageShare|quarterlyWriteOff|timestamp|trailingAccountsPayable|trailingAccountsReceivable|trailingAccumulatedDepreciation|trailingCapitalStock|trailingCashAndCashEquivalents|trailingCashCashEquivalentsAndShortTermInvestments|trailingChangeInCashSupplementalAsReported|trailingCurrentAccruedExpenses|trailingCurrentAssets|trailingCurrentDebt|trailingCurrentDeferredRevenue|trailingCurrentLiabilities|trailingearningsPerShare|trailingEnterprisesValueEBITDARatio|trailingEnterprisesValueRevenueRatio|trailingEnterpriseValue|trailingForwardPeRatio|trailingGainsLossesNotAffectingRetainedEarnings|trailingGoodwill|trailingGrossPPE|trailingIncomeTaxPayable|trailingInventory|trailingInvestmentsAndAdvances|trailingLongTermDebt|trailingMarketCap|trailingNetPPE|trailingNonCurrentDeferredRevenue|trailingNonCurrentDeferredTaxesLiabilities|trailingOtherCurrentAssets|trailingOtherCurrentLiabilities|trailingOtherIntangibleAssets|trailingOtherNonCurrentAssets|trailingOtherNonCurrentLiabilities|trailingOtherShortTermInvestments|trailingPbRatio|trailingPegRatio|trailingPeRatio|trailingPsRatio|trailingRetainedEarnings|trailingStockholdersEquity|trailingTotalAssets|trailingTotalLiabilitiesNetMinorityInterest|trailingTotalNonCurrentAssets|trailingTotalNonCurrentLiabilitiesNetMinorityInterest|trailingWeighteAverageShare')] = None) -> dict: 
    '''Get more data in Financials section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-timeseries'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'period2': period2,
        'period1': period1,
        'region': region,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_options(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                   lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None,
                   straddle: Annotated[Union[bool, None], Field(description='')] = None,
                   date: Annotated[Union[int, float, None], Field(description="Epoch timestamp in seconds (Ex : 1682035200), use the valid values of 'expirationDates' field returned right in this endpoint.")] = None) -> dict: 
    '''Get option prices'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-options'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
        'straddle': straddle,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_holders(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                   lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None,
                   straddle: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Get holders related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-holders'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
        'straddle': straddle,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_top_holdings(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                           region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                           lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None,
                           straddle: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Get top holdings related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-top-holdings'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
        'straddle': straddle,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_insights(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint')]) -> dict: 
    '''Get brief reports relating to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-insights'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_insights(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint')]) -> dict: 
    '''Get brief reports relating to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insights'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_earnings(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                       region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                       lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get earnings related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-earnings'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_fees_and_expenses(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                                region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                                lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get fees and expenses related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-fees-and-expenses'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_recent_updates(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                             region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                             lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get recent updates related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-recent-updates'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_recommendation_trend(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                                   lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get recommended trending information'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-recommendation-trend'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_esg_scores(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                         region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                         lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get scores related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-esg-scores'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_sec_filings(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                          region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                          lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get sec filings related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-sec-filings'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_futures_chain(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                            region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                            lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get futures chain'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-futures-chain'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_company_outlook(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                              region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                              lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get company outlook'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-company-outlook'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_events_calendar(tickersFilter: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')],
                              modules: Annotated[str, Field(description='One of the followings (Separated by comma for multiple options) : ipoEvents,earnings,secReports')],
                              region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                              lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None,
                              secFilingsTypeFilter: Annotated[Union[str, None], Field(description='One of the followings : 10-K|10-Q|8-K. Separated by comma for multiple options. Ex : 10-K,10-Q,8-K')] = None,
                              startDate: Annotated[Union[int, float, None], Field(description='Epoch timestamp in milliseconds, for filter by date range. Ex : 1708142400000')] = None,
                              endDate: Annotated[Union[int, float, None], Field(description='Epoch timestamp in milliseconds, for filter by date range. Ex : 1721102340000')] = None,
                              countPerDay: Annotated[Union[int, float, None], Field(description='Number of events per day. Maximum is 10')] = None) -> dict: 
    '''Get events calendar related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-events-calendar'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tickersFilter': tickersFilter,
        'modules': modules,
        'region': region,
        'lang': lang,
        'secFilingsTypeFilter': secFilingsTypeFilter,
        'startDate': startDate,
        'endDate': endDate,
        'countPerDay': countPerDay,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_what_analysts_are_saying(symbols: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint. Separated by comma for multiple symbols. Ex : AAPL,TSLA,etc…')],
                                       region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                                       lang: Annotated[Union[str, None], Field(description='One of the following is allowed en-US|pt-BR|en-AU|en-CA|fr-FR|de-DE|zh-Hant-HK|en-IN|it-IT|es-ES|en-GB|en-SG')] = None) -> dict: 
    '''Get "what analysts are saying" section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-what-analysts-are-saying'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
        'region': region,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_analysis(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                    region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Analysis section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_holders(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Major Holders tab in Holders section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_options(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                   date: Annotated[Union[int, float], Field(description='Epoch timestamp in seconds, the value must be starting of a day to get whole data Default: 1562284800')],
                   straddle: Annotated[Union[bool, None], Field(description='View as List or Straddle')] = None,
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Options section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-options'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'date': date,
        'straddle': straddle,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_statistics(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                      region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Statistics section This endpoint was deprecated, use .../stock/get-fundamentals instead'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_insider_roster(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                          region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Insider Roster tab in Holders section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-roster'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_historical_data(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                           region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Historical Data section This endpoint was deprecated, use .../stock/get-fundamentals instead'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_profile(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Profile section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_insider_transactions(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                                region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Insider Transactions tab in Holders section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-transactions'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_upgrades_downgrades(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                               region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get upgrades and downgrades data'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-upgrades-downgrades'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_cash_flow(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                     region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get cash flow tab information in Financials section * Use .../stock/v2/get-timeseries and .../stock/get-fundamentals instead'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-cash-flow'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_financials(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                      region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get Income Statement data in Financials section * Use .../stock/v2/get-timeseries and .../stock/get-fundamentals instead ** If you want to get Quarterly data, you need to use .../stock/v2/get-timeseries endpoint instead.'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_balance_sheet(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')],
                         region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Balance Sheet tab in Financials section * Use .../stock/v2/get-timeseries and .../stock/get-fundamentals instead'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-balance-sheet'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_summary(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Get data in Summary section * Use .../market/v2/get-quotes instead'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_statistics(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint.')]) -> dict: 
    '''Get data in Statistics section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-statistics'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_get_balance_sheet(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')]) -> dict: 
    '''Get data in Balance Sheet tab in Financials section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-balance-sheet'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_holdings(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint.')]) -> dict: 
    '''Get data in Holdings tab (it must be Mutual fun stock to have this tab displayed)'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holdings'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_esg_score_for_peers(symbol: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')]) -> dict: 
    '''Get ESG Risk scores for peers related to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-esg-score-for-peers'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_detail(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint ')],
                     region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG ')] = None) -> dict: 
    '''Get detail information of stock quote, index, exchange, etc...'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_histories(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint ')],
                        _from: Annotated[str, Field(description="Epoch timestamp in seconds, must be different from 'to', and the value must be starting of a day to get whole data in day. ")],
                        to: Annotated[str, Field(description="Epoch timestamp in seconds, must be different from 'from', and the value must be starting of the later day to get whole data all previous days. ")],
                        events: Annotated[str, Field(description='Pass this param multiple times to get more related events (div|split|earn), such as : &events=div&events=split&events=earn ')],
                        interval: Annotated[str, Field(description='Allowed values are (1d|5d|1mo|3mo|6mo|1y|2y|5y|max) ')],
                        region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG ')] = None) -> dict: 
    '''*This endpoint is deprecating Get stock histories to draw chart'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-histories'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'from': _from,
        'to': to,
        'events': events,
        'interval': interval,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_get_news(category: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint. ')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG ')] = None) -> dict: 
    '''*This endpoint is deprecating Get latest news related to a symbol, the result may be empty if there is no news in that region'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-news'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_similarities(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint.')]) -> dict: 
    '''Get similar and recommended symbols relating to specified one'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-similarities'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_historical_data(period1: Annotated[Union[int, float], Field(description="Epoch timestamp in seconds, must be different from 'period2', and the value must be starting of a day to get whole data in day. Default: 1546448400")],
                           period2: Annotated[Union[int, float], Field(description="Epoch timestamp in seconds, must be different from 'period1', and the value must be starting of the later day to get whole data in all previous days. Default: 1562086800")],
                           symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint. ')],
                           frequency: Annotated[Union[str, None], Field(description='Allow one of following : 1d|1wk|1mo ')] = None,
                           filter: Annotated[Union[str, None], Field(description='Allow one of following : history|div|split ')] = None) -> dict: 
    '''*This endpoint is deprecating Get data in Historical Data section'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'period1': period1,
        'period2': period2,
        'symbol': symbol,
        'frequency': frequency,
        'filter': filter,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_newsfeed(category: Annotated[str, Field(description='Pass "generalnews" to get general latest newsfeed or a specific symbol ')],
                    region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG ')] = None,
                    start_uuid: Annotated[Union[str, None], Field(description='The uuid of first newsfeed in a list (max 10 newsfeed per request), pass empty to load the first 10 latest newsfeed. ')] = None) -> dict: 
    '''*This endpoint is deprecating Get general latest newsfeed or specific newsfeed by symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-newsfeed'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'region': region,
        'start_uuid': start_uuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List latest general news or video feeds or news relating to a symbol, the result may be empty if there is no news in that region'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list'
    headers = {'Content-Type': 'text/plain', 'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def v2_get_details(uuid: Annotated[str, Field(description='The value of id field returned in .../news/v2/list endpoint. Ex : 375879c0-08f3-32fb-8aaf-523c93ff8792')],
                   region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None) -> dict: 
    '''Read the specific news in details'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'uuid': uuid,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list(category: Annotated[str, Field(description='One of the following : generalnews or videofeed or symbol (only one at a time) ')],
              region: Annotated[str, Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG ')],
              start_uuid: Annotated[Union[str, None], Field(description='Get suitable value of more/result/uuid returned right in this endpoint to load news in the next page ')] = None) -> dict: 
    '''*This endpoint is deprecating List latest general news or video feeds or news relating to a symbol, the result may be empty if there is no news in that region'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'region': region,
        'start_uuid': start_uuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_get_details(uuid: Annotated[str, Field(description='The value of uuid field returned in .../news/list endpoint. Ex : 375879c0-08f3-32fb-8aaf-523c93ff8792 ')]) -> dict: 
    '''*This endpoint is deprecating Read the specific news in details'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/get-details'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'uuid': uuid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_list_by_ticker(ticker: Annotated[str, Field(description='The value of symbol field returned in …/auto-complete endpoint')]) -> dict: 
    '''Get screener IDs related to a ticker'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/list-by-ticker'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_get_symbols_by_predefined(scrIds: Annotated[str, Field(description='The value of canonicalName field returned in …/screeners/list-by-ticker endpoint OR one of the following : MOST_ACTIVES|DAY_GAINERS|DAY_LOSERS|AUTO_MANUFACTURERS|MS_CONSUMER_CYCLICAL|MOST_WATCHED_TICKERS|all_cryptocurrencies_us')],
                                        start: Annotated[Union[int, float, None], Field(description='The offset for paging purpose Default: 0')] = None,
                                        count: Annotated[Union[int, float, None], Field(description='The number of items per response for paging purpose Default: 100')] = None) -> dict: 
    '''Get symbols related to a predefined screener'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/get-symbols-by-predefined'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'scrIds': scrIds,
        'start': start,
        'count': count,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def screeners_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List gainers, losers, most active stickers, mutual fund, ETF, etc… from different categories, exchanges, etc with optional filters'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/list'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def screeners_get_filters(region: Annotated[Union[str, None], Field(description='One of the following : US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                          quoteType: Annotated[Union[str, None], Field(description='One of the following : equity | etf | mutualfund | future | option | cryptocurrency | index | insider_transaction')] = None,
                          category: Annotated[Union[str, None], Field(description='Different quoteType supports different category and allows the following values : analyst_rating|balance_sheet|cash_flow|cashflowstatement|changes_in_price_and_market_cap|changes_in_volume_and_ownership|debt_ratios|dividends_and_splits|earnings|eps_and_income_statement|esg_scores|esgscores|fair_value|feesandexpenses|financials|fundamentals|historicalperformance|income|keystats|liquidity_ratios|morningstar_rating|popular_filters|portfoliostatistics|profile|profitability_ratios_and_dividends|purchasedetails|ratios|sector_industry|short_interest|signals|trailingperformance|valuation|valuation_metric|visualizations')] = None) -> dict: 
    '''Get optional filters for later use in .../screeners/list endpoint'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/screeners/get-filters'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'region': region,
        'quoteType': quoteType,
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def conversations_count(messageBoardId: Annotated[str, Field(description='The value of messageBoardId field returned in …/market/v2/get-quotes endpoint')]) -> dict: 
    '''Count total conversations relating to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/count'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'messageBoardId': messageBoardId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def conversations_list(symbol: Annotated[str, Field(description='The value of symbol field returned in .../auto-complete endpoint')],
                       messageBoardId: Annotated[str, Field(description='The value of messageBoardId field returned in .../market/get-quotes endpoint')],
                       region: Annotated[Union[str, None], Field(description='One of the following is allowed US|BR|AU|CA|FR|DE|HK|IN|IT|ES|GB|SG')] = None,
                       userActivity: Annotated[Union[bool, None], Field(description='Whether or not return current number of interacting users')] = None,
                       sortBy: Annotated[Union[str, None], Field(description='One of the following createdAt | popular')] = None,
                       off: Annotated[Union[int, float, None], Field(description='The offset to start loading messages. It is fixed at 10 messages returned per response. Ex : 0 -> 9 -> 19 -> 29 -> 39 -> ... Default: 0')] = None) -> dict: 
    '''List conversations relating to a symbol'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/list'
    headers = {'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'messageBoardId': messageBoardId,
        'region': region,
        'userActivity': userActivity,
        'sortBy': sortBy,
        'off': off,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_count_events(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Count the number of events happening in a period of time'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/calendar/count-events'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def calendar_get_events(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get events happening in a period of time'''
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/calendar/get-events'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'apidojo-yahoo-finance-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
