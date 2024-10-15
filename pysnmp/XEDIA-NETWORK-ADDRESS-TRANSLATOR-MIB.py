# SNMP MIB module (XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:58 2024
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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaNetworkAddressTranslatorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XnatIpAddress(IpAddress, TextualConvention):
    status = "current"


class XnatPort(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class XnatCounter(Counter32, TextualConvention):
    status = "current"
    displayHint = "d"


class XnatTimeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class XnatProtocol(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class XnatSessionType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 0),
          ("outbound", 1))
    )



class XnatBindingType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("loadshare", 2),
          ("static", 1))
    )



# MIB Managed Objects in the order of their OIDs

_XnatObjects_ObjectIdentity = ObjectIdentity
xnatObjects = _XnatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1)
)
_XnatGeneral_ObjectIdentity = ObjectIdentity
xnatGeneral = _XnatGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 1)
)


class _XnatAdminStatus_Type(Integer32):
    """Custom type xnatAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XnatAdminStatus_Type.__name__ = "Integer32"
_XnatAdminStatus_Object = MibScalar
xnatAdminStatus = _XnatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 1, 1),
    _XnatAdminStatus_Type()
)
xnatAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatAdminStatus.setStatus("current")


class _XnatMaxIboundSessions_Type(Integer32):
    """Custom type xnatMaxIboundSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_XnatMaxIboundSessions_Type.__name__ = "Integer32"
_XnatMaxIboundSessions_Object = MibScalar
xnatMaxIboundSessions = _XnatMaxIboundSessions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 1, 2),
    _XnatMaxIboundSessions_Type()
)
xnatMaxIboundSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatMaxIboundSessions.setStatus("current")


