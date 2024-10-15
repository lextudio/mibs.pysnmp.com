# SNMP MIB module (HUAWEI-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PWE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:28 2024
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

(HWEnableValue,
 HWL2VpnStateChangeReason,
 HWL2VpnVcEncapsType) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWEnableValue",
    "HWL2VpnStateChangeReason",
    "HWL2VpnVcEncapsType")

(InterfaceIndexOrZero,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifName")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

(Bits,
 Bits,
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

hwL2VpnPwe3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWLdpPwStateChangeReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
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
        *(("interfaceDown", 2),
          ("ldpSessionDown", 1),
          ("notifiNotForward", 6),
          ("paraUnMatched", 5),
          ("receivedNoMapping", 4),
          ("tunnelDown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwPwe3MIBObjects_ObjectIdentity = ObjectIdentity
hwPwe3MIBObjects = _HwPwe3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1)
)
_HwPwe3Objects_ObjectIdentity = ObjectIdentity
hwPwe3Objects = _HwPwe3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1)
)
_HwPWVcTable_Object = MibTable
hwPWVcTable = _HwPWVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwPWVcTable.setStatus("current")
_HwPWVcEntry_Object = MibTableRow
hwPWVcEntry = _HwPWVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1)
)
hwPWVcEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWVcID"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcType"),
)
if mibBuilder.loadTexts:
    hwPWVcEntry.setStatus("current")
_HwPWVcID_Type = Unsigned32
_HwPWVcID_Object = MibTableColumn
hwPWVcID = _HwPWVcID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 1),
    _HwPWVcID_Type()
)
hwPWVcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWVcID.setStatus("current")
_HwPWVcType_Type = HWL2VpnVcEncapsType
_HwPWVcType_Object = MibTableColumn
hwPWVcType = _HwPWVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 2),
    _HwPWVcType_Type()
)
hwPWVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWVcType.setStatus("current")


class _HwPWVcPeerAddrType_Type(InetAddressType):
    """Custom type hwPWVcPeerAddrType based on InetAddressType"""


_HwPWVcPeerAddrType_Object = MibTableColumn
hwPWVcPeerAddrType = _HwPWVcPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 3),
    _HwPWVcPeerAddrType_Type()
)
hwPWVcPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPeerAddrType.setStatus("current")
_HwPWVcPeerAddr_Type = IpAddress
_HwPWVcPeerAddr_Object = MibTableColumn
hwPWVcPeerAddr = _HwPWVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 4),
    _HwPWVcPeerAddr_Type()
)
hwPWVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPeerAddr.setStatus("current")


class _HwPWVcStatus_Type(Integer32):
    """Custom type hwPWVcStatus based on Integer32"""
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
        *(("backup", 4),
          ("down", 2),
          ("plugout", 3),
          ("up", 1))
    )


_HwPWVcStatus_Type.__name__ = "Integer32"
_HwPWVcStatus_Object = MibTableColumn
hwPWVcStatus = _HwPWVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 5),
    _HwPWVcStatus_Type()
)
hwPWVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcStatus.setStatus("current")
_HwPWVcInboundLabel_Type = Unsigned32
_HwPWVcInboundLabel_Object = MibTableColumn
hwPWVcInboundLabel = _HwPWVcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 6),
    _HwPWVcInboundLabel_Type()
)
hwPWVcInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcInboundLabel.setStatus("current")
_HwPWVcOutboundLabel_Type = Unsigned32
_HwPWVcOutboundLabel_Object = MibTableColumn
hwPWVcOutboundLabel = _HwPWVcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 7),
    _HwPWVcOutboundLabel_Type()
)
hwPWVcOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcOutboundLabel.setStatus("current")


class _HwPWVcSwitchSign_Type(Integer32):
    """Custom type hwPWVcSwitchSign based on Integer32"""
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
        *(("ldpToldp", 3),
          ("ldpTostatic", 2),
          ("staticTostatic", 1),
          ("upe", 4))
    )


_HwPWVcSwitchSign_Type.__name__ = "Integer32"
_HwPWVcSwitchSign_Object = MibTableColumn
hwPWVcSwitchSign = _HwPWVcSwitchSign_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 8),
    _HwPWVcSwitchSign_Type()
)
hwPWVcSwitchSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcSwitchSign.setStatus("current")
_HwPWVcSwitchID_Type = Unsigned32
_HwPWVcSwitchID_Object = MibTableColumn
hwPWVcSwitchID = _HwPWVcSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 9),
    _HwPWVcSwitchID_Type()
)
hwPWVcSwitchID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchID.setStatus("current")


class _HwPWVcSwitchPeerAddrType_Type(InetAddressType):
    """Custom type hwPWVcSwitchPeerAddrType based on InetAddressType"""


_HwPWVcSwitchPeerAddrType_Object = MibTableColumn
hwPWVcSwitchPeerAddrType = _HwPWVcSwitchPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 10),
    _HwPWVcSwitchPeerAddrType_Type()
)
hwPWVcSwitchPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchPeerAddrType.setStatus("current")
_HwPWVcSwitchPeerAddr_Type = IpAddress
_HwPWVcSwitchPeerAddr_Object = MibTableColumn
hwPWVcSwitchPeerAddr = _HwPWVcSwitchPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 11),
    _HwPWVcSwitchPeerAddr_Type()
)
hwPWVcSwitchPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchPeerAddr.setStatus("current")
_HwPWVcSwitchInboundLabel_Type = Unsigned32
_HwPWVcSwitchInboundLabel_Object = MibTableColumn
hwPWVcSwitchInboundLabel = _HwPWVcSwitchInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 12),
    _HwPWVcSwitchInboundLabel_Type()
)
hwPWVcSwitchInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchInboundLabel.setStatus("current")
_HwPWVcSwitchOutboundLabel_Type = Unsigned32
_HwPWVcSwitchOutboundLabel_Object = MibTableColumn
hwPWVcSwitchOutboundLabel = _HwPWVcSwitchOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 13),
    _HwPWVcSwitchOutboundLabel_Type()
)
hwPWVcSwitchOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchOutboundLabel.setStatus("current")
_HwPWVcGroupID_Type = Unsigned32
_HwPWVcGroupID_Object = MibTableColumn
hwPWVcGroupID = _HwPWVcGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 14),
    _HwPWVcGroupID_Type()
)
hwPWVcGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcGroupID.setStatus("current")
_HwPWVcIfIndex_Type = InterfaceIndexOrZero
_HwPWVcIfIndex_Object = MibTableColumn
hwPWVcIfIndex = _HwPWVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 15),
    _HwPWVcIfIndex_Type()
)
hwPWVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcIfIndex.setStatus("current")


class _HwPWVcAcStatus_Type(Integer32):
    """Custom type hwPWVcAcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
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
        *(("down", 2),
          ("downNotify", 6),
          ("notify", 4),
          ("notifyDown", 5),
          ("plugout", 3),
          ("up", 1))
    )


_HwPWVcAcStatus_Type.__name__ = "Integer32"
_HwPWVcAcStatus_Object = MibTableColumn
hwPWVcAcStatus = _HwPWVcAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 16),
    _HwPWVcAcStatus_Type()
)
hwPWVcAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcAcStatus.setStatus("current")


class _HwPWVcACOAMStatus_Type(Integer32):
    """Custom type hwPWVcACOAMStatus based on Integer32"""
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


_HwPWVcACOAMStatus_Type.__name__ = "Integer32"
_HwPWVcACOAMStatus_Object = MibTableColumn
hwPWVcACOAMStatus = _HwPWVcACOAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 17),
    _HwPWVcACOAMStatus_Type()
)
hwPWVcACOAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcACOAMStatus.setStatus("current")


class _HwPWVcMtu_Type(Integer32):
    """Custom type hwPWVcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(46, 9600),
    )


_HwPWVcMtu_Type.__name__ = "Integer32"
_HwPWVcMtu_Object = MibTableColumn
hwPWVcMtu = _HwPWVcMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 18),
    _HwPWVcMtu_Type()
)
hwPWVcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcMtu.setStatus("current")
_HwPWVcCtrlWord_Type = HWEnableValue
_HwPWVcCtrlWord_Object = MibTableColumn
hwPWVcCtrlWord = _HwPWVcCtrlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 19),
    _HwPWVcCtrlWord_Type()
)
hwPWVcCtrlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcCtrlWord.setStatus("current")


class _HwPWVcVCCV_Type(Bits):
    """Custom type hwPWVcVCCV based on Bits"""
    namedValues = NamedValues(
        *(("ccAlert", 1),
          ("ccCw", 0),
          ("ccLabel", 2),
          ("ccTtl", 6),
          ("cvBfd", 5),
          ("cvIcmpping", 3),
          ("cvLspping", 4))
    )

_HwPWVcVCCV_Type.__name__ = "Bits"
_HwPWVcVCCV_Object = MibTableColumn
hwPWVcVCCV = _HwPWVcVCCV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 20),
    _HwPWVcVCCV_Type()
)
hwPWVcVCCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcVCCV.setStatus("current")


class _HwPWVcBandWidth_Type(Unsigned32):
    """Custom type hwPWVcBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwPWVcBandWidth_Type.__name__ = "Unsigned32"
_HwPWVcBandWidth_Object = MibTableColumn
hwPWVcBandWidth = _HwPWVcBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 21),
    _HwPWVcBandWidth_Type()
)
hwPWVcBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcBandWidth.setStatus("current")


class _HwPWVcMaxAtmCells_Type(Unsigned32):
    """Custom type hwPWVcMaxAtmCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_HwPWVcMaxAtmCells_Type.__name__ = "Unsigned32"
_HwPWVcMaxAtmCells_Object = MibTableColumn
hwPWVcMaxAtmCells = _HwPWVcMaxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 22),
    _HwPWVcMaxAtmCells_Type()
)
hwPWVcMaxAtmCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcMaxAtmCells.setStatus("current")


class _HwPWVcTnlPolicyName_Type(OctetString):
    """Custom type hwPWVcTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HwPWVcTnlPolicyName_Type.__name__ = "OctetString"
_HwPWVcTnlPolicyName_Object = MibTableColumn
hwPWVcTnlPolicyName = _HwPWVcTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 23),
    _HwPWVcTnlPolicyName_Type()
)
hwPWVcTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcTnlPolicyName.setStatus("current")
_HwPWVcQoSBehaviorIndex_Type = Unsigned32
_HwPWVcQoSBehaviorIndex_Object = MibTableColumn
hwPWVcQoSBehaviorIndex = _HwPWVcQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 24),
    _HwPWVcQoSBehaviorIndex_Type()
)
hwPWVcQoSBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcQoSBehaviorIndex.setStatus("current")


class _HwPWVcExplicitPathName_Type(DisplayString):
    """Custom type hwPWVcExplicitPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPWVcExplicitPathName_Type.__name__ = "DisplayString"
_HwPWVcExplicitPathName_Object = MibTableColumn
hwPWVcExplicitPathName = _HwPWVcExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 25),
    _HwPWVcExplicitPathName_Type()
)
hwPWVcExplicitPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcExplicitPathName.setStatus("current")


class _HwPWVcTemplateName_Type(OctetString):
    """Custom type hwPWVcTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwPWVcTemplateName_Type.__name__ = "OctetString"
_HwPWVcTemplateName_Object = MibTableColumn
hwPWVcTemplateName = _HwPWVcTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 26),
    _HwPWVcTemplateName_Type()
)
hwPWVcTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcTemplateName.setStatus("current")
_HwPWVcSecondary_Type = TruthValue
_HwPWVcSecondary_Object = MibTableColumn
hwPWVcSecondary = _HwPWVcSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 27),
    _HwPWVcSecondary_Type()
)
hwPWVcSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSecondary.setStatus("current")
_HwPWVcUpTime_Type = Unsigned32
_HwPWVcUpTime_Object = MibTableColumn
hwPWVcUpTime = _HwPWVcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 28),
    _HwPWVcUpTime_Type()
)
hwPWVcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcUpTime.setStatus("current")
_HwPWOAMSync_Type = TruthValue
_HwPWOAMSync_Object = MibTableColumn
hwPWOAMSync = _HwPWOAMSync_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 29),
    _HwPWOAMSync_Type()
)
hwPWOAMSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWOAMSync.setStatus("current")
_HwPWVCForBfdIndex_Type = Unsigned32
_HwPWVCForBfdIndex_Object = MibTableColumn
hwPWVCForBfdIndex = _HwPWVCForBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 30),
    _HwPWVCForBfdIndex_Type()
)
hwPWVCForBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVCForBfdIndex.setStatus("current")
_HwPWVcDelayTime_Type = Unsigned32
_HwPWVcDelayTime_Object = MibTableColumn
hwPWVcDelayTime = _HwPWVcDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 31),
    _HwPWVcDelayTime_Type()
)
hwPWVcDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcDelayTime.setStatus("current")


class _HwPWVcReroutePolicy_Type(Integer32):
    """Custom type hwPWVcReroutePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("err", 5),
          ("immediately", 2),
          ("immediatelySwitch", 7),
          ("invalid", 6),
          ("never", 3),
          ("none", 4))
    )


_HwPWVcReroutePolicy_Type.__name__ = "Integer32"
_HwPWVcReroutePolicy_Object = MibTableColumn
hwPWVcReroutePolicy = _HwPWVcReroutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 32),
    _HwPWVcReroutePolicy_Type()
)
hwPWVcReroutePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcReroutePolicy.setStatus("current")
_HwPWVcResumeTime_Type = Unsigned32
_HwPWVcResumeTime_Object = MibTableColumn
hwPWVcResumeTime = _HwPWVcResumeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 33),
    _HwPWVcResumeTime_Type()
)
hwPWVcResumeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcResumeTime.setStatus("current")
_HwPWVcRerouteReason_Type = HWL2VpnStateChangeReason
_HwPWVcRerouteReason_Object = MibTableColumn
hwPWVcRerouteReason = _HwPWVcRerouteReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 34),
    _HwPWVcRerouteReason_Type()
)
hwPWVcRerouteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcRerouteReason.setStatus("current")
_HwPWVcLastRerouteTime_Type = Unsigned32
_HwPWVcLastRerouteTime_Object = MibTableColumn
hwPWVcLastRerouteTime = _HwPWVcLastRerouteTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 35),
    _HwPWVcLastRerouteTime_Type()
)
hwPWVcLastRerouteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcLastRerouteTime.setStatus("current")
_HwPWVcManualSetFault_Type = TruthValue
_HwPWVcManualSetFault_Object = MibTableColumn
hwPWVcManualSetFault = _HwPWVcManualSetFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 36),
    _HwPWVcManualSetFault_Type()
)
hwPWVcManualSetFault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcManualSetFault.setStatus("current")
_HwPWVcActive_Type = TruthValue
_HwPWVcActive_Object = MibTableColumn
hwPWVcActive = _HwPWVcActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 37),
    _HwPWVcActive_Type()
)
hwPWVcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcActive.setStatus("current")
_HwPWVcVrIfIndex_Type = InterfaceIndexOrZero
_HwPWVcVrIfIndex_Object = MibTableColumn
hwPWVcVrIfIndex = _HwPWVcVrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 38),
    _HwPWVcVrIfIndex_Type()
)
hwPWVcVrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcVrIfIndex.setStatus("current")


class _HwPWVcVrID_Type(Unsigned32):
    """Custom type hwPWVcVrID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPWVcVrID_Type.__name__ = "Unsigned32"
_HwPWVcVrID_Object = MibTableColumn
hwPWVcVrID = _HwPWVcVrID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 39),
    _HwPWVcVrID_Type()
)
hwPWVcVrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcVrID.setStatus("current")


class _HwPWBFDDetectMultiplier_Type(Unsigned32):
    """Custom type hwPWBFDDetectMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 50),
    )


_HwPWBFDDetectMultiplier_Type.__name__ = "Unsigned32"
_HwPWBFDDetectMultiplier_Object = MibTableColumn
hwPWBFDDetectMultiplier = _HwPWBFDDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 40),
    _HwPWBFDDetectMultiplier_Type()
)
hwPWBFDDetectMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWBFDDetectMultiplier.setStatus("current")


