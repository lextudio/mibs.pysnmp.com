# SNMP MIB module (HP-ICF-SMART-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SMART-LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:12 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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


# MODULE-IDENTITY

hpicfSmartLinkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96)
)
hpicfSmartLinkMIB.setRevisions(
        ("2013-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSmartLinkNotifications_ObjectIdentity = ObjectIdentity
hpicfSmartLinkNotifications = _HpicfSmartLinkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0)
)


class _HpicfSmartLinkNotifyGroupIndex_Type(Integer32):
    """Custom type hpicfSmartLinkNotifyGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfSmartLinkNotifyGroupIndex_Type.__name__ = "Integer32"
_HpicfSmartLinkNotifyGroupIndex_Object = MibScalar
hpicfSmartLinkNotifyGroupIndex = _HpicfSmartLinkNotifyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0, 1),
    _HpicfSmartLinkNotifyGroupIndex_Type()
)
hpicfSmartLinkNotifyGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfSmartLinkNotifyGroupIndex.setStatus("current")
_HpicfSmartLinkObjects_ObjectIdentity = ObjectIdentity
hpicfSmartLinkObjects = _HpicfSmartLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1)
)
_HpicfSmartLinkFlushStatistics_ObjectIdentity = ObjectIdentity
hpicfSmartLinkFlushStatistics = _HpicfSmartLinkFlushStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1)
)
_HpicfSmartLinkLastFlushTime_Type = DateAndTime
_HpicfSmartLinkLastFlushTime_Object = MibScalar
hpicfSmartLinkLastFlushTime = _HpicfSmartLinkLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 1),
    _HpicfSmartLinkLastFlushTime_Type()
)
hpicfSmartLinkLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkLastFlushTime.setStatus("current")
_HpicfSmartLinkTotalFlushPktsRx_Type = Counter64
_HpicfSmartLinkTotalFlushPktsRx_Object = MibScalar
hpicfSmartLinkTotalFlushPktsRx = _HpicfSmartLinkTotalFlushPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 2),
    _HpicfSmartLinkTotalFlushPktsRx_Type()
)
hpicfSmartLinkTotalFlushPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkTotalFlushPktsRx.setStatus("current")


class _HpicfSmartLinkLastFlushPort_Type(Integer32):
    """Custom type hpicfSmartLinkLastFlushPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfSmartLinkLastFlushPort_Type.__name__ = "Integer32"
_HpicfSmartLinkLastFlushPort_Object = MibScalar
hpicfSmartLinkLastFlushPort = _HpicfSmartLinkLastFlushPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 3),
    _HpicfSmartLinkLastFlushPort_Type()
)
hpicfSmartLinkLastFlushPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkLastFlushPort.setStatus("current")
_HpicfSmartLinkLastFlushDeviceId_Type = MacAddress
_HpicfSmartLinkLastFlushDeviceId_Object = MibScalar
hpicfSmartLinkLastFlushDeviceId = _HpicfSmartLinkLastFlushDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 4),
    _HpicfSmartLinkLastFlushDeviceId_Type()
)
hpicfSmartLinkLastFlushDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkLastFlushDeviceId.setStatus("current")


class _HpicfSmartLinkLastFlushVlan_Type(VlanIndex):
    """Custom type hpicfSmartLinkLastFlushVlan based on VlanIndex"""
    defaultValue = 0


_HpicfSmartLinkLastFlushVlan_Object = MibScalar
hpicfSmartLinkLastFlushVlan = _HpicfSmartLinkLastFlushVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 5),
    _HpicfSmartLinkLastFlushVlan_Type()
)
hpicfSmartLinkLastFlushVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkLastFlushVlan.setStatus("current")


class _HpicfSmartLinkResetFlushStatistics_Type(TruthValue):
    """Custom type hpicfSmartLinkResetFlushStatistics based on TruthValue"""


_HpicfSmartLinkResetFlushStatistics_Object = MibScalar
hpicfSmartLinkResetFlushStatistics = _HpicfSmartLinkResetFlushStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 2),
    _HpicfSmartLinkResetFlushStatistics_Type()
)
hpicfSmartLinkResetFlushStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSmartLinkResetFlushStatistics.setStatus("current")
_HpicfSmartLinkGroupTable_Object = MibTable
hpicfSmartLinkGroupTable = _HpicfSmartLinkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupTable.setStatus("current")
_HpicfSmartLinkGroupEntry_Object = MibTableRow
hpicfSmartLinkGroupEntry = _HpicfSmartLinkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1)
)
hpicfSmartLinkGroupEntry.setIndexNames(
    (0, "HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupIndex"),
)
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupEntry.setStatus("current")


