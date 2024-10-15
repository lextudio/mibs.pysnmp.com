# SNMP MIB module (CISCO-SIP-CALLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SIP-CALLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:17 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcCoderTypeRate,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCoderTypeRate")

(callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoSipCallsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995)
)
ciscoSipCallsMIB.setRevisions(
        ("2004-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CSipCallState(Integer32, TextualConvention):
    status = "current"
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("dead", 11),
          ("disconnecting", 10),
          ("idle", 2),
          ("incomingRegister", 30),
          ("incomingResrResv", 14),
          ("initTransfer", 28),
          ("midCallLocalRespPending", 17),
          ("none", 1),
          ("outgoingRegister", 29),
          ("outgoingResrAllocated", 7),
          ("outgoingResrResv", 6),
          ("rcvdInvite", 12),
          ("rcvdProceeding", 5),
          ("rcvdSubscribe", 20),
          ("rcvdTransfer", 9),
          ("rcvdUnsolicitedNotify", 31),
          ("sendMidCallInvitePending", 18),
          ("sendNotify", 24),
          ("sentAlerting", 15),
          ("sentInvite", 4),
          ("sentMidCallInvite", 19),
          ("sentPreAuthRequest", 23),
          ("sentQosProgress", 13),
          ("sentSubscribe", 26),
          ("sentSuccess", 16),
          ("setupBuffered", 3),
          ("subscribeExpired", 22),
          ("subscribeIdle", 25),
          ("subscribeSuccess", 21),
          ("subscribed", 27))
    )



class CSipCallSubstate(Integer32, TextualConvention):
    status = "current"
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
        *(("ackPending", 7),
          ("callTransferSendByeAlso", 9),
          ("none", 1),
          ("proceedingProceeding", 3),
          ("rcvdInviteCallSetup", 4),
          ("rcvdInviteProceeding", 5),
          ("sentDns", 2),
          ("sentEnum", 6),
          ("sentNotify", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSipCallsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSipCallsMIBNotifs = _CiscoSipCallsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 0)
)
_CiscoSipCallsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSipCallsMIBObjects = _CiscoSipCallsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1)
)
_CSipCallActive_ObjectIdentity = ObjectIdentity
cSipCallActive = _CSipCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1)
)
_CSipUACActiveCalls_Type = Gauge32
_CSipUACActiveCalls_Object = MibScalar
cSipUACActiveCalls = _CSipUACActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 1),
    _CSipUACActiveCalls_Type()
)
cSipUACActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipUACActiveCalls.setStatus("current")
_CSipUASActiveCalls_Type = Gauge32
_CSipUASActiveCalls_Object = MibScalar
cSipUASActiveCalls = _CSipUASActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 2),
    _CSipUASActiveCalls_Type()
)
cSipUASActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipUASActiveCalls.setStatus("current")
_CSipCallActiveTable_Object = MibTable
cSipCallActiveTable = _CSipCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cSipCallActiveTable.setStatus("current")
_CSipCallActiveEntry_Object = MibTableRow
cSipCallActiveEntry = _CSipCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1)
)
cSipCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cSipCallActiveEntry.setStatus("current")
_CSipCallActiveId_Type = SnmpAdminString
_CSipCallActiveId_Object = MibTableColumn
cSipCallActiveId = _CSipCallActiveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 1),
    _CSipCallActiveId_Type()
)
cSipCallActiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveId.setStatus("current")


class _CSipCallActiveType_Type(Integer32):
    """Custom type cSipCallActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uac", 1),
          ("uas", 2))
    )


_CSipCallActiveType_Type.__name__ = "Integer32"
_CSipCallActiveType_Object = MibTableColumn
cSipCallActiveType = _CSipCallActiveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 2),
    _CSipCallActiveType_Type()
)
cSipCallActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveType.setStatus("current")
_CSipCallActiveState_Type = CSipCallState
_CSipCallActiveState_Object = MibTableColumn
cSipCallActiveState = _CSipCallActiveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 3),
    _CSipCallActiveState_Type()
)
cSipCallActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveState.setStatus("current")
_CSipCallActiveSubstate_Type = CSipCallSubstate
_CSipCallActiveSubstate_Object = MibTableColumn
cSipCallActiveSubstate = _CSipCallActiveSubstate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 4),
    _CSipCallActiveSubstate_Type()
)
cSipCallActiveSubstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveSubstate.setStatus("current")


class _CSipCallActiveCallingNumber_Type(SnmpAdminString):
    """Custom type cSipCallActiveCallingNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CSipCallActiveCallingNumber_Type.__name__ = "SnmpAdminString"
