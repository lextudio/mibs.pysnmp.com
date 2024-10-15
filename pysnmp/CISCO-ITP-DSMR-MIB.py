# SNMP MIB module (CISCO-ITP-DSMR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-DSMR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:15 2024
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

(CgsccpGttGlobalTitleInd,
 CgsccpGttTransType) = mibBuilder.importSymbols(
    "CISCO-ITP-GSCCP-MIB",
    "CgsccpGttGlobalTitleInd",
    "CgsccpGttTransType")

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstNetwork")

(CmlrAddressDigits,
 CmlrAddressType,
 CmlrId,
 CmlrName,
 CmlrRuleProtocol,
 CmlrRuleSetName) = mibBuilder.importSymbols(
    "CISCO-ITP-MLR-MIB",
    "CmlrAddressDigits",
    "CmlrAddressType",
    "CmlrId",
    "CmlrName",
    "CmlrRuleProtocol",
    "CmlrRuleSetName")

(CItpTcGtaLongDisplay,
 CItpTcNAI,
 CItpTcNetworkName,
 CItpTcNumberingPlan,
 CItpTcPointCode,
 CItpTcSubSystemNumber,
 CItpTcTableLoadStatus,
 CItpTcURL) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcGtaLongDisplay",
    "CItpTcNAI",
    "CItpTcNetworkName",
    "CItpTcNumberingPlan",
    "CItpTcPointCode",
    "CItpTcSubSystemNumber",
    "CItpTcTableLoadStatus",
    "CItpTcURL")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpDsmrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300)
)
ciscoItpDsmrMIB.setRevisions(
        ("2005-05-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdsmrMaximumDigits(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )



class CdsmrMinimumDigits(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )



class CdsmrResultDestinationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gt", 2),
          ("none", 1),
          ("pc", 5),
          ("pcSsn", 6),
          ("smpp", 3),
          ("ucp", 4))
    )



class CdsmrResultOctet(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CdsmrResultParameters(Bits, TextualConvention):
    status = "current"


class CdsmrResultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("block", 7),
          ("deliverMt", 10),
          ("group", 4),
          ("gt", 3),
          ("none", 0),
          ("origImsi", 11),
          ("origImsiNext", 12),
          ("pc", 1),
          ("pcSsn", 2),
          ("ruleNext", 8),
          ("ruleNumber", 9),
          ("smpp", 5),
          ("ucp", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoItpDsmrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpDsmrMIBNotifs = _CiscoItpDsmrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 0)
)
_CiscoItpDsmrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpDsmrMIBObjects = _CiscoItpDsmrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1)
)
_CdsmrScalars_ObjectIdentity = ObjectIdentity
cdsmrScalars = _CdsmrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 1)
)


class _CdsmrTableLoadNotifEnabled_Type(TruthValue):
    """Custom type cdsmrTableLoadNotifEnabled based on TruthValue"""


_CdsmrTableLoadNotifEnabled_Object = MibScalar
cdsmrTableLoadNotifEnabled = _CdsmrTableLoadNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 1, 1),
    _CdsmrTableLoadNotifEnabled_Type()
)
cdsmrTableLoadNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsmrTableLoadNotifEnabled.setStatus("current")
_CdsmrInstTable_Object = MibTable
cdsmrInstTable = _CdsmrInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2)
)
if mibBuilder.loadTexts:
    cdsmrInstTable.setStatus("current")
_CdsmrInstTableEntry_Object = MibTableRow
cdsmrInstTableEntry = _CdsmrInstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1)
)
cdsmrInstTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cdsmrInstTableEntry.setStatus("current")
_CdsmrInstLastChanged_Type = TimeStamp
_CdsmrInstLastChanged_Object = MibTableColumn
cdsmrInstLastChanged = _CdsmrInstLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 1),
    _CdsmrInstLastChanged_Type()
)
cdsmrInstLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstLastChanged.setStatus("current")
_CdsmrInstLastLoadTime_Type = TimeStamp
_CdsmrInstLastLoadTime_Object = MibTableColumn
cdsmrInstLastLoadTime = _CdsmrInstLastLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 2),
    _CdsmrInstLastLoadTime_Type()
)
cdsmrInstLastLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstLastLoadTime.setStatus("current")
_CdsmrInstLoadStatus_Type = CItpTcTableLoadStatus
_CdsmrInstLoadStatus_Object = MibTableColumn
cdsmrInstLoadStatus = _CdsmrInstLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 3),
    _CdsmrInstLoadStatus_Type()
)
cdsmrInstLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstLoadStatus.setStatus("current")
_CdsmrInstLastURL_Type = CItpTcURL
_CdsmrInstLastURL_Object = MibTableColumn
cdsmrInstLastURL = _CdsmrInstLastURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 4),
    _CdsmrInstLastURL_Type()
)
cdsmrInstLastURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstLastURL.setStatus("current")
_CdsmrInstDeliveredSmppCounts_Type = Counter32
_CdsmrInstDeliveredSmppCounts_Object = MibTableColumn
cdsmrInstDeliveredSmppCounts = _CdsmrInstDeliveredSmppCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 5),
    _CdsmrInstDeliveredSmppCounts_Type()
)
cdsmrInstDeliveredSmppCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredSmppCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredSmppCounts.setUnits("packets")
_CdsmrInstDeliveredUcpCounts_Type = Counter32
_CdsmrInstDeliveredUcpCounts_Object = MibTableColumn
cdsmrInstDeliveredUcpCounts = _CdsmrInstDeliveredUcpCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 6),
    _CdsmrInstDeliveredUcpCounts_Type()
)
cdsmrInstDeliveredUcpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredUcpCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredUcpCounts.setUnits("packets")
_CdsmrInstDeliveredGsmCounts_Type = Counter32
_CdsmrInstDeliveredGsmCounts_Object = MibTableColumn
cdsmrInstDeliveredGsmCounts = _CdsmrInstDeliveredGsmCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 7),
    _CdsmrInstDeliveredGsmCounts_Type()
)
cdsmrInstDeliveredGsmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredGsmCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDeliveredGsmCounts.setUnits("packets")
_CdsmrInstDeferredGsmCounts_Type = Counter32
_CdsmrInstDeferredGsmCounts_Object = MibTableColumn
cdsmrInstDeferredGsmCounts = _CdsmrInstDeferredGsmCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 8),
    _CdsmrInstDeferredGsmCounts_Type()
)
cdsmrInstDeferredGsmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDeferredGsmCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDeferredGsmCounts.setUnits("packets")
_CdsmrInstGsmStatusReports_Type = Counter32
_CdsmrInstGsmStatusReports_Object = MibTableColumn
cdsmrInstGsmStatusReports = _CdsmrInstGsmStatusReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 9),
    _CdsmrInstGsmStatusReports_Type()
)
cdsmrInstGsmStatusReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstGsmStatusReports.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstGsmStatusReports.setUnits("packets")
_CdsmrInstUcpNotifications_Type = Counter32
_CdsmrInstUcpNotifications_Object = MibTableColumn
cdsmrInstUcpNotifications = _CdsmrInstUcpNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 10),
    _CdsmrInstUcpNotifications_Type()
)
cdsmrInstUcpNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstUcpNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstUcpNotifications.setUnits("packets")
_CdsmrInstSmppDeliveryReceipts_Type = Counter32
_CdsmrInstSmppDeliveryReceipts_Object = MibTableColumn
cdsmrInstSmppDeliveryReceipts = _CdsmrInstSmppDeliveryReceipts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 11),
    _CdsmrInstSmppDeliveryReceipts_Type()
)
cdsmrInstSmppDeliveryReceipts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstSmppDeliveryReceipts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstSmppDeliveryReceipts.setUnits("packets")
_CdsmrInstRoutingFailures_Type = Counter32
_CdsmrInstRoutingFailures_Object = MibTableColumn
cdsmrInstRoutingFailures = _CdsmrInstRoutingFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 12),
    _CdsmrInstRoutingFailures_Type()
)
cdsmrInstRoutingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstRoutingFailures.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstRoutingFailures.setUnits("packets")
_CdsmrInstResultFailures_Type = Counter32
_CdsmrInstResultFailures_Object = MibTableColumn
cdsmrInstResultFailures = _CdsmrInstResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 13),
    _CdsmrInstResultFailures_Type()
)
cdsmrInstResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstResultFailures.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstResultFailures.setUnits("packets")
_CdsmrInstInternalErrors_Type = Counter32
_CdsmrInstInternalErrors_Object = MibTableColumn
cdsmrInstInternalErrors = _CdsmrInstInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 14),
    _CdsmrInstInternalErrors_Type()
)
cdsmrInstInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstInternalErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstInternalErrors.setUnits("packets")
_CdsmrInstParseErrors_Type = Counter32
_CdsmrInstParseErrors_Object = MibTableColumn
cdsmrInstParseErrors = _CdsmrInstParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 15),
    _CdsmrInstParseErrors_Type()
)
cdsmrInstParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstParseErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstParseErrors.setUnits("packets")
_CdsmrInstResourceErrors_Type = Counter32
_CdsmrInstResourceErrors_Object = MibTableColumn
cdsmrInstResourceErrors = _CdsmrInstResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 16),
    _CdsmrInstResourceErrors_Type()
)
cdsmrInstResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstResourceErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstResourceErrors.setUnits("packets")
_CdsmrInstProvisioningErrors_Type = Counter32
_CdsmrInstProvisioningErrors_Object = MibTableColumn
cdsmrInstProvisioningErrors = _CdsmrInstProvisioningErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 17),
    _CdsmrInstProvisioningErrors_Type()
)
cdsmrInstProvisioningErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstProvisioningErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstProvisioningErrors.setUnits("packets")
_CdsmrInstDestUnreachableErrors_Type = Counter32
_CdsmrInstDestUnreachableErrors_Object = MibTableColumn
cdsmrInstDestUnreachableErrors = _CdsmrInstDestUnreachableErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 18),
    _CdsmrInstDestUnreachableErrors_Type()
)
cdsmrInstDestUnreachableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDestUnreachableErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDestUnreachableErrors.setUnits("packets")
_CdsmrInstDestSignalErrors_Type = Counter32
_CdsmrInstDestSignalErrors_Object = MibTableColumn
cdsmrInstDestSignalErrors = _CdsmrInstDestSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 19),
    _CdsmrInstDestSignalErrors_Type()
)
cdsmrInstDestSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstDestSignalErrors.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstDestSignalErrors.setUnits("packets")
_CdsmrInstTimeOuts_Type = Counter32
_CdsmrInstTimeOuts_Object = MibTableColumn
cdsmrInstTimeOuts = _CdsmrInstTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 20),
    _CdsmrInstTimeOuts_Type()
)
cdsmrInstTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstTimeOuts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstTimeOuts.setUnits("packets")
_CdsmrInstBlockedPackets_Type = Counter32
_CdsmrInstBlockedPackets_Object = MibTableColumn
cdsmrInstBlockedPackets = _CdsmrInstBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 21),
    _CdsmrInstBlockedPackets_Type()
)
cdsmrInstBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstBlockedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstBlockedPackets.setUnits("packets")
_CdsmrInstRoutingRequestsRcvdGsm_Type = Counter32
_CdsmrInstRoutingRequestsRcvdGsm_Object = MibTableColumn
cdsmrInstRoutingRequestsRcvdGsm = _CdsmrInstRoutingRequestsRcvdGsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 22),
    _CdsmrInstRoutingRequestsRcvdGsm_Type()
)
cdsmrInstRoutingRequestsRcvdGsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdGsm.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdGsm.setUnits("packets")
_CdsmrInstRoutingRequestsRcvdIs41_Type = Counter32
_CdsmrInstRoutingRequestsRcvdIs41_Object = MibTableColumn
cdsmrInstRoutingRequestsRcvdIs41 = _CdsmrInstRoutingRequestsRcvdIs41_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 23),
    _CdsmrInstRoutingRequestsRcvdIs41_Type()
)
cdsmrInstRoutingRequestsRcvdIs41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdIs41.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdIs41.setUnits("packets")
_CdsmrInstRoutingRequestsRcvdUcp_Type = Counter32
_CdsmrInstRoutingRequestsRcvdUcp_Object = MibTableColumn
cdsmrInstRoutingRequestsRcvdUcp = _CdsmrInstRoutingRequestsRcvdUcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 24),
    _CdsmrInstRoutingRequestsRcvdUcp_Type()
)
cdsmrInstRoutingRequestsRcvdUcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdUcp.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdUcp.setUnits("packets")
_CdsmrInstRoutingRequestsRcvdSmpp_Type = Counter32
_CdsmrInstRoutingRequestsRcvdSmpp_Object = MibTableColumn
cdsmrInstRoutingRequestsRcvdSmpp = _CdsmrInstRoutingRequestsRcvdSmpp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 25),
    _CdsmrInstRoutingRequestsRcvdSmpp_Type()
)
cdsmrInstRoutingRequestsRcvdSmpp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdSmpp.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrInstRoutingRequestsRcvdSmpp.setUnits("packets")
_CdsmrInstRowStatus_Type = RowStatus
_CdsmrInstRowStatus_Object = MibTableColumn
cdsmrInstRowStatus = _CdsmrInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 2, 1, 26),
    _CdsmrInstRowStatus_Type()
)
cdsmrInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrInstRowStatus.setStatus("current")
_CdsmrResultGroupTable_Object = MibTable
cdsmrResultGroupTable = _CdsmrResultGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3)
)
if mibBuilder.loadTexts:
    cdsmrResultGroupTable.setStatus("current")
