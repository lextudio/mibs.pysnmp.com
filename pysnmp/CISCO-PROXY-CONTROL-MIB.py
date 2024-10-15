# SNMP MIB module (CISCO-PROXY-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PROXY-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:11 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CvcGUid,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcGUid")

(AbsoluteCounter32,
 callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32",
    "callActiveIndex",
    "callActiveSetupTime")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoProxyControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57)
)
ciscoProxyControlMIB.setRevisions(
        ("2009-02-11 00:00",
         "2006-03-12 00:00",
         "2005-03-06 00:00",
         "2000-02-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CProxyEndptType(Integer32, TextualConvention):
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
        *(("gateway", 2),
          ("other", 0),
          ("proxy", 1))
    )



class CProxyAudioCodec(Integer32, TextualConvention):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("g711Alawr56k", 3),
          ("g711Alawr64k", 2),
          ("g711Ulawr56k", 5),
          ("g711Ulawr64k", 4),
          ("g722r48k", 8),
          ("g722r56k", 7),
          ("g722r64k", 6),
          ("g7231", 9),
          ("g728", 10),
          ("g729", 11),
          ("g729AnnexA", 12),
          ("g729AnnexAB", 16),
          ("g729AnnexB", 15),
          ("g729AnnexC", 17),
          ("gsmAmrNb", 21),
          ("gsmEnhancedFullRate", 20),
          ("gsmFullRate", 18),
          ("gsmHalfRate", 19),
          ("iLBC", 22),
          ("iSAC", 23),
          ("is11172", 13),
          ("is13818", 14),
          ("nonStandard", 1),
          ("other", 0))
    )



class CProxyVideoCodec(Integer32, TextualConvention):
    status = "current"
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
        *(("h261", 2),
          ("h262", 3),
          ("h263", 4),
          ("is11172", 5),
          ("nonStandard", 1),
          ("other", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoProxyControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBObjects = _CiscoProxyControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1)
)
_CProxyCallActive_ObjectIdentity = ObjectIdentity
cProxyCallActive = _CProxyCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1)
)
_CProxyCallActiveTable_Object = MibTable
cProxyCallActiveTable = _CProxyCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cProxyCallActiveTable.setStatus("current")
_CProxyCallActiveEntry_Object = MibTableRow
cProxyCallActiveEntry = _CProxyCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1)
)
cProxyCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cProxyCallActiveEntry.setStatus("current")
_CProxyCallActiveConnectionId_Type = CvcGUid
_CProxyCallActiveConnectionId_Object = MibTableColumn
cProxyCallActiveConnectionId = _CProxyCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 1),
    _CProxyCallActiveConnectionId_Type()
)
cProxyCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveConnectionId.setStatus("current")
_CProxyCallActiveRemoteIPAddress_Type = IpAddress
_CProxyCallActiveRemoteIPAddress_Object = MibTableColumn
cProxyCallActiveRemoteIPAddress = _CProxyCallActiveRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 2),
    _CProxyCallActiveRemoteIPAddress_Type()
)
cProxyCallActiveRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRemoteIPAddress.setStatus("current")


class _CProxyCallActiveAudioUDPPort_Type(Integer32):
    """Custom type cProxyCallActiveAudioUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveAudioUDPPort_Type.__name__ = "Integer32"
_CProxyCallActiveAudioUDPPort_Object = MibTableColumn
cProxyCallActiveAudioUDPPort = _CProxyCallActiveAudioUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 3),
    _CProxyCallActiveAudioUDPPort_Type()
)
cProxyCallActiveAudioUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveAudioUDPPort.setStatus("current")


class _CProxyCallActiveVideoUDPPort_Type(Integer32):
    """Custom type cProxyCallActiveVideoUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveVideoUDPPort_Type.__name__ = "Integer32"
_CProxyCallActiveVideoUDPPort_Object = MibTableColumn
cProxyCallActiveVideoUDPPort = _CProxyCallActiveVideoUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 4),
    _CProxyCallActiveVideoUDPPort_Type()
)
cProxyCallActiveVideoUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveVideoUDPPort.setStatus("current")


