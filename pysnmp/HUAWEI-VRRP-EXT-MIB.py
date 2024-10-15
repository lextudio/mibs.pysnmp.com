# SNMP MIB module (HUAWEI-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:38 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectGroup,
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
    "ObjectGroup",
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(VrId,
 vrrpOperMasterIpAddr,
 vrrpOperState) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId",
    "vrrpOperMasterIpAddr",
    "vrrpOperState")


# MODULE-IDENTITY

hwVrrpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVrrpExtGlobal_ObjectIdentity = ObjectIdentity
hwVrrpExtGlobal = _HwVrrpExtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1)
)


class _HwVrrpExtFreeArpInterval_Type(Integer32):
    """Custom type hwVrrpExtFreeArpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 1200),
    )


_HwVrrpExtFreeArpInterval_Type.__name__ = "Integer32"
_HwVrrpExtFreeArpInterval_Object = MibScalar
hwVrrpExtFreeArpInterval = _HwVrrpExtFreeArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 1),
    _HwVrrpExtFreeArpInterval_Type()
)
hwVrrpExtFreeArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtFreeArpInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwVrrpExtFreeArpInterval.setUnits("seconds")


class _HwVrrpExtVIPPingCtr_Type(Integer32):
    """Custom type hwVrrpExtVIPPingCtr based on Integer32"""
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


_HwVrrpExtVIPPingCtr_Type.__name__ = "Integer32"
_HwVrrpExtVIPPingCtr_Object = MibScalar
hwVrrpExtVIPPingCtr = _HwVrrpExtVIPPingCtr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 2),
    _HwVrrpExtVIPPingCtr_Type()
)
hwVrrpExtVIPPingCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtVIPPingCtr.setStatus("current")


class _HwVrrpExtSsTimer_Type(Integer32):
    """Custom type hwVrrpExtSsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpExtSsTimer_Type.__name__ = "Integer32"
_HwVrrpExtSsTimer_Object = MibScalar
hwVrrpExtSsTimer = _HwVrrpExtSsTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 3),
    _HwVrrpExtSsTimer_Type()
)
hwVrrpExtSsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtSsTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwVrrpExtSsTimer.setUnits("seconds")
_HwVrrpExtLearnAdvIntervalFlag_Type = EnabledStatus
_HwVrrpExtLearnAdvIntervalFlag_Object = MibScalar
hwVrrpExtLearnAdvIntervalFlag = _HwVrrpExtLearnAdvIntervalFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 4),
    _HwVrrpExtLearnAdvIntervalFlag_Type()
)
hwVrrpExtLearnAdvIntervalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtLearnAdvIntervalFlag.setStatus("current")


class _HwVrrpExtProtocolVersion_Type(Integer32):
    """Custom type hwVrrpExtProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_HwVrrpExtProtocolVersion_Type.__name__ = "Integer32"
_HwVrrpExtProtocolVersion_Object = MibScalar
hwVrrpExtProtocolVersion = _HwVrrpExtProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 5),
    _HwVrrpExtProtocolVersion_Type()
)
hwVrrpExtProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtProtocolVersion.setStatus("current")


class _HwVrrpExtSendV3AdverPktMode_Type(Integer32):
    """Custom type hwVrrpExtSendV3AdverPktMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2only", 1),
          ("v2v3both", 3),
          ("v3only", 2))
    )


_HwVrrpExtSendV3AdverPktMode_Type.__name__ = "Integer32"
_HwVrrpExtSendV3AdverPktMode_Object = MibScalar
hwVrrpExtSendV3AdverPktMode = _HwVrrpExtSendV3AdverPktMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 6),
    _HwVrrpExtSendV3AdverPktMode_Type()
)
hwVrrpExtSendV3AdverPktMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpExtSendV3AdverPktMode.setStatus("current")


class _HwVrrpExtStateChangeReasonString_Type(OctetString):
    """Custom type hwVrrpExtStateChangeReasonString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwVrrpExtStateChangeReasonString_Type.__name__ = "OctetString"
_HwVrrpExtStateChangeReasonString_Object = MibScalar
hwVrrpExtStateChangeReasonString = _HwVrrpExtStateChangeReasonString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 1, 7),
    _HwVrrpExtStateChangeReasonString_Type()
)
hwVrrpExtStateChangeReasonString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVrrpExtStateChangeReasonString.setStatus("current")
_VrrpExtOperations_ObjectIdentity = ObjectIdentity
vrrpExtOperations = _VrrpExtOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2)
)
_HwVrrpTrackInterTable_Object = MibTable
hwVrrpTrackInterTable = _HwVrrpTrackInterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1)
)
if mibBuilder.loadTexts:
    hwVrrpTrackInterTable.setStatus("current")
_HwVrrpTrackInterEntry_Object = MibTableRow
hwVrrpTrackInterEntry = _HwVrrpTrackInterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1)
)
hwVrrpTrackInterEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterStandByIfnet"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterIfnet"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackInterEntry.setStatus("current")
_HwVrrpTrackInterVRID_Type = VrId
_HwVrrpTrackInterVRID_Object = MibTableColumn
hwVrrpTrackInterVRID = _HwVrrpTrackInterVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 1),
    _HwVrrpTrackInterVRID_Type()
)
hwVrrpTrackInterVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackInterVRID.setStatus("current")
_HwVrrpTrackInterStandByIfnet_Type = InterfaceIndex
_HwVrrpTrackInterStandByIfnet_Object = MibTableColumn
hwVrrpTrackInterStandByIfnet = _HwVrrpTrackInterStandByIfnet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 2),
    _HwVrrpTrackInterStandByIfnet_Type()
)
hwVrrpTrackInterStandByIfnet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackInterStandByIfnet.setStatus("current")
_HwVrrpTrackInterIfnet_Type = InterfaceIndex
_HwVrrpTrackInterIfnet_Object = MibTableColumn
hwVrrpTrackInterIfnet = _HwVrrpTrackInterIfnet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 3),
    _HwVrrpTrackInterIfnet_Type()
)
hwVrrpTrackInterIfnet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackInterIfnet.setStatus("current")


class _HwVrrpTrackInterPriReduce_Type(Integer32):
    """Custom type hwVrrpTrackInterPriReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackInterPriReduce_Type.__name__ = "Integer32"
_HwVrrpTrackInterPriReduce_Object = MibTableColumn
hwVrrpTrackInterPriReduce = _HwVrrpTrackInterPriReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 4),
    _HwVrrpTrackInterPriReduce_Type()
)
hwVrrpTrackInterPriReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackInterPriReduce.setStatus("current")
_HwVrrpTrackInterOperRowStatus_Type = RowStatus
_HwVrrpTrackInterOperRowStatus_Object = MibTableColumn
hwVrrpTrackInterOperRowStatus = _HwVrrpTrackInterOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 5),
    _HwVrrpTrackInterOperRowStatus_Type()
)
hwVrrpTrackInterOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackInterOperRowStatus.setStatus("current")


