# SNMP MIB module (ALCATEL-IND1-TIMETRA-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:13 2024
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

(TmnxAlarmState,
 TmnxMDAChanType,
 TmnxPortAdminStatus,
 tmnxChassisIndex,
 tmnxChassisNotifyChassisId,
 tmnxHwConformance,
 tmnxHwNotification,
 tmnxHwObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-CHASSIS-MIB",
    "TmnxAlarmState",
    "TmnxMDAChanType",
    "TmnxPortAdminStatus",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId",
    "tmnxHwConformance",
    "tmnxHwNotification",
    "tmnxHwObjs")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(TFCName,
 TItemDescription,
 TItemLongDescription,
 TMlpppQoSProfileId,
 TNamedItem,
 TNamedItemOrEmpty,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TQueueId,
 TSecondaryShaper10GPIRRate,
 TmnxActionType,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TFCName",
    "TItemDescription",
    "TItemLongDescription",
    "TMlpppQoSProfileId",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TQueueId",
    "TSecondaryShaper10GPIRRate",
    "TmnxActionType",
    "TmnxOperState",
    "TmnxPortID")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

tmnxPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 25)
)
tmnxPortMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPortOperStatus(Integer32, TextualConvention):
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
        *(("diagnosing", 4),
          ("failed", 5),
          ("inService", 2),
          ("outOfService", 3),
          ("unknown", 1))
    )



class TmnxPortEtherReportValue(Integer32, TextualConvention):
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
        *(("highBer", 5),
          ("localFault", 3),
          ("noFrameLock", 4),
          ("notUsed", 0),
          ("remoteFault", 2),
          ("signalFailure", 1))
    )



class TmnxPortEtherReportStatus(Bits, TextualConvention):
    status = "current"


class TmnxPortClass(Integer32, TextualConvention):
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
        *(("faste", 2),
          ("gige", 3),
          ("none", 1),
          ("sonet", 5),
          ("tdm", 9),
          ("unused", 7),
          ("vport", 6),
          ("xcme", 8),
          ("xgige", 4))
    )



class TmnxPortConnectorType(Unsigned32, TextualConvention):
    status = "current"


class TmnxPortState(Integer32, TextualConvention):
    status = "current"
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
        *(("diagnose", 6),
          ("ghost", 2),
          ("linkDown", 3),
          ("linkUp", 4),
          ("none", 1),
          ("up", 5))
    )



class TmnxPortType(Unsigned32, TextualConvention):
    status = "current"


class TmnxDs0ChannelList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TmnxBundleID(Unsigned32, TextualConvention):
    status = "current"


class TmnxDSXBertPattern(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("alternating", 3),
          ("none", 0),
          ("ones", 1),
          ("twoexp11", 8),
          ("twoexp15", 6),
          ("twoexp20", 7),
          ("twoexp20q", 9),
          ("twoexp23", 10),
          ("twoexp3", 4),
          ("twoexp9", 5),
          ("zeros", 2))
    )



class TmnxDSXBertOperStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("idle", 2),
          ("noMdaResources", 3),
          ("none", 0))
    )



class TmnxDSXIdleCycleFlags(Integer32, TextualConvention):
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
        *(("flags", 1),
          ("none", 0),
          ("ones", 2))
    )



class TmnxDSXIdleFillType(Integer32, TextualConvention):
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
        *(("allOnes", 1),
          ("notApplicable", 0),
          ("userDefinedPattern", 2))
    )



class TmnxDSXLoopback(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("internal", 2),
          ("line", 1),
          ("none", 0),
          ("remote", 3))
    )



class TmnxDSXReportAlarm(Bits, TextualConvention):
    status = "current"


class TmnxDSXClockSource(Integer32, TextualConvention):
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
        *(("adaptive", 3),
          ("differential", 4),
          ("loopTimed", 1),
          ("nodeTimed", 2))
    )



class TmnxDSXClockSyncState(Integer32, TextualConvention):
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
        *(("freeRun", 3),
          ("holdOver", 2),
          ("normal", 1),
          ("unknown", 0))
    )



class TmnxDS1Loopback(Integer32, TextualConvention):
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
        *(("fdlAnsi", 3),
          ("fdlBellcore", 4),
          ("inbandAnsi", 6),
          ("inbandBellcore", 7),
          ("internal", 2),
          ("line", 1),
          ("none", 0),
          ("payloadAnsi", 5))
    )



class TmnxDS3Loopback(Integer32, TextualConvention):
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
        *(("internal", 2),
          ("line", 1),
          ("none", 0),
          ("remote", 3))
    )



class TmnxImaGrpState(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupportedImaVersion", 10),
          ("configAbortUnsupportedM", 4),
          ("insufficientLinks", 7),
          ("invalid", 0),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )



class TmnxImaGrpFailState(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blockedFe", 11),
          ("blockedNe", 10),
          ("failedAssymetricFe", 7),
          ("failedAssymetricNe", 6),
          ("insufficientLinksFe", 9),
          ("insufficientLinksNe", 8),
          ("invalidImaVersionFe", 14),
          ("invalidImaVersionNe", 13),
          ("invalidMValueFe", 5),
          ("invalidMValueNe", 4),
          ("noFailure", 1),
          ("otherFailure", 12),
          ("startUpFe", 3),
          ("startUpNe", 2))
    )



class TmnxImaLnkState(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableInhibited", 5),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )



class TmnxImaLnkFailState(Integer32, TextualConvention):
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
        *(("blocked", 6),
          ("farEndRxLinkUnusable", 9),
          ("farEndTxLinkUnusable", 8),
          ("fault", 7),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("noFailure", 1))
    )



class TmnxImaTestState(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("failed", 3),
          ("operating", 2))
    )



class TmnxImaGrpClockModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )



class TmnxImaGrpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneDotOne", 2),
          ("oneDotZero", 1))
    )



class TmnxMcMlpppClassIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxMlpppEndpointIdClass(Integer32, TextualConvention):
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
        *(("ieee802dot1GlobalMacAddress", 3),
          ("ipAddress", 2),
          ("localAddress", 1),
          ("nullClass", 0),
          ("pppMagicNumberBlock", 4),
          ("publicSwitchedNetworkDirNumber", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPortConformance_ObjectIdentity = ObjectIdentity
tmnxPortConformance = _TmnxPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2)
)
_TmnxPortCompliances_ObjectIdentity = ObjectIdentity
tmnxPortCompliances = _TmnxPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1)
)
_TmnxPortComp7750_ObjectIdentity = ObjectIdentity
tmnxPortComp7750 = _TmnxPortComp7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3)
)
_TmnxPortComp7450_ObjectIdentity = ObjectIdentity
tmnxPortComp7450 = _TmnxPortComp7450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4)
)
_TmnxPortComp7710_ObjectIdentity = ObjectIdentity
tmnxPortComp7710 = _TmnxPortComp7710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5)
)
_TmnxPortGroups_ObjectIdentity = ObjectIdentity
tmnxPortGroups = _TmnxPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2)
)
_TmnxPortObjs_ObjectIdentity = ObjectIdentity
tmnxPortObjs = _TmnxPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4)
)
_TmnxPortTableLastChange_Type = TimeStamp
_TmnxPortTableLastChange_Object = MibScalar
tmnxPortTableLastChange = _TmnxPortTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 1),
    _TmnxPortTableLastChange_Type()
)
tmnxPortTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTableLastChange.setStatus("current")
_TmnxPortTable_Object = MibTable
tmnxPortTable = _TmnxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxPortTable.setStatus("current")
_TmnxPortEntry_Object = MibTableRow
tmnxPortEntry = _TmnxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1)
)
tmnxPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortEntry.setStatus("current")
_TmnxPortPortID_Type = TmnxPortID
_TmnxPortPortID_Object = MibTableColumn
tmnxPortPortID = _TmnxPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 1),
    _TmnxPortPortID_Type()
)
tmnxPortPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortPortID.setStatus("current")
_TmnxPortLastChangeTime_Type = TimeStamp
_TmnxPortLastChangeTime_Object = MibTableColumn
tmnxPortLastChangeTime = _TmnxPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 2),
    _TmnxPortLastChangeTime_Type()
)
tmnxPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastChangeTime.setStatus("current")
_TmnxPortType_Type = TmnxPortType
_TmnxPortType_Object = MibTableColumn
tmnxPortType = _TmnxPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 3),
    _TmnxPortType_Type()
)
tmnxPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortType.setStatus("current")
_TmnxPortClass_Type = TmnxPortClass
_TmnxPortClass_Object = MibTableColumn
tmnxPortClass = _TmnxPortClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 4),
    _TmnxPortClass_Type()
)
tmnxPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortClass.setStatus("current")


class _TmnxPortDescription_Type(TItemLongDescription):
    """Custom type tmnxPortDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TmnxPortDescription_Object = MibTableColumn
tmnxPortDescription = _TmnxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 5),
    _TmnxPortDescription_Type()
)
tmnxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDescription.setStatus("current")
_TmnxPortName_Type = TNamedItemOrEmpty
_TmnxPortName_Object = MibTableColumn
tmnxPortName = _TmnxPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 6),
    _TmnxPortName_Type()
)
tmnxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortName.setStatus("current")


class _TmnxPortAlias_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortAlias based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortAlias_Object = MibTableColumn
tmnxPortAlias = _TmnxPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 7),
    _TmnxPortAlias_Type()
)
tmnxPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAlias.setStatus("current")


class _TmnxPortUserAssignedMac_Type(TruthValue):
    """Custom type tmnxPortUserAssignedMac based on TruthValue"""


_TmnxPortUserAssignedMac_Object = MibTableColumn
tmnxPortUserAssignedMac = _TmnxPortUserAssignedMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 8),
    _TmnxPortUserAssignedMac_Type()
)
tmnxPortUserAssignedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortUserAssignedMac.setStatus("current")


class _TmnxPortMacAddress_Type(MacAddress):
    """Custom type tmnxPortMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxPortMacAddress_Object = MibTableColumn
tmnxPortMacAddress = _TmnxPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 9),
    _TmnxPortMacAddress_Type()
)
tmnxPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortMacAddress.setStatus("current")
_TmnxPortHwMacAddress_Type = MacAddress
_TmnxPortHwMacAddress_Object = MibTableColumn
tmnxPortHwMacAddress = _TmnxPortHwMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 10),
    _TmnxPortHwMacAddress_Type()
)
tmnxPortHwMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortHwMacAddress.setStatus("current")


class _TmnxPortMode_Type(Integer32):
    """Custom type tmnxPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("network", 2),
          ("undefined", 0))
    )


_TmnxPortMode_Type.__name__ = "Integer32"
_TmnxPortMode_Object = MibTableColumn
tmnxPortMode = _TmnxPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 11),
    _TmnxPortMode_Type()
)
tmnxPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortMode.setStatus("current")


class _TmnxPortEncapType_Type(Integer32):
    """Custom type tmnxPortEncapType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("atmEncap", 9),
          ("bcpDot1qEncap", 5),
          ("bcpNullEncap", 4),
          ("cemEncap", 13),
          ("ciscoHDLCEncap", 12),
          ("frEncap", 7),
          ("ipcpEncap", 6),
          ("mplsEncap", 3),
          ("nullEncap", 1),
          ("pppAutoEncap", 8),
          ("qEncap", 2),
          ("qinqEncap", 10),
          ("unknown", 0),
          ("wanMirrorEncap", 11))
    )


_TmnxPortEncapType_Type.__name__ = "Integer32"
_TmnxPortEncapType_Object = MibTableColumn
tmnxPortEncapType = _TmnxPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 12),
    _TmnxPortEncapType_Type()
)
tmnxPortEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEncapType.setStatus("current")


class _TmnxPortLagId_Type(Unsigned32):
    """Custom type tmnxPortLagId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TmnxPortLagId_Type.__name__ = "Unsigned32"
_TmnxPortLagId_Object = MibTableColumn
tmnxPortLagId = _TmnxPortLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 13),
    _TmnxPortLagId_Type()
)
tmnxPortLagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLagId.setStatus("current")


class _TmnxPortHoldTimeUp_Type(Unsigned32):
    """Custom type tmnxPortHoldTimeUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxPortHoldTimeUp_Type.__name__ = "Unsigned32"
_TmnxPortHoldTimeUp_Object = MibTableColumn
tmnxPortHoldTimeUp = _TmnxPortHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 14),
    _TmnxPortHoldTimeUp_Type()
)
tmnxPortHoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeUp.setUnits("seconds")


class _TmnxPortHoldTimeDown_Type(Unsigned32):
    """Custom type tmnxPortHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxPortHoldTimeDown_Type.__name__ = "Unsigned32"
_TmnxPortHoldTimeDown_Object = MibTableColumn
tmnxPortHoldTimeDown = _TmnxPortHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 15),
    _TmnxPortHoldTimeDown_Type()
)
tmnxPortHoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeDown.setUnits("seconds")


class _TmnxPortUpProtocols_Type(Bits):
    """Custom type tmnxPortUpProtocols based on Bits"""
    namedValues = NamedValues(
        *(("portUpAtm", 5),
          ("portUpBcp", 2),
          ("portUpChdlc", 6),
          ("portUpFr", 4),
          ("portUpIma", 7),
          ("portUpIpv4", 0),
          ("portUpIpv6", 8),
          ("portUpIso", 3),
          ("portUpMpls", 1))
    )

_TmnxPortUpProtocols_Type.__name__ = "Bits"
_TmnxPortUpProtocols_Object = MibTableColumn
tmnxPortUpProtocols = _TmnxPortUpProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 16),
    _TmnxPortUpProtocols_Type()
)
tmnxPortUpProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortUpProtocols.setStatus("current")
_TmnxPortConnectorType_Type = TmnxPortConnectorType
_TmnxPortConnectorType_Object = MibTableColumn
tmnxPortConnectorType = _TmnxPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 17),
    _TmnxPortConnectorType_Type()
)
tmnxPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectorType.setStatus("current")


class _TmnxPortTransceiverType_Type(Integer32):
    """Custom type tmnxPortTransceiverType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("gbic", 1),
          ("moduleConnectorSolderedToMotherboard", 2),
          ("sfpTransceiver", 3),
          ("unknown", 0),
          ("x2Transceiver", 10),
          ("xbiTransceiver", 4),
          ("xenpakTransceiver", 5),
          ("xffTransceiver", 7),
          ("xfpTransceiver", 6),
          ("xfpeTransceiver", 8),
          ("xpakTransceiver", 9))
    )


_TmnxPortTransceiverType_Type.__name__ = "Integer32"
_TmnxPortTransceiverType_Object = MibTableColumn
tmnxPortTransceiverType = _TmnxPortTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 25),
    _TmnxPortTransceiverType_Type()
)
tmnxPortTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverType.setStatus("current")


class _TmnxPortTransceiverCode_Type(Bits):
    """Custom type tmnxPortTransceiverCode based on Bits"""
    namedValues = NamedValues(
        *(("faste-100base-mm-fx", 14),
          ("faste-100base-sm-fx", 15),
          ("gige-1000base-cx", 11),
          ("gige-1000base-lx", 12),
          ("gige-1000base-sx", 13),
          ("gige-1000base-t", 10),
          ("oc12-multimodeshortreach", 6),
          ("oc12-singlemodeinterreach", 5),
          ("oc12-singlemodelongreach", 4),
          ("oc3-multi-modeshortreach", 9),
          ("oc3-singlemodeinterreach", 8),
          ("oc3-singlemodelongreach", 7),
          ("oc48-intermediatereach", 2),
          ("oc48-longreach", 1),
          ("oc48-shortreach", 3),
          ("unknown", 0),
          ("xgige-10gbase-er", 18),
          ("xgige-10gbase-ew", 21),
          ("xgige-10gbase-lr", 17),
          ("xgige-10gbase-lw", 20),
          ("xgige-10gbase-sr", 16),
          ("xgige-10gbase-sw", 19))
    )

_TmnxPortTransceiverCode_Type.__name__ = "Bits"
_TmnxPortTransceiverCode_Object = MibTableColumn
tmnxPortTransceiverCode = _TmnxPortTransceiverCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 26),
    _TmnxPortTransceiverCode_Type()
)
tmnxPortTransceiverCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverCode.setStatus("obsolete")
_TmnxPortTransceiverLaserWaveLen_Type = Unsigned32
_TmnxPortTransceiverLaserWaveLen_Object = MibTableColumn
tmnxPortTransceiverLaserWaveLen = _TmnxPortTransceiverLaserWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 27),
    _TmnxPortTransceiverLaserWaveLen_Type()
)
tmnxPortTransceiverLaserWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverLaserWaveLen.setStatus("current")


class _TmnxPortTransceiverDiagCapable_Type(Integer32):
    """Custom type tmnxPortTransceiverDiagCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notApplicable", 0),
          ("true", 1))
    )


_TmnxPortTransceiverDiagCapable_Type.__name__ = "Integer32"
_TmnxPortTransceiverDiagCapable_Object = MibTableColumn
tmnxPortTransceiverDiagCapable = _TmnxPortTransceiverDiagCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 28),
    _TmnxPortTransceiverDiagCapable_Type()
)
tmnxPortTransceiverDiagCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverDiagCapable.setStatus("current")
_TmnxPortTransceiverModelNumber_Type = TNamedItemOrEmpty
_TmnxPortTransceiverModelNumber_Object = MibTableColumn
tmnxPortTransceiverModelNumber = _TmnxPortTransceiverModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 29),
    _TmnxPortTransceiverModelNumber_Type()
)
tmnxPortTransceiverModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverModelNumber.setStatus("current")


class _TmnxPortSFPConnectorCode_Type(Integer32):
    """Custom type tmnxPortSFPConnectorCode based on Integer32"""
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
              32,
              33,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bncortnc", 4),
          ("copperGigE", 128),
          ("copperPigtail", 33),
          ("fiberChannel-Style1-CopperConnector", 2),
          ("fiberChannel-Style2-CopperConnector", 3),
          ("fiberChannelCoaxialHeaders", 5),
          ("fiberJack", 6),
          ("hssdcII", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalPigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("unknown", 0))
    )


_TmnxPortSFPConnectorCode_Type.__name__ = "Integer32"
_TmnxPortSFPConnectorCode_Object = MibTableColumn
tmnxPortSFPConnectorCode = _TmnxPortSFPConnectorCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 30),
    _TmnxPortSFPConnectorCode_Type()
)
tmnxPortSFPConnectorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPConnectorCode.setStatus("current")
_TmnxPortSFPVendorOUI_Type = Unsigned32
_TmnxPortSFPVendorOUI_Object = MibTableColumn
tmnxPortSFPVendorOUI = _TmnxPortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 31),
    _TmnxPortSFPVendorOUI_Type()
)
tmnxPortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorOUI.setStatus("current")
_TmnxPortSFPVendorManufactureDate_Type = DateAndTime
_TmnxPortSFPVendorManufactureDate_Object = MibTableColumn
tmnxPortSFPVendorManufactureDate = _TmnxPortSFPVendorManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 32),
    _TmnxPortSFPVendorManufactureDate_Type()
)
tmnxPortSFPVendorManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorManufactureDate.setStatus("current")


class _TmnxPortSFPMedia_Type(Integer32):
    """Custom type tmnxPortSFPMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("notApplicable", 0),
          ("sonetsdh", 2))
    )


_TmnxPortSFPMedia_Type.__name__ = "Integer32"
_TmnxPortSFPMedia_Object = MibTableColumn
tmnxPortSFPMedia = _TmnxPortSFPMedia_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 33),
    _TmnxPortSFPMedia_Type()
)
tmnxPortSFPMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPMedia.setStatus("current")
_TmnxPortSFPEquipped_Type = TruthValue
_TmnxPortSFPEquipped_Object = MibTableColumn
tmnxPortSFPEquipped = _TmnxPortSFPEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 34),
    _TmnxPortSFPEquipped_Type()
)
tmnxPortSFPEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPEquipped.setStatus("current")
_TmnxPortEquipped_Type = TruthValue
_TmnxPortEquipped_Object = MibTableColumn
tmnxPortEquipped = _TmnxPortEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 35),
    _TmnxPortEquipped_Type()
)
tmnxPortEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEquipped.setStatus("current")
_TmnxPortLinkStatus_Type = TruthValue
_TmnxPortLinkStatus_Object = MibTableColumn
tmnxPortLinkStatus = _TmnxPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 36),
    _TmnxPortLinkStatus_Type()
)
tmnxPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLinkStatus.setStatus("current")


class _TmnxPortAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tmnxPortAdminStatus based on TmnxPortAdminStatus"""


_TmnxPortAdminStatus_Object = MibTableColumn
tmnxPortAdminStatus = _TmnxPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 37),
    _TmnxPortAdminStatus_Type()
)
tmnxPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAdminStatus.setStatus("current")
_TmnxPortOperStatus_Type = TmnxPortOperStatus
_TmnxPortOperStatus_Object = MibTableColumn
tmnxPortOperStatus = _TmnxPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 38),
    _TmnxPortOperStatus_Type()
)
tmnxPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortOperStatus.setStatus("current")
_TmnxPortState_Type = TmnxPortState
_TmnxPortState_Object = MibTableColumn
tmnxPortState = _TmnxPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 39),
    _TmnxPortState_Type()
)
tmnxPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortState.setStatus("current")
_TmnxPortPrevState_Type = TmnxPortState
_TmnxPortPrevState_Object = MibTableColumn
tmnxPortPrevState = _TmnxPortPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 40),
    _TmnxPortPrevState_Type()
)
tmnxPortPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortPrevState.setStatus("current")
_TmnxPortNumAlarms_Type = Unsigned32
_TmnxPortNumAlarms_Object = MibTableColumn
tmnxPortNumAlarms = _TmnxPortNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 41),
    _TmnxPortNumAlarms_Type()
)
tmnxPortNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNumAlarms.setStatus("current")
_TmnxPortAlarmState_Type = TmnxAlarmState
_TmnxPortAlarmState_Object = MibTableColumn
tmnxPortAlarmState = _TmnxPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 42),
    _TmnxPortAlarmState_Type()
)
tmnxPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAlarmState.setStatus("current")
_TmnxPortLastAlarmEvent_Type = RowPointer
_TmnxPortLastAlarmEvent_Object = MibTableColumn
tmnxPortLastAlarmEvent = _TmnxPortLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 43),
    _TmnxPortLastAlarmEvent_Type()
)
tmnxPortLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastAlarmEvent.setStatus("current")


class _TmnxPortClearAlarms_Type(TmnxActionType):
    """Custom type tmnxPortClearAlarms based on TmnxActionType"""


_TmnxPortClearAlarms_Object = MibTableColumn
tmnxPortClearAlarms = _TmnxPortClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 44),
    _TmnxPortClearAlarms_Type()
)
tmnxPortClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortClearAlarms.setStatus("current")
_TmnxPortSFPVendorSerialNum_Type = TNamedItemOrEmpty
_TmnxPortSFPVendorSerialNum_Object = MibTableColumn
tmnxPortSFPVendorSerialNum = _TmnxPortSFPVendorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 45),
    _TmnxPortSFPVendorSerialNum_Type()
)
tmnxPortSFPVendorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorSerialNum.setStatus("current")
_TmnxPortSFPVendorPartNum_Type = TNamedItemOrEmpty
_TmnxPortSFPVendorPartNum_Object = MibTableColumn
tmnxPortSFPVendorPartNum = _TmnxPortSFPVendorPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 46),
    _TmnxPortSFPVendorPartNum_Type()
)
tmnxPortSFPVendorPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorPartNum.setStatus("current")
_TmnxPortLastStateChanged_Type = TimeStamp
_TmnxPortLastStateChanged_Object = MibTableColumn
tmnxPortLastStateChanged = _TmnxPortLastStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 48),
    _TmnxPortLastStateChanged_Type()
)
tmnxPortLastStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastStateChanged.setStatus("current")
_TmnxPortNumChannels_Type = Unsigned32
_TmnxPortNumChannels_Object = MibTableColumn
tmnxPortNumChannels = _TmnxPortNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 49),
    _TmnxPortNumChannels_Type()
)
tmnxPortNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNumChannels.setStatus("current")
_TmnxPortNetworkEgrQueues_Type = TNamedItemOrEmpty
_TmnxPortNetworkEgrQueues_Object = MibTableColumn
tmnxPortNetworkEgrQueues = _TmnxPortNetworkEgrQueues_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 50),
    _TmnxPortNetworkEgrQueues_Type()
)
tmnxPortNetworkEgrQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortNetworkEgrQueues.setStatus("current")


class _TmnxPortBundleNumber_Type(Integer32):
    """Custom type tmnxPortBundleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_TmnxPortBundleNumber_Type.__name__ = "Integer32"
_TmnxPortBundleNumber_Object = MibTableColumn
tmnxPortBundleNumber = _TmnxPortBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 51),
    _TmnxPortBundleNumber_Type()
)
tmnxPortBundleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortBundleNumber.setStatus("current")
_TmnxPortIsLeaf_Type = TruthValue
_TmnxPortIsLeaf_Object = MibTableColumn
tmnxPortIsLeaf = _TmnxPortIsLeaf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 52),
    _TmnxPortIsLeaf_Type()
)
tmnxPortIsLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIsLeaf.setStatus("current")
_TmnxPortChanType_Type = TmnxMDAChanType
_TmnxPortChanType_Object = MibTableColumn
tmnxPortChanType = _TmnxPortChanType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 53),
    _TmnxPortChanType_Type()
)
tmnxPortChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortChanType.setStatus("current")
_TmnxPortParentPortID_Type = TmnxPortID
_TmnxPortParentPortID_Object = MibTableColumn
tmnxPortParentPortID = _TmnxPortParentPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 54),
    _TmnxPortParentPortID_Type()
)
tmnxPortParentPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortParentPortID.setStatus("current")


class _TmnxPortOpticalCompliance_Type(OctetString):
    """Custom type tmnxPortOpticalCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmnxPortOpticalCompliance_Type.__name__ = "OctetString"
_TmnxPortOpticalCompliance_Object = MibTableColumn
tmnxPortOpticalCompliance = _TmnxPortOpticalCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 55),
    _TmnxPortOpticalCompliance_Type()
)
tmnxPortOpticalCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortOpticalCompliance.setStatus("current")


class _TmnxPortLoadBalanceAlgorithm_Type(Integer32):
    """Custom type tmnxPortLoadBalanceAlgorithm based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("excludeL4", 3),
          ("includeL4", 2),
          ("notApplicable", 0))
    )


_TmnxPortLoadBalanceAlgorithm_Type.__name__ = "Integer32"
_TmnxPortLoadBalanceAlgorithm_Object = MibTableColumn
tmnxPortLoadBalanceAlgorithm = _TmnxPortLoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 56),
    _TmnxPortLoadBalanceAlgorithm_Type()
)
tmnxPortLoadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoadBalanceAlgorithm.setStatus("current")
_TmnxPortEgrPortSchedPlcy_Type = TNamedItemOrEmpty
_TmnxPortEgrPortSchedPlcy_Object = MibTableColumn
tmnxPortEgrPortSchedPlcy = _TmnxPortEgrPortSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 57),
    _TmnxPortEgrPortSchedPlcy_Type()
)
tmnxPortEgrPortSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrPortSchedPlcy.setStatus("current")
_TmnxPortLastClearedTime_Type = TimeStamp
_TmnxPortLastClearedTime_Object = MibTableColumn
tmnxPortLastClearedTime = _TmnxPortLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 58),
    _TmnxPortLastClearedTime_Type()
)
tmnxPortLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastClearedTime.setStatus("current")


class _TmnxPortIngNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortIngNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortIngNamedPoolPlcy_Object = MibTableColumn
tmnxPortIngNamedPoolPlcy = _TmnxPortIngNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 60),
    _TmnxPortIngNamedPoolPlcy_Type()
)
tmnxPortIngNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortIngNamedPoolPlcy.setStatus("current")


class _TmnxPortEgrNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortEgrNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortEgrNamedPoolPlcy_Object = MibTableColumn
tmnxPortEgrNamedPoolPlcy = _TmnxPortEgrNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 61),
    _TmnxPortEgrNamedPoolPlcy_Type()
)
tmnxPortEgrNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrNamedPoolPlcy.setStatus("current")


class _TmnxPortIngPoolPercentRate_Type(Unsigned32):
    """Custom type tmnxPortIngPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxPortIngPoolPercentRate_Type.__name__ = "Unsigned32"
_TmnxPortIngPoolPercentRate_Object = MibTableColumn
tmnxPortIngPoolPercentRate = _TmnxPortIngPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 62),
    _TmnxPortIngPoolPercentRate_Type()
)
tmnxPortIngPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortIngPoolPercentRate.setStatus("current")


class _TmnxPortEgrPoolPercentRate_Type(Unsigned32):
    """Custom type tmnxPortEgrPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxPortEgrPoolPercentRate_Type.__name__ = "Unsigned32"
_TmnxPortEgrPoolPercentRate_Object = MibTableColumn
tmnxPortEgrPoolPercentRate = _TmnxPortEgrPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 63),
    _TmnxPortEgrPoolPercentRate_Type()
)
tmnxPortEgrPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrPoolPercentRate.setStatus("current")


class _TmnxPortDDMEventSuppression_Type(TruthValue):
    """Custom type tmnxPortDDMEventSuppression based on TruthValue"""


_TmnxPortDDMEventSuppression_Object = MibTableColumn
tmnxPortDDMEventSuppression = _TmnxPortDDMEventSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 64),
    _TmnxPortDDMEventSuppression_Type()
)
tmnxPortDDMEventSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDDMEventSuppression.setStatus("current")


class _TmnxPortSFPStatus_Type(Integer32):
    """Custom type tmnxPortSFPStatus based on Integer32"""
    defaultValue = 0

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
        *(("data-corrupt", 3),
          ("ddm-corrupt", 4),
          ("not-equipped", 0),
          ("operational", 1),
          ("read-error", 2),
          ("unsupported", 5))
    )


_TmnxPortSFPStatus_Type.__name__ = "Integer32"
_TmnxPortSFPStatus_Object = MibTableColumn
tmnxPortSFPStatus = _TmnxPortSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 65),
    _TmnxPortSFPStatus_Type()
)
tmnxPortSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPStatus.setStatus("current")
_TmnxPortTestTable_Object = MibTable
tmnxPortTestTable = _TmnxPortTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxPortTestTable.setStatus("current")
_TmnxPortTestEntry_Object = MibTableRow
tmnxPortTestEntry = _TmnxPortTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPortTestEntry.setStatus("current")


class _TmnxPortTestState_Type(Integer32):
    """Custom type tmnxPortTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inTest", 2),
          ("notInTest", 1))
    )


_TmnxPortTestState_Type.__name__ = "Integer32"
_TmnxPortTestState_Object = MibTableColumn
tmnxPortTestState = _TmnxPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 1),
    _TmnxPortTestState_Type()
)
tmnxPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestState.setStatus("current")


class _TmnxPortTestMode_Type(Integer32):
    """Custom type tmnxPortTestMode based on Integer32"""
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
        *(("loopback1", 1),
          ("loopback2", 2),
          ("loopback3", 3),
          ("notApplicable", 0),
          ("singalInsertion", 4))
    )


_TmnxPortTestMode_Type.__name__ = "Integer32"
_TmnxPortTestMode_Object = MibTableColumn
tmnxPortTestMode = _TmnxPortTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 2),
    _TmnxPortTestMode_Type()
)
tmnxPortTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestMode.setStatus("current")
_TmnxPortTestParameter_Type = Unsigned32
_TmnxPortTestParameter_Object = MibTableColumn
tmnxPortTestParameter = _TmnxPortTestParameter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 3),
    _TmnxPortTestParameter_Type()
)
tmnxPortTestParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestParameter.setStatus("current")


class _TmnxPortTestLastResult_Type(Integer32):
    """Custom type tmnxPortTestLastResult based on Integer32"""
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
        *(("failure", 2),
          ("notApplicable", 0),
          ("success", 1),
          ("timeout", 3))
    )


_TmnxPortTestLastResult_Type.__name__ = "Integer32"
_TmnxPortTestLastResult_Object = MibTableColumn
tmnxPortTestLastResult = _TmnxPortTestLastResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 4),
    _TmnxPortTestLastResult_Type()
)
tmnxPortTestLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestLastResult.setStatus("current")
_TmnxPortTestStartTime_Type = DateAndTime
_TmnxPortTestStartTime_Object = MibTableColumn
tmnxPortTestStartTime = _TmnxPortTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 5),
    _TmnxPortTestStartTime_Type()
)
tmnxPortTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestStartTime.setStatus("current")
_TmnxPortTestEndTime_Type = DateAndTime
_TmnxPortTestEndTime_Object = MibTableColumn
tmnxPortTestEndTime = _TmnxPortTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 6),
    _TmnxPortTestEndTime_Type()
)
tmnxPortTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestEndTime.setStatus("current")


class _TmnxPortTestDuration_Type(Integer32):
    """Custom type tmnxPortTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TmnxPortTestDuration_Type.__name__ = "Integer32"
_TmnxPortTestDuration_Object = MibTableColumn
tmnxPortTestDuration = _TmnxPortTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 7),
    _TmnxPortTestDuration_Type()
)
tmnxPortTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestDuration.setStatus("current")


class _TmnxPortTestAction_Type(Integer32):
    """Custom type tmnxPortTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startTest", 2),
          ("stopTest", 3))
    )


_TmnxPortTestAction_Type.__name__ = "Integer32"
_TmnxPortTestAction_Object = MibTableColumn
tmnxPortTestAction = _TmnxPortTestAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 8),
    _TmnxPortTestAction_Type()
)
tmnxPortTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestAction.setStatus("current")
_TmnxPortEtherTable_Object = MibTable
tmnxPortEtherTable = _TmnxPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxPortEtherTable.setStatus("current")
_TmnxPortEtherEntry_Object = MibTableRow
tmnxPortEtherEntry = _TmnxPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1)
)
tmnxPortEtherEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortEtherEntry.setStatus("current")


class _TmnxPortEtherMTU_Type(Unsigned32):
    """Custom type tmnxPortEtherMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9212),
    )


_TmnxPortEtherMTU_Type.__name__ = "Unsigned32"
_TmnxPortEtherMTU_Object = MibTableColumn
tmnxPortEtherMTU = _TmnxPortEtherMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 1),
    _TmnxPortEtherMTU_Type()
)
tmnxPortEtherMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherMTU.setUnits("bytes")


class _TmnxPortEtherDuplex_Type(Integer32):
    """Custom type tmnxPortEtherDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 0))
    )


_TmnxPortEtherDuplex_Type.__name__ = "Integer32"
_TmnxPortEtherDuplex_Object = MibTableColumn
tmnxPortEtherDuplex = _TmnxPortEtherDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 2),
    _TmnxPortEtherDuplex_Type()
)
tmnxPortEtherDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDuplex.setStatus("current")


class _TmnxPortEtherSpeed_Type(Integer32):
    """Custom type tmnxPortEtherSpeed based on Integer32"""
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
        *(("notApplicable", 0),
          ("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4))
    )


_TmnxPortEtherSpeed_Type.__name__ = "Integer32"
_TmnxPortEtherSpeed_Object = MibTableColumn
tmnxPortEtherSpeed = _TmnxPortEtherSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 3),
    _TmnxPortEtherSpeed_Type()
)
tmnxPortEtherSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSpeed.setStatus("current")


class _TmnxPortEtherAutoNegotiate_Type(Integer32):
    """Custom type tmnxPortEtherAutoNegotiate based on Integer32"""
    defaultValue = 1

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
        *(("false", 2),
          ("limited", 3),
          ("notApplicable", 0),
          ("true", 1))
    )


_TmnxPortEtherAutoNegotiate_Type.__name__ = "Integer32"
_TmnxPortEtherAutoNegotiate_Object = MibTableColumn
tmnxPortEtherAutoNegotiate = _TmnxPortEtherAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 4),
    _TmnxPortEtherAutoNegotiate_Type()
)
tmnxPortEtherAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherAutoNegotiate.setStatus("current")


class _TmnxPortEtherOperDuplex_Type(Integer32):
    """Custom type tmnxPortEtherOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 0))
    )


_TmnxPortEtherOperDuplex_Type.__name__ = "Integer32"
_TmnxPortEtherOperDuplex_Object = MibTableColumn
tmnxPortEtherOperDuplex = _TmnxPortEtherOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 5),
    _TmnxPortEtherOperDuplex_Type()
)
tmnxPortEtherOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherOperDuplex.setStatus("current")
_TmnxPortEtherOperSpeed_Type = Unsigned32
_TmnxPortEtherOperSpeed_Object = MibTableColumn
tmnxPortEtherOperSpeed = _TmnxPortEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 6),
    _TmnxPortEtherOperSpeed_Type()
)
tmnxPortEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherOperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherOperSpeed.setUnits("mega-bits per second")


class _TmnxPortEtherAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxPortEtherAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxPortEtherAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxPortEtherAcctPolicyId_Object = MibTableColumn
tmnxPortEtherAcctPolicyId = _TmnxPortEtherAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 7),
    _TmnxPortEtherAcctPolicyId_Type()
)
tmnxPortEtherAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherAcctPolicyId.setStatus("current")


class _TmnxPortEtherCollectStats_Type(TruthValue):
    """Custom type tmnxPortEtherCollectStats based on TruthValue"""


_TmnxPortEtherCollectStats_Object = MibTableColumn
tmnxPortEtherCollectStats = _TmnxPortEtherCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 8),
    _TmnxPortEtherCollectStats_Type()
)
tmnxPortEtherCollectStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCollectStats.setStatus("current")


class _TmnxPortEtherMDIMDIX_Type(Integer32):
    """Custom type tmnxPortEtherMDIMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("unknown", 0))
    )


_TmnxPortEtherMDIMDIX_Type.__name__ = "Integer32"
_TmnxPortEtherMDIMDIX_Object = MibTableColumn
tmnxPortEtherMDIMDIX = _TmnxPortEtherMDIMDIX_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 9),
    _TmnxPortEtherMDIMDIX_Type()
)
tmnxPortEtherMDIMDIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherMDIMDIX.setStatus("current")


class _TmnxPortEtherXGigMode_Type(Integer32):
    """Custom type tmnxPortEtherXGigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("notApplicable", 0),
          ("wan", 2))
    )


_TmnxPortEtherXGigMode_Type.__name__ = "Integer32"
_TmnxPortEtherXGigMode_Object = MibTableColumn
tmnxPortEtherXGigMode = _TmnxPortEtherXGigMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 10),
    _TmnxPortEtherXGigMode_Type()
)
tmnxPortEtherXGigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherXGigMode.setStatus("current")


