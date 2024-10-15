# SNMP MIB module (CISCO-ICSUDSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ICSUDSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:19 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "RFC1406-MIB",
    "dsx1ConfigEntry")

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

ciscoICsuDsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoICsuDsuObjects_ObjectIdentity = ObjectIdentity
ciscoICsuDsuObjects = _CiscoICsuDsuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1)
)
_CiscoICsuDsuGeneral_ObjectIdentity = ObjectIdentity
ciscoICsuDsuGeneral = _CiscoICsuDsuGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1)
)
_CiscoICsuDsuStaticConfigTable_Object = MibTable
ciscoICsuDsuStaticConfigTable = _CiscoICsuDsuStaticConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuStaticConfigTable.setStatus("current")
_CiscoICsuDsuStaticConfigEntry_Object = MibTableRow
ciscoICsuDsuStaticConfigEntry = _CiscoICsuDsuStaticConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1)
)
ciscoICsuDsuStaticConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoICsuDsuStaticConfigEntry.setStatus("current")


class _CiscoICsuDsuType_Type(Integer32):
    """Custom type ciscoICsuDsuType based on Integer32"""
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
        *(("fourWireSwitched56k", 3),
          ("fractionalT1", 1),
          ("twoWireSwitched56k", 2),
          ("unknown", 4))
    )


_CiscoICsuDsuType_Type.__name__ = "Integer32"
_CiscoICsuDsuType_Object = MibTableColumn
ciscoICsuDsuType = _CiscoICsuDsuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 1),
    _CiscoICsuDsuType_Type()
)
ciscoICsuDsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuType.setStatus("current")


class _CiscoICsuDsuHwRevision_Type(DisplayString):
    """Custom type ciscoICsuDsuHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CiscoICsuDsuHwRevision_Type.__name__ = "DisplayString"
_CiscoICsuDsuHwRevision_Object = MibTableColumn
ciscoICsuDsuHwRevision = _CiscoICsuDsuHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 2),
    _CiscoICsuDsuHwRevision_Type()
)
ciscoICsuDsuHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuHwRevision.setStatus("current")


class _CiscoICsuDsuSwRevision_Type(DisplayString):
    """Custom type ciscoICsuDsuSwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CiscoICsuDsuSwRevision_Type.__name__ = "DisplayString"
_CiscoICsuDsuSwRevision_Object = MibTableColumn
ciscoICsuDsuSwRevision = _CiscoICsuDsuSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 3),
    _CiscoICsuDsuSwRevision_Type()
)
ciscoICsuDsuSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSwRevision.setStatus("current")


