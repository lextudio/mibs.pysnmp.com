# SNMP MIB module (T11-FC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:32 2024
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

(FcAddressIdOrZero,
 FcDomainIdOrZero,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcDomainIdOrZero",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 144)
)
t11FcRouteMIB.setRevisions(
        ("2006-08-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcRouteNotifications_ObjectIdentity = ObjectIdentity
t11FcRouteNotifications = _T11FcRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 144, 0)
)
_T11FcRouteObjects_ObjectIdentity = ObjectIdentity
t11FcRouteObjects = _T11FcRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 144, 1)
)
_T11FcRouteFabricTable_Object = MibTable
t11FcRouteFabricTable = _T11FcRouteFabricTable_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcRouteFabricTable.setStatus("current")
_T11FcRouteFabricEntry_Object = MibTableRow
t11FcRouteFabricEntry = _T11FcRouteFabricEntry_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 1, 1)
)
t11FcRouteFabricEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcRouteFabricEntry.setStatus("current")
_T11FcRouteFabricIndex_Type = T11FabricIndex
_T11FcRouteFabricIndex_Object = MibTableColumn
t11FcRouteFabricIndex = _T11FcRouteFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 1, 1, 1),
    _T11FcRouteFabricIndex_Type()
)
t11FcRouteFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteFabricIndex.setStatus("current")
_T11FcRouteFabricLastChange_Type = TimeStamp
_T11FcRouteFabricLastChange_Object = MibTableColumn
t11FcRouteFabricLastChange = _T11FcRouteFabricLastChange_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 1, 1, 2),
    _T11FcRouteFabricLastChange_Type()
)
t11FcRouteFabricLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRouteFabricLastChange.setStatus("current")
_T11FcRouteTable_Object = MibTable
t11FcRouteTable = _T11FcRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcRouteTable.setStatus("current")
_T11FcRouteEntry_Object = MibTableRow
t11FcRouteEntry = _T11FcRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1)
)
t11FcRouteEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteFabricIndex"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteDestAddrId"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteDestMask"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteSrcAddrId"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteSrcMask"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteInInterface"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteProto"),
    (0, "T11-FC-ROUTE-MIB", "t11FcRouteOutInterface"),
)
if mibBuilder.loadTexts:
    t11FcRouteEntry.setStatus("current")


class _T11FcRouteDestAddrId_Type(FcAddressIdOrZero):
    """Custom type t11FcRouteDestAddrId based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcRouteDestAddrId_Type.__name__ = "FcAddressIdOrZero"
_T11FcRouteDestAddrId_Object = MibTableColumn
t11FcRouteDestAddrId = _T11FcRouteDestAddrId_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 1),
    _T11FcRouteDestAddrId_Type()
)
t11FcRouteDestAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteDestAddrId.setStatus("current")
_T11FcRouteDestMask_Type = FcAddressIdOrZero
_T11FcRouteDestMask_Object = MibTableColumn
t11FcRouteDestMask = _T11FcRouteDestMask_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 2),
    _T11FcRouteDestMask_Type()
)
t11FcRouteDestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteDestMask.setStatus("current")
_T11FcRouteSrcAddrId_Type = FcAddressIdOrZero
_T11FcRouteSrcAddrId_Object = MibTableColumn
t11FcRouteSrcAddrId = _T11FcRouteSrcAddrId_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 3),
    _T11FcRouteSrcAddrId_Type()
)
t11FcRouteSrcAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteSrcAddrId.setStatus("current")
_T11FcRouteSrcMask_Type = FcAddressIdOrZero
_T11FcRouteSrcMask_Object = MibTableColumn
t11FcRouteSrcMask = _T11FcRouteSrcMask_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 4),
    _T11FcRouteSrcMask_Type()
)
t11FcRouteSrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteSrcMask.setStatus("current")
_T11FcRouteInInterface_Type = InterfaceIndexOrZero
_T11FcRouteInInterface_Object = MibTableColumn
t11FcRouteInInterface = _T11FcRouteInInterface_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 5),
    _T11FcRouteInInterface_Type()
)
t11FcRouteInInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteInInterface.setStatus("current")


class _T11FcRouteProto_Type(Integer32):
    """Custom type t11FcRouteProto based on Integer32"""
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
        *(("fspf", 4),
          ("local", 2),
          ("netmgmt", 3),
          ("other", 1))
    )


_T11FcRouteProto_Type.__name__ = "Integer32"
_T11FcRouteProto_Object = MibTableColumn
t11FcRouteProto = _T11FcRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 6),
    _T11FcRouteProto_Type()
)
t11FcRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteProto.setStatus("current")
_T11FcRouteOutInterface_Type = InterfaceIndex
_T11FcRouteOutInterface_Object = MibTableColumn
t11FcRouteOutInterface = _T11FcRouteOutInterface_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 7),
    _T11FcRouteOutInterface_Type()
)
t11FcRouteOutInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRouteOutInterface.setStatus("current")
_T11FcRouteDomainId_Type = FcDomainIdOrZero
_T11FcRouteDomainId_Object = MibTableColumn
t11FcRouteDomainId = _T11FcRouteDomainId_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 8),
    _T11FcRouteDomainId_Type()
)
t11FcRouteDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteDomainId.setStatus("current")


class _T11FcRouteMetric_Type(Unsigned32):
    """Custom type t11FcRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_T11FcRouteMetric_Type.__name__ = "Unsigned32"
