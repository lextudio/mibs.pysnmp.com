# SNMP MIB module (WWP-MULTI-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-MULTI-DHCP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:17 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpMultiDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42)
)
wwpMultiDhcpClientMIB.setRevisions(
        ("2002-11-01 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpMultiDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBObjects = _WwpMultiDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1)
)
_WwpMultiDhcpClient_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClient = _WwpMultiDhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1)
)
_WwpMultiDhcpClientNumber_Type = Integer32
_WwpMultiDhcpClientNumber_Object = MibScalar
wwpMultiDhcpClientNumber = _WwpMultiDhcpClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 1),
    _WwpMultiDhcpClientNumber_Type()
)
wwpMultiDhcpClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpMultiDhcpClientNumber.setStatus("current")
_WwpMultiDhcpClientTable_Object = MibTable
wwpMultiDhcpClientTable = _WwpMultiDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpMultiDhcpClientTable.setStatus("current")
_WwpMultiDhcpClientEntry_Object = MibTableRow
wwpMultiDhcpClientEntry = _WwpMultiDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1)
)
wwpMultiDhcpClientEntry.setIndexNames(
    (0, "WWP-MULTI-DHCP-CLIENT-MIB", "wwpDhcpIfIndex"),
)
if mibBuilder.loadTexts:
    wwpMultiDhcpClientEntry.setStatus("current")


class _WwpDhcpIfIndex_Type(Integer32):
    """Custom type wwpDhcpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpDhcpIfIndex_Type.__name__ = "Integer32"
_WwpDhcpIfIndex_Object = MibTableColumn
wwpDhcpIfIndex = _WwpDhcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 1),
    _WwpDhcpIfIndex_Type()
)
wwpDhcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpIfIndex.setStatus("current")


class _WwpDhcpIfName_Type(DisplayString):
    """Custom type wwpDhcpIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpDhcpIfName_Type.__name__ = "DisplayString"
_WwpDhcpIfName_Object = MibTableColumn
wwpDhcpIfName = _WwpDhcpIfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 2),
    _WwpDhcpIfName_Type()
)
wwpDhcpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpIfName.setStatus("current")


class _WwpDhcpStatus_Type(Integer32):
    """Custom type wwpDhcpStatus based on Integer32"""
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


_WwpDhcpStatus_Type.__name__ = "Integer32"
_WwpDhcpStatus_Object = MibTableColumn
wwpDhcpStatus = _WwpDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 3),
    _WwpDhcpStatus_Type()
)
wwpDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpStatus.setStatus("current")


class _WwpDhcpState_Type(Integer32):
    """Custom type wwpDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("disabled", 2),
          ("inform", 3),
          ("init", 4),
          ("rebinding", 5),
          ("renewing", 6),
          ("requesting", 7),
          ("selecting", 8),
          ("unknown", 9))
    )


_WwpDhcpState_Type.__name__ = "Integer32"
_WwpDhcpState_Object = MibTableColumn
wwpDhcpState = _WwpDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 4),
    _WwpDhcpState_Type()
)
wwpDhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpState.setStatus("current")


class _WwpDhcpLeaseTimeRequested_Type(Integer32):
    """Custom type wwpDhcpLeaseTimeRequested based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpLeaseTimeRequested_Type.__name__ = "Integer32"
_WwpDhcpLeaseTimeRequested_Object = MibTableColumn
wwpDhcpLeaseTimeRequested = _WwpDhcpLeaseTimeRequested_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 5),
    _WwpDhcpLeaseTimeRequested_Type()
)
wwpDhcpLeaseTimeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpLeaseTimeRequested.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpLeaseTimeRequested.setUnits("seconds")


class _WwpDhcpLeaseOffered_Type(Integer32):
    """Custom type wwpDhcpLeaseOffered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpLeaseOffered_Type.__name__ = "Integer32"
_WwpDhcpLeaseOffered_Object = MibTableColumn
wwpDhcpLeaseOffered = _WwpDhcpLeaseOffered_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 6),
    _WwpDhcpLeaseOffered_Type()
)
wwpDhcpLeaseOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpLeaseOffered.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpLeaseOffered.setUnits("seconds")


class _WwpDhcpLeaseRemaining_Type(Integer32):
    """Custom type wwpDhcpLeaseRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpLeaseRemaining_Type.__name__ = "Integer32"
_WwpDhcpLeaseRemaining_Object = MibTableColumn
wwpDhcpLeaseRemaining = _WwpDhcpLeaseRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 7),
    _WwpDhcpLeaseRemaining_Type()
)
wwpDhcpLeaseRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpLeaseRemaining.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpLeaseRemaining.setUnits("seconds")


