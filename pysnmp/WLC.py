# SNMP MIB module (WLC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:03 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wlc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_WlcSystemInfo_ObjectIdentity = ObjectIdentity
wlcSystemInfo = _WlcSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1)
)
_WlcSystemBasicInfo_ObjectIdentity = ObjectIdentity
wlcSystemBasicInfo = _WlcSystemBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1)
)


class _WlcApMgmtEnable_Type(Integer32):
    """Custom type wlcApMgmtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlcApMgmtEnable_Type.__name__ = "Integer32"
_WlcApMgmtEnable_Object = MibScalar
wlcApMgmtEnable = _WlcApMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 1),
    _WlcApMgmtEnable_Type()
)
wlcApMgmtEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApMgmtEnable.setStatus("current")


class _WlcRemoteApMgmtEnable_Type(Integer32):
    """Custom type wlcRemoteApMgmtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlcRemoteApMgmtEnable_Type.__name__ = "Integer32"
_WlcRemoteApMgmtEnable_Object = MibScalar
wlcRemoteApMgmtEnable = _WlcRemoteApMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 2),
    _WlcRemoteApMgmtEnable_Type()
)
wlcRemoteApMgmtEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcRemoteApMgmtEnable.setStatus("current")
_WlcMaxNumAp_Type = Integer32
_WlcMaxNumAp_Object = MibScalar
wlcMaxNumAp = _WlcMaxNumAp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 3),
    _WlcMaxNumAp_Type()
)
wlcMaxNumAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcMaxNumAp.setStatus("current")
_WlcNumApProfile_Type = Integer32
_WlcNumApProfile_Object = MibScalar
wlcNumApProfile = _WlcNumApProfile_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 4),
    _WlcNumApProfile_Type()
)
wlcNumApProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNumApProfile.setStatus("current")
_WlcNumWlanNetwork_Type = Integer32
_WlcNumWlanNetwork_Object = MibScalar
wlcNumWlanNetwork = _WlcNumWlanNetwork_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 5),
    _WlcNumWlanNetwork_Type()
)
wlcNumWlanNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNumWlanNetwork.setStatus("current")
_WlcNumApReg_Type = Integer32
_WlcNumApReg_Object = MibScalar
wlcNumApReg = _WlcNumApReg_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 6),
    _WlcNumApReg_Type()
)
wlcNumApReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNumApReg.setStatus("current")
_WlcNumApOnline_Type = Integer32
_WlcNumApOnline_Object = MibScalar
wlcNumApOnline = _WlcNumApOnline_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 7),
    _WlcNumApOnline_Type()
)
wlcNumApOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNumApOnline.setStatus("current")
_WlcNumAssocSta_Type = Integer32
_WlcNumAssocSta_Object = MibScalar
wlcNumAssocSta = _WlcNumAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 1, 1, 8),
    _WlcNumAssocSta_Type()
)
wlcNumAssocSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNumAssocSta.setStatus("current")
_WlcApMgmtInfo_ObjectIdentity = ObjectIdentity
wlcApMgmtInfo = _WlcApMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2)
)
_WlcApGroupInfoTable_Object = MibTable
wlcApGroupInfoTable = _WlcApGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wlcApGroupInfoTable.setStatus("current")
_WlcApGroupInfoEntry_Object = MibTableRow
wlcApGroupInfoEntry = _WlcApGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1)
)
wlcApGroupInfoEntry.setIndexNames(
    (0, "WLC", "wlcApGrpId"),
)
if mibBuilder.loadTexts:
    wlcApGroupInfoEntry.setStatus("current")
_WlcApGrpId_Type = Integer32
_WlcApGrpId_Object = MibTableColumn
wlcApGrpId = _WlcApGrpId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 1),
    _WlcApGrpId_Type()
)
wlcApGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpId.setStatus("current")


