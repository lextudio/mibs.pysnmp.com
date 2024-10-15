# SNMP MIB module (JUNIPER-SOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SOAM-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:14 2024
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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(IEEE8021VlanIndex,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021VlanIndex",
    "ieee802dot1mibs")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxSoamPmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78)
)
jnxSoamPmMib.setRevisions(
        ("2012-01-13 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021PriorityValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class JnxSoamTcTestPatternType(Integer32, TextualConvention):
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
        *(("null", 1),
          ("nullCrc32", 2),
          ("prbs", 3),
          ("prbsCrc32", 4))
    )



class JnxSoamTcDataPatternType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onesPattern", 2),
          ("zeroPattern", 1))
    )



class JnxSoamTcOperationTimeType(Integer32, TextualConvention):
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
        *(("fixed", 4),
          ("immediate", 2),
          ("none", 1),
          ("relative", 3))
    )



# MIB Managed Objects in the order of their OIDs

_JnxSoamPmNotifications_ObjectIdentity = ObjectIdentity
jnxSoamPmNotifications = _JnxSoamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0)
)
_JnxSoamPmMibObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmMibObjects = _JnxSoamPmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1)
)
_JnxSoamPmMep_ObjectIdentity = ObjectIdentity
jnxSoamPmMep = _JnxSoamPmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1)
)
_JnxSoamPmMepTable_Object = MibTable
jnxSoamPmMepTable = _JnxSoamPmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSoamPmMepTable.setStatus("current")
_JnxSoamPmMepEntry_Object = MibTableRow
jnxSoamPmMepEntry = _JnxSoamPmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSoamPmMepEntry.setStatus("current")
_JnxSoamPmMepOperNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_JnxSoamPmMepOperNextIndex_Object = MibTableColumn
jnxSoamPmMepOperNextIndex = _JnxSoamPmMepOperNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 1),
    _JnxSoamPmMepOperNextIndex_Type()
)
jnxSoamPmMepOperNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepOperNextIndex.setStatus("current")


class _JnxSoamPmMepLmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepLmSingleEndedResponder based on TruthValue"""


_JnxSoamPmMepLmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepLmSingleEndedResponder = _JnxSoamPmMepLmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 2),
    _JnxSoamPmMepLmSingleEndedResponder_Type()
)
jnxSoamPmMepLmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepLmSingleEndedResponder.setStatus("current")


class _JnxSoamPmMepSlmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepSlmSingleEndedResponder based on TruthValue"""


_JnxSoamPmMepSlmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepSlmSingleEndedResponder = _JnxSoamPmMepSlmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 3),
    _JnxSoamPmMepSlmSingleEndedResponder_Type()
)
jnxSoamPmMepSlmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepSlmSingleEndedResponder.setStatus("current")


class _JnxSoamPmMepDmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepDmSingleEndedResponder based on TruthValue"""


_JnxSoamPmMepDmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepDmSingleEndedResponder = _JnxSoamPmMepDmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 4),
    _JnxSoamPmMepDmSingleEndedResponder_Type()
)
jnxSoamPmMepDmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepDmSingleEndedResponder.setStatus("current")
_JnxSoamPmLmObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmLmObjects = _JnxSoamPmLmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2)
)
_JnxSoamLmCfgTable_Object = MibTable
jnxSoamLmCfgTable = _JnxSoamLmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxSoamLmCfgTable.setStatus("current")
_JnxSoamLmCfgEntry_Object = MibTableRow
jnxSoamLmCfgEntry = _JnxSoamLmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1)
)
jnxSoamLmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmCfgEntry.setStatus("current")


class _JnxSoamLmCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamLmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSoamLmCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgIndex_Object = MibTableColumn
jnxSoamLmCfgIndex = _JnxSoamLmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 1),
    _JnxSoamLmCfgIndex_Type()
)
jnxSoamLmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgIndex.setStatus("current")


class _JnxSoamLmCfgType_Type(Integer32):
    """Custom type jnxSoamLmCfgType based on Integer32"""
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
        *(("lmCcm", 3),
          ("lmLmm", 1),
          ("lmSlm", 2))
    )


_JnxSoamLmCfgType_Type.__name__ = "Integer32"
_JnxSoamLmCfgType_Object = MibTableColumn
jnxSoamLmCfgType = _JnxSoamLmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 2),
    _JnxSoamLmCfgType_Type()
)
jnxSoamLmCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgType.setStatus("current")


class _JnxSoamLmCfgVersion_Type(Unsigned32):
    """Custom type jnxSoamLmCfgVersion based on Unsigned32"""
    defaultValue = 0


_JnxSoamLmCfgVersion_Object = MibTableColumn
jnxSoamLmCfgVersion = _JnxSoamLmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 3),
    _JnxSoamLmCfgVersion_Type()
)
jnxSoamLmCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgVersion.setStatus("current")


class _JnxSoamLmCfgEnabled_Type(TruthValue):
    """Custom type jnxSoamLmCfgEnabled based on TruthValue"""


_JnxSoamLmCfgEnabled_Object = MibTableColumn
jnxSoamLmCfgEnabled = _JnxSoamLmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 4),
    _JnxSoamLmCfgEnabled_Type()
)
jnxSoamLmCfgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgEnabled.setStatus("current")


class _JnxSoamLmCfgMeasurementEnable_Type(Bits):
    """Custom type jnxSoamLmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bBackwardAvgFlr", 9),
          ("bBackwardMaxFlr", 8),
          ("bBackwardMinFlr", 7),
          ("bBackwardReceivedFrames", 6),
          ("bBackwardTransmitedFrames", 5),
          ("bForwardAvgFlr", 4),
          ("bForwardMaxFlr", 3),
          ("bForwardMinFlr", 2),
          ("bForwardReceivedFrames", 1),
          ("bForwardTransmitedFrames", 0),
          ("bMeasuredStatsBackwardMeasuredFlr", 27),
          ("bMeasuredStatsForwardMeasuredFlr", 26),
          ("bSoamPdusReceived", 11),
          ("bSoamPdusSent", 10))
    )

_JnxSoamLmCfgMeasurementEnable_Type.__name__ = "Bits"
_JnxSoamLmCfgMeasurementEnable_Object = MibTableColumn
jnxSoamLmCfgMeasurementEnable = _JnxSoamLmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 5),
    _JnxSoamLmCfgMeasurementEnable_Type()
)
jnxSoamLmCfgMeasurementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMeasurementEnable.setStatus("current")


class _JnxSoamLmCfgMessagePeriod_Type(Integer32):
    """Custom type jnxSoamLmCfgMessagePeriod based on Integer32"""
    defaultValue = 1000


_JnxSoamLmCfgMessagePeriod_Object = MibTableColumn
jnxSoamLmCfgMessagePeriod = _JnxSoamLmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 6),
    _JnxSoamLmCfgMessagePeriod_Type()
)
jnxSoamLmCfgMessagePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMessagePeriod.setUnits("ms")
_JnxSoamLmCfgPriority_Type = IEEE8021PriorityValue
_JnxSoamLmCfgPriority_Object = MibTableColumn
jnxSoamLmCfgPriority = _JnxSoamLmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 7),
    _JnxSoamLmCfgPriority_Type()
)
jnxSoamLmCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgPriority.setStatus("current")


class _JnxSoamLmCfgFrameSize_Type(Unsigned32):
    """Custom type jnxSoamLmCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_JnxSoamLmCfgFrameSize_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgFrameSize_Object = MibTableColumn
jnxSoamLmCfgFrameSize = _JnxSoamLmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 8),
    _JnxSoamLmCfgFrameSize_Type()
)
jnxSoamLmCfgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFrameSize.setUnits("bytes")


class _JnxSoamLmCfgDataPattern_Type(JnxSoamTcDataPatternType):
    """Custom type jnxSoamLmCfgDataPattern based on JnxSoamTcDataPatternType"""


_JnxSoamLmCfgDataPattern_Object = MibTableColumn
jnxSoamLmCfgDataPattern = _JnxSoamLmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 9),
    _JnxSoamLmCfgDataPattern_Type()
)
jnxSoamLmCfgDataPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDataPattern.setStatus("current")


class _JnxSoamLmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type jnxSoamLmCfgTestTlvIncluded based on TruthValue"""


_JnxSoamLmCfgTestTlvIncluded_Object = MibTableColumn
jnxSoamLmCfgTestTlvIncluded = _JnxSoamLmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 10),
    _JnxSoamLmCfgTestTlvIncluded_Type()
)
jnxSoamLmCfgTestTlvIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgTestTlvIncluded.setStatus("current")


class _JnxSoamLmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):
    """Custom type jnxSoamLmCfgTestTlvPattern based on JnxSoamTcTestPatternType"""


_JnxSoamLmCfgTestTlvPattern_Object = MibTableColumn
jnxSoamLmCfgTestTlvPattern = _JnxSoamLmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 11),
    _JnxSoamLmCfgTestTlvPattern_Type()
)
jnxSoamLmCfgTestTlvPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgTestTlvPattern.setStatus("current")


class _JnxSoamLmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type jnxSoamLmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamLmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgNumIntervalsStored_Object = MibTableColumn
jnxSoamLmCfgNumIntervalsStored = _JnxSoamLmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 12),
    _JnxSoamLmCfgNumIntervalsStored_Type()
)
jnxSoamLmCfgNumIntervalsStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgNumIntervalsStored.setStatus("current")


class _JnxSoamLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type jnxSoamLmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_JnxSoamLmCfgDestMepId_Object = MibTableColumn
jnxSoamLmCfgDestMepId = _JnxSoamLmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 13),
    _JnxSoamLmCfgDestMepId_Type()
)
jnxSoamLmCfgDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDestMepId.setStatus("current")


class _JnxSoamLmCfgDestIsMepId_Type(TruthValue):
    """Custom type jnxSoamLmCfgDestIsMepId based on TruthValue"""


_JnxSoamLmCfgDestIsMepId_Object = MibTableColumn
jnxSoamLmCfgDestIsMepId = _JnxSoamLmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 14),
    _JnxSoamLmCfgDestIsMepId_Type()
)
jnxSoamLmCfgDestIsMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDestIsMepId.setStatus("current")


