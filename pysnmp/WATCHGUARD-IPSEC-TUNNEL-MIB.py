# SNMP MIB module (WATCHGUARD-IPSEC-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-IPSEC-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:35 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgIpsecTunnelMIB_ObjectIdentity = ObjectIdentity
wgIpsecTunnelMIB = _WgIpsecTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5)
)
if mibBuilder.loadTexts:
    wgIpsecTunnelMIB.setStatus("current")
_WgIpsecTunnel_ObjectIdentity = ObjectIdentity
wgIpsecTunnel = _WgIpsecTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1)
)
if mibBuilder.loadTexts:
    wgIpsecTunnel.setStatus("current")
_WgIpsecTunnelNum_Type = Unsigned32
_WgIpsecTunnelNum_Object = MibScalar
wgIpsecTunnelNum = _WgIpsecTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 1),
    _WgIpsecTunnelNum_Type()
)
wgIpsecTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelNum.setStatus("current")
_WgIpsecTunnelTable_Object = MibTable
wgIpsecTunnelTable = _WgIpsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    wgIpsecTunnelTable.setStatus("current")
_WgIpsecTunnelEntry_Object = MibTableRow
wgIpsecTunnelEntry = _WgIpsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1)
)
wgIpsecTunnelEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-TUNNEL-MIB", "wgIpsecTunnelID"),
)
if mibBuilder.loadTexts:
    wgIpsecTunnelEntry.setStatus("current")
_WgIpsecTunnelID_Type = Integer32
_WgIpsecTunnelID_Object = MibTableColumn
wgIpsecTunnelID = _WgIpsecTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 1),
    _WgIpsecTunnelID_Type()
)
wgIpsecTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelID.setStatus("current")
_WgIpsecTunnelLocalAddr_Type = IpAddress
_WgIpsecTunnelLocalAddr_Object = MibTableColumn
wgIpsecTunnelLocalAddr = _WgIpsecTunnelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 2),
    _WgIpsecTunnelLocalAddr_Type()
)
wgIpsecTunnelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelLocalAddr.setStatus("current")
_WgIpsecTunnelPeerAddr_Type = IpAddress
_WgIpsecTunnelPeerAddr_Object = MibTableColumn
wgIpsecTunnelPeerAddr = _WgIpsecTunnelPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 3),
    _WgIpsecTunnelPeerAddr_Type()
)
wgIpsecTunnelPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelPeerAddr.setStatus("current")
_WgIpsecTunnelInSpi_Type = Integer32
_WgIpsecTunnelInSpi_Object = MibTableColumn
wgIpsecTunnelInSpi = _WgIpsecTunnelInSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 4),
    _WgIpsecTunnelInSpi_Type()
)
wgIpsecTunnelInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInSpi.setStatus("current")
_WgIpsecTunnelOutSpi_Type = Integer32
_WgIpsecTunnelOutSpi_Object = MibTableColumn
wgIpsecTunnelOutSpi = _WgIpsecTunnelOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 5),
    _WgIpsecTunnelOutSpi_Type()
)
wgIpsecTunnelOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutSpi.setStatus("current")
_WgIpsecTunnelCreateTime_Type = DateAndTime
_WgIpsecTunnelCreateTime_Object = MibTableColumn
wgIpsecTunnelCreateTime = _WgIpsecTunnelCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 6),
    _WgIpsecTunnelCreateTime_Type()
)
wgIpsecTunnelCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelCreateTime.setStatus("current")
_WgIpsecTunnelDeviceID_Type = Unsigned32
_WgIpsecTunnelDeviceID_Object = MibTableColumn
wgIpsecTunnelDeviceID = _WgIpsecTunnelDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 7),
    _WgIpsecTunnelDeviceID_Type()
)
wgIpsecTunnelDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelDeviceID.setStatus("current")