class _CiscoICsuDsuProtocolRevision_Type(DisplayString):
    """Custom type ciscoICsuDsuProtocolRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CiscoICsuDsuProtocolRevision_Type.__name__ = "DisplayString"
_CiscoICsuDsuProtocolRevision_Object = MibTableColumn
ciscoICsuDsuProtocolRevision = _CiscoICsuDsuProtocolRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 4),
    _CiscoICsuDsuProtocolRevision_Type()
)
ciscoICsuDsuProtocolRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuProtocolRevision.setStatus("current")
_CiscoICsuDsuTestReportTable_Object = MibTable
ciscoICsuDsuTestReportTable = _CiscoICsuDsuTestReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuTestReportTable.setStatus("current")
_CiscoICsuDsuTestReportEntry_Object = MibTableRow
ciscoICsuDsuTestReportEntry = _CiscoICsuDsuTestReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1)
)
ciscoICsuDsuTestReportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoICsuDsuTestReportEntry.setStatus("current")
_CiscoICsuDsuLastSelfTestResult_Type = Integer32
_CiscoICsuDsuLastSelfTestResult_Object = MibTableColumn
ciscoICsuDsuLastSelfTestResult = _CiscoICsuDsuLastSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 1),
    _CiscoICsuDsuLastSelfTestResult_Type()
)
ciscoICsuDsuLastSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLastSelfTestResult.setStatus("current")
_CiscoICsuDsuTimeOfLastSelfTest_Type = TimeStamp
_CiscoICsuDsuTimeOfLastSelfTest_Object = MibTableColumn
ciscoICsuDsuTimeOfLastSelfTest = _CiscoICsuDsuTimeOfLastSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 2),
    _CiscoICsuDsuTimeOfLastSelfTest_Type()
)
ciscoICsuDsuTimeOfLastSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuTimeOfLastSelfTest.setStatus("current")
_CiscoICsuDsuNumResets_Type = Counter32
_CiscoICsuDsuNumResets_Object = MibTableColumn
ciscoICsuDsuNumResets = _CiscoICsuDsuNumResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 3),
    _CiscoICsuDsuNumResets_Type()
)
ciscoICsuDsuNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuNumResets.setStatus("current")
_CiscoICsuDsuTimeOfLastReset_Type = TimeStamp
_CiscoICsuDsuTimeOfLastReset_Object = MibTableColumn
ciscoICsuDsuTimeOfLastReset = _CiscoICsuDsuTimeOfLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 4),
    _CiscoICsuDsuTimeOfLastReset_Type()
)
ciscoICsuDsuTimeOfLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuTimeOfLastReset.setStatus("current")


class _CiscoICsuDsuLoopbackStatus_Type(Integer32):
    """Custom type ciscoICsuDsuLoopbackStatus based on Integer32"""
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
        *(("completed", 1),
          ("failed", 4),
          ("inProgress", 2),
          ("neverPerformed", 3),
          ("noSyncWithTestPattern", 5))
    )


_CiscoICsuDsuLoopbackStatus_Type.__name__ = "Integer32"
_CiscoICsuDsuLoopbackStatus_Object = MibTableColumn
ciscoICsuDsuLoopbackStatus = _CiscoICsuDsuLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 5),
    _CiscoICsuDsuLoopbackStatus_Type()
)
ciscoICsuDsuLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackStatus.setStatus("current")
_CiscoICsuDsuLoopbackNumErrors_Type = Integer32
_CiscoICsuDsuLoopbackNumErrors_Object = MibTableColumn
ciscoICsuDsuLoopbackNumErrors = _CiscoICsuDsuLoopbackNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 6),
    _CiscoICsuDsuLoopbackNumErrors_Type()
)
ciscoICsuDsuLoopbackNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackNumErrors.setStatus("current")
_CiscoICsuDsuLoopbackDuration_Type = TimeTicks
_CiscoICsuDsuLoopbackDuration_Object = MibTableColumn
ciscoICsuDsuLoopbackDuration = _CiscoICsuDsuLoopbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 7),
    _CiscoICsuDsuLoopbackDuration_Type()
)
ciscoICsuDsuLoopbackDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackDuration.setStatus("current")


class _CiscoICsuDsuLoopbackPoint_Type(Integer32):
    """Custom type ciscoICsuDsuLoopbackPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dteFull", 2),
          ("dtePayload", 1),
          ("lineFull", 3),
          ("linePayload", 4),
          ("remoteFull", 6),
          ("remotePayload", 7),
          ("remoteSmartJack", 5))
    )


_CiscoICsuDsuLoopbackPoint_Type.__name__ = "Integer32"
_CiscoICsuDsuLoopbackPoint_Object = MibTableColumn
ciscoICsuDsuLoopbackPoint = _CiscoICsuDsuLoopbackPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 8),
    _CiscoICsuDsuLoopbackPoint_Type()
)
ciscoICsuDsuLoopbackPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackPoint.setStatus("current")


class _CiscoICsuDsuLoopbackPattern_Type(Integer32):
    """Custom type ciscoICsuDsuLoopbackPattern based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("noPattern", 1),
          ("pattern0In1", 3),
          ("pattern1In1", 4),
          ("pattern1In2", 5),
          ("pattern1In3", 6),
          ("pattern1In5", 7),
          ("pattern1In8", 8),
          ("pattern2047", 11),
          ("pattern3In24", 9),
          ("pattern511", 12),
          ("patternQRW", 2),
          ("patternStressDDS1", 13),
          ("patternStressDDS2", 14),
          ("patternStressDDS3", 15),
          ("patternStressDDS4", 16),
          ("patternUser", 10))
    )


_CiscoICsuDsuLoopbackPattern_Type.__name__ = "Integer32"
_CiscoICsuDsuLoopbackPattern_Object = MibTableColumn
ciscoICsuDsuLoopbackPattern = _CiscoICsuDsuLoopbackPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 9),
    _CiscoICsuDsuLoopbackPattern_Type()
)
ciscoICsuDsuLoopbackPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackPattern.setStatus("current")


class _CiscoICsuDsuUserDefinedPattern_Type(DisplayString):
    """Custom type ciscoICsuDsuUserDefinedPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CiscoICsuDsuUserDefinedPattern_Type.__name__ = "DisplayString"
_CiscoICsuDsuUserDefinedPattern_Object = MibTableColumn
ciscoICsuDsuUserDefinedPattern = _CiscoICsuDsuUserDefinedPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 10),
    _CiscoICsuDsuUserDefinedPattern_Type()
)
ciscoICsuDsuUserDefinedPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuUserDefinedPattern.setStatus("current")