class _HwPWBFDMinReceiveInterval_Type(Unsigned32):
    """Custom type hwPWBFDMinReceiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1000),
    )


_HwPWBFDMinReceiveInterval_Type.__name__ = "Unsigned32"
_HwPWBFDMinReceiveInterval_Object = MibTableColumn
hwPWBFDMinReceiveInterval = _HwPWBFDMinReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 41),
    _HwPWBFDMinReceiveInterval_Type()
)
hwPWBFDMinReceiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWBFDMinReceiveInterval.setStatus("current")


class _HwPWBFDMinTransmitInterval_Type(Unsigned32):
    """Custom type hwPWBFDMinTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1000),
    )


_HwPWBFDMinTransmitInterval_Type.__name__ = "Unsigned32"
_HwPWBFDMinTransmitInterval_Object = MibTableColumn
hwPWBFDMinTransmitInterval = _HwPWBFDMinTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 42),
    _HwPWBFDMinTransmitInterval_Type()
)
hwPWBFDMinTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWBFDMinTransmitInterval.setStatus("current")
_HwPWDynamicBFDDetect_Type = TruthValue
_HwPWDynamicBFDDetect_Object = MibTableColumn
hwPWDynamicBFDDetect = _HwPWDynamicBFDDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 43),
    _HwPWDynamicBFDDetect_Type()
)
hwPWDynamicBFDDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWDynamicBFDDetect.setStatus("current")


class _HwPWBFDRemoteVcID_Type(Unsigned32):
    """Custom type hwPWBFDRemoteVcID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwPWBFDRemoteVcID_Type.__name__ = "Unsigned32"
_HwPWBFDRemoteVcID_Object = MibTableColumn
hwPWBFDRemoteVcID = _HwPWBFDRemoteVcID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 44),
    _HwPWBFDRemoteVcID_Type()
)
hwPWBFDRemoteVcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWBFDRemoteVcID.setStatus("current")


class _HwPWEthOamType_Type(Integer32):
    """Custom type hwPWEthOamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethOam1ag", 1),
          ("ethOam3ah", 2),
          ("noEthOamCfg", 3))
    )


_HwPWEthOamType_Type.__name__ = "Integer32"
_HwPWEthOamType_Object = MibTableColumn
hwPWEthOamType = _HwPWEthOamType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 45),
    _HwPWEthOamType_Type()
)
hwPWEthOamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWEthOamType.setStatus("current")


class _HwPWCfmMaIndex_Type(Unsigned32):
    """Custom type hwPWCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HwPWCfmMaIndex_Type.__name__ = "Unsigned32"
_HwPWCfmMaIndex_Object = MibTableColumn
hwPWCfmMaIndex = _HwPWCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 46),
    _HwPWCfmMaIndex_Type()
)
hwPWCfmMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWCfmMaIndex.setStatus("current")


class _HwPWVcUpStartTime_Type(DisplayString):
    """Custom type hwPWVcUpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwPWVcUpStartTime_Type.__name__ = "DisplayString"
_HwPWVcUpStartTime_Object = MibTableColumn
hwPWVcUpStartTime = _HwPWVcUpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 47),
    _HwPWVcUpStartTime_Type()
)
hwPWVcUpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcUpStartTime.setStatus("current")
_HwPWVcUpSumTime_Type = Unsigned32
_HwPWVcUpSumTime_Object = MibTableColumn
hwPWVcUpSumTime = _HwPWVcUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 48),
    _HwPWVcUpSumTime_Type()
)
hwPWVcUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcUpSumTime.setStatus("current")


class _HwPWVcIfName_Type(DisplayString):
    """Custom type hwPWVcIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwPWVcIfName_Type.__name__ = "DisplayString"
_HwPWVcIfName_Object = MibTableColumn
hwPWVcIfName = _HwPWVcIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 49),
    _HwPWVcIfName_Type()
)
hwPWVcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcIfName.setStatus("current")
_HwPWVcRowStatus_Type = RowStatus
_HwPWVcRowStatus_Object = MibTableColumn
hwPWVcRowStatus = _HwPWVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 51),
    _HwPWVcRowStatus_Type()
)
hwPWVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcRowStatus.setStatus("current")


class _HwPWVcAtmPackOvertime_Type(Unsigned32):
    """Custom type hwPWVcAtmPackOvertime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 50000),
    )


_HwPWVcAtmPackOvertime_Type.__name__ = "Unsigned32"
_HwPWVcAtmPackOvertime_Object = MibTableColumn
hwPWVcAtmPackOvertime = _HwPWVcAtmPackOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 52),
    _HwPWVcAtmPackOvertime_Type()
)
hwPWVcAtmPackOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcAtmPackOvertime.setStatus("current")


class _HwPWVcPwJitterBufferDepth_Type(Unsigned32):
    """Custom type hwPWVcPwJitterBufferDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwPWVcPwJitterBufferDepth_Type.__name__ = "Unsigned32"
_HwPWVcPwJitterBufferDepth_Object = MibTableColumn
hwPWVcPwJitterBufferDepth = _HwPWVcPwJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 53),
    _HwPWVcPwJitterBufferDepth_Type()
)
hwPWVcPwJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPwJitterBufferDepth.setStatus("current")


class _HwPWVcPwTdmEncapsulationNum_Type(Unsigned32):
    """Custom type hwPWVcPwTdmEncapsulationNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwPWVcPwTdmEncapsulationNum_Type.__name__ = "Unsigned32"
_HwPWVcPwTdmEncapsulationNum_Object = MibTableColumn
hwPWVcPwTdmEncapsulationNum = _HwPWVcPwTdmEncapsulationNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 54),
    _HwPWVcPwTdmEncapsulationNum_Type()
)
hwPWVcPwTdmEncapsulationNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPwTdmEncapsulationNum.setStatus("current")


class _HwPWVcPwIdleCode_Type(Unsigned32):
    """Custom type hwPWVcPwIdleCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwPWVcPwIdleCode_Type.__name__ = "Unsigned32"
_HwPWVcPwIdleCode_Object = MibTableColumn
hwPWVcPwIdleCode = _HwPWVcPwIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 55),
    _HwPWVcPwIdleCode_Type()
)
hwPWVcPwIdleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPwIdleCode.setStatus("current")
_HwPWVcPwRtpHeader_Type = Unsigned32
_HwPWVcPwRtpHeader_Object = MibTableColumn
hwPWVcPwRtpHeader = _HwPWVcPwRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 56),
    _HwPWVcPwRtpHeader_Type()
)
hwPWVcPwRtpHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPwRtpHeader.setStatus("current")


class _HwPWVcSwitchTnlPolicyName_Type(OctetString):
    """Custom type hwPWVcSwitchTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HwPWVcSwitchTnlPolicyName_Type.__name__ = "OctetString"
_HwPWVcSwitchTnlPolicyName_Object = MibTableColumn
hwPWVcSwitchTnlPolicyName = _HwPWVcSwitchTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 57),
    _HwPWVcSwitchTnlPolicyName_Type()
)
hwPWVcSwitchTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchTnlPolicyName.setStatus("current")


class _HwPWVcCfmMdIndex_Type(Unsigned32):
    """Custom type hwPWVcCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HwPWVcCfmMdIndex_Type.__name__ = "Unsigned32"
_HwPWVcCfmMdIndex_Object = MibTableColumn
hwPWVcCfmMdIndex = _HwPWVcCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 58),
    _HwPWVcCfmMdIndex_Type()
)
hwPWVcCfmMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcCfmMdIndex.setStatus("current")


class _HwPWVcCfmMaName_Type(OctetString):
    """Custom type hwPWVcCfmMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_HwPWVcCfmMaName_Type.__name__ = "OctetString"
_HwPWVcCfmMaName_Object = MibTableColumn
hwPWVcCfmMaName = _HwPWVcCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 59),
    _HwPWVcCfmMaName_Type()
)
hwPWVcCfmMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcCfmMaName.setStatus("current")


class _HwPWVcCfmMdName_Type(OctetString):
    """Custom type hwPWVcCfmMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_HwPWVcCfmMdName_Type.__name__ = "OctetString"
_HwPWVcCfmMdName_Object = MibTableColumn
hwPWVcCfmMdName = _HwPWVcCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 60),
    _HwPWVcCfmMdName_Type()
)
hwPWVcCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcCfmMdName.setStatus("current")


class _HwPWVcRawOrTagged_Type(Integer32):
    """Custom type hwPWVcRawOrTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("rawTagNotConfiged", 3),
          ("tagged", 2))
    )


_HwPWVcRawOrTagged_Type.__name__ = "Integer32"
_HwPWVcRawOrTagged_Object = MibTableColumn
hwPWVcRawOrTagged = _HwPWVcRawOrTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 61),
    _HwPWVcRawOrTagged_Type()
)
hwPWVcRawOrTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcRawOrTagged.setStatus("current")


class _HwPWVcInterworkingType_Type(Integer32):
    """Custom type hwPWVcInterworkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipInterWorking", 1),
          ("ipLayer2", 2),
          ("ipUnknown", 3))
    )


_HwPWVcInterworkingType_Type.__name__ = "Integer32"
_HwPWVcInterworkingType_Object = MibTableColumn
hwPWVcInterworkingType = _HwPWVcInterworkingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 62),
    _HwPWVcInterworkingType_Type()
)
hwPWVcInterworkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcInterworkingType.setStatus("current")
_HwPWVcCir_Type = Unsigned32
_HwPWVcCir_Object = MibTableColumn
hwPWVcCir = _HwPWVcCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 63),
    _HwPWVcCir_Type()
)
hwPWVcCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcCir.setStatus("current")
_HwPWVcPir_Type = Unsigned32
_HwPWVcPir_Object = MibTableColumn
hwPWVcPir = _HwPWVcPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 64),
    _HwPWVcPir_Type()
)
hwPWVcPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcPir.setStatus("current")


class _HwPWVcQosProfile_Type(DisplayString):
    """Custom type hwPWVcQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPWVcQosProfile_Type.__name__ = "DisplayString"
_HwPWVcQosProfile_Object = MibTableColumn
hwPWVcQosProfile = _HwPWVcQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 65),
    _HwPWVcQosProfile_Type()
)
hwPWVcQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcQosProfile.setStatus("current")
_HwPWVcSwitchCir_Type = Unsigned32
_HwPWVcSwitchCir_Object = MibTableColumn
hwPWVcSwitchCir = _HwPWVcSwitchCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 66),
    _HwPWVcSwitchCir_Type()
)
hwPWVcSwitchCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchCir.setStatus("current")
_HwPWVcSwitchPir_Type = Unsigned32
_HwPWVcSwitchPir_Object = MibTableColumn
hwPWVcSwitchPir = _HwPWVcSwitchPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 67),
    _HwPWVcSwitchPir_Type()
)
hwPWVcSwitchPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchPir.setStatus("current")


class _HwPWVcSwitchQosProfile_Type(DisplayString):
    """Custom type hwPWVcSwitchQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPWVcSwitchQosProfile_Type.__name__ = "DisplayString"
_HwPWVcSwitchQosProfile_Object = MibTableColumn
hwPWVcSwitchQosProfile = _HwPWVcSwitchQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 68),
    _HwPWVcSwitchQosProfile_Type()
)
hwPWVcSwitchQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchQosProfile.setStatus("current")
_HwPWVcTrigger_Type = TruthValue
_HwPWVcTrigger_Object = MibTableColumn
hwPWVcTrigger = _HwPWVcTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 69),
    _HwPWVcTrigger_Type()
)
hwPWVcTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcTrigger.setStatus("current")
_HwPWVcEnableACOAM_Type = EnabledStatus
_HwPWVcEnableACOAM_Object = MibTableColumn
hwPWVcEnableACOAM = _HwPWVcEnableACOAM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 70),
    _HwPWVcEnableACOAM_Type()
)
hwPWVcEnableACOAM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcEnableACOAM.setStatus("current")
_HwPWVcSwitchVrIfIndex_Type = InterfaceIndexOrZero
_HwPWVcSwitchVrIfIndex_Object = MibTableColumn
hwPWVcSwitchVrIfIndex = _HwPWVcSwitchVrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 71),
    _HwPWVcSwitchVrIfIndex_Type()
)
hwPWVcSwitchVrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchVrIfIndex.setStatus("current")


class _HwPWVcSwitchVrID_Type(Unsigned32):
    """Custom type hwPWVcSwitchVrID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPWVcSwitchVrID_Type.__name__ = "Unsigned32"
_HwPWVcSwitchVrID_Object = MibTableColumn
hwPWVcSwitchVrID = _HwPWVcSwitchVrID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 72),
    _HwPWVcSwitchVrID_Type()
)
hwPWVcSwitchVrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWVcSwitchVrID.setStatus("current")


class _HwPWVcQosParaFromPWT_Type(Integer32):
    """Custom type hwPWVcQosParaFromPWT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cliOrMib", 1),
          ("pwTemplate", 2),
          ("unknown", 3))
    )


_HwPWVcQosParaFromPWT_Type.__name__ = "Integer32"
_HwPWVcQosParaFromPWT_Object = MibTableColumn
hwPWVcQosParaFromPWT = _HwPWVcQosParaFromPWT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 73),
    _HwPWVcQosParaFromPWT_Type()
)
hwPWVcQosParaFromPWT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcQosParaFromPWT.setStatus("current")


class _HwPWVcBfdParaFromPWT_Type(Integer32):
    """Custom type hwPWVcBfdParaFromPWT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cliOrMib", 1),
          ("pwTemplate", 2),
          ("unknown", 3))
    )


_HwPWVcBfdParaFromPWT_Type.__name__ = "Integer32"
_HwPWVcBfdParaFromPWT_Object = MibTableColumn
hwPWVcBfdParaFromPWT = _HwPWVcBfdParaFromPWT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 74),
    _HwPWVcBfdParaFromPWT_Type()
)
hwPWVcBfdParaFromPWT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcBfdParaFromPWT.setStatus("current")


class _HwPwVcNegotiateMode_Type(Integer32):
    """Custom type hwPwVcNegotiateMode based on Integer32"""
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
        *(("frr", 4),
          ("independent", 2),
          ("slaveOrMaster", 1),
          ("unknown", 3))
    )


_HwPwVcNegotiateMode_Type.__name__ = "Integer32"
_HwPwVcNegotiateMode_Object = MibTableColumn
hwPwVcNegotiateMode = _HwPwVcNegotiateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 75),
    _HwPwVcNegotiateMode_Type()
)
hwPwVcNegotiateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcNegotiateMode.setStatus("current")
_HwPwVcIsBypass_Type = TruthValue
_HwPwVcIsBypass_Object = MibTableColumn
hwPwVcIsBypass = _HwPwVcIsBypass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 76),
    _HwPwVcIsBypass_Type()
)
hwPwVcIsBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcIsBypass.setStatus("current")
_HwPwVcIsAdmin_Type = TruthValue
_HwPwVcIsAdmin_Object = MibTableColumn
hwPwVcIsAdmin = _HwPwVcIsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 77),
    _HwPwVcIsAdmin_Type()
)
hwPwVcIsAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcIsAdmin.setStatus("current")
_HwPwVcAdminPwIfIndex_Type = InterfaceIndexOrZero
_HwPwVcAdminPwIfIndex_Object = MibTableColumn
hwPwVcAdminPwIfIndex = _HwPwVcAdminPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 78),
    _HwPwVcAdminPwIfIndex_Type()
)
hwPwVcAdminPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcAdminPwIfIndex.setStatus("current")


