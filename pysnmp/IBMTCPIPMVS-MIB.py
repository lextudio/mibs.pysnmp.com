# SNMP MIB module (IBMTCPIPMVS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMTCPIPMVS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:59 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipForwardEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipForwardEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tcpConnEntry,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnEntry")

(udpEntry,) = mibBuilder.importSymbols(
    "UDP-MIB",
    "udpEntry")


# MODULE-IDENTITY

ibmTCPIPmvsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2)
)
ibmTCPIPmvsMIB.setRevisions(
        ("2001-03-23 00:00",
         "1900-05-08 00:00",
         "1999-04-01 00:00",
         "1998-09-16 00:00",
         "1998-08-26 00:00",
         "1998-06-03 00:00",
         "1998-03-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TypeOfService(Integer32, TextualConvention):
    status = "obsolete"
    displayHint = "1a"


class DeviceLinkTypes(Integer32, TextualConvention):
    status = "current"
    displayHint = "1a"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("atm", 5),
          ("cdlc", 4),
          ("claw", 3),
          ("ctc", 2),
          ("ethernet", 10),
          ("etheror8023", 12),
          ("fddi", 14),
          ("hch", 9),
          ("ibmtr", 13),
          ("ip", 15),
          ("ipaqenet", 22),
          ("ipaqidio", 28),
          ("ipaqtr", 27),
          ("iucv", 16),
          ("lcs", 1),
          ("loopback", 8),
          ("mpcipa", 21),
          ("mpcosa", 24),
          ("mpcptp", 18),
          ("osaenet", 26),
          ("osafddi", 25),
          ("snalu0", 19),
          ("snalu62", 20),
          ("stack", 17),
          ("t8023", 11),
          ("unknown", 0),
          ("vipa", 7),
          ("x25npsi", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_MvsSNMPagent_ObjectIdentity = ObjectIdentity
mvsSNMPagent = _MvsSNMPagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19)
)
_IbmSNMPRemPing_Type = Integer32
_IbmSNMPRemPing_Object = MibScalar
ibmSNMPRemPing = _IbmSNMPRemPing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 1),
    _IbmSNMPRemPing_Type()
)
ibmSNMPRemPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSNMPRemPing.setStatus("obsolete")
_IbmTCPIPmvsMIBTraps_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsMIBTraps = _IbmTCPIPmvsMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0)
)
_IbmTCPIPmvsAdmin_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsAdmin = _IbmTCPIPmvsAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 1)
)
_IbmTCPIPmvsMIBObjects_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsMIBObjects = _IbmTCPIPmvsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2)
)
_IbmRemotePingGroup_ObjectIdentity = ObjectIdentity
ibmRemotePingGroup = _IbmRemotePingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1)
)
_IbmRemotePingTable_Object = MibTable
ibmRemotePingTable = _IbmRemotePingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibmRemotePingTable.setStatus("current")
_IbmRemotePingEntry_Object = MibTableRow
ibmRemotePingEntry = _IbmRemotePingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1, 1)
)
ibmRemotePingEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsRPingPacketSize"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsRPingTimeOut"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsRPingHostAddress"),
)
if mibBuilder.loadTexts:
    ibmRemotePingEntry.setStatus("current")
_IbmMvsRPingPacketSize_Type = Integer32
_IbmMvsRPingPacketSize_Object = MibTableColumn
ibmMvsRPingPacketSize = _IbmMvsRPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1, 1, 1),
    _IbmMvsRPingPacketSize_Type()
)
ibmMvsRPingPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsRPingPacketSize.setStatus("current")
_IbmMvsRPingTimeOut_Type = Integer32
_IbmMvsRPingTimeOut_Object = MibTableColumn
ibmMvsRPingTimeOut = _IbmMvsRPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1, 1, 2),
    _IbmMvsRPingTimeOut_Type()
)
ibmMvsRPingTimeOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsRPingTimeOut.setStatus("current")
_IbmMvsRPingHostAddress_Type = IpAddress
_IbmMvsRPingHostAddress_Object = MibTableColumn
ibmMvsRPingHostAddress = _IbmMvsRPingHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1, 1, 3),
    _IbmMvsRPingHostAddress_Type()
)
ibmMvsRPingHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsRPingHostAddress.setStatus("current")
_IbmMvsRPingResponseTime_Type = Integer32
_IbmMvsRPingResponseTime_Object = MibTableColumn
ibmMvsRPingResponseTime = _IbmMvsRPingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 1, 1, 1, 4),
    _IbmMvsRPingResponseTime_Type()
)
ibmMvsRPingResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsRPingResponseTime.setStatus("current")
_IbmTcpipMvsSystem_ObjectIdentity = ObjectIdentity
ibmTcpipMvsSystem = _IbmTcpipMvsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2)
)


class _IbmMvsSubagentCacheTime_Type(Integer32):
    """Custom type ibmMvsSubagentCacheTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IbmMvsSubagentCacheTime_Type.__name__ = "Integer32"
_IbmMvsSubagentCacheTime_Object = MibScalar
ibmMvsSubagentCacheTime = _IbmMvsSubagentCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 1),
    _IbmMvsSubagentCacheTime_Type()
)
ibmMvsSubagentCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsSubagentCacheTime.setStatus("current")


class _IbmMvsIgnoreRedirect_Type(Integer32):
    """Custom type ibmMvsIgnoreRedirect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 0))
    )


_IbmMvsIgnoreRedirect_Type.__name__ = "Integer32"
_IbmMvsIgnoreRedirect_Object = MibScalar
ibmMvsIgnoreRedirect = _IbmMvsIgnoreRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 2),
    _IbmMvsIgnoreRedirect_Type()
)
ibmMvsIgnoreRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsIgnoreRedirect.setStatus("current")


class _IbmMvsArpCacheTimeout_Type(Integer32):
    """Custom type ibmMvsArpCacheTimeout based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_IbmMvsArpCacheTimeout_Type.__name__ = "Integer32"
_IbmMvsArpCacheTimeout_Object = MibScalar
ibmMvsArpCacheTimeout = _IbmMvsArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 3),
    _IbmMvsArpCacheTimeout_Type()
)
ibmMvsArpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsArpCacheTimeout.setStatus("current")


class _IbmMvsTcpKeepAliveTimer_Type(Integer32):
    """Custom type ibmMvsTcpKeepAliveTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35791),
    )


_IbmMvsTcpKeepAliveTimer_Type.__name__ = "Integer32"
_IbmMvsTcpKeepAliveTimer_Object = MibScalar
ibmMvsTcpKeepAliveTimer = _IbmMvsTcpKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 4),
    _IbmMvsTcpKeepAliveTimer_Type()
)
ibmMvsTcpKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpKeepAliveTimer.setStatus("current")


class _IbmMvsTcpReceiveBufferSize_Type(Integer32):
    """Custom type ibmMvsTcpReceiveBufferSize based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 524288),
    )


_IbmMvsTcpReceiveBufferSize_Type.__name__ = "Integer32"
_IbmMvsTcpReceiveBufferSize_Object = MibScalar
ibmMvsTcpReceiveBufferSize = _IbmMvsTcpReceiveBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 5),
    _IbmMvsTcpReceiveBufferSize_Type()
)
ibmMvsTcpReceiveBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpReceiveBufferSize.setStatus("current")


class _IbmMvsTcpSendBufferSize_Type(Integer32):
    """Custom type ibmMvsTcpSendBufferSize based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 262144),
    )


_IbmMvsTcpSendBufferSize_Type.__name__ = "Integer32"
_IbmMvsTcpSendBufferSize_Object = MibScalar
ibmMvsTcpSendBufferSize = _IbmMvsTcpSendBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 6),
    _IbmMvsTcpSendBufferSize_Type()
)
ibmMvsTcpSendBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpSendBufferSize.setStatus("current")


class _IbmMvsUdpChecksum_Type(Integer32):
    """Custom type ibmMvsUdpChecksum based on Integer32"""
    defaultValue = 1

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


_IbmMvsUdpChecksum_Type.__name__ = "Integer32"
_IbmMvsUdpChecksum_Object = MibScalar
ibmMvsUdpChecksum = _IbmMvsUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 7),
    _IbmMvsUdpChecksum_Type()
)
ibmMvsUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsUdpChecksum.setStatus("current")
_IbmMvsIplDateAndTime_Type = DateAndTime
_IbmMvsIplDateAndTime_Object = MibScalar
ibmMvsIplDateAndTime = _IbmMvsIplDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 8),
    _IbmMvsIplDateAndTime_Type()
)
ibmMvsIplDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIplDateAndTime.setStatus("current")


class _IbmMvsNoUdpQueueLimit_Type(Integer32):
    """Custom type ibmMvsNoUdpQueueLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noQueueLimit", 1),
          ("queueLimit", 0))
    )


_IbmMvsNoUdpQueueLimit_Type.__name__ = "Integer32"
_IbmMvsNoUdpQueueLimit_Object = MibScalar
ibmMvsNoUdpQueueLimit = _IbmMvsNoUdpQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 9),
    _IbmMvsNoUdpQueueLimit_Type()
)
ibmMvsNoUdpQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsNoUdpQueueLimit.setStatus("current")


class _IbmMvsSoMaxConn_Type(Integer32):
    """Custom type ibmMvsSoMaxConn based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IbmMvsSoMaxConn_Type.__name__ = "Integer32"
_IbmMvsSoMaxConn_Object = MibScalar
ibmMvsSoMaxConn = _IbmMvsSoMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 10),
    _IbmMvsSoMaxConn_Type()
)
ibmMvsSoMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsSoMaxConn.setStatus("current")


class _IbmMvsTcpipProcname_Type(DisplayString):
    """Custom type ibmMvsTcpipProcname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmMvsTcpipProcname_Type.__name__ = "DisplayString"
_IbmMvsTcpipProcname_Object = MibScalar
ibmMvsTcpipProcname = _IbmMvsTcpipProcname_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 11),
    _IbmMvsTcpipProcname_Type()
)
ibmMvsTcpipProcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpipProcname.setStatus("current")
_IbmMvsTcpipAsid_Type = Integer32
_IbmMvsTcpipAsid_Object = MibScalar
ibmMvsTcpipAsid = _IbmMvsTcpipAsid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 12),
    _IbmMvsTcpipAsid_Type()
)
ibmMvsTcpipAsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpipAsid.setStatus("current")


class _IbmMvsSourceVipaEnabled_Type(Integer32):
    """Custom type ibmMvsSourceVipaEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsSourceVipaEnabled_Type.__name__ = "Integer32"
_IbmMvsSourceVipaEnabled_Object = MibScalar
ibmMvsSourceVipaEnabled = _IbmMvsSourceVipaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 13),
    _IbmMvsSourceVipaEnabled_Type()
)
ibmMvsSourceVipaEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsSourceVipaEnabled.setStatus("current")


class _IbmMvsOsasfSysplexName_Type(DisplayString):
    """Custom type ibmMvsOsasfSysplexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsOsasfSysplexName_Type.__name__ = "DisplayString"
_IbmMvsOsasfSysplexName_Object = MibScalar
ibmMvsOsasfSysplexName = _IbmMvsOsasfSysplexName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 14),
    _IbmMvsOsasfSysplexName_Type()
)
ibmMvsOsasfSysplexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsasfSysplexName.setStatus("current")


class _IbmMvsOsasfHostName_Type(DisplayString):
    """Custom type ibmMvsOsasfHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsOsasfHostName_Type.__name__ = "DisplayString"
_IbmMvsOsasfHostName_Object = MibScalar
ibmMvsOsasfHostName = _IbmMvsOsasfHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 15),
    _IbmMvsOsasfHostName_Type()
)
ibmMvsOsasfHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsasfHostName.setStatus("current")


class _IbmMvsOsasfProductVersion_Type(DisplayString):
    """Custom type ibmMvsOsasfProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsOsasfProductVersion_Type.__name__ = "DisplayString"
_IbmMvsOsasfProductVersion_Object = MibScalar
ibmMvsOsasfProductVersion = _IbmMvsOsasfProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 16),
    _IbmMvsOsasfProductVersion_Type()
)
ibmMvsOsasfProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsasfProductVersion.setStatus("current")


class _IbmMvsPrimaryInterfaceIfIndex_Type(Integer32):
    """Custom type ibmMvsPrimaryInterfaceIfIndex based on Integer32"""
    defaultValue = 0


_IbmMvsPrimaryInterfaceIfIndex_Object = MibScalar
ibmMvsPrimaryInterfaceIfIndex = _IbmMvsPrimaryInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 17),
    _IbmMvsPrimaryInterfaceIfIndex_Type()
)
ibmMvsPrimaryInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsPrimaryInterfaceIfIndex.setStatus("current")


class _IbmMvsIpMaxReassemblySize_Type(Integer32):
    """Custom type ibmMvsIpMaxReassemblySize based on Integer32"""
    defaultValue = 65535


_IbmMvsIpMaxReassemblySize_Object = MibScalar
ibmMvsIpMaxReassemblySize = _IbmMvsIpMaxReassemblySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 18),
    _IbmMvsIpMaxReassemblySize_Type()
)
ibmMvsIpMaxReassemblySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpMaxReassemblySize.setStatus("current")


class _IbmMvsTcpRestrictLowPorts_Type(Integer32):
    """Custom type ibmMvsTcpRestrictLowPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsTcpRestrictLowPorts_Type.__name__ = "Integer32"
_IbmMvsTcpRestrictLowPorts_Object = MibScalar
ibmMvsTcpRestrictLowPorts = _IbmMvsTcpRestrictLowPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 19),
    _IbmMvsTcpRestrictLowPorts_Type()
)
ibmMvsTcpRestrictLowPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpRestrictLowPorts.setStatus("current")


class _IbmMvsUdpRestrictLowPorts_Type(Integer32):
    """Custom type ibmMvsUdpRestrictLowPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsUdpRestrictLowPorts_Type.__name__ = "Integer32"
_IbmMvsUdpRestrictLowPorts_Object = MibScalar
ibmMvsUdpRestrictLowPorts = _IbmMvsUdpRestrictLowPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 20),
    _IbmMvsUdpRestrictLowPorts_Type()
)
ibmMvsUdpRestrictLowPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsUdpRestrictLowPorts.setStatus("current")


class _IbmMvsUdpSendBufferSize_Type(Integer32):
    """Custom type ibmMvsUdpSendBufferSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmMvsUdpSendBufferSize_Type.__name__ = "Integer32"
_IbmMvsUdpSendBufferSize_Object = MibScalar
ibmMvsUdpSendBufferSize = _IbmMvsUdpSendBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 21),
    _IbmMvsUdpSendBufferSize_Type()
)
ibmMvsUdpSendBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsUdpSendBufferSize.setStatus("current")


class _IbmMvsUdpRecvBufferSize_Type(Integer32):
    """Custom type ibmMvsUdpRecvBufferSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmMvsUdpRecvBufferSize_Type.__name__ = "Integer32"
_IbmMvsUdpRecvBufferSize_Object = MibScalar
ibmMvsUdpRecvBufferSize = _IbmMvsUdpRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 22),
    _IbmMvsUdpRecvBufferSize_Type()
)
ibmMvsUdpRecvBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsUdpRecvBufferSize.setStatus("current")


class _IbmMvsTcpipStatisticsEnabled_Type(Integer32):
    """Custom type ibmMvsTcpipStatisticsEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsTcpipStatisticsEnabled_Type.__name__ = "Integer32"
_IbmMvsTcpipStatisticsEnabled_Object = MibScalar
ibmMvsTcpipStatisticsEnabled = _IbmMvsTcpipStatisticsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 23),
    _IbmMvsTcpipStatisticsEnabled_Type()
)
ibmMvsTcpipStatisticsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpipStatisticsEnabled.setStatus("current")


class _IbmMvsFirewallEnabled_Type(Integer32):
    """Custom type ibmMvsFirewallEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsFirewallEnabled_Type.__name__ = "Integer32"
_IbmMvsFirewallEnabled_Object = MibScalar
ibmMvsFirewallEnabled = _IbmMvsFirewallEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 24),
    _IbmMvsFirewallEnabled_Type()
)
ibmMvsFirewallEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsFirewallEnabled.setStatus("current")


class _IbmMvsMaximumRetransmitTime_Type(Integer32):
    """Custom type ibmMvsMaximumRetransmitTime based on Integer32"""
    defaultValue = 120000


_IbmMvsMaximumRetransmitTime_Object = MibScalar
ibmMvsMaximumRetransmitTime = _IbmMvsMaximumRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 25),
    _IbmMvsMaximumRetransmitTime_Type()
)
ibmMvsMaximumRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsMaximumRetransmitTime.setStatus("current")


class _IbmMvsMinimumRetransmitTime_Type(Integer32):
    """Custom type ibmMvsMinimumRetransmitTime based on Integer32"""
    defaultValue = 500


_IbmMvsMinimumRetransmitTime_Object = MibScalar
ibmMvsMinimumRetransmitTime = _IbmMvsMinimumRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 26),
    _IbmMvsMinimumRetransmitTime_Type()
)
ibmMvsMinimumRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsMinimumRetransmitTime.setStatus("current")


class _IbmMvsRoundTripGain_Type(Integer32):
    """Custom type ibmMvsRoundTripGain based on Integer32"""
    defaultValue = 125


_IbmMvsRoundTripGain_Object = MibScalar
ibmMvsRoundTripGain = _IbmMvsRoundTripGain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 27),
    _IbmMvsRoundTripGain_Type()
)
ibmMvsRoundTripGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsRoundTripGain.setStatus("current")


class _IbmMvsVarianceGain_Type(Integer32):
    """Custom type ibmMvsVarianceGain based on Integer32"""
    defaultValue = 250


_IbmMvsVarianceGain_Object = MibScalar
ibmMvsVarianceGain = _IbmMvsVarianceGain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 28),
    _IbmMvsVarianceGain_Type()
)
ibmMvsVarianceGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsVarianceGain.setStatus("current")


class _IbmMvsVarianceMultiplier_Type(Integer32):
    """Custom type ibmMvsVarianceMultiplier based on Integer32"""
    defaultValue = 2000


_IbmMvsVarianceMultiplier_Object = MibScalar
ibmMvsVarianceMultiplier = _IbmMvsVarianceMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 29),
    _IbmMvsVarianceMultiplier_Type()
)
ibmMvsVarianceMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsVarianceMultiplier.setStatus("current")


class _IbmMvsSendGarbageEnabled_Type(Integer32):
    """Custom type ibmMvsSendGarbageEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsSendGarbageEnabled_Type.__name__ = "Integer32"
_IbmMvsSendGarbageEnabled_Object = MibScalar
ibmMvsSendGarbageEnabled = _IbmMvsSendGarbageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 30),
    _IbmMvsSendGarbageEnabled_Type()
)
ibmMvsSendGarbageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsSendGarbageEnabled.setStatus("current")


class _IbmMvsTcpMaxReceiveBufferSize_Type(Integer32):
    """Custom type ibmMvsTcpMaxReceiveBufferSize based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 524288),
    )


_IbmMvsTcpMaxReceiveBufferSize_Type.__name__ = "Integer32"
_IbmMvsTcpMaxReceiveBufferSize_Object = MibScalar
ibmMvsTcpMaxReceiveBufferSize = _IbmMvsTcpMaxReceiveBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 31),
    _IbmMvsTcpMaxReceiveBufferSize_Type()
)
ibmMvsTcpMaxReceiveBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpMaxReceiveBufferSize.setStatus("current")


class _IbmMvsMultipathEnabled_Type(TruthValue):
    """Custom type ibmMvsMultipathEnabled based on TruthValue"""


_IbmMvsMultipathEnabled_Object = MibScalar
ibmMvsMultipathEnabled = _IbmMvsMultipathEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 32),
    _IbmMvsMultipathEnabled_Type()
)
ibmMvsMultipathEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsMultipathEnabled.setStatus("obsolete")


class _IbmMvsPathMtuDscEnabled_Type(TruthValue):
    """Custom type ibmMvsPathMtuDscEnabled based on TruthValue"""


_IbmMvsPathMtuDscEnabled_Object = MibScalar
ibmMvsPathMtuDscEnabled = _IbmMvsPathMtuDscEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 33),
    _IbmMvsPathMtuDscEnabled_Type()
)
ibmMvsPathMtuDscEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsPathMtuDscEnabled.setStatus("current")


class _IbmMvsMultipathType_Type(Integer32):
    """Custom type ibmMvsMultipathType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nomultipath", 0),
          ("perconnection", 2),
          ("perpacket", 3))
    )


_IbmMvsMultipathType_Type.__name__ = "Integer32"
_IbmMvsMultipathType_Object = MibScalar
ibmMvsMultipathType = _IbmMvsMultipathType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 34),
    _IbmMvsMultipathType_Type()
)
ibmMvsMultipathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsMultipathType.setStatus("current")


class _IbmMvsIpForwarding_Type(Integer32):
    """Custom type ibmMvsIpForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardingMultipathPkt", 3),
          ("forwardingNoMultipath", 2),
          ("notForwarding", 1))
    )


_IbmMvsIpForwarding_Type.__name__ = "Integer32"
_IbmMvsIpForwarding_Object = MibScalar
ibmMvsIpForwarding = _IbmMvsIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 35),
    _IbmMvsIpForwarding_Type()
)
ibmMvsIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsIpForwarding.setStatus("current")


class _IbmMvsDevRetryDuration_Type(Unsigned32):
    """Custom type ibmMvsDevRetryDuration based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IbmMvsDevRetryDuration_Type.__name__ = "Unsigned32"
_IbmMvsDevRetryDuration_Object = MibScalar
ibmMvsDevRetryDuration = _IbmMvsDevRetryDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 36),
    _IbmMvsDevRetryDuration_Type()
)
ibmMvsDevRetryDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsDevRetryDuration.setStatus("current")


class _IbmMvsTcpFinwait2Time_Type(Integer32):
    """Custom type ibmMvsTcpFinwait2Time based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_IbmMvsTcpFinwait2Time_Type.__name__ = "Integer32"
_IbmMvsTcpFinwait2Time_Object = MibScalar
ibmMvsTcpFinwait2Time = _IbmMvsTcpFinwait2Time_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 37),
    _IbmMvsTcpFinwait2Time_Type()
)
ibmMvsTcpFinwait2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpFinwait2Time.setStatus("current")


class _IbmMvsTcpTimeStamp_Type(TruthValue):
    """Custom type ibmMvsTcpTimeStamp based on TruthValue"""


_IbmMvsTcpTimeStamp_Object = MibScalar
ibmMvsTcpTimeStamp = _IbmMvsTcpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 38),
    _IbmMvsTcpTimeStamp_Type()
)
ibmMvsTcpTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsTcpTimeStamp.setStatus("current")


class _IbmMvsTcpipSubagentVersion_Type(Integer32):
    """Custom type ibmMvsTcpipSubagentVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("v1r2", 1)
    )


_IbmMvsTcpipSubagentVersion_Type.__name__ = "Integer32"
_IbmMvsTcpipSubagentVersion_Object = MibScalar
ibmMvsTcpipSubagentVersion = _IbmMvsTcpipSubagentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 2, 39),
    _IbmMvsTcpipSubagentVersion_Type()
)
ibmMvsTcpipSubagentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpipSubagentVersion.setStatus("current")
_IbmTcpipMvsInterfaceGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsInterfaceGroup = _IbmTcpipMvsInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3)
)
_IbmTcpipMvsDeviceTable_Object = MibTable
ibmTcpipMvsDeviceTable = _IbmTcpipMvsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsDeviceTable.setStatus("current")
_IbmTcpipMvsDeviceEntry_Object = MibTableRow
ibmTcpipMvsDeviceEntry = _IbmTcpipMvsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1)
)
ibmTcpipMvsDeviceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsDeviceEntry.setStatus("current")
_IbmMvsDeviceType_Type = DeviceLinkTypes
_IbmMvsDeviceType_Object = MibTableColumn
ibmMvsDeviceType = _IbmMvsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 1),
    _IbmMvsDeviceType_Type()
)
ibmMvsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceType.setStatus("current")


class _IbmMvsDeviceBaseNumber_Type(OctetString):
    """Custom type ibmMvsDeviceBaseNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmMvsDeviceBaseNumber_Type.__name__ = "OctetString"
_IbmMvsDeviceBaseNumber_Object = MibTableColumn
ibmMvsDeviceBaseNumber = _IbmMvsDeviceBaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 2),
    _IbmMvsDeviceBaseNumber_Type()
)
ibmMvsDeviceBaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceBaseNumber.setStatus("current")


class _IbmMvsDeviceIoBufferSize_Type(Integer32):
    """Custom type ibmMvsDeviceIoBufferSize based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 65535),
    )


_IbmMvsDeviceIoBufferSize_Type.__name__ = "Integer32"
_IbmMvsDeviceIoBufferSize_Object = MibTableColumn
ibmMvsDeviceIoBufferSize = _IbmMvsDeviceIoBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 3),
    _IbmMvsDeviceIoBufferSize_Type()
)
ibmMvsDeviceIoBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceIoBufferSize.setStatus("current")


class _IbmMvsDeviceAutoRestart_Type(Integer32):
    """Custom type ibmMvsDeviceAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsDeviceAutoRestart_Type.__name__ = "Integer32"
_IbmMvsDeviceAutoRestart_Object = MibTableColumn
ibmMvsDeviceAutoRestart = _IbmMvsDeviceAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 4),
    _IbmMvsDeviceAutoRestart_Type()
)
ibmMvsDeviceAutoRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceAutoRestart.setStatus("current")


class _IbmMvsDeviceNetmanEnabled_Type(Integer32):
    """Custom type ibmMvsDeviceNetmanEnabled based on Integer32"""
    defaultValue = -1


_IbmMvsDeviceNetmanEnabled_Object = MibTableColumn
ibmMvsDeviceNetmanEnabled = _IbmMvsDeviceNetmanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 5),
    _IbmMvsDeviceNetmanEnabled_Type()
)
ibmMvsDeviceNetmanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceNetmanEnabled.setStatus("current")


class _IbmMvsDeviceHostClawName_Type(DisplayString):
    """Custom type ibmMvsDeviceHostClawName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsDeviceHostClawName_Type.__name__ = "DisplayString"
_IbmMvsDeviceHostClawName_Object = MibTableColumn
ibmMvsDeviceHostClawName = _IbmMvsDeviceHostClawName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 6),
    _IbmMvsDeviceHostClawName_Type()
)
ibmMvsDeviceHostClawName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceHostClawName.setStatus("current")


class _IbmMvsDeviceWorkstationClawName_Type(DisplayString):
    """Custom type ibmMvsDeviceWorkstationClawName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsDeviceWorkstationClawName_Type.__name__ = "DisplayString"
_IbmMvsDeviceWorkstationClawName_Object = MibTableColumn
ibmMvsDeviceWorkstationClawName = _IbmMvsDeviceWorkstationClawName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 7),
    _IbmMvsDeviceWorkstationClawName_Type()
)
ibmMvsDeviceWorkstationClawName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceWorkstationClawName.setStatus("current")
_IbmMvsDeviceReadBuffers_Type = Integer32
_IbmMvsDeviceReadBuffers_Object = MibTableColumn
ibmMvsDeviceReadBuffers = _IbmMvsDeviceReadBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 8),
    _IbmMvsDeviceReadBuffers_Type()
)
ibmMvsDeviceReadBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceReadBuffers.setStatus("current")
_IbmMvsDeviceReadSize_Type = Integer32
_IbmMvsDeviceReadSize_Object = MibTableColumn
ibmMvsDeviceReadSize = _IbmMvsDeviceReadSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 9),
    _IbmMvsDeviceReadSize_Type()
)
ibmMvsDeviceReadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceReadSize.setStatus("current")
_IbmMvsDeviceWriteBuffers_Type = Integer32
_IbmMvsDeviceWriteBuffers_Object = MibTableColumn
ibmMvsDeviceWriteBuffers = _IbmMvsDeviceWriteBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 10),
    _IbmMvsDeviceWriteBuffers_Type()
)
ibmMvsDeviceWriteBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceWriteBuffers.setStatus("current")
_IbmMvsDeviceWriteSize_Type = Integer32
_IbmMvsDeviceWriteSize_Object = MibTableColumn
ibmMvsDeviceWriteSize = _IbmMvsDeviceWriteSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 11),
    _IbmMvsDeviceWriteSize_Type()
)
ibmMvsDeviceWriteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceWriteSize.setStatus("current")


class _IbmMvsDeviceProcname_Type(DisplayString):
    """Custom type ibmMvsDeviceProcname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsDeviceProcname_Type.__name__ = "DisplayString"
_IbmMvsDeviceProcname_Object = MibTableColumn
ibmMvsDeviceProcname = _IbmMvsDeviceProcname_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 12),
    _IbmMvsDeviceProcname_Type()
)
ibmMvsDeviceProcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceProcname.setStatus("current")


class _IbmMvsDeviceIncomingSvcEnabled_Type(Integer32):
    """Custom type ibmMvsDeviceIncomingSvcEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsDeviceIncomingSvcEnabled_Type.__name__ = "Integer32"
_IbmMvsDeviceIncomingSvcEnabled_Object = MibTableColumn
ibmMvsDeviceIncomingSvcEnabled = _IbmMvsDeviceIncomingSvcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 13),
    _IbmMvsDeviceIncomingSvcEnabled_Type()
)
ibmMvsDeviceIncomingSvcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceIncomingSvcEnabled.setStatus("current")


class _IbmMvsDeviceLuName_Type(DisplayString):
    """Custom type ibmMvsDeviceLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsDeviceLuName_Type.__name__ = "DisplayString"
_IbmMvsDeviceLuName_Object = MibTableColumn
ibmMvsDeviceLuName = _IbmMvsDeviceLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 14),
    _IbmMvsDeviceLuName_Type()
)
ibmMvsDeviceLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceLuName.setStatus("current")


class _IbmMvsDeviceRouterStatus_Type(Integer32):
    """Custom type ibmMvsDeviceRouterStatus based on Integer32"""
    defaultValue = -1


_IbmMvsDeviceRouterStatus_Object = MibTableColumn
ibmMvsDeviceRouterStatus = _IbmMvsDeviceRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 15),
    _IbmMvsDeviceRouterStatus_Type()
)
ibmMvsDeviceRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceRouterStatus.setStatus("current")


class _IbmMvsDeviceActualRouterStatus_Type(Integer32):
    """Custom type ibmMvsDeviceActualRouterStatus based on Integer32"""
    defaultValue = -1


_IbmMvsDeviceActualRouterStatus_Object = MibTableColumn
ibmMvsDeviceActualRouterStatus = _IbmMvsDeviceActualRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 16),
    _IbmMvsDeviceActualRouterStatus_Type()
)
ibmMvsDeviceActualRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceActualRouterStatus.setStatus("current")


class _IbmMvsDeviceConfigPackingMode_Type(Integer32):
    """Custom type ibmMvsDeviceConfigPackingMode based on Integer32"""
    defaultValue = -1


_IbmMvsDeviceConfigPackingMode_Object = MibTableColumn
ibmMvsDeviceConfigPackingMode = _IbmMvsDeviceConfigPackingMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 17),
    _IbmMvsDeviceConfigPackingMode_Type()
)
ibmMvsDeviceConfigPackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceConfigPackingMode.setStatus("current")


class _IbmMvsDeviceActualPackingMode_Type(Integer32):
    """Custom type ibmMvsDeviceActualPackingMode based on Integer32"""
    defaultValue = -1


_IbmMvsDeviceActualPackingMode_Object = MibTableColumn
ibmMvsDeviceActualPackingMode = _IbmMvsDeviceActualPackingMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 1, 1, 18),
    _IbmMvsDeviceActualPackingMode_Type()
)
ibmMvsDeviceActualPackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDeviceActualPackingMode.setStatus("current")
_IbmTcpipMvsLinkTable_Object = MibTable
ibmTcpipMvsLinkTable = _IbmTcpipMvsLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsLinkTable.setStatus("current")
_IbmTcpipMvsLinkEntry_Object = MibTableRow
ibmTcpipMvsLinkEntry = _IbmTcpipMvsLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1)
)
ibmTcpipMvsLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsLinkEntry.setStatus("current")
_IbmMvsLinkType_Type = DeviceLinkTypes
_IbmMvsLinkType_Object = MibTableColumn
ibmMvsLinkType = _IbmMvsLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 1),
    _IbmMvsLinkType_Type()
)
ibmMvsLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkType.setStatus("current")
_IbmMvsLinkDeviceIndex_Type = Integer32
_IbmMvsLinkDeviceIndex_Object = MibTableColumn
ibmMvsLinkDeviceIndex = _IbmMvsLinkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 2),
    _IbmMvsLinkDeviceIndex_Type()
)
ibmMvsLinkDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkDeviceIndex.setStatus("current")


class _IbmMvsLinkAdapterAddr_Type(Integer32):
    """Custom type ibmMvsLinkAdapterAddr based on Integer32"""
    defaultValue = -1


_IbmMvsLinkAdapterAddr_Object = MibTableColumn
ibmMvsLinkAdapterAddr = _IbmMvsLinkAdapterAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 3),
    _IbmMvsLinkAdapterAddr_Type()
)
ibmMvsLinkAdapterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkAdapterAddr.setStatus("current")


class _IbmMvsLinkNumber_Type(Integer32):
    """Custom type ibmMvsLinkNumber based on Integer32"""
    defaultValue = -1


_IbmMvsLinkNumber_Object = MibTableColumn
ibmMvsLinkNumber = _IbmMvsLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 4),
    _IbmMvsLinkNumber_Type()
)
ibmMvsLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkNumber.setStatus("current")


class _IbmMvsLinkIbmtrCanonical_Type(Integer32):
    """Custom type ibmMvsLinkIbmtrCanonical based on Integer32"""
    defaultValue = -1


_IbmMvsLinkIbmtrCanonical_Object = MibTableColumn
ibmMvsLinkIbmtrCanonical = _IbmMvsLinkIbmtrCanonical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 5),
    _IbmMvsLinkIbmtrCanonical_Type()
)
ibmMvsLinkIbmtrCanonical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkIbmtrCanonical.setStatus("current")


class _IbmMvsLinkIbmtrBcast_Type(Integer32):
    """Custom type ibmMvsLinkIbmtrBcast based on Integer32"""
    defaultValue = -1


_IbmMvsLinkIbmtrBcast_Object = MibTableColumn
ibmMvsLinkIbmtrBcast = _IbmMvsLinkIbmtrBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 6),
    _IbmMvsLinkIbmtrBcast_Type()
)
ibmMvsLinkIbmtrBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkIbmtrBcast.setStatus("current")


class _IbmMvsLinkMcast_Type(TruthValue):
    """Custom type ibmMvsLinkMcast based on TruthValue"""


_IbmMvsLinkMcast_Object = MibTableColumn
ibmMvsLinkMcast = _IbmMvsLinkMcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 7),
    _IbmMvsLinkMcast_Type()
)
ibmMvsLinkMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkMcast.setStatus("current")


class _IbmMvsLinkChecksumEnabled_Type(TruthValue):
    """Custom type ibmMvsLinkChecksumEnabled based on TruthValue"""


_IbmMvsLinkChecksumEnabled_Object = MibTableColumn
ibmMvsLinkChecksumEnabled = _IbmMvsLinkChecksumEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 8),
    _IbmMvsLinkChecksumEnabled_Type()
)
ibmMvsLinkChecksumEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkChecksumEnabled.setStatus("current")


class _IbmMvsLinkArpSupport_Type(Integer32):
    """Custom type ibmMvsLinkArpSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("offloadArpInfo", 4),
          ("offloadNoInfo", 3),
          ("tcpipArp", 2),
          ("unknown", 5))
    )


_IbmMvsLinkArpSupport_Type.__name__ = "Integer32"
_IbmMvsLinkArpSupport_Object = MibTableColumn
ibmMvsLinkArpSupport = _IbmMvsLinkArpSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 9),
    _IbmMvsLinkArpSupport_Type()
)
ibmMvsLinkArpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkArpSupport.setStatus("current")


class _IbmMvsLinkMacAddress_Type(OctetString):
    """Custom type ibmMvsLinkMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsLinkMacAddress_Type.__name__ = "OctetString"
