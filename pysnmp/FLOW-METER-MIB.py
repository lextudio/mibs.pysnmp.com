# SNMP MIB module (FLOW-METER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FLOW-METER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:08 2024
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

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

flowMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 40)
)
flowMIB.setRevisions(
        ("1999-10-25 00:00",
         "1999-08-30 12:50",
         "1999-08-19 10:10",
         "1997-12-23 09:37",
         "1997-07-07 17:15",
         "1996-03-08 02:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UTF8OwnerString(OctetString, TextualConvention):
    status = "current"
    displayHint = "127t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class PeerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 12),
          ("decnet", 13),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 11),
          ("nsap", 3))
    )



class PeerAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )



class AdjacentType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              9,
              11,
              12,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 12),
          ("decnet", 13),
          ("ethernet", 7),
          ("fddi", 15),
          ("ip", 1),
          ("ipx", 11),
          ("nsap", 3),
          ("tokenring", 9))
    )



class AdjacentAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )



class TransportType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TransportAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class RuleAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )



class FlowAttributeNumber(Integer32, TextualConvention):
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
              41)
        )
    )
    namedValues = NamedValues(
        *(("destAdjacentAddress", 16),
          ("destAdjacentMask", 17),
          ("destAdjacentType", 15),
          ("destClass", 37),
          ("destInterface", 14),
          ("destKind", 40),
          ("destPeerAddress", 19),
          ("destPeerMask", 20),
          ("destPeerType", 18),
          ("destSubscriberID", 34),
          ("destTransAddress", 22),
          ("destTransMask", 23),
          ("destTransType", 21),
          ("firstTime", 31),
          ("flowClass", 38),
          ("flowIndex", 1),
          ("flowKind", 41),
          ("flowStatus", 2),
          ("flowTimeMark", 3),
          ("fromOctets", 29),
          ("fromPDUs", 30),
          ("lastActiveTime", 32),
          ("octetScale", 25),
          ("pduScale", 24),
          ("ruleSet", 26),
          ("sessionID", 35),
          ("sourceAdjacentAddress", 6),
          ("sourceAdjacentMask", 7),
          ("sourceAdjacentType", 5),
          ("sourceClass", 36),
          ("sourceInterface", 4),
          ("sourceKind", 39),
          ("sourcePeerAddress", 9),
          ("sourcePeerMask", 10),
          ("sourcePeerType", 8),
          ("sourceSubscriberID", 33),
          ("sourceTransAddress", 12),
          ("sourceTransMask", 13),
          ("sourceTransType", 11),
          ("toOctets", 27),
          ("toPDUs", 28))
    )



class RuleAttributeNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              8,
              9,
              11,
              12,
              14,
              15,
              16,
              18,
              19,
              21,
              22,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              50,
              51,
              52,
              53,
              54,
              55)
        )
    )
    namedValues = NamedValues(
        *(("destAdjacentAddress", 16),
          ("destAdjacentType", 15),
          ("destClass", 37),
          ("destInterface", 14),
          ("destKind", 40),
          ("destPeerAddress", 19),
          ("destPeerType", 18),
          ("destSubscriberID", 34),
          ("destTransAddress", 22),
          ("destTransType", 21),
          ("flowClass", 38),
          ("flowKind", 41),
          ("matchingStoD", 50),
          ("null", 0),
          ("sessionID", 35),
          ("sourceAdjacentAddress", 6),
          ("sourceAdjacentType", 5),
          ("sourceClass", 36),
          ("sourceInterface", 4),
          ("sourceKind", 39),
          ("sourcePeerAddress", 9),
          ("sourcePeerType", 8),
          ("sourceSubscriberID", 33),
          ("sourceTransAddress", 12),
          ("sourceTransType", 11),
          ("v1", 51),
          ("v2", 52),
          ("v3", 53),
          ("v4", 54),
          ("v5", 55))
    )



class ActionNumber(Integer32, TextualConvention):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("assign", 8),
          ("assignAct", 9),
          ("count", 3),
          ("countPkt", 4),
          ("gosub", 6),
          ("gosubAct", 7),
          ("goto", 10),
          ("gotoAct", 11),
          ("ignore", 1),
          ("noMatch", 2),
          ("popTo", 16),
          ("popToAct", 17),
          ("pushPktTo", 14),
          ("pushPktToAct", 15),
          ("pushRuleTo", 12),
          ("pushRuleToAct", 13),
          ("return", 5))
    )



# MIB Managed Objects in the order of their OIDs

_FlowControl_ObjectIdentity = ObjectIdentity
flowControl = _FlowControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 1)
)
_FlowRuleSetInfoTable_Object = MibTable
flowRuleSetInfoTable = _FlowRuleSetInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1)
)
if mibBuilder.loadTexts:
    flowRuleSetInfoTable.setStatus("current")
_FlowRuleSetInfoEntry_Object = MibTableRow
flowRuleSetInfoEntry = _FlowRuleSetInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1)
)
flowRuleSetInfoEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowRuleInfoIndex"),
)
if mibBuilder.loadTexts:
    flowRuleSetInfoEntry.setStatus("current")


class _FlowRuleInfoIndex_Type(Integer32):
    """Custom type flowRuleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowRuleInfoIndex_Type.__name__ = "Integer32"
_FlowRuleInfoIndex_Object = MibTableColumn
flowRuleInfoIndex = _FlowRuleInfoIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 1),
    _FlowRuleInfoIndex_Type()
)
flowRuleInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowRuleInfoIndex.setStatus("current")
_FlowRuleInfoSize_Type = Integer32
_FlowRuleInfoSize_Object = MibTableColumn
flowRuleInfoSize = _FlowRuleInfoSize_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 2),
    _FlowRuleInfoSize_Type()
)
flowRuleInfoSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRuleInfoSize.setStatus("current")
_FlowRuleInfoOwner_Type = UTF8OwnerString
_FlowRuleInfoOwner_Object = MibTableColumn
flowRuleInfoOwner = _FlowRuleInfoOwner_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 3),
    _FlowRuleInfoOwner_Type()
)
flowRuleInfoOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRuleInfoOwner.setStatus("current")
_FlowRuleInfoTimeStamp_Type = TimeStamp
_FlowRuleInfoTimeStamp_Object = MibTableColumn
flowRuleInfoTimeStamp = _FlowRuleInfoTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 4),
    _FlowRuleInfoTimeStamp_Type()
)
flowRuleInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowRuleInfoTimeStamp.setStatus("current")
_FlowRuleInfoStatus_Type = RowStatus
_FlowRuleInfoStatus_Object = MibTableColumn
flowRuleInfoStatus = _FlowRuleInfoStatus_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 5),
    _FlowRuleInfoStatus_Type()
)
flowRuleInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRuleInfoStatus.setStatus("current")


class _FlowRuleInfoName_Type(OctetString):
    """Custom type flowRuleInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FlowRuleInfoName_Type.__name__ = "OctetString"