class _JnxSoamLmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamLmCfgStartTimeType based on JnxSoamTcOperationTimeType"""


_JnxSoamLmCfgStartTimeType_Object = MibTableColumn
jnxSoamLmCfgStartTimeType = _JnxSoamLmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 15),
    _JnxSoamLmCfgStartTimeType_Type()
)
jnxSoamLmCfgStartTimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgStartTimeType.setStatus("current")


class _JnxSoamLmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type jnxSoamLmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_JnxSoamLmCfgFixedStartDateAndTime_Object = MibTableColumn
jnxSoamLmCfgFixedStartDateAndTime = _JnxSoamLmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 16),
    _JnxSoamLmCfgFixedStartDateAndTime_Type()
)
jnxSoamLmCfgFixedStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFixedStartDateAndTime.setStatus("current")


class _JnxSoamLmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type jnxSoamLmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_JnxSoamLmCfgRelativeStartTime_Object = MibTableColumn
jnxSoamLmCfgRelativeStartTime = _JnxSoamLmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 17),
    _JnxSoamLmCfgRelativeStartTime_Type()
)
jnxSoamLmCfgRelativeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRelativeStartTime.setStatus("current")


class _JnxSoamLmCfgRepetitionTime_Type(Unsigned32):
    """Custom type jnxSoamLmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_JnxSoamLmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgRepetitionTime_Object = MibTableColumn
jnxSoamLmCfgRepetitionTime = _JnxSoamLmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 18),
    _JnxSoamLmCfgRepetitionTime_Type()
)
jnxSoamLmCfgRepetitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRepetitionTime.setUnits("seconds")


class _JnxSoamLmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type jnxSoamLmCfgAlignMeasurementIntervals based on TruthValue"""


_JnxSoamLmCfgAlignMeasurementIntervals_Object = MibTableColumn
jnxSoamLmCfgAlignMeasurementIntervals = _JnxSoamLmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 19),
    _JnxSoamLmCfgAlignMeasurementIntervals_Type()
)
jnxSoamLmCfgAlignMeasurementIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementIntervals.setStatus("current")


class _JnxSoamLmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_JnxSoamLmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAlignMeasurementOffset_Object = MibTableColumn
jnxSoamLmCfgAlignMeasurementOffset = _JnxSoamLmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 20),
    _JnxSoamLmCfgAlignMeasurementOffset_Type()
)
jnxSoamLmCfgAlignMeasurementOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementOffset.setUnits("minutes")


class _JnxSoamLmCfgSessionType_Type(OctetString):
    """Custom type jnxSoamLmCfgSessionType based on OctetString"""
    defaultValue = OctetString("proactive")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamLmCfgSessionType_Type.__name__ = "OctetString"
_JnxSoamLmCfgSessionType_Object = MibTableColumn
jnxSoamLmCfgSessionType = _JnxSoamLmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 21),
    _JnxSoamLmCfgSessionType_Type()
)
jnxSoamLmCfgSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgSessionType.setStatus("current")


class _JnxSoamLmCfgSessionStatus_Type(OctetString):
    """Custom type jnxSoamLmCfgSessionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_JnxSoamLmCfgSessionStatus_Type.__name__ = "OctetString"
_JnxSoamLmCfgSessionStatus_Object = MibTableColumn
jnxSoamLmCfgSessionStatus = _JnxSoamLmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 22),
    _JnxSoamLmCfgSessionStatus_Type()
)
jnxSoamLmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgSessionStatus.setStatus("current")


class _JnxSoamLmCfgHistoryClear_Type(TruthValue):
    """Custom type jnxSoamLmCfgHistoryClear based on TruthValue"""


_JnxSoamLmCfgHistoryClear_Object = MibTableColumn
jnxSoamLmCfgHistoryClear = _JnxSoamLmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 23),
    _JnxSoamLmCfgHistoryClear_Type()
)
jnxSoamLmCfgHistoryClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgHistoryClear.setStatus("current")
_JnxSoamLmCfgRowStatus_Type = RowStatus
_JnxSoamLmCfgRowStatus_Object = MibTableColumn
jnxSoamLmCfgRowStatus = _JnxSoamLmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 24),
    _JnxSoamLmCfgRowStatus_Type()
)
jnxSoamLmCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRowStatus.setStatus("current")
_JnxSoamLmMeasuredStatsTable_Object = MibTable
jnxSoamLmMeasuredStatsTable = _JnxSoamLmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsTable.setStatus("current")
_JnxSoamLmMeasuredStatsEntry_Object = MibTableRow
jnxSoamLmMeasuredStatsEntry = _JnxSoamLmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1)
)
jnxSoamLmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsEntry.setStatus("current")


class _JnxSoamLmMeasuredStatsForwardFlr_Type(Unsigned32):
    """Custom type jnxSoamLmMeasuredStatsForwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmMeasuredStatsForwardFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmMeasuredStatsForwardFlr_Object = MibTableColumn
jnxSoamLmMeasuredStatsForwardFlr = _JnxSoamLmMeasuredStatsForwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 1),
    _JnxSoamLmMeasuredStatsForwardFlr_Type()
)
jnxSoamLmMeasuredStatsForwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsForwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsForwardFlr.setUnits("milli-percent")


class _JnxSoamLmMeasuredStatsBackwardFlr_Type(Unsigned32):
    """Custom type jnxSoamLmMeasuredStatsBackwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmMeasuredStatsBackwardFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmMeasuredStatsBackwardFlr_Object = MibTableColumn
jnxSoamLmMeasuredStatsBackwardFlr = _JnxSoamLmMeasuredStatsBackwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 2),
    _JnxSoamLmMeasuredStatsBackwardFlr_Type()
)
jnxSoamLmMeasuredStatsBackwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsBackwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsBackwardFlr.setUnits("milli-percent")
_JnxSoamLmCurrentStatsTable_Object = MibTable
jnxSoamLmCurrentStatsTable = _JnxSoamLmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsTable.setStatus("current")
_JnxSoamLmCurrentStatsEntry_Object = MibTableRow
jnxSoamLmCurrentStatsEntry = _JnxSoamLmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1)
)
jnxSoamLmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsEntry.setStatus("current")
_JnxSoamLmCurrentStatsIndex_Type = Unsigned32
_JnxSoamLmCurrentStatsIndex_Object = MibTableColumn
jnxSoamLmCurrentStatsIndex = _JnxSoamLmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 1),
    _JnxSoamLmCurrentStatsIndex_Type()
)
jnxSoamLmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsIndex.setStatus("current")
_JnxSoamLmCurrentStatsStartTime_Type = DateAndTime
_JnxSoamLmCurrentStatsStartTime_Object = MibTableColumn
jnxSoamLmCurrentStatsStartTime = _JnxSoamLmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 2),
    _JnxSoamLmCurrentStatsStartTime_Type()
)
jnxSoamLmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsStartTime.setStatus("current")
_JnxSoamLmCurrentStatsElapsedTime_Type = TimeInterval
_JnxSoamLmCurrentStatsElapsedTime_Object = MibTableColumn
jnxSoamLmCurrentStatsElapsedTime = _JnxSoamLmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 3),
    _JnxSoamLmCurrentStatsElapsedTime_Type()
)
jnxSoamLmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsElapsedTime.setStatus("current")
_JnxSoamLmCurrentStatsSuspect_Type = TruthValue
_JnxSoamLmCurrentStatsSuspect_Object = MibTableColumn
jnxSoamLmCurrentStatsSuspect = _JnxSoamLmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 4),
    _JnxSoamLmCurrentStatsSuspect_Type()
)
jnxSoamLmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSuspect.setStatus("current")
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardTransmittedFrames = _JnxSoamLmCurrentStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 5),
    _JnxSoamLmCurrentStatsForwardTransmittedFrames_Type()
)
jnxSoamLmCurrentStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardTransmittedFrames.setStatus("current")
_JnxSoamLmCurrentStatsForwardReceivedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsForwardReceivedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardReceivedFrames = _JnxSoamLmCurrentStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 6),
    _JnxSoamLmCurrentStatsForwardReceivedFrames_Type()
)
jnxSoamLmCurrentStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardReceivedFrames.setStatus("current")


class _JnxSoamLmCurrentStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardMinFlr = _JnxSoamLmCurrentStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 7),
    _JnxSoamLmCurrentStatsForwardMinFlr_Type()
)
jnxSoamLmCurrentStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardMaxFlr = _JnxSoamLmCurrentStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 8),
    _JnxSoamLmCurrentStatsForwardMaxFlr_Type()
)
jnxSoamLmCurrentStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardAvgFlr = _JnxSoamLmCurrentStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 9),
    _JnxSoamLmCurrentStatsForwardAvgFlr_Type()
)
jnxSoamLmCurrentStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardTransmittedFrames = _JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 10),
    _JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type()
)
jnxSoamLmCurrentStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardTransmittedFrames.setStatus("current")
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardReceivedFrames = _JnxSoamLmCurrentStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 11),
    _JnxSoamLmCurrentStatsBackwardReceivedFrames_Type()
)
jnxSoamLmCurrentStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardReceivedFrames.setStatus("current")


class _JnxSoamLmCurrentStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardMinFlr = _JnxSoamLmCurrentStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 12),
    _JnxSoamLmCurrentStatsBackwardMinFlr_Type()
)
jnxSoamLmCurrentStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardMaxFlr = _JnxSoamLmCurrentStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 13),
    _JnxSoamLmCurrentStatsBackwardMaxFlr_Type()
)
jnxSoamLmCurrentStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardAvgFlr = _JnxSoamLmCurrentStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 14),
    _JnxSoamLmCurrentStatsBackwardAvgFlr_Type()
)
jnxSoamLmCurrentStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmCurrentStatsSoamPdusSent_Type = Gauge32
_JnxSoamLmCurrentStatsSoamPdusSent_Object = MibTableColumn
jnxSoamLmCurrentStatsSoamPdusSent = _JnxSoamLmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 15),
    _JnxSoamLmCurrentStatsSoamPdusSent_Type()
)
jnxSoamLmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSoamPdusSent.setStatus("current")
_JnxSoamLmCurrentStatsSoamPdusReceived_Type = Gauge32
_JnxSoamLmCurrentStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamLmCurrentStatsSoamPdusReceived = _JnxSoamLmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 16),
    _JnxSoamLmCurrentStatsSoamPdusReceived_Type()
)
jnxSoamLmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSoamPdusReceived.setStatus("current")
_JnxSoamLmHistoryStatsTable_Object = MibTable
jnxSoamLmHistoryStatsTable = _JnxSoamLmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsTable.setStatus("current")
_JnxSoamLmHistoryStatsEntry_Object = MibTableRow
jnxSoamLmHistoryStatsEntry = _JnxSoamLmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1)
)
jnxSoamLmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsEntry.setStatus("current")
_JnxSoamLmHistoryStatsIndex_Type = Unsigned32
_JnxSoamLmHistoryStatsIndex_Object = MibTableColumn
jnxSoamLmHistoryStatsIndex = _JnxSoamLmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 1),
    _JnxSoamLmHistoryStatsIndex_Type()
)
jnxSoamLmHistoryStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsIndex.setStatus("current")
_JnxSoamLmHistoryStatsEndTime_Type = DateAndTime
_JnxSoamLmHistoryStatsEndTime_Object = MibTableColumn
jnxSoamLmHistoryStatsEndTime = _JnxSoamLmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 2),
    _JnxSoamLmHistoryStatsEndTime_Type()
)
jnxSoamLmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsEndTime.setStatus("current")
_JnxSoamLmHistoryStatsElapsedTime_Type = TimeInterval
_JnxSoamLmHistoryStatsElapsedTime_Object = MibTableColumn
jnxSoamLmHistoryStatsElapsedTime = _JnxSoamLmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 3),
    _JnxSoamLmHistoryStatsElapsedTime_Type()
)
jnxSoamLmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsElapsedTime.setStatus("current")
_JnxSoamLmHistoryStatsSuspect_Type = TruthValue
_JnxSoamLmHistoryStatsSuspect_Object = MibTableColumn
jnxSoamLmHistoryStatsSuspect = _JnxSoamLmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 4),
    _JnxSoamLmHistoryStatsSuspect_Type()
)
jnxSoamLmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSuspect.setStatus("current")
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardTransmittedFrames = _JnxSoamLmHistoryStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 5),
    _JnxSoamLmHistoryStatsForwardTransmittedFrames_Type()
)
jnxSoamLmHistoryStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardTransmittedFrames.setStatus("current")
_JnxSoamLmHistoryStatsForwardReceivedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsForwardReceivedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardReceivedFrames = _JnxSoamLmHistoryStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 6),
    _JnxSoamLmHistoryStatsForwardReceivedFrames_Type()
)
jnxSoamLmHistoryStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardReceivedFrames.setStatus("current")


class _JnxSoamLmHistoryStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardMinFlr = _JnxSoamLmHistoryStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 7),
    _JnxSoamLmHistoryStatsForwardMinFlr_Type()
)
jnxSoamLmHistoryStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardMaxFlr = _JnxSoamLmHistoryStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 8),
    _JnxSoamLmHistoryStatsForwardMaxFlr_Type()
)
jnxSoamLmHistoryStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardAvgFlr = _JnxSoamLmHistoryStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 9),
    _JnxSoamLmHistoryStatsForwardAvgFlr_Type()
)
jnxSoamLmHistoryStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardTransmittedFrames = _JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 10),
    _JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type()
)
jnxSoamLmHistoryStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardTransmittedFrames.setStatus("current")
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardReceivedFrames = _JnxSoamLmHistoryStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 11),
    _JnxSoamLmHistoryStatsBackwardReceivedFrames_Type()
)
jnxSoamLmHistoryStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardReceivedFrames.setStatus("current")


class _JnxSoamLmHistoryStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardMinFlr = _JnxSoamLmHistoryStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 12),
    _JnxSoamLmHistoryStatsBackwardMinFlr_Type()
)
jnxSoamLmHistoryStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardMaxFlr = _JnxSoamLmHistoryStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 13),
    _JnxSoamLmHistoryStatsBackwardMaxFlr_Type()
)
jnxSoamLmHistoryStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardAvgFlr = _JnxSoamLmHistoryStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 14),
    _JnxSoamLmHistoryStatsBackwardAvgFlr_Type()
)
jnxSoamLmHistoryStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmHistoryStatsSoamPdusSent_Type = Gauge32
_JnxSoamLmHistoryStatsSoamPdusSent_Object = MibTableColumn
jnxSoamLmHistoryStatsSoamPdusSent = _JnxSoamLmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 15),
    _JnxSoamLmHistoryStatsSoamPdusSent_Type()
)
jnxSoamLmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSoamPdusSent.setStatus("current")
_JnxSoamLmHistoryStatsSoamPdusReceived_Type = Gauge32
_JnxSoamLmHistoryStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamLmHistoryStatsSoamPdusReceived = _JnxSoamLmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 16),
    _JnxSoamLmHistoryStatsSoamPdusReceived_Type()
)
jnxSoamLmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSoamPdusReceived.setStatus("current")
_JnxSoamLmThresholdCfgTable_Object = MibTable
jnxSoamLmThresholdCfgTable = _JnxSoamLmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgTable.setStatus("current")
_JnxSoamLmThresholdCfgEntry_Object = MibTableRow
jnxSoamLmThresholdCfgEntry = _JnxSoamLmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1)
)
jnxSoamLmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgEntry.setStatus("current")


class _JnxSoamLmThresholdCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSoamLmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgIndex_Object = MibTableColumn
jnxSoamLmThresholdCfgIndex = _JnxSoamLmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 1),
    _JnxSoamLmThresholdCfgIndex_Type()
)
jnxSoamLmThresholdCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgIndex.setStatus("current")


class _JnxSoamLmThresholdCfgEnable_Type(Bits):
    """Custom type jnxSoamLmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bJnxSoamLmAvgFlrBackwardThreshold", 5),
          ("bJnxSoamLmAvgFlrForwardThreshold", 2),
          ("bJnxSoamLmMaxFlrBackwardThreshold", 4),
          ("bJnxSoamLmMaxFlrForwardThreshold", 1),
          ("bJnxSoamLmMeasuredFlrBackwardThreshold", 3),
          ("bJnxSoamLmMeasuredFlrForwardThreshold", 0))
    )

_JnxSoamLmThresholdCfgEnable_Type.__name__ = "Bits"
_JnxSoamLmThresholdCfgEnable_Object = MibTableColumn
jnxSoamLmThresholdCfgEnable = _JnxSoamLmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 2),
    _JnxSoamLmThresholdCfgEnable_Type()
)
jnxSoamLmThresholdCfgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgEnable.setStatus("current")


class _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgAvgFlrForwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object = MibTableColumn
jnxSoamLmThresholdCfgAvgFlrForwardThreshold = _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 3),
    _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type()
)
jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setUnits("milli-percent")


class _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgAvgFlrBackwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object = MibTableColumn
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold = _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 4),
    _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type()
)
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setUnits("milli-percent")
_JnxSoamLmThresholdCfgRowStatus_Type = RowStatus
_JnxSoamLmThresholdCfgRowStatus_Object = MibTableColumn
jnxSoamLmThresholdCfgRowStatus = _JnxSoamLmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 5),
    _JnxSoamLmThresholdCfgRowStatus_Type()
)
jnxSoamLmThresholdCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgRowStatus.setStatus("current")
_JnxSoamPmDmObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmDmObjects = _JnxSoamPmDmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3)
)
_JnxSoamDmCfgTable_Object = MibTable
jnxSoamDmCfgTable = _JnxSoamDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgTable.setStatus("current")
_JnxSoamDmCfgEntry_Object = MibTableRow
jnxSoamDmCfgEntry = _JnxSoamDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1)
)
jnxSoamDmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgEntry.setStatus("current")


class _JnxSoamDmCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamDmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSoamDmCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgIndex_Object = MibTableColumn
jnxSoamDmCfgIndex = _JnxSoamDmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 1),
    _JnxSoamDmCfgIndex_Type()
)
jnxSoamDmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgIndex.setStatus("current")


class _JnxSoamDmCfgType_Type(Integer32):
    """Custom type jnxSoamDmCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dm1DmRx", 3),
          ("dm1DmTx", 2),
          ("dmDmm", 1))
    )


_JnxSoamDmCfgType_Type.__name__ = "Integer32"
_JnxSoamDmCfgType_Object = MibTableColumn
jnxSoamDmCfgType = _JnxSoamDmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 2),
    _JnxSoamDmCfgType_Type()
)
jnxSoamDmCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgType.setStatus("current")


class _JnxSoamDmCfgVersion_Type(Unsigned32):
    """Custom type jnxSoamDmCfgVersion based on Unsigned32"""
    defaultValue = 0


_JnxSoamDmCfgVersion_Object = MibTableColumn
jnxSoamDmCfgVersion = _JnxSoamDmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 3),
    _JnxSoamDmCfgVersion_Type()
)
jnxSoamDmCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgVersion.setStatus("current")


class _JnxSoamDmCfgEnabled_Type(TruthValue):
    """Custom type jnxSoamDmCfgEnabled based on TruthValue"""


_JnxSoamDmCfgEnabled_Object = MibTableColumn
jnxSoamDmCfgEnabled = _JnxSoamDmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 4),
    _JnxSoamDmCfgEnabled_Type()
)
jnxSoamDmCfgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgEnabled.setStatus("current")


