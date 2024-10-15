# SNMP MIB module (INKTOMI-TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INKTOMI-TS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:24 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

inktomiTrafficServerMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 1, 1, 2)
)
inktomiTrafficServerMibModule.setRevisions(
        ("1901-03-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VendorInktomi_ObjectIdentity = ObjectIdentity
vendorInktomi = _VendorInktomi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967)
)
_InktomiReg_ObjectIdentity = ObjectIdentity
inktomiReg = _InktomiReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 1)
)
_InktomiModules_ObjectIdentity = ObjectIdentity
inktomiModules = _InktomiModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 1, 1)
)
_InktomiGlobalRegModule_ObjectIdentity = ObjectIdentity
inktomiGlobalRegModule = _InktomiGlobalRegModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 1, 1, 1)
)
_InktomiGeneric_ObjectIdentity = ObjectIdentity
inktomiGeneric = _InktomiGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 2)
)
_InktomiProducts_ObjectIdentity = ObjectIdentity
inktomiProducts = _InktomiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3)
)
_InktomiTSMIBs_ObjectIdentity = ObjectIdentity
inktomiTSMIBs = _InktomiTSMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1)
)
_InktomiTSConformance_ObjectIdentity = ObjectIdentity
inktomiTSConformance = _InktomiTSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 1)
)
_InktomiTSObjs_ObjectIdentity = ObjectIdentity
inktomiTSObjs = _InktomiTSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2)
)
_TSProtocols_ObjectIdentity = ObjectIdentity
tSProtocols = _TSProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tSProtocols.setStatus("current")
_TsProtocolSummary_ObjectIdentity = ObjectIdentity
tsProtocolSummary = _TsProtocolSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tsProtocolSummary.setStatus("current")
_TsClientThroughputOutKBit_Type = Gauge32
_TsClientThroughputOutKBit_Object = MibScalar
tsClientThroughputOutKBit = _TsClientThroughputOutKBit_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1, 1),
    _TsClientThroughputOutKBit_Type()
)
tsClientThroughputOutKBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClientThroughputOutKBit.setStatus("current")
_TsDocumentHitRate_Type = Gauge32
_TsDocumentHitRate_Object = MibScalar
tsDocumentHitRate = _TsDocumentHitRate_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1, 2),
    _TsDocumentHitRate_Type()
)
tsDocumentHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsDocumentHitRate.setStatus("current")
_TsBandwidthSavingsRatio_Type = Gauge32
_TsBandwidthSavingsRatio_Object = MibScalar
tsBandwidthSavingsRatio = _TsBandwidthSavingsRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1, 3),
    _TsBandwidthSavingsRatio_Type()
)
tsBandwidthSavingsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsBandwidthSavingsRatio.setStatus("current")
_TsServerConnections_Type = Gauge32
_TsServerConnections_Object = MibScalar
tsServerConnections = _TsServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1, 4),
    _TsServerConnections_Type()
)
tsServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsServerConnections.setStatus("current")
_TsClientConnections_Type = Gauge32
_TsClientConnections_Object = MibScalar
tsClientConnections = _TsClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 1, 5),
    _TsClientConnections_Type()
)
tsClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClientConnections.setStatus("current")
_TsProtocolClusterSummary_ObjectIdentity = ObjectIdentity
tsProtocolClusterSummary = _TsProtocolClusterSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tsProtocolClusterSummary.setStatus("current")
_TsClusterClientThroughputOutKBit_Type = Gauge32
_TsClusterClientThroughputOutKBit_Object = MibScalar
tsClusterClientThroughputOutKBit = _TsClusterClientThroughputOutKBit_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2, 1),
    _TsClusterClientThroughputOutKBit_Type()
)
tsClusterClientThroughputOutKBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterClientThroughputOutKBit.setStatus("current")
_TsClusterDocumentHitRate_Type = Gauge32
_TsClusterDocumentHitRate_Object = MibScalar
tsClusterDocumentHitRate = _TsClusterDocumentHitRate_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2, 2),
    _TsClusterDocumentHitRate_Type()
)
tsClusterDocumentHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterDocumentHitRate.setStatus("current")
_TsClusterBandwidthSavingsRatio_Type = Gauge32
_TsClusterBandwidthSavingsRatio_Object = MibScalar
tsClusterBandwidthSavingsRatio = _TsClusterBandwidthSavingsRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2, 3),
    _TsClusterBandwidthSavingsRatio_Type()
)
tsClusterBandwidthSavingsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterBandwidthSavingsRatio.setStatus("current")
_TsClusterServerConnections_Type = Gauge32
_TsClusterServerConnections_Object = MibScalar
tsClusterServerConnections = _TsClusterServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2, 4),
    _TsClusterServerConnections_Type()
)
tsClusterServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterServerConnections.setStatus("current")
_TsClusterClientConnections_Type = Gauge32
_TsClusterClientConnections_Object = MibScalar
tsClusterClientConnections = _TsClusterClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 2, 5),
    _TsClusterClientConnections_Type()
)
tsClusterClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterClientConnections.setStatus("current")
_TsProtocolHTTP_ObjectIdentity = ObjectIdentity
tsProtocolHTTP = _TsProtocolHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tsProtocolHTTP.setStatus("current")
_TsHttpStats_ObjectIdentity = ObjectIdentity
tsHttpStats = _TsHttpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tsHttpStats.setStatus("current")
_HttpXacts_Type = Gauge32
_HttpXacts_Object = MibScalar
httpXacts = _HttpXacts_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 1),
    _HttpXacts_Type()
)
httpXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpXacts.setStatus("current")
_HttpThroughput_Type = Gauge32
_HttpThroughput_Object = MibScalar
httpThroughput = _HttpThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 2),
    _HttpThroughput_Type()
)
httpThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpThroughput.setStatus("current")
_HttpCurrentlyOpenUA_Type = Gauge32
_HttpCurrentlyOpenUA_Object = MibScalar
httpCurrentlyOpenUA = _HttpCurrentlyOpenUA_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 3),
    _HttpCurrentlyOpenUA_Type()
)
httpCurrentlyOpenUA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpCurrentlyOpenUA.setStatus("current")
_HttpHitRatio_Type = Gauge32
_HttpHitRatio_Object = MibScalar
httpHitRatio = _HttpHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 4),
    _HttpHitRatio_Type()
)
httpHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHitRatio.setStatus("current")
_HttpBandwidthSavingsRatio_Type = Gauge32
_HttpBandwidthSavingsRatio_Object = MibScalar
httpBandwidthSavingsRatio = _HttpBandwidthSavingsRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 5),
    _HttpBandwidthSavingsRatio_Type()
)
httpBandwidthSavingsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpBandwidthSavingsRatio.setStatus("current")
_HttpCurrentlyOpenOrigin_Type = Gauge32
_HttpCurrentlyOpenOrigin_Object = MibScalar
httpCurrentlyOpenOrigin = _HttpCurrentlyOpenOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 6),
    _HttpCurrentlyOpenOrigin_Type()
)
httpCurrentlyOpenOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpCurrentlyOpenOrigin.setStatus("current")
_HttpUserAgentDocumentBytes_Type = Counter64
_HttpUserAgentDocumentBytes_Object = MibScalar
httpUserAgentDocumentBytes = _HttpUserAgentDocumentBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 7),
    _HttpUserAgentDocumentBytes_Type()
)
httpUserAgentDocumentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentDocumentBytes.setStatus("current")
_HttpUserAgentHeaderBytes_Type = Counter64
_HttpUserAgentHeaderBytes_Object = MibScalar
httpUserAgentHeaderBytes = _HttpUserAgentHeaderBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 8),
    _HttpUserAgentHeaderBytes_Type()
)
httpUserAgentHeaderBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentHeaderBytes.setStatus("current")
_HttpUserAgentConnections_Type = Counter32
_HttpUserAgentConnections_Object = MibScalar
httpUserAgentConnections = _HttpUserAgentConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 9),
    _HttpUserAgentConnections_Type()
)
httpUserAgentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentConnections.setStatus("current")
_HttpUserAgentTransactionsInProgress_Type = Gauge32
_HttpUserAgentTransactionsInProgress_Object = MibScalar
httpUserAgentTransactionsInProgress = _HttpUserAgentTransactionsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 10),
    _HttpUserAgentTransactionsInProgress_Type()
)
httpUserAgentTransactionsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentTransactionsInProgress.setStatus("current")
_HttpOriginServerTotalTransactions_Type = Counter32
_HttpOriginServerTotalTransactions_Object = MibScalar
httpOriginServerTotalTransactions = _HttpOriginServerTotalTransactions_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 11),
    _HttpOriginServerTotalTransactions_Type()
)
httpOriginServerTotalTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerTotalTransactions.setStatus("current")
_HttpOriginServerTransactionsInProgress_Type = Gauge32
_HttpOriginServerTransactionsInProgress_Object = MibScalar
httpOriginServerTransactionsInProgress = _HttpOriginServerTransactionsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 12),
    _HttpOriginServerTransactionsInProgress_Type()
)
httpOriginServerTransactionsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerTransactionsInProgress.setStatus("current")
_HttpOriginServerDocumentBytes_Type = Counter64
_HttpOriginServerDocumentBytes_Object = MibScalar
httpOriginServerDocumentBytes = _HttpOriginServerDocumentBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 13),
    _HttpOriginServerDocumentBytes_Type()
)
httpOriginServerDocumentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerDocumentBytes.setStatus("current")
_HttpOriginServerHeaderBytes_Type = Counter64
_HttpOriginServerHeaderBytes_Object = MibScalar
httpOriginServerHeaderBytes = _HttpOriginServerHeaderBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 14),
    _HttpOriginServerHeaderBytes_Type()
)
httpOriginServerHeaderBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerHeaderBytes.setStatus("current")
_HttpOriginServerConnections_Type = Counter32
_HttpOriginServerConnections_Object = MibScalar
httpOriginServerConnections = _HttpOriginServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 15),
    _HttpOriginServerConnections_Type()
)
httpOriginServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerConnections.setStatus("current")
_HttpOriginServerResponseBytes_Type = Counter64
_HttpOriginServerResponseBytes_Object = MibScalar
httpOriginServerResponseBytes = _HttpOriginServerResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 16),
    _HttpOriginServerResponseBytes_Type()
)
httpOriginServerResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpOriginServerResponseBytes.setStatus("current")
_HttpUserAgentResponseBytes_Type = Counter64
_HttpUserAgentResponseBytes_Object = MibScalar
httpUserAgentResponseBytes = _HttpUserAgentResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 17),
    _HttpUserAgentResponseBytes_Type()
)
httpUserAgentResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentResponseBytes.setStatus("current")
_HttpUserAgentTransactions_Type = Counter32
_HttpUserAgentTransactions_Object = MibScalar
httpUserAgentTransactions = _HttpUserAgentTransactions_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 18),
    _HttpUserAgentTransactions_Type()
)
httpUserAgentTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpUserAgentTransactions.setStatus("current")
_HttpTransactionErrorsPossbileAbortsMsec_Type = Gauge32
_HttpTransactionErrorsPossbileAbortsMsec_Object = MibScalar
httpTransactionErrorsPossbileAbortsMsec = _HttpTransactionErrorsPossbileAbortsMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 19),
    _HttpTransactionErrorsPossbileAbortsMsec_Type()
)
httpTransactionErrorsPossbileAbortsMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsPossbileAbortsMsec.setStatus("current")
_HttpTransactionMissChangedMsec_Type = Gauge32
_HttpTransactionMissChangedMsec_Object = MibScalar
httpTransactionMissChangedMsec = _HttpTransactionMissChangedMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 20),
    _HttpTransactionMissChangedMsec_Type()
)
httpTransactionMissChangedMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissChangedMsec.setStatus("current")
_HttpTransactionHitRevalidatedMsec_Type = Gauge32
_HttpTransactionHitRevalidatedMsec_Object = MibScalar
httpTransactionHitRevalidatedMsec = _HttpTransactionHitRevalidatedMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 21),
    _HttpTransactionHitRevalidatedMsec_Type()
)
httpTransactionHitRevalidatedMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionHitRevalidatedMsec.setStatus("current")
_HttpTransactionErrorsOtherMsec_Type = Gauge32
_HttpTransactionErrorsOtherMsec_Object = MibScalar
httpTransactionErrorsOtherMsec = _HttpTransactionErrorsOtherMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 22),
    _HttpTransactionErrorsOtherMsec_Type()
)
httpTransactionErrorsOtherMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsOtherMsec.setStatus("current")
_HttpTransactionErrorsAbortsMsec_Type = Gauge32
_HttpTransactionErrorsAbortsMsec_Object = MibScalar
httpTransactionErrorsAbortsMsec = _HttpTransactionErrorsAbortsMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 23),
    _HttpTransactionErrorsAbortsMsec_Type()
)
httpTransactionErrorsAbortsMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsAbortsMsec.setStatus("current")
_HttpTransactionErrorsEarlyHangupsMsec_Type = Gauge32
_HttpTransactionErrorsEarlyHangupsMsec_Object = MibScalar
httpTransactionErrorsEarlyHangupsMsec = _HttpTransactionErrorsEarlyHangupsMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 24),
    _HttpTransactionErrorsEarlyHangupsMsec_Type()
)
httpTransactionErrorsEarlyHangupsMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsEarlyHangupsMsec.setStatus("current")
_HttpTransactionErrorsEmptyHangupsMsec_Type = Gauge32
_HttpTransactionErrorsEmptyHangupsMsec_Object = MibScalar
httpTransactionErrorsEmptyHangupsMsec = _HttpTransactionErrorsEmptyHangupsMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 25),
    _HttpTransactionErrorsEmptyHangupsMsec_Type()
)
httpTransactionErrorsEmptyHangupsMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsEmptyHangupsMsec.setStatus("current")
_HttpTransactionOtherUnclassifiedMsec_Type = Gauge32
_HttpTransactionOtherUnclassifiedMsec_Object = MibScalar
httpTransactionOtherUnclassifiedMsec = _HttpTransactionOtherUnclassifiedMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 26),
    _HttpTransactionOtherUnclassifiedMsec_Type()
)
httpTransactionOtherUnclassifiedMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionOtherUnclassifiedMsec.setStatus("current")
_HttpTransactionErrorsPreAcceptHangupsMsec_Type = Gauge32
_HttpTransactionErrorsPreAcceptHangupsMsec_Object = MibScalar
httpTransactionErrorsPreAcceptHangupsMsec = _HttpTransactionErrorsPreAcceptHangupsMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 27),
    _HttpTransactionErrorsPreAcceptHangupsMsec_Type()
)
httpTransactionErrorsPreAcceptHangupsMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsPreAcceptHangupsMsec.setStatus("current")
_HttpTransactionMissClientNoCacheMsec_Type = Gauge32
_HttpTransactionMissClientNoCacheMsec_Object = MibScalar
httpTransactionMissClientNoCacheMsec = _HttpTransactionMissClientNoCacheMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 28),
    _HttpTransactionMissClientNoCacheMsec_Type()
)
httpTransactionMissClientNoCacheMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissClientNoCacheMsec.setStatus("current")
_HttpTransactionMissNotCachableMsec_Type = Gauge32
_HttpTransactionMissNotCachableMsec_Object = MibScalar
httpTransactionMissNotCachableMsec = _HttpTransactionMissNotCachableMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 29),
    _HttpTransactionMissNotCachableMsec_Type()
)
httpTransactionMissNotCachableMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissNotCachableMsec.setStatus("current")
_HttpTransactionHitFreshMsec_Type = Gauge32
_HttpTransactionHitFreshMsec_Object = MibScalar
httpTransactionHitFreshMsec = _HttpTransactionHitFreshMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 30),
    _HttpTransactionHitFreshMsec_Type()
)
httpTransactionHitFreshMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionHitFreshMsec.setStatus("current")
_HttpTransactionErrorsConnectFailedMsec_Type = Gauge32
_HttpTransactionErrorsConnectFailedMsec_Object = MibScalar
httpTransactionErrorsConnectFailedMsec = _HttpTransactionErrorsConnectFailedMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 31),
    _HttpTransactionErrorsConnectFailedMsec_Type()
)
httpTransactionErrorsConnectFailedMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsConnectFailedMsec.setStatus("current")
_HttpTransactionMissColdMsec_Type = Gauge32
_HttpTransactionMissColdMsec_Object = MibScalar
httpTransactionMissColdMsec = _HttpTransactionMissColdMsec_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 32),
    _HttpTransactionMissColdMsec_Type()
)
httpTransactionMissColdMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissColdMsec.setStatus("current")
_HttpTransactionErrorsPossibleAbortsPct_Type = Gauge32
_HttpTransactionErrorsPossibleAbortsPct_Object = MibScalar
httpTransactionErrorsPossibleAbortsPct = _HttpTransactionErrorsPossibleAbortsPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 33),
    _HttpTransactionErrorsPossibleAbortsPct_Type()
)
httpTransactionErrorsPossibleAbortsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsPossibleAbortsPct.setStatus("current")
_HttpTransactionErrorsPreAcceptHangupsPct_Type = Gauge32
_HttpTransactionErrorsPreAcceptHangupsPct_Object = MibScalar
httpTransactionErrorsPreAcceptHangupsPct = _HttpTransactionErrorsPreAcceptHangupsPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 34),
    _HttpTransactionErrorsPreAcceptHangupsPct_Type()
)
httpTransactionErrorsPreAcceptHangupsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsPreAcceptHangupsPct.setStatus("current")
_HttpTransactionMissChangedPct_Type = Gauge32
_HttpTransactionMissChangedPct_Object = MibScalar
httpTransactionMissChangedPct = _HttpTransactionMissChangedPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 35),
    _HttpTransactionMissChangedPct_Type()
)
httpTransactionMissChangedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissChangedPct.setStatus("current")
_HttpTransactionErrorsOtherPct_Type = Gauge32
_HttpTransactionErrorsOtherPct_Object = MibScalar
httpTransactionErrorsOtherPct = _HttpTransactionErrorsOtherPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 36),
    _HttpTransactionErrorsOtherPct_Type()
)
httpTransactionErrorsOtherPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsOtherPct.setStatus("current")
_HttpTransactionHitFreshPct_Type = Gauge32
_HttpTransactionHitFreshPct_Object = MibScalar
httpTransactionHitFreshPct = _HttpTransactionHitFreshPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 37),
    _HttpTransactionHitFreshPct_Type()
)
httpTransactionHitFreshPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionHitFreshPct.setStatus("current")
_HttpTransactionErrorsConnectFailedPct_Type = Gauge32
_HttpTransactionErrorsConnectFailedPct_Object = MibScalar
httpTransactionErrorsConnectFailedPct = _HttpTransactionErrorsConnectFailedPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 38),
    _HttpTransactionErrorsConnectFailedPct_Type()
)
httpTransactionErrorsConnectFailedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsConnectFailedPct.setStatus("current")
_HttpTransactionErrorsEarlyHangupsPct_Type = Gauge32
_HttpTransactionErrorsEarlyHangupsPct_Object = MibScalar
httpTransactionErrorsEarlyHangupsPct = _HttpTransactionErrorsEarlyHangupsPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 39),
    _HttpTransactionErrorsEarlyHangupsPct_Type()
)
httpTransactionErrorsEarlyHangupsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsEarlyHangupsPct.setStatus("current")
_HttpTransactionErrorsEmptyHangupsPct_Type = Gauge32
_HttpTransactionErrorsEmptyHangupsPct_Object = MibScalar
httpTransactionErrorsEmptyHangupsPct = _HttpTransactionErrorsEmptyHangupsPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 40),
    _HttpTransactionErrorsEmptyHangupsPct_Type()
)
httpTransactionErrorsEmptyHangupsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsEmptyHangupsPct.setStatus("current")
_HttpTransactionMissColdPct_Type = Gauge32
_HttpTransactionMissColdPct_Object = MibScalar
httpTransactionMissColdPct = _HttpTransactionMissColdPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 41),
    _HttpTransactionMissColdPct_Type()
)
httpTransactionMissColdPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissColdPct.setStatus("current")
_HttpTransactionOtherUnclassifiedPct_Type = Gauge32
_HttpTransactionOtherUnclassifiedPct_Object = MibScalar
httpTransactionOtherUnclassifiedPct = _HttpTransactionOtherUnclassifiedPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 42),
    _HttpTransactionOtherUnclassifiedPct_Type()
)
httpTransactionOtherUnclassifiedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionOtherUnclassifiedPct.setStatus("current")
_HttpTransactionHitRevalidatedPct_Type = Gauge32
_HttpTransactionHitRevalidatedPct_Object = MibScalar
httpTransactionHitRevalidatedPct = _HttpTransactionHitRevalidatedPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 43),
    _HttpTransactionHitRevalidatedPct_Type()
)
httpTransactionHitRevalidatedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionHitRevalidatedPct.setStatus("current")
_HttpTransactionMissClientNoCachePct_Type = Gauge32
_HttpTransactionMissClientNoCachePct_Object = MibScalar
httpTransactionMissClientNoCachePct = _HttpTransactionMissClientNoCachePct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 44),
    _HttpTransactionMissClientNoCachePct_Type()
)
httpTransactionMissClientNoCachePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissClientNoCachePct.setStatus("current")
_HttpTransactionMissNotCachablePct_Type = Gauge32
_HttpTransactionMissNotCachablePct_Object = MibScalar
httpTransactionMissNotCachablePct = _HttpTransactionMissNotCachablePct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 45),
    _HttpTransactionMissNotCachablePct_Type()
)
httpTransactionMissNotCachablePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionMissNotCachablePct.setStatus("current")
_HttpTransactionErrorsAbortsPct_Type = Gauge32
_HttpTransactionErrorsAbortsPct_Object = MibScalar
httpTransactionErrorsAbortsPct = _HttpTransactionErrorsAbortsPct_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 46),
    _HttpTransactionErrorsAbortsPct_Type()
)
httpTransactionErrorsAbortsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpTransactionErrorsAbortsPct.setStatus("current")
_HttpCurrentlyParentProxy_Type = Gauge32
_HttpCurrentlyParentProxy_Object = MibScalar
httpCurrentlyParentProxy = _HttpCurrentlyParentProxy_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 1, 47),
    _HttpCurrentlyParentProxy_Type()
)
httpCurrentlyParentProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpCurrentlyParentProxy.setStatus("current")
_TsHttpClusterStats_ObjectIdentity = ObjectIdentity
tsHttpClusterStats = _TsHttpClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tsHttpClusterStats.setStatus("current")
_ClusterHttpHitRatio_Type = Gauge32
_ClusterHttpHitRatio_Object = MibScalar
clusterHttpHitRatio = _ClusterHttpHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 1),
    _ClusterHttpHitRatio_Type()
)
clusterHttpHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpHitRatio.setStatus("current")
_ClusterBandwidthSavingsRatio_Type = Gauge32
_ClusterBandwidthSavingsRatio_Object = MibScalar
clusterBandwidthSavingsRatio = _ClusterBandwidthSavingsRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 2),
    _ClusterBandwidthSavingsRatio_Type()
)
clusterBandwidthSavingsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterBandwidthSavingsRatio.setStatus("current")
_ClusterHttpCurrentlyOpenUA_Type = Gauge32
_ClusterHttpCurrentlyOpenUA_Object = MibScalar
clusterHttpCurrentlyOpenUA = _ClusterHttpCurrentlyOpenUA_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 3),
    _ClusterHttpCurrentlyOpenUA_Type()
)
clusterHttpCurrentlyOpenUA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpCurrentlyOpenUA.setStatus("current")
_ClusterHttpCurrentlyOpenOrigin_Type = Gauge32
_ClusterHttpCurrentlyOpenOrigin_Object = MibScalar
clusterHttpCurrentlyOpenOrigin = _ClusterHttpCurrentlyOpenOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 4),
    _ClusterHttpCurrentlyOpenOrigin_Type()
)
clusterHttpCurrentlyOpenOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpCurrentlyOpenOrigin.setStatus("current")
_ClusterHttpThroughput_Type = Gauge32
_ClusterHttpThroughput_Object = MibScalar
clusterHttpThroughput = _ClusterHttpThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 5),
    _ClusterHttpThroughput_Type()
)
clusterHttpThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpThroughput.setStatus("current")
_ClusterHttpXacts_Type = Gauge32
_ClusterHttpXacts_Object = MibScalar
clusterHttpXacts = _ClusterHttpXacts_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 6),
    _ClusterHttpXacts_Type()
)
clusterHttpXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpXacts.setStatus("current")
_ClusterHttpUserAgentResponseBytes_Type = Counter64
_ClusterHttpUserAgentResponseBytes_Object = MibScalar
clusterHttpUserAgentResponseBytes = _ClusterHttpUserAgentResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 7),
    _ClusterHttpUserAgentResponseBytes_Type()
)
clusterHttpUserAgentResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpUserAgentResponseBytes.setStatus("current")
_ClusterHttpOriginServerResponseBytes_Type = Counter64
_ClusterHttpOriginServerResponseBytes_Object = MibScalar
clusterHttpOriginServerResponseBytes = _ClusterHttpOriginServerResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 8),
    _ClusterHttpOriginServerResponseBytes_Type()
)
clusterHttpOriginServerResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpOriginServerResponseBytes.setStatus("current")
_ClusterHttpOriginServerTransactions_Type = Counter32
_ClusterHttpOriginServerTransactions_Object = MibScalar
clusterHttpOriginServerTransactions = _ClusterHttpOriginServerTransactions_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 9),
    _ClusterHttpOriginServerTransactions_Type()
)
clusterHttpOriginServerTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpOriginServerTransactions.setStatus("current")
_ClusterHttpUserAgentTransactions_Type = Counter32
_ClusterHttpUserAgentTransactions_Object = MibScalar
clusterHttpUserAgentTransactions = _ClusterHttpUserAgentTransactions_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 10),
    _ClusterHttpUserAgentTransactions_Type()
)
clusterHttpUserAgentTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpUserAgentTransactions.setStatus("current")
_ClusterHttpCurrentlyParentProxy_Type = Gauge32
_ClusterHttpCurrentlyParentProxy_Object = MibScalar
clusterHttpCurrentlyParentProxy = _ClusterHttpCurrentlyParentProxy_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 3, 2, 11),
    _ClusterHttpCurrentlyParentProxy_Type()
)
clusterHttpCurrentlyParentProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHttpCurrentlyParentProxy.setStatus("current")
_TsProtocolFTP_ObjectIdentity = ObjectIdentity
tsProtocolFTP = _TsProtocolFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tsProtocolFTP.setStatus("current")
_TsFTPStats_ObjectIdentity = ObjectIdentity
tsFTPStats = _TsFTPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tsFTPStats.setStatus("current")
_FtpCurrentlyOpenConnections_Type = Gauge32
_FtpCurrentlyOpenConnections_Object = MibScalar
ftpCurrentlyOpenConnections = _FtpCurrentlyOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 1),
    _FtpCurrentlyOpenConnections_Type()
)
ftpCurrentlyOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpCurrentlyOpenConnections.setStatus("current")
_FtpSuccessfulPASV_Type = Counter32
_FtpSuccessfulPASV_Object = MibScalar
ftpSuccessfulPASV = _FtpSuccessfulPASV_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 2),
    _FtpSuccessfulPASV_Type()
)
ftpSuccessfulPASV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpSuccessfulPASV.setStatus("current")
_FtpUnsuccessfulPASV_Type = Counter32
_FtpUnsuccessfulPASV_Object = MibScalar
ftpUnsuccessfulPASV = _FtpUnsuccessfulPASV_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 3),
    _FtpUnsuccessfulPASV_Type()
)
ftpUnsuccessfulPASV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUnsuccessfulPASV.setStatus("current")
_FtpSuccessfulPORT_Type = Counter32
_FtpSuccessfulPORT_Object = MibScalar
ftpSuccessfulPORT = _FtpSuccessfulPORT_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 4),
    _FtpSuccessfulPORT_Type()
)
ftpSuccessfulPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpSuccessfulPORT.setStatus("current")
_FtpUnsuccessfulPORT_Type = Counter32
_FtpUnsuccessfulPORT_Object = MibScalar
ftpUnsuccessfulPORT = _FtpUnsuccessfulPORT_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 5),
    _FtpUnsuccessfulPORT_Type()
)
ftpUnsuccessfulPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUnsuccessfulPORT.setStatus("current")
_FtpClientOpenConnections_Type = Gauge32
_FtpClientOpenConnections_Object = MibScalar
ftpClientOpenConnections = _FtpClientOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 6),
    _FtpClientOpenConnections_Type()
)
ftpClientOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientOpenConnections.setStatus("current")
_FtpClientBytesRead_Type = Counter64
_FtpClientBytesRead_Object = MibScalar
ftpClientBytesRead = _FtpClientBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 7),
    _FtpClientBytesRead_Type()
)
ftpClientBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientBytesRead.setStatus("current")
_FtpClientBytesWritten_Type = Counter64
_FtpClientBytesWritten_Object = MibScalar
ftpClientBytesWritten = _FtpClientBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 8),
    _FtpClientBytesWritten_Type()
)
ftpClientBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpClientBytesWritten.setStatus("current")
_FtpServerOpenConnections_Type = Gauge32
_FtpServerOpenConnections_Object = MibScalar
ftpServerOpenConnections = _FtpServerOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 9),
    _FtpServerOpenConnections_Type()
)
ftpServerOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpServerOpenConnections.setStatus("current")
_FtpServerBytesRead_Type = Counter64
_FtpServerBytesRead_Object = MibScalar
ftpServerBytesRead = _FtpServerBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 10),
    _FtpServerBytesRead_Type()
)
ftpServerBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpServerBytesRead.setStatus("current")
_FtpServerBytesWritten_Type = Counter64
_FtpServerBytesWritten_Object = MibScalar
ftpServerBytesWritten = _FtpServerBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 11),
    _FtpServerBytesWritten_Type()
)
ftpServerBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpServerBytesWritten.setStatus("current")
_FtpFileHits_Type = Counter32
_FtpFileHits_Object = MibScalar
ftpFileHits = _FtpFileHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 12),
    _FtpFileHits_Type()
)
ftpFileHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpFileHits.setStatus("current")
_FtpFileMisses_Type = Counter32
_FtpFileMisses_Object = MibScalar
ftpFileMisses = _FtpFileMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 13),
    _FtpFileMisses_Type()
)
ftpFileMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpFileMisses.setStatus("current")
_FtpCwdHits_Type = Counter32
_FtpCwdHits_Object = MibScalar
ftpCwdHits = _FtpCwdHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 14),
    _FtpCwdHits_Type()
)
ftpCwdHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpCwdHits.setStatus("current")
_FtpCwdMisses_Type = Counter32
_FtpCwdMisses_Object = MibScalar
ftpCwdMisses = _FtpCwdMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 15),
    _FtpCwdMisses_Type()
)
ftpCwdMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpCwdMisses.setStatus("current")
_FtpDirectoryHits_Type = Counter32
_FtpDirectoryHits_Object = MibScalar
ftpDirectoryHits = _FtpDirectoryHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 16),
    _FtpDirectoryHits_Type()
)
ftpDirectoryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpDirectoryHits.setStatus("current")
_FtpDirectoryMisses_Type = Counter32
_FtpDirectoryMisses_Object = MibScalar
ftpDirectoryMisses = _FtpDirectoryMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 1, 17),
    _FtpDirectoryMisses_Type()
)
ftpDirectoryMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpDirectoryMisses.setStatus("current")
_TsFTPClusterStats_ObjectIdentity = ObjectIdentity
tsFTPClusterStats = _TsFTPClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tsFTPClusterStats.setStatus("current")
_TsProtocolSOCKS_ObjectIdentity = ObjectIdentity
tsProtocolSOCKS = _TsProtocolSOCKS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tsProtocolSOCKS.setStatus("current")
_TsSOCKSStats_ObjectIdentity = ObjectIdentity
tsSOCKSStats = _TsSOCKSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tsSOCKSStats.setStatus("current")
_SocksUnsuccessfulConnections_Type = Counter32
_SocksUnsuccessfulConnections_Object = MibScalar
socksUnsuccessfulConnections = _SocksUnsuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5, 1, 1),
    _SocksUnsuccessfulConnections_Type()
)
socksUnsuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksUnsuccessfulConnections.setStatus("current")
_SocksSuccessfulConnections_Type = Counter32
_SocksSuccessfulConnections_Object = MibScalar
socksSuccessfulConnections = _SocksSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5, 1, 2),
    _SocksSuccessfulConnections_Type()
)
socksSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksSuccessfulConnections.setStatus("current")
_SocksOpenConnections_Type = Gauge32
_SocksOpenConnections_Object = MibScalar
socksOpenConnections = _SocksOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5, 1, 3),
    _SocksOpenConnections_Type()
)
socksOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksOpenConnections.setStatus("current")
_TsSOCKSClusterStats_ObjectIdentity = ObjectIdentity
tsSOCKSClusterStats = _TsSOCKSClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tsSOCKSClusterStats.setStatus("current")
_TsProtocolNNTP_ObjectIdentity = ObjectIdentity
tsProtocolNNTP = _TsProtocolNNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tsProtocolNNTP.setStatus("current")
_TsNNTPStats_ObjectIdentity = ObjectIdentity
tsNNTPStats = _TsNNTPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tsNNTPStats.setStatus("current")
_NntpClientOpenConnections_Type = Gauge32
_NntpClientOpenConnections_Object = MibScalar
nntpClientOpenConnections = _NntpClientOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 1),
    _NntpClientOpenConnections_Type()
)
nntpClientOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClientOpenConnections.setStatus("current")
_NntpServerOpenConnections_Type = Gauge32
_NntpServerOpenConnections_Object = MibScalar
nntpServerOpenConnections = _NntpServerOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 2),
    _NntpServerOpenConnections_Type()
)
nntpServerOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpServerOpenConnections.setStatus("current")
_NntpArticleHits_Type = Counter32
_NntpArticleHits_Object = MibScalar
nntpArticleHits = _NntpArticleHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 3),
    _NntpArticleHits_Type()
)
nntpArticleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpArticleHits.setStatus("current")
_NntpArticleMisses_Type = Counter32
_NntpArticleMisses_Object = MibScalar
nntpArticleMisses = _NntpArticleMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 4),
    _NntpArticleMisses_Type()
)
nntpArticleMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpArticleMisses.setStatus("current")
_NntpClientBytesWritten_Type = Counter32
_NntpClientBytesWritten_Object = MibScalar
nntpClientBytesWritten = _NntpClientBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 5),
    _NntpClientBytesWritten_Type()
)
nntpClientBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClientBytesWritten.setStatus("current")
_NntpClientBytesRead_Type = Counter32
_NntpClientBytesRead_Object = MibScalar
nntpClientBytesRead = _NntpClientBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 6),
    _NntpClientBytesRead_Type()
)
nntpClientBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClientBytesRead.setStatus("current")
_NntpFeedBytes_Type = Counter64
_NntpFeedBytes_Object = MibScalar
nntpFeedBytes = _NntpFeedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 7),
    _NntpFeedBytes_Type()
)
nntpFeedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpFeedBytes.setStatus("current")
_NntpPullBytes_Type = Counter64
_NntpPullBytes_Object = MibScalar
nntpPullBytes = _NntpPullBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 8),
    _NntpPullBytes_Type()
)
nntpPullBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpPullBytes.setStatus("current")
_NntpGroupHits_Type = Counter32
_NntpGroupHits_Object = MibScalar
nntpGroupHits = _NntpGroupHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 9),
    _NntpGroupHits_Type()
)
nntpGroupHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpGroupHits.setStatus("current")
_NntpGroupRefreshes_Type = Counter32
_NntpGroupRefreshes_Object = MibScalar
nntpGroupRefreshes = _NntpGroupRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 10),
    _NntpGroupRefreshes_Type()
)
nntpGroupRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpGroupRefreshes.setStatus("current")
_NntpOverviewHits_Type = Counter32
_NntpOverviewHits_Object = MibScalar
nntpOverviewHits = _NntpOverviewHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 11),
    _NntpOverviewHits_Type()
)
nntpOverviewHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpOverviewHits.setStatus("current")
_NntpOverviewRefreshes_Type = Counter32
_NntpOverviewRefreshes_Object = MibScalar
nntpOverviewRefreshes = _NntpOverviewRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 12),
    _NntpOverviewRefreshes_Type()
)
nntpOverviewRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpOverviewRefreshes.setStatus("current")
_NntpPostBytes_Type = Counter64
_NntpPostBytes_Object = MibScalar
nntpPostBytes = _NntpPostBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 13),
    _NntpPostBytes_Type()
)
nntpPostBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpPostBytes.setStatus("current")
_NntpPosts_Type = Counter32
_NntpPosts_Object = MibScalar
nntpPosts = _NntpPosts_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 14),
    _NntpPosts_Type()
)
nntpPosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpPosts.setStatus("current")
_NntpServerBytesRead_Type = Counter32
_NntpServerBytesRead_Object = MibScalar
nntpServerBytesRead = _NntpServerBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 15),
    _NntpServerBytesRead_Type()
)
nntpServerBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpServerBytesRead.setStatus("current")
_NntpServerBytesWritten_Type = Counter32
_NntpServerBytesWritten_Object = MibScalar
nntpServerBytesWritten = _NntpServerBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 16),
    _NntpServerBytesWritten_Type()
)
nntpServerBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpServerBytesWritten.setStatus("current")
_NntpUpstreamTotalBytes_Type = Counter64
_NntpUpstreamTotalBytes_Object = MibScalar
nntpUpstreamTotalBytes = _NntpUpstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 17),
    _NntpUpstreamTotalBytes_Type()
)
nntpUpstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpUpstreamTotalBytes.setStatus("current")
_NntpDownstreamTotalBytes_Type = Counter64
_NntpDownstreamTotalBytes_Object = MibScalar
nntpDownstreamTotalBytes = _NntpDownstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 1, 18),
    _NntpDownstreamTotalBytes_Type()
)
nntpDownstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpDownstreamTotalBytes.setStatus("current")
_TsNNTPClusterStats_ObjectIdentity = ObjectIdentity
tsNNTPClusterStats = _TsNNTPClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tsNNTPClusterStats.setStatus("current")
_NntpClusterUpstreamTotalBytes_Type = Counter64
_NntpClusterUpstreamTotalBytes_Object = MibScalar
nntpClusterUpstreamTotalBytes = _NntpClusterUpstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 2, 1),
    _NntpClusterUpstreamTotalBytes_Type()
)
nntpClusterUpstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClusterUpstreamTotalBytes.setStatus("current")
_NntpClusterDownstreamTotalBytes_Type = Counter64
_NntpClusterDownstreamTotalBytes_Object = MibScalar
nntpClusterDownstreamTotalBytes = _NntpClusterDownstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 2, 2),
    _NntpClusterDownstreamTotalBytes_Type()
)
nntpClusterDownstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClusterDownstreamTotalBytes.setStatus("current")
_NntpClusterClientOpenConnections_Type = Gauge32
_NntpClusterClientOpenConnections_Object = MibScalar
nntpClusterClientOpenConnections = _NntpClusterClientOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 2, 3),
    _NntpClusterClientOpenConnections_Type()
)
nntpClusterClientOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClusterClientOpenConnections.setStatus("current")
_NntpClusterServerOpenConnections_Type = Gauge32
_NntpClusterServerOpenConnections_Object = MibScalar
nntpClusterServerOpenConnections = _NntpClusterServerOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 6, 2, 4),
    _NntpClusterServerOpenConnections_Type()
)
nntpClusterServerOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nntpClusterServerOpenConnections.setStatus("current")
_TsProtocolRNI_ObjectIdentity = ObjectIdentity
tsProtocolRNI = _TsProtocolRNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tsProtocolRNI.setStatus("current")
_TsRNIStats_ObjectIdentity = ObjectIdentity
tsRNIStats = _TsRNIStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tsRNIStats.setStatus("current")
_RniObjectCount_Type = Counter32
_RniObjectCount_Object = MibScalar
rniObjectCount = _RniObjectCount_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 1),
    _RniObjectCount_Type()
)
rniObjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniObjectCount.setStatus("current")
_RniBlockHitCount_Type = Counter32
_RniBlockHitCount_Object = MibScalar
rniBlockHitCount = _RniBlockHitCount_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 2),
    _RniBlockHitCount_Type()
)
rniBlockHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniBlockHitCount.setStatus("current")
_RniBlockMissCount_Type = Counter32
_RniBlockMissCount_Object = MibScalar
rniBlockMissCount = _RniBlockMissCount_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 3),
    _RniBlockMissCount_Type()
)
rniBlockMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniBlockMissCount.setStatus("current")
_RniByteHitSum_Type = Counter32
_RniByteHitSum_Object = MibScalar
rniByteHitSum = _RniByteHitSum_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 4),
    _RniByteHitSum_Type()
)
rniByteHitSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniByteHitSum.setStatus("current")
_RniByteMissSum_Type = Counter32
_RniByteMissSum_Object = MibScalar
rniByteMissSum = _RniByteMissSum_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 5),
    _RniByteMissSum_Type()
)
rniByteMissSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniByteMissSum.setStatus("current")
_RniCurrentClientConnections_Type = Gauge32
_RniCurrentClientConnections_Object = MibScalar
rniCurrentClientConnections = _RniCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 6),
    _RniCurrentClientConnections_Type()
)
rniCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniCurrentClientConnections.setStatus("current")
_RniDownstreamRequests_Type = Counter32
_RniDownstreamRequests_Object = MibScalar
rniDownstreamRequests = _RniDownstreamRequests_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 7),
    _RniDownstreamRequests_Type()
)
rniDownstreamRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniDownstreamRequests.setStatus("current")
_RniDownstreamRequestBytes_Type = Counter64
_RniDownstreamRequestBytes_Object = MibScalar
rniDownstreamRequestBytes = _RniDownstreamRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 8),
    _RniDownstreamRequestBytes_Type()
)
rniDownstreamRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniDownstreamRequestBytes.setStatus("current")
_RniDownstreamResponseBytes_Type = Counter64
_RniDownstreamResponseBytes_Object = MibScalar
rniDownstreamResponseBytes = _RniDownstreamResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 9),
    _RniDownstreamResponseBytes_Type()
)
rniDownstreamResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniDownstreamResponseBytes.setStatus("current")
_RniCurrentServerConnections_Type = Gauge32
_RniCurrentServerConnections_Object = MibScalar
rniCurrentServerConnections = _RniCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 10),
    _RniCurrentServerConnections_Type()
)
rniCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniCurrentServerConnections.setStatus("current")
_RniUpstreamRequests_Type = Counter32
_RniUpstreamRequests_Object = MibScalar
rniUpstreamRequests = _RniUpstreamRequests_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 11),
    _RniUpstreamRequests_Type()
)
rniUpstreamRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniUpstreamRequests.setStatus("current")
_RniUpstreamRequestBytes_Type = Counter64
_RniUpstreamRequestBytes_Object = MibScalar
rniUpstreamRequestBytes = _RniUpstreamRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 12),
    _RniUpstreamRequestBytes_Type()
)
rniUpstreamRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniUpstreamRequestBytes.setStatus("current")
_RniUpstreamResponseBytes_Type = Counter64
_RniUpstreamResponseBytes_Object = MibScalar
rniUpstreamResponseBytes = _RniUpstreamResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 1, 13),
    _RniUpstreamResponseBytes_Type()
)
rniUpstreamResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniUpstreamResponseBytes.setStatus("current")
_TsRNIClusterStats_ObjectIdentity = ObjectIdentity
tsRNIClusterStats = _TsRNIClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    tsRNIClusterStats.setStatus("current")
_RniClusterUpstreamTotalBytes_Type = Counter64
_RniClusterUpstreamTotalBytes_Object = MibScalar
rniClusterUpstreamTotalBytes = _RniClusterUpstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 1),
    _RniClusterUpstreamTotalBytes_Type()
)
rniClusterUpstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterUpstreamTotalBytes.setStatus("current")
_RniClusterDownstreamTotalBytes_Type = Counter64
_RniClusterDownstreamTotalBytes_Object = MibScalar
rniClusterDownstreamTotalBytes = _RniClusterDownstreamTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 2),
    _RniClusterDownstreamTotalBytes_Type()
)
rniClusterDownstreamTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterDownstreamTotalBytes.setStatus("current")
_RniClusterCurrentServerConnections_Type = Counter32
_RniClusterCurrentServerConnections_Object = MibScalar
rniClusterCurrentServerConnections = _RniClusterCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 3),
    _RniClusterCurrentServerConnections_Type()
)
rniClusterCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterCurrentServerConnections.setStatus("current")
_RniClusterCurrentClientConnections_Type = Counter32
_RniClusterCurrentClientConnections_Object = MibScalar
rniClusterCurrentClientConnections = _RniClusterCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 4),
    _RniClusterCurrentClientConnections_Type()
)
rniClusterCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterCurrentClientConnections.setStatus("current")
_RniClusterUserAgentXactsPerSecond_Type = Gauge32
_RniClusterUserAgentXactsPerSecond_Object = MibScalar
rniClusterUserAgentXactsPerSecond = _RniClusterUserAgentXactsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 5),
    _RniClusterUserAgentXactsPerSecond_Type()
)
rniClusterUserAgentXactsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterUserAgentXactsPerSecond.setStatus("current")
_RniClusterUserAgentsTotalDocumentsServed_Type = Counter32
_RniClusterUserAgentsTotalDocumentsServed_Object = MibScalar
rniClusterUserAgentsTotalDocumentsServed = _RniClusterUserAgentsTotalDocumentsServed_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 7, 2, 6),
    _RniClusterUserAgentsTotalDocumentsServed_Type()
)
rniClusterUserAgentsTotalDocumentsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rniClusterUserAgentsTotalDocumentsServed.setStatus("current")
_TsProtocolQT_ObjectIdentity = ObjectIdentity
tsProtocolQT = _TsProtocolQT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tsProtocolQT.setStatus("current")
_TsQTStats_ObjectIdentity = ObjectIdentity
tsQTStats = _TsQTStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tsQTStats.setStatus("current")
_QtClientRequestBytes_Type = Counter32
_QtClientRequestBytes_Object = MibScalar
qtClientRequestBytes = _QtClientRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 1),
    _QtClientRequestBytes_Type()
)
qtClientRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClientRequestBytes.setStatus("current")
_QtClientResponseBytes_Type = Counter32
_QtClientResponseBytes_Object = MibScalar
qtClientResponseBytes = _QtClientResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 2),
    _QtClientResponseBytes_Type()
)
qtClientResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClientResponseBytes.setStatus("current")
_QtServerRequestBytes_Type = Counter32
_QtServerRequestBytes_Object = MibScalar
qtServerRequestBytes = _QtServerRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 3),
    _QtServerRequestBytes_Type()
)
qtServerRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtServerRequestBytes.setStatus("current")
_QtServerResponseBytes_Type = Counter32
_QtServerResponseBytes_Object = MibScalar
qtServerResponseBytes = _QtServerResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 4),
    _QtServerResponseBytes_Type()
)
qtServerResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtServerResponseBytes.setStatus("current")
_QtCurrentClientConnections_Type = Counter32
_QtCurrentClientConnections_Object = MibScalar
qtCurrentClientConnections = _QtCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 5),
    _QtCurrentClientConnections_Type()
)
qtCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtCurrentClientConnections.setStatus("current")
_QtCurrentServerConnections_Type = Counter32
_QtCurrentServerConnections_Object = MibScalar
qtCurrentServerConnections = _QtCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 6),
    _QtCurrentServerConnections_Type()
)
qtCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtCurrentServerConnections.setStatus("current")
_QtCurrentLiveStreams_Type = Counter32
_QtCurrentLiveStreams_Object = MibScalar
qtCurrentLiveStreams = _QtCurrentLiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 7),
    _QtCurrentLiveStreams_Type()
)
qtCurrentLiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtCurrentLiveStreams.setStatus("current")
_QtClientServerBytesRead_Type = Counter32
_QtClientServerBytesRead_Object = MibScalar
qtClientServerBytesRead = _QtClientServerBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 8),
    _QtClientServerBytesRead_Type()
)
qtClientServerBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClientServerBytesRead.setStatus("current")
_QtClientCacheBytesRead_Type = Counter32
_QtClientCacheBytesRead_Object = MibScalar
qtClientCacheBytesRead = _QtClientCacheBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 1, 9),
    _QtClientCacheBytesRead_Type()
)
qtClientCacheBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClientCacheBytesRead.setStatus("current")
_TsQTClusterStats_ObjectIdentity = ObjectIdentity
tsQTClusterStats = _TsQTClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    tsQTClusterStats.setStatus("current")
_QtClusterServerTotalBytes_Type = Counter64
_QtClusterServerTotalBytes_Object = MibScalar
qtClusterServerTotalBytes = _QtClusterServerTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 1),
    _QtClusterServerTotalBytes_Type()
)
qtClusterServerTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterServerTotalBytes.setStatus("current")
_QtClusterClientTotalBytes_Type = Counter64
_QtClusterClientTotalBytes_Object = MibScalar
qtClusterClientTotalBytes = _QtClusterClientTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 2),
    _QtClusterClientTotalBytes_Type()
)
qtClusterClientTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterClientTotalBytes.setStatus("current")
_QtClusterCurrentServerConnections_Type = Counter32
_QtClusterCurrentServerConnections_Object = MibScalar
qtClusterCurrentServerConnections = _QtClusterCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 3),
    _QtClusterCurrentServerConnections_Type()
)
qtClusterCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterCurrentServerConnections.setStatus("current")
_QtClusterCurrentClientConnections_Type = Counter32
_QtClusterCurrentClientConnections_Object = MibScalar
qtClusterCurrentClientConnections = _QtClusterCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 4),
    _QtClusterCurrentClientConnections_Type()
)
qtClusterCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterCurrentClientConnections.setStatus("current")
_QtClusterUserAgentXactsPerSecond_Type = Gauge32
_QtClusterUserAgentXactsPerSecond_Object = MibScalar
qtClusterUserAgentXactsPerSecond = _QtClusterUserAgentXactsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 5),
    _QtClusterUserAgentXactsPerSecond_Type()
)
qtClusterUserAgentXactsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterUserAgentXactsPerSecond.setStatus("current")
_QtClusterUserAgentsTotalDocumentsServed_Type = Counter32
_QtClusterUserAgentsTotalDocumentsServed_Object = MibScalar
qtClusterUserAgentsTotalDocumentsServed = _QtClusterUserAgentsTotalDocumentsServed_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 8, 2, 6),
    _QtClusterUserAgentsTotalDocumentsServed_Type()
)
qtClusterUserAgentsTotalDocumentsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtClusterUserAgentsTotalDocumentsServed.setStatus("current")
_TsProtocolWMT_ObjectIdentity = ObjectIdentity
tsProtocolWMT = _TsProtocolWMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tsProtocolWMT.setStatus("current")
_TsWMTStats_ObjectIdentity = ObjectIdentity
tsWMTStats = _TsWMTStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tsWMTStats.setStatus("current")
_WmtClientRequestBytes_Type = Counter32
_WmtClientRequestBytes_Object = MibScalar
wmtClientRequestBytes = _WmtClientRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 1),
    _WmtClientRequestBytes_Type()
)
wmtClientRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClientRequestBytes.setStatus("current")
_WmtClientResponseBytes_Type = Counter32
_WmtClientResponseBytes_Object = MibScalar
wmtClientResponseBytes = _WmtClientResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 2),
    _WmtClientResponseBytes_Type()
)
wmtClientResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClientResponseBytes.setStatus("current")
_WmtServerRequestBytes_Type = Counter32
_WmtServerRequestBytes_Object = MibScalar
wmtServerRequestBytes = _WmtServerRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 3),
    _WmtServerRequestBytes_Type()
)
wmtServerRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtServerRequestBytes.setStatus("current")
_WmtServerResponseBytes_Type = Counter32
_WmtServerResponseBytes_Object = MibScalar
wmtServerResponseBytes = _WmtServerResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 4),
    _WmtServerResponseBytes_Type()
)
wmtServerResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtServerResponseBytes.setStatus("current")
_WmtCurrentClientConnections_Type = Counter32
_WmtCurrentClientConnections_Object = MibScalar
wmtCurrentClientConnections = _WmtCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 5),
    _WmtCurrentClientConnections_Type()
)
wmtCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtCurrentClientConnections.setStatus("current")
_WmtCurrentServerConnections_Type = Counter32
_WmtCurrentServerConnections_Object = MibScalar
wmtCurrentServerConnections = _WmtCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 1, 6),
    _WmtCurrentServerConnections_Type()
)
wmtCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtCurrentServerConnections.setStatus("current")
_TsWMTClusterStats_ObjectIdentity = ObjectIdentity
tsWMTClusterStats = _TsWMTClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tsWMTClusterStats.setStatus("current")
_WmtClusterServerTotalBytes_Type = Counter64
_WmtClusterServerTotalBytes_Object = MibScalar
wmtClusterServerTotalBytes = _WmtClusterServerTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 1),
    _WmtClusterServerTotalBytes_Type()
)
wmtClusterServerTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterServerTotalBytes.setStatus("current")
_WmtClusterClientTotalBytes_Type = Counter64
_WmtClusterClientTotalBytes_Object = MibScalar
wmtClusterClientTotalBytes = _WmtClusterClientTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 2),
    _WmtClusterClientTotalBytes_Type()
)
wmtClusterClientTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterClientTotalBytes.setStatus("current")
_WmtClusterCurrentServerConnections_Type = Counter32
_WmtClusterCurrentServerConnections_Object = MibScalar
wmtClusterCurrentServerConnections = _WmtClusterCurrentServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 3),
    _WmtClusterCurrentServerConnections_Type()
)
wmtClusterCurrentServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterCurrentServerConnections.setStatus("current")
_WmtClusterCurrentClientConnections_Type = Counter32
_WmtClusterCurrentClientConnections_Object = MibScalar
wmtClusterCurrentClientConnections = _WmtClusterCurrentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 4),
    _WmtClusterCurrentClientConnections_Type()
)
wmtClusterCurrentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterCurrentClientConnections.setStatus("current")
_WmtClusterUserAgentXactsPerSecond_Type = Gauge32
_WmtClusterUserAgentXactsPerSecond_Object = MibScalar
wmtClusterUserAgentXactsPerSecond = _WmtClusterUserAgentXactsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 5),
    _WmtClusterUserAgentXactsPerSecond_Type()
)
wmtClusterUserAgentXactsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterUserAgentXactsPerSecond.setStatus("current")
_WmtClusterUserAgentsTotalDocumentsServed_Type = Counter32
_WmtClusterUserAgentsTotalDocumentsServed_Object = MibScalar
wmtClusterUserAgentsTotalDocumentsServed = _WmtClusterUserAgentsTotalDocumentsServed_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 1, 9, 2, 6),
    _WmtClusterUserAgentsTotalDocumentsServed_Type()
)
wmtClusterUserAgentsTotalDocumentsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmtClusterUserAgentsTotalDocumentsServed.setStatus("current")
_TSEventSubsystem_ObjectIdentity = ObjectIdentity
tSEventSubsystem = _TSEventSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tSEventSubsystem.setStatus("current")
_TSCacheSubsystem_ObjectIdentity = ObjectIdentity
tSCacheSubsystem = _TSCacheSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tSCacheSubsystem.setStatus("current")
_TSICPStats_ObjectIdentity = ObjectIdentity
tSICPStats = _TSICPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tSICPStats.setStatus("current")
_TsICPRemoteQuery_Type = Counter32
_TsICPRemoteQuery_Object = MibScalar
tsICPRemoteQuery = _TsICPRemoteQuery_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 1),
    _TsICPRemoteQuery_Type()
)
tsICPRemoteQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPRemoteQuery.setStatus("current")
_TsICPRemoteResponses_Type = Counter32
_TsICPRemoteResponses_Object = MibScalar
tsICPRemoteResponses = _TsICPRemoteResponses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 2),
    _TsICPRemoteResponses_Type()
)
tsICPRemoteResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPRemoteResponses.setStatus("current")
_TsICPCacheLookupSuccess_Type = Counter32
_TsICPCacheLookupSuccess_Object = MibScalar
tsICPCacheLookupSuccess = _TsICPCacheLookupSuccess_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 3),
    _TsICPCacheLookupSuccess_Type()
)
tsICPCacheLookupSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPCacheLookupSuccess.setStatus("current")
_TsICPCacheLookupFail_Type = Counter32
_TsICPCacheLookupFail_Object = MibScalar
tsICPCacheLookupFail = _TsICPCacheLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 4),
    _TsICPCacheLookupFail_Type()
)
tsICPCacheLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPCacheLookupFail.setStatus("current")
_TsICPQueryResponseWrite_Type = Counter32
_TsICPQueryResponseWrite_Object = MibScalar
tsICPQueryResponseWrite = _TsICPQueryResponseWrite_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 5),
    _TsICPQueryResponseWrite_Type()
)
tsICPQueryResponseWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPQueryResponseWrite.setStatus("current")
_TsICPQueryHits_Type = Counter32
_TsICPQueryHits_Object = MibScalar
tsICPQueryHits = _TsICPQueryHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 6),
    _TsICPQueryHits_Type()
)
tsICPQueryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPQueryHits.setStatus("current")
_TsICPQueryMisses_Type = Counter32
_TsICPQueryMisses_Object = MibScalar
tsICPQueryMisses = _TsICPQueryMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 7),
    _TsICPQueryMisses_Type()
)
tsICPQueryMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPQueryMisses.setStatus("current")
_TsICPQueryRequests_Type = Counter32
_TsICPQueryRequests_Object = MibScalar
tsICPQueryRequests = _TsICPQueryRequests_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 8),
    _TsICPQueryRequests_Type()
)
tsICPQueryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPQueryRequests.setStatus("current")
_TsICPResponseTime_Type = Gauge32
_TsICPResponseTime_Object = MibScalar
tsICPResponseTime = _TsICPResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 9),
    _TsICPResponseTime_Type()
)
tsICPResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPResponseTime.setStatus("current")
_TsICPUDPSendQueries_Type = Counter32
_TsICPUDPSendQueries_Object = MibScalar
tsICPUDPSendQueries = _TsICPUDPSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 10),
    _TsICPUDPSendQueries_Type()
)
tsICPUDPSendQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPUDPSendQueries.setStatus("current")
_TsICPRequestTime_Type = Gauge32
_TsICPRequestTime_Object = MibScalar
tsICPRequestTime = _TsICPRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 1, 11),
    _TsICPRequestTime_Type()
)
tsICPRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsICPRequestTime.setStatus("current")
_TSCacheStats_ObjectIdentity = ObjectIdentity
tSCacheStats = _TSCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tSCacheStats.setStatus("current")
_TSCachePercentFree_Type = Gauge32
_TSCachePercentFree_Object = MibScalar
tSCachePercentFree = _TSCachePercentFree_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 1),
    _TSCachePercentFree_Type()
)
tSCachePercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCachePercentFree.setStatus("current")
_TSCacheHTTPHits_Type = Counter32
_TSCacheHTTPHits_Object = MibScalar
tSCacheHTTPHits = _TSCacheHTTPHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 2),
    _TSCacheHTTPHits_Type()
)
tSCacheHTTPHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheHTTPHits.setStatus("current")
_TSCacheHits_Type = Counter32
_TSCacheHits_Object = MibScalar
tSCacheHits = _TSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 3),
    _TSCacheHits_Type()
)
tSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheHits.setStatus("current")
_TSCacheMisses_Type = Counter32
_TSCacheMisses_Object = MibScalar
tSCacheMisses = _TSCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 4),
    _TSCacheMisses_Type()
)
tSCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheMisses.setStatus("current")
_TSCacheCurrentXfers_Type = Gauge32
_TSCacheCurrentXfers_Object = MibScalar
tSCacheCurrentXfers = _TSCacheCurrentXfers_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 5),
    _TSCacheCurrentXfers_Type()
)
tSCacheCurrentXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheCurrentXfers.setStatus("current")
_TSCacheBytesTotalMB_Type = Gauge32
_TSCacheBytesTotalMB_Object = MibScalar
tSCacheBytesTotalMB = _TSCacheBytesTotalMB_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 6),
    _TSCacheBytesTotalMB_Type()
)
tSCacheBytesTotalMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheBytesTotalMB.setStatus("current")
_TSCacheLinkActive_Type = Gauge32
_TSCacheLinkActive_Object = MibScalar
tSCacheLinkActive = _TSCacheLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 7),
    _TSCacheLinkActive_Type()
)
tSCacheLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLinkActive.setStatus("obsolete")
_TSCacheLinkFailures_Type = Counter32
_TSCacheLinkFailures_Object = MibScalar
tSCacheLinkFailures = _TSCacheLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 8),
    _TSCacheLinkFailures_Type()
)
tSCacheLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLinkFailures.setStatus("obsolete")
_TSCacheLinkSuccesses_Type = Counter32
_TSCacheLinkSuccesses_Object = MibScalar
tSCacheLinkSuccesses = _TSCacheLinkSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 9),
    _TSCacheLinkSuccesses_Type()
)
tSCacheLinkSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLinkSuccesses.setStatus("obsolete")
_TSCacheLookupActive_Type = Gauge32
_TSCacheLookupActive_Object = MibScalar
tSCacheLookupActive = _TSCacheLookupActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 10),
    _TSCacheLookupActive_Type()
)
tSCacheLookupActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLookupActive.setStatus("current")
_TSCacheLookupFailures_Type = Counter32
_TSCacheLookupFailures_Object = MibScalar
tSCacheLookupFailures = _TSCacheLookupFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 11),
    _TSCacheLookupFailures_Type()
)
tSCacheLookupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLookupFailures.setStatus("current")
_TSCacheLookupSuccesses_Type = Counter32
_TSCacheLookupSuccesses_Object = MibScalar
tSCacheLookupSuccesses = _TSCacheLookupSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 12),
    _TSCacheLookupSuccesses_Type()
)
tSCacheLookupSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheLookupSuccesses.setStatus("current")
_TSCacheReadActive_Type = Gauge32
_TSCacheReadActive_Object = MibScalar
tSCacheReadActive = _TSCacheReadActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 13),
    _TSCacheReadActive_Type()
)
tSCacheReadActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheReadActive.setStatus("current")
_TSCacheReadFailures_Type = Counter32
_TSCacheReadFailures_Object = MibScalar
tSCacheReadFailures = _TSCacheReadFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 14),
    _TSCacheReadFailures_Type()
)
tSCacheReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheReadFailures.setStatus("current")
_TSCacheReadSuccesses_Type = Counter32
_TSCacheReadSuccesses_Object = MibScalar
tSCacheReadSuccesses = _TSCacheReadSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 15),
    _TSCacheReadSuccesses_Type()
)
tSCacheReadSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheReadSuccesses.setStatus("current")
_TSCacheRemoveActive_Type = Gauge32
_TSCacheRemoveActive_Object = MibScalar
tSCacheRemoveActive = _TSCacheRemoveActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 16),
    _TSCacheRemoveActive_Type()
)
tSCacheRemoveActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheRemoveActive.setStatus("current")
_TSCacheRemoveFailures_Type = Counter32
_TSCacheRemoveFailures_Object = MibScalar
tSCacheRemoveFailures = _TSCacheRemoveFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 17),
    _TSCacheRemoveFailures_Type()
)
tSCacheRemoveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheRemoveFailures.setStatus("current")
_TSCacheRemoveSuccesses_Type = Counter32
_TSCacheRemoveSuccesses_Object = MibScalar
tSCacheRemoveSuccesses = _TSCacheRemoveSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 18),
    _TSCacheRemoveSuccesses_Type()
)
tSCacheRemoveSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheRemoveSuccesses.setStatus("current")
_TSCacheUpdateActive_Type = Gauge32
_TSCacheUpdateActive_Object = MibScalar
tSCacheUpdateActive = _TSCacheUpdateActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 19),
    _TSCacheUpdateActive_Type()
)
tSCacheUpdateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheUpdateActive.setStatus("current")
_TSCacheUpdateFailures_Type = Counter32
_TSCacheUpdateFailures_Object = MibScalar
tSCacheUpdateFailures = _TSCacheUpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 20),
    _TSCacheUpdateFailures_Type()
)
tSCacheUpdateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheUpdateFailures.setStatus("current")
_TSCacheUpdateSuccesses_Type = Counter32
_TSCacheUpdateSuccesses_Object = MibScalar
tSCacheUpdateSuccesses = _TSCacheUpdateSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 21),
    _TSCacheUpdateSuccesses_Type()
)
tSCacheUpdateSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheUpdateSuccesses.setStatus("current")
_TSCacheWriteActive_Type = Gauge32
_TSCacheWriteActive_Object = MibScalar
tSCacheWriteActive = _TSCacheWriteActive_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 22),
    _TSCacheWriteActive_Type()
)
tSCacheWriteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheWriteActive.setStatus("current")
_TSCacheWriteFailures_Type = Counter32
_TSCacheWriteFailures_Object = MibScalar
tSCacheWriteFailures = _TSCacheWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 23),
    _TSCacheWriteFailures_Type()
)
tSCacheWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheWriteFailures.setStatus("current")
_TSCacheWriteSuccesses_Type = Counter32
_TSCacheWriteSuccesses_Object = MibScalar
tSCacheWriteSuccesses = _TSCacheWriteSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 24),
    _TSCacheWriteSuccesses_Type()
)
tSCacheWriteSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheWriteSuccesses.setStatus("current")
_TSCacheConnections_Type = Gauge32
_TSCacheConnections_Object = MibScalar
tSCacheConnections = _TSCacheConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 2, 25),
    _TSCacheConnections_Type()
)
tSCacheConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSCacheConnections.setStatus("current")
_TSCacheClusterStats_ObjectIdentity = ObjectIdentity
tSCacheClusterStats = _TSCacheClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tSCacheClusterStats.setStatus("current")
_TSClusterCacheFreeMB_Type = Gauge32
_TSClusterCacheFreeMB_Object = MibScalar
tSClusterCacheFreeMB = _TSClusterCacheFreeMB_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 1),
    _TSClusterCacheFreeMB_Type()
)
tSClusterCacheFreeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheFreeMB.setStatus("current")
_TSClusterCachePercentFree_Type = Gauge32
_TSClusterCachePercentFree_Object = MibScalar
tSClusterCachePercentFree = _TSClusterCachePercentFree_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 2),
    _TSClusterCachePercentFree_Type()
)
tSClusterCachePercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCachePercentFree.setStatus("current")
_TSClusterCacheHTTPHits_Type = Counter32
_TSClusterCacheHTTPHits_Object = MibScalar
tSClusterCacheHTTPHits = _TSClusterCacheHTTPHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 3),
    _TSClusterCacheHTTPHits_Type()
)
tSClusterCacheHTTPHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheHTTPHits.setStatus("current")
_TSClusterCacheHits_Type = Counter32
_TSClusterCacheHits_Object = MibScalar
tSClusterCacheHits = _TSClusterCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 4),
    _TSClusterCacheHits_Type()
)
tSClusterCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheHits.setStatus("current")
_TSClusterCacheMisses_Type = Counter32
_TSClusterCacheMisses_Object = MibScalar
tSClusterCacheMisses = _TSClusterCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 5),
    _TSClusterCacheMisses_Type()
)
tSClusterCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheMisses.setStatus("current")
_TSClusterCacheCurrentXfers_Type = Gauge32
_TSClusterCacheCurrentXfers_Object = MibScalar
tSClusterCacheCurrentXfers = _TSClusterCacheCurrentXfers_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 6),
    _TSClusterCacheCurrentXfers_Type()
)
tSClusterCacheCurrentXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheCurrentXfers.setStatus("current")
_TSClusterCacheConnections_Type = Gauge32
_TSClusterCacheConnections_Object = MibScalar
tSClusterCacheConnections = _TSClusterCacheConnections_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 3, 7),
    _TSClusterCacheConnections_Type()
)
tSClusterCacheConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSClusterCacheConnections.setStatus("current")
_TSCacheGCSubsystem_ObjectIdentity = ObjectIdentity
tSCacheGCSubsystem = _TSCacheGCSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tSCacheGCSubsystem.setStatus("current")
_TSCacheEngineSubsystem_ObjectIdentity = ObjectIdentity
tSCacheEngineSubsystem = _TSCacheEngineSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tSCacheEngineSubsystem.setStatus("current")
_TSDiskSubsystem_ObjectIdentity = ObjectIdentity
tSDiskSubsystem = _TSDiskSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tSDiskSubsystem.setStatus("current")
_TSHostDBSubsystem_ObjectIdentity = ObjectIdentity
tSHostDBSubsystem = _TSHostDBSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tSHostDBSubsystem.setStatus("current")
_TsDNSStats_ObjectIdentity = ObjectIdentity
tsDNSStats = _TsDNSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tsDNSStats.setStatus("current")
_DnsTotalLookups_Type = Counter32
_DnsTotalLookups_Object = MibScalar
dnsTotalLookups = _DnsTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 1, 1),
    _DnsTotalLookups_Type()
)
dnsTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotalLookups.setStatus("current")
_DnsLookupRate_Type = Gauge32
_DnsLookupRate_Object = MibScalar
dnsLookupRate = _DnsLookupRate_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 1, 2),
    _DnsLookupRate_Type()
)
dnsLookupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsLookupRate.setStatus("current")
_DnsTotalLookupSuccesses_Type = Counter32
_DnsTotalLookupSuccesses_Object = MibScalar
dnsTotalLookupSuccesses = _DnsTotalLookupSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 1, 3),
    _DnsTotalLookupSuccesses_Type()
)
dnsTotalLookupSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsTotalLookupSuccesses.setStatus("current")
_DnsLookupTimeMs_Type = Gauge32
_DnsLookupTimeMs_Object = MibScalar
dnsLookupTimeMs = _DnsLookupTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 1, 4),
    _DnsLookupTimeMs_Type()
)
dnsLookupTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsLookupTimeMs.setStatus("current")
_TsClusterDNSStats_ObjectIdentity = ObjectIdentity
tsClusterDNSStats = _TsClusterDNSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tsClusterDNSStats.setStatus("current")
_TsClusterDNSTotalLookups_Type = Counter32
_TsClusterDNSTotalLookups_Object = MibScalar
tsClusterDNSTotalLookups = _TsClusterDNSTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 2, 1),
    _TsClusterDNSTotalLookups_Type()
)
tsClusterDNSTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterDNSTotalLookups.setStatus("current")
_TsClusterDNSLookupRate_Type = Gauge32
_TsClusterDNSLookupRate_Object = MibScalar
tsClusterDNSLookupRate = _TsClusterDNSLookupRate_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 2, 2),
    _TsClusterDNSLookupRate_Type()
)
tsClusterDNSLookupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsClusterDNSLookupRate.setStatus("current")
_TsHostDBStats_ObjectIdentity = ObjectIdentity
tsHostDBStats = _TsHostDBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tsHostDBStats.setStatus("current")
_HostDBTotalLookups_Type = Counter32
_HostDBTotalLookups_Object = MibScalar
hostDBTotalLookups = _HostDBTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 3, 1),
    _HostDBTotalLookups_Type()
)
hostDBTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDBTotalLookups.setStatus("current")
_HostDBTotalHits_Type = Counter32
_HostDBTotalHits_Object = MibScalar
hostDBTotalHits = _HostDBTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 3, 2),
    _HostDBTotalHits_Type()
)
hostDBTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDBTotalHits.setStatus("current")
_HostDBAverageTTL_Type = Gauge32
_HostDBAverageTTL_Object = MibScalar
hostDBAverageTTL = _HostDBAverageTTL_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 3, 3),
    _HostDBAverageTTL_Type()
)
hostDBAverageTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDBAverageTTL.setStatus("current")
_TSClusterHostDBStats_ObjectIdentity = ObjectIdentity
tSClusterHostDBStats = _TSClusterHostDBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    tSClusterHostDBStats.setStatus("current")
_ClusterHostdbHitRatio_Type = Gauge32
_ClusterHostdbHitRatio_Object = MibScalar
clusterHostdbHitRatio = _ClusterHostdbHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 5, 4, 1),
    _ClusterHostdbHitRatio_Type()
)
clusterHostdbHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHostdbHitRatio.setStatus("current")
_TSClusterSubsystem_ObjectIdentity = ObjectIdentity
tSClusterSubsystem = _TSClusterSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tSClusterSubsystem.setStatus("current")
_TsClusterNodeStats_ObjectIdentity = ObjectIdentity
tsClusterNodeStats = _TsClusterNodeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tsClusterNodeStats.setStatus("current")
_ClusterBytesRead_Type = Counter32
_ClusterBytesRead_Object = MibScalar
clusterBytesRead = _ClusterBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 1),
    _ClusterBytesRead_Type()
)
clusterBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterBytesRead.setStatus("current")
_ClusterBytesWritten_Type = Counter32
_ClusterBytesWritten_Object = MibScalar
clusterBytesWritten = _ClusterBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 2),
    _ClusterBytesWritten_Type()
)
clusterBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterBytesWritten.setStatus("current")
_ClusterConnectionsOpen_Type = Gauge32
_ClusterConnectionsOpen_Object = MibScalar
clusterConnectionsOpen = _ClusterConnectionsOpen_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 3),
    _ClusterConnectionsOpen_Type()
)
clusterConnectionsOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConnectionsOpen.setStatus("current")
_ClusterConnectionsOpened_Type = Counter32
_ClusterConnectionsOpened_Object = MibScalar
clusterConnectionsOpened = _ClusterConnectionsOpened_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 4),
    _ClusterConnectionsOpened_Type()
)
clusterConnectionsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConnectionsOpened.setStatus("current")
_ClusterNetBackups_Type = Counter32
_ClusterNetBackups_Object = MibScalar
clusterNetBackups = _ClusterNetBackups_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 5),
    _ClusterNetBackups_Type()
)
clusterNetBackups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetBackups.setStatus("current")
_ClusterNodeCount_Type = Gauge32
_ClusterNodeCount_Object = MibScalar
clusterNodeCount = _ClusterNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 1, 6),
    _ClusterNodeCount_Type()
)
clusterNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeCount.setStatus("current")
_TsClusterClusterStats_ObjectIdentity = ObjectIdentity
tsClusterClusterStats = _TsClusterClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    tsClusterClusterStats.setStatus("current")
_TsLoggingSubsystem_ObjectIdentity = ObjectIdentity
tsLoggingSubsystem = _TsLoggingSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tsLoggingSubsystem.setStatus("current")
_TsLogStats_ObjectIdentity = ObjectIdentity
tsLogStats = _TsLogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tsLogStats.setStatus("current")
_TsLogOpenFiles_Type = Gauge32
_TsLogOpenFiles_Object = MibScalar
tsLogOpenFiles = _TsLogOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1, 1),
    _TsLogOpenFiles_Type()
)
tsLogOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLogOpenFiles.setStatus("current")
_TsLogSpaceUsed_Type = Gauge32
_TsLogSpaceUsed_Object = MibScalar
tsLogSpaceUsed = _TsLogSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1, 2),
    _TsLogSpaceUsed_Type()
)
tsLogSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLogSpaceUsed.setStatus("current")
_TsLogAccessesLogged_Type = Counter32
_TsLogAccessesLogged_Object = MibScalar
tsLogAccessesLogged = _TsLogAccessesLogged_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1, 3),
    _TsLogAccessesLogged_Type()
)
tsLogAccessesLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLogAccessesLogged.setStatus("current")
_TsLogAccessesSkipped_Type = Counter32
_TsLogAccessesSkipped_Object = MibScalar
tsLogAccessesSkipped = _TsLogAccessesSkipped_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1, 4),
    _TsLogAccessesSkipped_Type()
)
tsLogAccessesSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLogAccessesSkipped.setStatus("current")
_TsLogErrorsLogged_Type = Counter32
_TsLogErrorsLogged_Object = MibScalar
tsLogErrorsLogged = _TsLogErrorsLogged_Object(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 7, 1, 5),
    _TsLogErrorsLogged_Type()
)
tsLogErrorsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLogErrorsLogged.setStatus("current")
_TsNetworkSubsystem_ObjectIdentity = ObjectIdentity
tsNetworkSubsystem = _TsNetworkSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tsNetworkSubsystem.setStatus("current")
_TsNetworkStats_ObjectIdentity = ObjectIdentity
tsNetworkStats = _TsNetworkStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tsNetworkStats.setStatus("current")
_TsNetworkClusterStats_ObjectIdentity = ObjectIdentity
tsNetworkClusterStats = _TsNetworkClusterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    tsNetworkClusterStats.setStatus("current")
_TsIOSubsystem_ObjectIdentity = ObjectIdentity
tsIOSubsystem = _TsIOSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    tsIOSubsystem.setStatus("current")
_TsOSSubsystem_ObjectIdentity = ObjectIdentity
tsOSSubsystem = _TsOSSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tsOSSubsystem.setStatus("current")
_InktomiTSEvents_ObjectIdentity = ObjectIdentity
inktomiTSEvents = _InktomiTSEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3)
)
_InktomiTSLogEvents_ObjectIdentity = ObjectIdentity
inktomiTSLogEvents = _InktomiTSLogEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    inktomiTSLogEvents.setStatus("current")
_InktomiTSCacheEvents_ObjectIdentity = ObjectIdentity
inktomiTSCacheEvents = _InktomiTSCacheEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    inktomiTSCacheEvents.setStatus("current")
_InktomiTSProtocolEvents_ObjectIdentity = ObjectIdentity
inktomiTSProtocolEvents = _InktomiTSProtocolEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    inktomiTSProtocolEvents.setStatus("current")
_InktomiTSGeneralEvents_ObjectIdentity = ObjectIdentity
inktomiTSGeneralEvents = _InktomiTSGeneralEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    inktomiTSGeneralEvents.setStatus("current")
_InktomiTSClusterEvents_ObjectIdentity = ObjectIdentity
inktomiTSClusterEvents = _InktomiTSClusterEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    inktomiTSClusterEvents.setStatus("current")
_InktomiExpr_ObjectIdentity = ObjectIdentity
inktomiExpr = _InktomiExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1967, 6)
)