_FlowRuleInfoName_Object = MibTableColumn
flowRuleInfoName = _FlowRuleInfoName_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 6),
    _FlowRuleInfoName_Type()
)
flowRuleInfoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRuleInfoName.setStatus("current")
_FlowRuleInfoRulesReady_Type = TruthValue
_FlowRuleInfoRulesReady_Object = MibTableColumn
flowRuleInfoRulesReady = _FlowRuleInfoRulesReady_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 7),
    _FlowRuleInfoRulesReady_Type()
)
flowRuleInfoRulesReady.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowRuleInfoRulesReady.setStatus("deprecated")
_FlowRuleInfoFlowRecords_Type = Integer32
_FlowRuleInfoFlowRecords_Object = MibTableColumn
flowRuleInfoFlowRecords = _FlowRuleInfoFlowRecords_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 8),
    _FlowRuleInfoFlowRecords_Type()
)
flowRuleInfoFlowRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowRuleInfoFlowRecords.setStatus("current")
_FlowInterfaceTable_Object = MibTable
flowInterfaceTable = _FlowInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 2)
)
if mibBuilder.loadTexts:
    flowInterfaceTable.setStatus("current")
_FlowInterfaceEntry_Object = MibTableRow
flowInterfaceEntry = _FlowInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 2, 1)
)
flowInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flowInterfaceEntry.setStatus("current")


class _FlowInterfaceSampleRate_Type(Integer32):
    """Custom type flowInterfaceSampleRate based on Integer32"""
    defaultValue = 1


_FlowInterfaceSampleRate_Object = MibTableColumn
flowInterfaceSampleRate = _FlowInterfaceSampleRate_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 2, 1, 1),
    _FlowInterfaceSampleRate_Type()
)
flowInterfaceSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowInterfaceSampleRate.setStatus("current")
_FlowInterfaceLostPackets_Type = Counter32
_FlowInterfaceLostPackets_Object = MibTableColumn
flowInterfaceLostPackets = _FlowInterfaceLostPackets_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 2, 1, 2),
    _FlowInterfaceLostPackets_Type()
)
flowInterfaceLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowInterfaceLostPackets.setStatus("current")
_FlowReaderInfoTable_Object = MibTable
flowReaderInfoTable = _FlowReaderInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3)
)
if mibBuilder.loadTexts:
    flowReaderInfoTable.setStatus("current")
_FlowReaderInfoEntry_Object = MibTableRow
flowReaderInfoEntry = _FlowReaderInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1)
)
flowReaderInfoEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowReaderIndex"),
)
if mibBuilder.loadTexts:
    flowReaderInfoEntry.setStatus("current")


class _FlowReaderIndex_Type(Integer32):
    """Custom type flowReaderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowReaderIndex_Type.__name__ = "Integer32"
_FlowReaderIndex_Object = MibTableColumn
flowReaderIndex = _FlowReaderIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 1),
    _FlowReaderIndex_Type()
)
flowReaderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowReaderIndex.setStatus("current")
_FlowReaderTimeout_Type = Integer32
_FlowReaderTimeout_Object = MibTableColumn
flowReaderTimeout = _FlowReaderTimeout_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 2),
    _FlowReaderTimeout_Type()
)
flowReaderTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowReaderTimeout.setStatus("current")
_FlowReaderOwner_Type = UTF8OwnerString
_FlowReaderOwner_Object = MibTableColumn
flowReaderOwner = _FlowReaderOwner_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 3),
    _FlowReaderOwner_Type()
)
flowReaderOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowReaderOwner.setStatus("current")
_FlowReaderLastTime_Type = TimeStamp
_FlowReaderLastTime_Object = MibTableColumn
flowReaderLastTime = _FlowReaderLastTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 4),
    _FlowReaderLastTime_Type()
)
flowReaderLastTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowReaderLastTime.setStatus("current")
_FlowReaderPreviousTime_Type = TimeStamp
_FlowReaderPreviousTime_Object = MibTableColumn
flowReaderPreviousTime = _FlowReaderPreviousTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 5),
    _FlowReaderPreviousTime_Type()
)
flowReaderPreviousTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowReaderPreviousTime.setStatus("current")
_FlowReaderStatus_Type = RowStatus
_FlowReaderStatus_Object = MibTableColumn
flowReaderStatus = _FlowReaderStatus_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 6),
    _FlowReaderStatus_Type()
)
flowReaderStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowReaderStatus.setStatus("current")


class _FlowReaderRuleSet_Type(Integer32):
    """Custom type flowReaderRuleSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowReaderRuleSet_Type.__name__ = "Integer32"
_FlowReaderRuleSet_Object = MibTableColumn
flowReaderRuleSet = _FlowReaderRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 7),
    _FlowReaderRuleSet_Type()
)
flowReaderRuleSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowReaderRuleSet.setStatus("current")
_FlowManagerInfoTable_Object = MibTable
flowManagerInfoTable = _FlowManagerInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4)
)
if mibBuilder.loadTexts:
    flowManagerInfoTable.setStatus("current")
_FlowManagerInfoEntry_Object = MibTableRow
flowManagerInfoEntry = _FlowManagerInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1)
)
flowManagerInfoEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowManagerIndex"),
)
if mibBuilder.loadTexts:
    flowManagerInfoEntry.setStatus("current")


class _FlowManagerIndex_Type(Integer32):
    """Custom type flowManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowManagerIndex_Type.__name__ = "Integer32"
_FlowManagerIndex_Object = MibTableColumn
flowManagerIndex = _FlowManagerIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 1),
    _FlowManagerIndex_Type()
)
flowManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowManagerIndex.setStatus("current")
_FlowManagerCurrentRuleSet_Type = Integer32
_FlowManagerCurrentRuleSet_Object = MibTableColumn
flowManagerCurrentRuleSet = _FlowManagerCurrentRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 2),
    _FlowManagerCurrentRuleSet_Type()
)
flowManagerCurrentRuleSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerCurrentRuleSet.setStatus("current")


class _FlowManagerStandbyRuleSet_Type(Integer32):
    """Custom type flowManagerStandbyRuleSet based on Integer32"""
    defaultValue = 0


_FlowManagerStandbyRuleSet_Object = MibTableColumn
flowManagerStandbyRuleSet = _FlowManagerStandbyRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 3),
    _FlowManagerStandbyRuleSet_Type()
)
flowManagerStandbyRuleSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerStandbyRuleSet.setStatus("current")


class _FlowManagerHighWaterMark_Type(Integer32):
    """Custom type flowManagerHighWaterMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlowManagerHighWaterMark_Type.__name__ = "Integer32"
_FlowManagerHighWaterMark_Object = MibTableColumn
flowManagerHighWaterMark = _FlowManagerHighWaterMark_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 4),
    _FlowManagerHighWaterMark_Type()
)
flowManagerHighWaterMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerHighWaterMark.setStatus("current")


