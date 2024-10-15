# SNMP MIB module (ZXR10-MPLS-L2VPN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MPLS-L2VPN
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zxr10L2vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L2vpn")


# MODULE-IDENTITY

zxr10MplsL2vpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1)
)
zxr10MplsL2vpnMIB.setRevisions(
        ("2005-07-26 00:00",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsL2vpnType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2vpn-IPLS", 3),
          ("l2vpn-UNKNOWN", 0),
          ("l2vpn-VPLS", 2),
          ("l2vpn-VPWS", 1))
    )



class MplsL2vpnPWType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pw-HUB", 2),
          ("pw-SPOKE", 1),
          ("pw-UNKNOWN", 0))
    )



class MplsL2vpnPWEncapsulationType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("encap-ATM-AAL5", 2),
          ("encap-ATM-TRANSCELL", 3),
          ("encap-ATM-VCC", 9),
          ("encap-ATM-VPC", 10),
          ("encap-CEM", 8),
          ("encap-ETH", 5),
          ("encap-ETH-VLAN", 4),
          ("encap-FR-DLCI", 1),
          ("encap-HDLC", 6),
          ("encap-PPP", 7),
          ("encap-UNKNOWN", 0))
    )



class MplsL2vpnPWCbit(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cword-DISABLE", 0),
          ("cword-ENABLE", 1))
    )



class MplsL2vpnPWPsnType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpls-tunnel", 1),
          ("te-tunnel", 2),
          ("unknown-tunnel", 0))
    )



class MplsL2vpnPWStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("established", 1),
          ("not-established", 0))
    )



class MplsL2vpnTrapLevel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alerts", 2),
          ("critical", 3),
          ("debugging", 8),
          ("emergencies", 1),
          ("errors", 4),
          ("informational", 7),
          ("notifications", 6),
          ("warnings", 5))
    )



class MplsL2vpnTrapDetail(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("if-admini-down", 3),
          ("if-disappear", 4),
          ("if-encap-chg", 5),
          ("if-mtu-chg", 6),
          ("if-phy-down", 1),
          ("if-proto-down", 2),
          ("link-no-mpls-tunnel", 9),
          ("link-no-route", 7),
          ("link-no-te-tunnel", 10),
          ("link-te-tunnel-down", 8),
          ("proto-cbit-negotiate-fail", 17),
          ("proto-mtu-negotiate-fail", 16),
          ("proto-no-vfi", 18),
          ("proto-no-vpls-peer", 14),
          ("proto-no-vpws", 13),
          ("proto-sess-down", 12),
          ("proto-vc-withdraw", 11),
          ("proto-vctype-negotiate-fail", 15))
    )



# MIB Managed Objects in the order of their OIDs

_Zxr10MplsL2vpnObjects_ObjectIdentity = ObjectIdentity
zxr10MplsL2vpnObjects = _Zxr10MplsL2vpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0)
)
_Zxr10MplsL2vpnInstanceTable_Object = MibTable
zxr10MplsL2vpnInstanceTable = _Zxr10MplsL2vpnInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1)
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnInstanceTable.setStatus("current")
_Zxr10MplsL2vpnInstanceEntry_Object = MibTableRow
zxr10MplsL2vpnInstanceEntry = _Zxr10MplsL2vpnInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1)
)
zxr10MplsL2vpnInstanceEntry.setIndexNames(
    (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnInstanceVCId"),
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnInstanceEntry.setStatus("current")
_Zxr10MplsL2vpnInstanceType_Type = MplsL2vpnType
_Zxr10MplsL2vpnInstanceType_Object = MibTableColumn
zxr10MplsL2vpnInstanceType = _Zxr10MplsL2vpnInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 1),
    _Zxr10MplsL2vpnInstanceType_Type()
)
zxr10MplsL2vpnInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnInstanceType.setStatus("current")


class _Zxr10MplsL2vpnInstanceVCId_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnInstanceVCId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Zxr10MplsL2vpnInstanceVCId_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnInstanceVCId_Object = MibTableColumn
zxr10MplsL2vpnInstanceVCId = _Zxr10MplsL2vpnInstanceVCId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 2),
    _Zxr10MplsL2vpnInstanceVCId_Type()
)
zxr10MplsL2vpnInstanceVCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnInstanceVCId.setStatus("current")