class _TmnxPortEtherEgressRate_Type(Integer32):
    """Custom type tmnxPortEtherEgressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_TmnxPortEtherEgressRate_Type.__name__ = "Integer32"
_TmnxPortEtherEgressRate_Object = MibTableColumn
tmnxPortEtherEgressRate = _TmnxPortEtherEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 11),
    _TmnxPortEtherEgressRate_Type()
)
tmnxPortEtherEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherEgressRate.setStatus("current")


class _TmnxPortEtherDot1qEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherDot1qEtype based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherDot1qEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherDot1qEtype_Object = MibTableColumn
tmnxPortEtherDot1qEtype = _TmnxPortEtherDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 12),
    _TmnxPortEtherDot1qEtype_Type()
)
tmnxPortEtherDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDot1qEtype.setStatus("current")


class _TmnxPortEtherQinqEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherQinqEtype based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherQinqEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherQinqEtype_Object = MibTableColumn
tmnxPortEtherQinqEtype = _TmnxPortEtherQinqEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 13),
    _TmnxPortEtherQinqEtype_Type()
)
tmnxPortEtherQinqEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherQinqEtype.setStatus("current")


class _TmnxPortEtherIngressRate_Type(Integer32):
    """Custom type tmnxPortEtherIngressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_TmnxPortEtherIngressRate_Type.__name__ = "Integer32"
_TmnxPortEtherIngressRate_Object = MibTableColumn
tmnxPortEtherIngressRate = _TmnxPortEtherIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 14),
    _TmnxPortEtherIngressRate_Type()
)
tmnxPortEtherIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherIngressRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherIngressRate.setUnits("mega-bits per second")


class _TmnxPortEtherReportAlarm_Type(TmnxPortEtherReportStatus):
    """Custom type tmnxPortEtherReportAlarm based on TmnxPortEtherReportStatus"""
    defaultBinValue = "0011"


_TmnxPortEtherReportAlarm_Object = MibTableColumn
tmnxPortEtherReportAlarm = _TmnxPortEtherReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 15),
    _TmnxPortEtherReportAlarm_Type()
)
tmnxPortEtherReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherReportAlarm.setStatus("current")
_TmnxPortEtherReportAlarmStatus_Type = TmnxPortEtherReportStatus
_TmnxPortEtherReportAlarmStatus_Object = MibTableColumn
tmnxPortEtherReportAlarmStatus = _TmnxPortEtherReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 16),
    _TmnxPortEtherReportAlarmStatus_Type()
)
tmnxPortEtherReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherReportAlarmStatus.setStatus("current")
_TmnxPortEtherPkts1519toMax_Type = Counter32
_TmnxPortEtherPkts1519toMax_Object = MibTableColumn
tmnxPortEtherPkts1519toMax = _TmnxPortEtherPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 17),
    _TmnxPortEtherPkts1519toMax_Type()
)
tmnxPortEtherPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherPkts1519toMax.setUnits("Packets")
_TmnxPortEtherHCOverPkts1519toMax_Type = Counter32
_TmnxPortEtherHCOverPkts1519toMax_Object = MibTableColumn
tmnxPortEtherHCOverPkts1519toMax = _TmnxPortEtherHCOverPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 18),
    _TmnxPortEtherHCOverPkts1519toMax_Type()
)
tmnxPortEtherHCOverPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherHCOverPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherHCOverPkts1519toMax.setUnits("Packets")
_TmnxPortEtherHCPkts1519toMax_Type = Counter64
_TmnxPortEtherHCPkts1519toMax_Object = MibTableColumn
tmnxPortEtherHCPkts1519toMax = _TmnxPortEtherHCPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 19),
    _TmnxPortEtherHCPkts1519toMax_Type()
)
tmnxPortEtherHCPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherHCPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherHCPkts1519toMax.setUnits("Packets")


class _TmnxPortEtherLacpTunnel_Type(TruthValue):
    """Custom type tmnxPortEtherLacpTunnel based on TruthValue"""


_TmnxPortEtherLacpTunnel_Object = MibTableColumn
tmnxPortEtherLacpTunnel = _TmnxPortEtherLacpTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 20),
    _TmnxPortEtherLacpTunnel_Type()
)
tmnxPortEtherLacpTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherLacpTunnel.setStatus("current")


class _TmnxPortEtherDownWhenLoopedEnabled_Type(TruthValue):
    """Custom type tmnxPortEtherDownWhenLoopedEnabled based on TruthValue"""


_TmnxPortEtherDownWhenLoopedEnabled_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedEnabled = _TmnxPortEtherDownWhenLoopedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 21),
    _TmnxPortEtherDownWhenLoopedEnabled_Type()
)
tmnxPortEtherDownWhenLoopedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedEnabled.setStatus("current")


class _TmnxPortEtherDownWhenLoopedKeepAlive_Type(Unsigned32):
    """Custom type tmnxPortEtherDownWhenLoopedKeepAlive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxPortEtherDownWhenLoopedKeepAlive_Type.__name__ = "Unsigned32"
_TmnxPortEtherDownWhenLoopedKeepAlive_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedKeepAlive = _TmnxPortEtherDownWhenLoopedKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 22),
    _TmnxPortEtherDownWhenLoopedKeepAlive_Type()
)
tmnxPortEtherDownWhenLoopedKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedKeepAlive.setUnits("seconds")


class _TmnxPortEtherDownWhenLoopedRetry_Type(Unsigned32):
    """Custom type tmnxPortEtherDownWhenLoopedRetry based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 160),
    )


_TmnxPortEtherDownWhenLoopedRetry_Type.__name__ = "Unsigned32"
_TmnxPortEtherDownWhenLoopedRetry_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedRetry = _TmnxPortEtherDownWhenLoopedRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 23),
    _TmnxPortEtherDownWhenLoopedRetry_Type()
)
tmnxPortEtherDownWhenLoopedRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedRetry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedRetry.setUnits("seconds")


class _TmnxPortEtherDownWhenLoopedState_Type(Integer32):
    """Custom type tmnxPortEtherDownWhenLoopedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopDetected", 2),
          ("noLoopDetected", 1))
    )


_TmnxPortEtherDownWhenLoopedState_Type.__name__ = "Integer32"
_TmnxPortEtherDownWhenLoopedState_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedState = _TmnxPortEtherDownWhenLoopedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 24),
    _TmnxPortEtherDownWhenLoopedState_Type()
)
tmnxPortEtherDownWhenLoopedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedState.setStatus("current")


class _TmnxPortEtherPBBEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherPBBEtype based on Unsigned32"""
    defaultHexValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherPBBEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherPBBEtype_Object = MibTableColumn
tmnxPortEtherPBBEtype = _TmnxPortEtherPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 25),
    _TmnxPortEtherPBBEtype_Type()
)
tmnxPortEtherPBBEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherPBBEtype.setStatus("current")


class _TmnxPortEtherReasonDownFlags_Type(Bits):
    """Custom type tmnxPortEtherReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("linklossFwd", 1),
          ("unknown", 0))
    )

_TmnxPortEtherReasonDownFlags_Type.__name__ = "Bits"
_TmnxPortEtherReasonDownFlags_Object = MibTableColumn
tmnxPortEtherReasonDownFlags = _TmnxPortEtherReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 26),
    _TmnxPortEtherReasonDownFlags_Type()
)
tmnxPortEtherReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherReasonDownFlags.setStatus("current")
_TmnxSonetTable_Object = MibTable
tmnxSonetTable = _TmnxSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxSonetTable.setStatus("current")
_TmnxSonetEntry_Object = MibTableRow
tmnxSonetEntry = _TmnxSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1)
)
tmnxSonetEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetEntry.setStatus("current")


class _TmnxSonetSpeed_Type(Integer32):
    """Custom type tmnxSonetSpeed based on Integer32"""
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
        *(("oc1", 6),
          ("oc12", 2),
          ("oc192", 4),
          ("oc3", 1),
          ("oc48", 3),
          ("oc768", 5))
    )


_TmnxSonetSpeed_Type.__name__ = "Integer32"
_TmnxSonetSpeed_Object = MibTableColumn
tmnxSonetSpeed = _TmnxSonetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 1),
    _TmnxSonetSpeed_Type()
)
tmnxSonetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSpeed.setStatus("current")


class _TmnxSonetClockSource_Type(Integer32):
    """Custom type tmnxSonetClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopTimed", 1),
          ("nodeTimed", 2))
    )


_TmnxSonetClockSource_Type.__name__ = "Integer32"
_TmnxSonetClockSource_Object = MibTableColumn
tmnxSonetClockSource = _TmnxSonetClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 2),
    _TmnxSonetClockSource_Type()
)
tmnxSonetClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetClockSource.setStatus("current")


class _TmnxSonetFraming_Type(Integer32):
    """Custom type tmnxSonetFraming based on Integer32"""
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
        *(("sdh", 3),
          ("sonet", 2),
          ("unknown", 1))
    )


_TmnxSonetFraming_Type.__name__ = "Integer32"
_TmnxSonetFraming_Object = MibTableColumn
tmnxSonetFraming = _TmnxSonetFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 3),
    _TmnxSonetFraming_Type()
)
tmnxSonetFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetFraming.setStatus("current")


class _TmnxSonetReportAlarm_Type(Bits):
    """Custom type tmnxSonetReportAlarm based on Bits"""
    defaultBinValue = "0101000111"

    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )

_TmnxSonetReportAlarm_Type.__name__ = "Bits"
_TmnxSonetReportAlarm_Object = MibTableColumn
tmnxSonetReportAlarm = _TmnxSonetReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 4),
    _TmnxSonetReportAlarm_Type()
)
tmnxSonetReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetReportAlarm.setStatus("current")


class _TmnxSonetBerSdThreshold_Type(Unsigned32):
    """Custom type tmnxSonetBerSdThreshold based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_TmnxSonetBerSdThreshold_Type.__name__ = "Unsigned32"
_TmnxSonetBerSdThreshold_Object = MibTableColumn
tmnxSonetBerSdThreshold = _TmnxSonetBerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 5),
    _TmnxSonetBerSdThreshold_Type()
)
tmnxSonetBerSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetBerSdThreshold.setStatus("current")


class _TmnxSonetBerSfThreshold_Type(Unsigned32):
    """Custom type tmnxSonetBerSfThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_TmnxSonetBerSfThreshold_Type.__name__ = "Unsigned32"
_TmnxSonetBerSfThreshold_Object = MibTableColumn
tmnxSonetBerSfThreshold = _TmnxSonetBerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 6),
    _TmnxSonetBerSfThreshold_Type()
)
tmnxSonetBerSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetBerSfThreshold.setStatus("current")


class _TmnxSonetAps_Type(TruthValue):
    """Custom type tmnxSonetAps based on TruthValue"""


_TmnxSonetAps_Object = MibTableColumn
tmnxSonetAps = _TmnxSonetAps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 7),
    _TmnxSonetAps_Type()
)
tmnxSonetAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetAps.setStatus("obsolete")


class _TmnxSonetApsAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tmnxSonetApsAdminStatus based on TmnxPortAdminStatus"""


_TmnxSonetApsAdminStatus_Object = MibTableColumn
tmnxSonetApsAdminStatus = _TmnxSonetApsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 8),
    _TmnxSonetApsAdminStatus_Type()
)
tmnxSonetApsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAdminStatus.setStatus("obsolete")
_TmnxSonetApsOperStatus_Type = TmnxPortOperStatus
_TmnxSonetApsOperStatus_Object = MibTableColumn
tmnxSonetApsOperStatus = _TmnxSonetApsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 9),
    _TmnxSonetApsOperStatus_Type()
)
tmnxSonetApsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsOperStatus.setStatus("obsolete")


class _TmnxSonetApsAuthKey_Type(OctetString):
    """Custom type tmnxSonetApsAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxSonetApsAuthKey_Type.__name__ = "OctetString"
_TmnxSonetApsAuthKey_Object = MibTableColumn
tmnxSonetApsAuthKey = _TmnxSonetApsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 10),
    _TmnxSonetApsAuthKey_Type()
)
tmnxSonetApsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAuthKey.setStatus("obsolete")


class _TmnxSonetApsNeighborAddr_Type(IpAddress):
    """Custom type tmnxSonetApsNeighborAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxSonetApsNeighborAddr_Object = MibTableColumn
tmnxSonetApsNeighborAddr = _TmnxSonetApsNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 11),
    _TmnxSonetApsNeighborAddr_Type()
)
tmnxSonetApsNeighborAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsNeighborAddr.setStatus("obsolete")


class _TmnxSonetApsAdvertiseInterval_Type(TimeInterval):
    """Custom type tmnxSonetApsAdvertiseInterval based on TimeInterval"""
    defaultValue = 1000


_TmnxSonetApsAdvertiseInterval_Object = MibTableColumn
tmnxSonetApsAdvertiseInterval = _TmnxSonetApsAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 12),
    _TmnxSonetApsAdvertiseInterval_Type()
)
tmnxSonetApsAdvertiseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseInterval.setUnits("milliseconds")
_TmnxSonetApsAdvertiseTimeLeft_Type = TimeInterval
_TmnxSonetApsAdvertiseTimeLeft_Object = MibTableColumn
tmnxSonetApsAdvertiseTimeLeft = _TmnxSonetApsAdvertiseTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 13),
    _TmnxSonetApsAdvertiseTimeLeft_Type()
)
tmnxSonetApsAdvertiseTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseTimeLeft.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseTimeLeft.setUnits("milliseconds")


class _TmnxSonetApsHoldTime_Type(TimeInterval):
    """Custom type tmnxSonetApsHoldTime based on TimeInterval"""
    defaultValue = 3000


_TmnxSonetApsHoldTime_Object = MibTableColumn
tmnxSonetApsHoldTime = _TmnxSonetApsHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 14),
    _TmnxSonetApsHoldTime_Type()
)
tmnxSonetApsHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTime.setUnits("milliseconds")
_TmnxSonetApsHoldTimeLeft_Type = TimeInterval
_TmnxSonetApsHoldTimeLeft_Object = MibTableColumn
tmnxSonetApsHoldTimeLeft = _TmnxSonetApsHoldTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 15),
    _TmnxSonetApsHoldTimeLeft_Type()
)
tmnxSonetApsHoldTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTimeLeft.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTimeLeft.setUnits("milliseconds")


class _TmnxSonetLoopback_Type(Integer32):
    """Custom type tmnxSonetLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("line", 1),
          ("none", 0))
    )


_TmnxSonetLoopback_Type.__name__ = "Integer32"
_TmnxSonetLoopback_Object = MibTableColumn
tmnxSonetLoopback = _TmnxSonetLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 16),
    _TmnxSonetLoopback_Type()
)
tmnxSonetLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetLoopback.setStatus("current")


class _TmnxSonetReportAlarmStatus_Type(Bits):
    """Custom type tmnxSonetReportAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )

_TmnxSonetReportAlarmStatus_Type.__name__ = "Bits"
_TmnxSonetReportAlarmStatus_Object = MibTableColumn
tmnxSonetReportAlarmStatus = _TmnxSonetReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 17),
    _TmnxSonetReportAlarmStatus_Type()
)
tmnxSonetReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetReportAlarmStatus.setStatus("current")


class _TmnxSonetSectionTraceMode_Type(Integer32):
    """Custom type tmnxSonetSectionTraceMode based on Integer32"""
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
        *(("byte", 2),
          ("increment-z0", 1),
          ("string", 3))
    )


_TmnxSonetSectionTraceMode_Type.__name__ = "Integer32"
_TmnxSonetSectionTraceMode_Object = MibTableColumn
tmnxSonetSectionTraceMode = _TmnxSonetSectionTraceMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 18),
    _TmnxSonetSectionTraceMode_Type()
)
tmnxSonetSectionTraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSectionTraceMode.setStatus("current")


class _TmnxSonetJ0String_Type(OctetString):
    """Custom type tmnxSonetJ0String based on OctetString"""
    defaultHexValue = "01"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSonetJ0String_Type.__name__ = "OctetString"
_TmnxSonetJ0String_Object = MibTableColumn
tmnxSonetJ0String = _TmnxSonetJ0String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 19),
    _TmnxSonetJ0String_Type()
)
tmnxSonetJ0String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetJ0String.setStatus("current")


class _TmnxSonetMonS1Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonS1Byte based on Unsigned32"""
    defaultHexValue = 204

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonS1Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonS1Byte_Object = MibTableColumn
tmnxSonetMonS1Byte = _TmnxSonetMonS1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 20),
    _TmnxSonetMonS1Byte_Type()
)
tmnxSonetMonS1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonS1Byte.setStatus("current")


class _TmnxSonetMonJ0String_Type(OctetString):
    """Custom type tmnxSonetMonJ0String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSonetMonJ0String_Type.__name__ = "OctetString"
_TmnxSonetMonJ0String_Object = MibTableColumn
tmnxSonetMonJ0String = _TmnxSonetMonJ0String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 21),
    _TmnxSonetMonJ0String_Type()
)
tmnxSonetMonJ0String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonJ0String.setStatus("current")


class _TmnxSonetMonK1Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonK1Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonK1Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonK1Byte_Object = MibTableColumn
tmnxSonetMonK1Byte = _TmnxSonetMonK1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 22),
    _TmnxSonetMonK1Byte_Type()
)
tmnxSonetMonK1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonK1Byte.setStatus("current")


class _TmnxSonetMonK2Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonK2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonK2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonK2Byte_Object = MibTableColumn
tmnxSonetMonK2Byte = _TmnxSonetMonK2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 23),
    _TmnxSonetMonK2Byte_Type()
)
tmnxSonetMonK2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonK2Byte.setStatus("current")


class _TmnxSonetSingleFiber_Type(TruthValue):
    """Custom type tmnxSonetSingleFiber based on TruthValue"""


_TmnxSonetSingleFiber_Object = MibTableColumn
tmnxSonetSingleFiber = _TmnxSonetSingleFiber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 24),
    _TmnxSonetSingleFiber_Type()
)
tmnxSonetSingleFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSingleFiber.setStatus("current")


class _TmnxSonetHoldTimeUp_Type(Unsigned32):
    """Custom type tmnxSonetHoldTimeUp based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxSonetHoldTimeUp_Type.__name__ = "Unsigned32"
_TmnxSonetHoldTimeUp_Object = MibTableColumn
tmnxSonetHoldTimeUp = _TmnxSonetHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 25),
    _TmnxSonetHoldTimeUp_Type()
)
tmnxSonetHoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeUp.setUnits("100s of milliseconds")


class _TmnxSonetHoldTimeDown_Type(Unsigned32):
    """Custom type tmnxSonetHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxSonetHoldTimeDown_Type.__name__ = "Unsigned32"
_TmnxSonetHoldTimeDown_Object = MibTableColumn
tmnxSonetHoldTimeDown = _TmnxSonetHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 26),
    _TmnxSonetHoldTimeDown_Type()
)
tmnxSonetHoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeDown.setUnits("100s of milliseconds")
_TmnxSonetPathTable_Object = MibTable
tmnxSonetPathTable = _TmnxSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxSonetPathTable.setStatus("current")
_TmnxSonetPathEntry_Object = MibTableRow
tmnxSonetPathEntry = _TmnxSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1)
)
tmnxSonetPathEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetPathEntry.setStatus("current")
_TmnxSonetPathRowStatus_Type = RowStatus
_TmnxSonetPathRowStatus_Object = MibTableColumn
tmnxSonetPathRowStatus = _TmnxSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 1),
    _TmnxSonetPathRowStatus_Type()
)
tmnxSonetPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathRowStatus.setStatus("current")
_TmnxSonetPathLastChangeTime_Type = TimeStamp
_TmnxSonetPathLastChangeTime_Object = MibTableColumn
tmnxSonetPathLastChangeTime = _TmnxSonetPathLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 2),
    _TmnxSonetPathLastChangeTime_Type()
)
tmnxSonetPathLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathLastChangeTime.setStatus("current")


class _TmnxSonetPathMTU_Type(Unsigned32):
    """Custom type tmnxSonetPathMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxSonetPathMTU_Type.__name__ = "Unsigned32"
_TmnxSonetPathMTU_Object = MibTableColumn
tmnxSonetPathMTU = _TmnxSonetPathMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 3),
    _TmnxSonetPathMTU_Type()
)
tmnxSonetPathMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathMTU.setUnits("bytes")
_TmnxSonetPathScramble_Type = TruthValue
_TmnxSonetPathScramble_Object = MibTableColumn
tmnxSonetPathScramble = _TmnxSonetPathScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 4),
    _TmnxSonetPathScramble_Type()
)
tmnxSonetPathScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathScramble.setStatus("current")


class _TmnxSonetPathC2Byte_Type(Unsigned32):
    """Custom type tmnxSonetPathC2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxSonetPathC2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetPathC2Byte_Object = MibTableColumn
tmnxSonetPathC2Byte = _TmnxSonetPathC2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 5),
    _TmnxSonetPathC2Byte_Type()
)
tmnxSonetPathC2Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathC2Byte.setStatus("current")


class _TmnxSonetPathJ1String_Type(OctetString):
    """Custom type tmnxSonetPathJ1String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_TmnxSonetPathJ1String_Type.__name__ = "OctetString"
_TmnxSonetPathJ1String_Object = MibTableColumn
tmnxSonetPathJ1String = _TmnxSonetPathJ1String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 6),
    _TmnxSonetPathJ1String_Type()
)
tmnxSonetPathJ1String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathJ1String.setStatus("current")


class _TmnxSonetPathCRC_Type(Integer32):
    """Custom type tmnxSonetPathCRC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxSonetPathCRC_Type.__name__ = "Integer32"
_TmnxSonetPathCRC_Object = MibTableColumn
tmnxSonetPathCRC = _TmnxSonetPathCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 7),
    _TmnxSonetPathCRC_Type()
)
tmnxSonetPathCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathCRC.setStatus("current")
_TmnxSonetPathOperMTU_Type = Unsigned32
_TmnxSonetPathOperMTU_Object = MibTableColumn
tmnxSonetPathOperMTU = _TmnxSonetPathOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 8),
    _TmnxSonetPathOperMTU_Type()
)
tmnxSonetPathOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMTU.setUnits("bytes")
_TmnxSonetPathOperMRU_Type = Unsigned32
_TmnxSonetPathOperMRU_Object = MibTableColumn
tmnxSonetPathOperMRU = _TmnxSonetPathOperMRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 9),
    _TmnxSonetPathOperMRU_Type()
)
tmnxSonetPathOperMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMRU.setUnits("bytes")


class _TmnxSonetPathReportAlarm_Type(Bits):
    """Custom type tmnxSonetPathReportAlarm based on Bits"""
    defaultBinValue = "00100101"

    namedValues = NamedValues(
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )

_TmnxSonetPathReportAlarm_Type.__name__ = "Bits"
_TmnxSonetPathReportAlarm_Object = MibTableColumn
tmnxSonetPathReportAlarm = _TmnxSonetPathReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 10),
    _TmnxSonetPathReportAlarm_Type()
)
tmnxSonetPathReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathReportAlarm.setStatus("current")


class _TmnxSonetPathAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxSonetPathAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxSonetPathAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxSonetPathAcctPolicyId_Object = MibTableColumn
tmnxSonetPathAcctPolicyId = _TmnxSonetPathAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 11),
    _TmnxSonetPathAcctPolicyId_Type()
)
tmnxSonetPathAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathAcctPolicyId.setStatus("current")


class _TmnxSonetPathCollectStats_Type(TruthValue):
    """Custom type tmnxSonetPathCollectStats based on TruthValue"""


_TmnxSonetPathCollectStats_Object = MibTableColumn
tmnxSonetPathCollectStats = _TmnxSonetPathCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 12),
    _TmnxSonetPathCollectStats_Type()
)
tmnxSonetPathCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathCollectStats.setStatus("current")


class _TmnxSonetPathReportAlarmStatus_Type(Bits):
    """Custom type tmnxSonetPathReportAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )

_TmnxSonetPathReportAlarmStatus_Type.__name__ = "Bits"
_TmnxSonetPathReportAlarmStatus_Object = MibTableColumn
tmnxSonetPathReportAlarmStatus = _TmnxSonetPathReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 13),
    _TmnxSonetPathReportAlarmStatus_Type()
)
tmnxSonetPathReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathReportAlarmStatus.setStatus("current")


class _TmnxSonetPathMonC2Byte_Type(Unsigned32):
    """Custom type tmnxSonetPathMonC2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetPathMonC2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetPathMonC2Byte_Object = MibTableColumn
tmnxSonetPathMonC2Byte = _TmnxSonetPathMonC2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 14),
    _TmnxSonetPathMonC2Byte_Type()
)
tmnxSonetPathMonC2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathMonC2Byte.setStatus("current")


class _TmnxSonetPathMonJ1String_Type(OctetString):
    """Custom type tmnxSonetPathMonJ1String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxSonetPathMonJ1String_Type.__name__ = "OctetString"
_TmnxSonetPathMonJ1String_Object = MibTableColumn
tmnxSonetPathMonJ1String = _TmnxSonetPathMonJ1String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 15),
    _TmnxSonetPathMonJ1String_Type()
)
tmnxSonetPathMonJ1String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathMonJ1String.setStatus("current")


class _TmnxSonetPathType_Type(Integer32):
    """Custom type tmnxSonetPathType based on Integer32"""
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
        *(("ds3", 1),
          ("e3", 2),
          ("tug-2", 4),
          ("tug-3", 5),
          ("vtg", 3))
    )


_TmnxSonetPathType_Type.__name__ = "Integer32"
_TmnxSonetPathType_Object = MibTableColumn
tmnxSonetPathType = _TmnxSonetPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 16),
    _TmnxSonetPathType_Type()
)
tmnxSonetPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathType.setStatus("obsolete")
_TmnxSonetPathChildType_Type = TmnxMDAChanType
_TmnxSonetPathChildType_Object = MibTableColumn
tmnxSonetPathChildType = _TmnxSonetPathChildType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 17),
    _TmnxSonetPathChildType_Type()
)
tmnxSonetPathChildType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathChildType.setStatus("current")
_TmnxPortTypeTable_Object = MibTable
tmnxPortTypeTable = _TmnxPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxPortTypeTable.setStatus("current")
_TmnxPortTypeEntry_Object = MibTableRow
tmnxPortTypeEntry = _TmnxPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1)
)
tmnxPortTypeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortTypeEntry.setStatus("current")
_TmnxPortTypeIndex_Type = TmnxPortType
_TmnxPortTypeIndex_Object = MibTableColumn
tmnxPortTypeIndex = _TmnxPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 1),
    _TmnxPortTypeIndex_Type()
)
tmnxPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortTypeIndex.setStatus("current")
_TmnxPortTypeName_Type = TNamedItemOrEmpty
_TmnxPortTypeName_Object = MibTableColumn
tmnxPortTypeName = _TmnxPortTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 2),
    _TmnxPortTypeName_Type()
)
tmnxPortTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeName.setStatus("current")
_TmnxPortTypeDescription_Type = TItemDescription
_TmnxPortTypeDescription_Object = MibTableColumn
tmnxPortTypeDescription = _TmnxPortTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 3),
    _TmnxPortTypeDescription_Type()
)
tmnxPortTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeDescription.setStatus("current")
_TmnxPortTypeStatus_Type = TruthValue
_TmnxPortTypeStatus_Object = MibTableColumn
tmnxPortTypeStatus = _TmnxPortTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 4),
    _TmnxPortTypeStatus_Type()
)
tmnxPortTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeStatus.setStatus("current")
_TmnxPortConnectTypeTable_Object = MibTable
tmnxPortConnectTypeTable = _TmnxPortConnectTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tmnxPortConnectTypeTable.setStatus("current")
_TmnxPortConnectTypeEntry_Object = MibTableRow
tmnxPortConnectTypeEntry = _TmnxPortConnectTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1)
)
tmnxPortConnectTypeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortConnectTypeEntry.setStatus("current")
_TmnxPortConnectTypeIndex_Type = TmnxPortConnectorType
_TmnxPortConnectTypeIndex_Object = MibTableColumn
tmnxPortConnectTypeIndex = _TmnxPortConnectTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 1),
    _TmnxPortConnectTypeIndex_Type()
)
tmnxPortConnectTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeIndex.setStatus("current")
_TmnxPortConnectTypeName_Type = TNamedItemOrEmpty
_TmnxPortConnectTypeName_Object = MibTableColumn
tmnxPortConnectTypeName = _TmnxPortConnectTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 2),
    _TmnxPortConnectTypeName_Type()
)
tmnxPortConnectTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeName.setStatus("current")
_TmnxPortConnectTypeDescription_Type = TItemDescription
_TmnxPortConnectTypeDescription_Object = MibTableColumn
tmnxPortConnectTypeDescription = _TmnxPortConnectTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 3),
    _TmnxPortConnectTypeDescription_Type()
)
tmnxPortConnectTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeDescription.setStatus("current")
_TmnxPortConnectTypeStatus_Type = TruthValue
_TmnxPortConnectTypeStatus_Object = MibTableColumn
tmnxPortConnectTypeStatus = _TmnxPortConnectTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 4),
    _TmnxPortConnectTypeStatus_Type()
)
tmnxPortConnectTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeStatus.setStatus("current")
_TmnxPortFCStatsTable_Object = MibTable
tmnxPortFCStatsTable = _TmnxPortFCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tmnxPortFCStatsTable.setStatus("obsolete")
_TmnxPortFCStatsEntry_Object = MibTableRow
tmnxPortFCStatsEntry = _TmnxPortFCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1)
)
tmnxPortFCStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortFCStatsEntry.setStatus("obsolete")
_TmnxPortFCStatsIndex_Type = TFCName
_TmnxPortFCStatsIndex_Object = MibTableColumn
tmnxPortFCStatsIndex = _TmnxPortFCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 1),
    _TmnxPortFCStatsIndex_Type()
)
tmnxPortFCStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIndex.setStatus("obsolete")
_TmnxPortFCStatsIngFwdInProfPkts_Type = Counter64
_TmnxPortFCStatsIngFwdInProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngFwdInProfPkts = _TmnxPortFCStatsIngFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 2),
    _TmnxPortFCStatsIngFwdInProfPkts_Type()
)
tmnxPortFCStatsIngFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdOutProfPkts_Type = Counter64
_TmnxPortFCStatsIngFwdOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngFwdOutProfPkts = _TmnxPortFCStatsIngFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 3),
    _TmnxPortFCStatsIngFwdOutProfPkts_Type()
)
tmnxPortFCStatsIngFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdInProfOcts_Type = Counter64
_TmnxPortFCStatsIngFwdInProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngFwdInProfOcts = _TmnxPortFCStatsIngFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 4),
    _TmnxPortFCStatsIngFwdInProfOcts_Type()
)
tmnxPortFCStatsIngFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdOutProfOcts_Type = Counter64
_TmnxPortFCStatsIngFwdOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngFwdOutProfOcts = _TmnxPortFCStatsIngFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 5),
    _TmnxPortFCStatsIngFwdOutProfOcts_Type()
)
tmnxPortFCStatsIngFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngDroInProfPkts_Type = Counter64
_TmnxPortFCStatsIngDroInProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngDroInProfPkts = _TmnxPortFCStatsIngDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 6),
    _TmnxPortFCStatsIngDroInProfPkts_Type()
)
tmnxPortFCStatsIngDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngDroOutProfPkts_Type = Counter64
_TmnxPortFCStatsIngDroOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngDroOutProfPkts = _TmnxPortFCStatsIngDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 7),
    _TmnxPortFCStatsIngDroOutProfPkts_Type()
)
tmnxPortFCStatsIngDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngDroInProfOcts_Type = Counter64
_TmnxPortFCStatsIngDroInProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngDroInProfOcts = _TmnxPortFCStatsIngDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 8),
    _TmnxPortFCStatsIngDroInProfOcts_Type()
)
tmnxPortFCStatsIngDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngDroOutProfOcts_Type = Counter64
_TmnxPortFCStatsIngDroOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngDroOutProfOcts = _TmnxPortFCStatsIngDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 9),
    _TmnxPortFCStatsIngDroOutProfOcts_Type()
)
tmnxPortFCStatsIngDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdInProfPkts_Type = Counter64
_TmnxPortFCStatsEgrFwdInProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdInProfPkts = _TmnxPortFCStatsEgrFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 10),
    _TmnxPortFCStatsEgrFwdInProfPkts_Type()
)
tmnxPortFCStatsEgrFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdOutProfPkts_Type = Counter64
_TmnxPortFCStatsEgrFwdOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdOutProfPkts = _TmnxPortFCStatsEgrFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 11),
    _TmnxPortFCStatsEgrFwdOutProfPkts_Type()
)
tmnxPortFCStatsEgrFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdInProfOcts_Type = Counter64
_TmnxPortFCStatsEgrFwdInProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdInProfOcts = _TmnxPortFCStatsEgrFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 12),
    _TmnxPortFCStatsEgrFwdInProfOcts_Type()
)
tmnxPortFCStatsEgrFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdOutProfOcts_Type = Counter64
_TmnxPortFCStatsEgrFwdOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdOutProfOcts = _TmnxPortFCStatsEgrFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 13),
    _TmnxPortFCStatsEgrFwdOutProfOcts_Type()
)
tmnxPortFCStatsEgrFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroInProfPkts_Type = Counter64
_TmnxPortFCStatsEgrDroInProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrDroInProfPkts = _TmnxPortFCStatsEgrDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 14),
    _TmnxPortFCStatsEgrDroInProfPkts_Type()
)
tmnxPortFCStatsEgrDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroOutProfPkts_Type = Counter64
_TmnxPortFCStatsEgrDroOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrDroOutProfPkts = _TmnxPortFCStatsEgrDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 15),
    _TmnxPortFCStatsEgrDroOutProfPkts_Type()
)
tmnxPortFCStatsEgrDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroInProfOcts_Type = Counter64
_TmnxPortFCStatsEgrDroInProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrDroInProfOcts = _TmnxPortFCStatsEgrDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 16),
    _TmnxPortFCStatsEgrDroInProfOcts_Type()
)
tmnxPortFCStatsEgrDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroOutProfOcts_Type = Counter64
_TmnxPortFCStatsEgrDroOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrDroOutProfOcts = _TmnxPortFCStatsEgrDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 17),
    _TmnxPortFCStatsEgrDroOutProfOcts_Type()
)
tmnxPortFCStatsEgrDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroOutProfOcts.setStatus("obsolete")
_TmnxDS3Table_Object = MibTable
tmnxDS3Table = _TmnxDS3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tmnxDS3Table.setStatus("current")
_TmnxDS3Entry_Object = MibTableRow
tmnxDS3Entry = _TmnxDS3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1)
)
tmnxDS3Entry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS3Entry.setStatus("current")


class _TmnxDS3Buildout_Type(Integer32):
    """Custom type tmnxDS3Buildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_TmnxDS3Buildout_Type.__name__ = "Integer32"
_TmnxDS3Buildout_Object = MibTableColumn
tmnxDS3Buildout = _TmnxDS3Buildout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 1),
    _TmnxDS3Buildout_Type()
)
tmnxDS3Buildout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3Buildout.setStatus("current")
_TmnxDS3LastChangeTime_Type = TimeStamp
_TmnxDS3LastChangeTime_Object = MibTableColumn
tmnxDS3LastChangeTime = _TmnxDS3LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 2),
    _TmnxDS3LastChangeTime_Type()
)
tmnxDS3LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3LastChangeTime.setStatus("current")


class _TmnxDS3Type_Type(Integer32):
    """Custom type tmnxDS3Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("e3", 2))
    )


_TmnxDS3Type_Type.__name__ = "Integer32"
_TmnxDS3Type_Object = MibTableColumn
tmnxDS3Type = _TmnxDS3Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 3),
    _TmnxDS3Type_Type()
)
tmnxDS3Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3Type.setStatus("current")
_TmnxDS3ChannelTable_Object = MibTable
tmnxDS3ChannelTable = _TmnxDS3ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    tmnxDS3ChannelTable.setStatus("current")
_TmnxDS3ChannelEntry_Object = MibTableRow
tmnxDS3ChannelEntry = _TmnxDS3ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1)
)
tmnxDS3ChannelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS3ChannelEntry.setStatus("current")
_TmnxDS3ChannelRowStatus_Type = RowStatus
_TmnxDS3ChannelRowStatus_Object = MibTableColumn
tmnxDS3ChannelRowStatus = _TmnxDS3ChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 1),
    _TmnxDS3ChannelRowStatus_Type()
)
tmnxDS3ChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelRowStatus.setStatus("current")


class _TmnxDS3ChannelType_Type(Integer32):
    """Custom type tmnxDS3ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("e3", 2))
    )


_TmnxDS3ChannelType_Type.__name__ = "Integer32"
_TmnxDS3ChannelType_Object = MibTableColumn
tmnxDS3ChannelType = _TmnxDS3ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 2),
    _TmnxDS3ChannelType_Type()
)
tmnxDS3ChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelType.setStatus("current")


class _TmnxDS3ChannelFraming_Type(Integer32):
    """Custom type tmnxDS3ChannelFraming based on Integer32"""
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
        *(("cbit", 1),
          ("g751", 3),
          ("g832", 4),
          ("m23", 2))
    )


_TmnxDS3ChannelFraming_Type.__name__ = "Integer32"
_TmnxDS3ChannelFraming_Object = MibTableColumn
tmnxDS3ChannelFraming = _TmnxDS3ChannelFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 3),
    _TmnxDS3ChannelFraming_Type()
)
tmnxDS3ChannelFraming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelFraming.setStatus("current")


class _TmnxDS3ChannelClockSource_Type(TmnxDSXClockSource):
    """Custom type tmnxDS3ChannelClockSource based on TmnxDSXClockSource"""


_TmnxDS3ChannelClockSource_Object = MibTableColumn
tmnxDS3ChannelClockSource = _TmnxDS3ChannelClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 4),
    _TmnxDS3ChannelClockSource_Type()
)
tmnxDS3ChannelClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockSource.setStatus("current")


class _TmnxDS3ChannelChannelized_Type(Integer32):
    """Custom type tmnxDS3ChannelChannelized based on Integer32"""
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
        *(("ds1", 2),
          ("e1", 3),
          ("j1", 4),
          ("none", 1))
    )


_TmnxDS3ChannelChannelized_Type.__name__ = "Integer32"
_TmnxDS3ChannelChannelized_Object = MibTableColumn
tmnxDS3ChannelChannelized = _TmnxDS3ChannelChannelized_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 5),
    _TmnxDS3ChannelChannelized_Type()
)
tmnxDS3ChannelChannelized.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelChannelized.setStatus("current")


class _TmnxDS3ChannelSubrateCSUMode_Type(Integer32):
    """Custom type tmnxDS3ChannelSubrateCSUMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("digital-link", 1),
          ("notUsed", 0))
    )


