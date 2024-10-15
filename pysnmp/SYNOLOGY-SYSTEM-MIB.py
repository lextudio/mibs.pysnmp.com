# SNMP MIB module (SYNOLOGY-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOLOGY-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:00 2024
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

synoSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1)
)
synoSystem.setRevisions(
        ("2013-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)


class _SystemStatus_Type(Integer32):
    """Custom type systemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SystemStatus_Type.__name__ = "Integer32"
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_Temperature_Type = Integer32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 2),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibScalar
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 3),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("current")
_Fan_ObjectIdentity = ObjectIdentity
fan = _Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1, 4)
)


class _SystemFanStatus_Type(Integer32):
    """Custom type systemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SystemFanStatus_Type.__name__ = "Integer32"
_SystemFanStatus_Object = MibScalar
systemFanStatus = _SystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 4, 1),
    _SystemFanStatus_Type()
)
systemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanStatus.setStatus("current")


class _CpuFanStatus_Type(Integer32):
    """Custom type cpuFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CpuFanStatus_Type.__name__ = "Integer32"
_CpuFanStatus_Object = MibScalar
cpuFanStatus = _CpuFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 4, 2),
    _CpuFanStatus_Type()
)
cpuFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFanStatus.setStatus("current")
_DsmInfo_ObjectIdentity = ObjectIdentity
dsmInfo = _DsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1, 5)
)
_ModelName_Type = OctetString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 5, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 5, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Version_Type = OctetString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 5, 3),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")


class _UpgradeAvailable_Type(Integer32):
    """Custom type upgradeAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_UpgradeAvailable_Type.__name__ = "Integer32"
_UpgradeAvailable_Object = MibScalar
upgradeAvailable = _UpgradeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 1, 5, 4),
    _UpgradeAvailable_Type()
)
upgradeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeAvailable.setStatus("current")
_SystemConformance_ObjectIdentity = ObjectIdentity
systemConformance = _SystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1, 6)
)
_SystemCompliances_ObjectIdentity = ObjectIdentity
systemCompliances = _SystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1, 6, 1)
)
_SystemGroups_ObjectIdentity = ObjectIdentity
systemGroups = _SystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 1, 6, 2)
)

# Managed Objects groups

systemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 1, 6, 2, 1)
)
systemGroup.setObjects(
      *(("SYNOLOGY-SYSTEM-MIB", "systemStatus"),
        ("SYNOLOGY-SYSTEM-MIB", "temperature"),
        ("SYNOLOGY-SYSTEM-MIB", "powerStatus"),
        ("SYNOLOGY-SYSTEM-MIB", "systemFanStatus"),
        ("SYNOLOGY-SYSTEM-MIB", "cpuFanStatus"),
        ("SYNOLOGY-SYSTEM-MIB", "modelName"),
        ("SYNOLOGY-SYSTEM-MIB", "serialNumber"),
        ("SYNOLOGY-SYSTEM-MIB", "version"),
        ("SYNOLOGY-SYSTEM-MIB", "upgradeAvailable"))
)
if mibBuilder.loadTexts:
    systemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

systemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    systemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-SYSTEM-MIB",
    **{"synology": synology,
       "synoSystem": synoSystem,
       "systemStatus": systemStatus,
       "temperature": temperature,
       "powerStatus": powerStatus,
       "fan": fan,
       "systemFanStatus": systemFanStatus,
       "cpuFanStatus": cpuFanStatus,
       "dsmInfo": dsmInfo,
       "modelName": modelName,
       "serialNumber": serialNumber,
       "version": version,
       "upgradeAvailable": upgradeAvailable,
       "systemConformance": systemConformance,
       "systemCompliances": systemCompliances,
       "systemCompliance": systemCompliance,
       "systemGroups": systemGroups,
       "systemGroup": systemGroup}
)
