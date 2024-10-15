# SNMP MIB module (SALIX-HNE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-HNE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:26 2024
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

(atmfM4CellProtoHistIndex,
 atmfM4EquipHolderEntry,
 atmfM4PlugInUnitEntry,
 atmfM4TcAdaptorEntry) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4CellProtoHistIndex",
    "atmfM4EquipHolderEntry",
    "atmfM4PlugInUnitEntry",
    "atmfM4TcAdaptorEntry")

(AtmTrafficDescrParamIndex,
 atmInterfaceConfEntry,
 atmVclEntry,
 atmVclVci,
 atmVclVpi,
 atmVplEntry,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex",
    "atmInterfaceConfEntry",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi",
    "atmVplEntry",
    "atmVplVpi")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(hrSWInstalledEntry,
 hrSWInstalledIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSWInstalledEntry",
    "hrSWInstalledIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(hybridSwitch,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "hybridSwitch")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(sonetLineCurrentEntry,
 sonetLineIntervalEntry,
 sonetMediumEntry,
 sonetPathCurrentEntry,
 sonetPathIntervalEntry,
 sonetSectionCurrentEntry,
 sonetSectionIntervalEntry) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetLineCurrentEntry",
    "sonetLineIntervalEntry",
    "sonetMediumEntry",
    "sonetPathCurrentEntry",
    "sonetPathIntervalEntry",
    "sonetSectionCurrentEntry",
    "sonetSectionIntervalEntry")


# MODULE-IDENTITY

hneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HnePlugInUnitType(Integer32, TextualConvention):
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
        *(("dpu", 2),
          ("fan", 7),
          ("hardDrive", 8),
          ("hsf", 5),
          ("liu", 4),
          ("mpu", 1),
          ("powerSupply", 6),
          ("smu", 3),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_HneMIBObjects_ObjectIdentity = ObjectIdentity
hneMIBObjects = _HneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1)
)
_HneSystem_ObjectIdentity = ObjectIdentity
hneSystem = _HneSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1)
)
_HneSystemHost_ObjectIdentity = ObjectIdentity
hneSystemHost = _HneSystemHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 1)
)
_HneSystemSync_ObjectIdentity = ObjectIdentity
hneSystemSync = _HneSystemSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2)
)


class _HneSysSyncTimingMode_Type(Integer32):
    """Custom type hneSysSyncTimingMode based on Integer32"""
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
        *(("external", 3),
          ("internal", 1),
          ("line", 2))
    )


_HneSysSyncTimingMode_Type.__name__ = "Integer32"
_HneSysSyncTimingMode_Object = MibScalar
hneSysSyncTimingMode = _HneSysSyncTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 1),
    _HneSysSyncTimingMode_Type()
)
hneSysSyncTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncTimingMode.setStatus("current")
_HneSysSyncPrimaryRefLine_Type = InterfaceIndex
_HneSysSyncPrimaryRefLine_Object = MibScalar
hneSysSyncPrimaryRefLine = _HneSysSyncPrimaryRefLine_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 2),
    _HneSysSyncPrimaryRefLine_Type()
)
hneSysSyncPrimaryRefLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncPrimaryRefLine.setStatus("current")
_HneSysSyncSecondaryRefLine_Type = InterfaceIndex
_HneSysSyncSecondaryRefLine_Object = MibScalar
hneSysSyncSecondaryRefLine = _HneSysSyncSecondaryRefLine_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 3),
    _HneSysSyncSecondaryRefLine_Type()
)
hneSysSyncSecondaryRefLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncSecondaryRefLine.setStatus("current")


class _HneSysSyncRevertiveSwitch_Type(TruthValue):
    """Custom type hneSysSyncRevertiveSwitch based on TruthValue"""


_HneSysSyncRevertiveSwitch_Object = MibScalar
hneSysSyncRevertiveSwitch = _HneSysSyncRevertiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 4),
    _HneSysSyncRevertiveSwitch_Type()
)
hneSysSyncRevertiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncRevertiveSwitch.setStatus("current")


class _HneSysSyncClockMode_Type(Integer32):
    """Custom type hneSysSyncClockMode based on Integer32"""
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
        *(("fastStart", 4),
          ("freeRun", 1),
          ("holdover", 3),
          ("normal", 2))
    )


_HneSysSyncClockMode_Type.__name__ = "Integer32"
_HneSysSyncClockMode_Object = MibScalar
hneSysSyncClockMode = _HneSysSyncClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 5),
    _HneSysSyncClockMode_Type()
)
hneSysSyncClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncClockMode.setStatus("current")


class _HneSysSyncConfiguredActiveRef_Type(Integer32):
    """Custom type hneSysSyncConfiguredActiveRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HneSysSyncConfiguredActiveRef_Type.__name__ = "Integer32"
_HneSysSyncConfiguredActiveRef_Object = MibScalar
hneSysSyncConfiguredActiveRef = _HneSysSyncConfiguredActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 6),
    _HneSysSyncConfiguredActiveRef_Type()
)
hneSysSyncConfiguredActiveRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncConfiguredActiveRef.setStatus("current")


class _HneSysSyncAutoRefSwitch_Type(TruthValue):
    """Custom type hneSysSyncAutoRefSwitch based on TruthValue"""


_HneSysSyncAutoRefSwitch_Object = MibScalar
hneSysSyncAutoRefSwitch = _HneSysSyncAutoRefSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 7),
    _HneSysSyncAutoRefSwitch_Type()
)
hneSysSyncAutoRefSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncAutoRefSwitch.setStatus("current")


class _HneSysSyncFreeRunAlarm_Type(TruthValue):
    """Custom type hneSysSyncFreeRunAlarm based on TruthValue"""


_HneSysSyncFreeRunAlarm_Object = MibScalar
hneSysSyncFreeRunAlarm = _HneSysSyncFreeRunAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 8),
    _HneSysSyncFreeRunAlarm_Type()
)
hneSysSyncFreeRunAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncFreeRunAlarm.setStatus("current")
_HneSysSyncWorking_Type = PhysicalIndex
_HneSysSyncWorking_Object = MibScalar
hneSysSyncWorking = _HneSysSyncWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 9),
    _HneSysSyncWorking_Type()
)
hneSysSyncWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysSyncWorking.setStatus("current")
_HneSysSyncProtect_Type = PhysicalIndex
_HneSysSyncProtect_Object = MibScalar
hneSysSyncProtect = _HneSysSyncProtect_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 10),
    _HneSysSyncProtect_Type()
)
hneSysSyncProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncProtect.setStatus("current")


class _HneSysSyncPrimaryRefLineState_Type(Integer32):
    """Custom type hneSysSyncPrimaryRefLineState based on Integer32"""
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
        *(("frequencyOffsetError", 3),
          ("lossOfSignalError", 2),
          ("unknown", 0),
          ("valid", 1))
    )


_HneSysSyncPrimaryRefLineState_Type.__name__ = "Integer32"
_HneSysSyncPrimaryRefLineState_Object = MibScalar
hneSysSyncPrimaryRefLineState = _HneSysSyncPrimaryRefLineState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 11),
    _HneSysSyncPrimaryRefLineState_Type()
)
hneSysSyncPrimaryRefLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncPrimaryRefLineState.setStatus("current")


class _HneSysSyncSecondaryRefLineState_Type(Integer32):
    """Custom type hneSysSyncSecondaryRefLineState based on Integer32"""
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
        *(("frequencyOffsetError", 3),
          ("lossOfSignalError", 2),
          ("unknown", 0),
          ("valid", 1))
    )


_HneSysSyncSecondaryRefLineState_Type.__name__ = "Integer32"
_HneSysSyncSecondaryRefLineState_Object = MibScalar
hneSysSyncSecondaryRefLineState = _HneSysSyncSecondaryRefLineState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 12),
    _HneSysSyncSecondaryRefLineState_Type()
)
hneSysSyncSecondaryRefLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncSecondaryRefLineState.setStatus("current")


class _HneSysSyncCurrentActiveRef_Type(Integer32):
    """Custom type hneSysSyncCurrentActiveRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HneSysSyncCurrentActiveRef_Type.__name__ = "Integer32"
_HneSysSyncCurrentActiveRef_Object = MibScalar
hneSysSyncCurrentActiveRef = _HneSysSyncCurrentActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 13),
    _HneSysSyncCurrentActiveRef_Type()
)
hneSysSyncCurrentActiveRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncCurrentActiveRef.setStatus("current")


class _HneSysSyncForcedState_Type(Integer32):
    """Custom type hneSysSyncForcedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoReferenceSwitchInhbit", 2),
          ("none", 0),
          ("revertiveSwitchInhibit", 1))
    )


_HneSysSyncForcedState_Type.__name__ = "Integer32"
_HneSysSyncForcedState_Object = MibScalar
hneSysSyncForcedState = _HneSysSyncForcedState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 2, 14),
    _HneSysSyncForcedState_Type()
)
hneSysSyncForcedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysSyncForcedState.setStatus("current")
_HneSystemHsf_ObjectIdentity = ObjectIdentity
hneSystemHsf = _HneSystemHsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 3)
)
_HneSysHsfWorking_Type = PhysicalIndex
_HneSysHsfWorking_Object = MibScalar
hneSysHsfWorking = _HneSysHsfWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 3, 1),
    _HneSysHsfWorking_Type()
)
hneSysHsfWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSysHsfWorking.setStatus("current")
_HneSysHsfProtect_Type = PhysicalIndex
_HneSysHsfProtect_Object = MibScalar
hneSysHsfProtect = _HneSysHsfProtect_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 1, 3, 2),
    _HneSysHsfProtect_Type()
)
hneSysHsfProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSysHsfProtect.setStatus("current")
_HneSonet_ObjectIdentity = ObjectIdentity
hneSonet = _HneSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2)
)
_HneSonetLineTable_Object = MibTable
hneSonetLineTable = _HneSonetLineTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hneSonetLineTable.setStatus("current")
_HneSonetLineEntry_Object = MibTableRow
hneSonetLineEntry = _HneSonetLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hneSonetLineEntry.setStatus("current")


class _HneSonetLineTimingSource_Type(Integer32):
    """Custom type hneSonetLineTimingSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 2),
          ("sync", 1))
    )


