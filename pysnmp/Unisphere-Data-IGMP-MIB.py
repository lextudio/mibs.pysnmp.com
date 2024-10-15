# SNMP MIB module (Unisphere-Data-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:51 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40)
)
usdIgmpMIB.setRevisions(
        ("2000-09-26 18:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdIgmpProxyGroupState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usdIgmpProxyGroupDelayingMember", 2),
          ("usdIgmpProxyGroupIdleMember", 1),
          ("usdIgmpProxyGroupUnknown", 0))
    )



class UsdIgmpProxyInterfaceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usdIgmpProxyInterfaceStateNonV1RouterPresent", 2),
          ("usdIgmpProxyInterfaceStateV1RouterPresent", 1),
          ("usdIgmpProxyInterfaceUnknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_UsdIgmpMIBObject_ObjectIdentity = ObjectIdentity
usdIgmpMIBObject = _UsdIgmpMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1)
)
_UsdIgmpProtocol_ObjectIdentity = ObjectIdentity
usdIgmpProtocol = _UsdIgmpProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1)
)
_UsdIgmpProxy_ObjectIdentity = ObjectIdentity
usdIgmpProxy = _UsdIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2)
)
_UsdIgmpProxyInterfaceTable_Object = MibTable
usdIgmpProxyInterfaceTable = _UsdIgmpProxyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceTable.setStatus("current")
_UsdIgmpProxyInterfaceEntry_Object = MibTableRow
usdIgmpProxyInterfaceEntry = _UsdIgmpProxyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1)
)
usdIgmpProxyInterfaceEntry.setIndexNames(
    (0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceEntry.setStatus("current")
_UsdIgmpProxyInterfaceIfIndex_Type = InterfaceIndex
_UsdIgmpProxyInterfaceIfIndex_Object = MibTableColumn
usdIgmpProxyInterfaceIfIndex = _UsdIgmpProxyInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 1),
    _UsdIgmpProxyInterfaceIfIndex_Type()
)
usdIgmpProxyInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceIfIndex.setStatus("current")
_UsdIgmpProxyInterfaceAddress_Type = IpAddress
_UsdIgmpProxyInterfaceAddress_Object = MibTableColumn
usdIgmpProxyInterfaceAddress = _UsdIgmpProxyInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 2),
    _UsdIgmpProxyInterfaceAddress_Type()
)
usdIgmpProxyInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceAddress.setStatus("current")
_UsdIgmpProxyInterfaceMask_Type = IpAddress
_UsdIgmpProxyInterfaceMask_Object = MibTableColumn
usdIgmpProxyInterfaceMask = _UsdIgmpProxyInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 3),
    _UsdIgmpProxyInterfaceMask_Type()
)
usdIgmpProxyInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceMask.setStatus("current")
_UsdIgmpProxyInterfaceState_Type = UsdIgmpProxyInterfaceState
_UsdIgmpProxyInterfaceState_Object = MibTableColumn
usdIgmpProxyInterfaceState = _UsdIgmpProxyInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 4),
    _UsdIgmpProxyInterfaceState_Type()
)
usdIgmpProxyInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceState.setStatus("current")
_UsdIgmpProxyInterfaceStatus_Type = RowStatus
_UsdIgmpProxyInterfaceStatus_Object = MibTableColumn
usdIgmpProxyInterfaceStatus = _UsdIgmpProxyInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 5),
    _UsdIgmpProxyInterfaceStatus_Type()
)
usdIgmpProxyInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceStatus.setStatus("current")
_UsdIgmpProxyInterfaceVersion_Type = Integer32
_UsdIgmpProxyInterfaceVersion_Object = MibTableColumn
usdIgmpProxyInterfaceVersion = _UsdIgmpProxyInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 6),
    _UsdIgmpProxyInterfaceVersion_Type()
)
usdIgmpProxyInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceVersion.setStatus("current")


