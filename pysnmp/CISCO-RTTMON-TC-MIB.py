# SNMP MIB module (CISCO-RTTMON-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:00 2024
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

ciscoRttMonTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 485)
)
ciscoRttMonTCMIB.setRevisions(
        ("2014-03-19 00:00",
         "2013-11-26 00:00",
         "2012-11-02 00:00",
         "2012-05-25 00:00",
         "2011-09-15 00:00",
         "2010-04-26 00:00",
         "2006-08-11 00:00",
         "2006-07-17 00:00",
         "2006-03-02 00:00",
         "2005-08-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RttMonScheduleStartType(Integer32, TextualConvention):
    status = "current"
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
        *(("after", 4),
          ("now", 2),
          ("pending", 1),
          ("random", 3),
          ("specific", 5))
    )



class RttReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )



class RttMonOperation(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ftpActive", 5),
          ("ftpGet", 3),
          ("ftpPassive", 4),
          ("httpGet", 1),
          ("httpRaw", 2),
          ("notApplicable", 0),
          ("voipDTAlertRinging", 6),
          ("voipDTConnectOK", 7))
    )



class RttResponseSense(Integer32, TextualConvention):
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("applicationSpecific", 10),
          ("busy", 5),
          ("disconnected", 2),
          ("dnsQueryError", 14),
          ("dnsServerTimeout", 11),
          ("dropped", 7),
          ("enableAbort", 25),
          ("enableAuthFail", 27),
          ("enableFail", 26),
          ("enableFormatError", 28),
          ("enableInternalError", 24),
          ("enableNoConnect", 22),
          ("enableOk", 21),
          ("enablePortInUse", 29),
          ("enableVersionFail", 23),
          ("error", 16),
          ("httpError", 15),
          ("httpTransactionTimeout", 13),
          ("mplsLspEchoTxError", 17),
          ("mplsLspMalformedReq", 19),
          ("mplsLspReachButNotFEC", 20),
          ("mplsLspUnreachable", 18),
          ("notConnected", 6),
          ("ok", 1),
          ("other", 0),
          ("overThreshold", 3),
          ("sequenceError", 8),
          ("statsRetrieveAbort", 34),
          ("statsRetrieveAuthFail", 36),
          ("statsRetrieveFail", 35),
          ("statsRetrieveFormatError", 37),
          ("statsRetrieveInternalError", 33),
          ("statsRetrieveNoConnect", 31),
          ("statsRetrieveOk", 30),
          ("statsRetrievePortInUse", 38),
          ("statsRetrieveVersionFail", 32),
          ("tcpConnectTimeout", 12),
          ("timeout", 4),
          ("verifyError", 9))
    )



class RttMonRttType(Integer32, TextualConvention):
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 11),
          ("dlsw", 10),
          ("dns", 8),
          ("echo", 1),
          ("ethernetJitter", 20),
          ("ethernetPing", 19),
          ("fabricPathEcho", 26),
          ("fileIO", 3),
          ("ftp", 12),
          ("http", 7),
          ("icmpjitter", 16),
          ("jitter", 9),
          ("lspGroup", 15),
          ("lspPing", 17),
          ("lspPingPseudowire", 21),
          ("lspTrace", 18),
          ("mcastJitter", 25),
          ("pathEcho", 2),
          ("rtp", 14),
          ("script", 4),
          ("tcpConnect", 6),
          ("udpEcho", 5),
          ("video", 22),
          ("voip", 13),
          ("y1731Delay", 23),
          ("y1731Loss", 24))
    )



class RttMplsVpnMonRttType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("echo", 2),
          ("jitter", 1),
          ("pathEcho", 3))
    )



class RttMplsVpnMonLpdFailureSense(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("allPathsBroken", 3),
          ("allPathsBrokenOrUnexplorable", 5),
          ("allPathsUnexplorable", 4),
          ("error", 7),
          ("noPath", 2),
          ("timeout", 6),
          ("unknown", 1))
    )



class RttMplsVpnMonLpdGrpStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("down", 4),
          ("partial", 3),
          ("unknown", 1),
          ("up", 2))
    )