class _HwVrrpTrackInterPriIncrease_Type(Integer32):
    """Custom type hwVrrpTrackInterPriIncrease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackInterPriIncrease_Type.__name__ = "Integer32"
_HwVrrpTrackInterPriIncrease_Object = MibTableColumn
hwVrrpTrackInterPriIncrease = _HwVrrpTrackInterPriIncrease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 1, 1, 6),
    _HwVrrpTrackInterPriIncrease_Type()
)
hwVrrpTrackInterPriIncrease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackInterPriIncrease.setStatus("current")
_HwVrrpTrackBfdTable_Object = MibTable
hwVrrpTrackBfdTable = _HwVrrpTrackBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2)
)
if mibBuilder.loadTexts:
    hwVrrpTrackBfdTable.setStatus("current")
_HwVrrpTrackBfdEntry_Object = MibTableRow
hwVrrpTrackBfdEntry = _HwVrrpTrackBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1)
)
hwVrrpTrackBfdEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterStandByIfnet"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackBfdId"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackBfdEntry.setStatus("current")


class _HwVrrpTrackBfdId_Type(Integer32):
    """Custom type hwVrrpTrackBfdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_HwVrrpTrackBfdId_Type.__name__ = "Integer32"
_HwVrrpTrackBfdId_Object = MibTableColumn
hwVrrpTrackBfdId = _HwVrrpTrackBfdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 1),
    _HwVrrpTrackBfdId_Type()
)
hwVrrpTrackBfdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdId.setStatus("current")


class _HwVrrpTrackBfdPriReduce_Type(Integer32):
    """Custom type hwVrrpTrackBfdPriReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackBfdPriReduce_Type.__name__ = "Integer32"
_HwVrrpTrackBfdPriReduce_Object = MibTableColumn
hwVrrpTrackBfdPriReduce = _HwVrrpTrackBfdPriReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 2),
    _HwVrrpTrackBfdPriReduce_Type()
)
hwVrrpTrackBfdPriReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdPriReduce.setStatus("current")
_HwVrrpTrackBfdOperRowStatus_Type = RowStatus
_HwVrrpTrackBfdOperRowStatus_Object = MibTableColumn
hwVrrpTrackBfdOperRowStatus = _HwVrrpTrackBfdOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 3),
    _HwVrrpTrackBfdOperRowStatus_Type()
)
hwVrrpTrackBfdOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdOperRowStatus.setStatus("current")


class _HwVrrpTrackBfdPriIncrease_Type(Integer32):
    """Custom type hwVrrpTrackBfdPriIncrease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackBfdPriIncrease_Type.__name__ = "Integer32"
_HwVrrpTrackBfdPriIncrease_Object = MibTableColumn
hwVrrpTrackBfdPriIncrease = _HwVrrpTrackBfdPriIncrease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 4),
    _HwVrrpTrackBfdPriIncrease_Type()
)
hwVrrpTrackBfdPriIncrease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdPriIncrease.setStatus("current")


class _HwVrrpTrackBfdType_Type(Integer32):
    """Custom type hwVrrpTrackBfdType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("normal", 3),
          ("peer", 2))
    )


_HwVrrpTrackBfdType_Type.__name__ = "Integer32"
_HwVrrpTrackBfdType_Object = MibTableColumn
hwVrrpTrackBfdType = _HwVrrpTrackBfdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 5),
    _HwVrrpTrackBfdType_Type()
)
hwVrrpTrackBfdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdType.setStatus("current")


class _HwVrrpTrackBfdName_Type(DisplayString):
    """Custom type hwVrrpTrackBfdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HwVrrpTrackBfdName_Type.__name__ = "DisplayString"
_HwVrrpTrackBfdName_Object = MibTableColumn
hwVrrpTrackBfdName = _HwVrrpTrackBfdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 2, 1, 6),
    _HwVrrpTrackBfdName_Type()
)
hwVrrpTrackBfdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpTrackBfdName.setStatus("current")
_HwAdminVrrpCfgTable_Object = MibTable
hwAdminVrrpCfgTable = _HwAdminVrrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3)
)
if mibBuilder.loadTexts:
    hwAdminVrrpCfgTable.setStatus("current")
_HwAdminVrrpCfgEntry_Object = MibTableRow
hwAdminVrrpCfgEntry = _HwAdminVrrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3, 1)
)
hwAdminVrrpCfgEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpCfgIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpCfgVRID"),
)
if mibBuilder.loadTexts:
    hwAdminVrrpCfgEntry.setStatus("current")
_HwAdminVrrpCfgIfIndex_Type = InterfaceIndex
_HwAdminVrrpCfgIfIndex_Object = MibTableColumn
hwAdminVrrpCfgIfIndex = _HwAdminVrrpCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3, 1, 1),
    _HwAdminVrrpCfgIfIndex_Type()
)
hwAdminVrrpCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpCfgIfIndex.setStatus("current")
_HwAdminVrrpCfgVRID_Type = VrId
_HwAdminVrrpCfgVRID_Object = MibTableColumn
hwAdminVrrpCfgVRID = _HwAdminVrrpCfgVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3, 1, 2),
    _HwAdminVrrpCfgVRID_Type()
)
hwAdminVrrpCfgVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpCfgVRID.setStatus("current")
_HwAdminVrrpCfgOperRowStatus_Type = RowStatus
_HwAdminVrrpCfgOperRowStatus_Object = MibTableColumn
hwAdminVrrpCfgOperRowStatus = _HwAdminVrrpCfgOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3, 1, 3),
    _HwAdminVrrpCfgOperRowStatus_Type()
)
hwAdminVrrpCfgOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpCfgOperRowStatus.setStatus("current")


class _HwAdminVrrpCfgIgnoreIfDownMode_Type(EnabledStatus):
    """Custom type hwAdminVrrpCfgIgnoreIfDownMode based on EnabledStatus"""


_HwAdminVrrpCfgIgnoreIfDownMode_Object = MibTableColumn
hwAdminVrrpCfgIgnoreIfDownMode = _HwAdminVrrpCfgIgnoreIfDownMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 3, 1, 4),
    _HwAdminVrrpCfgIgnoreIfDownMode_Type()
)
hwAdminVrrpCfgIgnoreIfDownMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpCfgIgnoreIfDownMode.setStatus("current")
_HwAdminVrrpMemberTable_Object = MibTable
hwAdminVrrpMemberTable = _HwAdminVrrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4)
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberTable.setStatus("current")
_HwAdminVrrpMemberEntry_Object = MibTableRow
hwAdminVrrpMemberEntry = _HwAdminVrrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1)
)
hwAdminVrrpMemberEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpCfgIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpCfgVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpMemberIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpMemberVRID"),
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberEntry.setStatus("current")
_HwAdminVrrpMemberIfIndex_Type = InterfaceIndex
_HwAdminVrrpMemberIfIndex_Object = MibTableColumn
hwAdminVrrpMemberIfIndex = _HwAdminVrrpMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1, 1),
    _HwAdminVrrpMemberIfIndex_Type()
)
hwAdminVrrpMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberIfIndex.setStatus("current")
_HwAdminVrrpMemberVRID_Type = VrId
_HwAdminVrrpMemberVRID_Object = MibTableColumn
hwAdminVrrpMemberVRID = _HwAdminVrrpMemberVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1, 2),
    _HwAdminVrrpMemberVRID_Type()
)
hwAdminVrrpMemberVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberVRID.setStatus("current")
_HwAdminVrrpMemberDiscardPkts_Type = Counter32
_HwAdminVrrpMemberDiscardPkts_Object = MibTableColumn
hwAdminVrrpMemberDiscardPkts = _HwAdminVrrpMemberDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1, 3),
    _HwAdminVrrpMemberDiscardPkts_Type()
)
hwAdminVrrpMemberDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberDiscardPkts.setStatus("current")
_HwAdminVrrpMemberOperRowStatus_Type = RowStatus
_HwAdminVrrpMemberOperRowStatus_Object = MibTableColumn
hwAdminVrrpMemberOperRowStatus = _HwAdminVrrpMemberOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1, 4),
    _HwAdminVrrpMemberOperRowStatus_Type()
)
hwAdminVrrpMemberOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberOperRowStatus.setStatus("current")


