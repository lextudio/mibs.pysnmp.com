# SNMP MIB module (RIVERSTONE-CMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-CMTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:43 2024
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

(docsIfCmtsModIndex,
 docsIfCmtsModIntervalUsageCode) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsModIndex",
    "docsIfCmtsModIntervalUsageCode")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RSTONE-SMI-MIB",
    "riverstoneMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsCmtsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11)
)
rsCmtsMib.setRevisions(
        ("2000-07-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsCmtsCmdStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("failed", 5),
          ("process", 3),
          ("startup", 2),
          ("success", 4),
          ("undefined", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RsCmtsBaseTable_Object = MibTable
rsCmtsBaseTable = _RsCmtsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1)
)
if mibBuilder.loadTexts:
    rsCmtsBaseTable.setStatus("current")
_RsCmtsBaseEntry_Object = MibTableRow
rsCmtsBaseEntry = _RsCmtsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1)
)
rsCmtsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsCmtsBaseEntry.setStatus("current")


class _RsCmtsBaseBpduFilter_Type(TruthValue):
    """Custom type rsCmtsBaseBpduFilter based on TruthValue"""


_RsCmtsBaseBpduFilter_Object = MibTableColumn
rsCmtsBaseBpduFilter = _RsCmtsBaseBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 2),
    _RsCmtsBaseBpduFilter_Type()
)
rsCmtsBaseBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseBpduFilter.setStatus("current")
_RsCmtsBaseBpduFilterHits_Type = Counter32
_RsCmtsBaseBpduFilterHits_Object = MibTableColumn
rsCmtsBaseBpduFilterHits = _RsCmtsBaseBpduFilterHits_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 3),
    _RsCmtsBaseBpduFilterHits_Type()
)
rsCmtsBaseBpduFilterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCmtsBaseBpduFilterHits.setStatus("current")


class _RsCmtsBaseNonIPFilter_Type(TruthValue):
    """Custom type rsCmtsBaseNonIPFilter based on TruthValue"""


_RsCmtsBaseNonIPFilter_Object = MibTableColumn
rsCmtsBaseNonIPFilter = _RsCmtsBaseNonIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 4),
    _RsCmtsBaseNonIPFilter_Type()
)
rsCmtsBaseNonIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseNonIPFilter.setStatus("current")
_RsCmtsBaseNonIPFilterHits_Type = Counter32
_RsCmtsBaseNonIPFilterHits_Object = MibTableColumn
rsCmtsBaseNonIPFilterHits = _RsCmtsBaseNonIPFilterHits_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 5),
    _RsCmtsBaseNonIPFilterHits_Type()
)
rsCmtsBaseNonIPFilterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCmtsBaseNonIPFilterHits.setStatus("current")


class _RsCmtsBaseMapLength_Type(Integer32):
    """Custom type rsCmtsBaseMapLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RsCmtsBaseMapLength_Type.__name__ = "Integer32"
_RsCmtsBaseMapLength_Object = MibTableColumn
rsCmtsBaseMapLength = _RsCmtsBaseMapLength_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 6),
    _RsCmtsBaseMapLength_Type()
)
rsCmtsBaseMapLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseMapLength.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsBaseMapLength.setUnits("Microseconds")


class _RsCmtsBaseMapLeadTime_Type(Integer32):
    """Custom type rsCmtsBaseMapLeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RsCmtsBaseMapLeadTime_Type.__name__ = "Integer32"
_RsCmtsBaseMapLeadTime_Object = MibTableColumn
rsCmtsBaseMapLeadTime = _RsCmtsBaseMapLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 7),
    _RsCmtsBaseMapLeadTime_Type()
)
rsCmtsBaseMapLeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseMapLeadTime.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsBaseMapLeadTime.setUnits("Microseconds")


