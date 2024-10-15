# SNMP MIB module (ZYXEL-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:33 2024
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDhcpServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpServerSetup_ObjectIdentity = ObjectIdentity
zyxelDhcpServerSetup = _ZyxelDhcpServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1)
)
_ZyDhcpServerMaxNumberOfServers_Type = Integer32
_ZyDhcpServerMaxNumberOfServers_Object = MibScalar
zyDhcpServerMaxNumberOfServers = _ZyDhcpServerMaxNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 1),
    _ZyDhcpServerMaxNumberOfServers_Type()
)
zyDhcpServerMaxNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpServerMaxNumberOfServers.setStatus("current")
_ZyxelDhcpServerTable_Object = MibTable
zyxelDhcpServerTable = _ZyxelDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDhcpServerTable.setStatus("current")
_ZyxelDhcpServerEntry_Object = MibTableRow
zyxelDhcpServerEntry = _ZyxelDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1)
)
zyxelDhcpServerEntry.setIndexNames(
    (0, "ZYXEL-DHCP-SERVER-MIB", "zyDhcpServerVid"),
)
if mibBuilder.loadTexts:
    zyxelDhcpServerEntry.setStatus("current")
_ZyDhcpServerVid_Type = Integer32
_ZyDhcpServerVid_Object = MibTableColumn
zyDhcpServerVid = _ZyDhcpServerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 1),
    _ZyDhcpServerVid_Type()
)
zyDhcpServerVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpServerVid.setStatus("current")
_ZyDhcpServerStartIpAddress_Type = IpAddress
_ZyDhcpServerStartIpAddress_Object = MibTableColumn
zyDhcpServerStartIpAddress = _ZyDhcpServerStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 2),
    _ZyDhcpServerStartIpAddress_Type()
)
zyDhcpServerStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerStartIpAddress.setStatus("current")
_ZyDhcpServerPoolSize_Type = Integer32
_ZyDhcpServerPoolSize_Object = MibTableColumn
zyDhcpServerPoolSize = _ZyDhcpServerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 3),
    _ZyDhcpServerPoolSize_Type()
)
zyDhcpServerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerPoolSize.setStatus("current")
_ZyDhcpServerMask_Type = IpAddress
_ZyDhcpServerMask_Object = MibTableColumn
zyDhcpServerMask = _ZyDhcpServerMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 4),
    _ZyDhcpServerMask_Type()
)
zyDhcpServerMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerMask.setStatus("current")
_ZyDhcpServerGateway_Type = IpAddress
_ZyDhcpServerGateway_Object = MibTableColumn
zyDhcpServerGateway = _ZyDhcpServerGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 5),
    _ZyDhcpServerGateway_Type()
)
zyDhcpServerGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerGateway.setStatus("current")
_ZyDhcpServerPrimaryDNS_Type = IpAddress
_ZyDhcpServerPrimaryDNS_Object = MibTableColumn
zyDhcpServerPrimaryDNS = _ZyDhcpServerPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 6),
    _ZyDhcpServerPrimaryDNS_Type()
)
zyDhcpServerPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerPrimaryDNS.setStatus("current")
_ZyDhcpServerSecondaryDNS_Type = IpAddress
_ZyDhcpServerSecondaryDNS_Object = MibTableColumn
zyDhcpServerSecondaryDNS = _ZyDhcpServerSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 7),
    _ZyDhcpServerSecondaryDNS_Type()
)
zyDhcpServerSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpServerSecondaryDNS.setStatus("current")
_ZyDhcpServerRowStatus_Type = RowStatus
_ZyDhcpServerRowStatus_Object = MibTableColumn
zyDhcpServerRowStatus = _ZyDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 8),
    _ZyDhcpServerRowStatus_Type()
)
zyDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCP-SERVER-MIB",
    **{"zyxelDhcpServer": zyxelDhcpServer,
       "zyxelDhcpServerSetup": zyxelDhcpServerSetup,
       "zyDhcpServerMaxNumberOfServers": zyDhcpServerMaxNumberOfServers,
       "zyxelDhcpServerTable": zyxelDhcpServerTable,
       "zyxelDhcpServerEntry": zyxelDhcpServerEntry,
       "zyDhcpServerVid": zyDhcpServerVid,
       "zyDhcpServerStartIpAddress": zyDhcpServerStartIpAddress,
       "zyDhcpServerPoolSize": zyDhcpServerPoolSize,
       "zyDhcpServerMask": zyDhcpServerMask,
       "zyDhcpServerGateway": zyDhcpServerGateway,
       "zyDhcpServerPrimaryDNS": zyDhcpServerPrimaryDNS,
       "zyDhcpServerSecondaryDNS": zyDhcpServerSecondaryDNS,
       "zyDhcpServerRowStatus": zyDhcpServerRowStatus}
)