class _XnatMaxOboundSessions_Type(Integer32):
    """Custom type xnatMaxOboundSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_XnatMaxOboundSessions_Type.__name__ = "Integer32"
_XnatMaxOboundSessions_Object = MibScalar
xnatMaxOboundSessions = _XnatMaxOboundSessions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 1, 3),
    _XnatMaxOboundSessions_Type()
)
xnatMaxOboundSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatMaxOboundSessions.setStatus("current")
_XnatCounters_ObjectIdentity = ObjectIdentity
xnatCounters = _XnatCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2)
)
_XnatOboundPackets_Type = XnatCounter
_XnatOboundPackets_Object = MibScalar
xnatOboundPackets = _XnatOboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 1),
    _XnatOboundPackets_Type()
)
xnatOboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundPackets.setStatus("current")
_XnatOboundIcmp_Type = XnatCounter
_XnatOboundIcmp_Object = MibScalar
xnatOboundIcmp = _XnatOboundIcmp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 2),
    _XnatOboundIcmp_Type()
)
xnatOboundIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundIcmp.setStatus("current")
_XnatOboundTcp_Type = XnatCounter
_XnatOboundTcp_Object = MibScalar
xnatOboundTcp = _XnatOboundTcp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 3),
    _XnatOboundTcp_Type()
)
xnatOboundTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundTcp.setStatus("current")
_XnatOboundUdp_Type = XnatCounter
_XnatOboundUdp_Object = MibScalar
xnatOboundUdp = _XnatOboundUdp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 4),
    _XnatOboundUdp_Type()
)
xnatOboundUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundUdp.setStatus("current")
_XnatOboundUntranslated_Type = XnatCounter
_XnatOboundUntranslated_Object = MibScalar
xnatOboundUntranslated = _XnatOboundUntranslated_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 5),
    _XnatOboundUntranslated_Type()
)
xnatOboundUntranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundUntranslated.setStatus("current")
_XnatOboundDiscards_Type = XnatCounter
_XnatOboundDiscards_Object = MibScalar
xnatOboundDiscards = _XnatOboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 6),
    _XnatOboundDiscards_Type()
)
xnatOboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatOboundDiscards.setStatus("current")
_XnatIboundPackets_Type = XnatCounter
_XnatIboundPackets_Object = MibScalar
xnatIboundPackets = _XnatIboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 7),
    _XnatIboundPackets_Type()
)
xnatIboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundPackets.setStatus("current")
_XnatIboundIcmp_Type = XnatCounter
_XnatIboundIcmp_Object = MibScalar
xnatIboundIcmp = _XnatIboundIcmp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 8),
    _XnatIboundIcmp_Type()
)
xnatIboundIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundIcmp.setStatus("current")
_XnatIboundTcp_Type = XnatCounter
_XnatIboundTcp_Object = MibScalar
xnatIboundTcp = _XnatIboundTcp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 9),
    _XnatIboundTcp_Type()
)
xnatIboundTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundTcp.setStatus("current")
_XnatIboundUdp_Type = XnatCounter
_XnatIboundUdp_Object = MibScalar
xnatIboundUdp = _XnatIboundUdp_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 10),
    _XnatIboundUdp_Type()
)
xnatIboundUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundUdp.setStatus("current")
_XnatIboundUntranslated_Type = XnatCounter
_XnatIboundUntranslated_Object = MibScalar
xnatIboundUntranslated = _XnatIboundUntranslated_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 11),
    _XnatIboundUntranslated_Type()
)
xnatIboundUntranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundUntranslated.setStatus("current")
_XnatIboundDiscards_Type = XnatCounter
_XnatIboundDiscards_Object = MibScalar
xnatIboundDiscards = _XnatIboundDiscards_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 2, 12),
    _XnatIboundDiscards_Type()
)
xnatIboundDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatIboundDiscards.setStatus("current")
_XnatTimers_ObjectIdentity = ObjectIdentity
xnatTimers = _XnatTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3)
)


class _XnatUdpTimeout_Type(XnatTimeout):
    """Custom type xnatUdpTimeout based on XnatTimeout"""
    defaultValue = 300


_XnatUdpTimeout_Object = MibScalar
xnatUdpTimeout = _XnatUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 1),
    _XnatUdpTimeout_Type()
)
xnatUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatUdpTimeout.setStatus("current")


class _XnatDnsTimeout_Type(XnatTimeout):
    """Custom type xnatDnsTimeout based on XnatTimeout"""
    defaultValue = 60


_XnatDnsTimeout_Object = MibScalar
xnatDnsTimeout = _XnatDnsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 2),
    _XnatDnsTimeout_Type()
)
xnatDnsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatDnsTimeout.setStatus("current")


class _XnatTcpTimeout_Type(XnatTimeout):
    """Custom type xnatTcpTimeout based on XnatTimeout"""
    defaultValue = 86400


_XnatTcpTimeout_Object = MibScalar
xnatTcpTimeout = _XnatTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 3),
    _XnatTcpTimeout_Type()
)
xnatTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatTcpTimeout.setStatus("current")


class _XnatFinRstTimeout_Type(XnatTimeout):
    """Custom type xnatFinRstTimeout based on XnatTimeout"""
    defaultValue = 60


_XnatFinRstTimeout_Object = MibScalar
xnatFinRstTimeout = _XnatFinRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 4),
    _XnatFinRstTimeout_Type()
)
xnatFinRstTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatFinRstTimeout.setStatus("current")


class _XnatSynTimeout_Type(XnatTimeout):
    """Custom type xnatSynTimeout based on XnatTimeout"""
    defaultValue = 120


_XnatSynTimeout_Object = MibScalar
xnatSynTimeout = _XnatSynTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 5),
    _XnatSynTimeout_Type()
)
xnatSynTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatSynTimeout.setStatus("current")


class _XnatIcmpTimeout_Type(XnatTimeout):
    """Custom type xnatIcmpTimeout based on XnatTimeout"""
    defaultValue = 90


_XnatIcmpTimeout_Object = MibScalar
xnatIcmpTimeout = _XnatIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 3, 6),
    _XnatIcmpTimeout_Type()
)
xnatIcmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatIcmpTimeout.setStatus("current")
_XnatSessionTable_Object = MibTable
xnatSessionTable = _XnatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4)
)
if mibBuilder.loadTexts:
    xnatSessionTable.setStatus("current")
_XnatSessionEntry_Object = MibTableRow
xnatSessionEntry = _XnatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1)
)
xnatSessionEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionPriAddr"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionPriPort"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionOutAddr"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionOutPort"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionProtocol"),
)
if mibBuilder.loadTexts:
    xnatSessionEntry.setStatus("current")
_XnatSessionPriAddr_Type = XnatIpAddress
_XnatSessionPriAddr_Object = MibTableColumn
xnatSessionPriAddr = _XnatSessionPriAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 1),
    _XnatSessionPriAddr_Type()
)
xnatSessionPriAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatSessionPriAddr.setStatus("current")
_XnatSessionPriPort_Type = XnatPort
_XnatSessionPriPort_Object = MibTableColumn
xnatSessionPriPort = _XnatSessionPriPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 2),
    _XnatSessionPriPort_Type()
)
xnatSessionPriPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatSessionPriPort.setStatus("current")
_XnatSessionRegAddr_Type = XnatIpAddress
_XnatSessionRegAddr_Object = MibTableColumn
xnatSessionRegAddr = _XnatSessionRegAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 3),
    _XnatSessionRegAddr_Type()
)
xnatSessionRegAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatSessionRegAddr.setStatus("current")
_XnatSessionRegPort_Type = XnatPort
_XnatSessionRegPort_Object = MibTableColumn
xnatSessionRegPort = _XnatSessionRegPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 4),
    _XnatSessionRegPort_Type()
)
xnatSessionRegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatSessionRegPort.setStatus("current")
_XnatSessionOutAddr_Type = XnatIpAddress
_XnatSessionOutAddr_Object = MibTableColumn
xnatSessionOutAddr = _XnatSessionOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 5),
    _XnatSessionOutAddr_Type()
)
xnatSessionOutAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatSessionOutAddr.setStatus("current")
_XnatSessionOutPort_Type = XnatPort
_XnatSessionOutPort_Object = MibTableColumn
xnatSessionOutPort = _XnatSessionOutPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 6),
    _XnatSessionOutPort_Type()
)
xnatSessionOutPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatSessionOutPort.setStatus("current")
_XnatSessionProtocol_Type = XnatProtocol
_XnatSessionProtocol_Object = MibTableColumn
xnatSessionProtocol = _XnatSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 7),
    _XnatSessionProtocol_Type()
)
xnatSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatSessionProtocol.setStatus("current")
_XnatSessionType_Type = XnatSessionType
_XnatSessionType_Object = MibTableColumn
xnatSessionType = _XnatSessionType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 8),
    _XnatSessionType_Type()
)
xnatSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatSessionType.setStatus("current")
_XnatSessionRowStatus_Type = RowStatus
_XnatSessionRowStatus_Object = MibTableColumn
xnatSessionRowStatus = _XnatSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 4, 1, 9),
    _XnatSessionRowStatus_Type()
)
xnatSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xnatSessionRowStatus.setStatus("current")
_XnatBindingTable_Object = MibTable
xnatBindingTable = _XnatBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5)
)
if mibBuilder.loadTexts:
    xnatBindingTable.setStatus("current")
_XnatBindingEntry_Object = MibTableRow
xnatBindingEntry = _XnatBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1)
)
xnatBindingEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingPriAddr"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingPriPort"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingRegAddr"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingRegPort"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingProtocol"),
)
if mibBuilder.loadTexts:
    xnatBindingEntry.setStatus("current")
_XnatBindingPriAddr_Type = XnatIpAddress
_XnatBindingPriAddr_Object = MibTableColumn
xnatBindingPriAddr = _XnatBindingPriAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 1),
    _XnatBindingPriAddr_Type()
)
xnatBindingPriAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatBindingPriAddr.setStatus("current")
_XnatBindingPriPort_Type = XnatPort
_XnatBindingPriPort_Object = MibTableColumn
xnatBindingPriPort = _XnatBindingPriPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 2),
    _XnatBindingPriPort_Type()
)
xnatBindingPriPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatBindingPriPort.setStatus("current")
_XnatBindingRegAddr_Type = XnatIpAddress
_XnatBindingRegAddr_Object = MibTableColumn
xnatBindingRegAddr = _XnatBindingRegAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 3),
    _XnatBindingRegAddr_Type()
)
xnatBindingRegAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatBindingRegAddr.setStatus("current")
_XnatBindingRegPort_Type = XnatPort
_XnatBindingRegPort_Object = MibTableColumn
xnatBindingRegPort = _XnatBindingRegPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 4),
    _XnatBindingRegPort_Type()
)
xnatBindingRegPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatBindingRegPort.setStatus("current")
_XnatBindingProtocol_Type = XnatProtocol
_XnatBindingProtocol_Object = MibTableColumn
xnatBindingProtocol = _XnatBindingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 5),
    _XnatBindingProtocol_Type()
)
xnatBindingProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatBindingProtocol.setStatus("current")
_XnatBindingType_Type = XnatBindingType
_XnatBindingType_Object = MibTableColumn
xnatBindingType = _XnatBindingType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 6),
    _XnatBindingType_Type()
)
xnatBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatBindingType.setStatus("current")


class _XnatBindingInSessions_Type(Integer32):
    """Custom type xnatBindingInSessions based on Integer32"""
    defaultValue = 0


_XnatBindingInSessions_Object = MibTableColumn
xnatBindingInSessions = _XnatBindingInSessions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 7),
    _XnatBindingInSessions_Type()
)
xnatBindingInSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatBindingInSessions.setStatus("current")


class _XnatBindingOutSessions_Type(Integer32):
    """Custom type xnatBindingOutSessions based on Integer32"""
    defaultValue = 0


_XnatBindingOutSessions_Object = MibTableColumn
xnatBindingOutSessions = _XnatBindingOutSessions_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 8),
    _XnatBindingOutSessions_Type()
)
xnatBindingOutSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatBindingOutSessions.setStatus("current")
_XnatBindingRowStatus_Type = RowStatus
_XnatBindingRowStatus_Object = MibTableColumn
xnatBindingRowStatus = _XnatBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 5, 1, 9),
    _XnatBindingRowStatus_Type()
)
xnatBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatBindingRowStatus.setStatus("current")
_XnatPools_ObjectIdentity = ObjectIdentity
xnatPools = _XnatPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6)
)
_XnatDynamicNatPoolTable_Object = MibTable
xnatDynamicNatPoolTable = _XnatDynamicNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1)
)
if mibBuilder.loadTexts:
    xnatDynamicNatPoolTable.setStatus("current")
_XnatDynamicNatPoolEntry_Object = MibTableRow
xnatDynamicNatPoolEntry = _XnatDynamicNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1, 1)
)
xnatDynamicNatPoolEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolName"),
)
if mibBuilder.loadTexts:
    xnatDynamicNatPoolEntry.setStatus("current")
_XnatDynNatPoolName_Type = DisplayString
_XnatDynNatPoolName_Object = MibTableColumn
xnatDynNatPoolName = _XnatDynNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1, 1, 1),
    _XnatDynNatPoolName_Type()
)
xnatDynNatPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatDynNatPoolName.setStatus("current")
_XnatDynNatPoolRangeCount_Type = Integer32
_XnatDynNatPoolRangeCount_Object = MibTableColumn
xnatDynNatPoolRangeCount = _XnatDynNatPoolRangeCount_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1, 1, 2),
    _XnatDynNatPoolRangeCount_Type()
)
xnatDynNatPoolRangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeCount.setStatus("current")
_XnatDynNatPoolNetAssgns_Type = Integer32
_XnatDynNatPoolNetAssgns_Object = MibTableColumn
xnatDynNatPoolNetAssgns = _XnatDynNatPoolNetAssgns_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1, 1, 3),
    _XnatDynNatPoolNetAssgns_Type()
)
xnatDynNatPoolNetAssgns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatDynNatPoolNetAssgns.setStatus("current")
_XnatDynNatPoolRowStatus_Type = RowStatus
_XnatDynNatPoolRowStatus_Object = MibTableColumn
xnatDynNatPoolRowStatus = _XnatDynNatPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 1, 1, 4),
    _XnatDynNatPoolRowStatus_Type()
)
xnatDynNatPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNatPoolRowStatus.setStatus("current")
_XnatDynamicNatPoolRangeTable_Object = MibTable
xnatDynamicNatPoolRangeTable = _XnatDynamicNatPoolRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2)
)
if mibBuilder.loadTexts:
    xnatDynamicNatPoolRangeTable.setStatus("current")
_XnatDynamicNatPoolRangeEntry_Object = MibTableRow
xnatDynamicNatPoolRangeEntry = _XnatDynamicNatPoolRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1)
)
xnatDynamicNatPoolRangeEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeName"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeBeg"),
)
if mibBuilder.loadTexts:
    xnatDynamicNatPoolRangeEntry.setStatus("current")
_XnatDynNatPoolRangeName_Type = DisplayString
_XnatDynNatPoolRangeName_Object = MibTableColumn
xnatDynNatPoolRangeName = _XnatDynNatPoolRangeName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1, 1),
    _XnatDynNatPoolRangeName_Type()
)
xnatDynNatPoolRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeName.setStatus("current")
_XnatDynNatPoolRangeBeg_Type = XnatIpAddress
_XnatDynNatPoolRangeBeg_Object = MibTableColumn
xnatDynNatPoolRangeBeg = _XnatDynNatPoolRangeBeg_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1, 2),
    _XnatDynNatPoolRangeBeg_Type()
)
xnatDynNatPoolRangeBeg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeBeg.setStatus("current")
_XnatDynNatPoolRangeEnd_Type = XnatIpAddress
_XnatDynNatPoolRangeEnd_Object = MibTableColumn
xnatDynNatPoolRangeEnd = _XnatDynNatPoolRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1, 3),
    _XnatDynNatPoolRangeEnd_Type()
)
xnatDynNatPoolRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeEnd.setStatus("current")
_XnatDynNatPoolRangeMask_Type = XnatIpAddress
_XnatDynNatPoolRangeMask_Object = MibTableColumn
xnatDynNatPoolRangeMask = _XnatDynNatPoolRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1, 4),
    _XnatDynNatPoolRangeMask_Type()
)
xnatDynNatPoolRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeMask.setStatus("current")
_XnatDynNatPoolRangeRowStatus_Type = RowStatus
_XnatDynNatPoolRangeRowStatus_Object = MibTableColumn
xnatDynNatPoolRangeRowStatus = _XnatDynNatPoolRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 2, 1, 5),
    _XnatDynNatPoolRangeRowStatus_Type()
)
xnatDynNatPoolRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNatPoolRangeRowStatus.setStatus("current")
_XnatDynamicNaptPoolTable_Object = MibTable
xnatDynamicNaptPoolTable = _XnatDynamicNaptPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3)
)
if mibBuilder.loadTexts:
    xnatDynamicNaptPoolTable.setStatus("current")
_XnatDynamicNaptPoolEntry_Object = MibTableRow
xnatDynamicNaptPoolEntry = _XnatDynamicNaptPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1)
)
xnatDynamicNaptPoolEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolName"),
)
if mibBuilder.loadTexts:
    xnatDynamicNaptPoolEntry.setStatus("current")
_XnatDynNaptPoolName_Type = DisplayString
_XnatDynNaptPoolName_Object = MibTableColumn
xnatDynNaptPoolName = _XnatDynNaptPoolName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 1),
    _XnatDynNaptPoolName_Type()
)
xnatDynNaptPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatDynNaptPoolName.setStatus("current")
_XnatDynNaptPoolAddr_Type = XnatIpAddress
_XnatDynNaptPoolAddr_Object = MibTableColumn
xnatDynNaptPoolAddr = _XnatDynNaptPoolAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 2),
    _XnatDynNaptPoolAddr_Type()
)
xnatDynNaptPoolAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNaptPoolAddr.setStatus("current")
_XnatDynNaptPoolMask_Type = XnatIpAddress
_XnatDynNaptPoolMask_Object = MibTableColumn
xnatDynNaptPoolMask = _XnatDynNaptPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 3),
    _XnatDynNaptPoolMask_Type()
)
xnatDynNaptPoolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNaptPoolMask.setStatus("current")


class _XnatDynNaptPoolRangeBeg_Type(XnatPort):
    """Custom type xnatDynNaptPoolRangeBeg based on XnatPort"""
    defaultValue = 20000


_XnatDynNaptPoolRangeBeg_Object = MibTableColumn
xnatDynNaptPoolRangeBeg = _XnatDynNaptPoolRangeBeg_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 4),
    _XnatDynNaptPoolRangeBeg_Type()
)
xnatDynNaptPoolRangeBeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNaptPoolRangeBeg.setStatus("current")


class _XnatDynNaptPoolRangeEnd_Type(XnatPort):
    """Custom type xnatDynNaptPoolRangeEnd based on XnatPort"""
    defaultValue = 24095


_XnatDynNaptPoolRangeEnd_Object = MibTableColumn
xnatDynNaptPoolRangeEnd = _XnatDynNaptPoolRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 5),
    _XnatDynNaptPoolRangeEnd_Type()
)
xnatDynNaptPoolRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNaptPoolRangeEnd.setStatus("current")
_XnatDynNaptPoolNetAssgns_Type = Integer32
_XnatDynNaptPoolNetAssgns_Object = MibTableColumn
xnatDynNaptPoolNetAssgns = _XnatDynNaptPoolNetAssgns_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 6),
    _XnatDynNaptPoolNetAssgns_Type()
)
xnatDynNaptPoolNetAssgns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatDynNaptPoolNetAssgns.setStatus("current")
_XnatDynNaptPoolRowStatus_Type = RowStatus
_XnatDynNaptPoolRowStatus_Object = MibTableColumn
xnatDynNaptPoolRowStatus = _XnatDynNaptPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 3, 1, 7),
    _XnatDynNaptPoolRowStatus_Type()
)
xnatDynNaptPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatDynNaptPoolRowStatus.setStatus("current")
_XnatLoadSharePoolTable_Object = MibTable
xnatLoadSharePoolTable = _XnatLoadSharePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4)
)
if mibBuilder.loadTexts:
    xnatLoadSharePoolTable.setStatus("current")
_XnatLoadSharePoolEntry_Object = MibTableRow
xnatLoadSharePoolEntry = _XnatLoadSharePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1)
)
xnatLoadSharePoolEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolName"),
)
if mibBuilder.loadTexts:
    xnatLoadSharePoolEntry.setStatus("current")
_XnatLoadSharePoolName_Type = DisplayString
_XnatLoadSharePoolName_Object = MibTableColumn
xnatLoadSharePoolName = _XnatLoadSharePoolName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 1),
    _XnatLoadSharePoolName_Type()
)
xnatLoadSharePoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatLoadSharePoolName.setStatus("current")
_XnatLoadSharePoolAddr_Type = XnatIpAddress
_XnatLoadSharePoolAddr_Object = MibTableColumn
xnatLoadSharePoolAddr = _XnatLoadSharePoolAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 2),
    _XnatLoadSharePoolAddr_Type()
)
xnatLoadSharePoolAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolAddr.setStatus("current")
_XnatLoadSharePoolMask_Type = XnatIpAddress
_XnatLoadSharePoolMask_Object = MibTableColumn
xnatLoadSharePoolMask = _XnatLoadSharePoolMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 3),
    _XnatLoadSharePoolMask_Type()
)
xnatLoadSharePoolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolMask.setStatus("current")


class _XnatLoadSharePoolPort_Type(XnatPort):
    """Custom type xnatLoadSharePoolPort based on XnatPort"""
    defaultValue = 0


_XnatLoadSharePoolPort_Object = MibTableColumn
xnatLoadSharePoolPort = _XnatLoadSharePoolPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 4),
    _XnatLoadSharePoolPort_Type()
)
xnatLoadSharePoolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolPort.setStatus("current")


class _XnatLoadSharePoolProtocol_Type(XnatProtocol):
    """Custom type xnatLoadSharePoolProtocol based on XnatProtocol"""
    defaultValue = 0


_XnatLoadSharePoolProtocol_Object = MibTableColumn
xnatLoadSharePoolProtocol = _XnatLoadSharePoolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 5),
    _XnatLoadSharePoolProtocol_Type()
)
xnatLoadSharePoolProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolProtocol.setStatus("current")
_XnatLoadSharePoolRangeCount_Type = Integer32
_XnatLoadSharePoolRangeCount_Object = MibTableColumn
xnatLoadSharePoolRangeCount = _XnatLoadSharePoolRangeCount_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 6),
    _XnatLoadSharePoolRangeCount_Type()
)
xnatLoadSharePoolRangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeCount.setStatus("current")
_XnatLoadSharePoolRowStatus_Type = RowStatus
_XnatLoadSharePoolRowStatus_Object = MibTableColumn
xnatLoadSharePoolRowStatus = _XnatLoadSharePoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 4, 1, 7),
    _XnatLoadSharePoolRowStatus_Type()
)
xnatLoadSharePoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRowStatus.setStatus("current")
_XnatLoadSharePoolRangeTable_Object = MibTable
xnatLoadSharePoolRangeTable = _XnatLoadSharePoolRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5)
)
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeTable.setStatus("current")
_XnatLoadSharePoolRangeEntry_Object = MibTableRow
xnatLoadSharePoolRangeEntry = _XnatLoadSharePoolRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1)
)
xnatLoadSharePoolRangeEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeName"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeBeg"),
)
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeEntry.setStatus("current")
_XnatLoadSharePoolRangeName_Type = DisplayString
_XnatLoadSharePoolRangeName_Object = MibTableColumn
xnatLoadSharePoolRangeName = _XnatLoadSharePoolRangeName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 1),
    _XnatLoadSharePoolRangeName_Type()
)
xnatLoadSharePoolRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeName.setStatus("current")
_XnatLoadSharePoolRangeBeg_Type = XnatIpAddress
_XnatLoadSharePoolRangeBeg_Object = MibTableColumn
xnatLoadSharePoolRangeBeg = _XnatLoadSharePoolRangeBeg_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 2),
    _XnatLoadSharePoolRangeBeg_Type()
)
xnatLoadSharePoolRangeBeg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeBeg.setStatus("current")
_XnatLoadSharePoolRangeEnd_Type = XnatIpAddress
_XnatLoadSharePoolRangeEnd_Object = MibTableColumn
xnatLoadSharePoolRangeEnd = _XnatLoadSharePoolRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 3),
    _XnatLoadSharePoolRangeEnd_Type()
)
xnatLoadSharePoolRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeEnd.setStatus("current")
_XnatLoadSharePoolRangeMask_Type = XnatIpAddress
_XnatLoadSharePoolRangeMask_Object = MibTableColumn
xnatLoadSharePoolRangeMask = _XnatLoadSharePoolRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 4),
    _XnatLoadSharePoolRangeMask_Type()
)
xnatLoadSharePoolRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeMask.setStatus("current")


class _XnatLoadSharePoolRangePort_Type(XnatPort):
    """Custom type xnatLoadSharePoolRangePort based on XnatPort"""
    defaultValue = 0


_XnatLoadSharePoolRangePort_Object = MibTableColumn
xnatLoadSharePoolRangePort = _XnatLoadSharePoolRangePort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 5),
    _XnatLoadSharePoolRangePort_Type()
)
xnatLoadSharePoolRangePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangePort.setStatus("current")


class _XnatLoadSharePoolRangeProtocol_Type(XnatProtocol):
    """Custom type xnatLoadSharePoolRangeProtocol based on XnatProtocol"""
    defaultValue = 0


_XnatLoadSharePoolRangeProtocol_Object = MibTableColumn
xnatLoadSharePoolRangeProtocol = _XnatLoadSharePoolRangeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 6),
    _XnatLoadSharePoolRangeProtocol_Type()
)
xnatLoadSharePoolRangeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeProtocol.setStatus("current")
_XnatLoadSharePoolRangeRowStatus_Type = RowStatus
_XnatLoadSharePoolRangeRowStatus_Object = MibTableColumn
xnatLoadSharePoolRangeRowStatus = _XnatLoadSharePoolRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 6, 5, 1, 7),
    _XnatLoadSharePoolRangeRowStatus_Type()
)
xnatLoadSharePoolRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatLoadSharePoolRangeRowStatus.setStatus("current")
_XnatPrivateNetTable_Object = MibTable
xnatPrivateNetTable = _XnatPrivateNetTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7)
)
if mibBuilder.loadTexts:
    xnatPrivateNetTable.setStatus("current")
_XnatPrivateNetEntry_Object = MibTableRow
xnatPrivateNetEntry = _XnatPrivateNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7, 1)
)
xnatPrivateNetEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPrivateNetAddr"),
)
if mibBuilder.loadTexts:
    xnatPrivateNetEntry.setStatus("current")
_XnatPrivateNetAddr_Type = XnatIpAddress
_XnatPrivateNetAddr_Object = MibTableColumn
xnatPrivateNetAddr = _XnatPrivateNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7, 1, 1),
    _XnatPrivateNetAddr_Type()
)
xnatPrivateNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatPrivateNetAddr.setStatus("current")
_XnatPrivateNetMask_Type = XnatIpAddress
_XnatPrivateNetMask_Object = MibTableColumn
xnatPrivateNetMask = _XnatPrivateNetMask_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7, 1, 2),
    _XnatPrivateNetMask_Type()
)
xnatPrivateNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatPrivateNetMask.setStatus("current")
_XnatPrivateNetPoolCount_Type = Integer32
_XnatPrivateNetPoolCount_Object = MibTableColumn
xnatPrivateNetPoolCount = _XnatPrivateNetPoolCount_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7, 1, 3),
    _XnatPrivateNetPoolCount_Type()
)
xnatPrivateNetPoolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatPrivateNetPoolCount.setStatus("current")
_XnatPrivateNetRowStatus_Type = RowStatus
_XnatPrivateNetRowStatus_Object = MibTableColumn
xnatPrivateNetRowStatus = _XnatPrivateNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 7, 1, 4),
    _XnatPrivateNetRowStatus_Type()
)
xnatPrivateNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatPrivateNetRowStatus.setStatus("current")
_XnatPriNetAssoPoolTable_Object = MibTable
xnatPriNetAssoPoolTable = _XnatPriNetAssoPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8)
)
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolTable.setStatus("current")
_XnatPriNetAssoPoolEntry_Object = MibTableRow
xnatPriNetAssoPoolEntry = _XnatPriNetAssoPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8, 1)
)
xnatPriNetAssoPoolEntry.setIndexNames(
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPriNetAssoPoolNetAddr"),
    (0, "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPriNetAssoPoolName"),
)
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolEntry.setStatus("current")
_XnatPriNetAssoPoolNetAddr_Type = XnatIpAddress
_XnatPriNetAssoPoolNetAddr_Object = MibTableColumn
xnatPriNetAssoPoolNetAddr = _XnatPriNetAssoPoolNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8, 1, 1),
    _XnatPriNetAssoPoolNetAddr_Type()
)
xnatPriNetAssoPoolNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolNetAddr.setStatus("current")
_XnatPriNetAssoPoolName_Type = DisplayString
_XnatPriNetAssoPoolName_Object = MibTableColumn
xnatPriNetAssoPoolName = _XnatPriNetAssoPoolName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8, 1, 2),
    _XnatPriNetAssoPoolName_Type()
)
xnatPriNetAssoPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolName.setStatus("current")
_XnatPriNetAssoPoolOrder_Type = Integer32
_XnatPriNetAssoPoolOrder_Object = MibTableColumn
xnatPriNetAssoPoolOrder = _XnatPriNetAssoPoolOrder_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8, 1, 3),
    _XnatPriNetAssoPoolOrder_Type()
)
xnatPriNetAssoPoolOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolOrder.setStatus("current")
_XnatPriNetAssoPoolRowStatus_Type = RowStatus
_XnatPriNetAssoPoolRowStatus_Object = MibTableColumn
xnatPriNetAssoPoolRowStatus = _XnatPriNetAssoPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 1, 8, 1, 4),
    _XnatPriNetAssoPoolRowStatus_Type()
)
xnatPriNetAssoPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolRowStatus.setStatus("current")
_XnatConformance_ObjectIdentity = ObjectIdentity
xnatConformance = _XnatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2)
)
_XnatCompliances_ObjectIdentity = ObjectIdentity
xnatCompliances = _XnatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 1)
)
_XnatGroups_ObjectIdentity = ObjectIdentity
xnatGroups = _XnatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2)
)

# Managed Objects groups

xnatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 1)
)
xnatGeneralGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatAdminStatus"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatMaxIboundSessions"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatMaxOboundSessions"))
)
if mibBuilder.loadTexts:
    xnatGeneralGroup.setStatus("current")

xnatCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 2)
)
xnatCountersGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundPackets"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundIcmp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundTcp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundUdp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundUntranslated"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatOboundDiscards"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundPackets"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundIcmp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundTcp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundUdp"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundUntranslated"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIboundDiscards"))
)
if mibBuilder.loadTexts:
    xnatCountersGroup.setStatus("current")

xnatTimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 3)
)
xnatTimersGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatUdpTimeout"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDnsTimeout"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatTcpTimeout"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatFinRstTimeout"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSynTimeout"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatIcmpTimeout"))
)
if mibBuilder.loadTexts:
    xnatTimersGroup.setStatus("current")

xnatSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 4)
)
xnatSessionGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionRegAddr"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionRegPort"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionType"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatSessionRowStatus"))
)
if mibBuilder.loadTexts:
    xnatSessionGroup.setStatus("current")

xnatBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 5)
)
xnatBindingGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingType"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingInSessions"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingOutSessions"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatBindingRowStatus"))
)
if mibBuilder.loadTexts:
    xnatBindingGroup.setStatus("current")

xnatDynamicNatPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 6)
)
xnatDynamicNatPoolGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeCount"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolNetAssgns"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRowStatus"))
)
if mibBuilder.loadTexts:
    xnatDynamicNatPoolGroup.setStatus("current")

xnatDynamicNatRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 7)
)
xnatDynamicNatRangeGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeEnd"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeMask"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNatPoolRangeRowStatus"))
)
if mibBuilder.loadTexts:
    xnatDynamicNatRangeGroup.setStatus("current")

xnatDynamicNaptPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 8)
)
xnatDynamicNaptPoolGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolAddr"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolMask"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolRangeBeg"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolRangeEnd"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolNetAssgns"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatDynNaptPoolRowStatus"))
)
if mibBuilder.loadTexts:
    xnatDynamicNaptPoolGroup.setStatus("current")

xnatLoadSharePoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 9)
)
xnatLoadSharePoolGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolAddr"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolMask"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolPort"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolProtocol"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeCount"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRowStatus"))
)
if mibBuilder.loadTexts:
    xnatLoadSharePoolGroup.setStatus("current")

xnatLoadShareRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 10)
)
xnatLoadShareRangeGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeEnd"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeMask"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangePort"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeProtocol"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatLoadSharePoolRangeRowStatus"))
)
if mibBuilder.loadTexts:
    xnatLoadShareRangeGroup.setStatus("current")

xnatPrivateNetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 11)
)
xnatPrivateNetGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPrivateNetMask"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPrivateNetRowStatus"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPrivateNetPoolCount"))
)
if mibBuilder.loadTexts:
    xnatPrivateNetGroup.setStatus("current")

xnatPriNetAssoPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 2, 12)
)
xnatPriNetAssoPoolGroup.setObjects(
      *(("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPriNetAssoPoolOrder"),
        ("XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB", "xnatPriNetAssoPoolRowStatus"))
)
if mibBuilder.loadTexts:
    xnatPriNetAssoPoolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xnatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xnatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-NETWORK-ADDRESS-TRANSLATOR-MIB",
    **{"XnatIpAddress": XnatIpAddress,
       "XnatPort": XnatPort,
       "XnatCounter": XnatCounter,
       "XnatTimeout": XnatTimeout,
       "XnatProtocol": XnatProtocol,
       "XnatSessionType": XnatSessionType,
       "XnatBindingType": XnatBindingType,
       "xediaNetworkAddressTranslatorMIB": xediaNetworkAddressTranslatorMIB,
       "xnatObjects": xnatObjects,
       "xnatGeneral": xnatGeneral,
       "xnatAdminStatus": xnatAdminStatus,
       "xnatMaxIboundSessions": xnatMaxIboundSessions,
       "xnatMaxOboundSessions": xnatMaxOboundSessions,
       "xnatCounters": xnatCounters,
       "xnatOboundPackets": xnatOboundPackets,
       "xnatOboundIcmp": xnatOboundIcmp,
       "xnatOboundTcp": xnatOboundTcp,
       "xnatOboundUdp": xnatOboundUdp,
       "xnatOboundUntranslated": xnatOboundUntranslated,
       "xnatOboundDiscards": xnatOboundDiscards,
       "xnatIboundPackets": xnatIboundPackets,
       "xnatIboundIcmp": xnatIboundIcmp,
       "xnatIboundTcp": xnatIboundTcp,
       "xnatIboundUdp": xnatIboundUdp,
       "xnatIboundUntranslated": xnatIboundUntranslated,
       "xnatIboundDiscards": xnatIboundDiscards,
       "xnatTimers": xnatTimers,
       "xnatUdpTimeout": xnatUdpTimeout,
       "xnatDnsTimeout": xnatDnsTimeout,
       "xnatTcpTimeout": xnatTcpTimeout,
       "xnatFinRstTimeout": xnatFinRstTimeout,
       "xnatSynTimeout": xnatSynTimeout,
       "xnatIcmpTimeout": xnatIcmpTimeout,
       "xnatSessionTable": xnatSessionTable,
       "xnatSessionEntry": xnatSessionEntry,
       "xnatSessionPriAddr": xnatSessionPriAddr,
       "xnatSessionPriPort": xnatSessionPriPort,
       "xnatSessionRegAddr": xnatSessionRegAddr,
       "xnatSessionRegPort": xnatSessionRegPort,
       "xnatSessionOutAddr": xnatSessionOutAddr,
       "xnatSessionOutPort": xnatSessionOutPort,
       "xnatSessionProtocol": xnatSessionProtocol,
       "xnatSessionType": xnatSessionType,
       "xnatSessionRowStatus": xnatSessionRowStatus,
       "xnatBindingTable": xnatBindingTable,
       "xnatBindingEntry": xnatBindingEntry,
       "xnatBindingPriAddr": xnatBindingPriAddr,
       "xnatBindingPriPort": xnatBindingPriPort,
       "xnatBindingRegAddr": xnatBindingRegAddr,
       "xnatBindingRegPort": xnatBindingRegPort,
       "xnatBindingProtocol": xnatBindingProtocol,
       "xnatBindingType": xnatBindingType,
       "xnatBindingInSessions": xnatBindingInSessions,
       "xnatBindingOutSessions": xnatBindingOutSessions,
       "xnatBindingRowStatus": xnatBindingRowStatus,
       "xnatPools": xnatPools,
       "xnatDynamicNatPoolTable": xnatDynamicNatPoolTable,
       "xnatDynamicNatPoolEntry": xnatDynamicNatPoolEntry,
       "xnatDynNatPoolName": xnatDynNatPoolName,
       "xnatDynNatPoolRangeCount": xnatDynNatPoolRangeCount,
       "xnatDynNatPoolNetAssgns": xnatDynNatPoolNetAssgns,
       "xnatDynNatPoolRowStatus": xnatDynNatPoolRowStatus,
       "xnatDynamicNatPoolRangeTable": xnatDynamicNatPoolRangeTable,
       "xnatDynamicNatPoolRangeEntry": xnatDynamicNatPoolRangeEntry,
       "xnatDynNatPoolRangeName": xnatDynNatPoolRangeName,
       "xnatDynNatPoolRangeBeg": xnatDynNatPoolRangeBeg,
       "xnatDynNatPoolRangeEnd": xnatDynNatPoolRangeEnd,
       "xnatDynNatPoolRangeMask": xnatDynNatPoolRangeMask,
       "xnatDynNatPoolRangeRowStatus": xnatDynNatPoolRangeRowStatus,
       "xnatDynamicNaptPoolTable": xnatDynamicNaptPoolTable,
       "xnatDynamicNaptPoolEntry": xnatDynamicNaptPoolEntry,
       "xnatDynNaptPoolName": xnatDynNaptPoolName,
       "xnatDynNaptPoolAddr": xnatDynNaptPoolAddr,
       "xnatDynNaptPoolMask": xnatDynNaptPoolMask,
       "xnatDynNaptPoolRangeBeg": xnatDynNaptPoolRangeBeg,
       "xnatDynNaptPoolRangeEnd": xnatDynNaptPoolRangeEnd,
       "xnatDynNaptPoolNetAssgns": xnatDynNaptPoolNetAssgns,
       "xnatDynNaptPoolRowStatus": xnatDynNaptPoolRowStatus,
       "xnatLoadSharePoolTable": xnatLoadSharePoolTable,
       "xnatLoadSharePoolEntry": xnatLoadSharePoolEntry,
       "xnatLoadSharePoolName": xnatLoadSharePoolName,
       "xnatLoadSharePoolAddr": xnatLoadSharePoolAddr,
       "xnatLoadSharePoolMask": xnatLoadSharePoolMask,
       "xnatLoadSharePoolPort": xnatLoadSharePoolPort,
       "xnatLoadSharePoolProtocol": xnatLoadSharePoolProtocol,
       "xnatLoadSharePoolRangeCount": xnatLoadSharePoolRangeCount,
       "xnatLoadSharePoolRowStatus": xnatLoadSharePoolRowStatus,
       "xnatLoadSharePoolRangeTable": xnatLoadSharePoolRangeTable,
       "xnatLoadSharePoolRangeEntry": xnatLoadSharePoolRangeEntry,
       "xnatLoadSharePoolRangeName": xnatLoadSharePoolRangeName,
       "xnatLoadSharePoolRangeBeg": xnatLoadSharePoolRangeBeg,
       "xnatLoadSharePoolRangeEnd": xnatLoadSharePoolRangeEnd,
       "xnatLoadSharePoolRangeMask": xnatLoadSharePoolRangeMask,
       "xnatLoadSharePoolRangePort": xnatLoadSharePoolRangePort,
       "xnatLoadSharePoolRangeProtocol": xnatLoadSharePoolRangeProtocol,
       "xnatLoadSharePoolRangeRowStatus": xnatLoadSharePoolRangeRowStatus,
       "xnatPrivateNetTable": xnatPrivateNetTable,
       "xnatPrivateNetEntry": xnatPrivateNetEntry,
       "xnatPrivateNetAddr": xnatPrivateNetAddr,
       "xnatPrivateNetMask": xnatPrivateNetMask,
       "xnatPrivateNetPoolCount": xnatPrivateNetPoolCount,
       "xnatPrivateNetRowStatus": xnatPrivateNetRowStatus,
       "xnatPriNetAssoPoolTable": xnatPriNetAssoPoolTable,
       "xnatPriNetAssoPoolEntry": xnatPriNetAssoPoolEntry,
       "xnatPriNetAssoPoolNetAddr": xnatPriNetAssoPoolNetAddr,
       "xnatPriNetAssoPoolName": xnatPriNetAssoPoolName,
       "xnatPriNetAssoPoolOrder": xnatPriNetAssoPoolOrder,
       "xnatPriNetAssoPoolRowStatus": xnatPriNetAssoPoolRowStatus,
       "xnatConformance": xnatConformance,
       "xnatCompliances": xnatCompliances,
       "xnatCompliance": xnatCompliance,
       "xnatGroups": xnatGroups,
       "xnatGeneralGroup": xnatGeneralGroup,
       "xnatCountersGroup": xnatCountersGroup,
       "xnatTimersGroup": xnatTimersGroup,
       "xnatSessionGroup": xnatSessionGroup,
       "xnatBindingGroup": xnatBindingGroup,
       "xnatDynamicNatPoolGroup": xnatDynamicNatPoolGroup,
       "xnatDynamicNatRangeGroup": xnatDynamicNatRangeGroup,
       "xnatDynamicNaptPoolGroup": xnatDynamicNaptPoolGroup,
       "xnatLoadSharePoolGroup": xnatLoadSharePoolGroup,
       "xnatLoadShareRangeGroup": xnatLoadShareRangeGroup,
       "xnatPrivateNetGroup": xnatPrivateNetGroup,
       "xnatPriNetAssoPoolGroup": xnatPriNetAssoPoolGroup}
)