class _WgIpsecTunnelEspEncryptAlg_Type(Integer32):
    """Custom type wgIpsecTunnelEspEncryptAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("three-des", 3),
          ("unknown", 0))
    )


_WgIpsecTunnelEspEncryptAlg_Type.__name__ = "Integer32"
_WgIpsecTunnelEspEncryptAlg_Object = MibTableColumn
wgIpsecTunnelEspEncryptAlg = _WgIpsecTunnelEspEncryptAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 8),
    _WgIpsecTunnelEspEncryptAlg_Type()
)
wgIpsecTunnelEspEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelEspEncryptAlg.setStatus("current")


class _WgIpsecTunnelEspAuthAlg_Type(Integer32):
    """Custom type wgIpsecTunnelEspAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha", 3),
          ("unknown", 0))
    )


_WgIpsecTunnelEspAuthAlg_Type.__name__ = "Integer32"
_WgIpsecTunnelEspAuthAlg_Object = MibTableColumn
wgIpsecTunnelEspAuthAlg = _WgIpsecTunnelEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 9),
    _WgIpsecTunnelEspAuthAlg_Type()
)
wgIpsecTunnelEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelEspAuthAlg.setStatus("current")


class _WgIpsecTunnelAhAuthAlg_Type(Integer32):
    """Custom type wgIpsecTunnelAhAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha", 3),
          ("unknown", 0))
    )


_WgIpsecTunnelAhAuthAlg_Type.__name__ = "Integer32"
_WgIpsecTunnelAhAuthAlg_Object = MibTableColumn
wgIpsecTunnelAhAuthAlg = _WgIpsecTunnelAhAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 10),
    _WgIpsecTunnelAhAuthAlg_Type()
)
wgIpsecTunnelAhAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelAhAuthAlg.setStatus("current")


class _WgIpsecTunnelMode_Type(Integer32):
    """Custom type wgIpsecTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1),
          ("unknown", 0))
    )


_WgIpsecTunnelMode_Type.__name__ = "Integer32"
_WgIpsecTunnelMode_Object = MibTableColumn
wgIpsecTunnelMode = _WgIpsecTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 11),
    _WgIpsecTunnelMode_Type()
)
wgIpsecTunnelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelMode.setStatus("current")


class _WgIpsecTunnelKeyMode_Type(Integer32):
    """Custom type wgIpsecTunnelKeyMode based on Integer32"""
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
        *(("auto-ike", 2),
          ("manual", 1),
          ("other", 3),
          ("unknown", 0))
    )


_WgIpsecTunnelKeyMode_Type.__name__ = "Integer32"
_WgIpsecTunnelKeyMode_Object = MibTableColumn
wgIpsecTunnelKeyMode = _WgIpsecTunnelKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 12),
    _WgIpsecTunnelKeyMode_Type()
)
wgIpsecTunnelKeyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelKeyMode.setStatus("current")
_WgIpsecTunnelLifeTime_Type = TimeTicks
_WgIpsecTunnelLifeTime_Object = MibTableColumn
wgIpsecTunnelLifeTime = _WgIpsecTunnelLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 13),
    _WgIpsecTunnelLifeTime_Type()
)
wgIpsecTunnelLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelLifeTime.setStatus("current")
_WgIpsecTunnelLifeLength_Type = Counter32
_WgIpsecTunnelLifeLength_Object = MibTableColumn
wgIpsecTunnelLifeLength = _WgIpsecTunnelLifeLength_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 14),
    _WgIpsecTunnelLifeLength_Type()
)
wgIpsecTunnelLifeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelLifeLength.setStatus("current")
_WgIpsecTunnelInSaBytes_Type = Counter32
_WgIpsecTunnelInSaBytes_Object = MibTableColumn
wgIpsecTunnelInSaBytes = _WgIpsecTunnelInSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 15),
    _WgIpsecTunnelInSaBytes_Type()
)
wgIpsecTunnelInSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInSaBytes.setStatus("current")
_WgIpsecTunnelOutSaBytes_Type = Counter32
_WgIpsecTunnelOutSaBytes_Object = MibTableColumn
wgIpsecTunnelOutSaBytes = _WgIpsecTunnelOutSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 16),
    _WgIpsecTunnelOutSaBytes_Type()
)
wgIpsecTunnelOutSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutSaBytes.setStatus("current")
_WgIpsecTunnelAccSecs_Type = Counter32
_WgIpsecTunnelAccSecs_Object = MibTableColumn
wgIpsecTunnelAccSecs = _WgIpsecTunnelAccSecs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 17),
    _WgIpsecTunnelAccSecs_Type()
)
wgIpsecTunnelAccSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelAccSecs.setStatus("current")


