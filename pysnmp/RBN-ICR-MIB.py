# SNMP MIB module (RBN-ICR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ICR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:09 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

rbnIcrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101)
)
rbnIcrMIB.setRevisions(
        ("2011-01-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnIcrNotifications_ObjectIdentity = ObjectIdentity
rbnIcrNotifications = _RbnIcrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 0)
)
_RbnIcrMIBObjects_ObjectIdentity = ObjectIdentity
rbnIcrMIBObjects = _RbnIcrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1)
)
_RbnIcrTable_Object = MibTable
rbnIcrTable = _RbnIcrTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIcrTable.setStatus("current")
_RbnIcrEntry_Object = MibTableRow
rbnIcrEntry = _RbnIcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1)
)
rbnIcrEntry.setIndexNames(
    (0, "RBN-ICR-MIB", "rbnIcrId"),
)
if mibBuilder.loadTexts:
    rbnIcrEntry.setStatus("current")


class _RbnIcrId_Type(Integer32):
    """Custom type rbnIcrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnIcrId_Type.__name__ = "Integer32"
_RbnIcrId_Object = MibTableColumn
rbnIcrId = _RbnIcrId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 1),
    _RbnIcrId_Type()
)
rbnIcrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnIcrId.setStatus("current")


class _RbnIcrLocalAddressType_Type(InetAddressType):
    """Custom type rbnIcrLocalAddressType based on InetAddressType"""


_RbnIcrLocalAddressType_Object = MibTableColumn
rbnIcrLocalAddressType = _RbnIcrLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 2),
    _RbnIcrLocalAddressType_Type()
)
rbnIcrLocalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrLocalAddressType.setStatus("current")


class _RbnIcrLocalAddress_Type(InetAddress):
    """Custom type rbnIcrLocalAddress based on InetAddress"""
    defaultHexValue = ""


_RbnIcrLocalAddress_Object = MibTableColumn
rbnIcrLocalAddress = _RbnIcrLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 3),
    _RbnIcrLocalAddress_Type()
)
rbnIcrLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrLocalAddress.setStatus("current")


class _RbnIcrLocalPort_Type(InetPortNumber):
    """Custom type rbnIcrLocalPort based on InetPortNumber"""
    defaultValue = 0


_RbnIcrLocalPort_Object = MibTableColumn
rbnIcrLocalPort = _RbnIcrLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 4),
    _RbnIcrLocalPort_Type()
)
rbnIcrLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrLocalPort.setStatus("current")


class _RbnIcrPeerAddressType_Type(InetAddressType):
    """Custom type rbnIcrPeerAddressType based on InetAddressType"""


_RbnIcrPeerAddressType_Object = MibTableColumn
rbnIcrPeerAddressType = _RbnIcrPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 5),
    _RbnIcrPeerAddressType_Type()
)
rbnIcrPeerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrPeerAddressType.setStatus("current")


class _RbnIcrPeerAddress_Type(InetAddress):
    """Custom type rbnIcrPeerAddress based on InetAddress"""
    defaultHexValue = ""


_RbnIcrPeerAddress_Object = MibTableColumn
rbnIcrPeerAddress = _RbnIcrPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 6),
    _RbnIcrPeerAddress_Type()
)
rbnIcrPeerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrPeerAddress.setStatus("current")


class _RbnIcrPeerPort_Type(InetPortNumber):
    """Custom type rbnIcrPeerPort based on InetPortNumber"""
    defaultValue = 0


_RbnIcrPeerPort_Object = MibTableColumn
rbnIcrPeerPort = _RbnIcrPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 7),
    _RbnIcrPeerPort_Type()
)
rbnIcrPeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrPeerPort.setStatus("current")


class _RbnIcrPriority_Type(Integer32):
    """Custom type rbnIcrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_RbnIcrPriority_Type.__name__ = "Integer32"
_RbnIcrPriority_Object = MibTableColumn
rbnIcrPriority = _RbnIcrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 8),
    _RbnIcrPriority_Type()
)
rbnIcrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrPriority.setStatus("current")


class _RbnIcrKeepAliveInterval_Type(Integer32):
    """Custom type rbnIcrKeepAliveInterval based on Integer32"""
    defaultValue = 1


