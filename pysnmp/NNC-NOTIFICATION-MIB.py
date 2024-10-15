# SNMP MIB module (NNC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:13 2024
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

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtensions")

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

nncExtNotif = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpssAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class StringType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class ParameterStringType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class NBNodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              42,
              43,
              44,
              45,
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
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("nd1630SX", 64),
          ("nd2902", 61),
          ("nd3600", 5),
          ("nd3600PLUS", 57),
          ("nd3606IDSU", 62),
          ("nd36110-20", 68),
          ("nd36110-8", 67),
          ("nd36111-24", 69),
          ("nd36111-80", 70),
          ("nd3612", 6),
          ("nd36120", 22),
          ("nd36125", 65),
          ("nd36130", 63),
          ("nd36150", 24),
          ("nd36160", 66),
          ("nd36170", 35),
          ("nd36177", 76),
          ("nd3620", 34),
          ("nd3620Rtr", 54),
          ("nd3624", 7),
          ("nd3630", 8),
          ("nd3645DS3", 17),
          ("nd3645E3", 23),
          ("nd3645PU", 14),
          ("nd3645SU", 13),
          ("nd3664", 25),
          ("nd4601", 2),
          ("nd4601A", 12),
          ("nd46020", 3),
          ("nd46020CN", 32),
          ("nd46020DN", 31),
          ("nd46020RT", 33),
          ("nd48020", 42),
          ("nd5601", 9),
          ("nd5602", 10),
          ("nd5610", 11),
          ("ndA3606D", 20),
          ("ndA3606V", 19),
          ("ndConnectExec", 21),
          ("ndDACSII", 27),
          ("ndDACSIIProxyAgent", 29),
          ("ndDCS31", 43),
          ("ndDCS33", 44),
          ("ndDEXCS1L", 28),
          ("ndDEXCS1S", 16),
          ("ndEmGeneric", 60),
          ("ndEmMgr", 59),
          ("ndFRATM", 45),
          ("ndGeneric", 15),
          ("ndGenericDCS", 30),
          ("ndIAG", 71),
          ("ndISDNAccess", 58),
          ("ndLAG", 72),
          ("ndMNSC", 73),
          ("ndMNSC-CN", 75),
          ("ndMNSC-DN", 74),
          ("ndMVNMatm", 56),
          ("ndStatsCollector", 55),
          ("ndTAP", 4),
          ("ndTDAX100", 26))
    )



class SysDescrType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )



class AlmPriorityType(Integer32, TextualConvention):
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
        *(("critical", 4),
          ("diagn", 1),
          ("major", 3),
          ("minor", 2))
    )



class AlmInfoType(StringType, TextualConvention):
    status = "current"


class TTFaultLocationType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )



class TTPriorityType(Integer32, TextualConvention):
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("warning", 1))
    )



class TTFaultStatusType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 10),
          ("cleared", 5),
          ("custom", 7),
          ("dcsNode", 9),
          ("isolate", 2),
          ("maintenanc", 3),
          ("recovery", 1),
          ("tdaxNode", 8),
          ("user", 6),
          ("verify", 4))
    )



class TThardwareFaultType(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("activitySwitch", 14),
          ("cableFailure", 7),
          ("cableProblem", 18),
          ("cdFailure", 5),
          ("devFailure", 4),
          ("devProblem", 17),
          ("modemIsBusted", 9),
          ("nodeProblem", 15),
          ("nvmIntegrityError", 11),
          ("psFailure", 1),
          ("ramIntegrityError", 12),
          ("reconcileProblem", 16),
          ("ringGenFailure", 8),
          ("romIntegrityError", 13),
          ("slotIsEmpty", 10),
          ("tailEndCircGone", 6),
          ("wrongCdInSlot", 2),
          ("wrongModOnCd", 3))
    )



class TTsoftwareFaultType(Integer32, TextualConvention):
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
        *(("alarmProblem", 6),
          ("alarmQOverflow", 1),
          ("busiedOut", 7),
          ("maximumHops", 8),
          ("notConfigLocally", 4),
          ("swDownloadProblem", 9),
          ("unsupportedCd", 2),
          ("unsupportedMod", 3),
          ("unsupportedStatus", 5))
    )



class TTcommFaultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cannotTalkToNode", 1)
    )



class TTuserFaultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createdBySystem", 2),
          ("createdByUser", 1))
    )



class TTcustomNodeFaultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customNodeLog", 2),
          ("gfcAlarm", 1))
    )



class TTlanNodeFaultType(Integer32, TextualConvention):
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
        *(("circuitGroup", 4),
          ("interfaceRow", 2),
          ("lanPath", 5),
          ("lanTrap", 3),
          ("systemTable", 1))
    )



class TTconnectExecFaultType(Integer32, TextualConvention):
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
        *(("abnormalShutdown", 6),
          ("chgsrvQOverflow", 5),
          ("mibOutOfSync", 1),
          ("noReload", 2),
          ("pathProblem", 4),
          ("reloadAbort", 8),
          ("reloadMIB", 3),
          ("updateStarted", 7))
    )



class TTtDaxNodeFaultType(Integer32, TextualConvention):
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
        *(("cardAlarm", 3),
          ("nodeAlarm", 1),
          ("portAlarm", 4),
          ("shelfAlarm", 2))
    )



class TTdcsNodeFaultType(Integer32, TextualConvention):
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
        *(("cardAlarm", 3),
          ("nodeAlarm", 1),
          ("portAlarm", 4),
          ("shelfAlarm", 2))
    )



class TTadminFaultType(Integer32, TextualConvention):
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
        *(("invalidLicenseKey", 3),
          ("licenseViolation", 2),
          ("passwdViolation", 1))
    )



class TTssdhRingFaultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upsrProblem", 1)
    )



class TTextNodeFaultType(Integer32, TextualConvention):
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
        *(("cardAlarm", 3),
          ("deviceAlarm", 4),
          ("fanAlarm", 5),
          ("nodeAlarm", 1),
          ("shelfAlarm", 2))
    )



class TTcongestionFaultType(Integer32, TextualConvention):
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
        *(("mild", 2),
          ("none", 1),
          ("severe", 3))
    )



# MIB Managed Objects in the order of their OIDs

_NncExtNotifObjects_ObjectIdentity = ObjectIdentity
nncExtNotifObjects = _NncExtNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1)
)
_NncNodeInfo_Object = MibTable
nncNodeInfo = _NncNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1)
)
if mibBuilder.loadTexts:
    nncNodeInfo.setStatus("current")
_NncNodeIPAddr_Type = IpAddress
_NncNodeIPAddr_Object = MibTableColumn
nncNodeIPAddr = _NncNodeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 1),
    _NncNodeIPAddr_Type()
)
nncNodeIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNodeIPAddr.setStatus("current")
_NncNodeCPSSAddr_Type = CpssAddress
_NncNodeCPSSAddr_Object = MibTableColumn
nncNodeCPSSAddr = _NncNodeCPSSAddr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 2),
    _NncNodeCPSSAddr_Type()
)
nncNodeCPSSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNodeCPSSAddr.setStatus("current")
_NncNodeType_Type = NBNodeType
_NncNodeType_Object = MibTableColumn
nncNodeType = _NncNodeType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 3),
    _NncNodeType_Type()
)
nncNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNodeType.setStatus("current")
_NncNodeFullName_Type = StringType
_NncNodeFullName_Object = MibTableColumn
nncNodeFullName = _NncNodeFullName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 1, 4),
    _NncNodeFullName_Type()
)
nncNodeFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncNodeFullName.setStatus("current")
_NncAlmInfo_Object = MibTable
nncAlmInfo = _NncAlmInfo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2)
)
if mibBuilder.loadTexts:
    nncAlmInfo.setStatus("current")
_NncAlmDateAndTime_Type = TimeTicks
_NncAlmDateAndTime_Object = MibTableColumn
nncAlmDateAndTime = _NncAlmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 1),
    _NncAlmDateAndTime_Type()
)
nncAlmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAlmDateAndTime.setStatus("current")
_NncAlmPriority_Type = AlmPriorityType
_NncAlmPriority_Object = MibTableColumn
nncAlmPriority = _NncAlmPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 2),
    _NncAlmPriority_Type()
)
nncAlmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAlmPriority.setStatus("current")
_NncAlmText_Type = StringType
_NncAlmText_Object = MibTableColumn
nncAlmText = _NncAlmText_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 2, 3),
    _NncAlmText_Type()
)
nncAlmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAlmText.setStatus("current")
_NncTTInfo_Object = MibTable
nncTTInfo = _NncTTInfo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3)
)
if mibBuilder.loadTexts:
    nncTTInfo.setStatus("current")
