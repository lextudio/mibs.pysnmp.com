# SNMP MIB module (HP-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:08 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(tunnelIfAddressType,
 tunnelIfEntry,
 tunnelIfLocalInetAddress,
 tunnelIfRemoteInetAddress,
 tunnelInetConfigEntry) = mibBuilder.importSymbols(
    "TUNNEL-MIB",
    "tunnelIfAddressType",
    "tunnelIfEntry",
    "tunnelIfLocalInetAddress",
    "tunnelIfRemoteInetAddress",
    "tunnelInetConfigEntry")


# MODULE-IDENTITY

hpTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77)
)
hpTunnelMIB.setRevisions(
        ("2015-02-02 00:00",
         "2014-08-15 00:00",
         "2014-08-13 00:00",
         "2010-07-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpTunnelType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("direct4in4", 2),
          ("direct6in4", 3),
          ("direct6in4Ipsec", 4),
          ("direct6in6", 5),
          ("ipsecIpv4", 6),
          ("ipsecIpv6", 7),
          ("macinudp", 8),
          ("unspecified", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpTunnelNotifications_ObjectIdentity = ObjectIdentity
hpTunnelNotifications = _HpTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 0)
)
_HpTunnelObjects_ObjectIdentity = ObjectIdentity
hpTunnelObjects = _HpTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1)
)
_HpTunnelConfigTable_Object = MibTable
hpTunnelConfigTable = _HpTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1)
)
if mibBuilder.loadTexts:
    hpTunnelConfigTable.setStatus("current")
_HpTunnelConfigEntry_Object = MibTableRow
hpTunnelConfigEntry = _HpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1)
)
hpTunnelConfigEntry.setIndexNames(
    (0, "HP-TUNNEL-MIB", "hpTunnelID"),
)
if mibBuilder.loadTexts:
    hpTunnelConfigEntry.setStatus("current")


class _HpTunnelID_Type(Integer32):
    """Custom type hpTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpTunnelID_Type.__name__ = "Integer32"
_HpTunnelID_Object = MibTableColumn
hpTunnelID = _HpTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 1),
    _HpTunnelID_Type()
)
hpTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpTunnelID.setStatus("current")
_HpTunnelIfIndex_Type = InterfaceIndex
_HpTunnelIfIndex_Object = MibTableColumn
hpTunnelIfIndex = _HpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 2),
    _HpTunnelIfIndex_Type()
)
hpTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTunnelIfIndex.setStatus("deprecated")
_HpTunnelRowStatus_Type = RowStatus
_HpTunnelRowStatus_Object = MibTableColumn
hpTunnelRowStatus = _HpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 3),
    _HpTunnelRowStatus_Type()
)
hpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpTunnelRowStatus.setStatus("current")
_HpTunnelInterfaceIndex_Type = InterfaceIndex
_HpTunnelInterfaceIndex_Object = MibTableColumn
hpTunnelInterfaceIndex = _HpTunnelInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 1, 1, 4),
    _HpTunnelInterfaceIndex_Type()
)
hpTunnelInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpTunnelInterfaceIndex.setStatus("current")
_HpTunnelIfTable_Object = MibTable
hpTunnelIfTable = _HpTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2)
)
if mibBuilder.loadTexts:
    hpTunnelIfTable.setStatus("current")
_HpTunnelIfEntry_Object = MibTableRow
hpTunnelIfEntry = _HpTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpTunnelIfEntry.setStatus("current")


class _HpTunnelIfPMTU_Type(Integer32):
    """Custom type hpTunnelIfPMTU based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpTunnelIfPMTU_Type.__name__ = "Integer32"
_HpTunnelIfPMTU_Object = MibTableColumn
hpTunnelIfPMTU = _HpTunnelIfPMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 1),
    _HpTunnelIfPMTU_Type()
)
hpTunnelIfPMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelIfPMTU.setStatus("current")


