# SNMP MIB module (BAY-STACK-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-DHCP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:51 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackDhcpSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17)
)
bayStackDhcpSnoopingMib.setRevisions(
        ("2014-03-20 00:00",
         "2013-10-11 00:00",
         "2013-07-25 00:00",
         "2013-07-09 00:00",
         "2013-04-18 00:00",
         "2013-03-21 00:00",
         "2012-05-28 00:00",
         "2010-11-18 00:00",
         "2010-10-05 00:00",
         "2009-09-23 00:00",
         "2009-04-01 00:00",
         "2009-03-30 00:00",
         "2009-03-26 00:00",
         "2008-10-30 00:00",
         "2008-06-02 00:00",
         "2006-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsDhcpSnoopingNotifications_ObjectIdentity = ObjectIdentity
bsDhcpSnoopingNotifications = _BsDhcpSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0)
)
_BsDhcpSnoopingObjects_ObjectIdentity = ObjectIdentity
bsDhcpSnoopingObjects = _BsDhcpSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1)
)
_BsDhcpSnoopingScalars_ObjectIdentity = ObjectIdentity
bsDhcpSnoopingScalars = _BsDhcpSnoopingScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1)
)
_BsDhcpSnoopingEnabled_Type = TruthValue
_BsDhcpSnoopingEnabled_Object = MibScalar
bsDhcpSnoopingEnabled = _BsDhcpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1, 1),
    _BsDhcpSnoopingEnabled_Type()
)
bsDhcpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingEnabled.setStatus("current")
_BsDhcpSnoopingOption82Enabled_Type = TruthValue
_BsDhcpSnoopingOption82Enabled_Object = MibScalar
bsDhcpSnoopingOption82Enabled = _BsDhcpSnoopingOption82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1, 2),
    _BsDhcpSnoopingOption82Enabled_Type()
)
bsDhcpSnoopingOption82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingOption82Enabled.setStatus("current")
_BsDhcpSnoopingVlanTable_Object = MibTable
bsDhcpSnoopingVlanTable = _BsDhcpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2)
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingVlanTable.setStatus("current")
_BsDhcpSnoopingVlanEntry_Object = MibTableRow
bsDhcpSnoopingVlanEntry = _BsDhcpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1)
)
bsDhcpSnoopingVlanEntry.setIndexNames(
    (0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingVlanEntry.setStatus("current")
_BsDhcpSnoopingVlanId_Type = VlanIndex
_BsDhcpSnoopingVlanId_Object = MibTableColumn
bsDhcpSnoopingVlanId = _BsDhcpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 1),
    _BsDhcpSnoopingVlanId_Type()
)
bsDhcpSnoopingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDhcpSnoopingVlanId.setStatus("current")
_BsDhcpSnoopingVlanEnabled_Type = TruthValue
_BsDhcpSnoopingVlanEnabled_Object = MibTableColumn
bsDhcpSnoopingVlanEnabled = _BsDhcpSnoopingVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 2),
    _BsDhcpSnoopingVlanEnabled_Type()
)
bsDhcpSnoopingVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingVlanEnabled.setStatus("current")
_BsDhcpSnoopingVlanOption82Enabled_Type = TruthValue
_BsDhcpSnoopingVlanOption82Enabled_Object = MibTableColumn
bsDhcpSnoopingVlanOption82Enabled = _BsDhcpSnoopingVlanOption82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 3),
    _BsDhcpSnoopingVlanOption82Enabled_Type()
)
bsDhcpSnoopingVlanOption82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingVlanOption82Enabled.setStatus("current")
_BsDhcpSnoopingIfTable_Object = MibTable
bsDhcpSnoopingIfTable = _BsDhcpSnoopingIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3)
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingIfTable.setStatus("current")
_BsDhcpSnoopingIfEntry_Object = MibTableRow
bsDhcpSnoopingIfEntry = _BsDhcpSnoopingIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1)
)
bsDhcpSnoopingIfEntry.setIndexNames(
    (0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfIndex"),
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingIfEntry.setStatus("current")
_BsDhcpSnoopingIfIndex_Type = InterfaceIndex
_BsDhcpSnoopingIfIndex_Object = MibTableColumn
bsDhcpSnoopingIfIndex = _BsDhcpSnoopingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 1),
    _BsDhcpSnoopingIfIndex_Type()
)
bsDhcpSnoopingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDhcpSnoopingIfIndex.setStatus("current")
_BsDhcpSnoopingIfTrusted_Type = TruthValue
_BsDhcpSnoopingIfTrusted_Object = MibTableColumn
bsDhcpSnoopingIfTrusted = _BsDhcpSnoopingIfTrusted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 2),
    _BsDhcpSnoopingIfTrusted_Type()
)
bsDhcpSnoopingIfTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingIfTrusted.setStatus("current")
_BsDhcpSnoopingIfOption82SubscriberId_Type = DisplayString
_BsDhcpSnoopingIfOption82SubscriberId_Object = MibTableColumn
bsDhcpSnoopingIfOption82SubscriberId = _BsDhcpSnoopingIfOption82SubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 3),
    _BsDhcpSnoopingIfOption82SubscriberId_Type()
)
bsDhcpSnoopingIfOption82SubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingIfOption82SubscriberId.setStatus("current")
_BsDhcpSnoopingBindingTable_Object = MibTable
bsDhcpSnoopingBindingTable = _BsDhcpSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4)
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingTable.setStatus("current")
_BsDhcpSnoopingBindingEntry_Object = MibTableRow
bsDhcpSnoopingBindingEntry = _BsDhcpSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1)
)
bsDhcpSnoopingBindingEntry.setIndexNames(
    (0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingVlanId"),
    (0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingMacAddress"),
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingEntry.setStatus("current")
_BsDhcpSnoopingBindingVlanId_Type = VlanIndex
_BsDhcpSnoopingBindingVlanId_Object = MibTableColumn
bsDhcpSnoopingBindingVlanId = _BsDhcpSnoopingBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 1),
    _BsDhcpSnoopingBindingVlanId_Type()
)
bsDhcpSnoopingBindingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingVlanId.setStatus("current")
_BsDhcpSnoopingBindingMacAddress_Type = MacAddress
_BsDhcpSnoopingBindingMacAddress_Object = MibTableColumn
bsDhcpSnoopingBindingMacAddress = _BsDhcpSnoopingBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 2),
    _BsDhcpSnoopingBindingMacAddress_Type()
)
bsDhcpSnoopingBindingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingMacAddress.setStatus("current")
_BsDhcpSnoopingBindingAddressType_Type = InetAddressType
_BsDhcpSnoopingBindingAddressType_Object = MibTableColumn
bsDhcpSnoopingBindingAddressType = _BsDhcpSnoopingBindingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 3),
    _BsDhcpSnoopingBindingAddressType_Type()
)
bsDhcpSnoopingBindingAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingAddressType.setStatus("current")
_BsDhcpSnoopingBindingAddress_Type = InetAddress
_BsDhcpSnoopingBindingAddress_Object = MibTableColumn
bsDhcpSnoopingBindingAddress = _BsDhcpSnoopingBindingAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 4),
    _BsDhcpSnoopingBindingAddress_Type()
)
bsDhcpSnoopingBindingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingAddress.setStatus("current")
_BsDhcpSnoopingBindingInterface_Type = InterfaceIndex
_BsDhcpSnoopingBindingInterface_Object = MibTableColumn
bsDhcpSnoopingBindingInterface = _BsDhcpSnoopingBindingInterface_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 5),
    _BsDhcpSnoopingBindingInterface_Type()
)
bsDhcpSnoopingBindingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingInterface.setStatus("current")
_BsDhcpSnoopingBindingLeaseTime_Type = Unsigned32
_BsDhcpSnoopingBindingLeaseTime_Object = MibTableColumn
bsDhcpSnoopingBindingLeaseTime = _BsDhcpSnoopingBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 6),
    _BsDhcpSnoopingBindingLeaseTime_Type()
)
bsDhcpSnoopingBindingLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingLeaseTime.setUnits("seconds")
_BsDhcpSnoopingBindingRowStatus_Type = RowStatus
_BsDhcpSnoopingBindingRowStatus_Object = MibTableColumn
bsDhcpSnoopingBindingRowStatus = _BsDhcpSnoopingBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 7),
    _BsDhcpSnoopingBindingRowStatus_Type()
)
bsDhcpSnoopingBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingRowStatus.setStatus("current")
_BsDhcpSnoopingBindingTimeToExpiry_Type = Unsigned32
_BsDhcpSnoopingBindingTimeToExpiry_Object = MibTableColumn
bsDhcpSnoopingBindingTimeToExpiry = _BsDhcpSnoopingBindingTimeToExpiry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 8),
    _BsDhcpSnoopingBindingTimeToExpiry_Type()
)
bsDhcpSnoopingBindingTimeToExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingTimeToExpiry.setStatus("current")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingTimeToExpiry.setUnits("seconds")


