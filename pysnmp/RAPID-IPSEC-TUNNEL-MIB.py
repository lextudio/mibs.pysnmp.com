# SNMP MIB module (RAPID-IPSEC-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-IPSEC-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:39 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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


# MODULE-IDENTITY

rsInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6)
)
rsInfoModule.setRevisions(
        ("2001-04-20 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpsecTunnelMIB_ObjectIdentity = ObjectIdentity
rsIpsecTunnelMIB = _RsIpsecTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5)
)
if mibBuilder.loadTexts:
    rsIpsecTunnelMIB.setStatus("current")
_RsIpsecTunnel_ObjectIdentity = ObjectIdentity
rsIpsecTunnel = _RsIpsecTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1)
)
if mibBuilder.loadTexts:
    rsIpsecTunnel.setStatus("current")
_RsIpsecTunnelNum_Type = Unsigned32
_RsIpsecTunnelNum_Object = MibScalar
rsIpsecTunnelNum = _RsIpsecTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 1),
    _RsIpsecTunnelNum_Type()
)
rsIpsecTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelNum.setStatus("current")
_RsIpsecTunnelTable_Object = MibTable
rsIpsecTunnelTable = _RsIpsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    rsIpsecTunnelTable.setStatus("current")
_RsIpsecTunnelEntry_Object = MibTableRow
rsIpsecTunnelEntry = _RsIpsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1)
)
rsIpsecTunnelEntry.setIndexNames(
    (0, "RAPID-IPSEC-TUNNEL-MIB", "rsIpsecTunnelID"),
)
if mibBuilder.loadTexts:
    rsIpsecTunnelEntry.setStatus("current")
_RsIpsecTunnelID_Type = Integer32
_RsIpsecTunnelID_Object = MibTableColumn
rsIpsecTunnelID = _RsIpsecTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 1),
    _RsIpsecTunnelID_Type()
)
rsIpsecTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelID.setStatus("current")
_RsIpsecTunnelLocalAddr_Type = IpAddress
_RsIpsecTunnelLocalAddr_Object = MibTableColumn
rsIpsecTunnelLocalAddr = _RsIpsecTunnelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 2),
    _RsIpsecTunnelLocalAddr_Type()
)
rsIpsecTunnelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelLocalAddr.setStatus("current")
_RsIpsecTunnelPeerAddr_Type = IpAddress
_RsIpsecTunnelPeerAddr_Object = MibTableColumn
rsIpsecTunnelPeerAddr = _RsIpsecTunnelPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 3),
    _RsIpsecTunnelPeerAddr_Type()
)
rsIpsecTunnelPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelPeerAddr.setStatus("current")
_RsIpsecTunnelInSpi_Type = Integer32
_RsIpsecTunnelInSpi_Object = MibTableColumn
rsIpsecTunnelInSpi = _RsIpsecTunnelInSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 4),
    _RsIpsecTunnelInSpi_Type()
)
rsIpsecTunnelInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInSpi.setStatus("current")
_RsIpsecTunnelOutSpi_Type = Integer32
_RsIpsecTunnelOutSpi_Object = MibTableColumn
rsIpsecTunnelOutSpi = _RsIpsecTunnelOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 5),
    _RsIpsecTunnelOutSpi_Type()
)
rsIpsecTunnelOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutSpi.setStatus("current")
_RsIpsecTunnelCreateTime_Type = DateAndTime
_RsIpsecTunnelCreateTime_Object = MibTableColumn
rsIpsecTunnelCreateTime = _RsIpsecTunnelCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 6),
    _RsIpsecTunnelCreateTime_Type()
)
rsIpsecTunnelCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelCreateTime.setStatus("current")
_RsIpsecTunnelDeviceID_Type = Unsigned32
_RsIpsecTunnelDeviceID_Object = MibTableColumn
rsIpsecTunnelDeviceID = _RsIpsecTunnelDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 7),
    _RsIpsecTunnelDeviceID_Type()
)
rsIpsecTunnelDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelDeviceID.setStatus("current")