class _HpTunnelIfNUD_Type(Integer32):
    """Custom type hpTunnelIfNUD based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpTunnelIfNUD_Type.__name__ = "Integer32"
_HpTunnelIfNUD_Object = MibTableColumn
hpTunnelIfNUD = _HpTunnelIfNUD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 2),
    _HpTunnelIfNUD_Type()
)
hpTunnelIfNUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelIfNUD.setStatus("current")


class _HpTunnelIfMTU_Type(Unsigned32):
    """Custom type hpTunnelIfMTU based on Unsigned32"""
    defaultValue = 1280


_HpTunnelIfMTU_Object = MibTableColumn
hpTunnelIfMTU = _HpTunnelIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 3),
    _HpTunnelIfMTU_Type()
)
hpTunnelIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelIfMTU.setStatus("current")
_HpTunnelEncapsMethod_Type = HpTunnelType
_HpTunnelEncapsMethod_Object = MibTableColumn
hpTunnelEncapsMethod = _HpTunnelEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 4),
    _HpTunnelEncapsMethod_Type()
)
hpTunnelEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelEncapsMethod.setStatus("current")


class _HpTunnelIpsecName_Type(SnmpAdminString):
    """Custom type hpTunnelIpsecName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpTunnelIpsecName_Type.__name__ = "SnmpAdminString"
_HpTunnelIpsecName_Object = MibTableColumn
hpTunnelIpsecName = _HpTunnelIpsecName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 2, 1, 5),
    _HpTunnelIpsecName_Type()
)
hpTunnelIpsecName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelIpsecName.setStatus("current")
_HpTunnelInetConfigTable_Object = MibTable
hpTunnelInetConfigTable = _HpTunnelInetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3)
)
if mibBuilder.loadTexts:
    hpTunnelInetConfigTable.setStatus("current")
_HpTunnelInetConfigEntry_Object = MibTableRow
hpTunnelInetConfigEntry = _HpTunnelInetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpTunnelInetConfigEntry.setStatus("current")
_HpTunnelInetConfigEncapsMethod_Type = HpTunnelType
_HpTunnelInetConfigEncapsMethod_Object = MibTableColumn
hpTunnelInetConfigEncapsMethod = _HpTunnelInetConfigEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 3, 1, 1),
    _HpTunnelInetConfigEncapsMethod_Type()
)
hpTunnelInetConfigEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelInetConfigEncapsMethod.setStatus("current")
_HpicfVlanTunnelMappingTable_Object = MibTable
hpicfVlanTunnelMappingTable = _HpicfVlanTunnelMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfVlanTunnelMappingTable.setStatus("current")
_HpicfVlanTunnelMappingEntry_Object = MibTableRow
hpicfVlanTunnelMappingEntry = _HpicfVlanTunnelMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1)
)
hpicfVlanTunnelMappingEntry.setIndexNames(
    (0, "HP-TUNNEL-MIB", "hpicfVLANIndex"),
    (0, "HP-TUNNEL-MIB", "hpicfTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfVlanTunnelMappingEntry.setStatus("current")
_HpicfVLANIndex_Type = VlanIndex
_HpicfVLANIndex_Object = MibTableColumn
hpicfVLANIndex = _HpicfVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 1),
    _HpicfVLANIndex_Type()
)
hpicfVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVLANIndex.setStatus("current")
_HpicfTunnelIfIndex_Type = InterfaceIndex
_HpicfTunnelIfIndex_Object = MibTableColumn
hpicfTunnelIfIndex = _HpicfTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 2),
    _HpicfTunnelIfIndex_Type()
)
hpicfTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTunnelIfIndex.setStatus("current")
_HpicfVlanTunnelMappingRowStatus_Type = RowStatus
_HpicfVlanTunnelMappingRowStatus_Object = MibTableColumn
hpicfVlanTunnelMappingRowStatus = _HpicfVlanTunnelMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 4, 1, 3),
    _HpicfVlanTunnelMappingRowStatus_Type()
)
hpicfVlanTunnelMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVlanTunnelMappingRowStatus.setStatus("current")
_HpicfUDPTunnelTypeTable_Object = MibTable
hpicfUDPTunnelTypeTable = _HpicfUDPTunnelTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfUDPTunnelTypeTable.setStatus("current")
_HpicfUDPTunnelTypeEntry_Object = MibTableRow
hpicfUDPTunnelTypeEntry = _HpicfUDPTunnelTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfUDPTunnelTypeEntry.setStatus("current")