class _HpicfSmartLinkGroupIndex_Type(Integer32):
    """Custom type hpicfSmartLinkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfSmartLinkGroupIndex_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupIndex_Object = MibTableColumn
hpicfSmartLinkGroupIndex = _HpicfSmartLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 1),
    _HpicfSmartLinkGroupIndex_Type()
)
hpicfSmartLinkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupIndex.setStatus("current")


class _HpicfSmartLinkGroupMasterPort_Type(Integer32):
    """Custom type hpicfSmartLinkGroupMasterPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfSmartLinkGroupMasterPort_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupMasterPort_Object = MibTableColumn
hpicfSmartLinkGroupMasterPort = _HpicfSmartLinkGroupMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 2),
    _HpicfSmartLinkGroupMasterPort_Type()
)
hpicfSmartLinkGroupMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupMasterPort.setStatus("current")


class _HpicfSmartLinkGroupSlavePort_Type(Integer32):
    """Custom type hpicfSmartLinkGroupSlavePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfSmartLinkGroupSlavePort_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupSlavePort_Object = MibTableColumn
hpicfSmartLinkGroupSlavePort = _HpicfSmartLinkGroupSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 3),
    _HpicfSmartLinkGroupSlavePort_Type()
)
hpicfSmartLinkGroupSlavePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupSlavePort.setStatus("current")


class _HpicfSmartLinkGroupSendControlVlan_Type(VlanIndex):
    """Custom type hpicfSmartLinkGroupSendControlVlan based on VlanIndex"""
    defaultValue = 1


_HpicfSmartLinkGroupSendControlVlan_Object = MibTableColumn
hpicfSmartLinkGroupSendControlVlan = _HpicfSmartLinkGroupSendControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 4),
    _HpicfSmartLinkGroupSendControlVlan_Type()
)
hpicfSmartLinkGroupSendControlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupSendControlVlan.setStatus("current")


class _HpicfSmartLinkGroupPreemptionMode_Type(Integer32):
    """Custom type hpicfSmartLinkGroupPreemptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("role", 2))
    )


_HpicfSmartLinkGroupPreemptionMode_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupPreemptionMode_Object = MibTableColumn
hpicfSmartLinkGroupPreemptionMode = _HpicfSmartLinkGroupPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 5),
    _HpicfSmartLinkGroupPreemptionMode_Type()
)
hpicfSmartLinkGroupPreemptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupPreemptionMode.setStatus("current")


class _HpicfSmartLinkGroupPreemptionDelay_Type(Integer32):
    """Custom type hpicfSmartLinkGroupPreemptionDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HpicfSmartLinkGroupPreemptionDelay_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupPreemptionDelay_Object = MibTableColumn
hpicfSmartLinkGroupPreemptionDelay = _HpicfSmartLinkGroupPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 6),
    _HpicfSmartLinkGroupPreemptionDelay_Type()
)
hpicfSmartLinkGroupPreemptionDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupPreemptionDelay.setStatus("current")


class _HpicfSmartLinkGroupProtectedVlan1k_Type(OctetString):
    """Custom type hpicfSmartLinkGroupProtectedVlan1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkGroupProtectedVlan1k_Type.__name__ = "OctetString"
_HpicfSmartLinkGroupProtectedVlan1k_Object = MibTableColumn
hpicfSmartLinkGroupProtectedVlan1k = _HpicfSmartLinkGroupProtectedVlan1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 7),
    _HpicfSmartLinkGroupProtectedVlan1k_Type()
)
hpicfSmartLinkGroupProtectedVlan1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupProtectedVlan1k.setStatus("current")


class _HpicfSmartLinkGroupProtectedVlan2k_Type(OctetString):
    """Custom type hpicfSmartLinkGroupProtectedVlan2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkGroupProtectedVlan2k_Type.__name__ = "OctetString"
_HpicfSmartLinkGroupProtectedVlan2k_Object = MibTableColumn
hpicfSmartLinkGroupProtectedVlan2k = _HpicfSmartLinkGroupProtectedVlan2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 8),
    _HpicfSmartLinkGroupProtectedVlan2k_Type()
)
hpicfSmartLinkGroupProtectedVlan2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupProtectedVlan2k.setStatus("current")


class _HpicfSmartLinkGroupProtectedVlan3k_Type(OctetString):
    """Custom type hpicfSmartLinkGroupProtectedVlan3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkGroupProtectedVlan3k_Type.__name__ = "OctetString"
