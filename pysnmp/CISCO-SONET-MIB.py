# SNMP MIB module (CISCO-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:41 2024
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

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(sonetLineCurrentStatus,
 sonetPathCurrentEntry,
 sonetPathCurrentStatus,
 sonetSectionCurrentStatus,
 sonetVTCurrentStatus) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetLineCurrentStatus",
    "sonetPathCurrentEntry",
    "sonetPathCurrentStatus",
    "sonetSectionCurrentStatus",
    "sonetVTCurrentStatus")


# MODULE-IDENTITY

ciscoSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126)
)
ciscoSonetMIB.setRevisions(
        ("2003-03-07 00:00",
         "2002-06-14 00:00",
         "2002-05-22 00:00",
         "2001-10-17 00:00",
         "2000-07-12 00:00",
         "1999-03-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsApsLineFailureCode(Integer32, TextualConvention):
    status = "current"
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
        *(("csApsChannelMismatch", 1),
          ("csApsFEProtectionFailure", 3),
          ("csApsModeMismatch", 4),
          ("csApsProtectionByteFail", 2))
    )



class CsApsLineFailureStatus(Bits, TextualConvention):
    status = "current"


class CsApsLineSwitchReason(Integer32, TextualConvention):
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
        *(("csApsForceSwitch", 8),
          ("csApsLockOut", 9),
          ("csApsManual", 3),
          ("csApsNoSwitch", 10),
          ("csApsOther", 1),
          ("csApsRevertive", 2),
          ("csApsSignalDefectHigh", 5),
          ("csApsSignalDefectLow", 4),
          ("csApsSignalFailureHigh", 7),
          ("csApsSignalFailureLow", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSonetMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSonetMIBNotifs = _CiscoSonetMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 0)
)
_CiscoSonetMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSonetMIBObjects = _CiscoSonetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1)
)
_CsConfig_ObjectIdentity = ObjectIdentity
csConfig = _CsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1)
)
_CsConfigTable_Object = MibTable
csConfigTable = _CsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csConfigTable.setStatus("current")
_CsConfigEntry_Object = MibTableRow
csConfigEntry = _CsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1)
)
csConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csConfigEntry.setStatus("current")


class _CsConfigLoopbackType_Type(Integer32):
    """Custom type csConfigLoopbackType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineLocal", 2),
          ("lineRemote", 3),
          ("noLoopback", 1))
    )


_CsConfigLoopbackType_Type.__name__ = "Integer32"
_CsConfigLoopbackType_Object = MibTableColumn
csConfigLoopbackType = _CsConfigLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 1),
    _CsConfigLoopbackType_Type()
)
csConfigLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csConfigLoopbackType.setStatus("current")


class _CsConfigXmtClockSource_Type(Integer32):
    """Custom type csConfigXmtClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )


_CsConfigXmtClockSource_Type.__name__ = "Integer32"
_CsConfigXmtClockSource_Object = MibTableColumn
csConfigXmtClockSource = _CsConfigXmtClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 2),
    _CsConfigXmtClockSource_Type()
)
csConfigXmtClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csConfigXmtClockSource.setStatus("current")


class _CsConfigFrameScramble_Type(Integer32):
    """Custom type csConfigFrameScramble based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CsConfigFrameScramble_Type.__name__ = "Integer32"
_CsConfigFrameScramble_Object = MibTableColumn
csConfigFrameScramble = _CsConfigFrameScramble_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 3),
    _CsConfigFrameScramble_Type()
)
csConfigFrameScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csConfigFrameScramble.setStatus("current")


class _CsConfigType_Type(Integer32):
    """Custom type csConfigType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("sonetStm1", 2),
          ("sonetStm16", 6),
          ("sonetStm4", 4),
          ("sonetStm64", 8),
          ("sonetSts12c", 3),
          ("sonetSts192c", 7),
          ("sonetSts3", 9),
          ("sonetSts3c", 1),
          ("sonetSts48c", 5))
    )


_CsConfigType_Type.__name__ = "Integer32"
_CsConfigType_Object = MibTableColumn
csConfigType = _CsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 4),
    _CsConfigType_Type()
)
csConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csConfigType.setStatus("current")


class _CsConfigRDIVType_Type(Integer32):
    """Custom type csConfigRDIVType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onebit", 1),
          ("threebit", 3))
    )


_CsConfigRDIVType_Type.__name__ = "Integer32"
_CsConfigRDIVType_Object = MibTableColumn
csConfigRDIVType = _CsConfigRDIVType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 5),
    _CsConfigRDIVType_Type()
)
csConfigRDIVType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csConfigRDIVType.setStatus("current")


class _CsConfigRDIPType_Type(Integer32):
    """Custom type csConfigRDIPType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onebit", 1),
          ("threebit", 3))
    )


_CsConfigRDIPType_Type.__name__ = "Integer32"
_CsConfigRDIPType_Object = MibTableColumn
csConfigRDIPType = _CsConfigRDIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 1, 1, 6),
    _CsConfigRDIPType_Type()
)
csConfigRDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csConfigRDIPType.setStatus("current")
_CsVTConfigTable_Object = MibTable
csVTConfigTable = _CsVTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2)
)
if mibBuilder.loadTexts:
    csVTConfigTable.setStatus("current")
_CsVTConfigEntry_Object = MibTableRow
csVTConfigEntry = _CsVTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csVTConfigEntry.setStatus("current")


class _CsTributaryType_Type(Integer32):
    """Custom type csTributaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vt15vc11", 1),
          ("vt2vc12", 2))
    )


_CsTributaryType_Type.__name__ = "Integer32"
_CsTributaryType_Object = MibTableColumn
csTributaryType = _CsTributaryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1, 1),
    _CsTributaryType_Type()
)
csTributaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTributaryType.setStatus("current")


class _CsTributaryMappingType_Type(Integer32):
    """Custom type csTributaryMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("byteSynchronous", 2))
    )


_CsTributaryMappingType_Type.__name__ = "Integer32"
_CsTributaryMappingType_Object = MibTableColumn
csTributaryMappingType = _CsTributaryMappingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1, 2),
    _CsTributaryMappingType_Type()
)
csTributaryMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTributaryMappingType.setStatus("current")


class _CsTributaryFramingType_Type(Integer32):
    """Custom type csTributaryFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 2),
          ("dsx1ESF", 3),
          ("notApplicable", 1))
    )


_CsTributaryFramingType_Type.__name__ = "Integer32"
_CsTributaryFramingType_Object = MibTableColumn
csTributaryFramingType = _CsTributaryFramingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1, 3),
    _CsTributaryFramingType_Type()
)
csTributaryFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTributaryFramingType.setStatus("current")


class _CsSignallingTransportMode_Type(Integer32):
    """Custom type csSignallingTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearMode", 3),
          ("notApplicable", 1),
          ("signallingTransferMode", 2))
    )