_TmnxDS3ChannelSubrateCSUMode_Type.__name__ = "Integer32"
_TmnxDS3ChannelSubrateCSUMode_Object = MibTableColumn
tmnxDS3ChannelSubrateCSUMode = _TmnxDS3ChannelSubrateCSUMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 6),
    _TmnxDS3ChannelSubrateCSUMode_Type()
)
tmnxDS3ChannelSubrateCSUMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelSubrateCSUMode.setStatus("current")
_TmnxDS3ChannelSubrate_Type = Unsigned32
_TmnxDS3ChannelSubrate_Object = MibTableColumn
tmnxDS3ChannelSubrate = _TmnxDS3ChannelSubrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 7),
    _TmnxDS3ChannelSubrate_Type()
)
tmnxDS3ChannelSubrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelSubrate.setStatus("current")


class _TmnxDS3ChannelIdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS3ChannelIdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS3ChannelIdleCycleFlags_Object = MibTableColumn
tmnxDS3ChannelIdleCycleFlags = _TmnxDS3ChannelIdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 8),
    _TmnxDS3ChannelIdleCycleFlags_Type()
)
tmnxDS3ChannelIdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelIdleCycleFlags.setStatus("current")


class _TmnxDS3ChannelLoopback_Type(TmnxDS3Loopback):
    """Custom type tmnxDS3ChannelLoopback based on TmnxDS3Loopback"""


_TmnxDS3ChannelLoopback_Object = MibTableColumn
tmnxDS3ChannelLoopback = _TmnxDS3ChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 9),
    _TmnxDS3ChannelLoopback_Type()
)
tmnxDS3ChannelLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelLoopback.setStatus("current")


class _TmnxDS3ChannelBitErrorInsertionRate_Type(Integer32):
    """Custom type tmnxDS3ChannelBitErrorInsertionRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 7),
    )


_TmnxDS3ChannelBitErrorInsertionRate_Type.__name__ = "Integer32"
_TmnxDS3ChannelBitErrorInsertionRate_Object = MibTableColumn
tmnxDS3ChannelBitErrorInsertionRate = _TmnxDS3ChannelBitErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 10),
    _TmnxDS3ChannelBitErrorInsertionRate_Type()
)
tmnxDS3ChannelBitErrorInsertionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBitErrorInsertionRate.setStatus("current")


class _TmnxDS3ChannelBERTPattern_Type(TmnxDSXBertPattern):
    """Custom type tmnxDS3ChannelBERTPattern based on TmnxDSXBertPattern"""


_TmnxDS3ChannelBERTPattern_Object = MibTableColumn
tmnxDS3ChannelBERTPattern = _TmnxDS3ChannelBERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 11),
    _TmnxDS3ChannelBERTPattern_Type()
)
tmnxDS3ChannelBERTPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTPattern.setStatus("current")


class _TmnxDS3ChannelBERTDuration_Type(Unsigned32):
    """Custom type tmnxDS3ChannelBERTDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxDS3ChannelBERTDuration_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelBERTDuration_Object = MibTableColumn
tmnxDS3ChannelBERTDuration = _TmnxDS3ChannelBERTDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 12),
    _TmnxDS3ChannelBERTDuration_Type()
)
tmnxDS3ChannelBERTDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTDuration.setUnits("seconds")


class _TmnxDS3ChannelMDLEicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLEicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TmnxDS3ChannelMDLEicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLEicString_Object = MibTableColumn
tmnxDS3ChannelMDLEicString = _TmnxDS3ChannelMDLEicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 13),
    _TmnxDS3ChannelMDLEicString_Type()
)
tmnxDS3ChannelMDLEicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLEicString.setStatus("current")


class _TmnxDS3ChannelMDLLicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLLicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_TmnxDS3ChannelMDLLicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLLicString_Object = MibTableColumn
tmnxDS3ChannelMDLLicString = _TmnxDS3ChannelMDLLicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 14),
    _TmnxDS3ChannelMDLLicString_Type()
)
tmnxDS3ChannelMDLLicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLLicString.setStatus("current")


class _TmnxDS3ChannelMDLFicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLFicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TmnxDS3ChannelMDLFicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLFicString_Object = MibTableColumn
tmnxDS3ChannelMDLFicString = _TmnxDS3ChannelMDLFicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 15),
    _TmnxDS3ChannelMDLFicString_Type()
)
tmnxDS3ChannelMDLFicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLFicString.setStatus("current")


class _TmnxDS3ChannelMDLUnitString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLUnitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TmnxDS3ChannelMDLUnitString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLUnitString_Object = MibTableColumn
tmnxDS3ChannelMDLUnitString = _TmnxDS3ChannelMDLUnitString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 16),
    _TmnxDS3ChannelMDLUnitString_Type()
)
tmnxDS3ChannelMDLUnitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLUnitString.setStatus("current")


class _TmnxDS3ChannelMDLPfiString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLPfiString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLPfiString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLPfiString_Object = MibTableColumn
tmnxDS3ChannelMDLPfiString = _TmnxDS3ChannelMDLPfiString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 17),
    _TmnxDS3ChannelMDLPfiString_Type()
)
tmnxDS3ChannelMDLPfiString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLPfiString.setStatus("current")


class _TmnxDS3ChannelMDLPortString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLPortString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLPortString_Object = MibTableColumn
tmnxDS3ChannelMDLPortString = _TmnxDS3ChannelMDLPortString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 18),
    _TmnxDS3ChannelMDLPortString_Type()
)
tmnxDS3ChannelMDLPortString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLPortString.setStatus("current")


class _TmnxDS3ChannelMDLGenString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLGenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLGenString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLGenString_Object = MibTableColumn
tmnxDS3ChannelMDLGenString = _TmnxDS3ChannelMDLGenString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 19),
    _TmnxDS3ChannelMDLGenString_Type()
)
tmnxDS3ChannelMDLGenString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLGenString.setStatus("current")


class _TmnxDS3ChannelMDLMessageType_Type(Bits):
    """Custom type tmnxDS3ChannelMDLMessageType based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("ds3Path", 1),
          ("idleSignal", 2),
          ("none", 0),
          ("testSignal", 3))
    )

_TmnxDS3ChannelMDLMessageType_Type.__name__ = "Bits"
_TmnxDS3ChannelMDLMessageType_Object = MibTableColumn
tmnxDS3ChannelMDLMessageType = _TmnxDS3ChannelMDLMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 20),
    _TmnxDS3ChannelMDLMessageType_Type()
)
tmnxDS3ChannelMDLMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMessageType.setStatus("current")


class _TmnxDS3ChannelFEACLoopRespond_Type(TruthValue):
    """Custom type tmnxDS3ChannelFEACLoopRespond based on TruthValue"""


_TmnxDS3ChannelFEACLoopRespond_Object = MibTableColumn
tmnxDS3ChannelFEACLoopRespond = _TmnxDS3ChannelFEACLoopRespond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 21),
    _TmnxDS3ChannelFEACLoopRespond_Type()
)
tmnxDS3ChannelFEACLoopRespond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelFEACLoopRespond.setStatus("current")


class _TmnxDS3ChannelCRC_Type(Integer32):
    """Custom type tmnxDS3ChannelCRC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxDS3ChannelCRC_Type.__name__ = "Integer32"
_TmnxDS3ChannelCRC_Object = MibTableColumn
tmnxDS3ChannelCRC = _TmnxDS3ChannelCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 22),
    _TmnxDS3ChannelCRC_Type()
)
tmnxDS3ChannelCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelCRC.setStatus("current")


class _TmnxDS3ChannelMTU_Type(Unsigned32):
    """Custom type tmnxDS3ChannelMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxDS3ChannelMTU_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelMTU_Object = MibTableColumn
tmnxDS3ChannelMTU = _TmnxDS3ChannelMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 23),
    _TmnxDS3ChannelMTU_Type()
)
tmnxDS3ChannelMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMTU.setUnits("bytes")
_TmnxDS3ChannelOperMTU_Type = Unsigned32
_TmnxDS3ChannelOperMTU_Object = MibTableColumn
tmnxDS3ChannelOperMTU = _TmnxDS3ChannelOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 24),
    _TmnxDS3ChannelOperMTU_Type()
)
tmnxDS3ChannelOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelOperMTU.setUnits("bytes")


class _TmnxDS3ChannelReportAlarm_Type(TmnxDSXReportAlarm):
    """Custom type tmnxDS3ChannelReportAlarm based on TmnxDSXReportAlarm"""
    defaultBinValue = "011"


_TmnxDS3ChannelReportAlarm_Object = MibTableColumn
tmnxDS3ChannelReportAlarm = _TmnxDS3ChannelReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 25),
    _TmnxDS3ChannelReportAlarm_Type()
)
tmnxDS3ChannelReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelReportAlarm.setStatus("current")
_TmnxDS3ChannelReportAlarmStatus_Type = TmnxDSXReportAlarm
_TmnxDS3ChannelReportAlarmStatus_Object = MibTableColumn
tmnxDS3ChannelReportAlarmStatus = _TmnxDS3ChannelReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 26),
    _TmnxDS3ChannelReportAlarmStatus_Type()
)
tmnxDS3ChannelReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelReportAlarmStatus.setStatus("current")
_TmnxDS3ChannelLastChangeTime_Type = TimeStamp
_TmnxDS3ChannelLastChangeTime_Object = MibTableColumn
tmnxDS3ChannelLastChangeTime = _TmnxDS3ChannelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 27),
    _TmnxDS3ChannelLastChangeTime_Type()
)
tmnxDS3ChannelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelLastChangeTime.setStatus("current")
_TmnxDS3ChannelInFEACLoop_Type = TruthValue
_TmnxDS3ChannelInFEACLoop_Object = MibTableColumn
tmnxDS3ChannelInFEACLoop = _TmnxDS3ChannelInFEACLoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 28),
    _TmnxDS3ChannelInFEACLoop_Type()
)
tmnxDS3ChannelInFEACLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelInFEACLoop.setStatus("current")


class _TmnxDS3ChannelMDLMonPortString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLMonPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLMonPortString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLMonPortString_Object = MibTableColumn
tmnxDS3ChannelMDLMonPortString = _TmnxDS3ChannelMDLMonPortString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 29),
    _TmnxDS3ChannelMDLMonPortString_Type()
)
tmnxDS3ChannelMDLMonPortString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMonPortString.setStatus("current")


class _TmnxDS3ChannelMDLMonGenString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLMonGenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLMonGenString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLMonGenString_Object = MibTableColumn
tmnxDS3ChannelMDLMonGenString = _TmnxDS3ChannelMDLMonGenString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 30),
    _TmnxDS3ChannelMDLMonGenString_Type()
)
tmnxDS3ChannelMDLMonGenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMonGenString.setStatus("current")
_TmnxDS3ChannelBERTOperStatus_Type = TmnxDSXBertOperStatus
_TmnxDS3ChannelBERTOperStatus_Object = MibTableColumn
tmnxDS3ChannelBERTOperStatus = _TmnxDS3ChannelBERTOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 31),
    _TmnxDS3ChannelBERTOperStatus_Type()
)
tmnxDS3ChannelBERTOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTOperStatus.setStatus("current")
_TmnxDS3ChannelBERTSynched_Type = Unsigned32
_TmnxDS3ChannelBERTSynched_Object = MibTableColumn
tmnxDS3ChannelBERTSynched = _TmnxDS3ChannelBERTSynched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 32),
    _TmnxDS3ChannelBERTSynched_Type()
)
tmnxDS3ChannelBERTSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTSynched.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTSynched.setUnits("seconds")
_TmnxDS3ChannelBERTErrors_Type = Counter64
_TmnxDS3ChannelBERTErrors_Object = MibTableColumn
tmnxDS3ChannelBERTErrors = _TmnxDS3ChannelBERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 33),
    _TmnxDS3ChannelBERTErrors_Type()
)
tmnxDS3ChannelBERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTErrors.setStatus("current")
_TmnxDS3ChannelBERTTotalBits_Type = Counter64
_TmnxDS3ChannelBERTTotalBits_Object = MibTableColumn
tmnxDS3ChannelBERTTotalBits = _TmnxDS3ChannelBERTTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 34),
    _TmnxDS3ChannelBERTTotalBits_Type()
)
tmnxDS3ChannelBERTTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTTotalBits.setStatus("current")
_TmnxDS3ChannelScramble_Type = TruthValue
_TmnxDS3ChannelScramble_Object = MibTableColumn
tmnxDS3ChannelScramble = _TmnxDS3ChannelScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 35),
    _TmnxDS3ChannelScramble_Type()
)
tmnxDS3ChannelScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelScramble.setStatus("current")


class _TmnxDS3ChannelAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxDS3ChannelAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxDS3ChannelAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelAcctPolicyId_Object = MibTableColumn
tmnxDS3ChannelAcctPolicyId = _TmnxDS3ChannelAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 36),
    _TmnxDS3ChannelAcctPolicyId_Type()
)
tmnxDS3ChannelAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelAcctPolicyId.setStatus("current")


class _TmnxDS3ChannelCollectStats_Type(TruthValue):
    """Custom type tmnxDS3ChannelCollectStats based on TruthValue"""


_TmnxDS3ChannelCollectStats_Object = MibTableColumn
tmnxDS3ChannelCollectStats = _TmnxDS3ChannelCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 37),
    _TmnxDS3ChannelCollectStats_Type()
)
tmnxDS3ChannelCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelCollectStats.setStatus("current")
_TmnxDS3ChannelClockSyncState_Type = TmnxDSXClockSyncState
_TmnxDS3ChannelClockSyncState_Object = MibTableColumn
tmnxDS3ChannelClockSyncState = _TmnxDS3ChannelClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 38),
    _TmnxDS3ChannelClockSyncState_Type()
)
tmnxDS3ChannelClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockSyncState.setStatus("current")
_TmnxDS3ChannelClockMasterPortId_Type = TmnxPortID
_TmnxDS3ChannelClockMasterPortId_Object = MibTableColumn
tmnxDS3ChannelClockMasterPortId = _TmnxDS3ChannelClockMasterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 39),
    _TmnxDS3ChannelClockMasterPortId_Type()
)
tmnxDS3ChannelClockMasterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockMasterPortId.setStatus("current")
_TmnxDS1Table_Object = MibTable
tmnxDS1Table = _TmnxDS1Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12)
)
if mibBuilder.loadTexts:
    tmnxDS1Table.setStatus("current")
_TmnxDS1Entry_Object = MibTableRow
tmnxDS1Entry = _TmnxDS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1)
)
tmnxDS1Entry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS1Entry.setStatus("current")
_TmnxDS1RowStatus_Type = RowStatus
_TmnxDS1RowStatus_Object = MibTableColumn
tmnxDS1RowStatus = _TmnxDS1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 1),
    _TmnxDS1RowStatus_Type()
)
tmnxDS1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1RowStatus.setStatus("current")


class _TmnxDS1Type_Type(Integer32):
    """Custom type tmnxDS1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("e1", 2),
          ("j1", 3))
    )


_TmnxDS1Type_Type.__name__ = "Integer32"
_TmnxDS1Type_Object = MibTableColumn
tmnxDS1Type = _TmnxDS1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 2),
    _TmnxDS1Type_Type()
)
tmnxDS1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1Type.setStatus("current")


class _TmnxDS1Framing_Type(Integer32):
    """Custom type tmnxDS1Framing based on Integer32"""
    defaultValue = 1

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
        *(("ds1-unframed", 6),
          ("e1-unframed", 5),
          ("esf", 1),
          ("g704", 4),
          ("g704-no-crc", 3),
          ("sf", 2))
    )


_TmnxDS1Framing_Type.__name__ = "Integer32"
_TmnxDS1Framing_Object = MibTableColumn
tmnxDS1Framing = _TmnxDS1Framing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 3),
    _TmnxDS1Framing_Type()
)
tmnxDS1Framing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1Framing.setStatus("current")


class _TmnxDS1IdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS1IdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS1IdleCycleFlags_Object = MibTableColumn
tmnxDS1IdleCycleFlags = _TmnxDS1IdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 4),
    _TmnxDS1IdleCycleFlags_Type()
)
tmnxDS1IdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1IdleCycleFlags.setStatus("obsolete")


class _TmnxDS1Loopback_Type(TmnxDS1Loopback):
    """Custom type tmnxDS1Loopback based on TmnxDS1Loopback"""


_TmnxDS1Loopback_Object = MibTableColumn
tmnxDS1Loopback = _TmnxDS1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 5),
    _TmnxDS1Loopback_Type()
)
tmnxDS1Loopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1Loopback.setStatus("current")


class _TmnxDS1InvertData_Type(TruthValue):
    """Custom type tmnxDS1InvertData based on TruthValue"""


_TmnxDS1InvertData_Object = MibTableColumn
tmnxDS1InvertData = _TmnxDS1InvertData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 6),
    _TmnxDS1InvertData_Type()
)
tmnxDS1InvertData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1InvertData.setStatus("current")


class _TmnxDS1BitErrorInsertionRate_Type(Integer32):
    """Custom type tmnxDS1BitErrorInsertionRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 7),
    )


_TmnxDS1BitErrorInsertionRate_Type.__name__ = "Integer32"
_TmnxDS1BitErrorInsertionRate_Object = MibTableColumn
tmnxDS1BitErrorInsertionRate = _TmnxDS1BitErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 7),
    _TmnxDS1BitErrorInsertionRate_Type()
)
tmnxDS1BitErrorInsertionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BitErrorInsertionRate.setStatus("current")


class _TmnxDS1BERTPattern_Type(TmnxDSXBertPattern):
    """Custom type tmnxDS1BERTPattern based on TmnxDSXBertPattern"""


_TmnxDS1BERTPattern_Object = MibTableColumn
tmnxDS1BERTPattern = _TmnxDS1BERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 8),
    _TmnxDS1BERTPattern_Type()
)
tmnxDS1BERTPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BERTPattern.setStatus("current")


class _TmnxDS1BERTDuration_Type(Unsigned32):
    """Custom type tmnxDS1BERTDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxDS1BERTDuration_Type.__name__ = "Unsigned32"
_TmnxDS1BERTDuration_Object = MibTableColumn
tmnxDS1BERTDuration = _TmnxDS1BERTDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 9),
    _TmnxDS1BERTDuration_Type()
)
tmnxDS1BERTDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BERTDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BERTDuration.setUnits("seconds")


class _TmnxDS1ReportAlarm_Type(TmnxDSXReportAlarm):
    """Custom type tmnxDS1ReportAlarm based on TmnxDSXReportAlarm"""
    defaultBinValue = "011"


_TmnxDS1ReportAlarm_Object = MibTableColumn
tmnxDS1ReportAlarm = _TmnxDS1ReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 10),
    _TmnxDS1ReportAlarm_Type()
)
tmnxDS1ReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1ReportAlarm.setStatus("current")
_TmnxDS1ReportAlarmStatus_Type = TmnxDSXReportAlarm
_TmnxDS1ReportAlarmStatus_Object = MibTableColumn
tmnxDS1ReportAlarmStatus = _TmnxDS1ReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 11),
    _TmnxDS1ReportAlarmStatus_Type()
)
tmnxDS1ReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ReportAlarmStatus.setStatus("current")
_TmnxDS1LastChangeTime_Type = TimeStamp
_TmnxDS1LastChangeTime_Object = MibTableColumn
tmnxDS1LastChangeTime = _TmnxDS1LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 12),
    _TmnxDS1LastChangeTime_Type()
)
tmnxDS1LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1LastChangeTime.setStatus("current")


class _TmnxDS1ClockSource_Type(TmnxDSXClockSource):
    """Custom type tmnxDS1ClockSource based on TmnxDSXClockSource"""


_TmnxDS1ClockSource_Object = MibTableColumn
tmnxDS1ClockSource = _TmnxDS1ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 13),
    _TmnxDS1ClockSource_Type()
)
tmnxDS1ClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1ClockSource.setStatus("current")
_TmnxDS1BERTOperStatus_Type = TmnxDSXBertOperStatus
_TmnxDS1BERTOperStatus_Object = MibTableColumn
tmnxDS1BERTOperStatus = _TmnxDS1BERTOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 14),
    _TmnxDS1BERTOperStatus_Type()
)
tmnxDS1BERTOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTOperStatus.setStatus("current")
_TmnxDS1BERTSynched_Type = Unsigned32
_TmnxDS1BERTSynched_Object = MibTableColumn
tmnxDS1BERTSynched = _TmnxDS1BERTSynched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 15),
    _TmnxDS1BERTSynched_Type()
)
tmnxDS1BERTSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTSynched.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BERTSynched.setUnits("seconds")
_TmnxDS1BERTErrors_Type = Counter64
_TmnxDS1BERTErrors_Object = MibTableColumn
tmnxDS1BERTErrors = _TmnxDS1BERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 16),
    _TmnxDS1BERTErrors_Type()
)
tmnxDS1BERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTErrors.setStatus("current")
_TmnxDS1BERTTotalBits_Type = Counter64
_TmnxDS1BERTTotalBits_Object = MibTableColumn
tmnxDS1BERTTotalBits = _TmnxDS1BERTTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 17),
    _TmnxDS1BERTTotalBits_Type()
)
tmnxDS1BERTTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTTotalBits.setStatus("current")


class _TmnxDS1RemoteLoopRespond_Type(TruthValue):
    """Custom type tmnxDS1RemoteLoopRespond based on TruthValue"""


_TmnxDS1RemoteLoopRespond_Object = MibTableColumn
tmnxDS1RemoteLoopRespond = _TmnxDS1RemoteLoopRespond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 18),
    _TmnxDS1RemoteLoopRespond_Type()
)
tmnxDS1RemoteLoopRespond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1RemoteLoopRespond.setStatus("current")
_TmnxDS1InRemoteLoop_Type = TruthValue
_TmnxDS1InRemoteLoop_Object = MibTableColumn
tmnxDS1InRemoteLoop = _TmnxDS1InRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 19),
    _TmnxDS1InRemoteLoop_Type()
)
tmnxDS1InRemoteLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1InRemoteLoop.setStatus("current")
_TmnxDS1InsertSingleBitError_Type = TmnxActionType
_TmnxDS1InsertSingleBitError_Object = MibTableColumn
tmnxDS1InsertSingleBitError = _TmnxDS1InsertSingleBitError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 20),
    _TmnxDS1InsertSingleBitError_Type()
)
tmnxDS1InsertSingleBitError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1InsertSingleBitError.setStatus("current")


class _TmnxDS1SignalMode_Type(Integer32):
    """Custom type tmnxDS1SignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("none", 1))
    )


_TmnxDS1SignalMode_Type.__name__ = "Integer32"
_TmnxDS1SignalMode_Object = MibTableColumn
tmnxDS1SignalMode = _TmnxDS1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 21),
    _TmnxDS1SignalMode_Type()
)
tmnxDS1SignalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1SignalMode.setStatus("current")
_TmnxDS1ClockSyncState_Type = TmnxDSXClockSyncState
_TmnxDS1ClockSyncState_Object = MibTableColumn
tmnxDS1ClockSyncState = _TmnxDS1ClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 22),
    _TmnxDS1ClockSyncState_Type()
)
tmnxDS1ClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ClockSyncState.setStatus("current")
_TmnxDS1ClockMasterPortId_Type = TmnxPortID
_TmnxDS1ClockMasterPortId_Object = MibTableColumn
tmnxDS1ClockMasterPortId = _TmnxDS1ClockMasterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 23),
    _TmnxDS1ClockMasterPortId_Type()
)
tmnxDS1ClockMasterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ClockMasterPortId.setStatus("current")


class _TmnxDS1BerSdThreshold_Type(Unsigned32):
    """Custom type tmnxDS1BerSdThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(100, 100),
    )


_TmnxDS1BerSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDS1BerSdThreshold_Object = MibTableColumn
tmnxDS1BerSdThreshold = _TmnxDS1BerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 24),
    _TmnxDS1BerSdThreshold_Type()
)
tmnxDS1BerSdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BerSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BerSdThreshold.setUnits("error bits in million bits received")


class _TmnxDS1BerSfThreshold_Type(Unsigned32):
    """Custom type tmnxDS1BerSfThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(100, 100),
    )


_TmnxDS1BerSfThreshold_Type.__name__ = "Unsigned32"
_TmnxDS1BerSfThreshold_Object = MibTableColumn
tmnxDS1BerSfThreshold = _TmnxDS1BerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 25),
    _TmnxDS1BerSfThreshold_Type()
)
tmnxDS1BerSfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BerSfThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BerSfThreshold.setUnits("error bits in million bits received")
_TmnxDS0ChanGroupTable_Object = MibTable
tmnxDS0ChanGroupTable = _TmnxDS0ChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13)
)
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupTable.setStatus("current")
_TmnxDS0ChanGroupEntry_Object = MibTableRow
tmnxDS0ChanGroupEntry = _TmnxDS0ChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1)
)
tmnxDS0ChanGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupEntry.setStatus("current")
_TmnxDS0ChanGroupRowStatus_Type = RowStatus
_TmnxDS0ChanGroupRowStatus_Object = MibTableColumn
tmnxDS0ChanGroupRowStatus = _TmnxDS0ChanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 1),
    _TmnxDS0ChanGroupRowStatus_Type()
)
tmnxDS0ChanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupRowStatus.setStatus("current")
_TmnxDS0ChanGroupTimeSlots_Type = TmnxDs0ChannelList
_TmnxDS0ChanGroupTimeSlots_Object = MibTableColumn
tmnxDS0ChanGroupTimeSlots = _TmnxDS0ChanGroupTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 2),
    _TmnxDS0ChanGroupTimeSlots_Type()
)
tmnxDS0ChanGroupTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupTimeSlots.setStatus("current")


class _TmnxDS0ChanGroupSpeed_Type(Integer32):
    """Custom type tmnxDS0ChanGroupSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-56", 1),
          ("speed-64", 2))
    )


_TmnxDS0ChanGroupSpeed_Type.__name__ = "Integer32"
_TmnxDS0ChanGroupSpeed_Object = MibTableColumn
tmnxDS0ChanGroupSpeed = _TmnxDS0ChanGroupSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 3),
    _TmnxDS0ChanGroupSpeed_Type()
)
tmnxDS0ChanGroupSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSpeed.setStatus("current")


class _TmnxDS0ChanGroupCRC_Type(Integer32):
    """Custom type tmnxDS0ChanGroupCRC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxDS0ChanGroupCRC_Type.__name__ = "Integer32"
_TmnxDS0ChanGroupCRC_Object = MibTableColumn
tmnxDS0ChanGroupCRC = _TmnxDS0ChanGroupCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 4),
    _TmnxDS0ChanGroupCRC_Type()
)
tmnxDS0ChanGroupCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupCRC.setStatus("current")


class _TmnxDS0ChanGroupMTU_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxDS0ChanGroupMTU_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupMTU_Object = MibTableColumn
tmnxDS0ChanGroupMTU = _TmnxDS0ChanGroupMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 5),
    _TmnxDS0ChanGroupMTU_Type()
)
tmnxDS0ChanGroupMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupMTU.setUnits("bytes")
_TmnxDS0ChanGroupOperMTU_Type = Unsigned32
_TmnxDS0ChanGroupOperMTU_Object = MibTableColumn
tmnxDS0ChanGroupOperMTU = _TmnxDS0ChanGroupOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 6),
    _TmnxDS0ChanGroupOperMTU_Type()
)
tmnxDS0ChanGroupOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupOperMTU.setUnits("bytes")
_TmnxDS0ChanGroupLastChangeTime_Type = TimeStamp
_TmnxDS0ChanGroupLastChangeTime_Object = MibTableColumn
tmnxDS0ChanGroupLastChangeTime = _TmnxDS0ChanGroupLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 7),
    _TmnxDS0ChanGroupLastChangeTime_Type()
)
tmnxDS0ChanGroupLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupLastChangeTime.setStatus("current")


class _TmnxDS0ChanGroupIdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS0ChanGroupIdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS0ChanGroupIdleCycleFlags_Object = MibTableColumn
tmnxDS0ChanGroupIdleCycleFlags = _TmnxDS0ChanGroupIdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 8),
    _TmnxDS0ChanGroupIdleCycleFlags_Type()
)
tmnxDS0ChanGroupIdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupIdleCycleFlags.setStatus("current")
_TmnxDS0ChanGroupScramble_Type = TruthValue
_TmnxDS0ChanGroupScramble_Object = MibTableColumn
tmnxDS0ChanGroupScramble = _TmnxDS0ChanGroupScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 9),
    _TmnxDS0ChanGroupScramble_Type()
)
tmnxDS0ChanGroupScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupScramble.setStatus("current")


class _TmnxDS0ChanGroupAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxDS0ChanGroupAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupAcctPolicyId_Object = MibTableColumn
tmnxDS0ChanGroupAcctPolicyId = _TmnxDS0ChanGroupAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 10),
    _TmnxDS0ChanGroupAcctPolicyId_Type()
)
tmnxDS0ChanGroupAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupAcctPolicyId.setStatus("current")


class _TmnxDS0ChanGroupCollectStats_Type(TruthValue):
    """Custom type tmnxDS0ChanGroupCollectStats based on TruthValue"""


_TmnxDS0ChanGroupCollectStats_Object = MibTableColumn
tmnxDS0ChanGroupCollectStats = _TmnxDS0ChanGroupCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 11),
    _TmnxDS0ChanGroupCollectStats_Type()
)
tmnxDS0ChanGroupCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupCollectStats.setStatus("current")


class _TmnxDS0ChanGroupPayloadFillType_Type(TmnxDSXIdleFillType):
    """Custom type tmnxDS0ChanGroupPayloadFillType based on TmnxDSXIdleFillType"""


_TmnxDS0ChanGroupPayloadFillType_Object = MibTableColumn
tmnxDS0ChanGroupPayloadFillType = _TmnxDS0ChanGroupPayloadFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 12),
    _TmnxDS0ChanGroupPayloadFillType_Type()
)
tmnxDS0ChanGroupPayloadFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupPayloadFillType.setStatus("current")


class _TmnxDS0ChanGroupPayloadPattern_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupPayloadPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDS0ChanGroupPayloadPattern_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupPayloadPattern_Object = MibTableColumn
tmnxDS0ChanGroupPayloadPattern = _TmnxDS0ChanGroupPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 13),
    _TmnxDS0ChanGroupPayloadPattern_Type()
)
tmnxDS0ChanGroupPayloadPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupPayloadPattern.setStatus("current")


class _TmnxDS0ChanGroupSignalFillType_Type(TmnxDSXIdleFillType):
    """Custom type tmnxDS0ChanGroupSignalFillType based on TmnxDSXIdleFillType"""


_TmnxDS0ChanGroupSignalFillType_Object = MibTableColumn
tmnxDS0ChanGroupSignalFillType = _TmnxDS0ChanGroupSignalFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 14),
    _TmnxDS0ChanGroupSignalFillType_Type()
)
tmnxDS0ChanGroupSignalFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSignalFillType.setStatus("current")


class _TmnxDS0ChanGroupSignalPattern_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupSignalPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxDS0ChanGroupSignalPattern_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupSignalPattern_Object = MibTableColumn
tmnxDS0ChanGroupSignalPattern = _TmnxDS0ChanGroupSignalPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 15),
    _TmnxDS0ChanGroupSignalPattern_Type()
)
tmnxDS0ChanGroupSignalPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSignalPattern.setStatus("current")
_TmnxBundleTable_Object = MibTable
tmnxBundleTable = _TmnxBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14)
)
if mibBuilder.loadTexts:
    tmnxBundleTable.setStatus("current")
_TmnxBundleEntry_Object = MibTableRow
tmnxBundleEntry = _TmnxBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1)
)
tmnxBundleEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleEntry.setStatus("current")
_TmnxBundleBundleID_Type = TmnxBundleID
_TmnxBundleBundleID_Object = MibTableColumn
tmnxBundleBundleID = _TmnxBundleBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 1),
    _TmnxBundleBundleID_Type()
)
tmnxBundleBundleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBundleBundleID.setStatus("current")
_TmnxBundleRowStatus_Type = RowStatus
_TmnxBundleRowStatus_Object = MibTableColumn
tmnxBundleRowStatus = _TmnxBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 2),
    _TmnxBundleRowStatus_Type()
)
tmnxBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRowStatus.setStatus("current")


class _TmnxBundleType_Type(Integer32):
    """Custom type tmnxBundleType based on Integer32"""
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
        *(("imagrp", 3),
          ("mlfr", 2),
          ("mlppp", 1))
    )


_TmnxBundleType_Type.__name__ = "Integer32"
_TmnxBundleType_Object = MibTableColumn
tmnxBundleType = _TmnxBundleType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 3),
    _TmnxBundleType_Type()
)
tmnxBundleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleType.setStatus("current")


class _TmnxBundleMinimumLinks_Type(Unsigned32):
    """Custom type tmnxBundleMinimumLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxBundleMinimumLinks_Type.__name__ = "Unsigned32"
_TmnxBundleMinimumLinks_Object = MibTableColumn
tmnxBundleMinimumLinks = _TmnxBundleMinimumLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 4),
    _TmnxBundleMinimumLinks_Type()
)
tmnxBundleMinimumLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMinimumLinks.setStatus("current")
_TmnxBundleNumLinks_Type = Unsigned32
_TmnxBundleNumLinks_Object = MibTableColumn
tmnxBundleNumLinks = _TmnxBundleNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 5),
    _TmnxBundleNumLinks_Type()
)
tmnxBundleNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleNumLinks.setStatus("current")
_TmnxBundleNumActiveLinks_Type = Unsigned32
_TmnxBundleNumActiveLinks_Object = MibTableColumn
tmnxBundleNumActiveLinks = _TmnxBundleNumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 6),
    _TmnxBundleNumActiveLinks_Type()
)
tmnxBundleNumActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleNumActiveLinks.setStatus("current")


class _TmnxBundleMRRU_Type(Unsigned32):
    """Custom type tmnxBundleMRRU based on Unsigned32"""
    defaultValue = 1524

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1500, 9206),
    )


_TmnxBundleMRRU_Type.__name__ = "Unsigned32"
_TmnxBundleMRRU_Object = MibTableColumn
tmnxBundleMRRU = _TmnxBundleMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 7),
    _TmnxBundleMRRU_Type()
)
tmnxBundleMRRU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMRRU.setUnits("bytes")
_TmnxBundleOperMRRU_Type = Unsigned32
_TmnxBundleOperMRRU_Object = MibTableColumn
tmnxBundleOperMRRU = _TmnxBundleOperMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 8),
    _TmnxBundleOperMRRU_Type()
)
tmnxBundleOperMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleOperMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleOperMRRU.setUnits("bytes")
_TmnxBundlePeerMRRU_Type = Unsigned32
_TmnxBundlePeerMRRU_Object = MibTableColumn
tmnxBundlePeerMRRU = _TmnxBundlePeerMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 9),
    _TmnxBundlePeerMRRU_Type()
)
tmnxBundlePeerMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundlePeerMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundlePeerMRRU.setUnits("bytes")
_TmnxBundleOperMTU_Type = Unsigned32
_TmnxBundleOperMTU_Object = MibTableColumn
tmnxBundleOperMTU = _TmnxBundleOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 10),
    _TmnxBundleOperMTU_Type()
)
tmnxBundleOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleOperMTU.setUnits("bytes")


class _TmnxBundleRedDiffDelay_Type(Unsigned32):
    """Custom type tmnxBundleRedDiffDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
        ValueRangeConstraint(0, 50),
    )


_TmnxBundleRedDiffDelay_Type.__name__ = "Unsigned32"
_TmnxBundleRedDiffDelay_Object = MibTableColumn
tmnxBundleRedDiffDelay = _TmnxBundleRedDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 11),
    _TmnxBundleRedDiffDelay_Type()
)
tmnxBundleRedDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelay.setUnits("milliseconds")


class _TmnxBundleRedDiffDelayAction_Type(Integer32):
    """Custom type tmnxBundleRedDiffDelayAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("none", 0))
    )


_TmnxBundleRedDiffDelayAction_Type.__name__ = "Integer32"
_TmnxBundleRedDiffDelayAction_Object = MibTableColumn
tmnxBundleRedDiffDelayAction = _TmnxBundleRedDiffDelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 12),
    _TmnxBundleRedDiffDelayAction_Type()
)
tmnxBundleRedDiffDelayAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelayAction.setStatus("current")


class _TmnxBundleYellowDiffDelay_Type(Unsigned32):
    """Custom type tmnxBundleYellowDiffDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_TmnxBundleYellowDiffDelay_Type.__name__ = "Unsigned32"
_TmnxBundleYellowDiffDelay_Object = MibTableColumn
tmnxBundleYellowDiffDelay = _TmnxBundleYellowDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 13),
    _TmnxBundleYellowDiffDelay_Type()
)
tmnxBundleYellowDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleYellowDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleYellowDiffDelay.setUnits("milliseconds")


class _TmnxBundleShortSequence_Type(TruthValue):
    """Custom type tmnxBundleShortSequence based on TruthValue"""


_TmnxBundleShortSequence_Object = MibTableColumn
tmnxBundleShortSequence = _TmnxBundleShortSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 14),
    _TmnxBundleShortSequence_Type()
)
tmnxBundleShortSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleShortSequence.setStatus("current")
_TmnxBundleLastChangeTime_Type = TimeStamp
_TmnxBundleLastChangeTime_Object = MibTableColumn
tmnxBundleLastChangeTime = _TmnxBundleLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 15),
    _TmnxBundleLastChangeTime_Type()
)
tmnxBundleLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleLastChangeTime.setStatus("current")


class _TmnxBundleFragmentThreshold_Type(Unsigned32):
    """Custom type tmnxBundleFragmentThreshold based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 512),
    )


