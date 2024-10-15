# SNMP MIB module (STN-ATM-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-ATM-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:03 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnRouterAtmVpn,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterAtmVpn")


# MODULE-IDENTITY

stnAtmVpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnAtmVpnTrunkObjects_ObjectIdentity = ObjectIdentity
stnAtmVpnTrunkObjects = _StnAtmVpnTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1)
)
_StnAtmVpnTrunkTable_Object = MibTable
stnAtmVpnTrunkTable = _StnAtmVpnTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnAtmVpnTrunkTable.setStatus("current")
_StnAtmVpnTrunkEntry_Object = MibTableRow
stnAtmVpnTrunkEntry = _StnAtmVpnTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1)
)
stnAtmVpnTrunkEntry.setIndexNames(
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmVpnTrunkEntry.setStatus("current")
_StnAtmVpnTrunkIfIndex_Type = InterfaceIndex
_StnAtmVpnTrunkIfIndex_Object = MibTableColumn
stnAtmVpnTrunkIfIndex = _StnAtmVpnTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 1),
    _StnAtmVpnTrunkIfIndex_Type()
)
stnAtmVpnTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkIfIndex.setStatus("current")
_StnAtmVpnTrunkViId_Type = Integer32
_StnAtmVpnTrunkViId_Object = MibTableColumn
stnAtmVpnTrunkViId = _StnAtmVpnTrunkViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 2),
    _StnAtmVpnTrunkViId_Type()
)
stnAtmVpnTrunkViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkViId.setStatus("current")


class _StnAtmVpnTrunkName_Type(DisplayString):
    """Custom type stnAtmVpnTrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnAtmVpnTrunkName_Type.__name__ = "DisplayString"
_StnAtmVpnTrunkName_Object = MibTableColumn
stnAtmVpnTrunkName = _StnAtmVpnTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 3),
    _StnAtmVpnTrunkName_Type()
)
stnAtmVpnTrunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkName.setStatus("current")


class _StnAtmVpnTrunkState_Type(Integer32):
    """Custom type stnAtmVpnTrunkState based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_StnAtmVpnTrunkState_Type.__name__ = "Integer32"
