# SNMP MIB module (ENTERASYS-RIPv2-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RIPv2-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:29 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysRip2ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66)
)
etsysRip2ExtMIB.setRevisions(
        ("2009-02-06 17:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRip2ExtObjects_ObjectIdentity = ObjectIdentity
etsysRip2ExtObjects = _EtsysRip2ExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1)
)
_EtsysRip2ExtGlobals_ObjectIdentity = ObjectIdentity
etsysRip2ExtGlobals = _EtsysRip2ExtGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1)
)


class _EtsysRip2ExtAdminStatus_Type(Integer32):
    """Custom type etsysRip2ExtAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )


_EtsysRip2ExtAdminStatus_Type.__name__ = "Integer32"
_EtsysRip2ExtAdminStatus_Object = MibScalar
etsysRip2ExtAdminStatus = _EtsysRip2ExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 1),
    _EtsysRip2ExtAdminStatus_Type()
)
etsysRip2ExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtAdminStatus.setStatus("current")


class _EtsysRip2ExtOperStatus_Type(Integer32):
    """Custom type etsysRip2ExtOperStatus based on Integer32"""
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
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )


_EtsysRip2ExtOperStatus_Type.__name__ = "Integer32"
_EtsysRip2ExtOperStatus_Object = MibScalar
etsysRip2ExtOperStatus = _EtsysRip2ExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 2),
    _EtsysRip2ExtOperStatus_Type()
)
etsysRip2ExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRip2ExtOperStatus.setStatus("current")


class _EtsysRip2ExtMaxEcmpHops_Type(Unsigned32):
    """Custom type etsysRip2ExtMaxEcmpHops based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRip2ExtMaxEcmpHops_Type.__name__ = "Unsigned32"
_EtsysRip2ExtMaxEcmpHops_Object = MibScalar
etsysRip2ExtMaxEcmpHops = _EtsysRip2ExtMaxEcmpHops_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 3),
    _EtsysRip2ExtMaxEcmpHops_Type()
)
etsysRip2ExtMaxEcmpHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtMaxEcmpHops.setStatus("current")


class _EtsysRip2ExtRefreshInterval_Type(Unsigned32):
    """Custom type etsysRip2ExtRefreshInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRip2ExtRefreshInterval_Type.__name__ = "Unsigned32"
_EtsysRip2ExtRefreshInterval_Object = MibScalar
etsysRip2ExtRefreshInterval = _EtsysRip2ExtRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 4),
    _EtsysRip2ExtRefreshInterval_Type()
)
etsysRip2ExtRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysRip2ExtRefreshInterval.setUnits("seconds")


class _EtsysRip2ExtTriggeredDelayMin_Type(Unsigned32):
    """Custom type etsysRip2ExtTriggeredDelayMin based on Unsigned32"""
    defaultValue = 1


_EtsysRip2ExtTriggeredDelayMin_Object = MibScalar
etsysRip2ExtTriggeredDelayMin = _EtsysRip2ExtTriggeredDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 5),
    _EtsysRip2ExtTriggeredDelayMin_Type()
)
etsysRip2ExtTriggeredDelayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtTriggeredDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    etsysRip2ExtTriggeredDelayMin.setUnits("seconds")


class _EtsysRip2ExtTriggeredDelayMax_Type(Unsigned32):
    """Custom type etsysRip2ExtTriggeredDelayMax based on Unsigned32"""
    defaultValue = 5


_EtsysRip2ExtTriggeredDelayMax_Object = MibScalar
etsysRip2ExtTriggeredDelayMax = _EtsysRip2ExtTriggeredDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 6),
    _EtsysRip2ExtTriggeredDelayMax_Type()
)
etsysRip2ExtTriggeredDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtTriggeredDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    etsysRip2ExtTriggeredDelayMax.setUnits("seconds")


class _EtsysRip2ExtRouteCheckInterval_Type(Unsigned32):
    """Custom type etsysRip2ExtRouteCheckInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_EtsysRip2ExtRouteCheckInterval_Type.__name__ = "Unsigned32"
