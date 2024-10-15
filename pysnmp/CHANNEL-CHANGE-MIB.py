# SNMP MIB module (CHANNEL-CHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHANNEL-CHANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:32 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

channelChangeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsan_ObjectIdentity = ObjectIdentity
fsan = _Fsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_FsVdsl_ObjectIdentity = ObjectIdentity
fsVdsl = _FsVdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1)
)
_ChannelChangeMibObjects_ObjectIdentity = ObjectIdentity
channelChangeMibObjects = _ChannelChangeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1)
)
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1)
)
channelEntry.setIndexNames(
    (0, "CHANNEL-CHANGE-MIB", "channelId"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")
_ChannelId_Type = IpAddress
_ChannelId_Object = MibTableColumn
channelId = _ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1),
    _ChannelId_Type()
)
channelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelId.setStatus("current")


class _EntitlementIndex_Type(Integer32):
    """Custom type entitlementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EntitlementIndex_Type.__name__ = "Integer32"
_EntitlementIndex_Object = MibTableColumn
entitlementIndex = _EntitlementIndex_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 2),
    _EntitlementIndex_Type()
)
entitlementIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    entitlementIndex.setStatus("current")
_NetworkPortId_Type = InterfaceIndex
_NetworkPortId_Object = MibTableColumn
networkPortId = _NetworkPortId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 3),
    _NetworkPortId_Type()
)
networkPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkPortId.setStatus("current")


class _Vpi_Type(Integer32):
    """Custom type vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vpi_Type.__name__ = "Integer32"
_Vpi_Object = MibTableColumn
vpi = _Vpi_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4),
    _Vpi_Type()
)
vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpi.setStatus("current")


class _Vci_Type(Integer32):
    """Custom type vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_Vci_Type.__name__ = "Integer32"
_Vci_Object = MibTableColumn
vci = _Vci_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5),
    _Vci_Type()
)
vci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vci.setStatus("current")


class _ChannelAdminStatus_Type(Integer32):
    """Custom type channelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_ChannelAdminStatus_Type.__name__ = "Integer32"
_ChannelAdminStatus_Object = MibTableColumn
channelAdminStatus = _ChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 7),
    _ChannelAdminStatus_Type()
)
channelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelAdminStatus.setStatus("current")


class _ChannelRowStatus_Type(RowStatus):
    """Custom type channelRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ChannelRowStatus_Type.__name__ = "RowStatus"
_ChannelRowStatus_Object = MibTableColumn
channelRowStatus = _ChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 8),
    _ChannelRowStatus_Type()
)
channelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelRowStatus.setStatus("current")
_CustomerTable_Object = MibTable
customerTable = _CustomerTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    customerTable.setStatus("current")
_CustomerEntry_Object = MibTableRow
customerEntry = _CustomerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1)
)
customerEntry.setIndexNames(
    (0, "CHANNEL-CHANGE-MIB", "onuId"),
    (0, "CHANNEL-CHANGE-MIB", "customerPortId"),
)
if mibBuilder.loadTexts:
    customerEntry.setStatus("current")
_OnuId_Type = InterfaceIndexOrZero
_OnuId_Object = MibTableColumn
onuId = _OnuId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1),
    _OnuId_Type()
)
onuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuId.setStatus("current")
_CustomerPortId_Type = InterfaceIndex
_CustomerPortId_Object = MibTableColumn
customerPortId = _CustomerPortId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 2),
    _CustomerPortId_Type()
)
customerPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customerPortId.setStatus("current")
_MaxMulticastTraffic_Type = Integer32
_MaxMulticastTraffic_Object = MibTableColumn
maxMulticastTraffic = _MaxMulticastTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 3),
    _MaxMulticastTraffic_Type()
)
maxMulticastTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxMulticastTraffic.setStatus("current")
_MaxMulticastStreams_Type = Integer32
_MaxMulticastStreams_Object = MibTableColumn
maxMulticastStreams = _MaxMulticastStreams_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 4),
    _MaxMulticastStreams_Type()
)
maxMulticastStreams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxMulticastStreams.setStatus("current")


class _UntimedEntitlements1_Type(OctetString):
    """Custom type untimedEntitlements1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_UntimedEntitlements1_Type.__name__ = "OctetString"
_UntimedEntitlements1_Object = MibTableColumn
untimedEntitlements1 = _UntimedEntitlements1_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 5),
    _UntimedEntitlements1_Type()
)
untimedEntitlements1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    untimedEntitlements1.setStatus("current")


