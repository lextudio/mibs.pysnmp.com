# SNMP MIB module (Juniper-DOS-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DOS-PROTECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:01 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniDosProtectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80)
)
juniDosProtectionMIB.setRevisions(
        ("2008-05-06 00:00",
         "2006-07-01 00:00",
         "2006-08-18 04:00",
         "2006-08-17 19:26",
         "2006-01-01 05:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniDosProtectionProtocolType(Integer32, TextualConvention):
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
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73)
        )
    )
    namedValues = NamedValues(
        *(("atmControl", 4),
          ("atmDynamicIf", 6),
          ("atmDynamicIfPppData", 72),
          ("atmInverseArp", 7),
          ("atmOam", 5),
          ("dhcpExternal", 27),
          ("dhcpTesterIc", 71),
          ("ethernetArp", 13),
          ("ethernetArpMiss", 12),
          ("ethernetDynamicIf", 17),
          ("ethernetFcBasedArp", 14),
          ("ethernetLacp", 15),
          ("ethernetOam", 16),
          ("ethernetPppTerminate", 18),
          ("flisInPayload", 25),
          ("flisInPayloadUpdateTable", 26),
          ("frameRelayArp", 9),
          ("frameRelayControl", 8),
          ("ipAppClassifierHttpRedirect", 69),
          ("ipFastBfd", 63),
          ("ipIke", 65),
          ("ipLocalBfd", 62),
          ("ipLocalBgp", 45),
          ("ipLocalCops", 49),
          ("ipLocalDemuxMiss", 53),
          ("ipLocalDhcpIc", 41),
          ("ipLocalDhcpSc", 40),
          ("ipLocalFastBfd", 64),
          ("ipLocalFragment", 68),
          ("ipLocalIcmpEcho", 42),
          ("ipLocalIcmpFragment", 67),
          ("ipLocalIcmpOther", 43),
          ("ipLocalL2tpControlIc", 51),
          ("ipLocalL2tpControlSc", 50),
          ("ipLocalLDP", 44),
          ("ipLocalLspPing", 73),
          ("ipLocalOspf", 46),
          ("ipLocalOther", 52),
          ("ipLocalPim", 48),
          ("ipLocalPimAssert", 61),
          ("ipLocalRsvp", 47),
          ("ipMld", 60),
          ("ipMulticastBroadcastOther", 32),
          ("ipMulticastCacheMiss", 37),
          ("ipMulticastCacheMissAutoReply", 38),
          ("ipMulticastControlIc", 35),
          ("ipMulticastControlSc", 34),
          ("ipMulticastDhcpIc", 70),
          ("ipMulticastDhcpSc", 33),
          ("ipMulticastVrrp", 36),
          ("ipMulticastWrongIf", 39),
          ("ipNeighborDiscovery", 57),
          ("ipNeighborDiscoveryMiss", 58),
          ("ipNormalPathMtu", 56),
          ("ipOptionsOther", 30),
          ("ipOptionsRouterAlert", 31),
          ("ipOsi", 28),
          ("ipReassembly", 66),
          ("ipRouteNoRoute", 55),
          ("ipRouteToSrpEthernet", 54),
          ("ipSearchError", 59),
          ("ipTtlExpired", 29),
          ("itmL2tpControl", 24),
          ("mplsMtuExceeded", 23),
          ("mplsTtlOnReceive", 21),
          ("mplsTtlOnTransmit", 22),
          ("ppEchoReply", 1),
          ("pppControl", 3),
          ("pppEchoReplyFast", 2),
          ("pppEchoRequest", 0),
          ("pppoeControl", 10),
          ("pppoePppConfig", 11),
          ("slepSlarp", 19),
          ("slepSlarpReplyFast", 20))
    )



class JuniDosProtectionPriorityType(Integer32, TextualConvention):
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
        *(("hiGreenFcIc", 0),
          ("hiGreenFcSc", 4),
          ("hiYellowFcIc", 1),
          ("hiYellowFcSc", 5),
          ("loGreenFcIc", 2),
          ("loGreenFcSc", 6),
          ("loYellowFcIc", 3),
          ("loYellowFcSc", 7))
    )



class JuniDosProtectionProtocolState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inTrouble", 2),
          ("ok", 1))
    )



class JuniDosProtectionScfdsTableOverflowState(Integer32, TextualConvention):
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
        *(("grouping", 2),
          ("notOverflowingOrGrouping", 1),
          ("overflowing", 3))
    )



class JuniDosProtectionProtocolPriorityType(Integer32, TextualConvention):
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
        *(("dataPath", 4),
          ("hiGreen", 0),
          ("hiYellow", 1),
          ("loGreen", 2),
          ("loYellow", 3))
    )



class JuniDosProtectionProtocolCannedType(Integer32, TextualConvention):
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
        *(("atmAccess", 2),
          ("default", 0),
          ("enetAccess", 1),
          ("frame", 3),
          ("uplink", 4))
    )



