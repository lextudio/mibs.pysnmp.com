# SNMP MIB module (CISCO-ITP-MLR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-MLR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:16 2024
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

(CItpTcGtaLongDisplay,
 CItpTcNAI,
 CItpTcNetworkName,
 CItpTcNumberingPlan,
 CItpTcPointCode,
 CItpTcPointCodeMask,
 CItpTcServiceIndicator,
 CItpTcSubSystemNumber,
 CItpTcTableLoadStatus,
 CItpTcURL) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcGtaLongDisplay",
    "CItpTcNAI",
    "CItpTcNetworkName",
    "CItpTcNumberingPlan",
    "CItpTcPointCode",
    "CItpTcPointCodeMask",
    "CItpTcServiceIndicator",
    "CItpTcSubSystemNumber",
    "CItpTcTableLoadStatus",
    "CItpTcURL")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoMlrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396)
)
ciscoMlrMIB.setRevisions(
        ("2004-09-22 00:00",
         "2004-04-14 00:00",
         "2004-03-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmlrAddressDigits(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CmlrAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bch", 1),
          ("gsmDa", 2))
    )



class CmlrId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CmlrName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class CmlrResultOctet(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
        ValueSizeConstraint(255, 255),
    )



class CmlrResultParameters(Bits, TextualConvention):
    status = "current"


class CmlrResultType(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("address", 9),
          ("asname", 2),
          ("block", 7),
          ("continue", 8),
          ("group", 3),
          ("gt", 4),
          ("none", 1),
          ("pc", 5),
          ("pcSsn", 6),
          ("ruleset", 10))
    )



class CmlrRuleProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi41", 3),
          ("gsmMap", 2),
          ("none", 1))
    )



class CmlrRuleSetName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class CmlrMinimumDigits(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class CmlrMaximumDigits(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMlrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMlrMIBNotifs = _CiscoMlrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 0)
)
_CiscoMlrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMlrMIBObjects = _CiscoMlrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1)
)
_CmlrScalars_ObjectIdentity = ObjectIdentity
cmlrScalars = _CmlrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 0)
)


class _CmlrTableLoadNotifEnabled_Type(TruthValue):
    """Custom type cmlrTableLoadNotifEnabled based on TruthValue"""


_CmlrTableLoadNotifEnabled_Object = MibScalar
cmlrTableLoadNotifEnabled = _CmlrTableLoadNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 0, 1),
    _CmlrTableLoadNotifEnabled_Type()
)
cmlrTableLoadNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmlrTableLoadNotifEnabled.setStatus("current")
_CmlrInstTable_Object = MibTable
cmlrInstTable = _CmlrInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1)
)
if mibBuilder.loadTexts:
    cmlrInstTable.setStatus("current")
_CmlrInstTableEntry_Object = MibTableRow
cmlrInstTableEntry = _CmlrInstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1)
)
cmlrInstTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cmlrInstTableEntry.setStatus("current")
_CmlrInstLastChanged_Type = TimeStamp
_CmlrInstLastChanged_Object = MibTableColumn
cmlrInstLastChanged = _CmlrInstLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 1),
    _CmlrInstLastChanged_Type()
)
cmlrInstLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstLastChanged.setStatus("current")
_CmlrInstLastLoadTime_Type = TimeStamp
_CmlrInstLastLoadTime_Object = MibTableColumn
cmlrInstLastLoadTime = _CmlrInstLastLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 2),
    _CmlrInstLastLoadTime_Type()
)
cmlrInstLastLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstLastLoadTime.setStatus("current")
_CmlrInstLoadStatus_Type = CItpTcTableLoadStatus
_CmlrInstLoadStatus_Object = MibTableColumn
cmlrInstLoadStatus = _CmlrInstLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 3),
    _CmlrInstLoadStatus_Type()
)
cmlrInstLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstLoadStatus.setStatus("current")
_CmlrInstLastURL_Type = CItpTcURL
_CmlrInstLastURL_Object = MibTableColumn
cmlrInstLastURL = _CmlrInstLastURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 4),
    _CmlrInstLastURL_Type()
)
cmlrInstLastURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstLastURL.setStatus("current")
_CmlrInstRoutedCounts_Type = Counter32
_CmlrInstRoutedCounts_Object = MibTableColumn
cmlrInstRoutedCounts = _CmlrInstRoutedCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 5),
    _CmlrInstRoutedCounts_Type()
)
cmlrInstRoutedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstRoutedCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstRoutedCounts.setUnits("packets")
_CmlrInstAbortCounts_Type = Counter32
_CmlrInstAbortCounts_Object = MibTableColumn
cmlrInstAbortCounts = _CmlrInstAbortCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 6),
    _CmlrInstAbortCounts_Type()
)
cmlrInstAbortCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstAbortCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstAbortCounts.setUnits("packets")
_CmlrInstContinueCounts_Type = Counter32
_CmlrInstContinueCounts_Object = MibTableColumn
cmlrInstContinueCounts = _CmlrInstContinueCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 7),
    _CmlrInstContinueCounts_Type()
)
cmlrInstContinueCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstContinueCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstContinueCounts.setUnits("packets")
_CmlrInstSmsMoCounts_Type = Counter32
_CmlrInstSmsMoCounts_Object = MibTableColumn
cmlrInstSmsMoCounts = _CmlrInstSmsMoCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 8),
    _CmlrInstSmsMoCounts_Type()
)
cmlrInstSmsMoCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSmsMoCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSmsMoCounts.setUnits("packets")
_CmlrInstSmsMtCounts_Type = Counter32
_CmlrInstSmsMtCounts_Object = MibTableColumn
cmlrInstSmsMtCounts = _CmlrInstSmsMtCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 9),
    _CmlrInstSmsMtCounts_Type()
)
cmlrInstSmsMtCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSmsMtCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSmsMtCounts.setUnits("packets")
_CmlrInstSriSmCounts_Type = Counter32
_CmlrInstSriSmCounts_Object = MibTableColumn
cmlrInstSriSmCounts = _CmlrInstSriSmCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 10),
    _CmlrInstSriSmCounts_Type()
)
cmlrInstSriSmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSriSmCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSriSmCounts.setUnits("packets")
_CmlrInstSmdPpCounts_Type = Counter32
_CmlrInstSmdPpCounts_Object = MibTableColumn
cmlrInstSmdPpCounts = _CmlrInstSmdPpCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 11),
    _CmlrInstSmdPpCounts_Type()
)
cmlrInstSmdPpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSmdPpCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSmdPpCounts.setUnits("packets")
_CmlrInstAlertScCounts_Type = Counter32
_CmlrInstAlertScCounts_Object = MibTableColumn
cmlrInstAlertScCounts = _CmlrInstAlertScCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 12),
    _CmlrInstAlertScCounts_Type()
)
cmlrInstAlertScCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstAlertScCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstAlertScCounts.setUnits("packets")
_CmlrInstSmsRequestCounts_Type = Counter32
_CmlrInstSmsRequestCounts_Object = MibTableColumn
cmlrInstSmsRequestCounts = _CmlrInstSmsRequestCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 13),
    _CmlrInstSmsRequestCounts_Type()
)
cmlrInstSmsRequestCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSmsRequestCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSmsRequestCounts.setUnits("packets")
_CmlrInstSmsNotifCounts_Type = Counter32
_CmlrInstSmsNotifCounts_Object = MibTableColumn
cmlrInstSmsNotifCounts = _CmlrInstSmsNotifCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 14),
    _CmlrInstSmsNotifCounts_Type()
)
cmlrInstSmsNotifCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstSmsNotifCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstSmsNotifCounts.setUnits("packets")
_CmlrInstUnsupSCCPmsgTypeCounts_Type = Counter32
_CmlrInstUnsupSCCPmsgTypeCounts_Object = MibTableColumn
cmlrInstUnsupSCCPmsgTypeCounts = _CmlrInstUnsupSCCPmsgTypeCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 15),
    _CmlrInstUnsupSCCPmsgTypeCounts_Type()
)
cmlrInstUnsupSCCPmsgTypeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstUnsupSCCPmsgTypeCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstUnsupSCCPmsgTypeCounts.setUnits("packets")
_CmlrInstUnsupSegSCCPmsgCounts_Type = Counter32
_CmlrInstUnsupSegSCCPmsgCounts_Object = MibTableColumn
cmlrInstUnsupSegSCCPmsgCounts = _CmlrInstUnsupSegSCCPmsgCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 16),
    _CmlrInstUnsupSegSCCPmsgCounts_Type()
)
cmlrInstUnsupSegSCCPmsgCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstUnsupSegSCCPmsgCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstUnsupSegSCCPmsgCounts.setUnits("packets")
_CmlrInstUnsupportedMsgCounts_Type = Counter32
_CmlrInstUnsupportedMsgCounts_Object = MibTableColumn
cmlrInstUnsupportedMsgCounts = _CmlrInstUnsupportedMsgCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 17),
    _CmlrInstUnsupportedMsgCounts_Type()
)
cmlrInstUnsupportedMsgCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstUnsupportedMsgCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstUnsupportedMsgCounts.setUnits("packets")
_CmlrInstParsingErrorCounts_Type = Counter32
_CmlrInstParsingErrorCounts_Object = MibTableColumn
cmlrInstParsingErrorCounts = _CmlrInstParsingErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 18),
    _CmlrInstParsingErrorCounts_Type()
)
cmlrInstParsingErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstParsingErrorCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstParsingErrorCounts.setUnits("packets")
_CmlrInstNoResultCounts_Type = Counter32
_CmlrInstNoResultCounts_Object = MibTableColumn
cmlrInstNoResultCounts = _CmlrInstNoResultCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 19),
    _CmlrInstNoResultCounts_Type()
)
cmlrInstNoResultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstNoResultCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstNoResultCounts.setUnits("packets")
_CmlrInstResultContinueCounts_Type = Counter32
_CmlrInstResultContinueCounts_Object = MibTableColumn
cmlrInstResultContinueCounts = _CmlrInstResultContinueCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 20),
    _CmlrInstResultContinueCounts_Type()
)
cmlrInstResultContinueCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultContinueCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultContinueCounts.setUnits("packets")
_CmlrInstNoServerDiscardCounts_Type = Counter32
_CmlrInstNoServerDiscardCounts_Object = MibTableColumn
cmlrInstNoServerDiscardCounts = _CmlrInstNoServerDiscardCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 21),
    _CmlrInstNoServerDiscardCounts_Type()
)
cmlrInstNoServerDiscardCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstNoServerDiscardCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstNoServerDiscardCounts.setUnits("packets")
_CmlrInstResultGttCounts_Type = Counter32
_CmlrInstResultGttCounts_Object = MibTableColumn
cmlrInstResultGttCounts = _CmlrInstResultGttCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 22),
    _CmlrInstResultGttCounts_Type()
)
cmlrInstResultGttCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultGttCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultGttCounts.setUnits("packets")
_CmlrInstUnparsedCounts_Type = Counter32
_CmlrInstUnparsedCounts_Object = MibTableColumn
cmlrInstUnparsedCounts = _CmlrInstUnparsedCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 23),
    _CmlrInstUnparsedCounts_Type()
)
cmlrInstUnparsedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstUnparsedCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstUnparsedCounts.setUnits("packets")
_CmlrInstResultBlockCounts_Type = Counter32
_CmlrInstResultBlockCounts_Object = MibTableColumn
cmlrInstResultBlockCounts = _CmlrInstResultBlockCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 24),
    _CmlrInstResultBlockCounts_Type()
)
cmlrInstResultBlockCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultBlockCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultBlockCounts.setUnits("packets")
_CmlrInstGTImismatchCounts_Type = Counter32
_CmlrInstGTImismatchCounts_Object = MibTableColumn
cmlrInstGTImismatchCounts = _CmlrInstGTImismatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 25),
    _CmlrInstGTImismatchCounts_Type()
)
cmlrInstGTImismatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstGTImismatchCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstGTImismatchCounts.setUnits("packets")
_CmlrInstAddrConvFailureCounts_Type = Counter32
_CmlrInstAddrConvFailureCounts_Object = MibTableColumn
cmlrInstAddrConvFailureCounts = _CmlrInstAddrConvFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 26),
    _CmlrInstAddrConvFailureCounts_Type()
)
cmlrInstAddrConvFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstAddrConvFailureCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstAddrConvFailureCounts.setUnits("packets")
_CmlrInstDestUnavailableCounts_Type = Counter32
_CmlrInstDestUnavailableCounts_Object = MibTableColumn
cmlrInstDestUnavailableCounts = _CmlrInstDestUnavailableCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 27),
    _CmlrInstDestUnavailableCounts_Type()
)
cmlrInstDestUnavailableCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstDestUnavailableCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstDestUnavailableCounts.setUnits("packets")
_CmlrInstFailedTrigMatchCounts_Type = Counter32
_CmlrInstFailedTrigMatchCounts_Object = MibTableColumn
cmlrInstFailedTrigMatchCounts = _CmlrInstFailedTrigMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 28),
    _CmlrInstFailedTrigMatchCounts_Type()
)
cmlrInstFailedTrigMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstFailedTrigMatchCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstFailedTrigMatchCounts.setUnits("packets")
_CmlrInstDiscontinuityTime_Type = TimeStamp
_CmlrInstDiscontinuityTime_Object = MibTableColumn
cmlrInstDiscontinuityTime = _CmlrInstDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 29),
    _CmlrInstDiscontinuityTime_Type()
)
cmlrInstDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstDiscontinuityTime.setStatus("current")
_CmlrInstNoServerContinueCounts_Type = Counter32
_CmlrInstNoServerContinueCounts_Object = MibTableColumn
cmlrInstNoServerContinueCounts = _CmlrInstNoServerContinueCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 30),
    _CmlrInstNoServerContinueCounts_Type()
)
cmlrInstNoServerContinueCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstNoServerContinueCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstNoServerContinueCounts.setUnits("packets")
_CmlrInstResultAsCounts_Type = Counter32
_CmlrInstResultAsCounts_Object = MibTableColumn
cmlrInstResultAsCounts = _CmlrInstResultAsCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 31),
    _CmlrInstResultAsCounts_Type()
)
cmlrInstResultAsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultAsCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultAsCounts.setUnits("packets")
_CmlrInstResultPcCounts_Type = Counter32
_CmlrInstResultPcCounts_Object = MibTableColumn
cmlrInstResultPcCounts = _CmlrInstResultPcCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 32),
    _CmlrInstResultPcCounts_Type()
)
cmlrInstResultPcCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultPcCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultPcCounts.setUnits("packets")
_CmlrInstResultPcSsnCounts_Type = Counter32
_CmlrInstResultPcSsnCounts_Object = MibTableColumn
cmlrInstResultPcSsnCounts = _CmlrInstResultPcSsnCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 1, 1, 33),
    _CmlrInstResultPcSsnCounts_Type()
)
cmlrInstResultPcSsnCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrInstResultPcSsnCounts.setStatus("current")
if mibBuilder.loadTexts:
    cmlrInstResultPcSsnCounts.setUnits("packets")