class _WgIpsecTunnelSelectorProtocol_Type(Integer32):
    """Custom type wgIpsecTunnelSelectorProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              29,
              41,
              43,
              44,
              46,
              47,
              50,
              51,
              58,
              59,
              60,
              92,
              98,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("any", 0),
          ("dstopts", 60),
          ("egp", 8),
          ("encap", 98),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("icmpv6", 58),
          ("idp", 22),
          ("igmp", 2),
          ("ipip", 4),
          ("ipv6", 41),
          ("ipv6-fragmentation", 44),
          ("ipv6-routing", 43),
          ("mtp", 92),
          ("none", 59),
          ("pim", 103),
          ("pup", 12),
          ("raw", 255),
          ("rsvp", 46),
          ("tcp", 6),
          ("tp", 29),
          ("udp", 17))
    )


_WgIpsecTunnelSelectorProtocol_Type.__name__ = "Integer32"
_WgIpsecTunnelSelectorProtocol_Object = MibTableColumn
wgIpsecTunnelSelectorProtocol = _WgIpsecTunnelSelectorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 18),
    _WgIpsecTunnelSelectorProtocol_Type()
)
wgIpsecTunnelSelectorProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorProtocol.setStatus("current")


class _WgIpsecTunnelSelectorRemoteIPType_Type(Integer32):
    """Custom type wgIpsecTunnelSelectorRemoteIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-addr-range", 3),
          ("ip-addr-single", 1),
          ("ip-addr-subnet", 2))
    )


_WgIpsecTunnelSelectorRemoteIPType_Type.__name__ = "Integer32"
_WgIpsecTunnelSelectorRemoteIPType_Object = MibTableColumn
wgIpsecTunnelSelectorRemoteIPType = _WgIpsecTunnelSelectorRemoteIPType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 19),
    _WgIpsecTunnelSelectorRemoteIPType_Type()
)
wgIpsecTunnelSelectorRemoteIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorRemoteIPType.setStatus("current")
_WgIpsecTunnelSelectorRemoteIPOne_Type = IpAddress
_WgIpsecTunnelSelectorRemoteIPOne_Object = MibTableColumn
wgIpsecTunnelSelectorRemoteIPOne = _WgIpsecTunnelSelectorRemoteIPOne_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 20),
    _WgIpsecTunnelSelectorRemoteIPOne_Type()
)
wgIpsecTunnelSelectorRemoteIPOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorRemoteIPOne.setStatus("current")
_WgIpsecTunnelSelectorRemoteIPTwo_Type = IpAddress
_WgIpsecTunnelSelectorRemoteIPTwo_Object = MibTableColumn
wgIpsecTunnelSelectorRemoteIPTwo = _WgIpsecTunnelSelectorRemoteIPTwo_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 21),
    _WgIpsecTunnelSelectorRemoteIPTwo_Type()
)
wgIpsecTunnelSelectorRemoteIPTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorRemoteIPTwo.setStatus("current")


class _WgIpsecTunnelSelectorRemotePort_Type(Integer32):
    """Custom type wgIpsecTunnelSelectorRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecTunnelSelectorRemotePort_Type.__name__ = "Integer32"
_WgIpsecTunnelSelectorRemotePort_Object = MibTableColumn
wgIpsecTunnelSelectorRemotePort = _WgIpsecTunnelSelectorRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 22),
    _WgIpsecTunnelSelectorRemotePort_Type()
)
wgIpsecTunnelSelectorRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorRemotePort.setStatus("current")


class _WgIpsecTunnelSelectorLocalIPType_Type(Integer32):
    """Custom type wgIpsecTunnelSelectorLocalIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-addr-range", 3),
          ("ip-addr-single", 1),
          ("ip-addr-subnet", 2))
    )