class JuniDosProtectionLayerId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              11,
              17,
              19,
              35,
              50)
        )
    )
    namedValues = NamedValues(
        *(("atm1483", 11),
          ("bridge1483", 19),
          ("ethernet", 6),
          ("ip", 0),
          ("ipv6", 50),
          ("ppp", 1),
          ("pppoe", 17),
          ("vlan", 35))
    )



class JuniDosProtectionControlProcessorDestination(Integer32, TextualConvention):
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
        *(("dataPath", 2),
          ("ic", 0),
          ("sc", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JuniDosProtectionObjects_ObjectIdentity = ObjectIdentity
juniDosProtectionObjects = _JuniDosProtectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1)
)
_JuniDosProtectionScfdsGroup_ObjectIdentity = ObjectIdentity
juniDosProtectionScfdsGroup = _JuniDosProtectionScfdsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1)
)


class _JuniDosProtectionScfdsGlobalState_Type(JuniEnable):
    """Custom type juniDosProtectionScfdsGlobalState based on JuniEnable"""


_JuniDosProtectionScfdsGlobalState_Object = MibScalar
juniDosProtectionScfdsGlobalState = _JuniDosProtectionScfdsGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 1),
    _JuniDosProtectionScfdsGlobalState_Type()
)
juniDosProtectionScfdsGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalState.setStatus("current")


class _JuniDosProtectionScfdsGlobalGrouping_Type(JuniEnable):
    """Custom type juniDosProtectionScfdsGlobalGrouping based on JuniEnable"""


_JuniDosProtectionScfdsGlobalGrouping_Object = MibScalar
juniDosProtectionScfdsGlobalGrouping = _JuniDosProtectionScfdsGlobalGrouping_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 2),
    _JuniDosProtectionScfdsGlobalGrouping_Type()
)
juniDosProtectionScfdsGlobalGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalGrouping.setStatus("current")


class _JuniDosProtectionScfdsGlobalClearAll_Type(Integer32):
    """Custom type juniDosProtectionScfdsGlobalClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 0))
    )


_JuniDosProtectionScfdsGlobalClearAll_Type.__name__ = "Integer32"
_JuniDosProtectionScfdsGlobalClearAll_Object = MibScalar
juniDosProtectionScfdsGlobalClearAll = _JuniDosProtectionScfdsGlobalClearAll_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 3),
    _JuniDosProtectionScfdsGlobalClearAll_Type()
)
juniDosProtectionScfdsGlobalClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalClearAll.setStatus("current")
_JuniDosProtectionScfdsGlobalDiscontinuityTime_Type = Unsigned32
_JuniDosProtectionScfdsGlobalDiscontinuityTime_Object = MibScalar
juniDosProtectionScfdsGlobalDiscontinuityTime = _JuniDosProtectionScfdsGlobalDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 4),
    _JuniDosProtectionScfdsGlobalDiscontinuityTime_Type()
)
juniDosProtectionScfdsGlobalDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalDiscontinuityTime.setStatus("current")
_JuniDosProtectionScfdsGlobalTableOverflowState_Type = JuniDosProtectionScfdsTableOverflowState
_JuniDosProtectionScfdsGlobalTableOverflowState_Object = MibScalar
juniDosProtectionScfdsGlobalTableOverflowState = _JuniDosProtectionScfdsGlobalTableOverflowState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 5),
    _JuniDosProtectionScfdsGlobalTableOverflowState_Type()
)
juniDosProtectionScfdsGlobalTableOverflowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalTableOverflowState.setStatus("current")
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Type = Counter32
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Object = MibScalar
juniDosProtectionScfdsGlobalCurrentSuspiciousFlows = _JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 6),
    _JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Type()
)
juniDosProtectionScfdsGlobalCurrentSuspiciousFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalCurrentSuspiciousFlows.setStatus("current")
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Type = Counter32
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Object = MibScalar
juniDosProtectionScfdsGlobalNumberSuspiciousFlows = _JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 7),
    _JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Type()
)
juniDosProtectionScfdsGlobalNumberSuspiciousFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalNumberSuspiciousFlows.setStatus("current")
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Type = Counter32
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Object = MibScalar
juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups = _JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 8),
    _JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Type()
)
juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups.setStatus("current")
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Type = Counter32
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Object = MibScalar
juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups = _JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 9),
    _JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Type()
)
juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups.setStatus("current")
_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Type = Counter32
_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Object = MibScalar
juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows = _JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 10),
    _JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Type()
)
juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows.setStatus("current")
_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Type = Counter32
_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Object = MibScalar
juniDosProtectionScfdsGlobalNumberFalseNegativeFlows = _JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 11),
    _JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Type()
)
juniDosProtectionScfdsGlobalNumberFalseNegativeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalNumberFalseNegativeFlows.setStatus("current")
_JuniDosProtectionScfdsGlobalNumberTableOverflows_Type = Counter32
_JuniDosProtectionScfdsGlobalNumberTableOverflows_Object = MibScalar
juniDosProtectionScfdsGlobalNumberTableOverflows = _JuniDosProtectionScfdsGlobalNumberTableOverflows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 12),
    _JuniDosProtectionScfdsGlobalNumberTableOverflows_Type()
)
juniDosProtectionScfdsGlobalNumberTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGlobalNumberTableOverflows.setStatus("current")
_JuniDosProtectionScfdsProtocolTable_Object = MibTable
juniDosProtectionScfdsProtocolTable = _JuniDosProtectionScfdsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13)
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolTable.setStatus("current")
_JuniDosProtectionScfdsProtocolEntry_Object = MibTableRow
juniDosProtectionScfdsProtocolEntry = _JuniDosProtectionScfdsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1)
)
juniDosProtectionScfdsProtocolEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolIndex"),
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolEntry.setStatus("current")
_JuniDosProtectionScfdsProtocolIndex_Type = JuniDosProtectionProtocolType
_JuniDosProtectionScfdsProtocolIndex_Object = MibTableColumn
juniDosProtectionScfdsProtocolIndex = _JuniDosProtectionScfdsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 1),
    _JuniDosProtectionScfdsProtocolIndex_Type()
)
juniDosProtectionScfdsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolIndex.setStatus("current")


class _JuniDosProtectionScfdsProtocolThreshold_Type(Unsigned32):
    """Custom type juniDosProtectionScfdsProtocolThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JuniDosProtectionScfdsProtocolThreshold_Type.__name__ = "Unsigned32"
