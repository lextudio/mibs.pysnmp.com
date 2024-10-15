# SNMP MIB module (CISCO-ITP-GTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GTCAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:27 2024
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

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstDisplayName,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstDisplayName",
    "cgspInstNetwork")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGtcapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695)
)
ciscoGtcapMIB.setRevisions(
        ("2008-12-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpTcTCAPUser(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGtcapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGtcapMIBNotifs = _CiscoGtcapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0)
)
_CiscoGtcapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGtcapMIBObjects = _CiscoGtcapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1)
)
_CgtcapScalars_ObjectIdentity = ObjectIdentity
cgtcapScalars = _CgtcapScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1)
)


class _CgtcapTranErrorNotifEnabled_Type(TruthValue):
    """Custom type cgtcapTranErrorNotifEnabled based on TruthValue"""


_CgtcapTranErrorNotifEnabled_Object = MibScalar
cgtcapTranErrorNotifEnabled = _CgtcapTranErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 1),
    _CgtcapTranErrorNotifEnabled_Type()
)
cgtcapTranErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapTranErrorNotifEnabled.setStatus("current")


class _CgtcapCompErrorNotifEnabled_Type(TruthValue):
    """Custom type cgtcapCompErrorNotifEnabled based on TruthValue"""


_CgtcapCompErrorNotifEnabled_Object = MibScalar
cgtcapCompErrorNotifEnabled = _CgtcapCompErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 2),
    _CgtcapCompErrorNotifEnabled_Type()
)
cgtcapCompErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapCompErrorNotifEnabled.setStatus("current")


class _CgtcapUsrErrorNotifEnabled_Type(TruthValue):
    """Custom type cgtcapUsrErrorNotifEnabled based on TruthValue"""


_CgtcapUsrErrorNotifEnabled_Object = MibScalar
cgtcapUsrErrorNotifEnabled = _CgtcapUsrErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 3),
    _CgtcapUsrErrorNotifEnabled_Type()
)
cgtcapUsrErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapUsrErrorNotifEnabled.setStatus("current")


class _CgtcapThreshldExcdNotifEnabled_Type(TruthValue):
    """Custom type cgtcapThreshldExcdNotifEnabled based on TruthValue"""


_CgtcapThreshldExcdNotifEnabled_Object = MibScalar
cgtcapThreshldExcdNotifEnabled = _CgtcapThreshldExcdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 4),
    _CgtcapThreshldExcdNotifEnabled_Type()
)
cgtcapThreshldExcdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapThreshldExcdNotifEnabled.setStatus("current")


class _CgtcapNotifWindowTime_Type(Integer32):
    """Custom type cgtcapNotifWindowTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CgtcapNotifWindowTime_Type.__name__ = "Integer32"
_CgtcapNotifWindowTime_Object = MibScalar
cgtcapNotifWindowTime = _CgtcapNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 5),
    _CgtcapNotifWindowTime_Type()
)
cgtcapNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapNotifWindowTime.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapNotifWindowTime.setUnits("seconds")


class _CgtcapUtilSampleInterval_Type(Integer32):
    """Custom type cgtcapUtilSampleInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_CgtcapUtilSampleInterval_Type.__name__ = "Integer32"
_CgtcapUtilSampleInterval_Object = MibScalar
cgtcapUtilSampleInterval = _CgtcapUtilSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 6),
    _CgtcapUtilSampleInterval_Type()
)
cgtcapUtilSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgtcapUtilSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUtilSampleInterval.setUnits("seconds")


class _CgtcapStatsInterval_Type(Unsigned32):
    """Custom type cgtcapStatsInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_CgtcapStatsInterval_Type.__name__ = "Unsigned32"
_CgtcapStatsInterval_Object = MibScalar
cgtcapStatsInterval = _CgtcapStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 1, 7),
    _CgtcapStatsInterval_Type()
)
cgtcapStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapStatsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapStatsInterval.setUnits("seconds")
_CgtcapInst_ObjectIdentity = ObjectIdentity
cgtcapInst = _CgtcapInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2)
)
_CgtcapInstTable_Object = MibTable
cgtcapInstTable = _CgtcapInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgtcapInstTable.setStatus("current")
_CgtcapInstTableEntry_Object = MibTableRow
cgtcapInstTableEntry = _CgtcapInstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1)
)
cgtcapInstTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgtcapInstTableEntry.setStatus("current")
_CgtcapInstTotalTCMsgsSent_Type = Counter32
_CgtcapInstTotalTCMsgsSent_Object = MibTableColumn
cgtcapInstTotalTCMsgsSent = _CgtcapInstTotalTCMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 1),
    _CgtcapInstTotalTCMsgsSent_Type()
)
cgtcapInstTotalTCMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalTCMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalTCMsgsSent.setUnits("messages")
_CgtcapInstTotalTCMsgsRcvd_Type = Counter32
_CgtcapInstTotalTCMsgsRcvd_Object = MibTableColumn
cgtcapInstTotalTCMsgsRcvd = _CgtcapInstTotalTCMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 2),
    _CgtcapInstTotalTCMsgsRcvd_Type()
)
cgtcapInstTotalTCMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalTCMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalTCMsgsRcvd.setUnits("messages")
_CgtcapInstTotalCompSent_Type = Counter32
_CgtcapInstTotalCompSent_Object = MibTableColumn
cgtcapInstTotalCompSent = _CgtcapInstTotalCompSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 3),
    _CgtcapInstTotalCompSent_Type()
)
cgtcapInstTotalCompSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalCompSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalCompSent.setUnits("components")
_CgtcapInstTotalCompRcvd_Type = Counter32
_CgtcapInstTotalCompRcvd_Object = MibTableColumn
cgtcapInstTotalCompRcvd = _CgtcapInstTotalCompRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 4),
    _CgtcapInstTotalCompRcvd_Type()
)
cgtcapInstTotalCompRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalCompRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalCompRcvd.setUnits("components")
_CgtcapInstActiveExceedThresholds_Type = Counter32
_CgtcapInstActiveExceedThresholds_Object = MibTableColumn
cgtcapInstActiveExceedThresholds = _CgtcapInstActiveExceedThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 5),
    _CgtcapInstActiveExceedThresholds_Type()
)
cgtcapInstActiveExceedThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstActiveExceedThresholds.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstActiveExceedThresholds.setUnits("occurences")
_CgtcapInstUnidirectionalTranRcvd_Type = Counter32
_CgtcapInstUnidirectionalTranRcvd_Object = MibTableColumn
cgtcapInstUnidirectionalTranRcvd = _CgtcapInstUnidirectionalTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 6),
    _CgtcapInstUnidirectionalTranRcvd_Type()
)
cgtcapInstUnidirectionalTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstUnidirectionalTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstUnidirectionalTranRcvd.setUnits("messages")
_CgtcapInstUnidirectionalTranSent_Type = Counter32
_CgtcapInstUnidirectionalTranSent_Object = MibTableColumn
cgtcapInstUnidirectionalTranSent = _CgtcapInstUnidirectionalTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 7),
    _CgtcapInstUnidirectionalTranSent_Type()
)
cgtcapInstUnidirectionalTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstUnidirectionalTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstUnidirectionalTranSent.setUnits("messages")
_CgtcapInstBeginQueryTranRcvd_Type = Counter32
_CgtcapInstBeginQueryTranRcvd_Object = MibTableColumn
cgtcapInstBeginQueryTranRcvd = _CgtcapInstBeginQueryTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 8),
    _CgtcapInstBeginQueryTranRcvd_Type()
)
cgtcapInstBeginQueryTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryTranRcvd.setUnits("messages")
_CgtcapInstBeginQueryTranSent_Type = Counter32
_CgtcapInstBeginQueryTranSent_Object = MibTableColumn
cgtcapInstBeginQueryTranSent = _CgtcapInstBeginQueryTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 9),
    _CgtcapInstBeginQueryTranSent_Type()
)
cgtcapInstBeginQueryTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryTranSent.setUnits("messages")
_CgtcapInstBeginQueryWOPermTranRcvd_Type = Counter32
_CgtcapInstBeginQueryWOPermTranRcvd_Object = MibTableColumn
cgtcapInstBeginQueryWOPermTranRcvd = _CgtcapInstBeginQueryWOPermTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 10),
    _CgtcapInstBeginQueryWOPermTranRcvd_Type()
)
cgtcapInstBeginQueryWOPermTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryWOPermTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryWOPermTranRcvd.setUnits("messages")
_CgtcapInstBeginQueryWOPermTranSent_Type = Counter32
_CgtcapInstBeginQueryWOPermTranSent_Object = MibTableColumn
cgtcapInstBeginQueryWOPermTranSent = _CgtcapInstBeginQueryWOPermTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 11),
    _CgtcapInstBeginQueryWOPermTranSent_Type()
)
cgtcapInstBeginQueryWOPermTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryWOPermTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstBeginQueryWOPermTranSent.setUnits("messages")
_CgtcapInstEndResponseTranRcvd_Type = Counter32
_CgtcapInstEndResponseTranRcvd_Object = MibTableColumn
cgtcapInstEndResponseTranRcvd = _CgtcapInstEndResponseTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 12),
    _CgtcapInstEndResponseTranRcvd_Type()
)
cgtcapInstEndResponseTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstEndResponseTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstEndResponseTranRcvd.setUnits("messages")
_CgtcapInstEndResponseTranSent_Type = Counter32
_CgtcapInstEndResponseTranSent_Object = MibTableColumn
cgtcapInstEndResponseTranSent = _CgtcapInstEndResponseTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 13),
    _CgtcapInstEndResponseTranSent_Type()
)
cgtcapInstEndResponseTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstEndResponseTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstEndResponseTranSent.setUnits("messages")
_CgtcapInstContinueConvTranRcvd_Type = Counter32
_CgtcapInstContinueConvTranRcvd_Object = MibTableColumn
cgtcapInstContinueConvTranRcvd = _CgtcapInstContinueConvTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 14),
    _CgtcapInstContinueConvTranRcvd_Type()
)
cgtcapInstContinueConvTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstContinueConvTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstContinueConvTranRcvd.setUnits("messages")
_CgtcapInstContinueConvTranSent_Type = Counter32
_CgtcapInstContinueConvTranSent_Object = MibTableColumn
cgtcapInstContinueConvTranSent = _CgtcapInstContinueConvTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 15),
    _CgtcapInstContinueConvTranSent_Type()
)
cgtcapInstContinueConvTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstContinueConvTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstContinueConvTranSent.setUnits("messages")
_CgtcapInstContConvWOPermTranRcvd_Type = Counter32
_CgtcapInstContConvWOPermTranRcvd_Object = MibTableColumn
cgtcapInstContConvWOPermTranRcvd = _CgtcapInstContConvWOPermTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 16),
    _CgtcapInstContConvWOPermTranRcvd_Type()
)
cgtcapInstContConvWOPermTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstContConvWOPermTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstContConvWOPermTranRcvd.setUnits("messages")
_CgtcapInstContConvWOPermTranSent_Type = Counter32
_CgtcapInstContConvWOPermTranSent_Object = MibTableColumn
cgtcapInstContConvWOPermTranSent = _CgtcapInstContConvWOPermTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 17),
    _CgtcapInstContConvWOPermTranSent_Type()
)
cgtcapInstContConvWOPermTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstContConvWOPermTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstContConvWOPermTranSent.setUnits("messages")
_CgtcapInstAbortTranRcvd_Type = Counter32
_CgtcapInstAbortTranRcvd_Object = MibTableColumn
cgtcapInstAbortTranRcvd = _CgtcapInstAbortTranRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 18),
    _CgtcapInstAbortTranRcvd_Type()
)
cgtcapInstAbortTranRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstAbortTranRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstAbortTranRcvd.setUnits("messages")
_CgtcapInstAbortTranSent_Type = Counter32
_CgtcapInstAbortTranSent_Object = MibTableColumn
cgtcapInstAbortTranSent = _CgtcapInstAbortTranSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 19),
    _CgtcapInstAbortTranSent_Type()
)
cgtcapInstAbortTranSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstAbortTranSent.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstAbortTranSent.setUnits("messages")
_CgtcapInstClass1TCLocalCancelInd_Type = Counter32
_CgtcapInstClass1TCLocalCancelInd_Object = MibTableColumn
cgtcapInstClass1TCLocalCancelInd = _CgtcapInstClass1TCLocalCancelInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 20),
    _CgtcapInstClass1TCLocalCancelInd_Type()
)
cgtcapInstClass1TCLocalCancelInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstClass1TCLocalCancelInd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstClass1TCLocalCancelInd.setUnits("occurrences")
_CgtcapInstTotalDiscardsAllReasons_Type = Counter32
_CgtcapInstTotalDiscardsAllReasons_Object = MibTableColumn
cgtcapInstTotalDiscardsAllReasons = _CgtcapInstTotalDiscardsAllReasons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 21),
    _CgtcapInstTotalDiscardsAllReasons_Type()
)
cgtcapInstTotalDiscardsAllReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalDiscardsAllReasons.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalDiscardsAllReasons.setUnits("messages")
_CgtcapInstProviderAbortsRcvd_Type = Counter32
_CgtcapInstProviderAbortsRcvd_Object = MibTableColumn
cgtcapInstProviderAbortsRcvd = _CgtcapInstProviderAbortsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 22),
    _CgtcapInstProviderAbortsRcvd_Type()
)
cgtcapInstProviderAbortsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstProviderAbortsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstProviderAbortsRcvd.setUnits("messages")
_CgtcapInstTotalRejectsRcvd_Type = Counter32
_CgtcapInstTotalRejectsRcvd_Object = MibTableColumn
cgtcapInstTotalRejectsRcvd = _CgtcapInstTotalRejectsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 23),
    _CgtcapInstTotalRejectsRcvd_Type()
)
cgtcapInstTotalRejectsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalRejectsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalRejectsRcvd.setUnits("components")
_CgtcapInstTotalTransactionErr_Type = Counter32
_CgtcapInstTotalTransactionErr_Object = MibTableColumn
cgtcapInstTotalTransactionErr = _CgtcapInstTotalTransactionErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 2, 1, 1, 24),
    _CgtcapInstTotalTransactionErr_Type()
)
cgtcapInstTotalTransactionErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapInstTotalTransactionErr.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapInstTotalTransactionErr.setUnits("occurences")
_CgtcapUtil_ObjectIdentity = ObjectIdentity
cgtcapUtil = _CgtcapUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3)
)
_CgtcapUtilTable_Object = MibTable
cgtcapUtilTable = _CgtcapUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgtcapUtilTable.setStatus("current")
_CgtcapUtilTableEntry_Object = MibTableRow
cgtcapUtilTableEntry = _CgtcapUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1)
)
cgtcapUtilTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GTCAP-MIB", "cgtcapUtilSlot"),
    (0, "CISCO-ITP-GTCAP-MIB", "cgtcapUser"),
)
if mibBuilder.loadTexts:
    cgtcapUtilTableEntry.setStatus("current")


class _CgtcapUtilSlot_Type(Unsigned32):
    """Custom type cgtcapUtilSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CgtcapUtilSlot_Type.__name__ = "Unsigned32"