class _UntimedEntitlements2_Type(OctetString):
    """Custom type untimedEntitlements2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_UntimedEntitlements2_Type.__name__ = "OctetString"
_UntimedEntitlements2_Object = MibTableColumn
untimedEntitlements2 = _UntimedEntitlements2_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 6),
    _UntimedEntitlements2_Type()
)
untimedEntitlements2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    untimedEntitlements2.setStatus("current")
_GrantEntitlement_Type = IpAddress
_GrantEntitlement_Object = MibTableColumn
grantEntitlement = _GrantEntitlement_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 7),
    _GrantEntitlement_Type()
)
grantEntitlement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    grantEntitlement.setStatus("current")
_RevokeEntitlement_Type = IpAddress
_RevokeEntitlement_Object = MibTableColumn
revokeEntitlement = _RevokeEntitlement_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 8),
    _RevokeEntitlement_Type()
)
revokeEntitlement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    revokeEntitlement.setStatus("current")


class _CustomerAdminStatus_Type(Integer32):
    """Custom type customerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_CustomerAdminStatus_Type.__name__ = "Integer32"
_CustomerAdminStatus_Object = MibTableColumn
customerAdminStatus = _CustomerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 9),
    _CustomerAdminStatus_Type()
)
customerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customerAdminStatus.setStatus("current")


class _CustomerRowStatus_Type(RowStatus):
    """Custom type customerRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CustomerRowStatus_Type.__name__ = "RowStatus"
_CustomerRowStatus_Object = MibTableColumn
customerRowStatus = _CustomerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 2, 1, 10),
    _CustomerRowStatus_Type()
)
customerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customerRowStatus.setStatus("current")
_TimedEntitlementTable_Object = MibTable
timedEntitlementTable = _TimedEntitlementTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    timedEntitlementTable.setStatus("current")
_TimedEntitlementEntry_Object = MibTableRow
timedEntitlementEntry = _TimedEntitlementEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1)
)
timedEntitlementEntry.setIndexNames(
    (0, "CHANNEL-CHANGE-MIB", "timedEntitlementId"),
)
if mibBuilder.loadTexts:
    timedEntitlementEntry.setStatus("current")


class _TimedEntitlementId_Type(Integer32):
    """Custom type timedEntitlementId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimedEntitlementId_Type.__name__ = "Integer32"
_TimedEntitlementId_Object = MibTableColumn
timedEntitlementId = _TimedEntitlementId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1),
    _TimedEntitlementId_Type()
)
timedEntitlementId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timedEntitlementId.setStatus("current")
_TimedEntitlementChannelId_Type = IpAddress
_TimedEntitlementChannelId_Object = MibTableColumn
timedEntitlementChannelId = _TimedEntitlementChannelId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1, 2),
    _TimedEntitlementChannelId_Type()
)
timedEntitlementChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timedEntitlementChannelId.setStatus("current")


class _StartTime_Type(OctetString):
    """Custom type startTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StartTime_Type.__name__ = "OctetString"
_StartTime_Object = MibTableColumn
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1, 3),
    _StartTime_Type()
)
startTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    startTime.setStatus("current")


class _StopTime_Type(OctetString):
    """Custom type stopTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StopTime_Type.__name__ = "OctetString"
_StopTime_Object = MibTableColumn
stopTime = _StopTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1, 4),
    _StopTime_Type()
)
stopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stopTime.setStatus("current")


class _EntitlementRowStatus_Type(RowStatus):
    """Custom type entitlementRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_EntitlementRowStatus_Type.__name__ = "RowStatus"
_EntitlementRowStatus_Object = MibTableColumn
entitlementRowStatus = _EntitlementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 3, 1, 5),
    _EntitlementRowStatus_Type()
)
entitlementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    entitlementRowStatus.setStatus("current")
_CustomerTimedEntitlementTable_Object = MibTable
customerTimedEntitlementTable = _CustomerTimedEntitlementTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    customerTimedEntitlementTable.setStatus("current")
_CustomerTimedEntitlementEntry_Object = MibTableRow
customerTimedEntitlementEntry = _CustomerTimedEntitlementEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4, 1)
)
customerTimedEntitlementEntry.setIndexNames(
    (0, "CHANNEL-CHANGE-MIB", "custOnuId"),
    (0, "CHANNEL-CHANGE-MIB", "custPortId"),
    (0, "CHANNEL-CHANGE-MIB", "custTimedEntitlementId"),
)
if mibBuilder.loadTexts:
    customerTimedEntitlementEntry.setStatus("current")
_CustOnuId_Type = InterfaceIndexOrZero
_CustOnuId_Object = MibTableColumn
custOnuId = _CustOnuId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4, 1, 1),
    _CustOnuId_Type()
)
custOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custOnuId.setStatus("current")
_CustPortId_Type = InterfaceIndex
_CustPortId_Object = MibTableColumn
custPortId = _CustPortId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4, 1, 2),
    _CustPortId_Type()
)
custPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custPortId.setStatus("current")


class _CustTimedEntitlementId_Type(Integer32):
    """Custom type custTimedEntitlementId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustTimedEntitlementId_Type.__name__ = "Integer32"