_IbmMvsLinkMacAddress_Object = MibTableColumn
ibmMvsLinkMacAddress = _IbmMvsLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 2, 1, 10),
    _IbmMvsLinkMacAddress_Type()
)
ibmMvsLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkMacAddress.setStatus("current")
_IbmTcpipMvsLinkMcastTable_Object = MibTable
ibmTcpipMvsLinkMcastTable = _IbmTcpipMvsLinkMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsLinkMcastTable.setStatus("current")
_IbmTcpipMvsLinkMcastEntry_Object = MibTableRow
ibmTcpipMvsLinkMcastEntry = _IbmTcpipMvsLinkMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 3, 1)
)
ibmTcpipMvsLinkMcastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsLinkMcastGroupAddr"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsLinkMcastEntry.setStatus("current")
_IbmMvsLinkMcastGroupAddr_Type = IpAddress
_IbmMvsLinkMcastGroupAddr_Object = MibTableColumn
ibmMvsLinkMcastGroupAddr = _IbmMvsLinkMcastGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 3, 1, 1),
    _IbmMvsLinkMcastGroupAddr_Type()
)
ibmMvsLinkMcastGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsLinkMcastGroupAddr.setStatus("current")
_IbmMvsLinkMcastRefCount_Type = Unsigned32
_IbmMvsLinkMcastRefCount_Object = MibTableColumn
ibmMvsLinkMcastRefCount = _IbmMvsLinkMcastRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 3, 3, 1, 2),
    _IbmMvsLinkMcastRefCount_Type()
)
ibmMvsLinkMcastRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsLinkMcastRefCount.setStatus("current")
_IbmTcpipMvsPortGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsPortGroup = _IbmTcpipMvsPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4)
)
_IbmTcpipMvsPortTable_Object = MibTable
ibmTcpipMvsPortTable = _IbmTcpipMvsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsPortTable.setStatus("current")
_IbmTcpipMvsPortEntry_Object = MibTableRow
ibmTcpipMvsPortEntry = _IbmTcpipMvsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1)
)
ibmTcpipMvsPortEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsPortNumberLow"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsPortNumberHigh"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsPortProtocol"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsPortProcName"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsPortEntry.setStatus("current")
_IbmMvsPortNumberLow_Type = Integer32
_IbmMvsPortNumberLow_Object = MibTableColumn
ibmMvsPortNumberLow = _IbmMvsPortNumberLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 1),
    _IbmMvsPortNumberLow_Type()
)
ibmMvsPortNumberLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortNumberLow.setStatus("current")
_IbmMvsPortNumberHigh_Type = Integer32
_IbmMvsPortNumberHigh_Object = MibTableColumn
ibmMvsPortNumberHigh = _IbmMvsPortNumberHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 2),
    _IbmMvsPortNumberHigh_Type()
)
ibmMvsPortNumberHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortNumberHigh.setStatus("current")


class _IbmMvsPortProtocol_Type(Integer32):
    """Custom type ibmMvsPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 0),
          ("udp", 1))
    )


_IbmMvsPortProtocol_Type.__name__ = "Integer32"
_IbmMvsPortProtocol_Object = MibTableColumn
ibmMvsPortProtocol = _IbmMvsPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 3),
    _IbmMvsPortProtocol_Type()
)
ibmMvsPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortProtocol.setStatus("current")


class _IbmMvsPortProcName_Type(DisplayString):
    """Custom type ibmMvsPortProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmMvsPortProcName_Type.__name__ = "DisplayString"
_IbmMvsPortProcName_Object = MibTableColumn
ibmMvsPortProcName = _IbmMvsPortProcName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 4),
    _IbmMvsPortProcName_Type()
)
ibmMvsPortProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortProcName.setStatus("current")


class _IbmMvsPortAutoLoggable_Type(Integer32):
    """Custom type ibmMvsPortAutoLoggable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsPortAutoLoggable_Type.__name__ = "Integer32"
_IbmMvsPortAutoLoggable_Object = MibTableColumn
ibmMvsPortAutoLoggable = _IbmMvsPortAutoLoggable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 5),
    _IbmMvsPortAutoLoggable_Type()
)
ibmMvsPortAutoLoggable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortAutoLoggable.setStatus("current")


class _IbmMvsPortDelayAcks_Type(Integer32):
    """Custom type ibmMvsPortDelayAcks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsPortDelayAcks_Type.__name__ = "Integer32"
_IbmMvsPortDelayAcks_Object = MibTableColumn
ibmMvsPortDelayAcks = _IbmMvsPortDelayAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 6),
    _IbmMvsPortDelayAcks_Type()
)
ibmMvsPortDelayAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortDelayAcks.setStatus("current")


class _IbmMvsPortOptMaxSegmentSize_Type(Integer32):
    """Custom type ibmMvsPortOptMaxSegmentSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsPortOptMaxSegmentSize_Type.__name__ = "Integer32"
_IbmMvsPortOptMaxSegmentSize_Object = MibTableColumn
ibmMvsPortOptMaxSegmentSize = _IbmMvsPortOptMaxSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 7),
    _IbmMvsPortOptMaxSegmentSize_Type()
)
ibmMvsPortOptMaxSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortOptMaxSegmentSize.setStatus("current")


class _IbmMvsPortSharePort_Type(Integer32):
    """Custom type ibmMvsPortSharePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsPortSharePort_Type.__name__ = "Integer32"
_IbmMvsPortSharePort_Object = MibTableColumn
ibmMvsPortSharePort = _IbmMvsPortSharePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 8),
    _IbmMvsPortSharePort_Type()
)
ibmMvsPortSharePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortSharePort.setStatus("current")
_IbmMvsPortBindIpAddr_Type = IpAddress
_IbmMvsPortBindIpAddr_Object = MibTableColumn
ibmMvsPortBindIpAddr = _IbmMvsPortBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 9),
    _IbmMvsPortBindIpAddr_Type()
)
ibmMvsPortBindIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortBindIpAddr.setStatus("current")


class _IbmMvsPortSAFResource_Type(DisplayString):
    """Custom type ibmMvsPortSAFResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsPortSAFResource_Type.__name__ = "DisplayString"
_IbmMvsPortSAFResource_Object = MibTableColumn
ibmMvsPortSAFResource = _IbmMvsPortSAFResource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 10),
    _IbmMvsPortSAFResource_Type()
)
ibmMvsPortSAFResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortSAFResource.setStatus("current")


class _IbmMvsPortReuse_Type(TruthValue):
    """Custom type ibmMvsPortReuse based on TruthValue"""


_IbmMvsPortReuse_Object = MibTableColumn
ibmMvsPortReuse = _IbmMvsPortReuse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 4, 1, 1, 11),
    _IbmMvsPortReuse_Type()
)
ibmMvsPortReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsPortReuse.setStatus("current")
_IbmTcpipMvsRouteGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsRouteGroup = _IbmTcpipMvsRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5)
)
_IbmTcpipMvsGatewayTable_Object = MibTable
ibmTcpipMvsGatewayTable = _IbmTcpipMvsGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsGatewayTable.setStatus("current")
_IbmTcpipMvsGatewayEntry_Object = MibTableRow
ibmTcpipMvsGatewayEntry = _IbmTcpipMvsGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsGatewayEntry.setStatus("current")


class _IbmMvsGatewayMaximumRetransmitTime_Type(Integer32):
    """Custom type ibmMvsGatewayMaximumRetransmitTime based on Integer32"""
    defaultValue = 6000


_IbmMvsGatewayMaximumRetransmitTime_Object = MibTableColumn
ibmMvsGatewayMaximumRetransmitTime = _IbmMvsGatewayMaximumRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 1),
    _IbmMvsGatewayMaximumRetransmitTime_Type()
)
ibmMvsGatewayMaximumRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayMaximumRetransmitTime.setStatus("current")


class _IbmMvsGatewayMinimumRetransmitTime_Type(Integer32):
    """Custom type ibmMvsGatewayMinimumRetransmitTime based on Integer32"""
    defaultValue = 75


_IbmMvsGatewayMinimumRetransmitTime_Object = MibTableColumn
ibmMvsGatewayMinimumRetransmitTime = _IbmMvsGatewayMinimumRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 2),
    _IbmMvsGatewayMinimumRetransmitTime_Type()
)
ibmMvsGatewayMinimumRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayMinimumRetransmitTime.setStatus("current")


class _IbmMvsGatewayRoundTripGain_Type(Integer32):
    """Custom type ibmMvsGatewayRoundTripGain based on Integer32"""
    defaultValue = 1200


_IbmMvsGatewayRoundTripGain_Object = MibTableColumn
ibmMvsGatewayRoundTripGain = _IbmMvsGatewayRoundTripGain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 3),
    _IbmMvsGatewayRoundTripGain_Type()
)
ibmMvsGatewayRoundTripGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayRoundTripGain.setStatus("current")


class _IbmMvsGatewayVarianceGain_Type(Integer32):
    """Custom type ibmMvsGatewayVarianceGain based on Integer32"""
    defaultValue = 2500


_IbmMvsGatewayVarianceGain_Object = MibTableColumn
ibmMvsGatewayVarianceGain = _IbmMvsGatewayVarianceGain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 4),
    _IbmMvsGatewayVarianceGain_Type()
)
ibmMvsGatewayVarianceGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayVarianceGain.setStatus("current")


class _IbmMvsGatewayVarianceMultiplier_Type(Integer32):
    """Custom type ibmMvsGatewayVarianceMultiplier based on Integer32"""
    defaultValue = 20000


_IbmMvsGatewayVarianceMultiplier_Object = MibTableColumn
ibmMvsGatewayVarianceMultiplier = _IbmMvsGatewayVarianceMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 5),
    _IbmMvsGatewayVarianceMultiplier_Type()
)
ibmMvsGatewayVarianceMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayVarianceMultiplier.setStatus("current")


class _IbmMvsGatewayDelayAcks_Type(Integer32):
    """Custom type ibmMvsGatewayDelayAcks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IbmMvsGatewayDelayAcks_Type.__name__ = "Integer32"
_IbmMvsGatewayDelayAcks_Object = MibTableColumn
ibmMvsGatewayDelayAcks = _IbmMvsGatewayDelayAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 5, 1, 1, 6),
    _IbmMvsGatewayDelayAcks_Type()
)
ibmMvsGatewayDelayAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsGatewayDelayAcks.setStatus("current")
_IbmTcpipMvsAtmGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsAtmGroup = _IbmTcpipMvsAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6)
)
_OsasfChannelTable_Object = MibTable
osasfChannelTable = _OsasfChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    osasfChannelTable.setStatus("current")
_OsasfChannelEntry_Object = MibTableRow
osasfChannelEntry = _OsasfChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1)
)
osasfChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osasfChannelEntry.setStatus("current")
_IbmMvsAtmOsasfChannelNumber_Type = Integer32
_IbmMvsAtmOsasfChannelNumber_Object = MibTableColumn
ibmMvsAtmOsasfChannelNumber = _IbmMvsAtmOsasfChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 1),
    _IbmMvsAtmOsasfChannelNumber_Type()
)
ibmMvsAtmOsasfChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelNumber.setStatus("current")


class _IbmMvsAtmOsasfChannelType_Type(Integer32):
    """Custom type ibmMvsAtmOsasfChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("osa", 18),
          ("osaExp155", 16),
          ("osaExp155QDIO", 17),
          ("other", 1))
    )


_IbmMvsAtmOsasfChannelType_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfChannelType_Object = MibTableColumn
ibmMvsAtmOsasfChannelType = _IbmMvsAtmOsasfChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 2),
    _IbmMvsAtmOsasfChannelType_Type()
)
ibmMvsAtmOsasfChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelType.setStatus("current")
_IbmMvsAtmOsasfChannelSubType_Type = Integer32
_IbmMvsAtmOsasfChannelSubType_Object = MibTableColumn
ibmMvsAtmOsasfChannelSubType = _IbmMvsAtmOsasfChannelSubType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 3),
    _IbmMvsAtmOsasfChannelSubType_Type()
)
ibmMvsAtmOsasfChannelSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelSubType.setStatus("current")


class _IbmMvsAtmOsasfChannelMode_Type(Integer32):
    """Custom type ibmMvsAtmOsasfChannelMode based on Integer32"""
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
        *(("atmIpFwdMode", 8),
          ("atmLeSnaMode", 5),
          ("atmLeSnaTcpipMode", 6),
          ("atmLeTcpipMode", 4),
          ("atmNativeMode", 7),
          ("other", 1),
          ("passthruMode", 2),
          ("snaMode", 3))
    )


_IbmMvsAtmOsasfChannelMode_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfChannelMode_Object = MibTableColumn
ibmMvsAtmOsasfChannelMode = _IbmMvsAtmOsasfChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 4),
    _IbmMvsAtmOsasfChannelMode_Type()
)
ibmMvsAtmOsasfChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelMode.setStatus("current")


class _IbmMvsAtmOsasfChannelHwModel_Type(Integer32):
    """Custom type ibmMvsAtmOsasfChannelHwModel based on Integer32"""
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
        *(("osa1", 1),
          ("osa2", 2),
          ("osa2Atm", 3),
          ("osaExp155", 4),
          ("undefined", 0))
    )


_IbmMvsAtmOsasfChannelHwModel_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfChannelHwModel_Object = MibTableColumn
ibmMvsAtmOsasfChannelHwModel = _IbmMvsAtmOsasfChannelHwModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 5),
    _IbmMvsAtmOsasfChannelHwModel_Type()
)
ibmMvsAtmOsasfChannelHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelHwModel.setStatus("current")


class _IbmMvsAtmOsasfChannelState_Type(Integer32):
    """Custom type ibmMvsAtmOsasfChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notinst", 3),
          ("offline", 5),
          ("online", 1))
    )


_IbmMvsAtmOsasfChannelState_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfChannelState_Object = MibTableColumn
ibmMvsAtmOsasfChannelState = _IbmMvsAtmOsasfChannelState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 6),
    _IbmMvsAtmOsasfChannelState_Type()
)
ibmMvsAtmOsasfChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelState.setStatus("current")


class _IbmMvsAtmOsasfChannelShared_Type(Integer32):
    """Custom type ibmMvsAtmOsasfChannelShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IbmMvsAtmOsasfChannelShared_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfChannelShared_Object = MibTableColumn
ibmMvsAtmOsasfChannelShared = _IbmMvsAtmOsasfChannelShared_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 7),
    _IbmMvsAtmOsasfChannelShared_Type()
)
ibmMvsAtmOsasfChannelShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelShared.setStatus("current")
_IbmMvsAtmOsasfChannelNumPorts_Type = Integer32
_IbmMvsAtmOsasfChannelNumPorts_Object = MibTableColumn
ibmMvsAtmOsasfChannelNumPorts = _IbmMvsAtmOsasfChannelNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 8),
    _IbmMvsAtmOsasfChannelNumPorts_Type()
)
ibmMvsAtmOsasfChannelNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelNumPorts.setStatus("current")


class _IbmMvsAtmOsasfChannelDeterNodeDesc_Type(OctetString):
    """Custom type ibmMvsAtmOsasfChannelDeterNodeDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmMvsAtmOsasfChannelDeterNodeDesc_Type.__name__ = "OctetString"
_IbmMvsAtmOsasfChannelDeterNodeDesc_Object = MibTableColumn
ibmMvsAtmOsasfChannelDeterNodeDesc = _IbmMvsAtmOsasfChannelDeterNodeDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 9),
    _IbmMvsAtmOsasfChannelDeterNodeDesc_Type()
)
ibmMvsAtmOsasfChannelDeterNodeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelDeterNodeDesc.setStatus("current")
_IbmMvsAtmOsasfChannelControlUnitNumber_Type = Integer32
_IbmMvsAtmOsasfChannelControlUnitNumber_Object = MibTableColumn
ibmMvsAtmOsasfChannelControlUnitNumber = _IbmMvsAtmOsasfChannelControlUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 10),
    _IbmMvsAtmOsasfChannelControlUnitNumber_Type()
)
ibmMvsAtmOsasfChannelControlUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelControlUnitNumber.setStatus("current")
_IbmMvsAtmOsasfChannelCodeLevel_Type = Integer32
_IbmMvsAtmOsasfChannelCodeLevel_Object = MibTableColumn
ibmMvsAtmOsasfChannelCodeLevel = _IbmMvsAtmOsasfChannelCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 11),
    _IbmMvsAtmOsasfChannelCodeLevel_Type()
)
ibmMvsAtmOsasfChannelCodeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelCodeLevel.setStatus("current")


class _IbmMvsAtmOsasfChannelEcLevel_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsAtmOsasfChannelEcLevel_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelEcLevel_Object = MibTableColumn
ibmMvsAtmOsasfChannelEcLevel = _IbmMvsAtmOsasfChannelEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 12),
    _IbmMvsAtmOsasfChannelEcLevel_Type()
)
ibmMvsAtmOsasfChannelEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelEcLevel.setStatus("obsolete")


class _IbmMvsAtmOsasfChannelCurLparName_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelCurLparName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsAtmOsasfChannelCurLparName_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelCurLparName_Object = MibTableColumn
ibmMvsAtmOsasfChannelCurLparName = _IbmMvsAtmOsasfChannelCurLparName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 13),
    _IbmMvsAtmOsasfChannelCurLparName_Type()
)
ibmMvsAtmOsasfChannelCurLparName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelCurLparName.setStatus("current")
_IbmMvsAtmOsasfChannelCurLparNum_Type = Integer32
_IbmMvsAtmOsasfChannelCurLparNum_Object = MibTableColumn
ibmMvsAtmOsasfChannelCurLparNum = _IbmMvsAtmOsasfChannelCurLparNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 14),
    _IbmMvsAtmOsasfChannelCurLparNum_Type()
)
ibmMvsAtmOsasfChannelCurLparNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelCurLparNum.setStatus("current")


class _IbmMvsAtmOsasfChannelManParnName_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelManParnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsAtmOsasfChannelManParnName_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelManParnName_Object = MibTableColumn
ibmMvsAtmOsasfChannelManParnName = _IbmMvsAtmOsasfChannelManParnName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 15),
    _IbmMvsAtmOsasfChannelManParnName_Type()
)
ibmMvsAtmOsasfChannelManParnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelManParnName.setStatus("current")
_IbmMvsAtmOsasfChannelManParnNum_Type = Integer32
_IbmMvsAtmOsasfChannelManParnNum_Object = MibTableColumn
ibmMvsAtmOsasfChannelManParnNum = _IbmMvsAtmOsasfChannelManParnNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 16),
    _IbmMvsAtmOsasfChannelManParnNum_Type()
)
ibmMvsAtmOsasfChannelManParnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelManParnNum.setStatus("current")


class _IbmMvsAtmOsasfChannelDate_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_IbmMvsAtmOsasfChannelDate_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelDate_Object = MibTableColumn
ibmMvsAtmOsasfChannelDate = _IbmMvsAtmOsasfChannelDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 17),
    _IbmMvsAtmOsasfChannelDate_Type()
)
ibmMvsAtmOsasfChannelDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelDate.setStatus("obsolete")


class _IbmMvsAtmOsasfChannelTime_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsAtmOsasfChannelTime_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelTime_Object = MibTableColumn
ibmMvsAtmOsasfChannelTime = _IbmMvsAtmOsasfChannelTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 18),
    _IbmMvsAtmOsasfChannelTime_Type()
)
ibmMvsAtmOsasfChannelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelTime.setStatus("obsolete")


class _IbmMvsAtmOsasfChannelFlashLevel_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfChannelFlashLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IbmMvsAtmOsasfChannelFlashLevel_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfChannelFlashLevel_Object = MibTableColumn
ibmMvsAtmOsasfChannelFlashLevel = _IbmMvsAtmOsasfChannelFlashLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 19),
    _IbmMvsAtmOsasfChannelFlashLevel_Type()
)
ibmMvsAtmOsasfChannelFlashLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelFlashLevel.setStatus("current")
_IbmMvsAtmOsasfChannelVtamId_Type = Integer32
_IbmMvsAtmOsasfChannelVtamId_Object = MibTableColumn
ibmMvsAtmOsasfChannelVtamId = _IbmMvsAtmOsasfChannelVtamId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 1, 1, 20),
    _IbmMvsAtmOsasfChannelVtamId_Type()
)
ibmMvsAtmOsasfChannelVtamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfChannelVtamId.setStatus("obsolete")
_OsasfPortTable_Object = MibTable
osasfPortTable = _OsasfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    osasfPortTable.setStatus("current")
_OsasfPortEntry_Object = MibTableRow
osasfPortEntry = _OsasfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1)
)
osasfPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osasfPortEntry.setStatus("current")
_IbmMvsAtmOsasfPortNumber_Type = Integer32
_IbmMvsAtmOsasfPortNumber_Object = MibTableColumn
ibmMvsAtmOsasfPortNumber = _IbmMvsAtmOsasfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 1),
    _IbmMvsAtmOsasfPortNumber_Type()
)
ibmMvsAtmOsasfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortNumber.setStatus("current")


class _IbmMvsAtmOsasfPortType_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              41)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("ethernet", 1),
          ("osaExp155", 41),
          ("tokenRing", 2))
    )


_IbmMvsAtmOsasfPortType_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortType_Object = MibTableColumn
ibmMvsAtmOsasfPortType = _IbmMvsAtmOsasfPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 2),
    _IbmMvsAtmOsasfPortType_Type()
)
ibmMvsAtmOsasfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortType.setStatus("current")


class _IbmMvsAtmOsasfPortHardwareState_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortHardwareState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("externallyDisabled", 2),
          ("hostDisabled", 1),
          ("internallyDisabled", 3),
          ("linkMonitor", 7),
          ("secmExternallyDisabled", 5),
          ("secmHostDisabled", 4),
          ("secmInternallyDisabled", 6))
    )


_IbmMvsAtmOsasfPortHardwareState_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortHardwareState_Object = MibTableColumn
ibmMvsAtmOsasfPortHardwareState = _IbmMvsAtmOsasfPortHardwareState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 3),
    _IbmMvsAtmOsasfPortHardwareState_Type()
)
ibmMvsAtmOsasfPortHardwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortHardwareState.setStatus("current")


class _IbmMvsAtmOsasfPortMediaType_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("coaxCable", 1),
          ("multimodeFiber", 3),
          ("shieldedTwistedPair", 4),
          ("singleModeFiber", 2),
          ("unshieldedTwistedPair", 5))
    )


_IbmMvsAtmOsasfPortMediaType_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortMediaType_Object = MibTableColumn
ibmMvsAtmOsasfPortMediaType = _IbmMvsAtmOsasfPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 4),
    _IbmMvsAtmOsasfPortMediaType_Type()
)
ibmMvsAtmOsasfPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortMediaType.setStatus("current")


class _IbmMvsAtmOsasfPortUniType_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_IbmMvsAtmOsasfPortUniType_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortUniType_Object = MibTableColumn
ibmMvsAtmOsasfPortUniType = _IbmMvsAtmOsasfPortUniType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 5),
    _IbmMvsAtmOsasfPortUniType_Type()
)
ibmMvsAtmOsasfPortUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortUniType.setStatus("current")


class _IbmMvsAtmOsasfPortUniVersion_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version20", 1),
          ("version30", 2),
          ("version31", 3))
    )


_IbmMvsAtmOsasfPortUniVersion_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortUniVersion_Object = MibTableColumn
ibmMvsAtmOsasfPortUniVersion = _IbmMvsAtmOsasfPortUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 6),
    _IbmMvsAtmOsasfPortUniVersion_Type()
)
ibmMvsAtmOsasfPortUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortUniVersion.setStatus("current")
_IbmMvsAtmOsasfPortNetPrefix_Type = Integer32
_IbmMvsAtmOsasfPortNetPrefix_Object = MibTableColumn
ibmMvsAtmOsasfPortNetPrefix = _IbmMvsAtmOsasfPortNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 7),
    _IbmMvsAtmOsasfPortNetPrefix_Type()
)
ibmMvsAtmOsasfPortNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortNetPrefix.setStatus("current")


class _IbmMvsAtmOsasfPortNetPrefixPrefix_Type(OctetString):
    """Custom type ibmMvsAtmOsasfPortNetPrefixPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_IbmMvsAtmOsasfPortNetPrefixPrefix_Type.__name__ = "OctetString"
_IbmMvsAtmOsasfPortNetPrefixPrefix_Object = MibTableColumn
ibmMvsAtmOsasfPortNetPrefixPrefix = _IbmMvsAtmOsasfPortNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 8),
    _IbmMvsAtmOsasfPortNetPrefixPrefix_Type()
)
ibmMvsAtmOsasfPortNetPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortNetPrefixPrefix.setStatus("current")


class _IbmMvsAtmOsasfPortNetPrefixStatus_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortNetPrefixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IbmMvsAtmOsasfPortNetPrefixStatus_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortNetPrefixStatus_Object = MibTableColumn
ibmMvsAtmOsasfPortNetPrefixStatus = _IbmMvsAtmOsasfPortNetPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 9),
    _IbmMvsAtmOsasfPortNetPrefixStatus_Type()
)
ibmMvsAtmOsasfPortNetPrefixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortNetPrefixStatus.setStatus("current")


class _IbmMvsAtmOsasfPortCodeLoadStatus_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPortCodeLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("configRejected", 3),
          ("notApplicable", 5),
          ("notOperational", 2),
          ("operational", 1),
          ("outOfSync", 4))
    )


_IbmMvsAtmOsasfPortCodeLoadStatus_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPortCodeLoadStatus_Object = MibTableColumn
ibmMvsAtmOsasfPortCodeLoadStatus = _IbmMvsAtmOsasfPortCodeLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 10),
    _IbmMvsAtmOsasfPortCodeLoadStatus_Type()
)
ibmMvsAtmOsasfPortCodeLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortCodeLoadStatus.setStatus("current")


class _IbmMvsAtmOsasfPortMacAddrBurntIn_Type(OctetString):
    """Custom type ibmMvsAtmOsasfPortMacAddrBurntIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsAtmOsasfPortMacAddrBurntIn_Type.__name__ = "OctetString"
_IbmMvsAtmOsasfPortMacAddrBurntIn_Object = MibTableColumn
ibmMvsAtmOsasfPortMacAddrBurntIn = _IbmMvsAtmOsasfPortMacAddrBurntIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 11),
    _IbmMvsAtmOsasfPortMacAddrBurntIn_Type()
)
ibmMvsAtmOsasfPortMacAddrBurntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortMacAddrBurntIn.setStatus("current")


class _IbmMvsAtmOsasfPortMacAddrActive_Type(OctetString):
    """Custom type ibmMvsAtmOsasfPortMacAddrActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsAtmOsasfPortMacAddrActive_Type.__name__ = "OctetString"
_IbmMvsAtmOsasfPortMacAddrActive_Object = MibTableColumn
ibmMvsAtmOsasfPortMacAddrActive = _IbmMvsAtmOsasfPortMacAddrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 12),
    _IbmMvsAtmOsasfPortMacAddrActive_Type()
)
ibmMvsAtmOsasfPortMacAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortMacAddrActive.setStatus("current")
_IbmMvsAtmOsasfPortMaxPcmConnections_Type = Integer32
_IbmMvsAtmOsasfPortMaxPcmConnections_Object = MibTableColumn
ibmMvsAtmOsasfPortMaxPcmConnections = _IbmMvsAtmOsasfPortMaxPcmConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 13),
    _IbmMvsAtmOsasfPortMaxPcmConnections_Type()
)
ibmMvsAtmOsasfPortMaxPcmConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortMaxPcmConnections.setStatus("current")


class _IbmMvsAtmOsasfPortPcmName_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfPortPcmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmMvsAtmOsasfPortPcmName_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfPortPcmName_Object = MibTableColumn
ibmMvsAtmOsasfPortPcmName = _IbmMvsAtmOsasfPortPcmName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 14),
    _IbmMvsAtmOsasfPortPcmName_Type()
)
ibmMvsAtmOsasfPortPcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortPcmName.setStatus("current")
_IbmMvsAtmOsasfPortAAL5InPackets_Type = Counter32
_IbmMvsAtmOsasfPortAAL5InPackets_Object = MibTableColumn
ibmMvsAtmOsasfPortAAL5InPackets = _IbmMvsAtmOsasfPortAAL5InPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 15),
    _IbmMvsAtmOsasfPortAAL5InPackets_Type()
)
ibmMvsAtmOsasfPortAAL5InPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortAAL5InPackets.setStatus("current")
_IbmMvsAtmOsasfPortAAL5OutPackets_Type = Counter32
_IbmMvsAtmOsasfPortAAL5OutPackets_Object = MibTableColumn
ibmMvsAtmOsasfPortAAL5OutPackets = _IbmMvsAtmOsasfPortAAL5OutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 16),
    _IbmMvsAtmOsasfPortAAL5OutPackets_Type()
)
ibmMvsAtmOsasfPortAAL5OutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortAAL5OutPackets.setStatus("current")
_IbmMvsAtmOsasfPortIpAddress_Type = IpAddress
_IbmMvsAtmOsasfPortIpAddress_Object = MibTableColumn
ibmMvsAtmOsasfPortIpAddress = _IbmMvsAtmOsasfPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 2, 1, 17),
    _IbmMvsAtmOsasfPortIpAddress_Type()
)
ibmMvsAtmOsasfPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPortIpAddress.setStatus("current")
_OsasfPvcTable_Object = MibTable
osasfPvcTable = _OsasfPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    osasfPvcTable.setStatus("current")
_OsasfPvcEntry_Object = MibTableRow
osasfPvcEntry = _OsasfPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1)
)
osasfPvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName"),
)
if mibBuilder.loadTexts:
    osasfPvcEntry.setStatus("current")


class _IbmMvsAtmOsasfPvcName_Type(DisplayString):
    """Custom type ibmMvsAtmOsasfPvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmMvsAtmOsasfPvcName_Type.__name__ = "DisplayString"
_IbmMvsAtmOsasfPvcName_Object = MibTableColumn
ibmMvsAtmOsasfPvcName = _IbmMvsAtmOsasfPvcName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 1),
    _IbmMvsAtmOsasfPvcName_Type()
)
ibmMvsAtmOsasfPvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcName.setStatus("current")


class _IbmMvsAtmOsasfPvcBestEffort_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPvcBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IbmMvsAtmOsasfPvcBestEffort_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPvcBestEffort_Object = MibTableColumn
ibmMvsAtmOsasfPvcBestEffort = _IbmMvsAtmOsasfPvcBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 2),
    _IbmMvsAtmOsasfPvcBestEffort_Type()
)
ibmMvsAtmOsasfPvcBestEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcBestEffort.setStatus("current")
_IbmMvsAtmOsasfPvcFwdPeakCellRate_Type = Integer32
_IbmMvsAtmOsasfPvcFwdPeakCellRate_Object = MibTableColumn
ibmMvsAtmOsasfPvcFwdPeakCellRate = _IbmMvsAtmOsasfPvcFwdPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 3),
    _IbmMvsAtmOsasfPvcFwdPeakCellRate_Type()
)
ibmMvsAtmOsasfPvcFwdPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcFwdPeakCellRate.setStatus("current")
_IbmMvsAtmOsasfPvcBwdPeakCellRate_Type = Integer32
_IbmMvsAtmOsasfPvcBwdPeakCellRate_Object = MibTableColumn
ibmMvsAtmOsasfPvcBwdPeakCellRate = _IbmMvsAtmOsasfPvcBwdPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 4),
    _IbmMvsAtmOsasfPvcBwdPeakCellRate_Type()
)
ibmMvsAtmOsasfPvcBwdPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcBwdPeakCellRate.setStatus("current")
_IbmMvsAtmOsasfPvcFwdsustainCellRate_Type = Integer32
_IbmMvsAtmOsasfPvcFwdsustainCellRate_Object = MibTableColumn
ibmMvsAtmOsasfPvcFwdsustainCellRate = _IbmMvsAtmOsasfPvcFwdsustainCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 5),
    _IbmMvsAtmOsasfPvcFwdsustainCellRate_Type()
)
ibmMvsAtmOsasfPvcFwdsustainCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcFwdsustainCellRate.setStatus("current")
_IbmMvsAtmOsasfPvcBwdsustainCellRate_Type = Integer32
_IbmMvsAtmOsasfPvcBwdsustainCellRate_Object = MibTableColumn
ibmMvsAtmOsasfPvcBwdsustainCellRate = _IbmMvsAtmOsasfPvcBwdsustainCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 6),
    _IbmMvsAtmOsasfPvcBwdsustainCellRate_Type()
)
ibmMvsAtmOsasfPvcBwdsustainCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcBwdsustainCellRate.setStatus("current")
_IbmMvsAtmOsasfPvcFwdCellBurstSize_Type = Unsigned32
_IbmMvsAtmOsasfPvcFwdCellBurstSize_Object = MibTableColumn
ibmMvsAtmOsasfPvcFwdCellBurstSize = _IbmMvsAtmOsasfPvcFwdCellBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 7),
    _IbmMvsAtmOsasfPvcFwdCellBurstSize_Type()
)
ibmMvsAtmOsasfPvcFwdCellBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcFwdCellBurstSize.setStatus("current")
_IbmMvsAtmOsasfPvcBwdCellBurstSize_Type = Unsigned32
_IbmMvsAtmOsasfPvcBwdCellBurstSize_Object = MibTableColumn
ibmMvsAtmOsasfPvcBwdCellBurstSize = _IbmMvsAtmOsasfPvcBwdCellBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 8),
    _IbmMvsAtmOsasfPvcBwdCellBurstSize_Type()
)
ibmMvsAtmOsasfPvcBwdCellBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcBwdCellBurstSize.setStatus("current")
_IbmMvsAtmOsasfPvcVpi_Type = Integer32
_IbmMvsAtmOsasfPvcVpi_Object = MibTableColumn
ibmMvsAtmOsasfPvcVpi = _IbmMvsAtmOsasfPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 9),
    _IbmMvsAtmOsasfPvcVpi_Type()
)
ibmMvsAtmOsasfPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcVpi.setStatus("current")
_IbmMvsAtmOsasfPvcVci_Type = Integer32
_IbmMvsAtmOsasfPvcVci_Object = MibTableColumn
ibmMvsAtmOsasfPvcVci = _IbmMvsAtmOsasfPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 10),
    _IbmMvsAtmOsasfPvcVci_Type()
)
ibmMvsAtmOsasfPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcVci.setStatus("current")


class _IbmMvsAtmOsasfPvcFwdMaxAal5PduSize_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPvcFwdMaxAal5PduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9188),
    )


_IbmMvsAtmOsasfPvcFwdMaxAal5PduSize_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPvcFwdMaxAal5PduSize_Object = MibTableColumn
ibmMvsAtmOsasfPvcFwdMaxAal5PduSize = _IbmMvsAtmOsasfPvcFwdMaxAal5PduSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 11),
    _IbmMvsAtmOsasfPvcFwdMaxAal5PduSize_Type()
)
ibmMvsAtmOsasfPvcFwdMaxAal5PduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcFwdMaxAal5PduSize.setStatus("current")


class _IbmMvsAtmOsasfPvcBwdMaxAal5PduSize_Type(Integer32):
    """Custom type ibmMvsAtmOsasfPvcBwdMaxAal5PduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9188),
    )


_IbmMvsAtmOsasfPvcBwdMaxAal5PduSize_Type.__name__ = "Integer32"
_IbmMvsAtmOsasfPvcBwdMaxAal5PduSize_Object = MibTableColumn
ibmMvsAtmOsasfPvcBwdMaxAal5PduSize = _IbmMvsAtmOsasfPvcBwdMaxAal5PduSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 3, 1, 12),
    _IbmMvsAtmOsasfPvcBwdMaxAal5PduSize_Type()
)
ibmMvsAtmOsasfPvcBwdMaxAal5PduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfPvcBwdMaxAal5PduSize.setStatus("current")
_IbmMvsAtmSnaLeTable_Object = MibTable
ibmMvsAtmSnaLeTable = _IbmMvsAtmSnaLeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeTable.setStatus("current")
_IbmMvsAtmSnaLeEntry_Object = MibTableRow
ibmMvsAtmSnaLeEntry = _IbmMvsAtmSnaLeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1)
)
ibmMvsAtmSnaLeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeEntry.setStatus("current")
_IbmMvsAtmSnaLeLlcTi_Type = Integer32
_IbmMvsAtmSnaLeLlcTi_Object = MibTableColumn
ibmMvsAtmSnaLeLlcTi = _IbmMvsAtmSnaLeLlcTi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 1),
    _IbmMvsAtmSnaLeLlcTi_Type()
)
ibmMvsAtmSnaLeLlcTi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeLlcTi.setStatus("current")


class _IbmMvsAtmSnaLeLlcT1_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeLlcT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmMvsAtmSnaLeLlcT1_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeLlcT1_Object = MibTableColumn
ibmMvsAtmSnaLeLlcT1 = _IbmMvsAtmSnaLeLlcT1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 2),
    _IbmMvsAtmSnaLeLlcT1_Type()
)
ibmMvsAtmSnaLeLlcT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeLlcT1.setStatus("current")


class _IbmMvsAtmSnaLeLlcT2_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeLlcT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmMvsAtmSnaLeLlcT2_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeLlcT2_Object = MibTableColumn
ibmMvsAtmSnaLeLlcT2 = _IbmMvsAtmSnaLeLlcT2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 3),
    _IbmMvsAtmSnaLeLlcT2_Type()
)
ibmMvsAtmSnaLeLlcT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeLlcT2.setStatus("current")


class _IbmMvsAtmSnaleMaxStations_Type(Integer32):
    """Custom type ibmMvsAtmSnaleMaxStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmSnaleMaxStations_Type.__name__ = "Integer32"
_IbmMvsAtmSnaleMaxStations_Object = MibTableColumn
ibmMvsAtmSnaleMaxStations = _IbmMvsAtmSnaleMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 4),
    _IbmMvsAtmSnaleMaxStations_Type()
)
ibmMvsAtmSnaleMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaleMaxStations.setStatus("current")