class _CiscoICsuDsuLoopbackCode_Type(Integer32):
    """Custom type ciscoICsuDsuLoopbackCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("standard", 1),
          ("v54", 3))
    )


_CiscoICsuDsuLoopbackCode_Type.__name__ = "Integer32"
_CiscoICsuDsuLoopbackCode_Object = MibTableColumn
ciscoICsuDsuLoopbackCode = _CiscoICsuDsuLoopbackCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 11),
    _CiscoICsuDsuLoopbackCode_Type()
)
ciscoICsuDsuLoopbackCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuLoopbackCode.setStatus("current")
_CiscoICsuDsuEndTimeOfLastLoopback_Type = TimeStamp
_CiscoICsuDsuEndTimeOfLastLoopback_Object = MibTableColumn
ciscoICsuDsuEndTimeOfLastLoopback = _CiscoICsuDsuEndTimeOfLastLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 12),
    _CiscoICsuDsuEndTimeOfLastLoopback_Type()
)
ciscoICsuDsuEndTimeOfLastLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuEndTimeOfLastLoopback.setStatus("current")
_CiscoICsuDsuT1_ObjectIdentity = ObjectIdentity
ciscoICsuDsuT1 = _CiscoICsuDsuT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2)
)
_CiscoICsuDsuT1ConfigTable_Object = MibTable
ciscoICsuDsuT1ConfigTable = _CiscoICsuDsuT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuT1ConfigTable.setStatus("current")
_CiscoICsuDsuT1ConfigEntry_Object = MibTableRow
ciscoICsuDsuT1ConfigEntry = _CiscoICsuDsuT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuT1ConfigEntry.setStatus("current")


class _CiscoICsuDsuT1LineBuildOut_Type(Integer32):
    """Custom type ciscoICsuDsuT1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("buildOut0", 1),
          ("buildOut15", 3),
          ("buildOut7p5", 2))
    )


_CiscoICsuDsuT1LineBuildOut_Type.__name__ = "Integer32"
_CiscoICsuDsuT1LineBuildOut_Object = MibTableColumn
ciscoICsuDsuT1LineBuildOut = _CiscoICsuDsuT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 1),
    _CiscoICsuDsuT1LineBuildOut_Type()
)
ciscoICsuDsuT1LineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1LineBuildOut.setStatus("current")


class _CiscoICsuDsuT1DteLineCode_Type(Integer32):
    """Custom type ciscoICsuDsuT1DteLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_CiscoICsuDsuT1DteLineCode_Type.__name__ = "Integer32"
_CiscoICsuDsuT1DteLineCode_Object = MibTableColumn
ciscoICsuDsuT1DteLineCode = _CiscoICsuDsuT1DteLineCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 2),
    _CiscoICsuDsuT1DteLineCode_Type()
)
ciscoICsuDsuT1DteLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1DteLineCode.setStatus("current")
_CiscoICsuDsuT1SupportRemoteAlarmIndication_Type = TruthValue
_CiscoICsuDsuT1SupportRemoteAlarmIndication_Object = MibTableColumn
ciscoICsuDsuT1SupportRemoteAlarmIndication = _CiscoICsuDsuT1SupportRemoteAlarmIndication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 3),
    _CiscoICsuDsuT1SupportRemoteAlarmIndication_Type()
)
ciscoICsuDsuT1SupportRemoteAlarmIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1SupportRemoteAlarmIndication.setStatus("current")


class _CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type(Integer32):
    """Custom type ciscoICsuDsuT1FullBandwidthRemoteLoopcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("disabled", 3),
          ("standard", 1))
    )


_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type.__name__ = "Integer32"
_CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Object = MibTableColumn
ciscoICsuDsuT1FullBandwidthRemoteLoopcode = _CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 4),
    _CiscoICsuDsuT1FullBandwidthRemoteLoopcode_Type()
)
ciscoICsuDsuT1FullBandwidthRemoteLoopcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1FullBandwidthRemoteLoopcode.setStatus("current")


class _CiscoICsuDsuT1PayloadRemoteLoopcode_Type(Integer32):
    """Custom type ciscoICsuDsuT1PayloadRemoteLoopcode based on Integer32"""
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
        *(("alternate", 2),
          ("disabled", 3),
          ("standard", 1),
          ("v54", 4))
    )