class _FlowManagerCounterWrap_Type(Integer32):
    """Custom type flowManagerCounterWrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scale", 2),
          ("wrap", 1))
    )


_FlowManagerCounterWrap_Type.__name__ = "Integer32"
_FlowManagerCounterWrap_Object = MibTableColumn
flowManagerCounterWrap = _FlowManagerCounterWrap_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 5),
    _FlowManagerCounterWrap_Type()
)
flowManagerCounterWrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerCounterWrap.setStatus("deprecated")
_FlowManagerOwner_Type = UTF8OwnerString
_FlowManagerOwner_Object = MibTableColumn
flowManagerOwner = _FlowManagerOwner_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 6),
    _FlowManagerOwner_Type()
)
flowManagerOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerOwner.setStatus("current")
_FlowManagerTimeStamp_Type = TimeStamp
_FlowManagerTimeStamp_Object = MibTableColumn
flowManagerTimeStamp = _FlowManagerTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 7),
    _FlowManagerTimeStamp_Type()
)
flowManagerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowManagerTimeStamp.setStatus("current")
_FlowManagerStatus_Type = RowStatus
_FlowManagerStatus_Object = MibTableColumn
flowManagerStatus = _FlowManagerStatus_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 8),
    _FlowManagerStatus_Type()
)
flowManagerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerStatus.setStatus("current")


class _FlowManagerRunningStandby_Type(TruthValue):
    """Custom type flowManagerRunningStandby based on TruthValue"""


_FlowManagerRunningStandby_Object = MibTableColumn
flowManagerRunningStandby = _FlowManagerRunningStandby_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 9),
    _FlowManagerRunningStandby_Type()
)
flowManagerRunningStandby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowManagerRunningStandby.setStatus("current")


class _FlowFloodMark_Type(Integer32):
    """Custom type flowFloodMark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlowFloodMark_Type.__name__ = "Integer32"
_FlowFloodMark_Object = MibScalar
flowFloodMark = _FlowFloodMark_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 5),
    _FlowFloodMark_Type()
)
flowFloodMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFloodMark.setStatus("current")


class _FlowInactivityTimeout_Type(Integer32):
    """Custom type flowInactivityTimeout based on Integer32"""
    defaultValue = 600


_FlowInactivityTimeout_Object = MibScalar
flowInactivityTimeout = _FlowInactivityTimeout_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 6),
    _FlowInactivityTimeout_Type()
)
flowInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowInactivityTimeout.setStatus("current")
_FlowActiveFlows_Type = Integer32
_FlowActiveFlows_Object = MibScalar
flowActiveFlows = _FlowActiveFlows_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 7),
    _FlowActiveFlows_Type()
)
flowActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowActiveFlows.setStatus("current")
_FlowMaxFlows_Type = Integer32
_FlowMaxFlows_Object = MibScalar
flowMaxFlows = _FlowMaxFlows_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 8),
    _FlowMaxFlows_Type()
)
flowMaxFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowMaxFlows.setStatus("current")
_FlowFloodMode_Type = TruthValue
_FlowFloodMode_Object = MibScalar
flowFloodMode = _FlowFloodMode_Object(
    (1, 3, 6, 1, 2, 1, 40, 1, 9),
    _FlowFloodMode_Type()
)
flowFloodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowFloodMode.setStatus("current")
_FlowData_ObjectIdentity = ObjectIdentity
flowData = _FlowData_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 2)
)
_FlowDataTable_Object = MibTable
flowDataTable = _FlowDataTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1)
)
if mibBuilder.loadTexts:
    flowDataTable.setStatus("current")
_FlowDataEntry_Object = MibTableRow
flowDataEntry = _FlowDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1)
)
flowDataEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowDataRuleSet"),
    (0, "FLOW-METER-MIB", "flowDataTimeMark"),
    (0, "FLOW-METER-MIB", "flowDataIndex"),
)
if mibBuilder.loadTexts:
    flowDataEntry.setStatus("current")


class _FlowDataIndex_Type(Integer32):
    """Custom type flowDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowDataIndex_Type.__name__ = "Integer32"
_FlowDataIndex_Object = MibTableColumn
flowDataIndex = _FlowDataIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 1),
    _FlowDataIndex_Type()
)
flowDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowDataIndex.setStatus("current")
_FlowDataTimeMark_Type = TimeFilter
_FlowDataTimeMark_Object = MibTableColumn
flowDataTimeMark = _FlowDataTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 2),
    _FlowDataTimeMark_Type()
)
flowDataTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowDataTimeMark.setStatus("current")


class _FlowDataStatus_Type(Integer32):
    """Custom type flowDataStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 2),
          ("inactive", 1))
    )