_CmlrTriggerTable_Object = MibTable
cmlrTriggerTable = _CmlrTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2)
)
if mibBuilder.loadTexts:
    cmlrTriggerTable.setStatus("current")
_CmlrTriggerTableEntry_Object = MibTableRow
cmlrTriggerTableEntry = _CmlrTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1)
)
cmlrTriggerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrTableName"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrTriggerNumber"),
)
if mibBuilder.loadTexts:
    cmlrTriggerTableEntry.setStatus("current")
_CmlrTableName_Type = CmlrName
_CmlrTableName_Object = MibTableColumn
cmlrTableName = _CmlrTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 1),
    _CmlrTableName_Type()
)
cmlrTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrTableName.setStatus("current")
_CmlrTriggerNumber_Type = CmlrId
_CmlrTriggerNumber_Object = MibTableColumn
cmlrTriggerNumber = _CmlrTriggerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 2),
    _CmlrTriggerNumber_Type()
)
cmlrTriggerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrTriggerNumber.setStatus("current")


class _CmlrTriggerParameters_Type(Bits):
    """Custom type cmlrTriggerParameters based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("block", 0),
          ("cdpa", 3),
          ("cgpa", 4),
          ("continue", 1),
          ("dpc", 15),
          ("gt", 6),
          ("gti", 8),
          ("matchAll", 2),
          ("nai", 10),
          ("network", 13),
          ("np", 9),
          ("opc", 16),
          ("opcMask", 17),
          ("pc", 5),
          ("pid", 12),
          ("ruleset", 14),
          ("si", 18),
          ("ssn", 11),
          ("tt", 7))
    )

_CmlrTriggerParameters_Type.__name__ = "Bits"
_CmlrTriggerParameters_Object = MibTableColumn
cmlrTriggerParameters = _CmlrTriggerParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 3),
    _CmlrTriggerParameters_Type()
)
cmlrTriggerParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerParameters.setStatus("current")


class _CmlrTriggerGt_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrTriggerGt based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrTriggerGt_Object = MibTableColumn
cmlrTriggerGt = _CmlrTriggerGt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 4),
    _CmlrTriggerGt_Type()
)
cmlrTriggerGt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerGt.setStatus("current")


class _CmlrTriggerTransType_Type(CgsccpGttTransType):
    """Custom type cmlrTriggerTransType based on CgsccpGttTransType"""
    defaultValue = 0


_CmlrTriggerTransType_Object = MibTableColumn
cmlrTriggerTransType = _CmlrTriggerTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 5),
    _CmlrTriggerTransType_Type()
)
cmlrTriggerTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerTransType.setStatus("current")


class _CmlrTriggerGti_Type(CgsccpGttGlobalTitleInd):
    """Custom type cmlrTriggerGti based on CgsccpGttGlobalTitleInd"""
    defaultValue = 0


_CmlrTriggerGti_Object = MibTableColumn
cmlrTriggerGti = _CmlrTriggerGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 6),
    _CmlrTriggerGti_Type()
)
cmlrTriggerGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerGti.setStatus("current")


class _CmlrTriggerNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrTriggerNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrTriggerNp_Object = MibTableColumn
cmlrTriggerNp = _CmlrTriggerNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 7),
    _CmlrTriggerNp_Type()
)
cmlrTriggerNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerNp.setStatus("current")


class _CmlrTriggerNai_Type(CItpTcNAI):
    """Custom type cmlrTriggerNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrTriggerNai_Object = MibTableColumn
cmlrTriggerNai = _CmlrTriggerNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 8),
    _CmlrTriggerNai_Type()
)
cmlrTriggerNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerNai.setStatus("current")


class _CmlrTriggerPc_Type(CItpTcPointCode):
    """Custom type cmlrTriggerPc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrTriggerPc_Object = MibTableColumn
cmlrTriggerPc = _CmlrTriggerPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 9),
    _CmlrTriggerPc_Type()
)
cmlrTriggerPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerPc.setStatus("current")


class _CmlrTriggerSsn_Type(CItpTcSubSystemNumber):
    """Custom type cmlrTriggerSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CmlrTriggerSsn_Object = MibTableColumn
cmlrTriggerSsn = _CmlrTriggerSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 10),
    _CmlrTriggerSsn_Type()
)
cmlrTriggerSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerSsn.setStatus("current")


class _CmlrTriggerDpc_Type(CItpTcPointCode):
    """Custom type cmlrTriggerDpc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrTriggerDpc_Object = MibTableColumn
cmlrTriggerDpc = _CmlrTriggerDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 11),
    _CmlrTriggerDpc_Type()
)
cmlrTriggerDpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerDpc.setStatus("current")


class _CmlrTriggerOpc_Type(CItpTcPointCode):
    """Custom type cmlrTriggerOpc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrTriggerOpc_Object = MibTableColumn
cmlrTriggerOpc = _CmlrTriggerOpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 12),
    _CmlrTriggerOpc_Type()
)
cmlrTriggerOpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerOpc.setStatus("current")


class _CmlrTriggerOpcMask_Type(CItpTcPointCodeMask):
    """Custom type cmlrTriggerOpcMask based on CItpTcPointCodeMask"""
    defaultValue = 0


_CmlrTriggerOpcMask_Object = MibTableColumn
cmlrTriggerOpcMask = _CmlrTriggerOpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 13),
    _CmlrTriggerOpcMask_Type()
)
cmlrTriggerOpcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerOpcMask.setStatus("current")


class _CmlrTriggerSi_Type(CItpTcServiceIndicator):
    """Custom type cmlrTriggerSi based on CItpTcServiceIndicator"""


_CmlrTriggerSi_Object = MibTableColumn
cmlrTriggerSi = _CmlrTriggerSi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 14),
    _CmlrTriggerSi_Type()
)
cmlrTriggerSi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerSi.setStatus("current")


class _CmlrTriggerNetwork_Type(CItpTcNetworkName):
    """Custom type cmlrTriggerNetwork based on CItpTcNetworkName"""
    defaultHexValue = ""


_CmlrTriggerNetwork_Object = MibTableColumn
cmlrTriggerNetwork = _CmlrTriggerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 15),
    _CmlrTriggerNetwork_Type()
)
cmlrTriggerNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerNetwork.setStatus("current")


class _CmlrTriggerRuleset_Type(CmlrRuleSetName):
    """Custom type cmlrTriggerRuleset based on CmlrRuleSetName"""
    defaultHexValue = ""