_CiscoICsuDsuT1PayloadRemoteLoopcode_Type.__name__ = "Integer32"
_CiscoICsuDsuT1PayloadRemoteLoopcode_Object = MibTableColumn
ciscoICsuDsuT1PayloadRemoteLoopcode = _CiscoICsuDsuT1PayloadRemoteLoopcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 5),
    _CiscoICsuDsuT1PayloadRemoteLoopcode_Type()
)
ciscoICsuDsuT1PayloadRemoteLoopcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1PayloadRemoteLoopcode.setStatus("current")
_CiscoICsuDsuT1StatusTable_Object = MibTable
ciscoICsuDsuT1StatusTable = _CiscoICsuDsuT1StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuT1StatusTable.setStatus("current")
_CiscoICsuDsuT1StatusEntry_Object = MibTableRow
ciscoICsuDsuT1StatusEntry = _CiscoICsuDsuT1StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1)
)
ciscoICsuDsuT1StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoICsuDsuT1StatusEntry.setStatus("current")
_CiscoICsuDsuT1LoopStatus_Type = Integer32
_CiscoICsuDsuT1LoopStatus_Object = MibTableColumn
ciscoICsuDsuT1LoopStatus = _CiscoICsuDsuT1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 1),
    _CiscoICsuDsuT1LoopStatus_Type()
)
ciscoICsuDsuT1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1LoopStatus.setStatus("current")
_CiscoICsuDsuT1LossOfSignals_Type = Counter32
_CiscoICsuDsuT1LossOfSignals_Object = MibTableColumn
ciscoICsuDsuT1LossOfSignals = _CiscoICsuDsuT1LossOfSignals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 2),
    _CiscoICsuDsuT1LossOfSignals_Type()
)
ciscoICsuDsuT1LossOfSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1LossOfSignals.setStatus("current")
_CiscoICsuDsuT1LossOfFrames_Type = Counter32
_CiscoICsuDsuT1LossOfFrames_Object = MibTableColumn
ciscoICsuDsuT1LossOfFrames = _CiscoICsuDsuT1LossOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 3),
    _CiscoICsuDsuT1LossOfFrames_Type()
)
ciscoICsuDsuT1LossOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1LossOfFrames.setStatus("current")
_CiscoICsuDsuT1RemoteAlarmIndications_Type = Counter32
_CiscoICsuDsuT1RemoteAlarmIndications_Object = MibTableColumn
ciscoICsuDsuT1RemoteAlarmIndications = _CiscoICsuDsuT1RemoteAlarmIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 4),
    _CiscoICsuDsuT1RemoteAlarmIndications_Type()
)
ciscoICsuDsuT1RemoteAlarmIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1RemoteAlarmIndications.setStatus("current")
_CiscoICsuDsuT1AlarmIndicationSignals_Type = Counter32
_CiscoICsuDsuT1AlarmIndicationSignals_Object = MibTableColumn
ciscoICsuDsuT1AlarmIndicationSignals = _CiscoICsuDsuT1AlarmIndicationSignals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 5),
    _CiscoICsuDsuT1AlarmIndicationSignals_Type()
)
ciscoICsuDsuT1AlarmIndicationSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuT1AlarmIndicationSignals.setStatus("current")
_CiscoICsuDsuSw56k_ObjectIdentity = ObjectIdentity
ciscoICsuDsuSw56k = _CiscoICsuDsuSw56k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3)
)
_CiscoICsuDsuSw56kConfigTable_Object = MibTable
ciscoICsuDsuSw56kConfigTable = _CiscoICsuDsuSw56kConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kConfigTable.setStatus("current")
_CiscoICsuDsuSw56kConfigEntry_Object = MibTableRow
ciscoICsuDsuSw56kConfigEntry = _CiscoICsuDsuSw56kConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1)
)
ciscoICsuDsuSw56kConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kConfigEntry.setStatus("current")


class _CiscoICsuDsuSw56kNetworkType_Type(Integer32):
    """Custom type ciscoICsuDsuSw56kNetworkType based on Integer32"""
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
        *(("att", 2),
          ("dds", 1),
          ("otherCarrier", 4),
          ("sprint", 3))
    )


_CiscoICsuDsuSw56kNetworkType_Type.__name__ = "Integer32"
_CiscoICsuDsuSw56kNetworkType_Object = MibTableColumn
ciscoICsuDsuSw56kNetworkType = _CiscoICsuDsuSw56kNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 1),
    _CiscoICsuDsuSw56kNetworkType_Type()
)
ciscoICsuDsuSw56kNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kNetworkType.setStatus("current")


