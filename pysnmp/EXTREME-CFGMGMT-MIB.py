# SNMP MIB module (EXTREME-CFGMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-CFGMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:25 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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


# MODULE-IDENTITY

extremeCfgMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeCfgMgmtCommon_ObjectIdentity = ObjectIdentity
extremeCfgMgmtCommon = _ExtremeCfgMgmtCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1)
)
_ExtremeLastSaveCfgTable_Object = MibTable
extremeLastSaveCfgTable = _ExtremeLastSaveCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    extremeLastSaveCfgTable.setStatus("current")
_ExtremeLastSavedEntry_Object = MibTableRow
extremeLastSavedEntry = _ExtremeLastSavedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1, 1)
)
extremeLastSavedEntry.setIndexNames(
    (0, "EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigSlotId"),
)
if mibBuilder.loadTexts:
    extremeLastSavedEntry.setStatus("current")


class _ExtremeLastSaveConfigSlotId_Type(Integer32):
    """Custom type extremeLastSaveConfigSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeLastSaveConfigSlotId_Type.__name__ = "Integer32"
_ExtremeLastSaveConfigSlotId_Object = MibTableColumn
extremeLastSaveConfigSlotId = _ExtremeLastSaveConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1, 1, 1),
    _ExtremeLastSaveConfigSlotId_Type()
)
extremeLastSaveConfigSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastSaveConfigSlotId.setStatus("current")


class _ExtremeLastSaveConfigTime_Type(DisplayString):
    """Custom type extremeLastSaveConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeLastSaveConfigTime_Type.__name__ = "DisplayString"
_ExtremeLastSaveConfigTime_Object = MibTableColumn
extremeLastSaveConfigTime = _ExtremeLastSaveConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1, 1, 2),
    _ExtremeLastSaveConfigTime_Type()
)
extremeLastSaveConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastSaveConfigTime.setStatus("current")


class _ExtremeLastSaveConfigFileName_Type(DisplayString):
    """Custom type extremeLastSaveConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ExtremeLastSaveConfigFileName_Type.__name__ = "DisplayString"
_ExtremeLastSaveConfigFileName_Object = MibTableColumn
extremeLastSaveConfigFileName = _ExtremeLastSaveConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1, 1, 3),
    _ExtremeLastSaveConfigFileName_Type()
)
extremeLastSaveConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastSaveConfigFileName.setStatus("current")


class _ExtremeLastSaveConfigSource_Type(Integer32):
    """Custom type extremeLastSaveConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteDevice", 2),
          ("snmp", 1))
    )


_ExtremeLastSaveConfigSource_Type.__name__ = "Integer32"
_ExtremeLastSaveConfigSource_Object = MibTableColumn
extremeLastSaveConfigSource = _ExtremeLastSaveConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 1, 1, 4),
    _ExtremeLastSaveConfigSource_Type()
)
extremeLastSaveConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastSaveConfigSource.setStatus("current")
_ExtremeLastChangeCfgTable_Object = MibTable
extremeLastChangeCfgTable = _ExtremeLastChangeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2)
)
if mibBuilder.loadTexts:
    extremeLastChangeCfgTable.setStatus("current")
_ExtremeLastChangeCfgEntry_Object = MibTableRow
extremeLastChangeCfgEntry = _ExtremeLastChangeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2, 1)
)
extremeLastChangeCfgEntry.setIndexNames(
    (0, "EXTREME-CFGMGMT-MIB", "extremeLastChangeCfgSlotId"),
)
if mibBuilder.loadTexts:
    extremeLastChangeCfgEntry.setStatus("current")


class _ExtremeLastChangeCfgSlotId_Type(Integer32):
    """Custom type extremeLastChangeCfgSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeLastChangeCfgSlotId_Type.__name__ = "Integer32"
_ExtremeLastChangeCfgSlotId_Object = MibTableColumn
extremeLastChangeCfgSlotId = _ExtremeLastChangeCfgSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2, 1, 1),
    _ExtremeLastChangeCfgSlotId_Type()
)
extremeLastChangeCfgSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastChangeCfgSlotId.setStatus("current")


class _ExtremeLastChangeConfigTime_Type(DisplayString):
    """Custom type extremeLastChangeConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeLastChangeConfigTime_Type.__name__ = "DisplayString"
_ExtremeLastChangeConfigTime_Object = MibTableColumn
extremeLastChangeConfigTime = _ExtremeLastChangeConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2, 1, 2),
    _ExtremeLastChangeConfigTime_Type()
)
extremeLastChangeConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastChangeConfigTime.setStatus("current")


class _ExtremeLastChangeConfigFileName_Type(DisplayString):
    """Custom type extremeLastChangeConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ExtremeLastChangeConfigFileName_Type.__name__ = "DisplayString"
_ExtremeLastChangeConfigFileName_Object = MibTableColumn
extremeLastChangeConfigFileName = _ExtremeLastChangeConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2, 1, 3),
    _ExtremeLastChangeConfigFileName_Type()
)
extremeLastChangeConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastChangeConfigFileName.setStatus("current")


class _ExtremeLastChangeConfigSource_Type(Integer32):
    """Custom type extremeLastChangeConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteDevice", 2),
          ("snmp", 1))
    )


