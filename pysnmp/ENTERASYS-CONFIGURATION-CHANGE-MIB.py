# SNMP MIB module (ENTERASYS-CONFIGURATION-CHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-CONFIGURATION-CHANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:43 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysConfigurationChangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12)
)
etsysConfigurationChangeMIB.setRevisions(
        ("2001-11-26 16:44",
         "2001-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysConfigChangeNonVolatile_ObjectIdentity = ObjectIdentity
etsysConfigChangeNonVolatile = _EtsysConfigChangeNonVolatile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1)
)
_EtsysConfigChangeNonVolatileCount_Type = Counter32
_EtsysConfigChangeNonVolatileCount_Object = MibScalar
etsysConfigChangeNonVolatileCount = _EtsysConfigChangeNonVolatileCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 1),
    _EtsysConfigChangeNonVolatileCount_Type()
)
etsysConfigChangeNonVolatileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeNonVolatileCount.setStatus("current")
_EtsysConfigChangeNonVolatileTime_Type = DateAndTime
_EtsysConfigChangeNonVolatileTime_Object = MibScalar
etsysConfigChangeNonVolatileTime = _EtsysConfigChangeNonVolatileTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 2),
    _EtsysConfigChangeNonVolatileTime_Type()
)
etsysConfigChangeNonVolatileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeNonVolatileTime.setStatus("current")


class _EtsysConfigChangeNonVolatileMethod_Type(SnmpAdminString):
    """Custom type etsysConfigChangeNonVolatileMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysConfigChangeNonVolatileMethod_Type.__name__ = "SnmpAdminString"
_EtsysConfigChangeNonVolatileMethod_Object = MibScalar
etsysConfigChangeNonVolatileMethod = _EtsysConfigChangeNonVolatileMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 3),
    _EtsysConfigChangeNonVolatileMethod_Type()
)
etsysConfigChangeNonVolatileMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeNonVolatileMethod.setStatus("current")
_EtsysConfigChangeVolatile_ObjectIdentity = ObjectIdentity
etsysConfigChangeVolatile = _EtsysConfigChangeVolatile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2)
)
_EtsysConfigChangeVolatileCount_Type = Counter32
_EtsysConfigChangeVolatileCount_Object = MibScalar
etsysConfigChangeVolatileCount = _EtsysConfigChangeVolatileCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 1),
    _EtsysConfigChangeVolatileCount_Type()
)
etsysConfigChangeVolatileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeVolatileCount.setStatus("current")
_EtsysConfigChangeVolatileTime_Type = DateAndTime
_EtsysConfigChangeVolatileTime_Object = MibScalar
etsysConfigChangeVolatileTime = _EtsysConfigChangeVolatileTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 2),
    _EtsysConfigChangeVolatileTime_Type()
)
etsysConfigChangeVolatileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeVolatileTime.setStatus("current")


class _EtsysConfigChangeVolatileMethod_Type(SnmpAdminString):
    """Custom type etsysConfigChangeVolatileMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysConfigChangeVolatileMethod_Type.__name__ = "SnmpAdminString"
_EtsysConfigChangeVolatileMethod_Object = MibScalar
etsysConfigChangeVolatileMethod = _EtsysConfigChangeVolatileMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 3),
    _EtsysConfigChangeVolatileMethod_Type()
)
etsysConfigChangeVolatileMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeVolatileMethod.setStatus("current")
_EtsysConfigChangeFirmware_ObjectIdentity = ObjectIdentity
etsysConfigChangeFirmware = _EtsysConfigChangeFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3)
)
_EtsysConfigChangeFirmwareCount_Type = Counter32
_EtsysConfigChangeFirmwareCount_Object = MibScalar
etsysConfigChangeFirmwareCount = _EtsysConfigChangeFirmwareCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 1),
    _EtsysConfigChangeFirmwareCount_Type()
)
etsysConfigChangeFirmwareCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeFirmwareCount.setStatus("current")
_EtsysConfigChangeFirmwareTime_Type = DateAndTime
_EtsysConfigChangeFirmwareTime_Object = MibScalar
etsysConfigChangeFirmwareTime = _EtsysConfigChangeFirmwareTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 2),
    _EtsysConfigChangeFirmwareTime_Type()
)
etsysConfigChangeFirmwareTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeFirmwareTime.setStatus("current")