class RttMonProtocol(Integer32, TextualConvention):
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("apolloEcho", 21),
          ("apolloEchoAppl", 22),
          ("appleTalkEcho", 9),
          ("appleTalkEchoAppl", 10),
          ("decNetEcho", 11),
          ("decNetEchoAppl", 12),
          ("dhcpAppl", 29),
          ("dlswAppl", 28),
          ("dnsAppl", 26),
          ("ethernetJitterAppl", 36),
          ("ethernetPingAppl", 35),
          ("fabricPathEchoAppl", 44),
          ("ftpAppl", 30),
          ("httpAppl", 25),
          ("icmpJitterAppl", 34),
          ("ipIcmpEcho", 2),
          ("ipTcpConn", 24),
          ("ipUdpEchoAppl", 3),
          ("ipxEcho", 13),
          ("ipxEchoAppl", 14),
          ("isoClnsEcho", 15),
          ("isoClnsEchoAppl", 16),
          ("jitterAppl", 27),
          ("mcastJitterAppl", 41),
          ("mplsLspPingAppl", 31),
          ("netbiosEchoAppl", 23),
          ("notApplicable", 1),
          ("rtpAppl", 33),
          ("snaLU0EchoAppl", 5),
          ("snaLU2EchoAppl", 6),
          ("snaLU62Echo", 7),
          ("snaLU62EchoAppl", 8),
          ("snaRUEcho", 4),
          ("videoAppl", 37),
          ("vinesEcho", 17),
          ("vinesEchoAppl", 18),
          ("voipAppl", 32),
          ("xnsEcho", 19),
          ("xnsEchoAppl", 20),
          ("y17311dm", 39),
          ("y1731dmm", 38),
          ("y1731dmmv1", 43),
          ("y1731lmm", 40),
          ("y1731slm", 42))
    )



class RttMonCodecType(Integer32, TextualConvention):
    status = "current"
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
        *(("g711alaw", 2),
          ("g711ulaw", 1),
          ("g729a", 3),
          ("notApplicable", 0))
    )



class RttMonLSPPingReplyMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replyIpv4Udp", 1),
          ("replyIpv4UdpRA", 2))
    )



class RttMonTargetAddress(OctetString, TextualConvention):
    status = "current"


class RttMonReactVar(Integer32, TextualConvention):
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("connectionLoss", 8),
          ("frameLossDS", 20),
          ("iaJitterDS", 19),
          ("iaJitterSD", 30),
          ("icpif", 11),
          ("jitterAvg", 10),
          ("jitterAvgPct", 47),
          ("jitterDSAvg", 3),
          ("jitterDSAvgPct", 46),
          ("jitterSDAvg", 2),
          ("jitterSDAvgPct", 45),
          ("latencyDSAvg", 27),
          ("latencyDSAvgPct", 44),
          ("latencySDAvg", 28),
          ("latencySDAvgPct", 43),
          ("lpdAll", 35),
          ("lpdGroup", 33),
          ("lpdTreeTrace", 34),
          ("maxOfLatencyDS", 25),
          ("maxOfLatencyDSPct", 42),
          ("maxOfLatencySD", 26),
          ("maxOfLatencySDPct", 41),
          ("maxOfNegativeDS", 18),
          ("maxOfNegativeSD", 16),
          ("maxOfPositiveDS", 17),
          ("maxOfPositiveSD", 15),
          ("mos", 6),
          ("mosCQDS", 22),
          ("mosCQSD", 31),
          ("mosLQDS", 21),
          ("overThreshold", 48),
          ("packetLateArrival", 13),
          ("packetLoss", 29),
          ("packetLossDS", 5),
          ("packetLossSD", 4),
          ("packetMIA", 12),
          ("packetOutOfSequence", 14),
          ("pktLossPctDS", 39),
          ("pktLossPctSD", 38),
          ("protocolSpecificError", 49),
          ("rFactorDS", 23),
          ("rFactorSD", 32),
          ("rtt", 1),
          ("rttPct", 40),
          ("successivePacketLoss", 24),
          ("timeout", 7),
          ("unavailDS", 37),
          ("unavailSD", 36),
          ("verifyError", 9))
    )



class RttMonIdLst(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class RttMonCtrlIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-TC-MIB",
    **{"RttMonScheduleStartType": RttMonScheduleStartType,
       "RttReset": RttReset,
       "RttMonOperation": RttMonOperation,
       "RttResponseSense": RttResponseSense,
       "RttMonRttType": RttMonRttType,
       "RttMplsVpnMonRttType": RttMplsVpnMonRttType,
       "RttMplsVpnMonLpdFailureSense": RttMplsVpnMonLpdFailureSense,
       "RttMplsVpnMonLpdGrpStatus": RttMplsVpnMonLpdGrpStatus,
       "RttMonProtocol": RttMonProtocol,
       "RttMonCodecType": RttMonCodecType,
       "RttMonLSPPingReplyMode": RttMonLSPPingReplyMode,
       "RttMonTargetAddress": RttMonTargetAddress,
       "RttMonReactVar": RttMonReactVar,
       "RttMonIdLst": RttMonIdLst,
       "RttMonCtrlIndex": RttMonCtrlIndex,
       "ciscoRttMonTCMIB": ciscoRttMonTCMIB}
)