class _WlcApGrpName_Type(OctetString):
    """Custom type wlcApGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlcApGrpName_Type.__name__ = "OctetString"
_WlcApGrpName_Object = MibTableColumn
wlcApGrpName = _WlcApGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 2),
    _WlcApGrpName_Type()
)
wlcApGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpName.setStatus("current")
_WlcApGrpBand24WlanNetwork_Type = Integer32
_WlcApGrpBand24WlanNetwork_Object = MibTableColumn
wlcApGrpBand24WlanNetwork = _WlcApGrpBand24WlanNetwork_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 3),
    _WlcApGrpBand24WlanNetwork_Type()
)
wlcApGrpBand24WlanNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpBand24WlanNetwork.setStatus("current")
_WlcApGrpBand50WlanNetwork_Type = Integer32
_WlcApGrpBand50WlanNetwork_Object = MibTableColumn
wlcApGrpBand50WlanNetwork = _WlcApGrpBand50WlanNetwork_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 4),
    _WlcApGrpBand50WlanNetwork_Type()
)
wlcApGrpBand50WlanNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpBand50WlanNetwork.setStatus("current")
_WlcApGrpNumApReg_Type = Integer32
_WlcApGrpNumApReg_Object = MibTableColumn
wlcApGrpNumApReg = _WlcApGrpNumApReg_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 5),
    _WlcApGrpNumApReg_Type()
)
wlcApGrpNumApReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpNumApReg.setStatus("current")
_WlcApGrpNumApOnline_Type = Integer32
_WlcApGrpNumApOnline_Object = MibTableColumn
wlcApGrpNumApOnline = _WlcApGrpNumApOnline_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 6),
    _WlcApGrpNumApOnline_Type()
)
wlcApGrpNumApOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpNumApOnline.setStatus("current")
_WlcApGrpNumAssocSta_Type = Integer32
_WlcApGrpNumAssocSta_Object = MibTableColumn
wlcApGrpNumAssocSta = _WlcApGrpNumAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 7),
    _WlcApGrpNumAssocSta_Type()
)
wlcApGrpNumAssocSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpNumAssocSta.setStatus("current")


class _WlcApGrpMgmtVlan_Type(Integer32):
    """Custom type wlcApGrpMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WlcApGrpMgmtVlan_Type.__name__ = "Integer32"
_WlcApGrpMgmtVlan_Object = MibTableColumn
wlcApGrpMgmtVlan = _WlcApGrpMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 1, 1, 8),
    _WlcApGrpMgmtVlan_Type()
)
wlcApGrpMgmtVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpMgmtVlan.setStatus("current")
_WlcApGroupStatTable_Object = MibTable
wlcApGroupStatTable = _WlcApGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2)
)
if mibBuilder.loadTexts:
    wlcApGroupStatTable.setStatus("current")
_WlcApGroupStatEntry_Object = MibTableRow
wlcApGroupStatEntry = _WlcApGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1)
)
wlcApGroupStatEntry.setIndexNames(
    (0, "WLC", "wlcApGrpId"),
    (0, "WLC", "wlcApGrpStatBand"),
)
if mibBuilder.loadTexts:
    wlcApGroupStatEntry.setStatus("current")


class _WlcApGrpStatName_Type(OctetString):
    """Custom type wlcApGrpStatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlcApGrpStatName_Type.__name__ = "OctetString"
_WlcApGrpStatName_Object = MibTableColumn
wlcApGrpStatName = _WlcApGrpStatName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 1),
    _WlcApGrpStatName_Type()
)
wlcApGrpStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatName.setStatus("current")


class _WlcApGrpStatBand_Type(Integer32):
    """Custom type wlcApGrpStatBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band24", 1),
          ("band50", 2))
    )


