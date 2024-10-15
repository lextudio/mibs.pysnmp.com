# SNMP MIB module (HH3C-L2VPN-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-L2VPN-PWE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:43 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cL2VpnPwe3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cL2VpnVcEncapsType(Integer32, TextualConvention):
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

_Hh3cL2VpnPwe3ScalarGroup_ObjectIdentity = ObjectIdentity
hh3cL2VpnPwe3ScalarGroup = _Hh3cL2VpnPwe3ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 1)
)


class _Hh3cPwVcTrapOpen_Type(TruthValue):
    """Custom type hh3cPwVcTrapOpen based on TruthValue"""


_Hh3cPwVcTrapOpen_Object = MibScalar
hh3cPwVcTrapOpen = _Hh3cPwVcTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 1, 1),
    _Hh3cPwVcTrapOpen_Type()
)
hh3cPwVcTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPwVcTrapOpen.setStatus("current")
_Hh3cL2VpnPwe3Table_ObjectIdentity = ObjectIdentity
hh3cL2VpnPwe3Table = _Hh3cL2VpnPwe3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2)
)
_Hh3cPwVcTable_Object = MibTable
hh3cPwVcTable = _Hh3cPwVcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPwVcTable.setStatus("current")
_Hh3cPwVcEntry_Object = MibTableRow
hh3cPwVcEntry = _Hh3cPwVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1)
)
hh3cPwVcEntry.setIndexNames(
    (0, "HH3C-L2VPN-PWE3-MIB", "hh3cPwVcIndex"),
)
if mibBuilder.loadTexts:
    hh3cPwVcEntry.setStatus("current")
_Hh3cPwVcIndex_Type = Integer32
_Hh3cPwVcIndex_Object = MibTableColumn
hh3cPwVcIndex = _Hh3cPwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 1),
    _Hh3cPwVcIndex_Type()
)
hh3cPwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPwVcIndex.setStatus("current")
_Hh3cPwVcID_Type = Unsigned32
_Hh3cPwVcID_Object = MibTableColumn
hh3cPwVcID = _Hh3cPwVcID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 2),
    _Hh3cPwVcID_Type()
)
hh3cPwVcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcID.setStatus("current")
_Hh3cPwVcType_Type = Hh3cL2VpnVcEncapsType
_Hh3cPwVcType_Object = MibTableColumn
hh3cPwVcType = _Hh3cPwVcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 3),
    _Hh3cPwVcType_Type()
)
hh3cPwVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcType.setStatus("current")
_Hh3cPwVcPeerAddr_Type = IpAddress
_Hh3cPwVcPeerAddr_Object = MibTableColumn
hh3cPwVcPeerAddr = _Hh3cPwVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 4),
    _Hh3cPwVcPeerAddr_Type()
)
hh3cPwVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcPeerAddr.setStatus("current")
_Hh3cPwVcMtu_Type = Unsigned32
_Hh3cPwVcMtu_Object = MibTableColumn
hh3cPwVcMtu = _Hh3cPwVcMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 5),
    _Hh3cPwVcMtu_Type()
)
hh3cPwVcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcMtu.setStatus("current")


class _Hh3cPwVcCfgType_Type(Integer32):
    """Custom type hh3cPwVcCfgType based on Integer32"""
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


_Hh3cPwVcCfgType_Type.__name__ = "Integer32"
_Hh3cPwVcCfgType_Object = MibTableColumn
hh3cPwVcCfgType = _Hh3cPwVcCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 6),
    _Hh3cPwVcCfgType_Type()
)
hh3cPwVcCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcCfgType.setStatus("current")
_Hh3cPwVcInboundLabel_Type = Unsigned32
_Hh3cPwVcInboundLabel_Object = MibTableColumn
hh3cPwVcInboundLabel = _Hh3cPwVcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 7),
    _Hh3cPwVcInboundLabel_Type()
)
hh3cPwVcInboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPwVcInboundLabel.setStatus("current")
_Hh3cPwVcOutboundLabel_Type = Unsigned32
_Hh3cPwVcOutboundLabel_Object = MibTableColumn
hh3cPwVcOutboundLabel = _Hh3cPwVcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 8),
    _Hh3cPwVcOutboundLabel_Type()
)
hh3cPwVcOutboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPwVcOutboundLabel.setStatus("current")
_Hh3cPwVcIfIndex_Type = Unsigned32
_Hh3cPwVcIfIndex_Object = MibTableColumn
hh3cPwVcIfIndex = _Hh3cPwVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 9),
    _Hh3cPwVcIfIndex_Type()
)
hh3cPwVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcIfIndex.setStatus("current")