_CdsmrResultGroupTableEntry_Object = MibTableRow
cdsmrResultGroupTableEntry = _CdsmrResultGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1)
)
cdsmrResultGroupTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrResultGroupName"),
)
if mibBuilder.loadTexts:
    cdsmrResultGroupTableEntry.setStatus("current")
_CdsmrResultGroupName_Type = CmlrName
_CdsmrResultGroupName_Object = MibTableColumn
cdsmrResultGroupName = _CdsmrResultGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 1),
    _CdsmrResultGroupName_Type()
)
cdsmrResultGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrResultGroupName.setStatus("current")


class _CdsmrResultGroupServerType_Type(Integer32):
    """Custom type cdsmrResultGroupServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esme", 1),
          ("smsc", 2))
    )


_CdsmrResultGroupServerType_Type.__name__ = "Integer32"
_CdsmrResultGroupServerType_Object = MibTableColumn
cdsmrResultGroupServerType = _CdsmrResultGroupServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 2),
    _CdsmrResultGroupServerType_Type()
)
cdsmrResultGroupServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupServerType.setStatus("current")


class _CdsmrResultGroupCdrConsolidation_Type(OctetString):
    """Custom type cdsmrResultGroupCdrConsolidation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdsmrResultGroupCdrConsolidation_Type.__name__ = "OctetString"
_CdsmrResultGroupCdrConsolidation_Object = MibTableColumn
cdsmrResultGroupCdrConsolidation = _CdsmrResultGroupCdrConsolidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 3),
    _CdsmrResultGroupCdrConsolidation_Type()
)
cdsmrResultGroupCdrConsolidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupCdrConsolidation.setStatus("current")


class _CdsmrResultGroupIdentifier_Type(Unsigned32):
    """Custom type cdsmrResultGroupIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 9999),
    )


_CdsmrResultGroupIdentifier_Type.__name__ = "Unsigned32"
_CdsmrResultGroupIdentifier_Object = MibTableColumn
cdsmrResultGroupIdentifier = _CdsmrResultGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 4),
    _CdsmrResultGroupIdentifier_Type()
)
cdsmrResultGroupIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupIdentifier.setStatus("current")


class _CdsmrResultGroupQueueLimit_Type(Unsigned32):
    """Custom type cdsmrResultGroupQueueLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CdsmrResultGroupQueueLimit_Type.__name__ = "Unsigned32"
_CdsmrResultGroupQueueLimit_Object = MibTableColumn
cdsmrResultGroupQueueLimit = _CdsmrResultGroupQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 5),
    _CdsmrResultGroupQueueLimit_Type()
)
cdsmrResultGroupQueueLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupQueueLimit.setStatus("current")
_CdsmrResultGroupQueueTimeLimit_Type = Unsigned32
_CdsmrResultGroupQueueTimeLimit_Object = MibTableColumn
cdsmrResultGroupQueueTimeLimit = _CdsmrResultGroupQueueTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 6),
    _CdsmrResultGroupQueueTimeLimit_Type()
)
cdsmrResultGroupQueueTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupQueueTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrResultGroupQueueTimeLimit.setUnits("milliseconds")


class _CdsmrResultGroupMatchSmppId_Type(OctetString):
    """Custom type cdsmrResultGroupMatchSmppId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CdsmrResultGroupMatchSmppId_Type.__name__ = "OctetString"
_CdsmrResultGroupMatchSmppId_Object = MibTableColumn
cdsmrResultGroupMatchSmppId = _CdsmrResultGroupMatchSmppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 7),
    _CdsmrResultGroupMatchSmppId_Type()
)
cdsmrResultGroupMatchSmppId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupMatchSmppId.setStatus("current")


class _CdsmrResultGroupMatchSmppType_Type(OctetString):
    """Custom type cdsmrResultGroupMatchSmppType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CdsmrResultGroupMatchSmppType_Type.__name__ = "OctetString"
_CdsmrResultGroupMatchSmppType_Object = MibTableColumn
cdsmrResultGroupMatchSmppType = _CdsmrResultGroupMatchSmppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 8),
    _CdsmrResultGroupMatchSmppType_Type()
)
cdsmrResultGroupMatchSmppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupMatchSmppType.setStatus("current")


class _CdsmrResultGroupMatchUcpId_Type(OctetString):
    """Custom type cdsmrResultGroupMatchUcpId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CdsmrResultGroupMatchUcpId_Type.__name__ = "OctetString"
_CdsmrResultGroupMatchUcpId_Object = MibTableColumn
cdsmrResultGroupMatchUcpId = _CdsmrResultGroupMatchUcpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 9),
    _CdsmrResultGroupMatchUcpId_Type()
)
cdsmrResultGroupMatchUcpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupMatchUcpId.setStatus("current")
_CdsmrResultGroupRowStatus_Type = RowStatus
_CdsmrResultGroupRowStatus_Object = MibTableColumn
cdsmrResultGroupRowStatus = _CdsmrResultGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 3, 1, 10),
    _CdsmrResultGroupRowStatus_Type()
)
cdsmrResultGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGroupRowStatus.setStatus("current")
_CdsmrResultIpTable_Object = MibTable
cdsmrResultIpTable = _CdsmrResultIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4)
)
if mibBuilder.loadTexts:
    cdsmrResultIpTable.setStatus("current")
_CdsmrResultIpTableEntry_Object = MibTableRow
cdsmrResultIpTableEntry = _CdsmrResultIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1)
)
cdsmrResultIpTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrResultGroupName"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrResultIpNumber"),
)
if mibBuilder.loadTexts:
    cdsmrResultIpTableEntry.setStatus("current")
_CdsmrResultIpNumber_Type = CmlrId
_CdsmrResultIpNumber_Object = MibTableColumn
cdsmrResultIpNumber = _CdsmrResultIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 1),
    _CdsmrResultIpNumber_Type()
)
cdsmrResultIpNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrResultIpNumber.setStatus("current")
_CdsmrResultIpRemotePortNumber_Type = InetPortNumber
_CdsmrResultIpRemotePortNumber_Object = MibTableColumn
cdsmrResultIpRemotePortNumber = _CdsmrResultIpRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 2),
    _CdsmrResultIpRemotePortNumber_Type()
)
cdsmrResultIpRemotePortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpRemotePortNumber.setStatus("current")
_CdsmrResultIpRemoteIpAddrType_Type = InetAddressType
_CdsmrResultIpRemoteIpAddrType_Object = MibTableColumn
cdsmrResultIpRemoteIpAddrType = _CdsmrResultIpRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 3),
    _CdsmrResultIpRemoteIpAddrType_Type()
)
cdsmrResultIpRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpRemoteIpAddrType.setStatus("current")
_CdsmrResultIpRemoteIpAddress_Type = InetAddress
_CdsmrResultIpRemoteIpAddress_Object = MibTableColumn
cdsmrResultIpRemoteIpAddress = _CdsmrResultIpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 4),
    _CdsmrResultIpRemoteIpAddress_Type()
)
cdsmrResultIpRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpRemoteIpAddress.setStatus("current")
_CdsmrResultIpProfileName_Type = CmlrName
_CdsmrResultIpProfileName_Object = MibTableColumn
cdsmrResultIpProfileName = _CdsmrResultIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 5),
    _CdsmrResultIpProfileName_Type()
)
cdsmrResultIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpProfileName.setStatus("current")


class _CdsmrResultIpWeight_Type(Integer32):
    """Custom type cdsmrResultIpWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CdsmrResultIpWeight_Type.__name__ = "Integer32"