_CgtcapUtilSlot_Object = MibTableColumn
cgtcapUtilSlot = _CgtcapUtilSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 1),
    _CgtcapUtilSlot_Type()
)
cgtcapUtilSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgtcapUtilSlot.setStatus("current")
_CgtcapUser_Type = CItpTcTCAPUser
_CgtcapUser_Object = MibTableColumn
cgtcapUser = _CgtcapUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 2),
    _CgtcapUser_Type()
)
cgtcapUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgtcapUser.setStatus("current")
_CgtcapNewTransInInterval_Type = Gauge32
_CgtcapNewTransInInterval_Object = MibTableColumn
cgtcapNewTransInInterval = _CgtcapNewTransInInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 3),
    _CgtcapNewTransInInterval_Type()
)
cgtcapNewTransInInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapNewTransInInterval.setStatus("current")
_CgtcapMeanOpenTransIdInInterval_Type = Gauge32
_CgtcapMeanOpenTransIdInInterval_Object = MibTableColumn
cgtcapMeanOpenTransIdInInterval = _CgtcapMeanOpenTransIdInInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 4),
    _CgtcapMeanOpenTransIdInInterval_Type()
)
cgtcapMeanOpenTransIdInInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapMeanOpenTransIdInInterval.setStatus("current")
_CgtcapCumulativeMeanDurationOfTran_Type = Gauge32
_CgtcapCumulativeMeanDurationOfTran_Object = MibTableColumn
cgtcapCumulativeMeanDurationOfTran = _CgtcapCumulativeMeanDurationOfTran_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 5),
    _CgtcapCumulativeMeanDurationOfTran_Type()
)
cgtcapCumulativeMeanDurationOfTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapCumulativeMeanDurationOfTran.setStatus("current")
_CgtcapMaxOpenTransIdInInterval_Type = Gauge32
_CgtcapMaxOpenTransIdInInterval_Object = MibTableColumn
cgtcapMaxOpenTransIdInInterval = _CgtcapMaxOpenTransIdInInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 6),
    _CgtcapMaxOpenTransIdInInterval_Type()
)
cgtcapMaxOpenTransIdInInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapMaxOpenTransIdInInterval.setStatus("current")
_CgtcapUtilEndTimestamp_Type = TimeStamp
_CgtcapUtilEndTimestamp_Object = MibTableColumn
cgtcapUtilEndTimestamp = _CgtcapUtilEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 7),
    _CgtcapUtilEndTimestamp_Type()
)
cgtcapUtilEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUtilEndTimestamp.setStatus("current")
_CgtcapUtilPhysicalIndex_Type = EntPhysicalIndexOrZero
_CgtcapUtilPhysicalIndex_Object = MibTableColumn
cgtcapUtilPhysicalIndex = _CgtcapUtilPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 3, 1, 1, 8),
    _CgtcapUtilPhysicalIndex_Type()
)
cgtcapUtilPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUtilPhysicalIndex.setStatus("current")
_CgtcapPrErrTranRcvd_ObjectIdentity = ObjectIdentity
cgtcapPrErrTranRcvd = _CgtcapPrErrTranRcvd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4)
)
_CgtcapProtoTranRcvdErrorsTable_Object = MibTable
cgtcapProtoTranRcvdErrorsTable = _CgtcapProtoTranRcvdErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgtcapProtoTranRcvdErrorsTable.setStatus("current")
_CgtcapProtoTranRcvdErrorsTableEntry_Object = MibTableRow
cgtcapProtoTranRcvdErrorsTableEntry = _CgtcapProtoTranRcvdErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1)
)
cgtcapProtoTranRcvdErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgtcapProtoTranRcvdErrorsTableEntry.setStatus("current")
_CgtcapPrTranAbrtRcvdUnrecogMsgType_Type = Counter32
_CgtcapPrTranAbrtRcvdUnrecogMsgType_Object = MibTableColumn
cgtcapPrTranAbrtRcvdUnrecogMsgType = _CgtcapPrTranAbrtRcvdUnrecogMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1, 1),
    _CgtcapPrTranAbrtRcvdUnrecogMsgType_Type()
)
cgtcapPrTranAbrtRcvdUnrecogMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdUnrecogMsgType.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdUnrecogMsgType.setUnits("occurrences")
_CgtcapPrTranAbrtRcvdIncorrectTP_Type = Counter32
_CgtcapPrTranAbrtRcvdIncorrectTP_Object = MibTableColumn
cgtcapPrTranAbrtRcvdIncorrectTP = _CgtcapPrTranAbrtRcvdIncorrectTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1, 2),
    _CgtcapPrTranAbrtRcvdIncorrectTP_Type()
)
cgtcapPrTranAbrtRcvdIncorrectTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdIncorrectTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdIncorrectTP.setUnits("occurrences")
_CgtcapPrTranAbrtRcvdBadFmtTP_Type = Counter32
_CgtcapPrTranAbrtRcvdBadFmtTP_Object = MibTableColumn
cgtcapPrTranAbrtRcvdBadFmtTP = _CgtcapPrTranAbrtRcvdBadFmtTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1, 3),
    _CgtcapPrTranAbrtRcvdBadFmtTP_Type()
)
cgtcapPrTranAbrtRcvdBadFmtTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdBadFmtTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdBadFmtTP.setUnits("occurrences")
_CgtcapPrTranAbrtRcvdUnrecogTID_Type = Counter32
_CgtcapPrTranAbrtRcvdUnrecogTID_Object = MibTableColumn
cgtcapPrTranAbrtRcvdUnrecogTID = _CgtcapPrTranAbrtRcvdUnrecogTID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1, 4),
    _CgtcapPrTranAbrtRcvdUnrecogTID_Type()
)
cgtcapPrTranAbrtRcvdUnrecogTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdUnrecogTID.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdUnrecogTID.setUnits("occurrences")
_CgtcapPrTranAbrtRcvdResrcLimit_Type = Counter32
_CgtcapPrTranAbrtRcvdResrcLimit_Object = MibTableColumn
cgtcapPrTranAbrtRcvdResrcLimit = _CgtcapPrTranAbrtRcvdResrcLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 4, 1, 1, 5),
    _CgtcapPrTranAbrtRcvdResrcLimit_Type()
)
cgtcapPrTranAbrtRcvdResrcLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdResrcLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtRcvdResrcLimit.setUnits("occurrences")
_CgtcapPrErrTranSent_ObjectIdentity = ObjectIdentity
cgtcapPrErrTranSent = _CgtcapPrErrTranSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5)
)
_CgtcapProtoTranSentErrorsTable_Object = MibTable
cgtcapProtoTranSentErrorsTable = _CgtcapProtoTranSentErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgtcapProtoTranSentErrorsTable.setStatus("current")
_CgtcapProtoTranSentErrorsTableEntry_Object = MibTableRow
cgtcapProtoTranSentErrorsTableEntry = _CgtcapProtoTranSentErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1)
)
cgtcapProtoTranSentErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GTCAP-MIB", "cgtcapUser"),
)
if mibBuilder.loadTexts:
    cgtcapProtoTranSentErrorsTableEntry.setStatus("current")