class _CProxyCallActiveT120TCPPort1_Type(Integer32):
    """Custom type cProxyCallActiveT120TCPPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveT120TCPPort1_Type.__name__ = "Integer32"
_CProxyCallActiveT120TCPPort1_Object = MibTableColumn
cProxyCallActiveT120TCPPort1 = _CProxyCallActiveT120TCPPort1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 5),
    _CProxyCallActiveT120TCPPort1_Type()
)
cProxyCallActiveT120TCPPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveT120TCPPort1.setStatus("current")


class _CProxyCallActiveT120TCPPort2_Type(Integer32):
    """Custom type cProxyCallActiveT120TCPPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveT120TCPPort2_Type.__name__ = "Integer32"
_CProxyCallActiveT120TCPPort2_Object = MibTableColumn
cProxyCallActiveT120TCPPort2 = _CProxyCallActiveT120TCPPort2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 6),
    _CProxyCallActiveT120TCPPort2_Type()
)
cProxyCallActiveT120TCPPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveT120TCPPort2.setStatus("current")


class _CProxyCallActiveT120TCPPort3_Type(Integer32):
    """Custom type cProxyCallActiveT120TCPPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveT120TCPPort3_Type.__name__ = "Integer32"
_CProxyCallActiveT120TCPPort3_Object = MibTableColumn
cProxyCallActiveT120TCPPort3 = _CProxyCallActiveT120TCPPort3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 7),
    _CProxyCallActiveT120TCPPort3_Type()
)
cProxyCallActiveT120TCPPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveT120TCPPort3.setStatus("current")


class _CProxyCallActiveT120TCPPort4_Type(Integer32):
    """Custom type cProxyCallActiveT120TCPPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveT120TCPPort4_Type.__name__ = "Integer32"
_CProxyCallActiveT120TCPPort4_Object = MibTableColumn
cProxyCallActiveT120TCPPort4 = _CProxyCallActiveT120TCPPort4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 8),
    _CProxyCallActiveT120TCPPort4_Type()
)
cProxyCallActiveT120TCPPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveT120TCPPort4.setStatus("current")
_CProxyCallActiveEndpointType_Type = CProxyEndptType
_CProxyCallActiveEndpointType_Object = MibTableColumn
cProxyCallActiveEndpointType = _CProxyCallActiveEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 9),
    _CProxyCallActiveEndpointType_Type()
)
cProxyCallActiveEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveEndpointType.setStatus("current")


class _CProxyCallActiveEndpointVendor_Type(Integer32):
    """Custom type cProxyCallActiveEndpointVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallActiveEndpointVendor_Type.__name__ = "Integer32"
_CProxyCallActiveEndpointVendor_Object = MibTableColumn
cProxyCallActiveEndpointVendor = _CProxyCallActiveEndpointVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 10),
    _CProxyCallActiveEndpointVendor_Type()
)
cProxyCallActiveEndpointVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveEndpointVendor.setStatus("current")


class _CProxyCallActiveRequestBandwidth_Type(Integer32):
    """Custom type cProxyCallActiveRequestBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CProxyCallActiveRequestBandwidth_Type.__name__ = "Integer32"
_CProxyCallActiveRequestBandwidth_Object = MibTableColumn
cProxyCallActiveRequestBandwidth = _CProxyCallActiveRequestBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 11),
    _CProxyCallActiveRequestBandwidth_Type()
)
cProxyCallActiveRequestBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRequestBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRequestBandwidth.setUnits("kilobits per second")