_NncTTDateAndTime_Type = TimeTicks
_NncTTDateAndTime_Object = MibTableColumn
nncTTDateAndTime = _NncTTDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 1),
    _NncTTDateAndTime_Type()
)
nncTTDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTDateAndTime.setStatus("current")
_NncTTPriority_Type = TTPriorityType
_NncTTPriority_Object = MibTableColumn
nncTTPriority = _NncTTPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 2),
    _NncTTPriority_Type()
)
nncTTPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTPriority.setStatus("current")
_NncTTFaultLocation_Type = TTFaultLocationType
_NncTTFaultLocation_Object = MibTableColumn
nncTTFaultLocation = _NncTTFaultLocation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 3),
    _NncTTFaultLocation_Type()
)
nncTTFaultLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTFaultLocation.setStatus("current")
_NncTTFaultStatus_Type = TTFaultStatusType
_NncTTFaultStatus_Object = MibTableColumn
nncTTFaultStatus = _NncTTFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 4),
    _NncTTFaultStatus_Type()
)
nncTTFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTFaultStatus.setStatus("current")
_NncTTOwner_Type = StringType
_NncTTOwner_Object = MibTableColumn
nncTTOwner = _NncTTOwner_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 3, 5),
    _NncTTOwner_Type()
)
nncTTOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTOwner.setStatus("current")
_NncTTFaultType_Object = MibTable
nncTTFaultType = _NncTTFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4)
)
if mibBuilder.loadTexts:
    nncTTFaultType.setStatus("current")
_NncTThardwareFaultType_Type = TThardwareFaultType
_NncTThardwareFaultType_Object = MibTableColumn
nncTThardwareFaultType = _NncTThardwareFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 1),
    _NncTThardwareFaultType_Type()
)
nncTThardwareFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTThardwareFaultType.setStatus("current")
_NncTTsoftwareFaultType_Type = TTsoftwareFaultType
_NncTTsoftwareFaultType_Object = MibTableColumn
nncTTsoftwareFaultType = _NncTTsoftwareFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 2),
    _NncTTsoftwareFaultType_Type()
)
nncTTsoftwareFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTsoftwareFaultType.setStatus("current")
_NncTTcommFaultType_Type = TTcommFaultType
_NncTTcommFaultType_Object = MibTableColumn
nncTTcommFaultType = _NncTTcommFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 3),
    _NncTTcommFaultType_Type()
)
nncTTcommFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTcommFaultType.setStatus("current")
_NncTTuserFaultType_Type = TTuserFaultType
_NncTTuserFaultType_Object = MibTableColumn
nncTTuserFaultType = _NncTTuserFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 4),
    _NncTTuserFaultType_Type()
)
nncTTuserFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTuserFaultType.setStatus("current")
_NncTTcustomNodeFaultType_Type = TTcustomNodeFaultType
_NncTTcustomNodeFaultType_Object = MibTableColumn
nncTTcustomNodeFaultType = _NncTTcustomNodeFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 5),
    _NncTTcustomNodeFaultType_Type()
)
nncTTcustomNodeFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTcustomNodeFaultType.setStatus("current")
_NncTTlanNodeFaultType_Type = TTlanNodeFaultType
_NncTTlanNodeFaultType_Object = MibTableColumn
nncTTlanNodeFaultType = _NncTTlanNodeFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 6),
    _NncTTlanNodeFaultType_Type()
)
nncTTlanNodeFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTlanNodeFaultType.setStatus("current")
_NncTTconnectExecFaultType_Type = TTconnectExecFaultType
_NncTTconnectExecFaultType_Object = MibTableColumn
nncTTconnectExecFaultType = _NncTTconnectExecFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 7),
    _NncTTconnectExecFaultType_Type()
)
nncTTconnectExecFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTconnectExecFaultType.setStatus("current")
_NncTTtDaxNodeFaultType_Type = TTtDaxNodeFaultType
_NncTTtDaxNodeFaultType_Object = MibTableColumn
nncTTtDaxNodeFaultType = _NncTTtDaxNodeFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 8),
    _NncTTtDaxNodeFaultType_Type()
)
nncTTtDaxNodeFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTtDaxNodeFaultType.setStatus("current")
_NncTTdcsNodeFaultType_Type = TTdcsNodeFaultType
_NncTTdcsNodeFaultType_Object = MibTableColumn
nncTTdcsNodeFaultType = _NncTTdcsNodeFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 9),
    _NncTTdcsNodeFaultType_Type()
)
nncTTdcsNodeFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTdcsNodeFaultType.setStatus("current")
_NncTTadminFaultType_Type = TTadminFaultType
_NncTTadminFaultType_Object = MibTableColumn
nncTTadminFaultType = _NncTTadminFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 10),
    _NncTTadminFaultType_Type()
)
nncTTadminFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTadminFaultType.setStatus("current")
_NncTTssdhRingFaultType_Type = TTssdhRingFaultType
_NncTTssdhRingFaultType_Object = MibTableColumn
nncTTssdhRingFaultType = _NncTTssdhRingFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 11),
    _NncTTssdhRingFaultType_Type()
)
nncTTssdhRingFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTssdhRingFaultType.setStatus("current")
_NncTTextNodeFaultType_Type = TTextNodeFaultType
_NncTTextNodeFaultType_Object = MibTableColumn
nncTTextNodeFaultType = _NncTTextNodeFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 12),
    _NncTTextNodeFaultType_Type()
)
nncTTextNodeFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTextNodeFaultType.setStatus("current")
_NncTTcongestionFaultType_Type = TTcongestionFaultType
_NncTTcongestionFaultType_Object = MibTableColumn
nncTTcongestionFaultType = _NncTTcongestionFaultType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 4, 13),
    _NncTTcongestionFaultType_Type()
)
nncTTcongestionFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncTTcongestionFaultType.setStatus("current")
_NncHeartBeatInfo_Object = MibTable
nncHeartBeatInfo = _NncHeartBeatInfo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5)
)
if mibBuilder.loadTexts:
    nncHeartBeatInfo.setStatus("current")