_CdsmrResultIpWeight_Object = MibTableColumn
cdsmrResultIpWeight = _CdsmrResultIpWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 6),
    _CdsmrResultIpWeight_Type()
)
cdsmrResultIpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpWeight.setStatus("current")
_CdsmrResultIpRowStatus_Type = RowStatus
_CdsmrResultIpRowStatus_Object = MibTableColumn
cdsmrResultIpRowStatus = _CdsmrResultIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 4, 1, 7),
    _CdsmrResultIpRowStatus_Type()
)
cdsmrResultIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultIpRowStatus.setStatus("current")
_CdsmrResultTable_Object = MibTable
cdsmrResultTable = _CdsmrResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5)
)
if mibBuilder.loadTexts:
    cdsmrResultTable.setStatus("current")
_CdsmrResultTableEntry_Object = MibTableRow
cdsmrResultTableEntry = _CdsmrResultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1)
)
cdsmrResultTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrResultGroupName"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrResultNumber"),
)
if mibBuilder.loadTexts:
    cdsmrResultTableEntry.setStatus("current")
_CdsmrResultNumber_Type = CmlrId
_CdsmrResultNumber_Object = MibTableColumn
cdsmrResultNumber = _CdsmrResultNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 1),
    _CdsmrResultNumber_Type()
)
cdsmrResultNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrResultNumber.setStatus("current")
_CdsmrResultDestinationType_Type = CdsmrResultDestinationType
_CdsmrResultDestinationType_Object = MibTableColumn
cdsmrResultDestinationType = _CdsmrResultDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 2),
    _CdsmrResultDestinationType_Type()
)
cdsmrResultDestinationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultDestinationType.setStatus("current")
_CdsmrResultParameters_Type = CdsmrResultParameters
_CdsmrResultParameters_Object = MibTableColumn
cdsmrResultParameters = _CdsmrResultParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 3),
    _CdsmrResultParameters_Type()
)
cdsmrResultParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultParameters.setStatus("current")
_CdsmrResultDestinationName_Type = CmlrName
_CdsmrResultDestinationName_Object = MibTableColumn
cdsmrResultDestinationName = _CdsmrResultDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 4),
    _CdsmrResultDestinationName_Type()
)
cdsmrResultDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultDestinationName.setStatus("current")
_CdsmrResultPc_Type = CItpTcPointCode
_CdsmrResultPc_Object = MibTableColumn
cdsmrResultPc = _CdsmrResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 5),
    _CdsmrResultPc_Type()
)
cdsmrResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultPc.setStatus("current")
_CdsmrResultSsn_Type = CItpTcSubSystemNumber
_CdsmrResultSsn_Object = MibTableColumn
cdsmrResultSsn = _CdsmrResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 6),
    _CdsmrResultSsn_Type()
)
cdsmrResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultSsn.setStatus("current")
_CdsmrResultGt_Type = CItpTcGtaLongDisplay
_CdsmrResultGt_Object = MibTableColumn
cdsmrResultGt = _CdsmrResultGt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 7),
    _CdsmrResultGt_Type()
)
cdsmrResultGt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGt.setStatus("current")
_CdsmrResultTransType_Type = CgsccpGttTransType
_CdsmrResultTransType_Object = MibTableColumn
cdsmrResultTransType = _CdsmrResultTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 8),
    _CdsmrResultTransType_Type()
)
cdsmrResultTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultTransType.setStatus("current")
_CdsmrResultGti_Type = CgsccpGttGlobalTitleInd
_CdsmrResultGti_Object = MibTableColumn
cdsmrResultGti = _CdsmrResultGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 9),
    _CdsmrResultGti_Type()
)
cdsmrResultGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultGti.setStatus("current")
_CdsmrResultNp_Type = CItpTcNumberingPlan
_CdsmrResultNp_Object = MibTableColumn
cdsmrResultNp = _CdsmrResultNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 10),
    _CdsmrResultNp_Type()
)
cdsmrResultNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultNp.setStatus("current")
_CdsmrResultNai_Type = CItpTcNAI
_CdsmrResultNai_Object = MibTableColumn
cdsmrResultNai = _CdsmrResultNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 11),
    _CdsmrResultNai_Type()
)
cdsmrResultNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultNai.setStatus("current")