class _CiscoICsuDsuSw56kClockSource_Type(Integer32):
    """Custom type ciscoICsuDsuSw56kClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("line", 2))
    )


_CiscoICsuDsuSw56kClockSource_Type.__name__ = "Integer32"
_CiscoICsuDsuSw56kClockSource_Object = MibTableColumn
ciscoICsuDsuSw56kClockSource = _CiscoICsuDsuSw56kClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 2),
    _CiscoICsuDsuSw56kClockSource_Type()
)
ciscoICsuDsuSw56kClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kClockSource.setStatus("current")


class _CiscoICsuDsuSw56kLoopRate_Type(Integer32):
    """Custom type ciscoICsuDsuSw56kLoopRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bps19k", 4),
          ("bps2400", 1),
          ("bps38k", 5),
          ("bps4800", 2),
          ("bps56k", 6),
          ("bps64k", 7),
          ("bps9600", 3))
    )


_CiscoICsuDsuSw56kLoopRate_Type.__name__ = "Integer32"
_CiscoICsuDsuSw56kLoopRate_Object = MibTableColumn
ciscoICsuDsuSw56kLoopRate = _CiscoICsuDsuSw56kLoopRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 3),
    _CiscoICsuDsuSw56kLoopRate_Type()
)
ciscoICsuDsuSw56kLoopRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLoopRate.setStatus("current")
_CiscoICsuDsuSw56kScramblerEnabled_Type = TruthValue
_CiscoICsuDsuSw56kScramblerEnabled_Object = MibTableColumn
ciscoICsuDsuSw56kScramblerEnabled = _CiscoICsuDsuSw56kScramblerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 4),
    _CiscoICsuDsuSw56kScramblerEnabled_Type()
)
ciscoICsuDsuSw56kScramblerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kScramblerEnabled.setStatus("current")
_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Type = TruthValue
_CiscoICsuDsuSw56kRemoteLoopbackEnabled_Object = MibTableColumn
ciscoICsuDsuSw56kRemoteLoopbackEnabled = _CiscoICsuDsuSw56kRemoteLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 5),
    _CiscoICsuDsuSw56kRemoteLoopbackEnabled_Type()
)
ciscoICsuDsuSw56kRemoteLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kRemoteLoopbackEnabled.setStatus("current")
_CiscoICsuDsuSw56kLineStatusTable_Object = MibTable
ciscoICsuDsuSw56kLineStatusTable = _CiscoICsuDsuSw56kLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLineStatusTable.setStatus("current")
_CiscoICsuDsuSw56kLineStatusEntry_Object = MibTableRow
ciscoICsuDsuSw56kLineStatusEntry = _CiscoICsuDsuSw56kLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1)
)
ciscoICsuDsuSw56kLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLineStatusEntry.setStatus("current")


class _CiscoICsuDsuSw56kDialingStatus_Type(Integer32):
    """Custom type ciscoICsuDsuSw56kDialingStatus based on Integer32"""
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
        *(("dialing", 2),
          ("idle", 1),
          ("noAnswer", 6),
          ("noWinkFromSwitch", 4),
          ("numberBusy", 5),
          ("online", 3))
    )