class _Zxr10MplsL2vpnInstanceVpnName_Type(DisplayString):
    """Custom type zxr10MplsL2vpnInstanceVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Zxr10MplsL2vpnInstanceVpnName_Type.__name__ = "DisplayString"
_Zxr10MplsL2vpnInstanceVpnName_Object = MibTableColumn
zxr10MplsL2vpnInstanceVpnName = _Zxr10MplsL2vpnInstanceVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 3),
    _Zxr10MplsL2vpnInstanceVpnName_Type()
)
zxr10MplsL2vpnInstanceVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnInstanceVpnName.setStatus("current")


class _Zxr10MplsL2vpnPwCounts_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPwCounts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Zxr10MplsL2vpnPwCounts_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPwCounts_Object = MibTableColumn
zxr10MplsL2vpnPwCounts = _Zxr10MplsL2vpnPwCounts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 4),
    _Zxr10MplsL2vpnPwCounts_Type()
)
zxr10MplsL2vpnPwCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPwCounts.setStatus("current")
_Zxr10MplsL2vpnPWObjects_ObjectIdentity = ObjectIdentity
zxr10MplsL2vpnPWObjects = _Zxr10MplsL2vpnPWObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1)
)
_Zxr10MplsL2vpnPWTable_Object = MibTable
zxr10MplsL2vpnPWTable = _Zxr10MplsL2vpnPWTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWTable.setStatus("current")
_Zxr10MplsL2vpnPWEntry_Object = MibTableRow
zxr10MplsL2vpnPWEntry = _Zxr10MplsL2vpnPWEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1)
)
zxr10MplsL2vpnPWEntry.setIndexNames(
    (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnPWVcId"),
    (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnPWRemoteRouterId"),
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWEntry.setStatus("current")


class _Zxr10MplsL2vpnPWVcId_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPWVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Zxr10MplsL2vpnPWVcId_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPWVcId_Object = MibTableColumn
zxr10MplsL2vpnPWVcId = _Zxr10MplsL2vpnPWVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 1),
    _Zxr10MplsL2vpnPWVcId_Type()
)
zxr10MplsL2vpnPWVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWVcId.setStatus("current")
_Zxr10MplsL2vpnPWType_Type = MplsL2vpnPWType
_Zxr10MplsL2vpnPWType_Object = MibTableColumn
zxr10MplsL2vpnPWType = _Zxr10MplsL2vpnPWType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 2),
    _Zxr10MplsL2vpnPWType_Type()
)
zxr10MplsL2vpnPWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWType.setStatus("current")
_Zxr10MplsL2vpnPWEncapsulationType_Type = MplsL2vpnPWEncapsulationType
_Zxr10MplsL2vpnPWEncapsulationType_Object = MibTableColumn
zxr10MplsL2vpnPWEncapsulationType = _Zxr10MplsL2vpnPWEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 3),
    _Zxr10MplsL2vpnPWEncapsulationType_Type()
)
zxr10MplsL2vpnPWEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWEncapsulationType.setStatus("current")
_Zxr10MplsL2vpnPWVlanid_Type = Integer32
_Zxr10MplsL2vpnPWVlanid_Object = MibTableColumn
zxr10MplsL2vpnPWVlanid = _Zxr10MplsL2vpnPWVlanid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 4),
    _Zxr10MplsL2vpnPWVlanid_Type()
)
zxr10MplsL2vpnPWVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWVlanid.setStatus("current")
_Zxr10MplsL2vpnPWPsnType_Type = MplsL2vpnPWPsnType
_Zxr10MplsL2vpnPWPsnType_Object = MibTableColumn
zxr10MplsL2vpnPWPsnType = _Zxr10MplsL2vpnPWPsnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 5),
    _Zxr10MplsL2vpnPWPsnType_Type()
)
zxr10MplsL2vpnPWPsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWPsnType.setStatus("current")
_Zxr10MplsL2vpnPWTunnelid_Type = Unsigned32
_Zxr10MplsL2vpnPWTunnelid_Object = MibTableColumn
zxr10MplsL2vpnPWTunnelid = _Zxr10MplsL2vpnPWTunnelid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 6),
    _Zxr10MplsL2vpnPWTunnelid_Type()
)
zxr10MplsL2vpnPWTunnelid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWTunnelid.setStatus("current")


class _Zxr10MplsL2vpnPWInlabel_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPWInlabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_Zxr10MplsL2vpnPWInlabel_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPWInlabel_Object = MibTableColumn
zxr10MplsL2vpnPWInlabel = _Zxr10MplsL2vpnPWInlabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 7),
    _Zxr10MplsL2vpnPWInlabel_Type()
)
zxr10MplsL2vpnPWInlabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWInlabel.setStatus("current")


class _Zxr10MplsL2vpnPWOutlabel_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPWOutlabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_Zxr10MplsL2vpnPWOutlabel_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPWOutlabel_Object = MibTableColumn
zxr10MplsL2vpnPWOutlabel = _Zxr10MplsL2vpnPWOutlabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 8),
    _Zxr10MplsL2vpnPWOutlabel_Type()
)
zxr10MplsL2vpnPWOutlabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWOutlabel.setStatus("current")
_Zxr10MplsL2vpnPWCbit_Type = MplsL2vpnPWCbit
_Zxr10MplsL2vpnPWCbit_Object = MibTableColumn
zxr10MplsL2vpnPWCbit = _Zxr10MplsL2vpnPWCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 9),
    _Zxr10MplsL2vpnPWCbit_Type()
)
zxr10MplsL2vpnPWCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWCbit.setStatus("current")
_Zxr10MplsL2vpnPWStatus_Type = MplsL2vpnPWStatus
_Zxr10MplsL2vpnPWStatus_Object = MibTableColumn
zxr10MplsL2vpnPWStatus = _Zxr10MplsL2vpnPWStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 10),
    _Zxr10MplsL2vpnPWStatus_Type()
)
zxr10MplsL2vpnPWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWStatus.setStatus("current")
_Zxr10MplsL2vpnPWLocalGroupId_Type = Unsigned32
_Zxr10MplsL2vpnPWLocalGroupId_Object = MibTableColumn
zxr10MplsL2vpnPWLocalGroupId = _Zxr10MplsL2vpnPWLocalGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 11),
    _Zxr10MplsL2vpnPWLocalGroupId_Type()
)
zxr10MplsL2vpnPWLocalGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalGroupId.setStatus("current")
_Zxr10MplsL2vpnPWLocalEncapsulationType_Type = MplsL2vpnPWEncapsulationType
_Zxr10MplsL2vpnPWLocalEncapsulationType_Object = MibTableColumn
zxr10MplsL2vpnPWLocalEncapsulationType = _Zxr10MplsL2vpnPWLocalEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 12),
    _Zxr10MplsL2vpnPWLocalEncapsulationType_Type()
)
zxr10MplsL2vpnPWLocalEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalEncapsulationType.setStatus("current")


class _Zxr10MplsL2vpnPWLocalLabel_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPWLocalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_Zxr10MplsL2vpnPWLocalLabel_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPWLocalLabel_Object = MibTableColumn
zxr10MplsL2vpnPWLocalLabel = _Zxr10MplsL2vpnPWLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 13),
    _Zxr10MplsL2vpnPWLocalLabel_Type()
)
zxr10MplsL2vpnPWLocalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalLabel.setStatus("current")
_Zxr10MplsL2vpnPWLocalCbit_Type = MplsL2vpnPWCbit
_Zxr10MplsL2vpnPWLocalCbit_Object = MibTableColumn
zxr10MplsL2vpnPWLocalCbit = _Zxr10MplsL2vpnPWLocalCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 14),
    _Zxr10MplsL2vpnPWLocalCbit_Type()
)
zxr10MplsL2vpnPWLocalCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalCbit.setStatus("current")


class _Zxr10MplsL2vpnPWLocalPortName_Type(DisplayString):
    """Custom type zxr10MplsL2vpnPWLocalPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10MplsL2vpnPWLocalPortName_Type.__name__ = "DisplayString"