class _CdsmrResultWeight_Type(Integer32):
    """Custom type cdsmrResultWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CdsmrResultWeight_Type.__name__ = "Integer32"
_CdsmrResultWeight_Object = MibTableColumn
cdsmrResultWeight = _CdsmrResultWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 12),
    _CdsmrResultWeight_Type()
)
cdsmrResultWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultWeight.setStatus("current")
_CdsmrResultNetwork_Type = CItpTcNetworkName
_CdsmrResultNetwork_Object = MibTableColumn
cdsmrResultNetwork = _CdsmrResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 13),
    _CdsmrResultNetwork_Type()
)
cdsmrResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultNetwork.setStatus("current")
_CdsmrResultCounts_Type = Counter32
_CdsmrResultCounts_Object = MibTableColumn
cdsmrResultCounts = _CdsmrResultCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 14),
    _CdsmrResultCounts_Type()
)
cdsmrResultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrResultCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrResultCounts.setUnits("matches")
_CdsmrResultRowStatus_Type = RowStatus
_CdsmrResultRowStatus_Object = MibTableColumn
cdsmrResultRowStatus = _CdsmrResultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 5, 1, 15),
    _CdsmrResultRowStatus_Type()
)
cdsmrResultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrResultRowStatus.setStatus("current")
_CdsmrAddressTable_Object = MibTable
cdsmrAddressTable = _CdsmrAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6)
)
if mibBuilder.loadTexts:
    cdsmrAddressTable.setStatus("current")
_CdsmrAddressTableEntry_Object = MibTableRow
cdsmrAddressTableEntry = _CdsmrAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1)
)
cdsmrAddressTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrAddressTableName"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrAddressType"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrAddressDigits"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrAddressExactMatch"),
)
if mibBuilder.loadTexts:
    cdsmrAddressTableEntry.setStatus("current")
_CdsmrAddressTableName_Type = CmlrName
_CdsmrAddressTableName_Object = MibTableColumn
cdsmrAddressTableName = _CdsmrAddressTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 1),
    _CdsmrAddressTableName_Type()
)
cdsmrAddressTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrAddressTableName.setStatus("current")
_CdsmrAddressType_Type = CmlrAddressType
_CdsmrAddressType_Object = MibTableColumn
cdsmrAddressType = _CdsmrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 2),
    _CdsmrAddressType_Type()
)
cdsmrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrAddressType.setStatus("current")
_CdsmrAddressDigits_Type = CmlrAddressDigits
_CdsmrAddressDigits_Object = MibTableColumn
cdsmrAddressDigits = _CdsmrAddressDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 3),
    _CdsmrAddressDigits_Type()
)
cdsmrAddressDigits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrAddressDigits.setStatus("current")
_CdsmrAddressExactMatch_Type = TruthValue
_CdsmrAddressExactMatch_Object = MibTableColumn
cdsmrAddressExactMatch = _CdsmrAddressExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 4),
    _CdsmrAddressExactMatch_Type()
)
cdsmrAddressExactMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrAddressExactMatch.setStatus("current")
_CdsmrAddressResultParameters_Type = CdsmrResultParameters
_CdsmrAddressResultParameters_Object = MibTableColumn
cdsmrAddressResultParameters = _CdsmrAddressResultParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 5),
    _CdsmrAddressResultParameters_Type()
)
cdsmrAddressResultParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultParameters.setStatus("current")
_CdsmrAddressResultNetwork_Type = CItpTcNetworkName
_CdsmrAddressResultNetwork_Object = MibTableColumn
cdsmrAddressResultNetwork = _CdsmrAddressResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 6),
    _CdsmrAddressResultNetwork_Type()
)
cdsmrAddressResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultNetwork.setStatus("current")
_CdsmrAddressResultType_Type = CdsmrResultType
_CdsmrAddressResultType_Object = MibTableColumn
cdsmrAddressResultType = _CdsmrAddressResultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 7),
    _CdsmrAddressResultType_Type()
)
cdsmrAddressResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultType.setStatus("current")
_CdsmrAddressResultOctet_Type = CdsmrResultOctet
_CdsmrAddressResultOctet_Object = MibTableColumn
cdsmrAddressResultOctet = _CdsmrAddressResultOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 8),
    _CdsmrAddressResultOctet_Type()
)
cdsmrAddressResultOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultOctet.setStatus("current")
_CdsmrAddressResultTransType_Type = CgsccpGttTransType
_CdsmrAddressResultTransType_Object = MibTableColumn
cdsmrAddressResultTransType = _CdsmrAddressResultTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 9),
    _CdsmrAddressResultTransType_Type()
)
cdsmrAddressResultTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultTransType.setStatus("current")


class _CdsmrAddressResultGti_Type(CgsccpGttGlobalTitleInd):
    """Custom type cdsmrAddressResultGti based on CgsccpGttGlobalTitleInd"""
    defaultValue = 0


_CdsmrAddressResultGti_Object = MibTableColumn
cdsmrAddressResultGti = _CdsmrAddressResultGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 10),
    _CdsmrAddressResultGti_Type()
)
cdsmrAddressResultGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultGti.setStatus("current")
_CdsmrAddressResultNp_Type = CItpTcNumberingPlan
_CdsmrAddressResultNp_Object = MibTableColumn
cdsmrAddressResultNp = _CdsmrAddressResultNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 11),
    _CdsmrAddressResultNp_Type()
)
cdsmrAddressResultNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultNp.setStatus("current")
_CdsmrAddressResultNai_Type = CItpTcNAI
_CdsmrAddressResultNai_Object = MibTableColumn
cdsmrAddressResultNai = _CdsmrAddressResultNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 12),
    _CdsmrAddressResultNai_Type()
)
cdsmrAddressResultNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultNai.setStatus("current")
_CdsmrAddressResultPc_Type = CItpTcPointCode
_CdsmrAddressResultPc_Object = MibTableColumn
cdsmrAddressResultPc = _CdsmrAddressResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 13),
    _CdsmrAddressResultPc_Type()
)
cdsmrAddressResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultPc.setStatus("current")
_CdsmrAddressResultSsn_Type = CItpTcSubSystemNumber
_CdsmrAddressResultSsn_Object = MibTableColumn
cdsmrAddressResultSsn = _CdsmrAddressResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 14),
    _CdsmrAddressResultSsn_Type()
)
cdsmrAddressResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultSsn.setStatus("current")
_CdsmrAddressResultRuleNumber_Type = CmlrId
_CdsmrAddressResultRuleNumber_Object = MibTableColumn
cdsmrAddressResultRuleNumber = _CdsmrAddressResultRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 15),
    _CdsmrAddressResultRuleNumber_Type()
)
cdsmrAddressResultRuleNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressResultRuleNumber.setStatus("current")
_CdsmrAddressMatchCounts_Type = Counter32
_CdsmrAddressMatchCounts_Object = MibTableColumn
cdsmrAddressMatchCounts = _CdsmrAddressMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 16),
    _CdsmrAddressMatchCounts_Type()
)
cdsmrAddressMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrAddressMatchCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrAddressMatchCounts.setUnits("matches")
_CdsmrAddressRowStatus_Type = RowStatus
_CdsmrAddressRowStatus_Object = MibTableColumn
cdsmrAddressRowStatus = _CdsmrAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 6, 1, 17),
    _CdsmrAddressRowStatus_Type()
)
cdsmrAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrAddressRowStatus.setStatus("current")
_CdsmrRuleSetTable_Object = MibTable
cdsmrRuleSetTable = _CdsmrRuleSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7)
)
if mibBuilder.loadTexts:
    cdsmrRuleSetTable.setStatus("current")
_CdsmrRuleSetTableEntry_Object = MibTableRow
cdsmrRuleSetTableEntry = _CdsmrRuleSetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1)
)
cdsmrRuleSetTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrRuleSetName"),
)
if mibBuilder.loadTexts:
    cdsmrRuleSetTableEntry.setStatus("current")
_CdsmrRuleSetName_Type = CmlrRuleSetName
_CdsmrRuleSetName_Object = MibTableColumn
cdsmrRuleSetName = _CdsmrRuleSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1, 1),
    _CdsmrRuleSetName_Type()
)
cdsmrRuleSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrRuleSetName.setStatus("current")
_CdsmrRuleSetProtocol_Type = CmlrRuleProtocol
_CdsmrRuleSetProtocol_Object = MibTableColumn
cdsmrRuleSetProtocol = _CdsmrRuleSetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1, 2),
    _CdsmrRuleSetProtocol_Type()
)
cdsmrRuleSetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleSetProtocol.setStatus("current")
_CdsmrRuleSetStartDateAndTime_Type = DateAndTime
_CdsmrRuleSetStartDateAndTime_Object = MibTableColumn
cdsmrRuleSetStartDateAndTime = _CdsmrRuleSetStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1, 3),
    _CdsmrRuleSetStartDateAndTime_Type()
)
cdsmrRuleSetStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleSetStartDateAndTime.setStatus("current")
_CdsmrRuleSetEndDateAndTime_Type = DateAndTime
_CdsmrRuleSetEndDateAndTime_Object = MibTableColumn
cdsmrRuleSetEndDateAndTime = _CdsmrRuleSetEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1, 4),
    _CdsmrRuleSetEndDateAndTime_Type()
)
cdsmrRuleSetEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleSetEndDateAndTime.setStatus("current")
_CdsmrRuleSetRowStatus_Type = RowStatus
_CdsmrRuleSetRowStatus_Object = MibTableColumn
cdsmrRuleSetRowStatus = _CdsmrRuleSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 7, 1, 5),
    _CdsmrRuleSetRowStatus_Type()
)
cdsmrRuleSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleSetRowStatus.setStatus("current")
_CdsmrRuleTable_Object = MibTable
cdsmrRuleTable = _CdsmrRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8)
)
if mibBuilder.loadTexts:
    cdsmrRuleTable.setStatus("current")
_CdsmrRuleTableEntry_Object = MibTableRow
cdsmrRuleTableEntry = _CdsmrRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1)
)
cdsmrRuleTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrRuleSetName"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrRuleNumber"),
)
if mibBuilder.loadTexts:
    cdsmrRuleTableEntry.setStatus("current")
_CdsmrRuleNumber_Type = CmlrId
_CdsmrRuleNumber_Object = MibTableColumn
cdsmrRuleNumber = _CdsmrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 1),
    _CdsmrRuleNumber_Type()
)
cdsmrRuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrRuleNumber.setStatus("current")


class _CdsmrRuleOperationType_Type(Integer32):
    """Custom type cdsmrRuleOperationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("smdPp", 2),
          ("smsMo", 3),
          ("smsMt", 4),
          ("smsNot", 7),
          ("smsReg", 6),
          ("smsSri", 5),
          ("ucpSubmit", 8))
    )


_CdsmrRuleOperationType_Type.__name__ = "Integer32"
_CdsmrRuleOperationType_Object = MibTableColumn
cdsmrRuleOperationType = _CdsmrRuleOperationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 2),
    _CdsmrRuleOperationType_Type()
)
cdsmrRuleOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOperationType.setStatus("current")


class _CdsmrRuleCdrServiceQueue_Type(Integer32):
    """Custom type cdsmrRuleCdrServiceQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("congested", 2),
          ("none", 0),
          ("unavailable", 3))
    )


_CdsmrRuleCdrServiceQueue_Type.__name__ = "Integer32"
_CdsmrRuleCdrServiceQueue_Object = MibTableColumn
cdsmrRuleCdrServiceQueue = _CdsmrRuleCdrServiceQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 3),
    _CdsmrRuleCdrServiceQueue_Type()
)
cdsmrRuleCdrServiceQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleCdrServiceQueue.setStatus("current")


class _CdsmrRuleInputParameters_Type(Bits):
    """Custom type cdsmrRuleInputParameters based on Bits"""
    namedValues = NamedValues(
        *(("cdrService", 0),
          ("default", 53),
          ("destPort", 1),
          ("destSmeExact", 3),
          ("destSmeGta", 2),
          ("destSmeImsi", 6),
          ("destSmeMaxDigits", 9),
          ("destSmeMin", 7),
          ("destSmeMinDigits", 8),
          ("destSmeNai", 4),
          ("destSmeNp", 5),
          ("destSmeTable", 10),
          ("destSmeTableImsi", 12),
          ("destSmeTableLoc", 11),
          ("destSmeTableMin", 13),
          ("destSmeTableNai", 14),
          ("destSmeTableNp", 15),
          ("destSmscExact", 17),
          ("destSmscGta", 16),
          ("destSmscMaxDigits", 21),
          ("destSmscMinDigits", 20),
          ("destSmscNai", 18),
          ("destSmscNp", 19),
          ("origImsiExact", 23),
          ("origImsiGta", 22),
          ("origImsiMaxDigits", 28),
          ("origImsiMinDigits", 27),
          ("origImsiNai", 25),
          ("origImsiNp", 26),
          ("origImsiTable", 29),
          ("origImsiTableLoc", 30),
          ("origImsiUnknown", 24),
          ("origSmeExact", 32),
          ("origSmeGta", 31),
          ("origSmeMaxDigits", 36),
          ("origSmeMinDigits", 35),
          ("origSmeNai", 33),
          ("origSmeNp", 34),
          ("origSmeTable", 37),
          ("origSmeTableLoc", 38),
          ("origSmeTableNai", 39),
          ("origSmeTableNp", 40),
          ("origSmscExact", 42),
          ("origSmscGta", 41),
          ("origSmscMaxDigits", 46),
          ("origSmscMinDigits", 45),
          ("origSmscNai", 43),
          ("origSmscNp", 44),
          ("origSmscTable", 47),
          ("origSmscTableLoc", 48),
          ("origSmscTableNai", 49),
          ("origSmscTableNp", 50),
          ("pid", 51),
          ("tid", 52))
    )

_CdsmrRuleInputParameters_Type.__name__ = "Bits"
_CdsmrRuleInputParameters_Object = MibTableColumn
cdsmrRuleInputParameters = _CdsmrRuleInputParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 4),
    _CdsmrRuleInputParameters_Type()
)
cdsmrRuleInputParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleInputParameters.setStatus("current")


class _CdsmrRuleDestPort_Type(Unsigned32):
    """Custom type cdsmrRuleDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdsmrRuleDestPort_Type.__name__ = "Unsigned32"