class _HpicfUDPTunnelType_Type(Integer32):
    """Custom type hpicfUDPTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("remotemirror", 1),
          ("vxlan", 2))
    )


_HpicfUDPTunnelType_Type.__name__ = "Integer32"
_HpicfUDPTunnelType_Object = MibTableColumn
hpicfUDPTunnelType = _HpicfUDPTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 5, 1, 1),
    _HpicfUDPTunnelType_Type()
)
hpicfUDPTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUDPTunnelType.setStatus("current")
_HpTunnelNotifyScalars_ObjectIdentity = ObjectIdentity
hpTunnelNotifyScalars = _HpTunnelNotifyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6)
)
_HpTunnelMTUDropRouterAddrType_Type = InetAddressType
_HpTunnelMTUDropRouterAddrType_Object = MibScalar
hpTunnelMTUDropRouterAddrType = _HpTunnelMTUDropRouterAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 1),
    _HpTunnelMTUDropRouterAddrType_Type()
)
hpTunnelMTUDropRouterAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropRouterAddrType.setStatus("current")
_HpTunnelMTUDropRouterAddr_Type = InetAddress
_HpTunnelMTUDropRouterAddr_Object = MibScalar
hpTunnelMTUDropRouterAddr = _HpTunnelMTUDropRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 2),
    _HpTunnelMTUDropRouterAddr_Type()
)
hpTunnelMTUDropRouterAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropRouterAddr.setStatus("current")
_HpTunnelMTUDropRouterMTU_Type = Integer32
_HpTunnelMTUDropRouterMTU_Object = MibScalar
hpTunnelMTUDropRouterMTU = _HpTunnelMTUDropRouterMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 3),
    _HpTunnelMTUDropRouterMTU_Type()
)
hpTunnelMTUDropRouterMTU.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropRouterMTU.setStatus("current")
_HpTunnelMTUDropTunnelSrcAddrType_Type = InetAddressType
_HpTunnelMTUDropTunnelSrcAddrType_Object = MibScalar
hpTunnelMTUDropTunnelSrcAddrType = _HpTunnelMTUDropTunnelSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 4),
    _HpTunnelMTUDropTunnelSrcAddrType_Type()
)
hpTunnelMTUDropTunnelSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropTunnelSrcAddrType.setStatus("current")
_HpTunnelMTUDropTunnelSource_Type = InetAddress
_HpTunnelMTUDropTunnelSource_Object = MibScalar
hpTunnelMTUDropTunnelSource = _HpTunnelMTUDropTunnelSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 5),
    _HpTunnelMTUDropTunnelSource_Type()
)
hpTunnelMTUDropTunnelSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropTunnelSource.setStatus("current")
_HpTunnelMTUDropTunnelDstAddrType_Type = InetAddressType
_HpTunnelMTUDropTunnelDstAddrType_Object = MibScalar
hpTunnelMTUDropTunnelDstAddrType = _HpTunnelMTUDropTunnelDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 6),
    _HpTunnelMTUDropTunnelDstAddrType_Type()
)
hpTunnelMTUDropTunnelDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropTunnelDstAddrType.setStatus("current")
_HpTunnelMTUDropTunnelDest_Type = InetAddress
_HpTunnelMTUDropTunnelDest_Object = MibScalar
hpTunnelMTUDropTunnelDest = _HpTunnelMTUDropTunnelDest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 7),
    _HpTunnelMTUDropTunnelDest_Type()
)
hpTunnelMTUDropTunnelDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropTunnelDest.setStatus("current")
_HpTunnelMTUDropInIfIndex_Type = InterfaceIndex
_HpTunnelMTUDropInIfIndex_Object = MibScalar
hpTunnelMTUDropInIfIndex = _HpTunnelMTUDropInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 8),
    _HpTunnelMTUDropInIfIndex_Type()
)
hpTunnelMTUDropInIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpTunnelMTUDropInIfIndex.setStatus("current")


class _HpTunnelMTUDropNotifyEnable_Type(Integer32):
    """Custom type hpTunnelMTUDropNotifyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpTunnelMTUDropNotifyEnable_Type.__name__ = "Integer32"
