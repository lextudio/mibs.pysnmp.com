# SNMP MIB module (XEDIA-ADDRPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-ADDRPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:40 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaAddrPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AddrPoolObjects_ObjectIdentity = ObjectIdentity
addrPoolObjects = _AddrPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1)
)
_AddrPoolConfigTable_Object = MibTable
addrPoolConfigTable = _AddrPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1)
)
if mibBuilder.loadTexts:
    addrPoolConfigTable.setStatus("current")
_AddrPoolConfigEntry_Object = MibTableRow
addrPoolConfigEntry = _AddrPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1, 1)
)
addrPoolConfigEntry.setIndexNames(
    (0, "XEDIA-ADDRPOOL-MIB", "addrPoolConfigIdentifier"),
)
if mibBuilder.loadTexts:
    addrPoolConfigEntry.setStatus("current")


class _AddrPoolConfigIdentifier_Type(DisplayString):
    """Custom type addrPoolConfigIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AddrPoolConfigIdentifier_Type.__name__ = "DisplayString"
_AddrPoolConfigIdentifier_Object = MibTableColumn
addrPoolConfigIdentifier = _AddrPoolConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1, 1, 1),
    _AddrPoolConfigIdentifier_Type()
)
addrPoolConfigIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addrPoolConfigIdentifier.setStatus("current")


class _AddrPoolConfigNetwork_Type(IpAddress):
    """Custom type addrPoolConfigNetwork based on IpAddress"""
    defaultValue = 0


_AddrPoolConfigNetwork_Object = MibTableColumn
addrPoolConfigNetwork = _AddrPoolConfigNetwork_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1, 1, 2),
    _AddrPoolConfigNetwork_Type()
)
addrPoolConfigNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addrPoolConfigNetwork.setStatus("current")


class _AddrPoolConfigMask_Type(IpAddress):
    """Custom type addrPoolConfigMask based on IpAddress"""
    defaultValue = 0


_AddrPoolConfigMask_Object = MibTableColumn
addrPoolConfigMask = _AddrPoolConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1, 1, 3),
    _AddrPoolConfigMask_Type()
)
addrPoolConfigMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addrPoolConfigMask.setStatus("current")
_AddrPoolConfigRowStatus_Type = RowStatus
_AddrPoolConfigRowStatus_Object = MibTableColumn
addrPoolConfigRowStatus = _AddrPoolConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 1, 1, 4),
    _AddrPoolConfigRowStatus_Type()
)
addrPoolConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    addrPoolConfigRowStatus.setStatus("current")
_AddrPoolAllocationTable_Object = MibTable
addrPoolAllocationTable = _AddrPoolAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2)
)
if mibBuilder.loadTexts:
    addrPoolAllocationTable.setStatus("current")
_AddrPoolAllocationEntry_Object = MibTableRow
addrPoolAllocationEntry = _AddrPoolAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2, 1)
)
addrPoolAllocationEntry.setIndexNames(
    (0, "XEDIA-ADDRPOOL-MIB", "addrPoolAllocationNameIdentifier"),
    (0, "XEDIA-ADDRPOOL-MIB", "addrPoolAllocationIpAddress"),
)
if mibBuilder.loadTexts:
    addrPoolAllocationEntry.setStatus("current")


class _AddrPoolAllocationNameIdentifier_Type(DisplayString):
    """Custom type addrPoolAllocationNameIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AddrPoolAllocationNameIdentifier_Type.__name__ = "DisplayString"
_AddrPoolAllocationNameIdentifier_Object = MibTableColumn
addrPoolAllocationNameIdentifier = _AddrPoolAllocationNameIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2, 1, 1),
    _AddrPoolAllocationNameIdentifier_Type()
)
addrPoolAllocationNameIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addrPoolAllocationNameIdentifier.setStatus("current")
_AddrPoolAllocationIpAddress_Type = IpAddress
_AddrPoolAllocationIpAddress_Object = MibTableColumn
addrPoolAllocationIpAddress = _AddrPoolAllocationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2, 1, 2),
    _AddrPoolAllocationIpAddress_Type()
)
addrPoolAllocationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    addrPoolAllocationIpAddress.setStatus("current")
_AddrPoolAllocationUserLayer_Type = DisplayString
_AddrPoolAllocationUserLayer_Object = MibTableColumn
addrPoolAllocationUserLayer = _AddrPoolAllocationUserLayer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2, 1, 3),
    _AddrPoolAllocationUserLayer_Type()
)
addrPoolAllocationUserLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrPoolAllocationUserLayer.setStatus("current")
_AddrPoolAllocationRemoteUser_Type = DisplayString
_AddrPoolAllocationRemoteUser_Object = MibTableColumn
addrPoolAllocationRemoteUser = _AddrPoolAllocationRemoteUser_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 1, 2, 1, 4),
    _AddrPoolAllocationRemoteUser_Type()
)
addrPoolAllocationRemoteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrPoolAllocationRemoteUser.setStatus("current")
_AddrPoolConformance_ObjectIdentity = ObjectIdentity
addrPoolConformance = _AddrPoolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2)
)
_AddrPoolCompliances_ObjectIdentity = ObjectIdentity
addrPoolCompliances = _AddrPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2, 1)
)
_AddrPoolGroups_ObjectIdentity = ObjectIdentity
addrPoolGroups = _AddrPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2, 2)
)

# Managed Objects groups

addrPoolConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2, 2, 1)
)
addrPoolConfigGroup.setObjects(
      *(("XEDIA-ADDRPOOL-MIB", "addrPoolConfigNetwork"),
        ("XEDIA-ADDRPOOL-MIB", "addrPoolConfigMask"))
)
if mibBuilder.loadTexts:
    addrPoolConfigGroup.setStatus("current")

addrPoolAllocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2, 2, 2)
)
addrPoolAllocationGroup.setObjects(
      *(("XEDIA-ADDRPOOL-MIB", "addrPoolAllocationUserLayer"),
        ("XEDIA-ADDRPOOL-MIB", "addrPoolAllocationRemoteUser"))
)
if mibBuilder.loadTexts:
    addrPoolAllocationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

addrPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 43, 2, 1, 1)
)
if mibBuilder.loadTexts:
    addrPoolCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-ADDRPOOL-MIB",
    **{"xediaAddrPoolMIB": xediaAddrPoolMIB,
       "addrPoolObjects": addrPoolObjects,
       "addrPoolConfigTable": addrPoolConfigTable,
       "addrPoolConfigEntry": addrPoolConfigEntry,
       "addrPoolConfigIdentifier": addrPoolConfigIdentifier,
       "addrPoolConfigNetwork": addrPoolConfigNetwork,
       "addrPoolConfigMask": addrPoolConfigMask,
       "addrPoolConfigRowStatus": addrPoolConfigRowStatus,
       "addrPoolAllocationTable": addrPoolAllocationTable,
       "addrPoolAllocationEntry": addrPoolAllocationEntry,
       "addrPoolAllocationNameIdentifier": addrPoolAllocationNameIdentifier,
       "addrPoolAllocationIpAddress": addrPoolAllocationIpAddress,
       "addrPoolAllocationUserLayer": addrPoolAllocationUserLayer,
       "addrPoolAllocationRemoteUser": addrPoolAllocationRemoteUser,
       "addrPoolConformance": addrPoolConformance,
       "addrPoolCompliances": addrPoolCompliances,
       "addrPoolCompliance": addrPoolCompliance,
       "addrPoolGroups": addrPoolGroups,
       "addrPoolConfigGroup": addrPoolConfigGroup,
       "addrPoolAllocationGroup": addrPoolAllocationGroup}
)