_CmlrTriggerRuleset_Object = MibTableColumn
cmlrTriggerRuleset = _CmlrTriggerRuleset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 16),
    _CmlrTriggerRuleset_Type()
)
cmlrTriggerRuleset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerRuleset.setStatus("current")
_CmlrTriggerActive_Type = TruthValue
_CmlrTriggerActive_Object = MibTableColumn
cmlrTriggerActive = _CmlrTriggerActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 17),
    _CmlrTriggerActive_Type()
)
cmlrTriggerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrTriggerActive.setStatus("current")


class _CmlrTriggerStartDateAndTime_Type(DateAndTime):
    """Custom type cmlrTriggerStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CmlrTriggerStartDateAndTime_Object = MibTableColumn
cmlrTriggerStartDateAndTime = _CmlrTriggerStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 18),
    _CmlrTriggerStartDateAndTime_Type()
)
cmlrTriggerStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerStartDateAndTime.setStatus("current")


class _CmlrTriggerEndDateAndTime_Type(DateAndTime):
    """Custom type cmlrTriggerEndDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CmlrTriggerEndDateAndTime_Object = MibTableColumn
cmlrTriggerEndDateAndTime = _CmlrTriggerEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 19),
    _CmlrTriggerEndDateAndTime_Type()
)
cmlrTriggerEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerEndDateAndTime.setStatus("current")
_CmlTriggerPreliminaryMatchCounts_Type = Counter32
_CmlTriggerPreliminaryMatchCounts_Object = MibTableColumn
cmlTriggerPreliminaryMatchCounts = _CmlTriggerPreliminaryMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 20),
    _CmlTriggerPreliminaryMatchCounts_Type()
)
cmlTriggerPreliminaryMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlTriggerPreliminaryMatchCounts.setStatus("current")
_CmlrTriggerMatchCounts_Type = Counter32
_CmlrTriggerMatchCounts_Object = MibTableColumn
cmlrTriggerMatchCounts = _CmlrTriggerMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 21),
    _CmlrTriggerMatchCounts_Type()
)
cmlrTriggerMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrTriggerMatchCounts.setStatus("current")
_CmlrTriggerRowStatus_Type = RowStatus
_CmlrTriggerRowStatus_Object = MibTableColumn
cmlrTriggerRowStatus = _CmlrTriggerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 2, 1, 22),
    _CmlrTriggerRowStatus_Type()
)
cmlrTriggerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrTriggerRowStatus.setStatus("current")
_CmlrSubTriggerTable_Object = MibTable
cmlrSubTriggerTable = _CmlrSubTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3)
)
if mibBuilder.loadTexts:
    cmlrSubTriggerTable.setStatus("current")
_CmlrSubTriggerTableEntry_Object = MibTableRow
cmlrSubTriggerTableEntry = _CmlrSubTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1)
)
cmlrSubTriggerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrTableName"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrTriggerNumber"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrSubTriggerNumber"),
)
if mibBuilder.loadTexts:
    cmlrSubTriggerTableEntry.setStatus("current")
_CmlrSubTriggerNumber_Type = CmlrId
_CmlrSubTriggerNumber_Object = MibTableColumn
cmlrSubTriggerNumber = _CmlrSubTriggerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 1),
    _CmlrSubTriggerNumber_Type()
)
cmlrSubTriggerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrSubTriggerNumber.setStatus("current")


class _CmlrSubTriggerParameters_Type(Bits):
    """Custom type cmlrSubTriggerParameters based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("block", 0),
          ("cdpa", 3),
          ("cgpa", 4),
          ("continue", 1),
          ("gt", 6),
          ("gti", 8),
          ("matchAll", 2),
          ("nai", 10),
          ("network", 13),
          ("np", 9),
          ("pc", 5),
          ("pid", 12),
          ("ruleset", 14),
          ("ssn", 11),
          ("tt", 7))
    )

_CmlrSubTriggerParameters_Type.__name__ = "Bits"
_CmlrSubTriggerParameters_Object = MibTableColumn
cmlrSubTriggerParameters = _CmlrSubTriggerParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 2),
    _CmlrSubTriggerParameters_Type()
)
cmlrSubTriggerParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerParameters.setStatus("current")


class _CmlrSubTriggerGt_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrSubTriggerGt based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrSubTriggerGt_Object = MibTableColumn
cmlrSubTriggerGt = _CmlrSubTriggerGt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 4),
    _CmlrSubTriggerGt_Type()
)
cmlrSubTriggerGt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerGt.setStatus("current")


class _CmlrSubTriggerTransType_Type(CgsccpGttTransType):
    """Custom type cmlrSubTriggerTransType based on CgsccpGttTransType"""
    defaultValue = 0


_CmlrSubTriggerTransType_Object = MibTableColumn
cmlrSubTriggerTransType = _CmlrSubTriggerTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 5),
    _CmlrSubTriggerTransType_Type()
)
cmlrSubTriggerTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerTransType.setStatus("current")


class _CmlrSubTriggerGti_Type(CgsccpGttGlobalTitleInd):
    """Custom type cmlrSubTriggerGti based on CgsccpGttGlobalTitleInd"""
    defaultValue = 0


_CmlrSubTriggerGti_Object = MibTableColumn
cmlrSubTriggerGti = _CmlrSubTriggerGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 6),
    _CmlrSubTriggerGti_Type()
)
cmlrSubTriggerGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerGti.setStatus("current")


class _CmlrSubTriggerNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrSubTriggerNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrSubTriggerNp_Object = MibTableColumn
cmlrSubTriggerNp = _CmlrSubTriggerNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 7),
    _CmlrSubTriggerNp_Type()
)
cmlrSubTriggerNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerNp.setStatus("current")


class _CmlrSubTriggerNai_Type(CItpTcNAI):
    """Custom type cmlrSubTriggerNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrSubTriggerNai_Object = MibTableColumn
cmlrSubTriggerNai = _CmlrSubTriggerNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 8),
    _CmlrSubTriggerNai_Type()
)
cmlrSubTriggerNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerNai.setStatus("current")


class _CmlrSubTriggerPc_Type(CItpTcPointCode):
    """Custom type cmlrSubTriggerPc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrSubTriggerPc_Object = MibTableColumn
cmlrSubTriggerPc = _CmlrSubTriggerPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 9),
    _CmlrSubTriggerPc_Type()
)
cmlrSubTriggerPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerPc.setStatus("current")


class _CmlrSubTriggerSsn_Type(CItpTcSubSystemNumber):
    """Custom type cmlrSubTriggerSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CmlrSubTriggerSsn_Object = MibTableColumn
cmlrSubTriggerSsn = _CmlrSubTriggerSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 10),
    _CmlrSubTriggerSsn_Type()
)
cmlrSubTriggerSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerSsn.setStatus("current")


class _CmlrSubTriggerNetwork_Type(CItpTcNetworkName):
    """Custom type cmlrSubTriggerNetwork based on CItpTcNetworkName"""
    defaultHexValue = ""


_CmlrSubTriggerNetwork_Object = MibTableColumn
cmlrSubTriggerNetwork = _CmlrSubTriggerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 11),
    _CmlrSubTriggerNetwork_Type()
)
cmlrSubTriggerNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerNetwork.setStatus("current")


class _CmlrSubTriggerRuleset_Type(CmlrRuleSetName):
    """Custom type cmlrSubTriggerRuleset based on CmlrRuleSetName"""
    defaultHexValue = ""


_CmlrSubTriggerRuleset_Object = MibTableColumn
cmlrSubTriggerRuleset = _CmlrSubTriggerRuleset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 12),
    _CmlrSubTriggerRuleset_Type()
)
cmlrSubTriggerRuleset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerRuleset.setStatus("current")
_CmlrSubTriggerMatchCounts_Type = Counter32
_CmlrSubTriggerMatchCounts_Object = MibTableColumn
cmlrSubTriggerMatchCounts = _CmlrSubTriggerMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 13),
    _CmlrSubTriggerMatchCounts_Type()
)
cmlrSubTriggerMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrSubTriggerMatchCounts.setStatus("current")
_CmlrSubTriggerRowStatus_Type = RowStatus
_CmlrSubTriggerRowStatus_Object = MibTableColumn
cmlrSubTriggerRowStatus = _CmlrSubTriggerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 3, 1, 14),
    _CmlrSubTriggerRowStatus_Type()
)
cmlrSubTriggerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrSubTriggerRowStatus.setStatus("current")
_CmlrAddressTable_Object = MibTable
cmlrAddressTable = _CmlrAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4)
)
if mibBuilder.loadTexts:
    cmlrAddressTable.setStatus("current")
_CmlrAddressTableEntry_Object = MibTableRow
cmlrAddressTableEntry = _CmlrAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1)
)
cmlrAddressTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrAddressTableName"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrAddressType"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrAddressDigits"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrAddressExactMatch"),
)
if mibBuilder.loadTexts:
    cmlrAddressTableEntry.setStatus("current")
_CmlrAddressTableName_Type = CmlrName
_CmlrAddressTableName_Object = MibTableColumn
cmlrAddressTableName = _CmlrAddressTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 1),
    _CmlrAddressTableName_Type()
)
cmlrAddressTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrAddressTableName.setStatus("current")
_CmlrAddressType_Type = CmlrAddressType
_CmlrAddressType_Object = MibTableColumn
cmlrAddressType = _CmlrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 2),
    _CmlrAddressType_Type()
)
cmlrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrAddressType.setStatus("current")
_CmlrAddressDigits_Type = CmlrAddressDigits
_CmlrAddressDigits_Object = MibTableColumn
cmlrAddressDigits = _CmlrAddressDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 3),
    _CmlrAddressDigits_Type()
)
cmlrAddressDigits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrAddressDigits.setStatus("current")
_CmlrAddressExactMatch_Type = TruthValue
_CmlrAddressExactMatch_Object = MibTableColumn
cmlrAddressExactMatch = _CmlrAddressExactMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 4),
    _CmlrAddressExactMatch_Type()
)
cmlrAddressExactMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrAddressExactMatch.setStatus("current")


class _CmlrAddressResultParameters_Type(CmlrResultParameters):
    """Custom type cmlrAddressResultParameters based on CmlrResultParameters"""
    defaultBinValue = "0"


_CmlrAddressResultParameters_Object = MibTableColumn
cmlrAddressResultParameters = _CmlrAddressResultParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 5),
    _CmlrAddressResultParameters_Type()
)
cmlrAddressResultParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultParameters.setStatus("current")
_CmlrAddressResultNetwork_Type = CItpTcNetworkName
_CmlrAddressResultNetwork_Object = MibTableColumn
cmlrAddressResultNetwork = _CmlrAddressResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 6),
    _CmlrAddressResultNetwork_Type()
)
cmlrAddressResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultNetwork.setStatus("current")


