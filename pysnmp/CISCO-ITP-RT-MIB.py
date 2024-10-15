# SNMP MIB module (CISCO-ITP-RT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-RT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:33 2024
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

(CItpTcLinksetId,
 CItpTcPointCode,
 CItpTcQos,
 CItpTcRouteTableName,
 CItpTcTableLoadStatus) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcLinksetId",
    "CItpTcPointCode",
    "CItpTcQos",
    "CItpTcRouteTableName",
    "CItpTcTableLoadStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpRtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228)
)
ciscoItpRtMIB.setRevisions(
        ("2003-07-10 00:00",
         "2002-01-07 00:00",
         "2001-08-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CItpRouteNotifications_ObjectIdentity = ObjectIdentity
cItpRouteNotifications = _CItpRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 0)
)
_CItpRtMIBObjects_ObjectIdentity = ObjectIdentity
cItpRtMIBObjects = _CItpRtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1)
)
_CItpRtScalars_ObjectIdentity = ObjectIdentity
cItpRtScalars = _CItpRtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1)
)
_CItpRtConfigLastChanged_Type = TimeStamp
_CItpRtConfigLastChanged_Object = MibScalar
cItpRtConfigLastChanged = _CItpRtConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 1),
    _CItpRtConfigLastChanged_Type()
)
cItpRtConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtConfigLastChanged.setStatus("deprecated")
_CItpRtConfigLoad_Type = TimeStamp
_CItpRtConfigLoad_Object = MibScalar
cItpRtConfigLoad = _CItpRtConfigLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 2),
    _CItpRtConfigLoad_Type()
)
cItpRtConfigLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtConfigLoad.setStatus("deprecated")
_CItpRtConfigLoadStatus_Type = CItpTcTableLoadStatus
_CItpRtConfigLoadStatus_Object = MibScalar
cItpRtConfigLoadStatus = _CItpRtConfigLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 3),
    _CItpRtConfigLoadStatus_Type()
)
cItpRtConfigLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtConfigLoadStatus.setStatus("deprecated")
_CItpRtStateChangeCount_Type = Counter32
_CItpRtStateChangeCount_Object = MibScalar
cItpRtStateChangeCount = _CItpRtStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 4),
    _CItpRtStateChangeCount_Type()
)
cItpRtStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtStateChangeCount.setStatus("deprecated")


class _CItpRtStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cItpRtStateChangeNotifEnabled based on TruthValue"""


_CItpRtStateChangeNotifEnabled_Object = MibScalar
cItpRtStateChangeNotifEnabled = _CItpRtStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 5),
    _CItpRtStateChangeNotifEnabled_Type()
)
cItpRtStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpRtStateChangeNotifEnabled.setStatus("deprecated")


class _CItpRtChangeNotifDelayTime_Type(Unsigned32):
    """Custom type cItpRtChangeNotifDelayTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CItpRtChangeNotifDelayTime_Type.__name__ = "Unsigned32"
_CItpRtChangeNotifDelayTime_Object = MibScalar
cItpRtChangeNotifDelayTime = _CItpRtChangeNotifDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 6),
    _CItpRtChangeNotifDelayTime_Type()
)
cItpRtChangeNotifDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpRtChangeNotifDelayTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpRtChangeNotifDelayTime.setUnits("seconds")


class _CItpRtMaxDynamicRoutes_Type(Integer32):
    """Custom type cItpRtMaxDynamicRoutes based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CItpRtMaxDynamicRoutes_Type.__name__ = "Integer32"
_CItpRtMaxDynamicRoutes_Object = MibScalar
cItpRtMaxDynamicRoutes = _CItpRtMaxDynamicRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 7),
    _CItpRtMaxDynamicRoutes_Type()
)
cItpRtMaxDynamicRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpRtMaxDynamicRoutes.setStatus("deprecated")


class _CItpRtChangeNotifWindowTime_Type(Integer32):
    """Custom type cItpRtChangeNotifWindowTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_CItpRtChangeNotifWindowTime_Type.__name__ = "Integer32"