_TmnxBundleFragmentThreshold_Type.__name__ = "Unsigned32"
_TmnxBundleFragmentThreshold_Object = MibTableColumn
tmnxBundleFragmentThreshold = _TmnxBundleFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 16),
    _TmnxBundleFragmentThreshold_Type()
)
tmnxBundleFragmentThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleFragmentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleFragmentThreshold.setUnits("bytes")
_TmnxBundleUpTime_Type = Unsigned32
_TmnxBundleUpTime_Object = MibTableColumn
tmnxBundleUpTime = _TmnxBundleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 17),
    _TmnxBundleUpTime_Type()
)
tmnxBundleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleUpTime.setUnits("seconds")
_TmnxBundleInputDiscards_Type = Counter32
_TmnxBundleInputDiscards_Object = MibTableColumn
tmnxBundleInputDiscards = _TmnxBundleInputDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 18),
    _TmnxBundleInputDiscards_Type()
)
tmnxBundleInputDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleInputDiscards.setStatus("current")
_TmnxBundlePrimaryMemberPortID_Type = TmnxPortID
_TmnxBundlePrimaryMemberPortID_Object = MibTableColumn
tmnxBundlePrimaryMemberPortID = _TmnxBundlePrimaryMemberPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 19),
    _TmnxBundlePrimaryMemberPortID_Type()
)
tmnxBundlePrimaryMemberPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundlePrimaryMemberPortID.setStatus("current")


class _TmnxBundleLFI_Type(TruthValue):
    """Custom type tmnxBundleLFI based on TruthValue"""


_TmnxBundleLFI_Object = MibTableColumn
tmnxBundleLFI = _TmnxBundleLFI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 20),
    _TmnxBundleLFI_Type()
)
tmnxBundleLFI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleLFI.setStatus("current")


class _TmnxBundleProtectedType_Type(Integer32):
    """Custom type tmnxBundleProtectedType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("protection", 2),
          ("working", 1))
    )


_TmnxBundleProtectedType_Type.__name__ = "Integer32"
_TmnxBundleProtectedType_Object = MibTableColumn
tmnxBundleProtectedType = _TmnxBundleProtectedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 21),
    _TmnxBundleProtectedType_Type()
)
tmnxBundleProtectedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleProtectedType.setStatus("current")


class _TmnxBundleParentBundle_Type(TmnxBundleID):
    """Custom type tmnxBundleParentBundle based on TmnxBundleID"""
    defaultValue = 0


_TmnxBundleParentBundle_Object = MibTableColumn
tmnxBundleParentBundle = _TmnxBundleParentBundle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 22),
    _TmnxBundleParentBundle_Type()
)
tmnxBundleParentBundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleParentBundle.setStatus("current")
_TmnxBundleMemberTable_Object = MibTable
tmnxBundleMemberTable = _TmnxBundleMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15)
)
if mibBuilder.loadTexts:
    tmnxBundleMemberTable.setStatus("current")
_TmnxBundleMemberEntry_Object = MibTableRow
tmnxBundleMemberEntry = _TmnxBundleMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1)
)
tmnxBundleMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMemberEntry.setStatus("current")
_TmnxBundleMemberRowStatus_Type = RowStatus
_TmnxBundleMemberRowStatus_Object = MibTableColumn
tmnxBundleMemberRowStatus = _TmnxBundleMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 1),
    _TmnxBundleMemberRowStatus_Type()
)
tmnxBundleMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMemberRowStatus.setStatus("current")
_TmnxBundleMemberActive_Type = TruthValue
_TmnxBundleMemberActive_Object = MibTableColumn
tmnxBundleMemberActive = _TmnxBundleMemberActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 2),
    _TmnxBundleMemberActive_Type()
)
tmnxBundleMemberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberActive.setStatus("current")


class _TmnxBundleMemberDownReason_Type(Integer32):
    """Custom type tmnxBundleMemberDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mismatchEndPtDiscriminator", 3),
          ("none", 0),
          ("outOfService", 1),
          ("peerInvalidMlHdrFmt", 6),
          ("peerNotBundleMember", 4),
          ("redDiffDelayExceeded", 2),
          ("underNegotiation", 5))
    )


_TmnxBundleMemberDownReason_Type.__name__ = "Integer32"
_TmnxBundleMemberDownReason_Object = MibTableColumn
tmnxBundleMemberDownReason = _TmnxBundleMemberDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 3),
    _TmnxBundleMemberDownReason_Type()
)
tmnxBundleMemberDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberDownReason.setStatus("current")
_TmnxBundleMemberUpTime_Type = Unsigned32
_TmnxBundleMemberUpTime_Object = MibTableColumn
tmnxBundleMemberUpTime = _TmnxBundleMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 4),
    _TmnxBundleMemberUpTime_Type()
)
tmnxBundleMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMemberUpTime.setUnits("seconds")
_TmnxPortToChannelTable_Object = MibTable
tmnxPortToChannelTable = _TmnxPortToChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16)
)
if mibBuilder.loadTexts:
    tmnxPortToChannelTable.setStatus("current")
_TmnxPortToChannelEntry_Object = MibTableRow
tmnxPortToChannelEntry = _TmnxPortToChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1)
)
tmnxPortToChannelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxChannelIdxString"),
)
if mibBuilder.loadTexts:
    tmnxPortToChannelEntry.setStatus("current")
_TmnxChannelIdxString_Type = DisplayString
_TmnxChannelIdxString_Object = MibTableColumn
tmnxChannelIdxString = _TmnxChannelIdxString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1, 1),
    _TmnxChannelIdxString_Type()
)
tmnxChannelIdxString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChannelIdxString.setStatus("current")
_TmnxChannelPortID_Type = TmnxPortID
_TmnxChannelPortID_Object = MibTableColumn
tmnxChannelPortID = _TmnxChannelPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1, 2),
    _TmnxChannelPortID_Type()
)
tmnxChannelPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChannelPortID.setStatus("current")
_TmnxPortIngrMdaQosStatTable_Object = MibTable
tmnxPortIngrMdaQosStatTable = _TmnxPortIngrMdaQosStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17)
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatTable.setStatus("current")
_TmnxPortIngrMdaQosStatEntry_Object = MibTableRow
tmnxPortIngrMdaQosStatEntry = _TmnxPortIngrMdaQosStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1)
)
tmnxPortIngrMdaQosStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatEntry.setStatus("current")
_TmnxPortIngrMdaQos00StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos00StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos00StatDropPkts = _TmnxPortIngrMdaQos00StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 1),
    _TmnxPortIngrMdaQos00StatDropPkts_Type()
)
tmnxPortIngrMdaQos00StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos00StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos00StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos00StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos00StatDropOcts = _TmnxPortIngrMdaQos00StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 2),
    _TmnxPortIngrMdaQos00StatDropOcts_Type()
)
tmnxPortIngrMdaQos00StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos00StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos01StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos01StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos01StatDropPkts = _TmnxPortIngrMdaQos01StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 3),
    _TmnxPortIngrMdaQos01StatDropPkts_Type()
)
tmnxPortIngrMdaQos01StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos01StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos01StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos01StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos01StatDropOcts = _TmnxPortIngrMdaQos01StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 4),
    _TmnxPortIngrMdaQos01StatDropOcts_Type()
)
tmnxPortIngrMdaQos01StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos01StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos02StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos02StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos02StatDropPkts = _TmnxPortIngrMdaQos02StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 5),
    _TmnxPortIngrMdaQos02StatDropPkts_Type()
)
tmnxPortIngrMdaQos02StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos02StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos02StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos02StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos02StatDropOcts = _TmnxPortIngrMdaQos02StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 6),
    _TmnxPortIngrMdaQos02StatDropOcts_Type()
)
tmnxPortIngrMdaQos02StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos02StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos03StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos03StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos03StatDropPkts = _TmnxPortIngrMdaQos03StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 7),
    _TmnxPortIngrMdaQos03StatDropPkts_Type()
)
tmnxPortIngrMdaQos03StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos03StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos03StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos03StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos03StatDropOcts = _TmnxPortIngrMdaQos03StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 8),
    _TmnxPortIngrMdaQos03StatDropOcts_Type()
)
tmnxPortIngrMdaQos03StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos03StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos04StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos04StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos04StatDropPkts = _TmnxPortIngrMdaQos04StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 9),
    _TmnxPortIngrMdaQos04StatDropPkts_Type()
)
tmnxPortIngrMdaQos04StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos04StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos04StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos04StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos04StatDropOcts = _TmnxPortIngrMdaQos04StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 10),
    _TmnxPortIngrMdaQos04StatDropOcts_Type()
)
tmnxPortIngrMdaQos04StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos04StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos05StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos05StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos05StatDropPkts = _TmnxPortIngrMdaQos05StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 11),
    _TmnxPortIngrMdaQos05StatDropPkts_Type()
)
tmnxPortIngrMdaQos05StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos05StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos05StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos05StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos05StatDropOcts = _TmnxPortIngrMdaQos05StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 12),
    _TmnxPortIngrMdaQos05StatDropOcts_Type()
)
tmnxPortIngrMdaQos05StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos05StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos06StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos06StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos06StatDropPkts = _TmnxPortIngrMdaQos06StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 13),
    _TmnxPortIngrMdaQos06StatDropPkts_Type()
)
tmnxPortIngrMdaQos06StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos06StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos06StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos06StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos06StatDropOcts = _TmnxPortIngrMdaQos06StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 14),
    _TmnxPortIngrMdaQos06StatDropOcts_Type()
)
tmnxPortIngrMdaQos06StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos06StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos07StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos07StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos07StatDropPkts = _TmnxPortIngrMdaQos07StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 15),
    _TmnxPortIngrMdaQos07StatDropPkts_Type()
)
tmnxPortIngrMdaQos07StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos07StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos07StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos07StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos07StatDropOcts = _TmnxPortIngrMdaQos07StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 16),
    _TmnxPortIngrMdaQos07StatDropOcts_Type()
)
tmnxPortIngrMdaQos07StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos07StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos08StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos08StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos08StatDropPkts = _TmnxPortIngrMdaQos08StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 17),
    _TmnxPortIngrMdaQos08StatDropPkts_Type()
)
tmnxPortIngrMdaQos08StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos08StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos08StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos08StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos08StatDropOcts = _TmnxPortIngrMdaQos08StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 18),
    _TmnxPortIngrMdaQos08StatDropOcts_Type()
)
tmnxPortIngrMdaQos08StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos08StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos09StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos09StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos09StatDropPkts = _TmnxPortIngrMdaQos09StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 19),
    _TmnxPortIngrMdaQos09StatDropPkts_Type()
)
tmnxPortIngrMdaQos09StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos09StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos09StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos09StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos09StatDropOcts = _TmnxPortIngrMdaQos09StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 20),
    _TmnxPortIngrMdaQos09StatDropOcts_Type()
)
tmnxPortIngrMdaQos09StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos09StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos10StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos10StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos10StatDropPkts = _TmnxPortIngrMdaQos10StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 21),
    _TmnxPortIngrMdaQos10StatDropPkts_Type()
)
tmnxPortIngrMdaQos10StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos10StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos10StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos10StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos10StatDropOcts = _TmnxPortIngrMdaQos10StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 22),
    _TmnxPortIngrMdaQos10StatDropOcts_Type()
)
tmnxPortIngrMdaQos10StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos10StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos11StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos11StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos11StatDropPkts = _TmnxPortIngrMdaQos11StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 23),
    _TmnxPortIngrMdaQos11StatDropPkts_Type()
)
tmnxPortIngrMdaQos11StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos11StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos11StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos11StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos11StatDropOcts = _TmnxPortIngrMdaQos11StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 24),
    _TmnxPortIngrMdaQos11StatDropOcts_Type()
)
tmnxPortIngrMdaQos11StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos11StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos12StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos12StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos12StatDropPkts = _TmnxPortIngrMdaQos12StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 25),
    _TmnxPortIngrMdaQos12StatDropPkts_Type()
)
tmnxPortIngrMdaQos12StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos12StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos12StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos12StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos12StatDropOcts = _TmnxPortIngrMdaQos12StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 26),
    _TmnxPortIngrMdaQos12StatDropOcts_Type()
)
tmnxPortIngrMdaQos12StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos12StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos13StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos13StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos13StatDropPkts = _TmnxPortIngrMdaQos13StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 27),
    _TmnxPortIngrMdaQos13StatDropPkts_Type()
)
tmnxPortIngrMdaQos13StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos13StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos13StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos13StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos13StatDropOcts = _TmnxPortIngrMdaQos13StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 28),
    _TmnxPortIngrMdaQos13StatDropOcts_Type()
)
tmnxPortIngrMdaQos13StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos13StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos14StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos14StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos14StatDropPkts = _TmnxPortIngrMdaQos14StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 29),
    _TmnxPortIngrMdaQos14StatDropPkts_Type()
)
tmnxPortIngrMdaQos14StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos14StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos14StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos14StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos14StatDropOcts = _TmnxPortIngrMdaQos14StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 30),
    _TmnxPortIngrMdaQos14StatDropOcts_Type()
)
tmnxPortIngrMdaQos14StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos14StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos15StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos15StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos15StatDropPkts = _TmnxPortIngrMdaQos15StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 31),
    _TmnxPortIngrMdaQos15StatDropPkts_Type()
)
tmnxPortIngrMdaQos15StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos15StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos15StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos15StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos15StatDropOcts = _TmnxPortIngrMdaQos15StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 32),
    _TmnxPortIngrMdaQos15StatDropOcts_Type()
)
tmnxPortIngrMdaQos15StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos15StatDropOcts.setStatus("current")
_TmnxSonetGroupTable_Object = MibTable
tmnxSonetGroupTable = _TmnxSonetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18)
)
if mibBuilder.loadTexts:
    tmnxSonetGroupTable.setStatus("current")
_TmnxSonetGroupEntry_Object = MibTableRow
tmnxSonetGroupEntry = _TmnxSonetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1)
)
tmnxSonetGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetGroupEntry.setStatus("current")
_TmnxSonetGroupType_Type = TmnxMDAChanType
_TmnxSonetGroupType_Object = MibTableColumn
tmnxSonetGroupType = _TmnxSonetGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 1),
    _TmnxSonetGroupType_Type()
)
tmnxSonetGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupType.setStatus("current")
_TmnxSonetGroupParentPortID_Type = TmnxPortID
_TmnxSonetGroupParentPortID_Object = MibTableColumn
tmnxSonetGroupParentPortID = _TmnxSonetGroupParentPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 2),
    _TmnxSonetGroupParentPortID_Type()
)
tmnxSonetGroupParentPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupParentPortID.setStatus("current")
_TmnxSonetGroupChildType_Type = TmnxMDAChanType
_TmnxSonetGroupChildType_Object = MibTableColumn
tmnxSonetGroupChildType = _TmnxSonetGroupChildType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 3),
    _TmnxSonetGroupChildType_Type()
)
tmnxSonetGroupChildType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetGroupChildType.setStatus("current")
_TmnxSonetGroupName_Type = TNamedItemOrEmpty
_TmnxSonetGroupName_Object = MibTableColumn
tmnxSonetGroupName = _TmnxSonetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 4),
    _TmnxSonetGroupName_Type()
)
tmnxSonetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupName.setStatus("current")
_TmnxPortScalarObjs_ObjectIdentity = ObjectIdentity
tmnxPortScalarObjs = _TmnxPortScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19)
)


class _TmnxL4LoadBalancing_Type(TruthValue):
    """Custom type tmnxL4LoadBalancing based on TruthValue"""


_TmnxL4LoadBalancing_Object = MibScalar
tmnxL4LoadBalancing = _TmnxL4LoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19, 1),
    _TmnxL4LoadBalancing_Type()
)
tmnxL4LoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL4LoadBalancing.setStatus("current")
_TmnxCiscoHDLCTable_Object = MibTable
tmnxCiscoHDLCTable = _TmnxCiscoHDLCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCTable.setStatus("current")
_TmnxCiscoHDLCEntry_Object = MibTableRow
tmnxCiscoHDLCEntry = _TmnxCiscoHDLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1)
)
tmnxCiscoHDLCEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCEntry.setStatus("current")


class _TmnxCiscoHDLCKeepAliveInt_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCKeepAliveInt based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxCiscoHDLCKeepAliveInt_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCKeepAliveInt_Object = MibTableColumn
tmnxCiscoHDLCKeepAliveInt = _TmnxCiscoHDLCKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 1),
    _TmnxCiscoHDLCKeepAliveInt_Type()
)
tmnxCiscoHDLCKeepAliveInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCKeepAliveInt.setUnits("seconds")


class _TmnxCiscoHDLCUpCount_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCUpCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxCiscoHDLCUpCount_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCUpCount_Object = MibTableColumn
tmnxCiscoHDLCUpCount = _TmnxCiscoHDLCUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 2),
    _TmnxCiscoHDLCUpCount_Type()
)
tmnxCiscoHDLCUpCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCUpCount.setStatus("current")


class _TmnxCiscoHDLCDownCount_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCDownCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_TmnxCiscoHDLCDownCount_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCDownCount_Object = MibTableColumn
tmnxCiscoHDLCDownCount = _TmnxCiscoHDLCDownCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 3),
    _TmnxCiscoHDLCDownCount_Type()
)
tmnxCiscoHDLCDownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDownCount.setStatus("current")
_TmnxCiscoHDLCOperState_Type = TmnxOperState
_TmnxCiscoHDLCOperState_Object = MibTableColumn
tmnxCiscoHDLCOperState = _TmnxCiscoHDLCOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 4),
    _TmnxCiscoHDLCOperState_Type()
)
tmnxCiscoHDLCOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCOperState.setStatus("current")
_TmnxBundleImaGrpTable_Object = MibTable
tmnxBundleImaGrpTable = _TmnxBundleImaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21)
)
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTable.setStatus("current")
_TmnxBundleImaGrpEntry_Object = MibTableRow
tmnxBundleImaGrpEntry = _TmnxBundleImaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1)
)
tmnxBundleImaGrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleImaGrpEntry.setStatus("current")


class _TmnxBundleImaGrpLnkActTimer_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpLnkActTimer based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_TmnxBundleImaGrpLnkActTimer_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpLnkActTimer_Object = MibTableColumn
tmnxBundleImaGrpLnkActTimer = _TmnxBundleImaGrpLnkActTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 1),
    _TmnxBundleImaGrpLnkActTimer_Type()
)
tmnxBundleImaGrpLnkActTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkActTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkActTimer.setUnits("milliseconds")


class _TmnxBundleImaGrpLnkDeactTimer_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpLnkDeactTimer based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_TmnxBundleImaGrpLnkDeactTimer_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpLnkDeactTimer_Object = MibTableColumn
tmnxBundleImaGrpLnkDeactTimer = _TmnxBundleImaGrpLnkDeactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 2),
    _TmnxBundleImaGrpLnkDeactTimer_Type()
)
tmnxBundleImaGrpLnkDeactTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkDeactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkDeactTimer.setUnits("milliseconds")


class _TmnxBundleImaGrpSymmetryMode_Type(Integer32):
    """Custom type tmnxBundleImaGrpSymmetryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("symmetric", 1)
    )


_TmnxBundleImaGrpSymmetryMode_Type.__name__ = "Integer32"
_TmnxBundleImaGrpSymmetryMode_Object = MibTableColumn
tmnxBundleImaGrpSymmetryMode = _TmnxBundleImaGrpSymmetryMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 3),
    _TmnxBundleImaGrpSymmetryMode_Type()
)
tmnxBundleImaGrpSymmetryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSymmetryMode.setStatus("current")
_TmnxBundleImaGrpTxId_Type = Integer32
_TmnxBundleImaGrpTxId_Object = MibTableColumn
tmnxBundleImaGrpTxId = _TmnxBundleImaGrpTxId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 4),
    _TmnxBundleImaGrpTxId_Type()
)
tmnxBundleImaGrpTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxId.setStatus("current")
_TmnxBundleImaGrpRxId_Type = Integer32
_TmnxBundleImaGrpRxId_Object = MibTableColumn
tmnxBundleImaGrpRxId = _TmnxBundleImaGrpRxId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 5),
    _TmnxBundleImaGrpRxId_Type()
)
tmnxBundleImaGrpRxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxId.setStatus("current")
_TmnxBundleImaGrpTxRefLnk_Type = TmnxPortID
_TmnxBundleImaGrpTxRefLnk_Object = MibTableColumn
tmnxBundleImaGrpTxRefLnk = _TmnxBundleImaGrpTxRefLnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 6),
    _TmnxBundleImaGrpTxRefLnk_Type()
)
tmnxBundleImaGrpTxRefLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxRefLnk.setStatus("current")
_TmnxBundleImaGrpRxRefLnk_Type = TmnxPortID
_TmnxBundleImaGrpRxRefLnk_Object = MibTableColumn
tmnxBundleImaGrpRxRefLnk = _TmnxBundleImaGrpRxRefLnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 7),
    _TmnxBundleImaGrpRxRefLnk_Type()
)
tmnxBundleImaGrpRxRefLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxRefLnk.setStatus("current")
_TmnxBundleImaGrpSmNeState_Type = TmnxImaGrpState
_TmnxBundleImaGrpSmNeState_Object = MibTableColumn
tmnxBundleImaGrpSmNeState = _TmnxBundleImaGrpSmNeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 8),
    _TmnxBundleImaGrpSmNeState_Type()
)
tmnxBundleImaGrpSmNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmNeState.setStatus("current")
_TmnxBundleImaGrpSmFeState_Type = TmnxImaGrpState
_TmnxBundleImaGrpSmFeState_Object = MibTableColumn
tmnxBundleImaGrpSmFeState = _TmnxBundleImaGrpSmFeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 9),
    _TmnxBundleImaGrpSmFeState_Type()
)
tmnxBundleImaGrpSmFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmFeState.setStatus("current")
_TmnxBundleImaGrpSmFailState_Type = TmnxImaGrpFailState
_TmnxBundleImaGrpSmFailState_Object = MibTableColumn
tmnxBundleImaGrpSmFailState = _TmnxBundleImaGrpSmFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 10),
    _TmnxBundleImaGrpSmFailState_Type()
)
tmnxBundleImaGrpSmFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmFailState.setStatus("current")
_TmnxBundleImaGrpSmDownSecs_Type = Counter32
_TmnxBundleImaGrpSmDownSecs_Object = MibTableColumn
tmnxBundleImaGrpSmDownSecs = _TmnxBundleImaGrpSmDownSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 11),
    _TmnxBundleImaGrpSmDownSecs_Type()
)
tmnxBundleImaGrpSmDownSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmDownSecs.setStatus("current")
_TmnxBundleImaGrpSmOperSecs_Type = Counter32
_TmnxBundleImaGrpSmOperSecs_Object = MibTableColumn
tmnxBundleImaGrpSmOperSecs = _TmnxBundleImaGrpSmOperSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 12),
    _TmnxBundleImaGrpSmOperSecs_Type()
)
tmnxBundleImaGrpSmOperSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmOperSecs.setStatus("current")
_TmnxBundleImaGrpAvailTxCR_Type = Gauge32
_TmnxBundleImaGrpAvailTxCR_Object = MibTableColumn
tmnxBundleImaGrpAvailTxCR = _TmnxBundleImaGrpAvailTxCR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 13),
    _TmnxBundleImaGrpAvailTxCR_Type()
)
tmnxBundleImaGrpAvailTxCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAvailTxCR.setStatus("current")
_TmnxBundleImaGrpAvailRxCR_Type = Gauge32
_TmnxBundleImaGrpAvailRxCR_Object = MibTableColumn
tmnxBundleImaGrpAvailRxCR = _TmnxBundleImaGrpAvailRxCR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 14),
    _TmnxBundleImaGrpAvailRxCR_Type()
)
tmnxBundleImaGrpAvailRxCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAvailRxCR.setStatus("current")
_TmnxBundleImaGrpNeFails_Type = Counter32
_TmnxBundleImaGrpNeFails_Object = MibTableColumn
tmnxBundleImaGrpNeFails = _TmnxBundleImaGrpNeFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 15),
    _TmnxBundleImaGrpNeFails_Type()
)
tmnxBundleImaGrpNeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpNeFails.setStatus("current")
_TmnxBundleImaGrpFeFails_Type = Counter32
_TmnxBundleImaGrpFeFails_Object = MibTableColumn
tmnxBundleImaGrpFeFails = _TmnxBundleImaGrpFeFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 16),
    _TmnxBundleImaGrpFeFails_Type()
)
tmnxBundleImaGrpFeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpFeFails.setStatus("current")
_TmnxBundleImaGrpTxIcpCells_Type = Counter32
_TmnxBundleImaGrpTxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpTxIcpCells = _TmnxBundleImaGrpTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 17),
    _TmnxBundleImaGrpTxIcpCells_Type()
)
tmnxBundleImaGrpTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxIcpCells.setStatus("current")
_TmnxBundleImaGrpRxIcpCells_Type = Counter32
_TmnxBundleImaGrpRxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpRxIcpCells = _TmnxBundleImaGrpRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 18),
    _TmnxBundleImaGrpRxIcpCells_Type()
)
tmnxBundleImaGrpRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxIcpCells.setStatus("current")
_TmnxBundleImaGrpErrorIcpCells_Type = Counter32
_TmnxBundleImaGrpErrorIcpCells_Object = MibTableColumn
tmnxBundleImaGrpErrorIcpCells = _TmnxBundleImaGrpErrorIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 19),
    _TmnxBundleImaGrpErrorIcpCells_Type()
)
tmnxBundleImaGrpErrorIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpErrorIcpCells.setStatus("current")
_TmnxBundleImaGrpLostRxIcpCells_Type = Counter32
_TmnxBundleImaGrpLostRxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpLostRxIcpCells = _TmnxBundleImaGrpLostRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 20),
    _TmnxBundleImaGrpLostRxIcpCells_Type()
)
tmnxBundleImaGrpLostRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLostRxIcpCells.setStatus("current")
_TmnxBundleImaGrpTxOamLablVal_Type = Integer32
_TmnxBundleImaGrpTxOamLablVal_Object = MibTableColumn
tmnxBundleImaGrpTxOamLablVal = _TmnxBundleImaGrpTxOamLablVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 21),
    _TmnxBundleImaGrpTxOamLablVal_Type()
)
tmnxBundleImaGrpTxOamLablVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxOamLablVal.setStatus("current")
_TmnxBundleImaGrpRxOamLablVal_Type = Integer32
_TmnxBundleImaGrpRxOamLablVal_Object = MibTableColumn
tmnxBundleImaGrpRxOamLablVal = _TmnxBundleImaGrpRxOamLablVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 22),
    _TmnxBundleImaGrpRxOamLablVal_Type()
)
tmnxBundleImaGrpRxOamLablVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxOamLablVal.setStatus("current")


class _TmnxBundleImaGrpAlphaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpAlphaValue based on Integer32"""
    defaultValue = 2


_TmnxBundleImaGrpAlphaValue_Object = MibTableColumn
tmnxBundleImaGrpAlphaValue = _TmnxBundleImaGrpAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 23),
    _TmnxBundleImaGrpAlphaValue_Type()
)
tmnxBundleImaGrpAlphaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAlphaValue.setStatus("current")


class _TmnxBundleImaGrpBetaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpBetaValue based on Integer32"""
    defaultValue = 2


_TmnxBundleImaGrpBetaValue_Object = MibTableColumn
tmnxBundleImaGrpBetaValue = _TmnxBundleImaGrpBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 24),
    _TmnxBundleImaGrpBetaValue_Type()
)
tmnxBundleImaGrpBetaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpBetaValue.setStatus("current")


class _TmnxBundleImaGrpGammaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpGammaValue based on Integer32"""
    defaultValue = 1


_TmnxBundleImaGrpGammaValue_Object = MibTableColumn
tmnxBundleImaGrpGammaValue = _TmnxBundleImaGrpGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 25),
    _TmnxBundleImaGrpGammaValue_Type()
)
tmnxBundleImaGrpGammaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpGammaValue.setStatus("current")


class _TmnxBundleImaGrpNeClockMode_Type(TmnxImaGrpClockModes):
    """Custom type tmnxBundleImaGrpNeClockMode based on TmnxImaGrpClockModes"""


_TmnxBundleImaGrpNeClockMode_Object = MibTableColumn
tmnxBundleImaGrpNeClockMode = _TmnxBundleImaGrpNeClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 26),
    _TmnxBundleImaGrpNeClockMode_Type()
)
tmnxBundleImaGrpNeClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpNeClockMode.setStatus("current")


class _TmnxBundleImaGrpFeClockMode_Type(TmnxImaGrpClockModes):
    """Custom type tmnxBundleImaGrpFeClockMode based on TmnxImaGrpClockModes"""


_TmnxBundleImaGrpFeClockMode_Object = MibTableColumn
tmnxBundleImaGrpFeClockMode = _TmnxBundleImaGrpFeClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 27),
    _TmnxBundleImaGrpFeClockMode_Type()
)
tmnxBundleImaGrpFeClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpFeClockMode.setStatus("current")


class _TmnxBundleImaGrpVersion_Type(TmnxImaGrpVersion):
    """Custom type tmnxBundleImaGrpVersion based on TmnxImaGrpVersion"""


_TmnxBundleImaGrpVersion_Object = MibTableColumn
tmnxBundleImaGrpVersion = _TmnxBundleImaGrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 28),
    _TmnxBundleImaGrpVersion_Type()
)
tmnxBundleImaGrpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpVersion.setStatus("current")


class _TmnxBundleImaGrpMaxConfBw_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpMaxConfBw based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxBundleImaGrpMaxConfBw_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpMaxConfBw_Object = MibTableColumn
tmnxBundleImaGrpMaxConfBw = _TmnxBundleImaGrpMaxConfBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 29),
    _TmnxBundleImaGrpMaxConfBw_Type()
)
tmnxBundleImaGrpMaxConfBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpMaxConfBw.setStatus("current")


class _TmnxBundleImaGrpTestState_Type(TmnxImaTestState):
    """Custom type tmnxBundleImaGrpTestState based on TmnxImaTestState"""


_TmnxBundleImaGrpTestState_Object = MibTableColumn
tmnxBundleImaGrpTestState = _TmnxBundleImaGrpTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 30),
    _TmnxBundleImaGrpTestState_Type()
)
tmnxBundleImaGrpTestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestState.setStatus("current")


class _TmnxBundleImaGrpTestMember_Type(TmnxPortID):
    """Custom type tmnxBundleImaGrpTestMember based on TmnxPortID"""
    defaultValue = 0


_TmnxBundleImaGrpTestMember_Object = MibTableColumn
tmnxBundleImaGrpTestMember = _TmnxBundleImaGrpTestMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 31),
    _TmnxBundleImaGrpTestMember_Type()
)
tmnxBundleImaGrpTestMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestMember.setStatus("current")


class _TmnxBundleImaGrpTestPattern_Type(Integer32):
    """Custom type tmnxBundleImaGrpTestPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxBundleImaGrpTestPattern_Type.__name__ = "Integer32"
_TmnxBundleImaGrpTestPattern_Object = MibTableColumn
tmnxBundleImaGrpTestPattern = _TmnxBundleImaGrpTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 32),
    _TmnxBundleImaGrpTestPattern_Type()
)
tmnxBundleImaGrpTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestPattern.setStatus("current")
_TmnxBundleImaGrpDiffDelayMaxObs_Type = Unsigned32
_TmnxBundleImaGrpDiffDelayMaxObs_Object = MibTableColumn
tmnxBundleImaGrpDiffDelayMaxObs = _TmnxBundleImaGrpDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 33),
    _TmnxBundleImaGrpDiffDelayMaxObs_Type()
)
tmnxBundleImaGrpDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpDiffDelayMaxObs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpDiffDelayMaxObs.setUnits("milliseconds")
_TmnxBundleImaGrpLeastDelayLink_Type = Unsigned32
_TmnxBundleImaGrpLeastDelayLink_Object = MibTableColumn
tmnxBundleImaGrpLeastDelayLink = _TmnxBundleImaGrpLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 34),
    _TmnxBundleImaGrpLeastDelayLink_Type()
)
tmnxBundleImaGrpLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLeastDelayLink.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLeastDelayLink.setUnits("milliseconds")
_TmnxBundleMemberImaTable_Object = MibTable
tmnxBundleMemberImaTable = _TmnxBundleMemberImaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22)
)
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTable.setStatus("current")
_TmnxBundleMemberImaEntry_Object = MibTableRow
tmnxBundleMemberImaEntry = _TmnxBundleMemberImaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1)
)
tmnxBundleMemberImaEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMemberImaEntry.setStatus("current")
_TmnxBundleMemberImaNeTxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaNeTxState_Object = MibTableColumn
tmnxBundleMemberImaNeTxState = _TmnxBundleMemberImaNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 1),
    _TmnxBundleMemberImaNeTxState_Type()
)
tmnxBundleMemberImaNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxState.setStatus("current")
_TmnxBundleMemberImaNeRxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaNeRxState_Object = MibTableColumn
tmnxBundleMemberImaNeRxState = _TmnxBundleMemberImaNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 2),
    _TmnxBundleMemberImaNeRxState_Type()
)
tmnxBundleMemberImaNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxState.setStatus("current")
_TmnxBundleMemberImaFeTxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaFeTxState_Object = MibTableColumn
tmnxBundleMemberImaFeTxState = _TmnxBundleMemberImaFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 3),
    _TmnxBundleMemberImaFeTxState_Type()
)
tmnxBundleMemberImaFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxState.setStatus("current")
_TmnxBundleMemberImaFeRxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaFeRxState_Object = MibTableColumn
tmnxBundleMemberImaFeRxState = _TmnxBundleMemberImaFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 4),
    _TmnxBundleMemberImaFeRxState_Type()
)
tmnxBundleMemberImaFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxState.setStatus("current")
_TmnxBundleMemberImaNeRxFailState_Type = TmnxImaLnkFailState
_TmnxBundleMemberImaNeRxFailState_Object = MibTableColumn
tmnxBundleMemberImaNeRxFailState = _TmnxBundleMemberImaNeRxFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 5),
    _TmnxBundleMemberImaNeRxFailState_Type()
)
tmnxBundleMemberImaNeRxFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxFailState.setStatus("current")
_TmnxBundleMemberImaFeRxFailState_Type = TmnxImaLnkFailState
_TmnxBundleMemberImaFeRxFailState_Object = MibTableColumn
tmnxBundleMemberImaFeRxFailState = _TmnxBundleMemberImaFeRxFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 6),
    _TmnxBundleMemberImaFeRxFailState_Type()
)
tmnxBundleMemberImaFeRxFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxFailState.setStatus("current")
_TmnxBundleMemberImaTxLid_Type = Integer32
_TmnxBundleMemberImaTxLid_Object = MibTableColumn
tmnxBundleMemberImaTxLid = _TmnxBundleMemberImaTxLid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 7),
    _TmnxBundleMemberImaTxLid_Type()
)
tmnxBundleMemberImaTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTxLid.setStatus("current")
_TmnxBundleMemberImaRxLid_Type = Integer32
_TmnxBundleMemberImaRxLid_Object = MibTableColumn
tmnxBundleMemberImaRxLid = _TmnxBundleMemberImaRxLid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 8),
    _TmnxBundleMemberImaRxLid_Type()
)
tmnxBundleMemberImaRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxLid.setStatus("current")
_TmnxBundleMemberImaViolations_Type = Counter32
_TmnxBundleMemberImaViolations_Object = MibTableColumn
tmnxBundleMemberImaViolations = _TmnxBundleMemberImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 9),
    _TmnxBundleMemberImaViolations_Type()
)
tmnxBundleMemberImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaViolations.setStatus("current")
_TmnxBundleMemberImaNeSevErrSecs_Type = Counter32
_TmnxBundleMemberImaNeSevErrSecs_Object = MibTableColumn
tmnxBundleMemberImaNeSevErrSecs = _TmnxBundleMemberImaNeSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 10),
    _TmnxBundleMemberImaNeSevErrSecs_Type()
)
tmnxBundleMemberImaNeSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeSevErrSecs.setStatus("current")
_TmnxBundleMemberImaFeSevErrSecs_Type = Counter32
_TmnxBundleMemberImaFeSevErrSecs_Object = MibTableColumn
tmnxBundleMemberImaFeSevErrSecs = _TmnxBundleMemberImaFeSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 11),
    _TmnxBundleMemberImaFeSevErrSecs_Type()
)
tmnxBundleMemberImaFeSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeSevErrSecs.setStatus("current")
_TmnxBundleMemberImaNeUnavailSecs_Type = Counter32
_TmnxBundleMemberImaNeUnavailSecs_Object = MibTableColumn
tmnxBundleMemberImaNeUnavailSecs = _TmnxBundleMemberImaNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 12),
    _TmnxBundleMemberImaNeUnavailSecs_Type()
)
tmnxBundleMemberImaNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeUnavailSecs.setStatus("current")
_TmnxBundleMemberImaFeUnavailSecs_Type = Counter32
_TmnxBundleMemberImaFeUnavailSecs_Object = MibTableColumn
tmnxBundleMemberImaFeUnavailSecs = _TmnxBundleMemberImaFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 13),
    _TmnxBundleMemberImaFeUnavailSecs_Type()
)
tmnxBundleMemberImaFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeUnavailSecs.setStatus("current")
_TmnxBundleMemberImaNeTxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaNeTxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaNeTxUnuseSecs = _TmnxBundleMemberImaNeTxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 14),
    _TmnxBundleMemberImaNeTxUnuseSecs_Type()
)
tmnxBundleMemberImaNeTxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaNeRxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaNeRxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaNeRxUnuseSecs = _TmnxBundleMemberImaNeRxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 15),
    _TmnxBundleMemberImaNeRxUnuseSecs_Type()
)
tmnxBundleMemberImaNeRxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaFeTxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaFeTxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaFeTxUnuseSecs = _TmnxBundleMemberImaFeTxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 16),
    _TmnxBundleMemberImaFeTxUnuseSecs_Type()
)
tmnxBundleMemberImaFeTxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaFeRxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaFeRxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaFeRxUnuseSecs = _TmnxBundleMemberImaFeRxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 17),
    _TmnxBundleMemberImaFeRxUnuseSecs_Type()
)
tmnxBundleMemberImaFeRxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaNeTxNumFails_Type = Counter32
_TmnxBundleMemberImaNeTxNumFails_Object = MibTableColumn
tmnxBundleMemberImaNeTxNumFails = _TmnxBundleMemberImaNeTxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 18),
    _TmnxBundleMemberImaNeTxNumFails_Type()
)
tmnxBundleMemberImaNeTxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxNumFails.setStatus("current")
_TmnxBundleMemberImaNeRxNumFails_Type = Counter32
_TmnxBundleMemberImaNeRxNumFails_Object = MibTableColumn
tmnxBundleMemberImaNeRxNumFails = _TmnxBundleMemberImaNeRxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 19),
    _TmnxBundleMemberImaNeRxNumFails_Type()
)
tmnxBundleMemberImaNeRxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxNumFails.setStatus("current")
_TmnxBundleMemberImaFeTxNumFails_Type = Counter32
_TmnxBundleMemberImaFeTxNumFails_Object = MibTableColumn
tmnxBundleMemberImaFeTxNumFails = _TmnxBundleMemberImaFeTxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 20),
    _TmnxBundleMemberImaFeTxNumFails_Type()
)
tmnxBundleMemberImaFeTxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxNumFails.setStatus("current")
_TmnxBundleMemberImaFeRxNumFails_Type = Counter32
_TmnxBundleMemberImaFeRxNumFails_Object = MibTableColumn
tmnxBundleMemberImaFeRxNumFails = _TmnxBundleMemberImaFeRxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 21),
    _TmnxBundleMemberImaFeRxNumFails_Type()
)
tmnxBundleMemberImaFeRxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxNumFails.setStatus("current")
_TmnxBundleMemberImaTxIcpCells_Type = Counter32
_TmnxBundleMemberImaTxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaTxIcpCells = _TmnxBundleMemberImaTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 22),
    _TmnxBundleMemberImaTxIcpCells_Type()
)
tmnxBundleMemberImaTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTxIcpCells.setStatus("current")
_TmnxBundleMemberImaRxIcpCells_Type = Counter32
_TmnxBundleMemberImaRxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaRxIcpCells = _TmnxBundleMemberImaRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 23),
    _TmnxBundleMemberImaRxIcpCells_Type()
)
tmnxBundleMemberImaRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxIcpCells.setStatus("current")
_TmnxBundleMemberImaErrorIcpCells_Type = Counter32
_TmnxBundleMemberImaErrorIcpCells_Object = MibTableColumn
tmnxBundleMemberImaErrorIcpCells = _TmnxBundleMemberImaErrorIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 24),
    _TmnxBundleMemberImaErrorIcpCells_Type()
)
tmnxBundleMemberImaErrorIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaErrorIcpCells.setStatus("current")
_TmnxBundleMemberImaLstRxIcpCells_Type = Counter32
_TmnxBundleMemberImaLstRxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaLstRxIcpCells = _TmnxBundleMemberImaLstRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 25),
    _TmnxBundleMemberImaLstRxIcpCells_Type()
)
tmnxBundleMemberImaLstRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaLstRxIcpCells.setStatus("current")
_TmnxBundleMemberImaOifAnomalies_Type = Counter32
_TmnxBundleMemberImaOifAnomalies_Object = MibTableColumn
tmnxBundleMemberImaOifAnomalies = _TmnxBundleMemberImaOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 26),
    _TmnxBundleMemberImaOifAnomalies_Type()
)
tmnxBundleMemberImaOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaOifAnomalies.setStatus("current")
_TmnxBundleMemberImaRxTestState_Type = TmnxImaTestState
_TmnxBundleMemberImaRxTestState_Object = MibTableColumn
tmnxBundleMemberImaRxTestState = _TmnxBundleMemberImaRxTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 27),
    _TmnxBundleMemberImaRxTestState_Type()
)
tmnxBundleMemberImaRxTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxTestState.setStatus("current")


class _TmnxBundleMemberImaRxTestPattern_Type(Integer32):
    """Custom type tmnxBundleMemberImaRxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxBundleMemberImaRxTestPattern_Type.__name__ = "Integer32"
