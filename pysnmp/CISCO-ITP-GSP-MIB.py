# SNMP MIB module (CISCO-ITP-GSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSP-MIB
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

(CItpTcAclId,
 CItpTcCLLI,
 CItpTcDisplayPC,
 CItpTcInstanceNumber,
 CItpTcLinkSLC,
 CItpTcLinkType,
 CItpTcLinksetId,
 CItpTcNetworkIndicator,
 CItpTcNetworkName,
 CItpTcPointCode,
 CItpTcPointCodeType,
 CItpTcQos,
 CItpTcRouteTableName,
 CItpTcServiceIndicator) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcAclId",
    "CItpTcCLLI",
    "CItpTcDisplayPC",
    "CItpTcInstanceNumber",
    "CItpTcLinkSLC",
    "CItpTcLinkType",
    "CItpTcLinksetId",
    "CItpTcNetworkIndicator",
    "CItpTcNetworkName",
    "CItpTcPointCode",
    "CItpTcPointCodeType",
    "CItpTcQos",
    "CItpTcRouteTableName",
    "CItpTcServiceIndicator")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336)
)
ciscoGspMIB.setRevisions(
        ("2009-12-31 00:00",
         "2009-09-12 00:00",
         "2009-05-25 00:00",
         "2008-05-07 00:00",
         "2005-10-21 00:00",
         "2005-02-24 00:00",
         "2003-07-16 00:00",
         "2003-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgspSequenceNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CgspSampleInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )



class CgspPercentThreshold(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CgspLinkTestResults(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("badPattern", 6),
          ("failed", 8),
          ("incorrectNi", 5),
          ("incorrectOpc", 2),
          ("incorrectSlc", 4),
          ("noErrors", 0),
          ("nonAdjacent", 7),
          ("undefinedOpc", 1),
          ("undefinedSlc", 3))
    )



class CgspLinkUtilization(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class CgspLinkCapacity(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(56000, 2147483647),
    )



class CgspProfileName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )



class CgspLinkUtilizationState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overThreshold", 2),
          ("unMonitored", 0),
          ("underThreshold", 1))
    )



class CgspTimerNumbers(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("timerLinkActRetry", 37),
          ("timerLinkMessag1", 36),
          ("timerLinkTest", 35),
          ("timerMtp2T01", 38),
          ("timerMtp2T02", 39),
          ("timerMtp2T03", 40),
          ("timerMtp2T04E", 42),
          ("timerMtp2T04N", 41),
          ("timerMtp2T05", 43),
          ("timerMtp2T06", 44),
          ("timerMtp2T07", 45),
          ("timerMtp3T01", 1),
          ("timerMtp3T02", 2),
          ("timerMtp3T03", 3),
          ("timerMtp3T04", 4),
          ("timerMtp3T05", 5),
          ("timerMtp3T06", 6),
          ("timerMtp3T07", 7),
          ("timerMtp3T08", 8),
          ("timerMtp3T09", 9),
          ("timerMtp3T10", 10),
          ("timerMtp3T11", 11),
          ("timerMtp3T12", 12),
          ("timerMtp3T13", 13),
          ("timerMtp3T14", 14),
          ("timerMtp3T15", 15),
          ("timerMtp3T16", 16),
          ("timerMtp3T17", 17),
          ("timerMtp3T18", 18),
          ("timerMtp3T19", 19),
          ("timerMtp3T20", 20),
          ("timerMtp3T21", 21),
          ("timerMtp3T22", 22),
          ("timerMtp3T23", 23),
          ("timerMtp3T24", 24),
          ("timerMtp3T25", 25),
          ("timerMtp3T26", 26),
          ("timerMtp3T27", 27),
          ("timerMtp3T28", 28),
          ("timerMtp3T29", 29),
          ("timerMtp3T30", 30),
          ("timerMtp3T31", 31),
          ("timerMtp3T32", 32),
          ("timerMtp3T33", 33),
          ("timerMtp3T34", 34))
    )



class CgspTimerValue(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class CgspSS7Variant(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("china", 3),
          ("itu", 2),
          ("ntt", 4),
          ("ttc", 5),
          ("unknown", 0))
    )



class CgspDisplayInstanceUserPart(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class CItpTcSccpWrrOption(Integer32, TextualConvention):
    status = "current"
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
        *(("cgpaSls", 1),
          ("opc", 3),
          ("opcSls", 2),
          ("sls", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGspMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGspMIBNotifs = _CiscoGspMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0)
)
_CiscoGspMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGspMIBObjects = _CiscoGspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1)
)
_CgspScalars_ObjectIdentity = ObjectIdentity
cgspScalars = _CgspScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1)
)
_CgspCLLICode_Type = CItpTcCLLI
_CgspCLLICode_Object = MibScalar
cgspCLLICode = _CgspCLLICode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 1),
    _CgspCLLICode_Type()
)
cgspCLLICode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspCLLICode.setStatus("current")


class _CgspUtilSampleInterval_Type(CgspSampleInterval):
    """Custom type cgspUtilSampleInterval based on CgspSampleInterval"""
    defaultValue = 300


_CgspUtilSampleInterval_Object = MibScalar
cgspUtilSampleInterval = _CgspUtilSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 2),
    _CgspUtilSampleInterval_Type()
)
cgspUtilSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspUtilSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgspUtilSampleInterval.setUnits("seconds")


class _CgspUtilThreshold_Type(CgspPercentThreshold):
    """Custom type cgspUtilThreshold based on CgspPercentThreshold"""
    defaultValue = 40


_CgspUtilThreshold_Object = MibScalar
cgspUtilThreshold = _CgspUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 3),
    _CgspUtilThreshold_Type()
)
cgspUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspUtilThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cgspUtilThreshold.setUnits("percent")


class _CgspUtilAbateDelta_Type(CgspPercentThreshold):
    """Custom type cgspUtilAbateDelta based on CgspPercentThreshold"""
    defaultValue = 0


_CgspUtilAbateDelta_Object = MibScalar
cgspUtilAbateDelta = _CgspUtilAbateDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 4),
    _CgspUtilAbateDelta_Type()
)
cgspUtilAbateDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspUtilAbateDelta.setStatus("current")
if mibBuilder.loadTexts:
    cgspUtilAbateDelta.setUnits("percent")
_CgspPlanCapacityDefault_Type = CgspLinkCapacity
_CgspPlanCapacityDefault_Object = MibScalar
cgspPlanCapacityDefault = _CgspPlanCapacityDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 5),
    _CgspPlanCapacityDefault_Type()
)
cgspPlanCapacityDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspPlanCapacityDefault.setStatus("current")
if mibBuilder.loadTexts:
    cgspPlanCapacityDefault.setUnits("bits per second")
_CgspEventSequenceNumber_Type = Counter32
_CgspEventSequenceNumber_Object = MibScalar
cgspEventSequenceNumber = _CgspEventSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 6),
    _CgspEventSequenceNumber_Type()
)
cgspEventSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspEventSequenceNumber.setStatus("current")
if mibBuilder.loadTexts:
    cgspEventSequenceNumber.setUnits("events")


class _CgspUPUNotifWindowTime_Type(Integer32):
    """Custom type cgspUPUNotifWindowTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CgspUPUNotifWindowTime_Type.__name__ = "Integer32"
_CgspUPUNotifWindowTime_Object = MibScalar
cgspUPUNotifWindowTime = _CgspUPUNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 1, 7),
    _CgspUPUNotifWindowTime_Type()
)
cgspUPUNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspUPUNotifWindowTime.setStatus("current")
if mibBuilder.loadTexts:
    cgspUPUNotifWindowTime.setUnits("seconds")
_CgspProfile_ObjectIdentity = ObjectIdentity
cgspProfile = _CgspProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2)
)
_CgspProfileTable_Object = MibTable
cgspProfileTable = _CgspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgspProfileTable.setStatus("current")
_CgspProfileTableEntry_Object = MibTableRow
cgspProfileTableEntry = _CgspProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1)
)
cgspProfileTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspProfileName"),
)
if mibBuilder.loadTexts:
    cgspProfileTableEntry.setStatus("current")
_CgspProfileName_Type = CgspProfileName
_CgspProfileName_Object = MibTableColumn
cgspProfileName = _CgspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1, 1),
    _CgspProfileName_Type()
)
cgspProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspProfileName.setStatus("current")
_CgspProfileVariant_Type = CgspSS7Variant
_CgspProfileVariant_Object = MibTableColumn
cgspProfileVariant = _CgspProfileVariant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1, 2),
    _CgspProfileVariant_Type()
)
cgspProfileVariant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileVariant.setStatus("current")


class _CgspProfileMtp2BundleTimer_Type(Integer32):
    """Custom type cgspProfileMtp2BundleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 10000),
    )


_CgspProfileMtp2BundleTimer_Type.__name__ = "Integer32"
_CgspProfileMtp2BundleTimer_Object = MibTableColumn
cgspProfileMtp2BundleTimer = _CgspProfileMtp2BundleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1, 3),
    _CgspProfileMtp2BundleTimer_Type()
)
cgspProfileMtp2BundleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileMtp2BundleTimer.setStatus("current")


class _CgspProfileMtp2SendQueueDepth_Type(Integer32):
    """Custom type cgspProfileMtp2SendQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 32000),
    )


_CgspProfileMtp2SendQueueDepth_Type.__name__ = "Integer32"
_CgspProfileMtp2SendQueueDepth_Object = MibTableColumn
cgspProfileMtp2SendQueueDepth = _CgspProfileMtp2SendQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1, 4),
    _CgspProfileMtp2SendQueueDepth_Type()
)
cgspProfileMtp2SendQueueDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileMtp2SendQueueDepth.setStatus("current")
_CgspProfileRowStatus_Type = RowStatus
_CgspProfileRowStatus_Object = MibTableColumn
cgspProfileRowStatus = _CgspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 1, 1, 5),
    _CgspProfileRowStatus_Type()
)
cgspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileRowStatus.setStatus("current")
_CgspProfileTimerTable_Object = MibTable
cgspProfileTimerTable = _CgspProfileTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgspProfileTimerTable.setStatus("current")
_CgspProfileTimerTableEntry_Object = MibTableRow
cgspProfileTimerTableEntry = _CgspProfileTimerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 2, 1)
)
cgspProfileTimerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspProfileTimerNumber"),
)
if mibBuilder.loadTexts:
    cgspProfileTimerTableEntry.setStatus("current")
_CgspProfileTimerNumber_Type = CgspTimerNumbers
_CgspProfileTimerNumber_Object = MibTableColumn
cgspProfileTimerNumber = _CgspProfileTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 2, 1, 1),
    _CgspProfileTimerNumber_Type()
)
cgspProfileTimerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspProfileTimerNumber.setStatus("current")
_CgspProfileTimerValue_Type = CgspTimerValue
_CgspProfileTimerValue_Object = MibTableColumn
cgspProfileTimerValue = _CgspProfileTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 2, 1, 2),
    _CgspProfileTimerValue_Type()
)
cgspProfileTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    cgspProfileTimerValue.setUnits("milliseconds")
_CgspProfileTimerRowStatus_Type = RowStatus
_CgspProfileTimerRowStatus_Object = MibTableColumn
cgspProfileTimerRowStatus = _CgspProfileTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 2, 2, 1, 3),
    _CgspProfileTimerRowStatus_Type()
)
cgspProfileTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspProfileTimerRowStatus.setStatus("current")
_CgspInstance_ObjectIdentity = ObjectIdentity
cgspInstance = _CgspInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3)
)
_CgspInstanceTable_Object = MibTable
cgspInstanceTable = _CgspInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgspInstanceTable.setStatus("current")
_CgspInstanceTableEntry_Object = MibTableRow
cgspInstanceTableEntry = _CgspInstanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1)
)
cgspInstanceTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgspInstanceTableEntry.setStatus("current")
_CgspInstNetwork_Type = CItpTcNetworkName
_CgspInstNetwork_Object = MibTableColumn
cgspInstNetwork = _CgspInstNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 1),
    _CgspInstNetwork_Type()
)
cgspInstNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspInstNetwork.setStatus("current")
_CgspInstNetworkIndicator_Type = CItpTcNetworkIndicator
_CgspInstNetworkIndicator_Object = MibTableColumn
cgspInstNetworkIndicator = _CgspInstNetworkIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 2),
    _CgspInstNetworkIndicator_Type()
)
cgspInstNetworkIndicator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstNetworkIndicator.setStatus("current")
_CgspInstVariant_Type = CgspSS7Variant
_CgspInstVariant_Object = MibTableColumn
cgspInstVariant = _CgspInstVariant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 3),
    _CgspInstVariant_Type()
)
cgspInstVariant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstVariant.setStatus("current")


class _CgspInstDisplayName_Type(SnmpAdminString):
    """Custom type cgspInstDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CgspInstDisplayName_Type.__name__ = "SnmpAdminString"
_CgspInstDisplayName_Object = MibTableColumn
cgspInstDisplayName = _CgspInstDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 4),
    _CgspInstDisplayName_Type()
)
cgspInstDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstDisplayName.setStatus("current")


