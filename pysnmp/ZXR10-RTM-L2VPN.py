# SNMP MIB module (ZXR10-RTM-L2VPN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-RTM-L2VPN
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:06 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zxr10L2vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L2vpn")


# MODULE-IDENTITY

rtmL2vpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3)
)
rtmL2vpnMIB.setRevisions(
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



class RtmL2vpnEncapType(Integer32, TextualConvention):
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



class RtmL2vpnType(Integer32, TextualConvention):
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



class RtmL2vpnVCStatus(Integer32, TextualConvention):
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
        *(("vc-Down", 0),
          ("vc-Up", 1))
    )



class RtmL2vpnCsType(Integer32, TextualConvention):
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
        *(("client", 1),
          ("server", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RtmL2vpnVcObjects_ObjectIdentity = ObjectIdentity
rtmL2vpnVcObjects = _RtmL2vpnVcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0)
)
_RtmL2vpnVcTable_Object = MibTable
rtmL2vpnVcTable = _RtmL2vpnVcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1)
)
if mibBuilder.loadTexts:
    rtmL2vpnVcTable.setStatus("current")
_RtmL2vpnVcEntry_Object = MibTableRow
rtmL2vpnVcEntry = _RtmL2vpnVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1)
)
rtmL2vpnVcEntry.setIndexNames(
    (0, "ZXR10-RTM-L2VPN", "rtmL2vpnVCInInternalLabel"),
)
if mibBuilder.loadTexts:
    rtmL2vpnVcEntry.setStatus("current")


class _RtmL2vpnVCVcId_Type(Unsigned32):
    """Custom type rtmL2vpnVCVcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RtmL2vpnVCVcId_Type.__name__ = "Unsigned32"
_RtmL2vpnVCVcId_Object = MibTableColumn
rtmL2vpnVCVcId = _RtmL2vpnVCVcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 1),
    _RtmL2vpnVCVcId_Type()
)
rtmL2vpnVCVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCVcId.setStatus("current")
_RtmL2vpnVCStatus_Type = RtmL2vpnVCStatus
_RtmL2vpnVCStatus_Object = MibTableColumn
rtmL2vpnVCStatus = _RtmL2vpnVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 2),
    _RtmL2vpnVCStatus_Type()
)
rtmL2vpnVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCStatus.setStatus("current")
_RtmL2vpnVCPeerIP_Type = IpAddress
_RtmL2vpnVCPeerIP_Object = MibTableColumn
rtmL2vpnVCPeerIP = _RtmL2vpnVCPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 3),
    _RtmL2vpnVCPeerIP_Type()
)
rtmL2vpnVCPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCPeerIP.setStatus("current")


class _RtmL2vpnVCInInternalLabel_Type(Unsigned32):
    """Custom type rtmL2vpnVCInInternalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RtmL2vpnVCInInternalLabel_Type.__name__ = "Unsigned32"
_RtmL2vpnVCInInternalLabel_Object = MibTableColumn
rtmL2vpnVCInInternalLabel = _RtmL2vpnVCInInternalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 4),
    _RtmL2vpnVCInInternalLabel_Type()
)
rtmL2vpnVCInInternalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCInInternalLabel.setStatus("current")


class _RtmL2vpnVCOutInternalLabel_Type(Unsigned32):
    """Custom type rtmL2vpnVCOutInternalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RtmL2vpnVCOutInternalLabel_Type.__name__ = "Unsigned32"
_RtmL2vpnVCOutInternalLabel_Object = MibTableColumn
rtmL2vpnVCOutInternalLabel = _RtmL2vpnVCOutInternalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 5),
    _RtmL2vpnVCOutInternalLabel_Type()
)
rtmL2vpnVCOutInternalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCOutInternalLabel.setStatus("current")


class _RtmL2vpnVCInExternalLabel_Type(Unsigned32):
    """Custom type rtmL2vpnVCInExternalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RtmL2vpnVCInExternalLabel_Type.__name__ = "Unsigned32"
_RtmL2vpnVCInExternalLabel_Object = MibTableColumn
rtmL2vpnVCInExternalLabel = _RtmL2vpnVCInExternalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 6),
    _RtmL2vpnVCInExternalLabel_Type()
)
rtmL2vpnVCInExternalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCInExternalLabel.setStatus("current")


