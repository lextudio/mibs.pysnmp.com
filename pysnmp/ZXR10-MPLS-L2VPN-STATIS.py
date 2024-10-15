# SNMP MIB module (ZXR10-MPLS-L2VPN-STATIS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MPLS-L2VPN-STATIS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:58 2024
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

zxr10MplsL2vpnStatisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6)
)
zxr10MplsL2vpnStatisMIB.setRevisions(
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



# MIB Managed Objects in the order of their OIDs

_Zxr10L2vpnStatisObjects_ObjectIdentity = ObjectIdentity
zxr10L2vpnStatisObjects = _Zxr10L2vpnStatisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1)
)
_Zxr10L2vpnStatisTable_Object = MibTable
zxr10L2vpnStatisTable = _Zxr10L2vpnStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10L2vpnStatisTable.setStatus("current")
_Zxr10L2vpnStatisEntry_Object = MibTableRow
zxr10L2vpnStatisEntry = _Zxr10L2vpnStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1)
)
zxr10L2vpnStatisEntry.setIndexNames(
    (0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVCID"),
)
if mibBuilder.loadTexts:
    zxr10L2vpnStatisEntry.setStatus("current")
_Zxr10L2vpnStatisVCID_Type = Unsigned32
_Zxr10L2vpnStatisVCID_Object = MibTableColumn
zxr10L2vpnStatisVCID = _Zxr10L2vpnStatisVCID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 1),
    _Zxr10L2vpnStatisVCID_Type()
)
zxr10L2vpnStatisVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVCID.setStatus("current")