class _RsIpsecTunnelEspEncryptAlg_Type(Integer32):
    """Custom type rsIpsecTunnelEspEncryptAlg based on Integer32"""
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


_RsIpsecTunnelEspEncryptAlg_Type.__name__ = "Integer32"
_RsIpsecTunnelEspEncryptAlg_Object = MibTableColumn
rsIpsecTunnelEspEncryptAlg = _RsIpsecTunnelEspEncryptAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 8),
    _RsIpsecTunnelEspEncryptAlg_Type()
)
rsIpsecTunnelEspEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelEspEncryptAlg.setStatus("current")


class _RsIpsecTunnelEspAuthAlg_Type(Integer32):
    """Custom type rsIpsecTunnelEspAuthAlg based on Integer32"""
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


_RsIpsecTunnelEspAuthAlg_Type.__name__ = "Integer32"
_RsIpsecTunnelEspAuthAlg_Object = MibTableColumn
rsIpsecTunnelEspAuthAlg = _RsIpsecTunnelEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 9),
    _RsIpsecTunnelEspAuthAlg_Type()
)
rsIpsecTunnelEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelEspAuthAlg.setStatus("current")


class _RsIpsecTunnelAhAuthAlg_Type(Integer32):
    """Custom type rsIpsecTunnelAhAuthAlg based on Integer32"""
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


_RsIpsecTunnelAhAuthAlg_Type.__name__ = "Integer32"
_RsIpsecTunnelAhAuthAlg_Object = MibTableColumn
rsIpsecTunnelAhAuthAlg = _RsIpsecTunnelAhAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 10),
    _RsIpsecTunnelAhAuthAlg_Type()
)
rsIpsecTunnelAhAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelAhAuthAlg.setStatus("current")


class _RsIpsecTunnelMode_Type(Integer32):
    """Custom type rsIpsecTunnelMode based on Integer32"""
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


_RsIpsecTunnelMode_Type.__name__ = "Integer32"
_RsIpsecTunnelMode_Object = MibTableColumn
rsIpsecTunnelMode = _RsIpsecTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 11),
    _RsIpsecTunnelMode_Type()
)
rsIpsecTunnelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelMode.setStatus("current")


class _RsIpsecTunnelKeyMode_Type(Integer32):
    """Custom type rsIpsecTunnelKeyMode based on Integer32"""
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


_RsIpsecTunnelKeyMode_Type.__name__ = "Integer32"
_RsIpsecTunnelKeyMode_Object = MibTableColumn
rsIpsecTunnelKeyMode = _RsIpsecTunnelKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 12),
    _RsIpsecTunnelKeyMode_Type()
)
rsIpsecTunnelKeyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelKeyMode.setStatus("current")
_RsIpsecTunnelLifeTime_Type = TimeTicks
_RsIpsecTunnelLifeTime_Object = MibTableColumn
rsIpsecTunnelLifeTime = _RsIpsecTunnelLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 13),
    _RsIpsecTunnelLifeTime_Type()
)
rsIpsecTunnelLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelLifeTime.setStatus("current")
_RsIpsecTunnelLifeLength_Type = Counter32
_RsIpsecTunnelLifeLength_Object = MibTableColumn
rsIpsecTunnelLifeLength = _RsIpsecTunnelLifeLength_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 14),
    _RsIpsecTunnelLifeLength_Type()
)
rsIpsecTunnelLifeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelLifeLength.setStatus("current")
_RsIpsecTunnelInSaBytes_Type = Counter32
_RsIpsecTunnelInSaBytes_Object = MibTableColumn
rsIpsecTunnelInSaBytes = _RsIpsecTunnelInSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 15),
    _RsIpsecTunnelInSaBytes_Type()
)
rsIpsecTunnelInSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInSaBytes.setStatus("current")
_RsIpsecTunnelOutSaBytes_Type = Counter32
_RsIpsecTunnelOutSaBytes_Object = MibTableColumn
rsIpsecTunnelOutSaBytes = _RsIpsecTunnelOutSaBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 16),
    _RsIpsecTunnelOutSaBytes_Type()
)
rsIpsecTunnelOutSaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutSaBytes.setStatus("current")
_RsIpsecTunnelAccSecs_Type = Counter32
_RsIpsecTunnelAccSecs_Object = MibTableColumn
rsIpsecTunnelAccSecs = _RsIpsecTunnelAccSecs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 17),
    _RsIpsecTunnelAccSecs_Type()
)
rsIpsecTunnelAccSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelAccSecs.setStatus("current")