class _IbmMvsAtmSnaLeMaxSaps_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeMaxSaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_IbmMvsAtmSnaLeMaxSaps_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeMaxSaps_Object = MibTableColumn
ibmMvsAtmSnaLeMaxSaps = _IbmMvsAtmSnaLeMaxSaps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 5),
    _IbmMvsAtmSnaLeMaxSaps_Type()
)
ibmMvsAtmSnaLeMaxSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeMaxSaps.setStatus("current")


class _IbmMvsAtmSnaleMaxIn_Type(Integer32):
    """Custom type ibmMvsAtmSnaleMaxIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_IbmMvsAtmSnaleMaxIn_Type.__name__ = "Integer32"
_IbmMvsAtmSnaleMaxIn_Object = MibTableColumn
ibmMvsAtmSnaleMaxIn = _IbmMvsAtmSnaleMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 6),
    _IbmMvsAtmSnaleMaxIn_Type()
)
ibmMvsAtmSnaleMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaleMaxIn.setStatus("current")


class _IbmMvsAtmSnaLeMaxOut_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeMaxOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_IbmMvsAtmSnaLeMaxOut_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeMaxOut_Object = MibTableColumn
ibmMvsAtmSnaLeMaxOut = _IbmMvsAtmSnaLeMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 7),
    _IbmMvsAtmSnaLeMaxOut_Type()
)
ibmMvsAtmSnaLeMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeMaxOut.setStatus("current")


class _IbmMvsAtmSnaLeCrsGroupAddress_Type(OctetString):
    """Custom type ibmMvsAtmSnaLeCrsGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_IbmMvsAtmSnaLeCrsGroupAddress_Type.__name__ = "OctetString"
_IbmMvsAtmSnaLeCrsGroupAddress_Object = MibTableColumn
ibmMvsAtmSnaLeCrsGroupAddress = _IbmMvsAtmSnaLeCrsGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 8),
    _IbmMvsAtmSnaLeCrsGroupAddress_Type()
)
ibmMvsAtmSnaLeCrsGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeCrsGroupAddress.setStatus("current")


class _IbmMvsAtmSnaLeUserData_Type(OctetString):
    """Custom type ibmMvsAtmSnaLeUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmMvsAtmSnaLeUserData_Type.__name__ = "OctetString"
_IbmMvsAtmSnaLeUserData_Object = MibTableColumn
ibmMvsAtmSnaLeUserData = _IbmMvsAtmSnaLeUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 9),
    _IbmMvsAtmSnaLeUserData_Type()
)
ibmMvsAtmSnaLeUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeUserData.setStatus("current")


class _IbmMvsAtmSnaLeClientEnableState_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeClientEnableState based on Integer32"""
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
        *(("enabled", 3),
          ("externalDisabled", 7),
          ("internalFailureDisabled", 4),
          ("lecActivating", 2),
          ("notDefined", 1),
          ("osasfDisabled", 6),
          ("physicalPortDisabled", 5),
          ("unknown", 8))
    )


_IbmMvsAtmSnaLeClientEnableState_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeClientEnableState_Object = MibTableColumn
ibmMvsAtmSnaLeClientEnableState = _IbmMvsAtmSnaLeClientEnableState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 10),
    _IbmMvsAtmSnaLeClientEnableState_Type()
)
ibmMvsAtmSnaLeClientEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeClientEnableState.setStatus("current")
_IbmMvsAtmSnaLeBestEffortPeakRate_Type = Unsigned32
_IbmMvsAtmSnaLeBestEffortPeakRate_Object = MibTableColumn
ibmMvsAtmSnaLeBestEffortPeakRate = _IbmMvsAtmSnaLeBestEffortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 11),
    _IbmMvsAtmSnaLeBestEffortPeakRate_Type()
)
ibmMvsAtmSnaLeBestEffortPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeBestEffortPeakRate.setStatus("current")


class _IbmMvsAtmSnaLeMaxLECConnections_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeMaxLECConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_IbmMvsAtmSnaLeMaxLECConnections_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeMaxLECConnections_Object = MibTableColumn
ibmMvsAtmSnaLeMaxLECConnections = _IbmMvsAtmSnaLeMaxLECConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 12),
    _IbmMvsAtmSnaLeMaxLECConnections_Type()
)
ibmMvsAtmSnaLeMaxLECConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeMaxLECConnections.setStatus("current")


class _IbmMvsAtmSnaLeTrEnableLoadBalancing_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeTrEnableLoadBalancing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IbmMvsAtmSnaLeTrEnableLoadBalancing_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeTrEnableLoadBalancing_Object = MibTableColumn
ibmMvsAtmSnaLeTrEnableLoadBalancing = _IbmMvsAtmSnaLeTrEnableLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 13),
    _IbmMvsAtmSnaLeTrEnableLoadBalancing_Type()
)
ibmMvsAtmSnaLeTrEnableLoadBalancing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeTrEnableLoadBalancing.setStatus("current")


class _IbmMvsAtmSnaLeTrLoadBalancing_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeTrLoadBalancing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_IbmMvsAtmSnaLeTrLoadBalancing_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeTrLoadBalancing_Object = MibTableColumn
ibmMvsAtmSnaLeTrLoadBalancing = _IbmMvsAtmSnaLeTrLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 14),
    _IbmMvsAtmSnaLeTrLoadBalancing_Type()
)
ibmMvsAtmSnaLeTrLoadBalancing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeTrLoadBalancing.setStatus("current")


class _IbmMvsAtmSnaLeTrSessionDelay_Type(Integer32):
    """Custom type ibmMvsAtmSnaLeTrSessionDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 375),
    )


_IbmMvsAtmSnaLeTrSessionDelay_Type.__name__ = "Integer32"
_IbmMvsAtmSnaLeTrSessionDelay_Object = MibTableColumn
ibmMvsAtmSnaLeTrSessionDelay = _IbmMvsAtmSnaLeTrSessionDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 4, 1, 15),
    _IbmMvsAtmSnaLeTrSessionDelay_Type()
)
ibmMvsAtmSnaLeTrSessionDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmSnaLeTrSessionDelay.setStatus("current")
_IbmMvsAtmLecConfigTable_Object = MibTable
ibmMvsAtmLecConfigTable = _IbmMvsAtmLecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5)
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigTable.setStatus("current")
_IbmMvsAtmLecConfigEntry_Object = MibTableRow
ibmMvsAtmLecConfigEntry = _IbmMvsAtmLecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1)
)
ibmMvsAtmLecConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigEntry.setStatus("current")


class _IbmMvsAtmLecConfigMode_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_IbmMvsAtmLecConfigMode_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigMode_Object = MibTableColumn
ibmMvsAtmLecConfigMode = _IbmMvsAtmLecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 1),
    _IbmMvsAtmLecConfigMode_Type()
)
ibmMvsAtmLecConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigMode.setStatus("current")


class _IbmMvsAtmLecConfigLanType_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("tokenRing", 3),
          ("unspecified", 1))
    )


_IbmMvsAtmLecConfigLanType_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigLanType_Object = MibTableColumn
ibmMvsAtmLecConfigLanType = _IbmMvsAtmLecConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 2),
    _IbmMvsAtmLecConfigLanType_Type()
)
ibmMvsAtmLecConfigLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigLanType.setStatus("current")


class _IbmMvsAtmLecConfigMaxDataFrameSize_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigMaxDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("f1516", 2),
          ("f18190", 5),
          ("f4544", 3),
          ("f9234", 4),
          ("unspecified", 1))
    )


_IbmMvsAtmLecConfigMaxDataFrameSize_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigMaxDataFrameSize_Object = MibTableColumn
ibmMvsAtmLecConfigMaxDataFrameSize = _IbmMvsAtmLecConfigMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 3),
    _IbmMvsAtmLecConfigMaxDataFrameSize_Type()
)
ibmMvsAtmLecConfigMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigMaxDataFrameSize.setStatus("current")


class _IbmMvsAtmLecConfigLanName_Type(OctetString):
    """Custom type ibmMvsAtmLecConfigLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmMvsAtmLecConfigLanName_Type.__name__ = "OctetString"
_IbmMvsAtmLecConfigLanName_Object = MibTableColumn
ibmMvsAtmLecConfigLanName = _IbmMvsAtmLecConfigLanName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 4),
    _IbmMvsAtmLecConfigLanName_Type()
)
ibmMvsAtmLecConfigLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigLanName.setStatus("current")


class _IbmMvsAtmLecConfigLesAtmAddress_Type(OctetString):
    """Custom type ibmMvsAtmLecConfigLesAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmMvsAtmLecConfigLesAtmAddress_Type.__name__ = "OctetString"
_IbmMvsAtmLecConfigLesAtmAddress_Object = MibTableColumn
ibmMvsAtmLecConfigLesAtmAddress = _IbmMvsAtmLecConfigLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 5),
    _IbmMvsAtmLecConfigLesAtmAddress_Type()
)
ibmMvsAtmLecConfigLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigLesAtmAddress.setStatus("current")


class _IbmMvsAtmLecControlTimeout_Type(Integer32):
    """Custom type ibmMvsAtmLecControlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IbmMvsAtmLecControlTimeout_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlTimeout_Object = MibTableColumn
ibmMvsAtmLecControlTimeout = _IbmMvsAtmLecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 6),
    _IbmMvsAtmLecControlTimeout_Type()
)
ibmMvsAtmLecControlTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlTimeout.setStatus("current")


class _IbmMvsAtmLecMaxUnknownFrameCount_Type(Integer32):
    """Custom type ibmMvsAtmLecMaxUnknownFrameCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmMvsAtmLecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_IbmMvsAtmLecMaxUnknownFrameCount_Object = MibTableColumn
ibmMvsAtmLecMaxUnknownFrameCount = _IbmMvsAtmLecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 7),
    _IbmMvsAtmLecMaxUnknownFrameCount_Type()
)
ibmMvsAtmLecMaxUnknownFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMaxUnknownFrameCount.setStatus("current")


class _IbmMvsAtmLecMaxUnknownFrameTime_Type(Integer32):
    """Custom type ibmMvsAtmLecMaxUnknownFrameTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmMvsAtmLecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_IbmMvsAtmLecMaxUnknownFrameTime_Object = MibTableColumn
ibmMvsAtmLecMaxUnknownFrameTime = _IbmMvsAtmLecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 8),
    _IbmMvsAtmLecMaxUnknownFrameTime_Type()
)
ibmMvsAtmLecMaxUnknownFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMaxUnknownFrameTime.setStatus("current")
_IbmMvsAtmLecVccTimeoutPeriod_Type = Integer32
_IbmMvsAtmLecVccTimeoutPeriod_Object = MibTableColumn
ibmMvsAtmLecVccTimeoutPeriod = _IbmMvsAtmLecVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 9),
    _IbmMvsAtmLecVccTimeoutPeriod_Type()
)
ibmMvsAtmLecVccTimeoutPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecVccTimeoutPeriod.setStatus("current")


class _IbmMvsAtmLecMaxRetryCount_Type(Integer32):
    """Custom type ibmMvsAtmLecMaxRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_IbmMvsAtmLecMaxRetryCount_Type.__name__ = "Integer32"
_IbmMvsAtmLecMaxRetryCount_Object = MibTableColumn
ibmMvsAtmLecMaxRetryCount = _IbmMvsAtmLecMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 10),
    _IbmMvsAtmLecMaxRetryCount_Type()
)
ibmMvsAtmLecMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMaxRetryCount.setStatus("current")


class _IbmMvsAtmLecAgingTime_Type(Integer32):
    """Custom type ibmMvsAtmLecAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IbmMvsAtmLecAgingTime_Type.__name__ = "Integer32"
_IbmMvsAtmLecAgingTime_Object = MibTableColumn
ibmMvsAtmLecAgingTime = _IbmMvsAtmLecAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 11),
    _IbmMvsAtmLecAgingTime_Type()
)
ibmMvsAtmLecAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecAgingTime.setStatus("current")


class _IbmMvsAtmLecForwardDelayTime_Type(Integer32):
    """Custom type ibmMvsAtmLecForwardDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_IbmMvsAtmLecForwardDelayTime_Type.__name__ = "Integer32"
_IbmMvsAtmLecForwardDelayTime_Object = MibTableColumn
ibmMvsAtmLecForwardDelayTime = _IbmMvsAtmLecForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 12),
    _IbmMvsAtmLecForwardDelayTime_Type()
)
ibmMvsAtmLecForwardDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecForwardDelayTime.setStatus("current")


class _IbmMvsAtmLecExpectedArpResponseTime_Type(Integer32):
    """Custom type ibmMvsAtmLecExpectedArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IbmMvsAtmLecExpectedArpResponseTime_Type.__name__ = "Integer32"
_IbmMvsAtmLecExpectedArpResponseTime_Object = MibTableColumn
ibmMvsAtmLecExpectedArpResponseTime = _IbmMvsAtmLecExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 13),
    _IbmMvsAtmLecExpectedArpResponseTime_Type()
)
ibmMvsAtmLecExpectedArpResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecExpectedArpResponseTime.setStatus("current")


class _IbmMvsAtmLecFlushTimeout_Type(Integer32):
    """Custom type ibmMvsAtmLecFlushTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IbmMvsAtmLecFlushTimeout_Type.__name__ = "Integer32"
_IbmMvsAtmLecFlushTimeout_Object = MibTableColumn
ibmMvsAtmLecFlushTimeout = _IbmMvsAtmLecFlushTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 14),
    _IbmMvsAtmLecFlushTimeout_Type()
)
ibmMvsAtmLecFlushTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecFlushTimeout.setStatus("current")


class _IbmMvsAtmLecPathSwitchingDelay_Type(Integer32):
    """Custom type ibmMvsAtmLecPathSwitchingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IbmMvsAtmLecPathSwitchingDelay_Type.__name__ = "Integer32"
_IbmMvsAtmLecPathSwitchingDelay_Object = MibTableColumn
ibmMvsAtmLecPathSwitchingDelay = _IbmMvsAtmLecPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 15),
    _IbmMvsAtmLecPathSwitchingDelay_Type()
)
ibmMvsAtmLecPathSwitchingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecPathSwitchingDelay.setStatus("current")


class _IbmMvsAtmLecLocalSegmentID_Type(Integer32):
    """Custom type ibmMvsAtmLecLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IbmMvsAtmLecLocalSegmentID_Type.__name__ = "Integer32"
_IbmMvsAtmLecLocalSegmentID_Object = MibTableColumn
ibmMvsAtmLecLocalSegmentID = _IbmMvsAtmLecLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 16),
    _IbmMvsAtmLecLocalSegmentID_Type()
)
ibmMvsAtmLecLocalSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecLocalSegmentID.setStatus("current")


class _IbmMvsAtmLecMulticastSendType_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastSendType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("constantBitRate", 3),
          ("variableBitRate", 2))
    )


_IbmMvsAtmLecMulticastSendType_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastSendType_Object = MibTableColumn
ibmMvsAtmLecMulticastSendType = _IbmMvsAtmLecMulticastSendType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 17),
    _IbmMvsAtmLecMulticastSendType_Type()
)
ibmMvsAtmLecMulticastSendType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendType.setStatus("current")
_IbmMvsAtmLecMulticastSendAvgRate_Type = Unsigned32
_IbmMvsAtmLecMulticastSendAvgRate_Object = MibTableColumn
ibmMvsAtmLecMulticastSendAvgRate = _IbmMvsAtmLecMulticastSendAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 18),
    _IbmMvsAtmLecMulticastSendAvgRate_Type()
)
ibmMvsAtmLecMulticastSendAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendAvgRate.setStatus("current")
_IbmMvsAtmLecMulticastSendPeakRate_Type = Unsigned32
_IbmMvsAtmLecMulticastSendPeakRate_Object = MibTableColumn
ibmMvsAtmLecMulticastSendPeakRate = _IbmMvsAtmLecMulticastSendPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 19),
    _IbmMvsAtmLecMulticastSendPeakRate_Type()
)
ibmMvsAtmLecMulticastSendPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendPeakRate.setStatus("current")


class _IbmMvsAtmLecConnectionCompleteTimer_Type(Integer32):
    """Custom type ibmMvsAtmLecConnectionCompleteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmMvsAtmLecConnectionCompleteTimer_Type.__name__ = "Integer32"
_IbmMvsAtmLecConnectionCompleteTimer_Object = MibTableColumn
ibmMvsAtmLecConnectionCompleteTimer = _IbmMvsAtmLecConnectionCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 20),
    _IbmMvsAtmLecConnectionCompleteTimer_Type()
)
ibmMvsAtmLecConnectionCompleteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConnectionCompleteTimer.setStatus("current")


class _IbmMvsAtmLecPortName_Type(DisplayString):
    """Custom type ibmMvsAtmLecPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmMvsAtmLecPortName_Type.__name__ = "DisplayString"
_IbmMvsAtmLecPortName_Object = MibTableColumn
ibmMvsAtmLecPortName = _IbmMvsAtmLecPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 5, 1, 21),
    _IbmMvsAtmLecPortName_Type()
)
ibmMvsAtmLecPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecPortName.setStatus("current")
_IbmMvsAtmLecStatusTable_Object = MibTable
ibmMvsAtmLecStatusTable = _IbmMvsAtmLecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6)
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecStatusTable.setStatus("current")
_IbmMvsAtmLecStatusEntry_Object = MibTableRow
ibmMvsAtmLecStatusEntry = _IbmMvsAtmLecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1)
)
ibmMvsAtmLecStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecStatusEntry.setStatus("current")


class _IbmMvsAtmLecPrimaryAtmAddress_Type(OctetString):
    """Custom type ibmMvsAtmLecPrimaryAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmMvsAtmLecPrimaryAtmAddress_Type.__name__ = "OctetString"
_IbmMvsAtmLecPrimaryAtmAddress_Object = MibTableColumn
ibmMvsAtmLecPrimaryAtmAddress = _IbmMvsAtmLecPrimaryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 1),
    _IbmMvsAtmLecPrimaryAtmAddress_Type()
)
ibmMvsAtmLecPrimaryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecPrimaryAtmAddress.setStatus("current")


class _IbmMvsAtmLecID_Type(Integer32):
    """Custom type ibmMvsAtmLecID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_IbmMvsAtmLecID_Type.__name__ = "Integer32"
_IbmMvsAtmLecID_Object = MibTableColumn
ibmMvsAtmLecID = _IbmMvsAtmLecID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 2),
    _IbmMvsAtmLecID_Type()
)
ibmMvsAtmLecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecID.setStatus("current")


class _IbmMvsAtmLecInterfaceState_Type(Integer32):
    """Custom type ibmMvsAtmLecInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_IbmMvsAtmLecInterfaceState_Type.__name__ = "Integer32"
_IbmMvsAtmLecInterfaceState_Object = MibTableColumn
ibmMvsAtmLecInterfaceState = _IbmMvsAtmLecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 3),
    _IbmMvsAtmLecInterfaceState_Type()
)
ibmMvsAtmLecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecInterfaceState.setStatus("current")


class _IbmMvsAtmLecLastFailureRespCode_Type(Integer32):
    """Custom type ibmMvsAtmLecLastFailureRespCode based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 9),
          ("duplicateAtmAddress", 7),
          ("duplicateLanDestination", 6),
          ("insufficientInformation", 15),
          ("insufficientResources", 8),
          ("invalidAtmAddress", 12),
          ("invalidLanDestination", 11),
          ("invalidRequestParameters", 5),
          ("invalidRequesterId", 10),
          ("leConfigureError", 14),
          ("noConfiguration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4))
    )


_IbmMvsAtmLecLastFailureRespCode_Type.__name__ = "Integer32"
_IbmMvsAtmLecLastFailureRespCode_Object = MibTableColumn
ibmMvsAtmLecLastFailureRespCode = _IbmMvsAtmLecLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 4),
    _IbmMvsAtmLecLastFailureRespCode_Type()
)
ibmMvsAtmLecLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecLastFailureRespCode.setStatus("current")


class _IbmMvsAtmLecLastFailureState_Type(Integer32):
    """Custom type ibmMvsAtmLecLastFailureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_IbmMvsAtmLecLastFailureState_Type.__name__ = "Integer32"
_IbmMvsAtmLecLastFailureState_Object = MibTableColumn
ibmMvsAtmLecLastFailureState = _IbmMvsAtmLecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 5),
    _IbmMvsAtmLecLastFailureState_Type()
)
ibmMvsAtmLecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecLastFailureState.setStatus("current")


class _IbmMvsAtmLecProtocol_Type(Integer32):
    """Custom type ibmMvsAtmLecProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmMvsAtmLecProtocol_Type.__name__ = "Integer32"
_IbmMvsAtmLecProtocol_Object = MibTableColumn
ibmMvsAtmLecProtocol = _IbmMvsAtmLecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 6),
    _IbmMvsAtmLecProtocol_Type()
)
ibmMvsAtmLecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecProtocol.setStatus("current")


class _IbmMvsAtmLecVersion_Type(Integer32):
    """Custom type ibmMvsAtmLecVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmMvsAtmLecVersion_Type.__name__ = "Integer32"
_IbmMvsAtmLecVersion_Object = MibTableColumn
ibmMvsAtmLecVersion = _IbmMvsAtmLecVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 7),
    _IbmMvsAtmLecVersion_Type()
)
ibmMvsAtmLecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecVersion.setStatus("current")


class _IbmMvsAtmLecTopologyChange_Type(Integer32):
    """Custom type ibmMvsAtmLecTopologyChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IbmMvsAtmLecTopologyChange_Type.__name__ = "Integer32"
_IbmMvsAtmLecTopologyChange_Object = MibTableColumn
ibmMvsAtmLecTopologyChange = _IbmMvsAtmLecTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 8),
    _IbmMvsAtmLecTopologyChange_Type()
)
ibmMvsAtmLecTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecTopologyChange.setStatus("current")


class _IbmMvsAtmLecConfigServerAtmAddress_Type(OctetString):
    """Custom type ibmMvsAtmLecConfigServerAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmMvsAtmLecConfigServerAtmAddress_Type.__name__ = "OctetString"
_IbmMvsAtmLecConfigServerAtmAddress_Object = MibTableColumn
ibmMvsAtmLecConfigServerAtmAddress = _IbmMvsAtmLecConfigServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 9),
    _IbmMvsAtmLecConfigServerAtmAddress_Type()
)
ibmMvsAtmLecConfigServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigServerAtmAddress.setStatus("current")


class _IbmMvsAtmLecConfigSource_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("didNotUseLecs", 4),
          ("gotAddressViaIlmi", 1),
          ("usedLecsPvc", 3),
          ("usedWellKnownAddress", 2))
    )


_IbmMvsAtmLecConfigSource_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigSource_Object = MibTableColumn
ibmMvsAtmLecConfigSource = _IbmMvsAtmLecConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 10),
    _IbmMvsAtmLecConfigSource_Type()
)
ibmMvsAtmLecConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigSource.setStatus("current")


class _IbmMvsAtmLecActualLanType_Type(Integer32):
    """Custom type ibmMvsAtmLecActualLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("tokenRing", 3),
          ("unspecified", 1))
    )


_IbmMvsAtmLecActualLanType_Type.__name__ = "Integer32"
_IbmMvsAtmLecActualLanType_Object = MibTableColumn
ibmMvsAtmLecActualLanType = _IbmMvsAtmLecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 11),
    _IbmMvsAtmLecActualLanType_Type()
)
ibmMvsAtmLecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecActualLanType.setStatus("current")


class _IbmMvsAtmLecActualMaxDataFrameSize_Type(Integer32):
    """Custom type ibmMvsAtmLecActualMaxDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("f1516", 2),
          ("f18190", 5),
          ("f4544", 3),
          ("f9234", 4),
          ("unspecified", 1))
    )


_IbmMvsAtmLecActualMaxDataFrameSize_Type.__name__ = "Integer32"
_IbmMvsAtmLecActualMaxDataFrameSize_Object = MibTableColumn
ibmMvsAtmLecActualMaxDataFrameSize = _IbmMvsAtmLecActualMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 12),
    _IbmMvsAtmLecActualMaxDataFrameSize_Type()
)
ibmMvsAtmLecActualMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecActualMaxDataFrameSize.setStatus("current")


class _IbmMvsAtmLecActualLanName_Type(OctetString):
    """Custom type ibmMvsAtmLecActualLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmMvsAtmLecActualLanName_Type.__name__ = "OctetString"
_IbmMvsAtmLecActualLanName_Object = MibTableColumn
ibmMvsAtmLecActualLanName = _IbmMvsAtmLecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 13),
    _IbmMvsAtmLecActualLanName_Type()
)
ibmMvsAtmLecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecActualLanName.setStatus("current")


class _IbmMvsAtmLecAtmAddress_Type(OctetString):
    """Custom type ibmMvsAtmLecAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmMvsAtmLecAtmAddress_Type.__name__ = "OctetString"
_IbmMvsAtmLecAtmAddress_Object = MibTableColumn
ibmMvsAtmLecAtmAddress = _IbmMvsAtmLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 14),
    _IbmMvsAtmLecAtmAddress_Type()
)
ibmMvsAtmLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecAtmAddress.setStatus("current")


class _IbmMvsAtmLecProxyClient_Type(Integer32):
    """Custom type ibmMvsAtmLecProxyClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IbmMvsAtmLecProxyClient_Type.__name__ = "Integer32"
_IbmMvsAtmLecProxyClient_Object = MibTableColumn
ibmMvsAtmLecProxyClient = _IbmMvsAtmLecProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 6, 1, 15),
    _IbmMvsAtmLecProxyClient_Type()
)
ibmMvsAtmLecProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecProxyClient.setStatus("current")
_IbmMvsAtmLecStatisticsTable_Object = MibTable
ibmMvsAtmLecStatisticsTable = _IbmMvsAtmLecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7)
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecStatisticsTable.setStatus("current")
_IbmMvsAtmLecStatisticsEntry_Object = MibTableRow
ibmMvsAtmLecStatisticsEntry = _IbmMvsAtmLecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1)
)
ibmMvsAtmLecStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecStatisticsEntry.setStatus("current")
_IbmMvsAtmLecArpRequestsOut_Type = Counter32
_IbmMvsAtmLecArpRequestsOut_Object = MibTableColumn
ibmMvsAtmLecArpRequestsOut = _IbmMvsAtmLecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 1),
    _IbmMvsAtmLecArpRequestsOut_Type()
)
ibmMvsAtmLecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecArpRequestsOut.setStatus("current")
_IbmMvsAtmLecArpRequestsIn_Type = Counter32
_IbmMvsAtmLecArpRequestsIn_Object = MibTableColumn
ibmMvsAtmLecArpRequestsIn = _IbmMvsAtmLecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 2),
    _IbmMvsAtmLecArpRequestsIn_Type()
)
ibmMvsAtmLecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecArpRequestsIn.setStatus("current")
_IbmMvsAtmLecArpRepliesOut_Type = Counter32
_IbmMvsAtmLecArpRepliesOut_Object = MibTableColumn
ibmMvsAtmLecArpRepliesOut = _IbmMvsAtmLecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 3),
    _IbmMvsAtmLecArpRepliesOut_Type()
)
ibmMvsAtmLecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecArpRepliesOut.setStatus("current")
_IbmMvsAtmLecArpRepliesIn_Type = Counter32
_IbmMvsAtmLecArpRepliesIn_Object = MibTableColumn
ibmMvsAtmLecArpRepliesIn = _IbmMvsAtmLecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 4),
    _IbmMvsAtmLecArpRepliesIn_Type()
)
ibmMvsAtmLecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecArpRepliesIn.setStatus("current")
_IbmMvsAtmLecControlFramesOut_Type = Counter32
_IbmMvsAtmLecControlFramesOut_Object = MibTableColumn
ibmMvsAtmLecControlFramesOut = _IbmMvsAtmLecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 5),
    _IbmMvsAtmLecControlFramesOut_Type()
)
ibmMvsAtmLecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlFramesOut.setStatus("current")
_IbmMvsAtmLecControlFramesIn_Type = Counter32
_IbmMvsAtmLecControlFramesIn_Object = MibTableColumn
ibmMvsAtmLecControlFramesIn = _IbmMvsAtmLecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 6),
    _IbmMvsAtmLecControlFramesIn_Type()
)
ibmMvsAtmLecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlFramesIn.setStatus("current")
_IbmMvsAtmLecSvcFailures_Type = Counter32
_IbmMvsAtmLecSvcFailures_Object = MibTableColumn
ibmMvsAtmLecSvcFailures = _IbmMvsAtmLecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 7, 1, 7),
    _IbmMvsAtmLecSvcFailures_Type()
)
ibmMvsAtmLecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecSvcFailures.setStatus("current")
_IbmMvsAtmLecServerTable_Object = MibTable
ibmMvsAtmLecServerTable = _IbmMvsAtmLecServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8)
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecServerTable.setStatus("current")
_IbmMvsAtmLecServerEntry_Object = MibTableRow
ibmMvsAtmLecServerEntry = _IbmMvsAtmLecServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1)
)
ibmMvsAtmLecServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecServerEntry.setStatus("current")


class _IbmMvsAtmLecConfigDirectInterface_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigDirectInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmMvsAtmLecConfigDirectInterface_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigDirectInterface_Object = MibTableColumn
ibmMvsAtmLecConfigDirectInterface = _IbmMvsAtmLecConfigDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 1),
    _IbmMvsAtmLecConfigDirectInterface_Type()
)
ibmMvsAtmLecConfigDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigDirectInterface.setStatus("current")


class _IbmMvsAtmLecConfigDirectVPI_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigDirectVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmLecConfigDirectVPI_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigDirectVPI_Object = MibTableColumn
ibmMvsAtmLecConfigDirectVPI = _IbmMvsAtmLecConfigDirectVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 2),
    _IbmMvsAtmLecConfigDirectVPI_Type()
)
ibmMvsAtmLecConfigDirectVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigDirectVPI.setStatus("current")


class _IbmMvsAtmLecConfigDirectVCI_Type(Integer32):
    """Custom type ibmMvsAtmLecConfigDirectVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsAtmLecConfigDirectVCI_Type.__name__ = "Integer32"
_IbmMvsAtmLecConfigDirectVCI_Object = MibTableColumn
ibmMvsAtmLecConfigDirectVCI = _IbmMvsAtmLecConfigDirectVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 3),
    _IbmMvsAtmLecConfigDirectVCI_Type()
)
ibmMvsAtmLecConfigDirectVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecConfigDirectVCI.setStatus("current")


class _IbmMvsAtmLecControlDirectInterface_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDirectInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmMvsAtmLecControlDirectInterface_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDirectInterface_Object = MibTableColumn
ibmMvsAtmLecControlDirectInterface = _IbmMvsAtmLecControlDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 4),
    _IbmMvsAtmLecControlDirectInterface_Type()
)
ibmMvsAtmLecControlDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDirectInterface.setStatus("current")


class _IbmMvsAtmLecControlDirectVPI_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDirectVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmLecControlDirectVPI_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDirectVPI_Object = MibTableColumn
ibmMvsAtmLecControlDirectVPI = _IbmMvsAtmLecControlDirectVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 5),
    _IbmMvsAtmLecControlDirectVPI_Type()
)
ibmMvsAtmLecControlDirectVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDirectVPI.setStatus("current")


class _IbmMvsAtmLecControlDirectVCI_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDirectVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsAtmLecControlDirectVCI_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDirectVCI_Object = MibTableColumn
ibmMvsAtmLecControlDirectVCI = _IbmMvsAtmLecControlDirectVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 6),
    _IbmMvsAtmLecControlDirectVCI_Type()
)
ibmMvsAtmLecControlDirectVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDirectVCI.setStatus("current")


class _IbmMvsAtmLecControlDistributeInterface_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDistributeInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmMvsAtmLecControlDistributeInterface_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDistributeInterface_Object = MibTableColumn
ibmMvsAtmLecControlDistributeInterface = _IbmMvsAtmLecControlDistributeInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 7),
    _IbmMvsAtmLecControlDistributeInterface_Type()
)
ibmMvsAtmLecControlDistributeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDistributeInterface.setStatus("current")


class _IbmMvsAtmLecControlDistributeVPI_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDistributeVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmLecControlDistributeVPI_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDistributeVPI_Object = MibTableColumn
ibmMvsAtmLecControlDistributeVPI = _IbmMvsAtmLecControlDistributeVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 8),
    _IbmMvsAtmLecControlDistributeVPI_Type()
)
ibmMvsAtmLecControlDistributeVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDistributeVPI.setStatus("current")


class _IbmMvsAtmLecControlDistributeVCI_Type(Integer32):
    """Custom type ibmMvsAtmLecControlDistributeVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsAtmLecControlDistributeVCI_Type.__name__ = "Integer32"
_IbmMvsAtmLecControlDistributeVCI_Object = MibTableColumn
ibmMvsAtmLecControlDistributeVCI = _IbmMvsAtmLecControlDistributeVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 9),
    _IbmMvsAtmLecControlDistributeVCI_Type()
)
ibmMvsAtmLecControlDistributeVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecControlDistributeVCI.setStatus("current")


class _IbmMvsAtmLecMulticastSendInterface_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastSendInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmMvsAtmLecMulticastSendInterface_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastSendInterface_Object = MibTableColumn
ibmMvsAtmLecMulticastSendInterface = _IbmMvsAtmLecMulticastSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 10),
    _IbmMvsAtmLecMulticastSendInterface_Type()
)
ibmMvsAtmLecMulticastSendInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendInterface.setStatus("current")


class _IbmMvsAtmLecMulticastSendVPI_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastSendVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmLecMulticastSendVPI_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastSendVPI_Object = MibTableColumn
ibmMvsAtmLecMulticastSendVPI = _IbmMvsAtmLecMulticastSendVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 11),
    _IbmMvsAtmLecMulticastSendVPI_Type()
)
ibmMvsAtmLecMulticastSendVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendVPI.setStatus("current")


class _IbmMvsAtmLecMulticastSendVCI_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastSendVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsAtmLecMulticastSendVCI_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastSendVCI_Object = MibTableColumn
ibmMvsAtmLecMulticastSendVCI = _IbmMvsAtmLecMulticastSendVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 12),
    _IbmMvsAtmLecMulticastSendVCI_Type()
)
ibmMvsAtmLecMulticastSendVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastSendVCI.setStatus("current")


class _IbmMvsAtmLecMulticastFwdInterface_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastFwdInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmMvsAtmLecMulticastFwdInterface_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastFwdInterface_Object = MibTableColumn
ibmMvsAtmLecMulticastFwdInterface = _IbmMvsAtmLecMulticastFwdInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 13),
    _IbmMvsAtmLecMulticastFwdInterface_Type()
)
ibmMvsAtmLecMulticastFwdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastFwdInterface.setStatus("current")


class _IbmMvsAtmLecMulticastFwdVPI_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastFwdVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmMvsAtmLecMulticastFwdVPI_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastFwdVPI_Object = MibTableColumn
ibmMvsAtmLecMulticastFwdVPI = _IbmMvsAtmLecMulticastFwdVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 14),
    _IbmMvsAtmLecMulticastFwdVPI_Type()
)
ibmMvsAtmLecMulticastFwdVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastFwdVPI.setStatus("current")


class _IbmMvsAtmLecMulticastFwdVCI_Type(Integer32):
    """Custom type ibmMvsAtmLecMulticastFwdVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsAtmLecMulticastFwdVCI_Type.__name__ = "Integer32"
_IbmMvsAtmLecMulticastFwdVCI_Object = MibTableColumn
ibmMvsAtmLecMulticastFwdVCI = _IbmMvsAtmLecMulticastFwdVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 8, 1, 15),
    _IbmMvsAtmLecMulticastFwdVCI_Type()
)
ibmMvsAtmLecMulticastFwdVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMulticastFwdVCI.setStatus("current")
_IbmMvsAtmLecMacAddressTable_Object = MibTable
ibmMvsAtmLecMacAddressTable = _IbmMvsAtmLecMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 9)
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecMacAddressTable.setStatus("current")
_IbmMvsAtmLecMacAddressEntry_Object = MibTableRow
ibmMvsAtmLecMacAddressEntry = _IbmMvsAtmLecMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 9, 1)
)
ibmMvsAtmLecMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmMvsAtmLecMacAddressEntry.setStatus("current")


class _IbmMvsAtmLecMacAddress_Type(OctetString):
    """Custom type ibmMvsAtmLecMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsAtmLecMacAddress_Type.__name__ = "OctetString"
_IbmMvsAtmLecMacAddress_Object = MibTableColumn
ibmMvsAtmLecMacAddress = _IbmMvsAtmLecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 6, 9, 1, 1),
    _IbmMvsAtmLecMacAddress_Type()
)
ibmMvsAtmLecMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsAtmLecMacAddress.setStatus("current")
_IbmTcpipMvsTcpGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsTcpGroup = _IbmTcpipMvsTcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7)
)
_IbmTcpipMvsTcpConnTable_Object = MibTable
ibmTcpipMvsTcpConnTable = _IbmTcpipMvsTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsTcpConnTable.setStatus("current")
_IbmTcpipMvsTcpConnEntry_Object = MibTableRow
ibmTcpipMvsTcpConnEntry = _IbmTcpipMvsTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsTcpConnEntry.setStatus("current")


class _IbmMvsTcpConnLastActivity_Type(TimeTicks):
    """Custom type ibmMvsTcpConnLastActivity based on TimeTicks"""
    defaultValue = 0


_IbmMvsTcpConnLastActivity_Object = MibTableColumn
ibmMvsTcpConnLastActivity = _IbmMvsTcpConnLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 1),
    _IbmMvsTcpConnLastActivity_Type()
)
ibmMvsTcpConnLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnLastActivity.setStatus("current")


class _IbmMvsTcpConnBytesIn_Type(Unsigned32):
    """Custom type ibmMvsTcpConnBytesIn based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnBytesIn_Object = MibTableColumn