_HpicfSmartLinkGroupProtectedVlan3k_Object = MibTableColumn
hpicfSmartLinkGroupProtectedVlan3k = _HpicfSmartLinkGroupProtectedVlan3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 9),
    _HpicfSmartLinkGroupProtectedVlan3k_Type()
)
hpicfSmartLinkGroupProtectedVlan3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupProtectedVlan3k.setStatus("current")


class _HpicfSmartLinkGroupProtectedVlan4k_Type(OctetString):
    """Custom type hpicfSmartLinkGroupProtectedVlan4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkGroupProtectedVlan4k_Type.__name__ = "OctetString"
_HpicfSmartLinkGroupProtectedVlan4k_Object = MibTableColumn
hpicfSmartLinkGroupProtectedVlan4k = _HpicfSmartLinkGroupProtectedVlan4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 10),
    _HpicfSmartLinkGroupProtectedVlan4k_Type()
)
hpicfSmartLinkGroupProtectedVlan4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupProtectedVlan4k.setStatus("current")


class _HpicfSmartLinkGroupTrapControl_Type(TruthValue):
    """Custom type hpicfSmartLinkGroupTrapControl based on TruthValue"""


_HpicfSmartLinkGroupTrapControl_Object = MibTableColumn
hpicfSmartLinkGroupTrapControl = _HpicfSmartLinkGroupTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 11),
    _HpicfSmartLinkGroupTrapControl_Type()
)
hpicfSmartLinkGroupTrapControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupTrapControl.setStatus("current")


class _HpicfSmartLinkGroupClearStats_Type(TruthValue):
    """Custom type hpicfSmartLinkGroupClearStats based on TruthValue"""


_HpicfSmartLinkGroupClearStats_Object = MibTableColumn
hpicfSmartLinkGroupClearStats = _HpicfSmartLinkGroupClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 12),
    _HpicfSmartLinkGroupClearStats_Type()
)
hpicfSmartLinkGroupClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupClearStats.setStatus("current")
_HpicfSmartLinkGroupRowStatus_Type = RowStatus
_HpicfSmartLinkGroupRowStatus_Object = MibTableColumn
hpicfSmartLinkGroupRowStatus = _HpicfSmartLinkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 13),
    _HpicfSmartLinkGroupRowStatus_Type()
)
hpicfSmartLinkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupRowStatus.setStatus("current")
_HpicfSmartLinkExtendedGroupTable_Object = MibTable
hpicfSmartLinkExtendedGroupTable = _HpicfSmartLinkExtendedGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfSmartLinkExtendedGroupTable.setStatus("current")
_HpicfSmartLinkExtendedGroupEntry_Object = MibTableRow
hpicfSmartLinkExtendedGroupEntry = _HpicfSmartLinkExtendedGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfSmartLinkExtendedGroupEntry.setStatus("current")


class _HpicfSmartLinkGroupMasterPortState_Type(Integer32):
    """Custom type hpicfSmartLinkGroupMasterPortState based on Integer32"""
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
        *(("active", 2),
          ("down", 4),
          ("standby", 3),
          ("uninitialized", 1))
    )


_HpicfSmartLinkGroupMasterPortState_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupMasterPortState_Object = MibTableColumn
hpicfSmartLinkGroupMasterPortState = _HpicfSmartLinkGroupMasterPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 1),
    _HpicfSmartLinkGroupMasterPortState_Type()
)
hpicfSmartLinkGroupMasterPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupMasterPortState.setStatus("current")


class _HpicfSmartLinkGroupSlavePortState_Type(Integer32):
    """Custom type hpicfSmartLinkGroupSlavePortState based on Integer32"""
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
        *(("active", 2),
          ("down", 4),
          ("standby", 3),
          ("uninitialized", 1))
    )


_HpicfSmartLinkGroupSlavePortState_Type.__name__ = "Integer32"
_HpicfSmartLinkGroupSlavePortState_Object = MibTableColumn
hpicfSmartLinkGroupSlavePortState = _HpicfSmartLinkGroupSlavePortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 2),
    _HpicfSmartLinkGroupSlavePortState_Type()
)
hpicfSmartLinkGroupSlavePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupSlavePortState.setStatus("current")
_HpicfSmartLinkMasterFlushPktTx_Type = Counter64
_HpicfSmartLinkMasterFlushPktTx_Object = MibTableColumn
hpicfSmartLinkMasterFlushPktTx = _HpicfSmartLinkMasterFlushPktTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 3),
    _HpicfSmartLinkMasterFlushPktTx_Type()
)
hpicfSmartLinkMasterFlushPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkMasterFlushPktTx.setStatus("current")
_HpicfSmartLinkMasterFlushPktLastUpdate_Type = DateAndTime
_HpicfSmartLinkMasterFlushPktLastUpdate_Object = MibTableColumn
hpicfSmartLinkMasterFlushPktLastUpdate = _HpicfSmartLinkMasterFlushPktLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 4),
    _HpicfSmartLinkMasterFlushPktLastUpdate_Type()
)
hpicfSmartLinkMasterFlushPktLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkMasterFlushPktLastUpdate.setStatus("current")
_HpicfSmartLinkSlaveFlushPktTx_Type = Counter64
_HpicfSmartLinkSlaveFlushPktTx_Object = MibTableColumn
hpicfSmartLinkSlaveFlushPktTx = _HpicfSmartLinkSlaveFlushPktTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 5),
    _HpicfSmartLinkSlaveFlushPktTx_Type()
)
hpicfSmartLinkSlaveFlushPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkSlaveFlushPktTx.setStatus("current")
_HpicfSmartLinkSlaveFlushPktLastUpdate_Type = DateAndTime
_HpicfSmartLinkSlaveFlushPktLastUpdate_Object = MibTableColumn
hpicfSmartLinkSlaveFlushPktLastUpdate = _HpicfSmartLinkSlaveFlushPktLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 6),
    _HpicfSmartLinkSlaveFlushPktLastUpdate_Type()
)
hpicfSmartLinkSlaveFlushPktLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSmartLinkSlaveFlushPktLastUpdate.setStatus("current")
_HpicfSmartLinkPortTable_Object = MibTable
hpicfSmartLinkPortTable = _HpicfSmartLinkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfSmartLinkPortTable.setStatus("current")
_HpicfSmartLinkPortEntry_Object = MibTableRow
hpicfSmartLinkPortEntry = _HpicfSmartLinkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1)
)
hpicfSmartLinkPortEntry.setIndexNames(
    (0, "HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfSmartLinkPortEntry.setStatus("current")


class _HpicfSmartLinkPortIndex_Type(Integer32):
    """Custom type hpicfSmartLinkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfSmartLinkPortIndex_Type.__name__ = "Integer32"