_EtsysRip2ExtRouteCheckInterval_Object = MibScalar
etsysRip2ExtRouteCheckInterval = _EtsysRip2ExtRouteCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 7),
    _EtsysRip2ExtRouteCheckInterval_Type()
)
etsysRip2ExtRouteCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtRouteCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysRip2ExtRouteCheckInterval.setUnits("seconds")


class _EtsysRip2ExtRouteExpiryInterval_Type(Unsigned32):
    """Custom type etsysRip2ExtRouteExpiryInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysRip2ExtRouteExpiryInterval_Type.__name__ = "Unsigned32"
_EtsysRip2ExtRouteExpiryInterval_Object = MibScalar
etsysRip2ExtRouteExpiryInterval = _EtsysRip2ExtRouteExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 8),
    _EtsysRip2ExtRouteExpiryInterval_Type()
)
etsysRip2ExtRouteExpiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtRouteExpiryInterval.setStatus("current")


class _EtsysRip2ExtRouteFlushInterval_Type(Unsigned32):
    """Custom type etsysRip2ExtRouteFlushInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysRip2ExtRouteFlushInterval_Type.__name__ = "Unsigned32"
_EtsysRip2ExtRouteFlushInterval_Object = MibScalar
etsysRip2ExtRouteFlushInterval = _EtsysRip2ExtRouteFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 9),
    _EtsysRip2ExtRouteFlushInterval_Type()
)
etsysRip2ExtRouteFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRip2ExtRouteFlushInterval.setStatus("current")
_EtsysRip2ExtConformance_ObjectIdentity = ObjectIdentity
etsysRip2ExtConformance = _EtsysRip2ExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2)
)
_EtsysRip2ExtGroups_ObjectIdentity = ObjectIdentity
etsysRip2ExtGroups = _EtsysRip2ExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 1)
)
_EtsysRip2ExtCompliances_ObjectIdentity = ObjectIdentity
etsysRip2ExtCompliances = _EtsysRip2ExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 2)
)

# Managed Objects groups

etsysRip2ExtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 1, 1)
)
etsysRip2ExtGlobalGroup.setObjects(
      *(("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtAdminStatus"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtOperStatus"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtMaxEcmpHops"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRefreshInterval"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtTriggeredDelayMin"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtTriggeredDelayMax"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteCheckInterval"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteExpiryInterval"),
        ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteFlushInterval"))
)
if mibBuilder.loadTexts:
    etsysRip2ExtGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRip2ExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysRip2ExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RIPv2-EXT-MIB",
    **{"etsysRip2ExtMIB": etsysRip2ExtMIB,
       "etsysRip2ExtObjects": etsysRip2ExtObjects,
       "etsysRip2ExtGlobals": etsysRip2ExtGlobals,
       "etsysRip2ExtAdminStatus": etsysRip2ExtAdminStatus,
       "etsysRip2ExtOperStatus": etsysRip2ExtOperStatus,
       "etsysRip2ExtMaxEcmpHops": etsysRip2ExtMaxEcmpHops,
       "etsysRip2ExtRefreshInterval": etsysRip2ExtRefreshInterval,
       "etsysRip2ExtTriggeredDelayMin": etsysRip2ExtTriggeredDelayMin,
       "etsysRip2ExtTriggeredDelayMax": etsysRip2ExtTriggeredDelayMax,
       "etsysRip2ExtRouteCheckInterval": etsysRip2ExtRouteCheckInterval,
       "etsysRip2ExtRouteExpiryInterval": etsysRip2ExtRouteExpiryInterval,
       "etsysRip2ExtRouteFlushInterval": etsysRip2ExtRouteFlushInterval,
       "etsysRip2ExtConformance": etsysRip2ExtConformance,
       "etsysRip2ExtGroups": etsysRip2ExtGroups,
       "etsysRip2ExtGlobalGroup": etsysRip2ExtGlobalGroup,
       "etsysRip2ExtCompliances": etsysRip2ExtCompliances,
       "etsysRip2ExtCompliance": etsysRip2ExtCompliance}
)
