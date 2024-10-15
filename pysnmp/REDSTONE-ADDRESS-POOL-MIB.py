# SNMP MIB module (REDSTONE-ADDRESS-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-ADDRESS-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:33 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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


# MODULE-IDENTITY

rsAddressPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21)
)
rsAddressPoolMIB.setRevisions(
        ("1999-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsAddressPoolObjects_ObjectIdentity = ObjectIdentity
rsAddressPoolObjects = _RsAddressPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1)
)
_RsAddressPool_ObjectIdentity = ObjectIdentity
rsAddressPool = _RsAddressPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1)
)
_RsAddressPoolTable_Object = MibTable
rsAddressPoolTable = _RsAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsAddressPoolTable.setStatus("current")
_RsAddressPoolEntry_Object = MibTableRow
rsAddressPoolEntry = _RsAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1)
)
rsAddressPoolEntry.setIndexNames(
    (0, "REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolIndex"),
)
if mibBuilder.loadTexts:
    rsAddressPoolEntry.setStatus("current")


class _RsAddressPoolIndex_Type(Integer32):
    """Custom type rsAddressPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsAddressPoolIndex_Type.__name__ = "Integer32"
_RsAddressPoolIndex_Object = MibTableColumn
rsAddressPoolIndex = _RsAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 1),
    _RsAddressPoolIndex_Type()
)
rsAddressPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAddressPoolIndex.setStatus("current")
_RsAddressPoolRowStatus_Type = RowStatus
_RsAddressPoolRowStatus_Object = MibTableColumn
rsAddressPoolRowStatus = _RsAddressPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 2),
    _RsAddressPoolRowStatus_Type()
)
rsAddressPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAddressPoolRowStatus.setStatus("current")


class _RsAddressPoolName_Type(DisplayString):
    """Custom type rsAddressPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RsAddressPoolName_Type.__name__ = "DisplayString"
_RsAddressPoolName_Object = MibTableColumn
rsAddressPoolName = _RsAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 3),
    _RsAddressPoolName_Type()
)
rsAddressPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAddressPoolName.setStatus("current")
_RsAddressPoolStart_Type = IpAddress
_RsAddressPoolStart_Object = MibTableColumn
rsAddressPoolStart = _RsAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 4),
    _RsAddressPoolStart_Type()
)
rsAddressPoolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAddressPoolStart.setStatus("current")
_RsAddressPoolEnd_Type = IpAddress
_RsAddressPoolEnd_Object = MibTableColumn
rsAddressPoolEnd = _RsAddressPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 5),
    _RsAddressPoolEnd_Type()
)
rsAddressPoolEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAddressPoolEnd.setStatus("current")
_RsAddressPoolSize_Type = Integer32
_RsAddressPoolSize_Object = MibTableColumn
rsAddressPoolSize = _RsAddressPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 6),
    _RsAddressPoolSize_Type()
)
rsAddressPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAddressPoolSize.setStatus("current")
_RsAddressPoolInUse_Type = Integer32
_RsAddressPoolInUse_Object = MibTableColumn
rsAddressPoolInUse = _RsAddressPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 1, 1, 1, 1, 7),
    _RsAddressPoolInUse_Type()
)
rsAddressPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAddressPoolInUse.setStatus("current")
_RsAddressPoolMIBConformance_ObjectIdentity = ObjectIdentity
rsAddressPoolMIBConformance = _RsAddressPoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 4)
)
_RsAddressPoolMIBCompliances_ObjectIdentity = ObjectIdentity
rsAddressPoolMIBCompliances = _RsAddressPoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 4, 1)
)
_RsAddressPoolMIBGroups_ObjectIdentity = ObjectIdentity
rsAddressPoolMIBGroups = _RsAddressPoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 4, 2)
)

# Managed Objects groups

rsAddressPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 4, 2, 1)
)
rsAddressPoolGroup.setObjects(
      *(("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolRowStatus"),
        ("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolName"),
        ("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolStart"),
        ("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolEnd"),
        ("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolSize"),
        ("REDSTONE-ADDRESS-POOL-MIB", "rsAddressPoolInUse"))
)
if mibBuilder.loadTexts:
    rsAddressPoolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsAddressPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 21, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsAddressPoolCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-ADDRESS-POOL-MIB",
    **{"rsAddressPoolMIB": rsAddressPoolMIB,
       "rsAddressPoolObjects": rsAddressPoolObjects,
       "rsAddressPool": rsAddressPool,
       "rsAddressPoolTable": rsAddressPoolTable,
       "rsAddressPoolEntry": rsAddressPoolEntry,
       "rsAddressPoolIndex": rsAddressPoolIndex,
       "rsAddressPoolRowStatus": rsAddressPoolRowStatus,
       "rsAddressPoolName": rsAddressPoolName,
       "rsAddressPoolStart": rsAddressPoolStart,
       "rsAddressPoolEnd": rsAddressPoolEnd,
       "rsAddressPoolSize": rsAddressPoolSize,
       "rsAddressPoolInUse": rsAddressPoolInUse,
       "rsAddressPoolMIBConformance": rsAddressPoolMIBConformance,
       "rsAddressPoolMIBCompliances": rsAddressPoolMIBCompliances,
       "rsAddressPoolCompliance": rsAddressPoolCompliance,
       "rsAddressPoolMIBGroups": rsAddressPoolMIBGroups,
       "rsAddressPoolGroup": rsAddressPoolGroup}
)