class _BsDhcpSnoopingBindingSource_Type(Integer32):
    """Custom type bsDhcpSnoopingBindingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learned", 1),
          ("static", 2))
    )


_BsDhcpSnoopingBindingSource_Type.__name__ = "Integer32"
_BsDhcpSnoopingBindingSource_Object = MibTableColumn
bsDhcpSnoopingBindingSource = _BsDhcpSnoopingBindingSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 9),
    _BsDhcpSnoopingBindingSource_Type()
)
bsDhcpSnoopingBindingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingSource.setStatus("current")
_BsDhcpSnoopingNotificationObjects_ObjectIdentity = ObjectIdentity
bsDhcpSnoopingNotificationObjects = _BsDhcpSnoopingNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5)
)


class _BsDhcpSnoopingNotificationSourcePort_Type(InetPortNumber):
    """Custom type bsDhcpSnoopingNotificationSourcePort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BsDhcpSnoopingNotificationSourcePort_Type.__name__ = "InetPortNumber"
_BsDhcpSnoopingNotificationSourcePort_Object = MibScalar
bsDhcpSnoopingNotificationSourcePort = _BsDhcpSnoopingNotificationSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 1),
    _BsDhcpSnoopingNotificationSourcePort_Type()
)
bsDhcpSnoopingNotificationSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsDhcpSnoopingNotificationSourcePort.setStatus("current")