_CSipCallActiveCallingNumber_Object = MibTableColumn
cSipCallActiveCallingNumber = _CSipCallActiveCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 5),
    _CSipCallActiveCallingNumber_Type()
)
cSipCallActiveCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveCallingNumber.setStatus("current")


class _CSipCallActiveCalledNumber_Type(SnmpAdminString):
    """Custom type cSipCallActiveCalledNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CSipCallActiveCalledNumber_Type.__name__ = "SnmpAdminString"
_CSipCallActiveCalledNumber_Object = MibTableColumn
cSipCallActiveCalledNumber = _CSipCallActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 6),
    _CSipCallActiveCalledNumber_Type()
)
cSipCallActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveCalledNumber.setStatus("current")
_CSipCallActiveSigSrcIpAddrType_Type = InetAddressType
_CSipCallActiveSigSrcIpAddrType_Object = MibTableColumn
cSipCallActiveSigSrcIpAddrType = _CSipCallActiveSigSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 7),
    _CSipCallActiveSigSrcIpAddrType_Type()
)
cSipCallActiveSigSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveSigSrcIpAddrType.setStatus("current")
_CSipCallActiveSigSrcIpAddr_Type = InetAddress
_CSipCallActiveSigSrcIpAddr_Object = MibTableColumn
cSipCallActiveSigSrcIpAddr = _CSipCallActiveSigSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 8),
    _CSipCallActiveSigSrcIpAddr_Type()
)
cSipCallActiveSigSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveSigSrcIpAddr.setStatus("current")
_CSipCallActiveDestReqIpAddrType_Type = InetAddressType
_CSipCallActiveDestReqIpAddrType_Object = MibTableColumn
cSipCallActiveDestReqIpAddrType = _CSipCallActiveDestReqIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 9),
    _CSipCallActiveDestReqIpAddrType_Type()
)
cSipCallActiveDestReqIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestReqIpAddrType.setStatus("current")
_CSipCallActiveDestReqIpAddr_Type = InetAddress
_CSipCallActiveDestReqIpAddr_Object = MibTableColumn
cSipCallActiveDestReqIpAddr = _CSipCallActiveDestReqIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 10),
    _CSipCallActiveDestReqIpAddr_Type()
)
cSipCallActiveDestReqIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestReqIpAddr.setStatus("current")
_CSipCallActiveDestReqPort_Type = InetPortNumber
_CSipCallActiveDestReqPort_Object = MibTableColumn
cSipCallActiveDestReqPort = _CSipCallActiveDestReqPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 11),
    _CSipCallActiveDestReqPort_Type()
)
cSipCallActiveDestReqPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestReqPort.setStatus("current")
_CSipCallActiveDestResIpAddrType_Type = InetAddressType
_CSipCallActiveDestResIpAddrType_Object = MibTableColumn
cSipCallActiveDestResIpAddrType = _CSipCallActiveDestResIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 12),
    _CSipCallActiveDestResIpAddrType_Type()
)
cSipCallActiveDestResIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestResIpAddrType.setStatus("current")
_CSipCallActiveDestResIpAddr_Type = InetAddress
_CSipCallActiveDestResIpAddr_Object = MibTableColumn
cSipCallActiveDestResIpAddr = _CSipCallActiveDestResIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 13),
    _CSipCallActiveDestResIpAddr_Type()
)
cSipCallActiveDestResIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestResIpAddr.setStatus("current")
_CSipCallActiveDestResPort_Type = InetPortNumber
_CSipCallActiveDestResPort_Object = MibTableColumn
cSipCallActiveDestResPort = _CSipCallActiveDestResPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 14),
    _CSipCallActiveDestResPort_Type()
)
cSipCallActiveDestResPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestResPort.setStatus("current")
_CSipCallActiveDestIpAddrType_Type = InetAddressType
_CSipCallActiveDestIpAddrType_Object = MibTableColumn
cSipCallActiveDestIpAddrType = _CSipCallActiveDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 15),
    _CSipCallActiveDestIpAddrType_Type()
)
cSipCallActiveDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestIpAddrType.setStatus("current")
_CSipCallActiveDestIpAddr_Type = InetAddress
_CSipCallActiveDestIpAddr_Object = MibTableColumn
cSipCallActiveDestIpAddr = _CSipCallActiveDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 16),
    _CSipCallActiveDestIpAddr_Type()
)
cSipCallActiveDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveDestIpAddr.setStatus("current")
_CSipCallActiveMediaStreams_Type = Unsigned32
_CSipCallActiveMediaStreams_Object = MibTableColumn
cSipCallActiveMediaStreams = _CSipCallActiveMediaStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 17),
    _CSipCallActiveMediaStreams_Type()
)
cSipCallActiveMediaStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveMediaStreams.setStatus("current")
_CSipCallActiveMediaStreamsActive_Type = Unsigned32
_CSipCallActiveMediaStreamsActive_Object = MibTableColumn
cSipCallActiveMediaStreamsActive = _CSipCallActiveMediaStreamsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 3, 1, 18),
    _CSipCallActiveMediaStreamsActive_Type()
)
cSipCallActiveMediaStreamsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipCallActiveMediaStreamsActive.setStatus("current")
_CSipMediaStreamsTable_Object = MibTable
cSipMediaStreamsTable = _CSipMediaStreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cSipMediaStreamsTable.setStatus("current")
_CSipMediaStreamsEntry_Object = MibTableRow
cSipMediaStreamsEntry = _CSipMediaStreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1)
)
cSipMediaStreamsEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
    (0, "CISCO-SIP-CALLS-MIB", "cSipMediaStreamIndex"),
)
if mibBuilder.loadTexts:
    cSipMediaStreamsEntry.setStatus("current")
_CSipMediaStreamIndex_Type = Unsigned32
_CSipMediaStreamIndex_Object = MibTableColumn
cSipMediaStreamIndex = _CSipMediaStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 1),
    _CSipMediaStreamIndex_Type()
)
cSipMediaStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSipMediaStreamIndex.setStatus("current")


class _CSipMediaStreamState_Type(Integer32):
    """Custom type cSipMediaStreamState based on Integer32"""
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
        *(("active", 6),
          ("adding", 3),
          ("changing", 5),
          ("dead", 7),
          ("deleting", 4),
          ("idle", 2),
          ("invalidStreamState", 1))
    )


_CSipMediaStreamState_Type.__name__ = "Integer32"
_CSipMediaStreamState_Object = MibTableColumn
cSipMediaStreamState = _CSipMediaStreamState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 2),
    _CSipMediaStreamState_Type()
)
cSipMediaStreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamState.setStatus("current")


class _CSipMediaStreamCallId_Type(Integer32):
    """Custom type cSipMediaStreamCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CSipMediaStreamCallId_Type.__name__ = "Integer32"