class _HwAdminVrrpMemberFlowdownMode_Type(EnabledStatus):
    """Custom type hwAdminVrrpMemberFlowdownMode based on EnabledStatus"""


_HwAdminVrrpMemberFlowdownMode_Object = MibTableColumn
hwAdminVrrpMemberFlowdownMode = _HwAdminVrrpMemberFlowdownMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 4, 1, 5),
    _HwAdminVrrpMemberFlowdownMode_Type()
)
hwAdminVrrpMemberFlowdownMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpMemberFlowdownMode.setStatus("current")
_HwVrrpStatResetTable_Object = MibTable
hwVrrpStatResetTable = _HwVrrpStatResetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 5)
)
if mibBuilder.loadTexts:
    hwVrrpStatResetTable.setStatus("current")
_HwVrrpStatResetEntry_Object = MibTableRow
hwVrrpStatResetEntry = _HwVrrpStatResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 5, 1)
)
hwVrrpStatResetEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpStatResetIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpStatResetVRID"),
)
if mibBuilder.loadTexts:
    hwVrrpStatResetEntry.setStatus("current")
_HwVrrpStatResetIfIndex_Type = InterfaceIndex
_HwVrrpStatResetIfIndex_Object = MibTableColumn
hwVrrpStatResetIfIndex = _HwVrrpStatResetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 5, 1, 1),
    _HwVrrpStatResetIfIndex_Type()
)
hwVrrpStatResetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpStatResetIfIndex.setStatus("current")
_HwVrrpStatResetVRID_Type = VrId
_HwVrrpStatResetVRID_Object = MibTableColumn
hwVrrpStatResetVRID = _HwVrrpStatResetVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 5, 1, 2),
    _HwVrrpStatResetVRID_Type()
)
hwVrrpStatResetVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpStatResetVRID.setStatus("current")


class _HwVrrpStatResetFlag_Type(Integer32):
    """Custom type hwVrrpStatResetFlag based on Integer32"""
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


_HwVrrpStatResetFlag_Type.__name__ = "Integer32"
_HwVrrpStatResetFlag_Object = MibTableColumn
hwVrrpStatResetFlag = _HwVrrpStatResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 5, 1, 3),
    _HwVrrpStatResetFlag_Type()
)
hwVrrpStatResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVrrpStatResetFlag.setStatus("current")
_HwAdminVrrpTrackIfTable_Object = MibTable
hwAdminVrrpTrackIfTable = _HwAdminVrrpTrackIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6)
)
if mibBuilder.loadTexts:
    hwAdminVrrpTrackIfTable.setStatus("current")
_HwAdminVrrpTrackIfEntry_Object = MibTableRow
hwAdminVrrpTrackIfEntry = _HwAdminVrrpTrackIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6, 1)
)
hwAdminVrrpTrackIfEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpTrackIfIndex"),
)
if mibBuilder.loadTexts:
    hwAdminVrrpTrackIfEntry.setStatus("current")
_HwAdminVrrpTrackIfIndex_Type = InterfaceIndex
_HwAdminVrrpTrackIfIndex_Object = MibTableColumn
hwAdminVrrpTrackIfIndex = _HwAdminVrrpTrackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6, 1, 1),
    _HwAdminVrrpTrackIfIndex_Type()
)
hwAdminVrrpTrackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAdminVrrpTrackIfIndex.setStatus("current")
_HwAdminVrrpIfIndex_Type = InterfaceIndex
_HwAdminVrrpIfIndex_Object = MibTableColumn
hwAdminVrrpIfIndex = _HwAdminVrrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6, 1, 2),
    _HwAdminVrrpIfIndex_Type()
)
hwAdminVrrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpIfIndex.setStatus("current")
_HwAdminVrrpVrid_Type = VrId
_HwAdminVrrpVrid_Object = MibTableColumn
hwAdminVrrpVrid = _HwAdminVrrpVrid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6, 1, 3),
    _HwAdminVrrpVrid_Type()
)
hwAdminVrrpVrid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpVrid.setStatus("current")
_HwAdminVrrpTrackIfRowStatus_Type = RowStatus
_HwAdminVrrpTrackIfRowStatus_Object = MibTableColumn
hwAdminVrrpTrackIfRowStatus = _HwAdminVrrpTrackIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 6, 1, 4),
    _HwAdminVrrpTrackIfRowStatus_Type()
)
hwAdminVrrpTrackIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAdminVrrpTrackIfRowStatus.setStatus("current")
_HwVrrpTrackEfmTable_Object = MibTable
hwVrrpTrackEfmTable = _HwVrrpTrackEfmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7)
)
if mibBuilder.loadTexts:
    hwVrrpTrackEfmTable.setStatus("current")
_HwVrrpTrackEfmEntry_Object = MibTableRow
hwVrrpTrackEfmEntry = _HwVrrpTrackEfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1)
)
hwVrrpTrackEfmEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmIndex"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackEfmEntry.setStatus("current")
_HwVrrpTrackEfmIfIndex_Type = InterfaceIndex
_HwVrrpTrackEfmIfIndex_Object = MibTableColumn
hwVrrpTrackEfmIfIndex = _HwVrrpTrackEfmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 1),
    _HwVrrpTrackEfmIfIndex_Type()
)
hwVrrpTrackEfmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmIfIndex.setStatus("current")