class _RtmL2vpnVCOutExternalLabel_Type(Unsigned32):
    """Custom type rtmL2vpnVCOutExternalLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RtmL2vpnVCOutExternalLabel_Type.__name__ = "Unsigned32"
_RtmL2vpnVCOutExternalLabel_Object = MibTableColumn
rtmL2vpnVCOutExternalLabel = _RtmL2vpnVCOutExternalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 7),
    _RtmL2vpnVCOutExternalLabel_Type()
)
rtmL2vpnVCOutExternalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVCOutExternalLabel.setStatus("current")
_RtmL2vpnVplsIfObjects_ObjectIdentity = ObjectIdentity
rtmL2vpnVplsIfObjects = _RtmL2vpnVplsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1)
)
_RtmL2vpnIfTable_Object = MibTable
rtmL2vpnIfTable = _RtmL2vpnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rtmL2vpnIfTable.setStatus("current")
_RtmL2vpnIfEntry_Object = MibTableRow
rtmL2vpnIfEntry = _RtmL2vpnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1)
)
rtmL2vpnIfEntry.setIndexNames(
    (0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfVcid"),
    (0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfIndex"),
)
if mibBuilder.loadTexts:
    rtmL2vpnIfEntry.setStatus("current")


class _RtmL2vpnVplsIfIndex_Type(Unsigned32):
    """Custom type rtmL2vpnVplsIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RtmL2vpnVplsIfIndex_Type.__name__ = "Unsigned32"
_RtmL2vpnVplsIfIndex_Object = MibTableColumn
rtmL2vpnVplsIfIndex = _RtmL2vpnVplsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 1),
    _RtmL2vpnVplsIfIndex_Type()
)
rtmL2vpnVplsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfIndex.setStatus("current")


class _RtmL2vpnVplsIfName_Type(DisplayString):
    """Custom type rtmL2vpnVplsIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RtmL2vpnVplsIfName_Type.__name__ = "DisplayString"
_RtmL2vpnVplsIfName_Object = MibTableColumn
rtmL2vpnVplsIfName = _RtmL2vpnVplsIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 2),
    _RtmL2vpnVplsIfName_Type()
)
rtmL2vpnVplsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfName.setStatus("current")
_RtmL2vpnVplsIfEncapType_Type = Integer32
_RtmL2vpnVplsIfEncapType_Object = MibTableColumn
rtmL2vpnVplsIfEncapType = _RtmL2vpnVplsIfEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 3),
    _RtmL2vpnVplsIfEncapType_Type()
)
rtmL2vpnVplsIfEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfEncapType.setStatus("current")


class _RtmL2vpnVplsIfVpnName_Type(DisplayString):
    """Custom type rtmL2vpnVplsIfVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_RtmL2vpnVplsIfVpnName_Type.__name__ = "DisplayString"
_RtmL2vpnVplsIfVpnName_Object = MibTableColumn
rtmL2vpnVplsIfVpnName = _RtmL2vpnVplsIfVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 4),
    _RtmL2vpnVplsIfVpnName_Type()
)
rtmL2vpnVplsIfVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfVpnName.setStatus("current")