class _UsdIgmpProxyInterfaceV1RoutePresentTimeout_Type(Integer32):
    """Custom type usdIgmpProxyInterfaceV1RoutePresentTimeout based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_UsdIgmpProxyInterfaceV1RoutePresentTimeout_Type.__name__ = "Integer32"
_UsdIgmpProxyInterfaceV1RoutePresentTimeout_Object = MibTableColumn
usdIgmpProxyInterfaceV1RoutePresentTimeout = _UsdIgmpProxyInterfaceV1RoutePresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 7),
    _UsdIgmpProxyInterfaceV1RoutePresentTimeout_Type()
)
usdIgmpProxyInterfaceV1RoutePresentTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV1RoutePresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV1RoutePresentTimeout.setUnits("seconds")


class _UsdIgmpProxyInterfaceUnsolicitedReportInterval_Type(Integer32):
    """Custom type usdIgmpProxyInterfaceUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_UsdIgmpProxyInterfaceUnsolicitedReportInterval_Type.__name__ = "Integer32"
_UsdIgmpProxyInterfaceUnsolicitedReportInterval_Object = MibTableColumn
usdIgmpProxyInterfaceUnsolicitedReportInterval = _UsdIgmpProxyInterfaceUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 8),
    _UsdIgmpProxyInterfaceUnsolicitedReportInterval_Type()
)
usdIgmpProxyInterfaceUnsolicitedReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceUnsolicitedReportInterval.setUnits("seconds")
_UsdIgmpProxyInterfaceTotalGroupCount_Type = Counter32
_UsdIgmpProxyInterfaceTotalGroupCount_Object = MibTableColumn
usdIgmpProxyInterfaceTotalGroupCount = _UsdIgmpProxyInterfaceTotalGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 9),
    _UsdIgmpProxyInterfaceTotalGroupCount_Type()
)
usdIgmpProxyInterfaceTotalGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceTotalGroupCount.setStatus("current")
_UsdIgmpProxyInterfaceWrongVersionCount_Type = Counter32
_UsdIgmpProxyInterfaceWrongVersionCount_Object = MibTableColumn
usdIgmpProxyInterfaceWrongVersionCount = _UsdIgmpProxyInterfaceWrongVersionCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 10),
    _UsdIgmpProxyInterfaceWrongVersionCount_Type()
)
usdIgmpProxyInterfaceWrongVersionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceWrongVersionCount.setStatus("current")
_UsdIgmpProxyInterfaceV1QueryReceiveCount_Type = Counter32
_UsdIgmpProxyInterfaceV1QueryReceiveCount_Object = MibTableColumn
usdIgmpProxyInterfaceV1QueryReceiveCount = _UsdIgmpProxyInterfaceV1QueryReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 11),
    _UsdIgmpProxyInterfaceV1QueryReceiveCount_Type()
)
usdIgmpProxyInterfaceV1QueryReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV1QueryReceiveCount.setStatus("current")
_UsdIgmpProxyInterfaceV2QueryReceiveCount_Type = Counter32
_UsdIgmpProxyInterfaceV2QueryReceiveCount_Object = MibTableColumn
usdIgmpProxyInterfaceV2QueryReceiveCount = _UsdIgmpProxyInterfaceV2QueryReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 12),
    _UsdIgmpProxyInterfaceV2QueryReceiveCount_Type()
)
usdIgmpProxyInterfaceV2QueryReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV2QueryReceiveCount.setStatus("current")
_UsdIgmpProxyInterfaceV1ReportReceiveCount_Type = Counter32
_UsdIgmpProxyInterfaceV1ReportReceiveCount_Object = MibTableColumn
usdIgmpProxyInterfaceV1ReportReceiveCount = _UsdIgmpProxyInterfaceV1ReportReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 13),
    _UsdIgmpProxyInterfaceV1ReportReceiveCount_Type()
)
usdIgmpProxyInterfaceV1ReportReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV1ReportReceiveCount.setStatus("current")
_UsdIgmpProxyInterfaceV2ReportReceiveCount_Type = Counter32
_UsdIgmpProxyInterfaceV2ReportReceiveCount_Object = MibTableColumn
usdIgmpProxyInterfaceV2ReportReceiveCount = _UsdIgmpProxyInterfaceV2ReportReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 14),
    _UsdIgmpProxyInterfaceV2ReportReceiveCount_Type()
)
usdIgmpProxyInterfaceV2ReportReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV2ReportReceiveCount.setStatus("current")
_UsdIgmpProxyInterfaceV1JoinReportCount_Type = Counter32
_UsdIgmpProxyInterfaceV1JoinReportCount_Object = MibTableColumn
usdIgmpProxyInterfaceV1JoinReportCount = _UsdIgmpProxyInterfaceV1JoinReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 15),
    _UsdIgmpProxyInterfaceV1JoinReportCount_Type()
)
usdIgmpProxyInterfaceV1JoinReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV1JoinReportCount.setStatus("current")
_UsdIgmpProxyInterfaceV2JoinReportCount_Type = Counter32
_UsdIgmpProxyInterfaceV2JoinReportCount_Object = MibTableColumn
usdIgmpProxyInterfaceV2JoinReportCount = _UsdIgmpProxyInterfaceV2JoinReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 16),
    _UsdIgmpProxyInterfaceV2JoinReportCount_Type()
)
usdIgmpProxyInterfaceV2JoinReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceV2JoinReportCount.setStatus("current")
_UsdIgmpProxyInterfaceLeaveReportCount_Type = Counter32
_UsdIgmpProxyInterfaceLeaveReportCount_Object = MibTableColumn
usdIgmpProxyInterfaceLeaveReportCount = _UsdIgmpProxyInterfaceLeaveReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 17),
    _UsdIgmpProxyInterfaceLeaveReportCount_Type()
)
usdIgmpProxyInterfaceLeaveReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceLeaveReportCount.setStatus("current")
_UsdIgmpProxyCacheTable_Object = MibTable
usdIgmpProxyCacheTable = _UsdIgmpProxyCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdIgmpProxyCacheTable.setStatus("current")
_UsdIgmpProxyCacheEntry_Object = MibTableRow
usdIgmpProxyCacheEntry = _UsdIgmpProxyCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1)
)
usdIgmpProxyCacheEntry.setIndexNames(
    (0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyIfIndex"),
    (0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyAddress"),
)
if mibBuilder.loadTexts:
    usdIgmpProxyCacheEntry.setStatus("current")
_UsdIgmpProxyIfIndex_Type = InterfaceIndex
_UsdIgmpProxyIfIndex_Object = MibTableColumn
usdIgmpProxyIfIndex = _UsdIgmpProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 1),
    _UsdIgmpProxyIfIndex_Type()
)
usdIgmpProxyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIgmpProxyIfIndex.setStatus("current")
_UsdIgmpProxyAddress_Type = IpAddress
_UsdIgmpProxyAddress_Object = MibTableColumn
usdIgmpProxyAddress = _UsdIgmpProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 2),
    _UsdIgmpProxyAddress_Type()
)
usdIgmpProxyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIgmpProxyAddress.setStatus("current")
_UsdIgmpProxyStatus_Type = UsdIgmpProxyGroupState
_UsdIgmpProxyStatus_Object = MibTableColumn
usdIgmpProxyStatus = _UsdIgmpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 3),
    _UsdIgmpProxyStatus_Type()
)
usdIgmpProxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIgmpProxyStatus.setStatus("current")
_UsdIgmpConformance_ObjectIdentity = ObjectIdentity
usdIgmpConformance = _UsdIgmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4)
)
_UsdIgmpCompliances_ObjectIdentity = ObjectIdentity
usdIgmpCompliances = _UsdIgmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1)
)
_UsdIgmpGroups_ObjectIdentity = ObjectIdentity
usdIgmpGroups = _UsdIgmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2)
)

