# SNMP MIB module (HMTRACKING-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMTRACKING-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:44 2024
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hmConfiguration")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hmTracking = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 15)
)
hmTracking.setRevisions(
        ("2007-09-13 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmTrackingGroup_ObjectIdentity = ObjectIdentity
hmTrackingGroup = _HmTrackingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1)
)
_HmTrackEvent_ObjectIdentity = ObjectIdentity
hmTrackEvent = _HmTrackEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 0)
)
if mibBuilder.loadTexts:
    hmTrackEvent.setStatus("current")
_HmTrackingTable_Object = MibTable
hmTrackingTable = _HmTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hmTrackingTable.setStatus("current")
_HmTrackingEntry_Object = MibTableRow
hmTrackingEntry = _HmTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1)
)
hmTrackingEntry.setIndexNames(
    (0, "HMTRACKING-SNMP-MIB", "hmTrackId"),
)
if mibBuilder.loadTexts:
    hmTrackingEntry.setStatus("current")
_HmTrackId_Type = Integer32
_HmTrackId_Object = MibTableColumn
hmTrackId = _HmTrackId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 1),
    _HmTrackId_Type()
)
hmTrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackId.setStatus("current")


class _HmTrackRowStatus_Type(RowStatus):
    """Custom type hmTrackRowStatus based on RowStatus"""


_HmTrackRowStatus_Object = MibTableColumn
hmTrackRowStatus = _HmTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 2),
    _HmTrackRowStatus_Type()
)
hmTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmTrackRowStatus.setStatus("current")


class _HmTrackType_Type(Integer32):
    """Custom type hmTrackType based on Integer32"""
    defaultValue = 1

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
        *(("interface", 2),
          ("logical", 4),
          ("ping", 3),
          ("undefined", 1))
    )


_HmTrackType_Type.__name__ = "Integer32"
_HmTrackType_Object = MibTableColumn
hmTrackType = _HmTrackType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 3),
    _HmTrackType_Type()
)
hmTrackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackType.setStatus("current")


class _HmTrackState_Type(Integer32):
    """Custom type hmTrackState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HmTrackState_Type.__name__ = "Integer32"
_HmTrackState_Object = MibTableColumn
hmTrackState = _HmTrackState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 4),
    _HmTrackState_Type()
)
hmTrackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackState.setStatus("current")


class _HmTrackNumberOfChanges_Type(Integer32):
    """Custom type hmTrackNumberOfChanges based on Integer32"""
    defaultValue = 0


_HmTrackNumberOfChanges_Object = MibTableColumn
hmTrackNumberOfChanges = _HmTrackNumberOfChanges_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 5),
    _HmTrackNumberOfChanges_Type()
)
hmTrackNumberOfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackNumberOfChanges.setStatus("current")


class _HmTrackTimeSinceLastChange_Type(TimeTicks):
    """Custom type hmTrackTimeSinceLastChange based on TimeTicks"""
    defaultValue = 0


_HmTrackTimeSinceLastChange_Object = MibTableColumn
hmTrackTimeSinceLastChange = _HmTrackTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 6),
    _HmTrackTimeSinceLastChange_Type()
)
hmTrackTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackTimeSinceLastChange.setStatus("current")


class _HmTrackIfNumber_Type(InterfaceIndexOrZero):
    """Custom type hmTrackIfNumber based on InterfaceIndexOrZero"""
    defaultValue = 0


_HmTrackIfNumber_Object = MibTableColumn
hmTrackIfNumber = _HmTrackIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 7),
    _HmTrackIfNumber_Type()
)
hmTrackIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackIfNumber.setStatus("current")


class _HmTrackIfLinkUpDelay_Type(Integer32):
    """Custom type hmTrackIfLinkUpDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmTrackIfLinkUpDelay_Type.__name__ = "Integer32"
_HmTrackIfLinkUpDelay_Object = MibTableColumn
hmTrackIfLinkUpDelay = _HmTrackIfLinkUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 8),
    _HmTrackIfLinkUpDelay_Type()
)
hmTrackIfLinkUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackIfLinkUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    hmTrackIfLinkUpDelay.setUnits("seconds")


class _HmTrackIfLinkDownDelay_Type(Integer32):
    """Custom type hmTrackIfLinkDownDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmTrackIfLinkDownDelay_Type.__name__ = "Integer32"
_HmTrackIfLinkDownDelay_Object = MibTableColumn
hmTrackIfLinkDownDelay = _HmTrackIfLinkDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 9),
    _HmTrackIfLinkDownDelay_Type()
)
hmTrackIfLinkDownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackIfLinkDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    hmTrackIfLinkDownDelay.setUnits("seconds")
_HmTrackPingIpAddress_Type = IpAddress
_HmTrackPingIpAddress_Object = MibTableColumn
hmTrackPingIpAddress = _HmTrackPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 10),
    _HmTrackPingIpAddress_Type()
)
hmTrackPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingIpAddress.setStatus("current")


class _HmTrackPingInterval_Type(Integer32):
    """Custom type hmTrackPingInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmTrackPingInterval_Type.__name__ = "Integer32"
