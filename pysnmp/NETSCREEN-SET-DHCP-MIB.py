# SNMP MIB module (NETSCREEN-SET-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:54 2024
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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


# MODULE-IDENTITY

netscreenSetDhcpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 5)
)
netscreenSetDhcpMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-12-12 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetDHCP_ObjectIdentity = ObjectIdentity
nsSetDHCP = _NsSetDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5)
)
_NsSetDhcpTable_Object = MibTable
nsSetDhcpTable = _NsSetDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1)
)
if mibBuilder.loadTexts:
    nsSetDhcpTable.setStatus("current")
_NsSetDhcpEntry_Object = MibTableRow
nsSetDhcpEntry = _NsSetDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1)
)
nsSetDhcpEntry.setIndexNames(
    (0, "NETSCREEN-SET-DHCP-MIB", "nsSetDhcpIfIdx"),
)
if mibBuilder.loadTexts:
    nsSetDhcpEntry.setStatus("current")


class _NsSetDhcpIfIdx_Type(Integer32):
    """Custom type nsSetDhcpIfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSetDhcpIfIdx_Type.__name__ = "Integer32"
_NsSetDhcpIfIdx_Object = MibTableColumn
nsSetDhcpIfIdx = _NsSetDhcpIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 1),
    _NsSetDhcpIfIdx_Type()
)
nsSetDhcpIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetDhcpIfIdx.setStatus("current")


class _NsSetDHCPService_Type(Integer32):
    """Custom type nsSetDHCPService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-relay-agent", 1),
          ("dhcp-server", 2),
          ("none", 0))
    )


_NsSetDHCPService_Type.__name__ = "Integer32"
_NsSetDHCPService_Object = MibTableColumn
nsSetDHCPService = _NsSetDHCPService_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 2),
    _NsSetDHCPService_Type()
)
nsSetDHCPService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetDHCPService.setStatus("current")


class _NsSetDHCPRelayServer_Type(DisplayString):
    """Custom type nsSetDHCPRelayServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NsSetDHCPRelayServer_Type.__name__ = "DisplayString"
_NsSetDHCPRelayServer_Object = MibTableColumn
nsSetDHCPRelayServer = _NsSetDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 3),
    _NsSetDHCPRelayServer_Type()
)
nsSetDHCPRelayServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetDHCPRelayServer.setStatus("current")


class _NsSetDHCPVpnEncryp_Type(Integer32):
    """Custom type nsSetDHCPVpnEncryp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetDHCPVpnEncryp_Type.__name__ = "Integer32"
_NsSetDHCPVpnEncryp_Object = MibTableColumn
nsSetDHCPVpnEncryp = _NsSetDHCPVpnEncryp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 4),
    _NsSetDHCPVpnEncryp_Type()
)
nsSetDHCPVpnEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetDHCPVpnEncryp.setStatus("current")


class _NsSetDhcpIfInfo_Type(Integer32):
    """Custom type nsSetDhcpIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsSetDhcpIfInfo_Type.__name__ = "Integer32"
_NsSetDhcpIfInfo_Object = MibTableColumn
nsSetDhcpIfInfo = _NsSetDhcpIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 5),
    _NsSetDhcpIfInfo_Type()
)
nsSetDhcpIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetDhcpIfInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-DHCP-MIB",
    **{"netscreenSetDhcpMibModule": netscreenSetDhcpMibModule,
       "nsSetDHCP": nsSetDHCP,
       "nsSetDhcpTable": nsSetDhcpTable,
       "nsSetDhcpEntry": nsSetDhcpEntry,
       "nsSetDhcpIfIdx": nsSetDhcpIfIdx,
       "nsSetDHCPService": nsSetDHCPService,
       "nsSetDHCPRelayServer": nsSetDHCPRelayServer,
       "nsSetDHCPVpnEncryp": nsSetDHCPVpnEncryp,
       "nsSetDhcpIfInfo": nsSetDhcpIfInfo}
)