_TmnxBundleMemberImaRxTestPattern_Object = MibTableColumn
tmnxBundleMemberImaRxTestPattern = _TmnxBundleMemberImaRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 28),
    _TmnxBundleMemberImaRxTestPattern_Type()
)
tmnxBundleMemberImaRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxTestPattern.setStatus("current")
_TmnxBundleMemberImaRelDelay_Type = Unsigned32
_TmnxBundleMemberImaRelDelay_Object = MibTableColumn
tmnxBundleMemberImaRelDelay = _TmnxBundleMemberImaRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 29),
    _TmnxBundleMemberImaRelDelay_Type()
)
tmnxBundleMemberImaRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRelDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRelDelay.setUnits("milliseconds")
_TmnxDS1PortTable_Object = MibTable
tmnxDS1PortTable = _TmnxDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23)
)
if mibBuilder.loadTexts:
    tmnxDS1PortTable.setStatus("current")
_TmnxDS1PortEntry_Object = MibTableRow
tmnxDS1PortEntry = _TmnxDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1)
)
tmnxDS1PortEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS1PortEntry.setStatus("current")


class _TmnxDS1PortBuildout_Type(Integer32):
    """Custom type tmnxDS1PortBuildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_TmnxDS1PortBuildout_Type.__name__ = "Integer32"
_TmnxDS1PortBuildout_Object = MibTableColumn
tmnxDS1PortBuildout = _TmnxDS1PortBuildout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 1),
    _TmnxDS1PortBuildout_Type()
)
tmnxDS1PortBuildout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortBuildout.setStatus("current")
_TmnxDS1PortLastChangeTime_Type = TimeStamp
_TmnxDS1PortLastChangeTime_Object = MibTableColumn
tmnxDS1PortLastChangeTime = _TmnxDS1PortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 2),
    _TmnxDS1PortLastChangeTime_Type()
)
tmnxDS1PortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1PortLastChangeTime.setStatus("current")


class _TmnxDS1PortType_Type(Integer32):
    """Custom type tmnxDS1PortType based on Integer32"""
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
        *(("ds1", 1),
          ("e1", 2),
          ("j1", 3))
    )


_TmnxDS1PortType_Type.__name__ = "Integer32"
_TmnxDS1PortType_Object = MibTableColumn
tmnxDS1PortType = _TmnxDS1PortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 3),
    _TmnxDS1PortType_Type()
)
tmnxDS1PortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortType.setStatus("current")


class _TmnxDS1PortLineLength_Type(Integer32):
    """Custom type tmnxDS1PortLineLength based on Integer32"""
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
        *(("length0To133", 2),
          ("length134To266", 3),
          ("length267To399", 4),
          ("length400To533", 5),
          ("length534To655", 6),
          ("lengthNotApplicable", 1))
    )


_TmnxDS1PortLineLength_Type.__name__ = "Integer32"
_TmnxDS1PortLineLength_Object = MibTableColumn
tmnxDS1PortLineLength = _TmnxDS1PortLineLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 4),
    _TmnxDS1PortLineLength_Type()
)
tmnxDS1PortLineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortLineLength.setStatus("current")


class _TmnxDS1PortLbo_Type(Integer32):
    """Custom type tmnxDS1PortLbo based on Integer32"""
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
        *(("lbo0dB", 2),
          ("lboNeg15p0dB", 4),
          ("lboNeg22p5dB", 5),
          ("lboNeg7p5dB", 3),
          ("lboNotApplicable", 1))
    )


_TmnxDS1PortLbo_Type.__name__ = "Integer32"
_TmnxDS1PortLbo_Object = MibTableColumn
tmnxDS1PortLbo = _TmnxDS1PortLbo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 5),
    _TmnxDS1PortLbo_Type()
)
tmnxDS1PortLbo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortLbo.setStatus("current")
_TmnxDS1PortDbGain_Type = Integer32
_TmnxDS1PortDbGain_Object = MibTableColumn
tmnxDS1PortDbGain = _TmnxDS1PortDbGain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 6),
    _TmnxDS1PortDbGain_Type()
)
tmnxDS1PortDbGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1PortDbGain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1PortDbGain.setUnits("db")
_TmnxPortSchedOverrideTable_Object = MibTable
tmnxPortSchedOverrideTable = _TmnxPortSchedOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24)
)
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideTable.setStatus("current")
_TmnxPortSchedOverrideEntry_Object = MibTableRow
tmnxPortSchedOverrideEntry = _TmnxPortSchedOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1)
)
tmnxPortSchedOverrideEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideEntry.setStatus("current")
_TmnxPortSchedOverrideRowStatus_Type = RowStatus
_TmnxPortSchedOverrideRowStatus_Object = MibTableColumn
tmnxPortSchedOverrideRowStatus = _TmnxPortSchedOverrideRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 1),
    _TmnxPortSchedOverrideRowStatus_Type()
)
tmnxPortSchedOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideRowStatus.setStatus("current")
_TmnxPortSchedOverrideSchedName_Type = DisplayString
_TmnxPortSchedOverrideSchedName_Object = MibTableColumn
tmnxPortSchedOverrideSchedName = _TmnxPortSchedOverrideSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 2),
    _TmnxPortSchedOverrideSchedName_Type()
)
tmnxPortSchedOverrideSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideSchedName.setStatus("current")
_TmnxPortSchedOverrideLastChanged_Type = TimeStamp
_TmnxPortSchedOverrideLastChanged_Object = MibTableColumn
tmnxPortSchedOverrideLastChanged = _TmnxPortSchedOverrideLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 3),
    _TmnxPortSchedOverrideLastChanged_Type()
)
tmnxPortSchedOverrideLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLastChanged.setStatus("current")


class _TmnxPortSchedOverrideMaxRate_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideMaxRate based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideMaxRate_Object = MibTableColumn
tmnxPortSchedOverrideMaxRate = _TmnxPortSchedOverrideMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 4),
    _TmnxPortSchedOverrideMaxRate_Type()
)
tmnxPortSchedOverrideMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideMaxRate.setUnits("kbps")


class _TmnxPortSchedOverrideLvl1PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl1PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl1PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl1PIR = _TmnxPortSchedOverrideLvl1PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 5),
    _TmnxPortSchedOverrideLvl1PIR_Type()
)
tmnxPortSchedOverrideLvl1PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl1CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl1CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl1CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl1CIR = _TmnxPortSchedOverrideLvl1CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 6),
    _TmnxPortSchedOverrideLvl1CIR_Type()
)
tmnxPortSchedOverrideLvl1CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl2PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl2PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl2PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl2PIR = _TmnxPortSchedOverrideLvl2PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 7),
    _TmnxPortSchedOverrideLvl2PIR_Type()
)
tmnxPortSchedOverrideLvl2PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl2CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl2CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl2CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl2CIR = _TmnxPortSchedOverrideLvl2CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 8),
    _TmnxPortSchedOverrideLvl2CIR_Type()
)
tmnxPortSchedOverrideLvl2CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl3PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl3PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl3PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl3PIR = _TmnxPortSchedOverrideLvl3PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 9),
    _TmnxPortSchedOverrideLvl3PIR_Type()
)
tmnxPortSchedOverrideLvl3PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl3CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl3CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl3CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl3CIR = _TmnxPortSchedOverrideLvl3CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 10),
    _TmnxPortSchedOverrideLvl3CIR_Type()
)
tmnxPortSchedOverrideLvl3CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl4PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl4PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl4PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl4PIR = _TmnxPortSchedOverrideLvl4PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 11),
    _TmnxPortSchedOverrideLvl4PIR_Type()
)
tmnxPortSchedOverrideLvl4PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl4CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl4CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl4CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl4CIR = _TmnxPortSchedOverrideLvl4CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 12),
    _TmnxPortSchedOverrideLvl4CIR_Type()
)
tmnxPortSchedOverrideLvl4CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl5PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl5PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl5PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl5PIR = _TmnxPortSchedOverrideLvl5PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 13),
    _TmnxPortSchedOverrideLvl5PIR_Type()
)
tmnxPortSchedOverrideLvl5PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl5CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl5CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl5CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl5CIR = _TmnxPortSchedOverrideLvl5CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 14),
    _TmnxPortSchedOverrideLvl5CIR_Type()
)
tmnxPortSchedOverrideLvl5CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl6PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl6PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl6PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl6PIR = _TmnxPortSchedOverrideLvl6PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 15),
    _TmnxPortSchedOverrideLvl6PIR_Type()
)
tmnxPortSchedOverrideLvl6PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl6CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl6CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl6CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl6CIR = _TmnxPortSchedOverrideLvl6CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 16),
    _TmnxPortSchedOverrideLvl6CIR_Type()
)
tmnxPortSchedOverrideLvl6CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl7PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl7PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl7PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl7PIR = _TmnxPortSchedOverrideLvl7PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 17),
    _TmnxPortSchedOverrideLvl7PIR_Type()
)
tmnxPortSchedOverrideLvl7PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl7CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl7CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl7CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl7CIR = _TmnxPortSchedOverrideLvl7CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 18),
    _TmnxPortSchedOverrideLvl7CIR_Type()
)
tmnxPortSchedOverrideLvl7CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl8PIR_Type(TPortSchedulerPIR):
    """Custom type tmnxPortSchedOverrideLvl8PIR based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl8PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl8PIR = _TmnxPortSchedOverrideLvl8PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 19),
    _TmnxPortSchedOverrideLvl8PIR_Type()
)
tmnxPortSchedOverrideLvl8PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl8CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl8CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl8CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl8CIR = _TmnxPortSchedOverrideLvl8CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 20),
    _TmnxPortSchedOverrideLvl8CIR_Type()
)
tmnxPortSchedOverrideLvl8CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8CIR.setUnits("kbps")


class _TmnxPortSchedOverrideFlags_Type(Bits):
    """Custom type tmnxPortSchedOverrideFlags based on Bits"""
    namedValues = NamedValues(
        *(("lvl1CIR", 2),
          ("lvl1PIR", 1),
          ("lvl2CIR", 4),
          ("lvl2PIR", 3),
          ("lvl3CIR", 6),
          ("lvl3PIR", 5),
          ("lvl4CIR", 8),
          ("lvl4PIR", 7),
          ("lvl5CIR", 10),
          ("lvl5PIR", 9),
          ("lvl6CIR", 12),
          ("lvl6PIR", 11),
          ("lvl7CIR", 14),
          ("lvl7PIR", 13),
          ("lvl8CIR", 16),
          ("lvl8PIR", 15),
          ("maxRate", 0))
    )

_TmnxPortSchedOverrideFlags_Type.__name__ = "Bits"
_TmnxPortSchedOverrideFlags_Object = MibTableColumn
tmnxPortSchedOverrideFlags = _TmnxPortSchedOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 21),
    _TmnxPortSchedOverrideFlags_Type()
)
tmnxPortSchedOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideFlags.setStatus("current")
_TmnxBPGrpAssocTable_Object = MibTable
tmnxBPGrpAssocTable = _TmnxBPGrpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25)
)
if mibBuilder.loadTexts:
    tmnxBPGrpAssocTable.setStatus("current")
_TmnxBPGrpAssocEntry_Object = MibTableRow
tmnxBPGrpAssocEntry = _TmnxBPGrpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1)
)
tmnxBPGrpAssocEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBPGrpAssocEntry.setStatus("current")
_TmnxBPGrpAssocWorkingBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocWorkingBundleID_Object = MibTableColumn
tmnxBPGrpAssocWorkingBundleID = _TmnxBPGrpAssocWorkingBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 1),
    _TmnxBPGrpAssocWorkingBundleID_Type()
)
tmnxBPGrpAssocWorkingBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocWorkingBundleID.setStatus("current")
_TmnxBPGrpAssocProtectBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocProtectBundleID_Object = MibTableColumn
tmnxBPGrpAssocProtectBundleID = _TmnxBPGrpAssocProtectBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 2),
    _TmnxBPGrpAssocProtectBundleID_Type()
)
tmnxBPGrpAssocProtectBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocProtectBundleID.setStatus("current")
_TmnxBPGrpAssocActiveBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocActiveBundleID_Object = MibTableColumn
tmnxBPGrpAssocActiveBundleID = _TmnxBPGrpAssocActiveBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 3),
    _TmnxBPGrpAssocActiveBundleID_Type()
)
tmnxBPGrpAssocActiveBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocActiveBundleID.setStatus("current")
_TmnxBundleMlpppTable_Object = MibTable
tmnxBundleMlpppTable = _TmnxBundleMlpppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26)
)
if mibBuilder.loadTexts:
    tmnxBundleMlpppTable.setStatus("current")
_TmnxBundleMlpppEntry_Object = MibTableRow
tmnxBundleMlpppEntry = _TmnxBundleMlpppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1)
)
tmnxBundleMlpppEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMlpppEntry.setStatus("current")


class _TmnxBundleMlpppEndpointID_Type(OctetString):
    """Custom type tmnxBundleMlpppEndpointID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxBundleMlpppEndpointID_Type.__name__ = "OctetString"
_TmnxBundleMlpppEndpointID_Object = MibTableColumn
tmnxBundleMlpppEndpointID = _TmnxBundleMlpppEndpointID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 1),
    _TmnxBundleMlpppEndpointID_Type()
)
tmnxBundleMlpppEndpointID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEndpointID.setStatus("current")
_TmnxBundleMlpppEndpointIDClass_Type = TmnxMlpppEndpointIdClass
_TmnxBundleMlpppEndpointIDClass_Object = MibTableColumn
tmnxBundleMlpppEndpointIDClass = _TmnxBundleMlpppEndpointIDClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 2),
    _TmnxBundleMlpppEndpointIDClass_Type()
)
tmnxBundleMlpppEndpointIDClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEndpointIDClass.setStatus("current")


class _TmnxBundleMlpppClassCount_Type(Integer32):
    """Custom type tmnxBundleMlpppClassCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxBundleMlpppClassCount_Type.__name__ = "Integer32"
_TmnxBundleMlpppClassCount_Object = MibTableColumn
tmnxBundleMlpppClassCount = _TmnxBundleMlpppClassCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 3),
    _TmnxBundleMlpppClassCount_Type()
)
tmnxBundleMlpppClassCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppClassCount.setStatus("current")


class _TmnxBundleMlpppIngQoSProfId_Type(TMlpppQoSProfileId):
    """Custom type tmnxBundleMlpppIngQoSProfId based on TMlpppQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlpppIngQoSProfId_Object = MibTableColumn
tmnxBundleMlpppIngQoSProfId = _TmnxBundleMlpppIngQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 4),
    _TmnxBundleMlpppIngQoSProfId_Type()
)
tmnxBundleMlpppIngQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppIngQoSProfId.setStatus("current")


class _TmnxBundleMlpppEgrQoSProfId_Type(TMlpppQoSProfileId):
    """Custom type tmnxBundleMlpppEgrQoSProfId based on TMlpppQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlpppEgrQoSProfId_Object = MibTableColumn
tmnxBundleMlpppEgrQoSProfId = _TmnxBundleMlpppEgrQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 5),
    _TmnxBundleMlpppEgrQoSProfId_Type()
)
tmnxBundleMlpppEgrQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEgrQoSProfId.setStatus("current")
_TmnxDigitalDiagMonitorTable_Object = MibTable
tmnxDigitalDiagMonitorTable = _TmnxDigitalDiagMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31)
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorTable.setStatus("current")
_TmnxDigitalDiagMonitorEntry_Object = MibTableRow
tmnxDigitalDiagMonitorEntry = _TmnxDigitalDiagMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1)
)
tmnxDigitalDiagMonitorEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorEntry.setStatus("current")
_TmnxDDMTemperature_Type = Integer32
_TmnxDDMTemperature_Object = MibTableColumn
tmnxDDMTemperature = _TmnxDDMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 1),
    _TmnxDDMTemperature_Type()
)
tmnxDDMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTemperature.setStatus("current")
_TmnxDDMTempLowWarning_Type = Integer32
_TmnxDDMTempLowWarning_Object = MibTableColumn
tmnxDDMTempLowWarning = _TmnxDDMTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 2),
    _TmnxDDMTempLowWarning_Type()
)
tmnxDDMTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempLowWarning.setStatus("current")
_TmnxDDMTempLowAlarm_Type = Integer32
_TmnxDDMTempLowAlarm_Object = MibTableColumn
tmnxDDMTempLowAlarm = _TmnxDDMTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 3),
    _TmnxDDMTempLowAlarm_Type()
)
tmnxDDMTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempLowAlarm.setStatus("current")
_TmnxDDMTempHiWarning_Type = Integer32
_TmnxDDMTempHiWarning_Object = MibTableColumn
tmnxDDMTempHiWarning = _TmnxDDMTempHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 4),
    _TmnxDDMTempHiWarning_Type()
)
tmnxDDMTempHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempHiWarning.setStatus("current")
_TmnxDDMTempHiAlarm_Type = Integer32
_TmnxDDMTempHiAlarm_Object = MibTableColumn
tmnxDDMTempHiAlarm = _TmnxDDMTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 5),
    _TmnxDDMTempHiAlarm_Type()
)
tmnxDDMTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempHiAlarm.setStatus("current")
_TmnxDDMSupplyVoltage_Type = Integer32
_TmnxDDMSupplyVoltage_Object = MibTableColumn
tmnxDDMSupplyVoltage = _TmnxDDMSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 6),
    _TmnxDDMSupplyVoltage_Type()
)
tmnxDDMSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltage.setStatus("current")
_TmnxDDMSupplyVoltageLowWarning_Type = Integer32
_TmnxDDMSupplyVoltageLowWarning_Object = MibTableColumn
tmnxDDMSupplyVoltageLowWarning = _TmnxDDMSupplyVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 7),
    _TmnxDDMSupplyVoltageLowWarning_Type()
)
tmnxDDMSupplyVoltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageLowWarning.setStatus("current")
_TmnxDDMSupplyVoltageLowAlarm_Type = Integer32
_TmnxDDMSupplyVoltageLowAlarm_Object = MibTableColumn
tmnxDDMSupplyVoltageLowAlarm = _TmnxDDMSupplyVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 8),
    _TmnxDDMSupplyVoltageLowAlarm_Type()
)
tmnxDDMSupplyVoltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageLowAlarm.setStatus("current")
_TmnxDDMSupplyVoltageHiWarning_Type = Integer32
_TmnxDDMSupplyVoltageHiWarning_Object = MibTableColumn
tmnxDDMSupplyVoltageHiWarning = _TmnxDDMSupplyVoltageHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 9),
    _TmnxDDMSupplyVoltageHiWarning_Type()
)
tmnxDDMSupplyVoltageHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageHiWarning.setStatus("current")
_TmnxDDMSupplyVoltageHiAlarm_Type = Integer32
_TmnxDDMSupplyVoltageHiAlarm_Object = MibTableColumn
tmnxDDMSupplyVoltageHiAlarm = _TmnxDDMSupplyVoltageHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 10),
    _TmnxDDMSupplyVoltageHiAlarm_Type()
)
tmnxDDMSupplyVoltageHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageHiAlarm.setStatus("current")
_TmnxDDMTxBiasCurrent_Type = Integer32
_TmnxDDMTxBiasCurrent_Object = MibTableColumn
tmnxDDMTxBiasCurrent = _TmnxDDMTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 11),
    _TmnxDDMTxBiasCurrent_Type()
)
tmnxDDMTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrent.setStatus("current")
_TmnxDDMTxBiasCurrentLowWarning_Type = Integer32
_TmnxDDMTxBiasCurrentLowWarning_Object = MibTableColumn
tmnxDDMTxBiasCurrentLowWarning = _TmnxDDMTxBiasCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 12),
    _TmnxDDMTxBiasCurrentLowWarning_Type()
)
tmnxDDMTxBiasCurrentLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentLowWarning.setStatus("current")
_TmnxDDMTxBiasCurrentLowAlarm_Type = Integer32
_TmnxDDMTxBiasCurrentLowAlarm_Object = MibTableColumn
tmnxDDMTxBiasCurrentLowAlarm = _TmnxDDMTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 13),
    _TmnxDDMTxBiasCurrentLowAlarm_Type()
)
tmnxDDMTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentLowAlarm.setStatus("current")
_TmnxDDMTxBiasCurrentHiWarning_Type = Integer32
_TmnxDDMTxBiasCurrentHiWarning_Object = MibTableColumn
tmnxDDMTxBiasCurrentHiWarning = _TmnxDDMTxBiasCurrentHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 14),
    _TmnxDDMTxBiasCurrentHiWarning_Type()
)
tmnxDDMTxBiasCurrentHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentHiWarning.setStatus("current")
_TmnxDDMTxBiasCurrentHiAlarm_Type = Integer32
_TmnxDDMTxBiasCurrentHiAlarm_Object = MibTableColumn
tmnxDDMTxBiasCurrentHiAlarm = _TmnxDDMTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 15),
    _TmnxDDMTxBiasCurrentHiAlarm_Type()
)
tmnxDDMTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentHiAlarm.setStatus("current")
_TmnxDDMTxOutputPower_Type = Integer32
_TmnxDDMTxOutputPower_Object = MibTableColumn
tmnxDDMTxOutputPower = _TmnxDDMTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 16),
    _TmnxDDMTxOutputPower_Type()
)
tmnxDDMTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPower.setStatus("current")
_TmnxDDMTxOutputPowerLowWarning_Type = Integer32
_TmnxDDMTxOutputPowerLowWarning_Object = MibTableColumn
tmnxDDMTxOutputPowerLowWarning = _TmnxDDMTxOutputPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 17),
    _TmnxDDMTxOutputPowerLowWarning_Type()
)
tmnxDDMTxOutputPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerLowWarning.setStatus("current")
_TmnxDDMTxOutputPowerLowAlarm_Type = Integer32
_TmnxDDMTxOutputPowerLowAlarm_Object = MibTableColumn
tmnxDDMTxOutputPowerLowAlarm = _TmnxDDMTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 18),
    _TmnxDDMTxOutputPowerLowAlarm_Type()
)
tmnxDDMTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerLowAlarm.setStatus("current")
_TmnxDDMTxOutputPowerHiWarning_Type = Integer32
_TmnxDDMTxOutputPowerHiWarning_Object = MibTableColumn
tmnxDDMTxOutputPowerHiWarning = _TmnxDDMTxOutputPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 19),
    _TmnxDDMTxOutputPowerHiWarning_Type()
)
tmnxDDMTxOutputPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerHiWarning.setStatus("current")
_TmnxDDMTxOutputPowerHiAlarm_Type = Integer32
_TmnxDDMTxOutputPowerHiAlarm_Object = MibTableColumn
tmnxDDMTxOutputPowerHiAlarm = _TmnxDDMTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 20),
    _TmnxDDMTxOutputPowerHiAlarm_Type()
)
tmnxDDMTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerHiAlarm.setStatus("current")
_TmnxDDMRxOpticalPower_Type = Integer32
_TmnxDDMRxOpticalPower_Object = MibTableColumn
tmnxDDMRxOpticalPower = _TmnxDDMRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 21),
    _TmnxDDMRxOpticalPower_Type()
)
tmnxDDMRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPower.setStatus("current")
_TmnxDDMRxOpticalPowerLowWarning_Type = Integer32
_TmnxDDMRxOpticalPowerLowWarning_Object = MibTableColumn
tmnxDDMRxOpticalPowerLowWarning = _TmnxDDMRxOpticalPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 22),
    _TmnxDDMRxOpticalPowerLowWarning_Type()
)
tmnxDDMRxOpticalPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerLowWarning.setStatus("current")
_TmnxDDMRxOpticalPowerLowAlarm_Type = Integer32
_TmnxDDMRxOpticalPowerLowAlarm_Object = MibTableColumn
tmnxDDMRxOpticalPowerLowAlarm = _TmnxDDMRxOpticalPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 23),
    _TmnxDDMRxOpticalPowerLowAlarm_Type()
)
tmnxDDMRxOpticalPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerLowAlarm.setStatus("current")
_TmnxDDMRxOpticalPowerHiWarning_Type = Integer32
_TmnxDDMRxOpticalPowerHiWarning_Object = MibTableColumn
tmnxDDMRxOpticalPowerHiWarning = _TmnxDDMRxOpticalPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 24),
    _TmnxDDMRxOpticalPowerHiWarning_Type()
)
tmnxDDMRxOpticalPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerHiWarning.setStatus("current")
_TmnxDDMRxOpticalPowerHiAlarm_Type = Integer32
_TmnxDDMRxOpticalPowerHiAlarm_Object = MibTableColumn
tmnxDDMRxOpticalPowerHiAlarm = _TmnxDDMRxOpticalPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 25),
    _TmnxDDMRxOpticalPowerHiAlarm_Type()
)
tmnxDDMRxOpticalPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerHiAlarm.setStatus("current")


class _TmnxDDMRxOpticalPowerType_Type(Integer32):
    """Custom type tmnxDDMRxOpticalPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("oma", 0))
    )


_TmnxDDMRxOpticalPowerType_Type.__name__ = "Integer32"
_TmnxDDMRxOpticalPowerType_Object = MibTableColumn
tmnxDDMRxOpticalPowerType = _TmnxDDMRxOpticalPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 26),
    _TmnxDDMRxOpticalPowerType_Type()
)
tmnxDDMRxOpticalPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerType.setStatus("current")
_TmnxDDMAux1_Type = Integer32
_TmnxDDMAux1_Object = MibTableColumn
tmnxDDMAux1 = _TmnxDDMAux1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 27),
    _TmnxDDMAux1_Type()
)
tmnxDDMAux1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1.setStatus("current")
_TmnxDDMAux1LowWarning_Type = Integer32
_TmnxDDMAux1LowWarning_Object = MibTableColumn
tmnxDDMAux1LowWarning = _TmnxDDMAux1LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 28),
    _TmnxDDMAux1LowWarning_Type()
)
tmnxDDMAux1LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1LowWarning.setStatus("current")
_TmnxDDMAux1LowAlarm_Type = Integer32
_TmnxDDMAux1LowAlarm_Object = MibTableColumn
tmnxDDMAux1LowAlarm = _TmnxDDMAux1LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 29),
    _TmnxDDMAux1LowAlarm_Type()
)
tmnxDDMAux1LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1LowAlarm.setStatus("current")
_TmnxDDMAux1HiWarning_Type = Integer32
_TmnxDDMAux1HiWarning_Object = MibTableColumn
tmnxDDMAux1HiWarning = _TmnxDDMAux1HiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 30),
    _TmnxDDMAux1HiWarning_Type()
)
tmnxDDMAux1HiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1HiWarning.setStatus("current")
_TmnxDDMAux1HiAlarm_Type = Integer32
_TmnxDDMAux1HiAlarm_Object = MibTableColumn
tmnxDDMAux1HiAlarm = _TmnxDDMAux1HiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 31),
    _TmnxDDMAux1HiAlarm_Type()
)
tmnxDDMAux1HiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1HiAlarm.setStatus("current")


class _TmnxDDMAux1Type_Type(Integer32):
    """Custom type tmnxDDMAux1Type based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("adp-bias-voltage", 1),
          ("current-18", 14),
          ("current-33", 13),
          ("current-50", 10),
          ("current-52", 15),
          ("laser-temp", 4),
          ("laser-wavelength", 5),
          ("none", 0),
          ("reserved-11", 11),
          ("reserved-12", 12),
          ("reserved-2", 2),
          ("tec-current", 3),
          ("voltage-18", 8),
          ("voltage-33", 7),
          ("voltage-50", 6),
          ("voltage-52", 9))
    )


_TmnxDDMAux1Type_Type.__name__ = "Integer32"
_TmnxDDMAux1Type_Object = MibTableColumn
tmnxDDMAux1Type = _TmnxDDMAux1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 32),
    _TmnxDDMAux1Type_Type()
)
tmnxDDMAux1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1Type.setStatus("current")
_TmnxDDMAux2_Type = Integer32
_TmnxDDMAux2_Object = MibTableColumn
tmnxDDMAux2 = _TmnxDDMAux2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 33),
    _TmnxDDMAux2_Type()
)
tmnxDDMAux2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2.setStatus("current")
_TmnxDDMAux2LowWarning_Type = Integer32
_TmnxDDMAux2LowWarning_Object = MibTableColumn
tmnxDDMAux2LowWarning = _TmnxDDMAux2LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 34),
    _TmnxDDMAux2LowWarning_Type()
)
tmnxDDMAux2LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2LowWarning.setStatus("current")
_TmnxDDMAux2LowAlarm_Type = Integer32
_TmnxDDMAux2LowAlarm_Object = MibTableColumn
tmnxDDMAux2LowAlarm = _TmnxDDMAux2LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 35),
    _TmnxDDMAux2LowAlarm_Type()
)
tmnxDDMAux2LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2LowAlarm.setStatus("current")
_TmnxDDMAux2HiWarning_Type = Integer32
_TmnxDDMAux2HiWarning_Object = MibTableColumn
tmnxDDMAux2HiWarning = _TmnxDDMAux2HiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 36),
    _TmnxDDMAux2HiWarning_Type()
)
tmnxDDMAux2HiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2HiWarning.setStatus("current")
_TmnxDDMAux2HiAlarm_Type = Integer32
_TmnxDDMAux2HiAlarm_Object = MibTableColumn
tmnxDDMAux2HiAlarm = _TmnxDDMAux2HiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 37),
    _TmnxDDMAux2HiAlarm_Type()
)
tmnxDDMAux2HiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2HiAlarm.setStatus("current")


class _TmnxDDMAux2Type_Type(Integer32):
    """Custom type tmnxDDMAux2Type based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("adp-bias-voltage", 1),
          ("current-18", 14),
          ("current-33", 13),
          ("current-50", 10),
          ("current-52", 15),
          ("laser-temp", 4),
          ("laser-wavelength", 5),
          ("none", 0),
          ("reserved-11", 11),
          ("reserved-12", 12),
          ("reserved-2", 2),
          ("tec-current", 3),
          ("voltage-18", 8),
          ("voltage-33", 7),
          ("voltage-50", 6),
          ("voltage-52", 9))
    )


_TmnxDDMAux2Type_Type.__name__ = "Integer32"
_TmnxDDMAux2Type_Object = MibTableColumn
tmnxDDMAux2Type = _TmnxDDMAux2Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 38),
    _TmnxDDMAux2Type_Type()
)
tmnxDDMAux2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2Type.setStatus("current")


class _TmnxDDMFailedThresholds_Type(Bits):
    """Custom type tmnxDDMFailedThresholds based on Bits"""
    namedValues = NamedValues(
        *(("aux1-high-alarm", 24),
          ("aux1-high-warning", 23),
          ("aux1-low-alarm", 22),
          ("aux1-low-warning", 21),
          ("aux2-high-alarm", 28),
          ("aux2-high-warning", 27),
          ("aux2-low-alarm", 26),
          ("aux2-low-warning", 25),
          ("rxOpticalPower-high-alarm", 20),
          ("rxOpticalPower-high-warning", 19),
          ("rxOpticalPower-low-alarm", 18),
          ("rxOpticalPower-low-warning", 17),
          ("supplyVoltage-high-alarm", 8),
          ("supplyVoltage-high-warning", 7),
          ("supplyVoltage-low-alarm", 6),
          ("supplyVoltage-low-warning", 5),
          ("temperature-high-alarm", 4),
          ("temperature-high-warning", 3),
          ("temperature-low-alarm", 2),
          ("temperature-low-warning", 1),
          ("txBiasCurrent-high-alarm", 12),
          ("txBiasCurrent-high-warning", 11),
          ("txBiasCurrent-low-alarm", 10),
          ("txBiasCurrent-low-warning", 9),
          ("txOutputPower-high-alarm", 16),
          ("txOutputPower-high-warning", 15),
          ("txOutputPower-low-alarm", 14),
          ("txOutputPower-low-warning", 13),
          ("unknown", 0))
    )

_TmnxDDMFailedThresholds_Type.__name__ = "Bits"
_TmnxDDMFailedThresholds_Object = MibTableColumn
tmnxDDMFailedThresholds = _TmnxDDMFailedThresholds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 39),
    _TmnxDDMFailedThresholds_Type()
)
tmnxDDMFailedThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMFailedThresholds.setStatus("current")
_TmnxDDMExternallyCalibrated_Type = TruthValue
_TmnxDDMExternallyCalibrated_Object = MibTableColumn
tmnxDDMExternallyCalibrated = _TmnxDDMExternallyCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 40),
    _TmnxDDMExternallyCalibrated_Type()
)
tmnxDDMExternallyCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExternallyCalibrated.setStatus("current")
_TmnxDDMExtCalRxPower4_Type = Unsigned32
_TmnxDDMExtCalRxPower4_Object = MibTableColumn
tmnxDDMExtCalRxPower4 = _TmnxDDMExtCalRxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 41),
    _TmnxDDMExtCalRxPower4_Type()
)
tmnxDDMExtCalRxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower4.setStatus("current")
_TmnxDDMExtCalRxPower3_Type = Unsigned32
_TmnxDDMExtCalRxPower3_Object = MibTableColumn
tmnxDDMExtCalRxPower3 = _TmnxDDMExtCalRxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 42),
    _TmnxDDMExtCalRxPower3_Type()
)
tmnxDDMExtCalRxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower3.setStatus("current")
_TmnxDDMExtCalRxPower2_Type = Unsigned32
_TmnxDDMExtCalRxPower2_Object = MibTableColumn
tmnxDDMExtCalRxPower2 = _TmnxDDMExtCalRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 43),
    _TmnxDDMExtCalRxPower2_Type()
)
tmnxDDMExtCalRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower2.setStatus("current")
_TmnxDDMExtCalRxPower1_Type = Unsigned32
_TmnxDDMExtCalRxPower1_Object = MibTableColumn
tmnxDDMExtCalRxPower1 = _TmnxDDMExtCalRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 44),
    _TmnxDDMExtCalRxPower1_Type()
)
tmnxDDMExtCalRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower1.setStatus("current")
_TmnxDDMExtCalRxPower0_Type = Unsigned32
_TmnxDDMExtCalRxPower0_Object = MibTableColumn
tmnxDDMExtCalRxPower0 = _TmnxDDMExtCalRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 45),
    _TmnxDDMExtCalRxPower0_Type()
)
tmnxDDMExtCalRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower0.setStatus("current")


class _TmnxDDMExtCalTxLaserBiasSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTxLaserBiasSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTxLaserBiasSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTxLaserBiasSlope_Object = MibTableColumn
tmnxDDMExtCalTxLaserBiasSlope = _TmnxDDMExtCalTxLaserBiasSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 46),
    _TmnxDDMExtCalTxLaserBiasSlope_Type()
)
tmnxDDMExtCalTxLaserBiasSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxLaserBiasSlope.setStatus("current")


class _TmnxDDMExtCalTxLaserBiasOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTxLaserBiasOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTxLaserBiasOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTxLaserBiasOffset_Object = MibTableColumn
tmnxDDMExtCalTxLaserBiasOffset = _TmnxDDMExtCalTxLaserBiasOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 47),
    _TmnxDDMExtCalTxLaserBiasOffset_Type()
)
tmnxDDMExtCalTxLaserBiasOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxLaserBiasOffset.setStatus("current")


class _TmnxDDMExtCalTxPowerSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTxPowerSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTxPowerSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTxPowerSlope_Object = MibTableColumn
tmnxDDMExtCalTxPowerSlope = _TmnxDDMExtCalTxPowerSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 48),
    _TmnxDDMExtCalTxPowerSlope_Type()
)
tmnxDDMExtCalTxPowerSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxPowerSlope.setStatus("current")


class _TmnxDDMExtCalTxPowerOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTxPowerOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTxPowerOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTxPowerOffset_Object = MibTableColumn
tmnxDDMExtCalTxPowerOffset = _TmnxDDMExtCalTxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 49),
    _TmnxDDMExtCalTxPowerOffset_Type()
)
tmnxDDMExtCalTxPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxPowerOffset.setStatus("current")


class _TmnxDDMExtCalTemperatureSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTemperatureSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTemperatureSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTemperatureSlope_Object = MibTableColumn
tmnxDDMExtCalTemperatureSlope = _TmnxDDMExtCalTemperatureSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 50),
    _TmnxDDMExtCalTemperatureSlope_Type()
)
tmnxDDMExtCalTemperatureSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTemperatureSlope.setStatus("current")


class _TmnxDDMExtCalTemperatureOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTemperatureOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTemperatureOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTemperatureOffset_Object = MibTableColumn
tmnxDDMExtCalTemperatureOffset = _TmnxDDMExtCalTemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 51),
    _TmnxDDMExtCalTemperatureOffset_Type()
)
tmnxDDMExtCalTemperatureOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTemperatureOffset.setStatus("current")


class _TmnxDDMExtCalVoltageSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalVoltageSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalVoltageSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalVoltageSlope_Object = MibTableColumn
tmnxDDMExtCalVoltageSlope = _TmnxDDMExtCalVoltageSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 52),
    _TmnxDDMExtCalVoltageSlope_Type()
)
tmnxDDMExtCalVoltageSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalVoltageSlope.setStatus("current")


class _TmnxDDMExtCalVoltageOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalVoltageOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalVoltageOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalVoltageOffset_Object = MibTableColumn
tmnxDDMExtCalVoltageOffset = _TmnxDDMExtCalVoltageOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 53),
    _TmnxDDMExtCalVoltageOffset_Type()
)
tmnxDDMExtCalVoltageOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalVoltageOffset.setStatus("current")
_TmnxPortNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxPortNotificationObjects = _TmnxPortNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7)
)
_TmnxPortNotifyPortId_Type = TmnxPortID
_TmnxPortNotifyPortId_Object = MibScalar
tmnxPortNotifyPortId = _TmnxPortNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 1),
    _TmnxPortNotifyPortId_Type()
)
tmnxPortNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyPortId.setStatus("current")


class _TmnxPortNotifySonetAlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifySonetAlarmReason based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )


_TmnxPortNotifySonetAlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifySonetAlarmReason_Object = MibScalar
tmnxPortNotifySonetAlarmReason = _TmnxPortNotifySonetAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 2),
    _TmnxPortNotifySonetAlarmReason_Type()
)
tmnxPortNotifySonetAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifySonetAlarmReason.setStatus("current")


class _TmnxPortNotifySonetPathAlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifySonetPathAlarmReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )


_TmnxPortNotifySonetPathAlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifySonetPathAlarmReason_Object = MibScalar
tmnxPortNotifySonetPathAlarmReason = _TmnxPortNotifySonetPathAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 3),
    _TmnxPortNotifySonetPathAlarmReason_Type()
)
tmnxPortNotifySonetPathAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifySonetPathAlarmReason.setStatus("current")


class _TmnxPortNotifyError_Type(Integer32):
    """Custom type tmnxPortNotifyError based on Integer32"""
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
        *(("laserError", 4),
          ("miscError", 5),
          ("rxClockError", 2),
          ("txClockError", 1),
          ("txFifoError", 3))
    )


_TmnxPortNotifyError_Type.__name__ = "Integer32"
_TmnxPortNotifyError_Object = MibScalar
tmnxPortNotifyError = _TmnxPortNotifyError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 4),
    _TmnxPortNotifyError_Type()
)
tmnxPortNotifyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyError.setStatus("current")


class _TmnxPortNotifyDS3AlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifyDS3AlarmReason based on Integer32"""
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
        *(("ais", 1),
          ("looped", 5),
          ("los", 2),
          ("notUsed", 0),
          ("oof", 3),
          ("rai", 4))
    )