_FlowDataStatus_Type.__name__ = "Integer32"
_FlowDataStatus_Object = MibTableColumn
flowDataStatus = _FlowDataStatus_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 3),
    _FlowDataStatus_Type()
)
flowDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataStatus.setStatus("deprecated")
_FlowDataSourceInterface_Type = Integer32
_FlowDataSourceInterface_Object = MibTableColumn
flowDataSourceInterface = _FlowDataSourceInterface_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 4),
    _FlowDataSourceInterface_Type()
)
flowDataSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceInterface.setStatus("current")
_FlowDataSourceAdjacentType_Type = AdjacentType
_FlowDataSourceAdjacentType_Object = MibTableColumn
flowDataSourceAdjacentType = _FlowDataSourceAdjacentType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 5),
    _FlowDataSourceAdjacentType_Type()
)
flowDataSourceAdjacentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceAdjacentType.setStatus("current")
_FlowDataSourceAdjacentAddress_Type = AdjacentAddress
_FlowDataSourceAdjacentAddress_Object = MibTableColumn
flowDataSourceAdjacentAddress = _FlowDataSourceAdjacentAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 6),
    _FlowDataSourceAdjacentAddress_Type()
)
flowDataSourceAdjacentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceAdjacentAddress.setStatus("current")
_FlowDataSourceAdjacentMask_Type = AdjacentAddress
_FlowDataSourceAdjacentMask_Object = MibTableColumn
flowDataSourceAdjacentMask = _FlowDataSourceAdjacentMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 7),
    _FlowDataSourceAdjacentMask_Type()
)
flowDataSourceAdjacentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceAdjacentMask.setStatus("current")
_FlowDataSourcePeerType_Type = PeerType
_FlowDataSourcePeerType_Object = MibTableColumn
flowDataSourcePeerType = _FlowDataSourcePeerType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 8),
    _FlowDataSourcePeerType_Type()
)
flowDataSourcePeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourcePeerType.setStatus("current")
_FlowDataSourcePeerAddress_Type = PeerAddress
_FlowDataSourcePeerAddress_Object = MibTableColumn
flowDataSourcePeerAddress = _FlowDataSourcePeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 9),
    _FlowDataSourcePeerAddress_Type()
)
flowDataSourcePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourcePeerAddress.setStatus("current")
_FlowDataSourcePeerMask_Type = PeerAddress
_FlowDataSourcePeerMask_Object = MibTableColumn
flowDataSourcePeerMask = _FlowDataSourcePeerMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 10),
    _FlowDataSourcePeerMask_Type()
)
flowDataSourcePeerMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourcePeerMask.setStatus("current")
_FlowDataSourceTransType_Type = TransportType
_FlowDataSourceTransType_Object = MibTableColumn
flowDataSourceTransType = _FlowDataSourceTransType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 11),
    _FlowDataSourceTransType_Type()
)
flowDataSourceTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceTransType.setStatus("current")
_FlowDataSourceTransAddress_Type = TransportAddress
_FlowDataSourceTransAddress_Object = MibTableColumn
flowDataSourceTransAddress = _FlowDataSourceTransAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 12),
    _FlowDataSourceTransAddress_Type()
)
flowDataSourceTransAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceTransAddress.setStatus("current")
_FlowDataSourceTransMask_Type = TransportAddress
_FlowDataSourceTransMask_Object = MibTableColumn
flowDataSourceTransMask = _FlowDataSourceTransMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 13),
    _FlowDataSourceTransMask_Type()
)
flowDataSourceTransMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceTransMask.setStatus("current")
_FlowDataDestInterface_Type = Integer32
_FlowDataDestInterface_Object = MibTableColumn
flowDataDestInterface = _FlowDataDestInterface_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 14),
    _FlowDataDestInterface_Type()
)
flowDataDestInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestInterface.setStatus("current")
_FlowDataDestAdjacentType_Type = AdjacentType
_FlowDataDestAdjacentType_Object = MibTableColumn
flowDataDestAdjacentType = _FlowDataDestAdjacentType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 15),
    _FlowDataDestAdjacentType_Type()
)
flowDataDestAdjacentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestAdjacentType.setStatus("current")
_FlowDataDestAdjacentAddress_Type = AdjacentAddress
_FlowDataDestAdjacentAddress_Object = MibTableColumn
flowDataDestAdjacentAddress = _FlowDataDestAdjacentAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 16),
    _FlowDataDestAdjacentAddress_Type()
)
flowDataDestAdjacentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestAdjacentAddress.setStatus("current")
_FlowDataDestAdjacentMask_Type = AdjacentAddress
_FlowDataDestAdjacentMask_Object = MibTableColumn
flowDataDestAdjacentMask = _FlowDataDestAdjacentMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 17),
    _FlowDataDestAdjacentMask_Type()
)
flowDataDestAdjacentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestAdjacentMask.setStatus("current")
_FlowDataDestPeerType_Type = PeerType
_FlowDataDestPeerType_Object = MibTableColumn
flowDataDestPeerType = _FlowDataDestPeerType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 18),
    _FlowDataDestPeerType_Type()
)
flowDataDestPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestPeerType.setStatus("current")
_FlowDataDestPeerAddress_Type = PeerAddress
_FlowDataDestPeerAddress_Object = MibTableColumn
flowDataDestPeerAddress = _FlowDataDestPeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 19),
    _FlowDataDestPeerAddress_Type()
)
flowDataDestPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestPeerAddress.setStatus("current")
_FlowDataDestPeerMask_Type = PeerAddress
_FlowDataDestPeerMask_Object = MibTableColumn
flowDataDestPeerMask = _FlowDataDestPeerMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 20),
    _FlowDataDestPeerMask_Type()
)
flowDataDestPeerMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestPeerMask.setStatus("current")
_FlowDataDestTransType_Type = TransportType
_FlowDataDestTransType_Object = MibTableColumn
flowDataDestTransType = _FlowDataDestTransType_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 21),
    _FlowDataDestTransType_Type()
)
flowDataDestTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestTransType.setStatus("current")
_FlowDataDestTransAddress_Type = TransportAddress
_FlowDataDestTransAddress_Object = MibTableColumn
flowDataDestTransAddress = _FlowDataDestTransAddress_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 22),
    _FlowDataDestTransAddress_Type()
)
flowDataDestTransAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestTransAddress.setStatus("current")
_FlowDataDestTransMask_Type = TransportAddress
_FlowDataDestTransMask_Object = MibTableColumn
flowDataDestTransMask = _FlowDataDestTransMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 23),
    _FlowDataDestTransMask_Type()
)
flowDataDestTransMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestTransMask.setStatus("current")


class _FlowDataPDUScale_Type(Integer32):
    """Custom type flowDataPDUScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlowDataPDUScale_Type.__name__ = "Integer32"
_FlowDataPDUScale_Object = MibTableColumn
flowDataPDUScale = _FlowDataPDUScale_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 24),
    _FlowDataPDUScale_Type()
)
flowDataPDUScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataPDUScale.setStatus("current")


class _FlowDataOctetScale_Type(Integer32):
    """Custom type flowDataOctetScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlowDataOctetScale_Type.__name__ = "Integer32"
_FlowDataOctetScale_Object = MibTableColumn
flowDataOctetScale = _FlowDataOctetScale_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 25),
    _FlowDataOctetScale_Type()
)
flowDataOctetScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataOctetScale.setStatus("current")


class _FlowDataRuleSet_Type(Integer32):
    """Custom type flowDataRuleSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataRuleSet_Type.__name__ = "Integer32"
_FlowDataRuleSet_Object = MibTableColumn
flowDataRuleSet = _FlowDataRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 26),
    _FlowDataRuleSet_Type()
)
flowDataRuleSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowDataRuleSet.setStatus("current")
_FlowDataToOctets_Type = Counter64
_FlowDataToOctets_Object = MibTableColumn
flowDataToOctets = _FlowDataToOctets_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 27),
    _FlowDataToOctets_Type()
)
flowDataToOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataToOctets.setStatus("current")
_FlowDataToPDUs_Type = Counter64
_FlowDataToPDUs_Object = MibTableColumn
flowDataToPDUs = _FlowDataToPDUs_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 28),
    _FlowDataToPDUs_Type()
)
flowDataToPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataToPDUs.setStatus("current")
_FlowDataFromOctets_Type = Counter64
_FlowDataFromOctets_Object = MibTableColumn
flowDataFromOctets = _FlowDataFromOctets_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 29),
    _FlowDataFromOctets_Type()
)
flowDataFromOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataFromOctets.setStatus("current")
_FlowDataFromPDUs_Type = Counter64
_FlowDataFromPDUs_Object = MibTableColumn
flowDataFromPDUs = _FlowDataFromPDUs_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 30),
    _FlowDataFromPDUs_Type()
)
flowDataFromPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataFromPDUs.setStatus("current")
_FlowDataFirstTime_Type = TimeStamp
_FlowDataFirstTime_Object = MibTableColumn
flowDataFirstTime = _FlowDataFirstTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 31),
    _FlowDataFirstTime_Type()
)
flowDataFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataFirstTime.setStatus("current")
_FlowDataLastActiveTime_Type = TimeStamp
_FlowDataLastActiveTime_Object = MibTableColumn
flowDataLastActiveTime = _FlowDataLastActiveTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 32),
    _FlowDataLastActiveTime_Type()
)
flowDataLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataLastActiveTime.setStatus("current")


class _FlowDataSourceSubscriberID_Type(OctetString):
    """Custom type flowDataSourceSubscriberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FlowDataSourceSubscriberID_Type.__name__ = "OctetString"