class _CmlrAddressResultType_Type(CmlrResultType):
    """Custom type cmlrAddressResultType based on CmlrResultType"""


_CmlrAddressResultType_Object = MibTableColumn
cmlrAddressResultType = _CmlrAddressResultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 7),
    _CmlrAddressResultType_Type()
)
cmlrAddressResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultType.setStatus("current")


class _CmlrAddressResultOctet_Type(CmlrResultOctet):
    """Custom type cmlrAddressResultOctet based on CmlrResultOctet"""
    defaultHexValue = ""


_CmlrAddressResultOctet_Object = MibTableColumn
cmlrAddressResultOctet = _CmlrAddressResultOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 8),
    _CmlrAddressResultOctet_Type()
)
cmlrAddressResultOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultOctet.setStatus("current")


class _CmlrAddressResultTransType_Type(CgsccpGttTransType):
    """Custom type cmlrAddressResultTransType based on CgsccpGttTransType"""
    defaultValue = 0


_CmlrAddressResultTransType_Object = MibTableColumn
cmlrAddressResultTransType = _CmlrAddressResultTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 9),
    _CmlrAddressResultTransType_Type()
)
cmlrAddressResultTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultTransType.setStatus("current")


class _CmlrAddressResultGti_Type(CgsccpGttGlobalTitleInd):
    """Custom type cmlrAddressResultGti based on CgsccpGttGlobalTitleInd"""
    defaultValue = 0


_CmlrAddressResultGti_Object = MibTableColumn
cmlrAddressResultGti = _CmlrAddressResultGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 10),
    _CmlrAddressResultGti_Type()
)
cmlrAddressResultGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultGti.setStatus("current")


class _CmlrAddressResultNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrAddressResultNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrAddressResultNp_Object = MibTableColumn
cmlrAddressResultNp = _CmlrAddressResultNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 11),
    _CmlrAddressResultNp_Type()
)
cmlrAddressResultNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultNp.setStatus("current")


class _CmlrAddressResultNai_Type(CItpTcNAI):
    """Custom type cmlrAddressResultNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrAddressResultNai_Object = MibTableColumn
cmlrAddressResultNai = _CmlrAddressResultNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 12),
    _CmlrAddressResultNai_Type()
)
cmlrAddressResultNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultNai.setStatus("current")


class _CmlrAddressResultPc_Type(CItpTcPointCode):
    """Custom type cmlrAddressResultPc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrAddressResultPc_Object = MibTableColumn
cmlrAddressResultPc = _CmlrAddressResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 13),
    _CmlrAddressResultPc_Type()
)
cmlrAddressResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultPc.setStatus("current")


class _CmlrAddressResultSsn_Type(CItpTcSubSystemNumber):
    """Custom type cmlrAddressResultSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CmlrAddressResultSsn_Object = MibTableColumn
cmlrAddressResultSsn = _CmlrAddressResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 14),
    _CmlrAddressResultSsn_Type()
)
cmlrAddressResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressResultSsn.setStatus("current")
_CmlrAddressMatchCounts_Type = Counter32
_CmlrAddressMatchCounts_Object = MibTableColumn
cmlrAddressMatchCounts = _CmlrAddressMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 15),
    _CmlrAddressMatchCounts_Type()
)
cmlrAddressMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrAddressMatchCounts.setStatus("current")
_CmlrAddressRowStatus_Type = RowStatus
_CmlrAddressRowStatus_Object = MibTableColumn
cmlrAddressRowStatus = _CmlrAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 4, 1, 16),
    _CmlrAddressRowStatus_Type()
)
cmlrAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrAddressRowStatus.setStatus("current")
_CmlrRuleSetTable_Object = MibTable
cmlrRuleSetTable = _CmlrRuleSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5)
)
if mibBuilder.loadTexts:
    cmlrRuleSetTable.setStatus("current")
_CmlrRuleSetTableEntry_Object = MibTableRow
cmlrRuleSetTableEntry = _CmlrRuleSetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1)
)
cmlrRuleSetTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrRuleSetName"),
)
if mibBuilder.loadTexts:
    cmlrRuleSetTableEntry.setStatus("current")
_CmlrRuleSetName_Type = CmlrRuleSetName
_CmlrRuleSetName_Object = MibTableColumn
cmlrRuleSetName = _CmlrRuleSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 1),
    _CmlrRuleSetName_Type()
)
cmlrRuleSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrRuleSetName.setStatus("current")


class _CmlrRuleSetSegmented_Type(TruthValue):
    """Custom type cmlrRuleSetSegmented based on TruthValue"""


_CmlrRuleSetSegmented_Object = MibTableColumn
cmlrRuleSetSegmented = _CmlrRuleSetSegmented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 2),
    _CmlrRuleSetSegmented_Type()
)
cmlrRuleSetSegmented.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetSegmented.setStatus("current")


class _CmlrRuleSetProtocol_Type(CmlrRuleProtocol):
    """Custom type cmlrRuleSetProtocol based on CmlrRuleProtocol"""


_CmlrRuleSetProtocol_Object = MibTableColumn
cmlrRuleSetProtocol = _CmlrRuleSetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 3),
    _CmlrRuleSetProtocol_Type()
)
cmlrRuleSetProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetProtocol.setStatus("current")


class _CmlrRuleSetSearchType_Type(Integer32):
    """Custom type cmlrRuleSetSearchType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestMatch", 2),
          ("seq", 1))
    )


_CmlrRuleSetSearchType_Type.__name__ = "Integer32"
_CmlrRuleSetSearchType_Object = MibTableColumn
cmlrRuleSetSearchType = _CmlrRuleSetSearchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 4),
    _CmlrRuleSetSearchType_Type()
)
cmlrRuleSetSearchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetSearchType.setStatus("current")


class _CmlrRuleSetStartDateAndTime_Type(DateAndTime):
    """Custom type cmlrRuleSetStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CmlrRuleSetStartDateAndTime_Object = MibTableColumn
cmlrRuleSetStartDateAndTime = _CmlrRuleSetStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 5),
    _CmlrRuleSetStartDateAndTime_Type()
)
cmlrRuleSetStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetStartDateAndTime.setStatus("current")


class _CmlrRuleSetEndDateAndTime_Type(DateAndTime):
    """Custom type cmlrRuleSetEndDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CmlrRuleSetEndDateAndTime_Object = MibTableColumn
cmlrRuleSetEndDateAndTime = _CmlrRuleSetEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 6),
    _CmlrRuleSetEndDateAndTime_Type()
)
cmlrRuleSetEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetEndDateAndTime.setStatus("current")
_CmlrRuleSetRowStatus_Type = RowStatus
_CmlrRuleSetRowStatus_Object = MibTableColumn
cmlrRuleSetRowStatus = _CmlrRuleSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 5, 1, 7),
    _CmlrRuleSetRowStatus_Type()
)
cmlrRuleSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleSetRowStatus.setStatus("current")
_CmlrRuleTable_Object = MibTable
cmlrRuleTable = _CmlrRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6)
)
if mibBuilder.loadTexts:
    cmlrRuleTable.setStatus("current")
_CmlrRuleTableEntry_Object = MibTableRow
cmlrRuleTableEntry = _CmlrRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1)
)
cmlrRuleTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrRuleSetName"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrRuleNumber"),
)
if mibBuilder.loadTexts:
    cmlrRuleTableEntry.setStatus("current")
_CmlrRuleNumber_Type = CmlrId
_CmlrRuleNumber_Object = MibTableColumn
cmlrRuleNumber = _CmlrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 1),
    _CmlrRuleNumber_Type()
)
cmlrRuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrRuleNumber.setStatus("current")


class _CmlrRuleOperationType_Type(Integer32):
    """Custom type cmlrRuleOperationType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("alertSc", 1),
          ("all", 255),
          ("smdPp", 2),
          ("smsMo", 3),
          ("smsMt", 4),
          ("smsNotify", 7),
          ("smsReg", 5),
          ("sriSm", 6),
          ("unknown", 0))
    )


_CmlrRuleOperationType_Type.__name__ = "Integer32"
_CmlrRuleOperationType_Object = MibTableColumn
cmlrRuleOperationType = _CmlrRuleOperationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 2),
    _CmlrRuleOperationType_Type()
)
cmlrRuleOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOperationType.setStatus("current")
_CmlrRuleProtocol_Type = CmlrRuleProtocol
_CmlrRuleProtocol_Object = MibTableColumn
cmlrRuleProtocol = _CmlrRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 3),
    _CmlrRuleProtocol_Type()
)
cmlrRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleProtocol.setStatus("current")


class _CmlrRuleInputParameters_Type(Bits):
    """Custom type cmlrRuleInputParameters based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("default", 21),
          ("destPort", 0),
          ("destSmeExact", 2),
          ("destSmeGta", 1),
          ("destSmeImsi", 5),
          ("destSmeMaxDigits", 25),
          ("destSmeMin", 6),
          ("destSmeMinDigits", 24),
          ("destSmeNai", 3),
          ("destSmeNp", 4),
          ("destSmeTable", 22),
          ("destSmeTableImsi", 26),
          ("destSmeTableNai", 27),
          ("destSmeTableNp", 28),
          ("destSmscExact", 8),
          ("destSmscGta", 7),
          ("destSmscMaxDigits", 30),
          ("destSmscMinDigits", 29),
          ("destSmscNai", 9),
          ("destSmscNp", 10),
          ("multiMessageDialog", 45),
          ("origImsiExact", 36),
          ("origImsiGta", 35),
          ("origImsiMaxDigits", 40),
          ("origImsiMinDigits", 39),
          ("origImsiNai", 37),
          ("origImsiNp", 38),
          ("origImsiTable", 42),
          ("origImsiUnknown", 41),
          ("origSmeExact", 12),
          ("origSmeGta", 11),
          ("origSmeMaxDigits", 32),
          ("origSmeMinDigits", 31),
          ("origSmeNai", 13),
          ("origSmeNp", 14),
          ("origSmeTable", 23),
          ("origSmeTableNai", 33),
          ("origSmeTableNp", 34),
          ("origSmscExact", 16),
          ("origSmscGta", 15),
          ("origSmscMaxDigits", 44),
          ("origSmscMinDigits", 43),
          ("origSmscNai", 17),
          ("origSmscNp", 18),
          ("pid", 19),
          ("tid", 20))
    )

_CmlrRuleInputParameters_Type.__name__ = "Bits"
_CmlrRuleInputParameters_Object = MibTableColumn
cmlrRuleInputParameters = _CmlrRuleInputParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 4),
    _CmlrRuleInputParameters_Type()
)
cmlrRuleInputParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleInputParameters.setStatus("current")