class _WwpDhcpDiscoveryMsgInterval_Type(Integer32):
    """Custom type wwpDhcpDiscoveryMsgInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpDiscoveryMsgInterval_Type.__name__ = "Integer32"
_WwpDhcpDiscoveryMsgInterval_Object = MibTableColumn
wwpDhcpDiscoveryMsgInterval = _WwpDhcpDiscoveryMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 8),
    _WwpDhcpDiscoveryMsgInterval_Type()
)
wwpDhcpDiscoveryMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpDiscoveryMsgInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpDiscoveryMsgInterval.setUnits("seconds")


class _WwpDhcpRenewalTime_Type(Integer32):
    """Custom type wwpDhcpRenewalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpRenewalTime_Type.__name__ = "Integer32"
_WwpDhcpRenewalTime_Object = MibTableColumn
wwpDhcpRenewalTime = _WwpDhcpRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 9),
    _WwpDhcpRenewalTime_Type()
)
wwpDhcpRenewalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpRenewalTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpRenewalTime.setUnits("seconds")


class _WwpDhcpRebindingTime_Type(Integer32):
    """Custom type wwpDhcpRebindingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpRebindingTime_Type.__name__ = "Integer32"
_WwpDhcpRebindingTime_Object = MibTableColumn
wwpDhcpRebindingTime = _WwpDhcpRebindingTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 10),
    _WwpDhcpRebindingTime_Type()
)
wwpDhcpRebindingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpRebindingTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpRebindingTime.setUnits("seconds")
_WwpDhcpServerAddress_Type = IpAddress
_WwpDhcpServerAddress_Object = MibTableColumn
wwpDhcpServerAddress = _WwpDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 11),
    _WwpDhcpServerAddress_Type()
)
wwpDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDhcpServerAddress.setStatus("current")


class _WwpDhcpRenewLease_Type(TruthValue):
    """Custom type wwpDhcpRenewLease based on TruthValue"""


_WwpDhcpRenewLease_Object = MibTableColumn
wwpDhcpRenewLease = _WwpDhcpRenewLease_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 12),
    _WwpDhcpRenewLease_Type()
)
wwpDhcpRenewLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpRenewLease.setStatus("current")


class _WwpDhcpReleaseLease_Type(TruthValue):
    """Custom type wwpDhcpReleaseLease based on TruthValue"""


_WwpDhcpReleaseLease_Object = MibTableColumn
wwpDhcpReleaseLease = _WwpDhcpReleaseLease_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 13),
    _WwpDhcpReleaseLease_Type()
)
wwpDhcpReleaseLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpReleaseLease.setStatus("current")
_WwpMultiDhcpClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBNotificationPrefix = _WwpMultiDhcpClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 2)
)
_WwpMultiDhcpClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBNotifications = _WwpMultiDhcpClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 2, 0)
)
_WwpMultiDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBConformance = _WwpMultiDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 3)
)
_WwpMultiDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBCompliances = _WwpMultiDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 3, 1)
)
_WwpMultiDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpMultiDhcpClientMIBGroups = _WwpMultiDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 42, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-MULTI-DHCP-CLIENT-MIB",
    **{"wwpMultiDhcpClientMIB": wwpMultiDhcpClientMIB,
       "wwpMultiDhcpClientMIBObjects": wwpMultiDhcpClientMIBObjects,
       "wwpMultiDhcpClient": wwpMultiDhcpClient,
       "wwpMultiDhcpClientNumber": wwpMultiDhcpClientNumber,
       "wwpMultiDhcpClientTable": wwpMultiDhcpClientTable,
       "wwpMultiDhcpClientEntry": wwpMultiDhcpClientEntry,
       "wwpDhcpIfIndex": wwpDhcpIfIndex,
       "wwpDhcpIfName": wwpDhcpIfName,
       "wwpDhcpStatus": wwpDhcpStatus,
       "wwpDhcpState": wwpDhcpState,
       "wwpDhcpLeaseTimeRequested": wwpDhcpLeaseTimeRequested,
       "wwpDhcpLeaseOffered": wwpDhcpLeaseOffered,
       "wwpDhcpLeaseRemaining": wwpDhcpLeaseRemaining,
       "wwpDhcpDiscoveryMsgInterval": wwpDhcpDiscoveryMsgInterval,
       "wwpDhcpRenewalTime": wwpDhcpRenewalTime,
       "wwpDhcpRebindingTime": wwpDhcpRebindingTime,
       "wwpDhcpServerAddress": wwpDhcpServerAddress,
       "wwpDhcpRenewLease": wwpDhcpRenewLease,
       "wwpDhcpReleaseLease": wwpDhcpReleaseLease,
       "wwpMultiDhcpClientMIBNotificationPrefix": wwpMultiDhcpClientMIBNotificationPrefix,
       "wwpMultiDhcpClientMIBNotifications": wwpMultiDhcpClientMIBNotifications,
       "wwpMultiDhcpClientMIBConformance": wwpMultiDhcpClientMIBConformance,
       "wwpMultiDhcpClientMIBCompliances": wwpMultiDhcpClientMIBCompliances,
       "wwpMultiDhcpClientMIBGroups": wwpMultiDhcpClientMIBGroups}
)