class _BsDhcpSnoopingNotificationMsgType_Type(Integer32):
    """Custom type bsDhcpSnoopingNotificationMsgType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAck", 5),
          ("dhcpDecline", 4),
          ("dhcpDiscover", 1),
          ("dhcpForceRenew", 9),
          ("dhcpInform", 8),
          ("dhcpLeaseActive", 13),
          ("dhcpLeaseQuery", 10),
          ("dhcpLeaseUnassigned", 11),
          ("dhcpLeaseUnknown", 12),
          ("dhcpNak", 6),
          ("dhcpOffer", 2),
          ("dhcpRelease", 7),
          ("dhcpRequest", 3))
    )


_BsDhcpSnoopingNotificationMsgType_Type.__name__ = "Integer32"
_BsDhcpSnoopingNotificationMsgType_Object = MibScalar
bsDhcpSnoopingNotificationMsgType = _BsDhcpSnoopingNotificationMsgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 2),
    _BsDhcpSnoopingNotificationMsgType_Type()
)
bsDhcpSnoopingNotificationMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsDhcpSnoopingNotificationMsgType.setStatus("current")
_BsDhcpSnoopingNotificationSourceMACAddr_Type = MacAddress
_BsDhcpSnoopingNotificationSourceMACAddr_Object = MibScalar
bsDhcpSnoopingNotificationSourceMACAddr = _BsDhcpSnoopingNotificationSourceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 3),
    _BsDhcpSnoopingNotificationSourceMACAddr_Type()
)
bsDhcpSnoopingNotificationSourceMACAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsDhcpSnoopingNotificationSourceMACAddr.setStatus("current")
_BsDhcpSnoopingNotificationClientMACAddr_Type = MacAddress
_BsDhcpSnoopingNotificationClientMACAddr_Object = MibScalar
bsDhcpSnoopingNotificationClientMACAddr = _BsDhcpSnoopingNotificationClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 4),
    _BsDhcpSnoopingNotificationClientMACAddr_Type()
)
bsDhcpSnoopingNotificationClientMACAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsDhcpSnoopingNotificationClientMACAddr.setStatus("current")
_BsDhcpSnoopingNotificationsBindingMacAddress_Type = MacAddress
_BsDhcpSnoopingNotificationsBindingMacAddress_Object = MibScalar
bsDhcpSnoopingNotificationsBindingMacAddress = _BsDhcpSnoopingNotificationsBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 5),
    _BsDhcpSnoopingNotificationsBindingMacAddress_Type()
)
bsDhcpSnoopingNotificationsBindingMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsDhcpSnoopingNotificationsBindingMacAddress.setStatus("current")
_BsDhcpSnoopingExtSave_ObjectIdentity = ObjectIdentity
bsDhcpSnoopingExtSave = _BsDhcpSnoopingExtSave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6)
)
_BsDhcpSnoopingExtSaveEnabled_Type = TruthValue
_BsDhcpSnoopingExtSaveEnabled_Object = MibScalar
bsDhcpSnoopingExtSaveEnabled = _BsDhcpSnoopingExtSaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 1),
    _BsDhcpSnoopingExtSaveEnabled_Type()
)
bsDhcpSnoopingExtSaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEnabled.setStatus("current")
_BsDhcpSnoopingExtSaveLastSyncTime_Type = DateAndTime
_BsDhcpSnoopingExtSaveLastSyncTime_Object = MibScalar
bsDhcpSnoopingExtSaveLastSyncTime = _BsDhcpSnoopingExtSaveLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 2),
    _BsDhcpSnoopingExtSaveLastSyncTime_Type()
)
bsDhcpSnoopingExtSaveLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveLastSyncTime.setStatus("current")
_BsDhcpSnoopingExtSaveSyncFlag_Type = TruthValue
_BsDhcpSnoopingExtSaveSyncFlag_Object = MibScalar
bsDhcpSnoopingExtSaveSyncFlag = _BsDhcpSnoopingExtSaveSyncFlag_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 3),
    _BsDhcpSnoopingExtSaveSyncFlag_Type()
)
bsDhcpSnoopingExtSaveSyncFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSyncFlag.setStatus("current")


class _BsDhcpSnoopingExtSaveFilename_Type(DisplayString):
    """Custom type bsDhcpSnoopingExtSaveFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsDhcpSnoopingExtSaveFilename_Type.__name__ = "DisplayString"