_Zxr10MplsL2vpnPWLocalPortName_Object = MibTableColumn
zxr10MplsL2vpnPWLocalPortName = _Zxr10MplsL2vpnPWLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 15),
    _Zxr10MplsL2vpnPWLocalPortName_Type()
)
zxr10MplsL2vpnPWLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalPortName.setStatus("current")
_Zxr10MplsL2vpnPWLocalRouterId_Type = IpAddress
_Zxr10MplsL2vpnPWLocalRouterId_Object = MibTableColumn
zxr10MplsL2vpnPWLocalRouterId = _Zxr10MplsL2vpnPWLocalRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 16),
    _Zxr10MplsL2vpnPWLocalRouterId_Type()
)
zxr10MplsL2vpnPWLocalRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalRouterId.setStatus("current")


class _Zxr10MplsL2vpnPWLocalIfMtu_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnPWLocalIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10MplsL2vpnPWLocalIfMtu_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnPWLocalIfMtu_Object = MibTableColumn
zxr10MplsL2vpnPWLocalIfMtu = _Zxr10MplsL2vpnPWLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 17),
    _Zxr10MplsL2vpnPWLocalIfMtu_Type()
)
zxr10MplsL2vpnPWLocalIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWLocalIfMtu.setStatus("current")
_Zxr10MplsL2vpnPWRemoteGroupId_Type = Unsigned32
_Zxr10MplsL2vpnPWRemoteGroupId_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteGroupId = _Zxr10MplsL2vpnPWRemoteGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 18),
    _Zxr10MplsL2vpnPWRemoteGroupId_Type()
)
zxr10MplsL2vpnPWRemoteGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteGroupId.setStatus("current")
_Zxr10MplsL2vpnPWRemoteEncapsulationType_Type = MplsL2vpnPWEncapsulationType
_Zxr10MplsL2vpnPWRemoteEncapsulationType_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteEncapsulationType = _Zxr10MplsL2vpnPWRemoteEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 19),
    _Zxr10MplsL2vpnPWRemoteEncapsulationType_Type()
)
zxr10MplsL2vpnPWRemoteEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteEncapsulationType.setStatus("current")
_Zxr10MplsL2vpnPWRemoteLabel_Type = Unsigned32
_Zxr10MplsL2vpnPWRemoteLabel_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteLabel = _Zxr10MplsL2vpnPWRemoteLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 20),
    _Zxr10MplsL2vpnPWRemoteLabel_Type()
)
zxr10MplsL2vpnPWRemoteLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteLabel.setStatus("current")
_Zxr10MplsL2vpnPWRemoteCbit_Type = MplsL2vpnPWCbit
_Zxr10MplsL2vpnPWRemoteCbit_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteCbit = _Zxr10MplsL2vpnPWRemoteCbit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 21),
    _Zxr10MplsL2vpnPWRemoteCbit_Type()
)
zxr10MplsL2vpnPWRemoteCbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteCbit.setStatus("current")


