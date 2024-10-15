# SNMP MIB module (PACKET-VX-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKET-VX-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:01 2024
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

(condCodeType,
 condDateAndTime,
 condDescription,
 condObjectType,
 condReportType,
 condServiceAffecting,
 condSeverity,
 erpsCondNotifications,
 eventNotifications,
 evtCodeType,
 evtDateAndTime,
 evtDescription,
 evtObjectType,
 lagCondNotifications,
 mstpCondNotifications,
 mstpEvtNotifications,
 mstpNotificationObjects,
 performance,
 pvxBridge,
 pvxERPSSrvcEvtNotifications,
 pvxERPSSrvcNNIEvtNotifications,
 pvxESrvcBWPrflEvtNotifications,
 pvxESrvcEvtNotifications,
 pvxL2IntfPortIdx,
 pvxL2IntfPortTypeIdx,
 pvxL2IntfShelfIdx,
 pvxL2IntfSlotIdx,
 pvxL2IntfSubPortNumber,
 pvxL2IntfSwitchIdx,
 pvxObjects,
 pvxSUniEvtNotifications,
 pvxSlaMsmtEvtNotifications,
 swMemberCondNotifications,
 tcaDateAndTime,
 tcaMontype,
 tcaThreshold,
 tcaValue,
 trapSeqNum) = mibBuilder.importSymbols(
    "BTI-7000-MIB",
    "condCodeType",
    "condDateAndTime",
    "condDescription",
    "condObjectType",
    "condReportType",
    "condServiceAffecting",
    "condSeverity",
    "erpsCondNotifications",
    "eventNotifications",
    "evtCodeType",
    "evtDateAndTime",
    "evtDescription",
    "evtObjectType",
    "lagCondNotifications",
    "mstpCondNotifications",
    "mstpEvtNotifications",
    "mstpNotificationObjects",
    "performance",
    "pvxBridge",
    "pvxERPSSrvcEvtNotifications",
    "pvxERPSSrvcNNIEvtNotifications",
    "pvxESrvcBWPrflEvtNotifications",
    "pvxESrvcEvtNotifications",
    "pvxL2IntfPortIdx",
    "pvxL2IntfPortTypeIdx",
    "pvxL2IntfShelfIdx",
    "pvxL2IntfSlotIdx",
    "pvxL2IntfSubPortNumber",
    "pvxL2IntfSwitchIdx",
    "pvxObjects",
    "pvxSUniEvtNotifications",
    "pvxSlaMsmtEvtNotifications",
    "swMemberCondNotifications",
    "tcaDateAndTime",
    "tcaMontype",
    "tcaThreshold",
    "tcaValue",
    "trapSeqNum")

(btiModules,) = mibBuilder.importSymbols(
    "BTI-MIB",
    "btiModules")

(AdminStatus,
 CirTestResult,
 CommandStateType,
 CondReportType,
 CondServiceAffecting,
 CondSeverity,
 FixedX100,
 FixedX1000,
 InetAddress,
 InetAddressType,
 InitializeCmd,
 MirrorConfigType,
 MonitorPeriodType,
 OperStatus,
 PMIntervalType,
 PMValidity,
 PmTestCmdState,
 ProfileNameType,
 ProtocolActionType,
 PvxPortType,
 SlaTestRole,
 SwitchIdxType,
 Unsigned64) = mibBuilder.importSymbols(
    "BTI-TC-MIB",
    "AdminStatus",
    "CirTestResult",
    "CommandStateType",
    "CondReportType",
    "CondServiceAffecting",
    "CondSeverity",
    "FixedX100",
    "FixedX1000",
    "InetAddress",
    "InetAddressType",
    "InitializeCmd",
    "MirrorConfigType",
    "MonitorPeriodType",
    "OperStatus",
    "PMIntervalType",
    "PMValidity",
    "PmTestCmdState",
    "ProfileNameType",
    "ProtocolActionType",
    "PvxPortType",
    "SlaTestRole",
    "SwitchIdxType",
    "Unsigned64")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

packetVxBridgeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 1, 5)
)
packetVxBridgeMib.setRevisions(
        ("2013-04-03 12:00",
         "2012-12-20 12:00",
         "2012-12-06 12:00",
         "2012-06-20 12:00",
         "2012-02-10 12:00",
         "2011-06-23 12:00",
         "2010-08-06 12:00",
         "2010-06-18 12:00",
         "2010-02-12 12:00",
         "2008-12-19 12:00",
         "2008-03-10 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PvxPhyPort(DisplayString, TextualConvention):
    status = "current"


class PvxPhyPortList(DisplayString, TextualConvention):
    status = "current"


class PvxL2PortList(DisplayString, TextualConvention):
    status = "current"


class PvxVLANPortList(DisplayString, TextualConvention):
    status = "current"


class PvxL2Port(DisplayString, TextualConvention):
    status = "current"


class PvxVlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class PvxMSTPVlanList(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class PvxPCPDecodingList(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("prioirty7-DE", 2),
          ("priority0", 15),
          ("priority0-DE", 16),
          ("priority1", 13),
          ("priority1-DE", 14),
          ("priority2", 11),
          ("priority2-DE", 12),
          ("priority3", 9),
          ("priority3-DE", 10),
          ("priority4", 7),
          ("priority4-DE", 8),
          ("priority5", 5),
          ("priority5-DE", 6),
          ("priority6", 3),
          ("priority6-DE", 4),
          ("priority7", 1))
    )



class PvxPolicyDropAction(Integer32, TextualConvention):
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
        *(("doNotDrop", 2),
          ("drop", 1),
          ("notDefined", 3))
    )



class PvxQoSColorMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )



class PvxQoSPmCounterMode(Integer32, TextualConvention):
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
        *(("count-cnfrm", 2),
          ("count-cnfrmAndExceed", 3),
          ("count-violate", 1),
          ("count-violateAndExceec", 4),
          ("notUsed", 5))
    )



class PvxCVidMapOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notProgrammed", 2),
          ("programmed", 1))
    )



class PvxEcfmTransmitStatus(Integer32, TextualConvention):
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
        *(("notReady", 2),
          ("ready", 1),
          ("transmit", 3))
    )



class PvxEcfmMepDefects(Bits, TextualConvention):
    status = "current"


class PvxY1731MepDefects(Bits, TextualConvention):
    status = "current"


class PvxEcfmRemoteMepState(Integer32, TextualConvention):
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
        *(("rMepFailed", 3),
          ("rMepIdle", 1),
          ("rMepOk", 4),
          ("rMepStart", 2))
    )



class PvxEcfmConfigErrors(Bits, TextualConvention):
    status = "current"


class PvxEcfmRelayActionFieldValue(Integer32, TextualConvention):
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
        *(("rlyFdb", 2),
          ("rlyHit", 1),
          ("rlyMpdb", 3))
    )



class PvxEcfmIngressActionFieldValue(Integer32, TextualConvention):
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
        *(("ingBlocked", 3),
          ("ingDown", 2),
          ("ingOk", 1),
          ("ingVid", 4))
    )



class PvxEcfmEgressActionFieldValue(Integer32, TextualConvention):
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
        *(("egrBlocked", 3),
          ("egrDown", 2),
          ("egrOK", 1),
          ("egrVid", 4))
    )



class PvxErpsVirtualLinkList(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class PvxESrvcBWPrflPMThresholdLevelType(Integer32, TextualConvention):
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
        *(("day1CIR", 3),
          ("day1EIR", 4),
          ("min15CIR", 1),
          ("min15EIR", 2))
    )



class PvxStackingPortCommState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectionOk", 2),
          ("noConnection", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PvxMSTPCrntPMTable_Object = MibTable
pvxMSTPCrntPMTable = _PvxMSTPCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32)
)
if mibBuilder.loadTexts:
    pvxMSTPCrntPMTable.setStatus("current")
_PvxMSTPCrntPMEntry_Object = MibTableRow
pvxMSTPCrntPMEntry = _PvxMSTPCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1)
)
pvxMSTPCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPCrntPMXstIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPCrntPMEntry.setStatus("current")


class _PvxMSTPCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPCrntPMSwitchIdx_Object = MibTableColumn
pvxMSTPCrntPMSwitchIdx = _PvxMSTPCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 1),
    _PvxMSTPCrntPMSwitchIdx_Type()
)
pvxMSTPCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMSwitchIdx.setStatus("current")


class _PvxMSTPCrntPMXstIdx_Type(Integer32):
    """Custom type pvxMSTPCrntPMXstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxMSTPCrntPMXstIdx_Type.__name__ = "Integer32"
_PvxMSTPCrntPMXstIdx_Object = MibTableColumn
pvxMSTPCrntPMXstIdx = _PvxMSTPCrntPMXstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 2),
    _PvxMSTPCrntPMXstIdx_Type()
)
pvxMSTPCrntPMXstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMXstIdx.setStatus("current")
_PvxMSTPCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxMSTPCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxMSTPCrntPMIntervalTypeIdx = _PvxMSTPCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 3),
    _PvxMSTPCrntPMIntervalTypeIdx_Type()
)
pvxMSTPCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMIntervalTypeIdx.setStatus("current")
_PvxMSTPCrntPMRCCCValue_Type = Unsigned64
_PvxMSTPCrntPMRCCCValue_Object = MibTableColumn
pvxMSTPCrntPMRCCCValue = _PvxMSTPCrntPMRCCCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 4),
    _PvxMSTPCrntPMRCCCValue_Type()
)
pvxMSTPCrntPMRCCCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMRCCCValue.setStatus("current")
_PvxMSTPCrntPMRCCCTimeStamp_Type = DateAndTime
_PvxMSTPCrntPMRCCCTimeStamp_Object = MibTableColumn
pvxMSTPCrntPMRCCCTimeStamp = _PvxMSTPCrntPMRCCCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 5),
    _PvxMSTPCrntPMRCCCTimeStamp_Type()
)
pvxMSTPCrntPMRCCCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMRCCCTimeStamp.setStatus("current")
_PvxMSTPCrntPMRCCCValidity_Type = PMValidity
_PvxMSTPCrntPMRCCCValidity_Object = MibTableColumn
pvxMSTPCrntPMRCCCValidity = _PvxMSTPCrntPMRCCCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 6),
    _PvxMSTPCrntPMRCCCValidity_Type()
)
pvxMSTPCrntPMRCCCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMRCCCValidity.setStatus("current")
_PvxMSTPCrntPMRCCCInitialize_Type = InitializeCmd
_PvxMSTPCrntPMRCCCInitialize_Object = MibTableColumn
pvxMSTPCrntPMRCCCInitialize = _PvxMSTPCrntPMRCCCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 7),
    _PvxMSTPCrntPMRCCCInitialize_Type()
)
pvxMSTPCrntPMRCCCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMRCCCInitialize.setStatus("current")
_PvxMSTPCrntPMTCCValue_Type = Unsigned64
_PvxMSTPCrntPMTCCValue_Object = MibTableColumn
pvxMSTPCrntPMTCCValue = _PvxMSTPCrntPMTCCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 8),
    _PvxMSTPCrntPMTCCValue_Type()
)
pvxMSTPCrntPMTCCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMTCCValue.setStatus("current")
_PvxMSTPCrntPMTCCTimeStamp_Type = DateAndTime
_PvxMSTPCrntPMTCCTimeStamp_Object = MibTableColumn
pvxMSTPCrntPMTCCTimeStamp = _PvxMSTPCrntPMTCCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 9),
    _PvxMSTPCrntPMTCCTimeStamp_Type()
)
pvxMSTPCrntPMTCCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMTCCTimeStamp.setStatus("current")
_PvxMSTPCrntPMTCCValidity_Type = PMValidity
_PvxMSTPCrntPMTCCValidity_Object = MibTableColumn
pvxMSTPCrntPMTCCValidity = _PvxMSTPCrntPMTCCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 10),
    _PvxMSTPCrntPMTCCValidity_Type()
)
pvxMSTPCrntPMTCCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMTCCValidity.setStatus("current")
_PvxMSTPCrntPMTCCInitialize_Type = InitializeCmd
_PvxMSTPCrntPMTCCInitialize_Object = MibTableColumn
pvxMSTPCrntPMTCCInitialize = _PvxMSTPCrntPMTCCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 11),
    _PvxMSTPCrntPMTCCInitialize_Type()
)
pvxMSTPCrntPMTCCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMTCCInitialize.setStatus("current")
_PvxMSTPCrntPMNRBCValue_Type = Unsigned64
_PvxMSTPCrntPMNRBCValue_Object = MibTableColumn
pvxMSTPCrntPMNRBCValue = _PvxMSTPCrntPMNRBCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 12),
    _PvxMSTPCrntPMNRBCValue_Type()
)
pvxMSTPCrntPMNRBCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMNRBCValue.setStatus("current")
_PvxMSTPCrntPMNRBCTimeStamp_Type = DateAndTime
_PvxMSTPCrntPMNRBCTimeStamp_Object = MibTableColumn
pvxMSTPCrntPMNRBCTimeStamp = _PvxMSTPCrntPMNRBCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 13),
    _PvxMSTPCrntPMNRBCTimeStamp_Type()
)
pvxMSTPCrntPMNRBCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMNRBCTimeStamp.setStatus("current")
_PvxMSTPCrntPMNRBCValidity_Type = PMValidity
_PvxMSTPCrntPMNRBCValidity_Object = MibTableColumn
pvxMSTPCrntPMNRBCValidity = _PvxMSTPCrntPMNRBCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 14),
    _PvxMSTPCrntPMNRBCValidity_Type()
)
pvxMSTPCrntPMNRBCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMNRBCValidity.setStatus("current")
_PvxMSTPCrntPMNRBCInitialize_Type = InitializeCmd
_PvxMSTPCrntPMNRBCInitialize_Object = MibTableColumn
pvxMSTPCrntPMNRBCInitialize = _PvxMSTPCrntPMNRBCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 32, 1, 15),
    _PvxMSTPCrntPMNRBCInitialize_Type()
)
pvxMSTPCrntPMNRBCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPCrntPMNRBCInitialize.setStatus("current")
_PvxMSTPHistPMTable_Object = MibTable
pvxMSTPHistPMTable = _PvxMSTPHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33)
)
if mibBuilder.loadTexts:
    pvxMSTPHistPMTable.setStatus("current")
_PvxMSTPHistPMEntry_Object = MibTableRow
pvxMSTPHistPMEntry = _PvxMSTPHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1)
)
pvxMSTPHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPHistPMXstIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPHistPMEntry.setStatus("current")


class _PvxMSTPHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPHistPMSwitchIdx_Object = MibTableColumn
pvxMSTPHistPMSwitchIdx = _PvxMSTPHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 1),
    _PvxMSTPHistPMSwitchIdx_Type()
)
pvxMSTPHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPHistPMSwitchIdx.setStatus("current")


class _PvxMSTPHistPMXstIdx_Type(Integer32):
    """Custom type pvxMSTPHistPMXstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxMSTPHistPMXstIdx_Type.__name__ = "Integer32"
_PvxMSTPHistPMXstIdx_Object = MibTableColumn
pvxMSTPHistPMXstIdx = _PvxMSTPHistPMXstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 2),
    _PvxMSTPHistPMXstIdx_Type()
)
pvxMSTPHistPMXstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPHistPMXstIdx.setStatus("current")
_PvxMSTPHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxMSTPHistPMIntervalTypeIdx_Object = MibTableColumn
pvxMSTPHistPMIntervalTypeIdx = _PvxMSTPHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 3),
    _PvxMSTPHistPMIntervalTypeIdx_Type()
)
pvxMSTPHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPHistPMIntervalTypeIdx.setStatus("current")


class _PvxMSTPHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxMSTPHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxMSTPHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxMSTPHistPMIntervalIdx_Object = MibTableColumn
pvxMSTPHistPMIntervalIdx = _PvxMSTPHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 4),
    _PvxMSTPHistPMIntervalIdx_Type()
)
pvxMSTPHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPHistPMIntervalIdx.setStatus("current")
_PvxMSTPHistPMRCCCValue_Type = Unsigned64
_PvxMSTPHistPMRCCCValue_Object = MibTableColumn
pvxMSTPHistPMRCCCValue = _PvxMSTPHistPMRCCCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 5),
    _PvxMSTPHistPMRCCCValue_Type()
)
pvxMSTPHistPMRCCCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMRCCCValue.setStatus("current")
_PvxMSTPHistPMRCCCTimeStamp_Type = DateAndTime
_PvxMSTPHistPMRCCCTimeStamp_Object = MibTableColumn
pvxMSTPHistPMRCCCTimeStamp = _PvxMSTPHistPMRCCCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 6),
    _PvxMSTPHistPMRCCCTimeStamp_Type()
)
pvxMSTPHistPMRCCCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMRCCCTimeStamp.setStatus("current")
_PvxMSTPHistPMRCCCValidity_Type = PMValidity
_PvxMSTPHistPMRCCCValidity_Object = MibTableColumn
pvxMSTPHistPMRCCCValidity = _PvxMSTPHistPMRCCCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 7),
    _PvxMSTPHistPMRCCCValidity_Type()
)
pvxMSTPHistPMRCCCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMRCCCValidity.setStatus("current")
_PvxMSTPHistPMRCCCInitialize_Type = InitializeCmd
_PvxMSTPHistPMRCCCInitialize_Object = MibTableColumn
pvxMSTPHistPMRCCCInitialize = _PvxMSTPHistPMRCCCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 8),
    _PvxMSTPHistPMRCCCInitialize_Type()
)
pvxMSTPHistPMRCCCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPHistPMRCCCInitialize.setStatus("current")
_PvxMSTPHistPMTCCValue_Type = Unsigned64
_PvxMSTPHistPMTCCValue_Object = MibTableColumn
pvxMSTPHistPMTCCValue = _PvxMSTPHistPMTCCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 9),
    _PvxMSTPHistPMTCCValue_Type()
)
pvxMSTPHistPMTCCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMTCCValue.setStatus("current")
_PvxMSTPHistPMTCCTimeStamp_Type = DateAndTime
_PvxMSTPHistPMTCCTimeStamp_Object = MibTableColumn
pvxMSTPHistPMTCCTimeStamp = _PvxMSTPHistPMTCCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 10),
    _PvxMSTPHistPMTCCTimeStamp_Type()
)
pvxMSTPHistPMTCCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMTCCTimeStamp.setStatus("current")
_PvxMSTPHistPMTCCValidity_Type = PMValidity
_PvxMSTPHistPMTCCValidity_Object = MibTableColumn
pvxMSTPHistPMTCCValidity = _PvxMSTPHistPMTCCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 11),
    _PvxMSTPHistPMTCCValidity_Type()
)
pvxMSTPHistPMTCCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMTCCValidity.setStatus("current")
_PvxMSTPHistPMTCCInitialize_Type = InitializeCmd
_PvxMSTPHistPMTCCInitialize_Object = MibTableColumn
pvxMSTPHistPMTCCInitialize = _PvxMSTPHistPMTCCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 12),
    _PvxMSTPHistPMTCCInitialize_Type()
)
pvxMSTPHistPMTCCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPHistPMTCCInitialize.setStatus("current")
_PvxMSTPHistPMNRBCValue_Type = Unsigned64
_PvxMSTPHistPMNRBCValue_Object = MibTableColumn
pvxMSTPHistPMNRBCValue = _PvxMSTPHistPMNRBCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 13),
    _PvxMSTPHistPMNRBCValue_Type()
)
pvxMSTPHistPMNRBCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMNRBCValue.setStatus("current")
_PvxMSTPHistPMNRBCTimeStamp_Type = DateAndTime
_PvxMSTPHistPMNRBCTimeStamp_Object = MibTableColumn
pvxMSTPHistPMNRBCTimeStamp = _PvxMSTPHistPMNRBCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 14),
    _PvxMSTPHistPMNRBCTimeStamp_Type()
)
pvxMSTPHistPMNRBCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMNRBCTimeStamp.setStatus("current")
_PvxMSTPHistPMNRBCValidity_Type = PMValidity
_PvxMSTPHistPMNRBCValidity_Object = MibTableColumn
pvxMSTPHistPMNRBCValidity = _PvxMSTPHistPMNRBCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 15),
    _PvxMSTPHistPMNRBCValidity_Type()
)
pvxMSTPHistPMNRBCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPHistPMNRBCValidity.setStatus("current")
_PvxMSTPHistPMNRBCInitialize_Type = InitializeCmd
_PvxMSTPHistPMNRBCInitialize_Object = MibTableColumn
pvxMSTPHistPMNRBCInitialize = _PvxMSTPHistPMNRBCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 33, 1, 16),
    _PvxMSTPHistPMNRBCInitialize_Type()
)
pvxMSTPHistPMNRBCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPHistPMNRBCInitialize.setStatus("current")
_PvxMSTPPortCrntPMTable_Object = MibTable
pvxMSTPPortCrntPMTable = _PvxMSTPPortCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34)
)
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMTable.setStatus("current")
_PvxMSTPPortCrntPMEntry_Object = MibTableRow
pvxMSTPPortCrntPMEntry = _PvxMSTPPortCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1)
)
pvxMSTPPortCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMXstIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMEntry.setStatus("current")


class _PvxMSTPPortCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPPortCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPPortCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPPortCrntPMSwitchIdx_Object = MibTableColumn
pvxMSTPPortCrntPMSwitchIdx = _PvxMSTPPortCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 1),
    _PvxMSTPPortCrntPMSwitchIdx_Type()
)
pvxMSTPPortCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMSwitchIdx.setStatus("current")


class _PvxMSTPPortCrntPMShelfIdx_Type(Integer32):
    """Custom type pvxMSTPPortCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxMSTPPortCrntPMShelfIdx_Type.__name__ = "Integer32"
_PvxMSTPPortCrntPMShelfIdx_Object = MibTableColumn
pvxMSTPPortCrntPMShelfIdx = _PvxMSTPPortCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 2),
    _PvxMSTPPortCrntPMShelfIdx_Type()
)
pvxMSTPPortCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMShelfIdx.setStatus("current")


class _PvxMSTPPortCrntPMSlotIdx_Type(Integer32):
    """Custom type pvxMSTPPortCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxMSTPPortCrntPMSlotIdx_Type.__name__ = "Integer32"
_PvxMSTPPortCrntPMSlotIdx_Object = MibTableColumn
pvxMSTPPortCrntPMSlotIdx = _PvxMSTPPortCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 3),
    _PvxMSTPPortCrntPMSlotIdx_Type()
)
pvxMSTPPortCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMSlotIdx.setStatus("current")
_PvxMSTPPortCrntPMTypeIdx_Type = PvxPortType
_PvxMSTPPortCrntPMTypeIdx_Object = MibTableColumn
pvxMSTPPortCrntPMTypeIdx = _PvxMSTPPortCrntPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 4),
    _PvxMSTPPortCrntPMTypeIdx_Type()
)
pvxMSTPPortCrntPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMTypeIdx.setStatus("current")


class _PvxMSTPPortCrntPMXstIdx_Type(Integer32):
    """Custom type pvxMSTPPortCrntPMXstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxMSTPPortCrntPMXstIdx_Type.__name__ = "Integer32"
_PvxMSTPPortCrntPMXstIdx_Object = MibTableColumn
pvxMSTPPortCrntPMXstIdx = _PvxMSTPPortCrntPMXstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 5),
    _PvxMSTPPortCrntPMXstIdx_Type()
)
pvxMSTPPortCrntPMXstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMXstIdx.setStatus("current")


class _PvxMSTPPortCrntPMIdx_Type(Integer32):
    """Custom type pvxMSTPPortCrntPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxMSTPPortCrntPMIdx_Type.__name__ = "Integer32"
_PvxMSTPPortCrntPMIdx_Object = MibTableColumn
pvxMSTPPortCrntPMIdx = _PvxMSTPPortCrntPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 6),
    _PvxMSTPPortCrntPMIdx_Type()
)
pvxMSTPPortCrntPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMIdx.setStatus("current")
_PvxMSTPPortCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxMSTPPortCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxMSTPPortCrntPMIntervalTypeIdx = _PvxMSTPPortCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 7),
    _PvxMSTPPortCrntPMIntervalTypeIdx_Type()
)
pvxMSTPPortCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMIntervalTypeIdx.setStatus("current")
_PvxMSTPPortCrntPMFWDTRValue_Type = Unsigned64
_PvxMSTPPortCrntPMFWDTRValue_Object = MibTableColumn
pvxMSTPPortCrntPMFWDTRValue = _PvxMSTPPortCrntPMFWDTRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 8),
    _PvxMSTPPortCrntPMFWDTRValue_Type()
)
pvxMSTPPortCrntPMFWDTRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMFWDTRValue.setStatus("current")
_PvxMSTPPortCrntPMFWDTRTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMFWDTRTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMFWDTRTimeStamp = _PvxMSTPPortCrntPMFWDTRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 9),
    _PvxMSTPPortCrntPMFWDTRTimeStamp_Type()
)
pvxMSTPPortCrntPMFWDTRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMFWDTRTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMFWDTRValidity_Type = PMValidity
_PvxMSTPPortCrntPMFWDTRValidity_Object = MibTableColumn
pvxMSTPPortCrntPMFWDTRValidity = _PvxMSTPPortCrntPMFWDTRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 10),
    _PvxMSTPPortCrntPMFWDTRValidity_Type()
)
pvxMSTPPortCrntPMFWDTRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMFWDTRValidity.setStatus("current")
_PvxMSTPPortCrntPMFWDTRInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMFWDTRInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMFWDTRInitialize = _PvxMSTPPortCrntPMFWDTRInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 11),
    _PvxMSTPPortCrntPMFWDTRInitialize_Type()
)
pvxMSTPPortCrntPMFWDTRInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMFWDTRInitialize.setStatus("current")
_PvxMSTPPortCrntPMPMCValue_Type = Unsigned64
_PvxMSTPPortCrntPMPMCValue_Object = MibTableColumn
pvxMSTPPortCrntPMPMCValue = _PvxMSTPPortCrntPMPMCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 12),
    _PvxMSTPPortCrntPMPMCValue_Type()
)
pvxMSTPPortCrntPMPMCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMPMCValue.setStatus("current")
_PvxMSTPPortCrntPMPMCTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMPMCTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMPMCTimeStamp = _PvxMSTPPortCrntPMPMCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 13),
    _PvxMSTPPortCrntPMPMCTimeStamp_Type()
)
pvxMSTPPortCrntPMPMCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMPMCTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMPMCValidity_Type = PMValidity
_PvxMSTPPortCrntPMPMCValidity_Object = MibTableColumn
pvxMSTPPortCrntPMPMCValidity = _PvxMSTPPortCrntPMPMCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 14),
    _PvxMSTPPortCrntPMPMCValidity_Type()
)
pvxMSTPPortCrntPMPMCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMPMCValidity.setStatus("current")
_PvxMSTPPortCrntPMPMCInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMPMCInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMPMCInitialize = _PvxMSTPPortCrntPMPMCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 15),
    _PvxMSTPPortCrntPMPMCInitialize_Type()
)
pvxMSTPPortCrntPMPMCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMPMCInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDURXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDURXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDURXValue = _PvxMSTPPortCrntPMBPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 16),
    _PvxMSTPPortCrntPMBPDURXValue_Type()
)
pvxMSTPPortCrntPMBPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDURXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDURXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDURXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDURXTimeStamp = _PvxMSTPPortCrntPMBPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 17),
    _PvxMSTPPortCrntPMBPDURXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDURXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDURXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDURXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDURXValidity = _PvxMSTPPortCrntPMBPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 18),
    _PvxMSTPPortCrntPMBPDURXValidity_Type()
)
pvxMSTPPortCrntPMBPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDURXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDURXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDURXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDURXInitialize = _PvxMSTPPortCrntPMBPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 19),
    _PvxMSTPPortCrntPMBPDURXInitialize_Type()
)
pvxMSTPPortCrntPMBPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDURXInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDUTXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDUTXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTXValue = _PvxMSTPPortCrntPMBPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 20),
    _PvxMSTPPortCrntPMBPDUTXValue_Type()
)
pvxMSTPPortCrntPMBPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDUTXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDUTXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTXTimeStamp = _PvxMSTPPortCrntPMBPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 21),
    _PvxMSTPPortCrntPMBPDUTXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDUTXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDUTXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTXValidity = _PvxMSTPPortCrntPMBPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 22),
    _PvxMSTPPortCrntPMBPDUTXValidity_Type()
)
pvxMSTPPortCrntPMBPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDUTXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDUTXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTXInitialize = _PvxMSTPPortCrntPMBPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 23),
    _PvxMSTPPortCrntPMBPDUTXInitialize_Type()
)
pvxMSTPPortCrntPMBPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTXInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGRXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDUCFGRXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGRXValue = _PvxMSTPPortCrntPMBPDUCFGRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 24),
    _PvxMSTPPortCrntPMBPDUCFGRXValue_Type()
)
pvxMSTPPortCrntPMBPDUCFGRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGRXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGRXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDUCFGRXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGRXTimeStamp = _PvxMSTPPortCrntPMBPDUCFGRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 25),
    _PvxMSTPPortCrntPMBPDUCFGRXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDUCFGRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGRXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGRXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDUCFGRXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGRXValidity = _PvxMSTPPortCrntPMBPDUCFGRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 26),
    _PvxMSTPPortCrntPMBPDUCFGRXValidity_Type()
)
pvxMSTPPortCrntPMBPDUCFGRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGRXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGRXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDUCFGRXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGRXInitialize = _PvxMSTPPortCrntPMBPDUCFGRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 27),
    _PvxMSTPPortCrntPMBPDUCFGRXInitialize_Type()
)
pvxMSTPPortCrntPMBPDUCFGRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGRXInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGTXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDUCFGTXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGTXValue = _PvxMSTPPortCrntPMBPDUCFGTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 28),
    _PvxMSTPPortCrntPMBPDUCFGTXValue_Type()
)
pvxMSTPPortCrntPMBPDUCFGTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGTXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGTXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDUCFGTXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGTXTimeStamp = _PvxMSTPPortCrntPMBPDUCFGTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 29),
    _PvxMSTPPortCrntPMBPDUCFGTXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDUCFGTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGTXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGTXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDUCFGTXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGTXValidity = _PvxMSTPPortCrntPMBPDUCFGTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 30),
    _PvxMSTPPortCrntPMBPDUCFGTXValidity_Type()
)
pvxMSTPPortCrntPMBPDUCFGTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGTXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDUCFGTXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDUCFGTXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUCFGTXInitialize = _PvxMSTPPortCrntPMBPDUCFGTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 31),
    _PvxMSTPPortCrntPMBPDUCFGTXInitialize_Type()
)
pvxMSTPPortCrntPMBPDUCFGTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUCFGTXInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNRXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDUTCNRXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNRXValue = _PvxMSTPPortCrntPMBPDUTCNRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 32),
    _PvxMSTPPortCrntPMBPDUTCNRXValue_Type()
)
pvxMSTPPortCrntPMBPDUTCNRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNRXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNRXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDUTCNRXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNRXTimeStamp = _PvxMSTPPortCrntPMBPDUTCNRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 33),
    _PvxMSTPPortCrntPMBPDUTCNRXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDUTCNRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNRXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNRXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDUTCNRXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNRXValidity = _PvxMSTPPortCrntPMBPDUTCNRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 34),
    _PvxMSTPPortCrntPMBPDUTCNRXValidity_Type()
)
pvxMSTPPortCrntPMBPDUTCNRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNRXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNRXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDUTCNRXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNRXInitialize = _PvxMSTPPortCrntPMBPDUTCNRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 35),
    _PvxMSTPPortCrntPMBPDUTCNRXInitialize_Type()
)
pvxMSTPPortCrntPMBPDUTCNRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNRXInitialize.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNTXValue_Type = Unsigned64
_PvxMSTPPortCrntPMBPDUTCNTXValue_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNTXValue = _PvxMSTPPortCrntPMBPDUTCNTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 36),
    _PvxMSTPPortCrntPMBPDUTCNTXValue_Type()
)
pvxMSTPPortCrntPMBPDUTCNTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNTXValue.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNTXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMBPDUTCNTXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNTXTimeStamp = _PvxMSTPPortCrntPMBPDUTCNTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 37),
    _PvxMSTPPortCrntPMBPDUTCNTXTimeStamp_Type()
)
pvxMSTPPortCrntPMBPDUTCNTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNTXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNTXValidity_Type = PMValidity
_PvxMSTPPortCrntPMBPDUTCNTXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNTXValidity = _PvxMSTPPortCrntPMBPDUTCNTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 38),
    _PvxMSTPPortCrntPMBPDUTCNTXValidity_Type()
)
pvxMSTPPortCrntPMBPDUTCNTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNTXValidity.setStatus("current")
_PvxMSTPPortCrntPMBPDUTCNTXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMBPDUTCNTXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMBPDUTCNTXInitialize = _PvxMSTPPortCrntPMBPDUTCNTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 39),
    _PvxMSTPPortCrntPMBPDUTCNTXInitialize_Type()
)
pvxMSTPPortCrntPMBPDUTCNTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMBPDUTCNTXInitialize.setStatus("current")
_PvxMSTPPortCrntPMINVBPDURXValue_Type = Unsigned64
_PvxMSTPPortCrntPMINVBPDURXValue_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDURXValue = _PvxMSTPPortCrntPMINVBPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 40),
    _PvxMSTPPortCrntPMINVBPDURXValue_Type()
)
pvxMSTPPortCrntPMINVBPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDURXValue.setStatus("current")
_PvxMSTPPortCrntPMINVBPDURXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMINVBPDURXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDURXTimeStamp = _PvxMSTPPortCrntPMINVBPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 41),
    _PvxMSTPPortCrntPMINVBPDURXTimeStamp_Type()
)
pvxMSTPPortCrntPMINVBPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDURXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMINVBPDURXValidity_Type = PMValidity
_PvxMSTPPortCrntPMINVBPDURXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDURXValidity = _PvxMSTPPortCrntPMINVBPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 42),
    _PvxMSTPPortCrntPMINVBPDURXValidity_Type()
)
pvxMSTPPortCrntPMINVBPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDURXValidity.setStatus("current")
_PvxMSTPPortCrntPMINVBPDURXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMINVBPDURXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDURXInitialize = _PvxMSTPPortCrntPMINVBPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 43),
    _PvxMSTPPortCrntPMINVBPDURXInitialize_Type()
)
pvxMSTPPortCrntPMINVBPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDURXInitialize.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUCFGRXValue_Type = Unsigned64
_PvxMSTPPortCrntPMINVBPDUCFGRXValue_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUCFGRXValue = _PvxMSTPPortCrntPMINVBPDUCFGRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 44),
    _PvxMSTPPortCrntPMINVBPDUCFGRXValue_Type()
)
pvxMSTPPortCrntPMINVBPDUCFGRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUCFGRXValue.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp = _PvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 45),
    _PvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp_Type()
)
pvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUCFGRXValidity_Type = PMValidity
_PvxMSTPPortCrntPMINVBPDUCFGRXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUCFGRXValidity = _PvxMSTPPortCrntPMINVBPDUCFGRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 46),
    _PvxMSTPPortCrntPMINVBPDUCFGRXValidity_Type()
)
pvxMSTPPortCrntPMINVBPDUCFGRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUCFGRXValidity.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUCFGRXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMINVBPDUCFGRXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUCFGRXInitialize = _PvxMSTPPortCrntPMINVBPDUCFGRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 47),
    _PvxMSTPPortCrntPMINVBPDUCFGRXInitialize_Type()
)
pvxMSTPPortCrntPMINVBPDUCFGRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUCFGRXInitialize.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUTCNRXValue_Type = Unsigned64
_PvxMSTPPortCrntPMINVBPDUTCNRXValue_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUTCNRXValue = _PvxMSTPPortCrntPMINVBPDUTCNRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 48),
    _PvxMSTPPortCrntPMINVBPDUTCNRXValue_Type()
)
pvxMSTPPortCrntPMINVBPDUTCNRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUTCNRXValue.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp_Type = DateAndTime
_PvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp = _PvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 49),
    _PvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp_Type()
)
pvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUTCNRXValidity_Type = PMValidity
_PvxMSTPPortCrntPMINVBPDUTCNRXValidity_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUTCNRXValidity = _PvxMSTPPortCrntPMINVBPDUTCNRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 50),
    _PvxMSTPPortCrntPMINVBPDUTCNRXValidity_Type()
)
pvxMSTPPortCrntPMINVBPDUTCNRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUTCNRXValidity.setStatus("current")
_PvxMSTPPortCrntPMINVBPDUTCNRXInitialize_Type = InitializeCmd
_PvxMSTPPortCrntPMINVBPDUTCNRXInitialize_Object = MibTableColumn
pvxMSTPPortCrntPMINVBPDUTCNRXInitialize = _PvxMSTPPortCrntPMINVBPDUTCNRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 34, 1, 51),
    _PvxMSTPPortCrntPMINVBPDUTCNRXInitialize_Type()
)
pvxMSTPPortCrntPMINVBPDUTCNRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortCrntPMINVBPDUTCNRXInitialize.setStatus("current")
_PvxMSTPPortHistPMTable_Object = MibTable
pvxMSTPPortHistPMTable = _PvxMSTPPortHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35)
)
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMTable.setStatus("current")
_PvxMSTPPortHistPMEntry_Object = MibTableRow
pvxMSTPPortHistPMEntry = _PvxMSTPPortHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1)
)
pvxMSTPPortHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMXstIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMEntry.setStatus("current")


class _PvxMSTPPortHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPPortHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMSwitchIdx_Object = MibTableColumn
pvxMSTPPortHistPMSwitchIdx = _PvxMSTPPortHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 1),
    _PvxMSTPPortHistPMSwitchIdx_Type()
)
pvxMSTPPortHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMSwitchIdx.setStatus("current")


class _PvxMSTPPortHistPMShelfIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxMSTPPortHistPMShelfIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMShelfIdx_Object = MibTableColumn
pvxMSTPPortHistPMShelfIdx = _PvxMSTPPortHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 2),
    _PvxMSTPPortHistPMShelfIdx_Type()
)
pvxMSTPPortHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMShelfIdx.setStatus("current")


class _PvxMSTPPortHistPMSlotIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxMSTPPortHistPMSlotIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMSlotIdx_Object = MibTableColumn
pvxMSTPPortHistPMSlotIdx = _PvxMSTPPortHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 3),
    _PvxMSTPPortHistPMSlotIdx_Type()
)
pvxMSTPPortHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMSlotIdx.setStatus("current")
_PvxMSTPPortHistPMTypeIdx_Type = PvxPortType
_PvxMSTPPortHistPMTypeIdx_Object = MibTableColumn
pvxMSTPPortHistPMTypeIdx = _PvxMSTPPortHistPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 4),
    _PvxMSTPPortHistPMTypeIdx_Type()
)
pvxMSTPPortHistPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMTypeIdx.setStatus("current")


class _PvxMSTPPortHistPMXstIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMXstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxMSTPPortHistPMXstIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMXstIdx_Object = MibTableColumn
pvxMSTPPortHistPMXstIdx = _PvxMSTPPortHistPMXstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 5),
    _PvxMSTPPortHistPMXstIdx_Type()
)
pvxMSTPPortHistPMXstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMXstIdx.setStatus("current")


class _PvxMSTPPortHistPMIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxMSTPPortHistPMIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMIdx_Object = MibTableColumn
pvxMSTPPortHistPMIdx = _PvxMSTPPortHistPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 6),
    _PvxMSTPPortHistPMIdx_Type()
)
pvxMSTPPortHistPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMIdx.setStatus("current")
_PvxMSTPPortHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxMSTPPortHistPMIntervalTypeIdx_Object = MibTableColumn
pvxMSTPPortHistPMIntervalTypeIdx = _PvxMSTPPortHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 7),
    _PvxMSTPPortHistPMIntervalTypeIdx_Type()
)
pvxMSTPPortHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMIntervalTypeIdx.setStatus("current")


class _PvxMSTPPortHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxMSTPPortHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxMSTPPortHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxMSTPPortHistPMIntervalIdx_Object = MibTableColumn
pvxMSTPPortHistPMIntervalIdx = _PvxMSTPPortHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 8),
    _PvxMSTPPortHistPMIntervalIdx_Type()
)
pvxMSTPPortHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMIntervalIdx.setStatus("current")
_PvxMSTPPortHistPMFWDTRValue_Type = Unsigned64
_PvxMSTPPortHistPMFWDTRValue_Object = MibTableColumn
pvxMSTPPortHistPMFWDTRValue = _PvxMSTPPortHistPMFWDTRValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 9),
    _PvxMSTPPortHistPMFWDTRValue_Type()
)
pvxMSTPPortHistPMFWDTRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMFWDTRValue.setStatus("current")
_PvxMSTPPortHistPMFWDTRTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMFWDTRTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMFWDTRTimeStamp = _PvxMSTPPortHistPMFWDTRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 10),
    _PvxMSTPPortHistPMFWDTRTimeStamp_Type()
)
pvxMSTPPortHistPMFWDTRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMFWDTRTimeStamp.setStatus("current")
_PvxMSTPPortHistPMFWDTRValidity_Type = PMValidity
_PvxMSTPPortHistPMFWDTRValidity_Object = MibTableColumn
pvxMSTPPortHistPMFWDTRValidity = _PvxMSTPPortHistPMFWDTRValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 11),
    _PvxMSTPPortHistPMFWDTRValidity_Type()
)
pvxMSTPPortHistPMFWDTRValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMFWDTRValidity.setStatus("current")
_PvxMSTPPortHistPMFWDTRInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMFWDTRInitialize_Object = MibTableColumn
pvxMSTPPortHistPMFWDTRInitialize = _PvxMSTPPortHistPMFWDTRInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 12),
    _PvxMSTPPortHistPMFWDTRInitialize_Type()
)
pvxMSTPPortHistPMFWDTRInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMFWDTRInitialize.setStatus("current")
_PvxMSTPPortHistPMPMCValue_Type = Unsigned64
_PvxMSTPPortHistPMPMCValue_Object = MibTableColumn
pvxMSTPPortHistPMPMCValue = _PvxMSTPPortHistPMPMCValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 13),
    _PvxMSTPPortHistPMPMCValue_Type()
)
pvxMSTPPortHistPMPMCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMPMCValue.setStatus("current")
_PvxMSTPPortHistPMPMCTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMPMCTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMPMCTimeStamp = _PvxMSTPPortHistPMPMCTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 14),
    _PvxMSTPPortHistPMPMCTimeStamp_Type()
)
pvxMSTPPortHistPMPMCTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMPMCTimeStamp.setStatus("current")
_PvxMSTPPortHistPMPMCValidity_Type = PMValidity
_PvxMSTPPortHistPMPMCValidity_Object = MibTableColumn
pvxMSTPPortHistPMPMCValidity = _PvxMSTPPortHistPMPMCValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 15),
    _PvxMSTPPortHistPMPMCValidity_Type()
)
pvxMSTPPortHistPMPMCValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMPMCValidity.setStatus("current")
_PvxMSTPPortHistPMPMCInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMPMCInitialize_Object = MibTableColumn
pvxMSTPPortHistPMPMCInitialize = _PvxMSTPPortHistPMPMCInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 16),
    _PvxMSTPPortHistPMPMCInitialize_Type()
)
pvxMSTPPortHistPMPMCInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMPMCInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDURXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDURXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDURXValue = _PvxMSTPPortHistPMBPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 17),
    _PvxMSTPPortHistPMBPDURXValue_Type()
)
pvxMSTPPortHistPMBPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDURXValue.setStatus("current")
_PvxMSTPPortHistPMBPDURXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDURXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDURXTimeStamp = _PvxMSTPPortHistPMBPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 18),
    _PvxMSTPPortHistPMBPDURXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDURXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDURXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDURXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDURXValidity = _PvxMSTPPortHistPMBPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 19),
    _PvxMSTPPortHistPMBPDURXValidity_Type()
)
pvxMSTPPortHistPMBPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDURXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDURXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDURXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDURXInitialize = _PvxMSTPPortHistPMBPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 20),
    _PvxMSTPPortHistPMBPDURXInitialize_Type()
)
pvxMSTPPortHistPMBPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDURXInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDUTXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDUTXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTXValue = _PvxMSTPPortHistPMBPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 21),
    _PvxMSTPPortHistPMBPDUTXValue_Type()
)
pvxMSTPPortHistPMBPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTXValue.setStatus("current")
_PvxMSTPPortHistPMBPDUTXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDUTXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTXTimeStamp = _PvxMSTPPortHistPMBPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 22),
    _PvxMSTPPortHistPMBPDUTXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDUTXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDUTXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTXValidity = _PvxMSTPPortHistPMBPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 23),
    _PvxMSTPPortHistPMBPDUTXValidity_Type()
)
pvxMSTPPortHistPMBPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDUTXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDUTXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTXInitialize = _PvxMSTPPortHistPMBPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 24),
    _PvxMSTPPortHistPMBPDUTXInitialize_Type()
)
pvxMSTPPortHistPMBPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTXInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGRXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDUCFGRXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGRXValue = _PvxMSTPPortHistPMBPDUCFGRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 25),
    _PvxMSTPPortHistPMBPDUCFGRXValue_Type()
)
pvxMSTPPortHistPMBPDUCFGRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGRXValue.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGRXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDUCFGRXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGRXTimeStamp = _PvxMSTPPortHistPMBPDUCFGRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 26),
    _PvxMSTPPortHistPMBPDUCFGRXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDUCFGRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGRXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGRXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDUCFGRXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGRXValidity = _PvxMSTPPortHistPMBPDUCFGRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 27),
    _PvxMSTPPortHistPMBPDUCFGRXValidity_Type()
)
pvxMSTPPortHistPMBPDUCFGRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGRXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGRXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDUCFGRXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGRXInitialize = _PvxMSTPPortHistPMBPDUCFGRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 28),
    _PvxMSTPPortHistPMBPDUCFGRXInitialize_Type()
)
pvxMSTPPortHistPMBPDUCFGRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGRXInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGTXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDUCFGTXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGTXValue = _PvxMSTPPortHistPMBPDUCFGTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 29),
    _PvxMSTPPortHistPMBPDUCFGTXValue_Type()
)
pvxMSTPPortHistPMBPDUCFGTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGTXValue.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGTXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDUCFGTXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGTXTimeStamp = _PvxMSTPPortHistPMBPDUCFGTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 30),
    _PvxMSTPPortHistPMBPDUCFGTXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDUCFGTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGTXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGTXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDUCFGTXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGTXValidity = _PvxMSTPPortHistPMBPDUCFGTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 31),
    _PvxMSTPPortHistPMBPDUCFGTXValidity_Type()
)
pvxMSTPPortHistPMBPDUCFGTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGTXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDUCFGTXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDUCFGTXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDUCFGTXInitialize = _PvxMSTPPortHistPMBPDUCFGTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 32),
    _PvxMSTPPortHistPMBPDUCFGTXInitialize_Type()
)
pvxMSTPPortHistPMBPDUCFGTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUCFGTXInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNRXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDUTCNRXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNRXValue = _PvxMSTPPortHistPMBPDUTCNRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 33),
    _PvxMSTPPortHistPMBPDUTCNRXValue_Type()
)
pvxMSTPPortHistPMBPDUTCNRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNRXValue.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNRXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDUTCNRXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNRXTimeStamp = _PvxMSTPPortHistPMBPDUTCNRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 34),
    _PvxMSTPPortHistPMBPDUTCNRXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDUTCNRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNRXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNRXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDUTCNRXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNRXValidity = _PvxMSTPPortHistPMBPDUTCNRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 35),
    _PvxMSTPPortHistPMBPDUTCNRXValidity_Type()
)
pvxMSTPPortHistPMBPDUTCNRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNRXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNRXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDUTCNRXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNRXInitialize = _PvxMSTPPortHistPMBPDUTCNRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 36),
    _PvxMSTPPortHistPMBPDUTCNRXInitialize_Type()
)
pvxMSTPPortHistPMBPDUTCNRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNRXInitialize.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNTXValue_Type = Unsigned64
_PvxMSTPPortHistPMBPDUTCNTXValue_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNTXValue = _PvxMSTPPortHistPMBPDUTCNTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 37),
    _PvxMSTPPortHistPMBPDUTCNTXValue_Type()
)
pvxMSTPPortHistPMBPDUTCNTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNTXValue.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNTXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMBPDUTCNTXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNTXTimeStamp = _PvxMSTPPortHistPMBPDUTCNTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 38),
    _PvxMSTPPortHistPMBPDUTCNTXTimeStamp_Type()
)
pvxMSTPPortHistPMBPDUTCNTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNTXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNTXValidity_Type = PMValidity
_PvxMSTPPortHistPMBPDUTCNTXValidity_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNTXValidity = _PvxMSTPPortHistPMBPDUTCNTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 39),
    _PvxMSTPPortHistPMBPDUTCNTXValidity_Type()
)
pvxMSTPPortHistPMBPDUTCNTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNTXValidity.setStatus("current")
_PvxMSTPPortHistPMBPDUTCNTXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMBPDUTCNTXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMBPDUTCNTXInitialize = _PvxMSTPPortHistPMBPDUTCNTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 40),
    _PvxMSTPPortHistPMBPDUTCNTXInitialize_Type()
)
pvxMSTPPortHistPMBPDUTCNTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMBPDUTCNTXInitialize.setStatus("current")
_PvxMSTPPortHistPMINVBPDURXValue_Type = Unsigned64
_PvxMSTPPortHistPMINVBPDURXValue_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDURXValue = _PvxMSTPPortHistPMINVBPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 41),
    _PvxMSTPPortHistPMINVBPDURXValue_Type()
)
pvxMSTPPortHistPMINVBPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDURXValue.setStatus("current")
_PvxMSTPPortHistPMINVBPDURXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMINVBPDURXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDURXTimeStamp = _PvxMSTPPortHistPMINVBPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 42),
    _PvxMSTPPortHistPMINVBPDURXTimeStamp_Type()
)
pvxMSTPPortHistPMINVBPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDURXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMINVBPDURXValidity_Type = PMValidity
_PvxMSTPPortHistPMINVBPDURXValidity_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDURXValidity = _PvxMSTPPortHistPMINVBPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 43),
    _PvxMSTPPortHistPMINVBPDURXValidity_Type()
)
pvxMSTPPortHistPMINVBPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDURXValidity.setStatus("current")
_PvxMSTPPortHistPMINVBPDURXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMINVBPDURXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDURXInitialize = _PvxMSTPPortHistPMINVBPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 44),
    _PvxMSTPPortHistPMINVBPDURXInitialize_Type()
)
pvxMSTPPortHistPMINVBPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDURXInitialize.setStatus("current")
_PvxMSTPPortHistPMINVBPDUCFGRXValue_Type = Unsigned64
_PvxMSTPPortHistPMINVBPDUCFGRXValue_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUCFGRXValue = _PvxMSTPPortHistPMINVBPDUCFGRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 45),
    _PvxMSTPPortHistPMINVBPDUCFGRXValue_Type()
)
pvxMSTPPortHistPMINVBPDUCFGRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUCFGRXValue.setStatus("current")
_PvxMSTPPortHistPMINVBPDUCFGRXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMINVBPDUCFGRXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUCFGRXTimeStamp = _PvxMSTPPortHistPMINVBPDUCFGRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 46),
    _PvxMSTPPortHistPMINVBPDUCFGRXTimeStamp_Type()
)
pvxMSTPPortHistPMINVBPDUCFGRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUCFGRXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMINVBPDUCFGRXValidity_Type = PMValidity
_PvxMSTPPortHistPMINVBPDUCFGRXValidity_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUCFGRXValidity = _PvxMSTPPortHistPMINVBPDUCFGRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 47),
    _PvxMSTPPortHistPMINVBPDUCFGRXValidity_Type()
)
pvxMSTPPortHistPMINVBPDUCFGRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUCFGRXValidity.setStatus("current")
_PvxMSTPPortHistPMINVBPDUCFGRXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMINVBPDUCFGRXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUCFGRXInitialize = _PvxMSTPPortHistPMINVBPDUCFGRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 48),
    _PvxMSTPPortHistPMINVBPDUCFGRXInitialize_Type()
)
pvxMSTPPortHistPMINVBPDUCFGRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUCFGRXInitialize.setStatus("current")
_PvxMSTPPortHistPMINVBPDUTCNRXValue_Type = Unsigned64
_PvxMSTPPortHistPMINVBPDUTCNRXValue_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUTCNRXValue = _PvxMSTPPortHistPMINVBPDUTCNRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 49),
    _PvxMSTPPortHistPMINVBPDUTCNRXValue_Type()
)
pvxMSTPPortHistPMINVBPDUTCNRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUTCNRXValue.setStatus("current")
_PvxMSTPPortHistPMINVBPDUTCNRXTimeStamp_Type = DateAndTime
_PvxMSTPPortHistPMINVBPDUTCNRXTimeStamp_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUTCNRXTimeStamp = _PvxMSTPPortHistPMINVBPDUTCNRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 50),
    _PvxMSTPPortHistPMINVBPDUTCNRXTimeStamp_Type()
)
pvxMSTPPortHistPMINVBPDUTCNRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUTCNRXTimeStamp.setStatus("current")
_PvxMSTPPortHistPMINVBPDUTCNRXValidity_Type = PMValidity
_PvxMSTPPortHistPMINVBPDUTCNRXValidity_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUTCNRXValidity = _PvxMSTPPortHistPMINVBPDUTCNRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 51),
    _PvxMSTPPortHistPMINVBPDUTCNRXValidity_Type()
)
pvxMSTPPortHistPMINVBPDUTCNRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUTCNRXValidity.setStatus("current")
_PvxMSTPPortHistPMINVBPDUTCNRXInitialize_Type = InitializeCmd
_PvxMSTPPortHistPMINVBPDUTCNRXInitialize_Object = MibTableColumn
pvxMSTPPortHistPMINVBPDUTCNRXInitialize = _PvxMSTPPortHistPMINVBPDUTCNRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 35, 1, 52),
    _PvxMSTPPortHistPMINVBPDUTCNRXInitialize_Type()
)
pvxMSTPPortHistPMINVBPDUTCNRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxMSTPPortHistPMINVBPDUTCNRXInitialize.setStatus("current")
_PvxLAGPortCrntPMTable_Object = MibTable
pvxLAGPortCrntPMTable = _PvxLAGPortCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36)
)
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMTable.setStatus("current")
_PvxLAGPortCrntPMEntry_Object = MibTableRow
pvxLAGPortCrntPMEntry = _PvxLAGPortCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1)
)
pvxLAGPortCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMEntry.setStatus("current")


class _PvxLAGPortCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxLAGPortCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxLAGPortCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxLAGPortCrntPMSwitchIdx_Object = MibTableColumn
pvxLAGPortCrntPMSwitchIdx = _PvxLAGPortCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 1),
    _PvxLAGPortCrntPMSwitchIdx_Type()
)
pvxLAGPortCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMSwitchIdx.setStatus("current")


class _PvxLAGPortCrntPMShelfIdx_Type(Integer32):
    """Custom type pvxLAGPortCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxLAGPortCrntPMShelfIdx_Type.__name__ = "Integer32"
_PvxLAGPortCrntPMShelfIdx_Object = MibTableColumn
pvxLAGPortCrntPMShelfIdx = _PvxLAGPortCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 2),
    _PvxLAGPortCrntPMShelfIdx_Type()
)
pvxLAGPortCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMShelfIdx.setStatus("current")


class _PvxLAGPortCrntPMSlotIdx_Type(Integer32):
    """Custom type pvxLAGPortCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxLAGPortCrntPMSlotIdx_Type.__name__ = "Integer32"
_PvxLAGPortCrntPMSlotIdx_Object = MibTableColumn
pvxLAGPortCrntPMSlotIdx = _PvxLAGPortCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 3),
    _PvxLAGPortCrntPMSlotIdx_Type()
)
pvxLAGPortCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMSlotIdx.setStatus("current")
_PvxLAGPortCrntPMTypeIdx_Type = PvxPortType
_PvxLAGPortCrntPMTypeIdx_Object = MibTableColumn
pvxLAGPortCrntPMTypeIdx = _PvxLAGPortCrntPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 4),
    _PvxLAGPortCrntPMTypeIdx_Type()
)
pvxLAGPortCrntPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMTypeIdx.setStatus("current")


class _PvxLAGPortCrntPMIdx_Type(Integer32):
    """Custom type pvxLAGPortCrntPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxLAGPortCrntPMIdx_Type.__name__ = "Integer32"
_PvxLAGPortCrntPMIdx_Object = MibTableColumn
pvxLAGPortCrntPMIdx = _PvxLAGPortCrntPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 5),
    _PvxLAGPortCrntPMIdx_Type()
)
pvxLAGPortCrntPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMIdx.setStatus("current")
_PvxLAGPortCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxLAGPortCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxLAGPortCrntPMIntervalTypeIdx = _PvxLAGPortCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 6),
    _PvxLAGPortCrntPMIntervalTypeIdx_Type()
)
pvxLAGPortCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMIntervalTypeIdx.setStatus("current")
_PvxLAGPortCrntPMLACPDURXValue_Type = Unsigned64
_PvxLAGPortCrntPMLACPDURXValue_Object = MibTableColumn
pvxLAGPortCrntPMLACPDURXValue = _PvxLAGPortCrntPMLACPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 7),
    _PvxLAGPortCrntPMLACPDURXValue_Type()
)
pvxLAGPortCrntPMLACPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDURXValue.setStatus("current")
_PvxLAGPortCrntPMLACPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMLACPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMLACPDURXTimeStamp = _PvxLAGPortCrntPMLACPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 8),
    _PvxLAGPortCrntPMLACPDURXTimeStamp_Type()
)
pvxLAGPortCrntPMLACPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDURXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMLACPDURXValidity_Type = PMValidity
_PvxLAGPortCrntPMLACPDURXValidity_Object = MibTableColumn
pvxLAGPortCrntPMLACPDURXValidity = _PvxLAGPortCrntPMLACPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 9),
    _PvxLAGPortCrntPMLACPDURXValidity_Type()
)
pvxLAGPortCrntPMLACPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDURXValidity.setStatus("current")
_PvxLAGPortCrntPMLACPDURXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMLACPDURXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMLACPDURXInitialize = _PvxLAGPortCrntPMLACPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 10),
    _PvxLAGPortCrntPMLACPDURXInitialize_Type()
)
pvxLAGPortCrntPMLACPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDURXInitialize.setStatus("current")
_PvxLAGPortCrntPMMRKPDURXValue_Type = Unsigned64
_PvxLAGPortCrntPMMRKPDURXValue_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDURXValue = _PvxLAGPortCrntPMMRKPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 11),
    _PvxLAGPortCrntPMMRKPDURXValue_Type()
)
pvxLAGPortCrntPMMRKPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDURXValue.setStatus("current")
_PvxLAGPortCrntPMMRKPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMMRKPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDURXTimeStamp = _PvxLAGPortCrntPMMRKPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 12),
    _PvxLAGPortCrntPMMRKPDURXTimeStamp_Type()
)
pvxLAGPortCrntPMMRKPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDURXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMMRKPDURXValidity_Type = PMValidity
_PvxLAGPortCrntPMMRKPDURXValidity_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDURXValidity = _PvxLAGPortCrntPMMRKPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 13),
    _PvxLAGPortCrntPMMRKPDURXValidity_Type()
)
pvxLAGPortCrntPMMRKPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDURXValidity.setStatus("current")
_PvxLAGPortCrntPMMRKPDURXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMMRKPDURXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDURXInitialize = _PvxLAGPortCrntPMMRKPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 14),
    _PvxLAGPortCrntPMMRKPDURXInitialize_Type()
)
pvxLAGPortCrntPMMRKPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDURXInitialize.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDURXValue_Type = Unsigned64
_PvxLAGPortCrntPMMRKRSPPDURXValue_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDURXValue = _PvxLAGPortCrntPMMRKRSPPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 15),
    _PvxLAGPortCrntPMMRKRSPPDURXValue_Type()
)
pvxLAGPortCrntPMMRKRSPPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDURXValue.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMMRKRSPPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDURXTimeStamp = _PvxLAGPortCrntPMMRKRSPPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 16),
    _PvxLAGPortCrntPMMRKRSPPDURXTimeStamp_Type()
)
pvxLAGPortCrntPMMRKRSPPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDURXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDURXValidity_Type = PMValidity
_PvxLAGPortCrntPMMRKRSPPDURXValidity_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDURXValidity = _PvxLAGPortCrntPMMRKRSPPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 17),
    _PvxLAGPortCrntPMMRKRSPPDURXValidity_Type()
)
pvxLAGPortCrntPMMRKRSPPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDURXValidity.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDURXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMMRKRSPPDURXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDURXInitialize = _PvxLAGPortCrntPMMRKRSPPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 18),
    _PvxLAGPortCrntPMMRKRSPPDURXInitialize_Type()
)
pvxLAGPortCrntPMMRKRSPPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDURXInitialize.setStatus("current")
_PvxLAGPortCrntPMINVLACFRRXValue_Type = Unsigned64
_PvxLAGPortCrntPMINVLACFRRXValue_Object = MibTableColumn
pvxLAGPortCrntPMINVLACFRRXValue = _PvxLAGPortCrntPMINVLACFRRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 19),
    _PvxLAGPortCrntPMINVLACFRRXValue_Type()
)
pvxLAGPortCrntPMINVLACFRRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMINVLACFRRXValue.setStatus("current")
_PvxLAGPortCrntPMINVLACFRRXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMINVLACFRRXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMINVLACFRRXTimeStamp = _PvxLAGPortCrntPMINVLACFRRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 20),
    _PvxLAGPortCrntPMINVLACFRRXTimeStamp_Type()
)
pvxLAGPortCrntPMINVLACFRRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMINVLACFRRXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMINVLACFRRXValidity_Type = PMValidity
_PvxLAGPortCrntPMINVLACFRRXValidity_Object = MibTableColumn
pvxLAGPortCrntPMINVLACFRRXValidity = _PvxLAGPortCrntPMINVLACFRRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 21),
    _PvxLAGPortCrntPMINVLACFRRXValidity_Type()
)
pvxLAGPortCrntPMINVLACFRRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMINVLACFRRXValidity.setStatus("current")
_PvxLAGPortCrntPMINVLACFRRXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMINVLACFRRXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMINVLACFRRXInitialize = _PvxLAGPortCrntPMINVLACFRRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 22),
    _PvxLAGPortCrntPMINVLACFRRXInitialize_Type()
)
pvxLAGPortCrntPMINVLACFRRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMINVLACFRRXInitialize.setStatus("current")
_PvxLAGPortCrntPMLACPDUTXValue_Type = Unsigned64
_PvxLAGPortCrntPMLACPDUTXValue_Object = MibTableColumn
pvxLAGPortCrntPMLACPDUTXValue = _PvxLAGPortCrntPMLACPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 23),
    _PvxLAGPortCrntPMLACPDUTXValue_Type()
)
pvxLAGPortCrntPMLACPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDUTXValue.setStatus("current")
_PvxLAGPortCrntPMLACPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMLACPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMLACPDUTXTimeStamp = _PvxLAGPortCrntPMLACPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 24),
    _PvxLAGPortCrntPMLACPDUTXTimeStamp_Type()
)
pvxLAGPortCrntPMLACPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDUTXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMLACPDUTXValidity_Type = PMValidity
_PvxLAGPortCrntPMLACPDUTXValidity_Object = MibTableColumn
pvxLAGPortCrntPMLACPDUTXValidity = _PvxLAGPortCrntPMLACPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 25),
    _PvxLAGPortCrntPMLACPDUTXValidity_Type()
)
pvxLAGPortCrntPMLACPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDUTXValidity.setStatus("current")
_PvxLAGPortCrntPMLACPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMLACPDUTXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMLACPDUTXInitialize = _PvxLAGPortCrntPMLACPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 26),
    _PvxLAGPortCrntPMLACPDUTXInitialize_Type()
)
pvxLAGPortCrntPMLACPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMLACPDUTXInitialize.setStatus("current")
_PvxLAGPortCrntPMMRKPDUTXValue_Type = Unsigned64
_PvxLAGPortCrntPMMRKPDUTXValue_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDUTXValue = _PvxLAGPortCrntPMMRKPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 27),
    _PvxLAGPortCrntPMMRKPDUTXValue_Type()
)
pvxLAGPortCrntPMMRKPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDUTXValue.setStatus("current")
_PvxLAGPortCrntPMMRKPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMMRKPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDUTXTimeStamp = _PvxLAGPortCrntPMMRKPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 28),
    _PvxLAGPortCrntPMMRKPDUTXTimeStamp_Type()
)
pvxLAGPortCrntPMMRKPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDUTXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMMRKPDUTXValidity_Type = PMValidity
_PvxLAGPortCrntPMMRKPDUTXValidity_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDUTXValidity = _PvxLAGPortCrntPMMRKPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 29),
    _PvxLAGPortCrntPMMRKPDUTXValidity_Type()
)
pvxLAGPortCrntPMMRKPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDUTXValidity.setStatus("current")
_PvxLAGPortCrntPMMRKPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMMRKPDUTXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMMRKPDUTXInitialize = _PvxLAGPortCrntPMMRKPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 30),
    _PvxLAGPortCrntPMMRKPDUTXInitialize_Type()
)
pvxLAGPortCrntPMMRKPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKPDUTXInitialize.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDUTXValue_Type = Unsigned64
_PvxLAGPortCrntPMMRKRSPPDUTXValue_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDUTXValue = _PvxLAGPortCrntPMMRKRSPPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 31),
    _PvxLAGPortCrntPMMRKRSPPDUTXValue_Type()
)
pvxLAGPortCrntPMMRKRSPPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDUTXValue.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortCrntPMMRKRSPPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDUTXTimeStamp = _PvxLAGPortCrntPMMRKRSPPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 32),
    _PvxLAGPortCrntPMMRKRSPPDUTXTimeStamp_Type()
)
pvxLAGPortCrntPMMRKRSPPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDUTXTimeStamp.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDUTXValidity_Type = PMValidity
_PvxLAGPortCrntPMMRKRSPPDUTXValidity_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDUTXValidity = _PvxLAGPortCrntPMMRKRSPPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 33),
    _PvxLAGPortCrntPMMRKRSPPDUTXValidity_Type()
)
pvxLAGPortCrntPMMRKRSPPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDUTXValidity.setStatus("current")
_PvxLAGPortCrntPMMRKRSPPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortCrntPMMRKRSPPDUTXInitialize_Object = MibTableColumn
pvxLAGPortCrntPMMRKRSPPDUTXInitialize = _PvxLAGPortCrntPMMRKRSPPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 36, 1, 34),
    _PvxLAGPortCrntPMMRKRSPPDUTXInitialize_Type()
)
pvxLAGPortCrntPMMRKRSPPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortCrntPMMRKRSPPDUTXInitialize.setStatus("current")
_PvxLAGPortHistPMTable_Object = MibTable
pvxLAGPortHistPMTable = _PvxLAGPortHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37)
)
if mibBuilder.loadTexts:
    pvxLAGPortHistPMTable.setStatus("current")
_PvxLAGPortHistPMEntry_Object = MibTableRow
pvxLAGPortHistPMEntry = _PvxLAGPortHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1)
)
pvxLAGPortHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLAGPortHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxLAGPortHistPMEntry.setStatus("current")


class _PvxLAGPortHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxLAGPortHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxLAGPortHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxLAGPortHistPMSwitchIdx_Object = MibTableColumn
pvxLAGPortHistPMSwitchIdx = _PvxLAGPortHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 1),
    _PvxLAGPortHistPMSwitchIdx_Type()
)
pvxLAGPortHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMSwitchIdx.setStatus("current")


class _PvxLAGPortHistPMShelfIdx_Type(Integer32):
    """Custom type pvxLAGPortHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxLAGPortHistPMShelfIdx_Type.__name__ = "Integer32"
_PvxLAGPortHistPMShelfIdx_Object = MibTableColumn
pvxLAGPortHistPMShelfIdx = _PvxLAGPortHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 2),
    _PvxLAGPortHistPMShelfIdx_Type()
)
pvxLAGPortHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMShelfIdx.setStatus("current")


class _PvxLAGPortHistPMSlotIdx_Type(Integer32):
    """Custom type pvxLAGPortHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxLAGPortHistPMSlotIdx_Type.__name__ = "Integer32"
_PvxLAGPortHistPMSlotIdx_Object = MibTableColumn
pvxLAGPortHistPMSlotIdx = _PvxLAGPortHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 3),
    _PvxLAGPortHistPMSlotIdx_Type()
)
pvxLAGPortHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMSlotIdx.setStatus("current")
_PvxLAGPortHistPMTypeIdx_Type = PvxPortType
_PvxLAGPortHistPMTypeIdx_Object = MibTableColumn
pvxLAGPortHistPMTypeIdx = _PvxLAGPortHistPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 4),
    _PvxLAGPortHistPMTypeIdx_Type()
)
pvxLAGPortHistPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMTypeIdx.setStatus("current")


class _PvxLAGPortHistPMIdx_Type(Integer32):
    """Custom type pvxLAGPortHistPMIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxLAGPortHistPMIdx_Type.__name__ = "Integer32"
_PvxLAGPortHistPMIdx_Object = MibTableColumn
pvxLAGPortHistPMIdx = _PvxLAGPortHistPMIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 5),
    _PvxLAGPortHistPMIdx_Type()
)
pvxLAGPortHistPMIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMIdx.setStatus("current")
_PvxLAGPortHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxLAGPortHistPMIntervalTypeIdx_Object = MibTableColumn
pvxLAGPortHistPMIntervalTypeIdx = _PvxLAGPortHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 6),
    _PvxLAGPortHistPMIntervalTypeIdx_Type()
)
pvxLAGPortHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMIntervalTypeIdx.setStatus("current")


class _PvxLAGPortHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxLAGPortHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxLAGPortHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxLAGPortHistPMIntervalIdx_Object = MibTableColumn
pvxLAGPortHistPMIntervalIdx = _PvxLAGPortHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 7),
    _PvxLAGPortHistPMIntervalIdx_Type()
)
pvxLAGPortHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMIntervalIdx.setStatus("current")
_PvxLAGPortHistPMLACPDURXValue_Type = Unsigned64
_PvxLAGPortHistPMLACPDURXValue_Object = MibTableColumn
pvxLAGPortHistPMLACPDURXValue = _PvxLAGPortHistPMLACPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 8),
    _PvxLAGPortHistPMLACPDURXValue_Type()
)
pvxLAGPortHistPMLACPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDURXValue.setStatus("current")
_PvxLAGPortHistPMLACPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMLACPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMLACPDURXTimeStamp = _PvxLAGPortHistPMLACPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 9),
    _PvxLAGPortHistPMLACPDURXTimeStamp_Type()
)
pvxLAGPortHistPMLACPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDURXTimeStamp.setStatus("current")
_PvxLAGPortHistPMLACPDURXValidity_Type = PMValidity
_PvxLAGPortHistPMLACPDURXValidity_Object = MibTableColumn
pvxLAGPortHistPMLACPDURXValidity = _PvxLAGPortHistPMLACPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 10),
    _PvxLAGPortHistPMLACPDURXValidity_Type()
)
pvxLAGPortHistPMLACPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDURXValidity.setStatus("current")
_PvxLAGPortHistPMLACPDURXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMLACPDURXInitialize_Object = MibTableColumn
pvxLAGPortHistPMLACPDURXInitialize = _PvxLAGPortHistPMLACPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 11),
    _PvxLAGPortHistPMLACPDURXInitialize_Type()
)
pvxLAGPortHistPMLACPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDURXInitialize.setStatus("current")
_PvxLAGPortHistPMMRKPDURXValue_Type = Unsigned64
_PvxLAGPortHistPMMRKPDURXValue_Object = MibTableColumn
pvxLAGPortHistPMMRKPDURXValue = _PvxLAGPortHistPMMRKPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 12),
    _PvxLAGPortHistPMMRKPDURXValue_Type()
)
pvxLAGPortHistPMMRKPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDURXValue.setStatus("current")
_PvxLAGPortHistPMMRKPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMMRKPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMMRKPDURXTimeStamp = _PvxLAGPortHistPMMRKPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 13),
    _PvxLAGPortHistPMMRKPDURXTimeStamp_Type()
)
pvxLAGPortHistPMMRKPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDURXTimeStamp.setStatus("current")
_PvxLAGPortHistPMMRKPDURXValidity_Type = PMValidity
_PvxLAGPortHistPMMRKPDURXValidity_Object = MibTableColumn
pvxLAGPortHistPMMRKPDURXValidity = _PvxLAGPortHistPMMRKPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 14),
    _PvxLAGPortHistPMMRKPDURXValidity_Type()
)
pvxLAGPortHistPMMRKPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDURXValidity.setStatus("current")
_PvxLAGPortHistPMMRKPDURXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMMRKPDURXInitialize_Object = MibTableColumn
pvxLAGPortHistPMMRKPDURXInitialize = _PvxLAGPortHistPMMRKPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 15),
    _PvxLAGPortHistPMMRKPDURXInitialize_Type()
)
pvxLAGPortHistPMMRKPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDURXInitialize.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDURXValue_Type = Unsigned64
_PvxLAGPortHistPMMRKRSPPDURXValue_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDURXValue = _PvxLAGPortHistPMMRKRSPPDURXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 16),
    _PvxLAGPortHistPMMRKRSPPDURXValue_Type()
)
pvxLAGPortHistPMMRKRSPPDURXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDURXValue.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDURXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMMRKRSPPDURXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDURXTimeStamp = _PvxLAGPortHistPMMRKRSPPDURXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 17),
    _PvxLAGPortHistPMMRKRSPPDURXTimeStamp_Type()
)
pvxLAGPortHistPMMRKRSPPDURXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDURXTimeStamp.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDURXValidity_Type = PMValidity
_PvxLAGPortHistPMMRKRSPPDURXValidity_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDURXValidity = _PvxLAGPortHistPMMRKRSPPDURXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 18),
    _PvxLAGPortHistPMMRKRSPPDURXValidity_Type()
)
pvxLAGPortHistPMMRKRSPPDURXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDURXValidity.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDURXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMMRKRSPPDURXInitialize_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDURXInitialize = _PvxLAGPortHistPMMRKRSPPDURXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 19),
    _PvxLAGPortHistPMMRKRSPPDURXInitialize_Type()
)
pvxLAGPortHistPMMRKRSPPDURXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDURXInitialize.setStatus("current")
_PvxLAGPortHistPMINVLACFRRXValue_Type = Unsigned64
_PvxLAGPortHistPMINVLACFRRXValue_Object = MibTableColumn
pvxLAGPortHistPMINVLACFRRXValue = _PvxLAGPortHistPMINVLACFRRXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 20),
    _PvxLAGPortHistPMINVLACFRRXValue_Type()
)
pvxLAGPortHistPMINVLACFRRXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMINVLACFRRXValue.setStatus("current")
_PvxLAGPortHistPMINVLACFRRXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMINVLACFRRXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMINVLACFRRXTimeStamp = _PvxLAGPortHistPMINVLACFRRXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 21),
    _PvxLAGPortHistPMINVLACFRRXTimeStamp_Type()
)
pvxLAGPortHistPMINVLACFRRXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMINVLACFRRXTimeStamp.setStatus("current")
_PvxLAGPortHistPMINVLACFRRXValidity_Type = PMValidity
_PvxLAGPortHistPMINVLACFRRXValidity_Object = MibTableColumn
pvxLAGPortHistPMINVLACFRRXValidity = _PvxLAGPortHistPMINVLACFRRXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 22),
    _PvxLAGPortHistPMINVLACFRRXValidity_Type()
)
pvxLAGPortHistPMINVLACFRRXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMINVLACFRRXValidity.setStatus("current")
_PvxLAGPortHistPMINVLACFRRXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMINVLACFRRXInitialize_Object = MibTableColumn
pvxLAGPortHistPMINVLACFRRXInitialize = _PvxLAGPortHistPMINVLACFRRXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 23),
    _PvxLAGPortHistPMINVLACFRRXInitialize_Type()
)
pvxLAGPortHistPMINVLACFRRXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMINVLACFRRXInitialize.setStatus("current")
_PvxLAGPortHistPMLACPDUTXValue_Type = Unsigned64
_PvxLAGPortHistPMLACPDUTXValue_Object = MibTableColumn
pvxLAGPortHistPMLACPDUTXValue = _PvxLAGPortHistPMLACPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 24),
    _PvxLAGPortHistPMLACPDUTXValue_Type()
)
pvxLAGPortHistPMLACPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDUTXValue.setStatus("current")
_PvxLAGPortHistPMLACPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMLACPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMLACPDUTXTimeStamp = _PvxLAGPortHistPMLACPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 25),
    _PvxLAGPortHistPMLACPDUTXTimeStamp_Type()
)
pvxLAGPortHistPMLACPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDUTXTimeStamp.setStatus("current")
_PvxLAGPortHistPMLACPDUTXValidity_Type = PMValidity
_PvxLAGPortHistPMLACPDUTXValidity_Object = MibTableColumn
pvxLAGPortHistPMLACPDUTXValidity = _PvxLAGPortHistPMLACPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 26),
    _PvxLAGPortHistPMLACPDUTXValidity_Type()
)
pvxLAGPortHistPMLACPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDUTXValidity.setStatus("current")
_PvxLAGPortHistPMLACPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMLACPDUTXInitialize_Object = MibTableColumn
pvxLAGPortHistPMLACPDUTXInitialize = _PvxLAGPortHistPMLACPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 27),
    _PvxLAGPortHistPMLACPDUTXInitialize_Type()
)
pvxLAGPortHistPMLACPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMLACPDUTXInitialize.setStatus("current")
_PvxLAGPortHistPMMRKPDUTXValue_Type = Unsigned64
_PvxLAGPortHistPMMRKPDUTXValue_Object = MibTableColumn
pvxLAGPortHistPMMRKPDUTXValue = _PvxLAGPortHistPMMRKPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 28),
    _PvxLAGPortHistPMMRKPDUTXValue_Type()
)
pvxLAGPortHistPMMRKPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDUTXValue.setStatus("current")
_PvxLAGPortHistPMMRKPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMMRKPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMMRKPDUTXTimeStamp = _PvxLAGPortHistPMMRKPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 29),
    _PvxLAGPortHistPMMRKPDUTXTimeStamp_Type()
)
pvxLAGPortHistPMMRKPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDUTXTimeStamp.setStatus("current")
_PvxLAGPortHistPMMRKPDUTXValidity_Type = PMValidity
_PvxLAGPortHistPMMRKPDUTXValidity_Object = MibTableColumn
pvxLAGPortHistPMMRKPDUTXValidity = _PvxLAGPortHistPMMRKPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 30),
    _PvxLAGPortHistPMMRKPDUTXValidity_Type()
)
pvxLAGPortHistPMMRKPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDUTXValidity.setStatus("current")
_PvxLAGPortHistPMMRKPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMMRKPDUTXInitialize_Object = MibTableColumn
pvxLAGPortHistPMMRKPDUTXInitialize = _PvxLAGPortHistPMMRKPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 31),
    _PvxLAGPortHistPMMRKPDUTXInitialize_Type()
)
pvxLAGPortHistPMMRKPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKPDUTXInitialize.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDUTXValue_Type = Unsigned64
_PvxLAGPortHistPMMRKRSPPDUTXValue_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDUTXValue = _PvxLAGPortHistPMMRKRSPPDUTXValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 32),
    _PvxLAGPortHistPMMRKRSPPDUTXValue_Type()
)
pvxLAGPortHistPMMRKRSPPDUTXValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDUTXValue.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDUTXTimeStamp_Type = DateAndTime
_PvxLAGPortHistPMMRKRSPPDUTXTimeStamp_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDUTXTimeStamp = _PvxLAGPortHistPMMRKRSPPDUTXTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 33),
    _PvxLAGPortHistPMMRKRSPPDUTXTimeStamp_Type()
)
pvxLAGPortHistPMMRKRSPPDUTXTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDUTXTimeStamp.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDUTXValidity_Type = PMValidity
_PvxLAGPortHistPMMRKRSPPDUTXValidity_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDUTXValidity = _PvxLAGPortHistPMMRKRSPPDUTXValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 34),
    _PvxLAGPortHistPMMRKRSPPDUTXValidity_Type()
)
pvxLAGPortHistPMMRKRSPPDUTXValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDUTXValidity.setStatus("current")
_PvxLAGPortHistPMMRKRSPPDUTXInitialize_Type = InitializeCmd
_PvxLAGPortHistPMMRKRSPPDUTXInitialize_Object = MibTableColumn
pvxLAGPortHistPMMRKRSPPDUTXInitialize = _PvxLAGPortHistPMMRKRSPPDUTXInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 37, 1, 35),
    _PvxLAGPortHistPMMRKRSPPDUTXInitialize_Type()
)
pvxLAGPortHistPMMRKRSPPDUTXInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxLAGPortHistPMMRKRSPPDUTXInitialize.setStatus("current")
_PvxESrvcCrntPMTable_Object = MibTable
pvxESrvcCrntPMTable = _PvxESrvcCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40)
)
if mibBuilder.loadTexts:
    pvxESrvcCrntPMTable.setStatus("current")
_PvxESrvcCrntPMEntry_Object = MibTableRow
pvxESrvcCrntPMEntry = _PvxESrvcCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1)
)
pvxESrvcCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcCrntPMESrvcNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxESrvcCrntPMEntry.setStatus("current")


class _PvxESrvcCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxESrvcCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxESrvcCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxESrvcCrntPMSwitchIdx_Object = MibTableColumn
pvxESrvcCrntPMSwitchIdx = _PvxESrvcCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 1),
    _PvxESrvcCrntPMSwitchIdx_Type()
)
pvxESrvcCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMSwitchIdx.setStatus("current")


class _PvxESrvcCrntPMESrvcNameIdx_Type(DisplayString):
    """Custom type pvxESrvcCrntPMESrvcNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcCrntPMESrvcNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcCrntPMESrvcNameIdx_Object = MibTableColumn
pvxESrvcCrntPMESrvcNameIdx = _PvxESrvcCrntPMESrvcNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 2),
    _PvxESrvcCrntPMESrvcNameIdx_Type()
)
pvxESrvcCrntPMESrvcNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMESrvcNameIdx.setStatus("current")
_PvxESrvcCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxESrvcCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxESrvcCrntPMIntervalTypeIdx = _PvxESrvcCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 3),
    _PvxESrvcCrntPMIntervalTypeIdx_Type()
)
pvxESrvcCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMIntervalTypeIdx.setStatus("current")
_PvxESrvcCrntPMUASValue_Type = Unsigned32
_PvxESrvcCrntPMUASValue_Object = MibTableColumn
pvxESrvcCrntPMUASValue = _PvxESrvcCrntPMUASValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 4),
    _PvxESrvcCrntPMUASValue_Type()
)
pvxESrvcCrntPMUASValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMUASValue.setStatus("current")
_PvxESrvcCrntPMUASTimeStamp_Type = DateAndTime
_PvxESrvcCrntPMUASTimeStamp_Object = MibTableColumn
pvxESrvcCrntPMUASTimeStamp = _PvxESrvcCrntPMUASTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 5),
    _PvxESrvcCrntPMUASTimeStamp_Type()
)
pvxESrvcCrntPMUASTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMUASTimeStamp.setStatus("current")
_PvxESrvcCrntPMUASValidity_Type = PMValidity
_PvxESrvcCrntPMUASValidity_Object = MibTableColumn
pvxESrvcCrntPMUASValidity = _PvxESrvcCrntPMUASValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 6),
    _PvxESrvcCrntPMUASValidity_Type()
)
pvxESrvcCrntPMUASValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMUASValidity.setStatus("current")
_PvxESrvcCrntPMUASInitialize_Type = InitializeCmd
_PvxESrvcCrntPMUASInitialize_Object = MibTableColumn
pvxESrvcCrntPMUASInitialize = _PvxESrvcCrntPMUASInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 40, 1, 7),
    _PvxESrvcCrntPMUASInitialize_Type()
)
pvxESrvcCrntPMUASInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcCrntPMUASInitialize.setStatus("current")
_PvxESrvcHistPMTable_Object = MibTable
pvxESrvcHistPMTable = _PvxESrvcHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41)
)
if mibBuilder.loadTexts:
    pvxESrvcHistPMTable.setStatus("current")
_PvxESrvcHistPMEntry_Object = MibTableRow
pvxESrvcHistPMEntry = _PvxESrvcHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1)
)
pvxESrvcHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcHistPMESrvcNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxESrvcHistPMEntry.setStatus("current")


class _PvxESrvcHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxESrvcHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxESrvcHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxESrvcHistPMSwitchIdx_Object = MibTableColumn
pvxESrvcHistPMSwitchIdx = _PvxESrvcHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 1),
    _PvxESrvcHistPMSwitchIdx_Type()
)
pvxESrvcHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcHistPMSwitchIdx.setStatus("current")


class _PvxESrvcHistPMESrvcNameIdx_Type(DisplayString):
    """Custom type pvxESrvcHistPMESrvcNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcHistPMESrvcNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcHistPMESrvcNameIdx_Object = MibTableColumn
pvxESrvcHistPMESrvcNameIdx = _PvxESrvcHistPMESrvcNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 2),
    _PvxESrvcHistPMESrvcNameIdx_Type()
)
pvxESrvcHistPMESrvcNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcHistPMESrvcNameIdx.setStatus("current")
_PvxESrvcHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxESrvcHistPMIntervalTypeIdx_Object = MibTableColumn
pvxESrvcHistPMIntervalTypeIdx = _PvxESrvcHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 3),
    _PvxESrvcHistPMIntervalTypeIdx_Type()
)
pvxESrvcHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcHistPMIntervalTypeIdx.setStatus("current")


class _PvxESrvcHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxESrvcHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxESrvcHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxESrvcHistPMIntervalIdx_Object = MibTableColumn
pvxESrvcHistPMIntervalIdx = _PvxESrvcHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 4),
    _PvxESrvcHistPMIntervalIdx_Type()
)
pvxESrvcHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcHistPMIntervalIdx.setStatus("current")
_PvxESrvcHistPMUASValue_Type = Unsigned32
_PvxESrvcHistPMUASValue_Object = MibTableColumn
pvxESrvcHistPMUASValue = _PvxESrvcHistPMUASValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 5),
    _PvxESrvcHistPMUASValue_Type()
)
pvxESrvcHistPMUASValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcHistPMUASValue.setStatus("current")
_PvxESrvcHistPMUASTimeStamp_Type = DateAndTime
_PvxESrvcHistPMUASTimeStamp_Object = MibTableColumn
pvxESrvcHistPMUASTimeStamp = _PvxESrvcHistPMUASTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 6),
    _PvxESrvcHistPMUASTimeStamp_Type()
)
pvxESrvcHistPMUASTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcHistPMUASTimeStamp.setStatus("current")
_PvxESrvcHistPMUASValidity_Type = PMValidity
_PvxESrvcHistPMUASValidity_Object = MibTableColumn
pvxESrvcHistPMUASValidity = _PvxESrvcHistPMUASValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 7),
    _PvxESrvcHistPMUASValidity_Type()
)
pvxESrvcHistPMUASValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcHistPMUASValidity.setStatus("current")
_PvxESrvcHistPMUASInitialize_Type = InitializeCmd
_PvxESrvcHistPMUASInitialize_Object = MibTableColumn
pvxESrvcHistPMUASInitialize = _PvxESrvcHistPMUASInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 41, 1, 8),
    _PvxESrvcHistPMUASInitialize_Type()
)
pvxESrvcHistPMUASInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcHistPMUASInitialize.setStatus("current")
_PvxESrvcBWPrflCrntPMTable_Object = MibTable
pvxESrvcBWPrflCrntPMTable = _PvxESrvcBWPrflCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42)
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMTable.setStatus("current")
_PvxESrvcBWPrflCrntPMEntry_Object = MibTableRow
pvxESrvcBWPrflCrntPMEntry = _PvxESrvcBWPrflCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1)
)
pvxESrvcBWPrflCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMESrvcNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPlcyNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMClsMapNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMDirectionIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMEntry.setStatus("current")


class _PvxESrvcBWPrflCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxESrvcBWPrflCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflCrntPMSwitchIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMSwitchIdx = _PvxESrvcBWPrflCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 1),
    _PvxESrvcBWPrflCrntPMSwitchIdx_Type()
)
pvxESrvcBWPrflCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMSwitchIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMShelfIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxESrvcBWPrflCrntPMShelfIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflCrntPMShelfIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMShelfIdx = _PvxESrvcBWPrflCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 2),
    _PvxESrvcBWPrflCrntPMShelfIdx_Type()
)
pvxESrvcBWPrflCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMShelfIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMSlotIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxESrvcBWPrflCrntPMSlotIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflCrntPMSlotIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMSlotIdx = _PvxESrvcBWPrflCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 3),
    _PvxESrvcBWPrflCrntPMSlotIdx_Type()
)
pvxESrvcBWPrflCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMSlotIdx.setStatus("current")
_PvxESrvcBWPrflCrntPMPortTypeIdx_Type = PvxPortType
_PvxESrvcBWPrflCrntPMPortTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMPortTypeIdx = _PvxESrvcBWPrflCrntPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 4),
    _PvxESrvcBWPrflCrntPMPortTypeIdx_Type()
)
pvxESrvcBWPrflCrntPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMPortTypeIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMPortIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflCrntPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxESrvcBWPrflCrntPMPortIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflCrntPMPortIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMPortIdx = _PvxESrvcBWPrflCrntPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 5),
    _PvxESrvcBWPrflCrntPMPortIdx_Type()
)
pvxESrvcBWPrflCrntPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMPortIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMESrvcNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflCrntPMESrvcNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflCrntPMESrvcNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflCrntPMESrvcNameIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMESrvcNameIdx = _PvxESrvcBWPrflCrntPMESrvcNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 6),
    _PvxESrvcBWPrflCrntPMESrvcNameIdx_Type()
)
pvxESrvcBWPrflCrntPMESrvcNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMESrvcNameIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMPlcyNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflCrntPMPlcyNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflCrntPMPlcyNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflCrntPMPlcyNameIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMPlcyNameIdx = _PvxESrvcBWPrflCrntPMPlcyNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 7),
    _PvxESrvcBWPrflCrntPMPlcyNameIdx_Type()
)
pvxESrvcBWPrflCrntPMPlcyNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMPlcyNameIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMClsMapNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflCrntPMClsMapNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflCrntPMClsMapNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflCrntPMClsMapNameIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMClsMapNameIdx = _PvxESrvcBWPrflCrntPMClsMapNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 8),
    _PvxESrvcBWPrflCrntPMClsMapNameIdx_Type()
)
pvxESrvcBWPrflCrntPMClsMapNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMClsMapNameIdx.setStatus("current")


class _PvxESrvcBWPrflCrntPMDirectionIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflCrntPMDirectionIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_PvxESrvcBWPrflCrntPMDirectionIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflCrntPMDirectionIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMDirectionIdx = _PvxESrvcBWPrflCrntPMDirectionIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 9),
    _PvxESrvcBWPrflCrntPMDirectionIdx_Type()
)
pvxESrvcBWPrflCrntPMDirectionIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMDirectionIdx.setStatus("current")
_PvxESrvcBWPrflCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxESrvcBWPrflCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflCrntPMIntervalTypeIdx = _PvxESrvcBWPrflCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 10),
    _PvxESrvcBWPrflCrntPMIntervalTypeIdx_Type()
)
pvxESrvcBWPrflCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMIntervalTypeIdx.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsTotalValue_Type = Unsigned64
_PvxESrvcBWPrflCrntPMOctetsTotalValue_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsTotalValue = _PvxESrvcBWPrflCrntPMOctetsTotalValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 11),
    _PvxESrvcBWPrflCrntPMOctetsTotalValue_Type()
)
pvxESrvcBWPrflCrntPMOctetsTotalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsTotalValue.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsTotalTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflCrntPMOctetsTotalTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsTotalTimeStamp = _PvxESrvcBWPrflCrntPMOctetsTotalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 12),
    _PvxESrvcBWPrflCrntPMOctetsTotalTimeStamp_Type()
)
pvxESrvcBWPrflCrntPMOctetsTotalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsTotalTimeStamp.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsTotalValidity_Type = PMValidity
_PvxESrvcBWPrflCrntPMOctetsTotalValidity_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsTotalValidity = _PvxESrvcBWPrflCrntPMOctetsTotalValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 13),
    _PvxESrvcBWPrflCrntPMOctetsTotalValidity_Type()
)
pvxESrvcBWPrflCrntPMOctetsTotalValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsTotalValidity.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsTotalInitialize_Type = InitializeCmd
_PvxESrvcBWPrflCrntPMOctetsTotalInitialize_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsTotalInitialize = _PvxESrvcBWPrflCrntPMOctetsTotalInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 14),
    _PvxESrvcBWPrflCrntPMOctetsTotalInitialize_Type()
)
pvxESrvcBWPrflCrntPMOctetsTotalInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsTotalInitialize.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsVltValue_Type = Unsigned64
_PvxESrvcBWPrflCrntPMOctetsVltValue_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsVltValue = _PvxESrvcBWPrflCrntPMOctetsVltValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 15),
    _PvxESrvcBWPrflCrntPMOctetsVltValue_Type()
)
pvxESrvcBWPrflCrntPMOctetsVltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsVltValue.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsVltTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflCrntPMOctetsVltTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsVltTimeStamp = _PvxESrvcBWPrflCrntPMOctetsVltTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 16),
    _PvxESrvcBWPrflCrntPMOctetsVltTimeStamp_Type()
)
pvxESrvcBWPrflCrntPMOctetsVltTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsVltTimeStamp.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsVltValidity_Type = PMValidity
_PvxESrvcBWPrflCrntPMOctetsVltValidity_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsVltValidity = _PvxESrvcBWPrflCrntPMOctetsVltValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 17),
    _PvxESrvcBWPrflCrntPMOctetsVltValidity_Type()
)
pvxESrvcBWPrflCrntPMOctetsVltValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsVltValidity.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsVltInitialize_Type = InitializeCmd
_PvxESrvcBWPrflCrntPMOctetsVltInitialize_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsVltInitialize = _PvxESrvcBWPrflCrntPMOctetsVltInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 18),
    _PvxESrvcBWPrflCrntPMOctetsVltInitialize_Type()
)
pvxESrvcBWPrflCrntPMOctetsVltInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsVltInitialize.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsCnfExcValue_Type = Unsigned64
_PvxESrvcBWPrflCrntPMOctetsCnfExcValue_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsCnfExcValue = _PvxESrvcBWPrflCrntPMOctetsCnfExcValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 19),
    _PvxESrvcBWPrflCrntPMOctetsCnfExcValue_Type()
)
pvxESrvcBWPrflCrntPMOctetsCnfExcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsCnfExcValue.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp = _PvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 20),
    _PvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp_Type()
)
pvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsCnfExcValidity_Type = PMValidity
_PvxESrvcBWPrflCrntPMOctetsCnfExcValidity_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsCnfExcValidity = _PvxESrvcBWPrflCrntPMOctetsCnfExcValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 21),
    _PvxESrvcBWPrflCrntPMOctetsCnfExcValidity_Type()
)
pvxESrvcBWPrflCrntPMOctetsCnfExcValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsCnfExcValidity.setStatus("current")
_PvxESrvcBWPrflCrntPMOctetsCnfExcInitialize_Type = InitializeCmd
_PvxESrvcBWPrflCrntPMOctetsCnfExcInitialize_Object = MibTableColumn
pvxESrvcBWPrflCrntPMOctetsCnfExcInitialize = _PvxESrvcBWPrflCrntPMOctetsCnfExcInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 22),
    _PvxESrvcBWPrflCrntPMOctetsCnfExcInitialize_Type()
)
pvxESrvcBWPrflCrntPMOctetsCnfExcInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMOctetsCnfExcInitialize.setStatus("current")
_PvxESrvcBWPrflCrntPMBDWUtlzValue_Type = FixedX100
_PvxESrvcBWPrflCrntPMBDWUtlzValue_Object = MibTableColumn
pvxESrvcBWPrflCrntPMBDWUtlzValue = _PvxESrvcBWPrflCrntPMBDWUtlzValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 23),
    _PvxESrvcBWPrflCrntPMBDWUtlzValue_Type()
)
pvxESrvcBWPrflCrntPMBDWUtlzValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMBDWUtlzValue.setStatus("current")
_PvxESrvcBWPrflCrntPMBDWUtlzTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflCrntPMBDWUtlzTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflCrntPMBDWUtlzTimeStamp = _PvxESrvcBWPrflCrntPMBDWUtlzTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 24),
    _PvxESrvcBWPrflCrntPMBDWUtlzTimeStamp_Type()
)
pvxESrvcBWPrflCrntPMBDWUtlzTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMBDWUtlzTimeStamp.setStatus("current")
_PvxESrvcBWPrflCrntPMBDWUtlzValidity_Type = PMValidity
_PvxESrvcBWPrflCrntPMBDWUtlzValidity_Object = MibTableColumn
pvxESrvcBWPrflCrntPMBDWUtlzValidity = _PvxESrvcBWPrflCrntPMBDWUtlzValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 25),
    _PvxESrvcBWPrflCrntPMBDWUtlzValidity_Type()
)
pvxESrvcBWPrflCrntPMBDWUtlzValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMBDWUtlzValidity.setStatus("current")
_PvxESrvcBWPrflCrntPMBDWUtlzInitialize_Type = InitializeCmd
_PvxESrvcBWPrflCrntPMBDWUtlzInitialize_Object = MibTableColumn
pvxESrvcBWPrflCrntPMBDWUtlzInitialize = _PvxESrvcBWPrflCrntPMBDWUtlzInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 42, 1, 26),
    _PvxESrvcBWPrflCrntPMBDWUtlzInitialize_Type()
)
pvxESrvcBWPrflCrntPMBDWUtlzInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflCrntPMBDWUtlzInitialize.setStatus("current")
_PvxESrvcBWPrflHistPMTable_Object = MibTable
pvxESrvcBWPrflHistPMTable = _PvxESrvcBWPrflHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43)
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMTable.setStatus("current")
_PvxESrvcBWPrflHistPMEntry_Object = MibTableRow
pvxESrvcBWPrflHistPMEntry = _PvxESrvcBWPrflHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1)
)
pvxESrvcBWPrflHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMESrvcNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMPlcyNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMClsMapNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMDirectionIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMEntry.setStatus("current")


class _PvxESrvcBWPrflHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxESrvcBWPrflHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMSwitchIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMSwitchIdx = _PvxESrvcBWPrflHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 1),
    _PvxESrvcBWPrflHistPMSwitchIdx_Type()
)
pvxESrvcBWPrflHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMSwitchIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMShelfIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxESrvcBWPrflHistPMShelfIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMShelfIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMShelfIdx = _PvxESrvcBWPrflHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 2),
    _PvxESrvcBWPrflHistPMShelfIdx_Type()
)
pvxESrvcBWPrflHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMShelfIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMSlotIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxESrvcBWPrflHistPMSlotIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMSlotIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMSlotIdx = _PvxESrvcBWPrflHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 3),
    _PvxESrvcBWPrflHistPMSlotIdx_Type()
)
pvxESrvcBWPrflHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMSlotIdx.setStatus("current")
_PvxESrvcBWPrflHistPMPortTypeIdx_Type = PvxPortType
_PvxESrvcBWPrflHistPMPortTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMPortTypeIdx = _PvxESrvcBWPrflHistPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 4),
    _PvxESrvcBWPrflHistPMPortTypeIdx_Type()
)
pvxESrvcBWPrflHistPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMPortTypeIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMPortIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxESrvcBWPrflHistPMPortIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMPortIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMPortIdx = _PvxESrvcBWPrflHistPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 5),
    _PvxESrvcBWPrflHistPMPortIdx_Type()
)
pvxESrvcBWPrflHistPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMPortIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMESrvcNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflHistPMESrvcNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflHistPMESrvcNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflHistPMESrvcNameIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMESrvcNameIdx = _PvxESrvcBWPrflHistPMESrvcNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 6),
    _PvxESrvcBWPrflHistPMESrvcNameIdx_Type()
)
pvxESrvcBWPrflHistPMESrvcNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMESrvcNameIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMPlcyNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflHistPMPlcyNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflHistPMPlcyNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflHistPMPlcyNameIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMPlcyNameIdx = _PvxESrvcBWPrflHistPMPlcyNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 7),
    _PvxESrvcBWPrflHistPMPlcyNameIdx_Type()
)
pvxESrvcBWPrflHistPMPlcyNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMPlcyNameIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMClsMapNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflHistPMClsMapNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflHistPMClsMapNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflHistPMClsMapNameIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMClsMapNameIdx = _PvxESrvcBWPrflHistPMClsMapNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 8),
    _PvxESrvcBWPrflHistPMClsMapNameIdx_Type()
)
pvxESrvcBWPrflHistPMClsMapNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMClsMapNameIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMDirectionIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMDirectionIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_PvxESrvcBWPrflHistPMDirectionIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMDirectionIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMDirectionIdx = _PvxESrvcBWPrflHistPMDirectionIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 9),
    _PvxESrvcBWPrflHistPMDirectionIdx_Type()
)
pvxESrvcBWPrflHistPMDirectionIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMDirectionIdx.setStatus("current")
_PvxESrvcBWPrflHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxESrvcBWPrflHistPMIntervalTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMIntervalTypeIdx = _PvxESrvcBWPrflHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 10),
    _PvxESrvcBWPrflHistPMIntervalTypeIdx_Type()
)
pvxESrvcBWPrflHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMIntervalTypeIdx.setStatus("current")


class _PvxESrvcBWPrflHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxESrvcBWPrflHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflHistPMIntervalIdx_Object = MibTableColumn
pvxESrvcBWPrflHistPMIntervalIdx = _PvxESrvcBWPrflHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 11),
    _PvxESrvcBWPrflHistPMIntervalIdx_Type()
)
pvxESrvcBWPrflHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMIntervalIdx.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsTotalValue_Type = Unsigned64
_PvxESrvcBWPrflHistPMOctetsTotalValue_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsTotalValue = _PvxESrvcBWPrflHistPMOctetsTotalValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 12),
    _PvxESrvcBWPrflHistPMOctetsTotalValue_Type()
)
pvxESrvcBWPrflHistPMOctetsTotalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsTotalValue.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsTotalTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflHistPMOctetsTotalTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsTotalTimeStamp = _PvxESrvcBWPrflHistPMOctetsTotalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 13),
    _PvxESrvcBWPrflHistPMOctetsTotalTimeStamp_Type()
)
pvxESrvcBWPrflHistPMOctetsTotalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsTotalTimeStamp.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsTotalValidity_Type = PMValidity
_PvxESrvcBWPrflHistPMOctetsTotalValidity_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsTotalValidity = _PvxESrvcBWPrflHistPMOctetsTotalValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 14),
    _PvxESrvcBWPrflHistPMOctetsTotalValidity_Type()
)
pvxESrvcBWPrflHistPMOctetsTotalValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsTotalValidity.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsTotalInitialize_Type = InitializeCmd
_PvxESrvcBWPrflHistPMOctetsTotalInitialize_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsTotalInitialize = _PvxESrvcBWPrflHistPMOctetsTotalInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 15),
    _PvxESrvcBWPrflHistPMOctetsTotalInitialize_Type()
)
pvxESrvcBWPrflHistPMOctetsTotalInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsTotalInitialize.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsVltValue_Type = Unsigned64
_PvxESrvcBWPrflHistPMOctetsVltValue_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsVltValue = _PvxESrvcBWPrflHistPMOctetsVltValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 16),
    _PvxESrvcBWPrflHistPMOctetsVltValue_Type()
)
pvxESrvcBWPrflHistPMOctetsVltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsVltValue.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsVltTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflHistPMOctetsVltTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsVltTimeStamp = _PvxESrvcBWPrflHistPMOctetsVltTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 17),
    _PvxESrvcBWPrflHistPMOctetsVltTimeStamp_Type()
)
pvxESrvcBWPrflHistPMOctetsVltTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsVltTimeStamp.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsVltValidity_Type = PMValidity
_PvxESrvcBWPrflHistPMOctetsVltValidity_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsVltValidity = _PvxESrvcBWPrflHistPMOctetsVltValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 18),
    _PvxESrvcBWPrflHistPMOctetsVltValidity_Type()
)
pvxESrvcBWPrflHistPMOctetsVltValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsVltValidity.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsVltInitialize_Type = InitializeCmd
_PvxESrvcBWPrflHistPMOctetsVltInitialize_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsVltInitialize = _PvxESrvcBWPrflHistPMOctetsVltInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 19),
    _PvxESrvcBWPrflHistPMOctetsVltInitialize_Type()
)
pvxESrvcBWPrflHistPMOctetsVltInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsVltInitialize.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsCnfExcValue_Type = Unsigned64
_PvxESrvcBWPrflHistPMOctetsCnfExcValue_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsCnfExcValue = _PvxESrvcBWPrflHistPMOctetsCnfExcValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 20),
    _PvxESrvcBWPrflHistPMOctetsCnfExcValue_Type()
)
pvxESrvcBWPrflHistPMOctetsCnfExcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsCnfExcValue.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp = _PvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 21),
    _PvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp_Type()
)
pvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsCnfExcValidity_Type = PMValidity
_PvxESrvcBWPrflHistPMOctetsCnfExcValidity_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsCnfExcValidity = _PvxESrvcBWPrflHistPMOctetsCnfExcValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 22),
    _PvxESrvcBWPrflHistPMOctetsCnfExcValidity_Type()
)
pvxESrvcBWPrflHistPMOctetsCnfExcValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsCnfExcValidity.setStatus("current")
_PvxESrvcBWPrflHistPMOctetsCnfExcInitialize_Type = InitializeCmd
_PvxESrvcBWPrflHistPMOctetsCnfExcInitialize_Object = MibTableColumn
pvxESrvcBWPrflHistPMOctetsCnfExcInitialize = _PvxESrvcBWPrflHistPMOctetsCnfExcInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 23),
    _PvxESrvcBWPrflHistPMOctetsCnfExcInitialize_Type()
)
pvxESrvcBWPrflHistPMOctetsCnfExcInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMOctetsCnfExcInitialize.setStatus("current")
_PvxESrvcBWPrflHistPMBDWUtlzValue_Type = FixedX100
_PvxESrvcBWPrflHistPMBDWUtlzValue_Object = MibTableColumn
pvxESrvcBWPrflHistPMBDWUtlzValue = _PvxESrvcBWPrflHistPMBDWUtlzValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 24),
    _PvxESrvcBWPrflHistPMBDWUtlzValue_Type()
)
pvxESrvcBWPrflHistPMBDWUtlzValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMBDWUtlzValue.setStatus("current")
_PvxESrvcBWPrflHistPMBDWUtlzTimeStamp_Type = DateAndTime
_PvxESrvcBWPrflHistPMBDWUtlzTimeStamp_Object = MibTableColumn
pvxESrvcBWPrflHistPMBDWUtlzTimeStamp = _PvxESrvcBWPrflHistPMBDWUtlzTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 25),
    _PvxESrvcBWPrflHistPMBDWUtlzTimeStamp_Type()
)
pvxESrvcBWPrflHistPMBDWUtlzTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMBDWUtlzTimeStamp.setStatus("current")
_PvxESrvcBWPrflHistPMBDWUtlzValidity_Type = PMValidity
_PvxESrvcBWPrflHistPMBDWUtlzValidity_Object = MibTableColumn
pvxESrvcBWPrflHistPMBDWUtlzValidity = _PvxESrvcBWPrflHistPMBDWUtlzValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 26),
    _PvxESrvcBWPrflHistPMBDWUtlzValidity_Type()
)
pvxESrvcBWPrflHistPMBDWUtlzValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMBDWUtlzValidity.setStatus("current")
_PvxESrvcBWPrflHistPMBDWUtlzInitialize_Type = InitializeCmd
_PvxESrvcBWPrflHistPMBDWUtlzInitialize_Object = MibTableColumn
pvxESrvcBWPrflHistPMBDWUtlzInitialize = _PvxESrvcBWPrflHistPMBDWUtlzInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 43, 1, 27),
    _PvxESrvcBWPrflHistPMBDWUtlzInitialize_Type()
)
pvxESrvcBWPrflHistPMBDWUtlzInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflHistPMBDWUtlzInitialize.setStatus("current")
_PvxESrvcBWPrflPMThresholdTable_Object = MibTable
pvxESrvcBWPrflPMThresholdTable = _PvxESrvcBWPrflPMThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44)
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdTable.setStatus("current")
_PvxESrvcBWPrflPMThresholdEntry_Object = MibTableRow
pvxESrvcBWPrflPMThresholdEntry = _PvxESrvcBWPrflPMThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1)
)
pvxESrvcBWPrflPMThresholdEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdESrvcNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdPlcyNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdClsMapNameIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdDirectionIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdLevelTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdEntry.setStatus("current")


class _PvxESrvcBWPrflPMThresholdSwitchIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflPMThresholdSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxESrvcBWPrflPMThresholdSwitchIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflPMThresholdSwitchIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdSwitchIdx = _PvxESrvcBWPrflPMThresholdSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 1),
    _PvxESrvcBWPrflPMThresholdSwitchIdx_Type()
)
pvxESrvcBWPrflPMThresholdSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdSwitchIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdShelfIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflPMThresholdShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxESrvcBWPrflPMThresholdShelfIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflPMThresholdShelfIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdShelfIdx = _PvxESrvcBWPrflPMThresholdShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 2),
    _PvxESrvcBWPrflPMThresholdShelfIdx_Type()
)
pvxESrvcBWPrflPMThresholdShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdShelfIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdSlotIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflPMThresholdSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxESrvcBWPrflPMThresholdSlotIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflPMThresholdSlotIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdSlotIdx = _PvxESrvcBWPrflPMThresholdSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 3),
    _PvxESrvcBWPrflPMThresholdSlotIdx_Type()
)
pvxESrvcBWPrflPMThresholdSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdSlotIdx.setStatus("current")
_PvxESrvcBWPrflPMThresholdPortTypeIdx_Type = PvxPortType
_PvxESrvcBWPrflPMThresholdPortTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdPortTypeIdx = _PvxESrvcBWPrflPMThresholdPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 4),
    _PvxESrvcBWPrflPMThresholdPortTypeIdx_Type()
)
pvxESrvcBWPrflPMThresholdPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdPortTypeIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdPortIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflPMThresholdPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxESrvcBWPrflPMThresholdPortIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflPMThresholdPortIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdPortIdx = _PvxESrvcBWPrflPMThresholdPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 5),
    _PvxESrvcBWPrflPMThresholdPortIdx_Type()
)
pvxESrvcBWPrflPMThresholdPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdPortIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdESrvcNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflPMThresholdESrvcNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflPMThresholdESrvcNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflPMThresholdESrvcNameIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdESrvcNameIdx = _PvxESrvcBWPrflPMThresholdESrvcNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 6),
    _PvxESrvcBWPrflPMThresholdESrvcNameIdx_Type()
)
pvxESrvcBWPrflPMThresholdESrvcNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdESrvcNameIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdPlcyNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflPMThresholdPlcyNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflPMThresholdPlcyNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflPMThresholdPlcyNameIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdPlcyNameIdx = _PvxESrvcBWPrflPMThresholdPlcyNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 7),
    _PvxESrvcBWPrflPMThresholdPlcyNameIdx_Type()
)
pvxESrvcBWPrflPMThresholdPlcyNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdPlcyNameIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdClsMapNameIdx_Type(DisplayString):
    """Custom type pvxESrvcBWPrflPMThresholdClsMapNameIdx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxESrvcBWPrflPMThresholdClsMapNameIdx_Type.__name__ = "DisplayString"
_PvxESrvcBWPrflPMThresholdClsMapNameIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdClsMapNameIdx = _PvxESrvcBWPrflPMThresholdClsMapNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 8),
    _PvxESrvcBWPrflPMThresholdClsMapNameIdx_Type()
)
pvxESrvcBWPrflPMThresholdClsMapNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdClsMapNameIdx.setStatus("current")


class _PvxESrvcBWPrflPMThresholdDirectionIdx_Type(Integer32):
    """Custom type pvxESrvcBWPrflPMThresholdDirectionIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_PvxESrvcBWPrflPMThresholdDirectionIdx_Type.__name__ = "Integer32"
_PvxESrvcBWPrflPMThresholdDirectionIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdDirectionIdx = _PvxESrvcBWPrflPMThresholdDirectionIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 9),
    _PvxESrvcBWPrflPMThresholdDirectionIdx_Type()
)
pvxESrvcBWPrflPMThresholdDirectionIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdDirectionIdx.setStatus("current")
_PvxESrvcBWPrflPMThresholdLevelTypeIdx_Type = PvxESrvcBWPrflPMThresholdLevelType
_PvxESrvcBWPrflPMThresholdLevelTypeIdx_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdLevelTypeIdx = _PvxESrvcBWPrflPMThresholdLevelTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 10),
    _PvxESrvcBWPrflPMThresholdLevelTypeIdx_Type()
)
pvxESrvcBWPrflPMThresholdLevelTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdLevelTypeIdx.setStatus("current")
_PvxESrvcBWPrflPMThresholdBDWUtlzValue_Type = FixedX100
_PvxESrvcBWPrflPMThresholdBDWUtlzValue_Object = MibTableColumn
pvxESrvcBWPrflPMThresholdBDWUtlzValue = _PvxESrvcBWPrflPMThresholdBDWUtlzValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 44, 1, 11),
    _PvxESrvcBWPrflPMThresholdBDWUtlzValue_Type()
)
pvxESrvcBWPrflPMThresholdBDWUtlzValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxESrvcBWPrflPMThresholdBDWUtlzValue.setStatus("current")
_PvxERPSPortCrntPMTable_Object = MibTable
pvxERPSPortCrntPMTable = _PvxERPSPortCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45)
)
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMTable.setStatus("current")
_PvxERPSPortCrntPMEntry_Object = MibTableRow
pvxERPSPortCrntPMEntry = _PvxERPSPortCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1)
)
pvxERPSPortCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEntry.setStatus("current")


class _PvxERPSPortCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxERPSPortCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxERPSPortCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxERPSPortCrntPMSwitchIdx_Object = MibTableColumn
pvxERPSPortCrntPMSwitchIdx = _PvxERPSPortCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 1),
    _PvxERPSPortCrntPMSwitchIdx_Type()
)
pvxERPSPortCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSwitchIdx.setStatus("current")


class _PvxERPSPortCrntPMShelfIdx_Type(Integer32):
    """Custom type pvxERPSPortCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxERPSPortCrntPMShelfIdx_Type.__name__ = "Integer32"
_PvxERPSPortCrntPMShelfIdx_Object = MibTableColumn
pvxERPSPortCrntPMShelfIdx = _PvxERPSPortCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 2),
    _PvxERPSPortCrntPMShelfIdx_Type()
)
pvxERPSPortCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMShelfIdx.setStatus("current")


class _PvxERPSPortCrntPMSlotIdx_Type(Integer32):
    """Custom type pvxERPSPortCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxERPSPortCrntPMSlotIdx_Type.__name__ = "Integer32"
_PvxERPSPortCrntPMSlotIdx_Object = MibTableColumn
pvxERPSPortCrntPMSlotIdx = _PvxERPSPortCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 3),
    _PvxERPSPortCrntPMSlotIdx_Type()
)
pvxERPSPortCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSlotIdx.setStatus("current")
_PvxERPSPortCrntPMTypeIdx_Type = PvxPortType
_PvxERPSPortCrntPMTypeIdx_Object = MibTableColumn
pvxERPSPortCrntPMTypeIdx = _PvxERPSPortCrntPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 4),
    _PvxERPSPortCrntPMTypeIdx_Type()
)
pvxERPSPortCrntPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMTypeIdx.setStatus("current")


class _PvxERPSPortCrntPMPortIdx_Type(Integer32):
    """Custom type pvxERPSPortCrntPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxERPSPortCrntPMPortIdx_Type.__name__ = "Integer32"
_PvxERPSPortCrntPMPortIdx_Object = MibTableColumn
pvxERPSPortCrntPMPortIdx = _PvxERPSPortCrntPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 5),
    _PvxERPSPortCrntPMPortIdx_Type()
)
pvxERPSPortCrntPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPortIdx.setStatus("current")
_PvxERPSPortCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxERPSPortCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxERPSPortCrntPMIntervalTypeIdx = _PvxERPSPortCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 6),
    _PvxERPSPortCrntPMIntervalTypeIdx_Type()
)
pvxERPSPortCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMIntervalTypeIdx.setStatus("current")
_PvxERPSPortCrntPMPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMPduTxValue = _PvxERPSPortCrntPMPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 7),
    _PvxERPSPortCrntPMPduTxValue_Type()
)
pvxERPSPortCrntPMPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduTxValue.setStatus("current")
_PvxERPSPortCrntPMPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMPduTxTimeStamp = _PvxERPSPortCrntPMPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 8),
    _PvxERPSPortCrntPMPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMPduTxValidity = _PvxERPSPortCrntPMPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 9),
    _PvxERPSPortCrntPMPduTxValidity_Type()
)
pvxERPSPortCrntPMPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMPduTxInitialize = _PvxERPSPortCrntPMPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 10),
    _PvxERPSPortCrntPMPduTxInitialize_Type()
)
pvxERPSPortCrntPMPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMPduRxValue = _PvxERPSPortCrntPMPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 11),
    _PvxERPSPortCrntPMPduRxValue_Type()
)
pvxERPSPortCrntPMPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduRxValue.setStatus("current")
_PvxERPSPortCrntPMPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMPduRxTimeStamp = _PvxERPSPortCrntPMPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 12),
    _PvxERPSPortCrntPMPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMPduRxValidity = _PvxERPSPortCrntPMPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 13),
    _PvxERPSPortCrntPMPduRxValidity_Type()
)
pvxERPSPortCrntPMPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMPduRxInitialize = _PvxERPSPortCrntPMPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 14),
    _PvxERPSPortCrntPMPduRxInitialize_Type()
)
pvxERPSPortCrntPMPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMPduDiscardValue_Type = Unsigned64
_PvxERPSPortCrntPMPduDiscardValue_Object = MibTableColumn
pvxERPSPortCrntPMPduDiscardValue = _PvxERPSPortCrntPMPduDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 15),
    _PvxERPSPortCrntPMPduDiscardValue_Type()
)
pvxERPSPortCrntPMPduDiscardValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduDiscardValue.setStatus("current")
_PvxERPSPortCrntPMPduDiscardTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMPduDiscardTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMPduDiscardTimeStamp = _PvxERPSPortCrntPMPduDiscardTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 16),
    _PvxERPSPortCrntPMPduDiscardTimeStamp_Type()
)
pvxERPSPortCrntPMPduDiscardTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduDiscardTimeStamp.setStatus("current")
_PvxERPSPortCrntPMPduDiscardValidity_Type = PMValidity
_PvxERPSPortCrntPMPduDiscardValidity_Object = MibTableColumn
pvxERPSPortCrntPMPduDiscardValidity = _PvxERPSPortCrntPMPduDiscardValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 17),
    _PvxERPSPortCrntPMPduDiscardValidity_Type()
)
pvxERPSPortCrntPMPduDiscardValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduDiscardValidity.setStatus("current")
_PvxERPSPortCrntPMPduDiscardInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMPduDiscardInitialize_Object = MibTableColumn
pvxERPSPortCrntPMPduDiscardInitialize = _PvxERPSPortCrntPMPduDiscardInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 18),
    _PvxERPSPortCrntPMPduDiscardInitialize_Type()
)
pvxERPSPortCrntPMPduDiscardInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMPduDiscardInitialize.setStatus("current")
_PvxERPSPortCrntPMBlockedValue_Type = Unsigned64
_PvxERPSPortCrntPMBlockedValue_Object = MibTableColumn
pvxERPSPortCrntPMBlockedValue = _PvxERPSPortCrntPMBlockedValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 19),
    _PvxERPSPortCrntPMBlockedValue_Type()
)
pvxERPSPortCrntPMBlockedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMBlockedValue.setStatus("current")
_PvxERPSPortCrntPMBlockedTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMBlockedTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMBlockedTimeStamp = _PvxERPSPortCrntPMBlockedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 20),
    _PvxERPSPortCrntPMBlockedTimeStamp_Type()
)
pvxERPSPortCrntPMBlockedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMBlockedTimeStamp.setStatus("current")
_PvxERPSPortCrntPMBlockedValidity_Type = PMValidity
_PvxERPSPortCrntPMBlockedValidity_Object = MibTableColumn
pvxERPSPortCrntPMBlockedValidity = _PvxERPSPortCrntPMBlockedValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 21),
    _PvxERPSPortCrntPMBlockedValidity_Type()
)
pvxERPSPortCrntPMBlockedValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMBlockedValidity.setStatus("current")
_PvxERPSPortCrntPMBlockedInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMBlockedInitialize_Object = MibTableColumn
pvxERPSPortCrntPMBlockedInitialize = _PvxERPSPortCrntPMBlockedInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 22),
    _PvxERPSPortCrntPMBlockedInitialize_Type()
)
pvxERPSPortCrntPMBlockedInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMBlockedInitialize.setStatus("current")
_PvxERPSPortCrntPMUnblockedValue_Type = Unsigned64
_PvxERPSPortCrntPMUnblockedValue_Object = MibTableColumn
pvxERPSPortCrntPMUnblockedValue = _PvxERPSPortCrntPMUnblockedValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 23),
    _PvxERPSPortCrntPMUnblockedValue_Type()
)
pvxERPSPortCrntPMUnblockedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMUnblockedValue.setStatus("current")
_PvxERPSPortCrntPMUnblockedTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMUnblockedTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMUnblockedTimeStamp = _PvxERPSPortCrntPMUnblockedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 24),
    _PvxERPSPortCrntPMUnblockedTimeStamp_Type()
)
pvxERPSPortCrntPMUnblockedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMUnblockedTimeStamp.setStatus("current")
_PvxERPSPortCrntPMUnblockedValidity_Type = PMValidity
_PvxERPSPortCrntPMUnblockedValidity_Object = MibTableColumn
pvxERPSPortCrntPMUnblockedValidity = _PvxERPSPortCrntPMUnblockedValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 25),
    _PvxERPSPortCrntPMUnblockedValidity_Type()
)
pvxERPSPortCrntPMUnblockedValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMUnblockedValidity.setStatus("current")
_PvxERPSPortCrntPMUnblockedInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMUnblockedInitialize_Object = MibTableColumn
pvxERPSPortCrntPMUnblockedInitialize = _PvxERPSPortCrntPMUnblockedInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 26),
    _PvxERPSPortCrntPMUnblockedInitialize_Type()
)
pvxERPSPortCrntPMUnblockedInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMUnblockedInitialize.setStatus("current")
_PvxERPSPortCrntPMFailuresValue_Type = Unsigned64
_PvxERPSPortCrntPMFailuresValue_Object = MibTableColumn
pvxERPSPortCrntPMFailuresValue = _PvxERPSPortCrntPMFailuresValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 27),
    _PvxERPSPortCrntPMFailuresValue_Type()
)
pvxERPSPortCrntPMFailuresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFailuresValue.setStatus("current")
_PvxERPSPortCrntPMFailuresTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMFailuresTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMFailuresTimeStamp = _PvxERPSPortCrntPMFailuresTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 28),
    _PvxERPSPortCrntPMFailuresTimeStamp_Type()
)
pvxERPSPortCrntPMFailuresTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFailuresTimeStamp.setStatus("current")
_PvxERPSPortCrntPMFailuresValidity_Type = PMValidity
_PvxERPSPortCrntPMFailuresValidity_Object = MibTableColumn
pvxERPSPortCrntPMFailuresValidity = _PvxERPSPortCrntPMFailuresValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 29),
    _PvxERPSPortCrntPMFailuresValidity_Type()
)
pvxERPSPortCrntPMFailuresValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFailuresValidity.setStatus("current")
_PvxERPSPortCrntPMFailuresInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMFailuresInitialize_Object = MibTableColumn
pvxERPSPortCrntPMFailuresInitialize = _PvxERPSPortCrntPMFailuresInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 30),
    _PvxERPSPortCrntPMFailuresInitialize_Type()
)
pvxERPSPortCrntPMFailuresInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFailuresInitialize.setStatus("current")
_PvxERPSPortCrntPMRecoveriesValue_Type = Unsigned64
_PvxERPSPortCrntPMRecoveriesValue_Object = MibTableColumn
pvxERPSPortCrntPMRecoveriesValue = _PvxERPSPortCrntPMRecoveriesValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 31),
    _PvxERPSPortCrntPMRecoveriesValue_Type()
)
pvxERPSPortCrntPMRecoveriesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMRecoveriesValue.setStatus("current")
_PvxERPSPortCrntPMRecoveriesTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMRecoveriesTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMRecoveriesTimeStamp = _PvxERPSPortCrntPMRecoveriesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 32),
    _PvxERPSPortCrntPMRecoveriesTimeStamp_Type()
)
pvxERPSPortCrntPMRecoveriesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMRecoveriesTimeStamp.setStatus("current")
_PvxERPSPortCrntPMRecoveriesValidity_Type = PMValidity
_PvxERPSPortCrntPMRecoveriesValidity_Object = MibTableColumn
pvxERPSPortCrntPMRecoveriesValidity = _PvxERPSPortCrntPMRecoveriesValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 33),
    _PvxERPSPortCrntPMRecoveriesValidity_Type()
)
pvxERPSPortCrntPMRecoveriesValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMRecoveriesValidity.setStatus("current")
_PvxERPSPortCrntPMRecoveriesInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMRecoveriesInitialize_Object = MibTableColumn
pvxERPSPortCrntPMRecoveriesInitialize = _PvxERPSPortCrntPMRecoveriesInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 34),
    _PvxERPSPortCrntPMRecoveriesInitialize_Type()
)
pvxERPSPortCrntPMRecoveriesInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMRecoveriesInitialize.setStatus("current")
_PvxERPSPortCrntPMNrPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMNrPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMNrPduTxValue = _PvxERPSPortCrntPMNrPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 35),
    _PvxERPSPortCrntPMNrPduTxValue_Type()
)
pvxERPSPortCrntPMNrPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduTxValue.setStatus("current")
_PvxERPSPortCrntPMNrPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMNrPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMNrPduTxTimeStamp = _PvxERPSPortCrntPMNrPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 36),
    _PvxERPSPortCrntPMNrPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMNrPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMNrPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMNrPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMNrPduTxValidity = _PvxERPSPortCrntPMNrPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 37),
    _PvxERPSPortCrntPMNrPduTxValidity_Type()
)
pvxERPSPortCrntPMNrPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMNrPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMNrPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMNrPduTxInitialize = _PvxERPSPortCrntPMNrPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 38),
    _PvxERPSPortCrntPMNrPduTxInitialize_Type()
)
pvxERPSPortCrntPMNrPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMNrPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMNrPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMNrPduRxValue = _PvxERPSPortCrntPMNrPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 39),
    _PvxERPSPortCrntPMNrPduRxValue_Type()
)
pvxERPSPortCrntPMNrPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduRxValue.setStatus("current")
_PvxERPSPortCrntPMNrPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMNrPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMNrPduRxTimeStamp = _PvxERPSPortCrntPMNrPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 40),
    _PvxERPSPortCrntPMNrPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMNrPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMNrPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMNrPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMNrPduRxValidity = _PvxERPSPortCrntPMNrPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 41),
    _PvxERPSPortCrntPMNrPduRxValidity_Type()
)
pvxERPSPortCrntPMNrPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMNrPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMNrPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMNrPduRxInitialize = _PvxERPSPortCrntPMNrPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 42),
    _PvxERPSPortCrntPMNrPduRxInitialize_Type()
)
pvxERPSPortCrntPMNrPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMNrrbPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMNrrbPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduTxValue = _PvxERPSPortCrntPMNrrbPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 43),
    _PvxERPSPortCrntPMNrrbPduTxValue_Type()
)
pvxERPSPortCrntPMNrrbPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduTxValue.setStatus("current")
_PvxERPSPortCrntPMNrrbPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMNrrbPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduTxTimeStamp = _PvxERPSPortCrntPMNrrbPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 44),
    _PvxERPSPortCrntPMNrrbPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMNrrbPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMNrrbPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMNrrbPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduTxValidity = _PvxERPSPortCrntPMNrrbPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 45),
    _PvxERPSPortCrntPMNrrbPduTxValidity_Type()
)
pvxERPSPortCrntPMNrrbPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMNrrbPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMNrrbPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduTxInitialize = _PvxERPSPortCrntPMNrrbPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 46),
    _PvxERPSPortCrntPMNrrbPduTxInitialize_Type()
)
pvxERPSPortCrntPMNrrbPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMNrrbPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMNrrbPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduRxValue = _PvxERPSPortCrntPMNrrbPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 47),
    _PvxERPSPortCrntPMNrrbPduRxValue_Type()
)
pvxERPSPortCrntPMNrrbPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduRxValue.setStatus("current")
_PvxERPSPortCrntPMNrrbPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMNrrbPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduRxTimeStamp = _PvxERPSPortCrntPMNrrbPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 48),
    _PvxERPSPortCrntPMNrrbPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMNrrbPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMNrrbPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMNrrbPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduRxValidity = _PvxERPSPortCrntPMNrrbPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 49),
    _PvxERPSPortCrntPMNrrbPduRxValidity_Type()
)
pvxERPSPortCrntPMNrrbPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMNrrbPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMNrrbPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMNrrbPduRxInitialize = _PvxERPSPortCrntPMNrrbPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 50),
    _PvxERPSPortCrntPMNrrbPduRxInitialize_Type()
)
pvxERPSPortCrntPMNrrbPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMNrrbPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMSfPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMSfPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMSfPduTxValue = _PvxERPSPortCrntPMSfPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 51),
    _PvxERPSPortCrntPMSfPduTxValue_Type()
)
pvxERPSPortCrntPMSfPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduTxValue.setStatus("current")
_PvxERPSPortCrntPMSfPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMSfPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMSfPduTxTimeStamp = _PvxERPSPortCrntPMSfPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 52),
    _PvxERPSPortCrntPMSfPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMSfPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMSfPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMSfPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMSfPduTxValidity = _PvxERPSPortCrntPMSfPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 53),
    _PvxERPSPortCrntPMSfPduTxValidity_Type()
)
pvxERPSPortCrntPMSfPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMSfPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMSfPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMSfPduTxInitialize = _PvxERPSPortCrntPMSfPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 54),
    _PvxERPSPortCrntPMSfPduTxInitialize_Type()
)
pvxERPSPortCrntPMSfPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMSfPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMSfPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMSfPduRxValue = _PvxERPSPortCrntPMSfPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 55),
    _PvxERPSPortCrntPMSfPduRxValue_Type()
)
pvxERPSPortCrntPMSfPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduRxValue.setStatus("current")
_PvxERPSPortCrntPMSfPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMSfPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMSfPduRxTimeStamp = _PvxERPSPortCrntPMSfPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 56),
    _PvxERPSPortCrntPMSfPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMSfPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMSfPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMSfPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMSfPduRxValidity = _PvxERPSPortCrntPMSfPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 57),
    _PvxERPSPortCrntPMSfPduRxValidity_Type()
)
pvxERPSPortCrntPMSfPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMSfPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMSfPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMSfPduRxInitialize = _PvxERPSPortCrntPMSfPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 58),
    _PvxERPSPortCrntPMSfPduRxInitialize_Type()
)
pvxERPSPortCrntPMSfPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMSfPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMFsPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMFsPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMFsPduTxValue = _PvxERPSPortCrntPMFsPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 59),
    _PvxERPSPortCrntPMFsPduTxValue_Type()
)
pvxERPSPortCrntPMFsPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduTxValue.setStatus("current")
_PvxERPSPortCrntPMFsPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMFsPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMFsPduTxTimeStamp = _PvxERPSPortCrntPMFsPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 60),
    _PvxERPSPortCrntPMFsPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMFsPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMFsPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMFsPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMFsPduTxValidity = _PvxERPSPortCrntPMFsPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 61),
    _PvxERPSPortCrntPMFsPduTxValidity_Type()
)
pvxERPSPortCrntPMFsPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMFsPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMFsPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMFsPduTxInitialize = _PvxERPSPortCrntPMFsPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 62),
    _PvxERPSPortCrntPMFsPduTxInitialize_Type()
)
pvxERPSPortCrntPMFsPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMFsPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMFsPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMFsPduRxValue = _PvxERPSPortCrntPMFsPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 63),
    _PvxERPSPortCrntPMFsPduRxValue_Type()
)
pvxERPSPortCrntPMFsPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduRxValue.setStatus("current")
_PvxERPSPortCrntPMFsPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMFsPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMFsPduRxTimeStamp = _PvxERPSPortCrntPMFsPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 64),
    _PvxERPSPortCrntPMFsPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMFsPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMFsPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMFsPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMFsPduRxValidity = _PvxERPSPortCrntPMFsPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 65),
    _PvxERPSPortCrntPMFsPduRxValidity_Type()
)
pvxERPSPortCrntPMFsPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMFsPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMFsPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMFsPduRxInitialize = _PvxERPSPortCrntPMFsPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 66),
    _PvxERPSPortCrntPMFsPduRxInitialize_Type()
)
pvxERPSPortCrntPMFsPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMFsPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMMsPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMMsPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMMsPduTxValue = _PvxERPSPortCrntPMMsPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 67),
    _PvxERPSPortCrntPMMsPduTxValue_Type()
)
pvxERPSPortCrntPMMsPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduTxValue.setStatus("current")
_PvxERPSPortCrntPMMsPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMMsPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMMsPduTxTimeStamp = _PvxERPSPortCrntPMMsPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 68),
    _PvxERPSPortCrntPMMsPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMMsPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMMsPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMMsPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMMsPduTxValidity = _PvxERPSPortCrntPMMsPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 69),
    _PvxERPSPortCrntPMMsPduTxValidity_Type()
)
pvxERPSPortCrntPMMsPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMMsPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMMsPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMMsPduTxInitialize = _PvxERPSPortCrntPMMsPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 70),
    _PvxERPSPortCrntPMMsPduTxInitialize_Type()
)
pvxERPSPortCrntPMMsPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMMsPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMMsPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMMsPduRxValue = _PvxERPSPortCrntPMMsPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 71),
    _PvxERPSPortCrntPMMsPduRxValue_Type()
)
pvxERPSPortCrntPMMsPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduRxValue.setStatus("current")
_PvxERPSPortCrntPMMsPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMMsPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMMsPduRxTimeStamp = _PvxERPSPortCrntPMMsPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 72),
    _PvxERPSPortCrntPMMsPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMMsPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMMsPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMMsPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMMsPduRxValidity = _PvxERPSPortCrntPMMsPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 73),
    _PvxERPSPortCrntPMMsPduRxValidity_Type()
)
pvxERPSPortCrntPMMsPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMMsPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMMsPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMMsPduRxInitialize = _PvxERPSPortCrntPMMsPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 74),
    _PvxERPSPortCrntPMMsPduRxInitialize_Type()
)
pvxERPSPortCrntPMMsPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMMsPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMEventPduTxValue_Type = Unsigned64
_PvxERPSPortCrntPMEventPduTxValue_Object = MibTableColumn
pvxERPSPortCrntPMEventPduTxValue = _PvxERPSPortCrntPMEventPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 75),
    _PvxERPSPortCrntPMEventPduTxValue_Type()
)
pvxERPSPortCrntPMEventPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduTxValue.setStatus("current")
_PvxERPSPortCrntPMEventPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMEventPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMEventPduTxTimeStamp = _PvxERPSPortCrntPMEventPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 76),
    _PvxERPSPortCrntPMEventPduTxTimeStamp_Type()
)
pvxERPSPortCrntPMEventPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduTxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMEventPduTxValidity_Type = PMValidity
_PvxERPSPortCrntPMEventPduTxValidity_Object = MibTableColumn
pvxERPSPortCrntPMEventPduTxValidity = _PvxERPSPortCrntPMEventPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 77),
    _PvxERPSPortCrntPMEventPduTxValidity_Type()
)
pvxERPSPortCrntPMEventPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduTxValidity.setStatus("current")
_PvxERPSPortCrntPMEventPduTxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMEventPduTxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMEventPduTxInitialize = _PvxERPSPortCrntPMEventPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 78),
    _PvxERPSPortCrntPMEventPduTxInitialize_Type()
)
pvxERPSPortCrntPMEventPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduTxInitialize.setStatus("current")
_PvxERPSPortCrntPMEventPduRxValue_Type = Unsigned64
_PvxERPSPortCrntPMEventPduRxValue_Object = MibTableColumn
pvxERPSPortCrntPMEventPduRxValue = _PvxERPSPortCrntPMEventPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 79),
    _PvxERPSPortCrntPMEventPduRxValue_Type()
)
pvxERPSPortCrntPMEventPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduRxValue.setStatus("current")
_PvxERPSPortCrntPMEventPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMEventPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMEventPduRxTimeStamp = _PvxERPSPortCrntPMEventPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 80),
    _PvxERPSPortCrntPMEventPduRxTimeStamp_Type()
)
pvxERPSPortCrntPMEventPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduRxTimeStamp.setStatus("current")
_PvxERPSPortCrntPMEventPduRxValidity_Type = PMValidity
_PvxERPSPortCrntPMEventPduRxValidity_Object = MibTableColumn
pvxERPSPortCrntPMEventPduRxValidity = _PvxERPSPortCrntPMEventPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 81),
    _PvxERPSPortCrntPMEventPduRxValidity_Type()
)
pvxERPSPortCrntPMEventPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduRxValidity.setStatus("current")
_PvxERPSPortCrntPMEventPduRxInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMEventPduRxInitialize_Object = MibTableColumn
pvxERPSPortCrntPMEventPduRxInitialize = _PvxERPSPortCrntPMEventPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 82),
    _PvxERPSPortCrntPMEventPduRxInitialize_Type()
)
pvxERPSPortCrntPMEventPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMEventPduRxInitialize.setStatus("current")
_PvxERPSPortCrntPMVersionDiscardValue_Type = Unsigned64
_PvxERPSPortCrntPMVersionDiscardValue_Object = MibTableColumn
pvxERPSPortCrntPMVersionDiscardValue = _PvxERPSPortCrntPMVersionDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 83),
    _PvxERPSPortCrntPMVersionDiscardValue_Type()
)
pvxERPSPortCrntPMVersionDiscardValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMVersionDiscardValue.setStatus("current")
_PvxERPSPortCrntPMVersionDiscardTimeStamp_Type = DateAndTime
_PvxERPSPortCrntPMVersionDiscardTimeStamp_Object = MibTableColumn
pvxERPSPortCrntPMVersionDiscardTimeStamp = _PvxERPSPortCrntPMVersionDiscardTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 84),
    _PvxERPSPortCrntPMVersionDiscardTimeStamp_Type()
)
pvxERPSPortCrntPMVersionDiscardTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMVersionDiscardTimeStamp.setStatus("current")
_PvxERPSPortCrntPMVersionDiscardValidity_Type = PMValidity
_PvxERPSPortCrntPMVersionDiscardValidity_Object = MibTableColumn
pvxERPSPortCrntPMVersionDiscardValidity = _PvxERPSPortCrntPMVersionDiscardValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 85),
    _PvxERPSPortCrntPMVersionDiscardValidity_Type()
)
pvxERPSPortCrntPMVersionDiscardValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMVersionDiscardValidity.setStatus("current")
_PvxERPSPortCrntPMVersionDiscardInitialize_Type = InitializeCmd
_PvxERPSPortCrntPMVersionDiscardInitialize_Object = MibTableColumn
pvxERPSPortCrntPMVersionDiscardInitialize = _PvxERPSPortCrntPMVersionDiscardInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 45, 1, 86),
    _PvxERPSPortCrntPMVersionDiscardInitialize_Type()
)
pvxERPSPortCrntPMVersionDiscardInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortCrntPMVersionDiscardInitialize.setStatus("current")
_PvxERPSPortHistPMTable_Object = MibTable
pvxERPSPortHistPMTable = _PvxERPSPortHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46)
)
if mibBuilder.loadTexts:
    pvxERPSPortHistPMTable.setStatus("current")
_PvxERPSPortHistPMEntry_Object = MibTableRow
pvxERPSPortHistPMEntry = _PvxERPSPortHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1)
)
pvxERPSPortHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSPortHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEntry.setStatus("current")


class _PvxERPSPortHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxERPSPortHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxERPSPortHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxERPSPortHistPMSwitchIdx_Object = MibTableColumn
pvxERPSPortHistPMSwitchIdx = _PvxERPSPortHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 1),
    _PvxERPSPortHistPMSwitchIdx_Type()
)
pvxERPSPortHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSwitchIdx.setStatus("current")


class _PvxERPSPortHistPMShelfIdx_Type(Integer32):
    """Custom type pvxERPSPortHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxERPSPortHistPMShelfIdx_Type.__name__ = "Integer32"
_PvxERPSPortHistPMShelfIdx_Object = MibTableColumn
pvxERPSPortHistPMShelfIdx = _PvxERPSPortHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 2),
    _PvxERPSPortHistPMShelfIdx_Type()
)
pvxERPSPortHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMShelfIdx.setStatus("current")


class _PvxERPSPortHistPMSlotIdx_Type(Integer32):
    """Custom type pvxERPSPortHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxERPSPortHistPMSlotIdx_Type.__name__ = "Integer32"
_PvxERPSPortHistPMSlotIdx_Object = MibTableColumn
pvxERPSPortHistPMSlotIdx = _PvxERPSPortHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 3),
    _PvxERPSPortHistPMSlotIdx_Type()
)
pvxERPSPortHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSlotIdx.setStatus("current")
_PvxERPSPortHistPMTypeIdx_Type = PvxPortType
_PvxERPSPortHistPMTypeIdx_Object = MibTableColumn
pvxERPSPortHistPMTypeIdx = _PvxERPSPortHistPMTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 4),
    _PvxERPSPortHistPMTypeIdx_Type()
)
pvxERPSPortHistPMTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMTypeIdx.setStatus("current")


class _PvxERPSPortHistPMPortIdx_Type(Integer32):
    """Custom type pvxERPSPortHistPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxERPSPortHistPMPortIdx_Type.__name__ = "Integer32"
_PvxERPSPortHistPMPortIdx_Object = MibTableColumn
pvxERPSPortHistPMPortIdx = _PvxERPSPortHistPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 5),
    _PvxERPSPortHistPMPortIdx_Type()
)
pvxERPSPortHistPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPortIdx.setStatus("current")
_PvxERPSPortHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxERPSPortHistPMIntervalTypeIdx_Object = MibTableColumn
pvxERPSPortHistPMIntervalTypeIdx = _PvxERPSPortHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 6),
    _PvxERPSPortHistPMIntervalTypeIdx_Type()
)
pvxERPSPortHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMIntervalTypeIdx.setStatus("current")


class _PvxERPSPortHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxERPSPortHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxERPSPortHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxERPSPortHistPMIntervalIdx_Object = MibTableColumn
pvxERPSPortHistPMIntervalIdx = _PvxERPSPortHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 7),
    _PvxERPSPortHistPMIntervalIdx_Type()
)
pvxERPSPortHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMIntervalIdx.setStatus("current")
_PvxERPSPortHistPMPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMPduTxValue = _PvxERPSPortHistPMPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 8),
    _PvxERPSPortHistPMPduTxValue_Type()
)
pvxERPSPortHistPMPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduTxValue.setStatus("current")
_PvxERPSPortHistPMPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMPduTxTimeStamp = _PvxERPSPortHistPMPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 9),
    _PvxERPSPortHistPMPduTxTimeStamp_Type()
)
pvxERPSPortHistPMPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMPduTxValidity = _PvxERPSPortHistPMPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 10),
    _PvxERPSPortHistPMPduTxValidity_Type()
)
pvxERPSPortHistPMPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduTxValidity.setStatus("current")
_PvxERPSPortHistPMPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMPduTxInitialize = _PvxERPSPortHistPMPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 11),
    _PvxERPSPortHistPMPduTxInitialize_Type()
)
pvxERPSPortHistPMPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMPduRxValue = _PvxERPSPortHistPMPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 12),
    _PvxERPSPortHistPMPduRxValue_Type()
)
pvxERPSPortHistPMPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduRxValue.setStatus("current")
_PvxERPSPortHistPMPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMPduRxTimeStamp = _PvxERPSPortHistPMPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 13),
    _PvxERPSPortHistPMPduRxTimeStamp_Type()
)
pvxERPSPortHistPMPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMPduRxValidity = _PvxERPSPortHistPMPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 14),
    _PvxERPSPortHistPMPduRxValidity_Type()
)
pvxERPSPortHistPMPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduRxValidity.setStatus("current")
_PvxERPSPortHistPMPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMPduRxInitialize = _PvxERPSPortHistPMPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 15),
    _PvxERPSPortHistPMPduRxInitialize_Type()
)
pvxERPSPortHistPMPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMPduDiscardValue_Type = Unsigned64
_PvxERPSPortHistPMPduDiscardValue_Object = MibTableColumn
pvxERPSPortHistPMPduDiscardValue = _PvxERPSPortHistPMPduDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 16),
    _PvxERPSPortHistPMPduDiscardValue_Type()
)
pvxERPSPortHistPMPduDiscardValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduDiscardValue.setStatus("current")
_PvxERPSPortHistPMPduDiscardTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMPduDiscardTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMPduDiscardTimeStamp = _PvxERPSPortHistPMPduDiscardTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 17),
    _PvxERPSPortHistPMPduDiscardTimeStamp_Type()
)
pvxERPSPortHistPMPduDiscardTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduDiscardTimeStamp.setStatus("current")
_PvxERPSPortHistPMPduDiscardValidity_Type = PMValidity
_PvxERPSPortHistPMPduDiscardValidity_Object = MibTableColumn
pvxERPSPortHistPMPduDiscardValidity = _PvxERPSPortHistPMPduDiscardValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 18),
    _PvxERPSPortHistPMPduDiscardValidity_Type()
)
pvxERPSPortHistPMPduDiscardValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduDiscardValidity.setStatus("current")
_PvxERPSPortHistPMPduDiscardInitialize_Type = InitializeCmd
_PvxERPSPortHistPMPduDiscardInitialize_Object = MibTableColumn
pvxERPSPortHistPMPduDiscardInitialize = _PvxERPSPortHistPMPduDiscardInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 19),
    _PvxERPSPortHistPMPduDiscardInitialize_Type()
)
pvxERPSPortHistPMPduDiscardInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMPduDiscardInitialize.setStatus("current")
_PvxERPSPortHistPMBlockedValue_Type = Unsigned64
_PvxERPSPortHistPMBlockedValue_Object = MibTableColumn
pvxERPSPortHistPMBlockedValue = _PvxERPSPortHistPMBlockedValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 20),
    _PvxERPSPortHistPMBlockedValue_Type()
)
pvxERPSPortHistPMBlockedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMBlockedValue.setStatus("current")
_PvxERPSPortHistPMBlockedTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMBlockedTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMBlockedTimeStamp = _PvxERPSPortHistPMBlockedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 21),
    _PvxERPSPortHistPMBlockedTimeStamp_Type()
)
pvxERPSPortHistPMBlockedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMBlockedTimeStamp.setStatus("current")
_PvxERPSPortHistPMBlockedValidity_Type = PMValidity
_PvxERPSPortHistPMBlockedValidity_Object = MibTableColumn
pvxERPSPortHistPMBlockedValidity = _PvxERPSPortHistPMBlockedValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 22),
    _PvxERPSPortHistPMBlockedValidity_Type()
)
pvxERPSPortHistPMBlockedValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMBlockedValidity.setStatus("current")
_PvxERPSPortHistPMBlockedInitialize_Type = InitializeCmd
_PvxERPSPortHistPMBlockedInitialize_Object = MibTableColumn
pvxERPSPortHistPMBlockedInitialize = _PvxERPSPortHistPMBlockedInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 23),
    _PvxERPSPortHistPMBlockedInitialize_Type()
)
pvxERPSPortHistPMBlockedInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMBlockedInitialize.setStatus("current")
_PvxERPSPortHistPMUnblockedValue_Type = Unsigned64
_PvxERPSPortHistPMUnblockedValue_Object = MibTableColumn
pvxERPSPortHistPMUnblockedValue = _PvxERPSPortHistPMUnblockedValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 24),
    _PvxERPSPortHistPMUnblockedValue_Type()
)
pvxERPSPortHistPMUnblockedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMUnblockedValue.setStatus("current")
_PvxERPSPortHistPMUnblockedTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMUnblockedTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMUnblockedTimeStamp = _PvxERPSPortHistPMUnblockedTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 25),
    _PvxERPSPortHistPMUnblockedTimeStamp_Type()
)
pvxERPSPortHistPMUnblockedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMUnblockedTimeStamp.setStatus("current")
_PvxERPSPortHistPMUnblockedValidity_Type = PMValidity
_PvxERPSPortHistPMUnblockedValidity_Object = MibTableColumn
pvxERPSPortHistPMUnblockedValidity = _PvxERPSPortHistPMUnblockedValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 26),
    _PvxERPSPortHistPMUnblockedValidity_Type()
)
pvxERPSPortHistPMUnblockedValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMUnblockedValidity.setStatus("current")
_PvxERPSPortHistPMUnblockedInitialize_Type = InitializeCmd
_PvxERPSPortHistPMUnblockedInitialize_Object = MibTableColumn
pvxERPSPortHistPMUnblockedInitialize = _PvxERPSPortHistPMUnblockedInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 27),
    _PvxERPSPortHistPMUnblockedInitialize_Type()
)
pvxERPSPortHistPMUnblockedInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMUnblockedInitialize.setStatus("current")
_PvxERPSPortHistPMFailuresValue_Type = Unsigned64
_PvxERPSPortHistPMFailuresValue_Object = MibTableColumn
pvxERPSPortHistPMFailuresValue = _PvxERPSPortHistPMFailuresValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 28),
    _PvxERPSPortHistPMFailuresValue_Type()
)
pvxERPSPortHistPMFailuresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFailuresValue.setStatus("current")
_PvxERPSPortHistPMFailuresTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMFailuresTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMFailuresTimeStamp = _PvxERPSPortHistPMFailuresTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 29),
    _PvxERPSPortHistPMFailuresTimeStamp_Type()
)
pvxERPSPortHistPMFailuresTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFailuresTimeStamp.setStatus("current")
_PvxERPSPortHistPMFailuresValidity_Type = PMValidity
_PvxERPSPortHistPMFailuresValidity_Object = MibTableColumn
pvxERPSPortHistPMFailuresValidity = _PvxERPSPortHistPMFailuresValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 30),
    _PvxERPSPortHistPMFailuresValidity_Type()
)
pvxERPSPortHistPMFailuresValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFailuresValidity.setStatus("current")
_PvxERPSPortHistPMFailuresInitialize_Type = InitializeCmd
_PvxERPSPortHistPMFailuresInitialize_Object = MibTableColumn
pvxERPSPortHistPMFailuresInitialize = _PvxERPSPortHistPMFailuresInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 31),
    _PvxERPSPortHistPMFailuresInitialize_Type()
)
pvxERPSPortHistPMFailuresInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFailuresInitialize.setStatus("current")
_PvxERPSPortHistPMRecoveriesValue_Type = Unsigned64
_PvxERPSPortHistPMRecoveriesValue_Object = MibTableColumn
pvxERPSPortHistPMRecoveriesValue = _PvxERPSPortHistPMRecoveriesValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 32),
    _PvxERPSPortHistPMRecoveriesValue_Type()
)
pvxERPSPortHistPMRecoveriesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMRecoveriesValue.setStatus("current")
_PvxERPSPortHistPMRecoveriesTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMRecoveriesTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMRecoveriesTimeStamp = _PvxERPSPortHistPMRecoveriesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 33),
    _PvxERPSPortHistPMRecoveriesTimeStamp_Type()
)
pvxERPSPortHistPMRecoveriesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMRecoveriesTimeStamp.setStatus("current")
_PvxERPSPortHistPMRecoveriesValidity_Type = PMValidity
_PvxERPSPortHistPMRecoveriesValidity_Object = MibTableColumn
pvxERPSPortHistPMRecoveriesValidity = _PvxERPSPortHistPMRecoveriesValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 34),
    _PvxERPSPortHistPMRecoveriesValidity_Type()
)
pvxERPSPortHistPMRecoveriesValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMRecoveriesValidity.setStatus("current")
_PvxERPSPortHistPMRecoveriesInitialize_Type = InitializeCmd
_PvxERPSPortHistPMRecoveriesInitialize_Object = MibTableColumn
pvxERPSPortHistPMRecoveriesInitialize = _PvxERPSPortHistPMRecoveriesInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 35),
    _PvxERPSPortHistPMRecoveriesInitialize_Type()
)
pvxERPSPortHistPMRecoveriesInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMRecoveriesInitialize.setStatus("current")
_PvxERPSPortHistPMNrPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMNrPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMNrPduTxValue = _PvxERPSPortHistPMNrPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 36),
    _PvxERPSPortHistPMNrPduTxValue_Type()
)
pvxERPSPortHistPMNrPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduTxValue.setStatus("current")
_PvxERPSPortHistPMNrPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMNrPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMNrPduTxTimeStamp = _PvxERPSPortHistPMNrPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 37),
    _PvxERPSPortHistPMNrPduTxTimeStamp_Type()
)
pvxERPSPortHistPMNrPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMNrPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMNrPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMNrPduTxValidity = _PvxERPSPortHistPMNrPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 38),
    _PvxERPSPortHistPMNrPduTxValidity_Type()
)
pvxERPSPortHistPMNrPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduTxValidity.setStatus("current")
_PvxERPSPortHistPMNrPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMNrPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMNrPduTxInitialize = _PvxERPSPortHistPMNrPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 39),
    _PvxERPSPortHistPMNrPduTxInitialize_Type()
)
pvxERPSPortHistPMNrPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMNrPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMNrPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMNrPduRxValue = _PvxERPSPortHistPMNrPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 40),
    _PvxERPSPortHistPMNrPduRxValue_Type()
)
pvxERPSPortHistPMNrPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduRxValue.setStatus("current")
_PvxERPSPortHistPMNrPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMNrPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMNrPduRxTimeStamp = _PvxERPSPortHistPMNrPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 41),
    _PvxERPSPortHistPMNrPduRxTimeStamp_Type()
)
pvxERPSPortHistPMNrPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMNrPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMNrPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMNrPduRxValidity = _PvxERPSPortHistPMNrPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 42),
    _PvxERPSPortHistPMNrPduRxValidity_Type()
)
pvxERPSPortHistPMNrPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduRxValidity.setStatus("current")
_PvxERPSPortHistPMNrPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMNrPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMNrPduRxInitialize = _PvxERPSPortHistPMNrPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 43),
    _PvxERPSPortHistPMNrPduRxInitialize_Type()
)
pvxERPSPortHistPMNrPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMNrrbPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMNrrbPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduTxValue = _PvxERPSPortHistPMNrrbPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 44),
    _PvxERPSPortHistPMNrrbPduTxValue_Type()
)
pvxERPSPortHistPMNrrbPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduTxValue.setStatus("current")
_PvxERPSPortHistPMNrrbPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMNrrbPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduTxTimeStamp = _PvxERPSPortHistPMNrrbPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 45),
    _PvxERPSPortHistPMNrrbPduTxTimeStamp_Type()
)
pvxERPSPortHistPMNrrbPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMNrrbPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMNrrbPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduTxValidity = _PvxERPSPortHistPMNrrbPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 46),
    _PvxERPSPortHistPMNrrbPduTxValidity_Type()
)
pvxERPSPortHistPMNrrbPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduTxValidity.setStatus("current")
_PvxERPSPortHistPMNrrbPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMNrrbPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduTxInitialize = _PvxERPSPortHistPMNrrbPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 47),
    _PvxERPSPortHistPMNrrbPduTxInitialize_Type()
)
pvxERPSPortHistPMNrrbPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMNrrbPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMNrrbPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduRxValue = _PvxERPSPortHistPMNrrbPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 48),
    _PvxERPSPortHistPMNrrbPduRxValue_Type()
)
pvxERPSPortHistPMNrrbPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduRxValue.setStatus("current")
_PvxERPSPortHistPMNrrbPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMNrrbPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduRxTimeStamp = _PvxERPSPortHistPMNrrbPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 49),
    _PvxERPSPortHistPMNrrbPduRxTimeStamp_Type()
)
pvxERPSPortHistPMNrrbPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMNrrbPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMNrrbPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduRxValidity = _PvxERPSPortHistPMNrrbPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 50),
    _PvxERPSPortHistPMNrrbPduRxValidity_Type()
)
pvxERPSPortHistPMNrrbPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduRxValidity.setStatus("current")
_PvxERPSPortHistPMNrrbPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMNrrbPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMNrrbPduRxInitialize = _PvxERPSPortHistPMNrrbPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 51),
    _PvxERPSPortHistPMNrrbPduRxInitialize_Type()
)
pvxERPSPortHistPMNrrbPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMNrrbPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMSfPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMSfPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMSfPduTxValue = _PvxERPSPortHistPMSfPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 52),
    _PvxERPSPortHistPMSfPduTxValue_Type()
)
pvxERPSPortHistPMSfPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduTxValue.setStatus("current")
_PvxERPSPortHistPMSfPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMSfPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMSfPduTxTimeStamp = _PvxERPSPortHistPMSfPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 53),
    _PvxERPSPortHistPMSfPduTxTimeStamp_Type()
)
pvxERPSPortHistPMSfPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMSfPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMSfPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMSfPduTxValidity = _PvxERPSPortHistPMSfPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 54),
    _PvxERPSPortHistPMSfPduTxValidity_Type()
)
pvxERPSPortHistPMSfPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduTxValidity.setStatus("current")
_PvxERPSPortHistPMSfPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMSfPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMSfPduTxInitialize = _PvxERPSPortHistPMSfPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 55),
    _PvxERPSPortHistPMSfPduTxInitialize_Type()
)
pvxERPSPortHistPMSfPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMSfPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMSfPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMSfPduRxValue = _PvxERPSPortHistPMSfPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 56),
    _PvxERPSPortHistPMSfPduRxValue_Type()
)
pvxERPSPortHistPMSfPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduRxValue.setStatus("current")
_PvxERPSPortHistPMSfPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMSfPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMSfPduRxTimeStamp = _PvxERPSPortHistPMSfPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 57),
    _PvxERPSPortHistPMSfPduRxTimeStamp_Type()
)
pvxERPSPortHistPMSfPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMSfPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMSfPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMSfPduRxValidity = _PvxERPSPortHistPMSfPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 58),
    _PvxERPSPortHistPMSfPduRxValidity_Type()
)
pvxERPSPortHistPMSfPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduRxValidity.setStatus("current")
_PvxERPSPortHistPMSfPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMSfPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMSfPduRxInitialize = _PvxERPSPortHistPMSfPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 59),
    _PvxERPSPortHistPMSfPduRxInitialize_Type()
)
pvxERPSPortHistPMSfPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMSfPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMFsPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMFsPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMFsPduTxValue = _PvxERPSPortHistPMFsPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 60),
    _PvxERPSPortHistPMFsPduTxValue_Type()
)
pvxERPSPortHistPMFsPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduTxValue.setStatus("current")
_PvxERPSPortHistPMFsPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMFsPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMFsPduTxTimeStamp = _PvxERPSPortHistPMFsPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 61),
    _PvxERPSPortHistPMFsPduTxTimeStamp_Type()
)
pvxERPSPortHistPMFsPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMFsPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMFsPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMFsPduTxValidity = _PvxERPSPortHistPMFsPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 62),
    _PvxERPSPortHistPMFsPduTxValidity_Type()
)
pvxERPSPortHistPMFsPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduTxValidity.setStatus("current")
_PvxERPSPortHistPMFsPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMFsPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMFsPduTxInitialize = _PvxERPSPortHistPMFsPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 63),
    _PvxERPSPortHistPMFsPduTxInitialize_Type()
)
pvxERPSPortHistPMFsPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMFsPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMFsPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMFsPduRxValue = _PvxERPSPortHistPMFsPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 64),
    _PvxERPSPortHistPMFsPduRxValue_Type()
)
pvxERPSPortHistPMFsPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduRxValue.setStatus("current")
_PvxERPSPortHistPMFsPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMFsPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMFsPduRxTimeStamp = _PvxERPSPortHistPMFsPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 65),
    _PvxERPSPortHistPMFsPduRxTimeStamp_Type()
)
pvxERPSPortHistPMFsPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMFsPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMFsPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMFsPduRxValidity = _PvxERPSPortHistPMFsPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 66),
    _PvxERPSPortHistPMFsPduRxValidity_Type()
)
pvxERPSPortHistPMFsPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduRxValidity.setStatus("current")
_PvxERPSPortHistPMFsPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMFsPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMFsPduRxInitialize = _PvxERPSPortHistPMFsPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 67),
    _PvxERPSPortHistPMFsPduRxInitialize_Type()
)
pvxERPSPortHistPMFsPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMFsPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMMsPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMMsPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMMsPduTxValue = _PvxERPSPortHistPMMsPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 68),
    _PvxERPSPortHistPMMsPduTxValue_Type()
)
pvxERPSPortHistPMMsPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduTxValue.setStatus("current")
_PvxERPSPortHistPMMsPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMMsPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMMsPduTxTimeStamp = _PvxERPSPortHistPMMsPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 69),
    _PvxERPSPortHistPMMsPduTxTimeStamp_Type()
)
pvxERPSPortHistPMMsPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMMsPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMMsPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMMsPduTxValidity = _PvxERPSPortHistPMMsPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 70),
    _PvxERPSPortHistPMMsPduTxValidity_Type()
)
pvxERPSPortHistPMMsPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduTxValidity.setStatus("current")
_PvxERPSPortHistPMMsPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMMsPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMMsPduTxInitialize = _PvxERPSPortHistPMMsPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 71),
    _PvxERPSPortHistPMMsPduTxInitialize_Type()
)
pvxERPSPortHistPMMsPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMMsPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMMsPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMMsPduRxValue = _PvxERPSPortHistPMMsPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 72),
    _PvxERPSPortHistPMMsPduRxValue_Type()
)
pvxERPSPortHistPMMsPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduRxValue.setStatus("current")
_PvxERPSPortHistPMMsPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMMsPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMMsPduRxTimeStamp = _PvxERPSPortHistPMMsPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 73),
    _PvxERPSPortHistPMMsPduRxTimeStamp_Type()
)
pvxERPSPortHistPMMsPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMMsPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMMsPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMMsPduRxValidity = _PvxERPSPortHistPMMsPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 74),
    _PvxERPSPortHistPMMsPduRxValidity_Type()
)
pvxERPSPortHistPMMsPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduRxValidity.setStatus("current")
_PvxERPSPortHistPMMsPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMMsPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMMsPduRxInitialize = _PvxERPSPortHistPMMsPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 75),
    _PvxERPSPortHistPMMsPduRxInitialize_Type()
)
pvxERPSPortHistPMMsPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMMsPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMEventPduTxValue_Type = Unsigned64
_PvxERPSPortHistPMEventPduTxValue_Object = MibTableColumn
pvxERPSPortHistPMEventPduTxValue = _PvxERPSPortHistPMEventPduTxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 76),
    _PvxERPSPortHistPMEventPduTxValue_Type()
)
pvxERPSPortHistPMEventPduTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduTxValue.setStatus("current")
_PvxERPSPortHistPMEventPduTxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMEventPduTxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMEventPduTxTimeStamp = _PvxERPSPortHistPMEventPduTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 77),
    _PvxERPSPortHistPMEventPduTxTimeStamp_Type()
)
pvxERPSPortHistPMEventPduTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduTxTimeStamp.setStatus("current")
_PvxERPSPortHistPMEventPduTxValidity_Type = PMValidity
_PvxERPSPortHistPMEventPduTxValidity_Object = MibTableColumn
pvxERPSPortHistPMEventPduTxValidity = _PvxERPSPortHistPMEventPduTxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 78),
    _PvxERPSPortHistPMEventPduTxValidity_Type()
)
pvxERPSPortHistPMEventPduTxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduTxValidity.setStatus("current")
_PvxERPSPortHistPMEventPduTxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMEventPduTxInitialize_Object = MibTableColumn
pvxERPSPortHistPMEventPduTxInitialize = _PvxERPSPortHistPMEventPduTxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 79),
    _PvxERPSPortHistPMEventPduTxInitialize_Type()
)
pvxERPSPortHistPMEventPduTxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduTxInitialize.setStatus("current")
_PvxERPSPortHistPMEventPduRxValue_Type = Unsigned64
_PvxERPSPortHistPMEventPduRxValue_Object = MibTableColumn
pvxERPSPortHistPMEventPduRxValue = _PvxERPSPortHistPMEventPduRxValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 80),
    _PvxERPSPortHistPMEventPduRxValue_Type()
)
pvxERPSPortHistPMEventPduRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduRxValue.setStatus("current")
_PvxERPSPortHistPMEventPduRxTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMEventPduRxTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMEventPduRxTimeStamp = _PvxERPSPortHistPMEventPduRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 81),
    _PvxERPSPortHistPMEventPduRxTimeStamp_Type()
)
pvxERPSPortHistPMEventPduRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduRxTimeStamp.setStatus("current")
_PvxERPSPortHistPMEventPduRxValidity_Type = PMValidity
_PvxERPSPortHistPMEventPduRxValidity_Object = MibTableColumn
pvxERPSPortHistPMEventPduRxValidity = _PvxERPSPortHistPMEventPduRxValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 82),
    _PvxERPSPortHistPMEventPduRxValidity_Type()
)
pvxERPSPortHistPMEventPduRxValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduRxValidity.setStatus("current")
_PvxERPSPortHistPMEventPduRxInitialize_Type = InitializeCmd
_PvxERPSPortHistPMEventPduRxInitialize_Object = MibTableColumn
pvxERPSPortHistPMEventPduRxInitialize = _PvxERPSPortHistPMEventPduRxInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 83),
    _PvxERPSPortHistPMEventPduRxInitialize_Type()
)
pvxERPSPortHistPMEventPduRxInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMEventPduRxInitialize.setStatus("current")
_PvxERPSPortHistPMVersionDiscardValue_Type = Unsigned64
_PvxERPSPortHistPMVersionDiscardValue_Object = MibTableColumn
pvxERPSPortHistPMVersionDiscardValue = _PvxERPSPortHistPMVersionDiscardValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 84),
    _PvxERPSPortHistPMVersionDiscardValue_Type()
)
pvxERPSPortHistPMVersionDiscardValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMVersionDiscardValue.setStatus("current")
_PvxERPSPortHistPMVersionDiscardTimeStamp_Type = DateAndTime
_PvxERPSPortHistPMVersionDiscardTimeStamp_Object = MibTableColumn
pvxERPSPortHistPMVersionDiscardTimeStamp = _PvxERPSPortHistPMVersionDiscardTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 85),
    _PvxERPSPortHistPMVersionDiscardTimeStamp_Type()
)
pvxERPSPortHistPMVersionDiscardTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMVersionDiscardTimeStamp.setStatus("current")
_PvxERPSPortHistPMVersionDiscardValidity_Type = PMValidity
_PvxERPSPortHistPMVersionDiscardValidity_Object = MibTableColumn
pvxERPSPortHistPMVersionDiscardValidity = _PvxERPSPortHistPMVersionDiscardValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 86),
    _PvxERPSPortHistPMVersionDiscardValidity_Type()
)
pvxERPSPortHistPMVersionDiscardValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMVersionDiscardValidity.setStatus("current")
_PvxERPSPortHistPMVersionDiscardInitialize_Type = InitializeCmd
_PvxERPSPortHistPMVersionDiscardInitialize_Object = MibTableColumn
pvxERPSPortHistPMVersionDiscardInitialize = _PvxERPSPortHistPMVersionDiscardInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 46, 1, 87),
    _PvxERPSPortHistPMVersionDiscardInitialize_Type()
)
pvxERPSPortHistPMVersionDiscardInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSPortHistPMVersionDiscardInitialize.setStatus("current")
_PvxEServiceSlaCrntPMTable_Object = MibTable
pvxEServiceSlaCrntPMTable = _PvxEServiceSlaCrntPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47)
)
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMTable.setStatus("current")
_PvxEServiceSlaCrntPMEntry_Object = MibTableRow
pvxEServiceSlaCrntPMEntry = _PvxEServiceSlaCrntPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1)
)
pvxEServiceSlaCrntPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMESName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMRMepId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMIntervalTypeIdx"),
)
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMEntry.setStatus("current")


class _PvxEServiceSlaCrntPMSwitchIdx_Type(Integer32):
    """Custom type pvxEServiceSlaCrntPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEServiceSlaCrntPMSwitchIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaCrntPMSwitchIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMSwitchIdx = _PvxEServiceSlaCrntPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 1),
    _PvxEServiceSlaCrntPMSwitchIdx_Type()
)
pvxEServiceSlaCrntPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMSwitchIdx.setStatus("current")


class _PvxEServiceSlaCrntPMShelfIdx_Type(Integer32):
    """Custom type pvxEServiceSlaCrntPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxEServiceSlaCrntPMShelfIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaCrntPMShelfIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMShelfIdx = _PvxEServiceSlaCrntPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 2),
    _PvxEServiceSlaCrntPMShelfIdx_Type()
)
pvxEServiceSlaCrntPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMShelfIdx.setStatus("current")


class _PvxEServiceSlaCrntPMSlotIdx_Type(Integer32):
    """Custom type pvxEServiceSlaCrntPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxEServiceSlaCrntPMSlotIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaCrntPMSlotIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMSlotIdx = _PvxEServiceSlaCrntPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 3),
    _PvxEServiceSlaCrntPMSlotIdx_Type()
)
pvxEServiceSlaCrntPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMSlotIdx.setStatus("current")
_PvxEServiceSlaCrntPMPortTypeIdx_Type = PvxPortType
_PvxEServiceSlaCrntPMPortTypeIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMPortTypeIdx = _PvxEServiceSlaCrntPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 4),
    _PvxEServiceSlaCrntPMPortTypeIdx_Type()
)
pvxEServiceSlaCrntPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMPortTypeIdx.setStatus("current")


class _PvxEServiceSlaCrntPMPortIdx_Type(Integer32):
    """Custom type pvxEServiceSlaCrntPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxEServiceSlaCrntPMPortIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaCrntPMPortIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMPortIdx = _PvxEServiceSlaCrntPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 5),
    _PvxEServiceSlaCrntPMPortIdx_Type()
)
pvxEServiceSlaCrntPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMPortIdx.setStatus("current")
_PvxEServiceSlaCrntPMESName_Type = DisplayString
_PvxEServiceSlaCrntPMESName_Object = MibTableColumn
pvxEServiceSlaCrntPMESName = _PvxEServiceSlaCrntPMESName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 6),
    _PvxEServiceSlaCrntPMESName_Type()
)
pvxEServiceSlaCrntPMESName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMESName.setStatus("current")


class _PvxEServiceSlaCrntPMRMepId_Type(Integer32):
    """Custom type pvxEServiceSlaCrntPMRMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEServiceSlaCrntPMRMepId_Type.__name__ = "Integer32"
_PvxEServiceSlaCrntPMRMepId_Object = MibTableColumn
pvxEServiceSlaCrntPMRMepId = _PvxEServiceSlaCrntPMRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 7),
    _PvxEServiceSlaCrntPMRMepId_Type()
)
pvxEServiceSlaCrntPMRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMRMepId.setStatus("current")
_PvxEServiceSlaCrntPMIntervalTypeIdx_Type = PMIntervalType
_PvxEServiceSlaCrntPMIntervalTypeIdx_Object = MibTableColumn
pvxEServiceSlaCrntPMIntervalTypeIdx = _PvxEServiceSlaCrntPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 8),
    _PvxEServiceSlaCrntPMIntervalTypeIdx_Type()
)
pvxEServiceSlaCrntPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMIntervalTypeIdx.setStatus("current")
_PvxEServiceSlaCrntPMNearEndFrameLoss_Type = FixedX1000
_PvxEServiceSlaCrntPMNearEndFrameLoss_Object = MibTableColumn
pvxEServiceSlaCrntPMNearEndFrameLoss = _PvxEServiceSlaCrntPMNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 9),
    _PvxEServiceSlaCrntPMNearEndFrameLoss_Type()
)
pvxEServiceSlaCrntPMNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMNearEndFrameLoss.setStatus("current")
_PvxEServiceSlaCrntPMNearEndFrameLossTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPMNearEndFrameLossTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPMNearEndFrameLossTimeStamp = _PvxEServiceSlaCrntPMNearEndFrameLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 10),
    _PvxEServiceSlaCrntPMNearEndFrameLossTimeStamp_Type()
)
pvxEServiceSlaCrntPMNearEndFrameLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMNearEndFrameLossTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPMNearEndFrameLossValidity_Type = PMValidity
_PvxEServiceSlaCrntPMNearEndFrameLossValidity_Object = MibTableColumn
pvxEServiceSlaCrntPMNearEndFrameLossValidity = _PvxEServiceSlaCrntPMNearEndFrameLossValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 11),
    _PvxEServiceSlaCrntPMNearEndFrameLossValidity_Type()
)
pvxEServiceSlaCrntPMNearEndFrameLossValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMNearEndFrameLossValidity.setStatus("current")
_PvxEServiceSlaCrntPMNearEndFrameLossInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPMNearEndFrameLossInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPMNearEndFrameLossInitialize = _PvxEServiceSlaCrntPMNearEndFrameLossInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 12),
    _PvxEServiceSlaCrntPMNearEndFrameLossInitialize_Type()
)
pvxEServiceSlaCrntPMNearEndFrameLossInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMNearEndFrameLossInitialize.setStatus("current")
_PvxEServiceSlaCrntPMFarEndFrameLoss_Type = FixedX1000
_PvxEServiceSlaCrntPMFarEndFrameLoss_Object = MibTableColumn
pvxEServiceSlaCrntPMFarEndFrameLoss = _PvxEServiceSlaCrntPMFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 13),
    _PvxEServiceSlaCrntPMFarEndFrameLoss_Type()
)
pvxEServiceSlaCrntPMFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMFarEndFrameLoss.setStatus("current")
_PvxEServiceSlaCrntPMFarEndFrameLossTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPMFarEndFrameLossTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPMFarEndFrameLossTimeStamp = _PvxEServiceSlaCrntPMFarEndFrameLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 14),
    _PvxEServiceSlaCrntPMFarEndFrameLossTimeStamp_Type()
)
pvxEServiceSlaCrntPMFarEndFrameLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMFarEndFrameLossTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPMFarEndFrameLossValidity_Type = PMValidity
_PvxEServiceSlaCrntPMFarEndFrameLossValidity_Object = MibTableColumn
pvxEServiceSlaCrntPMFarEndFrameLossValidity = _PvxEServiceSlaCrntPMFarEndFrameLossValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 15),
    _PvxEServiceSlaCrntPMFarEndFrameLossValidity_Type()
)
pvxEServiceSlaCrntPMFarEndFrameLossValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMFarEndFrameLossValidity.setStatus("current")
_PvxEServiceSlaCrntPMFarEndFrameLossInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPMFarEndFrameLossInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPMFarEndFrameLossInitialize = _PvxEServiceSlaCrntPMFarEndFrameLossInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 16),
    _PvxEServiceSlaCrntPMFarEndFrameLossInitialize_Type()
)
pvxEServiceSlaCrntPMFarEndFrameLossInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPMFarEndFrameLossInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMinimum_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayMinimum_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMinimum = _PvxEServiceSlaCrntPM2WayDelayMinimum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 17),
    _PvxEServiceSlaCrntPM2WayDelayMinimum_Type()
)
pvxEServiceSlaCrntPM2WayDelayMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMinimum.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp = _PvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 18),
    _PvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMinimumValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayMinimumValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMinimumValidity = _PvxEServiceSlaCrntPM2WayDelayMinimumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 19),
    _PvxEServiceSlaCrntPM2WayDelayMinimumValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayMinimumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMinimumValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMinimumInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayMinimumInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMinimumInitialize = _PvxEServiceSlaCrntPM2WayDelayMinimumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 21),
    _PvxEServiceSlaCrntPM2WayDelayMinimumInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayMinimumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMinimumInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMaximum_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayMaximum_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMaximum = _PvxEServiceSlaCrntPM2WayDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 22),
    _PvxEServiceSlaCrntPM2WayDelayMaximum_Type()
)
pvxEServiceSlaCrntPM2WayDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMaximum.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp = _PvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 23),
    _PvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMaximumValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayMaximumValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMaximumValidity = _PvxEServiceSlaCrntPM2WayDelayMaximumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 24),
    _PvxEServiceSlaCrntPM2WayDelayMaximumValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayMaximumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMaximumValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayMaximumInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayMaximumInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayMaximumInitialize = _PvxEServiceSlaCrntPM2WayDelayMaximumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 25),
    _PvxEServiceSlaCrntPM2WayDelayMaximumInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayMaximumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayMaximumInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayAverage_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayAverage_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayAverage = _PvxEServiceSlaCrntPM2WayDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 26),
    _PvxEServiceSlaCrntPM2WayDelayAverage_Type()
)
pvxEServiceSlaCrntPM2WayDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayAverage.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayAverageTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayAverageTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayAverageTimeStamp = _PvxEServiceSlaCrntPM2WayDelayAverageTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 27),
    _PvxEServiceSlaCrntPM2WayDelayAverageTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayAverageTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayAverageTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayAverageValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayAverageValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayAverageValidity = _PvxEServiceSlaCrntPM2WayDelayAverageValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 28),
    _PvxEServiceSlaCrntPM2WayDelayAverageValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayAverageValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayAverageValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayAverageInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayAverageInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayAverageInitialize = _PvxEServiceSlaCrntPM2WayDelayAverageInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 29),
    _PvxEServiceSlaCrntPM2WayDelayAverageInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayAverageInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayAverageInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMinimum_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayVariationMinimum_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMinimum = _PvxEServiceSlaCrntPM2WayDelayVariationMinimum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 30),
    _PvxEServiceSlaCrntPM2WayDelayVariationMinimum_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMinimum.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp = _PvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 31),
    _PvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity = _PvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 32),
    _PvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize = _PvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 33),
    _PvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMaximum_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayVariationMaximum_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMaximum = _PvxEServiceSlaCrntPM2WayDelayVariationMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 34),
    _PvxEServiceSlaCrntPM2WayDelayVariationMaximum_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMaximum.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp = _PvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 35),
    _PvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity = _PvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 36),
    _PvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize = _PvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 37),
    _PvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationAverage_Type = Unsigned32
_PvxEServiceSlaCrntPM2WayDelayVariationAverage_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationAverage = _PvxEServiceSlaCrntPM2WayDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 38),
    _PvxEServiceSlaCrntPM2WayDelayVariationAverage_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationAverage.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp_Type = DateAndTime
_PvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp = _PvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 39),
    _PvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationAverageValidity_Type = PMValidity
_PvxEServiceSlaCrntPM2WayDelayVariationAverageValidity_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationAverageValidity = _PvxEServiceSlaCrntPM2WayDelayVariationAverageValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 40),
    _PvxEServiceSlaCrntPM2WayDelayVariationAverageValidity_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationAverageValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationAverageValidity.setStatus("current")
_PvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize_Type = InitializeCmd
_PvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize_Object = MibTableColumn
pvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize = _PvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 47, 1, 41),
    _PvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize_Type()
)
pvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize.setStatus("current")
_PvxEServiceSlaHistPMTable_Object = MibTable
pvxEServiceSlaHistPMTable = _PvxEServiceSlaHistPMTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48)
)
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMTable.setStatus("current")
_PvxEServiceSlaHistPMEntry_Object = MibTableRow
pvxEServiceSlaHistPMEntry = _PvxEServiceSlaHistPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1)
)
pvxEServiceSlaHistPMEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMESName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMRMepId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMIntervalTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaHistPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMEntry.setStatus("current")


class _PvxEServiceSlaHistPMSwitchIdx_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEServiceSlaHistPMSwitchIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMSwitchIdx_Object = MibTableColumn
pvxEServiceSlaHistPMSwitchIdx = _PvxEServiceSlaHistPMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 1),
    _PvxEServiceSlaHistPMSwitchIdx_Type()
)
pvxEServiceSlaHistPMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMSwitchIdx.setStatus("current")


class _PvxEServiceSlaHistPMShelfIdx_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxEServiceSlaHistPMShelfIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMShelfIdx_Object = MibTableColumn
pvxEServiceSlaHistPMShelfIdx = _PvxEServiceSlaHistPMShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 2),
    _PvxEServiceSlaHistPMShelfIdx_Type()
)
pvxEServiceSlaHistPMShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMShelfIdx.setStatus("current")


class _PvxEServiceSlaHistPMSlotIdx_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxEServiceSlaHistPMSlotIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMSlotIdx_Object = MibTableColumn
pvxEServiceSlaHistPMSlotIdx = _PvxEServiceSlaHistPMSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 3),
    _PvxEServiceSlaHistPMSlotIdx_Type()
)
pvxEServiceSlaHistPMSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMSlotIdx.setStatus("current")
_PvxEServiceSlaHistPMPortTypeIdx_Type = PvxPortType
_PvxEServiceSlaHistPMPortTypeIdx_Object = MibTableColumn
pvxEServiceSlaHistPMPortTypeIdx = _PvxEServiceSlaHistPMPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 4),
    _PvxEServiceSlaHistPMPortTypeIdx_Type()
)
pvxEServiceSlaHistPMPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMPortTypeIdx.setStatus("current")


class _PvxEServiceSlaHistPMPortIdx_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxEServiceSlaHistPMPortIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMPortIdx_Object = MibTableColumn
pvxEServiceSlaHistPMPortIdx = _PvxEServiceSlaHistPMPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 5),
    _PvxEServiceSlaHistPMPortIdx_Type()
)
pvxEServiceSlaHistPMPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMPortIdx.setStatus("current")
_PvxEServiceSlaHistPMESName_Type = DisplayString
_PvxEServiceSlaHistPMESName_Object = MibTableColumn
pvxEServiceSlaHistPMESName = _PvxEServiceSlaHistPMESName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 6),
    _PvxEServiceSlaHistPMESName_Type()
)
pvxEServiceSlaHistPMESName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMESName.setStatus("current")


class _PvxEServiceSlaHistPMRMepId_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMRMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEServiceSlaHistPMRMepId_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMRMepId_Object = MibTableColumn
pvxEServiceSlaHistPMRMepId = _PvxEServiceSlaHistPMRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 7),
    _PvxEServiceSlaHistPMRMepId_Type()
)
pvxEServiceSlaHistPMRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMRMepId.setStatus("current")
_PvxEServiceSlaHistPMIntervalTypeIdx_Type = PMIntervalType
_PvxEServiceSlaHistPMIntervalTypeIdx_Object = MibTableColumn
pvxEServiceSlaHistPMIntervalTypeIdx = _PvxEServiceSlaHistPMIntervalTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 8),
    _PvxEServiceSlaHistPMIntervalTypeIdx_Type()
)
pvxEServiceSlaHistPMIntervalTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMIntervalTypeIdx.setStatus("current")


class _PvxEServiceSlaHistPMIntervalIdx_Type(Integer32):
    """Custom type pvxEServiceSlaHistPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvxEServiceSlaHistPMIntervalIdx_Type.__name__ = "Integer32"
_PvxEServiceSlaHistPMIntervalIdx_Object = MibTableColumn
pvxEServiceSlaHistPMIntervalIdx = _PvxEServiceSlaHistPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 9),
    _PvxEServiceSlaHistPMIntervalIdx_Type()
)
pvxEServiceSlaHistPMIntervalIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMIntervalIdx.setStatus("current")
_PvxEServiceSlaHistPMNearEndFrameLoss_Type = FixedX1000
_PvxEServiceSlaHistPMNearEndFrameLoss_Object = MibTableColumn
pvxEServiceSlaHistPMNearEndFrameLoss = _PvxEServiceSlaHistPMNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 10),
    _PvxEServiceSlaHistPMNearEndFrameLoss_Type()
)
pvxEServiceSlaHistPMNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMNearEndFrameLoss.setStatus("current")
_PvxEServiceSlaHistPMNearEndFrameLossTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPMNearEndFrameLossTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPMNearEndFrameLossTimeStamp = _PvxEServiceSlaHistPMNearEndFrameLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 11),
    _PvxEServiceSlaHistPMNearEndFrameLossTimeStamp_Type()
)
pvxEServiceSlaHistPMNearEndFrameLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMNearEndFrameLossTimeStamp.setStatus("current")
_PvxEServiceSlaHistPMNearEndFrameLossValidity_Type = PMValidity
_PvxEServiceSlaHistPMNearEndFrameLossValidity_Object = MibTableColumn
pvxEServiceSlaHistPMNearEndFrameLossValidity = _PvxEServiceSlaHistPMNearEndFrameLossValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 12),
    _PvxEServiceSlaHistPMNearEndFrameLossValidity_Type()
)
pvxEServiceSlaHistPMNearEndFrameLossValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMNearEndFrameLossValidity.setStatus("current")
_PvxEServiceSlaHistPMNearEndFrameLossInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPMNearEndFrameLossInitialize_Object = MibTableColumn
pvxEServiceSlaHistPMNearEndFrameLossInitialize = _PvxEServiceSlaHistPMNearEndFrameLossInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 13),
    _PvxEServiceSlaHistPMNearEndFrameLossInitialize_Type()
)
pvxEServiceSlaHistPMNearEndFrameLossInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMNearEndFrameLossInitialize.setStatus("current")
_PvxEServiceSlaHistPMFarEndFrameLoss_Type = FixedX1000
_PvxEServiceSlaHistPMFarEndFrameLoss_Object = MibTableColumn
pvxEServiceSlaHistPMFarEndFrameLoss = _PvxEServiceSlaHistPMFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 14),
    _PvxEServiceSlaHistPMFarEndFrameLoss_Type()
)
pvxEServiceSlaHistPMFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMFarEndFrameLoss.setStatus("current")
_PvxEServiceSlaHistPMFarEndFrameLossTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPMFarEndFrameLossTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPMFarEndFrameLossTimeStamp = _PvxEServiceSlaHistPMFarEndFrameLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 15),
    _PvxEServiceSlaHistPMFarEndFrameLossTimeStamp_Type()
)
pvxEServiceSlaHistPMFarEndFrameLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMFarEndFrameLossTimeStamp.setStatus("current")
_PvxEServiceSlaHistPMFarEndFrameLossValidity_Type = PMValidity
_PvxEServiceSlaHistPMFarEndFrameLossValidity_Object = MibTableColumn
pvxEServiceSlaHistPMFarEndFrameLossValidity = _PvxEServiceSlaHistPMFarEndFrameLossValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 16),
    _PvxEServiceSlaHistPMFarEndFrameLossValidity_Type()
)
pvxEServiceSlaHistPMFarEndFrameLossValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMFarEndFrameLossValidity.setStatus("current")
_PvxEServiceSlaHistPMFarEndFrameLossInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPMFarEndFrameLossInitialize_Object = MibTableColumn
pvxEServiceSlaHistPMFarEndFrameLossInitialize = _PvxEServiceSlaHistPMFarEndFrameLossInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 17),
    _PvxEServiceSlaHistPMFarEndFrameLossInitialize_Type()
)
pvxEServiceSlaHistPMFarEndFrameLossInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPMFarEndFrameLossInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMinimum_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayMinimum_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMinimum = _PvxEServiceSlaHistPM2WayDelayMinimum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 18),
    _PvxEServiceSlaHistPM2WayDelayMinimum_Type()
)
pvxEServiceSlaHistPM2WayDelayMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMinimum.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMinimumTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayMinimumTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMinimumTimeStamp = _PvxEServiceSlaHistPM2WayDelayMinimumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 19),
    _PvxEServiceSlaHistPM2WayDelayMinimumTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayMinimumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMinimumTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMinimumValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayMinimumValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMinimumValidity = _PvxEServiceSlaHistPM2WayDelayMinimumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 20),
    _PvxEServiceSlaHistPM2WayDelayMinimumValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayMinimumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMinimumValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMinimumInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayMinimumInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMinimumInitialize = _PvxEServiceSlaHistPM2WayDelayMinimumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 21),
    _PvxEServiceSlaHistPM2WayDelayMinimumInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayMinimumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMinimumInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMaximum_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayMaximum_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMaximum = _PvxEServiceSlaHistPM2WayDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 22),
    _PvxEServiceSlaHistPM2WayDelayMaximum_Type()
)
pvxEServiceSlaHistPM2WayDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMaximum.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMaximumTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayMaximumTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMaximumTimeStamp = _PvxEServiceSlaHistPM2WayDelayMaximumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 23),
    _PvxEServiceSlaHistPM2WayDelayMaximumTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayMaximumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMaximumTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMaximumValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayMaximumValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMaximumValidity = _PvxEServiceSlaHistPM2WayDelayMaximumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 24),
    _PvxEServiceSlaHistPM2WayDelayMaximumValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayMaximumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMaximumValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayMaximumInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayMaximumInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayMaximumInitialize = _PvxEServiceSlaHistPM2WayDelayMaximumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 25),
    _PvxEServiceSlaHistPM2WayDelayMaximumInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayMaximumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayMaximumInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayAverage_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayAverage_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayAverage = _PvxEServiceSlaHistPM2WayDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 26),
    _PvxEServiceSlaHistPM2WayDelayAverage_Type()
)
pvxEServiceSlaHistPM2WayDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayAverage.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayAverageTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayAverageTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayAverageTimeStamp = _PvxEServiceSlaHistPM2WayDelayAverageTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 27),
    _PvxEServiceSlaHistPM2WayDelayAverageTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayAverageTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayAverageTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayAverageValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayAverageValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayAverageValidity = _PvxEServiceSlaHistPM2WayDelayAverageValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 28),
    _PvxEServiceSlaHistPM2WayDelayAverageValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayAverageValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayAverageValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayAverageInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayAverageInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayAverageInitialize = _PvxEServiceSlaHistPM2WayDelayAverageInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 29),
    _PvxEServiceSlaHistPM2WayDelayAverageInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayAverageInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayAverageInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMinimum_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayVariationMinimum_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMinimum = _PvxEServiceSlaHistPM2WayDelayVariationMinimum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 30),
    _PvxEServiceSlaHistPM2WayDelayVariationMinimum_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMinimum.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp = _PvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 31),
    _PvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMinimumValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayVariationMinimumValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMinimumValidity = _PvxEServiceSlaHistPM2WayDelayVariationMinimumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 32),
    _PvxEServiceSlaHistPM2WayDelayVariationMinimumValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMinimumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMinimumValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize = _PvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 33),
    _PvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMaximum_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayVariationMaximum_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMaximum = _PvxEServiceSlaHistPM2WayDelayVariationMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 34),
    _PvxEServiceSlaHistPM2WayDelayVariationMaximum_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMaximum.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp = _PvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 35),
    _PvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMaximumValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayVariationMaximumValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMaximumValidity = _PvxEServiceSlaHistPM2WayDelayVariationMaximumValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 36),
    _PvxEServiceSlaHistPM2WayDelayVariationMaximumValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMaximumValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMaximumValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize = _PvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 37),
    _PvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationAverage_Type = Unsigned32
_PvxEServiceSlaHistPM2WayDelayVariationAverage_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationAverage = _PvxEServiceSlaHistPM2WayDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 38),
    _PvxEServiceSlaHistPM2WayDelayVariationAverage_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationAverage.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp_Type = DateAndTime
_PvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp = _PvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 39),
    _PvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationAverageValidity_Type = PMValidity
_PvxEServiceSlaHistPM2WayDelayVariationAverageValidity_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationAverageValidity = _PvxEServiceSlaHistPM2WayDelayVariationAverageValidity_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 40),
    _PvxEServiceSlaHistPM2WayDelayVariationAverageValidity_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationAverageValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationAverageValidity.setStatus("current")
_PvxEServiceSlaHistPM2WayDelayVariationAverageInitialize_Type = InitializeCmd
_PvxEServiceSlaHistPM2WayDelayVariationAverageInitialize_Object = MibTableColumn
pvxEServiceSlaHistPM2WayDelayVariationAverageInitialize = _PvxEServiceSlaHistPM2WayDelayVariationAverageInitialize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 6, 48, 1, 41),
    _PvxEServiceSlaHistPM2WayDelayVariationAverageInitialize_Type()
)
pvxEServiceSlaHistPM2WayDelayVariationAverageInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEServiceSlaHistPM2WayDelayVariationAverageInitialize.setStatus("current")
_PvxSwitchTable_Object = MibTable
pvxSwitchTable = _PvxSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    pvxSwitchTable.setStatus("current")
_PvxSwitchEntry_Object = MibTableRow
pvxSwitchEntry = _PvxSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1)
)
pvxSwitchEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchIdx"),
)
if mibBuilder.loadTexts:
    pvxSwitchEntry.setStatus("current")


class _PvxSwitchIdx_Type(Integer32):
    """Custom type pvxSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSwitchIdx_Type.__name__ = "Integer32"
_PvxSwitchIdx_Object = MibTableColumn
pvxSwitchIdx = _PvxSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 1),
    _PvxSwitchIdx_Type()
)
pvxSwitchIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvxSwitchIdx.setStatus("current")


class _PvxSwitchMode_Type(Integer32):
    """Custom type pvxSwitchMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("provider-bridge", 2),
          ("q-bridge", 1))
    )


_PvxSwitchMode_Type.__name__ = "Integer32"
_PvxSwitchMode_Object = MibTableColumn
pvxSwitchMode = _PvxSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 2),
    _PvxSwitchMode_Type()
)
pvxSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMode.setStatus("current")
_PvxSwitchInnerEthType_Type = Integer32
_PvxSwitchInnerEthType_Object = MibTableColumn
pvxSwitchInnerEthType = _PvxSwitchInnerEthType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 3),
    _PvxSwitchInnerEthType_Type()
)
pvxSwitchInnerEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchInnerEthType.setStatus("current")


class _PvxSwitchLearning_Type(Integer32):
    """Custom type pvxSwitchLearning based on Integer32"""
    defaultValue = 1

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


_PvxSwitchLearning_Type.__name__ = "Integer32"
_PvxSwitchLearning_Object = MibTableColumn
pvxSwitchLearning = _PvxSwitchLearning_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 4),
    _PvxSwitchLearning_Type()
)
pvxSwitchLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchLearning.setStatus("current")


class _PvxSwitchAgingTimer_Type(Integer32):
    """Custom type pvxSwitchAgingTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_PvxSwitchAgingTimer_Type.__name__ = "Integer32"
_PvxSwitchAgingTimer_Object = MibTableColumn
pvxSwitchAgingTimer = _PvxSwitchAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 5),
    _PvxSwitchAgingTimer_Type()
)
pvxSwitchAgingTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchAgingTimer.setStatus("current")


class _PvxSwitchTimeToAge_Type(Integer32):
    """Custom type pvxSwitchTimeToAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_PvxSwitchTimeToAge_Type.__name__ = "Integer32"
_PvxSwitchTimeToAge_Object = MibTableColumn
pvxSwitchTimeToAge = _PvxSwitchTimeToAge_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 6),
    _PvxSwitchTimeToAge_Type()
)
pvxSwitchTimeToAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchTimeToAge.setStatus("current")
_PvxSwitchMasterNode_Type = DisplayString
_PvxSwitchMasterNode_Object = MibTableColumn
pvxSwitchMasterNode = _PvxSwitchMasterNode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 7),
    _PvxSwitchMasterNode_Type()
)
pvxSwitchMasterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchMasterNode.setStatus("deprecated")
_PvxSwitchForceSwitch_Type = TruthValue
_PvxSwitchForceSwitch_Object = MibTableColumn
pvxSwitchForceSwitch = _PvxSwitchForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 8),
    _PvxSwitchForceSwitch_Type()
)
pvxSwitchForceSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchForceSwitch.setStatus("deprecated")
_PvxSwitchClearDynamicFDBEntries_Type = TruthValue
_PvxSwitchClearDynamicFDBEntries_Object = MibTableColumn
pvxSwitchClearDynamicFDBEntries = _PvxSwitchClearDynamicFDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 10),
    _PvxSwitchClearDynamicFDBEntries_Type()
)
pvxSwitchClearDynamicFDBEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchClearDynamicFDBEntries.setStatus("current")


class _PvxSwitchProtocolAdminState_Type(Integer32):
    """Custom type pvxSwitchProtocolAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PvxSwitchProtocolAdminState_Type.__name__ = "Integer32"
_PvxSwitchProtocolAdminState_Object = MibTableColumn
pvxSwitchProtocolAdminState = _PvxSwitchProtocolAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 11),
    _PvxSwitchProtocolAdminState_Type()
)
pvxSwitchProtocolAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchProtocolAdminState.setStatus("current")
_PvxSwitchTunnMacAddrProfile_Type = ProfileNameType
_PvxSwitchTunnMacAddrProfile_Object = MibTableColumn
pvxSwitchTunnMacAddrProfile = _PvxSwitchTunnMacAddrProfile_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 12),
    _PvxSwitchTunnMacAddrProfile_Type()
)
pvxSwitchTunnMacAddrProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchTunnMacAddrProfile.setStatus("current")


class _PvxSwitchEvcMEGName_Type(DisplayString):
    """Custom type pvxSwitchEvcMEGName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_PvxSwitchEvcMEGName_Type.__name__ = "DisplayString"
_PvxSwitchEvcMEGName_Object = MibTableColumn
pvxSwitchEvcMEGName = _PvxSwitchEvcMEGName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 13),
    _PvxSwitchEvcMEGName_Type()
)
pvxSwitchEvcMEGName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchEvcMEGName.setStatus("current")


class _PvxSwitchEvcMEGLevel_Type(Integer32):
    """Custom type pvxSwitchEvcMEGLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PvxSwitchEvcMEGLevel_Type.__name__ = "Integer32"
_PvxSwitchEvcMEGLevel_Object = MibTableColumn
pvxSwitchEvcMEGLevel = _PvxSwitchEvcMEGLevel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 14),
    _PvxSwitchEvcMEGLevel_Type()
)
pvxSwitchEvcMEGLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchEvcMEGLevel.setStatus("current")


class _PvxSwitchName_Type(DisplayString):
    """Custom type pvxSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxSwitchName_Type.__name__ = "DisplayString"
_PvxSwitchName_Object = MibTableColumn
pvxSwitchName = _PvxSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 15),
    _PvxSwitchName_Type()
)
pvxSwitchName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchName.setStatus("current")
_PvxSwitchMIPAutoCreate_Type = TruthValue
_PvxSwitchMIPAutoCreate_Object = MibTableColumn
pvxSwitchMIPAutoCreate = _PvxSwitchMIPAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 16),
    _PvxSwitchMIPAutoCreate_Type()
)
pvxSwitchMIPAutoCreate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMIPAutoCreate.setStatus("current")


class _PvxSwitchMIPAutoCreateMEL_Type(Integer32):
    """Custom type pvxSwitchMIPAutoCreateMEL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PvxSwitchMIPAutoCreateMEL_Type.__name__ = "Integer32"
_PvxSwitchMIPAutoCreateMEL_Object = MibTableColumn
pvxSwitchMIPAutoCreateMEL = _PvxSwitchMIPAutoCreateMEL_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 17),
    _PvxSwitchMIPAutoCreateMEL_Type()
)
pvxSwitchMIPAutoCreateMEL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMIPAutoCreateMEL.setStatus("current")
_PvxSwitchStackingPrimary_Type = Integer32
_PvxSwitchStackingPrimary_Object = MibTableColumn
pvxSwitchStackingPrimary = _PvxSwitchStackingPrimary_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 18),
    _PvxSwitchStackingPrimary_Type()
)
pvxSwitchStackingPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchStackingPrimary.setStatus("current")
_PvxSwitchStackingTimeAsPrimary_Type = Integer32
_PvxSwitchStackingTimeAsPrimary_Object = MibTableColumn
pvxSwitchStackingTimeAsPrimary = _PvxSwitchStackingTimeAsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 19),
    _PvxSwitchStackingTimeAsPrimary_Type()
)
pvxSwitchStackingTimeAsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchStackingTimeAsPrimary.setStatus("current")


class _PvxSwitchErpsVlanPropagate_Type(Integer32):
    """Custom type pvxSwitchErpsVlanPropagate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2))
    )


_PvxSwitchErpsVlanPropagate_Type.__name__ = "Integer32"
_PvxSwitchErpsVlanPropagate_Object = MibTableColumn
pvxSwitchErpsVlanPropagate = _PvxSwitchErpsVlanPropagate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 20),
    _PvxSwitchErpsVlanPropagate_Type()
)
pvxSwitchErpsVlanPropagate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchErpsVlanPropagate.setStatus("current")


class _PvxSwitchCfmDestinationAddress_Type(Integer32):
    """Custom type pvxSwitchCfmDestinationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_PvxSwitchCfmDestinationAddress_Type.__name__ = "Integer32"
_PvxSwitchCfmDestinationAddress_Object = MibTableColumn
pvxSwitchCfmDestinationAddress = _PvxSwitchCfmDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 21),
    _PvxSwitchCfmDestinationAddress_Type()
)
pvxSwitchCfmDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchCfmDestinationAddress.setStatus("current")


class _PvxSwitchIntfBouncingTimerPeriod_Type(Integer32):
    """Custom type pvxSwitchIntfBouncingTimerPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_PvxSwitchIntfBouncingTimerPeriod_Type.__name__ = "Integer32"
_PvxSwitchIntfBouncingTimerPeriod_Object = MibTableColumn
pvxSwitchIntfBouncingTimerPeriod = _PvxSwitchIntfBouncingTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 22),
    _PvxSwitchIntfBouncingTimerPeriod_Type()
)
pvxSwitchIntfBouncingTimerPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchIntfBouncingTimerPeriod.setStatus("current")


class _PvxSwitchCpuRLCos0PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos0PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos0PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos0PPS_Object = MibTableColumn
pvxSwitchCpuRLCos0PPS = _PvxSwitchCpuRLCos0PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 23),
    _PvxSwitchCpuRLCos0PPS_Type()
)
pvxSwitchCpuRLCos0PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos0PPS.setStatus("current")


class _PvxSwitchCpuRLCos1PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos1PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos1PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos1PPS_Object = MibTableColumn
pvxSwitchCpuRLCos1PPS = _PvxSwitchCpuRLCos1PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 24),
    _PvxSwitchCpuRLCos1PPS_Type()
)
pvxSwitchCpuRLCos1PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos1PPS.setStatus("current")


class _PvxSwitchCpuRLCos2PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos2PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos2PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos2PPS_Object = MibTableColumn
pvxSwitchCpuRLCos2PPS = _PvxSwitchCpuRLCos2PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 25),
    _PvxSwitchCpuRLCos2PPS_Type()
)
pvxSwitchCpuRLCos2PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos2PPS.setStatus("current")


class _PvxSwitchCpuRLCos3PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos3PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos3PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos3PPS_Object = MibTableColumn
pvxSwitchCpuRLCos3PPS = _PvxSwitchCpuRLCos3PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 26),
    _PvxSwitchCpuRLCos3PPS_Type()
)
pvxSwitchCpuRLCos3PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos3PPS.setStatus("current")


class _PvxSwitchCpuRLCos4PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos4PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos4PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos4PPS_Object = MibTableColumn
pvxSwitchCpuRLCos4PPS = _PvxSwitchCpuRLCos4PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 27),
    _PvxSwitchCpuRLCos4PPS_Type()
)
pvxSwitchCpuRLCos4PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos4PPS.setStatus("current")


class _PvxSwitchCpuRLCos5PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos5PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos5PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos5PPS_Object = MibTableColumn
pvxSwitchCpuRLCos5PPS = _PvxSwitchCpuRLCos5PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 28),
    _PvxSwitchCpuRLCos5PPS_Type()
)
pvxSwitchCpuRLCos5PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos5PPS.setStatus("current")


class _PvxSwitchCpuRLCos6PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos6PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos6PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos6PPS_Object = MibTableColumn
pvxSwitchCpuRLCos6PPS = _PvxSwitchCpuRLCos6PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 29),
    _PvxSwitchCpuRLCos6PPS_Type()
)
pvxSwitchCpuRLCos6PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos6PPS.setStatus("current")


class _PvxSwitchCpuRLCos7PPS_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos7PPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos7PPS_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos7PPS_Object = MibTableColumn
pvxSwitchCpuRLCos7PPS = _PvxSwitchCpuRLCos7PPS_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 30),
    _PvxSwitchCpuRLCos7PPS_Type()
)
pvxSwitchCpuRLCos7PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos7PPS.setStatus("current")


class _PvxSwitchCpuRLCos0DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos0DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos0DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos0DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos0DEPTH = _PvxSwitchCpuRLCos0DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 31),
    _PvxSwitchCpuRLCos0DEPTH_Type()
)
pvxSwitchCpuRLCos0DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos0DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos1DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos1DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos1DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos1DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos1DEPTH = _PvxSwitchCpuRLCos1DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 32),
    _PvxSwitchCpuRLCos1DEPTH_Type()
)
pvxSwitchCpuRLCos1DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos1DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos2DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos2DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos2DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos2DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos2DEPTH = _PvxSwitchCpuRLCos2DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 33),
    _PvxSwitchCpuRLCos2DEPTH_Type()
)
pvxSwitchCpuRLCos2DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos2DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos3DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos3DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos3DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos3DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos3DEPTH = _PvxSwitchCpuRLCos3DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 34),
    _PvxSwitchCpuRLCos3DEPTH_Type()
)
pvxSwitchCpuRLCos3DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos3DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos4DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos4DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos4DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos4DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos4DEPTH = _PvxSwitchCpuRLCos4DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 35),
    _PvxSwitchCpuRLCos4DEPTH_Type()
)
pvxSwitchCpuRLCos4DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos4DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos5DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos5DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos5DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos5DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos5DEPTH = _PvxSwitchCpuRLCos5DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 36),
    _PvxSwitchCpuRLCos5DEPTH_Type()
)
pvxSwitchCpuRLCos5DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos5DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos6DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos6DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos6DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos6DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos6DEPTH = _PvxSwitchCpuRLCos6DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 37),
    _PvxSwitchCpuRLCos6DEPTH_Type()
)
pvxSwitchCpuRLCos6DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos6DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos7DEPTH_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos7DEPTH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos7DEPTH_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos7DEPTH_Object = MibTableColumn
pvxSwitchCpuRLCos7DEPTH = _PvxSwitchCpuRLCos7DEPTH_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 38),
    _PvxSwitchCpuRLCos7DEPTH_Type()
)
pvxSwitchCpuRLCos7DEPTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos7DEPTH.setStatus("current")


class _PvxSwitchCpuRLCos0BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos0BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos0BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos0BURST_Object = MibTableColumn
pvxSwitchCpuRLCos0BURST = _PvxSwitchCpuRLCos0BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 39),
    _PvxSwitchCpuRLCos0BURST_Type()
)
pvxSwitchCpuRLCos0BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos0BURST.setStatus("current")


class _PvxSwitchCpuRLCos1BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos1BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos1BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos1BURST_Object = MibTableColumn
pvxSwitchCpuRLCos1BURST = _PvxSwitchCpuRLCos1BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 40),
    _PvxSwitchCpuRLCos1BURST_Type()
)
pvxSwitchCpuRLCos1BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos1BURST.setStatus("current")


class _PvxSwitchCpuRLCos2BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos2BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos2BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos2BURST_Object = MibTableColumn
pvxSwitchCpuRLCos2BURST = _PvxSwitchCpuRLCos2BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 41),
    _PvxSwitchCpuRLCos2BURST_Type()
)
pvxSwitchCpuRLCos2BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos2BURST.setStatus("current")


class _PvxSwitchCpuRLCos3BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos3BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos3BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos3BURST_Object = MibTableColumn
pvxSwitchCpuRLCos3BURST = _PvxSwitchCpuRLCos3BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 42),
    _PvxSwitchCpuRLCos3BURST_Type()
)
pvxSwitchCpuRLCos3BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos3BURST.setStatus("current")


class _PvxSwitchCpuRLCos4BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos4BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos4BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos4BURST_Object = MibTableColumn
pvxSwitchCpuRLCos4BURST = _PvxSwitchCpuRLCos4BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 43),
    _PvxSwitchCpuRLCos4BURST_Type()
)
pvxSwitchCpuRLCos4BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos4BURST.setStatus("current")


class _PvxSwitchCpuRLCos5BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos5BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos5BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos5BURST_Object = MibTableColumn
pvxSwitchCpuRLCos5BURST = _PvxSwitchCpuRLCos5BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 44),
    _PvxSwitchCpuRLCos5BURST_Type()
)
pvxSwitchCpuRLCos5BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos5BURST.setStatus("current")


class _PvxSwitchCpuRLCos6BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos6BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos6BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos6BURST_Object = MibTableColumn
pvxSwitchCpuRLCos6BURST = _PvxSwitchCpuRLCos6BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 45),
    _PvxSwitchCpuRLCos6BURST_Type()
)
pvxSwitchCpuRLCos6BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos6BURST.setStatus("current")


class _PvxSwitchCpuRLCos7BURST_Type(Integer32):
    """Custom type pvxSwitchCpuRLCos7BURST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PvxSwitchCpuRLCos7BURST_Type.__name__ = "Integer32"
_PvxSwitchCpuRLCos7BURST_Object = MibTableColumn
pvxSwitchCpuRLCos7BURST = _PvxSwitchCpuRLCos7BURST_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 46),
    _PvxSwitchCpuRLCos7BURST_Type()
)
pvxSwitchCpuRLCos7BURST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLCos7BURST.setStatus("current")
_PvxSwitchMirrorFromCpu_Type = MirrorConfigType
_PvxSwitchMirrorFromCpu_Object = MibTableColumn
pvxSwitchMirrorFromCpu = _PvxSwitchMirrorFromCpu_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 47),
    _PvxSwitchMirrorFromCpu_Type()
)
pvxSwitchMirrorFromCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMirrorFromCpu.setStatus("current")


class _PvxSwitchLldpTrapInterval_Type(Integer32):
    """Custom type pvxSwitchLldpTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_PvxSwitchLldpTrapInterval_Type.__name__ = "Integer32"
_PvxSwitchLldpTrapInterval_Object = MibTableColumn
pvxSwitchLldpTrapInterval = _PvxSwitchLldpTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 48),
    _PvxSwitchLldpTrapInterval_Type()
)
pvxSwitchLldpTrapInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchLldpTrapInterval.setStatus("current")
_PvxSwitchRowStatus_Type = RowStatus
_PvxSwitchRowStatus_Object = MibTableColumn
pvxSwitchRowStatus = _PvxSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 1, 1, 100),
    _PvxSwitchRowStatus_Type()
)
pvxSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchRowStatus.setStatus("current")
_PvxSwitchMemberTable_Object = MibTable
pvxSwitchMemberTable = _PvxSwitchMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    pvxSwitchMemberTable.setStatus("current")
_PvxSwitchMemberEntry_Object = MibTableRow
pvxSwitchMemberEntry = _PvxSwitchMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1)
)
pvxSwitchMemberEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchMemberIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchMemberInstIdx"),
)
if mibBuilder.loadTexts:
    pvxSwitchMemberEntry.setStatus("current")


class _PvxSwitchMemberIdx_Type(Integer32):
    """Custom type pvxSwitchMemberIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSwitchMemberIdx_Type.__name__ = "Integer32"
_PvxSwitchMemberIdx_Object = MibTableColumn
pvxSwitchMemberIdx = _PvxSwitchMemberIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 1),
    _PvxSwitchMemberIdx_Type()
)
pvxSwitchMemberIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvxSwitchMemberIdx.setStatus("current")


class _PvxSwitchMemberInstIdx_Type(Integer32):
    """Custom type pvxSwitchMemberInstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PvxSwitchMemberInstIdx_Type.__name__ = "Integer32"
_PvxSwitchMemberInstIdx_Object = MibTableColumn
pvxSwitchMemberInstIdx = _PvxSwitchMemberInstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 2),
    _PvxSwitchMemberInstIdx_Type()
)
pvxSwitchMemberInstIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvxSwitchMemberInstIdx.setStatus("current")


class _PvxSwitchMemberShelfId_Type(Integer32):
    """Custom type pvxSwitchMemberShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSwitchMemberShelfId_Type.__name__ = "Integer32"
_PvxSwitchMemberShelfId_Object = MibTableColumn
pvxSwitchMemberShelfId = _PvxSwitchMemberShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 3),
    _PvxSwitchMemberShelfId_Type()
)
pvxSwitchMemberShelfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMemberShelfId.setStatus("current")


class _PvxSwitchMemberSlotId_Type(Integer32):
    """Custom type pvxSwitchMemberSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSwitchMemberSlotId_Type.__name__ = "Integer32"
_PvxSwitchMemberSlotId_Object = MibTableColumn
pvxSwitchMemberSlotId = _PvxSwitchMemberSlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 4),
    _PvxSwitchMemberSlotId_Type()
)
pvxSwitchMemberSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMemberSlotId.setStatus("current")


class _PvxSwitchMemberStackingState_Type(Integer32):
    """Custom type pvxSwitchMemberStackingState based on Integer32"""
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
        *(("disabled", 1),
          ("notPresent", 5),
          ("primary", 3),
          ("secondary", 4),
          ("unstacked", 2))
    )


_PvxSwitchMemberStackingState_Type.__name__ = "Integer32"
_PvxSwitchMemberStackingState_Object = MibTableColumn
pvxSwitchMemberStackingState = _PvxSwitchMemberStackingState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 8),
    _PvxSwitchMemberStackingState_Type()
)
pvxSwitchMemberStackingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchMemberStackingState.setStatus("current")
_PvxSwitchMemberStackingPortCommState_Type = PvxStackingPortCommState
_PvxSwitchMemberStackingPortCommState_Object = MibTableColumn
pvxSwitchMemberStackingPortCommState = _PvxSwitchMemberStackingPortCommState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 9),
    _PvxSwitchMemberStackingPortCommState_Type()
)
pvxSwitchMemberStackingPortCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchMemberStackingPortCommState.setStatus("current")
_PvxSwitchMemberBackplaneCommState_Type = PvxStackingPortCommState
_PvxSwitchMemberBackplaneCommState_Object = MibTableColumn
pvxSwitchMemberBackplaneCommState = _PvxSwitchMemberBackplaneCommState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 10),
    _PvxSwitchMemberBackplaneCommState_Type()
)
pvxSwitchMemberBackplaneCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchMemberBackplaneCommState.setStatus("current")
_PvxSwitchMemberRowStatus_Type = RowStatus
_PvxSwitchMemberRowStatus_Object = MibTableColumn
pvxSwitchMemberRowStatus = _PvxSwitchMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 2, 1, 100),
    _PvxSwitchMemberRowStatus_Type()
)
pvxSwitchMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSwitchMemberRowStatus.setStatus("current")
_PvxVLANTable_Object = MibTable
pvxVLANTable = _PvxVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    pvxVLANTable.setStatus("current")
_PvxVLANEntry_Object = MibTableRow
pvxVLANEntry = _PvxVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1)
)
pvxVLANEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVLANSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVLANIdx"),
)
if mibBuilder.loadTexts:
    pvxVLANEntry.setStatus("current")


class _PvxVLANSwitchIdx_Type(Integer32):
    """Custom type pvxVLANSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxVLANSwitchIdx_Type.__name__ = "Integer32"
_PvxVLANSwitchIdx_Object = MibTableColumn
pvxVLANSwitchIdx = _PvxVLANSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 1),
    _PvxVLANSwitchIdx_Type()
)
pvxVLANSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVLANSwitchIdx.setStatus("current")


class _PvxVLANIdx_Type(Integer32):
    """Custom type pvxVLANIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxVLANIdx_Type.__name__ = "Integer32"
_PvxVLANIdx_Object = MibTableColumn
pvxVLANIdx = _PvxVLANIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 2),
    _PvxVLANIdx_Type()
)
pvxVLANIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVLANIdx.setStatus("current")
_PvxVLANMemberPortList_Type = PvxL2PortList
_PvxVLANMemberPortList_Object = MibTableColumn
pvxVLANMemberPortList = _PvxVLANMemberPortList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 4),
    _PvxVLANMemberPortList_Type()
)
pvxVLANMemberPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANMemberPortList.setStatus("current")
_PvxVLANUnTaggedPortList_Type = PvxL2PortList
_PvxVLANUnTaggedPortList_Object = MibTableColumn
pvxVLANUnTaggedPortList = _PvxVLANUnTaggedPortList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 5),
    _PvxVLANUnTaggedPortList_Type()
)
pvxVLANUnTaggedPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANUnTaggedPortList.setStatus("current")


class _PvxVLANMacLearning_Type(Integer32):
    """Custom type pvxVLANMacLearning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxVLANMacLearning_Type.__name__ = "Integer32"
_PvxVLANMacLearning_Object = MibTableColumn
pvxVLANMacLearning = _PvxVLANMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 6),
    _PvxVLANMacLearning_Type()
)
pvxVLANMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANMacLearning.setStatus("current")


class _PvxVLANAdminState_Type(Integer32):
    """Custom type pvxVLANAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxVLANAdminState_Type.__name__ = "Integer32"
_PvxVLANAdminState_Object = MibTableColumn
pvxVLANAdminState = _PvxVLANAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 7),
    _PvxVLANAdminState_Type()
)
pvxVLANAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANAdminState.setStatus("current")
_PvxVLANMSTPId_Type = Integer32
_PvxVLANMSTPId_Object = MibTableColumn
pvxVLANMSTPId = _PvxVLANMSTPId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 8),
    _PvxVLANMSTPId_Type()
)
pvxVLANMSTPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANMSTPId.setStatus("current")


class _PvxVLANService_Type(DisplayString):
    """Custom type pvxVLANService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxVLANService_Type.__name__ = "DisplayString"
_PvxVLANService_Object = MibTableColumn
pvxVLANService = _PvxVLANService_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 9),
    _PvxVLANService_Type()
)
pvxVLANService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVLANService.setStatus("current")
_PvxVLANForbiddenPortList_Type = PvxL2PortList
_PvxVLANForbiddenPortList_Object = MibTableColumn
pvxVLANForbiddenPortList = _PvxVLANForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 10),
    _PvxVLANForbiddenPortList_Type()
)
pvxVLANForbiddenPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANForbiddenPortList.setStatus("current")


class _PvxVLANOperStatus_Type(Integer32):
    """Custom type pvxVLANOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("reserved", 3),
          ("up", 1))
    )


_PvxVLANOperStatus_Type.__name__ = "Integer32"
_PvxVLANOperStatus_Object = MibTableColumn
pvxVLANOperStatus = _PvxVLANOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 11),
    _PvxVLANOperStatus_Type()
)
pvxVLANOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVLANOperStatus.setStatus("current")
_PvxVLANRowStatus_Type = RowStatus
_PvxVLANRowStatus_Object = MibTableColumn
pvxVLANRowStatus = _PvxVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 4, 1, 100),
    _PvxVLANRowStatus_Type()
)
pvxVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVLANRowStatus.setStatus("current")
_PvxFDBTable_Object = MibTable
pvxFDBTable = _PvxFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    pvxFDBTable.setStatus("current")
_PvxFDBEntry_Object = MibTableRow
pvxFDBEntry = _PvxFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1)
)
pvxFDBEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFDBSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFDBVlanIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFDBMACAddrIdx"),
)
if mibBuilder.loadTexts:
    pvxFDBEntry.setStatus("current")


class _PvxFDBSwitchIdx_Type(Integer32):
    """Custom type pvxFDBSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFDBSwitchIdx_Type.__name__ = "Integer32"
_PvxFDBSwitchIdx_Object = MibTableColumn
pvxFDBSwitchIdx = _PvxFDBSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 1),
    _PvxFDBSwitchIdx_Type()
)
pvxFDBSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFDBSwitchIdx.setStatus("current")
_PvxFDBVlanIdx_Type = Integer32
_PvxFDBVlanIdx_Object = MibTableColumn
pvxFDBVlanIdx = _PvxFDBVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 2),
    _PvxFDBVlanIdx_Type()
)
pvxFDBVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFDBVlanIdx.setStatus("current")
_PvxFDBMACAddrIdx_Type = MacAddress
_PvxFDBMACAddrIdx_Object = MibTableColumn
pvxFDBMACAddrIdx = _PvxFDBMACAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 3),
    _PvxFDBMACAddrIdx_Type()
)
pvxFDBMACAddrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFDBMACAddrIdx.setStatus("current")
_PvxFDBPort_Type = PvxL2Port
_PvxFDBPort_Object = MibTableColumn
pvxFDBPort = _PvxFDBPort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 4),
    _PvxFDBPort_Type()
)
pvxFDBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxFDBPort.setStatus("current")


class _PvxFDBAddressType_Type(Integer32):
    """Custom type pvxFDBAddressType based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_PvxFDBAddressType_Type.__name__ = "Integer32"
_PvxFDBAddressType_Object = MibTableColumn
pvxFDBAddressType = _PvxFDBAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 5),
    _PvxFDBAddressType_Type()
)
pvxFDBAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxFDBAddressType.setStatus("current")
_PvxFDBRowStatus_Type = RowStatus
_PvxFDBRowStatus_Object = MibTableColumn
pvxFDBRowStatus = _PvxFDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 5, 1, 6),
    _PvxFDBRowStatus_Type()
)
pvxFDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFDBRowStatus.setStatus("current")
_PvxStaticUnicastTable_Object = MibTable
pvxStaticUnicastTable = _PvxStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    pvxStaticUnicastTable.setStatus("current")
_PvxStaticUnicastEntry_Object = MibTableRow
pvxStaticUnicastEntry = _PvxStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1)
)
pvxStaticUnicastEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticUnicastSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticUnicastVlanIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticUnicastMACAddrIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticUnicastReceivePort"),
)
if mibBuilder.loadTexts:
    pvxStaticUnicastEntry.setStatus("current")


class _PvxStaticUnicastSwitchIdx_Type(Integer32):
    """Custom type pvxStaticUnicastSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxStaticUnicastSwitchIdx_Type.__name__ = "Integer32"
_PvxStaticUnicastSwitchIdx_Object = MibTableColumn
pvxStaticUnicastSwitchIdx = _PvxStaticUnicastSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 1),
    _PvxStaticUnicastSwitchIdx_Type()
)
pvxStaticUnicastSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticUnicastSwitchIdx.setStatus("current")


class _PvxStaticUnicastVlanIdx_Type(Integer32):
    """Custom type pvxStaticUnicastVlanIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PvxStaticUnicastVlanIdx_Type.__name__ = "Integer32"
_PvxStaticUnicastVlanIdx_Object = MibTableColumn
pvxStaticUnicastVlanIdx = _PvxStaticUnicastVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 2),
    _PvxStaticUnicastVlanIdx_Type()
)
pvxStaticUnicastVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticUnicastVlanIdx.setStatus("current")
_PvxStaticUnicastMACAddrIdx_Type = MacAddress
_PvxStaticUnicastMACAddrIdx_Object = MibTableColumn
pvxStaticUnicastMACAddrIdx = _PvxStaticUnicastMACAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 3),
    _PvxStaticUnicastMACAddrIdx_Type()
)
pvxStaticUnicastMACAddrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticUnicastMACAddrIdx.setStatus("current")
_PvxStaticUnicastReceivePort_Type = PvxL2Port
_PvxStaticUnicastReceivePort_Object = MibTableColumn
pvxStaticUnicastReceivePort = _PvxStaticUnicastReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 4),
    _PvxStaticUnicastReceivePort_Type()
)
pvxStaticUnicastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticUnicastReceivePort.setStatus("current")
_PvxStaticUnicastIntfIdList_Type = PvxVLANPortList
_PvxStaticUnicastIntfIdList_Object = MibTableColumn
pvxStaticUnicastIntfIdList = _PvxStaticUnicastIntfIdList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 5),
    _PvxStaticUnicastIntfIdList_Type()
)
pvxStaticUnicastIntfIdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticUnicastIntfIdList.setStatus("current")


class _PvxStaticUnicastAddressType_Type(Integer32):
    """Custom type pvxStaticUnicastAddressType based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_PvxStaticUnicastAddressType_Type.__name__ = "Integer32"
_PvxStaticUnicastAddressType_Object = MibTableColumn
pvxStaticUnicastAddressType = _PvxStaticUnicastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 6),
    _PvxStaticUnicastAddressType_Type()
)
pvxStaticUnicastAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticUnicastAddressType.setStatus("current")
_PvxStaticUnicastRowStatus_Type = RowStatus
_PvxStaticUnicastRowStatus_Object = MibTableColumn
pvxStaticUnicastRowStatus = _PvxStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 6, 1, 100),
    _PvxStaticUnicastRowStatus_Type()
)
pvxStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticUnicastRowStatus.setStatus("current")
_PvxMultiCastGroupTable_Object = MibTable
pvxMultiCastGroupTable = _PvxMultiCastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7)
)
if mibBuilder.loadTexts:
    pvxMultiCastGroupTable.setStatus("current")
_PvxMultiCastEntry_Object = MibTableRow
pvxMultiCastEntry = _PvxMultiCastEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1)
)
pvxMultiCastEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMCSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMCVlanIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMCMACAddrIdx"),
)
if mibBuilder.loadTexts:
    pvxMultiCastEntry.setStatus("current")


class _PvxMCSwitchIdx_Type(Integer32):
    """Custom type pvxMCSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMCSwitchIdx_Type.__name__ = "Integer32"
_PvxMCSwitchIdx_Object = MibTableColumn
pvxMCSwitchIdx = _PvxMCSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1, 1),
    _PvxMCSwitchIdx_Type()
)
pvxMCSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMCSwitchIdx.setStatus("current")
_PvxMCVlanIdx_Type = Integer32
_PvxMCVlanIdx_Object = MibTableColumn
pvxMCVlanIdx = _PvxMCVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1, 2),
    _PvxMCVlanIdx_Type()
)
pvxMCVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMCVlanIdx.setStatus("current")
_PvxMCMACAddrIdx_Type = MacAddress
_PvxMCMACAddrIdx_Object = MibTableColumn
pvxMCMACAddrIdx = _PvxMCMACAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1, 3),
    _PvxMCMACAddrIdx_Type()
)
pvxMCMACAddrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMCMACAddrIdx.setStatus("current")
_PvxMCIntfIdList_Type = PvxVLANPortList
_PvxMCIntfIdList_Object = MibTableColumn
pvxMCIntfIdList = _PvxMCIntfIdList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1, 4),
    _PvxMCIntfIdList_Type()
)
pvxMCIntfIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMCIntfIdList.setStatus("current")
_PvxMCRowStatus_Type = RowStatus
_PvxMCRowStatus_Object = MibTableColumn
pvxMCRowStatus = _PvxMCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 7, 1, 6),
    _PvxMCRowStatus_Type()
)
pvxMCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMCRowStatus.setStatus("current")
_PvxStaticMulticastTable_Object = MibTable
pvxStaticMulticastTable = _PvxStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8)
)
if mibBuilder.loadTexts:
    pvxStaticMulticastTable.setStatus("current")
_PvxStaticMulticastEntry_Object = MibTableRow
pvxStaticMulticastEntry = _PvxStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1)
)
pvxStaticMulticastEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticMCSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticMCVlanIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticMCMACAddrIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxStaticMCReceivePort"),
)
if mibBuilder.loadTexts:
    pvxStaticMulticastEntry.setStatus("current")


class _PvxStaticMCSwitchIdx_Type(Integer32):
    """Custom type pvxStaticMCSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxStaticMCSwitchIdx_Type.__name__ = "Integer32"
_PvxStaticMCSwitchIdx_Object = MibTableColumn
pvxStaticMCSwitchIdx = _PvxStaticMCSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 1),
    _PvxStaticMCSwitchIdx_Type()
)
pvxStaticMCSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticMCSwitchIdx.setStatus("current")


class _PvxStaticMCVlanIdx_Type(Integer32):
    """Custom type pvxStaticMCVlanIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PvxStaticMCVlanIdx_Type.__name__ = "Integer32"
_PvxStaticMCVlanIdx_Object = MibTableColumn
pvxStaticMCVlanIdx = _PvxStaticMCVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 2),
    _PvxStaticMCVlanIdx_Type()
)
pvxStaticMCVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticMCVlanIdx.setStatus("current")
_PvxStaticMCMACAddrIdx_Type = MacAddress
_PvxStaticMCMACAddrIdx_Object = MibTableColumn
pvxStaticMCMACAddrIdx = _PvxStaticMCMACAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 3),
    _PvxStaticMCMACAddrIdx_Type()
)
pvxStaticMCMACAddrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticMCMACAddrIdx.setStatus("current")
_PvxStaticMCReceivePort_Type = PvxL2Port
_PvxStaticMCReceivePort_Object = MibTableColumn
pvxStaticMCReceivePort = _PvxStaticMCReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 4),
    _PvxStaticMCReceivePort_Type()
)
pvxStaticMCReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxStaticMCReceivePort.setStatus("current")
_PvxStaticMCStaticIntfIdList_Type = PvxVLANPortList
_PvxStaticMCStaticIntfIdList_Object = MibTableColumn
pvxStaticMCStaticIntfIdList = _PvxStaticMCStaticIntfIdList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 5),
    _PvxStaticMCStaticIntfIdList_Type()
)
pvxStaticMCStaticIntfIdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticMCStaticIntfIdList.setStatus("current")
_PvxStaticMCForbiddenIntfIdList_Type = PvxVLANPortList
_PvxStaticMCForbiddenIntfIdList_Object = MibTableColumn
pvxStaticMCForbiddenIntfIdList = _PvxStaticMCForbiddenIntfIdList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 6),
    _PvxStaticMCForbiddenIntfIdList_Type()
)
pvxStaticMCForbiddenIntfIdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticMCForbiddenIntfIdList.setStatus("current")


class _PvxStaticMCAddressType_Type(Integer32):
    """Custom type pvxStaticMCAddressType based on Integer32"""
    defaultValue = 3

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_PvxStaticMCAddressType_Type.__name__ = "Integer32"
_PvxStaticMCAddressType_Object = MibTableColumn
pvxStaticMCAddressType = _PvxStaticMCAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 7),
    _PvxStaticMCAddressType_Type()
)
pvxStaticMCAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticMCAddressType.setStatus("current")
_PvxStaticMCRowStatus_Type = RowStatus
_PvxStaticMCRowStatus_Object = MibTableColumn
pvxStaticMCRowStatus = _PvxStaticMCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 8, 1, 100),
    _PvxStaticMCRowStatus_Type()
)
pvxStaticMCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStaticMCRowStatus.setStatus("current")
_PvxLagTable_Object = MibTable
pvxLagTable = _PvxLagTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9)
)
if mibBuilder.loadTexts:
    pvxLagTable.setStatus("current")
_PvxLagEntry_Object = MibTableRow
pvxLagEntry = _PvxLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1)
)
pvxLagEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagSwitchIdx"),
)
if mibBuilder.loadTexts:
    pvxLagEntry.setStatus("current")


class _PvxLagSwitchIdx_Type(Integer32):
    """Custom type pvxLagSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxLagSwitchIdx_Type.__name__ = "Integer32"
_PvxLagSwitchIdx_Object = MibTableColumn
pvxLagSwitchIdx = _PvxLagSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1, 1),
    _PvxLagSwitchIdx_Type()
)
pvxLagSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagSwitchIdx.setStatus("current")


class _PvxLagState_Type(Integer32):
    """Custom type pvxLagState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxLagState_Type.__name__ = "Integer32"
_PvxLagState_Object = MibTableColumn
pvxLagState = _PvxLagState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1, 2),
    _PvxLagState_Type()
)
pvxLagState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagState.setStatus("current")
_PvxLagSystemPriority_Type = Integer32
_PvxLagSystemPriority_Object = MibTableColumn
pvxLagSystemPriority = _PvxLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1, 3),
    _PvxLagSystemPriority_Type()
)
pvxLagSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagSystemPriority.setStatus("current")
_PvxLagSystemIdentifier_Type = DisplayString
_PvxLagSystemIdentifier_Object = MibTableColumn
pvxLagSystemIdentifier = _PvxLagSystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1, 4),
    _PvxLagSystemIdentifier_Type()
)
pvxLagSystemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLagSystemIdentifier.setStatus("current")
_PvxLagRowStatus_Type = RowStatus
_PvxLagRowStatus_Object = MibTableColumn
pvxLagRowStatus = _PvxLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 9, 1, 100),
    _PvxLagRowStatus_Type()
)
pvxLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagRowStatus.setStatus("current")
_PvxLagGroupTable_Object = MibTable
pvxLagGroupTable = _PvxLagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10)
)
if mibBuilder.loadTexts:
    pvxLagGroupTable.setStatus("current")
_PvxLagGroupEntry_Object = MibTableRow
pvxLagGroupEntry = _PvxLagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1)
)
pvxLagGroupEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLGSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLGIdx"),
)
if mibBuilder.loadTexts:
    pvxLagGroupEntry.setStatus("current")


class _PvxLGSwitchIdx_Type(Integer32):
    """Custom type pvxLGSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxLGSwitchIdx_Type.__name__ = "Integer32"
_PvxLGSwitchIdx_Object = MibTableColumn
pvxLGSwitchIdx = _PvxLGSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 1),
    _PvxLGSwitchIdx_Type()
)
pvxLGSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLGSwitchIdx.setStatus("current")
_PvxLGIdx_Type = Integer32
_PvxLGIdx_Object = MibTableColumn
pvxLGIdx = _PvxLGIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 2),
    _PvxLGIdx_Type()
)
pvxLGIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLGIdx.setStatus("current")
_PvxLGPortList_Type = PvxPhyPortList
_PvxLGPortList_Object = MibTableColumn
pvxLGPortList = _PvxLGPortList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 3),
    _PvxLGPortList_Type()
)
pvxLGPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGPortList.setStatus("current")


class _PvxLGDistribution_Type(Integer32):
    """Custom type pvxLGDistribution based on Integer32"""
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
        *(("dstip", 5),
          ("dstmac", 2),
          ("srcdstip", 6),
          ("srcdstmac", 3),
          ("srcip", 4),
          ("srcmac", 1))
    )


_PvxLGDistribution_Type.__name__ = "Integer32"
_PvxLGDistribution_Object = MibTableColumn
pvxLGDistribution = _PvxLGDistribution_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 4),
    _PvxLGDistribution_Type()
)
pvxLGDistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGDistribution.setStatus("current")
_PvxLGMacAddress_Type = MacAddress
_PvxLGMacAddress_Object = MibTableColumn
pvxLGMacAddress = _PvxLGMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 6),
    _PvxLGMacAddress_Type()
)
pvxLGMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGMacAddress.setStatus("current")
_PvxLGPortCount_Type = Integer32
_PvxLGPortCount_Object = MibTableColumn
pvxLGPortCount = _PvxLGPortCount_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 7),
    _PvxLGPortCount_Type()
)
pvxLGPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGPortCount.setStatus("current")
_PvxLGActivePortCount_Type = Integer32
_PvxLGActivePortCount_Object = MibTableColumn
pvxLGActivePortCount = _PvxLGActivePortCount_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 8),
    _PvxLGActivePortCount_Type()
)
pvxLGActivePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGActivePortCount.setStatus("current")
_PvxLGMtuSize_Type = Integer32
_PvxLGMtuSize_Object = MibTableColumn
pvxLGMtuSize = _PvxLGMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 9),
    _PvxLGMtuSize_Type()
)
pvxLGMtuSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGMtuSize.setStatus("current")


class _PvxLGAdminStatus_Type(Integer32):
    """Custom type pvxLGAdminStatus based on Integer32"""
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


_PvxLGAdminStatus_Type.__name__ = "Integer32"
_PvxLGAdminStatus_Object = MibTableColumn
pvxLGAdminStatus = _PvxLGAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 10),
    _PvxLGAdminStatus_Type()
)
pvxLGAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGAdminStatus.setStatus("current")
_PvxLGOperStatus_Type = OperStatus
_PvxLGOperStatus_Object = MibTableColumn
pvxLGOperStatus = _PvxLGOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 11),
    _PvxLGOperStatus_Type()
)
pvxLGOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGOperStatus.setStatus("current")


class _PvxLGDataRate_Type(Integer32):
    """Custom type pvxLGDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_PvxLGDataRate_Type.__name__ = "Integer32"
_PvxLGDataRate_Object = MibTableColumn
pvxLGDataRate = _PvxLGDataRate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 12),
    _PvxLGDataRate_Type()
)
pvxLGDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLGDataRate.setStatus("current")


class _PvxLGMaxLinks_Type(Integer32):
    """Custom type pvxLGMaxLinks based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PvxLGMaxLinks_Type.__name__ = "Integer32"
_PvxLGMaxLinks_Object = MibTableColumn
pvxLGMaxLinks = _PvxLGMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 13),
    _PvxLGMaxLinks_Type()
)
pvxLGMaxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGMaxLinks.setStatus("current")


class _PvxLGMinLinks_Type(Integer32):
    """Custom type pvxLGMinLinks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PvxLGMinLinks_Type.__name__ = "Integer32"
_PvxLGMinLinks_Object = MibTableColumn
pvxLGMinLinks = _PvxLGMinLinks_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 14),
    _PvxLGMinLinks_Type()
)
pvxLGMinLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGMinLinks.setStatus("current")
_PvxLGRowStatus_Type = RowStatus
_PvxLGRowStatus_Object = MibTableColumn
pvxLGRowStatus = _PvxLGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 10, 1, 100),
    _PvxLGRowStatus_Type()
)
pvxLGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLGRowStatus.setStatus("current")
_PvxLagPortTable_Object = MibTable
pvxLagPortTable = _PvxLagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11)
)
if mibBuilder.loadTexts:
    pvxLagPortTable.setStatus("current")
_PvxLagPortEntry_Object = MibTableRow
pvxLagPortEntry = _PvxLagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1)
)
pvxLagPortEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagPortSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagPortShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagPortSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxLagPortIdx"),
)
if mibBuilder.loadTexts:
    pvxLagPortEntry.setStatus("current")


class _PvxLagPortSwitchIdx_Type(Integer32):
    """Custom type pvxLagPortSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxLagPortSwitchIdx_Type.__name__ = "Integer32"
_PvxLagPortSwitchIdx_Object = MibTableColumn
pvxLagPortSwitchIdx = _PvxLagPortSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 1),
    _PvxLagPortSwitchIdx_Type()
)
pvxLagPortSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagPortSwitchIdx.setStatus("current")


class _PvxLagPortShelfIdx_Type(Integer32):
    """Custom type pvxLagPortShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxLagPortShelfIdx_Type.__name__ = "Integer32"
_PvxLagPortShelfIdx_Object = MibTableColumn
pvxLagPortShelfIdx = _PvxLagPortShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 2),
    _PvxLagPortShelfIdx_Type()
)
pvxLagPortShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagPortShelfIdx.setStatus("current")


class _PvxLagPortSlotIdx_Type(Integer32):
    """Custom type pvxLagPortSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxLagPortSlotIdx_Type.__name__ = "Integer32"
_PvxLagPortSlotIdx_Object = MibTableColumn
pvxLagPortSlotIdx = _PvxLagPortSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 3),
    _PvxLagPortSlotIdx_Type()
)
pvxLagPortSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagPortSlotIdx.setStatus("current")
_PvxLagPortTypeIdx_Type = PvxPortType
_PvxLagPortTypeIdx_Object = MibTableColumn
pvxLagPortTypeIdx = _PvxLagPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 4),
    _PvxLagPortTypeIdx_Type()
)
pvxLagPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagPortTypeIdx.setStatus("current")
_PvxLagPortIdx_Type = Integer32
_PvxLagPortIdx_Object = MibTableColumn
pvxLagPortIdx = _PvxLagPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 5),
    _PvxLagPortIdx_Type()
)
pvxLagPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxLagPortIdx.setStatus("current")
_PvxLagPortPriority_Type = Integer32
_PvxLagPortPriority_Object = MibTableColumn
pvxLagPortPriority = _PvxLagPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 6),
    _PvxLagPortPriority_Type()
)
pvxLagPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortPriority.setStatus("current")


class _PvxLagPortMode_Type(Integer32):
    """Custom type pvxLagPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("on", 3),
          ("passive", 2))
    )


_PvxLagPortMode_Type.__name__ = "Integer32"
_PvxLagPortMode_Object = MibTableColumn
pvxLagPortMode = _PvxLagPortMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 7),
    _PvxLagPortMode_Type()
)
pvxLagPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortMode.setStatus("current")


class _PvxLagPortAggState_Type(Integer32):
    """Custom type pvxLagPortAggState based on Integer32"""
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
        *(("alone", 4),
          ("down", 3),
          ("inbndl", 1),
          ("stdby", 2))
    )


_PvxLagPortAggState_Type.__name__ = "Integer32"
_PvxLagPortAggState_Object = MibTableColumn
pvxLagPortAggState = _PvxLagPortAggState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 8),
    _PvxLagPortAggState_Type()
)
pvxLagPortAggState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLagPortAggState.setStatus("current")
_PvxLagPortLcapId_Type = Integer32
_PvxLagPortLcapId_Object = MibTableColumn
pvxLagPortLcapId = _PvxLagPortLcapId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 9),
    _PvxLagPortLcapId_Type()
)
pvxLagPortLcapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortLcapId.setStatus("current")


class _PvxLagPortTimeout_Type(Integer32):
    """Custom type pvxLagPortTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_PvxLagPortTimeout_Type.__name__ = "Integer32"
_PvxLagPortTimeout_Object = MibTableColumn
pvxLagPortTimeout = _PvxLagPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 10),
    _PvxLagPortTimeout_Type()
)
pvxLagPortTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortTimeout.setStatus("current")
_PvxLagPortWaitTime_Type = Integer32
_PvxLagPortWaitTime_Object = MibTableColumn
pvxLagPortWaitTime = _PvxLagPortWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 11),
    _PvxLagPortWaitTime_Type()
)
pvxLagPortWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortWaitTime.setStatus("current")
_PvxLagPortActAdminState_Type = Integer32
_PvxLagPortActAdminState_Object = MibTableColumn
pvxLagPortActAdminState = _PvxLagPortActAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 12),
    _PvxLagPortActAdminState_Type()
)
pvxLagPortActAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLagPortActAdminState.setStatus("current")
_PvxLagPortPrtnrAdminState_Type = Integer32
_PvxLagPortPrtnrAdminState_Object = MibTableColumn
pvxLagPortPrtnrAdminState = _PvxLagPortPrtnrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 13),
    _PvxLagPortPrtnrAdminState_Type()
)
pvxLagPortPrtnrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxLagPortPrtnrAdminState.setStatus("current")
_PvxLagPortGroupId_Type = Integer32
_PvxLagPortGroupId_Object = MibTableColumn
pvxLagPortGroupId = _PvxLagPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 14),
    _PvxLagPortGroupId_Type()
)
pvxLagPortGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortGroupId.setStatus("current")
_PvxLagPortRowStatus_Type = RowStatus
_PvxLagPortRowStatus_Object = MibTableColumn
pvxLagPortRowStatus = _PvxLagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 11, 1, 100),
    _PvxLagPortRowStatus_Type()
)
pvxLagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxLagPortRowStatus.setStatus("current")
_PvxMSTPGenTable_Object = MibTable
pvxMSTPGenTable = _PvxMSTPGenTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12)
)
if mibBuilder.loadTexts:
    pvxMSTPGenTable.setStatus("current")
_PvxMSTPGenEntry_Object = MibTableRow
pvxMSTPGenEntry = _PvxMSTPGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1)
)
pvxMSTPGenEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPGenEntry.setStatus("current")


class _PvxMSTPGenSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPGenSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPGenSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPGenSwitchIdx_Object = MibTableColumn
pvxMSTPGenSwitchIdx = _PvxMSTPGenSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 1),
    _PvxMSTPGenSwitchIdx_Type()
)
pvxMSTPGenSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPGenSwitchIdx.setStatus("current")


class _PvxMSTPGenMaxHops_Type(Integer32):
    """Custom type pvxMSTPGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_PvxMSTPGenMaxHops_Type.__name__ = "Integer32"
_PvxMSTPGenMaxHops_Object = MibTableColumn
pvxMSTPGenMaxHops = _PvxMSTPGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 2),
    _PvxMSTPGenMaxHops_Type()
)
pvxMSTPGenMaxHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPGenMaxHops.setStatus("current")


class _PvxMSTPGenVersionSupported_Type(Integer32):
    """Custom type pvxMSTPGenVersionSupported based on Integer32"""
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
        *(("dot1d", 3),
          ("dot1q", 6),
          ("dot1s", 5),
          ("dot1w", 4),
          ("nonStp", 2),
          ("unknown", 1))
    )


_PvxMSTPGenVersionSupported_Type.__name__ = "Integer32"
_PvxMSTPGenVersionSupported_Object = MibTableColumn
pvxMSTPGenVersionSupported = _PvxMSTPGenVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 3),
    _PvxMSTPGenVersionSupported_Type()
)
pvxMSTPGenVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenVersionSupported.setStatus("current")
_PvxMSTPGenIdFmtSel_Type = Integer32
_PvxMSTPGenIdFmtSel_Object = MibTableColumn
pvxMSTPGenIdFmtSel = _PvxMSTPGenIdFmtSel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 4),
    _PvxMSTPGenIdFmtSel_Type()
)
pvxMSTPGenIdFmtSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenIdFmtSel.setStatus("current")
_PvxMSTPGenIdName_Type = DisplayString
_PvxMSTPGenIdName_Object = MibTableColumn
pvxMSTPGenIdName = _PvxMSTPGenIdName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 5),
    _PvxMSTPGenIdName_Type()
)
pvxMSTPGenIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPGenIdName.setStatus("current")
_PvxMSTPGenIdRevisionLevel_Type = Integer32
_PvxMSTPGenIdRevisionLevel_Object = MibTableColumn
pvxMSTPGenIdRevisionLevel = _PvxMSTPGenIdRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 6),
    _PvxMSTPGenIdRevisionLevel_Type()
)
pvxMSTPGenIdRevisionLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPGenIdRevisionLevel.setStatus("current")
_PvxMSTPGenIdDigest_Type = DisplayString
_PvxMSTPGenIdDigest_Object = MibTableColumn
pvxMSTPGenIdDigest = _PvxMSTPGenIdDigest_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 7),
    _PvxMSTPGenIdDigest_Type()
)
pvxMSTPGenIdDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenIdDigest.setStatus("current")
_PvxMSTPGenRegionalRoot_Type = DisplayString
_PvxMSTPGenRegionalRoot_Object = MibTableColumn
pvxMSTPGenRegionalRoot = _PvxMSTPGenRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 8),
    _PvxMSTPGenRegionalRoot_Type()
)
pvxMSTPGenRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenRegionalRoot.setStatus("current")
_PvxMSTPGenExternalRootCost_Type = Integer32
_PvxMSTPGenExternalRootCost_Object = MibTableColumn
pvxMSTPGenExternalRootCost = _PvxMSTPGenExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 9),
    _PvxMSTPGenExternalRootCost_Type()
)
pvxMSTPGenExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenExternalRootCost.setStatus("current")


class _PvxMSTPGenCistPriority_Type(Integer32):
    """Custom type pvxMSTPGenCistPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_PvxMSTPGenCistPriority_Type.__name__ = "Integer32"
_PvxMSTPGenCistPriority_Object = MibTableColumn
pvxMSTPGenCistPriority = _PvxMSTPGenCistPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 10),
    _PvxMSTPGenCistPriority_Type()
)
pvxMSTPGenCistPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPGenCistPriority.setStatus("current")
_PvxMSTPGenBrdgId_Type = DisplayString
_PvxMSTPGenBrdgId_Object = MibTableColumn
pvxMSTPGenBrdgId = _PvxMSTPGenBrdgId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 11),
    _PvxMSTPGenBrdgId_Type()
)
pvxMSTPGenBrdgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenBrdgId.setStatus("current")
_PvxMSTPGenCistRoot_Type = DisplayString
_PvxMSTPGenCistRoot_Object = MibTableColumn
pvxMSTPGenCistRoot = _PvxMSTPGenCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 12),
    _PvxMSTPGenCistRoot_Type()
)
pvxMSTPGenCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenCistRoot.setStatus("current")


class _PvxMSTPGenCistRootPriority_Type(Integer32):
    """Custom type pvxMSTPGenCistRootPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_PvxMSTPGenCistRootPriority_Type.__name__ = "Integer32"
_PvxMSTPGenCistRootPriority_Object = MibTableColumn
pvxMSTPGenCistRootPriority = _PvxMSTPGenCistRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 13),
    _PvxMSTPGenCistRootPriority_Type()
)
pvxMSTPGenCistRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenCistRootPriority.setStatus("current")
_PvxMSTPGenCistRootCost_Type = Integer32
_PvxMSTPGenCistRootCost_Object = MibTableColumn
pvxMSTPGenCistRootCost = _PvxMSTPGenCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 12, 1, 14),
    _PvxMSTPGenCistRootCost_Type()
)
pvxMSTPGenCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPGenCistRootCost.setStatus("current")
_PvxMSTPMapTable_Object = MibTable
pvxMSTPMapTable = _PvxMSTPMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13)
)
if mibBuilder.loadTexts:
    pvxMSTPMapTable.setStatus("current")
_PvxMSTPMapEntry_Object = MibTableRow
pvxMSTPMapEntry = _PvxMSTPMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1)
)
pvxMSTPMapEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPMapSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPMapIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPMapEntry.setStatus("current")


class _PvxMSTPMapSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPMapSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPMapSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPMapSwitchIdx_Object = MibTableColumn
pvxMSTPMapSwitchIdx = _PvxMSTPMapSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 1),
    _PvxMSTPMapSwitchIdx_Type()
)
pvxMSTPMapSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPMapSwitchIdx.setStatus("current")
_PvxMSTPMapIdx_Type = Integer32
_PvxMSTPMapIdx_Object = MibTableColumn
pvxMSTPMapIdx = _PvxMSTPMapIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 2),
    _PvxMSTPMapIdx_Type()
)
pvxMSTPMapIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPMapIdx.setStatus("current")
_PvxMSTPMapVlanS1k_Type = PvxMSTPVlanList
_PvxMSTPMapVlanS1k_Object = MibTableColumn
pvxMSTPMapVlanS1k = _PvxMSTPMapVlanS1k_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 3),
    _PvxMSTPMapVlanS1k_Type()
)
pvxMSTPMapVlanS1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPMapVlanS1k.setStatus("current")
_PvxMSTPMapVlanS2k_Type = PvxMSTPVlanList
_PvxMSTPMapVlanS2k_Object = MibTableColumn
pvxMSTPMapVlanS2k = _PvxMSTPMapVlanS2k_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 4),
    _PvxMSTPMapVlanS2k_Type()
)
pvxMSTPMapVlanS2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPMapVlanS2k.setStatus("current")
_PvxMSTPMapVlanS3k_Type = PvxMSTPVlanList
_PvxMSTPMapVlanS3k_Object = MibTableColumn
pvxMSTPMapVlanS3k = _PvxMSTPMapVlanS3k_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 5),
    _PvxMSTPMapVlanS3k_Type()
)
pvxMSTPMapVlanS3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPMapVlanS3k.setStatus("current")
_PvxMSTPMapVlanS4k_Type = PvxMSTPVlanList
_PvxMSTPMapVlanS4k_Object = MibTableColumn
pvxMSTPMapVlanS4k = _PvxMSTPMapVlanS4k_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 6),
    _PvxMSTPMapVlanS4k_Type()
)
pvxMSTPMapVlanS4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPMapVlanS4k.setStatus("current")
_PvxMSTPMapRowStatus_Type = RowStatus
_PvxMSTPMapRowStatus_Object = MibTableColumn
pvxMSTPMapRowStatus = _PvxMSTPMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 13, 1, 100),
    _PvxMSTPMapRowStatus_Type()
)
pvxMSTPMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPMapRowStatus.setStatus("current")
_PvxMSTPPortTable_Object = MibTable
pvxMSTPPortTable = _PvxMSTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14)
)
if mibBuilder.loadTexts:
    pvxMSTPPortTable.setStatus("current")
_PvxMSTPPortEntry_Object = MibTableRow
pvxMSTPPortEntry = _PvxMSTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1)
)
pvxMSTPPortEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPPortIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPPortEntry.setStatus("current")


class _PvxMSTPPortSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPPortSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPPortSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPPortSwitchIdx_Object = MibTableColumn
pvxMSTPPortSwitchIdx = _PvxMSTPPortSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 1),
    _PvxMSTPPortSwitchIdx_Type()
)
pvxMSTPPortSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortSwitchIdx.setStatus("current")


class _PvxMSTPPortShelfIdx_Type(Integer32):
    """Custom type pvxMSTPPortShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxMSTPPortShelfIdx_Type.__name__ = "Integer32"
_PvxMSTPPortShelfIdx_Object = MibTableColumn
pvxMSTPPortShelfIdx = _PvxMSTPPortShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 2),
    _PvxMSTPPortShelfIdx_Type()
)
pvxMSTPPortShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortShelfIdx.setStatus("current")


class _PvxMSTPPortSlotIdx_Type(Integer32):
    """Custom type pvxMSTPPortSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxMSTPPortSlotIdx_Type.__name__ = "Integer32"
_PvxMSTPPortSlotIdx_Object = MibTableColumn
pvxMSTPPortSlotIdx = _PvxMSTPPortSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 3),
    _PvxMSTPPortSlotIdx_Type()
)
pvxMSTPPortSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortSlotIdx.setStatus("current")
_PvxMSTPPortTypeIdx_Type = PvxPortType
_PvxMSTPPortTypeIdx_Object = MibTableColumn
pvxMSTPPortTypeIdx = _PvxMSTPPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 4),
    _PvxMSTPPortTypeIdx_Type()
)
pvxMSTPPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortTypeIdx.setStatus("current")
_PvxMSTPPortIdx_Type = Integer32
_PvxMSTPPortIdx_Object = MibTableColumn
pvxMSTPPortIdx = _PvxMSTPPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 5),
    _PvxMSTPPortIdx_Type()
)
pvxMSTPPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPPortIdx.setStatus("current")
_PvxMSTPPortDesignatedRoot_Type = DisplayString
_PvxMSTPPortDesignatedRoot_Object = MibTableColumn
pvxMSTPPortDesignatedRoot = _PvxMSTPPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 6),
    _PvxMSTPPortDesignatedRoot_Type()
)
pvxMSTPPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortDesignatedRoot.setStatus("current")
_PvxMSTPPortDesignatedBridge_Type = DisplayString
_PvxMSTPPortDesignatedBridge_Object = MibTableColumn
pvxMSTPPortDesignatedBridge = _PvxMSTPPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 7),
    _PvxMSTPPortDesignatedBridge_Type()
)
pvxMSTPPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortDesignatedBridge.setStatus("current")
_PvxMSTPPortDesignatedPort_Type = Integer32
_PvxMSTPPortDesignatedPort_Object = MibTableColumn
pvxMSTPPortDesignatedPort = _PvxMSTPPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 8),
    _PvxMSTPPortDesignatedPort_Type()
)
pvxMSTPPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortDesignatedPort.setStatus("current")
_PvxMSTPPortPathCost_Type = Integer32
_PvxMSTPPortPathCost_Object = MibTableColumn
pvxMSTPPortPathCost = _PvxMSTPPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 9),
    _PvxMSTPPortPathCost_Type()
)
pvxMSTPPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortPathCost.setStatus("current")
_PvxMSTPPortPriority_Type = Integer32
_PvxMSTPPortPriority_Object = MibTableColumn
pvxMSTPPortPriority = _PvxMSTPPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 10),
    _PvxMSTPPortPriority_Type()
)
pvxMSTPPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortPriority.setStatus("current")


class _PvxMSTPPortState_Type(Integer32):
    """Custom type pvxMSTPPortState based on Integer32"""
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
        *(("disabled", 2),
          ("discarding", 3),
          ("forwarding", 5),
          ("learning", 4),
          ("unknown", 1))
    )


_PvxMSTPPortState_Type.__name__ = "Integer32"
_PvxMSTPPortState_Object = MibTableColumn
pvxMSTPPortState = _PvxMSTPPortState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 11),
    _PvxMSTPPortState_Type()
)
pvxMSTPPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortState.setStatus("current")


class _PvxMSTPPortRole_Type(Integer32):
    """Custom type pvxMSTPPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("nonSTP", 6),
          ("root", 4))
    )


_PvxMSTPPortRole_Type.__name__ = "Integer32"
_PvxMSTPPortRole_Object = MibTableColumn
pvxMSTPPortRole = _PvxMSTPPortRole_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 12),
    _PvxMSTPPortRole_Type()
)
pvxMSTPPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortRole.setStatus("current")
_PvxMSTPPortRegRoot_Type = DisplayString
_PvxMSTPPortRegRoot_Object = MibTableColumn
pvxMSTPPortRegRoot = _PvxMSTPPortRegRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 13),
    _PvxMSTPPortRegRoot_Type()
)
pvxMSTPPortRegRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortRegRoot.setStatus("current")
_PvxMSTPPortRegRootCost_Type = Integer32
_PvxMSTPPortRegRootCost_Object = MibTableColumn
pvxMSTPPortRegRootCost = _PvxMSTPPortRegRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 14),
    _PvxMSTPPortRegRootCost_Type()
)
pvxMSTPPortRegRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPPortRegRootCost.setStatus("current")
_PvxMSTPPortRestrictedRole_Type = TruthValue
_PvxMSTPPortRestrictedRole_Object = MibTableColumn
pvxMSTPPortRestrictedRole = _PvxMSTPPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 15),
    _PvxMSTPPortRestrictedRole_Type()
)
pvxMSTPPortRestrictedRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortRestrictedRole.setStatus("current")
_PvxMSTPPortRestrictedTCN_Type = TruthValue
_PvxMSTPPortRestrictedTCN_Object = MibTableColumn
pvxMSTPPortRestrictedTCN = _PvxMSTPPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 16),
    _PvxMSTPPortRestrictedTCN_Type()
)
pvxMSTPPortRestrictedTCN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortRestrictedTCN.setStatus("current")


class _PvxMSTPPortForcedPortState_Type(Integer32):
    """Custom type pvxMSTPPortForcedPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxMSTPPortForcedPortState_Type.__name__ = "Integer32"
_PvxMSTPPortForcedPortState_Object = MibTableColumn
pvxMSTPPortForcedPortState = _PvxMSTPPortForcedPortState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 17),
    _PvxMSTPPortForcedPortState_Type()
)
pvxMSTPPortForcedPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortForcedPortState.setStatus("current")


class _PvxMSTPPortLoopGuardState_Type(Integer32):
    """Custom type pvxMSTPPortLoopGuardState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxMSTPPortLoopGuardState_Type.__name__ = "Integer32"
_PvxMSTPPortLoopGuardState_Object = MibTableColumn
pvxMSTPPortLoopGuardState = _PvxMSTPPortLoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 18),
    _PvxMSTPPortLoopGuardState_Type()
)
pvxMSTPPortLoopGuardState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortLoopGuardState.setStatus("current")


class _PvxMSTPPortLinkType_Type(Integer32):
    """Custom type pvxMSTPPortLinkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-point", 2),
          ("shared", 1))
    )


_PvxMSTPPortLinkType_Type.__name__ = "Integer32"
_PvxMSTPPortLinkType_Object = MibTableColumn
pvxMSTPPortLinkType = _PvxMSTPPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 14, 1, 19),
    _PvxMSTPPortLinkType_Type()
)
pvxMSTPPortLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPPortLinkType.setStatus("current")
_PvxMSTPXstTable_Object = MibTable
pvxMSTPXstTable = _PvxMSTPXstTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15)
)
if mibBuilder.loadTexts:
    pvxMSTPXstTable.setStatus("current")
_PvxMSTPXstEntry_Object = MibTableRow
pvxMSTPXstEntry = _PvxMSTPXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1)
)
pvxMSTPXstEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPXstEntry.setStatus("current")


class _PvxMSTPXstSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPXstSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPXstSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPXstSwitchIdx_Object = MibTableColumn
pvxMSTPXstSwitchIdx = _PvxMSTPXstSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 1),
    _PvxMSTPXstSwitchIdx_Type()
)
pvxMSTPXstSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstSwitchIdx.setStatus("current")


class _PvxMSTPXstIdx_Type(Integer32):
    """Custom type pvxMSTPXstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PvxMSTPXstIdx_Type.__name__ = "Integer32"
_PvxMSTPXstIdx_Object = MibTableColumn
pvxMSTPXstIdx = _PvxMSTPXstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 2),
    _PvxMSTPXstIdx_Type()
)
pvxMSTPXstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstIdx.setStatus("current")


class _PvxMSTPXstBrdgPriority_Type(Integer32):
    """Custom type pvxMSTPXstBrdgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_PvxMSTPXstBrdgPriority_Type.__name__ = "Integer32"
_PvxMSTPXstBrdgPriority_Object = MibTableColumn
pvxMSTPXstBrdgPriority = _PvxMSTPXstBrdgPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 3),
    _PvxMSTPXstBrdgPriority_Type()
)
pvxMSTPXstBrdgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPXstBrdgPriority.setStatus("current")
_PvxMSTPXstBrdgId_Type = DisplayString
_PvxMSTPXstBrdgId_Object = MibTableColumn
pvxMSTPXstBrdgId = _PvxMSTPXstBrdgId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 4),
    _PvxMSTPXstBrdgId_Type()
)
pvxMSTPXstBrdgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstBrdgId.setStatus("current")
_PvxMSTPXstBrdgRegRoot_Type = DisplayString
_PvxMSTPXstBrdgRegRoot_Object = MibTableColumn
pvxMSTPXstBrdgRegRoot = _PvxMSTPXstBrdgRegRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 5),
    _PvxMSTPXstBrdgRegRoot_Type()
)
pvxMSTPXstBrdgRegRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstBrdgRegRoot.setStatus("current")


class _PvxMSTPXstBrdgRegRootCost_Type(Integer32):
    """Custom type pvxMSTPXstBrdgRegRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvxMSTPXstBrdgRegRootCost_Type.__name__ = "Integer32"
_PvxMSTPXstBrdgRegRootCost_Object = MibTableColumn
pvxMSTPXstBrdgRegRootCost = _PvxMSTPXstBrdgRegRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 6),
    _PvxMSTPXstBrdgRegRootCost_Type()
)
pvxMSTPXstBrdgRegRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstBrdgRegRootCost.setStatus("current")
_PvxMSTPXstRootPort_Type = PvxL2Port
_PvxMSTPXstRootPort_Object = MibTableColumn
pvxMSTPXstRootPort = _PvxMSTPXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 7),
    _PvxMSTPXstRootPort_Type()
)
pvxMSTPXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPort.setStatus("deprecated")


class _PvxMSTPXstRootPortSwitch_Type(Integer32):
    """Custom type pvxMSTPXstRootPortSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPXstRootPortSwitch_Type.__name__ = "Integer32"
_PvxMSTPXstRootPortSwitch_Object = MibTableColumn
pvxMSTPXstRootPortSwitch = _PvxMSTPXstRootPortSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 8),
    _PvxMSTPXstRootPortSwitch_Type()
)
pvxMSTPXstRootPortSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPortSwitch.setStatus("current")


class _PvxMSTPXstRootPortShelf_Type(Integer32):
    """Custom type pvxMSTPXstRootPortShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxMSTPXstRootPortShelf_Type.__name__ = "Integer32"
_PvxMSTPXstRootPortShelf_Object = MibTableColumn
pvxMSTPXstRootPortShelf = _PvxMSTPXstRootPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 9),
    _PvxMSTPXstRootPortShelf_Type()
)
pvxMSTPXstRootPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPortShelf.setStatus("current")


class _PvxMSTPXstRootPortSlot_Type(Integer32):
    """Custom type pvxMSTPXstRootPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxMSTPXstRootPortSlot_Type.__name__ = "Integer32"
_PvxMSTPXstRootPortSlot_Object = MibTableColumn
pvxMSTPXstRootPortSlot = _PvxMSTPXstRootPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 10),
    _PvxMSTPXstRootPortSlot_Type()
)
pvxMSTPXstRootPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPortSlot.setStatus("current")
_PvxMSTPXstRootPortType_Type = PvxPortType
_PvxMSTPXstRootPortType_Object = MibTableColumn
pvxMSTPXstRootPortType = _PvxMSTPXstRootPortType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 11),
    _PvxMSTPXstRootPortType_Type()
)
pvxMSTPXstRootPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPortType.setStatus("current")


class _PvxMSTPXstRootPortNum_Type(Integer32):
    """Custom type pvxMSTPXstRootPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_PvxMSTPXstRootPortNum_Type.__name__ = "Integer32"
_PvxMSTPXstRootPortNum_Object = MibTableColumn
pvxMSTPXstRootPortNum = _PvxMSTPXstRootPortNum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 15, 1, 12),
    _PvxMSTPXstRootPortNum_Type()
)
pvxMSTPXstRootPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstRootPortNum.setStatus("current")
_PvxMSTPXstPortTable_Object = MibTable
pvxMSTPXstPortTable = _PvxMSTPXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16)
)
if mibBuilder.loadTexts:
    pvxMSTPXstPortTable.setStatus("current")
_PvxMSTPXstPortEntry_Object = MibTableRow
pvxMSTPXstPortEntry = _PvxMSTPXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1)
)
pvxMSTPXstPortEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortInstIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMSTPXstPortIdx"),
)
if mibBuilder.loadTexts:
    pvxMSTPXstPortEntry.setStatus("current")


class _PvxMSTPXstPortSwitchIdx_Type(Integer32):
    """Custom type pvxMSTPXstPortSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMSTPXstPortSwitchIdx_Type.__name__ = "Integer32"
_PvxMSTPXstPortSwitchIdx_Object = MibTableColumn
pvxMSTPXstPortSwitchIdx = _PvxMSTPXstPortSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 1),
    _PvxMSTPXstPortSwitchIdx_Type()
)
pvxMSTPXstPortSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortSwitchIdx.setStatus("current")


class _PvxMSTPXstPortShelfIdx_Type(Integer32):
    """Custom type pvxMSTPXstPortShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxMSTPXstPortShelfIdx_Type.__name__ = "Integer32"
_PvxMSTPXstPortShelfIdx_Object = MibTableColumn
pvxMSTPXstPortShelfIdx = _PvxMSTPXstPortShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 2),
    _PvxMSTPXstPortShelfIdx_Type()
)
pvxMSTPXstPortShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortShelfIdx.setStatus("current")


class _PvxMSTPXstPortSlotIdx_Type(Integer32):
    """Custom type pvxMSTPXstPortSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxMSTPXstPortSlotIdx_Type.__name__ = "Integer32"
_PvxMSTPXstPortSlotIdx_Object = MibTableColumn
pvxMSTPXstPortSlotIdx = _PvxMSTPXstPortSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 3),
    _PvxMSTPXstPortSlotIdx_Type()
)
pvxMSTPXstPortSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortSlotIdx.setStatus("current")
_PvxMSTPXstPortTypeIdx_Type = PvxPortType
_PvxMSTPXstPortTypeIdx_Object = MibTableColumn
pvxMSTPXstPortTypeIdx = _PvxMSTPXstPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 4),
    _PvxMSTPXstPortTypeIdx_Type()
)
pvxMSTPXstPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortTypeIdx.setStatus("current")


class _PvxMSTPXstPortInstIdx_Type(Integer32):
    """Custom type pvxMSTPXstPortInstIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PvxMSTPXstPortInstIdx_Type.__name__ = "Integer32"
_PvxMSTPXstPortInstIdx_Object = MibTableColumn
pvxMSTPXstPortInstIdx = _PvxMSTPXstPortInstIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 5),
    _PvxMSTPXstPortInstIdx_Type()
)
pvxMSTPXstPortInstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortInstIdx.setStatus("current")


class _PvxMSTPXstPortIdx_Type(Integer32):
    """Custom type pvxMSTPXstPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_PvxMSTPXstPortIdx_Type.__name__ = "Integer32"
_PvxMSTPXstPortIdx_Object = MibTableColumn
pvxMSTPXstPortIdx = _PvxMSTPXstPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 6),
    _PvxMSTPXstPortIdx_Type()
)
pvxMSTPXstPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMSTPXstPortIdx.setStatus("current")


class _PvxMSTPXstPortState_Type(Integer32):
    """Custom type pvxMSTPXstPortState based on Integer32"""
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
        *(("disabled", 2),
          ("discarding", 3),
          ("forwarding", 5),
          ("learning", 4),
          ("unknown", 1))
    )


_PvxMSTPXstPortState_Type.__name__ = "Integer32"
_PvxMSTPXstPortState_Object = MibTableColumn
pvxMSTPXstPortState = _PvxMSTPXstPortState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 7),
    _PvxMSTPXstPortState_Type()
)
pvxMSTPXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortState.setStatus("current")


class _PvxMSTPXstPortRole_Type(Integer32):
    """Custom type pvxMSTPXstPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("master", 6),
          ("nonSTP", 7),
          ("root", 4))
    )


_PvxMSTPXstPortRole_Type.__name__ = "Integer32"
_PvxMSTPXstPortRole_Object = MibTableColumn
pvxMSTPXstPortRole = _PvxMSTPXstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 8),
    _PvxMSTPXstPortRole_Type()
)
pvxMSTPXstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortRole.setStatus("current")
_PvxMSTPXstPortDesigRoot_Type = DisplayString
_PvxMSTPXstPortDesigRoot_Object = MibTableColumn
pvxMSTPXstPortDesigRoot = _PvxMSTPXstPortDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 9),
    _PvxMSTPXstPortDesigRoot_Type()
)
pvxMSTPXstPortDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortDesigRoot.setStatus("current")
_PvxMSTPXstPortDesigCost_Type = Integer32
_PvxMSTPXstPortDesigCost_Object = MibTableColumn
pvxMSTPXstPortDesigCost = _PvxMSTPXstPortDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 10),
    _PvxMSTPXstPortDesigCost_Type()
)
pvxMSTPXstPortDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortDesigCost.setStatus("current")
_PvxMSTPXstPortDesigBridge_Type = DisplayString
_PvxMSTPXstPortDesigBridge_Object = MibTableColumn
pvxMSTPXstPortDesigBridge = _PvxMSTPXstPortDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 11),
    _PvxMSTPXstPortDesigBridge_Type()
)
pvxMSTPXstPortDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortDesigBridge.setStatus("current")
_PvxMSTPXstPortDesigPortId_Type = Integer32
_PvxMSTPXstPortDesigPortId_Object = MibTableColumn
pvxMSTPXstPortDesigPortId = _PvxMSTPXstPortDesigPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 12),
    _PvxMSTPXstPortDesigPortId_Type()
)
pvxMSTPXstPortDesigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMSTPXstPortDesigPortId.setStatus("current")
_PvxMSTPXstPortPriority_Type = Integer32
_PvxMSTPXstPortPriority_Object = MibTableColumn
pvxMSTPXstPortPriority = _PvxMSTPXstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 13),
    _PvxMSTPXstPortPriority_Type()
)
pvxMSTPXstPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPXstPortPriority.setStatus("current")
_PvxMSTPXstPortPathCost_Type = Integer32
_PvxMSTPXstPortPathCost_Object = MibTableColumn
pvxMSTPXstPortPathCost = _PvxMSTPXstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 14),
    _PvxMSTPXstPortPathCost_Type()
)
pvxMSTPXstPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPXstPortPathCost.setStatus("current")


class _PvxMSTPXstPortForcedPortState_Type(Integer32):
    """Custom type pvxMSTPXstPortForcedPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxMSTPXstPortForcedPortState_Type.__name__ = "Integer32"
_PvxMSTPXstPortForcedPortState_Object = MibTableColumn
pvxMSTPXstPortForcedPortState = _PvxMSTPXstPortForcedPortState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 16, 1, 15),
    _PvxMSTPXstPortForcedPortState_Type()
)
pvxMSTPXstPortForcedPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMSTPXstPortForcedPortState.setStatus("current")
_PvxNextFreeIndexTable_Object = MibTable
pvxNextFreeIndexTable = _PvxNextFreeIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 17)
)
if mibBuilder.loadTexts:
    pvxNextFreeIndexTable.setStatus("current")
_PvxNextFreeIndexEntry_Object = MibTableRow
pvxNextFreeIndexEntry = _PvxNextFreeIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 17, 1)
)
pvxNextFreeIndexEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNextFreeIndexTableIndex"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNextFreeIndexSwitchIdx"),
)
if mibBuilder.loadTexts:
    pvxNextFreeIndexEntry.setStatus("current")


class _PvxNextFreeIndexTableIndex_Type(Integer32):
    """Custom type pvxNextFreeIndexTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              70,
              84,
              87,
              93)
        )
    )
    namedValues = NamedValues(
        *(("flowclass", 87),
          ("lagGroup", 70),
          ("none", 1),
          ("switches", 84),
          ("vlan", 93))
    )


_PvxNextFreeIndexTableIndex_Type.__name__ = "Integer32"
_PvxNextFreeIndexTableIndex_Object = MibTableColumn
pvxNextFreeIndexTableIndex = _PvxNextFreeIndexTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 17, 1, 1),
    _PvxNextFreeIndexTableIndex_Type()
)
pvxNextFreeIndexTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNextFreeIndexTableIndex.setStatus("current")


class _PvxNextFreeIndexSwitchIdx_Type(Integer32):
    """Custom type pvxNextFreeIndexSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxNextFreeIndexSwitchIdx_Type.__name__ = "Integer32"
_PvxNextFreeIndexSwitchIdx_Object = MibTableColumn
pvxNextFreeIndexSwitchIdx = _PvxNextFreeIndexSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 17, 1, 2),
    _PvxNextFreeIndexSwitchIdx_Type()
)
pvxNextFreeIndexSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNextFreeIndexSwitchIdx.setStatus("current")
_PvxNextFreeIndexValue_Type = Integer32
_PvxNextFreeIndexValue_Object = MibTableColumn
pvxNextFreeIndexValue = _PvxNextFreeIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 17, 1, 3),
    _PvxNextFreeIndexValue_Type()
)
pvxNextFreeIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxNextFreeIndexValue.setStatus("current")
_PvxUNITable_Object = MibTable
pvxUNITable = _PvxUNITable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18)
)
if mibBuilder.loadTexts:
    pvxUNITable.setStatus("current")
_PvxUNIEntry_Object = MibTableRow
pvxUNIEntry = _PvxUNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1)
)
pvxUNIEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxUNISwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxUNIShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxUNISlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxUNIPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxUNIPortId"),
)
if mibBuilder.loadTexts:
    pvxUNIEntry.setStatus("current")


class _PvxUNISwitchId_Type(Integer32):
    """Custom type pvxUNISwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxUNISwitchId_Type.__name__ = "Integer32"
_PvxUNISwitchId_Object = MibTableColumn
pvxUNISwitchId = _PvxUNISwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 1),
    _PvxUNISwitchId_Type()
)
pvxUNISwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxUNISwitchId.setStatus("current")


class _PvxUNIShelfId_Type(Integer32):
    """Custom type pvxUNIShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxUNIShelfId_Type.__name__ = "Integer32"
_PvxUNIShelfId_Object = MibTableColumn
pvxUNIShelfId = _PvxUNIShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 2),
    _PvxUNIShelfId_Type()
)
pvxUNIShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxUNIShelfId.setStatus("current")


class _PvxUNISlotId_Type(Integer32):
    """Custom type pvxUNISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxUNISlotId_Type.__name__ = "Integer32"
_PvxUNISlotId_Object = MibTableColumn
pvxUNISlotId = _PvxUNISlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 3),
    _PvxUNISlotId_Type()
)
pvxUNISlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxUNISlotId.setStatus("current")
_PvxUNIPortTypeId_Type = PvxPortType
_PvxUNIPortTypeId_Object = MibTableColumn
pvxUNIPortTypeId = _PvxUNIPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 4),
    _PvxUNIPortTypeId_Type()
)
pvxUNIPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxUNIPortTypeId.setStatus("current")
_PvxUNIPortId_Type = Integer32
_PvxUNIPortId_Object = MibTableColumn
pvxUNIPortId = _PvxUNIPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 5),
    _PvxUNIPortId_Type()
)
pvxUNIPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxUNIPortId.setStatus("current")
_PvxUNISpeed_Type = Integer32
_PvxUNISpeed_Object = MibTableColumn
pvxUNISpeed = _PvxUNISpeed_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 6),
    _PvxUNISpeed_Type()
)
pvxUNISpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxUNISpeed.setStatus("current")


class _PvxUNIMode_Type(Integer32):
    """Custom type pvxUNIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_PvxUNIMode_Type.__name__ = "Integer32"
_PvxUNIMode_Object = MibTableColumn
pvxUNIMode = _PvxUNIMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 7),
    _PvxUNIMode_Type()
)
pvxUNIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxUNIMode.setStatus("current")


class _PvxUNIMaxFrameSize_Type(Integer32):
    """Custom type pvxUNIMaxFrameSize based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 9600),
    )


_PvxUNIMaxFrameSize_Type.__name__ = "Integer32"
_PvxUNIMaxFrameSize_Object = MibTableColumn
pvxUNIMaxFrameSize = _PvxUNIMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 8),
    _PvxUNIMaxFrameSize_Type()
)
pvxUNIMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxUNIMaxFrameSize.setStatus("current")


class _PvxUNICurrentFrameSize_Type(Integer32):
    """Custom type pvxUNICurrentFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 9600),
    )


_PvxUNICurrentFrameSize_Type.__name__ = "Integer32"
_PvxUNICurrentFrameSize_Object = MibTableColumn
pvxUNICurrentFrameSize = _PvxUNICurrentFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 9),
    _PvxUNICurrentFrameSize_Type()
)
pvxUNICurrentFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxUNICurrentFrameSize.setStatus("current")


class _PvxUNIServiceType_Type(Integer32):
    """Custom type pvxUNIServiceType based on Integer32"""
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
        *(("private", 2),
          ("unspecified", 1),
          ("virtualMultiple", 4),
          ("virtualSingle", 3),
          ("virtualUntagged", 5))
    )


_PvxUNIServiceType_Type.__name__ = "Integer32"
_PvxUNIServiceType_Object = MibTableColumn
pvxUNIServiceType = _PvxUNIServiceType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 10),
    _PvxUNIServiceType_Type()
)
pvxUNIServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxUNIServiceType.setStatus("current")
_PvxUNINumServices_Type = Integer32
_PvxUNINumServices_Object = MibTableColumn
pvxUNINumServices = _PvxUNINumServices_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 11),
    _PvxUNINumServices_Type()
)
pvxUNINumServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxUNINumServices.setStatus("current")


class _PvxUNICPVid_Type(Integer32):
    """Custom type pvxUNICPVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PvxUNICPVid_Type.__name__ = "Integer32"
_PvxUNICPVid_Object = MibTableColumn
pvxUNICPVid = _PvxUNICPVid_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 12),
    _PvxUNICPVid_Type()
)
pvxUNICPVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxUNICPVid.setStatus("current")
_PvxUNIRowStatus_Type = RowStatus
_PvxUNIRowStatus_Object = MibTableColumn
pvxUNIRowStatus = _PvxUNIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 18, 1, 100),
    _PvxUNIRowStatus_Type()
)
pvxUNIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxUNIRowStatus.setStatus("current")
_PvxNNITable_Object = MibTable
pvxNNITable = _PvxNNITable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19)
)
if mibBuilder.loadTexts:
    pvxNNITable.setStatus("current")
_PvxNNIEntry_Object = MibTableRow
pvxNNIEntry = _PvxNNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1)
)
pvxNNIEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNNISwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNNIShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNNISlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNNIPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxNNIPortId"),
)
if mibBuilder.loadTexts:
    pvxNNIEntry.setStatus("current")


class _PvxNNISwitchId_Type(Integer32):
    """Custom type pvxNNISwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxNNISwitchId_Type.__name__ = "Integer32"
_PvxNNISwitchId_Object = MibTableColumn
pvxNNISwitchId = _PvxNNISwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 1),
    _PvxNNISwitchId_Type()
)
pvxNNISwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNNISwitchId.setStatus("current")


class _PvxNNIShelfId_Type(Integer32):
    """Custom type pvxNNIShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxNNIShelfId_Type.__name__ = "Integer32"
_PvxNNIShelfId_Object = MibTableColumn
pvxNNIShelfId = _PvxNNIShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 2),
    _PvxNNIShelfId_Type()
)
pvxNNIShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNNIShelfId.setStatus("current")


class _PvxNNISlotId_Type(Integer32):
    """Custom type pvxNNISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxNNISlotId_Type.__name__ = "Integer32"
_PvxNNISlotId_Object = MibTableColumn
pvxNNISlotId = _PvxNNISlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 3),
    _PvxNNISlotId_Type()
)
pvxNNISlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNNISlotId.setStatus("current")
_PvxNNIPortTypeId_Type = PvxPortType
_PvxNNIPortTypeId_Object = MibTableColumn
pvxNNIPortTypeId = _PvxNNIPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 4),
    _PvxNNIPortTypeId_Type()
)
pvxNNIPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNNIPortTypeId.setStatus("current")
_PvxNNIPortId_Type = Integer32
_PvxNNIPortId_Object = MibTableColumn
pvxNNIPortId = _PvxNNIPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 5),
    _PvxNNIPortId_Type()
)
pvxNNIPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxNNIPortId.setStatus("current")
_PvxNNISpeed_Type = Integer32
_PvxNNISpeed_Object = MibTableColumn
pvxNNISpeed = _PvxNNISpeed_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 6),
    _PvxNNISpeed_Type()
)
pvxNNISpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxNNISpeed.setStatus("current")


class _PvxNNIMode_Type(Integer32):
    """Custom type pvxNNIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_PvxNNIMode_Type.__name__ = "Integer32"
_PvxNNIMode_Object = MibTableColumn
pvxNNIMode = _PvxNNIMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 7),
    _PvxNNIMode_Type()
)
pvxNNIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxNNIMode.setStatus("current")


class _PvxNNIMaxFrameSize_Type(Integer32):
    """Custom type pvxNNIMaxFrameSize based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1526, 9600),
    )


_PvxNNIMaxFrameSize_Type.__name__ = "Integer32"
_PvxNNIMaxFrameSize_Object = MibTableColumn
pvxNNIMaxFrameSize = _PvxNNIMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 8),
    _PvxNNIMaxFrameSize_Type()
)
pvxNNIMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxNNIMaxFrameSize.setStatus("current")
_PvxNNIRowStatus_Type = RowStatus
_PvxNNIRowStatus_Object = MibTableColumn
pvxNNIRowStatus = _PvxNNIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 19, 1, 100),
    _PvxNNIRowStatus_Type()
)
pvxNNIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxNNIRowStatus.setStatus("current")
_PvxVlanPortTable_Object = MibTable
pvxVlanPortTable = _PvxVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20)
)
if mibBuilder.loadTexts:
    pvxVlanPortTable.setStatus("current")
_PvxVlanPortEntry_Object = MibTableRow
pvxVlanPortEntry = _PvxVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1)
)
pvxVlanPortEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanPortSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanPortShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanPortSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanPortIdx"),
)
if mibBuilder.loadTexts:
    pvxVlanPortEntry.setStatus("current")


class _PvxVlanPortSwitchIdx_Type(Integer32):
    """Custom type pvxVlanPortSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxVlanPortSwitchIdx_Type.__name__ = "Integer32"
_PvxVlanPortSwitchIdx_Object = MibTableColumn
pvxVlanPortSwitchIdx = _PvxVlanPortSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 1),
    _PvxVlanPortSwitchIdx_Type()
)
pvxVlanPortSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanPortSwitchIdx.setStatus("current")


class _PvxVlanPortShelfIdx_Type(Integer32):
    """Custom type pvxVlanPortShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxVlanPortShelfIdx_Type.__name__ = "Integer32"
_PvxVlanPortShelfIdx_Object = MibTableColumn
pvxVlanPortShelfIdx = _PvxVlanPortShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 2),
    _PvxVlanPortShelfIdx_Type()
)
pvxVlanPortShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanPortShelfIdx.setStatus("current")


class _PvxVlanPortSlotIdx_Type(Integer32):
    """Custom type pvxVlanPortSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxVlanPortSlotIdx_Type.__name__ = "Integer32"
_PvxVlanPortSlotIdx_Object = MibTableColumn
pvxVlanPortSlotIdx = _PvxVlanPortSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 3),
    _PvxVlanPortSlotIdx_Type()
)
pvxVlanPortSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanPortSlotIdx.setStatus("current")
_PvxVlanPortTypeIdx_Type = PvxPortType
_PvxVlanPortTypeIdx_Object = MibTableColumn
pvxVlanPortTypeIdx = _PvxVlanPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 4),
    _PvxVlanPortTypeIdx_Type()
)
pvxVlanPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanPortTypeIdx.setStatus("current")


class _PvxVlanPortIdx_Type(Integer32):
    """Custom type pvxVlanPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxVlanPortIdx_Type.__name__ = "Integer32"
_PvxVlanPortIdx_Object = MibTableColumn
pvxVlanPortIdx = _PvxVlanPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 5),
    _PvxVlanPortIdx_Type()
)
pvxVlanPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanPortIdx.setStatus("current")


class _PvxVlanPortGvrpAdminState_Type(Integer32):
    """Custom type pvxVlanPortGvrpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxVlanPortGvrpAdminState_Type.__name__ = "Integer32"
_PvxVlanPortGvrpAdminState_Object = MibTableColumn
pvxVlanPortGvrpAdminState = _PvxVlanPortGvrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 6),
    _PvxVlanPortGvrpAdminState_Type()
)
pvxVlanPortGvrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVlanPortGvrpAdminState.setStatus("current")


class _PvxVlanPortRestrictedVlanState_Type(Integer32):
    """Custom type pvxVlanPortRestrictedVlanState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxVlanPortRestrictedVlanState_Type.__name__ = "Integer32"
_PvxVlanPortRestrictedVlanState_Object = MibTableColumn
pvxVlanPortRestrictedVlanState = _PvxVlanPortRestrictedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 7),
    _PvxVlanPortRestrictedVlanState_Type()
)
pvxVlanPortRestrictedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxVlanPortRestrictedVlanState.setStatus("current")


class _PvxVlanPortEthPortAllowedFrametType_Type(Integer32):
    """Custom type pvxVlanPortEthPortAllowedFrametType based on Integer32"""
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
        *(("admitAll", 1),
          ("admitDefault", 4),
          ("admitOnlyUntaggedAndPriorityTagged", 3),
          ("admitOnlyVlanTagged", 2))
    )


_PvxVlanPortEthPortAllowedFrametType_Type.__name__ = "Integer32"
_PvxVlanPortEthPortAllowedFrametType_Object = MibTableColumn
pvxVlanPortEthPortAllowedFrametType = _PvxVlanPortEthPortAllowedFrametType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 8),
    _PvxVlanPortEthPortAllowedFrametType_Type()
)
pvxVlanPortEthPortAllowedFrametType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanPortEthPortAllowedFrametType.setStatus("current")


class _PvxVlanPortIngressFiltering_Type(Integer32):
    """Custom type pvxVlanPortIngressFiltering based on Integer32"""
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


_PvxVlanPortIngressFiltering_Type.__name__ = "Integer32"
_PvxVlanPortIngressFiltering_Object = MibTableColumn
pvxVlanPortIngressFiltering = _PvxVlanPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 9),
    _PvxVlanPortIngressFiltering_Type()
)
pvxVlanPortIngressFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanPortIngressFiltering.setStatus("deprecated")
_PvxVlanPortGvrpFailedRegistrations_Type = Integer32
_PvxVlanPortGvrpFailedRegistrations_Object = MibTableColumn
pvxVlanPortGvrpFailedRegistrations = _PvxVlanPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 10),
    _PvxVlanPortGvrpFailedRegistrations_Type()
)
pvxVlanPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanPortGvrpFailedRegistrations.setStatus("current")
_PvxVlanPortLastBpduOrigin_Type = MacAddress
_PvxVlanPortLastBpduOrigin_Object = MibTableColumn
pvxVlanPortLastBpduOrigin = _PvxVlanPortLastBpduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 20, 1, 11),
    _PvxVlanPortLastBpduOrigin_Type()
)
pvxVlanPortLastBpduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanPortLastBpduOrigin.setStatus("current")
_PvxVlanCurrentTable_Object = MibTable
pvxVlanCurrentTable = _PvxVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21)
)
if mibBuilder.loadTexts:
    pvxVlanCurrentTable.setStatus("current")
_PvxVlanCurrentEntry_Object = MibTableRow
pvxVlanCurrentEntry = _PvxVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1)
)
pvxVlanCurrentEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanCurrentSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanCurrentTimeMark"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxVlanCurrentVlanIdx"),
)
if mibBuilder.loadTexts:
    pvxVlanCurrentEntry.setStatus("current")


class _PvxVlanCurrentSwitchIdx_Type(Integer32):
    """Custom type pvxVlanCurrentSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxVlanCurrentSwitchIdx_Type.__name__ = "Integer32"
_PvxVlanCurrentSwitchIdx_Object = MibTableColumn
pvxVlanCurrentSwitchIdx = _PvxVlanCurrentSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1, 1),
    _PvxVlanCurrentSwitchIdx_Type()
)
pvxVlanCurrentSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanCurrentSwitchIdx.setStatus("current")
_PvxVlanCurrentTimeMark_Type = Unsigned32
_PvxVlanCurrentTimeMark_Object = MibTableColumn
pvxVlanCurrentTimeMark = _PvxVlanCurrentTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1, 2),
    _PvxVlanCurrentTimeMark_Type()
)
pvxVlanCurrentTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanCurrentTimeMark.setStatus("current")


class _PvxVlanCurrentVlanIdx_Type(Integer32):
    """Custom type pvxVlanCurrentVlanIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxVlanCurrentVlanIdx_Type.__name__ = "Integer32"
_PvxVlanCurrentVlanIdx_Object = MibTableColumn
pvxVlanCurrentVlanIdx = _PvxVlanCurrentVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1, 3),
    _PvxVlanCurrentVlanIdx_Type()
)
pvxVlanCurrentVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxVlanCurrentVlanIdx.setStatus("current")


class _PvxVlanCurrentStatus_Type(Integer32):
    """Custom type pvxVlanCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGVRP", 3),
          ("other", 1),
          ("permanent", 2))
    )


_PvxVlanCurrentStatus_Type.__name__ = "Integer32"
_PvxVlanCurrentStatus_Object = MibTableColumn
pvxVlanCurrentStatus = _PvxVlanCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1, 4),
    _PvxVlanCurrentStatus_Type()
)
pvxVlanCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanCurrentStatus.setStatus("current")
_PvxVlanCurrentCreationTime_Type = Integer32
_PvxVlanCurrentCreationTime_Object = MibTableColumn
pvxVlanCurrentCreationTime = _PvxVlanCurrentCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 21, 1, 5),
    _PvxVlanCurrentCreationTime_Type()
)
pvxVlanCurrentCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxVlanCurrentCreationTime.setStatus("current")
_PvxDynamicVlanPortTable_Object = MibTable
pvxDynamicVlanPortTable = _PvxDynamicVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 24)
)
if mibBuilder.loadTexts:
    pvxDynamicVlanPortTable.setStatus("current")
_PvxDynamicVlanPortEntry_Object = MibTableRow
pvxDynamicVlanPortEntry = _PvxDynamicVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 24, 1)
)
pvxDynamicVlanPortEntry.setIndexNames(
    (0, "BTI-7000-MIB", "pvxL2IntfSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxDynamicVlanPortTimeMark"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxDynamicVlanPortVlanIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfShelfIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfSlotIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortTypeIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfSubPortNumber"),
)
if mibBuilder.loadTexts:
    pvxDynamicVlanPortEntry.setStatus("current")
_PvxDynamicVlanPortTimeMark_Type = Unsigned32
_PvxDynamicVlanPortTimeMark_Object = MibTableColumn
pvxDynamicVlanPortTimeMark = _PvxDynamicVlanPortTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 24, 1, 1),
    _PvxDynamicVlanPortTimeMark_Type()
)
pvxDynamicVlanPortTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxDynamicVlanPortTimeMark.setStatus("current")


class _PvxDynamicVlanPortVlanIdx_Type(Integer32):
    """Custom type pvxDynamicVlanPortVlanIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxDynamicVlanPortVlanIdx_Type.__name__ = "Integer32"
_PvxDynamicVlanPortVlanIdx_Object = MibTableColumn
pvxDynamicVlanPortVlanIdx = _PvxDynamicVlanPortVlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 24, 1, 2),
    _PvxDynamicVlanPortVlanIdx_Type()
)
pvxDynamicVlanPortVlanIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxDynamicVlanPortVlanIdx.setStatus("current")


class _PvxDynamicVlanPortTagged_Type(Integer32):
    """Custom type pvxDynamicVlanPortTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_PvxDynamicVlanPortTagged_Type.__name__ = "Integer32"
_PvxDynamicVlanPortTagged_Object = MibTableColumn
pvxDynamicVlanPortTagged = _PvxDynamicVlanPortTagged_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 24, 1, 3),
    _PvxDynamicVlanPortTagged_Type()
)
pvxDynamicVlanPortTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxDynamicVlanPortTagged.setStatus("current")
_PvxStackingPortTable_Object = MibTable
pvxStackingPortTable = _PvxStackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 25)
)
if mibBuilder.loadTexts:
    pvxStackingPortTable.setStatus("current")
_PvxStackingPortEntry_Object = MibTableRow
pvxStackingPortEntry = _PvxStackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 25, 1)
)
pvxStackingPortEntry.setIndexNames(
    (0, "BTI-7000-MIB", "pvxL2IntfSwitchIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfShelfIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfSlotIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortTypeIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortIdx"),
)
if mibBuilder.loadTexts:
    pvxStackingPortEntry.setStatus("current")


class _PvxStackingPortOperStatus_Type(Integer32):
    """Custom type pvxStackingPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notPresent", 3),
          ("up", 1))
    )


_PvxStackingPortOperStatus_Type.__name__ = "Integer32"
_PvxStackingPortOperStatus_Object = MibTableColumn
pvxStackingPortOperStatus = _PvxStackingPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 25, 1, 1),
    _PvxStackingPortOperStatus_Type()
)
pvxStackingPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxStackingPortOperStatus.setStatus("current")
_PvxStackingPortRowStatus_Type = RowStatus
_PvxStackingPortRowStatus_Object = MibTableColumn
pvxStackingPortRowStatus = _PvxStackingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 25, 1, 100),
    _PvxStackingPortRowStatus_Type()
)
pvxStackingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxStackingPortRowStatus.setStatus("current")
_PvxSwitchCpuRLMonTable_Object = MibTable
pvxSwitchCpuRLMonTable = _PvxSwitchCpuRLMonTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26)
)
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonTable.setStatus("current")
_PvxSwitchCpuRLMonEntry_Object = MibTableRow
pvxSwitchCpuRLMonEntry = _PvxSwitchCpuRLMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1)
)
pvxSwitchCpuRLMonEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchCpuRLMonSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchCpuRLMonShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchCpuRLMonSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSwitchCpuRLMonCosIdx"),
)
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonEntry.setStatus("current")


class _PvxSwitchCpuRLMonSwitchIdx_Type(Integer32):
    """Custom type pvxSwitchCpuRLMonSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSwitchCpuRLMonSwitchIdx_Type.__name__ = "Integer32"
_PvxSwitchCpuRLMonSwitchIdx_Object = MibTableColumn
pvxSwitchCpuRLMonSwitchIdx = _PvxSwitchCpuRLMonSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 1),
    _PvxSwitchCpuRLMonSwitchIdx_Type()
)
pvxSwitchCpuRLMonSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonSwitchIdx.setStatus("current")


class _PvxSwitchCpuRLMonShelfIdx_Type(Integer32):
    """Custom type pvxSwitchCpuRLMonShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSwitchCpuRLMonShelfIdx_Type.__name__ = "Integer32"
_PvxSwitchCpuRLMonShelfIdx_Object = MibTableColumn
pvxSwitchCpuRLMonShelfIdx = _PvxSwitchCpuRLMonShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 2),
    _PvxSwitchCpuRLMonShelfIdx_Type()
)
pvxSwitchCpuRLMonShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonShelfIdx.setStatus("current")


class _PvxSwitchCpuRLMonSlotIdx_Type(Integer32):
    """Custom type pvxSwitchCpuRLMonSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSwitchCpuRLMonSlotIdx_Type.__name__ = "Integer32"
_PvxSwitchCpuRLMonSlotIdx_Object = MibTableColumn
pvxSwitchCpuRLMonSlotIdx = _PvxSwitchCpuRLMonSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 3),
    _PvxSwitchCpuRLMonSlotIdx_Type()
)
pvxSwitchCpuRLMonSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonSlotIdx.setStatus("current")


class _PvxSwitchCpuRLMonCosIdx_Type(Integer32):
    """Custom type pvxSwitchCpuRLMonCosIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PvxSwitchCpuRLMonCosIdx_Type.__name__ = "Integer32"
_PvxSwitchCpuRLMonCosIdx_Object = MibTableColumn
pvxSwitchCpuRLMonCosIdx = _PvxSwitchCpuRLMonCosIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 4),
    _PvxSwitchCpuRLMonCosIdx_Type()
)
pvxSwitchCpuRLMonCosIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosIdx.setStatus("current")
_PvxSwitchCpuRLMonCosCurrDepth_Type = Integer32
_PvxSwitchCpuRLMonCosCurrDepth_Object = MibTableColumn
pvxSwitchCpuRLMonCosCurrDepth = _PvxSwitchCpuRLMonCosCurrDepth_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 5),
    _PvxSwitchCpuRLMonCosCurrDepth_Type()
)
pvxSwitchCpuRLMonCosCurrDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosCurrDepth.setStatus("current")
_PvxSwitchCpuRLMonCosReceived_Type = Integer32
_PvxSwitchCpuRLMonCosReceived_Object = MibTableColumn
pvxSwitchCpuRLMonCosReceived = _PvxSwitchCpuRLMonCosReceived_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 6),
    _PvxSwitchCpuRLMonCosReceived_Type()
)
pvxSwitchCpuRLMonCosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosReceived.setStatus("current")
_PvxSwitchCpuRLMonCosDiscards_Type = Integer32
_PvxSwitchCpuRLMonCosDiscards_Object = MibTableColumn
pvxSwitchCpuRLMonCosDiscards = _PvxSwitchCpuRLMonCosDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 7),
    _PvxSwitchCpuRLMonCosDiscards_Type()
)
pvxSwitchCpuRLMonCosDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosDiscards.setStatus("current")
_PvxSwitchCpuRLMonCosMinDepth60Sec_Type = Integer32
_PvxSwitchCpuRLMonCosMinDepth60Sec_Object = MibTableColumn
pvxSwitchCpuRLMonCosMinDepth60Sec = _PvxSwitchCpuRLMonCosMinDepth60Sec_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 8),
    _PvxSwitchCpuRLMonCosMinDepth60Sec_Type()
)
pvxSwitchCpuRLMonCosMinDepth60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosMinDepth60Sec.setStatus("current")
_PvxSwitchCpuRLMonCosMaxDepth60Sec_Type = Integer32
_PvxSwitchCpuRLMonCosMaxDepth60Sec_Object = MibTableColumn
pvxSwitchCpuRLMonCosMaxDepth60Sec = _PvxSwitchCpuRLMonCosMaxDepth60Sec_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 9),
    _PvxSwitchCpuRLMonCosMaxDepth60Sec_Type()
)
pvxSwitchCpuRLMonCosMaxDepth60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosMaxDepth60Sec.setStatus("current")
_PvxSwitchCpuRLMonCosReceived60Sec_Type = Integer32
_PvxSwitchCpuRLMonCosReceived60Sec_Object = MibTableColumn
pvxSwitchCpuRLMonCosReceived60Sec = _PvxSwitchCpuRLMonCosReceived60Sec_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 10),
    _PvxSwitchCpuRLMonCosReceived60Sec_Type()
)
pvxSwitchCpuRLMonCosReceived60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosReceived60Sec.setStatus("current")
_PvxSwitchCpuRLMonCosDiscards60Sec_Type = Integer32
_PvxSwitchCpuRLMonCosDiscards60Sec_Object = MibTableColumn
pvxSwitchCpuRLMonCosDiscards60Sec = _PvxSwitchCpuRLMonCosDiscards60Sec_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 11),
    _PvxSwitchCpuRLMonCosDiscards60Sec_Type()
)
pvxSwitchCpuRLMonCosDiscards60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosDiscards60Sec.setStatus("current")
_PvxSwitchCpuRLMonCosDiscardsTotal_Type = Integer32
_PvxSwitchCpuRLMonCosDiscardsTotal_Object = MibTableColumn
pvxSwitchCpuRLMonCosDiscardsTotal = _PvxSwitchCpuRLMonCosDiscardsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 12),
    _PvxSwitchCpuRLMonCosDiscardsTotal_Type()
)
pvxSwitchCpuRLMonCosDiscardsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosDiscardsTotal.setStatus("current")
_PvxSwitchCpuRLMonCosReceivedRateLimit_Type = Integer32
_PvxSwitchCpuRLMonCosReceivedRateLimit_Object = MibTableColumn
pvxSwitchCpuRLMonCosReceivedRateLimit = _PvxSwitchCpuRLMonCosReceivedRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 13),
    _PvxSwitchCpuRLMonCosReceivedRateLimit_Type()
)
pvxSwitchCpuRLMonCosReceivedRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosReceivedRateLimit.setStatus("current")
_PvxSwitchCpuRLMonCosMaxAllowedDepth_Type = Integer32
_PvxSwitchCpuRLMonCosMaxAllowedDepth_Object = MibTableColumn
pvxSwitchCpuRLMonCosMaxAllowedDepth = _PvxSwitchCpuRLMonCosMaxAllowedDepth_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 14),
    _PvxSwitchCpuRLMonCosMaxAllowedDepth_Type()
)
pvxSwitchCpuRLMonCosMaxAllowedDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosMaxAllowedDepth.setStatus("current")
_PvxSwitchCpuRLMonCosHighWatermark_Type = Integer32
_PvxSwitchCpuRLMonCosHighWatermark_Object = MibTableColumn
pvxSwitchCpuRLMonCosHighWatermark = _PvxSwitchCpuRLMonCosHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 15),
    _PvxSwitchCpuRLMonCosHighWatermark_Type()
)
pvxSwitchCpuRLMonCosHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosHighWatermark.setStatus("current")
_PvxSwitchCpuRLMonCosHighWatermark60Sec_Type = Integer32
_PvxSwitchCpuRLMonCosHighWatermark60Sec_Object = MibTableColumn
pvxSwitchCpuRLMonCosHighWatermark60Sec = _PvxSwitchCpuRLMonCosHighWatermark60Sec_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 16),
    _PvxSwitchCpuRLMonCosHighWatermark60Sec_Type()
)
pvxSwitchCpuRLMonCosHighWatermark60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosHighWatermark60Sec.setStatus("current")
_PvxSwitchCpuRLMonCosHighestWatermark_Type = Integer32
_PvxSwitchCpuRLMonCosHighestWatermark_Object = MibTableColumn
pvxSwitchCpuRLMonCosHighestWatermark = _PvxSwitchCpuRLMonCosHighestWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 1, 26, 1, 17),
    _PvxSwitchCpuRLMonCosHighestWatermark_Type()
)
pvxSwitchCpuRLMonCosHighestWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSwitchCpuRLMonCosHighestWatermark.setStatus("current")
_PvxBridgeServices_ObjectIdentity = ObjectIdentity
pvxBridgeServices = _PvxBridgeServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2)
)
_PvxFlowTable_Object = MibTable
pvxFlowTable = _PvxFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12)
)
if mibBuilder.loadTexts:
    pvxFlowTable.setStatus("current")
_PvxFlowEntry_Object = MibTableRow
pvxFlowEntry = _PvxFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1)
)
pvxFlowEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowEntry.setStatus("current")


class _PvxFSwitchIdx_Type(Integer32):
    """Custom type pvxFSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFSwitchIdx_Type.__name__ = "Integer32"
_PvxFSwitchIdx_Object = MibTableColumn
pvxFSwitchIdx = _PvxFSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 1),
    _PvxFSwitchIdx_Type()
)
pvxFSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFSwitchIdx.setStatus("current")
_PvxFIdx_Type = Integer32
_PvxFIdx_Object = MibTableColumn
pvxFIdx = _PvxFIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 2),
    _PvxFIdx_Type()
)
pvxFIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFIdx.setStatus("current")
_PvxFClassificationIdList_Type = DisplayString
_PvxFClassificationIdList_Object = MibTableColumn
pvxFClassificationIdList = _PvxFClassificationIdList_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 3),
    _PvxFClassificationIdList_Type()
)
pvxFClassificationIdList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFClassificationIdList.setStatus("current")
_PvxFMeterId_Type = Integer32
_PvxFMeterId_Object = MibTableColumn
pvxFMeterId = _PvxFMeterId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 4),
    _PvxFMeterId_Type()
)
pvxFMeterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMeterId.setStatus("current")
_PvxFCoSName_Type = DisplayString
_PvxFCoSName_Object = MibTableColumn
pvxFCoSName = _PvxFCoSName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 5),
    _PvxFCoSName_Type()
)
pvxFCoSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFCoSName.setStatus("current")
_PvxFRowStatus_Type = RowStatus
_PvxFRowStatus_Object = MibTableColumn
pvxFRowStatus = _PvxFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 12, 1, 100),
    _PvxFRowStatus_Type()
)
pvxFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFRowStatus.setStatus("current")
_PvxFlowClassificationTable_Object = MibTable
pvxFlowClassificationTable = _PvxFlowClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13)
)
if mibBuilder.loadTexts:
    pvxFlowClassificationTable.setStatus("current")
_PvxFlowClassificationEntry_Object = MibTableRow
pvxFlowClassificationEntry = _PvxFlowClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1)
)
pvxFlowClassificationEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFloClSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFloClIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowClassificationEntry.setStatus("current")


class _PvxFloClSwitchIdx_Type(Integer32):
    """Custom type pvxFloClSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFloClSwitchIdx_Type.__name__ = "Integer32"
_PvxFloClSwitchIdx_Object = MibTableColumn
pvxFloClSwitchIdx = _PvxFloClSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 1),
    _PvxFloClSwitchIdx_Type()
)
pvxFloClSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFloClSwitchIdx.setStatus("current")


class _PvxFloClIdx_Type(Integer32):
    """Custom type pvxFloClIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PvxFloClIdx_Type.__name__ = "Integer32"
_PvxFloClIdx_Object = MibTableColumn
pvxFloClIdx = _PvxFloClIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 2),
    _PvxFloClIdx_Type()
)
pvxFloClIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFloClIdx.setStatus("current")


class _PvxFloClActionId_Type(Integer32):
    """Custom type pvxFloClActionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PvxFloClActionId_Type.__name__ = "Integer32"
_PvxFloClActionId_Object = MibTableColumn
pvxFloClActionId = _PvxFloClActionId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 3),
    _PvxFloClActionId_Type()
)
pvxFloClActionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClActionId.setStatus("current")


class _PvxFloClMeterId_Type(Integer32):
    """Custom type pvxFloClMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PvxFloClMeterId_Type.__name__ = "Integer32"
_PvxFloClMeterId_Object = MibTableColumn
pvxFloClMeterId = _PvxFloClMeterId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 4),
    _PvxFloClMeterId_Type()
)
pvxFloClMeterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClMeterId.setStatus("current")


class _PvxFloClStatus_Type(Integer32):
    """Custom type pvxFloClStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxFloClStatus_Type.__name__ = "Integer32"
_PvxFloClStatus_Object = MibTableColumn
pvxFloClStatus = _PvxFloClStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 5),
    _PvxFloClStatus_Type()
)
pvxFloClStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClStatus.setStatus("current")


class _PvxFloClEntryType_Type(Integer32):
    """Custom type pvxFloClEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAcl", 2),
          ("macAcl", 3),
          ("untyped", 1))
    )


_PvxFloClEntryType_Type.__name__ = "Integer32"
_PvxFloClEntryType_Object = MibTableColumn
pvxFloClEntryType = _PvxFloClEntryType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 6),
    _PvxFloClEntryType_Type()
)
pvxFloClEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClEntryType.setStatus("current")
_PvxFloClL2InterfaceRange_Type = DisplayString
_PvxFloClL2InterfaceRange_Object = MibTableColumn
pvxFloClL2InterfaceRange = _PvxFloClL2InterfaceRange_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 7),
    _PvxFloClL2InterfaceRange_Type()
)
pvxFloClL2InterfaceRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClL2InterfaceRange.setStatus("current")
_PvxFloClCVlanFilter_Type = DisplayString
_PvxFloClCVlanFilter_Object = MibTableColumn
pvxFloClCVlanFilter = _PvxFloClCVlanFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 8),
    _PvxFloClCVlanFilter_Type()
)
pvxFloClCVlanFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClCVlanFilter.setStatus("current")
_PvxFloClSVlanFilter_Type = DisplayString
_PvxFloClSVlanFilter_Object = MibTableColumn
pvxFloClSVlanFilter = _PvxFloClSVlanFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 9),
    _PvxFloClSVlanFilter_Type()
)
pvxFloClSVlanFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClSVlanFilter.setStatus("current")
_PvxFloClSourceIPFilter_Type = DisplayString
_PvxFloClSourceIPFilter_Object = MibTableColumn
pvxFloClSourceIPFilter = _PvxFloClSourceIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 10),
    _PvxFloClSourceIPFilter_Type()
)
pvxFloClSourceIPFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClSourceIPFilter.setStatus("current")
_PvxFloClDestIPFilter_Type = DisplayString
_PvxFloClDestIPFilter_Object = MibTableColumn
pvxFloClDestIPFilter = _PvxFloClDestIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 11),
    _PvxFloClDestIPFilter_Type()
)
pvxFloClDestIPFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClDestIPFilter.setStatus("current")
_PvxFloClIPProtocolFilter_Type = DisplayString
_PvxFloClIPProtocolFilter_Object = MibTableColumn
pvxFloClIPProtocolFilter = _PvxFloClIPProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 12),
    _PvxFloClIPProtocolFilter_Type()
)
pvxFloClIPProtocolFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClIPProtocolFilter.setStatus("current")
_PvxFloClEtherTypeFilter_Type = DisplayString
_PvxFloClEtherTypeFilter_Object = MibTableColumn
pvxFloClEtherTypeFilter = _PvxFloClEtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 13),
    _PvxFloClEtherTypeFilter_Type()
)
pvxFloClEtherTypeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClEtherTypeFilter.setStatus("current")
_PvxFloClSourceMacFilter_Type = DisplayString
_PvxFloClSourceMacFilter_Object = MibTableColumn
pvxFloClSourceMacFilter = _PvxFloClSourceMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 14),
    _PvxFloClSourceMacFilter_Type()
)
pvxFloClSourceMacFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClSourceMacFilter.setStatus("current")
_PvxFloClDestMacFilter_Type = DisplayString
_PvxFloClDestMacFilter_Object = MibTableColumn
pvxFloClDestMacFilter = _PvxFloClDestMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 15),
    _PvxFloClDestMacFilter_Type()
)
pvxFloClDestMacFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClDestMacFilter.setStatus("current")
_PvxFloClSourceUDPorTCPFilter_Type = DisplayString
_PvxFloClSourceUDPorTCPFilter_Object = MibTableColumn
pvxFloClSourceUDPorTCPFilter = _PvxFloClSourceUDPorTCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 16),
    _PvxFloClSourceUDPorTCPFilter_Type()
)
pvxFloClSourceUDPorTCPFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClSourceUDPorTCPFilter.setStatus("current")
_PvxFloClDestUDPorTCPFilter_Type = DisplayString
_PvxFloClDestUDPorTCPFilter_Object = MibTableColumn
pvxFloClDestUDPorTCPFilter = _PvxFloClDestUDPorTCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 17),
    _PvxFloClDestUDPorTCPFilter_Type()
)
pvxFloClDestUDPorTCPFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClDestUDPorTCPFilter.setStatus("current")
_PvxFloClRowStatus_Type = RowStatus
_PvxFloClRowStatus_Object = MibTableColumn
pvxFloClRowStatus = _PvxFloClRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 13, 1, 100),
    _PvxFloClRowStatus_Type()
)
pvxFloClRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloClRowStatus.setStatus("current")
_PvxFlowActionsTable_Object = MibTable
pvxFlowActionsTable = _PvxFlowActionsTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14)
)
if mibBuilder.loadTexts:
    pvxFlowActionsTable.setStatus("current")
_PvxFlowActionsEntry_Object = MibTableRow
pvxFlowActionsEntry = _PvxFlowActionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1)
)
pvxFlowActionsEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFloActSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFloActIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowActionsEntry.setStatus("current")


class _PvxFloActSwitchIdx_Type(Integer32):
    """Custom type pvxFloActSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFloActSwitchIdx_Type.__name__ = "Integer32"
_PvxFloActSwitchIdx_Object = MibTableColumn
pvxFloActSwitchIdx = _PvxFloActSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 1),
    _PvxFloActSwitchIdx_Type()
)
pvxFloActSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFloActSwitchIdx.setStatus("current")


class _PvxFloActIdx_Type(Integer32):
    """Custom type pvxFloActIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PvxFloActIdx_Type.__name__ = "Integer32"
_PvxFloActIdx_Object = MibTableColumn
pvxFloActIdx = _PvxFloActIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 2),
    _PvxFloActIdx_Type()
)
pvxFloActIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFloActIdx.setStatus("current")
_PvxFloActChangePriority_Type = TruthValue
_PvxFloActChangePriority_Object = MibTableColumn
pvxFloActChangePriority = _PvxFloActChangePriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 3),
    _PvxFloActChangePriority_Type()
)
pvxFloActChangePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActChangePriority.setStatus("current")


class _PvxFloActNewPriority_Type(Integer32):
    """Custom type pvxFloActNewPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxFloActNewPriority_Type.__name__ = "Integer32"
_PvxFloActNewPriority_Object = MibTableColumn
pvxFloActNewPriority = _PvxFloActNewPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 4),
    _PvxFloActNewPriority_Type()
)
pvxFloActNewPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActNewPriority.setStatus("current")


class _PvxFloActPacketAction_Type(Integer32):
    """Custom type pvxFloActPacketAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("drop", 2),
          ("redirect", 3))
    )


_PvxFloActPacketAction_Type.__name__ = "Integer32"
_PvxFloActPacketAction_Object = MibTableColumn
pvxFloActPacketAction = _PvxFloActPacketAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 5),
    _PvxFloActPacketAction_Type()
)
pvxFloActPacketAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActPacketAction.setStatus("current")
_PvxFloActRedirectToInterfaceIndex_Type = DisplayString
_PvxFloActRedirectToInterfaceIndex_Object = MibTableColumn
pvxFloActRedirectToInterfaceIndex = _PvxFloActRedirectToInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 6),
    _PvxFloActRedirectToInterfaceIndex_Type()
)
pvxFloActRedirectToInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActRedirectToInterfaceIndex.setStatus("current")


class _PvxFloActMirrorType_Type(Integer32):
    """Custom type pvxFloActMirrorType based on Integer32"""
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
        *(("both", 4),
          ("egress", 3),
          ("ingress", 2),
          ("none", 1))
    )


_PvxFloActMirrorType_Type.__name__ = "Integer32"
_PvxFloActMirrorType_Object = MibTableColumn
pvxFloActMirrorType = _PvxFloActMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 7),
    _PvxFloActMirrorType_Type()
)
pvxFloActMirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActMirrorType.setStatus("current")
_PvxFloActMirrorToInterfaceIndex_Type = DisplayString
_PvxFloActMirrorToInterfaceIndex_Object = MibTableColumn
pvxFloActMirrorToInterfaceIndex = _PvxFloActMirrorToInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 8),
    _PvxFloActMirrorToInterfaceIndex_Type()
)
pvxFloActMirrorToInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActMirrorToInterfaceIndex.setStatus("current")


class _PvxFloActSVlanValue_Type(Integer32):
    """Custom type pvxFloActSVlanValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PvxFloActSVlanValue_Type.__name__ = "Integer32"
_PvxFloActSVlanValue_Object = MibTableColumn
pvxFloActSVlanValue = _PvxFloActSVlanValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 9),
    _PvxFloActSVlanValue_Type()
)
pvxFloActSVlanValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActSVlanValue.setStatus("current")


class _PvxFloActCVlanValue_Type(Integer32):
    """Custom type pvxFloActCVlanValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PvxFloActCVlanValue_Type.__name__ = "Integer32"
_PvxFloActCVlanValue_Object = MibTableColumn
pvxFloActCVlanValue = _PvxFloActCVlanValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 10),
    _PvxFloActCVlanValue_Type()
)
pvxFloActCVlanValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActCVlanValue.setStatus("current")


class _PvxFloActSVlanAction_Type(Integer32):
    """Custom type pvxFloActSVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("replace", 3))
    )


_PvxFloActSVlanAction_Type.__name__ = "Integer32"
_PvxFloActSVlanAction_Object = MibTableColumn
pvxFloActSVlanAction = _PvxFloActSVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 11),
    _PvxFloActSVlanAction_Type()
)
pvxFloActSVlanAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActSVlanAction.setStatus("current")


class _PvxFloActCVlanAction_Type(Integer32):
    """Custom type pvxFloActCVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("replace", 3))
    )


_PvxFloActCVlanAction_Type.__name__ = "Integer32"
_PvxFloActCVlanAction_Object = MibTableColumn
pvxFloActCVlanAction = _PvxFloActCVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 12),
    _PvxFloActCVlanAction_Type()
)
pvxFloActCVlanAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActCVlanAction.setStatus("current")


class _PvxFloActGreenAction_Type(Integer32):
    """Custom type pvxFloActGreenAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotDrop", 1),
          ("drop", 2))
    )


_PvxFloActGreenAction_Type.__name__ = "Integer32"
_PvxFloActGreenAction_Object = MibTableColumn
pvxFloActGreenAction = _PvxFloActGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 13),
    _PvxFloActGreenAction_Type()
)
pvxFloActGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActGreenAction.setStatus("current")


class _PvxFloActGreenCNGAction_Type(Integer32):
    """Custom type pvxFloActGreenCNGAction based on Integer32"""
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
        *(("doNotChange", 1),
          ("green", 2),
          ("red", 4),
          ("yellow", 3))
    )


_PvxFloActGreenCNGAction_Type.__name__ = "Integer32"
_PvxFloActGreenCNGAction_Object = MibTableColumn
pvxFloActGreenCNGAction = _PvxFloActGreenCNGAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 14),
    _PvxFloActGreenCNGAction_Type()
)
pvxFloActGreenCNGAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActGreenCNGAction.setStatus("current")


class _PvxFloActRedAction_Type(Integer32):
    """Custom type pvxFloActRedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotDrop", 1),
          ("drop", 2))
    )


_PvxFloActRedAction_Type.__name__ = "Integer32"
_PvxFloActRedAction_Object = MibTableColumn
pvxFloActRedAction = _PvxFloActRedAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 15),
    _PvxFloActRedAction_Type()
)
pvxFloActRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActRedAction.setStatus("current")


class _PvxFloActRedCNGAction_Type(Integer32):
    """Custom type pvxFloActRedCNGAction based on Integer32"""
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
        *(("doNotChange", 1),
          ("green", 2),
          ("red", 4),
          ("yellow", 3))
    )


_PvxFloActRedCNGAction_Type.__name__ = "Integer32"
_PvxFloActRedCNGAction_Object = MibTableColumn
pvxFloActRedCNGAction = _PvxFloActRedCNGAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 16),
    _PvxFloActRedCNGAction_Type()
)
pvxFloActRedCNGAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActRedCNGAction.setStatus("current")


class _PvxFloActYellowAction_Type(Integer32):
    """Custom type pvxFloActYellowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotDrop", 1),
          ("drop", 2))
    )


_PvxFloActYellowAction_Type.__name__ = "Integer32"
_PvxFloActYellowAction_Object = MibTableColumn
pvxFloActYellowAction = _PvxFloActYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 17),
    _PvxFloActYellowAction_Type()
)
pvxFloActYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActYellowAction.setStatus("current")


class _PvxFloActYellowCNGAction_Type(Integer32):
    """Custom type pvxFloActYellowCNGAction based on Integer32"""
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
        *(("doNotChange", 1),
          ("green", 2),
          ("red", 4),
          ("yellow", 3))
    )


_PvxFloActYellowCNGAction_Type.__name__ = "Integer32"
_PvxFloActYellowCNGAction_Object = MibTableColumn
pvxFloActYellowCNGAction = _PvxFloActYellowCNGAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 18),
    _PvxFloActYellowCNGAction_Type()
)
pvxFloActYellowCNGAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActYellowCNGAction.setStatus("current")
_PvxFloActRowStatus_Type = RowStatus
_PvxFloActRowStatus_Object = MibTableColumn
pvxFloActRowStatus = _PvxFloActRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 14, 1, 100),
    _PvxFloActRowStatus_Type()
)
pvxFloActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFloActRowStatus.setStatus("current")
_PvxFlowMeterTable_Object = MibTable
pvxFlowMeterTable = _PvxFlowMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15)
)
if mibBuilder.loadTexts:
    pvxFlowMeterTable.setStatus("current")
_PvxFlowMeterEntry_Object = MibTableRow
pvxFlowMeterEntry = _PvxFlowMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1)
)
pvxFlowMeterEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFMSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFMMeterIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowMeterEntry.setStatus("current")


class _PvxFMSwitchIdx_Type(Integer32):
    """Custom type pvxFMSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFMSwitchIdx_Type.__name__ = "Integer32"
_PvxFMSwitchIdx_Object = MibTableColumn
pvxFMSwitchIdx = _PvxFMSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1, 1),
    _PvxFMSwitchIdx_Type()
)
pvxFMSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFMSwitchIdx.setStatus("current")
_PvxFMMeterIdx_Type = Integer32
_PvxFMMeterIdx_Object = MibTableColumn
pvxFMMeterIdx = _PvxFMMeterIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1, 2),
    _PvxFMMeterIdx_Type()
)
pvxFMMeterIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFMMeterIdx.setStatus("current")
_PvxFMBWProfileId_Type = Integer32
_PvxFMBWProfileId_Object = MibTableColumn
pvxFMBWProfileId = _PvxFMBWProfileId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1, 3),
    _PvxFMBWProfileId_Type()
)
pvxFMBWProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMBWProfileId.setStatus("current")
_PvxFMMeterProfileId_Type = Integer32
_PvxFMMeterProfileId_Object = MibTableColumn
pvxFMMeterProfileId = _PvxFMMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1, 4),
    _PvxFMMeterProfileId_Type()
)
pvxFMMeterProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMMeterProfileId.setStatus("current")
_PvxFMRowStatus_Type = RowStatus
_PvxFMRowStatus_Object = MibTableColumn
pvxFMRowStatus = _PvxFMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 15, 1, 100),
    _PvxFMRowStatus_Type()
)
pvxFMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMRowStatus.setStatus("current")
_PvxFlowStatsTable_Object = MibTable
pvxFlowStatsTable = _PvxFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16)
)
if mibBuilder.loadTexts:
    pvxFlowStatsTable.setStatus("current")
_PvxFlowStatsEntry_Object = MibTableRow
pvxFlowStatsEntry = _PvxFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1)
)
pvxFlowStatsEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFSSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFSStatsIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowStatsEntry.setStatus("current")


class _PvxFSSwitchIdx_Type(Integer32):
    """Custom type pvxFSSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxFSSwitchIdx_Type.__name__ = "Integer32"
_PvxFSSwitchIdx_Object = MibTableColumn
pvxFSSwitchIdx = _PvxFSSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 1),
    _PvxFSSwitchIdx_Type()
)
pvxFSSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFSSwitchIdx.setStatus("current")
_PvxFSStatsIdx_Type = Integer32
_PvxFSStatsIdx_Object = MibTableColumn
pvxFSStatsIdx = _PvxFSStatsIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 2),
    _PvxFSStatsIdx_Type()
)
pvxFSStatsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFSStatsIdx.setStatus("current")
_PvxFSFlowId_Type = Integer32
_PvxFSFlowId_Object = MibTableColumn
pvxFSFlowId = _PvxFSFlowId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 3),
    _PvxFSFlowId_Type()
)
pvxFSFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFSFlowId.setStatus("current")
_PvxFSInProfilePackets_Type = Integer32
_PvxFSInProfilePackets_Object = MibTableColumn
pvxFSInProfilePackets = _PvxFSInProfilePackets_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 4),
    _PvxFSInProfilePackets_Type()
)
pvxFSInProfilePackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFSInProfilePackets.setStatus("current")
_PvxFSOutOfProfilePackets_Type = Integer32
_PvxFSOutOfProfilePackets_Object = MibTableColumn
pvxFSOutOfProfilePackets = _PvxFSOutOfProfilePackets_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 5),
    _PvxFSOutOfProfilePackets_Type()
)
pvxFSOutOfProfilePackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFSOutOfProfilePackets.setStatus("current")
_PvxFSCountOfClassifiedPackets_Type = Integer32
_PvxFSCountOfClassifiedPackets_Object = MibTableColumn
pvxFSCountOfClassifiedPackets = _PvxFSCountOfClassifiedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 6),
    _PvxFSCountOfClassifiedPackets_Type()
)
pvxFSCountOfClassifiedPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFSCountOfClassifiedPackets.setStatus("current")
_PvxFSRowStatus_Type = RowStatus
_PvxFSRowStatus_Object = MibTableColumn
pvxFSRowStatus = _PvxFSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 16, 1, 100),
    _PvxFSRowStatus_Type()
)
pvxFSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFSRowStatus.setStatus("current")
_PvxPbCVidRegistrationTable_Object = MibTable
pvxPbCVidRegistrationTable = _PvxPbCVidRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17)
)
if mibBuilder.loadTexts:
    pvxPbCVidRegistrationTable.setStatus("current")
_PvxPbCVidRegistrationTableEntry_Object = MibTableRow
pvxPbCVidRegistrationTableEntry = _PvxPbCVidRegistrationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1)
)
pvxPbCVidRegistrationTableEntry.setIndexNames(
    (0, "BTI-7000-MIB", "pvxL2IntfSwitchIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfShelfIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfSlotIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortTypeIdx"),
    (0, "BTI-7000-MIB", "pvxL2IntfPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxPCVRTCVlanIdFrom"),
)
if mibBuilder.loadTexts:
    pvxPbCVidRegistrationTableEntry.setStatus("current")


class _PvxPCVRTCVlanIdFrom_Type(Integer32):
    """Custom type pvxPCVRTCVlanIdFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxPCVRTCVlanIdFrom_Type.__name__ = "Integer32"
_PvxPCVRTCVlanIdFrom_Object = MibTableColumn
pvxPCVRTCVlanIdFrom = _PvxPCVRTCVlanIdFrom_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 1),
    _PvxPCVRTCVlanIdFrom_Type()
)
pvxPCVRTCVlanIdFrom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxPCVRTCVlanIdFrom.setStatus("current")


class _PvxPCVRTCVlanIdTo_Type(Integer32):
    """Custom type pvxPCVRTCVlanIdTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxPCVRTCVlanIdTo_Type.__name__ = "Integer32"
_PvxPCVRTCVlanIdTo_Object = MibTableColumn
pvxPCVRTCVlanIdTo = _PvxPCVRTCVlanIdTo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 2),
    _PvxPCVRTCVlanIdTo_Type()
)
pvxPCVRTCVlanIdTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCVRTCVlanIdTo.setStatus("current")


class _PvxPCVRTSVlanId_Type(Integer32):
    """Custom type pvxPCVRTSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxPCVRTSVlanId_Type.__name__ = "Integer32"
_PvxPCVRTSVlanId_Object = MibTableColumn
pvxPCVRTSVlanId = _PvxPCVRTSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 3),
    _PvxPCVRTSVlanId_Type()
)
pvxPCVRTSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCVRTSVlanId.setStatus("current")
_PvxPCVRTUntaggedPEP_Type = TruthValue
_PvxPCVRTUntaggedPEP_Object = MibTableColumn
pvxPCVRTUntaggedPEP = _PvxPCVRTUntaggedPEP_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 4),
    _PvxPCVRTUntaggedPEP_Type()
)
pvxPCVRTUntaggedPEP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCVRTUntaggedPEP.setStatus("current")
_PvxPCVRTUntaggedCEP_Type = TruthValue
_PvxPCVRTUntaggedCEP_Object = MibTableColumn
pvxPCVRTUntaggedCEP = _PvxPCVRTUntaggedCEP_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 5),
    _PvxPCVRTUntaggedCEP_Type()
)
pvxPCVRTUntaggedCEP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCVRTUntaggedCEP.setStatus("current")


class _PvxPCVRTSource_Type(Integer32):
    """Custom type pvxPCVRTSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoCreate", 2),
          ("manualCreate", 1))
    )


_PvxPCVRTSource_Type.__name__ = "Integer32"
_PvxPCVRTSource_Object = MibTableColumn
pvxPCVRTSource = _PvxPCVRTSource_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 6),
    _PvxPCVRTSource_Type()
)
pvxPCVRTSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxPCVRTSource.setStatus("current")
_PvxPCVRTMapOperStatus_Type = PvxCVidMapOperStatus
_PvxPCVRTMapOperStatus_Object = MibTableColumn
pvxPCVRTMapOperStatus = _PvxPCVRTMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 7),
    _PvxPCVRTMapOperStatus_Type()
)
pvxPCVRTMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxPCVRTMapOperStatus.setStatus("current")
_PvxPCVRTXlateOperStatus_Type = PvxCVidMapOperStatus
_PvxPCVRTXlateOperStatus_Object = MibTableColumn
pvxPCVRTXlateOperStatus = _PvxPCVRTXlateOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 8),
    _PvxPCVRTXlateOperStatus_Type()
)
pvxPCVRTXlateOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxPCVRTXlateOperStatus.setStatus("current")
_PvxPCVRTRowStatus_Type = RowStatus
_PvxPCVRTRowStatus_Object = MibTableColumn
pvxPCVRTRowStatus = _PvxPCVRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 17, 1, 100),
    _PvxPCVRTRowStatus_Type()
)
pvxPCVRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCVRTRowStatus.setStatus("current")
_PvxEthServiceTable_Object = MibTable
pvxEthServiceTable = _PvxEthServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18)
)
if mibBuilder.loadTexts:
    pvxEthServiceTable.setStatus("current")
_PvxEthServiceEntry_Object = MibTableRow
pvxEthServiceEntry = _PvxEthServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1)
)
pvxEthServiceEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEthSrvcSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEthSrvcName"),
)
if mibBuilder.loadTexts:
    pvxEthServiceEntry.setStatus("current")


class _PvxEthSrvcSwitchIdx_Type(Integer32):
    """Custom type pvxEthSrvcSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEthSrvcSwitchIdx_Type.__name__ = "Integer32"
_PvxEthSrvcSwitchIdx_Object = MibTableColumn
pvxEthSrvcSwitchIdx = _PvxEthSrvcSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 1),
    _PvxEthSrvcSwitchIdx_Type()
)
pvxEthSrvcSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEthSrvcSwitchIdx.setStatus("current")


class _PvxEthSrvcName_Type(DisplayString):
    """Custom type pvxEthSrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEthSrvcName_Type.__name__ = "DisplayString"
_PvxEthSrvcName_Object = MibTableColumn
pvxEthSrvcName = _PvxEthSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 2),
    _PvxEthSrvcName_Type()
)
pvxEthSrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEthSrvcName.setStatus("current")


class _PvxEthSrvcType_Type(Integer32):
    """Custom type pvxEthSrvcType based on Integer32"""
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
        *(("eplan", 3),
          ("epline", 1),
          ("eptree", 8),
          ("erps", 5),
          ("evplan", 4),
          ("evpline", 2),
          ("evptree", 9),
          ("igmp", 6),
          ("managementVLAN", 7))
    )


_PvxEthSrvcType_Type.__name__ = "Integer32"
_PvxEthSrvcType_Object = MibTableColumn
pvxEthSrvcType = _PvxEthSrvcType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 3),
    _PvxEthSrvcType_Type()
)
pvxEthSrvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcType.setStatus("current")


class _PvxEthSrvcState_Type(Integer32):
    """Custom type pvxEthSrvcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("testing", 3))
    )


_PvxEthSrvcState_Type.__name__ = "Integer32"
_PvxEthSrvcState_Object = MibTableColumn
pvxEthSrvcState = _PvxEthSrvcState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 4),
    _PvxEthSrvcState_Type()
)
pvxEthSrvcState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcState.setStatus("current")
_PvxEthSrvcOperState_Type = OperStatus
_PvxEthSrvcOperState_Object = MibTableColumn
pvxEthSrvcOperState = _PvxEthSrvcOperState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 5),
    _PvxEthSrvcOperState_Type()
)
pvxEthSrvcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcOperState.setStatus("current")


class _PvxEthSrvcTransportType_Type(Integer32):
    """Custom type pvxEthSrvcTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("providerBridge", 1))
    )


_PvxEthSrvcTransportType_Type.__name__ = "Integer32"
_PvxEthSrvcTransportType_Object = MibTableColumn
pvxEthSrvcTransportType = _PvxEthSrvcTransportType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 6),
    _PvxEthSrvcTransportType_Type()
)
pvxEthSrvcTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcTransportType.setStatus("current")
_PvxEthSrvcSVLAN_Type = PvxVlanId
_PvxEthSrvcSVLAN_Object = MibTableColumn
pvxEthSrvcSVLAN = _PvxEthSrvcSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 7),
    _PvxEthSrvcSVLAN_Type()
)
pvxEthSrvcSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcSVLAN.setStatus("current")


class _PvxEthSrvcSpanTreeInstance_Type(Integer32):
    """Custom type pvxEthSrvcSpanTreeInstance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PvxEthSrvcSpanTreeInstance_Type.__name__ = "Integer32"
_PvxEthSrvcSpanTreeInstance_Object = MibTableColumn
pvxEthSrvcSpanTreeInstance = _PvxEthSrvcSpanTreeInstance_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 8),
    _PvxEthSrvcSpanTreeInstance_Type()
)
pvxEthSrvcSpanTreeInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcSpanTreeInstance.setStatus("current")
_PvxEthSrvcMaxUNIs_Type = Integer32
_PvxEthSrvcMaxUNIs_Object = MibTableColumn
pvxEthSrvcMaxUNIs = _PvxEthSrvcMaxUNIs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 9),
    _PvxEthSrvcMaxUNIs_Type()
)
pvxEthSrvcMaxUNIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcMaxUNIs.setStatus("current")
_PvxEthSrvcNumUNIs_Type = Integer32
_PvxEthSrvcNumUNIs_Object = MibTableColumn
pvxEthSrvcNumUNIs = _PvxEthSrvcNumUNIs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 10),
    _PvxEthSrvcNumUNIs_Type()
)
pvxEthSrvcNumUNIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcNumUNIs.setStatus("current")


class _PvxEthSrvcPointedness_Type(Integer32):
    """Custom type pvxEthSrvcPointedness based on Integer32"""
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
        *(("internal", 3),
          ("multiPoint", 2),
          ("pointToPoint", 1),
          ("ring", 4))
    )


_PvxEthSrvcPointedness_Type.__name__ = "Integer32"
_PvxEthSrvcPointedness_Object = MibTableColumn
pvxEthSrvcPointedness = _PvxEthSrvcPointedness_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 11),
    _PvxEthSrvcPointedness_Type()
)
pvxEthSrvcPointedness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcPointedness.setStatus("current")


class _PvxEthSrvcFrameSize_Type(Integer32):
    """Custom type pvxEthSrvcFrameSize based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_PvxEthSrvcFrameSize_Type.__name__ = "Integer32"
_PvxEthSrvcFrameSize_Object = MibTableColumn
pvxEthSrvcFrameSize = _PvxEthSrvcFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 12),
    _PvxEthSrvcFrameSize_Type()
)
pvxEthSrvcFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcFrameSize.setStatus("current")
_PvxEthSrvcCVidXlate_Type = TruthValue
_PvxEthSrvcCVidXlate_Object = MibTableColumn
pvxEthSrvcCVidXlate = _PvxEthSrvcCVidXlate_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 13),
    _PvxEthSrvcCVidXlate_Type()
)
pvxEthSrvcCVidXlate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcCVidXlate.setStatus("current")


class _PvxEthSrvcMECciInterval_Type(Integer32):
    """Custom type pvxEthSrvcMECciInterval based on Integer32"""
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
        *(("interval100ms", 4),
          ("interval10min", 8),
          ("interval10ms", 3),
          ("interval10s", 6),
          ("interval1min", 7),
          ("interval1s", 5),
          ("interval300Hz", 2),
          ("intervalInvalid", 1))
    )


_PvxEthSrvcMECciInterval_Type.__name__ = "Integer32"
_PvxEthSrvcMECciInterval_Object = MibTableColumn
pvxEthSrvcMECciInterval = _PvxEthSrvcMECciInterval_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 14),
    _PvxEthSrvcMECciInterval_Type()
)
pvxEthSrvcMECciInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcMECciInterval.setStatus("current")
_PvxEthSrvcMECciEnable_Type = TruthValue
_PvxEthSrvcMECciEnable_Object = MibTableColumn
pvxEthSrvcMECciEnable = _PvxEthSrvcMECciEnable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 15),
    _PvxEthSrvcMECciEnable_Type()
)
pvxEthSrvcMECciEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcMECciEnable.setStatus("current")


class _PvxEthSrvcMEName_Type(DisplayString):
    """Custom type pvxEthSrvcMEName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_PvxEthSrvcMEName_Type.__name__ = "DisplayString"
_PvxEthSrvcMEName_Object = MibTableColumn
pvxEthSrvcMEName = _PvxEthSrvcMEName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 16),
    _PvxEthSrvcMEName_Type()
)
pvxEthSrvcMEName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcMEName.setStatus("current")
_PvxEthSrvcMaxNNIs_Type = Integer32
_PvxEthSrvcMaxNNIs_Object = MibTableColumn
pvxEthSrvcMaxNNIs = _PvxEthSrvcMaxNNIs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 17),
    _PvxEthSrvcMaxNNIs_Type()
)
pvxEthSrvcMaxNNIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcMaxNNIs.setStatus("current")
_PvxEthSrvcNumNNIs_Type = Integer32
_PvxEthSrvcNumNNIs_Object = MibTableColumn
pvxEthSrvcNumNNIs = _PvxEthSrvcNumNNIs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 18),
    _PvxEthSrvcNumNNIs_Type()
)
pvxEthSrvcNumNNIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcNumNNIs.setStatus("current")
_PvxEthSrvcLockNNIs_Type = TruthValue
_PvxEthSrvcLockNNIs_Object = MibTableColumn
pvxEthSrvcLockNNIs = _PvxEthSrvcLockNNIs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 19),
    _PvxEthSrvcLockNNIs_Type()
)
pvxEthSrvcLockNNIs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcLockNNIs.setStatus("current")
_PvxEthSrvcExceedMaxUNI_Type = TruthValue
_PvxEthSrvcExceedMaxUNI_Object = MibTableColumn
pvxEthSrvcExceedMaxUNI = _PvxEthSrvcExceedMaxUNI_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 20),
    _PvxEthSrvcExceedMaxUNI_Type()
)
pvxEthSrvcExceedMaxUNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEthSrvcExceedMaxUNI.setStatus("current")
_PvxEthSrvcRowStatus_Type = RowStatus
_PvxEthSrvcRowStatus_Object = MibTableColumn
pvxEthSrvcRowStatus = _PvxEthSrvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 18, 1, 100),
    _PvxEthSrvcRowStatus_Type()
)
pvxEthSrvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEthSrvcRowStatus.setStatus("current")
_PvxServiceUNITable_Object = MibTable
pvxServiceUNITable = _PvxServiceUNITable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19)
)
if mibBuilder.loadTexts:
    pvxServiceUNITable.setStatus("current")
_PvxServiceUNIEntry_Object = MibTableRow
pvxServiceUNIEntry = _PvxServiceUNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1)
)
pvxServiceUNIEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIPortId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISrvcName"),
)
if mibBuilder.loadTexts:
    pvxServiceUNIEntry.setStatus("current")


class _PvxSrvcUNISwitchId_Type(Integer32):
    """Custom type pvxSrvcUNISwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSrvcUNISwitchId_Type.__name__ = "Integer32"
_PvxSrvcUNISwitchId_Object = MibTableColumn
pvxSrvcUNISwitchId = _PvxSrvcUNISwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 1),
    _PvxSrvcUNISwitchId_Type()
)
pvxSrvcUNISwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNISwitchId.setStatus("current")


class _PvxSrvcUNIShelfId_Type(Integer32):
    """Custom type pvxSrvcUNIShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSrvcUNIShelfId_Type.__name__ = "Integer32"
_PvxSrvcUNIShelfId_Object = MibTableColumn
pvxSrvcUNIShelfId = _PvxSrvcUNIShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 2),
    _PvxSrvcUNIShelfId_Type()
)
pvxSrvcUNIShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNIShelfId.setStatus("current")


class _PvxSrvcUNISlotId_Type(Integer32):
    """Custom type pvxSrvcUNISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSrvcUNISlotId_Type.__name__ = "Integer32"
_PvxSrvcUNISlotId_Object = MibTableColumn
pvxSrvcUNISlotId = _PvxSrvcUNISlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 3),
    _PvxSrvcUNISlotId_Type()
)
pvxSrvcUNISlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNISlotId.setStatus("current")
_PvxSrvcUNIPortTypeId_Type = PvxPortType
_PvxSrvcUNIPortTypeId_Object = MibTableColumn
pvxSrvcUNIPortTypeId = _PvxSrvcUNIPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 4),
    _PvxSrvcUNIPortTypeId_Type()
)
pvxSrvcUNIPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNIPortTypeId.setStatus("current")
_PvxSrvcUNIPortId_Type = Integer32
_PvxSrvcUNIPortId_Object = MibTableColumn
pvxSrvcUNIPortId = _PvxSrvcUNIPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 5),
    _PvxSrvcUNIPortId_Type()
)
pvxSrvcUNIPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNIPortId.setStatus("current")


class _PvxSrvcUNISrvcName_Type(DisplayString):
    """Custom type pvxSrvcUNISrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxSrvcUNISrvcName_Type.__name__ = "DisplayString"
_PvxSrvcUNISrvcName_Object = MibTableColumn
pvxSrvcUNISrvcName = _PvxSrvcUNISrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 6),
    _PvxSrvcUNISrvcName_Type()
)
pvxSrvcUNISrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcUNISrvcName.setStatus("current")
_PvxSrvcUNINumCVids_Type = Integer32
_PvxSrvcUNINumCVids_Object = MibTableColumn
pvxSrvcUNINumCVids = _PvxSrvcUNINumCVids_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 7),
    _PvxSrvcUNINumCVids_Type()
)
pvxSrvcUNINumCVids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSrvcUNINumCVids.setStatus("current")


class _PvxSrvcUNIIngressBW_Type(DisplayString):
    """Custom type pvxSrvcUNIIngressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNIIngressBW_Type.__name__ = "DisplayString"
_PvxSrvcUNIIngressBW_Object = MibTableColumn
pvxSrvcUNIIngressBW = _PvxSrvcUNIIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 8),
    _PvxSrvcUNIIngressBW_Type()
)
pvxSrvcUNIIngressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIIngressBW.setStatus("current")


class _PvxSrvcUNIIngressBWperCos_Type(DisplayString):
    """Custom type pvxSrvcUNIIngressBWperCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNIIngressBWperCos_Type.__name__ = "DisplayString"
_PvxSrvcUNIIngressBWperCos_Object = MibTableColumn
pvxSrvcUNIIngressBWperCos = _PvxSrvcUNIIngressBWperCos_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 9),
    _PvxSrvcUNIIngressBWperCos_Type()
)
pvxSrvcUNIIngressBWperCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIIngressBWperCos.setStatus("current")


class _PvxSrvcUNIEgressBW_Type(DisplayString):
    """Custom type pvxSrvcUNIEgressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNIEgressBW_Type.__name__ = "DisplayString"
_PvxSrvcUNIEgressBW_Object = MibTableColumn
pvxSrvcUNIEgressBW = _PvxSrvcUNIEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 10),
    _PvxSrvcUNIEgressBW_Type()
)
pvxSrvcUNIEgressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIEgressBW.setStatus("current")


class _PvxSrvcUNIEgressBWperCos_Type(DisplayString):
    """Custom type pvxSrvcUNIEgressBWperCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNIEgressBWperCos_Type.__name__ = "DisplayString"
_PvxSrvcUNIEgressBWperCos_Object = MibTableColumn
pvxSrvcUNIEgressBWperCos = _PvxSrvcUNIEgressBWperCos_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 11),
    _PvxSrvcUNIEgressBWperCos_Type()
)
pvxSrvcUNIEgressBWperCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIEgressBWperCos.setStatus("current")


class _PvxSrvcUNIUserDefinedMepId_Type(Integer32):
    """Custom type pvxSrvcUNIUserDefinedMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PvxSrvcUNIUserDefinedMepId_Type.__name__ = "Integer32"
_PvxSrvcUNIUserDefinedMepId_Object = MibTableColumn
pvxSrvcUNIUserDefinedMepId = _PvxSrvcUNIUserDefinedMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 12),
    _PvxSrvcUNIUserDefinedMepId_Type()
)
pvxSrvcUNIUserDefinedMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIUserDefinedMepId.setStatus("current")


class _PvxSrvcUNIForwarding_Type(Integer32):
    """Custom type pvxSrvcUNIForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etree-leaf", 2),
          ("normal", 1))
    )


_PvxSrvcUNIForwarding_Type.__name__ = "Integer32"
_PvxSrvcUNIForwarding_Object = MibTableColumn
pvxSrvcUNIForwarding = _PvxSrvcUNIForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 13),
    _PvxSrvcUNIForwarding_Type()
)
pvxSrvcUNIForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIForwarding.setStatus("current")


class _PvxSrvcUNIServiceMap_Type(DisplayString):
    """Custom type pvxSrvcUNIServiceMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNIServiceMap_Type.__name__ = "DisplayString"
_PvxSrvcUNIServiceMap_Object = MibTableColumn
pvxSrvcUNIServiceMap = _PvxSrvcUNIServiceMap_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 14),
    _PvxSrvcUNIServiceMap_Type()
)
pvxSrvcUNIServiceMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIServiceMap.setStatus("current")


class _PvxSrvcUNIFilterSequence_Type(Integer32):
    """Custom type pvxSrvcUNIFilterSequence based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PvxSrvcUNIFilterSequence_Type.__name__ = "Integer32"
_PvxSrvcUNIFilterSequence_Object = MibTableColumn
pvxSrvcUNIFilterSequence = _PvxSrvcUNIFilterSequence_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 15),
    _PvxSrvcUNIFilterSequence_Type()
)
pvxSrvcUNIFilterSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIFilterSequence.setStatus("current")


class _PvxSrvcUNIEFPSDEnabled_Type(TruthValue):
    """Custom type pvxSrvcUNIEFPSDEnabled based on TruthValue"""


_PvxSrvcUNIEFPSDEnabled_Object = MibTableColumn
pvxSrvcUNIEFPSDEnabled = _PvxSrvcUNIEFPSDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 16),
    _PvxSrvcUNIEFPSDEnabled_Type()
)
pvxSrvcUNIEFPSDEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIEFPSDEnabled.setStatus("current")
_PvxSrvcUNIEFPSDLocalEFPSDState_Type = TruthValue
_PvxSrvcUNIEFPSDLocalEFPSDState_Object = MibTableColumn
pvxSrvcUNIEFPSDLocalEFPSDState = _PvxSrvcUNIEFPSDLocalEFPSDState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 17),
    _PvxSrvcUNIEFPSDLocalEFPSDState_Type()
)
pvxSrvcUNIEFPSDLocalEFPSDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSrvcUNIEFPSDLocalEFPSDState.setStatus("current")


class _PvxSrvcUNISlaMeasurementProfile_Type(DisplayString):
    """Custom type pvxSrvcUNISlaMeasurementProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcUNISlaMeasurementProfile_Type.__name__ = "DisplayString"
_PvxSrvcUNISlaMeasurementProfile_Object = MibTableColumn
pvxSrvcUNISlaMeasurementProfile = _PvxSrvcUNISlaMeasurementProfile_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 18),
    _PvxSrvcUNISlaMeasurementProfile_Type()
)
pvxSrvcUNISlaMeasurementProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNISlaMeasurementProfile.setStatus("current")
_PvxSrvcUNIRowStatus_Type = RowStatus
_PvxSrvcUNIRowStatus_Object = MibTableColumn
pvxSrvcUNIRowStatus = _PvxSrvcUNIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 19, 1, 100),
    _PvxSrvcUNIRowStatus_Type()
)
pvxSrvcUNIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcUNIRowStatus.setStatus("current")
_PvxSvidXlateTable_Object = MibTable
pvxSvidXlateTable = _PvxSvidXlateTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20)
)
if mibBuilder.loadTexts:
    pvxSvidXlateTable.setStatus("current")
_PvxSvidXlateEntry_Object = MibTableRow
pvxSvidXlateEntry = _PvxSvidXlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1)
)
pvxSvidXlateEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlateSwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlateShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlateSlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlatePortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlatePortId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSvidXlateInternalSVid"),
)
if mibBuilder.loadTexts:
    pvxSvidXlateEntry.setStatus("current")


class _PvxSvidXlateSwitchId_Type(Integer32):
    """Custom type pvxSvidXlateSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSvidXlateSwitchId_Type.__name__ = "Integer32"
_PvxSvidXlateSwitchId_Object = MibTableColumn
pvxSvidXlateSwitchId = _PvxSvidXlateSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 1),
    _PvxSvidXlateSwitchId_Type()
)
pvxSvidXlateSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlateSwitchId.setStatus("current")


class _PvxSvidXlateShelfId_Type(Integer32):
    """Custom type pvxSvidXlateShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSvidXlateShelfId_Type.__name__ = "Integer32"
_PvxSvidXlateShelfId_Object = MibTableColumn
pvxSvidXlateShelfId = _PvxSvidXlateShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 2),
    _PvxSvidXlateShelfId_Type()
)
pvxSvidXlateShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlateShelfId.setStatus("current")


class _PvxSvidXlateSlotId_Type(Integer32):
    """Custom type pvxSvidXlateSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSvidXlateSlotId_Type.__name__ = "Integer32"
_PvxSvidXlateSlotId_Object = MibTableColumn
pvxSvidXlateSlotId = _PvxSvidXlateSlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 3),
    _PvxSvidXlateSlotId_Type()
)
pvxSvidXlateSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlateSlotId.setStatus("current")
_PvxSvidXlatePortTypeId_Type = PvxPortType
_PvxSvidXlatePortTypeId_Object = MibTableColumn
pvxSvidXlatePortTypeId = _PvxSvidXlatePortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 4),
    _PvxSvidXlatePortTypeId_Type()
)
pvxSvidXlatePortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlatePortTypeId.setStatus("current")
_PvxSvidXlatePortId_Type = Integer32
_PvxSvidXlatePortId_Object = MibTableColumn
pvxSvidXlatePortId = _PvxSvidXlatePortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 5),
    _PvxSvidXlatePortId_Type()
)
pvxSvidXlatePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlatePortId.setStatus("current")
_PvxSvidXlateInternalSVid_Type = PvxVlanId
_PvxSvidXlateInternalSVid_Object = MibTableColumn
pvxSvidXlateInternalSVid = _PvxSvidXlateInternalSVid_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 6),
    _PvxSvidXlateInternalSVid_Type()
)
pvxSvidXlateInternalSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSvidXlateInternalSVid.setStatus("current")
_PvxSvidXlateExternalSVid_Type = PvxVlanId
_PvxSvidXlateExternalSVid_Object = MibTableColumn
pvxSvidXlateExternalSVid = _PvxSvidXlateExternalSVid_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 20, 1, 7),
    _PvxSvidXlateExternalSVid_Type()
)
pvxSvidXlateExternalSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxSvidXlateExternalSVid.setStatus("current")
_PvxEcfmService_ObjectIdentity = ObjectIdentity
pvxEcfmService = _PvxEcfmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21)
)
_PvxMepListTable_Object = MibTable
pvxMepListTable = _PvxMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1)
)
if mibBuilder.loadTexts:
    pvxMepListTable.setStatus("current")
_PvxMepListEntry_Object = MibTableRow
pvxMepListEntry = _PvxMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1)
)
pvxMepListEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMepListSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMepListESrvcVlanId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMepListIdentifier"),
)
if mibBuilder.loadTexts:
    pvxMepListEntry.setStatus("current")


class _PvxMepListSwitchIdx_Type(Integer32):
    """Custom type pvxMepListSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMepListSwitchIdx_Type.__name__ = "Integer32"
_PvxMepListSwitchIdx_Object = MibTableColumn
pvxMepListSwitchIdx = _PvxMepListSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 1),
    _PvxMepListSwitchIdx_Type()
)
pvxMepListSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMepListSwitchIdx.setStatus("current")


class _PvxMepListESrvcVlanId_Type(Integer32):
    """Custom type pvxMepListESrvcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxMepListESrvcVlanId_Type.__name__ = "Integer32"
_PvxMepListESrvcVlanId_Object = MibTableColumn
pvxMepListESrvcVlanId = _PvxMepListESrvcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 2),
    _PvxMepListESrvcVlanId_Type()
)
pvxMepListESrvcVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMepListESrvcVlanId.setStatus("current")


class _PvxMepListIdentifier_Type(Integer32):
    """Custom type pvxMepListIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxMepListIdentifier_Type.__name__ = "Integer32"
_PvxMepListIdentifier_Object = MibTableColumn
pvxMepListIdentifier = _PvxMepListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 3),
    _PvxMepListIdentifier_Type()
)
pvxMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMepListIdentifier.setStatus("current")


class _PvxMepLocalRemoteFlag_Type(Integer32):
    """Custom type pvxMepLocalRemoteFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMEP", 1),
          ("remoteMEP", 2))
    )


_PvxMepLocalRemoteFlag_Type.__name__ = "Integer32"
_PvxMepLocalRemoteFlag_Object = MibTableColumn
pvxMepLocalRemoteFlag = _PvxMepLocalRemoteFlag_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 4),
    _PvxMepLocalRemoteFlag_Type()
)
pvxMepLocalRemoteFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMepLocalRemoteFlag.setStatus("current")


class _PvxMepSequenceId_Type(Integer32):
    """Custom type pvxMepSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxMepSequenceId_Type.__name__ = "Integer32"
_PvxMepSequenceId_Object = MibTableColumn
pvxMepSequenceId = _PvxMepSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 5),
    _PvxMepSequenceId_Type()
)
pvxMepSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxMepSequenceId.setStatus("current")
_PvxMepListRowStatus_Type = RowStatus
_PvxMepListRowStatus_Object = MibTableColumn
pvxMepListRowStatus = _PvxMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 1, 1, 100),
    _PvxMepListRowStatus_Type()
)
pvxMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMepListRowStatus.setStatus("current")
_PvxEcfmMepTable_Object = MibTable
pvxEcfmMepTable = _PvxEcfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2)
)
if mibBuilder.loadTexts:
    pvxEcfmMepTable.setStatus("current")
_PvxEcfmMepEntry_Object = MibTableRow
pvxEcfmMepEntry = _PvxEcfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1)
)
pvxEcfmMepEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepSlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepPortId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepESrvcName"),
)
if mibBuilder.loadTexts:
    pvxEcfmMepEntry.setStatus("current")


class _PvxEcfmMepSwitchIdx_Type(Integer32):
    """Custom type pvxEcfmMepSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEcfmMepSwitchIdx_Type.__name__ = "Integer32"
_PvxEcfmMepSwitchIdx_Object = MibTableColumn
pvxEcfmMepSwitchIdx = _PvxEcfmMepSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 1),
    _PvxEcfmMepSwitchIdx_Type()
)
pvxEcfmMepSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepSwitchIdx.setStatus("current")


class _PvxEcfmMepShelfId_Type(Integer32):
    """Custom type pvxEcfmMepShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxEcfmMepShelfId_Type.__name__ = "Integer32"
_PvxEcfmMepShelfId_Object = MibTableColumn
pvxEcfmMepShelfId = _PvxEcfmMepShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 2),
    _PvxEcfmMepShelfId_Type()
)
pvxEcfmMepShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepShelfId.setStatus("current")


class _PvxEcfmMepSlotId_Type(Integer32):
    """Custom type pvxEcfmMepSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxEcfmMepSlotId_Type.__name__ = "Integer32"
_PvxEcfmMepSlotId_Object = MibTableColumn
pvxEcfmMepSlotId = _PvxEcfmMepSlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 3),
    _PvxEcfmMepSlotId_Type()
)
pvxEcfmMepSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepSlotId.setStatus("current")
_PvxEcfmMepPortTypeId_Type = PvxPortType
_PvxEcfmMepPortTypeId_Object = MibTableColumn
pvxEcfmMepPortTypeId = _PvxEcfmMepPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 4),
    _PvxEcfmMepPortTypeId_Type()
)
pvxEcfmMepPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepPortTypeId.setStatus("current")
_PvxEcfmMepPortId_Type = Integer32
_PvxEcfmMepPortId_Object = MibTableColumn
pvxEcfmMepPortId = _PvxEcfmMepPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 5),
    _PvxEcfmMepPortId_Type()
)
pvxEcfmMepPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepPortId.setStatus("current")


class _PvxEcfmMepESrvcName_Type(DisplayString):
    """Custom type pvxEcfmMepESrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmMepESrvcName_Type.__name__ = "DisplayString"
_PvxEcfmMepESrvcName_Object = MibTableColumn
pvxEcfmMepESrvcName = _PvxEcfmMepESrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 6),
    _PvxEcfmMepESrvcName_Type()
)
pvxEcfmMepESrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepESrvcName.setStatus("current")


class _PvxEcfmMepIdentifier_Type(Integer32):
    """Custom type pvxEcfmMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmMepIdentifier_Type.__name__ = "Integer32"
_PvxEcfmMepIdentifier_Object = MibTableColumn
pvxEcfmMepIdentifier = _PvxEcfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 7),
    _PvxEcfmMepIdentifier_Type()
)
pvxEcfmMepIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepIdentifier.setStatus("current")


class _PvxEcfmMepDirection_Type(Integer32):
    """Custom type pvxEcfmMepDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PvxEcfmMepDirection_Type.__name__ = "Integer32"
_PvxEcfmMepDirection_Object = MibTableColumn
pvxEcfmMepDirection = _PvxEcfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 8),
    _PvxEcfmMepDirection_Type()
)
pvxEcfmMepDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepDirection.setStatus("current")


class _PvxEcfmMepActive_Type(TruthValue):
    """Custom type pvxEcfmMepActive based on TruthValue"""


_PvxEcfmMepActive_Object = MibTableColumn
pvxEcfmMepActive = _PvxEcfmMepActive_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 9),
    _PvxEcfmMepActive_Type()
)
pvxEcfmMepActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepActive.setStatus("current")


class _PvxEcfmMepAutoGenerateFlag_Type(TruthValue):
    """Custom type pvxEcfmMepAutoGenerateFlag based on TruthValue"""


_PvxEcfmMepAutoGenerateFlag_Object = MibTableColumn
pvxEcfmMepAutoGenerateFlag = _PvxEcfmMepAutoGenerateFlag_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 10),
    _PvxEcfmMepAutoGenerateFlag_Type()
)
pvxEcfmMepAutoGenerateFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepAutoGenerateFlag.setStatus("current")
_PvxEcfmMepMacAddress_Type = MacAddress
_PvxEcfmMepMacAddress_Object = MibTableColumn
pvxEcfmMepMacAddress = _PvxEcfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 11),
    _PvxEcfmMepMacAddress_Type()
)
pvxEcfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepMacAddress.setStatus("current")


class _PvxEcfmMepFlushRMepDb_Type(TruthValue):
    """Custom type pvxEcfmMepFlushRMepDb based on TruthValue"""


_PvxEcfmMepFlushRMepDb_Object = MibTableColumn
pvxEcfmMepFlushRMepDb = _PvxEcfmMepFlushRMepDb_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 12),
    _PvxEcfmMepFlushRMepDb_Type()
)
pvxEcfmMepFlushRMepDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepFlushRMepDb.setStatus("current")


class _PvxEcfmMepOutOfService_Type(TruthValue):
    """Custom type pvxEcfmMepOutOfService based on TruthValue"""


_PvxEcfmMepOutOfService_Object = MibTableColumn
pvxEcfmMepOutOfService = _PvxEcfmMepOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 13),
    _PvxEcfmMepOutOfService_Type()
)
pvxEcfmMepOutOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepOutOfService.setStatus("current")
_PvxEcfmMepY1731DefectConditions_Type = PvxY1731MepDefects
_PvxEcfmMepY1731DefectConditions_Object = MibTableColumn
pvxEcfmMepY1731DefectConditions = _PvxEcfmMepY1731DefectConditions_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 14),
    _PvxEcfmMepY1731DefectConditions_Type()
)
pvxEcfmMepY1731DefectConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepY1731DefectConditions.setStatus("current")
_PvxEcfmMepDefects_Type = PvxEcfmMepDefects
_PvxEcfmMepDefects_Object = MibTableColumn
pvxEcfmMepDefects = _PvxEcfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 15),
    _PvxEcfmMepDefects_Type()
)
pvxEcfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDefects.setStatus("current")
_PvxEcfmMepCcmSequenceErr_Type = Unsigned32
_PvxEcfmMepCcmSequenceErr_Object = MibTableColumn
pvxEcfmMepCcmSequenceErr = _PvxEcfmMepCcmSequenceErr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 16),
    _PvxEcfmMepCcmSequenceErr_Type()
)
pvxEcfmMepCcmSequenceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepCcmSequenceErr.setStatus("current")
_PvxEcfmMepSentCcms_Type = Unsigned32
_PvxEcfmMepSentCcms_Object = MibTableColumn
pvxEcfmMepSentCcms = _PvxEcfmMepSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 17),
    _PvxEcfmMepSentCcms_Type()
)
pvxEcfmMepSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepSentCcms.setStatus("current")


class _PvxEcfmMepTransmitLtmStatus_Type(PvxEcfmTransmitStatus):
    """Custom type pvxEcfmMepTransmitLtmStatus based on PvxEcfmTransmitStatus"""


_PvxEcfmMepTransmitLtmStatus_Object = MibTableColumn
pvxEcfmMepTransmitLtmStatus = _PvxEcfmMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 18),
    _PvxEcfmMepTransmitLtmStatus_Type()
)
pvxEcfmMepTransmitLtmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLtmStatus.setStatus("current")


class _PvxEcfmMepTransmitLtmTargetMepId_Type(Integer32):
    """Custom type pvxEcfmMepTransmitLtmTargetMepId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmMepTransmitLtmTargetMepId_Type.__name__ = "Integer32"
_PvxEcfmMepTransmitLtmTargetMepId_Object = MibTableColumn
pvxEcfmMepTransmitLtmTargetMepId = _PvxEcfmMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 19),
    _PvxEcfmMepTransmitLtmTargetMepId_Type()
)
pvxEcfmMepTransmitLtmTargetMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLtmTargetMepId.setStatus("current")


class _PvxEcfmMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type pvxEcfmMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxEcfmMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_PvxEcfmMepTransmitLtmTtl_Object = MibTableColumn
pvxEcfmMepTransmitLtmTtl = _PvxEcfmMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 20),
    _PvxEcfmMepTransmitLtmTtl_Type()
)
pvxEcfmMepTransmitLtmTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLtmTtl.setStatus("current")
_PvxEcfmMepTransmitLtmResultOK_Type = TruthValue
_PvxEcfmMepTransmitLtmResultOK_Object = MibTableColumn
pvxEcfmMepTransmitLtmResultOK = _PvxEcfmMepTransmitLtmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 21),
    _PvxEcfmMepTransmitLtmResultOK_Type()
)
pvxEcfmMepTransmitLtmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLtmResultOK.setStatus("current")
_PvxEcfmMepTransmitLtmSeqNumber_Type = Unsigned32
_PvxEcfmMepTransmitLtmSeqNumber_Object = MibTableColumn
pvxEcfmMepTransmitLtmSeqNumber = _PvxEcfmMepTransmitLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 22),
    _PvxEcfmMepTransmitLtmSeqNumber_Type()
)
pvxEcfmMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLtmSeqNumber.setStatus("current")


class _PvxEcfmMepTransmitLbmStatus_Type(PvxEcfmTransmitStatus):
    """Custom type pvxEcfmMepTransmitLbmStatus based on PvxEcfmTransmitStatus"""


_PvxEcfmMepTransmitLbmStatus_Object = MibTableColumn
pvxEcfmMepTransmitLbmStatus = _PvxEcfmMepTransmitLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 23),
    _PvxEcfmMepTransmitLbmStatus_Type()
)
pvxEcfmMepTransmitLbmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLbmStatus.setStatus("current")


class _PvxEcfmMepTransmitLbmDestMepId_Type(Integer32):
    """Custom type pvxEcfmMepTransmitLbmDestMepId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmMepTransmitLbmDestMepId_Type.__name__ = "Integer32"
_PvxEcfmMepTransmitLbmDestMepId_Object = MibTableColumn
pvxEcfmMepTransmitLbmDestMepId = _PvxEcfmMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 24),
    _PvxEcfmMepTransmitLbmDestMepId_Type()
)
pvxEcfmMepTransmitLbmDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLbmDestMepId.setStatus("current")


class _PvxEcfmMepTransmitLbmCount_Type(Unsigned32):
    """Custom type pvxEcfmMepTransmitLbmCount based on Unsigned32"""
    defaultValue = 0


_PvxEcfmMepTransmitLbmCount_Object = MibTableColumn
pvxEcfmMepTransmitLbmCount = _PvxEcfmMepTransmitLbmCount_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 25),
    _PvxEcfmMepTransmitLbmCount_Type()
)
pvxEcfmMepTransmitLbmCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLbmCount.setStatus("current")
_PvxEcfmMepTransmitLbmResultOK_Type = TruthValue
_PvxEcfmMepTransmitLbmResultOK_Object = MibTableColumn
pvxEcfmMepTransmitLbmResultOK = _PvxEcfmMepTransmitLbmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 26),
    _PvxEcfmMepTransmitLbmResultOK_Type()
)
pvxEcfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepTransmitLbmResultOK.setStatus("current")


class _PvxEcfmMepY1731LbmCurrentTransId_Type(Unsigned32):
    """Custom type pvxEcfmMepY1731LbmCurrentTransId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PvxEcfmMepY1731LbmCurrentTransId_Type.__name__ = "Unsigned32"
_PvxEcfmMepY1731LbmCurrentTransId_Object = MibTableColumn
pvxEcfmMepY1731LbmCurrentTransId = _PvxEcfmMepY1731LbmCurrentTransId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 27),
    _PvxEcfmMepY1731LbmCurrentTransId_Type()
)
pvxEcfmMepY1731LbmCurrentTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepY1731LbmCurrentTransId.setStatus("current")
_PvxEcfmMepLbrIn_Type = Unsigned32
_PvxEcfmMepLbrIn_Object = MibTableColumn
pvxEcfmMepLbrIn = _PvxEcfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 28),
    _PvxEcfmMepLbrIn_Type()
)
pvxEcfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepLbrIn.setStatus("current")
_PvxEcfmMepLbrInOutOfOrder_Type = Unsigned32
_PvxEcfmMepLbrInOutOfOrder_Object = MibTableColumn
pvxEcfmMepLbrInOutOfOrder = _PvxEcfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 29),
    _PvxEcfmMepLbrInOutOfOrder_Type()
)
pvxEcfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepLbrInOutOfOrder.setStatus("current")
_PvxEcfmMepLbrBadMsdu_Type = Unsigned32
_PvxEcfmMepLbrBadMsdu_Object = MibTableColumn
pvxEcfmMepLbrBadMsdu = _PvxEcfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 30),
    _PvxEcfmMepLbrBadMsdu_Type()
)
pvxEcfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepLbrBadMsdu.setStatus("current")
_PvxEcfmMepLbrOut_Type = Unsigned32
_PvxEcfmMepLbrOut_Object = MibTableColumn
pvxEcfmMepLbrOut = _PvxEcfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 31),
    _PvxEcfmMepLbrOut_Type()
)
pvxEcfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepLbrOut.setStatus("current")
_PvxEcfmMepUnexpLtrIn_Type = Unsigned32
_PvxEcfmMepUnexpLtrIn_Object = MibTableColumn
pvxEcfmMepUnexpLtrIn = _PvxEcfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 32),
    _PvxEcfmMepUnexpLtrIn_Type()
)
pvxEcfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepUnexpLtrIn.setStatus("current")
_PvxEcfmMepErrCcmRMepId_Type = Unsigned32
_PvxEcfmMepErrCcmRMepId_Object = MibTableColumn
pvxEcfmMepErrCcmRMepId = _PvxEcfmMepErrCcmRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 33),
    _PvxEcfmMepErrCcmRMepId_Type()
)
pvxEcfmMepErrCcmRMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepErrCcmRMepId.setStatus("current")
_PvxEcfmMepXconnRMepId_Type = Unsigned32
_PvxEcfmMepXconnRMepId_Object = MibTableColumn
pvxEcfmMepXconnRMepId = _PvxEcfmMepXconnRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 2, 1, 34),
    _PvxEcfmMepXconnRMepId_Type()
)
pvxEcfmMepXconnRMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepXconnRMepId.setStatus("current")
_PvxEcfmMepDbTable_Object = MibTable
pvxEcfmMepDbTable = _PvxEcfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3)
)
if mibBuilder.loadTexts:
    pvxEcfmMepDbTable.setStatus("current")
_PvxEcfmMepDbEntry_Object = MibTableRow
pvxEcfmMepDbEntry = _PvxEcfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1)
)
pvxEcfmMepDbEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDbSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDbVlanId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDbLocalMepId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDbRemoteMepId"),
)
if mibBuilder.loadTexts:
    pvxEcfmMepDbEntry.setStatus("current")


class _PvxEcfmMepDbSwitchIdx_Type(Integer32):
    """Custom type pvxEcfmMepDbSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEcfmMepDbSwitchIdx_Type.__name__ = "Integer32"
_PvxEcfmMepDbSwitchIdx_Object = MibTableColumn
pvxEcfmMepDbSwitchIdx = _PvxEcfmMepDbSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 1),
    _PvxEcfmMepDbSwitchIdx_Type()
)
pvxEcfmMepDbSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepDbSwitchIdx.setStatus("current")


class _PvxEcfmMepDbVlanId_Type(Integer32):
    """Custom type pvxEcfmMepDbVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxEcfmMepDbVlanId_Type.__name__ = "Integer32"
_PvxEcfmMepDbVlanId_Object = MibTableColumn
pvxEcfmMepDbVlanId = _PvxEcfmMepDbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 2),
    _PvxEcfmMepDbVlanId_Type()
)
pvxEcfmMepDbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepDbVlanId.setStatus("current")


class _PvxEcfmMepDbLocalMepId_Type(Integer32):
    """Custom type pvxEcfmMepDbLocalMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmMepDbLocalMepId_Type.__name__ = "Integer32"
_PvxEcfmMepDbLocalMepId_Object = MibTableColumn
pvxEcfmMepDbLocalMepId = _PvxEcfmMepDbLocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 3),
    _PvxEcfmMepDbLocalMepId_Type()
)
pvxEcfmMepDbLocalMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepDbLocalMepId.setStatus("current")


class _PvxEcfmMepDbRemoteMepId_Type(Integer32):
    """Custom type pvxEcfmMepDbRemoteMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmMepDbRemoteMepId_Type.__name__ = "Integer32"
_PvxEcfmMepDbRemoteMepId_Object = MibTableColumn
pvxEcfmMepDbRemoteMepId = _PvxEcfmMepDbRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 4),
    _PvxEcfmMepDbRemoteMepId_Type()
)
pvxEcfmMepDbRemoteMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRemoteMepId.setStatus("current")
_PvxEcfmMepDbRMepState_Type = PvxEcfmRemoteMepState
_PvxEcfmMepDbRMepState_Object = MibTableColumn
pvxEcfmMepDbRMepState = _PvxEcfmMepDbRMepState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 5),
    _PvxEcfmMepDbRMepState_Type()
)
pvxEcfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepState.setStatus("current")
_PvxEcfmMepDbMacAddress_Type = MacAddress
_PvxEcfmMepDbMacAddress_Object = MibTableColumn
pvxEcfmMepDbMacAddress = _PvxEcfmMepDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 6),
    _PvxEcfmMepDbMacAddress_Type()
)
pvxEcfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbMacAddress.setStatus("current")


class _PvxEcfmMepDbRMepSwitchName_Type(DisplayString):
    """Custom type pvxEcfmMepDbRMepSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmMepDbRMepSwitchName_Type.__name__ = "DisplayString"
_PvxEcfmMepDbRMepSwitchName_Object = MibTableColumn
pvxEcfmMepDbRMepSwitchName = _PvxEcfmMepDbRMepSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 7),
    _PvxEcfmMepDbRMepSwitchName_Type()
)
pvxEcfmMepDbRMepSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepSwitchName.setStatus("current")


class _PvxEcfmMepDbRMepPortInfo_Type(DisplayString):
    """Custom type pvxEcfmMepDbRMepPortInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmMepDbRMepPortInfo_Type.__name__ = "DisplayString"
_PvxEcfmMepDbRMepPortInfo_Object = MibTableColumn
pvxEcfmMepDbRMepPortInfo = _PvxEcfmMepDbRMepPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 8),
    _PvxEcfmMepDbRMepPortInfo_Type()
)
pvxEcfmMepDbRMepPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepPortInfo.setStatus("current")
_PvxEcfmMepDbRMepRDI_Type = TruthValue
_PvxEcfmMepDbRMepRDI_Object = MibTableColumn
pvxEcfmMepDbRMepRDI = _PvxEcfmMepDbRMepRDI_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 9),
    _PvxEcfmMepDbRMepRDI_Type()
)
pvxEcfmMepDbRMepRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepRDI.setStatus("current")
_PvxEcfmMepDbRMepCcmDefect_Type = TruthValue
_PvxEcfmMepDbRMepCcmDefect_Object = MibTableColumn
pvxEcfmMepDbRMepCcmDefect = _PvxEcfmMepDbRMepCcmDefect_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 10),
    _PvxEcfmMepDbRMepCcmDefect_Type()
)
pvxEcfmMepDbRMepCcmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepCcmDefect.setStatus("current")
_PvxEcfmMepDbRMepPortStatusDefect_Type = TruthValue
_PvxEcfmMepDbRMepPortStatusDefect_Object = MibTableColumn
pvxEcfmMepDbRMepPortStatusDefect = _PvxEcfmMepDbRMepPortStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 11),
    _PvxEcfmMepDbRMepPortStatusDefect_Type()
)
pvxEcfmMepDbRMepPortStatusDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepPortStatusDefect.setStatus("current")
_PvxEcfmMepDbRMepIntfStatusDefect_Type = TruthValue
_PvxEcfmMepDbRMepIntfStatusDefect_Object = MibTableColumn
pvxEcfmMepDbRMepIntfStatusDefect = _PvxEcfmMepDbRMepIntfStatusDefect_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 3, 1, 12),
    _PvxEcfmMepDbRMepIntfStatusDefect_Type()
)
pvxEcfmMepDbRMepIntfStatusDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMepDbRMepIntfStatusDefect.setStatus("current")
_PvxEcfmMipTable_Object = MibTable
pvxEcfmMipTable = _PvxEcfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4)
)
if mibBuilder.loadTexts:
    pvxEcfmMipTable.setStatus("current")
_PvxEcfmMipEntry_Object = MibTableRow
pvxEcfmMipEntry = _PvxEcfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1)
)
pvxEcfmMipEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipSlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipPortId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipMegLevel"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmMipESrvcVlanId"),
)
if mibBuilder.loadTexts:
    pvxEcfmMipEntry.setStatus("current")


class _PvxEcfmMipSwitchIdx_Type(Integer32):
    """Custom type pvxEcfmMipSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEcfmMipSwitchIdx_Type.__name__ = "Integer32"
_PvxEcfmMipSwitchIdx_Object = MibTableColumn
pvxEcfmMipSwitchIdx = _PvxEcfmMipSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 1),
    _PvxEcfmMipSwitchIdx_Type()
)
pvxEcfmMipSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipSwitchIdx.setStatus("current")


class _PvxEcfmMipShelfId_Type(Integer32):
    """Custom type pvxEcfmMipShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxEcfmMipShelfId_Type.__name__ = "Integer32"
_PvxEcfmMipShelfId_Object = MibTableColumn
pvxEcfmMipShelfId = _PvxEcfmMipShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 2),
    _PvxEcfmMipShelfId_Type()
)
pvxEcfmMipShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipShelfId.setStatus("current")


class _PvxEcfmMipSlotId_Type(Integer32):
    """Custom type pvxEcfmMipSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxEcfmMipSlotId_Type.__name__ = "Integer32"
_PvxEcfmMipSlotId_Object = MibTableColumn
pvxEcfmMipSlotId = _PvxEcfmMipSlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 3),
    _PvxEcfmMipSlotId_Type()
)
pvxEcfmMipSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipSlotId.setStatus("current")
_PvxEcfmMipPortTypeId_Type = PvxPortType
_PvxEcfmMipPortTypeId_Object = MibTableColumn
pvxEcfmMipPortTypeId = _PvxEcfmMipPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 4),
    _PvxEcfmMipPortTypeId_Type()
)
pvxEcfmMipPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipPortTypeId.setStatus("current")


class _PvxEcfmMipPortId_Type(Integer32):
    """Custom type pvxEcfmMipPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PvxEcfmMipPortId_Type.__name__ = "Integer32"
_PvxEcfmMipPortId_Object = MibTableColumn
pvxEcfmMipPortId = _PvxEcfmMipPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 5),
    _PvxEcfmMipPortId_Type()
)
pvxEcfmMipPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipPortId.setStatus("current")


class _PvxEcfmMipMegLevel_Type(Integer32):
    """Custom type pvxEcfmMipMegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PvxEcfmMipMegLevel_Type.__name__ = "Integer32"
_PvxEcfmMipMegLevel_Object = MibTableColumn
pvxEcfmMipMegLevel = _PvxEcfmMipMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 6),
    _PvxEcfmMipMegLevel_Type()
)
pvxEcfmMipMegLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipMegLevel.setStatus("current")


class _PvxEcfmMipESrvcVlanId_Type(Integer32):
    """Custom type pvxEcfmMipESrvcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxEcfmMipESrvcVlanId_Type.__name__ = "Integer32"
_PvxEcfmMipESrvcVlanId_Object = MibTableColumn
pvxEcfmMipESrvcVlanId = _PvxEcfmMipESrvcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 7),
    _PvxEcfmMipESrvcVlanId_Type()
)
pvxEcfmMipESrvcVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmMipESrvcVlanId.setStatus("current")


class _PvxEcfmMipESrvcName_Type(DisplayString):
    """Custom type pvxEcfmMipESrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmMipESrvcName_Type.__name__ = "DisplayString"
_PvxEcfmMipESrvcName_Object = MibTableColumn
pvxEcfmMipESrvcName = _PvxEcfmMipESrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 8),
    _PvxEcfmMipESrvcName_Type()
)
pvxEcfmMipESrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmMipESrvcName.setStatus("current")
_PvxEcfmMipActiveState_Type = TruthValue
_PvxEcfmMipActiveState_Object = MibTableColumn
pvxEcfmMipActiveState = _PvxEcfmMipActiveState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 9),
    _PvxEcfmMipActiveState_Type()
)
pvxEcfmMipActiveState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEcfmMipActiveState.setStatus("current")
_PvxEcfmMipRowStatus_Type = RowStatus
_PvxEcfmMipRowStatus_Object = MibTableColumn
pvxEcfmMipRowStatus = _PvxEcfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 4, 1, 100),
    _PvxEcfmMipRowStatus_Type()
)
pvxEcfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxEcfmMipRowStatus.setStatus("current")
_PvxY1731LbStatsTable_Object = MibTable
pvxY1731LbStatsTable = _PvxY1731LbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6)
)
if mibBuilder.loadTexts:
    pvxY1731LbStatsTable.setStatus("current")
_PvxY1731LbStatsEntry_Object = MibTableRow
pvxY1731LbStatsEntry = _PvxY1731LbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1)
)
pvxY1731LbStatsEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxY1731LbStatsSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxY1731LbStatsESrvcName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxY1731LbStatsIdentifier"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxY1731LbmTransId"),
)
if mibBuilder.loadTexts:
    pvxY1731LbStatsEntry.setStatus("current")


class _PvxY1731LbStatsSwitchIdx_Type(Integer32):
    """Custom type pvxY1731LbStatsSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxY1731LbStatsSwitchIdx_Type.__name__ = "Integer32"
_PvxY1731LbStatsSwitchIdx_Object = MibTableColumn
pvxY1731LbStatsSwitchIdx = _PvxY1731LbStatsSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 1),
    _PvxY1731LbStatsSwitchIdx_Type()
)
pvxY1731LbStatsSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxY1731LbStatsSwitchIdx.setStatus("current")


class _PvxY1731LbStatsESrvcName_Type(DisplayString):
    """Custom type pvxY1731LbStatsESrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxY1731LbStatsESrvcName_Type.__name__ = "DisplayString"
_PvxY1731LbStatsESrvcName_Object = MibTableColumn
pvxY1731LbStatsESrvcName = _PvxY1731LbStatsESrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 2),
    _PvxY1731LbStatsESrvcName_Type()
)
pvxY1731LbStatsESrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxY1731LbStatsESrvcName.setStatus("current")


class _PvxY1731LbStatsIdentifier_Type(Integer32):
    """Custom type pvxY1731LbStatsIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxY1731LbStatsIdentifier_Type.__name__ = "Integer32"
_PvxY1731LbStatsIdentifier_Object = MibTableColumn
pvxY1731LbStatsIdentifier = _PvxY1731LbStatsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 3),
    _PvxY1731LbStatsIdentifier_Type()
)
pvxY1731LbStatsIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxY1731LbStatsIdentifier.setStatus("current")


class _PvxY1731LbmTransId_Type(Unsigned32):
    """Custom type pvxY1731LbmTransId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PvxY1731LbmTransId_Type.__name__ = "Unsigned32"
_PvxY1731LbmTransId_Object = MibTableColumn
pvxY1731LbmTransId = _PvxY1731LbmTransId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 4),
    _PvxY1731LbmTransId_Type()
)
pvxY1731LbmTransId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxY1731LbmTransId.setStatus("current")
_PvxY1731LbStatsLbmOut_Type = Unsigned32
_PvxY1731LbStatsLbmOut_Object = MibTableColumn
pvxY1731LbStatsLbmOut = _PvxY1731LbStatsLbmOut_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 5),
    _PvxY1731LbStatsLbmOut_Type()
)
pvxY1731LbStatsLbmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsLbmOut.setStatus("current")
_PvxY1731LbStatsLbrIn_Type = Unsigned32
_PvxY1731LbStatsLbrIn_Object = MibTableColumn
pvxY1731LbStatsLbrIn = _PvxY1731LbStatsLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 6),
    _PvxY1731LbStatsLbrIn_Type()
)
pvxY1731LbStatsLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsLbrIn.setStatus("current")
_PvxY1731LbStatsLbrTimeAverage_Type = TimeInterval
_PvxY1731LbStatsLbrTimeAverage_Object = MibTableColumn
pvxY1731LbStatsLbrTimeAverage = _PvxY1731LbStatsLbrTimeAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 7),
    _PvxY1731LbStatsLbrTimeAverage_Type()
)
pvxY1731LbStatsLbrTimeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsLbrTimeAverage.setStatus("current")
_PvxY1731LbStatsLbrTimeMin_Type = TimeInterval
_PvxY1731LbStatsLbrTimeMin_Object = MibTableColumn
pvxY1731LbStatsLbrTimeMin = _PvxY1731LbStatsLbrTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 8),
    _PvxY1731LbStatsLbrTimeMin_Type()
)
pvxY1731LbStatsLbrTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsLbrTimeMin.setStatus("current")
_PvxY1731LbStatsLbrTimeMax_Type = TimeInterval
_PvxY1731LbStatsLbrTimeMax_Object = MibTableColumn
pvxY1731LbStatsLbrTimeMax = _PvxY1731LbStatsLbrTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 9),
    _PvxY1731LbStatsLbrTimeMax_Type()
)
pvxY1731LbStatsLbrTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsLbrTimeMax.setStatus("current")
_PvxY1731LbStatsTotalResponders_Type = Unsigned32
_PvxY1731LbStatsTotalResponders_Object = MibTableColumn
pvxY1731LbStatsTotalResponders = _PvxY1731LbStatsTotalResponders_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 10),
    _PvxY1731LbStatsTotalResponders_Type()
)
pvxY1731LbStatsTotalResponders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsTotalResponders.setStatus("current")
_PvxY1731LbStatsAvgLbrsPerResponder_Type = Unsigned32
_PvxY1731LbStatsAvgLbrsPerResponder_Object = MibTableColumn
pvxY1731LbStatsAvgLbrsPerResponder = _PvxY1731LbStatsAvgLbrsPerResponder_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 6, 1, 11),
    _PvxY1731LbStatsAvgLbrsPerResponder_Type()
)
pvxY1731LbStatsAvgLbrsPerResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxY1731LbStatsAvgLbrsPerResponder.setStatus("current")
_PvxEcfmLtrTable_Object = MibTable
pvxEcfmLtrTable = _PvxEcfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7)
)
if mibBuilder.loadTexts:
    pvxEcfmLtrTable.setStatus("current")
_PvxEcfmLtrEntry_Object = MibTableRow
pvxEcfmLtrEntry = _PvxEcfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1)
)
pvxEcfmLtrEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmLtrSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmLtrVlanId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmLtrMepIdentifier"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmLtrSeqNumber"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxEcfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    pvxEcfmLtrEntry.setStatus("current")


class _PvxEcfmLtrSwitchIdx_Type(Integer32):
    """Custom type pvxEcfmLtrSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxEcfmLtrSwitchIdx_Type.__name__ = "Integer32"
_PvxEcfmLtrSwitchIdx_Object = MibTableColumn
pvxEcfmLtrSwitchIdx = _PvxEcfmLtrSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 1),
    _PvxEcfmLtrSwitchIdx_Type()
)
pvxEcfmLtrSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmLtrSwitchIdx.setStatus("current")


class _PvxEcfmLtrVlanId_Type(Integer32):
    """Custom type pvxEcfmLtrVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PvxEcfmLtrVlanId_Type.__name__ = "Integer32"
_PvxEcfmLtrVlanId_Object = MibTableColumn
pvxEcfmLtrVlanId = _PvxEcfmLtrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 2),
    _PvxEcfmLtrVlanId_Type()
)
pvxEcfmLtrVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmLtrVlanId.setStatus("current")


class _PvxEcfmLtrMepIdentifier_Type(Integer32):
    """Custom type pvxEcfmLtrMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxEcfmLtrMepIdentifier_Type.__name__ = "Integer32"
_PvxEcfmLtrMepIdentifier_Object = MibTableColumn
pvxEcfmLtrMepIdentifier = _PvxEcfmLtrMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 3),
    _PvxEcfmLtrMepIdentifier_Type()
)
pvxEcfmLtrMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmLtrMepIdentifier.setStatus("current")


class _PvxEcfmLtrSeqNumber_Type(Unsigned32):
    """Custom type pvxEcfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PvxEcfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_PvxEcfmLtrSeqNumber_Object = MibTableColumn
pvxEcfmLtrSeqNumber = _PvxEcfmLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 4),
    _PvxEcfmLtrSeqNumber_Type()
)
pvxEcfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmLtrSeqNumber.setStatus("current")


class _PvxEcfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type pvxEcfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PvxEcfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_PvxEcfmLtrReceiveOrder_Object = MibTableColumn
pvxEcfmLtrReceiveOrder = _PvxEcfmLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 5),
    _PvxEcfmLtrReceiveOrder_Type()
)
pvxEcfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxEcfmLtrReceiveOrder.setStatus("current")


class _PvxEcfmLtrTtl_Type(Unsigned32):
    """Custom type pvxEcfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxEcfmLtrTtl_Type.__name__ = "Unsigned32"
_PvxEcfmLtrTtl_Object = MibTableColumn
pvxEcfmLtrTtl = _PvxEcfmLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 6),
    _PvxEcfmLtrTtl_Type()
)
pvxEcfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrTtl.setStatus("current")
_PvxEcfmLtrForwarded_Type = TruthValue
_PvxEcfmLtrForwarded_Object = MibTableColumn
pvxEcfmLtrForwarded = _PvxEcfmLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 7),
    _PvxEcfmLtrForwarded_Type()
)
pvxEcfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrForwarded.setStatus("current")
_PvxEcfmLtrTerminalMep_Type = TruthValue
_PvxEcfmLtrTerminalMep_Object = MibTableColumn
pvxEcfmLtrTerminalMep = _PvxEcfmLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 8),
    _PvxEcfmLtrTerminalMep_Type()
)
pvxEcfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrTerminalMep.setStatus("current")
_PvxEcfmLtrRelayAction_Type = PvxEcfmRelayActionFieldValue
_PvxEcfmLtrRelayAction_Object = MibTableColumn
pvxEcfmLtrRelayAction = _PvxEcfmLtrRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 9),
    _PvxEcfmLtrRelayAction_Type()
)
pvxEcfmLtrRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrRelayAction.setStatus("current")


class _PvxEcfmLtrSwitchName_Type(DisplayString):
    """Custom type pvxEcfmLtrSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmLtrSwitchName_Type.__name__ = "DisplayString"
_PvxEcfmLtrSwitchName_Object = MibTableColumn
pvxEcfmLtrSwitchName = _PvxEcfmLtrSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 10),
    _PvxEcfmLtrSwitchName_Type()
)
pvxEcfmLtrSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrSwitchName.setStatus("current")
_PvxEcfmLtrIngressAction_Type = PvxEcfmIngressActionFieldValue
_PvxEcfmLtrIngressAction_Object = MibTableColumn
pvxEcfmLtrIngressAction = _PvxEcfmLtrIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 11),
    _PvxEcfmLtrIngressAction_Type()
)
pvxEcfmLtrIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrIngressAction.setStatus("current")
_PvxEcfmLtrIngressMac_Type = MacAddress
_PvxEcfmLtrIngressMac_Object = MibTableColumn
pvxEcfmLtrIngressMac = _PvxEcfmLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 12),
    _PvxEcfmLtrIngressMac_Type()
)
pvxEcfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrIngressMac.setStatus("current")


class _PvxEcfmLtrIngressPortInfo_Type(DisplayString):
    """Custom type pvxEcfmLtrIngressPortInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmLtrIngressPortInfo_Type.__name__ = "DisplayString"
_PvxEcfmLtrIngressPortInfo_Object = MibTableColumn
pvxEcfmLtrIngressPortInfo = _PvxEcfmLtrIngressPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 13),
    _PvxEcfmLtrIngressPortInfo_Type()
)
pvxEcfmLtrIngressPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrIngressPortInfo.setStatus("current")
_PvxEcfmLtrEgressAction_Type = PvxEcfmEgressActionFieldValue
_PvxEcfmLtrEgressAction_Object = MibTableColumn
pvxEcfmLtrEgressAction = _PvxEcfmLtrEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 14),
    _PvxEcfmLtrEgressAction_Type()
)
pvxEcfmLtrEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrEgressAction.setStatus("current")
_PvxEcfmLtrEgressMac_Type = MacAddress
_PvxEcfmLtrEgressMac_Object = MibTableColumn
pvxEcfmLtrEgressMac = _PvxEcfmLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 15),
    _PvxEcfmLtrEgressMac_Type()
)
pvxEcfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrEgressMac.setStatus("current")


class _PvxEcfmLtrEgressPortInfo_Type(DisplayString):
    """Custom type pvxEcfmLtrEgressPortInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxEcfmLtrEgressPortInfo_Type.__name__ = "DisplayString"
_PvxEcfmLtrEgressPortInfo_Object = MibTableColumn
pvxEcfmLtrEgressPortInfo = _PvxEcfmLtrEgressPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 7, 1, 16),
    _PvxEcfmLtrEgressPortInfo_Type()
)
pvxEcfmLtrEgressPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxEcfmLtrEgressPortInfo.setStatus("current")
_PvxSLAThroughputTestTable_Object = MibTable
pvxSLAThroughputTestTable = _PvxSLAThroughputTestTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8)
)
if mibBuilder.loadTexts:
    pvxSLAThroughputTestTable.setStatus("current")
_PvxSLAThroughputTestEntry_Object = MibTableRow
pvxSLAThroughputTestEntry = _PvxSLAThroughputTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1)
)
pvxSLAThroughputTestEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestESName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAThroughputTestRMepId"),
)
if mibBuilder.loadTexts:
    pvxSLAThroughputTestEntry.setStatus("current")


class _PvxSLAThroughputTestSwitchIdx_Type(Integer32):
    """Custom type pvxSLAThroughputTestSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSLAThroughputTestSwitchIdx_Type.__name__ = "Integer32"
_PvxSLAThroughputTestSwitchIdx_Object = MibTableColumn
pvxSLAThroughputTestSwitchIdx = _PvxSLAThroughputTestSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 1),
    _PvxSLAThroughputTestSwitchIdx_Type()
)
pvxSLAThroughputTestSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestSwitchIdx.setStatus("current")


class _PvxSLAThroughputTestShelfIdx_Type(Integer32):
    """Custom type pvxSLAThroughputTestShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSLAThroughputTestShelfIdx_Type.__name__ = "Integer32"
_PvxSLAThroughputTestShelfIdx_Object = MibTableColumn
pvxSLAThroughputTestShelfIdx = _PvxSLAThroughputTestShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 2),
    _PvxSLAThroughputTestShelfIdx_Type()
)
pvxSLAThroughputTestShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestShelfIdx.setStatus("current")


class _PvxSLAThroughputTestSlotIdx_Type(Integer32):
    """Custom type pvxSLAThroughputTestSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSLAThroughputTestSlotIdx_Type.__name__ = "Integer32"
_PvxSLAThroughputTestSlotIdx_Object = MibTableColumn
pvxSLAThroughputTestSlotIdx = _PvxSLAThroughputTestSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 3),
    _PvxSLAThroughputTestSlotIdx_Type()
)
pvxSLAThroughputTestSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestSlotIdx.setStatus("current")
_PvxSLAThroughputTestPortTypeIdx_Type = PvxPortType
_PvxSLAThroughputTestPortTypeIdx_Object = MibTableColumn
pvxSLAThroughputTestPortTypeIdx = _PvxSLAThroughputTestPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 4),
    _PvxSLAThroughputTestPortTypeIdx_Type()
)
pvxSLAThroughputTestPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestPortTypeIdx.setStatus("current")


class _PvxSLAThroughputTestPortIdx_Type(Integer32):
    """Custom type pvxSLAThroughputTestPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxSLAThroughputTestPortIdx_Type.__name__ = "Integer32"
_PvxSLAThroughputTestPortIdx_Object = MibTableColumn
pvxSLAThroughputTestPortIdx = _PvxSLAThroughputTestPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 5),
    _PvxSLAThroughputTestPortIdx_Type()
)
pvxSLAThroughputTestPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestPortIdx.setStatus("current")
_PvxSLAThroughputTestESName_Type = DisplayString
_PvxSLAThroughputTestESName_Object = MibTableColumn
pvxSLAThroughputTestESName = _PvxSLAThroughputTestESName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 6),
    _PvxSLAThroughputTestESName_Type()
)
pvxSLAThroughputTestESName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestESName.setStatus("current")


class _PvxSLAThroughputTestRMepId_Type(Integer32):
    """Custom type pvxSLAThroughputTestRMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxSLAThroughputTestRMepId_Type.__name__ = "Integer32"
_PvxSLAThroughputTestRMepId_Object = MibTableColumn
pvxSLAThroughputTestRMepId = _PvxSLAThroughputTestRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 7),
    _PvxSLAThroughputTestRMepId_Type()
)
pvxSLAThroughputTestRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestRMepId.setStatus("current")
_PvxSLAThroughputTestRole_Type = SlaTestRole
_PvxSLAThroughputTestRole_Object = MibTableColumn
pvxSLAThroughputTestRole = _PvxSLAThroughputTestRole_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 8),
    _PvxSLAThroughputTestRole_Type()
)
pvxSLAThroughputTestRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestRole.setStatus("current")
_PvxSLAThroughputTestInitiatorCmdState_Type = CommandStateType
_PvxSLAThroughputTestInitiatorCmdState_Object = MibTableColumn
pvxSLAThroughputTestInitiatorCmdState = _PvxSLAThroughputTestInitiatorCmdState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 9),
    _PvxSLAThroughputTestInitiatorCmdState_Type()
)
pvxSLAThroughputTestInitiatorCmdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestInitiatorCmdState.setStatus("current")


class _PvxSLAThroughputTestResponderOpState_Type(Integer32):
    """Custom type pvxSLAThroughputTestResponderOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("rmepNotReady", 3),
          ("testInProgress", 2))
    )


_PvxSLAThroughputTestResponderOpState_Type.__name__ = "Integer32"
_PvxSLAThroughputTestResponderOpState_Object = MibTableColumn
pvxSLAThroughputTestResponderOpState = _PvxSLAThroughputTestResponderOpState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 10),
    _PvxSLAThroughputTestResponderOpState_Type()
)
pvxSLAThroughputTestResponderOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestResponderOpState.setStatus("current")


class _PvxSLAThroughputTestFrameSize1_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize1_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize1_Object = MibTableColumn
pvxSLAThroughputTestFrameSize1 = _PvxSLAThroughputTestFrameSize1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 11),
    _PvxSLAThroughputTestFrameSize1_Type()
)
pvxSLAThroughputTestFrameSize1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize1.setStatus("current")


class _PvxSLAThroughputTestFrameSize2_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize2_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize2_Object = MibTableColumn
pvxSLAThroughputTestFrameSize2 = _PvxSLAThroughputTestFrameSize2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 12),
    _PvxSLAThroughputTestFrameSize2_Type()
)
pvxSLAThroughputTestFrameSize2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize2.setStatus("current")


class _PvxSLAThroughputTestFrameSize3_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize3_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize3_Object = MibTableColumn
pvxSLAThroughputTestFrameSize3 = _PvxSLAThroughputTestFrameSize3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 13),
    _PvxSLAThroughputTestFrameSize3_Type()
)
pvxSLAThroughputTestFrameSize3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize3.setStatus("current")


class _PvxSLAThroughputTestFrameSize4_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize4_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize4_Object = MibTableColumn
pvxSLAThroughputTestFrameSize4 = _PvxSLAThroughputTestFrameSize4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 14),
    _PvxSLAThroughputTestFrameSize4_Type()
)
pvxSLAThroughputTestFrameSize4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize4.setStatus("current")


class _PvxSLAThroughputTestFrameSize5_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize5_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize5_Object = MibTableColumn
pvxSLAThroughputTestFrameSize5 = _PvxSLAThroughputTestFrameSize5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 15),
    _PvxSLAThroughputTestFrameSize5_Type()
)
pvxSLAThroughputTestFrameSize5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize5.setStatus("current")


class _PvxSLAThroughputTestFrameSize6_Type(Integer32):
    """Custom type pvxSLAThroughputTestFrameSize6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9600),
    )


_PvxSLAThroughputTestFrameSize6_Type.__name__ = "Integer32"
_PvxSLAThroughputTestFrameSize6_Object = MibTableColumn
pvxSLAThroughputTestFrameSize6 = _PvxSLAThroughputTestFrameSize6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 16),
    _PvxSLAThroughputTestFrameSize6_Type()
)
pvxSLAThroughputTestFrameSize6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize6.setStatus("current")
_PvxSLAThroughputTestSrvcPolicyName_Type = DisplayString
_PvxSLAThroughputTestSrvcPolicyName_Object = MibTableColumn
pvxSLAThroughputTestSrvcPolicyName = _PvxSLAThroughputTestSrvcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 17),
    _PvxSLAThroughputTestSrvcPolicyName_Type()
)
pvxSLAThroughputTestSrvcPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestSrvcPolicyName.setStatus("current")
_PvxSLAThroughputTestClassMapName_Type = DisplayString
_PvxSLAThroughputTestClassMapName_Object = MibTableColumn
pvxSLAThroughputTestClassMapName = _PvxSLAThroughputTestClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 18),
    _PvxSLAThroughputTestClassMapName_Type()
)
pvxSLAThroughputTestClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestClassMapName.setStatus("current")
_PvxSLAThroughputTestBwProfileName_Type = DisplayString
_PvxSLAThroughputTestBwProfileName_Object = MibTableColumn
pvxSLAThroughputTestBwProfileName = _PvxSLAThroughputTestBwProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 19),
    _PvxSLAThroughputTestBwProfileName_Type()
)
pvxSLAThroughputTestBwProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestBwProfileName.setStatus("current")


class _PvxSLAThroughputTestSVlanPriority_Type(Integer32):
    """Custom type pvxSLAThroughputTestSVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxSLAThroughputTestSVlanPriority_Type.__name__ = "Integer32"
_PvxSLAThroughputTestSVlanPriority_Object = MibTableColumn
pvxSLAThroughputTestSVlanPriority = _PvxSLAThroughputTestSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 20),
    _PvxSLAThroughputTestSVlanPriority_Type()
)
pvxSLAThroughputTestSVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestSVlanPriority.setStatus("current")
_PvxSLAThroughputTestCirRateTestResult_Type = CirTestResult
_PvxSLAThroughputTestCirRateTestResult_Object = MibTableColumn
pvxSLAThroughputTestCirRateTestResult = _PvxSLAThroughputTestCirRateTestResult_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 21),
    _PvxSLAThroughputTestCirRateTestResult_Type()
)
pvxSLAThroughputTestCirRateTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestCirRateTestResult.setStatus("current")
_PvxSLAThroughputTestFrameSize1FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize1FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize1FarEndThroughput = _PvxSLAThroughputTestFrameSize1FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 22),
    _PvxSLAThroughputTestFrameSize1FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize1FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize1FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize1NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize1NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize1NearEndThroughput = _PvxSLAThroughputTestFrameSize1NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 23),
    _PvxSLAThroughputTestFrameSize1NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize1NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize1NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize2FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize2FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize2FarEndThroughput = _PvxSLAThroughputTestFrameSize2FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 24),
    _PvxSLAThroughputTestFrameSize2FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize2FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize2FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize2NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize2NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize2NearEndThroughput = _PvxSLAThroughputTestFrameSize2NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 25),
    _PvxSLAThroughputTestFrameSize2NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize2NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize2NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize3FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize3FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize3FarEndThroughput = _PvxSLAThroughputTestFrameSize3FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 26),
    _PvxSLAThroughputTestFrameSize3FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize3FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize3FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize3NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize3NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize3NearEndThroughput = _PvxSLAThroughputTestFrameSize3NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 27),
    _PvxSLAThroughputTestFrameSize3NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize3NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize3NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize4FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize4FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize4FarEndThroughput = _PvxSLAThroughputTestFrameSize4FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 28),
    _PvxSLAThroughputTestFrameSize4FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize4FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize4FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize4NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize4NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize4NearEndThroughput = _PvxSLAThroughputTestFrameSize4NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 29),
    _PvxSLAThroughputTestFrameSize4NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize4NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize4NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize5FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize5FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize5FarEndThroughput = _PvxSLAThroughputTestFrameSize5FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 30),
    _PvxSLAThroughputTestFrameSize5FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize5FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize5FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize5NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize5NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize5NearEndThroughput = _PvxSLAThroughputTestFrameSize5NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 31),
    _PvxSLAThroughputTestFrameSize5NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize5NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize5NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize6FarEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize6FarEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize6FarEndThroughput = _PvxSLAThroughputTestFrameSize6FarEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 32),
    _PvxSLAThroughputTestFrameSize6FarEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize6FarEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize6FarEndThroughput.setStatus("current")
_PvxSLAThroughputTestFrameSize6NearEndThroughput_Type = Unsigned32
_PvxSLAThroughputTestFrameSize6NearEndThroughput_Object = MibTableColumn
pvxSLAThroughputTestFrameSize6NearEndThroughput = _PvxSLAThroughputTestFrameSize6NearEndThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 33),
    _PvxSLAThroughputTestFrameSize6NearEndThroughput_Type()
)
pvxSLAThroughputTestFrameSize6NearEndThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestFrameSize6NearEndThroughput.setStatus("current")
_PvxSLAThroughputTestRowStatus_Type = RowStatus
_PvxSLAThroughputTestRowStatus_Object = MibTableColumn
pvxSLAThroughputTestRowStatus = _PvxSLAThroughputTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 8, 1, 100),
    _PvxSLAThroughputTestRowStatus_Type()
)
pvxSLAThroughputTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAThroughputTestRowStatus.setStatus("current")
_PvxSLAMsmtInitiatorDBTable_Object = MibTable
pvxSLAMsmtInitiatorDBTable = _PvxSLAMsmtInitiatorDBTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9)
)
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBTable.setStatus("current")
_PvxSLAMsmtInitiatorDBEntry_Object = MibTableRow
pvxSLAMsmtInitiatorDBEntry = _PvxSLAMsmtInitiatorDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1)
)
pvxSLAMsmtInitiatorDBEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBESName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtInitiatorDBRMepId"),
)
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBEntry.setStatus("current")


class _PvxSLAMsmtInitiatorDBSwitchIdx_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSLAMsmtInitiatorDBSwitchIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBSwitchIdx_Object = MibTableColumn
pvxSLAMsmtInitiatorDBSwitchIdx = _PvxSLAMsmtInitiatorDBSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 1),
    _PvxSLAMsmtInitiatorDBSwitchIdx_Type()
)
pvxSLAMsmtInitiatorDBSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBSwitchIdx.setStatus("current")


class _PvxSLAMsmtInitiatorDBShelfIdx_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSLAMsmtInitiatorDBShelfIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBShelfIdx_Object = MibTableColumn
pvxSLAMsmtInitiatorDBShelfIdx = _PvxSLAMsmtInitiatorDBShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 2),
    _PvxSLAMsmtInitiatorDBShelfIdx_Type()
)
pvxSLAMsmtInitiatorDBShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBShelfIdx.setStatus("current")


class _PvxSLAMsmtInitiatorDBSlotIdx_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSLAMsmtInitiatorDBSlotIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBSlotIdx_Object = MibTableColumn
pvxSLAMsmtInitiatorDBSlotIdx = _PvxSLAMsmtInitiatorDBSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 3),
    _PvxSLAMsmtInitiatorDBSlotIdx_Type()
)
pvxSLAMsmtInitiatorDBSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBSlotIdx.setStatus("current")
_PvxSLAMsmtInitiatorDBPortTypeIdx_Type = PvxPortType
_PvxSLAMsmtInitiatorDBPortTypeIdx_Object = MibTableColumn
pvxSLAMsmtInitiatorDBPortTypeIdx = _PvxSLAMsmtInitiatorDBPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 4),
    _PvxSLAMsmtInitiatorDBPortTypeIdx_Type()
)
pvxSLAMsmtInitiatorDBPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBPortTypeIdx.setStatus("current")


class _PvxSLAMsmtInitiatorDBPortIdx_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxSLAMsmtInitiatorDBPortIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBPortIdx_Object = MibTableColumn
pvxSLAMsmtInitiatorDBPortIdx = _PvxSLAMsmtInitiatorDBPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 5),
    _PvxSLAMsmtInitiatorDBPortIdx_Type()
)
pvxSLAMsmtInitiatorDBPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBPortIdx.setStatus("current")
_PvxSLAMsmtInitiatorDBESName_Type = DisplayString
_PvxSLAMsmtInitiatorDBESName_Object = MibTableColumn
pvxSLAMsmtInitiatorDBESName = _PvxSLAMsmtInitiatorDBESName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 6),
    _PvxSLAMsmtInitiatorDBESName_Type()
)
pvxSLAMsmtInitiatorDBESName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBESName.setStatus("current")


class _PvxSLAMsmtInitiatorDBRMepId_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBRMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxSLAMsmtInitiatorDBRMepId_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBRMepId_Object = MibTableColumn
pvxSLAMsmtInitiatorDBRMepId = _PvxSLAMsmtInitiatorDBRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 7),
    _PvxSLAMsmtInitiatorDBRMepId_Type()
)
pvxSLAMsmtInitiatorDBRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBRMepId.setStatus("current")
_PvxSLAMsmtInitiatorDBCmdState_Type = PmTestCmdState
_PvxSLAMsmtInitiatorDBCmdState_Object = MibTableColumn
pvxSLAMsmtInitiatorDBCmdState = _PvxSLAMsmtInitiatorDBCmdState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 8),
    _PvxSLAMsmtInitiatorDBCmdState_Type()
)
pvxSLAMsmtInitiatorDBCmdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBCmdState.setStatus("current")


class _PvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority_Type(Integer32):
    """Custom type pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority_Type.__name__ = "Integer32"
_PvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority_Object = MibTableColumn
pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority = _PvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 9),
    _PvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority_Type()
)
pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority.setStatus("current")
_PvxSLAMsmtInitiatorDBRowStatus_Type = RowStatus
_PvxSLAMsmtInitiatorDBRowStatus_Object = MibTableColumn
pvxSLAMsmtInitiatorDBRowStatus = _PvxSLAMsmtInitiatorDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 9, 1, 100),
    _PvxSLAMsmtInitiatorDBRowStatus_Type()
)
pvxSLAMsmtInitiatorDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtInitiatorDBRowStatus.setStatus("current")
_PvxSLAMsmtResponderDBTable_Object = MibTable
pvxSLAMsmtResponderDBTable = _PvxSLAMsmtResponderDBTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10)
)
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBTable.setStatus("current")
_PvxSLAMsmtResponderDBEntry_Object = MibTableRow
pvxSLAMsmtResponderDBEntry = _PvxSLAMsmtResponderDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1)
)
pvxSLAMsmtResponderDBEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBShelfIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBSlotIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBPortTypeIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBPortIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBESName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtResponderDBRMepId"),
)
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBEntry.setStatus("current")


class _PvxSLAMsmtResponderDBSwitchIdx_Type(Integer32):
    """Custom type pvxSLAMsmtResponderDBSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSLAMsmtResponderDBSwitchIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtResponderDBSwitchIdx_Object = MibTableColumn
pvxSLAMsmtResponderDBSwitchIdx = _PvxSLAMsmtResponderDBSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 1),
    _PvxSLAMsmtResponderDBSwitchIdx_Type()
)
pvxSLAMsmtResponderDBSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBSwitchIdx.setStatus("current")


class _PvxSLAMsmtResponderDBShelfIdx_Type(Integer32):
    """Custom type pvxSLAMsmtResponderDBShelfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSLAMsmtResponderDBShelfIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtResponderDBShelfIdx_Object = MibTableColumn
pvxSLAMsmtResponderDBShelfIdx = _PvxSLAMsmtResponderDBShelfIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 2),
    _PvxSLAMsmtResponderDBShelfIdx_Type()
)
pvxSLAMsmtResponderDBShelfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBShelfIdx.setStatus("current")


class _PvxSLAMsmtResponderDBSlotIdx_Type(Integer32):
    """Custom type pvxSLAMsmtResponderDBSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSLAMsmtResponderDBSlotIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtResponderDBSlotIdx_Object = MibTableColumn
pvxSLAMsmtResponderDBSlotIdx = _PvxSLAMsmtResponderDBSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 3),
    _PvxSLAMsmtResponderDBSlotIdx_Type()
)
pvxSLAMsmtResponderDBSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBSlotIdx.setStatus("current")
_PvxSLAMsmtResponderDBPortTypeIdx_Type = PvxPortType
_PvxSLAMsmtResponderDBPortTypeIdx_Object = MibTableColumn
pvxSLAMsmtResponderDBPortTypeIdx = _PvxSLAMsmtResponderDBPortTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 4),
    _PvxSLAMsmtResponderDBPortTypeIdx_Type()
)
pvxSLAMsmtResponderDBPortTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBPortTypeIdx.setStatus("current")


class _PvxSLAMsmtResponderDBPortIdx_Type(Integer32):
    """Custom type pvxSLAMsmtResponderDBPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PvxSLAMsmtResponderDBPortIdx_Type.__name__ = "Integer32"
_PvxSLAMsmtResponderDBPortIdx_Object = MibTableColumn
pvxSLAMsmtResponderDBPortIdx = _PvxSLAMsmtResponderDBPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 5),
    _PvxSLAMsmtResponderDBPortIdx_Type()
)
pvxSLAMsmtResponderDBPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBPortIdx.setStatus("current")
_PvxSLAMsmtResponderDBESName_Type = DisplayString
_PvxSLAMsmtResponderDBESName_Object = MibTableColumn
pvxSLAMsmtResponderDBESName = _PvxSLAMsmtResponderDBESName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 6),
    _PvxSLAMsmtResponderDBESName_Type()
)
pvxSLAMsmtResponderDBESName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBESName.setStatus("current")


class _PvxSLAMsmtResponderDBRMepId_Type(Integer32):
    """Custom type pvxSLAMsmtResponderDBRMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PvxSLAMsmtResponderDBRMepId_Type.__name__ = "Integer32"
_PvxSLAMsmtResponderDBRMepId_Object = MibTableColumn
pvxSLAMsmtResponderDBRMepId = _PvxSLAMsmtResponderDBRMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 7),
    _PvxSLAMsmtResponderDBRMepId_Type()
)
pvxSLAMsmtResponderDBRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBRMepId.setStatus("current")
_PvxSLAMsmtResponderDBRowStatus_Type = RowStatus
_PvxSLAMsmtResponderDBRowStatus_Object = MibTableColumn
pvxSLAMsmtResponderDBRowStatus = _PvxSLAMsmtResponderDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 21, 10, 1, 100),
    _PvxSLAMsmtResponderDBRowStatus_Type()
)
pvxSLAMsmtResponderDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtResponderDBRowStatus.setStatus("current")
_PvxMgmtVLANTable_Object = MibTable
pvxMgmtVLANTable = _PvxMgmtVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22)
)
if mibBuilder.loadTexts:
    pvxMgmtVLANTable.setStatus("current")
_PvxMgmtVLANEntry_Object = MibTableRow
pvxMgmtVLANEntry = _PvxMgmtVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1)
)
pvxMgmtVLANEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMgmtVLANSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxMgmtVLANSrvcName"),
)
if mibBuilder.loadTexts:
    pvxMgmtVLANEntry.setStatus("current")


class _PvxMgmtVLANSwitchIdx_Type(Integer32):
    """Custom type pvxMgmtVLANSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxMgmtVLANSwitchIdx_Type.__name__ = "Integer32"
_PvxMgmtVLANSwitchIdx_Object = MibTableColumn
pvxMgmtVLANSwitchIdx = _PvxMgmtVLANSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 1),
    _PvxMgmtVLANSwitchIdx_Type()
)
pvxMgmtVLANSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMgmtVLANSwitchIdx.setStatus("current")
_PvxMgmtVLANSrvcName_Type = DisplayString
_PvxMgmtVLANSrvcName_Object = MibTableColumn
pvxMgmtVLANSrvcName = _PvxMgmtVLANSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 2),
    _PvxMgmtVLANSrvcName_Type()
)
pvxMgmtVLANSrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxMgmtVLANSrvcName.setStatus("current")
_PvxMgmtVLANBWProfileName_Type = DisplayString
_PvxMgmtVLANBWProfileName_Object = MibTableColumn
pvxMgmtVLANBWProfileName = _PvxMgmtVLANBWProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 3),
    _PvxMgmtVLANBWProfileName_Type()
)
pvxMgmtVLANBWProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANBWProfileName.setStatus("current")


class _PvxMgmtVLANCVLANId_Type(Integer32):
    """Custom type pvxMgmtVLANCVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PvxMgmtVLANCVLANId_Type.__name__ = "Integer32"
_PvxMgmtVLANCVLANId_Object = MibTableColumn
pvxMgmtVLANCVLANId = _PvxMgmtVLANCVLANId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 4),
    _PvxMgmtVLANCVLANId_Type()
)
pvxMgmtVLANCVLANId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANCVLANId.setStatus("current")
_PvxMgmtVLANAddressType_Type = InetAddressType
_PvxMgmtVLANAddressType_Object = MibTableColumn
pvxMgmtVLANAddressType = _PvxMgmtVLANAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 5),
    _PvxMgmtVLANAddressType_Type()
)
pvxMgmtVLANAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANAddressType.setStatus("current")
_PvxMgmtVLANIpAddress_Type = InetAddress
_PvxMgmtVLANIpAddress_Object = MibTableColumn
pvxMgmtVLANIpAddress = _PvxMgmtVLANIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 6),
    _PvxMgmtVLANIpAddress_Type()
)
pvxMgmtVLANIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANIpAddress.setStatus("current")
_PvxMgmtVLANNetMask_Type = InetAddress
_PvxMgmtVLANNetMask_Object = MibTableColumn
pvxMgmtVLANNetMask = _PvxMgmtVLANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 7),
    _PvxMgmtVLANNetMask_Type()
)
pvxMgmtVLANNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANNetMask.setStatus("current")
_PvxMgmtVLANDebugMode_Type = TruthValue
_PvxMgmtVLANDebugMode_Object = MibTableColumn
pvxMgmtVLANDebugMode = _PvxMgmtVLANDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 8),
    _PvxMgmtVLANDebugMode_Type()
)
pvxMgmtVLANDebugMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANDebugMode.setStatus("current")
_PvxMgmtVLANRowStatus_Type = RowStatus
_PvxMgmtVLANRowStatus_Object = MibTableColumn
pvxMgmtVLANRowStatus = _PvxMgmtVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 22, 1, 100),
    _PvxMgmtVLANRowStatus_Type()
)
pvxMgmtVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxMgmtVLANRowStatus.setStatus("current")
_PvxServiceNNITable_Object = MibTable
pvxServiceNNITable = _PvxServiceNNITable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23)
)
if mibBuilder.loadTexts:
    pvxServiceNNITable.setStatus("current")
_PvxServiceNNIEntry_Object = MibTableRow
pvxServiceNNIEntry = _PvxServiceNNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1)
)
pvxServiceNNIEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNISwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNIShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNISlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNIPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNIPortId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSrvcNNISrvcName"),
)
if mibBuilder.loadTexts:
    pvxServiceNNIEntry.setStatus("current")


class _PvxSrvcNNISwitchId_Type(Integer32):
    """Custom type pvxSrvcNNISwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxSrvcNNISwitchId_Type.__name__ = "Integer32"
_PvxSrvcNNISwitchId_Object = MibTableColumn
pvxSrvcNNISwitchId = _PvxSrvcNNISwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 1),
    _PvxSrvcNNISwitchId_Type()
)
pvxSrvcNNISwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNISwitchId.setStatus("current")


class _PvxSrvcNNIShelfId_Type(Integer32):
    """Custom type pvxSrvcNNIShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxSrvcNNIShelfId_Type.__name__ = "Integer32"
_PvxSrvcNNIShelfId_Object = MibTableColumn
pvxSrvcNNIShelfId = _PvxSrvcNNIShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 2),
    _PvxSrvcNNIShelfId_Type()
)
pvxSrvcNNIShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNIShelfId.setStatus("current")


class _PvxSrvcNNISlotId_Type(Integer32):
    """Custom type pvxSrvcNNISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxSrvcNNISlotId_Type.__name__ = "Integer32"
_PvxSrvcNNISlotId_Object = MibTableColumn
pvxSrvcNNISlotId = _PvxSrvcNNISlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 3),
    _PvxSrvcNNISlotId_Type()
)
pvxSrvcNNISlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNISlotId.setStatus("current")
_PvxSrvcNNIPortTypeId_Type = PvxPortType
_PvxSrvcNNIPortTypeId_Object = MibTableColumn
pvxSrvcNNIPortTypeId = _PvxSrvcNNIPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 4),
    _PvxSrvcNNIPortTypeId_Type()
)
pvxSrvcNNIPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNIPortTypeId.setStatus("current")
_PvxSrvcNNIPortId_Type = Integer32
_PvxSrvcNNIPortId_Object = MibTableColumn
pvxSrvcNNIPortId = _PvxSrvcNNIPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 5),
    _PvxSrvcNNIPortId_Type()
)
pvxSrvcNNIPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNIPortId.setStatus("current")


class _PvxSrvcNNISrvcName_Type(DisplayString):
    """Custom type pvxSrvcNNISrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxSrvcNNISrvcName_Type.__name__ = "DisplayString"
_PvxSrvcNNISrvcName_Object = MibTableColumn
pvxSrvcNNISrvcName = _PvxSrvcNNISrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 6),
    _PvxSrvcNNISrvcName_Type()
)
pvxSrvcNNISrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSrvcNNISrvcName.setStatus("current")


class _PvxSrvcNNIIngressBW_Type(DisplayString):
    """Custom type pvxSrvcNNIIngressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcNNIIngressBW_Type.__name__ = "DisplayString"
_PvxSrvcNNIIngressBW_Object = MibTableColumn
pvxSrvcNNIIngressBW = _PvxSrvcNNIIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 8),
    _PvxSrvcNNIIngressBW_Type()
)
pvxSrvcNNIIngressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcNNIIngressBW.setStatus("current")


class _PvxSrvcNNIIngressBWperCos_Type(DisplayString):
    """Custom type pvxSrvcNNIIngressBWperCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcNNIIngressBWperCos_Type.__name__ = "DisplayString"
_PvxSrvcNNIIngressBWperCos_Object = MibTableColumn
pvxSrvcNNIIngressBWperCos = _PvxSrvcNNIIngressBWperCos_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 9),
    _PvxSrvcNNIIngressBWperCos_Type()
)
pvxSrvcNNIIngressBWperCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcNNIIngressBWperCos.setStatus("current")


class _PvxSrvcNNIEgressBW_Type(DisplayString):
    """Custom type pvxSrvcNNIEgressBW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcNNIEgressBW_Type.__name__ = "DisplayString"
_PvxSrvcNNIEgressBW_Object = MibTableColumn
pvxSrvcNNIEgressBW = _PvxSrvcNNIEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 10),
    _PvxSrvcNNIEgressBW_Type()
)
pvxSrvcNNIEgressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcNNIEgressBW.setStatus("current")


class _PvxSrvcNNIEgressBWperCos_Type(DisplayString):
    """Custom type pvxSrvcNNIEgressBWperCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxSrvcNNIEgressBWperCos_Type.__name__ = "DisplayString"
_PvxSrvcNNIEgressBWperCos_Object = MibTableColumn
pvxSrvcNNIEgressBWperCos = _PvxSrvcNNIEgressBWperCos_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 11),
    _PvxSrvcNNIEgressBWperCos_Type()
)
pvxSrvcNNIEgressBWperCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcNNIEgressBWperCos.setStatus("current")
_PvxSrvcNNIRowStatus_Type = RowStatus
_PvxSrvcNNIRowStatus_Object = MibTableColumn
pvxSrvcNNIRowStatus = _PvxSrvcNNIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 23, 1, 100),
    _PvxSrvcNNIRowStatus_Type()
)
pvxSrvcNNIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSrvcNNIRowStatus.setStatus("current")
_PvxERPSServiceNNITable_Object = MibTable
pvxERPSServiceNNITable = _PvxERPSServiceNNITable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24)
)
if mibBuilder.loadTexts:
    pvxERPSServiceNNITable.setStatus("current")
_PvxERPSServiceNNIEntry_Object = MibTableRow
pvxERPSServiceNNIEntry = _PvxERPSServiceNNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1)
)
pvxERPSServiceNNIEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNISwitchId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIShelfId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNISlotId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIPortTypeId"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIPortId"),
)
if mibBuilder.loadTexts:
    pvxERPSServiceNNIEntry.setStatus("current")


class _PvxERPSSrvcNNISwitchId_Type(Integer32):
    """Custom type pvxERPSSrvcNNISwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxERPSSrvcNNISwitchId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNISwitchId_Object = MibTableColumn
pvxERPSSrvcNNISwitchId = _PvxERPSSrvcNNISwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 1),
    _PvxERPSSrvcNNISwitchId_Type()
)
pvxERPSSrvcNNISwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNISwitchId.setStatus("current")


class _PvxERPSSrvcNNIShelfId_Type(Integer32):
    """Custom type pvxERPSSrvcNNIShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(31, 31),
    )


_PvxERPSSrvcNNIShelfId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIShelfId_Object = MibTableColumn
pvxERPSSrvcNNIShelfId = _PvxERPSSrvcNNIShelfId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 2),
    _PvxERPSSrvcNNIShelfId_Type()
)
pvxERPSSrvcNNIShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIShelfId.setStatus("current")


class _PvxERPSSrvcNNISlotId_Type(Integer32):
    """Custom type pvxERPSSrvcNNISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(13, 13),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(17, 17),
        ValueRangeConstraint(19, 19),
    )


_PvxERPSSrvcNNISlotId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNISlotId_Object = MibTableColumn
pvxERPSSrvcNNISlotId = _PvxERPSSrvcNNISlotId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 3),
    _PvxERPSSrvcNNISlotId_Type()
)
pvxERPSSrvcNNISlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNISlotId.setStatus("current")
_PvxERPSSrvcNNIPortTypeId_Type = PvxPortType
_PvxERPSSrvcNNIPortTypeId_Object = MibTableColumn
pvxERPSSrvcNNIPortTypeId = _PvxERPSSrvcNNIPortTypeId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 4),
    _PvxERPSSrvcNNIPortTypeId_Type()
)
pvxERPSSrvcNNIPortTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIPortTypeId.setStatus("current")
_PvxERPSSrvcNNIPortId_Type = Integer32
_PvxERPSSrvcNNIPortId_Object = MibTableColumn
pvxERPSSrvcNNIPortId = _PvxERPSSrvcNNIPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 5),
    _PvxERPSSrvcNNIPortId_Type()
)
pvxERPSSrvcNNIPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIPortId.setStatus("current")


class _PvxERPSSrvcNNIRingProtectLink_Type(Integer32):
    """Custom type pvxERPSSrvcNNIRingProtectLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcNNIRingProtectLink_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIRingProtectLink_Object = MibTableColumn
pvxERPSSrvcNNIRingProtectLink = _PvxERPSSrvcNNIRingProtectLink_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 6),
    _PvxERPSSrvcNNIRingProtectLink_Type()
)
pvxERPSSrvcNNIRingProtectLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIRingProtectLink.setStatus("current")


class _PvxERPSSrvcNNIProtectionSwitch_Type(Integer32):
    """Custom type pvxERPSSrvcNNIProtectionSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcNNIProtectionSwitch_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIProtectionSwitch_Object = MibTableColumn
pvxERPSSrvcNNIProtectionSwitch = _PvxERPSSrvcNNIProtectionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 7),
    _PvxERPSSrvcNNIProtectionSwitch_Type()
)
pvxERPSSrvcNNIProtectionSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIProtectionSwitch.setStatus("current")


class _PvxERPSSrvcNNIRingPortStatus_Type(Integer32):
    """Custom type pvxERPSSrvcNNIRingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_PvxERPSSrvcNNIRingPortStatus_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIRingPortStatus_Object = MibTableColumn
pvxERPSSrvcNNIRingPortStatus = _PvxERPSSrvcNNIRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 8),
    _PvxERPSSrvcNNIRingPortStatus_Type()
)
pvxERPSSrvcNNIRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIRingPortStatus.setStatus("current")


class _PvxERPSSrvcNNISrvcName_Type(DisplayString):
    """Custom type pvxERPSSrvcNNISrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxERPSSrvcNNISrvcName_Type.__name__ = "DisplayString"
_PvxERPSSrvcNNISrvcName_Object = MibTableColumn
pvxERPSSrvcNNISrvcName = _PvxERPSSrvcNNISrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 9),
    _PvxERPSSrvcNNISrvcName_Type()
)
pvxERPSSrvcNNISrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNISrvcName.setStatus("current")


class _PvxERPSSrvcNNIRingPortId_Type(Integer32):
    """Custom type pvxERPSSrvcNNIRingPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringPort1", 1),
          ("ringPort2", 2))
    )


_PvxERPSSrvcNNIRingPortId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIRingPortId_Object = MibTableColumn
pvxERPSSrvcNNIRingPortId = _PvxERPSSrvcNNIRingPortId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 10),
    _PvxERPSSrvcNNIRingPortId_Type()
)
pvxERPSSrvcNNIRingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIRingPortId.setStatus("current")


class _PvxERPSSrvcNNIMEName_Type(DisplayString):
    """Custom type pvxERPSSrvcNNIMEName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_PvxERPSSrvcNNIMEName_Type.__name__ = "DisplayString"
_PvxERPSSrvcNNIMEName_Object = MibTableColumn
pvxERPSSrvcNNIMEName = _PvxERPSSrvcNNIMEName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 11),
    _PvxERPSSrvcNNIMEName_Type()
)
pvxERPSSrvcNNIMEName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIMEName.setStatus("current")


class _PvxERPSSrvcNNIRemoteMepId_Type(Integer32):
    """Custom type pvxERPSSrvcNNIRemoteMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PvxERPSSrvcNNIRemoteMepId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNIRemoteMepId_Object = MibTableColumn
pvxERPSSrvcNNIRemoteMepId = _PvxERPSSrvcNNIRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 12),
    _PvxERPSSrvcNNIRemoteMepId_Type()
)
pvxERPSSrvcNNIRemoteMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIRemoteMepId.setStatus("current")


class _PvxERPSSrvcNNIECFMInfo_Type(DisplayString):
    """Custom type pvxERPSSrvcNNIECFMInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PvxERPSSrvcNNIECFMInfo_Type.__name__ = "DisplayString"
_PvxERPSSrvcNNIECFMInfo_Object = MibTableColumn
pvxERPSSrvcNNIECFMInfo = _PvxERPSSrvcNNIECFMInfo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 13),
    _PvxERPSSrvcNNIECFMInfo_Type()
)
pvxERPSSrvcNNIECFMInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIECFMInfo.setStatus("current")


class _PvxERPSSrvcNNILocalMepId_Type(Integer32):
    """Custom type pvxERPSSrvcNNILocalMepId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PvxERPSSrvcNNILocalMepId_Type.__name__ = "Integer32"
_PvxERPSSrvcNNILocalMepId_Object = MibTableColumn
pvxERPSSrvcNNILocalMepId = _PvxERPSSrvcNNILocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 14),
    _PvxERPSSrvcNNILocalMepId_Type()
)
pvxERPSSrvcNNILocalMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNILocalMepId.setStatus("current")


class _PvxERPSSrvcNNINeighborPort_Type(Integer32):
    """Custom type pvxERPSSrvcNNINeighborPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcNNINeighborPort_Type.__name__ = "Integer32"
_PvxERPSSrvcNNINeighborPort_Object = MibTableColumn
pvxERPSSrvcNNINeighborPort = _PvxERPSSrvcNNINeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 15),
    _PvxERPSSrvcNNINeighborPort_Type()
)
pvxERPSSrvcNNINeighborPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNINeighborPort.setStatus("current")


class _PvxERPSSrvcNNINextNeighborPort_Type(Integer32):
    """Custom type pvxERPSSrvcNNINextNeighborPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcNNINextNeighborPort_Type.__name__ = "Integer32"
_PvxERPSSrvcNNINextNeighborPort_Object = MibTableColumn
pvxERPSSrvcNNINextNeighborPort = _PvxERPSSrvcNNINextNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 16),
    _PvxERPSSrvcNNINextNeighborPort_Type()
)
pvxERPSSrvcNNINextNeighborPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNINextNeighborPort.setStatus("current")


class _PvxERPSSrvcNNIFlushRemoteMEP_Type(TruthValue):
    """Custom type pvxERPSSrvcNNIFlushRemoteMEP based on TruthValue"""


_PvxERPSSrvcNNIFlushRemoteMEP_Object = MibTableColumn
pvxERPSSrvcNNIFlushRemoteMEP = _PvxERPSSrvcNNIFlushRemoteMEP_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 17),
    _PvxERPSSrvcNNIFlushRemoteMEP_Type()
)
pvxERPSSrvcNNIFlushRemoteMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIFlushRemoteMEP.setStatus("current")


class _PvxERPSSrvcNNICcmLinkDetection_Type(Integer32):
    """Custom type pvxERPSSrvcNNICcmLinkDetection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcNNICcmLinkDetection_Type.__name__ = "Integer32"
_PvxERPSSrvcNNICcmLinkDetection_Object = MibTableColumn
pvxERPSSrvcNNICcmLinkDetection = _PvxERPSSrvcNNICcmLinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 24, 1, 18),
    _PvxERPSSrvcNNICcmLinkDetection_Type()
)
pvxERPSSrvcNNICcmLinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcNNICcmLinkDetection.setStatus("current")
_PvxERPSServiceTable_Object = MibTable
pvxERPSServiceTable = _PvxERPSServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25)
)
if mibBuilder.loadTexts:
    pvxERPSServiceTable.setStatus("current")
_PvxERPSServiceEntry_Object = MibTableRow
pvxERPSServiceEntry = _PvxERPSServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1)
)
pvxERPSServiceEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
)
if mibBuilder.loadTexts:
    pvxERPSServiceEntry.setStatus("current")


class _PvxERPSSrvcSwitchIdx_Type(Integer32):
    """Custom type pvxERPSSrvcSwitchIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PvxERPSSrvcSwitchIdx_Type.__name__ = "Integer32"
_PvxERPSSrvcSwitchIdx_Object = MibTableColumn
pvxERPSSrvcSwitchIdx = _PvxERPSSrvcSwitchIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 1),
    _PvxERPSSrvcSwitchIdx_Type()
)
pvxERPSSrvcSwitchIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcSwitchIdx.setStatus("current")


class _PvxERPSSrvcName_Type(DisplayString):
    """Custom type pvxERPSSrvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxERPSSrvcName_Type.__name__ = "DisplayString"
_PvxERPSSrvcName_Object = MibTableColumn
pvxERPSSrvcName = _PvxERPSSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 2),
    _PvxERPSSrvcName_Type()
)
pvxERPSSrvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxERPSSrvcName.setStatus("current")


class _PvxERPSSrvcRevertMode_Type(Integer32):
    """Custom type pvxERPSSrvcRevertMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-revertive", 2),
          ("revertive", 1))
    )


_PvxERPSSrvcRevertMode_Type.__name__ = "Integer32"
_PvxERPSSrvcRevertMode_Object = MibTableColumn
pvxERPSSrvcRevertMode = _PvxERPSSrvcRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 3),
    _PvxERPSSrvcRevertMode_Type()
)
pvxERPSSrvcRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcRevertMode.setStatus("current")


class _PvxERPSSrvcProtectionSwitchMode_Type(Integer32):
    """Custom type pvxERPSSrvcProtectionSwitchMode based on Integer32"""
    defaultValue = 1

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
        *(("clear", 4),
          ("forceSwitch", 2),
          ("manualSwitch", 3),
          ("normalSwitch", 1))
    )


_PvxERPSSrvcProtectionSwitchMode_Type.__name__ = "Integer32"
_PvxERPSSrvcProtectionSwitchMode_Object = MibTableColumn
pvxERPSSrvcProtectionSwitchMode = _PvxERPSSrvcProtectionSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 4),
    _PvxERPSSrvcProtectionSwitchMode_Type()
)
pvxERPSSrvcProtectionSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcProtectionSwitchMode.setStatus("current")


class _PvxERPSSrvcHoldTimer_Type(Unsigned32):
    """Custom type pvxERPSSrvcHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvxERPSSrvcHoldTimer_Type.__name__ = "Unsigned32"
_PvxERPSSrvcHoldTimer_Object = MibTableColumn
pvxERPSSrvcHoldTimer = _PvxERPSSrvcHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 5),
    _PvxERPSSrvcHoldTimer_Type()
)
pvxERPSSrvcHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    pvxERPSSrvcHoldTimer.setUnits("deciseconds")


class _PvxERPSSrvcWaitToRestoreTimer_Type(Unsigned32):
    """Custom type pvxERPSSrvcWaitToRestoreTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(360, 360),
        ValueRangeConstraint(420, 420),
        ValueRangeConstraint(480, 480),
        ValueRangeConstraint(540, 540),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(660, 660),
        ValueRangeConstraint(720, 720),
        ValueRangeConstraint(780, 780),
        ValueRangeConstraint(840, 840),
        ValueRangeConstraint(900, 900),
    )


_PvxERPSSrvcWaitToRestoreTimer_Type.__name__ = "Unsigned32"
_PvxERPSSrvcWaitToRestoreTimer_Object = MibTableColumn
pvxERPSSrvcWaitToRestoreTimer = _PvxERPSSrvcWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 6),
    _PvxERPSSrvcWaitToRestoreTimer_Type()
)
pvxERPSSrvcWaitToRestoreTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcWaitToRestoreTimer.setStatus("current")
if mibBuilder.loadTexts:
    pvxERPSSrvcWaitToRestoreTimer.setUnits("seconds")


class _PvxERPSSrvcGuardTimer_Type(Unsigned32):
    """Custom type pvxERPSSrvcGuardTimer based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PvxERPSSrvcGuardTimer_Type.__name__ = "Unsigned32"
_PvxERPSSrvcGuardTimer_Object = MibTableColumn
pvxERPSSrvcGuardTimer = _PvxERPSSrvcGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 7),
    _PvxERPSSrvcGuardTimer_Type()
)
pvxERPSSrvcGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    pvxERPSSrvcGuardTimer.setUnits("centiseconds")


class _PvxERPSSrvcPeriodicTimer_Type(Unsigned32):
    """Custom type pvxERPSSrvcPeriodicTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_PvxERPSSrvcPeriodicTimer_Type.__name__ = "Unsigned32"
_PvxERPSSrvcPeriodicTimer_Object = MibTableColumn
pvxERPSSrvcPeriodicTimer = _PvxERPSSrvcPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 8),
    _PvxERPSSrvcPeriodicTimer_Type()
)
pvxERPSSrvcPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcPeriodicTimer.setStatus("current")
if mibBuilder.loadTexts:
    pvxERPSSrvcPeriodicTimer.setUnits("seconds")


class _PvxERPSSrvcPropagateTC_Type(Integer32):
    """Custom type pvxERPSSrvcPropagateTC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PvxERPSSrvcPropagateTC_Type.__name__ = "Integer32"
_PvxERPSSrvcPropagateTC_Object = MibTableColumn
pvxERPSSrvcPropagateTC = _PvxERPSSrvcPropagateTC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 9),
    _PvxERPSSrvcPropagateTC_Type()
)
pvxERPSSrvcPropagateTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcPropagateTC.setStatus("current")


class _PvxERPSSrvcNodeType_Type(Integer32):
    """Custom type pvxERPSSrvcNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRplOwner", 2),
          ("rplOwner", 1))
    )


_PvxERPSSrvcNodeType_Type.__name__ = "Integer32"
_PvxERPSSrvcNodeType_Object = MibTableColumn
pvxERPSSrvcNodeType = _PvxERPSSrvcNodeType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 10),
    _PvxERPSSrvcNodeType_Type()
)
pvxERPSSrvcNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNodeType.setStatus("current")


class _PvxERPSSrvcRingMonitoring_Type(Integer32):
    """Custom type pvxERPSSrvcRingMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 1),
          ("local", 2))
    )


_PvxERPSSrvcRingMonitoring_Type.__name__ = "Integer32"
_PvxERPSSrvcRingMonitoring_Object = MibTableColumn
pvxERPSSrvcRingMonitoring = _PvxERPSSrvcRingMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 11),
    _PvxERPSSrvcRingMonitoring_Type()
)
pvxERPSSrvcRingMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcRingMonitoring.setStatus("current")


class _PvxERPSSrvcRingProperty_Type(Integer32):
    """Custom type pvxERPSSrvcRingProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inter-connect", 2),
          ("normal", 1))
    )


_PvxERPSSrvcRingProperty_Type.__name__ = "Integer32"
_PvxERPSSrvcRingProperty_Object = MibTableColumn
pvxERPSSrvcRingProperty = _PvxERPSSrvcRingProperty_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 12),
    _PvxERPSSrvcRingProperty_Type()
)
pvxERPSSrvcRingProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcRingProperty.setStatus("current")


class _PvxERPSSrvcRingSemState_Type(Integer32):
    """Custom type pvxERPSSrvcRingSemState based on Integer32"""
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
        *(("disable", 1),
          ("forcedswitch", 5),
          ("idle", 2),
          ("manualswitch", 4),
          ("pending", 6),
          ("protection", 3))
    )


_PvxERPSSrvcRingSemState_Type.__name__ = "Integer32"
_PvxERPSSrvcRingSemState_Object = MibTableColumn
pvxERPSSrvcRingSemState = _PvxERPSSrvcRingSemState_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 13),
    _PvxERPSSrvcRingSemState_Type()
)
pvxERPSSrvcRingSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcRingSemState.setStatus("current")
_PvxERPSSrvcRingNodeStatus_Type = Integer32
_PvxERPSSrvcRingNodeStatus_Object = MibTableColumn
pvxERPSSrvcRingNodeStatus = _PvxERPSSrvcRingNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 14),
    _PvxERPSSrvcRingNodeStatus_Type()
)
pvxERPSSrvcRingNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcRingNodeStatus.setStatus("current")


class _PvxERPSSrvcNumRingPorts_Type(Integer32):
    """Custom type pvxERPSSrvcNumRingPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PvxERPSSrvcNumRingPorts_Type.__name__ = "Integer32"
_PvxERPSSrvcNumRingPorts_Object = MibTableColumn
pvxERPSSrvcNumRingPorts = _PvxERPSSrvcNumRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 15),
    _PvxERPSSrvcNumRingPorts_Type()
)
pvxERPSSrvcNumRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcNumRingPorts.setStatus("current")
_PvxERPSSrvcSVLAN_Type = PvxVlanId
_PvxERPSSrvcSVLAN_Object = MibTableColumn
pvxERPSSrvcSVLAN = _PvxERPSSrvcSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 16),
    _PvxERPSSrvcSVLAN_Type()
)
pvxERPSSrvcSVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcSVLAN.setStatus("current")
_PvxERPSSrvcVirtualLink_Type = PvxErpsVirtualLinkList
_PvxERPSSrvcVirtualLink_Object = MibTableColumn
pvxERPSSrvcVirtualLink = _PvxERPSSrvcVirtualLink_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 17),
    _PvxERPSSrvcVirtualLink_Type()
)
pvxERPSSrvcVirtualLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcVirtualLink.setStatus("current")


class _PvxERPSSrvcWaitToBlockTimer_Type(Unsigned32):
    """Custom type pvxERPSSrvcWaitToBlockTimer based on Unsigned32"""
    defaultValue = 5500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 864000000),
    )


_PvxERPSSrvcWaitToBlockTimer_Type.__name__ = "Unsigned32"
_PvxERPSSrvcWaitToBlockTimer_Object = MibTableColumn
pvxERPSSrvcWaitToBlockTimer = _PvxERPSSrvcWaitToBlockTimer_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 18),
    _PvxERPSSrvcWaitToBlockTimer_Type()
)
pvxERPSSrvcWaitToBlockTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcWaitToBlockTimer.setStatus("current")
if mibBuilder.loadTexts:
    pvxERPSSrvcWaitToBlockTimer.setUnits("miliseconds")


class _PvxERPSSrvcCompatibleVersion_Type(Integer32):
    """Custom type pvxERPSSrvcCompatibleVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_PvxERPSSrvcCompatibleVersion_Type.__name__ = "Integer32"
_PvxERPSSrvcCompatibleVersion_Object = MibTableColumn
pvxERPSSrvcCompatibleVersion = _PvxERPSSrvcCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 19),
    _PvxERPSSrvcCompatibleVersion_Type()
)
pvxERPSSrvcCompatibleVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcCompatibleVersion.setStatus("current")


class _PvxERPSSrvcMultipleFailure_Type(Integer32):
    """Custom type pvxERPSSrvcMultipleFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("primary", 2))
    )


_PvxERPSSrvcMultipleFailure_Type.__name__ = "Integer32"
_PvxERPSSrvcMultipleFailure_Object = MibTableColumn
pvxERPSSrvcMultipleFailure = _PvxERPSSrvcMultipleFailure_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 20),
    _PvxERPSSrvcMultipleFailure_Type()
)
pvxERPSSrvcMultipleFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcMultipleFailure.setStatus("current")


class _PvxERPSSrvcSubRingWithoutVC_Type(TruthValue):
    """Custom type pvxERPSSrvcSubRingWithoutVC based on TruthValue"""


_PvxERPSSrvcSubRingWithoutVC_Object = MibTableColumn
pvxERPSSrvcSubRingWithoutVC = _PvxERPSSrvcSubRingWithoutVC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 21),
    _PvxERPSSrvcSubRingWithoutVC_Type()
)
pvxERPSSrvcSubRingWithoutVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcSubRingWithoutVC.setStatus("current")


class _PvxERPSSrvcDownMegLevel_Type(Integer32):
    """Custom type pvxERPSSrvcDownMegLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PvxERPSSrvcDownMegLevel_Type.__name__ = "Integer32"
_PvxERPSSrvcDownMegLevel_Object = MibTableColumn
pvxERPSSrvcDownMegLevel = _PvxERPSSrvcDownMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 22),
    _PvxERPSSrvcDownMegLevel_Type()
)
pvxERPSSrvcDownMegLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcDownMegLevel.setStatus("current")


class _PvxERPSSrvcUpMegLevel_Type(Integer32):
    """Custom type pvxERPSSrvcUpMegLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PvxERPSSrvcUpMegLevel_Type.__name__ = "Integer32"
_PvxERPSSrvcUpMegLevel_Object = MibTableColumn
pvxERPSSrvcUpMegLevel = _PvxERPSSrvcUpMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 23),
    _PvxERPSSrvcUpMegLevel_Type()
)
pvxERPSSrvcUpMegLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvxERPSSrvcUpMegLevel.setStatus("current")
_PvxERPSSrvcWTRRemaining_Type = Unsigned32
_PvxERPSSrvcWTRRemaining_Object = MibTableColumn
pvxERPSSrvcWTRRemaining = _PvxERPSSrvcWTRRemaining_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 2, 25, 1, 24),
    _PvxERPSSrvcWTRRemaining_Type()
)
pvxERPSSrvcWTRRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxERPSSrvcWTRRemaining.setStatus("current")
_PvxBridgeProfiles_ObjectIdentity = ObjectIdentity
pvxBridgeProfiles = _PvxBridgeProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3)
)
_PvxBWProfileTable_Object = MibTable
pvxBWProfileTable = _PvxBWProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    pvxBWProfileTable.setStatus("current")
_PvxBWProfileEntry_Object = MibTableRow
pvxBWProfileEntry = _PvxBWProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1)
)
pvxBWProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxBWPIdx"),
)
if mibBuilder.loadTexts:
    pvxBWProfileEntry.setStatus("current")
_PvxBWPIdx_Type = Integer32
_PvxBWPIdx_Object = MibTableColumn
pvxBWPIdx = _PvxBWPIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 1),
    _PvxBWPIdx_Type()
)
pvxBWPIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxBWPIdx.setStatus("current")
_PvxBWPCir_Type = Integer32
_PvxBWPCir_Object = MibTableColumn
pvxBWPCir = _PvxBWPCir_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 2),
    _PvxBWPCir_Type()
)
pvxBWPCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPCir.setStatus("current")
_PvxBWPCbs_Type = Integer32
_PvxBWPCbs_Object = MibTableColumn
pvxBWPCbs = _PvxBWPCbs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 3),
    _PvxBWPCbs_Type()
)
pvxBWPCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPCbs.setStatus("current")
_PvxBWPEir_Type = Integer32
_PvxBWPEir_Object = MibTableColumn
pvxBWPEir = _PvxBWPEir_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 4),
    _PvxBWPEir_Type()
)
pvxBWPEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPEir.setStatus("current")
_PvxBWPEbs_Type = Integer32
_PvxBWPEbs_Object = MibTableColumn
pvxBWPEbs = _PvxBWPEbs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 5),
    _PvxBWPEbs_Type()
)
pvxBWPEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPEbs.setStatus("current")
_PvxBWPCoSQueue_Type = Integer32
_PvxBWPCoSQueue_Object = MibTableColumn
pvxBWPCoSQueue = _PvxBWPCoSQueue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 6),
    _PvxBWPCoSQueue_Type()
)
pvxBWPCoSQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPCoSQueue.setStatus("current")
_PvxBWPRowStatus_Type = RowStatus
_PvxBWPRowStatus_Object = MibTableColumn
pvxBWPRowStatus = _PvxBWPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 1, 1, 100),
    _PvxBWPRowStatus_Type()
)
pvxBWPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWPRowStatus.setStatus("current")
_PvxCoSProfileTable_Object = MibTable
pvxCoSProfileTable = _PvxCoSProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    pvxCoSProfileTable.setStatus("current")
_PvxCoSProfileEntry_Object = MibTableRow
pvxCoSProfileEntry = _PvxCoSProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1)
)
pvxCoSProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxCPIdx"),
)
if mibBuilder.loadTexts:
    pvxCoSProfileEntry.setStatus("current")
_PvxCPIdx_Type = Integer32
_PvxCPIdx_Object = MibTableColumn
pvxCPIdx = _PvxCPIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 1),
    _PvxCPIdx_Type()
)
pvxCPIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxCPIdx.setStatus("current")
_PvxCPMaxBandwidth_Type = Integer32
_PvxCPMaxBandwidth_Object = MibTableColumn
pvxCPMaxBandwidth = _PvxCPMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 2),
    _PvxCPMaxBandwidth_Type()
)
pvxCPMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxCPMaxBandwidth.setStatus("current")
_PvxCPMinBandwidth_Type = Integer32
_PvxCPMinBandwidth_Object = MibTableColumn
pvxCPMinBandwidth = _PvxCPMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 3),
    _PvxCPMinBandwidth_Type()
)
pvxCPMinBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxCPMinBandwidth.setStatus("current")
_PvxCPWeight_Type = Integer32
_PvxCPWeight_Object = MibTableColumn
pvxCPWeight = _PvxCPWeight_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 4),
    _PvxCPWeight_Type()
)
pvxCPWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxCPWeight.setStatus("current")


class _PvxCPQueueAlgo_Type(Integer32):
    """Custom type pvxCPQueueAlgo based on Integer32"""
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
        *(("drr", 4),
          ("drrsp", 6),
          ("rr", 2),
          ("sp", 1),
          ("wrr", 3),
          ("wrrsp", 5))
    )


_PvxCPQueueAlgo_Type.__name__ = "Integer32"
_PvxCPQueueAlgo_Object = MibTableColumn
pvxCPQueueAlgo = _PvxCPQueueAlgo_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 5),
    _PvxCPQueueAlgo_Type()
)
pvxCPQueueAlgo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxCPQueueAlgo.setStatus("current")
_PvxCPRowStatus_Type = RowStatus
_PvxCPRowStatus_Object = MibTableColumn
pvxCPRowStatus = _PvxCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 2, 1, 100),
    _PvxCPRowStatus_Type()
)
pvxCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxCPRowStatus.setStatus("current")
_PvxCtrlFrmProfileTable_ObjectIdentity = ObjectIdentity
pvxCtrlFrmProfileTable = _PvxCtrlFrmProfileTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 3)
)
_PvxFlowMeterProfileTable_Object = MibTable
pvxFlowMeterProfileTable = _PvxFlowMeterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    pvxFlowMeterProfileTable.setStatus("current")
_PvxFlowMeterProfileEntry_Object = MibTableRow
pvxFlowMeterProfileEntry = _PvxFlowMeterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1)
)
pvxFlowMeterProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxFMPIdx"),
)
if mibBuilder.loadTexts:
    pvxFlowMeterProfileEntry.setStatus("current")
_PvxFMPIdx_Type = Integer32
_PvxFMPIdx_Object = MibTableColumn
pvxFMPIdx = _PvxFMPIdx_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 1),
    _PvxFMPIdx_Type()
)
pvxFMPIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxFMPIdx.setStatus("current")
_PvxFMPBWProfileId_Type = Integer32
_PvxFMPBWProfileId_Object = MibTableColumn
pvxFMPBWProfileId = _PvxFMPBWProfileId_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 2),
    _PvxFMPBWProfileId_Type()
)
pvxFMPBWProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMPBWProfileId.setStatus("current")
_PvxFMPColorAware_Type = TruthValue
_PvxFMPColorAware_Object = MibTableColumn
pvxFMPColorAware = _PvxFMPColorAware_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 3),
    _PvxFMPColorAware_Type()
)
pvxFMPColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMPColorAware.setStatus("current")


class _PvxFMPMeterType_Type(Integer32):
    """Custom type pvxFMPMeterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drTCM", 3),
          ("flow", 1),
          ("srTCM", 2))
    )


_PvxFMPMeterType_Type.__name__ = "Integer32"
_PvxFMPMeterType_Object = MibTableColumn
pvxFMPMeterType = _PvxFMPMeterType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 4),
    _PvxFMPMeterType_Type()
)
pvxFMPMeterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMPMeterType.setStatus("current")
_PvxFMPStatsEnabled_Type = ProtocolActionType
_PvxFMPStatsEnabled_Object = MibTableColumn
pvxFMPStatsEnabled = _PvxFMPStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 5),
    _PvxFMPStatsEnabled_Type()
)
pvxFMPStatsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMPStatsEnabled.setStatus("current")
_PvxFMPRowStatus_Type = RowStatus
_PvxFMPRowStatus_Object = MibTableColumn
pvxFMPRowStatus = _PvxFMPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 4, 1, 100),
    _PvxFMPRowStatus_Type()
)
pvxFMPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxFMPRowStatus.setStatus("current")
_PvxTunnMacAddrProfileTable_ObjectIdentity = ObjectIdentity
pvxTunnMacAddrProfileTable = _PvxTunnMacAddrProfileTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 5)
)
_PvxSchedulerProfileTable_Object = MibTable
pvxSchedulerProfileTable = _PvxSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6)
)
if mibBuilder.loadTexts:
    pvxSchedulerProfileTable.setStatus("current")
_PvxSchedulerProfileEntry_Object = MibTableRow
pvxSchedulerProfileEntry = _PvxSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1)
)
pvxSchedulerProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSchedProfName"),
)
if mibBuilder.loadTexts:
    pvxSchedulerProfileEntry.setStatus("current")


class _PvxSchedProfName_Type(DisplayString):
    """Custom type pvxSchedProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxSchedProfName_Type.__name__ = "DisplayString"
_PvxSchedProfName_Object = MibTableColumn
pvxSchedProfName = _PvxSchedProfName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 1),
    _PvxSchedProfName_Type()
)
pvxSchedProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSchedProfName.setStatus("current")


class _PvxSchedProfAlgorithm_Type(Integer32):
    """Custom type pvxSchedProfAlgorithm based on Integer32"""
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
        *(("drr", 4),
          ("rr", 2),
          ("sp", 1),
          ("sp-drr", 6),
          ("sp-wrr", 5),
          ("wrr", 3))
    )


_PvxSchedProfAlgorithm_Type.__name__ = "Integer32"
_PvxSchedProfAlgorithm_Object = MibTableColumn
pvxSchedProfAlgorithm = _PvxSchedProfAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 2),
    _PvxSchedProfAlgorithm_Type()
)
pvxSchedProfAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfAlgorithm.setStatus("current")


class _PvxSchedProfWeightQ0_Type(Integer32):
    """Custom type pvxSchedProfWeightQ0 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ0_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ0_Object = MibTableColumn
pvxSchedProfWeightQ0 = _PvxSchedProfWeightQ0_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 3),
    _PvxSchedProfWeightQ0_Type()
)
pvxSchedProfWeightQ0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ0.setStatus("current")


class _PvxSchedProfWeightQ1_Type(Integer32):
    """Custom type pvxSchedProfWeightQ1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ1_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ1_Object = MibTableColumn
pvxSchedProfWeightQ1 = _PvxSchedProfWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 4),
    _PvxSchedProfWeightQ1_Type()
)
pvxSchedProfWeightQ1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ1.setStatus("current")


class _PvxSchedProfWeightQ2_Type(Integer32):
    """Custom type pvxSchedProfWeightQ2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ2_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ2_Object = MibTableColumn
pvxSchedProfWeightQ2 = _PvxSchedProfWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 5),
    _PvxSchedProfWeightQ2_Type()
)
pvxSchedProfWeightQ2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ2.setStatus("current")


class _PvxSchedProfWeightQ3_Type(Integer32):
    """Custom type pvxSchedProfWeightQ3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ3_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ3_Object = MibTableColumn
pvxSchedProfWeightQ3 = _PvxSchedProfWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 6),
    _PvxSchedProfWeightQ3_Type()
)
pvxSchedProfWeightQ3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ3.setStatus("current")


class _PvxSchedProfWeightQ4_Type(Integer32):
    """Custom type pvxSchedProfWeightQ4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ4_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ4_Object = MibTableColumn
pvxSchedProfWeightQ4 = _PvxSchedProfWeightQ4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 7),
    _PvxSchedProfWeightQ4_Type()
)
pvxSchedProfWeightQ4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ4.setStatus("current")


class _PvxSchedProfWeightQ5_Type(Integer32):
    """Custom type pvxSchedProfWeightQ5 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ5_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ5_Object = MibTableColumn
pvxSchedProfWeightQ5 = _PvxSchedProfWeightQ5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 8),
    _PvxSchedProfWeightQ5_Type()
)
pvxSchedProfWeightQ5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ5.setStatus("current")


class _PvxSchedProfWeightQ6_Type(Integer32):
    """Custom type pvxSchedProfWeightQ6 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ6_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ6_Object = MibTableColumn
pvxSchedProfWeightQ6 = _PvxSchedProfWeightQ6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 9),
    _PvxSchedProfWeightQ6_Type()
)
pvxSchedProfWeightQ6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ6.setStatus("current")


class _PvxSchedProfWeightQ7_Type(Integer32):
    """Custom type pvxSchedProfWeightQ7 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvxSchedProfWeightQ7_Type.__name__ = "Integer32"
_PvxSchedProfWeightQ7_Object = MibTableColumn
pvxSchedProfWeightQ7 = _PvxSchedProfWeightQ7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 10),
    _PvxSchedProfWeightQ7_Type()
)
pvxSchedProfWeightQ7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfWeightQ7.setStatus("current")


class _PvxSchedProfMinBwQ0_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ0 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ0_Object = MibTableColumn
pvxSchedProfMinBwQ0 = _PvxSchedProfMinBwQ0_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 11),
    _PvxSchedProfMinBwQ0_Type()
)
pvxSchedProfMinBwQ0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ0.setStatus("current")


class _PvxSchedProfMaxBwQ0_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ0 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ0_Object = MibTableColumn
pvxSchedProfMaxBwQ0 = _PvxSchedProfMaxBwQ0_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 12),
    _PvxSchedProfMaxBwQ0_Type()
)
pvxSchedProfMaxBwQ0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ0.setStatus("current")


class _PvxSchedProfMinBwQ1_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ1 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ1_Object = MibTableColumn
pvxSchedProfMinBwQ1 = _PvxSchedProfMinBwQ1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 13),
    _PvxSchedProfMinBwQ1_Type()
)
pvxSchedProfMinBwQ1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ1.setStatus("current")


class _PvxSchedProfMaxBwQ1_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ1 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ1_Object = MibTableColumn
pvxSchedProfMaxBwQ1 = _PvxSchedProfMaxBwQ1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 14),
    _PvxSchedProfMaxBwQ1_Type()
)
pvxSchedProfMaxBwQ1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ1.setStatus("current")


class _PvxSchedProfMinBwQ2_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ2 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ2_Object = MibTableColumn
pvxSchedProfMinBwQ2 = _PvxSchedProfMinBwQ2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 15),
    _PvxSchedProfMinBwQ2_Type()
)
pvxSchedProfMinBwQ2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ2.setStatus("current")


class _PvxSchedProfMaxBwQ2_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ2 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ2_Object = MibTableColumn
pvxSchedProfMaxBwQ2 = _PvxSchedProfMaxBwQ2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 16),
    _PvxSchedProfMaxBwQ2_Type()
)
pvxSchedProfMaxBwQ2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ2.setStatus("current")


class _PvxSchedProfMinBwQ3_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ3 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ3_Object = MibTableColumn
pvxSchedProfMinBwQ3 = _PvxSchedProfMinBwQ3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 17),
    _PvxSchedProfMinBwQ3_Type()
)
pvxSchedProfMinBwQ3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ3.setStatus("current")


class _PvxSchedProfMaxBwQ3_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ3 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ3_Object = MibTableColumn
pvxSchedProfMaxBwQ3 = _PvxSchedProfMaxBwQ3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 18),
    _PvxSchedProfMaxBwQ3_Type()
)
pvxSchedProfMaxBwQ3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ3.setStatus("current")


class _PvxSchedProfMinBwQ4_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ4 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ4_Object = MibTableColumn
pvxSchedProfMinBwQ4 = _PvxSchedProfMinBwQ4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 19),
    _PvxSchedProfMinBwQ4_Type()
)
pvxSchedProfMinBwQ4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ4.setStatus("current")


class _PvxSchedProfMaxBwQ4_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ4 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ4_Object = MibTableColumn
pvxSchedProfMaxBwQ4 = _PvxSchedProfMaxBwQ4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 20),
    _PvxSchedProfMaxBwQ4_Type()
)
pvxSchedProfMaxBwQ4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ4.setStatus("current")


class _PvxSchedProfMinBwQ5_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ5 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ5_Object = MibTableColumn
pvxSchedProfMinBwQ5 = _PvxSchedProfMinBwQ5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 21),
    _PvxSchedProfMinBwQ5_Type()
)
pvxSchedProfMinBwQ5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ5.setStatus("current")


class _PvxSchedProfMaxBwQ5_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ5 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ5_Object = MibTableColumn
pvxSchedProfMaxBwQ5 = _PvxSchedProfMaxBwQ5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 22),
    _PvxSchedProfMaxBwQ5_Type()
)
pvxSchedProfMaxBwQ5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ5.setStatus("current")


class _PvxSchedProfMinBwQ6_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ6 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ6_Object = MibTableColumn
pvxSchedProfMinBwQ6 = _PvxSchedProfMinBwQ6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 23),
    _PvxSchedProfMinBwQ6_Type()
)
pvxSchedProfMinBwQ6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ6.setStatus("current")


class _PvxSchedProfMaxBwQ6_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ6 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ6_Object = MibTableColumn
pvxSchedProfMaxBwQ6 = _PvxSchedProfMaxBwQ6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 24),
    _PvxSchedProfMaxBwQ6_Type()
)
pvxSchedProfMaxBwQ6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ6.setStatus("current")


class _PvxSchedProfMinBwQ7_Type(Integer32):
    """Custom type pvxSchedProfMinBwQ7 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMinBwQ7_Object = MibTableColumn
pvxSchedProfMinBwQ7 = _PvxSchedProfMinBwQ7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 25),
    _PvxSchedProfMinBwQ7_Type()
)
pvxSchedProfMinBwQ7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMinBwQ7.setStatus("current")


class _PvxSchedProfMaxBwQ7_Type(Integer32):
    """Custom type pvxSchedProfMaxBwQ7 based on Integer32"""
    defaultValue = 0


_PvxSchedProfMaxBwQ7_Object = MibTableColumn
pvxSchedProfMaxBwQ7 = _PvxSchedProfMaxBwQ7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 26),
    _PvxSchedProfMaxBwQ7_Type()
)
pvxSchedProfMaxBwQ7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMaxBwQ7.setStatus("current")


class _PvxSchedProfMTUQuanta_Type(Integer32):
    """Custom type pvxSchedProfMTUQuanta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byte16k", 2),
          ("byte2k", 1))
    )


_PvxSchedProfMTUQuanta_Type.__name__ = "Integer32"
_PvxSchedProfMTUQuanta_Object = MibTableColumn
pvxSchedProfMTUQuanta = _PvxSchedProfMTUQuanta_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 27),
    _PvxSchedProfMTUQuanta_Type()
)
pvxSchedProfMTUQuanta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfMTUQuanta.setStatus("current")
_PvxSchedProfRowStatus_Type = RowStatus
_PvxSchedProfRowStatus_Object = MibTableColumn
pvxSchedProfRowStatus = _PvxSchedProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 6, 1, 100),
    _PvxSchedProfRowStatus_Type()
)
pvxSchedProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSchedProfRowStatus.setStatus("current")
_PvxPriorityTCMapTable_Object = MibTable
pvxPriorityTCMapTable = _PvxPriorityTCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7)
)
if mibBuilder.loadTexts:
    pvxPriorityTCMapTable.setStatus("current")
_PvxPriorityTCMapEntry_Object = MibTableRow
pvxPriorityTCMapEntry = _PvxPriorityTCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1)
)
pvxPriorityTCMapEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxPriorityTCMapName"),
)
if mibBuilder.loadTexts:
    pvxPriorityTCMapEntry.setStatus("current")


class _PvxPriorityTCMapName_Type(DisplayString):
    """Custom type pvxPriorityTCMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxPriorityTCMapName_Type.__name__ = "DisplayString"
_PvxPriorityTCMapName_Object = MibTableColumn
pvxPriorityTCMapName = _PvxPriorityTCMapName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 1),
    _PvxPriorityTCMapName_Type()
)
pvxPriorityTCMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxPriorityTCMapName.setStatus("current")


class _PvxPriority7TrafficClass_Type(Integer32):
    """Custom type pvxPriority7TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority7TrafficClass_Type.__name__ = "Integer32"
_PvxPriority7TrafficClass_Object = MibTableColumn
pvxPriority7TrafficClass = _PvxPriority7TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 2),
    _PvxPriority7TrafficClass_Type()
)
pvxPriority7TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority7TrafficClass.setStatus("current")


class _PvxPriority6TrafficClass_Type(Integer32):
    """Custom type pvxPriority6TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority6TrafficClass_Type.__name__ = "Integer32"
_PvxPriority6TrafficClass_Object = MibTableColumn
pvxPriority6TrafficClass = _PvxPriority6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 3),
    _PvxPriority6TrafficClass_Type()
)
pvxPriority6TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority6TrafficClass.setStatus("current")


class _PvxPriority5TrafficClass_Type(Integer32):
    """Custom type pvxPriority5TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority5TrafficClass_Type.__name__ = "Integer32"
_PvxPriority5TrafficClass_Object = MibTableColumn
pvxPriority5TrafficClass = _PvxPriority5TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 4),
    _PvxPriority5TrafficClass_Type()
)
pvxPriority5TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority5TrafficClass.setStatus("current")


class _PvxPriority4TrafficClass_Type(Integer32):
    """Custom type pvxPriority4TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority4TrafficClass_Type.__name__ = "Integer32"
_PvxPriority4TrafficClass_Object = MibTableColumn
pvxPriority4TrafficClass = _PvxPriority4TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 5),
    _PvxPriority4TrafficClass_Type()
)
pvxPriority4TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority4TrafficClass.setStatus("current")


class _PvxPriority3TrafficClass_Type(Integer32):
    """Custom type pvxPriority3TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority3TrafficClass_Type.__name__ = "Integer32"
_PvxPriority3TrafficClass_Object = MibTableColumn
pvxPriority3TrafficClass = _PvxPriority3TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 6),
    _PvxPriority3TrafficClass_Type()
)
pvxPriority3TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority3TrafficClass.setStatus("current")


class _PvxPriority2TrafficClass_Type(Integer32):
    """Custom type pvxPriority2TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority2TrafficClass_Type.__name__ = "Integer32"
_PvxPriority2TrafficClass_Object = MibTableColumn
pvxPriority2TrafficClass = _PvxPriority2TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 7),
    _PvxPriority2TrafficClass_Type()
)
pvxPriority2TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority2TrafficClass.setStatus("current")


class _PvxPriority1TrafficClass_Type(Integer32):
    """Custom type pvxPriority1TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority1TrafficClass_Type.__name__ = "Integer32"
_PvxPriority1TrafficClass_Object = MibTableColumn
pvxPriority1TrafficClass = _PvxPriority1TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 8),
    _PvxPriority1TrafficClass_Type()
)
pvxPriority1TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority1TrafficClass.setStatus("current")


class _PvxPriority0TrafficClass_Type(Integer32):
    """Custom type pvxPriority0TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPriority0TrafficClass_Type.__name__ = "Integer32"
_PvxPriority0TrafficClass_Object = MibTableColumn
pvxPriority0TrafficClass = _PvxPriority0TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 9),
    _PvxPriority0TrafficClass_Type()
)
pvxPriority0TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriority0TrafficClass.setStatus("current")
_PvxPriorityTCMapRowStatus_Type = RowStatus
_PvxPriorityTCMapRowStatus_Object = MibTableColumn
pvxPriorityTCMapRowStatus = _PvxPriorityTCMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 7, 1, 100),
    _PvxPriorityTCMapRowStatus_Type()
)
pvxPriorityTCMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPriorityTCMapRowStatus.setStatus("current")
_PvxPCPEncDecProfileTable_Object = MibTable
pvxPCPEncDecProfileTable = _PvxPCPEncDecProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8)
)
if mibBuilder.loadTexts:
    pvxPCPEncDecProfileTable.setStatus("current")
_PvxPCPEncDecProfEntry_Object = MibTableRow
pvxPCPEncDecProfEntry = _PvxPCPEncDecProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1)
)
pvxPCPEncDecProfEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxPCPEncDecProfileName"),
)
if mibBuilder.loadTexts:
    pvxPCPEncDecProfEntry.setStatus("current")


class _PvxPCPEncDecProfileName_Type(DisplayString):
    """Custom type pvxPCPEncDecProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxPCPEncDecProfileName_Type.__name__ = "DisplayString"
_PvxPCPEncDecProfileName_Object = MibTableColumn
pvxPCPEncDecProfileName = _PvxPCPEncDecProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 1),
    _PvxPCPEncDecProfileName_Type()
)
pvxPCPEncDecProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxPCPEncDecProfileName.setStatus("current")


class _PvxPCPEncDecSelectRow_Type(Integer32):
    """Custom type pvxPCPEncDecSelectRow based on Integer32"""
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
        *(("row-5P3D", 4),
          ("row-6P2D", 3),
          ("row-7P1D", 2),
          ("row-8P0D", 1))
    )


_PvxPCPEncDecSelectRow_Type.__name__ = "Integer32"
_PvxPCPEncDecSelectRow_Object = MibTableColumn
pvxPCPEncDecSelectRow = _PvxPCPEncDecSelectRow_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 2),
    _PvxPCPEncDecSelectRow_Type()
)
pvxPCPEncDecSelectRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncDecSelectRow.setStatus("current")


class _PvxPCPEncPriority7_Type(Integer32):
    """Custom type pvxPCPEncPriority7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority7_Type.__name__ = "Integer32"
_PvxPCPEncPriority7_Object = MibTableColumn
pvxPCPEncPriority7 = _PvxPCPEncPriority7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 3),
    _PvxPCPEncPriority7_Type()
)
pvxPCPEncPriority7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority7.setStatus("current")


class _PvxPCPEncPriority7DE_Type(Integer32):
    """Custom type pvxPCPEncPriority7DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority7DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority7DE_Object = MibTableColumn
pvxPCPEncPriority7DE = _PvxPCPEncPriority7DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 4),
    _PvxPCPEncPriority7DE_Type()
)
pvxPCPEncPriority7DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority7DE.setStatus("current")


class _PvxPCPEncPriority6_Type(Integer32):
    """Custom type pvxPCPEncPriority6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority6_Type.__name__ = "Integer32"
_PvxPCPEncPriority6_Object = MibTableColumn
pvxPCPEncPriority6 = _PvxPCPEncPriority6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 5),
    _PvxPCPEncPriority6_Type()
)
pvxPCPEncPriority6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority6.setStatus("current")


class _PvxPCPEncPriority6DE_Type(Integer32):
    """Custom type pvxPCPEncPriority6DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority6DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority6DE_Object = MibTableColumn
pvxPCPEncPriority6DE = _PvxPCPEncPriority6DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 6),
    _PvxPCPEncPriority6DE_Type()
)
pvxPCPEncPriority6DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority6DE.setStatus("current")


class _PvxPCPEncPriority5_Type(Integer32):
    """Custom type pvxPCPEncPriority5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority5_Type.__name__ = "Integer32"
_PvxPCPEncPriority5_Object = MibTableColumn
pvxPCPEncPriority5 = _PvxPCPEncPriority5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 7),
    _PvxPCPEncPriority5_Type()
)
pvxPCPEncPriority5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority5.setStatus("current")


class _PvxPCPEncPriority5DE_Type(Integer32):
    """Custom type pvxPCPEncPriority5DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority5DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority5DE_Object = MibTableColumn
pvxPCPEncPriority5DE = _PvxPCPEncPriority5DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 8),
    _PvxPCPEncPriority5DE_Type()
)
pvxPCPEncPriority5DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority5DE.setStatus("current")


class _PvxPCPEncPriority4_Type(Integer32):
    """Custom type pvxPCPEncPriority4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority4_Type.__name__ = "Integer32"
_PvxPCPEncPriority4_Object = MibTableColumn
pvxPCPEncPriority4 = _PvxPCPEncPriority4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 9),
    _PvxPCPEncPriority4_Type()
)
pvxPCPEncPriority4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority4.setStatus("current")


class _PvxPCPEncPriority4DE_Type(Integer32):
    """Custom type pvxPCPEncPriority4DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority4DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority4DE_Object = MibTableColumn
pvxPCPEncPriority4DE = _PvxPCPEncPriority4DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 10),
    _PvxPCPEncPriority4DE_Type()
)
pvxPCPEncPriority4DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority4DE.setStatus("current")


class _PvxPCPEncPriority3_Type(Integer32):
    """Custom type pvxPCPEncPriority3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority3_Type.__name__ = "Integer32"
_PvxPCPEncPriority3_Object = MibTableColumn
pvxPCPEncPriority3 = _PvxPCPEncPriority3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 11),
    _PvxPCPEncPriority3_Type()
)
pvxPCPEncPriority3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority3.setStatus("current")


class _PvxPCPEncPriority3DE_Type(Integer32):
    """Custom type pvxPCPEncPriority3DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority3DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority3DE_Object = MibTableColumn
pvxPCPEncPriority3DE = _PvxPCPEncPriority3DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 12),
    _PvxPCPEncPriority3DE_Type()
)
pvxPCPEncPriority3DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority3DE.setStatus("current")


class _PvxPCPEncPriority2_Type(Integer32):
    """Custom type pvxPCPEncPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority2_Type.__name__ = "Integer32"
_PvxPCPEncPriority2_Object = MibTableColumn
pvxPCPEncPriority2 = _PvxPCPEncPriority2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 13),
    _PvxPCPEncPriority2_Type()
)
pvxPCPEncPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority2.setStatus("current")


class _PvxPCPEncPriority2DE_Type(Integer32):
    """Custom type pvxPCPEncPriority2DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority2DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority2DE_Object = MibTableColumn
pvxPCPEncPriority2DE = _PvxPCPEncPriority2DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 14),
    _PvxPCPEncPriority2DE_Type()
)
pvxPCPEncPriority2DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority2DE.setStatus("current")


class _PvxPCPEncPriority1_Type(Integer32):
    """Custom type pvxPCPEncPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority1_Type.__name__ = "Integer32"
_PvxPCPEncPriority1_Object = MibTableColumn
pvxPCPEncPriority1 = _PvxPCPEncPriority1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 15),
    _PvxPCPEncPriority1_Type()
)
pvxPCPEncPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority1.setStatus("current")


class _PvxPCPEncPriority1DE_Type(Integer32):
    """Custom type pvxPCPEncPriority1DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority1DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority1DE_Object = MibTableColumn
pvxPCPEncPriority1DE = _PvxPCPEncPriority1DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 16),
    _PvxPCPEncPriority1DE_Type()
)
pvxPCPEncPriority1DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority1DE.setStatus("current")


class _PvxPCPEncPriority0_Type(Integer32):
    """Custom type pvxPCPEncPriority0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority0_Type.__name__ = "Integer32"
_PvxPCPEncPriority0_Object = MibTableColumn
pvxPCPEncPriority0 = _PvxPCPEncPriority0_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 17),
    _PvxPCPEncPriority0_Type()
)
pvxPCPEncPriority0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority0.setStatus("current")


class _PvxPCPEncPriority0DE_Type(Integer32):
    """Custom type pvxPCPEncPriority0DE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxPCPEncPriority0DE_Type.__name__ = "Integer32"
_PvxPCPEncPriority0DE_Object = MibTableColumn
pvxPCPEncPriority0DE = _PvxPCPEncPriority0DE_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 18),
    _PvxPCPEncPriority0DE_Type()
)
pvxPCPEncPriority0DE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncPriority0DE.setStatus("current")
_PvxPCPDecPriority7_Type = PvxPCPDecodingList
_PvxPCPDecPriority7_Object = MibTableColumn
pvxPCPDecPriority7 = _PvxPCPDecPriority7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 19),
    _PvxPCPDecPriority7_Type()
)
pvxPCPDecPriority7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority7.setStatus("current")
_PvxPCPDecPriority6_Type = PvxPCPDecodingList
_PvxPCPDecPriority6_Object = MibTableColumn
pvxPCPDecPriority6 = _PvxPCPDecPriority6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 20),
    _PvxPCPDecPriority6_Type()
)
pvxPCPDecPriority6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority6.setStatus("current")
_PvxPCPDecPriority5_Type = PvxPCPDecodingList
_PvxPCPDecPriority5_Object = MibTableColumn
pvxPCPDecPriority5 = _PvxPCPDecPriority5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 21),
    _PvxPCPDecPriority5_Type()
)
pvxPCPDecPriority5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority5.setStatus("current")
_PvxPCPDecPriority4_Type = PvxPCPDecodingList
_PvxPCPDecPriority4_Object = MibTableColumn
pvxPCPDecPriority4 = _PvxPCPDecPriority4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 22),
    _PvxPCPDecPriority4_Type()
)
pvxPCPDecPriority4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority4.setStatus("current")
_PvxPCPDecPriority3_Type = PvxPCPDecodingList
_PvxPCPDecPriority3_Object = MibTableColumn
pvxPCPDecPriority3 = _PvxPCPDecPriority3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 23),
    _PvxPCPDecPriority3_Type()
)
pvxPCPDecPriority3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority3.setStatus("current")
_PvxPCPDecPriority2_Type = PvxPCPDecodingList
_PvxPCPDecPriority2_Object = MibTableColumn
pvxPCPDecPriority2 = _PvxPCPDecPriority2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 24),
    _PvxPCPDecPriority2_Type()
)
pvxPCPDecPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority2.setStatus("current")
_PvxPCPDecPriority1_Type = PvxPCPDecodingList
_PvxPCPDecPriority1_Object = MibTableColumn
pvxPCPDecPriority1 = _PvxPCPDecPriority1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 25),
    _PvxPCPDecPriority1_Type()
)
pvxPCPDecPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority1.setStatus("current")
_PvxPCPDecPriority0_Type = PvxPCPDecodingList
_PvxPCPDecPriority0_Object = MibTableColumn
pvxPCPDecPriority0 = _PvxPCPDecPriority0_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 26),
    _PvxPCPDecPriority0_Type()
)
pvxPCPDecPriority0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPDecPriority0.setStatus("current")
_PvxPCPEncDecRowStatus_Type = RowStatus
_PvxPCPEncDecRowStatus_Object = MibTableColumn
pvxPCPEncDecRowStatus = _PvxPCPEncDecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 8, 1, 100),
    _PvxPCPEncDecRowStatus_Type()
)
pvxPCPEncDecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPCPEncDecRowStatus.setStatus("current")
_PvxDscpPHBProfileTable_Object = MibTable
pvxDscpPHBProfileTable = _PvxDscpPHBProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9)
)
if mibBuilder.loadTexts:
    pvxDscpPHBProfileTable.setStatus("current")
_PvxDscpPHBProfileEntry_Object = MibTableRow
pvxDscpPHBProfileEntry = _PvxDscpPHBProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1)
)
pvxDscpPHBProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxDscpPHBProfileName"),
)
if mibBuilder.loadTexts:
    pvxDscpPHBProfileEntry.setStatus("current")


class _PvxDscpPHBProfileName_Type(DisplayString):
    """Custom type pvxDscpPHBProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxDscpPHBProfileName_Type.__name__ = "DisplayString"
_PvxDscpPHBProfileName_Object = MibTableColumn
pvxDscpPHBProfileName = _PvxDscpPHBProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 1),
    _PvxDscpPHBProfileName_Type()
)
pvxDscpPHBProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxDscpPHBProfileName.setStatus("current")


class _PvxDscpClassSelector7_Type(Integer32):
    """Custom type pvxDscpClassSelector7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector7_Type.__name__ = "Integer32"
_PvxDscpClassSelector7_Object = MibTableColumn
pvxDscpClassSelector7 = _PvxDscpClassSelector7_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 2),
    _PvxDscpClassSelector7_Type()
)
pvxDscpClassSelector7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector7.setStatus("current")


class _PvxDscpClassSelector6_Type(Integer32):
    """Custom type pvxDscpClassSelector6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector6_Type.__name__ = "Integer32"
_PvxDscpClassSelector6_Object = MibTableColumn
pvxDscpClassSelector6 = _PvxDscpClassSelector6_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 3),
    _PvxDscpClassSelector6_Type()
)
pvxDscpClassSelector6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector6.setStatus("current")


class _PvxDscpClassSelector5_Type(Integer32):
    """Custom type pvxDscpClassSelector5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector5_Type.__name__ = "Integer32"
_PvxDscpClassSelector5_Object = MibTableColumn
pvxDscpClassSelector5 = _PvxDscpClassSelector5_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 4),
    _PvxDscpClassSelector5_Type()
)
pvxDscpClassSelector5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector5.setStatus("current")


class _PvxDscpClassSelector4_Type(Integer32):
    """Custom type pvxDscpClassSelector4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector4_Type.__name__ = "Integer32"
_PvxDscpClassSelector4_Object = MibTableColumn
pvxDscpClassSelector4 = _PvxDscpClassSelector4_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 5),
    _PvxDscpClassSelector4_Type()
)
pvxDscpClassSelector4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector4.setStatus("current")


class _PvxDscpClassSelector3_Type(Integer32):
    """Custom type pvxDscpClassSelector3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector3_Type.__name__ = "Integer32"
_PvxDscpClassSelector3_Object = MibTableColumn
pvxDscpClassSelector3 = _PvxDscpClassSelector3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 6),
    _PvxDscpClassSelector3_Type()
)
pvxDscpClassSelector3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector3.setStatus("current")


class _PvxDscpClassSelector2_Type(Integer32):
    """Custom type pvxDscpClassSelector2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector2_Type.__name__ = "Integer32"
_PvxDscpClassSelector2_Object = MibTableColumn
pvxDscpClassSelector2 = _PvxDscpClassSelector2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 7),
    _PvxDscpClassSelector2_Type()
)
pvxDscpClassSelector2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector2.setStatus("current")


class _PvxDscpClassSelector1_Type(Integer32):
    """Custom type pvxDscpClassSelector1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassSelector1_Type.__name__ = "Integer32"
_PvxDscpClassSelector1_Object = MibTableColumn
pvxDscpClassSelector1 = _PvxDscpClassSelector1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 8),
    _PvxDscpClassSelector1_Type()
)
pvxDscpClassSelector1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassSelector1.setStatus("current")


class _PvxDscpClassBestEffort_Type(Integer32):
    """Custom type pvxDscpClassBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpClassBestEffort_Type.__name__ = "Integer32"
_PvxDscpClassBestEffort_Object = MibTableColumn
pvxDscpClassBestEffort = _PvxDscpClassBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 9),
    _PvxDscpClassBestEffort_Type()
)
pvxDscpClassBestEffort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpClassBestEffort.setStatus("current")


class _PvxDscpAssuredFwd1y_Type(Integer32):
    """Custom type pvxDscpAssuredFwd1y based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpAssuredFwd1y_Type.__name__ = "Integer32"
_PvxDscpAssuredFwd1y_Object = MibTableColumn
pvxDscpAssuredFwd1y = _PvxDscpAssuredFwd1y_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 10),
    _PvxDscpAssuredFwd1y_Type()
)
pvxDscpAssuredFwd1y.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpAssuredFwd1y.setStatus("current")


class _PvxDscpAssuredFwd2y_Type(Integer32):
    """Custom type pvxDscpAssuredFwd2y based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpAssuredFwd2y_Type.__name__ = "Integer32"
_PvxDscpAssuredFwd2y_Object = MibTableColumn
pvxDscpAssuredFwd2y = _PvxDscpAssuredFwd2y_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 11),
    _PvxDscpAssuredFwd2y_Type()
)
pvxDscpAssuredFwd2y.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpAssuredFwd2y.setStatus("current")


class _PvxDscpAssuredFwd3y_Type(Integer32):
    """Custom type pvxDscpAssuredFwd3y based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpAssuredFwd3y_Type.__name__ = "Integer32"
_PvxDscpAssuredFwd3y_Object = MibTableColumn
pvxDscpAssuredFwd3y = _PvxDscpAssuredFwd3y_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 12),
    _PvxDscpAssuredFwd3y_Type()
)
pvxDscpAssuredFwd3y.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpAssuredFwd3y.setStatus("current")


class _PvxDscpAssuredFwd4y_Type(Integer32):
    """Custom type pvxDscpAssuredFwd4y based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpAssuredFwd4y_Type.__name__ = "Integer32"
_PvxDscpAssuredFwd4y_Object = MibTableColumn
pvxDscpAssuredFwd4y = _PvxDscpAssuredFwd4y_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 13),
    _PvxDscpAssuredFwd4y_Type()
)
pvxDscpAssuredFwd4y.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpAssuredFwd4y.setStatus("current")


class _PvxDscpExpeditedFwd_Type(Integer32):
    """Custom type pvxDscpExpeditedFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvxDscpExpeditedFwd_Type.__name__ = "Integer32"
_PvxDscpExpeditedFwd_Object = MibTableColumn
pvxDscpExpeditedFwd = _PvxDscpExpeditedFwd_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 14),
    _PvxDscpExpeditedFwd_Type()
)
pvxDscpExpeditedFwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpExpeditedFwd.setStatus("current")
_PvxDscpPHBProfileRowStatus_Type = RowStatus
_PvxDscpPHBProfileRowStatus_Object = MibTableColumn
pvxDscpPHBProfileRowStatus = _PvxDscpPHBProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 9, 1, 100),
    _PvxDscpPHBProfileRowStatus_Type()
)
pvxDscpPHBProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxDscpPHBProfileRowStatus.setStatus("current")
_PvxBandwidthProfileTable_Object = MibTable
pvxBandwidthProfileTable = _PvxBandwidthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    pvxBandwidthProfileTable.setStatus("current")
_PvxBandwidthProfileEntry_Object = MibTableRow
pvxBandwidthProfileEntry = _PvxBandwidthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1)
)
pvxBandwidthProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxBandwidthProfileName"),
)
if mibBuilder.loadTexts:
    pvxBandwidthProfileEntry.setStatus("current")


class _PvxBandwidthProfileName_Type(DisplayString):
    """Custom type pvxBandwidthProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxBandwidthProfileName_Type.__name__ = "DisplayString"
_PvxBandwidthProfileName_Object = MibTableColumn
pvxBandwidthProfileName = _PvxBandwidthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 1),
    _PvxBandwidthProfileName_Type()
)
pvxBandwidthProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxBandwidthProfileName.setStatus("current")


class _PvxBWCnfrmActionChangeDscp_Type(Integer32):
    """Custom type pvxBWCnfrmActionChangeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PvxBWCnfrmActionChangeDscp_Type.__name__ = "Integer32"
_PvxBWCnfrmActionChangeDscp_Object = MibTableColumn
pvxBWCnfrmActionChangeDscp = _PvxBWCnfrmActionChangeDscp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 2),
    _PvxBWCnfrmActionChangeDscp_Type()
)
pvxBWCnfrmActionChangeDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWCnfrmActionChangeDscp.setStatus("current")


class _PvxBWCnfrmActionChangeTOSFrmPri_Type(Integer32):
    """Custom type pvxBWCnfrmActionChangeTOSFrmPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("change", 1),
          ("doNotChange", 2),
          ("notUsed", 3))
    )


_PvxBWCnfrmActionChangeTOSFrmPri_Type.__name__ = "Integer32"
_PvxBWCnfrmActionChangeTOSFrmPri_Object = MibTableColumn
pvxBWCnfrmActionChangeTOSFrmPri = _PvxBWCnfrmActionChangeTOSFrmPri_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 3),
    _PvxBWCnfrmActionChangeTOSFrmPri_Type()
)
pvxBWCnfrmActionChangeTOSFrmPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWCnfrmActionChangeTOSFrmPri.setStatus("current")


class _PvxBWExceedActionChangeDscp_Type(Integer32):
    """Custom type pvxBWExceedActionChangeDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PvxBWExceedActionChangeDscp_Type.__name__ = "Integer32"
_PvxBWExceedActionChangeDscp_Object = MibTableColumn
pvxBWExceedActionChangeDscp = _PvxBWExceedActionChangeDscp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 8),
    _PvxBWExceedActionChangeDscp_Type()
)
pvxBWExceedActionChangeDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWExceedActionChangeDscp.setStatus("current")
_PvxBWMeterColorAware_Type = PvxQoSColorMode
_PvxBWMeterColorAware_Object = MibTableColumn
pvxBWMeterColorAware = _PvxBWMeterColorAware_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 13),
    _PvxBWMeterColorAware_Type()
)
pvxBWMeterColorAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterColorAware.setStatus("current")


class _PvxBWMeterMode_Type(Integer32):
    """Custom type pvxBWMeterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 3),
          ("srTCM", 1),
          ("trTCM", 2))
    )


_PvxBWMeterMode_Type.__name__ = "Integer32"
_PvxBWMeterMode_Object = MibTableColumn
pvxBWMeterMode = _PvxBWMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 14),
    _PvxBWMeterMode_Type()
)
pvxBWMeterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterMode.setStatus("current")


class _PvxBWMeterCir_Type(Integer32):
    """Custom type pvxBWMeterCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_PvxBWMeterCir_Type.__name__ = "Integer32"
_PvxBWMeterCir_Object = MibTableColumn
pvxBWMeterCir = _PvxBWMeterCir_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 15),
    _PvxBWMeterCir_Type()
)
pvxBWMeterCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterCir.setStatus("current")


class _PvxBWMeterCbs_Type(Integer32):
    """Custom type pvxBWMeterCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 256),
    )


_PvxBWMeterCbs_Type.__name__ = "Integer32"
_PvxBWMeterCbs_Object = MibTableColumn
pvxBWMeterCbs = _PvxBWMeterCbs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 16),
    _PvxBWMeterCbs_Type()
)
pvxBWMeterCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterCbs.setStatus("current")


class _PvxBWMeterEir_Type(Integer32):
    """Custom type pvxBWMeterEir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000000),
    )


_PvxBWMeterEir_Type.__name__ = "Integer32"
_PvxBWMeterEir_Object = MibTableColumn
pvxBWMeterEir = _PvxBWMeterEir_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 17),
    _PvxBWMeterEir_Type()
)
pvxBWMeterEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterEir.setStatus("current")


class _PvxBWMeterEbs_Type(Integer32):
    """Custom type pvxBWMeterEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PvxBWMeterEbs_Type.__name__ = "Integer32"
_PvxBWMeterEbs_Object = MibTableColumn
pvxBWMeterEbs = _PvxBWMeterEbs_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 18),
    _PvxBWMeterEbs_Type()
)
pvxBWMeterEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWMeterEbs.setStatus("current")


class _PvxBWSetInternalPriority_Type(Integer32):
    """Custom type pvxBWSetInternalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PvxBWSetInternalPriority_Type.__name__ = "Integer32"
_PvxBWSetInternalPriority_Object = MibTableColumn
pvxBWSetInternalPriority = _PvxBWSetInternalPriority_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 19),
    _PvxBWSetInternalPriority_Type()
)
pvxBWSetInternalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWSetInternalPriority.setStatus("current")


class _PvxBWExceedActionSetDEI_Type(Integer32):
    """Custom type pvxBWExceedActionSetDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNotSet", 2),
          ("notUsed", 3),
          ("set", 1))
    )


_PvxBWExceedActionSetDEI_Type.__name__ = "Integer32"
_PvxBWExceedActionSetDEI_Object = MibTableColumn
pvxBWExceedActionSetDEI = _PvxBWExceedActionSetDEI_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 20),
    _PvxBWExceedActionSetDEI_Type()
)
pvxBWExceedActionSetDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBWExceedActionSetDEI.setStatus("current")
_PvxBandwidthProfileRowStatus_Type = RowStatus
_PvxBandwidthProfileRowStatus_Object = MibTableColumn
pvxBandwidthProfileRowStatus = _PvxBandwidthProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 10, 1, 100),
    _PvxBandwidthProfileRowStatus_Type()
)
pvxBandwidthProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxBandwidthProfileRowStatus.setStatus("current")
_PvxClassMapProfileTable_Object = MibTable
pvxClassMapProfileTable = _PvxClassMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11)
)
if mibBuilder.loadTexts:
    pvxClassMapProfileTable.setStatus("current")
_PvxClassMapProfileEntry_Object = MibTableRow
pvxClassMapProfileEntry = _PvxClassMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1)
)
pvxClassMapProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxClassMapProfileName"),
)
if mibBuilder.loadTexts:
    pvxClassMapProfileEntry.setStatus("current")


class _PvxClassMapProfileName_Type(DisplayString):
    """Custom type pvxClassMapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxClassMapProfileName_Type.__name__ = "DisplayString"
_PvxClassMapProfileName_Object = MibTableColumn
pvxClassMapProfileName = _PvxClassMapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 1),
    _PvxClassMapProfileName_Type()
)
pvxClassMapProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxClassMapProfileName.setStatus("current")


class _PvxClassMapType_Type(Integer32):
    """Custom type pvxClassMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress-Per-Cos", 2),
          ("ingress-Per-Cos", 1),
          ("service-Map", 3))
    )


_PvxClassMapType_Type.__name__ = "Integer32"
_PvxClassMapType_Object = MibTableColumn
pvxClassMapType = _PvxClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 2),
    _PvxClassMapType_Type()
)
pvxClassMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapType.setStatus("current")


class _PvxClassMapMatchType_Type(Integer32):
    """Custom type pvxClassMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match-all", 1),
          ("match-any", 2))
    )


_PvxClassMapMatchType_Type.__name__ = "Integer32"
_PvxClassMapMatchType_Object = MibTableColumn
pvxClassMapMatchType = _PvxClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 3),
    _PvxClassMapMatchType_Type()
)
pvxClassMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapMatchType.setStatus("current")


class _PvxClassMapCVlanFilter_Type(Integer32):
    """Custom type pvxClassMapCVlanFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_PvxClassMapCVlanFilter_Type.__name__ = "Integer32"
_PvxClassMapCVlanFilter_Object = MibTableColumn
pvxClassMapCVlanFilter = _PvxClassMapCVlanFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 4),
    _PvxClassMapCVlanFilter_Type()
)
pvxClassMapCVlanFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapCVlanFilter.setStatus("current")


class _PvxClassMapSVlanFilter_Type(Integer32):
    """Custom type pvxClassMapSVlanFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_PvxClassMapSVlanFilter_Type.__name__ = "Integer32"
_PvxClassMapSVlanFilter_Object = MibTableColumn
pvxClassMapSVlanFilter = _PvxClassMapSVlanFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 5),
    _PvxClassMapSVlanFilter_Type()
)
pvxClassMapSVlanFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvxClassMapSVlanFilter.setStatus("deprecated")


class _PvxClassMapCVlanPriFilter_Type(Integer32):
    """Custom type pvxClassMapCVlanPriFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PvxClassMapCVlanPriFilter_Type.__name__ = "Integer32"
_PvxClassMapCVlanPriFilter_Object = MibTableColumn
pvxClassMapCVlanPriFilter = _PvxClassMapCVlanPriFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 6),
    _PvxClassMapCVlanPriFilter_Type()
)
pvxClassMapCVlanPriFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapCVlanPriFilter.setStatus("current")


class _PvxClassMapSVlanPriFilter_Type(Integer32):
    """Custom type pvxClassMapSVlanPriFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PvxClassMapSVlanPriFilter_Type.__name__ = "Integer32"
_PvxClassMapSVlanPriFilter_Object = MibTableColumn
pvxClassMapSVlanPriFilter = _PvxClassMapSVlanPriFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 7),
    _PvxClassMapSVlanPriFilter_Type()
)
pvxClassMapSVlanPriFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapSVlanPriFilter.setStatus("current")
_PvxClassMapSrcIpFilter_Type = IpAddress
_PvxClassMapSrcIpFilter_Object = MibTableColumn
pvxClassMapSrcIpFilter = _PvxClassMapSrcIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 8),
    _PvxClassMapSrcIpFilter_Type()
)
pvxClassMapSrcIpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapSrcIpFilter.setStatus("current")
_PvxClassMapSrcIpNetMaskFilter_Type = IpAddress
_PvxClassMapSrcIpNetMaskFilter_Object = MibTableColumn
pvxClassMapSrcIpNetMaskFilter = _PvxClassMapSrcIpNetMaskFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 9),
    _PvxClassMapSrcIpNetMaskFilter_Type()
)
pvxClassMapSrcIpNetMaskFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapSrcIpNetMaskFilter.setStatus("current")
_PvxClassMapDstIpFilter_Type = IpAddress
_PvxClassMapDstIpFilter_Object = MibTableColumn
pvxClassMapDstIpFilter = _PvxClassMapDstIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 10),
    _PvxClassMapDstIpFilter_Type()
)
pvxClassMapDstIpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapDstIpFilter.setStatus("current")
_PvxClassMapDstIpNetMaskFilter_Type = IpAddress
_PvxClassMapDstIpNetMaskFilter_Object = MibTableColumn
pvxClassMapDstIpNetMaskFilter = _PvxClassMapDstIpNetMaskFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 11),
    _PvxClassMapDstIpNetMaskFilter_Type()
)
pvxClassMapDstIpNetMaskFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapDstIpNetMaskFilter.setStatus("current")


class _PvxClassMapIpProtocolFilter_Type(Integer32):
    """Custom type pvxClassMapIpProtocolFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_PvxClassMapIpProtocolFilter_Type.__name__ = "Integer32"
_PvxClassMapIpProtocolFilter_Object = MibTableColumn
pvxClassMapIpProtocolFilter = _PvxClassMapIpProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 12),
    _PvxClassMapIpProtocolFilter_Type()
)
pvxClassMapIpProtocolFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapIpProtocolFilter.setStatus("current")


class _PvxClassMapDscpFilter_Type(Integer32):
    """Custom type pvxClassMapDscpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PvxClassMapDscpFilter_Type.__name__ = "Integer32"
_PvxClassMapDscpFilter_Object = MibTableColumn
pvxClassMapDscpFilter = _PvxClassMapDscpFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 13),
    _PvxClassMapDscpFilter_Type()
)
pvxClassMapDscpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapDscpFilter.setStatus("current")


class _PvxClassMapL4SrcPortFilter_Type(Integer32):
    """Custom type pvxClassMapL4SrcPortFilter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PvxClassMapL4SrcPortFilter_Type.__name__ = "Integer32"
_PvxClassMapL4SrcPortFilter_Object = MibTableColumn
pvxClassMapL4SrcPortFilter = _PvxClassMapL4SrcPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 14),
    _PvxClassMapL4SrcPortFilter_Type()
)
pvxClassMapL4SrcPortFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapL4SrcPortFilter.setStatus("current")


class _PvxClassMapL4DstPortFilter_Type(Integer32):
    """Custom type pvxClassMapL4DstPortFilter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PvxClassMapL4DstPortFilter_Type.__name__ = "Integer32"
_PvxClassMapL4DstPortFilter_Object = MibTableColumn
pvxClassMapL4DstPortFilter = _PvxClassMapL4DstPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 15),
    _PvxClassMapL4DstPortFilter_Type()
)
pvxClassMapL4DstPortFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapL4DstPortFilter.setStatus("current")


class _PvxClassMapTcpControlFilter_Type(Integer32):
    """Custom type pvxClassMapTcpControlFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PvxClassMapTcpControlFilter_Type.__name__ = "Integer32"
_PvxClassMapTcpControlFilter_Object = MibTableColumn
pvxClassMapTcpControlFilter = _PvxClassMapTcpControlFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 16),
    _PvxClassMapTcpControlFilter_Type()
)
pvxClassMapTcpControlFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapTcpControlFilter.setStatus("current")
_PvxClassMapSrcMACAddrFilter_Type = MacAddress
_PvxClassMapSrcMACAddrFilter_Object = MibTableColumn
pvxClassMapSrcMACAddrFilter = _PvxClassMapSrcMACAddrFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 17),
    _PvxClassMapSrcMACAddrFilter_Type()
)
pvxClassMapSrcMACAddrFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapSrcMACAddrFilter.setStatus("current")
_PvxClassMapDstMACAddrFilter_Type = MacAddress
_PvxClassMapDstMACAddrFilter_Object = MibTableColumn
pvxClassMapDstMACAddrFilter = _PvxClassMapDstMACAddrFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 18),
    _PvxClassMapDstMACAddrFilter_Type()
)
pvxClassMapDstMACAddrFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapDstMACAddrFilter.setStatus("current")


class _PvxClassMapEtherTypeFilter_Type(Integer32):
    """Custom type pvxClassMapEtherTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PvxClassMapEtherTypeFilter_Type.__name__ = "Integer32"
_PvxClassMapEtherTypeFilter_Object = MibTableColumn
pvxClassMapEtherTypeFilter = _PvxClassMapEtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 19),
    _PvxClassMapEtherTypeFilter_Type()
)
pvxClassMapEtherTypeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapEtherTypeFilter.setStatus("current")


class _PvxClassMapSrcMACMaskFilter_Type(Integer32):
    """Custom type pvxClassMapSrcMACMaskFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_PvxClassMapSrcMACMaskFilter_Type.__name__ = "Integer32"
_PvxClassMapSrcMACMaskFilter_Object = MibTableColumn
pvxClassMapSrcMACMaskFilter = _PvxClassMapSrcMACMaskFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 20),
    _PvxClassMapSrcMACMaskFilter_Type()
)
pvxClassMapSrcMACMaskFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapSrcMACMaskFilter.setStatus("current")


class _PvxClassMapDstMACMaskFilter_Type(Integer32):
    """Custom type pvxClassMapDstMACMaskFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_PvxClassMapDstMACMaskFilter_Type.__name__ = "Integer32"
_PvxClassMapDstMACMaskFilter_Object = MibTableColumn
pvxClassMapDstMACMaskFilter = _PvxClassMapDstMACMaskFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 21),
    _PvxClassMapDstMACMaskFilter_Type()
)
pvxClassMapDstMACMaskFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapDstMACMaskFilter.setStatus("current")


class _PvxClassMapL4SrcPortEndFilter_Type(Integer32):
    """Custom type pvxClassMapL4SrcPortEndFilter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(31, 31),
        ValueRangeConstraint(63, 63),
        ValueRangeConstraint(127, 127),
        ValueRangeConstraint(255, 255),
        ValueRangeConstraint(511, 511),
        ValueRangeConstraint(1023, 1023),
        ValueRangeConstraint(2047, 2047),
        ValueRangeConstraint(4095, 4095),
        ValueRangeConstraint(8191, 8191),
        ValueRangeConstraint(16383, 16383),
        ValueRangeConstraint(32767, 32767),
        ValueRangeConstraint(65535, 65535),
    )


_PvxClassMapL4SrcPortEndFilter_Type.__name__ = "Integer32"
_PvxClassMapL4SrcPortEndFilter_Object = MibTableColumn
pvxClassMapL4SrcPortEndFilter = _PvxClassMapL4SrcPortEndFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 22),
    _PvxClassMapL4SrcPortEndFilter_Type()
)
pvxClassMapL4SrcPortEndFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapL4SrcPortEndFilter.setStatus("current")


class _PvxClassMapL4DstPortEndFilter_Type(Integer32):
    """Custom type pvxClassMapL4DstPortEndFilter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(31, 31),
        ValueRangeConstraint(63, 63),
        ValueRangeConstraint(127, 127),
        ValueRangeConstraint(255, 255),
        ValueRangeConstraint(511, 511),
        ValueRangeConstraint(1023, 1023),
        ValueRangeConstraint(2047, 2047),
        ValueRangeConstraint(4095, 4095),
        ValueRangeConstraint(8191, 8191),
        ValueRangeConstraint(16383, 16383),
        ValueRangeConstraint(32767, 32767),
        ValueRangeConstraint(65535, 65535),
    )


_PvxClassMapL4DstPortEndFilter_Type.__name__ = "Integer32"
_PvxClassMapL4DstPortEndFilter_Object = MibTableColumn
pvxClassMapL4DstPortEndFilter = _PvxClassMapL4DstPortEndFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 23),
    _PvxClassMapL4DstPortEndFilter_Type()
)
pvxClassMapL4DstPortEndFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapL4DstPortEndFilter.setStatus("current")


class _PvxClassMapCVlanEndFilter_Type(Integer32):
    """Custom type pvxClassMapCVlanEndFilter based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_PvxClassMapCVlanEndFilter_Type.__name__ = "Integer32"
_PvxClassMapCVlanEndFilter_Object = MibTableColumn
pvxClassMapCVlanEndFilter = _PvxClassMapCVlanEndFilter_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 24),
    _PvxClassMapCVlanEndFilter_Type()
)
pvxClassMapCVlanEndFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapCVlanEndFilter.setStatus("current")
_PvxClassMapProfileRowStatus_Type = RowStatus
_PvxClassMapProfileRowStatus_Object = MibTableColumn
pvxClassMapProfileRowStatus = _PvxClassMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 11, 1, 100),
    _PvxClassMapProfileRowStatus_Type()
)
pvxClassMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxClassMapProfileRowStatus.setStatus("current")
_PvxPolicyMapProfileTable_Object = MibTable
pvxPolicyMapProfileTable = _PvxPolicyMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12)
)
if mibBuilder.loadTexts:
    pvxPolicyMapProfileTable.setStatus("current")
_PvxPolicyMapProfileEntry_Object = MibTableRow
pvxPolicyMapProfileEntry = _PvxPolicyMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12, 1)
)
pvxPolicyMapProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxPolicyMapPolicyName"),
    (0, "PACKET-VX-BRIDGE-MIB", "pvxPolicyMapClassMapName"),
)
if mibBuilder.loadTexts:
    pvxPolicyMapProfileEntry.setStatus("current")


class _PvxPolicyMapPolicyName_Type(DisplayString):
    """Custom type pvxPolicyMapPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxPolicyMapPolicyName_Type.__name__ = "DisplayString"
_PvxPolicyMapPolicyName_Object = MibTableColumn
pvxPolicyMapPolicyName = _PvxPolicyMapPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12, 1, 1),
    _PvxPolicyMapPolicyName_Type()
)
pvxPolicyMapPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxPolicyMapPolicyName.setStatus("current")


class _PvxPolicyMapClassMapName_Type(DisplayString):
    """Custom type pvxPolicyMapClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PvxPolicyMapClassMapName_Type.__name__ = "DisplayString"
_PvxPolicyMapClassMapName_Object = MibTableColumn
pvxPolicyMapClassMapName = _PvxPolicyMapClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12, 1, 2),
    _PvxPolicyMapClassMapName_Type()
)
pvxPolicyMapClassMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxPolicyMapClassMapName.setStatus("current")


class _PvxPolicyMapBWProfileName_Type(DisplayString):
    """Custom type pvxPolicyMapBWProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvxPolicyMapBWProfileName_Type.__name__ = "DisplayString"
_PvxPolicyMapBWProfileName_Object = MibTableColumn
pvxPolicyMapBWProfileName = _PvxPolicyMapBWProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12, 1, 3),
    _PvxPolicyMapBWProfileName_Type()
)
pvxPolicyMapBWProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPolicyMapBWProfileName.setStatus("current")
_PvxPolicyMapProfileRowStatus_Type = RowStatus
_PvxPolicyMapProfileRowStatus_Object = MibTableColumn
pvxPolicyMapProfileRowStatus = _PvxPolicyMapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 12, 1, 100),
    _PvxPolicyMapProfileRowStatus_Type()
)
pvxPolicyMapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxPolicyMapProfileRowStatus.setStatus("current")
_PvxControlFrameProfileTable_Object = MibTable
pvxControlFrameProfileTable = _PvxControlFrameProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13)
)
if mibBuilder.loadTexts:
    pvxControlFrameProfileTable.setStatus("current")
_PvxControlFrameProfileEntry_Object = MibTableRow
pvxControlFrameProfileEntry = _PvxControlFrameProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1)
)
pvxControlFrameProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxControlFrameProfileName"),
)
if mibBuilder.loadTexts:
    pvxControlFrameProfileEntry.setStatus("current")
_PvxControlFrameProfileName_Type = ProfileNameType
_PvxControlFrameProfileName_Object = MibTableColumn
pvxControlFrameProfileName = _PvxControlFrameProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 1),
    _PvxControlFrameProfileName_Type()
)
pvxControlFrameProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileName.setStatus("current")
_PvxControlFrameProfileLacp_Type = ProtocolActionType
_PvxControlFrameProfileLacp_Object = MibTableColumn
pvxControlFrameProfileLacp = _PvxControlFrameProfileLacp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 2),
    _PvxControlFrameProfileLacp_Type()
)
pvxControlFrameProfileLacp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileLacp.setStatus("current")
_PvxControlFrameProfileStp_Type = ProtocolActionType
_PvxControlFrameProfileStp_Object = MibTableColumn
pvxControlFrameProfileStp = _PvxControlFrameProfileStp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 3),
    _PvxControlFrameProfileStp_Type()
)
pvxControlFrameProfileStp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileStp.setStatus("current")
_PvxControlFrameProfileDot1x_Type = ProtocolActionType
_PvxControlFrameProfileDot1x_Object = MibTableColumn
pvxControlFrameProfileDot1x = _PvxControlFrameProfileDot1x_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 4),
    _PvxControlFrameProfileDot1x_Type()
)
pvxControlFrameProfileDot1x.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileDot1x.setStatus("current")
_PvxControlFrameProfileGvrp_Type = ProtocolActionType
_PvxControlFrameProfileGvrp_Object = MibTableColumn
pvxControlFrameProfileGvrp = _PvxControlFrameProfileGvrp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 5),
    _PvxControlFrameProfileGvrp_Type()
)
pvxControlFrameProfileGvrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileGvrp.setStatus("current")
_PvxControlFrameProfileGmrp_Type = ProtocolActionType
_PvxControlFrameProfileGmrp_Object = MibTableColumn
pvxControlFrameProfileGmrp = _PvxControlFrameProfileGmrp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 6),
    _PvxControlFrameProfileGmrp_Type()
)
pvxControlFrameProfileGmrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileGmrp.setStatus("current")
_PvxControlFrameProfileLldp_Type = ProtocolActionType
_PvxControlFrameProfileLldp_Object = MibTableColumn
pvxControlFrameProfileLldp = _PvxControlFrameProfileLldp_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 7),
    _PvxControlFrameProfileLldp_Type()
)
pvxControlFrameProfileLldp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileLldp.setStatus("current")
_PvxControlFrameProfileRowStatus_Type = RowStatus
_PvxControlFrameProfileRowStatus_Object = MibTableColumn
pvxControlFrameProfileRowStatus = _PvxControlFrameProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 13, 1, 100),
    _PvxControlFrameProfileRowStatus_Type()
)
pvxControlFrameProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxControlFrameProfileRowStatus.setStatus("current")
_PvxTunnelMacAddrProfileTable_Object = MibTable
pvxTunnelMacAddrProfileTable = _PvxTunnelMacAddrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14)
)
if mibBuilder.loadTexts:
    pvxTunnelMacAddrProfileTable.setStatus("current")
_PvxTunnelMacAddrProfileEntry_Object = MibTableRow
pvxTunnelMacAddrProfileEntry = _PvxTunnelMacAddrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1)
)
pvxTunnelMacAddrProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxTMAPName"),
)
if mibBuilder.loadTexts:
    pvxTunnelMacAddrProfileEntry.setStatus("current")
_PvxTMAPName_Type = ProfileNameType
_PvxTMAPName_Object = MibTableColumn
pvxTMAPName = _PvxTMAPName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 1),
    _PvxTMAPName_Type()
)
pvxTMAPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPName.setStatus("current")
_PvxTMAPDot1xTunnMacAddr_Type = MacAddress
_PvxTMAPDot1xTunnMacAddr_Object = MibTableColumn
pvxTMAPDot1xTunnMacAddr = _PvxTMAPDot1xTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 2),
    _PvxTMAPDot1xTunnMacAddr_Type()
)
pvxTMAPDot1xTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPDot1xTunnMacAddr.setStatus("current")
_PvxTMAPLacpTunnMacAddr_Type = MacAddress
_PvxTMAPLacpTunnMacAddr_Object = MibTableColumn
pvxTMAPLacpTunnMacAddr = _PvxTMAPLacpTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 3),
    _PvxTMAPLacpTunnMacAddr_Type()
)
pvxTMAPLacpTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPLacpTunnMacAddr.setStatus("current")
_PvxTMAPStpTunnMacAddr_Type = MacAddress
_PvxTMAPStpTunnMacAddr_Object = MibTableColumn
pvxTMAPStpTunnMacAddr = _PvxTMAPStpTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 4),
    _PvxTMAPStpTunnMacAddr_Type()
)
pvxTMAPStpTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPStpTunnMacAddr.setStatus("current")
_PvxTMAPGvrpTunnMacAddr_Type = MacAddress
_PvxTMAPGvrpTunnMacAddr_Object = MibTableColumn
pvxTMAPGvrpTunnMacAddr = _PvxTMAPGvrpTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 5),
    _PvxTMAPGvrpTunnMacAddr_Type()
)
pvxTMAPGvrpTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPGvrpTunnMacAddr.setStatus("current")
_PvxTMAPGmrpTunnMacAddr_Type = MacAddress
_PvxTMAPGmrpTunnMacAddr_Object = MibTableColumn
pvxTMAPGmrpTunnMacAddr = _PvxTMAPGmrpTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 6),
    _PvxTMAPGmrpTunnMacAddr_Type()
)
pvxTMAPGmrpTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPGmrpTunnMacAddr.setStatus("current")
_PvxTMAPLldpTunnMacAddr_Type = MacAddress
_PvxTMAPLldpTunnMacAddr_Object = MibTableColumn
pvxTMAPLldpTunnMacAddr = _PvxTMAPLldpTunnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 7),
    _PvxTMAPLldpTunnMacAddr_Type()
)
pvxTMAPLldpTunnMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPLldpTunnMacAddr.setStatus("current")
_PvxTMAPRowStatus_Type = RowStatus
_PvxTMAPRowStatus_Object = MibTableColumn
pvxTMAPRowStatus = _PvxTMAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 14, 1, 100),
    _PvxTMAPRowStatus_Type()
)
pvxTMAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxTMAPRowStatus.setStatus("current")
_PvxSLAMeasurementProfileTable_Object = MibTable
pvxSLAMeasurementProfileTable = _PvxSLAMeasurementProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15)
)
if mibBuilder.loadTexts:
    pvxSLAMeasurementProfileTable.setStatus("current")
_PvxSLAMeasurementProfileEntry_Object = MibTableRow
pvxSLAMeasurementProfileEntry = _PvxSLAMeasurementProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1)
)
pvxSLAMeasurementProfileEntry.setIndexNames(
    (0, "PACKET-VX-BRIDGE-MIB", "pvxSLAMsmtProfileName"),
)
if mibBuilder.loadTexts:
    pvxSLAMeasurementProfileEntry.setStatus("current")
_PvxSLAMsmtProfileName_Type = ProfileNameType
_PvxSLAMsmtProfileName_Object = MibTableColumn
pvxSLAMsmtProfileName = _PvxSLAMsmtProfileName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 1),
    _PvxSLAMsmtProfileName_Type()
)
pvxSLAMsmtProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvxSLAMsmtProfileName.setStatus("current")
_PvxSLAMsmtThresholdFarEndLossRatio_Type = FixedX1000
_PvxSLAMsmtThresholdFarEndLossRatio_Object = MibTableColumn
pvxSLAMsmtThresholdFarEndLossRatio = _PvxSLAMsmtThresholdFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 2),
    _PvxSLAMsmtThresholdFarEndLossRatio_Type()
)
pvxSLAMsmtThresholdFarEndLossRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdFarEndLossRatio.setStatus("current")
_PvxSLAMsmtThresholdNearEndLossRatio_Type = FixedX1000
_PvxSLAMsmtThresholdNearEndLossRatio_Object = MibTableColumn
pvxSLAMsmtThresholdNearEndLossRatio = _PvxSLAMsmtThresholdNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 3),
    _PvxSLAMsmtThresholdNearEndLossRatio_Type()
)
pvxSLAMsmtThresholdNearEndLossRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdNearEndLossRatio.setStatus("current")
_PvxSLAMsmtThresholdDelayMaximum_Type = Unsigned32
_PvxSLAMsmtThresholdDelayMaximum_Object = MibTableColumn
pvxSLAMsmtThresholdDelayMaximum = _PvxSLAMsmtThresholdDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 4),
    _PvxSLAMsmtThresholdDelayMaximum_Type()
)
pvxSLAMsmtThresholdDelayMaximum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdDelayMaximum.setStatus("current")
_PvxSLAMsmtThresholdDelayAverage_Type = Unsigned32
_PvxSLAMsmtThresholdDelayAverage_Object = MibTableColumn
pvxSLAMsmtThresholdDelayAverage = _PvxSLAMsmtThresholdDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 5),
    _PvxSLAMsmtThresholdDelayAverage_Type()
)
pvxSLAMsmtThresholdDelayAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdDelayAverage.setStatus("current")
_PvxSLAMsmtThresholdDelayVarMaximum_Type = Unsigned32
_PvxSLAMsmtThresholdDelayVarMaximum_Object = MibTableColumn
pvxSLAMsmtThresholdDelayVarMaximum = _PvxSLAMsmtThresholdDelayVarMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 6),
    _PvxSLAMsmtThresholdDelayVarMaximum_Type()
)
pvxSLAMsmtThresholdDelayVarMaximum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdDelayVarMaximum.setStatus("current")
_PvxSLAMsmtThresholdDelayVarAverage_Type = Unsigned32
_PvxSLAMsmtThresholdDelayVarAverage_Object = MibTableColumn
pvxSLAMsmtThresholdDelayVarAverage = _PvxSLAMsmtThresholdDelayVarAverage_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 7),
    _PvxSLAMsmtThresholdDelayVarAverage_Type()
)
pvxSLAMsmtThresholdDelayVarAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtThresholdDelayVarAverage.setStatus("current")
_PvxSLAMsmtMonitorPeriod_Type = MonitorPeriodType
_PvxSLAMsmtMonitorPeriod_Object = MibTableColumn
pvxSLAMsmtMonitorPeriod = _PvxSLAMsmtMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 8),
    _PvxSLAMsmtMonitorPeriod_Type()
)
pvxSLAMsmtMonitorPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtMonitorPeriod.setStatus("current")
_PvxSLAMsmtRowStatus_Type = RowStatus
_PvxSLAMsmtRowStatus_Object = MibTableColumn
pvxSLAMsmtRowStatus = _PvxSLAMsmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 3, 15, 1, 100),
    _PvxSLAMsmtRowStatus_Type()
)
pvxSLAMsmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvxSLAMsmtRowStatus.setStatus("current")


class _MstpGlobalErrType_Type(Integer32):
    """Custom type mstpGlobalErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1))
    )


_MstpGlobalErrType_Type.__name__ = "Integer32"
_MstpGlobalErrType_Object = MibScalar
mstpGlobalErrType = _MstpGlobalErrType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 4, 1, 1),
    _MstpGlobalErrType_Type()
)
mstpGlobalErrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mstpGlobalErrType.setStatus("current")


class _MstpGeneralEvtType_Type(Integer32):
    """Custom type mstpGeneralEvtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MstpGeneralEvtType_Type.__name__ = "Integer32"
_MstpGeneralEvtType_Object = MibScalar
mstpGeneralEvtType = _MstpGeneralEvtType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 4, 1, 2),
    _MstpGeneralEvtType_Type()
)
mstpGeneralEvtType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mstpGeneralEvtType.setStatus("current")


class _MstpProtocolMigrationType_Type(Integer32):
    """Custom type mstpProtocolMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 2),
          ("sendstp", 1))
    )


_MstpProtocolMigrationType_Type.__name__ = "Integer32"
_MstpProtocolMigrationType_Object = MibScalar
mstpProtocolMigrationType = _MstpProtocolMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 4, 1, 3),
    _MstpProtocolMigrationType_Type()
)
mstpProtocolMigrationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mstpProtocolMigrationType.setStatus("current")


class _MstpPacketErrType_Type(Integer32):
    """Custom type mstpPacketErrType based on Integer32"""
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
        *(("configLengthErr", 3),
          ("fwdDelayErr", 7),
          ("helloTimeErr", 8),
          ("invalidBpdu", 2),
          ("maxAgeErr", 6),
          ("mstpLengthErr", 9),
          ("protocolIdErr", 1),
          ("rstpLengthErr", 5),
          ("tcnLengthErr", 4))
    )


_MstpPacketErrType_Type.__name__ = "Integer32"
_MstpPacketErrType_Object = MibScalar
mstpPacketErrType = _MstpPacketErrType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 4, 1, 4),
    _MstpPacketErrType_Type()
)
mstpPacketErrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mstpPacketErrType.setStatus("current")
_MstpPacketErrValue_Type = Integer32
_MstpPacketErrValue_Object = MibScalar
mstpPacketErrValue = _MstpPacketErrValue_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 4, 1, 5),
    _MstpPacketErrValue_Type()
)
mstpPacketErrValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mstpPacketErrValue.setStatus("current")
_PvxBridgeGVRP_ObjectIdentity = ObjectIdentity
pvxBridgeGVRP = _PvxBridgeGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 1, 14, 5)
)
_CfmRMepStateChangeEvtNotifications_ObjectIdentity = ObjectIdentity
cfmRMepStateChangeEvtNotifications = _CfmRMepStateChangeEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 36)
)
_PvxVlanPortLastBpduOriginChangeEvtNotifications_ObjectIdentity = ObjectIdentity
pvxVlanPortLastBpduOriginChangeEvtNotifications = _PvxVlanPortLastBpduOriginChangeEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 37)
)
_PvxVlanPortAddDynamicVlanEvtNotifications_ObjectIdentity = ObjectIdentity
pvxVlanPortAddDynamicVlanEvtNotifications = _PvxVlanPortAddDynamicVlanEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 38)
)
_PvxVlanPortRemoveDynamicVlanEvtNotifications_ObjectIdentity = ObjectIdentity
pvxVlanPortRemoveDynamicVlanEvtNotifications = _PvxVlanPortRemoveDynamicVlanEvtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 39)
)

# Managed Objects groups


# Notification objects

mstpProtocolGeneralEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 1)
)
mstpProtocolGeneralEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "mstpGeneralEvtType"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpProtocolGeneralEvt.setStatus(
        "current"
    )

mstpNewRootEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 2)
)
mstpNewRootEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgRegRoot"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpNewRootEvt.setStatus(
        "current"
    )

mstpTopologyChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 3)
)
mstpTopologyChangeEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpTopologyChangeEvt.setStatus(
        "current"
    )

mstpProtocolMigrationEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 4)
)
mstpProtocolMigrationEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenVersionSupported"),
        ("PACKET-VX-BRIDGE-MIB", "mstpProtocolMigrationType"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpProtocolMigrationEvt.setStatus(
        "current"
    )

mstpInvalidPacketRcvdEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 5)
)
mstpInvalidPacketRcvdEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "mstpPacketErrType"),
        ("PACKET-VX-BRIDGE-MIB", "mstpPacketErrValue"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpInvalidPacketRcvdEvt.setStatus(
        "current"
    )

mstpRegionConfigChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 6)
)
mstpRegionConfigChangeEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenIdFmtSel"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenIdName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenIdRevisionLevel"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenIdDigest"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpRegionConfigChangeEvt.setStatus(
        "current"
    )

mstpRoleChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 23, 0, 7)
)
mstpRoleChangeEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPPortRole"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    mstpRoleChangeEvt.setStatus(
        "current"
    )

pvxESrvcBWPrflBDWUtlzTcaEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 26, 0, 1)
)
pvxESrvcBWPrflBDWUtlzTcaEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMShelfIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMSlotIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPortTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPortIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMESrvcNameIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMPlcyNameIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMClsMapNameIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMDirectionIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMIntervalTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflCrntPMBDWUtlzValue"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdLevelTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxESrvcBWPrflPMThresholdBDWUtlzValue"),
        ("BTI-7000-MIB", "tcaDateAndTime"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxESrvcBWPrflBDWUtlzTcaEvt.setStatus(
        "current"
    )

pvxESrvcOperStateChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 27, 0, 1)
)
pvxESrvcOperStateChangeEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxEthSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEthSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEthSrvcOperState"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDefects"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEcfmMepY1731DefectConditions"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEthSrvcExceedMaxUNI"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxESrvcOperStateChangeEvt.setStatus(
        "current"
    )

pvxERPSSrvcNNIProtectionSwitchChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 28, 0, 1)
)
pvxERPSSrvcNNIProtectionSwitchChangeEvent.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNISwitchId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIShelfId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNISlotId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIPortTypeId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIPortId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNISrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcProtectionSwitchMode"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIProtectionSwitch"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcNNIRingPortStatus"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcNNIProtectionSwitchChangeEvent.setStatus(
        "current"
    )

pvxERPSSrvcRingSemStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 29, 0, 1)
)
pvxERPSSrvcRingSemStateChangeEvent.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcRingSemStateChangeEvent.setStatus(
        "current"
    )

pvxERPSSrvcConfigFailEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 29, 0, 2)
)
pvxERPSSrvcConfigFailEvent.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcConfigFailEvent.setStatus(
        "current"
    )

pvxERPSSrvcTimerStartEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 29, 0, 3)
)
pvxERPSSrvcTimerStartEvent.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcTimerStartEvent.setStatus(
        "current"
    )

pvxSlaMeasurementTcaEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 30, 0, 1)
)
pvxSlaMeasurementTcaEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMShelfIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMSlotIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMPortTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMPortIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMESName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMRMepId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEServiceSlaCrntPMIntervalTypeIdx"),
        ("BTI-7000-MIB", "tcaDateAndTime"),
        ("BTI-7000-MIB", "tcaMontype"),
        ("BTI-7000-MIB", "tcaValue"),
        ("BTI-7000-MIB", "tcaThreshold"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxSlaMeasurementTcaEvt.setStatus(
        "current"
    )

pvxSrvcUNIEFPSDLocalEFPSDStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 32, 0, 1)
)
pvxSrvcUNIEFPSDLocalEFPSDStateChangeEvent.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISwitchId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIShelfId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISlotId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIPortTypeId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIPortId"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNISrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSrvcUNIEFPSDLocalEFPSDState"),
        ("BTI-7000-MIB", "evtDateAndTime"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "evtDescription"),
        ("BTI-7000-MIB", "evtObjectType"),
        ("BTI-7000-MIB", "evtCodeType"))
)
if mibBuilder.loadTexts:
    pvxSrvcUNIEFPSDLocalEFPSDStateChangeEvent.setStatus(
        "current"
    )

cfmRMepStateChangeV2Evt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 36, 0, 2)
)
cfmRMepStateChangeV2Evt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDbRMepState"),
        ("PACKET-VX-BRIDGE-MIB", "pvxEcfmMepDefects"))
)
if mibBuilder.loadTexts:
    cfmRMepStateChangeV2Evt.setStatus(
        "current"
    )

pvxVlanPortLastBpduOriginChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 37, 0, 1)
)
pvxVlanPortLastBpduOriginChangeEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortShelfIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSlotIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortIdx"))
)
if mibBuilder.loadTexts:
    pvxVlanPortLastBpduOriginChangeEvt.setStatus(
        "current"
    )

pvxVlanPortAddDynamicVlanEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 38, 0, 1)
)
pvxVlanPortAddDynamicVlanEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortShelfIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSlotIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVLANIdx"))
)
if mibBuilder.loadTexts:
    pvxVlanPortAddDynamicVlanEvt.setStatus(
        "current"
    )

pvxVlanPortRemoveDynamicVlanEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 1, 39, 0, 1)
)
pvxVlanPortRemoveDynamicVlanEvt.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortShelfIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortSlotIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortTypeIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVlanPortIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxVLANIdx"))
)
if mibBuilder.loadTexts:
    pvxVlanPortRemoveDynamicVlanEvt.setStatus(
        "current"
    )

resourceUnavailableCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 22, 0, 1)
)
resourceUnavailableCond.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "mstpGlobalErrType"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    resourceUnavailableCond.setStatus(
        "current"
    )

resourceUnavailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 22, 0, 2)
)
resourceUnavailableClear.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxMSTPGenSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxMSTPXstBrdgId"),
        ("PACKET-VX-BRIDGE-MIB", "mstpGlobalErrType"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    resourceUnavailableClear.setStatus(
        "current"
    )

lagLinkDownCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 23, 0, 1)
)
lagLinkDownCond.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxLGSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxLGIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    lagLinkDownCond.setStatus(
        "current"
    )

lagLinkDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 23, 0, 2)
)
lagLinkDownClear.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxLGSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxLGIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    lagLinkDownClear.setStatus(
        "current"
    )

pvxERPSSrvcVersionMismatchCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 29, 0, 1)
)
pvxERPSSrvcVersionMismatchCond.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcCompatibleVersion"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcVersionMismatchCond.setStatus(
        "current"
    )

pvxERPSSrvcVersionMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 29, 0, 2)
)
pvxERPSSrvcVersionMismatchClear.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcCompatibleVersion"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcVersionMismatchClear.setStatus(
        "current"
    )

pvxERPSSrvcFOPProvisionMismatchCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 29, 0, 3)
)
pvxERPSSrvcFOPProvisionMismatchCond.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcFOPProvisionMismatchCond.setStatus(
        "current"
    )

pvxERPSSrvcFOPProvisionMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 29, 0, 4)
)
pvxERPSSrvcFOPProvisionMismatchClear.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcName"),
        ("PACKET-VX-BRIDGE-MIB", "pvxERPSSrvcRingSemState"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condDescription"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    pvxERPSSrvcFOPProvisionMismatchClear.setStatus(
        "current"
    )

switchMemberStkPortDownCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 30, 0, 1)
)
switchMemberStkPortDownCond.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSwitchMemberIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    switchMemberStkPortDownCond.setStatus(
        "current"
    )

switchMemberStkPortDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2, 2, 2, 30, 0, 2)
)
switchMemberStkPortDownClear.setObjects(
      *(("PACKET-VX-BRIDGE-MIB", "pvxSwitchIdx"),
        ("PACKET-VX-BRIDGE-MIB", "pvxSwitchMemberIdx"),
        ("BTI-7000-MIB", "condReportType"),
        ("BTI-7000-MIB", "condDateAndTime"),
        ("BTI-7000-MIB", "condSeverity"),
        ("BTI-7000-MIB", "condServiceAffecting"),
        ("BTI-7000-MIB", "trapSeqNum"),
        ("BTI-7000-MIB", "condObjectType"),
        ("BTI-7000-MIB", "condCodeType"))
)
if mibBuilder.loadTexts:
    switchMemberStkPortDownClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKET-VX-BRIDGE-MIB",
    **{"PvxPhyPort": PvxPhyPort,
       "PvxPhyPortList": PvxPhyPortList,
       "PvxL2PortList": PvxL2PortList,
       "PvxVLANPortList": PvxVLANPortList,
       "PvxL2Port": PvxL2Port,
       "PvxVlanId": PvxVlanId,
       "PvxMSTPVlanList": PvxMSTPVlanList,
       "PvxPCPDecodingList": PvxPCPDecodingList,
       "PvxPolicyDropAction": PvxPolicyDropAction,
       "PvxQoSColorMode": PvxQoSColorMode,
       "PvxQoSPmCounterMode": PvxQoSPmCounterMode,
       "PvxCVidMapOperStatus": PvxCVidMapOperStatus,
       "PvxEcfmTransmitStatus": PvxEcfmTransmitStatus,
       "PvxEcfmMepDefects": PvxEcfmMepDefects,
       "PvxY1731MepDefects": PvxY1731MepDefects,
       "PvxEcfmRemoteMepState": PvxEcfmRemoteMepState,
       "PvxEcfmConfigErrors": PvxEcfmConfigErrors,
       "PvxEcfmRelayActionFieldValue": PvxEcfmRelayActionFieldValue,
       "PvxEcfmIngressActionFieldValue": PvxEcfmIngressActionFieldValue,
       "PvxEcfmEgressActionFieldValue": PvxEcfmEgressActionFieldValue,
       "PvxErpsVirtualLinkList": PvxErpsVirtualLinkList,
       "PvxESrvcBWPrflPMThresholdLevelType": PvxESrvcBWPrflPMThresholdLevelType,
       "PvxStackingPortCommState": PvxStackingPortCommState,
       "packetVxBridgeMib": packetVxBridgeMib,
       "pvxMSTPCrntPMTable": pvxMSTPCrntPMTable,
       "pvxMSTPCrntPMEntry": pvxMSTPCrntPMEntry,
       "pvxMSTPCrntPMSwitchIdx": pvxMSTPCrntPMSwitchIdx,
       "pvxMSTPCrntPMXstIdx": pvxMSTPCrntPMXstIdx,
       "pvxMSTPCrntPMIntervalTypeIdx": pvxMSTPCrntPMIntervalTypeIdx,
       "pvxMSTPCrntPMRCCCValue": pvxMSTPCrntPMRCCCValue,
       "pvxMSTPCrntPMRCCCTimeStamp": pvxMSTPCrntPMRCCCTimeStamp,
       "pvxMSTPCrntPMRCCCValidity": pvxMSTPCrntPMRCCCValidity,
       "pvxMSTPCrntPMRCCCInitialize": pvxMSTPCrntPMRCCCInitialize,
       "pvxMSTPCrntPMTCCValue": pvxMSTPCrntPMTCCValue,
       "pvxMSTPCrntPMTCCTimeStamp": pvxMSTPCrntPMTCCTimeStamp,
       "pvxMSTPCrntPMTCCValidity": pvxMSTPCrntPMTCCValidity,
       "pvxMSTPCrntPMTCCInitialize": pvxMSTPCrntPMTCCInitialize,
       "pvxMSTPCrntPMNRBCValue": pvxMSTPCrntPMNRBCValue,
       "pvxMSTPCrntPMNRBCTimeStamp": pvxMSTPCrntPMNRBCTimeStamp,
       "pvxMSTPCrntPMNRBCValidity": pvxMSTPCrntPMNRBCValidity,
       "pvxMSTPCrntPMNRBCInitialize": pvxMSTPCrntPMNRBCInitialize,
       "pvxMSTPHistPMTable": pvxMSTPHistPMTable,
       "pvxMSTPHistPMEntry": pvxMSTPHistPMEntry,
       "pvxMSTPHistPMSwitchIdx": pvxMSTPHistPMSwitchIdx,
       "pvxMSTPHistPMXstIdx": pvxMSTPHistPMXstIdx,
       "pvxMSTPHistPMIntervalTypeIdx": pvxMSTPHistPMIntervalTypeIdx,
       "pvxMSTPHistPMIntervalIdx": pvxMSTPHistPMIntervalIdx,
       "pvxMSTPHistPMRCCCValue": pvxMSTPHistPMRCCCValue,
       "pvxMSTPHistPMRCCCTimeStamp": pvxMSTPHistPMRCCCTimeStamp,
       "pvxMSTPHistPMRCCCValidity": pvxMSTPHistPMRCCCValidity,
       "pvxMSTPHistPMRCCCInitialize": pvxMSTPHistPMRCCCInitialize,
       "pvxMSTPHistPMTCCValue": pvxMSTPHistPMTCCValue,
       "pvxMSTPHistPMTCCTimeStamp": pvxMSTPHistPMTCCTimeStamp,
       "pvxMSTPHistPMTCCValidity": pvxMSTPHistPMTCCValidity,
       "pvxMSTPHistPMTCCInitialize": pvxMSTPHistPMTCCInitialize,
       "pvxMSTPHistPMNRBCValue": pvxMSTPHistPMNRBCValue,
       "pvxMSTPHistPMNRBCTimeStamp": pvxMSTPHistPMNRBCTimeStamp,
       "pvxMSTPHistPMNRBCValidity": pvxMSTPHistPMNRBCValidity,
       "pvxMSTPHistPMNRBCInitialize": pvxMSTPHistPMNRBCInitialize,
       "pvxMSTPPortCrntPMTable": pvxMSTPPortCrntPMTable,
       "pvxMSTPPortCrntPMEntry": pvxMSTPPortCrntPMEntry,
       "pvxMSTPPortCrntPMSwitchIdx": pvxMSTPPortCrntPMSwitchIdx,
       "pvxMSTPPortCrntPMShelfIdx": pvxMSTPPortCrntPMShelfIdx,
       "pvxMSTPPortCrntPMSlotIdx": pvxMSTPPortCrntPMSlotIdx,
       "pvxMSTPPortCrntPMTypeIdx": pvxMSTPPortCrntPMTypeIdx,
       "pvxMSTPPortCrntPMXstIdx": pvxMSTPPortCrntPMXstIdx,
       "pvxMSTPPortCrntPMIdx": pvxMSTPPortCrntPMIdx,
       "pvxMSTPPortCrntPMIntervalTypeIdx": pvxMSTPPortCrntPMIntervalTypeIdx,
       "pvxMSTPPortCrntPMFWDTRValue": pvxMSTPPortCrntPMFWDTRValue,
       "pvxMSTPPortCrntPMFWDTRTimeStamp": pvxMSTPPortCrntPMFWDTRTimeStamp,
       "pvxMSTPPortCrntPMFWDTRValidity": pvxMSTPPortCrntPMFWDTRValidity,
       "pvxMSTPPortCrntPMFWDTRInitialize": pvxMSTPPortCrntPMFWDTRInitialize,
       "pvxMSTPPortCrntPMPMCValue": pvxMSTPPortCrntPMPMCValue,
       "pvxMSTPPortCrntPMPMCTimeStamp": pvxMSTPPortCrntPMPMCTimeStamp,
       "pvxMSTPPortCrntPMPMCValidity": pvxMSTPPortCrntPMPMCValidity,
       "pvxMSTPPortCrntPMPMCInitialize": pvxMSTPPortCrntPMPMCInitialize,
       "pvxMSTPPortCrntPMBPDURXValue": pvxMSTPPortCrntPMBPDURXValue,
       "pvxMSTPPortCrntPMBPDURXTimeStamp": pvxMSTPPortCrntPMBPDURXTimeStamp,
       "pvxMSTPPortCrntPMBPDURXValidity": pvxMSTPPortCrntPMBPDURXValidity,
       "pvxMSTPPortCrntPMBPDURXInitialize": pvxMSTPPortCrntPMBPDURXInitialize,
       "pvxMSTPPortCrntPMBPDUTXValue": pvxMSTPPortCrntPMBPDUTXValue,
       "pvxMSTPPortCrntPMBPDUTXTimeStamp": pvxMSTPPortCrntPMBPDUTXTimeStamp,
       "pvxMSTPPortCrntPMBPDUTXValidity": pvxMSTPPortCrntPMBPDUTXValidity,
       "pvxMSTPPortCrntPMBPDUTXInitialize": pvxMSTPPortCrntPMBPDUTXInitialize,
       "pvxMSTPPortCrntPMBPDUCFGRXValue": pvxMSTPPortCrntPMBPDUCFGRXValue,
       "pvxMSTPPortCrntPMBPDUCFGRXTimeStamp": pvxMSTPPortCrntPMBPDUCFGRXTimeStamp,
       "pvxMSTPPortCrntPMBPDUCFGRXValidity": pvxMSTPPortCrntPMBPDUCFGRXValidity,
       "pvxMSTPPortCrntPMBPDUCFGRXInitialize": pvxMSTPPortCrntPMBPDUCFGRXInitialize,
       "pvxMSTPPortCrntPMBPDUCFGTXValue": pvxMSTPPortCrntPMBPDUCFGTXValue,
       "pvxMSTPPortCrntPMBPDUCFGTXTimeStamp": pvxMSTPPortCrntPMBPDUCFGTXTimeStamp,
       "pvxMSTPPortCrntPMBPDUCFGTXValidity": pvxMSTPPortCrntPMBPDUCFGTXValidity,
       "pvxMSTPPortCrntPMBPDUCFGTXInitialize": pvxMSTPPortCrntPMBPDUCFGTXInitialize,
       "pvxMSTPPortCrntPMBPDUTCNRXValue": pvxMSTPPortCrntPMBPDUTCNRXValue,
       "pvxMSTPPortCrntPMBPDUTCNRXTimeStamp": pvxMSTPPortCrntPMBPDUTCNRXTimeStamp,
       "pvxMSTPPortCrntPMBPDUTCNRXValidity": pvxMSTPPortCrntPMBPDUTCNRXValidity,
       "pvxMSTPPortCrntPMBPDUTCNRXInitialize": pvxMSTPPortCrntPMBPDUTCNRXInitialize,
       "pvxMSTPPortCrntPMBPDUTCNTXValue": pvxMSTPPortCrntPMBPDUTCNTXValue,
       "pvxMSTPPortCrntPMBPDUTCNTXTimeStamp": pvxMSTPPortCrntPMBPDUTCNTXTimeStamp,
       "pvxMSTPPortCrntPMBPDUTCNTXValidity": pvxMSTPPortCrntPMBPDUTCNTXValidity,
       "pvxMSTPPortCrntPMBPDUTCNTXInitialize": pvxMSTPPortCrntPMBPDUTCNTXInitialize,
       "pvxMSTPPortCrntPMINVBPDURXValue": pvxMSTPPortCrntPMINVBPDURXValue,
       "pvxMSTPPortCrntPMINVBPDURXTimeStamp": pvxMSTPPortCrntPMINVBPDURXTimeStamp,
       "pvxMSTPPortCrntPMINVBPDURXValidity": pvxMSTPPortCrntPMINVBPDURXValidity,
       "pvxMSTPPortCrntPMINVBPDURXInitialize": pvxMSTPPortCrntPMINVBPDURXInitialize,
       "pvxMSTPPortCrntPMINVBPDUCFGRXValue": pvxMSTPPortCrntPMINVBPDUCFGRXValue,
       "pvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp": pvxMSTPPortCrntPMINVBPDUCFGRXTimeStamp,
       "pvxMSTPPortCrntPMINVBPDUCFGRXValidity": pvxMSTPPortCrntPMINVBPDUCFGRXValidity,
       "pvxMSTPPortCrntPMINVBPDUCFGRXInitialize": pvxMSTPPortCrntPMINVBPDUCFGRXInitialize,
       "pvxMSTPPortCrntPMINVBPDUTCNRXValue": pvxMSTPPortCrntPMINVBPDUTCNRXValue,
       "pvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp": pvxMSTPPortCrntPMINVBPDUTCNRXTimeStamp,
       "pvxMSTPPortCrntPMINVBPDUTCNRXValidity": pvxMSTPPortCrntPMINVBPDUTCNRXValidity,
       "pvxMSTPPortCrntPMINVBPDUTCNRXInitialize": pvxMSTPPortCrntPMINVBPDUTCNRXInitialize,
       "pvxMSTPPortHistPMTable": pvxMSTPPortHistPMTable,
       "pvxMSTPPortHistPMEntry": pvxMSTPPortHistPMEntry,
       "pvxMSTPPortHistPMSwitchIdx": pvxMSTPPortHistPMSwitchIdx,
       "pvxMSTPPortHistPMShelfIdx": pvxMSTPPortHistPMShelfIdx,
       "pvxMSTPPortHistPMSlotIdx": pvxMSTPPortHistPMSlotIdx,
       "pvxMSTPPortHistPMTypeIdx": pvxMSTPPortHistPMTypeIdx,
       "pvxMSTPPortHistPMXstIdx": pvxMSTPPortHistPMXstIdx,
       "pvxMSTPPortHistPMIdx": pvxMSTPPortHistPMIdx,
       "pvxMSTPPortHistPMIntervalTypeIdx": pvxMSTPPortHistPMIntervalTypeIdx,
       "pvxMSTPPortHistPMIntervalIdx": pvxMSTPPortHistPMIntervalIdx,
       "pvxMSTPPortHistPMFWDTRValue": pvxMSTPPortHistPMFWDTRValue,
       "pvxMSTPPortHistPMFWDTRTimeStamp": pvxMSTPPortHistPMFWDTRTimeStamp,
       "pvxMSTPPortHistPMFWDTRValidity": pvxMSTPPortHistPMFWDTRValidity,
       "pvxMSTPPortHistPMFWDTRInitialize": pvxMSTPPortHistPMFWDTRInitialize,
       "pvxMSTPPortHistPMPMCValue": pvxMSTPPortHistPMPMCValue,
       "pvxMSTPPortHistPMPMCTimeStamp": pvxMSTPPortHistPMPMCTimeStamp,
       "pvxMSTPPortHistPMPMCValidity": pvxMSTPPortHistPMPMCValidity,
       "pvxMSTPPortHistPMPMCInitialize": pvxMSTPPortHistPMPMCInitialize,
       "pvxMSTPPortHistPMBPDURXValue": pvxMSTPPortHistPMBPDURXValue,
       "pvxMSTPPortHistPMBPDURXTimeStamp": pvxMSTPPortHistPMBPDURXTimeStamp,
       "pvxMSTPPortHistPMBPDURXValidity": pvxMSTPPortHistPMBPDURXValidity,
       "pvxMSTPPortHistPMBPDURXInitialize": pvxMSTPPortHistPMBPDURXInitialize,
       "pvxMSTPPortHistPMBPDUTXValue": pvxMSTPPortHistPMBPDUTXValue,
       "pvxMSTPPortHistPMBPDUTXTimeStamp": pvxMSTPPortHistPMBPDUTXTimeStamp,
       "pvxMSTPPortHistPMBPDUTXValidity": pvxMSTPPortHistPMBPDUTXValidity,
       "pvxMSTPPortHistPMBPDUTXInitialize": pvxMSTPPortHistPMBPDUTXInitialize,
       "pvxMSTPPortHistPMBPDUCFGRXValue": pvxMSTPPortHistPMBPDUCFGRXValue,
       "pvxMSTPPortHistPMBPDUCFGRXTimeStamp": pvxMSTPPortHistPMBPDUCFGRXTimeStamp,
       "pvxMSTPPortHistPMBPDUCFGRXValidity": pvxMSTPPortHistPMBPDUCFGRXValidity,
       "pvxMSTPPortHistPMBPDUCFGRXInitialize": pvxMSTPPortHistPMBPDUCFGRXInitialize,
       "pvxMSTPPortHistPMBPDUCFGTXValue": pvxMSTPPortHistPMBPDUCFGTXValue,
       "pvxMSTPPortHistPMBPDUCFGTXTimeStamp": pvxMSTPPortHistPMBPDUCFGTXTimeStamp,
       "pvxMSTPPortHistPMBPDUCFGTXValidity": pvxMSTPPortHistPMBPDUCFGTXValidity,
       "pvxMSTPPortHistPMBPDUCFGTXInitialize": pvxMSTPPortHistPMBPDUCFGTXInitialize,
       "pvxMSTPPortHistPMBPDUTCNRXValue": pvxMSTPPortHistPMBPDUTCNRXValue,
       "pvxMSTPPortHistPMBPDUTCNRXTimeStamp": pvxMSTPPortHistPMBPDUTCNRXTimeStamp,
       "pvxMSTPPortHistPMBPDUTCNRXValidity": pvxMSTPPortHistPMBPDUTCNRXValidity,
       "pvxMSTPPortHistPMBPDUTCNRXInitialize": pvxMSTPPortHistPMBPDUTCNRXInitialize,
       "pvxMSTPPortHistPMBPDUTCNTXValue": pvxMSTPPortHistPMBPDUTCNTXValue,
       "pvxMSTPPortHistPMBPDUTCNTXTimeStamp": pvxMSTPPortHistPMBPDUTCNTXTimeStamp,
       "pvxMSTPPortHistPMBPDUTCNTXValidity": pvxMSTPPortHistPMBPDUTCNTXValidity,
       "pvxMSTPPortHistPMBPDUTCNTXInitialize": pvxMSTPPortHistPMBPDUTCNTXInitialize,
       "pvxMSTPPortHistPMINVBPDURXValue": pvxMSTPPortHistPMINVBPDURXValue,
       "pvxMSTPPortHistPMINVBPDURXTimeStamp": pvxMSTPPortHistPMINVBPDURXTimeStamp,
       "pvxMSTPPortHistPMINVBPDURXValidity": pvxMSTPPortHistPMINVBPDURXValidity,
       "pvxMSTPPortHistPMINVBPDURXInitialize": pvxMSTPPortHistPMINVBPDURXInitialize,
       "pvxMSTPPortHistPMINVBPDUCFGRXValue": pvxMSTPPortHistPMINVBPDUCFGRXValue,
       "pvxMSTPPortHistPMINVBPDUCFGRXTimeStamp": pvxMSTPPortHistPMINVBPDUCFGRXTimeStamp,
       "pvxMSTPPortHistPMINVBPDUCFGRXValidity": pvxMSTPPortHistPMINVBPDUCFGRXValidity,
       "pvxMSTPPortHistPMINVBPDUCFGRXInitialize": pvxMSTPPortHistPMINVBPDUCFGRXInitialize,
       "pvxMSTPPortHistPMINVBPDUTCNRXValue": pvxMSTPPortHistPMINVBPDUTCNRXValue,
       "pvxMSTPPortHistPMINVBPDUTCNRXTimeStamp": pvxMSTPPortHistPMINVBPDUTCNRXTimeStamp,
       "pvxMSTPPortHistPMINVBPDUTCNRXValidity": pvxMSTPPortHistPMINVBPDUTCNRXValidity,
       "pvxMSTPPortHistPMINVBPDUTCNRXInitialize": pvxMSTPPortHistPMINVBPDUTCNRXInitialize,
       "pvxLAGPortCrntPMTable": pvxLAGPortCrntPMTable,
       "pvxLAGPortCrntPMEntry": pvxLAGPortCrntPMEntry,
       "pvxLAGPortCrntPMSwitchIdx": pvxLAGPortCrntPMSwitchIdx,
       "pvxLAGPortCrntPMShelfIdx": pvxLAGPortCrntPMShelfIdx,
       "pvxLAGPortCrntPMSlotIdx": pvxLAGPortCrntPMSlotIdx,
       "pvxLAGPortCrntPMTypeIdx": pvxLAGPortCrntPMTypeIdx,
       "pvxLAGPortCrntPMIdx": pvxLAGPortCrntPMIdx,
       "pvxLAGPortCrntPMIntervalTypeIdx": pvxLAGPortCrntPMIntervalTypeIdx,
       "pvxLAGPortCrntPMLACPDURXValue": pvxLAGPortCrntPMLACPDURXValue,
       "pvxLAGPortCrntPMLACPDURXTimeStamp": pvxLAGPortCrntPMLACPDURXTimeStamp,
       "pvxLAGPortCrntPMLACPDURXValidity": pvxLAGPortCrntPMLACPDURXValidity,
       "pvxLAGPortCrntPMLACPDURXInitialize": pvxLAGPortCrntPMLACPDURXInitialize,
       "pvxLAGPortCrntPMMRKPDURXValue": pvxLAGPortCrntPMMRKPDURXValue,
       "pvxLAGPortCrntPMMRKPDURXTimeStamp": pvxLAGPortCrntPMMRKPDURXTimeStamp,
       "pvxLAGPortCrntPMMRKPDURXValidity": pvxLAGPortCrntPMMRKPDURXValidity,
       "pvxLAGPortCrntPMMRKPDURXInitialize": pvxLAGPortCrntPMMRKPDURXInitialize,
       "pvxLAGPortCrntPMMRKRSPPDURXValue": pvxLAGPortCrntPMMRKRSPPDURXValue,
       "pvxLAGPortCrntPMMRKRSPPDURXTimeStamp": pvxLAGPortCrntPMMRKRSPPDURXTimeStamp,
       "pvxLAGPortCrntPMMRKRSPPDURXValidity": pvxLAGPortCrntPMMRKRSPPDURXValidity,
       "pvxLAGPortCrntPMMRKRSPPDURXInitialize": pvxLAGPortCrntPMMRKRSPPDURXInitialize,
       "pvxLAGPortCrntPMINVLACFRRXValue": pvxLAGPortCrntPMINVLACFRRXValue,
       "pvxLAGPortCrntPMINVLACFRRXTimeStamp": pvxLAGPortCrntPMINVLACFRRXTimeStamp,
       "pvxLAGPortCrntPMINVLACFRRXValidity": pvxLAGPortCrntPMINVLACFRRXValidity,
       "pvxLAGPortCrntPMINVLACFRRXInitialize": pvxLAGPortCrntPMINVLACFRRXInitialize,
       "pvxLAGPortCrntPMLACPDUTXValue": pvxLAGPortCrntPMLACPDUTXValue,
       "pvxLAGPortCrntPMLACPDUTXTimeStamp": pvxLAGPortCrntPMLACPDUTXTimeStamp,
       "pvxLAGPortCrntPMLACPDUTXValidity": pvxLAGPortCrntPMLACPDUTXValidity,
       "pvxLAGPortCrntPMLACPDUTXInitialize": pvxLAGPortCrntPMLACPDUTXInitialize,
       "pvxLAGPortCrntPMMRKPDUTXValue": pvxLAGPortCrntPMMRKPDUTXValue,
       "pvxLAGPortCrntPMMRKPDUTXTimeStamp": pvxLAGPortCrntPMMRKPDUTXTimeStamp,
       "pvxLAGPortCrntPMMRKPDUTXValidity": pvxLAGPortCrntPMMRKPDUTXValidity,
       "pvxLAGPortCrntPMMRKPDUTXInitialize": pvxLAGPortCrntPMMRKPDUTXInitialize,
       "pvxLAGPortCrntPMMRKRSPPDUTXValue": pvxLAGPortCrntPMMRKRSPPDUTXValue,
       "pvxLAGPortCrntPMMRKRSPPDUTXTimeStamp": pvxLAGPortCrntPMMRKRSPPDUTXTimeStamp,
       "pvxLAGPortCrntPMMRKRSPPDUTXValidity": pvxLAGPortCrntPMMRKRSPPDUTXValidity,
       "pvxLAGPortCrntPMMRKRSPPDUTXInitialize": pvxLAGPortCrntPMMRKRSPPDUTXInitialize,
       "pvxLAGPortHistPMTable": pvxLAGPortHistPMTable,
       "pvxLAGPortHistPMEntry": pvxLAGPortHistPMEntry,
       "pvxLAGPortHistPMSwitchIdx": pvxLAGPortHistPMSwitchIdx,
       "pvxLAGPortHistPMShelfIdx": pvxLAGPortHistPMShelfIdx,
       "pvxLAGPortHistPMSlotIdx": pvxLAGPortHistPMSlotIdx,
       "pvxLAGPortHistPMTypeIdx": pvxLAGPortHistPMTypeIdx,
       "pvxLAGPortHistPMIdx": pvxLAGPortHistPMIdx,
       "pvxLAGPortHistPMIntervalTypeIdx": pvxLAGPortHistPMIntervalTypeIdx,
       "pvxLAGPortHistPMIntervalIdx": pvxLAGPortHistPMIntervalIdx,
       "pvxLAGPortHistPMLACPDURXValue": pvxLAGPortHistPMLACPDURXValue,
       "pvxLAGPortHistPMLACPDURXTimeStamp": pvxLAGPortHistPMLACPDURXTimeStamp,
       "pvxLAGPortHistPMLACPDURXValidity": pvxLAGPortHistPMLACPDURXValidity,
       "pvxLAGPortHistPMLACPDURXInitialize": pvxLAGPortHistPMLACPDURXInitialize,
       "pvxLAGPortHistPMMRKPDURXValue": pvxLAGPortHistPMMRKPDURXValue,
       "pvxLAGPortHistPMMRKPDURXTimeStamp": pvxLAGPortHistPMMRKPDURXTimeStamp,
       "pvxLAGPortHistPMMRKPDURXValidity": pvxLAGPortHistPMMRKPDURXValidity,
       "pvxLAGPortHistPMMRKPDURXInitialize": pvxLAGPortHistPMMRKPDURXInitialize,
       "pvxLAGPortHistPMMRKRSPPDURXValue": pvxLAGPortHistPMMRKRSPPDURXValue,
       "pvxLAGPortHistPMMRKRSPPDURXTimeStamp": pvxLAGPortHistPMMRKRSPPDURXTimeStamp,
       "pvxLAGPortHistPMMRKRSPPDURXValidity": pvxLAGPortHistPMMRKRSPPDURXValidity,
       "pvxLAGPortHistPMMRKRSPPDURXInitialize": pvxLAGPortHistPMMRKRSPPDURXInitialize,
       "pvxLAGPortHistPMINVLACFRRXValue": pvxLAGPortHistPMINVLACFRRXValue,
       "pvxLAGPortHistPMINVLACFRRXTimeStamp": pvxLAGPortHistPMINVLACFRRXTimeStamp,
       "pvxLAGPortHistPMINVLACFRRXValidity": pvxLAGPortHistPMINVLACFRRXValidity,
       "pvxLAGPortHistPMINVLACFRRXInitialize": pvxLAGPortHistPMINVLACFRRXInitialize,
       "pvxLAGPortHistPMLACPDUTXValue": pvxLAGPortHistPMLACPDUTXValue,
       "pvxLAGPortHistPMLACPDUTXTimeStamp": pvxLAGPortHistPMLACPDUTXTimeStamp,
       "pvxLAGPortHistPMLACPDUTXValidity": pvxLAGPortHistPMLACPDUTXValidity,
       "pvxLAGPortHistPMLACPDUTXInitialize": pvxLAGPortHistPMLACPDUTXInitialize,
       "pvxLAGPortHistPMMRKPDUTXValue": pvxLAGPortHistPMMRKPDUTXValue,
       "pvxLAGPortHistPMMRKPDUTXTimeStamp": pvxLAGPortHistPMMRKPDUTXTimeStamp,
       "pvxLAGPortHistPMMRKPDUTXValidity": pvxLAGPortHistPMMRKPDUTXValidity,
       "pvxLAGPortHistPMMRKPDUTXInitialize": pvxLAGPortHistPMMRKPDUTXInitialize,
       "pvxLAGPortHistPMMRKRSPPDUTXValue": pvxLAGPortHistPMMRKRSPPDUTXValue,
       "pvxLAGPortHistPMMRKRSPPDUTXTimeStamp": pvxLAGPortHistPMMRKRSPPDUTXTimeStamp,
       "pvxLAGPortHistPMMRKRSPPDUTXValidity": pvxLAGPortHistPMMRKRSPPDUTXValidity,
       "pvxLAGPortHistPMMRKRSPPDUTXInitialize": pvxLAGPortHistPMMRKRSPPDUTXInitialize,
       "pvxESrvcCrntPMTable": pvxESrvcCrntPMTable,
       "pvxESrvcCrntPMEntry": pvxESrvcCrntPMEntry,
       "pvxESrvcCrntPMSwitchIdx": pvxESrvcCrntPMSwitchIdx,
       "pvxESrvcCrntPMESrvcNameIdx": pvxESrvcCrntPMESrvcNameIdx,
       "pvxESrvcCrntPMIntervalTypeIdx": pvxESrvcCrntPMIntervalTypeIdx,
       "pvxESrvcCrntPMUASValue": pvxESrvcCrntPMUASValue,
       "pvxESrvcCrntPMUASTimeStamp": pvxESrvcCrntPMUASTimeStamp,
       "pvxESrvcCrntPMUASValidity": pvxESrvcCrntPMUASValidity,
       "pvxESrvcCrntPMUASInitialize": pvxESrvcCrntPMUASInitialize,
       "pvxESrvcHistPMTable": pvxESrvcHistPMTable,
       "pvxESrvcHistPMEntry": pvxESrvcHistPMEntry,
       "pvxESrvcHistPMSwitchIdx": pvxESrvcHistPMSwitchIdx,
       "pvxESrvcHistPMESrvcNameIdx": pvxESrvcHistPMESrvcNameIdx,
       "pvxESrvcHistPMIntervalTypeIdx": pvxESrvcHistPMIntervalTypeIdx,
       "pvxESrvcHistPMIntervalIdx": pvxESrvcHistPMIntervalIdx,
       "pvxESrvcHistPMUASValue": pvxESrvcHistPMUASValue,
       "pvxESrvcHistPMUASTimeStamp": pvxESrvcHistPMUASTimeStamp,
       "pvxESrvcHistPMUASValidity": pvxESrvcHistPMUASValidity,
       "pvxESrvcHistPMUASInitialize": pvxESrvcHistPMUASInitialize,
       "pvxESrvcBWPrflCrntPMTable": pvxESrvcBWPrflCrntPMTable,
       "pvxESrvcBWPrflCrntPMEntry": pvxESrvcBWPrflCrntPMEntry,
       "pvxESrvcBWPrflCrntPMSwitchIdx": pvxESrvcBWPrflCrntPMSwitchIdx,
       "pvxESrvcBWPrflCrntPMShelfIdx": pvxESrvcBWPrflCrntPMShelfIdx,
       "pvxESrvcBWPrflCrntPMSlotIdx": pvxESrvcBWPrflCrntPMSlotIdx,
       "pvxESrvcBWPrflCrntPMPortTypeIdx": pvxESrvcBWPrflCrntPMPortTypeIdx,
       "pvxESrvcBWPrflCrntPMPortIdx": pvxESrvcBWPrflCrntPMPortIdx,
       "pvxESrvcBWPrflCrntPMESrvcNameIdx": pvxESrvcBWPrflCrntPMESrvcNameIdx,
       "pvxESrvcBWPrflCrntPMPlcyNameIdx": pvxESrvcBWPrflCrntPMPlcyNameIdx,
       "pvxESrvcBWPrflCrntPMClsMapNameIdx": pvxESrvcBWPrflCrntPMClsMapNameIdx,
       "pvxESrvcBWPrflCrntPMDirectionIdx": pvxESrvcBWPrflCrntPMDirectionIdx,
       "pvxESrvcBWPrflCrntPMIntervalTypeIdx": pvxESrvcBWPrflCrntPMIntervalTypeIdx,
       "pvxESrvcBWPrflCrntPMOctetsTotalValue": pvxESrvcBWPrflCrntPMOctetsTotalValue,
       "pvxESrvcBWPrflCrntPMOctetsTotalTimeStamp": pvxESrvcBWPrflCrntPMOctetsTotalTimeStamp,
       "pvxESrvcBWPrflCrntPMOctetsTotalValidity": pvxESrvcBWPrflCrntPMOctetsTotalValidity,
       "pvxESrvcBWPrflCrntPMOctetsTotalInitialize": pvxESrvcBWPrflCrntPMOctetsTotalInitialize,
       "pvxESrvcBWPrflCrntPMOctetsVltValue": pvxESrvcBWPrflCrntPMOctetsVltValue,
       "pvxESrvcBWPrflCrntPMOctetsVltTimeStamp": pvxESrvcBWPrflCrntPMOctetsVltTimeStamp,
       "pvxESrvcBWPrflCrntPMOctetsVltValidity": pvxESrvcBWPrflCrntPMOctetsVltValidity,
       "pvxESrvcBWPrflCrntPMOctetsVltInitialize": pvxESrvcBWPrflCrntPMOctetsVltInitialize,
       "pvxESrvcBWPrflCrntPMOctetsCnfExcValue": pvxESrvcBWPrflCrntPMOctetsCnfExcValue,
       "pvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp": pvxESrvcBWPrflCrntPMOctetsCnfExcTimeStamp,
       "pvxESrvcBWPrflCrntPMOctetsCnfExcValidity": pvxESrvcBWPrflCrntPMOctetsCnfExcValidity,
       "pvxESrvcBWPrflCrntPMOctetsCnfExcInitialize": pvxESrvcBWPrflCrntPMOctetsCnfExcInitialize,
       "pvxESrvcBWPrflCrntPMBDWUtlzValue": pvxESrvcBWPrflCrntPMBDWUtlzValue,
       "pvxESrvcBWPrflCrntPMBDWUtlzTimeStamp": pvxESrvcBWPrflCrntPMBDWUtlzTimeStamp,
       "pvxESrvcBWPrflCrntPMBDWUtlzValidity": pvxESrvcBWPrflCrntPMBDWUtlzValidity,
       "pvxESrvcBWPrflCrntPMBDWUtlzInitialize": pvxESrvcBWPrflCrntPMBDWUtlzInitialize,
       "pvxESrvcBWPrflHistPMTable": pvxESrvcBWPrflHistPMTable,
       "pvxESrvcBWPrflHistPMEntry": pvxESrvcBWPrflHistPMEntry,
       "pvxESrvcBWPrflHistPMSwitchIdx": pvxESrvcBWPrflHistPMSwitchIdx,
       "pvxESrvcBWPrflHistPMShelfIdx": pvxESrvcBWPrflHistPMShelfIdx,
       "pvxESrvcBWPrflHistPMSlotIdx": pvxESrvcBWPrflHistPMSlotIdx,
       "pvxESrvcBWPrflHistPMPortTypeIdx": pvxESrvcBWPrflHistPMPortTypeIdx,
       "pvxESrvcBWPrflHistPMPortIdx": pvxESrvcBWPrflHistPMPortIdx,
       "pvxESrvcBWPrflHistPMESrvcNameIdx": pvxESrvcBWPrflHistPMESrvcNameIdx,
       "pvxESrvcBWPrflHistPMPlcyNameIdx": pvxESrvcBWPrflHistPMPlcyNameIdx,
       "pvxESrvcBWPrflHistPMClsMapNameIdx": pvxESrvcBWPrflHistPMClsMapNameIdx,
       "pvxESrvcBWPrflHistPMDirectionIdx": pvxESrvcBWPrflHistPMDirectionIdx,
       "pvxESrvcBWPrflHistPMIntervalTypeIdx": pvxESrvcBWPrflHistPMIntervalTypeIdx,
       "pvxESrvcBWPrflHistPMIntervalIdx": pvxESrvcBWPrflHistPMIntervalIdx,
       "pvxESrvcBWPrflHistPMOctetsTotalValue": pvxESrvcBWPrflHistPMOctetsTotalValue,
       "pvxESrvcBWPrflHistPMOctetsTotalTimeStamp": pvxESrvcBWPrflHistPMOctetsTotalTimeStamp,
       "pvxESrvcBWPrflHistPMOctetsTotalValidity": pvxESrvcBWPrflHistPMOctetsTotalValidity,
       "pvxESrvcBWPrflHistPMOctetsTotalInitialize": pvxESrvcBWPrflHistPMOctetsTotalInitialize,
       "pvxESrvcBWPrflHistPMOctetsVltValue": pvxESrvcBWPrflHistPMOctetsVltValue,
       "pvxESrvcBWPrflHistPMOctetsVltTimeStamp": pvxESrvcBWPrflHistPMOctetsVltTimeStamp,
       "pvxESrvcBWPrflHistPMOctetsVltValidity": pvxESrvcBWPrflHistPMOctetsVltValidity,
       "pvxESrvcBWPrflHistPMOctetsVltInitialize": pvxESrvcBWPrflHistPMOctetsVltInitialize,
       "pvxESrvcBWPrflHistPMOctetsCnfExcValue": pvxESrvcBWPrflHistPMOctetsCnfExcValue,
       "pvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp": pvxESrvcBWPrflHistPMOctetsCnfExcTimeStamp,
       "pvxESrvcBWPrflHistPMOctetsCnfExcValidity": pvxESrvcBWPrflHistPMOctetsCnfExcValidity,
       "pvxESrvcBWPrflHistPMOctetsCnfExcInitialize": pvxESrvcBWPrflHistPMOctetsCnfExcInitialize,
       "pvxESrvcBWPrflHistPMBDWUtlzValue": pvxESrvcBWPrflHistPMBDWUtlzValue,
       "pvxESrvcBWPrflHistPMBDWUtlzTimeStamp": pvxESrvcBWPrflHistPMBDWUtlzTimeStamp,
       "pvxESrvcBWPrflHistPMBDWUtlzValidity": pvxESrvcBWPrflHistPMBDWUtlzValidity,
       "pvxESrvcBWPrflHistPMBDWUtlzInitialize": pvxESrvcBWPrflHistPMBDWUtlzInitialize,
       "pvxESrvcBWPrflPMThresholdTable": pvxESrvcBWPrflPMThresholdTable,
       "pvxESrvcBWPrflPMThresholdEntry": pvxESrvcBWPrflPMThresholdEntry,
       "pvxESrvcBWPrflPMThresholdSwitchIdx": pvxESrvcBWPrflPMThresholdSwitchIdx,
       "pvxESrvcBWPrflPMThresholdShelfIdx": pvxESrvcBWPrflPMThresholdShelfIdx,
       "pvxESrvcBWPrflPMThresholdSlotIdx": pvxESrvcBWPrflPMThresholdSlotIdx,
       "pvxESrvcBWPrflPMThresholdPortTypeIdx": pvxESrvcBWPrflPMThresholdPortTypeIdx,
       "pvxESrvcBWPrflPMThresholdPortIdx": pvxESrvcBWPrflPMThresholdPortIdx,
       "pvxESrvcBWPrflPMThresholdESrvcNameIdx": pvxESrvcBWPrflPMThresholdESrvcNameIdx,
       "pvxESrvcBWPrflPMThresholdPlcyNameIdx": pvxESrvcBWPrflPMThresholdPlcyNameIdx,
       "pvxESrvcBWPrflPMThresholdClsMapNameIdx": pvxESrvcBWPrflPMThresholdClsMapNameIdx,
       "pvxESrvcBWPrflPMThresholdDirectionIdx": pvxESrvcBWPrflPMThresholdDirectionIdx,
       "pvxESrvcBWPrflPMThresholdLevelTypeIdx": pvxESrvcBWPrflPMThresholdLevelTypeIdx,
       "pvxESrvcBWPrflPMThresholdBDWUtlzValue": pvxESrvcBWPrflPMThresholdBDWUtlzValue,
       "pvxERPSPortCrntPMTable": pvxERPSPortCrntPMTable,
       "pvxERPSPortCrntPMEntry": pvxERPSPortCrntPMEntry,
       "pvxERPSPortCrntPMSwitchIdx": pvxERPSPortCrntPMSwitchIdx,
       "pvxERPSPortCrntPMShelfIdx": pvxERPSPortCrntPMShelfIdx,
       "pvxERPSPortCrntPMSlotIdx": pvxERPSPortCrntPMSlotIdx,
       "pvxERPSPortCrntPMTypeIdx": pvxERPSPortCrntPMTypeIdx,
       "pvxERPSPortCrntPMPortIdx": pvxERPSPortCrntPMPortIdx,
       "pvxERPSPortCrntPMIntervalTypeIdx": pvxERPSPortCrntPMIntervalTypeIdx,
       "pvxERPSPortCrntPMPduTxValue": pvxERPSPortCrntPMPduTxValue,
       "pvxERPSPortCrntPMPduTxTimeStamp": pvxERPSPortCrntPMPduTxTimeStamp,
       "pvxERPSPortCrntPMPduTxValidity": pvxERPSPortCrntPMPduTxValidity,
       "pvxERPSPortCrntPMPduTxInitialize": pvxERPSPortCrntPMPduTxInitialize,
       "pvxERPSPortCrntPMPduRxValue": pvxERPSPortCrntPMPduRxValue,
       "pvxERPSPortCrntPMPduRxTimeStamp": pvxERPSPortCrntPMPduRxTimeStamp,
       "pvxERPSPortCrntPMPduRxValidity": pvxERPSPortCrntPMPduRxValidity,
       "pvxERPSPortCrntPMPduRxInitialize": pvxERPSPortCrntPMPduRxInitialize,
       "pvxERPSPortCrntPMPduDiscardValue": pvxERPSPortCrntPMPduDiscardValue,
       "pvxERPSPortCrntPMPduDiscardTimeStamp": pvxERPSPortCrntPMPduDiscardTimeStamp,
       "pvxERPSPortCrntPMPduDiscardValidity": pvxERPSPortCrntPMPduDiscardValidity,
       "pvxERPSPortCrntPMPduDiscardInitialize": pvxERPSPortCrntPMPduDiscardInitialize,
       "pvxERPSPortCrntPMBlockedValue": pvxERPSPortCrntPMBlockedValue,
       "pvxERPSPortCrntPMBlockedTimeStamp": pvxERPSPortCrntPMBlockedTimeStamp,
       "pvxERPSPortCrntPMBlockedValidity": pvxERPSPortCrntPMBlockedValidity,
       "pvxERPSPortCrntPMBlockedInitialize": pvxERPSPortCrntPMBlockedInitialize,
       "pvxERPSPortCrntPMUnblockedValue": pvxERPSPortCrntPMUnblockedValue,
       "pvxERPSPortCrntPMUnblockedTimeStamp": pvxERPSPortCrntPMUnblockedTimeStamp,
       "pvxERPSPortCrntPMUnblockedValidity": pvxERPSPortCrntPMUnblockedValidity,
       "pvxERPSPortCrntPMUnblockedInitialize": pvxERPSPortCrntPMUnblockedInitialize,
       "pvxERPSPortCrntPMFailuresValue": pvxERPSPortCrntPMFailuresValue,
       "pvxERPSPortCrntPMFailuresTimeStamp": pvxERPSPortCrntPMFailuresTimeStamp,
       "pvxERPSPortCrntPMFailuresValidity": pvxERPSPortCrntPMFailuresValidity,
       "pvxERPSPortCrntPMFailuresInitialize": pvxERPSPortCrntPMFailuresInitialize,
       "pvxERPSPortCrntPMRecoveriesValue": pvxERPSPortCrntPMRecoveriesValue,
       "pvxERPSPortCrntPMRecoveriesTimeStamp": pvxERPSPortCrntPMRecoveriesTimeStamp,
       "pvxERPSPortCrntPMRecoveriesValidity": pvxERPSPortCrntPMRecoveriesValidity,
       "pvxERPSPortCrntPMRecoveriesInitialize": pvxERPSPortCrntPMRecoveriesInitialize,
       "pvxERPSPortCrntPMNrPduTxValue": pvxERPSPortCrntPMNrPduTxValue,
       "pvxERPSPortCrntPMNrPduTxTimeStamp": pvxERPSPortCrntPMNrPduTxTimeStamp,
       "pvxERPSPortCrntPMNrPduTxValidity": pvxERPSPortCrntPMNrPduTxValidity,
       "pvxERPSPortCrntPMNrPduTxInitialize": pvxERPSPortCrntPMNrPduTxInitialize,
       "pvxERPSPortCrntPMNrPduRxValue": pvxERPSPortCrntPMNrPduRxValue,
       "pvxERPSPortCrntPMNrPduRxTimeStamp": pvxERPSPortCrntPMNrPduRxTimeStamp,
       "pvxERPSPortCrntPMNrPduRxValidity": pvxERPSPortCrntPMNrPduRxValidity,
       "pvxERPSPortCrntPMNrPduRxInitialize": pvxERPSPortCrntPMNrPduRxInitialize,
       "pvxERPSPortCrntPMNrrbPduTxValue": pvxERPSPortCrntPMNrrbPduTxValue,
       "pvxERPSPortCrntPMNrrbPduTxTimeStamp": pvxERPSPortCrntPMNrrbPduTxTimeStamp,
       "pvxERPSPortCrntPMNrrbPduTxValidity": pvxERPSPortCrntPMNrrbPduTxValidity,
       "pvxERPSPortCrntPMNrrbPduTxInitialize": pvxERPSPortCrntPMNrrbPduTxInitialize,
       "pvxERPSPortCrntPMNrrbPduRxValue": pvxERPSPortCrntPMNrrbPduRxValue,
       "pvxERPSPortCrntPMNrrbPduRxTimeStamp": pvxERPSPortCrntPMNrrbPduRxTimeStamp,
       "pvxERPSPortCrntPMNrrbPduRxValidity": pvxERPSPortCrntPMNrrbPduRxValidity,
       "pvxERPSPortCrntPMNrrbPduRxInitialize": pvxERPSPortCrntPMNrrbPduRxInitialize,
       "pvxERPSPortCrntPMSfPduTxValue": pvxERPSPortCrntPMSfPduTxValue,
       "pvxERPSPortCrntPMSfPduTxTimeStamp": pvxERPSPortCrntPMSfPduTxTimeStamp,
       "pvxERPSPortCrntPMSfPduTxValidity": pvxERPSPortCrntPMSfPduTxValidity,
       "pvxERPSPortCrntPMSfPduTxInitialize": pvxERPSPortCrntPMSfPduTxInitialize,
       "pvxERPSPortCrntPMSfPduRxValue": pvxERPSPortCrntPMSfPduRxValue,
       "pvxERPSPortCrntPMSfPduRxTimeStamp": pvxERPSPortCrntPMSfPduRxTimeStamp,
       "pvxERPSPortCrntPMSfPduRxValidity": pvxERPSPortCrntPMSfPduRxValidity,
       "pvxERPSPortCrntPMSfPduRxInitialize": pvxERPSPortCrntPMSfPduRxInitialize,
       "pvxERPSPortCrntPMFsPduTxValue": pvxERPSPortCrntPMFsPduTxValue,
       "pvxERPSPortCrntPMFsPduTxTimeStamp": pvxERPSPortCrntPMFsPduTxTimeStamp,
       "pvxERPSPortCrntPMFsPduTxValidity": pvxERPSPortCrntPMFsPduTxValidity,
       "pvxERPSPortCrntPMFsPduTxInitialize": pvxERPSPortCrntPMFsPduTxInitialize,
       "pvxERPSPortCrntPMFsPduRxValue": pvxERPSPortCrntPMFsPduRxValue,
       "pvxERPSPortCrntPMFsPduRxTimeStamp": pvxERPSPortCrntPMFsPduRxTimeStamp,
       "pvxERPSPortCrntPMFsPduRxValidity": pvxERPSPortCrntPMFsPduRxValidity,
       "pvxERPSPortCrntPMFsPduRxInitialize": pvxERPSPortCrntPMFsPduRxInitialize,
       "pvxERPSPortCrntPMMsPduTxValue": pvxERPSPortCrntPMMsPduTxValue,
       "pvxERPSPortCrntPMMsPduTxTimeStamp": pvxERPSPortCrntPMMsPduTxTimeStamp,
       "pvxERPSPortCrntPMMsPduTxValidity": pvxERPSPortCrntPMMsPduTxValidity,
       "pvxERPSPortCrntPMMsPduTxInitialize": pvxERPSPortCrntPMMsPduTxInitialize,
       "pvxERPSPortCrntPMMsPduRxValue": pvxERPSPortCrntPMMsPduRxValue,
       "pvxERPSPortCrntPMMsPduRxTimeStamp": pvxERPSPortCrntPMMsPduRxTimeStamp,
       "pvxERPSPortCrntPMMsPduRxValidity": pvxERPSPortCrntPMMsPduRxValidity,
       "pvxERPSPortCrntPMMsPduRxInitialize": pvxERPSPortCrntPMMsPduRxInitialize,
       "pvxERPSPortCrntPMEventPduTxValue": pvxERPSPortCrntPMEventPduTxValue,
       "pvxERPSPortCrntPMEventPduTxTimeStamp": pvxERPSPortCrntPMEventPduTxTimeStamp,
       "pvxERPSPortCrntPMEventPduTxValidity": pvxERPSPortCrntPMEventPduTxValidity,
       "pvxERPSPortCrntPMEventPduTxInitialize": pvxERPSPortCrntPMEventPduTxInitialize,
       "pvxERPSPortCrntPMEventPduRxValue": pvxERPSPortCrntPMEventPduRxValue,
       "pvxERPSPortCrntPMEventPduRxTimeStamp": pvxERPSPortCrntPMEventPduRxTimeStamp,
       "pvxERPSPortCrntPMEventPduRxValidity": pvxERPSPortCrntPMEventPduRxValidity,
       "pvxERPSPortCrntPMEventPduRxInitialize": pvxERPSPortCrntPMEventPduRxInitialize,
       "pvxERPSPortCrntPMVersionDiscardValue": pvxERPSPortCrntPMVersionDiscardValue,
       "pvxERPSPortCrntPMVersionDiscardTimeStamp": pvxERPSPortCrntPMVersionDiscardTimeStamp,
       "pvxERPSPortCrntPMVersionDiscardValidity": pvxERPSPortCrntPMVersionDiscardValidity,
       "pvxERPSPortCrntPMVersionDiscardInitialize": pvxERPSPortCrntPMVersionDiscardInitialize,
       "pvxERPSPortHistPMTable": pvxERPSPortHistPMTable,
       "pvxERPSPortHistPMEntry": pvxERPSPortHistPMEntry,
       "pvxERPSPortHistPMSwitchIdx": pvxERPSPortHistPMSwitchIdx,
       "pvxERPSPortHistPMShelfIdx": pvxERPSPortHistPMShelfIdx,
       "pvxERPSPortHistPMSlotIdx": pvxERPSPortHistPMSlotIdx,
       "pvxERPSPortHistPMTypeIdx": pvxERPSPortHistPMTypeIdx,
       "pvxERPSPortHistPMPortIdx": pvxERPSPortHistPMPortIdx,
       "pvxERPSPortHistPMIntervalTypeIdx": pvxERPSPortHistPMIntervalTypeIdx,
       "pvxERPSPortHistPMIntervalIdx": pvxERPSPortHistPMIntervalIdx,
       "pvxERPSPortHistPMPduTxValue": pvxERPSPortHistPMPduTxValue,
       "pvxERPSPortHistPMPduTxTimeStamp": pvxERPSPortHistPMPduTxTimeStamp,
       "pvxERPSPortHistPMPduTxValidity": pvxERPSPortHistPMPduTxValidity,
       "pvxERPSPortHistPMPduTxInitialize": pvxERPSPortHistPMPduTxInitialize,
       "pvxERPSPortHistPMPduRxValue": pvxERPSPortHistPMPduRxValue,
       "pvxERPSPortHistPMPduRxTimeStamp": pvxERPSPortHistPMPduRxTimeStamp,
       "pvxERPSPortHistPMPduRxValidity": pvxERPSPortHistPMPduRxValidity,
       "pvxERPSPortHistPMPduRxInitialize": pvxERPSPortHistPMPduRxInitialize,
       "pvxERPSPortHistPMPduDiscardValue": pvxERPSPortHistPMPduDiscardValue,
       "pvxERPSPortHistPMPduDiscardTimeStamp": pvxERPSPortHistPMPduDiscardTimeStamp,
       "pvxERPSPortHistPMPduDiscardValidity": pvxERPSPortHistPMPduDiscardValidity,
       "pvxERPSPortHistPMPduDiscardInitialize": pvxERPSPortHistPMPduDiscardInitialize,
       "pvxERPSPortHistPMBlockedValue": pvxERPSPortHistPMBlockedValue,
       "pvxERPSPortHistPMBlockedTimeStamp": pvxERPSPortHistPMBlockedTimeStamp,
       "pvxERPSPortHistPMBlockedValidity": pvxERPSPortHistPMBlockedValidity,
       "pvxERPSPortHistPMBlockedInitialize": pvxERPSPortHistPMBlockedInitialize,
       "pvxERPSPortHistPMUnblockedValue": pvxERPSPortHistPMUnblockedValue,
       "pvxERPSPortHistPMUnblockedTimeStamp": pvxERPSPortHistPMUnblockedTimeStamp,
       "pvxERPSPortHistPMUnblockedValidity": pvxERPSPortHistPMUnblockedValidity,
       "pvxERPSPortHistPMUnblockedInitialize": pvxERPSPortHistPMUnblockedInitialize,
       "pvxERPSPortHistPMFailuresValue": pvxERPSPortHistPMFailuresValue,
       "pvxERPSPortHistPMFailuresTimeStamp": pvxERPSPortHistPMFailuresTimeStamp,
       "pvxERPSPortHistPMFailuresValidity": pvxERPSPortHistPMFailuresValidity,
       "pvxERPSPortHistPMFailuresInitialize": pvxERPSPortHistPMFailuresInitialize,
       "pvxERPSPortHistPMRecoveriesValue": pvxERPSPortHistPMRecoveriesValue,
       "pvxERPSPortHistPMRecoveriesTimeStamp": pvxERPSPortHistPMRecoveriesTimeStamp,
       "pvxERPSPortHistPMRecoveriesValidity": pvxERPSPortHistPMRecoveriesValidity,
       "pvxERPSPortHistPMRecoveriesInitialize": pvxERPSPortHistPMRecoveriesInitialize,
       "pvxERPSPortHistPMNrPduTxValue": pvxERPSPortHistPMNrPduTxValue,
       "pvxERPSPortHistPMNrPduTxTimeStamp": pvxERPSPortHistPMNrPduTxTimeStamp,
       "pvxERPSPortHistPMNrPduTxValidity": pvxERPSPortHistPMNrPduTxValidity,
       "pvxERPSPortHistPMNrPduTxInitialize": pvxERPSPortHistPMNrPduTxInitialize,
       "pvxERPSPortHistPMNrPduRxValue": pvxERPSPortHistPMNrPduRxValue,
       "pvxERPSPortHistPMNrPduRxTimeStamp": pvxERPSPortHistPMNrPduRxTimeStamp,
       "pvxERPSPortHistPMNrPduRxValidity": pvxERPSPortHistPMNrPduRxValidity,
       "pvxERPSPortHistPMNrPduRxInitialize": pvxERPSPortHistPMNrPduRxInitialize,
       "pvxERPSPortHistPMNrrbPduTxValue": pvxERPSPortHistPMNrrbPduTxValue,
       "pvxERPSPortHistPMNrrbPduTxTimeStamp": pvxERPSPortHistPMNrrbPduTxTimeStamp,
       "pvxERPSPortHistPMNrrbPduTxValidity": pvxERPSPortHistPMNrrbPduTxValidity,
       "pvxERPSPortHistPMNrrbPduTxInitialize": pvxERPSPortHistPMNrrbPduTxInitialize,
       "pvxERPSPortHistPMNrrbPduRxValue": pvxERPSPortHistPMNrrbPduRxValue,
       "pvxERPSPortHistPMNrrbPduRxTimeStamp": pvxERPSPortHistPMNrrbPduRxTimeStamp,
       "pvxERPSPortHistPMNrrbPduRxValidity": pvxERPSPortHistPMNrrbPduRxValidity,
       "pvxERPSPortHistPMNrrbPduRxInitialize": pvxERPSPortHistPMNrrbPduRxInitialize,
       "pvxERPSPortHistPMSfPduTxValue": pvxERPSPortHistPMSfPduTxValue,
       "pvxERPSPortHistPMSfPduTxTimeStamp": pvxERPSPortHistPMSfPduTxTimeStamp,
       "pvxERPSPortHistPMSfPduTxValidity": pvxERPSPortHistPMSfPduTxValidity,
       "pvxERPSPortHistPMSfPduTxInitialize": pvxERPSPortHistPMSfPduTxInitialize,
       "pvxERPSPortHistPMSfPduRxValue": pvxERPSPortHistPMSfPduRxValue,
       "pvxERPSPortHistPMSfPduRxTimeStamp": pvxERPSPortHistPMSfPduRxTimeStamp,
       "pvxERPSPortHistPMSfPduRxValidity": pvxERPSPortHistPMSfPduRxValidity,
       "pvxERPSPortHistPMSfPduRxInitialize": pvxERPSPortHistPMSfPduRxInitialize,
       "pvxERPSPortHistPMFsPduTxValue": pvxERPSPortHistPMFsPduTxValue,
       "pvxERPSPortHistPMFsPduTxTimeStamp": pvxERPSPortHistPMFsPduTxTimeStamp,
       "pvxERPSPortHistPMFsPduTxValidity": pvxERPSPortHistPMFsPduTxValidity,
       "pvxERPSPortHistPMFsPduTxInitialize": pvxERPSPortHistPMFsPduTxInitialize,
       "pvxERPSPortHistPMFsPduRxValue": pvxERPSPortHistPMFsPduRxValue,
       "pvxERPSPortHistPMFsPduRxTimeStamp": pvxERPSPortHistPMFsPduRxTimeStamp,
       "pvxERPSPortHistPMFsPduRxValidity": pvxERPSPortHistPMFsPduRxValidity,
       "pvxERPSPortHistPMFsPduRxInitialize": pvxERPSPortHistPMFsPduRxInitialize,
       "pvxERPSPortHistPMMsPduTxValue": pvxERPSPortHistPMMsPduTxValue,
       "pvxERPSPortHistPMMsPduTxTimeStamp": pvxERPSPortHistPMMsPduTxTimeStamp,
       "pvxERPSPortHistPMMsPduTxValidity": pvxERPSPortHistPMMsPduTxValidity,
       "pvxERPSPortHistPMMsPduTxInitialize": pvxERPSPortHistPMMsPduTxInitialize,
       "pvxERPSPortHistPMMsPduRxValue": pvxERPSPortHistPMMsPduRxValue,
       "pvxERPSPortHistPMMsPduRxTimeStamp": pvxERPSPortHistPMMsPduRxTimeStamp,
       "pvxERPSPortHistPMMsPduRxValidity": pvxERPSPortHistPMMsPduRxValidity,
       "pvxERPSPortHistPMMsPduRxInitialize": pvxERPSPortHistPMMsPduRxInitialize,
       "pvxERPSPortHistPMEventPduTxValue": pvxERPSPortHistPMEventPduTxValue,
       "pvxERPSPortHistPMEventPduTxTimeStamp": pvxERPSPortHistPMEventPduTxTimeStamp,
       "pvxERPSPortHistPMEventPduTxValidity": pvxERPSPortHistPMEventPduTxValidity,
       "pvxERPSPortHistPMEventPduTxInitialize": pvxERPSPortHistPMEventPduTxInitialize,
       "pvxERPSPortHistPMEventPduRxValue": pvxERPSPortHistPMEventPduRxValue,
       "pvxERPSPortHistPMEventPduRxTimeStamp": pvxERPSPortHistPMEventPduRxTimeStamp,
       "pvxERPSPortHistPMEventPduRxValidity": pvxERPSPortHistPMEventPduRxValidity,
       "pvxERPSPortHistPMEventPduRxInitialize": pvxERPSPortHistPMEventPduRxInitialize,
       "pvxERPSPortHistPMVersionDiscardValue": pvxERPSPortHistPMVersionDiscardValue,
       "pvxERPSPortHistPMVersionDiscardTimeStamp": pvxERPSPortHistPMVersionDiscardTimeStamp,
       "pvxERPSPortHistPMVersionDiscardValidity": pvxERPSPortHistPMVersionDiscardValidity,
       "pvxERPSPortHistPMVersionDiscardInitialize": pvxERPSPortHistPMVersionDiscardInitialize,
       "pvxEServiceSlaCrntPMTable": pvxEServiceSlaCrntPMTable,
       "pvxEServiceSlaCrntPMEntry": pvxEServiceSlaCrntPMEntry,
       "pvxEServiceSlaCrntPMSwitchIdx": pvxEServiceSlaCrntPMSwitchIdx,
       "pvxEServiceSlaCrntPMShelfIdx": pvxEServiceSlaCrntPMShelfIdx,
       "pvxEServiceSlaCrntPMSlotIdx": pvxEServiceSlaCrntPMSlotIdx,
       "pvxEServiceSlaCrntPMPortTypeIdx": pvxEServiceSlaCrntPMPortTypeIdx,
       "pvxEServiceSlaCrntPMPortIdx": pvxEServiceSlaCrntPMPortIdx,
       "pvxEServiceSlaCrntPMESName": pvxEServiceSlaCrntPMESName,
       "pvxEServiceSlaCrntPMRMepId": pvxEServiceSlaCrntPMRMepId,
       "pvxEServiceSlaCrntPMIntervalTypeIdx": pvxEServiceSlaCrntPMIntervalTypeIdx,
       "pvxEServiceSlaCrntPMNearEndFrameLoss": pvxEServiceSlaCrntPMNearEndFrameLoss,
       "pvxEServiceSlaCrntPMNearEndFrameLossTimeStamp": pvxEServiceSlaCrntPMNearEndFrameLossTimeStamp,
       "pvxEServiceSlaCrntPMNearEndFrameLossValidity": pvxEServiceSlaCrntPMNearEndFrameLossValidity,
       "pvxEServiceSlaCrntPMNearEndFrameLossInitialize": pvxEServiceSlaCrntPMNearEndFrameLossInitialize,
       "pvxEServiceSlaCrntPMFarEndFrameLoss": pvxEServiceSlaCrntPMFarEndFrameLoss,
       "pvxEServiceSlaCrntPMFarEndFrameLossTimeStamp": pvxEServiceSlaCrntPMFarEndFrameLossTimeStamp,
       "pvxEServiceSlaCrntPMFarEndFrameLossValidity": pvxEServiceSlaCrntPMFarEndFrameLossValidity,
       "pvxEServiceSlaCrntPMFarEndFrameLossInitialize": pvxEServiceSlaCrntPMFarEndFrameLossInitialize,
       "pvxEServiceSlaCrntPM2WayDelayMinimum": pvxEServiceSlaCrntPM2WayDelayMinimum,
       "pvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp": pvxEServiceSlaCrntPM2WayDelayMinimumTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayMinimumValidity": pvxEServiceSlaCrntPM2WayDelayMinimumValidity,
       "pvxEServiceSlaCrntPM2WayDelayMinimumInitialize": pvxEServiceSlaCrntPM2WayDelayMinimumInitialize,
       "pvxEServiceSlaCrntPM2WayDelayMaximum": pvxEServiceSlaCrntPM2WayDelayMaximum,
       "pvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp": pvxEServiceSlaCrntPM2WayDelayMaximumTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayMaximumValidity": pvxEServiceSlaCrntPM2WayDelayMaximumValidity,
       "pvxEServiceSlaCrntPM2WayDelayMaximumInitialize": pvxEServiceSlaCrntPM2WayDelayMaximumInitialize,
       "pvxEServiceSlaCrntPM2WayDelayAverage": pvxEServiceSlaCrntPM2WayDelayAverage,
       "pvxEServiceSlaCrntPM2WayDelayAverageTimeStamp": pvxEServiceSlaCrntPM2WayDelayAverageTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayAverageValidity": pvxEServiceSlaCrntPM2WayDelayAverageValidity,
       "pvxEServiceSlaCrntPM2WayDelayAverageInitialize": pvxEServiceSlaCrntPM2WayDelayAverageInitialize,
       "pvxEServiceSlaCrntPM2WayDelayVariationMinimum": pvxEServiceSlaCrntPM2WayDelayVariationMinimum,
       "pvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp": pvxEServiceSlaCrntPM2WayDelayVariationMinimumTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity": pvxEServiceSlaCrntPM2WayDelayVariationMinimumValidity,
       "pvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize": pvxEServiceSlaCrntPM2WayDelayVariationMinimumInitialize,
       "pvxEServiceSlaCrntPM2WayDelayVariationMaximum": pvxEServiceSlaCrntPM2WayDelayVariationMaximum,
       "pvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp": pvxEServiceSlaCrntPM2WayDelayVariationMaximumTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity": pvxEServiceSlaCrntPM2WayDelayVariationMaximumValidity,
       "pvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize": pvxEServiceSlaCrntPM2WayDelayVariationMaximumInitialize,
       "pvxEServiceSlaCrntPM2WayDelayVariationAverage": pvxEServiceSlaCrntPM2WayDelayVariationAverage,
       "pvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp": pvxEServiceSlaCrntPM2WayDelayVariationAverageTimeStamp,
       "pvxEServiceSlaCrntPM2WayDelayVariationAverageValidity": pvxEServiceSlaCrntPM2WayDelayVariationAverageValidity,
       "pvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize": pvxEServiceSlaCrntPM2WayDelayVariationAverageInitialize,
       "pvxEServiceSlaHistPMTable": pvxEServiceSlaHistPMTable,
       "pvxEServiceSlaHistPMEntry": pvxEServiceSlaHistPMEntry,
       "pvxEServiceSlaHistPMSwitchIdx": pvxEServiceSlaHistPMSwitchIdx,
       "pvxEServiceSlaHistPMShelfIdx": pvxEServiceSlaHistPMShelfIdx,
       "pvxEServiceSlaHistPMSlotIdx": pvxEServiceSlaHistPMSlotIdx,
       "pvxEServiceSlaHistPMPortTypeIdx": pvxEServiceSlaHistPMPortTypeIdx,
       "pvxEServiceSlaHistPMPortIdx": pvxEServiceSlaHistPMPortIdx,
       "pvxEServiceSlaHistPMESName": pvxEServiceSlaHistPMESName,
       "pvxEServiceSlaHistPMRMepId": pvxEServiceSlaHistPMRMepId,
       "pvxEServiceSlaHistPMIntervalTypeIdx": pvxEServiceSlaHistPMIntervalTypeIdx,
       "pvxEServiceSlaHistPMIntervalIdx": pvxEServiceSlaHistPMIntervalIdx,
       "pvxEServiceSlaHistPMNearEndFrameLoss": pvxEServiceSlaHistPMNearEndFrameLoss,
       "pvxEServiceSlaHistPMNearEndFrameLossTimeStamp": pvxEServiceSlaHistPMNearEndFrameLossTimeStamp,
       "pvxEServiceSlaHistPMNearEndFrameLossValidity": pvxEServiceSlaHistPMNearEndFrameLossValidity,
       "pvxEServiceSlaHistPMNearEndFrameLossInitialize": pvxEServiceSlaHistPMNearEndFrameLossInitialize,
       "pvxEServiceSlaHistPMFarEndFrameLoss": pvxEServiceSlaHistPMFarEndFrameLoss,
       "pvxEServiceSlaHistPMFarEndFrameLossTimeStamp": pvxEServiceSlaHistPMFarEndFrameLossTimeStamp,
       "pvxEServiceSlaHistPMFarEndFrameLossValidity": pvxEServiceSlaHistPMFarEndFrameLossValidity,
       "pvxEServiceSlaHistPMFarEndFrameLossInitialize": pvxEServiceSlaHistPMFarEndFrameLossInitialize,
       "pvxEServiceSlaHistPM2WayDelayMinimum": pvxEServiceSlaHistPM2WayDelayMinimum,
       "pvxEServiceSlaHistPM2WayDelayMinimumTimeStamp": pvxEServiceSlaHistPM2WayDelayMinimumTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayMinimumValidity": pvxEServiceSlaHistPM2WayDelayMinimumValidity,
       "pvxEServiceSlaHistPM2WayDelayMinimumInitialize": pvxEServiceSlaHistPM2WayDelayMinimumInitialize,
       "pvxEServiceSlaHistPM2WayDelayMaximum": pvxEServiceSlaHistPM2WayDelayMaximum,
       "pvxEServiceSlaHistPM2WayDelayMaximumTimeStamp": pvxEServiceSlaHistPM2WayDelayMaximumTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayMaximumValidity": pvxEServiceSlaHistPM2WayDelayMaximumValidity,
       "pvxEServiceSlaHistPM2WayDelayMaximumInitialize": pvxEServiceSlaHistPM2WayDelayMaximumInitialize,
       "pvxEServiceSlaHistPM2WayDelayAverage": pvxEServiceSlaHistPM2WayDelayAverage,
       "pvxEServiceSlaHistPM2WayDelayAverageTimeStamp": pvxEServiceSlaHistPM2WayDelayAverageTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayAverageValidity": pvxEServiceSlaHistPM2WayDelayAverageValidity,
       "pvxEServiceSlaHistPM2WayDelayAverageInitialize": pvxEServiceSlaHistPM2WayDelayAverageInitialize,
       "pvxEServiceSlaHistPM2WayDelayVariationMinimum": pvxEServiceSlaHistPM2WayDelayVariationMinimum,
       "pvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp": pvxEServiceSlaHistPM2WayDelayVariationMinimumTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayVariationMinimumValidity": pvxEServiceSlaHistPM2WayDelayVariationMinimumValidity,
       "pvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize": pvxEServiceSlaHistPM2WayDelayVariationMinimumInitialize,
       "pvxEServiceSlaHistPM2WayDelayVariationMaximum": pvxEServiceSlaHistPM2WayDelayVariationMaximum,
       "pvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp": pvxEServiceSlaHistPM2WayDelayVariationMaximumTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayVariationMaximumValidity": pvxEServiceSlaHistPM2WayDelayVariationMaximumValidity,
       "pvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize": pvxEServiceSlaHistPM2WayDelayVariationMaximumInitialize,
       "pvxEServiceSlaHistPM2WayDelayVariationAverage": pvxEServiceSlaHistPM2WayDelayVariationAverage,
       "pvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp": pvxEServiceSlaHistPM2WayDelayVariationAverageTimeStamp,
       "pvxEServiceSlaHistPM2WayDelayVariationAverageValidity": pvxEServiceSlaHistPM2WayDelayVariationAverageValidity,
       "pvxEServiceSlaHistPM2WayDelayVariationAverageInitialize": pvxEServiceSlaHistPM2WayDelayVariationAverageInitialize,
       "pvxSwitchTable": pvxSwitchTable,
       "pvxSwitchEntry": pvxSwitchEntry,
       "pvxSwitchIdx": pvxSwitchIdx,
       "pvxSwitchMode": pvxSwitchMode,
       "pvxSwitchInnerEthType": pvxSwitchInnerEthType,
       "pvxSwitchLearning": pvxSwitchLearning,
       "pvxSwitchAgingTimer": pvxSwitchAgingTimer,
       "pvxSwitchTimeToAge": pvxSwitchTimeToAge,
       "pvxSwitchMasterNode": pvxSwitchMasterNode,
       "pvxSwitchForceSwitch": pvxSwitchForceSwitch,
       "pvxSwitchClearDynamicFDBEntries": pvxSwitchClearDynamicFDBEntries,
       "pvxSwitchProtocolAdminState": pvxSwitchProtocolAdminState,
       "pvxSwitchTunnMacAddrProfile": pvxSwitchTunnMacAddrProfile,
       "pvxSwitchEvcMEGName": pvxSwitchEvcMEGName,
       "pvxSwitchEvcMEGLevel": pvxSwitchEvcMEGLevel,
       "pvxSwitchName": pvxSwitchName,
       "pvxSwitchMIPAutoCreate": pvxSwitchMIPAutoCreate,
       "pvxSwitchMIPAutoCreateMEL": pvxSwitchMIPAutoCreateMEL,
       "pvxSwitchStackingPrimary": pvxSwitchStackingPrimary,
       "pvxSwitchStackingTimeAsPrimary": pvxSwitchStackingTimeAsPrimary,
       "pvxSwitchErpsVlanPropagate": pvxSwitchErpsVlanPropagate,
       "pvxSwitchCfmDestinationAddress": pvxSwitchCfmDestinationAddress,
       "pvxSwitchIntfBouncingTimerPeriod": pvxSwitchIntfBouncingTimerPeriod,
       "pvxSwitchCpuRLCos0PPS": pvxSwitchCpuRLCos0PPS,
       "pvxSwitchCpuRLCos1PPS": pvxSwitchCpuRLCos1PPS,
       "pvxSwitchCpuRLCos2PPS": pvxSwitchCpuRLCos2PPS,
       "pvxSwitchCpuRLCos3PPS": pvxSwitchCpuRLCos3PPS,
       "pvxSwitchCpuRLCos4PPS": pvxSwitchCpuRLCos4PPS,
       "pvxSwitchCpuRLCos5PPS": pvxSwitchCpuRLCos5PPS,
       "pvxSwitchCpuRLCos6PPS": pvxSwitchCpuRLCos6PPS,
       "pvxSwitchCpuRLCos7PPS": pvxSwitchCpuRLCos7PPS,
       "pvxSwitchCpuRLCos0DEPTH": pvxSwitchCpuRLCos0DEPTH,
       "pvxSwitchCpuRLCos1DEPTH": pvxSwitchCpuRLCos1DEPTH,
       "pvxSwitchCpuRLCos2DEPTH": pvxSwitchCpuRLCos2DEPTH,
       "pvxSwitchCpuRLCos3DEPTH": pvxSwitchCpuRLCos3DEPTH,
       "pvxSwitchCpuRLCos4DEPTH": pvxSwitchCpuRLCos4DEPTH,
       "pvxSwitchCpuRLCos5DEPTH": pvxSwitchCpuRLCos5DEPTH,
       "pvxSwitchCpuRLCos6DEPTH": pvxSwitchCpuRLCos6DEPTH,
       "pvxSwitchCpuRLCos7DEPTH": pvxSwitchCpuRLCos7DEPTH,
       "pvxSwitchCpuRLCos0BURST": pvxSwitchCpuRLCos0BURST,
       "pvxSwitchCpuRLCos1BURST": pvxSwitchCpuRLCos1BURST,
       "pvxSwitchCpuRLCos2BURST": pvxSwitchCpuRLCos2BURST,
       "pvxSwitchCpuRLCos3BURST": pvxSwitchCpuRLCos3BURST,
       "pvxSwitchCpuRLCos4BURST": pvxSwitchCpuRLCos4BURST,
       "pvxSwitchCpuRLCos5BURST": pvxSwitchCpuRLCos5BURST,
       "pvxSwitchCpuRLCos6BURST": pvxSwitchCpuRLCos6BURST,
       "pvxSwitchCpuRLCos7BURST": pvxSwitchCpuRLCos7BURST,
       "pvxSwitchMirrorFromCpu": pvxSwitchMirrorFromCpu,
       "pvxSwitchLldpTrapInterval": pvxSwitchLldpTrapInterval,
       "pvxSwitchRowStatus": pvxSwitchRowStatus,
       "pvxSwitchMemberTable": pvxSwitchMemberTable,
       "pvxSwitchMemberEntry": pvxSwitchMemberEntry,
       "pvxSwitchMemberIdx": pvxSwitchMemberIdx,
       "pvxSwitchMemberInstIdx": pvxSwitchMemberInstIdx,
       "pvxSwitchMemberShelfId": pvxSwitchMemberShelfId,
       "pvxSwitchMemberSlotId": pvxSwitchMemberSlotId,
       "pvxSwitchMemberStackingState": pvxSwitchMemberStackingState,
       "pvxSwitchMemberStackingPortCommState": pvxSwitchMemberStackingPortCommState,
       "pvxSwitchMemberBackplaneCommState": pvxSwitchMemberBackplaneCommState,
       "pvxSwitchMemberRowStatus": pvxSwitchMemberRowStatus,
       "pvxVLANTable": pvxVLANTable,
       "pvxVLANEntry": pvxVLANEntry,
       "pvxVLANSwitchIdx": pvxVLANSwitchIdx,
       "pvxVLANIdx": pvxVLANIdx,
       "pvxVLANMemberPortList": pvxVLANMemberPortList,
       "pvxVLANUnTaggedPortList": pvxVLANUnTaggedPortList,
       "pvxVLANMacLearning": pvxVLANMacLearning,
       "pvxVLANAdminState": pvxVLANAdminState,
       "pvxVLANMSTPId": pvxVLANMSTPId,
       "pvxVLANService": pvxVLANService,
       "pvxVLANForbiddenPortList": pvxVLANForbiddenPortList,
       "pvxVLANOperStatus": pvxVLANOperStatus,
       "pvxVLANRowStatus": pvxVLANRowStatus,
       "pvxFDBTable": pvxFDBTable,
       "pvxFDBEntry": pvxFDBEntry,
       "pvxFDBSwitchIdx": pvxFDBSwitchIdx,
       "pvxFDBVlanIdx": pvxFDBVlanIdx,
       "pvxFDBMACAddrIdx": pvxFDBMACAddrIdx,
       "pvxFDBPort": pvxFDBPort,
       "pvxFDBAddressType": pvxFDBAddressType,
       "pvxFDBRowStatus": pvxFDBRowStatus,
       "pvxStaticUnicastTable": pvxStaticUnicastTable,
       "pvxStaticUnicastEntry": pvxStaticUnicastEntry,
       "pvxStaticUnicastSwitchIdx": pvxStaticUnicastSwitchIdx,
       "pvxStaticUnicastVlanIdx": pvxStaticUnicastVlanIdx,
       "pvxStaticUnicastMACAddrIdx": pvxStaticUnicastMACAddrIdx,
       "pvxStaticUnicastReceivePort": pvxStaticUnicastReceivePort,
       "pvxStaticUnicastIntfIdList": pvxStaticUnicastIntfIdList,
       "pvxStaticUnicastAddressType": pvxStaticUnicastAddressType,
       "pvxStaticUnicastRowStatus": pvxStaticUnicastRowStatus,
       "pvxMultiCastGroupTable": pvxMultiCastGroupTable,
       "pvxMultiCastEntry": pvxMultiCastEntry,
       "pvxMCSwitchIdx": pvxMCSwitchIdx,
       "pvxMCVlanIdx": pvxMCVlanIdx,
       "pvxMCMACAddrIdx": pvxMCMACAddrIdx,
       "pvxMCIntfIdList": pvxMCIntfIdList,
       "pvxMCRowStatus": pvxMCRowStatus,
       "pvxStaticMulticastTable": pvxStaticMulticastTable,
       "pvxStaticMulticastEntry": pvxStaticMulticastEntry,
       "pvxStaticMCSwitchIdx": pvxStaticMCSwitchIdx,
       "pvxStaticMCVlanIdx": pvxStaticMCVlanIdx,
       "pvxStaticMCMACAddrIdx": pvxStaticMCMACAddrIdx,
       "pvxStaticMCReceivePort": pvxStaticMCReceivePort,
       "pvxStaticMCStaticIntfIdList": pvxStaticMCStaticIntfIdList,
       "pvxStaticMCForbiddenIntfIdList": pvxStaticMCForbiddenIntfIdList,
       "pvxStaticMCAddressType": pvxStaticMCAddressType,
       "pvxStaticMCRowStatus": pvxStaticMCRowStatus,
       "pvxLagTable": pvxLagTable,
       "pvxLagEntry": pvxLagEntry,
       "pvxLagSwitchIdx": pvxLagSwitchIdx,
       "pvxLagState": pvxLagState,
       "pvxLagSystemPriority": pvxLagSystemPriority,
       "pvxLagSystemIdentifier": pvxLagSystemIdentifier,
       "pvxLagRowStatus": pvxLagRowStatus,
       "pvxLagGroupTable": pvxLagGroupTable,
       "pvxLagGroupEntry": pvxLagGroupEntry,
       "pvxLGSwitchIdx": pvxLGSwitchIdx,
       "pvxLGIdx": pvxLGIdx,
       "pvxLGPortList": pvxLGPortList,
       "pvxLGDistribution": pvxLGDistribution,
       "pvxLGMacAddress": pvxLGMacAddress,
       "pvxLGPortCount": pvxLGPortCount,
       "pvxLGActivePortCount": pvxLGActivePortCount,
       "pvxLGMtuSize": pvxLGMtuSize,
       "pvxLGAdminStatus": pvxLGAdminStatus,
       "pvxLGOperStatus": pvxLGOperStatus,
       "pvxLGDataRate": pvxLGDataRate,
       "pvxLGMaxLinks": pvxLGMaxLinks,
       "pvxLGMinLinks": pvxLGMinLinks,
       "pvxLGRowStatus": pvxLGRowStatus,
       "pvxLagPortTable": pvxLagPortTable,
       "pvxLagPortEntry": pvxLagPortEntry,
       "pvxLagPortSwitchIdx": pvxLagPortSwitchIdx,
       "pvxLagPortShelfIdx": pvxLagPortShelfIdx,
       "pvxLagPortSlotIdx": pvxLagPortSlotIdx,
       "pvxLagPortTypeIdx": pvxLagPortTypeIdx,
       "pvxLagPortIdx": pvxLagPortIdx,
       "pvxLagPortPriority": pvxLagPortPriority,
       "pvxLagPortMode": pvxLagPortMode,
       "pvxLagPortAggState": pvxLagPortAggState,
       "pvxLagPortLcapId": pvxLagPortLcapId,
       "pvxLagPortTimeout": pvxLagPortTimeout,
       "pvxLagPortWaitTime": pvxLagPortWaitTime,
       "pvxLagPortActAdminState": pvxLagPortActAdminState,
       "pvxLagPortPrtnrAdminState": pvxLagPortPrtnrAdminState,
       "pvxLagPortGroupId": pvxLagPortGroupId,
       "pvxLagPortRowStatus": pvxLagPortRowStatus,
       "pvxMSTPGenTable": pvxMSTPGenTable,
       "pvxMSTPGenEntry": pvxMSTPGenEntry,
       "pvxMSTPGenSwitchIdx": pvxMSTPGenSwitchIdx,
       "pvxMSTPGenMaxHops": pvxMSTPGenMaxHops,
       "pvxMSTPGenVersionSupported": pvxMSTPGenVersionSupported,
       "pvxMSTPGenIdFmtSel": pvxMSTPGenIdFmtSel,
       "pvxMSTPGenIdName": pvxMSTPGenIdName,
       "pvxMSTPGenIdRevisionLevel": pvxMSTPGenIdRevisionLevel,
       "pvxMSTPGenIdDigest": pvxMSTPGenIdDigest,
       "pvxMSTPGenRegionalRoot": pvxMSTPGenRegionalRoot,
       "pvxMSTPGenExternalRootCost": pvxMSTPGenExternalRootCost,
       "pvxMSTPGenCistPriority": pvxMSTPGenCistPriority,
       "pvxMSTPGenBrdgId": pvxMSTPGenBrdgId,
       "pvxMSTPGenCistRoot": pvxMSTPGenCistRoot,
       "pvxMSTPGenCistRootPriority": pvxMSTPGenCistRootPriority,
       "pvxMSTPGenCistRootCost": pvxMSTPGenCistRootCost,
       "pvxMSTPMapTable": pvxMSTPMapTable,
       "pvxMSTPMapEntry": pvxMSTPMapEntry,
       "pvxMSTPMapSwitchIdx": pvxMSTPMapSwitchIdx,
       "pvxMSTPMapIdx": pvxMSTPMapIdx,
       "pvxMSTPMapVlanS1k": pvxMSTPMapVlanS1k,
       "pvxMSTPMapVlanS2k": pvxMSTPMapVlanS2k,
       "pvxMSTPMapVlanS3k": pvxMSTPMapVlanS3k,
       "pvxMSTPMapVlanS4k": pvxMSTPMapVlanS4k,
       "pvxMSTPMapRowStatus": pvxMSTPMapRowStatus,
       "pvxMSTPPortTable": pvxMSTPPortTable,
       "pvxMSTPPortEntry": pvxMSTPPortEntry,
       "pvxMSTPPortSwitchIdx": pvxMSTPPortSwitchIdx,
       "pvxMSTPPortShelfIdx": pvxMSTPPortShelfIdx,
       "pvxMSTPPortSlotIdx": pvxMSTPPortSlotIdx,
       "pvxMSTPPortTypeIdx": pvxMSTPPortTypeIdx,
       "pvxMSTPPortIdx": pvxMSTPPortIdx,
       "pvxMSTPPortDesignatedRoot": pvxMSTPPortDesignatedRoot,
       "pvxMSTPPortDesignatedBridge": pvxMSTPPortDesignatedBridge,
       "pvxMSTPPortDesignatedPort": pvxMSTPPortDesignatedPort,
       "pvxMSTPPortPathCost": pvxMSTPPortPathCost,
       "pvxMSTPPortPriority": pvxMSTPPortPriority,
       "pvxMSTPPortState": pvxMSTPPortState,
       "pvxMSTPPortRole": pvxMSTPPortRole,
       "pvxMSTPPortRegRoot": pvxMSTPPortRegRoot,
       "pvxMSTPPortRegRootCost": pvxMSTPPortRegRootCost,
       "pvxMSTPPortRestrictedRole": pvxMSTPPortRestrictedRole,
       "pvxMSTPPortRestrictedTCN": pvxMSTPPortRestrictedTCN,
       "pvxMSTPPortForcedPortState": pvxMSTPPortForcedPortState,
       "pvxMSTPPortLoopGuardState": pvxMSTPPortLoopGuardState,
       "pvxMSTPPortLinkType": pvxMSTPPortLinkType,
       "pvxMSTPXstTable": pvxMSTPXstTable,
       "pvxMSTPXstEntry": pvxMSTPXstEntry,
       "pvxMSTPXstSwitchIdx": pvxMSTPXstSwitchIdx,
       "pvxMSTPXstIdx": pvxMSTPXstIdx,
       "pvxMSTPXstBrdgPriority": pvxMSTPXstBrdgPriority,
       "pvxMSTPXstBrdgId": pvxMSTPXstBrdgId,
       "pvxMSTPXstBrdgRegRoot": pvxMSTPXstBrdgRegRoot,
       "pvxMSTPXstBrdgRegRootCost": pvxMSTPXstBrdgRegRootCost,
       "pvxMSTPXstRootPort": pvxMSTPXstRootPort,
       "pvxMSTPXstRootPortSwitch": pvxMSTPXstRootPortSwitch,
       "pvxMSTPXstRootPortShelf": pvxMSTPXstRootPortShelf,
       "pvxMSTPXstRootPortSlot": pvxMSTPXstRootPortSlot,
       "pvxMSTPXstRootPortType": pvxMSTPXstRootPortType,
       "pvxMSTPXstRootPortNum": pvxMSTPXstRootPortNum,
       "pvxMSTPXstPortTable": pvxMSTPXstPortTable,
       "pvxMSTPXstPortEntry": pvxMSTPXstPortEntry,
       "pvxMSTPXstPortSwitchIdx": pvxMSTPXstPortSwitchIdx,
       "pvxMSTPXstPortShelfIdx": pvxMSTPXstPortShelfIdx,
       "pvxMSTPXstPortSlotIdx": pvxMSTPXstPortSlotIdx,
       "pvxMSTPXstPortTypeIdx": pvxMSTPXstPortTypeIdx,
       "pvxMSTPXstPortInstIdx": pvxMSTPXstPortInstIdx,
       "pvxMSTPXstPortIdx": pvxMSTPXstPortIdx,
       "pvxMSTPXstPortState": pvxMSTPXstPortState,
       "pvxMSTPXstPortRole": pvxMSTPXstPortRole,
       "pvxMSTPXstPortDesigRoot": pvxMSTPXstPortDesigRoot,
       "pvxMSTPXstPortDesigCost": pvxMSTPXstPortDesigCost,
       "pvxMSTPXstPortDesigBridge": pvxMSTPXstPortDesigBridge,
       "pvxMSTPXstPortDesigPortId": pvxMSTPXstPortDesigPortId,
       "pvxMSTPXstPortPriority": pvxMSTPXstPortPriority,
       "pvxMSTPXstPortPathCost": pvxMSTPXstPortPathCost,
       "pvxMSTPXstPortForcedPortState": pvxMSTPXstPortForcedPortState,
       "pvxNextFreeIndexTable": pvxNextFreeIndexTable,
       "pvxNextFreeIndexEntry": pvxNextFreeIndexEntry,
       "pvxNextFreeIndexTableIndex": pvxNextFreeIndexTableIndex,
       "pvxNextFreeIndexSwitchIdx": pvxNextFreeIndexSwitchIdx,
       "pvxNextFreeIndexValue": pvxNextFreeIndexValue,
       "pvxUNITable": pvxUNITable,
       "pvxUNIEntry": pvxUNIEntry,
       "pvxUNISwitchId": pvxUNISwitchId,
       "pvxUNIShelfId": pvxUNIShelfId,
       "pvxUNISlotId": pvxUNISlotId,
       "pvxUNIPortTypeId": pvxUNIPortTypeId,
       "pvxUNIPortId": pvxUNIPortId,
       "pvxUNISpeed": pvxUNISpeed,
       "pvxUNIMode": pvxUNIMode,
       "pvxUNIMaxFrameSize": pvxUNIMaxFrameSize,
       "pvxUNICurrentFrameSize": pvxUNICurrentFrameSize,
       "pvxUNIServiceType": pvxUNIServiceType,
       "pvxUNINumServices": pvxUNINumServices,
       "pvxUNICPVid": pvxUNICPVid,
       "pvxUNIRowStatus": pvxUNIRowStatus,
       "pvxNNITable": pvxNNITable,
       "pvxNNIEntry": pvxNNIEntry,
       "pvxNNISwitchId": pvxNNISwitchId,
       "pvxNNIShelfId": pvxNNIShelfId,
       "pvxNNISlotId": pvxNNISlotId,
       "pvxNNIPortTypeId": pvxNNIPortTypeId,
       "pvxNNIPortId": pvxNNIPortId,
       "pvxNNISpeed": pvxNNISpeed,
       "pvxNNIMode": pvxNNIMode,
       "pvxNNIMaxFrameSize": pvxNNIMaxFrameSize,
       "pvxNNIRowStatus": pvxNNIRowStatus,
       "pvxVlanPortTable": pvxVlanPortTable,
       "pvxVlanPortEntry": pvxVlanPortEntry,
       "pvxVlanPortSwitchIdx": pvxVlanPortSwitchIdx,
       "pvxVlanPortShelfIdx": pvxVlanPortShelfIdx,
       "pvxVlanPortSlotIdx": pvxVlanPortSlotIdx,
       "pvxVlanPortTypeIdx": pvxVlanPortTypeIdx,
       "pvxVlanPortIdx": pvxVlanPortIdx,
       "pvxVlanPortGvrpAdminState": pvxVlanPortGvrpAdminState,
       "pvxVlanPortRestrictedVlanState": pvxVlanPortRestrictedVlanState,
       "pvxVlanPortEthPortAllowedFrametType": pvxVlanPortEthPortAllowedFrametType,
       "pvxVlanPortIngressFiltering": pvxVlanPortIngressFiltering,
       "pvxVlanPortGvrpFailedRegistrations": pvxVlanPortGvrpFailedRegistrations,
       "pvxVlanPortLastBpduOrigin": pvxVlanPortLastBpduOrigin,
       "pvxVlanCurrentTable": pvxVlanCurrentTable,
       "pvxVlanCurrentEntry": pvxVlanCurrentEntry,
       "pvxVlanCurrentSwitchIdx": pvxVlanCurrentSwitchIdx,
       "pvxVlanCurrentTimeMark": pvxVlanCurrentTimeMark,
       "pvxVlanCurrentVlanIdx": pvxVlanCurrentVlanIdx,
       "pvxVlanCurrentStatus": pvxVlanCurrentStatus,
       "pvxVlanCurrentCreationTime": pvxVlanCurrentCreationTime,
       "pvxDynamicVlanPortTable": pvxDynamicVlanPortTable,
       "pvxDynamicVlanPortEntry": pvxDynamicVlanPortEntry,
       "pvxDynamicVlanPortTimeMark": pvxDynamicVlanPortTimeMark,
       "pvxDynamicVlanPortVlanIdx": pvxDynamicVlanPortVlanIdx,
       "pvxDynamicVlanPortTagged": pvxDynamicVlanPortTagged,
       "pvxStackingPortTable": pvxStackingPortTable,
       "pvxStackingPortEntry": pvxStackingPortEntry,
       "pvxStackingPortOperStatus": pvxStackingPortOperStatus,
       "pvxStackingPortRowStatus": pvxStackingPortRowStatus,
       "pvxSwitchCpuRLMonTable": pvxSwitchCpuRLMonTable,
       "pvxSwitchCpuRLMonEntry": pvxSwitchCpuRLMonEntry,
       "pvxSwitchCpuRLMonSwitchIdx": pvxSwitchCpuRLMonSwitchIdx,
       "pvxSwitchCpuRLMonShelfIdx": pvxSwitchCpuRLMonShelfIdx,
       "pvxSwitchCpuRLMonSlotIdx": pvxSwitchCpuRLMonSlotIdx,
       "pvxSwitchCpuRLMonCosIdx": pvxSwitchCpuRLMonCosIdx,
       "pvxSwitchCpuRLMonCosCurrDepth": pvxSwitchCpuRLMonCosCurrDepth,
       "pvxSwitchCpuRLMonCosReceived": pvxSwitchCpuRLMonCosReceived,
       "pvxSwitchCpuRLMonCosDiscards": pvxSwitchCpuRLMonCosDiscards,
       "pvxSwitchCpuRLMonCosMinDepth60Sec": pvxSwitchCpuRLMonCosMinDepth60Sec,
       "pvxSwitchCpuRLMonCosMaxDepth60Sec": pvxSwitchCpuRLMonCosMaxDepth60Sec,
       "pvxSwitchCpuRLMonCosReceived60Sec": pvxSwitchCpuRLMonCosReceived60Sec,
       "pvxSwitchCpuRLMonCosDiscards60Sec": pvxSwitchCpuRLMonCosDiscards60Sec,
       "pvxSwitchCpuRLMonCosDiscardsTotal": pvxSwitchCpuRLMonCosDiscardsTotal,
       "pvxSwitchCpuRLMonCosReceivedRateLimit": pvxSwitchCpuRLMonCosReceivedRateLimit,
       "pvxSwitchCpuRLMonCosMaxAllowedDepth": pvxSwitchCpuRLMonCosMaxAllowedDepth,
       "pvxSwitchCpuRLMonCosHighWatermark": pvxSwitchCpuRLMonCosHighWatermark,
       "pvxSwitchCpuRLMonCosHighWatermark60Sec": pvxSwitchCpuRLMonCosHighWatermark60Sec,
       "pvxSwitchCpuRLMonCosHighestWatermark": pvxSwitchCpuRLMonCosHighestWatermark,
       "pvxBridgeServices": pvxBridgeServices,
       "pvxFlowTable": pvxFlowTable,
       "pvxFlowEntry": pvxFlowEntry,
       "pvxFSwitchIdx": pvxFSwitchIdx,
       "pvxFIdx": pvxFIdx,
       "pvxFClassificationIdList": pvxFClassificationIdList,
       "pvxFMeterId": pvxFMeterId,
       "pvxFCoSName": pvxFCoSName,
       "pvxFRowStatus": pvxFRowStatus,
       "pvxFlowClassificationTable": pvxFlowClassificationTable,
       "pvxFlowClassificationEntry": pvxFlowClassificationEntry,
       "pvxFloClSwitchIdx": pvxFloClSwitchIdx,
       "pvxFloClIdx": pvxFloClIdx,
       "pvxFloClActionId": pvxFloClActionId,
       "pvxFloClMeterId": pvxFloClMeterId,
       "pvxFloClStatus": pvxFloClStatus,
       "pvxFloClEntryType": pvxFloClEntryType,
       "pvxFloClL2InterfaceRange": pvxFloClL2InterfaceRange,
       "pvxFloClCVlanFilter": pvxFloClCVlanFilter,
       "pvxFloClSVlanFilter": pvxFloClSVlanFilter,
       "pvxFloClSourceIPFilter": pvxFloClSourceIPFilter,
       "pvxFloClDestIPFilter": pvxFloClDestIPFilter,
       "pvxFloClIPProtocolFilter": pvxFloClIPProtocolFilter,
       "pvxFloClEtherTypeFilter": pvxFloClEtherTypeFilter,
       "pvxFloClSourceMacFilter": pvxFloClSourceMacFilter,
       "pvxFloClDestMacFilter": pvxFloClDestMacFilter,
       "pvxFloClSourceUDPorTCPFilter": pvxFloClSourceUDPorTCPFilter,
       "pvxFloClDestUDPorTCPFilter": pvxFloClDestUDPorTCPFilter,
       "pvxFloClRowStatus": pvxFloClRowStatus,
       "pvxFlowActionsTable": pvxFlowActionsTable,
       "pvxFlowActionsEntry": pvxFlowActionsEntry,
       "pvxFloActSwitchIdx": pvxFloActSwitchIdx,
       "pvxFloActIdx": pvxFloActIdx,
       "pvxFloActChangePriority": pvxFloActChangePriority,
       "pvxFloActNewPriority": pvxFloActNewPriority,
       "pvxFloActPacketAction": pvxFloActPacketAction,
       "pvxFloActRedirectToInterfaceIndex": pvxFloActRedirectToInterfaceIndex,
       "pvxFloActMirrorType": pvxFloActMirrorType,
       "pvxFloActMirrorToInterfaceIndex": pvxFloActMirrorToInterfaceIndex,
       "pvxFloActSVlanValue": pvxFloActSVlanValue,
       "pvxFloActCVlanValue": pvxFloActCVlanValue,
       "pvxFloActSVlanAction": pvxFloActSVlanAction,
       "pvxFloActCVlanAction": pvxFloActCVlanAction,
       "pvxFloActGreenAction": pvxFloActGreenAction,
       "pvxFloActGreenCNGAction": pvxFloActGreenCNGAction,
       "pvxFloActRedAction": pvxFloActRedAction,
       "pvxFloActRedCNGAction": pvxFloActRedCNGAction,
       "pvxFloActYellowAction": pvxFloActYellowAction,
       "pvxFloActYellowCNGAction": pvxFloActYellowCNGAction,
       "pvxFloActRowStatus": pvxFloActRowStatus,
       "pvxFlowMeterTable": pvxFlowMeterTable,
       "pvxFlowMeterEntry": pvxFlowMeterEntry,
       "pvxFMSwitchIdx": pvxFMSwitchIdx,
       "pvxFMMeterIdx": pvxFMMeterIdx,
       "pvxFMBWProfileId": pvxFMBWProfileId,
       "pvxFMMeterProfileId": pvxFMMeterProfileId,
       "pvxFMRowStatus": pvxFMRowStatus,
       "pvxFlowStatsTable": pvxFlowStatsTable,
       "pvxFlowStatsEntry": pvxFlowStatsEntry,
       "pvxFSSwitchIdx": pvxFSSwitchIdx,
       "pvxFSStatsIdx": pvxFSStatsIdx,
       "pvxFSFlowId": pvxFSFlowId,
       "pvxFSInProfilePackets": pvxFSInProfilePackets,
       "pvxFSOutOfProfilePackets": pvxFSOutOfProfilePackets,
       "pvxFSCountOfClassifiedPackets": pvxFSCountOfClassifiedPackets,
       "pvxFSRowStatus": pvxFSRowStatus,
       "pvxPbCVidRegistrationTable": pvxPbCVidRegistrationTable,
       "pvxPbCVidRegistrationTableEntry": pvxPbCVidRegistrationTableEntry,
       "pvxPCVRTCVlanIdFrom": pvxPCVRTCVlanIdFrom,
       "pvxPCVRTCVlanIdTo": pvxPCVRTCVlanIdTo,
       "pvxPCVRTSVlanId": pvxPCVRTSVlanId,
       "pvxPCVRTUntaggedPEP": pvxPCVRTUntaggedPEP,
       "pvxPCVRTUntaggedCEP": pvxPCVRTUntaggedCEP,
       "pvxPCVRTSource": pvxPCVRTSource,
       "pvxPCVRTMapOperStatus": pvxPCVRTMapOperStatus,
       "pvxPCVRTXlateOperStatus": pvxPCVRTXlateOperStatus,
       "pvxPCVRTRowStatus": pvxPCVRTRowStatus,
       "pvxEthServiceTable": pvxEthServiceTable,
       "pvxEthServiceEntry": pvxEthServiceEntry,
       "pvxEthSrvcSwitchIdx": pvxEthSrvcSwitchIdx,
       "pvxEthSrvcName": pvxEthSrvcName,
       "pvxEthSrvcType": pvxEthSrvcType,
       "pvxEthSrvcState": pvxEthSrvcState,
       "pvxEthSrvcOperState": pvxEthSrvcOperState,
       "pvxEthSrvcTransportType": pvxEthSrvcTransportType,
       "pvxEthSrvcSVLAN": pvxEthSrvcSVLAN,
       "pvxEthSrvcSpanTreeInstance": pvxEthSrvcSpanTreeInstance,
       "pvxEthSrvcMaxUNIs": pvxEthSrvcMaxUNIs,
       "pvxEthSrvcNumUNIs": pvxEthSrvcNumUNIs,
       "pvxEthSrvcPointedness": pvxEthSrvcPointedness,
       "pvxEthSrvcFrameSize": pvxEthSrvcFrameSize,
       "pvxEthSrvcCVidXlate": pvxEthSrvcCVidXlate,
       "pvxEthSrvcMECciInterval": pvxEthSrvcMECciInterval,
       "pvxEthSrvcMECciEnable": pvxEthSrvcMECciEnable,
       "pvxEthSrvcMEName": pvxEthSrvcMEName,
       "pvxEthSrvcMaxNNIs": pvxEthSrvcMaxNNIs,
       "pvxEthSrvcNumNNIs": pvxEthSrvcNumNNIs,
       "pvxEthSrvcLockNNIs": pvxEthSrvcLockNNIs,
       "pvxEthSrvcExceedMaxUNI": pvxEthSrvcExceedMaxUNI,
       "pvxEthSrvcRowStatus": pvxEthSrvcRowStatus,
       "pvxServiceUNITable": pvxServiceUNITable,
       "pvxServiceUNIEntry": pvxServiceUNIEntry,
       "pvxSrvcUNISwitchId": pvxSrvcUNISwitchId,
       "pvxSrvcUNIShelfId": pvxSrvcUNIShelfId,
       "pvxSrvcUNISlotId": pvxSrvcUNISlotId,
       "pvxSrvcUNIPortTypeId": pvxSrvcUNIPortTypeId,
       "pvxSrvcUNIPortId": pvxSrvcUNIPortId,
       "pvxSrvcUNISrvcName": pvxSrvcUNISrvcName,
       "pvxSrvcUNINumCVids": pvxSrvcUNINumCVids,
       "pvxSrvcUNIIngressBW": pvxSrvcUNIIngressBW,
       "pvxSrvcUNIIngressBWperCos": pvxSrvcUNIIngressBWperCos,
       "pvxSrvcUNIEgressBW": pvxSrvcUNIEgressBW,
       "pvxSrvcUNIEgressBWperCos": pvxSrvcUNIEgressBWperCos,
       "pvxSrvcUNIUserDefinedMepId": pvxSrvcUNIUserDefinedMepId,
       "pvxSrvcUNIForwarding": pvxSrvcUNIForwarding,
       "pvxSrvcUNIServiceMap": pvxSrvcUNIServiceMap,
       "pvxSrvcUNIFilterSequence": pvxSrvcUNIFilterSequence,
       "pvxSrvcUNIEFPSDEnabled": pvxSrvcUNIEFPSDEnabled,
       "pvxSrvcUNIEFPSDLocalEFPSDState": pvxSrvcUNIEFPSDLocalEFPSDState,
       "pvxSrvcUNISlaMeasurementProfile": pvxSrvcUNISlaMeasurementProfile,
       "pvxSrvcUNIRowStatus": pvxSrvcUNIRowStatus,
       "pvxSvidXlateTable": pvxSvidXlateTable,
       "pvxSvidXlateEntry": pvxSvidXlateEntry,
       "pvxSvidXlateSwitchId": pvxSvidXlateSwitchId,
       "pvxSvidXlateShelfId": pvxSvidXlateShelfId,
       "pvxSvidXlateSlotId": pvxSvidXlateSlotId,
       "pvxSvidXlatePortTypeId": pvxSvidXlatePortTypeId,
       "pvxSvidXlatePortId": pvxSvidXlatePortId,
       "pvxSvidXlateInternalSVid": pvxSvidXlateInternalSVid,
       "pvxSvidXlateExternalSVid": pvxSvidXlateExternalSVid,
       "pvxEcfmService": pvxEcfmService,
       "pvxMepListTable": pvxMepListTable,
       "pvxMepListEntry": pvxMepListEntry,
       "pvxMepListSwitchIdx": pvxMepListSwitchIdx,
       "pvxMepListESrvcVlanId": pvxMepListESrvcVlanId,
       "pvxMepListIdentifier": pvxMepListIdentifier,
       "pvxMepLocalRemoteFlag": pvxMepLocalRemoteFlag,
       "pvxMepSequenceId": pvxMepSequenceId,
       "pvxMepListRowStatus": pvxMepListRowStatus,
       "pvxEcfmMepTable": pvxEcfmMepTable,
       "pvxEcfmMepEntry": pvxEcfmMepEntry,
       "pvxEcfmMepSwitchIdx": pvxEcfmMepSwitchIdx,
       "pvxEcfmMepShelfId": pvxEcfmMepShelfId,
       "pvxEcfmMepSlotId": pvxEcfmMepSlotId,
       "pvxEcfmMepPortTypeId": pvxEcfmMepPortTypeId,
       "pvxEcfmMepPortId": pvxEcfmMepPortId,
       "pvxEcfmMepESrvcName": pvxEcfmMepESrvcName,
       "pvxEcfmMepIdentifier": pvxEcfmMepIdentifier,
       "pvxEcfmMepDirection": pvxEcfmMepDirection,
       "pvxEcfmMepActive": pvxEcfmMepActive,
       "pvxEcfmMepAutoGenerateFlag": pvxEcfmMepAutoGenerateFlag,
       "pvxEcfmMepMacAddress": pvxEcfmMepMacAddress,
       "pvxEcfmMepFlushRMepDb": pvxEcfmMepFlushRMepDb,
       "pvxEcfmMepOutOfService": pvxEcfmMepOutOfService,
       "pvxEcfmMepY1731DefectConditions": pvxEcfmMepY1731DefectConditions,
       "pvxEcfmMepDefects": pvxEcfmMepDefects,
       "pvxEcfmMepCcmSequenceErr": pvxEcfmMepCcmSequenceErr,
       "pvxEcfmMepSentCcms": pvxEcfmMepSentCcms,
       "pvxEcfmMepTransmitLtmStatus": pvxEcfmMepTransmitLtmStatus,
       "pvxEcfmMepTransmitLtmTargetMepId": pvxEcfmMepTransmitLtmTargetMepId,
       "pvxEcfmMepTransmitLtmTtl": pvxEcfmMepTransmitLtmTtl,
       "pvxEcfmMepTransmitLtmResultOK": pvxEcfmMepTransmitLtmResultOK,
       "pvxEcfmMepTransmitLtmSeqNumber": pvxEcfmMepTransmitLtmSeqNumber,
       "pvxEcfmMepTransmitLbmStatus": pvxEcfmMepTransmitLbmStatus,
       "pvxEcfmMepTransmitLbmDestMepId": pvxEcfmMepTransmitLbmDestMepId,
       "pvxEcfmMepTransmitLbmCount": pvxEcfmMepTransmitLbmCount,
       "pvxEcfmMepTransmitLbmResultOK": pvxEcfmMepTransmitLbmResultOK,
       "pvxEcfmMepY1731LbmCurrentTransId": pvxEcfmMepY1731LbmCurrentTransId,
       "pvxEcfmMepLbrIn": pvxEcfmMepLbrIn,
       "pvxEcfmMepLbrInOutOfOrder": pvxEcfmMepLbrInOutOfOrder,
       "pvxEcfmMepLbrBadMsdu": pvxEcfmMepLbrBadMsdu,
       "pvxEcfmMepLbrOut": pvxEcfmMepLbrOut,
       "pvxEcfmMepUnexpLtrIn": pvxEcfmMepUnexpLtrIn,
       "pvxEcfmMepErrCcmRMepId": pvxEcfmMepErrCcmRMepId,
       "pvxEcfmMepXconnRMepId": pvxEcfmMepXconnRMepId,
       "pvxEcfmMepDbTable": pvxEcfmMepDbTable,
       "pvxEcfmMepDbEntry": pvxEcfmMepDbEntry,
       "pvxEcfmMepDbSwitchIdx": pvxEcfmMepDbSwitchIdx,
       "pvxEcfmMepDbVlanId": pvxEcfmMepDbVlanId,
       "pvxEcfmMepDbLocalMepId": pvxEcfmMepDbLocalMepId,
       "pvxEcfmMepDbRemoteMepId": pvxEcfmMepDbRemoteMepId,
       "pvxEcfmMepDbRMepState": pvxEcfmMepDbRMepState,
       "pvxEcfmMepDbMacAddress": pvxEcfmMepDbMacAddress,
       "pvxEcfmMepDbRMepSwitchName": pvxEcfmMepDbRMepSwitchName,
       "pvxEcfmMepDbRMepPortInfo": pvxEcfmMepDbRMepPortInfo,
       "pvxEcfmMepDbRMepRDI": pvxEcfmMepDbRMepRDI,
       "pvxEcfmMepDbRMepCcmDefect": pvxEcfmMepDbRMepCcmDefect,
       "pvxEcfmMepDbRMepPortStatusDefect": pvxEcfmMepDbRMepPortStatusDefect,
       "pvxEcfmMepDbRMepIntfStatusDefect": pvxEcfmMepDbRMepIntfStatusDefect,
       "pvxEcfmMipTable": pvxEcfmMipTable,
       "pvxEcfmMipEntry": pvxEcfmMipEntry,
       "pvxEcfmMipSwitchIdx": pvxEcfmMipSwitchIdx,
       "pvxEcfmMipShelfId": pvxEcfmMipShelfId,
       "pvxEcfmMipSlotId": pvxEcfmMipSlotId,
       "pvxEcfmMipPortTypeId": pvxEcfmMipPortTypeId,
       "pvxEcfmMipPortId": pvxEcfmMipPortId,
       "pvxEcfmMipMegLevel": pvxEcfmMipMegLevel,
       "pvxEcfmMipESrvcVlanId": pvxEcfmMipESrvcVlanId,
       "pvxEcfmMipESrvcName": pvxEcfmMipESrvcName,
       "pvxEcfmMipActiveState": pvxEcfmMipActiveState,
       "pvxEcfmMipRowStatus": pvxEcfmMipRowStatus,
       "pvxY1731LbStatsTable": pvxY1731LbStatsTable,
       "pvxY1731LbStatsEntry": pvxY1731LbStatsEntry,
       "pvxY1731LbStatsSwitchIdx": pvxY1731LbStatsSwitchIdx,
       "pvxY1731LbStatsESrvcName": pvxY1731LbStatsESrvcName,
       "pvxY1731LbStatsIdentifier": pvxY1731LbStatsIdentifier,
       "pvxY1731LbmTransId": pvxY1731LbmTransId,
       "pvxY1731LbStatsLbmOut": pvxY1731LbStatsLbmOut,
       "pvxY1731LbStatsLbrIn": pvxY1731LbStatsLbrIn,
       "pvxY1731LbStatsLbrTimeAverage": pvxY1731LbStatsLbrTimeAverage,
       "pvxY1731LbStatsLbrTimeMin": pvxY1731LbStatsLbrTimeMin,
       "pvxY1731LbStatsLbrTimeMax": pvxY1731LbStatsLbrTimeMax,
       "pvxY1731LbStatsTotalResponders": pvxY1731LbStatsTotalResponders,
       "pvxY1731LbStatsAvgLbrsPerResponder": pvxY1731LbStatsAvgLbrsPerResponder,
       "pvxEcfmLtrTable": pvxEcfmLtrTable,
       "pvxEcfmLtrEntry": pvxEcfmLtrEntry,
       "pvxEcfmLtrSwitchIdx": pvxEcfmLtrSwitchIdx,
       "pvxEcfmLtrVlanId": pvxEcfmLtrVlanId,
       "pvxEcfmLtrMepIdentifier": pvxEcfmLtrMepIdentifier,
       "pvxEcfmLtrSeqNumber": pvxEcfmLtrSeqNumber,
       "pvxEcfmLtrReceiveOrder": pvxEcfmLtrReceiveOrder,
       "pvxEcfmLtrTtl": pvxEcfmLtrTtl,
       "pvxEcfmLtrForwarded": pvxEcfmLtrForwarded,
       "pvxEcfmLtrTerminalMep": pvxEcfmLtrTerminalMep,
       "pvxEcfmLtrRelayAction": pvxEcfmLtrRelayAction,
       "pvxEcfmLtrSwitchName": pvxEcfmLtrSwitchName,
       "pvxEcfmLtrIngressAction": pvxEcfmLtrIngressAction,
       "pvxEcfmLtrIngressMac": pvxEcfmLtrIngressMac,
       "pvxEcfmLtrIngressPortInfo": pvxEcfmLtrIngressPortInfo,
       "pvxEcfmLtrEgressAction": pvxEcfmLtrEgressAction,
       "pvxEcfmLtrEgressMac": pvxEcfmLtrEgressMac,
       "pvxEcfmLtrEgressPortInfo": pvxEcfmLtrEgressPortInfo,
       "pvxSLAThroughputTestTable": pvxSLAThroughputTestTable,
       "pvxSLAThroughputTestEntry": pvxSLAThroughputTestEntry,
       "pvxSLAThroughputTestSwitchIdx": pvxSLAThroughputTestSwitchIdx,
       "pvxSLAThroughputTestShelfIdx": pvxSLAThroughputTestShelfIdx,
       "pvxSLAThroughputTestSlotIdx": pvxSLAThroughputTestSlotIdx,
       "pvxSLAThroughputTestPortTypeIdx": pvxSLAThroughputTestPortTypeIdx,
       "pvxSLAThroughputTestPortIdx": pvxSLAThroughputTestPortIdx,
       "pvxSLAThroughputTestESName": pvxSLAThroughputTestESName,
       "pvxSLAThroughputTestRMepId": pvxSLAThroughputTestRMepId,
       "pvxSLAThroughputTestRole": pvxSLAThroughputTestRole,
       "pvxSLAThroughputTestInitiatorCmdState": pvxSLAThroughputTestInitiatorCmdState,
       "pvxSLAThroughputTestResponderOpState": pvxSLAThroughputTestResponderOpState,
       "pvxSLAThroughputTestFrameSize1": pvxSLAThroughputTestFrameSize1,
       "pvxSLAThroughputTestFrameSize2": pvxSLAThroughputTestFrameSize2,
       "pvxSLAThroughputTestFrameSize3": pvxSLAThroughputTestFrameSize3,
       "pvxSLAThroughputTestFrameSize4": pvxSLAThroughputTestFrameSize4,
       "pvxSLAThroughputTestFrameSize5": pvxSLAThroughputTestFrameSize5,
       "pvxSLAThroughputTestFrameSize6": pvxSLAThroughputTestFrameSize6,
       "pvxSLAThroughputTestSrvcPolicyName": pvxSLAThroughputTestSrvcPolicyName,
       "pvxSLAThroughputTestClassMapName": pvxSLAThroughputTestClassMapName,
       "pvxSLAThroughputTestBwProfileName": pvxSLAThroughputTestBwProfileName,
       "pvxSLAThroughputTestSVlanPriority": pvxSLAThroughputTestSVlanPriority,
       "pvxSLAThroughputTestCirRateTestResult": pvxSLAThroughputTestCirRateTestResult,
       "pvxSLAThroughputTestFrameSize1FarEndThroughput": pvxSLAThroughputTestFrameSize1FarEndThroughput,
       "pvxSLAThroughputTestFrameSize1NearEndThroughput": pvxSLAThroughputTestFrameSize1NearEndThroughput,
       "pvxSLAThroughputTestFrameSize2FarEndThroughput": pvxSLAThroughputTestFrameSize2FarEndThroughput,
       "pvxSLAThroughputTestFrameSize2NearEndThroughput": pvxSLAThroughputTestFrameSize2NearEndThroughput,
       "pvxSLAThroughputTestFrameSize3FarEndThroughput": pvxSLAThroughputTestFrameSize3FarEndThroughput,
       "pvxSLAThroughputTestFrameSize3NearEndThroughput": pvxSLAThroughputTestFrameSize3NearEndThroughput,
       "pvxSLAThroughputTestFrameSize4FarEndThroughput": pvxSLAThroughputTestFrameSize4FarEndThroughput,
       "pvxSLAThroughputTestFrameSize4NearEndThroughput": pvxSLAThroughputTestFrameSize4NearEndThroughput,
       "pvxSLAThroughputTestFrameSize5FarEndThroughput": pvxSLAThroughputTestFrameSize5FarEndThroughput,
       "pvxSLAThroughputTestFrameSize5NearEndThroughput": pvxSLAThroughputTestFrameSize5NearEndThroughput,
       "pvxSLAThroughputTestFrameSize6FarEndThroughput": pvxSLAThroughputTestFrameSize6FarEndThroughput,
       "pvxSLAThroughputTestFrameSize6NearEndThroughput": pvxSLAThroughputTestFrameSize6NearEndThroughput,
       "pvxSLAThroughputTestRowStatus": pvxSLAThroughputTestRowStatus,
       "pvxSLAMsmtInitiatorDBTable": pvxSLAMsmtInitiatorDBTable,
       "pvxSLAMsmtInitiatorDBEntry": pvxSLAMsmtInitiatorDBEntry,
       "pvxSLAMsmtInitiatorDBSwitchIdx": pvxSLAMsmtInitiatorDBSwitchIdx,
       "pvxSLAMsmtInitiatorDBShelfIdx": pvxSLAMsmtInitiatorDBShelfIdx,
       "pvxSLAMsmtInitiatorDBSlotIdx": pvxSLAMsmtInitiatorDBSlotIdx,
       "pvxSLAMsmtInitiatorDBPortTypeIdx": pvxSLAMsmtInitiatorDBPortTypeIdx,
       "pvxSLAMsmtInitiatorDBPortIdx": pvxSLAMsmtInitiatorDBPortIdx,
       "pvxSLAMsmtInitiatorDBESName": pvxSLAMsmtInitiatorDBESName,
       "pvxSLAMsmtInitiatorDBRMepId": pvxSLAMsmtInitiatorDBRMepId,
       "pvxSLAMsmtInitiatorDBCmdState": pvxSLAMsmtInitiatorDBCmdState,
       "pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority": pvxSLAMsmtInitiatorDBDelayMsmtSVlanPriority,
       "pvxSLAMsmtInitiatorDBRowStatus": pvxSLAMsmtInitiatorDBRowStatus,
       "pvxSLAMsmtResponderDBTable": pvxSLAMsmtResponderDBTable,
       "pvxSLAMsmtResponderDBEntry": pvxSLAMsmtResponderDBEntry,
       "pvxSLAMsmtResponderDBSwitchIdx": pvxSLAMsmtResponderDBSwitchIdx,
       "pvxSLAMsmtResponderDBShelfIdx": pvxSLAMsmtResponderDBShelfIdx,
       "pvxSLAMsmtResponderDBSlotIdx": pvxSLAMsmtResponderDBSlotIdx,
       "pvxSLAMsmtResponderDBPortTypeIdx": pvxSLAMsmtResponderDBPortTypeIdx,
       "pvxSLAMsmtResponderDBPortIdx": pvxSLAMsmtResponderDBPortIdx,
       "pvxSLAMsmtResponderDBESName": pvxSLAMsmtResponderDBESName,
       "pvxSLAMsmtResponderDBRMepId": pvxSLAMsmtResponderDBRMepId,
       "pvxSLAMsmtResponderDBRowStatus": pvxSLAMsmtResponderDBRowStatus,
       "pvxMgmtVLANTable": pvxMgmtVLANTable,
       "pvxMgmtVLANEntry": pvxMgmtVLANEntry,
       "pvxMgmtVLANSwitchIdx": pvxMgmtVLANSwitchIdx,
       "pvxMgmtVLANSrvcName": pvxMgmtVLANSrvcName,
       "pvxMgmtVLANBWProfileName": pvxMgmtVLANBWProfileName,
       "pvxMgmtVLANCVLANId": pvxMgmtVLANCVLANId,
       "pvxMgmtVLANAddressType": pvxMgmtVLANAddressType,
       "pvxMgmtVLANIpAddress": pvxMgmtVLANIpAddress,
       "pvxMgmtVLANNetMask": pvxMgmtVLANNetMask,
       "pvxMgmtVLANDebugMode": pvxMgmtVLANDebugMode,
       "pvxMgmtVLANRowStatus": pvxMgmtVLANRowStatus,
       "pvxServiceNNITable": pvxServiceNNITable,
       "pvxServiceNNIEntry": pvxServiceNNIEntry,
       "pvxSrvcNNISwitchId": pvxSrvcNNISwitchId,
       "pvxSrvcNNIShelfId": pvxSrvcNNIShelfId,
       "pvxSrvcNNISlotId": pvxSrvcNNISlotId,
       "pvxSrvcNNIPortTypeId": pvxSrvcNNIPortTypeId,
       "pvxSrvcNNIPortId": pvxSrvcNNIPortId,
       "pvxSrvcNNISrvcName": pvxSrvcNNISrvcName,
       "pvxSrvcNNIIngressBW": pvxSrvcNNIIngressBW,
       "pvxSrvcNNIIngressBWperCos": pvxSrvcNNIIngressBWperCos,
       "pvxSrvcNNIEgressBW": pvxSrvcNNIEgressBW,
       "pvxSrvcNNIEgressBWperCos": pvxSrvcNNIEgressBWperCos,
       "pvxSrvcNNIRowStatus": pvxSrvcNNIRowStatus,
       "pvxERPSServiceNNITable": pvxERPSServiceNNITable,
       "pvxERPSServiceNNIEntry": pvxERPSServiceNNIEntry,
       "pvxERPSSrvcNNISwitchId": pvxERPSSrvcNNISwitchId,
       "pvxERPSSrvcNNIShelfId": pvxERPSSrvcNNIShelfId,
       "pvxERPSSrvcNNISlotId": pvxERPSSrvcNNISlotId,
       "pvxERPSSrvcNNIPortTypeId": pvxERPSSrvcNNIPortTypeId,
       "pvxERPSSrvcNNIPortId": pvxERPSSrvcNNIPortId,
       "pvxERPSSrvcNNIRingProtectLink": pvxERPSSrvcNNIRingProtectLink,
       "pvxERPSSrvcNNIProtectionSwitch": pvxERPSSrvcNNIProtectionSwitch,
       "pvxERPSSrvcNNIRingPortStatus": pvxERPSSrvcNNIRingPortStatus,
       "pvxERPSSrvcNNISrvcName": pvxERPSSrvcNNISrvcName,
       "pvxERPSSrvcNNIRingPortId": pvxERPSSrvcNNIRingPortId,
       "pvxERPSSrvcNNIMEName": pvxERPSSrvcNNIMEName,
       "pvxERPSSrvcNNIRemoteMepId": pvxERPSSrvcNNIRemoteMepId,
       "pvxERPSSrvcNNIECFMInfo": pvxERPSSrvcNNIECFMInfo,
       "pvxERPSSrvcNNILocalMepId": pvxERPSSrvcNNILocalMepId,
       "pvxERPSSrvcNNINeighborPort": pvxERPSSrvcNNINeighborPort,
       "pvxERPSSrvcNNINextNeighborPort": pvxERPSSrvcNNINextNeighborPort,
       "pvxERPSSrvcNNIFlushRemoteMEP": pvxERPSSrvcNNIFlushRemoteMEP,
       "pvxERPSSrvcNNICcmLinkDetection": pvxERPSSrvcNNICcmLinkDetection,
       "pvxERPSServiceTable": pvxERPSServiceTable,
       "pvxERPSServiceEntry": pvxERPSServiceEntry,
       "pvxERPSSrvcSwitchIdx": pvxERPSSrvcSwitchIdx,
       "pvxERPSSrvcName": pvxERPSSrvcName,
       "pvxERPSSrvcRevertMode": pvxERPSSrvcRevertMode,
       "pvxERPSSrvcProtectionSwitchMode": pvxERPSSrvcProtectionSwitchMode,
       "pvxERPSSrvcHoldTimer": pvxERPSSrvcHoldTimer,
       "pvxERPSSrvcWaitToRestoreTimer": pvxERPSSrvcWaitToRestoreTimer,
       "pvxERPSSrvcGuardTimer": pvxERPSSrvcGuardTimer,
       "pvxERPSSrvcPeriodicTimer": pvxERPSSrvcPeriodicTimer,
       "pvxERPSSrvcPropagateTC": pvxERPSSrvcPropagateTC,
       "pvxERPSSrvcNodeType": pvxERPSSrvcNodeType,
       "pvxERPSSrvcRingMonitoring": pvxERPSSrvcRingMonitoring,
       "pvxERPSSrvcRingProperty": pvxERPSSrvcRingProperty,
       "pvxERPSSrvcRingSemState": pvxERPSSrvcRingSemState,
       "pvxERPSSrvcRingNodeStatus": pvxERPSSrvcRingNodeStatus,
       "pvxERPSSrvcNumRingPorts": pvxERPSSrvcNumRingPorts,
       "pvxERPSSrvcSVLAN": pvxERPSSrvcSVLAN,
       "pvxERPSSrvcVirtualLink": pvxERPSSrvcVirtualLink,
       "pvxERPSSrvcWaitToBlockTimer": pvxERPSSrvcWaitToBlockTimer,
       "pvxERPSSrvcCompatibleVersion": pvxERPSSrvcCompatibleVersion,
       "pvxERPSSrvcMultipleFailure": pvxERPSSrvcMultipleFailure,
       "pvxERPSSrvcSubRingWithoutVC": pvxERPSSrvcSubRingWithoutVC,
       "pvxERPSSrvcDownMegLevel": pvxERPSSrvcDownMegLevel,
       "pvxERPSSrvcUpMegLevel": pvxERPSSrvcUpMegLevel,
       "pvxERPSSrvcWTRRemaining": pvxERPSSrvcWTRRemaining,
       "pvxBridgeProfiles": pvxBridgeProfiles,
       "pvxBWProfileTable": pvxBWProfileTable,
       "pvxBWProfileEntry": pvxBWProfileEntry,
       "pvxBWPIdx": pvxBWPIdx,
       "pvxBWPCir": pvxBWPCir,
       "pvxBWPCbs": pvxBWPCbs,
       "pvxBWPEir": pvxBWPEir,
       "pvxBWPEbs": pvxBWPEbs,
       "pvxBWPCoSQueue": pvxBWPCoSQueue,
       "pvxBWPRowStatus": pvxBWPRowStatus,
       "pvxCoSProfileTable": pvxCoSProfileTable,
       "pvxCoSProfileEntry": pvxCoSProfileEntry,
       "pvxCPIdx": pvxCPIdx,
       "pvxCPMaxBandwidth": pvxCPMaxBandwidth,
       "pvxCPMinBandwidth": pvxCPMinBandwidth,
       "pvxCPWeight": pvxCPWeight,
       "pvxCPQueueAlgo": pvxCPQueueAlgo,
       "pvxCPRowStatus": pvxCPRowStatus,
       "pvxCtrlFrmProfileTable": pvxCtrlFrmProfileTable,
       "pvxFlowMeterProfileTable": pvxFlowMeterProfileTable,
       "pvxFlowMeterProfileEntry": pvxFlowMeterProfileEntry,
       "pvxFMPIdx": pvxFMPIdx,
       "pvxFMPBWProfileId": pvxFMPBWProfileId,
       "pvxFMPColorAware": pvxFMPColorAware,
       "pvxFMPMeterType": pvxFMPMeterType,
       "pvxFMPStatsEnabled": pvxFMPStatsEnabled,
       "pvxFMPRowStatus": pvxFMPRowStatus,
       "pvxTunnMacAddrProfileTable": pvxTunnMacAddrProfileTable,
       "pvxSchedulerProfileTable": pvxSchedulerProfileTable,
       "pvxSchedulerProfileEntry": pvxSchedulerProfileEntry,
       "pvxSchedProfName": pvxSchedProfName,
       "pvxSchedProfAlgorithm": pvxSchedProfAlgorithm,
       "pvxSchedProfWeightQ0": pvxSchedProfWeightQ0,
       "pvxSchedProfWeightQ1": pvxSchedProfWeightQ1,
       "pvxSchedProfWeightQ2": pvxSchedProfWeightQ2,
       "pvxSchedProfWeightQ3": pvxSchedProfWeightQ3,
       "pvxSchedProfWeightQ4": pvxSchedProfWeightQ4,
       "pvxSchedProfWeightQ5": pvxSchedProfWeightQ5,
       "pvxSchedProfWeightQ6": pvxSchedProfWeightQ6,
       "pvxSchedProfWeightQ7": pvxSchedProfWeightQ7,
       "pvxSchedProfMinBwQ0": pvxSchedProfMinBwQ0,
       "pvxSchedProfMaxBwQ0": pvxSchedProfMaxBwQ0,
       "pvxSchedProfMinBwQ1": pvxSchedProfMinBwQ1,
       "pvxSchedProfMaxBwQ1": pvxSchedProfMaxBwQ1,
       "pvxSchedProfMinBwQ2": pvxSchedProfMinBwQ2,
       "pvxSchedProfMaxBwQ2": pvxSchedProfMaxBwQ2,
       "pvxSchedProfMinBwQ3": pvxSchedProfMinBwQ3,
       "pvxSchedProfMaxBwQ3": pvxSchedProfMaxBwQ3,
       "pvxSchedProfMinBwQ4": pvxSchedProfMinBwQ4,
       "pvxSchedProfMaxBwQ4": pvxSchedProfMaxBwQ4,
       "pvxSchedProfMinBwQ5": pvxSchedProfMinBwQ5,
       "pvxSchedProfMaxBwQ5": pvxSchedProfMaxBwQ5,
       "pvxSchedProfMinBwQ6": pvxSchedProfMinBwQ6,
       "pvxSchedProfMaxBwQ6": pvxSchedProfMaxBwQ6,
       "pvxSchedProfMinBwQ7": pvxSchedProfMinBwQ7,
       "pvxSchedProfMaxBwQ7": pvxSchedProfMaxBwQ7,
       "pvxSchedProfMTUQuanta": pvxSchedProfMTUQuanta,
       "pvxSchedProfRowStatus": pvxSchedProfRowStatus,
       "pvxPriorityTCMapTable": pvxPriorityTCMapTable,
       "pvxPriorityTCMapEntry": pvxPriorityTCMapEntry,
       "pvxPriorityTCMapName": pvxPriorityTCMapName,
       "pvxPriority7TrafficClass": pvxPriority7TrafficClass,
       "pvxPriority6TrafficClass": pvxPriority6TrafficClass,
       "pvxPriority5TrafficClass": pvxPriority5TrafficClass,
       "pvxPriority4TrafficClass": pvxPriority4TrafficClass,
       "pvxPriority3TrafficClass": pvxPriority3TrafficClass,
       "pvxPriority2TrafficClass": pvxPriority2TrafficClass,
       "pvxPriority1TrafficClass": pvxPriority1TrafficClass,
       "pvxPriority0TrafficClass": pvxPriority0TrafficClass,
       "pvxPriorityTCMapRowStatus": pvxPriorityTCMapRowStatus,
       "pvxPCPEncDecProfileTable": pvxPCPEncDecProfileTable,
       "pvxPCPEncDecProfEntry": pvxPCPEncDecProfEntry,
       "pvxPCPEncDecProfileName": pvxPCPEncDecProfileName,
       "pvxPCPEncDecSelectRow": pvxPCPEncDecSelectRow,
       "pvxPCPEncPriority7": pvxPCPEncPriority7,
       "pvxPCPEncPriority7DE": pvxPCPEncPriority7DE,
       "pvxPCPEncPriority6": pvxPCPEncPriority6,
       "pvxPCPEncPriority6DE": pvxPCPEncPriority6DE,
       "pvxPCPEncPriority5": pvxPCPEncPriority5,
       "pvxPCPEncPriority5DE": pvxPCPEncPriority5DE,
       "pvxPCPEncPriority4": pvxPCPEncPriority4,
       "pvxPCPEncPriority4DE": pvxPCPEncPriority4DE,
       "pvxPCPEncPriority3": pvxPCPEncPriority3,
       "pvxPCPEncPriority3DE": pvxPCPEncPriority3DE,
       "pvxPCPEncPriority2": pvxPCPEncPriority2,
       "pvxPCPEncPriority2DE": pvxPCPEncPriority2DE,
       "pvxPCPEncPriority1": pvxPCPEncPriority1,
       "pvxPCPEncPriority1DE": pvxPCPEncPriority1DE,
       "pvxPCPEncPriority0": pvxPCPEncPriority0,
       "pvxPCPEncPriority0DE": pvxPCPEncPriority0DE,
       "pvxPCPDecPriority7": pvxPCPDecPriority7,
       "pvxPCPDecPriority6": pvxPCPDecPriority6,
       "pvxPCPDecPriority5": pvxPCPDecPriority5,
       "pvxPCPDecPriority4": pvxPCPDecPriority4,
       "pvxPCPDecPriority3": pvxPCPDecPriority3,
       "pvxPCPDecPriority2": pvxPCPDecPriority2,
       "pvxPCPDecPriority1": pvxPCPDecPriority1,
       "pvxPCPDecPriority0": pvxPCPDecPriority0,
       "pvxPCPEncDecRowStatus": pvxPCPEncDecRowStatus,
       "pvxDscpPHBProfileTable": pvxDscpPHBProfileTable,
       "pvxDscpPHBProfileEntry": pvxDscpPHBProfileEntry,
       "pvxDscpPHBProfileName": pvxDscpPHBProfileName,
       "pvxDscpClassSelector7": pvxDscpClassSelector7,
       "pvxDscpClassSelector6": pvxDscpClassSelector6,
       "pvxDscpClassSelector5": pvxDscpClassSelector5,
       "pvxDscpClassSelector4": pvxDscpClassSelector4,
       "pvxDscpClassSelector3": pvxDscpClassSelector3,
       "pvxDscpClassSelector2": pvxDscpClassSelector2,
       "pvxDscpClassSelector1": pvxDscpClassSelector1,
       "pvxDscpClassBestEffort": pvxDscpClassBestEffort,
       "pvxDscpAssuredFwd1y": pvxDscpAssuredFwd1y,
       "pvxDscpAssuredFwd2y": pvxDscpAssuredFwd2y,
       "pvxDscpAssuredFwd3y": pvxDscpAssuredFwd3y,
       "pvxDscpAssuredFwd4y": pvxDscpAssuredFwd4y,
       "pvxDscpExpeditedFwd": pvxDscpExpeditedFwd,
       "pvxDscpPHBProfileRowStatus": pvxDscpPHBProfileRowStatus,
       "pvxBandwidthProfileTable": pvxBandwidthProfileTable,
       "pvxBandwidthProfileEntry": pvxBandwidthProfileEntry,
       "pvxBandwidthProfileName": pvxBandwidthProfileName,
       "pvxBWCnfrmActionChangeDscp": pvxBWCnfrmActionChangeDscp,
       "pvxBWCnfrmActionChangeTOSFrmPri": pvxBWCnfrmActionChangeTOSFrmPri,
       "pvxBWExceedActionChangeDscp": pvxBWExceedActionChangeDscp,
       "pvxBWMeterColorAware": pvxBWMeterColorAware,
       "pvxBWMeterMode": pvxBWMeterMode,
       "pvxBWMeterCir": pvxBWMeterCir,
       "pvxBWMeterCbs": pvxBWMeterCbs,
       "pvxBWMeterEir": pvxBWMeterEir,
       "pvxBWMeterEbs": pvxBWMeterEbs,
       "pvxBWSetInternalPriority": pvxBWSetInternalPriority,
       "pvxBWExceedActionSetDEI": pvxBWExceedActionSetDEI,
       "pvxBandwidthProfileRowStatus": pvxBandwidthProfileRowStatus,
       "pvxClassMapProfileTable": pvxClassMapProfileTable,
       "pvxClassMapProfileEntry": pvxClassMapProfileEntry,
       "pvxClassMapProfileName": pvxClassMapProfileName,
       "pvxClassMapType": pvxClassMapType,
       "pvxClassMapMatchType": pvxClassMapMatchType,
       "pvxClassMapCVlanFilter": pvxClassMapCVlanFilter,
       "pvxClassMapSVlanFilter": pvxClassMapSVlanFilter,
       "pvxClassMapCVlanPriFilter": pvxClassMapCVlanPriFilter,
       "pvxClassMapSVlanPriFilter": pvxClassMapSVlanPriFilter,
       "pvxClassMapSrcIpFilter": pvxClassMapSrcIpFilter,
       "pvxClassMapSrcIpNetMaskFilter": pvxClassMapSrcIpNetMaskFilter,
       "pvxClassMapDstIpFilter": pvxClassMapDstIpFilter,
       "pvxClassMapDstIpNetMaskFilter": pvxClassMapDstIpNetMaskFilter,
       "pvxClassMapIpProtocolFilter": pvxClassMapIpProtocolFilter,
       "pvxClassMapDscpFilter": pvxClassMapDscpFilter,
       "pvxClassMapL4SrcPortFilter": pvxClassMapL4SrcPortFilter,
       "pvxClassMapL4DstPortFilter": pvxClassMapL4DstPortFilter,
       "pvxClassMapTcpControlFilter": pvxClassMapTcpControlFilter,
       "pvxClassMapSrcMACAddrFilter": pvxClassMapSrcMACAddrFilter,
       "pvxClassMapDstMACAddrFilter": pvxClassMapDstMACAddrFilter,
       "pvxClassMapEtherTypeFilter": pvxClassMapEtherTypeFilter,
       "pvxClassMapSrcMACMaskFilter": pvxClassMapSrcMACMaskFilter,
       "pvxClassMapDstMACMaskFilter": pvxClassMapDstMACMaskFilter,
       "pvxClassMapL4SrcPortEndFilter": pvxClassMapL4SrcPortEndFilter,
       "pvxClassMapL4DstPortEndFilter": pvxClassMapL4DstPortEndFilter,
       "pvxClassMapCVlanEndFilter": pvxClassMapCVlanEndFilter,
       "pvxClassMapProfileRowStatus": pvxClassMapProfileRowStatus,
       "pvxPolicyMapProfileTable": pvxPolicyMapProfileTable,
       "pvxPolicyMapProfileEntry": pvxPolicyMapProfileEntry,
       "pvxPolicyMapPolicyName": pvxPolicyMapPolicyName,
       "pvxPolicyMapClassMapName": pvxPolicyMapClassMapName,
       "pvxPolicyMapBWProfileName": pvxPolicyMapBWProfileName,
       "pvxPolicyMapProfileRowStatus": pvxPolicyMapProfileRowStatus,
       "pvxControlFrameProfileTable": pvxControlFrameProfileTable,
       "pvxControlFrameProfileEntry": pvxControlFrameProfileEntry,
       "pvxControlFrameProfileName": pvxControlFrameProfileName,
       "pvxControlFrameProfileLacp": pvxControlFrameProfileLacp,
       "pvxControlFrameProfileStp": pvxControlFrameProfileStp,
       "pvxControlFrameProfileDot1x": pvxControlFrameProfileDot1x,
       "pvxControlFrameProfileGvrp": pvxControlFrameProfileGvrp,
       "pvxControlFrameProfileGmrp": pvxControlFrameProfileGmrp,
       "pvxControlFrameProfileLldp": pvxControlFrameProfileLldp,
       "pvxControlFrameProfileRowStatus": pvxControlFrameProfileRowStatus,
       "pvxTunnelMacAddrProfileTable": pvxTunnelMacAddrProfileTable,
       "pvxTunnelMacAddrProfileEntry": pvxTunnelMacAddrProfileEntry,
       "pvxTMAPName": pvxTMAPName,
       "pvxTMAPDot1xTunnMacAddr": pvxTMAPDot1xTunnMacAddr,
       "pvxTMAPLacpTunnMacAddr": pvxTMAPLacpTunnMacAddr,
       "pvxTMAPStpTunnMacAddr": pvxTMAPStpTunnMacAddr,
       "pvxTMAPGvrpTunnMacAddr": pvxTMAPGvrpTunnMacAddr,
       "pvxTMAPGmrpTunnMacAddr": pvxTMAPGmrpTunnMacAddr,
       "pvxTMAPLldpTunnMacAddr": pvxTMAPLldpTunnMacAddr,
       "pvxTMAPRowStatus": pvxTMAPRowStatus,
       "pvxSLAMeasurementProfileTable": pvxSLAMeasurementProfileTable,
       "pvxSLAMeasurementProfileEntry": pvxSLAMeasurementProfileEntry,
       "pvxSLAMsmtProfileName": pvxSLAMsmtProfileName,
       "pvxSLAMsmtThresholdFarEndLossRatio": pvxSLAMsmtThresholdFarEndLossRatio,
       "pvxSLAMsmtThresholdNearEndLossRatio": pvxSLAMsmtThresholdNearEndLossRatio,
       "pvxSLAMsmtThresholdDelayMaximum": pvxSLAMsmtThresholdDelayMaximum,
       "pvxSLAMsmtThresholdDelayAverage": pvxSLAMsmtThresholdDelayAverage,
       "pvxSLAMsmtThresholdDelayVarMaximum": pvxSLAMsmtThresholdDelayVarMaximum,
       "pvxSLAMsmtThresholdDelayVarAverage": pvxSLAMsmtThresholdDelayVarAverage,
       "pvxSLAMsmtMonitorPeriod": pvxSLAMsmtMonitorPeriod,
       "pvxSLAMsmtRowStatus": pvxSLAMsmtRowStatus,
       "mstpGlobalErrType": mstpGlobalErrType,
       "mstpGeneralEvtType": mstpGeneralEvtType,
       "mstpProtocolMigrationType": mstpProtocolMigrationType,
       "mstpPacketErrType": mstpPacketErrType,
       "mstpPacketErrValue": mstpPacketErrValue,
       "pvxBridgeGVRP": pvxBridgeGVRP,
       "mstpProtocolGeneralEvt": mstpProtocolGeneralEvt,
       "mstpNewRootEvt": mstpNewRootEvt,
       "mstpTopologyChangeEvt": mstpTopologyChangeEvt,
       "mstpProtocolMigrationEvt": mstpProtocolMigrationEvt,
       "mstpInvalidPacketRcvdEvt": mstpInvalidPacketRcvdEvt,
       "mstpRegionConfigChangeEvt": mstpRegionConfigChangeEvt,
       "mstpRoleChangeEvt": mstpRoleChangeEvt,
       "pvxESrvcBWPrflBDWUtlzTcaEvt": pvxESrvcBWPrflBDWUtlzTcaEvt,
       "pvxESrvcOperStateChangeEvt": pvxESrvcOperStateChangeEvt,
       "pvxERPSSrvcNNIProtectionSwitchChangeEvent": pvxERPSSrvcNNIProtectionSwitchChangeEvent,
       "pvxERPSSrvcRingSemStateChangeEvent": pvxERPSSrvcRingSemStateChangeEvent,
       "pvxERPSSrvcConfigFailEvent": pvxERPSSrvcConfigFailEvent,
       "pvxERPSSrvcTimerStartEvent": pvxERPSSrvcTimerStartEvent,
       "pvxSlaMeasurementTcaEvt": pvxSlaMeasurementTcaEvt,
       "pvxSrvcUNIEFPSDLocalEFPSDStateChangeEvent": pvxSrvcUNIEFPSDLocalEFPSDStateChangeEvent,
       "cfmRMepStateChangeEvtNotifications": cfmRMepStateChangeEvtNotifications,
       "cfmRMepStateChangeV2Evt": cfmRMepStateChangeV2Evt,
       "pvxVlanPortLastBpduOriginChangeEvtNotifications": pvxVlanPortLastBpduOriginChangeEvtNotifications,
       "pvxVlanPortLastBpduOriginChangeEvt": pvxVlanPortLastBpduOriginChangeEvt,
       "pvxVlanPortAddDynamicVlanEvtNotifications": pvxVlanPortAddDynamicVlanEvtNotifications,
       "pvxVlanPortAddDynamicVlanEvt": pvxVlanPortAddDynamicVlanEvt,
       "pvxVlanPortRemoveDynamicVlanEvtNotifications": pvxVlanPortRemoveDynamicVlanEvtNotifications,
       "pvxVlanPortRemoveDynamicVlanEvt": pvxVlanPortRemoveDynamicVlanEvt,
       "resourceUnavailableCond": resourceUnavailableCond,
       "resourceUnavailableClear": resourceUnavailableClear,
       "lagLinkDownCond": lagLinkDownCond,
       "lagLinkDownClear": lagLinkDownClear,
       "pvxERPSSrvcVersionMismatchCond": pvxERPSSrvcVersionMismatchCond,
       "pvxERPSSrvcVersionMismatchClear": pvxERPSSrvcVersionMismatchClear,
       "pvxERPSSrvcFOPProvisionMismatchCond": pvxERPSSrvcFOPProvisionMismatchCond,
       "pvxERPSSrvcFOPProvisionMismatchClear": pvxERPSSrvcFOPProvisionMismatchClear,
       "switchMemberStkPortDownCond": switchMemberStkPortDownCond,
       "switchMemberStkPortDownClear": switchMemberStkPortDownClear}
)