class _CProxyCallActiveActualBandwidth_Type(Integer32):
    """Custom type cProxyCallActiveActualBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CProxyCallActiveActualBandwidth_Type.__name__ = "Integer32"
_CProxyCallActiveActualBandwidth_Object = MibTableColumn
cProxyCallActiveActualBandwidth = _CProxyCallActiveActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 12),
    _CProxyCallActiveActualBandwidth_Type()
)
cProxyCallActiveActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveActualBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveActualBandwidth.setUnits("kilobits per second")
_CProxyCallActiveAudioCoderRate_Type = CProxyAudioCodec
_CProxyCallActiveAudioCoderRate_Object = MibTableColumn
cProxyCallActiveAudioCoderRate = _CProxyCallActiveAudioCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 13),
    _CProxyCallActiveAudioCoderRate_Type()
)
cProxyCallActiveAudioCoderRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveAudioCoderRate.setStatus("current")
_CProxyCallActiveVideoCoderRate_Type = CProxyVideoCodec
_CProxyCallActiveVideoCoderRate_Object = MibTableColumn
cProxyCallActiveVideoCoderRate = _CProxyCallActiveVideoCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 14),
    _CProxyCallActiveVideoCoderRate_Type()
)
cProxyCallActiveVideoCoderRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveVideoCoderRate.setStatus("current")
_CProxyCallActiveRxAudioPackets_Type = AbsoluteCounter32
_CProxyCallActiveRxAudioPackets_Object = MibTableColumn
cProxyCallActiveRxAudioPackets = _CProxyCallActiveRxAudioPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 15),
    _CProxyCallActiveRxAudioPackets_Type()
)
cProxyCallActiveRxAudioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxAudioPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxAudioPackets.setUnits("packets")
_CProxyCallActiveRxAudioBytes_Type = AbsoluteCounter32
_CProxyCallActiveRxAudioBytes_Object = MibTableColumn
cProxyCallActiveRxAudioBytes = _CProxyCallActiveRxAudioBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 16),
    _CProxyCallActiveRxAudioBytes_Type()
)
cProxyCallActiveRxAudioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxAudioBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxAudioBytes.setUnits("bytes")
_CProxyCallActiveTxAudioPackets_Type = AbsoluteCounter32
_CProxyCallActiveTxAudioPackets_Object = MibTableColumn
cProxyCallActiveTxAudioPackets = _CProxyCallActiveTxAudioPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 17),
    _CProxyCallActiveTxAudioPackets_Type()
)
cProxyCallActiveTxAudioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxAudioPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxAudioPackets.setUnits("packets")
_CProxyCallActiveTxAudioBytes_Type = AbsoluteCounter32
_CProxyCallActiveTxAudioBytes_Object = MibTableColumn
cProxyCallActiveTxAudioBytes = _CProxyCallActiveTxAudioBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 18),
    _CProxyCallActiveTxAudioBytes_Type()
)
cProxyCallActiveTxAudioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxAudioBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxAudioBytes.setUnits("bytes")
_CProxyCallActiveRxVideoPackets_Type = AbsoluteCounter32
_CProxyCallActiveRxVideoPackets_Object = MibTableColumn
cProxyCallActiveRxVideoPackets = _CProxyCallActiveRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 19),
    _CProxyCallActiveRxVideoPackets_Type()
)
cProxyCallActiveRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxVideoPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxVideoPackets.setUnits("packets")
_CProxyCallActiveRxVideoBytes_Type = AbsoluteCounter32
_CProxyCallActiveRxVideoBytes_Object = MibTableColumn
cProxyCallActiveRxVideoBytes = _CProxyCallActiveRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 20),
    _CProxyCallActiveRxVideoBytes_Type()
)
cProxyCallActiveRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxVideoBytes.setUnits("bytes")
_CProxyCallActiveTxVideoPackets_Type = AbsoluteCounter32
_CProxyCallActiveTxVideoPackets_Object = MibTableColumn
cProxyCallActiveTxVideoPackets = _CProxyCallActiveTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 21),
    _CProxyCallActiveTxVideoPackets_Type()
)
cProxyCallActiveTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxVideoPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxVideoPackets.setUnits("packets")
_CProxyCallActiveTxVideoBytes_Type = AbsoluteCounter32
_CProxyCallActiveTxVideoBytes_Object = MibTableColumn
cProxyCallActiveTxVideoBytes = _CProxyCallActiveTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 22),
    _CProxyCallActiveTxVideoBytes_Type()
)
cProxyCallActiveTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxVideoBytes.setUnits("bytes")
_CProxyCallActiveRxT120Packets_Type = AbsoluteCounter32
_CProxyCallActiveRxT120Packets_Object = MibTableColumn
cProxyCallActiveRxT120Packets = _CProxyCallActiveRxT120Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 23),
    _CProxyCallActiveRxT120Packets_Type()
)
cProxyCallActiveRxT120Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxT120Packets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxT120Packets.setUnits("packets")
_CProxyCallActiveRxT120Bytes_Type = AbsoluteCounter32
_CProxyCallActiveRxT120Bytes_Object = MibTableColumn
cProxyCallActiveRxT120Bytes = _CProxyCallActiveRxT120Bytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 24),
    _CProxyCallActiveRxT120Bytes_Type()
)
cProxyCallActiveRxT120Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveRxT120Bytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveRxT120Bytes.setUnits("bytes")
_CProxyCallActiveTxT120Packets_Type = AbsoluteCounter32
_CProxyCallActiveTxT120Packets_Object = MibTableColumn
cProxyCallActiveTxT120Packets = _CProxyCallActiveTxT120Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 25),
    _CProxyCallActiveTxT120Packets_Type()
)
cProxyCallActiveTxT120Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxT120Packets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxT120Packets.setUnits("packets")
_CProxyCallActiveTxT120Bytes_Type = AbsoluteCounter32
_CProxyCallActiveTxT120Bytes_Object = MibTableColumn
cProxyCallActiveTxT120Bytes = _CProxyCallActiveTxT120Bytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 1, 1, 1, 26),
    _CProxyCallActiveTxT120Bytes_Type()
)
cProxyCallActiveTxT120Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallActiveTxT120Bytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallActiveTxT120Bytes.setUnits("bytes")
_CProxyCallHistory_ObjectIdentity = ObjectIdentity
cProxyCallHistory = _CProxyCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2)
)
_CProxyCallHistoryTable_Object = MibTable
cProxyCallHistoryTable = _CProxyCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cProxyCallHistoryTable.setStatus("current")
_CProxyCallHistoryEntry_Object = MibTableRow
cProxyCallHistoryEntry = _CProxyCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1)
)
cProxyCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cProxyCallHistoryEntry.setStatus("current")
_CProxyCallHistoryConnectionId_Type = CvcGUid
_CProxyCallHistoryConnectionId_Object = MibTableColumn
cProxyCallHistoryConnectionId = _CProxyCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 1),
    _CProxyCallHistoryConnectionId_Type()
)
cProxyCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryConnectionId.setStatus("current")
_CProxyCallHistoryRemoteIPAddress_Type = IpAddress
_CProxyCallHistoryRemoteIPAddress_Object = MibTableColumn
cProxyCallHistoryRemoteIPAddress = _CProxyCallHistoryRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 2),
    _CProxyCallHistoryRemoteIPAddress_Type()
)
cProxyCallHistoryRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRemoteIPAddress.setStatus("current")


class _CProxyCallHistoryAudioUDPPort_Type(Integer32):
    """Custom type cProxyCallHistoryAudioUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryAudioUDPPort_Type.__name__ = "Integer32"