_CSipMediaStreamCallId_Object = MibTableColumn
cSipMediaStreamCallId = _CSipMediaStreamCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 3),
    _CSipMediaStreamCallId_Type()
)
cSipMediaStreamCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamCallId.setStatus("current")


class _CSipMediaStreamType_Type(Integer32):
    """Custom type cSipMediaStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtmfRelay", 2),
          ("voiceAndDtmfRelay", 3),
          ("voiceOnly", 1))
    )


_CSipMediaStreamType_Type.__name__ = "Integer32"
_CSipMediaStreamType_Object = MibTableColumn
cSipMediaStreamType = _CSipMediaStreamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 4),
    _CSipMediaStreamType_Type()
)
cSipMediaStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamType.setStatus("current")
_CSipMediaStreamNegotdCodec_Type = CvcCoderTypeRate
_CSipMediaStreamNegotdCodec_Object = MibTableColumn
cSipMediaStreamNegotdCodec = _CSipMediaStreamNegotdCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 5),
    _CSipMediaStreamNegotdCodec_Type()
)
cSipMediaStreamNegotdCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamNegotdCodec.setStatus("current")


class _CSipMediaStreamCodecPayloadType_Type(Integer32):
    """Custom type cSipMediaStreamCodecPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CSipMediaStreamCodecPayloadType_Type.__name__ = "Integer32"
_CSipMediaStreamCodecPayloadType_Object = MibTableColumn
cSipMediaStreamCodecPayloadType = _CSipMediaStreamCodecPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 6),
    _CSipMediaStreamCodecPayloadType_Type()
)
cSipMediaStreamCodecPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamCodecPayloadType.setStatus("current")


