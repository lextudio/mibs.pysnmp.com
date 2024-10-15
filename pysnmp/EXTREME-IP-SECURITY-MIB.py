# SNMP MIB module (EXTREME-IP-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-IP-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:46 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremeIpSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HexOctet(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class VlanTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class IpProtocol(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17),
          ("unknown", 0))
    )



class TcpFlagAnomalyReason(Integer32, TextualConvention):
    status = "current"
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
        *(("flagAndSeq", 2),
          ("flagFinAndUrgAandPshandSeq", 3),
          ("flagSynAndFin", 4),
          ("flagSynAndSrcPort", 1),
          ("unknown", 0))
    )



class IcmpAnomalyReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmpFragmented", 2),
          ("icmpOverSize", 1),
          ("unknown", 0))
    )



class TcpFragmentAnomalyReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcpFragmented", 2),
          ("tcpHdrLessSize", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeIpSecurityTraps_ObjectIdentity = ObjectIdentity
extremeIpSecurityTraps = _ExtremeIpSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1)
)
_ExtremeIpSecurityTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeIpSecurityTrapsPrefix = _ExtremeIpSecurityTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0)
)
_ExtremeIpSecurityVlanIfIndex_Type = Integer32
_ExtremeIpSecurityVlanIfIndex_Object = MibScalar
extremeIpSecurityVlanIfIndex = _ExtremeIpSecurityVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 1),
    _ExtremeIpSecurityVlanIfIndex_Type()
)
extremeIpSecurityVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityVlanIfIndex.setStatus("current")


class _ExtremeIpSecurityVlanDescr_Type(DisplayString):
    """Custom type extremeIpSecurityVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeIpSecurityVlanDescr_Type.__name__ = "DisplayString"
_ExtremeIpSecurityVlanDescr_Object = MibScalar
extremeIpSecurityVlanDescr = _ExtremeIpSecurityVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 2),
    _ExtremeIpSecurityVlanDescr_Type()
)
extremeIpSecurityVlanDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityVlanDescr.setStatus("current")
_ExtremeIpSecurityPortIfIndex_Type = Integer32
_ExtremeIpSecurityPortIfIndex_Object = MibScalar
extremeIpSecurityPortIfIndex = _ExtremeIpSecurityPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 3),
    _ExtremeIpSecurityPortIfIndex_Type()
)
extremeIpSecurityPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityPortIfIndex.setStatus("current")
_ExtremeIpSecurityIpAddr_Type = IpAddress
_ExtremeIpSecurityIpAddr_Object = MibScalar
extremeIpSecurityIpAddr = _ExtremeIpSecurityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 4),
    _ExtremeIpSecurityIpAddr_Type()
)
extremeIpSecurityIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityIpAddr.setStatus("current")
_ExtremeIpSecurityMacAddress_Type = MacAddress
_ExtremeIpSecurityMacAddress_Object = MibScalar
extremeIpSecurityMacAddress = _ExtremeIpSecurityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 5),
    _ExtremeIpSecurityMacAddress_Type()
)
extremeIpSecurityMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityMacAddress.setStatus("current")


class _ExtremeIpSecurityViolationType_Type(Integer32):
    """Custom type extremeIpSecurityViolationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("badIpInArpPacket", 3),
          ("badIpMacBindingInArpPacket", 2),
          ("badMacInArpPacket", 4),
          ("bcastSenderIpInArpPacket", 5),
          ("bcastTargetIpInArpPacket", 6),
          ("rogueDhcpServerPacket", 1))
    )


