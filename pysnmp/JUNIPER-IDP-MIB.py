# SNMP MIB module (JUNIPER-IDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:05 2024
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

(jnxMibs,
 jnxTraps) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxTraps")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxIdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIdpSensor_ObjectIdentity = ObjectIdentity
jnxIdpSensor = _JnxIdpSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1)
)


class _JnxIdpSensorCpuUsage_Type(Gauge32):
    """Custom type jnxIdpSensorCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorCpuUsage_Type.__name__ = "Gauge32"
_JnxIdpSensorCpuUsage_Object = MibScalar
jnxIdpSensorCpuUsage = _JnxIdpSensorCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 1),
    _JnxIdpSensorCpuUsage_Type()
)
jnxIdpSensorCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorCpuUsage.setStatus("current")


class _JnxIdpSensorMemUsage_Type(Gauge32):
    """Custom type jnxIdpSensorMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorMemUsage_Type.__name__ = "Gauge32"
_JnxIdpSensorMemUsage_Object = MibScalar
jnxIdpSensorMemUsage = _JnxIdpSensorMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 2),
    _JnxIdpSensorMemUsage_Type()
)
jnxIdpSensorMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorMemUsage.setStatus("mandatory")
_JnxIdpSensorSessAllocated_Type = Gauge32
_JnxIdpSensorSessAllocated_Object = MibScalar
jnxIdpSensorSessAllocated = _JnxIdpSensorSessAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 3),
    _JnxIdpSensorSessAllocated_Type()
)
jnxIdpSensorSessAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorSessAllocated.setStatus("mandatory")
_JnxIdpSensorSessMaximum_Type = Integer32
_JnxIdpSensorSessMaximum_Object = MibScalar
jnxIdpSensorSessMaximum = _JnxIdpSensorSessMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 4),
    _JnxIdpSensorSessMaximum_Type()
)
jnxIdpSensorSessMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorSessMaximum.setStatus("mandatory")
_JnxIdpSensorFreeDiskSpace_Type = Gauge32
_JnxIdpSensorFreeDiskSpace_Object = MibScalar
jnxIdpSensorFreeDiskSpace = _JnxIdpSensorFreeDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 5),
    _JnxIdpSensorFreeDiskSpace_Type()
)
jnxIdpSensorFreeDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorFreeDiskSpace.setStatus("mandatory")
if mibBuilder.loadTexts:
    jnxIdpSensorFreeDiskSpace.setUnits("Megabytes")


class _JnxIdpSensorCpuThreshold_Type(Integer32):
    """Custom type jnxIdpSensorCpuThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorCpuThreshold_Type.__name__ = "Integer32"
_JnxIdpSensorCpuThreshold_Object = MibScalar
jnxIdpSensorCpuThreshold = _JnxIdpSensorCpuThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 6),
    _JnxIdpSensorCpuThreshold_Type()
)
jnxIdpSensorCpuThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorCpuThreshold.setStatus("current")


class _JnxIdpSensorMemThreshold_Type(Integer32):
    """Custom type jnxIdpSensorMemThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorMemThreshold_Type.__name__ = "Integer32"
_JnxIdpSensorMemThreshold_Object = MibScalar
jnxIdpSensorMemThreshold = _JnxIdpSensorMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 7),
    _JnxIdpSensorMemThreshold_Type()
)
jnxIdpSensorMemThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorMemThreshold.setStatus("mandatory")


class _JnxIdpSensorSessThreshold_Type(Integer32):
    """Custom type jnxIdpSensorSessThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorSessThreshold_Type.__name__ = "Integer32"
_JnxIdpSensorSessThreshold_Object = MibScalar
jnxIdpSensorSessThreshold = _JnxIdpSensorSessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 8),
    _JnxIdpSensorSessThreshold_Type()
)
jnxIdpSensorSessThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorSessThreshold.setStatus("mandatory")


class _JnxIdpSensorDiskSpaceThreshold_Type(Integer32):
    """Custom type jnxIdpSensorDiskSpaceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxIdpSensorDiskSpaceThreshold_Type.__name__ = "Integer32"
_JnxIdpSensorDiskSpaceThreshold_Object = MibScalar
jnxIdpSensorDiskSpaceThreshold = _JnxIdpSensorDiskSpaceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 9, 1, 9),
    _JnxIdpSensorDiskSpaceThreshold_Type()
)
jnxIdpSensorDiskSpaceThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIdpSensorDiskSpaceThreshold.setStatus("mandatory")
_JnxIdpTrap_ObjectIdentity = ObjectIdentity
jnxIdpTrap = _JnxIdpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12)
)
_JnxIdpTrapsPrefix_ObjectIdentity = ObjectIdentity
jnxIdpTrapsPrefix = _JnxIdpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0)
)

# Managed Objects groups


# Notification objects

jnxIdpSessionCountNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 1)
)
jnxIdpSessionCountNotify.setObjects(
      *(("JUNIPER-IDP-MIB", "jnxIdpSensorSessAllocated"),
        ("JUNIPER-IDP-MIB", "jnxIdpSensorSessThreshold"))
)
if mibBuilder.loadTexts:
    jnxIdpSessionCountNotify.setStatus(
        "current"
    )

jnxIdpSessionCountLimitRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 2)
)
jnxIdpSessionCountLimitRestored.setObjects(
    ("JUNIPER-IDP-MIB", "jnxIdpSensorSessAllocated")
)
if mibBuilder.loadTexts:
    jnxIdpSessionCountLimitRestored.setStatus(
        "current"
    )

jnxIdpCPUUtilizationNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 3)
)
jnxIdpCPUUtilizationNotify.setObjects(
      *(("JUNIPER-IDP-MIB", "jnxIdpSensorCpuUsage"),
        ("JUNIPER-IDP-MIB", "jnxIdpSensorCpuThreshold"))
)
if mibBuilder.loadTexts:
    jnxIdpCPUUtilizationNotify.setStatus(
        "current"
    )

jnxIdpCPUUtilizationLimitRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 4)
)
jnxIdpCPUUtilizationLimitRestored.setObjects(
    ("JUNIPER-IDP-MIB", "jnxIdpSensorCpuUsage")
)
if mibBuilder.loadTexts:
    jnxIdpCPUUtilizationLimitRestored.setStatus(
        "current"
    )

jnxIdpMemoryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 5)
)
jnxIdpMemoryNotify.setObjects(
      *(("JUNIPER-IDP-MIB", "jnxIdpSensorMemUsage"),
        ("JUNIPER-IDP-MIB", "jnxIdpSensorMemThreshold"))
)
if mibBuilder.loadTexts:
    jnxIdpMemoryNotify.setStatus(
        "current"
    )

jnxIdpMemoryLimitRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 6)
)
jnxIdpMemoryLimitRestored.setObjects(
    ("JUNIPER-IDP-MIB", "jnxIdpSensorMemUsage")
)
if mibBuilder.loadTexts:
    jnxIdpMemoryLimitRestored.setStatus(
        "current"
    )

jnxIdpDiskUtilizationNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 7)
)
jnxIdpDiskUtilizationNotify.setObjects(
      *(("JUNIPER-IDP-MIB", "jnxIdpSensorFreeDiskSpace"),
        ("JUNIPER-IDP-MIB", "jnxIdpSensorDiskSpaceThreshold"))
)
if mibBuilder.loadTexts:
    jnxIdpDiskUtilizationNotify.setStatus(
        "current"
    )

jnxIdpDiskUtilizationLimitRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 8)
)
jnxIdpDiskUtilizationLimitRestored.setObjects(
    ("JUNIPER-IDP-MIB", "jnxIdpSensorFreeDiskSpace")
)
if mibBuilder.loadTexts:
    jnxIdpDiskUtilizationLimitRestored.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IDP-MIB",
    **{"jnxIdpMIB": jnxIdpMIB,
       "jnxIdpSensor": jnxIdpSensor,
       "jnxIdpSensorCpuUsage": jnxIdpSensorCpuUsage,
       "jnxIdpSensorMemUsage": jnxIdpSensorMemUsage,
       "jnxIdpSensorSessAllocated": jnxIdpSensorSessAllocated,
       "jnxIdpSensorSessMaximum": jnxIdpSensorSessMaximum,
       "jnxIdpSensorFreeDiskSpace": jnxIdpSensorFreeDiskSpace,
       "jnxIdpSensorCpuThreshold": jnxIdpSensorCpuThreshold,
       "jnxIdpSensorMemThreshold": jnxIdpSensorMemThreshold,
       "jnxIdpSensorSessThreshold": jnxIdpSensorSessThreshold,
       "jnxIdpSensorDiskSpaceThreshold": jnxIdpSensorDiskSpaceThreshold,
       "jnxIdpTrap": jnxIdpTrap,
       "jnxIdpTrapsPrefix": jnxIdpTrapsPrefix,
       "jnxIdpSessionCountNotify": jnxIdpSessionCountNotify,
       "jnxIdpSessionCountLimitRestored": jnxIdpSessionCountLimitRestored,
       "jnxIdpCPUUtilizationNotify": jnxIdpCPUUtilizationNotify,
       "jnxIdpCPUUtilizationLimitRestored": jnxIdpCPUUtilizationLimitRestored,
       "jnxIdpMemoryNotify": jnxIdpMemoryNotify,
       "jnxIdpMemoryLimitRestored": jnxIdpMemoryLimitRestored,
       "jnxIdpDiskUtilizationNotify": jnxIdpDiskUtilizationNotify,
       "jnxIdpDiskUtilizationLimitRestored": jnxIdpDiskUtilizationLimitRestored}
)