class _RsIpsecTunnelSelectorProtocol_Type(Integer32):
    """Custom type rsIpsecTunnelSelectorProtocol based on Integer32"""
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


_RsIpsecTunnelSelectorProtocol_Type.__name__ = "Integer32"
_RsIpsecTunnelSelectorProtocol_Object = MibTableColumn
rsIpsecTunnelSelectorProtocol = _RsIpsecTunnelSelectorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 18),
    _RsIpsecTunnelSelectorProtocol_Type()
)
rsIpsecTunnelSelectorProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorProtocol.setStatus("current")


class _RsIpsecTunnelSelectorRemoteIPType_Type(Integer32):
    """Custom type rsIpsecTunnelSelectorRemoteIPType based on Integer32"""
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


_RsIpsecTunnelSelectorRemoteIPType_Type.__name__ = "Integer32"
_RsIpsecTunnelSelectorRemoteIPType_Object = MibTableColumn
rsIpsecTunnelSelectorRemoteIPType = _RsIpsecTunnelSelectorRemoteIPType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 19),
    _RsIpsecTunnelSelectorRemoteIPType_Type()
)
rsIpsecTunnelSelectorRemoteIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorRemoteIPType.setStatus("current")
_RsIpsecTunnelSelectorRemoteIPOne_Type = IpAddress
_RsIpsecTunnelSelectorRemoteIPOne_Object = MibTableColumn
rsIpsecTunnelSelectorRemoteIPOne = _RsIpsecTunnelSelectorRemoteIPOne_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 20),
    _RsIpsecTunnelSelectorRemoteIPOne_Type()
)
rsIpsecTunnelSelectorRemoteIPOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorRemoteIPOne.setStatus("current")
_RsIpsecTunnelSelectorRemoteIPTwo_Type = IpAddress
_RsIpsecTunnelSelectorRemoteIPTwo_Object = MibTableColumn
rsIpsecTunnelSelectorRemoteIPTwo = _RsIpsecTunnelSelectorRemoteIPTwo_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 21),
    _RsIpsecTunnelSelectorRemoteIPTwo_Type()
)
rsIpsecTunnelSelectorRemoteIPTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorRemoteIPTwo.setStatus("current")


class _RsIpsecTunnelSelectorRemotePort_Type(Integer32):
    """Custom type rsIpsecTunnelSelectorRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecTunnelSelectorRemotePort_Type.__name__ = "Integer32"
_RsIpsecTunnelSelectorRemotePort_Object = MibTableColumn
rsIpsecTunnelSelectorRemotePort = _RsIpsecTunnelSelectorRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 22),
    _RsIpsecTunnelSelectorRemotePort_Type()
)
rsIpsecTunnelSelectorRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorRemotePort.setStatus("current")


class _RsIpsecTunnelSelectorLocalIPType_Type(Integer32):
    """Custom type rsIpsecTunnelSelectorLocalIPType based on Integer32"""
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


_RsIpsecTunnelSelectorLocalIPType_Type.__name__ = "Integer32"
_RsIpsecTunnelSelectorLocalIPType_Object = MibTableColumn
rsIpsecTunnelSelectorLocalIPType = _RsIpsecTunnelSelectorLocalIPType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 23),
    _RsIpsecTunnelSelectorLocalIPType_Type()
)
rsIpsecTunnelSelectorLocalIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorLocalIPType.setStatus("current")
_RsIpsecTunnelSelectorLocalIPOne_Type = IpAddress
_RsIpsecTunnelSelectorLocalIPOne_Object = MibTableColumn
rsIpsecTunnelSelectorLocalIPOne = _RsIpsecTunnelSelectorLocalIPOne_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 24),
    _RsIpsecTunnelSelectorLocalIPOne_Type()
)
rsIpsecTunnelSelectorLocalIPOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorLocalIPOne.setStatus("current")
_RsIpsecTunnelSelectorLocalIPTwo_Type = IpAddress
_RsIpsecTunnelSelectorLocalIPTwo_Object = MibTableColumn
rsIpsecTunnelSelectorLocalIPTwo = _RsIpsecTunnelSelectorLocalIPTwo_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 25),
    _RsIpsecTunnelSelectorLocalIPTwo_Type()
)
rsIpsecTunnelSelectorLocalIPTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorLocalIPTwo.setStatus("current")


class _RsIpsecTunnelSelectorLocalPort_Type(Integer32):
    """Custom type rsIpsecTunnelSelectorLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecTunnelSelectorLocalPort_Type.__name__ = "Integer32"