_CItpRtChangeNotifWindowTime_Object = MibScalar
cItpRtChangeNotifWindowTime = _CItpRtChangeNotifWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 8),
    _CItpRtChangeNotifWindowTime_Type()
)
cItpRtChangeNotifWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpRtChangeNotifWindowTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpRtChangeNotifWindowTime.setUnits("seconds")


class _CItpRtChangeNotifMaxPerWindow_Type(Integer32):
    """Custom type cItpRtChangeNotifMaxPerWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 9000),
    )


_CItpRtChangeNotifMaxPerWindow_Type.__name__ = "Integer32"
_CItpRtChangeNotifMaxPerWindow_Object = MibScalar
cItpRtChangeNotifMaxPerWindow = _CItpRtChangeNotifMaxPerWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 1, 9),
    _CItpRtChangeNotifMaxPerWindow_Type()
)
cItpRtChangeNotifMaxPerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpRtChangeNotifMaxPerWindow.setStatus("deprecated")
_CItpRtTables_ObjectIdentity = ObjectIdentity
cItpRtTables = _CItpRtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2)
)
_CItpRouteTable_Object = MibTable
cItpRouteTable = _CItpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpRouteTable.setStatus("deprecated")
_CItpRouteTableEntry_Object = MibTableRow
cItpRouteTableEntry = _CItpRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1)
)
cItpRouteTableEntry.setIndexNames(
    (0, "CISCO-ITP-RT-MIB", "cItpRouteTableName"),
    (0, "CISCO-ITP-RT-MIB", "cItpRouteDpc"),
    (0, "CISCO-ITP-RT-MIB", "cItpRouteMask"),
    (0, "CISCO-ITP-RT-MIB", "cItpRouteDestLsCost"),
    (0, "CISCO-ITP-RT-MIB", "cItpRouteDestLinkset"),
)
if mibBuilder.loadTexts:
    cItpRouteTableEntry.setStatus("deprecated")
_CItpRouteTableName_Type = CItpTcRouteTableName
_CItpRouteTableName_Object = MibTableColumn
cItpRouteTableName = _CItpRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 1),
    _CItpRouteTableName_Type()
)
cItpRouteTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpRouteTableName.setStatus("deprecated")
_CItpRouteDpc_Type = CItpTcPointCode
_CItpRouteDpc_Object = MibTableColumn
cItpRouteDpc = _CItpRouteDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 2),
    _CItpRouteDpc_Type()
)
cItpRouteDpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpRouteDpc.setStatus("deprecated")


class _CItpRouteDestLsCost_Type(Unsigned32):
    """Custom type cItpRouteDestLsCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CItpRouteDestLsCost_Type.__name__ = "Unsigned32"
_CItpRouteDestLsCost_Object = MibTableColumn
cItpRouteDestLsCost = _CItpRouteDestLsCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 3),
    _CItpRouteDestLsCost_Type()
)
cItpRouteDestLsCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpRouteDestLsCost.setStatus("deprecated")
_CItpRouteDestLinkset_Type = CItpTcLinksetId
_CItpRouteDestLinkset_Object = MibTableColumn
cItpRouteDestLinkset = _CItpRouteDestLinkset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 4),
    _CItpRouteDestLinkset_Type()
)
cItpRouteDestLinkset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpRouteDestLinkset.setStatus("deprecated")