_CdsmrRuleDestPort_Object = MibTableColumn
cdsmrRuleDestPort = _CdsmrRuleDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 5),
    _CdsmrRuleDestPort_Type()
)
cdsmrRuleDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestPort.setStatus("current")
_CdsmrRuleDestSmeGta_Type = CItpTcGtaLongDisplay
_CdsmrRuleDestSmeGta_Object = MibTableColumn
cdsmrRuleDestSmeGta = _CdsmrRuleDestSmeGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 6),
    _CdsmrRuleDestSmeGta_Type()
)
cdsmrRuleDestSmeGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeGta.setStatus("current")
_CdsmrRuleDestSmeNai_Type = CItpTcNAI
_CdsmrRuleDestSmeNai_Object = MibTableColumn
cdsmrRuleDestSmeNai = _CdsmrRuleDestSmeNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 7),
    _CdsmrRuleDestSmeNai_Type()
)
cdsmrRuleDestSmeNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeNai.setStatus("current")
_CdsmrRuleDestSmeNp_Type = CItpTcNumberingPlan
_CdsmrRuleDestSmeNp_Object = MibTableColumn
cdsmrRuleDestSmeNp = _CdsmrRuleDestSmeNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 8),
    _CdsmrRuleDestSmeNp_Type()
)
cdsmrRuleDestSmeNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeNp.setStatus("current")
_CdsmrRuleDestSmeMinDigits_Type = CdsmrMinimumDigits
_CdsmrRuleDestSmeMinDigits_Object = MibTableColumn
cdsmrRuleDestSmeMinDigits = _CdsmrRuleDestSmeMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 9),
    _CdsmrRuleDestSmeMinDigits_Type()
)
cdsmrRuleDestSmeMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeMinDigits.setStatus("current")
_CdsmrRuleDestSmeMaxDigits_Type = CdsmrMaximumDigits
_CdsmrRuleDestSmeMaxDigits_Object = MibTableColumn
cdsmrRuleDestSmeMaxDigits = _CdsmrRuleDestSmeMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 10),
    _CdsmrRuleDestSmeMaxDigits_Type()
)
cdsmrRuleDestSmeMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeMaxDigits.setStatus("current")
_CdsmrRuleDestSmeTable_Type = CmlrName
_CdsmrRuleDestSmeTable_Object = MibTableColumn
cdsmrRuleDestSmeTable = _CdsmrRuleDestSmeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 11),
    _CdsmrRuleDestSmeTable_Type()
)
cdsmrRuleDestSmeTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeTable.setStatus("current")
_CdsmrRuleDestSmeTableNai_Type = CItpTcNAI
_CdsmrRuleDestSmeTableNai_Object = MibTableColumn
cdsmrRuleDestSmeTableNai = _CdsmrRuleDestSmeTableNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 12),
    _CdsmrRuleDestSmeTableNai_Type()
)
cdsmrRuleDestSmeTableNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeTableNai.setStatus("current")
_CdsmrRuleDestSmeTableNp_Type = CItpTcNumberingPlan
_CdsmrRuleDestSmeTableNp_Object = MibTableColumn
cdsmrRuleDestSmeTableNp = _CdsmrRuleDestSmeTableNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 13),
    _CdsmrRuleDestSmeTableNp_Type()
)
cdsmrRuleDestSmeTableNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmeTableNp.setStatus("current")
_CdsmrRuleDestSmscGta_Type = CItpTcGtaLongDisplay
_CdsmrRuleDestSmscGta_Object = MibTableColumn
cdsmrRuleDestSmscGta = _CdsmrRuleDestSmscGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 14),
    _CdsmrRuleDestSmscGta_Type()
)
cdsmrRuleDestSmscGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmscGta.setStatus("current")
_CdsmrRuleDestSmscNai_Type = CItpTcNAI
_CdsmrRuleDestSmscNai_Object = MibTableColumn
cdsmrRuleDestSmscNai = _CdsmrRuleDestSmscNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 15),
    _CdsmrRuleDestSmscNai_Type()
)
cdsmrRuleDestSmscNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmscNai.setStatus("current")
_CdsmrRuleDestSmscNp_Type = CItpTcNumberingPlan
_CdsmrRuleDestSmscNp_Object = MibTableColumn
cdsmrRuleDestSmscNp = _CdsmrRuleDestSmscNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 16),
    _CdsmrRuleDestSmscNp_Type()
)
cdsmrRuleDestSmscNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmscNp.setStatus("current")
_CdsmrRuleDestSmscMinDigits_Type = CdsmrMinimumDigits
_CdsmrRuleDestSmscMinDigits_Object = MibTableColumn
cdsmrRuleDestSmscMinDigits = _CdsmrRuleDestSmscMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 17),
    _CdsmrRuleDestSmscMinDigits_Type()
)
cdsmrRuleDestSmscMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmscMinDigits.setStatus("current")
_CdsmrRuleDestSmscMaxDigits_Type = CdsmrMaximumDigits
_CdsmrRuleDestSmscMaxDigits_Object = MibTableColumn
cdsmrRuleDestSmscMaxDigits = _CdsmrRuleDestSmscMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 18),
    _CdsmrRuleDestSmscMaxDigits_Type()
)
cdsmrRuleDestSmscMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleDestSmscMaxDigits.setStatus("current")
_CdsmrRuleOrigImsiGta_Type = CItpTcGtaLongDisplay
_CdsmrRuleOrigImsiGta_Object = MibTableColumn
cdsmrRuleOrigImsiGta = _CdsmrRuleOrigImsiGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 19),
    _CdsmrRuleOrigImsiGta_Type()
)
cdsmrRuleOrigImsiGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiGta.setStatus("current")
_CdsmrRuleOrigImsiNai_Type = CItpTcNAI
_CdsmrRuleOrigImsiNai_Object = MibTableColumn
cdsmrRuleOrigImsiNai = _CdsmrRuleOrigImsiNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 20),
    _CdsmrRuleOrigImsiNai_Type()
)
cdsmrRuleOrigImsiNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiNai.setStatus("current")
_CdsmrRuleOrigImsiNp_Type = CItpTcNumberingPlan
_CdsmrRuleOrigImsiNp_Object = MibTableColumn
cdsmrRuleOrigImsiNp = _CdsmrRuleOrigImsiNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 21),
    _CdsmrRuleOrigImsiNp_Type()
)
cdsmrRuleOrigImsiNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiNp.setStatus("current")
_CdsmrRuleOrigImsiMinDigits_Type = CdsmrMinimumDigits
_CdsmrRuleOrigImsiMinDigits_Object = MibTableColumn
cdsmrRuleOrigImsiMinDigits = _CdsmrRuleOrigImsiMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 22),
    _CdsmrRuleOrigImsiMinDigits_Type()
)
cdsmrRuleOrigImsiMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiMinDigits.setStatus("current")
_CdsmrRuleOrigImsiMaxDigits_Type = CdsmrMaximumDigits
_CdsmrRuleOrigImsiMaxDigits_Object = MibTableColumn
cdsmrRuleOrigImsiMaxDigits = _CdsmrRuleOrigImsiMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 23),
    _CdsmrRuleOrigImsiMaxDigits_Type()
)
cdsmrRuleOrigImsiMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiMaxDigits.setStatus("current")
_CdsmrRuleOrigImsiTable_Type = CmlrName
_CdsmrRuleOrigImsiTable_Object = MibTableColumn
cdsmrRuleOrigImsiTable = _CdsmrRuleOrigImsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 24),
    _CdsmrRuleOrigImsiTable_Type()
)
cdsmrRuleOrigImsiTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigImsiTable.setStatus("current")
_CdsmrRuleOrigSmeGta_Type = CItpTcGtaLongDisplay
_CdsmrRuleOrigSmeGta_Object = MibTableColumn
cdsmrRuleOrigSmeGta = _CdsmrRuleOrigSmeGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 25),
    _CdsmrRuleOrigSmeGta_Type()
)
cdsmrRuleOrigSmeGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeGta.setStatus("current")
_CdsmrRuleOrigSmeNai_Type = CItpTcNAI
_CdsmrRuleOrigSmeNai_Object = MibTableColumn
cdsmrRuleOrigSmeNai = _CdsmrRuleOrigSmeNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 26),
    _CdsmrRuleOrigSmeNai_Type()
)
cdsmrRuleOrigSmeNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeNai.setStatus("current")
_CdsmrRuleOrigSmeNp_Type = CItpTcNumberingPlan
_CdsmrRuleOrigSmeNp_Object = MibTableColumn
cdsmrRuleOrigSmeNp = _CdsmrRuleOrigSmeNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 27),
    _CdsmrRuleOrigSmeNp_Type()
)
cdsmrRuleOrigSmeNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeNp.setStatus("current")
_CdsmrRuleOrigSmeMinDigits_Type = CdsmrMinimumDigits
_CdsmrRuleOrigSmeMinDigits_Object = MibTableColumn
cdsmrRuleOrigSmeMinDigits = _CdsmrRuleOrigSmeMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 28),
    _CdsmrRuleOrigSmeMinDigits_Type()
)
cdsmrRuleOrigSmeMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeMinDigits.setStatus("current")
_CdsmrRuleOrigSmeMaxDigits_Type = CdsmrMaximumDigits
_CdsmrRuleOrigSmeMaxDigits_Object = MibTableColumn
cdsmrRuleOrigSmeMaxDigits = _CdsmrRuleOrigSmeMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 29),
    _CdsmrRuleOrigSmeMaxDigits_Type()
)
cdsmrRuleOrigSmeMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeMaxDigits.setStatus("current")
_CdsmrRuleOrigSmeTable_Type = CmlrName
_CdsmrRuleOrigSmeTable_Object = MibTableColumn
cdsmrRuleOrigSmeTable = _CdsmrRuleOrigSmeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 30),
    _CdsmrRuleOrigSmeTable_Type()
)
cdsmrRuleOrigSmeTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeTable.setStatus("current")
_CdsmrRuleOrigSmeTableNai_Type = CItpTcNAI
_CdsmrRuleOrigSmeTableNai_Object = MibTableColumn
cdsmrRuleOrigSmeTableNai = _CdsmrRuleOrigSmeTableNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 31),
    _CdsmrRuleOrigSmeTableNai_Type()
)
cdsmrRuleOrigSmeTableNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeTableNai.setStatus("current")
_CdsmrRuleOrigSmeTableNp_Type = CItpTcNumberingPlan
_CdsmrRuleOrigSmeTableNp_Object = MibTableColumn
cdsmrRuleOrigSmeTableNp = _CdsmrRuleOrigSmeTableNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 32),
    _CdsmrRuleOrigSmeTableNp_Type()
)
cdsmrRuleOrigSmeTableNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmeTableNp.setStatus("current")
_CdsmrRuleOrigSmscGta_Type = CItpTcGtaLongDisplay
_CdsmrRuleOrigSmscGta_Object = MibTableColumn
cdsmrRuleOrigSmscGta = _CdsmrRuleOrigSmscGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 33),
    _CdsmrRuleOrigSmscGta_Type()
)
cdsmrRuleOrigSmscGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscGta.setStatus("current")
_CdsmrRuleOrigSmscNai_Type = CItpTcNAI
_CdsmrRuleOrigSmscNai_Object = MibTableColumn
cdsmrRuleOrigSmscNai = _CdsmrRuleOrigSmscNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 34),
    _CdsmrRuleOrigSmscNai_Type()
)
cdsmrRuleOrigSmscNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscNai.setStatus("current")
_CdsmrRuleOrigSmscNp_Type = CItpTcNumberingPlan
_CdsmrRuleOrigSmscNp_Object = MibTableColumn
cdsmrRuleOrigSmscNp = _CdsmrRuleOrigSmscNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 35),
    _CdsmrRuleOrigSmscNp_Type()
)
cdsmrRuleOrigSmscNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscNp.setStatus("current")
_CdsmrRuleOrigSmscMinDigits_Type = CdsmrMinimumDigits
_CdsmrRuleOrigSmscMinDigits_Object = MibTableColumn
cdsmrRuleOrigSmscMinDigits = _CdsmrRuleOrigSmscMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 36),
    _CdsmrRuleOrigSmscMinDigits_Type()
)
cdsmrRuleOrigSmscMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscMinDigits.setStatus("current")
_CdsmrRuleOrigSmscMaxDigits_Type = CdsmrMaximumDigits
_CdsmrRuleOrigSmscMaxDigits_Object = MibTableColumn
cdsmrRuleOrigSmscMaxDigits = _CdsmrRuleOrigSmscMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 37),
    _CdsmrRuleOrigSmscMaxDigits_Type()
)
cdsmrRuleOrigSmscMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscMaxDigits.setStatus("current")
_CdsmrRuleOrigSmscTable_Type = CmlrName
_CdsmrRuleOrigSmscTable_Object = MibTableColumn
cdsmrRuleOrigSmscTable = _CdsmrRuleOrigSmscTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 38),
    _CdsmrRuleOrigSmscTable_Type()
)
cdsmrRuleOrigSmscTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscTable.setStatus("current")
_CdsmrRuleOrigSmscTableNai_Type = CItpTcNAI
_CdsmrRuleOrigSmscTableNai_Object = MibTableColumn
cdsmrRuleOrigSmscTableNai = _CdsmrRuleOrigSmscTableNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 39),
    _CdsmrRuleOrigSmscTableNai_Type()
)
cdsmrRuleOrigSmscTableNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscTableNai.setStatus("current")
_CdsmrRuleOrigSmscTableNp_Type = CItpTcNumberingPlan
_CdsmrRuleOrigSmscTableNp_Object = MibTableColumn
cdsmrRuleOrigSmscTableNp = _CdsmrRuleOrigSmscTableNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 40),
    _CdsmrRuleOrigSmscTableNp_Type()
)
cdsmrRuleOrigSmscTableNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleOrigSmscTableNp.setStatus("current")