_StnAtmVpnTrunkState_Object = MibTableColumn
stnAtmVpnTrunkState = _StnAtmVpnTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 4),
    _StnAtmVpnTrunkState_Type()
)
stnAtmVpnTrunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkState.setStatus("current")
_StnAtmVpnTrunkLowerIfIndex_Type = InterfaceIndex
_StnAtmVpnTrunkLowerIfIndex_Object = MibTableColumn
stnAtmVpnTrunkLowerIfIndex = _StnAtmVpnTrunkLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 5),
    _StnAtmVpnTrunkLowerIfIndex_Type()
)
stnAtmVpnTrunkLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkLowerIfIndex.setStatus("current")
_StnAtmVpnTrunkVpnPaths_Type = Integer32
_StnAtmVpnTrunkVpnPaths_Object = MibTableColumn
stnAtmVpnTrunkVpnPaths = _StnAtmVpnTrunkVpnPaths_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 6),
    _StnAtmVpnTrunkVpnPaths_Type()
)
stnAtmVpnTrunkVpnPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkVpnPaths.setStatus("current")
_StnAtmVpnTrunkInUnknownVpnId_Type = Counter64
_StnAtmVpnTrunkInUnknownVpnId_Object = MibTableColumn
stnAtmVpnTrunkInUnknownVpnId = _StnAtmVpnTrunkInUnknownVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 7),
    _StnAtmVpnTrunkInUnknownVpnId_Type()
)
stnAtmVpnTrunkInUnknownVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkInUnknownVpnId.setStatus("current")
_StnAtmVpnTrunkInVpnIdIfaceInvalid_Type = Counter64
_StnAtmVpnTrunkInVpnIdIfaceInvalid_Object = MibTableColumn
stnAtmVpnTrunkInVpnIdIfaceInvalid = _StnAtmVpnTrunkInVpnIdIfaceInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 8),
    _StnAtmVpnTrunkInVpnIdIfaceInvalid_Type()
)
stnAtmVpnTrunkInVpnIdIfaceInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkInVpnIdIfaceInvalid.setStatus("current")
_StnAtmVpnTrunkOutUnknownVpnId_Type = Counter64
_StnAtmVpnTrunkOutUnknownVpnId_Object = MibTableColumn
stnAtmVpnTrunkOutUnknownVpnId = _StnAtmVpnTrunkOutUnknownVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 9),
    _StnAtmVpnTrunkOutUnknownVpnId_Type()
)
stnAtmVpnTrunkOutUnknownVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkOutUnknownVpnId.setStatus("current")
_StnAtmVpnTrunkOutVpnIdIfaceInvalid_Type = Counter64
_StnAtmVpnTrunkOutVpnIdIfaceInvalid_Object = MibTableColumn
stnAtmVpnTrunkOutVpnIdIfaceInvalid = _StnAtmVpnTrunkOutVpnIdIfaceInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 1, 1, 10),
    _StnAtmVpnTrunkOutVpnIdIfaceInvalid_Type()
)
stnAtmVpnTrunkOutVpnIdIfaceInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkOutVpnIdIfaceInvalid.setStatus("current")
_StnAtmVpnTrunkPathTable_Object = MibTable
stnAtmVpnTrunkPathTable = _StnAtmVpnTrunkPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathTable.setStatus("current")
_StnAtmVpnTrunkPathEntry_Object = MibTableRow
stnAtmVpnTrunkPathEntry = _StnAtmVpnTrunkPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1)
)
stnAtmVpnTrunkPathEntry.setIndexNames(
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathTrunkIfIndex"),
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnOUI"),
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnIndex"),
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnTrunkPathVpnSubIndex"),
)
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathEntry.setStatus("current")
_StnAtmVpnTrunkPathTrunkIfIndex_Type = InterfaceIndex
_StnAtmVpnTrunkPathTrunkIfIndex_Object = MibTableColumn
stnAtmVpnTrunkPathTrunkIfIndex = _StnAtmVpnTrunkPathTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 1),
    _StnAtmVpnTrunkPathTrunkIfIndex_Type()
)
stnAtmVpnTrunkPathTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathTrunkIfIndex.setStatus("current")
_StnAtmVpnTrunkPathVpnOUI_Type = Integer32
_StnAtmVpnTrunkPathVpnOUI_Object = MibTableColumn
stnAtmVpnTrunkPathVpnOUI = _StnAtmVpnTrunkPathVpnOUI_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 2),
    _StnAtmVpnTrunkPathVpnOUI_Type()
)
stnAtmVpnTrunkPathVpnOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathVpnOUI.setStatus("current")
_StnAtmVpnTrunkPathVpnIndex_Type = Integer32
_StnAtmVpnTrunkPathVpnIndex_Object = MibTableColumn
stnAtmVpnTrunkPathVpnIndex = _StnAtmVpnTrunkPathVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 3),
    _StnAtmVpnTrunkPathVpnIndex_Type()
)
stnAtmVpnTrunkPathVpnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathVpnIndex.setStatus("current")
_StnAtmVpnTrunkPathVpnSubIndex_Type = Integer32
_StnAtmVpnTrunkPathVpnSubIndex_Object = MibTableColumn
stnAtmVpnTrunkPathVpnSubIndex = _StnAtmVpnTrunkPathVpnSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 4),
    _StnAtmVpnTrunkPathVpnSubIndex_Type()
)
stnAtmVpnTrunkPathVpnSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathVpnSubIndex.setStatus("current")


class _StnAtmVpnTrunkPathType_Type(Integer32):
    """Custom type stnAtmVpnTrunkPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vpnLearnedPath", 1),
          ("vpnStaticPath", 2))
    )


_StnAtmVpnTrunkPathType_Type.__name__ = "Integer32"
_StnAtmVpnTrunkPathType_Object = MibTableColumn
stnAtmVpnTrunkPathType = _StnAtmVpnTrunkPathType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 5),
    _StnAtmVpnTrunkPathType_Type()
)
stnAtmVpnTrunkPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathType.setStatus("current")


class _StnAtmVpnTrunkPathNextIfType_Type(Integer32):
    """Custom type stnAtmVpnTrunkPathNextIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmVpnLink", 1),
          ("atmVpnTrunk", 2))
    )