_WlcApGrpStatBand_Type.__name__ = "Integer32"
_WlcApGrpStatBand_Object = MibTableColumn
wlcApGrpStatBand = _WlcApGrpStatBand_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 2),
    _WlcApGrpStatBand_Type()
)
wlcApGrpStatBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatBand.setStatus("current")
_WlcApGrpStatNumTxPkt_Type = Counter64
_WlcApGrpStatNumTxPkt_Object = MibTableColumn
wlcApGrpStatNumTxPkt = _WlcApGrpStatNumTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 3),
    _WlcApGrpStatNumTxPkt_Type()
)
wlcApGrpStatNumTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatNumTxPkt.setStatus("current")
_WlcApGrpStatNumTxByte_Type = Counter64
_WlcApGrpStatNumTxByte_Object = MibTableColumn
wlcApGrpStatNumTxByte = _WlcApGrpStatNumTxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 4),
    _WlcApGrpStatNumTxByte_Type()
)
wlcApGrpStatNumTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatNumTxByte.setStatus("current")
_WlcApGrpStatNumRxPkt_Type = Counter64
_WlcApGrpStatNumRxPkt_Object = MibTableColumn
wlcApGrpStatNumRxPkt = _WlcApGrpStatNumRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 5),
    _WlcApGrpStatNumRxPkt_Type()
)
wlcApGrpStatNumRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatNumRxPkt.setStatus("current")
_WlcApGrpStatNumRxByte_Type = Counter64
_WlcApGrpStatNumRxByte_Object = MibTableColumn
wlcApGrpStatNumRxByte = _WlcApGrpStatNumRxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 2, 1, 6),
    _WlcApGrpStatNumRxByte_Type()
)
wlcApGrpStatNumRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApGrpStatNumRxByte.setStatus("current")
_WlcWlanNetworkInfoTable_Object = MibTable
wlcWlanNetworkInfoTable = _WlcWlanNetworkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3)
)
if mibBuilder.loadTexts:
    wlcWlanNetworkInfoTable.setStatus("current")
_WlcWlanNetworkInfoEntry_Object = MibTableRow
wlcWlanNetworkInfoEntry = _WlcWlanNetworkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1)
)
wlcWlanNetworkInfoEntry.setIndexNames(
    (0, "WLC", "wlcWlanNetworkId"),
)
if mibBuilder.loadTexts:
    wlcWlanNetworkInfoEntry.setStatus("current")
_WlcWlanNetworkId_Type = Integer32
_WlcWlanNetworkId_Object = MibTableColumn
wlcWlanNetworkId = _WlcWlanNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 1),
    _WlcWlanNetworkId_Type()
)
wlcWlanNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanNetworkId.setStatus("current")


class _WlcWlanEssid_Type(OctetString):
    """Custom type wlcWlanEssid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcWlanEssid_Type.__name__ = "OctetString"
_WlcWlanEssid_Object = MibTableColumn
wlcWlanEssid = _WlcWlanEssid_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 2),
    _WlcWlanEssid_Type()
)
wlcWlanEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanEssid.setStatus("current")


class _WlcWlanSecMode_Type(Integer32):
    """Custom type wlcWlanSecMode based on Integer32"""
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
        *(("legacy8021x", 2),
          ("none", 0),
          ("wep", 1),
          ("wpaMix", 3))
    )


_WlcWlanSecMode_Type.__name__ = "Integer32"
_WlcWlanSecMode_Object = MibTableColumn
wlcWlanSecMode = _WlcWlanSecMode_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 3),
    _WlcWlanSecMode_Type()
)
wlcWlanSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanSecMode.setStatus("current")
_WlcWlanNumApOnline_Type = Integer32
_WlcWlanNumApOnline_Object = MibTableColumn
wlcWlanNumApOnline = _WlcWlanNumApOnline_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 4),
    _WlcWlanNumApOnline_Type()
)
wlcWlanNumApOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanNumApOnline.setStatus("current")
_WlcWlanNumAssocSta_Type = Integer32
_WlcWlanNumAssocSta_Object = MibTableColumn
wlcWlanNumAssocSta = _WlcWlanNumAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 5),
    _WlcWlanNumAssocSta_Type()
)
wlcWlanNumAssocSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanNumAssocSta.setStatus("current")


class _WlcWlanVlanPool_Type(OctetString):
    """Custom type wlcWlanVlanPool based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcWlanVlanPool_Type.__name__ = "OctetString"
_WlcWlanVlanPool_Object = MibTableColumn
wlcWlanVlanPool = _WlcWlanVlanPool_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 3, 1, 6),
    _WlcWlanVlanPool_Type()
)
wlcWlanVlanPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanVlanPool.setStatus("current")
_WlcWlanNetworkStatTable_Object = MibTable
wlcWlanNetworkStatTable = _WlcWlanNetworkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4)
)
if mibBuilder.loadTexts:
    wlcWlanNetworkStatTable.setStatus("current")