_ExtremeIpSecurityViolationType_Type.__name__ = "Integer32"
_ExtremeIpSecurityViolationType_Object = MibScalar
extremeIpSecurityViolationType = _ExtremeIpSecurityViolationType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 6),
    _ExtremeIpSecurityViolationType_Type()
)
extremeIpSecurityViolationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIpSecurityViolationType.setStatus("current")
_ExtremeIpSecurityAnomalyTraps_ObjectIdentity = ObjectIdentity
extremeIpSecurityAnomalyTraps = _ExtremeIpSecurityAnomalyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2)
)
_ExtremeIpSecurityAnomalyTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeIpSecurityAnomalyTrapsPrefix = _ExtremeIpSecurityAnomalyTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0)
)
_EsAnomalyPortIfIndex_Type = Integer32
_EsAnomalyPortIfIndex_Object = MibScalar
esAnomalyPortIfIndex = _EsAnomalyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 1),
    _EsAnomalyPortIfIndex_Type()
)
esAnomalyPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyPortIfIndex.setStatus("current")
_EsAnomalyVlanIfIndex_Type = Integer32
_EsAnomalyVlanIfIndex_Object = MibScalar
esAnomalyVlanIfIndex = _EsAnomalyVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 2),
    _EsAnomalyVlanIfIndex_Type()
)
esAnomalyVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyVlanIfIndex.setStatus("current")