class _JnxSoamDmCfgMeasurementEnable_Type(Bits):
    """Custom type jnxSoamDmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bFrameDelayBackwardAvg", 13),
          ("bFrameDelayBackwardBins", 10),
          ("bFrameDelayBackwardMax", 12),
          ("bFrameDelayBackwardMin", 11),
          ("bFrameDelayForwardAvg", 9),
          ("bFrameDelayForwardBins", 6),
          ("bFrameDelayForwardMax", 8),
          ("bFrameDelayForwardMin", 7),
          ("bFrameDelayRangeBackwardAvg", 31),
          ("bFrameDelayRangeBackwardBins", 29),
          ("bFrameDelayRangeBackwardMax", 30),
          ("bFrameDelayRangeForwardAvg", 28),
          ("bFrameDelayRangeForwardBins", 26),
          ("bFrameDelayRangeForwardMax", 27),
          ("bFrameDelayRangeTwoWayAvg", 34),
          ("bFrameDelayRangeTwoWayBins", 32),
          ("bFrameDelayRangeTwoWayMax", 33),
          ("bFrameDelayTwoWayAvg", 5),
          ("bFrameDelayTwoWayBins", 2),
          ("bFrameDelayTwoWayMax", 4),
          ("bFrameDelayTwoWayMin", 3),
          ("bIfdvBackwardAvg", 21),
          ("bIfdvBackwardBins", 18),
          ("bIfdvBackwardMax", 20),
          ("bIfdvBackwardMin", 19),
          ("bIfdvForwardAvg", 17),
          ("bIfdvForwardBins", 14),
          ("bIfdvForwardMax", 16),
          ("bIfdvForwardMin", 15),
          ("bIfdvTwoWayAvg", 25),
          ("bIfdvTwoWayBins", 22),
          ("bIfdvTwoWayMax", 24),
          ("bIfdvTwoWayMin", 23),
          ("bMeasuredStatsFrameDelayBackward", 37),
          ("bMeasuredStatsFrameDelayForward", 36),
          ("bMeasuredStatsFrameDelayTwoWay", 35),
          ("bMeasuredStatsIfdvBackward", 40),
          ("bMeasuredStatsIfdvForward", 39),
          ("bMeasuredStatsIfdvTwoWay", 38),
          ("bSoamPdusReceived", 1),
          ("bSoamPdusSent", 0))
    )

_JnxSoamDmCfgMeasurementEnable_Type.__name__ = "Bits"
_JnxSoamDmCfgMeasurementEnable_Object = MibTableColumn
jnxSoamDmCfgMeasurementEnable = _JnxSoamDmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 5),
    _JnxSoamDmCfgMeasurementEnable_Type()
)
jnxSoamDmCfgMeasurementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasurementEnable.setStatus("current")


class _JnxSoamDmCfgMessagePeriod_Type(Integer32):
    """Custom type jnxSoamDmCfgMessagePeriod based on Integer32"""
    defaultValue = 100


_JnxSoamDmCfgMessagePeriod_Object = MibTableColumn
jnxSoamDmCfgMessagePeriod = _JnxSoamDmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 6),
    _JnxSoamDmCfgMessagePeriod_Type()
)
jnxSoamDmCfgMessagePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMessagePeriod.setUnits("ms")
_JnxSoamDmCfgPriority_Type = IEEE8021PriorityValue
_JnxSoamDmCfgPriority_Object = MibTableColumn
jnxSoamDmCfgPriority = _JnxSoamDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 7),
    _JnxSoamDmCfgPriority_Type()
)
jnxSoamDmCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgPriority.setStatus("current")


class _JnxSoamDmCfgFrameSize_Type(Unsigned32):
    """Custom type jnxSoamDmCfgFrameSize based on Unsigned32"""
    defaultValue = 64


_JnxSoamDmCfgFrameSize_Object = MibTableColumn
jnxSoamDmCfgFrameSize = _JnxSoamDmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 8),
    _JnxSoamDmCfgFrameSize_Type()
)
jnxSoamDmCfgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgFrameSize.setStatus("current")


class _JnxSoamDmCfgDataPattern_Type(JnxSoamTcDataPatternType):
    """Custom type jnxSoamDmCfgDataPattern based on JnxSoamTcDataPatternType"""


_JnxSoamDmCfgDataPattern_Object = MibTableColumn
jnxSoamDmCfgDataPattern = _JnxSoamDmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 9),
    _JnxSoamDmCfgDataPattern_Type()
)
jnxSoamDmCfgDataPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDataPattern.setStatus("current")


class _JnxSoamDmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type jnxSoamDmCfgTestTlvIncluded based on TruthValue"""


_JnxSoamDmCfgTestTlvIncluded_Object = MibTableColumn
jnxSoamDmCfgTestTlvIncluded = _JnxSoamDmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 10),
    _JnxSoamDmCfgTestTlvIncluded_Type()
)
jnxSoamDmCfgTestTlvIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgTestTlvIncluded.setStatus("current")


class _JnxSoamDmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):
    """Custom type jnxSoamDmCfgTestTlvPattern based on JnxSoamTcTestPatternType"""


_JnxSoamDmCfgTestTlvPattern_Object = MibTableColumn
jnxSoamDmCfgTestTlvPattern = _JnxSoamDmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 11),
    _JnxSoamDmCfgTestTlvPattern_Type()
)
jnxSoamDmCfgTestTlvPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgTestTlvPattern.setStatus("current")


class _JnxSoamDmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type jnxSoamDmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamDmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgNumIntervalsStored_Object = MibTableColumn
jnxSoamDmCfgNumIntervalsStored = _JnxSoamDmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 12),
    _JnxSoamDmCfgNumIntervalsStored_Type()
)
jnxSoamDmCfgNumIntervalsStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgNumIntervalsStored.setStatus("current")


class _JnxSoamDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type jnxSoamDmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_JnxSoamDmCfgDestMepId_Object = MibTableColumn
jnxSoamDmCfgDestMepId = _JnxSoamDmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 13),
    _JnxSoamDmCfgDestMepId_Type()
)
jnxSoamDmCfgDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDestMepId.setStatus("current")


class _JnxSoamDmCfgDestIsMepId_Type(TruthValue):
    """Custom type jnxSoamDmCfgDestIsMepId based on TruthValue"""


_JnxSoamDmCfgDestIsMepId_Object = MibTableColumn
jnxSoamDmCfgDestIsMepId = _JnxSoamDmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 14),
    _JnxSoamDmCfgDestIsMepId_Type()
)
jnxSoamDmCfgDestIsMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDestIsMepId.setStatus("current")


class _JnxSoamDmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamDmCfgStartTimeType based on JnxSoamTcOperationTimeType"""


_JnxSoamDmCfgStartTimeType_Object = MibTableColumn
jnxSoamDmCfgStartTimeType = _JnxSoamDmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 15),
    _JnxSoamDmCfgStartTimeType_Type()
)
jnxSoamDmCfgStartTimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgStartTimeType.setStatus("current")


class _JnxSoamDmCfgRepetitionTime_Type(Unsigned32):
    """Custom type jnxSoamDmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_JnxSoamDmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgRepetitionTime_Object = MibTableColumn
jnxSoamDmCfgRepetitionTime = _JnxSoamDmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 16),
    _JnxSoamDmCfgRepetitionTime_Type()
)
jnxSoamDmCfgRepetitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRepetitionTime.setUnits("seconds")


class _JnxSoamDmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type jnxSoamDmCfgAlignMeasurementIntervals based on TruthValue"""


_JnxSoamDmCfgAlignMeasurementIntervals_Object = MibTableColumn
jnxSoamDmCfgAlignMeasurementIntervals = _JnxSoamDmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 17),
    _JnxSoamDmCfgAlignMeasurementIntervals_Type()
)
jnxSoamDmCfgAlignMeasurementIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgAlignMeasurementIntervals.setStatus("current")


class _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type(Unsigned32):
    """Custom type jnxSoamDmCfgInterFrameDelayVariationSelectionOffset based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object = MibTableColumn
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset = _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 18),
    _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type()
)
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setStatus("current")


class _JnxSoamDmCfgSessionType_Type(OctetString):
    """Custom type jnxSoamDmCfgSessionType based on OctetString"""
    defaultValue = OctetString("proactive")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamDmCfgSessionType_Type.__name__ = "OctetString"
_JnxSoamDmCfgSessionType_Object = MibTableColumn
jnxSoamDmCfgSessionType = _JnxSoamDmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 19),
    _JnxSoamDmCfgSessionType_Type()
)
jnxSoamDmCfgSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgSessionType.setStatus("current")