_CsSignallingTransportMode_Type.__name__ = "Integer32"
_CsSignallingTransportMode_Object = MibTableColumn
csSignallingTransportMode = _CsSignallingTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1, 4),
    _CsSignallingTransportMode_Type()
)
csSignallingTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csSignallingTransportMode.setStatus("current")


class _CsTributaryGroupingType_Type(Integer32):
    """Custom type csTributaryGroupingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("au3Grouping", 2),
          ("au4Grouping", 3),
          ("notApplicable", 1))
    )


_CsTributaryGroupingType_Type.__name__ = "Integer32"
_CsTributaryGroupingType_Object = MibTableColumn
csTributaryGroupingType = _CsTributaryGroupingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 1, 2, 1, 5),
    _CsTributaryGroupingType_Type()
)
csTributaryGroupingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csTributaryGroupingType.setStatus("current")
_CsApsConfig_ObjectIdentity = ObjectIdentity
csApsConfig = _CsApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2)
)
_CsApsConfigTable_Object = MibTable
csApsConfigTable = _CsApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csApsConfigTable.setStatus("current")
_CsApsConfigEntry_Object = MibTableRow
csApsConfigEntry = _CsApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1)
)
csApsConfigEntry.setIndexNames(
    (0, "CISCO-SONET-MIB", "csApsWorkingIndex"),
)
if mibBuilder.loadTexts:
    csApsConfigEntry.setStatus("current")
_CsApsWorkingIndex_Type = InterfaceIndex
_CsApsWorkingIndex_Object = MibTableColumn
csApsWorkingIndex = _CsApsWorkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 1),
    _CsApsWorkingIndex_Type()
)
csApsWorkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csApsWorkingIndex.setStatus("current")
_CsApsProtectionIndex_Type = InterfaceIndex
_CsApsProtectionIndex_Object = MibTableColumn
csApsProtectionIndex = _CsApsProtectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 2),
    _CsApsProtectionIndex_Type()
)
csApsProtectionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsProtectionIndex.setStatus("current")


class _CsApsEnable_Type(Integer32):
    """Custom type csApsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csApsDisabled", 1),
          ("csApsEnabled", 2))
    )


_CsApsEnable_Type.__name__ = "Integer32"
_CsApsEnable_Object = MibTableColumn
csApsEnable = _CsApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 3),
    _CsApsEnable_Type()
)
csApsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsEnable.setStatus("current")


class _CsApsArchMode_Type(Integer32):
    """Custom type csApsArchMode based on Integer32"""
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
        *(("anexBOnePlusOne", 3),
          ("onePlusOne", 1),
          ("oneToOne", 2),
          ("straightOnePlusOneNok1k2", 5),
          ("ycableOnePlusOneNok1k2", 4))
    )


_CsApsArchMode_Type.__name__ = "Integer32"
_CsApsArchMode_Object = MibTableColumn
csApsArchMode = _CsApsArchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 4),
    _CsApsArchMode_Type()
)
csApsArchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsArchMode.setStatus("current")


class _CsApsActiveLine_Type(Integer32):
    """Custom type csApsActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csApsNone", 3),
          ("csApsProtectionLine", 2),
          ("csApsWorkingLine", 1))
    )


_CsApsActiveLine_Type.__name__ = "Integer32"
_CsApsActiveLine_Object = MibTableColumn
csApsActiveLine = _CsApsActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 5),
    _CsApsActiveLine_Type()
)
csApsActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsActiveLine.setStatus("current")


class _CsApsSigFaultBER_Type(Unsigned32):
    """Custom type csApsSigFaultBER based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_CsApsSigFaultBER_Type.__name__ = "Unsigned32"
_CsApsSigFaultBER_Object = MibTableColumn
csApsSigFaultBER = _CsApsSigFaultBER_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 6),
    _CsApsSigFaultBER_Type()
)
csApsSigFaultBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsSigFaultBER.setStatus("current")


class _CsApsSigDegradeBER_Type(Unsigned32):
    """Custom type csApsSigDegradeBER based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_CsApsSigDegradeBER_Type.__name__ = "Unsigned32"
_CsApsSigDegradeBER_Object = MibTableColumn
csApsSigDegradeBER = _CsApsSigDegradeBER_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 7),
    _CsApsSigDegradeBER_Type()
)
csApsSigDegradeBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsSigDegradeBER.setStatus("current")


class _CsApsWaitToRestore_Type(Unsigned32):
    """Custom type csApsWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CsApsWaitToRestore_Type.__name__ = "Unsigned32"
_CsApsWaitToRestore_Object = MibTableColumn
csApsWaitToRestore = _CsApsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 8),
    _CsApsWaitToRestore_Type()
)
csApsWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    csApsWaitToRestore.setUnits("minutes")


class _CsApsDirection_Type(Integer32):
    """Custom type csApsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_CsApsDirection_Type.__name__ = "Integer32"
_CsApsDirection_Object = MibTableColumn
csApsDirection = _CsApsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 9),
    _CsApsDirection_Type()
)
csApsDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsDirection.setStatus("current")


class _CsApsRevertive_Type(Integer32):
    """Custom type csApsRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_CsApsRevertive_Type.__name__ = "Integer32"
_CsApsRevertive_Object = MibTableColumn
csApsRevertive = _CsApsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 10),
    _CsApsRevertive_Type()
)
csApsRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsRevertive.setStatus("current")


class _CsApsDirectionOperational_Type(Integer32):
    """Custom type csApsDirectionOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_CsApsDirectionOperational_Type.__name__ = "Integer32"
_CsApsDirectionOperational_Object = MibTableColumn
csApsDirectionOperational = _CsApsDirectionOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 11),
    _CsApsDirectionOperational_Type()
)
csApsDirectionOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsDirectionOperational.setStatus("current")


class _CsApsArchModeOperational_Type(Integer32):
    """Custom type csApsArchModeOperational based on Integer32"""
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
        *(("anexBOnePlusOne", 3),
          ("onePlusOne", 1),
          ("oneToOne", 2),
          ("straightOnePlusOneNok1k2", 5),
          ("ycableOnePlusOneNok1k2", 4))
    )


_CsApsArchModeOperational_Type.__name__ = "Integer32"
_CsApsArchModeOperational_Object = MibTableColumn
csApsArchModeOperational = _CsApsArchModeOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 12),
    _CsApsArchModeOperational_Type()
)
csApsArchModeOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsArchModeOperational.setStatus("current")


class _CsApsChannelProtocol_Type(Integer32):
    """Custom type csApsChannelProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bellcore", 1),
          ("itu", 2))
    )