class _CmlrRuleDestPort_Type(Unsigned32):
    """Custom type cmlrRuleDestPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmlrRuleDestPort_Type.__name__ = "Unsigned32"
_CmlrRuleDestPort_Object = MibTableColumn
cmlrRuleDestPort = _CmlrRuleDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 5),
    _CmlrRuleDestPort_Type()
)
cmlrRuleDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestPort.setStatus("current")


class _CmlrRuleDestSmeGta_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrRuleDestSmeGta based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrRuleDestSmeGta_Object = MibTableColumn
cmlrRuleDestSmeGta = _CmlrRuleDestSmeGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 6),
    _CmlrRuleDestSmeGta_Type()
)
cmlrRuleDestSmeGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeGta.setStatus("current")


class _CmlrRuleDestSmeNai_Type(CItpTcNAI):
    """Custom type cmlrRuleDestSmeNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleDestSmeNai_Object = MibTableColumn
cmlrRuleDestSmeNai = _CmlrRuleDestSmeNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 7),
    _CmlrRuleDestSmeNai_Type()
)
cmlrRuleDestSmeNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeNai.setStatus("current")


class _CmlrRuleDestSmeNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleDestSmeNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleDestSmeNp_Object = MibTableColumn
cmlrRuleDestSmeNp = _CmlrRuleDestSmeNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 8),
    _CmlrRuleDestSmeNp_Type()
)
cmlrRuleDestSmeNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeNp.setStatus("current")


class _CmlrRuleDestSmscGta_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrRuleDestSmscGta based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrRuleDestSmscGta_Object = MibTableColumn
cmlrRuleDestSmscGta = _CmlrRuleDestSmscGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 9),
    _CmlrRuleDestSmscGta_Type()
)
cmlrRuleDestSmscGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmscGta.setStatus("current")


class _CmlrRuleDestSmscNai_Type(CItpTcNAI):
    """Custom type cmlrRuleDestSmscNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleDestSmscNai_Object = MibTableColumn
cmlrRuleDestSmscNai = _CmlrRuleDestSmscNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 10),
    _CmlrRuleDestSmscNai_Type()
)
cmlrRuleDestSmscNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmscNai.setStatus("current")


class _CmlrRuleDestSmscNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleDestSmscNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleDestSmscNp_Object = MibTableColumn
cmlrRuleDestSmscNp = _CmlrRuleDestSmscNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 11),
    _CmlrRuleDestSmscNp_Type()
)
cmlrRuleDestSmscNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmscNp.setStatus("current")


class _CmlrRuleOrigSmeGta_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrRuleOrigSmeGta based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrRuleOrigSmeGta_Object = MibTableColumn
cmlrRuleOrigSmeGta = _CmlrRuleOrigSmeGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 12),
    _CmlrRuleOrigSmeGta_Type()
)
cmlrRuleOrigSmeGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeGta.setStatus("current")


class _CmlrRuleOrigSmeNai_Type(CItpTcNAI):
    """Custom type cmlrRuleOrigSmeNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleOrigSmeNai_Object = MibTableColumn
cmlrRuleOrigSmeNai = _CmlrRuleOrigSmeNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 13),
    _CmlrRuleOrigSmeNai_Type()
)
cmlrRuleOrigSmeNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeNai.setStatus("current")


class _CmlrRuleOrigSmeNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleOrigSmeNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleOrigSmeNp_Object = MibTableColumn
cmlrRuleOrigSmeNp = _CmlrRuleOrigSmeNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 14),
    _CmlrRuleOrigSmeNp_Type()
)
cmlrRuleOrigSmeNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeNp.setStatus("current")


class _CmlrRuleOrigSmscGta_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrRuleOrigSmscGta based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrRuleOrigSmscGta_Object = MibTableColumn
cmlrRuleOrigSmscGta = _CmlrRuleOrigSmscGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 15),
    _CmlrRuleOrigSmscGta_Type()
)
cmlrRuleOrigSmscGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmscGta.setStatus("current")


class _CmlrRuleOrigSmscNai_Type(CItpTcNAI):
    """Custom type cmlrRuleOrigSmscNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleOrigSmscNai_Object = MibTableColumn
cmlrRuleOrigSmscNai = _CmlrRuleOrigSmscNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 16),
    _CmlrRuleOrigSmscNai_Type()
)
cmlrRuleOrigSmscNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmscNai.setStatus("current")


class _CmlrRuleOrigSmscNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleOrigSmscNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleOrigSmscNp_Object = MibTableColumn
cmlrRuleOrigSmscNp = _CmlrRuleOrigSmscNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 17),
    _CmlrRuleOrigSmscNp_Type()
)
cmlrRuleOrigSmscNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmscNp.setStatus("current")


class _CmlrRuleProtocolId_Type(Unsigned32):
    """Custom type cmlrRuleProtocolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmlrRuleProtocolId_Type.__name__ = "Unsigned32"
_CmlrRuleProtocolId_Object = MibTableColumn
cmlrRuleProtocolId = _CmlrRuleProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 18),
    _CmlrRuleProtocolId_Type()
)
cmlrRuleProtocolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleProtocolId.setStatus("current")


class _CmlrRuleTeleserviceId_Type(Unsigned32):
    """Custom type cmlrRuleTeleserviceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmlrRuleTeleserviceId_Type.__name__ = "Unsigned32"
_CmlrRuleTeleserviceId_Object = MibTableColumn
cmlrRuleTeleserviceId = _CmlrRuleTeleserviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 19),
    _CmlrRuleTeleserviceId_Type()
)
cmlrRuleTeleserviceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleTeleserviceId.setStatus("current")


class _CmlrRuleAddressTable_Type(CmlrName):
    """Custom type cmlrRuleAddressTable based on CmlrName"""
    defaultHexValue = ""


_CmlrRuleAddressTable_Object = MibTableColumn
cmlrRuleAddressTable = _CmlrRuleAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 20),
    _CmlrRuleAddressTable_Type()
)
cmlrRuleAddressTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleAddressTable.setStatus("current")


class _CmlrRuleResultParameters_Type(CmlrResultParameters):
    """Custom type cmlrRuleResultParameters based on CmlrResultParameters"""
    defaultBinValue = "0"


_CmlrRuleResultParameters_Object = MibTableColumn
cmlrRuleResultParameters = _CmlrRuleResultParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 21),
    _CmlrRuleResultParameters_Type()
)
cmlrRuleResultParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultParameters.setStatus("current")
_CmlrRuleResultNetwork_Type = CItpTcNetworkName
_CmlrRuleResultNetwork_Object = MibTableColumn
cmlrRuleResultNetwork = _CmlrRuleResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 22),
    _CmlrRuleResultNetwork_Type()
)
cmlrRuleResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultNetwork.setStatus("current")


class _CmlrRuleResultType_Type(CmlrResultType):
    """Custom type cmlrRuleResultType based on CmlrResultType"""


_CmlrRuleResultType_Object = MibTableColumn
cmlrRuleResultType = _CmlrRuleResultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 23),
    _CmlrRuleResultType_Type()
)
cmlrRuleResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultType.setStatus("current")


class _CmlrRuleResultOctet_Type(CmlrResultOctet):
    """Custom type cmlrRuleResultOctet based on CmlrResultOctet"""
    defaultHexValue = ""


_CmlrRuleResultOctet_Object = MibTableColumn
cmlrRuleResultOctet = _CmlrRuleResultOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 24),
    _CmlrRuleResultOctet_Type()
)
cmlrRuleResultOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultOctet.setStatus("current")


class _CmlrRuleResultTransType_Type(CgsccpGttTransType):
    """Custom type cmlrRuleResultTransType based on CgsccpGttTransType"""
    defaultValue = 0


_CmlrRuleResultTransType_Object = MibTableColumn
cmlrRuleResultTransType = _CmlrRuleResultTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 25),
    _CmlrRuleResultTransType_Type()
)
cmlrRuleResultTransType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultTransType.setStatus("current")


class _CmlrRuleResultGti_Type(CgsccpGttGlobalTitleInd):
    """Custom type cmlrRuleResultGti based on CgsccpGttGlobalTitleInd"""
    defaultValue = 0


_CmlrRuleResultGti_Object = MibTableColumn
cmlrRuleResultGti = _CmlrRuleResultGti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 26),
    _CmlrRuleResultGti_Type()
)
cmlrRuleResultGti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultGti.setStatus("current")


class _CmlrRuleResultNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleResultNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleResultNp_Object = MibTableColumn
cmlrRuleResultNp = _CmlrRuleResultNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 27),
    _CmlrRuleResultNp_Type()
)
cmlrRuleResultNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultNp.setStatus("current")


class _CmlrRuleResultNai_Type(CItpTcNAI):
    """Custom type cmlrRuleResultNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleResultNai_Object = MibTableColumn
cmlrRuleResultNai = _CmlrRuleResultNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 28),
    _CmlrRuleResultNai_Type()
)
cmlrRuleResultNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultNai.setStatus("current")


class _CmlrRuleResultPc_Type(CItpTcPointCode):
    """Custom type cmlrRuleResultPc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrRuleResultPc_Object = MibTableColumn
cmlrRuleResultPc = _CmlrRuleResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 29),
    _CmlrRuleResultPc_Type()
)
cmlrRuleResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultPc.setStatus("current")


class _CmlrRuleResultSsn_Type(CItpTcSubSystemNumber):
    """Custom type cmlrRuleResultSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CmlrRuleResultSsn_Object = MibTableColumn
cmlrRuleResultSsn = _CmlrRuleResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 30),
    _CmlrRuleResultSsn_Type()
)
cmlrRuleResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleResultSsn.setStatus("current")
_CmlrRuleMatchCounts_Type = Counter32
_CmlrRuleMatchCounts_Object = MibTableColumn
cmlrRuleMatchCounts = _CmlrRuleMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 31),
    _CmlrRuleMatchCounts_Type()
)
cmlrRuleMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrRuleMatchCounts.setStatus("current")
_CmlrRuleRowStatus_Type = RowStatus
_CmlrRuleRowStatus_Object = MibTableColumn
cmlrRuleRowStatus = _CmlrRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 32),
    _CmlrRuleRowStatus_Type()
)
cmlrRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleRowStatus.setStatus("current")


class _CmlrRuleOrigAddressTable_Type(CmlrName):
    """Custom type cmlrRuleOrigAddressTable based on CmlrName"""
    defaultHexValue = ""


