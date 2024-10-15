# SNMP MIB module (CISCO-FCTRACEROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCTRACEROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:28 2024
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

(FcStartOper,) = mibBuilder.importSymbols(
    "CISCO-FCPING-MIB",
    "FcStartOper")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddress,
 FcAddressType,
 FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddress",
    "FcAddressType",
    "FcNameId",
    "VsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcTraceRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296)
)
ciscoFcTraceRouteMIB.setRevisions(
        ("2002-10-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFcTraceRouteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcTraceRouteMIBObjects = _CiscoFcTraceRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1)
)
_FcTraceRouteConfiguration_ObjectIdentity = ObjectIdentity
fcTraceRouteConfiguration = _FcTraceRouteConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1)
)
_FcTraceRouteTable_Object = MibTable
fcTraceRouteTable = _FcTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fcTraceRouteTable.setStatus("current")
_FcTraceRouteEntry_Object = MibTableRow
fcTraceRouteEntry = _FcTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1)
)
fcTraceRouteEntry.setIndexNames(
    (0, "CISCO-FCTRACEROUTE-MIB", "fcTraceRouteIndex"),
)
if mibBuilder.loadTexts:
    fcTraceRouteEntry.setStatus("current")


class _FcTraceRouteIndex_Type(Unsigned32):
    """Custom type fcTraceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcTraceRouteIndex_Type.__name__ = "Unsigned32"
_FcTraceRouteIndex_Object = MibTableColumn
fcTraceRouteIndex = _FcTraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 1),
    _FcTraceRouteIndex_Type()
)
fcTraceRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcTraceRouteIndex.setStatus("current")


class _FcTraceRouteVsanIndex_Type(VsanIndex):
    """Custom type fcTraceRouteVsanIndex based on VsanIndex"""
    defaultValue = 1


_FcTraceRouteVsanIndex_Object = MibTableColumn
fcTraceRouteVsanIndex = _FcTraceRouteVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 2),
    _FcTraceRouteVsanIndex_Type()
)
fcTraceRouteVsanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteVsanIndex.setStatus("current")


class _FcTraceRouteTargetAddrType_Type(FcAddressType):
    """Custom type fcTraceRouteTargetAddrType based on FcAddressType"""


_FcTraceRouteTargetAddrType_Object = MibTableColumn
fcTraceRouteTargetAddrType = _FcTraceRouteTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 3),
    _FcTraceRouteTargetAddrType_Type()
)
fcTraceRouteTargetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteTargetAddrType.setStatus("current")
_FcTraceRouteTargetAddr_Type = FcAddress
_FcTraceRouteTargetAddr_Object = MibTableColumn
fcTraceRouteTargetAddr = _FcTraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 4),
    _FcTraceRouteTargetAddr_Type()
)
fcTraceRouteTargetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteTargetAddr.setStatus("current")


class _FcTraceRouteTimeout_Type(Unsigned32):
    """Custom type fcTraceRouteTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_FcTraceRouteTimeout_Type.__name__ = "Unsigned32"
_FcTraceRouteTimeout_Object = MibTableColumn
fcTraceRouteTimeout = _FcTraceRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 5),
    _FcTraceRouteTimeout_Type()
)
fcTraceRouteTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fcTraceRouteTimeout.setUnits("seconds")


class _FcTraceRouteAdminStatus_Type(FcStartOper):
    """Custom type fcTraceRouteAdminStatus based on FcStartOper"""


_FcTraceRouteAdminStatus_Object = MibTableColumn
fcTraceRouteAdminStatus = _FcTraceRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 6),
    _FcTraceRouteAdminStatus_Type()
)
fcTraceRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteAdminStatus.setStatus("current")


class _FcTraceRouteOperStatus_Type(Integer32):
    """Custom type fcTraceRouteOperStatus based on Integer32"""
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
        *(("disabled", 5),
          ("failure", 4),
          ("inProgress", 1),
          ("partialSuccess", 3),
          ("success", 2))
    )


_FcTraceRouteOperStatus_Type.__name__ = "Integer32"
_FcTraceRouteOperStatus_Object = MibTableColumn
fcTraceRouteOperStatus = _FcTraceRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 7),
    _FcTraceRouteOperStatus_Type()
)
fcTraceRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTraceRouteOperStatus.setStatus("current")


class _FcTraceRouteAgeInterval_Type(Unsigned32):
    """Custom type fcTraceRouteAgeInterval based on Unsigned32"""
    defaultValue = 500000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500000, 900000),
    )