_CgtcapPrTranAbrtSentUnrecogMsgType_Type = Counter32
_CgtcapPrTranAbrtSentUnrecogMsgType_Object = MibTableColumn
cgtcapPrTranAbrtSentUnrecogMsgType = _CgtcapPrTranAbrtSentUnrecogMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1, 1),
    _CgtcapPrTranAbrtSentUnrecogMsgType_Type()
)
cgtcapPrTranAbrtSentUnrecogMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentUnrecogMsgType.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentUnrecogMsgType.setUnits("occurrences")
_CgtcapPrTranAbrtSentIncorrectTP_Type = Counter32
_CgtcapPrTranAbrtSentIncorrectTP_Object = MibTableColumn
cgtcapPrTranAbrtSentIncorrectTP = _CgtcapPrTranAbrtSentIncorrectTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1, 2),
    _CgtcapPrTranAbrtSentIncorrectTP_Type()
)
cgtcapPrTranAbrtSentIncorrectTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentIncorrectTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentIncorrectTP.setUnits("occurrences")
_CgtcapPrTranAbrtSentBadFmtTP_Type = Counter32
_CgtcapPrTranAbrtSentBadFmtTP_Object = MibTableColumn
cgtcapPrTranAbrtSentBadFmtTP = _CgtcapPrTranAbrtSentBadFmtTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1, 3),
    _CgtcapPrTranAbrtSentBadFmtTP_Type()
)
cgtcapPrTranAbrtSentBadFmtTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentBadFmtTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentBadFmtTP.setUnits("occurrences")
_CgtcapPrTranAbrtSentUnrecogTID_Type = Counter32
_CgtcapPrTranAbrtSentUnrecogTID_Object = MibTableColumn
cgtcapPrTranAbrtSentUnrecogTID = _CgtcapPrTranAbrtSentUnrecogTID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1, 4),
    _CgtcapPrTranAbrtSentUnrecogTID_Type()
)
cgtcapPrTranAbrtSentUnrecogTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentUnrecogTID.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentUnrecogTID.setUnits("occurrences")
_CgtcapPrTranAbrtSentResrcLimit_Type = Counter32
_CgtcapPrTranAbrtSentResrcLimit_Object = MibTableColumn
cgtcapPrTranAbrtSentResrcLimit = _CgtcapPrTranAbrtSentResrcLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 5, 1, 1, 5),
    _CgtcapPrTranAbrtSentResrcLimit_Type()
)
cgtcapPrTranAbrtSentResrcLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentResrcLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrTranAbrtSentResrcLimit.setUnits("occurrences")
_CgtcapPrErrComp_ObjectIdentity = ObjectIdentity
cgtcapPrErrComp = _CgtcapPrErrComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6)
)
_CgtcapProtoCompErrorsTable_Object = MibTable
cgtcapProtoCompErrorsTable = _CgtcapProtoCompErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgtcapProtoCompErrorsTable.setStatus("current")
_CgtcapProtoCompErrorsTableEntry_Object = MibTableRow
cgtcapProtoCompErrorsTableEntry = _CgtcapProtoCompErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1)
)
cgtcapProtoCompErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgtcapProtoCompErrorsTableEntry.setStatus("current")
_CgtcapPrCompRjctRcvdUnrecogCompGP_Type = Counter32
_CgtcapPrCompRjctRcvdUnrecogCompGP_Object = MibTableColumn
cgtcapPrCompRjctRcvdUnrecogCompGP = _CgtcapPrCompRjctRcvdUnrecogCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 1),
    _CgtcapPrCompRjctRcvdUnrecogCompGP_Type()
)
cgtcapPrCompRjctRcvdUnrecogCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogCompGP.setUnits("occurrences")
_CgtcapPrCompRjctSentUnrecogCompGP_Type = Counter32
_CgtcapPrCompRjctSentUnrecogCompGP_Object = MibTableColumn
cgtcapPrCompRjctSentUnrecogCompGP = _CgtcapPrCompRjctSentUnrecogCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 2),
    _CgtcapPrCompRjctSentUnrecogCompGP_Type()
)
cgtcapPrCompRjctSentUnrecogCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogCompGP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdMistypedCompGP_Type = Counter32
_CgtcapPrCompRjctRcvdMistypedCompGP_Object = MibTableColumn
cgtcapPrCompRjctRcvdMistypedCompGP = _CgtcapPrCompRjctRcvdMistypedCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 3),
    _CgtcapPrCompRjctRcvdMistypedCompGP_Type()
)
cgtcapPrCompRjctRcvdMistypedCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdMistypedCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdMistypedCompGP.setUnits("occurrences")
_CgtcapPrCompRjctSentMistypedCompGP_Type = Counter32
_CgtcapPrCompRjctSentMistypedCompGP_Object = MibTableColumn
cgtcapPrCompRjctSentMistypedCompGP = _CgtcapPrCompRjctSentMistypedCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 4),
    _CgtcapPrCompRjctSentMistypedCompGP_Type()
)
cgtcapPrCompRjctSentMistypedCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentMistypedCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentMistypedCompGP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdBadStructCompGP_Type = Counter32
_CgtcapPrCompRjctRcvdBadStructCompGP_Object = MibTableColumn
cgtcapPrCompRjctRcvdBadStructCompGP = _CgtcapPrCompRjctRcvdBadStructCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 5),
    _CgtcapPrCompRjctRcvdBadStructCompGP_Type()
)
cgtcapPrCompRjctRcvdBadStructCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdBadStructCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdBadStructCompGP.setUnits("occurrences")
_CgtcapPrCompRjctSentBadStructCompGP_Type = Counter32
_CgtcapPrCompRjctSentBadStructCompGP_Object = MibTableColumn
cgtcapPrCompRjctSentBadStructCompGP = _CgtcapPrCompRjctSentBadStructCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 6),
    _CgtcapPrCompRjctSentBadStructCompGP_Type()
)
cgtcapPrCompRjctSentBadStructCompGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentBadStructCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentBadStructCompGP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdUnrecogLinkedIdIP_Type = Counter32
_CgtcapPrCompRjctRcvdUnrecogLinkedIdIP_Object = MibTableColumn
cgtcapPrCompRjctRcvdUnrecogLinkedIdIP = _CgtcapPrCompRjctRcvdUnrecogLinkedIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 7),
    _CgtcapPrCompRjctRcvdUnrecogLinkedIdIP_Type()
)
cgtcapPrCompRjctRcvdUnrecogLinkedIdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogLinkedIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogLinkedIdIP.setUnits("occurrences")
_CgtcapPrCompRjctSentUnrecogLinkedIdIP_Type = Counter32
_CgtcapPrCompRjctSentUnrecogLinkedIdIP_Object = MibTableColumn
cgtcapPrCompRjctSentUnrecogLinkedIdIP = _CgtcapPrCompRjctSentUnrecogLinkedIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 8),
    _CgtcapPrCompRjctSentUnrecogLinkedIdIP_Type()
)
cgtcapPrCompRjctSentUnrecogLinkedIdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogLinkedIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogLinkedIdIP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdUnrecogInvIdRRP_Type = Counter32
_CgtcapPrCompRjctRcvdUnrecogInvIdRRP_Object = MibTableColumn
cgtcapPrCompRjctRcvdUnrecogInvIdRRP = _CgtcapPrCompRjctRcvdUnrecogInvIdRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 9),
    _CgtcapPrCompRjctRcvdUnrecogInvIdRRP_Type()
)
cgtcapPrCompRjctRcvdUnrecogInvIdRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogInvIdRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogInvIdRRP.setUnits("occurrences")
_CgtcapPrCompRjctSentUnrecogInvIdRRP_Type = Counter32
_CgtcapPrCompRjctSentUnrecogInvIdRRP_Object = MibTableColumn
cgtcapPrCompRjctSentUnrecogInvIdRRP = _CgtcapPrCompRjctSentUnrecogInvIdRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 10),
    _CgtcapPrCompRjctSentUnrecogInvIdRRP_Type()
)
cgtcapPrCompRjctSentUnrecogInvIdRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogInvIdRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogInvIdRRP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdRetRsltUnexpRRP_Type = Counter32
_CgtcapPrCompRjctRcvdRetRsltUnexpRRP_Object = MibTableColumn
cgtcapPrCompRjctRcvdRetRsltUnexpRRP = _CgtcapPrCompRjctRcvdRetRsltUnexpRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 11),
    _CgtcapPrCompRjctRcvdRetRsltUnexpRRP_Type()
)
cgtcapPrCompRjctRcvdRetRsltUnexpRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdRetRsltUnexpRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdRetRsltUnexpRRP.setUnits("occurrences")
_CgtcapPrCompRjctSentRetRsltUnexpRRP_Type = Counter32
_CgtcapPrCompRjctSentRetRsltUnexpRRP_Object = MibTableColumn
cgtcapPrCompRjctSentRetRsltUnexpRRP = _CgtcapPrCompRjctSentRetRsltUnexpRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 12),
    _CgtcapPrCompRjctSentRetRsltUnexpRRP_Type()
)
cgtcapPrCompRjctSentRetRsltUnexpRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentRetRsltUnexpRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentRetRsltUnexpRRP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdUnrecogInvIdREP_Type = Counter32
_CgtcapPrCompRjctRcvdUnrecogInvIdREP_Object = MibTableColumn
cgtcapPrCompRjctRcvdUnrecogInvIdREP = _CgtcapPrCompRjctRcvdUnrecogInvIdREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 13),
    _CgtcapPrCompRjctRcvdUnrecogInvIdREP_Type()
)
cgtcapPrCompRjctRcvdUnrecogInvIdREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogInvIdREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnrecogInvIdREP.setUnits("occurrences")
_CgtcapPrCompRjctSentUnrecogInvIdREP_Type = Counter32
_CgtcapPrCompRjctSentUnrecogInvIdREP_Object = MibTableColumn
cgtcapPrCompRjctSentUnrecogInvIdREP = _CgtcapPrCompRjctSentUnrecogInvIdREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 14),
    _CgtcapPrCompRjctSentUnrecogInvIdREP_Type()
)
cgtcapPrCompRjctSentUnrecogInvIdREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogInvIdREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnrecogInvIdREP.setUnits("occurrences")
_CgtcapPrCompRjctRcvdUnexpRetErrREP_Type = Counter32
_CgtcapPrCompRjctRcvdUnexpRetErrREP_Object = MibTableColumn
cgtcapPrCompRjctRcvdUnexpRetErrREP = _CgtcapPrCompRjctRcvdUnexpRetErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 15),
    _CgtcapPrCompRjctRcvdUnexpRetErrREP_Type()
)
cgtcapPrCompRjctRcvdUnexpRetErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnexpRetErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctRcvdUnexpRetErrREP.setUnits("occurrences")
_CgtcapPrCompRjctSentUnexpRetErrREP_Type = Counter32
_CgtcapPrCompRjctSentUnexpRetErrREP_Object = MibTableColumn
cgtcapPrCompRjctSentUnexpRetErrREP = _CgtcapPrCompRjctSentUnexpRetErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 6, 1, 1, 16),
    _CgtcapPrCompRjctSentUnexpRetErrREP_Type()
)
cgtcapPrCompRjctSentUnexpRetErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnexpRetErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapPrCompRjctSentUnexpRetErrREP.setUnits("occurrences")
_CgtcapUsrErrRcvd_ObjectIdentity = ObjectIdentity
cgtcapUsrErrRcvd = _CgtcapUsrErrRcvd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7)
)
_CgtcapUsrRjctRcvdErrorsTable_Object = MibTable
cgtcapUsrRjctRcvdErrorsTable = _CgtcapUsrRjctRcvdErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdErrorsTable.setStatus("current")
_CgtcapUsrRjctRcvdErrorsTableEntry_Object = MibTableRow
cgtcapUsrRjctRcvdErrorsTableEntry = _CgtcapUsrRjctRcvdErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1)
)
cgtcapUsrRjctRcvdErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdErrorsTableEntry.setStatus("current")
_CgtcapUsrRjctRcvdDupInvIdIP_Type = Counter32
_CgtcapUsrRjctRcvdDupInvIdIP_Object = MibTableColumn
cgtcapUsrRjctRcvdDupInvIdIP = _CgtcapUsrRjctRcvdDupInvIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 1),
    _CgtcapUsrRjctRcvdDupInvIdIP_Type()
)
cgtcapUsrRjctRcvdDupInvIdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdDupInvIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdDupInvIdIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdUnrecogOpIP_Type = Counter32
_CgtcapUsrRjctRcvdUnrecogOpIP_Object = MibTableColumn
cgtcapUsrRjctRcvdUnrecogOpIP = _CgtcapUsrRjctRcvdUnrecogOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 2),
    _CgtcapUsrRjctRcvdUnrecogOpIP_Type()
)
cgtcapUsrRjctRcvdUnrecogOpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnrecogOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnrecogOpIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdMistypedParamIP_Type = Counter32
_CgtcapUsrRjctRcvdMistypedParamIP_Object = MibTableColumn
cgtcapUsrRjctRcvdMistypedParamIP = _CgtcapUsrRjctRcvdMistypedParamIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 3),
    _CgtcapUsrRjctRcvdMistypedParamIP_Type()
)
cgtcapUsrRjctRcvdMistypedParamIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdResourceLimitIP_Type = Counter32
_CgtcapUsrRjctRcvdResourceLimitIP_Object = MibTableColumn
cgtcapUsrRjctRcvdResourceLimitIP = _CgtcapUsrRjctRcvdResourceLimitIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 4),
    _CgtcapUsrRjctRcvdResourceLimitIP_Type()
)
cgtcapUsrRjctRcvdResourceLimitIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdResourceLimitIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdResourceLimitIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdInitReleaseIP_Type = Counter32
_CgtcapUsrRjctRcvdInitReleaseIP_Object = MibTableColumn
cgtcapUsrRjctRcvdInitReleaseIP = _CgtcapUsrRjctRcvdInitReleaseIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 5),
    _CgtcapUsrRjctRcvdInitReleaseIP_Type()
)
cgtcapUsrRjctRcvdInitReleaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdInitReleaseIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdInitReleaseIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdLinkedRespUnexpIP_Type = Counter32
_CgtcapUsrRjctRcvdLinkedRespUnexpIP_Object = MibTableColumn
cgtcapUsrRjctRcvdLinkedRespUnexpIP = _CgtcapUsrRjctRcvdLinkedRespUnexpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 6),
    _CgtcapUsrRjctRcvdLinkedRespUnexpIP_Type()
)
cgtcapUsrRjctRcvdLinkedRespUnexpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdLinkedRespUnexpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdLinkedRespUnexpIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdUnexpLinkedOpIP_Type = Counter32
_CgtcapUsrRjctRcvdUnexpLinkedOpIP_Object = MibTableColumn
cgtcapUsrRjctRcvdUnexpLinkedOpIP = _CgtcapUsrRjctRcvdUnexpLinkedOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 7),
    _CgtcapUsrRjctRcvdUnexpLinkedOpIP_Type()
)
cgtcapUsrRjctRcvdUnexpLinkedOpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnexpLinkedOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnexpLinkedOpIP.setUnits("occurrences")
_CgtcapUsrRjctRcvdUnrecogErrREP_Type = Counter32
_CgtcapUsrRjctRcvdUnrecogErrREP_Object = MibTableColumn
cgtcapUsrRjctRcvdUnrecogErrREP = _CgtcapUsrRjctRcvdUnrecogErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 8),
    _CgtcapUsrRjctRcvdUnrecogErrREP_Type()
)
cgtcapUsrRjctRcvdUnrecogErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnrecogErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnrecogErrREP.setUnits("occurrences")
_CgtcapUsrRjctRcvdUnexpErrREP_Type = Counter32
_CgtcapUsrRjctRcvdUnexpErrREP_Object = MibTableColumn
cgtcapUsrRjctRcvdUnexpErrREP = _CgtcapUsrRjctRcvdUnexpErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 9),
    _CgtcapUsrRjctRcvdUnexpErrREP_Type()
)
cgtcapUsrRjctRcvdUnexpErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnexpErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdUnexpErrREP.setUnits("occurrences")
_CgtcapUsrRjctRcvdMistypedParamRRP_Type = Counter32
_CgtcapUsrRjctRcvdMistypedParamRRP_Object = MibTableColumn
cgtcapUsrRjctRcvdMistypedParamRRP = _CgtcapUsrRjctRcvdMistypedParamRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 10),
    _CgtcapUsrRjctRcvdMistypedParamRRP_Type()
)
cgtcapUsrRjctRcvdMistypedParamRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamRRP.setUnits("occurrences")
_CgtcapUsrRjctRcvdMistypedParamREP_Type = Counter32
_CgtcapUsrRjctRcvdMistypedParamREP_Object = MibTableColumn
cgtcapUsrRjctRcvdMistypedParamREP = _CgtcapUsrRjctRcvdMistypedParamREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 7, 1, 1, 11),
    _CgtcapUsrRjctRcvdMistypedParamREP_Type()
)
cgtcapUsrRjctRcvdMistypedParamREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctRcvdMistypedParamREP.setUnits("occurrences")
_CgtcapUsrErrSent_ObjectIdentity = ObjectIdentity
cgtcapUsrErrSent = _CgtcapUsrErrSent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8)
)
_CgtcapUsrRjctSentErrorsTable_Object = MibTable
cgtcapUsrRjctSentErrorsTable = _CgtcapUsrRjctSentErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentErrorsTable.setStatus("current")
_CgtcapUsrRjctSentErrorsTableEntry_Object = MibTableRow
cgtcapUsrRjctSentErrorsTableEntry = _CgtcapUsrRjctSentErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1)
)
cgtcapUsrRjctSentErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GTCAP-MIB", "cgtcapUser"),
)
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentErrorsTableEntry.setStatus("current")
_CgtcapUsrRjctSentDupInvIdIP_Type = Counter32
_CgtcapUsrRjctSentDupInvIdIP_Object = MibTableColumn
cgtcapUsrRjctSentDupInvIdIP = _CgtcapUsrRjctSentDupInvIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 1),
    _CgtcapUsrRjctSentDupInvIdIP_Type()
)
cgtcapUsrRjctSentDupInvIdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentDupInvIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentDupInvIdIP.setUnits("occurrences")
_CgtcapUsrRjctSentUnrecogOpIP_Type = Counter32
_CgtcapUsrRjctSentUnrecogOpIP_Object = MibTableColumn
cgtcapUsrRjctSentUnrecogOpIP = _CgtcapUsrRjctSentUnrecogOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 2),
    _CgtcapUsrRjctSentUnrecogOpIP_Type()
)
cgtcapUsrRjctSentUnrecogOpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnrecogOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnrecogOpIP.setUnits("occurrences")
_CgtcapUsrRjctSentMistypedParamIP_Type = Counter32
_CgtcapUsrRjctSentMistypedParamIP_Object = MibTableColumn
cgtcapUsrRjctSentMistypedParamIP = _CgtcapUsrRjctSentMistypedParamIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 3),
    _CgtcapUsrRjctSentMistypedParamIP_Type()
)
cgtcapUsrRjctSentMistypedParamIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamIP.setUnits("occurrences")
_CgtcapUsrRjctSentResourceLimitIP_Type = Counter32
_CgtcapUsrRjctSentResourceLimitIP_Object = MibTableColumn
cgtcapUsrRjctSentResourceLimitIP = _CgtcapUsrRjctSentResourceLimitIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 4),
    _CgtcapUsrRjctSentResourceLimitIP_Type()
)
cgtcapUsrRjctSentResourceLimitIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentResourceLimitIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentResourceLimitIP.setUnits("occurrences")
_CgtcapUsrRjctSentInitReleaseIP_Type = Counter32
_CgtcapUsrRjctSentInitReleaseIP_Object = MibTableColumn
cgtcapUsrRjctSentInitReleaseIP = _CgtcapUsrRjctSentInitReleaseIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 5),
    _CgtcapUsrRjctSentInitReleaseIP_Type()
)
cgtcapUsrRjctSentInitReleaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentInitReleaseIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentInitReleaseIP.setUnits("occurrences")
_CgtcapUsrRjctSentLinkedRespUnexpIP_Type = Counter32
_CgtcapUsrRjctSentLinkedRespUnexpIP_Object = MibTableColumn
cgtcapUsrRjctSentLinkedRespUnexpIP = _CgtcapUsrRjctSentLinkedRespUnexpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 6),
    _CgtcapUsrRjctSentLinkedRespUnexpIP_Type()
)
cgtcapUsrRjctSentLinkedRespUnexpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentLinkedRespUnexpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentLinkedRespUnexpIP.setUnits("occurrences")
_CgtcapUsrRjctSentUnexpLinkedOpIP_Type = Counter32
_CgtcapUsrRjctSentUnexpLinkedOpIP_Object = MibTableColumn
cgtcapUsrRjctSentUnexpLinkedOpIP = _CgtcapUsrRjctSentUnexpLinkedOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 7),
    _CgtcapUsrRjctSentUnexpLinkedOpIP_Type()
)
cgtcapUsrRjctSentUnexpLinkedOpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnexpLinkedOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnexpLinkedOpIP.setUnits("occurrences")
_CgtcapUsrRjctSentUnrecogErrREP_Type = Counter32
_CgtcapUsrRjctSentUnrecogErrREP_Object = MibTableColumn
cgtcapUsrRjctSentUnrecogErrREP = _CgtcapUsrRjctSentUnrecogErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 8),
    _CgtcapUsrRjctSentUnrecogErrREP_Type()
)
cgtcapUsrRjctSentUnrecogErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnrecogErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnrecogErrREP.setUnits("occurrences")
_CgtcapUsrRjctSentUnexpErrREP_Type = Counter32
_CgtcapUsrRjctSentUnexpErrREP_Object = MibTableColumn
cgtcapUsrRjctSentUnexpErrREP = _CgtcapUsrRjctSentUnexpErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 9),
    _CgtcapUsrRjctSentUnexpErrREP_Type()
)
cgtcapUsrRjctSentUnexpErrREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnexpErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentUnexpErrREP.setUnits("occurrences")
_CgtcapUsrRjctSentMistypedParamRRP_Type = Counter32
_CgtcapUsrRjctSentMistypedParamRRP_Object = MibTableColumn
cgtcapUsrRjctSentMistypedParamRRP = _CgtcapUsrRjctSentMistypedParamRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 10),
    _CgtcapUsrRjctSentMistypedParamRRP_Type()
)
cgtcapUsrRjctSentMistypedParamRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamRRP.setUnits("occurrences")
_CgtcapUsrRjctSentMistypedParamREP_Type = Counter32
_CgtcapUsrRjctSentMistypedParamREP_Object = MibTableColumn
cgtcapUsrRjctSentMistypedParamREP = _CgtcapUsrRjctSentMistypedParamREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 8, 1, 1, 11),
    _CgtcapUsrRjctSentMistypedParamREP_Type()
)
cgtcapUsrRjctSentMistypedParamREP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapUsrRjctSentMistypedParamREP.setUnits("occurrences")
_CgtcapNotifInfo_ObjectIdentity = ObjectIdentity
cgtcapNotifInfo = _CgtcapNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9)
)
_CgtcapNotifIntervalDuration_Type = Unsigned32
_CgtcapNotifIntervalDuration_Object = MibScalar
cgtcapNotifIntervalDuration = _CgtcapNotifIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 1),
    _CgtcapNotifIntervalDuration_Type()
)
cgtcapNotifIntervalDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapNotifIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapNotifIntervalDuration.setUnits("seconds")
_CgtcapIntervalActiveTranExceeds_Type = Unsigned32
_CgtcapIntervalActiveTranExceeds_Object = MibScalar
cgtcapIntervalActiveTranExceeds = _CgtcapIntervalActiveTranExceeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 2),
    _CgtcapIntervalActiveTranExceeds_Type()
)
cgtcapIntervalActiveTranExceeds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntervalActiveTranExceeds.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntervalActiveTranExceeds.setUnits("occurrences")
_CgtcapTCUser_Type = CItpTcTCAPUser
_CgtcapTCUser_Object = MibScalar
cgtcapTCUser = _CgtcapTCUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 3),
    _CgtcapTCUser_Type()
)
cgtcapTCUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapTCUser.setStatus("current")
_CgtcapIntTranAbrtUnrecogMsgType_Type = Counter32
_CgtcapIntTranAbrtUnrecogMsgType_Object = MibScalar
cgtcapIntTranAbrtUnrecogMsgType = _CgtcapIntTranAbrtUnrecogMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 4),
    _CgtcapIntTranAbrtUnrecogMsgType_Type()
)
cgtcapIntTranAbrtUnrecogMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtUnrecogMsgType.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtUnrecogMsgType.setUnits("occurrences")
_CgtcapIntTranAbrtIncorrectTP_Type = Unsigned32
_CgtcapIntTranAbrtIncorrectTP_Object = MibScalar
cgtcapIntTranAbrtIncorrectTP = _CgtcapIntTranAbrtIncorrectTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 5),
    _CgtcapIntTranAbrtIncorrectTP_Type()
)
cgtcapIntTranAbrtIncorrectTP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtIncorrectTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtIncorrectTP.setUnits("occurrences")
_CgtcapIntTranAbrtBadFmtTP_Type = Unsigned32
_CgtcapIntTranAbrtBadFmtTP_Object = MibScalar
cgtcapIntTranAbrtBadFmtTP = _CgtcapIntTranAbrtBadFmtTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 6),
    _CgtcapIntTranAbrtBadFmtTP_Type()
)
cgtcapIntTranAbrtBadFmtTP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtBadFmtTP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtBadFmtTP.setUnits("occurrences")
_CgtcapIntTranAbrtUnrecogTID_Type = Unsigned32
_CgtcapIntTranAbrtUnrecogTID_Object = MibScalar
cgtcapIntTranAbrtUnrecogTID = _CgtcapIntTranAbrtUnrecogTID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 7),
    _CgtcapIntTranAbrtUnrecogTID_Type()
)
cgtcapIntTranAbrtUnrecogTID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtUnrecogTID.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtUnrecogTID.setUnits("occurrences")
_CgtcapIntTranAbrtResrcLimit_Type = Unsigned32
_CgtcapIntTranAbrtResrcLimit_Object = MibScalar
cgtcapIntTranAbrtResrcLimit = _CgtcapIntTranAbrtResrcLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 8),
    _CgtcapIntTranAbrtResrcLimit_Type()
)
cgtcapIntTranAbrtResrcLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtResrcLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntTranAbrtResrcLimit.setUnits("occurrences")
_CgtcapIntCompRjctUnrecogCompGP_Type = Unsigned32
_CgtcapIntCompRjctUnrecogCompGP_Object = MibScalar
cgtcapIntCompRjctUnrecogCompGP = _CgtcapIntCompRjctUnrecogCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 9),
    _CgtcapIntCompRjctUnrecogCompGP_Type()
)
cgtcapIntCompRjctUnrecogCompGP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogCompGP.setUnits("occurrences")
_CgtcapIntCompRjctMistypedCompGP_Type = Unsigned32
_CgtcapIntCompRjctMistypedCompGP_Object = MibScalar
cgtcapIntCompRjctMistypedCompGP = _CgtcapIntCompRjctMistypedCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 10),
    _CgtcapIntCompRjctMistypedCompGP_Type()
)
cgtcapIntCompRjctMistypedCompGP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctMistypedCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctMistypedCompGP.setUnits("occurrences")
_CgtcapIntCompRjctBadStructCompGP_Type = Unsigned32
_CgtcapIntCompRjctBadStructCompGP_Object = MibScalar
cgtcapIntCompRjctBadStructCompGP = _CgtcapIntCompRjctBadStructCompGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 11),
    _CgtcapIntCompRjctBadStructCompGP_Type()
)
cgtcapIntCompRjctBadStructCompGP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctBadStructCompGP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctBadStructCompGP.setUnits("occurrences")
_CgtcapIntCompRjctUnrecogLinkedIdIP_Type = Unsigned32
_CgtcapIntCompRjctUnrecogLinkedIdIP_Object = MibScalar
cgtcapIntCompRjctUnrecogLinkedIdIP = _CgtcapIntCompRjctUnrecogLinkedIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 12),
    _CgtcapIntCompRjctUnrecogLinkedIdIP_Type()
)
cgtcapIntCompRjctUnrecogLinkedIdIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogLinkedIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogLinkedIdIP.setUnits("occurrences")
_CgtcapIntCompRjctUnrecogInvIdRRP_Type = Unsigned32
_CgtcapIntCompRjctUnrecogInvIdRRP_Object = MibScalar
cgtcapIntCompRjctUnrecogInvIdRRP = _CgtcapIntCompRjctUnrecogInvIdRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 13),
    _CgtcapIntCompRjctUnrecogInvIdRRP_Type()
)
cgtcapIntCompRjctUnrecogInvIdRRP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogInvIdRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogInvIdRRP.setUnits("occurrences")
_CgtcapIntCompRjctRetRsltUnexpRRP_Type = Unsigned32
_CgtcapIntCompRjctRetRsltUnexpRRP_Object = MibScalar
cgtcapIntCompRjctRetRsltUnexpRRP = _CgtcapIntCompRjctRetRsltUnexpRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 14),
    _CgtcapIntCompRjctRetRsltUnexpRRP_Type()
)
cgtcapIntCompRjctRetRsltUnexpRRP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctRetRsltUnexpRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctRetRsltUnexpRRP.setUnits("occurrences")
_CgtcapIntCompRjctUnrecogInvIdREP_Type = Unsigned32
_CgtcapIntCompRjctUnrecogInvIdREP_Object = MibScalar
cgtcapIntCompRjctUnrecogInvIdREP = _CgtcapIntCompRjctUnrecogInvIdREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 15),
    _CgtcapIntCompRjctUnrecogInvIdREP_Type()
)
cgtcapIntCompRjctUnrecogInvIdREP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogInvIdREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnrecogInvIdREP.setUnits("occurrences")
_CgtcapIntCompRjctUnexpRetErrREP_Type = Unsigned32
_CgtcapIntCompRjctUnexpRetErrREP_Object = MibScalar
cgtcapIntCompRjctUnexpRetErrREP = _CgtcapIntCompRjctUnexpRetErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 16),
    _CgtcapIntCompRjctUnexpRetErrREP_Type()
)
cgtcapIntCompRjctUnexpRetErrREP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnexpRetErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntCompRjctUnexpRetErrREP.setUnits("occurrences")
_CgtcapIntUsrRjctDupInvIdIP_Type = Unsigned32
_CgtcapIntUsrRjctDupInvIdIP_Object = MibScalar
cgtcapIntUsrRjctDupInvIdIP = _CgtcapIntUsrRjctDupInvIdIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 17),
    _CgtcapIntUsrRjctDupInvIdIP_Type()
)
cgtcapIntUsrRjctDupInvIdIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctDupInvIdIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctDupInvIdIP.setUnits("occurrences")
_CgtcapIntUsrRjctUnrecogOpIP_Type = Unsigned32
_CgtcapIntUsrRjctUnrecogOpIP_Object = MibScalar
cgtcapIntUsrRjctUnrecogOpIP = _CgtcapIntUsrRjctUnrecogOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 18),
    _CgtcapIntUsrRjctUnrecogOpIP_Type()
)
cgtcapIntUsrRjctUnrecogOpIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnrecogOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnrecogOpIP.setUnits("occurrences")
_CgtcapIntUsrRjctMistypedParamIP_Type = Unsigned32
_CgtcapIntUsrRjctMistypedParamIP_Object = MibScalar
cgtcapIntUsrRjctMistypedParamIP = _CgtcapIntUsrRjctMistypedParamIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 19),
    _CgtcapIntUsrRjctMistypedParamIP_Type()
)
cgtcapIntUsrRjctMistypedParamIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamIP.setUnits("occurrences")
_CgtcapIntUsrRjctResourceLimitIP_Type = Unsigned32
_CgtcapIntUsrRjctResourceLimitIP_Object = MibScalar
cgtcapIntUsrRjctResourceLimitIP = _CgtcapIntUsrRjctResourceLimitIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 20),
    _CgtcapIntUsrRjctResourceLimitIP_Type()
)
cgtcapIntUsrRjctResourceLimitIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctResourceLimitIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctResourceLimitIP.setUnits("occurrences")
_CgtcapIntUsrRjctInitReleaseIP_Type = Unsigned32
_CgtcapIntUsrRjctInitReleaseIP_Object = MibScalar
cgtcapIntUsrRjctInitReleaseIP = _CgtcapIntUsrRjctInitReleaseIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 21),
    _CgtcapIntUsrRjctInitReleaseIP_Type()
)
cgtcapIntUsrRjctInitReleaseIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctInitReleaseIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctInitReleaseIP.setUnits("occurrences")
_CgtcapIntUsrRjctLinkedRespUnexpIP_Type = Unsigned32
_CgtcapIntUsrRjctLinkedRespUnexpIP_Object = MibScalar
cgtcapIntUsrRjctLinkedRespUnexpIP = _CgtcapIntUsrRjctLinkedRespUnexpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 22),
    _CgtcapIntUsrRjctLinkedRespUnexpIP_Type()
)
cgtcapIntUsrRjctLinkedRespUnexpIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctLinkedRespUnexpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctLinkedRespUnexpIP.setUnits("occurrences")
_CgtcapIntUsrRjctUnexpLinkedOpIP_Type = Unsigned32
_CgtcapIntUsrRjctUnexpLinkedOpIP_Object = MibScalar
cgtcapIntUsrRjctUnexpLinkedOpIP = _CgtcapIntUsrRjctUnexpLinkedOpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 23),
    _CgtcapIntUsrRjctUnexpLinkedOpIP_Type()
)
cgtcapIntUsrRjctUnexpLinkedOpIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnexpLinkedOpIP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnexpLinkedOpIP.setUnits("occurrences")
_CgtcapIntUsrRjctUnrecogErrREP_Type = Unsigned32
_CgtcapIntUsrRjctUnrecogErrREP_Object = MibScalar
cgtcapIntUsrRjctUnrecogErrREP = _CgtcapIntUsrRjctUnrecogErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 24),
    _CgtcapIntUsrRjctUnrecogErrREP_Type()
)
cgtcapIntUsrRjctUnrecogErrREP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnrecogErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnrecogErrREP.setUnits("occurrences")
_CgtcapIntUsrRjctUnexpErrREP_Type = Unsigned32
_CgtcapIntUsrRjctUnexpErrREP_Object = MibScalar
cgtcapIntUsrRjctUnexpErrREP = _CgtcapIntUsrRjctUnexpErrREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 25),
    _CgtcapIntUsrRjctUnexpErrREP_Type()
)
cgtcapIntUsrRjctUnexpErrREP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnexpErrREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctUnexpErrREP.setUnits("occurrences")
_CgtcapIntUsrRjctMistypedParamRRP_Type = Unsigned32
_CgtcapIntUsrRjctMistypedParamRRP_Object = MibScalar
cgtcapIntUsrRjctMistypedParamRRP = _CgtcapIntUsrRjctMistypedParamRRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 26),
    _CgtcapIntUsrRjctMistypedParamRRP_Type()
)
cgtcapIntUsrRjctMistypedParamRRP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamRRP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamRRP.setUnits("occurrences")
_CgtcapIntUsrRjctMistypedParamREP_Type = Unsigned32
_CgtcapIntUsrRjctMistypedParamREP_Object = MibScalar
cgtcapIntUsrRjctMistypedParamREP = _CgtcapIntUsrRjctMistypedParamREP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 1, 9, 27),
    _CgtcapIntUsrRjctMistypedParamREP_Type()
)
cgtcapIntUsrRjctMistypedParamREP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamREP.setStatus("current")
if mibBuilder.loadTexts:
    cgtcapIntUsrRjctMistypedParamREP.setUnits("occurrences")
