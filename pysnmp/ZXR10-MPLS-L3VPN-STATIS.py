# SNMP MIB module (ZXR10-MPLS-L3VPN-STATIS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MPLS-L3VPN-STATIS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:59 2024
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

(zxr10L3vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L3vpn")


# MODULE-IDENTITY

zxr10MplsL3vpnStatisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1)
)
zxr10MplsL3vpnStatisMIB.setRevisions(
        ("2005-09-26 00:00",)
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

_Zxr10L3vpnStatisObjects_ObjectIdentity = ObjectIdentity
zxr10L3vpnStatisObjects = _Zxr10L3vpnStatisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1)
)
_Zxr10L3vpnStatisTable_Object = MibTable
zxr10L3vpnStatisTable = _Zxr10L3vpnStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10L3vpnStatisTable.setStatus("current")
_Zxr10L3vpnStatisEntry_Object = MibTableRow
zxr10L3vpnStatisEntry = _Zxr10L3vpnStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1)
)
zxr10L3vpnStatisEntry.setIndexNames(
    (0, "ZXR10-MPLS-L3VPN-STATIS", "zxr10L3vpnStatisVpnID"),
)
if mibBuilder.loadTexts:
    zxr10L3vpnStatisEntry.setStatus("current")
_Zxr10L3vpnStatisVpnID_Type = Unsigned32
_Zxr10L3vpnStatisVpnID_Object = MibTableColumn
zxr10L3vpnStatisVpnID = _Zxr10L3vpnStatisVpnID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 1),
    _Zxr10L3vpnStatisVpnID_Type()
)
zxr10L3vpnStatisVpnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisVpnID.setStatus("current")


class _Zxr10L3vpnStatisVpnName_Type(DisplayString):
    """Custom type zxr10L3vpnStatisVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Zxr10L3vpnStatisVpnName_Type.__name__ = "DisplayString"
_Zxr10L3vpnStatisVpnName_Object = MibTableColumn
zxr10L3vpnStatisVpnName = _Zxr10L3vpnStatisVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 2),
    _Zxr10L3vpnStatisVpnName_Type()
)
zxr10L3vpnStatisVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisVpnName.setStatus("current")
_Zxr10L3vpnStatisRecvPkts_Type = Counter64
_Zxr10L3vpnStatisRecvPkts_Object = MibTableColumn
zxr10L3vpnStatisRecvPkts = _Zxr10L3vpnStatisRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 3),
    _Zxr10L3vpnStatisRecvPkts_Type()
)
zxr10L3vpnStatisRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisRecvPkts.setStatus("current")
_Zxr10L3vpnStatisRecvBytes_Type = Counter64
_Zxr10L3vpnStatisRecvBytes_Object = MibTableColumn
zxr10L3vpnStatisRecvBytes = _Zxr10L3vpnStatisRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 4),
    _Zxr10L3vpnStatisRecvBytes_Type()
)
zxr10L3vpnStatisRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisRecvBytes.setStatus("current")
_Zxr10L3vpnStatisSndPkts_Type = Counter64
_Zxr10L3vpnStatisSndPkts_Object = MibTableColumn
zxr10L3vpnStatisSndPkts = _Zxr10L3vpnStatisSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 5),
    _Zxr10L3vpnStatisSndPkts_Type()
)
zxr10L3vpnStatisSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisSndPkts.setStatus("current")
_Zxr10L3vpnStatisSndBytes_Type = Counter64
_Zxr10L3vpnStatisSndBytes_Object = MibTableColumn
zxr10L3vpnStatisSndBytes = _Zxr10L3vpnStatisSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 6),
    _Zxr10L3vpnStatisSndBytes_Type()
)
zxr10L3vpnStatisSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10L3vpnStatisSndBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MPLS-L3VPN-STATIS",
    **{"DisplayString": DisplayString,
       "InterfaceIndex": InterfaceIndex,
       "zxr10MplsL3vpnStatisMIB": zxr10MplsL3vpnStatisMIB,
       "zxr10L3vpnStatisObjects": zxr10L3vpnStatisObjects,
       "zxr10L3vpnStatisTable": zxr10L3vpnStatisTable,
       "zxr10L3vpnStatisEntry": zxr10L3vpnStatisEntry,
       "zxr10L3vpnStatisVpnID": zxr10L3vpnStatisVpnID,
       "zxr10L3vpnStatisVpnName": zxr10L3vpnStatisVpnName,
       "zxr10L3vpnStatisRecvPkts": zxr10L3vpnStatisRecvPkts,
       "zxr10L3vpnStatisRecvBytes": zxr10L3vpnStatisRecvBytes,
       "zxr10L3vpnStatisSndPkts": zxr10L3vpnStatisSndPkts,
       "zxr10L3vpnStatisSndBytes": zxr10L3vpnStatisSndBytes}
)