# Managed Objects groups

usdIgmpProxyInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 1)
)
usdIgmpProxyInterfaceGroup.setObjects(
      *(("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceAddress"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceMask"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceState"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceStatus"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceVersion"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1RoutePresentTimeout"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceUnsolicitedReportInterval"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceTotalGroupCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceWrongVersionCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1QueryReceiveCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2QueryReceiveCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1ReportReceiveCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2ReportReceiveCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1JoinReportCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2JoinReportCount"),
        ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceLeaveReportCount"))
)
if mibBuilder.loadTexts:
    usdIgmpProxyInterfaceGroup.setStatus("current")

usdIgmpProxyCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 2)
)
usdIgmpProxyCacheGroup.setObjects(
    ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyStatus")
)
if mibBuilder.loadTexts:
    usdIgmpProxyCacheGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIgmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdIgmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IGMP-MIB",
    **{"UsdIgmpProxyGroupState": UsdIgmpProxyGroupState,
       "UsdIgmpProxyInterfaceState": UsdIgmpProxyInterfaceState,
       "usdIgmpMIB": usdIgmpMIB,
       "usdIgmpMIBObject": usdIgmpMIBObject,
       "usdIgmpProtocol": usdIgmpProtocol,
       "usdIgmpProxy": usdIgmpProxy,
       "usdIgmpProxyInterfaceTable": usdIgmpProxyInterfaceTable,
       "usdIgmpProxyInterfaceEntry": usdIgmpProxyInterfaceEntry,
       "usdIgmpProxyInterfaceIfIndex": usdIgmpProxyInterfaceIfIndex,
       "usdIgmpProxyInterfaceAddress": usdIgmpProxyInterfaceAddress,
       "usdIgmpProxyInterfaceMask": usdIgmpProxyInterfaceMask,
       "usdIgmpProxyInterfaceState": usdIgmpProxyInterfaceState,
       "usdIgmpProxyInterfaceStatus": usdIgmpProxyInterfaceStatus,
       "usdIgmpProxyInterfaceVersion": usdIgmpProxyInterfaceVersion,
       "usdIgmpProxyInterfaceV1RoutePresentTimeout": usdIgmpProxyInterfaceV1RoutePresentTimeout,
       "usdIgmpProxyInterfaceUnsolicitedReportInterval": usdIgmpProxyInterfaceUnsolicitedReportInterval,
       "usdIgmpProxyInterfaceTotalGroupCount": usdIgmpProxyInterfaceTotalGroupCount,
       "usdIgmpProxyInterfaceWrongVersionCount": usdIgmpProxyInterfaceWrongVersionCount,
       "usdIgmpProxyInterfaceV1QueryReceiveCount": usdIgmpProxyInterfaceV1QueryReceiveCount,
       "usdIgmpProxyInterfaceV2QueryReceiveCount": usdIgmpProxyInterfaceV2QueryReceiveCount,
       "usdIgmpProxyInterfaceV1ReportReceiveCount": usdIgmpProxyInterfaceV1ReportReceiveCount,
       "usdIgmpProxyInterfaceV2ReportReceiveCount": usdIgmpProxyInterfaceV2ReportReceiveCount,
       "usdIgmpProxyInterfaceV1JoinReportCount": usdIgmpProxyInterfaceV1JoinReportCount,
       "usdIgmpProxyInterfaceV2JoinReportCount": usdIgmpProxyInterfaceV2JoinReportCount,
       "usdIgmpProxyInterfaceLeaveReportCount": usdIgmpProxyInterfaceLeaveReportCount,
       "usdIgmpProxyCacheTable": usdIgmpProxyCacheTable,
       "usdIgmpProxyCacheEntry": usdIgmpProxyCacheEntry,
       "usdIgmpProxyIfIndex": usdIgmpProxyIfIndex,
       "usdIgmpProxyAddress": usdIgmpProxyAddress,
       "usdIgmpProxyStatus": usdIgmpProxyStatus,
       "usdIgmpConformance": usdIgmpConformance,
       "usdIgmpCompliances": usdIgmpCompliances,
       "usdIgmpCompliance": usdIgmpCompliance,
       "usdIgmpGroups": usdIgmpGroups,
       "usdIgmpProxyInterfaceGroup": usdIgmpProxyInterfaceGroup,
       "usdIgmpProxyCacheGroup": usdIgmpProxyCacheGroup}
)