_BsDhcpSnoopingExtSaveFilename_Object = MibScalar
bsDhcpSnoopingExtSaveFilename = _BsDhcpSnoopingExtSaveFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 4),
    _BsDhcpSnoopingExtSaveFilename_Type()
)
bsDhcpSnoopingExtSaveFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveFilename.setStatus("current")
_BsDhcpSnoopingExtSaveTftpServerAddressType_Type = InetAddressType
_BsDhcpSnoopingExtSaveTftpServerAddressType_Object = MibScalar
bsDhcpSnoopingExtSaveTftpServerAddressType = _BsDhcpSnoopingExtSaveTftpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 5),
    _BsDhcpSnoopingExtSaveTftpServerAddressType_Type()
)
bsDhcpSnoopingExtSaveTftpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTftpServerAddressType.setStatus("current")
_BsDhcpSnoopingExtSaveTftpServerAddress_Type = InetAddress
_BsDhcpSnoopingExtSaveTftpServerAddress_Object = MibScalar
bsDhcpSnoopingExtSaveTftpServerAddress = _BsDhcpSnoopingExtSaveTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 6),
    _BsDhcpSnoopingExtSaveTftpServerAddress_Type()
)
bsDhcpSnoopingExtSaveTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTftpServerAddress.setStatus("current")