_WgIpsecTunnelSelectorLocalIPType_Type.__name__ = "Integer32"
_WgIpsecTunnelSelectorLocalIPType_Object = MibTableColumn
wgIpsecTunnelSelectorLocalIPType = _WgIpsecTunnelSelectorLocalIPType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 23),
    _WgIpsecTunnelSelectorLocalIPType_Type()
)
wgIpsecTunnelSelectorLocalIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorLocalIPType.setStatus("current")
_WgIpsecTunnelSelectorLocalIPOne_Type = IpAddress
_WgIpsecTunnelSelectorLocalIPOne_Object = MibTableColumn
wgIpsecTunnelSelectorLocalIPOne = _WgIpsecTunnelSelectorLocalIPOne_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 24),
    _WgIpsecTunnelSelectorLocalIPOne_Type()
)
wgIpsecTunnelSelectorLocalIPOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorLocalIPOne.setStatus("current")
_WgIpsecTunnelSelectorLocalIPTwo_Type = IpAddress
_WgIpsecTunnelSelectorLocalIPTwo_Object = MibTableColumn
wgIpsecTunnelSelectorLocalIPTwo = _WgIpsecTunnelSelectorLocalIPTwo_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 25),
    _WgIpsecTunnelSelectorLocalIPTwo_Type()
)
wgIpsecTunnelSelectorLocalIPTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorLocalIPTwo.setStatus("current")


class _WgIpsecTunnelSelectorLocalPort_Type(Integer32):
    """Custom type wgIpsecTunnelSelectorLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecTunnelSelectorLocalPort_Type.__name__ = "Integer32"
_WgIpsecTunnelSelectorLocalPort_Object = MibTableColumn
wgIpsecTunnelSelectorLocalPort = _WgIpsecTunnelSelectorLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 26),
    _WgIpsecTunnelSelectorLocalPort_Type()
)
wgIpsecTunnelSelectorLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelSelectorLocalPort.setStatus("current")
_WgIpsecTunnelNumRekey_Type = Counter32
_WgIpsecTunnelNumRekey_Object = MibTableColumn
wgIpsecTunnelNumRekey = _WgIpsecTunnelNumRekey_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 27),
    _WgIpsecTunnelNumRekey_Type()
)
wgIpsecTunnelNumRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelNumRekey.setStatus("current")
_WgIpsecTunnelInKbytes_Type = Counter32
_WgIpsecTunnelInKbytes_Object = MibTableColumn
wgIpsecTunnelInKbytes = _WgIpsecTunnelInKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 28),
    _WgIpsecTunnelInKbytes_Type()
)
wgIpsecTunnelInKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecTunnelInKbytes.setUnits("Kbytes")
_WgIpsecTunnelOutKbytes_Type = Counter32
_WgIpsecTunnelOutKbytes_Object = MibTableColumn
wgIpsecTunnelOutKbytes = _WgIpsecTunnelOutKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 29),
    _WgIpsecTunnelOutKbytes_Type()
)
wgIpsecTunnelOutKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutKbytes.setUnits("Kbytes")
_WgIpsecTunnelInPackets_Type = Counter32
_WgIpsecTunnelInPackets_Object = MibTableColumn
wgIpsecTunnelInPackets = _WgIpsecTunnelInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 30),
    _WgIpsecTunnelInPackets_Type()
)
wgIpsecTunnelInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInPackets.setStatus("current")
_WgIpsecTunnelOutPackets_Type = Counter32
_WgIpsecTunnelOutPackets_Object = MibTableColumn
wgIpsecTunnelOutPackets = _WgIpsecTunnelOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 31),
    _WgIpsecTunnelOutPackets_Type()
)
wgIpsecTunnelOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutPackets.setStatus("current")
_WgIpsecTunnelInDecryptErrors_Type = Counter32
_WgIpsecTunnelInDecryptErrors_Object = MibTableColumn
wgIpsecTunnelInDecryptErrors = _WgIpsecTunnelInDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 32),
    _WgIpsecTunnelInDecryptErrors_Type()
)
wgIpsecTunnelInDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInDecryptErrors.setStatus("current")
_WgIpsecTunnelInAuthErrors_Type = Counter32
_WgIpsecTunnelInAuthErrors_Object = MibTableColumn
wgIpsecTunnelInAuthErrors = _WgIpsecTunnelInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 33),
    _WgIpsecTunnelInAuthErrors_Type()
)
wgIpsecTunnelInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInAuthErrors.setStatus("current")
_WgIpsecTunnelInReplayErrors_Type = Counter32
_WgIpsecTunnelInReplayErrors_Object = MibTableColumn
wgIpsecTunnelInReplayErrors = _WgIpsecTunnelInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 34),
    _WgIpsecTunnelInReplayErrors_Type()
)
wgIpsecTunnelInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInReplayErrors.setStatus("current")
_WgIpsecTunnelInOtherErrors_Type = Counter32
_WgIpsecTunnelInOtherErrors_Object = MibTableColumn
wgIpsecTunnelInOtherErrors = _WgIpsecTunnelInOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 35),
    _WgIpsecTunnelInOtherErrors_Type()
)
wgIpsecTunnelInOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelInOtherErrors.setStatus("current")
_WgIpsecTunnelOutDecryptErrors_Type = Counter32
_WgIpsecTunnelOutDecryptErrors_Object = MibTableColumn
wgIpsecTunnelOutDecryptErrors = _WgIpsecTunnelOutDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 36),
    _WgIpsecTunnelOutDecryptErrors_Type()
)
wgIpsecTunnelOutDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutDecryptErrors.setStatus("current")
_WgIpsecTunnelOutAuthErrors_Type = Counter32
_WgIpsecTunnelOutAuthErrors_Object = MibTableColumn
wgIpsecTunnelOutAuthErrors = _WgIpsecTunnelOutAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 37),
    _WgIpsecTunnelOutAuthErrors_Type()
)
wgIpsecTunnelOutAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutAuthErrors.setStatus("current")
_WgIpsecTunnelOutReplayErrors_Type = Counter32
_WgIpsecTunnelOutReplayErrors_Object = MibTableColumn
wgIpsecTunnelOutReplayErrors = _WgIpsecTunnelOutReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 38),
    _WgIpsecTunnelOutReplayErrors_Type()
)
wgIpsecTunnelOutReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutReplayErrors.setStatus("current")
_WgIpsecTunnelOutOtherErrors_Type = Counter32
_WgIpsecTunnelOutOtherErrors_Object = MibTableColumn
wgIpsecTunnelOutOtherErrors = _WgIpsecTunnelOutOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 39),
    _WgIpsecTunnelOutOtherErrors_Type()
)
wgIpsecTunnelOutOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOutOtherErrors.setStatus("current")


class _WgIpsecTunnelUdpEncap_Type(Integer32):
    """Custom type wgIpsecTunnelUdpEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WgIpsecTunnelUdpEncap_Type.__name__ = "Integer32"