_TmnxPortNotifyDS3AlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifyDS3AlarmReason_Object = MibScalar
tmnxPortNotifyDS3AlarmReason = _TmnxPortNotifyDS3AlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 5),
    _TmnxPortNotifyDS3AlarmReason_Type()
)
tmnxPortNotifyDS3AlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyDS3AlarmReason.setStatus("current")


class _TmnxPortNotifyDS1AlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifyDS1AlarmReason based on Integer32"""
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
        *(("ais", 1),
          ("berSd", 6),
          ("berSf", 7),
          ("looped", 5),
          ("los", 2),
          ("notUsed", 0),
          ("oof", 3),
          ("rai", 4))
    )


_TmnxPortNotifyDS1AlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifyDS1AlarmReason_Object = MibScalar
tmnxPortNotifyDS1AlarmReason = _TmnxPortNotifyDS1AlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 6),
    _TmnxPortNotifyDS1AlarmReason_Type()
)
tmnxPortNotifyDS1AlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyDS1AlarmReason.setStatus("current")
_TmnxPortNotifyBundleId_Type = TmnxBundleID
_TmnxPortNotifyBundleId_Object = MibScalar
tmnxPortNotifyBundleId = _TmnxPortNotifyBundleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 7),
    _TmnxPortNotifyBundleId_Type()
)
tmnxPortNotifyBundleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyBundleId.setStatus("current")
_TmnxPortNotifyEtherAlarmReason_Type = TmnxPortEtherReportValue
_TmnxPortNotifyEtherAlarmReason_Object = MibScalar
tmnxPortNotifyEtherAlarmReason = _TmnxPortNotifyEtherAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 8),
    _TmnxPortNotifyEtherAlarmReason_Type()
)
tmnxPortNotifyEtherAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyEtherAlarmReason.setStatus("current")


class _TmnxDDMFailedObject_Type(Integer32):
    """Custom type tmnxDDMFailedObject based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("aux1-high-alarm", 24),
          ("aux1-high-warning", 23),
          ("aux1-low-alarm", 22),
          ("aux1-low-warning", 21),
          ("aux2-high-alarm", 28),
          ("aux2-high-warning", 27),
          ("aux2-low-alarm", 26),
          ("aux2-low-warning", 25),
          ("rxOpticalPower-high-alarm", 20),
          ("rxOpticalPower-high-warning", 19),
          ("rxOpticalPower-low-alarm", 18),
          ("rxOpticalPower-low-warning", 17),
          ("supplyVoltage-high-alarm", 8),
          ("supplyVoltage-high-warning", 7),
          ("supplyVoltage-low-alarm", 6),
          ("supplyVoltage-low-warning", 5),
          ("temperature-high-alarm", 4),
          ("temperature-high-warning", 3),
          ("temperature-low-alarm", 2),
          ("temperature-low-warning", 1),
          ("txBiasCurrent-high-alarm", 12),
          ("txBiasCurrent-high-warning", 11),
          ("txBiasCurrent-low-alarm", 10),
          ("txBiasCurrent-low-warning", 9),
          ("txOutputPower-high-alarm", 16),
          ("txOutputPower-high-warning", 15),
          ("txOutputPower-low-alarm", 14),
          ("txOutputPower-low-warning", 13),
          ("unknown", 0))
    )


_TmnxDDMFailedObject_Type.__name__ = "Integer32"
_TmnxDDMFailedObject_Object = MibScalar
tmnxDDMFailedObject = _TmnxDDMFailedObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 9),
    _TmnxDDMFailedObject_Type()
)
tmnxDDMFailedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDDMFailedObject.setStatus("current")
_TmnxFRObjs_ObjectIdentity = ObjectIdentity
tmnxFRObjs = _TmnxFRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9)
)
_TmnxFRDlcmiTable_Object = MibTable
tmnxFRDlcmiTable = _TmnxFRDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxFRDlcmiTable.setStatus("current")
_TmnxFRDlcmiEntry_Object = MibTableRow
tmnxFRDlcmiEntry = _TmnxFRDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1)
)
tmnxFRDlcmiEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxFRDlcmiEntry.setStatus("current")


class _TmnxFRDlcmiMode_Type(Integer32):
    """Custom type tmnxFRDlcmiMode based on Integer32"""
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
        *(("bidir", 3),
          ("dce", 2),
          ("dte", 1))
    )


_TmnxFRDlcmiMode_Type.__name__ = "Integer32"
_TmnxFRDlcmiMode_Object = MibTableColumn
tmnxFRDlcmiMode = _TmnxFRDlcmiMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 1),
    _TmnxFRDlcmiMode_Type()
)
tmnxFRDlcmiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiMode.setStatus("current")


class _TmnxFRDlcmiN392Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiN392Dce based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxFRDlcmiN392Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiN392Dce_Object = MibTableColumn
tmnxFRDlcmiN392Dce = _TmnxFRDlcmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 2),
    _TmnxFRDlcmiN392Dce_Type()
)
tmnxFRDlcmiN392Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiN392Dce.setStatus("current")


class _TmnxFRDlcmiN393Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiN393Dce based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxFRDlcmiN393Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiN393Dce_Object = MibTableColumn
tmnxFRDlcmiN393Dce = _TmnxFRDlcmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 3),
    _TmnxFRDlcmiN393Dce_Type()
)
tmnxFRDlcmiN393Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiN393Dce.setStatus("current")


class _TmnxFRDlcmiT392Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiT392Dce based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TmnxFRDlcmiT392Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiT392Dce_Object = MibTableColumn
tmnxFRDlcmiT392Dce = _TmnxFRDlcmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 4),
    _TmnxFRDlcmiT392Dce_Type()
)
tmnxFRDlcmiT392Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiT392Dce.setUnits("seconds")
_TmnxFRDlcmiTxStatusEnqMsgs_Type = Counter32
_TmnxFRDlcmiTxStatusEnqMsgs_Object = MibTableColumn
tmnxFRDlcmiTxStatusEnqMsgs = _TmnxFRDlcmiTxStatusEnqMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 5),
    _TmnxFRDlcmiTxStatusEnqMsgs_Type()
)
tmnxFRDlcmiTxStatusEnqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusEnqMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusEnqMsgs.setUnits("messages")
_TmnxFRDlcmiRxStatusEnqMsgs_Type = Counter32
_TmnxFRDlcmiRxStatusEnqMsgs_Object = MibTableColumn
tmnxFRDlcmiRxStatusEnqMsgs = _TmnxFRDlcmiRxStatusEnqMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 6),
    _TmnxFRDlcmiRxStatusEnqMsgs_Type()
)
tmnxFRDlcmiRxStatusEnqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusEnqMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusEnqMsgs.setUnits("messages")
_TmnxFRDlcmiStatusEnqMsgTimeouts_Type = Counter32
_TmnxFRDlcmiStatusEnqMsgTimeouts_Object = MibTableColumn
tmnxFRDlcmiStatusEnqMsgTimeouts = _TmnxFRDlcmiStatusEnqMsgTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 7),
    _TmnxFRDlcmiStatusEnqMsgTimeouts_Type()
)
tmnxFRDlcmiStatusEnqMsgTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusEnqMsgTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusEnqMsgTimeouts.setUnits("messages")
_TmnxFRDlcmiTxStatusMsgs_Type = Counter32
_TmnxFRDlcmiTxStatusMsgs_Object = MibTableColumn
tmnxFRDlcmiTxStatusMsgs = _TmnxFRDlcmiTxStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 8),
    _TmnxFRDlcmiTxStatusMsgs_Type()
)
tmnxFRDlcmiTxStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusMsgs.setUnits("messages")
_TmnxFRDlcmiRxStatusMsgs_Type = Counter32
_TmnxFRDlcmiRxStatusMsgs_Object = MibTableColumn
tmnxFRDlcmiRxStatusMsgs = _TmnxFRDlcmiRxStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 9),
    _TmnxFRDlcmiRxStatusMsgs_Type()
)
tmnxFRDlcmiRxStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusMsgs.setUnits("messages")
_TmnxFRDlcmiStatusMsgTimeouts_Type = Counter32
_TmnxFRDlcmiStatusMsgTimeouts_Object = MibTableColumn
tmnxFRDlcmiStatusMsgTimeouts = _TmnxFRDlcmiStatusMsgTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 10),
    _TmnxFRDlcmiStatusMsgTimeouts_Type()
)
tmnxFRDlcmiStatusMsgTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusMsgTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusMsgTimeouts.setUnits("messages")
_TmnxFRDlcmiDiscardedMsgs_Type = Counter32
_TmnxFRDlcmiDiscardedMsgs_Object = MibTableColumn
tmnxFRDlcmiDiscardedMsgs = _TmnxFRDlcmiDiscardedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 11),
    _TmnxFRDlcmiDiscardedMsgs_Type()
)
tmnxFRDlcmiDiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiDiscardedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiDiscardedMsgs.setUnits("messages")
_TmnxFRDlcmiInvRxSeqNumMsgs_Type = Counter32
_TmnxFRDlcmiInvRxSeqNumMsgs_Object = MibTableColumn
tmnxFRDlcmiInvRxSeqNumMsgs = _TmnxFRDlcmiInvRxSeqNumMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 12),
    _TmnxFRDlcmiInvRxSeqNumMsgs_Type()
)
tmnxFRDlcmiInvRxSeqNumMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiInvRxSeqNumMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiInvRxSeqNumMsgs.setUnits("messages")
_TmnxQosAppObjs_ObjectIdentity = ObjectIdentity
tmnxQosAppObjs = _TmnxQosAppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10)
)
_TmnxQosPoolAppTable_Object = MibTable
tmnxQosPoolAppTable = _TmnxQosPoolAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    tmnxQosPoolAppTable.setStatus("current")
_TmnxQosPoolAppEntry_Object = MibTableRow
tmnxQosPoolAppEntry = _TmnxQosPoolAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1)
)
tmnxQosPoolAppEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectType"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectId"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppType"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppPool"),
)
if mibBuilder.loadTexts:
    tmnxQosPoolAppEntry.setStatus("current")


class _TmnxObjectType_Type(Integer32):
    """Custom type tmnxObjectType based on Integer32"""
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
        *(("bundle", 4),
          ("channel", 3),
          ("mda", 1),
          ("port", 2))
    )


_TmnxObjectType_Type.__name__ = "Integer32"
_TmnxObjectType_Object = MibTableColumn
tmnxObjectType = _TmnxObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 1),
    _TmnxObjectType_Type()
)
tmnxObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectType.setStatus("current")
_TmnxObjectId_Type = TmnxPortID
_TmnxObjectId_Object = MibTableColumn
tmnxObjectId = _TmnxObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 2),
    _TmnxObjectId_Type()
)
tmnxObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectId.setStatus("current")


class _TmnxObjectAppType_Type(Integer32):
    """Custom type tmnxObjectAppType based on Integer32"""
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
        *(("accessEgress", 2),
          ("accessIngress", 1),
          ("networkEgress", 4),
          ("networkIngress", 3))
    )


_TmnxObjectAppType_Type.__name__ = "Integer32"
_TmnxObjectAppType_Object = MibTableColumn
tmnxObjectAppType = _TmnxObjectAppType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 3),
    _TmnxObjectAppType_Type()
)
tmnxObjectAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectAppType.setStatus("current")
_TmnxObjectAppPool_Type = TNamedItem
_TmnxObjectAppPool_Object = MibTableColumn
tmnxObjectAppPool = _TmnxObjectAppPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 4),
    _TmnxObjectAppPool_Type()
)
tmnxObjectAppPool.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectAppPool.setStatus("current")
_TmnxObjectAppPoolRowStatus_Type = RowStatus
_TmnxObjectAppPoolRowStatus_Object = MibTableColumn
tmnxObjectAppPoolRowStatus = _TmnxObjectAppPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 5),
    _TmnxObjectAppPoolRowStatus_Type()
)
tmnxObjectAppPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxObjectAppPoolRowStatus.setStatus("current")


class _TmnxObjectAppResvCbs_Type(Integer32):
    """Custom type tmnxObjectAppResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppResvCbs_Type.__name__ = "Integer32"
_TmnxObjectAppResvCbs_Object = MibTableColumn
tmnxObjectAppResvCbs = _TmnxObjectAppResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 6),
    _TmnxObjectAppResvCbs_Type()
)
tmnxObjectAppResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbs.setStatus("current")


class _TmnxObjectAppSlopePolicy_Type(TNamedItem):
    """Custom type tmnxObjectAppSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxObjectAppSlopePolicy_Object = MibTableColumn
tmnxObjectAppSlopePolicy = _TmnxObjectAppSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 7),
    _TmnxObjectAppSlopePolicy_Type()
)
tmnxObjectAppSlopePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxObjectAppSlopePolicy.setStatus("current")


class _TmnxObjectAppPoolSize_Type(Integer32):
    """Custom type tmnxObjectAppPoolSize based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppPoolSize_Type.__name__ = "Integer32"
_TmnxObjectAppPoolSize_Object = MibTableColumn
tmnxObjectAppPoolSize = _TmnxObjectAppPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 8),
    _TmnxObjectAppPoolSize_Type()
)
tmnxObjectAppPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxObjectAppPoolSize.setStatus("current")
_TmnxATMObjs_ObjectIdentity = ObjectIdentity
tmnxATMObjs = _TmnxATMObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11)
)
_TmnxATMIntfTable_Object = MibTable
tmnxATMIntfTable = _TmnxATMIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxATMIntfTable.setStatus("current")
_TmnxATMIntfEntry_Object = MibTableRow
tmnxATMIntfEntry = _TmnxATMIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1)
)
tmnxATMIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxATMIntfEntry.setStatus("current")


class _TmnxATMIntfCellFormat_Type(Integer32):
    """Custom type tmnxATMIntfCellFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_TmnxATMIntfCellFormat_Type.__name__ = "Integer32"
_TmnxATMIntfCellFormat_Object = MibTableColumn
tmnxATMIntfCellFormat = _TmnxATMIntfCellFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 1),
    _TmnxATMIntfCellFormat_Type()
)
tmnxATMIntfCellFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfCellFormat.setStatus("current")


class _TmnxATMIntfMinVpValue_Type(Integer32):
    """Custom type tmnxATMIntfMinVpValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TmnxATMIntfMinVpValue_Type.__name__ = "Integer32"
_TmnxATMIntfMinVpValue_Object = MibTableColumn
tmnxATMIntfMinVpValue = _TmnxATMIntfMinVpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 2),
    _TmnxATMIntfMinVpValue_Type()
)
tmnxATMIntfMinVpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfMinVpValue.setStatus("current")


class _TmnxATMIntfMapping_Type(Integer32):
    """Custom type tmnxATMIntfMapping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("plcp", 2))
    )


_TmnxATMIntfMapping_Type.__name__ = "Integer32"
_TmnxATMIntfMapping_Object = MibTableColumn
tmnxATMIntfMapping = _TmnxATMIntfMapping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 3),
    _TmnxATMIntfMapping_Type()
)
tmnxATMIntfMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfMapping.setStatus("current")
_TmnxPortStatsObjs_ObjectIdentity = ObjectIdentity
tmnxPortStatsObjs = _TmnxPortStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12)
)
_TmnxPortNetIngressStatsTable_Object = MibTable
tmnxPortNetIngressStatsTable = _TmnxPortNetIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxPortNetIngressStatsTable.setStatus("current")
_TmnxPortNetIngressStatsEntry_Object = MibTableRow
tmnxPortNetIngressStatsEntry = _TmnxPortNetIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1)
)
tmnxPortNetIngressStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressQueueIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortNetIngressStatsEntry.setStatus("current")


class _TmnxPortNetIngressQueueIndex_Type(TQueueId):
    """Custom type tmnxPortNetIngressQueueIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxPortNetIngressQueueIndex_Type.__name__ = "TQueueId"
_TmnxPortNetIngressQueueIndex_Object = MibTableColumn
tmnxPortNetIngressQueueIndex = _TmnxPortNetIngressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 1),
    _TmnxPortNetIngressQueueIndex_Type()
)
tmnxPortNetIngressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortNetIngressQueueIndex.setStatus("current")
_TmnxPortNetIngressFwdInProfPkts_Type = Counter64
_TmnxPortNetIngressFwdInProfPkts_Object = MibTableColumn
tmnxPortNetIngressFwdInProfPkts = _TmnxPortNetIngressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 2),
    _TmnxPortNetIngressFwdInProfPkts_Type()
)
tmnxPortNetIngressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdInProfPkts.setStatus("current")
_TmnxPortNetIngressFwdOutProfPkts_Type = Counter64
_TmnxPortNetIngressFwdOutProfPkts_Object = MibTableColumn
tmnxPortNetIngressFwdOutProfPkts = _TmnxPortNetIngressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 3),
    _TmnxPortNetIngressFwdOutProfPkts_Type()
)
tmnxPortNetIngressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdOutProfPkts.setStatus("current")
_TmnxPortNetIngressFwdInProfOcts_Type = Counter64
_TmnxPortNetIngressFwdInProfOcts_Object = MibTableColumn
tmnxPortNetIngressFwdInProfOcts = _TmnxPortNetIngressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 4),
    _TmnxPortNetIngressFwdInProfOcts_Type()
)
tmnxPortNetIngressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdInProfOcts.setStatus("current")
_TmnxPortNetIngressFwdOutProfOcts_Type = Counter64
_TmnxPortNetIngressFwdOutProfOcts_Object = MibTableColumn
tmnxPortNetIngressFwdOutProfOcts = _TmnxPortNetIngressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 5),
    _TmnxPortNetIngressFwdOutProfOcts_Type()
)
tmnxPortNetIngressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdOutProfOcts.setStatus("current")
_TmnxPortNetIngressDroInProfPkts_Type = Counter64
_TmnxPortNetIngressDroInProfPkts_Object = MibTableColumn
tmnxPortNetIngressDroInProfPkts = _TmnxPortNetIngressDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 6),
    _TmnxPortNetIngressDroInProfPkts_Type()
)
tmnxPortNetIngressDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroInProfPkts.setStatus("current")
_TmnxPortNetIngressDroOutProfPkts_Type = Counter64
_TmnxPortNetIngressDroOutProfPkts_Object = MibTableColumn
tmnxPortNetIngressDroOutProfPkts = _TmnxPortNetIngressDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 7),
    _TmnxPortNetIngressDroOutProfPkts_Type()
)
tmnxPortNetIngressDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroOutProfPkts.setStatus("current")
_TmnxPortNetIngressDroInProfOcts_Type = Counter64
_TmnxPortNetIngressDroInProfOcts_Object = MibTableColumn
tmnxPortNetIngressDroInProfOcts = _TmnxPortNetIngressDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 8),
    _TmnxPortNetIngressDroInProfOcts_Type()
)
tmnxPortNetIngressDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroInProfOcts.setStatus("current")
_TmnxPortNetIngressDroOutProfOcts_Type = Counter64
_TmnxPortNetIngressDroOutProfOcts_Object = MibTableColumn
tmnxPortNetIngressDroOutProfOcts = _TmnxPortNetIngressDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 9),
    _TmnxPortNetIngressDroOutProfOcts_Type()
)
tmnxPortNetIngressDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroOutProfOcts.setStatus("current")
_TmnxPortNetEgressStatsTable_Object = MibTable
tmnxPortNetEgressStatsTable = _TmnxPortNetEgressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2)
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressStatsTable.setStatus("current")
_TmnxPortNetEgressStatsEntry_Object = MibTableRow
tmnxPortNetEgressStatsEntry = _TmnxPortNetEgressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1)
)
tmnxPortNetEgressStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressStatsEntry.setStatus("current")


class _TmnxPortNetEgressQueueIndex_Type(TQueueId):
    """Custom type tmnxPortNetEgressQueueIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortNetEgressQueueIndex_Type.__name__ = "TQueueId"
_TmnxPortNetEgressQueueIndex_Object = MibTableColumn
tmnxPortNetEgressQueueIndex = _TmnxPortNetEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 1),
    _TmnxPortNetEgressQueueIndex_Type()
)
tmnxPortNetEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueIndex.setStatus("current")
_TmnxPortNetEgressFwdInProfPkts_Type = Counter64
_TmnxPortNetEgressFwdInProfPkts_Object = MibTableColumn
tmnxPortNetEgressFwdInProfPkts = _TmnxPortNetEgressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 2),
    _TmnxPortNetEgressFwdInProfPkts_Type()
)
tmnxPortNetEgressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdInProfPkts.setStatus("current")
_TmnxPortNetEgressFwdOutProfPkts_Type = Counter64
_TmnxPortNetEgressFwdOutProfPkts_Object = MibTableColumn
tmnxPortNetEgressFwdOutProfPkts = _TmnxPortNetEgressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 3),
    _TmnxPortNetEgressFwdOutProfPkts_Type()
)
tmnxPortNetEgressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdOutProfPkts.setStatus("current")
_TmnxPortNetEgressFwdInProfOcts_Type = Counter64
_TmnxPortNetEgressFwdInProfOcts_Object = MibTableColumn
tmnxPortNetEgressFwdInProfOcts = _TmnxPortNetEgressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 4),
    _TmnxPortNetEgressFwdInProfOcts_Type()
)
tmnxPortNetEgressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdInProfOcts.setStatus("current")
_TmnxPortNetEgressFwdOutProfOcts_Type = Counter64
_TmnxPortNetEgressFwdOutProfOcts_Object = MibTableColumn
tmnxPortNetEgressFwdOutProfOcts = _TmnxPortNetEgressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 5),
    _TmnxPortNetEgressFwdOutProfOcts_Type()
)
tmnxPortNetEgressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdOutProfOcts.setStatus("current")
_TmnxPortNetEgressDroInProfPkts_Type = Counter64
_TmnxPortNetEgressDroInProfPkts_Object = MibTableColumn
tmnxPortNetEgressDroInProfPkts = _TmnxPortNetEgressDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 6),
    _TmnxPortNetEgressDroInProfPkts_Type()
)
tmnxPortNetEgressDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroInProfPkts.setStatus("current")
_TmnxPortNetEgressDroOutProfPkts_Type = Counter64
_TmnxPortNetEgressDroOutProfPkts_Object = MibTableColumn
tmnxPortNetEgressDroOutProfPkts = _TmnxPortNetEgressDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 7),
    _TmnxPortNetEgressDroOutProfPkts_Type()
)
tmnxPortNetEgressDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroOutProfPkts.setStatus("current")
_TmnxPortNetEgressDroInProfOcts_Type = Counter64
_TmnxPortNetEgressDroInProfOcts_Object = MibTableColumn
tmnxPortNetEgressDroInProfOcts = _TmnxPortNetEgressDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 8),
    _TmnxPortNetEgressDroInProfOcts_Type()
)
tmnxPortNetEgressDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroInProfOcts.setStatus("current")
_TmnxPortNetEgressDroOutProfOcts_Type = Counter64
_TmnxPortNetEgressDroOutProfOcts_Object = MibTableColumn
tmnxPortNetEgressDroOutProfOcts = _TmnxPortNetEgressDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 9),
    _TmnxPortNetEgressDroOutProfOcts_Type()
)
tmnxPortNetEgressDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroOutProfOcts.setStatus("current")
_TmnxCiscoHDLCStatsTable_Object = MibTable
tmnxCiscoHDLCStatsTable = _TmnxCiscoHDLCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatsTable.setStatus("current")
_TmnxCiscoHDLCStatsEntry_Object = MibTableRow
tmnxCiscoHDLCStatsEntry = _TmnxCiscoHDLCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatsEntry.setStatus("current")
_TmnxCiscoHDLCDiscardStatInPkts_Type = Unsigned32
_TmnxCiscoHDLCDiscardStatInPkts_Object = MibTableColumn
tmnxCiscoHDLCDiscardStatInPkts = _TmnxCiscoHDLCDiscardStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 1),
    _TmnxCiscoHDLCDiscardStatInPkts_Type()
)
tmnxCiscoHDLCDiscardStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDiscardStatInPkts.setStatus("current")
_TmnxCiscoHDLCDiscardStatOutPkts_Type = Unsigned32
_TmnxCiscoHDLCDiscardStatOutPkts_Object = MibTableColumn
tmnxCiscoHDLCDiscardStatOutPkts = _TmnxCiscoHDLCDiscardStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 2),
    _TmnxCiscoHDLCDiscardStatOutPkts_Type()
)
tmnxCiscoHDLCDiscardStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDiscardStatOutPkts.setStatus("current")
_TmnxCiscoHDLCStatInPkts_Type = Unsigned32
_TmnxCiscoHDLCStatInPkts_Object = MibTableColumn
tmnxCiscoHDLCStatInPkts = _TmnxCiscoHDLCStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 3),
    _TmnxCiscoHDLCStatInPkts_Type()
)
tmnxCiscoHDLCStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatInPkts.setStatus("current")
_TmnxCiscoHDLCStatOutPkts_Type = Unsigned32
_TmnxCiscoHDLCStatOutPkts_Object = MibTableColumn
tmnxCiscoHDLCStatOutPkts = _TmnxCiscoHDLCStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 4),
    _TmnxCiscoHDLCStatOutPkts_Type()
)
tmnxCiscoHDLCStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatOutPkts.setStatus("current")
_TmnxCiscoHDLCStatInOctets_Type = Unsigned32
_TmnxCiscoHDLCStatInOctets_Object = MibTableColumn
tmnxCiscoHDLCStatInOctets = _TmnxCiscoHDLCStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 5),
    _TmnxCiscoHDLCStatInOctets_Type()
)
tmnxCiscoHDLCStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatInOctets.setStatus("current")
_TmnxCiscoHDLCStatOutOctets_Type = Unsigned32
_TmnxCiscoHDLCStatOutOctets_Object = MibTableColumn
tmnxCiscoHDLCStatOutOctets = _TmnxCiscoHDLCStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 6),
    _TmnxCiscoHDLCStatOutOctets_Type()
)
tmnxCiscoHDLCStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatOutOctets.setStatus("current")
_TmnxMcMlpppStatsTable_Object = MibTable
tmnxMcMlpppStatsTable = _TmnxMcMlpppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsTable.setStatus("current")
_TmnxMcMlpppStatsEntry_Object = MibTableRow
tmnxMcMlpppStatsEntry = _TmnxMcMlpppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1)
)
tmnxMcMlpppStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppClassIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEntry.setStatus("current")
_TmnxMcMlpppClassIndex_Type = TmnxMcMlpppClassIndex
_TmnxMcMlpppClassIndex_Object = MibTableColumn
tmnxMcMlpppClassIndex = _TmnxMcMlpppClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 1),
    _TmnxMcMlpppClassIndex_Type()
)
tmnxMcMlpppClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcMlpppClassIndex.setStatus("current")
_TmnxMcMlpppStatsIngressOct_Type = Counter32
_TmnxMcMlpppStatsIngressOct_Object = MibTableColumn
tmnxMcMlpppStatsIngressOct = _TmnxMcMlpppStatsIngressOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 2),
    _TmnxMcMlpppStatsIngressOct_Type()
)
tmnxMcMlpppStatsIngressOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressOct.setStatus("current")
_TmnxMcMlpppStatsIngressPkt_Type = Counter32
_TmnxMcMlpppStatsIngressPkt_Object = MibTableColumn
tmnxMcMlpppStatsIngressPkt = _TmnxMcMlpppStatsIngressPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 3),
    _TmnxMcMlpppStatsIngressPkt_Type()
)
tmnxMcMlpppStatsIngressPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressPkt.setStatus("current")
_TmnxMcMlpppStatsIngressErrPkt_Type = Counter32
_TmnxMcMlpppStatsIngressErrPkt_Object = MibTableColumn
tmnxMcMlpppStatsIngressErrPkt = _TmnxMcMlpppStatsIngressErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 4),
    _TmnxMcMlpppStatsIngressErrPkt_Type()
)
tmnxMcMlpppStatsIngressErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressErrPkt.setStatus("current")
_TmnxMcMlpppStatsEgressOct_Type = Counter32
_TmnxMcMlpppStatsEgressOct_Object = MibTableColumn
tmnxMcMlpppStatsEgressOct = _TmnxMcMlpppStatsEgressOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 5),
    _TmnxMcMlpppStatsEgressOct_Type()
)
tmnxMcMlpppStatsEgressOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressOct.setStatus("current")
_TmnxMcMlpppStatsEgressPkt_Type = Counter32
_TmnxMcMlpppStatsEgressPkt_Object = MibTableColumn
tmnxMcMlpppStatsEgressPkt = _TmnxMcMlpppStatsEgressPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 6),
    _TmnxMcMlpppStatsEgressPkt_Type()
)
tmnxMcMlpppStatsEgressPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressPkt.setStatus("current")
_TmnxMcMlpppStatsEgressErrPkt_Type = Counter32
_TmnxMcMlpppStatsEgressErrPkt_Object = MibTableColumn
tmnxMcMlpppStatsEgressErrPkt = _TmnxMcMlpppStatsEgressErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 7),
    _TmnxMcMlpppStatsEgressErrPkt_Type()
)
tmnxMcMlpppStatsEgressErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressErrPkt.setStatus("current")
_TmnxPortNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPortNotifyPrefix = _TmnxPortNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2)
)
_TmnxPortNotification_ObjectIdentity = ObjectIdentity
tmnxPortNotification = _TmnxPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0)
)
tmnxPortEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB",
     "tmnxPortTestEntry")
)
tmnxPortTestEntry.setIndexNames(*tmnxPortEntry.getIndexNames())
tmnxCiscoHDLCEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB",
     "tmnxCiscoHDLCStatsEntry")
)
tmnxCiscoHDLCStatsEntry.setIndexNames(*tmnxCiscoHDLCEntry.getIndexNames())

# Managed Objects groups

tmnxPortFRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 5)
)
tmnxPortFRGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiN392Dce"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiN393Dce"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiT392Dce"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiTxStatusEnqMsgs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiRxStatusEnqMsgs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiStatusEnqMsgTimeouts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiTxStatusMsgs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiRxStatusMsgs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiStatusMsgTimeouts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiDiscardedMsgs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxFRDlcmiInvRxSeqNumMsgs"))
)
if mibBuilder.loadTexts:
    tmnxPortFRGroup.setStatus("current")

tmnxQosAppObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 6)
)
tmnxQosAppObjsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppPoolRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppResvCbs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppSlopePolicy"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxObjectAppPoolSize"))
)
if mibBuilder.loadTexts:
    tmnxQosAppObjsGroup.setStatus("current")

tmnxPortTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 7)
)
tmnxPortTestGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestParameter"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestLastResult"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestStartTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestEndTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTestAction"))
)
if mibBuilder.loadTexts:
    tmnxPortTestGroup.setStatus("current")

tmnxPortObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 11)
)
tmnxPortObsoleteGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1IdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroOutProfOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortObsoleteGroup.setStatus("current")

tmnxPortIngrMdaQosStatR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 14)
)
tmnxPortIngrMdaQosStatR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos00StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos00StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos01StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos01StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos02StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos02StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos03StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos03StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos04StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos04StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos05StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos05StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos06StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos06StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos07StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos07StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos08StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos08StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos09StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos09StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos10StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos10StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos11StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos11StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos12StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos12StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos13StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos13StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos14StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos14StatDropOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos15StatDropPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos15StatDropOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatR2r1Group.setStatus("current")

tmnxPortStatsR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 16)
)
tmnxPortStatsR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressDroInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressDroOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressDroInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetIngressDroOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdOutProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressDroInProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressDroOutProfPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressDroInProfOcts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetEgressDroOutProfOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortStatsR2r1Group.setStatus("current")

tmnxPortNotifyObjsGroupR2r1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 18)
)
tmnxPortNotifyObjsGroupR2r1.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyBundleId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupR2r1.setStatus("current")

tmnxPortSonetV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 21)
)
tmnxPortSonetV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetFraming"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetBerSdThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetBerSfThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetLoopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSectionTraceMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetJ0String"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetMonS1Byte"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetMonJ0String"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetMonK1Byte"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetMonK2Byte"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSingleFiber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetHoldTimeUp"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetHoldTimeDown"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathScramble"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathC2Byte"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathJ1String"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathOperMRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathMonC2Byte"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathMonJ1String"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetPathChildType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetGroupType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetGroupParentPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetGroupChildType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetGroupName"))
)
if mibBuilder.loadTexts:
    tmnxPortSonetV3v0Group.setStatus("current")

tmnxPortTDMV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 22)
)
tmnxPortTDMV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMV3v0Group.setStatus("obsolete")

tmnxPortATMV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 23)
)
tmnxPortATMV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxATMIntfCellFormat"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxATMIntfMinVpValue"))
)
if mibBuilder.loadTexts:
    tmnxPortATMV3v0Group.setStatus("obsolete")

tmnxScalarPortV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 24)
)
tmnxScalarPortV3v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxL4LoadBalancing")
)
if mibBuilder.loadTexts:
    tmnxScalarPortV3v0Group.setStatus("current")

tmnxPortV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 25)
)
tmnxPortV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"))
)
if mibBuilder.loadTexts:
    tmnxPortV3v0Group.setStatus("obsolete")

tmnxCiscoHDLCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 26)
)
tmnxCiscoHDLCGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCKeepAliveInt"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCUpCount"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCDownCount"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCOperState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCDiscardStatInPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCDiscardStatOutPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatInPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatOutPkts"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatInOctets"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatOutOctets"))
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCGroup.setStatus("current")

tmnxMlBundleV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 27)
)
tmnxMlBundleV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortBundleNumber"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleV3v0Group.setStatus("obsolete")

tmnxObsoleteGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 28)
)
tmnxObsoleteGroupV3v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetAps"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsAuthKey"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsNeighborAddr"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsAdvertiseInterval"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsAdvertiseTimeLeft"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsHoldTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetApsHoldTimeLeft"))
)
if mibBuilder.loadTexts:
    tmnxObsoleteGroupV3v0.setStatus("current")

tmnxPortEthernetV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 29)
)
tmnxPortEthernetV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV3v0Group.setStatus("obsolete")

tmnxPortTDMGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 30)
)
tmnxPortTDMGroupV4v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV4v0.setStatus("obsolete")

tmnxPortATMGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 31)
)
tmnxPortATMGroupV4v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxATMIntfCellFormat"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxATMIntfMinVpValue"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxATMIntfMapping"))
)
if mibBuilder.loadTexts:
    tmnxPortATMGroupV4v0.setStatus("current")

tmnxMlBundleGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 32)
)
tmnxMlBundleGroupV4v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortBundleNumber"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV4v0.setStatus("obsolete")

tmnxMlImaBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 33)
)
tmnxMlImaBundleGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpLnkActTimer"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpLnkDeactTimer"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSymmetryMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxRefLnk"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxRefLnk"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmNeState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmFeState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmFailState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmDownSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmOperSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpAvailTxCR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpAvailRxCR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpNeFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpFeFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpErrorIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpLostRxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxOamLablVal"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxOamLablVal"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpAlphaValue"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpBetaValue"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpGammaValue"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpNeClockMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpFeClockMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpVersion"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpMaxConfBw"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestMember"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpDiffDelayMaxObs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleImaGrpLeastDelayLink"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxFailState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxFailState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaTxLid"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxLid"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaViolations"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeSevErrSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeSevErrSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeUnavailSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeUnavailSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxUnuseSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxUnuseSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxUnuseSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxUnuseSecs"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxNumFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxNumFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxNumFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxNumFails"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaTxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaErrorIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaLstRxIcpCells"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaOifAnomalies"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxTestState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxTestPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberImaRelDelay"))
)
if mibBuilder.loadTexts:
    tmnxMlImaBundleGroup.setStatus("current")

tmnx7710PortTDMGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 34)
)
tmnx7710PortTDMGroupV3v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortBuildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLineLength"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLbo"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortDbGain"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InsertSingleBitError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCollectStats"))
)
if mibBuilder.loadTexts:
    tmnx7710PortTDMGroupV3v0.setStatus("obsolete")

tmnxPortGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 35)
)
tmnxPortGroupV4v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV4v0.setStatus("obsolete")

tmnxObsoleteGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 36)
)
tmnxObsoleteGroupV5v0.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverCode")
)
if mibBuilder.loadTexts:
    tmnxObsoleteGroupV5v0.setStatus("current")

tmnxPortSchedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 37)
)
tmnxPortSchedV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEgrPortSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideSchedName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLastChanged"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideMaxRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl1PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl1CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl2PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl2CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl3PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl3CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl4PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl4CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl5PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl5CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl6PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl6CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl7PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl7CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl8PIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl8CIR"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSchedOverrideFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortSchedV5v0Group.setStatus("current")

tmnxPortEthernetV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 38)
)
tmnxPortEthernetV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV5v0Group.setStatus("obsolete")

tmnxPortGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 39)
)
tmnxPortGroupV5v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV5v0.setStatus("obsolete")

tmnxMlBundleGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 40)
)
tmnxMlBundleGroupV5v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortBundleNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleProtectedType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleParentBundle"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocWorkingBundleID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocProtectBundleID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocActiveBundleID"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV5v0.setStatus("obsolete")

tmnxPortTDMGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 42)
)
tmnxPortTDMGroupV5v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV5v0.setStatus("obsolete")

tmnx7710PortTDMGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 43)
)
tmnx7710PortTDMGroupV5v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortBuildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLineLength"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortLbo"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1PortDbGain"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InsertSingleBitError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCollectStats"))
)
if mibBuilder.loadTexts:
    tmnx7710PortTDMGroupV5v0.setStatus("current")

tmnxPortCemGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 44)
)
tmnxPortCemGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSyncState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockMasterPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1SignalMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockSyncState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockMasterPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupPayloadFillType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupPayloadPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSignalFillType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSignalPattern"))
)
if mibBuilder.loadTexts:
    tmnxPortCemGroupV6v0.setStatus("current")

tmnxMcMlpppBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 45)
)
tmnxMcMlpppBundleGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMlpppClassCount"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMlpppIngQoSProfId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMlpppEgrQoSProfId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressOct"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressPkt"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressErrPkt"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressOct"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressPkt"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressErrPkt"))
)
if mibBuilder.loadTexts:
    tmnxMcMlpppBundleGroup.setStatus("current")

tmnxPortEthernetV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 47)
)
tmnxPortEthernetV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedEnabled"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedKeepAlive"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedRetry"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherPBBEtype"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV6v0Group.setStatus("current")

tmnxMlBundleGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 48)
)
tmnxMlBundleGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortBundleNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleProtectedType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleParentBundle"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocWorkingBundleID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocProtectBundleID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBPGrpAssocActiveBundleID"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV6v0.setStatus("current")

tmnxMlpppBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 49)
)
tmnxMlpppBundleGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMlpppEndpointID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMlpppEndpointIDClass"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleLFI"))
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleGroup.setStatus("current")

tmnxPortTDMGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 52)
)
tmnxPortTDMGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BerSdThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1BerSfThreshold"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV6v0.setStatus("current")

tmnxDigitalDiagMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 53)
)
tmnxDigitalDiagMonitorGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTemperature"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTempLowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTempLowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTempHiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTempHiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltage"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageLowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageLowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageHiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageHiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrent"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentLowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentLowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentHiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentHiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxOutputPower"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerLowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerLowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerHiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerHiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPower"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerLowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerLowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerHiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerHiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1LowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1LowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1HiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1HiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux1Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2LowWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2LowAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2HiWarning"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2HiAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMAux2Type"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMFailedThresholds"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExternallyCalibrated"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower4"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower3"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower2"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower1"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower0"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTxLaserBiasSlope"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTxLaserBiasOffset"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTxPowerSlope"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTxPowerOffset"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTemperatureSlope"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalTemperatureOffset"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalVoltageSlope"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMExtCalVoltageOffset"))
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorGroup.setStatus("current")

tmnxPortGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 54)
)
tmnxPortGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortLastClearedTime"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortDDMEventSuppression"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPStatus"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV6v0.setStatus("current")

tmnxNamedPoolGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 55)
)
tmnxNamedPoolGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngNamedPoolPlcy"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEgrNamedPoolPlcy"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortIngPoolPercentRate"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEgrPoolPercentRate"))
)
if mibBuilder.loadTexts:
    tmnxNamedPoolGroupV6v0.setStatus("current")

tmnxPortNotifyObjsGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 57)
)
tmnxPortNotifyObjsGroupV6v0.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMFailedObject")
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV6v0.setStatus("current")


# Notification objects

tmnxEqOobPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 1)
)
tmnxEqOobPortFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxEqOobPortFailure.setStatus(
        "obsolete"
    )

tmnxEqPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 2)
)
tmnxEqPortFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxEqPortFailure.setStatus(
        "obsolete"
    )

tmnxQosServiceDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 3)
)
tmnxQosServiceDegraded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxQosServiceDegraded.setStatus(
        "obsolete"
    )

tmnxEqPortSonetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 4)
)
tmnxEqPortSonetAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetAlarm.setStatus(
        "current"
    )

tmnxEqPortSonetAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 5)
)
tmnxEqPortSonetAlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetAlarmClear.setStatus(
        "current"
    )

tmnxEqPortSonetPathAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 6)
)
tmnxEqPortSonetPathAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetPathAlarm.setStatus(
        "current"
    )

tmnxEqPortSonetPathAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 7)
)
tmnxEqPortSonetPathAlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetPathAlarmClear.setStatus(
        "current"
    )

tmnxEqPortSFPInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 8)
)
tmnxEqPortSFPInserted.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPInserted.setStatus(
        "current"
    )

tmnxEqPortSFPRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 9)
)
tmnxEqPortSFPRemoved.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPRemoved.setStatus(
        "current"
    )

tmnxEqPortWrongSFP = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 10)
)
tmnxEqPortWrongSFP.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortWrongSFP.setStatus(
        "obsolete"
    )

tmnxEqPortSFPCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 11)
)
tmnxEqPortSFPCorrupted.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPCorrupted.setStatus(
        "obsolete"
    )

tmnxPortNotifyBerSdTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 12)
)
tmnxPortNotifyBerSdTca.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetBerSdThreshold"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyBerSdTca.setStatus(
        "obsolete"
    )

tmnxPortNotifyBerSfTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 13)
)
tmnxPortNotifyBerSfTca.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetBerSfThreshold"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyBerSfTca.setStatus(
        "obsolete"
    )

tmnxEqPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 14)
)
tmnxEqPortError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyError"))
)
if mibBuilder.loadTexts:
    tmnxEqPortError.setStatus(
        "current"
    )

tmnxEqPortDS3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 15)
)
tmnxEqPortDS3Alarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS3Alarm.setStatus(
        "current"
    )

tmnxEqPortDS3AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 16)
)
tmnxEqPortDS3AlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS3AlarmClear.setStatus(
        "current"
    )

tmnxEqPortDS1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 17)
)
tmnxEqPortDS1Alarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS1Alarm.setStatus(
        "current"
    )

tmnxEqPortDS1AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 18)
)
tmnxEqPortDS1AlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS1AlarmClear.setStatus(
        "current"
    )

tmnxEqPortBndlYellowDiffExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 19)
)
tmnxEqPortBndlYellowDiffExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"))
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlYellowDiffExceeded.setStatus(
        "current"
    )

tmnxEqPortBndlRedDiffExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 20)
)
tmnxEqPortBndlRedDiffExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"))
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlRedDiffExceeded.setStatus(
        "current"
    )

tmnxEqPortBndlBadEndPtDiscr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 21)
)
tmnxEqPortBndlBadEndPtDiscr.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason")
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlBadEndPtDiscr.setStatus(
        "current"
    )

tmnxEqPortEtherAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 22)
)
tmnxEqPortEtherAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherAlarm.setStatus(
        "current"
    )

tmnxEqPortEtherAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 23)
)
tmnxEqPortEtherAlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherAlarmClear.setStatus(
        "current"
    )

tmnxDS1E1LoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 24)
)
tmnxDS1E1LoopbackStarted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"))
)
if mibBuilder.loadTexts:
    tmnxDS1E1LoopbackStarted.setStatus(
        "current"
    )

tmnxDS1E1LoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 25)
)
tmnxDS1E1LoopbackStopped.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1Loopback"))
)
if mibBuilder.loadTexts:
    tmnxDS1E1LoopbackStopped.setStatus(
        "current"
    )

tmnxDS3E3LoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 26)
)
tmnxDS3E3LoopbackStarted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"))
)
if mibBuilder.loadTexts:
    tmnxDS3E3LoopbackStarted.setStatus(
        "current"
    )

tmnxDS3E3LoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 27)
)
tmnxDS3E3LoopbackStopped.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"))
)
if mibBuilder.loadTexts:
    tmnxDS3E3LoopbackStopped.setStatus(
        "current"
    )

tmnxSonetSDHLoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 28)
)
tmnxSonetSDHLoopbackStarted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSonetSDHLoopbackStarted.setStatus(
        "current"
    )

tmnxSonetSDHLoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 29)
)
tmnxSonetSDHLoopbackStopped.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSonetSDHLoopbackStopped.setStatus(
        "current"
    )

tmnxEqPortEtherLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 30)
)
tmnxEqPortEtherLoopDetected.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherLoopDetected.setStatus(
        "current"
    )

tmnxEqPortEtherLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 31)
)
tmnxEqPortEtherLoopCleared.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherLoopCleared.setStatus(
        "current"
    )

tmnxEqPortSpeedCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 32)
)
tmnxEqPortSpeedCfgNotCompatible.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSpeedCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqPortDuplexCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 33)
)
tmnxEqPortDuplexCfgNotCompatible.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDuplexCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqPortIngressRateCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 34)
)
tmnxEqPortIngressRateCfgNotCompatible.setObjects(
    ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortIngressRateCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqDigitalDiagMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 35)
)
tmnxEqDigitalDiagMonitorFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDDMFailedObject"))
)
if mibBuilder.loadTexts:
    tmnxEqDigitalDiagMonitorFailure.setStatus(
        "current"
    )

tmnxEqPortSFPStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 36)
)
tmnxEqPortSFPStatusFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortSFPStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPStatusFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxPortNotificationGroupR2r1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 17)
)
tmnxPortNotificationGroupR2r1.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupR2r1.setStatus(
        "obsolete"
    )

tmnxPortNotifyObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 20)
)
tmnxPortNotifyObsoleteGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqOobPortFailure"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortFailure"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxQosServiceDegraded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyBerSdTca"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyBerSfTca"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortWrongSFP"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObsoleteGroup.setStatus(
        "current"
    )

tmnxPortNotificationGroupV5v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 41)
)
tmnxPortNotificationGroupV5v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV5v0.setStatus(
        "obsolete"
    )

tmnxPortNotificationGroupV6v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 46)
)
tmnxPortNotificationGroupV6v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopDetected"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopCleared"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqDigitalDiagMonitorFailure"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPStatusFailure"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV6v0.setStatus(
        "current"
    )

tmnxPortNotificationGroupV3v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 50)
)
tmnxPortNotificationGroupV3v0.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV3v0.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

tmnxPortComp7750V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V4v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V6v0.setStatus(
        "current"
    )

tmnxPortComp7450V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V4v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V6v0.setStatus(
        "current"
    )