_CiscoGtcapMIBConform_ObjectIdentity = ObjectIdentity
ciscoGtcapMIBConform = _CiscoGtcapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2)
)
_CiscoGtcapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGtcapMIBCompliances = _CiscoGtcapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 1)
)
_CiscoGtcapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGtcapMIBGroups = _CiscoGtcapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2)
)

# Managed Objects groups

ciscoGtcapGlobalEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 1)
)
ciscoGtcapGlobalEntryGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapTranErrorNotifEnabled"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapCompErrorNotifEnabled"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrErrorNotifEnabled"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapThreshldExcdNotifEnabled"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifWindowTime"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUtilSampleInterval"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapStatsInterval"))
)
if mibBuilder.loadTexts:
    ciscoGtcapGlobalEntryGroup.setStatus("current")

ciscoGtcapInstTableEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 2)
)
ciscoGtcapInstTableEntryGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalTCMsgsSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalTCMsgsRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalCompSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalCompRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstActiveExceedThresholds"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstUnidirectionalTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstUnidirectionalTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstBeginQueryTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstBeginQueryTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstBeginQueryWOPermTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstBeginQueryWOPermTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstEndResponseTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstEndResponseTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstContinueConvTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstContinueConvTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstContConvWOPermTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstContConvWOPermTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstAbortTranRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstAbortTranSent"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstClass1TCLocalCancelInd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalDiscardsAllReasons"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstProviderAbortsRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalRejectsRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapInstTotalTransactionErr"))
)
if mibBuilder.loadTexts:
    ciscoGtcapInstTableEntryGroup.setStatus("current")

ciscogtcapUtilTableEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 3)
)
ciscogtcapUtilTableEntryGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapNewTransInInterval"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapMeanOpenTransIdInInterval"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapCumulativeMeanDurationOfTran"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapMaxOpenTransIdInInterval"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUtilEndTimestamp"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUtilPhysicalIndex"))
)
if mibBuilder.loadTexts:
    ciscogtcapUtilTableEntryGroup.setStatus("current")

ciscoGtcapProtoTranRcvdErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 4)
)
ciscoGtcapProtoTranRcvdErrorsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtRcvdUnrecogMsgType"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtRcvdIncorrectTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtRcvdBadFmtTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtRcvdUnrecogTID"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtRcvdResrcLimit"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoTranRcvdErrorsGroup.setStatus("current")

ciscoGtcapProtoTranSentErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 5)
)
ciscoGtcapProtoTranSentErrorsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtSentUnrecogMsgType"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtSentIncorrectTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtSentBadFmtTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtSentUnrecogTID"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrTranAbrtSentResrcLimit"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoTranSentErrorsGroup.setStatus("current")

ciscoGtcapProtoCompErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 6)
)
ciscoGtcapProtoCompErrorsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdUnrecogCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentUnrecogCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdMistypedCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentMistypedCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdBadStructCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentBadStructCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdUnrecogLinkedIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentUnrecogLinkedIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdUnrecogInvIdRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentUnrecogInvIdRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdRetRsltUnexpRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentRetRsltUnexpRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdUnrecogInvIdREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentUnrecogInvIdREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctRcvdUnexpRetErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapPrCompRjctSentUnexpRetErrREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoCompErrorsGroup.setStatus("current")

ciscoGtcapUsrRjctRcvdErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 7)
)
ciscoGtcapUsrRjctRcvdErrorsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdDupInvIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdUnrecogOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdMistypedParamIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdResourceLimitIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdInitReleaseIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdLinkedRespUnexpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdUnexpLinkedOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdUnrecogErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdUnexpErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdMistypedParamRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctRcvdMistypedParamREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapUsrRjctRcvdErrorsGroup.setStatus("current")

ciscoGtcapProtoCompSentErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 8)
)
ciscoGtcapProtoCompSentErrorsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentDupInvIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentUnrecogOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentMistypedParamIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentResourceLimitIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentInitReleaseIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentLinkedRespUnexpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentUnexpLinkedOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentUnrecogErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentUnexpErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentMistypedParamRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapUsrRjctSentMistypedParamREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoCompSentErrorsGroup.setStatus("current")

ciscoGtcapNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 9)
)
ciscoGtcapNotifInfoGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntervalActiveTranExceeds"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapTCUser"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogMsgType"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtIncorrectTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtBadFmtTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogTID"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtResrcLimit"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctMistypedCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctBadStructCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogLinkedIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctRetRsltUnexpRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnexpRetErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctDupInvIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctResourceLimitIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctInitReleaseIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctLinkedRespUnexpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpLinkedOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapNotifInfoGroup.setStatus("current")