# Managed Objects groups


# Notification objects

loggingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 1, 0, 1)
)
if mibBuilder.loadTexts:
    loggingError.setStatus(
        "current"
    )

loggingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 1, 0, 2)
)
if mibBuilder.loadTexts:
    loggingWarning.setStatus(
        "current"
    )

logSpaceCrisis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 1, 0, 3)
)
if mibBuilder.loadTexts:
    logSpaceCrisis.setStatus(
        "current"
    )

cacheError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    cacheError.setStatus(
        "current"
    )

cacheWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 2, 0, 2)
)
if mibBuilder.loadTexts:
    cacheWarning.setStatus(
        "current"
    )

nntpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 3, 0, 1)
)
if mibBuilder.loadTexts:
    nntpError.setStatus(
        "current"
    )

configurationUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 1)
)
if mibBuilder.loadTexts:
    configurationUpdateFailed.setStatus(
        "current"
    )

managerUIInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 2)
)
if mibBuilder.loadTexts:
    managerUIInitFailed.setStatus(
        "current"
    )

invalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 3)
)
if mibBuilder.loadTexts:
    invalidConfig.setStatus(
        "current"
    )

processBorn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 4)
)
if mibBuilder.loadTexts:
    processBorn.setStatus(
        "current"
    )

systemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 5)
)
if mibBuilder.loadTexts:
    systemError.setStatus(
        "current"
    )

testAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 4, 0, 6)
)
if mibBuilder.loadTexts:
    testAlarm.setStatus(
        "current"
    )

peerDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 5, 0, 1)
)
if mibBuilder.loadTexts:
    peerDied.setStatus(
        "current"
    )

peerBorn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 5, 0, 2)
)
if mibBuilder.loadTexts:
    peerBorn.setStatus(
        "current"
    )

pingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1967, 3, 1, 3, 5, 0, 3)
)
if mibBuilder.loadTexts:
    pingFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INKTOMI-TS-MIB",
    **{"vendorInktomi": vendorInktomi,
       "inktomiReg": inktomiReg,
       "inktomiModules": inktomiModules,
       "inktomiGlobalRegModule": inktomiGlobalRegModule,
       "inktomiTrafficServerMibModule": inktomiTrafficServerMibModule,
       "inktomiGeneric": inktomiGeneric,
       "inktomiProducts": inktomiProducts,
       "inktomiTSMIBs": inktomiTSMIBs,
       "inktomiTSConformance": inktomiTSConformance,
       "inktomiTSObjs": inktomiTSObjs,
       "tSProtocols": tSProtocols,
       "tsProtocolSummary": tsProtocolSummary,
       "tsClientThroughputOutKBit": tsClientThroughputOutKBit,
       "tsDocumentHitRate": tsDocumentHitRate,
       "tsBandwidthSavingsRatio": tsBandwidthSavingsRatio,
       "tsServerConnections": tsServerConnections,
       "tsClientConnections": tsClientConnections,
       "tsProtocolClusterSummary": tsProtocolClusterSummary,
       "tsClusterClientThroughputOutKBit": tsClusterClientThroughputOutKBit,
       "tsClusterDocumentHitRate": tsClusterDocumentHitRate,
       "tsClusterBandwidthSavingsRatio": tsClusterBandwidthSavingsRatio,
       "tsClusterServerConnections": tsClusterServerConnections,
       "tsClusterClientConnections": tsClusterClientConnections,
       "tsProtocolHTTP": tsProtocolHTTP,
       "tsHttpStats": tsHttpStats,
       "httpXacts": httpXacts,
       "httpThroughput": httpThroughput,
       "httpCurrentlyOpenUA": httpCurrentlyOpenUA,
       "httpHitRatio": httpHitRatio,
       "httpBandwidthSavingsRatio": httpBandwidthSavingsRatio,
       "httpCurrentlyOpenOrigin": httpCurrentlyOpenOrigin,
       "httpUserAgentDocumentBytes": httpUserAgentDocumentBytes,
       "httpUserAgentHeaderBytes": httpUserAgentHeaderBytes,
       "httpUserAgentConnections": httpUserAgentConnections,
       "httpUserAgentTransactionsInProgress": httpUserAgentTransactionsInProgress,
       "httpOriginServerTotalTransactions": httpOriginServerTotalTransactions,
       "httpOriginServerTransactionsInProgress": httpOriginServerTransactionsInProgress,
       "httpOriginServerDocumentBytes": httpOriginServerDocumentBytes,
       "httpOriginServerHeaderBytes": httpOriginServerHeaderBytes,
       "httpOriginServerConnections": httpOriginServerConnections,
       "httpOriginServerResponseBytes": httpOriginServerResponseBytes,
       "httpUserAgentResponseBytes": httpUserAgentResponseBytes,
       "httpUserAgentTransactions": httpUserAgentTransactions,
       "httpTransactionErrorsPossbileAbortsMsec": httpTransactionErrorsPossbileAbortsMsec,
       "httpTransactionMissChangedMsec": httpTransactionMissChangedMsec,
       "httpTransactionHitRevalidatedMsec": httpTransactionHitRevalidatedMsec,
       "httpTransactionErrorsOtherMsec": httpTransactionErrorsOtherMsec,
       "httpTransactionErrorsAbortsMsec": httpTransactionErrorsAbortsMsec,
       "httpTransactionErrorsEarlyHangupsMsec": httpTransactionErrorsEarlyHangupsMsec,
       "httpTransactionErrorsEmptyHangupsMsec": httpTransactionErrorsEmptyHangupsMsec,
       "httpTransactionOtherUnclassifiedMsec": httpTransactionOtherUnclassifiedMsec,
       "httpTransactionErrorsPreAcceptHangupsMsec": httpTransactionErrorsPreAcceptHangupsMsec,
       "httpTransactionMissClientNoCacheMsec": httpTransactionMissClientNoCacheMsec,
       "httpTransactionMissNotCachableMsec": httpTransactionMissNotCachableMsec,
       "httpTransactionHitFreshMsec": httpTransactionHitFreshMsec,
       "httpTransactionErrorsConnectFailedMsec": httpTransactionErrorsConnectFailedMsec,
       "httpTransactionMissColdMsec": httpTransactionMissColdMsec,
       "httpTransactionErrorsPossibleAbortsPct": httpTransactionErrorsPossibleAbortsPct,
       "httpTransactionErrorsPreAcceptHangupsPct": httpTransactionErrorsPreAcceptHangupsPct,
       "httpTransactionMissChangedPct": httpTransactionMissChangedPct,
       "httpTransactionErrorsOtherPct": httpTransactionErrorsOtherPct,
       "httpTransactionHitFreshPct": httpTransactionHitFreshPct,
       "httpTransactionErrorsConnectFailedPct": httpTransactionErrorsConnectFailedPct,
       "httpTransactionErrorsEarlyHangupsPct": httpTransactionErrorsEarlyHangupsPct,
       "httpTransactionErrorsEmptyHangupsPct": httpTransactionErrorsEmptyHangupsPct,
       "httpTransactionMissColdPct": httpTransactionMissColdPct,
       "httpTransactionOtherUnclassifiedPct": httpTransactionOtherUnclassifiedPct,
       "httpTransactionHitRevalidatedPct": httpTransactionHitRevalidatedPct,
       "httpTransactionMissClientNoCachePct": httpTransactionMissClientNoCachePct,
       "httpTransactionMissNotCachablePct": httpTransactionMissNotCachablePct,
       "httpTransactionErrorsAbortsPct": httpTransactionErrorsAbortsPct,
       "httpCurrentlyParentProxy": httpCurrentlyParentProxy,
       "tsHttpClusterStats": tsHttpClusterStats,
       "clusterHttpHitRatio": clusterHttpHitRatio,
       "clusterBandwidthSavingsRatio": clusterBandwidthSavingsRatio,
       "clusterHttpCurrentlyOpenUA": clusterHttpCurrentlyOpenUA,
       "clusterHttpCurrentlyOpenOrigin": clusterHttpCurrentlyOpenOrigin,
       "clusterHttpThroughput": clusterHttpThroughput,
       "clusterHttpXacts": clusterHttpXacts,
       "clusterHttpUserAgentResponseBytes": clusterHttpUserAgentResponseBytes,
       "clusterHttpOriginServerResponseBytes": clusterHttpOriginServerResponseBytes,
       "clusterHttpOriginServerTransactions": clusterHttpOriginServerTransactions,
       "clusterHttpUserAgentTransactions": clusterHttpUserAgentTransactions,
       "clusterHttpCurrentlyParentProxy": clusterHttpCurrentlyParentProxy,
       "tsProtocolFTP": tsProtocolFTP,
       "tsFTPStats": tsFTPStats,
       "ftpCurrentlyOpenConnections": ftpCurrentlyOpenConnections,
       "ftpSuccessfulPASV": ftpSuccessfulPASV,
       "ftpUnsuccessfulPASV": ftpUnsuccessfulPASV,
       "ftpSuccessfulPORT": ftpSuccessfulPORT,
       "ftpUnsuccessfulPORT": ftpUnsuccessfulPORT,
       "ftpClientOpenConnections": ftpClientOpenConnections,
       "ftpClientBytesRead": ftpClientBytesRead,
       "ftpClientBytesWritten": ftpClientBytesWritten,
       "ftpServerOpenConnections": ftpServerOpenConnections,
       "ftpServerBytesRead": ftpServerBytesRead,
       "ftpServerBytesWritten": ftpServerBytesWritten,
       "ftpFileHits": ftpFileHits,
       "ftpFileMisses": ftpFileMisses,
       "ftpCwdHits": ftpCwdHits,
       "ftpCwdMisses": ftpCwdMisses,
       "ftpDirectoryHits": ftpDirectoryHits,
       "ftpDirectoryMisses": ftpDirectoryMisses,
       "tsFTPClusterStats": tsFTPClusterStats,
       "tsProtocolSOCKS": tsProtocolSOCKS,
       "tsSOCKSStats": tsSOCKSStats,
       "socksUnsuccessfulConnections": socksUnsuccessfulConnections,
       "socksSuccessfulConnections": socksSuccessfulConnections,
       "socksOpenConnections": socksOpenConnections,
       "tsSOCKSClusterStats": tsSOCKSClusterStats,
       "tsProtocolNNTP": tsProtocolNNTP,
       "tsNNTPStats": tsNNTPStats,
       "nntpClientOpenConnections": nntpClientOpenConnections,
       "nntpServerOpenConnections": nntpServerOpenConnections,
       "nntpArticleHits": nntpArticleHits,
       "nntpArticleMisses": nntpArticleMisses,
       "nntpClientBytesWritten": nntpClientBytesWritten,
       "nntpClientBytesRead": nntpClientBytesRead,
       "nntpFeedBytes": nntpFeedBytes,
       "nntpPullBytes": nntpPullBytes,
       "nntpGroupHits": nntpGroupHits,
       "nntpGroupRefreshes": nntpGroupRefreshes,
       "nntpOverviewHits": nntpOverviewHits,
       "nntpOverviewRefreshes": nntpOverviewRefreshes,
       "nntpPostBytes": nntpPostBytes,
       "nntpPosts": nntpPosts,
       "nntpServerBytesRead": nntpServerBytesRead,
       "nntpServerBytesWritten": nntpServerBytesWritten,
       "nntpUpstreamTotalBytes": nntpUpstreamTotalBytes,
       "nntpDownstreamTotalBytes": nntpDownstreamTotalBytes,
       "tsNNTPClusterStats": tsNNTPClusterStats,
       "nntpClusterUpstreamTotalBytes": nntpClusterUpstreamTotalBytes,
       "nntpClusterDownstreamTotalBytes": nntpClusterDownstreamTotalBytes,
       "nntpClusterClientOpenConnections": nntpClusterClientOpenConnections,
       "nntpClusterServerOpenConnections": nntpClusterServerOpenConnections,
       "tsProtocolRNI": tsProtocolRNI,
       "tsRNIStats": tsRNIStats,
       "rniObjectCount": rniObjectCount,
       "rniBlockHitCount": rniBlockHitCount,
       "rniBlockMissCount": rniBlockMissCount,
       "rniByteHitSum": rniByteHitSum,
       "rniByteMissSum": rniByteMissSum,
       "rniCurrentClientConnections": rniCurrentClientConnections,
       "rniDownstreamRequests": rniDownstreamRequests,
       "rniDownstreamRequestBytes": rniDownstreamRequestBytes,
       "rniDownstreamResponseBytes": rniDownstreamResponseBytes,
       "rniCurrentServerConnections": rniCurrentServerConnections,
       "rniUpstreamRequests": rniUpstreamRequests,
       "rniUpstreamRequestBytes": rniUpstreamRequestBytes,
       "rniUpstreamResponseBytes": rniUpstreamResponseBytes,
       "tsRNIClusterStats": tsRNIClusterStats,
       "rniClusterUpstreamTotalBytes": rniClusterUpstreamTotalBytes,
       "rniClusterDownstreamTotalBytes": rniClusterDownstreamTotalBytes,
       "rniClusterCurrentServerConnections": rniClusterCurrentServerConnections,
       "rniClusterCurrentClientConnections": rniClusterCurrentClientConnections,
       "rniClusterUserAgentXactsPerSecond": rniClusterUserAgentXactsPerSecond,
       "rniClusterUserAgentsTotalDocumentsServed": rniClusterUserAgentsTotalDocumentsServed,
       "tsProtocolQT": tsProtocolQT,
       "tsQTStats": tsQTStats,
       "qtClientRequestBytes": qtClientRequestBytes,
       "qtClientResponseBytes": qtClientResponseBytes,
       "qtServerRequestBytes": qtServerRequestBytes,
       "qtServerResponseBytes": qtServerResponseBytes,
       "qtCurrentClientConnections": qtCurrentClientConnections,
       "qtCurrentServerConnections": qtCurrentServerConnections,
       "qtCurrentLiveStreams": qtCurrentLiveStreams,
       "qtClientServerBytesRead": qtClientServerBytesRead,
       "qtClientCacheBytesRead": qtClientCacheBytesRead,
       "tsQTClusterStats": tsQTClusterStats,
       "qtClusterServerTotalBytes": qtClusterServerTotalBytes,
       "qtClusterClientTotalBytes": qtClusterClientTotalBytes,
       "qtClusterCurrentServerConnections": qtClusterCurrentServerConnections,
       "qtClusterCurrentClientConnections": qtClusterCurrentClientConnections,
       "qtClusterUserAgentXactsPerSecond": qtClusterUserAgentXactsPerSecond,
       "qtClusterUserAgentsTotalDocumentsServed": qtClusterUserAgentsTotalDocumentsServed,
       "tsProtocolWMT": tsProtocolWMT,
       "tsWMTStats": tsWMTStats,
       "wmtClientRequestBytes": wmtClientRequestBytes,
       "wmtClientResponseBytes": wmtClientResponseBytes,
       "wmtServerRequestBytes": wmtServerRequestBytes,
       "wmtServerResponseBytes": wmtServerResponseBytes,
       "wmtCurrentClientConnections": wmtCurrentClientConnections,
       "wmtCurrentServerConnections": wmtCurrentServerConnections,
       "tsWMTClusterStats": tsWMTClusterStats,
       "wmtClusterServerTotalBytes": wmtClusterServerTotalBytes,
       "wmtClusterClientTotalBytes": wmtClusterClientTotalBytes,
       "wmtClusterCurrentServerConnections": wmtClusterCurrentServerConnections,
       "wmtClusterCurrentClientConnections": wmtClusterCurrentClientConnections,
       "wmtClusterUserAgentXactsPerSecond": wmtClusterUserAgentXactsPerSecond,
       "wmtClusterUserAgentsTotalDocumentsServed": wmtClusterUserAgentsTotalDocumentsServed,
       "tSEventSubsystem": tSEventSubsystem,
       "tSCacheSubsystem": tSCacheSubsystem,
       "tSICPStats": tSICPStats,
       "tsICPRemoteQuery": tsICPRemoteQuery,
       "tsICPRemoteResponses": tsICPRemoteResponses,
       "tsICPCacheLookupSuccess": tsICPCacheLookupSuccess,
       "tsICPCacheLookupFail": tsICPCacheLookupFail,
       "tsICPQueryResponseWrite": tsICPQueryResponseWrite,
       "tsICPQueryHits": tsICPQueryHits,
       "tsICPQueryMisses": tsICPQueryMisses,
       "tsICPQueryRequests": tsICPQueryRequests,
       "tsICPResponseTime": tsICPResponseTime,
       "tsICPUDPSendQueries": tsICPUDPSendQueries,
       "tsICPRequestTime": tsICPRequestTime,
       "tSCacheStats": tSCacheStats,
       "tSCachePercentFree": tSCachePercentFree,
       "tSCacheHTTPHits": tSCacheHTTPHits,
       "tSCacheHits": tSCacheHits,
       "tSCacheMisses": tSCacheMisses,
       "tSCacheCurrentXfers": tSCacheCurrentXfers,
       "tSCacheBytesTotalMB": tSCacheBytesTotalMB,
       "tSCacheLinkActive": tSCacheLinkActive,
       "tSCacheLinkFailures": tSCacheLinkFailures,
       "tSCacheLinkSuccesses": tSCacheLinkSuccesses,
       "tSCacheLookupActive": tSCacheLookupActive,
       "tSCacheLookupFailures": tSCacheLookupFailures,
       "tSCacheLookupSuccesses": tSCacheLookupSuccesses,
       "tSCacheReadActive": tSCacheReadActive,
       "tSCacheReadFailures": tSCacheReadFailures,
       "tSCacheReadSuccesses": tSCacheReadSuccesses,
       "tSCacheRemoveActive": tSCacheRemoveActive,
       "tSCacheRemoveFailures": tSCacheRemoveFailures,
       "tSCacheRemoveSuccesses": tSCacheRemoveSuccesses,
       "tSCacheUpdateActive": tSCacheUpdateActive,
       "tSCacheUpdateFailures": tSCacheUpdateFailures,
       "tSCacheUpdateSuccesses": tSCacheUpdateSuccesses,
       "tSCacheWriteActive": tSCacheWriteActive,
       "tSCacheWriteFailures": tSCacheWriteFailures,
       "tSCacheWriteSuccesses": tSCacheWriteSuccesses,
       "tSCacheConnections": tSCacheConnections,
       "tSCacheClusterStats": tSCacheClusterStats,
       "tSClusterCacheFreeMB": tSClusterCacheFreeMB,
       "tSClusterCachePercentFree": tSClusterCachePercentFree,
       "tSClusterCacheHTTPHits": tSClusterCacheHTTPHits,
       "tSClusterCacheHits": tSClusterCacheHits,
       "tSClusterCacheMisses": tSClusterCacheMisses,
       "tSClusterCacheCurrentXfers": tSClusterCacheCurrentXfers,
       "tSClusterCacheConnections": tSClusterCacheConnections,
       "tSCacheGCSubsystem": tSCacheGCSubsystem,
       "tSCacheEngineSubsystem": tSCacheEngineSubsystem,
       "tSDiskSubsystem": tSDiskSubsystem,
       "tSHostDBSubsystem": tSHostDBSubsystem,
       "tsDNSStats": tsDNSStats,
       "dnsTotalLookups": dnsTotalLookups,
       "dnsLookupRate": dnsLookupRate,
       "dnsTotalLookupSuccesses": dnsTotalLookupSuccesses,
       "dnsLookupTimeMs": dnsLookupTimeMs,
       "tsClusterDNSStats": tsClusterDNSStats,
       "tsClusterDNSTotalLookups": tsClusterDNSTotalLookups,
       "tsClusterDNSLookupRate": tsClusterDNSLookupRate,
       "tsHostDBStats": tsHostDBStats,
       "hostDBTotalLookups": hostDBTotalLookups,
       "hostDBTotalHits": hostDBTotalHits,
       "hostDBAverageTTL": hostDBAverageTTL,
       "tSClusterHostDBStats": tSClusterHostDBStats,
       "clusterHostdbHitRatio": clusterHostdbHitRatio,
       "tSClusterSubsystem": tSClusterSubsystem,
       "tsClusterNodeStats": tsClusterNodeStats,
       "clusterBytesRead": clusterBytesRead,
       "clusterBytesWritten": clusterBytesWritten,
       "clusterConnectionsOpen": clusterConnectionsOpen,
       "clusterConnectionsOpened": clusterConnectionsOpened,
       "clusterNetBackups": clusterNetBackups,
       "clusterNodeCount": clusterNodeCount,
       "tsClusterClusterStats": tsClusterClusterStats,
       "tsLoggingSubsystem": tsLoggingSubsystem,
       "tsLogStats": tsLogStats,
       "tsLogOpenFiles": tsLogOpenFiles,
       "tsLogSpaceUsed": tsLogSpaceUsed,
       "tsLogAccessesLogged": tsLogAccessesLogged,
       "tsLogAccessesSkipped": tsLogAccessesSkipped,
       "tsLogErrorsLogged": tsLogErrorsLogged,
       "tsNetworkSubsystem": tsNetworkSubsystem,
       "tsNetworkStats": tsNetworkStats,
       "tsNetworkClusterStats": tsNetworkClusterStats,
       "tsIOSubsystem": tsIOSubsystem,
       "tsOSSubsystem": tsOSSubsystem,
       "inktomiTSEvents": inktomiTSEvents,
       "inktomiTSLogEvents": inktomiTSLogEvents,
       "loggingError": loggingError,
       "loggingWarning": loggingWarning,
       "logSpaceCrisis": logSpaceCrisis,
       "inktomiTSCacheEvents": inktomiTSCacheEvents,
       "cacheError": cacheError,
       "cacheWarning": cacheWarning,
       "inktomiTSProtocolEvents": inktomiTSProtocolEvents,
       "nntpError": nntpError,
       "inktomiTSGeneralEvents": inktomiTSGeneralEvents,
       "configurationUpdateFailed": configurationUpdateFailed,
       "managerUIInitFailed": managerUIInitFailed,
       "invalidConfig": invalidConfig,
       "processBorn": processBorn,
       "systemError": systemError,
       "testAlarm": testAlarm,
       "inktomiTSClusterEvents": inktomiTSClusterEvents,
       "peerDied": peerDied,
       "peerBorn": peerBorn,
       "pingFailure": pingFailure,
       "inktomiExpr": inktomiExpr}
)