ibmMvsTcpConnBytesIn = _IbmMvsTcpConnBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 2),
    _IbmMvsTcpConnBytesIn_Type()
)
ibmMvsTcpConnBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnBytesIn.setStatus("current")


class _IbmMvsTcpConnBytesOut_Type(Unsigned32):
    """Custom type ibmMvsTcpConnBytesOut based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnBytesOut_Object = MibTableColumn
ibmMvsTcpConnBytesOut = _IbmMvsTcpConnBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 3),
    _IbmMvsTcpConnBytesOut_Type()
)
ibmMvsTcpConnBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnBytesOut.setStatus("current")


class _IbmMvsTcpConnActiveOpen_Type(Integer32):
    """Custom type ibmMvsTcpConnActiveOpen based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnActiveOpen_Object = MibTableColumn
ibmMvsTcpConnActiveOpen = _IbmMvsTcpConnActiveOpen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 4),
    _IbmMvsTcpConnActiveOpen_Type()
)
ibmMvsTcpConnActiveOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnActiveOpen.setStatus("obsolete")
_IbmMvsTcpConnIpTos_Type = TypeOfService
_IbmMvsTcpConnIpTos_Object = MibTableColumn
ibmMvsTcpConnIpTos = _IbmMvsTcpConnIpTos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 5),
    _IbmMvsTcpConnIpTos_Type()
)
ibmMvsTcpConnIpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnIpTos.setStatus("obsolete")


class _IbmMvsTcpConnOptions_Type(OctetString):
    """Custom type ibmMvsTcpConnOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_IbmMvsTcpConnOptions_Type.__name__ = "OctetString"
_IbmMvsTcpConnOptions_Object = MibTableColumn
ibmMvsTcpConnOptions = _IbmMvsTcpConnOptions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 6),
    _IbmMvsTcpConnOptions_Type()
)
ibmMvsTcpConnOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOptions.setStatus("current")


class _IbmMvsTcpConnOutBuffered_Type(Unsigned32):
    """Custom type ibmMvsTcpConnOutBuffered based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnOutBuffered_Object = MibTableColumn
ibmMvsTcpConnOutBuffered = _IbmMvsTcpConnOutBuffered_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 7),
    _IbmMvsTcpConnOutBuffered_Type()
)
ibmMvsTcpConnOutBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOutBuffered.setStatus("current")
_IbmMvsTcpConnUsrSndNxt_Type = Counter32
_IbmMvsTcpConnUsrSndNxt_Object = MibTableColumn
ibmMvsTcpConnUsrSndNxt = _IbmMvsTcpConnUsrSndNxt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 8),
    _IbmMvsTcpConnUsrSndNxt_Type()
)
ibmMvsTcpConnUsrSndNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnUsrSndNxt.setStatus("current")
_IbmMvsTcpConnSndNxt_Type = Counter32
_IbmMvsTcpConnSndNxt_Object = MibTableColumn
ibmMvsTcpConnSndNxt = _IbmMvsTcpConnSndNxt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 9),
    _IbmMvsTcpConnSndNxt_Type()
)
ibmMvsTcpConnSndNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndNxt.setStatus("current")
_IbmMvsTcpConnSndUna_Type = Counter32
_IbmMvsTcpConnSndUna_Object = MibTableColumn
ibmMvsTcpConnSndUna = _IbmMvsTcpConnSndUna_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 10),
    _IbmMvsTcpConnSndUna_Type()
)
ibmMvsTcpConnSndUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndUna.setStatus("current")
_IbmMvsTcpConnOutgoingPush_Type = Counter32
_IbmMvsTcpConnOutgoingPush_Object = MibTableColumn
ibmMvsTcpConnOutgoingPush = _IbmMvsTcpConnOutgoingPush_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 11),
    _IbmMvsTcpConnOutgoingPush_Type()
)
ibmMvsTcpConnOutgoingPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOutgoingPush.setStatus("current")
_IbmMvsTcpConnOutgoingUrg_Type = Counter32
_IbmMvsTcpConnOutgoingUrg_Object = MibTableColumn
ibmMvsTcpConnOutgoingUrg = _IbmMvsTcpConnOutgoingUrg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 12),
    _IbmMvsTcpConnOutgoingUrg_Type()
)
ibmMvsTcpConnOutgoingUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOutgoingUrg.setStatus("current")
_IbmMvsTcpConnOutgoingWinSeq_Type = Counter32
_IbmMvsTcpConnOutgoingWinSeq_Object = MibTableColumn
ibmMvsTcpConnOutgoingWinSeq = _IbmMvsTcpConnOutgoingWinSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 13),
    _IbmMvsTcpConnOutgoingWinSeq_Type()
)
ibmMvsTcpConnOutgoingWinSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOutgoingWinSeq.setStatus("current")


class _IbmMvsTcpConnSendWindowSeq_Type(Integer32):
    """Custom type ibmMvsTcpConnSendWindowSeq based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnSendWindowSeq_Object = MibTableColumn
ibmMvsTcpConnSendWindowSeq = _IbmMvsTcpConnSendWindowSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 14),
    _IbmMvsTcpConnSendWindowSeq_Type()
)
ibmMvsTcpConnSendWindowSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSendWindowSeq.setStatus("obsolete")


class _IbmMvsTcpConnSendWindowAck_Type(Integer32):
    """Custom type ibmMvsTcpConnSendWindowAck based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnSendWindowAck_Object = MibTableColumn
ibmMvsTcpConnSendWindowAck = _IbmMvsTcpConnSendWindowAck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 15),
    _IbmMvsTcpConnSendWindowAck_Type()
)
ibmMvsTcpConnSendWindowAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSendWindowAck.setStatus("obsolete")


class _IbmMvsTcpConnInBuffered_Type(Unsigned32):
    """Custom type ibmMvsTcpConnInBuffered based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnInBuffered_Object = MibTableColumn
ibmMvsTcpConnInBuffered = _IbmMvsTcpConnInBuffered_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 16),
    _IbmMvsTcpConnInBuffered_Type()
)
ibmMvsTcpConnInBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnInBuffered.setStatus("current")
_IbmMvsTcpConnRcvNxt_Type = Counter32
_IbmMvsTcpConnRcvNxt_Object = MibTableColumn
ibmMvsTcpConnRcvNxt = _IbmMvsTcpConnRcvNxt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 17),
    _IbmMvsTcpConnRcvNxt_Type()
)
ibmMvsTcpConnRcvNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnRcvNxt.setStatus("current")
_IbmMvsTcpConnUsrRcvNxt_Type = Counter32
_IbmMvsTcpConnUsrRcvNxt_Object = MibTableColumn
ibmMvsTcpConnUsrRcvNxt = _IbmMvsTcpConnUsrRcvNxt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 18),
    _IbmMvsTcpConnUsrRcvNxt_Type()
)
ibmMvsTcpConnUsrRcvNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnUsrRcvNxt.setStatus("current")
_IbmMvsTcpConnIncomingPush_Type = Counter32
_IbmMvsTcpConnIncomingPush_Object = MibTableColumn
ibmMvsTcpConnIncomingPush = _IbmMvsTcpConnIncomingPush_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 19),
    _IbmMvsTcpConnIncomingPush_Type()
)
ibmMvsTcpConnIncomingPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnIncomingPush.setStatus("current")
_IbmMvsTcpConnIncomingUrg_Type = Counter32
_IbmMvsTcpConnIncomingUrg_Object = MibTableColumn
ibmMvsTcpConnIncomingUrg = _IbmMvsTcpConnIncomingUrg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 20),
    _IbmMvsTcpConnIncomingUrg_Type()
)
ibmMvsTcpConnIncomingUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnIncomingUrg.setStatus("current")
_IbmMvsTcpConnIncomingWinSeq_Type = Counter32
_IbmMvsTcpConnIncomingWinSeq_Object = MibTableColumn
ibmMvsTcpConnIncomingWinSeq = _IbmMvsTcpConnIncomingWinSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 21),
    _IbmMvsTcpConnIncomingWinSeq_Type()
)
ibmMvsTcpConnIncomingWinSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnIncomingWinSeq.setStatus("current")


class _IbmMvsTcpConnReXmt_Type(Integer32):
    """Custom type ibmMvsTcpConnReXmt based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnReXmt_Object = MibTableColumn
ibmMvsTcpConnReXmt = _IbmMvsTcpConnReXmt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 22),
    _IbmMvsTcpConnReXmt_Type()
)
ibmMvsTcpConnReXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnReXmt.setStatus("current")


class _IbmMvsTcpConnMaxSndWnd_Type(Unsigned32):
    """Custom type ibmMvsTcpConnMaxSndWnd based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnMaxSndWnd_Object = MibTableColumn
ibmMvsTcpConnMaxSndWnd = _IbmMvsTcpConnMaxSndWnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 23),
    _IbmMvsTcpConnMaxSndWnd_Type()
)
ibmMvsTcpConnMaxSndWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnMaxSndWnd.setStatus("current")


class _IbmMvsTcpConnReXmtCount_Type(Integer32):
    """Custom type ibmMvsTcpConnReXmtCount based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnReXmtCount_Object = MibTableColumn
ibmMvsTcpConnReXmtCount = _IbmMvsTcpConnReXmtCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 24),
    _IbmMvsTcpConnReXmtCount_Type()
)
ibmMvsTcpConnReXmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnReXmtCount.setStatus("current")


class _IbmMvsTcpConnCongestionWnd_Type(Unsigned32):
    """Custom type ibmMvsTcpConnCongestionWnd based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnCongestionWnd_Object = MibTableColumn
ibmMvsTcpConnCongestionWnd = _IbmMvsTcpConnCongestionWnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 25),
    _IbmMvsTcpConnCongestionWnd_Type()
)
ibmMvsTcpConnCongestionWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnCongestionWnd.setStatus("current")


class _IbmMvsTcpConnSSThresh_Type(Unsigned32):
    """Custom type ibmMvsTcpConnSSThresh based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnSSThresh_Object = MibTableColumn
ibmMvsTcpConnSSThresh = _IbmMvsTcpConnSSThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 26),
    _IbmMvsTcpConnSSThresh_Type()
)
ibmMvsTcpConnSSThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSSThresh.setStatus("current")


class _IbmMvsTcpConnRoundTripTime_Type(Unsigned32):
    """Custom type ibmMvsTcpConnRoundTripTime based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnRoundTripTime_Object = MibTableColumn
ibmMvsTcpConnRoundTripTime = _IbmMvsTcpConnRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 27),
    _IbmMvsTcpConnRoundTripTime_Type()
)
ibmMvsTcpConnRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnRoundTripTime.setStatus("current")


class _IbmMvsTcpConnRoundTripVariance_Type(Unsigned32):
    """Custom type ibmMvsTcpConnRoundTripVariance based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnRoundTripVariance_Object = MibTableColumn
ibmMvsTcpConnRoundTripVariance = _IbmMvsTcpConnRoundTripVariance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 28),
    _IbmMvsTcpConnRoundTripVariance_Type()
)
ibmMvsTcpConnRoundTripVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnRoundTripVariance.setStatus("current")


class _IbmMvsTcpConnInitSndSeq_Type(Unsigned32):
    """Custom type ibmMvsTcpConnInitSndSeq based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnInitSndSeq_Object = MibTableColumn
ibmMvsTcpConnInitSndSeq = _IbmMvsTcpConnInitSndSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 29),
    _IbmMvsTcpConnInitSndSeq_Type()
)
ibmMvsTcpConnInitSndSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnInitSndSeq.setStatus("current")


class _IbmMvsTcpConnInitRcvSeq_Type(Unsigned32):
    """Custom type ibmMvsTcpConnInitRcvSeq based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnInitRcvSeq_Object = MibTableColumn
ibmMvsTcpConnInitRcvSeq = _IbmMvsTcpConnInitRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 30),
    _IbmMvsTcpConnInitRcvSeq_Type()
)
ibmMvsTcpConnInitRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnInitRcvSeq.setStatus("current")


class _IbmMvsTcpConnSendMSS_Type(Unsigned32):
    """Custom type ibmMvsTcpConnSendMSS based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnSendMSS_Object = MibTableColumn
ibmMvsTcpConnSendMSS = _IbmMvsTcpConnSendMSS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 31),
    _IbmMvsTcpConnSendMSS_Type()
)
ibmMvsTcpConnSendMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSendMSS.setStatus("current")
_IbmMvsTcpConnSndWl1_Type = Counter32
_IbmMvsTcpConnSndWl1_Object = MibTableColumn
ibmMvsTcpConnSndWl1 = _IbmMvsTcpConnSndWl1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 32),
    _IbmMvsTcpConnSndWl1_Type()
)
ibmMvsTcpConnSndWl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndWl1.setStatus("current")
_IbmMvsTcpConnSndWl2_Type = Counter32
_IbmMvsTcpConnSndWl2_Object = MibTableColumn
ibmMvsTcpConnSndWl2 = _IbmMvsTcpConnSndWl2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 33),
    _IbmMvsTcpConnSndWl2_Type()
)
ibmMvsTcpConnSndWl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndWl2.setStatus("current")


class _IbmMvsTcpConnSndWnd_Type(Unsigned32):
    """Custom type ibmMvsTcpConnSndWnd based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnSndWnd_Object = MibTableColumn
ibmMvsTcpConnSndWnd = _IbmMvsTcpConnSndWnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 34),
    _IbmMvsTcpConnSndWnd_Type()
)
ibmMvsTcpConnSndWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndWnd.setStatus("current")


class _IbmMvsTcpConnPendTcpRecv_Type(Integer32):
    """Custom type ibmMvsTcpConnPendTcpRecv based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnPendTcpRecv_Object = MibTableColumn
ibmMvsTcpConnPendTcpRecv = _IbmMvsTcpConnPendTcpRecv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 35),
    _IbmMvsTcpConnPendTcpRecv_Type()
)
ibmMvsTcpConnPendTcpRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnPendTcpRecv.setStatus("obsolete")


class _IbmMvsTcpConnRcvBufSize_Type(Unsigned32):
    """Custom type ibmMvsTcpConnRcvBufSize based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnRcvBufSize_Object = MibTableColumn
ibmMvsTcpConnRcvBufSize = _IbmMvsTcpConnRcvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 36),
    _IbmMvsTcpConnRcvBufSize_Type()
)
ibmMvsTcpConnRcvBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnRcvBufSize.setStatus("current")


class _IbmMvsTcpConnResourceName_Type(DisplayString):
    """Custom type ibmMvsTcpConnResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpConnResourceName_Type.__name__ = "DisplayString"
_IbmMvsTcpConnResourceName_Object = MibTableColumn
ibmMvsTcpConnResourceName = _IbmMvsTcpConnResourceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 37),
    _IbmMvsTcpConnResourceName_Type()
)
ibmMvsTcpConnResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnResourceName.setStatus("current")


class _IbmMvsTcpConnSubtask_Type(Unsigned32):
    """Custom type ibmMvsTcpConnSubtask based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnSubtask_Object = MibTableColumn
ibmMvsTcpConnSubtask = _IbmMvsTcpConnSubtask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 38),
    _IbmMvsTcpConnSubtask_Type()
)
ibmMvsTcpConnSubtask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSubtask.setStatus("current")


class _IbmMvsTcpConnResourceId_Type(Unsigned32):
    """Custom type ibmMvsTcpConnResourceId based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnResourceId_Object = MibTableColumn
ibmMvsTcpConnResourceId = _IbmMvsTcpConnResourceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 39),
    _IbmMvsTcpConnResourceId_Type()
)
ibmMvsTcpConnResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnResourceId.setStatus("current")


class _IbmMvsTcpConnSockOpt_Type(OctetString):
    """Custom type ibmMvsTcpConnSockOpt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnSockOpt_Type.__name__ = "OctetString"
_IbmMvsTcpConnSockOpt_Object = MibTableColumn
ibmMvsTcpConnSockOpt = _IbmMvsTcpConnSockOpt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 40),
    _IbmMvsTcpConnSockOpt_Type()
)
ibmMvsTcpConnSockOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSockOpt.setStatus("current")


class _IbmMvsTcpConnTcpTimer_Type(OctetString):
    """Custom type ibmMvsTcpConnTcpTimer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnTcpTimer_Type.__name__ = "OctetString"
_IbmMvsTcpConnTcpTimer_Object = MibTableColumn
ibmMvsTcpConnTcpTimer = _IbmMvsTcpConnTcpTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 41),
    _IbmMvsTcpConnTcpTimer_Type()
)
ibmMvsTcpConnTcpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTcpTimer.setStatus("obsolete")


class _IbmMvsTcpConnTcpSig_Type(OctetString):
    """Custom type ibmMvsTcpConnTcpSig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnTcpSig_Type.__name__ = "OctetString"
_IbmMvsTcpConnTcpSig_Object = MibTableColumn
ibmMvsTcpConnTcpSig = _IbmMvsTcpConnTcpSig_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 42),
    _IbmMvsTcpConnTcpSig_Type()
)
ibmMvsTcpConnTcpSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTcpSig.setStatus("obsolete")


class _IbmMvsTcpConnTcpSel_Type(OctetString):
    """Custom type ibmMvsTcpConnTcpSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnTcpSel_Type.__name__ = "OctetString"
_IbmMvsTcpConnTcpSel_Object = MibTableColumn
ibmMvsTcpConnTcpSel = _IbmMvsTcpConnTcpSel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 43),
    _IbmMvsTcpConnTcpSel_Type()
)
ibmMvsTcpConnTcpSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTcpSel.setStatus("obsolete")
_IbmMvsTcpConnRttSeq_Type = Counter32
_IbmMvsTcpConnRttSeq_Object = MibTableColumn
ibmMvsTcpConnRttSeq = _IbmMvsTcpConnRttSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 44),
    _IbmMvsTcpConnRttSeq_Type()
)
ibmMvsTcpConnRttSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnRttSeq.setStatus("current")


class _IbmMvsTcpConnBackoffCount_Type(Integer32):
    """Custom type ibmMvsTcpConnBackoffCount based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnBackoffCount_Object = MibTableColumn
ibmMvsTcpConnBackoffCount = _IbmMvsTcpConnBackoffCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 45),
    _IbmMvsTcpConnBackoffCount_Type()
)
ibmMvsTcpConnBackoffCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnBackoffCount.setStatus("obsolete")


class _IbmMvsTcpConnTcpDet_Type(OctetString):
    """Custom type ibmMvsTcpConnTcpDet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnTcpDet_Type.__name__ = "OctetString"
_IbmMvsTcpConnTcpDet_Object = MibTableColumn
ibmMvsTcpConnTcpDet = _IbmMvsTcpConnTcpDet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 46),
    _IbmMvsTcpConnTcpDet_Type()
)
ibmMvsTcpConnTcpDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTcpDet.setStatus("obsolete")


class _IbmMvsTcpConnTcpPol_Type(OctetString):
    """Custom type ibmMvsTcpConnTcpPol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnTcpPol_Type.__name__ = "OctetString"
_IbmMvsTcpConnTcpPol_Object = MibTableColumn
ibmMvsTcpConnTcpPol = _IbmMvsTcpConnTcpPol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 47),
    _IbmMvsTcpConnTcpPol_Type()
)
ibmMvsTcpConnTcpPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTcpPol.setStatus("obsolete")


class _IbmMvsTcpConnTargetAppl_Type(DisplayString):
    """Custom type ibmMvsTcpConnTargetAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpConnTargetAppl_Type.__name__ = "DisplayString"
_IbmMvsTcpConnTargetAppl_Object = MibTableColumn
ibmMvsTcpConnTargetAppl = _IbmMvsTcpConnTargetAppl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 48),
    _IbmMvsTcpConnTargetAppl_Type()
)
ibmMvsTcpConnTargetAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTargetAppl.setStatus("current")


class _IbmMvsTcpConnLuName_Type(DisplayString):
    """Custom type ibmMvsTcpConnLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpConnLuName_Type.__name__ = "DisplayString"
_IbmMvsTcpConnLuName_Object = MibTableColumn
ibmMvsTcpConnLuName = _IbmMvsTcpConnLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 49),
    _IbmMvsTcpConnLuName_Type()
)
ibmMvsTcpConnLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnLuName.setStatus("current")


class _IbmMvsTcpConnClientUserId_Type(DisplayString):
    """Custom type ibmMvsTcpConnClientUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpConnClientUserId_Type.__name__ = "DisplayString"
_IbmMvsTcpConnClientUserId_Object = MibTableColumn
ibmMvsTcpConnClientUserId = _IbmMvsTcpConnClientUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 50),
    _IbmMvsTcpConnClientUserId_Type()
)
ibmMvsTcpConnClientUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnClientUserId.setStatus("current")


class _IbmMvsTcpConnLogMode_Type(DisplayString):
    """Custom type ibmMvsTcpConnLogMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpConnLogMode_Type.__name__ = "DisplayString"
_IbmMvsTcpConnLogMode_Object = MibTableColumn
ibmMvsTcpConnLogMode = _IbmMvsTcpConnLogMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 51),
    _IbmMvsTcpConnLogMode_Type()
)
ibmMvsTcpConnLogMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnLogMode.setStatus("current")


class _IbmMvsTcpConnProto_Type(OctetString):
    """Custom type ibmMvsTcpConnProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnProto_Type.__name__ = "OctetString"
_IbmMvsTcpConnProto_Object = MibTableColumn
ibmMvsTcpConnProto = _IbmMvsTcpConnProto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 52),
    _IbmMvsTcpConnProto_Type()
)
ibmMvsTcpConnProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnProto.setStatus("current")


class _IbmMvsTcpConnDupacks_Type(Unsigned32):
    """Custom type ibmMvsTcpConnDupacks based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnDupacks_Object = MibTableColumn
ibmMvsTcpConnDupacks = _IbmMvsTcpConnDupacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 53),
    _IbmMvsTcpConnDupacks_Type()
)
ibmMvsTcpConnDupacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnDupacks.setStatus("current")


class _IbmMvsTcpConnOptMaxSegmentSize_Type(Integer32):
    """Custom type ibmMvsTcpConnOptMaxSegmentSize based on Integer32"""
    defaultValue = 0


_IbmMvsTcpConnOptMaxSegmentSize_Object = MibTableColumn
ibmMvsTcpConnOptMaxSegmentSize = _IbmMvsTcpConnOptMaxSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 54),
    _IbmMvsTcpConnOptMaxSegmentSize_Type()
)
ibmMvsTcpConnOptMaxSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOptMaxSegmentSize.setStatus("current")


class _IbmMvsTcpConnClusterConnFlag_Type(OctetString):
    """Custom type ibmMvsTcpConnClusterConnFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnClusterConnFlag_Type.__name__ = "OctetString"
_IbmMvsTcpConnClusterConnFlag_Object = MibTableColumn
ibmMvsTcpConnClusterConnFlag = _IbmMvsTcpConnClusterConnFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 55),
    _IbmMvsTcpConnClusterConnFlag_Type()
)
ibmMvsTcpConnClusterConnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnClusterConnFlag.setStatus("current")
_IbmMvsTcpConnInSegs_Type = Counter32
_IbmMvsTcpConnInSegs_Object = MibTableColumn
ibmMvsTcpConnInSegs = _IbmMvsTcpConnInSegs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 56),
    _IbmMvsTcpConnInSegs_Type()
)
ibmMvsTcpConnInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnInSegs.setStatus("current")
_IbmMvsTcpConnOutSegs_Type = Counter32
_IbmMvsTcpConnOutSegs_Object = MibTableColumn
ibmMvsTcpConnOutSegs = _IbmMvsTcpConnOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 57),
    _IbmMvsTcpConnOutSegs_Type()
)
ibmMvsTcpConnOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnOutSegs.setStatus("current")


class _IbmMvsTcpConnDSField_Type(OctetString):
    """Custom type ibmMvsTcpConnDSField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsTcpConnDSField_Type.__name__ = "OctetString"
_IbmMvsTcpConnDSField_Object = MibTableColumn
ibmMvsTcpConnDSField = _IbmMvsTcpConnDSField_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 58),
    _IbmMvsTcpConnDSField_Type()
)
ibmMvsTcpConnDSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnDSField.setStatus("current")


class _IbmMvsTcpConnSndBufSize_Type(Unsigned32):
    """Custom type ibmMvsTcpConnSndBufSize based on Unsigned32"""
    defaultValue = 0


_IbmMvsTcpConnSndBufSize_Object = MibTableColumn
ibmMvsTcpConnSndBufSize = _IbmMvsTcpConnSndBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 59),
    _IbmMvsTcpConnSndBufSize_Type()
)
ibmMvsTcpConnSndBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnSndBufSize.setStatus("current")
_IbmMvsTcpConnAcceptCount_Type = Counter32
_IbmMvsTcpConnAcceptCount_Object = MibTableColumn
ibmMvsTcpConnAcceptCount = _IbmMvsTcpConnAcceptCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 60),
    _IbmMvsTcpConnAcceptCount_Type()
)
ibmMvsTcpConnAcceptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnAcceptCount.setStatus("current")
_IbmMvsTcpConnExceedBacklog_Type = Integer32
_IbmMvsTcpConnExceedBacklog_Object = MibTableColumn
ibmMvsTcpConnExceedBacklog = _IbmMvsTcpConnExceedBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 61),
    _IbmMvsTcpConnExceedBacklog_Type()
)
ibmMvsTcpConnExceedBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnExceedBacklog.setStatus("current")
_IbmMvsTcpConnCurrBacklog_Type = Integer32
_IbmMvsTcpConnCurrBacklog_Object = MibTableColumn
ibmMvsTcpConnCurrBacklog = _IbmMvsTcpConnCurrBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 62),
    _IbmMvsTcpConnCurrBacklog_Type()
)
ibmMvsTcpConnCurrBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnCurrBacklog.setStatus("current")
_IbmMvsTcpConnMaxBacklog_Type = Integer32
_IbmMvsTcpConnMaxBacklog_Object = MibTableColumn
ibmMvsTcpConnMaxBacklog = _IbmMvsTcpConnMaxBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 63),
    _IbmMvsTcpConnMaxBacklog_Type()
)
ibmMvsTcpConnMaxBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnMaxBacklog.setStatus("current")
_IbmMvsTcpConnWindowScale_Type = TruthValue
_IbmMvsTcpConnWindowScale_Object = MibTableColumn
ibmMvsTcpConnWindowScale = _IbmMvsTcpConnWindowScale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 64),
    _IbmMvsTcpConnWindowScale_Type()
)
ibmMvsTcpConnWindowScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnWindowScale.setStatus("current")
_IbmMvsTcpConnTimeStamp_Type = TruthValue
_IbmMvsTcpConnTimeStamp_Object = MibTableColumn
ibmMvsTcpConnTimeStamp = _IbmMvsTcpConnTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 65),
    _IbmMvsTcpConnTimeStamp_Type()
)
ibmMvsTcpConnTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnTimeStamp.setStatus("current")
_IbmMvsTcpConnServerResourceId_Type = Unsigned32
_IbmMvsTcpConnServerResourceId_Object = MibTableColumn
ibmMvsTcpConnServerResourceId = _IbmMvsTcpConnServerResourceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 1, 1, 66),
    _IbmMvsTcpConnServerResourceId_Type()
)
ibmMvsTcpConnServerResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnServerResourceId.setStatus("current")
_IbmMvsTcpConnsClosed_Type = Counter32
_IbmMvsTcpConnsClosed_Object = MibScalar
ibmMvsTcpConnsClosed = _IbmMvsTcpConnsClosed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 2),
    _IbmMvsTcpConnsClosed_Type()
)
ibmMvsTcpConnsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpConnsClosed.setStatus("current")
_IbmMvsTcpPassiveDrops_Type = Counter32
_IbmMvsTcpPassiveDrops_Object = MibScalar
ibmMvsTcpPassiveDrops = _IbmMvsTcpPassiveDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 3),
    _IbmMvsTcpPassiveDrops_Type()
)
ibmMvsTcpPassiveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpPassiveDrops.setStatus("current")
_IbmMvsTcpTimeWaitReused_Type = Counter32
_IbmMvsTcpTimeWaitReused_Object = MibScalar
ibmMvsTcpTimeWaitReused = _IbmMvsTcpTimeWaitReused_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 4),
    _IbmMvsTcpTimeWaitReused_Type()
)
ibmMvsTcpTimeWaitReused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpTimeWaitReused.setStatus("current")
_IbmMvsTcpPredictAck_Type = Counter32
_IbmMvsTcpPredictAck_Object = MibScalar
ibmMvsTcpPredictAck = _IbmMvsTcpPredictAck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 5),
    _IbmMvsTcpPredictAck_Type()
)
ibmMvsTcpPredictAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpPredictAck.setStatus("current")
_IbmMvsTcpPredictData_Type = Counter32
_IbmMvsTcpPredictData_Object = MibScalar
ibmMvsTcpPredictData = _IbmMvsTcpPredictData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 6),
    _IbmMvsTcpPredictData_Type()
)
ibmMvsTcpPredictData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpPredictData.setStatus("current")
_IbmMvsTcpInDupAck_Type = Counter32
_IbmMvsTcpInDupAck_Object = MibScalar
ibmMvsTcpInDupAck = _IbmMvsTcpInDupAck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 7),
    _IbmMvsTcpInDupAck_Type()
)
ibmMvsTcpInDupAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInDupAck.setStatus("current")
_IbmMvsTcpInBadSum_Type = Counter32
_IbmMvsTcpInBadSum_Object = MibScalar
ibmMvsTcpInBadSum = _IbmMvsTcpInBadSum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 8),
    _IbmMvsTcpInBadSum_Type()
)
ibmMvsTcpInBadSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInBadSum.setStatus("current")
_IbmMvsTcpInBadLen_Type = Counter32
_IbmMvsTcpInBadLen_Object = MibScalar
ibmMvsTcpInBadLen = _IbmMvsTcpInBadLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 9),
    _IbmMvsTcpInBadLen_Type()
)
ibmMvsTcpInBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInBadLen.setStatus("current")
_IbmMvsTcpInShort_Type = Counter32
_IbmMvsTcpInShort_Object = MibScalar
ibmMvsTcpInShort = _IbmMvsTcpInShort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 10),
    _IbmMvsTcpInShort_Type()
)
ibmMvsTcpInShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInShort.setStatus("current")
_IbmMvsTcpInPawsDrop_Type = Counter32
_IbmMvsTcpInPawsDrop_Object = MibScalar
ibmMvsTcpInPawsDrop = _IbmMvsTcpInPawsDrop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 11),
    _IbmMvsTcpInPawsDrop_Type()
)
ibmMvsTcpInPawsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInPawsDrop.setStatus("current")
_IbmMvsTcpInAllBeforeWin_Type = Counter32
_IbmMvsTcpInAllBeforeWin_Object = MibScalar
ibmMvsTcpInAllBeforeWin = _IbmMvsTcpInAllBeforeWin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 12),
    _IbmMvsTcpInAllBeforeWin_Type()
)
ibmMvsTcpInAllBeforeWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInAllBeforeWin.setStatus("current")
_IbmMvsTcpInSomeBeforeWin_Type = Counter32
_IbmMvsTcpInSomeBeforeWin_Object = MibScalar
ibmMvsTcpInSomeBeforeWin = _IbmMvsTcpInSomeBeforeWin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 13),
    _IbmMvsTcpInSomeBeforeWin_Type()
)
ibmMvsTcpInSomeBeforeWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInSomeBeforeWin.setStatus("current")
_IbmMvsTcpInAllAfterWin_Type = Counter32
_IbmMvsTcpInAllAfterWin_Object = MibScalar
ibmMvsTcpInAllAfterWin = _IbmMvsTcpInAllAfterWin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 14),
    _IbmMvsTcpInAllAfterWin_Type()
)
ibmMvsTcpInAllAfterWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInAllAfterWin.setStatus("current")
_IbmMvsTcpInSomeAfterWin_Type = Counter32
_IbmMvsTcpInSomeAfterWin_Object = MibScalar
ibmMvsTcpInSomeAfterWin = _IbmMvsTcpInSomeAfterWin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 15),
    _IbmMvsTcpInSomeAfterWin_Type()
)
ibmMvsTcpInSomeAfterWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInSomeAfterWin.setStatus("current")
_IbmMvsTcpInOutOfOrder_Type = Counter32
_IbmMvsTcpInOutOfOrder_Object = MibScalar
ibmMvsTcpInOutOfOrder = _IbmMvsTcpInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 16),
    _IbmMvsTcpInOutOfOrder_Type()
)
ibmMvsTcpInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInOutOfOrder.setStatus("current")
_IbmMvsTcpInAfterClose_Type = Counter32
_IbmMvsTcpInAfterClose_Object = MibScalar
ibmMvsTcpInAfterClose = _IbmMvsTcpInAfterClose_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 17),
    _IbmMvsTcpInAfterClose_Type()
)
ibmMvsTcpInAfterClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInAfterClose.setStatus("current")
_IbmMvsTcpInWinProbes_Type = Counter32
_IbmMvsTcpInWinProbes_Object = MibScalar
ibmMvsTcpInWinProbes = _IbmMvsTcpInWinProbes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 18),
    _IbmMvsTcpInWinProbes_Type()
)
ibmMvsTcpInWinProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInWinProbes.setStatus("current")
_IbmMvsTcpInWinUpdates_Type = Counter32
_IbmMvsTcpInWinUpdates_Object = MibScalar
ibmMvsTcpInWinUpdates = _IbmMvsTcpInWinUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 19),
    _IbmMvsTcpInWinUpdates_Type()
)
ibmMvsTcpInWinUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpInWinUpdates.setStatus("current")
_IbmMvsTcpOutWinUpdates_Type = Counter32
_IbmMvsTcpOutWinUpdates_Object = MibScalar
ibmMvsTcpOutWinUpdates = _IbmMvsTcpOutWinUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 20),
    _IbmMvsTcpOutWinUpdates_Type()
)
ibmMvsTcpOutWinUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpOutWinUpdates.setStatus("current")
_IbmMvsTcpOutDelayAcks_Type = Counter32
_IbmMvsTcpOutDelayAcks_Object = MibScalar
ibmMvsTcpOutDelayAcks = _IbmMvsTcpOutDelayAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 21),
    _IbmMvsTcpOutDelayAcks_Type()
)
ibmMvsTcpOutDelayAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpOutDelayAcks.setStatus("current")
_IbmMvsTcpOutWinProbes_Type = Counter32
_IbmMvsTcpOutWinProbes_Object = MibScalar
ibmMvsTcpOutWinProbes = _IbmMvsTcpOutWinProbes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 22),
    _IbmMvsTcpOutWinProbes_Type()
)
ibmMvsTcpOutWinProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpOutWinProbes.setStatus("current")
_IbmMvsTcpRxmtTimers_Type = Counter32
_IbmMvsTcpRxmtTimers_Object = MibScalar
ibmMvsTcpRxmtTimers = _IbmMvsTcpRxmtTimers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 23),
    _IbmMvsTcpRxmtTimers_Type()
)
ibmMvsTcpRxmtTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpRxmtTimers.setStatus("current")
_IbmMvsTcpRxmtDrops_Type = Counter32
_IbmMvsTcpRxmtDrops_Object = MibScalar
ibmMvsTcpRxmtDrops = _IbmMvsTcpRxmtDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 24),
    _IbmMvsTcpRxmtDrops_Type()
)
ibmMvsTcpRxmtDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpRxmtDrops.setStatus("current")
_IbmMvsTcpPMTURxmts_Type = Counter32
_IbmMvsTcpPMTURxmts_Object = MibScalar
ibmMvsTcpPMTURxmts = _IbmMvsTcpPMTURxmts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 25),
    _IbmMvsTcpPMTURxmts_Type()
)
ibmMvsTcpPMTURxmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpPMTURxmts.setStatus("current")
_IbmMvsTcpPMTUErrors_Type = Counter32
_IbmMvsTcpPMTUErrors_Object = MibScalar
ibmMvsTcpPMTUErrors = _IbmMvsTcpPMTUErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 26),
    _IbmMvsTcpPMTUErrors_Type()
)
ibmMvsTcpPMTUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpPMTUErrors.setStatus("current")
_IbmMvsTcpProbeDrops_Type = Counter32
_IbmMvsTcpProbeDrops_Object = MibScalar
ibmMvsTcpProbeDrops = _IbmMvsTcpProbeDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 27),
    _IbmMvsTcpProbeDrops_Type()
)
ibmMvsTcpProbeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpProbeDrops.setStatus("current")
_IbmMvsTcpKeepAliveProbes_Type = Counter32
_IbmMvsTcpKeepAliveProbes_Object = MibScalar
ibmMvsTcpKeepAliveProbes = _IbmMvsTcpKeepAliveProbes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 28),
    _IbmMvsTcpKeepAliveProbes_Type()
)
ibmMvsTcpKeepAliveProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpKeepAliveProbes.setStatus("current")
_IbmMvsTcpKeepAliveDrops_Type = Counter32
_IbmMvsTcpKeepAliveDrops_Object = MibScalar
ibmMvsTcpKeepAliveDrops = _IbmMvsTcpKeepAliveDrops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 29),
    _IbmMvsTcpKeepAliveDrops_Type()
)
ibmMvsTcpKeepAliveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpKeepAliveDrops.setStatus("current")
_IbmMvsTcpFinwait2Drops_Type = Counter32
_IbmMvsTcpFinwait2Drops_Object = MibScalar
ibmMvsTcpFinwait2Drops = _IbmMvsTcpFinwait2Drops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 30),
    _IbmMvsTcpFinwait2Drops_Type()
)
ibmMvsTcpFinwait2Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpFinwait2Drops.setStatus("current")
_IbmTcpipMvsTcpListenerTable_Object = MibTable
ibmTcpipMvsTcpListenerTable = _IbmTcpipMvsTcpListenerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsTcpListenerTable.setStatus("current")
_IbmTcpipMvsTcpListenerEntry_Object = MibTableRow
ibmTcpipMvsTcpListenerEntry = _IbmTcpipMvsTcpListenerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1)
)
ibmTcpipMvsTcpListenerEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsTcpListenerResourceId"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsTcpListenerEntry.setStatus("current")
_IbmMvsTcpListenerResourceId_Type = Unsigned32
_IbmMvsTcpListenerResourceId_Object = MibTableColumn
ibmMvsTcpListenerResourceId = _IbmMvsTcpListenerResourceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 1),
    _IbmMvsTcpListenerResourceId_Type()
)
ibmMvsTcpListenerResourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerResourceId.setStatus("current")
_IbmMvsTcpListenerLocalAddrType_Type = InetAddressType
_IbmMvsTcpListenerLocalAddrType_Object = MibTableColumn
ibmMvsTcpListenerLocalAddrType = _IbmMvsTcpListenerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 2),
    _IbmMvsTcpListenerLocalAddrType_Type()
)
ibmMvsTcpListenerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerLocalAddrType.setStatus("current")