_CProxyCallHistoryAudioUDPPort_Object = MibTableColumn
cProxyCallHistoryAudioUDPPort = _CProxyCallHistoryAudioUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 3),
    _CProxyCallHistoryAudioUDPPort_Type()
)
cProxyCallHistoryAudioUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryAudioUDPPort.setStatus("current")


class _CProxyCallHistoryVideoUDPPort_Type(Integer32):
    """Custom type cProxyCallHistoryVideoUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryVideoUDPPort_Type.__name__ = "Integer32"
_CProxyCallHistoryVideoUDPPort_Object = MibTableColumn
cProxyCallHistoryVideoUDPPort = _CProxyCallHistoryVideoUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 4),
    _CProxyCallHistoryVideoUDPPort_Type()
)
cProxyCallHistoryVideoUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryVideoUDPPort.setStatus("current")


class _CProxyCallHistoryT120TCPPort1_Type(Integer32):
    """Custom type cProxyCallHistoryT120TCPPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryT120TCPPort1_Type.__name__ = "Integer32"
_CProxyCallHistoryT120TCPPort1_Object = MibTableColumn
cProxyCallHistoryT120TCPPort1 = _CProxyCallHistoryT120TCPPort1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 5),
    _CProxyCallHistoryT120TCPPort1_Type()
)
cProxyCallHistoryT120TCPPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryT120TCPPort1.setStatus("current")


class _CProxyCallHistoryT120TCPPort2_Type(Integer32):
    """Custom type cProxyCallHistoryT120TCPPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryT120TCPPort2_Type.__name__ = "Integer32"
_CProxyCallHistoryT120TCPPort2_Object = MibTableColumn
cProxyCallHistoryT120TCPPort2 = _CProxyCallHistoryT120TCPPort2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 6),
    _CProxyCallHistoryT120TCPPort2_Type()
)
cProxyCallHistoryT120TCPPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryT120TCPPort2.setStatus("current")


class _CProxyCallHistoryT120TCPPort3_Type(Integer32):
    """Custom type cProxyCallHistoryT120TCPPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryT120TCPPort3_Type.__name__ = "Integer32"
_CProxyCallHistoryT120TCPPort3_Object = MibTableColumn
cProxyCallHistoryT120TCPPort3 = _CProxyCallHistoryT120TCPPort3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 7),
    _CProxyCallHistoryT120TCPPort3_Type()
)
cProxyCallHistoryT120TCPPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryT120TCPPort3.setStatus("current")