_CsApsChannelProtocol_Type.__name__ = "Integer32"
_CsApsChannelProtocol_Object = MibTableColumn
csApsChannelProtocol = _CsApsChannelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 13),
    _CsApsChannelProtocol_Type()
)
csApsChannelProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csApsChannelProtocol.setStatus("current")
_CsApsFailureStatus_Type = CsApsLineFailureStatus
_CsApsFailureStatus_Object = MibTableColumn
csApsFailureStatus = _CsApsFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 14),
    _CsApsFailureStatus_Type()
)
csApsFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsFailureStatus.setStatus("current")
_CsApsSwitchReason_Type = CsApsLineSwitchReason
_CsApsSwitchReason_Object = MibTableColumn
csApsSwitchReason = _CsApsSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 15),
    _CsApsSwitchReason_Type()
)
csApsSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsSwitchReason.setStatus("current")


class _CsApsPrimarySection_Type(Integer32):
    """Custom type csApsPrimarySection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("workingSection1", 1),
          ("workingSection2", 2))
    )


_CsApsPrimarySection_Type.__name__ = "Integer32"
_CsApsPrimarySection_Object = MibTableColumn
csApsPrimarySection = _CsApsPrimarySection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 1, 1, 16),
    _CsApsPrimarySection_Type()
)
csApsPrimarySection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsPrimarySection.setStatus("current")
_CsApsLineFailureCode_Type = CsApsLineFailureCode
_CsApsLineFailureCode_Object = MibScalar
csApsLineFailureCode = _CsApsLineFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 2),
    _CsApsLineFailureCode_Type()
)
csApsLineFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsLineFailureCode.setStatus("current")
_CsApsLineSwitchReason_Type = CsApsLineSwitchReason
_CsApsLineSwitchReason_Object = MibScalar
csApsLineSwitchReason = _CsApsLineSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 2, 3),
    _CsApsLineSwitchReason_Type()
)
csApsLineSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csApsLineSwitchReason.setStatus("current")
_CsSection_ObjectIdentity = ObjectIdentity
csSection = _CsSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3)
)
_CssTotalTable_Object = MibTable
cssTotalTable = _CssTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cssTotalTable.setStatus("current")
_CssTotalEntry_Object = MibTableRow
cssTotalEntry = _CssTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1, 1)
)
cssTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cssTotalEntry.setStatus("current")
_CssTotalESs_Type = Gauge32
_CssTotalESs_Object = MibTableColumn
cssTotalESs = _CssTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1, 1, 1),
    _CssTotalESs_Type()
)
cssTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTotalESs.setStatus("current")
if mibBuilder.loadTexts:
    cssTotalESs.setUnits("errored seconds")
_CssTotalSESs_Type = Gauge32
_CssTotalSESs_Object = MibTableColumn
cssTotalSESs = _CssTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1, 1, 2),
    _CssTotalSESs_Type()
)
cssTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTotalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cssTotalSESs.setUnits("severely errored seconds")
_CssTotalSEFSs_Type = Gauge32
_CssTotalSEFSs_Object = MibTableColumn
cssTotalSEFSs = _CssTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1, 1, 3),
    _CssTotalSEFSs_Type()
)
cssTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTotalSEFSs.setStatus("current")
if mibBuilder.loadTexts:
    cssTotalSEFSs.setUnits("severely errored framing seconds")
_CssTotalCVs_Type = Gauge32
_CssTotalCVs_Object = MibTableColumn
cssTotalCVs = _CssTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 1, 1, 4),
    _CssTotalCVs_Type()
)
cssTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTotalCVs.setStatus("current")
if mibBuilder.loadTexts:
    cssTotalCVs.setUnits("coding violations")
_CssTraceTable_Object = MibTable
cssTraceTable = _CssTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cssTraceTable.setStatus("current")
_CssTraceEntry_Object = MibTableRow
cssTraceEntry = _CssTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2, 1)
)
cssTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cssTraceEntry.setStatus("current")


class _CssTraceToTransmit_Type(OctetString):
    """Custom type cssTraceToTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CssTraceToTransmit_Type.__name__ = "OctetString"
_CssTraceToTransmit_Object = MibTableColumn
cssTraceToTransmit = _CssTraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2, 1, 1),
    _CssTraceToTransmit_Type()
)
cssTraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssTraceToTransmit.setStatus("current")


class _CssTraceToExpect_Type(OctetString):
    """Custom type cssTraceToExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CssTraceToExpect_Type.__name__ = "OctetString"
_CssTraceToExpect_Object = MibTableColumn
cssTraceToExpect = _CssTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2, 1, 2),
    _CssTraceToExpect_Type()
)
cssTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssTraceToExpect.setStatus("current")
_CssTraceFailure_Type = TruthValue
_CssTraceFailure_Object = MibTableColumn
cssTraceFailure = _CssTraceFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2, 1, 3),
    _CssTraceFailure_Type()
)
cssTraceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTraceFailure.setStatus("current")


class _CssTraceReceived_Type(OctetString):
    """Custom type cssTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CssTraceReceived_Type.__name__ = "OctetString"
_CssTraceReceived_Object = MibTableColumn
cssTraceReceived = _CssTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 3, 2, 1, 4),
    _CssTraceReceived_Type()
)
cssTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssTraceReceived.setStatus("current")
_CsLine_ObjectIdentity = ObjectIdentity
csLine = _CsLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4)
)
_CslTotalTable_Object = MibTable
cslTotalTable = _CslTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cslTotalTable.setStatus("current")
_CslTotalEntry_Object = MibTableRow
cslTotalEntry = _CslTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1, 1)
)
cslTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cslTotalEntry.setStatus("current")
_CslTotalESs_Type = Gauge32
_CslTotalESs_Object = MibTableColumn
cslTotalESs = _CslTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1, 1, 1),
    _CslTotalESs_Type()
)
cslTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslTotalESs.setStatus("current")
if mibBuilder.loadTexts:
    cslTotalESs.setUnits("errored seconds")
_CslTotalSESs_Type = Gauge32
_CslTotalSESs_Object = MibTableColumn
cslTotalSESs = _CslTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1, 1, 2),
    _CslTotalSESs_Type()
)
cslTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslTotalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cslTotalSESs.setUnits("severely errored seconds")
_CslTotalCVs_Type = Gauge32
_CslTotalCVs_Object = MibTableColumn
cslTotalCVs = _CslTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1, 1, 3),
    _CslTotalCVs_Type()
)
cslTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslTotalCVs.setStatus("current")
if mibBuilder.loadTexts:
    cslTotalCVs.setUnits("coding violations")