tmnxPortComp7710V3v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V3v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V6v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-PORT-MIB",
    **{"TmnxPortOperStatus": TmnxPortOperStatus,
       "TmnxPortEtherReportValue": TmnxPortEtherReportValue,
       "TmnxPortEtherReportStatus": TmnxPortEtherReportStatus,
       "TmnxPortClass": TmnxPortClass,
       "TmnxPortConnectorType": TmnxPortConnectorType,
       "TmnxPortState": TmnxPortState,
       "TmnxPortType": TmnxPortType,
       "TmnxDs0ChannelList": TmnxDs0ChannelList,
       "TmnxBundleID": TmnxBundleID,
       "TmnxDSXBertPattern": TmnxDSXBertPattern,
       "TmnxDSXBertOperStatus": TmnxDSXBertOperStatus,
       "TmnxDSXIdleCycleFlags": TmnxDSXIdleCycleFlags,
       "TmnxDSXIdleFillType": TmnxDSXIdleFillType,
       "TmnxDSXLoopback": TmnxDSXLoopback,
       "TmnxDSXReportAlarm": TmnxDSXReportAlarm,
       "TmnxDSXClockSource": TmnxDSXClockSource,
       "TmnxDSXClockSyncState": TmnxDSXClockSyncState,
       "TmnxDS1Loopback": TmnxDS1Loopback,
       "TmnxDS3Loopback": TmnxDS3Loopback,
       "TmnxImaGrpState": TmnxImaGrpState,
       "TmnxImaGrpFailState": TmnxImaGrpFailState,
       "TmnxImaLnkState": TmnxImaLnkState,
       "TmnxImaLnkFailState": TmnxImaLnkFailState,
       "TmnxImaTestState": TmnxImaTestState,
       "TmnxImaGrpClockModes": TmnxImaGrpClockModes,
       "TmnxImaGrpVersion": TmnxImaGrpVersion,
       "TmnxMcMlpppClassIndex": TmnxMcMlpppClassIndex,
       "TmnxMlpppEndpointIdClass": TmnxMlpppEndpointIdClass,
       "tmnxPortMIBModule": tmnxPortMIBModule,
       "tmnxPortConformance": tmnxPortConformance,
       "tmnxPortCompliances": tmnxPortCompliances,
       "tmnxPortComp7750": tmnxPortComp7750,
       "tmnxPortComp7750V4v0": tmnxPortComp7750V4v0,
       "tmnxPortComp7750V5v0": tmnxPortComp7750V5v0,
       "tmnxPortComp7750V6v0": tmnxPortComp7750V6v0,
       "tmnxPortComp7450": tmnxPortComp7450,
       "tmnxPortComp7450V4v0": tmnxPortComp7450V4v0,
       "tmnxPortComp7450V5v0": tmnxPortComp7450V5v0,
       "tmnxPortComp7450V6v0": tmnxPortComp7450V6v0,
       "tmnxPortComp7710": tmnxPortComp7710,
       "tmnxPortComp7710V3v0": tmnxPortComp7710V3v0,
       "tmnxPortComp7710V5v0": tmnxPortComp7710V5v0,
       "tmnxPortComp7710V6v0": tmnxPortComp7710V6v0,
       "tmnxPortGroups": tmnxPortGroups,
       "tmnxPortFRGroup": tmnxPortFRGroup,
       "tmnxQosAppObjsGroup": tmnxQosAppObjsGroup,
       "tmnxPortTestGroup": tmnxPortTestGroup,
       "tmnxPortObsoleteGroup": tmnxPortObsoleteGroup,
       "tmnxPortIngrMdaQosStatR2r1Group": tmnxPortIngrMdaQosStatR2r1Group,
       "tmnxPortStatsR2r1Group": tmnxPortStatsR2r1Group,
       "tmnxPortNotificationGroupR2r1": tmnxPortNotificationGroupR2r1,
       "tmnxPortNotifyObjsGroupR2r1": tmnxPortNotifyObjsGroupR2r1,
       "tmnxPortNotifyObsoleteGroup": tmnxPortNotifyObsoleteGroup,
       "tmnxPortSonetV3v0Group": tmnxPortSonetV3v0Group,
       "tmnxPortTDMV3v0Group": tmnxPortTDMV3v0Group,
       "tmnxPortATMV3v0Group": tmnxPortATMV3v0Group,
       "tmnxScalarPortV3v0Group": tmnxScalarPortV3v0Group,
       "tmnxPortV3v0Group": tmnxPortV3v0Group,
       "tmnxCiscoHDLCGroup": tmnxCiscoHDLCGroup,
       "tmnxMlBundleV3v0Group": tmnxMlBundleV3v0Group,
       "tmnxObsoleteGroupV3v0": tmnxObsoleteGroupV3v0,
       "tmnxPortEthernetV3v0Group": tmnxPortEthernetV3v0Group,
       "tmnxPortTDMGroupV4v0": tmnxPortTDMGroupV4v0,
       "tmnxPortATMGroupV4v0": tmnxPortATMGroupV4v0,
       "tmnxMlBundleGroupV4v0": tmnxMlBundleGroupV4v0,
       "tmnxMlImaBundleGroup": tmnxMlImaBundleGroup,
       "tmnx7710PortTDMGroupV3v0": tmnx7710PortTDMGroupV3v0,
       "tmnxPortGroupV4v0": tmnxPortGroupV4v0,
       "tmnxObsoleteGroupV5v0": tmnxObsoleteGroupV5v0,
       "tmnxPortSchedV5v0Group": tmnxPortSchedV5v0Group,
       "tmnxPortEthernetV5v0Group": tmnxPortEthernetV5v0Group,
       "tmnxPortGroupV5v0": tmnxPortGroupV5v0,
       "tmnxMlBundleGroupV5v0": tmnxMlBundleGroupV5v0,
       "tmnxPortNotificationGroupV5v0": tmnxPortNotificationGroupV5v0,
       "tmnxPortTDMGroupV5v0": tmnxPortTDMGroupV5v0,
       "tmnx7710PortTDMGroupV5v0": tmnx7710PortTDMGroupV5v0,
       "tmnxPortCemGroupV6v0": tmnxPortCemGroupV6v0,
       "tmnxMcMlpppBundleGroup": tmnxMcMlpppBundleGroup,
       "tmnxPortNotificationGroupV6v0": tmnxPortNotificationGroupV6v0,
       "tmnxPortEthernetV6v0Group": tmnxPortEthernetV6v0Group,
       "tmnxMlBundleGroupV6v0": tmnxMlBundleGroupV6v0,
       "tmnxMlpppBundleGroup": tmnxMlpppBundleGroup,
       "tmnxPortNotificationGroupV3v0": tmnxPortNotificationGroupV3v0,
       "tmnxPortTDMGroupV6v0": tmnxPortTDMGroupV6v0,
       "tmnxDigitalDiagMonitorGroup": tmnxDigitalDiagMonitorGroup,
       "tmnxPortGroupV6v0": tmnxPortGroupV6v0,
       "tmnxNamedPoolGroupV6v0": tmnxNamedPoolGroupV6v0,
       "tmnxPortNotifyObjsGroupV6v0": tmnxPortNotifyObjsGroupV6v0,
       "tmnxPortObjs": tmnxPortObjs,
       "tmnxPortTableLastChange": tmnxPortTableLastChange,
       "tmnxPortTable": tmnxPortTable,
       "tmnxPortEntry": tmnxPortEntry,
       "tmnxPortPortID": tmnxPortPortID,
       "tmnxPortLastChangeTime": tmnxPortLastChangeTime,
       "tmnxPortType": tmnxPortType,
       "tmnxPortClass": tmnxPortClass,
       "tmnxPortDescription": tmnxPortDescription,
       "tmnxPortName": tmnxPortName,
       "tmnxPortAlias": tmnxPortAlias,
       "tmnxPortUserAssignedMac": tmnxPortUserAssignedMac,
       "tmnxPortMacAddress": tmnxPortMacAddress,
       "tmnxPortHwMacAddress": tmnxPortHwMacAddress,
       "tmnxPortMode": tmnxPortMode,
       "tmnxPortEncapType": tmnxPortEncapType,
       "tmnxPortLagId": tmnxPortLagId,
       "tmnxPortHoldTimeUp": tmnxPortHoldTimeUp,
       "tmnxPortHoldTimeDown": tmnxPortHoldTimeDown,
       "tmnxPortUpProtocols": tmnxPortUpProtocols,
       "tmnxPortConnectorType": tmnxPortConnectorType,
       "tmnxPortTransceiverType": tmnxPortTransceiverType,
       "tmnxPortTransceiverCode": tmnxPortTransceiverCode,
       "tmnxPortTransceiverLaserWaveLen": tmnxPortTransceiverLaserWaveLen,
       "tmnxPortTransceiverDiagCapable": tmnxPortTransceiverDiagCapable,
       "tmnxPortTransceiverModelNumber": tmnxPortTransceiverModelNumber,
       "tmnxPortSFPConnectorCode": tmnxPortSFPConnectorCode,
       "tmnxPortSFPVendorOUI": tmnxPortSFPVendorOUI,
       "tmnxPortSFPVendorManufactureDate": tmnxPortSFPVendorManufactureDate,
       "tmnxPortSFPMedia": tmnxPortSFPMedia,
       "tmnxPortSFPEquipped": tmnxPortSFPEquipped,
       "tmnxPortEquipped": tmnxPortEquipped,
       "tmnxPortLinkStatus": tmnxPortLinkStatus,
       "tmnxPortAdminStatus": tmnxPortAdminStatus,
       "tmnxPortOperStatus": tmnxPortOperStatus,
       "tmnxPortState": tmnxPortState,
       "tmnxPortPrevState": tmnxPortPrevState,
       "tmnxPortNumAlarms": tmnxPortNumAlarms,
       "tmnxPortAlarmState": tmnxPortAlarmState,
       "tmnxPortLastAlarmEvent": tmnxPortLastAlarmEvent,
       "tmnxPortClearAlarms": tmnxPortClearAlarms,
       "tmnxPortSFPVendorSerialNum": tmnxPortSFPVendorSerialNum,
       "tmnxPortSFPVendorPartNum": tmnxPortSFPVendorPartNum,
       "tmnxPortLastStateChanged": tmnxPortLastStateChanged,
       "tmnxPortNumChannels": tmnxPortNumChannels,
       "tmnxPortNetworkEgrQueues": tmnxPortNetworkEgrQueues,
       "tmnxPortBundleNumber": tmnxPortBundleNumber,
       "tmnxPortIsLeaf": tmnxPortIsLeaf,
       "tmnxPortChanType": tmnxPortChanType,
       "tmnxPortParentPortID": tmnxPortParentPortID,
       "tmnxPortOpticalCompliance": tmnxPortOpticalCompliance,
       "tmnxPortLoadBalanceAlgorithm": tmnxPortLoadBalanceAlgorithm,
       "tmnxPortEgrPortSchedPlcy": tmnxPortEgrPortSchedPlcy,
       "tmnxPortLastClearedTime": tmnxPortLastClearedTime,
       "tmnxPortIngNamedPoolPlcy": tmnxPortIngNamedPoolPlcy,
       "tmnxPortEgrNamedPoolPlcy": tmnxPortEgrNamedPoolPlcy,
       "tmnxPortIngPoolPercentRate": tmnxPortIngPoolPercentRate,
       "tmnxPortEgrPoolPercentRate": tmnxPortEgrPoolPercentRate,
       "tmnxPortDDMEventSuppression": tmnxPortDDMEventSuppression,
       "tmnxPortSFPStatus": tmnxPortSFPStatus,
       "tmnxPortTestTable": tmnxPortTestTable,
       "tmnxPortTestEntry": tmnxPortTestEntry,
       "tmnxPortTestState": tmnxPortTestState,
       "tmnxPortTestMode": tmnxPortTestMode,
       "tmnxPortTestParameter": tmnxPortTestParameter,
       "tmnxPortTestLastResult": tmnxPortTestLastResult,
       "tmnxPortTestStartTime": tmnxPortTestStartTime,
       "tmnxPortTestEndTime": tmnxPortTestEndTime,
       "tmnxPortTestDuration": tmnxPortTestDuration,
       "tmnxPortTestAction": tmnxPortTestAction,
       "tmnxPortEtherTable": tmnxPortEtherTable,
       "tmnxPortEtherEntry": tmnxPortEtherEntry,
       "tmnxPortEtherMTU": tmnxPortEtherMTU,
       "tmnxPortEtherDuplex": tmnxPortEtherDuplex,
       "tmnxPortEtherSpeed": tmnxPortEtherSpeed,
       "tmnxPortEtherAutoNegotiate": tmnxPortEtherAutoNegotiate,
       "tmnxPortEtherOperDuplex": tmnxPortEtherOperDuplex,
       "tmnxPortEtherOperSpeed": tmnxPortEtherOperSpeed,
       "tmnxPortEtherAcctPolicyId": tmnxPortEtherAcctPolicyId,
       "tmnxPortEtherCollectStats": tmnxPortEtherCollectStats,
       "tmnxPortEtherMDIMDIX": tmnxPortEtherMDIMDIX,
       "tmnxPortEtherXGigMode": tmnxPortEtherXGigMode,
       "tmnxPortEtherEgressRate": tmnxPortEtherEgressRate,
       "tmnxPortEtherDot1qEtype": tmnxPortEtherDot1qEtype,
       "tmnxPortEtherQinqEtype": tmnxPortEtherQinqEtype,
       "tmnxPortEtherIngressRate": tmnxPortEtherIngressRate,
       "tmnxPortEtherReportAlarm": tmnxPortEtherReportAlarm,
       "tmnxPortEtherReportAlarmStatus": tmnxPortEtherReportAlarmStatus,
       "tmnxPortEtherPkts1519toMax": tmnxPortEtherPkts1519toMax,
       "tmnxPortEtherHCOverPkts1519toMax": tmnxPortEtherHCOverPkts1519toMax,
       "tmnxPortEtherHCPkts1519toMax": tmnxPortEtherHCPkts1519toMax,
       "tmnxPortEtherLacpTunnel": tmnxPortEtherLacpTunnel,
       "tmnxPortEtherDownWhenLoopedEnabled": tmnxPortEtherDownWhenLoopedEnabled,
       "tmnxPortEtherDownWhenLoopedKeepAlive": tmnxPortEtherDownWhenLoopedKeepAlive,
       "tmnxPortEtherDownWhenLoopedRetry": tmnxPortEtherDownWhenLoopedRetry,
       "tmnxPortEtherDownWhenLoopedState": tmnxPortEtherDownWhenLoopedState,
       "tmnxPortEtherPBBEtype": tmnxPortEtherPBBEtype,
       "tmnxPortEtherReasonDownFlags": tmnxPortEtherReasonDownFlags,
       "tmnxSonetTable": tmnxSonetTable,
       "tmnxSonetEntry": tmnxSonetEntry,
       "tmnxSonetSpeed": tmnxSonetSpeed,
       "tmnxSonetClockSource": tmnxSonetClockSource,
       "tmnxSonetFraming": tmnxSonetFraming,
       "tmnxSonetReportAlarm": tmnxSonetReportAlarm,
       "tmnxSonetBerSdThreshold": tmnxSonetBerSdThreshold,
       "tmnxSonetBerSfThreshold": tmnxSonetBerSfThreshold,
       "tmnxSonetAps": tmnxSonetAps,
       "tmnxSonetApsAdminStatus": tmnxSonetApsAdminStatus,
       "tmnxSonetApsOperStatus": tmnxSonetApsOperStatus,
       "tmnxSonetApsAuthKey": tmnxSonetApsAuthKey,
       "tmnxSonetApsNeighborAddr": tmnxSonetApsNeighborAddr,
       "tmnxSonetApsAdvertiseInterval": tmnxSonetApsAdvertiseInterval,
       "tmnxSonetApsAdvertiseTimeLeft": tmnxSonetApsAdvertiseTimeLeft,
       "tmnxSonetApsHoldTime": tmnxSonetApsHoldTime,
       "tmnxSonetApsHoldTimeLeft": tmnxSonetApsHoldTimeLeft,
       "tmnxSonetLoopback": tmnxSonetLoopback,
       "tmnxSonetReportAlarmStatus": tmnxSonetReportAlarmStatus,
       "tmnxSonetSectionTraceMode": tmnxSonetSectionTraceMode,
       "tmnxSonetJ0String": tmnxSonetJ0String,
       "tmnxSonetMonS1Byte": tmnxSonetMonS1Byte,
       "tmnxSonetMonJ0String": tmnxSonetMonJ0String,
       "tmnxSonetMonK1Byte": tmnxSonetMonK1Byte,
       "tmnxSonetMonK2Byte": tmnxSonetMonK2Byte,
       "tmnxSonetSingleFiber": tmnxSonetSingleFiber,
       "tmnxSonetHoldTimeUp": tmnxSonetHoldTimeUp,
       "tmnxSonetHoldTimeDown": tmnxSonetHoldTimeDown,
       "tmnxSonetPathTable": tmnxSonetPathTable,
       "tmnxSonetPathEntry": tmnxSonetPathEntry,
       "tmnxSonetPathRowStatus": tmnxSonetPathRowStatus,
       "tmnxSonetPathLastChangeTime": tmnxSonetPathLastChangeTime,
       "tmnxSonetPathMTU": tmnxSonetPathMTU,
       "tmnxSonetPathScramble": tmnxSonetPathScramble,
       "tmnxSonetPathC2Byte": tmnxSonetPathC2Byte,
       "tmnxSonetPathJ1String": tmnxSonetPathJ1String,
       "tmnxSonetPathCRC": tmnxSonetPathCRC,
       "tmnxSonetPathOperMTU": tmnxSonetPathOperMTU,
       "tmnxSonetPathOperMRU": tmnxSonetPathOperMRU,
       "tmnxSonetPathReportAlarm": tmnxSonetPathReportAlarm,
       "tmnxSonetPathAcctPolicyId": tmnxSonetPathAcctPolicyId,
       "tmnxSonetPathCollectStats": tmnxSonetPathCollectStats,
       "tmnxSonetPathReportAlarmStatus": tmnxSonetPathReportAlarmStatus,
       "tmnxSonetPathMonC2Byte": tmnxSonetPathMonC2Byte,
       "tmnxSonetPathMonJ1String": tmnxSonetPathMonJ1String,
       "tmnxSonetPathType": tmnxSonetPathType,
       "tmnxSonetPathChildType": tmnxSonetPathChildType,
       "tmnxPortTypeTable": tmnxPortTypeTable,
       "tmnxPortTypeEntry": tmnxPortTypeEntry,
       "tmnxPortTypeIndex": tmnxPortTypeIndex,
       "tmnxPortTypeName": tmnxPortTypeName,
       "tmnxPortTypeDescription": tmnxPortTypeDescription,
       "tmnxPortTypeStatus": tmnxPortTypeStatus,
       "tmnxPortConnectTypeTable": tmnxPortConnectTypeTable,
       "tmnxPortConnectTypeEntry": tmnxPortConnectTypeEntry,
       "tmnxPortConnectTypeIndex": tmnxPortConnectTypeIndex,
       "tmnxPortConnectTypeName": tmnxPortConnectTypeName,
       "tmnxPortConnectTypeDescription": tmnxPortConnectTypeDescription,
       "tmnxPortConnectTypeStatus": tmnxPortConnectTypeStatus,
       "tmnxPortFCStatsTable": tmnxPortFCStatsTable,
       "tmnxPortFCStatsEntry": tmnxPortFCStatsEntry,
       "tmnxPortFCStatsIndex": tmnxPortFCStatsIndex,
       "tmnxPortFCStatsIngFwdInProfPkts": tmnxPortFCStatsIngFwdInProfPkts,
       "tmnxPortFCStatsIngFwdOutProfPkts": tmnxPortFCStatsIngFwdOutProfPkts,
       "tmnxPortFCStatsIngFwdInProfOcts": tmnxPortFCStatsIngFwdInProfOcts,
       "tmnxPortFCStatsIngFwdOutProfOcts": tmnxPortFCStatsIngFwdOutProfOcts,
       "tmnxPortFCStatsIngDroInProfPkts": tmnxPortFCStatsIngDroInProfPkts,
       "tmnxPortFCStatsIngDroOutProfPkts": tmnxPortFCStatsIngDroOutProfPkts,
       "tmnxPortFCStatsIngDroInProfOcts": tmnxPortFCStatsIngDroInProfOcts,
       "tmnxPortFCStatsIngDroOutProfOcts": tmnxPortFCStatsIngDroOutProfOcts,
       "tmnxPortFCStatsEgrFwdInProfPkts": tmnxPortFCStatsEgrFwdInProfPkts,
       "tmnxPortFCStatsEgrFwdOutProfPkts": tmnxPortFCStatsEgrFwdOutProfPkts,
       "tmnxPortFCStatsEgrFwdInProfOcts": tmnxPortFCStatsEgrFwdInProfOcts,
       "tmnxPortFCStatsEgrFwdOutProfOcts": tmnxPortFCStatsEgrFwdOutProfOcts,
       "tmnxPortFCStatsEgrDroInProfPkts": tmnxPortFCStatsEgrDroInProfPkts,
       "tmnxPortFCStatsEgrDroOutProfPkts": tmnxPortFCStatsEgrDroOutProfPkts,
       "tmnxPortFCStatsEgrDroInProfOcts": tmnxPortFCStatsEgrDroInProfOcts,
       "tmnxPortFCStatsEgrDroOutProfOcts": tmnxPortFCStatsEgrDroOutProfOcts,
       "tmnxDS3Table": tmnxDS3Table,
       "tmnxDS3Entry": tmnxDS3Entry,
       "tmnxDS3Buildout": tmnxDS3Buildout,
       "tmnxDS3LastChangeTime": tmnxDS3LastChangeTime,
       "tmnxDS3Type": tmnxDS3Type,
       "tmnxDS3ChannelTable": tmnxDS3ChannelTable,
       "tmnxDS3ChannelEntry": tmnxDS3ChannelEntry,
       "tmnxDS3ChannelRowStatus": tmnxDS3ChannelRowStatus,
       "tmnxDS3ChannelType": tmnxDS3ChannelType,
       "tmnxDS3ChannelFraming": tmnxDS3ChannelFraming,
       "tmnxDS3ChannelClockSource": tmnxDS3ChannelClockSource,
       "tmnxDS3ChannelChannelized": tmnxDS3ChannelChannelized,
       "tmnxDS3ChannelSubrateCSUMode": tmnxDS3ChannelSubrateCSUMode,
       "tmnxDS3ChannelSubrate": tmnxDS3ChannelSubrate,
       "tmnxDS3ChannelIdleCycleFlags": tmnxDS3ChannelIdleCycleFlags,
       "tmnxDS3ChannelLoopback": tmnxDS3ChannelLoopback,
       "tmnxDS3ChannelBitErrorInsertionRate": tmnxDS3ChannelBitErrorInsertionRate,
       "tmnxDS3ChannelBERTPattern": tmnxDS3ChannelBERTPattern,
       "tmnxDS3ChannelBERTDuration": tmnxDS3ChannelBERTDuration,
       "tmnxDS3ChannelMDLEicString": tmnxDS3ChannelMDLEicString,
       "tmnxDS3ChannelMDLLicString": tmnxDS3ChannelMDLLicString,
       "tmnxDS3ChannelMDLFicString": tmnxDS3ChannelMDLFicString,
       "tmnxDS3ChannelMDLUnitString": tmnxDS3ChannelMDLUnitString,
       "tmnxDS3ChannelMDLPfiString": tmnxDS3ChannelMDLPfiString,
       "tmnxDS3ChannelMDLPortString": tmnxDS3ChannelMDLPortString,
       "tmnxDS3ChannelMDLGenString": tmnxDS3ChannelMDLGenString,
       "tmnxDS3ChannelMDLMessageType": tmnxDS3ChannelMDLMessageType,
       "tmnxDS3ChannelFEACLoopRespond": tmnxDS3ChannelFEACLoopRespond,
       "tmnxDS3ChannelCRC": tmnxDS3ChannelCRC,
       "tmnxDS3ChannelMTU": tmnxDS3ChannelMTU,
       "tmnxDS3ChannelOperMTU": tmnxDS3ChannelOperMTU,
       "tmnxDS3ChannelReportAlarm": tmnxDS3ChannelReportAlarm,
       "tmnxDS3ChannelReportAlarmStatus": tmnxDS3ChannelReportAlarmStatus,
       "tmnxDS3ChannelLastChangeTime": tmnxDS3ChannelLastChangeTime,
       "tmnxDS3ChannelInFEACLoop": tmnxDS3ChannelInFEACLoop,
       "tmnxDS3ChannelMDLMonPortString": tmnxDS3ChannelMDLMonPortString,
       "tmnxDS3ChannelMDLMonGenString": tmnxDS3ChannelMDLMonGenString,
       "tmnxDS3ChannelBERTOperStatus": tmnxDS3ChannelBERTOperStatus,
       "tmnxDS3ChannelBERTSynched": tmnxDS3ChannelBERTSynched,
       "tmnxDS3ChannelBERTErrors": tmnxDS3ChannelBERTErrors,
       "tmnxDS3ChannelBERTTotalBits": tmnxDS3ChannelBERTTotalBits,
       "tmnxDS3ChannelScramble": tmnxDS3ChannelScramble,
       "tmnxDS3ChannelAcctPolicyId": tmnxDS3ChannelAcctPolicyId,
       "tmnxDS3ChannelCollectStats": tmnxDS3ChannelCollectStats,
       "tmnxDS3ChannelClockSyncState": tmnxDS3ChannelClockSyncState,
       "tmnxDS3ChannelClockMasterPortId": tmnxDS3ChannelClockMasterPortId,
       "tmnxDS1Table": tmnxDS1Table,
       "tmnxDS1Entry": tmnxDS1Entry,
       "tmnxDS1RowStatus": tmnxDS1RowStatus,
       "tmnxDS1Type": tmnxDS1Type,
       "tmnxDS1Framing": tmnxDS1Framing,
       "tmnxDS1IdleCycleFlags": tmnxDS1IdleCycleFlags,
       "tmnxDS1Loopback": tmnxDS1Loopback,
       "tmnxDS1InvertData": tmnxDS1InvertData,
       "tmnxDS1BitErrorInsertionRate": tmnxDS1BitErrorInsertionRate,
       "tmnxDS1BERTPattern": tmnxDS1BERTPattern,
       "tmnxDS1BERTDuration": tmnxDS1BERTDuration,
       "tmnxDS1ReportAlarm": tmnxDS1ReportAlarm,
       "tmnxDS1ReportAlarmStatus": tmnxDS1ReportAlarmStatus,
       "tmnxDS1LastChangeTime": tmnxDS1LastChangeTime,
       "tmnxDS1ClockSource": tmnxDS1ClockSource,
       "tmnxDS1BERTOperStatus": tmnxDS1BERTOperStatus,
       "tmnxDS1BERTSynched": tmnxDS1BERTSynched,
       "tmnxDS1BERTErrors": tmnxDS1BERTErrors,
       "tmnxDS1BERTTotalBits": tmnxDS1BERTTotalBits,
       "tmnxDS1RemoteLoopRespond": tmnxDS1RemoteLoopRespond,
       "tmnxDS1InRemoteLoop": tmnxDS1InRemoteLoop,
       "tmnxDS1InsertSingleBitError": tmnxDS1InsertSingleBitError,
       "tmnxDS1SignalMode": tmnxDS1SignalMode,
       "tmnxDS1ClockSyncState": tmnxDS1ClockSyncState,
       "tmnxDS1ClockMasterPortId": tmnxDS1ClockMasterPortId,
       "tmnxDS1BerSdThreshold": tmnxDS1BerSdThreshold,
       "tmnxDS1BerSfThreshold": tmnxDS1BerSfThreshold,
       "tmnxDS0ChanGroupTable": tmnxDS0ChanGroupTable,
       "tmnxDS0ChanGroupEntry": tmnxDS0ChanGroupEntry,
       "tmnxDS0ChanGroupRowStatus": tmnxDS0ChanGroupRowStatus,
       "tmnxDS0ChanGroupTimeSlots": tmnxDS0ChanGroupTimeSlots,
       "tmnxDS0ChanGroupSpeed": tmnxDS0ChanGroupSpeed,
       "tmnxDS0ChanGroupCRC": tmnxDS0ChanGroupCRC,
       "tmnxDS0ChanGroupMTU": tmnxDS0ChanGroupMTU,
       "tmnxDS0ChanGroupOperMTU": tmnxDS0ChanGroupOperMTU,
       "tmnxDS0ChanGroupLastChangeTime": tmnxDS0ChanGroupLastChangeTime,
       "tmnxDS0ChanGroupIdleCycleFlags": tmnxDS0ChanGroupIdleCycleFlags,
       "tmnxDS0ChanGroupScramble": tmnxDS0ChanGroupScramble,
       "tmnxDS0ChanGroupAcctPolicyId": tmnxDS0ChanGroupAcctPolicyId,
       "tmnxDS0ChanGroupCollectStats": tmnxDS0ChanGroupCollectStats,
       "tmnxDS0ChanGroupPayloadFillType": tmnxDS0ChanGroupPayloadFillType,
       "tmnxDS0ChanGroupPayloadPattern": tmnxDS0ChanGroupPayloadPattern,
       "tmnxDS0ChanGroupSignalFillType": tmnxDS0ChanGroupSignalFillType,
       "tmnxDS0ChanGroupSignalPattern": tmnxDS0ChanGroupSignalPattern,
       "tmnxBundleTable": tmnxBundleTable,
       "tmnxBundleEntry": tmnxBundleEntry,
       "tmnxBundleBundleID": tmnxBundleBundleID,
       "tmnxBundleRowStatus": tmnxBundleRowStatus,
       "tmnxBundleType": tmnxBundleType,
       "tmnxBundleMinimumLinks": tmnxBundleMinimumLinks,
       "tmnxBundleNumLinks": tmnxBundleNumLinks,
       "tmnxBundleNumActiveLinks": tmnxBundleNumActiveLinks,
       "tmnxBundleMRRU": tmnxBundleMRRU,
       "tmnxBundleOperMRRU": tmnxBundleOperMRRU,
       "tmnxBundlePeerMRRU": tmnxBundlePeerMRRU,
       "tmnxBundleOperMTU": tmnxBundleOperMTU,
       "tmnxBundleRedDiffDelay": tmnxBundleRedDiffDelay,
       "tmnxBundleRedDiffDelayAction": tmnxBundleRedDiffDelayAction,
       "tmnxBundleYellowDiffDelay": tmnxBundleYellowDiffDelay,
       "tmnxBundleShortSequence": tmnxBundleShortSequence,
       "tmnxBundleLastChangeTime": tmnxBundleLastChangeTime,
       "tmnxBundleFragmentThreshold": tmnxBundleFragmentThreshold,
       "tmnxBundleUpTime": tmnxBundleUpTime,
       "tmnxBundleInputDiscards": tmnxBundleInputDiscards,
       "tmnxBundlePrimaryMemberPortID": tmnxBundlePrimaryMemberPortID,
       "tmnxBundleLFI": tmnxBundleLFI,
       "tmnxBundleProtectedType": tmnxBundleProtectedType,
       "tmnxBundleParentBundle": tmnxBundleParentBundle,
       "tmnxBundleMemberTable": tmnxBundleMemberTable,
       "tmnxBundleMemberEntry": tmnxBundleMemberEntry,
       "tmnxBundleMemberRowStatus": tmnxBundleMemberRowStatus,
       "tmnxBundleMemberActive": tmnxBundleMemberActive,
       "tmnxBundleMemberDownReason": tmnxBundleMemberDownReason,
       "tmnxBundleMemberUpTime": tmnxBundleMemberUpTime,
       "tmnxPortToChannelTable": tmnxPortToChannelTable,
       "tmnxPortToChannelEntry": tmnxPortToChannelEntry,
       "tmnxChannelIdxString": tmnxChannelIdxString,
       "tmnxChannelPortID": tmnxChannelPortID,
       "tmnxPortIngrMdaQosStatTable": tmnxPortIngrMdaQosStatTable,
       "tmnxPortIngrMdaQosStatEntry": tmnxPortIngrMdaQosStatEntry,
       "tmnxPortIngrMdaQos00StatDropPkts": tmnxPortIngrMdaQos00StatDropPkts,
       "tmnxPortIngrMdaQos00StatDropOcts": tmnxPortIngrMdaQos00StatDropOcts,
       "tmnxPortIngrMdaQos01StatDropPkts": tmnxPortIngrMdaQos01StatDropPkts,
       "tmnxPortIngrMdaQos01StatDropOcts": tmnxPortIngrMdaQos01StatDropOcts,
       "tmnxPortIngrMdaQos02StatDropPkts": tmnxPortIngrMdaQos02StatDropPkts,
       "tmnxPortIngrMdaQos02StatDropOcts": tmnxPortIngrMdaQos02StatDropOcts,
       "tmnxPortIngrMdaQos03StatDropPkts": tmnxPortIngrMdaQos03StatDropPkts,
       "tmnxPortIngrMdaQos03StatDropOcts": tmnxPortIngrMdaQos03StatDropOcts,
       "tmnxPortIngrMdaQos04StatDropPkts": tmnxPortIngrMdaQos04StatDropPkts,
       "tmnxPortIngrMdaQos04StatDropOcts": tmnxPortIngrMdaQos04StatDropOcts,
       "tmnxPortIngrMdaQos05StatDropPkts": tmnxPortIngrMdaQos05StatDropPkts,
       "tmnxPortIngrMdaQos05StatDropOcts": tmnxPortIngrMdaQos05StatDropOcts,
       "tmnxPortIngrMdaQos06StatDropPkts": tmnxPortIngrMdaQos06StatDropPkts,
       "tmnxPortIngrMdaQos06StatDropOcts": tmnxPortIngrMdaQos06StatDropOcts,
       "tmnxPortIngrMdaQos07StatDropPkts": tmnxPortIngrMdaQos07StatDropPkts,
       "tmnxPortIngrMdaQos07StatDropOcts": tmnxPortIngrMdaQos07StatDropOcts,
       "tmnxPortIngrMdaQos08StatDropPkts": tmnxPortIngrMdaQos08StatDropPkts,
       "tmnxPortIngrMdaQos08StatDropOcts": tmnxPortIngrMdaQos08StatDropOcts,
       "tmnxPortIngrMdaQos09StatDropPkts": tmnxPortIngrMdaQos09StatDropPkts,
       "tmnxPortIngrMdaQos09StatDropOcts": tmnxPortIngrMdaQos09StatDropOcts,
       "tmnxPortIngrMdaQos10StatDropPkts": tmnxPortIngrMdaQos10StatDropPkts,
       "tmnxPortIngrMdaQos10StatDropOcts": tmnxPortIngrMdaQos10StatDropOcts,
       "tmnxPortIngrMdaQos11StatDropPkts": tmnxPortIngrMdaQos11StatDropPkts,
       "tmnxPortIngrMdaQos11StatDropOcts": tmnxPortIngrMdaQos11StatDropOcts,
       "tmnxPortIngrMdaQos12StatDropPkts": tmnxPortIngrMdaQos12StatDropPkts,
       "tmnxPortIngrMdaQos12StatDropOcts": tmnxPortIngrMdaQos12StatDropOcts,
       "tmnxPortIngrMdaQos13StatDropPkts": tmnxPortIngrMdaQos13StatDropPkts,
       "tmnxPortIngrMdaQos13StatDropOcts": tmnxPortIngrMdaQos13StatDropOcts,
       "tmnxPortIngrMdaQos14StatDropPkts": tmnxPortIngrMdaQos14StatDropPkts,
       "tmnxPortIngrMdaQos14StatDropOcts": tmnxPortIngrMdaQos14StatDropOcts,
       "tmnxPortIngrMdaQos15StatDropPkts": tmnxPortIngrMdaQos15StatDropPkts,
       "tmnxPortIngrMdaQos15StatDropOcts": tmnxPortIngrMdaQos15StatDropOcts,
       "tmnxSonetGroupTable": tmnxSonetGroupTable,
       "tmnxSonetGroupEntry": tmnxSonetGroupEntry,
       "tmnxSonetGroupType": tmnxSonetGroupType,
       "tmnxSonetGroupParentPortID": tmnxSonetGroupParentPortID,
       "tmnxSonetGroupChildType": tmnxSonetGroupChildType,
       "tmnxSonetGroupName": tmnxSonetGroupName,
       "tmnxPortScalarObjs": tmnxPortScalarObjs,
       "tmnxL4LoadBalancing": tmnxL4LoadBalancing,
       "tmnxCiscoHDLCTable": tmnxCiscoHDLCTable,
       "tmnxCiscoHDLCEntry": tmnxCiscoHDLCEntry,
       "tmnxCiscoHDLCKeepAliveInt": tmnxCiscoHDLCKeepAliveInt,
       "tmnxCiscoHDLCUpCount": tmnxCiscoHDLCUpCount,
       "tmnxCiscoHDLCDownCount": tmnxCiscoHDLCDownCount,
       "tmnxCiscoHDLCOperState": tmnxCiscoHDLCOperState,
       "tmnxBundleImaGrpTable": tmnxBundleImaGrpTable,
       "tmnxBundleImaGrpEntry": tmnxBundleImaGrpEntry,
       "tmnxBundleImaGrpLnkActTimer": tmnxBundleImaGrpLnkActTimer,
       "tmnxBundleImaGrpLnkDeactTimer": tmnxBundleImaGrpLnkDeactTimer,
       "tmnxBundleImaGrpSymmetryMode": tmnxBundleImaGrpSymmetryMode,
       "tmnxBundleImaGrpTxId": tmnxBundleImaGrpTxId,
       "tmnxBundleImaGrpRxId": tmnxBundleImaGrpRxId,
       "tmnxBundleImaGrpTxRefLnk": tmnxBundleImaGrpTxRefLnk,
       "tmnxBundleImaGrpRxRefLnk": tmnxBundleImaGrpRxRefLnk,
       "tmnxBundleImaGrpSmNeState": tmnxBundleImaGrpSmNeState,
       "tmnxBundleImaGrpSmFeState": tmnxBundleImaGrpSmFeState,
       "tmnxBundleImaGrpSmFailState": tmnxBundleImaGrpSmFailState,
       "tmnxBundleImaGrpSmDownSecs": tmnxBundleImaGrpSmDownSecs,
       "tmnxBundleImaGrpSmOperSecs": tmnxBundleImaGrpSmOperSecs,
       "tmnxBundleImaGrpAvailTxCR": tmnxBundleImaGrpAvailTxCR,
       "tmnxBundleImaGrpAvailRxCR": tmnxBundleImaGrpAvailRxCR,
       "tmnxBundleImaGrpNeFails": tmnxBundleImaGrpNeFails,
       "tmnxBundleImaGrpFeFails": tmnxBundleImaGrpFeFails,
       "tmnxBundleImaGrpTxIcpCells": tmnxBundleImaGrpTxIcpCells,
       "tmnxBundleImaGrpRxIcpCells": tmnxBundleImaGrpRxIcpCells,
       "tmnxBundleImaGrpErrorIcpCells": tmnxBundleImaGrpErrorIcpCells,
       "tmnxBundleImaGrpLostRxIcpCells": tmnxBundleImaGrpLostRxIcpCells,
       "tmnxBundleImaGrpTxOamLablVal": tmnxBundleImaGrpTxOamLablVal,
       "tmnxBundleImaGrpRxOamLablVal": tmnxBundleImaGrpRxOamLablVal,
       "tmnxBundleImaGrpAlphaValue": tmnxBundleImaGrpAlphaValue,
       "tmnxBundleImaGrpBetaValue": tmnxBundleImaGrpBetaValue,
       "tmnxBundleImaGrpGammaValue": tmnxBundleImaGrpGammaValue,
       "tmnxBundleImaGrpNeClockMode": tmnxBundleImaGrpNeClockMode,
       "tmnxBundleImaGrpFeClockMode": tmnxBundleImaGrpFeClockMode,
       "tmnxBundleImaGrpVersion": tmnxBundleImaGrpVersion,
       "tmnxBundleImaGrpMaxConfBw": tmnxBundleImaGrpMaxConfBw,
       "tmnxBundleImaGrpTestState": tmnxBundleImaGrpTestState,
       "tmnxBundleImaGrpTestMember": tmnxBundleImaGrpTestMember,
       "tmnxBundleImaGrpTestPattern": tmnxBundleImaGrpTestPattern,
       "tmnxBundleImaGrpDiffDelayMaxObs": tmnxBundleImaGrpDiffDelayMaxObs,
       "tmnxBundleImaGrpLeastDelayLink": tmnxBundleImaGrpLeastDelayLink,
       "tmnxBundleMemberImaTable": tmnxBundleMemberImaTable,
       "tmnxBundleMemberImaEntry": tmnxBundleMemberImaEntry,
       "tmnxBundleMemberImaNeTxState": tmnxBundleMemberImaNeTxState,
       "tmnxBundleMemberImaNeRxState": tmnxBundleMemberImaNeRxState,
       "tmnxBundleMemberImaFeTxState": tmnxBundleMemberImaFeTxState,
       "tmnxBundleMemberImaFeRxState": tmnxBundleMemberImaFeRxState,
       "tmnxBundleMemberImaNeRxFailState": tmnxBundleMemberImaNeRxFailState,
       "tmnxBundleMemberImaFeRxFailState": tmnxBundleMemberImaFeRxFailState,
       "tmnxBundleMemberImaTxLid": tmnxBundleMemberImaTxLid,
       "tmnxBundleMemberImaRxLid": tmnxBundleMemberImaRxLid,
       "tmnxBundleMemberImaViolations": tmnxBundleMemberImaViolations,
       "tmnxBundleMemberImaNeSevErrSecs": tmnxBundleMemberImaNeSevErrSecs,
       "tmnxBundleMemberImaFeSevErrSecs": tmnxBundleMemberImaFeSevErrSecs,
       "tmnxBundleMemberImaNeUnavailSecs": tmnxBundleMemberImaNeUnavailSecs,
       "tmnxBundleMemberImaFeUnavailSecs": tmnxBundleMemberImaFeUnavailSecs,
       "tmnxBundleMemberImaNeTxUnuseSecs": tmnxBundleMemberImaNeTxUnuseSecs,
       "tmnxBundleMemberImaNeRxUnuseSecs": tmnxBundleMemberImaNeRxUnuseSecs,
       "tmnxBundleMemberImaFeTxUnuseSecs": tmnxBundleMemberImaFeTxUnuseSecs,
       "tmnxBundleMemberImaFeRxUnuseSecs": tmnxBundleMemberImaFeRxUnuseSecs,
       "tmnxBundleMemberImaNeTxNumFails": tmnxBundleMemberImaNeTxNumFails,
       "tmnxBundleMemberImaNeRxNumFails": tmnxBundleMemberImaNeRxNumFails,
       "tmnxBundleMemberImaFeTxNumFails": tmnxBundleMemberImaFeTxNumFails,
       "tmnxBundleMemberImaFeRxNumFails": tmnxBundleMemberImaFeRxNumFails,
       "tmnxBundleMemberImaTxIcpCells": tmnxBundleMemberImaTxIcpCells,
       "tmnxBundleMemberImaRxIcpCells": tmnxBundleMemberImaRxIcpCells,
       "tmnxBundleMemberImaErrorIcpCells": tmnxBundleMemberImaErrorIcpCells,
       "tmnxBundleMemberImaLstRxIcpCells": tmnxBundleMemberImaLstRxIcpCells,
       "tmnxBundleMemberImaOifAnomalies": tmnxBundleMemberImaOifAnomalies,
       "tmnxBundleMemberImaRxTestState": tmnxBundleMemberImaRxTestState,
       "tmnxBundleMemberImaRxTestPattern": tmnxBundleMemberImaRxTestPattern,
       "tmnxBundleMemberImaRelDelay": tmnxBundleMemberImaRelDelay,
       "tmnxDS1PortTable": tmnxDS1PortTable,
       "tmnxDS1PortEntry": tmnxDS1PortEntry,
       "tmnxDS1PortBuildout": tmnxDS1PortBuildout,
       "tmnxDS1PortLastChangeTime": tmnxDS1PortLastChangeTime,
       "tmnxDS1PortType": tmnxDS1PortType,
       "tmnxDS1PortLineLength": tmnxDS1PortLineLength,
       "tmnxDS1PortLbo": tmnxDS1PortLbo,
       "tmnxDS1PortDbGain": tmnxDS1PortDbGain,
       "tmnxPortSchedOverrideTable": tmnxPortSchedOverrideTable,
       "tmnxPortSchedOverrideEntry": tmnxPortSchedOverrideEntry,
       "tmnxPortSchedOverrideRowStatus": tmnxPortSchedOverrideRowStatus,
       "tmnxPortSchedOverrideSchedName": tmnxPortSchedOverrideSchedName,
       "tmnxPortSchedOverrideLastChanged": tmnxPortSchedOverrideLastChanged,
       "tmnxPortSchedOverrideMaxRate": tmnxPortSchedOverrideMaxRate,
       "tmnxPortSchedOverrideLvl1PIR": tmnxPortSchedOverrideLvl1PIR,
       "tmnxPortSchedOverrideLvl1CIR": tmnxPortSchedOverrideLvl1CIR,
       "tmnxPortSchedOverrideLvl2PIR": tmnxPortSchedOverrideLvl2PIR,
       "tmnxPortSchedOverrideLvl2CIR": tmnxPortSchedOverrideLvl2CIR,
       "tmnxPortSchedOverrideLvl3PIR": tmnxPortSchedOverrideLvl3PIR,
       "tmnxPortSchedOverrideLvl3CIR": tmnxPortSchedOverrideLvl3CIR,
       "tmnxPortSchedOverrideLvl4PIR": tmnxPortSchedOverrideLvl4PIR,
       "tmnxPortSchedOverrideLvl4CIR": tmnxPortSchedOverrideLvl4CIR,
       "tmnxPortSchedOverrideLvl5PIR": tmnxPortSchedOverrideLvl5PIR,
       "tmnxPortSchedOverrideLvl5CIR": tmnxPortSchedOverrideLvl5CIR,
       "tmnxPortSchedOverrideLvl6PIR": tmnxPortSchedOverrideLvl6PIR,
       "tmnxPortSchedOverrideLvl6CIR": tmnxPortSchedOverrideLvl6CIR,
       "tmnxPortSchedOverrideLvl7PIR": tmnxPortSchedOverrideLvl7PIR,
       "tmnxPortSchedOverrideLvl7CIR": tmnxPortSchedOverrideLvl7CIR,
       "tmnxPortSchedOverrideLvl8PIR": tmnxPortSchedOverrideLvl8PIR,
       "tmnxPortSchedOverrideLvl8CIR": tmnxPortSchedOverrideLvl8CIR,
       "tmnxPortSchedOverrideFlags": tmnxPortSchedOverrideFlags,
       "tmnxBPGrpAssocTable": tmnxBPGrpAssocTable,
       "tmnxBPGrpAssocEntry": tmnxBPGrpAssocEntry,
       "tmnxBPGrpAssocWorkingBundleID": tmnxBPGrpAssocWorkingBundleID,
       "tmnxBPGrpAssocProtectBundleID": tmnxBPGrpAssocProtectBundleID,
       "tmnxBPGrpAssocActiveBundleID": tmnxBPGrpAssocActiveBundleID,
       "tmnxBundleMlpppTable": tmnxBundleMlpppTable,
       "tmnxBundleMlpppEntry": tmnxBundleMlpppEntry,
       "tmnxBundleMlpppEndpointID": tmnxBundleMlpppEndpointID,
       "tmnxBundleMlpppEndpointIDClass": tmnxBundleMlpppEndpointIDClass,
       "tmnxBundleMlpppClassCount": tmnxBundleMlpppClassCount,
       "tmnxBundleMlpppIngQoSProfId": tmnxBundleMlpppIngQoSProfId,
       "tmnxBundleMlpppEgrQoSProfId": tmnxBundleMlpppEgrQoSProfId,
       "tmnxDigitalDiagMonitorTable": tmnxDigitalDiagMonitorTable,
       "tmnxDigitalDiagMonitorEntry": tmnxDigitalDiagMonitorEntry,
       "tmnxDDMTemperature": tmnxDDMTemperature,
       "tmnxDDMTempLowWarning": tmnxDDMTempLowWarning,
       "tmnxDDMTempLowAlarm": tmnxDDMTempLowAlarm,
       "tmnxDDMTempHiWarning": tmnxDDMTempHiWarning,
       "tmnxDDMTempHiAlarm": tmnxDDMTempHiAlarm,
       "tmnxDDMSupplyVoltage": tmnxDDMSupplyVoltage,
       "tmnxDDMSupplyVoltageLowWarning": tmnxDDMSupplyVoltageLowWarning,
       "tmnxDDMSupplyVoltageLowAlarm": tmnxDDMSupplyVoltageLowAlarm,
       "tmnxDDMSupplyVoltageHiWarning": tmnxDDMSupplyVoltageHiWarning,
       "tmnxDDMSupplyVoltageHiAlarm": tmnxDDMSupplyVoltageHiAlarm,
       "tmnxDDMTxBiasCurrent": tmnxDDMTxBiasCurrent,
       "tmnxDDMTxBiasCurrentLowWarning": tmnxDDMTxBiasCurrentLowWarning,
       "tmnxDDMTxBiasCurrentLowAlarm": tmnxDDMTxBiasCurrentLowAlarm,
       "tmnxDDMTxBiasCurrentHiWarning": tmnxDDMTxBiasCurrentHiWarning,
       "tmnxDDMTxBiasCurrentHiAlarm": tmnxDDMTxBiasCurrentHiAlarm,
       "tmnxDDMTxOutputPower": tmnxDDMTxOutputPower,
       "tmnxDDMTxOutputPowerLowWarning": tmnxDDMTxOutputPowerLowWarning,
       "tmnxDDMTxOutputPowerLowAlarm": tmnxDDMTxOutputPowerLowAlarm,
       "tmnxDDMTxOutputPowerHiWarning": tmnxDDMTxOutputPowerHiWarning,
       "tmnxDDMTxOutputPowerHiAlarm": tmnxDDMTxOutputPowerHiAlarm,
       "tmnxDDMRxOpticalPower": tmnxDDMRxOpticalPower,
       "tmnxDDMRxOpticalPowerLowWarning": tmnxDDMRxOpticalPowerLowWarning,
       "tmnxDDMRxOpticalPowerLowAlarm": tmnxDDMRxOpticalPowerLowAlarm,
       "tmnxDDMRxOpticalPowerHiWarning": tmnxDDMRxOpticalPowerHiWarning,
       "tmnxDDMRxOpticalPowerHiAlarm": tmnxDDMRxOpticalPowerHiAlarm,
       "tmnxDDMRxOpticalPowerType": tmnxDDMRxOpticalPowerType,
       "tmnxDDMAux1": tmnxDDMAux1,
       "tmnxDDMAux1LowWarning": tmnxDDMAux1LowWarning,
       "tmnxDDMAux1LowAlarm": tmnxDDMAux1LowAlarm,
       "tmnxDDMAux1HiWarning": tmnxDDMAux1HiWarning,
       "tmnxDDMAux1HiAlarm": tmnxDDMAux1HiAlarm,
       "tmnxDDMAux1Type": tmnxDDMAux1Type,
       "tmnxDDMAux2": tmnxDDMAux2,
       "tmnxDDMAux2LowWarning": tmnxDDMAux2LowWarning,
       "tmnxDDMAux2LowAlarm": tmnxDDMAux2LowAlarm,
       "tmnxDDMAux2HiWarning": tmnxDDMAux2HiWarning,
       "tmnxDDMAux2HiAlarm": tmnxDDMAux2HiAlarm,
       "tmnxDDMAux2Type": tmnxDDMAux2Type,
       "tmnxDDMFailedThresholds": tmnxDDMFailedThresholds,
       "tmnxDDMExternallyCalibrated": tmnxDDMExternallyCalibrated,
       "tmnxDDMExtCalRxPower4": tmnxDDMExtCalRxPower4,
       "tmnxDDMExtCalRxPower3": tmnxDDMExtCalRxPower3,
       "tmnxDDMExtCalRxPower2": tmnxDDMExtCalRxPower2,
       "tmnxDDMExtCalRxPower1": tmnxDDMExtCalRxPower1,
       "tmnxDDMExtCalRxPower0": tmnxDDMExtCalRxPower0,
       "tmnxDDMExtCalTxLaserBiasSlope": tmnxDDMExtCalTxLaserBiasSlope,
       "tmnxDDMExtCalTxLaserBiasOffset": tmnxDDMExtCalTxLaserBiasOffset,
       "tmnxDDMExtCalTxPowerSlope": tmnxDDMExtCalTxPowerSlope,
       "tmnxDDMExtCalTxPowerOffset": tmnxDDMExtCalTxPowerOffset,
       "tmnxDDMExtCalTemperatureSlope": tmnxDDMExtCalTemperatureSlope,
       "tmnxDDMExtCalTemperatureOffset": tmnxDDMExtCalTemperatureOffset,
       "tmnxDDMExtCalVoltageSlope": tmnxDDMExtCalVoltageSlope,
       "tmnxDDMExtCalVoltageOffset": tmnxDDMExtCalVoltageOffset,
       "tmnxPortNotificationObjects": tmnxPortNotificationObjects,
       "tmnxPortNotifyPortId": tmnxPortNotifyPortId,
       "tmnxPortNotifySonetAlarmReason": tmnxPortNotifySonetAlarmReason,
       "tmnxPortNotifySonetPathAlarmReason": tmnxPortNotifySonetPathAlarmReason,
       "tmnxPortNotifyError": tmnxPortNotifyError,
       "tmnxPortNotifyDS3AlarmReason": tmnxPortNotifyDS3AlarmReason,
       "tmnxPortNotifyDS1AlarmReason": tmnxPortNotifyDS1AlarmReason,
       "tmnxPortNotifyBundleId": tmnxPortNotifyBundleId,
       "tmnxPortNotifyEtherAlarmReason": tmnxPortNotifyEtherAlarmReason,
       "tmnxDDMFailedObject": tmnxDDMFailedObject,
       "tmnxFRObjs": tmnxFRObjs,
       "tmnxFRDlcmiTable": tmnxFRDlcmiTable,
       "tmnxFRDlcmiEntry": tmnxFRDlcmiEntry,
       "tmnxFRDlcmiMode": tmnxFRDlcmiMode,
       "tmnxFRDlcmiN392Dce": tmnxFRDlcmiN392Dce,
       "tmnxFRDlcmiN393Dce": tmnxFRDlcmiN393Dce,
       "tmnxFRDlcmiT392Dce": tmnxFRDlcmiT392Dce,
       "tmnxFRDlcmiTxStatusEnqMsgs": tmnxFRDlcmiTxStatusEnqMsgs,
       "tmnxFRDlcmiRxStatusEnqMsgs": tmnxFRDlcmiRxStatusEnqMsgs,
       "tmnxFRDlcmiStatusEnqMsgTimeouts": tmnxFRDlcmiStatusEnqMsgTimeouts,
       "tmnxFRDlcmiTxStatusMsgs": tmnxFRDlcmiTxStatusMsgs,
       "tmnxFRDlcmiRxStatusMsgs": tmnxFRDlcmiRxStatusMsgs,
       "tmnxFRDlcmiStatusMsgTimeouts": tmnxFRDlcmiStatusMsgTimeouts,
       "tmnxFRDlcmiDiscardedMsgs": tmnxFRDlcmiDiscardedMsgs,
       "tmnxFRDlcmiInvRxSeqNumMsgs": tmnxFRDlcmiInvRxSeqNumMsgs,
       "tmnxQosAppObjs": tmnxQosAppObjs,
       "tmnxQosPoolAppTable": tmnxQosPoolAppTable,
       "tmnxQosPoolAppEntry": tmnxQosPoolAppEntry,
       "tmnxObjectType": tmnxObjectType,
       "tmnxObjectId": tmnxObjectId,
       "tmnxObjectAppType": tmnxObjectAppType,
       "tmnxObjectAppPool": tmnxObjectAppPool,
       "tmnxObjectAppPoolRowStatus": tmnxObjectAppPoolRowStatus,
       "tmnxObjectAppResvCbs": tmnxObjectAppResvCbs,
       "tmnxObjectAppSlopePolicy": tmnxObjectAppSlopePolicy,
       "tmnxObjectAppPoolSize": tmnxObjectAppPoolSize,
       "tmnxATMObjs": tmnxATMObjs,
       "tmnxATMIntfTable": tmnxATMIntfTable,
       "tmnxATMIntfEntry": tmnxATMIntfEntry,
       "tmnxATMIntfCellFormat": tmnxATMIntfCellFormat,
       "tmnxATMIntfMinVpValue": tmnxATMIntfMinVpValue,
       "tmnxATMIntfMapping": tmnxATMIntfMapping,
       "tmnxPortStatsObjs": tmnxPortStatsObjs,
       "tmnxPortNetIngressStatsTable": tmnxPortNetIngressStatsTable,
       "tmnxPortNetIngressStatsEntry": tmnxPortNetIngressStatsEntry,
       "tmnxPortNetIngressQueueIndex": tmnxPortNetIngressQueueIndex,
       "tmnxPortNetIngressFwdInProfPkts": tmnxPortNetIngressFwdInProfPkts,
       "tmnxPortNetIngressFwdOutProfPkts": tmnxPortNetIngressFwdOutProfPkts,
       "tmnxPortNetIngressFwdInProfOcts": tmnxPortNetIngressFwdInProfOcts,
       "tmnxPortNetIngressFwdOutProfOcts": tmnxPortNetIngressFwdOutProfOcts,
       "tmnxPortNetIngressDroInProfPkts": tmnxPortNetIngressDroInProfPkts,
       "tmnxPortNetIngressDroOutProfPkts": tmnxPortNetIngressDroOutProfPkts,
       "tmnxPortNetIngressDroInProfOcts": tmnxPortNetIngressDroInProfOcts,
       "tmnxPortNetIngressDroOutProfOcts": tmnxPortNetIngressDroOutProfOcts,
       "tmnxPortNetEgressStatsTable": tmnxPortNetEgressStatsTable,
       "tmnxPortNetEgressStatsEntry": tmnxPortNetEgressStatsEntry,
       "tmnxPortNetEgressQueueIndex": tmnxPortNetEgressQueueIndex,
       "tmnxPortNetEgressFwdInProfPkts": tmnxPortNetEgressFwdInProfPkts,
       "tmnxPortNetEgressFwdOutProfPkts": tmnxPortNetEgressFwdOutProfPkts,
       "tmnxPortNetEgressFwdInProfOcts": tmnxPortNetEgressFwdInProfOcts,
       "tmnxPortNetEgressFwdOutProfOcts": tmnxPortNetEgressFwdOutProfOcts,
       "tmnxPortNetEgressDroInProfPkts": tmnxPortNetEgressDroInProfPkts,
       "tmnxPortNetEgressDroOutProfPkts": tmnxPortNetEgressDroOutProfPkts,
       "tmnxPortNetEgressDroInProfOcts": tmnxPortNetEgressDroInProfOcts,
       "tmnxPortNetEgressDroOutProfOcts": tmnxPortNetEgressDroOutProfOcts,
       "tmnxCiscoHDLCStatsTable": tmnxCiscoHDLCStatsTable,
       "tmnxCiscoHDLCStatsEntry": tmnxCiscoHDLCStatsEntry,
       "tmnxCiscoHDLCDiscardStatInPkts": tmnxCiscoHDLCDiscardStatInPkts,
       "tmnxCiscoHDLCDiscardStatOutPkts": tmnxCiscoHDLCDiscardStatOutPkts,
       "tmnxCiscoHDLCStatInPkts": tmnxCiscoHDLCStatInPkts,
       "tmnxCiscoHDLCStatOutPkts": tmnxCiscoHDLCStatOutPkts,
       "tmnxCiscoHDLCStatInOctets": tmnxCiscoHDLCStatInOctets,
       "tmnxCiscoHDLCStatOutOctets": tmnxCiscoHDLCStatOutOctets,
       "tmnxMcMlpppStatsTable": tmnxMcMlpppStatsTable,
       "tmnxMcMlpppStatsEntry": tmnxMcMlpppStatsEntry,
       "tmnxMcMlpppClassIndex": tmnxMcMlpppClassIndex,
       "tmnxMcMlpppStatsIngressOct": tmnxMcMlpppStatsIngressOct,
       "tmnxMcMlpppStatsIngressPkt": tmnxMcMlpppStatsIngressPkt,
       "tmnxMcMlpppStatsIngressErrPkt": tmnxMcMlpppStatsIngressErrPkt,
       "tmnxMcMlpppStatsEgressOct": tmnxMcMlpppStatsEgressOct,
       "tmnxMcMlpppStatsEgressPkt": tmnxMcMlpppStatsEgressPkt,
       "tmnxMcMlpppStatsEgressErrPkt": tmnxMcMlpppStatsEgressErrPkt,
       "tmnxPortNotifyPrefix": tmnxPortNotifyPrefix,
       "tmnxPortNotification": tmnxPortNotification,
       "tmnxEqOobPortFailure": tmnxEqOobPortFailure,
       "tmnxEqPortFailure": tmnxEqPortFailure,
       "tmnxQosServiceDegraded": tmnxQosServiceDegraded,
       "tmnxEqPortSonetAlarm": tmnxEqPortSonetAlarm,
       "tmnxEqPortSonetAlarmClear": tmnxEqPortSonetAlarmClear,
       "tmnxEqPortSonetPathAlarm": tmnxEqPortSonetPathAlarm,
       "tmnxEqPortSonetPathAlarmClear": tmnxEqPortSonetPathAlarmClear,
       "tmnxEqPortSFPInserted": tmnxEqPortSFPInserted,
       "tmnxEqPortSFPRemoved": tmnxEqPortSFPRemoved,
       "tmnxEqPortWrongSFP": tmnxEqPortWrongSFP,
       "tmnxEqPortSFPCorrupted": tmnxEqPortSFPCorrupted,
       "tmnxPortNotifyBerSdTca": tmnxPortNotifyBerSdTca,
       "tmnxPortNotifyBerSfTca": tmnxPortNotifyBerSfTca,
       "tmnxEqPortError": tmnxEqPortError,
       "tmnxEqPortDS3Alarm": tmnxEqPortDS3Alarm,
       "tmnxEqPortDS3AlarmClear": tmnxEqPortDS3AlarmClear,
       "tmnxEqPortDS1Alarm": tmnxEqPortDS1Alarm,
       "tmnxEqPortDS1AlarmClear": tmnxEqPortDS1AlarmClear,
       "tmnxEqPortBndlYellowDiffExceeded": tmnxEqPortBndlYellowDiffExceeded,
       "tmnxEqPortBndlRedDiffExceeded": tmnxEqPortBndlRedDiffExceeded,
       "tmnxEqPortBndlBadEndPtDiscr": tmnxEqPortBndlBadEndPtDiscr,
       "tmnxEqPortEtherAlarm": tmnxEqPortEtherAlarm,
       "tmnxEqPortEtherAlarmClear": tmnxEqPortEtherAlarmClear,
       "tmnxDS1E1LoopbackStarted": tmnxDS1E1LoopbackStarted,
       "tmnxDS1E1LoopbackStopped": tmnxDS1E1LoopbackStopped,
       "tmnxDS3E3LoopbackStarted": tmnxDS3E3LoopbackStarted,
       "tmnxDS3E3LoopbackStopped": tmnxDS3E3LoopbackStopped,
       "tmnxSonetSDHLoopbackStarted": tmnxSonetSDHLoopbackStarted,
       "tmnxSonetSDHLoopbackStopped": tmnxSonetSDHLoopbackStopped,
       "tmnxEqPortEtherLoopDetected": tmnxEqPortEtherLoopDetected,
       "tmnxEqPortEtherLoopCleared": tmnxEqPortEtherLoopCleared,
       "tmnxEqPortSpeedCfgNotCompatible": tmnxEqPortSpeedCfgNotCompatible,
       "tmnxEqPortDuplexCfgNotCompatible": tmnxEqPortDuplexCfgNotCompatible,
       "tmnxEqPortIngressRateCfgNotCompatible": tmnxEqPortIngressRateCfgNotCompatible,
       "tmnxEqDigitalDiagMonitorFailure": tmnxEqDigitalDiagMonitorFailure,
       "tmnxEqPortSFPStatusFailure": tmnxEqPortSFPStatusFailure}
)