class _Zxr10MplsL2vpnPWRemotePortName_Type(DisplayString):
    """Custom type zxr10MplsL2vpnPWRemotePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10MplsL2vpnPWRemotePortName_Type.__name__ = "DisplayString"
_Zxr10MplsL2vpnPWRemotePortName_Object = MibTableColumn
zxr10MplsL2vpnPWRemotePortName = _Zxr10MplsL2vpnPWRemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 22),
    _Zxr10MplsL2vpnPWRemotePortName_Type()
)
zxr10MplsL2vpnPWRemotePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemotePortName.setStatus("current")
_Zxr10MplsL2vpnPWRemoteRouterId_Type = IpAddress
_Zxr10MplsL2vpnPWRemoteRouterId_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteRouterId = _Zxr10MplsL2vpnPWRemoteRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 23),
    _Zxr10MplsL2vpnPWRemoteRouterId_Type()
)
zxr10MplsL2vpnPWRemoteRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteRouterId.setStatus("current")
_Zxr10MplsL2vpnPWRemoteIfMtu_Type = Unsigned32
_Zxr10MplsL2vpnPWRemoteIfMtu_Object = MibTableColumn
zxr10MplsL2vpnPWRemoteIfMtu = _Zxr10MplsL2vpnPWRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 24),
    _Zxr10MplsL2vpnPWRemoteIfMtu_Type()
)
zxr10MplsL2vpnPWRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnPWRemoteIfMtu.setStatus("current")
_Zxr10MplsL2vpnVpwsIfObjects_ObjectIdentity = ObjectIdentity
zxr10MplsL2vpnVpwsIfObjects = _Zxr10MplsL2vpnVpwsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2)
)
_Zxr10MplsL2vpnVpwsIfTable_Object = MibTable
zxr10MplsL2vpnVpwsIfTable = _Zxr10MplsL2vpnVpwsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfTable.setStatus("current")
_Zxr10MplsL2vpnVpwsIfEntry_Object = MibTableRow
zxr10MplsL2vpnVpwsIfEntry = _Zxr10MplsL2vpnVpwsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1)
)
zxr10MplsL2vpnVpwsIfEntry.setIndexNames(
    (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnInstanceVCId"),
    (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnVpwsIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfEntry.setStatus("current")
_Zxr10MplsL2vpnVpwsIfIndex_Type = InterfaceIndex
_Zxr10MplsL2vpnVpwsIfIndex_Object = MibTableColumn
zxr10MplsL2vpnVpwsIfIndex = _Zxr10MplsL2vpnVpwsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 1),
    _Zxr10MplsL2vpnVpwsIfIndex_Type()
)
zxr10MplsL2vpnVpwsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfIndex.setStatus("current")


class _Zxr10MplsL2vpnVpwsIfName_Type(DisplayString):
    """Custom type zxr10MplsL2vpnVpwsIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10MplsL2vpnVpwsIfName_Type.__name__ = "DisplayString"