_HmTrackPingInterval_Object = MibTableColumn
hmTrackPingInterval = _HmTrackPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 11),
    _HmTrackPingInterval_Type()
)
hmTrackPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmTrackPingInterval.setUnits("seconds")


class _HmTrackPingMiss_Type(Integer32):
    """Custom type hmTrackPingMiss based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmTrackPingMiss_Type.__name__ = "Integer32"
_HmTrackPingMiss_Object = MibTableColumn
hmTrackPingMiss = _HmTrackPingMiss_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 12),
    _HmTrackPingMiss_Type()
)
hmTrackPingMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingMiss.setStatus("current")


class _HmTrackPingSuccess_Type(Integer32):
    """Custom type hmTrackPingSuccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmTrackPingSuccess_Type.__name__ = "Integer32"
_HmTrackPingSuccess_Object = MibTableColumn
hmTrackPingSuccess = _HmTrackPingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 13),
    _HmTrackPingSuccess_Type()
)
hmTrackPingSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingSuccess.setStatus("current")


class _HmTrackPingTimeout_Type(Integer32):
    """Custom type hmTrackPingTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_HmTrackPingTimeout_Type.__name__ = "Integer32"
_HmTrackPingTimeout_Object = MibTableColumn
hmTrackPingTimeout = _HmTrackPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 14),
    _HmTrackPingTimeout_Type()
)
hmTrackPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hmTrackPingTimeout.setUnits("milliseconds")


class _HmTrackPingTTL_Type(Integer32):
    """Custom type hmTrackPingTTL based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmTrackPingTTL_Type.__name__ = "Integer32"
_HmTrackPingTTL_Object = MibTableColumn
hmTrackPingTTL = _HmTrackPingTTL_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 15),
    _HmTrackPingTTL_Type()
)
hmTrackPingTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackPingTTL.setStatus("current")


class _HmTrackPingBestRouteIfNumber_Type(InterfaceIndexOrZero):
    """Custom type hmTrackPingBestRouteIfNumber based on InterfaceIndexOrZero"""
    defaultValue = 0


_HmTrackPingBestRouteIfNumber_Object = MibTableColumn
hmTrackPingBestRouteIfNumber = _HmTrackPingBestRouteIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 16),
    _HmTrackPingBestRouteIfNumber_Type()
)
hmTrackPingBestRouteIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackPingBestRouteIfNumber.setStatus("current")


class _HmTrackLogicalOperator_Type(Integer32):
    """Custom type hmTrackLogicalOperator based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2))
    )


_HmTrackLogicalOperator_Type.__name__ = "Integer32"
_HmTrackLogicalOperator_Object = MibTableColumn
hmTrackLogicalOperator = _HmTrackLogicalOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 17),
    _HmTrackLogicalOperator_Type()
)
hmTrackLogicalOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackLogicalOperator.setStatus("current")


class _HmTrackSendStateChangeTrap_Type(Integer32):
    """Custom type hmTrackSendStateChangeTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HmTrackSendStateChangeTrap_Type.__name__ = "Integer32"
_HmTrackSendStateChangeTrap_Object = MibTableColumn
hmTrackSendStateChangeTrap = _HmTrackSendStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 18),
    _HmTrackSendStateChangeTrap_Type()
)
hmTrackSendStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrackSendStateChangeTrap.setStatus("current")
_HmTrackingApplicationTable_Object = MibTable
hmTrackingApplicationTable = _HmTrackingApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hmTrackingApplicationTable.setStatus("current")
_HmTrackingApplicationEntry_Object = MibTableRow
hmTrackingApplicationEntry = _HmTrackingApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1)
)
hmTrackingApplicationEntry.setIndexNames(
    (0, "HMTRACKING-SNMP-MIB", "hmTrackId"),
    (0, "HMTRACKING-SNMP-MIB", "hmTrackAppId"),
)
if mibBuilder.loadTexts:
    hmTrackingApplicationEntry.setStatus("current")
_HmTrackAppId_Type = Integer32
_HmTrackAppId_Object = MibTableColumn
hmTrackAppId = _HmTrackAppId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1, 2),
    _HmTrackAppId_Type()
)
hmTrackAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmTrackAppId.setStatus("current")