class _RtmL2vpnVplsIfVcid_Type(Unsigned32):
    """Custom type rtmL2vpnVplsIfVcid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RtmL2vpnVplsIfVcid_Type.__name__ = "Unsigned32"
_RtmL2vpnVplsIfVcid_Object = MibTableColumn
rtmL2vpnVplsIfVcid = _RtmL2vpnVplsIfVcid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 5),
    _RtmL2vpnVplsIfVcid_Type()
)
rtmL2vpnVplsIfVcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfVcid.setStatus("current")
_RtmL2vpnVplsIfVpnType_Type = Integer32
_RtmL2vpnVplsIfVpnType_Object = MibTableColumn
rtmL2vpnVplsIfVpnType = _RtmL2vpnVplsIfVpnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 6),
    _RtmL2vpnVplsIfVpnType_Type()
)
rtmL2vpnVplsIfVpnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnVplsIfVpnType.setStatus("current")
_RtmL2vpnIfQinQEx_Type = Integer32
_RtmL2vpnIfQinQEx_Object = MibTableColumn
rtmL2vpnIfQinQEx = _RtmL2vpnIfQinQEx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 7),
    _RtmL2vpnIfQinQEx_Type()
)
rtmL2vpnIfQinQEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfQinQEx.setStatus("current")
_RtmL2vpnIfQinQIn_Type = Integer32
_RtmL2vpnIfQinQIn_Object = MibTableColumn
rtmL2vpnIfQinQIn = _RtmL2vpnIfQinQIn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 8),
    _RtmL2vpnIfQinQIn_Type()
)
rtmL2vpnIfQinQIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfQinQIn.setStatus("current")
_RtmL2vpnIfVlanRangeTop1_Type = Integer32
_RtmL2vpnIfVlanRangeTop1_Object = MibTableColumn
rtmL2vpnIfVlanRangeTop1 = _RtmL2vpnIfVlanRangeTop1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 9),
    _RtmL2vpnIfVlanRangeTop1_Type()
)
rtmL2vpnIfVlanRangeTop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeTop1.setStatus("current")
_RtmL2vpnIfVlanRangeTop2_Type = Integer32
_RtmL2vpnIfVlanRangeTop2_Object = MibTableColumn
rtmL2vpnIfVlanRangeTop2 = _RtmL2vpnIfVlanRangeTop2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 10),
    _RtmL2vpnIfVlanRangeTop2_Type()
)
rtmL2vpnIfVlanRangeTop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeTop2.setStatus("current")
_RtmL2vpnIfVlanRangeTop3_Type = Integer32
_RtmL2vpnIfVlanRangeTop3_Object = MibTableColumn
rtmL2vpnIfVlanRangeTop3 = _RtmL2vpnIfVlanRangeTop3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 11),
    _RtmL2vpnIfVlanRangeTop3_Type()
)
rtmL2vpnIfVlanRangeTop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeTop3.setStatus("current")
_RtmL2vpnIfVlanRangeBot1_Type = Integer32
_RtmL2vpnIfVlanRangeBot1_Object = MibTableColumn
rtmL2vpnIfVlanRangeBot1 = _RtmL2vpnIfVlanRangeBot1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 12),
    _RtmL2vpnIfVlanRangeBot1_Type()
)
rtmL2vpnIfVlanRangeBot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeBot1.setStatus("current")
_RtmL2vpnIfVlanRangeBot2_Type = Integer32
_RtmL2vpnIfVlanRangeBot2_Object = MibTableColumn
rtmL2vpnIfVlanRangeBot2 = _RtmL2vpnIfVlanRangeBot2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 13),
    _RtmL2vpnIfVlanRangeBot2_Type()
)
rtmL2vpnIfVlanRangeBot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeBot2.setStatus("current")
_RtmL2vpnIfVlanRangeBot3_Type = Integer32
_RtmL2vpnIfVlanRangeBot3_Object = MibTableColumn
rtmL2vpnIfVlanRangeBot3 = _RtmL2vpnIfVlanRangeBot3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 14),
    _RtmL2vpnIfVlanRangeBot3_Type()
)
rtmL2vpnIfVlanRangeBot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfVlanRangeBot3.setStatus("current")
_RtmL2vpnIfCSAttr_Type = RtmL2vpnCsType
_RtmL2vpnIfCSAttr_Object = MibTableColumn
rtmL2vpnIfCSAttr = _RtmL2vpnIfCSAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 15),
    _RtmL2vpnIfCSAttr_Type()
)
rtmL2vpnIfCSAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmL2vpnIfCSAttr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-RTM-L2VPN",
    **{"DisplayString": DisplayString,
       "InterfaceIndex": InterfaceIndex,
       "RtmL2vpnEncapType": RtmL2vpnEncapType,
       "RtmL2vpnType": RtmL2vpnType,
       "RtmL2vpnVCStatus": RtmL2vpnVCStatus,
       "RtmL2vpnCsType": RtmL2vpnCsType,
       "rtmL2vpnMIB": rtmL2vpnMIB,
       "rtmL2vpnVcObjects": rtmL2vpnVcObjects,
       "rtmL2vpnVcTable": rtmL2vpnVcTable,
       "rtmL2vpnVcEntry": rtmL2vpnVcEntry,
       "rtmL2vpnVCVcId": rtmL2vpnVCVcId,
       "rtmL2vpnVCStatus": rtmL2vpnVCStatus,
       "rtmL2vpnVCPeerIP": rtmL2vpnVCPeerIP,
       "rtmL2vpnVCInInternalLabel": rtmL2vpnVCInInternalLabel,
       "rtmL2vpnVCOutInternalLabel": rtmL2vpnVCOutInternalLabel,
       "rtmL2vpnVCInExternalLabel": rtmL2vpnVCInExternalLabel,
       "rtmL2vpnVCOutExternalLabel": rtmL2vpnVCOutExternalLabel,
       "rtmL2vpnVplsIfObjects": rtmL2vpnVplsIfObjects,
       "rtmL2vpnIfTable": rtmL2vpnIfTable,
       "rtmL2vpnIfEntry": rtmL2vpnIfEntry,
       "rtmL2vpnVplsIfIndex": rtmL2vpnVplsIfIndex,
       "rtmL2vpnVplsIfName": rtmL2vpnVplsIfName,
       "rtmL2vpnVplsIfEncapType": rtmL2vpnVplsIfEncapType,
       "rtmL2vpnVplsIfVpnName": rtmL2vpnVplsIfVpnName,
       "rtmL2vpnVplsIfVcid": rtmL2vpnVplsIfVcid,
       "rtmL2vpnVplsIfVpnType": rtmL2vpnVplsIfVpnType,
       "rtmL2vpnIfQinQEx": rtmL2vpnIfQinQEx,
       "rtmL2vpnIfQinQIn": rtmL2vpnIfQinQIn,
       "rtmL2vpnIfVlanRangeTop1": rtmL2vpnIfVlanRangeTop1,
       "rtmL2vpnIfVlanRangeTop2": rtmL2vpnIfVlanRangeTop2,
       "rtmL2vpnIfVlanRangeTop3": rtmL2vpnIfVlanRangeTop3,
       "rtmL2vpnIfVlanRangeBot1": rtmL2vpnIfVlanRangeBot1,
       "rtmL2vpnIfVlanRangeBot2": rtmL2vpnIfVlanRangeBot2,
       "rtmL2vpnIfVlanRangeBot3": rtmL2vpnIfVlanRangeBot3,
       "rtmL2vpnIfCSAttr": rtmL2vpnIfCSAttr}
)