_RbnIcrKeepAliveInterval_Object = MibTableColumn
rbnIcrKeepAliveInterval = _RbnIcrKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 9),
    _RbnIcrKeepAliveInterval_Type()
)
rbnIcrKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    rbnIcrKeepAliveInterval.setUnits("seconds")


class _RbnIcrHoldTime_Type(Integer32):
    """Custom type rbnIcrHoldTime based on Integer32"""
    defaultValue = 10


_RbnIcrHoldTime_Object = MibTableColumn
rbnIcrHoldTime = _RbnIcrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 10),
    _RbnIcrHoldTime_Type()
)
rbnIcrHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    rbnIcrHoldTime.setUnits("seconds")


class _RbnIcrState_Type(Integer32):
    """Custom type rbnIcrState based on Integer32"""
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
        *(("active", 2),
          ("initialize", 1),
          ("pendingStandby", 4),
          ("standby", 3))
    )


_RbnIcrState_Type.__name__ = "Integer32"
_RbnIcrState_Object = MibTableColumn
rbnIcrState = _RbnIcrState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 11),
    _RbnIcrState_Type()
)
rbnIcrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIcrState.setStatus("current")


class _RbnIcrAdminStatus_Type(Integer32):
    """Custom type rbnIcrAdminStatus based on Integer32"""
    defaultValue = 2

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


_RbnIcrAdminStatus_Type.__name__ = "Integer32"
_RbnIcrAdminStatus_Object = MibTableColumn
rbnIcrAdminStatus = _RbnIcrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 12),
    _RbnIcrAdminStatus_Type()
)
rbnIcrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrAdminStatus.setStatus("current")
_RbnIcrRowStatus_Type = RowStatus
_RbnIcrRowStatus_Object = MibTableColumn
rbnIcrRowStatus = _RbnIcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 13),
    _RbnIcrRowStatus_Type()
)
rbnIcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnIcrRowStatus.setStatus("current")