_HneSonetLineTimingSource_Type.__name__ = "Integer32"
_HneSonetLineTimingSource_Object = MibTableColumn
hneSonetLineTimingSource = _HneSonetLineTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 1, 1, 1),
    _HneSonetLineTimingSource_Type()
)
hneSonetLineTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetLineTimingSource.setStatus("current")


class _HneSonetLineDccSelection_Type(Integer32):
    """Custom type hneSonetLineDccSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 2),
          ("section", 1))
    )


_HneSonetLineDccSelection_Type.__name__ = "Integer32"
_HneSonetLineDccSelection_Object = MibTableColumn
hneSonetLineDccSelection = _HneSonetLineDccSelection_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 1, 1, 2),
    _HneSonetLineDccSelection_Type()
)
hneSonetLineDccSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetLineDccSelection.setStatus("current")


class _HneSonetLineOverheadLoopThroughModeEnabled_Type(TruthValue):
    """Custom type hneSonetLineOverheadLoopThroughModeEnabled based on TruthValue"""


_HneSonetLineOverheadLoopThroughModeEnabled_Object = MibTableColumn
hneSonetLineOverheadLoopThroughModeEnabled = _HneSonetLineOverheadLoopThroughModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 1, 1, 3),
    _HneSonetLineOverheadLoopThroughModeEnabled_Type()
)
hneSonetLineOverheadLoopThroughModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetLineOverheadLoopThroughModeEnabled.setStatus("current")
_HneSonetProtectionTable_Object = MibTable
hneSonetProtectionTable = _HneSonetProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hneSonetProtectionTable.setStatus("current")
_HneSonetProtectionEntry_Object = MibTableRow
hneSonetProtectionEntry = _HneSonetProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1)
)
hneSonetProtectionEntry.setIndexNames(
    (0, "SALIX-HNE-MIB", "hneSonetProtectionInterfaceHigh"),
    (0, "SALIX-HNE-MIB", "hneSonetProtectionInterfaceLow"),
)
if mibBuilder.loadTexts:
    hneSonetProtectionEntry.setStatus("current")
_HneSonetProtectionInterfaceHigh_Type = InterfaceIndex
_HneSonetProtectionInterfaceHigh_Object = MibTableColumn
hneSonetProtectionInterfaceHigh = _HneSonetProtectionInterfaceHigh_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 1),
    _HneSonetProtectionInterfaceHigh_Type()
)
hneSonetProtectionInterfaceHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneSonetProtectionInterfaceHigh.setStatus("current")
_HneSonetProtectionInterfaceLow_Type = InterfaceIndex
_HneSonetProtectionInterfaceLow_Object = MibTableColumn
hneSonetProtectionInterfaceLow = _HneSonetProtectionInterfaceLow_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 2),
    _HneSonetProtectionInterfaceLow_Type()
)
hneSonetProtectionInterfaceLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneSonetProtectionInterfaceLow.setStatus("current")
_HneSonetProtectionInterfaceWorking_Type = InterfaceIndex
_HneSonetProtectionInterfaceWorking_Object = MibTableColumn
hneSonetProtectionInterfaceWorking = _HneSonetProtectionInterfaceWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 3),
    _HneSonetProtectionInterfaceWorking_Type()
)
hneSonetProtectionInterfaceWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetProtectionInterfaceWorking.setStatus("current")


class _HneSonetProtectionConfig_Type(Integer32):
    """Custom type hneSonetProtectionConfig based on Integer32"""
    defaultValue = 1

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
        *(("none", 0),
          ("onePlusOne", 1),
          ("oneToN", 3),
          ("oneToOne", 2))
    )


_HneSonetProtectionConfig_Type.__name__ = "Integer32"
_HneSonetProtectionConfig_Object = MibTableColumn
hneSonetProtectionConfig = _HneSonetProtectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 4),
    _HneSonetProtectionConfig_Type()
)
hneSonetProtectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetProtectionConfig.setStatus("current")


class _HneSonetProtectionRevertive_Type(TruthValue):
    """Custom type hneSonetProtectionRevertive based on TruthValue"""


_HneSonetProtectionRevertive_Object = MibTableColumn
hneSonetProtectionRevertive = _HneSonetProtectionRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 5),
    _HneSonetProtectionRevertive_Type()
)
hneSonetProtectionRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetProtectionRevertive.setStatus("current")


class _HneSonetProtectionBiDirectional_Type(TruthValue):
    """Custom type hneSonetProtectionBiDirectional based on TruthValue"""


_HneSonetProtectionBiDirectional_Object = MibTableColumn
hneSonetProtectionBiDirectional = _HneSonetProtectionBiDirectional_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 2, 1, 6),
    _HneSonetProtectionBiDirectional_Type()
)
hneSonetProtectionBiDirectional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneSonetProtectionBiDirectional.setStatus("current")
_HneSonetPathTable_Object = MibTable
hneSonetPathTable = _HneSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hneSonetPathTable.setStatus("current")
_HneSonetPathEntry_Object = MibTableRow
hneSonetPathEntry = _HneSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hneSonetPathEntry.setStatus("current")


class _HneSonetPathContentType_Type(Integer32):
    """Custom type hneSonetPathContentType based on Integer32"""
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
        *(("atm", 1),
          ("atmVam", 2),
          ("notTerminated", 3),
          ("terminatedNotSpecified", 4))
    )


_HneSonetPathContentType_Type.__name__ = "Integer32"
_HneSonetPathContentType_Object = MibTableColumn
hneSonetPathContentType = _HneSonetPathContentType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 1),
    _HneSonetPathContentType_Type()
)
hneSonetPathContentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneSonetPathContentType.setStatus("current")
_HneSonetPathOverheadLoopThroughModeEnabled_Type = TruthValue
_HneSonetPathOverheadLoopThroughModeEnabled_Object = MibTableColumn
hneSonetPathOverheadLoopThroughModeEnabled = _HneSonetPathOverheadLoopThroughModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 2),
    _HneSonetPathOverheadLoopThroughModeEnabled_Type()
)
hneSonetPathOverheadLoopThroughModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathOverheadLoopThroughModeEnabled.setStatus("current")


class _HneSonetPathSpeMicMode_Type(Integer32):
    """Custom type hneSonetPathSpeMicMode based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("receive", 1),
          ("receiveTransmit", 3),
          ("transmit", 2))
    )


_HneSonetPathSpeMicMode_Type.__name__ = "Integer32"
_HneSonetPathSpeMicMode_Object = MibTableColumn
hneSonetPathSpeMicMode = _HneSonetPathSpeMicMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 3),
    _HneSonetPathSpeMicMode_Type()
)
hneSonetPathSpeMicMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneSonetPathSpeMicMode.setStatus("current")


class _HneSonetPathReceiveTraceMessage_Type(DisplayString):
    """Custom type hneSonetPathReceiveTraceMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneSonetPathReceiveTraceMessage_Type.__name__ = "DisplayString"
_HneSonetPathReceiveTraceMessage_Object = MibTableColumn
hneSonetPathReceiveTraceMessage = _HneSonetPathReceiveTraceMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 4),
    _HneSonetPathReceiveTraceMessage_Type()
)
hneSonetPathReceiveTraceMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneSonetPathReceiveTraceMessage.setStatus("current")


class _HneSonetPathTransmitTraceMessage_Type(DisplayString):
    """Custom type hneSonetPathTransmitTraceMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneSonetPathTransmitTraceMessage_Type.__name__ = "DisplayString"
_HneSonetPathTransmitTraceMessage_Object = MibTableColumn
hneSonetPathTransmitTraceMessage = _HneSonetPathTransmitTraceMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 5),
    _HneSonetPathTransmitTraceMessage_Type()
)
hneSonetPathTransmitTraceMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneSonetPathTransmitTraceMessage.setStatus("current")
_HneSonetPathRowStatus_Type = RowStatus
_HneSonetPathRowStatus_Object = MibTableColumn
hneSonetPathRowStatus = _HneSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 2, 3, 1, 6),
    _HneSonetPathRowStatus_Type()
)
hneSonetPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneSonetPathRowStatus.setStatus("current")
_HneTdm_ObjectIdentity = ObjectIdentity
hneTdm = _HneTdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3)
)
_HneTdmCrossConnectTable_Object = MibTable
hneTdmCrossConnectTable = _HneTdmCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hneTdmCrossConnectTable.setStatus("current")
_HneTdmCrossConnectEntry_Object = MibTableRow
hneTdmCrossConnectEntry = _HneTdmCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1, 1)
)
hneTdmCrossConnectEntry.setIndexNames(
    (0, "SALIX-HNE-MIB", "hneTdmCrossConnectPathTerminationPoint1"),
    (0, "SALIX-HNE-MIB", "hneTdmCrossConnectPathTerminationPoint2"),
)
if mibBuilder.loadTexts:
    hneTdmCrossConnectEntry.setStatus("current")
