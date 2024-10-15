# SNMP MIB module (HPN-ICF-L2VPN-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-L2VPN-PWE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:43 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfL2VpnPwe3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfL2VpnVcEncapsType(Integer32, TextualConvention):
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

_HpnicfL2VpnPwe3ScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfL2VpnPwe3ScalarGroup = _HpnicfL2VpnPwe3ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 1)
)


class _HpnicfPwVcTrapOpen_Type(TruthValue):
    """Custom type hpnicfPwVcTrapOpen based on TruthValue"""


_HpnicfPwVcTrapOpen_Object = MibScalar
hpnicfPwVcTrapOpen = _HpnicfPwVcTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 1, 1),
    _HpnicfPwVcTrapOpen_Type()
)
hpnicfPwVcTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPwVcTrapOpen.setStatus("current")
_HpnicfL2VpnPwe3Table_ObjectIdentity = ObjectIdentity
hpnicfL2VpnPwe3Table = _HpnicfL2VpnPwe3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2)
)
_HpnicfPwVcTable_Object = MibTable
hpnicfPwVcTable = _HpnicfPwVcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfPwVcTable.setStatus("current")
_HpnicfPwVcEntry_Object = MibTableRow
hpnicfPwVcEntry = _HpnicfPwVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1)
)
hpnicfPwVcEntry.setIndexNames(
    (0, "HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPwVcEntry.setStatus("current")
_HpnicfPwVcIndex_Type = Integer32
_HpnicfPwVcIndex_Object = MibTableColumn
hpnicfPwVcIndex = _HpnicfPwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 1),
    _HpnicfPwVcIndex_Type()
)
hpnicfPwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPwVcIndex.setStatus("current")
_HpnicfPwVcID_Type = Unsigned32
_HpnicfPwVcID_Object = MibTableColumn
hpnicfPwVcID = _HpnicfPwVcID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 2),
    _HpnicfPwVcID_Type()
)
hpnicfPwVcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcID.setStatus("current")
_HpnicfPwVcType_Type = HpnicfL2VpnVcEncapsType
_HpnicfPwVcType_Object = MibTableColumn
hpnicfPwVcType = _HpnicfPwVcType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 3),
    _HpnicfPwVcType_Type()
)
hpnicfPwVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcType.setStatus("current")
_HpnicfPwVcPeerAddr_Type = IpAddress
_HpnicfPwVcPeerAddr_Object = MibTableColumn
hpnicfPwVcPeerAddr = _HpnicfPwVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 4),
    _HpnicfPwVcPeerAddr_Type()
)
hpnicfPwVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcPeerAddr.setStatus("current")
_HpnicfPwVcMtu_Type = Unsigned32
_HpnicfPwVcMtu_Object = MibTableColumn
hpnicfPwVcMtu = _HpnicfPwVcMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 5),
    _HpnicfPwVcMtu_Type()
)
hpnicfPwVcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcMtu.setStatus("current")


class _HpnicfPwVcCfgType_Type(Integer32):
    """Custom type hpnicfPwVcCfgType based on Integer32"""
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


_HpnicfPwVcCfgType_Type.__name__ = "Integer32"
_HpnicfPwVcCfgType_Object = MibTableColumn
hpnicfPwVcCfgType = _HpnicfPwVcCfgType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 6),
    _HpnicfPwVcCfgType_Type()
)
hpnicfPwVcCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcCfgType.setStatus("current")
_HpnicfPwVcInboundLabel_Type = Unsigned32
_HpnicfPwVcInboundLabel_Object = MibTableColumn
hpnicfPwVcInboundLabel = _HpnicfPwVcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 7),
    _HpnicfPwVcInboundLabel_Type()
)
hpnicfPwVcInboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPwVcInboundLabel.setStatus("current")
_HpnicfPwVcOutboundLabel_Type = Unsigned32
_HpnicfPwVcOutboundLabel_Object = MibTableColumn
hpnicfPwVcOutboundLabel = _HpnicfPwVcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 8),
    _HpnicfPwVcOutboundLabel_Type()
)
hpnicfPwVcOutboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPwVcOutboundLabel.setStatus("current")
_HpnicfPwVcIfIndex_Type = Unsigned32
_HpnicfPwVcIfIndex_Object = MibTableColumn
hpnicfPwVcIfIndex = _HpnicfPwVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 9),
    _HpnicfPwVcIfIndex_Type()
)
hpnicfPwVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcIfIndex.setStatus("current")


class _HpnicfPwVcAcStatus_Type(Integer32):
    """Custom type hpnicfPwVcAcStatus based on Integer32"""
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