_CslTotalUASs_Type = Gauge32
_CslTotalUASs_Object = MibTableColumn
cslTotalUASs = _CslTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 1, 1, 4),
    _CslTotalUASs_Type()
)
cslTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslTotalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cslTotalUASs.setUnits("unavailable seconds")
_CslFarEndTotalTable_Object = MibTable
cslFarEndTotalTable = _CslFarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cslFarEndTotalTable.setStatus("current")
_CslFarEndTotalEntry_Object = MibTableRow
cslFarEndTotalEntry = _CslFarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2, 1)
)
cslFarEndTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cslFarEndTotalEntry.setStatus("current")
_CslFarEndTotalESs_Type = Gauge32
_CslFarEndTotalESs_Object = MibTableColumn
cslFarEndTotalESs = _CslFarEndTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2, 1, 1),
    _CslFarEndTotalESs_Type()
)
cslFarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslFarEndTotalESs.setStatus("current")
if mibBuilder.loadTexts:
    cslFarEndTotalESs.setUnits("errored seconds")
_CslFarEndTotalSESs_Type = Gauge32
_CslFarEndTotalSESs_Object = MibTableColumn
cslFarEndTotalSESs = _CslFarEndTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2, 1, 2),
    _CslFarEndTotalSESs_Type()
)
cslFarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslFarEndTotalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cslFarEndTotalSESs.setUnits("severely errored seconds")
_CslFarEndTotalCVs_Type = Gauge32
_CslFarEndTotalCVs_Object = MibTableColumn
cslFarEndTotalCVs = _CslFarEndTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2, 1, 3),
    _CslFarEndTotalCVs_Type()
)
cslFarEndTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslFarEndTotalCVs.setStatus("current")
if mibBuilder.loadTexts:
    cslFarEndTotalCVs.setUnits("coding violations")
_CslFarEndTotalUASs_Type = Gauge32
_CslFarEndTotalUASs_Object = MibTableColumn
cslFarEndTotalUASs = _CslFarEndTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 4, 2, 1, 4),
    _CslFarEndTotalUASs_Type()
)
cslFarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslFarEndTotalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cslFarEndTotalUASs.setUnits("unavailable seconds")
_CsPath_ObjectIdentity = ObjectIdentity
csPath = _CsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5)
)
_CspTotalTable_Object = MibTable
cspTotalTable = _CspTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cspTotalTable.setStatus("current")
_CspTotalEntry_Object = MibTableRow
cspTotalEntry = _CspTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1, 1)
)
cspTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cspTotalEntry.setStatus("current")
_CspTotalESs_Type = Gauge32
_CspTotalESs_Object = MibTableColumn
cspTotalESs = _CspTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1, 1, 1),
    _CspTotalESs_Type()
)
cspTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTotalESs.setStatus("current")
if mibBuilder.loadTexts:
    cspTotalESs.setUnits("errored seconds")
_CspTotalSESs_Type = Gauge32
_CspTotalSESs_Object = MibTableColumn
cspTotalSESs = _CspTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1, 1, 2),
    _CspTotalSESs_Type()
)
cspTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTotalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cspTotalSESs.setUnits("severely errored seconds")
_CspTotalCVs_Type = Gauge32
_CspTotalCVs_Object = MibTableColumn
cspTotalCVs = _CspTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1, 1, 3),
    _CspTotalCVs_Type()
)
cspTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTotalCVs.setStatus("current")
if mibBuilder.loadTexts:
    cspTotalCVs.setUnits("coding violations")
_CspTotalUASs_Type = Gauge32
_CspTotalUASs_Object = MibTableColumn
cspTotalUASs = _CspTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 1, 1, 4),
    _CspTotalUASs_Type()
)
cspTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTotalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cspTotalUASs.setUnits("unavailable seconds")
_CspFarEndTotalTable_Object = MibTable
cspFarEndTotalTable = _CspFarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cspFarEndTotalTable.setStatus("current")
_CspFarEndTotalEntry_Object = MibTableRow
cspFarEndTotalEntry = _CspFarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2, 1)
)
cspFarEndTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cspFarEndTotalEntry.setStatus("current")
_CspFarEndTotalESs_Type = Gauge32
_CspFarEndTotalESs_Object = MibTableColumn
cspFarEndTotalESs = _CspFarEndTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2, 1, 1),
    _CspFarEndTotalESs_Type()
)
cspFarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspFarEndTotalESs.setStatus("current")
if mibBuilder.loadTexts:
    cspFarEndTotalESs.setUnits("errored seconds")
_CspFarEndTotalSESs_Type = Gauge32
_CspFarEndTotalSESs_Object = MibTableColumn
cspFarEndTotalSESs = _CspFarEndTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2, 1, 2),
    _CspFarEndTotalSESs_Type()
)
cspFarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspFarEndTotalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cspFarEndTotalSESs.setUnits("severely errored seconds")
_CspFarEndTotalCVs_Type = Gauge32
_CspFarEndTotalCVs_Object = MibTableColumn
cspFarEndTotalCVs = _CspFarEndTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2, 1, 3),
    _CspFarEndTotalCVs_Type()
)
cspFarEndTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspFarEndTotalCVs.setStatus("current")
if mibBuilder.loadTexts:
    cspFarEndTotalCVs.setUnits("coding violations")
_CspFarEndTotalUASs_Type = Gauge32
_CspFarEndTotalUASs_Object = MibTableColumn
cspFarEndTotalUASs = _CspFarEndTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 2, 1, 4),
    _CspFarEndTotalUASs_Type()
)
cspFarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspFarEndTotalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cspFarEndTotalUASs.setUnits("unavailable seconds")
_CspTraceTable_Object = MibTable
cspTraceTable = _CspTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cspTraceTable.setStatus("current")
_CspTraceEntry_Object = MibTableRow
cspTraceEntry = _CspTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3, 1)
)
cspTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cspTraceEntry.setStatus("current")


class _CspTraceToTransmit_Type(OctetString):
    """Custom type cspTraceToTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CspTraceToTransmit_Type.__name__ = "OctetString"
_CspTraceToTransmit_Object = MibTableColumn
cspTraceToTransmit = _CspTraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3, 1, 1),
    _CspTraceToTransmit_Type()
)
cspTraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspTraceToTransmit.setStatus("current")


class _CspTraceToExpect_Type(OctetString):
    """Custom type cspTraceToExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CspTraceToExpect_Type.__name__ = "OctetString"
_CspTraceToExpect_Object = MibTableColumn
cspTraceToExpect = _CspTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3, 1, 2),
    _CspTraceToExpect_Type()
)
cspTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspTraceToExpect.setStatus("current")
_CspTraceFailure_Type = TruthValue
_CspTraceFailure_Object = MibTableColumn
cspTraceFailure = _CspTraceFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3, 1, 3),
    _CspTraceFailure_Type()
)
cspTraceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTraceFailure.setStatus("current")