_StnAtmVpnTrunkPathNextIfType_Type.__name__ = "Integer32"
_StnAtmVpnTrunkPathNextIfType_Object = MibTableColumn
stnAtmVpnTrunkPathNextIfType = _StnAtmVpnTrunkPathNextIfType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 6),
    _StnAtmVpnTrunkPathNextIfType_Type()
)
stnAtmVpnTrunkPathNextIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathNextIfType.setStatus("current")
_StnAtmVpnTrunkPathNextIfIndex_Type = InterfaceIndex
_StnAtmVpnTrunkPathNextIfIndex_Object = MibTableColumn
stnAtmVpnTrunkPathNextIfIndex = _StnAtmVpnTrunkPathNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 7),
    _StnAtmVpnTrunkPathNextIfIndex_Type()
)
stnAtmVpnTrunkPathNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathNextIfIndex.setStatus("current")
_StnAtmVpnTrunkPathInPackets_Type = Counter64
_StnAtmVpnTrunkPathInPackets_Object = MibTableColumn
stnAtmVpnTrunkPathInPackets = _StnAtmVpnTrunkPathInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 8),
    _StnAtmVpnTrunkPathInPackets_Type()
)
stnAtmVpnTrunkPathInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathInPackets.setStatus("current")
_StnAtmVpnTrunkPathInOctets_Type = Counter64
_StnAtmVpnTrunkPathInOctets_Object = MibTableColumn
stnAtmVpnTrunkPathInOctets = _StnAtmVpnTrunkPathInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 9),
    _StnAtmVpnTrunkPathInOctets_Type()
)
stnAtmVpnTrunkPathInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathInOctets.setStatus("current")
_StnAtmVpnTrunkPathOutPackets_Type = Counter64
_StnAtmVpnTrunkPathOutPackets_Object = MibTableColumn
stnAtmVpnTrunkPathOutPackets = _StnAtmVpnTrunkPathOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 10),
    _StnAtmVpnTrunkPathOutPackets_Type()
)
stnAtmVpnTrunkPathOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathOutPackets.setStatus("current")
_StnAtmVpnTrunkPathOutOctets_Type = Counter64
_StnAtmVpnTrunkPathOutOctets_Object = MibTableColumn
stnAtmVpnTrunkPathOutOctets = _StnAtmVpnTrunkPathOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 1, 2, 1, 11),
    _StnAtmVpnTrunkPathOutOctets_Type()
)
stnAtmVpnTrunkPathOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnTrunkPathOutOctets.setStatus("current")
_StnAtmVpnLinkObjects_ObjectIdentity = ObjectIdentity
stnAtmVpnLinkObjects = _StnAtmVpnLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2)
)
_StnAtmVpnLinkTable_Object = MibTable
stnAtmVpnLinkTable = _StnAtmVpnLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnAtmVpnLinkTable.setStatus("current")
_StnAtmVpnLinkEntry_Object = MibTableRow
stnAtmVpnLinkEntry = _StnAtmVpnLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1)
)
stnAtmVpnLinkEntry.setIndexNames(
    (0, "STN-ATM-VPN-MIB", "stnAtmVpnLinkIfIndex"),
)
if mibBuilder.loadTexts:
    stnAtmVpnLinkEntry.setStatus("current")
_StnAtmVpnLinkIfIndex_Type = InterfaceIndex
_StnAtmVpnLinkIfIndex_Object = MibTableColumn
stnAtmVpnLinkIfIndex = _StnAtmVpnLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 1),
    _StnAtmVpnLinkIfIndex_Type()
)
stnAtmVpnLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkIfIndex.setStatus("current")
_StnAtmVpnLinkViId_Type = Integer32
_StnAtmVpnLinkViId_Object = MibTableColumn
stnAtmVpnLinkViId = _StnAtmVpnLinkViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 2),
    _StnAtmVpnLinkViId_Type()
)
stnAtmVpnLinkViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkViId.setStatus("current")