_ExtremeLastChangeConfigSource_Type.__name__ = "Integer32"
_ExtremeLastChangeConfigSource_Object = MibTableColumn
extremeLastChangeConfigSource = _ExtremeLastChangeConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 1, 2, 1, 4),
    _ExtremeLastChangeConfigSource_Type()
)
extremeLastChangeConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLastChangeConfigSource.setStatus("current")
_ExtremeCfgGroups_ObjectIdentity = ObjectIdentity
extremeCfgGroups = _ExtremeCfgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 9)
)
_ExtremeCfgMgmtTrapPrefix_ObjectIdentity = ObjectIdentity
extremeCfgMgmtTrapPrefix = _ExtremeCfgMgmtTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 10)
)
_CfgMgmtTraps_ObjectIdentity = ObjectIdentity
cfgMgmtTraps = _CfgMgmtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 10, 0)
)
_CfgMgmtControl_ObjectIdentity = ObjectIdentity
cfgMgmtControl = _CfgMgmtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 11)
)


class _CfgMgmtConfigSaveTrapEnable_Type(TruthValue):
    """Custom type cfgMgmtConfigSaveTrapEnable based on TruthValue"""


_CfgMgmtConfigSaveTrapEnable_Object = MibScalar
cfgMgmtConfigSaveTrapEnable = _CfgMgmtConfigSaveTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 11, 1),
    _CfgMgmtConfigSaveTrapEnable_Type()
)
cfgMgmtConfigSaveTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMgmtConfigSaveTrapEnable.setStatus("current")


class _CfgMgmtConfigChangeTrapEnable_Type(TruthValue):
    """Custom type cfgMgmtConfigChangeTrapEnable based on TruthValue"""


_CfgMgmtConfigChangeTrapEnable_Object = MibScalar
cfgMgmtConfigChangeTrapEnable = _CfgMgmtConfigChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 11, 2),
    _CfgMgmtConfigChangeTrapEnable_Type()
)
cfgMgmtConfigChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMgmtConfigChangeTrapEnable.setStatus("current")

# Managed Objects groups

extremeRunningLastSavedCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 9, 1)
)
extremeRunningLastSavedCfgGroup.setObjects(
      *(("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigTime"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigFileName"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigSource"))
)
if mibBuilder.loadTexts:
    extremeRunningLastSavedCfgGroup.setStatus("current")

extremeRunningLastChangeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 9, 2)
)
extremeRunningLastChangeCfgGroup.setObjects(
      *(("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigTime"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigFileName"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigSource"))
)
if mibBuilder.loadTexts:
    extremeRunningLastChangeCfgGroup.setStatus("current")


# Notification objects

cfgMgmtConfigSaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 10, 0, 1)
)
cfgMgmtConfigSaveTrap.setObjects(
      *(("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigTime"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigFileName"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastSaveConfigSource"))
)
if mibBuilder.loadTexts:
    cfgMgmtConfigSaveTrap.setStatus(
        "current"
    )

cfgMgmtConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42, 10, 0, 2)
)
cfgMgmtConfigChangeTrap.setObjects(
      *(("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigTime"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigFileName"),
        ("EXTREME-CFGMGMT-MIB", "extremeLastChangeConfigSource"))
)
if mibBuilder.loadTexts:
    cfgMgmtConfigChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-CFGMGMT-MIB",
    **{"extremeCfgMgmt": extremeCfgMgmt,
       "extremeCfgMgmtCommon": extremeCfgMgmtCommon,
       "extremeLastSaveCfgTable": extremeLastSaveCfgTable,
       "extremeLastSavedEntry": extremeLastSavedEntry,
       "extremeLastSaveConfigSlotId": extremeLastSaveConfigSlotId,
       "extremeLastSaveConfigTime": extremeLastSaveConfigTime,
       "extremeLastSaveConfigFileName": extremeLastSaveConfigFileName,
       "extremeLastSaveConfigSource": extremeLastSaveConfigSource,
       "extremeLastChangeCfgTable": extremeLastChangeCfgTable,
       "extremeLastChangeCfgEntry": extremeLastChangeCfgEntry,
       "extremeLastChangeCfgSlotId": extremeLastChangeCfgSlotId,
       "extremeLastChangeConfigTime": extremeLastChangeConfigTime,
       "extremeLastChangeConfigFileName": extremeLastChangeConfigFileName,
       "extremeLastChangeConfigSource": extremeLastChangeConfigSource,
       "extremeCfgGroups": extremeCfgGroups,
       "extremeRunningLastSavedCfgGroup": extremeRunningLastSavedCfgGroup,
       "extremeRunningLastChangeCfgGroup": extremeRunningLastChangeCfgGroup,
       "extremeCfgMgmtTrapPrefix": extremeCfgMgmtTrapPrefix,
       "cfgMgmtTraps": cfgMgmtTraps,
       "cfgMgmtConfigSaveTrap": cfgMgmtConfigSaveTrap,
       "cfgMgmtConfigChangeTrap": cfgMgmtConfigChangeTrap,
       "cfgMgmtControl": cfgMgmtControl,
       "cfgMgmtConfigSaveTrapEnable": cfgMgmtConfigSaveTrapEnable,
       "cfgMgmtConfigChangeTrapEnable": cfgMgmtConfigChangeTrapEnable}
)
