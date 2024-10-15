# SNMP MIB module (JUNIPER-PW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-PW-TDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:04 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(jnxMibs,
 jnxPwTdmMibRoot) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxPwTdmMibRoot")

(jnxVpnPwIndex,
 jnxVpnPwVpnName,
 jnxVpnPwVpnType) = mibBuilder.importSymbols(
    "JUNIPER-VPN-MIB",
    "jnxVpnPwIndex",
    "jnxVpnPwVpnName",
    "jnxVpnPwVpnType")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxPWTdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1)
)
jnxPWTdmMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPwTDMCfgIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class JnxPwCfgIndexOrzero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_JnxpwTDMObjects_ObjectIdentity = ObjectIdentity
jnxpwTDMObjects = _JnxpwTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1)
)
_JnxpwTDMTable_Object = MibTable
jnxpwTDMTable = _JnxpwTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxpwTDMTable.setStatus("current")
_JnxpwTDMEntry_Object = MibTableRow
jnxpwTDMEntry = _JnxpwTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1)
)
jnxpwTDMEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
)
if mibBuilder.loadTexts:
    jnxpwTDMEntry.setStatus("current")


class _JnxpwTDMRate_Type(Integer32):
    """Custom type jnxpwTDMRate based on Integer32"""
    defaultValue = 32


_JnxpwTDMRate_Object = MibTableColumn
jnxpwTDMRate = _JnxpwTDMRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 1),
    _JnxpwTDMRate_Type()
)
jnxpwTDMRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMRate.setStatus("current")
_JnxpwTDMIfIndex_Type = InterfaceIndexOrZero
_JnxpwTDMIfIndex_Object = MibTableColumn
jnxpwTDMIfIndex = _JnxpwTDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 2),
    _JnxpwTDMIfIndex_Type()
)
jnxpwTDMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMIfIndex.setStatus("current")
_JnxpwGenTDMCfgIndex_Type = JnxPwCfgIndexOrzero
_JnxpwGenTDMCfgIndex_Object = MibTableColumn
jnxpwGenTDMCfgIndex = _JnxpwGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 3),
    _JnxpwGenTDMCfgIndex_Type()
)
jnxpwGenTDMCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwGenTDMCfgIndex.setStatus("current")
_JnxpwRelTDMCfgIndex_Type = JnxPwCfgIndexOrzero
_JnxpwRelTDMCfgIndex_Object = MibTableColumn
jnxpwRelTDMCfgIndex = _JnxpwRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 4),
    _JnxpwRelTDMCfgIndex_Type()
)
jnxpwRelTDMCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwRelTDMCfgIndex.setStatus("current")


class _JnxpwTDMConfigError_Type(Bits):
    """Custom type jnxpwTDMConfigError based on Bits"""
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("peerPayloadSizeIncompatible", 3),
          ("peerRtpIncompatible", 2),
          ("tdmTypeIncompatible", 1))
    )

_JnxpwTDMConfigError_Type.__name__ = "Bits"
_JnxpwTDMConfigError_Object = MibTableColumn
jnxpwTDMConfigError = _JnxpwTDMConfigError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 5),
    _JnxpwTDMConfigError_Type()
)
jnxpwTDMConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMConfigError.setStatus("current")


class _JnxpwTDMTimeElapsed_Type(Integer32):
    """Custom type jnxpwTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_JnxpwTDMTimeElapsed_Type.__name__ = "Integer32"
_JnxpwTDMTimeElapsed_Object = MibTableColumn
jnxpwTDMTimeElapsed = _JnxpwTDMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 6),
    _JnxpwTDMTimeElapsed_Type()
)
jnxpwTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMTimeElapsed.setStatus("current")


class _JnxpwTDMValidIntervals_Type(Integer32):
    """Custom type jnxpwTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_JnxpwTDMValidIntervals_Type.__name__ = "Integer32"
_JnxpwTDMValidIntervals_Object = MibTableColumn
jnxpwTDMValidIntervals = _JnxpwTDMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 7),
    _JnxpwTDMValidIntervals_Type()
)
jnxpwTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMValidIntervals.setStatus("current")