_RsIpsecTunnelSelectorLocalPort_Object = MibTableColumn
rsIpsecTunnelSelectorLocalPort = _RsIpsecTunnelSelectorLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 26),
    _RsIpsecTunnelSelectorLocalPort_Type()
)
rsIpsecTunnelSelectorLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelSelectorLocalPort.setStatus("current")
_RsIpsecTunnelNumRekey_Type = Counter32
_RsIpsecTunnelNumRekey_Object = MibTableColumn
rsIpsecTunnelNumRekey = _RsIpsecTunnelNumRekey_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 27),
    _RsIpsecTunnelNumRekey_Type()
)
rsIpsecTunnelNumRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelNumRekey.setStatus("current")
_RsIpsecTunnelInKbytes_Type = Counter32
_RsIpsecTunnelInKbytes_Object = MibTableColumn
rsIpsecTunnelInKbytes = _RsIpsecTunnelInKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 28),
    _RsIpsecTunnelInKbytes_Type()
)
rsIpsecTunnelInKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecTunnelInKbytes.setUnits("Kbytes")
_RsIpsecTunnelOutKbytes_Type = Counter32
_RsIpsecTunnelOutKbytes_Object = MibTableColumn
rsIpsecTunnelOutKbytes = _RsIpsecTunnelOutKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 29),
    _RsIpsecTunnelOutKbytes_Type()
)
rsIpsecTunnelOutKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutKbytes.setUnits("Kbytes")
_RsIpsecTunnelInPackets_Type = Counter32
_RsIpsecTunnelInPackets_Object = MibTableColumn
rsIpsecTunnelInPackets = _RsIpsecTunnelInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 30),
    _RsIpsecTunnelInPackets_Type()
)
rsIpsecTunnelInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInPackets.setStatus("current")
_RsIpsecTunnelOutPackets_Type = Counter32
_RsIpsecTunnelOutPackets_Object = MibTableColumn
rsIpsecTunnelOutPackets = _RsIpsecTunnelOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 31),
    _RsIpsecTunnelOutPackets_Type()
)
rsIpsecTunnelOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutPackets.setStatus("current")
_RsIpsecTunnelInDecryptErrors_Type = Counter32
_RsIpsecTunnelInDecryptErrors_Object = MibTableColumn
rsIpsecTunnelInDecryptErrors = _RsIpsecTunnelInDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 32),
    _RsIpsecTunnelInDecryptErrors_Type()
)
rsIpsecTunnelInDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInDecryptErrors.setStatus("current")
_RsIpsecTunnelInAuthErrors_Type = Counter32
_RsIpsecTunnelInAuthErrors_Object = MibTableColumn
rsIpsecTunnelInAuthErrors = _RsIpsecTunnelInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 33),
    _RsIpsecTunnelInAuthErrors_Type()
)
rsIpsecTunnelInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInAuthErrors.setStatus("current")
_RsIpsecTunnelInReplayErrors_Type = Counter32
_RsIpsecTunnelInReplayErrors_Object = MibTableColumn
rsIpsecTunnelInReplayErrors = _RsIpsecTunnelInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 34),
    _RsIpsecTunnelInReplayErrors_Type()
)
rsIpsecTunnelInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInReplayErrors.setStatus("current")
_RsIpsecTunnelInOtherErrors_Type = Counter32
_RsIpsecTunnelInOtherErrors_Object = MibTableColumn
rsIpsecTunnelInOtherErrors = _RsIpsecTunnelInOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 35),
    _RsIpsecTunnelInOtherErrors_Type()
)
rsIpsecTunnelInOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelInOtherErrors.setStatus("current")
_RsIpsecTunnelOutDecryptErrors_Type = Counter32
_RsIpsecTunnelOutDecryptErrors_Object = MibTableColumn
rsIpsecTunnelOutDecryptErrors = _RsIpsecTunnelOutDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 36),
    _RsIpsecTunnelOutDecryptErrors_Type()
)
rsIpsecTunnelOutDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutDecryptErrors.setStatus("current")
_RsIpsecTunnelOutAuthErrors_Type = Counter32
_RsIpsecTunnelOutAuthErrors_Object = MibTableColumn
rsIpsecTunnelOutAuthErrors = _RsIpsecTunnelOutAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 37),
    _RsIpsecTunnelOutAuthErrors_Type()
)
rsIpsecTunnelOutAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutAuthErrors.setStatus("current")
_RsIpsecTunnelOutReplayErrors_Type = Counter32
_RsIpsecTunnelOutReplayErrors_Object = MibTableColumn
rsIpsecTunnelOutReplayErrors = _RsIpsecTunnelOutReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 38),
    _RsIpsecTunnelOutReplayErrors_Type()
)
rsIpsecTunnelOutReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutReplayErrors.setStatus("current")
_RsIpsecTunnelOutOtherErrors_Type = Counter32
_RsIpsecTunnelOutOtherErrors_Object = MibTableColumn
rsIpsecTunnelOutOtherErrors = _RsIpsecTunnelOutOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 39),
    _RsIpsecTunnelOutOtherErrors_Type()
)
rsIpsecTunnelOutOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOutOtherErrors.setStatus("current")