class _CdsmrRuleProtocolId_Type(Unsigned32):
    """Custom type cdsmrRuleProtocolId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdsmrRuleProtocolId_Type.__name__ = "Unsigned32"
_CdsmrRuleProtocolId_Object = MibTableColumn
cdsmrRuleProtocolId = _CdsmrRuleProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 41),
    _CdsmrRuleProtocolId_Type()
)
cdsmrRuleProtocolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleProtocolId.setStatus("current")


class _CdsmrRuleTeleserviceId_Type(Unsigned32):
    """Custom type cdsmrRuleTeleserviceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdsmrRuleTeleserviceId_Type.__name__ = "Unsigned32"
_CdsmrRuleTeleserviceId_Object = MibTableColumn
cdsmrRuleTeleserviceId = _CdsmrRuleTeleserviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 42),
    _CdsmrRuleTeleserviceId_Type()
)
cdsmrRuleTeleserviceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleTeleserviceId.setStatus("current")
_CdsmrRuleResultParameters_Type = CdsmrResultParameters
_CdsmrRuleResultParameters_Object = MibTableColumn
cdsmrRuleResultParameters = _CdsmrRuleResultParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 43),
    _CdsmrRuleResultParameters_Type()
)
cdsmrRuleResultParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultParameters.setStatus("current")
_CdsmrRuleResultNetwork_Type = CItpTcNetworkName
_CdsmrRuleResultNetwork_Object = MibTableColumn
cdsmrRuleResultNetwork = _CdsmrRuleResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 44),
    _CdsmrRuleResultNetwork_Type()
)
cdsmrRuleResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultNetwork.setStatus("current")
_CdsmrRuleResultType_Type = CdsmrResultType
_CdsmrRuleResultType_Object = MibTableColumn
cdsmrRuleResultType = _CdsmrRuleResultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 45),
    _CdsmrRuleResultType_Type()
)
cdsmrRuleResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultType.setStatus("current")
_CdsmrRuleResultOctet_Type = CdsmrResultOctet
_CdsmrRuleResultOctet_Object = MibTableColumn
cdsmrRuleResultOctet = _CdsmrRuleResultOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 46),
    _CdsmrRuleResultOctet_Type()
)
cdsmrRuleResultOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultOctet.setStatus("current")
_CdsmrRuleResultTransType_Type = CgsccpGttTransType
_CdsmrRuleResultTransType_Object = MibTableColumn
cdsmrRuleResultTransType = _CdsmrRuleResultTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 47),
    _CdsmrRuleResultTransType_Type()
)
cdsmrRuleResultTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultTransType.setStatus("current")
_CdsmrRuleResultGti_Type = CgsccpGttGlobalTitleInd
_CdsmrRuleResultGti_Object = MibTableColumn
cdsmrRuleResultGti = _CdsmrRuleResultGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 48),
    _CdsmrRuleResultGti_Type()
)
cdsmrRuleResultGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultGti.setStatus("current")
_CdsmrRuleResultNp_Type = CItpTcNumberingPlan
_CdsmrRuleResultNp_Object = MibTableColumn
cdsmrRuleResultNp = _CdsmrRuleResultNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 49),
    _CdsmrRuleResultNp_Type()
)
cdsmrRuleResultNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultNp.setStatus("current")
_CdsmrRuleResultNai_Type = CItpTcNAI
_CdsmrRuleResultNai_Object = MibTableColumn
cdsmrRuleResultNai = _CdsmrRuleResultNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 50),
    _CdsmrRuleResultNai_Type()
)
cdsmrRuleResultNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultNai.setStatus("current")
_CdsmrRuleResultPc_Type = CItpTcPointCode
_CdsmrRuleResultPc_Object = MibTableColumn
cdsmrRuleResultPc = _CdsmrRuleResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 51),
    _CdsmrRuleResultPc_Type()
)
cdsmrRuleResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultPc.setStatus("current")
_CdsmrRuleResultSsn_Type = CItpTcSubSystemNumber
_CdsmrRuleResultSsn_Object = MibTableColumn
cdsmrRuleResultSsn = _CdsmrRuleResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 52),
    _CdsmrRuleResultSsn_Type()
)
cdsmrRuleResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultSsn.setStatus("current")
_CdsmrRuleResultRuleNumber_Type = CmlrId
_CdsmrRuleResultRuleNumber_Object = MibTableColumn
cdsmrRuleResultRuleNumber = _CdsmrRuleResultRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 53),
    _CdsmrRuleResultRuleNumber_Type()
)
cdsmrRuleResultRuleNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultRuleNumber.setStatus("current")
_CdsmrRuleResultRowStatus_Type = RowStatus
_CdsmrRuleResultRowStatus_Object = MibTableColumn
cdsmrRuleResultRowStatus = _CdsmrRuleResultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 8, 1, 54),
    _CdsmrRuleResultRowStatus_Type()
)
cdsmrRuleResultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrRuleResultRowStatus.setStatus("current")
_CdsmrRuleStatsTable_Object = MibTable
cdsmrRuleStatsTable = _CdsmrRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 9)
)
if mibBuilder.loadTexts:
    cdsmrRuleStatsTable.setStatus("current")
_CdsmrRuleStatsTableEntry_Object = MibTableRow
cdsmrRuleStatsTableEntry = _CdsmrRuleStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 9, 1)
)
cdsmrRuleStatsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrRuleSetName"),
    (0, "CISCO-ITP-DSMR-MIB", "cdsmrRuleNumber"),
)
if mibBuilder.loadTexts:
    cdsmrRuleStatsTableEntry.setStatus("current")