_FcTraceRouteAgeInterval_Type.__name__ = "Unsigned32"
_FcTraceRouteAgeInterval_Object = MibTableColumn
fcTraceRouteAgeInterval = _FcTraceRouteAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 8),
    _FcTraceRouteAgeInterval_Type()
)
fcTraceRouteAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    fcTraceRouteAgeInterval.setUnits("milliseconds")


class _FcTraceRouteTrapOnCompletion_Type(TruthValue):
    """Custom type fcTraceRouteTrapOnCompletion based on TruthValue"""


_FcTraceRouteTrapOnCompletion_Object = MibTableColumn
fcTraceRouteTrapOnCompletion = _FcTraceRouteTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 9),
    _FcTraceRouteTrapOnCompletion_Type()
)
fcTraceRouteTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteTrapOnCompletion.setStatus("current")
_FcTraceRouteRowStatus_Type = RowStatus
_FcTraceRouteRowStatus_Object = MibTableColumn
fcTraceRouteRowStatus = _FcTraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 1, 1, 1, 10),
    _FcTraceRouteRowStatus_Type()
)
fcTraceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcTraceRouteRowStatus.setStatus("current")
_FcTraceRouteResults_ObjectIdentity = ObjectIdentity
fcTraceRouteResults = _FcTraceRouteResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2)
)
_FcTraceRouteHopsTable_Object = MibTable
fcTraceRouteHopsTable = _FcTraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcTraceRouteHopsTable.setStatus("current")
_FcTraceRouteHopsEntry_Object = MibTableRow
fcTraceRouteHopsEntry = _FcTraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1, 1)
)
fcTraceRouteHopsEntry.setIndexNames(
    (0, "CISCO-FCTRACEROUTE-MIB", "fcTraceRouteIndex"),
    (0, "CISCO-FCTRACEROUTE-MIB", "fcTraceRouteHopsHopIndex"),
)
if mibBuilder.loadTexts:
    fcTraceRouteHopsEntry.setStatus("current")


class _FcTraceRouteHopsHopIndex_Type(Unsigned32):
    """Custom type fcTraceRouteHopsHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcTraceRouteHopsHopIndex_Type.__name__ = "Unsigned32"
_FcTraceRouteHopsHopIndex_Object = MibTableColumn
fcTraceRouteHopsHopIndex = _FcTraceRouteHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1, 1, 1),
    _FcTraceRouteHopsHopIndex_Type()
)
fcTraceRouteHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcTraceRouteHopsHopIndex.setStatus("current")
_FcTraceRouteHopsHopAddr_Type = FcNameId
_FcTraceRouteHopsHopAddr_Object = MibTableColumn
fcTraceRouteHopsHopAddr = _FcTraceRouteHopsHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1, 1, 2),
    _FcTraceRouteHopsHopAddr_Type()
)
fcTraceRouteHopsHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTraceRouteHopsHopAddr.setStatus("current")
_FcTraceRouteHopsHopLatencyValid_Type = TruthValue
_FcTraceRouteHopsHopLatencyValid_Object = MibTableColumn
fcTraceRouteHopsHopLatencyValid = _FcTraceRouteHopsHopLatencyValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1, 1, 3),
    _FcTraceRouteHopsHopLatencyValid_Type()
)
fcTraceRouteHopsHopLatencyValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTraceRouteHopsHopLatencyValid.setStatus("current")


class _FcTraceRouteHopsHopLatency_Type(Unsigned32):
    """Custom type fcTraceRouteHopsHopLatency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000000),
    )


_FcTraceRouteHopsHopLatency_Type.__name__ = "Unsigned32"
_FcTraceRouteHopsHopLatency_Object = MibTableColumn
fcTraceRouteHopsHopLatency = _FcTraceRouteHopsHopLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 2, 1, 1, 4),
    _FcTraceRouteHopsHopLatency_Type()
)
fcTraceRouteHopsHopLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTraceRouteHopsHopLatency.setStatus("current")
_FcTraceRouteNotification_ObjectIdentity = ObjectIdentity
fcTraceRouteNotification = _FcTraceRouteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 3)
)
_FcTraceRouteNotifications_ObjectIdentity = ObjectIdentity
fcTraceRouteNotifications = _FcTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 3, 0)
)
_FcTraceRouteMIBConformance_ObjectIdentity = ObjectIdentity
fcTraceRouteMIBConformance = _FcTraceRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2)
)
_FcTraceRouteMIBCompliances_ObjectIdentity = ObjectIdentity
fcTraceRouteMIBCompliances = _FcTraceRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 1)
)
_FcTraceRouteMIBGroups_ObjectIdentity = ObjectIdentity
fcTraceRouteMIBGroups = _FcTraceRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 2)
)