class _CgspInstDescription_Type(SnmpAdminString):
    """Custom type cgspInstDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CgspInstDescription_Type.__name__ = "SnmpAdminString"
_CgspInstDescription_Object = MibTableColumn
cgspInstDescription = _CgspInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 5),
    _CgspInstDescription_Type()
)
cgspInstDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstDescription.setStatus("current")


class _CgspInstTFR_Type(TruthValue):
    """Custom type cgspInstTFR based on TruthValue"""


_CgspInstTFR_Object = MibTableColumn
cgspInstTFR = _CgspInstTFR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 6),
    _CgspInstTFR_Type()
)
cgspInstTFR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstTFR.setStatus("current")


class _CgspInstCongestionsLevels_Type(TruthValue):
    """Custom type cgspInstCongestionsLevels based on TruthValue"""


_CgspInstCongestionsLevels_Object = MibTableColumn
cgspInstCongestionsLevels = _CgspInstCongestionsLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 7),
    _CgspInstCongestionsLevels_Type()
)
cgspInstCongestionsLevels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstCongestionsLevels.setStatus("current")


class _CgspInstFastRestart_Type(TruthValue):
    """Custom type cgspInstFastRestart based on TruthValue"""


_CgspInstFastRestart_Object = MibTableColumn
cgspInstFastRestart = _CgspInstFastRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 8),
    _CgspInstFastRestart_Type()
)
cgspInstFastRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstFastRestart.setStatus("current")


class _CgspInstDistSccpUnseq_Type(TruthValue):
    """Custom type cgspInstDistSccpUnseq based on TruthValue"""


_CgspInstDistSccpUnseq_Object = MibTableColumn
cgspInstDistSccpUnseq = _CgspInstDistSccpUnseq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 9),
    _CgspInstDistSccpUnseq_Type()
)
cgspInstDistSccpUnseq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstDistSccpUnseq.setStatus("current")


class _CgspInstSummaryRoutingException_Type(TruthValue):
    """Custom type cgspInstSummaryRoutingException based on TruthValue"""


_CgspInstSummaryRoutingException_Object = MibTableColumn
cgspInstSummaryRoutingException = _CgspInstSummaryRoutingException_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 10),
    _CgspInstSummaryRoutingException_Type()
)
cgspInstSummaryRoutingException.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstSummaryRoutingException.setStatus("current")
_CgspInstNumber_Type = CItpTcInstanceNumber
_CgspInstNumber_Object = MibTableColumn
cgspInstNumber = _CgspInstNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 11),
    _CgspInstNumber_Type()
)
cgspInstNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspInstNumber.setStatus("current")
_CgspInstRouteTableName_Type = CItpTcRouteTableName
_CgspInstRouteTableName_Object = MibTableColumn
cgspInstRouteTableName = _CgspInstRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 12),
    _CgspInstRouteTableName_Type()
)
cgspInstRouteTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstRouteTableName.setStatus("current")
_CgspInstRowStatus_Type = RowStatus
_CgspInstRowStatus_Object = MibTableColumn
cgspInstRowStatus = _CgspInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 13),
    _CgspInstRowStatus_Type()
)
cgspInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstRowStatus.setStatus("current")


class _CgspInstSccpWrrOpcShift_Type(Unsigned32):
    """Custom type cgspInstSccpWrrOpcShift based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CgspInstSccpWrrOpcShift_Type.__name__ = "Unsigned32"
_CgspInstSccpWrrOpcShift_Object = MibTableColumn
cgspInstSccpWrrOpcShift = _CgspInstSccpWrrOpcShift_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 14),
    _CgspInstSccpWrrOpcShift_Type()
)
cgspInstSccpWrrOpcShift.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstSccpWrrOpcShift.setStatus("current")
_CgspInstSccpWrrOption_Type = CItpTcSccpWrrOption
_CgspInstSccpWrrOption_Object = MibTableColumn
cgspInstSccpWrrOption = _CgspInstSccpWrrOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 1, 1, 15),
    _CgspInstSccpWrrOption_Type()
)
cgspInstSccpWrrOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstSccpWrrOption.setStatus("current")
_CgspInstTimerTable_Object = MibTable
cgspInstTimerTable = _CgspInstTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cgspInstTimerTable.setStatus("current")
_CgspInstTimerTableEntry_Object = MibTableRow
cgspInstTimerTableEntry = _CgspInstTimerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 2, 1)
)
cgspInstTimerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspInstTimerNumber"),
)
if mibBuilder.loadTexts:
    cgspInstTimerTableEntry.setStatus("current")
_CgspInstTimerNumber_Type = CgspTimerNumbers
_CgspInstTimerNumber_Object = MibTableColumn
cgspInstTimerNumber = _CgspInstTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 2, 1, 1),
    _CgspInstTimerNumber_Type()
)
cgspInstTimerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspInstTimerNumber.setStatus("current")
_CgspInstTimerValue_Type = CgspTimerValue
_CgspInstTimerValue_Object = MibTableColumn
cgspInstTimerValue = _CgspInstTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 2, 1, 2),
    _CgspInstTimerValue_Type()
)
cgspInstTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    cgspInstTimerValue.setUnits("milliseconds")
_CgspInstTimerRowStatus_Type = RowStatus
_CgspInstTimerRowStatus_Object = MibTableColumn
cgspInstTimerRowStatus = _CgspInstTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 2, 1, 3),
    _CgspInstTimerRowStatus_Type()
)
cgspInstTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspInstTimerRowStatus.setStatus("current")
_CgspInstUPUTable_Object = MibTable
cgspInstUPUTable = _CgspInstUPUTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cgspInstUPUTable.setStatus("current")
_CgspInstUPUTableEntry_Object = MibTableRow
cgspInstUPUTableEntry = _CgspInstUPUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3, 1)
)
cgspInstUPUTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspMtp3SI"),
)
if mibBuilder.loadTexts:
    cgspInstUPUTableEntry.setStatus("current")
_CgspMtp3SI_Type = CItpTcServiceIndicator
_CgspMtp3SI_Object = MibTableColumn
cgspMtp3SI = _CgspMtp3SI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3, 1, 1),
    _CgspMtp3SI_Type()
)
cgspMtp3SI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspMtp3SI.setStatus("current")
_CgspInstSIUPUReceived_Type = Counter32
_CgspInstSIUPUReceived_Object = MibTableColumn
cgspInstSIUPUReceived = _CgspInstSIUPUReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3, 1, 2),
    _CgspInstSIUPUReceived_Type()
)
cgspInstSIUPUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspInstSIUPUReceived.setStatus("current")
if mibBuilder.loadTexts:
    cgspInstSIUPUReceived.setUnits("MSUs")
_CgspInstSIUPUTransmitted_Type = Counter32
_CgspInstSIUPUTransmitted_Object = MibTableColumn
cgspInstSIUPUTransmitted = _CgspInstSIUPUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3, 1, 3),
    _CgspInstSIUPUTransmitted_Type()
)
cgspInstSIUPUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspInstSIUPUTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    cgspInstSIUPUTransmitted.setUnits("MSUs")
_CgspInstUserPartDisplay_Type = CgspDisplayInstanceUserPart
_CgspInstUserPartDisplay_Object = MibTableColumn
cgspInstUserPartDisplay = _CgspInstUserPartDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 3, 3, 1, 4),
    _CgspInstUserPartDisplay_Type()
)
cgspInstUserPartDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspInstUserPartDisplay.setStatus("current")
_CgspPointCode_ObjectIdentity = ObjectIdentity
cgspPointCode = _CgspPointCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4)
)
_CgspPointCodeTable_Object = MibTable
cgspPointCodeTable = _CgspPointCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgspPointCodeTable.setStatus("current")
_CgspPointCodeTableEntry_Object = MibTableRow
cgspPointCodeTableEntry = _CgspPointCodeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1)
)
cgspPointCodeTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspPointCodeNi"),
    (0, "CISCO-ITP-GSP-MIB", "cgspPointCodeBin"),
)
if mibBuilder.loadTexts:
    cgspPointCodeTableEntry.setStatus("current")
_CgspPointCodeNi_Type = CItpTcNetworkIndicator
_CgspPointCodeNi_Object = MibTableColumn
cgspPointCodeNi = _CgspPointCodeNi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1, 1),
    _CgspPointCodeNi_Type()
)
cgspPointCodeNi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspPointCodeNi.setStatus("current")
_CgspPointCodeBin_Type = CItpTcPointCode
_CgspPointCodeBin_Object = MibTableColumn
cgspPointCodeBin = _CgspPointCodeBin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1, 2),
    _CgspPointCodeBin_Type()
)
cgspPointCodeBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspPointCodeBin.setStatus("current")
_CgspPointCodeType_Type = CItpTcPointCodeType
_CgspPointCodeType_Object = MibTableColumn
cgspPointCodeType = _CgspPointCodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1, 3),
    _CgspPointCodeType_Type()
)
cgspPointCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspPointCodeType.setStatus("current")
_CgspPointCodeDisplay_Type = CItpTcDisplayPC
_CgspPointCodeDisplay_Object = MibTableColumn
cgspPointCodeDisplay = _CgspPointCodeDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1, 4),
    _CgspPointCodeDisplay_Type()
)
cgspPointCodeDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspPointCodeDisplay.setStatus("current")
_CgspPointCodeRowStatus_Type = RowStatus
_CgspPointCodeRowStatus_Object = MibTableColumn
cgspPointCodeRowStatus = _CgspPointCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 4, 1, 1, 5),
    _CgspPointCodeRowStatus_Type()
)
cgspPointCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspPointCodeRowStatus.setStatus("current")
_CgspLinkset_ObjectIdentity = ObjectIdentity
cgspLinkset = _CgspLinkset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5)
)
_CgspLinksetTable_Object = MibTable
cgspLinksetTable = _CgspLinksetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgspLinksetTable.setStatus("current")
_CgspLinksetTableEntry_Object = MibTableRow
cgspLinksetTableEntry = _CgspLinksetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1)
)
cgspLinksetTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
)
if mibBuilder.loadTexts:
    cgspLinksetTableEntry.setStatus("current")
_CgspLinksetName_Type = CItpTcLinksetId
_CgspLinksetName_Object = MibTableColumn
cgspLinksetName = _CgspLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 1),
    _CgspLinksetName_Type()
)
cgspLinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinksetName.setStatus("current")
_CgspLinksetSourcePointCode_Type = CItpTcPointCode
_CgspLinksetSourcePointCode_Object = MibTableColumn
cgspLinksetSourcePointCode = _CgspLinksetSourcePointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 2),
    _CgspLinksetSourcePointCode_Type()
)
cgspLinksetSourcePointCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetSourcePointCode.setStatus("current")
_CgspLinksetSourceDisplayPC_Type = CItpTcDisplayPC
_CgspLinksetSourceDisplayPC_Object = MibTableColumn
cgspLinksetSourceDisplayPC = _CgspLinksetSourceDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 3),
    _CgspLinksetSourceDisplayPC_Type()
)
cgspLinksetSourceDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetSourceDisplayPC.setStatus("current")
_CgspLinksetAdjacentPointCode_Type = CItpTcPointCode
_CgspLinksetAdjacentPointCode_Object = MibTableColumn
cgspLinksetAdjacentPointCode = _CgspLinksetAdjacentPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 4),
    _CgspLinksetAdjacentPointCode_Type()
)
cgspLinksetAdjacentPointCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetAdjacentPointCode.setStatus("current")
_CgspLinksetAdjacentDisplayPC_Type = CItpTcDisplayPC
_CgspLinksetAdjacentDisplayPC_Object = MibTableColumn
cgspLinksetAdjacentDisplayPC = _CgspLinksetAdjacentDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 5),
    _CgspLinksetAdjacentDisplayPC_Type()
)
cgspLinksetAdjacentDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetAdjacentDisplayPC.setStatus("current")


class _CgspLinksetState_Type(Integer32):
    """Custom type cgspLinksetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("shutdown", 2),
          ("unavailable", 3))
    )


_CgspLinksetState_Type.__name__ = "Integer32"
_CgspLinksetState_Object = MibTableColumn
cgspLinksetState = _CgspLinksetState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 6),
    _CgspLinksetState_Type()
)
cgspLinksetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetState.setStatus("current")
_CgspLinksetInboundAcl_Type = CItpTcAclId
_CgspLinksetInboundAcl_Object = MibTableColumn
cgspLinksetInboundAcl = _CgspLinksetInboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 7),
    _CgspLinksetInboundAcl_Type()
)
cgspLinksetInboundAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetInboundAcl.setStatus("current")
_CgspLinksetOutboundAcl_Type = CItpTcAclId
_CgspLinksetOutboundAcl_Object = MibTableColumn
cgspLinksetOutboundAcl = _CgspLinksetOutboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 8),
    _CgspLinksetOutboundAcl_Type()
)
cgspLinksetOutboundAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetOutboundAcl.setStatus("current")


class _CgspLinksetAccountingMtp3_Type(TruthValue):
    """Custom type cgspLinksetAccountingMtp3 based on TruthValue"""


_CgspLinksetAccountingMtp3_Object = MibTableColumn
cgspLinksetAccountingMtp3 = _CgspLinksetAccountingMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 9),
    _CgspLinksetAccountingMtp3_Type()
)
cgspLinksetAccountingMtp3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetAccountingMtp3.setStatus("current")


class _CgspLinksetAccountingGtt_Type(TruthValue):
    """Custom type cgspLinksetAccountingGtt based on TruthValue"""


_CgspLinksetAccountingGtt_Object = MibTableColumn
cgspLinksetAccountingGtt = _CgspLinksetAccountingGtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 10),
    _CgspLinksetAccountingGtt_Type()
)
cgspLinksetAccountingGtt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetAccountingGtt.setStatus("current")
_CgspLinksetNumLinks_Type = Unsigned32
_CgspLinksetNumLinks_Object = MibTableColumn
cgspLinksetNumLinks = _CgspLinksetNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 11),
    _CgspLinksetNumLinks_Type()
)
cgspLinksetNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetNumLinks.setStatus("current")
_CgspLinksetDurationInService_Type = Counter32
_CgspLinksetDurationInService_Object = MibTableColumn
cgspLinksetDurationInService = _CgspLinksetDurationInService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 12),
    _CgspLinksetDurationInService_Type()
)
cgspLinksetDurationInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetDurationInService.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinksetDurationInService.setUnits("seconds")
_CgspLinksetDurationOutService_Type = Counter32
_CgspLinksetDurationOutService_Object = MibTableColumn
cgspLinksetDurationOutService = _CgspLinksetDurationOutService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 13),
    _CgspLinksetDurationOutService_Type()
)
cgspLinksetDurationOutService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetDurationOutService.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinksetDurationOutService.setUnits("seconds")


class _CgspLinksetActPriority_Type(Unsigned32):
    """Custom type cgspLinksetActPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CgspLinksetActPriority_Type.__name__ = "Unsigned32"
_CgspLinksetActPriority_Object = MibTableColumn
cgspLinksetActPriority = _CgspLinksetActPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 14),
    _CgspLinksetActPriority_Type()
)
cgspLinksetActPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetActPriority.setStatus("current")