_CustTimedEntitlementId_Object = MibTableColumn
custTimedEntitlementId = _CustTimedEntitlementId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4, 1, 3),
    _CustTimedEntitlementId_Type()
)
custTimedEntitlementId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custTimedEntitlementId.setStatus("current")


class _CustTimedEntitlementRowStatus_Type(RowStatus):
    """Custom type custTimedEntitlementRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CustTimedEntitlementRowStatus_Type.__name__ = "RowStatus"
_CustTimedEntitlementRowStatus_Object = MibTableColumn
custTimedEntitlementRowStatus = _CustTimedEntitlementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4),
    _CustTimedEntitlementRowStatus_Type()
)
custTimedEntitlementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custTimedEntitlementRowStatus.setStatus("current")
_RejectedOnuId_Type = InterfaceIndexOrZero
_RejectedOnuId_Object = MibScalar
rejectedOnuId = _RejectedOnuId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 5),
    _RejectedOnuId_Type()
)
rejectedOnuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rejectedOnuId.setStatus("current")
_RejectedCustomerPortId_Type = InterfaceIndex
_RejectedCustomerPortId_Object = MibScalar
rejectedCustomerPortId = _RejectedCustomerPortId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 6),
    _RejectedCustomerPortId_Type()
)
rejectedCustomerPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rejectedCustomerPortId.setStatus("current")


class _CaFailedNotificationStatus_Type(Integer32):
    """Custom type caFailedNotificationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CaFailedNotificationStatus_Type.__name__ = "Integer32"
_CaFailedNotificationStatus_Object = MibScalar
caFailedNotificationStatus = _CaFailedNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 1, 7),
    _CaFailedNotificationStatus_Type()
)
caFailedNotificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caFailedNotificationStatus.setStatus("current")
_ChannelChangeMibNotifications_ObjectIdentity = ObjectIdentity
channelChangeMibNotifications = _ChannelChangeMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 2)
)
_ChannelChangeMibNotificationPrefix_ObjectIdentity = ObjectIdentity
channelChangeMibNotificationPrefix = _ChannelChangeMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 2, 0)
)
_ChannelChangeMibConformance_ObjectIdentity = ObjectIdentity
channelChangeMibConformance = _ChannelChangeMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3)
)
_ChannelChangeMibCompliances_ObjectIdentity = ObjectIdentity
channelChangeMibCompliances = _ChannelChangeMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 1)
)
_ChannelChangeMibGroups_ObjectIdentity = ObjectIdentity
channelChangeMibGroups = _ChannelChangeMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2)
)

# Managed Objects groups

channelChangeBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 1)
)
channelChangeBasicGroup.setObjects(
      *(("CHANNEL-CHANGE-MIB", "channelId"),
        ("CHANNEL-CHANGE-MIB", "networkPortId"),
        ("CHANNEL-CHANGE-MIB", "vpi"),
        ("CHANNEL-CHANGE-MIB", "vci"),
        ("CHANNEL-CHANGE-MIB", "channelAdminStatus"),
        ("CHANNEL-CHANGE-MIB", "channelRowStatus"),
        ("CHANNEL-CHANGE-MIB", "onuId"),
        ("CHANNEL-CHANGE-MIB", "customerPortId"))
)
if mibBuilder.loadTexts:
    channelChangeBasicGroup.setStatus("current")

channelChangeCACGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 2)
)
channelChangeCACGroup.setObjects(
    ("CHANNEL-CHANGE-MIB", "maxMulticastTraffic")
)
if mibBuilder.loadTexts:
    channelChangeCACGroup.setStatus("current")

channelChangeBasicCAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 3)
)
channelChangeBasicCAGroup.setObjects(
      *(("CHANNEL-CHANGE-MIB", "maxMulticastStreams"),
        ("CHANNEL-CHANGE-MIB", "entitlementIndex"),
        ("CHANNEL-CHANGE-MIB", "untimedEntitlements1"),
        ("CHANNEL-CHANGE-MIB", "grantEntitlement"),
        ("CHANNEL-CHANGE-MIB", "revokeEntitlement"),
        ("CHANNEL-CHANGE-MIB", "rejectedOnuId"),
        ("CHANNEL-CHANGE-MIB", "rejectedCustomerPortId"),
        ("CHANNEL-CHANGE-MIB", "caFailedNotificationStatus"))
)
if mibBuilder.loadTexts:
    channelChangeBasicCAGroup.setStatus("current")