class _JnxSoamDmCfgSessionStatus_Type(OctetString):
    """Custom type jnxSoamDmCfgSessionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamDmCfgSessionStatus_Type.__name__ = "OctetString"
_JnxSoamDmCfgSessionStatus_Object = MibTableColumn
jnxSoamDmCfgSessionStatus = _JnxSoamDmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 20),
    _JnxSoamDmCfgSessionStatus_Type()
)
jnxSoamDmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgSessionStatus.setStatus("current")


class _JnxSoamDmCfgHistoryClear_Type(TruthValue):
    """Custom type jnxSoamDmCfgHistoryClear based on TruthValue"""


_JnxSoamDmCfgHistoryClear_Object = MibTableColumn
jnxSoamDmCfgHistoryClear = _JnxSoamDmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 21),
    _JnxSoamDmCfgHistoryClear_Type()
)
jnxSoamDmCfgHistoryClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgHistoryClear.setStatus("current")
_JnxSoamDmCfgRowStatus_Type = RowStatus
_JnxSoamDmCfgRowStatus_Object = MibTableColumn
jnxSoamDmCfgRowStatus = _JnxSoamDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 22),
    _JnxSoamDmCfgRowStatus_Type()
)
jnxSoamDmCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRowStatus.setStatus("current")
_JnxSoamDmMeasuredStatsTable_Object = MibTable
jnxSoamDmMeasuredStatsTable = _JnxSoamDmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsTable.setStatus("current")
_JnxSoamDmMeasuredStatsEntry_Object = MibTableRow
jnxSoamDmMeasuredStatsEntry = _JnxSoamDmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1)
)
jnxSoamDmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsEntry.setStatus("current")
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayTwoWay = _JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 1),
    _JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type()
)
jnxSoamDmMeasuredStatsFrameDelayTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayTwoWay.setUnits("microseconds")
_JnxSoamDmMeasuredStatsFrameDelayForward_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayForward_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayForward = _JnxSoamDmMeasuredStatsFrameDelayForward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 2),
    _JnxSoamDmMeasuredStatsFrameDelayForward_Type()
)
jnxSoamDmMeasuredStatsFrameDelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayForward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayForward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsFrameDelayBackward_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayBackward_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayBackward = _JnxSoamDmMeasuredStatsFrameDelayBackward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 3),
    _JnxSoamDmMeasuredStatsFrameDelayBackward_Type()
)
jnxSoamDmMeasuredStatsFrameDelayBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayBackward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayBackward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvTwoWay_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvTwoWay_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvTwoWay = _JnxSoamDmMeasuredStatsIfdvTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 4),
    _JnxSoamDmMeasuredStatsIfdvTwoWay_Type()
)
jnxSoamDmMeasuredStatsIfdvTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvTwoWay.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvForward_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvForward_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvForward = _JnxSoamDmMeasuredStatsIfdvForward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 5),
    _JnxSoamDmMeasuredStatsIfdvForward_Type()
)
jnxSoamDmMeasuredStatsIfdvForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvForward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvForward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvBackward_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvBackward_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvBackward = _JnxSoamDmMeasuredStatsIfdvBackward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 6),
    _JnxSoamDmMeasuredStatsIfdvBackward_Type()
)
jnxSoamDmMeasuredStatsIfdvBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvBackward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvBackward.setUnits("microseconds")
_JnxSoamDmCurrentStatsTable_Object = MibTable
jnxSoamDmCurrentStatsTable = _JnxSoamDmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3)
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsTable.setStatus("current")
_JnxSoamDmCurrentStatsEntry_Object = MibTableRow
jnxSoamDmCurrentStatsEntry = _JnxSoamDmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1)
)
jnxSoamDmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsEntry.setStatus("current")
_JnxSoamDmCurrentStatsIndex_Type = Unsigned32
_JnxSoamDmCurrentStatsIndex_Object = MibTableColumn
jnxSoamDmCurrentStatsIndex = _JnxSoamDmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 1),
    _JnxSoamDmCurrentStatsIndex_Type()
)
jnxSoamDmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIndex.setStatus("current")
_JnxSoamDmCurrentStatsStartTime_Type = DateAndTime
_JnxSoamDmCurrentStatsStartTime_Object = MibTableColumn
jnxSoamDmCurrentStatsStartTime = _JnxSoamDmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 2),
    _JnxSoamDmCurrentStatsStartTime_Type()
)
jnxSoamDmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsStartTime.setStatus("current")
_JnxSoamDmCurrentStatsElapsedTime_Type = TimeInterval
_JnxSoamDmCurrentStatsElapsedTime_Object = MibTableColumn
jnxSoamDmCurrentStatsElapsedTime = _JnxSoamDmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 3),
    _JnxSoamDmCurrentStatsElapsedTime_Type()
)
jnxSoamDmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsElapsedTime.setStatus("current")
_JnxSoamDmCurrentStatsSuspect_Type = TruthValue
_JnxSoamDmCurrentStatsSuspect_Object = MibTableColumn
jnxSoamDmCurrentStatsSuspect = _JnxSoamDmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 4),
    _JnxSoamDmCurrentStatsSuspect_Type()
)
jnxSoamDmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSuspect.setStatus("current")
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMin = _JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 5),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMax = _JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 6),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg = _JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 7),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMin = _JnxSoamDmCurrentStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 8),
    _JnxSoamDmCurrentStatsFrameDelayForwardMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMax = _JnxSoamDmCurrentStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 9),
    _JnxSoamDmCurrentStatsFrameDelayForwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardAvg = _JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 10),
    _JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMin = _JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 11),
    _JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMax = _JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 12),
    _JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardAvg = _JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 13),
    _JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMin = _JnxSoamDmCurrentStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 14),
    _JnxSoamDmCurrentStatsIfdvForwardMin_Type()
)
jnxSoamDmCurrentStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMax = _JnxSoamDmCurrentStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 15),
    _JnxSoamDmCurrentStatsIfdvForwardMax_Type()
)
jnxSoamDmCurrentStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardAvg = _JnxSoamDmCurrentStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 16),
    _JnxSoamDmCurrentStatsIfdvForwardAvg_Type()
)
jnxSoamDmCurrentStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMin = _JnxSoamDmCurrentStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 17),
    _JnxSoamDmCurrentStatsIfdvBackwardMin_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMax = _JnxSoamDmCurrentStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 18),
    _JnxSoamDmCurrentStatsIfdvBackwardMax_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardAvg = _JnxSoamDmCurrentStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 19),
    _JnxSoamDmCurrentStatsIfdvBackwardAvg_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMin = _JnxSoamDmCurrentStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 20),
    _JnxSoamDmCurrentStatsIfdvTwoWayMin_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMax = _JnxSoamDmCurrentStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 21),
    _JnxSoamDmCurrentStatsIfdvTwoWayMax_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayAvg = _JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 22),
    _JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsSoamPdusSent_Type = Gauge32
_JnxSoamDmCurrentStatsSoamPdusSent_Object = MibTableColumn
jnxSoamDmCurrentStatsSoamPdusSent = _JnxSoamDmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 23),
    _JnxSoamDmCurrentStatsSoamPdusSent_Type()
)
jnxSoamDmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSoamPdusSent.setStatus("current")
_JnxSoamDmCurrentStatsSoamPdusReceived_Type = Gauge32
_JnxSoamDmCurrentStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamDmCurrentStatsSoamPdusReceived = _JnxSoamDmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 24),
    _JnxSoamDmCurrentStatsSoamPdusReceived_Type()
)
jnxSoamDmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSoamPdusReceived.setStatus("current")
_JnxSoamDmHistoryStatsTable_Object = MibTable
jnxSoamDmHistoryStatsTable = _JnxSoamDmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4)
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsTable.setStatus("current")
_JnxSoamDmHistoryStatsEntry_Object = MibTableRow
jnxSoamDmHistoryStatsEntry = _JnxSoamDmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1)
)
jnxSoamDmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsEntry.setStatus("current")
_JnxSoamDmHistoryStatsIndex_Type = Unsigned32
_JnxSoamDmHistoryStatsIndex_Object = MibTableColumn
jnxSoamDmHistoryStatsIndex = _JnxSoamDmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 1),
    _JnxSoamDmHistoryStatsIndex_Type()
)
jnxSoamDmHistoryStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIndex.setStatus("current")
_JnxSoamDmHistoryStatsEndTime_Type = DateAndTime
_JnxSoamDmHistoryStatsEndTime_Object = MibTableColumn
jnxSoamDmHistoryStatsEndTime = _JnxSoamDmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 2),
    _JnxSoamDmHistoryStatsEndTime_Type()
)
jnxSoamDmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsEndTime.setStatus("current")
_JnxSoamDmHistoryStatsElapsedTime_Type = TimeInterval
_JnxSoamDmHistoryStatsElapsedTime_Object = MibTableColumn
jnxSoamDmHistoryStatsElapsedTime = _JnxSoamDmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 3),
    _JnxSoamDmHistoryStatsElapsedTime_Type()
)
jnxSoamDmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsElapsedTime.setStatus("current")
_JnxSoamDmHistoryStatsSuspect_Type = TruthValue
_JnxSoamDmHistoryStatsSuspect_Object = MibTableColumn
jnxSoamDmHistoryStatsSuspect = _JnxSoamDmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 4),
    _JnxSoamDmHistoryStatsSuspect_Type()
)
jnxSoamDmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSuspect.setStatus("current")
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMin = _JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 5),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMax = _JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 6),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg = _JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 7),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMin = _JnxSoamDmHistoryStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 8),
    _JnxSoamDmHistoryStatsFrameDelayForwardMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMax = _JnxSoamDmHistoryStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 9),
    _JnxSoamDmHistoryStatsFrameDelayForwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardAvg = _JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 10),
    _JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMin = _JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 11),
    _JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMax = _JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 12),
    _JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardAvg = _JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 13),
    _JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMin = _JnxSoamDmHistoryStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 14),
    _JnxSoamDmHistoryStatsIfdvForwardMin_Type()
)
jnxSoamDmHistoryStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMax = _JnxSoamDmHistoryStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 15),
    _JnxSoamDmHistoryStatsIfdvForwardMax_Type()
)
jnxSoamDmHistoryStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardAvg = _JnxSoamDmHistoryStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 16),
    _JnxSoamDmHistoryStatsIfdvForwardAvg_Type()
)
jnxSoamDmHistoryStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMin = _JnxSoamDmHistoryStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 17),
    _JnxSoamDmHistoryStatsIfdvBackwardMin_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMax = _JnxSoamDmHistoryStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 18),
    _JnxSoamDmHistoryStatsIfdvBackwardMax_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardAvg = _JnxSoamDmHistoryStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 19),
    _JnxSoamDmHistoryStatsIfdvBackwardAvg_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMin = _JnxSoamDmHistoryStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 20),
    _JnxSoamDmHistoryStatsIfdvTwoWayMin_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMax = _JnxSoamDmHistoryStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 21),
    _JnxSoamDmHistoryStatsIfdvTwoWayMax_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayAvg = _JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 22),
    _JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsSoamPdusSent_Type = Gauge32
_JnxSoamDmHistoryStatsSoamPdusSent_Object = MibTableColumn
jnxSoamDmHistoryStatsSoamPdusSent = _JnxSoamDmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 23),
    _JnxSoamDmHistoryStatsSoamPdusSent_Type()
)
jnxSoamDmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSoamPdusSent.setStatus("current")
_JnxSoamDmHistoryStatsSoamPdusReceived_Type = Gauge32
_JnxSoamDmHistoryStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamDmHistoryStatsSoamPdusReceived = _JnxSoamDmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 24),
    _JnxSoamDmHistoryStatsSoamPdusReceived_Type()
)
jnxSoamDmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSoamPdusReceived.setStatus("current")
_JnxSoamDmThresholdCfgTable_Object = MibTable
jnxSoamDmThresholdCfgTable = _JnxSoamDmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5)
)
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgTable.setStatus("current")
_JnxSoamDmThresholdCfgEntry_Object = MibTableRow
jnxSoamDmThresholdCfgEntry = _JnxSoamDmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1)
)
jnxSoamDmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgEntry.setStatus("current")


class _JnxSoamDmThresholdCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSoamDmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamDmThresholdCfgIndex_Object = MibTableColumn
jnxSoamDmThresholdCfgIndex = _JnxSoamDmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 1),
    _JnxSoamDmThresholdCfgIndex_Type()
)
jnxSoamDmThresholdCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgIndex.setStatus("current")


class _JnxSoamDmThresholdCfgEnable_Type(Bits):
    """Custom type jnxSoamDmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bJnxSoamDmAvgFrameDelayBackwardThreshold", 18),
          ("bJnxSoamDmAvgFrameDelayForwardThreshold", 10),
          ("bJnxSoamDmAvgFrameDelayRangeBackwardThreshold", 23),
          ("bJnxSoamDmAvgFrameDelayRangeForwardThreshold", 15),
          ("bJnxSoamDmAvgFrameDelayRangeTwoWayThreshold", 7),
          ("bJnxSoamDmAvgFrameDelayTwoWayThreshold", 2),
          ("bJnxSoamDmAvgIfdvBackwardThreshold", 21),
          ("bJnxSoamDmAvgIfdvForwardThreshold", 13),
          ("bJnxSoamDmAvgIfdvTwoWayThreshold", 5),
          ("bJnxSoamDmMaxFrameDelayBackwardThreshold", 17),
          ("bJnxSoamDmMaxFrameDelayForwardThreshold", 9),
          ("bJnxSoamDmMaxFrameDelayRangeBackwardThreshold", 22),
          ("bJnxSoamDmMaxFrameDelayRangeForwardThreshold", 14),
          ("bJnxSoamDmMaxFrameDelayRangeTwoWayThreshold", 6),
          ("bJnxSoamDmMaxFrameDelayTwoWayThreshold", 1),
          ("bJnxSoamDmMaxIfdvBackwardThreshold", 20),
          ("bJnxSoamDmMaxIfdvForwardThreshold", 12),
          ("bJnxSoamDmMaxIfdvTwoWayThreshold", 4),
          ("bJnxSoamDmMeasuredFrameDelayBackwardThreshold", 16),
          ("bJnxSoamDmMeasuredFrameDelayForwardThreshold", 8),
          ("bJnxSoamDmMeasuredFrameDelayTwoWayThreshold", 0),
          ("bJnxSoamDmMeasuredIfdvBackwardThreshold", 19),
          ("bJnxSoamDmMeasuredIfdvForwardThreshold", 11),
          ("bJnxSoamDmMeasuredIfdvTwoWayThreshold", 3))
    )