class _RsCmtsBaseInitMaintLength_Type(Integer32):
    """Custom type rsCmtsBaseInitMaintLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_RsCmtsBaseInitMaintLength_Type.__name__ = "Integer32"
_RsCmtsBaseInitMaintLength_Object = MibTableColumn
rsCmtsBaseInitMaintLength = _RsCmtsBaseInitMaintLength_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 8),
    _RsCmtsBaseInitMaintLength_Type()
)
rsCmtsBaseInitMaintLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseInitMaintLength.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsBaseInitMaintLength.setUnits("Microseconds")


class _RsCmtsBase3137Config1_Type(Integer32):
    """Custom type rsCmtsBase3137Config1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsCmtsBase3137Config1_Type.__name__ = "Integer32"
_RsCmtsBase3137Config1_Object = MibTableColumn
rsCmtsBase3137Config1 = _RsCmtsBase3137Config1_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 9),
    _RsCmtsBase3137Config1_Type()
)
rsCmtsBase3137Config1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBase3137Config1.setStatus("current")


class _RsCmtsBase3137Config2_Type(Integer32):
    """Custom type rsCmtsBase3137Config2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsCmtsBase3137Config2_Type.__name__ = "Integer32"
_RsCmtsBase3137Config2_Object = MibTableColumn
rsCmtsBase3137Config2 = _RsCmtsBase3137Config2_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 10),
    _RsCmtsBase3137Config2_Type()
)
rsCmtsBase3137Config2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBase3137Config2.setStatus("current")


class _RsCmtsBaseConcatenation_Type(TruthValue):
    """Custom type rsCmtsBaseConcatenation based on TruthValue"""


_RsCmtsBaseConcatenation_Object = MibTableColumn
rsCmtsBaseConcatenation = _RsCmtsBaseConcatenation_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 11),
    _RsCmtsBaseConcatenation_Type()
)
rsCmtsBaseConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseConcatenation.setStatus("current")


class _RsCmtsBaseBpiHwAssist_Type(TruthValue):
    """Custom type rsCmtsBaseBpiHwAssist based on TruthValue"""


_RsCmtsBaseBpiHwAssist_Object = MibTableColumn
rsCmtsBaseBpiHwAssist = _RsCmtsBaseBpiHwAssist_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 12),
    _RsCmtsBaseBpiHwAssist_Type()
)
rsCmtsBaseBpiHwAssist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseBpiHwAssist.setStatus("current")
_RsCmtsBaseGenericCmd_Type = DisplayString
_RsCmtsBaseGenericCmd_Object = MibTableColumn
rsCmtsBaseGenericCmd = _RsCmtsBaseGenericCmd_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 13),
    _RsCmtsBaseGenericCmd_Type()
)
rsCmtsBaseGenericCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseGenericCmd.setStatus("current")
_RsCmtsBaseGenericCmdStatus_Type = RsCmtsCmdStatus
_RsCmtsBaseGenericCmdStatus_Object = MibTableColumn
rsCmtsBaseGenericCmdStatus = _RsCmtsBaseGenericCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 14),
    _RsCmtsBaseGenericCmdStatus_Type()
)
rsCmtsBaseGenericCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseGenericCmdStatus.setStatus("current")


class _RsCmtsBaseUccRetryInterval_Type(Integer32):
    """Custom type rsCmtsBaseUccRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RsCmtsBaseUccRetryInterval_Type.__name__ = "Integer32"
_RsCmtsBaseUccRetryInterval_Object = MibTableColumn
rsCmtsBaseUccRetryInterval = _RsCmtsBaseUccRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 15),
    _RsCmtsBaseUccRetryInterval_Type()
)
rsCmtsBaseUccRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsBaseUccRetryInterval.setStatus("current")
_RsCmtsBaseUccRetries_Type = Integer32
_RsCmtsBaseUccRetries_Object = MibTableColumn
rsCmtsBaseUccRetries = _RsCmtsBaseUccRetries_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 1, 1, 16),
    _RsCmtsBaseUccRetries_Type()
)
rsCmtsBaseUccRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCmtsBaseUccRetries.setStatus("current")
_RsCmtsUpstreamTable_Object = MibTable
rsCmtsUpstreamTable = _RsCmtsUpstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2)
)
if mibBuilder.loadTexts:
    rsCmtsUpstreamTable.setStatus("current")