_WgIpsecTunnelUdpEncap_Object = MibTableColumn
wgIpsecTunnelUdpEncap = _WgIpsecTunnelUdpEncap_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 40),
    _WgIpsecTunnelUdpEncap_Type()
)
wgIpsecTunnelUdpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelUdpEncap.setStatus("current")


class _WgIpsecTunnelPeerUdpPort_Type(Integer32):
    """Custom type wgIpsecTunnelPeerUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecTunnelPeerUdpPort_Type.__name__ = "Integer32"
_WgIpsecTunnelPeerUdpPort_Object = MibTableColumn
wgIpsecTunnelPeerUdpPort = _WgIpsecTunnelPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 41),
    _WgIpsecTunnelPeerUdpPort_Type()
)
wgIpsecTunnelPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelPeerUdpPort.setStatus("current")
_WgIpsecTunnelOrigPeerAddr_Type = IpAddress
_WgIpsecTunnelOrigPeerAddr_Object = MibTableColumn
wgIpsecTunnelOrigPeerAddr = _WgIpsecTunnelOrigPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 5, 1, 2, 1, 42),
    _WgIpsecTunnelOrigPeerAddr_Type()
)
wgIpsecTunnelOrigPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecTunnelOrigPeerAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-IPSEC-TUNNEL-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgIpsecTunnelMIB": wgIpsecTunnelMIB,
       "wgIpsecTunnel": wgIpsecTunnel,
       "wgIpsecTunnelNum": wgIpsecTunnelNum,
       "wgIpsecTunnelTable": wgIpsecTunnelTable,
       "wgIpsecTunnelEntry": wgIpsecTunnelEntry,
       "wgIpsecTunnelID": wgIpsecTunnelID,
       "wgIpsecTunnelLocalAddr": wgIpsecTunnelLocalAddr,
       "wgIpsecTunnelPeerAddr": wgIpsecTunnelPeerAddr,
       "wgIpsecTunnelInSpi": wgIpsecTunnelInSpi,
       "wgIpsecTunnelOutSpi": wgIpsecTunnelOutSpi,
       "wgIpsecTunnelCreateTime": wgIpsecTunnelCreateTime,
       "wgIpsecTunnelDeviceID": wgIpsecTunnelDeviceID,
       "wgIpsecTunnelEspEncryptAlg": wgIpsecTunnelEspEncryptAlg,
       "wgIpsecTunnelEspAuthAlg": wgIpsecTunnelEspAuthAlg,
       "wgIpsecTunnelAhAuthAlg": wgIpsecTunnelAhAuthAlg,
       "wgIpsecTunnelMode": wgIpsecTunnelMode,
       "wgIpsecTunnelKeyMode": wgIpsecTunnelKeyMode,
       "wgIpsecTunnelLifeTime": wgIpsecTunnelLifeTime,
       "wgIpsecTunnelLifeLength": wgIpsecTunnelLifeLength,
       "wgIpsecTunnelInSaBytes": wgIpsecTunnelInSaBytes,
       "wgIpsecTunnelOutSaBytes": wgIpsecTunnelOutSaBytes,
       "wgIpsecTunnelAccSecs": wgIpsecTunnelAccSecs,
       "wgIpsecTunnelSelectorProtocol": wgIpsecTunnelSelectorProtocol,
       "wgIpsecTunnelSelectorRemoteIPType": wgIpsecTunnelSelectorRemoteIPType,
       "wgIpsecTunnelSelectorRemoteIPOne": wgIpsecTunnelSelectorRemoteIPOne,
       "wgIpsecTunnelSelectorRemoteIPTwo": wgIpsecTunnelSelectorRemoteIPTwo,
       "wgIpsecTunnelSelectorRemotePort": wgIpsecTunnelSelectorRemotePort,
       "wgIpsecTunnelSelectorLocalIPType": wgIpsecTunnelSelectorLocalIPType,
       "wgIpsecTunnelSelectorLocalIPOne": wgIpsecTunnelSelectorLocalIPOne,
       "wgIpsecTunnelSelectorLocalIPTwo": wgIpsecTunnelSelectorLocalIPTwo,
       "wgIpsecTunnelSelectorLocalPort": wgIpsecTunnelSelectorLocalPort,
       "wgIpsecTunnelNumRekey": wgIpsecTunnelNumRekey,
       "wgIpsecTunnelInKbytes": wgIpsecTunnelInKbytes,
       "wgIpsecTunnelOutKbytes": wgIpsecTunnelOutKbytes,
       "wgIpsecTunnelInPackets": wgIpsecTunnelInPackets,
       "wgIpsecTunnelOutPackets": wgIpsecTunnelOutPackets,
       "wgIpsecTunnelInDecryptErrors": wgIpsecTunnelInDecryptErrors,
       "wgIpsecTunnelInAuthErrors": wgIpsecTunnelInAuthErrors,
       "wgIpsecTunnelInReplayErrors": wgIpsecTunnelInReplayErrors,
       "wgIpsecTunnelInOtherErrors": wgIpsecTunnelInOtherErrors,
       "wgIpsecTunnelOutDecryptErrors": wgIpsecTunnelOutDecryptErrors,
       "wgIpsecTunnelOutAuthErrors": wgIpsecTunnelOutAuthErrors,
       "wgIpsecTunnelOutReplayErrors": wgIpsecTunnelOutReplayErrors,
       "wgIpsecTunnelOutOtherErrors": wgIpsecTunnelOutOtherErrors,
       "wgIpsecTunnelUdpEncap": wgIpsecTunnelUdpEncap,
       "wgIpsecTunnelPeerUdpPort": wgIpsecTunnelPeerUdpPort,
       "wgIpsecTunnelOrigPeerAddr": wgIpsecTunnelOrigPeerAddr}
)