class _IbmMvsTcpListenerLocalAddr_Type(InetAddress):
    """Custom type ibmMvsTcpListenerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsTcpListenerLocalAddr_Type.__name__ = "InetAddress"
_IbmMvsTcpListenerLocalAddr_Object = MibTableColumn
ibmMvsTcpListenerLocalAddr = _IbmMvsTcpListenerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 3),
    _IbmMvsTcpListenerLocalAddr_Type()
)
ibmMvsTcpListenerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerLocalAddr.setStatus("current")


class _IbmMvsTcpListenerLocalPort_Type(Integer32):
    """Custom type ibmMvsTcpListenerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsTcpListenerLocalPort_Type.__name__ = "Integer32"
_IbmMvsTcpListenerLocalPort_Object = MibTableColumn
ibmMvsTcpListenerLocalPort = _IbmMvsTcpListenerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 4),
    _IbmMvsTcpListenerLocalPort_Type()
)
ibmMvsTcpListenerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerLocalPort.setStatus("current")
_IbmMvsTcpListenerRemoteAddrType_Type = InetAddressType
_IbmMvsTcpListenerRemoteAddrType_Object = MibTableColumn
ibmMvsTcpListenerRemoteAddrType = _IbmMvsTcpListenerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 5),
    _IbmMvsTcpListenerRemoteAddrType_Type()
)
ibmMvsTcpListenerRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerRemoteAddrType.setStatus("current")


class _IbmMvsTcpListenerRemoteAddr_Type(InetAddress):
    """Custom type ibmMvsTcpListenerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsTcpListenerRemoteAddr_Type.__name__ = "InetAddress"
_IbmMvsTcpListenerRemoteAddr_Object = MibTableColumn
ibmMvsTcpListenerRemoteAddr = _IbmMvsTcpListenerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 6),
    _IbmMvsTcpListenerRemoteAddr_Type()
)
ibmMvsTcpListenerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerRemoteAddr.setStatus("current")


class _IbmMvsTcpListenerRemotePort_Type(Integer32):
    """Custom type ibmMvsTcpListenerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsTcpListenerRemotePort_Type.__name__ = "Integer32"
_IbmMvsTcpListenerRemotePort_Object = MibTableColumn
ibmMvsTcpListenerRemotePort = _IbmMvsTcpListenerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 7),
    _IbmMvsTcpListenerRemotePort_Type()
)
ibmMvsTcpListenerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerRemotePort.setStatus("current")
_IbmMvsTcpListenerAcceptCount_Type = Counter32
_IbmMvsTcpListenerAcceptCount_Object = MibTableColumn
ibmMvsTcpListenerAcceptCount = _IbmMvsTcpListenerAcceptCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 8),
    _IbmMvsTcpListenerAcceptCount_Type()
)
ibmMvsTcpListenerAcceptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerAcceptCount.setStatus("current")
_IbmMvsTcpListenerExceedBacklog_Type = Integer32
_IbmMvsTcpListenerExceedBacklog_Object = MibTableColumn
ibmMvsTcpListenerExceedBacklog = _IbmMvsTcpListenerExceedBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 9),
    _IbmMvsTcpListenerExceedBacklog_Type()
)
ibmMvsTcpListenerExceedBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerExceedBacklog.setStatus("current")
_IbmMvsTcpListenerCurrBacklog_Type = Integer32
_IbmMvsTcpListenerCurrBacklog_Object = MibTableColumn
ibmMvsTcpListenerCurrBacklog = _IbmMvsTcpListenerCurrBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 10),
    _IbmMvsTcpListenerCurrBacklog_Type()
)
ibmMvsTcpListenerCurrBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerCurrBacklog.setStatus("current")
_IbmMvsTcpListenerMaxBacklog_Type = Integer32
_IbmMvsTcpListenerMaxBacklog_Object = MibTableColumn
ibmMvsTcpListenerMaxBacklog = _IbmMvsTcpListenerMaxBacklog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 11),
    _IbmMvsTcpListenerMaxBacklog_Type()
)
ibmMvsTcpListenerMaxBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerMaxBacklog.setStatus("current")


class _IbmMvsTcpListenerResourceName_Type(SnmpAdminString):
    """Custom type ibmMvsTcpListenerResourceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsTcpListenerResourceName_Type.__name__ = "SnmpAdminString"
_IbmMvsTcpListenerResourceName_Object = MibTableColumn
ibmMvsTcpListenerResourceName = _IbmMvsTcpListenerResourceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 7, 31, 1, 12),
    _IbmMvsTcpListenerResourceName_Type()
)
ibmMvsTcpListenerResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsTcpListenerResourceName.setStatus("current")
_IbmTcpipMvsUdpGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsUdpGroup = _IbmTcpipMvsUdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8)
)
_IbmTcpipMvsUdpTable_Object = MibTable
ibmTcpipMvsUdpTable = _IbmTcpipMvsUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsUdpTable.setStatus("current")
_IbmTcpipMvsUdpEntry_Object = MibTableRow
ibmTcpipMvsUdpEntry = _IbmTcpipMvsUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsUdpEntry.setStatus("current")


class _IbmMvsUdpLastAct_Type(TimeTicks):
    """Custom type ibmMvsUdpLastAct based on TimeTicks"""
    defaultValue = 0


_IbmMvsUdpLastAct_Object = MibTableColumn
ibmMvsUdpLastAct = _IbmMvsUdpLastAct_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 1),
    _IbmMvsUdpLastAct_Type()
)
ibmMvsUdpLastAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpLastAct.setStatus("current")


class _IbmMvsUdpTos_Type(TypeOfService):
    """Custom type ibmMvsUdpTos based on TypeOfService"""
    defaultValue = 0


_IbmMvsUdpTos_Object = MibTableColumn
ibmMvsUdpTos = _IbmMvsUdpTos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 2),
    _IbmMvsUdpTos_Type()
)
ibmMvsUdpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpTos.setStatus("obsolete")


class _IbmMvsUdpIpOpts_Type(OctetString):
    """Custom type ibmMvsUdpIpOpts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmMvsUdpIpOpts_Type.__name__ = "OctetString"
_IbmMvsUdpIpOpts_Object = MibTableColumn
ibmMvsUdpIpOpts = _IbmMvsUdpIpOpts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 3),
    _IbmMvsUdpIpOpts_Type()
)
ibmMvsUdpIpOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpIpOpts.setStatus("current")
_IbmMvsUdpDgramIn_Type = Counter32
_IbmMvsUdpDgramIn_Object = MibTableColumn
ibmMvsUdpDgramIn = _IbmMvsUdpDgramIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 4),
    _IbmMvsUdpDgramIn_Type()
)
ibmMvsUdpDgramIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpDgramIn.setStatus("current")
_IbmMvsUdpBytesIn_Type = Counter32
_IbmMvsUdpBytesIn_Object = MibTableColumn
ibmMvsUdpBytesIn = _IbmMvsUdpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 5),
    _IbmMvsUdpBytesIn_Type()
)
ibmMvsUdpBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpBytesIn.setStatus("current")
_IbmMvsUdpDgramOut_Type = Counter32
_IbmMvsUdpDgramOut_Object = MibTableColumn
ibmMvsUdpDgramOut = _IbmMvsUdpDgramOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 6),
    _IbmMvsUdpDgramOut_Type()
)
ibmMvsUdpDgramOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpDgramOut.setStatus("current")
_IbmMvsUdpBytesOut_Type = Counter32
_IbmMvsUdpBytesOut_Object = MibTableColumn
ibmMvsUdpBytesOut = _IbmMvsUdpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 7),
    _IbmMvsUdpBytesOut_Type()
)
ibmMvsUdpBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpBytesOut.setStatus("current")


class _IbmMvsUdpResourceName_Type(DisplayString):
    """Custom type ibmMvsUdpResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsUdpResourceName_Type.__name__ = "DisplayString"
_IbmMvsUdpResourceName_Object = MibTableColumn
ibmMvsUdpResourceName = _IbmMvsUdpResourceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 8),
    _IbmMvsUdpResourceName_Type()
)
ibmMvsUdpResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpResourceName.setStatus("current")


class _IbmMvsUdpSubtask_Type(Unsigned32):
    """Custom type ibmMvsUdpSubtask based on Unsigned32"""
    defaultValue = 0


_IbmMvsUdpSubtask_Object = MibTableColumn
ibmMvsUdpSubtask = _IbmMvsUdpSubtask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 9),
    _IbmMvsUdpSubtask_Type()
)
ibmMvsUdpSubtask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpSubtask.setStatus("current")


class _IbmMvsUdpResourceId_Type(Unsigned32):
    """Custom type ibmMvsUdpResourceId based on Unsigned32"""
    defaultValue = 0


_IbmMvsUdpResourceId_Object = MibTableColumn
ibmMvsUdpResourceId = _IbmMvsUdpResourceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 10),
    _IbmMvsUdpResourceId_Type()
)
ibmMvsUdpResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpResourceId.setStatus("current")


class _IbmMvsUdpSockOpt_Type(OctetString):
    """Custom type ibmMvsUdpSockOpt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsUdpSockOpt_Type.__name__ = "OctetString"
_IbmMvsUdpSockOpt_Object = MibTableColumn
ibmMvsUdpSockOpt = _IbmMvsUdpSockOpt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 11),
    _IbmMvsUdpSockOpt_Type()
)
ibmMvsUdpSockOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpSockOpt.setStatus("current")


class _IbmMvsUdpSendLim_Type(Unsigned32):
    """Custom type ibmMvsUdpSendLim based on Unsigned32"""
    defaultValue = 0


_IbmMvsUdpSendLim_Object = MibTableColumn
ibmMvsUdpSendLim = _IbmMvsUdpSendLim_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 12),
    _IbmMvsUdpSendLim_Type()
)
ibmMvsUdpSendLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpSendLim.setStatus("current")


class _IbmMvsUdpRecvLim_Type(Unsigned32):
    """Custom type ibmMvsUdpRecvLim based on Unsigned32"""
    defaultValue = 0


_IbmMvsUdpRecvLim_Object = MibTableColumn
ibmMvsUdpRecvLim = _IbmMvsUdpRecvLim_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 13),
    _IbmMvsUdpRecvLim_Type()
)
ibmMvsUdpRecvLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpRecvLim.setStatus("current")


class _IbmMvsUdpEntryState_Type(Integer32):
    """Custom type ibmMvsUdpEntryState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_IbmMvsUdpEntryState_Type.__name__ = "Integer32"
_IbmMvsUdpEntryState_Object = MibTableColumn
ibmMvsUdpEntryState = _IbmMvsUdpEntryState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 14),
    _IbmMvsUdpEntryState_Type()
)
ibmMvsUdpEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsUdpEntryState.setStatus("current")


class _IbmMvsUdpMcastTTL_Type(Integer32):
    """Custom type ibmMvsUdpMcastTTL based on Integer32"""
    defaultValue = 1


_IbmMvsUdpMcastTTL_Object = MibTableColumn
ibmMvsUdpMcastTTL = _IbmMvsUdpMcastTTL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 15),
    _IbmMvsUdpMcastTTL_Type()
)
ibmMvsUdpMcastTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastTTL.setStatus("current")
_IbmMvsUdpMcastLoopback_Type = TruthValue
_IbmMvsUdpMcastLoopback_Object = MibTableColumn
ibmMvsUdpMcastLoopback = _IbmMvsUdpMcastLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 16),
    _IbmMvsUdpMcastLoopback_Type()
)
ibmMvsUdpMcastLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastLoopback.setStatus("current")
_IbmMvsUdpMcastLinkAddr_Type = IpAddress
_IbmMvsUdpMcastLinkAddr_Object = MibTableColumn
ibmMvsUdpMcastLinkAddr = _IbmMvsUdpMcastLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 17),
    _IbmMvsUdpMcastLinkAddr_Type()
)
ibmMvsUdpMcastLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastLinkAddr.setStatus("current")


class _IbmMvsUdpDSField_Type(OctetString):
    """Custom type ibmMvsUdpDSField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmMvsUdpDSField_Type.__name__ = "OctetString"
_IbmMvsUdpDSField_Object = MibTableColumn
ibmMvsUdpDSField = _IbmMvsUdpDSField_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 1, 1, 18),
    _IbmMvsUdpDSField_Type()
)
ibmMvsUdpDSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpDSField.setStatus("current")
_IbmTcpipMvsUdpMcastRecvTable_Object = MibTable
ibmTcpipMvsUdpMcastRecvTable = _IbmTcpipMvsUdpMcastRecvTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ibmTcpipMvsUdpMcastRecvTable.setStatus("current")
_IbmTcpipMvsUdpMcastRecvEntry_Object = MibTableRow
ibmTcpipMvsUdpMcastRecvEntry = _IbmTcpipMvsUdpMcastRecvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2, 1)
)
ibmTcpipMvsUdpMcastRecvEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvLocalAddress"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvLocalPort"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvGroup"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvLinkAddr"),
)
if mibBuilder.loadTexts:
    ibmTcpipMvsUdpMcastRecvEntry.setStatus("current")
_IbmMvsUdpMcastRecvLocalAddress_Type = IpAddress
_IbmMvsUdpMcastRecvLocalAddress_Object = MibTableColumn
ibmMvsUdpMcastRecvLocalAddress = _IbmMvsUdpMcastRecvLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2, 1, 1),
    _IbmMvsUdpMcastRecvLocalAddress_Type()
)
ibmMvsUdpMcastRecvLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastRecvLocalAddress.setStatus("current")


class _IbmMvsUdpMcastRecvLocalPort_Type(Integer32):
    """Custom type ibmMvsUdpMcastRecvLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsUdpMcastRecvLocalPort_Type.__name__ = "Integer32"
_IbmMvsUdpMcastRecvLocalPort_Object = MibTableColumn
ibmMvsUdpMcastRecvLocalPort = _IbmMvsUdpMcastRecvLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2, 1, 2),
    _IbmMvsUdpMcastRecvLocalPort_Type()
)
ibmMvsUdpMcastRecvLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastRecvLocalPort.setStatus("current")
_IbmMvsUdpMcastRecvGroup_Type = IpAddress
_IbmMvsUdpMcastRecvGroup_Object = MibTableColumn
ibmMvsUdpMcastRecvGroup = _IbmMvsUdpMcastRecvGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2, 1, 3),
    _IbmMvsUdpMcastRecvGroup_Type()
)
ibmMvsUdpMcastRecvGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastRecvGroup.setStatus("current")
_IbmMvsUdpMcastRecvLinkAddr_Type = IpAddress
_IbmMvsUdpMcastRecvLinkAddr_Object = MibTableColumn
ibmMvsUdpMcastRecvLinkAddr = _IbmMvsUdpMcastRecvLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 8, 2, 1, 4),
    _IbmMvsUdpMcastRecvLinkAddr_Type()
)
ibmMvsUdpMcastRecvLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsUdpMcastRecvLinkAddr.setStatus("current")
_IbmTcpipMvsIpGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsIpGroup = _IbmTcpipMvsIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9)
)
_IbmMvsIpInDevLayerCalls_Type = Counter32
_IbmMvsIpInDevLayerCalls_Object = MibScalar
ibmMvsIpInDevLayerCalls = _IbmMvsIpInDevLayerCalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 1),
    _IbmMvsIpInDevLayerCalls_Type()
)
ibmMvsIpInDevLayerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpInDevLayerCalls.setStatus("current")
_IbmMvsIpInUnpackErrors_Type = Counter32
_IbmMvsIpInUnpackErrors_Object = MibScalar
ibmMvsIpInUnpackErrors = _IbmMvsIpInUnpackErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 2),
    _IbmMvsIpInUnpackErrors_Type()
)
ibmMvsIpInUnpackErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpInUnpackErrors.setStatus("current")
_IbmMvsIpInDiscardsMemory_Type = Counter32
_IbmMvsIpInDiscardsMemory_Object = MibScalar
ibmMvsIpInDiscardsMemory = _IbmMvsIpInDiscardsMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 3),
    _IbmMvsIpInDiscardsMemory_Type()
)
ibmMvsIpInDiscardsMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpInDiscardsMemory.setStatus("current")
_IbmMvsIpOutDiscardsDlcSynch_Type = Counter32
_IbmMvsIpOutDiscardsDlcSynch_Object = MibScalar
ibmMvsIpOutDiscardsDlcSynch = _IbmMvsIpOutDiscardsDlcSynch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 4),
    _IbmMvsIpOutDiscardsDlcSynch_Type()
)
ibmMvsIpOutDiscardsDlcSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpOutDiscardsDlcSynch.setStatus("current")
_IbmMvsIpOutDiscardsDlcAsynch_Type = Counter32
_IbmMvsIpOutDiscardsDlcAsynch_Object = MibScalar
ibmMvsIpOutDiscardsDlcAsynch = _IbmMvsIpOutDiscardsDlcAsynch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 5),
    _IbmMvsIpOutDiscardsDlcAsynch_Type()
)
ibmMvsIpOutDiscardsDlcAsynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpOutDiscardsDlcAsynch.setStatus("current")
_IbmMvsIpOutDiscardsMemory_Type = Counter32
_IbmMvsIpOutDiscardsMemory_Object = MibScalar
ibmMvsIpOutDiscardsMemory = _IbmMvsIpOutDiscardsMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 9, 6),
    _IbmMvsIpOutDiscardsMemory_Type()
)
ibmMvsIpOutDiscardsMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsIpOutDiscardsMemory.setStatus("current")
_IbmTcpipMvsOsaExpGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsOsaExpGroup = _IbmTcpipMvsOsaExpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10)
)
_OsaexpChannelTable_Object = MibTable
osaexpChannelTable = _OsaexpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    osaexpChannelTable.setStatus("current")
_OsaexpChannelEntry_Object = MibTableRow
osaexpChannelEntry = _OsaexpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1)
)
osaexpChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osaexpChannelEntry.setStatus("current")
_IbmMvsOsaExpChannelNumber_Type = Integer32
_IbmMvsOsaExpChannelNumber_Object = MibTableColumn
ibmMvsOsaExpChannelNumber = _IbmMvsOsaExpChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 1),
    _IbmMvsOsaExpChannelNumber_Type()
)
ibmMvsOsaExpChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelNumber.setStatus("current")


class _IbmMvsOsaExpChannelType_Type(Integer32):
    """Custom type ibmMvsOsaExpChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("osd", 17),
          ("ose", 16))
    )


_IbmMvsOsaExpChannelType_Type.__name__ = "Integer32"
_IbmMvsOsaExpChannelType_Object = MibTableColumn
ibmMvsOsaExpChannelType = _IbmMvsOsaExpChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 2),
    _IbmMvsOsaExpChannelType_Type()
)
ibmMvsOsaExpChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelType.setStatus("current")


class _IbmMvsOsaExpChannelSubType_Type(Integer32):
    """Custom type ibmMvsOsaExpChannelSubType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("atmLanEmulation", 5),
          ("atmNative", 4),
          ("fastEthernet", 3),
          ("gigabit", 2),
          ("logicalEthernetAndTokenRingPorts", 11),
          ("logicalTokenRingAndEthPorts", 12),
          ("noPortsDefined", 6),
          ("oneLogicalEthPort", 7),
          ("oneLogicalTokenRingPort", 8),
          ("twoLogicalEthPorts", 9),
          ("twoLogicalTokenRingPorts", 10),
          ("unknown", 1))
    )


_IbmMvsOsaExpChannelSubType_Type.__name__ = "Integer32"
_IbmMvsOsaExpChannelSubType_Object = MibTableColumn
ibmMvsOsaExpChannelSubType = _IbmMvsOsaExpChannelSubType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 3),
    _IbmMvsOsaExpChannelSubType_Type()
)
ibmMvsOsaExpChannelSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelSubType.setStatus("current")


class _IbmMvsOsaExpChannelMode_Type(Integer32):
    """Custom type ibmMvsOsaExpChannelMode based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmLe", 9),
          ("atmLePassthru", 5),
          ("atmLePassthruAndSna", 7),
          ("atmLeSna", 6),
          ("atmNative", 8),
          ("nothingConfigured", 1),
          ("passthruAndSna", 4),
          ("passthruMode", 2),
          ("snaMode", 3))
    )


_IbmMvsOsaExpChannelMode_Type.__name__ = "Integer32"
_IbmMvsOsaExpChannelMode_Object = MibTableColumn
ibmMvsOsaExpChannelMode = _IbmMvsOsaExpChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 4),
    _IbmMvsOsaExpChannelMode_Type()
)
ibmMvsOsaExpChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelMode.setStatus("current")


class _IbmMvsOsaExpChannelState_Type(Integer32):
    """Custom type ibmMvsOsaExpChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notinst", 3),
          ("offline", 5),
          ("online", 1))
    )


_IbmMvsOsaExpChannelState_Type.__name__ = "Integer32"
_IbmMvsOsaExpChannelState_Object = MibTableColumn
ibmMvsOsaExpChannelState = _IbmMvsOsaExpChannelState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 5),
    _IbmMvsOsaExpChannelState_Type()
)
ibmMvsOsaExpChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelState.setStatus("current")


class _IbmMvsOsaExpChannelShared_Type(Integer32):
    """Custom type ibmMvsOsaExpChannelShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IbmMvsOsaExpChannelShared_Type.__name__ = "Integer32"
_IbmMvsOsaExpChannelShared_Object = MibTableColumn
ibmMvsOsaExpChannelShared = _IbmMvsOsaExpChannelShared_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 6),
    _IbmMvsOsaExpChannelShared_Type()
)
ibmMvsOsaExpChannelShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelShared.setStatus("current")
_IbmMvsOsaExpChannelNumPorts_Type = Integer32
_IbmMvsOsaExpChannelNumPorts_Object = MibTableColumn
ibmMvsOsaExpChannelNumPorts = _IbmMvsOsaExpChannelNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 7),
    _IbmMvsOsaExpChannelNumPorts_Type()
)
ibmMvsOsaExpChannelNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelNumPorts.setStatus("current")


class _IbmMvsOsaExpChannelDeterNodeDesc_Type(OctetString):
    """Custom type ibmMvsOsaExpChannelDeterNodeDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmMvsOsaExpChannelDeterNodeDesc_Type.__name__ = "OctetString"
_IbmMvsOsaExpChannelDeterNodeDesc_Object = MibTableColumn
ibmMvsOsaExpChannelDeterNodeDesc = _IbmMvsOsaExpChannelDeterNodeDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 8),
    _IbmMvsOsaExpChannelDeterNodeDesc_Type()
)
ibmMvsOsaExpChannelDeterNodeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelDeterNodeDesc.setStatus("current")


class _IbmMvsOsaExpChannelControlUnitNumber_Type(OctetString):
    """Custom type ibmMvsOsaExpChannelControlUnitNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmMvsOsaExpChannelControlUnitNumber_Type.__name__ = "OctetString"
_IbmMvsOsaExpChannelControlUnitNumber_Object = MibTableColumn
ibmMvsOsaExpChannelControlUnitNumber = _IbmMvsOsaExpChannelControlUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 9),
    _IbmMvsOsaExpChannelControlUnitNumber_Type()
)
ibmMvsOsaExpChannelControlUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelControlUnitNumber.setStatus("current")


class _IbmMvsOsaExpChannelCodeLevel_Type(OctetString):
    """Custom type ibmMvsOsaExpChannelCodeLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmMvsOsaExpChannelCodeLevel_Type.__name__ = "OctetString"
_IbmMvsOsaExpChannelCodeLevel_Object = MibTableColumn
ibmMvsOsaExpChannelCodeLevel = _IbmMvsOsaExpChannelCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 10),
    _IbmMvsOsaExpChannelCodeLevel_Type()
)
ibmMvsOsaExpChannelCodeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelCodeLevel.setStatus("current")


class _IbmMvsOsaExpChannelCurLparName_Type(DisplayString):
    """Custom type ibmMvsOsaExpChannelCurLparName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsOsaExpChannelCurLparName_Type.__name__ = "DisplayString"
_IbmMvsOsaExpChannelCurLparName_Object = MibTableColumn
ibmMvsOsaExpChannelCurLparName = _IbmMvsOsaExpChannelCurLparName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 11),
    _IbmMvsOsaExpChannelCurLparName_Type()
)
ibmMvsOsaExpChannelCurLparName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelCurLparName.setStatus("current")
_IbmMvsOsaExpChannelCurLparNum_Type = Integer32
_IbmMvsOsaExpChannelCurLparNum_Object = MibTableColumn
ibmMvsOsaExpChannelCurLparNum = _IbmMvsOsaExpChannelCurLparNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 12),
    _IbmMvsOsaExpChannelCurLparNum_Type()
)
ibmMvsOsaExpChannelCurLparNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelCurLparNum.setStatus("current")


class _IbmMvsOsaExpChannelManLparName_Type(DisplayString):
    """Custom type ibmMvsOsaExpChannelManLparName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmMvsOsaExpChannelManLparName_Type.__name__ = "DisplayString"
_IbmMvsOsaExpChannelManLparName_Object = MibTableColumn
ibmMvsOsaExpChannelManLparName = _IbmMvsOsaExpChannelManLparName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 13),
    _IbmMvsOsaExpChannelManLparName_Type()
)
ibmMvsOsaExpChannelManLparName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelManLparName.setStatus("current")
_IbmMvsOsaExpChannelManLparNum_Type = Integer32
_IbmMvsOsaExpChannelManLparNum_Object = MibTableColumn
ibmMvsOsaExpChannelManLparNum = _IbmMvsOsaExpChannelManLparNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 14),
    _IbmMvsOsaExpChannelManLparNum_Type()
)
ibmMvsOsaExpChannelManLparNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelManLparNum.setStatus("current")
_IbmMvsOsaExpChannelPCIBusUtil1Min_Type = Integer32
_IbmMvsOsaExpChannelPCIBusUtil1Min_Object = MibTableColumn
ibmMvsOsaExpChannelPCIBusUtil1Min = _IbmMvsOsaExpChannelPCIBusUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 15),
    _IbmMvsOsaExpChannelPCIBusUtil1Min_Type()
)
ibmMvsOsaExpChannelPCIBusUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelPCIBusUtil1Min.setStatus("current")
_IbmMvsOsaExpChannelProcessorUtil1Min_Type = Integer32
_IbmMvsOsaExpChannelProcessorUtil1Min_Object = MibTableColumn
ibmMvsOsaExpChannelProcessorUtil1Min = _IbmMvsOsaExpChannelProcessorUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 16),
    _IbmMvsOsaExpChannelProcessorUtil1Min_Type()
)
ibmMvsOsaExpChannelProcessorUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelProcessorUtil1Min.setStatus("current")
_IbmMvsOsaExpChannelPCIBusUtil5Min_Type = Integer32
_IbmMvsOsaExpChannelPCIBusUtil5Min_Object = MibTableColumn
ibmMvsOsaExpChannelPCIBusUtil5Min = _IbmMvsOsaExpChannelPCIBusUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 17),
    _IbmMvsOsaExpChannelPCIBusUtil5Min_Type()
)
ibmMvsOsaExpChannelPCIBusUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelPCIBusUtil5Min.setStatus("current")
_IbmMvsOsaExpChannelProcessorUtil5Min_Type = Integer32
_IbmMvsOsaExpChannelProcessorUtil5Min_Object = MibTableColumn
ibmMvsOsaExpChannelProcessorUtil5Min = _IbmMvsOsaExpChannelProcessorUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 18),
    _IbmMvsOsaExpChannelProcessorUtil5Min_Type()
)
ibmMvsOsaExpChannelProcessorUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelProcessorUtil5Min.setStatus("current")
_IbmMvsOsaExpChannelPCIBusUtilHour_Type = Integer32
_IbmMvsOsaExpChannelPCIBusUtilHour_Object = MibTableColumn
ibmMvsOsaExpChannelPCIBusUtilHour = _IbmMvsOsaExpChannelPCIBusUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 19),
    _IbmMvsOsaExpChannelPCIBusUtilHour_Type()
)
ibmMvsOsaExpChannelPCIBusUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelPCIBusUtilHour.setStatus("current")
_IbmMvsOsaExpChannelProcessorUtilHour_Type = Integer32
_IbmMvsOsaExpChannelProcessorUtilHour_Object = MibTableColumn
ibmMvsOsaExpChannelProcessorUtilHour = _IbmMvsOsaExpChannelProcessorUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 1, 1, 20),
    _IbmMvsOsaExpChannelProcessorUtilHour_Type()
)
ibmMvsOsaExpChannelProcessorUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpChannelProcessorUtilHour.setStatus("current")
_OsaexpPerfTable_Object = MibTable
osaexpPerfTable = _OsaexpPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    osaexpPerfTable.setStatus("current")
_OsaexpPerfEntry_Object = MibTableRow
osaexpPerfEntry = _OsaexpPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1)
)
osaexpPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfLparNum"),
)
if mibBuilder.loadTexts:
    osaexpPerfEntry.setStatus("current")
_IbmMvsOsaExpPerfLparNum_Type = Integer32
_IbmMvsOsaExpPerfLparNum_Object = MibTableColumn
ibmMvsOsaExpPerfLparNum = _IbmMvsOsaExpPerfLparNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 1),
    _IbmMvsOsaExpPerfLparNum_Type()
)
ibmMvsOsaExpPerfLparNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfLparNum.setStatus("current")
_IbmMvsOsaExpPerfProcessorUtil1Min_Type = Integer32
_IbmMvsOsaExpPerfProcessorUtil1Min_Object = MibTableColumn
ibmMvsOsaExpPerfProcessorUtil1Min = _IbmMvsOsaExpPerfProcessorUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 2),
    _IbmMvsOsaExpPerfProcessorUtil1Min_Type()
)
ibmMvsOsaExpPerfProcessorUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfProcessorUtil1Min.setStatus("current")
_IbmMvsOsaExpPerfInKbytesRate1Min_Type = Counter32
_IbmMvsOsaExpPerfInKbytesRate1Min_Object = MibTableColumn
ibmMvsOsaExpPerfInKbytesRate1Min = _IbmMvsOsaExpPerfInKbytesRate1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 3),
    _IbmMvsOsaExpPerfInKbytesRate1Min_Type()
)
ibmMvsOsaExpPerfInKbytesRate1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfInKbytesRate1Min.setStatus("current")
_IbmMvsOsaExpPerfOutKbytesRate1Min_Type = Counter32
_IbmMvsOsaExpPerfOutKbytesRate1Min_Object = MibTableColumn
ibmMvsOsaExpPerfOutKbytesRate1Min = _IbmMvsOsaExpPerfOutKbytesRate1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 4),
    _IbmMvsOsaExpPerfOutKbytesRate1Min_Type()
)
ibmMvsOsaExpPerfOutKbytesRate1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfOutKbytesRate1Min.setStatus("current")
_IbmMvsOsaExpPerfProcessorUtil5Min_Type = Integer32
_IbmMvsOsaExpPerfProcessorUtil5Min_Object = MibTableColumn
ibmMvsOsaExpPerfProcessorUtil5Min = _IbmMvsOsaExpPerfProcessorUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 5),
    _IbmMvsOsaExpPerfProcessorUtil5Min_Type()
)
ibmMvsOsaExpPerfProcessorUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfProcessorUtil5Min.setStatus("current")
_IbmMvsOsaExpPerfInKbytesRate5Min_Type = Counter32
_IbmMvsOsaExpPerfInKbytesRate5Min_Object = MibTableColumn
ibmMvsOsaExpPerfInKbytesRate5Min = _IbmMvsOsaExpPerfInKbytesRate5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 6),
    _IbmMvsOsaExpPerfInKbytesRate5Min_Type()
)
ibmMvsOsaExpPerfInKbytesRate5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfInKbytesRate5Min.setStatus("current")
_IbmMvsOsaExpPerfOutKbytesRate5Min_Type = Counter32
_IbmMvsOsaExpPerfOutKbytesRate5Min_Object = MibTableColumn
ibmMvsOsaExpPerfOutKbytesRate5Min = _IbmMvsOsaExpPerfOutKbytesRate5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 7),
    _IbmMvsOsaExpPerfOutKbytesRate5Min_Type()
)
ibmMvsOsaExpPerfOutKbytesRate5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfOutKbytesRate5Min.setStatus("current")
_IbmMvsOsaExpPerfProcessorUtilHour_Type = Integer32
_IbmMvsOsaExpPerfProcessorUtilHour_Object = MibTableColumn
ibmMvsOsaExpPerfProcessorUtilHour = _IbmMvsOsaExpPerfProcessorUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 8),
    _IbmMvsOsaExpPerfProcessorUtilHour_Type()
)
ibmMvsOsaExpPerfProcessorUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfProcessorUtilHour.setStatus("current")
_IbmMvsOsaExpPerfInKbytesRateHour_Type = Counter32
_IbmMvsOsaExpPerfInKbytesRateHour_Object = MibTableColumn
ibmMvsOsaExpPerfInKbytesRateHour = _IbmMvsOsaExpPerfInKbytesRateHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 9),
    _IbmMvsOsaExpPerfInKbytesRateHour_Type()
)
ibmMvsOsaExpPerfInKbytesRateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfInKbytesRateHour.setStatus("current")
_IbmMvsOsaExpPerfOutKbytesRateHour_Type = Counter32
_IbmMvsOsaExpPerfOutKbytesRateHour_Object = MibTableColumn
ibmMvsOsaExpPerfOutKbytesRateHour = _IbmMvsOsaExpPerfOutKbytesRateHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 2, 1, 10),
    _IbmMvsOsaExpPerfOutKbytesRateHour_Type()
)
ibmMvsOsaExpPerfOutKbytesRateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpPerfOutKbytesRateHour.setStatus("current")
_OsaexpEthPortTable_Object = MibTable
osaexpEthPortTable = _OsaexpEthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3)
)
if mibBuilder.loadTexts:
    osaexpEthPortTable.setStatus("current")
_OsaexpEthPortEntry_Object = MibTableRow
osaexpEthPortEntry = _OsaexpEthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1)
)
osaexpEthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osaexpEthPortEntry.setStatus("current")
_IbmMvsOsaExpEthPortNumber_Type = Integer32
_IbmMvsOsaExpEthPortNumber_Object = MibTableColumn
ibmMvsOsaExpEthPortNumber = _IbmMvsOsaExpEthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 1),
    _IbmMvsOsaExpEthPortNumber_Type()
)
ibmMvsOsaExpEthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortNumber.setStatus("current")


class _IbmMvsOsaExpEthPortType_Type(Integer32):
    """Custom type ibmMvsOsaExpEthPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              81)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 81),
          ("gigabitEthernet", 65))
    )


_IbmMvsOsaExpEthPortType_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthPortType_Object = MibTableColumn
ibmMvsOsaExpEthPortType = _IbmMvsOsaExpEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 2),
    _IbmMvsOsaExpEthPortType_Type()
)
ibmMvsOsaExpEthPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortType.setStatus("current")


class _IbmMvsOsaExpEthPortHardwareState_Type(Integer32):
    """Custom type ibmMvsOsaExpEthPortHardwareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 4),
          ("linkFailure", 2),
          ("unknown", 1))
    )


_IbmMvsOsaExpEthPortHardwareState_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthPortHardwareState_Object = MibTableColumn
ibmMvsOsaExpEthPortHardwareState = _IbmMvsOsaExpEthPortHardwareState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 3),
    _IbmMvsOsaExpEthPortHardwareState_Type()
)
ibmMvsOsaExpEthPortHardwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortHardwareState.setStatus("current")


class _IbmMvsOsaExpEthPortServiceMode_Type(Integer32):
    """Custom type ibmMvsOsaExpEthPortServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonserviceMode", 0),
          ("serviceMode", 1))
    )