_HpicfSmartLinkPortIndex_Object = MibTableColumn
hpicfSmartLinkPortIndex = _HpicfSmartLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 1),
    _HpicfSmartLinkPortIndex_Type()
)
hpicfSmartLinkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSmartLinkPortIndex.setStatus("current")


class _HpicfSmartLinkRecvControlVlans1k_Type(OctetString):
    """Custom type hpicfSmartLinkRecvControlVlans1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkRecvControlVlans1k_Type.__name__ = "OctetString"
_HpicfSmartLinkRecvControlVlans1k_Object = MibTableColumn
hpicfSmartLinkRecvControlVlans1k = _HpicfSmartLinkRecvControlVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 2),
    _HpicfSmartLinkRecvControlVlans1k_Type()
)
hpicfSmartLinkRecvControlVlans1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkRecvControlVlans1k.setStatus("current")


class _HpicfSmartLinkRecvControlVlans2k_Type(OctetString):
    """Custom type hpicfSmartLinkRecvControlVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkRecvControlVlans2k_Type.__name__ = "OctetString"
_HpicfSmartLinkRecvControlVlans2k_Object = MibTableColumn
hpicfSmartLinkRecvControlVlans2k = _HpicfSmartLinkRecvControlVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 3),
    _HpicfSmartLinkRecvControlVlans2k_Type()
)
hpicfSmartLinkRecvControlVlans2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkRecvControlVlans2k.setStatus("current")


class _HpicfSmartLinkRecvControlVlans3k_Type(OctetString):
    """Custom type hpicfSmartLinkRecvControlVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkRecvControlVlans3k_Type.__name__ = "OctetString"
_HpicfSmartLinkRecvControlVlans3k_Object = MibTableColumn
hpicfSmartLinkRecvControlVlans3k = _HpicfSmartLinkRecvControlVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 4),
    _HpicfSmartLinkRecvControlVlans3k_Type()
)
hpicfSmartLinkRecvControlVlans3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkRecvControlVlans3k.setStatus("current")


class _HpicfSmartLinkRecvControlVlans4k_Type(OctetString):
    """Custom type hpicfSmartLinkRecvControlVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfSmartLinkRecvControlVlans4k_Type.__name__ = "OctetString"
