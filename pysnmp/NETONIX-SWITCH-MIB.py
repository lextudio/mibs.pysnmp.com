# SNMP MIB module (NETONIX-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETONIX-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:38 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpMIBGroups,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpMIBGroups")

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

netonixSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46242)
)
netonixSwitch.setRevisions(
        ("1998-03-23 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VoltageTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class PowerTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class CurrentTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs



class _FirmwareVersion_Type(DisplayString):
    """Custom type firmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FirmwareVersion_Type.__name__ = "DisplayString"
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 46242, 1),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 46242, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 46242, 2, 1)
)
fanEntry.setIndexNames(
    (0, "NETONIX-SWITCH-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 46242, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanSpeed_Type(Integer32):
    """Custom type fanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FanSpeed_Type.__name__ = "Integer32"
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 46242, 2, 1, 2),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 46242, 3)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 46242, 3, 1)
)
tempEntry.setIndexNames(
    (0, "NETONIX-SWITCH-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 46242, 3, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")


class _TempDescription_Type(DisplayString):
    """Custom type tempDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempDescription_Type.__name__ = "DisplayString"
_TempDescription_Object = MibTableColumn
tempDescription = _TempDescription_Object(
    (1, 3, 6, 1, 4, 1, 46242, 3, 1, 2),
    _TempDescription_Type()
)
tempDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescription.setStatus("current")


class _Temp_Type(Integer32):
    """Custom type temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Temp_Type.__name__ = "Integer32"
_Temp_Object = MibTableColumn
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 46242, 3, 1, 3),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 46242, 4)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 46242, 4, 1)
)
voltageEntry.setIndexNames(
    (0, "NETONIX-SWITCH-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")


class _VoltageIndex_Type(Integer32):
    """Custom type voltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VoltageIndex_Type.__name__ = "Integer32"
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 46242, 4, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")


class _VoltageDescription_Type(DisplayString):
    """Custom type voltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageDescription_Type.__name__ = "DisplayString"
_VoltageDescription_Object = MibTableColumn
voltageDescription = _VoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 46242, 4, 1, 2),
    _VoltageDescription_Type()
)
voltageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescription.setStatus("current")
_Voltage_Type = VoltageTC
_Voltage_Object = MibTableColumn
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 46242, 4, 1, 3),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("current")
_PoeStatusTable_Object = MibTable
poeStatusTable = _PoeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 46242, 5)
)
if mibBuilder.loadTexts:
    poeStatusTable.setStatus("current")
_PoeStatusEntry_Object = MibTableRow
poeStatusEntry = _PoeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 46242, 5, 1)
)
poeStatusEntry.setIndexNames(
    (0, "NETONIX-SWITCH-MIB", "poeStatusIndex"),
)
if mibBuilder.loadTexts:
    poeStatusEntry.setStatus("current")


class _PoeStatusIndex_Type(Integer32):
    """Custom type poeStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoeStatusIndex_Type.__name__ = "Integer32"
_PoeStatusIndex_Object = MibTableColumn
poeStatusIndex = _PoeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 46242, 5, 1, 1),
    _PoeStatusIndex_Type()
)
poeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poeStatusIndex.setStatus("current")


class _PoeStatus_Type(DisplayString):
    """Custom type poeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoeStatus_Type.__name__ = "DisplayString"
_PoeStatus_Object = MibTableColumn
poeStatus = _PoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 46242, 5, 1, 2),
    _PoeStatus_Type()
)
poeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeStatus.setStatus("current")
_TotalPowerConsumption_Type = PowerTC
_TotalPowerConsumption_Object = MibScalar
totalPowerConsumption = _TotalPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 46242, 6),
    _TotalPowerConsumption_Type()
)
totalPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPowerConsumption.setStatus("current")
_DcdcInputCurrent_Type = CurrentTC
_DcdcInputCurrent_Object = MibScalar
dcdcInputCurrent = _DcdcInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 46242, 7),
    _DcdcInputCurrent_Type()
)
dcdcInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcInputCurrent.setStatus("current")
_DcdcEfficiency_Type = Integer32
_DcdcEfficiency_Object = MibScalar
dcdcEfficiency = _DcdcEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 46242, 8),
    _DcdcEfficiency_Type()
)
dcdcEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEfficiency.setStatus("current")
_NetonixSwitchConformance_ObjectIdentity = ObjectIdentity
netonixSwitchConformance = _NetonixSwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46242, 99)
)
_NetonixSwitchGroups_ObjectIdentity = ObjectIdentity
netonixSwitchGroups = _NetonixSwitchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46242, 99, 1)
)
_NetonixSwitchCompliances_ObjectIdentity = ObjectIdentity
netonixSwitchCompliances = _NetonixSwitchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46242, 99, 2)
)

# Managed Objects groups

netonixSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 1, 2, 2, 8)
)
netonixSwitchGroup.setObjects(
      *(("NETONIX-SWITCH-MIB", "firmwareVersion"),
        ("NETONIX-SWITCH-MIB", "fanSpeed"),
        ("NETONIX-SWITCH-MIB", "tempDescription"),
        ("NETONIX-SWITCH-MIB", "temp"),
        ("NETONIX-SWITCH-MIB", "voltageDescription"),
        ("NETONIX-SWITCH-MIB", "voltage"),
        ("NETONIX-SWITCH-MIB", "poeStatus"),
        ("NETONIX-SWITCH-MIB", "totalPowerConsumption"),
        ("NETONIX-SWITCH-MIB", "dcdcInputCurrent"),
        ("NETONIX-SWITCH-MIB", "dcdcEfficiency"))
)
if mibBuilder.loadTexts:
    netonixSwitchGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

netonixSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46242, 99, 2, 1)
)
if mibBuilder.loadTexts:
    netonixSwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETONIX-SWITCH-MIB",
    **{"VoltageTC": VoltageTC,
       "PowerTC": PowerTC,
       "CurrentTC": CurrentTC,
       "netonixSwitch": netonixSwitch,
       "firmwareVersion": firmwareVersion,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanSpeed": fanSpeed,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempDescription": tempDescription,
       "temp": temp,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageDescription": voltageDescription,
       "voltage": voltage,
       "poeStatusTable": poeStatusTable,
       "poeStatusEntry": poeStatusEntry,
       "poeStatusIndex": poeStatusIndex,
       "poeStatus": poeStatus,
       "totalPowerConsumption": totalPowerConsumption,
       "dcdcInputCurrent": dcdcInputCurrent,
       "dcdcEfficiency": dcdcEfficiency,
       "netonixSwitchConformance": netonixSwitchConformance,
       "netonixSwitchGroups": netonixSwitchGroups,
       "netonixSwitchCompliances": netonixSwitchCompliances,
       "netonixSwitchCompliance": netonixSwitchCompliance,
       "netonixSwitchGroup": netonixSwitchGroup}
)