class _CSipMediaStreamNegotdDtmfRelay_Type(Integer32):
    """Custom type cSipMediaStreamNegotdDtmfRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inBandVoice", 1),
          ("rtpNte", 2))
    )


_CSipMediaStreamNegotdDtmfRelay_Type.__name__ = "Integer32"
_CSipMediaStreamNegotdDtmfRelay_Object = MibTableColumn
cSipMediaStreamNegotdDtmfRelay = _CSipMediaStreamNegotdDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 7),
    _CSipMediaStreamNegotdDtmfRelay_Type()
)
cSipMediaStreamNegotdDtmfRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamNegotdDtmfRelay.setStatus("current")


class _CSipMediaStreamDtmfPayloadType_Type(Integer32):
    """Custom type cSipMediaStreamDtmfPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CSipMediaStreamDtmfPayloadType_Type.__name__ = "Integer32"
_CSipMediaStreamDtmfPayloadType_Object = MibTableColumn
cSipMediaStreamDtmfPayloadType = _CSipMediaStreamDtmfPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 8),
    _CSipMediaStreamDtmfPayloadType_Type()
)
cSipMediaStreamDtmfPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamDtmfPayloadType.setStatus("current")
_CSipMediaStreamSrcIpAddrType_Type = InetAddressType
_CSipMediaStreamSrcIpAddrType_Object = MibTableColumn
cSipMediaStreamSrcIpAddrType = _CSipMediaStreamSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 9),
    _CSipMediaStreamSrcIpAddrType_Type()
)
cSipMediaStreamSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamSrcIpAddrType.setStatus("current")
_CSipMediaStreamSrcIpAddr_Type = InetAddress
_CSipMediaStreamSrcIpAddr_Object = MibTableColumn
cSipMediaStreamSrcIpAddr = _CSipMediaStreamSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 10),
    _CSipMediaStreamSrcIpAddr_Type()
)
cSipMediaStreamSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamSrcIpAddr.setStatus("current")
_CSipMediaStreamSrcPort_Type = InetPortNumber
_CSipMediaStreamSrcPort_Object = MibTableColumn
cSipMediaStreamSrcPort = _CSipMediaStreamSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 11),
    _CSipMediaStreamSrcPort_Type()
)
cSipMediaStreamSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamSrcPort.setStatus("current")
_CSipMediaStreamDestIpAddrType_Type = InetAddressType
_CSipMediaStreamDestIpAddrType_Object = MibTableColumn
cSipMediaStreamDestIpAddrType = _CSipMediaStreamDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 12),
    _CSipMediaStreamDestIpAddrType_Type()
)
cSipMediaStreamDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamDestIpAddrType.setStatus("current")
_CSipMediaStreamDestIpAddr_Type = InetAddress
_CSipMediaStreamDestIpAddr_Object = MibTableColumn
cSipMediaStreamDestIpAddr = _CSipMediaStreamDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 13),
    _CSipMediaStreamDestIpAddr_Type()
)
cSipMediaStreamDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamDestIpAddr.setStatus("current")
_CSipMediaStreamDestPort_Type = InetPortNumber
_CSipMediaStreamDestPort_Object = MibTableColumn
cSipMediaStreamDestPort = _CSipMediaStreamDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 1, 4, 1, 14),
    _CSipMediaStreamDestPort_Type()
)
cSipMediaStreamDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSipMediaStreamDestPort.setStatus("current")
_CSipCallsMIBConformance_ObjectIdentity = ObjectIdentity
cSipCallsMIBConformance = _CSipCallsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2)
)
_CSipCallsMIBCompliances_ObjectIdentity = ObjectIdentity
cSipCallsMIBCompliances = _CSipCallsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2, 1)
)
_CSipCallsMIBGroups_ObjectIdentity = ObjectIdentity
cSipCallsMIBGroups = _CSipCallsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2, 2)
)

# Managed Objects groups

cSipCallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2, 2, 1)
)
cSipCallActiveGroup.setObjects(
      *(("CISCO-SIP-CALLS-MIB", "cSipUACActiveCalls"),
        ("CISCO-SIP-CALLS-MIB", "cSipUASActiveCalls"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveId"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveType"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveState"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveSubstate"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveCallingNumber"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveCalledNumber"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveSigSrcIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveSigSrcIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestReqIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestReqIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestReqPort"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestResIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestResIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestResPort"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveDestIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveMediaStreams"),
        ("CISCO-SIP-CALLS-MIB", "cSipCallActiveMediaStreamsActive"))
)
if mibBuilder.loadTexts:
    cSipCallActiveGroup.setStatus("current")

cSipMediaStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2, 2, 2)
)
cSipMediaStreamGroup.setObjects(
      *(("CISCO-SIP-CALLS-MIB", "cSipMediaStreamState"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamCallId"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamType"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamNegotdCodec"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamCodecPayloadType"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamNegotdDtmfRelay"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamDtmfPayloadType"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamSrcIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamSrcIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamSrcPort"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamDestIpAddrType"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamDestIpAddr"),
        ("CISCO-SIP-CALLS-MIB", "cSipMediaStreamDestPort"))
)
if mibBuilder.loadTexts:
    cSipMediaStreamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cSipCallsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 995, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cSipCallsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIP-CALLS-MIB",
    **{"CSipCallState": CSipCallState,
       "CSipCallSubstate": CSipCallSubstate,
       "ciscoSipCallsMIB": ciscoSipCallsMIB,
       "ciscoSipCallsMIBNotifs": ciscoSipCallsMIBNotifs,
       "ciscoSipCallsMIBObjects": ciscoSipCallsMIBObjects,
       "cSipCallActive": cSipCallActive,
       "cSipUACActiveCalls": cSipUACActiveCalls,
       "cSipUASActiveCalls": cSipUASActiveCalls,
       "cSipCallActiveTable": cSipCallActiveTable,
       "cSipCallActiveEntry": cSipCallActiveEntry,
       "cSipCallActiveId": cSipCallActiveId,
       "cSipCallActiveType": cSipCallActiveType,
       "cSipCallActiveState": cSipCallActiveState,
       "cSipCallActiveSubstate": cSipCallActiveSubstate,
       "cSipCallActiveCallingNumber": cSipCallActiveCallingNumber,
       "cSipCallActiveCalledNumber": cSipCallActiveCalledNumber,
       "cSipCallActiveSigSrcIpAddrType": cSipCallActiveSigSrcIpAddrType,
       "cSipCallActiveSigSrcIpAddr": cSipCallActiveSigSrcIpAddr,
       "cSipCallActiveDestReqIpAddrType": cSipCallActiveDestReqIpAddrType,
       "cSipCallActiveDestReqIpAddr": cSipCallActiveDestReqIpAddr,
       "cSipCallActiveDestReqPort": cSipCallActiveDestReqPort,
       "cSipCallActiveDestResIpAddrType": cSipCallActiveDestResIpAddrType,
       "cSipCallActiveDestResIpAddr": cSipCallActiveDestResIpAddr,
       "cSipCallActiveDestResPort": cSipCallActiveDestResPort,
       "cSipCallActiveDestIpAddrType": cSipCallActiveDestIpAddrType,
       "cSipCallActiveDestIpAddr": cSipCallActiveDestIpAddr,
       "cSipCallActiveMediaStreams": cSipCallActiveMediaStreams,
       "cSipCallActiveMediaStreamsActive": cSipCallActiveMediaStreamsActive,
       "cSipMediaStreamsTable": cSipMediaStreamsTable,
       "cSipMediaStreamsEntry": cSipMediaStreamsEntry,
       "cSipMediaStreamIndex": cSipMediaStreamIndex,
       "cSipMediaStreamState": cSipMediaStreamState,
       "cSipMediaStreamCallId": cSipMediaStreamCallId,
       "cSipMediaStreamType": cSipMediaStreamType,
       "cSipMediaStreamNegotdCodec": cSipMediaStreamNegotdCodec,
       "cSipMediaStreamCodecPayloadType": cSipMediaStreamCodecPayloadType,
       "cSipMediaStreamNegotdDtmfRelay": cSipMediaStreamNegotdDtmfRelay,
       "cSipMediaStreamDtmfPayloadType": cSipMediaStreamDtmfPayloadType,
       "cSipMediaStreamSrcIpAddrType": cSipMediaStreamSrcIpAddrType,
       "cSipMediaStreamSrcIpAddr": cSipMediaStreamSrcIpAddr,
       "cSipMediaStreamSrcPort": cSipMediaStreamSrcPort,
       "cSipMediaStreamDestIpAddrType": cSipMediaStreamDestIpAddrType,
       "cSipMediaStreamDestIpAddr": cSipMediaStreamDestIpAddr,
       "cSipMediaStreamDestPort": cSipMediaStreamDestPort,
       "cSipCallsMIBConformance": cSipCallsMIBConformance,
       "cSipCallsMIBCompliances": cSipCallsMIBCompliances,
       "cSipCallsMIBCompliance": cSipCallsMIBCompliance,
       "cSipCallsMIBGroups": cSipCallsMIBGroups,
       "cSipCallActiveGroup": cSipCallActiveGroup,
       "cSipMediaStreamGroup": cSipMediaStreamGroup}
)