class _CgspLinksetDisplayName_Type(SnmpAdminString):
    """Custom type cgspLinksetDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CgspLinksetDisplayName_Type.__name__ = "SnmpAdminString"
_CgspLinksetDisplayName_Object = MibTableColumn
cgspLinksetDisplayName = _CgspLinksetDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 15),
    _CgspLinksetDisplayName_Type()
)
cgspLinksetDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetDisplayName.setStatus("current")


class _CgspLinksetDescription_Type(SnmpAdminString):
    """Custom type cgspLinksetDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CgspLinksetDescription_Type.__name__ = "SnmpAdminString"
_CgspLinksetDescription_Object = MibTableColumn
cgspLinksetDescription = _CgspLinksetDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 16),
    _CgspLinksetDescription_Type()
)
cgspLinksetDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetDescription.setStatus("current")
_CgspLinksetRotateSlsEnable_Type = TruthValue
_CgspLinksetRotateSlsEnable_Object = MibTableColumn
cgspLinksetRotateSlsEnable = _CgspLinksetRotateSlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 17),
    _CgspLinksetRotateSlsEnable_Type()
)
cgspLinksetRotateSlsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetRotateSlsEnable.setStatus("current")


class _CgspLinksetRotateSlsShift_Type(Unsigned32):
    """Custom type cgspLinksetRotateSlsShift based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CgspLinksetRotateSlsShift_Type.__name__ = "Unsigned32"
_CgspLinksetRotateSlsShift_Object = MibTableColumn
cgspLinksetRotateSlsShift = _CgspLinksetRotateSlsShift_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 18),
    _CgspLinksetRotateSlsShift_Type()
)
cgspLinksetRotateSlsShift.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetRotateSlsShift.setStatus("current")
_CgspLinksetProfileName_Type = CgspProfileName
_CgspLinksetProfileName_Object = MibTableColumn
cgspLinksetProfileName = _CgspLinksetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 19),
    _CgspLinksetProfileName_Type()
)
cgspLinksetProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetProfileName.setStatus("current")
_CgspLinksetAdjacentInst_Type = CItpTcNetworkName
_CgspLinksetAdjacentInst_Object = MibTableColumn
cgspLinksetAdjacentInst = _CgspLinksetAdjacentInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 20),
    _CgspLinksetAdjacentInst_Type()
)
cgspLinksetAdjacentInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinksetAdjacentInst.setStatus("current")
_CgspLinksetRowStatus_Type = RowStatus
_CgspLinksetRowStatus_Object = MibTableColumn
cgspLinksetRowStatus = _CgspLinksetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 1, 1, 21),
    _CgspLinksetRowStatus_Type()
)
cgspLinksetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetRowStatus.setStatus("current")
_CgspLinksetTimerTable_Object = MibTable
cgspLinksetTimerTable = _CgspLinksetTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cgspLinksetTimerTable.setStatus("current")
_CgspLinksetTimerTableEntry_Object = MibTableRow
cgspLinksetTimerTableEntry = _CgspLinksetTimerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 2, 1)
)
cgspLinksetTimerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetTimerNumber"),
)
if mibBuilder.loadTexts:
    cgspLinksetTimerTableEntry.setStatus("current")
_CgspLinksetTimerNumber_Type = CgspTimerNumbers
_CgspLinksetTimerNumber_Object = MibTableColumn
cgspLinksetTimerNumber = _CgspLinksetTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 2, 1, 1),
    _CgspLinksetTimerNumber_Type()
)
cgspLinksetTimerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinksetTimerNumber.setStatus("current")
_CgspLinksetTimerValue_Type = CgspTimerValue
_CgspLinksetTimerValue_Object = MibTableColumn
cgspLinksetTimerValue = _CgspLinksetTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 2, 1, 2),
    _CgspLinksetTimerValue_Type()
)
cgspLinksetTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinksetTimerValue.setUnits("milliseconds")
_CgspLinksetTimerRowStatus_Type = RowStatus
_CgspLinksetTimerRowStatus_Object = MibTableColumn
cgspLinksetTimerRowStatus = _CgspLinksetTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 5, 2, 1, 3),
    _CgspLinksetTimerRowStatus_Type()
)
cgspLinksetTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinksetTimerRowStatus.setStatus("current")
_CgspLink_ObjectIdentity = ObjectIdentity
cgspLink = _CgspLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6)
)
_CgspLinkTable_Object = MibTable
cgspLinkTable = _CgspLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgspLinkTable.setStatus("current")
_CgspLinkTableEntry_Object = MibTableRow
cgspLinkTableEntry = _CgspLinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1)
)
cgspLinkTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkSlc"),
)
if mibBuilder.loadTexts:
    cgspLinkTableEntry.setStatus("current")
_CgspLinkSlc_Type = CItpTcLinkSLC
_CgspLinkSlc_Object = MibTableColumn
cgspLinkSlc = _CgspLinkSlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 1),
    _CgspLinkSlc_Type()
)
cgspLinkSlc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinkSlc.setStatus("current")


class _CgspLinkDescription_Type(SnmpAdminString):
    """Custom type cgspLinkDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CgspLinkDescription_Type.__name__ = "SnmpAdminString"
_CgspLinkDescription_Object = MibTableColumn
cgspLinkDescription = _CgspLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 2),
    _CgspLinkDescription_Type()
)
cgspLinkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkDescription.setStatus("current")


class _CgspLinkState_Type(Integer32):
    """Custom type cgspLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("failed", 2),
          ("shutdown", 3),
          ("unavailable", 4))
    )


_CgspLinkState_Type.__name__ = "Integer32"
_CgspLinkState_Object = MibTableColumn
cgspLinkState = _CgspLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 3),
    _CgspLinkState_Type()
)
cgspLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkState.setStatus("current")


class _CgspLinkReason_Type(Integer32):
    """Custom type cgspLinkReason based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("bufferNotAvailable", 21),
          ("cardInserted", 23),
          ("cardRemoved", 22),
          ("changeOverInProgress", 1),
          ("communicationLost", 19),
          ("configDownload", 25),
          ("connectionLost", 4),
          ("falseLinkCongestion", 24),
          ("linkAlignmentLost", 3),
          ("linkRestored", 34),
          ("linkTestFailure", 35),
          ("localBlocked", 30),
          ("localDisconnect", 5),
          ("localInhibit", 26),
          ("localUnBlocked", 31),
          ("localUninhibit", 27),
          ("mgmtDisconnectRequest", 2),
          ("noListenPosted", 20),
          ("peerNotReady", 18),
          ("protocolErrorBsn", 14),
          ("protocolErrorFib", 15),
          ("protocolErrorLssu", 17),
          ("protocolErrorSin", 16),
          ("provingFailure", 13),
          ("remoteBlocked", 32),
          ("remoteDisconnect", 6),
          ("remoteInhibit", 28),
          ("remoteUnblocked", 33),
          ("remoteUninhibit", 29),
          ("suermFailure", 7),
          ("t1Timeout", 8),
          ("t2Timeout", 9),
          ("t3Timeout", 10),
          ("t6Timeout", 11),
          ("t7Timeout", 12),
          ("unknown", 0))
    )


_CgspLinkReason_Type.__name__ = "Integer32"
_CgspLinkReason_Object = MibTableColumn
cgspLinkReason = _CgspLinkReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 4),
    _CgspLinkReason_Type()
)
cgspLinkReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkReason.setStatus("current")
_CgspLinkType_Type = CItpTcLinkType
_CgspLinkType_Object = MibTableColumn
cgspLinkType = _CgspLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 5),
    _CgspLinkType_Type()
)
cgspLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkType.setStatus("current")
_CgspLinkifIndex_Type = InterfaceIndexOrZero
_CgspLinkifIndex_Object = MibTableColumn
cgspLinkifIndex = _CgspLinkifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 6),
    _CgspLinkifIndex_Type()
)
cgspLinkifIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkifIndex.setStatus("current")


class _CgspLinkSctpAssociation_Type(Unsigned32):
    """Custom type cgspLinkSctpAssociation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkSctpAssociation_Type.__name__ = "Unsigned32"
_CgspLinkSctpAssociation_Object = MibTableColumn
cgspLinkSctpAssociation = _CgspLinkSctpAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 7),
    _CgspLinkSctpAssociation_Type()
)
cgspLinkSctpAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkSctpAssociation.setStatus("deprecated")
_CgspLinkXmitQueueDepth_Type = Gauge32
_CgspLinkXmitQueueDepth_Object = MibTableColumn
cgspLinkXmitQueueDepth = _CgspLinkXmitQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 8),
    _CgspLinkXmitQueueDepth_Type()
)
cgspLinkXmitQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkXmitQueueDepth.setStatus("current")
_CgspLinkXmitQueueDepthHigh_Type = Unsigned32
_CgspLinkXmitQueueDepthHigh_Object = MibTableColumn
cgspLinkXmitQueueDepthHigh = _CgspLinkXmitQueueDepthHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 9),
    _CgspLinkXmitQueueDepthHigh_Type()
)
cgspLinkXmitQueueDepthHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkXmitQueueDepthHigh.setStatus("current")
_CgspLinkXmitQueueDepthHighRT_Type = TimeStamp
_CgspLinkXmitQueueDepthHighRT_Object = MibTableColumn
cgspLinkXmitQueueDepthHighRT = _CgspLinkXmitQueueDepthHighRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 10),
    _CgspLinkXmitQueueDepthHighRT_Type()
)
cgspLinkXmitQueueDepthHighRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkXmitQueueDepthHighRT.setStatus("current")


class _CgspLinkCongestionState_Type(Unsigned32):
    """Custom type cgspLinkCongestionState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CgspLinkCongestionState_Type.__name__ = "Unsigned32"
_CgspLinkCongestionState_Object = MibTableColumn
cgspLinkCongestionState = _CgspLinkCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 11),
    _CgspLinkCongestionState_Type()
)
cgspLinkCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkCongestionState.setStatus("current")


class _CgspLinkCongestionAbate1_Type(Unsigned32):
    """Custom type cgspLinkCongestionAbate1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionAbate1_Type.__name__ = "Unsigned32"
_CgspLinkCongestionAbate1_Object = MibTableColumn
cgspLinkCongestionAbate1 = _CgspLinkCongestionAbate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 12),
    _CgspLinkCongestionAbate1_Type()
)
cgspLinkCongestionAbate1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionAbate1.setStatus("current")


class _CgspLinkCongestionAbate2_Type(Unsigned32):
    """Custom type cgspLinkCongestionAbate2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionAbate2_Type.__name__ = "Unsigned32"
_CgspLinkCongestionAbate2_Object = MibTableColumn
cgspLinkCongestionAbate2 = _CgspLinkCongestionAbate2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 13),
    _CgspLinkCongestionAbate2_Type()
)
cgspLinkCongestionAbate2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionAbate2.setStatus("current")


class _CgspLinkCongestionAbate3_Type(Unsigned32):
    """Custom type cgspLinkCongestionAbate3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionAbate3_Type.__name__ = "Unsigned32"
_CgspLinkCongestionAbate3_Object = MibTableColumn
cgspLinkCongestionAbate3 = _CgspLinkCongestionAbate3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 14),
    _CgspLinkCongestionAbate3_Type()
)
cgspLinkCongestionAbate3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionAbate3.setStatus("current")


class _CgspLinkCongestionOnset1_Type(Unsigned32):
    """Custom type cgspLinkCongestionOnset1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionOnset1_Type.__name__ = "Unsigned32"
_CgspLinkCongestionOnset1_Object = MibTableColumn
cgspLinkCongestionOnset1 = _CgspLinkCongestionOnset1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 15),
    _CgspLinkCongestionOnset1_Type()
)
cgspLinkCongestionOnset1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionOnset1.setStatus("current")


class _CgspLinkCongestionOnset2_Type(Unsigned32):
    """Custom type cgspLinkCongestionOnset2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionOnset2_Type.__name__ = "Unsigned32"
_CgspLinkCongestionOnset2_Object = MibTableColumn
cgspLinkCongestionOnset2 = _CgspLinkCongestionOnset2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 16),
    _CgspLinkCongestionOnset2_Type()
)
cgspLinkCongestionOnset2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionOnset2.setStatus("current")


class _CgspLinkCongestionOnset3_Type(Unsigned32):
    """Custom type cgspLinkCongestionOnset3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgspLinkCongestionOnset3_Type.__name__ = "Unsigned32"
_CgspLinkCongestionOnset3_Object = MibTableColumn
cgspLinkCongestionOnset3 = _CgspLinkCongestionOnset3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 17),
    _CgspLinkCongestionOnset3_Type()
)
cgspLinkCongestionOnset3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkCongestionOnset3.setStatus("current")


class _CgspLinkSigLinkTest_Type(TruthValue):
    """Custom type cgspLinkSigLinkTest based on TruthValue"""