class _EsAnomalyVlanDescr_Type(DisplayString):
    """Custom type esAnomalyVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EsAnomalyVlanDescr_Type.__name__ = "DisplayString"
_EsAnomalyVlanDescr_Object = MibScalar
esAnomalyVlanDescr = _EsAnomalyVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 3),
    _EsAnomalyVlanDescr_Type()
)
esAnomalyVlanDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyVlanDescr.setStatus("current")
_EsAnomalySrcMacAddress_Type = MacAddress
_EsAnomalySrcMacAddress_Object = MibScalar
esAnomalySrcMacAddress = _EsAnomalySrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 4),
    _EsAnomalySrcMacAddress_Type()
)
esAnomalySrcMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalySrcMacAddress.setStatus("current")
_EsAnomalyDestMacAddress_Type = MacAddress
_EsAnomalyDestMacAddress_Object = MibScalar
esAnomalyDestMacAddress = _EsAnomalyDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 5),
    _EsAnomalyDestMacAddress_Type()
)
esAnomalyDestMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyDestMacAddress.setStatus("current")
_EsAnomalySrcIpAddrType_Type = InetAddressType
_EsAnomalySrcIpAddrType_Object = MibScalar
esAnomalySrcIpAddrType = _EsAnomalySrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 6),
    _EsAnomalySrcIpAddrType_Type()
)
esAnomalySrcIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalySrcIpAddrType.setStatus("current")
_EsAnomalySrcIpAddr_Type = InetAddress
_EsAnomalySrcIpAddr_Object = MibScalar
esAnomalySrcIpAddr = _EsAnomalySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 7),
    _EsAnomalySrcIpAddr_Type()
)
esAnomalySrcIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalySrcIpAddr.setStatus("current")
_EsAnomalyDestIpAddrType_Type = InetAddressType
_EsAnomalyDestIpAddrType_Object = MibScalar
esAnomalyDestIpAddrType = _EsAnomalyDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 8),
    _EsAnomalyDestIpAddrType_Type()
)
esAnomalyDestIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyDestIpAddrType.setStatus("current")
_EsAnomalyDestIpAddr_Type = InetAddress
_EsAnomalyDestIpAddr_Object = MibScalar
esAnomalyDestIpAddr = _EsAnomalyDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 9),
    _EsAnomalyDestIpAddr_Type()
)
esAnomalyDestIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyDestIpAddr.setStatus("current")
_EsAnomalyIpProto_Type = IpProtocol
_EsAnomalyIpProto_Object = MibScalar
esAnomalyIpProto = _EsAnomalyIpProto_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 10),
    _EsAnomalyIpProto_Type()
)
esAnomalyIpProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyIpProto.setStatus("current")
_EsAnomalySrcL4Port_Type = InetPortNumber
_EsAnomalySrcL4Port_Object = MibScalar
esAnomalySrcL4Port = _EsAnomalySrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 11),
    _EsAnomalySrcL4Port_Type()
)
esAnomalySrcL4Port.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalySrcL4Port.setStatus("current")
_EsAnomalyDestL4Port_Type = InetPortNumber
_EsAnomalyDestL4Port_Object = MibScalar
esAnomalyDestL4Port = _EsAnomalyDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 12),
    _EsAnomalyDestL4Port_Type()
)
esAnomalyDestL4Port.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyDestL4Port.setStatus("current")
_EsAnomalyTcpFlag_Type = HexOctet
_EsAnomalyTcpFlag_Object = MibScalar
esAnomalyTcpFlag = _EsAnomalyTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 13),
    _EsAnomalyTcpFlag_Type()
)
esAnomalyTcpFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyTcpFlag.setStatus("current")
_EsAnomalyTcpSeq_Type = Integer32
_EsAnomalyTcpSeq_Object = MibScalar
esAnomalyTcpSeq = _EsAnomalyTcpSeq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 14),
    _EsAnomalyTcpSeq_Type()
)
esAnomalyTcpSeq.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyTcpSeq.setStatus("current")
_EsAnomalyTcpHdrSize_Type = Integer32
_EsAnomalyTcpHdrSize_Object = MibScalar
esAnomalyTcpHdrSize = _EsAnomalyTcpHdrSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 15),
    _EsAnomalyTcpHdrSize_Type()
)
esAnomalyTcpHdrSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyTcpHdrSize.setStatus("current")
_EsAnomalyTcpFlagReason_Type = TcpFlagAnomalyReason
_EsAnomalyTcpFlagReason_Object = MibScalar
esAnomalyTcpFlagReason = _EsAnomalyTcpFlagReason_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 16),
    _EsAnomalyTcpFlagReason_Type()
)
esAnomalyTcpFlagReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyTcpFlagReason.setStatus("current")
_EsAnomalyIcmpReason_Type = IcmpAnomalyReason
_EsAnomalyIcmpReason_Object = MibScalar
esAnomalyIcmpReason = _EsAnomalyIcmpReason_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 17),
    _EsAnomalyIcmpReason_Type()
)
esAnomalyIcmpReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyIcmpReason.setStatus("current")
_EsAnomalyVlanTag_Type = VlanTag
_EsAnomalyVlanTag_Object = MibScalar
esAnomalyVlanTag = _EsAnomalyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 18),
    _EsAnomalyVlanTag_Type()
)
esAnomalyVlanTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyVlanTag.setStatus("current")
_EsAnomalyTcpFragmentReason_Type = TcpFragmentAnomalyReason
_EsAnomalyTcpFragmentReason_Object = MibScalar
esAnomalyTcpFragmentReason = _EsAnomalyTcpFragmentReason_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 19),
    _EsAnomalyTcpFragmentReason_Type()
)
esAnomalyTcpFragmentReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esAnomalyTcpFragmentReason.setStatus("current")

# Managed Objects groups


# Notification objects

extremeIpSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0, 1)
)
extremeIpSecurityViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityViolationType"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityViolation.setStatus(
        "current"
    )

extremeIpSecurityAnomalyIpViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 1)
)
extremeIpSecurityAnomalyIpViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityAnomalyIpViolation.setStatus(
        "current"
    )

extremeIpSecurityAnomalyL4PortViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 2)
)
extremeIpSecurityAnomalyL4PortViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityAnomalyL4PortViolation.setStatus(
        "current"
    )

extremeIpSecurityAnomalyTcpFlagViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 3)
)
extremeIpSecurityAnomalyTcpFlagViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlagReason"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpSeq"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityAnomalyTcpFlagViolation.setStatus(
        "current"
    )

extremeIpSecurityAnomalyTcpFragmentViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 4)
)
extremeIpSecurityAnomalyTcpFragmentViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFragmentReason"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpHdrSize"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityAnomalyTcpFragmentViolation.setStatus(
        "current"
    )

extremeIpSecurityAnomalyIcmpViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 5)
)
extremeIpSecurityAnomalyIcmpViolation.setObjects(
      *(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"),
        ("EXTREME-IP-SECURITY-MIB", "esAnomalyIcmpReason"))
)
if mibBuilder.loadTexts:
    extremeIpSecurityAnomalyIcmpViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-IP-SECURITY-MIB",
    **{"HexOctet": HexOctet,
       "VlanTag": VlanTag,
       "IpProtocol": IpProtocol,
       "TcpFlagAnomalyReason": TcpFlagAnomalyReason,
       "IcmpAnomalyReason": IcmpAnomalyReason,
       "TcpFragmentAnomalyReason": TcpFragmentAnomalyReason,
       "extremeIpSecurity": extremeIpSecurity,
       "extremeIpSecurityTraps": extremeIpSecurityTraps,
       "extremeIpSecurityTrapsPrefix": extremeIpSecurityTrapsPrefix,
       "extremeIpSecurityViolation": extremeIpSecurityViolation,
       "extremeIpSecurityVlanIfIndex": extremeIpSecurityVlanIfIndex,
       "extremeIpSecurityVlanDescr": extremeIpSecurityVlanDescr,
       "extremeIpSecurityPortIfIndex": extremeIpSecurityPortIfIndex,
       "extremeIpSecurityIpAddr": extremeIpSecurityIpAddr,
       "extremeIpSecurityMacAddress": extremeIpSecurityMacAddress,
       "extremeIpSecurityViolationType": extremeIpSecurityViolationType,
       "extremeIpSecurityAnomalyTraps": extremeIpSecurityAnomalyTraps,
       "extremeIpSecurityAnomalyTrapsPrefix": extremeIpSecurityAnomalyTrapsPrefix,
       "extremeIpSecurityAnomalyIpViolation": extremeIpSecurityAnomalyIpViolation,
       "extremeIpSecurityAnomalyL4PortViolation": extremeIpSecurityAnomalyL4PortViolation,
       "extremeIpSecurityAnomalyTcpFlagViolation": extremeIpSecurityAnomalyTcpFlagViolation,
       "extremeIpSecurityAnomalyTcpFragmentViolation": extremeIpSecurityAnomalyTcpFragmentViolation,
       "extremeIpSecurityAnomalyIcmpViolation": extremeIpSecurityAnomalyIcmpViolation,
       "esAnomalyPortIfIndex": esAnomalyPortIfIndex,
       "esAnomalyVlanIfIndex": esAnomalyVlanIfIndex,
       "esAnomalyVlanDescr": esAnomalyVlanDescr,
       "esAnomalySrcMacAddress": esAnomalySrcMacAddress,
       "esAnomalyDestMacAddress": esAnomalyDestMacAddress,
       "esAnomalySrcIpAddrType": esAnomalySrcIpAddrType,
       "esAnomalySrcIpAddr": esAnomalySrcIpAddr,
       "esAnomalyDestIpAddrType": esAnomalyDestIpAddrType,
       "esAnomalyDestIpAddr": esAnomalyDestIpAddr,
       "esAnomalyIpProto": esAnomalyIpProto,
       "esAnomalySrcL4Port": esAnomalySrcL4Port,
       "esAnomalyDestL4Port": esAnomalyDestL4Port,
       "esAnomalyTcpFlag": esAnomalyTcpFlag,
       "esAnomalyTcpSeq": esAnomalyTcpSeq,
       "esAnomalyTcpHdrSize": esAnomalyTcpHdrSize,
       "esAnomalyTcpFlagReason": esAnomalyTcpFlagReason,
       "esAnomalyIcmpReason": esAnomalyIcmpReason,
       "esAnomalyVlanTag": esAnomalyVlanTag,
       "esAnomalyTcpFragmentReason": esAnomalyTcpFragmentReason}
)