_JuniDosProtectionScfdsProtocolThreshold_Object = MibTableColumn
juniDosProtectionScfdsProtocolThreshold = _JuniDosProtectionScfdsProtocolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 2),
    _JuniDosProtectionScfdsProtocolThreshold_Type()
)
juniDosProtectionScfdsProtocolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolThreshold.setStatus("current")


class _JuniDosProtectionScfdsProtocolLowThreshold_Type(Unsigned32):
    """Custom type juniDosProtectionScfdsProtocolLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_JuniDosProtectionScfdsProtocolLowThreshold_Type.__name__ = "Unsigned32"
_JuniDosProtectionScfdsProtocolLowThreshold_Object = MibTableColumn
juniDosProtectionScfdsProtocolLowThreshold = _JuniDosProtectionScfdsProtocolLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 3),
    _JuniDosProtectionScfdsProtocolLowThreshold_Type()
)
juniDosProtectionScfdsProtocolLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolLowThreshold.setStatus("current")


class _JuniDosProtectionScfdsProtocolBackoffTime_Type(Unsigned32):
    """Custom type juniDosProtectionScfdsProtocolBackoffTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000),
    )


_JuniDosProtectionScfdsProtocolBackoffTime_Type.__name__ = "Unsigned32"
_JuniDosProtectionScfdsProtocolBackoffTime_Object = MibTableColumn
juniDosProtectionScfdsProtocolBackoffTime = _JuniDosProtectionScfdsProtocolBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 4),
    _JuniDosProtectionScfdsProtocolBackoffTime_Type()
)
juniDosProtectionScfdsProtocolBackoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolBackoffTime.setStatus("current")
_JuniDosProtectionScfdsProtocolState_Type = JuniDosProtectionProtocolState
_JuniDosProtectionScfdsProtocolState_Object = MibTableColumn
juniDosProtectionScfdsProtocolState = _JuniDosProtectionScfdsProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 5),
    _JuniDosProtectionScfdsProtocolState_Type()
)
juniDosProtectionScfdsProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolState.setStatus("current")
_JuniDosProtectionScfdsProtocolTransitions_Type = Counter32
_JuniDosProtectionScfdsProtocolTransitions_Object = MibTableColumn
juniDosProtectionScfdsProtocolTransitions = _JuniDosProtectionScfdsProtocolTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 6),
    _JuniDosProtectionScfdsProtocolTransitions_Type()
)
juniDosProtectionScfdsProtocolTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsProtocolTransitions.setStatus("current")
_JuniDosProtectionDpgGroup_ObjectIdentity = ObjectIdentity
juniDosProtectionDpgGroup = _JuniDosProtectionDpgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2)
)
_JuniDosProtectionDpgTable_Object = MibTable
juniDosProtectionDpgTable = _JuniDosProtectionDpgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgTable.setStatus("current")
_JuniDosProtectionDpgEntry_Object = MibTableRow
juniDosProtectionDpgEntry = _JuniDosProtectionDpgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1)
)
juniDosProtectionDpgEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgIndex"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgEntry.setStatus("current")