_CiscoICsuDsuSw56kDialingStatus_Type.__name__ = "Integer32"
_CiscoICsuDsuSw56kDialingStatus_Object = MibTableColumn
ciscoICsuDsuSw56kDialingStatus = _CiscoICsuDsuSw56kDialingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 1),
    _CiscoICsuDsuSw56kDialingStatus_Type()
)
ciscoICsuDsuSw56kDialingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kDialingStatus.setStatus("current")
_CiscoICsuDsuSw56kLoopStatus_Type = Integer32
_CiscoICsuDsuSw56kLoopStatus_Object = MibTableColumn
ciscoICsuDsuSw56kLoopStatus = _CiscoICsuDsuSw56kLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 2),
    _CiscoICsuDsuSw56kLoopStatus_Type()
)
ciscoICsuDsuSw56kLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLoopStatus.setStatus("current")
_CiscoICsuDsuSw56kReceivedOosOofs_Type = Counter32
_CiscoICsuDsuSw56kReceivedOosOofs_Object = MibTableColumn
ciscoICsuDsuSw56kReceivedOosOofs = _CiscoICsuDsuSw56kReceivedOosOofs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 3),
    _CiscoICsuDsuSw56kReceivedOosOofs_Type()
)
ciscoICsuDsuSw56kReceivedOosOofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kReceivedOosOofs.setStatus("current")
_CiscoICsuDsuSw56kLostSealingCurrents_Type = Counter32
_CiscoICsuDsuSw56kLostSealingCurrents_Object = MibTableColumn
ciscoICsuDsuSw56kLostSealingCurrents = _CiscoICsuDsuSw56kLostSealingCurrents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 4),
    _CiscoICsuDsuSw56kLostSealingCurrents_Type()
)
ciscoICsuDsuSw56kLostSealingCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLostSealingCurrents.setStatus("current")
_CiscoICsuDsuSw56kLostReceiveSignals_Type = Counter32
_CiscoICsuDsuSw56kLostReceiveSignals_Object = MibTableColumn
ciscoICsuDsuSw56kLostReceiveSignals = _CiscoICsuDsuSw56kLostReceiveSignals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 5),
    _CiscoICsuDsuSw56kLostReceiveSignals_Type()
)
ciscoICsuDsuSw56kLostReceiveSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLostReceiveSignals.setStatus("current")
_CiscoICsuDsuSw56kLostFrameSyncs_Type = Counter32
_CiscoICsuDsuSw56kLostFrameSyncs_Object = MibTableColumn
ciscoICsuDsuSw56kLostFrameSyncs = _CiscoICsuDsuSw56kLostFrameSyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 6),
    _CiscoICsuDsuSw56kLostFrameSyncs_Type()
)
ciscoICsuDsuSw56kLostFrameSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLostFrameSyncs.setStatus("current")
_CiscoICsuDsuSw56kLoopRateSearches_Type = Counter32
_CiscoICsuDsuSw56kLoopRateSearches_Object = MibTableColumn
ciscoICsuDsuSw56kLoopRateSearches = _CiscoICsuDsuSw56kLoopRateSearches_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 7),
    _CiscoICsuDsuSw56kLoopRateSearches_Type()
)
ciscoICsuDsuSw56kLoopRateSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLoopRateSearches.setStatus("current")
_CiscoICsuDsuMIBNotificationEnables_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBNotificationEnables = _CiscoICsuDsuMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 2)
)


class _CiscoICsuDsuEnableT1LoopStatusNotification_Type(TruthValue):
    """Custom type ciscoICsuDsuEnableT1LoopStatusNotification based on TruthValue"""


_CiscoICsuDsuEnableT1LoopStatusNotification_Object = MibScalar
ciscoICsuDsuEnableT1LoopStatusNotification = _CiscoICsuDsuEnableT1LoopStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 1),
    _CiscoICsuDsuEnableT1LoopStatusNotification_Type()
)
ciscoICsuDsuEnableT1LoopStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoICsuDsuEnableT1LoopStatusNotification.setStatus("current")


class _CiscoICsuDsuEnableSw56kLoopStatusNotification_Type(TruthValue):
    """Custom type ciscoICsuDsuEnableSw56kLoopStatusNotification based on TruthValue"""


_CiscoICsuDsuEnableSw56kLoopStatusNotification_Object = MibScalar
ciscoICsuDsuEnableSw56kLoopStatusNotification = _CiscoICsuDsuEnableSw56kLoopStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 2),
    _CiscoICsuDsuEnableSw56kLoopStatusNotification_Type()
)
ciscoICsuDsuEnableSw56kLoopStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoICsuDsuEnableSw56kLoopStatusNotification.setStatus("current")
_CiscoICsuDsuMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBNotificationPrefix = _CiscoICsuDsuMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 3)
)
_CiscoICsuDsuMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBNotifications = _CiscoICsuDsuMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0)
)
_CiscoICsuDsuMIBConformance_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBConformance = _CiscoICsuDsuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4)
)
_CiscoICsuDsuMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBCompliances = _CiscoICsuDsuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 1)
)
_CiscoICsuDsuMIBGroups_ObjectIdentity = ObjectIdentity
ciscoICsuDsuMIBGroups = _CiscoICsuDsuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("CISCO-ICSUDSU-MIB",
     "ciscoICsuDsuT1ConfigEntry")
)
ciscoICsuDsuT1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

ciscoICsuDsuMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 1)
)
ciscoICsuDsuMIBGroup.setObjects(
      *(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuType"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuHwRevision"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSwRevision"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuProtocolRevision"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLastSelfTestResult"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuTimeOfLastSelfTest"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuNumResets"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuTimeOfLastReset"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackStatus"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackNumErrors"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackDuration"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackPoint"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackPattern"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuUserDefinedPattern"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackCode"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEndTimeOfLastLoopback"))
)
if mibBuilder.loadTexts:
    ciscoICsuDsuMIBGroup.setStatus("current")