_RsCmtsUpstreamEntry_Object = MibTableRow
rsCmtsUpstreamEntry = _RsCmtsUpstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1)
)
rsCmtsUpstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsCmtsUpstreamEntry.setStatus("current")
_RsCmtsUpstreamNominalRxPower_Type = Integer32
_RsCmtsUpstreamNominalRxPower_Object = MibTableColumn
rsCmtsUpstreamNominalRxPower = _RsCmtsUpstreamNominalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 1),
    _RsCmtsUpstreamNominalRxPower_Type()
)
rsCmtsUpstreamNominalRxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamNominalRxPower.setStatus("current")


class _RsCmtsUpstreamState_Type(TruthValue):
    """Custom type rsCmtsUpstreamState based on TruthValue"""


_RsCmtsUpstreamState_Object = MibTableColumn
rsCmtsUpstreamState = _RsCmtsUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 2),
    _RsCmtsUpstreamState_Type()
)
rsCmtsUpstreamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamState.setStatus("current")


class _RsCmtsUpstreamPolicing_Type(TruthValue):
    """Custom type rsCmtsUpstreamPolicing based on TruthValue"""


_RsCmtsUpstreamPolicing_Object = MibTableColumn
rsCmtsUpstreamPolicing = _RsCmtsUpstreamPolicing_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 3),
    _RsCmtsUpstreamPolicing_Type()
)
rsCmtsUpstreamPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamPolicing.setStatus("current")


class _RsCmtsUpstreamRangeInterval_Type(Integer32):
    """Custom type rsCmtsUpstreamRangeInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_RsCmtsUpstreamRangeInterval_Type.__name__ = "Integer32"
_RsCmtsUpstreamRangeInterval_Object = MibTableColumn
rsCmtsUpstreamRangeInterval = _RsCmtsUpstreamRangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 4),
    _RsCmtsUpstreamRangeInterval_Type()
)
rsCmtsUpstreamRangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamRangeInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsUpstreamRangeInterval.setUnits("Milliseconds")


class _RsCmtsUpstreamRangeRetryInterval_Type(Integer32):
    """Custom type rsCmtsUpstreamRangeRetryInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_RsCmtsUpstreamRangeRetryInterval_Type.__name__ = "Integer32"
_RsCmtsUpstreamRangeRetryInterval_Object = MibTableColumn
rsCmtsUpstreamRangeRetryInterval = _RsCmtsUpstreamRangeRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 5),
    _RsCmtsUpstreamRangeRetryInterval_Type()
)
rsCmtsUpstreamRangeRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamRangeRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsUpstreamRangeRetryInterval.setUnits("Milliseconds")