class _JuniDosProtectionDpgIndex_Type(DisplayString):
    """Custom type juniDosProtectionDpgIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgIndex_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgIndex_Object = MibTableColumn
juniDosProtectionDpgIndex = _JuniDosProtectionDpgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 1),
    _JuniDosProtectionDpgIndex_Type()
)
juniDosProtectionDpgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgIndex.setStatus("current")
_JuniDosProtectionDpgRowStatus_Type = RowStatus
_JuniDosProtectionDpgRowStatus_Object = MibTableColumn
juniDosProtectionDpgRowStatus = _JuniDosProtectionDpgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 2),
    _JuniDosProtectionDpgRowStatus_Type()
)
juniDosProtectionDpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgRowStatus.setStatus("current")


class _JuniDosProtectionDpgCanned_Type(JuniDosProtectionProtocolCannedType):
    """Custom type juniDosProtectionDpgCanned based on JuniDosProtectionProtocolCannedType"""


_JuniDosProtectionDpgCanned_Object = MibTableColumn
juniDosProtectionDpgCanned = _JuniDosProtectionDpgCanned_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 3),
    _JuniDosProtectionDpgCanned_Type()
)
juniDosProtectionDpgCanned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgCanned.setStatus("current")


class _JuniDosProtectionDpgRevert_Type(Integer32):
    """Custom type juniDosProtectionDpgRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-revert", 0),
          ("revert", 1))
    )


_JuniDosProtectionDpgRevert_Type.__name__ = "Integer32"
_JuniDosProtectionDpgRevert_Object = MibTableColumn
juniDosProtectionDpgRevert = _JuniDosProtectionDpgRevert_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 4),
    _JuniDosProtectionDpgRevert_Type()
)
juniDosProtectionDpgRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgRevert.setStatus("current")
_JuniDosProtectionDpgModified_Type = TruthValue
_JuniDosProtectionDpgModified_Object = MibTableColumn
juniDosProtectionDpgModified = _JuniDosProtectionDpgModified_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 5),
    _JuniDosProtectionDpgModified_Type()
)
juniDosProtectionDpgModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgModified.setStatus("current")
_JuniDosProtectionDpgReferences_Type = Integer32
_JuniDosProtectionDpgReferences_Object = MibTableColumn
juniDosProtectionDpgReferences = _JuniDosProtectionDpgReferences_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 6),
    _JuniDosProtectionDpgReferences_Type()
)
juniDosProtectionDpgReferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgReferences.setStatus("current")
_JuniDosProtectionDpgProtocolTable_Object = MibTable
juniDosProtectionDpgProtocolTable = _JuniDosProtectionDpgProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolTable.setStatus("current")
_JuniDosProtectionDpgProtocolEntry_Object = MibTableRow
juniDosProtectionDpgProtocolEntry = _JuniDosProtectionDpgProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1)
)
juniDosProtectionDpgProtocolEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolName"),
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolProtocol"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolEntry.setStatus("current")


class _JuniDosProtectionDpgProtocolName_Type(DisplayString):
    """Custom type juniDosProtectionDpgProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgProtocolName_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgProtocolName_Object = MibTableColumn
juniDosProtectionDpgProtocolName = _JuniDosProtectionDpgProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 1),
    _JuniDosProtectionDpgProtocolName_Type()
)
juniDosProtectionDpgProtocolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolName.setStatus("current")
_JuniDosProtectionDpgProtocolProtocol_Type = JuniDosProtectionProtocolType
_JuniDosProtectionDpgProtocolProtocol_Object = MibTableColumn
juniDosProtectionDpgProtocolProtocol = _JuniDosProtectionDpgProtocolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 2),
    _JuniDosProtectionDpgProtocolProtocol_Type()
)
juniDosProtectionDpgProtocolProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolProtocol.setStatus("current")


class _JuniDosProtectionDpgProtocolBurst_Type(Unsigned32):
    """Custom type juniDosProtectionDpgProtocolBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 65535),
    )


_JuniDosProtectionDpgProtocolBurst_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgProtocolBurst_Object = MibTableColumn
juniDosProtectionDpgProtocolBurst = _JuniDosProtectionDpgProtocolBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 3),
    _JuniDosProtectionDpgProtocolBurst_Type()
)
juniDosProtectionDpgProtocolBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolBurst.setStatus("current")


class _JuniDosProtectionDpgProtocolDropProbability_Type(Unsigned32):
    """Custom type juniDosProtectionDpgProtocolDropProbability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_JuniDosProtectionDpgProtocolDropProbability_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgProtocolDropProbability_Object = MibTableColumn
juniDosProtectionDpgProtocolDropProbability = _JuniDosProtectionDpgProtocolDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 4),
    _JuniDosProtectionDpgProtocolDropProbability_Type()
)
juniDosProtectionDpgProtocolDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolDropProbability.setStatus("current")


class _JuniDosProtectionDpgProtocolRate_Type(Unsigned32):
    """Custom type juniDosProtectionDpgProtocolRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 65535),
    )