class _JnxpwTDMValidDayIntervals_Type(Integer32):
    """Custom type jnxpwTDMValidDayIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_JnxpwTDMValidDayIntervals_Type.__name__ = "Integer32"
_JnxpwTDMValidDayIntervals_Object = MibTableColumn
jnxpwTDMValidDayIntervals = _JnxpwTDMValidDayIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 8),
    _JnxpwTDMValidDayIntervals_Type()
)
jnxpwTDMValidDayIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMValidDayIntervals.setStatus("current")
_JnxpwTDMLastEsTimeStamp_Type = TimeStamp
_JnxpwTDMLastEsTimeStamp_Object = MibTableColumn
jnxpwTDMLastEsTimeStamp = _JnxpwTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 1, 1, 11),
    _JnxpwTDMLastEsTimeStamp_Type()
)
jnxpwTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMLastEsTimeStamp.setStatus("current")
_JnxpwTDMCfgIndexNext_Type = Unsigned32
_JnxpwTDMCfgIndexNext_Object = MibScalar
jnxpwTDMCfgIndexNext = _JnxpwTDMCfgIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 2),
    _JnxpwTDMCfgIndexNext_Type()
)
jnxpwTDMCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgIndexNext.setStatus("current")
_JnxpwTDMCfgTable_Object = MibTable
jnxpwTDMCfgTable = _JnxpwTDMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxpwTDMCfgTable.setStatus("current")
_JnxpwTDMCfgEntry_Object = MibTableRow
jnxpwTDMCfgEntry = _JnxpwTDMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1)
)
jnxpwTDMCfgEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
)
if mibBuilder.loadTexts:
    jnxpwTDMCfgEntry.setStatus("current")
_JnxpwTDMCfgIndex_Type = JnxPwTDMCfgIndex
_JnxpwTDMCfgIndex_Object = MibTableColumn
jnxpwTDMCfgIndex = _JnxpwTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 1),
    _JnxpwTDMCfgIndex_Type()
)
jnxpwTDMCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxpwTDMCfgIndex.setStatus("current")
_JnxpwTDMCfgRowStatus_Type = RowStatus
_JnxpwTDMCfgRowStatus_Object = MibTableColumn
jnxpwTDMCfgRowStatus = _JnxpwTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 2),
    _JnxpwTDMCfgRowStatus_Type()
)
jnxpwTDMCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgRowStatus.setStatus("current")
_JnxpwTDMCfgPayloadSize_Type = Unsigned32
_JnxpwTDMCfgPayloadSize_Object = MibTableColumn
jnxpwTDMCfgPayloadSize = _JnxpwTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 4),
    _JnxpwTDMCfgPayloadSize_Type()
)
jnxpwTDMCfgPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgPayloadSize.setStatus("current")
_JnxpwTDMCfgPktReorder_Type = TruthValue
_JnxpwTDMCfgPktReorder_Object = MibTableColumn
jnxpwTDMCfgPktReorder = _JnxpwTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 5),
    _JnxpwTDMCfgPktReorder_Type()
)
jnxpwTDMCfgPktReorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgPktReorder.setStatus("current")


class _JnxpwTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type jnxpwTDMCfgRtpHdrUsed based on TruthValue"""


_JnxpwTDMCfgRtpHdrUsed_Object = MibTableColumn
jnxpwTDMCfgRtpHdrUsed = _JnxpwTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 6),
    _JnxpwTDMCfgRtpHdrUsed_Type()
)
jnxpwTDMCfgRtpHdrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgRtpHdrUsed.setStatus("current")


class _JnxpwTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type jnxpwTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3000


_JnxpwTDMCfgJtrBfrDepth_Object = MibTableColumn
jnxpwTDMCfgJtrBfrDepth = _JnxpwTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 7),
    _JnxpwTDMCfgJtrBfrDepth_Type()
)
jnxpwTDMCfgJtrBfrDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    jnxpwTDMCfgJtrBfrDepth.setUnits("microsecond")