_HneTdmCrossConnectPathTerminationPoint1_Type = InterfaceIndex
_HneTdmCrossConnectPathTerminationPoint1_Object = MibTableColumn
hneTdmCrossConnectPathTerminationPoint1 = _HneTdmCrossConnectPathTerminationPoint1_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1, 1, 1),
    _HneTdmCrossConnectPathTerminationPoint1_Type()
)
hneTdmCrossConnectPathTerminationPoint1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneTdmCrossConnectPathTerminationPoint1.setStatus("current")
_HneTdmCrossConnectPathTerminationPoint2_Type = InterfaceIndex
_HneTdmCrossConnectPathTerminationPoint2_Object = MibTableColumn
hneTdmCrossConnectPathTerminationPoint2 = _HneTdmCrossConnectPathTerminationPoint2_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1, 1, 2),
    _HneTdmCrossConnectPathTerminationPoint2_Type()
)
hneTdmCrossConnectPathTerminationPoint2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneTdmCrossConnectPathTerminationPoint2.setStatus("current")


class _HneTdmCrossConnectOperStatus_Type(Integer32):
    """Custom type hneTdmCrossConnectOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_HneTdmCrossConnectOperStatus_Type.__name__ = "Integer32"
_HneTdmCrossConnectOperStatus_Object = MibTableColumn
hneTdmCrossConnectOperStatus = _HneTdmCrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1, 1, 3),
    _HneTdmCrossConnectOperStatus_Type()
)
hneTdmCrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneTdmCrossConnectOperStatus.setStatus("current")
_HneTdmCrossConnectRowStatus_Type = RowStatus
_HneTdmCrossConnectRowStatus_Object = MibTableColumn
hneTdmCrossConnectRowStatus = _HneTdmCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 3, 1, 1, 4),
    _HneTdmCrossConnectRowStatus_Type()
)
hneTdmCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneTdmCrossConnectRowStatus.setStatus("current")
_HneAtm_ObjectIdentity = ObjectIdentity
hneAtm = _HneAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4)
)
_HneAtmInterfaceConfTable_Object = MibTable
hneAtmInterfaceConfTable = _HneAtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hneAtmInterfaceConfTable.setStatus("current")
_HneAtmInterfaceConfEntry_Object = MibTableRow
hneAtmInterfaceConfEntry = _HneAtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hneAtmInterfaceConfEntry.setStatus("current")


class _HneAtmInterfaceValueAddedModeEnabled_Type(TruthValue):
    """Custom type hneAtmInterfaceValueAddedModeEnabled based on TruthValue"""


_HneAtmInterfaceValueAddedModeEnabled_Object = MibTableColumn
hneAtmInterfaceValueAddedModeEnabled = _HneAtmInterfaceValueAddedModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 1, 1, 2),
    _HneAtmInterfaceValueAddedModeEnabled_Type()
)
hneAtmInterfaceValueAddedModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmInterfaceValueAddedModeEnabled.setStatus("current")
_HneAtmTrafficDescrParamIndexNext_Type = AtmTrafficDescrParamIndex
_HneAtmTrafficDescrParamIndexNext_Object = MibScalar
hneAtmTrafficDescrParamIndexNext = _HneAtmTrafficDescrParamIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 3),
    _HneAtmTrafficDescrParamIndexNext_Type()
)
hneAtmTrafficDescrParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmTrafficDescrParamIndexNext.setStatus("current")
_HneAtmVplTable_Object = MibTable
hneAtmVplTable = _HneAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hneAtmVplTable.setStatus("current")
_HneAtmVplEntry_Object = MibTableRow
hneAtmVplEntry = _HneAtmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hneAtmVplEntry.setStatus("current")


class _HneAtmVplVamMode_Type(Integer32):
    """Custom type hneAtmVplVamMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hostTerminated", 1),
          ("none", 0))
    )


_HneAtmVplVamMode_Type.__name__ = "Integer32"
_HneAtmVplVamMode_Object = MibTableColumn
hneAtmVplVamMode = _HneAtmVplVamMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 4, 4, 1, 1),
    _HneAtmVplVamMode_Type()
)
hneAtmVplVamMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneAtmVplVamMode.setStatus("current")
_HneAtmfM4_ObjectIdentity = ObjectIdentity
hneAtmfM4 = _HneAtmfM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 5)
)
_HneAtmfM4TcAdaptorTable_Object = MibTable
hneAtmfM4TcAdaptorTable = _HneAtmfM4TcAdaptorTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hneAtmfM4TcAdaptorTable.setStatus("current")
_HneAtmfM4TcAdaptorEntry_Object = MibTableRow
hneAtmfM4TcAdaptorEntry = _HneAtmfM4TcAdaptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hneAtmfM4TcAdaptorEntry.setStatus("current")