_IbmMvsOsaExpEthPortServiceMode_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthPortServiceMode_Object = MibTableColumn
ibmMvsOsaExpEthPortServiceMode = _IbmMvsOsaExpEthPortServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 4),
    _IbmMvsOsaExpEthPortServiceMode_Type()
)
ibmMvsOsaExpEthPortServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortServiceMode.setStatus("current")


class _IbmMvsOsaExpEthPortDisabledStatus_Type(OctetString):
    """Custom type ibmMvsOsaExpEthPortDisabledStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmMvsOsaExpEthPortDisabledStatus_Type.__name__ = "OctetString"
_IbmMvsOsaExpEthPortDisabledStatus_Object = MibTableColumn
ibmMvsOsaExpEthPortDisabledStatus = _IbmMvsOsaExpEthPortDisabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 5),
    _IbmMvsOsaExpEthPortDisabledStatus_Type()
)
ibmMvsOsaExpEthPortDisabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortDisabledStatus.setStatus("current")


class _IbmMvsOsaExpEthPortConfigName_Type(DisplayString):
    """Custom type ibmMvsOsaExpEthPortConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_IbmMvsOsaExpEthPortConfigName_Type.__name__ = "DisplayString"
_IbmMvsOsaExpEthPortConfigName_Object = MibTableColumn
ibmMvsOsaExpEthPortConfigName = _IbmMvsOsaExpEthPortConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 6),
    _IbmMvsOsaExpEthPortConfigName_Type()
)
ibmMvsOsaExpEthPortConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortConfigName.setStatus("current")


class _IbmMvsOsaExpEthPortConfigSpeed_Type(Integer32):
    """Custom type ibmMvsOsaExpEthPortConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 0),
          ("fullDuplex1000Mb", 7),
          ("fullDuplex100Mb", 4),
          ("fullDuplex10Mb", 2),
          ("halfDuplex100Mb", 3),
          ("halfDuplex10Mb", 1))
    )


_IbmMvsOsaExpEthPortConfigSpeed_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthPortConfigSpeed_Object = MibTableColumn
ibmMvsOsaExpEthPortConfigSpeed = _IbmMvsOsaExpEthPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 7),
    _IbmMvsOsaExpEthPortConfigSpeed_Type()
)
ibmMvsOsaExpEthPortConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortConfigSpeed.setStatus("current")


class _IbmMvsOsaExpEthPortActiveSpeed_Type(Integer32):
    """Custom type ibmMvsOsaExpEthPortActiveSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex1000Mb", 7),
          ("fullDuplex100Mb", 4),
          ("fullDuplex10Mb", 2),
          ("halfDuplex100Mb", 3),
          ("halfDuplex10Mb", 1),
          ("unknown", 0))
    )


_IbmMvsOsaExpEthPortActiveSpeed_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthPortActiveSpeed_Object = MibTableColumn
ibmMvsOsaExpEthPortActiveSpeed = _IbmMvsOsaExpEthPortActiveSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 8),
    _IbmMvsOsaExpEthPortActiveSpeed_Type()
)
ibmMvsOsaExpEthPortActiveSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortActiveSpeed.setStatus("current")


class _IbmMvsOsaExpEthPortMacAddrActive_Type(OctetString):
    """Custom type ibmMvsOsaExpEthPortMacAddrActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsOsaExpEthPortMacAddrActive_Type.__name__ = "OctetString"
_IbmMvsOsaExpEthPortMacAddrActive_Object = MibTableColumn
ibmMvsOsaExpEthPortMacAddrActive = _IbmMvsOsaExpEthPortMacAddrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 9),
    _IbmMvsOsaExpEthPortMacAddrActive_Type()
)
ibmMvsOsaExpEthPortMacAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortMacAddrActive.setStatus("current")


class _IbmMvsOsaExpEthPortMacAddrBurntIn_Type(OctetString):
    """Custom type ibmMvsOsaExpEthPortMacAddrBurntIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmMvsOsaExpEthPortMacAddrBurntIn_Type.__name__ = "OctetString"
_IbmMvsOsaExpEthPortMacAddrBurntIn_Object = MibTableColumn
ibmMvsOsaExpEthPortMacAddrBurntIn = _IbmMvsOsaExpEthPortMacAddrBurntIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 10),
    _IbmMvsOsaExpEthPortMacAddrBurntIn_Type()
)
ibmMvsOsaExpEthPortMacAddrBurntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortMacAddrBurntIn.setStatus("current")
_IbmMvsOsaExpEthPortUserData_Type = DisplayString
_IbmMvsOsaExpEthPortUserData_Object = MibTableColumn
ibmMvsOsaExpEthPortUserData = _IbmMvsOsaExpEthPortUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 11),
    _IbmMvsOsaExpEthPortUserData_Type()
)
ibmMvsOsaExpEthPortUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortUserData.setStatus("current")
_IbmMvsOsaExpEthPortOutPackets_Type = Counter32
_IbmMvsOsaExpEthPortOutPackets_Object = MibTableColumn
ibmMvsOsaExpEthPortOutPackets = _IbmMvsOsaExpEthPortOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 12),
    _IbmMvsOsaExpEthPortOutPackets_Type()
)
ibmMvsOsaExpEthPortOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortOutPackets.setStatus("current")
_IbmMvsOsaExpEthPortInPackets_Type = Counter32
_IbmMvsOsaExpEthPortInPackets_Object = MibTableColumn
ibmMvsOsaExpEthPortInPackets = _IbmMvsOsaExpEthPortInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 13),
    _IbmMvsOsaExpEthPortInPackets_Type()
)
ibmMvsOsaExpEthPortInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortInPackets.setStatus("current")
_IbmMvsOsaExpEthPortInGroupFrames_Type = Counter32
_IbmMvsOsaExpEthPortInGroupFrames_Object = MibTableColumn
ibmMvsOsaExpEthPortInGroupFrames = _IbmMvsOsaExpEthPortInGroupFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 14),
    _IbmMvsOsaExpEthPortInGroupFrames_Type()
)
ibmMvsOsaExpEthPortInGroupFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortInGroupFrames.setStatus("current")
_IbmMvsOsaExpEthPortInBroadcastFrames_Type = Counter32
_IbmMvsOsaExpEthPortInBroadcastFrames_Object = MibTableColumn
ibmMvsOsaExpEthPortInBroadcastFrames = _IbmMvsOsaExpEthPortInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 15),
    _IbmMvsOsaExpEthPortInBroadcastFrames_Type()
)
ibmMvsOsaExpEthPortInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortInBroadcastFrames.setStatus("current")


class _IbmMvsOsaExpEthPortName_Type(DisplayString):
    """Custom type ibmMvsOsaExpEthPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmMvsOsaExpEthPortName_Type.__name__ = "DisplayString"
_IbmMvsOsaExpEthPortName_Object = MibTableColumn
ibmMvsOsaExpEthPortName = _IbmMvsOsaExpEthPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 16),
    _IbmMvsOsaExpEthPortName_Type()
)
ibmMvsOsaExpEthPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortName.setStatus("current")
_IbmMvsOsaExpEthPortInUnknownIPFrames_Type = Counter32
_IbmMvsOsaExpEthPortInUnknownIPFrames_Object = MibTableColumn
ibmMvsOsaExpEthPortInUnknownIPFrames = _IbmMvsOsaExpEthPortInUnknownIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 17),
    _IbmMvsOsaExpEthPortInUnknownIPFrames_Type()
)
ibmMvsOsaExpEthPortInUnknownIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortInUnknownIPFrames.setStatus("current")


class _IbmMvsOsaExpEthPortGroupMacAddrs_Type(OctetString):
    """Custom type ibmMvsOsaExpEthPortGroupMacAddrs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_IbmMvsOsaExpEthPortGroupMacAddrs_Type.__name__ = "OctetString"
_IbmMvsOsaExpEthPortGroupMacAddrs_Object = MibTableColumn
ibmMvsOsaExpEthPortGroupMacAddrs = _IbmMvsOsaExpEthPortGroupMacAddrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 3, 1, 18),
    _IbmMvsOsaExpEthPortGroupMacAddrs_Type()
)
ibmMvsOsaExpEthPortGroupMacAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthPortGroupMacAddrs.setStatus("current")
_OsaexpEthSnaTable_Object = MibTable
osaexpEthSnaTable = _OsaexpEthSnaTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    osaexpEthSnaTable.setStatus("current")
_OsaexpEthSnaEntry_Object = MibTableRow
osaexpEthSnaEntry = _OsaexpEthSnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1)
)
osaexpEthSnaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osaexpEthSnaEntry.setStatus("current")
_IbmMvsOsaExpEthSnaInactTimer_Type = Integer32
_IbmMvsOsaExpEthSnaInactTimer_Object = MibTableColumn
ibmMvsOsaExpEthSnaInactTimer = _IbmMvsOsaExpEthSnaInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1, 1),
    _IbmMvsOsaExpEthSnaInactTimer_Type()
)
ibmMvsOsaExpEthSnaInactTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthSnaInactTimer.setStatus("current")


class _IbmMvsOsaExpEthSnaRespTimer_Type(Integer32):
    """Custom type ibmMvsOsaExpEthSnaRespTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 510),
    )


_IbmMvsOsaExpEthSnaRespTimer_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthSnaRespTimer_Object = MibTableColumn
ibmMvsOsaExpEthSnaRespTimer = _IbmMvsOsaExpEthSnaRespTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1, 2),
    _IbmMvsOsaExpEthSnaRespTimer_Type()
)
ibmMvsOsaExpEthSnaRespTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthSnaRespTimer.setStatus("current")


class _IbmMvsOsaExpEthSnaAckTimer_Type(Integer32):
    """Custom type ibmMvsOsaExpEthSnaAckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2040),
    )


_IbmMvsOsaExpEthSnaAckTimer_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthSnaAckTimer_Object = MibTableColumn
ibmMvsOsaExpEthSnaAckTimer = _IbmMvsOsaExpEthSnaAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1, 3),
    _IbmMvsOsaExpEthSnaAckTimer_Type()
)
ibmMvsOsaExpEthSnaAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthSnaAckTimer.setStatus("current")


class _IbmMvsOsaExpEthSnaMaxIFramesBeforeAck_Type(Integer32):
    """Custom type ibmMvsOsaExpEthSnaMaxIFramesBeforeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IbmMvsOsaExpEthSnaMaxIFramesBeforeAck_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthSnaMaxIFramesBeforeAck_Object = MibTableColumn
ibmMvsOsaExpEthSnaMaxIFramesBeforeAck = _IbmMvsOsaExpEthSnaMaxIFramesBeforeAck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1, 4),
    _IbmMvsOsaExpEthSnaMaxIFramesBeforeAck_Type()
)
ibmMvsOsaExpEthSnaMaxIFramesBeforeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthSnaMaxIFramesBeforeAck.setStatus("current")


class _IbmMvsOsaExpEthSnaMaxTransmitWindow_Type(Integer32):
    """Custom type ibmMvsOsaExpEthSnaMaxTransmitWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IbmMvsOsaExpEthSnaMaxTransmitWindow_Type.__name__ = "Integer32"
_IbmMvsOsaExpEthSnaMaxTransmitWindow_Object = MibTableColumn
ibmMvsOsaExpEthSnaMaxTransmitWindow = _IbmMvsOsaExpEthSnaMaxTransmitWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 10, 4, 1, 5),
    _IbmMvsOsaExpEthSnaMaxTransmitWindow_Type()
)
ibmMvsOsaExpEthSnaMaxTransmitWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsOsaExpEthSnaMaxTransmitWindow.setStatus("current")
_IbmTcpipMvsDVIPAGroup_ObjectIdentity = ObjectIdentity
ibmTcpipMvsDVIPAGroup = _IbmTcpipMvsDVIPAGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11)
)
_IbmMvsDVIPATable_Object = MibTable
ibmMvsDVIPATable = _IbmMvsDVIPATable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    ibmMvsDVIPATable.setStatus("current")
_IbmMvsDVIPAEntry_Object = MibTableRow
ibmMvsDVIPAEntry = _IbmMvsDVIPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1)
)
ibmMvsDVIPAEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddr"),
)
if mibBuilder.loadTexts:
    ibmMvsDVIPAEntry.setStatus("current")
_IbmMvsDVIPAIpAddrType_Type = InetAddressType
_IbmMvsDVIPAIpAddrType_Object = MibTableColumn
ibmMvsDVIPAIpAddrType = _IbmMvsDVIPAIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 1),
    _IbmMvsDVIPAIpAddrType_Type()
)
ibmMvsDVIPAIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAIpAddrType.setStatus("current")


class _IbmMvsDVIPAIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPAIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsDVIPAIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPAIpAddr_Object = MibTableColumn
ibmMvsDVIPAIpAddr = _IbmMvsDVIPAIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 2),
    _IbmMvsDVIPAIpAddr_Type()
)
ibmMvsDVIPAIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAIpAddr.setStatus("current")
_IbmMvsDVIPAMaskType_Type = InetAddressType
_IbmMvsDVIPAMaskType_Object = MibTableColumn
ibmMvsDVIPAMaskType = _IbmMvsDVIPAMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 3),
    _IbmMvsDVIPAMaskType_Type()
)
ibmMvsDVIPAMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAMaskType.setStatus("current")


class _IbmMvsDVIPAMaskAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPAMaskAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IbmMvsDVIPAMaskAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPAMaskAddr_Object = MibTableColumn
ibmMvsDVIPAMaskAddr = _IbmMvsDVIPAMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 4),
    _IbmMvsDVIPAMaskAddr_Type()
)
ibmMvsDVIPAMaskAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAMaskAddr.setStatus("current")


class _IbmMvsDVIPAStatus_Type(Integer32):
    """Custom type ibmMvsDVIPAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 3),
          ("moving", 4),
          ("quiescing", 5),
          ("unknown", 1))
    )


_IbmMvsDVIPAStatus_Type.__name__ = "Integer32"
_IbmMvsDVIPAStatus_Object = MibTableColumn
ibmMvsDVIPAStatus = _IbmMvsDVIPAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 5),
    _IbmMvsDVIPAStatus_Type()
)
ibmMvsDVIPAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAStatus.setStatus("current")


class _IbmMvsDVIPAOrigin_Type(Integer32):
    """Custom type ibmMvsDVIPAOrigin based on Integer32"""
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
        *(("backup", 2),
          ("define", 3),
          ("rangeBind", 4),
          ("rangeIoctl", 5),
          ("target", 6),
          ("unknown", 1))
    )


_IbmMvsDVIPAOrigin_Type.__name__ = "Integer32"
_IbmMvsDVIPAOrigin_Object = MibTableColumn
ibmMvsDVIPAOrigin = _IbmMvsDVIPAOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 6),
    _IbmMvsDVIPAOrigin_Type()
)
ibmMvsDVIPAOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAOrigin.setStatus("current")
_IbmMvsDVIPARank_Type = Integer32
_IbmMvsDVIPARank_Object = MibTableColumn
ibmMvsDVIPARank = _IbmMvsDVIPARank_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 7),
    _IbmMvsDVIPARank_Type()
)
ibmMvsDVIPARank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPARank.setStatus("current")


class _IbmMvsDVIPADistributeStatus_Type(Integer32):
    """Custom type ibmMvsDVIPADistributeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disgtributorAndTarget", 4),
          ("distributor", 2),
          ("none", 1),
          ("target", 3))
    )


_IbmMvsDVIPADistributeStatus_Type.__name__ = "Integer32"
_IbmMvsDVIPADistributeStatus_Object = MibTableColumn
ibmMvsDVIPADistributeStatus = _IbmMvsDVIPADistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 8),
    _IbmMvsDVIPADistributeStatus_Type()
)
ibmMvsDVIPADistributeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistributeStatus.setStatus("current")


class _IbmMvsDVIPAMoveable_Type(Integer32):
    """Custom type ibmMvsDVIPAMoveable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disruptive", 5),
          ("immediate", 2),
          ("nonDisruptive", 4),
          ("none", 1),
          ("whenIdle", 3))
    )


_IbmMvsDVIPAMoveable_Type.__name__ = "Integer32"
_IbmMvsDVIPAMoveable_Object = MibTableColumn
ibmMvsDVIPAMoveable = _IbmMvsDVIPAMoveable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 9),
    _IbmMvsDVIPAMoveable_Type()
)
ibmMvsDVIPAMoveable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAMoveable.setStatus("current")
_IbmMvsDVIPAServMgrEnabled_Type = TruthValue
_IbmMvsDVIPAServMgrEnabled_Object = MibTableColumn
ibmMvsDVIPAServMgrEnabled = _IbmMvsDVIPAServMgrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 1, 1, 10),
    _IbmMvsDVIPAServMgrEnabled_Type()
)
ibmMvsDVIPAServMgrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAServMgrEnabled.setStatus("current")
_IbmMvsDVIPARangeConfTable_Object = MibTable
ibmMvsDVIPARangeConfTable = _IbmMvsDVIPARangeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2)
)
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfTable.setStatus("current")
_IbmMvsDVIPARangeConfEntry_Object = MibTableRow
ibmMvsDVIPARangeConfEntry = _IbmMvsDVIPARangeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1)
)
ibmMvsDVIPARangeConfEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfIpAddr"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfMaskType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfMaskAddr"),
)
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfEntry.setStatus("current")
_IbmMvsDVIPARangeConfIpAddrType_Type = InetAddressType
_IbmMvsDVIPARangeConfIpAddrType_Object = MibTableColumn
ibmMvsDVIPARangeConfIpAddrType = _IbmMvsDVIPARangeConfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 1),
    _IbmMvsDVIPARangeConfIpAddrType_Type()
)
ibmMvsDVIPARangeConfIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfIpAddrType.setStatus("current")


class _IbmMvsDVIPARangeConfIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPARangeConfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsDVIPARangeConfIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPARangeConfIpAddr_Object = MibTableColumn
ibmMvsDVIPARangeConfIpAddr = _IbmMvsDVIPARangeConfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 2),
    _IbmMvsDVIPARangeConfIpAddr_Type()
)
ibmMvsDVIPARangeConfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfIpAddr.setStatus("current")
_IbmMvsDVIPARangeConfMaskType_Type = InetAddressType
_IbmMvsDVIPARangeConfMaskType_Object = MibTableColumn
ibmMvsDVIPARangeConfMaskType = _IbmMvsDVIPARangeConfMaskType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 3),
    _IbmMvsDVIPARangeConfMaskType_Type()
)
ibmMvsDVIPARangeConfMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfMaskType.setStatus("current")


class _IbmMvsDVIPARangeConfMaskAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPARangeConfMaskAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmMvsDVIPARangeConfMaskAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPARangeConfMaskAddr_Object = MibTableColumn
ibmMvsDVIPARangeConfMaskAddr = _IbmMvsDVIPARangeConfMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 4),
    _IbmMvsDVIPARangeConfMaskAddr_Type()
)
ibmMvsDVIPARangeConfMaskAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfMaskAddr.setStatus("current")


class _IbmMvsDVIPARangeConfMoveable_Type(Integer32):
    """Custom type ibmMvsDVIPARangeConfMoveable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disruptive", 2),
          ("nonDisruptive", 1))
    )


_IbmMvsDVIPARangeConfMoveable_Type.__name__ = "Integer32"
_IbmMvsDVIPARangeConfMoveable_Object = MibTableColumn
ibmMvsDVIPARangeConfMoveable = _IbmMvsDVIPARangeConfMoveable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 5),
    _IbmMvsDVIPARangeConfMoveable_Type()
)
ibmMvsDVIPARangeConfMoveable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfMoveable.setStatus("current")
_IbmMvsDVIPARangeConfStatus_Type = RowStatus
_IbmMvsDVIPARangeConfStatus_Object = MibTableColumn
ibmMvsDVIPARangeConfStatus = _IbmMvsDVIPARangeConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 2, 1, 6),
    _IbmMvsDVIPARangeConfStatus_Type()
)
ibmMvsDVIPARangeConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibmMvsDVIPARangeConfStatus.setStatus("current")
_IbmMvsDVIPADistConfTable_Object = MibTable
ibmMvsDVIPADistConfTable = _IbmMvsDVIPADistConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3)
)
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfTable.setStatus("current")
_IbmMvsDVIPADistConfEntry_Object = MibTableRow
ibmMvsDVIPADistConfEntry = _IbmMvsDVIPADistConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1)
)
ibmMvsDVIPADistConfEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfIpAddr"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfPort"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfTargetDynXcfIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfTargetDynXcfIpAddr"),
)
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfEntry.setStatus("current")
_IbmMvsDVIPADistConfIpAddrType_Type = InetAddressType
_IbmMvsDVIPADistConfIpAddrType_Object = MibTableColumn
ibmMvsDVIPADistConfIpAddrType = _IbmMvsDVIPADistConfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 1),
    _IbmMvsDVIPADistConfIpAddrType_Type()
)
ibmMvsDVIPADistConfIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfIpAddrType.setStatus("current")


class _IbmMvsDVIPADistConfIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPADistConfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsDVIPADistConfIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPADistConfIpAddr_Object = MibTableColumn
ibmMvsDVIPADistConfIpAddr = _IbmMvsDVIPADistConfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 2),
    _IbmMvsDVIPADistConfIpAddr_Type()
)
ibmMvsDVIPADistConfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfIpAddr.setStatus("current")


class _IbmMvsDVIPADistConfPort_Type(Integer32):
    """Custom type ibmMvsDVIPADistConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsDVIPADistConfPort_Type.__name__ = "Integer32"
_IbmMvsDVIPADistConfPort_Object = MibTableColumn
ibmMvsDVIPADistConfPort = _IbmMvsDVIPADistConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 3),
    _IbmMvsDVIPADistConfPort_Type()
)
ibmMvsDVIPADistConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfPort.setStatus("current")
_IbmMvsDVIPADistConfTargetDynXcfIpAddrType_Type = InetAddressType
_IbmMvsDVIPADistConfTargetDynXcfIpAddrType_Object = MibTableColumn
ibmMvsDVIPADistConfTargetDynXcfIpAddrType = _IbmMvsDVIPADistConfTargetDynXcfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 4),
    _IbmMvsDVIPADistConfTargetDynXcfIpAddrType_Type()
)
ibmMvsDVIPADistConfTargetDynXcfIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfTargetDynXcfIpAddrType.setStatus("current")


class _IbmMvsDVIPADistConfTargetDynXcfIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPADistConfTargetDynXcfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IbmMvsDVIPADistConfTargetDynXcfIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPADistConfTargetDynXcfIpAddr_Object = MibTableColumn
ibmMvsDVIPADistConfTargetDynXcfIpAddr = _IbmMvsDVIPADistConfTargetDynXcfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 5),
    _IbmMvsDVIPADistConfTargetDynXcfIpAddr_Type()
)
ibmMvsDVIPADistConfTargetDynXcfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfTargetDynXcfIpAddr.setStatus("current")
_IbmMvsDVIPADistConfStatus_Type = RowStatus
_IbmMvsDVIPADistConfStatus_Object = MibTableColumn
ibmMvsDVIPADistConfStatus = _IbmMvsDVIPADistConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 3, 1, 6),
    _IbmMvsDVIPADistConfStatus_Type()
)
ibmMvsDVIPADistConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistConfStatus.setStatus("current")
_IbmMvsDVIPAConnRoutingTable_Object = MibTable
ibmMvsDVIPAConnRoutingTable = _IbmMvsDVIPAConnRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4)
)
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnRoutingTable.setStatus("current")
_IbmMvsDVIPAConnRoutingEntry_Object = MibTableRow
ibmMvsDVIPAConnRoutingEntry = _IbmMvsDVIPAConnRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1)
)
ibmMvsDVIPAConnRoutingEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddr"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnPort"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnRemIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnRemIpAddr"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnRemPort"),
)
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnRoutingEntry.setStatus("current")


class _IbmMvsDVIPAConnPort_Type(Integer32):
    """Custom type ibmMvsDVIPAConnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsDVIPAConnPort_Type.__name__ = "Integer32"
_IbmMvsDVIPAConnPort_Object = MibTableColumn
ibmMvsDVIPAConnPort = _IbmMvsDVIPAConnPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 1),
    _IbmMvsDVIPAConnPort_Type()
)
ibmMvsDVIPAConnPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnPort.setStatus("current")
_IbmMvsDVIPAConnRemIpAddrType_Type = InetAddressType
_IbmMvsDVIPAConnRemIpAddrType_Object = MibTableColumn
ibmMvsDVIPAConnRemIpAddrType = _IbmMvsDVIPAConnRemIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 2),
    _IbmMvsDVIPAConnRemIpAddrType_Type()
)
ibmMvsDVIPAConnRemIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnRemIpAddrType.setStatus("current")


class _IbmMvsDVIPAConnRemIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPAConnRemIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsDVIPAConnRemIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPAConnRemIpAddr_Object = MibTableColumn
ibmMvsDVIPAConnRemIpAddr = _IbmMvsDVIPAConnRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 3),
    _IbmMvsDVIPAConnRemIpAddr_Type()
)
ibmMvsDVIPAConnRemIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnRemIpAddr.setStatus("current")


class _IbmMvsDVIPAConnRemPort_Type(Integer32):
    """Custom type ibmMvsDVIPAConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsDVIPAConnRemPort_Type.__name__ = "Integer32"
_IbmMvsDVIPAConnRemPort_Object = MibTableColumn
ibmMvsDVIPAConnRemPort = _IbmMvsDVIPAConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 4),
    _IbmMvsDVIPAConnRemPort_Type()
)
ibmMvsDVIPAConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnRemPort.setStatus("current")
_IbmMvsDVIPAConnDynXcfIpAddrType_Type = InetAddressType
_IbmMvsDVIPAConnDynXcfIpAddrType_Object = MibTableColumn
ibmMvsDVIPAConnDynXcfIpAddrType = _IbmMvsDVIPAConnDynXcfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 5),
    _IbmMvsDVIPAConnDynXcfIpAddrType_Type()
)
ibmMvsDVIPAConnDynXcfIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnDynXcfIpAddrType.setStatus("current")


class _IbmMvsDVIPAConnDynXcfIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPAConnDynXcfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_IbmMvsDVIPAConnDynXcfIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPAConnDynXcfIpAddr_Object = MibTableColumn
ibmMvsDVIPAConnDynXcfIpAddr = _IbmMvsDVIPAConnDynXcfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 6),
    _IbmMvsDVIPAConnDynXcfIpAddr_Type()
)
ibmMvsDVIPAConnDynXcfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnDynXcfIpAddr.setStatus("current")


class _IbmMvsDVIPAConnPolicyRuleName_Type(SnmpAdminString):
    """Custom type ibmMvsDVIPAConnPolicyRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IbmMvsDVIPAConnPolicyRuleName_Type.__name__ = "SnmpAdminString"
_IbmMvsDVIPAConnPolicyRuleName_Object = MibTableColumn
ibmMvsDVIPAConnPolicyRuleName = _IbmMvsDVIPAConnPolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 7),
    _IbmMvsDVIPAConnPolicyRuleName_Type()
)
ibmMvsDVIPAConnPolicyRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnPolicyRuleName.setStatus("current")


class _IbmMvsDVIPAConnPolicyActionName_Type(SnmpAdminString):
    """Custom type ibmMvsDVIPAConnPolicyActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IbmMvsDVIPAConnPolicyActionName_Type.__name__ = "SnmpAdminString"
_IbmMvsDVIPAConnPolicyActionName_Object = MibTableColumn
ibmMvsDVIPAConnPolicyActionName = _IbmMvsDVIPAConnPolicyActionName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 4, 1, 8),
    _IbmMvsDVIPAConnPolicyActionName_Type()
)
ibmMvsDVIPAConnPolicyActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAConnPolicyActionName.setStatus("current")
_IbmMvsDVIPADistPortTable_Object = MibTable
ibmMvsDVIPADistPortTable = _IbmMvsDVIPADistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5)
)
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortTable.setStatus("current")
_IbmMvsDVIPADistPortEntry_Object = MibTableRow
ibmMvsDVIPADistPortEntry = _IbmMvsDVIPADistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1)
)
ibmMvsDVIPADistPortEntry.setIndexNames(
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPAIpAddr"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortPort"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortTargetDynXcfIpAddrType"),
    (0, "IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortTargetDynXcfIpAddr"),
)
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortEntry.setStatus("current")


class _IbmMvsDVIPADistPortPort_Type(Integer32):
    """Custom type ibmMvsDVIPADistPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsDVIPADistPortPort_Type.__name__ = "Integer32"
_IbmMvsDVIPADistPortPort_Object = MibTableColumn
ibmMvsDVIPADistPortPort = _IbmMvsDVIPADistPortPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 1),
    _IbmMvsDVIPADistPortPort_Type()
)
ibmMvsDVIPADistPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortPort.setStatus("current")
_IbmMvsDVIPADistPortTargetDynXcfIpAddrType_Type = InetAddressType
_IbmMvsDVIPADistPortTargetDynXcfIpAddrType_Object = MibTableColumn
ibmMvsDVIPADistPortTargetDynXcfIpAddrType = _IbmMvsDVIPADistPortTargetDynXcfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 2),
    _IbmMvsDVIPADistPortTargetDynXcfIpAddrType_Type()
)
ibmMvsDVIPADistPortTargetDynXcfIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortTargetDynXcfIpAddrType.setStatus("current")


class _IbmMvsDVIPADistPortTargetDynXcfIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPADistPortTargetDynXcfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IbmMvsDVIPADistPortTargetDynXcfIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPADistPortTargetDynXcfIpAddr_Object = MibTableColumn
ibmMvsDVIPADistPortTargetDynXcfIpAddr = _IbmMvsDVIPADistPortTargetDynXcfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 3),
    _IbmMvsDVIPADistPortTargetDynXcfIpAddr_Type()
)
ibmMvsDVIPADistPortTargetDynXcfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortTargetDynXcfIpAddr.setStatus("current")
_IbmMvsDVIPADistPortReadyCount_Type = Gauge32
_IbmMvsDVIPADistPortReadyCount_Object = MibTableColumn
ibmMvsDVIPADistPortReadyCount = _IbmMvsDVIPADistPortReadyCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 4),
    _IbmMvsDVIPADistPortReadyCount_Type()
)
ibmMvsDVIPADistPortReadyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortReadyCount.setStatus("current")
_IbmMvsDVIPADistPortTotalConn_Type = Counter32
_IbmMvsDVIPADistPortTotalConn_Object = MibTableColumn
ibmMvsDVIPADistPortTotalConn = _IbmMvsDVIPADistPortTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 5),
    _IbmMvsDVIPADistPortTotalConn_Type()
)
ibmMvsDVIPADistPortTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortTotalConn.setStatus("current")
_IbmMvsDVIPADistPortWlmWeight_Type = Unsigned32
_IbmMvsDVIPADistPortWlmWeight_Object = MibTableColumn
ibmMvsDVIPADistPortWlmWeight = _IbmMvsDVIPADistPortWlmWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 5, 1, 6),
    _IbmMvsDVIPADistPortWlmWeight_Type()
)
ibmMvsDVIPADistPortWlmWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPADistPortWlmWeight.setStatus("current")
_IbmMvsDVIPAServMgrMulticastIpAddrType_Type = InetAddressType
_IbmMvsDVIPAServMgrMulticastIpAddrType_Object = MibScalar
ibmMvsDVIPAServMgrMulticastIpAddrType = _IbmMvsDVIPAServMgrMulticastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 6),
    _IbmMvsDVIPAServMgrMulticastIpAddrType_Type()
)
ibmMvsDVIPAServMgrMulticastIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAServMgrMulticastIpAddrType.setStatus("current")


class _IbmMvsDVIPAServMgrMulticastIpAddr_Type(InetAddress):
    """Custom type ibmMvsDVIPAServMgrMulticastIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IbmMvsDVIPAServMgrMulticastIpAddr_Type.__name__ = "InetAddress"
_IbmMvsDVIPAServMgrMulticastIpAddr_Object = MibScalar
ibmMvsDVIPAServMgrMulticastIpAddr = _IbmMvsDVIPAServMgrMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 7),
    _IbmMvsDVIPAServMgrMulticastIpAddr_Type()
)
ibmMvsDVIPAServMgrMulticastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAServMgrMulticastIpAddr.setStatus("current")


class _IbmMvsDVIPAServMgrPort_Type(Integer32):
    """Custom type ibmMvsDVIPAServMgrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmMvsDVIPAServMgrPort_Type.__name__ = "Integer32"
_IbmMvsDVIPAServMgrPort_Object = MibScalar
ibmMvsDVIPAServMgrPort = _IbmMvsDVIPAServMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 8),
    _IbmMvsDVIPAServMgrPort_Type()
)
ibmMvsDVIPAServMgrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAServMgrPort.setStatus("current")
_IbmMvsDVIPAServMgrPasswordSpecified_Type = TruthValue
_IbmMvsDVIPAServMgrPasswordSpecified_Object = MibScalar
ibmMvsDVIPAServMgrPasswordSpecified = _IbmMvsDVIPAServMgrPasswordSpecified_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 9),
    _IbmMvsDVIPAServMgrPasswordSpecified_Type()
)
ibmMvsDVIPAServMgrPasswordSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMvsDVIPAServMgrPasswordSpecified.setStatus("current")


class _IbmMvsDVIPATrapControl_Type(Bits):
    """Custom type ibmMvsDVIPATrapControl based on Bits"""
    namedValues = NamedValues(
        *(("dvipaRemoved", 1),
          ("dvipaStatusChange", 0),
          ("targetAdded", 2),
          ("targetRemoved", 3),
          ("targetServerEnded", 5),
          ("targetServerStarted", 4))
    )

_IbmMvsDVIPATrapControl_Type.__name__ = "Bits"
_IbmMvsDVIPATrapControl_Object = MibScalar
ibmMvsDVIPATrapControl = _IbmMvsDVIPATrapControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 2, 11, 10),
    _IbmMvsDVIPATrapControl_Type()
)
ibmMvsDVIPATrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmMvsDVIPATrapControl.setStatus("current")
_IbmTCPIPmvsConformance_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsConformance = _IbmTCPIPmvsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3)
)
_IbmTCPIPmvsCompliances_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsCompliances = _IbmTCPIPmvsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 1)
)
_IbmTCPIPmvsGroups_ObjectIdentity = ObjectIdentity
ibmTCPIPmvsGroups = _IbmTCPIPmvsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2)
)
_IbmAgentCaps_ObjectIdentity = ObjectIdentity
ibmAgentCaps = _IbmAgentCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 11)
)
ipForwardEntry.registerAugmentions(
    ("IBMTCPIPMVS-MIB",
     "ibmTcpipMvsGatewayEntry")
)
ibmTcpipMvsGatewayEntry.setIndexNames(*ipForwardEntry.getIndexNames())
tcpConnEntry.registerAugmentions(
    ("IBMTCPIPMVS-MIB",
     "ibmTcpipMvsTcpConnEntry")
)
ibmTcpipMvsTcpConnEntry.setIndexNames(*tcpConnEntry.getIndexNames())
udpEntry.registerAugmentions(
    ("IBMTCPIPMVS-MIB",
     "ibmTcpipMvsUdpEntry")
)
ibmTcpipMvsUdpEntry.setIndexNames(*udpEntry.getIndexNames())

# Managed Objects groups

ibmTCPIPmvsPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 1)
)
ibmTCPIPmvsPingGroup.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsRPingResponseTime")
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsPingGroup.setStatus("current")

ibmTCPIPmvsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 2)
)
ibmTCPIPmvsSystemGroup.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime")
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup.setStatus("obsolete")

ibmTCPIPmvsTcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 3)
)
ibmTCPIPmvsTcpGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnActiveOpen"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendWindowSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendWindowAck"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnPendTcpRecv"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSig"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBackoffCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpDet"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpPol"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup.setStatus("obsolete")

ibmTCPIPmvsUdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 4)
)
ibmTCPIPmvsUdpGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsUdpLastAct"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpIpOpts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpEntryState"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsUdpGroup.setStatus("obsolete")

ibmTCPIPmvsAtmSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 5)
)
ibmTCPIPmvsAtmSupportGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelSubType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelHwModel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelShared"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDeterNodeDesc"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelControlUnitNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCodeLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelEcLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelFlashLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelVtamId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortHardwareState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMediaType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortCodeLoadStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrBurntIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrActive"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMaxPcmConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortPcmName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBestEffort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVpi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVci"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdMaxAal5PduSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdMaxAal5PduSize"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmSupportGroup.setStatus("obsolete")

ibmTCPIPmvsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 6)
)
ibmTCPIPmvsObsoleteGroup.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmSNMPRemPing")
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsObsoleteGroup.setStatus("obsolete")

ibmTCPIPmvsInterfacesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 8)
)
ibmTCPIPmvsInterfacesGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDeviceType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceBaseNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIoBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceAutoRestart"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceNetmanEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceHostClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWorkstationClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIncomingSvcEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkDeviceIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkAdapterAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrCanonical"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrBcast"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsInterfacesGroup.setStatus("obsolete")

ibmTCPIPmvsAtmLeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 9)
)
ibmTCPIPmvsAtmLeGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcTi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcT1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcT2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaleMaxStations"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxSaps"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaleMaxIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeCrsGroupAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeUserData"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeClientEnableState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeBestEffortPeakRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxLECConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrEnableLoadBalancing"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrLoadBalancing"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrSessionDelay"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLanType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigMaxDataFrameSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLanName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLesAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxUnknownFrameCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxUnknownFrameTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecVccTimeoutPeriod"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxRetryCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecAgingTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecForwardDelayTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecExpectedArpResponseTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecFlushTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecPathSwitchingDelay"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLocalSegmentID"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendAvgRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendPeakRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConnectionCompleteTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecPrimaryAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecID"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecInterfaceState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLastFailureRespCode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLastFailureState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecProtocol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecTopologyChange"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigServerAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigSource"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualLanType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualMaxDataFrameSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualLanName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecProxyClient"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRequestsOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRequestsIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRepliesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRepliesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlFramesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlFramesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecSvcFailures"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMacAddress"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmLeGroup.setStatus("obsolete")

ibmTCPIPmvsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 10)
)
ibmTCPIPmvsPortGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsPortNumberLow"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortNumberHigh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortProtocol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortProcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortAutoLoggable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortDelayAcks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortSharePort"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsPortGroup.setStatus("obsolete")

ibmTCPIPmvsRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 11)
)
ibmTCPIPmvsRoutingGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsGatewayMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsGatewayMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsGatewayRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsGatewayVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsGatewayVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsGatewayDelayAcks"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsRoutingGroup.setStatus("current")

ibmTCPIPmvsTcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 12)
)
ibmTCPIPmvsTcpGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnActiveOpen"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnPendTcpRecv"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSig"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBackoffCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpDet"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpPol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTargetAppl"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClientUserId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLogMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnProto"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDupacks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptMaxSegmentSize"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup2.setStatus("obsolete")

ibmTCPIPmvsSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 13)
)
ibmTCPIPmvsSystemGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup2.setStatus("obsolete")

ibmTCPIPmvsAtmSupportGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 14)
)
ibmTCPIPmvsAtmSupportGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelSubType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelHwModel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelShared"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDeterNodeDesc"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelControlUnitNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCodeLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelEcLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelFlashLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelVtamId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortHardwareState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMediaType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortCodeLoadStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrBurntIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrActive"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMaxPcmConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortPcmName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5InPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5OutPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortIpAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBestEffort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVpi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVci"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdMaxAal5PduSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdMaxAal5PduSize"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmSupportGroup2.setStatus("obsolete")

ibmTCPIPmvsSystemGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 15)
)
ibmTCPIPmvsSystemGroup3.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpMaxReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMultipathEnabled"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup3.setStatus("obsolete")

ibmTCPIPmvsInterfacesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 16)
)
ibmTCPIPmvsInterfacesGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDeviceType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceBaseNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIoBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceAutoRestart"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceNetmanEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceHostClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWorkstationClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIncomingSvcEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkDeviceIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkAdapterAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrCanonical"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrBcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcastRefCount"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsInterfacesGroup2.setStatus("obsolete")

ibmTCPIPmvsUdpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 17)
)
ibmTCPIPmvsUdpGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsUdpLastAct"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpIpOpts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpEntryState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastTTL"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastLoopback"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastLinkAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvLinkAddr"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsUdpGroup2.setStatus("obsolete")

ibmTCPIPmvsSystemGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 18)
)
ibmTCPIPmvsSystemGroup4.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpMaxReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMultipathEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPathMtuDscEnabled"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup4.setStatus("obsolete")

ibmTCPIPmvsInterfacesGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 19)
)
ibmTCPIPmvsInterfacesGroup3.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDeviceType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceBaseNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIoBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceAutoRestart"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceNetmanEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceHostClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWorkstationClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIncomingSvcEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceRouterStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkDeviceIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkAdapterAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrCanonical"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrBcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkChecksumEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcastRefCount"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsInterfacesGroup3.setStatus("obsolete")

ibmTCPIPmvsTcpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 20)
)
ibmTCPIPmvsTcpGroup3.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnActiveOpen"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnPendTcpRecv"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSig"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBackoffCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpDet"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpPol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTargetAppl"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClientUserId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLogMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnProto"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDupacks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClusterConnFlag"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup3.setStatus("obsolete")

ibmTCPIPmvsSystemGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 21)
)
ibmTCPIPmvsSystemGroup5.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpMaxReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPathMtuDscEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMultipathType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpForwarding"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup5.setStatus("obsolete")

ibmTCPIPmvsTcpGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 22)
)
ibmTCPIPmvsTcpGroup4.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIpTos"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSig"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpDet"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpPol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTargetAppl"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClientUserId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLogMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnProto"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDupacks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClusterConnFlag"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInSegs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutSegs"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup4.setStatus("obsolete")

ibmTCPIPmvsAtmSupportGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 24)
)
ibmTCPIPmvsAtmSupportGroup3.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelSubType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelHwModel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelShared"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDeterNodeDesc"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelControlUnitNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCodeLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelEcLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelFlashLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortHardwareState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMediaType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortCodeLoadStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrBurntIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrActive"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMaxPcmConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortPcmName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5InPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5OutPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortIpAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBestEffort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVpi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVci"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdMaxAal5PduSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdMaxAal5PduSize"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmSupportGroup3.setStatus("obsolete")

ibmTCPIPmvsInterfacesGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 25)
)
ibmTCPIPmvsInterfacesGroup4.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDeviceType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceBaseNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIoBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceAutoRestart"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceNetmanEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceHostClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWorkstationClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIncomingSvcEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceRouterStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceActualRouterStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkDeviceIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkAdapterAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrCanonical"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrBcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkChecksumEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkArpSupport"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcastRefCount"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsInterfacesGroup4.setStatus("obsolete")

ibmTCPIPmvsPortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 26)
)
ibmTCPIPmvsPortGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsPortNumberLow"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortNumberHigh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortProtocol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortProcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortAutoLoggable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortDelayAcks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortSharePort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortBindIpAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortSAFResource"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPortReuse"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsPortGroup2.setStatus("current")

ibmTCPIPmvsAtmSupportGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 27)
)
ibmTCPIPmvsAtmSupportGroup4.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelSubType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelHwModel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelShared"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelNumPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelDeterNodeDesc"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelControlUnitNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCodeLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelCurLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelManParnNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfChannelFlashLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortHardwareState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMediaType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortUniVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixPrefix"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortNetPrefixStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortCodeLoadStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrBurntIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMacAddrActive"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortMaxPcmConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortPcmName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5InPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortAAL5OutPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPortIpAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBestEffort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdPeakCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdsustainCellRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdCellBurstSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVpi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcVci"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcFwdMaxAal5PduSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcBwdMaxAal5PduSize"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmSupportGroup4.setStatus("current")

ibmTCPIPmvsTcpGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 28)
)
ibmTCPIPmvsTcpGroup5.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSig"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpSel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpDet"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTcpPol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTargetAppl"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClientUserId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLogMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnProto"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDupacks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClusterConnFlag"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInSegs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutSegs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDSField"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup5.setStatus("obsolete")

ibmTCPIPmvsUdpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 29)
)
ibmTCPIPmvsUdpGroup3.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsUdpLastAct"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpIpOpts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDgramOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvLim"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpEntryState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastTTL"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastLoopback"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastLinkAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpDSField"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpMcastRecvLinkAddr"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsUdpGroup3.setStatus("current")

ibmTCPIPmvsAtmLeGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 30)
)
ibmTCPIPmvsAtmLeGroup2.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcTi"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcT1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeLlcT2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaleMaxStations"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxSaps"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaleMaxIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeCrsGroupAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeUserData"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeClientEnableState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeBestEffortPeakRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeMaxLECConnections"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrEnableLoadBalancing"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrLoadBalancing"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmSnaLeTrSessionDelay"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLanType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigMaxDataFrameSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLanName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigLesAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxUnknownFrameCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxUnknownFrameTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecVccTimeoutPeriod"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMaxRetryCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecAgingTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecForwardDelayTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecExpectedArpResponseTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecFlushTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecPathSwitchingDelay"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLocalSegmentID"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendAvgRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendPeakRate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConnectionCompleteTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecPortName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecPrimaryAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecID"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecInterfaceState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLastFailureRespCode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecLastFailureState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecProtocol"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecTopologyChange"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigServerAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigSource"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualLanType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualMaxDataFrameSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecActualLanName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecAtmAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecProxyClient"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRequestsOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRequestsIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRepliesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecArpRepliesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlFramesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlFramesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecSvcFailures"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecConfigDirectVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDirectVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecControlDistributeVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastSendVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdInterface"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdVPI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMulticastFwdVCI"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmLecMacAddress"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmLeGroup2.setStatus("current")

ibmTCPIPmvsSystemGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 31)
)
ibmTCPIPmvsSystemGroup6.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpMaxReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPathMtuDscEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMultipathType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpForwarding"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDevRetryDuration"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup6.setStatus("obsolete")

ibmTCPIPmvsTcpGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 32)
)
ibmTCPIPmvsTcpGroup6.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLastActivity"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnBytesOut"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptions"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndUna"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutgoingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInBuffered"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnUsrRcvNxt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingPush"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingUrg"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnIncomingWinSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnReXmtCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCongestionWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSSThresh"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRoundTripVariance"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitSndSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInitRcvSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSendMSS"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl1"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWl2"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndWnd"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRcvBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSubtask"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSockOpt"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnRttSeq"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTargetAppl"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClientUserId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnLogMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnProto"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDupacks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOptMaxSegmentSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnClusterConnFlag"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnInSegs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnOutSegs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnDSField"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnSndBufSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnAcceptCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnExceedBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnCurrBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnMaxBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnWindowScale"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnTimeStamp"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnServerResourceId"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpConnsClosed"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpPassiveDrops"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpTimeWaitReused"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpPredictAck"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpPredictData"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInDupAck"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInBadSum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInBadLen"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInShort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInPawsDrop"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInAllBeforeWin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInSomeBeforeWin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInAllAfterWin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInSomeAfterWin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInOutOfOrder"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInAfterClose"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInWinProbes"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpInWinUpdates"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpOutWinUpdates"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpOutDelayAcks"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpOutWinProbes"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRxmtTimers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRxmtDrops"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpPMTURxmts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpPMTUErrors"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpProbeDrops"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveProbes"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveDrops"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpFinwait2Drops"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerLocalAddrType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerLocalAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerLocalPort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerRemoteAddrType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerRemoteAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerRemotePort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerAcceptCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerExceedBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerCurrBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerMaxBacklog"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpListenerResourceName"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsTcpGroup6.setStatus("current")

ibmTCPIPmvsIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 33)
)
ibmTCPIPmvsIpGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsIpInDevLayerCalls"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpInUnpackErrors"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpInDiscardsMemory"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpOutDiscardsDlcSynch"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpOutDiscardsDlcAsynch"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpOutDiscardsMemory"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsIpGroup.setStatus("current")

ibmTCPIPmvsSystemGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 34)
)
ibmTCPIPmvsSystemGroup7.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsSubagentCacheTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIgnoreRedirect"),
        ("IBMTCPIPMVS-MIB", "ibmMvsArpCacheTimeout"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpKeepAliveTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpChecksum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIplDateAndTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsNoUdpQueueLimit"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSoMaxConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipAsid"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSourceVipaEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfSysplexName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfHostName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsasfProductVersion"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPrimaryInterfaceIfIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpMaxReassemblySize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRestrictLowPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpSendBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsUdpRecvBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipStatisticsEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsFirewallEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMaximumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMinimumRetransmitTime"),
        ("IBMTCPIPMVS-MIB", "ibmMvsRoundTripGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceMultiplier"),
        ("IBMTCPIPMVS-MIB", "ibmMvsVarianceGain"),
        ("IBMTCPIPMVS-MIB", "ibmMvsSendGarbageEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpMaxReceiveBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsPathMtuDscEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsMultipathType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsIpForwarding"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDevRetryDuration"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpFinwait2Time"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpTimeStamp"),
        ("IBMTCPIPMVS-MIB", "ibmMvsTcpipSubagentVersion"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemGroup7.setStatus("current")

ibmTCPIPmvsOsaExpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 35)
)
ibmTCPIPmvsOsaExpGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelSubType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelShared"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelNumPorts"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelDeterNodeDesc"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelControlUnitNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelCodeLevel"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelCurLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelCurLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelManLparName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelManLparNum"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelPCIBusUtil1Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelProcessorUtil1Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelPCIBusUtil5Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelProcessorUtil5Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelPCIBusUtilHour"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpChannelProcessorUtilHour"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfProcessorUtil1Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfInKbytesRate1Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfOutKbytesRate1Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfProcessorUtil5Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfInKbytesRate5Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfOutKbytesRate5Min"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfProcessorUtilHour"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfInKbytesRateHour"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpPerfOutKbytesRateHour"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortHardwareState"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortServiceMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortDisabledStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortConfigName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortConfigSpeed"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortActiveSpeed"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortMacAddrActive"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortMacAddrBurntIn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortUserData"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortOutPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortInPackets"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortInGroupFrames"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortInBroadcastFrames"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortInUnknownIPFrames"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthPortGroupMacAddrs"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthSnaInactTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthSnaRespTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthSnaAckTimer"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthSnaMaxIFramesBeforeAck"),
        ("IBMTCPIPMVS-MIB", "ibmMvsOsaExpEthSnaMaxTransmitWindow"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsOsaExpGroup.setStatus("current")

ibmTCPIPmvsInterfacesGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 36)
)
ibmTCPIPmvsInterfacesGroup5.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDeviceType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceBaseNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIoBufferSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceAutoRestart"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceNetmanEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceHostClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWorkstationClawName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceReadSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteBuffers"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceWriteSize"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceProcname"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceIncomingSvcEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceLuName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceRouterStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceActualRouterStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceConfigPackingMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDeviceActualPackingMode"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkDeviceIndex"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkAdapterAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkNumber"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrCanonical"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkIbmtrBcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcast"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkChecksumEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkArpSupport"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMacAddress"),
        ("IBMTCPIPMVS-MIB", "ibmMvsLinkMcastRefCount"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsInterfacesGroup5.setStatus("current")

ibmTCPIPmvsDVIPAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 37)
)
ibmTCPIPmvsDVIPAGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDVIPAMaskType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAMaskAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAOrigin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARank"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistributeStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAMoveable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrEnabled"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfMoveable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARangeConfStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnDynXcfIpAddrType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnDynXcfIpAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnPolicyRuleName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAConnPolicyActionName"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortReadyCount"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortTotalConn"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortWlmWeight"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrMulticastIpAddrType"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrMulticastIpAddr"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrPort"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrPasswordSpecified"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPATrapControl"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsDVIPAGroup.setStatus("current")


# Notification objects

ibmMvsAtmOsasfAtmPvcCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 1)
)
ibmMvsAtmOsasfAtmPvcCreate.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName")
)
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfAtmPvcCreate.setStatus(
        "current"
    )

ibmMvsAtmOsasfAtmPvcDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 2)
)
ibmMvsAtmOsasfAtmPvcDelete.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfPvcName")
)
if mibBuilder.loadTexts:
    ibmMvsAtmOsasfAtmPvcDelete.setStatus(
        "current"
    )

ibmMvsDVIPAStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 3)
)
ibmMvsDVIPAStatusChange.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDVIPAStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAOrigin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARank"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAMoveable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrEnabled"))
)
if mibBuilder.loadTexts:
    ibmMvsDVIPAStatusChange.setStatus(
        "current"
    )

ibmMvsDVIPARemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 4)
)
ibmMvsDVIPARemoved.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDVIPAStatus"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAOrigin"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARank"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAMoveable"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPAServMgrEnabled"))
)
if mibBuilder.loadTexts:
    ibmMvsDVIPARemoved.setStatus(
        "current"
    )

ibmMvsDVIPATargetAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 5)
)
ibmMvsDVIPATargetAdded.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfStatus")
)
if mibBuilder.loadTexts:
    ibmMvsDVIPATargetAdded.setStatus(
        "current"
    )

ibmMvsDVIPATargetRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 6)
)
ibmMvsDVIPATargetRemoved.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistConfStatus")
)
if mibBuilder.loadTexts:
    ibmMvsDVIPATargetRemoved.setStatus(
        "current"
    )

ibmMvsDVIPATargetServerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 7)
)
ibmMvsDVIPATargetServerStarted.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortReadyCount")
)
if mibBuilder.loadTexts:
    ibmMvsDVIPATargetServerStarted.setStatus(
        "current"
    )

ibmMvsDVIPATargetServerEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 8)
)
ibmMvsDVIPATargetServerEnded.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsDVIPADistPortReadyCount")
)
if mibBuilder.loadTexts:
    ibmMvsDVIPATargetServerEnded.setStatus(
        "current"
    )

ibmMvsTcpipSubagentColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 0, 9)
)
if mibBuilder.loadTexts:
    ibmMvsTcpipSubagentColdStart.setStatus(
        "current"
    )


# Notifications groups

ibmTCPIPmvsAtmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 7)
)
ibmTCPIPmvsAtmNotificationGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfAtmPvcCreate"),
        ("IBMTCPIPMVS-MIB", "ibmMvsAtmOsasfAtmPvcDelete"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsAtmNotificationGroup.setStatus(
        "current"
    )

ibmTCPIPmvsDVIPANotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 38)
)
ibmTCPIPmvsDVIPANotificationGroup.setObjects(
      *(("IBMTCPIPMVS-MIB", "ibmMvsDVIPAStatusChange"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPARemoved"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPATargetAdded"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPATargetRemoved"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPATargetServerStarted"),
        ("IBMTCPIPMVS-MIB", "ibmMvsDVIPATargetServerEnded"))
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsDVIPANotificationGroup.setStatus(
        "current"
    )

ibmTCPIPmvsSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 2, 39)
)
ibmTCPIPmvsSystemNotificationGroup.setObjects(
    ("IBMTCPIPMVS-MIB", "ibmMvsTcpipSubagentColdStart")
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsSystemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ibmTCPIPmvsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 19, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibmTCPIPmvsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMTCPIPMVS-MIB",
    **{"TypeOfService": TypeOfService,
       "DeviceLinkTypes": DeviceLinkTypes,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "mvsSNMPagent": mvsSNMPagent,
       "ibmSNMPRemPing": ibmSNMPRemPing,
       "ibmTCPIPmvsMIB": ibmTCPIPmvsMIB,
       "ibmTCPIPmvsMIBTraps": ibmTCPIPmvsMIBTraps,
       "ibmMvsAtmOsasfAtmPvcCreate": ibmMvsAtmOsasfAtmPvcCreate,
       "ibmMvsAtmOsasfAtmPvcDelete": ibmMvsAtmOsasfAtmPvcDelete,
       "ibmMvsDVIPAStatusChange": ibmMvsDVIPAStatusChange,
       "ibmMvsDVIPARemoved": ibmMvsDVIPARemoved,
       "ibmMvsDVIPATargetAdded": ibmMvsDVIPATargetAdded,
       "ibmMvsDVIPATargetRemoved": ibmMvsDVIPATargetRemoved,
       "ibmMvsDVIPATargetServerStarted": ibmMvsDVIPATargetServerStarted,
       "ibmMvsDVIPATargetServerEnded": ibmMvsDVIPATargetServerEnded,
       "ibmMvsTcpipSubagentColdStart": ibmMvsTcpipSubagentColdStart,
       "ibmTCPIPmvsAdmin": ibmTCPIPmvsAdmin,
       "ibmTCPIPmvsMIBObjects": ibmTCPIPmvsMIBObjects,
       "ibmRemotePingGroup": ibmRemotePingGroup,
       "ibmRemotePingTable": ibmRemotePingTable,
       "ibmRemotePingEntry": ibmRemotePingEntry,
       "ibmMvsRPingPacketSize": ibmMvsRPingPacketSize,
       "ibmMvsRPingTimeOut": ibmMvsRPingTimeOut,
       "ibmMvsRPingHostAddress": ibmMvsRPingHostAddress,
       "ibmMvsRPingResponseTime": ibmMvsRPingResponseTime,
       "ibmTcpipMvsSystem": ibmTcpipMvsSystem,
       "ibmMvsSubagentCacheTime": ibmMvsSubagentCacheTime,
       "ibmMvsIgnoreRedirect": ibmMvsIgnoreRedirect,
       "ibmMvsArpCacheTimeout": ibmMvsArpCacheTimeout,
       "ibmMvsTcpKeepAliveTimer": ibmMvsTcpKeepAliveTimer,
       "ibmMvsTcpReceiveBufferSize": ibmMvsTcpReceiveBufferSize,
       "ibmMvsTcpSendBufferSize": ibmMvsTcpSendBufferSize,
       "ibmMvsUdpChecksum": ibmMvsUdpChecksum,
       "ibmMvsIplDateAndTime": ibmMvsIplDateAndTime,
       "ibmMvsNoUdpQueueLimit": ibmMvsNoUdpQueueLimit,
       "ibmMvsSoMaxConn": ibmMvsSoMaxConn,
       "ibmMvsTcpipProcname": ibmMvsTcpipProcname,
       "ibmMvsTcpipAsid": ibmMvsTcpipAsid,
       "ibmMvsSourceVipaEnabled": ibmMvsSourceVipaEnabled,
       "ibmMvsOsasfSysplexName": ibmMvsOsasfSysplexName,
       "ibmMvsOsasfHostName": ibmMvsOsasfHostName,
       "ibmMvsOsasfProductVersion": ibmMvsOsasfProductVersion,
       "ibmMvsPrimaryInterfaceIfIndex": ibmMvsPrimaryInterfaceIfIndex,
       "ibmMvsIpMaxReassemblySize": ibmMvsIpMaxReassemblySize,
       "ibmMvsTcpRestrictLowPorts": ibmMvsTcpRestrictLowPorts,
       "ibmMvsUdpRestrictLowPorts": ibmMvsUdpRestrictLowPorts,
       "ibmMvsUdpSendBufferSize": ibmMvsUdpSendBufferSize,
       "ibmMvsUdpRecvBufferSize": ibmMvsUdpRecvBufferSize,
       "ibmMvsTcpipStatisticsEnabled": ibmMvsTcpipStatisticsEnabled,
       "ibmMvsFirewallEnabled": ibmMvsFirewallEnabled,
       "ibmMvsMaximumRetransmitTime": ibmMvsMaximumRetransmitTime,
       "ibmMvsMinimumRetransmitTime": ibmMvsMinimumRetransmitTime,
       "ibmMvsRoundTripGain": ibmMvsRoundTripGain,
       "ibmMvsVarianceGain": ibmMvsVarianceGain,
       "ibmMvsVarianceMultiplier": ibmMvsVarianceMultiplier,
       "ibmMvsSendGarbageEnabled": ibmMvsSendGarbageEnabled,
       "ibmMvsTcpMaxReceiveBufferSize": ibmMvsTcpMaxReceiveBufferSize,
       "ibmMvsMultipathEnabled": ibmMvsMultipathEnabled,
       "ibmMvsPathMtuDscEnabled": ibmMvsPathMtuDscEnabled,
       "ibmMvsMultipathType": ibmMvsMultipathType,
       "ibmMvsIpForwarding": ibmMvsIpForwarding,
       "ibmMvsDevRetryDuration": ibmMvsDevRetryDuration,
       "ibmMvsTcpFinwait2Time": ibmMvsTcpFinwait2Time,
       "ibmMvsTcpTimeStamp": ibmMvsTcpTimeStamp,
       "ibmMvsTcpipSubagentVersion": ibmMvsTcpipSubagentVersion,
       "ibmTcpipMvsInterfaceGroup": ibmTcpipMvsInterfaceGroup,
       "ibmTcpipMvsDeviceTable": ibmTcpipMvsDeviceTable,
       "ibmTcpipMvsDeviceEntry": ibmTcpipMvsDeviceEntry,
       "ibmMvsDeviceType": ibmMvsDeviceType,
       "ibmMvsDeviceBaseNumber": ibmMvsDeviceBaseNumber,
       "ibmMvsDeviceIoBufferSize": ibmMvsDeviceIoBufferSize,
       "ibmMvsDeviceAutoRestart": ibmMvsDeviceAutoRestart,
       "ibmMvsDeviceNetmanEnabled": ibmMvsDeviceNetmanEnabled,
       "ibmMvsDeviceHostClawName": ibmMvsDeviceHostClawName,
       "ibmMvsDeviceWorkstationClawName": ibmMvsDeviceWorkstationClawName,
       "ibmMvsDeviceReadBuffers": ibmMvsDeviceReadBuffers,
       "ibmMvsDeviceReadSize": ibmMvsDeviceReadSize,
       "ibmMvsDeviceWriteBuffers": ibmMvsDeviceWriteBuffers,
       "ibmMvsDeviceWriteSize": ibmMvsDeviceWriteSize,
       "ibmMvsDeviceProcname": ibmMvsDeviceProcname,
       "ibmMvsDeviceIncomingSvcEnabled": ibmMvsDeviceIncomingSvcEnabled,
       "ibmMvsDeviceLuName": ibmMvsDeviceLuName,
       "ibmMvsDeviceRouterStatus": ibmMvsDeviceRouterStatus,
       "ibmMvsDeviceActualRouterStatus": ibmMvsDeviceActualRouterStatus,
       "ibmMvsDeviceConfigPackingMode": ibmMvsDeviceConfigPackingMode,
       "ibmMvsDeviceActualPackingMode": ibmMvsDeviceActualPackingMode,
       "ibmTcpipMvsLinkTable": ibmTcpipMvsLinkTable,
       "ibmTcpipMvsLinkEntry": ibmTcpipMvsLinkEntry,
       "ibmMvsLinkType": ibmMvsLinkType,
       "ibmMvsLinkDeviceIndex": ibmMvsLinkDeviceIndex,
       "ibmMvsLinkAdapterAddr": ibmMvsLinkAdapterAddr,
       "ibmMvsLinkNumber": ibmMvsLinkNumber,
       "ibmMvsLinkIbmtrCanonical": ibmMvsLinkIbmtrCanonical,
       "ibmMvsLinkIbmtrBcast": ibmMvsLinkIbmtrBcast,
       "ibmMvsLinkMcast": ibmMvsLinkMcast,
       "ibmMvsLinkChecksumEnabled": ibmMvsLinkChecksumEnabled,
       "ibmMvsLinkArpSupport": ibmMvsLinkArpSupport,
       "ibmMvsLinkMacAddress": ibmMvsLinkMacAddress,
       "ibmTcpipMvsLinkMcastTable": ibmTcpipMvsLinkMcastTable,
       "ibmTcpipMvsLinkMcastEntry": ibmTcpipMvsLinkMcastEntry,
       "ibmMvsLinkMcastGroupAddr": ibmMvsLinkMcastGroupAddr,
       "ibmMvsLinkMcastRefCount": ibmMvsLinkMcastRefCount,
       "ibmTcpipMvsPortGroup": ibmTcpipMvsPortGroup,
       "ibmTcpipMvsPortTable": ibmTcpipMvsPortTable,
       "ibmTcpipMvsPortEntry": ibmTcpipMvsPortEntry,
       "ibmMvsPortNumberLow": ibmMvsPortNumberLow,
       "ibmMvsPortNumberHigh": ibmMvsPortNumberHigh,
       "ibmMvsPortProtocol": ibmMvsPortProtocol,
       "ibmMvsPortProcName": ibmMvsPortProcName,
       "ibmMvsPortAutoLoggable": ibmMvsPortAutoLoggable,
       "ibmMvsPortDelayAcks": ibmMvsPortDelayAcks,
       "ibmMvsPortOptMaxSegmentSize": ibmMvsPortOptMaxSegmentSize,
       "ibmMvsPortSharePort": ibmMvsPortSharePort,
       "ibmMvsPortBindIpAddr": ibmMvsPortBindIpAddr,
       "ibmMvsPortSAFResource": ibmMvsPortSAFResource,
       "ibmMvsPortReuse": ibmMvsPortReuse,
       "ibmTcpipMvsRouteGroup": ibmTcpipMvsRouteGroup,
       "ibmTcpipMvsGatewayTable": ibmTcpipMvsGatewayTable,
       "ibmTcpipMvsGatewayEntry": ibmTcpipMvsGatewayEntry,
       "ibmMvsGatewayMaximumRetransmitTime": ibmMvsGatewayMaximumRetransmitTime,
       "ibmMvsGatewayMinimumRetransmitTime": ibmMvsGatewayMinimumRetransmitTime,
       "ibmMvsGatewayRoundTripGain": ibmMvsGatewayRoundTripGain,
       "ibmMvsGatewayVarianceGain": ibmMvsGatewayVarianceGain,
       "ibmMvsGatewayVarianceMultiplier": ibmMvsGatewayVarianceMultiplier,
       "ibmMvsGatewayDelayAcks": ibmMvsGatewayDelayAcks,
       "ibmTcpipMvsAtmGroup": ibmTcpipMvsAtmGroup,
       "osasfChannelTable": osasfChannelTable,
       "osasfChannelEntry": osasfChannelEntry,
       "ibmMvsAtmOsasfChannelNumber": ibmMvsAtmOsasfChannelNumber,
       "ibmMvsAtmOsasfChannelType": ibmMvsAtmOsasfChannelType,
       "ibmMvsAtmOsasfChannelSubType": ibmMvsAtmOsasfChannelSubType,
       "ibmMvsAtmOsasfChannelMode": ibmMvsAtmOsasfChannelMode,
       "ibmMvsAtmOsasfChannelHwModel": ibmMvsAtmOsasfChannelHwModel,
       "ibmMvsAtmOsasfChannelState": ibmMvsAtmOsasfChannelState,
       "ibmMvsAtmOsasfChannelShared": ibmMvsAtmOsasfChannelShared,
       "ibmMvsAtmOsasfChannelNumPorts": ibmMvsAtmOsasfChannelNumPorts,
       "ibmMvsAtmOsasfChannelDeterNodeDesc": ibmMvsAtmOsasfChannelDeterNodeDesc,
       "ibmMvsAtmOsasfChannelControlUnitNumber": ibmMvsAtmOsasfChannelControlUnitNumber,
       "ibmMvsAtmOsasfChannelCodeLevel": ibmMvsAtmOsasfChannelCodeLevel,
       "ibmMvsAtmOsasfChannelEcLevel": ibmMvsAtmOsasfChannelEcLevel,
       "ibmMvsAtmOsasfChannelCurLparName": ibmMvsAtmOsasfChannelCurLparName,
       "ibmMvsAtmOsasfChannelCurLparNum": ibmMvsAtmOsasfChannelCurLparNum,
       "ibmMvsAtmOsasfChannelManParnName": ibmMvsAtmOsasfChannelManParnName,
       "ibmMvsAtmOsasfChannelManParnNum": ibmMvsAtmOsasfChannelManParnNum,
       "ibmMvsAtmOsasfChannelDate": ibmMvsAtmOsasfChannelDate,
       "ibmMvsAtmOsasfChannelTime": ibmMvsAtmOsasfChannelTime,
       "ibmMvsAtmOsasfChannelFlashLevel": ibmMvsAtmOsasfChannelFlashLevel,
       "ibmMvsAtmOsasfChannelVtamId": ibmMvsAtmOsasfChannelVtamId,
       "osasfPortTable": osasfPortTable,
       "osasfPortEntry": osasfPortEntry,
       "ibmMvsAtmOsasfPortNumber": ibmMvsAtmOsasfPortNumber,
       "ibmMvsAtmOsasfPortType": ibmMvsAtmOsasfPortType,
       "ibmMvsAtmOsasfPortHardwareState": ibmMvsAtmOsasfPortHardwareState,
       "ibmMvsAtmOsasfPortMediaType": ibmMvsAtmOsasfPortMediaType,
       "ibmMvsAtmOsasfPortUniType": ibmMvsAtmOsasfPortUniType,
       "ibmMvsAtmOsasfPortUniVersion": ibmMvsAtmOsasfPortUniVersion,
       "ibmMvsAtmOsasfPortNetPrefix": ibmMvsAtmOsasfPortNetPrefix,
       "ibmMvsAtmOsasfPortNetPrefixPrefix": ibmMvsAtmOsasfPortNetPrefixPrefix,
       "ibmMvsAtmOsasfPortNetPrefixStatus": ibmMvsAtmOsasfPortNetPrefixStatus,
       "ibmMvsAtmOsasfPortCodeLoadStatus": ibmMvsAtmOsasfPortCodeLoadStatus,
       "ibmMvsAtmOsasfPortMacAddrBurntIn": ibmMvsAtmOsasfPortMacAddrBurntIn,
       "ibmMvsAtmOsasfPortMacAddrActive": ibmMvsAtmOsasfPortMacAddrActive,
       "ibmMvsAtmOsasfPortMaxPcmConnections": ibmMvsAtmOsasfPortMaxPcmConnections,
       "ibmMvsAtmOsasfPortPcmName": ibmMvsAtmOsasfPortPcmName,
       "ibmMvsAtmOsasfPortAAL5InPackets": ibmMvsAtmOsasfPortAAL5InPackets,
       "ibmMvsAtmOsasfPortAAL5OutPackets": ibmMvsAtmOsasfPortAAL5OutPackets,
       "ibmMvsAtmOsasfPortIpAddress": ibmMvsAtmOsasfPortIpAddress,
       "osasfPvcTable": osasfPvcTable,
       "osasfPvcEntry": osasfPvcEntry,
       "ibmMvsAtmOsasfPvcName": ibmMvsAtmOsasfPvcName,
       "ibmMvsAtmOsasfPvcBestEffort": ibmMvsAtmOsasfPvcBestEffort,
       "ibmMvsAtmOsasfPvcFwdPeakCellRate": ibmMvsAtmOsasfPvcFwdPeakCellRate,
       "ibmMvsAtmOsasfPvcBwdPeakCellRate": ibmMvsAtmOsasfPvcBwdPeakCellRate,
       "ibmMvsAtmOsasfPvcFwdsustainCellRate": ibmMvsAtmOsasfPvcFwdsustainCellRate,
       "ibmMvsAtmOsasfPvcBwdsustainCellRate": ibmMvsAtmOsasfPvcBwdsustainCellRate,
       "ibmMvsAtmOsasfPvcFwdCellBurstSize": ibmMvsAtmOsasfPvcFwdCellBurstSize,
       "ibmMvsAtmOsasfPvcBwdCellBurstSize": ibmMvsAtmOsasfPvcBwdCellBurstSize,
       "ibmMvsAtmOsasfPvcVpi": ibmMvsAtmOsasfPvcVpi,
       "ibmMvsAtmOsasfPvcVci": ibmMvsAtmOsasfPvcVci,
       "ibmMvsAtmOsasfPvcFwdMaxAal5PduSize": ibmMvsAtmOsasfPvcFwdMaxAal5PduSize,
       "ibmMvsAtmOsasfPvcBwdMaxAal5PduSize": ibmMvsAtmOsasfPvcBwdMaxAal5PduSize,
       "ibmMvsAtmSnaLeTable": ibmMvsAtmSnaLeTable,
       "ibmMvsAtmSnaLeEntry": ibmMvsAtmSnaLeEntry,
       "ibmMvsAtmSnaLeLlcTi": ibmMvsAtmSnaLeLlcTi,
       "ibmMvsAtmSnaLeLlcT1": ibmMvsAtmSnaLeLlcT1,
       "ibmMvsAtmSnaLeLlcT2": ibmMvsAtmSnaLeLlcT2,
       "ibmMvsAtmSnaleMaxStations": ibmMvsAtmSnaleMaxStations,
       "ibmMvsAtmSnaLeMaxSaps": ibmMvsAtmSnaLeMaxSaps,
       "ibmMvsAtmSnaleMaxIn": ibmMvsAtmSnaleMaxIn,
       "ibmMvsAtmSnaLeMaxOut": ibmMvsAtmSnaLeMaxOut,
       "ibmMvsAtmSnaLeCrsGroupAddress": ibmMvsAtmSnaLeCrsGroupAddress,
       "ibmMvsAtmSnaLeUserData": ibmMvsAtmSnaLeUserData,
       "ibmMvsAtmSnaLeClientEnableState": ibmMvsAtmSnaLeClientEnableState,
       "ibmMvsAtmSnaLeBestEffortPeakRate": ibmMvsAtmSnaLeBestEffortPeakRate,
       "ibmMvsAtmSnaLeMaxLECConnections": ibmMvsAtmSnaLeMaxLECConnections,
       "ibmMvsAtmSnaLeTrEnableLoadBalancing": ibmMvsAtmSnaLeTrEnableLoadBalancing,
       "ibmMvsAtmSnaLeTrLoadBalancing": ibmMvsAtmSnaLeTrLoadBalancing,
       "ibmMvsAtmSnaLeTrSessionDelay": ibmMvsAtmSnaLeTrSessionDelay,
       "ibmMvsAtmLecConfigTable": ibmMvsAtmLecConfigTable,
       "ibmMvsAtmLecConfigEntry": ibmMvsAtmLecConfigEntry,
       "ibmMvsAtmLecConfigMode": ibmMvsAtmLecConfigMode,
       "ibmMvsAtmLecConfigLanType": ibmMvsAtmLecConfigLanType,
       "ibmMvsAtmLecConfigMaxDataFrameSize": ibmMvsAtmLecConfigMaxDataFrameSize,
       "ibmMvsAtmLecConfigLanName": ibmMvsAtmLecConfigLanName,
       "ibmMvsAtmLecConfigLesAtmAddress": ibmMvsAtmLecConfigLesAtmAddress,
       "ibmMvsAtmLecControlTimeout": ibmMvsAtmLecControlTimeout,
       "ibmMvsAtmLecMaxUnknownFrameCount": ibmMvsAtmLecMaxUnknownFrameCount,
       "ibmMvsAtmLecMaxUnknownFrameTime": ibmMvsAtmLecMaxUnknownFrameTime,
       "ibmMvsAtmLecVccTimeoutPeriod": ibmMvsAtmLecVccTimeoutPeriod,
       "ibmMvsAtmLecMaxRetryCount": ibmMvsAtmLecMaxRetryCount,
       "ibmMvsAtmLecAgingTime": ibmMvsAtmLecAgingTime,
       "ibmMvsAtmLecForwardDelayTime": ibmMvsAtmLecForwardDelayTime,
       "ibmMvsAtmLecExpectedArpResponseTime": ibmMvsAtmLecExpectedArpResponseTime,
       "ibmMvsAtmLecFlushTimeout": ibmMvsAtmLecFlushTimeout,
       "ibmMvsAtmLecPathSwitchingDelay": ibmMvsAtmLecPathSwitchingDelay,
       "ibmMvsAtmLecLocalSegmentID": ibmMvsAtmLecLocalSegmentID,
       "ibmMvsAtmLecMulticastSendType": ibmMvsAtmLecMulticastSendType,
       "ibmMvsAtmLecMulticastSendAvgRate": ibmMvsAtmLecMulticastSendAvgRate,
       "ibmMvsAtmLecMulticastSendPeakRate": ibmMvsAtmLecMulticastSendPeakRate,
       "ibmMvsAtmLecConnectionCompleteTimer": ibmMvsAtmLecConnectionCompleteTimer,
       "ibmMvsAtmLecPortName": ibmMvsAtmLecPortName,
       "ibmMvsAtmLecStatusTable": ibmMvsAtmLecStatusTable,
       "ibmMvsAtmLecStatusEntry": ibmMvsAtmLecStatusEntry,
       "ibmMvsAtmLecPrimaryAtmAddress": ibmMvsAtmLecPrimaryAtmAddress,
       "ibmMvsAtmLecID": ibmMvsAtmLecID,
       "ibmMvsAtmLecInterfaceState": ibmMvsAtmLecInterfaceState,
       "ibmMvsAtmLecLastFailureRespCode": ibmMvsAtmLecLastFailureRespCode,
       "ibmMvsAtmLecLastFailureState": ibmMvsAtmLecLastFailureState,
       "ibmMvsAtmLecProtocol": ibmMvsAtmLecProtocol,
       "ibmMvsAtmLecVersion": ibmMvsAtmLecVersion,
       "ibmMvsAtmLecTopologyChange": ibmMvsAtmLecTopologyChange,
       "ibmMvsAtmLecConfigServerAtmAddress": ibmMvsAtmLecConfigServerAtmAddress,
       "ibmMvsAtmLecConfigSource": ibmMvsAtmLecConfigSource,
       "ibmMvsAtmLecActualLanType": ibmMvsAtmLecActualLanType,
       "ibmMvsAtmLecActualMaxDataFrameSize": ibmMvsAtmLecActualMaxDataFrameSize,
       "ibmMvsAtmLecActualLanName": ibmMvsAtmLecActualLanName,
       "ibmMvsAtmLecAtmAddress": ibmMvsAtmLecAtmAddress,
       "ibmMvsAtmLecProxyClient": ibmMvsAtmLecProxyClient,
       "ibmMvsAtmLecStatisticsTable": ibmMvsAtmLecStatisticsTable,
       "ibmMvsAtmLecStatisticsEntry": ibmMvsAtmLecStatisticsEntry,
       "ibmMvsAtmLecArpRequestsOut": ibmMvsAtmLecArpRequestsOut,
       "ibmMvsAtmLecArpRequestsIn": ibmMvsAtmLecArpRequestsIn,
       "ibmMvsAtmLecArpRepliesOut": ibmMvsAtmLecArpRepliesOut,
       "ibmMvsAtmLecArpRepliesIn": ibmMvsAtmLecArpRepliesIn,
       "ibmMvsAtmLecControlFramesOut": ibmMvsAtmLecControlFramesOut,
       "ibmMvsAtmLecControlFramesIn": ibmMvsAtmLecControlFramesIn,
       "ibmMvsAtmLecSvcFailures": ibmMvsAtmLecSvcFailures,
       "ibmMvsAtmLecServerTable": ibmMvsAtmLecServerTable,
       "ibmMvsAtmLecServerEntry": ibmMvsAtmLecServerEntry,
       "ibmMvsAtmLecConfigDirectInterface": ibmMvsAtmLecConfigDirectInterface,
       "ibmMvsAtmLecConfigDirectVPI": ibmMvsAtmLecConfigDirectVPI,
       "ibmMvsAtmLecConfigDirectVCI": ibmMvsAtmLecConfigDirectVCI,
       "ibmMvsAtmLecControlDirectInterface": ibmMvsAtmLecControlDirectInterface,
       "ibmMvsAtmLecControlDirectVPI": ibmMvsAtmLecControlDirectVPI,
       "ibmMvsAtmLecControlDirectVCI": ibmMvsAtmLecControlDirectVCI,
       "ibmMvsAtmLecControlDistributeInterface": ibmMvsAtmLecControlDistributeInterface,
       "ibmMvsAtmLecControlDistributeVPI": ibmMvsAtmLecControlDistributeVPI,
       "ibmMvsAtmLecControlDistributeVCI": ibmMvsAtmLecControlDistributeVCI,
       "ibmMvsAtmLecMulticastSendInterface": ibmMvsAtmLecMulticastSendInterface,
       "ibmMvsAtmLecMulticastSendVPI": ibmMvsAtmLecMulticastSendVPI,
       "ibmMvsAtmLecMulticastSendVCI": ibmMvsAtmLecMulticastSendVCI,
       "ibmMvsAtmLecMulticastFwdInterface": ibmMvsAtmLecMulticastFwdInterface,
       "ibmMvsAtmLecMulticastFwdVPI": ibmMvsAtmLecMulticastFwdVPI,
       "ibmMvsAtmLecMulticastFwdVCI": ibmMvsAtmLecMulticastFwdVCI,
       "ibmMvsAtmLecMacAddressTable": ibmMvsAtmLecMacAddressTable,
       "ibmMvsAtmLecMacAddressEntry": ibmMvsAtmLecMacAddressEntry,
       "ibmMvsAtmLecMacAddress": ibmMvsAtmLecMacAddress,
       "ibmTcpipMvsTcpGroup": ibmTcpipMvsTcpGroup,
       "ibmTcpipMvsTcpConnTable": ibmTcpipMvsTcpConnTable,
       "ibmTcpipMvsTcpConnEntry": ibmTcpipMvsTcpConnEntry,
       "ibmMvsTcpConnLastActivity": ibmMvsTcpConnLastActivity,
       "ibmMvsTcpConnBytesIn": ibmMvsTcpConnBytesIn,
       "ibmMvsTcpConnBytesOut": ibmMvsTcpConnBytesOut,
       "ibmMvsTcpConnActiveOpen": ibmMvsTcpConnActiveOpen,
       "ibmMvsTcpConnIpTos": ibmMvsTcpConnIpTos,
       "ibmMvsTcpConnOptions": ibmMvsTcpConnOptions,
       "ibmMvsTcpConnOutBuffered": ibmMvsTcpConnOutBuffered,
       "ibmMvsTcpConnUsrSndNxt": ibmMvsTcpConnUsrSndNxt,
       "ibmMvsTcpConnSndNxt": ibmMvsTcpConnSndNxt,
       "ibmMvsTcpConnSndUna": ibmMvsTcpConnSndUna,
       "ibmMvsTcpConnOutgoingPush": ibmMvsTcpConnOutgoingPush,
       "ibmMvsTcpConnOutgoingUrg": ibmMvsTcpConnOutgoingUrg,
       "ibmMvsTcpConnOutgoingWinSeq": ibmMvsTcpConnOutgoingWinSeq,
       "ibmMvsTcpConnSendWindowSeq": ibmMvsTcpConnSendWindowSeq,
       "ibmMvsTcpConnSendWindowAck": ibmMvsTcpConnSendWindowAck,
       "ibmMvsTcpConnInBuffered": ibmMvsTcpConnInBuffered,
       "ibmMvsTcpConnRcvNxt": ibmMvsTcpConnRcvNxt,
       "ibmMvsTcpConnUsrRcvNxt": ibmMvsTcpConnUsrRcvNxt,
       "ibmMvsTcpConnIncomingPush": ibmMvsTcpConnIncomingPush,
       "ibmMvsTcpConnIncomingUrg": ibmMvsTcpConnIncomingUrg,
       "ibmMvsTcpConnIncomingWinSeq": ibmMvsTcpConnIncomingWinSeq,
       "ibmMvsTcpConnReXmt": ibmMvsTcpConnReXmt,
       "ibmMvsTcpConnMaxSndWnd": ibmMvsTcpConnMaxSndWnd,
       "ibmMvsTcpConnReXmtCount": ibmMvsTcpConnReXmtCount,
       "ibmMvsTcpConnCongestionWnd": ibmMvsTcpConnCongestionWnd,
       "ibmMvsTcpConnSSThresh": ibmMvsTcpConnSSThresh,
       "ibmMvsTcpConnRoundTripTime": ibmMvsTcpConnRoundTripTime,
       "ibmMvsTcpConnRoundTripVariance": ibmMvsTcpConnRoundTripVariance,
       "ibmMvsTcpConnInitSndSeq": ibmMvsTcpConnInitSndSeq,
       "ibmMvsTcpConnInitRcvSeq": ibmMvsTcpConnInitRcvSeq,
       "ibmMvsTcpConnSendMSS": ibmMvsTcpConnSendMSS,
       "ibmMvsTcpConnSndWl1": ibmMvsTcpConnSndWl1,
       "ibmMvsTcpConnSndWl2": ibmMvsTcpConnSndWl2,
       "ibmMvsTcpConnSndWnd": ibmMvsTcpConnSndWnd,
       "ibmMvsTcpConnPendTcpRecv": ibmMvsTcpConnPendTcpRecv,
       "ibmMvsTcpConnRcvBufSize": ibmMvsTcpConnRcvBufSize,
       "ibmMvsTcpConnResourceName": ibmMvsTcpConnResourceName,
       "ibmMvsTcpConnSubtask": ibmMvsTcpConnSubtask,
       "ibmMvsTcpConnResourceId": ibmMvsTcpConnResourceId,
       "ibmMvsTcpConnSockOpt": ibmMvsTcpConnSockOpt,
       "ibmMvsTcpConnTcpTimer": ibmMvsTcpConnTcpTimer,
       "ibmMvsTcpConnTcpSig": ibmMvsTcpConnTcpSig,
       "ibmMvsTcpConnTcpSel": ibmMvsTcpConnTcpSel,
       "ibmMvsTcpConnRttSeq": ibmMvsTcpConnRttSeq,
       "ibmMvsTcpConnBackoffCount": ibmMvsTcpConnBackoffCount,
       "ibmMvsTcpConnTcpDet": ibmMvsTcpConnTcpDet,
       "ibmMvsTcpConnTcpPol": ibmMvsTcpConnTcpPol,
       "ibmMvsTcpConnTargetAppl": ibmMvsTcpConnTargetAppl,
       "ibmMvsTcpConnLuName": ibmMvsTcpConnLuName,
       "ibmMvsTcpConnClientUserId": ibmMvsTcpConnClientUserId,
       "ibmMvsTcpConnLogMode": ibmMvsTcpConnLogMode,
       "ibmMvsTcpConnProto": ibmMvsTcpConnProto,
       "ibmMvsTcpConnDupacks": ibmMvsTcpConnDupacks,
       "ibmMvsTcpConnOptMaxSegmentSize": ibmMvsTcpConnOptMaxSegmentSize,
       "ibmMvsTcpConnClusterConnFlag": ibmMvsTcpConnClusterConnFlag,
       "ibmMvsTcpConnInSegs": ibmMvsTcpConnInSegs,
       "ibmMvsTcpConnOutSegs": ibmMvsTcpConnOutSegs,
       "ibmMvsTcpConnDSField": ibmMvsTcpConnDSField,
       "ibmMvsTcpConnSndBufSize": ibmMvsTcpConnSndBufSize,
       "ibmMvsTcpConnAcceptCount": ibmMvsTcpConnAcceptCount,
       "ibmMvsTcpConnExceedBacklog": ibmMvsTcpConnExceedBacklog,
       "ibmMvsTcpConnCurrBacklog": ibmMvsTcpConnCurrBacklog,
       "ibmMvsTcpConnMaxBacklog": ibmMvsTcpConnMaxBacklog,
       "ibmMvsTcpConnWindowScale": ibmMvsTcpConnWindowScale,
       "ibmMvsTcpConnTimeStamp": ibmMvsTcpConnTimeStamp,
       "ibmMvsTcpConnServerResourceId": ibmMvsTcpConnServerResourceId,
       "ibmMvsTcpConnsClosed": ibmMvsTcpConnsClosed,
       "ibmMvsTcpPassiveDrops": ibmMvsTcpPassiveDrops,
       "ibmMvsTcpTimeWaitReused": ibmMvsTcpTimeWaitReused,
       "ibmMvsTcpPredictAck": ibmMvsTcpPredictAck,
       "ibmMvsTcpPredictData": ibmMvsTcpPredictData,
       "ibmMvsTcpInDupAck": ibmMvsTcpInDupAck,
       "ibmMvsTcpInBadSum": ibmMvsTcpInBadSum,
       "ibmMvsTcpInBadLen": ibmMvsTcpInBadLen,
       "ibmMvsTcpInShort": ibmMvsTcpInShort,
       "ibmMvsTcpInPawsDrop": ibmMvsTcpInPawsDrop,
       "ibmMvsTcpInAllBeforeWin": ibmMvsTcpInAllBeforeWin,
       "ibmMvsTcpInSomeBeforeWin": ibmMvsTcpInSomeBeforeWin,
       "ibmMvsTcpInAllAfterWin": ibmMvsTcpInAllAfterWin,
       "ibmMvsTcpInSomeAfterWin": ibmMvsTcpInSomeAfterWin,
       "ibmMvsTcpInOutOfOrder": ibmMvsTcpInOutOfOrder,
       "ibmMvsTcpInAfterClose": ibmMvsTcpInAfterClose,
       "ibmMvsTcpInWinProbes": ibmMvsTcpInWinProbes,
       "ibmMvsTcpInWinUpdates": ibmMvsTcpInWinUpdates,
       "ibmMvsTcpOutWinUpdates": ibmMvsTcpOutWinUpdates,
       "ibmMvsTcpOutDelayAcks": ibmMvsTcpOutDelayAcks,
       "ibmMvsTcpOutWinProbes": ibmMvsTcpOutWinProbes,
       "ibmMvsTcpRxmtTimers": ibmMvsTcpRxmtTimers,
       "ibmMvsTcpRxmtDrops": ibmMvsTcpRxmtDrops,
       "ibmMvsTcpPMTURxmts": ibmMvsTcpPMTURxmts,
       "ibmMvsTcpPMTUErrors": ibmMvsTcpPMTUErrors,
       "ibmMvsTcpProbeDrops": ibmMvsTcpProbeDrops,
       "ibmMvsTcpKeepAliveProbes": ibmMvsTcpKeepAliveProbes,
       "ibmMvsTcpKeepAliveDrops": ibmMvsTcpKeepAliveDrops,
       "ibmMvsTcpFinwait2Drops": ibmMvsTcpFinwait2Drops,
       "ibmTcpipMvsTcpListenerTable": ibmTcpipMvsTcpListenerTable,
       "ibmTcpipMvsTcpListenerEntry": ibmTcpipMvsTcpListenerEntry,
       "ibmMvsTcpListenerResourceId": ibmMvsTcpListenerResourceId,
       "ibmMvsTcpListenerLocalAddrType": ibmMvsTcpListenerLocalAddrType,
       "ibmMvsTcpListenerLocalAddr": ibmMvsTcpListenerLocalAddr,
       "ibmMvsTcpListenerLocalPort": ibmMvsTcpListenerLocalPort,
       "ibmMvsTcpListenerRemoteAddrType": ibmMvsTcpListenerRemoteAddrType,
       "ibmMvsTcpListenerRemoteAddr": ibmMvsTcpListenerRemoteAddr,
       "ibmMvsTcpListenerRemotePort": ibmMvsTcpListenerRemotePort,
       "ibmMvsTcpListenerAcceptCount": ibmMvsTcpListenerAcceptCount,
       "ibmMvsTcpListenerExceedBacklog": ibmMvsTcpListenerExceedBacklog,
       "ibmMvsTcpListenerCurrBacklog": ibmMvsTcpListenerCurrBacklog,
       "ibmMvsTcpListenerMaxBacklog": ibmMvsTcpListenerMaxBacklog,
       "ibmMvsTcpListenerResourceName": ibmMvsTcpListenerResourceName,
       "ibmTcpipMvsUdpGroup": ibmTcpipMvsUdpGroup,
       "ibmTcpipMvsUdpTable": ibmTcpipMvsUdpTable,
       "ibmTcpipMvsUdpEntry": ibmTcpipMvsUdpEntry,
       "ibmMvsUdpLastAct": ibmMvsUdpLastAct,
       "ibmMvsUdpTos": ibmMvsUdpTos,
       "ibmMvsUdpIpOpts": ibmMvsUdpIpOpts,
       "ibmMvsUdpDgramIn": ibmMvsUdpDgramIn,
       "ibmMvsUdpBytesIn": ibmMvsUdpBytesIn,
       "ibmMvsUdpDgramOut": ibmMvsUdpDgramOut,
       "ibmMvsUdpBytesOut": ibmMvsUdpBytesOut,
       "ibmMvsUdpResourceName": ibmMvsUdpResourceName,
       "ibmMvsUdpSubtask": ibmMvsUdpSubtask,
       "ibmMvsUdpResourceId": ibmMvsUdpResourceId,
       "ibmMvsUdpSockOpt": ibmMvsUdpSockOpt,
       "ibmMvsUdpSendLim": ibmMvsUdpSendLim,
       "ibmMvsUdpRecvLim": ibmMvsUdpRecvLim,
       "ibmMvsUdpEntryState": ibmMvsUdpEntryState,
       "ibmMvsUdpMcastTTL": ibmMvsUdpMcastTTL,
       "ibmMvsUdpMcastLoopback": ibmMvsUdpMcastLoopback,
       "ibmMvsUdpMcastLinkAddr": ibmMvsUdpMcastLinkAddr,
       "ibmMvsUdpDSField": ibmMvsUdpDSField,
       "ibmTcpipMvsUdpMcastRecvTable": ibmTcpipMvsUdpMcastRecvTable,
       "ibmTcpipMvsUdpMcastRecvEntry": ibmTcpipMvsUdpMcastRecvEntry,
       "ibmMvsUdpMcastRecvLocalAddress": ibmMvsUdpMcastRecvLocalAddress,
       "ibmMvsUdpMcastRecvLocalPort": ibmMvsUdpMcastRecvLocalPort,
       "ibmMvsUdpMcastRecvGroup": ibmMvsUdpMcastRecvGroup,
       "ibmMvsUdpMcastRecvLinkAddr": ibmMvsUdpMcastRecvLinkAddr,
       "ibmTcpipMvsIpGroup": ibmTcpipMvsIpGroup,
       "ibmMvsIpInDevLayerCalls": ibmMvsIpInDevLayerCalls,
       "ibmMvsIpInUnpackErrors": ibmMvsIpInUnpackErrors,
       "ibmMvsIpInDiscardsMemory": ibmMvsIpInDiscardsMemory,
       "ibmMvsIpOutDiscardsDlcSynch": ibmMvsIpOutDiscardsDlcSynch,
       "ibmMvsIpOutDiscardsDlcAsynch": ibmMvsIpOutDiscardsDlcAsynch,
       "ibmMvsIpOutDiscardsMemory": ibmMvsIpOutDiscardsMemory,
       "ibmTcpipMvsOsaExpGroup": ibmTcpipMvsOsaExpGroup,
       "osaexpChannelTable": osaexpChannelTable,
       "osaexpChannelEntry": osaexpChannelEntry,
       "ibmMvsOsaExpChannelNumber": ibmMvsOsaExpChannelNumber,
       "ibmMvsOsaExpChannelType": ibmMvsOsaExpChannelType,
       "ibmMvsOsaExpChannelSubType": ibmMvsOsaExpChannelSubType,
       "ibmMvsOsaExpChannelMode": ibmMvsOsaExpChannelMode,
       "ibmMvsOsaExpChannelState": ibmMvsOsaExpChannelState,
       "ibmMvsOsaExpChannelShared": ibmMvsOsaExpChannelShared,
       "ibmMvsOsaExpChannelNumPorts": ibmMvsOsaExpChannelNumPorts,
       "ibmMvsOsaExpChannelDeterNodeDesc": ibmMvsOsaExpChannelDeterNodeDesc,
       "ibmMvsOsaExpChannelControlUnitNumber": ibmMvsOsaExpChannelControlUnitNumber,
       "ibmMvsOsaExpChannelCodeLevel": ibmMvsOsaExpChannelCodeLevel,
       "ibmMvsOsaExpChannelCurLparName": ibmMvsOsaExpChannelCurLparName,
       "ibmMvsOsaExpChannelCurLparNum": ibmMvsOsaExpChannelCurLparNum,
       "ibmMvsOsaExpChannelManLparName": ibmMvsOsaExpChannelManLparName,
       "ibmMvsOsaExpChannelManLparNum": ibmMvsOsaExpChannelManLparNum,
       "ibmMvsOsaExpChannelPCIBusUtil1Min": ibmMvsOsaExpChannelPCIBusUtil1Min,
       "ibmMvsOsaExpChannelProcessorUtil1Min": ibmMvsOsaExpChannelProcessorUtil1Min,
       "ibmMvsOsaExpChannelPCIBusUtil5Min": ibmMvsOsaExpChannelPCIBusUtil5Min,
       "ibmMvsOsaExpChannelProcessorUtil5Min": ibmMvsOsaExpChannelProcessorUtil5Min,
       "ibmMvsOsaExpChannelPCIBusUtilHour": ibmMvsOsaExpChannelPCIBusUtilHour,
       "ibmMvsOsaExpChannelProcessorUtilHour": ibmMvsOsaExpChannelProcessorUtilHour,
       "osaexpPerfTable": osaexpPerfTable,
       "osaexpPerfEntry": osaexpPerfEntry,
       "ibmMvsOsaExpPerfLparNum": ibmMvsOsaExpPerfLparNum,
       "ibmMvsOsaExpPerfProcessorUtil1Min": ibmMvsOsaExpPerfProcessorUtil1Min,
       "ibmMvsOsaExpPerfInKbytesRate1Min": ibmMvsOsaExpPerfInKbytesRate1Min,
       "ibmMvsOsaExpPerfOutKbytesRate1Min": ibmMvsOsaExpPerfOutKbytesRate1Min,
       "ibmMvsOsaExpPerfProcessorUtil5Min": ibmMvsOsaExpPerfProcessorUtil5Min,
       "ibmMvsOsaExpPerfInKbytesRate5Min": ibmMvsOsaExpPerfInKbytesRate5Min,
       "ibmMvsOsaExpPerfOutKbytesRate5Min": ibmMvsOsaExpPerfOutKbytesRate5Min,
       "ibmMvsOsaExpPerfProcessorUtilHour": ibmMvsOsaExpPerfProcessorUtilHour,
       "ibmMvsOsaExpPerfInKbytesRateHour": ibmMvsOsaExpPerfInKbytesRateHour,
       "ibmMvsOsaExpPerfOutKbytesRateHour": ibmMvsOsaExpPerfOutKbytesRateHour,
       "osaexpEthPortTable": osaexpEthPortTable,
       "osaexpEthPortEntry": osaexpEthPortEntry,
       "ibmMvsOsaExpEthPortNumber": ibmMvsOsaExpEthPortNumber,
       "ibmMvsOsaExpEthPortType": ibmMvsOsaExpEthPortType,
       "ibmMvsOsaExpEthPortHardwareState": ibmMvsOsaExpEthPortHardwareState,
       "ibmMvsOsaExpEthPortServiceMode": ibmMvsOsaExpEthPortServiceMode,
       "ibmMvsOsaExpEthPortDisabledStatus": ibmMvsOsaExpEthPortDisabledStatus,
       "ibmMvsOsaExpEthPortConfigName": ibmMvsOsaExpEthPortConfigName,
       "ibmMvsOsaExpEthPortConfigSpeed": ibmMvsOsaExpEthPortConfigSpeed,
       "ibmMvsOsaExpEthPortActiveSpeed": ibmMvsOsaExpEthPortActiveSpeed,
       "ibmMvsOsaExpEthPortMacAddrActive": ibmMvsOsaExpEthPortMacAddrActive,
       "ibmMvsOsaExpEthPortMacAddrBurntIn": ibmMvsOsaExpEthPortMacAddrBurntIn,
       "ibmMvsOsaExpEthPortUserData": ibmMvsOsaExpEthPortUserData,
       "ibmMvsOsaExpEthPortOutPackets": ibmMvsOsaExpEthPortOutPackets,
       "ibmMvsOsaExpEthPortInPackets": ibmMvsOsaExpEthPortInPackets,
       "ibmMvsOsaExpEthPortInGroupFrames": ibmMvsOsaExpEthPortInGroupFrames,
       "ibmMvsOsaExpEthPortInBroadcastFrames": ibmMvsOsaExpEthPortInBroadcastFrames,
       "ibmMvsOsaExpEthPortName": ibmMvsOsaExpEthPortName,
       "ibmMvsOsaExpEthPortInUnknownIPFrames": ibmMvsOsaExpEthPortInUnknownIPFrames,
       "ibmMvsOsaExpEthPortGroupMacAddrs": ibmMvsOsaExpEthPortGroupMacAddrs,
       "osaexpEthSnaTable": osaexpEthSnaTable,
       "osaexpEthSnaEntry": osaexpEthSnaEntry,
       "ibmMvsOsaExpEthSnaInactTimer": ibmMvsOsaExpEthSnaInactTimer,
       "ibmMvsOsaExpEthSnaRespTimer": ibmMvsOsaExpEthSnaRespTimer,
       "ibmMvsOsaExpEthSnaAckTimer": ibmMvsOsaExpEthSnaAckTimer,
       "ibmMvsOsaExpEthSnaMaxIFramesBeforeAck": ibmMvsOsaExpEthSnaMaxIFramesBeforeAck,
       "ibmMvsOsaExpEthSnaMaxTransmitWindow": ibmMvsOsaExpEthSnaMaxTransmitWindow,
       "ibmTcpipMvsDVIPAGroup": ibmTcpipMvsDVIPAGroup,
       "ibmMvsDVIPATable": ibmMvsDVIPATable,
       "ibmMvsDVIPAEntry": ibmMvsDVIPAEntry,
       "ibmMvsDVIPAIpAddrType": ibmMvsDVIPAIpAddrType,
       "ibmMvsDVIPAIpAddr": ibmMvsDVIPAIpAddr,
       "ibmMvsDVIPAMaskType": ibmMvsDVIPAMaskType,
       "ibmMvsDVIPAMaskAddr": ibmMvsDVIPAMaskAddr,
       "ibmMvsDVIPAStatus": ibmMvsDVIPAStatus,
       "ibmMvsDVIPAOrigin": ibmMvsDVIPAOrigin,
       "ibmMvsDVIPARank": ibmMvsDVIPARank,
       "ibmMvsDVIPADistributeStatus": ibmMvsDVIPADistributeStatus,
       "ibmMvsDVIPAMoveable": ibmMvsDVIPAMoveable,
       "ibmMvsDVIPAServMgrEnabled": ibmMvsDVIPAServMgrEnabled,
       "ibmMvsDVIPARangeConfTable": ibmMvsDVIPARangeConfTable,
       "ibmMvsDVIPARangeConfEntry": ibmMvsDVIPARangeConfEntry,
       "ibmMvsDVIPARangeConfIpAddrType": ibmMvsDVIPARangeConfIpAddrType,
       "ibmMvsDVIPARangeConfIpAddr": ibmMvsDVIPARangeConfIpAddr,
       "ibmMvsDVIPARangeConfMaskType": ibmMvsDVIPARangeConfMaskType,
       "ibmMvsDVIPARangeConfMaskAddr": ibmMvsDVIPARangeConfMaskAddr,
       "ibmMvsDVIPARangeConfMoveable": ibmMvsDVIPARangeConfMoveable,
       "ibmMvsDVIPARangeConfStatus": ibmMvsDVIPARangeConfStatus,
       "ibmMvsDVIPADistConfTable": ibmMvsDVIPADistConfTable,
       "ibmMvsDVIPADistConfEntry": ibmMvsDVIPADistConfEntry,
       "ibmMvsDVIPADistConfIpAddrType": ibmMvsDVIPADistConfIpAddrType,
       "ibmMvsDVIPADistConfIpAddr": ibmMvsDVIPADistConfIpAddr,
       "ibmMvsDVIPADistConfPort": ibmMvsDVIPADistConfPort,
       "ibmMvsDVIPADistConfTargetDynXcfIpAddrType": ibmMvsDVIPADistConfTargetDynXcfIpAddrType,
       "ibmMvsDVIPADistConfTargetDynXcfIpAddr": ibmMvsDVIPADistConfTargetDynXcfIpAddr,
       "ibmMvsDVIPADistConfStatus": ibmMvsDVIPADistConfStatus,
       "ibmMvsDVIPAConnRoutingTable": ibmMvsDVIPAConnRoutingTable,
       "ibmMvsDVIPAConnRoutingEntry": ibmMvsDVIPAConnRoutingEntry,
       "ibmMvsDVIPAConnPort": ibmMvsDVIPAConnPort,
       "ibmMvsDVIPAConnRemIpAddrType": ibmMvsDVIPAConnRemIpAddrType,
       "ibmMvsDVIPAConnRemIpAddr": ibmMvsDVIPAConnRemIpAddr,
       "ibmMvsDVIPAConnRemPort": ibmMvsDVIPAConnRemPort,
       "ibmMvsDVIPAConnDynXcfIpAddrType": ibmMvsDVIPAConnDynXcfIpAddrType,
       "ibmMvsDVIPAConnDynXcfIpAddr": ibmMvsDVIPAConnDynXcfIpAddr,
       "ibmMvsDVIPAConnPolicyRuleName": ibmMvsDVIPAConnPolicyRuleName,
       "ibmMvsDVIPAConnPolicyActionName": ibmMvsDVIPAConnPolicyActionName,
       "ibmMvsDVIPADistPortTable": ibmMvsDVIPADistPortTable,
       "ibmMvsDVIPADistPortEntry": ibmMvsDVIPADistPortEntry,
       "ibmMvsDVIPADistPortPort": ibmMvsDVIPADistPortPort,
       "ibmMvsDVIPADistPortTargetDynXcfIpAddrType": ibmMvsDVIPADistPortTargetDynXcfIpAddrType,
       "ibmMvsDVIPADistPortTargetDynXcfIpAddr": ibmMvsDVIPADistPortTargetDynXcfIpAddr,
       "ibmMvsDVIPADistPortReadyCount": ibmMvsDVIPADistPortReadyCount,
       "ibmMvsDVIPADistPortTotalConn": ibmMvsDVIPADistPortTotalConn,
       "ibmMvsDVIPADistPortWlmWeight": ibmMvsDVIPADistPortWlmWeight,
       "ibmMvsDVIPAServMgrMulticastIpAddrType": ibmMvsDVIPAServMgrMulticastIpAddrType,
       "ibmMvsDVIPAServMgrMulticastIpAddr": ibmMvsDVIPAServMgrMulticastIpAddr,
       "ibmMvsDVIPAServMgrPort": ibmMvsDVIPAServMgrPort,
       "ibmMvsDVIPAServMgrPasswordSpecified": ibmMvsDVIPAServMgrPasswordSpecified,
       "ibmMvsDVIPATrapControl": ibmMvsDVIPATrapControl,
       "ibmTCPIPmvsConformance": ibmTCPIPmvsConformance,
       "ibmTCPIPmvsCompliances": ibmTCPIPmvsCompliances,
       "ibmTCPIPmvsCompliance": ibmTCPIPmvsCompliance,
       "ibmTCPIPmvsGroups": ibmTCPIPmvsGroups,
       "ibmTCPIPmvsPingGroup": ibmTCPIPmvsPingGroup,
       "ibmTCPIPmvsSystemGroup": ibmTCPIPmvsSystemGroup,
       "ibmTCPIPmvsTcpGroup": ibmTCPIPmvsTcpGroup,
       "ibmTCPIPmvsUdpGroup": ibmTCPIPmvsUdpGroup,
       "ibmTCPIPmvsAtmSupportGroup": ibmTCPIPmvsAtmSupportGroup,
       "ibmTCPIPmvsObsoleteGroup": ibmTCPIPmvsObsoleteGroup,
       "ibmTCPIPmvsAtmNotificationGroup": ibmTCPIPmvsAtmNotificationGroup,
       "ibmTCPIPmvsInterfacesGroup": ibmTCPIPmvsInterfacesGroup,
       "ibmTCPIPmvsAtmLeGroup": ibmTCPIPmvsAtmLeGroup,
       "ibmTCPIPmvsPortGroup": ibmTCPIPmvsPortGroup,
       "ibmTCPIPmvsRoutingGroup": ibmTCPIPmvsRoutingGroup,
       "ibmTCPIPmvsTcpGroup2": ibmTCPIPmvsTcpGroup2,
       "ibmTCPIPmvsSystemGroup2": ibmTCPIPmvsSystemGroup2,
       "ibmTCPIPmvsAtmSupportGroup2": ibmTCPIPmvsAtmSupportGroup2,
       "ibmTCPIPmvsSystemGroup3": ibmTCPIPmvsSystemGroup3,
       "ibmTCPIPmvsInterfacesGroup2": ibmTCPIPmvsInterfacesGroup2,
       "ibmTCPIPmvsUdpGroup2": ibmTCPIPmvsUdpGroup2,
       "ibmTCPIPmvsSystemGroup4": ibmTCPIPmvsSystemGroup4,
       "ibmTCPIPmvsInterfacesGroup3": ibmTCPIPmvsInterfacesGroup3,
       "ibmTCPIPmvsTcpGroup3": ibmTCPIPmvsTcpGroup3,
       "ibmTCPIPmvsSystemGroup5": ibmTCPIPmvsSystemGroup5,
       "ibmTCPIPmvsTcpGroup4": ibmTCPIPmvsTcpGroup4,
       "ibmTCPIPmvsAtmSupportGroup3": ibmTCPIPmvsAtmSupportGroup3,
       "ibmTCPIPmvsInterfacesGroup4": ibmTCPIPmvsInterfacesGroup4,
       "ibmTCPIPmvsPortGroup2": ibmTCPIPmvsPortGroup2,
       "ibmTCPIPmvsAtmSupportGroup4": ibmTCPIPmvsAtmSupportGroup4,
       "ibmTCPIPmvsTcpGroup5": ibmTCPIPmvsTcpGroup5,
       "ibmTCPIPmvsUdpGroup3": ibmTCPIPmvsUdpGroup3,
       "ibmTCPIPmvsAtmLeGroup2": ibmTCPIPmvsAtmLeGroup2,
       "ibmTCPIPmvsSystemGroup6": ibmTCPIPmvsSystemGroup6,
       "ibmTCPIPmvsTcpGroup6": ibmTCPIPmvsTcpGroup6,
       "ibmTCPIPmvsIpGroup": ibmTCPIPmvsIpGroup,
       "ibmTCPIPmvsSystemGroup7": ibmTCPIPmvsSystemGroup7,
       "ibmTCPIPmvsOsaExpGroup": ibmTCPIPmvsOsaExpGroup,
       "ibmTCPIPmvsInterfacesGroup5": ibmTCPIPmvsInterfacesGroup5,
       "ibmTCPIPmvsDVIPAGroup": ibmTCPIPmvsDVIPAGroup,
       "ibmTCPIPmvsDVIPANotificationGroup": ibmTCPIPmvsDVIPANotificationGroup,
       "ibmTCPIPmvsSystemNotificationGroup": ibmTCPIPmvsSystemNotificationGroup,
       "ibmAgentCaps": ibmAgentCaps}
)
