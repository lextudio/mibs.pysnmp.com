# SNMP MIB module (ACC-IP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:20 2024
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

(accAccessPartitionIfIndex,) = mibBuilder.importSymbols(
    "ACC-ACCESSPARTITION",
    "accAccessPartitionIfIndex")

(accBgpAggrComponentAddr,
 accBgpAggrComponentMask,
 accBgpAggregateAddr,
 accBgpAggregateMask) = mibBuilder.importSymbols(
    "ACC-BGP",
    "accBgpAggrComponentAddr",
    "accBgpAggrComponentMask",
    "accBgpAggregateAddr",
    "accBgpAggregateMask")

(ipCidrRouteDest,
 ipCidrRouteMask,
 ipCidrRouteNextHop,
 ipCidrRouteTos) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "ipCidrRouteDest",
    "ipCidrRouteMask",
    "ipCidrRouteNextHop",
    "ipCidrRouteTos")

(accIpAssignStartAddr,) = mibBuilder.importSymbols(
    "ACC-IPMISC",
    "accIpAssignStartAddr")

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpMultiPathTable_Object = MibTable
ipMultiPathTable = _IpMultiPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23)
)
if mibBuilder.loadTexts:
    ipMultiPathTable.setStatus("obsolete")
_IpMultiPathEntry_Object = MibTableRow
ipMultiPathEntry = _IpMultiPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1)
)
ipMultiPathEntry.setIndexNames(
    (0, "ACC-IP", "ipMultiPathDest"),
    (0, "ACC-IP", "ipMultiPathPolicy"),
    (0, "ACC-IP", "ipMultiPathNextHop"),
)
if mibBuilder.loadTexts:
    ipMultiPathEntry.setStatus("obsolete")
_IpMultiPathDest_Type = IpAddress
_IpMultiPathDest_Object = MibTableColumn
ipMultiPathDest = _IpMultiPathDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 1),
    _IpMultiPathDest_Type()
)
ipMultiPathDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathDest.setStatus("obsolete")
_IpMultiPathPolicy_Type = Integer32
_IpMultiPathPolicy_Object = MibTableColumn
ipMultiPathPolicy = _IpMultiPathPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 2),
    _IpMultiPathPolicy_Type()
)
ipMultiPathPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathPolicy.setStatus("obsolete")
_IpMultiPathIfIndex_Type = Integer32
_IpMultiPathIfIndex_Object = MibTableColumn
ipMultiPathIfIndex = _IpMultiPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 3),
    _IpMultiPathIfIndex_Type()
)
ipMultiPathIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathIfIndex.setStatus("obsolete")
_IpMultiPathMask_Type = IpAddress
_IpMultiPathMask_Object = MibTableColumn
ipMultiPathMask = _IpMultiPathMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 4),
    _IpMultiPathMask_Type()
)
ipMultiPathMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathMask.setStatus("obsolete")
_IpMultiPathNextHop_Type = IpAddress
_IpMultiPathNextHop_Object = MibTableColumn
ipMultiPathNextHop = _IpMultiPathNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 5),
    _IpMultiPathNextHop_Type()
)
ipMultiPathNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathNextHop.setStatus("obsolete")
_IpMultiPathMetric_Type = Integer32
_IpMultiPathMetric_Object = MibTableColumn
ipMultiPathMetric = _IpMultiPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 6),
    _IpMultiPathMetric_Type()
)
ipMultiPathMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathMetric.setStatus("obsolete")


class _IpMultiPathType_Type(Integer32):
    """Custom type ipMultiPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_IpMultiPathType_Type.__name__ = "Integer32"
_IpMultiPathType_Object = MibTableColumn
ipMultiPathType = _IpMultiPathType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 7),
    _IpMultiPathType_Type()
)
ipMultiPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathType.setStatus("obsolete")


class _IpMultiPathProto_Type(Integer32):
    """Custom type ipMultiPathProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              13)
        )
    )
    namedValues = NamedValues(
        *(("egp", 5),
          ("icmp", 4),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpMultiPathProto_Type.__name__ = "Integer32"
_IpMultiPathProto_Object = MibTableColumn
ipMultiPathProto = _IpMultiPathProto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 8),
    _IpMultiPathProto_Type()
)
ipMultiPathProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathProto.setStatus("obsolete")
_IpMultiPathAge_Type = Integer32
_IpMultiPathAge_Object = MibTableColumn
ipMultiPathAge = _IpMultiPathAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 9),
    _IpMultiPathAge_Type()
)
ipMultiPathAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathAge.setStatus("obsolete")
_IpMultiPathApplId_Type = Integer32
_IpMultiPathApplId_Object = MibTableColumn
ipMultiPathApplId = _IpMultiPathApplId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 10),
    _IpMultiPathApplId_Type()
)
ipMultiPathApplId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathApplId.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IP",
    **{"ipMultiPathTable": ipMultiPathTable,
       "ipMultiPathEntry": ipMultiPathEntry,
       "ipMultiPathDest": ipMultiPathDest,
       "ipMultiPathPolicy": ipMultiPathPolicy,
       "ipMultiPathIfIndex": ipMultiPathIfIndex,
       "ipMultiPathMask": ipMultiPathMask,
       "ipMultiPathNextHop": ipMultiPathNextHop,
       "ipMultiPathMetric": ipMultiPathMetric,
       "ipMultiPathType": ipMultiPathType,
       "ipMultiPathProto": ipMultiPathProto,
       "ipMultiPathAge": ipMultiPathAge,
       "ipMultiPathApplId": ipMultiPathApplId}
)