class _JnxpwTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type jnxpwTDMCfgPayloadSuppression based on Integer32"""
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


_JnxpwTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_JnxpwTDMCfgPayloadSuppression_Object = MibTableColumn
jnxpwTDMCfgPayloadSuppression = _JnxpwTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 8),
    _JnxpwTDMCfgPayloadSuppression_Type()
)
jnxpwTDMCfgPayloadSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgPayloadSuppression.setStatus("current")


class _JnxpwTDMCfgConsecPktsInSynch_Type(Unsigned32):
    """Custom type jnxpwTDMCfgConsecPktsInSynch based on Unsigned32"""
    defaultValue = 2


_JnxpwTDMCfgConsecPktsInSynch_Object = MibTableColumn
jnxpwTDMCfgConsecPktsInSynch = _JnxpwTDMCfgConsecPktsInSynch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 9),
    _JnxpwTDMCfgConsecPktsInSynch_Type()
)
jnxpwTDMCfgConsecPktsInSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgConsecPktsInSynch.setStatus("current")


class _JnxpwTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):
    """Custom type jnxpwTDMCfgConsecMissPktsOutSynch based on Unsigned32"""
    defaultValue = 10


_JnxpwTDMCfgConsecMissPktsOutSynch_Object = MibTableColumn
jnxpwTDMCfgConsecMissPktsOutSynch = _JnxpwTDMCfgConsecMissPktsOutSynch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 10),
    _JnxpwTDMCfgConsecMissPktsOutSynch_Type()
)
jnxpwTDMCfgConsecMissPktsOutSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgConsecMissPktsOutSynch.setStatus("current")


class _JnxpwTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):
    """Custom type jnxpwTDMCfgSetUp2SynchTimeOut based on Unsigned32"""
    defaultValue = 5000


_JnxpwTDMCfgSetUp2SynchTimeOut_Object = MibTableColumn
jnxpwTDMCfgSetUp2SynchTimeOut = _JnxpwTDMCfgSetUp2SynchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 11),
    _JnxpwTDMCfgSetUp2SynchTimeOut_Type()
)
jnxpwTDMCfgSetUp2SynchTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgSetUp2SynchTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxpwTDMCfgSetUp2SynchTimeOut.setUnits("millisecond")


class _JnxpwTDMCfgPktReplacePolicy_Type(Integer32):
    """Custom type jnxpwTDMCfgPktReplacePolicy based on Integer32"""
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
        *(("allOnes", 1),
          ("filler", 3),
          ("implementationSpecific", 2))
    )


_JnxpwTDMCfgPktReplacePolicy_Type.__name__ = "Integer32"
_JnxpwTDMCfgPktReplacePolicy_Object = MibTableColumn
jnxpwTDMCfgPktReplacePolicy = _JnxpwTDMCfgPktReplacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 12),
    _JnxpwTDMCfgPktReplacePolicy_Type()
)
jnxpwTDMCfgPktReplacePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgPktReplacePolicy.setStatus("current")
_JnxpwTDMCfgAvePktLossTimeWindow_Type = Integer32
_JnxpwTDMCfgAvePktLossTimeWindow_Object = MibTableColumn
jnxpwTDMCfgAvePktLossTimeWindow = _JnxpwTDMCfgAvePktLossTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 13),
    _JnxpwTDMCfgAvePktLossTimeWindow_Type()
)
jnxpwTDMCfgAvePktLossTimeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgAvePktLossTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    jnxpwTDMCfgAvePktLossTimeWindow.setUnits("millisecond")
_JnxpwTDMCfgExcessivePktLossThreshold_Type = Unsigned32
_JnxpwTDMCfgExcessivePktLossThreshold_Object = MibTableColumn
jnxpwTDMCfgExcessivePktLossThreshold = _JnxpwTDMCfgExcessivePktLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 14),
    _JnxpwTDMCfgExcessivePktLossThreshold_Type()
)
jnxpwTDMCfgExcessivePktLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgExcessivePktLossThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxpwTDMCfgExcessivePktLossThreshold.setUnits("Percent")


class _JnxpwTDMCfgAlarmThreshold_Type(Unsigned32):
    """Custom type jnxpwTDMCfgAlarmThreshold based on Unsigned32"""
    defaultValue = 2500


_JnxpwTDMCfgAlarmThreshold_Object = MibTableColumn
jnxpwTDMCfgAlarmThreshold = _JnxpwTDMCfgAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 15),
    _JnxpwTDMCfgAlarmThreshold_Type()
)
jnxpwTDMCfgAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgAlarmThreshold.setStatus("current")


class _JnxpwTDMCfgClearAlarmThreshold_Type(Unsigned32):
    """Custom type jnxpwTDMCfgClearAlarmThreshold based on Unsigned32"""
    defaultValue = 10000


_JnxpwTDMCfgClearAlarmThreshold_Object = MibTableColumn
jnxpwTDMCfgClearAlarmThreshold = _JnxpwTDMCfgClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 16),
    _JnxpwTDMCfgClearAlarmThreshold_Type()
)
jnxpwTDMCfgClearAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgClearAlarmThreshold.setStatus("current")


class _JnxpwTDMCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type jnxpwTDMCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 30


_JnxpwTDMCfgMissingPktsToSes_Object = MibTableColumn
jnxpwTDMCfgMissingPktsToSes = _JnxpwTDMCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 17),
    _JnxpwTDMCfgMissingPktsToSes_Type()
)
jnxpwTDMCfgMissingPktsToSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    jnxpwTDMCfgMissingPktsToSes.setUnits("Percent")


class _JnxpwTDMCfgTimestampMode_Type(Integer32):
    """Custom type jnxpwTDMCfgTimestampMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("differential", 3),
          ("notApplicable", 1))
    )


_JnxpwTDMCfgTimestampMode_Type.__name__ = "Integer32"
_JnxpwTDMCfgTimestampMode_Object = MibTableColumn
jnxpwTDMCfgTimestampMode = _JnxpwTDMCfgTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 18),
    _JnxpwTDMCfgTimestampMode_Type()
)
jnxpwTDMCfgTimestampMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgTimestampMode.setStatus("current")
_JnxpwTDMCfgStorageType_Type = StorageType
_JnxpwTDMCfgStorageType_Object = MibTableColumn
jnxpwTDMCfgStorageType = _JnxpwTDMCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 19),
    _JnxpwTDMCfgStorageType_Type()
)
jnxpwTDMCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgStorageType.setStatus("current")


