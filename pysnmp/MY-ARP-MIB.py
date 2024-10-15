# SNMP MIB module (MY-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:19 2024
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

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "MY-TC",
    "IfIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2)
)
myArpMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyArpMIBObjects_ObjectIdentity = ObjectIdentity
myArpMIBObjects = _MyArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1)
)
_MyArpTable_Object = MibTable
myArpTable = _MyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myArpTable.setStatus("current")
_MyArpEntry_Object = MibTableRow
myArpEntry = _MyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1)
)
myArpEntry.setIndexNames(
    (0, "MY-ARP-MIB", "myArpIfIndex"),
    (0, "MY-ARP-MIB", "myArpNetAddress"),
)
if mibBuilder.loadTexts:
    myArpEntry.setStatus("current")
_MyArpIfIndex_Type = IfIndex
_MyArpIfIndex_Object = MibTableColumn
myArpIfIndex = _MyArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 1),
    _MyArpIfIndex_Type()
)
myArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpIfIndex.setStatus("current")
_MyArpPhysAddress_Type = PhysAddress
_MyArpPhysAddress_Object = MibTableColumn
myArpPhysAddress = _MyArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 2),
    _MyArpPhysAddress_Type()
)
myArpPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myArpPhysAddress.setStatus("current")
_MyArpNetAddress_Type = IpAddress
_MyArpNetAddress_Object = MibTableColumn
myArpNetAddress = _MyArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 3),
    _MyArpNetAddress_Type()
)
myArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpNetAddress.setStatus("current")
_MyArpRemainAge_Type = Integer32
_MyArpRemainAge_Object = MibTableColumn
myArpRemainAge = _MyArpRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 4),
    _MyArpRemainAge_Type()
)
myArpRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpRemainAge.setStatus("current")


class _MyArpType_Type(Integer32):
    """Custom type myArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("arpa", 1)
    )


_MyArpType_Type.__name__ = "Integer32"
_MyArpType_Object = MibTableColumn
myArpType = _MyArpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 5),
    _MyArpType_Type()
)
myArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myArpType.setStatus("current")


class _MyArpEntryType_Type(Integer32):
    """Custom type myArpEntryType based on Integer32"""
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
        *(("dynamic", 2),
          ("interface", 3),
          ("static", 1),
          ("trusted", 5),
          ("vrrp", 4))
    )


_MyArpEntryType_Type.__name__ = "Integer32"
_MyArpEntryType_Object = MibTableColumn
myArpEntryType = _MyArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 6),
    _MyArpEntryType_Type()
)
myArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpEntryType.setStatus("current")
_MyArpStatus_Type = RowStatus
_MyArpStatus_Object = MibTableColumn
myArpStatus = _MyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 1, 1, 7),
    _MyArpStatus_Type()
)
myArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myArpStatus.setStatus("current")
_MyArpIfTable_Object = MibTable
myArpIfTable = _MyArpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    myArpIfTable.setStatus("current")
_MyArpIfEntry_Object = MibTableRow
myArpIfEntry = _MyArpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 2, 1)
)
myArpIfEntry.setIndexNames(
    (0, "MY-ARP-MIB", "myArpIfIfIndex"),
)
if mibBuilder.loadTexts:
    myArpIfEntry.setStatus("current")
_MyArpIfIfIndex_Type = IfIndex
_MyArpIfIfIndex_Object = MibTableColumn
myArpIfIfIndex = _MyArpIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 2, 1, 1),
    _MyArpIfIfIndex_Type()
)
myArpIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpIfIfIndex.setStatus("current")


class _MyArpIfCacheTimeOut_Type(Integer32):
    """Custom type myArpIfCacheTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_MyArpIfCacheTimeOut_Type.__name__ = "Integer32"
_MyArpIfCacheTimeOut_Object = MibTableColumn
myArpIfCacheTimeOut = _MyArpIfCacheTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 2, 1, 2),
    _MyArpIfCacheTimeOut_Type()
)
myArpIfCacheTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myArpIfCacheTimeOut.setStatus("current")
_MyArpCurrentTotalNumber_Type = Counter32
_MyArpCurrentTotalNumber_Object = MibScalar
myArpCurrentTotalNumber = _MyArpCurrentTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 3),
    _MyArpCurrentTotalNumber_Type()
)
myArpCurrentTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpCurrentTotalNumber.setStatus("current")
_MyArpCurrentUnresolveNumber_Type = Counter32
_MyArpCurrentUnresolveNumber_Object = MibScalar
myArpCurrentUnresolveNumber = _MyArpCurrentUnresolveNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 1, 4),
    _MyArpCurrentUnresolveNumber_Type()
)
myArpCurrentUnresolveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myArpCurrentUnresolveNumber.setStatus("current")
_MyArpMIBConformance_ObjectIdentity = ObjectIdentity
myArpMIBConformance = _MyArpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 2)
)
_MyArpMIBCompliances_ObjectIdentity = ObjectIdentity
myArpMIBCompliances = _MyArpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 2, 1)
)
_MyArpMIBGroups_ObjectIdentity = ObjectIdentity
myArpMIBGroups = _MyArpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 2, 2)
)

# Managed Objects groups

myArpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 2, 2, 1)
)
myArpMIBGroup.setObjects(
      *(("MY-ARP-MIB", "myArpIfIndex"),
        ("MY-ARP-MIB", "myArpPhysAddress"),
        ("MY-ARP-MIB", "myArpNetAddress"),
        ("MY-ARP-MIB", "myArpRemainAge"),
        ("MY-ARP-MIB", "myArpType"),
        ("MY-ARP-MIB", "myArpEntryType"),
        ("MY-ARP-MIB", "myArpStatus"),
        ("MY-ARP-MIB", "myArpIfIfIndex"),
        ("MY-ARP-MIB", "myArpIfCacheTimeOut"),
        ("MY-ARP-MIB", "myArpCurrentTotalNumber"),
        ("MY-ARP-MIB", "myArpCurrentUnresolveNumber"))
)
if mibBuilder.loadTexts:
    myArpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myArpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myArpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ARP-MIB",
    **{"myArpMIB": myArpMIB,
       "myArpMIBObjects": myArpMIBObjects,
       "myArpTable": myArpTable,
       "myArpEntry": myArpEntry,
       "myArpIfIndex": myArpIfIndex,
       "myArpPhysAddress": myArpPhysAddress,
       "myArpNetAddress": myArpNetAddress,
       "myArpRemainAge": myArpRemainAge,
       "myArpType": myArpType,
       "myArpEntryType": myArpEntryType,
       "myArpStatus": myArpStatus,
       "myArpIfTable": myArpIfTable,
       "myArpIfEntry": myArpIfEntry,
       "myArpIfIfIndex": myArpIfIfIndex,
       "myArpIfCacheTimeOut": myArpIfCacheTimeOut,
       "myArpCurrentTotalNumber": myArpCurrentTotalNumber,
       "myArpCurrentUnresolveNumber": myArpCurrentUnresolveNumber,
       "myArpMIBConformance": myArpMIBConformance,
       "myArpMIBCompliances": myArpMIBCompliances,
       "myArpMIBCompliance": myArpMIBCompliance,
       "myArpMIBGroups": myArpMIBGroups,
       "myArpMIBGroup": myArpMIBGroup}
)
