# SNMP MIB module (NETSCREEN-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-IPPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:46 2024
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenIppoolMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 9)
)
netscreenIppoolMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2000-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnIpPool_ObjectIdentity = ObjectIdentity
nsVpnIpPool = _NsVpnIpPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9)
)
_NsVpnIpPoolTable_Object = MibTable
nsVpnIpPoolTable = _NsVpnIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1)
)
if mibBuilder.loadTexts:
    nsVpnIpPoolTable.setStatus("current")
_NsVpnIpPoolEntry_Object = MibTableRow
nsVpnIpPoolEntry = _NsVpnIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1)
)
nsVpnIpPoolEntry.setIndexNames(
    (0, "NETSCREEN-IPPOOL-MIB", "nsVpnIpPoolIndex"),
)
if mibBuilder.loadTexts:
    nsVpnIpPoolEntry.setStatus("current")


class _NsVpnIpPoolIndex_Type(Integer32):
    """Custom type nsVpnIpPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnIpPoolIndex_Type.__name__ = "Integer32"
_NsVpnIpPoolIndex_Object = MibTableColumn
nsVpnIpPoolIndex = _NsVpnIpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 1),
    _NsVpnIpPoolIndex_Type()
)
nsVpnIpPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolIndex.setStatus("current")


class _NsVpnIpPoolName_Type(DisplayString):
    """Custom type nsVpnIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIpPoolName_Type.__name__ = "DisplayString"
_NsVpnIpPoolName_Object = MibTableColumn
nsVpnIpPoolName = _NsVpnIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 2),
    _NsVpnIpPoolName_Type()
)
nsVpnIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolName.setStatus("current")
_NsVpnIpPoolStartIp_Type = IpAddress
_NsVpnIpPoolStartIp_Object = MibTableColumn
nsVpnIpPoolStartIp = _NsVpnIpPoolStartIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 3),
    _NsVpnIpPoolStartIp_Type()
)
nsVpnIpPoolStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolStartIp.setStatus("current")
_NsVpnIpPoolEndIp_Type = IpAddress
_NsVpnIpPoolEndIp_Object = MibTableColumn
nsVpnIpPoolEndIp = _NsVpnIpPoolEndIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 4),
    _NsVpnIpPoolEndIp_Type()
)
nsVpnIpPoolEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolEndIp.setStatus("current")
_NsVpnIpPoolIpUsed_Type = Integer32
_NsVpnIpPoolIpUsed_Object = MibTableColumn
nsVpnIpPoolIpUsed = _NsVpnIpPoolIpUsed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 5),
    _NsVpnIpPoolIpUsed_Type()
)
nsVpnIpPoolIpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIpPoolIpUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-IPPOOL-MIB",
    **{"netscreenIppoolMibModule": netscreenIppoolMibModule,
       "nsVpnIpPool": nsVpnIpPool,
       "nsVpnIpPoolTable": nsVpnIpPoolTable,
       "nsVpnIpPoolEntry": nsVpnIpPoolEntry,
       "nsVpnIpPoolIndex": nsVpnIpPoolIndex,
       "nsVpnIpPoolName": nsVpnIpPoolName,
       "nsVpnIpPoolStartIp": nsVpnIpPoolStartIp,
       "nsVpnIpPoolEndIp": nsVpnIpPoolEndIp,
       "nsVpnIpPoolIpUsed": nsVpnIpPoolIpUsed}
)
