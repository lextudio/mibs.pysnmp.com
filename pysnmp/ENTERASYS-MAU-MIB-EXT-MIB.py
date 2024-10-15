# SNMP MIB module (ENTERASYS-MAU-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MAU-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:08 2024
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

(ifMauIfIndex,) = mibBuilder.importSymbols(
    "MAU-MIB",
    "ifMauIfIndex")

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

etsysMauMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59)
)
etsysMauMibExtMIB.setRevisions(
        ("2006-05-09 11:30",
         "2006-02-16 19:18",
         "2005-02-07 15:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysMauMibExtObjects_ObjectIdentity = ObjectIdentity
etsysMauMibExtObjects = _EtsysMauMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1)
)
_EtsysMauMibExtBasic_ObjectIdentity = ObjectIdentity
etsysMauMibExtBasic = _EtsysMauMibExtBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1)
)
_EtsysIfMauExtMDIXTable_Object = MibTable
etsysIfMauExtMDIXTable = _EtsysIfMauExtMDIXTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIfMauExtMDIXTable.setStatus("current")
_EtsysIfMauExtMDIXEntry_Object = MibTableRow
etsysIfMauExtMDIXEntry = _EtsysIfMauExtMDIXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1)
)
etsysIfMauExtMDIXEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
)
if mibBuilder.loadTexts:
    etsysIfMauExtMDIXEntry.setStatus("current")


class _EtsysIfMauExtMDIXStatus_Type(Integer32):
    """Custom type etsysIfMauExtMDIXStatus based on Integer32"""
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
        *(("auto", 1),
          ("mdi", 3),
          ("mdix", 2))
    )


_EtsysIfMauExtMDIXStatus_Type.__name__ = "Integer32"
_EtsysIfMauExtMDIXStatus_Object = MibTableColumn
etsysIfMauExtMDIXStatus = _EtsysIfMauExtMDIXStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1, 1),
    _EtsysIfMauExtMDIXStatus_Type()
)
etsysIfMauExtMDIXStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIfMauExtMDIXStatus.setStatus("current")
_EtsysIfMauExtMasterSlaveTable_Object = MibTable
etsysIfMauExtMasterSlaveTable = _EtsysIfMauExtMasterSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysIfMauExtMasterSlaveTable.setStatus("deprecated")
_EtsysIfMauExtMasterSlaveEntry_Object = MibTableRow
etsysIfMauExtMasterSlaveEntry = _EtsysIfMauExtMasterSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1)
)
etsysIfMauExtMasterSlaveEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
)
if mibBuilder.loadTexts:
    etsysIfMauExtMasterSlaveEntry.setStatus("deprecated")


class _EtsysIfMauExtMasterSlaveStatus_Type(Integer32):
    """Custom type etsysIfMauExtMasterSlaveStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_EtsysIfMauExtMasterSlaveStatus_Type.__name__ = "Integer32"
_EtsysIfMauExtMasterSlaveStatus_Object = MibTableColumn
etsysIfMauExtMasterSlaveStatus = _EtsysIfMauExtMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1, 1),
    _EtsysIfMauExtMasterSlaveStatus_Type()
)
etsysIfMauExtMasterSlaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIfMauExtMasterSlaveStatus.setStatus("deprecated")
_EtsysMauMibExtConformance_ObjectIdentity = ObjectIdentity
etsysMauMibExtConformance = _EtsysMauMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2)
)
_EtsysMauMibExtGroups_ObjectIdentity = ObjectIdentity
etsysMauMibExtGroups = _EtsysMauMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1)
)
_EtsysMauMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysMauMibExtCompliances = _EtsysMauMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2)
)

# Managed Objects groups

etsysMauMibExtMDIXGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 1)
)
etsysMauMibExtMDIXGroup.setObjects(
    ("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMDIXStatus")
)
if mibBuilder.loadTexts:
    etsysMauMibExtMDIXGroup.setStatus("current")

etsysMauMibExtMasterSlaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 2)
)
etsysMauMibExtMasterSlaveGroup.setObjects(
    ("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMasterSlaveStatus")
)
if mibBuilder.loadTexts:
    etsysMauMibExtMasterSlaveGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMauMibExtMDIXCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMauMibExtMDIXCompliance.setStatus(
        "current"
    )

etsysMauMibExtMasterSlaveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMauMibExtMasterSlaveCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MAU-MIB-EXT-MIB",
    **{"etsysMauMibExtMIB": etsysMauMibExtMIB,
       "etsysMauMibExtObjects": etsysMauMibExtObjects,
       "etsysMauMibExtBasic": etsysMauMibExtBasic,
       "etsysIfMauExtMDIXTable": etsysIfMauExtMDIXTable,
       "etsysIfMauExtMDIXEntry": etsysIfMauExtMDIXEntry,
       "etsysIfMauExtMDIXStatus": etsysIfMauExtMDIXStatus,
       "etsysIfMauExtMasterSlaveTable": etsysIfMauExtMasterSlaveTable,
       "etsysIfMauExtMasterSlaveEntry": etsysIfMauExtMasterSlaveEntry,
       "etsysIfMauExtMasterSlaveStatus": etsysIfMauExtMasterSlaveStatus,
       "etsysMauMibExtConformance": etsysMauMibExtConformance,
       "etsysMauMibExtGroups": etsysMauMibExtGroups,
       "etsysMauMibExtMDIXGroup": etsysMauMibExtMDIXGroup,
       "etsysMauMibExtMasterSlaveGroup": etsysMauMibExtMasterSlaveGroup,
       "etsysMauMibExtCompliances": etsysMauMibExtCompliances,
       "etsysMauMibExtMDIXCompliance": etsysMauMibExtMDIXCompliance,
       "etsysMauMibExtMasterSlaveCompliance": etsysMauMibExtMasterSlaveCompliance}
)