class _EtsysConfigChangeFirmwareMethod_Type(SnmpAdminString):
    """Custom type etsysConfigChangeFirmwareMethod based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysConfigChangeFirmwareMethod_Type.__name__ = "SnmpAdminString"
_EtsysConfigChangeFirmwareMethod_Object = MibScalar
etsysConfigChangeFirmwareMethod = _EtsysConfigChangeFirmwareMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 3),
    _EtsysConfigChangeFirmwareMethod_Type()
)
etsysConfigChangeFirmwareMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysConfigChangeFirmwareMethod.setStatus("current")
_EtsysConfigChangeConformance_ObjectIdentity = ObjectIdentity
etsysConfigChangeConformance = _EtsysConfigChangeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4)
)
_EtsysConfigChangeGroups_ObjectIdentity = ObjectIdentity
etsysConfigChangeGroups = _EtsysConfigChangeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1)
)
_EtsysConfigChangeCompliances_ObjectIdentity = ObjectIdentity
etsysConfigChangeCompliances = _EtsysConfigChangeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 2)
)

# Managed Objects groups

etsysConfigChangeNonVolatileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 1)
)
etsysConfigChangeNonVolatileGroup.setObjects(
      *(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileCount"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileTime"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileMethod"))
)
if mibBuilder.loadTexts:
    etsysConfigChangeNonVolatileGroup.setStatus("current")

etsysConfigChangeVolatileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 2)
)
etsysConfigChangeVolatileGroup.setObjects(
      *(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileCount"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileTime"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileMethod"))
)
if mibBuilder.loadTexts:
    etsysConfigChangeVolatileGroup.setStatus("current")

etsysConfigChangeFirmwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 3)
)
etsysConfigChangeFirmwareGroup.setObjects(
      *(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareCount"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareTime"),
        ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareMethod"))
)
if mibBuilder.loadTexts:
    etsysConfigChangeFirmwareGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysConfigChangeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    etsysConfigChangeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-CONFIGURATION-CHANGE-MIB",
    **{"etsysConfigurationChangeMIB": etsysConfigurationChangeMIB,
       "etsysConfigChangeNonVolatile": etsysConfigChangeNonVolatile,
       "etsysConfigChangeNonVolatileCount": etsysConfigChangeNonVolatileCount,
       "etsysConfigChangeNonVolatileTime": etsysConfigChangeNonVolatileTime,
       "etsysConfigChangeNonVolatileMethod": etsysConfigChangeNonVolatileMethod,
       "etsysConfigChangeVolatile": etsysConfigChangeVolatile,
       "etsysConfigChangeVolatileCount": etsysConfigChangeVolatileCount,
       "etsysConfigChangeVolatileTime": etsysConfigChangeVolatileTime,
       "etsysConfigChangeVolatileMethod": etsysConfigChangeVolatileMethod,
       "etsysConfigChangeFirmware": etsysConfigChangeFirmware,
       "etsysConfigChangeFirmwareCount": etsysConfigChangeFirmwareCount,
       "etsysConfigChangeFirmwareTime": etsysConfigChangeFirmwareTime,
       "etsysConfigChangeFirmwareMethod": etsysConfigChangeFirmwareMethod,
       "etsysConfigChangeConformance": etsysConfigChangeConformance,
       "etsysConfigChangeGroups": etsysConfigChangeGroups,
       "etsysConfigChangeNonVolatileGroup": etsysConfigChangeNonVolatileGroup,
       "etsysConfigChangeVolatileGroup": etsysConfigChangeVolatileGroup,
       "etsysConfigChangeFirmwareGroup": etsysConfigChangeFirmwareGroup,
       "etsysConfigChangeCompliances": etsysConfigChangeCompliances,
       "etsysConfigChangeCompliance": etsysConfigChangeCompliance}
)