_Zxr10MplsL2vpnVpwsIfName_Object = MibTableColumn
zxr10MplsL2vpnVpwsIfName = _Zxr10MplsL2vpnVpwsIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 2),
    _Zxr10MplsL2vpnVpwsIfName_Type()
)
zxr10MplsL2vpnVpwsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfName.setStatus("current")
_Zxr10MplsL2vpnVpwsIfEncapsulationType_Type = MplsL2vpnPWEncapsulationType
_Zxr10MplsL2vpnVpwsIfEncapsulationType_Object = MibTableColumn
zxr10MplsL2vpnVpwsIfEncapsulationType = _Zxr10MplsL2vpnVpwsIfEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 3),
    _Zxr10MplsL2vpnVpwsIfEncapsulationType_Type()
)
zxr10MplsL2vpnVpwsIfEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfEncapsulationType.setStatus("current")


class _Zxr10MplsL2vpnVpwsIfVcid_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnVpwsIfVcid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Zxr10MplsL2vpnVpwsIfVcid_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnVpwsIfVcid_Object = MibTableColumn
zxr10MplsL2vpnVpwsIfVcid = _Zxr10MplsL2vpnVpwsIfVcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 4),
    _Zxr10MplsL2vpnVpwsIfVcid_Type()
)
zxr10MplsL2vpnVpwsIfVcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfVcid.setStatus("current")
_Zxr10MplsL2vpnVpwsIfVpnType_Type = MplsL2vpnType
_Zxr10MplsL2vpnVpwsIfVpnType_Object = MibTableColumn
zxr10MplsL2vpnVpwsIfVpnType = _Zxr10MplsL2vpnVpwsIfVpnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 5),
    _Zxr10MplsL2vpnVpwsIfVpnType_Type()
)
zxr10MplsL2vpnVpwsIfVpnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnVpwsIfVpnType.setStatus("current")
_Zxr10MplsL2vpnNotifications_ObjectIdentity = ObjectIdentity
zxr10MplsL2vpnNotifications = _Zxr10MplsL2vpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3)
)
_Zxr10MplsL2vpnTrapObjects_ObjectIdentity = ObjectIdentity
zxr10MplsL2vpnTrapObjects = _Zxr10MplsL2vpnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4)
)
_Zxr10MplsL2vpnTrapIfIndex_Type = InterfaceIndex
_Zxr10MplsL2vpnTrapIfIndex_Object = MibScalar
zxr10MplsL2vpnTrapIfIndex = _Zxr10MplsL2vpnTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 1),
    _Zxr10MplsL2vpnTrapIfIndex_Type()
)
zxr10MplsL2vpnTrapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapIfIndex.setStatus("current")