class _HwVrrpTrackEfmIfName_Type(DisplayString):
    """Custom type hwVrrpTrackEfmIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwVrrpTrackEfmIfName_Type.__name__ = "DisplayString"
_HwVrrpTrackEfmIfName_Object = MibTableColumn
hwVrrpTrackEfmIfName = _HwVrrpTrackEfmIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 2),
    _HwVrrpTrackEfmIfName_Type()
)
hwVrrpTrackEfmIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmIfName.setStatus("current")
_HwVrrpTrackEfmVRID_Type = VrId
_HwVrrpTrackEfmVRID_Object = MibTableColumn
hwVrrpTrackEfmVRID = _HwVrrpTrackEfmVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 3),
    _HwVrrpTrackEfmVRID_Type()
)
hwVrrpTrackEfmVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmVRID.setStatus("current")
_HwVrrpTrackEfmIndex_Type = InterfaceIndex
_HwVrrpTrackEfmIndex_Object = MibTableColumn
hwVrrpTrackEfmIndex = _HwVrrpTrackEfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 4),
    _HwVrrpTrackEfmIndex_Type()
)
hwVrrpTrackEfmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmIndex.setStatus("current")


class _HwVrrpTrackEfmName_Type(DisplayString):
    """Custom type hwVrrpTrackEfmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwVrrpTrackEfmName_Type.__name__ = "DisplayString"
_HwVrrpTrackEfmName_Object = MibTableColumn
hwVrrpTrackEfmName = _HwVrrpTrackEfmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 5),
    _HwVrrpTrackEfmName_Type()
)
hwVrrpTrackEfmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmName.setStatus("current")
_HwVrrpTrackEfmOperRowStatus_Type = RowStatus
_HwVrrpTrackEfmOperRowStatus_Object = MibTableColumn
hwVrrpTrackEfmOperRowStatus = _HwVrrpTrackEfmOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 7, 1, 6),
    _HwVrrpTrackEfmOperRowStatus_Type()
)
hwVrrpTrackEfmOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackEfmOperRowStatus.setStatus("current")
_HwVrrpTriggerRouteTable_Object = MibTable
hwVrrpTriggerRouteTable = _HwVrrpTriggerRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 8)
)
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteTable.setStatus("current")
_HwVrrpTriggerRouteEntry_Object = MibTableRow
hwVrrpTriggerRouteEntry = _HwVrrpTriggerRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 8, 1)
)
hwVrrpTriggerRouteEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTriggerRouteIfIndex"),
)
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteEntry.setStatus("current")
_HwVrrpTriggerRouteIfIndex_Type = InterfaceIndex
_HwVrrpTriggerRouteIfIndex_Object = MibTableColumn
hwVrrpTriggerRouteIfIndex = _HwVrrpTriggerRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 8, 1, 1),
    _HwVrrpTriggerRouteIfIndex_Type()
)
hwVrrpTriggerRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteIfIndex.setStatus("current")


class _HwVrrpTriggerRouteMode_Type(Integer32):
    """Custom type hwVrrpTriggerRouteMode based on Integer32"""
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


_HwVrrpTriggerRouteMode_Type.__name__ = "Integer32"
_HwVrrpTriggerRouteMode_Object = MibTableColumn
hwVrrpTriggerRouteMode = _HwVrrpTriggerRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 8, 1, 2),
    _HwVrrpTriggerRouteMode_Type()
)
hwVrrpTriggerRouteMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteMode.setStatus("current")
_HwVrrpTriggerRouteOperRowStatus_Type = RowStatus
_HwVrrpTriggerRouteOperRowStatus_Object = MibTableColumn
hwVrrpTriggerRouteOperRowStatus = _HwVrrpTriggerRouteOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 8, 1, 51),
    _HwVrrpTriggerRouteOperRowStatus_Type()
)
hwVrrpTriggerRouteOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteOperRowStatus.setStatus("current")
_HwVrrpCfgTable_Object = MibTable
hwVrrpCfgTable = _HwVrrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9)
)
if mibBuilder.loadTexts:
    hwVrrpCfgTable.setStatus("current")
_HwVrrpCfgEntry_Object = MibTableRow
hwVrrpCfgEntry = _HwVrrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1)
)
hwVrrpCfgEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpCfgIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpCfgVrId"),
)
if mibBuilder.loadTexts:
    hwVrrpCfgEntry.setStatus("current")
_HwVrrpCfgIfIndex_Type = InterfaceIndex
_HwVrrpCfgIfIndex_Object = MibTableColumn
hwVrrpCfgIfIndex = _HwVrrpCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 1),
    _HwVrrpCfgIfIndex_Type()
)
hwVrrpCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpCfgIfIndex.setStatus("current")
_HwVrrpCfgVrId_Type = VrId
_HwVrrpCfgVrId_Object = MibTableColumn
hwVrrpCfgVrId = _HwVrrpCfgVrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 2),
    _HwVrrpCfgVrId_Type()
)
hwVrrpCfgVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpCfgVrId.setStatus("current")


class _HwVrrpCfgLinkBfdDownNumber_Type(Integer32):
    """Custom type hwVrrpCfgLinkBfdDownNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwVrrpCfgLinkBfdDownNumber_Type.__name__ = "Integer32"
_HwVrrpCfgLinkBfdDownNumber_Object = MibTableColumn
hwVrrpCfgLinkBfdDownNumber = _HwVrrpCfgLinkBfdDownNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 3),
    _HwVrrpCfgLinkBfdDownNumber_Type()
)
hwVrrpCfgLinkBfdDownNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpCfgLinkBfdDownNumber.setStatus("current")


class _HwVrrpCfgMsecAdvInterval_Type(Integer32):
    """Custom type hwVrrpCfgMsecAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_HwVrrpCfgMsecAdvInterval_Type.__name__ = "Integer32"
_HwVrrpCfgMsecAdvInterval_Object = MibTableColumn
hwVrrpCfgMsecAdvInterval = _HwVrrpCfgMsecAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 4),
    _HwVrrpCfgMsecAdvInterval_Type()
)
hwVrrpCfgMsecAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpCfgMsecAdvInterval.setStatus("current")


class _HwVrrpCfgFastResumeFlag_Type(Integer32):
    """Custom type hwVrrpCfgFastResumeFlag based on Integer32"""
    defaultValue = 2

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


_HwVrrpCfgFastResumeFlag_Type.__name__ = "Integer32"
_HwVrrpCfgFastResumeFlag_Object = MibTableColumn
hwVrrpCfgFastResumeFlag = _HwVrrpCfgFastResumeFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 50),
    _HwVrrpCfgFastResumeFlag_Type()
)
hwVrrpCfgFastResumeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpCfgFastResumeFlag.setStatus("current")
_HwVrrpCfgOperRowStatus_Type = RowStatus
_HwVrrpCfgOperRowStatus_Object = MibTableColumn
hwVrrpCfgOperRowStatus = _HwVrrpCfgOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 9, 1, 51),
    _HwVrrpCfgOperRowStatus_Type()
)
hwVrrpCfgOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpCfgOperRowStatus.setStatus("current")
_HwVrrpStatExtTable_Object = MibTable
hwVrrpStatExtTable = _HwVrrpStatExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10)
)
if mibBuilder.loadTexts:
    hwVrrpStatExtTable.setStatus("current")
_HwVrrpStatExtEntry_Object = MibTableRow
hwVrrpStatExtEntry = _HwVrrpStatExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1)
)
hwVrrpStatExtEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpStatExtIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpStatExtVRID"),
)
if mibBuilder.loadTexts:
    hwVrrpStatExtEntry.setStatus("current")