class _CspTraceReceived_Type(OctetString):
    """Custom type cspTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CspTraceReceived_Type.__name__ = "OctetString"
_CspTraceReceived_Object = MibTableColumn
cspTraceReceived = _CspTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 5, 3, 1, 4),
    _CspTraceReceived_Type()
)
cspTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTraceReceived.setStatus("current")
_CsStats_ObjectIdentity = ObjectIdentity
csStats = _CsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6)
)
_CsStatsTable_Object = MibTable
csStatsTable = _CsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1)
)
if mibBuilder.loadTexts:
    csStatsTable.setStatus("current")
_CsStatsEntry_Object = MibTableRow
csStatsEntry = _CsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1)
)
csStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csStatsEntry.setStatus("current")
_CssLOSs_Type = Counter32
_CssLOSs_Object = MibTableColumn
cssLOSs = _CssLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 1),
    _CssLOSs_Type()
)
cssLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cssLOSs.setUnits("loss of signals")
_CssLOFs_Type = Counter32
_CssLOFs_Object = MibTableColumn
cssLOFs = _CssLOFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 2),
    _CssLOFs_Type()
)
cssLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssLOFs.setStatus("current")
if mibBuilder.loadTexts:
    cssLOFs.setUnits("loss of frames")
_CslAISs_Type = Counter32
_CslAISs_Object = MibTableColumn
cslAISs = _CslAISs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 3),
    _CslAISs_Type()
)
cslAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslAISs.setStatus("current")
if mibBuilder.loadTexts:
    cslAISs.setUnits("alarm indication signals")
_CslRFIs_Type = Counter32
_CslRFIs_Object = MibTableColumn
cslRFIs = _CslRFIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 4),
    _CslRFIs_Type()
)
cslRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslRFIs.setStatus("current")
if mibBuilder.loadTexts:
    cslRFIs.setUnits("remote failure indications")
_CspAISs_Type = Counter32
_CspAISs_Object = MibTableColumn
cspAISs = _CspAISs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 5),
    _CspAISs_Type()
)
cspAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspAISs.setStatus("current")
if mibBuilder.loadTexts:
    cspAISs.setUnits("alarm indication signals")
_CspRFIs_Type = Counter32
_CspRFIs_Object = MibTableColumn
cspRFIs = _CspRFIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 6, 1, 1, 6),
    _CspRFIs_Type()
)
cspRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspRFIs.setStatus("current")
if mibBuilder.loadTexts:
    cspRFIs.setUnits("remote failure indications")
_CspConfig_ObjectIdentity = ObjectIdentity
cspConfig = _CspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7)
)
_CspConfigTable_Object = MibTable
cspConfigTable = _CspConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cspConfigTable.setStatus("current")
_CspConfigEntry_Object = MibTableRow
cspConfigEntry = _CspConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cspConfigEntry.setStatus("current")


class _CspSonetPathPayload_Type(Integer32):
    """Custom type cspSonetPathPayload based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmCell", 6),
          ("ds3", 3),
          ("e3", 8),
          ("hdlcFr", 7),
          ("unequipped", 1),
          ("unspecified", 2),
          ("vt15vc11", 4),
          ("vt2vc12", 5),
          ("vtStructured", 9))
    )


_CspSonetPathPayload_Type.__name__ = "Integer32"
_CspSonetPathPayload_Object = MibTableColumn
cspSonetPathPayload = _CspSonetPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1, 1, 1),
    _CspSonetPathPayload_Type()
)
cspSonetPathPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspSonetPathPayload.setStatus("current")


class _CspTributaryMappingType_Type(Integer32):
    """Custom type cspTributaryMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("byteSynchronous", 2))
    )


_CspTributaryMappingType_Type.__name__ = "Integer32"
_CspTributaryMappingType_Object = MibTableColumn
cspTributaryMappingType = _CspTributaryMappingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1, 1, 2),
    _CspTributaryMappingType_Type()
)
cspTributaryMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspTributaryMappingType.setStatus("current")


class _CspSignallingTransportMode_Type(Integer32):
    """Custom type cspSignallingTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearMode", 3),
          ("notApplicable", 1),
          ("signallingTransferMode", 2))
    )


_CspSignallingTransportMode_Type.__name__ = "Integer32"
_CspSignallingTransportMode_Object = MibTableColumn
cspSignallingTransportMode = _CspSignallingTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1, 1, 3),
    _CspSignallingTransportMode_Type()
)
cspSignallingTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspSignallingTransportMode.setStatus("current")


class _CspTributaryGroupingType_Type(Integer32):
    """Custom type cspTributaryGroupingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("au3Grouping", 2),
          ("au4Grouping", 3),
          ("notApplicable", 1))
    )


_CspTributaryGroupingType_Type.__name__ = "Integer32"
_CspTributaryGroupingType_Object = MibTableColumn
cspTributaryGroupingType = _CspTributaryGroupingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 7, 1, 1, 4),
    _CspTributaryGroupingType_Type()
)
cspTributaryGroupingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspTributaryGroupingType.setStatus("current")
_CsNotifications_ObjectIdentity = ObjectIdentity
csNotifications = _CsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 8)
)


class _CsNotificationsEnabled_Type(TruthValue):
    """Custom type csNotificationsEnabled based on TruthValue"""


_CsNotificationsEnabled_Object = MibScalar
csNotificationsEnabled = _CsNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 8, 1),
    _CsNotificationsEnabled_Type()
)
csNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csNotificationsEnabled.setStatus("current")
_CsAu4Tug3Config_ObjectIdentity = ObjectIdentity
csAu4Tug3Config = _CsAu4Tug3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 9)
)
_CsAu4Tug3ConfigTable_Object = MibTable
csAu4Tug3ConfigTable = _CsAu4Tug3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 9, 1)
)
if mibBuilder.loadTexts:
    csAu4Tug3ConfigTable.setStatus("current")
_CsAu4Tug3ConfigEntry_Object = MibTableRow
csAu4Tug3ConfigEntry = _CsAu4Tug3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 9, 1, 1)
)
csAu4Tug3ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SONET-MIB", "csAu4Tug3"),
)
if mibBuilder.loadTexts:
    csAu4Tug3ConfigEntry.setStatus("current")


class _CsAu4Tug3_Type(Integer32):
    """Custom type csAu4Tug3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CsAu4Tug3_Type.__name__ = "Integer32"
_CsAu4Tug3_Object = MibTableColumn
csAu4Tug3 = _CsAu4Tug3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 9, 1, 1, 1),
    _CsAu4Tug3_Type()
)
csAu4Tug3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csAu4Tug3.setStatus("current")