_HpicfSmartLinkRecvControlVlans4k_Object = MibTableColumn
hpicfSmartLinkRecvControlVlans4k = _HpicfSmartLinkRecvControlVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 5),
    _HpicfSmartLinkRecvControlVlans4k_Type()
)
hpicfSmartLinkRecvControlVlans4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkRecvControlVlans4k.setStatus("current")
_HpicfSmartLinkPortRowStatus_Type = RowStatus
_HpicfSmartLinkPortRowStatus_Object = MibTableColumn
hpicfSmartLinkPortRowStatus = _HpicfSmartLinkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 6),
    _HpicfSmartLinkPortRowStatus_Type()
)
hpicfSmartLinkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSmartLinkPortRowStatus.setStatus("current")
_HpicfSmartLinkConformance_ObjectIdentity = ObjectIdentity
hpicfSmartLinkConformance = _HpicfSmartLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2)
)
_HpicfSmartLinkConformanceGroups_ObjectIdentity = ObjectIdentity
hpicfSmartLinkConformanceGroups = _HpicfSmartLinkConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1)
)
_HpicfSmartLinkCompliances_ObjectIdentity = ObjectIdentity
hpicfSmartLinkCompliances = _HpicfSmartLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 2)
)
hpicfSmartLinkGroupEntry.registerAugmentions(
    ("HP-ICF-SMART-LINK-MIB",
     "hpicfSmartLinkExtendedGroupEntry")
)
hpicfSmartLinkExtendedGroupEntry.setIndexNames(*hpicfSmartLinkGroupEntry.getIndexNames())

# Managed Objects groups

hpicfSmartLinkGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 1)
)
hpicfSmartLinkGlobalGroup.setObjects(
      *(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkTotalFlushPktsRx"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushPort"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushTime"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushDeviceId"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushVlan"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkResetFlushStatistics"))
)
if mibBuilder.loadTexts:
    hpicfSmartLinkGlobalGroup.setStatus("current")

hpicfSmartLinkGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 2)
)
hpicfSmartLinkGroupsGroup.setObjects(
      *(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPort"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePort"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSendControlVlan"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupPreemptionMode"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupPreemptionDelay"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan1k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan2k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan3k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan4k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupTrapControl"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupClearStats"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPortState"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePortState"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkMasterFlushPktTx"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkMasterFlushPktLastUpdate"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkSlaveFlushPktTx"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkSlaveFlushPktLastUpdate"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSmartLinkGroupsGroup.setStatus("current")

hpicfSmartLinkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 3)
)
hpicfSmartLinkPortGroup.setObjects(
      *(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans1k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans2k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans3k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans4k"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSmartLinkPortGroup.setStatus("current")

hpicfSmartLinkNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 4)
)
hpicfSmartLinkNotificationObjectsGroup.setObjects(
    ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotifyGroupIndex")
)
if mibBuilder.loadTexts:
    hpicfSmartLinkNotificationObjectsGroup.setStatus("current")


# Notification objects

hpicfSmartLinkPortStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0, 2)
)
hpicfSmartLinkPortStateChangeNotification.setObjects(
      *(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotifyGroupIndex"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPortState"),
        ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePortState"))
)
if mibBuilder.loadTexts:
    hpicfSmartLinkPortStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups

hpicfSmartLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 5)
)
hpicfSmartLinkNotificationGroup.setObjects(
    ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortStateChangeNotification")
)
if mibBuilder.loadTexts:
    hpicfSmartLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfSmartLinkCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSmartLinkCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SMART-LINK-MIB",
    **{"hpicfSmartLinkMIB": hpicfSmartLinkMIB,
       "hpicfSmartLinkNotifications": hpicfSmartLinkNotifications,
       "hpicfSmartLinkNotifyGroupIndex": hpicfSmartLinkNotifyGroupIndex,
       "hpicfSmartLinkPortStateChangeNotification": hpicfSmartLinkPortStateChangeNotification,
       "hpicfSmartLinkObjects": hpicfSmartLinkObjects,
       "hpicfSmartLinkFlushStatistics": hpicfSmartLinkFlushStatistics,
       "hpicfSmartLinkLastFlushTime": hpicfSmartLinkLastFlushTime,
       "hpicfSmartLinkTotalFlushPktsRx": hpicfSmartLinkTotalFlushPktsRx,
       "hpicfSmartLinkLastFlushPort": hpicfSmartLinkLastFlushPort,
       "hpicfSmartLinkLastFlushDeviceId": hpicfSmartLinkLastFlushDeviceId,
       "hpicfSmartLinkLastFlushVlan": hpicfSmartLinkLastFlushVlan,
       "hpicfSmartLinkResetFlushStatistics": hpicfSmartLinkResetFlushStatistics,
       "hpicfSmartLinkGroupTable": hpicfSmartLinkGroupTable,
       "hpicfSmartLinkGroupEntry": hpicfSmartLinkGroupEntry,
       "hpicfSmartLinkGroupIndex": hpicfSmartLinkGroupIndex,
       "hpicfSmartLinkGroupMasterPort": hpicfSmartLinkGroupMasterPort,
       "hpicfSmartLinkGroupSlavePort": hpicfSmartLinkGroupSlavePort,
       "hpicfSmartLinkGroupSendControlVlan": hpicfSmartLinkGroupSendControlVlan,
       "hpicfSmartLinkGroupPreemptionMode": hpicfSmartLinkGroupPreemptionMode,
       "hpicfSmartLinkGroupPreemptionDelay": hpicfSmartLinkGroupPreemptionDelay,
       "hpicfSmartLinkGroupProtectedVlan1k": hpicfSmartLinkGroupProtectedVlan1k,
       "hpicfSmartLinkGroupProtectedVlan2k": hpicfSmartLinkGroupProtectedVlan2k,
       "hpicfSmartLinkGroupProtectedVlan3k": hpicfSmartLinkGroupProtectedVlan3k,
       "hpicfSmartLinkGroupProtectedVlan4k": hpicfSmartLinkGroupProtectedVlan4k,
       "hpicfSmartLinkGroupTrapControl": hpicfSmartLinkGroupTrapControl,
       "hpicfSmartLinkGroupClearStats": hpicfSmartLinkGroupClearStats,
       "hpicfSmartLinkGroupRowStatus": hpicfSmartLinkGroupRowStatus,
       "hpicfSmartLinkExtendedGroupTable": hpicfSmartLinkExtendedGroupTable,
       "hpicfSmartLinkExtendedGroupEntry": hpicfSmartLinkExtendedGroupEntry,
       "hpicfSmartLinkGroupMasterPortState": hpicfSmartLinkGroupMasterPortState,
       "hpicfSmartLinkGroupSlavePortState": hpicfSmartLinkGroupSlavePortState,
       "hpicfSmartLinkMasterFlushPktTx": hpicfSmartLinkMasterFlushPktTx,
       "hpicfSmartLinkMasterFlushPktLastUpdate": hpicfSmartLinkMasterFlushPktLastUpdate,
       "hpicfSmartLinkSlaveFlushPktTx": hpicfSmartLinkSlaveFlushPktTx,
       "hpicfSmartLinkSlaveFlushPktLastUpdate": hpicfSmartLinkSlaveFlushPktLastUpdate,
       "hpicfSmartLinkPortTable": hpicfSmartLinkPortTable,
       "hpicfSmartLinkPortEntry": hpicfSmartLinkPortEntry,
       "hpicfSmartLinkPortIndex": hpicfSmartLinkPortIndex,
       "hpicfSmartLinkRecvControlVlans1k": hpicfSmartLinkRecvControlVlans1k,
       "hpicfSmartLinkRecvControlVlans2k": hpicfSmartLinkRecvControlVlans2k,
       "hpicfSmartLinkRecvControlVlans3k": hpicfSmartLinkRecvControlVlans3k,
       "hpicfSmartLinkRecvControlVlans4k": hpicfSmartLinkRecvControlVlans4k,
       "hpicfSmartLinkPortRowStatus": hpicfSmartLinkPortRowStatus,
       "hpicfSmartLinkConformance": hpicfSmartLinkConformance,
       "hpicfSmartLinkConformanceGroups": hpicfSmartLinkConformanceGroups,
       "hpicfSmartLinkGlobalGroup": hpicfSmartLinkGlobalGroup,
       "hpicfSmartLinkGroupsGroup": hpicfSmartLinkGroupsGroup,
       "hpicfSmartLinkPortGroup": hpicfSmartLinkPortGroup,
       "hpicfSmartLinkNotificationObjectsGroup": hpicfSmartLinkNotificationObjectsGroup,
       "hpicfSmartLinkNotificationGroup": hpicfSmartLinkNotificationGroup,
       "hpicfSmartLinkCompliances": hpicfSmartLinkCompliances,
       "hpicfSmartLinkCompliance1": hpicfSmartLinkCompliance1}
)