class _RsIpsecTunnelUdpEncap_Type(Integer32):
    """Custom type rsIpsecTunnelUdpEncap based on Integer32"""
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


_RsIpsecTunnelUdpEncap_Type.__name__ = "Integer32"
_RsIpsecTunnelUdpEncap_Object = MibTableColumn
rsIpsecTunnelUdpEncap = _RsIpsecTunnelUdpEncap_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 40),
    _RsIpsecTunnelUdpEncap_Type()
)
rsIpsecTunnelUdpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelUdpEncap.setStatus("current")


class _RsIpsecTunnelPeerUdpPort_Type(Integer32):
    """Custom type rsIpsecTunnelPeerUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecTunnelPeerUdpPort_Type.__name__ = "Integer32"
_RsIpsecTunnelPeerUdpPort_Object = MibTableColumn
rsIpsecTunnelPeerUdpPort = _RsIpsecTunnelPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 41),
    _RsIpsecTunnelPeerUdpPort_Type()
)
rsIpsecTunnelPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelPeerUdpPort.setStatus("current")
_RsIpsecTunnelOrigPeerAddr_Type = IpAddress
_RsIpsecTunnelOrigPeerAddr_Object = MibTableColumn
rsIpsecTunnelOrigPeerAddr = _RsIpsecTunnelOrigPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 42),
    _RsIpsecTunnelOrigPeerAddr_Type()
)
rsIpsecTunnelOrigPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecTunnelOrigPeerAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-IPSEC-TUNNEL-MIB",
    **{"rsInfoModule": rsInfoModule,
       "rsIpsecTunnelMIB": rsIpsecTunnelMIB,
       "rsIpsecTunnel": rsIpsecTunnel,
       "rsIpsecTunnelNum": rsIpsecTunnelNum,
       "rsIpsecTunnelTable": rsIpsecTunnelTable,
       "rsIpsecTunnelEntry": rsIpsecTunnelEntry,
       "rsIpsecTunnelID": rsIpsecTunnelID,
       "rsIpsecTunnelLocalAddr": rsIpsecTunnelLocalAddr,
       "rsIpsecTunnelPeerAddr": rsIpsecTunnelPeerAddr,
       "rsIpsecTunnelInSpi": rsIpsecTunnelInSpi,
       "rsIpsecTunnelOutSpi": rsIpsecTunnelOutSpi,
       "rsIpsecTunnelCreateTime": rsIpsecTunnelCreateTime,
       "rsIpsecTunnelDeviceID": rsIpsecTunnelDeviceID,
       "rsIpsecTunnelEspEncryptAlg": rsIpsecTunnelEspEncryptAlg,
       "rsIpsecTunnelEspAuthAlg": rsIpsecTunnelEspAuthAlg,
       "rsIpsecTunnelAhAuthAlg": rsIpsecTunnelAhAuthAlg,
       "rsIpsecTunnelMode": rsIpsecTunnelMode,
       "rsIpsecTunnelKeyMode": rsIpsecTunnelKeyMode,
       "rsIpsecTunnelLifeTime": rsIpsecTunnelLifeTime,
       "rsIpsecTunnelLifeLength": rsIpsecTunnelLifeLength,
       "rsIpsecTunnelInSaBytes": rsIpsecTunnelInSaBytes,
       "rsIpsecTunnelOutSaBytes": rsIpsecTunnelOutSaBytes,
       "rsIpsecTunnelAccSecs": rsIpsecTunnelAccSecs,
       "rsIpsecTunnelSelectorProtocol": rsIpsecTunnelSelectorProtocol,
       "rsIpsecTunnelSelectorRemoteIPType": rsIpsecTunnelSelectorRemoteIPType,
       "rsIpsecTunnelSelectorRemoteIPOne": rsIpsecTunnelSelectorRemoteIPOne,
       "rsIpsecTunnelSelectorRemoteIPTwo": rsIpsecTunnelSelectorRemoteIPTwo,
       "rsIpsecTunnelSelectorRemotePort": rsIpsecTunnelSelectorRemotePort,
       "rsIpsecTunnelSelectorLocalIPType": rsIpsecTunnelSelectorLocalIPType,
       "rsIpsecTunnelSelectorLocalIPOne": rsIpsecTunnelSelectorLocalIPOne,
       "rsIpsecTunnelSelectorLocalIPTwo": rsIpsecTunnelSelectorLocalIPTwo,
       "rsIpsecTunnelSelectorLocalPort": rsIpsecTunnelSelectorLocalPort,
       "rsIpsecTunnelNumRekey": rsIpsecTunnelNumRekey,
       "rsIpsecTunnelInKbytes": rsIpsecTunnelInKbytes,
       "rsIpsecTunnelOutKbytes": rsIpsecTunnelOutKbytes,
       "rsIpsecTunnelInPackets": rsIpsecTunnelInPackets,
       "rsIpsecTunnelOutPackets": rsIpsecTunnelOutPackets,
       "rsIpsecTunnelInDecryptErrors": rsIpsecTunnelInDecryptErrors,
       "rsIpsecTunnelInAuthErrors": rsIpsecTunnelInAuthErrors,
       "rsIpsecTunnelInReplayErrors": rsIpsecTunnelInReplayErrors,
       "rsIpsecTunnelInOtherErrors": rsIpsecTunnelInOtherErrors,
       "rsIpsecTunnelOutDecryptErrors": rsIpsecTunnelOutDecryptErrors,
       "rsIpsecTunnelOutAuthErrors": rsIpsecTunnelOutAuthErrors,
       "rsIpsecTunnelOutReplayErrors": rsIpsecTunnelOutReplayErrors,
       "rsIpsecTunnelOutOtherErrors": rsIpsecTunnelOutOtherErrors,
       "rsIpsecTunnelUdpEncap": rsIpsecTunnelUdpEncap,
       "rsIpsecTunnelPeerUdpPort": rsIpsecTunnelPeerUdpPort,
       "rsIpsecTunnelOrigPeerAddr": rsIpsecTunnelOrigPeerAddr}
)