class _CProxyCallHistoryT120TCPPort4_Type(Integer32):
    """Custom type cProxyCallHistoryT120TCPPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryT120TCPPort4_Type.__name__ = "Integer32"
_CProxyCallHistoryT120TCPPort4_Object = MibTableColumn
cProxyCallHistoryT120TCPPort4 = _CProxyCallHistoryT120TCPPort4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 8),
    _CProxyCallHistoryT120TCPPort4_Type()
)
cProxyCallHistoryT120TCPPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryT120TCPPort4.setStatus("current")
_CProxyCallHistoryEndpointType_Type = CProxyEndptType
_CProxyCallHistoryEndpointType_Object = MibTableColumn
cProxyCallHistoryEndpointType = _CProxyCallHistoryEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 9),
    _CProxyCallHistoryEndpointType_Type()
)
cProxyCallHistoryEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryEndpointType.setStatus("current")


class _CProxyCallHistoryEndpointVendor_Type(Integer32):
    """Custom type cProxyCallHistoryEndpointVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CProxyCallHistoryEndpointVendor_Type.__name__ = "Integer32"
_CProxyCallHistoryEndpointVendor_Object = MibTableColumn
cProxyCallHistoryEndpointVendor = _CProxyCallHistoryEndpointVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 10),
    _CProxyCallHistoryEndpointVendor_Type()
)
cProxyCallHistoryEndpointVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryEndpointVendor.setStatus("current")


class _CProxyCallHistoryRequestBandwidth_Type(Integer32):
    """Custom type cProxyCallHistoryRequestBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CProxyCallHistoryRequestBandwidth_Type.__name__ = "Integer32"
_CProxyCallHistoryRequestBandwidth_Object = MibTableColumn
cProxyCallHistoryRequestBandwidth = _CProxyCallHistoryRequestBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 11),
    _CProxyCallHistoryRequestBandwidth_Type()
)
cProxyCallHistoryRequestBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRequestBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRequestBandwidth.setUnits("kilobits per second")


class _CProxyCallHistoryActualBandwidth_Type(Integer32):
    """Custom type cProxyCallHistoryActualBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CProxyCallHistoryActualBandwidth_Type.__name__ = "Integer32"