_CmlrRuleOrigAddressTable_Object = MibTableColumn
cmlrRuleOrigAddressTable = _CmlrRuleOrigAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 33),
    _CmlrRuleOrigAddressTable_Type()
)
cmlrRuleOrigAddressTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigAddressTable.setStatus("current")
_CmlrRuleDestSmeMinDigits_Type = CmlrMinimumDigits
_CmlrRuleDestSmeMinDigits_Object = MibTableColumn
cmlrRuleDestSmeMinDigits = _CmlrRuleDestSmeMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 34),
    _CmlrRuleDestSmeMinDigits_Type()
)
cmlrRuleDestSmeMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeMinDigits.setStatus("current")
_CmlrRuleDestSmeMaxDigits_Type = CmlrMaximumDigits
_CmlrRuleDestSmeMaxDigits_Object = MibTableColumn
cmlrRuleDestSmeMaxDigits = _CmlrRuleDestSmeMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 35),
    _CmlrRuleDestSmeMaxDigits_Type()
)
cmlrRuleDestSmeMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeMaxDigits.setStatus("current")


class _CmlrRuleDestSmeTableNai_Type(CItpTcNAI):
    """Custom type cmlrRuleDestSmeTableNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleDestSmeTableNai_Object = MibTableColumn
cmlrRuleDestSmeTableNai = _CmlrRuleDestSmeTableNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 36),
    _CmlrRuleDestSmeTableNai_Type()
)
cmlrRuleDestSmeTableNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeTableNai.setStatus("current")


class _CmlrRuleDestSmeTableNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleDestSmeTableNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleDestSmeTableNp_Object = MibTableColumn
cmlrRuleDestSmeTableNp = _CmlrRuleDestSmeTableNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 37),
    _CmlrRuleDestSmeTableNp_Type()
)
cmlrRuleDestSmeTableNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmeTableNp.setStatus("current")
_CmlrRuleDestSmscMinDigits_Type = CmlrMinimumDigits
_CmlrRuleDestSmscMinDigits_Object = MibTableColumn
cmlrRuleDestSmscMinDigits = _CmlrRuleDestSmscMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 38),
    _CmlrRuleDestSmscMinDigits_Type()
)
cmlrRuleDestSmscMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmscMinDigits.setStatus("current")
_CmlrRuleDestSmscMaxDigits_Type = CmlrMaximumDigits
_CmlrRuleDestSmscMaxDigits_Object = MibTableColumn
cmlrRuleDestSmscMaxDigits = _CmlrRuleDestSmscMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 39),
    _CmlrRuleDestSmscMaxDigits_Type()
)
cmlrRuleDestSmscMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleDestSmscMaxDigits.setStatus("current")
_CmlrRuleOrigSmeMinDigits_Type = CmlrMinimumDigits
_CmlrRuleOrigSmeMinDigits_Object = MibTableColumn
cmlrRuleOrigSmeMinDigits = _CmlrRuleOrigSmeMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 40),
    _CmlrRuleOrigSmeMinDigits_Type()
)
cmlrRuleOrigSmeMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeMinDigits.setStatus("current")
_CmlrRuleOrigSmeMaxDigits_Type = CmlrMaximumDigits
_CmlrRuleOrigSmeMaxDigits_Object = MibTableColumn
cmlrRuleOrigSmeMaxDigits = _CmlrRuleOrigSmeMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 41),
    _CmlrRuleOrigSmeMaxDigits_Type()
)
cmlrRuleOrigSmeMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeMaxDigits.setStatus("current")


class _CmlrRuleOrigSmeTableNai_Type(CItpTcNAI):
    """Custom type cmlrRuleOrigSmeTableNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleOrigSmeTableNai_Object = MibTableColumn
cmlrRuleOrigSmeTableNai = _CmlrRuleOrigSmeTableNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 42),
    _CmlrRuleOrigSmeTableNai_Type()
)
cmlrRuleOrigSmeTableNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeTableNai.setStatus("current")


class _CmlrRuleOrigSmeTableNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleOrigSmeTableNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleOrigSmeTableNp_Object = MibTableColumn
cmlrRuleOrigSmeTableNp = _CmlrRuleOrigSmeTableNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 43),
    _CmlrRuleOrigSmeTableNp_Type()
)
cmlrRuleOrigSmeTableNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmeTableNp.setStatus("current")


class _CmlrRuleOrigImsiGta_Type(CItpTcGtaLongDisplay):
    """Custom type cmlrRuleOrigImsiGta based on CItpTcGtaLongDisplay"""
    defaultHexValue = ""


_CmlrRuleOrigImsiGta_Object = MibTableColumn
cmlrRuleOrigImsiGta = _CmlrRuleOrigImsiGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 44),
    _CmlrRuleOrigImsiGta_Type()
)
cmlrRuleOrigImsiGta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiGta.setStatus("current")


class _CmlrRuleOrigImsiNai_Type(CItpTcNAI):
    """Custom type cmlrRuleOrigImsiNai based on CItpTcNAI"""
    defaultValue = 0


_CmlrRuleOrigImsiNai_Object = MibTableColumn
cmlrRuleOrigImsiNai = _CmlrRuleOrigImsiNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 45),
    _CmlrRuleOrigImsiNai_Type()
)
cmlrRuleOrigImsiNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiNai.setStatus("current")


class _CmlrRuleOrigImsiNp_Type(CItpTcNumberingPlan):
    """Custom type cmlrRuleOrigImsiNp based on CItpTcNumberingPlan"""
    defaultValue = 0


_CmlrRuleOrigImsiNp_Object = MibTableColumn
cmlrRuleOrigImsiNp = _CmlrRuleOrigImsiNp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 46),
    _CmlrRuleOrigImsiNp_Type()
)
cmlrRuleOrigImsiNp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiNp.setStatus("current")
_CmlrRuleOrigImsiMinDigits_Type = CmlrMinimumDigits
_CmlrRuleOrigImsiMinDigits_Object = MibTableColumn
cmlrRuleOrigImsiMinDigits = _CmlrRuleOrigImsiMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 47),
    _CmlrRuleOrigImsiMinDigits_Type()
)
cmlrRuleOrigImsiMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiMinDigits.setStatus("current")
_CmlrRuleOrigImsiMaxDigits_Type = CmlrMaximumDigits
_CmlrRuleOrigImsiMaxDigits_Object = MibTableColumn
cmlrRuleOrigImsiMaxDigits = _CmlrRuleOrigImsiMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 48),
    _CmlrRuleOrigImsiMaxDigits_Type()
)
cmlrRuleOrigImsiMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiMaxDigits.setStatus("current")


class _CmlrRuleOrigImsiTable_Type(CmlrName):
    """Custom type cmlrRuleOrigImsiTable based on CmlrName"""
    defaultHexValue = ""


_CmlrRuleOrigImsiTable_Object = MibTableColumn
cmlrRuleOrigImsiTable = _CmlrRuleOrigImsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 49),
    _CmlrRuleOrigImsiTable_Type()
)
cmlrRuleOrigImsiTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigImsiTable.setStatus("current")
_CmlrRuleOrigSmscMinDigits_Type = CmlrMinimumDigits
_CmlrRuleOrigSmscMinDigits_Object = MibTableColumn
cmlrRuleOrigSmscMinDigits = _CmlrRuleOrigSmscMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 50),
    _CmlrRuleOrigSmscMinDigits_Type()
)
cmlrRuleOrigSmscMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmscMinDigits.setStatus("current")
_CmlrRuleOrigSmscMaxDigits_Type = CmlrMaximumDigits
_CmlrRuleOrigSmscMaxDigits_Object = MibTableColumn
cmlrRuleOrigSmscMaxDigits = _CmlrRuleOrigSmscMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 6, 1, 51),
    _CmlrRuleOrigSmscMaxDigits_Type()
)
cmlrRuleOrigSmscMaxDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrRuleOrigSmscMaxDigits.setStatus("current")
_CmlrResultSetTable_Object = MibTable
cmlrResultSetTable = _CmlrResultSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 8)
)
if mibBuilder.loadTexts:
    cmlrResultSetTable.setStatus("current")
_CmlrResultSetTableEntry_Object = MibTableRow
cmlrResultSetTableEntry = _CmlrResultSetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 8, 1)
)
cmlrResultSetTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrResultSetName"),
)
if mibBuilder.loadTexts:
    cmlrResultSetTableEntry.setStatus("current")
_CmlrResultSetName_Type = CmlrName
_CmlrResultSetName_Object = MibTableColumn
cmlrResultSetName = _CmlrResultSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 8, 1, 1),
    _CmlrResultSetName_Type()
)
cmlrResultSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrResultSetName.setStatus("current")


class _CmlrResultSetUnavailDiscard_Type(TruthValue):
    """Custom type cmlrResultSetUnavailDiscard based on TruthValue"""


_CmlrResultSetUnavailDiscard_Object = MibTableColumn
cmlrResultSetUnavailDiscard = _CmlrResultSetUnavailDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 8, 1, 2),
    _CmlrResultSetUnavailDiscard_Type()
)
cmlrResultSetUnavailDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultSetUnavailDiscard.setStatus("current")
_CmlrResultSetRowStatus_Type = RowStatus
_CmlrResultSetRowStatus_Object = MibTableColumn
cmlrResultSetRowStatus = _CmlrResultSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 8, 1, 3),
    _CmlrResultSetRowStatus_Type()
)
cmlrResultSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultSetRowStatus.setStatus("current")
_CmlrResultTable_Object = MibTable
cmlrResultTable = _CmlrResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9)
)
if mibBuilder.loadTexts:
    cmlrResultTable.setStatus("current")
_CmlrResultTableEntry_Object = MibTableRow
cmlrResultTableEntry = _CmlrResultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1)
)
cmlrResultTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrResultSetName"),
    (0, "CISCO-ITP-MLR-MIB", "cmlrResultNumber"),
)
if mibBuilder.loadTexts:
    cmlrResultTableEntry.setStatus("current")
_CmlrResultNumber_Type = CmlrId
_CmlrResultNumber_Object = MibTableColumn
cmlrResultNumber = _CmlrResultNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 1),
    _CmlrResultNumber_Type()
)
cmlrResultNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmlrResultNumber.setStatus("current")


class _CmlrResultType_Type(CmlrResultType):
    """Custom type cmlrResultType based on CmlrResultType"""


_CmlrResultType_Object = MibTableColumn
cmlrResultType = _CmlrResultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 2),
    _CmlrResultType_Type()
)
cmlrResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultType.setStatus("current")
_CmlrResultNetwork_Type = CItpTcNetworkName
_CmlrResultNetwork_Object = MibTableColumn
cmlrResultNetwork = _CmlrResultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 3),
    _CmlrResultNetwork_Type()
)
cmlrResultNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultNetwork.setStatus("current")


class _CmlrResultOctet_Type(CmlrResultOctet):
    """Custom type cmlrResultOctet based on CmlrResultOctet"""
    defaultHexValue = ""


_CmlrResultOctet_Object = MibTableColumn
cmlrResultOctet = _CmlrResultOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 4),
    _CmlrResultOctet_Type()
)
cmlrResultOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultOctet.setStatus("current")