_FlowDataSourceSubscriberID_Object = MibTableColumn
flowDataSourceSubscriberID = _FlowDataSourceSubscriberID_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 33),
    _FlowDataSourceSubscriberID_Type()
)
flowDataSourceSubscriberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceSubscriberID.setStatus("current")


class _FlowDataDestSubscriberID_Type(OctetString):
    """Custom type flowDataDestSubscriberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FlowDataDestSubscriberID_Type.__name__ = "OctetString"
_FlowDataDestSubscriberID_Object = MibTableColumn
flowDataDestSubscriberID = _FlowDataDestSubscriberID_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 34),
    _FlowDataDestSubscriberID_Type()
)
flowDataDestSubscriberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestSubscriberID.setStatus("current")


class _FlowDataSessionID_Type(OctetString):
    """Custom type flowDataSessionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_FlowDataSessionID_Type.__name__ = "OctetString"
_FlowDataSessionID_Object = MibTableColumn
flowDataSessionID = _FlowDataSessionID_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 35),
    _FlowDataSessionID_Type()
)
flowDataSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSessionID.setStatus("current")


class _FlowDataSourceClass_Type(Integer32):
    """Custom type flowDataSourceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataSourceClass_Type.__name__ = "Integer32"
_FlowDataSourceClass_Object = MibTableColumn
flowDataSourceClass = _FlowDataSourceClass_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 36),
    _FlowDataSourceClass_Type()
)
flowDataSourceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceClass.setStatus("current")


class _FlowDataDestClass_Type(Integer32):
    """Custom type flowDataDestClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataDestClass_Type.__name__ = "Integer32"
_FlowDataDestClass_Object = MibTableColumn
flowDataDestClass = _FlowDataDestClass_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 37),
    _FlowDataDestClass_Type()
)
flowDataDestClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestClass.setStatus("current")


class _FlowDataClass_Type(Integer32):
    """Custom type flowDataClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataClass_Type.__name__ = "Integer32"
_FlowDataClass_Object = MibTableColumn
flowDataClass = _FlowDataClass_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 38),
    _FlowDataClass_Type()
)
flowDataClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataClass.setStatus("current")


class _FlowDataSourceKind_Type(Integer32):
    """Custom type flowDataSourceKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataSourceKind_Type.__name__ = "Integer32"
_FlowDataSourceKind_Object = MibTableColumn
flowDataSourceKind = _FlowDataSourceKind_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 39),
    _FlowDataSourceKind_Type()
)
flowDataSourceKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataSourceKind.setStatus("current")


class _FlowDataDestKind_Type(Integer32):
    """Custom type flowDataDestKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataDestKind_Type.__name__ = "Integer32"
_FlowDataDestKind_Object = MibTableColumn
flowDataDestKind = _FlowDataDestKind_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 40),
    _FlowDataDestKind_Type()
)
flowDataDestKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataDestKind.setStatus("current")


class _FlowDataKind_Type(Integer32):
    """Custom type flowDataKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowDataKind_Type.__name__ = "Integer32"
_FlowDataKind_Object = MibTableColumn
flowDataKind = _FlowDataKind_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 41),
    _FlowDataKind_Type()
)
flowDataKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowDataKind.setStatus("current")
_FlowColumnActivityTable_Object = MibTable
flowColumnActivityTable = _FlowColumnActivityTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2)
)
if mibBuilder.loadTexts:
    flowColumnActivityTable.setStatus("deprecated")
_FlowColumnActivityEntry_Object = MibTableRow
flowColumnActivityEntry = _FlowColumnActivityEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2, 1)
)
flowColumnActivityEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowColumnActivityAttribute"),
    (0, "FLOW-METER-MIB", "flowColumnActivityTime"),
    (0, "FLOW-METER-MIB", "flowColumnActivityIndex"),
)
if mibBuilder.loadTexts:
    flowColumnActivityEntry.setStatus("deprecated")
_FlowColumnActivityAttribute_Type = FlowAttributeNumber
_FlowColumnActivityAttribute_Object = MibTableColumn
flowColumnActivityAttribute = _FlowColumnActivityAttribute_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 1),
    _FlowColumnActivityAttribute_Type()
)
flowColumnActivityAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowColumnActivityAttribute.setStatus("deprecated")
_FlowColumnActivityTime_Type = TimeFilter
_FlowColumnActivityTime_Object = MibTableColumn
flowColumnActivityTime = _FlowColumnActivityTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 2),
    _FlowColumnActivityTime_Type()
)
flowColumnActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowColumnActivityTime.setStatus("deprecated")


class _FlowColumnActivityIndex_Type(Integer32):
    """Custom type flowColumnActivityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowColumnActivityIndex_Type.__name__ = "Integer32"
_FlowColumnActivityIndex_Object = MibTableColumn
flowColumnActivityIndex = _FlowColumnActivityIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 3),
    _FlowColumnActivityIndex_Type()
)
flowColumnActivityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowColumnActivityIndex.setStatus("deprecated")


class _FlowColumnActivityData_Type(OctetString):
    """Custom type flowColumnActivityData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 1000),
    )


_FlowColumnActivityData_Type.__name__ = "OctetString"
_FlowColumnActivityData_Object = MibTableColumn
flowColumnActivityData = _FlowColumnActivityData_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 4),
    _FlowColumnActivityData_Type()
)
flowColumnActivityData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowColumnActivityData.setStatus("deprecated")
_FlowDataPackageTable_Object = MibTable
flowDataPackageTable = _FlowDataPackageTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3)
)
if mibBuilder.loadTexts:
    flowDataPackageTable.setStatus("current")
_FlowDataPackageEntry_Object = MibTableRow
flowDataPackageEntry = _FlowDataPackageEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1)
)
flowDataPackageEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowPackageSelector"),
    (0, "FLOW-METER-MIB", "flowPackageRuleSet"),
    (0, "FLOW-METER-MIB", "flowPackageTime"),
    (0, "FLOW-METER-MIB", "flowPackageIndex"),
)
if mibBuilder.loadTexts:
    flowDataPackageEntry.setStatus("current")
_FlowPackageSelector_Type = OctetString
_FlowPackageSelector_Object = MibTableColumn
flowPackageSelector = _FlowPackageSelector_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 1),
    _FlowPackageSelector_Type()
)
flowPackageSelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowPackageSelector.setStatus("current")


class _FlowPackageRuleSet_Type(Integer32):
    """Custom type flowPackageRuleSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlowPackageRuleSet_Type.__name__ = "Integer32"
_FlowPackageRuleSet_Object = MibTableColumn
flowPackageRuleSet = _FlowPackageRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 2),
    _FlowPackageRuleSet_Type()
)
flowPackageRuleSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowPackageRuleSet.setStatus("current")
_FlowPackageTime_Type = TimeFilter
_FlowPackageTime_Object = MibTableColumn
flowPackageTime = _FlowPackageTime_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 3),
    _FlowPackageTime_Type()
)
flowPackageTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowPackageTime.setStatus("current")


class _FlowPackageIndex_Type(Integer32):
    """Custom type flowPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowPackageIndex_Type.__name__ = "Integer32"
