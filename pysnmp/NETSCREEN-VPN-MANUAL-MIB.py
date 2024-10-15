# SNMP MIB module (NETSCREEN-VPN-MANUAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-MANUAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:04 2024
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

netscreenVpnManualMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 2)
)
netscreenVpnManualMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2002-05-21 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnManualKey_ObjectIdentity = ObjectIdentity
nsVpnManualKey = _NsVpnManualKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2)
)
_NsVpnManualKeyTable_Object = MibTable
nsVpnManualKeyTable = _NsVpnManualKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nsVpnManualKeyTable.setStatus("current")
_NsVpnManualKeyEntry_Object = MibTableRow
nsVpnManualKeyEntry = _NsVpnManualKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1)
)
nsVpnManualKeyEntry.setIndexNames(
    (0, "NETSCREEN-VPN-MANUAL-MIB", "nsVpnManualKeyIndex"),
)
if mibBuilder.loadTexts:
    nsVpnManualKeyEntry.setStatus("current")


class _NsVpnManualKeyIndex_Type(Integer32):
    """Custom type nsVpnManualKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnManualKeyIndex_Type.__name__ = "Integer32"
_NsVpnManualKeyIndex_Object = MibTableColumn
nsVpnManualKeyIndex = _NsVpnManualKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 1),
    _NsVpnManualKeyIndex_Type()
)
nsVpnManualKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyIndex.setStatus("current")


class _NsVpnManualKeyTunName_Type(DisplayString):
    """Custom type nsVpnManualKeyTunName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnManualKeyTunName_Type.__name__ = "DisplayString"
_NsVpnManualKeyTunName_Object = MibTableColumn
nsVpnManualKeyTunName = _NsVpnManualKeyTunName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 2),
    _NsVpnManualKeyTunName_Type()
)
nsVpnManualKeyTunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyTunName.setStatus("current")
_NsVpnManualKeyGW_Type = IpAddress
_NsVpnManualKeyGW_Object = MibTableColumn
nsVpnManualKeyGW = _NsVpnManualKeyGW_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 3),
    _NsVpnManualKeyGW_Type()
)
nsVpnManualKeyGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyGW.setStatus("current")
_NsVpnManualKeySILocal_Type = Integer32
_NsVpnManualKeySILocal_Object = MibTableColumn
nsVpnManualKeySILocal = _NsVpnManualKeySILocal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 4),
    _NsVpnManualKeySILocal_Type()
)
nsVpnManualKeySILocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeySILocal.setStatus("current")
_NsVpnManualKeySIRemote_Type = Integer32
_NsVpnManualKeySIRemote_Object = MibTableColumn
nsVpnManualKeySIRemote = _NsVpnManualKeySIRemote_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 5),
    _NsVpnManualKeySIRemote_Type()
)
nsVpnManualKeySIRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeySIRemote.setStatus("current")


class _NsVpnManualKeyTunnelType_Type(Integer32):
    """Custom type nsVpnManualKeyTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 0))
    )


_NsVpnManualKeyTunnelType_Type.__name__ = "Integer32"
_NsVpnManualKeyTunnelType_Object = MibTableColumn
nsVpnManualKeyTunnelType = _NsVpnManualKeyTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 6),
    _NsVpnManualKeyTunnelType_Type()
)
nsVpnManualKeyTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyTunnelType.setStatus("current")


class _NsVpnManualKeyEspEncAlg_Type(Integer32):
    """Custom type nsVpnManualKeyEspEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aes-192", 4),
          ("aes-256", 5),
          ("aes-cbc", 3),
          ("des-cbc", 1),
          ("null", 0),
          ("tripple-des-cbc", 2))
    )


_NsVpnManualKeyEspEncAlg_Type.__name__ = "Integer32"
_NsVpnManualKeyEspEncAlg_Object = MibTableColumn
nsVpnManualKeyEspEncAlg = _NsVpnManualKeyEspEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 7),
    _NsVpnManualKeyEspEncAlg_Type()
)
nsVpnManualKeyEspEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyEspEncAlg.setStatus("current")