# Managed Objects groups

fcTraceRouteConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 2, 1)
)
fcTraceRouteConfigGroup.setObjects(
      *(("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteVsanIndex"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteTargetAddrType"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteTargetAddr"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteTimeout"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteAdminStatus"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteOperStatus"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteAgeInterval"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteTrapOnCompletion"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteRowStatus"))
)
if mibBuilder.loadTexts:
    fcTraceRouteConfigGroup.setStatus("current")

fcTraceRouteResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 2, 2)
)
fcTraceRouteResultsGroup.setObjects(
      *(("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteHopsHopAddr"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteHopsHopLatencyValid"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteHopsHopLatency"))
)
if mibBuilder.loadTexts:
    fcTraceRouteResultsGroup.setStatus("current")


# Notification objects

fcTraceRouteCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 1, 3, 0, 1)
)
fcTraceRouteCompletionNotify.setObjects(
      *(("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteTargetAddr"),
        ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteOperStatus"))
)
if mibBuilder.loadTexts:
    fcTraceRouteCompletionNotify.setStatus(
        "current"
    )


# Notifications groups

fcTraceRouteNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 2, 3)
)
fcTraceRouteNotifyGroup.setObjects(
    ("CISCO-FCTRACEROUTE-MIB", "fcTraceRouteCompletionNotify")
)
if mibBuilder.loadTexts:
    fcTraceRouteNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fcTraceRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 296, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcTraceRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCTRACEROUTE-MIB",
    **{"ciscoFcTraceRouteMIB": ciscoFcTraceRouteMIB,
       "ciscoFcTraceRouteMIBObjects": ciscoFcTraceRouteMIBObjects,
       "fcTraceRouteConfiguration": fcTraceRouteConfiguration,
       "fcTraceRouteTable": fcTraceRouteTable,
       "fcTraceRouteEntry": fcTraceRouteEntry,
       "fcTraceRouteIndex": fcTraceRouteIndex,
       "fcTraceRouteVsanIndex": fcTraceRouteVsanIndex,
       "fcTraceRouteTargetAddrType": fcTraceRouteTargetAddrType,
       "fcTraceRouteTargetAddr": fcTraceRouteTargetAddr,
       "fcTraceRouteTimeout": fcTraceRouteTimeout,
       "fcTraceRouteAdminStatus": fcTraceRouteAdminStatus,
       "fcTraceRouteOperStatus": fcTraceRouteOperStatus,
       "fcTraceRouteAgeInterval": fcTraceRouteAgeInterval,
       "fcTraceRouteTrapOnCompletion": fcTraceRouteTrapOnCompletion,
       "fcTraceRouteRowStatus": fcTraceRouteRowStatus,
       "fcTraceRouteResults": fcTraceRouteResults,
       "fcTraceRouteHopsTable": fcTraceRouteHopsTable,
       "fcTraceRouteHopsEntry": fcTraceRouteHopsEntry,
       "fcTraceRouteHopsHopIndex": fcTraceRouteHopsHopIndex,
       "fcTraceRouteHopsHopAddr": fcTraceRouteHopsHopAddr,
       "fcTraceRouteHopsHopLatencyValid": fcTraceRouteHopsHopLatencyValid,
       "fcTraceRouteHopsHopLatency": fcTraceRouteHopsHopLatency,
       "fcTraceRouteNotification": fcTraceRouteNotification,
       "fcTraceRouteNotifications": fcTraceRouteNotifications,
       "fcTraceRouteCompletionNotify": fcTraceRouteCompletionNotify,
       "fcTraceRouteMIBConformance": fcTraceRouteMIBConformance,
       "fcTraceRouteMIBCompliances": fcTraceRouteMIBCompliances,
       "fcTraceRouteMIBCompliance": fcTraceRouteMIBCompliance,
       "fcTraceRouteMIBGroups": fcTraceRouteMIBGroups,
       "fcTraceRouteConfigGroup": fcTraceRouteConfigGroup,
       "fcTraceRouteResultsGroup": fcTraceRouteResultsGroup,
       "fcTraceRouteNotifyGroup": fcTraceRouteNotifyGroup}
)