class _HwPwVcAdminPwLinkStatus_Type(Integer32):
    """Custom type hwPwVcAdminPwLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_HwPwVcAdminPwLinkStatus_Type.__name__ = "Integer32"
_HwPwVcAdminPwLinkStatus_Object = MibTableColumn
hwPwVcAdminPwLinkStatus = _HwPwVcAdminPwLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 79),
    _HwPwVcAdminPwLinkStatus_Type()
)
hwPwVcAdminPwLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcAdminPwLinkStatus.setStatus("current")
_HwPwVcSwitchAdminPwIfIndex_Type = InterfaceIndexOrZero
_HwPwVcSwitchAdminPwIfIndex_Object = MibTableColumn
hwPwVcSwitchAdminPwIfIndex = _HwPwVcSwitchAdminPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 80),
    _HwPwVcSwitchAdminPwIfIndex_Type()
)
hwPwVcSwitchAdminPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchAdminPwIfIndex.setStatus("current")


class _HwPwVcSwitchAdminPwLinkStatus_Type(Integer32):
    """Custom type hwPwVcSwitchAdminPwLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_HwPwVcSwitchAdminPwLinkStatus_Type.__name__ = "Integer32"
_HwPwVcSwitchAdminPwLinkStatus_Object = MibTableColumn
hwPwVcSwitchAdminPwLinkStatus = _HwPwVcSwitchAdminPwLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 81),
    _HwPwVcSwitchAdminPwLinkStatus_Type()
)
hwPwVcSwitchAdminPwLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchAdminPwLinkStatus.setStatus("current")
_HwPwVcSwitchBackupAdminPwIfIndex_Type = InterfaceIndexOrZero
_HwPwVcSwitchBackupAdminPwIfIndex_Object = MibTableColumn
hwPwVcSwitchBackupAdminPwIfIndex = _HwPwVcSwitchBackupAdminPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 82),
    _HwPwVcSwitchBackupAdminPwIfIndex_Type()
)
hwPwVcSwitchBackupAdminPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupAdminPwIfIndex.setStatus("current")


class _HwPwVcSwitchBackupAdminPwLinkStatus_Type(Integer32):
    """Custom type hwPwVcSwitchBackupAdminPwLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_HwPwVcSwitchBackupAdminPwLinkStatus_Type.__name__ = "Integer32"
_HwPwVcSwitchBackupAdminPwLinkStatus_Object = MibTableColumn
hwPwVcSwitchBackupAdminPwLinkStatus = _HwPwVcSwitchBackupAdminPwLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 83),
    _HwPwVcSwitchBackupAdminPwLinkStatus_Type()
)
hwPwVcSwitchBackupAdminPwLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupAdminPwLinkStatus.setStatus("current")
_HwPwVcSwitchBackupVcId_Type = Unsigned32
_HwPwVcSwitchBackupVcId_Object = MibTableColumn
hwPwVcSwitchBackupVcId = _HwPwVcSwitchBackupVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 84),
    _HwPwVcSwitchBackupVcId_Type()
)
hwPwVcSwitchBackupVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcId.setStatus("current")
_HwPwVcSwitchBackupVcPeerAddrType_Type = InetAddressType
_HwPwVcSwitchBackupVcPeerAddrType_Object = MibTableColumn
hwPwVcSwitchBackupVcPeerAddrType = _HwPwVcSwitchBackupVcPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 85),
    _HwPwVcSwitchBackupVcPeerAddrType_Type()
)
hwPwVcSwitchBackupVcPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcPeerAddrType.setStatus("current")
_HwPwVcSwitchBackupVcPeerAddr_Type = IpAddress
_HwPwVcSwitchBackupVcPeerAddr_Object = MibTableColumn
hwPwVcSwitchBackupVcPeerAddr = _HwPwVcSwitchBackupVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 86),
    _HwPwVcSwitchBackupVcPeerAddr_Type()
)
hwPwVcSwitchBackupVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcPeerAddr.setStatus("current")
_HwPwVcSwitchBackupVcReceiveLabel_Type = Unsigned32
_HwPwVcSwitchBackupVcReceiveLabel_Object = MibTableColumn
hwPwVcSwitchBackupVcReceiveLabel = _HwPwVcSwitchBackupVcReceiveLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 87),
    _HwPwVcSwitchBackupVcReceiveLabel_Type()
)
hwPwVcSwitchBackupVcReceiveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcReceiveLabel.setStatus("current")
_HwPwVcSwitchBackupVcSendLabel_Type = Unsigned32
_HwPwVcSwitchBackupVcSendLabel_Object = MibTableColumn
hwPwVcSwitchBackupVcSendLabel = _HwPwVcSwitchBackupVcSendLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 88),
    _HwPwVcSwitchBackupVcSendLabel_Type()
)
hwPwVcSwitchBackupVcSendLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcSendLabel.setStatus("current")


class _HwPwVcSwitchBackupVcTnlPolicyName_Type(OctetString):
    """Custom type hwPwVcSwitchBackupVcTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwPwVcSwitchBackupVcTnlPolicyName_Type.__name__ = "OctetString"
_HwPwVcSwitchBackupVcTnlPolicyName_Object = MibTableColumn
hwPwVcSwitchBackupVcTnlPolicyName = _HwPwVcSwitchBackupVcTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 89),
    _HwPwVcSwitchBackupVcTnlPolicyName_Type()
)
hwPwVcSwitchBackupVcTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcTnlPolicyName.setStatus("current")
_HwPwVcSwitchBackupVcCir_Type = Unsigned32
_HwPwVcSwitchBackupVcCir_Object = MibTableColumn
hwPwVcSwitchBackupVcCir = _HwPwVcSwitchBackupVcCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 90),
    _HwPwVcSwitchBackupVcCir_Type()
)
hwPwVcSwitchBackupVcCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcCir.setStatus("current")
_HwPwVcSwitchBackupVcPir_Type = Unsigned32
_HwPwVcSwitchBackupVcPir_Object = MibTableColumn
hwPwVcSwitchBackupVcPir = _HwPwVcSwitchBackupVcPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 91),
    _HwPwVcSwitchBackupVcPir_Type()
)
hwPwVcSwitchBackupVcPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcPir.setStatus("current")


class _HwPwVcSwitchBackupVcQosProfile_Type(DisplayString):
    """Custom type hwPwVcSwitchBackupVcQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPwVcSwitchBackupVcQosProfile_Type.__name__ = "DisplayString"
_HwPwVcSwitchBackupVcQosProfile_Object = MibTableColumn
hwPwVcSwitchBackupVcQosProfile = _HwPwVcSwitchBackupVcQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 92),
    _HwPwVcSwitchBackupVcQosProfile_Type()
)
hwPwVcSwitchBackupVcQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcQosProfile.setStatus("current")


class _HwPwVcSlaveMasterMode_Type(Integer32):
    """Custom type hwPwVcSlaveMasterMode based on Integer32"""
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
        *(("bypass", 4),
          ("master", 2),
          ("slave", 1),
          ("unknown", 3))
    )


_HwPwVcSlaveMasterMode_Type.__name__ = "Integer32"
_HwPwVcSlaveMasterMode_Object = MibTableColumn
hwPwVcSlaveMasterMode = _HwPwVcSlaveMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 93),
    _HwPwVcSlaveMasterMode_Type()
)
hwPwVcSlaveMasterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSlaveMasterMode.setStatus("current")


class _HwPwVcSwitchVcSlaveMasterMode_Type(Integer32):
    """Custom type hwPwVcSwitchVcSlaveMasterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1),
          ("unknown", 3))
    )


_HwPwVcSwitchVcSlaveMasterMode_Type.__name__ = "Integer32"
_HwPwVcSwitchVcSlaveMasterMode_Object = MibTableColumn
hwPwVcSwitchVcSlaveMasterMode = _HwPwVcSwitchVcSlaveMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 94),
    _HwPwVcSwitchVcSlaveMasterMode_Type()
)
hwPwVcSwitchVcSlaveMasterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchVcSlaveMasterMode.setStatus("current")


class _HwPwVcSwitchBackupVcSlaveMasterMode_Type(Integer32):
    """Custom type hwPwVcSwitchBackupVcSlaveMasterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1),
          ("unknown", 3))
    )


_HwPwVcSwitchBackupVcSlaveMasterMode_Type.__name__ = "Integer32"
_HwPwVcSwitchBackupVcSlaveMasterMode_Object = MibTableColumn
hwPwVcSwitchBackupVcSlaveMasterMode = _HwPwVcSwitchBackupVcSlaveMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 95),
    _HwPwVcSwitchBackupVcSlaveMasterMode_Type()
)
hwPwVcSwitchBackupVcSlaveMasterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcSlaveMasterMode.setStatus("current")
_HwPwVcSwitchVcActive_Type = TruthValue
_HwPwVcSwitchVcActive_Object = MibTableColumn
hwPwVcSwitchVcActive = _HwPwVcSwitchVcActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 96),
    _HwPwVcSwitchVcActive_Type()
)
hwPwVcSwitchVcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchVcActive.setStatus("current")
_HwPwVcSwitchBackupVcActive_Type = TruthValue
_HwPwVcSwitchBackupVcActive_Object = MibTableColumn
hwPwVcSwitchBackupVcActive = _HwPwVcSwitchBackupVcActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 97),
    _HwPwVcSwitchBackupVcActive_Type()
)
hwPwVcSwitchBackupVcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcActive.setStatus("current")
_HwPwVcSwitchCwTrans_Type = TruthValue
_HwPwVcSwitchCwTrans_Object = MibTableColumn
hwPwVcSwitchCwTrans = _HwPwVcSwitchCwTrans_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 98),
    _HwPwVcSwitchCwTrans_Type()
)
hwPwVcSwitchCwTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchCwTrans.setStatus("current")


class _HwPwVcSwitchVcServiceName_Type(OctetString):
    """Custom type hwPwVcSwitchVcServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HwPwVcSwitchVcServiceName_Type.__name__ = "OctetString"
_HwPwVcSwitchVcServiceName_Object = MibTableColumn
hwPwVcSwitchVcServiceName = _HwPwVcSwitchVcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 99),
    _HwPwVcSwitchVcServiceName_Type()
)
hwPwVcSwitchVcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchVcServiceName.setStatus("current")


class _HwPwVcSwitchBackupVcServiceName_Type(OctetString):
    """Custom type hwPwVcSwitchBackupVcServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HwPwVcSwitchBackupVcServiceName_Type.__name__ = "OctetString"
_HwPwVcSwitchBackupVcServiceName_Object = MibTableColumn
hwPwVcSwitchBackupVcServiceName = _HwPwVcSwitchBackupVcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 1, 1, 100),
    _HwPwVcSwitchBackupVcServiceName_Type()
)
hwPwVcSwitchBackupVcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcSwitchBackupVcServiceName.setStatus("current")
_HwPWVcTnlTable_Object = MibTable
hwPWVcTnlTable = _HwPWVcTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwPWVcTnlTable.setStatus("current")
_HwPWVcTnlEntry_Object = MibTableRow
hwPWVcTnlEntry = _HwPWVcTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 2, 1)
)
hwPWVcTnlEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWVcID"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcType"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcTnlIndex"),
)
if mibBuilder.loadTexts:
    hwPWVcTnlEntry.setStatus("current")
_HwPWVcTnlIndex_Type = Unsigned32
_HwPWVcTnlIndex_Object = MibTableColumn
hwPWVcTnlIndex = _HwPWVcTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 2, 1, 1),
    _HwPWVcTnlIndex_Type()
)
hwPWVcTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWVcTnlIndex.setStatus("current")


class _HwPWVcTnlType_Type(Integer32):
    """Custom type hwPWVcTnlType based on Integer32"""
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
        *(("crLsp", 4),
          ("gre", 2),
          ("ipsec", 3),
          ("lsp", 1))
    )


_HwPWVcTnlType_Type.__name__ = "Integer32"
_HwPWVcTnlType_Object = MibTableColumn
hwPWVcTnlType = _HwPWVcTnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 2, 1, 2),
    _HwPWVcTnlType_Type()
)
hwPWVcTnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTnlType.setStatus("current")
_HwPWTnlForBfdIndex_Type = Unsigned32
_HwPWTnlForBfdIndex_Object = MibTableColumn
hwPWTnlForBfdIndex = _HwPWTnlForBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 2, 1, 3),
    _HwPWTnlForBfdIndex_Type()
)
hwPWTnlForBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWTnlForBfdIndex.setStatus("current")
_HwPWVcStatisticsTable_Object = MibTable
hwPWVcStatisticsTable = _HwPWVcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwPWVcStatisticsTable.setStatus("current")
_HwPWVcStatisticsEntry_Object = MibTableRow
hwPWVcStatisticsEntry = _HwPWVcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3, 1)
)
hwPWVcStatisticsEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWVcID"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcType"),
)
if mibBuilder.loadTexts:
    hwPWVcStatisticsEntry.setStatus("current")
_HwPWVcStatisticsRcvPkts_Type = Counter64
_HwPWVcStatisticsRcvPkts_Object = MibTableColumn
hwPWVcStatisticsRcvPkts = _HwPWVcStatisticsRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3, 1, 1),
    _HwPWVcStatisticsRcvPkts_Type()
)
hwPWVcStatisticsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcStatisticsRcvPkts.setStatus("current")
_HwPWVcStatisticsRcvBytes_Type = Counter64
_HwPWVcStatisticsRcvBytes_Object = MibTableColumn
hwPWVcStatisticsRcvBytes = _HwPWVcStatisticsRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3, 1, 2),
    _HwPWVcStatisticsRcvBytes_Type()
)
hwPWVcStatisticsRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcStatisticsRcvBytes.setStatus("current")
_HwPWVcStatisticsSndPkts_Type = Counter64
_HwPWVcStatisticsSndPkts_Object = MibTableColumn
hwPWVcStatisticsSndPkts = _HwPWVcStatisticsSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3, 1, 3),
    _HwPWVcStatisticsSndPkts_Type()
)
hwPWVcStatisticsSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcStatisticsSndPkts.setStatus("current")
_HwPWVcStatisticsSndBytes_Type = Counter64
_HwPWVcStatisticsSndBytes_Object = MibTableColumn
hwPWVcStatisticsSndBytes = _HwPWVcStatisticsSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 3, 1, 4),
    _HwPWVcStatisticsSndBytes_Type()
)
hwPWVcStatisticsSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcStatisticsSndBytes.setStatus("current")
_HwPWRemoteVcTable_Object = MibTable
hwPWRemoteVcTable = _HwPWRemoteVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwPWRemoteVcTable.setStatus("current")
_HwPWRemoteVcEntry_Object = MibTableRow
hwPWRemoteVcEntry = _HwPWRemoteVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1)
)
hwPWRemoteVcEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWVcID"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcType"),
)
if mibBuilder.loadTexts:
    hwPWRemoteVcEntry.setStatus("current")
_HwPWRemoteVcID_Type = Unsigned32
_HwPWRemoteVcID_Object = MibTableColumn
hwPWRemoteVcID = _HwPWRemoteVcID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 1),
    _HwPWRemoteVcID_Type()
)
hwPWRemoteVcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcID.setStatus("current")
_HwPWRemoteVcType_Type = HWL2VpnVcEncapsType
_HwPWRemoteVcType_Object = MibTableColumn
hwPWRemoteVcType = _HwPWRemoteVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 2),
    _HwPWRemoteVcType_Type()
)
hwPWRemoteVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcType.setStatus("current")


class _HwPWRemoteVcStatus_Type(Integer32):
    """Custom type hwPWRemoteVcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("plugout", 3),
          ("up", 1))
    )


_HwPWRemoteVcStatus_Type.__name__ = "Integer32"
_HwPWRemoteVcStatus_Object = MibTableColumn
hwPWRemoteVcStatus = _HwPWRemoteVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 3),
    _HwPWRemoteVcStatus_Type()
)
hwPWRemoteVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcStatus.setStatus("current")
_HwPWRemoteVcGroupID_Type = Unsigned32
_HwPWRemoteVcGroupID_Object = MibTableColumn
hwPWRemoteVcGroupID = _HwPWRemoteVcGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 4),
    _HwPWRemoteVcGroupID_Type()
)
hwPWRemoteVcGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcGroupID.setStatus("current")