class _Hh3cPwVcAcStatus_Type(Integer32):
    """Custom type hh3cPwVcAcStatus based on Integer32"""
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


_Hh3cPwVcAcStatus_Type.__name__ = "Integer32"
_Hh3cPwVcAcStatus_Object = MibTableColumn
hh3cPwVcAcStatus = _Hh3cPwVcAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 10),
    _Hh3cPwVcAcStatus_Type()
)
hh3cPwVcAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPwVcAcStatus.setStatus("current")


class _Hh3cPwVcStatus_Type(Integer32):
    """Custom type hh3cPwVcStatus based on Integer32"""
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


_Hh3cPwVcStatus_Type.__name__ = "Integer32"
_Hh3cPwVcStatus_Object = MibTableColumn
hh3cPwVcStatus = _Hh3cPwVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 11),
    _Hh3cPwVcStatus_Type()
)
hh3cPwVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPwVcStatus.setStatus("current")
_Hh3cPwVcRowStatus_Type = RowStatus
_Hh3cPwVcRowStatus_Object = MibTableColumn
hh3cPwVcRowStatus = _Hh3cPwVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 12),
    _Hh3cPwVcRowStatus_Type()
)
hh3cPwVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPwVcRowStatus.setStatus("current")
_Hh3cL2VpnPwe3Notifications_ObjectIdentity = ObjectIdentity
hh3cL2VpnPwe3Notifications = _Hh3cL2VpnPwe3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3)
)

# Managed Objects groups


# Notification objects

hh3cPwVcSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 1)
)
hh3cPwVcSwitchWtoP.setObjects(
      *(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hh3cPwVcSwitchWtoP.setStatus(
        "current"
    )

hh3cPwVcSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 2)
)
hh3cPwVcSwitchPtoW.setObjects(
      *(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hh3cPwVcSwitchPtoW.setStatus(
        "current"
    )

hh3cPwVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 3)
)
hh3cPwVcDown.setObjects(
      *(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hh3cPwVcDown.setStatus(
        "current"
    )

hh3cPwVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 4)
)
hh3cPwVcUp.setObjects(
      *(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hh3cPwVcUp.setStatus(
        "current"
    )

hh3cPwVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 5)
)
hh3cPwVcDeleted.setObjects(
      *(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"),
        ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hh3cPwVcDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2VPN-PWE3-MIB",
    **{"Hh3cL2VpnVcEncapsType": Hh3cL2VpnVcEncapsType,
       "hh3cL2VpnPwe3": hh3cL2VpnPwe3,
       "hh3cL2VpnPwe3ScalarGroup": hh3cL2VpnPwe3ScalarGroup,
       "hh3cPwVcTrapOpen": hh3cPwVcTrapOpen,
       "hh3cL2VpnPwe3Table": hh3cL2VpnPwe3Table,
       "hh3cPwVcTable": hh3cPwVcTable,
       "hh3cPwVcEntry": hh3cPwVcEntry,
       "hh3cPwVcIndex": hh3cPwVcIndex,
       "hh3cPwVcID": hh3cPwVcID,
       "hh3cPwVcType": hh3cPwVcType,
       "hh3cPwVcPeerAddr": hh3cPwVcPeerAddr,
       "hh3cPwVcMtu": hh3cPwVcMtu,
       "hh3cPwVcCfgType": hh3cPwVcCfgType,
       "hh3cPwVcInboundLabel": hh3cPwVcInboundLabel,
       "hh3cPwVcOutboundLabel": hh3cPwVcOutboundLabel,
       "hh3cPwVcIfIndex": hh3cPwVcIfIndex,
       "hh3cPwVcAcStatus": hh3cPwVcAcStatus,
       "hh3cPwVcStatus": hh3cPwVcStatus,
       "hh3cPwVcRowStatus": hh3cPwVcRowStatus,
       "hh3cL2VpnPwe3Notifications": hh3cL2VpnPwe3Notifications,
       "hh3cPwVcSwitchWtoP": hh3cPwVcSwitchWtoP,
       "hh3cPwVcSwitchPtoW": hh3cPwVcSwitchPtoW,
       "hh3cPwVcDown": hh3cPwVcDown,
       "hh3cPwVcUp": hh3cPwVcUp,
       "hh3cPwVcDeleted": hh3cPwVcDeleted}
)