_HwVrrpStatExtIfIndex_Type = InterfaceIndex
_HwVrrpStatExtIfIndex_Object = MibTableColumn
hwVrrpStatExtIfIndex = _HwVrrpStatExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 1),
    _HwVrrpStatExtIfIndex_Type()
)
hwVrrpStatExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpStatExtIfIndex.setStatus("current")
_HwVrrpStatExtVRID_Type = VrId
_HwVrrpStatExtVRID_Object = MibTableColumn
hwVrrpStatExtVRID = _HwVrrpStatExtVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 2),
    _HwVrrpStatExtVRID_Type()
)
hwVrrpStatExtVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpStatExtVRID.setStatus("current")
_HwVrrpStatExtBecomeBackup_Type = Counter32
_HwVrrpStatExtBecomeBackup_Object = MibTableColumn
hwVrrpStatExtBecomeBackup = _HwVrrpStatExtBecomeBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 3),
    _HwVrrpStatExtBecomeBackup_Type()
)
hwVrrpStatExtBecomeBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpStatExtBecomeBackup.setStatus("current")
_HwVrrpStatExtBecomeInit_Type = Counter32
_HwVrrpStatExtBecomeInit_Object = MibTableColumn
hwVrrpStatExtBecomeInit = _HwVrrpStatExtBecomeInit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 4),
    _HwVrrpStatExtBecomeInit_Type()
)
hwVrrpStatExtBecomeInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpStatExtBecomeInit.setStatus("current")


class _HwVrrpStatExtCreateTime_Type(DisplayString):
    """Custom type hwVrrpStatExtCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HwVrrpStatExtCreateTime_Type.__name__ = "DisplayString"
_HwVrrpStatExtCreateTime_Object = MibTableColumn
hwVrrpStatExtCreateTime = _HwVrrpStatExtCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 5),
    _HwVrrpStatExtCreateTime_Type()
)
hwVrrpStatExtCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpStatExtCreateTime.setStatus("current")


class _HwVrrpStatExtLastChangeTime_Type(DisplayString):
    """Custom type hwVrrpStatExtLastChangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HwVrrpStatExtLastChangeTime_Type.__name__ = "DisplayString"
_HwVrrpStatExtLastChangeTime_Object = MibTableColumn
hwVrrpStatExtLastChangeTime = _HwVrrpStatExtLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 10, 1, 6),
    _HwVrrpStatExtLastChangeTime_Type()
)
hwVrrpStatExtLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVrrpStatExtLastChangeTime.setStatus("current")
_HwVrrpTrackIpsecInstanceTable_Object = MibTable
hwVrrpTrackIpsecInstanceTable = _HwVrrpTrackIpsecInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11)
)
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceTable.setStatus("current")
_HwVrrpTrackIpsecInstanceEntry_Object = MibTableRow
hwVrrpTrackIpsecInstanceEntry = _HwVrrpTrackIpsecInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1)
)
hwVrrpTrackIpsecInstanceEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackIpsecInstanceVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackIpsecInstanceStandByIfnet"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackIpsecInstanceID"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceEntry.setStatus("current")
_HwVrrpTrackIpsecInstanceVRID_Type = VrId
_HwVrrpTrackIpsecInstanceVRID_Object = MibTableColumn
hwVrrpTrackIpsecInstanceVRID = _HwVrrpTrackIpsecInstanceVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1, 1),
    _HwVrrpTrackIpsecInstanceVRID_Type()
)
hwVrrpTrackIpsecInstanceVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceVRID.setStatus("current")
_HwVrrpTrackIpsecInstanceStandByIfnet_Type = InterfaceIndex
_HwVrrpTrackIpsecInstanceStandByIfnet_Object = MibTableColumn
hwVrrpTrackIpsecInstanceStandByIfnet = _HwVrrpTrackIpsecInstanceStandByIfnet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1, 2),
    _HwVrrpTrackIpsecInstanceStandByIfnet_Type()
)
hwVrrpTrackIpsecInstanceStandByIfnet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceStandByIfnet.setStatus("current")


class _HwVrrpTrackIpsecInstanceID_Type(Integer32):
    """Custom type hwVrrpTrackIpsecInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwVrrpTrackIpsecInstanceID_Type.__name__ = "Integer32"
_HwVrrpTrackIpsecInstanceID_Object = MibTableColumn
hwVrrpTrackIpsecInstanceID = _HwVrrpTrackIpsecInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1, 3),
    _HwVrrpTrackIpsecInstanceID_Type()
)
hwVrrpTrackIpsecInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceID.setStatus("current")


class _HwVrrpTrackIpsecInstancePriReduce_Type(Integer32):
    """Custom type hwVrrpTrackIpsecInstancePriReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackIpsecInstancePriReduce_Type.__name__ = "Integer32"
_HwVrrpTrackIpsecInstancePriReduce_Object = MibTableColumn
hwVrrpTrackIpsecInstancePriReduce = _HwVrrpTrackIpsecInstancePriReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1, 4),
    _HwVrrpTrackIpsecInstancePriReduce_Type()
)
hwVrrpTrackIpsecInstancePriReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstancePriReduce.setStatus("current")
_HwVrrpTrackIpsecInstanceOperRowStatus_Type = RowStatus
_HwVrrpTrackIpsecInstanceOperRowStatus_Object = MibTableColumn
hwVrrpTrackIpsecInstanceOperRowStatus = _HwVrrpTrackIpsecInstanceOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 11, 1, 5),
    _HwVrrpTrackIpsecInstanceOperRowStatus_Type()
)
hwVrrpTrackIpsecInstanceOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackIpsecInstanceOperRowStatus.setStatus("current")
_HwVrrpTrackNQATable_Object = MibTable
hwVrrpTrackNQATable = _HwVrrpTrackNQATable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12)
)
if mibBuilder.loadTexts:
    hwVrrpTrackNQATable.setStatus("current")
_HwVrrpTrackNQAEntry_Object = MibTableRow
hwVrrpTrackNQAEntry = _HwVrrpTrackNQAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1)
)
hwVrrpTrackNQAEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackNQAVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackNQAStandbyIfIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackNQAAdminName"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackNQATestName"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackNQAEntry.setStatus("current")
_HwVrrpTrackNQAVRID_Type = VrId
_HwVrrpTrackNQAVRID_Object = MibTableColumn
hwVrrpTrackNQAVRID = _HwVrrpTrackNQAVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 1),
    _HwVrrpTrackNQAVRID_Type()
)
hwVrrpTrackNQAVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackNQAVRID.setStatus("current")
_HwVrrpTrackNQAStandbyIfIndex_Type = InterfaceIndex
_HwVrrpTrackNQAStandbyIfIndex_Object = MibTableColumn
hwVrrpTrackNQAStandbyIfIndex = _HwVrrpTrackNQAStandbyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 2),
    _HwVrrpTrackNQAStandbyIfIndex_Type()
)
hwVrrpTrackNQAStandbyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackNQAStandbyIfIndex.setStatus("current")