ciscoICsuDsuMIBT1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 2)
)
ciscoICsuDsuMIBT1Group.setObjects(
      *(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LineBuildOut"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1DteLineCode"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1SupportRemoteAlarmIndication"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1FullBandwidthRemoteLoopcode"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1PayloadRemoteLoopcode"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LoopStatus"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LossOfSignals"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LossOfFrames"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1RemoteAlarmIndications"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1AlarmIndicationSignals"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEnableT1LoopStatusNotification"))
)
if mibBuilder.loadTexts:
    ciscoICsuDsuMIBT1Group.setStatus("current")

ciscoICsuDsuMIBSw56kGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 3)
)
ciscoICsuDsuMIBSw56kGroup.setObjects(
      *(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kNetworkType"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kClockSource"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopRate"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kScramblerEnabled"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kRemoteLoopbackEnabled"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kDialingStatus"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopStatus"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kReceivedOosOofs"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostSealingCurrents"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostReceiveSignals"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostFrameSyncs"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopRateSearches"),
        ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEnableSw56kLoopStatusNotification"))
)
if mibBuilder.loadTexts:
    ciscoICsuDsuMIBSw56kGroup.setStatus("current")


# Notification objects

ciscoICsuDsuT1LoopStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 1)
)
ciscoICsuDsuT1LoopStatusNotification.setObjects(
    ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LoopStatus")
)
if mibBuilder.loadTexts:
    ciscoICsuDsuT1LoopStatusNotification.setStatus(
        "current"
    )