_JuniDosProtectionDpgProtocolRate_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgProtocolRate_Object = MibTableColumn
juniDosProtectionDpgProtocolRate = _JuniDosProtectionDpgProtocolRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 5),
    _JuniDosProtectionDpgProtocolRate_Type()
)
juniDosProtectionDpgProtocolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolRate.setStatus("current")
_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Type = JuniEnable
_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Object = MibTableColumn
juniDosProtectionDpgProtocolSkipPriorityRateLimiter = _JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 6),
    _JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Type()
)
juniDosProtectionDpgProtocolSkipPriorityRateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolSkipPriorityRateLimiter.setStatus("current")


class _JuniDosProtectionDpgProtocolWeight_Type(Unsigned32):
    """Custom type juniDosProtectionDpgProtocolWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_JuniDosProtectionDpgProtocolWeight_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgProtocolWeight_Object = MibTableColumn
juniDosProtectionDpgProtocolWeight = _JuniDosProtectionDpgProtocolWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 7),
    _JuniDosProtectionDpgProtocolWeight_Type()
)
juniDosProtectionDpgProtocolWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolWeight.setStatus("current")
_JuniDosProtectionDpgProtocolPriority_Type = JuniDosProtectionProtocolPriorityType
_JuniDosProtectionDpgProtocolPriority_Object = MibTableColumn
juniDosProtectionDpgProtocolPriority = _JuniDosProtectionDpgProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 8),
    _JuniDosProtectionDpgProtocolPriority_Type()
)
juniDosProtectionDpgProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolPriority.setStatus("current")
_JuniDosProtectionDpgProtocolModified_Type = TruthValue
_JuniDosProtectionDpgProtocolModified_Object = MibTableColumn
juniDosProtectionDpgProtocolModified = _JuniDosProtectionDpgProtocolModified_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 9),
    _JuniDosProtectionDpgProtocolModified_Type()
)
juniDosProtectionDpgProtocolModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolModified.setStatus("current")
_JuniDosProtectionDpgProtocolDestination_Type = JuniDosProtectionControlProcessorDestination
_JuniDosProtectionDpgProtocolDestination_Object = MibTableColumn
juniDosProtectionDpgProtocolDestination = _JuniDosProtectionDpgProtocolDestination_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 10),
    _JuniDosProtectionDpgProtocolDestination_Type()
)
juniDosProtectionDpgProtocolDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProtocolDestination.setStatus("current")
_JuniDosProtectionDpgPriorityTable_Object = MibTable
juniDosProtectionDpgPriorityTable = _JuniDosProtectionDpgPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityTable.setStatus("current")
_JuniDosProtectionDpgPriorityEntry_Object = MibTableRow
juniDosProtectionDpgPriorityEntry = _JuniDosProtectionDpgPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1)
)
juniDosProtectionDpgPriorityEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityName"),
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityPriority"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityEntry.setStatus("current")


class _JuniDosProtectionDpgPriorityName_Type(DisplayString):
    """Custom type juniDosProtectionDpgPriorityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgPriorityName_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgPriorityName_Object = MibTableColumn
juniDosProtectionDpgPriorityName = _JuniDosProtectionDpgPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 1),
    _JuniDosProtectionDpgPriorityName_Type()
)
juniDosProtectionDpgPriorityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityName.setStatus("current")
_JuniDosProtectionDpgPriorityPriority_Type = JuniDosProtectionPriorityType
_JuniDosProtectionDpgPriorityPriority_Object = MibTableColumn
juniDosProtectionDpgPriorityPriority = _JuniDosProtectionDpgPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 2),
    _JuniDosProtectionDpgPriorityPriority_Type()
)
juniDosProtectionDpgPriorityPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityPriority.setStatus("current")


class _JuniDosProtectionDpgPriorityBurst_Type(Unsigned32):
    """Custom type juniDosProtectionDpgPriorityBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 65535),
    )


_JuniDosProtectionDpgPriorityBurst_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgPriorityBurst_Object = MibTableColumn
juniDosProtectionDpgPriorityBurst = _JuniDosProtectionDpgPriorityBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 3),
    _JuniDosProtectionDpgPriorityBurst_Type()
)
juniDosProtectionDpgPriorityBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityBurst.setStatus("current")


class _JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type(Unsigned32):
    """Custom type juniDosProtectionDpgPriorityOverSubscriptionFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Object = MibTableColumn
juniDosProtectionDpgPriorityOverSubscriptionFactor = _JuniDosProtectionDpgPriorityOverSubscriptionFactor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 4),
    _JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type()
)
juniDosProtectionDpgPriorityOverSubscriptionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityOverSubscriptionFactor.setStatus("current")


