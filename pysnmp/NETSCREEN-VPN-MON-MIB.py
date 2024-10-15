# SNMP MIB module (NETSCREEN-VPN-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:05 2024
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

netscreenVpnMonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 1)
)
netscreenVpnMonMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2000-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetscreenVpnMon_ObjectIdentity = ObjectIdentity
netscreenVpnMon = _NetscreenVpnMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1)
)
_NsVpnMonTable_Object = MibTable
nsVpnMonTable = _NsVpnMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nsVpnMonTable.setStatus("current")
_NsVpnMonEntry_Object = MibTableRow
nsVpnMonEntry = _NsVpnMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1)
)
nsVpnMonEntry.setIndexNames(
    (0, "NETSCREEN-VPN-MON-MIB", "nsVpnMonIndex"),
)
if mibBuilder.loadTexts:
    nsVpnMonEntry.setStatus("current")


class _NsVpnMonIndex_Type(Integer32):
    """Custom type nsVpnMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnMonIndex_Type.__name__ = "Integer32"
_NsVpnMonIndex_Object = MibTableColumn
nsVpnMonIndex = _NsVpnMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 1),
    _NsVpnMonIndex_Type()
)
nsVpnMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonIndex.setStatus("current")
_NsVpnMonInPlyId_Type = Integer32
_NsVpnMonInPlyId_Object = MibTableColumn
nsVpnMonInPlyId = _NsVpnMonInPlyId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 2),
    _NsVpnMonInPlyId_Type()
)
nsVpnMonInPlyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonInPlyId.setStatus("current")
_NsVpnMonOutPlyId_Type = Integer32
_NsVpnMonOutPlyId_Object = MibTableColumn
nsVpnMonOutPlyId = _NsVpnMonOutPlyId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 3),
    _NsVpnMonOutPlyId_Type()
)
nsVpnMonOutPlyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonOutPlyId.setStatus("current")


class _NsVpnMonVpnName_Type(DisplayString):
    """Custom type nsVpnMonVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnMonVpnName_Type.__name__ = "DisplayString"
_NsVpnMonVpnName_Object = MibTableColumn
nsVpnMonVpnName = _NsVpnMonVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 4),
    _NsVpnMonVpnName_Type()
)
nsVpnMonVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonVpnName.setStatus("current")


class _NsVpnMonVsysName_Type(DisplayString):
    """Custom type nsVpnMonVsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnMonVsysName_Type.__name__ = "DisplayString"
_NsVpnMonVsysName_Object = MibTableColumn
nsVpnMonVsysName = _NsVpnMonVsysName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 5),
    _NsVpnMonVsysName_Type()
)
nsVpnMonVsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonVsysName.setStatus("current")


class _NsVpnMonTunnelType_Type(Integer32):
    """Custom type nsVpnMonTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("proto-ipcomp", 4),
          ("proto-ipsec-ah", 2),
          ("proto-ipsec-esp", 3),
          ("proto-isakmp", 1),
          ("reserved", 0))
    )


_NsVpnMonTunnelType_Type.__name__ = "Integer32"
_NsVpnMonTunnelType_Object = MibTableColumn
nsVpnMonTunnelType = _NsVpnMonTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 6),
    _NsVpnMonTunnelType_Type()
)
nsVpnMonTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonTunnelType.setStatus("current")


class _NsVpnMonEspEncAlg_Type(Integer32):
    """Custom type nsVpnMonEspEncAlg based on Integer32"""
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
              10,
              11,
              12,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("esp-3des", 3),
          ("esp-3idea", 8),
          ("esp-aes", 12),
          ("esp-aes192", 20),
          ("esp-aes256", 21),
          ("esp-blowfish", 7),
          ("esp-cast", 6),
          ("esp-des", 2),
          ("esp-des-iv32", 9),
          ("esp-des-iv64", 1),
          ("esp-idea", 5),
          ("esp-null", 11),
          ("esp-rc4", 10),
          ("esp-rc5", 4),
          ("reserved", 0))
    )


