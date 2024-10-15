# SNMP MIB module (A3COM-HUAWEI-L2VPN-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-L2VPN-PWE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:14 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cL2VpnPwe3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cL2VpnVcEncapsType(Integer32, TextualConvention):
    status = "current"
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5PduVccTransport", 14),
          ("atmAal5SduVccTransport", 2),
          ("atmN2OneVccCellTransport", 9),
          ("atmN2OneVpcCellTransport", 10),
          ("atmOne2OneVccCellMode", 12),
          ("atmOne2OneVpcCellMode", 13),
          ("atmTransparentCellTransport", 3),
          ("cESoPsnBasicMode", 21),
          ("cem", 8),
          ("cep", 16),
          ("ethernet", 5),
          ("ethernetTagged", 4),
          ("frameRelayDlci", 25),
          ("frameRelayDlciMartini", 1),
          ("frameRelayPortMode", 15),
          ("hdlc", 6),
          ("ipInterworking", 64),
          ("ipLayer2Transport", 11),
          ("l2VpnCESoPSNTDMwithCAS", 23),
          ("l2VpnTDMoIPTDMwithCAS", 24),
          ("ppp", 7),
          ("saE1oP", 17),
          ("saE3oP", 19),
          ("saT1oP", 18),
          ("saT3oP", 20),
          ("tDMoIPbasicMode", 22),
          ("unknown", 255))
    )



# MIB Managed Objects in the order of their OIDs

_H3cL2VpnPwe3ScalarGroup_ObjectIdentity = ObjectIdentity
h3cL2VpnPwe3ScalarGroup = _H3cL2VpnPwe3ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 1)
)


class _H3cPwVcTrapOpen_Type(TruthValue):
    """Custom type h3cPwVcTrapOpen based on TruthValue"""


_H3cPwVcTrapOpen_Object = MibScalar
h3cPwVcTrapOpen = _H3cPwVcTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 1, 1),
    _H3cPwVcTrapOpen_Type()
)
h3cPwVcTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPwVcTrapOpen.setStatus("current")
_H3cL2VpnPwe3Table_ObjectIdentity = ObjectIdentity
h3cL2VpnPwe3Table = _H3cL2VpnPwe3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2)
)
_H3cPwVcTable_Object = MibTable
h3cPwVcTable = _H3cPwVcTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPwVcTable.setStatus("current")
_H3cPwVcEntry_Object = MibTableRow
h3cPwVcEntry = _H3cPwVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1)
)
h3cPwVcEntry.setIndexNames(
    (0, "A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcIndex"),
)
if mibBuilder.loadTexts:
    h3cPwVcEntry.setStatus("current")
_H3cPwVcIndex_Type = Integer32
_H3cPwVcIndex_Object = MibTableColumn
h3cPwVcIndex = _H3cPwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 1),
    _H3cPwVcIndex_Type()
)
h3cPwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPwVcIndex.setStatus("current")
_H3cPwVcID_Type = Unsigned32
_H3cPwVcID_Object = MibTableColumn
h3cPwVcID = _H3cPwVcID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 2),
    _H3cPwVcID_Type()
)
h3cPwVcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcID.setStatus("current")
_H3cPwVcType_Type = H3cL2VpnVcEncapsType
_H3cPwVcType_Object = MibTableColumn
h3cPwVcType = _H3cPwVcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 3),
    _H3cPwVcType_Type()
)
h3cPwVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcType.setStatus("current")
_H3cPwVcPeerAddr_Type = IpAddress
_H3cPwVcPeerAddr_Object = MibTableColumn
h3cPwVcPeerAddr = _H3cPwVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 4),
    _H3cPwVcPeerAddr_Type()
)
h3cPwVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcPeerAddr.setStatus("current")
_H3cPwVcMtu_Type = Unsigned32
_H3cPwVcMtu_Object = MibTableColumn
h3cPwVcMtu = _H3cPwVcMtu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 5),
    _H3cPwVcMtu_Type()
)
h3cPwVcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcMtu.setStatus("current")