class _CsAu4Tug3Payload_Type(Integer32):
    """Custom type csAu4Tug3Payload based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("tu3ds3", 4),
          ("tu3e3", 5),
          ("vc11", 2),
          ("vc12", 3))
    )


_CsAu4Tug3Payload_Type.__name__ = "Integer32"
_CsAu4Tug3Payload_Object = MibTableColumn
csAu4Tug3Payload = _CsAu4Tug3Payload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 1, 9, 1, 1, 2),
    _CsAu4Tug3Payload_Type()
)
csAu4Tug3Payload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csAu4Tug3Payload.setStatus("current")
_CiscoSonetMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSonetMIBConformance = _CiscoSonetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3)
)
_CiscoSonetMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSonetMIBCompliances = _CiscoSonetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 1)
)
_CiscoSonetMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSonetMIBGroups = _CiscoSonetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2)
)
csConfigEntry.registerAugmentions(
    ("CISCO-SONET-MIB",
     "csVTConfigEntry")
)
csVTConfigEntry.setIndexNames(*csConfigEntry.getIndexNames())
sonetPathCurrentEntry.registerAugmentions(
    ("CISCO-SONET-MIB",
     "cspConfigEntry")
)
cspConfigEntry.setIndexNames(*sonetPathCurrentEntry.getIndexNames())

# Managed Objects groups

ciscoSonetConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 1)
)
ciscoSonetConfMIBGroup.setObjects(
      *(("CISCO-SONET-MIB", "csConfigLoopbackType"),
        ("CISCO-SONET-MIB", "csConfigXmtClockSource"),
        ("CISCO-SONET-MIB", "csConfigFrameScramble"),
        ("CISCO-SONET-MIB", "csConfigType"))
)
if mibBuilder.loadTexts:
    ciscoSonetConfMIBGroup.setStatus("deprecated")

ciscoSonetStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 2)
)
ciscoSonetStatsMIBGroup.setObjects(
      *(("CISCO-SONET-MIB", "cssTotalESs"),
        ("CISCO-SONET-MIB", "cssTotalSESs"),
        ("CISCO-SONET-MIB", "cssTotalSEFSs"),
        ("CISCO-SONET-MIB", "cssTotalCVs"),
        ("CISCO-SONET-MIB", "cssLOSs"),
        ("CISCO-SONET-MIB", "cssLOFs"),
        ("CISCO-SONET-MIB", "cslAISs"),
        ("CISCO-SONET-MIB", "cslRFIs"),
        ("CISCO-SONET-MIB", "cspAISs"),
        ("CISCO-SONET-MIB", "cspRFIs"),
        ("CISCO-SONET-MIB", "cslTotalESs"),
        ("CISCO-SONET-MIB", "cslTotalSESs"),
        ("CISCO-SONET-MIB", "cslTotalCVs"),
        ("CISCO-SONET-MIB", "cslTotalUASs"),
        ("CISCO-SONET-MIB", "cslFarEndTotalESs"),
        ("CISCO-SONET-MIB", "cslFarEndTotalSESs"),
        ("CISCO-SONET-MIB", "cslFarEndTotalCVs"),
        ("CISCO-SONET-MIB", "cslFarEndTotalUASs"),
        ("CISCO-SONET-MIB", "cspTotalESs"),
        ("CISCO-SONET-MIB", "cspTotalSESs"),
        ("CISCO-SONET-MIB", "cspTotalCVs"),
        ("CISCO-SONET-MIB", "cspTotalUASs"),
        ("CISCO-SONET-MIB", "cspFarEndTotalESs"),
        ("CISCO-SONET-MIB", "cspFarEndTotalSESs"),
        ("CISCO-SONET-MIB", "cspFarEndTotalCVs"),
        ("CISCO-SONET-MIB", "cspFarEndTotalUASs"))
)
if mibBuilder.loadTexts:
    ciscoSonetStatsMIBGroup.setStatus("current")

ciscoSonetTraceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 3)
)
ciscoSonetTraceMIBGroup.setObjects(
      *(("CISCO-SONET-MIB", "cssTraceToTransmit"),
        ("CISCO-SONET-MIB", "cssTraceToExpect"),
        ("CISCO-SONET-MIB", "cssTraceFailure"),
        ("CISCO-SONET-MIB", "cssTraceReceived"),
        ("CISCO-SONET-MIB", "cspTraceToTransmit"),
        ("CISCO-SONET-MIB", "cspTraceToExpect"),
        ("CISCO-SONET-MIB", "cspTraceFailure"),
        ("CISCO-SONET-MIB", "cspTraceReceived"))
)
if mibBuilder.loadTexts:
    ciscoSonetTraceMIBGroup.setStatus("current")

ciscoSonetApsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 4)
)
ciscoSonetApsMIBGroup.setObjects(
      *(("CISCO-SONET-MIB", "csApsProtectionIndex"),
        ("CISCO-SONET-MIB", "csApsEnable"),
        ("CISCO-SONET-MIB", "csApsArchMode"),
        ("CISCO-SONET-MIB", "csApsActiveLine"),
        ("CISCO-SONET-MIB", "csApsSigFaultBER"),
        ("CISCO-SONET-MIB", "csApsSigDegradeBER"),
        ("CISCO-SONET-MIB", "csApsWaitToRestore"),
        ("CISCO-SONET-MIB", "csApsDirection"),
        ("CISCO-SONET-MIB", "csApsRevertive"),
        ("CISCO-SONET-MIB", "csApsLineFailureCode"),
        ("CISCO-SONET-MIB", "csApsLineSwitchReason"),
        ("CISCO-SONET-MIB", "csApsDirectionOperational"),
        ("CISCO-SONET-MIB", "csApsArchModeOperational"),
        ("CISCO-SONET-MIB", "csApsChannelProtocol"))
)
if mibBuilder.loadTexts:
    ciscoSonetApsMIBGroup.setStatus("deprecated")

ciscoSonetApsMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 5)
)
ciscoSonetApsMIBGroup1.setObjects(
      *(("CISCO-SONET-MIB", "csApsProtectionIndex"),
        ("CISCO-SONET-MIB", "csApsEnable"),
        ("CISCO-SONET-MIB", "csApsArchMode"),
        ("CISCO-SONET-MIB", "csApsActiveLine"),
        ("CISCO-SONET-MIB", "csApsSigFaultBER"),
        ("CISCO-SONET-MIB", "csApsSigDegradeBER"),
        ("CISCO-SONET-MIB", "csApsWaitToRestore"),
        ("CISCO-SONET-MIB", "csApsDirection"),
        ("CISCO-SONET-MIB", "csApsRevertive"),
        ("CISCO-SONET-MIB", "csApsLineFailureCode"),
        ("CISCO-SONET-MIB", "csApsLineSwitchReason"),
        ("CISCO-SONET-MIB", "csApsDirectionOperational"),
        ("CISCO-SONET-MIB", "csApsArchModeOperational"),
        ("CISCO-SONET-MIB", "csApsChannelProtocol"),
        ("CISCO-SONET-MIB", "csApsFailureStatus"),
        ("CISCO-SONET-MIB", "csApsSwitchReason"),
        ("CISCO-SONET-MIB", "csApsPrimarySection"))
)
if mibBuilder.loadTexts:
    ciscoSonetApsMIBGroup1.setStatus("current")

ciscoSonetConfMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 6)
)
ciscoSonetConfMIBGroup1.setObjects(
      *(("CISCO-SONET-MIB", "csConfigLoopbackType"),
        ("CISCO-SONET-MIB", "csConfigXmtClockSource"),
        ("CISCO-SONET-MIB", "csConfigFrameScramble"),
        ("CISCO-SONET-MIB", "csConfigType"),
        ("CISCO-SONET-MIB", "csConfigRDIPType"),
        ("CISCO-SONET-MIB", "csConfigRDIVType"))
)
if mibBuilder.loadTexts:
    ciscoSonetConfMIBGroup1.setStatus("current")

ciscoSonetVTConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 7)
)
ciscoSonetVTConfMIBGroup.setObjects(
      *(("CISCO-SONET-MIB", "csTributaryType"),
        ("CISCO-SONET-MIB", "csTributaryMappingType"),
        ("CISCO-SONET-MIB", "csTributaryFramingType"),
        ("CISCO-SONET-MIB", "csSignallingTransportMode"),
        ("CISCO-SONET-MIB", "csTributaryGroupingType"))
)
if mibBuilder.loadTexts:
    ciscoSonetVTConfMIBGroup.setStatus("current")

ciscoSonetPathConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 8)
)
ciscoSonetPathConfMIBGroup.setObjects(
    ("CISCO-SONET-MIB", "cspSonetPathPayload")
)
if mibBuilder.loadTexts:
    ciscoSonetPathConfMIBGroup.setStatus("current")

ciscoSonetNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 9)
)
ciscoSonetNotifEnableGroup.setObjects(
    ("CISCO-SONET-MIB", "csNotificationsEnabled")
)
if mibBuilder.loadTexts:
    ciscoSonetNotifEnableGroup.setStatus("current")

ciscoSonetPathConfMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 14)
)
ciscoSonetPathConfMIBGroup1.setObjects(
      *(("CISCO-SONET-MIB", "cspTributaryMappingType"),
        ("CISCO-SONET-MIB", "cspSignallingTransportMode"),
        ("CISCO-SONET-MIB", "cspTributaryGroupingType"))
)
if mibBuilder.loadTexts:
    ciscoSonetPathConfMIBGroup1.setStatus("current")

ciscoSonetAu4Tug3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 15)
)
ciscoSonetAu4Tug3Group.setObjects(
    ("CISCO-SONET-MIB", "csAu4Tug3Payload")
)
if mibBuilder.loadTexts:
    ciscoSonetAu4Tug3Group.setStatus("current")


# Notification objects

ciscoSonetSectionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 0, 1)
)
ciscoSonetSectionStatusChange.setObjects(
      *(("SONET-MIB", "sonetSectionCurrentStatus"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ciscoSonetSectionStatusChange.setStatus(
        "current"
    )

ciscoSonetLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 0, 2)
)
ciscoSonetLineStatusChange.setObjects(
      *(("SONET-MIB", "sonetLineCurrentStatus"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ciscoSonetLineStatusChange.setStatus(
        "current"
    )

ciscoSonetPathStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 0, 3)
)
ciscoSonetPathStatusChange.setObjects(
      *(("SONET-MIB", "sonetPathCurrentStatus"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ciscoSonetPathStatusChange.setStatus(
        "current"
    )

ciscoSonetVTStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 0, 4)
)
ciscoSonetVTStatusChange.setObjects(
      *(("SONET-MIB", "sonetVTCurrentStatus"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    ciscoSonetVTStatusChange.setStatus(
        "current"
    )


# Notifications groups

ciscoSonetSectionNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 10)
)
ciscoSonetSectionNotifGroup.setObjects(
    ("CISCO-SONET-MIB", "ciscoSonetSectionStatusChange")
)
if mibBuilder.loadTexts:
    ciscoSonetSectionNotifGroup.setStatus(
        "current"
    )

ciscoSonetLineNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 11)
)
ciscoSonetLineNotifGroup.setObjects(
    ("CISCO-SONET-MIB", "ciscoSonetLineStatusChange")
)
if mibBuilder.loadTexts:
    ciscoSonetLineNotifGroup.setStatus(
        "current"
    )

ciscoSonetPathNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 12)
)
ciscoSonetPathNotifGroup.setObjects(
    ("CISCO-SONET-MIB", "ciscoSonetPathStatusChange")
)
if mibBuilder.loadTexts:
    ciscoSonetPathNotifGroup.setStatus(
        "current"
    )

ciscoSonetVTNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 2, 13)
)
ciscoSonetVTNotifGroup.setObjects(
    ("CISCO-SONET-MIB", "ciscoSonetVTStatusChange")
)
if mibBuilder.loadTexts:
    ciscoSonetVTNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSonetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSonetMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSonetMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSonetMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoSonetMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSonetMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoSonetMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 126, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSonetMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SONET-MIB",
    **{"CsApsLineFailureCode": CsApsLineFailureCode,
       "CsApsLineFailureStatus": CsApsLineFailureStatus,
       "CsApsLineSwitchReason": CsApsLineSwitchReason,
       "ciscoSonetMIB": ciscoSonetMIB,
       "ciscoSonetMIBNotifs": ciscoSonetMIBNotifs,
       "ciscoSonetSectionStatusChange": ciscoSonetSectionStatusChange,
       "ciscoSonetLineStatusChange": ciscoSonetLineStatusChange,
       "ciscoSonetPathStatusChange": ciscoSonetPathStatusChange,
       "ciscoSonetVTStatusChange": ciscoSonetVTStatusChange,
       "ciscoSonetMIBObjects": ciscoSonetMIBObjects,
       "csConfig": csConfig,
       "csConfigTable": csConfigTable,
       "csConfigEntry": csConfigEntry,
       "csConfigLoopbackType": csConfigLoopbackType,
       "csConfigXmtClockSource": csConfigXmtClockSource,
       "csConfigFrameScramble": csConfigFrameScramble,
       "csConfigType": csConfigType,
       "csConfigRDIVType": csConfigRDIVType,
       "csConfigRDIPType": csConfigRDIPType,
       "csVTConfigTable": csVTConfigTable,
       "csVTConfigEntry": csVTConfigEntry,
       "csTributaryType": csTributaryType,
       "csTributaryMappingType": csTributaryMappingType,
       "csTributaryFramingType": csTributaryFramingType,
       "csSignallingTransportMode": csSignallingTransportMode,
       "csTributaryGroupingType": csTributaryGroupingType,
       "csApsConfig": csApsConfig,
       "csApsConfigTable": csApsConfigTable,
       "csApsConfigEntry": csApsConfigEntry,
       "csApsWorkingIndex": csApsWorkingIndex,
       "csApsProtectionIndex": csApsProtectionIndex,
       "csApsEnable": csApsEnable,
       "csApsArchMode": csApsArchMode,
       "csApsActiveLine": csApsActiveLine,
       "csApsSigFaultBER": csApsSigFaultBER,
       "csApsSigDegradeBER": csApsSigDegradeBER,
       "csApsWaitToRestore": csApsWaitToRestore,
       "csApsDirection": csApsDirection,
       "csApsRevertive": csApsRevertive,
       "csApsDirectionOperational": csApsDirectionOperational,
       "csApsArchModeOperational": csApsArchModeOperational,
       "csApsChannelProtocol": csApsChannelProtocol,
       "csApsFailureStatus": csApsFailureStatus,
       "csApsSwitchReason": csApsSwitchReason,
       "csApsPrimarySection": csApsPrimarySection,
       "csApsLineFailureCode": csApsLineFailureCode,
       "csApsLineSwitchReason": csApsLineSwitchReason,
       "csSection": csSection,
       "cssTotalTable": cssTotalTable,
       "cssTotalEntry": cssTotalEntry,
       "cssTotalESs": cssTotalESs,
       "cssTotalSESs": cssTotalSESs,
       "cssTotalSEFSs": cssTotalSEFSs,
       "cssTotalCVs": cssTotalCVs,
       "cssTraceTable": cssTraceTable,
       "cssTraceEntry": cssTraceEntry,
       "cssTraceToTransmit": cssTraceToTransmit,
       "cssTraceToExpect": cssTraceToExpect,
       "cssTraceFailure": cssTraceFailure,
       "cssTraceReceived": cssTraceReceived,
       "csLine": csLine,
       "cslTotalTable": cslTotalTable,
       "cslTotalEntry": cslTotalEntry,
       "cslTotalESs": cslTotalESs,
       "cslTotalSESs": cslTotalSESs,
       "cslTotalCVs": cslTotalCVs,
       "cslTotalUASs": cslTotalUASs,
       "cslFarEndTotalTable": cslFarEndTotalTable,
       "cslFarEndTotalEntry": cslFarEndTotalEntry,
       "cslFarEndTotalESs": cslFarEndTotalESs,
       "cslFarEndTotalSESs": cslFarEndTotalSESs,
       "cslFarEndTotalCVs": cslFarEndTotalCVs,
       "cslFarEndTotalUASs": cslFarEndTotalUASs,
       "csPath": csPath,
       "cspTotalTable": cspTotalTable,
       "cspTotalEntry": cspTotalEntry,
       "cspTotalESs": cspTotalESs,
       "cspTotalSESs": cspTotalSESs,
       "cspTotalCVs": cspTotalCVs,
       "cspTotalUASs": cspTotalUASs,
       "cspFarEndTotalTable": cspFarEndTotalTable,
       "cspFarEndTotalEntry": cspFarEndTotalEntry,
       "cspFarEndTotalESs": cspFarEndTotalESs,
       "cspFarEndTotalSESs": cspFarEndTotalSESs,
       "cspFarEndTotalCVs": cspFarEndTotalCVs,
       "cspFarEndTotalUASs": cspFarEndTotalUASs,
       "cspTraceTable": cspTraceTable,
       "cspTraceEntry": cspTraceEntry,
       "cspTraceToTransmit": cspTraceToTransmit,
       "cspTraceToExpect": cspTraceToExpect,
       "cspTraceFailure": cspTraceFailure,
       "cspTraceReceived": cspTraceReceived,
       "csStats": csStats,
       "csStatsTable": csStatsTable,
       "csStatsEntry": csStatsEntry,
       "cssLOSs": cssLOSs,
       "cssLOFs": cssLOFs,
       "cslAISs": cslAISs,
       "cslRFIs": cslRFIs,
       "cspAISs": cspAISs,
       "cspRFIs": cspRFIs,
       "cspConfig": cspConfig,
       "cspConfigTable": cspConfigTable,
       "cspConfigEntry": cspConfigEntry,
       "cspSonetPathPayload": cspSonetPathPayload,
       "cspTributaryMappingType": cspTributaryMappingType,
       "cspSignallingTransportMode": cspSignallingTransportMode,
       "cspTributaryGroupingType": cspTributaryGroupingType,
       "csNotifications": csNotifications,
       "csNotificationsEnabled": csNotificationsEnabled,
       "csAu4Tug3Config": csAu4Tug3Config,
       "csAu4Tug3ConfigTable": csAu4Tug3ConfigTable,
       "csAu4Tug3ConfigEntry": csAu4Tug3ConfigEntry,
       "csAu4Tug3": csAu4Tug3,
       "csAu4Tug3Payload": csAu4Tug3Payload,
       "ciscoSonetMIBConformance": ciscoSonetMIBConformance,
       "ciscoSonetMIBCompliances": ciscoSonetMIBCompliances,
       "ciscoSonetMIBCompliance": ciscoSonetMIBCompliance,
       "ciscoSonetMIBCompliance1": ciscoSonetMIBCompliance1,
       "ciscoSonetMIBCompliance2": ciscoSonetMIBCompliance2,
       "ciscoSonetMIBCompliance3": ciscoSonetMIBCompliance3,
       "ciscoSonetMIBGroups": ciscoSonetMIBGroups,
       "ciscoSonetConfMIBGroup": ciscoSonetConfMIBGroup,
       "ciscoSonetStatsMIBGroup": ciscoSonetStatsMIBGroup,
       "ciscoSonetTraceMIBGroup": ciscoSonetTraceMIBGroup,
       "ciscoSonetApsMIBGroup": ciscoSonetApsMIBGroup,
       "ciscoSonetApsMIBGroup1": ciscoSonetApsMIBGroup1,
       "ciscoSonetConfMIBGroup1": ciscoSonetConfMIBGroup1,
       "ciscoSonetVTConfMIBGroup": ciscoSonetVTConfMIBGroup,
       "ciscoSonetPathConfMIBGroup": ciscoSonetPathConfMIBGroup,
       "ciscoSonetNotifEnableGroup": ciscoSonetNotifEnableGroup,
       "ciscoSonetSectionNotifGroup": ciscoSonetSectionNotifGroup,
       "ciscoSonetLineNotifGroup": ciscoSonetLineNotifGroup,
       "ciscoSonetPathNotifGroup": ciscoSonetPathNotifGroup,
       "ciscoSonetVTNotifGroup": ciscoSonetVTNotifGroup,
       "ciscoSonetPathConfMIBGroup1": ciscoSonetPathConfMIBGroup1,
       "ciscoSonetAu4Tug3Group": ciscoSonetAu4Tug3Group}
)