class _JuniDosProtectionDpgPriorityRate_Type(Unsigned32):
    """Custom type juniDosProtectionDpgPriorityRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 65535),
    )


_JuniDosProtectionDpgPriorityRate_Type.__name__ = "Unsigned32"
_JuniDosProtectionDpgPriorityRate_Object = MibTableColumn
juniDosProtectionDpgPriorityRate = _JuniDosProtectionDpgPriorityRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 5),
    _JuniDosProtectionDpgPriorityRate_Type()
)
juniDosProtectionDpgPriorityRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityRate.setStatus("current")
_JuniDosProtectionDpgPriorityModified_Type = TruthValue
_JuniDosProtectionDpgPriorityModified_Object = MibTableColumn
juniDosProtectionDpgPriorityModified = _JuniDosProtectionDpgPriorityModified_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 6),
    _JuniDosProtectionDpgPriorityModified_Type()
)
juniDosProtectionDpgPriorityModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgPriorityModified.setStatus("current")
_JuniDosProtectionDpgAttachTable_Object = MibTable
juniDosProtectionDpgAttachTable = _JuniDosProtectionDpgAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachTable.setStatus("current")
_JuniDosProtectionDpgAttachEntry_Object = MibTableRow
juniDosProtectionDpgAttachEntry = _JuniDosProtectionDpgAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1)
)
juniDosProtectionDpgAttachEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachIndex"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachEntry.setStatus("current")
_JuniDosProtectionDpgAttachIndex_Type = InterfaceIndex
_JuniDosProtectionDpgAttachIndex_Object = MibTableColumn
juniDosProtectionDpgAttachIndex = _JuniDosProtectionDpgAttachIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 1),
    _JuniDosProtectionDpgAttachIndex_Type()
)
juniDosProtectionDpgAttachIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachIndex.setStatus("current")
_JuniDosProtectionDpgAttachRowStatus_Type = RowStatus
_JuniDosProtectionDpgAttachRowStatus_Object = MibTableColumn
juniDosProtectionDpgAttachRowStatus = _JuniDosProtectionDpgAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 2),
    _JuniDosProtectionDpgAttachRowStatus_Type()
)
juniDosProtectionDpgAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachRowStatus.setStatus("current")


class _JuniDosProtectionDpgAttachName_Type(DisplayString):
    """Custom type juniDosProtectionDpgAttachName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgAttachName_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgAttachName_Object = MibTableColumn
juniDosProtectionDpgAttachName = _JuniDosProtectionDpgAttachName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 3),
    _JuniDosProtectionDpgAttachName_Type()
)
juniDosProtectionDpgAttachName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachName.setStatus("current")
_JuniDosProtectionDpgAttachConfigured_Type = TruthValue
_JuniDosProtectionDpgAttachConfigured_Object = MibTableColumn
juniDosProtectionDpgAttachConfigured = _JuniDosProtectionDpgAttachConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 4),
    _JuniDosProtectionDpgAttachConfigured_Type()
)
juniDosProtectionDpgAttachConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgAttachConfigured.setStatus("current")
_JuniDosProtectionDpgProfileTable_Object = MibTable
juniDosProtectionDpgProfileTable = _JuniDosProtectionDpgProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileTable.setStatus("current")
_JuniDosProtectionDpgProfileEntry_Object = MibTableRow
juniDosProtectionDpgProfileEntry = _JuniDosProtectionDpgProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1)
)
juniDosProtectionDpgProfileEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileProfileId"),
    (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileLayerId"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileEntry.setStatus("current")
_JuniDosProtectionDpgProfileProfileId_Type = Unsigned32
_JuniDosProtectionDpgProfileProfileId_Object = MibTableColumn
juniDosProtectionDpgProfileProfileId = _JuniDosProtectionDpgProfileProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 1),
    _JuniDosProtectionDpgProfileProfileId_Type()
)
juniDosProtectionDpgProfileProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileProfileId.setStatus("current")
_JuniDosProtectionDpgProfileLayerId_Type = JuniDosProtectionLayerId
_JuniDosProtectionDpgProfileLayerId_Object = MibTableColumn
juniDosProtectionDpgProfileLayerId = _JuniDosProtectionDpgProfileLayerId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 2),
    _JuniDosProtectionDpgProfileLayerId_Type()
)
juniDosProtectionDpgProfileLayerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileLayerId.setStatus("current")
_JuniDosProtectionDpgProfileRowStatus_Type = RowStatus
_JuniDosProtectionDpgProfileRowStatus_Object = MibTableColumn
juniDosProtectionDpgProfileRowStatus = _JuniDosProtectionDpgProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 3),
    _JuniDosProtectionDpgProfileRowStatus_Type()
)
juniDosProtectionDpgProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileRowStatus.setStatus("current")