class _CItpRouteMask_Type(Unsigned32):
    """Custom type cItpRouteMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CItpRouteMask_Type.__name__ = "Unsigned32"
_CItpRouteMask_Object = MibTableColumn
cItpRouteMask = _CItpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 5),
    _CItpRouteMask_Type()
)
cItpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpRouteMask.setStatus("deprecated")
_CItpRouteQos_Type = CItpTcQos
_CItpRouteQos_Object = MibTableColumn
cItpRouteQos = _CItpRouteQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 6),
    _CItpRouteQos_Type()
)
cItpRouteQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRouteQos.setStatus("deprecated")


class _CItpRouteStatus_Type(Integer32):
    """Custom type cItpRouteStatus based on Integer32"""
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
        *(("available", 2),
          ("restricted", 3),
          ("unavailable", 4),
          ("unknown", 1))
    )


_CItpRouteStatus_Type.__name__ = "Integer32"
_CItpRouteStatus_Object = MibTableColumn
cItpRouteStatus = _CItpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 7),
    _CItpRouteStatus_Type()
)
cItpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRouteStatus.setStatus("deprecated")


class _CItpRouteNonAdjStatus_Type(Integer32):
    """Custom type cItpRouteNonAdjStatus based on Integer32"""
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
        *(("allowed", 2),
          ("prohibited", 4),
          ("restricted", 3),
          ("unknown", 1))
    )


_CItpRouteNonAdjStatus_Type.__name__ = "Integer32"
_CItpRouteNonAdjStatus_Object = MibTableColumn
cItpRouteNonAdjStatus = _CItpRouteNonAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 2, 1, 1, 8),
    _CItpRouteNonAdjStatus_Type()
)
cItpRouteNonAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRouteNonAdjStatus.setStatus("deprecated")
_CItpRtNotificationsInfo_ObjectIdentity = ObjectIdentity
cItpRtNotificationsInfo = _CItpRtNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3)
)
_CItpRtNotifInfoSuppressedFlag_Type = TruthValue
_CItpRtNotifInfoSuppressedFlag_Object = MibScalar
cItpRtNotifInfoSuppressedFlag = _CItpRtNotifInfoSuppressedFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3, 1),
    _CItpRtNotifInfoSuppressedFlag_Type()
)
cItpRtNotifInfoSuppressedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtNotifInfoSuppressedFlag.setStatus("deprecated")


class _CItpRtNotifInfoStateChanges_Type(OctetString):
    """Custom type cItpRtNotifInfoStateChanges based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 480),
    )


_CItpRtNotifInfoStateChanges_Type.__name__ = "OctetString"
_CItpRtNotifInfoStateChanges_Object = MibScalar
cItpRtNotifInfoStateChanges = _CItpRtNotifInfoStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 1, 3, 2),
    _CItpRtNotifInfoStateChanges_Type()
)
cItpRtNotifInfoStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpRtNotifInfoStateChanges.setStatus("deprecated")
_CItpRtMIBConformance_ObjectIdentity = ObjectIdentity
cItpRtMIBConformance = _CItpRtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2)
)
_CItpRtMIBCompliances_ObjectIdentity = ObjectIdentity
cItpRtMIBCompliances = _CItpRtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1)
)
_CItpRtMIBGroups_ObjectIdentity = ObjectIdentity
cItpRtMIBGroups = _CItpRtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2)
)

# Managed Objects groups

cItpRtScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 1)
)
cItpRtScalarGroup.setObjects(
    ("CISCO-ITP-RT-MIB", "cItpRtConfigLastChanged")
)
if mibBuilder.loadTexts:
    cItpRtScalarGroup.setStatus("deprecated")

cItpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 2)
)
cItpRouteGroup.setObjects(
      *(("CISCO-ITP-RT-MIB", "cItpRouteQos"),
        ("CISCO-ITP-RT-MIB", "cItpRouteStatus"),
        ("CISCO-ITP-RT-MIB", "cItpRouteNonAdjStatus"))
)
if mibBuilder.loadTexts:
    cItpRouteGroup.setStatus("deprecated")

cItpRtScalarGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 4)
)
cItpRtScalarGroupRev1.setObjects(
      *(("CISCO-ITP-RT-MIB", "cItpRtConfigLoad"),
        ("CISCO-ITP-RT-MIB", "cItpRtConfigLoadStatus"),
        ("CISCO-ITP-RT-MIB", "cItpRtStateChangeCount"),
        ("CISCO-ITP-RT-MIB", "cItpRtStateChangeNotifEnabled"),
        ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifDelayTime"),
        ("CISCO-ITP-RT-MIB", "cItpRtMaxDynamicRoutes"),
        ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifWindowTime"),
        ("CISCO-ITP-RT-MIB", "cItpRtChangeNotifMaxPerWindow"),
        ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoSuppressedFlag"),
        ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoStateChanges"))
)
if mibBuilder.loadTexts:
    cItpRtScalarGroupRev1.setStatus("deprecated")


# Notification objects

cItpRouteStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 0, 1)
)
cItpRouteStateChange.setObjects(
      *(("CISCO-ITP-RT-MIB", "cItpRtStateChangeCount"),
        ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoSuppressedFlag"),
        ("CISCO-ITP-RT-MIB", "cItpRtNotifInfoStateChanges"))
)
if mibBuilder.loadTexts:
    cItpRouteStateChange.setStatus(
        "deprecated"
    )


# Notifications groups

cItpRtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 2, 3)
)
cItpRtNotificationsGroup.setObjects(
    ("CISCO-ITP-RT-MIB", "cItpRouteStateChange")
)
if mibBuilder.loadTexts:
    cItpRtNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

cItpRtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cItpRtMIBCompliance.setStatus(
        "deprecated"
    )

cItpRtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 228, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cItpRtMIBComplianceRev1.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-RT-MIB",
    **{"ciscoItpRtMIB": ciscoItpRtMIB,
       "cItpRouteNotifications": cItpRouteNotifications,
       "cItpRouteStateChange": cItpRouteStateChange,
       "cItpRtMIBObjects": cItpRtMIBObjects,
       "cItpRtScalars": cItpRtScalars,
       "cItpRtConfigLastChanged": cItpRtConfigLastChanged,
       "cItpRtConfigLoad": cItpRtConfigLoad,
       "cItpRtConfigLoadStatus": cItpRtConfigLoadStatus,
       "cItpRtStateChangeCount": cItpRtStateChangeCount,
       "cItpRtStateChangeNotifEnabled": cItpRtStateChangeNotifEnabled,
       "cItpRtChangeNotifDelayTime": cItpRtChangeNotifDelayTime,
       "cItpRtMaxDynamicRoutes": cItpRtMaxDynamicRoutes,
       "cItpRtChangeNotifWindowTime": cItpRtChangeNotifWindowTime,
       "cItpRtChangeNotifMaxPerWindow": cItpRtChangeNotifMaxPerWindow,
       "cItpRtTables": cItpRtTables,
       "cItpRouteTable": cItpRouteTable,
       "cItpRouteTableEntry": cItpRouteTableEntry,
       "cItpRouteTableName": cItpRouteTableName,
       "cItpRouteDpc": cItpRouteDpc,
       "cItpRouteDestLsCost": cItpRouteDestLsCost,
       "cItpRouteDestLinkset": cItpRouteDestLinkset,
       "cItpRouteMask": cItpRouteMask,
       "cItpRouteQos": cItpRouteQos,
       "cItpRouteStatus": cItpRouteStatus,
       "cItpRouteNonAdjStatus": cItpRouteNonAdjStatus,
       "cItpRtNotificationsInfo": cItpRtNotificationsInfo,
       "cItpRtNotifInfoSuppressedFlag": cItpRtNotifInfoSuppressedFlag,
       "cItpRtNotifInfoStateChanges": cItpRtNotifInfoStateChanges,
       "cItpRtMIBConformance": cItpRtMIBConformance,
       "cItpRtMIBCompliances": cItpRtMIBCompliances,
       "cItpRtMIBCompliance": cItpRtMIBCompliance,
       "cItpRtMIBComplianceRev1": cItpRtMIBComplianceRev1,
       "cItpRtMIBGroups": cItpRtMIBGroups,
       "cItpRtScalarGroup": cItpRtScalarGroup,
       "cItpRouteGroup": cItpRouteGroup,
       "cItpRtNotificationsGroup": cItpRtNotificationsGroup,
       "cItpRtScalarGroupRev1": cItpRtScalarGroupRev1}
)