class _Zxr10L2vpnStatisVpnName_Type(DisplayString):
    """Custom type zxr10L2vpnStatisVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Zxr10L2vpnStatisVpnName_Type.__name__ = "DisplayString"
_Zxr10L2vpnStatisVpnName_Object = MibTableColumn
zxr10L2vpnStatisVpnName = _Zxr10L2vpnStatisVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 2),
    _Zxr10L2vpnStatisVpnName_Type()
)
zxr10L2vpnStatisVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVpnName.setStatus("current")
_Zxr10L2vpnStatisRecvPkts_Type = Counter64
_Zxr10L2vpnStatisRecvPkts_Object = MibTableColumn
zxr10L2vpnStatisRecvPkts = _Zxr10L2vpnStatisRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 3),
    _Zxr10L2vpnStatisRecvPkts_Type()
)
zxr10L2vpnStatisRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisRecvPkts.setStatus("current")
_Zxr10L2vpnStatisRecvBytes_Type = Counter64
_Zxr10L2vpnStatisRecvBytes_Object = MibTableColumn
zxr10L2vpnStatisRecvBytes = _Zxr10L2vpnStatisRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 4),
    _Zxr10L2vpnStatisRecvBytes_Type()
)
zxr10L2vpnStatisRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisRecvBytes.setStatus("current")
_Zxr10L2vpnStatisSndPkts_Type = Counter64
_Zxr10L2vpnStatisSndPkts_Object = MibTableColumn
zxr10L2vpnStatisSndPkts = _Zxr10L2vpnStatisSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 5),
    _Zxr10L2vpnStatisSndPkts_Type()
)
zxr10L2vpnStatisSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisSndPkts.setStatus("current")
_Zxr10L2vpnStatisSndBytes_Type = Counter64
_Zxr10L2vpnStatisSndBytes_Object = MibTableColumn
zxr10L2vpnStatisSndBytes = _Zxr10L2vpnStatisSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 6),
    _Zxr10L2vpnStatisSndBytes_Type()
)
zxr10L2vpnStatisSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisSndBytes.setStatus("current")
_Zxr10L2vpnStatisVcTable_Object = MibTable
zxr10L2vpnStatisVcTable = _Zxr10L2vpnStatisVcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcTable.setStatus("current")
_Zxr10L2vpnStatisVcEntry_Object = MibTableRow
zxr10L2vpnStatisVcEntry = _Zxr10L2vpnStatisVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1)
)
zxr10L2vpnStatisVcEntry.setIndexNames(
    (0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVcID"),
    (0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVcPeerAddr"),
)
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcEntry.setStatus("current")
_Zxr10L2vpnStatisVcID_Type = Unsigned32
_Zxr10L2vpnStatisVcID_Object = MibTableColumn
zxr10L2vpnStatisVcID = _Zxr10L2vpnStatisVcID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 1),
    _Zxr10L2vpnStatisVcID_Type()
)
zxr10L2vpnStatisVcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcID.setStatus("current")
_Zxr10L2vpnStatisVcPeerAddr_Type = IpAddress
_Zxr10L2vpnStatisVcPeerAddr_Object = MibTableColumn
zxr10L2vpnStatisVcPeerAddr = _Zxr10L2vpnStatisVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 2),
    _Zxr10L2vpnStatisVcPeerAddr_Type()
)
zxr10L2vpnStatisVcPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcPeerAddr.setStatus("current")
_Zxr10L2vpnStatisVcRecvPkts_Type = Counter64
_Zxr10L2vpnStatisVcRecvPkts_Object = MibTableColumn
zxr10L2vpnStatisVcRecvPkts = _Zxr10L2vpnStatisVcRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 3),
    _Zxr10L2vpnStatisVcRecvPkts_Type()
)
zxr10L2vpnStatisVcRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcRecvPkts.setStatus("current")
_Zxr10L2vpnStatisVcRecvBytes_Type = Counter64
_Zxr10L2vpnStatisVcRecvBytes_Object = MibTableColumn
zxr10L2vpnStatisVcRecvBytes = _Zxr10L2vpnStatisVcRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 4),
    _Zxr10L2vpnStatisVcRecvBytes_Type()
)
zxr10L2vpnStatisVcRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcRecvBytes.setStatus("current")
_Zxr10L2vpnStatisVcSndPkts_Type = Counter64
_Zxr10L2vpnStatisVcSndPkts_Object = MibTableColumn
zxr10L2vpnStatisVcSndPkts = _Zxr10L2vpnStatisVcSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 5),
    _Zxr10L2vpnStatisVcSndPkts_Type()
)
zxr10L2vpnStatisVcSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcSndPkts.setStatus("current")
_Zxr10L2vpnStatisVcSndBytes_Type = Counter64
_Zxr10L2vpnStatisVcSndBytes_Object = MibTableColumn
zxr10L2vpnStatisVcSndBytes = _Zxr10L2vpnStatisVcSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 6),
    _Zxr10L2vpnStatisVcSndBytes_Type()
)
zxr10L2vpnStatisVcSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L2vpnStatisVcSndBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MPLS-L2VPN-STATIS",
    **{"DisplayString": DisplayString,
       "InterfaceIndex": InterfaceIndex,
       "zxr10MplsL2vpnStatisMIB": zxr10MplsL2vpnStatisMIB,
       "zxr10L2vpnStatisObjects": zxr10L2vpnStatisObjects,
       "zxr10L2vpnStatisTable": zxr10L2vpnStatisTable,
       "zxr10L2vpnStatisEntry": zxr10L2vpnStatisEntry,
       "zxr10L2vpnStatisVCID": zxr10L2vpnStatisVCID,
       "zxr10L2vpnStatisVpnName": zxr10L2vpnStatisVpnName,
       "zxr10L2vpnStatisRecvPkts": zxr10L2vpnStatisRecvPkts,
       "zxr10L2vpnStatisRecvBytes": zxr10L2vpnStatisRecvBytes,
       "zxr10L2vpnStatisSndPkts": zxr10L2vpnStatisSndPkts,
       "zxr10L2vpnStatisSndBytes": zxr10L2vpnStatisSndBytes,
       "zxr10L2vpnStatisVcTable": zxr10L2vpnStatisVcTable,
       "zxr10L2vpnStatisVcEntry": zxr10L2vpnStatisVcEntry,
       "zxr10L2vpnStatisVcID": zxr10L2vpnStatisVcID,
       "zxr10L2vpnStatisVcPeerAddr": zxr10L2vpnStatisVcPeerAddr,
       "zxr10L2vpnStatisVcRecvPkts": zxr10L2vpnStatisVcRecvPkts,
       "zxr10L2vpnStatisVcRecvBytes": zxr10L2vpnStatisVcRecvBytes,
       "zxr10L2vpnStatisVcSndPkts": zxr10L2vpnStatisVcSndPkts,
       "zxr10L2vpnStatisVcSndBytes": zxr10L2vpnStatisVcSndBytes}
)