class _NsVpnManualKeyEspAuthAlg_Type(Integer32):
    """Custom type nsVpnManualKeyEspAuthAlg based on Integer32"""
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
        *(("md5", 1),
          ("null", 0),
          ("sha", 2),
          ("sha256", 3))
    )


_NsVpnManualKeyEspAuthAlg_Type.__name__ = "Integer32"
_NsVpnManualKeyEspAuthAlg_Object = MibTableColumn
nsVpnManualKeyEspAuthAlg = _NsVpnManualKeyEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 8),
    _NsVpnManualKeyEspAuthAlg_Type()
)
nsVpnManualKeyEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyEspAuthAlg.setStatus("current")


class _NsVpnManualKeyAhHash_Type(Integer32):
    """Custom type nsVpnManualKeyAhHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("null", 0),
          ("sha", 2))
    )


_NsVpnManualKeyAhHash_Type.__name__ = "Integer32"
_NsVpnManualKeyAhHash_Object = MibTableColumn
nsVpnManualKeyAhHash = _NsVpnManualKeyAhHash_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 9),
    _NsVpnManualKeyAhHash_Type()
)
nsVpnManualKeyAhHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyAhHash.setStatus("current")


class _NsVpnManualKeyMonitorEnable_Type(Integer32):
    """Custom type nsVpnManualKeyMonitorEnable based on Integer32"""
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


_NsVpnManualKeyMonitorEnable_Type.__name__ = "Integer32"
_NsVpnManualKeyMonitorEnable_Object = MibTableColumn
nsVpnManualKeyMonitorEnable = _NsVpnManualKeyMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 10),
    _NsVpnManualKeyMonitorEnable_Type()
)
nsVpnManualKeyMonitorEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyMonitorEnable.setStatus("current")


class _NsVpnManualKeyTunToTrust_Type(Integer32):
    """Custom type nsVpnManualKeyTunToTrust based on Integer32"""
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


_NsVpnManualKeyTunToTrust_Type.__name__ = "Integer32"
_NsVpnManualKeyTunToTrust_Object = MibTableColumn
nsVpnManualKeyTunToTrust = _NsVpnManualKeyTunToTrust_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 11),
    _NsVpnManualKeyTunToTrust_Type()
)
nsVpnManualKeyTunToTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyTunToTrust.setStatus("current")
_NsVpnManualKeyVsys_Type = Integer32
_NsVpnManualKeyVsys_Object = MibTableColumn
nsVpnManualKeyVsys = _NsVpnManualKeyVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 2, 1, 1, 12),
    _NsVpnManualKeyVsys_Type()
)
nsVpnManualKeyVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnManualKeyVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-MANUAL-MIB",
    **{"netscreenVpnManualMibModule": netscreenVpnManualMibModule,
       "nsVpnManualKey": nsVpnManualKey,
       "nsVpnManualKeyTable": nsVpnManualKeyTable,
       "nsVpnManualKeyEntry": nsVpnManualKeyEntry,
       "nsVpnManualKeyIndex": nsVpnManualKeyIndex,
       "nsVpnManualKeyTunName": nsVpnManualKeyTunName,
       "nsVpnManualKeyGW": nsVpnManualKeyGW,
       "nsVpnManualKeySILocal": nsVpnManualKeySILocal,
       "nsVpnManualKeySIRemote": nsVpnManualKeySIRemote,
       "nsVpnManualKeyTunnelType": nsVpnManualKeyTunnelType,
       "nsVpnManualKeyEspEncAlg": nsVpnManualKeyEspEncAlg,
       "nsVpnManualKeyEspAuthAlg": nsVpnManualKeyEspAuthAlg,
       "nsVpnManualKeyAhHash": nsVpnManualKeyAhHash,
       "nsVpnManualKeyMonitorEnable": nsVpnManualKeyMonitorEnable,
       "nsVpnManualKeyTunToTrust": nsVpnManualKeyTunToTrust,
       "nsVpnManualKeyVsys": nsVpnManualKeyVsys}
)