_T11FcRouteMetric_Object = MibTableColumn
t11FcRouteMetric = _T11FcRouteMetric_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 9),
    _T11FcRouteMetric_Type()
)
t11FcRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteMetric.setStatus("current")


class _T11FcRouteType_Type(Integer32):
    """Custom type t11FcRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_T11FcRouteType_Type.__name__ = "Integer32"
_T11FcRouteType_Object = MibTableColumn
t11FcRouteType = _T11FcRouteType_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 10),
    _T11FcRouteType_Type()
)
t11FcRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteType.setStatus("current")


class _T11FcRouteIfDown_Type(Integer32):
    """Custom type t11FcRouteIfDown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remove", 1),
          ("retain", 2))
    )


_T11FcRouteIfDown_Type.__name__ = "Integer32"
_T11FcRouteIfDown_Object = MibTableColumn
t11FcRouteIfDown = _T11FcRouteIfDown_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 11),
    _T11FcRouteIfDown_Type()
)
t11FcRouteIfDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteIfDown.setStatus("current")


class _T11FcRouteStorageType_Type(StorageType):
    """Custom type t11FcRouteStorageType based on StorageType"""


_T11FcRouteStorageType_Object = MibTableColumn
t11FcRouteStorageType = _T11FcRouteStorageType_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 12),
    _T11FcRouteStorageType_Type()
)
t11FcRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteStorageType.setStatus("current")
_T11FcRouteRowStatus_Type = RowStatus
_T11FcRouteRowStatus_Object = MibTableColumn
t11FcRouteRowStatus = _T11FcRouteRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 13),
    _T11FcRouteRowStatus_Type()
)
t11FcRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcRouteRowStatus.setStatus("current")
_T11FcRouteConformance_ObjectIdentity = ObjectIdentity
t11FcRouteConformance = _T11FcRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 144, 2)
)
_T11FcRouteCompliances_ObjectIdentity = ObjectIdentity
t11FcRouteCompliances = _T11FcRouteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 144, 2, 1)
)
_T11FcRouteGroups_ObjectIdentity = ObjectIdentity
t11FcRouteGroups = _T11FcRouteGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 144, 2, 2)
)

# Managed Objects groups

t11FcRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 144, 2, 2, 1)
)
t11FcRouteGroup.setObjects(
      *(("T11-FC-ROUTE-MIB", "t11FcRouteFabricLastChange"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteDomainId"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteMetric"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteType"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteIfDown"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteStorageType"),
        ("T11-FC-ROUTE-MIB", "t11FcRouteRowStatus"))
)
if mibBuilder.loadTexts:
    t11FcRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

t11FcRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 144, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcRouteCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-ROUTE-MIB",
    **{"t11FcRouteMIB": t11FcRouteMIB,
       "t11FcRouteNotifications": t11FcRouteNotifications,
       "t11FcRouteObjects": t11FcRouteObjects,
       "t11FcRouteFabricTable": t11FcRouteFabricTable,
       "t11FcRouteFabricEntry": t11FcRouteFabricEntry,
       "t11FcRouteFabricIndex": t11FcRouteFabricIndex,
       "t11FcRouteFabricLastChange": t11FcRouteFabricLastChange,
       "t11FcRouteTable": t11FcRouteTable,
       "t11FcRouteEntry": t11FcRouteEntry,
       "t11FcRouteDestAddrId": t11FcRouteDestAddrId,
       "t11FcRouteDestMask": t11FcRouteDestMask,
       "t11FcRouteSrcAddrId": t11FcRouteSrcAddrId,
       "t11FcRouteSrcMask": t11FcRouteSrcMask,
       "t11FcRouteInInterface": t11FcRouteInInterface,
       "t11FcRouteProto": t11FcRouteProto,
       "t11FcRouteOutInterface": t11FcRouteOutInterface,
       "t11FcRouteDomainId": t11FcRouteDomainId,
       "t11FcRouteMetric": t11FcRouteMetric,
       "t11FcRouteType": t11FcRouteType,
       "t11FcRouteIfDown": t11FcRouteIfDown,
       "t11FcRouteStorageType": t11FcRouteStorageType,
       "t11FcRouteRowStatus": t11FcRouteRowStatus,
       "t11FcRouteConformance": t11FcRouteConformance,
       "t11FcRouteCompliances": t11FcRouteCompliances,
       "t11FcRouteCompliance": t11FcRouteCompliance,
       "t11FcRouteGroups": t11FcRouteGroups,
       "t11FcRouteGroup": t11FcRouteGroup}
)