_NsVpnMonEspEncAlg_Type.__name__ = "Integer32"
_NsVpnMonEspEncAlg_Object = MibTableColumn
nsVpnMonEspEncAlg = _NsVpnMonEspEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 7),
    _NsVpnMonEspEncAlg_Type()
)
nsVpnMonEspEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonEspEncAlg.setStatus("current")


class _NsVpnMonEspAuthAlg_Type(Integer32):
    """Custom type nsVpnMonEspAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("des-mac", 3),
          ("hmac-md5", 1),
          ("hmac-sha", 2),
          ("ipdk", 4),
          ("reserved", 0))
    )


_NsVpnMonEspAuthAlg_Type.__name__ = "Integer32"
_NsVpnMonEspAuthAlg_Object = MibTableColumn
nsVpnMonEspAuthAlg = _NsVpnMonEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 8),
    _NsVpnMonEspAuthAlg_Type()
)
nsVpnMonEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonEspAuthAlg.setStatus("current")


class _NsVpnMonAhAlg_Type(Integer32):
    """Custom type nsVpnMonAhAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ah-des", 4),
          ("ah-md5", 2),
          ("ah-sha", 3),
          ("reserved", 0))
    )


_NsVpnMonAhAlg_Type.__name__ = "Integer32"
_NsVpnMonAhAlg_Object = MibTableColumn
nsVpnMonAhAlg = _NsVpnMonAhAlg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 9),
    _NsVpnMonAhAlg_Type()
)
nsVpnMonAhAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonAhAlg.setStatus("current")


class _NsVpnMonKeyType_Type(Integer32):
    """Custom type nsVpnMonKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-ike", 1),
          ("manual", 0))
    )


_NsVpnMonKeyType_Type.__name__ = "Integer32"
_NsVpnMonKeyType_Object = MibTableColumn
nsVpnMonKeyType = _NsVpnMonKeyType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 10),
    _NsVpnMonKeyType_Type()
)
nsVpnMonKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonKeyType.setStatus("current")


class _NsVpnMonP1Auth_Type(Integer32):
    """Custom type nsVpnMonP1Auth based on Integer32"""
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
        *(("dss-Signature", 2),
          ("preshared-key", 1),
          ("rsa-Encryption1", 4),
          ("rsa-Encryption2", 5),
          ("rsa-Signature", 3),
          ("unused", 0))
    )


_NsVpnMonP1Auth_Type.__name__ = "Integer32"
_NsVpnMonP1Auth_Object = MibTableColumn
nsVpnMonP1Auth = _NsVpnMonP1Auth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 11),
    _NsVpnMonP1Auth_Type()
)
nsVpnMonP1Auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP1Auth.setStatus("current")


class _NsVpnMonVpnType_Type(Integer32):
    """Custom type nsVpnMonVpnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("reserved", 0),
          ("site-to-site", 2))
    )


_NsVpnMonVpnType_Type.__name__ = "Integer32"
_NsVpnMonVpnType_Object = MibTableColumn
nsVpnMonVpnType = _NsVpnMonVpnType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 12),
    _NsVpnMonVpnType_Type()
)
nsVpnMonVpnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonVpnType.setStatus("current")
_NsVpnMonRmtGwIp_Type = IpAddress
_NsVpnMonRmtGwIp_Object = MibTableColumn
nsVpnMonRmtGwIp = _NsVpnMonRmtGwIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 13),
    _NsVpnMonRmtGwIp_Type()
)
nsVpnMonRmtGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonRmtGwIp.setStatus("current")
_NsVpnMonRmtGwId_Type = DisplayString
_NsVpnMonRmtGwId_Object = MibTableColumn
nsVpnMonRmtGwId = _NsVpnMonRmtGwId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 14),
    _NsVpnMonRmtGwId_Type()
)
nsVpnMonRmtGwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonRmtGwId.setStatus("current")
_NsVpnMonMyGwIp_Type = IpAddress
_NsVpnMonMyGwIp_Object = MibTableColumn
nsVpnMonMyGwIp = _NsVpnMonMyGwIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 15),
    _NsVpnMonMyGwIp_Type()
)
nsVpnMonMyGwIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonMyGwIp.setStatus("current")
_NsVpnMonMyGwId_Type = DisplayString
_NsVpnMonMyGwId_Object = MibTableColumn
nsVpnMonMyGwId = _NsVpnMonMyGwId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 16),
    _NsVpnMonMyGwId_Type()
)
nsVpnMonMyGwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonMyGwId.setStatus("current")
_NsVpnMonOutSpi_Type = Integer32
_NsVpnMonOutSpi_Object = MibTableColumn
nsVpnMonOutSpi = _NsVpnMonOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 17),
    _NsVpnMonOutSpi_Type()
)
nsVpnMonOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonOutSpi.setStatus("current")
_NsVpnMonInSpi_Type = Integer32
_NsVpnMonInSpi_Object = MibTableColumn
nsVpnMonInSpi = _NsVpnMonInSpi_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 18),
    _NsVpnMonInSpi_Type()
)
nsVpnMonInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonInSpi.setStatus("current")