_WlcWlanNetworkStatEntry_Object = MibTableRow
wlcWlanNetworkStatEntry = _WlcWlanNetworkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1)
)
wlcWlanNetworkStatEntry.setIndexNames(
    (0, "WLC", "wlcWlanNetworkId"),
    (0, "WLC", "wlcWlanStatBand"),
)
if mibBuilder.loadTexts:
    wlcWlanNetworkStatEntry.setStatus("current")


class _WlcWlanStatEssid_Type(OctetString):
    """Custom type wlcWlanStatEssid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcWlanStatEssid_Type.__name__ = "OctetString"
_WlcWlanStatEssid_Object = MibTableColumn
wlcWlanStatEssid = _WlcWlanStatEssid_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 1),
    _WlcWlanStatEssid_Type()
)
wlcWlanStatEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatEssid.setStatus("current")


class _WlcWlanStatBand_Type(Integer32):
    """Custom type wlcWlanStatBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band24", 1),
          ("band50", 2))
    )


_WlcWlanStatBand_Type.__name__ = "Integer32"
_WlcWlanStatBand_Object = MibTableColumn
wlcWlanStatBand = _WlcWlanStatBand_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 2),
    _WlcWlanStatBand_Type()
)
wlcWlanStatBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatBand.setStatus("current")
_WlcWlanStatNumTxPkt_Type = Counter64
_WlcWlanStatNumTxPkt_Object = MibTableColumn
wlcWlanStatNumTxPkt = _WlcWlanStatNumTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 3),
    _WlcWlanStatNumTxPkt_Type()
)
wlcWlanStatNumTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatNumTxPkt.setStatus("current")
_WlcWlanStatNumTxByte_Type = Counter64
_WlcWlanStatNumTxByte_Object = MibTableColumn
wlcWlanStatNumTxByte = _WlcWlanStatNumTxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 4),
    _WlcWlanStatNumTxByte_Type()
)
wlcWlanStatNumTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatNumTxByte.setStatus("current")
_WlcWlanStatNumRxPkt_Type = Counter64
_WlcWlanStatNumRxPkt_Object = MibTableColumn
wlcWlanStatNumRxPkt = _WlcWlanStatNumRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 5),
    _WlcWlanStatNumRxPkt_Type()
)
wlcWlanStatNumRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatNumRxPkt.setStatus("current")
_WlcWlanStatNumRxByte_Type = Counter64
_WlcWlanStatNumRxByte_Object = MibTableColumn
wlcWlanStatNumRxByte = _WlcWlanStatNumRxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 2, 4, 1, 6),
    _WlcWlanStatNumRxByte_Type()
)
wlcWlanStatNumRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcWlanStatNumRxByte.setStatus("current")
_WlcWlanNeighDeviceInfo_ObjectIdentity = ObjectIdentity
wlcWlanNeighDeviceInfo = _WlcWlanNeighDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3)
)
_WlcWlanNeighApTable_Object = MibTable
wlcWlanNeighApTable = _WlcWlanNeighApTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wlcWlanNeighApTable.setStatus("current")
_WlcWlanNeighApEntry_Object = MibTableRow
wlcWlanNeighApEntry = _WlcWlanNeighApEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1)
)
wlcWlanNeighApEntry.setIndexNames(
    (0, "WLC", "wlcNeighApBssid"),
)
if mibBuilder.loadTexts:
    wlcWlanNeighApEntry.setStatus("current")
_WlcNeighApBssid_Type = MacAddress
_WlcNeighApBssid_Object = MibTableColumn
wlcNeighApBssid = _WlcNeighApBssid_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 1),
    _WlcNeighApBssid_Type()
)
wlcNeighApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighApBssid.setStatus("current")