class _Zxr10MplsL2vpnTrapIfName_Type(DisplayString):
    """Custom type zxr10MplsL2vpnTrapIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10MplsL2vpnTrapIfName_Type.__name__ = "DisplayString"
_Zxr10MplsL2vpnTrapIfName_Object = MibScalar
zxr10MplsL2vpnTrapIfName = _Zxr10MplsL2vpnTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 2),
    _Zxr10MplsL2vpnTrapIfName_Type()
)
zxr10MplsL2vpnTrapIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapIfName.setStatus("current")
_Zxr10MplsL2vpnTrapLevel_Type = MplsL2vpnTrapLevel
_Zxr10MplsL2vpnTrapLevel_Object = MibScalar
zxr10MplsL2vpnTrapLevel = _Zxr10MplsL2vpnTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 3),
    _Zxr10MplsL2vpnTrapLevel_Type()
)
zxr10MplsL2vpnTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapLevel.setStatus("current")
_Zxr10MplsL2vpnTrapDetail_Type = MplsL2vpnTrapDetail
_Zxr10MplsL2vpnTrapDetail_Object = MibScalar
zxr10MplsL2vpnTrapDetail = _Zxr10MplsL2vpnTrapDetail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 4),
    _Zxr10MplsL2vpnTrapDetail_Type()
)
zxr10MplsL2vpnTrapDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapDetail.setStatus("current")


class _Zxr10MplsL2vpnTrapVcid_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnTrapVcid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Zxr10MplsL2vpnTrapVcid_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnTrapVcid_Object = MibScalar
zxr10MplsL2vpnTrapVcid = _Zxr10MplsL2vpnTrapVcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 5),
    _Zxr10MplsL2vpnTrapVcid_Type()
)
zxr10MplsL2vpnTrapVcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapVcid.setStatus("current")
_Zxr10MplsL2vpnTrapPeerAddress_Type = IpAddress
_Zxr10MplsL2vpnTrapPeerAddress_Object = MibScalar
zxr10MplsL2vpnTrapPeerAddress = _Zxr10MplsL2vpnTrapPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 6),
    _Zxr10MplsL2vpnTrapPeerAddress_Type()
)
zxr10MplsL2vpnTrapPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapPeerAddress.setStatus("current")
_Zxr10MplsL2vpnTrapVpnType_Type = MplsL2vpnType
_Zxr10MplsL2vpnTrapVpnType_Object = MibScalar
zxr10MplsL2vpnTrapVpnType = _Zxr10MplsL2vpnTrapVpnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 7),
    _Zxr10MplsL2vpnTrapVpnType_Type()
)
zxr10MplsL2vpnTrapVpnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapVpnType.setStatus("current")


class _Zxr10MplsL2vpnTrapTETunnelId_Type(Unsigned32):
    """Custom type zxr10MplsL2vpnTrapTETunnelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Zxr10MplsL2vpnTrapTETunnelId_Type.__name__ = "Unsigned32"
_Zxr10MplsL2vpnTrapTETunnelId_Object = MibScalar
zxr10MplsL2vpnTrapTETunnelId = _Zxr10MplsL2vpnTrapTETunnelId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 8),
    _Zxr10MplsL2vpnTrapTETunnelId_Type()
)
zxr10MplsL2vpnTrapTETunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MplsL2vpnTrapTETunnelId.setStatus("current")

# Managed Objects groups


# Notification objects

mplsL2vpnGenericInterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 1)
)
mplsL2vpnGenericInterfaceTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfIndex"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfName"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
)
if mibBuilder.loadTexts:
    mplsL2vpnGenericInterfaceTrap.setStatus(
        "current"
    )

mplsL2vpnMatchInterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 2)
)
mplsL2vpnMatchInterfaceTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfIndex"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfName"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"))
)
if mibBuilder.loadTexts:
    mplsL2vpnMatchInterfaceTrap.setStatus(
        "current"
    )

mplsL2vpnGenericProtocolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 3)
)
mplsL2vpnGenericProtocolTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
)
if mibBuilder.loadTexts:
    mplsL2vpnGenericProtocolTrap.setStatus(
        "current"
    )

mplsL2vpnSessionDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 4)
)
mplsL2vpnSessionDownTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"))
)
if mibBuilder.loadTexts:
    mplsL2vpnSessionDownTrap.setStatus(
        "current"
    )