_HpnicfPwVcAcStatus_Type.__name__ = "Integer32"
_HpnicfPwVcAcStatus_Object = MibTableColumn
hpnicfPwVcAcStatus = _HpnicfPwVcAcStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 10),
    _HpnicfPwVcAcStatus_Type()
)
hpnicfPwVcAcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPwVcAcStatus.setStatus("current")


class _HpnicfPwVcStatus_Type(Integer32):
    """Custom type hpnicfPwVcStatus based on Integer32"""
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


_HpnicfPwVcStatus_Type.__name__ = "Integer32"
_HpnicfPwVcStatus_Object = MibTableColumn
hpnicfPwVcStatus = _HpnicfPwVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 11),
    _HpnicfPwVcStatus_Type()
)
hpnicfPwVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPwVcStatus.setStatus("current")
_HpnicfPwVcRowStatus_Type = RowStatus
_HpnicfPwVcRowStatus_Object = MibTableColumn
hpnicfPwVcRowStatus = _HpnicfPwVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 2, 1, 1, 12),
    _HpnicfPwVcRowStatus_Type()
)
hpnicfPwVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPwVcRowStatus.setStatus("current")
_HpnicfL2VpnPwe3Notifications_ObjectIdentity = ObjectIdentity
hpnicfL2VpnPwe3Notifications = _HpnicfL2VpnPwe3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3)
)

# Managed Objects groups


# Notification objects

hpnicfPwVcSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3, 1)
)
hpnicfPwVcSwitchWtoP.setObjects(
      *(("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPwVcSwitchWtoP.setStatus(
        "current"
    )

hpnicfPwVcSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3, 2)
)
hpnicfPwVcSwitchPtoW.setObjects(
      *(("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPwVcSwitchPtoW.setStatus(
        "current"
    )

hpnicfPwVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3, 3)
)
hpnicfPwVcDown.setObjects(
      *(("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPwVcDown.setStatus(
        "current"
    )

hpnicfPwVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3, 4)
)
hpnicfPwVcUp.setObjects(
      *(("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPwVcUp.setStatus(
        "current"
    )

hpnicfPwVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78, 3, 5)
)
hpnicfPwVcDeleted.setObjects(
      *(("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcID"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcType"),
        ("HPN-ICF-L2VPN-PWE3-MIB", "hpnicfPwVcPeerAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPwVcDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-L2VPN-PWE3-MIB",
    **{"HpnicfL2VpnVcEncapsType": HpnicfL2VpnVcEncapsType,
       "hpnicfL2VpnPwe3": hpnicfL2VpnPwe3,
       "hpnicfL2VpnPwe3ScalarGroup": hpnicfL2VpnPwe3ScalarGroup,
       "hpnicfPwVcTrapOpen": hpnicfPwVcTrapOpen,
       "hpnicfL2VpnPwe3Table": hpnicfL2VpnPwe3Table,
       "hpnicfPwVcTable": hpnicfPwVcTable,
       "hpnicfPwVcEntry": hpnicfPwVcEntry,
       "hpnicfPwVcIndex": hpnicfPwVcIndex,
       "hpnicfPwVcID": hpnicfPwVcID,
       "hpnicfPwVcType": hpnicfPwVcType,
       "hpnicfPwVcPeerAddr": hpnicfPwVcPeerAddr,
       "hpnicfPwVcMtu": hpnicfPwVcMtu,
       "hpnicfPwVcCfgType": hpnicfPwVcCfgType,
       "hpnicfPwVcInboundLabel": hpnicfPwVcInboundLabel,
       "hpnicfPwVcOutboundLabel": hpnicfPwVcOutboundLabel,
       "hpnicfPwVcIfIndex": hpnicfPwVcIfIndex,
       "hpnicfPwVcAcStatus": hpnicfPwVcAcStatus,
       "hpnicfPwVcStatus": hpnicfPwVcStatus,
       "hpnicfPwVcRowStatus": hpnicfPwVcRowStatus,
       "hpnicfL2VpnPwe3Notifications": hpnicfL2VpnPwe3Notifications,
       "hpnicfPwVcSwitchWtoP": hpnicfPwVcSwitchWtoP,
       "hpnicfPwVcSwitchPtoW": hpnicfPwVcSwitchPtoW,
       "hpnicfPwVcDown": hpnicfPwVcDown,
       "hpnicfPwVcUp": hpnicfPwVcUp,
       "hpnicfPwVcDeleted": hpnicfPwVcDeleted}
)