_CProxyCallHistoryActualBandwidth_Object = MibTableColumn
cProxyCallHistoryActualBandwidth = _CProxyCallHistoryActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 12),
    _CProxyCallHistoryActualBandwidth_Type()
)
cProxyCallHistoryActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryActualBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryActualBandwidth.setUnits("kilobits per second")
_CProxyCallHistoryAudioCoderRate_Type = CProxyAudioCodec
_CProxyCallHistoryAudioCoderRate_Object = MibTableColumn
cProxyCallHistoryAudioCoderRate = _CProxyCallHistoryAudioCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 13),
    _CProxyCallHistoryAudioCoderRate_Type()
)
cProxyCallHistoryAudioCoderRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryAudioCoderRate.setStatus("current")
_CProxyCallHistoryVideoCoderRate_Type = CProxyVideoCodec
_CProxyCallHistoryVideoCoderRate_Object = MibTableColumn
cProxyCallHistoryVideoCoderRate = _CProxyCallHistoryVideoCoderRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 14),
    _CProxyCallHistoryVideoCoderRate_Type()
)
cProxyCallHistoryVideoCoderRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryVideoCoderRate.setStatus("current")
_CProxyCallHistoryRxAudioPackets_Type = AbsoluteCounter32
_CProxyCallHistoryRxAudioPackets_Object = MibTableColumn
cProxyCallHistoryRxAudioPackets = _CProxyCallHistoryRxAudioPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 15),
    _CProxyCallHistoryRxAudioPackets_Type()
)
cProxyCallHistoryRxAudioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxAudioPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxAudioPackets.setUnits("packets")
_CProxyCallHistoryRxAudioBytes_Type = AbsoluteCounter32
_CProxyCallHistoryRxAudioBytes_Object = MibTableColumn
cProxyCallHistoryRxAudioBytes = _CProxyCallHistoryRxAudioBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 16),
    _CProxyCallHistoryRxAudioBytes_Type()
)
cProxyCallHistoryRxAudioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxAudioBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxAudioBytes.setUnits("bytes")
_CProxyCallHistoryTxAudioPackets_Type = AbsoluteCounter32
_CProxyCallHistoryTxAudioPackets_Object = MibTableColumn
cProxyCallHistoryTxAudioPackets = _CProxyCallHistoryTxAudioPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 17),
    _CProxyCallHistoryTxAudioPackets_Type()
)
cProxyCallHistoryTxAudioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxAudioPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxAudioPackets.setUnits("packets")
_CProxyCallHistoryTxAudioBytes_Type = AbsoluteCounter32
_CProxyCallHistoryTxAudioBytes_Object = MibTableColumn
cProxyCallHistoryTxAudioBytes = _CProxyCallHistoryTxAudioBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 18),
    _CProxyCallHistoryTxAudioBytes_Type()
)
cProxyCallHistoryTxAudioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxAudioBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxAudioBytes.setUnits("bytes")
_CProxyCallHistoryRxVideoPackets_Type = AbsoluteCounter32
_CProxyCallHistoryRxVideoPackets_Object = MibTableColumn
cProxyCallHistoryRxVideoPackets = _CProxyCallHistoryRxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 19),
    _CProxyCallHistoryRxVideoPackets_Type()
)
cProxyCallHistoryRxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxVideoPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxVideoPackets.setUnits("packets")
_CProxyCallHistoryRxVideoBytes_Type = AbsoluteCounter32
_CProxyCallHistoryRxVideoBytes_Object = MibTableColumn
cProxyCallHistoryRxVideoBytes = _CProxyCallHistoryRxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 20),
    _CProxyCallHistoryRxVideoBytes_Type()
)
cProxyCallHistoryRxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxVideoBytes.setUnits("bytes")
_CProxyCallHistoryTxVideoPackets_Type = AbsoluteCounter32
_CProxyCallHistoryTxVideoPackets_Object = MibTableColumn
cProxyCallHistoryTxVideoPackets = _CProxyCallHistoryTxVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 21),
    _CProxyCallHistoryTxVideoPackets_Type()
)
cProxyCallHistoryTxVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxVideoPackets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxVideoPackets.setUnits("packets")
_CProxyCallHistoryTxVideoBytes_Type = AbsoluteCounter32
_CProxyCallHistoryTxVideoBytes_Object = MibTableColumn
cProxyCallHistoryTxVideoBytes = _CProxyCallHistoryTxVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 22),
    _CProxyCallHistoryTxVideoBytes_Type()
)
cProxyCallHistoryTxVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxVideoBytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxVideoBytes.setUnits("bytes")
_CProxyCallHistoryRxT120Packets_Type = AbsoluteCounter32
_CProxyCallHistoryRxT120Packets_Object = MibTableColumn
cProxyCallHistoryRxT120Packets = _CProxyCallHistoryRxT120Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 23),
    _CProxyCallHistoryRxT120Packets_Type()
)
cProxyCallHistoryRxT120Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxT120Packets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxT120Packets.setUnits("packets")
_CProxyCallHistoryRxT120Bytes_Type = AbsoluteCounter32
_CProxyCallHistoryRxT120Bytes_Object = MibTableColumn
cProxyCallHistoryRxT120Bytes = _CProxyCallHistoryRxT120Bytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 24),
    _CProxyCallHistoryRxT120Bytes_Type()
)
cProxyCallHistoryRxT120Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxT120Bytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryRxT120Bytes.setUnits("bytes")
_CProxyCallHistoryTxT120Packets_Type = AbsoluteCounter32
_CProxyCallHistoryTxT120Packets_Object = MibTableColumn
cProxyCallHistoryTxT120Packets = _CProxyCallHistoryTxT120Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 25),
    _CProxyCallHistoryTxT120Packets_Type()
)
cProxyCallHistoryTxT120Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxT120Packets.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxT120Packets.setUnits("packets")
_CProxyCallHistoryTxT120Bytes_Type = AbsoluteCounter32
_CProxyCallHistoryTxT120Bytes_Object = MibTableColumn
cProxyCallHistoryTxT120Bytes = _CProxyCallHistoryTxT120Bytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 1, 2, 1, 1, 26),
    _CProxyCallHistoryTxT120Bytes_Type()
)
cProxyCallHistoryTxT120Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxT120Bytes.setStatus("current")
if mibBuilder.loadTexts:
    cProxyCallHistoryTxT120Bytes.setUnits("bytes")
_CiscoProxyControlMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBNotificationPrefix = _CiscoProxyControlMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 2)
)
_CiscoProxyControlMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBNotifications = _CiscoProxyControlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 2, 0)
)
_CiscoProxyControlMIBConformance_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBConformance = _CiscoProxyControlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3)
)
_CiscoProxyControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBCompliances = _CiscoProxyControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 1)
)
_CiscoProxyControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoProxyControlMIBGroups = _CiscoProxyControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2)
)

# Managed Objects groups

cProxyCallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2, 1)
)
cProxyCallActiveGroup.setObjects(
      *(("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveConnectionId"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRemoteIPAddress"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveAudioUDPPort"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveVideoUDPPort"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort1"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort2"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort3"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveT120TCPPort4"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveEndpointType"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveEndpointVendor"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRequestBandwidth"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveActualBandwidth"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveAudioCoderRate"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveVideoCoderRate"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxAudioPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxAudioBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxAudioPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxAudioBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxVideoPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxVideoBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxVideoPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxVideoBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxT120Packets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveRxT120Bytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxT120Packets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallActiveTxT120Bytes"))
)
if mibBuilder.loadTexts:
    cProxyCallActiveGroup.setStatus("current")

cProxyCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 2, 2)
)
cProxyCallHistoryGroup.setObjects(
      *(("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryConnectionId"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRemoteIPAddress"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryAudioUDPPort"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryVideoUDPPort"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort1"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort2"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort3"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryT120TCPPort4"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryEndpointType"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryEndpointVendor"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRequestBandwidth"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryActualBandwidth"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryAudioCoderRate"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryVideoCoderRate"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxAudioPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxAudioBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxAudioPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxAudioBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxVideoPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxVideoBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxVideoPackets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxVideoBytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxT120Packets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryRxT120Bytes"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxT120Packets"),
        ("CISCO-PROXY-CONTROL-MIB", "cProxyCallHistoryTxT120Bytes"))
)
if mibBuilder.loadTexts:
    cProxyCallHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoProxyControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 57, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoProxyControlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PROXY-CONTROL-MIB",
    **{"CProxyEndptType": CProxyEndptType,
       "CProxyAudioCodec": CProxyAudioCodec,
       "CProxyVideoCodec": CProxyVideoCodec,
       "ciscoProxyControlMIB": ciscoProxyControlMIB,
       "ciscoProxyControlMIBObjects": ciscoProxyControlMIBObjects,
       "cProxyCallActive": cProxyCallActive,
       "cProxyCallActiveTable": cProxyCallActiveTable,
       "cProxyCallActiveEntry": cProxyCallActiveEntry,
       "cProxyCallActiveConnectionId": cProxyCallActiveConnectionId,
       "cProxyCallActiveRemoteIPAddress": cProxyCallActiveRemoteIPAddress,
       "cProxyCallActiveAudioUDPPort": cProxyCallActiveAudioUDPPort,
       "cProxyCallActiveVideoUDPPort": cProxyCallActiveVideoUDPPort,
       "cProxyCallActiveT120TCPPort1": cProxyCallActiveT120TCPPort1,
       "cProxyCallActiveT120TCPPort2": cProxyCallActiveT120TCPPort2,
       "cProxyCallActiveT120TCPPort3": cProxyCallActiveT120TCPPort3,
       "cProxyCallActiveT120TCPPort4": cProxyCallActiveT120TCPPort4,
       "cProxyCallActiveEndpointType": cProxyCallActiveEndpointType,
       "cProxyCallActiveEndpointVendor": cProxyCallActiveEndpointVendor,
       "cProxyCallActiveRequestBandwidth": cProxyCallActiveRequestBandwidth,
       "cProxyCallActiveActualBandwidth": cProxyCallActiveActualBandwidth,
       "cProxyCallActiveAudioCoderRate": cProxyCallActiveAudioCoderRate,
       "cProxyCallActiveVideoCoderRate": cProxyCallActiveVideoCoderRate,
       "cProxyCallActiveRxAudioPackets": cProxyCallActiveRxAudioPackets,
       "cProxyCallActiveRxAudioBytes": cProxyCallActiveRxAudioBytes,
       "cProxyCallActiveTxAudioPackets": cProxyCallActiveTxAudioPackets,
       "cProxyCallActiveTxAudioBytes": cProxyCallActiveTxAudioBytes,
       "cProxyCallActiveRxVideoPackets": cProxyCallActiveRxVideoPackets,
       "cProxyCallActiveRxVideoBytes": cProxyCallActiveRxVideoBytes,
       "cProxyCallActiveTxVideoPackets": cProxyCallActiveTxVideoPackets,
       "cProxyCallActiveTxVideoBytes": cProxyCallActiveTxVideoBytes,
       "cProxyCallActiveRxT120Packets": cProxyCallActiveRxT120Packets,
       "cProxyCallActiveRxT120Bytes": cProxyCallActiveRxT120Bytes,
       "cProxyCallActiveTxT120Packets": cProxyCallActiveTxT120Packets,
       "cProxyCallActiveTxT120Bytes": cProxyCallActiveTxT120Bytes,
       "cProxyCallHistory": cProxyCallHistory,
       "cProxyCallHistoryTable": cProxyCallHistoryTable,
       "cProxyCallHistoryEntry": cProxyCallHistoryEntry,
       "cProxyCallHistoryConnectionId": cProxyCallHistoryConnectionId,
       "cProxyCallHistoryRemoteIPAddress": cProxyCallHistoryRemoteIPAddress,
       "cProxyCallHistoryAudioUDPPort": cProxyCallHistoryAudioUDPPort,
       "cProxyCallHistoryVideoUDPPort": cProxyCallHistoryVideoUDPPort,
       "cProxyCallHistoryT120TCPPort1": cProxyCallHistoryT120TCPPort1,
       "cProxyCallHistoryT120TCPPort2": cProxyCallHistoryT120TCPPort2,
       "cProxyCallHistoryT120TCPPort3": cProxyCallHistoryT120TCPPort3,
       "cProxyCallHistoryT120TCPPort4": cProxyCallHistoryT120TCPPort4,
       "cProxyCallHistoryEndpointType": cProxyCallHistoryEndpointType,
       "cProxyCallHistoryEndpointVendor": cProxyCallHistoryEndpointVendor,
       "cProxyCallHistoryRequestBandwidth": cProxyCallHistoryRequestBandwidth,
       "cProxyCallHistoryActualBandwidth": cProxyCallHistoryActualBandwidth,
       "cProxyCallHistoryAudioCoderRate": cProxyCallHistoryAudioCoderRate,
       "cProxyCallHistoryVideoCoderRate": cProxyCallHistoryVideoCoderRate,
       "cProxyCallHistoryRxAudioPackets": cProxyCallHistoryRxAudioPackets,
       "cProxyCallHistoryRxAudioBytes": cProxyCallHistoryRxAudioBytes,
       "cProxyCallHistoryTxAudioPackets": cProxyCallHistoryTxAudioPackets,
       "cProxyCallHistoryTxAudioBytes": cProxyCallHistoryTxAudioBytes,
       "cProxyCallHistoryRxVideoPackets": cProxyCallHistoryRxVideoPackets,
       "cProxyCallHistoryRxVideoBytes": cProxyCallHistoryRxVideoBytes,
       "cProxyCallHistoryTxVideoPackets": cProxyCallHistoryTxVideoPackets,
       "cProxyCallHistoryTxVideoBytes": cProxyCallHistoryTxVideoBytes,
       "cProxyCallHistoryRxT120Packets": cProxyCallHistoryRxT120Packets,
       "cProxyCallHistoryRxT120Bytes": cProxyCallHistoryRxT120Bytes,
       "cProxyCallHistoryTxT120Packets": cProxyCallHistoryTxT120Packets,
       "cProxyCallHistoryTxT120Bytes": cProxyCallHistoryTxT120Bytes,
       "ciscoProxyControlMIBNotificationPrefix": ciscoProxyControlMIBNotificationPrefix,
       "ciscoProxyControlMIBNotifications": ciscoProxyControlMIBNotifications,
       "ciscoProxyControlMIBConformance": ciscoProxyControlMIBConformance,
       "ciscoProxyControlMIBCompliances": ciscoProxyControlMIBCompliances,
       "ciscoProxyControlMIBCompliance": ciscoProxyControlMIBCompliance,
       "ciscoProxyControlMIBGroups": ciscoProxyControlMIBGroups,
       "cProxyCallActiveGroup": cProxyCallActiveGroup,
       "cProxyCallHistoryGroup": cProxyCallHistoryGroup}
)