class _HwPWRemoteVcMtu_Type(Unsigned32):
    """Custom type hwPWRemoteVcMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(46, 9600),
    )


_HwPWRemoteVcMtu_Type.__name__ = "Unsigned32"
_HwPWRemoteVcMtu_Object = MibTableColumn
hwPWRemoteVcMtu = _HwPWRemoteVcMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 5),
    _HwPWRemoteVcMtu_Type()
)
hwPWRemoteVcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcMtu.setStatus("current")
_HwPWRemoteVcCtrlword_Type = HWEnableValue
_HwPWRemoteVcCtrlword_Object = MibTableColumn
hwPWRemoteVcCtrlword = _HwPWRemoteVcCtrlword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 6),
    _HwPWRemoteVcCtrlword_Type()
)
hwPWRemoteVcCtrlword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcCtrlword.setStatus("current")


class _HwPWRemoteVcMaxAtmCells_Type(Unsigned32):
    """Custom type hwPWRemoteVcMaxAtmCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPWRemoteVcMaxAtmCells_Type.__name__ = "Unsigned32"
_HwPWRemoteVcMaxAtmCells_Object = MibTableColumn
hwPWRemoteVcMaxAtmCells = _HwPWRemoteVcMaxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 7),
    _HwPWRemoteVcMaxAtmCells_Type()
)
hwPWRemoteVcMaxAtmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcMaxAtmCells.setStatus("current")
_HwPWRemoteVcNotif_Type = TruthValue
_HwPWRemoteVcNotif_Object = MibTableColumn
hwPWRemoteVcNotif = _HwPWRemoteVcNotif_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 4, 1, 8),
    _HwPWRemoteVcNotif_Type()
)
hwPWRemoteVcNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWRemoteVcNotif.setStatus("current")
_HwPWVcSwitchNotifEnable_Type = HWEnableValue
_HwPWVcSwitchNotifEnable_Object = MibScalar
hwPWVcSwitchNotifEnable = _HwPWVcSwitchNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 5),
    _HwPWVcSwitchNotifEnable_Type()
)
hwPWVcSwitchNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPWVcSwitchNotifEnable.setStatus("current")
_HwPWVcUpDownNotifEnable_Type = HWEnableValue
_HwPWVcUpDownNotifEnable_Object = MibScalar
hwPWVcUpDownNotifEnable = _HwPWVcUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 6),
    _HwPWVcUpDownNotifEnable_Type()
)
hwPWVcUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPWVcUpDownNotifEnable.setStatus("current")
_HwPWVcDeletedNotifEnable_Type = HWEnableValue
_HwPWVcDeletedNotifEnable_Object = MibScalar
hwPWVcDeletedNotifEnable = _HwPWVcDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 7),
    _HwPWVcDeletedNotifEnable_Type()
)
hwPWVcDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPWVcDeletedNotifEnable.setStatus("current")
_HwPWVcStateChangeReason_Type = HWL2VpnStateChangeReason
_HwPWVcStateChangeReason_Object = MibScalar
hwPWVcStateChangeReason = _HwPWVcStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 8),
    _HwPWVcStateChangeReason_Type()
)
hwPWVcStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPWVcStateChangeReason.setStatus("current")
_HwPWVcSwitchRmtID_Type = Unsigned32
_HwPWVcSwitchRmtID_Object = MibScalar
hwPWVcSwitchRmtID = _HwPWVcSwitchRmtID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 9),
    _HwPWVcSwitchRmtID_Type()
)
hwPWVcSwitchRmtID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPWVcSwitchRmtID.setStatus("current")
_HwLdpPWStateChangeReason_Type = HWLdpPwStateChangeReason
_HwLdpPWStateChangeReason_Object = MibScalar
hwLdpPWStateChangeReason = _HwLdpPWStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 10),
    _HwLdpPWStateChangeReason_Type()
)
hwLdpPWStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpPWStateChangeReason.setStatus("current")
_HwPWVcTDMPerfCurrentTable_Object = MibTable
hwPWVcTDMPerfCurrentTable = _HwPWVcTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentTable.setStatus("current")
_HwPWVcTDMPerfCurrentEntry_Object = MibTableRow
hwPWVcTDMPerfCurrentEntry = _HwPWVcTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1)
)
hwPWVcTDMPerfCurrentEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWVcID"),
    (0, "HUAWEI-PWE3-MIB", "hwPWVcType"),
)
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentEntry.setStatus("current")
_HwPWVcTDMPerfCurrentMissingPkts_Type = Unsigned32
_HwPWVcTDMPerfCurrentMissingPkts_Object = MibTableColumn
hwPWVcTDMPerfCurrentMissingPkts = _HwPWVcTDMPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 1),
    _HwPWVcTDMPerfCurrentMissingPkts_Type()
)
hwPWVcTDMPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentMissingPkts.setStatus("current")
_HwPWVcTDMPerfCurrentJtrBfrOverruns_Type = Unsigned32
_HwPWVcTDMPerfCurrentJtrBfrOverruns_Object = MibTableColumn
hwPWVcTDMPerfCurrentJtrBfrOverruns = _HwPWVcTDMPerfCurrentJtrBfrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 2),
    _HwPWVcTDMPerfCurrentJtrBfrOverruns_Type()
)
hwPWVcTDMPerfCurrentJtrBfrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentJtrBfrOverruns.setStatus("current")
_HwPWVcTDMPerfCurrentJtrBfrUnderruns_Type = Unsigned32
_HwPWVcTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
hwPWVcTDMPerfCurrentJtrBfrUnderruns = _HwPWVcTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 3),
    _HwPWVcTDMPerfCurrentJtrBfrUnderruns_Type()
)
hwPWVcTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_HwPWVcTDMPerfCurrentMisOrderDropped_Type = Unsigned32
_HwPWVcTDMPerfCurrentMisOrderDropped_Object = MibTableColumn
hwPWVcTDMPerfCurrentMisOrderDropped = _HwPWVcTDMPerfCurrentMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 4),
    _HwPWVcTDMPerfCurrentMisOrderDropped_Type()
)
hwPWVcTDMPerfCurrentMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentMisOrderDropped.setStatus("current")
_HwPWVcTDMPerfCurrentMalformedPkt_Type = Unsigned32
_HwPWVcTDMPerfCurrentMalformedPkt_Object = MibTableColumn
hwPWVcTDMPerfCurrentMalformedPkt = _HwPWVcTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 5),
    _HwPWVcTDMPerfCurrentMalformedPkt_Type()
)
hwPWVcTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentMalformedPkt.setStatus("current")
_HwPWVcTDMPerfCurrentESs_Type = Unsigned32
_HwPWVcTDMPerfCurrentESs_Object = MibTableColumn
hwPWVcTDMPerfCurrentESs = _HwPWVcTDMPerfCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 6),
    _HwPWVcTDMPerfCurrentESs_Type()
)
hwPWVcTDMPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentESs.setStatus("current")
_HwPWVcTDMPerfCurrentSESs_Type = Unsigned32
_HwPWVcTDMPerfCurrentSESs_Object = MibTableColumn
hwPWVcTDMPerfCurrentSESs = _HwPWVcTDMPerfCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 7),
    _HwPWVcTDMPerfCurrentSESs_Type()
)
hwPWVcTDMPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentSESs.setStatus("current")
_HwPWVcTDMPerfCurrentUASs_Type = Unsigned32
_HwPWVcTDMPerfCurrentUASs_Object = MibTableColumn
hwPWVcTDMPerfCurrentUASs = _HwPWVcTDMPerfCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 1, 11, 1, 8),
    _HwPWVcTDMPerfCurrentUASs_Type()
)
hwPWVcTDMPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentUASs.setStatus("current")
_HwPwe3MIBTraps_ObjectIdentity = ObjectIdentity
hwPwe3MIBTraps = _HwPwe3MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2)
)
_HwSvcObjects_ObjectIdentity = ObjectIdentity
hwSvcObjects = _HwSvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3)
)
_HwSvcTable_Object = MibTable
hwSvcTable = _HwSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwSvcTable.setStatus("current")
_HwSvcEntry_Object = MibTableRow
hwSvcEntry = _HwSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1)
)
hwSvcEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwSvcIfIndex"),
)
if mibBuilder.loadTexts:
    hwSvcEntry.setStatus("current")
_HwSvcIfIndex_Type = InterfaceIndexOrZero
_HwSvcIfIndex_Object = MibTableColumn
hwSvcIfIndex = _HwSvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 1),
    _HwSvcIfIndex_Type()
)
hwSvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSvcIfIndex.setStatus("current")
_HwSvcID_Type = Unsigned32
_HwSvcID_Object = MibTableColumn
hwSvcID = _HwSvcID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 2),
    _HwSvcID_Type()
)
hwSvcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcID.setStatus("current")
_HwSvcType_Type = HWL2VpnVcEncapsType
_HwSvcType_Object = MibTableColumn
hwSvcType = _HwSvcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 3),
    _HwSvcType_Type()
)
hwSvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcType.setStatus("current")


class _HwSvcPeerAddrType_Type(InetAddressType):
    """Custom type hwSvcPeerAddrType based on InetAddressType"""


_HwSvcPeerAddrType_Object = MibTableColumn
hwSvcPeerAddrType = _HwSvcPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 4),
    _HwSvcPeerAddrType_Type()
)
hwSvcPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPeerAddrType.setStatus("current")
_HwSvcPeerAddr_Type = IpAddress
_HwSvcPeerAddr_Object = MibTableColumn
hwSvcPeerAddr = _HwSvcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 5),
    _HwSvcPeerAddr_Type()
)
hwSvcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPeerAddr.setStatus("current")


class _HwSvcStatus_Type(Integer32):
    """Custom type hwSvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("plugout", 3),
          ("up", 1))
    )


_HwSvcStatus_Type.__name__ = "Integer32"
_HwSvcStatus_Object = MibTableColumn
hwSvcStatus = _HwSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 6),
    _HwSvcStatus_Type()
)
hwSvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcStatus.setStatus("current")
_HwSvcInboundLabel_Type = Unsigned32
_HwSvcInboundLabel_Object = MibTableColumn
hwSvcInboundLabel = _HwSvcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 7),
    _HwSvcInboundLabel_Type()
)
hwSvcInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcInboundLabel.setStatus("current")
_HwSvcOutboundLabel_Type = Unsigned32
_HwSvcOutboundLabel_Object = MibTableColumn
hwSvcOutboundLabel = _HwSvcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 8),
    _HwSvcOutboundLabel_Type()
)
hwSvcOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcOutboundLabel.setStatus("current")
_HwSvcGroupID_Type = Unsigned32
_HwSvcGroupID_Object = MibTableColumn
hwSvcGroupID = _HwSvcGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 9),
    _HwSvcGroupID_Type()
)
hwSvcGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcGroupID.setStatus("current")


class _HwSvcAcStatus_Type(Integer32):
    """Custom type hwSvcAcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("plugout", 3),
          ("up", 1))
    )


_HwSvcAcStatus_Type.__name__ = "Integer32"
_HwSvcAcStatus_Object = MibTableColumn
hwSvcAcStatus = _HwSvcAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 10),
    _HwSvcAcStatus_Type()
)
hwSvcAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcAcStatus.setStatus("current")


class _HwSvcACOAMStatus_Type(Integer32):
    """Custom type hwSvcACOAMStatus based on Integer32"""
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


_HwSvcACOAMStatus_Type.__name__ = "Integer32"
_HwSvcACOAMStatus_Object = MibTableColumn
hwSvcACOAMStatus = _HwSvcACOAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 11),
    _HwSvcACOAMStatus_Type()
)
hwSvcACOAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcACOAMStatus.setStatus("current")


class _HwSvcMtu_Type(Integer32):
    """Custom type hwSvcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(46, 9600),
    )


_HwSvcMtu_Type.__name__ = "Integer32"
_HwSvcMtu_Object = MibTableColumn
hwSvcMtu = _HwSvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 12),
    _HwSvcMtu_Type()
)
hwSvcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcMtu.setStatus("current")
_HwSvcCtrlWord_Type = HWEnableValue
_HwSvcCtrlWord_Object = MibTableColumn
hwSvcCtrlWord = _HwSvcCtrlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 13),
    _HwSvcCtrlWord_Type()
)
hwSvcCtrlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcCtrlWord.setStatus("current")


class _HwSvcVCCV_Type(Bits):
    """Custom type hwSvcVCCV based on Bits"""
    namedValues = NamedValues(
        *(("ccAlert", 1),
          ("ccCw", 0),
          ("ccLabel", 2),
          ("cvBfd", 5),
          ("cvIcmpping", 3),
          ("cvLspping", 4))
    )

_HwSvcVCCV_Type.__name__ = "Bits"
_HwSvcVCCV_Object = MibTableColumn
hwSvcVCCV = _HwSvcVCCV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 14),
    _HwSvcVCCV_Type()
)
hwSvcVCCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcVCCV.setStatus("current")


class _HwSvcBandWidth_Type(Unsigned32):
    """Custom type hwSvcBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwSvcBandWidth_Type.__name__ = "Unsigned32"
_HwSvcBandWidth_Object = MibTableColumn
hwSvcBandWidth = _HwSvcBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 15),
    _HwSvcBandWidth_Type()
)
hwSvcBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcBandWidth.setStatus("current")


class _HwSvcMaxAtmCells_Type(Unsigned32):
    """Custom type hwSvcMaxAtmCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_HwSvcMaxAtmCells_Type.__name__ = "Unsigned32"
_HwSvcMaxAtmCells_Object = MibTableColumn
hwSvcMaxAtmCells = _HwSvcMaxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 16),
    _HwSvcMaxAtmCells_Type()
)
hwSvcMaxAtmCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcMaxAtmCells.setStatus("current")


class _HwSvcTnlPolicyName_Type(OctetString):
    """Custom type hwSvcTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HwSvcTnlPolicyName_Type.__name__ = "OctetString"
_HwSvcTnlPolicyName_Object = MibTableColumn
hwSvcTnlPolicyName = _HwSvcTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 17),
    _HwSvcTnlPolicyName_Type()
)
hwSvcTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcTnlPolicyName.setStatus("current")
_HwSvcQoSBehaviorIndex_Type = Unsigned32
_HwSvcQoSBehaviorIndex_Object = MibTableColumn
hwSvcQoSBehaviorIndex = _HwSvcQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 18),
    _HwSvcQoSBehaviorIndex_Type()
)
hwSvcQoSBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcQoSBehaviorIndex.setStatus("current")


class _HwSvcPWTemplateName_Type(OctetString):
    """Custom type hwSvcPWTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwSvcPWTemplateName_Type.__name__ = "OctetString"
_HwSvcPWTemplateName_Object = MibTableColumn
hwSvcPWTemplateName = _HwSvcPWTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 19),
    _HwSvcPWTemplateName_Type()
)
hwSvcPWTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPWTemplateName.setStatus("current")
_HwSvcUpTime_Type = Unsigned32
_HwSvcUpTime_Object = MibTableColumn
hwSvcUpTime = _HwSvcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 20),
    _HwSvcUpTime_Type()
)
hwSvcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcUpTime.setStatus("current")
_HwSvcOAMSync_Type = TruthValue
_HwSvcOAMSync_Object = MibTableColumn
hwSvcOAMSync = _HwSvcOAMSync_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 21),
    _HwSvcOAMSync_Type()
)
hwSvcOAMSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcOAMSync.setStatus("current")
_HwSvcForBfdIndex_Type = Unsigned32
_HwSvcForBfdIndex_Object = MibTableColumn
hwSvcForBfdIndex = _HwSvcForBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 22),
    _HwSvcForBfdIndex_Type()
)
hwSvcForBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcForBfdIndex.setStatus("current")
_HwSvcSecondary_Type = TruthValue
_HwSvcSecondary_Object = MibTableColumn
hwSvcSecondary = _HwSvcSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 23),
    _HwSvcSecondary_Type()
)
hwSvcSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcSecondary.setStatus("current")
_HwSvcDelayTime_Type = Unsigned32
_HwSvcDelayTime_Object = MibTableColumn
hwSvcDelayTime = _HwSvcDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 24),
    _HwSvcDelayTime_Type()
)
hwSvcDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcDelayTime.setStatus("current")


class _HwSvcReroutePolicy_Type(Integer32):
    """Custom type hwSvcReroutePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
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
        *(("delay", 1),
          ("err", 5),
          ("immediately", 2),
          ("invalid", 6),
          ("never", 3),
          ("none", 4))
    )