_JnxSoamDmThresholdCfgEnable_Type.__name__ = "Bits"
_JnxSoamDmThresholdCfgEnable_Object = MibTableColumn
jnxSoamDmThresholdCfgEnable = _JnxSoamDmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 2),
    _JnxSoamDmThresholdCfgEnable_Type()
)
jnxSoamDmThresholdCfgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgEnable.setStatus("current")


class _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object = MibTableColumn
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold = _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 3),
    _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type()
)
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setUnits("microseconds")


class _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object = MibTableColumn
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold = _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 4),
    _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type()
)
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setUnits("microseconds")
_JnxSoamDmThresholdCfgRowStatus_Type = RowStatus
_JnxSoamDmThresholdCfgRowStatus_Object = MibTableColumn
jnxSoamDmThresholdCfgRowStatus = _JnxSoamDmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 5),
    _JnxSoamDmThresholdCfgRowStatus_Type()
)
jnxSoamDmThresholdCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgRowStatus.setStatus("current")
_JnxSoamPmNotificationCfg_ObjectIdentity = ObjectIdentity
jnxSoamPmNotificationCfg = _JnxSoamPmNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 4)
)
_JnxSoamPmNotificationObj_ObjectIdentity = ObjectIdentity
jnxSoamPmNotificationObj = _JnxSoamPmNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5)
)
_JnxSoamPmNotificationObjDateAndTime_Type = DateAndTime
_JnxSoamPmNotificationObjDateAndTime_Object = MibScalar
jnxSoamPmNotificationObjDateAndTime = _JnxSoamPmNotificationObjDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 1),
    _JnxSoamPmNotificationObjDateAndTime_Type()
)
jnxSoamPmNotificationObjDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjDateAndTime.setStatus("current")
_JnxSoamPmNotificationObjThresholdId_Type = ObjectIdentifier
_JnxSoamPmNotificationObjThresholdId_Object = MibScalar
jnxSoamPmNotificationObjThresholdId = _JnxSoamPmNotificationObjThresholdId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 2),
    _JnxSoamPmNotificationObjThresholdId_Type()
)
jnxSoamPmNotificationObjThresholdId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdId.setStatus("current")
_JnxSoamPmNotificationObjThresholdConfig_Type = Unsigned32
_JnxSoamPmNotificationObjThresholdConfig_Object = MibScalar
jnxSoamPmNotificationObjThresholdConfig = _JnxSoamPmNotificationObjThresholdConfig_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 3),
    _JnxSoamPmNotificationObjThresholdConfig_Type()
)
jnxSoamPmNotificationObjThresholdConfig.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdConfig.setStatus("current")
_JnxSoamPmNotificationObjThresholdValue_Type = Unsigned32
_JnxSoamPmNotificationObjThresholdValue_Object = MibScalar
jnxSoamPmNotificationObjThresholdValue = _JnxSoamPmNotificationObjThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 4),
    _JnxSoamPmNotificationObjThresholdValue_Type()
)
jnxSoamPmNotificationObjThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdValue.setStatus("current")
_JnxSoamPmNotificationObjSuspect_Type = TruthValue
_JnxSoamPmNotificationObjSuspect_Object = MibScalar
jnxSoamPmNotificationObjSuspect = _JnxSoamPmNotificationObjSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 5),
    _JnxSoamPmNotificationObjSuspect_Type()
)
jnxSoamPmNotificationObjSuspect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjSuspect.setStatus("current")