class _WlcNeighApEssid_Type(OctetString):
    """Custom type wlcNeighApEssid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcNeighApEssid_Type.__name__ = "OctetString"
_WlcNeighApEssid_Object = MibTableColumn
wlcNeighApEssid = _WlcNeighApEssid_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 2),
    _WlcNeighApEssid_Type()
)
wlcNeighApEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighApEssid.setStatus("current")
_WlcNeighApChannel_Type = Integer32
_WlcNeighApChannel_Object = MibTableColumn
wlcNeighApChannel = _WlcNeighApChannel_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 3),
    _WlcNeighApChannel_Type()
)
wlcNeighApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighApChannel.setStatus("current")


class _WlcNeighApEncytMode_Type(Integer32):
    """Custom type wlcNeighApEncytMode based on Integer32"""
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
        *(("none", 0),
          ("wep", 1),
          ("wpa", 2),
          ("wpa2", 3))
    )


_WlcNeighApEncytMode_Type.__name__ = "Integer32"
_WlcNeighApEncytMode_Object = MibTableColumn
wlcNeighApEncytMode = _WlcNeighApEncytMode_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 4),
    _WlcNeighApEncytMode_Type()
)
wlcNeighApEncytMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighApEncytMode.setStatus("current")
_WlcNeighNumApSeen_Type = Integer32
_WlcNeighNumApSeen_Object = MibTableColumn
wlcNeighNumApSeen = _WlcNeighNumApSeen_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 5),
    _WlcNeighNumApSeen_Type()
)
wlcNeighNumApSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighNumApSeen.setStatus("current")


class _WlcNeighNearestAp_Type(OctetString):
    """Custom type wlcNeighNearestAp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WlcNeighNearestAp_Type.__name__ = "OctetString"
_WlcNeighNearestAp_Object = MibTableColumn
wlcNeighNearestAp = _WlcNeighNearestAp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 6),
    _WlcNeighNearestAp_Type()
)
wlcNeighNearestAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighNearestAp.setStatus("current")
_WlcNeighNearestApRssi_Type = Integer32
_WlcNeighNearestApRssi_Object = MibTableColumn
wlcNeighNearestApRssi = _WlcNeighNearestApRssi_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 7),
    _WlcNeighNearestApRssi_Type()
)
wlcNeighNearestApRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighNearestApRssi.setStatus("current")


class _WlcNeighFurthestAp_Type(OctetString):
    """Custom type wlcNeighFurthestAp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WlcNeighFurthestAp_Type.__name__ = "OctetString"
_WlcNeighFurthestAp_Object = MibTableColumn
wlcNeighFurthestAp = _WlcNeighFurthestAp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 8),
    _WlcNeighFurthestAp_Type()
)
wlcNeighFurthestAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighFurthestAp.setStatus("current")
_WlcNeighFurthestApRssi_Type = Integer32
_WlcNeighFurthestApRssi_Object = MibTableColumn
wlcNeighFurthestApRssi = _WlcNeighFurthestApRssi_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 3, 1, 1, 9),
    _WlcNeighFurthestApRssi_Type()
)
wlcNeighFurthestApRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcNeighFurthestApRssi.setStatus("current")
_WlcApInfo_ObjectIdentity = ObjectIdentity
wlcApInfo = _WlcApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4)
)
_WlcApInfoTable_Object = MibTable
wlcApInfoTable = _WlcApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1)
)
if mibBuilder.loadTexts:
    wlcApInfoTable.setStatus("current")
_WlcApInfoEntry_Object = MibTableRow
wlcApInfoEntry = _WlcApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1)
)
wlcApInfoEntry.setIndexNames(
    (0, "WLC", "wlcApInfoApId"),
)
if mibBuilder.loadTexts:
    wlcApInfoEntry.setStatus("current")
_WlcApInfoApId_Type = Integer32
_WlcApInfoApId_Object = MibTableColumn
wlcApInfoApId = _WlcApInfoApId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 1),
    _WlcApInfoApId_Type()
)
wlcApInfoApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApId.setStatus("current")


class _WlcApInfoApSerialNumber_Type(OctetString):
    """Custom type wlcApInfoApSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_WlcApInfoApSerialNumber_Type.__name__ = "OctetString"