class _NsVpnMonMonState_Type(Integer32):
    """Custom type nsVpnMonMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsVpnMonMonState_Type.__name__ = "Integer32"
_NsVpnMonMonState_Object = MibTableColumn
nsVpnMonMonState = _NsVpnMonMonState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 19),
    _NsVpnMonMonState_Type()
)
nsVpnMonMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonMonState.setStatus("current")


class _NsVpnMonTunnelState_Type(Integer32):
    """Custom type nsVpnMonTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_NsVpnMonTunnelState_Type.__name__ = "Integer32"
_NsVpnMonTunnelState_Object = MibTableColumn
nsVpnMonTunnelState = _NsVpnMonTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 20),
    _NsVpnMonTunnelState_Type()
)
nsVpnMonTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonTunnelState.setStatus("current")


class _NsVpnMonP1State_Type(Integer32):
    """Custom type nsVpnMonP1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_NsVpnMonP1State_Type.__name__ = "Integer32"
_NsVpnMonP1State_Object = MibTableColumn
nsVpnMonP1State = _NsVpnMonP1State_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 21),
    _NsVpnMonP1State_Type()
)
nsVpnMonP1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP1State.setStatus("current")
_NsVpnMonP1LifeTime_Type = Integer32
_NsVpnMonP1LifeTime_Object = MibTableColumn
nsVpnMonP1LifeTime = _NsVpnMonP1LifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 22),
    _NsVpnMonP1LifeTime_Type()
)
nsVpnMonP1LifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP1LifeTime.setStatus("current")


class _NsVpnMonP2State_Type(Integer32):
    """Custom type nsVpnMonP2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_NsVpnMonP2State_Type.__name__ = "Integer32"