class _HwVrrpTrackNQAAdminName_Type(DisplayString):
    """Custom type hwVrrpTrackNQAAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVrrpTrackNQAAdminName_Type.__name__ = "DisplayString"
_HwVrrpTrackNQAAdminName_Object = MibTableColumn
hwVrrpTrackNQAAdminName = _HwVrrpTrackNQAAdminName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 3),
    _HwVrrpTrackNQAAdminName_Type()
)
hwVrrpTrackNQAAdminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackNQAAdminName.setStatus("current")


class _HwVrrpTrackNQATestName_Type(DisplayString):
    """Custom type hwVrrpTrackNQATestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVrrpTrackNQATestName_Type.__name__ = "DisplayString"
_HwVrrpTrackNQATestName_Object = MibTableColumn
hwVrrpTrackNQATestName = _HwVrrpTrackNQATestName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 4),
    _HwVrrpTrackNQATestName_Type()
)
hwVrrpTrackNQATestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackNQATestName.setStatus("current")


class _HwVrrpTrackNQAPriReduce_Type(Integer32):
    """Custom type hwVrrpTrackNQAPriReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackNQAPriReduce_Type.__name__ = "Integer32"
_HwVrrpTrackNQAPriReduce_Object = MibTableColumn
hwVrrpTrackNQAPriReduce = _HwVrrpTrackNQAPriReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 5),
    _HwVrrpTrackNQAPriReduce_Type()
)
hwVrrpTrackNQAPriReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackNQAPriReduce.setStatus("current")
_HwVrrpTrackNQAOperRowStatus_Type = RowStatus
_HwVrrpTrackNQAOperRowStatus_Object = MibTableColumn
hwVrrpTrackNQAOperRowStatus = _HwVrrpTrackNQAOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 12, 1, 6),
    _HwVrrpTrackNQAOperRowStatus_Type()
)
hwVrrpTrackNQAOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackNQAOperRowStatus.setStatus("current")
_HwVrrpTrackRouteTable_Object = MibTable
hwVrrpTrackRouteTable = _HwVrrpTrackRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13)
)
if mibBuilder.loadTexts:
    hwVrrpTrackRouteTable.setStatus("current")
_HwVrrpTrackRouteEntry_Object = MibTableRow
hwVrrpTrackRouteEntry = _HwVrrpTrackRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1)
)
hwVrrpTrackRouteEntry.setIndexNames(
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackRouteIndex"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackRouteVRID"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackRoutePrefix"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackRouteMask"),
    (0, "HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackRouteVrf"),
)
if mibBuilder.loadTexts:
    hwVrrpTrackRouteEntry.setStatus("current")
_HwVrrpTrackRouteVRID_Type = VrId
_HwVrrpTrackRouteVRID_Object = MibTableColumn
hwVrrpTrackRouteVRID = _HwVrrpTrackRouteVRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 1),
    _HwVrrpTrackRouteVRID_Type()
)
hwVrrpTrackRouteVRID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackRouteVRID.setStatus("current")
_HwVrrpTrackRouteIndex_Type = InterfaceIndex
_HwVrrpTrackRouteIndex_Object = MibTableColumn
hwVrrpTrackRouteIndex = _HwVrrpTrackRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 2),
    _HwVrrpTrackRouteIndex_Type()
)
hwVrrpTrackRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackRouteIndex.setStatus("current")
_HwVrrpTrackRoutePrefix_Type = IpAddress
_HwVrrpTrackRoutePrefix_Object = MibTableColumn
hwVrrpTrackRoutePrefix = _HwVrrpTrackRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 3),
    _HwVrrpTrackRoutePrefix_Type()
)
hwVrrpTrackRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackRoutePrefix.setStatus("current")
_HwVrrpTrackRouteMask_Type = IpAddress
_HwVrrpTrackRouteMask_Object = MibTableColumn
hwVrrpTrackRouteMask = _HwVrrpTrackRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 4),
    _HwVrrpTrackRouteMask_Type()
)
hwVrrpTrackRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackRouteMask.setStatus("current")


class _HwVrrpTrackRouteVrf_Type(DisplayString):
    """Custom type hwVrrpTrackRouteVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVrrpTrackRouteVrf_Type.__name__ = "DisplayString"
_HwVrrpTrackRouteVrf_Object = MibTableColumn
hwVrrpTrackRouteVrf = _HwVrrpTrackRouteVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 5),
    _HwVrrpTrackRouteVrf_Type()
)
hwVrrpTrackRouteVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVrrpTrackRouteVrf.setStatus("current")