_HwSvcReroutePolicy_Type.__name__ = "Integer32"
_HwSvcReroutePolicy_Object = MibTableColumn
hwSvcReroutePolicy = _HwSvcReroutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 25),
    _HwSvcReroutePolicy_Type()
)
hwSvcReroutePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcReroutePolicy.setStatus("current")
_HwSvcResumeTime_Type = Unsigned32
_HwSvcResumeTime_Object = MibTableColumn
hwSvcResumeTime = _HwSvcResumeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 26),
    _HwSvcResumeTime_Type()
)
hwSvcResumeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcResumeTime.setStatus("current")
_HwSvcRerouteReason_Type = HWL2VpnStateChangeReason
_HwSvcRerouteReason_Object = MibTableColumn
hwSvcRerouteReason = _HwSvcRerouteReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 27),
    _HwSvcRerouteReason_Type()
)
hwSvcRerouteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcRerouteReason.setStatus("current")
_HwSvcLastRerouteTime_Type = Unsigned32
_HwSvcLastRerouteTime_Object = MibTableColumn
hwSvcLastRerouteTime = _HwSvcLastRerouteTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 28),
    _HwSvcLastRerouteTime_Type()
)
hwSvcLastRerouteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcLastRerouteTime.setStatus("current")
_HwSvcManualSetFault_Type = TruthValue
_HwSvcManualSetFault_Object = MibTableColumn
hwSvcManualSetFault = _HwSvcManualSetFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 29),
    _HwSvcManualSetFault_Type()
)
hwSvcManualSetFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcManualSetFault.setStatus("current")
_HwSvcActive_Type = TruthValue
_HwSvcActive_Object = MibTableColumn
hwSvcActive = _HwSvcActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 30),
    _HwSvcActive_Type()
)
hwSvcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcActive.setStatus("current")


class _HwSvcUpStartTime_Type(DisplayString):
    """Custom type hwSvcUpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSvcUpStartTime_Type.__name__ = "DisplayString"
_HwSvcUpStartTime_Object = MibTableColumn
hwSvcUpStartTime = _HwSvcUpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 31),
    _HwSvcUpStartTime_Type()
)
hwSvcUpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcUpStartTime.setStatus("current")
_HwSvcUpSumTime_Type = Unsigned32
_HwSvcUpSumTime_Object = MibTableColumn
hwSvcUpSumTime = _HwSvcUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 32),
    _HwSvcUpSumTime_Type()
)
hwSvcUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcUpSumTime.setStatus("current")


class _HwSvcAtmPackOvertime_Type(Unsigned32):
    """Custom type hwSvcAtmPackOvertime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 50000),
    )


_HwSvcAtmPackOvertime_Type.__name__ = "Unsigned32"
_HwSvcAtmPackOvertime_Object = MibTableColumn
hwSvcAtmPackOvertime = _HwSvcAtmPackOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 33),
    _HwSvcAtmPackOvertime_Type()
)
hwSvcAtmPackOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcAtmPackOvertime.setStatus("current")


class _HwSvcPwJitterBufferDepth_Type(Unsigned32):
    """Custom type hwSvcPwJitterBufferDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwSvcPwJitterBufferDepth_Type.__name__ = "Unsigned32"
_HwSvcPwJitterBufferDepth_Object = MibTableColumn
hwSvcPwJitterBufferDepth = _HwSvcPwJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 34),
    _HwSvcPwJitterBufferDepth_Type()
)
hwSvcPwJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPwJitterBufferDepth.setStatus("current")


class _HwSvcPwTdmEncapsulationNum_Type(Unsigned32):
    """Custom type hwSvcPwTdmEncapsulationNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwSvcPwTdmEncapsulationNum_Type.__name__ = "Unsigned32"
_HwSvcPwTdmEncapsulationNum_Object = MibTableColumn
hwSvcPwTdmEncapsulationNum = _HwSvcPwTdmEncapsulationNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 35),
    _HwSvcPwTdmEncapsulationNum_Type()
)
hwSvcPwTdmEncapsulationNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPwTdmEncapsulationNum.setStatus("current")


class _HwSvcPwIdleCode_Type(Unsigned32):
    """Custom type hwSvcPwIdleCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwSvcPwIdleCode_Type.__name__ = "Unsigned32"
_HwSvcPwIdleCode_Object = MibTableColumn
hwSvcPwIdleCode = _HwSvcPwIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 36),
    _HwSvcPwIdleCode_Type()
)
hwSvcPwIdleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPwIdleCode.setStatus("current")
_HwSvcPwRtpHeader_Type = Unsigned32
_HwSvcPwRtpHeader_Object = MibTableColumn
hwSvcPwRtpHeader = _HwSvcPwRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 37),
    _HwSvcPwRtpHeader_Type()
)
hwSvcPwRtpHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPwRtpHeader.setStatus("current")


class _HwSvcRawOrTagged_Type(Integer32):
    """Custom type hwSvcRawOrTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("rawTagNotConfiged", 3),
          ("tagged", 2))
    )


_HwSvcRawOrTagged_Type.__name__ = "Integer32"
_HwSvcRawOrTagged_Object = MibTableColumn
hwSvcRawOrTagged = _HwSvcRawOrTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 38),
    _HwSvcRawOrTagged_Type()
)
hwSvcRawOrTagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcRawOrTagged.setStatus("current")


class _HwSvcInterworkingType_Type(Integer32):
    """Custom type hwSvcInterworkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipInterWorking", 1),
          ("ipLayer2", 2),
          ("ipUnknown", 3))
    )


_HwSvcInterworkingType_Type.__name__ = "Integer32"
_HwSvcInterworkingType_Object = MibTableColumn
hwSvcInterworkingType = _HwSvcInterworkingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 39),
    _HwSvcInterworkingType_Type()
)
hwSvcInterworkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcInterworkingType.setStatus("current")
_HwSvcCir_Type = Unsigned32
_HwSvcCir_Object = MibTableColumn
hwSvcCir = _HwSvcCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 40),
    _HwSvcCir_Type()
)
hwSvcCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcCir.setStatus("current")
_HwSvcPir_Type = Unsigned32
_HwSvcPir_Object = MibTableColumn
hwSvcPir = _HwSvcPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 41),
    _HwSvcPir_Type()
)
hwSvcPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcPir.setStatus("current")


class _HwSvcQosProfile_Type(DisplayString):
    """Custom type hwSvcQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwSvcQosProfile_Type.__name__ = "DisplayString"
_HwSvcQosProfile_Object = MibTableColumn
hwSvcQosProfile = _HwSvcQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 42),
    _HwSvcQosProfile_Type()
)
hwSvcQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcQosProfile.setStatus("current")
_HwSvcRowStatus_Type = RowStatus
_HwSvcRowStatus_Object = MibTableColumn
hwSvcRowStatus = _HwSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 1, 1, 51),
    _HwSvcRowStatus_Type()
)
hwSvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSvcRowStatus.setStatus("current")
_HwSvcTnlTable_Object = MibTable
hwSvcTnlTable = _HwSvcTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwSvcTnlTable.setStatus("current")
_HwSvcTnlEntry_Object = MibTableRow
hwSvcTnlEntry = _HwSvcTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 2, 1)
)
hwSvcTnlEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwSvcIfIndex"),
    (0, "HUAWEI-PWE3-MIB", "hwSvcTnlIndex"),
)
if mibBuilder.loadTexts:
    hwSvcTnlEntry.setStatus("current")
_HwSvcTnlIndex_Type = Unsigned32
_HwSvcTnlIndex_Object = MibTableColumn
hwSvcTnlIndex = _HwSvcTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 2, 1, 1),
    _HwSvcTnlIndex_Type()
)
hwSvcTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSvcTnlIndex.setStatus("current")


class _HwSvcTnlType_Type(Integer32):
    """Custom type hwSvcTnlType based on Integer32"""
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
        *(("crLsp", 4),
          ("gre", 2),
          ("ipsec", 3),
          ("lsp", 1))
    )


_HwSvcTnlType_Type.__name__ = "Integer32"
_HwSvcTnlType_Object = MibTableColumn
hwSvcTnlType = _HwSvcTnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 2, 1, 2),
    _HwSvcTnlType_Type()
)
hwSvcTnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcTnlType.setStatus("current")
_HwSvcTnlForBfdIndex_Type = Unsigned32
_HwSvcTnlForBfdIndex_Object = MibTableColumn
hwSvcTnlForBfdIndex = _HwSvcTnlForBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 2, 1, 3),
    _HwSvcTnlForBfdIndex_Type()
)
hwSvcTnlForBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcTnlForBfdIndex.setStatus("current")
_HwSvcStatisticsTable_Object = MibTable
hwSvcStatisticsTable = _HwSvcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwSvcStatisticsTable.setStatus("current")
_HwSvcStatisticsEntry_Object = MibTableRow
hwSvcStatisticsEntry = _HwSvcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3, 1)
)
hwSvcStatisticsEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwSvcIfIndex"),
)
if mibBuilder.loadTexts:
    hwSvcStatisticsEntry.setStatus("current")
_HwSvcStatisticsRcvPkts_Type = Counter64
_HwSvcStatisticsRcvPkts_Object = MibTableColumn
hwSvcStatisticsRcvPkts = _HwSvcStatisticsRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3, 1, 1),
    _HwSvcStatisticsRcvPkts_Type()
)
hwSvcStatisticsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcStatisticsRcvPkts.setStatus("current")
_HwSvcStatisticsRcvBytes_Type = Counter64
_HwSvcStatisticsRcvBytes_Object = MibTableColumn
hwSvcStatisticsRcvBytes = _HwSvcStatisticsRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3, 1, 2),
    _HwSvcStatisticsRcvBytes_Type()
)
hwSvcStatisticsRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcStatisticsRcvBytes.setStatus("current")
_HwSvcStatisticsSndPkts_Type = Counter64
_HwSvcStatisticsSndPkts_Object = MibTableColumn
hwSvcStatisticsSndPkts = _HwSvcStatisticsSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3, 1, 3),
    _HwSvcStatisticsSndPkts_Type()
)
hwSvcStatisticsSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcStatisticsSndPkts.setStatus("current")
_HwSvcStatisticsSndBytes_Type = Counter64
_HwSvcStatisticsSndBytes_Object = MibTableColumn
hwSvcStatisticsSndBytes = _HwSvcStatisticsSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 3, 1, 4),
    _HwSvcStatisticsSndBytes_Type()
)
hwSvcStatisticsSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcStatisticsSndBytes.setStatus("current")
_HwSvcSwitchNotifEnable_Type = HWEnableValue
_HwSvcSwitchNotifEnable_Object = MibScalar
hwSvcSwitchNotifEnable = _HwSvcSwitchNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 4),
    _HwSvcSwitchNotifEnable_Type()
)
hwSvcSwitchNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSvcSwitchNotifEnable.setStatus("current")
_HwSvcUpDownNotifEnable_Type = HWEnableValue
_HwSvcUpDownNotifEnable_Object = MibScalar
hwSvcUpDownNotifEnable = _HwSvcUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 5),
    _HwSvcUpDownNotifEnable_Type()
)
hwSvcUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSvcUpDownNotifEnable.setStatus("current")
_HwSvcDeletedNotifEnable_Type = HWEnableValue
_HwSvcDeletedNotifEnable_Object = MibScalar
hwSvcDeletedNotifEnable = _HwSvcDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 6),
    _HwSvcDeletedNotifEnable_Type()
)
hwSvcDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSvcDeletedNotifEnable.setStatus("current")
_HwSvcStateChangeReason_Type = HWL2VpnStateChangeReason
_HwSvcStateChangeReason_Object = MibScalar
hwSvcStateChangeReason = _HwSvcStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 3, 7),
    _HwSvcStateChangeReason_Type()
)
hwSvcStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSvcStateChangeReason.setStatus("current")
_HwL2vpnSvcMIBTraps_ObjectIdentity = ObjectIdentity
hwL2vpnSvcMIBTraps = _HwL2vpnSvcMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4)
)
_HwPWTemplateTable_Object = MibTable
hwPWTemplateTable = _HwPWTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5)
)
if mibBuilder.loadTexts:
    hwPWTemplateTable.setStatus("current")
_HwPWTemplateEntry_Object = MibTableRow
hwPWTemplateEntry = _HwPWTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1)
)
hwPWTemplateEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWTemplateName"),
)
if mibBuilder.loadTexts:
    hwPWTemplateEntry.setStatus("current")


class _HwPWTemplateName_Type(OctetString):
    """Custom type hwPWTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HwPWTemplateName_Type.__name__ = "OctetString"
_HwPWTemplateName_Object = MibTableColumn
hwPWTemplateName = _HwPWTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 1),
    _HwPWTemplateName_Type()
)
hwPWTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWTemplateName.setStatus("current")


class _HwPWTemplatePeerAddrType_Type(InetAddressType):
    """Custom type hwPWTemplatePeerAddrType based on InetAddressType"""


_HwPWTemplatePeerAddrType_Object = MibTableColumn
hwPWTemplatePeerAddrType = _HwPWTemplatePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 2),
    _HwPWTemplatePeerAddrType_Type()
)
hwPWTemplatePeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePeerAddrType.setStatus("current")
_HwPWTemplatePeerAddr_Type = IpAddress
_HwPWTemplatePeerAddr_Object = MibTableColumn
hwPWTemplatePeerAddr = _HwPWTemplatePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 3),
    _HwPWTemplatePeerAddr_Type()
)
hwPWTemplatePeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePeerAddr.setStatus("current")
_HwPWTemplateCtrlword_Type = HWEnableValue
_HwPWTemplateCtrlword_Object = MibTableColumn
hwPWTemplateCtrlword = _HwPWTemplateCtrlword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 4),
    _HwPWTemplateCtrlword_Type()
)
hwPWTemplateCtrlword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateCtrlword.setStatus("current")


class _HwPWTemplateVCCV_Type(Bits):
    """Custom type hwPWTemplateVCCV based on Bits"""
    namedValues = NamedValues(
        *(("ccAlert", 1),
          ("ccCw", 0),
          ("ccLabel", 2),
          ("ccTtl", 6),
          ("cvBfd", 5),
          ("cvIcmpping", 3),
          ("cvLspping", 4))
    )

_HwPWTemplateVCCV_Type.__name__ = "Bits"
_HwPWTemplateVCCV_Object = MibTableColumn
hwPWTemplateVCCV = _HwPWTemplateVCCV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 5),
    _HwPWTemplateVCCV_Type()
)
hwPWTemplateVCCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateVCCV.setStatus("current")
_HwPWTemplateFrag_Type = TruthValue
_HwPWTemplateFrag_Object = MibTableColumn
hwPWTemplateFrag = _HwPWTemplateFrag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 6),
    _HwPWTemplateFrag_Type()
)
hwPWTemplateFrag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateFrag.setStatus("current")


class _HwPWTemplateBandwidth_Type(Integer32):
    """Custom type hwPWTemplateBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_HwPWTemplateBandwidth_Type.__name__ = "Integer32"
_HwPWTemplateBandwidth_Object = MibTableColumn
hwPWTemplateBandwidth = _HwPWTemplateBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 7),
    _HwPWTemplateBandwidth_Type()
)
hwPWTemplateBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWTemplateBandwidth.setStatus("current")


class _HwPWTemplateTnlPolicyName_Type(OctetString):
    """Custom type hwPWTemplateTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HwPWTemplateTnlPolicyName_Type.__name__ = "OctetString"
_HwPWTemplateTnlPolicyName_Object = MibTableColumn
hwPWTemplateTnlPolicyName = _HwPWTemplateTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 8),
    _HwPWTemplateTnlPolicyName_Type()
)
hwPWTemplateTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateTnlPolicyName.setStatus("current")
_HwPWTemplateQoSBehaviorIndex_Type = Integer32
_HwPWTemplateQoSBehaviorIndex_Object = MibTableColumn
hwPWTemplateQoSBehaviorIndex = _HwPWTemplateQoSBehaviorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 9),
    _HwPWTemplateQoSBehaviorIndex_Type()
)
hwPWTemplateQoSBehaviorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateQoSBehaviorIndex.setStatus("current")


class _HwPWTemplateExplicitPathName_Type(OctetString):
    """Custom type hwPWTemplateExplicitPathName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPWTemplateExplicitPathName_Type.__name__ = "OctetString"