class _JuniDosProtectionDpgProfileName_Type(DisplayString):
    """Custom type juniDosProtectionDpgProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgProfileName_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgProfileName_Object = MibTableColumn
juniDosProtectionDpgProfileName = _JuniDosProtectionDpgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 4),
    _JuniDosProtectionDpgProfileName_Type()
)
juniDosProtectionDpgProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDosProtectionDpgProfileName.setStatus("current")
_JuniDosProtectionMIBConformance_ObjectIdentity = ObjectIdentity
juniDosProtectionMIBConformance = _JuniDosProtectionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4)
)
_JuniDosProtectionMIBCompliances_ObjectIdentity = ObjectIdentity
juniDosProtectionMIBCompliances = _JuniDosProtectionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1)
)
_JuniDosProtectionMIBGroups_ObjectIdentity = ObjectIdentity
juniDosProtectionMIBGroups = _JuniDosProtectionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2)
)

# Managed Objects groups

juniDosProtectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2, 1)
)
juniDosProtectionGroup.setObjects(
      *(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalGrouping"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalClearAll"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalDiscontinuityTime"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalTableOverflowState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberTableOverflows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolThreshold"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolLowThreshold"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolBackoffTime"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolTransitions"))
)
if mibBuilder.loadTexts:
    juniDosProtectionGroup.setStatus("obsolete")

juniDosProtectionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2, 2)
)
juniDosProtectionGroup2.setObjects(
      *(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalGrouping"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalClearAll"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalDiscontinuityTime"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalTableOverflowState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberTableOverflows"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolThreshold"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolLowThreshold"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolBackoffTime"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolState"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolTransitions"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgRowStatus"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgCanned"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgRevert"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgModified"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgReferences"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolBurst"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolDropProbability"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolRate"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolSkipPriorityRateLimiter"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolWeight"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolModified"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityBurst"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityOverSubscriptionFactor"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityRate"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityModified"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachRowStatus"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachName"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileRowStatus"),
        ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileName"))
)
if mibBuilder.loadTexts:
    juniDosProtectionGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDosProtectionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionCompliance.setStatus(
        "obsolete"
    )

juniDosProtectionCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDosProtectionCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DOS-PROTECTION-MIB",
    **{"JuniDosProtectionProtocolType": JuniDosProtectionProtocolType,
       "JuniDosProtectionPriorityType": JuniDosProtectionPriorityType,
       "JuniDosProtectionProtocolState": JuniDosProtectionProtocolState,
       "JuniDosProtectionScfdsTableOverflowState": JuniDosProtectionScfdsTableOverflowState,
       "JuniDosProtectionProtocolPriorityType": JuniDosProtectionProtocolPriorityType,
       "JuniDosProtectionProtocolCannedType": JuniDosProtectionProtocolCannedType,
       "JuniDosProtectionLayerId": JuniDosProtectionLayerId,
       "JuniDosProtectionControlProcessorDestination": JuniDosProtectionControlProcessorDestination,
       "juniDosProtectionMIB": juniDosProtectionMIB,
       "juniDosProtectionObjects": juniDosProtectionObjects,
       "juniDosProtectionScfdsGroup": juniDosProtectionScfdsGroup,
       "juniDosProtectionScfdsGlobalState": juniDosProtectionScfdsGlobalState,
       "juniDosProtectionScfdsGlobalGrouping": juniDosProtectionScfdsGlobalGrouping,
       "juniDosProtectionScfdsGlobalClearAll": juniDosProtectionScfdsGlobalClearAll,
       "juniDosProtectionScfdsGlobalDiscontinuityTime": juniDosProtectionScfdsGlobalDiscontinuityTime,
       "juniDosProtectionScfdsGlobalTableOverflowState": juniDosProtectionScfdsGlobalTableOverflowState,
       "juniDosProtectionScfdsGlobalCurrentSuspiciousFlows": juniDosProtectionScfdsGlobalCurrentSuspiciousFlows,
       "juniDosProtectionScfdsGlobalNumberSuspiciousFlows": juniDosProtectionScfdsGlobalNumberSuspiciousFlows,
       "juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups": juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups,
       "juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups": juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups,
       "juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows": juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows,
       "juniDosProtectionScfdsGlobalNumberFalseNegativeFlows": juniDosProtectionScfdsGlobalNumberFalseNegativeFlows,
       "juniDosProtectionScfdsGlobalNumberTableOverflows": juniDosProtectionScfdsGlobalNumberTableOverflows,
       "juniDosProtectionScfdsProtocolTable": juniDosProtectionScfdsProtocolTable,
       "juniDosProtectionScfdsProtocolEntry": juniDosProtectionScfdsProtocolEntry,
       "juniDosProtectionScfdsProtocolIndex": juniDosProtectionScfdsProtocolIndex,
       "juniDosProtectionScfdsProtocolThreshold": juniDosProtectionScfdsProtocolThreshold,
       "juniDosProtectionScfdsProtocolLowThreshold": juniDosProtectionScfdsProtocolLowThreshold,
       "juniDosProtectionScfdsProtocolBackoffTime": juniDosProtectionScfdsProtocolBackoffTime,
       "juniDosProtectionScfdsProtocolState": juniDosProtectionScfdsProtocolState,
       "juniDosProtectionScfdsProtocolTransitions": juniDosProtectionScfdsProtocolTransitions,
       "juniDosProtectionDpgGroup": juniDosProtectionDpgGroup,
       "juniDosProtectionDpgTable": juniDosProtectionDpgTable,
       "juniDosProtectionDpgEntry": juniDosProtectionDpgEntry,
       "juniDosProtectionDpgIndex": juniDosProtectionDpgIndex,
       "juniDosProtectionDpgRowStatus": juniDosProtectionDpgRowStatus,
       "juniDosProtectionDpgCanned": juniDosProtectionDpgCanned,
       "juniDosProtectionDpgRevert": juniDosProtectionDpgRevert,
       "juniDosProtectionDpgModified": juniDosProtectionDpgModified,
       "juniDosProtectionDpgReferences": juniDosProtectionDpgReferences,
       "juniDosProtectionDpgProtocolTable": juniDosProtectionDpgProtocolTable,
       "juniDosProtectionDpgProtocolEntry": juniDosProtectionDpgProtocolEntry,
       "juniDosProtectionDpgProtocolName": juniDosProtectionDpgProtocolName,
       "juniDosProtectionDpgProtocolProtocol": juniDosProtectionDpgProtocolProtocol,
       "juniDosProtectionDpgProtocolBurst": juniDosProtectionDpgProtocolBurst,
       "juniDosProtectionDpgProtocolDropProbability": juniDosProtectionDpgProtocolDropProbability,
       "juniDosProtectionDpgProtocolRate": juniDosProtectionDpgProtocolRate,
       "juniDosProtectionDpgProtocolSkipPriorityRateLimiter": juniDosProtectionDpgProtocolSkipPriorityRateLimiter,
       "juniDosProtectionDpgProtocolWeight": juniDosProtectionDpgProtocolWeight,
       "juniDosProtectionDpgProtocolPriority": juniDosProtectionDpgProtocolPriority,
       "juniDosProtectionDpgProtocolModified": juniDosProtectionDpgProtocolModified,
       "juniDosProtectionDpgProtocolDestination": juniDosProtectionDpgProtocolDestination,
       "juniDosProtectionDpgPriorityTable": juniDosProtectionDpgPriorityTable,
       "juniDosProtectionDpgPriorityEntry": juniDosProtectionDpgPriorityEntry,
       "juniDosProtectionDpgPriorityName": juniDosProtectionDpgPriorityName,
       "juniDosProtectionDpgPriorityPriority": juniDosProtectionDpgPriorityPriority,
       "juniDosProtectionDpgPriorityBurst": juniDosProtectionDpgPriorityBurst,
       "juniDosProtectionDpgPriorityOverSubscriptionFactor": juniDosProtectionDpgPriorityOverSubscriptionFactor,
       "juniDosProtectionDpgPriorityRate": juniDosProtectionDpgPriorityRate,
       "juniDosProtectionDpgPriorityModified": juniDosProtectionDpgPriorityModified,
       "juniDosProtectionDpgAttachTable": juniDosProtectionDpgAttachTable,
       "juniDosProtectionDpgAttachEntry": juniDosProtectionDpgAttachEntry,
       "juniDosProtectionDpgAttachIndex": juniDosProtectionDpgAttachIndex,
       "juniDosProtectionDpgAttachRowStatus": juniDosProtectionDpgAttachRowStatus,
       "juniDosProtectionDpgAttachName": juniDosProtectionDpgAttachName,
       "juniDosProtectionDpgAttachConfigured": juniDosProtectionDpgAttachConfigured,
       "juniDosProtectionDpgProfileTable": juniDosProtectionDpgProfileTable,
       "juniDosProtectionDpgProfileEntry": juniDosProtectionDpgProfileEntry,
       "juniDosProtectionDpgProfileProfileId": juniDosProtectionDpgProfileProfileId,
       "juniDosProtectionDpgProfileLayerId": juniDosProtectionDpgProfileLayerId,
       "juniDosProtectionDpgProfileRowStatus": juniDosProtectionDpgProfileRowStatus,
       "juniDosProtectionDpgProfileName": juniDosProtectionDpgProfileName,
       "juniDosProtectionMIBConformance": juniDosProtectionMIBConformance,
       "juniDosProtectionMIBCompliances": juniDosProtectionMIBCompliances,
       "juniDosProtectionCompliance": juniDosProtectionCompliance,
       "juniDosProtectionCompliance2": juniDosProtectionCompliance2,
       "juniDosProtectionMIBGroups": juniDosProtectionMIBGroups,
       "juniDosProtectionGroup": juniDosProtectionGroup,
       "juniDosProtectionGroup2": juniDosProtectionGroup2}
)