channelChangeCA4095ChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 4)
)
channelChangeCA4095ChannelsGroup.setObjects(
    ("CHANNEL-CHANGE-MIB", "untimedEntitlements2")
)
if mibBuilder.loadTexts:
    channelChangeCA4095ChannelsGroup.setStatus("current")

channelChangeCATimedEntitlementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 5)
)
channelChangeCATimedEntitlementsGroup.setObjects(
      *(("CHANNEL-CHANGE-MIB", "timedEntitlementId"),
        ("CHANNEL-CHANGE-MIB", "timedEntitlementChannelId"),
        ("CHANNEL-CHANGE-MIB", "startTime"),
        ("CHANNEL-CHANGE-MIB", "stopTime"),
        ("CHANNEL-CHANGE-MIB", "entitlementRowStatus"),
        ("CHANNEL-CHANGE-MIB", "custTimedEntitlementId"),
        ("CHANNEL-CHANGE-MIB", "custTimedEntitlementRowStatus"))
)
if mibBuilder.loadTexts:
    channelChangeCATimedEntitlementsGroup.setStatus("current")


# Notification objects

channelChangeCAFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 2, 0, 1)
)
channelChangeCAFailed.setObjects(
      *(("CHANNEL-CHANGE-MIB", "rejectedOnuId"),
        ("CHANNEL-CHANGE-MIB", "rejectedCustomerPortId"))
)
if mibBuilder.loadTexts:
    channelChangeCAFailed.setStatus(
        "current"
    )


# Notifications groups

channelChangeCANotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 2, 6)
)
channelChangeCANotificationsGroup.setObjects(
    ("CHANNEL-CHANGE-MIB", "channelChangeCAFailed")
)
if mibBuilder.loadTexts:
    channelChangeCANotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

channelChangeMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    channelChangeMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHANNEL-CHANGE-MIB",
    **{"fsan": fsan,
       "fsVdsl": fsVdsl,
       "channelChangeMib": channelChangeMib,
       "channelChangeMibObjects": channelChangeMibObjects,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelId": channelId,
       "entitlementIndex": entitlementIndex,
       "networkPortId": networkPortId,
       "vpi": vpi,
       "vci": vci,
       "channelAdminStatus": channelAdminStatus,
       "channelRowStatus": channelRowStatus,
       "customerTable": customerTable,
       "customerEntry": customerEntry,
       "onuId": onuId,
       "customerPortId": customerPortId,
       "maxMulticastTraffic": maxMulticastTraffic,
       "maxMulticastStreams": maxMulticastStreams,
       "untimedEntitlements1": untimedEntitlements1,
       "untimedEntitlements2": untimedEntitlements2,
       "grantEntitlement": grantEntitlement,
       "revokeEntitlement": revokeEntitlement,
       "customerAdminStatus": customerAdminStatus,
       "customerRowStatus": customerRowStatus,
       "timedEntitlementTable": timedEntitlementTable,
       "timedEntitlementEntry": timedEntitlementEntry,
       "timedEntitlementId": timedEntitlementId,
       "timedEntitlementChannelId": timedEntitlementChannelId,
       "startTime": startTime,
       "stopTime": stopTime,
       "entitlementRowStatus": entitlementRowStatus,
       "customerTimedEntitlementTable": customerTimedEntitlementTable,
       "customerTimedEntitlementEntry": customerTimedEntitlementEntry,
       "custOnuId": custOnuId,
       "custPortId": custPortId,
       "custTimedEntitlementId": custTimedEntitlementId,
       "custTimedEntitlementRowStatus": custTimedEntitlementRowStatus,
       "rejectedOnuId": rejectedOnuId,
       "rejectedCustomerPortId": rejectedCustomerPortId,
       "caFailedNotificationStatus": caFailedNotificationStatus,
       "channelChangeMibNotifications": channelChangeMibNotifications,
       "channelChangeMibNotificationPrefix": channelChangeMibNotificationPrefix,
       "channelChangeCAFailed": channelChangeCAFailed,
       "channelChangeMibConformance": channelChangeMibConformance,
       "channelChangeMibCompliances": channelChangeMibCompliances,
       "channelChangeMibCompliance": channelChangeMibCompliance,
       "channelChangeMibGroups": channelChangeMibGroups,
       "channelChangeBasicGroup": channelChangeBasicGroup,
       "channelChangeCACGroup": channelChangeCACGroup,
       "channelChangeBasicCAGroup": channelChangeBasicCAGroup,
       "channelChangeCA4095ChannelsGroup": channelChangeCA4095ChannelsGroup,
       "channelChangeCATimedEntitlementsGroup": channelChangeCATimedEntitlementsGroup,
       "channelChangeCANotificationsGroup": channelChangeCANotificationsGroup}
)