_HpTunnelMTUDropNotifyEnable_Object = MibScalar
hpTunnelMTUDropNotifyEnable = _HpTunnelMTUDropNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 1, 6, 9),
    _HpTunnelMTUDropNotifyEnable_Type()
)
hpTunnelMTUDropNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTunnelMTUDropNotifyEnable.setStatus("current")
_HpTunnelConformance_ObjectIdentity = ObjectIdentity
hpTunnelConformance = _HpTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2)
)
_HpTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
hpTunnelMIBCompliances = _HpTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1)
)
_HpTunnelMIBGroups_ObjectIdentity = ObjectIdentity
hpTunnelMIBGroups = _HpTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2)
)
tunnelIfEntry.registerAugmentions(
    ("HP-TUNNEL-MIB",
     "hpTunnelIfEntry")
)
hpTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
tunnelInetConfigEntry.registerAugmentions(
    ("HP-TUNNEL-MIB",
     "hpTunnelInetConfigEntry")
)
hpTunnelInetConfigEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
tunnelInetConfigEntry.registerAugmentions(
    ("HP-TUNNEL-MIB",
     "hpicfUDPTunnelTypeEntry")
)
hpicfUDPTunnelTypeEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())

# Managed Objects groups

hpTunnelProvisionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 1)
)
hpTunnelProvisionGroup.setObjects(
      *(("HP-TUNNEL-MIB", "hpTunnelIfIndex"),
        ("HP-TUNNEL-MIB", "hpTunnelEncapsMethod"),
        ("HP-TUNNEL-MIB", "hpTunnelIfPMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelIfMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelIfNUD"),
        ("HP-TUNNEL-MIB", "hpTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    hpTunnelProvisionGroup.setStatus("deprecated")

hpTunnelInetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 2)
)
hpTunnelInetConfigGroup.setObjects(
      *(("HP-TUNNEL-MIB", "hpTunnelInetConfigEncapsMethod"),
        ("HP-TUNNEL-MIB", "hpTunnelIpsecName"),
        ("HP-TUNNEL-MIB", "hpicfUDPTunnelType"))
)
if mibBuilder.loadTexts:
    hpTunnelInetConfigGroup.setStatus("current")

hpVlanTunnelMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 3)
)
hpVlanTunnelMappingGroup.setObjects(
    ("HP-TUNNEL-MIB", "hpicfVlanTunnelMappingRowStatus")
)
if mibBuilder.loadTexts:
    hpVlanTunnelMappingGroup.setStatus("current")

hpTunnelProvisionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 4)
)
hpTunnelProvisionGroup2.setObjects(
      *(("HP-TUNNEL-MIB", "hpTunnelInterfaceIndex"),
        ("HP-TUNNEL-MIB", "hpTunnelEncapsMethod"),
        ("HP-TUNNEL-MIB", "hpTunnelIfPMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelIfMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelIfNUD"),
        ("HP-TUNNEL-MIB", "hpTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    hpTunnelProvisionGroup2.setStatus("current")

hpTunnelNotifyScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 5)
)
hpTunnelNotifyScalarsGroup.setObjects(
      *(("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddr"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSrcAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSource"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDstAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDest"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropInIfIndex"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpTunnelNotifyScalarsGroup.setStatus("current")


# Notification objects

hpTunnelIcmpErrorRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 0, 1)
)
hpTunnelIcmpErrorRcvd.setObjects(
      *(("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterAddr"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropRouterMTU"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSrcAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelSource"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDstAddrType"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropTunnelDest"),
        ("HP-TUNNEL-MIB", "hpTunnelMTUDropInIfIndex"),
        ("TUNNEL-MIB", "tunnelIfAddressType"),
        ("TUNNEL-MIB", "tunnelIfLocalInetAddress"),
        ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"))
)
if mibBuilder.loadTexts:
    hpTunnelIcmpErrorRcvd.setStatus(
        "current"
    )


# Notifications groups

hpTunnelNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 2, 6)
)
hpTunnelNotificationsGroup.setObjects(
    ("HP-TUNNEL-MIB", "hpTunnelIcmpErrorRcvd")
)
if mibBuilder.loadTexts:
    hpTunnelNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpTunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpTunnelMIBCompliance.setStatus(
        "deprecated"
    )

hpTunnelMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpTunnelMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-TUNNEL-MIB",
    **{"HpTunnelType": HpTunnelType,
       "hpTunnelMIB": hpTunnelMIB,
       "hpTunnelNotifications": hpTunnelNotifications,
       "hpTunnelIcmpErrorRcvd": hpTunnelIcmpErrorRcvd,
       "hpTunnelObjects": hpTunnelObjects,
       "hpTunnelConfigTable": hpTunnelConfigTable,
       "hpTunnelConfigEntry": hpTunnelConfigEntry,
       "hpTunnelID": hpTunnelID,
       "hpTunnelIfIndex": hpTunnelIfIndex,
       "hpTunnelRowStatus": hpTunnelRowStatus,
       "hpTunnelInterfaceIndex": hpTunnelInterfaceIndex,
       "hpTunnelIfTable": hpTunnelIfTable,
       "hpTunnelIfEntry": hpTunnelIfEntry,
       "hpTunnelIfPMTU": hpTunnelIfPMTU,
       "hpTunnelIfNUD": hpTunnelIfNUD,
       "hpTunnelIfMTU": hpTunnelIfMTU,
       "hpTunnelEncapsMethod": hpTunnelEncapsMethod,
       "hpTunnelIpsecName": hpTunnelIpsecName,
       "hpTunnelInetConfigTable": hpTunnelInetConfigTable,
       "hpTunnelInetConfigEntry": hpTunnelInetConfigEntry,
       "hpTunnelInetConfigEncapsMethod": hpTunnelInetConfigEncapsMethod,
       "hpicfVlanTunnelMappingTable": hpicfVlanTunnelMappingTable,
       "hpicfVlanTunnelMappingEntry": hpicfVlanTunnelMappingEntry,
       "hpicfVLANIndex": hpicfVLANIndex,
       "hpicfTunnelIfIndex": hpicfTunnelIfIndex,
       "hpicfVlanTunnelMappingRowStatus": hpicfVlanTunnelMappingRowStatus,
       "hpicfUDPTunnelTypeTable": hpicfUDPTunnelTypeTable,
       "hpicfUDPTunnelTypeEntry": hpicfUDPTunnelTypeEntry,
       "hpicfUDPTunnelType": hpicfUDPTunnelType,
       "hpTunnelNotifyScalars": hpTunnelNotifyScalars,
       "hpTunnelMTUDropRouterAddrType": hpTunnelMTUDropRouterAddrType,
       "hpTunnelMTUDropRouterAddr": hpTunnelMTUDropRouterAddr,
       "hpTunnelMTUDropRouterMTU": hpTunnelMTUDropRouterMTU,
       "hpTunnelMTUDropTunnelSrcAddrType": hpTunnelMTUDropTunnelSrcAddrType,
       "hpTunnelMTUDropTunnelSource": hpTunnelMTUDropTunnelSource,
       "hpTunnelMTUDropTunnelDstAddrType": hpTunnelMTUDropTunnelDstAddrType,
       "hpTunnelMTUDropTunnelDest": hpTunnelMTUDropTunnelDest,
       "hpTunnelMTUDropInIfIndex": hpTunnelMTUDropInIfIndex,
       "hpTunnelMTUDropNotifyEnable": hpTunnelMTUDropNotifyEnable,
       "hpTunnelConformance": hpTunnelConformance,
       "hpTunnelMIBCompliances": hpTunnelMIBCompliances,
       "hpTunnelMIBCompliance": hpTunnelMIBCompliance,
       "hpTunnelMIBCompliance2": hpTunnelMIBCompliance2,
       "hpTunnelMIBGroups": hpTunnelMIBGroups,
       "hpTunnelProvisionGroup": hpTunnelProvisionGroup,
       "hpTunnelInetConfigGroup": hpTunnelInetConfigGroup,
       "hpVlanTunnelMappingGroup": hpVlanTunnelMappingGroup,
       "hpTunnelProvisionGroup2": hpTunnelProvisionGroup2,
       "hpTunnelNotifyScalarsGroup": hpTunnelNotifyScalarsGroup,
       "hpTunnelNotificationsGroup": hpTunnelNotificationsGroup}
)