class _CmlrResultPc_Type(CItpTcPointCode):
    """Custom type cmlrResultPc based on CItpTcPointCode"""
    defaultValue = 0


_CmlrResultPc_Object = MibTableColumn
cmlrResultPc = _CmlrResultPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 5),
    _CmlrResultPc_Type()
)
cmlrResultPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultPc.setStatus("current")


class _CmlrResultSsn_Type(CItpTcSubSystemNumber):
    """Custom type cmlrResultSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CmlrResultSsn_Object = MibTableColumn
cmlrResultSsn = _CmlrResultSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 6),
    _CmlrResultSsn_Type()
)
cmlrResultSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultSsn.setStatus("current")


class _CmlrResultWeight_Type(Integer32):
    """Custom type cmlrResultWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CmlrResultWeight_Type.__name__ = "Integer32"
_CmlrResultWeight_Object = MibTableColumn
cmlrResultWeight = _CmlrResultWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 7),
    _CmlrResultWeight_Type()
)
cmlrResultWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultWeight.setStatus("current")
_CmlrResultCounts_Type = Counter32
_CmlrResultCounts_Object = MibTableColumn
cmlrResultCounts = _CmlrResultCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 8),
    _CmlrResultCounts_Type()
)
cmlrResultCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmlrResultCounts.setStatus("current")
_CmlrResultRowStatus_Type = RowStatus
_CmlrResultRowStatus_Object = MibTableColumn
cmlrResultRowStatus = _CmlrResultRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 1, 9, 1, 9),
    _CmlrResultRowStatus_Type()
)
cmlrResultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmlrResultRowStatus.setStatus("current")
_CiscoMlrMIBConform_ObjectIdentity = ObjectIdentity
ciscoMlrMIBConform = _CiscoMlrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2)
)
_CiscoMlrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMlrMIBCompliances = _CiscoMlrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 1)
)
_CiscoMlrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMlrMIBGroups = _CiscoMlrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2)
)

# Managed Objects groups

ciscoMlrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 1)
)
ciscoMlrTableGroup.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrTableLoadNotifEnabled"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLastChanged"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLastLoadTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLoadStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLastURL"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstRoutedCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstAbortCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstContinueCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSmsMoCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSmsMtCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSriSmCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSmdPpCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstAlertScCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSmsRequestCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstSmsNotifCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstUnsupSCCPmsgTypeCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstUnsupSegSCCPmsgCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstUnsupportedMsgCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstParsingErrorCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstNoResultCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultContinueCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstNoServerDiscardCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultGttCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstUnparsedCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultBlockCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstGTImismatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstAddrConvFailureCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstDestUnavailableCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstFailedTrigMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstDiscontinuityTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstNoServerContinueCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultAsCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultPcCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstResultPcSsnCounts"))
)
if mibBuilder.loadTexts:
    ciscoMlrTableGroup.setStatus("current")

ciscoMlrTriggerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 2)
)
ciscoMlrTriggerGroup.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrTriggerParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerGt"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerDpc"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerOpc"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerOpcMask"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerSi"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerRuleset"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerActive"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerStartDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerEndDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlTriggerPreliminaryMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrTriggerRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerGt"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerRuleset"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrSubTriggerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMlrTriggerGroup.setStatus("current")

ciscoMlrAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 3)
)
ciscoMlrAddressGroup.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrAddressResultParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultType"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultOctet"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressResultSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrAddressRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMlrAddressGroup.setStatus("current")

ciscoMlrRuleSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 4)
)
ciscoMlrRuleSetGroup.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrRuleSetSegmented"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetSearchType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetStartDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetEndDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOperationType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleInputParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestPort"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocolId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleTeleserviceId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleAddressTable"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultOctet"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMlrRuleSetGroup.setStatus("deprecated")

ciscoMlrResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 5)
)
ciscoMlrResultGroup.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrResultSetUnavailDiscard"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultSetRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultType"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultOctet"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultWeight"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrResultRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMlrResultGroup.setStatus("current")

ciscoMlrRuleSetGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 7)
)
ciscoMlrRuleSetGroupRev1.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrRuleSetSegmented"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetSearchType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetStartDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetEndDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOperationType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleInputParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestPort"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocolId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleTeleserviceId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleAddressTable"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultOctet"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigAddressTable"))
)
if mibBuilder.loadTexts:
    ciscoMlrRuleSetGroupRev1.setStatus("deprecated")

ciscoMlrRuleSetGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 8)
)
ciscoMlrRuleSetGroupRev2.setObjects(
      *(("CISCO-ITP-MLR-MIB", "cmlrRuleSetSegmented"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetSearchType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetStartDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetEndDateAndTime"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleSetRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOperationType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocol"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleInputParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestPort"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleProtocolId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleTeleserviceId"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleAddressTable"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultParameters"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNetwork"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultOctet"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultTransType"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultGti"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultPc"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleResultSsn"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleMatchCounts"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleRowStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigAddressTable"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeMinDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeMaxDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeTableNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmeTableNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscMinDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleDestSmscMaxDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeMinDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeMaxDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeTableNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmeTableNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiGta"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiNai"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiNp"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiMinDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiMaxDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigImsiTable"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscMinDigits"),
        ("CISCO-ITP-MLR-MIB", "cmlrRuleOrigSmscMaxDigits"))
)
if mibBuilder.loadTexts:
    ciscoMlrRuleSetGroupRev2.setStatus("current")


# Notification objects

ciscoMlrTableLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 0, 1)
)
ciscoMlrTableLoad.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLoadStatus"),
        ("CISCO-ITP-MLR-MIB", "cmlrInstLastURL"))
)
if mibBuilder.loadTexts:
    ciscoMlrTableLoad.setStatus(
        "current"
    )


# Notifications groups

ciscoMlrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 2, 6)
)
ciscoMlrNotificationsGroup.setObjects(
    ("CISCO-ITP-MLR-MIB", "ciscoMlrTableLoad")
)
if mibBuilder.loadTexts:
    ciscoMlrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMlrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMlrMIBCompliance.setStatus(
        "deprecated"
    )

ciscoMlrMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMlrMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoMlrMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 396, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoMlrMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-MLR-MIB",
    **{"CmlrAddressDigits": CmlrAddressDigits,
       "CmlrAddressType": CmlrAddressType,
       "CmlrId": CmlrId,
       "CmlrName": CmlrName,
       "CmlrResultOctet": CmlrResultOctet,
       "CmlrResultParameters": CmlrResultParameters,
       "CmlrResultType": CmlrResultType,
       "CmlrRuleProtocol": CmlrRuleProtocol,
       "CmlrRuleSetName": CmlrRuleSetName,
       "CmlrMinimumDigits": CmlrMinimumDigits,
       "CmlrMaximumDigits": CmlrMaximumDigits,
       "ciscoMlrMIB": ciscoMlrMIB,
       "ciscoMlrMIBNotifs": ciscoMlrMIBNotifs,
       "ciscoMlrTableLoad": ciscoMlrTableLoad,
       "ciscoMlrMIBObjects": ciscoMlrMIBObjects,
       "cmlrScalars": cmlrScalars,
       "cmlrTableLoadNotifEnabled": cmlrTableLoadNotifEnabled,
       "cmlrInstTable": cmlrInstTable,
       "cmlrInstTableEntry": cmlrInstTableEntry,
       "cmlrInstLastChanged": cmlrInstLastChanged,
       "cmlrInstLastLoadTime": cmlrInstLastLoadTime,
       "cmlrInstLoadStatus": cmlrInstLoadStatus,
       "cmlrInstLastURL": cmlrInstLastURL,
       "cmlrInstRoutedCounts": cmlrInstRoutedCounts,
       "cmlrInstAbortCounts": cmlrInstAbortCounts,
       "cmlrInstContinueCounts": cmlrInstContinueCounts,
       "cmlrInstSmsMoCounts": cmlrInstSmsMoCounts,
       "cmlrInstSmsMtCounts": cmlrInstSmsMtCounts,
       "cmlrInstSriSmCounts": cmlrInstSriSmCounts,
       "cmlrInstSmdPpCounts": cmlrInstSmdPpCounts,
       "cmlrInstAlertScCounts": cmlrInstAlertScCounts,
       "cmlrInstSmsRequestCounts": cmlrInstSmsRequestCounts,
       "cmlrInstSmsNotifCounts": cmlrInstSmsNotifCounts,
       "cmlrInstUnsupSCCPmsgTypeCounts": cmlrInstUnsupSCCPmsgTypeCounts,
       "cmlrInstUnsupSegSCCPmsgCounts": cmlrInstUnsupSegSCCPmsgCounts,
       "cmlrInstUnsupportedMsgCounts": cmlrInstUnsupportedMsgCounts,
       "cmlrInstParsingErrorCounts": cmlrInstParsingErrorCounts,
       "cmlrInstNoResultCounts": cmlrInstNoResultCounts,
       "cmlrInstResultContinueCounts": cmlrInstResultContinueCounts,
       "cmlrInstNoServerDiscardCounts": cmlrInstNoServerDiscardCounts,
       "cmlrInstResultGttCounts": cmlrInstResultGttCounts,
       "cmlrInstUnparsedCounts": cmlrInstUnparsedCounts,
       "cmlrInstResultBlockCounts": cmlrInstResultBlockCounts,
       "cmlrInstGTImismatchCounts": cmlrInstGTImismatchCounts,
       "cmlrInstAddrConvFailureCounts": cmlrInstAddrConvFailureCounts,
       "cmlrInstDestUnavailableCounts": cmlrInstDestUnavailableCounts,
       "cmlrInstFailedTrigMatchCounts": cmlrInstFailedTrigMatchCounts,
       "cmlrInstDiscontinuityTime": cmlrInstDiscontinuityTime,
       "cmlrInstNoServerContinueCounts": cmlrInstNoServerContinueCounts,
       "cmlrInstResultAsCounts": cmlrInstResultAsCounts,
       "cmlrInstResultPcCounts": cmlrInstResultPcCounts,
       "cmlrInstResultPcSsnCounts": cmlrInstResultPcSsnCounts,
       "cmlrTriggerTable": cmlrTriggerTable,
       "cmlrTriggerTableEntry": cmlrTriggerTableEntry,
       "cmlrTableName": cmlrTableName,
       "cmlrTriggerNumber": cmlrTriggerNumber,
       "cmlrTriggerParameters": cmlrTriggerParameters,
       "cmlrTriggerGt": cmlrTriggerGt,
       "cmlrTriggerTransType": cmlrTriggerTransType,
       "cmlrTriggerGti": cmlrTriggerGti,
       "cmlrTriggerNp": cmlrTriggerNp,
       "cmlrTriggerNai": cmlrTriggerNai,
       "cmlrTriggerPc": cmlrTriggerPc,
       "cmlrTriggerSsn": cmlrTriggerSsn,
       "cmlrTriggerDpc": cmlrTriggerDpc,
       "cmlrTriggerOpc": cmlrTriggerOpc,
       "cmlrTriggerOpcMask": cmlrTriggerOpcMask,
       "cmlrTriggerSi": cmlrTriggerSi,
       "cmlrTriggerNetwork": cmlrTriggerNetwork,
       "cmlrTriggerRuleset": cmlrTriggerRuleset,
       "cmlrTriggerActive": cmlrTriggerActive,
       "cmlrTriggerStartDateAndTime": cmlrTriggerStartDateAndTime,
       "cmlrTriggerEndDateAndTime": cmlrTriggerEndDateAndTime,
       "cmlTriggerPreliminaryMatchCounts": cmlTriggerPreliminaryMatchCounts,
       "cmlrTriggerMatchCounts": cmlrTriggerMatchCounts,
       "cmlrTriggerRowStatus": cmlrTriggerRowStatus,
       "cmlrSubTriggerTable": cmlrSubTriggerTable,
       "cmlrSubTriggerTableEntry": cmlrSubTriggerTableEntry,
       "cmlrSubTriggerNumber": cmlrSubTriggerNumber,
       "cmlrSubTriggerParameters": cmlrSubTriggerParameters,
       "cmlrSubTriggerGt": cmlrSubTriggerGt,
       "cmlrSubTriggerTransType": cmlrSubTriggerTransType,
       "cmlrSubTriggerGti": cmlrSubTriggerGti,
       "cmlrSubTriggerNp": cmlrSubTriggerNp,
       "cmlrSubTriggerNai": cmlrSubTriggerNai,
       "cmlrSubTriggerPc": cmlrSubTriggerPc,
       "cmlrSubTriggerSsn": cmlrSubTriggerSsn,
       "cmlrSubTriggerNetwork": cmlrSubTriggerNetwork,
       "cmlrSubTriggerRuleset": cmlrSubTriggerRuleset,
       "cmlrSubTriggerMatchCounts": cmlrSubTriggerMatchCounts,
       "cmlrSubTriggerRowStatus": cmlrSubTriggerRowStatus,
       "cmlrAddressTable": cmlrAddressTable,
       "cmlrAddressTableEntry": cmlrAddressTableEntry,
       "cmlrAddressTableName": cmlrAddressTableName,
       "cmlrAddressType": cmlrAddressType,
       "cmlrAddressDigits": cmlrAddressDigits,
       "cmlrAddressExactMatch": cmlrAddressExactMatch,
       "cmlrAddressResultParameters": cmlrAddressResultParameters,
       "cmlrAddressResultNetwork": cmlrAddressResultNetwork,
       "cmlrAddressResultType": cmlrAddressResultType,
       "cmlrAddressResultOctet": cmlrAddressResultOctet,
       "cmlrAddressResultTransType": cmlrAddressResultTransType,
       "cmlrAddressResultGti": cmlrAddressResultGti,
       "cmlrAddressResultNp": cmlrAddressResultNp,
       "cmlrAddressResultNai": cmlrAddressResultNai,
       "cmlrAddressResultPc": cmlrAddressResultPc,
       "cmlrAddressResultSsn": cmlrAddressResultSsn,
       "cmlrAddressMatchCounts": cmlrAddressMatchCounts,
       "cmlrAddressRowStatus": cmlrAddressRowStatus,
       "cmlrRuleSetTable": cmlrRuleSetTable,
       "cmlrRuleSetTableEntry": cmlrRuleSetTableEntry,
       "cmlrRuleSetName": cmlrRuleSetName,
       "cmlrRuleSetSegmented": cmlrRuleSetSegmented,
       "cmlrRuleSetProtocol": cmlrRuleSetProtocol,
       "cmlrRuleSetSearchType": cmlrRuleSetSearchType,
       "cmlrRuleSetStartDateAndTime": cmlrRuleSetStartDateAndTime,
       "cmlrRuleSetEndDateAndTime": cmlrRuleSetEndDateAndTime,
       "cmlrRuleSetRowStatus": cmlrRuleSetRowStatus,
       "cmlrRuleTable": cmlrRuleTable,
       "cmlrRuleTableEntry": cmlrRuleTableEntry,
       "cmlrRuleNumber": cmlrRuleNumber,
       "cmlrRuleOperationType": cmlrRuleOperationType,
       "cmlrRuleProtocol": cmlrRuleProtocol,
       "cmlrRuleInputParameters": cmlrRuleInputParameters,
       "cmlrRuleDestPort": cmlrRuleDestPort,
       "cmlrRuleDestSmeGta": cmlrRuleDestSmeGta,
       "cmlrRuleDestSmeNai": cmlrRuleDestSmeNai,
       "cmlrRuleDestSmeNp": cmlrRuleDestSmeNp,
       "cmlrRuleDestSmscGta": cmlrRuleDestSmscGta,
       "cmlrRuleDestSmscNai": cmlrRuleDestSmscNai,
       "cmlrRuleDestSmscNp": cmlrRuleDestSmscNp,
       "cmlrRuleOrigSmeGta": cmlrRuleOrigSmeGta,
       "cmlrRuleOrigSmeNai": cmlrRuleOrigSmeNai,
       "cmlrRuleOrigSmeNp": cmlrRuleOrigSmeNp,
       "cmlrRuleOrigSmscGta": cmlrRuleOrigSmscGta,
       "cmlrRuleOrigSmscNai": cmlrRuleOrigSmscNai,
       "cmlrRuleOrigSmscNp": cmlrRuleOrigSmscNp,
       "cmlrRuleProtocolId": cmlrRuleProtocolId,
       "cmlrRuleTeleserviceId": cmlrRuleTeleserviceId,
       "cmlrRuleAddressTable": cmlrRuleAddressTable,
       "cmlrRuleResultParameters": cmlrRuleResultParameters,
       "cmlrRuleResultNetwork": cmlrRuleResultNetwork,
       "cmlrRuleResultType": cmlrRuleResultType,
       "cmlrRuleResultOctet": cmlrRuleResultOctet,
       "cmlrRuleResultTransType": cmlrRuleResultTransType,
       "cmlrRuleResultGti": cmlrRuleResultGti,
       "cmlrRuleResultNp": cmlrRuleResultNp,
       "cmlrRuleResultNai": cmlrRuleResultNai,
       "cmlrRuleResultPc": cmlrRuleResultPc,
       "cmlrRuleResultSsn": cmlrRuleResultSsn,
       "cmlrRuleMatchCounts": cmlrRuleMatchCounts,
       "cmlrRuleRowStatus": cmlrRuleRowStatus,
       "cmlrRuleOrigAddressTable": cmlrRuleOrigAddressTable,
       "cmlrRuleDestSmeMinDigits": cmlrRuleDestSmeMinDigits,
       "cmlrRuleDestSmeMaxDigits": cmlrRuleDestSmeMaxDigits,
       "cmlrRuleDestSmeTableNai": cmlrRuleDestSmeTableNai,
       "cmlrRuleDestSmeTableNp": cmlrRuleDestSmeTableNp,
       "cmlrRuleDestSmscMinDigits": cmlrRuleDestSmscMinDigits,
       "cmlrRuleDestSmscMaxDigits": cmlrRuleDestSmscMaxDigits,
       "cmlrRuleOrigSmeMinDigits": cmlrRuleOrigSmeMinDigits,
       "cmlrRuleOrigSmeMaxDigits": cmlrRuleOrigSmeMaxDigits,
       "cmlrRuleOrigSmeTableNai": cmlrRuleOrigSmeTableNai,
       "cmlrRuleOrigSmeTableNp": cmlrRuleOrigSmeTableNp,
       "cmlrRuleOrigImsiGta": cmlrRuleOrigImsiGta,
       "cmlrRuleOrigImsiNai": cmlrRuleOrigImsiNai,
       "cmlrRuleOrigImsiNp": cmlrRuleOrigImsiNp,
       "cmlrRuleOrigImsiMinDigits": cmlrRuleOrigImsiMinDigits,
       "cmlrRuleOrigImsiMaxDigits": cmlrRuleOrigImsiMaxDigits,
       "cmlrRuleOrigImsiTable": cmlrRuleOrigImsiTable,
       "cmlrRuleOrigSmscMinDigits": cmlrRuleOrigSmscMinDigits,
       "cmlrRuleOrigSmscMaxDigits": cmlrRuleOrigSmscMaxDigits,
       "cmlrResultSetTable": cmlrResultSetTable,
       "cmlrResultSetTableEntry": cmlrResultSetTableEntry,
       "cmlrResultSetName": cmlrResultSetName,
       "cmlrResultSetUnavailDiscard": cmlrResultSetUnavailDiscard,
       "cmlrResultSetRowStatus": cmlrResultSetRowStatus,
       "cmlrResultTable": cmlrResultTable,
       "cmlrResultTableEntry": cmlrResultTableEntry,
       "cmlrResultNumber": cmlrResultNumber,
       "cmlrResultType": cmlrResultType,
       "cmlrResultNetwork": cmlrResultNetwork,
       "cmlrResultOctet": cmlrResultOctet,
       "cmlrResultPc": cmlrResultPc,
       "cmlrResultSsn": cmlrResultSsn,
       "cmlrResultWeight": cmlrResultWeight,
       "cmlrResultCounts": cmlrResultCounts,
       "cmlrResultRowStatus": cmlrResultRowStatus,
       "ciscoMlrMIBConform": ciscoMlrMIBConform,
       "ciscoMlrMIBCompliances": ciscoMlrMIBCompliances,
       "ciscoMlrMIBCompliance": ciscoMlrMIBCompliance,
       "ciscoMlrMIBComplianceRev1": ciscoMlrMIBComplianceRev1,
       "ciscoMlrMIBComplianceRev2": ciscoMlrMIBComplianceRev2,
       "ciscoMlrMIBGroups": ciscoMlrMIBGroups,
       "ciscoMlrTableGroup": ciscoMlrTableGroup,
       "ciscoMlrTriggerGroup": ciscoMlrTriggerGroup,
       "ciscoMlrAddressGroup": ciscoMlrAddressGroup,
       "ciscoMlrRuleSetGroup": ciscoMlrRuleSetGroup,
       "ciscoMlrResultGroup": ciscoMlrResultGroup,
       "ciscoMlrNotificationsGroup": ciscoMlrNotificationsGroup,
       "ciscoMlrRuleSetGroupRev1": ciscoMlrRuleSetGroupRev1,
       "ciscoMlrRuleSetGroupRev2": ciscoMlrRuleSetGroupRev2}
)