_NsVpnMonP2State_Object = MibTableColumn
nsVpnMonP2State = _NsVpnMonP2State_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 23),
    _NsVpnMonP2State_Type()
)
nsVpnMonP2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP2State.setStatus("current")
_NsVpnMonP2LifeTime_Type = Integer32
_NsVpnMonP2LifeTime_Object = MibTableColumn
nsVpnMonP2LifeTime = _NsVpnMonP2LifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 24),
    _NsVpnMonP2LifeTime_Type()
)
nsVpnMonP2LifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP2LifeTime.setStatus("current")
_NsVpnMonP2LifeBytes_Type = Integer32
_NsVpnMonP2LifeBytes_Object = MibTableColumn
nsVpnMonP2LifeBytes = _NsVpnMonP2LifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 25),
    _NsVpnMonP2LifeBytes_Type()
)
nsVpnMonP2LifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonP2LifeBytes.setStatus("current")
_NsVpnMonDelayAvg_Type = Integer32
_NsVpnMonDelayAvg_Object = MibTableColumn
nsVpnMonDelayAvg = _NsVpnMonDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 26),
    _NsVpnMonDelayAvg_Type()
)
nsVpnMonDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonDelayAvg.setStatus("current")
_NsVpnMonDelayLast_Type = Integer32
_NsVpnMonDelayLast_Object = MibTableColumn
nsVpnMonDelayLast = _NsVpnMonDelayLast_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 27),
    _NsVpnMonDelayLast_Type()
)
nsVpnMonDelayLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonDelayLast.setStatus("current")
_NsVpnMonAvail_Type = Integer32
_NsVpnMonAvail_Object = MibTableColumn
nsVpnMonAvail = _NsVpnMonAvail_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 28),
    _NsVpnMonAvail_Type()
)
nsVpnMonAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonAvail.setStatus("current")
_NsVpnMonSaId_Type = Integer32
_NsVpnMonSaId_Object = MibTableColumn
nsVpnMonSaId = _NsVpnMonSaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 29),
    _NsVpnMonSaId_Type()
)
nsVpnMonSaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonSaId.setStatus("current")
_NsVpnMonGroupId_Type = Integer32
_NsVpnMonGroupId_Object = MibTableColumn
nsVpnMonGroupId = _NsVpnMonGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 30),
    _NsVpnMonGroupId_Type()
)
nsVpnMonGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonGroupId.setStatus("current")
_NsVpnMonUsrId_Type = Integer32
_NsVpnMonUsrId_Object = MibTableColumn
nsVpnMonUsrId = _NsVpnMonUsrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 31),
    _NsVpnMonUsrId_Type()
)
nsVpnMonUsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonUsrId.setStatus("current")
_NsVpnMonStartSessRequestTime_Type = TimeTicks
_NsVpnMonStartSessRequestTime_Object = MibTableColumn
nsVpnMonStartSessRequestTime = _NsVpnMonStartSessRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 32),
    _NsVpnMonStartSessRequestTime_Type()
)
nsVpnMonStartSessRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonStartSessRequestTime.setStatus("current")
_NsVpnMonStartSessEstTime_Type = TimeTicks
_NsVpnMonStartSessEstTime_Object = MibTableColumn
nsVpnMonStartSessEstTime = _NsVpnMonStartSessEstTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 33),
    _NsVpnMonStartSessEstTime_Type()
)
nsVpnMonStartSessEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonStartSessEstTime.setStatus("current")
_NsVpnMonEndSessTime_Type = TimeTicks
_NsVpnMonEndSessTime_Object = MibTableColumn
nsVpnMonEndSessTime = _NsVpnMonEndSessTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 34),
    _NsVpnMonEndSessTime_Type()
)
nsVpnMonEndSessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonEndSessTime.setStatus("current")
_NsVpnMonBytesIn_Type = Counter32
_NsVpnMonBytesIn_Object = MibTableColumn
nsVpnMonBytesIn = _NsVpnMonBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 35),
    _NsVpnMonBytesIn_Type()
)
nsVpnMonBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonBytesIn.setStatus("current")
_NsVpnMonBytesOut_Type = Counter32
_NsVpnMonBytesOut_Object = MibTableColumn
nsVpnMonBytesOut = _NsVpnMonBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 36),
    _NsVpnMonBytesOut_Type()
)
nsVpnMonBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonBytesOut.setStatus("current")
_NsVpnMonPacketsIn_Type = Counter32
_NsVpnMonPacketsIn_Object = MibTableColumn
nsVpnMonPacketsIn = _NsVpnMonPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 37),
    _NsVpnMonPacketsIn_Type()
)
nsVpnMonPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonPacketsIn.setStatus("current")
_NsVpnMonPacketsOut_Type = Counter32
_NsVpnMonPacketsOut_Object = MibTableColumn
nsVpnMonPacketsOut = _NsVpnMonPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 38),
    _NsVpnMonPacketsOut_Type()
)
nsVpnMonPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonPacketsOut.setStatus("current")
_NsVpnMonIfIndex_Type = Integer32
_NsVpnMonIfIndex_Object = MibTableColumn
nsVpnMonIfIndex = _NsVpnMonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 39),
    _NsVpnMonIfIndex_Type()
)
nsVpnMonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonIfIndex.setStatus("current")
_NsVpnMonUpdateTime_Type = TimeTicks
_NsVpnMonUpdateTime_Object = MibTableColumn
nsVpnMonUpdateTime = _NsVpnMonUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 40),
    _NsVpnMonUpdateTime_Type()
)
nsVpnMonUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonUpdateTime.setStatus("current")