class _HmTrackAppName_Type(DisplayString):
    """Custom type hmTrackAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmTrackAppName_Type.__name__ = "DisplayString"
_HmTrackAppName_Object = MibTableColumn
hmTrackAppName = _HmTrackAppName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1, 3),
    _HmTrackAppName_Type()
)
hmTrackAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrackAppName.setStatus("current")
_HmTrackLogicalInstanceTable_Object = MibTable
hmTrackLogicalInstanceTable = _HmTrackLogicalInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3)
)
if mibBuilder.loadTexts:
    hmTrackLogicalInstanceTable.setStatus("current")
_HmTrackLogicalInstanceEntry_Object = MibTableRow
hmTrackLogicalInstanceEntry = _HmTrackLogicalInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1)
)
hmTrackLogicalInstanceEntry.setIndexNames(
    (0, "HMTRACKING-SNMP-MIB", "hmTrackId"),
    (0, "HMTRACKING-SNMP-MIB", "hmTrackLogicalInstanceId"),
)
if mibBuilder.loadTexts:
    hmTrackLogicalInstanceEntry.setStatus("current")
_HmTrackLogicalInstanceId_Type = Integer32
_HmTrackLogicalInstanceId_Object = MibTableColumn
hmTrackLogicalInstanceId = _HmTrackLogicalInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1, 2),
    _HmTrackLogicalInstanceId_Type()
)
hmTrackLogicalInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmTrackLogicalInstanceId.setStatus("current")


class _HmTrackLogicInstRowStatus_Type(RowStatus):
    """Custom type hmTrackLogicInstRowStatus based on RowStatus"""


_HmTrackLogicInstRowStatus_Object = MibTableColumn
hmTrackLogicInstRowStatus = _HmTrackLogicInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1, 3),
    _HmTrackLogicInstRowStatus_Type()
)
hmTrackLogicInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmTrackLogicInstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hmTrackStatusChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 0, 1)
)
hmTrackStatusChangeEvent.setObjects(
      *(("HMTRACKING-SNMP-MIB", "hmTrackId"),
        ("HMTRACKING-SNMP-MIB", "hmTrackRowStatus"),
        ("HMTRACKING-SNMP-MIB", "hmTrackState"))
)
if mibBuilder.loadTexts:
    hmTrackStatusChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMTRACKING-SNMP-MIB",
    **{"hmTracking": hmTracking,
       "hmTrackingGroup": hmTrackingGroup,
       "hmTrackEvent": hmTrackEvent,
       "hmTrackStatusChangeEvent": hmTrackStatusChangeEvent,
       "hmTrackingTable": hmTrackingTable,
       "hmTrackingEntry": hmTrackingEntry,
       "hmTrackId": hmTrackId,
       "hmTrackRowStatus": hmTrackRowStatus,
       "hmTrackType": hmTrackType,
       "hmTrackState": hmTrackState,
       "hmTrackNumberOfChanges": hmTrackNumberOfChanges,
       "hmTrackTimeSinceLastChange": hmTrackTimeSinceLastChange,
       "hmTrackIfNumber": hmTrackIfNumber,
       "hmTrackIfLinkUpDelay": hmTrackIfLinkUpDelay,
       "hmTrackIfLinkDownDelay": hmTrackIfLinkDownDelay,
       "hmTrackPingIpAddress": hmTrackPingIpAddress,
       "hmTrackPingInterval": hmTrackPingInterval,
       "hmTrackPingMiss": hmTrackPingMiss,
       "hmTrackPingSuccess": hmTrackPingSuccess,
       "hmTrackPingTimeout": hmTrackPingTimeout,
       "hmTrackPingTTL": hmTrackPingTTL,
       "hmTrackPingBestRouteIfNumber": hmTrackPingBestRouteIfNumber,
       "hmTrackLogicalOperator": hmTrackLogicalOperator,
       "hmTrackSendStateChangeTrap": hmTrackSendStateChangeTrap,
       "hmTrackingApplicationTable": hmTrackingApplicationTable,
       "hmTrackingApplicationEntry": hmTrackingApplicationEntry,
       "hmTrackAppId": hmTrackAppId,
       "hmTrackAppName": hmTrackAppName,
       "hmTrackLogicalInstanceTable": hmTrackLogicalInstanceTable,
       "hmTrackLogicalInstanceEntry": hmTrackLogicalInstanceEntry,
       "hmTrackLogicalInstanceId": hmTrackLogicalInstanceId,
       "hmTrackLogicInstRowStatus": hmTrackLogicInstRowStatus}
)