_CgspLinkSigLinkTest_Object = MibTableColumn
cgspLinkSigLinkTest = _CgspLinkSigLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 18),
    _CgspLinkSigLinkTest_Type()
)
cgspLinkSigLinkTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkSigLinkTest.setStatus("current")
_CgspLinkQ752T1E1_Type = Counter32
_CgspLinkQ752T1E1_Object = MibTableColumn
cgspLinkQ752T1E1 = _CgspLinkQ752T1E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 19),
    _CgspLinkQ752T1E1_Type()
)
cgspLinkQ752T1E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E1.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E1.setUnits("seconds")
_CgspLinkQ752T1E2_Type = Counter32
_CgspLinkQ752T1E2_Object = MibTableColumn
cgspLinkQ752T1E2 = _CgspLinkQ752T1E2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 20),
    _CgspLinkQ752T1E2_Type()
)
cgspLinkQ752T1E2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E2.setStatus("current")
_CgspLinkQ752T1E3_Type = Counter32
_CgspLinkQ752T1E3_Object = MibTableColumn
cgspLinkQ752T1E3 = _CgspLinkQ752T1E3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 21),
    _CgspLinkQ752T1E3_Type()
)
cgspLinkQ752T1E3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E3.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E3.setUnits("occurrences")
_CgspLinkQ752T1E5_Type = Counter32
_CgspLinkQ752T1E5_Object = MibTableColumn
cgspLinkQ752T1E5 = _CgspLinkQ752T1E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 22),
    _CgspLinkQ752T1E5_Type()
)
cgspLinkQ752T1E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E5.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E5.setUnits("occurrences")
_CgspLinkQ752T1E7_Type = Counter32
_CgspLinkQ752T1E7_Object = MibTableColumn
cgspLinkQ752T1E7 = _CgspLinkQ752T1E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 23),
    _CgspLinkQ752T1E7_Type()
)
cgspLinkQ752T1E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E7.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E7.setUnits("occurrences")
_CgspLinkQ752T1E8_Type = Counter32
_CgspLinkQ752T1E8_Object = MibTableColumn
cgspLinkQ752T1E8 = _CgspLinkQ752T1E8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 24),
    _CgspLinkQ752T1E8_Type()
)
cgspLinkQ752T1E8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E8.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E8.setUnits("occurrences")
_CgspLinkQ752T1E9_Type = Counter32
_CgspLinkQ752T1E9_Object = MibTableColumn
cgspLinkQ752T1E9 = _CgspLinkQ752T1E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 25),
    _CgspLinkQ752T1E9_Type()
)
cgspLinkQ752T1E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E9.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E9.setUnits("negative acknowledgements")
_CgspLinkQ752T1E10_Type = Counter32
_CgspLinkQ752T1E10_Object = MibTableColumn
cgspLinkQ752T1E10 = _CgspLinkQ752T1E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 26),
    _CgspLinkQ752T1E10_Type()
)
cgspLinkQ752T1E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E10.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E10.setUnits("occurrences")
_CgspLinkQ752T1E11_Type = Counter32
_CgspLinkQ752T1E11_Object = MibTableColumn
cgspLinkQ752T1E11 = _CgspLinkQ752T1E11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 27),
    _CgspLinkQ752T1E11_Type()
)
cgspLinkQ752T1E11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E11.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E11.setUnits("occurrences")
_CgspLinkQ752T2E1_Type = Counter32
_CgspLinkQ752T2E1_Object = MibTableColumn
cgspLinkQ752T2E1 = _CgspLinkQ752T2E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 28),
    _CgspLinkQ752T2E1_Type()
)
cgspLinkQ752T2E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E1.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E1.setUnits("seconds")
_CgspLinkQ752T2E5_Type = Counter32
_CgspLinkQ752T2E5_Object = MibTableColumn
cgspLinkQ752T2E5 = _CgspLinkQ752T2E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 29),
    _CgspLinkQ752T2E5_Type()
)
cgspLinkQ752T2E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E5.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E5.setUnits("seconds")
_CgspLinkQ752T2E6_Type = Counter32
_CgspLinkQ752T2E6_Object = MibTableColumn
cgspLinkQ752T2E6 = _CgspLinkQ752T2E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 30),
    _CgspLinkQ752T2E6_Type()
)
cgspLinkQ752T2E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E6.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E6.setUnits("seconds")
_CgspLinkQ752T2E7_Type = Counter32
_CgspLinkQ752T2E7_Object = MibTableColumn
cgspLinkQ752T2E7 = _CgspLinkQ752T2E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 31),
    _CgspLinkQ752T2E7_Type()
)
cgspLinkQ752T2E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E7.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E7.setUnits("seconds")
_CgspLinkQ752T2E9_Type = Counter32
_CgspLinkQ752T2E9_Object = MibTableColumn
cgspLinkQ752T2E9 = _CgspLinkQ752T2E9_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 32),
    _CgspLinkQ752T2E9_Type()
)
cgspLinkQ752T2E9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E9.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E9.setUnits("seconds")
_CgspLinkQ752T2E10_Type = Counter32
_CgspLinkQ752T2E10_Object = MibTableColumn
cgspLinkQ752T2E10 = _CgspLinkQ752T2E10_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 33),
    _CgspLinkQ752T2E10_Type()
)
cgspLinkQ752T2E10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E10.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E10.setUnits("occurrences")
_CgspLinkQ752T2E15_Type = Counter32
_CgspLinkQ752T2E15_Object = MibTableColumn
cgspLinkQ752T2E15 = _CgspLinkQ752T2E15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 34),
    _CgspLinkQ752T2E15_Type()
)
cgspLinkQ752T2E15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E15.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E15.setUnits("occurrences")
_CgspLinkQ752T2E16_Type = Counter32
_CgspLinkQ752T2E16_Object = MibTableColumn
cgspLinkQ752T2E16 = _CgspLinkQ752T2E16_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 35),
    _CgspLinkQ752T2E16_Type()
)
cgspLinkQ752T2E16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E16.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E16.setUnits("occurrences")
_CgspLinkQ752T2E18_Type = Counter32
_CgspLinkQ752T2E18_Object = MibTableColumn
cgspLinkQ752T2E18 = _CgspLinkQ752T2E18_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 36),
    _CgspLinkQ752T2E18_Type()
)
cgspLinkQ752T2E18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E18.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E18.setUnits("occurrences")
_CgspLinkQ752T3E1_Type = Counter32
_CgspLinkQ752T3E1_Object = MibTableColumn
cgspLinkQ752T3E1 = _CgspLinkQ752T3E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 37),
    _CgspLinkQ752T3E1_Type()
)
cgspLinkQ752T3E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E1.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E1.setUnits("bytes")
_CgspLinkQ752T3E2Bytes_Type = Counter32
_CgspLinkQ752T3E2Bytes_Object = MibTableColumn
cgspLinkQ752T3E2Bytes = _CgspLinkQ752T3E2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 38),
    _CgspLinkQ752T3E2Bytes_Type()
)
cgspLinkQ752T3E2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E2Bytes.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E2Bytes.setUnits("bytes")
_CgspLinkQ752T3E2Packets_Type = Counter32
_CgspLinkQ752T3E2Packets_Object = MibTableColumn
cgspLinkQ752T3E2Packets = _CgspLinkQ752T3E2Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 39),
    _CgspLinkQ752T3E2Packets_Type()
)
cgspLinkQ752T3E2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E2Packets.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E2Packets.setUnits("packets")
_CgspLinkQ752T3E3_Type = Counter32
_CgspLinkQ752T3E3_Object = MibTableColumn
cgspLinkQ752T3E3 = _CgspLinkQ752T3E3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 40),
    _CgspLinkQ752T3E3_Type()
)
cgspLinkQ752T3E3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E3.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E3.setUnits("packets")
_CgspLinkQ752T3E4_Type = Counter32
_CgspLinkQ752T3E4_Object = MibTableColumn
cgspLinkQ752T3E4 = _CgspLinkQ752T3E4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 41),
    _CgspLinkQ752T3E4_Type()
)
cgspLinkQ752T3E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E4.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E4.setUnits("bytes")
_CgspLinkQ752T3E5_Type = Counter32
_CgspLinkQ752T3E5_Object = MibTableColumn
cgspLinkQ752T3E5 = _CgspLinkQ752T3E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 42),
    _CgspLinkQ752T3E5_Type()
)
cgspLinkQ752T3E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E5.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E5.setUnits("packets")
_CgspLinkQ752T3E6_Type = Counter32
_CgspLinkQ752T3E6_Object = MibTableColumn
cgspLinkQ752T3E6 = _CgspLinkQ752T3E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 43),
    _CgspLinkQ752T3E6_Type()
)
cgspLinkQ752T3E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E6.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E6.setUnits("events")
_CgspLinkQ752T3E7_Type = Counter32
_CgspLinkQ752T3E7_Object = MibTableColumn
cgspLinkQ752T3E7 = _CgspLinkQ752T3E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 44),
    _CgspLinkQ752T3E7_Type()
)
cgspLinkQ752T3E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E7.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E7.setUnits("seconds")
_CgspLinkQ752T3E10L1_Type = Counter32
_CgspLinkQ752T3E10L1_Object = MibTableColumn
cgspLinkQ752T3E10L1 = _CgspLinkQ752T3E10L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 45),
    _CgspLinkQ752T3E10L1_Type()
)
cgspLinkQ752T3E10L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L1.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L1.setUnits("Packets")
_CgspLinkQ752T3E10L2_Type = Counter32
_CgspLinkQ752T3E10L2_Object = MibTableColumn
cgspLinkQ752T3E10L2 = _CgspLinkQ752T3E10L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 46),
    _CgspLinkQ752T3E10L2_Type()
)
cgspLinkQ752T3E10L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L2.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L2.setUnits("Packets")
_CgspLinkQ752T3E10L3_Type = Counter32
_CgspLinkQ752T3E10L3_Object = MibTableColumn
cgspLinkQ752T3E10L3 = _CgspLinkQ752T3E10L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 47),
    _CgspLinkQ752T3E10L3_Type()
)
cgspLinkQ752T3E10L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L3.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E10L3.setUnits("Packets")
_CgspLinkQ752T3E11L1_Type = Counter32
_CgspLinkQ752T3E11L1_Object = MibTableColumn
cgspLinkQ752T3E11L1 = _CgspLinkQ752T3E11L1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 48),
    _CgspLinkQ752T3E11L1_Type()
)
cgspLinkQ752T3E11L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L1.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L1.setUnits("occurrences")
_CgspLinkQ752T3E11L2_Type = Counter32
_CgspLinkQ752T3E11L2_Object = MibTableColumn
cgspLinkQ752T3E11L2 = _CgspLinkQ752T3E11L2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 49),
    _CgspLinkQ752T3E11L2_Type()
)
cgspLinkQ752T3E11L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L2.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L2.setUnits("occurrences")
_CgspLinkQ752T3E11L3_Type = Counter32
_CgspLinkQ752T3E11L3_Object = MibTableColumn
cgspLinkQ752T3E11L3 = _CgspLinkQ752T3E11L3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 50),
    _CgspLinkQ752T3E11L3_Type()
)
cgspLinkQ752T3E11L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L3.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T3E11L3.setUnits("occurrences")
_CgspLinkLocalPeerPort_Type = InetPortNumber
_CgspLinkLocalPeerPort_Object = MibTableColumn
cgspLinkLocalPeerPort = _CgspLinkLocalPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 51),
    _CgspLinkLocalPeerPort_Type()
)
cgspLinkLocalPeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkLocalPeerPort.setStatus("current")
_CgspLinkRemotePeerPort_Type = InetPortNumber
_CgspLinkRemotePeerPort_Object = MibTableColumn
cgspLinkRemotePeerPort = _CgspLinkRemotePeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 52),
    _CgspLinkRemotePeerPort_Type()
)
cgspLinkRemotePeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkRemotePeerPort.setStatus("current")
_CgspLinkQosClass_Type = CItpTcQos
_CgspLinkQosClass_Object = MibTableColumn
cgspLinkQosClass = _CgspLinkQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 53),
    _CgspLinkQosClass_Type()
)
cgspLinkQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkQosClass.setStatus("current")


class _CgspLinkDisplayName_Type(SnmpAdminString):
    """Custom type cgspLinkDisplayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CgspLinkDisplayName_Type.__name__ = "SnmpAdminString"
_CgspLinkDisplayName_Object = MibTableColumn
cgspLinkDisplayName = _CgspLinkDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 54),
    _CgspLinkDisplayName_Type()
)
cgspLinkDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkDisplayName.setStatus("current")
_CgspLinkDroppedPkts_Type = Counter32
_CgspLinkDroppedPkts_Object = MibTableColumn
cgspLinkDroppedPkts = _CgspLinkDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 55),
    _CgspLinkDroppedPkts_Type()
)
cgspLinkDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkDroppedPkts.setUnits("packets")
_CgspLinkTransmittedLSSUs_Type = Counter32
_CgspLinkTransmittedLSSUs_Object = MibTableColumn
cgspLinkTransmittedLSSUs = _CgspLinkTransmittedLSSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 56),
    _CgspLinkTransmittedLSSUs_Type()
)
cgspLinkTransmittedLSSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTransmittedLSSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkTransmittedLSSUs.setUnits("LSSU")
_CgspLinkReceivedLSSUs_Type = Counter32
_CgspLinkReceivedLSSUs_Object = MibTableColumn
cgspLinkReceivedLSSUs = _CgspLinkReceivedLSSUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 57),
    _CgspLinkReceivedLSSUs_Type()
)
cgspLinkReceivedLSSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkReceivedLSSUs.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkReceivedLSSUs.setUnits("LSSU")


class _CgspLinkProtocolDetails_Type(Bits):
    """Custom type cgspLinkProtocolDetails based on Bits"""
    namedValues = NamedValues(
        *(("tcbcBuffering", 0),
          ("tcocBuffering", 1),
          ("tlacAdjacentSpRestarting", 2),
          ("tlacChangebackInProgress", 4),
          ("tlacChangeoverFailed", 6),
          ("tlacChangeoverInProgress", 5),
          ("tlacEmergencyCoInProgress", 3),
          ("tlacInhibitRetry", 7),
          ("tlacLocalBlocked", 14),
          ("tlacLocalInhibit", 12),
          ("tlacManagementRequest", 8),
          ("tlacRemoteBlocked", 15),
          ("tlacRemoteInhibit", 13),
          ("tlacSpRestarting", 9),
          ("tsrcAdjacentSpRestart", 11),
          ("tsrcChangeOverComplete", 10))
    )

_CgspLinkProtocolDetails_Type.__name__ = "Bits"
_CgspLinkProtocolDetails_Object = MibTableColumn
cgspLinkProtocolDetails = _CgspLinkProtocolDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 58),
    _CgspLinkProtocolDetails_Type()
)
cgspLinkProtocolDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkProtocolDetails.setStatus("current")


class _CgspLinkLsacState_Type(Integer32):
    """Custom type cgspLinkLsacState based on Integer32"""
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
        *(("actAnsiWaitDeloaded", 7),
          ("actItuWaitStmReady", 8),
          ("actT17wait", 6),
          ("activatingRestoring", 4),
          ("active", 3),
          ("failed", 5),
          ("inactive", 2),
          ("undefined", 1))
    )


_CgspLinkLsacState_Type.__name__ = "Integer32"
_CgspLinkLsacState_Object = MibTableColumn
cgspLinkLsacState = _CgspLinkLsacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 59),
    _CgspLinkLsacState_Type()
)
cgspLinkLsacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkLsacState.setStatus("current")


class _CgspLinkTsrcState_Type(Integer32):
    """Custom type cgspLinkTsrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("undefined", 1),
          ("wait5", 3))
    )


