# SNMP MIB module (NOKIA-ALCHEMYOS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ALCHEMYOS-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:31 2024
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

(alchemyOSModules,
 alchemyOSTraps,
 cryptoCluster) = mibBuilder.importSymbols(
    "NOKIA-ALCHEMYOS-MIB",
    "alchemyOSModules",
    "alchemyOSTraps",
    "cryptoCluster")

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

nokiaAlchemyOSClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 5, 2)
)
nokiaAlchemyOSClusterMIB.setRevisions(
        ("2001-01-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClusterInfoName_Type = DisplayString
_ClusterInfoName_Object = MibScalar
clusterInfoName = _ClusterInfoName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 2),
    _ClusterMemberInfoNumMembers_Type()
)
clusterMemberInfoNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberInfoNumMembers.setStatus("current")
_ClusterAddrTable_Object = MibTable
clusterAddrTable = _ClusterAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3)
)
if mibBuilder.loadTexts:
    clusterAddrTable.setStatus("current")
_ClusterAddrEntry_Object = MibTableRow
clusterAddrEntry = _ClusterAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1)
)
clusterAddrEntry.setIndexNames(
    (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterAddrIndex"),
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
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1, 1),
    _ClusterAddrIndex_Type()
)
clusterAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterAddrIndex.setStatus("current")
_ClusterInfoAddrs_Type = IpAddress
_ClusterInfoAddrs_Object = MibTableColumn
clusterInfoAddrs = _ClusterInfoAddrs_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 3, 1, 2),
    _ClusterInfoAddrs_Type()
)
clusterInfoAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterInfoAddrs.setStatus("current")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("current")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberIndex"),
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
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 1),
    _ClusterMemberIndex_Type()
)
clusterMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberIndex.setStatus("current")
_ClusterMemberPrimaryIPAddr_Type = IpAddress
_ClusterMemberPrimaryIPAddr_Object = MibTableColumn
clusterMemberPrimaryIPAddr = _ClusterMemberPrimaryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 4, 1, 4),
    _ClusterMemberMaster_Type()
)
clusterMemberMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMaster.setStatus("current")
_ClusterMemberSecondaryIPAddrTable_Object = MibTable
clusterMemberSecondaryIPAddrTable = _ClusterMemberSecondaryIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5)
)
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrTable.setStatus("current")
_ClusterMemberSecondaryIPAddrEntry_Object = MibTableRow
clusterMemberSecondaryIPAddrEntry = _ClusterMemberSecondaryIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1)
)
clusterMemberSecondaryIPAddrEntry.setIndexNames(
    (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberIndex"),
    (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "clusterMemberSecondaryIPAddrIndex"),
)
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrEntry.setStatus("current")
_ClusterMemberSecondaryIPAddr_Type = IpAddress
_ClusterMemberSecondaryIPAddr_Object = MibTableColumn
clusterMemberSecondaryIPAddr = _ClusterMemberSecondaryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1, 1),
    _ClusterMemberSecondaryIPAddr_Type()
)
clusterMemberSecondaryIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddr.setStatus("current")
_ClusterMemberSecondaryIPAddrIndex_Type = Integer32
_ClusterMemberSecondaryIPAddrIndex_Object = MibTableColumn
clusterMemberSecondaryIPAddrIndex = _ClusterMemberSecondaryIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 5, 1, 2),
    _ClusterMemberSecondaryIPAddrIndex_Type()
)
clusterMemberSecondaryIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberSecondaryIPAddrIndex.setStatus("current")
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6)
)
if mibBuilder.loadTexts:
    processTable.setStatus("current")
_ProcessEntry_Object = MibTableRow
processEntry = _ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1)
)
processEntry.setIndexNames(
    (0, "NOKIA-ALCHEMYOS-CLUSTER-MIB", "processIndex"),
)
if mibBuilder.loadTexts:
    processEntry.setStatus("current")


class _ProcessIndex_Type(Integer32):
    """Custom type processIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProcessIndex_Type.__name__ = "Integer32"
_ProcessIndex_Object = MibTableColumn
processIndex = _ProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1, 1),
    _ProcessIndex_Type()
)
processIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIndex.setStatus("current")
_ProcessName_Type = DisplayString
_ProcessName_Object = MibTableColumn
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 6, 1, 2),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("current")
_ExternalIPAddress_Type = IpAddress
_ExternalIPAddress_Object = MibScalar
externalIPAddress = _ExternalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1, 7),
    _ExternalIPAddress_Type()
)
externalIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalIPAddress.setStatus("current")
_AlchemyOSTrap0_ObjectIdentity = ObjectIdentity
alchemyOSTrap0 = _AlchemyOSTrap0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0)
)
if mibBuilder.loadTexts:
    alchemyOSTrap0.setStatus("current")

# Managed Objects groups


# Notification objects

clusterMemberJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 1)
)
if mibBuilder.loadTexts:
    clusterMemberJoin.setStatus(
        "current"
    )

clusterMemberLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 2)
)
if mibBuilder.loadTexts:
    clusterMemberLeft.setStatus(
        "current"
    )

clusterMemberBecameMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 3)
)
if mibBuilder.loadTexts:
    clusterMemberBecameMaster.setStatus(
        "current"
    )

cpuUtilExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 4)
)
if mibBuilder.loadTexts:
    cpuUtilExceeded.setStatus(
        "current"
    )

ioLoadExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 5)
)
if mibBuilder.loadTexts:
    ioLoadExceeded.setStatus(
        "current"
    )

droppedUdpPacketsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 6)
)
if mibBuilder.loadTexts:
    droppedUdpPacketsExceeded.setStatus(
        "current"
    )

memUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 7)
)
if mibBuilder.loadTexts:
    memUsageExceeded.setStatus(
        "current"
    )

droppedIpPacketsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 8)
)
if mibBuilder.loadTexts:
    droppedIpPacketsExceeded.setStatus(
        "current"
    )

gatedConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 9)
)
if mibBuilder.loadTexts:
    gatedConfigError.setStatus(
        "current"
    )

informAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6, 0, 10)
)
informAddress.setObjects(
    ("NOKIA-ALCHEMYOS-CLUSTER-MIB", "externalIPAddress")
)
if mibBuilder.loadTexts:
    informAddress.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ALCHEMYOS-CLUSTER-MIB",
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
       "processTable": processTable,
       "processEntry": processEntry,
       "processIndex": processIndex,
       "processName": processName,
       "externalIPAddress": externalIPAddress,
       "nokiaAlchemyOSClusterMIB": nokiaAlchemyOSClusterMIB,
       "alchemyOSTrap0": alchemyOSTrap0,
       "clusterMemberJoin": clusterMemberJoin,
       "clusterMemberLeft": clusterMemberLeft,
       "clusterMemberBecameMaster": clusterMemberBecameMaster,
       "cpuUtilExceeded": cpuUtilExceeded,
       "ioLoadExceeded": ioLoadExceeded,
       "droppedUdpPacketsExceeded": droppedUdpPacketsExceeded,
       "memUsageExceeded": memUsageExceeded,
       "droppedIpPacketsExceeded": droppedIpPacketsExceeded,
       "gatedConfigError": gatedConfigError,
       "informAddress": informAddress}
)