class _RsCmtsUpstreamPowerThreshold_Type(Integer32):
    """Custom type rsCmtsUpstreamPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_RsCmtsUpstreamPowerThreshold_Type.__name__ = "Integer32"
_RsCmtsUpstreamPowerThreshold_Object = MibTableColumn
rsCmtsUpstreamPowerThreshold = _RsCmtsUpstreamPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 6),
    _RsCmtsUpstreamPowerThreshold_Type()
)
rsCmtsUpstreamPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rsCmtsUpstreamPowerThreshold.setUnits("Quarter DBmv")


class _RsCmtsUpstreamPowerAdjust_Type(TruthValue):
    """Custom type rsCmtsUpstreamPowerAdjust based on TruthValue"""


_RsCmtsUpstreamPowerAdjust_Object = MibTableColumn
rsCmtsUpstreamPowerAdjust = _RsCmtsUpstreamPowerAdjust_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 7),
    _RsCmtsUpstreamPowerAdjust_Type()
)
rsCmtsUpstreamPowerAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamPowerAdjust.setStatus("current")


class _RsCmtsUpstreamTimingAdjust_Type(TruthValue):
    """Custom type rsCmtsUpstreamTimingAdjust based on TruthValue"""


_RsCmtsUpstreamTimingAdjust_Object = MibTableColumn
rsCmtsUpstreamTimingAdjust = _RsCmtsUpstreamTimingAdjust_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 8),
    _RsCmtsUpstreamTimingAdjust_Type()
)
rsCmtsUpstreamTimingAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamTimingAdjust.setStatus("current")


class _RsCmtsUpstreamFreqencyAdjust_Type(TruthValue):
    """Custom type rsCmtsUpstreamFreqencyAdjust based on TruthValue"""


_RsCmtsUpstreamFreqencyAdjust_Object = MibTableColumn
rsCmtsUpstreamFreqencyAdjust = _RsCmtsUpstreamFreqencyAdjust_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 9),
    _RsCmtsUpstreamFreqencyAdjust_Type()
)
rsCmtsUpstreamFreqencyAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamFreqencyAdjust.setStatus("current")


class _RsCmtsUpstreamTXCoefficients_Type(TruthValue):
    """Custom type rsCmtsUpstreamTXCoefficients based on TruthValue"""


_RsCmtsUpstreamTXCoefficients_Object = MibTableColumn
rsCmtsUpstreamTXCoefficients = _RsCmtsUpstreamTXCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 10),
    _RsCmtsUpstreamTXCoefficients_Type()
)
rsCmtsUpstreamTXCoefficients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamTXCoefficients.setStatus("current")


class _RsCmtsUpstreamForceContinue_Type(TruthValue):
    """Custom type rsCmtsUpstreamForceContinue based on TruthValue"""


_RsCmtsUpstreamForceContinue_Object = MibTableColumn
rsCmtsUpstreamForceContinue = _RsCmtsUpstreamForceContinue_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 11),
    _RsCmtsUpstreamForceContinue_Type()
)
rsCmtsUpstreamForceContinue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamForceContinue.setStatus("current")


class _RsCmtsUpstreamQosConfirm_Type(TruthValue):
    """Custom type rsCmtsUpstreamQosConfirm based on TruthValue"""


_RsCmtsUpstreamQosConfirm_Object = MibTableColumn
rsCmtsUpstreamQosConfirm = _RsCmtsUpstreamQosConfirm_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 12),
    _RsCmtsUpstreamQosConfirm_Type()
)
rsCmtsUpstreamQosConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamQosConfirm.setStatus("current")
_RsCmtsUpstreamQosMaxBps_Type = Integer32
_RsCmtsUpstreamQosMaxBps_Object = MibTableColumn
rsCmtsUpstreamQosMaxBps = _RsCmtsUpstreamQosMaxBps_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 2, 1, 13),
    _RsCmtsUpstreamQosMaxBps_Type()
)
rsCmtsUpstreamQosMaxBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsUpstreamQosMaxBps.setStatus("current")
_RsCmtsModulationTable_Object = MibTable
rsCmtsModulationTable = _RsCmtsModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3)
)
if mibBuilder.loadTexts:
    rsCmtsModulationTable.setStatus("current")
_RsCmtsModulationEntry_Object = MibTableRow
rsCmtsModulationEntry = _RsCmtsModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3, 1)
)
rsCmtsModulationEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsModIndex"),
    (0, "DOCS-IF-MIB", "docsIfCmtsModIntervalUsageCode"),
)
if mibBuilder.loadTexts:
    rsCmtsModulationEntry.setStatus("current")


class _RsCmtsModulationUWLength_Type(Integer32):
    """Custom type rsCmtsModulationUWLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RsCmtsModulationUWLength_Type.__name__ = "Integer32"
_RsCmtsModulationUWLength_Object = MibTableColumn
rsCmtsModulationUWLength = _RsCmtsModulationUWLength_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3, 1, 1),
    _RsCmtsModulationUWLength_Type()
)
rsCmtsModulationUWLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCmtsModulationUWLength.setStatus("current")


class _RsCmtsModulationDetectWindow_Type(Integer32):
    """Custom type rsCmtsModulationDetectWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsCmtsModulationDetectWindow_Type.__name__ = "Integer32"
_RsCmtsModulationDetectWindow_Object = MibTableColumn
rsCmtsModulationDetectWindow = _RsCmtsModulationDetectWindow_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3, 1, 2),
    _RsCmtsModulationDetectWindow_Type()
)
rsCmtsModulationDetectWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsModulationDetectWindow.setStatus("current")


class _RsCmtsModulationUWMismatch_Type(Integer32):
    """Custom type rsCmtsModulationUWMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RsCmtsModulationUWMismatch_Type.__name__ = "Integer32"