_CgspLinkTsrcState_Type.__name__ = "Integer32"
_CgspLinkTsrcState_Object = MibTableColumn
cgspLinkTsrcState = _CgspLinkTsrcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 60),
    _CgspLinkTsrcState_Type()
)
cgspLinkTsrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTsrcState.setStatus("current")


class _CgspLinkTcocState_Type(Integer32):
    """Custom type cgspLinkTcocState based on Integer32"""
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
        *(("idle", 2),
          ("retrieving", 5),
          ("undefined", 1),
          ("wait2", 3),
          ("wait5", 6),
          ("wait7", 7),
          ("wait8", 8),
          ("waitForAck", 4))
    )


_CgspLinkTcocState_Type.__name__ = "Integer32"
_CgspLinkTcocState_Object = MibTableColumn
cgspLinkTcocState = _CgspLinkTcocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 61),
    _CgspLinkTcocState_Type()
)
cgspLinkTcocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTcocState.setStatus("current")
_CgspLinkTcocLocalBSNT_Type = CgspSequenceNumber
_CgspLinkTcocLocalBSNT_Object = MibTableColumn
cgspLinkTcocLocalBSNT = _CgspLinkTcocLocalBSNT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 62),
    _CgspLinkTcocLocalBSNT_Type()
)
cgspLinkTcocLocalBSNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTcocLocalBSNT.setStatus("current")
_CgspLinkTcocRemoteBSNT_Type = CgspSequenceNumber
_CgspLinkTcocRemoteBSNT_Object = MibTableColumn
cgspLinkTcocRemoteBSNT = _CgspLinkTcocRemoteBSNT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 63),
    _CgspLinkTcocRemoteBSNT_Type()
)
cgspLinkTcocRemoteBSNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTcocRemoteBSNT.setStatus("current")


class _CgspLinkTcbcState_Type(Integer32):
    """Custom type cgspLinkTcbcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("firstAttempt", 3),
          ("idle", 2),
          ("secondAttempt", 4),
          ("timeControlledDiversion", 5),
          ("undefined", 1))
    )


_CgspLinkTcbcState_Type.__name__ = "Integer32"
_CgspLinkTcbcState_Object = MibTableColumn
cgspLinkTcbcState = _CgspLinkTcbcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 64),
    _CgspLinkTcbcState_Type()
)
cgspLinkTcbcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTcbcState.setStatus("current")
_CgspLinkReceivedSIBs_Type = Counter32
_CgspLinkReceivedSIBs_Object = MibTableColumn
cgspLinkReceivedSIBs = _CgspLinkReceivedSIBs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 65),
    _CgspLinkReceivedSIBs_Type()
)
cgspLinkReceivedSIBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkReceivedSIBs.setStatus("current")
_CgspLinkTransmittedSIBs_Type = Counter32
_CgspLinkTransmittedSIBs_Object = MibTableColumn
cgspLinkTransmittedSIBs = _CgspLinkTransmittedSIBs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 66),
    _CgspLinkTransmittedSIBs_Type()
)
cgspLinkTransmittedSIBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTransmittedSIBs.setStatus("current")
_CgspLinkMtp2T01Counts_Type = Counter32
_CgspLinkMtp2T01Counts_Object = MibTableColumn
cgspLinkMtp2T01Counts = _CgspLinkMtp2T01Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 67),
    _CgspLinkMtp2T01Counts_Type()
)
cgspLinkMtp2T01Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T01Counts.setStatus("current")
_CgspLinkMtp2T02Counts_Type = Counter32
_CgspLinkMtp2T02Counts_Object = MibTableColumn
cgspLinkMtp2T02Counts = _CgspLinkMtp2T02Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 68),
    _CgspLinkMtp2T02Counts_Type()
)
cgspLinkMtp2T02Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T02Counts.setStatus("current")
_CgspLinkMtp2T03Counts_Type = Counter32
_CgspLinkMtp2T03Counts_Object = MibTableColumn
cgspLinkMtp2T03Counts = _CgspLinkMtp2T03Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 69),
    _CgspLinkMtp2T03Counts_Type()
)
cgspLinkMtp2T03Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T03Counts.setStatus("current")
_CgspLinkMtp2T04Counts_Type = Counter32
_CgspLinkMtp2T04Counts_Object = MibTableColumn
cgspLinkMtp2T04Counts = _CgspLinkMtp2T04Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 70),
    _CgspLinkMtp2T04Counts_Type()
)
cgspLinkMtp2T04Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T04Counts.setStatus("current")
_CgspLinkMtp2T05Counts_Type = Counter32
_CgspLinkMtp2T05Counts_Object = MibTableColumn
cgspLinkMtp2T05Counts = _CgspLinkMtp2T05Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 71),
    _CgspLinkMtp2T05Counts_Type()
)
cgspLinkMtp2T05Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T05Counts.setStatus("current")
_CgspLinkMtp2T06Counts_Type = Counter32
_CgspLinkMtp2T06Counts_Object = MibTableColumn
cgspLinkMtp2T06Counts = _CgspLinkMtp2T06Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 72),
    _CgspLinkMtp2T06Counts_Type()
)
cgspLinkMtp2T06Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T06Counts.setStatus("current")
_CgspLinkMtp2T07Counts_Type = Counter32
_CgspLinkMtp2T07Counts_Object = MibTableColumn
cgspLinkMtp2T07Counts = _CgspLinkMtp2T07Counts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 73),
    _CgspLinkMtp2T07Counts_Type()
)
cgspLinkMtp2T07Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkMtp2T07Counts.setStatus("current")
_CgspLinkOMAERMCounts_Type = Counter32
_CgspLinkOMAERMCounts_Object = MibTableColumn
cgspLinkOMAERMCounts = _CgspLinkOMAERMCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 74),
    _CgspLinkOMAERMCounts_Type()
)
cgspLinkOMAERMCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkOMAERMCounts.setStatus("current")
_CgspLinkOMAERMFailCounts_Type = Counter32
_CgspLinkOMAERMFailCounts_Object = MibTableColumn
cgspLinkOMAERMFailCounts = _CgspLinkOMAERMFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 75),
    _CgspLinkOMAERMFailCounts_Type()
)
cgspLinkOMAERMFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkOMAERMFailCounts.setStatus("current")
_CgspLinkOMSURMCounts_Type = Counter32
_CgspLinkOMSURMCounts_Object = MibTableColumn
cgspLinkOMSURMCounts = _CgspLinkOMSURMCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 76),
    _CgspLinkOMSURMCounts_Type()
)
cgspLinkOMSURMCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkOMSURMCounts.setStatus("current")
_CgspLinkOMSURMFailCounts_Type = Counter32
_CgspLinkOMSURMFailCounts_Object = MibTableColumn
cgspLinkOMSURMFailCounts = _CgspLinkOMSURMFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 77),
    _CgspLinkOMSURMFailCounts_Type()
)
cgspLinkOMSURMFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkOMSURMFailCounts.setStatus("current")
_CgspLinkPlanCapacityRcvd_Type = CgspLinkCapacity
_CgspLinkPlanCapacityRcvd_Object = MibTableColumn
cgspLinkPlanCapacityRcvd = _CgspLinkPlanCapacityRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 78),
    _CgspLinkPlanCapacityRcvd_Type()
)
cgspLinkPlanCapacityRcvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkPlanCapacityRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkPlanCapacityRcvd.setUnits("bits per second")


class _CgspLinkUtilThresholdRcvd_Type(CgspPercentThreshold):
    """Custom type cgspLinkUtilThresholdRcvd based on CgspPercentThreshold"""
    defaultValue = 0


_CgspLinkUtilThresholdRcvd_Object = MibTableColumn
cgspLinkUtilThresholdRcvd = _CgspLinkUtilThresholdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 79),
    _CgspLinkUtilThresholdRcvd_Type()
)
cgspLinkUtilThresholdRcvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkUtilThresholdRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilThresholdRcvd.setUnits("percent")
_CgspLinkUtilizationRcvd_Type = CgspLinkUtilization
_CgspLinkUtilizationRcvd_Object = MibTableColumn
cgspLinkUtilizationRcvd = _CgspLinkUtilizationRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 80),
    _CgspLinkUtilizationRcvd_Type()
)
cgspLinkUtilizationRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilizationRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilizationRcvd.setUnits("percent")
_CgspLinkUtilStateRcvd_Type = CgspLinkUtilizationState
_CgspLinkUtilStateRcvd_Object = MibTableColumn
cgspLinkUtilStateRcvd = _CgspLinkUtilStateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 81),
    _CgspLinkUtilStateRcvd_Type()
)
cgspLinkUtilStateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilStateRcvd.setStatus("current")
_CgspLinkL2BytesRcvd_Type = Counter32
_CgspLinkL2BytesRcvd_Object = MibTableColumn
cgspLinkL2BytesRcvd = _CgspLinkL2BytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 82),
    _CgspLinkL2BytesRcvd_Type()
)
cgspLinkL2BytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkL2BytesRcvd.setStatus("current")
_CgspLinkPlanCapacitySent_Type = CgspLinkCapacity
_CgspLinkPlanCapacitySent_Object = MibTableColumn
cgspLinkPlanCapacitySent = _CgspLinkPlanCapacitySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 83),
    _CgspLinkPlanCapacitySent_Type()
)
cgspLinkPlanCapacitySent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkPlanCapacitySent.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkPlanCapacitySent.setUnits("bits per second")


class _CgspLinkUtilThresholdSent_Type(CgspPercentThreshold):
    """Custom type cgspLinkUtilThresholdSent based on CgspPercentThreshold"""
    defaultValue = 0


_CgspLinkUtilThresholdSent_Object = MibTableColumn
cgspLinkUtilThresholdSent = _CgspLinkUtilThresholdSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 84),
    _CgspLinkUtilThresholdSent_Type()
)
cgspLinkUtilThresholdSent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkUtilThresholdSent.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilThresholdSent.setUnits("percent")
_CgspLinkUtilizationSent_Type = CgspLinkUtilization
_CgspLinkUtilizationSent_Object = MibTableColumn
cgspLinkUtilizationSent = _CgspLinkUtilizationSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 85),
    _CgspLinkUtilizationSent_Type()
)
cgspLinkUtilizationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilizationSent.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilizationSent.setUnits("percent")
_CgspLinkUtilStateSent_Type = CgspLinkUtilizationState
_CgspLinkUtilStateSent_Object = MibTableColumn
cgspLinkUtilStateSent = _CgspLinkUtilStateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 86),
    _CgspLinkUtilStateSent_Type()
)
cgspLinkUtilStateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilStateSent.setStatus("current")
_CgspLinkL2BytesSent_Type = Counter32
_CgspLinkL2BytesSent_Object = MibTableColumn
cgspLinkL2BytesSent = _CgspLinkL2BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 87),
    _CgspLinkL2BytesSent_Type()
)
cgspLinkL2BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkL2BytesSent.setStatus("current")
_CgspLinkTestResult_Type = CgspLinkTestResults
_CgspLinkTestResult_Object = MibTableColumn
cgspLinkTestResult = _CgspLinkTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 88),
    _CgspLinkTestResult_Type()
)
cgspLinkTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkTestResult.setStatus("current")
_CgspLinkRowStatus_Type = RowStatus
_CgspLinkRowStatus_Object = MibTableColumn
cgspLinkRowStatus = _CgspLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 89),
    _CgspLinkRowStatus_Type()
)
cgspLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkRowStatus.setStatus("current")
_CgspLinkSctpAssociationId_Type = Unsigned32
_CgspLinkSctpAssociationId_Object = MibTableColumn
cgspLinkSctpAssociationId = _CgspLinkSctpAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 90),
    _CgspLinkSctpAssociationId_Type()
)
cgspLinkSctpAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkSctpAssociationId.setStatus("current")
_CgspLinkQ752T1E12_Type = Counter32
_CgspLinkQ752T1E12_Object = MibTableColumn
cgspLinkQ752T1E12 = _CgspLinkQ752T1E12_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 91),
    _CgspLinkQ752T1E12_Type()
)
cgspLinkQ752T1E12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E12.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E12.setUnits("occurrences")
_CgspLinkQ752T1E12Errors_Type = Counter32
_CgspLinkQ752T1E12Errors_Object = MibTableColumn
cgspLinkQ752T1E12Errors = _CgspLinkQ752T1E12Errors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 92),
    _CgspLinkQ752T1E12Errors_Type()
)
cgspLinkQ752T1E12Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E12Errors.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T1E12Errors.setUnits("occurrences")
_CgspLinkQ752T2E11_Type = Counter32
_CgspLinkQ752T2E11_Object = MibTableColumn
cgspLinkQ752T2E11 = _CgspLinkQ752T2E11_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 93),
    _CgspLinkQ752T2E11_Type()
)
cgspLinkQ752T2E11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E11.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E11.setUnits("occurrences")
_CgspLinkQ752T2E17_Type = Counter32
_CgspLinkQ752T2E17_Object = MibTableColumn
cgspLinkQ752T2E17 = _CgspLinkQ752T2E17_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 94),
    _CgspLinkQ752T2E17_Type()
)
cgspLinkQ752T2E17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E17.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E17.setUnits("occurrences")
_CgspLinkQ752T2E19_Type = Counter32
_CgspLinkQ752T2E19_Object = MibTableColumn
cgspLinkQ752T2E19 = _CgspLinkQ752T2E19_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 95),
    _CgspLinkQ752T2E19_Type()
)
cgspLinkQ752T2E19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E19.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkQ752T2E19.setUnits("occurrences")


class _CgspLinkRxCongestionState_Type(Unsigned32):
    """Custom type cgspLinkRxCongestionState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CgspLinkRxCongestionState_Type.__name__ = "Unsigned32"