mplsL2vpnVplsDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 5)
)
mplsL2vpnVplsDeleteTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"))
)
if mibBuilder.loadTexts:
    mplsL2vpnVplsDeleteTrap.setStatus(
        "current"
    )

mplsL2vpnLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 6)
)
mplsL2vpnLinkTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
)
if mibBuilder.loadTexts:
    mplsL2vpnLinkTrap.setStatus(
        "current"
    )

mplsL2vpnPsnRouteDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 7)
)
mplsL2vpnPsnRouteDownTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"))
)
if mibBuilder.loadTexts:
    mplsL2vpnPsnRouteDownTrap.setStatus(
        "current"
    )

mplsL2vpnTETunnelDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 8)
)
mplsL2vpnTETunnelDownTrap.setObjects(
      *(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"),
        ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapTETunnelId"))
)
if mibBuilder.loadTexts:
    mplsL2vpnTETunnelDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MPLS-L2VPN",
    **{"DisplayString": DisplayString,
       "InterfaceIndex": InterfaceIndex,
       "MplsL2vpnType": MplsL2vpnType,
       "MplsL2vpnPWType": MplsL2vpnPWType,
       "MplsL2vpnPWEncapsulationType": MplsL2vpnPWEncapsulationType,
       "MplsL2vpnPWCbit": MplsL2vpnPWCbit,
       "MplsL2vpnPWPsnType": MplsL2vpnPWPsnType,
       "MplsL2vpnPWStatus": MplsL2vpnPWStatus,
       "MplsL2vpnTrapLevel": MplsL2vpnTrapLevel,
       "MplsL2vpnTrapDetail": MplsL2vpnTrapDetail,
       "zxr10MplsL2vpnMIB": zxr10MplsL2vpnMIB,
       "zxr10MplsL2vpnObjects": zxr10MplsL2vpnObjects,
       "zxr10MplsL2vpnInstanceTable": zxr10MplsL2vpnInstanceTable,
       "zxr10MplsL2vpnInstanceEntry": zxr10MplsL2vpnInstanceEntry,
       "zxr10MplsL2vpnInstanceType": zxr10MplsL2vpnInstanceType,
       "zxr10MplsL2vpnInstanceVCId": zxr10MplsL2vpnInstanceVCId,
       "zxr10MplsL2vpnInstanceVpnName": zxr10MplsL2vpnInstanceVpnName,
       "zxr10MplsL2vpnPwCounts": zxr10MplsL2vpnPwCounts,
       "zxr10MplsL2vpnPWObjects": zxr10MplsL2vpnPWObjects,
       "zxr10MplsL2vpnPWTable": zxr10MplsL2vpnPWTable,
       "zxr10MplsL2vpnPWEntry": zxr10MplsL2vpnPWEntry,
       "zxr10MplsL2vpnPWVcId": zxr10MplsL2vpnPWVcId,
       "zxr10MplsL2vpnPWType": zxr10MplsL2vpnPWType,
       "zxr10MplsL2vpnPWEncapsulationType": zxr10MplsL2vpnPWEncapsulationType,
       "zxr10MplsL2vpnPWVlanid": zxr10MplsL2vpnPWVlanid,
       "zxr10MplsL2vpnPWPsnType": zxr10MplsL2vpnPWPsnType,
       "zxr10MplsL2vpnPWTunnelid": zxr10MplsL2vpnPWTunnelid,
       "zxr10MplsL2vpnPWInlabel": zxr10MplsL2vpnPWInlabel,
       "zxr10MplsL2vpnPWOutlabel": zxr10MplsL2vpnPWOutlabel,
       "zxr10MplsL2vpnPWCbit": zxr10MplsL2vpnPWCbit,
       "zxr10MplsL2vpnPWStatus": zxr10MplsL2vpnPWStatus,
       "zxr10MplsL2vpnPWLocalGroupId": zxr10MplsL2vpnPWLocalGroupId,
       "zxr10MplsL2vpnPWLocalEncapsulationType": zxr10MplsL2vpnPWLocalEncapsulationType,
       "zxr10MplsL2vpnPWLocalLabel": zxr10MplsL2vpnPWLocalLabel,
       "zxr10MplsL2vpnPWLocalCbit": zxr10MplsL2vpnPWLocalCbit,
       "zxr10MplsL2vpnPWLocalPortName": zxr10MplsL2vpnPWLocalPortName,
       "zxr10MplsL2vpnPWLocalRouterId": zxr10MplsL2vpnPWLocalRouterId,
       "zxr10MplsL2vpnPWLocalIfMtu": zxr10MplsL2vpnPWLocalIfMtu,
       "zxr10MplsL2vpnPWRemoteGroupId": zxr10MplsL2vpnPWRemoteGroupId,
       "zxr10MplsL2vpnPWRemoteEncapsulationType": zxr10MplsL2vpnPWRemoteEncapsulationType,
       "zxr10MplsL2vpnPWRemoteLabel": zxr10MplsL2vpnPWRemoteLabel,
       "zxr10MplsL2vpnPWRemoteCbit": zxr10MplsL2vpnPWRemoteCbit,
       "zxr10MplsL2vpnPWRemotePortName": zxr10MplsL2vpnPWRemotePortName,
       "zxr10MplsL2vpnPWRemoteRouterId": zxr10MplsL2vpnPWRemoteRouterId,
       "zxr10MplsL2vpnPWRemoteIfMtu": zxr10MplsL2vpnPWRemoteIfMtu,
       "zxr10MplsL2vpnVpwsIfObjects": zxr10MplsL2vpnVpwsIfObjects,
       "zxr10MplsL2vpnVpwsIfTable": zxr10MplsL2vpnVpwsIfTable,
       "zxr10MplsL2vpnVpwsIfEntry": zxr10MplsL2vpnVpwsIfEntry,
       "zxr10MplsL2vpnVpwsIfIndex": zxr10MplsL2vpnVpwsIfIndex,
       "zxr10MplsL2vpnVpwsIfName": zxr10MplsL2vpnVpwsIfName,
       "zxr10MplsL2vpnVpwsIfEncapsulationType": zxr10MplsL2vpnVpwsIfEncapsulationType,
       "zxr10MplsL2vpnVpwsIfVcid": zxr10MplsL2vpnVpwsIfVcid,
       "zxr10MplsL2vpnVpwsIfVpnType": zxr10MplsL2vpnVpwsIfVpnType,
       "zxr10MplsL2vpnNotifications": zxr10MplsL2vpnNotifications,
       "mplsL2vpnGenericInterfaceTrap": mplsL2vpnGenericInterfaceTrap,
       "mplsL2vpnMatchInterfaceTrap": mplsL2vpnMatchInterfaceTrap,
       "mplsL2vpnGenericProtocolTrap": mplsL2vpnGenericProtocolTrap,
       "mplsL2vpnSessionDownTrap": mplsL2vpnSessionDownTrap,
       "mplsL2vpnVplsDeleteTrap": mplsL2vpnVplsDeleteTrap,
       "mplsL2vpnLinkTrap": mplsL2vpnLinkTrap,
       "mplsL2vpnPsnRouteDownTrap": mplsL2vpnPsnRouteDownTrap,
       "mplsL2vpnTETunnelDownTrap": mplsL2vpnTETunnelDownTrap,
       "zxr10MplsL2vpnTrapObjects": zxr10MplsL2vpnTrapObjects,
       "zxr10MplsL2vpnTrapIfIndex": zxr10MplsL2vpnTrapIfIndex,
       "zxr10MplsL2vpnTrapIfName": zxr10MplsL2vpnTrapIfName,
       "zxr10MplsL2vpnTrapLevel": zxr10MplsL2vpnTrapLevel,
       "zxr10MplsL2vpnTrapDetail": zxr10MplsL2vpnTrapDetail,
       "zxr10MplsL2vpnTrapVcid": zxr10MplsL2vpnTrapVcid,
       "zxr10MplsL2vpnTrapPeerAddress": zxr10MplsL2vpnTrapPeerAddress,
       "zxr10MplsL2vpnTrapVpnType": zxr10MplsL2vpnTrapVpnType,
       "zxr10MplsL2vpnTrapTETunnelId": zxr10MplsL2vpnTrapTETunnelId}
)