_CdsmrRuleStatsCheckedCounts_Type = Counter32
_CdsmrRuleStatsCheckedCounts_Object = MibTableColumn
cdsmrRuleStatsCheckedCounts = _CdsmrRuleStatsCheckedCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 9, 1, 1),
    _CdsmrRuleStatsCheckedCounts_Type()
)
cdsmrRuleStatsCheckedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrRuleStatsCheckedCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrRuleStatsCheckedCounts.setUnits("checks")
_CdsmrRuleStatsMatchCounts_Type = Counter32
_CdsmrRuleStatsMatchCounts_Object = MibTableColumn
cdsmrRuleStatsMatchCounts = _CdsmrRuleStatsMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 9, 1, 2),
    _CdsmrRuleStatsMatchCounts_Type()
)
cdsmrRuleStatsMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrRuleStatsMatchCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrRuleStatsMatchCounts.setUnits("matches")
_CdsmrRuleStatsRoutedCounts_Type = Counter32
_CdsmrRuleStatsRoutedCounts_Object = MibTableColumn
cdsmrRuleStatsRoutedCounts = _CdsmrRuleStatsRoutedCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 1, 9, 1, 3),
    _CdsmrRuleStatsRoutedCounts_Type()
)
cdsmrRuleStatsRoutedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrRuleStatsRoutedCounts.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrRuleStatsRoutedCounts.setUnits("successes")
_CiscoItpDsmrMIBConform_ObjectIdentity = ObjectIdentity
ciscoItpDsmrMIBConform = _CiscoItpDsmrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2)
)
_CiscoItpDsmrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpDsmrMIBCompliances = _CiscoItpDsmrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 1)
)
_CiscoItpDsmrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpDsmrMIBGroups = _CiscoItpDsmrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2)
)

# Managed Objects groups

ciscoItpDsmrInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2, 1)
)
ciscoItpDsmrInstanceGroup.setObjects(
      *(("CISCO-ITP-DSMR-MIB", "cdsmrTableLoadNotifEnabled"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLastChanged"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLastLoadTime"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLoadStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLastURL"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDeliveredSmppCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDeliveredUcpCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDeliveredGsmCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDeferredGsmCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstGsmStatusReports"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstUcpNotifications"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstSmppDeliveryReceipts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRoutingFailures"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstResultFailures"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstInternalErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstParseErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstResourceErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstProvisioningErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDestUnreachableErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstDestSignalErrors"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstTimeOuts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstBlockedPackets"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRoutingRequestsRcvdGsm"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRoutingRequestsRcvdIs41"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRoutingRequestsRcvdUcp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRoutingRequestsRcvdSmpp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrInstanceGroup.setStatus("current")

ciscoItpDsmrResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2, 2)
)
ciscoItpDsmrResultGroup.setObjects(
      *(("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupServerType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupCdrConsolidation"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupIdentifier"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupQueueLimit"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupQueueTimeLimit"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupMatchSmppId"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupMatchSmppType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupMatchUcpId"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGroupRowStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultDestinationType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultParameters"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultDestinationName"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultPc"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultSsn"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGt"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultTransType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultGti"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultWeight"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultNetwork"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultRowStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpRemotePortNumber"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpRemoteIpAddrType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpRemoteIpAddress"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpProfileName"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpWeight"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrResultIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrResultGroup.setStatus("current")

ciscoItpDsmrAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2, 3)
)
ciscoItpDsmrAddressGroup.setObjects(
      *(("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultParameters"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultNetwork"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultOctet"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultTransType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultGti"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultPc"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultSsn"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressResultRuleNumber"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressMatchCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrAddressRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrAddressGroup.setStatus("current")

ciscoItpDsmrRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2, 4)
)
ciscoItpDsmrRulesGroup.setObjects(
      *(("CISCO-ITP-DSMR-MIB", "cdsmrRuleSetProtocol"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleSetStartDateAndTime"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleSetEndDateAndTime"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleSetRowStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOperationType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleCdrServiceQueue"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleInputParameters"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestPort"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeGta"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeMinDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeMaxDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeTable"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeTableNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmeTableNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmscGta"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmscNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmscNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmscMinDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleDestSmscMaxDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiGta"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiMinDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiMaxDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigImsiTable"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeGta"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeMinDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeMaxDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeTable"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeTableNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmeTableNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscGta"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscMinDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscMaxDigits"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscTable"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscTableNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleOrigSmscTableNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleProtocolId"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleTeleserviceId"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultParameters"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultNetwork"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultOctet"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultTransType"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultGti"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultNp"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultNai"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultPc"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultSsn"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultRuleNumber"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleResultRowStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleStatsMatchCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleStatsCheckedCounts"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrRuleStatsRoutedCounts"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrRulesGroup.setStatus("current")


# Notification objects

ciscoItpDsmrTableLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 0, 1)
)
ciscoItpDsmrTableLoad.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLoadStatus"),
        ("CISCO-ITP-DSMR-MIB", "cdsmrInstLastURL"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrTableLoad.setStatus(
        "current"
    )


# Notifications groups

ciscoItpDsmrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 2, 6)
)
ciscoItpDsmrNotificationsGroup.setObjects(
    ("CISCO-ITP-DSMR-MIB", "ciscoItpDsmrTableLoad")
)
if mibBuilder.loadTexts:
    ciscoItpDsmrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpDsmrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1300, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpDsmrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-DSMR-MIB",
    **{"CdsmrMaximumDigits": CdsmrMaximumDigits,
       "CdsmrMinimumDigits": CdsmrMinimumDigits,
       "CdsmrResultDestinationType": CdsmrResultDestinationType,
       "CdsmrResultOctet": CdsmrResultOctet,
       "CdsmrResultParameters": CdsmrResultParameters,
       "CdsmrResultType": CdsmrResultType,
       "ciscoItpDsmrMIB": ciscoItpDsmrMIB,
       "ciscoItpDsmrMIBNotifs": ciscoItpDsmrMIBNotifs,
       "ciscoItpDsmrTableLoad": ciscoItpDsmrTableLoad,
       "ciscoItpDsmrMIBObjects": ciscoItpDsmrMIBObjects,
       "cdsmrScalars": cdsmrScalars,
       "cdsmrTableLoadNotifEnabled": cdsmrTableLoadNotifEnabled,
       "cdsmrInstTable": cdsmrInstTable,
       "cdsmrInstTableEntry": cdsmrInstTableEntry,
       "cdsmrInstLastChanged": cdsmrInstLastChanged,
       "cdsmrInstLastLoadTime": cdsmrInstLastLoadTime,
       "cdsmrInstLoadStatus": cdsmrInstLoadStatus,
       "cdsmrInstLastURL": cdsmrInstLastURL,
       "cdsmrInstDeliveredSmppCounts": cdsmrInstDeliveredSmppCounts,
       "cdsmrInstDeliveredUcpCounts": cdsmrInstDeliveredUcpCounts,
       "cdsmrInstDeliveredGsmCounts": cdsmrInstDeliveredGsmCounts,
       "cdsmrInstDeferredGsmCounts": cdsmrInstDeferredGsmCounts,
       "cdsmrInstGsmStatusReports": cdsmrInstGsmStatusReports,
       "cdsmrInstUcpNotifications": cdsmrInstUcpNotifications,
       "cdsmrInstSmppDeliveryReceipts": cdsmrInstSmppDeliveryReceipts,
       "cdsmrInstRoutingFailures": cdsmrInstRoutingFailures,
       "cdsmrInstResultFailures": cdsmrInstResultFailures,
       "cdsmrInstInternalErrors": cdsmrInstInternalErrors,
       "cdsmrInstParseErrors": cdsmrInstParseErrors,
       "cdsmrInstResourceErrors": cdsmrInstResourceErrors,
       "cdsmrInstProvisioningErrors": cdsmrInstProvisioningErrors,
       "cdsmrInstDestUnreachableErrors": cdsmrInstDestUnreachableErrors,
       "cdsmrInstDestSignalErrors": cdsmrInstDestSignalErrors,
       "cdsmrInstTimeOuts": cdsmrInstTimeOuts,
       "cdsmrInstBlockedPackets": cdsmrInstBlockedPackets,
       "cdsmrInstRoutingRequestsRcvdGsm": cdsmrInstRoutingRequestsRcvdGsm,
       "cdsmrInstRoutingRequestsRcvdIs41": cdsmrInstRoutingRequestsRcvdIs41,
       "cdsmrInstRoutingRequestsRcvdUcp": cdsmrInstRoutingRequestsRcvdUcp,
       "cdsmrInstRoutingRequestsRcvdSmpp": cdsmrInstRoutingRequestsRcvdSmpp,
       "cdsmrInstRowStatus": cdsmrInstRowStatus,
       "cdsmrResultGroupTable": cdsmrResultGroupTable,
       "cdsmrResultGroupTableEntry": cdsmrResultGroupTableEntry,
       "cdsmrResultGroupName": cdsmrResultGroupName,
       "cdsmrResultGroupServerType": cdsmrResultGroupServerType,
       "cdsmrResultGroupCdrConsolidation": cdsmrResultGroupCdrConsolidation,
       "cdsmrResultGroupIdentifier": cdsmrResultGroupIdentifier,
       "cdsmrResultGroupQueueLimit": cdsmrResultGroupQueueLimit,
       "cdsmrResultGroupQueueTimeLimit": cdsmrResultGroupQueueTimeLimit,
       "cdsmrResultGroupMatchSmppId": cdsmrResultGroupMatchSmppId,
       "cdsmrResultGroupMatchSmppType": cdsmrResultGroupMatchSmppType,
       "cdsmrResultGroupMatchUcpId": cdsmrResultGroupMatchUcpId,
       "cdsmrResultGroupRowStatus": cdsmrResultGroupRowStatus,
       "cdsmrResultIpTable": cdsmrResultIpTable,
       "cdsmrResultIpTableEntry": cdsmrResultIpTableEntry,
       "cdsmrResultIpNumber": cdsmrResultIpNumber,
       "cdsmrResultIpRemotePortNumber": cdsmrResultIpRemotePortNumber,
       "cdsmrResultIpRemoteIpAddrType": cdsmrResultIpRemoteIpAddrType,
       "cdsmrResultIpRemoteIpAddress": cdsmrResultIpRemoteIpAddress,
       "cdsmrResultIpProfileName": cdsmrResultIpProfileName,
       "cdsmrResultIpWeight": cdsmrResultIpWeight,
       "cdsmrResultIpRowStatus": cdsmrResultIpRowStatus,
       "cdsmrResultTable": cdsmrResultTable,
       "cdsmrResultTableEntry": cdsmrResultTableEntry,
       "cdsmrResultNumber": cdsmrResultNumber,
       "cdsmrResultDestinationType": cdsmrResultDestinationType,
       "cdsmrResultParameters": cdsmrResultParameters,
       "cdsmrResultDestinationName": cdsmrResultDestinationName,
       "cdsmrResultPc": cdsmrResultPc,
       "cdsmrResultSsn": cdsmrResultSsn,
       "cdsmrResultGt": cdsmrResultGt,
       "cdsmrResultTransType": cdsmrResultTransType,
       "cdsmrResultGti": cdsmrResultGti,
       "cdsmrResultNp": cdsmrResultNp,
       "cdsmrResultNai": cdsmrResultNai,
       "cdsmrResultWeight": cdsmrResultWeight,
       "cdsmrResultNetwork": cdsmrResultNetwork,
       "cdsmrResultCounts": cdsmrResultCounts,
       "cdsmrResultRowStatus": cdsmrResultRowStatus,
       "cdsmrAddressTable": cdsmrAddressTable,
       "cdsmrAddressTableEntry": cdsmrAddressTableEntry,
       "cdsmrAddressTableName": cdsmrAddressTableName,
       "cdsmrAddressType": cdsmrAddressType,
       "cdsmrAddressDigits": cdsmrAddressDigits,
       "cdsmrAddressExactMatch": cdsmrAddressExactMatch,
       "cdsmrAddressResultParameters": cdsmrAddressResultParameters,
       "cdsmrAddressResultNetwork": cdsmrAddressResultNetwork,
       "cdsmrAddressResultType": cdsmrAddressResultType,
       "cdsmrAddressResultOctet": cdsmrAddressResultOctet,
       "cdsmrAddressResultTransType": cdsmrAddressResultTransType,
       "cdsmrAddressResultGti": cdsmrAddressResultGti,
       "cdsmrAddressResultNp": cdsmrAddressResultNp,
       "cdsmrAddressResultNai": cdsmrAddressResultNai,
       "cdsmrAddressResultPc": cdsmrAddressResultPc,
       "cdsmrAddressResultSsn": cdsmrAddressResultSsn,
       "cdsmrAddressResultRuleNumber": cdsmrAddressResultRuleNumber,
       "cdsmrAddressMatchCounts": cdsmrAddressMatchCounts,
       "cdsmrAddressRowStatus": cdsmrAddressRowStatus,
       "cdsmrRuleSetTable": cdsmrRuleSetTable,
       "cdsmrRuleSetTableEntry": cdsmrRuleSetTableEntry,
       "cdsmrRuleSetName": cdsmrRuleSetName,
       "cdsmrRuleSetProtocol": cdsmrRuleSetProtocol,
       "cdsmrRuleSetStartDateAndTime": cdsmrRuleSetStartDateAndTime,
       "cdsmrRuleSetEndDateAndTime": cdsmrRuleSetEndDateAndTime,
       "cdsmrRuleSetRowStatus": cdsmrRuleSetRowStatus,
       "cdsmrRuleTable": cdsmrRuleTable,
       "cdsmrRuleTableEntry": cdsmrRuleTableEntry,
       "cdsmrRuleNumber": cdsmrRuleNumber,
       "cdsmrRuleOperationType": cdsmrRuleOperationType,
       "cdsmrRuleCdrServiceQueue": cdsmrRuleCdrServiceQueue,
       "cdsmrRuleInputParameters": cdsmrRuleInputParameters,
       "cdsmrRuleDestPort": cdsmrRuleDestPort,
       "cdsmrRuleDestSmeGta": cdsmrRuleDestSmeGta,
       "cdsmrRuleDestSmeNai": cdsmrRuleDestSmeNai,
       "cdsmrRuleDestSmeNp": cdsmrRuleDestSmeNp,
       "cdsmrRuleDestSmeMinDigits": cdsmrRuleDestSmeMinDigits,
       "cdsmrRuleDestSmeMaxDigits": cdsmrRuleDestSmeMaxDigits,
       "cdsmrRuleDestSmeTable": cdsmrRuleDestSmeTable,
       "cdsmrRuleDestSmeTableNai": cdsmrRuleDestSmeTableNai,
       "cdsmrRuleDestSmeTableNp": cdsmrRuleDestSmeTableNp,
       "cdsmrRuleDestSmscGta": cdsmrRuleDestSmscGta,
       "cdsmrRuleDestSmscNai": cdsmrRuleDestSmscNai,
       "cdsmrRuleDestSmscNp": cdsmrRuleDestSmscNp,
       "cdsmrRuleDestSmscMinDigits": cdsmrRuleDestSmscMinDigits,
       "cdsmrRuleDestSmscMaxDigits": cdsmrRuleDestSmscMaxDigits,
       "cdsmrRuleOrigImsiGta": cdsmrRuleOrigImsiGta,
       "cdsmrRuleOrigImsiNai": cdsmrRuleOrigImsiNai,
       "cdsmrRuleOrigImsiNp": cdsmrRuleOrigImsiNp,
       "cdsmrRuleOrigImsiMinDigits": cdsmrRuleOrigImsiMinDigits,
       "cdsmrRuleOrigImsiMaxDigits": cdsmrRuleOrigImsiMaxDigits,
       "cdsmrRuleOrigImsiTable": cdsmrRuleOrigImsiTable,
       "cdsmrRuleOrigSmeGta": cdsmrRuleOrigSmeGta,
       "cdsmrRuleOrigSmeNai": cdsmrRuleOrigSmeNai,
       "cdsmrRuleOrigSmeNp": cdsmrRuleOrigSmeNp,
       "cdsmrRuleOrigSmeMinDigits": cdsmrRuleOrigSmeMinDigits,
       "cdsmrRuleOrigSmeMaxDigits": cdsmrRuleOrigSmeMaxDigits,
       "cdsmrRuleOrigSmeTable": cdsmrRuleOrigSmeTable,
       "cdsmrRuleOrigSmeTableNai": cdsmrRuleOrigSmeTableNai,
       "cdsmrRuleOrigSmeTableNp": cdsmrRuleOrigSmeTableNp,
       "cdsmrRuleOrigSmscGta": cdsmrRuleOrigSmscGta,
       "cdsmrRuleOrigSmscNai": cdsmrRuleOrigSmscNai,
       "cdsmrRuleOrigSmscNp": cdsmrRuleOrigSmscNp,
       "cdsmrRuleOrigSmscMinDigits": cdsmrRuleOrigSmscMinDigits,
       "cdsmrRuleOrigSmscMaxDigits": cdsmrRuleOrigSmscMaxDigits,
       "cdsmrRuleOrigSmscTable": cdsmrRuleOrigSmscTable,
       "cdsmrRuleOrigSmscTableNai": cdsmrRuleOrigSmscTableNai,
       "cdsmrRuleOrigSmscTableNp": cdsmrRuleOrigSmscTableNp,
       "cdsmrRuleProtocolId": cdsmrRuleProtocolId,
       "cdsmrRuleTeleserviceId": cdsmrRuleTeleserviceId,
       "cdsmrRuleResultParameters": cdsmrRuleResultParameters,
       "cdsmrRuleResultNetwork": cdsmrRuleResultNetwork,
       "cdsmrRuleResultType": cdsmrRuleResultType,
       "cdsmrRuleResultOctet": cdsmrRuleResultOctet,
       "cdsmrRuleResultTransType": cdsmrRuleResultTransType,
       "cdsmrRuleResultGti": cdsmrRuleResultGti,
       "cdsmrRuleResultNp": cdsmrRuleResultNp,
       "cdsmrRuleResultNai": cdsmrRuleResultNai,
       "cdsmrRuleResultPc": cdsmrRuleResultPc,
       "cdsmrRuleResultSsn": cdsmrRuleResultSsn,
       "cdsmrRuleResultRuleNumber": cdsmrRuleResultRuleNumber,
       "cdsmrRuleResultRowStatus": cdsmrRuleResultRowStatus,
       "cdsmrRuleStatsTable": cdsmrRuleStatsTable,
       "cdsmrRuleStatsTableEntry": cdsmrRuleStatsTableEntry,
       "cdsmrRuleStatsCheckedCounts": cdsmrRuleStatsCheckedCounts,
       "cdsmrRuleStatsMatchCounts": cdsmrRuleStatsMatchCounts,
       "cdsmrRuleStatsRoutedCounts": cdsmrRuleStatsRoutedCounts,
       "ciscoItpDsmrMIBConform": ciscoItpDsmrMIBConform,
       "ciscoItpDsmrMIBCompliances": ciscoItpDsmrMIBCompliances,
       "ciscoItpDsmrMIBCompliance": ciscoItpDsmrMIBCompliance,
       "ciscoItpDsmrMIBGroups": ciscoItpDsmrMIBGroups,
       "ciscoItpDsmrInstanceGroup": ciscoItpDsmrInstanceGroup,
       "ciscoItpDsmrResultGroup": ciscoItpDsmrResultGroup,
       "ciscoItpDsmrAddressGroup": ciscoItpDsmrAddressGroup,
       "ciscoItpDsmrRulesGroup": ciscoItpDsmrRulesGroup,
       "ciscoItpDsmrNotificationsGroup": ciscoItpDsmrNotificationsGroup}
)