_CgspLinkRxCongestionState_Object = MibTableColumn
cgspLinkRxCongestionState = _CgspLinkRxCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 1, 1, 96),
    _CgspLinkRxCongestionState_Type()
)
cgspLinkRxCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkRxCongestionState.setStatus("current")
_CgspLinkTimerTable_Object = MibTable
cgspLinkTimerTable = _CgspLinkTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cgspLinkTimerTable.setStatus("current")
_CgspLinkTimerTableEntry_Object = MibTableRow
cgspLinkTimerTableEntry = _CgspLinkTimerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 2, 1)
)
cgspLinkTimerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkSlc"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkTimerNumber"),
)
if mibBuilder.loadTexts:
    cgspLinkTimerTableEntry.setStatus("current")
_CgspLinkTimerNumber_Type = CgspTimerNumbers
_CgspLinkTimerNumber_Object = MibTableColumn
cgspLinkTimerNumber = _CgspLinkTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 2, 1, 1),
    _CgspLinkTimerNumber_Type()
)
cgspLinkTimerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinkTimerNumber.setStatus("current")
_CgspLinkTimerValue_Type = CgspTimerValue
_CgspLinkTimerValue_Object = MibTableColumn
cgspLinkTimerValue = _CgspLinkTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 2, 1, 2),
    _CgspLinkTimerValue_Type()
)
cgspLinkTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkTimerValue.setUnits("milliseconds")
_CgspLinkTimerRowStatus_Type = RowStatus
_CgspLinkTimerRowStatus_Object = MibTableColumn
cgspLinkTimerRowStatus = _CgspLinkTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 2, 1, 3),
    _CgspLinkTimerRowStatus_Type()
)
cgspLinkTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkTimerRowStatus.setStatus("current")
_CgspLinkRemoteIpAddrTable_Object = MibTable
cgspLinkRemoteIpAddrTable = _CgspLinkRemoteIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddrTable.setStatus("current")
_CgspLinkRemoteIpAddrTableEntry_Object = MibTableRow
cgspLinkRemoteIpAddrTableEntry = _CgspLinkRemoteIpAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3, 1)
)
cgspLinkRemoteIpAddrTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkSlc"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkRemoteIpAddrNumber"),
)
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddrTableEntry.setStatus("current")


class _CgspLinkRemoteIpAddrNumber_Type(Unsigned32):
    """Custom type cgspLinkRemoteIpAddrNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgspLinkRemoteIpAddrNumber_Type.__name__ = "Unsigned32"
_CgspLinkRemoteIpAddrNumber_Object = MibTableColumn
cgspLinkRemoteIpAddrNumber = _CgspLinkRemoteIpAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3, 1, 1),
    _CgspLinkRemoteIpAddrNumber_Type()
)
cgspLinkRemoteIpAddrNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddrNumber.setStatus("current")
_CgspLinkRemoteIpAddrType_Type = InetAddressType
_CgspLinkRemoteIpAddrType_Object = MibTableColumn
cgspLinkRemoteIpAddrType = _CgspLinkRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3, 1, 2),
    _CgspLinkRemoteIpAddrType_Type()
)
cgspLinkRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddrType.setStatus("current")
_CgspLinkRemoteIpAddress_Type = InetAddress
_CgspLinkRemoteIpAddress_Object = MibTableColumn
cgspLinkRemoteIpAddress = _CgspLinkRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3, 1, 3),
    _CgspLinkRemoteIpAddress_Type()
)
cgspLinkRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddress.setStatus("current")
_CgspLinkRemoteIpAddrRowStatus_Type = RowStatus
_CgspLinkRemoteIpAddrRowStatus_Object = MibTableColumn
cgspLinkRemoteIpAddrRowStatus = _CgspLinkRemoteIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 3, 1, 4),
    _CgspLinkRemoteIpAddrRowStatus_Type()
)
cgspLinkRemoteIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgspLinkRemoteIpAddrRowStatus.setStatus("current")
_CgspLinkUtilTable_Object = MibTable
cgspLinkUtilTable = _CgspLinkUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cgspLinkUtilTable.setStatus("current")
_CgspLinkUtilTableEntry_Object = MibTableRow
cgspLinkUtilTableEntry = _CgspLinkUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4, 1)
)
cgspLinkUtilTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinksetName"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkSlc"),
    (0, "CISCO-ITP-GSP-MIB", "cgspLinkUtilIndex"),
)
if mibBuilder.loadTexts:
    cgspLinkUtilTableEntry.setStatus("current")


class _CgspLinkUtilIndex_Type(Unsigned32):
    """Custom type cgspLinkUtilIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CgspLinkUtilIndex_Type.__name__ = "Unsigned32"
_CgspLinkUtilIndex_Object = MibTableColumn
cgspLinkUtilIndex = _CgspLinkUtilIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4, 1, 1),
    _CgspLinkUtilIndex_Type()
)
cgspLinkUtilIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgspLinkUtilIndex.setStatus("current")
_CgspLinkUtilRcvd_Type = CgspLinkUtilization
_CgspLinkUtilRcvd_Object = MibTableColumn
cgspLinkUtilRcvd = _CgspLinkUtilRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4, 1, 2),
    _CgspLinkUtilRcvd_Type()
)
cgspLinkUtilRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilRcvd.setUnits("percent")
_CgspLinkUtilSent_Type = CgspLinkUtilization
_CgspLinkUtilSent_Object = MibTableColumn
cgspLinkUtilSent = _CgspLinkUtilSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4, 1, 3),
    _CgspLinkUtilSent_Type()
)
cgspLinkUtilSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilSent.setStatus("current")
if mibBuilder.loadTexts:
    cgspLinkUtilSent.setUnits("percent")
_CgspLinkUtilEndTimestamp_Type = TimeStamp
_CgspLinkUtilEndTimestamp_Object = MibTableColumn
cgspLinkUtilEndTimestamp = _CgspLinkUtilEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 6, 4, 1, 4),
    _CgspLinkUtilEndTimestamp_Type()
)
cgspLinkUtilEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgspLinkUtilEndTimestamp.setStatus("current")
_CgspNotificationsEnable_ObjectIdentity = ObjectIdentity
cgspNotificationsEnable = _CgspNotificationsEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7)
)


class _CgspLsStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cgspLsStateChangeNotifEnabled based on TruthValue"""


_CgspLsStateChangeNotifEnabled_Object = MibScalar
cgspLsStateChangeNotifEnabled = _CgspLsStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 1),
    _CgspLsStateChangeNotifEnabled_Type()
)
cgspLsStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspLsStateChangeNotifEnabled.setStatus("current")


class _CgspLnkStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cgspLnkStateChangeNotifEnabled based on TruthValue"""


_CgspLnkStateChangeNotifEnabled_Object = MibScalar
cgspLnkStateChangeNotifEnabled = _CgspLnkStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 2),
    _CgspLnkStateChangeNotifEnabled_Type()
)
cgspLnkStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspLnkStateChangeNotifEnabled.setStatus("current")


class _CgspCongestionNotifEnabled_Type(TruthValue):
    """Custom type cgspCongestionNotifEnabled based on TruthValue"""


_CgspCongestionNotifEnabled_Object = MibScalar
cgspCongestionNotifEnabled = _CgspCongestionNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 3),
    _CgspCongestionNotifEnabled_Type()
)
cgspCongestionNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspCongestionNotifEnabled.setStatus("current")


class _CgspLinkUtilNotifEnabled_Type(TruthValue):
    """Custom type cgspLinkUtilNotifEnabled based on TruthValue"""


_CgspLinkUtilNotifEnabled_Object = MibScalar
cgspLinkUtilNotifEnabled = _CgspLinkUtilNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 4),
    _CgspLinkUtilNotifEnabled_Type()
)
cgspLinkUtilNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspLinkUtilNotifEnabled.setStatus("current")


class _CgspIsolationNotifEnabled_Type(TruthValue):
    """Custom type cgspIsolationNotifEnabled based on TruthValue"""


_CgspIsolationNotifEnabled_Object = MibScalar
cgspIsolationNotifEnabled = _CgspIsolationNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 5),
    _CgspIsolationNotifEnabled_Type()
)
cgspIsolationNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspIsolationNotifEnabled.setStatus("current")


class _CgspUPUNotifEnabled_Type(TruthValue):
    """Custom type cgspUPUNotifEnabled based on TruthValue"""


_CgspUPUNotifEnabled_Object = MibScalar
cgspUPUNotifEnabled = _CgspUPUNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 7, 6),
    _CgspUPUNotifEnabled_Type()
)
cgspUPUNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgspUPUNotifEnabled.setStatus("current")
_CgspNotificationsInfo_ObjectIdentity = ObjectIdentity
cgspNotificationsInfo = _CgspNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 8)
)
_CgspUPUIntervalDuration_Type = Unsigned32
_CgspUPUIntervalDuration_Object = MibScalar
cgspUPUIntervalDuration = _CgspUPUIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 8, 1),
    _CgspUPUIntervalDuration_Type()
)
cgspUPUIntervalDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgspUPUIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    cgspUPUIntervalDuration.setUnits("seconds")
_CgspIntervalUPUs_Type = Unsigned32
_CgspIntervalUPUs_Object = MibScalar
cgspIntervalUPUs = _CgspIntervalUPUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 1, 8, 2),
    _CgspIntervalUPUs_Type()
)
cgspIntervalUPUs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgspIntervalUPUs.setStatus("current")
if mibBuilder.loadTexts:
    cgspIntervalUPUs.setUnits("MSUs")
_CiscoGspMIBConform_ObjectIdentity = ObjectIdentity
ciscoGspMIBConform = _CiscoGspMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2)
)
_CiscoGspMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGspMIBCompliances = _CiscoGspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1)
)
_CiscoGspMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGspMIBGroups = _CiscoGspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2)
)

# Managed Objects groups

ciscoGspScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 1)
)
ciscoGspScalarsGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspUtilSampleInterval"),
        ("CISCO-ITP-GSP-MIB", "cgspUtilThreshold"),
        ("CISCO-ITP-GSP-MIB", "cgspUtilAbateDelta"),
        ("CISCO-ITP-GSP-MIB", "cgspPlanCapacityDefault"),
        ("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    ciscoGspScalarsGroup.setStatus("current")

ciscoGspProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 2)
)
ciscoGspProfileGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspProfileVariant"),
        ("CISCO-ITP-GSP-MIB", "cgspProfileMtp2BundleTimer"),
        ("CISCO-ITP-GSP-MIB", "cgspProfileMtp2SendQueueDepth"),
        ("CISCO-ITP-GSP-MIB", "cgspProfileRowStatus"),
        ("CISCO-ITP-GSP-MIB", "cgspProfileTimerValue"),
        ("CISCO-ITP-GSP-MIB", "cgspProfileTimerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspProfileGroup.setStatus("current")

ciscoGspInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 3)
)
ciscoGspInstanceGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspInstNetworkIndicator"),
        ("CISCO-ITP-GSP-MIB", "cgspInstVariant"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDescription"),
        ("CISCO-ITP-GSP-MIB", "cgspInstTFR"),
        ("CISCO-ITP-GSP-MIB", "cgspInstCongestionsLevels"),
        ("CISCO-ITP-GSP-MIB", "cgspInstFastRestart"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDistSccpUnseq"),
        ("CISCO-ITP-GSP-MIB", "cgspInstSummaryRoutingException"),
        ("CISCO-ITP-GSP-MIB", "cgspInstNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspInstRouteTableName"),
        ("CISCO-ITP-GSP-MIB", "cgspInstRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspInstanceGroup.setStatus("current")

ciscoGspInstTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 4)
)
ciscoGspInstTimerGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspInstTimerValue"),
        ("CISCO-ITP-GSP-MIB", "cgspInstTimerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspInstTimerGroup.setStatus("current")

ciscoGspPointCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 5)
)
ciscoGspPointCodeGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspPointCodeType"),
        ("CISCO-ITP-GSP-MIB", "cgspPointCodeDisplay"),
        ("CISCO-ITP-GSP-MIB", "cgspPointCodeRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspPointCodeGroup.setStatus("current")

ciscoGspLinksetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 6)
)
ciscoGspLinksetGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinksetSourcePointCode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentPointCode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetInboundAcl"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetOutboundAcl"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAccountingMtp3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAccountingGtt"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetNumLinks"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetDurationInService"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetDurationOutService"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetActPriority"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetDescription"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetRotateSlsEnable"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetRotateSlsShift"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetProfileName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentInst"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspLinksetGroup.setStatus("current")

ciscoGspLinksetTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 7)
)
ciscoGspLinksetTimerGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinksetTimerValue"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetTimerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspLinksetTimerGroup.setStatus("current")

ciscoGspLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 8)
)
ciscoGspLinkGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkDescription"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReason"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkType"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkifIndex"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkSctpAssociation"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepth"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepthHigh"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepthHighRT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkSigLinkTest"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E8"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E9"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E10"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E11"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E6"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E9"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E10"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E15"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E16"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E18"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E2Packets"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E2Bytes"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E4"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E6"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkLocalPeerPort"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRemotePeerPort"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQosClass"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDroppedPkts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTransmittedLSSUs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReceivedLSSUs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkProtocolDetails"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkLsacState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTsrcState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocLocalBSNT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocRemoteBSNT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcbcState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReceivedSIBs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTransmittedSIBs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T01Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T02Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T03Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T04Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T05Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T06Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T07Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMAERMCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMAERMFailCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMSURMCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMSURMFailCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkPlanCapacityRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilThresholdRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkL2BytesRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkPlanCapacitySent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilThresholdSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkL2BytesSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTestResult"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkGroup.setStatus("deprecated")

ciscoGspLinkTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 9)
)
ciscoGspLinkTimerGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkTimerValue"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTimerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkTimerGroup.setStatus("current")

ciscoGspLinkRemoteIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 10)
)
ciscoGspLinkRemoteIpGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkRemoteIpAddrType"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRemoteIpAddress"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRemoteIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkRemoteIpGroup.setStatus("current")

ciscoGspLinkUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 11)
)
ciscoGspLinkUtilGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkUtilRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilEndTimestamp"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkUtilGroup.setStatus("current")

ciscoGspNotificationsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 12)
)
ciscoGspNotificationsEnableGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLsStateChangeNotifEnabled"),
        ("CISCO-ITP-GSP-MIB", "cgspLnkStateChangeNotifEnabled"),
        ("CISCO-ITP-GSP-MIB", "cgspCongestionNotifEnabled"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsEnableGroup.setStatus("current")

ciscoGspLinkGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 14)
)
ciscoGspLinkGroupRev1.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkDescription"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReason"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkType"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkifIndex"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepth"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepthHigh"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkXmitQueueDepthHighRT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionAbate3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionOnset3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkSigLinkTest"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E8"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E9"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E10"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E11"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E6"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E9"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E10"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E15"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E16"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E18"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E2Packets"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E2Bytes"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E4"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E5"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E6"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E7"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E10L3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L1"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L2"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T3E11L3"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkLocalPeerPort"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRemotePeerPort"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQosClass"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDroppedPkts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTransmittedLSSUs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReceivedLSSUs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkProtocolDetails"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkLsacState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTsrcState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocLocalBSNT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcocRemoteBSNT"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTcbcState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReceivedSIBs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTransmittedSIBs"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T01Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T02Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T03Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T04Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T05Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T06Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkMtp2T07Counts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMAERMCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMAERMFailCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMSURMCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkOMSURMFailCounts"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkPlanCapacityRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilThresholdRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkL2BytesRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkPlanCapacitySent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilThresholdSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkL2BytesSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTestResult"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRowStatus"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkSctpAssociationId"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkGroupRev1.setStatus("current")

ciscoGspNotificationsEnableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 15)
)
ciscoGspNotificationsEnableGroupSup1.setObjects(
    ("CISCO-ITP-GSP-MIB", "cgspIsolationNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsEnableGroupSup1.setStatus("current")

ciscoGspLinkGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 17)
)
ciscoGspLinkGroupSup1.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E12"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T1E12Errors"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E11"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E17"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkQ752T2E19"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkGroupSup1.setStatus("current")

ciscoGspScalarsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 18)
)
ciscoGspScalarsGroupSup1.setObjects(
    ("CISCO-ITP-GSP-MIB", "cgspUPUNotifWindowTime")
)
if mibBuilder.loadTexts:
    ciscoGspScalarsGroupSup1.setStatus("current")

ciscoGspInstUPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 20)
)
ciscoGspInstUPUGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspInstSIUPUReceived"),
        ("CISCO-ITP-GSP-MIB", "cgspInstSIUPUTransmitted"),
        ("CISCO-ITP-GSP-MIB", "cgspInstUserPartDisplay"))
)
if mibBuilder.loadTexts:
    ciscoGspInstUPUGroup.setStatus("current")

ciscoGspNotificationsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 21)
)
ciscoGspNotificationsInfoGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspUPUIntervalDuration"),
        ("CISCO-ITP-GSP-MIB", "cgspIntervalUPUs"))
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsInfoGroup.setStatus("current")

ciscoGspNotificationsEnableGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 22)
)
ciscoGspNotificationsEnableGroupSup2.setObjects(
    ("CISCO-ITP-GSP-MIB", "cgspUPUNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsEnableGroupSup2.setStatus("current")

ciscoGspInstSccpWrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 24)
)
ciscoGspInstSccpWrrGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspInstSccpWrrOpcShift"),
        ("CISCO-ITP-GSP-MIB", "cgspInstSccpWrrOption"))
)
if mibBuilder.loadTexts:
    ciscoGspInstSccpWrrGroup.setStatus("current")

ciscoGspLinkTableEntryGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 25)
)
ciscoGspLinkTableEntryGroupSup1.setObjects(
    ("CISCO-ITP-GSP-MIB", "cgspLinkRxCongestionState")
)
if mibBuilder.loadTexts:
    ciscoGspLinkTableEntryGroupSup1.setStatus("current")


# Notification objects

ciscoGspLinksetStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 1)
)
ciscoGspLinksetStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetState"))
)
if mibBuilder.loadTexts:
    ciscoGspLinksetStateChange.setStatus(
        "current"
    )

ciscoGspLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 2)
)
ciscoGspLinkStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkState"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkReason"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkTestResult"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkStateChange.setStatus(
        "current"
    )

ciscoGspCongestionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 3)
)
ciscoGspCongestionChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkCongestionState"))
)
if mibBuilder.loadTexts:
    ciscoGspCongestionChange.setStatus(
        "current"
    )

ciscoGspLinkRcvdUtilChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 4)
)
ciscoGspLinkRcvdUtilChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateRcvd"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationRcvd"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkRcvdUtilChange.setStatus(
        "current"
    )

ciscoGspLinkSentUtilChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 5)
)
ciscoGspLinkSentUtilChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilStateSent"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkUtilizationSent"))
)
if mibBuilder.loadTexts:
    ciscoGspLinkSentUtilChange.setStatus(
        "current"
    )

ciscoGspIsolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 6)
)
ciscoGspIsolation.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspInstDescription"))
)
if mibBuilder.loadTexts:
    ciscoGspIsolation.setStatus(
        "current"
    )

ciscoGspUPUReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 8)
)
ciscoGspUPUReceived.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstUserPartDisplay"),
        ("CISCO-ITP-GSP-MIB", "cgspUPUIntervalDuration"),
        ("CISCO-ITP-GSP-MIB", "cgspIntervalUPUs"))
)
if mibBuilder.loadTexts:
    ciscoGspUPUReceived.setStatus(
        "current"
    )

ciscoGspUPUTransmitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 9)
)
ciscoGspUPUTransmitted.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspInstUserPartDisplay"),
        ("CISCO-ITP-GSP-MIB", "cgspUPUIntervalDuration"),
        ("CISCO-ITP-GSP-MIB", "cgspIntervalUPUs"))
)
if mibBuilder.loadTexts:
    ciscoGspUPUTransmitted.setStatus(
        "current"
    )

ciscoGspRxCongestionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 0, 10)
)
ciscoGspRxCongestionChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetSourceDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinksetAdjacentDisplayPC"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkDisplayName"),
        ("CISCO-ITP-GSP-MIB", "cgspLinkRxCongestionState"))
)
if mibBuilder.loadTexts:
    ciscoGspRxCongestionChange.setStatus(
        "current"
    )


# Notifications groups

ciscoGspNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 13)
)
ciscoGspNotificationsGroup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "ciscoGspLinksetStateChange"),
        ("CISCO-ITP-GSP-MIB", "ciscoGspLinkStateChange"),
        ("CISCO-ITP-GSP-MIB", "ciscoGspCongestionChange"),
        ("CISCO-ITP-GSP-MIB", "ciscoGspLinkRcvdUtilChange"),
        ("CISCO-ITP-GSP-MIB", "ciscoGspLinkSentUtilChange"))
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsGroup.setStatus(
        "current"
    )

ciscoGspNotificationsGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 16)
)
ciscoGspNotificationsGroupSup1.setObjects(
    ("CISCO-ITP-GSP-MIB", "ciscoGspIsolation")
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsGroupSup1.setStatus(
        "current"
    )

ciscoGspNotificationsGroupSup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 23)
)
ciscoGspNotificationsGroupSup2.setObjects(
      *(("CISCO-ITP-GSP-MIB", "ciscoGspUPUReceived"),
        ("CISCO-ITP-GSP-MIB", "ciscoGspUPUTransmitted"))
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsGroupSup2.setStatus(
        "current"
    )

ciscoGspNotificationsGroupSup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 2, 26)
)
ciscoGspNotificationsGroupSup3.setObjects(
    ("CISCO-ITP-GSP-MIB", "ciscoGspRxCongestionChange")
)
if mibBuilder.loadTexts:
    ciscoGspNotificationsGroupSup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGspMIBCompliance.setStatus(
        "deprecated"
    )

ciscoGspMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGspMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoGspMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoGspMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoGspMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoGspMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoGspMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoGspMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoGspMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 336, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoGspMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSP-MIB",
    **{"CgspSequenceNumber": CgspSequenceNumber,
       "CgspSampleInterval": CgspSampleInterval,
       "CgspPercentThreshold": CgspPercentThreshold,
       "CgspLinkTestResults": CgspLinkTestResults,
       "CgspLinkUtilization": CgspLinkUtilization,
       "CgspLinkCapacity": CgspLinkCapacity,
       "CgspProfileName": CgspProfileName,
       "CgspLinkUtilizationState": CgspLinkUtilizationState,
       "CgspTimerNumbers": CgspTimerNumbers,
       "CgspTimerValue": CgspTimerValue,
       "CgspSS7Variant": CgspSS7Variant,
       "CgspDisplayInstanceUserPart": CgspDisplayInstanceUserPart,
       "CItpTcSccpWrrOption": CItpTcSccpWrrOption,
       "ciscoGspMIB": ciscoGspMIB,
       "ciscoGspMIBNotifs": ciscoGspMIBNotifs,
       "ciscoGspLinksetStateChange": ciscoGspLinksetStateChange,
       "ciscoGspLinkStateChange": ciscoGspLinkStateChange,
       "ciscoGspCongestionChange": ciscoGspCongestionChange,
       "ciscoGspLinkRcvdUtilChange": ciscoGspLinkRcvdUtilChange,
       "ciscoGspLinkSentUtilChange": ciscoGspLinkSentUtilChange,
       "ciscoGspIsolation": ciscoGspIsolation,
       "ciscoGspUPUReceived": ciscoGspUPUReceived,
       "ciscoGspUPUTransmitted": ciscoGspUPUTransmitted,
       "ciscoGspRxCongestionChange": ciscoGspRxCongestionChange,
       "ciscoGspMIBObjects": ciscoGspMIBObjects,
       "cgspScalars": cgspScalars,
       "cgspCLLICode": cgspCLLICode,
       "cgspUtilSampleInterval": cgspUtilSampleInterval,
       "cgspUtilThreshold": cgspUtilThreshold,
       "cgspUtilAbateDelta": cgspUtilAbateDelta,
       "cgspPlanCapacityDefault": cgspPlanCapacityDefault,
       "cgspEventSequenceNumber": cgspEventSequenceNumber,
       "cgspUPUNotifWindowTime": cgspUPUNotifWindowTime,
       "cgspProfile": cgspProfile,
       "cgspProfileTable": cgspProfileTable,
       "cgspProfileTableEntry": cgspProfileTableEntry,
       "cgspProfileName": cgspProfileName,
       "cgspProfileVariant": cgspProfileVariant,
       "cgspProfileMtp2BundleTimer": cgspProfileMtp2BundleTimer,
       "cgspProfileMtp2SendQueueDepth": cgspProfileMtp2SendQueueDepth,
       "cgspProfileRowStatus": cgspProfileRowStatus,
       "cgspProfileTimerTable": cgspProfileTimerTable,
       "cgspProfileTimerTableEntry": cgspProfileTimerTableEntry,
       "cgspProfileTimerNumber": cgspProfileTimerNumber,
       "cgspProfileTimerValue": cgspProfileTimerValue,
       "cgspProfileTimerRowStatus": cgspProfileTimerRowStatus,
       "cgspInstance": cgspInstance,
       "cgspInstanceTable": cgspInstanceTable,
       "cgspInstanceTableEntry": cgspInstanceTableEntry,
       "cgspInstNetwork": cgspInstNetwork,
       "cgspInstNetworkIndicator": cgspInstNetworkIndicator,
       "cgspInstVariant": cgspInstVariant,
       "cgspInstDisplayName": cgspInstDisplayName,
       "cgspInstDescription": cgspInstDescription,
       "cgspInstTFR": cgspInstTFR,
       "cgspInstCongestionsLevels": cgspInstCongestionsLevels,
       "cgspInstFastRestart": cgspInstFastRestart,
       "cgspInstDistSccpUnseq": cgspInstDistSccpUnseq,
       "cgspInstSummaryRoutingException": cgspInstSummaryRoutingException,
       "cgspInstNumber": cgspInstNumber,
       "cgspInstRouteTableName": cgspInstRouteTableName,
       "cgspInstRowStatus": cgspInstRowStatus,
       "cgspInstSccpWrrOpcShift": cgspInstSccpWrrOpcShift,
       "cgspInstSccpWrrOption": cgspInstSccpWrrOption,
       "cgspInstTimerTable": cgspInstTimerTable,
       "cgspInstTimerTableEntry": cgspInstTimerTableEntry,
       "cgspInstTimerNumber": cgspInstTimerNumber,
       "cgspInstTimerValue": cgspInstTimerValue,
       "cgspInstTimerRowStatus": cgspInstTimerRowStatus,
       "cgspInstUPUTable": cgspInstUPUTable,
       "cgspInstUPUTableEntry": cgspInstUPUTableEntry,
       "cgspMtp3SI": cgspMtp3SI,
       "cgspInstSIUPUReceived": cgspInstSIUPUReceived,
       "cgspInstSIUPUTransmitted": cgspInstSIUPUTransmitted,
       "cgspInstUserPartDisplay": cgspInstUserPartDisplay,
       "cgspPointCode": cgspPointCode,
       "cgspPointCodeTable": cgspPointCodeTable,
       "cgspPointCodeTableEntry": cgspPointCodeTableEntry,
       "cgspPointCodeNi": cgspPointCodeNi,
       "cgspPointCodeBin": cgspPointCodeBin,
       "cgspPointCodeType": cgspPointCodeType,
       "cgspPointCodeDisplay": cgspPointCodeDisplay,
       "cgspPointCodeRowStatus": cgspPointCodeRowStatus,
       "cgspLinkset": cgspLinkset,
       "cgspLinksetTable": cgspLinksetTable,
       "cgspLinksetTableEntry": cgspLinksetTableEntry,
       "cgspLinksetName": cgspLinksetName,
       "cgspLinksetSourcePointCode": cgspLinksetSourcePointCode,
       "cgspLinksetSourceDisplayPC": cgspLinksetSourceDisplayPC,
       "cgspLinksetAdjacentPointCode": cgspLinksetAdjacentPointCode,
       "cgspLinksetAdjacentDisplayPC": cgspLinksetAdjacentDisplayPC,
       "cgspLinksetState": cgspLinksetState,
       "cgspLinksetInboundAcl": cgspLinksetInboundAcl,
       "cgspLinksetOutboundAcl": cgspLinksetOutboundAcl,
       "cgspLinksetAccountingMtp3": cgspLinksetAccountingMtp3,
       "cgspLinksetAccountingGtt": cgspLinksetAccountingGtt,
       "cgspLinksetNumLinks": cgspLinksetNumLinks,
       "cgspLinksetDurationInService": cgspLinksetDurationInService,
       "cgspLinksetDurationOutService": cgspLinksetDurationOutService,
       "cgspLinksetActPriority": cgspLinksetActPriority,
       "cgspLinksetDisplayName": cgspLinksetDisplayName,
       "cgspLinksetDescription": cgspLinksetDescription,
       "cgspLinksetRotateSlsEnable": cgspLinksetRotateSlsEnable,
       "cgspLinksetRotateSlsShift": cgspLinksetRotateSlsShift,
       "cgspLinksetProfileName": cgspLinksetProfileName,
       "cgspLinksetAdjacentInst": cgspLinksetAdjacentInst,
       "cgspLinksetRowStatus": cgspLinksetRowStatus,
       "cgspLinksetTimerTable": cgspLinksetTimerTable,
       "cgspLinksetTimerTableEntry": cgspLinksetTimerTableEntry,
       "cgspLinksetTimerNumber": cgspLinksetTimerNumber,
       "cgspLinksetTimerValue": cgspLinksetTimerValue,
       "cgspLinksetTimerRowStatus": cgspLinksetTimerRowStatus,
       "cgspLink": cgspLink,
       "cgspLinkTable": cgspLinkTable,
       "cgspLinkTableEntry": cgspLinkTableEntry,
       "cgspLinkSlc": cgspLinkSlc,
       "cgspLinkDescription": cgspLinkDescription,
       "cgspLinkState": cgspLinkState,
       "cgspLinkReason": cgspLinkReason,
       "cgspLinkType": cgspLinkType,
       "cgspLinkifIndex": cgspLinkifIndex,
       "cgspLinkSctpAssociation": cgspLinkSctpAssociation,
       "cgspLinkXmitQueueDepth": cgspLinkXmitQueueDepth,
       "cgspLinkXmitQueueDepthHigh": cgspLinkXmitQueueDepthHigh,
       "cgspLinkXmitQueueDepthHighRT": cgspLinkXmitQueueDepthHighRT,
       "cgspLinkCongestionState": cgspLinkCongestionState,
       "cgspLinkCongestionAbate1": cgspLinkCongestionAbate1,
       "cgspLinkCongestionAbate2": cgspLinkCongestionAbate2,
       "cgspLinkCongestionAbate3": cgspLinkCongestionAbate3,
       "cgspLinkCongestionOnset1": cgspLinkCongestionOnset1,
       "cgspLinkCongestionOnset2": cgspLinkCongestionOnset2,
       "cgspLinkCongestionOnset3": cgspLinkCongestionOnset3,
       "cgspLinkSigLinkTest": cgspLinkSigLinkTest,
       "cgspLinkQ752T1E1": cgspLinkQ752T1E1,
       "cgspLinkQ752T1E2": cgspLinkQ752T1E2,
       "cgspLinkQ752T1E3": cgspLinkQ752T1E3,
       "cgspLinkQ752T1E5": cgspLinkQ752T1E5,
       "cgspLinkQ752T1E7": cgspLinkQ752T1E7,
       "cgspLinkQ752T1E8": cgspLinkQ752T1E8,
       "cgspLinkQ752T1E9": cgspLinkQ752T1E9,
       "cgspLinkQ752T1E10": cgspLinkQ752T1E10,
       "cgspLinkQ752T1E11": cgspLinkQ752T1E11,
       "cgspLinkQ752T2E1": cgspLinkQ752T2E1,
       "cgspLinkQ752T2E5": cgspLinkQ752T2E5,
       "cgspLinkQ752T2E6": cgspLinkQ752T2E6,
       "cgspLinkQ752T2E7": cgspLinkQ752T2E7,
       "cgspLinkQ752T2E9": cgspLinkQ752T2E9,
       "cgspLinkQ752T2E10": cgspLinkQ752T2E10,
       "cgspLinkQ752T2E15": cgspLinkQ752T2E15,
       "cgspLinkQ752T2E16": cgspLinkQ752T2E16,
       "cgspLinkQ752T2E18": cgspLinkQ752T2E18,
       "cgspLinkQ752T3E1": cgspLinkQ752T3E1,
       "cgspLinkQ752T3E2Bytes": cgspLinkQ752T3E2Bytes,
       "cgspLinkQ752T3E2Packets": cgspLinkQ752T3E2Packets,
       "cgspLinkQ752T3E3": cgspLinkQ752T3E3,
       "cgspLinkQ752T3E4": cgspLinkQ752T3E4,
       "cgspLinkQ752T3E5": cgspLinkQ752T3E5,
       "cgspLinkQ752T3E6": cgspLinkQ752T3E6,
       "cgspLinkQ752T3E7": cgspLinkQ752T3E7,
       "cgspLinkQ752T3E10L1": cgspLinkQ752T3E10L1,
       "cgspLinkQ752T3E10L2": cgspLinkQ752T3E10L2,
       "cgspLinkQ752T3E10L3": cgspLinkQ752T3E10L3,
       "cgspLinkQ752T3E11L1": cgspLinkQ752T3E11L1,
       "cgspLinkQ752T3E11L2": cgspLinkQ752T3E11L2,
       "cgspLinkQ752T3E11L3": cgspLinkQ752T3E11L3,
       "cgspLinkLocalPeerPort": cgspLinkLocalPeerPort,
       "cgspLinkRemotePeerPort": cgspLinkRemotePeerPort,
       "cgspLinkQosClass": cgspLinkQosClass,
       "cgspLinkDisplayName": cgspLinkDisplayName,
       "cgspLinkDroppedPkts": cgspLinkDroppedPkts,
       "cgspLinkTransmittedLSSUs": cgspLinkTransmittedLSSUs,
       "cgspLinkReceivedLSSUs": cgspLinkReceivedLSSUs,
       "cgspLinkProtocolDetails": cgspLinkProtocolDetails,
       "cgspLinkLsacState": cgspLinkLsacState,
       "cgspLinkTsrcState": cgspLinkTsrcState,
       "cgspLinkTcocState": cgspLinkTcocState,
       "cgspLinkTcocLocalBSNT": cgspLinkTcocLocalBSNT,
       "cgspLinkTcocRemoteBSNT": cgspLinkTcocRemoteBSNT,
       "cgspLinkTcbcState": cgspLinkTcbcState,
       "cgspLinkReceivedSIBs": cgspLinkReceivedSIBs,
       "cgspLinkTransmittedSIBs": cgspLinkTransmittedSIBs,
       "cgspLinkMtp2T01Counts": cgspLinkMtp2T01Counts,
       "cgspLinkMtp2T02Counts": cgspLinkMtp2T02Counts,
       "cgspLinkMtp2T03Counts": cgspLinkMtp2T03Counts,
       "cgspLinkMtp2T04Counts": cgspLinkMtp2T04Counts,
       "cgspLinkMtp2T05Counts": cgspLinkMtp2T05Counts,
       "cgspLinkMtp2T06Counts": cgspLinkMtp2T06Counts,
       "cgspLinkMtp2T07Counts": cgspLinkMtp2T07Counts,
       "cgspLinkOMAERMCounts": cgspLinkOMAERMCounts,
       "cgspLinkOMAERMFailCounts": cgspLinkOMAERMFailCounts,
       "cgspLinkOMSURMCounts": cgspLinkOMSURMCounts,
       "cgspLinkOMSURMFailCounts": cgspLinkOMSURMFailCounts,
       "cgspLinkPlanCapacityRcvd": cgspLinkPlanCapacityRcvd,
       "cgspLinkUtilThresholdRcvd": cgspLinkUtilThresholdRcvd,
       "cgspLinkUtilizationRcvd": cgspLinkUtilizationRcvd,
       "cgspLinkUtilStateRcvd": cgspLinkUtilStateRcvd,
       "cgspLinkL2BytesRcvd": cgspLinkL2BytesRcvd,
       "cgspLinkPlanCapacitySent": cgspLinkPlanCapacitySent,
       "cgspLinkUtilThresholdSent": cgspLinkUtilThresholdSent,
       "cgspLinkUtilizationSent": cgspLinkUtilizationSent,
       "cgspLinkUtilStateSent": cgspLinkUtilStateSent,
       "cgspLinkL2BytesSent": cgspLinkL2BytesSent,
       "cgspLinkTestResult": cgspLinkTestResult,
       "cgspLinkRowStatus": cgspLinkRowStatus,
       "cgspLinkSctpAssociationId": cgspLinkSctpAssociationId,
       "cgspLinkQ752T1E12": cgspLinkQ752T1E12,
       "cgspLinkQ752T1E12Errors": cgspLinkQ752T1E12Errors,
       "cgspLinkQ752T2E11": cgspLinkQ752T2E11,
       "cgspLinkQ752T2E17": cgspLinkQ752T2E17,
       "cgspLinkQ752T2E19": cgspLinkQ752T2E19,
       "cgspLinkRxCongestionState": cgspLinkRxCongestionState,
       "cgspLinkTimerTable": cgspLinkTimerTable,
       "cgspLinkTimerTableEntry": cgspLinkTimerTableEntry,
       "cgspLinkTimerNumber": cgspLinkTimerNumber,
       "cgspLinkTimerValue": cgspLinkTimerValue,
       "cgspLinkTimerRowStatus": cgspLinkTimerRowStatus,
       "cgspLinkRemoteIpAddrTable": cgspLinkRemoteIpAddrTable,
       "cgspLinkRemoteIpAddrTableEntry": cgspLinkRemoteIpAddrTableEntry,
       "cgspLinkRemoteIpAddrNumber": cgspLinkRemoteIpAddrNumber,
       "cgspLinkRemoteIpAddrType": cgspLinkRemoteIpAddrType,
       "cgspLinkRemoteIpAddress": cgspLinkRemoteIpAddress,
       "cgspLinkRemoteIpAddrRowStatus": cgspLinkRemoteIpAddrRowStatus,
       "cgspLinkUtilTable": cgspLinkUtilTable,
       "cgspLinkUtilTableEntry": cgspLinkUtilTableEntry,
       "cgspLinkUtilIndex": cgspLinkUtilIndex,
       "cgspLinkUtilRcvd": cgspLinkUtilRcvd,
       "cgspLinkUtilSent": cgspLinkUtilSent,
       "cgspLinkUtilEndTimestamp": cgspLinkUtilEndTimestamp,
       "cgspNotificationsEnable": cgspNotificationsEnable,
       "cgspLsStateChangeNotifEnabled": cgspLsStateChangeNotifEnabled,
       "cgspLnkStateChangeNotifEnabled": cgspLnkStateChangeNotifEnabled,
       "cgspCongestionNotifEnabled": cgspCongestionNotifEnabled,
       "cgspLinkUtilNotifEnabled": cgspLinkUtilNotifEnabled,
       "cgspIsolationNotifEnabled": cgspIsolationNotifEnabled,
       "cgspUPUNotifEnabled": cgspUPUNotifEnabled,
       "cgspNotificationsInfo": cgspNotificationsInfo,
       "cgspUPUIntervalDuration": cgspUPUIntervalDuration,
       "cgspIntervalUPUs": cgspIntervalUPUs,
       "ciscoGspMIBConform": ciscoGspMIBConform,
       "ciscoGspMIBCompliances": ciscoGspMIBCompliances,
       "ciscoGspMIBCompliance": ciscoGspMIBCompliance,
       "ciscoGspMIBComplianceRev1": ciscoGspMIBComplianceRev1,
       "ciscoGspMIBComplianceRev2": ciscoGspMIBComplianceRev2,
       "ciscoGspMIBComplianceRev3": ciscoGspMIBComplianceRev3,
       "ciscoGspMIBComplianceRev4": ciscoGspMIBComplianceRev4,
       "ciscoGspMIBComplianceRev5": ciscoGspMIBComplianceRev5,
       "ciscoGspMIBGroups": ciscoGspMIBGroups,
       "ciscoGspScalarsGroup": ciscoGspScalarsGroup,
       "ciscoGspProfileGroup": ciscoGspProfileGroup,
       "ciscoGspInstanceGroup": ciscoGspInstanceGroup,
       "ciscoGspInstTimerGroup": ciscoGspInstTimerGroup,
       "ciscoGspPointCodeGroup": ciscoGspPointCodeGroup,
       "ciscoGspLinksetGroup": ciscoGspLinksetGroup,
       "ciscoGspLinksetTimerGroup": ciscoGspLinksetTimerGroup,
       "ciscoGspLinkGroup": ciscoGspLinkGroup,
       "ciscoGspLinkTimerGroup": ciscoGspLinkTimerGroup,
       "ciscoGspLinkRemoteIpGroup": ciscoGspLinkRemoteIpGroup,
       "ciscoGspLinkUtilGroup": ciscoGspLinkUtilGroup,
       "ciscoGspNotificationsEnableGroup": ciscoGspNotificationsEnableGroup,
       "ciscoGspNotificationsGroup": ciscoGspNotificationsGroup,
       "ciscoGspLinkGroupRev1": ciscoGspLinkGroupRev1,
       "ciscoGspNotificationsEnableGroupSup1": ciscoGspNotificationsEnableGroupSup1,
       "ciscoGspNotificationsGroupSup1": ciscoGspNotificationsGroupSup1,
       "ciscoGspLinkGroupSup1": ciscoGspLinkGroupSup1,
       "ciscoGspScalarsGroupSup1": ciscoGspScalarsGroupSup1,
       "ciscoGspInstUPUGroup": ciscoGspInstUPUGroup,
       "ciscoGspNotificationsInfoGroup": ciscoGspNotificationsInfoGroup,
       "ciscoGspNotificationsEnableGroupSup2": ciscoGspNotificationsEnableGroupSup2,
       "ciscoGspNotificationsGroupSup2": ciscoGspNotificationsGroupSup2,
       "ciscoGspInstSccpWrrGroup": ciscoGspInstSccpWrrGroup,
       "ciscoGspLinkTableEntryGroupSup1": ciscoGspLinkTableEntryGroupSup1,
       "ciscoGspNotificationsGroupSup3": ciscoGspNotificationsGroupSup3}
)