_WlcApInfoApSerialNumber_Object = MibTableColumn
wlcApInfoApSerialNumber = _WlcApInfoApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 2),
    _WlcApInfoApSerialNumber_Type()
)
wlcApInfoApSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApSerialNumber.setStatus("current")


class _WlcApInfoApName_Type(OctetString):
    """Custom type wlcApInfoApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcApInfoApName_Type.__name__ = "OctetString"
_WlcApInfoApName_Object = MibTableColumn
wlcApInfoApName = _WlcApInfoApName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 3),
    _WlcApInfoApName_Type()
)
wlcApInfoApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApName.setStatus("current")


class _WlcApInfoApModelName_Type(OctetString):
    """Custom type wlcApInfoApModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcApInfoApModelName_Type.__name__ = "OctetString"
_WlcApInfoApModelName_Object = MibTableColumn
wlcApInfoApModelName = _WlcApInfoApModelName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 4),
    _WlcApInfoApModelName_Type()
)
wlcApInfoApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApModelName.setStatus("current")


class _WlcApInfoApFirmwareVer_Type(OctetString):
    """Custom type wlcApInfoApFirmwareVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlcApInfoApFirmwareVer_Type.__name__ = "OctetString"
_WlcApInfoApFirmwareVer_Object = MibTableColumn
wlcApInfoApFirmwareVer = _WlcApInfoApFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 5),
    _WlcApInfoApFirmwareVer_Type()
)
wlcApInfoApFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApFirmwareVer.setStatus("current")


class _WlcApInfoApStatus_Type(Integer32):
    """Custom type wlcApInfoApStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1))
    )


_WlcApInfoApStatus_Type.__name__ = "Integer32"
_WlcApInfoApStatus_Object = MibTableColumn
wlcApInfoApStatus = _WlcApInfoApStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 6),
    _WlcApInfoApStatus_Type()
)
wlcApInfoApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApStatus.setStatus("current")
_WlcApInfoApIp_Type = IpAddress
_WlcApInfoApIp_Object = MibTableColumn
wlcApInfoApIp = _WlcApInfoApIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 7),
    _WlcApInfoApIp_Type()
)
wlcApInfoApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApIp.setStatus("current")
_WlcApInfoApGrpID_Type = Integer32
_WlcApInfoApGrpID_Object = MibTableColumn
wlcApInfoApGrpID = _WlcApInfoApGrpID_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 8),
    _WlcApInfoApGrpID_Type()
)
wlcApInfoApGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApGrpID.setStatus("current")