_RsCmtsModulationUWMismatch_Object = MibTableColumn
rsCmtsModulationUWMismatch = _RsCmtsModulationUWMismatch_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3, 1, 3),
    _RsCmtsModulationUWMismatch_Type()
)
rsCmtsModulationUWMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsModulationUWMismatch.setStatus("current")


class _RsCmtsModulationEQSymbols_Type(Integer32):
    """Custom type rsCmtsModulationEQSymbols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RsCmtsModulationEQSymbols_Type.__name__ = "Integer32"
_RsCmtsModulationEQSymbols_Object = MibTableColumn
rsCmtsModulationEQSymbols = _RsCmtsModulationEQSymbols_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 3, 1, 4),
    _RsCmtsModulationEQSymbols_Type()
)
rsCmtsModulationEQSymbols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsModulationEQSymbols.setStatus("current")
_RsCmtsDownstreamTable_Object = MibTable
rsCmtsDownstreamTable = _RsCmtsDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 4)
)
if mibBuilder.loadTexts:
    rsCmtsDownstreamTable.setStatus("current")
_RsCmtsDownstreamEntry_Object = MibTableRow
rsCmtsDownstreamEntry = _RsCmtsDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 4, 1)
)
rsCmtsDownstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsCmtsDownstreamEntry.setStatus("current")


class _RsCmtsDownstreamState_Type(TruthValue):
    """Custom type rsCmtsDownstreamState based on TruthValue"""


_RsCmtsDownstreamState_Object = MibTableColumn
rsCmtsDownstreamState = _RsCmtsDownstreamState_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 4, 1, 1),
    _RsCmtsDownstreamState_Type()
)
rsCmtsDownstreamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsDownstreamState.setStatus("current")


class _RsCmtsDownstreamModulation_Type(TruthValue):
    """Custom type rsCmtsDownstreamModulation based on TruthValue"""


_RsCmtsDownstreamModulation_Object = MibTableColumn
rsCmtsDownstreamModulation = _RsCmtsDownstreamModulation_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 4, 1, 2),
    _RsCmtsDownstreamModulation_Type()
)
rsCmtsDownstreamModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCmtsDownstreamModulation.setStatus("current")
_RsCmtsConformance_ObjectIdentity = ObjectIdentity
rsCmtsConformance = _RsCmtsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 6)
)
_RsCmtsGroups_ObjectIdentity = ObjectIdentity
rsCmtsGroups = _RsCmtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 6, 1)
)
_RsCmtsCompliances_ObjectIdentity = ObjectIdentity
rsCmtsCompliances = _RsCmtsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 6, 2)
)

# Managed Objects groups

rsCmtsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 6, 1, 1)
)
rsCmtsBaseGroup.setObjects(
      *(("RIVERSTONE-CMTS-MIB", "rsCmtsBaseBpduFilter"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseBpduFilterHits"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseNonIPFilter"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseNonIPFilterHits"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseMapLength"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseMapLeadTime"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseInitMaintLength"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBase3137Config1"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBase3137Config2"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseConcatenation"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseBpiHwAssist"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseGenericCmd"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseGenericCmdStatus"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseUccRetryInterval"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsBaseUccRetries"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamNominalRxPower"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamState"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamPolicing"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamRangeInterval"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamRangeRetryInterval"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamPowerThreshold"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamPowerAdjust"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamTimingAdjust"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamFreqencyAdjust"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamTXCoefficients"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamForceContinue"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamQosConfirm"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsUpstreamQosMaxBps"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsModulationUWLength"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsModulationDetectWindow"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsModulationUWMismatch"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsModulationEQSymbols"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsDownstreamState"),
        ("RIVERSTONE-CMTS-MIB", "rsCmtsDownstreamModulation"))
)
if mibBuilder.loadTexts:
    rsCmtsBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsCmtsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 11, 6, 2, 1)
)
if mibBuilder.loadTexts:
    rsCmtsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-CMTS-MIB",
    **{"RsCmtsCmdStatus": RsCmtsCmdStatus,
       "rsCmtsMib": rsCmtsMib,
       "rsCmtsBaseTable": rsCmtsBaseTable,
       "rsCmtsBaseEntry": rsCmtsBaseEntry,
       "rsCmtsBaseBpduFilter": rsCmtsBaseBpduFilter,
       "rsCmtsBaseBpduFilterHits": rsCmtsBaseBpduFilterHits,
       "rsCmtsBaseNonIPFilter": rsCmtsBaseNonIPFilter,
       "rsCmtsBaseNonIPFilterHits": rsCmtsBaseNonIPFilterHits,
       "rsCmtsBaseMapLength": rsCmtsBaseMapLength,
       "rsCmtsBaseMapLeadTime": rsCmtsBaseMapLeadTime,
       "rsCmtsBaseInitMaintLength": rsCmtsBaseInitMaintLength,
       "rsCmtsBase3137Config1": rsCmtsBase3137Config1,
       "rsCmtsBase3137Config2": rsCmtsBase3137Config2,
       "rsCmtsBaseConcatenation": rsCmtsBaseConcatenation,
       "rsCmtsBaseBpiHwAssist": rsCmtsBaseBpiHwAssist,
       "rsCmtsBaseGenericCmd": rsCmtsBaseGenericCmd,
       "rsCmtsBaseGenericCmdStatus": rsCmtsBaseGenericCmdStatus,
       "rsCmtsBaseUccRetryInterval": rsCmtsBaseUccRetryInterval,
       "rsCmtsBaseUccRetries": rsCmtsBaseUccRetries,
       "rsCmtsUpstreamTable": rsCmtsUpstreamTable,
       "rsCmtsUpstreamEntry": rsCmtsUpstreamEntry,
       "rsCmtsUpstreamNominalRxPower": rsCmtsUpstreamNominalRxPower,
       "rsCmtsUpstreamState": rsCmtsUpstreamState,
       "rsCmtsUpstreamPolicing": rsCmtsUpstreamPolicing,
       "rsCmtsUpstreamRangeInterval": rsCmtsUpstreamRangeInterval,
       "rsCmtsUpstreamRangeRetryInterval": rsCmtsUpstreamRangeRetryInterval,
       "rsCmtsUpstreamPowerThreshold": rsCmtsUpstreamPowerThreshold,
       "rsCmtsUpstreamPowerAdjust": rsCmtsUpstreamPowerAdjust,
       "rsCmtsUpstreamTimingAdjust": rsCmtsUpstreamTimingAdjust,
       "rsCmtsUpstreamFreqencyAdjust": rsCmtsUpstreamFreqencyAdjust,
       "rsCmtsUpstreamTXCoefficients": rsCmtsUpstreamTXCoefficients,
       "rsCmtsUpstreamForceContinue": rsCmtsUpstreamForceContinue,
       "rsCmtsUpstreamQosConfirm": rsCmtsUpstreamQosConfirm,
       "rsCmtsUpstreamQosMaxBps": rsCmtsUpstreamQosMaxBps,
       "rsCmtsModulationTable": rsCmtsModulationTable,
       "rsCmtsModulationEntry": rsCmtsModulationEntry,
       "rsCmtsModulationUWLength": rsCmtsModulationUWLength,
       "rsCmtsModulationDetectWindow": rsCmtsModulationDetectWindow,
       "rsCmtsModulationUWMismatch": rsCmtsModulationUWMismatch,
       "rsCmtsModulationEQSymbols": rsCmtsModulationEQSymbols,
       "rsCmtsDownstreamTable": rsCmtsDownstreamTable,
       "rsCmtsDownstreamEntry": rsCmtsDownstreamEntry,
       "rsCmtsDownstreamState": rsCmtsDownstreamState,
       "rsCmtsDownstreamModulation": rsCmtsDownstreamModulation,
       "rsCmtsConformance": rsCmtsConformance,
       "rsCmtsGroups": rsCmtsGroups,
       "rsCmtsBaseGroup": rsCmtsBaseGroup,
       "rsCmtsCompliances": rsCmtsCompliances,
       "rsCmtsMibCompliance": rsCmtsMibCompliance}
)