class _JnxpwTDMCfgPktFiller_Type(Unsigned32):
    """Custom type jnxpwTDMCfgPktFiller based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxpwTDMCfgPktFiller_Type.__name__ = "Unsigned32"
_JnxpwTDMCfgPktFiller_Object = MibTableColumn
jnxpwTDMCfgPktFiller = _JnxpwTDMCfgPktFiller_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 20),
    _JnxpwTDMCfgPktFiller_Type()
)
jnxpwTDMCfgPktFiller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgPktFiller.setStatus("current")
_JnxpwTDMCfgName_Type = SnmpAdminString
_JnxpwTDMCfgName_Object = MibTableColumn
jnxpwTDMCfgName = _JnxpwTDMCfgName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 3, 1, 21),
    _JnxpwTDMCfgName_Type()
)
jnxpwTDMCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMCfgName.setStatus("current")
_JnxpwTDMPerfCurrentTable_Object = MibTable
jnxpwTDMPerfCurrentTable = _JnxpwTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentTable.setStatus("current")
_JnxpwTDMPerfCurrentEntry_Object = MibTableRow
jnxpwTDMPerfCurrentEntry = _JnxpwTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1)
)
jnxpwTDMPerfCurrentEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentEntry.setStatus("current")
_JnxpwTDMPerfCurrentMissingPkts_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentMissingPkts_Object = MibTableColumn
jnxpwTDMPerfCurrentMissingPkts = _JnxpwTDMPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 1),
    _JnxpwTDMPerfCurrentMissingPkts_Type()
)
jnxpwTDMPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentMissingPkts.setStatus("current")
_JnxpwTDMPerfCurrentPktsReOrder_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentPktsReOrder_Object = MibTableColumn
jnxpwTDMPerfCurrentPktsReOrder = _JnxpwTDMPerfCurrentPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 2),
    _JnxpwTDMPerfCurrentPktsReOrder_Type()
)
jnxpwTDMPerfCurrentPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentPktsReOrder.setStatus("current")
_JnxpwTDMPerfCurrentJtrBfrUnderruns_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
jnxpwTDMPerfCurrentJtrBfrUnderruns = _JnxpwTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 3),
    _JnxpwTDMPerfCurrentJtrBfrUnderruns_Type()
)
jnxpwTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_JnxpwTDMPerfCurrentMisOrderDropped_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentMisOrderDropped_Object = MibTableColumn
jnxpwTDMPerfCurrentMisOrderDropped = _JnxpwTDMPerfCurrentMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 4),
    _JnxpwTDMPerfCurrentMisOrderDropped_Type()
)
jnxpwTDMPerfCurrentMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentMisOrderDropped.setStatus("current")
_JnxpwTDMPerfCurrentMalformedPkt_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentMalformedPkt_Object = MibTableColumn
jnxpwTDMPerfCurrentMalformedPkt = _JnxpwTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 5),
    _JnxpwTDMPerfCurrentMalformedPkt_Type()
)
jnxpwTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentMalformedPkt.setStatus("current")
_JnxpwTDMPerfCurrentESs_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentESs_Object = MibTableColumn
jnxpwTDMPerfCurrentESs = _JnxpwTDMPerfCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 6),
    _JnxpwTDMPerfCurrentESs_Type()
)
jnxpwTDMPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentESs.setStatus("current")
_JnxpwTDMPerfCurrentSESs_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentSESs_Object = MibTableColumn
jnxpwTDMPerfCurrentSESs = _JnxpwTDMPerfCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 7),
    _JnxpwTDMPerfCurrentSESs_Type()
)
jnxpwTDMPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentSESs.setStatus("current")
_JnxpwTDMPerfCurrentUASs_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentUASs_Object = MibTableColumn
jnxpwTDMPerfCurrentUASs = _JnxpwTDMPerfCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 8),
    _JnxpwTDMPerfCurrentUASs_Type()
)
jnxpwTDMPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentUASs.setStatus("current")
_JnxpwTDMPerfCurrentFC_Type = PerfCurrentCount
_JnxpwTDMPerfCurrentFC_Object = MibTableColumn
jnxpwTDMPerfCurrentFC = _JnxpwTDMPerfCurrentFC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 5, 1, 9),
    _JnxpwTDMPerfCurrentFC_Type()
)
jnxpwTDMPerfCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentFC.setStatus("current")
_JnxpwTDMPerfIntervalTable_Object = MibTable
jnxpwTDMPerfIntervalTable = _JnxpwTDMPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalTable.setStatus("current")
_JnxpwTDMPerfIntervalEntry_Object = MibTableRow
jnxpwTDMPerfIntervalEntry = _JnxpwTDMPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1)
)
jnxpwTDMPerfIntervalEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
    (0, "JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalEntry.setStatus("current")
_JnxpwTDMPerfIntervalNumber_Type = Unsigned32
_JnxpwTDMPerfIntervalNumber_Object = MibTableColumn
jnxpwTDMPerfIntervalNumber = _JnxpwTDMPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 1),
    _JnxpwTDMPerfIntervalNumber_Type()
)
jnxpwTDMPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalNumber.setStatus("current")
_JnxpwTDMPerfIntervalValidData_Type = TruthValue
_JnxpwTDMPerfIntervalValidData_Object = MibTableColumn
jnxpwTDMPerfIntervalValidData = _JnxpwTDMPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 2),
    _JnxpwTDMPerfIntervalValidData_Type()
)
jnxpwTDMPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalValidData.setStatus("current")
_JnxpwTDMPerfIntervalDuration_Type = Unsigned32
_JnxpwTDMPerfIntervalDuration_Object = MibTableColumn
jnxpwTDMPerfIntervalDuration = _JnxpwTDMPerfIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 3),
    _JnxpwTDMPerfIntervalDuration_Type()
)
jnxpwTDMPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalDuration.setStatus("current")
_JnxpwTDMPerfIntervalMissingPkts_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalMissingPkts_Object = MibTableColumn
jnxpwTDMPerfIntervalMissingPkts = _JnxpwTDMPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 4),
    _JnxpwTDMPerfIntervalMissingPkts_Type()
)
jnxpwTDMPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalMissingPkts.setStatus("current")
_JnxpwTDMPerfIntervalPktsReOrder_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalPktsReOrder_Object = MibTableColumn
jnxpwTDMPerfIntervalPktsReOrder = _JnxpwTDMPerfIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 5),
    _JnxpwTDMPerfIntervalPktsReOrder_Type()
)
jnxpwTDMPerfIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalPktsReOrder.setStatus("current")
_JnxpwTDMPerfIntervalJtrBfrUnderruns_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
jnxpwTDMPerfIntervalJtrBfrUnderruns = _JnxpwTDMPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 6),
    _JnxpwTDMPerfIntervalJtrBfrUnderruns_Type()
)
jnxpwTDMPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalJtrBfrUnderruns.setStatus("current")
_JnxpwTDMPerfIntervalMisOrderDropped_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalMisOrderDropped_Object = MibTableColumn
jnxpwTDMPerfIntervalMisOrderDropped = _JnxpwTDMPerfIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 7),
    _JnxpwTDMPerfIntervalMisOrderDropped_Type()
)
jnxpwTDMPerfIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalMisOrderDropped.setStatus("current")
_JnxpwTDMPerfIntervalMalformedPkt_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalMalformedPkt_Object = MibTableColumn
jnxpwTDMPerfIntervalMalformedPkt = _JnxpwTDMPerfIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 8),
    _JnxpwTDMPerfIntervalMalformedPkt_Type()
)
jnxpwTDMPerfIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalMalformedPkt.setStatus("current")
_JnxpwTDMPerfIntervalESs_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalESs_Object = MibTableColumn
jnxpwTDMPerfIntervalESs = _JnxpwTDMPerfIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 9),
    _JnxpwTDMPerfIntervalESs_Type()
)
jnxpwTDMPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalESs.setStatus("current")
_JnxpwTDMPerfIntervalSESs_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalSESs_Object = MibTableColumn
jnxpwTDMPerfIntervalSESs = _JnxpwTDMPerfIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 10),
    _JnxpwTDMPerfIntervalSESs_Type()
)
jnxpwTDMPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalSESs.setStatus("current")
_JnxpwTDMPerfIntervalUASs_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalUASs_Object = MibTableColumn
jnxpwTDMPerfIntervalUASs = _JnxpwTDMPerfIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 11),
    _JnxpwTDMPerfIntervalUASs_Type()
)
jnxpwTDMPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalUASs.setStatus("current")
_JnxpwTDMPerfIntervalFC_Type = PerfIntervalCount
_JnxpwTDMPerfIntervalFC_Object = MibTableColumn
jnxpwTDMPerfIntervalFC = _JnxpwTDMPerfIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 6, 1, 12),
    _JnxpwTDMPerfIntervalFC_Type()
)
jnxpwTDMPerfIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalFC.setStatus("current")
_JnxpwTDMPerf1DayIntervalTable_Object = MibTable
jnxpwTDMPerf1DayIntervalTable = _JnxpwTDMPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalTable.setStatus("current")
_JnxpwTDMPerf1DayIntervalEntry_Object = MibTableRow
jnxpwTDMPerf1DayIntervalEntry = _JnxpwTDMPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1)
)
jnxpwTDMPerf1DayIntervalEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
    (0, "JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalEntry.setStatus("current")
_JnxpwTDMPerf1DayIntervalNumber_Type = Unsigned32
_JnxpwTDMPerf1DayIntervalNumber_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalNumber = _JnxpwTDMPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 1),
    _JnxpwTDMPerf1DayIntervalNumber_Type()
)
jnxpwTDMPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalNumber.setStatus("current")
_JnxpwTDMPerf1DayIntervalValidData_Type = TruthValue
_JnxpwTDMPerf1DayIntervalValidData_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalValidData = _JnxpwTDMPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 2),
    _JnxpwTDMPerf1DayIntervalValidData_Type()
)
jnxpwTDMPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalValidData.setStatus("current")
_JnxpwTDMPerf1DayIntervalDuration_Type = Unsigned32
_JnxpwTDMPerf1DayIntervalDuration_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalDuration = _JnxpwTDMPerf1DayIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 3),
    _JnxpwTDMPerf1DayIntervalDuration_Type()
)
jnxpwTDMPerf1DayIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalDuration.setStatus("current")
_JnxpwTDMPerf1DayIntervalMissingPkts_Type = Counter32
_JnxpwTDMPerf1DayIntervalMissingPkts_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalMissingPkts = _JnxpwTDMPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 4),
    _JnxpwTDMPerf1DayIntervalMissingPkts_Type()
)
jnxpwTDMPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalMissingPkts.setStatus("current")
_JnxpwTDMPerf1DayIntervalPktsReOrder_Type = Counter32
_JnxpwTDMPerf1DayIntervalPktsReOrder_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalPktsReOrder = _JnxpwTDMPerf1DayIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 5),
    _JnxpwTDMPerf1DayIntervalPktsReOrder_Type()
)
jnxpwTDMPerf1DayIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalPktsReOrder.setStatus("current")
_JnxpwTDMPerf1DayIntervalJtrBfrUnderruns_Type = Counter32
_JnxpwTDMPerf1DayIntervalJtrBfrUnderruns_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalJtrBfrUnderruns = _JnxpwTDMPerf1DayIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 6),
    _JnxpwTDMPerf1DayIntervalJtrBfrUnderruns_Type()
)
jnxpwTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalJtrBfrUnderruns.setStatus("current")
_JnxpwTDMPerf1DayIntervalMisOrderDropped_Type = Counter32
_JnxpwTDMPerf1DayIntervalMisOrderDropped_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalMisOrderDropped = _JnxpwTDMPerf1DayIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 7),
    _JnxpwTDMPerf1DayIntervalMisOrderDropped_Type()
)
jnxpwTDMPerf1DayIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalMisOrderDropped.setStatus("current")
_JnxpwTDMPerf1DayIntervalMalformedPkt_Type = Counter32
_JnxpwTDMPerf1DayIntervalMalformedPkt_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalMalformedPkt = _JnxpwTDMPerf1DayIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 8),
    _JnxpwTDMPerf1DayIntervalMalformedPkt_Type()
)
jnxpwTDMPerf1DayIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalMalformedPkt.setStatus("current")
_JnxpwTDMPerf1DayIntervalESs_Type = Counter32
_JnxpwTDMPerf1DayIntervalESs_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalESs = _JnxpwTDMPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 9),
    _JnxpwTDMPerf1DayIntervalESs_Type()
)
jnxpwTDMPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalESs.setStatus("current")
_JnxpwTDMPerf1DayIntervalSESs_Type = Counter32
_JnxpwTDMPerf1DayIntervalSESs_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalSESs = _JnxpwTDMPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 10),
    _JnxpwTDMPerf1DayIntervalSESs_Type()
)
jnxpwTDMPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalSESs.setStatus("current")
_JnxpwTDMPerf1DayIntervalUASs_Type = Counter32
_JnxpwTDMPerf1DayIntervalUASs_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalUASs = _JnxpwTDMPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 11),
    _JnxpwTDMPerf1DayIntervalUASs_Type()
)
jnxpwTDMPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalUASs.setStatus("current")
_JnxpwTDMPerf1DayIntervalFC_Type = Counter32
_JnxpwTDMPerf1DayIntervalFC_Object = MibTableColumn
jnxpwTDMPerf1DayIntervalFC = _JnxpwTDMPerf1DayIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 1, 7, 1, 12),
    _JnxpwTDMPerf1DayIntervalFC_Type()
)
jnxpwTDMPerf1DayIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalFC.setStatus("current")
_JnxpwTDMNotifications_ObjectIdentity = ObjectIdentity
jnxpwTDMNotifications = _JnxpwTDMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 2)
)
_JnxpwTDMConformance_ObjectIdentity = ObjectIdentity
jnxpwTDMConformance = _JnxpwTDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3)
)
_JnxpwTDMGroups_ObjectIdentity = ObjectIdentity
jnxpwTDMGroups = _JnxpwTDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 1)
)
_JnxpwTDMCompliances_ObjectIdentity = ObjectIdentity
jnxpwTDMCompliances = _JnxpwTDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 2)
)

# Managed Objects groups

jnxpwTDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 1, 1)
)
jnxpwTDMGroup.setObjects(
      *(("JUNIPER-PW-TDM-MIB", "jnxpwTDMRate"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMIfIndex"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwGenTDMCfgIndex"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwRelTDMCfgIndex"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMConfigError"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMTimeElapsed"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMValidIntervals"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMValidDayIntervals"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMLastEsTimeStamp"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgIndexNext"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgRowStatus"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgPayloadSize"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgPktReorder"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgRtpHdrUsed"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgJtrBfrDepth"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgPayloadSuppression"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgConsecPktsInSynch"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgConsecMissPktsOutSynch"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgSetUp2SynchTimeOut"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgPktReplacePolicy"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgAvePktLossTimeWindow"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgExcessivePktLossThreshold"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgAlarmThreshold"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgClearAlarmThreshold"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgMissingPktsToSes"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgTimestampMode"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgStorageType"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgPktFiller"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMCfgName"))
)
if mibBuilder.loadTexts:
    jnxpwTDMGroup.setStatus("current")

jnxpwTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 1, 2)
)
jnxpwTDMPerfCurrentGroup.setObjects(
      *(("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentMissingPkts"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentPktsReOrder"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentJtrBfrUnderruns"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentMisOrderDropped"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentMalformedPkt"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentSESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentUASs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfCurrentFC"))
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfCurrentGroup.setStatus("current")

jnxpwTDMPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 1, 3)
)
jnxpwTDMPerfIntervalGroup.setObjects(
      *(("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalValidData"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalDuration"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalMissingPkts"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalPktsReOrder"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalJtrBfrUnderruns"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalMisOrderDropped"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalMalformedPkt"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalSESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalUASs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerfIntervalFC"))
)
if mibBuilder.loadTexts:
    jnxpwTDMPerfIntervalGroup.setStatus("current")

jnxpwTDMPerf1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 1, 4)
)
jnxpwTDMPerf1DayIntervalGroup.setObjects(
      *(("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalValidData"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalDuration"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalMissingPkts"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalPktsReOrder"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalJtrBfrUnderruns"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalMisOrderDropped"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalMalformedPkt"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalSESs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalUASs"),
        ("JUNIPER-PW-TDM-MIB", "jnxpwTDMPerf1DayIntervalFC"))
)
if mibBuilder.loadTexts:
    jnxpwTDMPerf1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

jnxpwTDMModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    jnxpwTDMModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-PW-TDM-MIB",
    **{"JnxPwTDMCfgIndex": JnxPwTDMCfgIndex,
       "JnxPwCfgIndexOrzero": JnxPwCfgIndexOrzero,
       "jnxPWTdmMIB": jnxPWTdmMIB,
       "jnxpwTDMObjects": jnxpwTDMObjects,
       "jnxpwTDMTable": jnxpwTDMTable,
       "jnxpwTDMEntry": jnxpwTDMEntry,
       "jnxpwTDMRate": jnxpwTDMRate,
       "jnxpwTDMIfIndex": jnxpwTDMIfIndex,
       "jnxpwGenTDMCfgIndex": jnxpwGenTDMCfgIndex,
       "jnxpwRelTDMCfgIndex": jnxpwRelTDMCfgIndex,
       "jnxpwTDMConfigError": jnxpwTDMConfigError,
       "jnxpwTDMTimeElapsed": jnxpwTDMTimeElapsed,
       "jnxpwTDMValidIntervals": jnxpwTDMValidIntervals,
       "jnxpwTDMValidDayIntervals": jnxpwTDMValidDayIntervals,
       "jnxpwTDMLastEsTimeStamp": jnxpwTDMLastEsTimeStamp,
       "jnxpwTDMCfgIndexNext": jnxpwTDMCfgIndexNext,
       "jnxpwTDMCfgTable": jnxpwTDMCfgTable,
       "jnxpwTDMCfgEntry": jnxpwTDMCfgEntry,
       "jnxpwTDMCfgIndex": jnxpwTDMCfgIndex,
       "jnxpwTDMCfgRowStatus": jnxpwTDMCfgRowStatus,
       "jnxpwTDMCfgPayloadSize": jnxpwTDMCfgPayloadSize,
       "jnxpwTDMCfgPktReorder": jnxpwTDMCfgPktReorder,
       "jnxpwTDMCfgRtpHdrUsed": jnxpwTDMCfgRtpHdrUsed,
       "jnxpwTDMCfgJtrBfrDepth": jnxpwTDMCfgJtrBfrDepth,
       "jnxpwTDMCfgPayloadSuppression": jnxpwTDMCfgPayloadSuppression,
       "jnxpwTDMCfgConsecPktsInSynch": jnxpwTDMCfgConsecPktsInSynch,
       "jnxpwTDMCfgConsecMissPktsOutSynch": jnxpwTDMCfgConsecMissPktsOutSynch,
       "jnxpwTDMCfgSetUp2SynchTimeOut": jnxpwTDMCfgSetUp2SynchTimeOut,
       "jnxpwTDMCfgPktReplacePolicy": jnxpwTDMCfgPktReplacePolicy,
       "jnxpwTDMCfgAvePktLossTimeWindow": jnxpwTDMCfgAvePktLossTimeWindow,
       "jnxpwTDMCfgExcessivePktLossThreshold": jnxpwTDMCfgExcessivePktLossThreshold,
       "jnxpwTDMCfgAlarmThreshold": jnxpwTDMCfgAlarmThreshold,
       "jnxpwTDMCfgClearAlarmThreshold": jnxpwTDMCfgClearAlarmThreshold,
       "jnxpwTDMCfgMissingPktsToSes": jnxpwTDMCfgMissingPktsToSes,
       "jnxpwTDMCfgTimestampMode": jnxpwTDMCfgTimestampMode,
       "jnxpwTDMCfgStorageType": jnxpwTDMCfgStorageType,
       "jnxpwTDMCfgPktFiller": jnxpwTDMCfgPktFiller,
       "jnxpwTDMCfgName": jnxpwTDMCfgName,
       "jnxpwTDMPerfCurrentTable": jnxpwTDMPerfCurrentTable,
       "jnxpwTDMPerfCurrentEntry": jnxpwTDMPerfCurrentEntry,
       "jnxpwTDMPerfCurrentMissingPkts": jnxpwTDMPerfCurrentMissingPkts,
       "jnxpwTDMPerfCurrentPktsReOrder": jnxpwTDMPerfCurrentPktsReOrder,
       "jnxpwTDMPerfCurrentJtrBfrUnderruns": jnxpwTDMPerfCurrentJtrBfrUnderruns,
       "jnxpwTDMPerfCurrentMisOrderDropped": jnxpwTDMPerfCurrentMisOrderDropped,
       "jnxpwTDMPerfCurrentMalformedPkt": jnxpwTDMPerfCurrentMalformedPkt,
       "jnxpwTDMPerfCurrentESs": jnxpwTDMPerfCurrentESs,
       "jnxpwTDMPerfCurrentSESs": jnxpwTDMPerfCurrentSESs,
       "jnxpwTDMPerfCurrentUASs": jnxpwTDMPerfCurrentUASs,
       "jnxpwTDMPerfCurrentFC": jnxpwTDMPerfCurrentFC,
       "jnxpwTDMPerfIntervalTable": jnxpwTDMPerfIntervalTable,
       "jnxpwTDMPerfIntervalEntry": jnxpwTDMPerfIntervalEntry,
       "jnxpwTDMPerfIntervalNumber": jnxpwTDMPerfIntervalNumber,
       "jnxpwTDMPerfIntervalValidData": jnxpwTDMPerfIntervalValidData,
       "jnxpwTDMPerfIntervalDuration": jnxpwTDMPerfIntervalDuration,
       "jnxpwTDMPerfIntervalMissingPkts": jnxpwTDMPerfIntervalMissingPkts,
       "jnxpwTDMPerfIntervalPktsReOrder": jnxpwTDMPerfIntervalPktsReOrder,
       "jnxpwTDMPerfIntervalJtrBfrUnderruns": jnxpwTDMPerfIntervalJtrBfrUnderruns,
       "jnxpwTDMPerfIntervalMisOrderDropped": jnxpwTDMPerfIntervalMisOrderDropped,
       "jnxpwTDMPerfIntervalMalformedPkt": jnxpwTDMPerfIntervalMalformedPkt,
       "jnxpwTDMPerfIntervalESs": jnxpwTDMPerfIntervalESs,
       "jnxpwTDMPerfIntervalSESs": jnxpwTDMPerfIntervalSESs,
       "jnxpwTDMPerfIntervalUASs": jnxpwTDMPerfIntervalUASs,
       "jnxpwTDMPerfIntervalFC": jnxpwTDMPerfIntervalFC,
       "jnxpwTDMPerf1DayIntervalTable": jnxpwTDMPerf1DayIntervalTable,
       "jnxpwTDMPerf1DayIntervalEntry": jnxpwTDMPerf1DayIntervalEntry,
       "jnxpwTDMPerf1DayIntervalNumber": jnxpwTDMPerf1DayIntervalNumber,
       "jnxpwTDMPerf1DayIntervalValidData": jnxpwTDMPerf1DayIntervalValidData,
       "jnxpwTDMPerf1DayIntervalDuration": jnxpwTDMPerf1DayIntervalDuration,
       "jnxpwTDMPerf1DayIntervalMissingPkts": jnxpwTDMPerf1DayIntervalMissingPkts,
       "jnxpwTDMPerf1DayIntervalPktsReOrder": jnxpwTDMPerf1DayIntervalPktsReOrder,
       "jnxpwTDMPerf1DayIntervalJtrBfrUnderruns": jnxpwTDMPerf1DayIntervalJtrBfrUnderruns,
       "jnxpwTDMPerf1DayIntervalMisOrderDropped": jnxpwTDMPerf1DayIntervalMisOrderDropped,
       "jnxpwTDMPerf1DayIntervalMalformedPkt": jnxpwTDMPerf1DayIntervalMalformedPkt,
       "jnxpwTDMPerf1DayIntervalESs": jnxpwTDMPerf1DayIntervalESs,
       "jnxpwTDMPerf1DayIntervalSESs": jnxpwTDMPerf1DayIntervalSESs,
       "jnxpwTDMPerf1DayIntervalUASs": jnxpwTDMPerf1DayIntervalUASs,
       "jnxpwTDMPerf1DayIntervalFC": jnxpwTDMPerf1DayIntervalFC,
       "jnxpwTDMNotifications": jnxpwTDMNotifications,
       "jnxpwTDMConformance": jnxpwTDMConformance,
       "jnxpwTDMGroups": jnxpwTDMGroups,
       "jnxpwTDMGroup": jnxpwTDMGroup,
       "jnxpwTDMPerfCurrentGroup": jnxpwTDMPerfCurrentGroup,
       "jnxpwTDMPerfIntervalGroup": jnxpwTDMPerfIntervalGroup,
       "jnxpwTDMPerf1DayIntervalGroup": jnxpwTDMPerf1DayIntervalGroup,
       "jnxpwTDMCompliances": jnxpwTDMCompliances,
       "jnxpwTDMModuleCompliance": jnxpwTDMModuleCompliance}
)