class _HneAtmfM4TcHecErroredCellAction_Type(Integer32):
    """Custom type hneAtmfM4TcHecErroredCellAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("pass", 1))
    )


_HneAtmfM4TcHecErroredCellAction_Type.__name__ = "Integer32"
_HneAtmfM4TcHecErroredCellAction_Object = MibTableColumn
hneAtmfM4TcHecErroredCellAction = _HneAtmfM4TcHecErroredCellAction_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 5, 1, 1, 1),
    _HneAtmfM4TcHecErroredCellAction_Type()
)
hneAtmfM4TcHecErroredCellAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneAtmfM4TcHecErroredCellAction.setStatus("current")
_HnePlugInUnit_ObjectIdentity = ObjectIdentity
hnePlugInUnit = _HnePlugInUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 1, 6)
)
_HneMIBTraps_ObjectIdentity = ObjectIdentity
hneMIBTraps = _HneMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 2)
)
_HneMIBCompliance_ObjectIdentity = ObjectIdentity
hneMIBCompliance = _HneMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3)
)
_HneGroups_ObjectIdentity = ObjectIdentity
hneGroups = _HneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1)
)
_HneCompliances_ObjectIdentity = ObjectIdentity
hneCompliances = _HneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 2)
)
_HneMIBStats_ObjectIdentity = ObjectIdentity
hneMIBStats = _HneMIBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4)
)
_HneSonetPathCurrentTable_Object = MibTable
hneSonetPathCurrentTable = _HneSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hneSonetPathCurrentTable.setStatus("current")
_HneSonetPathCurrentEntry_Object = MibTableRow
hneSonetPathCurrentEntry = _HneSonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hneSonetPathCurrentEntry.setStatus("current")
_HneSonetPathCurrentRxPosPointerJustCount_Type = Gauge32
_HneSonetPathCurrentRxPosPointerJustCount_Object = MibTableColumn
hneSonetPathCurrentRxPosPointerJustCount = _HneSonetPathCurrentRxPosPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5, 1, 1),
    _HneSonetPathCurrentRxPosPointerJustCount_Type()
)
hneSonetPathCurrentRxPosPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathCurrentRxPosPointerJustCount.setStatus("current")
_HneSonetPathCurrentRxNegPointerJustCount_Type = Gauge32
_HneSonetPathCurrentRxNegPointerJustCount_Object = MibTableColumn
hneSonetPathCurrentRxNegPointerJustCount = _HneSonetPathCurrentRxNegPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5, 1, 2),
    _HneSonetPathCurrentRxNegPointerJustCount_Type()
)
hneSonetPathCurrentRxNegPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathCurrentRxNegPointerJustCount.setStatus("current")
_HneSonetPathCurrentTxPosPointerJustCount_Type = Gauge32
_HneSonetPathCurrentTxPosPointerJustCount_Object = MibTableColumn
hneSonetPathCurrentTxPosPointerJustCount = _HneSonetPathCurrentTxPosPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5, 1, 3),
    _HneSonetPathCurrentTxPosPointerJustCount_Type()
)
hneSonetPathCurrentTxPosPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathCurrentTxPosPointerJustCount.setStatus("current")
_HneSonetPathCurrentTxNegPointerJustCount_Type = Gauge32
_HneSonetPathCurrentTxNegPointerJustCount_Object = MibTableColumn
hneSonetPathCurrentTxNegPointerJustCount = _HneSonetPathCurrentTxNegPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 5, 1, 4),
    _HneSonetPathCurrentTxNegPointerJustCount_Type()
)
hneSonetPathCurrentTxNegPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathCurrentTxNegPointerJustCount.setStatus("current")
_HneSonetPathIntervalTable_Object = MibTable
hneSonetPathIntervalTable = _HneSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hneSonetPathIntervalTable.setStatus("current")
_HneSonetPathIntervalEntry_Object = MibTableRow
hneSonetPathIntervalEntry = _HneSonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hneSonetPathIntervalEntry.setStatus("current")
_HneSonetPathIntervalRxPosPointerJustCount_Type = Gauge32
_HneSonetPathIntervalRxPosPointerJustCount_Object = MibTableColumn
hneSonetPathIntervalRxPosPointerJustCount = _HneSonetPathIntervalRxPosPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6, 1, 1),
    _HneSonetPathIntervalRxPosPointerJustCount_Type()
)
hneSonetPathIntervalRxPosPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathIntervalRxPosPointerJustCount.setStatus("current")
_HneSonetPathIntervalRxNegPointerJustCount_Type = Gauge32
_HneSonetPathIntervalRxNegPointerJustCount_Object = MibTableColumn
hneSonetPathIntervalRxNegPointerJustCount = _HneSonetPathIntervalRxNegPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6, 1, 2),
    _HneSonetPathIntervalRxNegPointerJustCount_Type()
)
hneSonetPathIntervalRxNegPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathIntervalRxNegPointerJustCount.setStatus("current")
_HneSonetPathIntervalTxPosPointerJustCount_Type = Gauge32
_HneSonetPathIntervalTxPosPointerJustCount_Object = MibTableColumn
hneSonetPathIntervalTxPosPointerJustCount = _HneSonetPathIntervalTxPosPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6, 1, 3),
    _HneSonetPathIntervalTxPosPointerJustCount_Type()
)
hneSonetPathIntervalTxPosPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathIntervalTxPosPointerJustCount.setStatus("current")
_HneSonetPathIntervalTxNegPointerJustCount_Type = Gauge32
_HneSonetPathIntervalTxNegPointerJustCount_Object = MibTableColumn
hneSonetPathIntervalTxNegPointerJustCount = _HneSonetPathIntervalTxNegPointerJustCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 6, 1, 4),
    _HneSonetPathIntervalTxNegPointerJustCount_Type()
)
hneSonetPathIntervalTxNegPointerJustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneSonetPathIntervalTxNegPointerJustCount.setStatus("current")
_HneAtmLiuCurrentTable_Object = MibTable
hneAtmLiuCurrentTable = _HneAtmLiuCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    hneAtmLiuCurrentTable.setStatus("current")
_HneAtmLiuCurrentEntry_Object = MibTableRow
hneAtmLiuCurrentEntry = _HneAtmLiuCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1)
)
hneAtmLiuCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hneAtmLiuCurrentEntry.setStatus("current")
_HneAtmLiuCurrentPhysLayerCellCount_Type = Gauge32
_HneAtmLiuCurrentPhysLayerCellCount_Object = MibTableColumn
hneAtmLiuCurrentPhysLayerCellCount = _HneAtmLiuCurrentPhysLayerCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 1),
    _HneAtmLiuCurrentPhysLayerCellCount_Type()
)
hneAtmLiuCurrentPhysLayerCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentPhysLayerCellCount.setStatus("current")
_HneAtmLiuCurrentRxCellCount_Type = Counter64
_HneAtmLiuCurrentRxCellCount_Object = MibTableColumn
hneAtmLiuCurrentRxCellCount = _HneAtmLiuCurrentRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 2),
    _HneAtmLiuCurrentRxCellCount_Type()
)
hneAtmLiuCurrentRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentRxCellCount.setStatus("current")
_HneAtmLiuCurrentTxCellCount_Type = Gauge32
_HneAtmLiuCurrentTxCellCount_Object = MibTableColumn
hneAtmLiuCurrentTxCellCount = _HneAtmLiuCurrentTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 3),
    _HneAtmLiuCurrentTxCellCount_Type()
)
hneAtmLiuCurrentTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentTxCellCount.setStatus("current")
_HneAtmLiuCurrentCongestionDroppedCount_Type = Gauge32
_HneAtmLiuCurrentCongestionDroppedCount_Object = MibTableColumn
hneAtmLiuCurrentCongestionDroppedCount = _HneAtmLiuCurrentCongestionDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 4),
    _HneAtmLiuCurrentCongestionDroppedCount_Type()
)
hneAtmLiuCurrentCongestionDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentCongestionDroppedCount.setStatus("current")
_HneAtmLiuCurrentInvalidCellCount_Type = Gauge32
_HneAtmLiuCurrentInvalidCellCount_Object = MibTableColumn
hneAtmLiuCurrentInvalidCellCount = _HneAtmLiuCurrentInvalidCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 5),
    _HneAtmLiuCurrentInvalidCellCount_Type()
)
hneAtmLiuCurrentInvalidCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentInvalidCellCount.setStatus("current")
_HneAtmLiuCurrentErroredOAMCellCount_Type = Gauge32
_HneAtmLiuCurrentErroredOAMCellCount_Object = MibTableColumn
hneAtmLiuCurrentErroredOAMCellCount = _HneAtmLiuCurrentErroredOAMCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 6),
    _HneAtmLiuCurrentErroredOAMCellCount_Type()
)
hneAtmLiuCurrentErroredOAMCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentErroredOAMCellCount.setStatus("current")
_HneAtmLiuCurrentValidOAMCellCount_Type = Gauge32
_HneAtmLiuCurrentValidOAMCellCount_Object = MibTableColumn
hneAtmLiuCurrentValidOAMCellCount = _HneAtmLiuCurrentValidOAMCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 7),
    _HneAtmLiuCurrentValidOAMCellCount_Type()
)
hneAtmLiuCurrentValidOAMCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentValidOAMCellCount.setStatus("current")
_HneAtmLiuCurrentTxOverrunCount_Type = Gauge32
_HneAtmLiuCurrentTxOverrunCount_Object = MibTableColumn
hneAtmLiuCurrentTxOverrunCount = _HneAtmLiuCurrentTxOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 8),
    _HneAtmLiuCurrentTxOverrunCount_Type()
)
hneAtmLiuCurrentTxOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentTxOverrunCount.setStatus("current")
_HneAtmLiuCurrentMissingHeaderCellCount_Type = Gauge32
_HneAtmLiuCurrentMissingHeaderCellCount_Object = MibTableColumn
hneAtmLiuCurrentMissingHeaderCellCount = _HneAtmLiuCurrentMissingHeaderCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 9),
    _HneAtmLiuCurrentMissingHeaderCellCount_Type()
)
hneAtmLiuCurrentMissingHeaderCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentMissingHeaderCellCount.setStatus("current")
_HneAtmLiuCurrentNonRoutableCellCount_Type = Gauge32
_HneAtmLiuCurrentNonRoutableCellCount_Object = MibTableColumn
hneAtmLiuCurrentNonRoutableCellCount = _HneAtmLiuCurrentNonRoutableCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 10),
    _HneAtmLiuCurrentNonRoutableCellCount_Type()
)
hneAtmLiuCurrentNonRoutableCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentNonRoutableCellCount.setStatus("current")
_HneAtmLiuCurrentVcSearchFailedCount_Type = Gauge32
_HneAtmLiuCurrentVcSearchFailedCount_Object = MibTableColumn
hneAtmLiuCurrentVcSearchFailedCount = _HneAtmLiuCurrentVcSearchFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 11),
    _HneAtmLiuCurrentVcSearchFailedCount_Type()
)
hneAtmLiuCurrentVcSearchFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentVcSearchFailedCount.setStatus("current")
_HneAtmLiuCurrentInternalParityErrorCount_Type = Gauge32
_HneAtmLiuCurrentInternalParityErrorCount_Object = MibTableColumn
hneAtmLiuCurrentInternalParityErrorCount = _HneAtmLiuCurrentInternalParityErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 7, 1, 12),
    _HneAtmLiuCurrentInternalParityErrorCount_Type()
)
hneAtmLiuCurrentInternalParityErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuCurrentInternalParityErrorCount.setStatus("current")
_HneAtmLiuHistoryTable_Object = MibTable
hneAtmLiuHistoryTable = _HneAtmLiuHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    hneAtmLiuHistoryTable.setStatus("current")
_HneAtmLiuHistoryEntry_Object = MibTableRow
hneAtmLiuHistoryEntry = _HneAtmLiuHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1)
)
hneAtmLiuHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4CellProtoHistIndex"),
)
if mibBuilder.loadTexts:
    hneAtmLiuHistoryEntry.setStatus("current")
_HneAtmLiuHistoryPhysLayerCellCount_Type = Gauge32
_HneAtmLiuHistoryPhysLayerCellCount_Object = MibTableColumn
hneAtmLiuHistoryPhysLayerCellCount = _HneAtmLiuHistoryPhysLayerCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 1),
    _HneAtmLiuHistoryPhysLayerCellCount_Type()
)
hneAtmLiuHistoryPhysLayerCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryPhysLayerCellCount.setStatus("current")
_HneAtmLiuHistoryRxCellCount_Type = Counter64
_HneAtmLiuHistoryRxCellCount_Object = MibTableColumn
hneAtmLiuHistoryRxCellCount = _HneAtmLiuHistoryRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 2),
    _HneAtmLiuHistoryRxCellCount_Type()
)
hneAtmLiuHistoryRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryRxCellCount.setStatus("current")
_HneAtmLiuHistoryTxCellCount_Type = Gauge32
_HneAtmLiuHistoryTxCellCount_Object = MibTableColumn
hneAtmLiuHistoryTxCellCount = _HneAtmLiuHistoryTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 3),
    _HneAtmLiuHistoryTxCellCount_Type()
)
hneAtmLiuHistoryTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryTxCellCount.setStatus("current")
_HneAtmLiuHistoryCongestionDroppedCount_Type = Gauge32
_HneAtmLiuHistoryCongestionDroppedCount_Object = MibTableColumn
hneAtmLiuHistoryCongestionDroppedCount = _HneAtmLiuHistoryCongestionDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 4),
    _HneAtmLiuHistoryCongestionDroppedCount_Type()
)
hneAtmLiuHistoryCongestionDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryCongestionDroppedCount.setStatus("current")
_HneAtmLiuHistoryInvalidCellCount_Type = Gauge32
_HneAtmLiuHistoryInvalidCellCount_Object = MibTableColumn
hneAtmLiuHistoryInvalidCellCount = _HneAtmLiuHistoryInvalidCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 5),
    _HneAtmLiuHistoryInvalidCellCount_Type()
)
hneAtmLiuHistoryInvalidCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryInvalidCellCount.setStatus("current")
_HneAtmLiuHistoryErroredOAMCellCount_Type = Gauge32
_HneAtmLiuHistoryErroredOAMCellCount_Object = MibTableColumn
hneAtmLiuHistoryErroredOAMCellCount = _HneAtmLiuHistoryErroredOAMCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 6),
    _HneAtmLiuHistoryErroredOAMCellCount_Type()
)
hneAtmLiuHistoryErroredOAMCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryErroredOAMCellCount.setStatus("current")
_HneAtmLiuHistoryValidOAMCellCount_Type = Gauge32
_HneAtmLiuHistoryValidOAMCellCount_Object = MibTableColumn
hneAtmLiuHistoryValidOAMCellCount = _HneAtmLiuHistoryValidOAMCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 7),
    _HneAtmLiuHistoryValidOAMCellCount_Type()
)
hneAtmLiuHistoryValidOAMCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryValidOAMCellCount.setStatus("current")
_HneAtmLiuHistoryTxOverrunCount_Type = Gauge32
_HneAtmLiuHistoryTxOverrunCount_Object = MibTableColumn
hneAtmLiuHistoryTxOverrunCount = _HneAtmLiuHistoryTxOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 8),
    _HneAtmLiuHistoryTxOverrunCount_Type()
)
hneAtmLiuHistoryTxOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryTxOverrunCount.setStatus("current")
_HneAtmLiuHistoryMissingHeaderCellCount_Type = Gauge32
_HneAtmLiuHistoryMissingHeaderCellCount_Object = MibTableColumn
hneAtmLiuHistoryMissingHeaderCellCount = _HneAtmLiuHistoryMissingHeaderCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 9),
    _HneAtmLiuHistoryMissingHeaderCellCount_Type()
)
hneAtmLiuHistoryMissingHeaderCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryMissingHeaderCellCount.setStatus("current")
_HneAtmLiuHistoryNonRoutableCellCount_Type = Gauge32
_HneAtmLiuHistoryNonRoutableCellCount_Object = MibTableColumn
hneAtmLiuHistoryNonRoutableCellCount = _HneAtmLiuHistoryNonRoutableCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 10),
    _HneAtmLiuHistoryNonRoutableCellCount_Type()
)
hneAtmLiuHistoryNonRoutableCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryNonRoutableCellCount.setStatus("current")
_HneAtmLiuHistoryVcSearchFailedCount_Type = Gauge32
_HneAtmLiuHistoryVcSearchFailedCount_Object = MibTableColumn
hneAtmLiuHistoryVcSearchFailedCount = _HneAtmLiuHistoryVcSearchFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 11),
    _HneAtmLiuHistoryVcSearchFailedCount_Type()
)
hneAtmLiuHistoryVcSearchFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryVcSearchFailedCount.setStatus("current")
_HneAtmLiuHistoryInternalParityErrorCount_Type = Gauge32
_HneAtmLiuHistoryInternalParityErrorCount_Object = MibTableColumn
hneAtmLiuHistoryInternalParityErrorCount = _HneAtmLiuHistoryInternalParityErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 8, 1, 12),
    _HneAtmLiuHistoryInternalParityErrorCount_Type()
)
hneAtmLiuHistoryInternalParityErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAtmLiuHistoryInternalParityErrorCount.setStatus("current")
_HneVclCurrentTable_Object = MibTable
hneVclCurrentTable = _HneVclCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    hneVclCurrentTable.setStatus("current")
_HneVclCurrentEntry_Object = MibTableRow
hneVclCurrentEntry = _HneVclCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1)
)
hneVclCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    hneVclCurrentEntry.setStatus("current")
_HneVclCurrentBIP16Count_Type = Gauge32
_HneVclCurrentBIP16Count_Object = MibTableColumn
hneVclCurrentBIP16Count = _HneVclCurrentBIP16Count_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 5),
    _HneVclCurrentBIP16Count_Type()
)
hneVclCurrentBIP16Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentBIP16Count.setStatus("current")
_HneVclCurrentRxSECBCount_Type = Gauge32
_HneVclCurrentRxSECBCount_Object = MibTableColumn
hneVclCurrentRxSECBCount = _HneVclCurrentRxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 6),
    _HneVclCurrentRxSECBCount_Type()
)
hneVclCurrentRxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentRxSECBCount.setStatus("current")
_HneVclCurrentRxLostCellCount_Type = Gauge32
_HneVclCurrentRxLostCellCount_Object = MibTableColumn
hneVclCurrentRxLostCellCount = _HneVclCurrentRxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 7),
    _HneVclCurrentRxLostCellCount_Type()
)
hneVclCurrentRxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentRxLostCellCount.setStatus("current")
_HneVclCurrentRxMisinsertedCellCount_Type = Gauge32
_HneVclCurrentRxMisinsertedCellCount_Object = MibTableColumn
hneVclCurrentRxMisinsertedCellCount = _HneVclCurrentRxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 8),
    _HneVclCurrentRxMisinsertedCellCount_Type()
)
hneVclCurrentRxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentRxMisinsertedCellCount.setStatus("current")
_HneVclCurrentRxBIPVCount_Type = Gauge32
_HneVclCurrentRxBIPVCount_Object = MibTableColumn
hneVclCurrentRxBIPVCount = _HneVclCurrentRxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 9),
    _HneVclCurrentRxBIPVCount_Type()
)
hneVclCurrentRxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentRxBIPVCount.setStatus("current")
_HneVclCurrentTxSECBCount_Type = Gauge32
_HneVclCurrentTxSECBCount_Object = MibTableColumn
hneVclCurrentTxSECBCount = _HneVclCurrentTxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 10),
    _HneVclCurrentTxSECBCount_Type()
)
hneVclCurrentTxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentTxSECBCount.setStatus("current")
_HneVclCurrentTxLostCellCount_Type = Gauge32
_HneVclCurrentTxLostCellCount_Object = MibTableColumn
hneVclCurrentTxLostCellCount = _HneVclCurrentTxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 11),
    _HneVclCurrentTxLostCellCount_Type()
)
hneVclCurrentTxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentTxLostCellCount.setStatus("current")
_HneVclCurrentTxMisinsertedCellCount_Type = Gauge32
_HneVclCurrentTxMisinsertedCellCount_Object = MibTableColumn
hneVclCurrentTxMisinsertedCellCount = _HneVclCurrentTxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 12),
    _HneVclCurrentTxMisinsertedCellCount_Type()
)
hneVclCurrentTxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentTxMisinsertedCellCount.setStatus("current")
_HneVclCurrentTxBIPVCount_Type = Gauge32
_HneVclCurrentTxBIPVCount_Object = MibTableColumn
hneVclCurrentTxBIPVCount = _HneVclCurrentTxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 9, 1, 13),
    _HneVclCurrentTxBIPVCount_Type()
)
hneVclCurrentTxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclCurrentTxBIPVCount.setStatus("current")
_HneVclHistoryTable_Object = MibTable
hneVclHistoryTable = _HneVclHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    hneVclHistoryTable.setStatus("current")
_HneVclHistoryEntry_Object = MibTableRow
hneVclHistoryEntry = _HneVclHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1)
)
hneVclHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4CellProtoHistIndex"),
)
if mibBuilder.loadTexts:
    hneVclHistoryEntry.setStatus("current")
_HneVclHistoryBIP16Count_Type = Gauge32
_HneVclHistoryBIP16Count_Object = MibTableColumn
hneVclHistoryBIP16Count = _HneVclHistoryBIP16Count_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 5),
    _HneVclHistoryBIP16Count_Type()
)
hneVclHistoryBIP16Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryBIP16Count.setStatus("current")
_HneVclHistoryRxSECBCount_Type = Gauge32
_HneVclHistoryRxSECBCount_Object = MibTableColumn
hneVclHistoryRxSECBCount = _HneVclHistoryRxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 6),
    _HneVclHistoryRxSECBCount_Type()
)
hneVclHistoryRxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryRxSECBCount.setStatus("current")
_HneVclHistoryRxLostCellCount_Type = Gauge32
_HneVclHistoryRxLostCellCount_Object = MibTableColumn
hneVclHistoryRxLostCellCount = _HneVclHistoryRxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 7),
    _HneVclHistoryRxLostCellCount_Type()
)
hneVclHistoryRxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryRxLostCellCount.setStatus("current")
_HneVclHistoryRxMisinsertedCellCount_Type = Gauge32
_HneVclHistoryRxMisinsertedCellCount_Object = MibTableColumn
hneVclHistoryRxMisinsertedCellCount = _HneVclHistoryRxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 8),
    _HneVclHistoryRxMisinsertedCellCount_Type()
)
hneVclHistoryRxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryRxMisinsertedCellCount.setStatus("current")
_HneVclHistoryRxBIPVCount_Type = Gauge32
_HneVclHistoryRxBIPVCount_Object = MibTableColumn
hneVclHistoryRxBIPVCount = _HneVclHistoryRxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 9),
    _HneVclHistoryRxBIPVCount_Type()
)
hneVclHistoryRxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryRxBIPVCount.setStatus("current")
_HneVclHistoryTxSECBCount_Type = Gauge32
_HneVclHistoryTxSECBCount_Object = MibTableColumn
hneVclHistoryTxSECBCount = _HneVclHistoryTxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 10),
    _HneVclHistoryTxSECBCount_Type()
)
hneVclHistoryTxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryTxSECBCount.setStatus("current")
_HneVclHistoryTxLostCellCount_Type = Gauge32
_HneVclHistoryTxLostCellCount_Object = MibTableColumn
hneVclHistoryTxLostCellCount = _HneVclHistoryTxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 11),
    _HneVclHistoryTxLostCellCount_Type()
)
hneVclHistoryTxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryTxLostCellCount.setStatus("current")
_HneVclHistoryTxMisinsertedCellCount_Type = Gauge32
_HneVclHistoryTxMisinsertedCellCount_Object = MibTableColumn
hneVclHistoryTxMisinsertedCellCount = _HneVclHistoryTxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 12),
    _HneVclHistoryTxMisinsertedCellCount_Type()
)
hneVclHistoryTxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryTxMisinsertedCellCount.setStatus("current")
_HneVclHistoryTxBIPVCount_Type = Gauge32
_HneVclHistoryTxBIPVCount_Object = MibTableColumn
hneVclHistoryTxBIPVCount = _HneVclHistoryTxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 10, 1, 13),
    _HneVclHistoryTxBIPVCount_Type()
)
hneVclHistoryTxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVclHistoryTxBIPVCount.setStatus("current")
_HneVplCurrentTable_Object = MibTable
hneVplCurrentTable = _HneVplCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    hneVplCurrentTable.setStatus("current")
_HneVplCurrentEntry_Object = MibTableRow
hneVplCurrentEntry = _HneVplCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1)
)
hneVplCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    hneVplCurrentEntry.setStatus("current")
_HneVplCurrentBIP16Count_Type = Gauge32
_HneVplCurrentBIP16Count_Object = MibTableColumn
hneVplCurrentBIP16Count = _HneVplCurrentBIP16Count_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 5),
    _HneVplCurrentBIP16Count_Type()
)
hneVplCurrentBIP16Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentBIP16Count.setStatus("current")
_HneVplCurrentRxSECBCount_Type = Gauge32
_HneVplCurrentRxSECBCount_Object = MibTableColumn
hneVplCurrentRxSECBCount = _HneVplCurrentRxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 6),
    _HneVplCurrentRxSECBCount_Type()
)
hneVplCurrentRxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentRxSECBCount.setStatus("current")
_HneVplCurrentRxLostCellCount_Type = Gauge32
_HneVplCurrentRxLostCellCount_Object = MibTableColumn
hneVplCurrentRxLostCellCount = _HneVplCurrentRxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 7),
    _HneVplCurrentRxLostCellCount_Type()
)
hneVplCurrentRxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentRxLostCellCount.setStatus("current")
_HneVplCurrentRxMisinsertedCellCount_Type = Gauge32
_HneVplCurrentRxMisinsertedCellCount_Object = MibTableColumn
hneVplCurrentRxMisinsertedCellCount = _HneVplCurrentRxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 8),
    _HneVplCurrentRxMisinsertedCellCount_Type()
)
hneVplCurrentRxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentRxMisinsertedCellCount.setStatus("current")
_HneVplCurrentRxBIPVCount_Type = Gauge32
_HneVplCurrentRxBIPVCount_Object = MibTableColumn
hneVplCurrentRxBIPVCount = _HneVplCurrentRxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 9),
    _HneVplCurrentRxBIPVCount_Type()
)
hneVplCurrentRxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentRxBIPVCount.setStatus("current")
_HneVplCurrentTxSECBCount_Type = Gauge32
_HneVplCurrentTxSECBCount_Object = MibTableColumn
hneVplCurrentTxSECBCount = _HneVplCurrentTxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 10),
    _HneVplCurrentTxSECBCount_Type()
)
hneVplCurrentTxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentTxSECBCount.setStatus("current")
_HneVplCurrentTxLostCellCount_Type = Gauge32
_HneVplCurrentTxLostCellCount_Object = MibTableColumn
hneVplCurrentTxLostCellCount = _HneVplCurrentTxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 11),
    _HneVplCurrentTxLostCellCount_Type()
)
hneVplCurrentTxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentTxLostCellCount.setStatus("current")
_HneVplCurrentTxMisinsertedCellCount_Type = Gauge32
_HneVplCurrentTxMisinsertedCellCount_Object = MibTableColumn
hneVplCurrentTxMisinsertedCellCount = _HneVplCurrentTxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 12),
    _HneVplCurrentTxMisinsertedCellCount_Type()
)
hneVplCurrentTxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentTxMisinsertedCellCount.setStatus("current")
_HneVplCurrentTxBIPVCount_Type = Gauge32
_HneVplCurrentTxBIPVCount_Object = MibTableColumn
hneVplCurrentTxBIPVCount = _HneVplCurrentTxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 11, 1, 13),
    _HneVplCurrentTxBIPVCount_Type()
)
hneVplCurrentTxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplCurrentTxBIPVCount.setStatus("current")
_HneVplHistoryTable_Object = MibTable
hneVplHistoryTable = _HneVplHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12)
)
if mibBuilder.loadTexts:
    hneVplHistoryTable.setStatus("current")
_HneVplHistoryEntry_Object = MibTableRow
hneVplHistoryEntry = _HneVplHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1)
)
hneVplHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-FORUM-M4-MIB", "atmfM4CellProtoHistIndex"),
)
if mibBuilder.loadTexts:
    hneVplHistoryEntry.setStatus("current")
_HneVplHistoryBIP16Count_Type = Gauge32
_HneVplHistoryBIP16Count_Object = MibTableColumn
hneVplHistoryBIP16Count = _HneVplHistoryBIP16Count_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 5),
    _HneVplHistoryBIP16Count_Type()
)
hneVplHistoryBIP16Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryBIP16Count.setStatus("current")
_HneVplHistoryRxSECBCount_Type = Gauge32
_HneVplHistoryRxSECBCount_Object = MibTableColumn
hneVplHistoryRxSECBCount = _HneVplHistoryRxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 6),
    _HneVplHistoryRxSECBCount_Type()
)
hneVplHistoryRxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryRxSECBCount.setStatus("current")
_HneVplHistoryRxLostCellCount_Type = Gauge32
_HneVplHistoryRxLostCellCount_Object = MibTableColumn
hneVplHistoryRxLostCellCount = _HneVplHistoryRxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 7),
    _HneVplHistoryRxLostCellCount_Type()
)
hneVplHistoryRxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryRxLostCellCount.setStatus("current")
_HneVplHistoryRxMisinsertedCellCount_Type = Gauge32
_HneVplHistoryRxMisinsertedCellCount_Object = MibTableColumn
hneVplHistoryRxMisinsertedCellCount = _HneVplHistoryRxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 8),
    _HneVplHistoryRxMisinsertedCellCount_Type()
)
hneVplHistoryRxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryRxMisinsertedCellCount.setStatus("current")
_HneVplHistoryRxBIPVCount_Type = Gauge32
_HneVplHistoryRxBIPVCount_Object = MibTableColumn
hneVplHistoryRxBIPVCount = _HneVplHistoryRxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 9),
    _HneVplHistoryRxBIPVCount_Type()
)
hneVplHistoryRxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryRxBIPVCount.setStatus("current")
_HneVplHistoryTxSECBCount_Type = Gauge32
_HneVplHistoryTxSECBCount_Object = MibTableColumn
hneVplHistoryTxSECBCount = _HneVplHistoryTxSECBCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 10),
    _HneVplHistoryTxSECBCount_Type()
)
hneVplHistoryTxSECBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryTxSECBCount.setStatus("current")
_HneVplHistoryTxLostCellCount_Type = Gauge32
_HneVplHistoryTxLostCellCount_Object = MibTableColumn
hneVplHistoryTxLostCellCount = _HneVplHistoryTxLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 11),
    _HneVplHistoryTxLostCellCount_Type()
)
hneVplHistoryTxLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryTxLostCellCount.setStatus("current")
_HneVplHistoryTxMisinsertedCellCount_Type = Gauge32
_HneVplHistoryTxMisinsertedCellCount_Object = MibTableColumn
hneVplHistoryTxMisinsertedCellCount = _HneVplHistoryTxMisinsertedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 12),
    _HneVplHistoryTxMisinsertedCellCount_Type()
)
hneVplHistoryTxMisinsertedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryTxMisinsertedCellCount.setStatus("current")
_HneVplHistoryTxBIPVCount_Type = Gauge32
_HneVplHistoryTxBIPVCount_Object = MibTableColumn
hneVplHistoryTxBIPVCount = _HneVplHistoryTxBIPVCount_Object(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 4, 12, 1, 13),
    _HneVplHistoryTxBIPVCount_Type()
)
hneVplHistoryTxBIPVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneVplHistoryTxBIPVCount.setStatus("current")
sonetMediumEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneSonetLineEntry")
)
hneSonetLineEntry.setIndexNames(*sonetMediumEntry.getIndexNames())
sonetPathCurrentEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneSonetPathEntry")
)
hneSonetPathEntry.setIndexNames(*sonetPathCurrentEntry.getIndexNames())
atmInterfaceConfEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneAtmInterfaceConfEntry")
)
hneAtmInterfaceConfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneAtmVplEntry")
)
hneAtmVplEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmfM4TcAdaptorEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneAtmfM4TcAdaptorEntry")
)
hneAtmfM4TcAdaptorEntry.setIndexNames(*atmfM4TcAdaptorEntry.getIndexNames())
sonetPathCurrentEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneSonetPathCurrentEntry")
)
hneSonetPathCurrentEntry.setIndexNames(*sonetPathCurrentEntry.getIndexNames())
sonetPathIntervalEntry.registerAugmentions(
    ("SALIX-HNE-MIB",
     "hneSonetPathIntervalEntry")
)
hneSonetPathIntervalEntry.setIndexNames(*sonetPathIntervalEntry.getIndexNames())

# Managed Objects groups

hneSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1, 1)
)
hneSystemGroup.setObjects(
      *(("SALIX-HNE-MIB", "hneSysSyncTimingMode"),
        ("SALIX-HNE-MIB", "hneSysSyncPrimaryRefLine"),
        ("SALIX-HNE-MIB", "hneSysSyncSecondaryRefLine"),
        ("SALIX-HNE-MIB", "hneSysSyncRevertiveSwitch"),
        ("SALIX-HNE-MIB", "hneSysSyncClockMode"),
        ("SALIX-HNE-MIB", "hneSysSyncConfiguredActiveRef"),
        ("SALIX-HNE-MIB", "hneSysSyncAutoRefSwitch"),
        ("SALIX-HNE-MIB", "hneSysSyncFreeRunAlarm"),
        ("SALIX-HNE-MIB", "hneSysSyncWorking"),
        ("SALIX-HNE-MIB", "hneSysSyncProtect"),
        ("SALIX-HNE-MIB", "hneSysSyncPrimaryRefLineState"),
        ("SALIX-HNE-MIB", "hneSysSyncSecondaryRefLineState"),
        ("SALIX-HNE-MIB", "hneSysSyncCurrentActiveRef"),
        ("SALIX-HNE-MIB", "hneSysSyncForcedState"),
        ("SALIX-HNE-MIB", "hneSysHsfWorking"),
        ("SALIX-HNE-MIB", "hneSysHsfProtect"))
)
if mibBuilder.loadTexts:
    hneSystemGroup.setStatus("current")

hneSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1, 2)
)
hneSonetGroup.setObjects(
      *(("SALIX-HNE-MIB", "hneSonetLineTimingSource"),
        ("SALIX-HNE-MIB", "hneSonetLineDccSelection"),
        ("SALIX-HNE-MIB", "hneSonetLineOverheadLoopThroughModeEnabled"),
        ("SALIX-HNE-MIB", "hneSonetProtectionInterfaceWorking"),
        ("SALIX-HNE-MIB", "hneSonetProtectionConfig"),
        ("SALIX-HNE-MIB", "hneSonetProtectionRevertive"),
        ("SALIX-HNE-MIB", "hneSonetProtectionBiDirectional"),
        ("SALIX-HNE-MIB", "hneSonetPathContentType"),
        ("SALIX-HNE-MIB", "hneSonetPathOverheadLoopThroughModeEnabled"),
        ("SALIX-HNE-MIB", "hneSonetPathSpeMicMode"),
        ("SALIX-HNE-MIB", "hneSonetPathReceiveTraceMessage"),
        ("SALIX-HNE-MIB", "hneSonetPathTransmitTraceMessage"),
        ("SALIX-HNE-MIB", "hneSonetPathRowStatus"))
)
if mibBuilder.loadTexts:
    hneSonetGroup.setStatus("current")

hneTdmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1, 3)
)
hneTdmGroup.setObjects(
      *(("SALIX-HNE-MIB", "hneTdmCrossConnectRowStatus"),
        ("SALIX-HNE-MIB", "hneTdmCrossConnectOperStatus"))
)
if mibBuilder.loadTexts:
    hneTdmGroup.setStatus("current")

hneAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1, 4)
)
hneAtmGroup.setObjects(
      *(("SALIX-HNE-MIB", "hneAtmInterfaceValueAddedModeEnabled"),
        ("SALIX-HNE-MIB", "hneAtmTrafficDescrParamIndexNext"),
        ("SALIX-HNE-MIB", "hneAtmVplVamMode"))
)
if mibBuilder.loadTexts:
    hneAtmGroup.setStatus("current")

hneAtmfM4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 1, 5)
)
hneAtmfM4Group.setObjects(
    ("SALIX-HNE-MIB", "hneAtmfM4TcHecErroredCellAction")
)
if mibBuilder.loadTexts:
    hneAtmfM4Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hneCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hneCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-HNE-MIB",
    **{"HnePlugInUnitType": HnePlugInUnitType,
       "hneMIB": hneMIB,
       "hneMIBObjects": hneMIBObjects,
       "hneSystem": hneSystem,
       "hneSystemHost": hneSystemHost,
       "hneSystemSync": hneSystemSync,
       "hneSysSyncTimingMode": hneSysSyncTimingMode,
       "hneSysSyncPrimaryRefLine": hneSysSyncPrimaryRefLine,
       "hneSysSyncSecondaryRefLine": hneSysSyncSecondaryRefLine,
       "hneSysSyncRevertiveSwitch": hneSysSyncRevertiveSwitch,
       "hneSysSyncClockMode": hneSysSyncClockMode,
       "hneSysSyncConfiguredActiveRef": hneSysSyncConfiguredActiveRef,
       "hneSysSyncAutoRefSwitch": hneSysSyncAutoRefSwitch,
       "hneSysSyncFreeRunAlarm": hneSysSyncFreeRunAlarm,
       "hneSysSyncWorking": hneSysSyncWorking,
       "hneSysSyncProtect": hneSysSyncProtect,
       "hneSysSyncPrimaryRefLineState": hneSysSyncPrimaryRefLineState,
       "hneSysSyncSecondaryRefLineState": hneSysSyncSecondaryRefLineState,
       "hneSysSyncCurrentActiveRef": hneSysSyncCurrentActiveRef,
       "hneSysSyncForcedState": hneSysSyncForcedState,
       "hneSystemHsf": hneSystemHsf,
       "hneSysHsfWorking": hneSysHsfWorking,
       "hneSysHsfProtect": hneSysHsfProtect,
       "hneSonet": hneSonet,
       "hneSonetLineTable": hneSonetLineTable,
       "hneSonetLineEntry": hneSonetLineEntry,
       "hneSonetLineTimingSource": hneSonetLineTimingSource,
       "hneSonetLineDccSelection": hneSonetLineDccSelection,
       "hneSonetLineOverheadLoopThroughModeEnabled": hneSonetLineOverheadLoopThroughModeEnabled,
       "hneSonetProtectionTable": hneSonetProtectionTable,
       "hneSonetProtectionEntry": hneSonetProtectionEntry,
       "hneSonetProtectionInterfaceHigh": hneSonetProtectionInterfaceHigh,
       "hneSonetProtectionInterfaceLow": hneSonetProtectionInterfaceLow,
       "hneSonetProtectionInterfaceWorking": hneSonetProtectionInterfaceWorking,
       "hneSonetProtectionConfig": hneSonetProtectionConfig,
       "hneSonetProtectionRevertive": hneSonetProtectionRevertive,
       "hneSonetProtectionBiDirectional": hneSonetProtectionBiDirectional,
       "hneSonetPathTable": hneSonetPathTable,
       "hneSonetPathEntry": hneSonetPathEntry,
       "hneSonetPathContentType": hneSonetPathContentType,
       "hneSonetPathOverheadLoopThroughModeEnabled": hneSonetPathOverheadLoopThroughModeEnabled,
       "hneSonetPathSpeMicMode": hneSonetPathSpeMicMode,
       "hneSonetPathReceiveTraceMessage": hneSonetPathReceiveTraceMessage,
       "hneSonetPathTransmitTraceMessage": hneSonetPathTransmitTraceMessage,
       "hneSonetPathRowStatus": hneSonetPathRowStatus,
       "hneTdm": hneTdm,
       "hneTdmCrossConnectTable": hneTdmCrossConnectTable,
       "hneTdmCrossConnectEntry": hneTdmCrossConnectEntry,
       "hneTdmCrossConnectPathTerminationPoint1": hneTdmCrossConnectPathTerminationPoint1,
       "hneTdmCrossConnectPathTerminationPoint2": hneTdmCrossConnectPathTerminationPoint2,
       "hneTdmCrossConnectOperStatus": hneTdmCrossConnectOperStatus,
       "hneTdmCrossConnectRowStatus": hneTdmCrossConnectRowStatus,
       "hneAtm": hneAtm,
       "hneAtmInterfaceConfTable": hneAtmInterfaceConfTable,
       "hneAtmInterfaceConfEntry": hneAtmInterfaceConfEntry,
       "hneAtmInterfaceValueAddedModeEnabled": hneAtmInterfaceValueAddedModeEnabled,
       "hneAtmTrafficDescrParamIndexNext": hneAtmTrafficDescrParamIndexNext,
       "hneAtmVplTable": hneAtmVplTable,
       "hneAtmVplEntry": hneAtmVplEntry,
       "hneAtmVplVamMode": hneAtmVplVamMode,
       "hneAtmfM4": hneAtmfM4,
       "hneAtmfM4TcAdaptorTable": hneAtmfM4TcAdaptorTable,
       "hneAtmfM4TcAdaptorEntry": hneAtmfM4TcAdaptorEntry,
       "hneAtmfM4TcHecErroredCellAction": hneAtmfM4TcHecErroredCellAction,
       "hnePlugInUnit": hnePlugInUnit,
       "hneMIBTraps": hneMIBTraps,
       "hneMIBCompliance": hneMIBCompliance,
       "hneGroups": hneGroups,
       "hneSystemGroup": hneSystemGroup,
       "hneSonetGroup": hneSonetGroup,
       "hneTdmGroup": hneTdmGroup,
       "hneAtmGroup": hneAtmGroup,
       "hneAtmfM4Group": hneAtmfM4Group,
       "hneCompliances": hneCompliances,
       "hneCompliance": hneCompliance,
       "hneMIBStats": hneMIBStats,
       "hneSonetPathCurrentTable": hneSonetPathCurrentTable,
       "hneSonetPathCurrentEntry": hneSonetPathCurrentEntry,
       "hneSonetPathCurrentRxPosPointerJustCount": hneSonetPathCurrentRxPosPointerJustCount,
       "hneSonetPathCurrentRxNegPointerJustCount": hneSonetPathCurrentRxNegPointerJustCount,
       "hneSonetPathCurrentTxPosPointerJustCount": hneSonetPathCurrentTxPosPointerJustCount,
       "hneSonetPathCurrentTxNegPointerJustCount": hneSonetPathCurrentTxNegPointerJustCount,
       "hneSonetPathIntervalTable": hneSonetPathIntervalTable,
       "hneSonetPathIntervalEntry": hneSonetPathIntervalEntry,
       "hneSonetPathIntervalRxPosPointerJustCount": hneSonetPathIntervalRxPosPointerJustCount,
       "hneSonetPathIntervalRxNegPointerJustCount": hneSonetPathIntervalRxNegPointerJustCount,
       "hneSonetPathIntervalTxPosPointerJustCount": hneSonetPathIntervalTxPosPointerJustCount,
       "hneSonetPathIntervalTxNegPointerJustCount": hneSonetPathIntervalTxNegPointerJustCount,
       "hneAtmLiuCurrentTable": hneAtmLiuCurrentTable,
       "hneAtmLiuCurrentEntry": hneAtmLiuCurrentEntry,
       "hneAtmLiuCurrentPhysLayerCellCount": hneAtmLiuCurrentPhysLayerCellCount,
       "hneAtmLiuCurrentRxCellCount": hneAtmLiuCurrentRxCellCount,
       "hneAtmLiuCurrentTxCellCount": hneAtmLiuCurrentTxCellCount,
       "hneAtmLiuCurrentCongestionDroppedCount": hneAtmLiuCurrentCongestionDroppedCount,
       "hneAtmLiuCurrentInvalidCellCount": hneAtmLiuCurrentInvalidCellCount,
       "hneAtmLiuCurrentErroredOAMCellCount": hneAtmLiuCurrentErroredOAMCellCount,
       "hneAtmLiuCurrentValidOAMCellCount": hneAtmLiuCurrentValidOAMCellCount,
       "hneAtmLiuCurrentTxOverrunCount": hneAtmLiuCurrentTxOverrunCount,
       "hneAtmLiuCurrentMissingHeaderCellCount": hneAtmLiuCurrentMissingHeaderCellCount,
       "hneAtmLiuCurrentNonRoutableCellCount": hneAtmLiuCurrentNonRoutableCellCount,
       "hneAtmLiuCurrentVcSearchFailedCount": hneAtmLiuCurrentVcSearchFailedCount,
       "hneAtmLiuCurrentInternalParityErrorCount": hneAtmLiuCurrentInternalParityErrorCount,
       "hneAtmLiuHistoryTable": hneAtmLiuHistoryTable,
       "hneAtmLiuHistoryEntry": hneAtmLiuHistoryEntry,
       "hneAtmLiuHistoryPhysLayerCellCount": hneAtmLiuHistoryPhysLayerCellCount,
       "hneAtmLiuHistoryRxCellCount": hneAtmLiuHistoryRxCellCount,
       "hneAtmLiuHistoryTxCellCount": hneAtmLiuHistoryTxCellCount,
       "hneAtmLiuHistoryCongestionDroppedCount": hneAtmLiuHistoryCongestionDroppedCount,
       "hneAtmLiuHistoryInvalidCellCount": hneAtmLiuHistoryInvalidCellCount,
       "hneAtmLiuHistoryErroredOAMCellCount": hneAtmLiuHistoryErroredOAMCellCount,
       "hneAtmLiuHistoryValidOAMCellCount": hneAtmLiuHistoryValidOAMCellCount,
       "hneAtmLiuHistoryTxOverrunCount": hneAtmLiuHistoryTxOverrunCount,
       "hneAtmLiuHistoryMissingHeaderCellCount": hneAtmLiuHistoryMissingHeaderCellCount,
       "hneAtmLiuHistoryNonRoutableCellCount": hneAtmLiuHistoryNonRoutableCellCount,
       "hneAtmLiuHistoryVcSearchFailedCount": hneAtmLiuHistoryVcSearchFailedCount,
       "hneAtmLiuHistoryInternalParityErrorCount": hneAtmLiuHistoryInternalParityErrorCount,
       "hneVclCurrentTable": hneVclCurrentTable,
       "hneVclCurrentEntry": hneVclCurrentEntry,
       "hneVclCurrentBIP16Count": hneVclCurrentBIP16Count,
       "hneVclCurrentRxSECBCount": hneVclCurrentRxSECBCount,
       "hneVclCurrentRxLostCellCount": hneVclCurrentRxLostCellCount,
       "hneVclCurrentRxMisinsertedCellCount": hneVclCurrentRxMisinsertedCellCount,
       "hneVclCurrentRxBIPVCount": hneVclCurrentRxBIPVCount,
       "hneVclCurrentTxSECBCount": hneVclCurrentTxSECBCount,
       "hneVclCurrentTxLostCellCount": hneVclCurrentTxLostCellCount,
       "hneVclCurrentTxMisinsertedCellCount": hneVclCurrentTxMisinsertedCellCount,
       "hneVclCurrentTxBIPVCount": hneVclCurrentTxBIPVCount,
       "hneVclHistoryTable": hneVclHistoryTable,
       "hneVclHistoryEntry": hneVclHistoryEntry,
       "hneVclHistoryBIP16Count": hneVclHistoryBIP16Count,
       "hneVclHistoryRxSECBCount": hneVclHistoryRxSECBCount,
       "hneVclHistoryRxLostCellCount": hneVclHistoryRxLostCellCount,
       "hneVclHistoryRxMisinsertedCellCount": hneVclHistoryRxMisinsertedCellCount,
       "hneVclHistoryRxBIPVCount": hneVclHistoryRxBIPVCount,
       "hneVclHistoryTxSECBCount": hneVclHistoryTxSECBCount,
       "hneVclHistoryTxLostCellCount": hneVclHistoryTxLostCellCount,
       "hneVclHistoryTxMisinsertedCellCount": hneVclHistoryTxMisinsertedCellCount,
       "hneVclHistoryTxBIPVCount": hneVclHistoryTxBIPVCount,
       "hneVplCurrentTable": hneVplCurrentTable,
       "hneVplCurrentEntry": hneVplCurrentEntry,
       "hneVplCurrentBIP16Count": hneVplCurrentBIP16Count,
       "hneVplCurrentRxSECBCount": hneVplCurrentRxSECBCount,
       "hneVplCurrentRxLostCellCount": hneVplCurrentRxLostCellCount,
       "hneVplCurrentRxMisinsertedCellCount": hneVplCurrentRxMisinsertedCellCount,
       "hneVplCurrentRxBIPVCount": hneVplCurrentRxBIPVCount,
       "hneVplCurrentTxSECBCount": hneVplCurrentTxSECBCount,
       "hneVplCurrentTxLostCellCount": hneVplCurrentTxLostCellCount,
       "hneVplCurrentTxMisinsertedCellCount": hneVplCurrentTxMisinsertedCellCount,
       "hneVplCurrentTxBIPVCount": hneVplCurrentTxBIPVCount,
       "hneVplHistoryTable": hneVplHistoryTable,
       "hneVplHistoryEntry": hneVplHistoryEntry,
       "hneVplHistoryBIP16Count": hneVplHistoryBIP16Count,
       "hneVplHistoryRxSECBCount": hneVplHistoryRxSECBCount,
       "hneVplHistoryRxLostCellCount": hneVplHistoryRxLostCellCount,
       "hneVplHistoryRxMisinsertedCellCount": hneVplHistoryRxMisinsertedCellCount,
       "hneVplHistoryRxBIPVCount": hneVplHistoryRxBIPVCount,
       "hneVplHistoryTxSECBCount": hneVplHistoryTxSECBCount,
       "hneVplHistoryTxLostCellCount": hneVplHistoryTxLostCellCount,
       "hneVplHistoryTxMisinsertedCellCount": hneVplHistoryTxMisinsertedCellCount,
       "hneVplHistoryTxBIPVCount": hneVplHistoryTxBIPVCount}
)