# Notification objects

ciscoGtcapProtoErrTranAbortRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 1)
)
ciscoGtcapProtoErrTranAbortRcvd.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogMsgType"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtIncorrectTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtBadFmtTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogTID"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtResrcLimit"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoErrTranAbortRcvd.setStatus(
        "current"
    )

ciscoGtcapProtoErrTranAbortSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 2)
)
ciscoGtcapProtoErrTranAbortSent.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapTCUser"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogMsgType"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtIncorrectTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtBadFmtTP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtUnrecogTID"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntTranAbrtResrcLimit"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoErrTranAbortSent.setStatus(
        "current"
    )

ciscoGtcapProtoErrCompRejectRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 3)
)
ciscoGtcapProtoErrCompRejectRcvd.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctMistypedCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctBadStructCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogLinkedIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctRetRsltUnexpRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnexpRetErrREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoErrCompRejectRcvd.setStatus(
        "current"
    )

ciscoGtcapProtoErrCompRejectSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 4)
)
ciscoGtcapProtoErrCompRejectSent.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctMistypedCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctBadStructCompGP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogLinkedIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctRetRsltUnexpRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnrecogInvIdREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntCompRjctUnexpRetErrREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapProtoErrCompRejectSent.setStatus(
        "current"
    )

ciscoGtcapTCUserErrRejectRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 5)
)
ciscoGtcapTCUserErrRejectRcvd.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctDupInvIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctResourceLimitIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctInitReleaseIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctLinkedRespUnexpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpLinkedOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapTCUserErrRejectRcvd.setStatus(
        "current"
    )

ciscoGtcapTCUserErrRejectSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 6)
)
ciscoGtcapTCUserErrRejectSent.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapTCUser"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctDupInvIdIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctResourceLimitIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctInitReleaseIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctLinkedRespUnexpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpLinkedOpIP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnrecogErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctUnexpErrREP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamRRP"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntUsrRjctMistypedParamREP"))
)
if mibBuilder.loadTexts:
    ciscoGtcapTCUserErrRejectSent.setStatus(
        "current"
    )

ciscoGtcapActiveTranExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 0, 7)
)
ciscoGtcapActiveTranExceedThreshold.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapNotifIntervalDuration"),
        ("CISCO-ITP-GTCAP-MIB", "cgtcapIntervalActiveTranExceeds"))
)
if mibBuilder.loadTexts:
    ciscoGtcapActiveTranExceedThreshold.setStatus(
        "current"
    )


# Notifications groups

ciscoGtcapNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 2, 10)
)
ciscoGtcapNotificationsGroup.setObjects(
      *(("CISCO-ITP-GTCAP-MIB", "ciscoGtcapProtoErrTranAbortRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapProtoErrTranAbortSent"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapProtoErrCompRejectRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapProtoErrCompRejectSent"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapTCUserErrRejectRcvd"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapTCUserErrRejectSent"),
        ("CISCO-ITP-GTCAP-MIB", "ciscoGtcapActiveTranExceedThreshold"))
)
if mibBuilder.loadTexts:
    ciscoGtcapNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGtcapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 695, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGtcapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GTCAP-MIB",
    **{"CItpTcTCAPUser": CItpTcTCAPUser,
       "ciscoGtcapMIB": ciscoGtcapMIB,
       "ciscoGtcapMIBNotifs": ciscoGtcapMIBNotifs,
       "ciscoGtcapProtoErrTranAbortRcvd": ciscoGtcapProtoErrTranAbortRcvd,
       "ciscoGtcapProtoErrTranAbortSent": ciscoGtcapProtoErrTranAbortSent,
       "ciscoGtcapProtoErrCompRejectRcvd": ciscoGtcapProtoErrCompRejectRcvd,
       "ciscoGtcapProtoErrCompRejectSent": ciscoGtcapProtoErrCompRejectSent,
       "ciscoGtcapTCUserErrRejectRcvd": ciscoGtcapTCUserErrRejectRcvd,
       "ciscoGtcapTCUserErrRejectSent": ciscoGtcapTCUserErrRejectSent,
       "ciscoGtcapActiveTranExceedThreshold": ciscoGtcapActiveTranExceedThreshold,
       "ciscoGtcapMIBObjects": ciscoGtcapMIBObjects,
       "cgtcapScalars": cgtcapScalars,
       "cgtcapTranErrorNotifEnabled": cgtcapTranErrorNotifEnabled,
       "cgtcapCompErrorNotifEnabled": cgtcapCompErrorNotifEnabled,
       "cgtcapUsrErrorNotifEnabled": cgtcapUsrErrorNotifEnabled,
       "cgtcapThreshldExcdNotifEnabled": cgtcapThreshldExcdNotifEnabled,
       "cgtcapNotifWindowTime": cgtcapNotifWindowTime,
       "cgtcapUtilSampleInterval": cgtcapUtilSampleInterval,
       "cgtcapStatsInterval": cgtcapStatsInterval,
       "cgtcapInst": cgtcapInst,
       "cgtcapInstTable": cgtcapInstTable,
       "cgtcapInstTableEntry": cgtcapInstTableEntry,
       "cgtcapInstTotalTCMsgsSent": cgtcapInstTotalTCMsgsSent,
       "cgtcapInstTotalTCMsgsRcvd": cgtcapInstTotalTCMsgsRcvd,
       "cgtcapInstTotalCompSent": cgtcapInstTotalCompSent,
       "cgtcapInstTotalCompRcvd": cgtcapInstTotalCompRcvd,
       "cgtcapInstActiveExceedThresholds": cgtcapInstActiveExceedThresholds,
       "cgtcapInstUnidirectionalTranRcvd": cgtcapInstUnidirectionalTranRcvd,
       "cgtcapInstUnidirectionalTranSent": cgtcapInstUnidirectionalTranSent,
       "cgtcapInstBeginQueryTranRcvd": cgtcapInstBeginQueryTranRcvd,
       "cgtcapInstBeginQueryTranSent": cgtcapInstBeginQueryTranSent,
       "cgtcapInstBeginQueryWOPermTranRcvd": cgtcapInstBeginQueryWOPermTranRcvd,
       "cgtcapInstBeginQueryWOPermTranSent": cgtcapInstBeginQueryWOPermTranSent,
       "cgtcapInstEndResponseTranRcvd": cgtcapInstEndResponseTranRcvd,
       "cgtcapInstEndResponseTranSent": cgtcapInstEndResponseTranSent,
       "cgtcapInstContinueConvTranRcvd": cgtcapInstContinueConvTranRcvd,
       "cgtcapInstContinueConvTranSent": cgtcapInstContinueConvTranSent,
       "cgtcapInstContConvWOPermTranRcvd": cgtcapInstContConvWOPermTranRcvd,
       "cgtcapInstContConvWOPermTranSent": cgtcapInstContConvWOPermTranSent,
       "cgtcapInstAbortTranRcvd": cgtcapInstAbortTranRcvd,
       "cgtcapInstAbortTranSent": cgtcapInstAbortTranSent,
       "cgtcapInstClass1TCLocalCancelInd": cgtcapInstClass1TCLocalCancelInd,
       "cgtcapInstTotalDiscardsAllReasons": cgtcapInstTotalDiscardsAllReasons,
       "cgtcapInstProviderAbortsRcvd": cgtcapInstProviderAbortsRcvd,
       "cgtcapInstTotalRejectsRcvd": cgtcapInstTotalRejectsRcvd,
       "cgtcapInstTotalTransactionErr": cgtcapInstTotalTransactionErr,
       "cgtcapUtil": cgtcapUtil,
       "cgtcapUtilTable": cgtcapUtilTable,
       "cgtcapUtilTableEntry": cgtcapUtilTableEntry,
       "cgtcapUtilSlot": cgtcapUtilSlot,
       "cgtcapUser": cgtcapUser,
       "cgtcapNewTransInInterval": cgtcapNewTransInInterval,
       "cgtcapMeanOpenTransIdInInterval": cgtcapMeanOpenTransIdInInterval,
       "cgtcapCumulativeMeanDurationOfTran": cgtcapCumulativeMeanDurationOfTran,
       "cgtcapMaxOpenTransIdInInterval": cgtcapMaxOpenTransIdInInterval,
       "cgtcapUtilEndTimestamp": cgtcapUtilEndTimestamp,
       "cgtcapUtilPhysicalIndex": cgtcapUtilPhysicalIndex,
       "cgtcapPrErrTranRcvd": cgtcapPrErrTranRcvd,
       "cgtcapProtoTranRcvdErrorsTable": cgtcapProtoTranRcvdErrorsTable,
       "cgtcapProtoTranRcvdErrorsTableEntry": cgtcapProtoTranRcvdErrorsTableEntry,
       "cgtcapPrTranAbrtRcvdUnrecogMsgType": cgtcapPrTranAbrtRcvdUnrecogMsgType,
       "cgtcapPrTranAbrtRcvdIncorrectTP": cgtcapPrTranAbrtRcvdIncorrectTP,
       "cgtcapPrTranAbrtRcvdBadFmtTP": cgtcapPrTranAbrtRcvdBadFmtTP,
       "cgtcapPrTranAbrtRcvdUnrecogTID": cgtcapPrTranAbrtRcvdUnrecogTID,
       "cgtcapPrTranAbrtRcvdResrcLimit": cgtcapPrTranAbrtRcvdResrcLimit,
       "cgtcapPrErrTranSent": cgtcapPrErrTranSent,
       "cgtcapProtoTranSentErrorsTable": cgtcapProtoTranSentErrorsTable,
       "cgtcapProtoTranSentErrorsTableEntry": cgtcapProtoTranSentErrorsTableEntry,
       "cgtcapPrTranAbrtSentUnrecogMsgType": cgtcapPrTranAbrtSentUnrecogMsgType,
       "cgtcapPrTranAbrtSentIncorrectTP": cgtcapPrTranAbrtSentIncorrectTP,
       "cgtcapPrTranAbrtSentBadFmtTP": cgtcapPrTranAbrtSentBadFmtTP,
       "cgtcapPrTranAbrtSentUnrecogTID": cgtcapPrTranAbrtSentUnrecogTID,
       "cgtcapPrTranAbrtSentResrcLimit": cgtcapPrTranAbrtSentResrcLimit,
       "cgtcapPrErrComp": cgtcapPrErrComp,
       "cgtcapProtoCompErrorsTable": cgtcapProtoCompErrorsTable,
       "cgtcapProtoCompErrorsTableEntry": cgtcapProtoCompErrorsTableEntry,
       "cgtcapPrCompRjctRcvdUnrecogCompGP": cgtcapPrCompRjctRcvdUnrecogCompGP,
       "cgtcapPrCompRjctSentUnrecogCompGP": cgtcapPrCompRjctSentUnrecogCompGP,
       "cgtcapPrCompRjctRcvdMistypedCompGP": cgtcapPrCompRjctRcvdMistypedCompGP,
       "cgtcapPrCompRjctSentMistypedCompGP": cgtcapPrCompRjctSentMistypedCompGP,
       "cgtcapPrCompRjctRcvdBadStructCompGP": cgtcapPrCompRjctRcvdBadStructCompGP,
       "cgtcapPrCompRjctSentBadStructCompGP": cgtcapPrCompRjctSentBadStructCompGP,
       "cgtcapPrCompRjctRcvdUnrecogLinkedIdIP": cgtcapPrCompRjctRcvdUnrecogLinkedIdIP,
       "cgtcapPrCompRjctSentUnrecogLinkedIdIP": cgtcapPrCompRjctSentUnrecogLinkedIdIP,
       "cgtcapPrCompRjctRcvdUnrecogInvIdRRP": cgtcapPrCompRjctRcvdUnrecogInvIdRRP,
       "cgtcapPrCompRjctSentUnrecogInvIdRRP": cgtcapPrCompRjctSentUnrecogInvIdRRP,
       "cgtcapPrCompRjctRcvdRetRsltUnexpRRP": cgtcapPrCompRjctRcvdRetRsltUnexpRRP,
       "cgtcapPrCompRjctSentRetRsltUnexpRRP": cgtcapPrCompRjctSentRetRsltUnexpRRP,
       "cgtcapPrCompRjctRcvdUnrecogInvIdREP": cgtcapPrCompRjctRcvdUnrecogInvIdREP,
       "cgtcapPrCompRjctSentUnrecogInvIdREP": cgtcapPrCompRjctSentUnrecogInvIdREP,
       "cgtcapPrCompRjctRcvdUnexpRetErrREP": cgtcapPrCompRjctRcvdUnexpRetErrREP,
       "cgtcapPrCompRjctSentUnexpRetErrREP": cgtcapPrCompRjctSentUnexpRetErrREP,
       "cgtcapUsrErrRcvd": cgtcapUsrErrRcvd,
       "cgtcapUsrRjctRcvdErrorsTable": cgtcapUsrRjctRcvdErrorsTable,
       "cgtcapUsrRjctRcvdErrorsTableEntry": cgtcapUsrRjctRcvdErrorsTableEntry,
       "cgtcapUsrRjctRcvdDupInvIdIP": cgtcapUsrRjctRcvdDupInvIdIP,
       "cgtcapUsrRjctRcvdUnrecogOpIP": cgtcapUsrRjctRcvdUnrecogOpIP,
       "cgtcapUsrRjctRcvdMistypedParamIP": cgtcapUsrRjctRcvdMistypedParamIP,
       "cgtcapUsrRjctRcvdResourceLimitIP": cgtcapUsrRjctRcvdResourceLimitIP,
       "cgtcapUsrRjctRcvdInitReleaseIP": cgtcapUsrRjctRcvdInitReleaseIP,
       "cgtcapUsrRjctRcvdLinkedRespUnexpIP": cgtcapUsrRjctRcvdLinkedRespUnexpIP,
       "cgtcapUsrRjctRcvdUnexpLinkedOpIP": cgtcapUsrRjctRcvdUnexpLinkedOpIP,
       "cgtcapUsrRjctRcvdUnrecogErrREP": cgtcapUsrRjctRcvdUnrecogErrREP,
       "cgtcapUsrRjctRcvdUnexpErrREP": cgtcapUsrRjctRcvdUnexpErrREP,
       "cgtcapUsrRjctRcvdMistypedParamRRP": cgtcapUsrRjctRcvdMistypedParamRRP,
       "cgtcapUsrRjctRcvdMistypedParamREP": cgtcapUsrRjctRcvdMistypedParamREP,
       "cgtcapUsrErrSent": cgtcapUsrErrSent,
       "cgtcapUsrRjctSentErrorsTable": cgtcapUsrRjctSentErrorsTable,
       "cgtcapUsrRjctSentErrorsTableEntry": cgtcapUsrRjctSentErrorsTableEntry,
       "cgtcapUsrRjctSentDupInvIdIP": cgtcapUsrRjctSentDupInvIdIP,
       "cgtcapUsrRjctSentUnrecogOpIP": cgtcapUsrRjctSentUnrecogOpIP,
       "cgtcapUsrRjctSentMistypedParamIP": cgtcapUsrRjctSentMistypedParamIP,
       "cgtcapUsrRjctSentResourceLimitIP": cgtcapUsrRjctSentResourceLimitIP,
       "cgtcapUsrRjctSentInitReleaseIP": cgtcapUsrRjctSentInitReleaseIP,
       "cgtcapUsrRjctSentLinkedRespUnexpIP": cgtcapUsrRjctSentLinkedRespUnexpIP,
       "cgtcapUsrRjctSentUnexpLinkedOpIP": cgtcapUsrRjctSentUnexpLinkedOpIP,
       "cgtcapUsrRjctSentUnrecogErrREP": cgtcapUsrRjctSentUnrecogErrREP,
       "cgtcapUsrRjctSentUnexpErrREP": cgtcapUsrRjctSentUnexpErrREP,
       "cgtcapUsrRjctSentMistypedParamRRP": cgtcapUsrRjctSentMistypedParamRRP,
       "cgtcapUsrRjctSentMistypedParamREP": cgtcapUsrRjctSentMistypedParamREP,
       "cgtcapNotifInfo": cgtcapNotifInfo,
       "cgtcapNotifIntervalDuration": cgtcapNotifIntervalDuration,
       "cgtcapIntervalActiveTranExceeds": cgtcapIntervalActiveTranExceeds,
       "cgtcapTCUser": cgtcapTCUser,
       "cgtcapIntTranAbrtUnrecogMsgType": cgtcapIntTranAbrtUnrecogMsgType,
       "cgtcapIntTranAbrtIncorrectTP": cgtcapIntTranAbrtIncorrectTP,
       "cgtcapIntTranAbrtBadFmtTP": cgtcapIntTranAbrtBadFmtTP,
       "cgtcapIntTranAbrtUnrecogTID": cgtcapIntTranAbrtUnrecogTID,
       "cgtcapIntTranAbrtResrcLimit": cgtcapIntTranAbrtResrcLimit,
       "cgtcapIntCompRjctUnrecogCompGP": cgtcapIntCompRjctUnrecogCompGP,
       "cgtcapIntCompRjctMistypedCompGP": cgtcapIntCompRjctMistypedCompGP,
       "cgtcapIntCompRjctBadStructCompGP": cgtcapIntCompRjctBadStructCompGP,
       "cgtcapIntCompRjctUnrecogLinkedIdIP": cgtcapIntCompRjctUnrecogLinkedIdIP,
       "cgtcapIntCompRjctUnrecogInvIdRRP": cgtcapIntCompRjctUnrecogInvIdRRP,
       "cgtcapIntCompRjctRetRsltUnexpRRP": cgtcapIntCompRjctRetRsltUnexpRRP,
       "cgtcapIntCompRjctUnrecogInvIdREP": cgtcapIntCompRjctUnrecogInvIdREP,
       "cgtcapIntCompRjctUnexpRetErrREP": cgtcapIntCompRjctUnexpRetErrREP,
       "cgtcapIntUsrRjctDupInvIdIP": cgtcapIntUsrRjctDupInvIdIP,
       "cgtcapIntUsrRjctUnrecogOpIP": cgtcapIntUsrRjctUnrecogOpIP,
       "cgtcapIntUsrRjctMistypedParamIP": cgtcapIntUsrRjctMistypedParamIP,
       "cgtcapIntUsrRjctResourceLimitIP": cgtcapIntUsrRjctResourceLimitIP,
       "cgtcapIntUsrRjctInitReleaseIP": cgtcapIntUsrRjctInitReleaseIP,
       "cgtcapIntUsrRjctLinkedRespUnexpIP": cgtcapIntUsrRjctLinkedRespUnexpIP,
       "cgtcapIntUsrRjctUnexpLinkedOpIP": cgtcapIntUsrRjctUnexpLinkedOpIP,
       "cgtcapIntUsrRjctUnrecogErrREP": cgtcapIntUsrRjctUnrecogErrREP,
       "cgtcapIntUsrRjctUnexpErrREP": cgtcapIntUsrRjctUnexpErrREP,
       "cgtcapIntUsrRjctMistypedParamRRP": cgtcapIntUsrRjctMistypedParamRRP,
       "cgtcapIntUsrRjctMistypedParamREP": cgtcapIntUsrRjctMistypedParamREP,
       "ciscoGtcapMIBConform": ciscoGtcapMIBConform,
       "ciscoGtcapMIBCompliances": ciscoGtcapMIBCompliances,
       "ciscoGtcapMIBCompliance": ciscoGtcapMIBCompliance,
       "ciscoGtcapMIBGroups": ciscoGtcapMIBGroups,
       "ciscoGtcapGlobalEntryGroup": ciscoGtcapGlobalEntryGroup,
       "ciscoGtcapInstTableEntryGroup": ciscoGtcapInstTableEntryGroup,
       "ciscogtcapUtilTableEntryGroup": ciscogtcapUtilTableEntryGroup,
       "ciscoGtcapProtoTranRcvdErrorsGroup": ciscoGtcapProtoTranRcvdErrorsGroup,
       "ciscoGtcapProtoTranSentErrorsGroup": ciscoGtcapProtoTranSentErrorsGroup,
       "ciscoGtcapProtoCompErrorsGroup": ciscoGtcapProtoCompErrorsGroup,
       "ciscoGtcapUsrRjctRcvdErrorsGroup": ciscoGtcapUsrRjctRcvdErrorsGroup,
       "ciscoGtcapProtoCompSentErrorsGroup": ciscoGtcapProtoCompSentErrorsGroup,
       "ciscoGtcapNotifInfoGroup": ciscoGtcapNotifInfoGroup,
       "ciscoGtcapNotificationsGroup": ciscoGtcapNotificationsGroup}
)