class _JnxSoamPmNotificationObjCrossingType_Type(Integer32):
    """Custom type jnxSoamPmNotificationObjCrossingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveAlarm", 1),
          ("clearAlarm", 3),
          ("setAlarm", 2))
    )


_JnxSoamPmNotificationObjCrossingType_Type.__name__ = "Integer32"
_JnxSoamPmNotificationObjCrossingType_Object = MibScalar
jnxSoamPmNotificationObjCrossingType = _JnxSoamPmNotificationObjCrossingType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 6),
    _JnxSoamPmNotificationObjCrossingType_Type()
)
jnxSoamPmNotificationObjCrossingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjCrossingType.setStatus("current")
_JnxSoamPmNotificationObjDestinationMep_Type = MacAddress
_JnxSoamPmNotificationObjDestinationMep_Object = MibScalar
jnxSoamPmNotificationObjDestinationMep = _JnxSoamPmNotificationObjDestinationMep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 7),
    _JnxSoamPmNotificationObjDestinationMep_Type()
)
jnxSoamPmNotificationObjDestinationMep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjDestinationMep.setStatus("current")
_JnxSoamPmNotificationObjPriority_Type = MacAddress
_JnxSoamPmNotificationObjPriority_Object = MibScalar
jnxSoamPmNotificationObjPriority = _JnxSoamPmNotificationObjPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 8),
    _JnxSoamPmNotificationObjPriority_Type()
)
jnxSoamPmNotificationObjPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjPriority.setStatus("current")
_JnxSoamPmMibConformance_ObjectIdentity = ObjectIdentity
jnxSoamPmMibConformance = _JnxSoamPmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("JUNIPER-SOAM-PM-MIB",
     "jnxSoamPmMepEntry")
)
jnxSoamPmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxSoamLmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 1)
)
jnxSoamLmSessionStartStopAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgSessionStatus"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamLmSessionStartStopAlarm.setStatus(
        "current"
    )

jnxSoamDmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 2)
)
jnxSoamDmSessionStartStopAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgSessionStatus"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamDmSessionStartStopAlarm.setStatus(
        "current"
    )

jnxSoamPmThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 3)
)
jnxSoamPmThresholdCrossingAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjCrossingType"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdId"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdConfig"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdValue"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjSuspect"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamPmThresholdCrossingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SOAM-PM-MIB",
    **{"IEEE8021PriorityValue": IEEE8021PriorityValue,
       "JnxSoamTcTestPatternType": JnxSoamTcTestPatternType,
       "JnxSoamTcDataPatternType": JnxSoamTcDataPatternType,
       "JnxSoamTcOperationTimeType": JnxSoamTcOperationTimeType,
       "jnxSoamPmMib": jnxSoamPmMib,
       "jnxSoamPmNotifications": jnxSoamPmNotifications,
       "jnxSoamLmSessionStartStopAlarm": jnxSoamLmSessionStartStopAlarm,
       "jnxSoamDmSessionStartStopAlarm": jnxSoamDmSessionStartStopAlarm,
       "jnxSoamPmThresholdCrossingAlarm": jnxSoamPmThresholdCrossingAlarm,
       "jnxSoamPmMibObjects": jnxSoamPmMibObjects,
       "jnxSoamPmMep": jnxSoamPmMep,
       "jnxSoamPmMepTable": jnxSoamPmMepTable,
       "jnxSoamPmMepEntry": jnxSoamPmMepEntry,
       "jnxSoamPmMepOperNextIndex": jnxSoamPmMepOperNextIndex,
       "jnxSoamPmMepLmSingleEndedResponder": jnxSoamPmMepLmSingleEndedResponder,
       "jnxSoamPmMepSlmSingleEndedResponder": jnxSoamPmMepSlmSingleEndedResponder,
       "jnxSoamPmMepDmSingleEndedResponder": jnxSoamPmMepDmSingleEndedResponder,
       "jnxSoamPmLmObjects": jnxSoamPmLmObjects,
       "jnxSoamLmCfgTable": jnxSoamLmCfgTable,
       "jnxSoamLmCfgEntry": jnxSoamLmCfgEntry,
       "jnxSoamLmCfgIndex": jnxSoamLmCfgIndex,
       "jnxSoamLmCfgType": jnxSoamLmCfgType,
       "jnxSoamLmCfgVersion": jnxSoamLmCfgVersion,
       "jnxSoamLmCfgEnabled": jnxSoamLmCfgEnabled,
       "jnxSoamLmCfgMeasurementEnable": jnxSoamLmCfgMeasurementEnable,
       "jnxSoamLmCfgMessagePeriod": jnxSoamLmCfgMessagePeriod,
       "jnxSoamLmCfgPriority": jnxSoamLmCfgPriority,
       "jnxSoamLmCfgFrameSize": jnxSoamLmCfgFrameSize,
       "jnxSoamLmCfgDataPattern": jnxSoamLmCfgDataPattern,
       "jnxSoamLmCfgTestTlvIncluded": jnxSoamLmCfgTestTlvIncluded,
       "jnxSoamLmCfgTestTlvPattern": jnxSoamLmCfgTestTlvPattern,
       "jnxSoamLmCfgNumIntervalsStored": jnxSoamLmCfgNumIntervalsStored,
       "jnxSoamLmCfgDestMepId": jnxSoamLmCfgDestMepId,
       "jnxSoamLmCfgDestIsMepId": jnxSoamLmCfgDestIsMepId,
       "jnxSoamLmCfgStartTimeType": jnxSoamLmCfgStartTimeType,
       "jnxSoamLmCfgFixedStartDateAndTime": jnxSoamLmCfgFixedStartDateAndTime,
       "jnxSoamLmCfgRelativeStartTime": jnxSoamLmCfgRelativeStartTime,
       "jnxSoamLmCfgRepetitionTime": jnxSoamLmCfgRepetitionTime,
       "jnxSoamLmCfgAlignMeasurementIntervals": jnxSoamLmCfgAlignMeasurementIntervals,
       "jnxSoamLmCfgAlignMeasurementOffset": jnxSoamLmCfgAlignMeasurementOffset,
       "jnxSoamLmCfgSessionType": jnxSoamLmCfgSessionType,
       "jnxSoamLmCfgSessionStatus": jnxSoamLmCfgSessionStatus,
       "jnxSoamLmCfgHistoryClear": jnxSoamLmCfgHistoryClear,
       "jnxSoamLmCfgRowStatus": jnxSoamLmCfgRowStatus,
       "jnxSoamLmMeasuredStatsTable": jnxSoamLmMeasuredStatsTable,
       "jnxSoamLmMeasuredStatsEntry": jnxSoamLmMeasuredStatsEntry,
       "jnxSoamLmMeasuredStatsForwardFlr": jnxSoamLmMeasuredStatsForwardFlr,
       "jnxSoamLmMeasuredStatsBackwardFlr": jnxSoamLmMeasuredStatsBackwardFlr,
       "jnxSoamLmCurrentStatsTable": jnxSoamLmCurrentStatsTable,
       "jnxSoamLmCurrentStatsEntry": jnxSoamLmCurrentStatsEntry,
       "jnxSoamLmCurrentStatsIndex": jnxSoamLmCurrentStatsIndex,
       "jnxSoamLmCurrentStatsStartTime": jnxSoamLmCurrentStatsStartTime,
       "jnxSoamLmCurrentStatsElapsedTime": jnxSoamLmCurrentStatsElapsedTime,
       "jnxSoamLmCurrentStatsSuspect": jnxSoamLmCurrentStatsSuspect,
       "jnxSoamLmCurrentStatsForwardTransmittedFrames": jnxSoamLmCurrentStatsForwardTransmittedFrames,
       "jnxSoamLmCurrentStatsForwardReceivedFrames": jnxSoamLmCurrentStatsForwardReceivedFrames,
       "jnxSoamLmCurrentStatsForwardMinFlr": jnxSoamLmCurrentStatsForwardMinFlr,
       "jnxSoamLmCurrentStatsForwardMaxFlr": jnxSoamLmCurrentStatsForwardMaxFlr,
       "jnxSoamLmCurrentStatsForwardAvgFlr": jnxSoamLmCurrentStatsForwardAvgFlr,
       "jnxSoamLmCurrentStatsBackwardTransmittedFrames": jnxSoamLmCurrentStatsBackwardTransmittedFrames,
       "jnxSoamLmCurrentStatsBackwardReceivedFrames": jnxSoamLmCurrentStatsBackwardReceivedFrames,
       "jnxSoamLmCurrentStatsBackwardMinFlr": jnxSoamLmCurrentStatsBackwardMinFlr,
       "jnxSoamLmCurrentStatsBackwardMaxFlr": jnxSoamLmCurrentStatsBackwardMaxFlr,
       "jnxSoamLmCurrentStatsBackwardAvgFlr": jnxSoamLmCurrentStatsBackwardAvgFlr,
       "jnxSoamLmCurrentStatsSoamPdusSent": jnxSoamLmCurrentStatsSoamPdusSent,
       "jnxSoamLmCurrentStatsSoamPdusReceived": jnxSoamLmCurrentStatsSoamPdusReceived,
       "jnxSoamLmHistoryStatsTable": jnxSoamLmHistoryStatsTable,
       "jnxSoamLmHistoryStatsEntry": jnxSoamLmHistoryStatsEntry,
       "jnxSoamLmHistoryStatsIndex": jnxSoamLmHistoryStatsIndex,
       "jnxSoamLmHistoryStatsEndTime": jnxSoamLmHistoryStatsEndTime,
       "jnxSoamLmHistoryStatsElapsedTime": jnxSoamLmHistoryStatsElapsedTime,
       "jnxSoamLmHistoryStatsSuspect": jnxSoamLmHistoryStatsSuspect,
       "jnxSoamLmHistoryStatsForwardTransmittedFrames": jnxSoamLmHistoryStatsForwardTransmittedFrames,
       "jnxSoamLmHistoryStatsForwardReceivedFrames": jnxSoamLmHistoryStatsForwardReceivedFrames,
       "jnxSoamLmHistoryStatsForwardMinFlr": jnxSoamLmHistoryStatsForwardMinFlr,
       "jnxSoamLmHistoryStatsForwardMaxFlr": jnxSoamLmHistoryStatsForwardMaxFlr,
       "jnxSoamLmHistoryStatsForwardAvgFlr": jnxSoamLmHistoryStatsForwardAvgFlr,
       "jnxSoamLmHistoryStatsBackwardTransmittedFrames": jnxSoamLmHistoryStatsBackwardTransmittedFrames,
       "jnxSoamLmHistoryStatsBackwardReceivedFrames": jnxSoamLmHistoryStatsBackwardReceivedFrames,
       "jnxSoamLmHistoryStatsBackwardMinFlr": jnxSoamLmHistoryStatsBackwardMinFlr,
       "jnxSoamLmHistoryStatsBackwardMaxFlr": jnxSoamLmHistoryStatsBackwardMaxFlr,
       "jnxSoamLmHistoryStatsBackwardAvgFlr": jnxSoamLmHistoryStatsBackwardAvgFlr,
       "jnxSoamLmHistoryStatsSoamPdusSent": jnxSoamLmHistoryStatsSoamPdusSent,
       "jnxSoamLmHistoryStatsSoamPdusReceived": jnxSoamLmHistoryStatsSoamPdusReceived,
       "jnxSoamLmThresholdCfgTable": jnxSoamLmThresholdCfgTable,
       "jnxSoamLmThresholdCfgEntry": jnxSoamLmThresholdCfgEntry,
       "jnxSoamLmThresholdCfgIndex": jnxSoamLmThresholdCfgIndex,
       "jnxSoamLmThresholdCfgEnable": jnxSoamLmThresholdCfgEnable,
       "jnxSoamLmThresholdCfgAvgFlrForwardThreshold": jnxSoamLmThresholdCfgAvgFlrForwardThreshold,
       "jnxSoamLmThresholdCfgAvgFlrBackwardThreshold": jnxSoamLmThresholdCfgAvgFlrBackwardThreshold,
       "jnxSoamLmThresholdCfgRowStatus": jnxSoamLmThresholdCfgRowStatus,
       "jnxSoamPmDmObjects": jnxSoamPmDmObjects,
       "jnxSoamDmCfgTable": jnxSoamDmCfgTable,
       "jnxSoamDmCfgEntry": jnxSoamDmCfgEntry,
       "jnxSoamDmCfgIndex": jnxSoamDmCfgIndex,
       "jnxSoamDmCfgType": jnxSoamDmCfgType,
       "jnxSoamDmCfgVersion": jnxSoamDmCfgVersion,
       "jnxSoamDmCfgEnabled": jnxSoamDmCfgEnabled,
       "jnxSoamDmCfgMeasurementEnable": jnxSoamDmCfgMeasurementEnable,
       "jnxSoamDmCfgMessagePeriod": jnxSoamDmCfgMessagePeriod,
       "jnxSoamDmCfgPriority": jnxSoamDmCfgPriority,
       "jnxSoamDmCfgFrameSize": jnxSoamDmCfgFrameSize,
       "jnxSoamDmCfgDataPattern": jnxSoamDmCfgDataPattern,
       "jnxSoamDmCfgTestTlvIncluded": jnxSoamDmCfgTestTlvIncluded,
       "jnxSoamDmCfgTestTlvPattern": jnxSoamDmCfgTestTlvPattern,
       "jnxSoamDmCfgNumIntervalsStored": jnxSoamDmCfgNumIntervalsStored,
       "jnxSoamDmCfgDestMepId": jnxSoamDmCfgDestMepId,
       "jnxSoamDmCfgDestIsMepId": jnxSoamDmCfgDestIsMepId,
       "jnxSoamDmCfgStartTimeType": jnxSoamDmCfgStartTimeType,
       "jnxSoamDmCfgRepetitionTime": jnxSoamDmCfgRepetitionTime,
       "jnxSoamDmCfgAlignMeasurementIntervals": jnxSoamDmCfgAlignMeasurementIntervals,
       "jnxSoamDmCfgInterFrameDelayVariationSelectionOffset": jnxSoamDmCfgInterFrameDelayVariationSelectionOffset,
       "jnxSoamDmCfgSessionType": jnxSoamDmCfgSessionType,
       "jnxSoamDmCfgSessionStatus": jnxSoamDmCfgSessionStatus,
       "jnxSoamDmCfgHistoryClear": jnxSoamDmCfgHistoryClear,
       "jnxSoamDmCfgRowStatus": jnxSoamDmCfgRowStatus,
       "jnxSoamDmMeasuredStatsTable": jnxSoamDmMeasuredStatsTable,
       "jnxSoamDmMeasuredStatsEntry": jnxSoamDmMeasuredStatsEntry,
       "jnxSoamDmMeasuredStatsFrameDelayTwoWay": jnxSoamDmMeasuredStatsFrameDelayTwoWay,
       "jnxSoamDmMeasuredStatsFrameDelayForward": jnxSoamDmMeasuredStatsFrameDelayForward,
       "jnxSoamDmMeasuredStatsFrameDelayBackward": jnxSoamDmMeasuredStatsFrameDelayBackward,
       "jnxSoamDmMeasuredStatsIfdvTwoWay": jnxSoamDmMeasuredStatsIfdvTwoWay,
       "jnxSoamDmMeasuredStatsIfdvForward": jnxSoamDmMeasuredStatsIfdvForward,
       "jnxSoamDmMeasuredStatsIfdvBackward": jnxSoamDmMeasuredStatsIfdvBackward,
       "jnxSoamDmCurrentStatsTable": jnxSoamDmCurrentStatsTable,
       "jnxSoamDmCurrentStatsEntry": jnxSoamDmCurrentStatsEntry,
       "jnxSoamDmCurrentStatsIndex": jnxSoamDmCurrentStatsIndex,
       "jnxSoamDmCurrentStatsStartTime": jnxSoamDmCurrentStatsStartTime,
       "jnxSoamDmCurrentStatsElapsedTime": jnxSoamDmCurrentStatsElapsedTime,
       "jnxSoamDmCurrentStatsSuspect": jnxSoamDmCurrentStatsSuspect,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayMin": jnxSoamDmCurrentStatsFrameDelayTwoWayMin,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayMax": jnxSoamDmCurrentStatsFrameDelayTwoWayMax,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayAvg": jnxSoamDmCurrentStatsFrameDelayTwoWayAvg,
       "jnxSoamDmCurrentStatsFrameDelayForwardMin": jnxSoamDmCurrentStatsFrameDelayForwardMin,
       "jnxSoamDmCurrentStatsFrameDelayForwardMax": jnxSoamDmCurrentStatsFrameDelayForwardMax,
       "jnxSoamDmCurrentStatsFrameDelayForwardAvg": jnxSoamDmCurrentStatsFrameDelayForwardAvg,
       "jnxSoamDmCurrentStatsFrameDelayBackwardMin": jnxSoamDmCurrentStatsFrameDelayBackwardMin,
       "jnxSoamDmCurrentStatsFrameDelayBackwardMax": jnxSoamDmCurrentStatsFrameDelayBackwardMax,
       "jnxSoamDmCurrentStatsFrameDelayBackwardAvg": jnxSoamDmCurrentStatsFrameDelayBackwardAvg,
       "jnxSoamDmCurrentStatsIfdvForwardMin": jnxSoamDmCurrentStatsIfdvForwardMin,
       "jnxSoamDmCurrentStatsIfdvForwardMax": jnxSoamDmCurrentStatsIfdvForwardMax,
       "jnxSoamDmCurrentStatsIfdvForwardAvg": jnxSoamDmCurrentStatsIfdvForwardAvg,
       "jnxSoamDmCurrentStatsIfdvBackwardMin": jnxSoamDmCurrentStatsIfdvBackwardMin,
       "jnxSoamDmCurrentStatsIfdvBackwardMax": jnxSoamDmCurrentStatsIfdvBackwardMax,
       "jnxSoamDmCurrentStatsIfdvBackwardAvg": jnxSoamDmCurrentStatsIfdvBackwardAvg,
       "jnxSoamDmCurrentStatsIfdvTwoWayMin": jnxSoamDmCurrentStatsIfdvTwoWayMin,
       "jnxSoamDmCurrentStatsIfdvTwoWayMax": jnxSoamDmCurrentStatsIfdvTwoWayMax,
       "jnxSoamDmCurrentStatsIfdvTwoWayAvg": jnxSoamDmCurrentStatsIfdvTwoWayAvg,
       "jnxSoamDmCurrentStatsSoamPdusSent": jnxSoamDmCurrentStatsSoamPdusSent,
       "jnxSoamDmCurrentStatsSoamPdusReceived": jnxSoamDmCurrentStatsSoamPdusReceived,
       "jnxSoamDmHistoryStatsTable": jnxSoamDmHistoryStatsTable,
       "jnxSoamDmHistoryStatsEntry": jnxSoamDmHistoryStatsEntry,
       "jnxSoamDmHistoryStatsIndex": jnxSoamDmHistoryStatsIndex,
       "jnxSoamDmHistoryStatsEndTime": jnxSoamDmHistoryStatsEndTime,
       "jnxSoamDmHistoryStatsElapsedTime": jnxSoamDmHistoryStatsElapsedTime,
       "jnxSoamDmHistoryStatsSuspect": jnxSoamDmHistoryStatsSuspect,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayMin": jnxSoamDmHistoryStatsFrameDelayTwoWayMin,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayMax": jnxSoamDmHistoryStatsFrameDelayTwoWayMax,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayAvg": jnxSoamDmHistoryStatsFrameDelayTwoWayAvg,
       "jnxSoamDmHistoryStatsFrameDelayForwardMin": jnxSoamDmHistoryStatsFrameDelayForwardMin,
       "jnxSoamDmHistoryStatsFrameDelayForwardMax": jnxSoamDmHistoryStatsFrameDelayForwardMax,
       "jnxSoamDmHistoryStatsFrameDelayForwardAvg": jnxSoamDmHistoryStatsFrameDelayForwardAvg,
       "jnxSoamDmHistoryStatsFrameDelayBackwardMin": jnxSoamDmHistoryStatsFrameDelayBackwardMin,
       "jnxSoamDmHistoryStatsFrameDelayBackwardMax": jnxSoamDmHistoryStatsFrameDelayBackwardMax,
       "jnxSoamDmHistoryStatsFrameDelayBackwardAvg": jnxSoamDmHistoryStatsFrameDelayBackwardAvg,
       "jnxSoamDmHistoryStatsIfdvForwardMin": jnxSoamDmHistoryStatsIfdvForwardMin,
       "jnxSoamDmHistoryStatsIfdvForwardMax": jnxSoamDmHistoryStatsIfdvForwardMax,
       "jnxSoamDmHistoryStatsIfdvForwardAvg": jnxSoamDmHistoryStatsIfdvForwardAvg,
       "jnxSoamDmHistoryStatsIfdvBackwardMin": jnxSoamDmHistoryStatsIfdvBackwardMin,
       "jnxSoamDmHistoryStatsIfdvBackwardMax": jnxSoamDmHistoryStatsIfdvBackwardMax,
       "jnxSoamDmHistoryStatsIfdvBackwardAvg": jnxSoamDmHistoryStatsIfdvBackwardAvg,
       "jnxSoamDmHistoryStatsIfdvTwoWayMin": jnxSoamDmHistoryStatsIfdvTwoWayMin,
       "jnxSoamDmHistoryStatsIfdvTwoWayMax": jnxSoamDmHistoryStatsIfdvTwoWayMax,
       "jnxSoamDmHistoryStatsIfdvTwoWayAvg": jnxSoamDmHistoryStatsIfdvTwoWayAvg,
       "jnxSoamDmHistoryStatsSoamPdusSent": jnxSoamDmHistoryStatsSoamPdusSent,
       "jnxSoamDmHistoryStatsSoamPdusReceived": jnxSoamDmHistoryStatsSoamPdusReceived,
       "jnxSoamDmThresholdCfgTable": jnxSoamDmThresholdCfgTable,
       "jnxSoamDmThresholdCfgEntry": jnxSoamDmThresholdCfgEntry,
       "jnxSoamDmThresholdCfgIndex": jnxSoamDmThresholdCfgIndex,
       "jnxSoamDmThresholdCfgEnable": jnxSoamDmThresholdCfgEnable,
       "jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold": jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold,
       "jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold": jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold,
       "jnxSoamDmThresholdCfgRowStatus": jnxSoamDmThresholdCfgRowStatus,
       "jnxSoamPmNotificationCfg": jnxSoamPmNotificationCfg,
       "jnxSoamPmNotificationObj": jnxSoamPmNotificationObj,
       "jnxSoamPmNotificationObjDateAndTime": jnxSoamPmNotificationObjDateAndTime,
       "jnxSoamPmNotificationObjThresholdId": jnxSoamPmNotificationObjThresholdId,
       "jnxSoamPmNotificationObjThresholdConfig": jnxSoamPmNotificationObjThresholdConfig,
       "jnxSoamPmNotificationObjThresholdValue": jnxSoamPmNotificationObjThresholdValue,
       "jnxSoamPmNotificationObjSuspect": jnxSoamPmNotificationObjSuspect,
       "jnxSoamPmNotificationObjCrossingType": jnxSoamPmNotificationObjCrossingType,
       "jnxSoamPmNotificationObjDestinationMep": jnxSoamPmNotificationObjDestinationMep,
       "jnxSoamPmNotificationObjPriority": jnxSoamPmNotificationObjPriority,
       "jnxSoamPmMibConformance": jnxSoamPmMibConformance}
)