ciscoICsuDsuSw56kLoopStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 2)
)
ciscoICsuDsuSw56kLoopStatusNotification.setObjects(
    ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopStatus")
)
if mibBuilder.loadTexts:
    ciscoICsuDsuSw56kLoopStatusNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoICsuDsuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoICsuDsuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ICSUDSU-MIB",
    **{"ciscoICsuDsuMIB": ciscoICsuDsuMIB,
       "ciscoICsuDsuObjects": ciscoICsuDsuObjects,
       "ciscoICsuDsuGeneral": ciscoICsuDsuGeneral,
       "ciscoICsuDsuStaticConfigTable": ciscoICsuDsuStaticConfigTable,
       "ciscoICsuDsuStaticConfigEntry": ciscoICsuDsuStaticConfigEntry,
       "ciscoICsuDsuType": ciscoICsuDsuType,
       "ciscoICsuDsuHwRevision": ciscoICsuDsuHwRevision,
       "ciscoICsuDsuSwRevision": ciscoICsuDsuSwRevision,
       "ciscoICsuDsuProtocolRevision": ciscoICsuDsuProtocolRevision,
       "ciscoICsuDsuTestReportTable": ciscoICsuDsuTestReportTable,
       "ciscoICsuDsuTestReportEntry": ciscoICsuDsuTestReportEntry,
       "ciscoICsuDsuLastSelfTestResult": ciscoICsuDsuLastSelfTestResult,
       "ciscoICsuDsuTimeOfLastSelfTest": ciscoICsuDsuTimeOfLastSelfTest,
       "ciscoICsuDsuNumResets": ciscoICsuDsuNumResets,
       "ciscoICsuDsuTimeOfLastReset": ciscoICsuDsuTimeOfLastReset,
       "ciscoICsuDsuLoopbackStatus": ciscoICsuDsuLoopbackStatus,
       "ciscoICsuDsuLoopbackNumErrors": ciscoICsuDsuLoopbackNumErrors,
       "ciscoICsuDsuLoopbackDuration": ciscoICsuDsuLoopbackDuration,
       "ciscoICsuDsuLoopbackPoint": ciscoICsuDsuLoopbackPoint,
       "ciscoICsuDsuLoopbackPattern": ciscoICsuDsuLoopbackPattern,
       "ciscoICsuDsuUserDefinedPattern": ciscoICsuDsuUserDefinedPattern,
       "ciscoICsuDsuLoopbackCode": ciscoICsuDsuLoopbackCode,
       "ciscoICsuDsuEndTimeOfLastLoopback": ciscoICsuDsuEndTimeOfLastLoopback,
       "ciscoICsuDsuT1": ciscoICsuDsuT1,
       "ciscoICsuDsuT1ConfigTable": ciscoICsuDsuT1ConfigTable,
       "ciscoICsuDsuT1ConfigEntry": ciscoICsuDsuT1ConfigEntry,
       "ciscoICsuDsuT1LineBuildOut": ciscoICsuDsuT1LineBuildOut,
       "ciscoICsuDsuT1DteLineCode": ciscoICsuDsuT1DteLineCode,
       "ciscoICsuDsuT1SupportRemoteAlarmIndication": ciscoICsuDsuT1SupportRemoteAlarmIndication,
       "ciscoICsuDsuT1FullBandwidthRemoteLoopcode": ciscoICsuDsuT1FullBandwidthRemoteLoopcode,
       "ciscoICsuDsuT1PayloadRemoteLoopcode": ciscoICsuDsuT1PayloadRemoteLoopcode,
       "ciscoICsuDsuT1StatusTable": ciscoICsuDsuT1StatusTable,
       "ciscoICsuDsuT1StatusEntry": ciscoICsuDsuT1StatusEntry,
       "ciscoICsuDsuT1LoopStatus": ciscoICsuDsuT1LoopStatus,
       "ciscoICsuDsuT1LossOfSignals": ciscoICsuDsuT1LossOfSignals,
       "ciscoICsuDsuT1LossOfFrames": ciscoICsuDsuT1LossOfFrames,
       "ciscoICsuDsuT1RemoteAlarmIndications": ciscoICsuDsuT1RemoteAlarmIndications,
       "ciscoICsuDsuT1AlarmIndicationSignals": ciscoICsuDsuT1AlarmIndicationSignals,
       "ciscoICsuDsuSw56k": ciscoICsuDsuSw56k,
       "ciscoICsuDsuSw56kConfigTable": ciscoICsuDsuSw56kConfigTable,
       "ciscoICsuDsuSw56kConfigEntry": ciscoICsuDsuSw56kConfigEntry,
       "ciscoICsuDsuSw56kNetworkType": ciscoICsuDsuSw56kNetworkType,
       "ciscoICsuDsuSw56kClockSource": ciscoICsuDsuSw56kClockSource,
       "ciscoICsuDsuSw56kLoopRate": ciscoICsuDsuSw56kLoopRate,
       "ciscoICsuDsuSw56kScramblerEnabled": ciscoICsuDsuSw56kScramblerEnabled,
       "ciscoICsuDsuSw56kRemoteLoopbackEnabled": ciscoICsuDsuSw56kRemoteLoopbackEnabled,
       "ciscoICsuDsuSw56kLineStatusTable": ciscoICsuDsuSw56kLineStatusTable,
       "ciscoICsuDsuSw56kLineStatusEntry": ciscoICsuDsuSw56kLineStatusEntry,
       "ciscoICsuDsuSw56kDialingStatus": ciscoICsuDsuSw56kDialingStatus,
       "ciscoICsuDsuSw56kLoopStatus": ciscoICsuDsuSw56kLoopStatus,
       "ciscoICsuDsuSw56kReceivedOosOofs": ciscoICsuDsuSw56kReceivedOosOofs,
       "ciscoICsuDsuSw56kLostSealingCurrents": ciscoICsuDsuSw56kLostSealingCurrents,
       "ciscoICsuDsuSw56kLostReceiveSignals": ciscoICsuDsuSw56kLostReceiveSignals,
       "ciscoICsuDsuSw56kLostFrameSyncs": ciscoICsuDsuSw56kLostFrameSyncs,
       "ciscoICsuDsuSw56kLoopRateSearches": ciscoICsuDsuSw56kLoopRateSearches,
       "ciscoICsuDsuMIBNotificationEnables": ciscoICsuDsuMIBNotificationEnables,
       "ciscoICsuDsuEnableT1LoopStatusNotification": ciscoICsuDsuEnableT1LoopStatusNotification,
       "ciscoICsuDsuEnableSw56kLoopStatusNotification": ciscoICsuDsuEnableSw56kLoopStatusNotification,
       "ciscoICsuDsuMIBNotificationPrefix": ciscoICsuDsuMIBNotificationPrefix,
       "ciscoICsuDsuMIBNotifications": ciscoICsuDsuMIBNotifications,
       "ciscoICsuDsuT1LoopStatusNotification": ciscoICsuDsuT1LoopStatusNotification,
       "ciscoICsuDsuSw56kLoopStatusNotification": ciscoICsuDsuSw56kLoopStatusNotification,
       "ciscoICsuDsuMIBConformance": ciscoICsuDsuMIBConformance,
       "ciscoICsuDsuMIBCompliances": ciscoICsuDsuMIBCompliances,
       "ciscoICsuDsuMIBCompliance": ciscoICsuDsuMIBCompliance,
       "ciscoICsuDsuMIBGroups": ciscoICsuDsuMIBGroups,
       "ciscoICsuDsuMIBGroup": ciscoICsuDsuMIBGroup,
       "ciscoICsuDsuMIBT1Group": ciscoICsuDsuMIBT1Group,
       "ciscoICsuDsuMIBSw56kGroup": ciscoICsuDsuMIBSw56kGroup}
)