class _StnAtmVpnLinkName_Type(DisplayString):
    """Custom type stnAtmVpnLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnAtmVpnLinkName_Type.__name__ = "DisplayString"
_StnAtmVpnLinkName_Object = MibTableColumn
stnAtmVpnLinkName = _StnAtmVpnLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 3),
    _StnAtmVpnLinkName_Type()
)
stnAtmVpnLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkName.setStatus("current")
_StnAtmVpnLinkVpnOUI_Type = Integer32
_StnAtmVpnLinkVpnOUI_Object = MibTableColumn
stnAtmVpnLinkVpnOUI = _StnAtmVpnLinkVpnOUI_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 4),
    _StnAtmVpnLinkVpnOUI_Type()
)
stnAtmVpnLinkVpnOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkVpnOUI.setStatus("current")
_StnAtmVpnLinkVpnIndex_Type = Integer32
_StnAtmVpnLinkVpnIndex_Object = MibTableColumn
stnAtmVpnLinkVpnIndex = _StnAtmVpnLinkVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 5),
    _StnAtmVpnLinkVpnIndex_Type()
)
stnAtmVpnLinkVpnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkVpnIndex.setStatus("current")
_StnAtmVpnLinkVpnSubIndex_Type = Integer32
_StnAtmVpnLinkVpnSubIndex_Object = MibTableColumn
stnAtmVpnLinkVpnSubIndex = _StnAtmVpnLinkVpnSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 6),
    _StnAtmVpnLinkVpnSubIndex_Type()
)
stnAtmVpnLinkVpnSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkVpnSubIndex.setStatus("current")


class _StnAtmVpnLinkState_Type(Integer32):
    """Custom type stnAtmVpnLinkState based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_StnAtmVpnLinkState_Type.__name__ = "Integer32"