class _WlcApInfoApGrpName_Type(OctetString):
    """Custom type wlcApInfoApGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlcApInfoApGrpName_Type.__name__ = "OctetString"
_WlcApInfoApGrpName_Object = MibTableColumn
wlcApInfoApGrpName = _WlcApInfoApGrpName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 4, 4, 1, 1, 9),
    _WlcApInfoApGrpName_Type()
)
wlcApInfoApGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlcApInfoApGrpName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLC",
    **{"pepwave": pepwave,
       "wlc": wlc,
       "wlcSystemInfo": wlcSystemInfo,
       "wlcSystemBasicInfo": wlcSystemBasicInfo,
       "wlcApMgmtEnable": wlcApMgmtEnable,
       "wlcRemoteApMgmtEnable": wlcRemoteApMgmtEnable,
       "wlcMaxNumAp": wlcMaxNumAp,
       "wlcNumApProfile": wlcNumApProfile,
       "wlcNumWlanNetwork": wlcNumWlanNetwork,
       "wlcNumApReg": wlcNumApReg,
       "wlcNumApOnline": wlcNumApOnline,
       "wlcNumAssocSta": wlcNumAssocSta,
       "wlcApMgmtInfo": wlcApMgmtInfo,
       "wlcApGroupInfoTable": wlcApGroupInfoTable,
       "wlcApGroupInfoEntry": wlcApGroupInfoEntry,
       "wlcApGrpId": wlcApGrpId,
       "wlcApGrpName": wlcApGrpName,
       "wlcApGrpBand24WlanNetwork": wlcApGrpBand24WlanNetwork,
       "wlcApGrpBand50WlanNetwork": wlcApGrpBand50WlanNetwork,
       "wlcApGrpNumApReg": wlcApGrpNumApReg,
       "wlcApGrpNumApOnline": wlcApGrpNumApOnline,
       "wlcApGrpNumAssocSta": wlcApGrpNumAssocSta,
       "wlcApGrpMgmtVlan": wlcApGrpMgmtVlan,
       "wlcApGroupStatTable": wlcApGroupStatTable,
       "wlcApGroupStatEntry": wlcApGroupStatEntry,
       "wlcApGrpStatName": wlcApGrpStatName,
       "wlcApGrpStatBand": wlcApGrpStatBand,
       "wlcApGrpStatNumTxPkt": wlcApGrpStatNumTxPkt,
       "wlcApGrpStatNumTxByte": wlcApGrpStatNumTxByte,
       "wlcApGrpStatNumRxPkt": wlcApGrpStatNumRxPkt,
       "wlcApGrpStatNumRxByte": wlcApGrpStatNumRxByte,
       "wlcWlanNetworkInfoTable": wlcWlanNetworkInfoTable,
       "wlcWlanNetworkInfoEntry": wlcWlanNetworkInfoEntry,
       "wlcWlanNetworkId": wlcWlanNetworkId,
       "wlcWlanEssid": wlcWlanEssid,
       "wlcWlanSecMode": wlcWlanSecMode,
       "wlcWlanNumApOnline": wlcWlanNumApOnline,
       "wlcWlanNumAssocSta": wlcWlanNumAssocSta,
       "wlcWlanVlanPool": wlcWlanVlanPool,
       "wlcWlanNetworkStatTable": wlcWlanNetworkStatTable,
       "wlcWlanNetworkStatEntry": wlcWlanNetworkStatEntry,
       "wlcWlanStatEssid": wlcWlanStatEssid,
       "wlcWlanStatBand": wlcWlanStatBand,
       "wlcWlanStatNumTxPkt": wlcWlanStatNumTxPkt,
       "wlcWlanStatNumTxByte": wlcWlanStatNumTxByte,
       "wlcWlanStatNumRxPkt": wlcWlanStatNumRxPkt,
       "wlcWlanStatNumRxByte": wlcWlanStatNumRxByte,
       "wlcWlanNeighDeviceInfo": wlcWlanNeighDeviceInfo,
       "wlcWlanNeighApTable": wlcWlanNeighApTable,
       "wlcWlanNeighApEntry": wlcWlanNeighApEntry,
       "wlcNeighApBssid": wlcNeighApBssid,
       "wlcNeighApEssid": wlcNeighApEssid,
       "wlcNeighApChannel": wlcNeighApChannel,
       "wlcNeighApEncytMode": wlcNeighApEncytMode,
       "wlcNeighNumApSeen": wlcNeighNumApSeen,
       "wlcNeighNearestAp": wlcNeighNearestAp,
       "wlcNeighNearestApRssi": wlcNeighNearestApRssi,
       "wlcNeighFurthestAp": wlcNeighFurthestAp,
       "wlcNeighFurthestApRssi": wlcNeighFurthestApRssi,
       "wlcApInfo": wlcApInfo,
       "wlcApInfoTable": wlcApInfoTable,
       "wlcApInfoEntry": wlcApInfoEntry,
       "wlcApInfoApId": wlcApInfoApId,
       "wlcApInfoApSerialNumber": wlcApInfoApSerialNumber,
       "wlcApInfoApName": wlcApInfoApName,
       "wlcApInfoApModelName": wlcApInfoApModelName,
       "wlcApInfoApFirmwareVer": wlcApInfoApFirmwareVer,
       "wlcApInfoApStatus": wlcApInfoApStatus,
       "wlcApInfoApIp": wlcApInfoApIp,
       "wlcApInfoApGrpID": wlcApInfoApGrpID,
       "wlcApInfoApGrpName": wlcApInfoApGrpName}
)