_HwPWTemplateExplicitPathName_Object = MibTableColumn
hwPWTemplateExplicitPathName = _HwPWTemplateExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 10),
    _HwPWTemplateExplicitPathName_Type()
)
hwPWTemplateExplicitPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateExplicitPathName.setStatus("current")


class _HwPWTemplateBFDDetectMultiplier_Type(Unsigned32):
    """Custom type hwPWTemplateBFDDetectMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 50),
    )


_HwPWTemplateBFDDetectMultiplier_Type.__name__ = "Unsigned32"
_HwPWTemplateBFDDetectMultiplier_Object = MibTableColumn
hwPWTemplateBFDDetectMultiplier = _HwPWTemplateBFDDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 11),
    _HwPWTemplateBFDDetectMultiplier_Type()
)
hwPWTemplateBFDDetectMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateBFDDetectMultiplier.setStatus("current")


class _HwPWTemplateBFDMinReceiveInterval_Type(Unsigned32):
    """Custom type hwPWTemplateBFDMinReceiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1000),
    )


_HwPWTemplateBFDMinReceiveInterval_Type.__name__ = "Unsigned32"
_HwPWTemplateBFDMinReceiveInterval_Object = MibTableColumn
hwPWTemplateBFDMinReceiveInterval = _HwPWTemplateBFDMinReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 12),
    _HwPWTemplateBFDMinReceiveInterval_Type()
)
hwPWTemplateBFDMinReceiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateBFDMinReceiveInterval.setStatus("current")


class _HwPWTemplateBFDMinTransmitInterval_Type(Unsigned32):
    """Custom type hwPWTemplateBFDMinTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1000),
    )


_HwPWTemplateBFDMinTransmitInterval_Type.__name__ = "Unsigned32"
_HwPWTemplateBFDMinTransmitInterval_Object = MibTableColumn
hwPWTemplateBFDMinTransmitInterval = _HwPWTemplateBFDMinTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 13),
    _HwPWTemplateBFDMinTransmitInterval_Type()
)
hwPWTemplateBFDMinTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateBFDMinTransmitInterval.setStatus("current")
_HwPWTemplateDynamicBFDDetect_Type = TruthValue
_HwPWTemplateDynamicBFDDetect_Object = MibTableColumn
hwPWTemplateDynamicBFDDetect = _HwPWTemplateDynamicBFDDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 14),
    _HwPWTemplateDynamicBFDDetect_Type()
)
hwPWTemplateDynamicBFDDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateDynamicBFDDetect.setStatus("current")


class _HwPWTemplateMaxAtmCells_Type(Unsigned32):
    """Custom type hwPWTemplateMaxAtmCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_HwPWTemplateMaxAtmCells_Type.__name__ = "Unsigned32"
_HwPWTemplateMaxAtmCells_Object = MibTableColumn
hwPWTemplateMaxAtmCells = _HwPWTemplateMaxAtmCells_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 15),
    _HwPWTemplateMaxAtmCells_Type()
)
hwPWTemplateMaxAtmCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateMaxAtmCells.setStatus("current")


class _HwPWTemplateAtmPackOvertime_Type(Unsigned32):
    """Custom type hwPWTemplateAtmPackOvertime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 50000),
    )


_HwPWTemplateAtmPackOvertime_Type.__name__ = "Unsigned32"
_HwPWTemplateAtmPackOvertime_Object = MibTableColumn
hwPWTemplateAtmPackOvertime = _HwPWTemplateAtmPackOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 16),
    _HwPWTemplateAtmPackOvertime_Type()
)
hwPWTemplateAtmPackOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateAtmPackOvertime.setStatus("current")


class _HwPWTemplatePwJitterBufferDepth_Type(Unsigned32):
    """Custom type hwPWTemplatePwJitterBufferDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwPWTemplatePwJitterBufferDepth_Type.__name__ = "Unsigned32"
_HwPWTemplatePwJitterBufferDepth_Object = MibTableColumn
hwPWTemplatePwJitterBufferDepth = _HwPWTemplatePwJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 17),
    _HwPWTemplatePwJitterBufferDepth_Type()
)
hwPWTemplatePwJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePwJitterBufferDepth.setStatus("current")


class _HwPWTemplatePwTdmEncapsulationNum_Type(Unsigned32):
    """Custom type hwPWTemplatePwTdmEncapsulationNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwPWTemplatePwTdmEncapsulationNum_Type.__name__ = "Unsigned32"
_HwPWTemplatePwTdmEncapsulationNum_Object = MibTableColumn
hwPWTemplatePwTdmEncapsulationNum = _HwPWTemplatePwTdmEncapsulationNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 18),
    _HwPWTemplatePwTdmEncapsulationNum_Type()
)
hwPWTemplatePwTdmEncapsulationNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePwTdmEncapsulationNum.setStatus("current")


class _HwPWTemplatePwIdleCode_Type(Unsigned32):
    """Custom type hwPWTemplatePwIdleCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwPWTemplatePwIdleCode_Type.__name__ = "Unsigned32"
_HwPWTemplatePwIdleCode_Object = MibTableColumn
hwPWTemplatePwIdleCode = _HwPWTemplatePwIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 19),
    _HwPWTemplatePwIdleCode_Type()
)
hwPWTemplatePwIdleCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePwIdleCode.setStatus("current")
_HwPWTemplatePwRtpHeader_Type = Unsigned32
_HwPWTemplatePwRtpHeader_Object = MibTableColumn
hwPWTemplatePwRtpHeader = _HwPWTemplatePwRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 20),
    _HwPWTemplatePwRtpHeader_Type()
)
hwPWTemplatePwRtpHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePwRtpHeader.setStatus("current")
_HwPWTemplatePwCCSeqEnable_Type = HWEnableValue
_HwPWTemplatePwCCSeqEnable_Object = MibTableColumn
hwPWTemplatePwCCSeqEnable = _HwPWTemplatePwCCSeqEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 21),
    _HwPWTemplatePwCCSeqEnable_Type()
)
hwPWTemplatePwCCSeqEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePwCCSeqEnable.setStatus("current")
_HwPWTemplateCir_Type = Unsigned32
_HwPWTemplateCir_Object = MibTableColumn
hwPWTemplateCir = _HwPWTemplateCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 22),
    _HwPWTemplateCir_Type()
)
hwPWTemplateCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateCir.setStatus("current")
_HwPWTemplatePir_Type = Unsigned32
_HwPWTemplatePir_Object = MibTableColumn
hwPWTemplatePir = _HwPWTemplatePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 23),
    _HwPWTemplatePir_Type()
)
hwPWTemplatePir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplatePir.setStatus("current")