class _RbnIcrInconsistencyError_Type(Integer32):
    """Custom type rbnIcrInconsistencyError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("peerLoss", 1)
    )


_RbnIcrInconsistencyError_Type.__name__ = "Integer32"
_RbnIcrInconsistencyError_Object = MibScalar
rbnIcrInconsistencyError = _RbnIcrInconsistencyError_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 2),
    _RbnIcrInconsistencyError_Type()
)
rbnIcrInconsistencyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIcrInconsistencyError.setStatus("current")
_RbnIcrMIBConformance_ObjectIdentity = ObjectIdentity
rbnIcrMIBConformance = _RbnIcrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2)
)
_RbnIcrMIBCompliances_ObjectIdentity = ObjectIdentity
rbnIcrMIBCompliances = _RbnIcrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 1)
)
_RbnIcrMIBGroups_ObjectIdentity = ObjectIdentity
rbnIcrMIBGroups = _RbnIcrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2)
)

# Managed Objects groups

rbnIcrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 1)
)
rbnIcrGroup.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrLocalAddressType"),
        ("RBN-ICR-MIB", "rbnIcrLocalAddress"),
        ("RBN-ICR-MIB", "rbnIcrLocalPort"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddressType"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddress"),
        ("RBN-ICR-MIB", "rbnIcrPeerPort"),
        ("RBN-ICR-MIB", "rbnIcrPriority"),
        ("RBN-ICR-MIB", "rbnIcrKeepAliveInterval"),
        ("RBN-ICR-MIB", "rbnIcrHoldTime"),
        ("RBN-ICR-MIB", "rbnIcrState"),
        ("RBN-ICR-MIB", "rbnIcrAdminStatus"),
        ("RBN-ICR-MIB", "rbnIcrRowStatus"))
)
if mibBuilder.loadTexts:
    rbnIcrGroup.setStatus("current")

rbnIcrNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 2)
)
rbnIcrNotificationObjectGroup.setObjects(
    ("RBN-ICR-MIB", "rbnIcrInconsistencyError")
)
if mibBuilder.loadTexts:
    rbnIcrNotificationObjectGroup.setStatus("current")


# Notification objects

rbnIcrNewActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 1)
)
rbnIcrNewActive.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrLocalAddressType"),
        ("RBN-ICR-MIB", "rbnIcrLocalAddress"),
        ("RBN-ICR-MIB", "rbnIcrLocalPort"),
        ("RBN-ICR-MIB", "rbnIcrState"))
)
if mibBuilder.loadTexts:
    rbnIcrNewActive.setStatus(
        "current"
    )

rbnIcrNewStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 2)
)
rbnIcrNewStandby.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrLocalAddressType"),
        ("RBN-ICR-MIB", "rbnIcrLocalAddress"),
        ("RBN-ICR-MIB", "rbnIcrLocalPort"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddressType"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddress"),
        ("RBN-ICR-MIB", "rbnIcrPeerPort"),
        ("RBN-ICR-MIB", "rbnIcrState"))
)
if mibBuilder.loadTexts:
    rbnIcrNewStandby.setStatus(
        "current"
    )

rbnIcrNewPendingStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 3)
)
rbnIcrNewPendingStandby.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrLocalAddressType"),
        ("RBN-ICR-MIB", "rbnIcrLocalAddress"),
        ("RBN-ICR-MIB", "rbnIcrLocalPort"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddressType"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddress"),
        ("RBN-ICR-MIB", "rbnIcrPeerPort"),
        ("RBN-ICR-MIB", "rbnIcrState"))
)
if mibBuilder.loadTexts:
    rbnIcrNewPendingStandby.setStatus(
        "current"
    )

rbnIcrInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 4)
)
rbnIcrInconsistency.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrLocalAddressType"),
        ("RBN-ICR-MIB", "rbnIcrLocalAddress"),
        ("RBN-ICR-MIB", "rbnIcrLocalPort"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddressType"),
        ("RBN-ICR-MIB", "rbnIcrPeerAddress"),
        ("RBN-ICR-MIB", "rbnIcrPeerPort"),
        ("RBN-ICR-MIB", "rbnIcrInconsistencyError"))
)
if mibBuilder.loadTexts:
    rbnIcrInconsistency.setStatus(
        "current"
    )


# Notifications groups

rbnIcrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 3)
)
rbnIcrNotificationGroup.setObjects(
      *(("RBN-ICR-MIB", "rbnIcrNewActive"),
        ("RBN-ICR-MIB", "rbnIcrNewStandby"),
        ("RBN-ICR-MIB", "rbnIcrNewPendingStandby"),
        ("RBN-ICR-MIB", "rbnIcrInconsistency"))
)
if mibBuilder.loadTexts:
    rbnIcrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnIcrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIcrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ICR-MIB",
    **{"rbnIcrMIB": rbnIcrMIB,
       "rbnIcrNotifications": rbnIcrNotifications,
       "rbnIcrNewActive": rbnIcrNewActive,
       "rbnIcrNewStandby": rbnIcrNewStandby,
       "rbnIcrNewPendingStandby": rbnIcrNewPendingStandby,
       "rbnIcrInconsistency": rbnIcrInconsistency,
       "rbnIcrMIBObjects": rbnIcrMIBObjects,
       "rbnIcrTable": rbnIcrTable,
       "rbnIcrEntry": rbnIcrEntry,
       "rbnIcrId": rbnIcrId,
       "rbnIcrLocalAddressType": rbnIcrLocalAddressType,
       "rbnIcrLocalAddress": rbnIcrLocalAddress,
       "rbnIcrLocalPort": rbnIcrLocalPort,
       "rbnIcrPeerAddressType": rbnIcrPeerAddressType,
       "rbnIcrPeerAddress": rbnIcrPeerAddress,
       "rbnIcrPeerPort": rbnIcrPeerPort,
       "rbnIcrPriority": rbnIcrPriority,
       "rbnIcrKeepAliveInterval": rbnIcrKeepAliveInterval,
       "rbnIcrHoldTime": rbnIcrHoldTime,
       "rbnIcrState": rbnIcrState,
       "rbnIcrAdminStatus": rbnIcrAdminStatus,
       "rbnIcrRowStatus": rbnIcrRowStatus,
       "rbnIcrInconsistencyError": rbnIcrInconsistencyError,
       "rbnIcrMIBConformance": rbnIcrMIBConformance,
       "rbnIcrMIBCompliances": rbnIcrMIBCompliances,
       "rbnIcrMIBCompliance": rbnIcrMIBCompliance,
       "rbnIcrMIBGroups": rbnIcrMIBGroups,
       "rbnIcrGroup": rbnIcrGroup,
       "rbnIcrNotificationObjectGroup": rbnIcrNotificationObjectGroup,
       "rbnIcrNotificationGroup": rbnIcrNotificationGroup}
)