_StnAtmVpnLinkState_Object = MibTableColumn
stnAtmVpnLinkState = _StnAtmVpnLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 7),
    _StnAtmVpnLinkState_Type()
)
stnAtmVpnLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkState.setStatus("current")
_StnAtmVpnLinkTrunkViId_Type = Integer32
_StnAtmVpnLinkTrunkViId_Object = MibTableColumn
stnAtmVpnLinkTrunkViId = _StnAtmVpnLinkTrunkViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 8),
    _StnAtmVpnLinkTrunkViId_Type()
)
stnAtmVpnLinkTrunkViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkTrunkViId.setStatus("current")
_StnAtmVpnLinkLowerIfIndex_Type = InterfaceIndex
_StnAtmVpnLinkLowerIfIndex_Object = MibTableColumn
stnAtmVpnLinkLowerIfIndex = _StnAtmVpnLinkLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 9),
    _StnAtmVpnLinkLowerIfIndex_Type()
)
stnAtmVpnLinkLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkLowerIfIndex.setStatus("current")
_StnAtmVpnLinkOutUnknownVpnId_Type = Counter64
_StnAtmVpnLinkOutUnknownVpnId_Object = MibTableColumn
stnAtmVpnLinkOutUnknownVpnId = _StnAtmVpnLinkOutUnknownVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 10),
    _StnAtmVpnLinkOutUnknownVpnId_Type()
)
stnAtmVpnLinkOutUnknownVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkOutUnknownVpnId.setStatus("current")
_StnAtmVpnLinkOutVpnIdIfaceInvalid_Type = Counter64
_StnAtmVpnLinkOutVpnIdIfaceInvalid_Object = MibTableColumn
stnAtmVpnLinkOutVpnIdIfaceInvalid = _StnAtmVpnLinkOutVpnIdIfaceInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 11),
    _StnAtmVpnLinkOutVpnIdIfaceInvalid_Type()
)
stnAtmVpnLinkOutVpnIdIfaceInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkOutVpnIdIfaceInvalid.setStatus("current")
_StnAtmVpnLinkInVpnIdIfaceInvalid_Type = Counter64
_StnAtmVpnLinkInVpnIdIfaceInvalid_Object = MibTableColumn
stnAtmVpnLinkInVpnIdIfaceInvalid = _StnAtmVpnLinkInVpnIdIfaceInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7, 1, 2, 1, 1, 12),
    _StnAtmVpnLinkInVpnIdIfaceInvalid_Type()
)
stnAtmVpnLinkInVpnIdIfaceInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAtmVpnLinkInVpnIdIfaceInvalid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-ATM-VPN-MIB",
    **{"stnAtmVpn": stnAtmVpn,
       "stnAtmVpnTrunkObjects": stnAtmVpnTrunkObjects,
       "stnAtmVpnTrunkTable": stnAtmVpnTrunkTable,
       "stnAtmVpnTrunkEntry": stnAtmVpnTrunkEntry,
       "stnAtmVpnTrunkIfIndex": stnAtmVpnTrunkIfIndex,
       "stnAtmVpnTrunkViId": stnAtmVpnTrunkViId,
       "stnAtmVpnTrunkName": stnAtmVpnTrunkName,
       "stnAtmVpnTrunkState": stnAtmVpnTrunkState,
       "stnAtmVpnTrunkLowerIfIndex": stnAtmVpnTrunkLowerIfIndex,
       "stnAtmVpnTrunkVpnPaths": stnAtmVpnTrunkVpnPaths,
       "stnAtmVpnTrunkInUnknownVpnId": stnAtmVpnTrunkInUnknownVpnId,
       "stnAtmVpnTrunkInVpnIdIfaceInvalid": stnAtmVpnTrunkInVpnIdIfaceInvalid,
       "stnAtmVpnTrunkOutUnknownVpnId": stnAtmVpnTrunkOutUnknownVpnId,
       "stnAtmVpnTrunkOutVpnIdIfaceInvalid": stnAtmVpnTrunkOutVpnIdIfaceInvalid,
       "stnAtmVpnTrunkPathTable": stnAtmVpnTrunkPathTable,
       "stnAtmVpnTrunkPathEntry": stnAtmVpnTrunkPathEntry,
       "stnAtmVpnTrunkPathTrunkIfIndex": stnAtmVpnTrunkPathTrunkIfIndex,
       "stnAtmVpnTrunkPathVpnOUI": stnAtmVpnTrunkPathVpnOUI,
       "stnAtmVpnTrunkPathVpnIndex": stnAtmVpnTrunkPathVpnIndex,
       "stnAtmVpnTrunkPathVpnSubIndex": stnAtmVpnTrunkPathVpnSubIndex,
       "stnAtmVpnTrunkPathType": stnAtmVpnTrunkPathType,
       "stnAtmVpnTrunkPathNextIfType": stnAtmVpnTrunkPathNextIfType,
       "stnAtmVpnTrunkPathNextIfIndex": stnAtmVpnTrunkPathNextIfIndex,
       "stnAtmVpnTrunkPathInPackets": stnAtmVpnTrunkPathInPackets,
       "stnAtmVpnTrunkPathInOctets": stnAtmVpnTrunkPathInOctets,
       "stnAtmVpnTrunkPathOutPackets": stnAtmVpnTrunkPathOutPackets,
       "stnAtmVpnTrunkPathOutOctets": stnAtmVpnTrunkPathOutOctets,
       "stnAtmVpnLinkObjects": stnAtmVpnLinkObjects,
       "stnAtmVpnLinkTable": stnAtmVpnLinkTable,
       "stnAtmVpnLinkEntry": stnAtmVpnLinkEntry,
       "stnAtmVpnLinkIfIndex": stnAtmVpnLinkIfIndex,
       "stnAtmVpnLinkViId": stnAtmVpnLinkViId,
       "stnAtmVpnLinkName": stnAtmVpnLinkName,
       "stnAtmVpnLinkVpnOUI": stnAtmVpnLinkVpnOUI,
       "stnAtmVpnLinkVpnIndex": stnAtmVpnLinkVpnIndex,
       "stnAtmVpnLinkVpnSubIndex": stnAtmVpnLinkVpnSubIndex,
       "stnAtmVpnLinkState": stnAtmVpnLinkState,
       "stnAtmVpnLinkTrunkViId": stnAtmVpnLinkTrunkViId,
       "stnAtmVpnLinkLowerIfIndex": stnAtmVpnLinkLowerIfIndex,
       "stnAtmVpnLinkOutUnknownVpnId": stnAtmVpnLinkOutUnknownVpnId,
       "stnAtmVpnLinkOutVpnIdIfaceInvalid": stnAtmVpnLinkOutVpnIdIfaceInvalid,
       "stnAtmVpnLinkInVpnIdIfaceInvalid": stnAtmVpnLinkInVpnIdIfaceInvalid}
)