class _HwPWTemplateQosProfile_Type(DisplayString):
    """Custom type hwPWTemplateQosProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPWTemplateQosProfile_Type.__name__ = "DisplayString"
_HwPWTemplateQosProfile_Object = MibTableColumn
hwPWTemplateQosProfile = _HwPWTemplateQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 24),
    _HwPWTemplateQosProfile_Type()
)
hwPWTemplateQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateQosProfile.setStatus("current")
_HwPWTemplateFlowLabel_Type = EnabledStatus
_HwPWTemplateFlowLabel_Object = MibTableColumn
hwPWTemplateFlowLabel = _HwPWTemplateFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 25),
    _HwPWTemplateFlowLabel_Type()
)
hwPWTemplateFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateFlowLabel.setStatus("current")
_HwPWTemplateRowStatus_Type = RowStatus
_HwPWTemplateRowStatus_Object = MibTableColumn
hwPWTemplateRowStatus = _HwPWTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 5, 1, 51),
    _HwPWTemplateRowStatus_Type()
)
hwPWTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPWTemplateRowStatus.setStatus("current")
_HwPWTemplateMIBTraps_ObjectIdentity = ObjectIdentity
hwPWTemplateMIBTraps = _HwPWTemplateMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 6)
)
_HwPWTableObjects_ObjectIdentity = ObjectIdentity
hwPWTableObjects = _HwPWTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7)
)
_HwPWTable_Object = MibTable
hwPWTable = _HwPWTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwPWTable.setStatus("current")
_HwPWEntry_Object = MibTableRow
hwPWEntry = _HwPWEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1, 1)
)
hwPWEntry.setIndexNames(
    (0, "HUAWEI-PWE3-MIB", "hwPWId"),
    (0, "HUAWEI-PWE3-MIB", "hwPWType"),
    (0, "HUAWEI-PWE3-MIB", "hwPWPeerIp"),
)
if mibBuilder.loadTexts:
    hwPWEntry.setStatus("current")
_HwPWId_Type = Unsigned32
_HwPWId_Object = MibTableColumn
hwPWId = _HwPWId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1, 1, 1),
    _HwPWId_Type()
)
hwPWId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWId.setStatus("current")
_HwPWType_Type = HWL2VpnVcEncapsType
_HwPWType_Object = MibTableColumn
hwPWType = _HwPWType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1, 1, 2),
    _HwPWType_Type()
)
hwPWType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWType.setStatus("current")
_HwPWPeerIp_Type = IpAddress
_HwPWPeerIp_Object = MibTableColumn
hwPWPeerIp = _HwPWPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1, 1, 3),
    _HwPWPeerIp_Type()
)
hwPWPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPWPeerIp.setStatus("current")
_HwPWInterfaceIndex_Type = InterfaceIndexOrZero
_HwPWInterfaceIndex_Object = MibTableColumn
hwPWInterfaceIndex = _HwPWInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 7, 1, 1, 4),
    _HwPWInterfaceIndex_Type()
)
hwPWInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPWInterfaceIndex.setStatus("current")
_HwPwe3MIBConformance_ObjectIdentity = ObjectIdentity
hwPwe3MIBConformance = _HwPwe3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3)
)
_HwPwe3MIBCompliances_ObjectIdentity = ObjectIdentity
hwPwe3MIBCompliances = _HwPwe3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 1)
)
_HwPwe3MIBGroups_ObjectIdentity = ObjectIdentity
hwPwe3MIBGroups = _HwPwe3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2)
)
_HwL2vpnSvcMIBGroups_ObjectIdentity = ObjectIdentity
hwL2vpnSvcMIBGroups = _HwL2vpnSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3)
)
_HwL2vpnPWTableMIBGroups_ObjectIdentity = ObjectIdentity
hwL2vpnPWTableMIBGroups = _HwL2vpnPWTableMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 4)
)

# Managed Objects groups

hwPWVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 1)
)
hwPWVcGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddrType"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStatus"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchSign"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchPeerAddrType"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcGroupID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcAcStatus"),
        ("HUAWEI-PWE3-MIB", "hwPWVcACOAMStatus"),
        ("HUAWEI-PWE3-MIB", "hwPWVcMtu"),
        ("HUAWEI-PWE3-MIB", "hwPWVcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwPWVcVCCV"),
        ("HUAWEI-PWE3-MIB", "hwPWVcBandWidth"),
        ("HUAWEI-PWE3-MIB", "hwPWVcMaxAtmCells"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTnlPolicyName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcQoSBehaviorIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcExplicitPathName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTemplateName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwPWVcUpTime"),
        ("HUAWEI-PWE3-MIB", "hwPWOAMSync"),
        ("HUAWEI-PWE3-MIB", "hwPWVCForBfdIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcDelayTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcReroutePolicy"),
        ("HUAWEI-PWE3-MIB", "hwPWVcResumeTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcRerouteReason"),
        ("HUAWEI-PWE3-MIB", "hwPWVcLastRerouteTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcManualSetFault"),
        ("HUAWEI-PWE3-MIB", "hwPWVcActive"),
        ("HUAWEI-PWE3-MIB", "hwPWVcVrIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcVrID"),
        ("HUAWEI-PWE3-MIB", "hwPWBFDDetectMultiplier"),
        ("HUAWEI-PWE3-MIB", "hwPWBFDMinReceiveInterval"),
        ("HUAWEI-PWE3-MIB", "hwPWBFDMinTransmitInterval"),
        ("HUAWEI-PWE3-MIB", "hwPWDynamicBFDDetect"),
        ("HUAWEI-PWE3-MIB", "hwPWBFDRemoteVcID"),
        ("HUAWEI-PWE3-MIB", "hwPWEthOamType"),
        ("HUAWEI-PWE3-MIB", "hwPWCfmMaIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcUpStartTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcUpSumTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcRowStatus"),
        ("HUAWEI-PWE3-MIB", "hwPWVcAtmPackOvertime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPwJitterBufferDepth"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPwTdmEncapsulationNum"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPwIdleCode"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPwRtpHeader"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchTnlPolicyName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcCfmMdIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcCfmMaName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcCfmMdName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcRawOrTagged"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInterworkingType"),
        ("HUAWEI-PWE3-MIB", "hwPWVcCir"),
        ("HUAWEI-PWE3-MIB", "hwPWVcPir"),
        ("HUAWEI-PWE3-MIB", "hwPWVcQosProfile"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchCir"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchPir"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchQosProfile"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTrigger"),
        ("HUAWEI-PWE3-MIB", "hwPWVcEnableACOAM"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchVrIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchVrID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcQosParaFromPWT"),
        ("HUAWEI-PWE3-MIB", "hwPWVcBfdParaFromPWT"),
        ("HUAWEI-PWE3-MIB", "hwPwVcNegotiateMode"),
        ("HUAWEI-PWE3-MIB", "hwPwVcIsBypass"),
        ("HUAWEI-PWE3-MIB", "hwPwVcIsAdmin"),
        ("HUAWEI-PWE3-MIB", "hwPwVcAdminPwIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPwVcAdminPwLinkStatus"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchAdminPwIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchAdminPwLinkStatus"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupAdminPwIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupAdminPwLinkStatus"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcId"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcPeerAddrType"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcReceiveLabel"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcSendLabel"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcTnlPolicyName"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcCir"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcPir"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcQosProfile"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSlaveMasterMode"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchVcSlaveMasterMode"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcSlaveMasterMode"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchVcActive"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcActive"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchCwTrans"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchVcServiceName"),
        ("HUAWEI-PWE3-MIB", "hwPwVcSwitchBackupVcServiceName"))
)
if mibBuilder.loadTexts:
    hwPWVcGroup.setStatus("current")

hwPWVcTnlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 2)
)
hwPWVcTnlGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcTnlType"),
        ("HUAWEI-PWE3-MIB", "hwPWTnlForBfdIndex"))
)
if mibBuilder.loadTexts:
    hwPWVcTnlGroup.setStatus("current")

hwPWVcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 3)
)
hwPWVcStatisticsGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcStatisticsRcvPkts"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStatisticsRcvBytes"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStatisticsSndPkts"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStatisticsSndBytes"))
)
if mibBuilder.loadTexts:
    hwPWVcStatisticsGroup.setStatus("current")

hwPWRemoteVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 4)
)
hwPWRemoteVcGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWRemoteVcID"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcType"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcStatus"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcGroupID"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcMtu"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcCtrlword"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcMaxAtmCells"),
        ("HUAWEI-PWE3-MIB", "hwPWRemoteVcNotif"))
)
if mibBuilder.loadTexts:
    hwPWRemoteVcGroup.setStatus("current")

hwPWTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 5)
)
hwPWTemplateGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWTemplatePeerAddrType"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateCtrlword"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateVCCV"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateFrag"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateBandwidth"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateTnlPolicyName"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateQoSBehaviorIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateExplicitPathName"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateBFDDetectMultiplier"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateBFDMinReceiveInterval"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateBFDMinTransmitInterval"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateDynamicBFDDetect"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateMaxAtmCells"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateAtmPackOvertime"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePwJitterBufferDepth"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePwTdmEncapsulationNum"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePwIdleCode"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePwRtpHeader"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePwCCSeqEnable"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateCir"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplatePir"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateQosProfile"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateFlowLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hwPWTemplateGroup.setStatus("current")

hwPWNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 6)
)
hwPWNotificationControlGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcSwitchNotifEnable"),
        ("HUAWEI-PWE3-MIB", "hwPWVcUpDownNotifEnable"),
        ("HUAWEI-PWE3-MIB", "hwPWVcDeletedNotifEnable"))
)
if mibBuilder.loadTexts:
    hwPWNotificationControlGroup.setStatus("current")

hwPWVcStateChangeReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 7)
)
hwPWVcStateChangeReasonGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchRmtID"))
)
if mibBuilder.loadTexts:
    hwPWVcStateChangeReasonGroup.setStatus("current")

hwLdpPWStateChangeReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 9)
)
hwLdpPWStateChangeReasonGroup.setObjects(
    ("HUAWEI-PWE3-MIB", "hwLdpPWStateChangeReason")
)
if mibBuilder.loadTexts:
    hwLdpPWStateChangeReasonGroup.setStatus("current")

hwPWVcTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 10)
)
hwPWVcTDMPerfCurrentGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentMissingPkts"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentJtrBfrOverruns"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentJtrBfrUnderruns"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentMisOrderDropped"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentMalformedPkt"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentESs"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentSESs"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTDMPerfCurrentUASs"))
)
if mibBuilder.loadTexts:
    hwPWVcTDMPerfCurrentGroup.setStatus("current")

hwSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 1)
)
hwSvcGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcPeerAddrType"),
        ("HUAWEI-PWE3-MIB", "hwSvcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwSvcStatus"),
        ("HUAWEI-PWE3-MIB", "hwSvcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcGroupID"),
        ("HUAWEI-PWE3-MIB", "hwSvcAcStatus"),
        ("HUAWEI-PWE3-MIB", "hwSvcACOAMStatus"),
        ("HUAWEI-PWE3-MIB", "hwSvcMtu"),
        ("HUAWEI-PWE3-MIB", "hwSvcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwSvcVCCV"),
        ("HUAWEI-PWE3-MIB", "hwSvcBandWidth"),
        ("HUAWEI-PWE3-MIB", "hwSvcMaxAtmCells"),
        ("HUAWEI-PWE3-MIB", "hwSvcTnlPolicyName"),
        ("HUAWEI-PWE3-MIB", "hwSvcQoSBehaviorIndex"),
        ("HUAWEI-PWE3-MIB", "hwSvcPWTemplateName"),
        ("HUAWEI-PWE3-MIB", "hwSvcUpTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcOAMSync"),
        ("HUAWEI-PWE3-MIB", "hwSvcForBfdIndex"),
        ("HUAWEI-PWE3-MIB", "hwSvcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwSvcDelayTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcReroutePolicy"),
        ("HUAWEI-PWE3-MIB", "hwSvcResumeTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcRerouteReason"),
        ("HUAWEI-PWE3-MIB", "hwSvcLastRerouteTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcManualSetFault"),
        ("HUAWEI-PWE3-MIB", "hwSvcActive"),
        ("HUAWEI-PWE3-MIB", "hwSvcUpStartTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcUpSumTime"),
        ("HUAWEI-PWE3-MIB", "hwSvcAtmPackOvertime"),
        ("HUAWEI-PWE3-MIB", "hwSvcPwJitterBufferDepth"),
        ("HUAWEI-PWE3-MIB", "hwSvcPwTdmEncapsulationNum"),
        ("HUAWEI-PWE3-MIB", "hwSvcPwIdleCode"),
        ("HUAWEI-PWE3-MIB", "hwSvcPwRtpHeader"),
        ("HUAWEI-PWE3-MIB", "hwSvcRawOrTagged"),
        ("HUAWEI-PWE3-MIB", "hwSvcInterworkingType"),
        ("HUAWEI-PWE3-MIB", "hwSvcCir"),
        ("HUAWEI-PWE3-MIB", "hwSvcPir"),
        ("HUAWEI-PWE3-MIB", "hwSvcQosProfile"),
        ("HUAWEI-PWE3-MIB", "hwSvcRowStatus"))
)
if mibBuilder.loadTexts:
    hwSvcGroup.setStatus("current")

hwSvcTnlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 2)
)
hwSvcTnlGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcTnlType"),
        ("HUAWEI-PWE3-MIB", "hwSvcTnlForBfdIndex"))
)
if mibBuilder.loadTexts:
    hwSvcTnlGroup.setStatus("current")

hwSvcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 3)
)
hwSvcStatisticsGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcStatisticsRcvPkts"),
        ("HUAWEI-PWE3-MIB", "hwSvcStatisticsRcvBytes"),
        ("HUAWEI-PWE3-MIB", "hwSvcStatisticsSndPkts"),
        ("HUAWEI-PWE3-MIB", "hwSvcStatisticsSndBytes"))
)
if mibBuilder.loadTexts:
    hwSvcStatisticsGroup.setStatus("current")

hwSvcNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 4)
)
hwSvcNotificationControlGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcSwitchNotifEnable"),
        ("HUAWEI-PWE3-MIB", "hwSvcUpDownNotifEnable"),
        ("HUAWEI-PWE3-MIB", "hwSvcDeletedNotifEnable"))
)
if mibBuilder.loadTexts:
    hwSvcNotificationControlGroup.setStatus("current")

hwSvcStateChangeReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 5)
)
hwSvcStateChangeReasonGroup.setObjects(
    ("HUAWEI-PWE3-MIB", "hwSvcStateChangeReason")
)
if mibBuilder.loadTexts:
    hwSvcStateChangeReasonGroup.setStatus("current")

hwPWTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 4, 1)
)
hwPWTableGroup.setObjects(
    ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex")
)
if mibBuilder.loadTexts:
    hwPWTableGroup.setStatus("current")


# Notification objects

hwPWVcSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 1)
)
hwPWVcSwitchWtoP.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchRmtID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"))
)
if mibBuilder.loadTexts:
    hwPWVcSwitchWtoP.setStatus(
        "current"
    )

hwPWVcSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 2)
)
hwPWVcSwitchPtoW.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchRmtID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"))
)
if mibBuilder.loadTexts:
    hwPWVcSwitchPtoW.setStatus(
        "current"
    )

hwPWVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 3)
)
hwPWVcDown.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwPWVcDown.setStatus(
        "current"
    )

hwPWVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 4)
)
hwPWVcUp.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchID"),
        ("HUAWEI-PWE3-MIB", "hwPWVcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwPWVcUp.setStatus(
        "current"
    )

hwPWVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 5)
)
hwPWVcDeleted.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchID"))
)
if mibBuilder.loadTexts:
    hwPWVcDeleted.setStatus(
        "current"
    )

hwPWVcBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 6)
)
hwPWVcBackup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfIndex"),
        ("HUAWEI-PWE3-MIB", "hwPWVcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSecondary"),
        ("HUAWEI-PWE3-MIB", "hwPWVcStateChangeReason"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("HUAWEI-PWE3-MIB", "hwPWVcIfName"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchID"))
)
if mibBuilder.loadTexts:
    hwPWVcBackup.setStatus(
        "current"
    )

hwLdpPWVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 7)
)
hwLdpPWVcDown.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwLdpPWStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwLdpPWVcDown.setStatus(
        "current"
    )

hwLdpPWVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 2, 8)
)
hwLdpPWVcUp.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwLdpPWStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwLdpPWVcUp.setStatus(
        "current"
    )

hwSvcSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4, 1)
)
hwSvcSwitchWtoP.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwSvcStateChangeReason"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwSvcSwitchWtoP.setStatus(
        "current"
    )

hwSvcSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4, 2)
)
hwSvcSwitchPtoW.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcCtrlWord"),
        ("HUAWEI-PWE3-MIB", "hwSvcStateChangeReason"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwSvcSwitchPtoW.setStatus(
        "current"
    )

hwSvcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4, 3)
)
hwSvcDown.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwSvcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcStateChangeReason"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-PWE3-MIB", "hwSvcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwSvcDown.setStatus(
        "current"
    )

hwSvcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4, 4)
)
hwSvcUp.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwSvcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcOutboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcStateChangeReason"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-PWE3-MIB", "hwSvcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwSvcUp.setStatus(
        "current"
    )

hwSvcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 4, 5)
)
hwSvcDeleted.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcID"),
        ("HUAWEI-PWE3-MIB", "hwSvcType"),
        ("HUAWEI-PWE3-MIB", "hwSvcPeerAddr"),
        ("HUAWEI-PWE3-MIB", "hwSvcInboundLabel"),
        ("HUAWEI-PWE3-MIB", "hwSvcOutboundLabel"))
)
if mibBuilder.loadTexts:
    hwSvcDeleted.setStatus(
        "current"
    )

hwPWTemplateCannotDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 1, 6, 1)
)
hwPWTemplateCannotDeleted.setObjects(
    ("HUAWEI-PWE3-MIB", "hwPWTemplateName")
)
if mibBuilder.loadTexts:
    hwPWTemplateCannotDeleted.setStatus(
        "current"
    )


# Notifications groups

hwPWVcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 2, 8)
)
hwPWVcNotificationGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwPWVcSwitchWtoP"),
        ("HUAWEI-PWE3-MIB", "hwPWVcSwitchPtoW"),
        ("HUAWEI-PWE3-MIB", "hwPWVcDown"),
        ("HUAWEI-PWE3-MIB", "hwPWVcUp"),
        ("HUAWEI-PWE3-MIB", "hwPWVcDeleted"),
        ("HUAWEI-PWE3-MIB", "hwPWVcBackup"),
        ("HUAWEI-PWE3-MIB", "hwLdpPWVcDown"),
        ("HUAWEI-PWE3-MIB", "hwLdpPWVcUp"))
)
if mibBuilder.loadTexts:
    hwPWVcNotificationGroup.setStatus(
        "current"
    )

hwSvcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 3, 6)
)
hwSvcNotificationGroup.setObjects(
      *(("HUAWEI-PWE3-MIB", "hwSvcSwitchWtoP"),
        ("HUAWEI-PWE3-MIB", "hwSvcSwitchPtoW"),
        ("HUAWEI-PWE3-MIB", "hwSvcDown"),
        ("HUAWEI-PWE3-MIB", "hwSvcUp"),
        ("HUAWEI-PWE3-MIB", "hwSvcDeleted"))
)
if mibBuilder.loadTexts:
    hwSvcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwPwe3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwPwe3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PWE3-MIB",
    **{"HWLdpPwStateChangeReason": HWLdpPwStateChangeReason,
       "hwL2Vpn": hwL2Vpn,
       "hwL2VpnPwe3": hwL2VpnPwe3,
       "hwPwe3MIBObjects": hwPwe3MIBObjects,
       "hwPwe3Objects": hwPwe3Objects,
       "hwPWVcTable": hwPWVcTable,
       "hwPWVcEntry": hwPWVcEntry,
       "hwPWVcID": hwPWVcID,
       "hwPWVcType": hwPWVcType,
       "hwPWVcPeerAddrType": hwPWVcPeerAddrType,
       "hwPWVcPeerAddr": hwPWVcPeerAddr,
       "hwPWVcStatus": hwPWVcStatus,
       "hwPWVcInboundLabel": hwPWVcInboundLabel,
       "hwPWVcOutboundLabel": hwPWVcOutboundLabel,
       "hwPWVcSwitchSign": hwPWVcSwitchSign,
       "hwPWVcSwitchID": hwPWVcSwitchID,
       "hwPWVcSwitchPeerAddrType": hwPWVcSwitchPeerAddrType,
       "hwPWVcSwitchPeerAddr": hwPWVcSwitchPeerAddr,
       "hwPWVcSwitchInboundLabel": hwPWVcSwitchInboundLabel,
       "hwPWVcSwitchOutboundLabel": hwPWVcSwitchOutboundLabel,
       "hwPWVcGroupID": hwPWVcGroupID,
       "hwPWVcIfIndex": hwPWVcIfIndex,
       "hwPWVcAcStatus": hwPWVcAcStatus,
       "hwPWVcACOAMStatus": hwPWVcACOAMStatus,
       "hwPWVcMtu": hwPWVcMtu,
       "hwPWVcCtrlWord": hwPWVcCtrlWord,
       "hwPWVcVCCV": hwPWVcVCCV,
       "hwPWVcBandWidth": hwPWVcBandWidth,
       "hwPWVcMaxAtmCells": hwPWVcMaxAtmCells,
       "hwPWVcTnlPolicyName": hwPWVcTnlPolicyName,
       "hwPWVcQoSBehaviorIndex": hwPWVcQoSBehaviorIndex,
       "hwPWVcExplicitPathName": hwPWVcExplicitPathName,
       "hwPWVcTemplateName": hwPWVcTemplateName,
       "hwPWVcSecondary": hwPWVcSecondary,
       "hwPWVcUpTime": hwPWVcUpTime,
       "hwPWOAMSync": hwPWOAMSync,
       "hwPWVCForBfdIndex": hwPWVCForBfdIndex,
       "hwPWVcDelayTime": hwPWVcDelayTime,
       "hwPWVcReroutePolicy": hwPWVcReroutePolicy,
       "hwPWVcResumeTime": hwPWVcResumeTime,
       "hwPWVcRerouteReason": hwPWVcRerouteReason,
       "hwPWVcLastRerouteTime": hwPWVcLastRerouteTime,
       "hwPWVcManualSetFault": hwPWVcManualSetFault,
       "hwPWVcActive": hwPWVcActive,
       "hwPWVcVrIfIndex": hwPWVcVrIfIndex,
       "hwPWVcVrID": hwPWVcVrID,
       "hwPWBFDDetectMultiplier": hwPWBFDDetectMultiplier,
       "hwPWBFDMinReceiveInterval": hwPWBFDMinReceiveInterval,
       "hwPWBFDMinTransmitInterval": hwPWBFDMinTransmitInterval,
       "hwPWDynamicBFDDetect": hwPWDynamicBFDDetect,
       "hwPWBFDRemoteVcID": hwPWBFDRemoteVcID,
       "hwPWEthOamType": hwPWEthOamType,
       "hwPWCfmMaIndex": hwPWCfmMaIndex,
       "hwPWVcUpStartTime": hwPWVcUpStartTime,
       "hwPWVcUpSumTime": hwPWVcUpSumTime,
       "hwPWVcIfName": hwPWVcIfName,
       "hwPWVcRowStatus": hwPWVcRowStatus,
       "hwPWVcAtmPackOvertime": hwPWVcAtmPackOvertime,
       "hwPWVcPwJitterBufferDepth": hwPWVcPwJitterBufferDepth,
       "hwPWVcPwTdmEncapsulationNum": hwPWVcPwTdmEncapsulationNum,
       "hwPWVcPwIdleCode": hwPWVcPwIdleCode,
       "hwPWVcPwRtpHeader": hwPWVcPwRtpHeader,
       "hwPWVcSwitchTnlPolicyName": hwPWVcSwitchTnlPolicyName,
       "hwPWVcCfmMdIndex": hwPWVcCfmMdIndex,
       "hwPWVcCfmMaName": hwPWVcCfmMaName,
       "hwPWVcCfmMdName": hwPWVcCfmMdName,
       "hwPWVcRawOrTagged": hwPWVcRawOrTagged,
       "hwPWVcInterworkingType": hwPWVcInterworkingType,
       "hwPWVcCir": hwPWVcCir,
       "hwPWVcPir": hwPWVcPir,
       "hwPWVcQosProfile": hwPWVcQosProfile,
       "hwPWVcSwitchCir": hwPWVcSwitchCir,
       "hwPWVcSwitchPir": hwPWVcSwitchPir,
       "hwPWVcSwitchQosProfile": hwPWVcSwitchQosProfile,
       "hwPWVcTrigger": hwPWVcTrigger,
       "hwPWVcEnableACOAM": hwPWVcEnableACOAM,
       "hwPWVcSwitchVrIfIndex": hwPWVcSwitchVrIfIndex,
       "hwPWVcSwitchVrID": hwPWVcSwitchVrID,
       "hwPWVcQosParaFromPWT": hwPWVcQosParaFromPWT,
       "hwPWVcBfdParaFromPWT": hwPWVcBfdParaFromPWT,
       "hwPwVcNegotiateMode": hwPwVcNegotiateMode,
       "hwPwVcIsBypass": hwPwVcIsBypass,
       "hwPwVcIsAdmin": hwPwVcIsAdmin,
       "hwPwVcAdminPwIfIndex": hwPwVcAdminPwIfIndex,
       "hwPwVcAdminPwLinkStatus": hwPwVcAdminPwLinkStatus,
       "hwPwVcSwitchAdminPwIfIndex": hwPwVcSwitchAdminPwIfIndex,
       "hwPwVcSwitchAdminPwLinkStatus": hwPwVcSwitchAdminPwLinkStatus,
       "hwPwVcSwitchBackupAdminPwIfIndex": hwPwVcSwitchBackupAdminPwIfIndex,
       "hwPwVcSwitchBackupAdminPwLinkStatus": hwPwVcSwitchBackupAdminPwLinkStatus,
       "hwPwVcSwitchBackupVcId": hwPwVcSwitchBackupVcId,
       "hwPwVcSwitchBackupVcPeerAddrType": hwPwVcSwitchBackupVcPeerAddrType,
       "hwPwVcSwitchBackupVcPeerAddr": hwPwVcSwitchBackupVcPeerAddr,
       "hwPwVcSwitchBackupVcReceiveLabel": hwPwVcSwitchBackupVcReceiveLabel,
       "hwPwVcSwitchBackupVcSendLabel": hwPwVcSwitchBackupVcSendLabel,
       "hwPwVcSwitchBackupVcTnlPolicyName": hwPwVcSwitchBackupVcTnlPolicyName,
       "hwPwVcSwitchBackupVcCir": hwPwVcSwitchBackupVcCir,
       "hwPwVcSwitchBackupVcPir": hwPwVcSwitchBackupVcPir,
       "hwPwVcSwitchBackupVcQosProfile": hwPwVcSwitchBackupVcQosProfile,
       "hwPwVcSlaveMasterMode": hwPwVcSlaveMasterMode,
       "hwPwVcSwitchVcSlaveMasterMode": hwPwVcSwitchVcSlaveMasterMode,
       "hwPwVcSwitchBackupVcSlaveMasterMode": hwPwVcSwitchBackupVcSlaveMasterMode,
       "hwPwVcSwitchVcActive": hwPwVcSwitchVcActive,
       "hwPwVcSwitchBackupVcActive": hwPwVcSwitchBackupVcActive,
       "hwPwVcSwitchCwTrans": hwPwVcSwitchCwTrans,
       "hwPwVcSwitchVcServiceName": hwPwVcSwitchVcServiceName,
       "hwPwVcSwitchBackupVcServiceName": hwPwVcSwitchBackupVcServiceName,
       "hwPWVcTnlTable": hwPWVcTnlTable,
       "hwPWVcTnlEntry": hwPWVcTnlEntry,
       "hwPWVcTnlIndex": hwPWVcTnlIndex,
       "hwPWVcTnlType": hwPWVcTnlType,
       "hwPWTnlForBfdIndex": hwPWTnlForBfdIndex,
       "hwPWVcStatisticsTable": hwPWVcStatisticsTable,
       "hwPWVcStatisticsEntry": hwPWVcStatisticsEntry,
       "hwPWVcStatisticsRcvPkts": hwPWVcStatisticsRcvPkts,
       "hwPWVcStatisticsRcvBytes": hwPWVcStatisticsRcvBytes,
       "hwPWVcStatisticsSndPkts": hwPWVcStatisticsSndPkts,
       "hwPWVcStatisticsSndBytes": hwPWVcStatisticsSndBytes,
       "hwPWRemoteVcTable": hwPWRemoteVcTable,
       "hwPWRemoteVcEntry": hwPWRemoteVcEntry,
       "hwPWRemoteVcID": hwPWRemoteVcID,
       "hwPWRemoteVcType": hwPWRemoteVcType,
       "hwPWRemoteVcStatus": hwPWRemoteVcStatus,
       "hwPWRemoteVcGroupID": hwPWRemoteVcGroupID,
       "hwPWRemoteVcMtu": hwPWRemoteVcMtu,
       "hwPWRemoteVcCtrlword": hwPWRemoteVcCtrlword,
       "hwPWRemoteVcMaxAtmCells": hwPWRemoteVcMaxAtmCells,
       "hwPWRemoteVcNotif": hwPWRemoteVcNotif,
       "hwPWVcSwitchNotifEnable": hwPWVcSwitchNotifEnable,
       "hwPWVcUpDownNotifEnable": hwPWVcUpDownNotifEnable,
       "hwPWVcDeletedNotifEnable": hwPWVcDeletedNotifEnable,
       "hwPWVcStateChangeReason": hwPWVcStateChangeReason,
       "hwPWVcSwitchRmtID": hwPWVcSwitchRmtID,
       "hwLdpPWStateChangeReason": hwLdpPWStateChangeReason,
       "hwPWVcTDMPerfCurrentTable": hwPWVcTDMPerfCurrentTable,
       "hwPWVcTDMPerfCurrentEntry": hwPWVcTDMPerfCurrentEntry,
       "hwPWVcTDMPerfCurrentMissingPkts": hwPWVcTDMPerfCurrentMissingPkts,
       "hwPWVcTDMPerfCurrentJtrBfrOverruns": hwPWVcTDMPerfCurrentJtrBfrOverruns,
       "hwPWVcTDMPerfCurrentJtrBfrUnderruns": hwPWVcTDMPerfCurrentJtrBfrUnderruns,
       "hwPWVcTDMPerfCurrentMisOrderDropped": hwPWVcTDMPerfCurrentMisOrderDropped,
       "hwPWVcTDMPerfCurrentMalformedPkt": hwPWVcTDMPerfCurrentMalformedPkt,
       "hwPWVcTDMPerfCurrentESs": hwPWVcTDMPerfCurrentESs,
       "hwPWVcTDMPerfCurrentSESs": hwPWVcTDMPerfCurrentSESs,
       "hwPWVcTDMPerfCurrentUASs": hwPWVcTDMPerfCurrentUASs,
       "hwPwe3MIBTraps": hwPwe3MIBTraps,
       "hwPWVcSwitchWtoP": hwPWVcSwitchWtoP,
       "hwPWVcSwitchPtoW": hwPWVcSwitchPtoW,
       "hwPWVcDown": hwPWVcDown,
       "hwPWVcUp": hwPWVcUp,
       "hwPWVcDeleted": hwPWVcDeleted,
       "hwPWVcBackup": hwPWVcBackup,
       "hwLdpPWVcDown": hwLdpPWVcDown,
       "hwLdpPWVcUp": hwLdpPWVcUp,
       "hwSvcObjects": hwSvcObjects,
       "hwSvcTable": hwSvcTable,
       "hwSvcEntry": hwSvcEntry,
       "hwSvcIfIndex": hwSvcIfIndex,
       "hwSvcID": hwSvcID,
       "hwSvcType": hwSvcType,
       "hwSvcPeerAddrType": hwSvcPeerAddrType,
       "hwSvcPeerAddr": hwSvcPeerAddr,
       "hwSvcStatus": hwSvcStatus,
       "hwSvcInboundLabel": hwSvcInboundLabel,
       "hwSvcOutboundLabel": hwSvcOutboundLabel,
       "hwSvcGroupID": hwSvcGroupID,
       "hwSvcAcStatus": hwSvcAcStatus,
       "hwSvcACOAMStatus": hwSvcACOAMStatus,
       "hwSvcMtu": hwSvcMtu,
       "hwSvcCtrlWord": hwSvcCtrlWord,
       "hwSvcVCCV": hwSvcVCCV,
       "hwSvcBandWidth": hwSvcBandWidth,
       "hwSvcMaxAtmCells": hwSvcMaxAtmCells,
       "hwSvcTnlPolicyName": hwSvcTnlPolicyName,
       "hwSvcQoSBehaviorIndex": hwSvcQoSBehaviorIndex,
       "hwSvcPWTemplateName": hwSvcPWTemplateName,
       "hwSvcUpTime": hwSvcUpTime,
       "hwSvcOAMSync": hwSvcOAMSync,
       "hwSvcForBfdIndex": hwSvcForBfdIndex,
       "hwSvcSecondary": hwSvcSecondary,
       "hwSvcDelayTime": hwSvcDelayTime,
       "hwSvcReroutePolicy": hwSvcReroutePolicy,
       "hwSvcResumeTime": hwSvcResumeTime,
       "hwSvcRerouteReason": hwSvcRerouteReason,
       "hwSvcLastRerouteTime": hwSvcLastRerouteTime,
       "hwSvcManualSetFault": hwSvcManualSetFault,
       "hwSvcActive": hwSvcActive,
       "hwSvcUpStartTime": hwSvcUpStartTime,
       "hwSvcUpSumTime": hwSvcUpSumTime,
       "hwSvcAtmPackOvertime": hwSvcAtmPackOvertime,
       "hwSvcPwJitterBufferDepth": hwSvcPwJitterBufferDepth,
       "hwSvcPwTdmEncapsulationNum": hwSvcPwTdmEncapsulationNum,
       "hwSvcPwIdleCode": hwSvcPwIdleCode,
       "hwSvcPwRtpHeader": hwSvcPwRtpHeader,
       "hwSvcRawOrTagged": hwSvcRawOrTagged,
       "hwSvcInterworkingType": hwSvcInterworkingType,
       "hwSvcCir": hwSvcCir,
       "hwSvcPir": hwSvcPir,
       "hwSvcQosProfile": hwSvcQosProfile,
       "hwSvcRowStatus": hwSvcRowStatus,
       "hwSvcTnlTable": hwSvcTnlTable,
       "hwSvcTnlEntry": hwSvcTnlEntry,
       "hwSvcTnlIndex": hwSvcTnlIndex,
       "hwSvcTnlType": hwSvcTnlType,
       "hwSvcTnlForBfdIndex": hwSvcTnlForBfdIndex,
       "hwSvcStatisticsTable": hwSvcStatisticsTable,
       "hwSvcStatisticsEntry": hwSvcStatisticsEntry,
       "hwSvcStatisticsRcvPkts": hwSvcStatisticsRcvPkts,
       "hwSvcStatisticsRcvBytes": hwSvcStatisticsRcvBytes,
       "hwSvcStatisticsSndPkts": hwSvcStatisticsSndPkts,
       "hwSvcStatisticsSndBytes": hwSvcStatisticsSndBytes,
       "hwSvcSwitchNotifEnable": hwSvcSwitchNotifEnable,
       "hwSvcUpDownNotifEnable": hwSvcUpDownNotifEnable,
       "hwSvcDeletedNotifEnable": hwSvcDeletedNotifEnable,
       "hwSvcStateChangeReason": hwSvcStateChangeReason,
       "hwL2vpnSvcMIBTraps": hwL2vpnSvcMIBTraps,
       "hwSvcSwitchWtoP": hwSvcSwitchWtoP,
       "hwSvcSwitchPtoW": hwSvcSwitchPtoW,
       "hwSvcDown": hwSvcDown,
       "hwSvcUp": hwSvcUp,
       "hwSvcDeleted": hwSvcDeleted,
       "hwPWTemplateTable": hwPWTemplateTable,
       "hwPWTemplateEntry": hwPWTemplateEntry,
       "hwPWTemplateName": hwPWTemplateName,
       "hwPWTemplatePeerAddrType": hwPWTemplatePeerAddrType,
       "hwPWTemplatePeerAddr": hwPWTemplatePeerAddr,
       "hwPWTemplateCtrlword": hwPWTemplateCtrlword,
       "hwPWTemplateVCCV": hwPWTemplateVCCV,
       "hwPWTemplateFrag": hwPWTemplateFrag,
       "hwPWTemplateBandwidth": hwPWTemplateBandwidth,
       "hwPWTemplateTnlPolicyName": hwPWTemplateTnlPolicyName,
       "hwPWTemplateQoSBehaviorIndex": hwPWTemplateQoSBehaviorIndex,
       "hwPWTemplateExplicitPathName": hwPWTemplateExplicitPathName,
       "hwPWTemplateBFDDetectMultiplier": hwPWTemplateBFDDetectMultiplier,
       "hwPWTemplateBFDMinReceiveInterval": hwPWTemplateBFDMinReceiveInterval,
       "hwPWTemplateBFDMinTransmitInterval": hwPWTemplateBFDMinTransmitInterval,
       "hwPWTemplateDynamicBFDDetect": hwPWTemplateDynamicBFDDetect,
       "hwPWTemplateMaxAtmCells": hwPWTemplateMaxAtmCells,
       "hwPWTemplateAtmPackOvertime": hwPWTemplateAtmPackOvertime,
       "hwPWTemplatePwJitterBufferDepth": hwPWTemplatePwJitterBufferDepth,
       "hwPWTemplatePwTdmEncapsulationNum": hwPWTemplatePwTdmEncapsulationNum,
       "hwPWTemplatePwIdleCode": hwPWTemplatePwIdleCode,
       "hwPWTemplatePwRtpHeader": hwPWTemplatePwRtpHeader,
       "hwPWTemplatePwCCSeqEnable": hwPWTemplatePwCCSeqEnable,
       "hwPWTemplateCir": hwPWTemplateCir,
       "hwPWTemplatePir": hwPWTemplatePir,
       "hwPWTemplateQosProfile": hwPWTemplateQosProfile,
       "hwPWTemplateFlowLabel": hwPWTemplateFlowLabel,
       "hwPWTemplateRowStatus": hwPWTemplateRowStatus,
       "hwPWTemplateMIBTraps": hwPWTemplateMIBTraps,
       "hwPWTemplateCannotDeleted": hwPWTemplateCannotDeleted,
       "hwPWTableObjects": hwPWTableObjects,
       "hwPWTable": hwPWTable,
       "hwPWEntry": hwPWEntry,
       "hwPWId": hwPWId,
       "hwPWType": hwPWType,
       "hwPWPeerIp": hwPWPeerIp,
       "hwPWInterfaceIndex": hwPWInterfaceIndex,
       "hwPwe3MIBConformance": hwPwe3MIBConformance,
       "hwPwe3MIBCompliances": hwPwe3MIBCompliances,
       "hwPwe3MIBCompliance": hwPwe3MIBCompliance,
       "hwPwe3MIBGroups": hwPwe3MIBGroups,
       "hwPWVcGroup": hwPWVcGroup,
       "hwPWVcTnlGroup": hwPWVcTnlGroup,
       "hwPWVcStatisticsGroup": hwPWVcStatisticsGroup,
       "hwPWRemoteVcGroup": hwPWRemoteVcGroup,
       "hwPWTemplateGroup": hwPWTemplateGroup,
       "hwPWNotificationControlGroup": hwPWNotificationControlGroup,
       "hwPWVcStateChangeReasonGroup": hwPWVcStateChangeReasonGroup,
       "hwPWVcNotificationGroup": hwPWVcNotificationGroup,
       "hwLdpPWStateChangeReasonGroup": hwLdpPWStateChangeReasonGroup,
       "hwPWVcTDMPerfCurrentGroup": hwPWVcTDMPerfCurrentGroup,
       "hwL2vpnSvcMIBGroups": hwL2vpnSvcMIBGroups,
       "hwSvcGroup": hwSvcGroup,
       "hwSvcTnlGroup": hwSvcTnlGroup,
       "hwSvcStatisticsGroup": hwSvcStatisticsGroup,
       "hwSvcNotificationControlGroup": hwSvcNotificationControlGroup,
       "hwSvcStateChangeReasonGroup": hwSvcStateChangeReasonGroup,
       "hwSvcNotificationGroup": hwSvcNotificationGroup,
       "hwL2vpnPWTableMIBGroups": hwL2vpnPWTableMIBGroups,
       "hwPWTableGroup": hwPWTableGroup}
)
