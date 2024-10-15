# SNMP MIB module (RBN-FAST-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-FAST-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:09 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

(VrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId")


# MODULE-IDENTITY

rbnFastVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45)
)
rbnFastVrrpMIB.setRevisions(
        ("2008-05-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnFastVrrpMIBObjects_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBObjects = _RbnFastVrrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1)
)
_RbnFastVrrpOperTable_Object = MibTable
rbnFastVrrpOperTable = _RbnFastVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFastVrrpOperTable.setStatus("current")
_RbnFastVrrpOperEntry_Object = MibTableRow
rbnFastVrrpOperEntry = _RbnFastVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1)
)
rbnFastVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-FAST-VRRP-MIB", "rbnFastVrrpOperVrId"),
)
if mibBuilder.loadTexts:
    rbnFastVrrpOperEntry.setStatus("current")
_RbnFastVrrpOperVrId_Type = VrId
_RbnFastVrrpOperVrId_Object = MibTableColumn
rbnFastVrrpOperVrId = _RbnFastVrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 1),
    _RbnFastVrrpOperVrId_Type()
)
rbnFastVrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFastVrrpOperVrId.setStatus("current")


class _RbnFastVrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type rbnFastVrrpOperAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_RbnFastVrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_RbnFastVrrpOperAdvertisementInterval_Object = MibTableColumn
rbnFastVrrpOperAdvertisementInterval = _RbnFastVrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 2),
    _RbnFastVrrpOperAdvertisementInterval_Type()
)
rbnFastVrrpOperAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFastVrrpOperAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    rbnFastVrrpOperAdvertisementInterval.setUnits("milliseconds")
_RbnFastVrrpConformance_ObjectIdentity = ObjectIdentity
rbnFastVrrpConformance = _RbnFastVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2)
)
_RbnFastVrrpMIBCompliances_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBCompliances = _RbnFastVrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1)
)
_RbnFastVrrpMIBGroups_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBGroups = _RbnFastVrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2)
)

# Managed Objects groups

rbnFastVrrpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2, 1)
)
rbnFastVrrpObjectGroup.setObjects(
    ("RBN-FAST-VRRP-MIB", "rbnFastVrrpOperAdvertisementInterval")
)
if mibBuilder.loadTexts:
    rbnFastVrrpObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnFastVrrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFastVrrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-FAST-VRRP-MIB",
    **{"rbnFastVrrpMIB": rbnFastVrrpMIB,
       "rbnFastVrrpMIBObjects": rbnFastVrrpMIBObjects,
       "rbnFastVrrpOperTable": rbnFastVrrpOperTable,
       "rbnFastVrrpOperEntry": rbnFastVrrpOperEntry,
       "rbnFastVrrpOperVrId": rbnFastVrrpOperVrId,
       "rbnFastVrrpOperAdvertisementInterval": rbnFastVrrpOperAdvertisementInterval,
       "rbnFastVrrpConformance": rbnFastVrrpConformance,
       "rbnFastVrrpMIBCompliances": rbnFastVrrpMIBCompliances,
       "rbnFastVrrpCompliance": rbnFastVrrpCompliance,
       "rbnFastVrrpMIBGroups": rbnFastVrrpMIBGroups,
       "rbnFastVrrpObjectGroup": rbnFastVrrpObjectGroup}
)