_FlowPackageIndex_Object = MibTableColumn
flowPackageIndex = _FlowPackageIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 4),
    _FlowPackageIndex_Type()
)
flowPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowPackageIndex.setStatus("current")
_FlowPackageData_Type = OctetString
_FlowPackageData_Object = MibTableColumn
flowPackageData = _FlowPackageData_Object(
    (1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 5),
    _FlowPackageData_Type()
)
flowPackageData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPackageData.setStatus("current")
_FlowRules_ObjectIdentity = ObjectIdentity
flowRules = _FlowRules_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 3)
)
_FlowRuleTable_Object = MibTable
flowRuleTable = _FlowRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1)
)
if mibBuilder.loadTexts:
    flowRuleTable.setStatus("current")
_FlowRuleEntry_Object = MibTableRow
flowRuleEntry = _FlowRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1)
)
flowRuleEntry.setIndexNames(
    (0, "FLOW-METER-MIB", "flowRuleSet"),
    (0, "FLOW-METER-MIB", "flowRuleIndex"),
)
if mibBuilder.loadTexts:
    flowRuleEntry.setStatus("current")


class _FlowRuleSet_Type(Integer32):
    """Custom type flowRuleSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowRuleSet_Type.__name__ = "Integer32"
_FlowRuleSet_Object = MibTableColumn
flowRuleSet = _FlowRuleSet_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 1),
    _FlowRuleSet_Type()
)
flowRuleSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowRuleSet.setStatus("current")


class _FlowRuleIndex_Type(Integer32):
    """Custom type flowRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FlowRuleIndex_Type.__name__ = "Integer32"
_FlowRuleIndex_Object = MibTableColumn
flowRuleIndex = _FlowRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 2),
    _FlowRuleIndex_Type()
)
flowRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowRuleIndex.setStatus("current")
_FlowRuleSelector_Type = RuleAttributeNumber
_FlowRuleSelector_Object = MibTableColumn
flowRuleSelector = _FlowRuleSelector_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 3),
    _FlowRuleSelector_Type()
)
flowRuleSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRuleSelector.setStatus("current")
_FlowRuleMask_Type = RuleAddress
_FlowRuleMask_Object = MibTableColumn
flowRuleMask = _FlowRuleMask_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 4),
    _FlowRuleMask_Type()
)
flowRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRuleMask.setStatus("current")
_FlowRuleMatchedValue_Type = RuleAddress
_FlowRuleMatchedValue_Object = MibTableColumn
flowRuleMatchedValue = _FlowRuleMatchedValue_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 5),
    _FlowRuleMatchedValue_Type()
)
flowRuleMatchedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRuleMatchedValue.setStatus("current")
_FlowRuleAction_Type = ActionNumber
_FlowRuleAction_Object = MibTableColumn
flowRuleAction = _FlowRuleAction_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 6),
    _FlowRuleAction_Type()
)
flowRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRuleAction.setStatus("current")