class _NsVpnMonDN_Type(DisplayString):
    """Custom type nsVpnMonDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsVpnMonDN_Type.__name__ = "DisplayString"
_NsVpnMonDN_Object = MibTableColumn
nsVpnMonDN = _NsVpnMonDN_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 41),
    _NsVpnMonDN_Type()
)
nsVpnMonDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonDN.setStatus("current")


class _NsVpnMonIfInfo_Type(Integer32):
    """Custom type nsVpnMonIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnMonIfInfo_Type.__name__ = "Integer32"
_NsVpnMonIfInfo_Object = MibTableColumn
nsVpnMonIfInfo = _NsVpnMonIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 1, 1, 1, 42),
    _NsVpnMonIfInfo_Type()
)
nsVpnMonIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnMonIfInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-MON-MIB",
    **{"netscreenVpnMonMibModule": netscreenVpnMonMibModule,
       "netscreenVpnMon": netscreenVpnMon,
       "nsVpnMonTable": nsVpnMonTable,
       "nsVpnMonEntry": nsVpnMonEntry,
       "nsVpnMonIndex": nsVpnMonIndex,
       "nsVpnMonInPlyId": nsVpnMonInPlyId,
       "nsVpnMonOutPlyId": nsVpnMonOutPlyId,
       "nsVpnMonVpnName": nsVpnMonVpnName,
       "nsVpnMonVsysName": nsVpnMonVsysName,
       "nsVpnMonTunnelType": nsVpnMonTunnelType,
       "nsVpnMonEspEncAlg": nsVpnMonEspEncAlg,
       "nsVpnMonEspAuthAlg": nsVpnMonEspAuthAlg,
       "nsVpnMonAhAlg": nsVpnMonAhAlg,
       "nsVpnMonKeyType": nsVpnMonKeyType,
       "nsVpnMonP1Auth": nsVpnMonP1Auth,
       "nsVpnMonVpnType": nsVpnMonVpnType,
       "nsVpnMonRmtGwIp": nsVpnMonRmtGwIp,
       "nsVpnMonRmtGwId": nsVpnMonRmtGwId,
       "nsVpnMonMyGwIp": nsVpnMonMyGwIp,
       "nsVpnMonMyGwId": nsVpnMonMyGwId,
       "nsVpnMonOutSpi": nsVpnMonOutSpi,
       "nsVpnMonInSpi": nsVpnMonInSpi,
       "nsVpnMonMonState": nsVpnMonMonState,
       "nsVpnMonTunnelState": nsVpnMonTunnelState,
       "nsVpnMonP1State": nsVpnMonP1State,
       "nsVpnMonP1LifeTime": nsVpnMonP1LifeTime,
       "nsVpnMonP2State": nsVpnMonP2State,
       "nsVpnMonP2LifeTime": nsVpnMonP2LifeTime,
       "nsVpnMonP2LifeBytes": nsVpnMonP2LifeBytes,
       "nsVpnMonDelayAvg": nsVpnMonDelayAvg,
       "nsVpnMonDelayLast": nsVpnMonDelayLast,
       "nsVpnMonAvail": nsVpnMonAvail,
       "nsVpnMonSaId": nsVpnMonSaId,
       "nsVpnMonGroupId": nsVpnMonGroupId,
       "nsVpnMonUsrId": nsVpnMonUsrId,
       "nsVpnMonStartSessRequestTime": nsVpnMonStartSessRequestTime,
       "nsVpnMonStartSessEstTime": nsVpnMonStartSessEstTime,
       "nsVpnMonEndSessTime": nsVpnMonEndSessTime,
       "nsVpnMonBytesIn": nsVpnMonBytesIn,
       "nsVpnMonBytesOut": nsVpnMonBytesOut,
       "nsVpnMonPacketsIn": nsVpnMonPacketsIn,
       "nsVpnMonPacketsOut": nsVpnMonPacketsOut,
       "nsVpnMonIfIndex": nsVpnMonIfIndex,
       "nsVpnMonUpdateTime": nsVpnMonUpdateTime,
       "nsVpnMonDN": nsVpnMonDN,
       "nsVpnMonIfInfo": nsVpnMonIfInfo}
)
