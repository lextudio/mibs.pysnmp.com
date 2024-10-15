# SNMP MIB module (NETWORK-ALCHEMY-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-ALCHEMY-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:15 2024
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

(cryptoCluster,
 netalModules,
 netalTraps) = mibBuilder.importSymbols(
    "NETAL-SMI",
    "cryptoCluster",
    "netalModules",
    "netalTraps")

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

networkAlchemyClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5, 2)
)
networkAlchemyClusterMIB.setRevisions(
        ("2000-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClusterInfoName_Type = DisplayString
_ClusterInfoName_Object = MibScalar
clusterInfoName = _ClusterInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 1),
    _ClusterInfoName_Type()
)
clusterInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterInfoName.setStatus("current")


class _ClusterMemberInfoNumMembers_Type(Integer32):
    """Custom type clusterMemberInfoNumMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterMemberInfoNumMembers_Type.__name__ = "Integer32"
_ClusterMemberInfoNumMembers_Object = MibScalar
clusterMemberInfoNumMembers = _ClusterMemberInfoNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 2),
    _ClusterMemberInfoNumMembers_Type()
)
clusterMemberInfoNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberInfoNumMembers.setStatus("current")
_ClusterAddrTable_Object = MibTable
clusterAddrTable = _ClusterAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 3)
)
if mibBuilder.loadTexts:
    clusterAddrTable.setStatus("current")
_ClusterAddrEntry_Object = MibTableRow
clusterAddrEntry = _ClusterAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 3, 1)
)
clusterAddrEntry.setIndexNames(
    (0, "NETWORK-ALCHEMY-CLUSTER-MIB", "clusterAddrIndex"),
)
if mibBuilder.loadTexts:
    clusterAddrEntry.setStatus("current")


class _ClusterAddrIndex_Type(Integer32):
    """Custom type clusterAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterAddrIndex_Type.__name__ = "Integer32"
_ClusterAddrIndex_Object = MibTableColumn
clusterAddrIndex = _ClusterAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 3, 1, 1),
    _ClusterAddrIndex_Type()
)
clusterAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterAddrIndex.setStatus("current")
_ClusterInfoAddrs_Type = IpAddress
_ClusterInfoAddrs_Object = MibTableColumn
clusterInfoAddrs = _ClusterInfoAddrs_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 3, 1, 2),
    _ClusterInfoAddrs_Type()
)
clusterInfoAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterInfoAddrs.setStatus("current")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("current")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "NETWORK-ALCHEMY-CLUSTER-MIB", "clusterMemberIndex"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("current")


class _ClusterMemberIndex_Type(Integer32):
    """Custom type clusterMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClusterMemberIndex_Type.__name__ = "Integer32"
_ClusterMemberIndex_Object = MibTableColumn
clusterMemberIndex = _ClusterMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4, 1, 1),
    _ClusterMemberIndex_Type()
)
clusterMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberIndex.setStatus("current")
_ClusterMemberPrimaryIPAddr_Type = IpAddress
_ClusterMemberPrimaryIPAddr_Object = MibTableColumn
clusterMemberPrimaryIPAddr = _ClusterMemberPrimaryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4, 1, 2),
    _ClusterMemberPrimaryIPAddr_Type()
)
clusterMemberPrimaryIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberPrimaryIPAddr.setStatus("current")


class _ClusterMemberWorkload_Type(Integer32):
    """Custom type clusterMemberWorkload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterMemberWorkload_Type.__name__ = "Integer32"
_ClusterMemberWorkload_Object = MibTableColumn
clusterMemberWorkload = _ClusterMemberWorkload_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4, 1, 3),
    _ClusterMemberWorkload_Type()
)
clusterMemberWorkload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberWorkload.setStatus("current")


class _ClusterMemberMaster_Type(Integer32):
    """Custom type clusterMemberMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ClusterMemberMaster_Type.__name__ = "Integer32"
_ClusterMemberMaster_Object = MibTableColumn
clusterMemberMaster = _ClusterMemberMaster_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 4, 1, 4),
    _ClusterMemberMaster_Type()
)
clusterMemberMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMaster.setStatus("current")
_ClusterMemberSecondaryIPAddrTable_Object = MibTable
clusterMemberSecondaryIPAddrTable = _ClusterMemberSecondaryIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 5)
)
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrTable.setStatus("current")
_ClusterMemberSecondaryIPAddrEntry_Object = MibTableRow
clusterMemberSecondaryIPAddrEntry = _ClusterMemberSecondaryIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 5, 1)
)
clusterMemberSecondaryIPAddrEntry.setIndexNames(
    (0, "NETWORK-ALCHEMY-CLUSTER-MIB", "clusterMemberIndex"),
    (0, "NETWORK-ALCHEMY-CLUSTER-MIB", "clusterMemberSecondaryIPAddrIndex"),
)
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrEntry.setStatus("current")
_ClusterMemberSecondaryIPAddr_Type = IpAddress
_ClusterMemberSecondaryIPAddr_Object = MibTableColumn
clusterMemberSecondaryIPAddr = _ClusterMemberSecondaryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 5, 1, 1),
    _ClusterMemberSecondaryIPAddr_Type()
)
clusterMemberSecondaryIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddr.setStatus("current")
_ClusterMemberSecondaryIPAddrIndex_Type = Integer32
_ClusterMemberSecondaryIPAddrIndex_Object = MibTableColumn
clusterMemberSecondaryIPAddrIndex = _ClusterMemberSecondaryIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1, 5, 1, 2),
    _ClusterMemberSecondaryIPAddrIndex_Type()
)
clusterMemberSecondaryIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrIndex.setStatus("current")

# Managed Objects groups


# Notification objects

netalTrap0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2972, 6, 0)
)
if mibBuilder.loadTexts:
    netalTrap0.setStatus(
        "current"
    )

clusterMemberJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2972, 6, 0, 1)
)
if mibBuilder.loadTexts:
    clusterMemberJoin.setStatus(
        "current"
    )

clusterMemberLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 2972, 6, 0, 2)
)
if mibBuilder.loadTexts:
    clusterMemberLeft.setStatus(
        "current"
    )

clusterMemberBecameMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2972, 6, 0, 3)
)
if mibBuilder.loadTexts:
    clusterMemberBecameMaster.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-ALCHEMY-CLUSTER-MIB",
    **{"clusterInfoName": clusterInfoName,
       "clusterMemberInfoNumMembers": clusterMemberInfoNumMembers,
       "clusterAddrTable": clusterAddrTable,
       "clusterAddrEntry": clusterAddrEntry,
       "clusterAddrIndex": clusterAddrIndex,
       "clusterInfoAddrs": clusterInfoAddrs,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "clusterMemberIndex": clusterMemberIndex,
       "clusterMemberPrimaryIPAddr": clusterMemberPrimaryIPAddr,
       "clusterMemberWorkload": clusterMemberWorkload,
       "clusterMemberMaster": clusterMemberMaster,
       "clusterMemberSecondaryIPAddrTable": clusterMemberSecondaryIPAddrTable,
       "clusterMemberSecondaryIPAddrEntry": clusterMemberSecondaryIPAddrEntry,
       "clusterMemberSecondaryIPAddr": clusterMemberSecondaryIPAddr,
       "clusterMemberSecondaryIPAddrIndex": clusterMemberSecondaryIPAddrIndex,
       "networkAlchemyClusterMIB": networkAlchemyClusterMIB,
       "netalTrap0": netalTrap0,
       "clusterMemberJoin": clusterMemberJoin,
       "clusterMemberLeft": clusterMemberLeft,
       "clusterMemberBecameMaster": clusterMemberBecameMaster}
)