class _FlowRuleParameter_Type(Integer32):
    """Custom type flowRuleParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FlowRuleParameter_Type.__name__ = "Integer32"
_FlowRuleParameter_Object = MibTableColumn
flowRuleParameter = _FlowRuleParameter_Object(
    (1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 7),
    _FlowRuleParameter_Type()
)
flowRuleParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowRuleParameter.setStatus("current")
_FlowMIBConformance_ObjectIdentity = ObjectIdentity
flowMIBConformance = _FlowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 4)
)
_FlowMIBCompliances_ObjectIdentity = ObjectIdentity
flowMIBCompliances = _FlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 4, 1)
)
_FlowMIBGroups_ObjectIdentity = ObjectIdentity
flowMIBGroups = _FlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 40, 4, 2)
)

# Managed Objects groups

flowControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 1)
)
flowControlGroup.setObjects(
      *(("FLOW-METER-MIB", "flowRuleInfoSize"),
        ("FLOW-METER-MIB", "flowRuleInfoOwner"),
        ("FLOW-METER-MIB", "flowRuleInfoTimeStamp"),
        ("FLOW-METER-MIB", "flowRuleInfoStatus"),
        ("FLOW-METER-MIB", "flowRuleInfoName"),
        ("FLOW-METER-MIB", "flowRuleInfoRulesReady"),
        ("FLOW-METER-MIB", "flowRuleInfoFlowRecords"),
        ("FLOW-METER-MIB", "flowInterfaceSampleRate"),
        ("FLOW-METER-MIB", "flowInterfaceLostPackets"),
        ("FLOW-METER-MIB", "flowReaderTimeout"),
        ("FLOW-METER-MIB", "flowReaderOwner"),
        ("FLOW-METER-MIB", "flowReaderLastTime"),
        ("FLOW-METER-MIB", "flowReaderPreviousTime"),
        ("FLOW-METER-MIB", "flowReaderStatus"),
        ("FLOW-METER-MIB", "flowReaderRuleSet"),
        ("FLOW-METER-MIB", "flowManagerCurrentRuleSet"),
        ("FLOW-METER-MIB", "flowManagerStandbyRuleSet"),
        ("FLOW-METER-MIB", "flowManagerHighWaterMark"),
        ("FLOW-METER-MIB", "flowManagerCounterWrap"),
        ("FLOW-METER-MIB", "flowManagerOwner"),
        ("FLOW-METER-MIB", "flowManagerTimeStamp"),
        ("FLOW-METER-MIB", "flowManagerStatus"),
        ("FLOW-METER-MIB", "flowManagerRunningStandby"),
        ("FLOW-METER-MIB", "flowFloodMark"),
        ("FLOW-METER-MIB", "flowInactivityTimeout"),
        ("FLOW-METER-MIB", "flowActiveFlows"),
        ("FLOW-METER-MIB", "flowMaxFlows"),
        ("FLOW-METER-MIB", "flowFloodMode"))
)
if mibBuilder.loadTexts:
    flowControlGroup.setStatus("deprecated")

flowDataTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 2)
)
flowDataTableGroup.setObjects(
      *(("FLOW-METER-MIB", "flowDataStatus"),
        ("FLOW-METER-MIB", "flowDataSourceInterface"),
        ("FLOW-METER-MIB", "flowDataSourceAdjacentType"),
        ("FLOW-METER-MIB", "flowDataSourceAdjacentAddress"),
        ("FLOW-METER-MIB", "flowDataSourceAdjacentMask"),
        ("FLOW-METER-MIB", "flowDataSourcePeerType"),
        ("FLOW-METER-MIB", "flowDataSourcePeerAddress"),
        ("FLOW-METER-MIB", "flowDataSourcePeerMask"),
        ("FLOW-METER-MIB", "flowDataSourceTransType"),
        ("FLOW-METER-MIB", "flowDataSourceTransAddress"),
        ("FLOW-METER-MIB", "flowDataSourceTransMask"),
        ("FLOW-METER-MIB", "flowDataDestInterface"),
        ("FLOW-METER-MIB", "flowDataDestAdjacentType"),
        ("FLOW-METER-MIB", "flowDataDestAdjacentAddress"),
        ("FLOW-METER-MIB", "flowDataDestAdjacentMask"),
        ("FLOW-METER-MIB", "flowDataDestPeerType"),
        ("FLOW-METER-MIB", "flowDataDestPeerAddress"),
        ("FLOW-METER-MIB", "flowDataDestPeerMask"),
        ("FLOW-METER-MIB", "flowDataDestTransType"),
        ("FLOW-METER-MIB", "flowDataDestTransAddress"),
        ("FLOW-METER-MIB", "flowDataDestTransMask"),
        ("FLOW-METER-MIB", "flowDataToOctets"),
        ("FLOW-METER-MIB", "flowDataToPDUs"),
        ("FLOW-METER-MIB", "flowDataFromOctets"),
        ("FLOW-METER-MIB", "flowDataFromPDUs"),
        ("FLOW-METER-MIB", "flowDataFirstTime"),
        ("FLOW-METER-MIB", "flowDataLastActiveTime"),
        ("FLOW-METER-MIB", "flowDataSourceClass"),
        ("FLOW-METER-MIB", "flowDataDestClass"),
        ("FLOW-METER-MIB", "flowDataClass"),
        ("FLOW-METER-MIB", "flowDataSourceKind"),
        ("FLOW-METER-MIB", "flowDataDestKind"),
        ("FLOW-METER-MIB", "flowDataKind"))
)
if mibBuilder.loadTexts:
    flowDataTableGroup.setStatus("deprecated")

flowDataScaleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 3)
)
flowDataScaleGroup.setObjects(
      *(("FLOW-METER-MIB", "flowManagerCounterWrap"),
        ("FLOW-METER-MIB", "flowDataPDUScale"),
        ("FLOW-METER-MIB", "flowDataOctetScale"))
)
if mibBuilder.loadTexts:
    flowDataScaleGroup.setStatus("deprecated")

flowDataSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 4)
)
flowDataSubscriberGroup.setObjects(
      *(("FLOW-METER-MIB", "flowDataSourceSubscriberID"),
        ("FLOW-METER-MIB", "flowDataDestSubscriberID"),
        ("FLOW-METER-MIB", "flowDataSessionID"))
)
if mibBuilder.loadTexts:
    flowDataSubscriberGroup.setStatus("current")

flowDataColumnTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 5)
)
flowDataColumnTableGroup.setObjects(
      *(("FLOW-METER-MIB", "flowColumnActivityAttribute"),
        ("FLOW-METER-MIB", "flowColumnActivityIndex"),
        ("FLOW-METER-MIB", "flowColumnActivityTime"),
        ("FLOW-METER-MIB", "flowColumnActivityData"))
)
if mibBuilder.loadTexts:
    flowDataColumnTableGroup.setStatus("deprecated")

flowDataPackageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 6)
)
flowDataPackageGroup.setObjects(
    ("FLOW-METER-MIB", "flowPackageData")
)
if mibBuilder.loadTexts:
    flowDataPackageGroup.setStatus("current")

flowRuleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 7)
)
flowRuleTableGroup.setObjects(
      *(("FLOW-METER-MIB", "flowRuleSelector"),
        ("FLOW-METER-MIB", "flowRuleMask"),
        ("FLOW-METER-MIB", "flowRuleMatchedValue"),
        ("FLOW-METER-MIB", "flowRuleAction"),
        ("FLOW-METER-MIB", "flowRuleParameter"))
)
if mibBuilder.loadTexts:
    flowRuleTableGroup.setStatus("current")

flowDataScaleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 8)
)
flowDataScaleGroup2.setObjects(
      *(("FLOW-METER-MIB", "flowDataPDUScale"),
        ("FLOW-METER-MIB", "flowDataOctetScale"))
)
if mibBuilder.loadTexts:
    flowDataScaleGroup2.setStatus("current")

flowControlGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 40, 4, 2, 9)
)
flowControlGroup2.setObjects(
      *(("FLOW-METER-MIB", "flowRuleInfoSize"),
        ("FLOW-METER-MIB", "flowRuleInfoOwner"),
        ("FLOW-METER-MIB", "flowRuleInfoTimeStamp"),
        ("FLOW-METER-MIB", "flowRuleInfoStatus"),
        ("FLOW-METER-MIB", "flowRuleInfoName"),
        ("FLOW-METER-MIB", "flowRuleInfoFlowRecords"),
        ("FLOW-METER-MIB", "flowInterfaceSampleRate"),
        ("FLOW-METER-MIB", "flowInterfaceLostPackets"),
        ("FLOW-METER-MIB", "flowReaderTimeout"),
        ("FLOW-METER-MIB", "flowReaderOwner"),
        ("FLOW-METER-MIB", "flowReaderLastTime"),
        ("FLOW-METER-MIB", "flowReaderPreviousTime"),
        ("FLOW-METER-MIB", "flowReaderStatus"),
        ("FLOW-METER-MIB", "flowReaderRuleSet"),
        ("FLOW-METER-MIB", "flowManagerCurrentRuleSet"),
        ("FLOW-METER-MIB", "flowManagerStandbyRuleSet"),
        ("FLOW-METER-MIB", "flowManagerHighWaterMark"),
        ("FLOW-METER-MIB", "flowManagerOwner"),
        ("FLOW-METER-MIB", "flowManagerTimeStamp"),
        ("FLOW-METER-MIB", "flowManagerStatus"),
        ("FLOW-METER-MIB", "flowManagerRunningStandby"),
        ("FLOW-METER-MIB", "flowFloodMark"),
        ("FLOW-METER-MIB", "flowInactivityTimeout"),
        ("FLOW-METER-MIB", "flowActiveFlows"),
        ("FLOW-METER-MIB", "flowMaxFlows"),
        ("FLOW-METER-MIB", "flowFloodMode"))
)
if mibBuilder.loadTexts:
    flowControlGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 40, 4, 1, 1)
)
if mibBuilder.loadTexts:
    flowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FLOW-METER-MIB",
    **{"UTF8OwnerString": UTF8OwnerString,
       "PeerType": PeerType,
       "PeerAddress": PeerAddress,
       "AdjacentType": AdjacentType,
       "AdjacentAddress": AdjacentAddress,
       "TransportType": TransportType,
       "TransportAddress": TransportAddress,
       "RuleAddress": RuleAddress,
       "FlowAttributeNumber": FlowAttributeNumber,
       "RuleAttributeNumber": RuleAttributeNumber,
       "ActionNumber": ActionNumber,
       "flowMIB": flowMIB,
       "flowControl": flowControl,
       "flowRuleSetInfoTable": flowRuleSetInfoTable,
       "flowRuleSetInfoEntry": flowRuleSetInfoEntry,
       "flowRuleInfoIndex": flowRuleInfoIndex,
       "flowRuleInfoSize": flowRuleInfoSize,
       "flowRuleInfoOwner": flowRuleInfoOwner,
       "flowRuleInfoTimeStamp": flowRuleInfoTimeStamp,
       "flowRuleInfoStatus": flowRuleInfoStatus,
       "flowRuleInfoName": flowRuleInfoName,
       "flowRuleInfoRulesReady": flowRuleInfoRulesReady,
       "flowRuleInfoFlowRecords": flowRuleInfoFlowRecords,
       "flowInterfaceTable": flowInterfaceTable,
       "flowInterfaceEntry": flowInterfaceEntry,
       "flowInterfaceSampleRate": flowInterfaceSampleRate,
       "flowInterfaceLostPackets": flowInterfaceLostPackets,
       "flowReaderInfoTable": flowReaderInfoTable,
       "flowReaderInfoEntry": flowReaderInfoEntry,
       "flowReaderIndex": flowReaderIndex,
       "flowReaderTimeout": flowReaderTimeout,
       "flowReaderOwner": flowReaderOwner,
       "flowReaderLastTime": flowReaderLastTime,
       "flowReaderPreviousTime": flowReaderPreviousTime,
       "flowReaderStatus": flowReaderStatus,
       "flowReaderRuleSet": flowReaderRuleSet,
       "flowManagerInfoTable": flowManagerInfoTable,
       "flowManagerInfoEntry": flowManagerInfoEntry,
       "flowManagerIndex": flowManagerIndex,
       "flowManagerCurrentRuleSet": flowManagerCurrentRuleSet,
       "flowManagerStandbyRuleSet": flowManagerStandbyRuleSet,
       "flowManagerHighWaterMark": flowManagerHighWaterMark,
       "flowManagerCounterWrap": flowManagerCounterWrap,
       "flowManagerOwner": flowManagerOwner,
       "flowManagerTimeStamp": flowManagerTimeStamp,
       "flowManagerStatus": flowManagerStatus,
       "flowManagerRunningStandby": flowManagerRunningStandby,
       "flowFloodMark": flowFloodMark,
       "flowInactivityTimeout": flowInactivityTimeout,
       "flowActiveFlows": flowActiveFlows,
       "flowMaxFlows": flowMaxFlows,
       "flowFloodMode": flowFloodMode,
       "flowData": flowData,
       "flowDataTable": flowDataTable,
       "flowDataEntry": flowDataEntry,
       "flowDataIndex": flowDataIndex,
       "flowDataTimeMark": flowDataTimeMark,
       "flowDataStatus": flowDataStatus,
       "flowDataSourceInterface": flowDataSourceInterface,
       "flowDataSourceAdjacentType": flowDataSourceAdjacentType,
       "flowDataSourceAdjacentAddress": flowDataSourceAdjacentAddress,
       "flowDataSourceAdjacentMask": flowDataSourceAdjacentMask,
       "flowDataSourcePeerType": flowDataSourcePeerType,
       "flowDataSourcePeerAddress": flowDataSourcePeerAddress,
       "flowDataSourcePeerMask": flowDataSourcePeerMask,
       "flowDataSourceTransType": flowDataSourceTransType,
       "flowDataSourceTransAddress": flowDataSourceTransAddress,
       "flowDataSourceTransMask": flowDataSourceTransMask,
       "flowDataDestInterface": flowDataDestInterface,
       "flowDataDestAdjacentType": flowDataDestAdjacentType,
       "flowDataDestAdjacentAddress": flowDataDestAdjacentAddress,
       "flowDataDestAdjacentMask": flowDataDestAdjacentMask,
       "flowDataDestPeerType": flowDataDestPeerType,
       "flowDataDestPeerAddress": flowDataDestPeerAddress,
       "flowDataDestPeerMask": flowDataDestPeerMask,
       "flowDataDestTransType": flowDataDestTransType,
       "flowDataDestTransAddress": flowDataDestTransAddress,
       "flowDataDestTransMask": flowDataDestTransMask,
       "flowDataPDUScale": flowDataPDUScale,
       "flowDataOctetScale": flowDataOctetScale,
       "flowDataRuleSet": flowDataRuleSet,
       "flowDataToOctets": flowDataToOctets,
       "flowDataToPDUs": flowDataToPDUs,
       "flowDataFromOctets": flowDataFromOctets,
       "flowDataFromPDUs": flowDataFromPDUs,
       "flowDataFirstTime": flowDataFirstTime,
       "flowDataLastActiveTime": flowDataLastActiveTime,
       "flowDataSourceSubscriberID": flowDataSourceSubscriberID,
       "flowDataDestSubscriberID": flowDataDestSubscriberID,
       "flowDataSessionID": flowDataSessionID,
       "flowDataSourceClass": flowDataSourceClass,
       "flowDataDestClass": flowDataDestClass,
       "flowDataClass": flowDataClass,
       "flowDataSourceKind": flowDataSourceKind,
       "flowDataDestKind": flowDataDestKind,
       "flowDataKind": flowDataKind,
       "flowColumnActivityTable": flowColumnActivityTable,
       "flowColumnActivityEntry": flowColumnActivityEntry,
       "flowColumnActivityAttribute": flowColumnActivityAttribute,
       "flowColumnActivityTime": flowColumnActivityTime,
       "flowColumnActivityIndex": flowColumnActivityIndex,
       "flowColumnActivityData": flowColumnActivityData,
       "flowDataPackageTable": flowDataPackageTable,
       "flowDataPackageEntry": flowDataPackageEntry,
       "flowPackageSelector": flowPackageSelector,
       "flowPackageRuleSet": flowPackageRuleSet,
       "flowPackageTime": flowPackageTime,
       "flowPackageIndex": flowPackageIndex,
       "flowPackageData": flowPackageData,
       "flowRules": flowRules,
       "flowRuleTable": flowRuleTable,
       "flowRuleEntry": flowRuleEntry,
       "flowRuleSet": flowRuleSet,
       "flowRuleIndex": flowRuleIndex,
       "flowRuleSelector": flowRuleSelector,
       "flowRuleMask": flowRuleMask,
       "flowRuleMatchedValue": flowRuleMatchedValue,
       "flowRuleAction": flowRuleAction,
       "flowRuleParameter": flowRuleParameter,
       "flowMIBConformance": flowMIBConformance,
       "flowMIBCompliances": flowMIBCompliances,
       "flowMIBCompliance": flowMIBCompliance,
       "flowMIBGroups": flowMIBGroups,
       "flowControlGroup": flowControlGroup,
       "flowDataTableGroup": flowDataTableGroup,
       "flowDataScaleGroup": flowDataScaleGroup,
       "flowDataSubscriberGroup": flowDataSubscriberGroup,
       "flowDataColumnTableGroup": flowDataColumnTableGroup,
       "flowDataPackageGroup": flowDataPackageGroup,
       "flowRuleTableGroup": flowRuleTableGroup,
       "flowDataScaleGroup2": flowDataScaleGroup2,
       "flowControlGroup2": flowControlGroup2}
)