class _BsDhcpSnoopingExtSaveUsbTargetUnit_Type(Integer32):
    """Custom type bsDhcpSnoopingExtSaveUsbTargetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BsDhcpSnoopingExtSaveUsbTargetUnit_Type.__name__ = "Integer32"
_BsDhcpSnoopingExtSaveUsbTargetUnit_Object = MibScalar
bsDhcpSnoopingExtSaveUsbTargetUnit = _BsDhcpSnoopingExtSaveUsbTargetUnit_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 7),
    _BsDhcpSnoopingExtSaveUsbTargetUnit_Type()
)
bsDhcpSnoopingExtSaveUsbTargetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveUsbTargetUnit.setStatus("current")
_BsDhcpSnoopingExtSaveForceRestore_Type = Integer32
_BsDhcpSnoopingExtSaveForceRestore_Object = MibScalar
bsDhcpSnoopingExtSaveForceRestore = _BsDhcpSnoopingExtSaveForceRestore_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 8),
    _BsDhcpSnoopingExtSaveForceRestore_Type()
)
bsDhcpSnoopingExtSaveForceRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveForceRestore.setStatus("current")
_BsDhcpSnoopingExtSaveSftpServerAddressType_Type = InetAddressType
_BsDhcpSnoopingExtSaveSftpServerAddressType_Object = MibScalar
bsDhcpSnoopingExtSaveSftpServerAddressType = _BsDhcpSnoopingExtSaveSftpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 9),
    _BsDhcpSnoopingExtSaveSftpServerAddressType_Type()
)
bsDhcpSnoopingExtSaveSftpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSftpServerAddressType.setStatus("current")
_BsDhcpSnoopingExtSaveSftpServerAddress_Type = InetAddress
_BsDhcpSnoopingExtSaveSftpServerAddress_Object = MibScalar
bsDhcpSnoopingExtSaveSftpServerAddress = _BsDhcpSnoopingExtSaveSftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 10),
    _BsDhcpSnoopingExtSaveSftpServerAddress_Type()
)
bsDhcpSnoopingExtSaveSftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSftpServerAddress.setStatus("current")

# Managed Objects groups


# Notification objects

bsDhcpSnoopingBindingTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 1)
)
bsDhcpSnoopingBindingTableFull.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationClientMACAddr")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingBindingTableFull.setStatus(
        "current"
    )

bsDhcpSnoopingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 2)
)
bsDhcpSnoopingTrap.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourcePort"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationMsgType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourceMACAddr"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationClientMACAddr"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfTrusted"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingTrap.setStatus(
        "current"
    )

bsDhcpOption82MaxLengthExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 3)
)
if mibBuilder.loadTexts:
    bsDhcpOption82MaxLengthExceeded.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryMACConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 4)
)
bsDhcpSnoopingExtSaveEntryMACConflict.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryMACConflict.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryInvalidInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 5)
)
bsDhcpSnoopingExtSaveEntryInvalidInterface.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingInterface"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryInvalidInterface.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryLeaseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 6)
)
bsDhcpSnoopingExtSaveEntryLeaseExpired.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryLeaseExpired.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryParsingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 7)
)
bsDhcpSnoopingExtSaveEntryParsingFailure.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryParsingFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveNTP = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 8)
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveNTP.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveUSBSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 9)
)
bsDhcpSnoopingExtSaveUSBSyncSuccess.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveUSBSyncSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveTFTPSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 10)
)
bsDhcpSnoopingExtSaveTFTPSyncSuccess.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTFTPSyncSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveUSBSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 11)
)
bsDhcpSnoopingExtSaveUSBSyncFailure.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveUSBSyncFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveTFTPSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 12)
)
bsDhcpSnoopingExtSaveTFTPSyncFailure.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTFTPSyncFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveUSBRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 13)
)
bsDhcpSnoopingExtSaveUSBRestoreSuccess.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveUSBRestoreSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveTFTPRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 14)
)
bsDhcpSnoopingExtSaveTFTPRestoreSuccess.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTFTPRestoreSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveUSBRestoreFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 15)
)
bsDhcpSnoopingExtSaveUSBRestoreFailure.setObjects(
    ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit")
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveUSBRestoreFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveTFTPRestoreFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 16)
)
bsDhcpSnoopingExtSaveTFTPRestoreFailure.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveTFTPRestoreFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryInvalidVlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 17)
)
bsDhcpSnoopingExtSaveEntryInvalidVlan.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingVlanId"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryInvalidVlan.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveSFTPSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 18)
)
bsDhcpSnoopingExtSaveSFTPSyncSuccess.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSFTPSyncSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveSFTPSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 19)
)
bsDhcpSnoopingExtSaveSFTPSyncFailure.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSFTPSyncFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveSFTPRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 20)
)
bsDhcpSnoopingExtSaveSFTPRestoreSuccess.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSFTPRestoreSuccess.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveSFTPRestoreFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 21)
)
bsDhcpSnoopingExtSaveSFTPRestoreFailure.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveSFTPRestoreFailure.setStatus(
        "current"
    )

bsDhcpSnoopingExtSaveEntryIfTrustedConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 22)
)
bsDhcpSnoopingExtSaveEntryIfTrustedConflict.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfTrusted"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingExtSaveEntryIfTrustedConflict.setStatus(
        "current"
    )

bsDhcpSnoopingStaticEntryMACConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 23)
)
bsDhcpSnoopingStaticEntryMACConflict.setObjects(
      *(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourceMACAddr"),
        ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfIndex"))
)
if mibBuilder.loadTexts:
    bsDhcpSnoopingStaticEntryMACConflict.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-DHCP-SNOOPING-MIB",
    **{"bayStackDhcpSnoopingMib": bayStackDhcpSnoopingMib,
       "bsDhcpSnoopingNotifications": bsDhcpSnoopingNotifications,
       "bsDhcpSnoopingBindingTableFull": bsDhcpSnoopingBindingTableFull,
       "bsDhcpSnoopingTrap": bsDhcpSnoopingTrap,
       "bsDhcpOption82MaxLengthExceeded": bsDhcpOption82MaxLengthExceeded,
       "bsDhcpSnoopingExtSaveEntryMACConflict": bsDhcpSnoopingExtSaveEntryMACConflict,
       "bsDhcpSnoopingExtSaveEntryInvalidInterface": bsDhcpSnoopingExtSaveEntryInvalidInterface,
       "bsDhcpSnoopingExtSaveEntryLeaseExpired": bsDhcpSnoopingExtSaveEntryLeaseExpired,
       "bsDhcpSnoopingExtSaveEntryParsingFailure": bsDhcpSnoopingExtSaveEntryParsingFailure,
       "bsDhcpSnoopingExtSaveNTP": bsDhcpSnoopingExtSaveNTP,
       "bsDhcpSnoopingExtSaveUSBSyncSuccess": bsDhcpSnoopingExtSaveUSBSyncSuccess,
       "bsDhcpSnoopingExtSaveTFTPSyncSuccess": bsDhcpSnoopingExtSaveTFTPSyncSuccess,
       "bsDhcpSnoopingExtSaveUSBSyncFailure": bsDhcpSnoopingExtSaveUSBSyncFailure,
       "bsDhcpSnoopingExtSaveTFTPSyncFailure": bsDhcpSnoopingExtSaveTFTPSyncFailure,
       "bsDhcpSnoopingExtSaveUSBRestoreSuccess": bsDhcpSnoopingExtSaveUSBRestoreSuccess,
       "bsDhcpSnoopingExtSaveTFTPRestoreSuccess": bsDhcpSnoopingExtSaveTFTPRestoreSuccess,
       "bsDhcpSnoopingExtSaveUSBRestoreFailure": bsDhcpSnoopingExtSaveUSBRestoreFailure,
       "bsDhcpSnoopingExtSaveTFTPRestoreFailure": bsDhcpSnoopingExtSaveTFTPRestoreFailure,
       "bsDhcpSnoopingExtSaveEntryInvalidVlan": bsDhcpSnoopingExtSaveEntryInvalidVlan,
       "bsDhcpSnoopingExtSaveSFTPSyncSuccess": bsDhcpSnoopingExtSaveSFTPSyncSuccess,
       "bsDhcpSnoopingExtSaveSFTPSyncFailure": bsDhcpSnoopingExtSaveSFTPSyncFailure,
       "bsDhcpSnoopingExtSaveSFTPRestoreSuccess": bsDhcpSnoopingExtSaveSFTPRestoreSuccess,
       "bsDhcpSnoopingExtSaveSFTPRestoreFailure": bsDhcpSnoopingExtSaveSFTPRestoreFailure,
       "bsDhcpSnoopingExtSaveEntryIfTrustedConflict": bsDhcpSnoopingExtSaveEntryIfTrustedConflict,
       "bsDhcpSnoopingStaticEntryMACConflict": bsDhcpSnoopingStaticEntryMACConflict,
       "bsDhcpSnoopingObjects": bsDhcpSnoopingObjects,
       "bsDhcpSnoopingScalars": bsDhcpSnoopingScalars,
       "bsDhcpSnoopingEnabled": bsDhcpSnoopingEnabled,
       "bsDhcpSnoopingOption82Enabled": bsDhcpSnoopingOption82Enabled,
       "bsDhcpSnoopingVlanTable": bsDhcpSnoopingVlanTable,
       "bsDhcpSnoopingVlanEntry": bsDhcpSnoopingVlanEntry,
       "bsDhcpSnoopingVlanId": bsDhcpSnoopingVlanId,
       "bsDhcpSnoopingVlanEnabled": bsDhcpSnoopingVlanEnabled,
       "bsDhcpSnoopingVlanOption82Enabled": bsDhcpSnoopingVlanOption82Enabled,
       "bsDhcpSnoopingIfTable": bsDhcpSnoopingIfTable,
       "bsDhcpSnoopingIfEntry": bsDhcpSnoopingIfEntry,
       "bsDhcpSnoopingIfIndex": bsDhcpSnoopingIfIndex,
       "bsDhcpSnoopingIfTrusted": bsDhcpSnoopingIfTrusted,
       "bsDhcpSnoopingIfOption82SubscriberId": bsDhcpSnoopingIfOption82SubscriberId,
       "bsDhcpSnoopingBindingTable": bsDhcpSnoopingBindingTable,
       "bsDhcpSnoopingBindingEntry": bsDhcpSnoopingBindingEntry,
       "bsDhcpSnoopingBindingVlanId": bsDhcpSnoopingBindingVlanId,
       "bsDhcpSnoopingBindingMacAddress": bsDhcpSnoopingBindingMacAddress,
       "bsDhcpSnoopingBindingAddressType": bsDhcpSnoopingBindingAddressType,
       "bsDhcpSnoopingBindingAddress": bsDhcpSnoopingBindingAddress,
       "bsDhcpSnoopingBindingInterface": bsDhcpSnoopingBindingInterface,
       "bsDhcpSnoopingBindingLeaseTime": bsDhcpSnoopingBindingLeaseTime,
       "bsDhcpSnoopingBindingRowStatus": bsDhcpSnoopingBindingRowStatus,
       "bsDhcpSnoopingBindingTimeToExpiry": bsDhcpSnoopingBindingTimeToExpiry,
       "bsDhcpSnoopingBindingSource": bsDhcpSnoopingBindingSource,
       "bsDhcpSnoopingNotificationObjects": bsDhcpSnoopingNotificationObjects,
       "bsDhcpSnoopingNotificationSourcePort": bsDhcpSnoopingNotificationSourcePort,
       "bsDhcpSnoopingNotificationMsgType": bsDhcpSnoopingNotificationMsgType,
       "bsDhcpSnoopingNotificationSourceMACAddr": bsDhcpSnoopingNotificationSourceMACAddr,
       "bsDhcpSnoopingNotificationClientMACAddr": bsDhcpSnoopingNotificationClientMACAddr,
       "bsDhcpSnoopingNotificationsBindingMacAddress": bsDhcpSnoopingNotificationsBindingMacAddress,
       "bsDhcpSnoopingExtSave": bsDhcpSnoopingExtSave,
       "bsDhcpSnoopingExtSaveEnabled": bsDhcpSnoopingExtSaveEnabled,
       "bsDhcpSnoopingExtSaveLastSyncTime": bsDhcpSnoopingExtSaveLastSyncTime,
       "bsDhcpSnoopingExtSaveSyncFlag": bsDhcpSnoopingExtSaveSyncFlag,
       "bsDhcpSnoopingExtSaveFilename": bsDhcpSnoopingExtSaveFilename,
       "bsDhcpSnoopingExtSaveTftpServerAddressType": bsDhcpSnoopingExtSaveTftpServerAddressType,
       "bsDhcpSnoopingExtSaveTftpServerAddress": bsDhcpSnoopingExtSaveTftpServerAddress,
       "bsDhcpSnoopingExtSaveUsbTargetUnit": bsDhcpSnoopingExtSaveUsbTargetUnit,
       "bsDhcpSnoopingExtSaveForceRestore": bsDhcpSnoopingExtSaveForceRestore,
       "bsDhcpSnoopingExtSaveSftpServerAddressType": bsDhcpSnoopingExtSaveSftpServerAddressType,
       "bsDhcpSnoopingExtSaveSftpServerAddress": bsDhcpSnoopingExtSaveSftpServerAddress}
)