class _HwPwVcCfgType_Type(Integer32):
    """Custom type hwPwVcCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("multiPort", 3),
          ("primary", 1))
    )


_HwPwVcCfgType_Type.__name__ = "Integer32"
_HwPwVcCfgType_Object = MibTableColumn
hwPwVcCfgType = _HwPwVcCfgType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 6),
    _HwPwVcCfgType_Type()
)
hwPwVcCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwVcCfgType.setStatus("current")
_H3cPwVcInboundLabel_Type = Unsigned32
_H3cPwVcInboundLabel_Object = MibTableColumn
h3cPwVcInboundLabel = _H3cPwVcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 7),
    _H3cPwVcInboundLabel_Type()
)
h3cPwVcInboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPwVcInboundLabel.setStatus("current")
_H3cPwVcOutboundLabel_Type = Unsigned32
_H3cPwVcOutboundLabel_Object = MibTableColumn
h3cPwVcOutboundLabel = _H3cPwVcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 8),
    _H3cPwVcOutboundLabel_Type()
)
h3cPwVcOutboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPwVcOutboundLabel.setStatus("current")
_H3cPwVcIfIndex_Type = Unsigned32
_H3cPwVcIfIndex_Object = MibTableColumn
h3cPwVcIfIndex = _H3cPwVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 9),
    _H3cPwVcIfIndex_Type()
)
h3cPwVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcIfIndex.setStatus("current")


class _H3cPwVcAcStatus_Type(Integer32):
    """Custom type h3cPwVcAcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_H3cPwVcAcStatus_Type.__name__ = "Integer32"
_H3cPwVcAcStatus_Object = MibTableColumn
h3cPwVcAcStatus = _H3cPwVcAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 10),
    _H3cPwVcAcStatus_Type()
)
h3cPwVcAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPwVcAcStatus.setStatus("current")


class _H3cPwVcStatus_Type(Integer32):
    """Custom type h3cPwVcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_H3cPwVcStatus_Type.__name__ = "Integer32"
_H3cPwVcStatus_Object = MibTableColumn
h3cPwVcStatus = _H3cPwVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 11),
    _H3cPwVcStatus_Type()
)
h3cPwVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPwVcStatus.setStatus("current")
_H3cPwVcRowStatus_Type = RowStatus
_H3cPwVcRowStatus_Object = MibTableColumn
h3cPwVcRowStatus = _H3cPwVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 2, 1, 1, 12),
    _H3cPwVcRowStatus_Type()
)
h3cPwVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPwVcRowStatus.setStatus("current")
_H3cL2VpnPwe3Notifications_ObjectIdentity = ObjectIdentity
h3cL2VpnPwe3Notifications = _H3cL2VpnPwe3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3)
)

# Managed Objects groups


# Notification objects

h3cPwVcSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3, 1)
)
h3cPwVcSwitchWtoP.setObjects(
      *(("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    h3cPwVcSwitchWtoP.setStatus(
        "current"
    )

h3cPwVcSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3, 2)
)
h3cPwVcSwitchPtoW.setObjects(
      *(("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    h3cPwVcSwitchPtoW.setStatus(
        "current"
    )

h3cPwVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3, 3)
)
h3cPwVcDown.setObjects(
      *(("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    h3cPwVcDown.setStatus(
        "current"
    )

h3cPwVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3, 4)
)
h3cPwVcUp.setObjects(
      *(("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    h3cPwVcUp.setStatus(
        "current"
    )

h3cPwVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 78, 3, 5)
)
h3cPwVcDeleted.setObjects(
      *(("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcID"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcType"),
        ("A3COM-HUAWEI-L2VPN-PWE3-MIB", "h3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    h3cPwVcDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-L2VPN-PWE3-MIB",
    **{"H3cL2VpnVcEncapsType": H3cL2VpnVcEncapsType,
       "h3cL2VpnPwe3": h3cL2VpnPwe3,
       "h3cL2VpnPwe3ScalarGroup": h3cL2VpnPwe3ScalarGroup,
       "h3cPwVcTrapOpen": h3cPwVcTrapOpen,
       "h3cL2VpnPwe3Table": h3cL2VpnPwe3Table,
       "h3cPwVcTable": h3cPwVcTable,
       "h3cPwVcEntry": h3cPwVcEntry,
       "h3cPwVcIndex": h3cPwVcIndex,
       "h3cPwVcID": h3cPwVcID,
       "h3cPwVcType": h3cPwVcType,
       "h3cPwVcPeerAddr": h3cPwVcPeerAddr,
       "h3cPwVcMtu": h3cPwVcMtu,
       "hwPwVcCfgType": hwPwVcCfgType,
       "h3cPwVcInboundLabel": h3cPwVcInboundLabel,
       "h3cPwVcOutboundLabel": h3cPwVcOutboundLabel,
       "h3cPwVcIfIndex": h3cPwVcIfIndex,
       "h3cPwVcAcStatus": h3cPwVcAcStatus,
       "h3cPwVcStatus": h3cPwVcStatus,
       "h3cPwVcRowStatus": h3cPwVcRowStatus,
       "h3cL2VpnPwe3Notifications": h3cL2VpnPwe3Notifications,
       "h3cPwVcSwitchWtoP": h3cPwVcSwitchWtoP,
       "h3cPwVcSwitchPtoW": h3cPwVcSwitchPtoW,
       "h3cPwVcDown": h3cPwVcDown,
       "h3cPwVcUp": h3cPwVcUp,
       "h3cPwVcDeleted": h3cPwVcDeleted}
)