_NncSysDescr_Type = SysDescrType
_NncSysDescr_Object = MibTableColumn
nncSysDescr = _NncSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5, 1),
    _NncSysDescr_Type()
)
nncSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSysDescr.setStatus("current")
_NncSysUpTime_Type = TimeTicks
_NncSysUpTime_Object = MibTableColumn
nncSysUpTime = _NncSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 1, 5, 2),
    _NncSysUpTime_Type()
)
nncSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSysUpTime.setStatus("current")
_NncExtNotifType_ObjectIdentity = ObjectIdentity
nncExtNotifType = _NncExtNotifType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2)
)
_NncExtNotifAlarmType_ObjectIdentity = ObjectIdentity
nncExtNotifAlarmType = _NncExtNotifAlarmType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1)
)
_NncExtNotifAlarmType_v1Trap_ObjectIdentity = ObjectIdentity
nncExtNotifAlarmType_v1Trap = _NncExtNotifAlarmType_v1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1, 0)
)
_NncExtNotifTroubleTicketType_ObjectIdentity = ObjectIdentity
nncExtNotifTroubleTicketType = _NncExtNotifTroubleTicketType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2)
)
_NncExtNotifTroubleTicketType_v1Trap_ObjectIdentity = ObjectIdentity
nncExtNotifTroubleTicketType_v1Trap = _NncExtNotifTroubleTicketType_v1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0)
)
_NncExtNotifHeartBeatType_ObjectIdentity = ObjectIdentity
nncExtNotifHeartBeatType = _NncExtNotifHeartBeatType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3)
)
_NncExtNotifHeartBeatType_v1Trap_ObjectIdentity = ObjectIdentity
nncExtNotifHeartBeatType_v1Trap = _NncExtNotifHeartBeatType_v1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3, 0)
)
_NncExtNotifGroups_ObjectIdentity = ObjectIdentity
nncExtNotifGroups = _NncExtNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 3)
)
_NncExtNotifCompliances_ObjectIdentity = ObjectIdentity
nncExtNotifCompliances = _NncExtNotifCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 4)
)

# Managed Objects groups

nncExtNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 3, 1)
)
nncExtNotifGroup.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncAlmInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTFaultType"))
)
if mibBuilder.loadTexts:
    nncExtNotifGroup.setStatus("current")


# Notification objects

nncExtNotifAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 1, 0, 1)
)
nncExtNotifAlarm.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncAlmInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifAlarm.setStatus(
        "current"
    )

nncExtNotifHardwareTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 2)
)
nncExtNotifHardwareTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTThardwareFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifHardwareTT.setStatus(
        "current"
    )

nncExtNotifSoftwareTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 3)
)
nncExtNotifSoftwareTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTsoftwareFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifSoftwareTT.setStatus(
        "current"
    )

nncExtNotifCommTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 4)
)
nncExtNotifCommTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTcommFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifCommTT.setStatus(
        "current"
    )

nncExtNotifUserTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 5)
)
nncExtNotifUserTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTuserFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifUserTT.setStatus(
        "current"
    )

nncExtNotifCustomNodeTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 6)
)
nncExtNotifCustomNodeTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTcustomNodeFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifCustomNodeTT.setStatus(
        "current"
    )

nncExtNotifLanNodeTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 7)
)
nncExtNotifLanNodeTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTlanNodeFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifLanNodeTT.setStatus(
        "current"
    )

nncExtNotifConnectExecTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 8)
)
nncExtNotifConnectExecTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTconnectExecFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifConnectExecTT.setStatus(
        "current"
    )

nncExtNotifTDaxNodeTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 9)
)
nncExtNotifTDaxNodeTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTtDaxNodeFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifTDaxNodeTT.setStatus(
        "current"
    )

nncExtNotifAdminTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 10)
)
nncExtNotifAdminTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTadminFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifAdminTT.setStatus(
        "current"
    )

nncExtNotifSsdhRingTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 11)
)
nncExtNotifSsdhRingTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTssdhRingFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifSsdhRingTT.setStatus(
        "current"
    )

nncExtNotifExternalNodeTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 12)
)
nncExtNotifExternalNodeTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTextNodeFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifExternalNodeTT.setStatus(
        "current"
    )

nncExtNotifCongestionTT = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 2, 0, 13)
)
nncExtNotifCongestionTT.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncNodeInfo"),
        ("NNC-NOTIFICATION-MIB", "nncTTcongestionFaultType"),
        ("NNC-NOTIFICATION-MIB", "nncTTInfo"))
)
if mibBuilder.loadTexts:
    nncExtNotifCongestionTT.setStatus(
        "current"
    )

nncExtNotifHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 2, 3, 0, 1)
)
nncExtNotifHeartBeat.setObjects(
      *(("NNC-NOTIFICATION-MIB", "nncSysDescr"),
        ("NNC-NOTIFICATION-MIB", "nncSysUpTime"))
)
if mibBuilder.loadTexts:
    nncExtNotifHeartBeat.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

nncExtNotifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 44, 4, 1)
)
if mibBuilder.loadTexts:
    nncExtNotifCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-NOTIFICATION-MIB",
    **{"CpssAddress": CpssAddress,
       "StringType": StringType,
       "ParameterStringType": ParameterStringType,
       "NBNodeType": NBNodeType,
       "SysDescrType": SysDescrType,
       "AlmPriorityType": AlmPriorityType,
       "AlmInfoType": AlmInfoType,
       "TTFaultLocationType": TTFaultLocationType,
       "TTPriorityType": TTPriorityType,
       "TTFaultStatusType": TTFaultStatusType,
       "TThardwareFaultType": TThardwareFaultType,
       "TTsoftwareFaultType": TTsoftwareFaultType,
       "TTcommFaultType": TTcommFaultType,
       "TTuserFaultType": TTuserFaultType,
       "TTcustomNodeFaultType": TTcustomNodeFaultType,
       "TTlanNodeFaultType": TTlanNodeFaultType,
       "TTconnectExecFaultType": TTconnectExecFaultType,
       "TTtDaxNodeFaultType": TTtDaxNodeFaultType,
       "TTdcsNodeFaultType": TTdcsNodeFaultType,
       "TTadminFaultType": TTadminFaultType,
       "TTssdhRingFaultType": TTssdhRingFaultType,
       "TTextNodeFaultType": TTextNodeFaultType,
       "TTcongestionFaultType": TTcongestionFaultType,
       "nncExtNotif": nncExtNotif,
       "nncExtNotifObjects": nncExtNotifObjects,
       "nncNodeInfo": nncNodeInfo,
       "nncNodeIPAddr": nncNodeIPAddr,
       "nncNodeCPSSAddr": nncNodeCPSSAddr,
       "nncNodeType": nncNodeType,
       "nncNodeFullName": nncNodeFullName,
       "nncAlmInfo": nncAlmInfo,
       "nncAlmDateAndTime": nncAlmDateAndTime,
       "nncAlmPriority": nncAlmPriority,
       "nncAlmText": nncAlmText,
       "nncTTInfo": nncTTInfo,
       "nncTTDateAndTime": nncTTDateAndTime,
       "nncTTPriority": nncTTPriority,
       "nncTTFaultLocation": nncTTFaultLocation,
       "nncTTFaultStatus": nncTTFaultStatus,
       "nncTTOwner": nncTTOwner,
       "nncTTFaultType": nncTTFaultType,
       "nncTThardwareFaultType": nncTThardwareFaultType,
       "nncTTsoftwareFaultType": nncTTsoftwareFaultType,
       "nncTTcommFaultType": nncTTcommFaultType,
       "nncTTuserFaultType": nncTTuserFaultType,
       "nncTTcustomNodeFaultType": nncTTcustomNodeFaultType,
       "nncTTlanNodeFaultType": nncTTlanNodeFaultType,
       "nncTTconnectExecFaultType": nncTTconnectExecFaultType,
       "nncTTtDaxNodeFaultType": nncTTtDaxNodeFaultType,
       "nncTTdcsNodeFaultType": nncTTdcsNodeFaultType,
       "nncTTadminFaultType": nncTTadminFaultType,
       "nncTTssdhRingFaultType": nncTTssdhRingFaultType,
       "nncTTextNodeFaultType": nncTTextNodeFaultType,
       "nncTTcongestionFaultType": nncTTcongestionFaultType,
       "nncHeartBeatInfo": nncHeartBeatInfo,
       "nncSysDescr": nncSysDescr,
       "nncSysUpTime": nncSysUpTime,
       "nncExtNotifType": nncExtNotifType,
       "nncExtNotifAlarmType": nncExtNotifAlarmType,
       "nncExtNotifAlarmType-v1Trap": nncExtNotifAlarmType_v1Trap,
       "nncExtNotifAlarm": nncExtNotifAlarm,
       "nncExtNotifTroubleTicketType": nncExtNotifTroubleTicketType,
       "nncExtNotifTroubleTicketType-v1Trap": nncExtNotifTroubleTicketType_v1Trap,
       "nncExtNotifHardwareTT": nncExtNotifHardwareTT,
       "nncExtNotifSoftwareTT": nncExtNotifSoftwareTT,
       "nncExtNotifCommTT": nncExtNotifCommTT,
       "nncExtNotifUserTT": nncExtNotifUserTT,
       "nncExtNotifCustomNodeTT": nncExtNotifCustomNodeTT,
       "nncExtNotifLanNodeTT": nncExtNotifLanNodeTT,
       "nncExtNotifConnectExecTT": nncExtNotifConnectExecTT,
       "nncExtNotifTDaxNodeTT": nncExtNotifTDaxNodeTT,
       "nncExtNotifAdminTT": nncExtNotifAdminTT,
       "nncExtNotifSsdhRingTT": nncExtNotifSsdhRingTT,
       "nncExtNotifExternalNodeTT": nncExtNotifExternalNodeTT,
       "nncExtNotifCongestionTT": nncExtNotifCongestionTT,
       "nncExtNotifHeartBeatType": nncExtNotifHeartBeatType,
       "nncExtNotifHeartBeatType-v1Trap": nncExtNotifHeartBeatType_v1Trap,
       "nncExtNotifHeartBeat": nncExtNotifHeartBeat,
       "nncExtNotifGroups": nncExtNotifGroups,
       "nncExtNotifGroup": nncExtNotifGroup,
       "nncExtNotifCompliances": nncExtNotifCompliances,
       "nncExtNotifCompliance": nncExtNotifCompliance}
)