class _HwVrrpTrackRoutePriReduce_Type(Integer32):
    """Custom type hwVrrpTrackRoutePriReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVrrpTrackRoutePriReduce_Type.__name__ = "Integer32"
_HwVrrpTrackRoutePriReduce_Object = MibTableColumn
hwVrrpTrackRoutePriReduce = _HwVrrpTrackRoutePriReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 6),
    _HwVrrpTrackRoutePriReduce_Type()
)
hwVrrpTrackRoutePriReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackRoutePriReduce.setStatus("current")
_HwVrrpTrackRouteOperRowStatus_Type = RowStatus
_HwVrrpTrackRouteOperRowStatus_Object = MibTableColumn
hwVrrpTrackRouteOperRowStatus = _HwVrrpTrackRouteOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 13, 1, 7),
    _HwVrrpTrackRouteOperRowStatus_Type()
)
hwVrrpTrackRouteOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVrrpTrackRouteOperRowStatus.setStatus("current")
_HwVrrpExtNotifications_ObjectIdentity = ObjectIdentity
hwVrrpExtNotifications = _HwVrrpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 30)
)
_VrrpExtConformance_ObjectIdentity = ObjectIdentity
vrrpExtConformance = _VrrpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3)
)
_HwvrrpExtCompliances_ObjectIdentity = ObjectIdentity
hwvrrpExtCompliances = _HwvrrpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1)
)
_HwvrrpExtGroups_ObjectIdentity = ObjectIdentity
hwvrrpExtGroups = _HwvrrpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1)
)

# Managed Objects groups

hwvrrpExtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 1)
)
hwvrrpExtGlobalGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtFreeArpInterval"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtVIPPingCtr"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtSsTimer"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtLearnAdvIntervalFlag"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtStateChangeReasonString"))
)
if mibBuilder.loadTexts:
    hwvrrpExtGlobalGroup.setStatus("current")

hwvrrpExtTrackInterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 2)
)
hwvrrpExtTrackInterGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterPriReduce"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterOperRowStatus"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackInterPriIncrease"))
)
if mibBuilder.loadTexts:
    hwvrrpExtTrackInterGroup.setStatus("current")

hwvrrpExtTrackBFDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 3)
)
hwvrrpExtTrackBFDGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackBfdPriReduce"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackBfdOperRowStatus"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackBfdPriIncrease"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackBfdType"))
)
if mibBuilder.loadTexts:
    hwvrrpExtTrackBFDGroup.setStatus("current")

hwAdminVrrpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 4)
)
hwAdminVrrpCfgGroup.setObjects(
    ("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpCfgOperRowStatus")
)
if mibBuilder.loadTexts:
    hwAdminVrrpCfgGroup.setStatus("current")

hwAdminVrrpMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 5)
)
hwAdminVrrpMemberGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpMemberDiscardPkts"),
        ("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpMemberOperRowStatus"),
        ("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpMemberFlowdownMode"))
)
if mibBuilder.loadTexts:
    hwAdminVrrpMemberGroup.setStatus("current")

hwVrrpStatResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 6)
)
hwVrrpStatResetGroup.setObjects(
    ("HUAWEI-VRRP-EXT-MIB", "hwVrrpStatResetFlag")
)
if mibBuilder.loadTexts:
    hwVrrpStatResetGroup.setStatus("current")

hwAdminVrrpTrackIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 7)
)
hwAdminVrrpTrackIfGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpIfIndex"),
        ("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpVrid"),
        ("HUAWEI-VRRP-EXT-MIB", "hwAdminVrrpTrackIfRowStatus"))
)
if mibBuilder.loadTexts:
    hwAdminVrrpTrackIfGroup.setStatus("current")

hwVrrpTrackEfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 8)
)
hwVrrpTrackEfmGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmIfName"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmName"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTrackEfmOperRowStatus"))
)
if mibBuilder.loadTexts:
    hwVrrpTrackEfmGroup.setStatus("current")

hwVrrpTriggerRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 9)
)
hwVrrpTriggerRouteGroup.setObjects(
    ("HUAWEI-VRRP-EXT-MIB", "hwVrrpTriggerRouteIfIndex")
)
if mibBuilder.loadTexts:
    hwVrrpTriggerRouteGroup.setStatus("current")

hwVrrpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 10)
)
hwVrrpCfgGroup.setObjects(
    ("HUAWEI-VRRP-EXT-MIB", "hwVrrpCfgIfIndex")
)
if mibBuilder.loadTexts:
    hwVrrpCfgGroup.setStatus("current")

hwVrrpStatExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 11)
)
hwVrrpStatExtGroup.setObjects(
      *(("HUAWEI-VRRP-EXT-MIB", "hwVrrpStatExtIfIndex"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpStatExtVRID"))
)
if mibBuilder.loadTexts:
    hwVrrpStatExtGroup.setStatus("current")


# Notification objects

hwVrrpExtTrapMasterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 2, 30, 1)
)
hwVrrpExtTrapMasterDown.setObjects(
      *(("VRRP-MIB", "vrrpOperMasterIpAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifName"),
        ("VRRP-MIB", "vrrpOperState"),
        ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtStateChangeReasonString"))
)
if mibBuilder.loadTexts:
    hwVrrpExtTrapMasterDown.setStatus(
        "current"
    )


# Notifications groups

hwVrrpExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 127, 3, 1, 1, 12)
)
hwVrrpExtNotificationGroup.setObjects(
    ("HUAWEI-VRRP-EXT-MIB", "hwVrrpExtTrapMasterDown")
)
if mibBuilder.loadTexts:
    hwVrrpExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VRRP-EXT-MIB",
    **{"hwVrrpExt": hwVrrpExt,
       "hwVrrpExtGlobal": hwVrrpExtGlobal,
       "hwVrrpExtFreeArpInterval": hwVrrpExtFreeArpInterval,
       "hwVrrpExtVIPPingCtr": hwVrrpExtVIPPingCtr,
       "hwVrrpExtSsTimer": hwVrrpExtSsTimer,
       "hwVrrpExtLearnAdvIntervalFlag": hwVrrpExtLearnAdvIntervalFlag,
       "hwVrrpExtProtocolVersion": hwVrrpExtProtocolVersion,
       "hwVrrpExtSendV3AdverPktMode": hwVrrpExtSendV3AdverPktMode,
       "hwVrrpExtStateChangeReasonString": hwVrrpExtStateChangeReasonString,
       "vrrpExtOperations": vrrpExtOperations,
       "hwVrrpTrackInterTable": hwVrrpTrackInterTable,
       "hwVrrpTrackInterEntry": hwVrrpTrackInterEntry,
       "hwVrrpTrackInterVRID": hwVrrpTrackInterVRID,
       "hwVrrpTrackInterStandByIfnet": hwVrrpTrackInterStandByIfnet,
       "hwVrrpTrackInterIfnet": hwVrrpTrackInterIfnet,
       "hwVrrpTrackInterPriReduce": hwVrrpTrackInterPriReduce,
       "hwVrrpTrackInterOperRowStatus": hwVrrpTrackInterOperRowStatus,
       "hwVrrpTrackInterPriIncrease": hwVrrpTrackInterPriIncrease,
       "hwVrrpTrackBfdTable": hwVrrpTrackBfdTable,
       "hwVrrpTrackBfdEntry": hwVrrpTrackBfdEntry,
       "hwVrrpTrackBfdId": hwVrrpTrackBfdId,
       "hwVrrpTrackBfdPriReduce": hwVrrpTrackBfdPriReduce,
       "hwVrrpTrackBfdOperRowStatus": hwVrrpTrackBfdOperRowStatus,
       "hwVrrpTrackBfdPriIncrease": hwVrrpTrackBfdPriIncrease,
       "hwVrrpTrackBfdType": hwVrrpTrackBfdType,
       "hwVrrpTrackBfdName": hwVrrpTrackBfdName,
       "hwAdminVrrpCfgTable": hwAdminVrrpCfgTable,
       "hwAdminVrrpCfgEntry": hwAdminVrrpCfgEntry,
       "hwAdminVrrpCfgIfIndex": hwAdminVrrpCfgIfIndex,
       "hwAdminVrrpCfgVRID": hwAdminVrrpCfgVRID,
       "hwAdminVrrpCfgOperRowStatus": hwAdminVrrpCfgOperRowStatus,
       "hwAdminVrrpCfgIgnoreIfDownMode": hwAdminVrrpCfgIgnoreIfDownMode,
       "hwAdminVrrpMemberTable": hwAdminVrrpMemberTable,
       "hwAdminVrrpMemberEntry": hwAdminVrrpMemberEntry,
       "hwAdminVrrpMemberIfIndex": hwAdminVrrpMemberIfIndex,
       "hwAdminVrrpMemberVRID": hwAdminVrrpMemberVRID,
       "hwAdminVrrpMemberDiscardPkts": hwAdminVrrpMemberDiscardPkts,
       "hwAdminVrrpMemberOperRowStatus": hwAdminVrrpMemberOperRowStatus,
       "hwAdminVrrpMemberFlowdownMode": hwAdminVrrpMemberFlowdownMode,
       "hwVrrpStatResetTable": hwVrrpStatResetTable,
       "hwVrrpStatResetEntry": hwVrrpStatResetEntry,
       "hwVrrpStatResetIfIndex": hwVrrpStatResetIfIndex,
       "hwVrrpStatResetVRID": hwVrrpStatResetVRID,
       "hwVrrpStatResetFlag": hwVrrpStatResetFlag,
       "hwAdminVrrpTrackIfTable": hwAdminVrrpTrackIfTable,
       "hwAdminVrrpTrackIfEntry": hwAdminVrrpTrackIfEntry,
       "hwAdminVrrpTrackIfIndex": hwAdminVrrpTrackIfIndex,
       "hwAdminVrrpIfIndex": hwAdminVrrpIfIndex,
       "hwAdminVrrpVrid": hwAdminVrrpVrid,
       "hwAdminVrrpTrackIfRowStatus": hwAdminVrrpTrackIfRowStatus,
       "hwVrrpTrackEfmTable": hwVrrpTrackEfmTable,
       "hwVrrpTrackEfmEntry": hwVrrpTrackEfmEntry,
       "hwVrrpTrackEfmIfIndex": hwVrrpTrackEfmIfIndex,
       "hwVrrpTrackEfmIfName": hwVrrpTrackEfmIfName,
       "hwVrrpTrackEfmVRID": hwVrrpTrackEfmVRID,
       "hwVrrpTrackEfmIndex": hwVrrpTrackEfmIndex,
       "hwVrrpTrackEfmName": hwVrrpTrackEfmName,
       "hwVrrpTrackEfmOperRowStatus": hwVrrpTrackEfmOperRowStatus,
       "hwVrrpTriggerRouteTable": hwVrrpTriggerRouteTable,
       "hwVrrpTriggerRouteEntry": hwVrrpTriggerRouteEntry,
       "hwVrrpTriggerRouteIfIndex": hwVrrpTriggerRouteIfIndex,
       "hwVrrpTriggerRouteMode": hwVrrpTriggerRouteMode,
       "hwVrrpTriggerRouteOperRowStatus": hwVrrpTriggerRouteOperRowStatus,
       "hwVrrpCfgTable": hwVrrpCfgTable,
       "hwVrrpCfgEntry": hwVrrpCfgEntry,
       "hwVrrpCfgIfIndex": hwVrrpCfgIfIndex,
       "hwVrrpCfgVrId": hwVrrpCfgVrId,
       "hwVrrpCfgLinkBfdDownNumber": hwVrrpCfgLinkBfdDownNumber,
       "hwVrrpCfgMsecAdvInterval": hwVrrpCfgMsecAdvInterval,
       "hwVrrpCfgFastResumeFlag": hwVrrpCfgFastResumeFlag,
       "hwVrrpCfgOperRowStatus": hwVrrpCfgOperRowStatus,
       "hwVrrpStatExtTable": hwVrrpStatExtTable,
       "hwVrrpStatExtEntry": hwVrrpStatExtEntry,
       "hwVrrpStatExtIfIndex": hwVrrpStatExtIfIndex,
       "hwVrrpStatExtVRID": hwVrrpStatExtVRID,
       "hwVrrpStatExtBecomeBackup": hwVrrpStatExtBecomeBackup,
       "hwVrrpStatExtBecomeInit": hwVrrpStatExtBecomeInit,
       "hwVrrpStatExtCreateTime": hwVrrpStatExtCreateTime,
       "hwVrrpStatExtLastChangeTime": hwVrrpStatExtLastChangeTime,
       "hwVrrpTrackIpsecInstanceTable": hwVrrpTrackIpsecInstanceTable,
       "hwVrrpTrackIpsecInstanceEntry": hwVrrpTrackIpsecInstanceEntry,
       "hwVrrpTrackIpsecInstanceVRID": hwVrrpTrackIpsecInstanceVRID,
       "hwVrrpTrackIpsecInstanceStandByIfnet": hwVrrpTrackIpsecInstanceStandByIfnet,
       "hwVrrpTrackIpsecInstanceID": hwVrrpTrackIpsecInstanceID,
       "hwVrrpTrackIpsecInstancePriReduce": hwVrrpTrackIpsecInstancePriReduce,
       "hwVrrpTrackIpsecInstanceOperRowStatus": hwVrrpTrackIpsecInstanceOperRowStatus,
       "hwVrrpTrackNQATable": hwVrrpTrackNQATable,
       "hwVrrpTrackNQAEntry": hwVrrpTrackNQAEntry,
       "hwVrrpTrackNQAVRID": hwVrrpTrackNQAVRID,
       "hwVrrpTrackNQAStandbyIfIndex": hwVrrpTrackNQAStandbyIfIndex,
       "hwVrrpTrackNQAAdminName": hwVrrpTrackNQAAdminName,
       "hwVrrpTrackNQATestName": hwVrrpTrackNQATestName,
       "hwVrrpTrackNQAPriReduce": hwVrrpTrackNQAPriReduce,
       "hwVrrpTrackNQAOperRowStatus": hwVrrpTrackNQAOperRowStatus,
       "hwVrrpTrackRouteTable": hwVrrpTrackRouteTable,
       "hwVrrpTrackRouteEntry": hwVrrpTrackRouteEntry,
       "hwVrrpTrackRouteVRID": hwVrrpTrackRouteVRID,
       "hwVrrpTrackRouteIndex": hwVrrpTrackRouteIndex,
       "hwVrrpTrackRoutePrefix": hwVrrpTrackRoutePrefix,
       "hwVrrpTrackRouteMask": hwVrrpTrackRouteMask,
       "hwVrrpTrackRouteVrf": hwVrrpTrackRouteVrf,
       "hwVrrpTrackRoutePriReduce": hwVrrpTrackRoutePriReduce,
       "hwVrrpTrackRouteOperRowStatus": hwVrrpTrackRouteOperRowStatus,
       "hwVrrpExtNotifications": hwVrrpExtNotifications,
       "hwVrrpExtTrapMasterDown": hwVrrpExtTrapMasterDown,
       "vrrpExtConformance": vrrpExtConformance,
       "hwvrrpExtCompliances": hwvrrpExtCompliances,
       "hwvrrpExtGroups": hwvrrpExtGroups,
       "hwvrrpExtGlobalGroup": hwvrrpExtGlobalGroup,
       "hwvrrpExtTrackInterGroup": hwvrrpExtTrackInterGroup,
       "hwvrrpExtTrackBFDGroup": hwvrrpExtTrackBFDGroup,
       "hwAdminVrrpCfgGroup": hwAdminVrrpCfgGroup,
       "hwAdminVrrpMemberGroup": hwAdminVrrpMemberGroup,
       "hwVrrpStatResetGroup": hwVrrpStatResetGroup,
       "hwAdminVrrpTrackIfGroup": hwAdminVrrpTrackIfGroup,
       "hwVrrpTrackEfmGroup": hwVrrpTrackEfmGroup,
       "hwVrrpTriggerRouteGroup": hwVrrpTriggerRouteGroup,
       "hwVrrpCfgGroup": hwVrrpCfgGroup,
       "hwVrrpStatExtGroup": hwVrrpStatExtGroup,
       "hwVrrpExtNotificationGroup": hwVrrpExtNotificationGroup}
)
