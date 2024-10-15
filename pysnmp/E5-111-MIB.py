# SNMP MIB module (E5-111-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E5-111-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:07 2024
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

(BridgeId,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1dTrafficClass,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "dot1dTrafficClass")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixNetworks_ObjectIdentity = ObjectIdentity
calixNetworks = _CalixNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321)
)
_CalixRegistrations_ObjectIdentity = ObjectIdentity
calixRegistrations = _CalixRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1)
)
_CalixProducts_ObjectIdentity = ObjectIdentity
calixProducts = _CalixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2)
)
_E5x100_ObjectIdentity = ObjectIdentity
e5x100 = _E5x100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3)
)
_E5x111_ObjectIdentity = ObjectIdentity
e5x111 = _E5x111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2)
)
_Alarmconf_ObjectIdentity = ObjectIdentity
alarmconf = _Alarmconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2)
)
_AlarmOps_Type = Integer32
_AlarmOps_Object = MibScalar
alarmOps = _AlarmOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 1),
    _AlarmOps_Type()
)
alarmOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOps.setStatus("current")
_AlarmConfTable_Object = MibTable
alarmConfTable = _AlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    alarmConfTable.setStatus("current")
_AlarmConfEntry_Object = MibTableRow
alarmConfEntry = _AlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1)
)
alarmConfEntry.setIndexNames(
    (0, "E5-111-MIB", "alarmConfId"),
)
if mibBuilder.loadTexts:
    alarmConfEntry.setStatus("current")
_AlarmConfId_Type = Integer32
_AlarmConfId_Object = MibTableColumn
alarmConfId = _AlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1, 1),
    _AlarmConfId_Type()
)
alarmConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConfId.setStatus("current")


class _AlarmConfFacility_Type(Integer32):
    """Custom type alarmConfFacility based on Integer32"""
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
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_AlarmConfFacility_Type.__name__ = "Integer32"
_AlarmConfFacility_Object = MibTableColumn
alarmConfFacility = _AlarmConfFacility_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1, 2),
    _AlarmConfFacility_Type()
)
alarmConfFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfFacility.setStatus("current")
_AlarmConfTarget_Type = Integer32
_AlarmConfTarget_Object = MibTableColumn
alarmConfTarget = _AlarmConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1, 3),
    _AlarmConfTarget_Type()
)
alarmConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfTarget.setStatus("current")


class _AlarmConfSeverity_Type(Integer32):
    """Custom type alarmConfSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3))
    )


_AlarmConfSeverity_Type.__name__ = "Integer32"
_AlarmConfSeverity_Object = MibTableColumn
alarmConfSeverity = _AlarmConfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1, 4),
    _AlarmConfSeverity_Type()
)
alarmConfSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfSeverity.setStatus("current")


class _AlarmConfClearable_Type(Integer32):
    """Custom type alarmConfClearable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearable", 1),
          ("unclearable", 2))
    )


_AlarmConfClearable_Type.__name__ = "Integer32"
_AlarmConfClearable_Object = MibTableColumn
alarmConfClearable = _AlarmConfClearable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 2, 1, 5),
    _AlarmConfClearable_Type()
)
alarmConfClearable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmConfClearable.setStatus("current")
_AlarmCurrTable_Object = MibTable
alarmCurrTable = _AlarmCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    alarmCurrTable.setStatus("current")
_AlarmCurrEntry_Object = MibTableRow
alarmCurrEntry = _AlarmCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1)
)
alarmCurrEntry.setIndexNames(
    (0, "E5-111-MIB", "alarmCurrIndex"),
)
if mibBuilder.loadTexts:
    alarmCurrEntry.setStatus("current")
_AlarmCurrIndex_Type = Integer32
_AlarmCurrIndex_Object = MibTableColumn
alarmCurrIndex = _AlarmCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 1),
    _AlarmCurrIndex_Type()
)
alarmCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrIndex.setStatus("current")
_AlarmCurrOccurTime_Type = TimeTicks
_AlarmCurrOccurTime_Object = MibTableColumn
alarmCurrOccurTime = _AlarmCurrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 2),
    _AlarmCurrOccurTime_Type()
)
alarmCurrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrOccurTime.setStatus("current")
_AlarmCurrTrapOid_Type = ObjectIdentifier
_AlarmCurrTrapOid_Object = MibTableColumn
alarmCurrTrapOid = _AlarmCurrTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 3),
    _AlarmCurrTrapOid_Type()
)
alarmCurrTrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTrapOid.setStatus("current")
_AlarmCurrParam1_Type = Integer32
_AlarmCurrParam1_Object = MibTableColumn
alarmCurrParam1 = _AlarmCurrParam1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 4),
    _AlarmCurrParam1_Type()
)
alarmCurrParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam1.setStatus("current")
_AlarmCurrParam2_Type = Integer32
_AlarmCurrParam2_Object = MibTableColumn
alarmCurrParam2 = _AlarmCurrParam2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 5),
    _AlarmCurrParam2_Type()
)
alarmCurrParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam2.setStatus("current")
_AlarmCurrParam3_Type = Integer32
_AlarmCurrParam3_Object = MibTableColumn
alarmCurrParam3 = _AlarmCurrParam3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 6),
    _AlarmCurrParam3_Type()
)
alarmCurrParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam3.setStatus("current")
_AlarmCurrParam4_Type = Integer32
_AlarmCurrParam4_Object = MibTableColumn
alarmCurrParam4 = _AlarmCurrParam4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 7),
    _AlarmCurrParam4_Type()
)
alarmCurrParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam4.setStatus("current")
_AlarmCurrParam5_Type = Integer32
_AlarmCurrParam5_Object = MibTableColumn
alarmCurrParam5 = _AlarmCurrParam5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 8),
    _AlarmCurrParam5_Type()
)
alarmCurrParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam5.setStatus("current")
_AlarmCurrParam6_Type = Integer32
_AlarmCurrParam6_Object = MibTableColumn
alarmCurrParam6 = _AlarmCurrParam6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 9),
    _AlarmCurrParam6_Type()
)
alarmCurrParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam6.setStatus("current")
_AlarmCurrParam7_Type = Integer32
_AlarmCurrParam7_Object = MibTableColumn
alarmCurrParam7 = _AlarmCurrParam7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 10),
    _AlarmCurrParam7_Type()
)
alarmCurrParam7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam7.setStatus("current")
_AlarmCurrParam8_Type = Integer32
_AlarmCurrParam8_Object = MibTableColumn
alarmCurrParam8 = _AlarmCurrParam8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 11),
    _AlarmCurrParam8_Type()
)
alarmCurrParam8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrParam8.setStatus("current")
_AlarmCurrTimeDescr_Type = DisplayString
_AlarmCurrTimeDescr_Object = MibTableColumn
alarmCurrTimeDescr = _AlarmCurrTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 12),
    _AlarmCurrTimeDescr_Type()
)
alarmCurrTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrTimeDescr.setStatus("current")


class _AlarmCurrSeverity_Type(Integer32):
    """Custom type alarmCurrSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3))
    )


_AlarmCurrSeverity_Type.__name__ = "Integer32"
_AlarmCurrSeverity_Object = MibTableColumn
alarmCurrSeverity = _AlarmCurrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 13),
    _AlarmCurrSeverity_Type()
)
alarmCurrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrSeverity.setStatus("current")
_AlarmCurrDescr_Type = DisplayString
_AlarmCurrDescr_Object = MibTableColumn
alarmCurrDescr = _AlarmCurrDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 3, 1, 14),
    _AlarmCurrDescr_Type()
)
alarmCurrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrDescr.setStatus("current")
_AlarmSeverityPortTable_Object = MibTable
alarmSeverityPortTable = _AlarmSeverityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    alarmSeverityPortTable.setStatus("current")
_AlarmSeverityPortEntry_Object = MibTableRow
alarmSeverityPortEntry = _AlarmSeverityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 4, 1)
)
alarmSeverityPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alarmSeverityPortEntry.setStatus("current")


class _SeverityThresh_Type(Integer32):
    """Custom type severityThresh based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3))
    )


_SeverityThresh_Type.__name__ = "Integer32"
_SeverityThresh_Object = MibTableColumn
severityThresh = _SeverityThresh_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 2, 4, 1, 1),
    _SeverityThresh_Type()
)
severityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityThresh.setStatus("current")
_Diagnostic_ObjectIdentity = ObjectIdentity
diagnostic = _Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4)
)
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("awg24", 1),
          ("awg26", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 3, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")
_Mlt_ObjectIdentity = ObjectIdentity
mlt = _Mlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4)
)
_MltTarget_Type = Integer32
_MltTarget_Object = MibScalar
mltTarget = _MltTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 1),
    _MltTarget_Type()
)
mltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTarget.setStatus("current")
_MltOps_Type = Integer32
_MltOps_Object = MibScalar
mltOps = _MltOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 2),
    _MltOps_Type()
)
mltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOps.setStatus("current")


class _MltOption_Type(Integer32):
    """Custom type mltOption based on Integer32"""
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
        *(("all", 1),
          ("cap", 6),
          ("metering", 9),
          ("ren", 7),
          ("ring", 8),
          ("riso", 5),
          ("rload", 4),
          ("vac", 2),
          ("vdc", 3))
    )


_MltOption_Type.__name__ = "Integer32"
_MltOption_Object = MibScalar
mltOption = _MltOption_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 3),
    _MltOption_Type()
)
mltOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltOption.setStatus("current")


class _MltForce_Type(Integer32):
    """Custom type mltForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("notForce", 2))
    )


_MltForce_Type.__name__ = "Integer32"
_MltForce_Object = MibScalar
mltForce = _MltForce_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 4),
    _MltForce_Type()
)
mltForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltForce.setStatus("current")
_MltResult_ObjectIdentity = ObjectIdentity
mltResult = _MltResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5)
)
_MltVacTip_Type = Integer32
_MltVacTip_Object = MibScalar
mltVacTip = _MltVacTip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 1),
    _MltVacTip_Type()
)
mltVacTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVacTip.setUnits("0.1 rms")
_MltVacRing_Type = Integer32
_MltVacRing_Object = MibScalar
mltVacRing = _MltVacRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 2),
    _MltVacRing_Type()
)
mltVacRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVacRing.setUnits("0.1 rms")
_MltVacDiff_Type = Integer32
_MltVacDiff_Object = MibScalar
mltVacDiff = _MltVacDiff_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 3),
    _MltVacDiff_Type()
)
mltVacDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVacDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVacDiff.setUnits("0.1 rms")
_MltVdcTip_Type = Integer32
_MltVdcTip_Object = MibScalar
mltVdcTip = _MltVdcTip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 4),
    _MltVdcTip_Type()
)
mltVdcTip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcTip.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcTip.setUnits("0.1 volt")
_MltVdcRing_Type = Integer32
_MltVdcRing_Object = MibScalar
mltVdcRing = _MltVdcRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 5),
    _MltVdcRing_Type()
)
mltVdcRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcRing.setUnits("0.1 volt")
_MltVdcDiff_Type = Integer32
_MltVdcDiff_Object = MibScalar
mltVdcDiff = _MltVdcDiff_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 6),
    _MltVdcDiff_Type()
)
mltVdcDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVdcDiff.setStatus("current")
if mibBuilder.loadTexts:
    mltVdcDiff.setUnits("0.1 volt")
_MltRLoop_Type = Integer32
_MltRLoop_Object = MibScalar
mltRLoop = _MltRLoop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 7),
    _MltRLoop_Type()
)
mltRLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRLoop.setStatus("current")
if mibBuilder.loadTexts:
    mltRLoop.setUnits("0.1 ohm")
_MltRtg_Type = Integer32
_MltRtg_Object = MibScalar
mltRtg = _MltRtg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 8),
    _MltRtg_Type()
)
mltRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtg.setStatus("current")
if mibBuilder.loadTexts:
    mltRtg.setUnits("0.1 ohm")
_MltRrg_Type = Integer32
_MltRrg_Object = MibScalar
mltRrg = _MltRrg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 9),
    _MltRrg_Type()
)
mltRrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRrg.setStatus("current")
if mibBuilder.loadTexts:
    mltRrg.setUnits("0.1 ohm")
_MltRtr_Type = Integer32
_MltRtr_Object = MibScalar
mltRtr = _MltRtr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 10),
    _MltRtr_Type()
)
mltRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRtr.setStatus("current")
if mibBuilder.loadTexts:
    mltRtr.setUnits("0.1 ohm")
_MltCtg_Type = Integer32
_MltCtg_Object = MibScalar
mltCtg = _MltCtg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 11),
    _MltCtg_Type()
)
mltCtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtg.setStatus("current")
if mibBuilder.loadTexts:
    mltCtg.setUnits("10^-9 F")
_MltCrg_Type = Integer32
_MltCrg_Object = MibScalar
mltCrg = _MltCrg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 12),
    _MltCrg_Type()
)
mltCrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCrg.setStatus("current")
if mibBuilder.loadTexts:
    mltCrg.setUnits("10^-9 F")
_MltCtr_Type = Integer32
_MltCtr_Object = MibScalar
mltCtr = _MltCtr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 13),
    _MltCtr_Type()
)
mltCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCtr.setStatus("current")
if mibBuilder.loadTexts:
    mltCtr.setUnits("10^-9 F")
_MltRen_Type = Integer32
_MltRen_Object = MibScalar
mltRen = _MltRen_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 14),
    _MltRen_Type()
)
mltRen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltRen.setStatus("current")
if mibBuilder.loadTexts:
    mltRen.setUnits("0.1 ren")
_MltVRing_Type = Integer32
_MltVRing_Object = MibScalar
mltVRing = _MltVRing_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 15),
    _MltVRing_Type()
)
mltVRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVRing.setStatus("current")
if mibBuilder.loadTexts:
    mltVRing.setUnits("0.1 rms")
_MltVMetering_Type = Integer32
_MltVMetering_Object = MibScalar
mltVMetering = _MltVMetering_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 16),
    _MltVMetering_Type()
)
mltVMetering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltVMetering.setStatus("current")
if mibBuilder.loadTexts:
    mltVMetering.setUnits("0.1 vpeak")


class _MltDialToneDetected_Type(Integer32):
    """Custom type mltDialToneDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MltDialToneDetected_Type.__name__ = "Integer32"
_MltDialToneDetected_Object = MibScalar
mltDialToneDetected = _MltDialToneDetected_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 17),
    _MltDialToneDetected_Type()
)
mltDialToneDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDetected.setStatus("current")
_MltDetectedDtmfCount_Type = Integer32
_MltDetectedDtmfCount_Object = MibScalar
mltDetectedDtmfCount = _MltDetectedDtmfCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 18),
    _MltDetectedDtmfCount_Type()
)
mltDetectedDtmfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDetectedDtmfCount.setStatus("current")
_MltDialToneDelay_Type = Integer32
_MltDialToneDelay_Object = MibScalar
mltDialToneDelay = _MltDialToneDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 5, 19),
    _MltDialToneDelay_Type()
)
mltDialToneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDialToneDelay.setStatus("current")
if mibBuilder.loadTexts:
    mltDialToneDelay.setUnits("0.001 sec")
_MltRelayTable_Object = MibTable
mltRelayTable = _MltRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    mltRelayTable.setStatus("current")
_MltRelayEntry_Object = MibTableRow
mltRelayEntry = _MltRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 6, 1)
)
mltRelayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mltRelayEntry.setStatus("current")


class _MltRelaySet_Type(Integer32):
    """Custom type mltRelaySet based on Integer32"""
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
        *(("both", 3),
          ("in", 1),
          ("off", 4),
          ("out", 2))
    )


_MltRelaySet_Type.__name__ = "Integer32"
_MltRelaySet_Object = MibTableColumn
mltRelaySet = _MltRelaySet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 4, 4, 6, 1, 1),
    _MltRelaySet_Type()
)
mltRelaySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltRelaySet.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7)
)


class _IgmpEnable_Type(Integer32):
    """Custom type igmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableProxy", 1),
          ("enableSnooping", 2))
    )


_IgmpEnable_Type.__name__ = "Integer32"
_IgmpEnable_Object = MibScalar
igmpEnable = _IgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_McastBandwidth_ObjectIdentity = ObjectIdentity
mcastBandwidth = _McastBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4)
)


class _McastDefaultBandwidth_Type(Integer32):
    """Custom type mcastDefaultBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_McastDefaultBandwidth_Type.__name__ = "Integer32"
_McastDefaultBandwidth_Object = MibScalar
mcastDefaultBandwidth = _McastDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 1),
    _McastDefaultBandwidth_Type()
)
mcastDefaultBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastDefaultBandwidth.setUnits("Kbps")
_MaxNumOfMcastBw_Type = Integer32
_MaxNumOfMcastBw_Object = MibScalar
maxNumOfMcastBw = _MaxNumOfMcastBw_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 2),
    _MaxNumOfMcastBw_Type()
)
maxNumOfMcastBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMcastBw.setStatus("current")
_McastBwTable_Object = MibTable
mcastBwTable = _McastBwTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3)
)
if mibBuilder.loadTexts:
    mcastBwTable.setStatus("current")
_McastBwEntry_Object = MibTableRow
mcastBwEntry = _McastBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1)
)
mcastBwEntry.setIndexNames(
    (0, "E5-111-MIB", "mcastBwIndex"),
    (0, "E5-111-MIB", "mcastBwStartIp"),
    (0, "E5-111-MIB", "mcastBwEndIp"),
)
if mibBuilder.loadTexts:
    mcastBwEntry.setStatus("current")
_McastBwIndex_Type = Integer32
_McastBwIndex_Object = MibTableColumn
mcastBwIndex = _McastBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1, 1),
    _McastBwIndex_Type()
)
mcastBwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwIndex.setStatus("current")
_McastBwStartIp_Type = IpAddress
_McastBwStartIp_Object = MibTableColumn
mcastBwStartIp = _McastBwStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1, 2),
    _McastBwStartIp_Type()
)
mcastBwStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwStartIp.setStatus("current")
_McastBwEndIp_Type = IpAddress
_McastBwEndIp_Object = MibTableColumn
mcastBwEndIp = _McastBwEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1, 3),
    _McastBwEndIp_Type()
)
mcastBwEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastBwEndIp.setStatus("current")
_McastBwBandwidth_Type = Integer32
_McastBwBandwidth_Object = MibTableColumn
mcastBwBandwidth = _McastBwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1, 4),
    _McastBwBandwidth_Type()
)
mcastBwBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwBandwidth.setUnits("Kbps")
_McastBwRowStatus_Type = RowStatus
_McastBwRowStatus_Object = MibTableColumn
mcastBwRowStatus = _McastBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 3, 1, 5),
    _McastBwRowStatus_Type()
)
mcastBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastBwRowStatus.setStatus("current")
_McastBwPortTable_Object = MibTable
mcastBwPortTable = _McastBwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mcastBwPortTable.setStatus("current")
_McastBwPortEntry_Object = MibTableRow
mcastBwPortEntry = _McastBwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 4, 1)
)
mcastBwPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mcastBwPortEntry.setStatus("current")


class _McastBwPortEnable_Type(Integer32):
    """Custom type mcastBwPortEnable based on Integer32"""
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


_McastBwPortEnable_Type.__name__ = "Integer32"
_McastBwPortEnable_Object = MibTableColumn
mcastBwPortEnable = _McastBwPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 4, 1, 1),
    _McastBwPortEnable_Type()
)
mcastBwPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortEnable.setStatus("current")
_McastBwPortBandwidth_Type = Integer32
_McastBwPortBandwidth_Object = MibTableColumn
mcastBwPortBandwidth = _McastBwPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 4, 4, 1, 2),
    _McastBwPortBandwidth_Type()
)
mcastBwPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mcastBwPortBandwidth.setUnits("Kbps")
_IgmpCount_ObjectIdentity = ObjectIdentity
igmpCount = _IgmpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 5)
)
_IgmpCountPortTable_Object = MibTable
igmpCountPortTable = _IgmpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    igmpCountPortTable.setStatus("current")
_IgmpCountPortEntry_Object = MibTableRow
igmpCountPortEntry = _IgmpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 5, 1, 1)
)
igmpCountPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpCountPortEntry.setStatus("current")


class _IgmpCountPortEnable_Type(Integer32):
    """Custom type igmpCountPortEnable based on Integer32"""
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


_IgmpCountPortEnable_Type.__name__ = "Integer32"
_IgmpCountPortEnable_Object = MibTableColumn
igmpCountPortEnable = _IgmpCountPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 5, 1, 1, 1),
    _IgmpCountPortEnable_Type()
)
igmpCountPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortEnable.setStatus("current")


class _IgmpCountPortLimit_Type(Integer32):
    """Custom type igmpCountPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IgmpCountPortLimit_Type.__name__ = "Integer32"
_IgmpCountPortLimit_Object = MibTableColumn
igmpCountPortLimit = _IgmpCountPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 5, 1, 1, 2),
    _IgmpCountPortLimit_Type()
)
igmpCountPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCountPortLimit.setStatus("current")
_Mvlan_ObjectIdentity = ObjectIdentity
mvlan = _Mvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6)
)
_MaxNumOfMvlan_Type = Integer32
_MaxNumOfMvlan_Object = MibScalar
maxNumOfMvlan = _MaxNumOfMvlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 1),
    _MaxNumOfMvlan_Type()
)
maxNumOfMvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMvlan.setStatus("current")
_MvlanTable_Object = MibTable
mvlanTable = _MvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2)
)
if mibBuilder.loadTexts:
    mvlanTable.setStatus("current")
_MvlanEntry_Object = MibTableRow
mvlanEntry = _MvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1)
)
mvlanEntry.setIndexNames(
    (0, "E5-111-MIB", "mvlanIndex"),
)
if mibBuilder.loadTexts:
    mvlanEntry.setStatus("current")
_MvlanIndex_Type = VlanIndex
_MvlanIndex_Object = MibTableColumn
mvlanIndex = _MvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1, 1),
    _MvlanIndex_Type()
)
mvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanIndex.setStatus("current")


class _MvlanName_Type(DisplayString):
    """Custom type mvlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MvlanName_Type.__name__ = "DisplayString"
_MvlanName_Object = MibTableColumn
mvlanName = _MvlanName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1, 2),
    _MvlanName_Type()
)
mvlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanName.setStatus("current")
_MvlanEgressPorts_Type = PortList
_MvlanEgressPorts_Object = MibTableColumn
mvlanEgressPorts = _MvlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1, 3),
    _MvlanEgressPorts_Type()
)
mvlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanEgressPorts.setStatus("current")
_MvlanUntaggedPorts_Type = PortList
_MvlanUntaggedPorts_Object = MibTableColumn
mvlanUntaggedPorts = _MvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1, 4),
    _MvlanUntaggedPorts_Type()
)
mvlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanUntaggedPorts.setStatus("current")
_MvlanRowStatus_Type = RowStatus
_MvlanRowStatus_Object = MibTableColumn
mvlanRowStatus = _MvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 2, 1, 5),
    _MvlanRowStatus_Type()
)
mvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowStatus.setStatus("current")
_MvlanTranslateTable_Object = MibTable
mvlanTranslateTable = _MvlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 3)
)
if mibBuilder.loadTexts:
    mvlanTranslateTable.setStatus("current")
_MvlanTranslateEntry_Object = MibTableRow
mvlanTranslateEntry = _MvlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 3, 1)
)
mvlanTranslateEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "E5-111-MIB", "mvlanTranslateIndex"),
)
if mibBuilder.loadTexts:
    mvlanTranslateEntry.setStatus("current")
_MvlanTranslateIndex_Type = Integer32
_MvlanTranslateIndex_Object = MibTableColumn
mvlanTranslateIndex = _MvlanTranslateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 3, 1, 1),
    _MvlanTranslateIndex_Type()
)
mvlanTranslateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvlanTranslateIndex.setStatus("current")
_MvlanTranslateStartIp_Type = IpAddress
_MvlanTranslateStartIp_Object = MibTableColumn
mvlanTranslateStartIp = _MvlanTranslateStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 3, 1, 2),
    _MvlanTranslateStartIp_Type()
)
mvlanTranslateStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateStartIp.setStatus("current")
_MvlanTranslateEndIp_Type = IpAddress
_MvlanTranslateEndIp_Object = MibTableColumn
mvlanTranslateEndIp = _MvlanTranslateEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 6, 3, 1, 3),
    _MvlanTranslateEndIp_Type()
)
mvlanTranslateEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvlanTranslateEndIp.setStatus("current")
_QueryVid_ObjectIdentity = ObjectIdentity
queryVid = _QueryVid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7)
)
_MaxNumOfQryVid_Type = Integer32
_MaxNumOfQryVid_Object = MibScalar
maxNumOfQryVid = _MaxNumOfQryVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 1),
    _MaxNumOfQryVid_Type()
)
maxNumOfQryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfQryVid.setStatus("current")
_QryVidConfTable_Object = MibTable
qryVidConfTable = _QryVidConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 2)
)
if mibBuilder.loadTexts:
    qryVidConfTable.setStatus("current")
_QryVidConfEntry_Object = MibTableRow
qryVidConfEntry = _QryVidConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 2, 1)
)
qryVidConfEntry.setIndexNames(
    (0, "E5-111-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidConfEntry.setStatus("current")
_QryVid_Type = Integer32
_QryVid_Object = MibTableColumn
qryVid = _QryVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 2, 1, 1),
    _QryVid_Type()
)
qryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVid.setStatus("current")
_QryVidRowStatus_Type = RowStatus
_QryVidRowStatus_Object = MibTableColumn
qryVidRowStatus = _QryVidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 2, 1, 2),
    _QryVidRowStatus_Type()
)
qryVidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qryVidRowStatus.setStatus("current")
_QryVidStatusTable_Object = MibTable
qryVidStatusTable = _QryVidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 3)
)
if mibBuilder.loadTexts:
    qryVidStatusTable.setStatus("current")
_QryVidStatusEntry_Object = MibTableRow
qryVidStatusEntry = _QryVidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 3, 1)
)
qryVidStatusEntry.setIndexNames(
    (0, "E5-111-MIB", "qryVid"),
)
if mibBuilder.loadTexts:
    qryVidStatusEntry.setStatus("current")


class _QryVidType_Type(Integer32):
    """Custom type qryVidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_QryVidType_Type.__name__ = "Integer32"
_QryVidType_Object = MibTableColumn
qryVidType = _QryVidType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 7, 3, 1, 1),
    _QryVidType_Type()
)
qryVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qryVidType.setStatus("current")


class _IgmpVersion_Type(Integer32):
    """Custom type igmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )


_IgmpVersion_Type.__name__ = "Integer32"
_IgmpVersion_Object = MibScalar
igmpVersion = _IgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 9),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")


class _IgmpLeaveMode_Type(Integer32):
    """Custom type igmpLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediateLeave", 1),
          ("lastMemberQuery", 2))
    )


_IgmpLeaveMode_Type.__name__ = "Integer32"
_IgmpLeaveMode_Object = MibScalar
igmpLeaveMode = _IgmpLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 10),
    _IgmpLeaveMode_Type()
)
igmpLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLeaveMode.setStatus("current")
_IgmpTimer_ObjectIdentity = ObjectIdentity
igmpTimer = _IgmpTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11)
)


class _IgmpQryInterval_Type(Integer32):
    """Custom type igmpQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_IgmpQryInterval_Type.__name__ = "Integer32"
_IgmpQryInterval_Object = MibScalar
igmpQryInterval = _IgmpQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11, 1),
    _IgmpQryInterval_Type()
)
igmpQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQryInterval.setStatus("current")


class _IgmpRobust_Type(Integer32):
    """Custom type igmpRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpRobust_Type.__name__ = "Integer32"
_IgmpRobust_Object = MibScalar
igmpRobust = _IgmpRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11, 2),
    _IgmpRobust_Type()
)
igmpRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpRobust.setStatus("current")


class _IgmpQryRespInterval_Type(Integer32):
    """Custom type igmpQryRespInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IgmpQryRespInterval_Type.__name__ = "Integer32"
_IgmpQryRespInterval_Object = MibScalar
igmpQryRespInterval = _IgmpQryRespInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11, 3),
    _IgmpQryRespInterval_Type()
)
igmpQryRespInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQryRespInterval.setStatus("current")


class _IgmpLastMemQryInterval_Type(Integer32):
    """Custom type igmpLastMemQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpLastMemQryInterval_Type.__name__ = "Integer32"
_IgmpLastMemQryInterval_Object = MibScalar
igmpLastMemQryInterval = _IgmpLastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11, 4),
    _IgmpLastMemQryInterval_Type()
)
igmpLastMemQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastMemQryInterval.setStatus("current")


class _IgmpLastMemQryRobust_Type(Integer32):
    """Custom type igmpLastMemQryRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IgmpLastMemQryRobust_Type.__name__ = "Integer32"
_IgmpLastMemQryRobust_Object = MibScalar
igmpLastMemQryRobust = _IgmpLastMemQryRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 11, 5),
    _IgmpLastMemQryRobust_Type()
)
igmpLastMemQryRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpLastMemQryRobust.setStatus("current")
_AuditQuery_ObjectIdentity = ObjectIdentity
auditQuery = _AuditQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 12)
)


class _AuditQryEnable_Type(Integer32):
    """Custom type auditQryEnable based on Integer32"""
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


_AuditQryEnable_Type.__name__ = "Integer32"
_AuditQryEnable_Object = MibScalar
auditQryEnable = _AuditQryEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 12, 1),
    _AuditQryEnable_Type()
)
auditQryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryEnable.setStatus("current")


class _AuditQryInterval_Type(Integer32):
    """Custom type auditQryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AuditQryInterval_Type.__name__ = "Integer32"
_AuditQryInterval_Object = MibScalar
auditQryInterval = _AuditQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 12, 2),
    _AuditQryInterval_Type()
)
auditQryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryInterval.setStatus("current")


class _AuditQryRobust_Type(Integer32):
    """Custom type auditQryRobust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AuditQryRobust_Type.__name__ = "Integer32"
_AuditQryRobust_Object = MibScalar
auditQryRobust = _AuditQryRobust_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 12, 3),
    _AuditQryRobust_Type()
)
auditQryRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditQryRobust.setStatus("current")
_IgmpProfile_ObjectIdentity = ObjectIdentity
igmpProfile = _IgmpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13)
)
_MaxNumberOfIgmpProfiles_Type = Integer32
_MaxNumberOfIgmpProfiles_Object = MibScalar
maxNumberOfIgmpProfiles = _MaxNumberOfIgmpProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 1),
    _MaxNumberOfIgmpProfiles_Type()
)
maxNumberOfIgmpProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfIgmpProfiles.setStatus("current")
_IgmpProfileTable_Object = MibTable
igmpProfileTable = _IgmpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2)
)
if mibBuilder.loadTexts:
    igmpProfileTable.setStatus("current")
_IgmpProfileEntry_Object = MibTableRow
igmpProfileEntry = _IgmpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2, 1)
)
igmpProfileEntry.setIndexNames(
    (1, "E5-111-MIB", "igmpProfileName"),
)
if mibBuilder.loadTexts:
    igmpProfileEntry.setStatus("current")


class _IgmpProfileName_Type(DisplayString):
    """Custom type igmpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpProfileName_Type.__name__ = "DisplayString"
_IgmpProfileName_Object = MibTableColumn
igmpProfileName = _IgmpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2, 1, 1),
    _IgmpProfileName_Type()
)
igmpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpProfileName.setStatus("current")


class _IgmpProfileEnable_Type(Integer32):
    """Custom type igmpProfileEnable based on Integer32"""
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


_IgmpProfileEnable_Type.__name__ = "Integer32"
_IgmpProfileEnable_Object = MibTableColumn
igmpProfileEnable = _IgmpProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2, 1, 2),
    _IgmpProfileEnable_Type()
)
igmpProfileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfileEnable.setStatus("current")


class _IgmpProfileMaxGroup_Type(Integer32):
    """Custom type igmpProfileMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IgmpProfileMaxGroup_Type.__name__ = "Integer32"
_IgmpProfileMaxGroup_Object = MibTableColumn
igmpProfileMaxGroup = _IgmpProfileMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2, 1, 3),
    _IgmpProfileMaxGroup_Type()
)
igmpProfileMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfileMaxGroup.setStatus("current")
_IgmpProfileRowStatus_Type = RowStatus
_IgmpProfileRowStatus_Object = MibTableColumn
igmpProfileRowStatus = _IgmpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 2, 1, 4),
    _IgmpProfileRowStatus_Type()
)
igmpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpProfileRowStatus.setStatus("current")
_IgmpFilterTable_Object = MibTable
igmpFilterTable = _IgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 3)
)
if mibBuilder.loadTexts:
    igmpFilterTable.setStatus("current")
_IgmpFilterEntry_Object = MibTableRow
igmpFilterEntry = _IgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 3, 1)
)
igmpFilterEntry.setIndexNames(
    (0, "E5-111-MIB", "igmpProfileName"),
    (0, "E5-111-MIB", "igmpFilterIndex"),
)
if mibBuilder.loadTexts:
    igmpFilterEntry.setStatus("current")
_IgmpFilterIndex_Type = Integer32
_IgmpFilterIndex_Object = MibTableColumn
igmpFilterIndex = _IgmpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 3, 1, 1),
    _IgmpFilterIndex_Type()
)
igmpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilterIndex.setStatus("current")
_IgmpFilterStartIp_Type = IpAddress
_IgmpFilterStartIp_Object = MibTableColumn
igmpFilterStartIp = _IgmpFilterStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 3, 1, 2),
    _IgmpFilterStartIp_Type()
)
igmpFilterStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterStartIp.setStatus("current")
_IgmpFilterEndIp_Type = IpAddress
_IgmpFilterEndIp_Object = MibTableColumn
igmpFilterEndIp = _IgmpFilterEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 3, 1, 3),
    _IgmpFilterEndIp_Type()
)
igmpFilterEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilterEndIp.setStatus("current")
_IgmpProfilePortTable_Object = MibTable
igmpProfilePortTable = _IgmpProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 4)
)
if mibBuilder.loadTexts:
    igmpProfilePortTable.setStatus("current")
_IgmpProfilePortEntry_Object = MibTableRow
igmpProfilePortEntry = _IgmpProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 4, 1)
)
igmpProfilePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpProfilePortEntry.setStatus("current")


class _IgmpProfilePortProfile_Type(OctetString):
    """Custom type igmpProfilePortProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IgmpProfilePortProfile_Type.__name__ = "OctetString"
_IgmpProfilePortProfile_Object = MibTableColumn
igmpProfilePortProfile = _IgmpProfilePortProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 7, 13, 4, 1, 1),
    _IgmpProfilePortProfile_Type()
)
igmpProfilePortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProfilePortProfile.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8)
)
_SubrPortTable_Object = MibTable
subrPortTable = _SubrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    subrPortTable.setStatus("current")
_SubrPortEntry_Object = MibTableRow
subrPortEntry = _SubrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 1, 1)
)
subrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subrPortEntry.setStatus("current")


class _SubrPortName_Type(DisplayString):
    """Custom type subrPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SubrPortName_Type.__name__ = "DisplayString"
_SubrPortName_Object = MibTableColumn
subrPortName = _SubrPortName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 1, 1, 1),
    _SubrPortName_Type()
)
subrPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortName.setStatus("current")


class _SubrPortTel_Type(DisplayString):
    """Custom type subrPortTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SubrPortTel_Type.__name__ = "DisplayString"
_SubrPortTel_Object = MibTableColumn
subrPortTel = _SubrPortTel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 1, 1, 2),
    _SubrPortTel_Type()
)
subrPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subrPortTel.setStatus("current")
_AdslPort_ObjectIdentity = ObjectIdentity
adslPort = _AdslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2)
)
_AdslLineConfTable_Object = MibTable
adslLineConfTable = _AdslLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    adslLineConfTable.setStatus("current")
_AdslLineConfEntry_Object = MibTableRow
adslLineConfEntry = _AdslLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1)
)
adslLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineConfEntry.setStatus("current")


class _AdslLineConfAdslMode_Type(Integer32):
    """Custom type adslLineConfAdslMode based on Integer32"""
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
        *(("adsl2", 6),
          ("adsl2Plus", 7),
          ("auto", 4),
          ("etsi", 5),
          ("gDotDmt", 2),
          ("gDotLite", 1),
          ("t1Dot413", 3))
    )


_AdslLineConfAdslMode_Type.__name__ = "Integer32"
_AdslLineConfAdslMode_Object = MibTableColumn
adslLineConfAdslMode = _AdslLineConfAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 1),
    _AdslLineConfAdslMode_Type()
)
adslLineConfAdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAdslMode.setStatus("current")


class _AdslLineConfAnnexL_Type(Integer32):
    """Custom type adslLineConfAnnexL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableNarrowMode", 1),
          ("enableWideMode", 2))
    )


_AdslLineConfAnnexL_Type.__name__ = "Integer32"
_AdslLineConfAnnexL_Object = MibTableColumn
adslLineConfAnnexL = _AdslLineConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 2),
    _AdslLineConfAnnexL_Type()
)
adslLineConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexL.setStatus("current")


class _AdslLineConfAnnexM_Type(Integer32):
    """Custom type adslLineConfAnnexM based on Integer32"""
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


_AdslLineConfAnnexM_Type.__name__ = "Integer32"
_AdslLineConfAnnexM_Object = MibTableColumn
adslLineConfAnnexM = _AdslLineConfAnnexM_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 3),
    _AdslLineConfAnnexM_Type()
)
adslLineConfAnnexM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexM.setStatus("current")


class _AdslLineConfAnnexI_Type(Integer32):
    """Custom type adslLineConfAnnexI based on Integer32"""
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


_AdslLineConfAnnexI_Type.__name__ = "Integer32"
_AdslLineConfAnnexI_Object = MibTableColumn
adslLineConfAnnexI = _AdslLineConfAnnexI_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 4),
    _AdslLineConfAnnexI_Type()
)
adslLineConfAnnexI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAnnexI.setStatus("current")
_AdslLineConfOptionMask_Type = Integer32
_AdslLineConfOptionMask_Object = MibTableColumn
adslLineConfOptionMask = _AdslLineConfOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 5),
    _AdslLineConfOptionMask_Type()
)
adslLineConfOptionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfOptionMask.setStatus("current")


class _AdslLineConfPowerMgmt_Type(Integer32):
    """Custom type adslLineConfPowerMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableL2", 2))
    )


_AdslLineConfPowerMgmt_Type.__name__ = "Integer32"
_AdslLineConfPowerMgmt_Object = MibTableColumn
adslLineConfPowerMgmt = _AdslLineConfPowerMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 6),
    _AdslLineConfPowerMgmt_Type()
)
adslLineConfPowerMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfPowerMgmt.setStatus("current")


class _AdslLineConfPowerMode_Type(Integer32):
    """Custom type adslLineConfPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fix", 1),
          ("priorityToPower", 2),
          ("priorityToRate", 3))
    )


_AdslLineConfPowerMode_Type.__name__ = "Integer32"
_AdslLineConfPowerMode_Object = MibTableColumn
adslLineConfPowerMode = _AdslLineConfPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 7),
    _AdslLineConfPowerMode_Type()
)
adslLineConfPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfPowerMode.setStatus("current")


class _AdslLineConfAturMaxTxPower_Type(Integer32):
    """Custom type adslLineConfAturMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_AdslLineConfAturMaxTxPower_Type.__name__ = "Integer32"
_AdslLineConfAturMaxTxPower_Object = MibTableColumn
adslLineConfAturMaxTxPower = _AdslLineConfAturMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 8),
    _AdslLineConfAturMaxTxPower_Type()
)
adslLineConfAturMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfAturMaxTxPower.setUnits("tenth dBm")


class _AdslLineConfAtucMaxTxPower_Type(Integer32):
    """Custom type adslLineConfAtucMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_AdslLineConfAtucMaxTxPower_Type.__name__ = "Integer32"
_AdslLineConfAtucMaxTxPower_Object = MibTableColumn
adslLineConfAtucMaxTxPower = _AdslLineConfAtucMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 9),
    _AdslLineConfAtucMaxTxPower_Type()
)
adslLineConfAtucMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfAtucMaxTxPower.setUnits("tenth dBm")


class _AdslLineConfMaxRxPower_Type(Integer32):
    """Custom type adslLineConfMaxRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_AdslLineConfMaxRxPower_Type.__name__ = "Integer32"
_AdslLineConfMaxRxPower_Object = MibTableColumn
adslLineConfMaxRxPower = _AdslLineConfMaxRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 10),
    _AdslLineConfMaxRxPower_Type()
)
adslLineConfMaxRxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMaxRxPower.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMaxRxPower.setUnits("tenth dBm")
_AdslLineConfAturCarrierMask_Type = OctetString
_AdslLineConfAturCarrierMask_Object = MibTableColumn
adslLineConfAturCarrierMask = _AdslLineConfAturCarrierMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 11),
    _AdslLineConfAturCarrierMask_Type()
)
adslLineConfAturCarrierMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturCarrierMask.setStatus("current")
_AdslLineConfAtucCarrierMask0_Type = OctetString
_AdslLineConfAtucCarrierMask0_Object = MibTableColumn
adslLineConfAtucCarrierMask0 = _AdslLineConfAtucCarrierMask0_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 12),
    _AdslLineConfAtucCarrierMask0_Type()
)
adslLineConfAtucCarrierMask0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucCarrierMask0.setStatus("current")
_AdslLineConfAtucCarrierMask1_Type = OctetString
_AdslLineConfAtucCarrierMask1_Object = MibTableColumn
adslLineConfAtucCarrierMask1 = _AdslLineConfAtucCarrierMask1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 13),
    _AdslLineConfAtucCarrierMask1_Type()
)
adslLineConfAtucCarrierMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucCarrierMask1.setStatus("current")


class _AdslLineConfAturInp_Type(Integer32):
    """Custom type adslLineConfAturInp based on Integer32"""
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
        *(("eight", 6),
          ("four", 5),
          ("one", 3),
          ("sixteen", 7),
          ("two", 4),
          ("zero", 1),
          ("zeroPointFive", 2))
    )


_AdslLineConfAturInp_Type.__name__ = "Integer32"
_AdslLineConfAturInp_Object = MibTableColumn
adslLineConfAturInp = _AdslLineConfAturInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 14),
    _AdslLineConfAturInp_Type()
)
adslLineConfAturInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAturInp.setStatus("current")


class _AdslLineConfAtucInp_Type(Integer32):
    """Custom type adslLineConfAtucInp based on Integer32"""
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
        *(("eight", 6),
          ("four", 5),
          ("one", 3),
          ("sixteen", 7),
          ("two", 4),
          ("zero", 1),
          ("zeroPointFive", 2))
    )


_AdslLineConfAtucInp_Type.__name__ = "Integer32"
_AdslLineConfAtucInp_Object = MibTableColumn
adslLineConfAtucInp = _AdslLineConfAtucInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 15),
    _AdslLineConfAtucInp_Type()
)
adslLineConfAtucInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfAtucInp.setStatus("current")
_AdslLineConfL0Time_Type = Integer32
_AdslLineConfL0Time_Object = MibTableColumn
adslLineConfL0Time = _AdslLineConfL0Time_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 16),
    _AdslLineConfL0Time_Type()
)
adslLineConfL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL0Time.setStatus("current")
_AdslLineConfL2Time_Type = Integer32
_AdslLineConfL2Time_Object = MibTableColumn
adslLineConfL2Time = _AdslLineConfL2Time_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 17),
    _AdslLineConfL2Time_Type()
)
adslLineConfL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2Time.setStatus("current")
_AdslLineConfL2ATPR_Type = Integer32
_AdslLineConfL2ATPR_Object = MibTableColumn
adslLineConfL2ATPR = _AdslLineConfL2ATPR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 18),
    _AdslLineConfL2ATPR_Type()
)
adslLineConfL2ATPR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2ATPR.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL2ATPR.setUnits("dB")
_AdslLineConfL2ATPRT_Type = Integer32
_AdslLineConfL2ATPRT_Object = MibTableColumn
adslLineConfL2ATPRT = _AdslLineConfL2ATPRT_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 19),
    _AdslLineConfL2ATPRT_Type()
)
adslLineConfL2ATPRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL2ATPRT.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL2ATPRT.setUnits("dB")
_AdslLineConfMaxL2Rate_Type = Integer32
_AdslLineConfMaxL2Rate_Object = MibTableColumn
adslLineConfMaxL2Rate = _AdslLineConfMaxL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 20),
    _AdslLineConfMaxL2Rate_Type()
)
adslLineConfMaxL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMaxL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMaxL2Rate.setUnits("kbps")
_AdslLineConfMinL2Rate_Type = Integer32
_AdslLineConfMinL2Rate_Object = MibTableColumn
adslLineConfMinL2Rate = _AdslLineConfMinL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 21),
    _AdslLineConfMinL2Rate_Type()
)
adslLineConfMinL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfMinL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfMinL2Rate.setUnits("kbps")
_AdslLineConfL0toL2Rate_Type = Integer32
_AdslLineConfL0toL2Rate_Object = MibTableColumn
adslLineConfL0toL2Rate = _AdslLineConfL0toL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 22),
    _AdslLineConfL0toL2Rate_Type()
)
adslLineConfL0toL2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfL0toL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    adslLineConfL0toL2Rate.setUnits("kbps")


class _AdslLineConfNitro_Type(Integer32):
    """Custom type adslLineConfNitro based on Integer32"""
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


_AdslLineConfNitro_Type.__name__ = "Integer32"
_AdslLineConfNitro_Object = MibTableColumn
adslLineConfNitro = _AdslLineConfNitro_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 23),
    _AdslLineConfNitro_Type()
)
adslLineConfNitro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfNitro.setStatus("current")


class _AdslLineConfUSPhyr_Type(Integer32):
    """Custom type adslLineConfUSPhyr based on Integer32"""
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


_AdslLineConfUSPhyr_Type.__name__ = "Integer32"
_AdslLineConfUSPhyr_Object = MibTableColumn
adslLineConfUSPhyr = _AdslLineConfUSPhyr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 24),
    _AdslLineConfUSPhyr_Type()
)
adslLineConfUSPhyr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfUSPhyr.setStatus("current")


class _AdslLineConfDSPhyr_Type(Integer32):
    """Custom type adslLineConfDSPhyr based on Integer32"""
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


_AdslLineConfDSPhyr_Type.__name__ = "Integer32"
_AdslLineConfDSPhyr_Object = MibTableColumn
adslLineConfDSPhyr = _AdslLineConfDSPhyr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 1, 1, 25),
    _AdslLineConfDSPhyr_Type()
)
adslLineConfDSPhyr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfDSPhyr.setStatus("current")
_AdslPortBatchSet_ObjectIdentity = ObjectIdentity
adslPortBatchSet = _AdslPortBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3)
)
_AdslPortTarget_Type = OctetString
_AdslPortTarget_Object = MibScalar
adslPortTarget = _AdslPortTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 1),
    _AdslPortTarget_Type()
)
adslPortTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortTarget.setStatus("current")
_AdslPortOps_Type = Integer32
_AdslPortOps_Object = MibScalar
adslPortOps = _AdslPortOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 2),
    _AdslPortOps_Type()
)
adslPortOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortOps.setStatus("current")
_AdslPortOps2_Type = Integer32
_AdslPortOps2_Object = MibScalar
adslPortOps2 = _AdslPortOps2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 3),
    _AdslPortOps2_Type()
)
adslPortOps2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPortOps2.setStatus("current")


class _AdslModeForBatchSet_Type(Integer32):
    """Custom type adslModeForBatchSet based on Integer32"""
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
        *(("adsl2", 6),
          ("adsl2Plus", 7),
          ("auto", 4),
          ("etsi", 5),
          ("gDotDmt", 2),
          ("gDotLite", 1),
          ("t1Dot413", 3))
    )


_AdslModeForBatchSet_Type.__name__ = "Integer32"
_AdslModeForBatchSet_Object = MibScalar
adslModeForBatchSet = _AdslModeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 4),
    _AdslModeForBatchSet_Type()
)
adslModeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslModeForBatchSet.setStatus("current")


class _AdslLineProfileForBatchSet_Type(DisplayString):
    """Custom type adslLineProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AdslLineProfileForBatchSet_Type.__name__ = "DisplayString"
_AdslLineProfileForBatchSet_Object = MibScalar
adslLineProfileForBatchSet = _AdslLineProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 5),
    _AdslLineProfileForBatchSet_Type()
)
adslLineProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineProfileForBatchSet.setStatus("current")


class _AdslAlarmProfileForBatchSet_Type(DisplayString):
    """Custom type adslAlarmProfileForBatchSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AdslAlarmProfileForBatchSet_Type.__name__ = "DisplayString"
_AdslAlarmProfileForBatchSet_Object = MibScalar
adslAlarmProfileForBatchSet = _AdslAlarmProfileForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 6),
    _AdslAlarmProfileForBatchSet_Type()
)
adslAlarmProfileForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAlarmProfileForBatchSet.setStatus("current")
_AdslOptionMaskForBatchSet_Type = Integer32
_AdslOptionMaskForBatchSet_Object = MibScalar
adslOptionMaskForBatchSet = _AdslOptionMaskForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 7),
    _AdslOptionMaskForBatchSet_Type()
)
adslOptionMaskForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslOptionMaskForBatchSet.setStatus("current")


class _AdslAturMaxTxPowerForBatchSet_Type(Integer32):
    """Custom type adslAturMaxTxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_AdslAturMaxTxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslAturMaxTxPowerForBatchSet_Object = MibScalar
adslAturMaxTxPowerForBatchSet = _AdslAturMaxTxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 8),
    _AdslAturMaxTxPowerForBatchSet_Type()
)
adslAturMaxTxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturMaxTxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslAturMaxTxPowerForBatchSet.setUnits("tenth dBm")


class _AdslAtucMaxTxPowerForBatchSet_Type(Integer32):
    """Custom type adslAtucMaxTxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_AdslAtucMaxTxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslAtucMaxTxPowerForBatchSet_Object = MibScalar
adslAtucMaxTxPowerForBatchSet = _AdslAtucMaxTxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 9),
    _AdslAtucMaxTxPowerForBatchSet_Type()
)
adslAtucMaxTxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucMaxTxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucMaxTxPowerForBatchSet.setUnits("tenth dBm")


class _AdslMaxRxPowerForBatchSet_Type(Integer32):
    """Custom type adslMaxRxPowerForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_AdslMaxRxPowerForBatchSet_Type.__name__ = "Integer32"
_AdslMaxRxPowerForBatchSet_Object = MibScalar
adslMaxRxPowerForBatchSet = _AdslMaxRxPowerForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 10),
    _AdslMaxRxPowerForBatchSet_Type()
)
adslMaxRxPowerForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMaxRxPowerForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMaxRxPowerForBatchSet.setUnits("tenth dBm")
_AdslAturCarrierMaskForBatchSet_Type = OctetString
_AdslAturCarrierMaskForBatchSet_Object = MibScalar
adslAturCarrierMaskForBatchSet = _AdslAturCarrierMaskForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 11),
    _AdslAturCarrierMaskForBatchSet_Type()
)
adslAturCarrierMaskForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturCarrierMaskForBatchSet.setStatus("current")
_AdslAtucCarrierMask0ForBatchSet_Type = OctetString
_AdslAtucCarrierMask0ForBatchSet_Object = MibScalar
adslAtucCarrierMask0ForBatchSet = _AdslAtucCarrierMask0ForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 12),
    _AdslAtucCarrierMask0ForBatchSet_Type()
)
adslAtucCarrierMask0ForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucCarrierMask0ForBatchSet.setStatus("current")
_AdslAtucCarrierMask1ForBatchSet_Type = OctetString
_AdslAtucCarrierMask1ForBatchSet_Object = MibScalar
adslAtucCarrierMask1ForBatchSet = _AdslAtucCarrierMask1ForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 13),
    _AdslAtucCarrierMask1ForBatchSet_Type()
)
adslAtucCarrierMask1ForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucCarrierMask1ForBatchSet.setStatus("current")


class _AdslAturInpForBatchSet_Type(Integer32):
    """Custom type adslAturInpForBatchSet based on Integer32"""
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
        *(("eight", 6),
          ("four", 5),
          ("one", 3),
          ("sixteen", 7),
          ("two", 4),
          ("zero", 1),
          ("zeroPointFive", 2))
    )


_AdslAturInpForBatchSet_Type.__name__ = "Integer32"
_AdslAturInpForBatchSet_Object = MibScalar
adslAturInpForBatchSet = _AdslAturInpForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 14),
    _AdslAturInpForBatchSet_Type()
)
adslAturInpForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAturInpForBatchSet.setStatus("current")


class _AdslAtucInpForBatchSet_Type(Integer32):
    """Custom type adslAtucInpForBatchSet based on Integer32"""
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
        *(("eight", 6),
          ("four", 5),
          ("one", 3),
          ("sixteen", 7),
          ("two", 4),
          ("zero", 1),
          ("zeroPointFive", 2))
    )


_AdslAtucInpForBatchSet_Type.__name__ = "Integer32"
_AdslAtucInpForBatchSet_Object = MibScalar
adslAtucInpForBatchSet = _AdslAtucInpForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 15),
    _AdslAtucInpForBatchSet_Type()
)
adslAtucInpForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslAtucInpForBatchSet.setStatus("current")
_AdslL0TimeForBatchSet_Type = Integer32
_AdslL0TimeForBatchSet_Object = MibScalar
adslL0TimeForBatchSet = _AdslL0TimeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 16),
    _AdslL0TimeForBatchSet_Type()
)
adslL0TimeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL0TimeForBatchSet.setStatus("current")
_AdslL2TimeForBatchSet_Type = Integer32
_AdslL2TimeForBatchSet_Object = MibScalar
adslL2TimeForBatchSet = _AdslL2TimeForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 17),
    _AdslL2TimeForBatchSet_Type()
)
adslL2TimeForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2TimeForBatchSet.setStatus("current")
_AdslL2ATPRForBatchSet_Type = Integer32
_AdslL2ATPRForBatchSet_Object = MibScalar
adslL2ATPRForBatchSet = _AdslL2ATPRForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 18),
    _AdslL2ATPRForBatchSet_Type()
)
adslL2ATPRForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2ATPRForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL2ATPRForBatchSet.setUnits("dB")
_AdslL2ATPRTForBatchSet_Type = Integer32
_AdslL2ATPRTForBatchSet_Object = MibScalar
adslL2ATPRTForBatchSet = _AdslL2ATPRTForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 19),
    _AdslL2ATPRTForBatchSet_Type()
)
adslL2ATPRTForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL2ATPRTForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL2ATPRTForBatchSet.setUnits("dB")
_AdslMaxL2RateForBatchSet_Type = Integer32
_AdslMaxL2RateForBatchSet_Object = MibScalar
adslMaxL2RateForBatchSet = _AdslMaxL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 20),
    _AdslMaxL2RateForBatchSet_Type()
)
adslMaxL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMaxL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMaxL2RateForBatchSet.setUnits("kbps")
_AdslMinL2RateForBatchSet_Type = Integer32
_AdslMinL2RateForBatchSet_Object = MibScalar
adslMinL2RateForBatchSet = _AdslMinL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 21),
    _AdslMinL2RateForBatchSet_Type()
)
adslMinL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslMinL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslMinL2RateForBatchSet.setUnits("kbps")
_AdslL0toL2RateForBatchSet_Type = Integer32
_AdslL0toL2RateForBatchSet_Object = MibScalar
adslL0toL2RateForBatchSet = _AdslL0toL2RateForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 3, 22),
    _AdslL0toL2RateForBatchSet_Type()
)
adslL0toL2RateForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslL0toL2RateForBatchSet.setStatus("current")
if mibBuilder.loadTexts:
    adslL0toL2RateForBatchSet.setUnits("kbps")
_AdslLineStatusTable_Object = MibTable
adslLineStatusTable = _AdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 4)
)
if mibBuilder.loadTexts:
    adslLineStatusTable.setStatus("current")
_AdslLineStatusEntry_Object = MibTableRow
adslLineStatusEntry = _AdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 4, 1)
)
adslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslLineStatusEntry.setStatus("current")


class _AdslLineStatusMode_Type(Integer32):
    """Custom type adslLineStatusMode based on Integer32"""
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
        *(("adsl2", 5),
          ("adsl2Plus", 6),
          ("etsi", 4),
          ("gDotDmt", 2),
          ("gDotLite", 1),
          ("none", 7),
          ("t1Dot413", 3))
    )


_AdslLineStatusMode_Type.__name__ = "Integer32"
_AdslLineStatusMode_Object = MibTableColumn
adslLineStatusMode = _AdslLineStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 4, 1, 1),
    _AdslLineStatusMode_Type()
)
adslLineStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineStatusMode.setStatus("current")
_AdslLineUpTime_Type = Integer32
_AdslLineUpTime_Object = MibTableColumn
adslLineUpTime = _AdslLineUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 4, 1, 2),
    _AdslLineUpTime_Type()
)
adslLineUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineUpTime.setStatus("current")
_PowerMgmtParamTable_Object = MibTable
powerMgmtParamTable = _PowerMgmtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5)
)
if mibBuilder.loadTexts:
    powerMgmtParamTable.setStatus("current")
_PowerMgmtParamEntry_Object = MibTableRow
powerMgmtParamEntry = _PowerMgmtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1)
)
powerMgmtParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtParamEntry.setStatus("current")
_PowerMgmtL0Time_Type = Integer32
_PowerMgmtL0Time_Object = MibTableColumn
powerMgmtL0Time = _PowerMgmtL0Time_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 1),
    _PowerMgmtL0Time_Type()
)
powerMgmtL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL0Time.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL0Time.setUnits("second")
_PowerMgmtL2Time_Type = Integer32
_PowerMgmtL2Time_Object = MibTableColumn
powerMgmtL2Time = _PowerMgmtL2Time_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 2),
    _PowerMgmtL2Time_Type()
)
powerMgmtL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Time.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Time.setUnits("second")
_PowerMgmtL2Atpr_Type = Integer32
_PowerMgmtL2Atpr_Object = MibTableColumn
powerMgmtL2Atpr = _PowerMgmtL2Atpr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 3),
    _PowerMgmtL2Atpr_Type()
)
powerMgmtL2Atpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Atpr.setUnits("dB")
_PowerMgmtL2Atprt_Type = Integer32
_PowerMgmtL2Atprt_Object = MibTableColumn
powerMgmtL2Atprt = _PowerMgmtL2Atprt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 4),
    _PowerMgmtL2Atprt_Type()
)
powerMgmtL2Atprt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2Atprt.setUnits("dB")
_PowerMgmtL2MinRate_Type = Integer32
_PowerMgmtL2MinRate_Object = MibTableColumn
powerMgmtL2MinRate = _PowerMgmtL2MinRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 5),
    _PowerMgmtL2MinRate_Type()
)
powerMgmtL2MinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2MinRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2MinRate.setUnits("Kbps")
_PowerMgmtL2MaxRate_Type = Integer32
_PowerMgmtL2MaxRate_Object = MibTableColumn
powerMgmtL2MaxRate = _PowerMgmtL2MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 6),
    _PowerMgmtL2MaxRate_Type()
)
powerMgmtL2MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2MaxRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2MaxRate.setUnits("Kbps")
_PowerMgmtL2ThreshRate_Type = Integer32
_PowerMgmtL2ThreshRate_Object = MibTableColumn
powerMgmtL2ThreshRate = _PowerMgmtL2ThreshRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 5, 1, 7),
    _PowerMgmtL2ThreshRate_Type()
)
powerMgmtL2ThreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtL2ThreshRate.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtL2ThreshRate.setUnits("Kbps")
_PowerMgmtPSDTable_Object = MibTable
powerMgmtPSDTable = _PowerMgmtPSDTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 6)
)
if mibBuilder.loadTexts:
    powerMgmtPSDTable.setStatus("current")
_PowerMgmtPSDEntry_Object = MibTableRow
powerMgmtPSDEntry = _PowerMgmtPSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 6, 1)
)
powerMgmtPSDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtPSDEntry.setStatus("current")
_PowerMgmtAtucMaxPSD_Type = Integer32
_PowerMgmtAtucMaxPSD_Object = MibTableColumn
powerMgmtAtucMaxPSD = _PowerMgmtAtucMaxPSD_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 6, 1, 1),
    _PowerMgmtAtucMaxPSD_Type()
)
powerMgmtAtucMaxPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtAtucMaxPSD.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtAtucMaxPSD.setUnits("0.1dBm/Hz")
_PowerMgmtAturMaxPSD_Type = Integer32
_PowerMgmtAturMaxPSD_Object = MibTableColumn
powerMgmtAturMaxPSD = _PowerMgmtAturMaxPSD_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 2, 6, 1, 2),
    _PowerMgmtAturMaxPSD_Type()
)
powerMgmtAturMaxPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtAturMaxPSD.setStatus("current")
if mibBuilder.loadTexts:
    powerMgmtAturMaxPSD.setUnits("0.1dBm/Hz")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4)
)
_MaxNumOfPvcs_Type = Integer32
_MaxNumOfPvcs_Object = MibScalar
maxNumOfPvcs = _MaxNumOfPvcs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 1),
    _MaxNumOfPvcs_Type()
)
maxNumOfPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPvcs.setStatus("current")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("current")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "pvcVpi"),
    (0, "E5-111-MIB", "pvcVci"),
    (0, "E5-111-MIB", "pvcPvid"),
)
if mibBuilder.loadTexts:
    pvcEntry.setStatus("current")


class _PvcVpi_Type(Integer32):
    """Custom type pvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcVpi_Type.__name__ = "Integer32"
_PvcVpi_Object = MibTableColumn
pvcVpi = _PvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 1),
    _PvcVpi_Type()
)
pvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVpi.setStatus("current")


class _PvcVci_Type(Integer32):
    """Custom type pvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcVci_Type.__name__ = "Integer32"
_PvcVci_Object = MibTableColumn
pvcVci = _PvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 2),
    _PvcVci_Type()
)
pvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcVci.setStatus("current")
_PvcPvid_Type = VlanIndex
_PvcPvid_Object = MibTableColumn
pvcPvid = _PvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 3),
    _PvcPvid_Type()
)
pvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPvid.setStatus("current")


class _PvcPriority_Type(Integer32):
    """Custom type pvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcPriority_Type.__name__ = "Integer32"
_PvcPriority_Object = MibTableColumn
pvcPriority = _PvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 5),
    _PvcPriority_Type()
)
pvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcPriority.setStatus("current")


class _PvcProfileDS_Type(DisplayString):
    """Custom type pvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfileDS_Type.__name__ = "DisplayString"
_PvcProfileDS_Object = MibTableColumn
pvcProfileDS = _PvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 6),
    _PvcProfileDS_Type()
)
pvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileDS.setStatus("current")
_PvcRowStatus_Type = RowStatus
_PvcRowStatus_Object = MibTableColumn
pvcRowStatus = _PvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 7),
    _PvcRowStatus_Type()
)
pvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcRowStatus.setStatus("current")


class _PvcProfileUS_Type(DisplayString):
    """Custom type pvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcProfileUS_Type.__name__ = "DisplayString"
_PvcProfileUS_Object = MibTableColumn
pvcProfileUS = _PvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 8),
    _PvcProfileUS_Type()
)
pvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcProfileUS.setStatus("current")
_PvcAcName_Type = DisplayString
_PvcAcName_Object = MibTableColumn
pvcAcName = _PvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 11),
    _PvcAcName_Type()
)
pvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcAcName.setStatus("current")
_PvcServiceName_Type = DisplayString
_PvcServiceName_Object = MibTableColumn
pvcServiceName = _PvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 12),
    _PvcServiceName_Type()
)
pvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcServiceName.setStatus("current")
_PvcHelloTime_Type = Integer32
_PvcHelloTime_Object = MibTableColumn
pvcHelloTime = _PvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 2, 1, 13),
    _PvcHelloTime_Type()
)
pvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    pvcHelloTime.setUnits("second")
_PvcStateTable_Object = MibTable
pvcStateTable = _PvcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3)
)
if mibBuilder.loadTexts:
    pvcStateTable.setStatus("current")
_PvcStateEntry_Object = MibTableRow
pvcStateEntry = _PvcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1)
)
pvcStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "pvcStateVpi"),
    (0, "E5-111-MIB", "pvcStateVci"),
    (0, "E5-111-MIB", "pvcStatePvid"),
)
if mibBuilder.loadTexts:
    pvcStateEntry.setStatus("current")


class _PvcStateVpi_Type(Integer32):
    """Custom type pvcStateVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcStateVpi_Type.__name__ = "Integer32"
_PvcStateVpi_Object = MibTableColumn
pvcStateVpi = _PvcStateVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 1),
    _PvcStateVpi_Type()
)
pvcStateVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateVpi.setStatus("current")


class _PvcStateVci_Type(Integer32):
    """Custom type pvcStateVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcStateVci_Type.__name__ = "Integer32"
_PvcStateVci_Object = MibTableColumn
pvcStateVci = _PvcStateVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 2),
    _PvcStateVci_Type()
)
pvcStateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateVci.setStatus("current")
_PvcStatePvid_Type = VlanIndex
_PvcStatePvid_Object = MibTableColumn
pvcStatePvid = _PvcStatePvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 3),
    _PvcStatePvid_Type()
)
pvcStatePvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatePvid.setStatus("current")


class _PvcStatePriority_Type(Integer32):
    """Custom type pvcStatePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PvcStatePriority_Type.__name__ = "Integer32"
_PvcStatePriority_Object = MibTableColumn
pvcStatePriority = _PvcStatePriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 4),
    _PvcStatePriority_Type()
)
pvcStatePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatePriority.setStatus("current")


class _PvcStateChannelType_Type(DisplayString):
    """Custom type pvcStateChannelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcStateChannelType_Type.__name__ = "DisplayString"
_PvcStateChannelType_Object = MibTableColumn
pvcStateChannelType = _PvcStateChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 8),
    _PvcStateChannelType_Type()
)
pvcStateChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateChannelType.setStatus("current")


class _PvcStateEncap_Type(DisplayString):
    """Custom type pvcStateEncap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PvcStateEncap_Type.__name__ = "DisplayString"
_PvcStateEncap_Object = MibTableColumn
pvcStateEncap = _PvcStateEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 3, 1, 9),
    _PvcStateEncap_Type()
)
pvcStateEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStateEncap.setStatus("current")
_PvcUsRateLimitTable_Object = MibTable
pvcUsRateLimitTable = _PvcUsRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 4)
)
if mibBuilder.loadTexts:
    pvcUsRateLimitTable.setStatus("current")
_PvcUsRateLimitEntry_Object = MibTableRow
pvcUsRateLimitEntry = _PvcUsRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 4, 1)
)
pvcUsRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "pvcVpi"),
    (0, "E5-111-MIB", "pvcVci"),
)
if mibBuilder.loadTexts:
    pvcUsRateLimitEntry.setStatus("current")


class _PvcUsRateLimitEnable_Type(Integer32):
    """Custom type pvcUsRateLimitEnable based on Integer32"""
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


_PvcUsRateLimitEnable_Type.__name__ = "Integer32"
_PvcUsRateLimitEnable_Object = MibTableColumn
pvcUsRateLimitEnable = _PvcUsRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 4, 1, 1),
    _PvcUsRateLimitEnable_Type()
)
pvcUsRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimitEnable.setStatus("current")
_PvcUsRateLimit_Type = Integer32
_PvcUsRateLimit_Object = MibTableColumn
pvcUsRateLimit = _PvcUsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 4, 4, 1, 2),
    _PvcUsRateLimit_Type()
)
pvcUsRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    pvcUsRateLimit.setUnits("Kbps")
_Ppvc_ObjectIdentity = ObjectIdentity
ppvc = _Ppvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5)
)
_MaxNumOfPriorityPvcs_Type = Integer32
_MaxNumOfPriorityPvcs_Object = MibScalar
maxNumOfPriorityPvcs = _MaxNumOfPriorityPvcs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 1),
    _MaxNumOfPriorityPvcs_Type()
)
maxNumOfPriorityPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPriorityPvcs.setStatus("current")
_PpvcTable_Object = MibTable
ppvcTable = _PpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2)
)
if mibBuilder.loadTexts:
    ppvcTable.setStatus("current")
_PpvcEntry_Object = MibTableRow
ppvcEntry = _PpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1)
)
ppvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "ppvcVpi"),
    (0, "E5-111-MIB", "ppvcVci"),
    (0, "E5-111-MIB", "ppvcPvid"),
)
if mibBuilder.loadTexts:
    ppvcEntry.setStatus("current")


class _PpvcVpi_Type(Integer32):
    """Custom type ppvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PpvcVpi_Type.__name__ = "Integer32"
_PpvcVpi_Object = MibTableColumn
ppvcVpi = _PpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 1),
    _PpvcVpi_Type()
)
ppvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcVpi.setStatus("current")


class _PpvcVci_Type(Integer32):
    """Custom type ppvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PpvcVci_Type.__name__ = "Integer32"
_PpvcVci_Object = MibTableColumn
ppvcVci = _PpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 2),
    _PpvcVci_Type()
)
ppvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcVci.setStatus("current")
_PpvcPvid_Type = VlanIndex
_PpvcPvid_Object = MibTableColumn
ppvcPvid = _PpvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 3),
    _PpvcPvid_Type()
)
ppvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcPvid.setStatus("current")


class _PpvcEncap_Type(Integer32):
    """Custom type ppvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_PpvcEncap_Type.__name__ = "Integer32"
_PpvcEncap_Object = MibTableColumn
ppvcEncap = _PpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 4),
    _PpvcEncap_Type()
)
ppvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcEncap.setStatus("current")


class _PpvcPriority_Type(Integer32):
    """Custom type ppvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PpvcPriority_Type.__name__ = "Integer32"
_PpvcPriority_Object = MibTableColumn
ppvcPriority = _PpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 5),
    _PpvcPriority_Type()
)
ppvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcPriority.setStatus("current")
_PpvcRowStatus_Type = RowStatus
_PpvcRowStatus_Object = MibTableColumn
ppvcRowStatus = _PpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 2, 1, 6),
    _PpvcRowStatus_Type()
)
ppvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcRowStatus.setStatus("current")
_PpvcMemberTable_Object = MibTable
ppvcMemberTable = _PpvcMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4)
)
if mibBuilder.loadTexts:
    ppvcMemberTable.setStatus("current")
_PpvcMemberEntry_Object = MibTableRow
ppvcMemberEntry = _PpvcMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1)
)
ppvcMemberEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "ppvcVpi"),
    (0, "E5-111-MIB", "ppvcVci"),
    (0, "E5-111-MIB", "ppvcMemberVpi"),
    (0, "E5-111-MIB", "ppvcMemberVci"),
    (0, "E5-111-MIB", "ppvcMemberPriority"),
)
if mibBuilder.loadTexts:
    ppvcMemberEntry.setStatus("current")


class _PpvcMemberVpi_Type(Integer32):
    """Custom type ppvcMemberVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PpvcMemberVpi_Type.__name__ = "Integer32"
_PpvcMemberVpi_Object = MibTableColumn
ppvcMemberVpi = _PpvcMemberVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 1),
    _PpvcMemberVpi_Type()
)
ppvcMemberVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberVpi.setStatus("current")


class _PpvcMemberVci_Type(Integer32):
    """Custom type ppvcMemberVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PpvcMemberVci_Type.__name__ = "Integer32"
_PpvcMemberVci_Object = MibTableColumn
ppvcMemberVci = _PpvcMemberVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 2),
    _PpvcMemberVci_Type()
)
ppvcMemberVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberVci.setStatus("current")


class _PpvcMemberPriority_Type(Integer32):
    """Custom type ppvcMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PpvcMemberPriority_Type.__name__ = "Integer32"
_PpvcMemberPriority_Object = MibTableColumn
ppvcMemberPriority = _PpvcMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 3),
    _PpvcMemberPriority_Type()
)
ppvcMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppvcMemberPriority.setStatus("current")


class _PpvcMemberProfileDS_Type(DisplayString):
    """Custom type ppvcMemberProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PpvcMemberProfileDS_Type.__name__ = "DisplayString"
_PpvcMemberProfileDS_Object = MibTableColumn
ppvcMemberProfileDS = _PpvcMemberProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 4),
    _PpvcMemberProfileDS_Type()
)
ppvcMemberProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileDS.setStatus("current")
_PpvcMemberRowStatus_Type = RowStatus
_PpvcMemberRowStatus_Object = MibTableColumn
ppvcMemberRowStatus = _PpvcMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 5),
    _PpvcMemberRowStatus_Type()
)
ppvcMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberRowStatus.setStatus("current")


class _PpvcMemberProfileUS_Type(DisplayString):
    """Custom type ppvcMemberProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PpvcMemberProfileUS_Type.__name__ = "DisplayString"
_PpvcMemberProfileUS_Object = MibTableColumn
ppvcMemberProfileUS = _PpvcMemberProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 5, 4, 1, 6),
    _PpvcMemberProfileUS_Type()
)
ppvcMemberProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ppvcMemberProfileUS.setStatus("current")
_Rpvc_ObjectIdentity = ObjectIdentity
rpvc = _Rpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8)
)
_RpvcGatewayTable_Object = MibTable
rpvcGatewayTable = _RpvcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1)
)
if mibBuilder.loadTexts:
    rpvcGatewayTable.setStatus("current")
_RpvcGatewayEntry_Object = MibTableRow
rpvcGatewayEntry = _RpvcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1, 1)
)
rpvcGatewayEntry.setIndexNames(
    (0, "E5-111-MIB", "rpvcGatewayIp"),
)
if mibBuilder.loadTexts:
    rpvcGatewayEntry.setStatus("current")
_RpvcGatewayIp_Type = IpAddress
_RpvcGatewayIp_Object = MibTableColumn
rpvcGatewayIp = _RpvcGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1, 1, 1),
    _RpvcGatewayIp_Type()
)
rpvcGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcGatewayIp.setStatus("current")
_RpvcGatewayVlanId_Type = VlanIndex
_RpvcGatewayVlanId_Object = MibTableColumn
rpvcGatewayVlanId = _RpvcGatewayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1, 1, 2),
    _RpvcGatewayVlanId_Type()
)
rpvcGatewayVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayVlanId.setStatus("current")
_RpvcGatewayRowStatus_Type = RowStatus
_RpvcGatewayRowStatus_Object = MibTableColumn
rpvcGatewayRowStatus = _RpvcGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1, 1, 3),
    _RpvcGatewayRowStatus_Type()
)
rpvcGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayRowStatus.setStatus("current")
_RpvcGatewayPriority_Type = Integer32
_RpvcGatewayPriority_Object = MibTableColumn
rpvcGatewayPriority = _RpvcGatewayPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 1, 1, 4),
    _RpvcGatewayPriority_Type()
)
rpvcGatewayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcGatewayPriority.setStatus("current")
_RpvcTable_Object = MibTable
rpvcTable = _RpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2)
)
if mibBuilder.loadTexts:
    rpvcTable.setStatus("current")
_RpvcEntry_Object = MibTableRow
rpvcEntry = _RpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1)
)
rpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "rpvcVpi"),
    (0, "E5-111-MIB", "rpvcVci"),
    (0, "E5-111-MIB", "rpvcIp"),
    (0, "E5-111-MIB", "rpvcNetmask"),
)
if mibBuilder.loadTexts:
    rpvcEntry.setStatus("current")


class _RpvcVpi_Type(Integer32):
    """Custom type rpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcVpi_Type.__name__ = "Integer32"
_RpvcVpi_Object = MibTableColumn
rpvcVpi = _RpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 1),
    _RpvcVpi_Type()
)
rpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVpi.setStatus("current")


class _RpvcVci_Type(Integer32):
    """Custom type rpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcVci_Type.__name__ = "Integer32"
_RpvcVci_Object = MibTableColumn
rpvcVci = _RpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 2),
    _RpvcVci_Type()
)
rpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcVci.setStatus("current")


class _RpvcDSProfile_Type(DisplayString):
    """Custom type rpvcDSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcDSProfile_Type.__name__ = "DisplayString"
_RpvcDSProfile_Object = MibTableColumn
rpvcDSProfile = _RpvcDSProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 3),
    _RpvcDSProfile_Type()
)
rpvcDSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcDSProfile.setStatus("current")


class _RpvcUSProfile_Type(DisplayString):
    """Custom type rpvcUSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RpvcUSProfile_Type.__name__ = "DisplayString"
_RpvcUSProfile_Object = MibTableColumn
rpvcUSProfile = _RpvcUSProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 4),
    _RpvcUSProfile_Type()
)
rpvcUSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcUSProfile.setStatus("current")
_RpvcIp_Type = IpAddress
_RpvcIp_Object = MibTableColumn
rpvcIp = _RpvcIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 5),
    _RpvcIp_Type()
)
rpvcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcIp.setStatus("current")
_RpvcNetmask_Type = IpAddress
_RpvcNetmask_Object = MibTableColumn
rpvcNetmask = _RpvcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 6),
    _RpvcNetmask_Type()
)
rpvcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcNetmask.setStatus("current")
_RpvcGatewayIpAddress_Type = IpAddress
_RpvcGatewayIpAddress_Object = MibTableColumn
rpvcGatewayIpAddress = _RpvcGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 7),
    _RpvcGatewayIpAddress_Type()
)
rpvcGatewayIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcGatewayIpAddress.setStatus("current")
_RpvcRowStatus_Type = RowStatus
_RpvcRowStatus_Object = MibTableColumn
rpvcRowStatus = _RpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 2, 1, 8),
    _RpvcRowStatus_Type()
)
rpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRowStatus.setStatus("current")
_RpvcRouteDomainTable_Object = MibTable
rpvcRouteDomainTable = _RpvcRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3)
)
if mibBuilder.loadTexts:
    rpvcRouteDomainTable.setStatus("current")
_RpvcRouteDomainEntry_Object = MibTableRow
rpvcRouteDomainEntry = _RpvcRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1)
)
rpvcRouteDomainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "rpvcRouteDomainVpi"),
    (0, "E5-111-MIB", "rpvcRouteDomainVci"),
    (0, "E5-111-MIB", "rpvcRouteDomainIp"),
    (0, "E5-111-MIB", "rpvcRouteDomainNetmask"),
)
if mibBuilder.loadTexts:
    rpvcRouteDomainEntry.setStatus("current")


class _RpvcRouteDomainVpi_Type(Integer32):
    """Custom type rpvcRouteDomainVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpvcRouteDomainVpi_Type.__name__ = "Integer32"
_RpvcRouteDomainVpi_Object = MibTableColumn
rpvcRouteDomainVpi = _RpvcRouteDomainVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1, 1),
    _RpvcRouteDomainVpi_Type()
)
rpvcRouteDomainVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVpi.setStatus("current")


class _RpvcRouteDomainVci_Type(Integer32):
    """Custom type rpvcRouteDomainVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpvcRouteDomainVci_Type.__name__ = "Integer32"
_RpvcRouteDomainVci_Object = MibTableColumn
rpvcRouteDomainVci = _RpvcRouteDomainVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1, 2),
    _RpvcRouteDomainVci_Type()
)
rpvcRouteDomainVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainVci.setStatus("current")
_RpvcRouteDomainIp_Type = IpAddress
_RpvcRouteDomainIp_Object = MibTableColumn
rpvcRouteDomainIp = _RpvcRouteDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1, 3),
    _RpvcRouteDomainIp_Type()
)
rpvcRouteDomainIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainIp.setStatus("current")
_RpvcRouteDomainNetmask_Type = IpAddress
_RpvcRouteDomainNetmask_Object = MibTableColumn
rpvcRouteDomainNetmask = _RpvcRouteDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1, 4),
    _RpvcRouteDomainNetmask_Type()
)
rpvcRouteDomainNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpvcRouteDomainNetmask.setStatus("current")
_RpvcRouteDomainRowStatus_Type = RowStatus
_RpvcRouteDomainRowStatus_Object = MibTableColumn
rpvcRouteDomainRowStatus = _RpvcRouteDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 3, 1, 5),
    _RpvcRouteDomainRowStatus_Type()
)
rpvcRouteDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rpvcRouteDomainRowStatus.setStatus("current")
_RpvcArpAgingTime_Type = Integer32
_RpvcArpAgingTime_Object = MibScalar
rpvcArpAgingTime = _RpvcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 4),
    _RpvcArpAgingTime_Type()
)
rpvcArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpAgingTime.setStatus("current")


class _RpvcArpFlush_Type(Integer32):
    """Custom type rpvcArpFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RpvcArpFlush_Type.__name__ = "Integer32"
_RpvcArpFlush_Object = MibScalar
rpvcArpFlush = _RpvcArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 8, 5),
    _RpvcArpFlush_Type()
)
rpvcArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpvcArpFlush.setStatus("current")
_DsBcastDisableTable_Object = MibTable
dsBcastDisableTable = _DsBcastDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 9)
)
if mibBuilder.loadTexts:
    dsBcastDisableTable.setStatus("current")
_DsBcastDisableEntry_Object = MibTableRow
dsBcastDisableEntry = _DsBcastDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 9, 1)
)
dsBcastDisableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "dsBcastDisableVlanId"),
)
if mibBuilder.loadTexts:
    dsBcastDisableEntry.setStatus("current")
_DsBcastDisableVlanId_Type = Integer32
_DsBcastDisableVlanId_Object = MibTableColumn
dsBcastDisableVlanId = _DsBcastDisableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 9, 1, 1),
    _DsBcastDisableVlanId_Type()
)
dsBcastDisableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsBcastDisableVlanId.setStatus("current")
_DsBcastDisableRowStatus_Type = RowStatus
_DsBcastDisableRowStatus_Object = MibTableColumn
dsBcastDisableRowStatus = _DsBcastDisableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 9, 1, 2),
    _DsBcastDisableRowStatus_Type()
)
dsBcastDisableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsBcastDisableRowStatus.setStatus("current")
_Paepvc_ObjectIdentity = ObjectIdentity
paepvc = _Paepvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10)
)
_PaepvcTable_Object = MibTable
paepvcTable = _PaepvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    paepvcTable.setStatus("current")
_PaepvcEntry_Object = MibTableRow
paepvcEntry = _PaepvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1)
)
paepvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "paepvcVpi"),
    (0, "E5-111-MIB", "paepvcVci"),
    (0, "E5-111-MIB", "paepvcPvid"),
)
if mibBuilder.loadTexts:
    paepvcEntry.setStatus("current")


class _PaepvcVpi_Type(Integer32):
    """Custom type paepvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PaepvcVpi_Type.__name__ = "Integer32"
_PaepvcVpi_Object = MibTableColumn
paepvcVpi = _PaepvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 1),
    _PaepvcVpi_Type()
)
paepvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVpi.setStatus("current")


class _PaepvcVci_Type(Integer32):
    """Custom type paepvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PaepvcVci_Type.__name__ = "Integer32"
_PaepvcVci_Object = MibTableColumn
paepvcVci = _PaepvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 2),
    _PaepvcVci_Type()
)
paepvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcVci.setStatus("current")
_PaepvcPvid_Type = VlanIndex
_PaepvcPvid_Object = MibTableColumn
paepvcPvid = _PaepvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 3),
    _PaepvcPvid_Type()
)
paepvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcPvid.setStatus("current")


class _PaepvcPriority_Type(Integer32):
    """Custom type paepvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcPriority_Type.__name__ = "Integer32"
_PaepvcPriority_Object = MibTableColumn
paepvcPriority = _PaepvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 5),
    _PaepvcPriority_Type()
)
paepvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcPriority.setStatus("current")


class _PaepvcProfileDS_Type(DisplayString):
    """Custom type paepvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfileDS_Type.__name__ = "DisplayString"
_PaepvcProfileDS_Object = MibTableColumn
paepvcProfileDS = _PaepvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 6),
    _PaepvcProfileDS_Type()
)
paepvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileDS.setStatus("current")
_PaepvcAcName_Type = DisplayString
_PaepvcAcName_Object = MibTableColumn
paepvcAcName = _PaepvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 7),
    _PaepvcAcName_Type()
)
paepvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcAcName.setStatus("current")
_PaepvcServiceName_Type = DisplayString
_PaepvcServiceName_Object = MibTableColumn
paepvcServiceName = _PaepvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 8),
    _PaepvcServiceName_Type()
)
paepvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcServiceName.setStatus("current")
_PaepvcHelloTime_Type = Integer32
_PaepvcHelloTime_Object = MibTableColumn
paepvcHelloTime = _PaepvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 9),
    _PaepvcHelloTime_Type()
)
paepvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcHelloTime.setUnits("second")
_PaepvcRowStatus_Type = RowStatus
_PaepvcRowStatus_Object = MibTableColumn
paepvcRowStatus = _PaepvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 10),
    _PaepvcRowStatus_Type()
)
paepvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcRowStatus.setStatus("current")


class _PaepvcProfileUS_Type(DisplayString):
    """Custom type paepvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PaepvcProfileUS_Type.__name__ = "DisplayString"
_PaepvcProfileUS_Object = MibTableColumn
paepvcProfileUS = _PaepvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 11),
    _PaepvcProfileUS_Type()
)
paepvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcProfileUS.setStatus("current")
_PaepvcCvid_Type = VlanIndex
_PaepvcCvid_Object = MibTableColumn
paepvcCvid = _PaepvcCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 12),
    _PaepvcCvid_Type()
)
paepvcCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcCvid.setStatus("current")


class _PaepvcCPriority_Type(Integer32):
    """Custom type paepvcCPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PaepvcCPriority_Type.__name__ = "Integer32"
_PaepvcCPriority_Object = MibTableColumn
paepvcCPriority = _PaepvcCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 10, 1, 1, 13),
    _PaepvcCPriority_Type()
)
paepvcCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcCPriority.setStatus("current")
_Tlspvc_ObjectIdentity = ObjectIdentity
tlspvc = _Tlspvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11)
)
_TlspvcTable_Object = MibTable
tlspvcTable = _TlspvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1)
)
if mibBuilder.loadTexts:
    tlspvcTable.setStatus("current")
_TlspvcEntry_Object = MibTableRow
tlspvcEntry = _TlspvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1)
)
tlspvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "tlspvcVpi"),
    (0, "E5-111-MIB", "tlspvcVci"),
    (0, "E5-111-MIB", "tlspvcSvid"),
)
if mibBuilder.loadTexts:
    tlspvcEntry.setStatus("current")


class _TlspvcVpi_Type(Integer32):
    """Custom type tlspvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlspvcVpi_Type.__name__ = "Integer32"
_TlspvcVpi_Object = MibTableColumn
tlspvcVpi = _TlspvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 1),
    _TlspvcVpi_Type()
)
tlspvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVpi.setStatus("current")


class _TlspvcVci_Type(Integer32):
    """Custom type tlspvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlspvcVci_Type.__name__ = "Integer32"
_TlspvcVci_Object = MibTableColumn
tlspvcVci = _TlspvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 2),
    _TlspvcVci_Type()
)
tlspvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcVci.setStatus("current")
_TlspvcSvid_Type = VlanIndex
_TlspvcSvid_Object = MibTableColumn
tlspvcSvid = _TlspvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 3),
    _TlspvcSvid_Type()
)
tlspvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlspvcSvid.setStatus("current")


class _TlspvcSpriority_Type(Integer32):
    """Custom type tlspvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TlspvcSpriority_Type.__name__ = "Integer32"
_TlspvcSpriority_Object = MibTableColumn
tlspvcSpriority = _TlspvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 5),
    _TlspvcSpriority_Type()
)
tlspvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcSpriority.setStatus("current")


class _TlspvcProfileDS_Type(DisplayString):
    """Custom type tlspvcProfileDS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfileDS_Type.__name__ = "DisplayString"
_TlspvcProfileDS_Object = MibTableColumn
tlspvcProfileDS = _TlspvcProfileDS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 6),
    _TlspvcProfileDS_Type()
)
tlspvcProfileDS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileDS.setStatus("current")
_TlspvcRowStatus_Type = RowStatus
_TlspvcRowStatus_Object = MibTableColumn
tlspvcRowStatus = _TlspvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 7),
    _TlspvcRowStatus_Type()
)
tlspvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcRowStatus.setStatus("current")


class _TlspvcProfileUS_Type(DisplayString):
    """Custom type tlspvcProfileUS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TlspvcProfileUS_Type.__name__ = "DisplayString"
_TlspvcProfileUS_Object = MibTableColumn
tlspvcProfileUS = _TlspvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 11, 1, 1, 8),
    _TlspvcProfileUS_Type()
)
tlspvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlspvcProfileUS.setStatus("current")
_Ipbpvc_ObjectIdentity = ObjectIdentity
ipbpvc = _Ipbpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12)
)
_IpbpvcDomainTable_Object = MibTable
ipbpvcDomainTable = _IpbpvcDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 1)
)
if mibBuilder.loadTexts:
    ipbpvcDomainTable.setStatus("current")
_IpbpvcDomainEntry_Object = MibTableRow
ipbpvcDomainEntry = _IpbpvcDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 1, 1)
)
ipbpvcDomainEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
)
if mibBuilder.loadTexts:
    ipbpvcDomainEntry.setStatus("current")
_IpbpvcDomainName_Type = OctetString
_IpbpvcDomainName_Object = MibTableColumn
ipbpvcDomainName = _IpbpvcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 1, 1, 1),
    _IpbpvcDomainName_Type()
)
ipbpvcDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcDomainName.setStatus("current")
_IpbpvcDomainRowStatus_Type = RowStatus
_IpbpvcDomainRowStatus_Object = MibTableColumn
ipbpvcDomainRowStatus = _IpbpvcDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 1, 1, 2),
    _IpbpvcDomainRowStatus_Type()
)
ipbpvcDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainRowStatus.setStatus("current")
_IpbpvcDomainVlanTable_Object = MibTable
ipbpvcDomainVlanTable = _IpbpvcDomainVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 2)
)
if mibBuilder.loadTexts:
    ipbpvcDomainVlanTable.setStatus("current")
_IpbpvcDomainVlanEntry_Object = MibTableRow
ipbpvcDomainVlanEntry = _IpbpvcDomainVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 2, 1)
)
ipbpvcDomainVlanEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcDomainVlanId"),
)
if mibBuilder.loadTexts:
    ipbpvcDomainVlanEntry.setStatus("current")
_IpbpvcDomainVlanId_Type = VlanIndex
_IpbpvcDomainVlanId_Object = MibTableColumn
ipbpvcDomainVlanId = _IpbpvcDomainVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 2, 1, 1),
    _IpbpvcDomainVlanId_Type()
)
ipbpvcDomainVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcDomainVlanId.setStatus("current")


class _IpbpvcDomainDhcpVlanEnable_Type(Integer32):
    """Custom type ipbpvcDomainDhcpVlanEnable based on Integer32"""
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


_IpbpvcDomainDhcpVlanEnable_Type.__name__ = "Integer32"
_IpbpvcDomainDhcpVlanEnable_Object = MibTableColumn
ipbpvcDomainDhcpVlanEnable = _IpbpvcDomainDhcpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 2, 1, 2),
    _IpbpvcDomainDhcpVlanEnable_Type()
)
ipbpvcDomainDhcpVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainDhcpVlanEnable.setStatus("current")
_IpbpvcDomainVlanRowStatus_Type = RowStatus
_IpbpvcDomainVlanRowStatus_Object = MibTableColumn
ipbpvcDomainVlanRowStatus = _IpbpvcDomainVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 2, 1, 3),
    _IpbpvcDomainVlanRowStatus_Type()
)
ipbpvcDomainVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcDomainVlanRowStatus.setStatus("current")
_IpbpvcEdgeRouterTable_Object = MibTable
ipbpvcEdgeRouterTable = _IpbpvcEdgeRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3)
)
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterTable.setStatus("current")
_IpbpvcEdgeRouterEntry_Object = MibTableRow
ipbpvcEdgeRouterEntry = _IpbpvcEdgeRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3, 1)
)
ipbpvcEdgeRouterEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcEdgeRouterIp"),
    (0, "E5-111-MIB", "ipbpvcEdgeRouterMask"),
    (0, "E5-111-MIB", "ipbpvcEdgeRouterVid"),
)
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterEntry.setStatus("current")
_IpbpvcEdgeRouterIp_Type = IpAddress
_IpbpvcEdgeRouterIp_Object = MibTableColumn
ipbpvcEdgeRouterIp = _IpbpvcEdgeRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3, 1, 1),
    _IpbpvcEdgeRouterIp_Type()
)
ipbpvcEdgeRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterIp.setStatus("current")
_IpbpvcEdgeRouterVid_Type = VlanIndex
_IpbpvcEdgeRouterVid_Object = MibTableColumn
ipbpvcEdgeRouterVid = _IpbpvcEdgeRouterVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3, 1, 2),
    _IpbpvcEdgeRouterVid_Type()
)
ipbpvcEdgeRouterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterVid.setStatus("current")
_IpbpvcEdgeRouterMask_Type = Integer32
_IpbpvcEdgeRouterMask_Object = MibTableColumn
ipbpvcEdgeRouterMask = _IpbpvcEdgeRouterMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3, 1, 3),
    _IpbpvcEdgeRouterMask_Type()
)
ipbpvcEdgeRouterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterMask.setStatus("current")
_IpbpvcEdgeRouterRowStatus_Type = RowStatus
_IpbpvcEdgeRouterRowStatus_Object = MibTableColumn
ipbpvcEdgeRouterRowStatus = _IpbpvcEdgeRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 3, 1, 4),
    _IpbpvcEdgeRouterRowStatus_Type()
)
ipbpvcEdgeRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcEdgeRouterRowStatus.setStatus("current")
_IpbpvcInterfaceTable_Object = MibTable
ipbpvcInterfaceTable = _IpbpvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4)
)
if mibBuilder.loadTexts:
    ipbpvcInterfaceTable.setStatus("current")
_IpbpvcInterfaceEntry_Object = MibTableRow
ipbpvcInterfaceEntry = _IpbpvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1)
)
ipbpvcInterfaceEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcInterfaceIp"),
    (0, "E5-111-MIB", "ipbpvcInterfaceMask"),
    (0, "E5-111-MIB", "ipbpvcInterfaceVid"),
)
if mibBuilder.loadTexts:
    ipbpvcInterfaceEntry.setStatus("current")
_IpbpvcInterfaceIp_Type = IpAddress
_IpbpvcInterfaceIp_Object = MibTableColumn
ipbpvcInterfaceIp = _IpbpvcInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 1),
    _IpbpvcInterfaceIp_Type()
)
ipbpvcInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceIp.setStatus("current")
_IpbpvcInterfaceMask_Type = Integer32
_IpbpvcInterfaceMask_Object = MibTableColumn
ipbpvcInterfaceMask = _IpbpvcInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 2),
    _IpbpvcInterfaceMask_Type()
)
ipbpvcInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceMask.setStatus("current")
_IpbpvcInterfaceVid_Type = VlanIndex
_IpbpvcInterfaceVid_Object = MibTableColumn
ipbpvcInterfaceVid = _IpbpvcInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 3),
    _IpbpvcInterfaceVid_Type()
)
ipbpvcInterfaceVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVid.setStatus("current")
_IpbpvcInterfaceIfIndex_Type = Integer32
_IpbpvcInterfaceIfIndex_Object = MibTableColumn
ipbpvcInterfaceIfIndex = _IpbpvcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 4),
    _IpbpvcInterfaceIfIndex_Type()
)
ipbpvcInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceIfIndex.setStatus("current")
_IpbpvcInterfaceVpi_Type = Integer32
_IpbpvcInterfaceVpi_Object = MibTableColumn
ipbpvcInterfaceVpi = _IpbpvcInterfaceVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 5),
    _IpbpvcInterfaceVpi_Type()
)
ipbpvcInterfaceVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVpi.setStatus("current")
_IpbpvcInterfaceVci_Type = Integer32
_IpbpvcInterfaceVci_Object = MibTableColumn
ipbpvcInterfaceVci = _IpbpvcInterfaceVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 6),
    _IpbpvcInterfaceVci_Type()
)
ipbpvcInterfaceVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceVci.setStatus("current")
_IpbpvcInterfaceRowStatus_Type = RowStatus
_IpbpvcInterfaceRowStatus_Object = MibTableColumn
ipbpvcInterfaceRowStatus = _IpbpvcInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 4, 1, 7),
    _IpbpvcInterfaceRowStatus_Type()
)
ipbpvcInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcInterfaceRowStatus.setStatus("current")
_IpbpvcRouteTable_Object = MibTable
ipbpvcRouteTable = _IpbpvcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5)
)
if mibBuilder.loadTexts:
    ipbpvcRouteTable.setStatus("current")
_IpbpvcRouteEntry_Object = MibTableRow
ipbpvcRouteEntry = _IpbpvcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1)
)
ipbpvcRouteEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcRouteIp"),
    (0, "E5-111-MIB", "ipbpvcRouteMask"),
    (0, "E5-111-MIB", "ipbpvcRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipbpvcRouteEntry.setStatus("current")
_IpbpvcRouteIp_Type = IpAddress
_IpbpvcRouteIp_Object = MibTableColumn
ipbpvcRouteIp = _IpbpvcRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 1),
    _IpbpvcRouteIp_Type()
)
ipbpvcRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteIp.setStatus("current")
_IpbpvcRouteMask_Type = Integer32
_IpbpvcRouteMask_Object = MibTableColumn
ipbpvcRouteMask = _IpbpvcRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 2),
    _IpbpvcRouteMask_Type()
)
ipbpvcRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteMask.setStatus("current")
_IpbpvcRouteNextHop_Type = IpAddress
_IpbpvcRouteNextHop_Object = MibTableColumn
ipbpvcRouteNextHop = _IpbpvcRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 3),
    _IpbpvcRouteNextHop_Type()
)
ipbpvcRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteNextHop.setStatus("current")


class _IpbpvcRouteMetric_Type(Integer32):
    """Custom type ipbpvcRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IpbpvcRouteMetric_Type.__name__ = "Integer32"
_IpbpvcRouteMetric_Object = MibTableColumn
ipbpvcRouteMetric = _IpbpvcRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 4),
    _IpbpvcRouteMetric_Type()
)
ipbpvcRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRouteMetric.setStatus("current")
_IpbpvcRoutePriority_Type = Integer32
_IpbpvcRoutePriority_Object = MibTableColumn
ipbpvcRoutePriority = _IpbpvcRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 5),
    _IpbpvcRoutePriority_Type()
)
ipbpvcRoutePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRoutePriority.setStatus("current")
_IpbpvcRouteRowStatus_Type = RowStatus
_IpbpvcRouteRowStatus_Object = MibTableColumn
ipbpvcRouteRowStatus = _IpbpvcRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 5, 1, 6),
    _IpbpvcRouteRowStatus_Type()
)
ipbpvcRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRouteRowStatus.setStatus("current")
_IpbpvcTable_Object = MibTable
ipbpvcTable = _IpbpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6)
)
if mibBuilder.loadTexts:
    ipbpvcTable.setStatus("current")
_IpbpvcEntry_Object = MibTableRow
ipbpvcEntry = _IpbpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1)
)
ipbpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "ipbpvcVpi"),
    (0, "E5-111-MIB", "ipbpvcVci"),
    (0, "E5-111-MIB", "ipbpvcPvid"),
)
if mibBuilder.loadTexts:
    ipbpvcEntry.setStatus("current")
_IpbpvcVpi_Type = Integer32
_IpbpvcVpi_Object = MibTableColumn
ipbpvcVpi = _IpbpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 1),
    _IpbpvcVpi_Type()
)
ipbpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcVpi.setStatus("current")
_IpbpvcVci_Type = Integer32
_IpbpvcVci_Object = MibTableColumn
ipbpvcVci = _IpbpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 2),
    _IpbpvcVci_Type()
)
ipbpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcVci.setStatus("current")
_IpbpvcPvid_Type = Integer32
_IpbpvcPvid_Object = MibTableColumn
ipbpvcPvid = _IpbpvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 3),
    _IpbpvcPvid_Type()
)
ipbpvcPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcPvid.setStatus("current")


class _IpbpvcEncap_Type(Integer32):
    """Custom type ipbpvcEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipoa", 3),
          ("ipoe", 1),
          ("reserved", 2))
    )


_IpbpvcEncap_Type.__name__ = "Integer32"
_IpbpvcEncap_Object = MibTableColumn
ipbpvcEncap = _IpbpvcEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 4),
    _IpbpvcEncap_Type()
)
ipbpvcEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcEncap.setStatus("current")


class _IpbpvcPriority_Type(Integer32):
    """Custom type ipbpvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpbpvcPriority_Type.__name__ = "Integer32"
_IpbpvcPriority_Object = MibTableColumn
ipbpvcPriority = _IpbpvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 5),
    _IpbpvcPriority_Type()
)
ipbpvcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcPriority.setStatus("current")
_IpbpvcProfile_Type = OctetString
_IpbpvcProfile_Object = MibTableColumn
ipbpvcProfile = _IpbpvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 6),
    _IpbpvcProfile_Type()
)
ipbpvcProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcProfile.setStatus("current")
_IpbpvcRowStatus_Type = Integer32
_IpbpvcRowStatus_Object = MibTableColumn
ipbpvcRowStatus = _IpbpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 7),
    _IpbpvcRowStatus_Type()
)
ipbpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcRowStatus.setStatus("current")
_IpbpvcProfileUS_Type = OctetString
_IpbpvcProfileUS_Object = MibTableColumn
ipbpvcProfileUS = _IpbpvcProfileUS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 6, 1, 8),
    _IpbpvcProfileUS_Type()
)
ipbpvcProfileUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipbpvcProfileUS.setStatus("current")
_Arpproxy_ObjectIdentity = ObjectIdentity
arpproxy = _Arpproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8)
)


class _ArpproxyAge_Type(Integer32):
    """Custom type arpproxyAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_ArpproxyAge_Type.__name__ = "Integer32"
_ArpproxyAge_Object = MibScalar
arpproxyAge = _ArpproxyAge_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 1),
    _ArpproxyAge_Type()
)
arpproxyAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyAge.setStatus("current")
if mibBuilder.loadTexts:
    arpproxyAge.setUnits("second")
_ArpproxyFlush_ObjectIdentity = ObjectIdentity
arpproxyFlush = _ArpproxyFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2)
)


class _ArpproxyFlushTarget_Type(Integer32):
    """Custom type arpproxyFlushTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("edgerouter", 2),
          ("interface", 3))
    )


_ArpproxyFlushTarget_Type.__name__ = "Integer32"
_ArpproxyFlushTarget_Object = MibScalar
arpproxyFlushTarget = _ArpproxyFlushTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 1),
    _ArpproxyFlushTarget_Type()
)
arpproxyFlushTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushTarget.setStatus("current")
_ArpproxyFlushOps_Type = Integer32
_ArpproxyFlushOps_Object = MibScalar
arpproxyFlushOps = _ArpproxyFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 2),
    _ArpproxyFlushOps_Type()
)
arpproxyFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushOps.setStatus("current")
_ArpproxyFlushEdgeRouterIp_Type = IpAddress
_ArpproxyFlushEdgeRouterIp_Object = MibScalar
arpproxyFlushEdgeRouterIp = _ArpproxyFlushEdgeRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 3),
    _ArpproxyFlushEdgeRouterIp_Type()
)
arpproxyFlushEdgeRouterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushEdgeRouterIp.setStatus("current")
_ArpproxyFlushEdgeRouterVid_Type = VlanIndex
_ArpproxyFlushEdgeRouterVid_Object = MibScalar
arpproxyFlushEdgeRouterVid = _ArpproxyFlushEdgeRouterVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 4),
    _ArpproxyFlushEdgeRouterVid_Type()
)
arpproxyFlushEdgeRouterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushEdgeRouterVid.setStatus("current")
_ArpproxyFlushInterfaceIp_Type = IpAddress
_ArpproxyFlushInterfaceIp_Object = MibScalar
arpproxyFlushInterfaceIp = _ArpproxyFlushInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 5),
    _ArpproxyFlushInterfaceIp_Type()
)
arpproxyFlushInterfaceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceIp.setStatus("current")
_ArpproxyFlushInterfaceMask_Type = Integer32
_ArpproxyFlushInterfaceMask_Object = MibScalar
arpproxyFlushInterfaceMask = _ArpproxyFlushInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 6),
    _ArpproxyFlushInterfaceMask_Type()
)
arpproxyFlushInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceMask.setStatus("current")
_ArpproxyFlushInterfaceVid_Type = VlanIndex
_ArpproxyFlushInterfaceVid_Object = MibScalar
arpproxyFlushInterfaceVid = _ArpproxyFlushInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 12, 8, 2, 7),
    _ArpproxyFlushInterfaceVid_Type()
)
arpproxyFlushInterfaceVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpproxyFlushInterfaceVid.setStatus("current")
_VoipPort_ObjectIdentity = ObjectIdentity
voipPort = _VoipPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13)
)
_VoipSipLineConfTable_Object = MibTable
voipSipLineConfTable = _VoipSipLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 1)
)
if mibBuilder.loadTexts:
    voipSipLineConfTable.setStatus("current")
_VoipSipLineConfEntry_Object = MibTableRow
voipSipLineConfEntry = _VoipSipLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 1, 1)
)
voipSipLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipSipLineConfEntry.setStatus("current")
_VoipSipLineConfSipProfile_Type = OctetString
_VoipSipLineConfSipProfile_Object = MibTableColumn
voipSipLineConfSipProfile = _VoipSipLineConfSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 1, 1, 1),
    _VoipSipLineConfSipProfile_Type()
)
voipSipLineConfSipProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfSipProfile.setStatus("current")
_VoipSipLineConfSipCallSvcProfile_Type = OctetString
_VoipSipLineConfSipCallSvcProfile_Object = MibTableColumn
voipSipLineConfSipCallSvcProfile = _VoipSipLineConfSipCallSvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 1, 1, 2),
    _VoipSipLineConfSipCallSvcProfile_Type()
)
voipSipLineConfSipCallSvcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfSipCallSvcProfile.setStatus("current")
_VoipSipLineConfDspProfile_Type = OctetString
_VoipSipLineConfDspProfile_Object = MibTableColumn
voipSipLineConfDspProfile = _VoipSipLineConfDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 1, 1, 3),
    _VoipSipLineConfDspProfile_Type()
)
voipSipLineConfDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipSipLineConfDspProfile.setStatus("current")
_PortOperations_ObjectIdentity = ObjectIdentity
portOperations = _PortOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 2)
)
_VoipPortTarget_Type = OctetString
_VoipPortTarget_Object = MibScalar
voipPortTarget = _VoipPortTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 2, 1),
    _VoipPortTarget_Type()
)
voipPortTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTarget.setStatus("current")
_VoipPortOps_Type = Integer32
_VoipPortOps_Object = MibScalar
voipPortOps = _VoipPortOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 2, 2),
    _VoipPortOps_Type()
)
voipPortOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortOps.setStatus("current")
_VoipPortEnableStatus_Type = OctetString
_VoipPortEnableStatus_Object = MibScalar
voipPortEnableStatus = _VoipPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 2, 3),
    _VoipPortEnableStatus_Type()
)
voipPortEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortEnableStatus.setStatus("current")
_VoipPortTelTable_Object = MibTable
voipPortTelTable = _VoipPortTelTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 3)
)
if mibBuilder.loadTexts:
    voipPortTelTable.setStatus("current")
_VoipPortTelEntry_Object = MibTableRow
voipPortTelEntry = _VoipPortTelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 3, 1)
)
voipPortTelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortTelEntry.setStatus("current")


class _VoipPortTel_Type(DisplayString):
    """Custom type voipPortTel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VoipPortTel_Type.__name__ = "DisplayString"
_VoipPortTel_Object = MibTableColumn
voipPortTel = _VoipPortTel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 3, 1, 1),
    _VoipPortTel_Type()
)
voipPortTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTel.setStatus("current")
_VoipPortGainTable_Object = MibTable
voipPortGainTable = _VoipPortGainTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 6)
)
if mibBuilder.loadTexts:
    voipPortGainTable.setStatus("current")
_VoipPortGainEntry_Object = MibTableRow
voipPortGainEntry = _VoipPortGainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 6, 1)
)
voipPortGainEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortGainEntry.setStatus("current")
_VoipPortTXGain_Type = Integer32
_VoipPortTXGain_Object = MibTableColumn
voipPortTXGain = _VoipPortTXGain_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 6, 1, 1),
    _VoipPortTXGain_Type()
)
voipPortTXGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortTXGain.setStatus("current")
_VoipPortRXGain_Type = Integer32
_VoipPortRXGain_Object = MibTableColumn
voipPortRXGain = _VoipPortRXGain_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 6, 1, 2),
    _VoipPortRXGain_Type()
)
voipPortRXGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipPortRXGain.setStatus("current")
_VoipH248LineConfTable_Object = MibTable
voipH248LineConfTable = _VoipH248LineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 7)
)
if mibBuilder.loadTexts:
    voipH248LineConfTable.setStatus("current")
_VoipH248LineConfEntry_Object = MibTableRow
voipH248LineConfEntry = _VoipH248LineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 7, 1)
)
voipH248LineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipH248LineConfEntry.setStatus("current")
_VoipH248LineConfMgName_Type = OctetString
_VoipH248LineConfMgName_Object = MibTableColumn
voipH248LineConfMgName = _VoipH248LineConfMgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 7, 1, 1),
    _VoipH248LineConfMgName_Type()
)
voipH248LineConfMgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248LineConfMgName.setStatus("current")
_VoipH248LineConfDspProfile_Type = OctetString
_VoipH248LineConfDspProfile_Object = MibTableColumn
voipH248LineConfDspProfile = _VoipH248LineConfDspProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 7, 1, 2),
    _VoipH248LineConfDspProfile_Type()
)
voipH248LineConfDspProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248LineConfDspProfile.setStatus("current")
_VoipH248LineConfVBDProfile_Type = OctetString
_VoipH248LineConfVBDProfile_Object = MibTableColumn
voipH248LineConfVBDProfile = _VoipH248LineConfVBDProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 7, 1, 3),
    _VoipH248LineConfVBDProfile_Type()
)
voipH248LineConfVBDProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248LineConfVBDProfile.setStatus("current")
_VoipPortH248TerminationTable_Object = MibTable
voipPortH248TerminationTable = _VoipPortH248TerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 8)
)
if mibBuilder.loadTexts:
    voipPortH248TerminationTable.setStatus("current")
_VoipPortH248TerminationEntry_Object = MibTableRow
voipPortH248TerminationEntry = _VoipPortH248TerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 8, 1)
)
voipPortH248TerminationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipPortH248TerminationEntry.setStatus("current")
_VoipPortH248TermName_Type = OctetString
_VoipPortH248TermName_Object = MibTableColumn
voipPortH248TermName = _VoipPortH248TermName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 13, 8, 1, 1),
    _VoipPortH248TermName_Type()
)
voipPortH248TermName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipPortH248TermName.setStatus("current")
_Dtpvc_ObjectIdentity = ObjectIdentity
dtpvc = _Dtpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14)
)
_DtpvcTable_Object = MibTable
dtpvcTable = _DtpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1)
)
if mibBuilder.loadTexts:
    dtpvcTable.setStatus("current")
_DtpvcEntry_Object = MibTableRow
dtpvcEntry = _DtpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1)
)
dtpvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "dtpvcVpi"),
    (0, "E5-111-MIB", "dtpvcVci"),
    (0, "E5-111-MIB", "dtpvcSvid"),
)
if mibBuilder.loadTexts:
    dtpvcEntry.setStatus("current")


class _DtpvcVpi_Type(Integer32):
    """Custom type dtpvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtpvcVpi_Type.__name__ = "Integer32"
_DtpvcVpi_Object = MibTableColumn
dtpvcVpi = _DtpvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 1),
    _DtpvcVpi_Type()
)
dtpvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVpi.setStatus("current")


class _DtpvcVci_Type(Integer32):
    """Custom type dtpvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtpvcVci_Type.__name__ = "Integer32"
_DtpvcVci_Object = MibTableColumn
dtpvcVci = _DtpvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 2),
    _DtpvcVci_Type()
)
dtpvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcVci.setStatus("current")
_DtpvcSvid_Type = VlanIndex
_DtpvcSvid_Object = MibTableColumn
dtpvcSvid = _DtpvcSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 3),
    _DtpvcSvid_Type()
)
dtpvcSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcSvid.setStatus("current")


class _DtpvcSpriority_Type(Integer32):
    """Custom type dtpvcSpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcSpriority_Type.__name__ = "Integer32"
_DtpvcSpriority_Object = MibTableColumn
dtpvcSpriority = _DtpvcSpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 4),
    _DtpvcSpriority_Type()
)
dtpvcSpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcSpriority.setStatus("current")
_DtpvcCvid_Type = VlanIndex
_DtpvcCvid_Object = MibTableColumn
dtpvcCvid = _DtpvcCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 5),
    _DtpvcCvid_Type()
)
dtpvcCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCvid.setStatus("current")


class _DtpvcCpriority_Type(Integer32):
    """Custom type dtpvcCpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcCpriority_Type.__name__ = "Integer32"
_DtpvcCpriority_Object = MibTableColumn
dtpvcCpriority = _DtpvcCpriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 6),
    _DtpvcCpriority_Type()
)
dtpvcCpriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcCpriority.setStatus("current")


class _DtpvcDSProfile_Type(DisplayString):
    """Custom type dtpvcDSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcDSProfile_Type.__name__ = "DisplayString"
_DtpvcDSProfile_Object = MibTableColumn
dtpvcDSProfile = _DtpvcDSProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 7),
    _DtpvcDSProfile_Type()
)
dtpvcDSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcDSProfile.setStatus("current")


class _DtpvcUSProfile_Type(DisplayString):
    """Custom type dtpvcUSProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcUSProfile_Type.__name__ = "DisplayString"
_DtpvcUSProfile_Object = MibTableColumn
dtpvcUSProfile = _DtpvcUSProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 8),
    _DtpvcUSProfile_Type()
)
dtpvcUSProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcUSProfile.setStatus("current")
_DtpvcRowStatus_Type = RowStatus
_DtpvcRowStatus_Object = MibTableColumn
dtpvcRowStatus = _DtpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 9),
    _DtpvcRowStatus_Type()
)
dtpvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcRowStatus.setStatus("current")


class _DtpvcSuperChannel_Type(Integer32):
    """Custom type dtpvcSuperChannel based on Integer32"""
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


_DtpvcSuperChannel_Type.__name__ = "Integer32"
_DtpvcSuperChannel_Object = MibTableColumn
dtpvcSuperChannel = _DtpvcSuperChannel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 10),
    _DtpvcSuperChannel_Type()
)
dtpvcSuperChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcSuperChannel.setStatus("current")
_DtpvcAcName_Type = DisplayString
_DtpvcAcName_Object = MibTableColumn
dtpvcAcName = _DtpvcAcName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 11),
    _DtpvcAcName_Type()
)
dtpvcAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcAcName.setStatus("current")
_DtpvcServiceName_Type = DisplayString
_DtpvcServiceName_Object = MibTableColumn
dtpvcServiceName = _DtpvcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 12),
    _DtpvcServiceName_Type()
)
dtpvcServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcServiceName.setStatus("current")
_DtpvcHelloTime_Type = Integer32
_DtpvcHelloTime_Object = MibTableColumn
dtpvcHelloTime = _DtpvcHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 1, 1, 13),
    _DtpvcHelloTime_Type()
)
dtpvcHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dtpvcHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    dtpvcHelloTime.setUnits("second")
_DtpvcStateTable_Object = MibTable
dtpvcStateTable = _DtpvcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2)
)
if mibBuilder.loadTexts:
    dtpvcStateTable.setStatus("current")
_DtpvcStateEntry_Object = MibTableRow
dtpvcStateEntry = _DtpvcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1)
)
dtpvcStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "dtpvcStateVpi"),
    (0, "E5-111-MIB", "dtpvcStateVci"),
    (0, "E5-111-MIB", "dtpvcStateSvid"),
)
if mibBuilder.loadTexts:
    dtpvcStateEntry.setStatus("current")


class _DtpvcStateVpi_Type(Integer32):
    """Custom type dtpvcStateVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtpvcStateVpi_Type.__name__ = "Integer32"
_DtpvcStateVpi_Object = MibTableColumn
dtpvcStateVpi = _DtpvcStateVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 1),
    _DtpvcStateVpi_Type()
)
dtpvcStateVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateVpi.setStatus("current")


class _DtpvcStateVci_Type(Integer32):
    """Custom type dtpvcStateVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtpvcStateVci_Type.__name__ = "Integer32"
_DtpvcStateVci_Object = MibTableColumn
dtpvcStateVci = _DtpvcStateVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 2),
    _DtpvcStateVci_Type()
)
dtpvcStateVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateVci.setStatus("current")
_DtpvcStateSvid_Type = VlanIndex
_DtpvcStateSvid_Object = MibTableColumn
dtpvcStateSvid = _DtpvcStateSvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 3),
    _DtpvcStateSvid_Type()
)
dtpvcStateSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateSvid.setStatus("current")


class _DtpvcStateSPriority_Type(Integer32):
    """Custom type dtpvcStateSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcStateSPriority_Type.__name__ = "Integer32"
_DtpvcStateSPriority_Object = MibTableColumn
dtpvcStateSPriority = _DtpvcStateSPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 4),
    _DtpvcStateSPriority_Type()
)
dtpvcStateSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateSPriority.setStatus("current")
_DtpvcStateCvid_Type = VlanIndex
_DtpvcStateCvid_Object = MibTableColumn
dtpvcStateCvid = _DtpvcStateCvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 5),
    _DtpvcStateCvid_Type()
)
dtpvcStateCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateCvid.setStatus("current")


class _DtpvcStateCPriority_Type(Integer32):
    """Custom type dtpvcStateCPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DtpvcStateCPriority_Type.__name__ = "Integer32"
_DtpvcStateCPriority_Object = MibTableColumn
dtpvcStateCPriority = _DtpvcStateCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 6),
    _DtpvcStateCPriority_Type()
)
dtpvcStateCPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateCPriority.setStatus("current")


class _DtpvcStateChannelType_Type(DisplayString):
    """Custom type dtpvcStateChannelType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcStateChannelType_Type.__name__ = "DisplayString"
_DtpvcStateChannelType_Object = MibTableColumn
dtpvcStateChannelType = _DtpvcStateChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 8),
    _DtpvcStateChannelType_Type()
)
dtpvcStateChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateChannelType.setStatus("current")


class _DtpvcStateEncap_Type(DisplayString):
    """Custom type dtpvcStateEncap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DtpvcStateEncap_Type.__name__ = "DisplayString"
_DtpvcStateEncap_Object = MibTableColumn
dtpvcStateEncap = _DtpvcStateEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 14, 2, 1, 9),
    _DtpvcStateEncap_Type()
)
dtpvcStateEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpvcStateEncap.setStatus("current")
_SnrMgn_ObjectIdentity = ObjectIdentity
snrMgn = _SnrMgn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15)
)
_SnrMgnTable_Object = MibTable
snrMgnTable = _SnrMgnTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1)
)
if mibBuilder.loadTexts:
    snrMgnTable.setStatus("current")
_SnrMgnEntry_Object = MibTableRow
snrMgnEntry = _SnrMgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1)
)
snrMgnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snrMgnEntry.setStatus("current")


class _SnrMgnMode_Type(Integer32):
    """Custom type snrMgnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("profile", 0))
    )


_SnrMgnMode_Type.__name__ = "Integer32"
_SnrMgnMode_Object = MibTableColumn
snrMgnMode = _SnrMgnMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 1),
    _SnrMgnMode_Type()
)
snrMgnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnMode.setStatus("current")


class _SnrMgnUcTarget_Type(Integer32):
    """Custom type snrMgnUcTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcTarget_Type.__name__ = "Integer32"
_SnrMgnUcTarget_Object = MibTableColumn
snrMgnUcTarget = _SnrMgnUcTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 2),
    _SnrMgnUcTarget_Type()
)
snrMgnUcTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcTarget.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcTarget.setUnits("tenth dB")


class _SnrMgnUcMax_Type(Integer32):
    """Custom type snrMgnUcMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcMax_Type.__name__ = "Integer32"
_SnrMgnUcMax_Object = MibTableColumn
snrMgnUcMax = _SnrMgnUcMax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 3),
    _SnrMgnUcMax_Type()
)
snrMgnUcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcMax.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcMax.setUnits("tenth dB")


class _SnrMgnUcMin_Type(Integer32):
    """Custom type snrMgnUcMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcMin_Type.__name__ = "Integer32"
_SnrMgnUcMin_Object = MibTableColumn
snrMgnUcMin = _SnrMgnUcMin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 4),
    _SnrMgnUcMin_Type()
)
snrMgnUcMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcMin.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcMin.setUnits("tenth dB")


class _SnrMgnUcDownshift_Type(Integer32):
    """Custom type snrMgnUcDownshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcDownshift_Type.__name__ = "Integer32"
_SnrMgnUcDownshift_Object = MibTableColumn
snrMgnUcDownshift = _SnrMgnUcDownshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 5),
    _SnrMgnUcDownshift_Type()
)
snrMgnUcDownshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcDownshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcDownshift.setUnits("tenth dB")


class _SnrMgnUcUpshift_Type(Integer32):
    """Custom type snrMgnUcUpshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUcUpshift_Type.__name__ = "Integer32"
_SnrMgnUcUpshift_Object = MibTableColumn
snrMgnUcUpshift = _SnrMgnUcUpshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 6),
    _SnrMgnUcUpshift_Type()
)
snrMgnUcUpshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUcUpshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUcUpshift.setUnits("tenth dB")


class _SnrMgnUrTarget_Type(Integer32):
    """Custom type snrMgnUrTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrTarget_Type.__name__ = "Integer32"
_SnrMgnUrTarget_Object = MibTableColumn
snrMgnUrTarget = _SnrMgnUrTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 7),
    _SnrMgnUrTarget_Type()
)
snrMgnUrTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrTarget.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrTarget.setUnits("tenth dB")


class _SnrMgnUrMax_Type(Integer32):
    """Custom type snrMgnUrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrMax_Type.__name__ = "Integer32"
_SnrMgnUrMax_Object = MibTableColumn
snrMgnUrMax = _SnrMgnUrMax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 8),
    _SnrMgnUrMax_Type()
)
snrMgnUrMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrMax.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrMax.setUnits("tenth dB")


class _SnrMgnUrMin_Type(Integer32):
    """Custom type snrMgnUrMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrMin_Type.__name__ = "Integer32"
_SnrMgnUrMin_Object = MibTableColumn
snrMgnUrMin = _SnrMgnUrMin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 9),
    _SnrMgnUrMin_Type()
)
snrMgnUrMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrMin.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrMin.setUnits("tenth dB")


class _SnrMgnUrDownshift_Type(Integer32):
    """Custom type snrMgnUrDownshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrDownshift_Type.__name__ = "Integer32"
_SnrMgnUrDownshift_Object = MibTableColumn
snrMgnUrDownshift = _SnrMgnUrDownshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 10),
    _SnrMgnUrDownshift_Type()
)
snrMgnUrDownshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrDownshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrDownshift.setUnits("tenth dB")


class _SnrMgnUrUpshift_Type(Integer32):
    """Custom type snrMgnUrUpshift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_SnrMgnUrUpshift_Type.__name__ = "Integer32"
_SnrMgnUrUpshift_Object = MibTableColumn
snrMgnUrUpshift = _SnrMgnUrUpshift_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 15, 1, 1, 11),
    _SnrMgnUrUpshift_Type()
)
snrMgnUrUpshift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrMgnUrUpshift.setStatus("current")
if mibBuilder.loadTexts:
    snrMgnUrUpshift.setUnits("tenth dB")
_DslRate_ObjectIdentity = ObjectIdentity
dslRate = _DslRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16)
)
_DslRateTable_Object = MibTable
dslRateTable = _DslRateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1)
)
if mibBuilder.loadTexts:
    dslRateTable.setStatus("current")
_DslRateEntry_Object = MibTableRow
dslRateEntry = _DslRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1)
)
dslRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dslRateEntry.setStatus("current")


class _DslRateMode_Type(Integer32):
    """Custom type dslRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("profile", 0))
    )


_DslRateMode_Type.__name__ = "Integer32"
_DslRateMode_Object = MibTableColumn
dslRateMode = _DslRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 1),
    _DslRateMode_Type()
)
dslRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateMode.setStatus("current")


class _DslRateLatencyMode_Type(Integer32):
    """Custom type dslRateLatencyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("interleave", 1))
    )


_DslRateLatencyMode_Type.__name__ = "Integer32"
_DslRateLatencyMode_Object = MibTableColumn
dslRateLatencyMode = _DslRateLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 2),
    _DslRateLatencyMode_Type()
)
dslRateLatencyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslRateLatencyMode.setStatus("current")


class _DslRateXtucMaxInterleaveDelay_Type(Integer32):
    """Custom type dslRateXtucMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DslRateXtucMaxInterleaveDelay_Type.__name__ = "Integer32"
_DslRateXtucMaxInterleaveDelay_Object = MibTableColumn
dslRateXtucMaxInterleaveDelay = _DslRateXtucMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 3),
    _DslRateXtucMaxInterleaveDelay_Type()
)
dslRateXtucMaxInterleaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMaxInterleaveDelay.setUnits("milli-seconds")
_DslRateXtucMaxTxRate_Type = Unsigned32
_DslRateXtucMaxTxRate_Object = MibTableColumn
dslRateXtucMaxTxRate = _DslRateXtucMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 4),
    _DslRateXtucMaxTxRate_Type()
)
dslRateXtucMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMaxTxRate.setUnits("kbps")
_DslRateXtucMinTxRate_Type = Unsigned32
_DslRateXtucMinTxRate_Object = MibTableColumn
dslRateXtucMinTxRate = _DslRateXtucMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 5),
    _DslRateXtucMinTxRate_Type()
)
dslRateXtucMinTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXtucMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXtucMinTxRate.setUnits("kbps")


class _DslRateXturMaxInterleaveDelay_Type(Integer32):
    """Custom type dslRateXturMaxInterleaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DslRateXturMaxInterleaveDelay_Type.__name__ = "Integer32"
_DslRateXturMaxInterleaveDelay_Object = MibTableColumn
dslRateXturMaxInterleaveDelay = _DslRateXturMaxInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 6),
    _DslRateXturMaxInterleaveDelay_Type()
)
dslRateXturMaxInterleaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMaxInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMaxInterleaveDelay.setUnits("milli-seconds")
_DslRateXturMaxTxRate_Type = Unsigned32
_DslRateXturMaxTxRate_Object = MibTableColumn
dslRateXturMaxTxRate = _DslRateXturMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 7),
    _DslRateXturMaxTxRate_Type()
)
dslRateXturMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMaxTxRate.setUnits("kbps")
_DslRateXturMinTxRate_Type = Unsigned32
_DslRateXturMinTxRate_Object = MibTableColumn
dslRateXturMinTxRate = _DslRateXturMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 16, 1, 1, 8),
    _DslRateXturMinTxRate_Type()
)
dslRateXturMinTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslRateXturMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    dslRateXturMinTxRate.setUnits("kbps")
_Gbond_ObjectIdentity = ObjectIdentity
gbond = _Gbond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51)
)
_GbondGroupTable_Object = MibTable
gbondGroupTable = _GbondGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1)
)
if mibBuilder.loadTexts:
    gbondGroupTable.setStatus("current")
_GbondGroupEntry_Object = MibTableRow
gbondGroupEntry = _GbondGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1)
)
gbondGroupEntry.setIndexNames(
    (0, "E5-111-MIB", "gbondGroupName"),
)
if mibBuilder.loadTexts:
    gbondGroupEntry.setStatus("current")


class _GbondGroupName_Type(OctetString):
    """Custom type gbondGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GbondGroupName_Type.__name__ = "OctetString"
_GbondGroupName_Object = MibTableColumn
gbondGroupName = _GbondGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1, 1),
    _GbondGroupName_Type()
)
gbondGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupName.setStatus("current")
_GbondGroupPorts_Type = OctetString
_GbondGroupPorts_Object = MibTableColumn
gbondGroupPorts = _GbondGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1, 2),
    _GbondGroupPorts_Type()
)
gbondGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupPorts.setStatus("current")
_GbondGroupUpRate_Type = Unsigned32
_GbondGroupUpRate_Object = MibTableColumn
gbondGroupUpRate = _GbondGroupUpRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1, 4),
    _GbondGroupUpRate_Type()
)
gbondGroupUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupUpRate.setStatus("current")
_GbondGroupDownRate_Type = Unsigned32
_GbondGroupDownRate_Object = MibTableColumn
gbondGroupDownRate = _GbondGroupDownRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1, 5),
    _GbondGroupDownRate_Type()
)
gbondGroupDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbondGroupDownRate.setStatus("current")
_GbondGroupRowStatus_Type = RowStatus
_GbondGroupRowStatus_Object = MibTableColumn
gbondGroupRowStatus = _GbondGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 8, 51, 1, 1, 6),
    _GbondGroupRowStatus_Type()
)
gbondGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gbondGroupRowStatus.setStatus("current")
_Profile_ObjectIdentity = ObjectIdentity
profile = _Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9)
)
_VoipProfile_ObjectIdentity = ObjectIdentity
voipProfile = _VoipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7)
)
_SipProfile_ObjectIdentity = ObjectIdentity
sipProfile = _SipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1)
)
_MaxNumOfSipProfiles_Type = Integer32
_MaxNumOfSipProfiles_Object = MibScalar
maxNumOfSipProfiles = _MaxNumOfSipProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 1),
    _MaxNumOfSipProfiles_Type()
)
maxNumOfSipProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipProfiles.setStatus("current")
_SipProfileTable_Object = MibTable
sipProfileTable = _SipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2)
)
if mibBuilder.loadTexts:
    sipProfileTable.setStatus("current")
_SipProfileEntry_Object = MibTableRow
sipProfileEntry = _SipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1)
)
sipProfileEntry.setIndexNames(
    (1, "E5-111-MIB", "sipProfileName"),
)
if mibBuilder.loadTexts:
    sipProfileEntry.setStatus("current")


class _SipProfileName_Type(DisplayString):
    """Custom type sipProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipProfileName_Type.__name__ = "DisplayString"
_SipProfileName_Object = MibTableColumn
sipProfileName = _SipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 1),
    _SipProfileName_Type()
)
sipProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProfileName.setStatus("current")
_SipProfileSipSvr_Type = OctetString
_SipProfileSipSvr_Object = MibTableColumn
sipProfileSipSvr = _SipProfileSipSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 2),
    _SipProfileSipSvr_Type()
)
sipProfileSipSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipSvr.setStatus("current")
_SipProfileRegSvr_Type = OctetString
_SipProfileRegSvr_Object = MibTableColumn
sipProfileRegSvr = _SipProfileRegSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 3),
    _SipProfileRegSvr_Type()
)
sipProfileRegSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvr.setStatus("current")
_SipProfileProxySvr_Type = OctetString
_SipProfileProxySvr_Object = MibTableColumn
sipProfileProxySvr = _SipProfileProxySvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 4),
    _SipProfileProxySvr_Type()
)
sipProfileProxySvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvr.setStatus("current")


class _SipProfileSipPort_Type(Integer32):
    """Custom type sipProfileSipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileSipPort_Type.__name__ = "Integer32"
_SipProfileSipPort_Object = MibTableColumn
sipProfileSipPort = _SipProfileSipPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 5),
    _SipProfileSipPort_Type()
)
sipProfileSipPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSipPort.setStatus("current")


class _SipProfileRegSvrPort_Type(Integer32):
    """Custom type sipProfileRegSvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileRegSvrPort_Type.__name__ = "Integer32"
_SipProfileRegSvrPort_Object = MibTableColumn
sipProfileRegSvrPort = _SipProfileRegSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 6),
    _SipProfileRegSvrPort_Type()
)
sipProfileRegSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegSvrPort.setStatus("current")


class _SipProfileProxySvrPort_Type(Integer32):
    """Custom type sipProfileProxySvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SipProfileProxySvrPort_Type.__name__ = "Integer32"
_SipProfileProxySvrPort_Object = MibTableColumn
sipProfileProxySvrPort = _SipProfileProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 7),
    _SipProfileProxySvrPort_Type()
)
sipProfileProxySvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileProxySvrPort.setStatus("current")


class _SipProfileUriType_Type(Integer32):
    """Custom type sipProfileUriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useSipUri", 1),
          ("useTelUri", 2))
    )


_SipProfileUriType_Type.__name__ = "Integer32"
_SipProfileUriType_Object = MibTableColumn
sipProfileUriType = _SipProfileUriType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 8),
    _SipProfileUriType_Type()
)
sipProfileUriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileUriType.setStatus("current")


class _SipProfilePbit_Type(Integer32):
    """Custom type sipProfilePbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SipProfilePbit_Type.__name__ = "Integer32"
_SipProfilePbit_Object = MibTableColumn
sipProfilePbit = _SipProfilePbit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 9),
    _SipProfilePbit_Type()
)
sipProfilePbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfilePbit.setStatus("current")


class _SipProfileDscp_Type(Integer32):
    """Custom type sipProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SipProfileDscp_Type.__name__ = "Integer32"
_SipProfileDscp_Object = MibTableColumn
sipProfileDscp = _SipProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 10),
    _SipProfileDscp_Type()
)
sipProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileDscp.setStatus("current")


class _SipProfileKeepAlive_Type(Integer32):
    """Custom type sipProfileKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SipProfileKeepAlive_Type.__name__ = "Integer32"
_SipProfileKeepAlive_Object = MibTableColumn
sipProfileKeepAlive = _SipProfileKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 11),
    _SipProfileKeepAlive_Type()
)
sipProfileKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileKeepAlive.setStatus("current")


class _SipProfileSe_Type(Integer32):
    """Custom type sipProfileSe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 65535),
    )


_SipProfileSe_Type.__name__ = "Integer32"
_SipProfileSe_Object = MibTableColumn
sipProfileSe = _SipProfileSe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 12),
    _SipProfileSe_Type()
)
sipProfileSe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileSe.setStatus("current")
if mibBuilder.loadTexts:
    sipProfileSe.setUnits("second")


class _SipProfilePrack_Type(Integer32):
    """Custom type sipProfilePrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SipProfilePrack_Type.__name__ = "Integer32"
_SipProfilePrack_Object = MibTableColumn
sipProfilePrack = _SipProfilePrack_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 13),
    _SipProfilePrack_Type()
)
sipProfilePrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfilePrack.setStatus("current")
_SipProfileRowStatus_Type = RowStatus
_SipProfileRowStatus_Object = MibTableColumn
sipProfileRowStatus = _SipProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 14),
    _SipProfileRowStatus_Type()
)
sipProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRowStatus.setStatus("current")


class _SipProfileRegExpire_Type(Integer32):
    """Custom type sipProfileRegExpire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2073600),
    )


_SipProfileRegExpire_Type.__name__ = "Integer32"
_SipProfileRegExpire_Object = MibTableColumn
sipProfileRegExpire = _SipProfileRegExpire_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 2, 1, 15),
    _SipProfileRegExpire_Type()
)
sipProfileRegExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRegExpire.setStatus("current")
if mibBuilder.loadTexts:
    sipProfileRegExpire.setUnits("second")
_MaxNumOfSipCallSvcProfiles_Type = Integer32
_MaxNumOfSipCallSvcProfiles_Object = MibScalar
maxNumOfSipCallSvcProfiles = _MaxNumOfSipCallSvcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 3),
    _MaxNumOfSipCallSvcProfiles_Type()
)
maxNumOfSipCallSvcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfSipCallSvcProfiles.setStatus("current")
_SipCallSvcProfileTable_Object = MibTable
sipCallSvcProfileTable = _SipCallSvcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4)
)
if mibBuilder.loadTexts:
    sipCallSvcProfileTable.setStatus("current")
_SipCallSvcProfileEntry_Object = MibTableRow
sipCallSvcProfileEntry = _SipCallSvcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1)
)
sipCallSvcProfileEntry.setIndexNames(
    (1, "E5-111-MIB", "sipCallSvcProfileName"),
)
if mibBuilder.loadTexts:
    sipCallSvcProfileEntry.setStatus("current")


class _SipCallSvcProfileName_Type(DisplayString):
    """Custom type sipCallSvcProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SipCallSvcProfileName_Type.__name__ = "DisplayString"
_SipCallSvcProfileName_Object = MibTableColumn
sipCallSvcProfileName = _SipCallSvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 1),
    _SipCallSvcProfileName_Type()
)
sipCallSvcProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCallSvcProfileName.setStatus("current")


class _SipCallSvcProfilePasswdOn_Type(Integer32):
    """Custom type sipCallSvcProfilePasswdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SipCallSvcProfilePasswdOn_Type.__name__ = "Integer32"
_SipCallSvcProfilePasswdOn_Object = MibTableColumn
sipCallSvcProfilePasswdOn = _SipCallSvcProfilePasswdOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 2),
    _SipCallSvcProfilePasswdOn_Type()
)
sipCallSvcProfilePasswdOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfilePasswdOn.setStatus("current")
_SipCallSvcProfilePasswd_Type = OctetString
_SipCallSvcProfilePasswd_Object = MibTableColumn
sipCallSvcProfilePasswd = _SipCallSvcProfilePasswd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 3),
    _SipCallSvcProfilePasswd_Type()
)
sipCallSvcProfilePasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfilePasswd.setStatus("current")


class _SipCallSvcProfileNumberPlanOn_Type(Integer32):
    """Custom type sipCallSvcProfileNumberPlanOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SipCallSvcProfileNumberPlanOn_Type.__name__ = "Integer32"
_SipCallSvcProfileNumberPlanOn_Object = MibTableColumn
sipCallSvcProfileNumberPlanOn = _SipCallSvcProfileNumberPlanOn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 4),
    _SipCallSvcProfileNumberPlanOn_Type()
)
sipCallSvcProfileNumberPlanOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanOn.setStatus("current")
_SipCallSvcProfileNumberPlanCc_Type = OctetString
_SipCallSvcProfileNumberPlanCc_Object = MibTableColumn
sipCallSvcProfileNumberPlanCc = _SipCallSvcProfileNumberPlanCc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 5),
    _SipCallSvcProfileNumberPlanCc_Type()
)
sipCallSvcProfileNumberPlanCc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanCc.setStatus("current")
_SipCallSvcProfileNumberPlanNdc_Type = OctetString
_SipCallSvcProfileNumberPlanNdc_Object = MibTableColumn
sipCallSvcProfileNumberPlanNdc = _SipCallSvcProfileNumberPlanNdc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 6),
    _SipCallSvcProfileNumberPlanNdc_Type()
)
sipCallSvcProfileNumberPlanNdc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanNdc.setStatus("current")
_SipCallSvcProfileNumberPlanTable_Type = OctetString
_SipCallSvcProfileNumberPlanTable_Object = MibTableColumn
sipCallSvcProfileNumberPlanTable = _SipCallSvcProfileNumberPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 7),
    _SipCallSvcProfileNumberPlanTable_Type()
)
sipCallSvcProfileNumberPlanTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileNumberPlanTable.setStatus("current")
_SipCallSvcProfileStateMask_Type = Integer32
_SipCallSvcProfileStateMask_Object = MibTableColumn
sipCallSvcProfileStateMask = _SipCallSvcProfileStateMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 8),
    _SipCallSvcProfileStateMask_Type()
)
sipCallSvcProfileStateMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileStateMask.setStatus("current")


class _SipCallSvcProfileDtmf_Type(Integer32):
    """Custom type sipCallSvcProfileDtmf based on Integer32"""
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
        *(("bypass", 1),
          ("rfc2833", 2),
          ("rfc2833like", 3),
          ("sipinfo", 4))
    )


_SipCallSvcProfileDtmf_Type.__name__ = "Integer32"
_SipCallSvcProfileDtmf_Object = MibTableColumn
sipCallSvcProfileDtmf = _SipCallSvcProfileDtmf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 9),
    _SipCallSvcProfileDtmf_Type()
)
sipCallSvcProfileDtmf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileDtmf.setStatus("current")


class _SipCallSvcProfileFax_Type(Integer32):
    """Custom type sipCallSvcProfileFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711", 1),
          ("t38", 2))
    )


_SipCallSvcProfileFax_Type.__name__ = "Integer32"
_SipCallSvcProfileFax_Object = MibTableColumn
sipCallSvcProfileFax = _SipCallSvcProfileFax_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 10),
    _SipCallSvcProfileFax_Type()
)
sipCallSvcProfileFax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFax.setStatus("current")
_SipCallSvcProfileRowStatus_Type = RowStatus
_SipCallSvcProfileRowStatus_Object = MibTableColumn
sipCallSvcProfileRowStatus = _SipCallSvcProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 11),
    _SipCallSvcProfileRowStatus_Type()
)
sipCallSvcProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileRowStatus.setStatus("current")


class _SipCallSvcProfileFlashType_Type(Integer32):
    """Custom type sipCallSvcProfileFlashType based on Integer32"""
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
        *(("bypass", 10),
          ("invite", 1),
          ("rfc2833", 2),
          ("rfc2833like", 3),
          ("sipinfo-1", 4),
          ("sipinfo-2", 5),
          ("sipinfo-3", 6),
          ("sipinfo-4", 7),
          ("sipinfo-5", 8),
          ("sipinfo-6", 9))
    )


_SipCallSvcProfileFlashType_Type.__name__ = "Integer32"
_SipCallSvcProfileFlashType_Object = MibTableColumn
sipCallSvcProfileFlashType = _SipCallSvcProfileFlashType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 12),
    _SipCallSvcProfileFlashType_Type()
)
sipCallSvcProfileFlashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlashType.setStatus("current")
_SipCallSvcProfileFlashInfo_Type = OctetString
_SipCallSvcProfileFlashInfo_Object = MibTableColumn
sipCallSvcProfileFlashInfo = _SipCallSvcProfileFlashInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 13),
    _SipCallSvcProfileFlashInfo_Type()
)
sipCallSvcProfileFlashInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileFlashInfo.setStatus("current")


class _SipCallSvcProfileSoftSwitchType_Type(Integer32):
    """Custom type sipCallSvcProfileSoftSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("metaswitch", 1),
          ("nortel", 2))
    )


_SipCallSvcProfileSoftSwitchType_Type.__name__ = "Integer32"
_SipCallSvcProfileSoftSwitchType_Object = MibTableColumn
sipCallSvcProfileSoftSwitchType = _SipCallSvcProfileSoftSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 1, 4, 1, 14),
    _SipCallSvcProfileSoftSwitchType_Type()
)
sipCallSvcProfileSoftSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCallSvcProfileSoftSwitchType.setStatus("current")
_MaxNumOfDspProfiles_Type = Integer32
_MaxNumOfDspProfiles_Object = MibScalar
maxNumOfDspProfiles = _MaxNumOfDspProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 2),
    _MaxNumOfDspProfiles_Type()
)
maxNumOfDspProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDspProfiles.setStatus("current")
_DspProfileTable_Object = MibTable
dspProfileTable = _DspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3)
)
if mibBuilder.loadTexts:
    dspProfileTable.setStatus("current")
_DspProfileEntry_Object = MibTableRow
dspProfileEntry = _DspProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1)
)
dspProfileEntry.setIndexNames(
    (1, "E5-111-MIB", "dspProfileName"),
)
if mibBuilder.loadTexts:
    dspProfileEntry.setStatus("current")


class _DspProfileName_Type(DisplayString):
    """Custom type dspProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DspProfileName_Type.__name__ = "DisplayString"
_DspProfileName_Object = MibTableColumn
dspProfileName = _DspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 1),
    _DspProfileName_Type()
)
dspProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspProfileName.setStatus("current")
_DspProfileCodec_Type = OctetString
_DspProfileCodec_Object = MibTableColumn
dspProfileCodec = _DspProfileCodec_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 2),
    _DspProfileCodec_Type()
)
dspProfileCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileCodec.setStatus("current")


class _DspProfilePlayBufferMinDelay_Type(Integer32):
    """Custom type dspProfilePlayBufferMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DspProfilePlayBufferMinDelay_Type.__name__ = "Integer32"
_DspProfilePlayBufferMinDelay_Object = MibTableColumn
dspProfilePlayBufferMinDelay = _DspProfilePlayBufferMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 3),
    _DspProfilePlayBufferMinDelay_Type()
)
dspProfilePlayBufferMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMinDelay.setUnits("millisecond")


class _DspProfilePlayBufferMaxDelay_Type(Integer32):
    """Custom type dspProfilePlayBufferMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_DspProfilePlayBufferMaxDelay_Type.__name__ = "Integer32"
_DspProfilePlayBufferMaxDelay_Object = MibTableColumn
dspProfilePlayBufferMaxDelay = _DspProfilePlayBufferMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 4),
    _DspProfilePlayBufferMaxDelay_Type()
)
dspProfilePlayBufferMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    dspProfilePlayBufferMaxDelay.setUnits("millisecond")


class _DspProfileEchoTail_Type(Integer32):
    """Custom type dspProfileEchoTail based on Integer32"""
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
        *(("echotail128", 4),
          ("echotail16", 2),
          ("echotail32", 3),
          ("echotail8", 1))
    )


_DspProfileEchoTail_Type.__name__ = "Integer32"
_DspProfileEchoTail_Object = MibTableColumn
dspProfileEchoTail = _DspProfileEchoTail_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 5),
    _DspProfileEchoTail_Type()
)
dspProfileEchoTail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileEchoTail.setStatus("current")
_DspProfileRowStatus_Type = RowStatus
_DspProfileRowStatus_Object = MibTableColumn
dspProfileRowStatus = _DspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 6),
    _DspProfileRowStatus_Type()
)
dspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileRowStatus.setStatus("current")


class _DspProfileG711Vpi_Type(Integer32):
    """Custom type dspProfileG711Vpi based on Integer32"""
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
        *(("g711x10ms", 1),
          ("g711x20ms", 2),
          ("g711x30ms", 3),
          ("g711x40ms", 4))
    )


_DspProfileG711Vpi_Type.__name__ = "Integer32"
_DspProfileG711Vpi_Object = MibTableColumn
dspProfileG711Vpi = _DspProfileG711Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 7),
    _DspProfileG711Vpi_Type()
)
dspProfileG711Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG711Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG711Vpi.setUnits("millisecond")


class _DspProfileG723Vpi_Type(Integer32):
    """Custom type dspProfileG723Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g723x30ms", 1),
          ("g723x60ms", 2))
    )


_DspProfileG723Vpi_Type.__name__ = "Integer32"
_DspProfileG723Vpi_Object = MibTableColumn
dspProfileG723Vpi = _DspProfileG723Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 8),
    _DspProfileG723Vpi_Type()
)
dspProfileG723Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG723Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG723Vpi.setUnits("millisecond")


class _DspProfileG726Vpi_Type(Integer32):
    """Custom type dspProfileG726Vpi based on Integer32"""
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
        *(("g726x10ms", 1),
          ("g726x20ms", 2),
          ("g726x30ms", 3),
          ("g726x40ms", 4))
    )


_DspProfileG726Vpi_Type.__name__ = "Integer32"
_DspProfileG726Vpi_Object = MibTableColumn
dspProfileG726Vpi = _DspProfileG726Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 9),
    _DspProfileG726Vpi_Type()
)
dspProfileG726Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG726Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG726Vpi.setUnits("millisecond")


class _DspProfileG729Vpi_Type(Integer32):
    """Custom type dspProfileG729Vpi based on Integer32"""
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
        *(("g729x10ms", 1),
          ("g729x20ms", 2),
          ("g729x30ms", 3),
          ("g729x40ms", 4),
          ("g729x50ms", 5),
          ("g729x60ms", 6))
    )


_DspProfileG729Vpi_Type.__name__ = "Integer32"
_DspProfileG729Vpi_Object = MibTableColumn
dspProfileG729Vpi = _DspProfileG729Vpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 3, 1, 10),
    _DspProfileG729Vpi_Type()
)
dspProfileG729Vpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspProfileG729Vpi.setStatus("current")
if mibBuilder.loadTexts:
    dspProfileG729Vpi.setUnits("millisecond")
_H248Profile_ObjectIdentity = ObjectIdentity
h248Profile = _H248Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4)
)
_MaxNumOfH248Profiles_Type = Integer32
_MaxNumOfH248Profiles_Object = MibScalar
maxNumOfH248Profiles = _MaxNumOfH248Profiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 1),
    _MaxNumOfH248Profiles_Type()
)
maxNumOfH248Profiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfH248Profiles.setStatus("current")
_H248ProfileTable_Object = MibTable
h248ProfileTable = _H248ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2)
)
if mibBuilder.loadTexts:
    h248ProfileTable.setStatus("current")
_H248ProfileEntry_Object = MibTableRow
h248ProfileEntry = _H248ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1)
)
h248ProfileEntry.setIndexNames(
    (1, "E5-111-MIB", "h248ProfileName"),
)
if mibBuilder.loadTexts:
    h248ProfileEntry.setStatus("current")


class _H248ProfileName_Type(DisplayString):
    """Custom type h248ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfileName_Type.__name__ = "DisplayString"
_H248ProfileName_Object = MibTableColumn
h248ProfileName = _H248ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 1),
    _H248ProfileName_Type()
)
h248ProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h248ProfileName.setStatus("current")
_H248ProfileMgcSvr_Type = OctetString
_H248ProfileMgcSvr_Object = MibTableColumn
h248ProfileMgcSvr = _H248ProfileMgcSvr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 2),
    _H248ProfileMgcSvr_Type()
)
h248ProfileMgcSvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgcSvr.setStatus("current")


class _H248ProfileMgcPort_Type(Integer32):
    """Custom type h248ProfileMgcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248ProfileMgcPort_Type.__name__ = "Integer32"
_H248ProfileMgcPort_Object = MibTableColumn
h248ProfileMgcPort = _H248ProfileMgcPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 3),
    _H248ProfileMgcPort_Type()
)
h248ProfileMgcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgcPort.setStatus("current")


class _H248ProfileMgc2On_Type(Integer32):
    """Custom type h248ProfileMgc2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H248ProfileMgc2On_Type.__name__ = "Integer32"
_H248ProfileMgc2On_Object = MibTableColumn
h248ProfileMgc2On = _H248ProfileMgc2On_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 4),
    _H248ProfileMgc2On_Type()
)
h248ProfileMgc2On.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2On.setStatus("current")
_H248ProfileMgc2Svr_Type = OctetString
_H248ProfileMgc2Svr_Object = MibTableColumn
h248ProfileMgc2Svr = _H248ProfileMgc2Svr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 5),
    _H248ProfileMgc2Svr_Type()
)
h248ProfileMgc2Svr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2Svr.setStatus("current")


class _H248ProfileMgc2Port_Type(Integer32):
    """Custom type h248ProfileMgc2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_H248ProfileMgc2Port_Type.__name__ = "Integer32"
_H248ProfileMgc2Port_Object = MibTableColumn
h248ProfileMgc2Port = _H248ProfileMgc2Port_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 6),
    _H248ProfileMgc2Port_Type()
)
h248ProfileMgc2Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileMgc2Port.setStatus("current")


class _H248ProfileTransport_Type(Integer32):
    """Custom type h248ProfileTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_H248ProfileTransport_Type.__name__ = "Integer32"
_H248ProfileTransport_Object = MibTableColumn
h248ProfileTransport = _H248ProfileTransport_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 7),
    _H248ProfileTransport_Type()
)
h248ProfileTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileTransport.setStatus("current")


class _H248ProfileEncode_Type(Integer32):
    """Custom type h248ProfileEncode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longtext", 1),
          ("shorttext", 2))
    )


_H248ProfileEncode_Type.__name__ = "Integer32"
_H248ProfileEncode_Object = MibTableColumn
h248ProfileEncode = _H248ProfileEncode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 8),
    _H248ProfileEncode_Type()
)
h248ProfileEncode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEncode.setStatus("current")


class _H248ProfilePbit_Type(Integer32):
    """Custom type h248ProfilePbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H248ProfilePbit_Type.__name__ = "Integer32"
_H248ProfilePbit_Object = MibTableColumn
h248ProfilePbit = _H248ProfilePbit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 9),
    _H248ProfilePbit_Type()
)
h248ProfilePbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePbit.setStatus("current")


class _H248ProfileDscp_Type(Integer32):
    """Custom type h248ProfileDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H248ProfileDscp_Type.__name__ = "Integer32"
_H248ProfileDscp_Object = MibTableColumn
h248ProfileDscp = _H248ProfileDscp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 10),
    _H248ProfileDscp_Type()
)
h248ProfileDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileDscp.setStatus("current")
_H248ProfileRowStatus_Type = RowStatus
_H248ProfileRowStatus_Object = MibTableColumn
h248ProfileRowStatus = _H248ProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 11),
    _H248ProfileRowStatus_Type()
)
h248ProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileRowStatus.setStatus("current")


class _H248ProfileVbd_Type(Integer32):
    """Custom type h248ProfileVbd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H248ProfileVbd_Type.__name__ = "Integer32"
_H248ProfileVbd_Object = MibTableColumn
h248ProfileVbd = _H248ProfileVbd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 12),
    _H248ProfileVbd_Type()
)
h248ProfileVbd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileVbd.setStatus("current")


class _H248ProfileEphemeralPrefix_Type(DisplayString):
    """Custom type h248ProfileEphemeralPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfileEphemeralPrefix_Type.__name__ = "DisplayString"
_H248ProfileEphemeralPrefix_Object = MibTableColumn
h248ProfileEphemeralPrefix = _H248ProfileEphemeralPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 14),
    _H248ProfileEphemeralPrefix_Type()
)
h248ProfileEphemeralPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralPrefix.setStatus("current")


class _H248ProfileSoftswitch_Type(Integer32):
    """Custom type h248ProfileSoftswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("metaswitch", 1),
          ("nortelCs1500", 2),
          ("nortelCs2000", 3))
    )


_H248ProfileSoftswitch_Type.__name__ = "Integer32"
_H248ProfileSoftswitch_Object = MibTableColumn
h248ProfileSoftswitch = _H248ProfileSoftswitch_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 15),
    _H248ProfileSoftswitch_Type()
)
h248ProfileSoftswitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileSoftswitch.setStatus("current")


class _H248ProfileForceVer_Type(Integer32):
    """Custom type h248ProfileForceVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H248ProfileForceVer_Type.__name__ = "Integer32"
_H248ProfileForceVer_Object = MibTableColumn
h248ProfileForceVer = _H248ProfileForceVer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 16),
    _H248ProfileForceVer_Type()
)
h248ProfileForceVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileForceVer.setStatus("current")


class _H248ProfileStartRTPPort_Type(Integer32):
    """Custom type h248ProfileStartRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 64000),
    )


_H248ProfileStartRTPPort_Type.__name__ = "Integer32"
_H248ProfileStartRTPPort_Object = MibTableColumn
h248ProfileStartRTPPort = _H248ProfileStartRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 17),
    _H248ProfileStartRTPPort_Type()
)
h248ProfileStartRTPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileStartRTPPort.setStatus("current")


class _H248ProfileEndRTPPort_Type(Integer32):
    """Custom type h248ProfileEndRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 65000),
    )


_H248ProfileEndRTPPort_Type.__name__ = "Integer32"
_H248ProfileEndRTPPort_Object = MibTableColumn
h248ProfileEndRTPPort = _H248ProfileEndRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 18),
    _H248ProfileEndRTPPort_Type()
)
h248ProfileEndRTPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEndRTPPort.setStatus("current")
_H248ProfileEphemeralStartNumber_Type = OctetString
_H248ProfileEphemeralStartNumber_Object = MibTableColumn
h248ProfileEphemeralStartNumber = _H248ProfileEphemeralStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 19),
    _H248ProfileEphemeralStartNumber_Type()
)
h248ProfileEphemeralStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralStartNumber.setStatus("current")


class _H248ProfileEphemeralSuffixLength_Type(Integer32):
    """Custom type h248ProfileEphemeralSuffixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H248ProfileEphemeralSuffixLength_Type.__name__ = "Integer32"
_H248ProfileEphemeralSuffixLength_Object = MibTableColumn
h248ProfileEphemeralSuffixLength = _H248ProfileEphemeralSuffixLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 20),
    _H248ProfileEphemeralSuffixLength_Type()
)
h248ProfileEphemeralSuffixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfileEphemeralSuffixLength.setStatus("current")


class _H248ProfilePhysicalPrefix_Type(DisplayString):
    """Custom type h248ProfilePhysicalPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H248ProfilePhysicalPrefix_Type.__name__ = "DisplayString"
_H248ProfilePhysicalPrefix_Object = MibTableColumn
h248ProfilePhysicalPrefix = _H248ProfilePhysicalPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 21),
    _H248ProfilePhysicalPrefix_Type()
)
h248ProfilePhysicalPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalPrefix.setStatus("current")
_H248ProfilePhysicalStartNumber_Type = OctetString
_H248ProfilePhysicalStartNumber_Object = MibTableColumn
h248ProfilePhysicalStartNumber = _H248ProfilePhysicalStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 22),
    _H248ProfilePhysicalStartNumber_Type()
)
h248ProfilePhysicalStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalStartNumber.setStatus("current")


class _H248ProfilePhysicalSuffixLength_Type(Integer32):
    """Custom type h248ProfilePhysicalSuffixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H248ProfilePhysicalSuffixLength_Type.__name__ = "Integer32"
_H248ProfilePhysicalSuffixLength_Object = MibTableColumn
h248ProfilePhysicalSuffixLength = _H248ProfilePhysicalSuffixLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 9, 7, 4, 2, 1, 23),
    _H248ProfilePhysicalSuffixLength_Type()
)
h248ProfilePhysicalSuffixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h248ProfilePhysicalSuffixLength.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10)
)
_Dscp_ObjectIdentity = ObjectIdentity
dscp = _Dscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10)
)
_DscpMappingTable_Object = MibTable
dscpMappingTable = _DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 1)
)
if mibBuilder.loadTexts:
    dscpMappingTable.setStatus("current")
_DscpMappingEntry_Object = MibTableRow
dscpMappingEntry = _DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 1, 1)
)
dscpMappingEntry.setIndexNames(
    (0, "E5-111-MIB", "dscpSrcCodePoint"),
)
if mibBuilder.loadTexts:
    dscpMappingEntry.setStatus("current")
_DscpSrcCodePoint_Type = Integer32
_DscpSrcCodePoint_Object = MibTableColumn
dscpSrcCodePoint = _DscpSrcCodePoint_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 1, 1, 1),
    _DscpSrcCodePoint_Type()
)
dscpSrcCodePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpSrcCodePoint.setStatus("current")


class _DscpMapPriority_Type(Integer32):
    """Custom type dscpMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DscpMapPriority_Type.__name__ = "Integer32"
_DscpMapPriority_Object = MibTableColumn
dscpMapPriority = _DscpMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 1, 1, 3),
    _DscpMapPriority_Type()
)
dscpMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpMapPriority.setStatus("current")
_DscpPortTable_Object = MibTable
dscpPortTable = _DscpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 2)
)
if mibBuilder.loadTexts:
    dscpPortTable.setStatus("current")
_DscpPortEntry_Object = MibTableRow
dscpPortEntry = _DscpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 2, 1)
)
dscpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dscpPortEntry.setStatus("current")


class _DscpStatusEnable_Type(Integer32):
    """Custom type dscpStatusEnable based on Integer32"""
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


_DscpStatusEnable_Type.__name__ = "Integer32"
_DscpStatusEnable_Object = MibTableColumn
dscpStatusEnable = _DscpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 10, 2, 1, 1),
    _DscpStatusEnable_Type()
)
dscpStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpStatusEnable.setStatus("current")
_VlanIsolation_ObjectIdentity = ObjectIdentity
vlanIsolation = _VlanIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 12)
)
_VlanIsolationTable_Object = MibTable
vlanIsolationTable = _VlanIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 12, 1)
)
if mibBuilder.loadTexts:
    vlanIsolationTable.setStatus("current")
_VlanIsolationEntry_Object = MibTableRow
vlanIsolationEntry = _VlanIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 12, 1, 1)
)
vlanIsolationEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanIsolationEntry.setStatus("current")
_VlanIsolationRowStatus_Type = RowStatus
_VlanIsolationRowStatus_Object = MibTableColumn
vlanIsolationRowStatus = _VlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 12, 1, 1, 1),
    _VlanIsolationRowStatus_Type()
)
vlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIsolationRowStatus.setStatus("current")
_EnetMtu_ObjectIdentity = ObjectIdentity
enetMtu = _EnetMtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 13)
)
_EnetMtuEntry_Type = Integer32
_EnetMtuEntry_Object = MibScalar
enetMtuEntry = _EnetMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 13, 1),
    _EnetMtuEntry_Type()
)
enetMtuEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetMtuEntry.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51)
)
_DhcpRelay82Table_Object = MibTable
dhcpRelay82Table = _DhcpRelay82Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2)
)
if mibBuilder.loadTexts:
    dhcpRelay82Table.setStatus("current")
_DhcpRelay82Entry_Object = MibTableRow
dhcpRelay82Entry = _DhcpRelay82Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1)
)
dhcpRelay82Entry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelay82Entry.setStatus("current")
_DhcpRelay82PrimaryServer_Type = IpAddress
_DhcpRelay82PrimaryServer_Object = MibTableColumn
dhcpRelay82PrimaryServer = _DhcpRelay82PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 1),
    _DhcpRelay82PrimaryServer_Type()
)
dhcpRelay82PrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82PrimaryServer.setStatus("current")
_DhcpRelay82SecondaryServer_Type = IpAddress
_DhcpRelay82SecondaryServer_Object = MibTableColumn
dhcpRelay82SecondaryServer = _DhcpRelay82SecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 2),
    _DhcpRelay82SecondaryServer_Type()
)
dhcpRelay82SecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82SecondaryServer.setStatus("current")


class _DhcpRelay82ActiveServer_Type(Integer32):
    """Custom type dhcpRelay82ActiveServer based on Integer32"""
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
        *(("fifth", 5),
          ("fourth", 4),
          ("primary", 1),
          ("secondary", 2),
          ("third", 3))
    )


_DhcpRelay82ActiveServer_Type.__name__ = "Integer32"
_DhcpRelay82ActiveServer_Object = MibTableColumn
dhcpRelay82ActiveServer = _DhcpRelay82ActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 3),
    _DhcpRelay82ActiveServer_Type()
)
dhcpRelay82ActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelay82ActiveServer.setStatus("current")


class _DhcpRelay82Enable_Type(Integer32):
    """Custom type dhcpRelay82Enable based on Integer32"""
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


_DhcpRelay82Enable_Type.__name__ = "Integer32"
_DhcpRelay82Enable_Object = MibTableColumn
dhcpRelay82Enable = _DhcpRelay82Enable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 4),
    _DhcpRelay82Enable_Type()
)
dhcpRelay82Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Enable.setStatus("current")


class _DhcpRelay82Info_Type(DisplayString):
    """Custom type dhcpRelay82Info based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_DhcpRelay82Info_Type.__name__ = "DisplayString"
_DhcpRelay82Info_Object = MibTableColumn
dhcpRelay82Info = _DhcpRelay82Info_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 5),
    _DhcpRelay82Info_Type()
)
dhcpRelay82Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Info.setStatus("current")


class _DhcpRelay82RelayMode_Type(Integer32):
    """Custom type dhcpRelay82RelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("auto", 1))
    )


_DhcpRelay82RelayMode_Type.__name__ = "Integer32"
_DhcpRelay82RelayMode_Object = MibTableColumn
dhcpRelay82RelayMode = _DhcpRelay82RelayMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 6),
    _DhcpRelay82RelayMode_Type()
)
dhcpRelay82RelayMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82RelayMode.setStatus("current")


class _DhcpRelay82Suboption2Enable_Type(Integer32):
    """Custom type dhcpRelay82Suboption2Enable based on Integer32"""
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


_DhcpRelay82Suboption2Enable_Type.__name__ = "Integer32"
_DhcpRelay82Suboption2Enable_Object = MibTableColumn
dhcpRelay82Suboption2Enable = _DhcpRelay82Suboption2Enable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 8),
    _DhcpRelay82Suboption2Enable_Type()
)
dhcpRelay82Suboption2Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Enable.setStatus("current")
_DhcpRelay82Suboption2Info_Type = DisplayString
_DhcpRelay82Suboption2Info_Object = MibTableColumn
dhcpRelay82Suboption2Info = _DhcpRelay82Suboption2Info_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 9),
    _DhcpRelay82Suboption2Info_Type()
)
dhcpRelay82Suboption2Info.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82Suboption2Info.setStatus("current")


class _DhcpRelay82EntryEnable_Type(Integer32):
    """Custom type dhcpRelay82EntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("auto", 1),
          ("disable", 3))
    )


_DhcpRelay82EntryEnable_Type.__name__ = "Integer32"
_DhcpRelay82EntryEnable_Object = MibTableColumn
dhcpRelay82EntryEnable = _DhcpRelay82EntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 10),
    _DhcpRelay82EntryEnable_Type()
)
dhcpRelay82EntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryEnable.setStatus("current")


class _DhcpRelay82EntryOptionMode_Type(Integer32):
    """Custom type dhcpRelay82EntryOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2))
    )


_DhcpRelay82EntryOptionMode_Type.__name__ = "Integer32"
_DhcpRelay82EntryOptionMode_Object = MibTableColumn
dhcpRelay82EntryOptionMode = _DhcpRelay82EntryOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 11),
    _DhcpRelay82EntryOptionMode_Type()
)
dhcpRelay82EntryOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelay82EntryOptionMode.setStatus("current")
_DhcpRelay82VlanIp_Type = IpAddress
_DhcpRelay82VlanIp_Object = MibTableColumn
dhcpRelay82VlanIp = _DhcpRelay82VlanIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 12),
    _DhcpRelay82VlanIp_Type()
)
dhcpRelay82VlanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanIp.setStatus("current")
_DhcpRelay82VlanMask_Type = Integer32
_DhcpRelay82VlanMask_Object = MibTableColumn
dhcpRelay82VlanMask = _DhcpRelay82VlanMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 13),
    _DhcpRelay82VlanMask_Type()
)
dhcpRelay82VlanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanMask.setStatus("current")
_DhcpRelay82VlanGateway_Type = IpAddress
_DhcpRelay82VlanGateway_Object = MibTableColumn
dhcpRelay82VlanGateway = _DhcpRelay82VlanGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 14),
    _DhcpRelay82VlanGateway_Type()
)
dhcpRelay82VlanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82VlanGateway.setStatus("current")
_DhcpRelay82ThirdServer_Type = IpAddress
_DhcpRelay82ThirdServer_Object = MibTableColumn
dhcpRelay82ThirdServer = _DhcpRelay82ThirdServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 15),
    _DhcpRelay82ThirdServer_Type()
)
dhcpRelay82ThirdServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82ThirdServer.setStatus("current")
_DhcpRelay82FourthServer_Type = IpAddress
_DhcpRelay82FourthServer_Object = MibTableColumn
dhcpRelay82FourthServer = _DhcpRelay82FourthServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 16),
    _DhcpRelay82FourthServer_Type()
)
dhcpRelay82FourthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82FourthServer.setStatus("current")
_DhcpRelay82FifthServer_Type = IpAddress
_DhcpRelay82FifthServer_Object = MibTableColumn
dhcpRelay82FifthServer = _DhcpRelay82FifthServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 17),
    _DhcpRelay82FifthServer_Type()
)
dhcpRelay82FifthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82FifthServer.setStatus("current")
_DhcpRelay82ServerVid_Type = Integer32
_DhcpRelay82ServerVid_Object = MibTableColumn
dhcpRelay82ServerVid = _DhcpRelay82ServerVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 2, 1, 18),
    _DhcpRelay82ServerVid_Type()
)
dhcpRelay82ServerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelay82ServerVid.setStatus("current")
_DhcpRelayTest_ObjectIdentity = ObjectIdentity
dhcpRelayTest = _DhcpRelayTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 8)
)
_DhcpRelayTestVid_Type = Integer32
_DhcpRelayTestVid_Object = MibScalar
dhcpRelayTestVid = _DhcpRelayTestVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 8, 1),
    _DhcpRelayTestVid_Type()
)
dhcpRelayTestVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestVid.setStatus("current")
_DhcpRelayTestIp_Type = IpAddress
_DhcpRelayTestIp_Object = MibScalar
dhcpRelayTestIp = _DhcpRelayTestIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 8, 2),
    _DhcpRelayTestIp_Type()
)
dhcpRelayTestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestIp.setStatus("current")
_DhcpRelayTestOps_Type = Integer32
_DhcpRelayTestOps_Object = MibScalar
dhcpRelayTestOps = _DhcpRelayTestOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 8, 3),
    _DhcpRelayTestOps_Type()
)
dhcpRelayTestOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTestOps.setStatus("current")
_DhcpRelayTestStatus_Type = DisplayString
_DhcpRelayTestStatus_Object = MibScalar
dhcpRelayTestStatus = _DhcpRelayTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 8, 4),
    _DhcpRelayTestStatus_Type()
)
dhcpRelayTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayTestStatus.setStatus("current")
_DhcpRelayArp_ObjectIdentity = ObjectIdentity
dhcpRelayArp = _DhcpRelayArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9)
)
_DhcpRelayArpShowTable_Object = MibTable
dhcpRelayArpShowTable = _DhcpRelayArpShowTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayArpShowTable.setStatus("current")
_DhcpRelayArpShowEntry_Object = MibTableRow
dhcpRelayArpShowEntry = _DhcpRelayArpShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 1, 1)
)
dhcpRelayArpShowEntry.setIndexNames(
    (0, "E5-111-MIB", "dhcpRelayArpShowVid"),
    (0, "E5-111-MIB", "dhcpRelayArpShowIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayArpShowEntry.setStatus("current")
_DhcpRelayArpShowVid_Type = Integer32
_DhcpRelayArpShowVid_Object = MibTableColumn
dhcpRelayArpShowVid = _DhcpRelayArpShowVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 1, 1, 1),
    _DhcpRelayArpShowVid_Type()
)
dhcpRelayArpShowVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowVid.setStatus("current")
_DhcpRelayArpShowIp_Type = IpAddress
_DhcpRelayArpShowIp_Object = MibTableColumn
dhcpRelayArpShowIp = _DhcpRelayArpShowIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 1, 1, 2),
    _DhcpRelayArpShowIp_Type()
)
dhcpRelayArpShowIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowIp.setStatus("current")
_DhcpRelayArpShowMac_Type = PhysAddress
_DhcpRelayArpShowMac_Object = MibTableColumn
dhcpRelayArpShowMac = _DhcpRelayArpShowMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 1, 1, 3),
    _DhcpRelayArpShowMac_Type()
)
dhcpRelayArpShowMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayArpShowMac.setStatus("current")
_DhcpRelayArpFlushOps_Type = Integer32
_DhcpRelayArpFlushOps_Object = MibScalar
dhcpRelayArpFlushOps = _DhcpRelayArpFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 51, 9, 2),
    _DhcpRelayArpFlushOps_Type()
)
dhcpRelayArpFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayArpFlushOps.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53)
)
_MacFilterPortTable_Object = MibTable
macFilterPortTable = _MacFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 1)
)
if mibBuilder.loadTexts:
    macFilterPortTable.setStatus("current")
_MacFilterPortEntry_Object = MibTableRow
macFilterPortEntry = _MacFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 1, 1)
)
macFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macFilterPortEntry.setStatus("current")


class _MacFilterPortEnable_Type(Integer32):
    """Custom type macFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 4),
          ("enableMacCount", 2),
          ("enableMacFilter", 1),
          ("enableMacFilterAndMacCount", 5))
    )


_MacFilterPortEnable_Type.__name__ = "Integer32"
_MacFilterPortEnable_Object = MibTableColumn
macFilterPortEnable = _MacFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 1, 1, 1),
    _MacFilterPortEnable_Type()
)
macFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortEnable.setStatus("current")


class _MacFilterPortMacCount_Type(Integer32):
    """Custom type macFilterPortMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterPortMacCount_Type.__name__ = "Integer32"
_MacFilterPortMacCount_Object = MibTableColumn
macFilterPortMacCount = _MacFilterPortMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 1, 1, 2),
    _MacFilterPortMacCount_Type()
)
macFilterPortMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortMacCount.setStatus("current")


class _MacFilterPortFilterMode_Type(Integer32):
    """Custom type macFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MacFilterPortFilterMode_Type.__name__ = "Integer32"
_MacFilterPortFilterMode_Object = MibTableColumn
macFilterPortFilterMode = _MacFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 1, 1, 3),
    _MacFilterPortFilterMode_Type()
)
macFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPortFilterMode.setStatus("current")
_MaxNumOfMacFiltersInSystem_Type = Integer32
_MaxNumOfMacFiltersInSystem_Object = MibScalar
maxNumOfMacFiltersInSystem = _MaxNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 2),
    _MaxNumOfMacFiltersInSystem_Type()
)
maxNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersInSystem.setStatus("current")
_MaxNumOfMacFiltersPerPort_Type = Integer32
_MaxNumOfMacFiltersPerPort_Object = MibScalar
maxNumOfMacFiltersPerPort = _MaxNumOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 3),
    _MaxNumOfMacFiltersPerPort_Type()
)
maxNumOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFiltersPerPort.setStatus("current")
_CurrNumOfMacFiltersInSystem_Type = Integer32
_CurrNumOfMacFiltersInSystem_Object = MibScalar
currNumOfMacFiltersInSystem = _CurrNumOfMacFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 4),
    _CurrNumOfMacFiltersInSystem_Type()
)
currNumOfMacFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currNumOfMacFiltersInSystem.setStatus("current")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 5)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("current")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 5, 1)
)
macFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "macFilterAddr"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("current")
_MacFilterAddr_Type = PhysAddress
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 5, 1, 1),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("current")
_MacFilterRowStatus_Type = RowStatus
_MacFilterRowStatus_Object = MibTableColumn
macFilterRowStatus = _MacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 5, 1, 2),
    _MacFilterRowStatus_Type()
)
macFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterRowStatus.setStatus("current")
_MacfilterBatchSet_ObjectIdentity = ObjectIdentity
macfilterBatchSet = _MacfilterBatchSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 6)
)
_MacfilterTarget_Type = OctetString
_MacfilterTarget_Object = MibScalar
macfilterTarget = _MacfilterTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 6, 1),
    _MacfilterTarget_Type()
)
macfilterTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterTarget.setStatus("current")
_MacfilterOps_Type = Integer32
_MacfilterOps_Object = MibScalar
macfilterOps = _MacfilterOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 6, 2),
    _MacfilterOps_Type()
)
macfilterOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macfilterOps.setStatus("current")


class _MacFilterMacCountForBatchSet_Type(Integer32):
    """Custom type macFilterMacCountForBatchSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MacFilterMacCountForBatchSet_Type.__name__ = "Integer32"
_MacFilterMacCountForBatchSet_Object = MibScalar
macFilterMacCountForBatchSet = _MacFilterMacCountForBatchSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 6, 3),
    _MacFilterMacCountForBatchSet_Type()
)
macFilterMacCountForBatchSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterMacCountForBatchSet.setStatus("current")
_OuiFilterTableOld_Object = MibTable
ouiFilterTableOld = _OuiFilterTableOld_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 7)
)
if mibBuilder.loadTexts:
    ouiFilterTableOld.setStatus("current")
_OuiFilterEntryOld_Object = MibTableRow
ouiFilterEntryOld = _OuiFilterEntryOld_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 7, 1)
)
ouiFilterEntryOld.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "ouiFilterAddrOld"),
)
if mibBuilder.loadTexts:
    ouiFilterEntryOld.setStatus("current")
_OuiFilterAddrOld_Type = OctetString
_OuiFilterAddrOld_Object = MibTableColumn
ouiFilterAddrOld = _OuiFilterAddrOld_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 7, 1, 1),
    _OuiFilterAddrOld_Type()
)
ouiFilterAddrOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddrOld.setStatus("current")
_OuiFilterRowStatusOld_Type = RowStatus
_OuiFilterRowStatusOld_Object = MibTableColumn
ouiFilterRowStatusOld = _OuiFilterRowStatusOld_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 7, 1, 2),
    _OuiFilterRowStatusOld_Type()
)
ouiFilterRowStatusOld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatusOld.setStatus("current")
_MaxNumOfOuiFiltersPerPort_Type = Integer32
_MaxNumOfOuiFiltersPerPort_Object = MibScalar
maxNumOfOuiFiltersPerPort = _MaxNumOfOuiFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 8),
    _MaxNumOfOuiFiltersPerPort_Type()
)
maxNumOfOuiFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerPort.setStatus("current")
_OuiFilterPortTable_Object = MibTable
ouiFilterPortTable = _OuiFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 9)
)
if mibBuilder.loadTexts:
    ouiFilterPortTable.setStatus("current")
_OuiFilterPortEntry_Object = MibTableRow
ouiFilterPortEntry = _OuiFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 9, 1)
)
ouiFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ouiFilterPortEntry.setStatus("current")


class _OuiFilterPortEnable_Type(Integer32):
    """Custom type ouiFilterPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enableOuiFilter", 1))
    )


_OuiFilterPortEnable_Type.__name__ = "Integer32"
_OuiFilterPortEnable_Object = MibTableColumn
ouiFilterPortEnable = _OuiFilterPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 9, 1, 1),
    _OuiFilterPortEnable_Type()
)
ouiFilterPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortEnable.setStatus("current")


class _OuiFilterPortFilterMode_Type(Integer32):
    """Custom type ouiFilterPortFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_OuiFilterPortFilterMode_Type.__name__ = "Integer32"
_OuiFilterPortFilterMode_Object = MibTableColumn
ouiFilterPortFilterMode = _OuiFilterPortFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 9, 1, 2),
    _OuiFilterPortFilterMode_Type()
)
ouiFilterPortFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterPortFilterMode.setStatus("current")
_MaxNumOfOuiFiltersInSystem_Type = Integer32
_MaxNumOfOuiFiltersInSystem_Object = MibScalar
maxNumOfOuiFiltersInSystem = _MaxNumOfOuiFiltersInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 10),
    _MaxNumOfOuiFiltersInSystem_Type()
)
maxNumOfOuiFiltersInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersInSystem.setStatus("current")
_MaxNumOfOuiFiltersPerVlan_Type = Integer32
_MaxNumOfOuiFiltersPerVlan_Object = MibScalar
maxNumOfOuiFiltersPerVlan = _MaxNumOfOuiFiltersPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 11),
    _MaxNumOfOuiFiltersPerVlan_Type()
)
maxNumOfOuiFiltersPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfOuiFiltersPerVlan.setStatus("current")
_OuiFilterTable_Object = MibTable
ouiFilterTable = _OuiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 12)
)
if mibBuilder.loadTexts:
    ouiFilterTable.setStatus("current")
_OuiFilterEntry_Object = MibTableRow
ouiFilterEntry = _OuiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 12, 1)
)
ouiFilterEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "E5-111-MIB", "ouiFilterAddr"),
)
if mibBuilder.loadTexts:
    ouiFilterEntry.setStatus("current")
_OuiFilterAddr_Type = OctetString
_OuiFilterAddr_Object = MibTableColumn
ouiFilterAddr = _OuiFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 12, 1, 1),
    _OuiFilterAddr_Type()
)
ouiFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ouiFilterAddr.setStatus("current")
_OuiFilterRowStatus_Type = RowStatus
_OuiFilterRowStatus_Object = MibTableColumn
ouiFilterRowStatus = _OuiFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 12, 1, 2),
    _OuiFilterRowStatus_Type()
)
ouiFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ouiFilterRowStatus.setStatus("current")
_OuiFilterVlanTable_Object = MibTable
ouiFilterVlanTable = _OuiFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 13)
)
if mibBuilder.loadTexts:
    ouiFilterVlanTable.setStatus("current")
_OuiFilterVlanEntry_Object = MibTableRow
ouiFilterVlanEntry = _OuiFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 13, 1)
)
ouiFilterVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    ouiFilterVlanEntry.setStatus("current")


class _OuiFilterVlanEnable_Type(Integer32):
    """Custom type ouiFilterVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enableOuiFilter", 1))
    )


_OuiFilterVlanEnable_Type.__name__ = "Integer32"
_OuiFilterVlanEnable_Object = MibTableColumn
ouiFilterVlanEnable = _OuiFilterVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 13, 1, 1),
    _OuiFilterVlanEnable_Type()
)
ouiFilterVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterVlanEnable.setStatus("current")


class _OuiFilterVlanFilterMode_Type(Integer32):
    """Custom type ouiFilterVlanFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_OuiFilterVlanFilterMode_Type.__name__ = "Integer32"
_OuiFilterVlanFilterMode_Object = MibTableColumn
ouiFilterVlanFilterMode = _OuiFilterVlanFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 53, 13, 1, 2),
    _OuiFilterVlanFilterMode_Type()
)
ouiFilterVlanFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ouiFilterVlanFilterMode.setStatus("current")
_DhcpSnoop_ObjectIdentity = ObjectIdentity
dhcpSnoop = _DhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55)
)
_DhcpSnoopPortTable_Object = MibTable
dhcpSnoopPortTable = _DhcpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortTable.setStatus("current")
_DhcpSnoopPortEntry_Object = MibTableRow
dhcpSnoopPortEntry = _DhcpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 1, 1)
)
dhcpSnoopPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortEntry.setStatus("current")


class _DhcpSnoopEnable_Type(Integer32):
    """Custom type dhcpSnoopEnable based on Integer32"""
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


_DhcpSnoopEnable_Type.__name__ = "Integer32"
_DhcpSnoopEnable_Object = MibTableColumn
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 1, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopMaxcnt_Type = Integer32
_DhcpSnoopMaxcnt_Object = MibTableColumn
dhcpSnoopMaxcnt = _DhcpSnoopMaxcnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 1, 1, 2),
    _DhcpSnoopMaxcnt_Type()
)
dhcpSnoopMaxcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopMaxcnt.setStatus("current")


class _DhcpSnoopSmacverifyEnable_Type(Integer32):
    """Custom type dhcpSnoopSmacverifyEnable based on Integer32"""
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


_DhcpSnoopSmacverifyEnable_Type.__name__ = "Integer32"
_DhcpSnoopSmacverifyEnable_Object = MibTableColumn
dhcpSnoopSmacverifyEnable = _DhcpSnoopSmacverifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 1, 1, 3),
    _DhcpSnoopSmacverifyEnable_Type()
)
dhcpSnoopSmacverifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopSmacverifyEnable.setStatus("current")
_DhcpSnoopTarget_Type = OctetString
_DhcpSnoopTarget_Object = MibScalar
dhcpSnoopTarget = _DhcpSnoopTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 2),
    _DhcpSnoopTarget_Type()
)
dhcpSnoopTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopTarget.setStatus("current")
_DhcpSnoopOps_Type = Integer32
_DhcpSnoopOps_Object = MibScalar
dhcpSnoopOps = _DhcpSnoopOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 3),
    _DhcpSnoopOps_Type()
)
dhcpSnoopOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopOps.setStatus("current")
_DhcpStaticTable_Object = MibTable
dhcpStaticTable = _DhcpStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 4)
)
if mibBuilder.loadTexts:
    dhcpStaticTable.setStatus("current")
_DhcpStaticEntry_Object = MibTableRow
dhcpStaticEntry = _DhcpStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 4, 1)
)
dhcpStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "dhcpStaticIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpStaticEntry.setStatus("current")
_DhcpStaticIpAddr_Type = IpAddress
_DhcpStaticIpAddr_Object = MibTableColumn
dhcpStaticIpAddr = _DhcpStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 4, 1, 1),
    _DhcpStaticIpAddr_Type()
)
dhcpStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIpAddr.setStatus("current")
_DhcpStaticRowStatus_Type = RowStatus
_DhcpStaticRowStatus_Object = MibTableColumn
dhcpStaticRowStatus = _DhcpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 4, 1, 2),
    _DhcpStaticRowStatus_Type()
)
dhcpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpStaticRowStatus.setStatus("current")
_MaxNumOfDhcpStaticIp_Type = Integer32
_MaxNumOfDhcpStaticIp_Object = MibScalar
maxNumOfDhcpStaticIp = _MaxNumOfDhcpStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 5),
    _MaxNumOfDhcpStaticIp_Type()
)
maxNumOfDhcpStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfDhcpStaticIp.setStatus("current")


class _DhcpSnoopMaxcntMode_Type(Integer32):
    """Custom type dhcpSnoopMaxcntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("replace", 1))
    )


_DhcpSnoopMaxcntMode_Type.__name__ = "Integer32"
_DhcpSnoopMaxcntMode_Object = MibScalar
dhcpSnoopMaxcntMode = _DhcpSnoopMaxcntMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 55, 6),
    _DhcpSnoopMaxcntMode_Type()
)
dhcpSnoopMaxcntMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopMaxcntMode.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56)
)
_AclSetTable_Object = MibTable
aclSetTable = _AclSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1)
)
if mibBuilder.loadTexts:
    aclSetTable.setStatus("current")
_AclSetEntry_Object = MibTableRow
aclSetEntry = _AclSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1, 1)
)
aclSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "aclSetVpi"),
    (0, "E5-111-MIB", "aclSetVci"),
    (0, "E5-111-MIB", "aclSetProfileName"),
)
if mibBuilder.loadTexts:
    aclSetEntry.setStatus("current")
_AclSetVpi_Type = Integer32
_AclSetVpi_Object = MibTableColumn
aclSetVpi = _AclSetVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1, 1, 1),
    _AclSetVpi_Type()
)
aclSetVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVpi.setStatus("current")
_AclSetVci_Type = Integer32
_AclSetVci_Object = MibTableColumn
aclSetVci = _AclSetVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1, 1, 2),
    _AclSetVci_Type()
)
aclSetVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetVci.setStatus("current")
_AclSetProfileName_Type = DisplayString
_AclSetProfileName_Object = MibTableColumn
aclSetProfileName = _AclSetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1, 1, 3),
    _AclSetProfileName_Type()
)
aclSetProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclSetProfileName.setStatus("current")
_AclSetRowStatus_Type = RowStatus
_AclSetRowStatus_Object = MibTableColumn
aclSetRowStatus = _AclSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 1, 1, 4),
    _AclSetRowStatus_Type()
)
aclSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclSetRowStatus.setStatus("current")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "E5-111-MIB", "aclProfileRuleName"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")
_AclProfileRuleName_Type = DisplayString
_AclProfileRuleName_Object = MibTableColumn
aclProfileRuleName = _AclProfileRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 1),
    _AclProfileRuleName_Type()
)
aclProfileRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleName.setStatus("current")
_AclProfileRuleNumber_Type = Integer32
_AclProfileRuleNumber_Object = MibTableColumn
aclProfileRuleNumber = _AclProfileRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 2),
    _AclProfileRuleNumber_Type()
)
aclProfileRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleNumber.setStatus("current")
_AclProfileActionNumber_Type = Integer32
_AclProfileActionNumber_Object = MibTableColumn
aclProfileActionNumber = _AclProfileActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 3),
    _AclProfileActionNumber_Type()
)
aclProfileActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionNumber.setStatus("current")
_AclProfileRuleParamMask_Type = Integer32
_AclProfileRuleParamMask_Object = MibTableColumn
aclProfileRuleParamMask = _AclProfileRuleParamMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 4),
    _AclProfileRuleParamMask_Type()
)
aclProfileRuleParamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleParamMask.setStatus("current")


class _AclProfileRuleEtype_Type(Integer32):
    """Custom type aclProfileRuleEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleEtype_Type.__name__ = "Integer32"
_AclProfileRuleEtype_Object = MibTableColumn
aclProfileRuleEtype = _AclProfileRuleEtype_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 5),
    _AclProfileRuleEtype_Type()
)
aclProfileRuleEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleEtype.setStatus("current")


class _AclProfileRuleVid_Type(Integer32):
    """Custom type aclProfileRuleVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileRuleVid_Type.__name__ = "Integer32"
_AclProfileRuleVid_Object = MibTableColumn
aclProfileRuleVid = _AclProfileRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 6),
    _AclProfileRuleVid_Type()
)
aclProfileRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleVid.setStatus("current")
_AclProfileRuleSmac_Type = PhysAddress
_AclProfileRuleSmac_Object = MibTableColumn
aclProfileRuleSmac = _AclProfileRuleSmac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 7),
    _AclProfileRuleSmac_Type()
)
aclProfileRuleSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSmac.setStatus("current")
_AclProfileRuleDmac_Type = PhysAddress
_AclProfileRuleDmac_Object = MibTableColumn
aclProfileRuleDmac = _AclProfileRuleDmac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 8),
    _AclProfileRuleDmac_Type()
)
aclProfileRuleDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDmac.setStatus("current")


class _AclProfileRulePriority_Type(Integer32):
    """Custom type aclProfileRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileRulePriority_Type.__name__ = "Integer32"
_AclProfileRulePriority_Object = MibTableColumn
aclProfileRulePriority = _AclProfileRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 9),
    _AclProfileRulePriority_Type()
)
aclProfileRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRulePriority.setStatus("current")


class _AclProfileRuleProtocol_Type(Integer32):
    """Custom type aclProfileRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleProtocol_Type.__name__ = "Integer32"
_AclProfileRuleProtocol_Object = MibTableColumn
aclProfileRuleProtocol = _AclProfileRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 10),
    _AclProfileRuleProtocol_Type()
)
aclProfileRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleProtocol.setStatus("current")
_AclProfileRuleSrcIP_Type = IpAddress
_AclProfileRuleSrcIP_Object = MibTableColumn
aclProfileRuleSrcIP = _AclProfileRuleSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 11),
    _AclProfileRuleSrcIP_Type()
)
aclProfileRuleSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIP.setStatus("current")


class _AclProfileRuleSrcIPMask_Type(Integer32):
    """Custom type aclProfileRuleSrcIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclProfileRuleSrcIPMask_Type.__name__ = "Integer32"
_AclProfileRuleSrcIPMask_Object = MibTableColumn
aclProfileRuleSrcIPMask = _AclProfileRuleSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 12),
    _AclProfileRuleSrcIPMask_Type()
)
aclProfileRuleSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcIPMask.setStatus("current")
_AclProfileRuleDestIP_Type = IpAddress
_AclProfileRuleDestIP_Object = MibTableColumn
aclProfileRuleDestIP = _AclProfileRuleDestIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 13),
    _AclProfileRuleDestIP_Type()
)
aclProfileRuleDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestIP.setStatus("current")


class _AclProfileRuleDestIPMask_Type(Integer32):
    """Custom type aclProfileRuleDestIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclProfileRuleDestIPMask_Type.__name__ = "Integer32"
_AclProfileRuleDestIPMask_Object = MibTableColumn
aclProfileRuleDestIPMask = _AclProfileRuleDestIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 14),
    _AclProfileRuleDestIPMask_Type()
)
aclProfileRuleDestIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestIPMask.setStatus("current")


class _AclProfileRuleStartTos_Type(Integer32):
    """Custom type aclProfileRuleStartTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleStartTos_Type.__name__ = "Integer32"
_AclProfileRuleStartTos_Object = MibTableColumn
aclProfileRuleStartTos = _AclProfileRuleStartTos_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 15),
    _AclProfileRuleStartTos_Type()
)
aclProfileRuleStartTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleStartTos.setStatus("current")


class _AclProfileRuleEndTos_Type(Integer32):
    """Custom type aclProfileRuleEndTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclProfileRuleEndTos_Type.__name__ = "Integer32"
_AclProfileRuleEndTos_Object = MibTableColumn
aclProfileRuleEndTos = _AclProfileRuleEndTos_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 16),
    _AclProfileRuleEndTos_Type()
)
aclProfileRuleEndTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleEndTos.setStatus("current")


class _AclProfileRuleSrcStartPort_Type(Integer32):
    """Custom type aclProfileRuleSrcStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcStartPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcStartPort_Object = MibTableColumn
aclProfileRuleSrcStartPort = _AclProfileRuleSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 17),
    _AclProfileRuleSrcStartPort_Type()
)
aclProfileRuleSrcStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcStartPort.setStatus("current")


class _AclProfileRuleSrcEndPort_Type(Integer32):
    """Custom type aclProfileRuleSrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleSrcEndPort_Type.__name__ = "Integer32"
_AclProfileRuleSrcEndPort_Object = MibTableColumn
aclProfileRuleSrcEndPort = _AclProfileRuleSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 18),
    _AclProfileRuleSrcEndPort_Type()
)
aclProfileRuleSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleSrcEndPort.setStatus("current")


class _AclProfileRuleDestStartPort_Type(Integer32):
    """Custom type aclProfileRuleDestStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestStartPort_Type.__name__ = "Integer32"
_AclProfileRuleDestStartPort_Object = MibTableColumn
aclProfileRuleDestStartPort = _AclProfileRuleDestStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 19),
    _AclProfileRuleDestStartPort_Type()
)
aclProfileRuleDestStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestStartPort.setStatus("current")


class _AclProfileRuleDestEndPort_Type(Integer32):
    """Custom type aclProfileRuleDestEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleDestEndPort_Type.__name__ = "Integer32"
_AclProfileRuleDestEndPort_Object = MibTableColumn
aclProfileRuleDestEndPort = _AclProfileRuleDestEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 20),
    _AclProfileRuleDestEndPort_Type()
)
aclProfileRuleDestEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRuleDestEndPort.setStatus("current")


class _AclProfileActionRate_Type(Integer32):
    """Custom type aclProfileActionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclProfileActionRate_Type.__name__ = "Integer32"
_AclProfileActionRate_Object = MibTableColumn
aclProfileActionRate = _AclProfileActionRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 21),
    _AclProfileActionRate_Type()
)
aclProfileActionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionRate.setStatus("current")


class _AclProfileActionrvlan_Type(Integer32):
    """Custom type aclProfileActionrvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclProfileActionrvlan_Type.__name__ = "Integer32"
_AclProfileActionrvlan_Object = MibTableColumn
aclProfileActionrvlan = _AclProfileActionrvlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 22),
    _AclProfileActionrvlan_Type()
)
aclProfileActionrvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrvlan.setStatus("current")


class _AclProfileActionrpri_Type(Integer32):
    """Custom type aclProfileActionrpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclProfileActionrpri_Type.__name__ = "Integer32"
_AclProfileActionrpri_Object = MibTableColumn
aclProfileActionrpri = _AclProfileActionrpri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 23),
    _AclProfileActionrpri_Type()
)
aclProfileActionrpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileActionrpri.setStatus("current")
_AclProfileRowStatus_Type = RowStatus
_AclProfileRowStatus_Object = MibTableColumn
aclProfileRowStatus = _AclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 56, 2, 1, 24),
    _AclProfileRowStatus_Type()
)
aclProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileRowStatus.setStatus("current")
_PppoeAgent_ObjectIdentity = ObjectIdentity
pppoeAgent = _PppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57)
)
_PppoeAgentTable_Object = MibTable
pppoeAgentTable = _PppoeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1)
)
if mibBuilder.loadTexts:
    pppoeAgentTable.setStatus("current")
_PppoeAgentEntry_Object = MibTableRow
pppoeAgentEntry = _PppoeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1, 1)
)
pppoeAgentEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    pppoeAgentEntry.setStatus("current")


class _PppoeAgentEnable_Type(Integer32):
    """Custom type pppoeAgentEnable based on Integer32"""
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


_PppoeAgentEnable_Type.__name__ = "Integer32"
_PppoeAgentEnable_Object = MibTableColumn
pppoeAgentEnable = _PppoeAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1, 1, 1),
    _PppoeAgentEnable_Type()
)
pppoeAgentEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentEnable.setStatus("current")


class _PppoeAgentInfo_Type(DisplayString):
    """Custom type pppoeAgentInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_PppoeAgentInfo_Type.__name__ = "DisplayString"
_PppoeAgentInfo_Object = MibTableColumn
pppoeAgentInfo = _PppoeAgentInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1, 1, 2),
    _PppoeAgentInfo_Type()
)
pppoeAgentInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentInfo.setStatus("current")
_PppoeAgentRowStatus_Type = RowStatus
_PppoeAgentRowStatus_Object = MibTableColumn
pppoeAgentRowStatus = _PppoeAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1, 1, 3),
    _PppoeAgentRowStatus_Type()
)
pppoeAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentRowStatus.setStatus("current")


class _PppoeAgentOptionMode_Type(Integer32):
    """Custom type pppoeAgentOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("tr101", 2))
    )


_PppoeAgentOptionMode_Type.__name__ = "Integer32"
_PppoeAgentOptionMode_Object = MibTableColumn
pppoeAgentOptionMode = _PppoeAgentOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 1, 1, 4),
    _PppoeAgentOptionMode_Type()
)
pppoeAgentOptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeAgentOptionMode.setStatus("current")
_MaxNumOfPppoeDhcpRelay82Conf_Type = Integer32
_MaxNumOfPppoeDhcpRelay82Conf_Object = MibScalar
maxNumOfPppoeDhcpRelay82Conf = _MaxNumOfPppoeDhcpRelay82Conf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 57, 2),
    _MaxNumOfPppoeDhcpRelay82Conf_Type()
)
maxNumOfPppoeDhcpRelay82Conf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfPppoeDhcpRelay82Conf.setStatus("current")
_Macff_ObjectIdentity = ObjectIdentity
macff = _Macff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60)
)
_MacFfTable_Object = MibTable
macFfTable = _MacFfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1)
)
if mibBuilder.loadTexts:
    macFfTable.setStatus("current")
_MacFfEntry_Object = MibTableRow
macFfEntry = _MacFfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1)
)
macFfEntry.setIndexNames(
    (0, "E5-111-MIB", "macFfIndex"),
)
if mibBuilder.loadTexts:
    macFfEntry.setStatus("current")
_MacFfIndex_Type = Integer32
_MacFfIndex_Object = MibTableColumn
macFfIndex = _MacFfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 1),
    _MacFfIndex_Type()
)
macFfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfIndex.setStatus("current")
_MacFfVid_Type = Integer32
_MacFfVid_Object = MibTableColumn
macFfVid = _MacFfVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 2),
    _MacFfVid_Type()
)
macFfVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfVid.setStatus("current")
_MacFfArIP_Type = IpAddress
_MacFfArIP_Object = MibTableColumn
macFfArIP = _MacFfArIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 3),
    _MacFfArIP_Type()
)
macFfArIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArIP.setStatus("current")
_MacFfSrcIP_Type = IpAddress
_MacFfSrcIP_Object = MibTableColumn
macFfSrcIP = _MacFfSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 4),
    _MacFfSrcIP_Type()
)
macFfSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcIP.setStatus("current")
_MacFfSrcMask_Type = Integer32
_MacFfSrcMask_Object = MibTableColumn
macFfSrcMask = _MacFfSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 5),
    _MacFfSrcMask_Type()
)
macFfSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfSrcMask.setStatus("current")
_MacFfRowStatus_Type = RowStatus
_MacFfRowStatus_Object = MibTableColumn
macFfRowStatus = _MacFfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 1, 1, 6),
    _MacFfRowStatus_Type()
)
macFfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfRowStatus.setStatus("current")
_MacFfArpFlush_Type = Integer32
_MacFfArpFlush_Object = MibScalar
macFfArpFlush = _MacFfArpFlush_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 3),
    _MacFfArpFlush_Type()
)
macFfArpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFfArpFlush.setStatus("current")
_MaxNumOfMacFfVlanInSystem_Type = Integer32
_MaxNumOfMacFfVlanInSystem_Object = MibScalar
maxNumOfMacFfVlanInSystem = _MaxNumOfMacFfVlanInSystem_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 4),
    _MaxNumOfMacFfVlanInSystem_Type()
)
maxNumOfMacFfVlanInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMacFfVlanInSystem.setStatus("current")
_MacFfVlanTable_Object = MibTable
macFfVlanTable = _MacFfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 5)
)
if mibBuilder.loadTexts:
    macFfVlanTable.setStatus("current")
_MacFfVlanEntry_Object = MibTableRow
macFfVlanEntry = _MacFfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 5, 1)
)
macFfVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    macFfVlanEntry.setStatus("current")
_MacFfVlanRowstatus_Type = RowStatus
_MacFfVlanRowstatus_Object = MibTableColumn
macFfVlanRowstatus = _MacFfVlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 5, 1, 1),
    _MacFfVlanRowstatus_Type()
)
macFfVlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfVlanRowstatus.setStatus("current")


class _MacFfVlanUnknownUnicast_Type(Integer32):
    """Custom type macFfVlanUnknownUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_MacFfVlanUnknownUnicast_Type.__name__ = "Integer32"
_MacFfVlanUnknownUnicast_Object = MibTableColumn
macFfVlanUnknownUnicast = _MacFfVlanUnknownUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 5, 1, 2),
    _MacFfVlanUnknownUnicast_Type()
)
macFfVlanUnknownUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfVlanUnknownUnicast.setStatus("current")
_MacFfStaticIPTable_Object = MibTable
macFfStaticIPTable = _MacFfStaticIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6)
)
if mibBuilder.loadTexts:
    macFfStaticIPTable.setStatus("current")
_MacFfStaticIPEntry_Object = MibTableRow
macFfStaticIPEntry = _MacFfStaticIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1)
)
macFfStaticIPEntry.setIndexNames(
    (0, "E5-111-MIB", "macFfStaticIPPort"),
    (0, "E5-111-MIB", "macFfStaticIPVid"),
    (0, "E5-111-MIB", "macFfstaticIP"),
    (0, "E5-111-MIB", "macFfStaticIPMask"),
)
if mibBuilder.loadTexts:
    macFfStaticIPEntry.setStatus("current")
_MacFfStaticIPPort_Type = Integer32
_MacFfStaticIPPort_Object = MibTableColumn
macFfStaticIPPort = _MacFfStaticIPPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1, 1),
    _MacFfStaticIPPort_Type()
)
macFfStaticIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPPort.setStatus("current")
_MacFfStaticIPVid_Type = Integer32
_MacFfStaticIPVid_Object = MibTableColumn
macFfStaticIPVid = _MacFfStaticIPVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1, 2),
    _MacFfStaticIPVid_Type()
)
macFfStaticIPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPVid.setStatus("current")
_MacFfstaticIP_Type = IpAddress
_MacFfstaticIP_Object = MibTableColumn
macFfstaticIP = _MacFfstaticIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1, 3),
    _MacFfstaticIP_Type()
)
macFfstaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfstaticIP.setStatus("current")
_MacFfStaticIPMask_Type = Integer32
_MacFfStaticIPMask_Object = MibTableColumn
macFfStaticIPMask = _MacFfStaticIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1, 4),
    _MacFfStaticIPMask_Type()
)
macFfStaticIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStaticIPMask.setStatus("current")
_MacFfStaticIPRowStatus_Type = RowStatus
_MacFfStaticIPRowStatus_Object = MibTableColumn
macFfStaticIPRowStatus = _MacFfStaticIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 10, 60, 6, 1, 5),
    _MacFfStaticIPRowStatus_Type()
)
macFfStaticIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFfStaticIPRowStatus.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11)
)
_AccessCtrl_ObjectIdentity = ObjectIdentity
accessCtrl = _AccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5)
)
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "E5-111-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1, 2),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1, 3),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")
_SecuredClientService_Type = Integer32
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1, 4),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("current")


class _SecuredClientEnable_Type(Integer32):
    """Custom type securedClientEnable based on Integer32"""
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


_SecuredClientEnable_Type.__name__ = "Integer32"
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 5, 2, 1, 5),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_ExtAlarm_ObjectIdentity = ObjectIdentity
extAlarm = _ExtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8)
)
_ExtAlarmTable_Object = MibTable
extAlarmTable = _ExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    extAlarmTable.setStatus("current")
_ExtAlarmEntry_Object = MibTableRow
extAlarmEntry = _ExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1, 1)
)
extAlarmEntry.setIndexNames(
    (0, "E5-111-MIB", "extAlarmIndex"),
)
if mibBuilder.loadTexts:
    extAlarmEntry.setStatus("current")
_ExtAlarmIndex_Type = Integer32
_ExtAlarmIndex_Object = MibTableColumn
extAlarmIndex = _ExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1, 1, 1),
    _ExtAlarmIndex_Type()
)
extAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmIndex.setStatus("current")


class _ExtAlarmname_Type(DisplayString):
    """Custom type extAlarmname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmname_Type.__name__ = "DisplayString"
_ExtAlarmname_Object = MibTableColumn
extAlarmname = _ExtAlarmname_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1, 1, 2),
    _ExtAlarmname_Type()
)
extAlarmname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmname.setStatus("current")


class _ExtAlarmstatus_Type(DisplayString):
    """Custom type extAlarmstatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtAlarmstatus_Type.__name__ = "DisplayString"
_ExtAlarmstatus_Object = MibTableColumn
extAlarmstatus = _ExtAlarmstatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1, 1, 3),
    _ExtAlarmstatus_Type()
)
extAlarmstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extAlarmstatus.setStatus("current")


class _ExtAlarmTriggeredMode_Type(Integer32):
    """Custom type extAlarmTriggeredMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closeAlarm", 1),
          ("openAlarm", 2))
    )


_ExtAlarmTriggeredMode_Type.__name__ = "Integer32"
_ExtAlarmTriggeredMode_Object = MibTableColumn
extAlarmTriggeredMode = _ExtAlarmTriggeredMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 8, 1, 1, 4),
    _ExtAlarmTriggeredMode_Type()
)
extAlarmTriggeredMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extAlarmTriggeredMode.setStatus("current")
_User_ObjectIdentity = ObjectIdentity
user = _User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9)
)


class _UserAuthMode_Type(Integer32):
    """Custom type userAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("localThenRadius", 3),
          ("radius", 2))
    )


_UserAuthMode_Type.__name__ = "Integer32"
_UserAuthMode_Object = MibScalar
userAuthMode = _UserAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 1),
    _UserAuthMode_Type()
)
userAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMode.setStatus("current")
_UserAuthServerIp_Type = IpAddress
_UserAuthServerIp_Object = MibScalar
userAuthServerIp = _UserAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 2),
    _UserAuthServerIp_Type()
)
userAuthServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerIp.setStatus("current")
_UserAuthServerPort_Type = Integer32
_UserAuthServerPort_Object = MibScalar
userAuthServerPort = _UserAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 3),
    _UserAuthServerPort_Type()
)
userAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerPort.setStatus("current")
_UserAuthServerSecret_Type = OctetString
_UserAuthServerSecret_Object = MibScalar
userAuthServerSecret = _UserAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 4),
    _UserAuthServerSecret_Type()
)
userAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthServerSecret.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5, 1)
)
userEntry.setIndexNames(
    (0, "E5-111-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5, 1, 2),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserPriviledge_Type(Integer32):
    """Custom type userPriviledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("middle", 2))
    )


_UserPriviledge_Type.__name__ = "Integer32"
_UserPriviledge_Object = MibTableColumn
userPriviledge = _UserPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5, 1, 3),
    _UserPriviledge_Type()
)
userPriviledge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPriviledge.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 5, 1, 4),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("current")


class _UserAuthDefaultPriviledge_Type(Integer32):
    """Custom type userAuthDefaultPriviledge based on Integer32"""
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
        *(("deny", 4),
          ("high", 1),
          ("low", 3),
          ("middle", 2))
    )


_UserAuthDefaultPriviledge_Type.__name__ = "Integer32"
_UserAuthDefaultPriviledge_Object = MibScalar
userAuthDefaultPriviledge = _UserAuthDefaultPriviledge_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 9, 6),
    _UserAuthDefaultPriviledge_Type()
)
userAuthDefaultPriviledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthDefaultPriviledge.setStatus("current")
_UsbCastCtrl_ObjectIdentity = ObjectIdentity
usbCastCtrl = _UsbCastCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 10)
)


class _UsBcastCtrlEnable_Type(Integer32):
    """Custom type usBcastCtrlEnable based on Integer32"""
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


_UsBcastCtrlEnable_Type.__name__ = "Integer32"
_UsBcastCtrlEnable_Object = MibScalar
usBcastCtrlEnable = _UsBcastCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 10, 1),
    _UsBcastCtrlEnable_Type()
)
usBcastCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlEnable.setStatus("current")
_UsBcastCtrlRate_Type = Integer32
_UsBcastCtrlRate_Object = MibScalar
usBcastCtrlRate = _UsBcastCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 10, 2),
    _UsBcastCtrlRate_Type()
)
usBcastCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setStatus("current")
if mibBuilder.loadTexts:
    usBcastCtrlRate.setUnits("Kbps")
_DsbCastCtrl_ObjectIdentity = ObjectIdentity
dsbCastCtrl = _DsbCastCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 11)
)


class _DsBcastCtrlEnable_Type(Integer32):
    """Custom type dsBcastCtrlEnable based on Integer32"""
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


_DsBcastCtrlEnable_Type.__name__ = "Integer32"
_DsBcastCtrlEnable_Object = MibScalar
dsBcastCtrlEnable = _DsBcastCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 11, 1),
    _DsBcastCtrlEnable_Type()
)
dsBcastCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsBcastCtrlEnable.setStatus("current")
_DsBcastCtrlRate_Type = Integer32
_DsBcastCtrlRate_Object = MibScalar
dsBcastCtrlRate = _DsBcastCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 11, 2),
    _DsBcastCtrlRate_Type()
)
dsBcastCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsBcastCtrlRate.setStatus("current")
if mibBuilder.loadTexts:
    dsBcastCtrlRate.setUnits("Kbps")


class _StdioTimeout_Type(Integer32):
    """Custom type stdioTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_StdioTimeout_Type.__name__ = "Integer32"
_StdioTimeout_Object = MibScalar
stdioTimeout = _StdioTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 12),
    _StdioTimeout_Type()
)
stdioTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stdioTimeout.setStatus("current")


class _IsConfigChanged_Type(Integer32):
    """Custom type isConfigChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IsConfigChanged_Type.__name__ = "Integer32"
_IsConfigChanged_Object = MibScalar
isConfigChanged = _IsConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 13),
    _IsConfigChanged_Type()
)
isConfigChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isConfigChanged.setStatus("current")
_FwUpgrade_ObjectIdentity = ObjectIdentity
fwUpgrade = _FwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 14)
)
_FwUpgradeVersion_Type = OctetString
_FwUpgradeVersion_Object = MibScalar
fwUpgradeVersion = _FwUpgradeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 14, 1),
    _FwUpgradeVersion_Type()
)
fwUpgradeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpgradeVersion.setStatus("current")


class _FwUpgradeCheck_Type(Integer32):
    """Custom type fwUpgradeCheck based on Integer32"""
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


_FwUpgradeCheck_Type.__name__ = "Integer32"
_FwUpgradeCheck_Object = MibScalar
fwUpgradeCheck = _FwUpgradeCheck_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 14, 2),
    _FwUpgradeCheck_Type()
)
fwUpgradeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwUpgradeCheck.setStatus("current")
_FwUpgradeStatus_Type = DisplayString
_FwUpgradeStatus_Object = MibScalar
fwUpgradeStatus = _FwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 14, 3),
    _FwUpgradeStatus_Type()
)
fwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUpgradeStatus.setStatus("current")
_DelayedReboot_ObjectIdentity = ObjectIdentity
delayedReboot = _DelayedReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 15)
)
_DelayedRebootTimer_Type = Integer32
_DelayedRebootTimer_Object = MibScalar
delayedRebootTimer = _DelayedRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 15, 1),
    _DelayedRebootTimer_Type()
)
delayedRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delayedRebootTimer.setStatus("current")
if mibBuilder.loadTexts:
    delayedRebootTimer.setUnits("sec")
_DelayedRebootRemainingTime_Type = Integer32
_DelayedRebootRemainingTime_Object = MibScalar
delayedRebootRemainingTime = _DelayedRebootRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 15, 2),
    _DelayedRebootRemainingTime_Type()
)
delayedRebootRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayedRebootRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    delayedRebootRemainingTime.setUnits("sec")


class _DelayedRebootCancel_Type(Integer32):
    """Custom type delayedRebootCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancel", 1)
    )


_DelayedRebootCancel_Type.__name__ = "Integer32"
_DelayedRebootCancel_Object = MibScalar
delayedRebootCancel = _DelayedRebootCancel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 11, 15, 3),
    _DelayedRebootCancel_Type()
)
delayedRebootCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delayedRebootCancel.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 12)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13)
)
_IgmpQueryCntTotal_Type = Counter32
_IgmpQueryCntTotal_Object = MibScalar
igmpQueryCntTotal = _IgmpQueryCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 1),
    _IgmpQueryCntTotal_Type()
)
igmpQueryCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryCntTotal.setStatus("current")
_IgmpReportCntTotal_Type = Counter32
_IgmpReportCntTotal_Object = MibScalar
igmpReportCntTotal = _IgmpReportCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 2),
    _IgmpReportCntTotal_Type()
)
igmpReportCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpReportCntTotal.setStatus("current")
_IgmpLeaveCntTotal_Type = Counter32
_IgmpLeaveCntTotal_Object = MibScalar
igmpLeaveCntTotal = _IgmpLeaveCntTotal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 3),
    _IgmpLeaveCntTotal_Type()
)
igmpLeaveCntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLeaveCntTotal.setStatus("current")
_IgmpNumOfActiveGroups_Type = Integer32
_IgmpNumOfActiveGroups_Object = MibScalar
igmpNumOfActiveGroups = _IgmpNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 4),
    _IgmpNumOfActiveGroups_Type()
)
igmpNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpNumOfActiveGroups.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "E5-111-MIB", "igmpGroupIp"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")
_IgmpGroupIp_Type = IpAddress
_IgmpGroupIp_Object = MibTableColumn
igmpGroupIp = _IgmpGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5, 1, 1),
    _IgmpGroupIp_Type()
)
igmpGroupIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIp.setStatus("current")
_IgmpGroupvid_Type = Integer32
_IgmpGroupvid_Object = MibTableColumn
igmpGroupvid = _IgmpGroupvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5, 1, 2),
    _IgmpGroupvid_Type()
)
igmpGroupvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupvid.setStatus("current")
_IgmpGroupnumberOfMembers_Type = Integer32
_IgmpGroupnumberOfMembers_Object = MibTableColumn
igmpGroupnumberOfMembers = _IgmpGroupnumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5, 1, 3),
    _IgmpGroupnumberOfMembers_Type()
)
igmpGroupnumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupnumberOfMembers.setStatus("current")
_IgmpGroupMemberPorts_Type = PortList
_IgmpGroupMemberPorts_Object = MibTableColumn
igmpGroupMemberPorts = _IgmpGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 5, 1, 4),
    _IgmpGroupMemberPorts_Type()
)
igmpGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupMemberPorts.setStatus("current")
_IgmpGroupPortTable_Object = MibTable
igmpGroupPortTable = _IgmpGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 6)
)
if mibBuilder.loadTexts:
    igmpGroupPortTable.setStatus("current")
_IgmpGroupPortEntry_Object = MibTableRow
igmpGroupPortEntry = _IgmpGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 6, 1)
)
igmpGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "igmpGroupPortIp"),
    (0, "E5-111-MIB", "igmpGroupPortvid"),
)
if mibBuilder.loadTexts:
    igmpGroupPortEntry.setStatus("current")
_IgmpGroupPortIp_Type = IpAddress
_IgmpGroupPortIp_Object = MibTableColumn
igmpGroupPortIp = _IgmpGroupPortIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 6, 1, 1),
    _IgmpGroupPortIp_Type()
)
igmpGroupPortIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortIp.setStatus("current")
_IgmpGroupPortvid_Type = Integer32
_IgmpGroupPortvid_Object = MibTableColumn
igmpGroupPortvid = _IgmpGroupPortvid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 6, 1, 2),
    _IgmpGroupPortvid_Type()
)
igmpGroupPortvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortvid.setStatus("current")
_IgmpGroupV2Table_Object = MibTable
igmpGroupV2Table = _IgmpGroupV2Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7)
)
if mibBuilder.loadTexts:
    igmpGroupV2Table.setStatus("current")
_IgmpGroupV2Entry_Object = MibTableRow
igmpGroupV2Entry = _IgmpGroupV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7, 1)
)
igmpGroupV2Entry.setIndexNames(
    (0, "E5-111-MIB", "igmpGroupV2Vid"),
    (0, "E5-111-MIB", "igmpGroupV2Ip"),
)
if mibBuilder.loadTexts:
    igmpGroupV2Entry.setStatus("current")
_IgmpGroupV2Vid_Type = VlanIndex
_IgmpGroupV2Vid_Object = MibTableColumn
igmpGroupV2Vid = _IgmpGroupV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7, 1, 1),
    _IgmpGroupV2Vid_Type()
)
igmpGroupV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Vid.setStatus("current")
_IgmpGroupV2Ip_Type = IpAddress
_IgmpGroupV2Ip_Object = MibTableColumn
igmpGroupV2Ip = _IgmpGroupV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7, 1, 2),
    _IgmpGroupV2Ip_Type()
)
igmpGroupV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2Ip.setStatus("current")
_IgmpGroupV2NumOfMembers_Type = Integer32
_IgmpGroupV2NumOfMembers_Object = MibTableColumn
igmpGroupV2NumOfMembers = _IgmpGroupV2NumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7, 1, 3),
    _IgmpGroupV2NumOfMembers_Type()
)
igmpGroupV2NumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2NumOfMembers.setStatus("current")
_IgmpGroupV2MemberPorts_Type = PortList
_IgmpGroupV2MemberPorts_Object = MibTableColumn
igmpGroupV2MemberPorts = _IgmpGroupV2MemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 7, 1, 4),
    _IgmpGroupV2MemberPorts_Type()
)
igmpGroupV2MemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupV2MemberPorts.setStatus("current")
_IgmpGroupPortV2Table_Object = MibTable
igmpGroupPortV2Table = _IgmpGroupPortV2Table_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 8)
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Table.setStatus("current")
_IgmpGroupPortV2Entry_Object = MibTableRow
igmpGroupPortV2Entry = _IgmpGroupPortV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 8, 1)
)
igmpGroupPortV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "igmpGroupPortV2Vid"),
    (0, "E5-111-MIB", "igmpGroupPortV2Ip"),
    (0, "E5-111-MIB", "igmpGroupPortV2SourceIp"),
)
if mibBuilder.loadTexts:
    igmpGroupPortV2Entry.setStatus("current")
_IgmpGroupPortV2Vid_Type = VlanIndex
_IgmpGroupPortV2Vid_Object = MibTableColumn
igmpGroupPortV2Vid = _IgmpGroupPortV2Vid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 8, 1, 1),
    _IgmpGroupPortV2Vid_Type()
)
igmpGroupPortV2Vid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Vid.setStatus("current")
_IgmpGroupPortV2Ip_Type = IpAddress
_IgmpGroupPortV2Ip_Object = MibTableColumn
igmpGroupPortV2Ip = _IgmpGroupPortV2Ip_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 8, 1, 2),
    _IgmpGroupPortV2Ip_Type()
)
igmpGroupPortV2Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2Ip.setStatus("current")
_IgmpGroupPortV2SourceIp_Type = IpAddress
_IgmpGroupPortV2SourceIp_Object = MibTableColumn
igmpGroupPortV2SourceIp = _IgmpGroupPortV2SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 8, 1, 3),
    _IgmpGroupPortV2SourceIp_Type()
)
igmpGroupPortV2SourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupPortV2SourceIp.setStatus("current")
_IgmpPortCtrlPduTable_Object = MibTable
igmpPortCtrlPduTable = _IgmpPortCtrlPduTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9)
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduTable.setStatus("current")
_IgmpPortCtrlPduEntry_Object = MibTableRow
igmpPortCtrlPduEntry = _IgmpPortCtrlPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1)
)
igmpPortCtrlPduEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    igmpPortCtrlPduEntry.setStatus("current")
_IgmpPortCtrlPduQueryCnt_Type = Counter32
_IgmpPortCtrlPduQueryCnt_Object = MibTableColumn
igmpPortCtrlPduQueryCnt = _IgmpPortCtrlPduQueryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1, 1),
    _IgmpPortCtrlPduQueryCnt_Type()
)
igmpPortCtrlPduQueryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduQueryCnt.setStatus("current")
_IgmpPortCtrlPduReportCnt_Type = Counter32
_IgmpPortCtrlPduReportCnt_Object = MibTableColumn
igmpPortCtrlPduReportCnt = _IgmpPortCtrlPduReportCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1, 2),
    _IgmpPortCtrlPduReportCnt_Type()
)
igmpPortCtrlPduReportCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduReportCnt.setStatus("current")
_IgmpPortCtrlPduLeaveCnt_Type = Counter32
_IgmpPortCtrlPduLeaveCnt_Object = MibTableColumn
igmpPortCtrlPduLeaveCnt = _IgmpPortCtrlPduLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1, 3),
    _IgmpPortCtrlPduLeaveCnt_Type()
)
igmpPortCtrlPduLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlPduLeaveCnt.setStatus("current")
_IgmpPortNumOfActiveGroups_Type = Integer32
_IgmpPortNumOfActiveGroups_Object = MibTableColumn
igmpPortNumOfActiveGroups = _IgmpPortNumOfActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1, 4),
    _IgmpPortNumOfActiveGroups_Type()
)
igmpPortNumOfActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortNumOfActiveGroups.setStatus("current")
_IgmpPortCtrlAuditLeaveCnt_Type = Counter32
_IgmpPortCtrlAuditLeaveCnt_Object = MibTableColumn
igmpPortCtrlAuditLeaveCnt = _IgmpPortCtrlAuditLeaveCnt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 9, 1, 5),
    _IgmpPortCtrlAuditLeaveCnt_Type()
)
igmpPortCtrlAuditLeaveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpPortCtrlAuditLeaveCnt.setStatus("current")
_DhcpStats_ObjectIdentity = ObjectIdentity
dhcpStats = _DhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11)
)
_DhcpSnoopIpTable_Object = MibTable
dhcpSnoopIpTable = _DhcpSnoopIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopIpTable.setStatus("current")
_DhcpSnoopIpEntry_Object = MibTableRow
dhcpSnoopIpEntry = _DhcpSnoopIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1)
)
dhcpSnoopIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "dhcpSnoopIp"),
)
if mibBuilder.loadTexts:
    dhcpSnoopIpEntry.setStatus("current")
_DhcpSnoopIp_Type = IpAddress
_DhcpSnoopIp_Object = MibTableColumn
dhcpSnoopIp = _DhcpSnoopIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 1),
    _DhcpSnoopIp_Type()
)
dhcpSnoopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopIp.setStatus("current")
_DhcpSnoopMac_Type = PhysAddress
_DhcpSnoopMac_Object = MibTableColumn
dhcpSnoopMac = _DhcpSnoopMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 2),
    _DhcpSnoopMac_Type()
)
dhcpSnoopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMac.setStatus("current")
_DhcpSnoopVid_Type = VlanIndex
_DhcpSnoopVid_Object = MibTableColumn
dhcpSnoopVid = _DhcpSnoopVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 3),
    _DhcpSnoopVid_Type()
)
dhcpSnoopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopVid.setStatus("current")
_DhcpSnoopMask_Type = Integer32
_DhcpSnoopMask_Object = MibTableColumn
dhcpSnoopMask = _DhcpSnoopMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 4),
    _DhcpSnoopMask_Type()
)
dhcpSnoopMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopMask.setStatus("current")
_DhcpSnoopGateway_Type = IpAddress
_DhcpSnoopGateway_Object = MibTableColumn
dhcpSnoopGateway = _DhcpSnoopGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 5),
    _DhcpSnoopGateway_Type()
)
dhcpSnoopGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopGateway.setStatus("current")
_DhcpSnoopRouteMap_Type = OctetString
_DhcpSnoopRouteMap_Object = MibTableColumn
dhcpSnoopRouteMap = _DhcpSnoopRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 1, 1, 6),
    _DhcpSnoopRouteMap_Type()
)
dhcpSnoopRouteMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopRouteMap.setStatus("current")
_DhcpSnoopCounterTable_Object = MibTable
dhcpSnoopCounterTable = _DhcpSnoopCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterTable.setStatus("current")
_DhcpSnoopCounterEntry_Object = MibTableRow
dhcpSnoopCounterEntry = _DhcpSnoopCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1)
)
dhcpSnoopCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopCounterEntry.setStatus("current")
_DhcpDiscovery_Type = Counter64
_DhcpDiscovery_Object = MibTableColumn
dhcpDiscovery = _DhcpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1, 1),
    _DhcpDiscovery_Type()
)
dhcpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDiscovery.setStatus("current")
_DhcpOffer_Type = Counter64
_DhcpOffer_Object = MibTableColumn
dhcpOffer = _DhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1, 2),
    _DhcpOffer_Type()
)
dhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOffer.setStatus("current")
_DhcpRequest_Type = Counter64
_DhcpRequest_Object = MibTableColumn
dhcpRequest = _DhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1, 3),
    _DhcpRequest_Type()
)
dhcpRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRequest.setStatus("current")
_DhcpAck_Type = Counter64
_DhcpAck_Object = MibTableColumn
dhcpAck = _DhcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1, 4),
    _DhcpAck_Type()
)
dhcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAck.setStatus("current")
_DhcpAckBySnoopFull_Type = Counter64
_DhcpAckBySnoopFull_Object = MibTableColumn
dhcpAckBySnoopFull = _DhcpAckBySnoopFull_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 2, 1, 5),
    _DhcpAckBySnoopFull_Type()
)
dhcpAckBySnoopFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAckBySnoopFull.setStatus("current")
_DhcpRouteTable_Object = MibTable
dhcpRouteTable = _DhcpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3)
)
if mibBuilder.loadTexts:
    dhcpRouteTable.setStatus("current")
_DhcpRouteEntry_Object = MibTableRow
dhcpRouteEntry = _DhcpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1)
)
dhcpRouteEntry.setIndexNames(
    (0, "E5-111-MIB", "dhcpRouteIndex"),
)
if mibBuilder.loadTexts:
    dhcpRouteEntry.setStatus("current")


class _DhcpRouteIndex_Type(Integer32):
    """Custom type dhcpRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DhcpRouteIndex_Type.__name__ = "Integer32"
_DhcpRouteIndex_Object = MibTableColumn
dhcpRouteIndex = _DhcpRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1, 1),
    _DhcpRouteIndex_Type()
)
dhcpRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteIndex.setStatus("current")
_DhcpRouteVid_Type = VlanIndex
_DhcpRouteVid_Object = MibTableColumn
dhcpRouteVid = _DhcpRouteVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1, 2),
    _DhcpRouteVid_Type()
)
dhcpRouteVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteVid.setStatus("current")
_DhcpRouteIP_Type = IpAddress
_DhcpRouteIP_Object = MibTableColumn
dhcpRouteIP = _DhcpRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1, 3),
    _DhcpRouteIP_Type()
)
dhcpRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteIP.setStatus("current")
_DhcpRouteMask_Type = Integer32
_DhcpRouteMask_Object = MibTableColumn
dhcpRouteMask = _DhcpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1, 4),
    _DhcpRouteMask_Type()
)
dhcpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteMask.setStatus("current")
_DhcpRouteGwIP_Type = IpAddress
_DhcpRouteGwIP_Object = MibTableColumn
dhcpRouteGwIP = _DhcpRouteGwIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 11, 3, 1, 5),
    _DhcpRouteGwIP_Type()
)
dhcpRouteGwIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRouteGwIP.setStatus("current")
_PaepvcStats_ObjectIdentity = ObjectIdentity
paepvcStats = _PaepvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12)
)
_PaepvcSessionTable_Object = MibTable
paepvcSessionTable = _PaepvcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1)
)
if mibBuilder.loadTexts:
    paepvcSessionTable.setStatus("current")
_PaepvcSessionEntry_Object = MibTableRow
paepvcSessionEntry = _PaepvcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1)
)
paepvcSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "paepvcSessionVpi"),
    (0, "E5-111-MIB", "paepvcSessionVci"),
)
if mibBuilder.loadTexts:
    paepvcSessionEntry.setStatus("current")
_PaepvcSessionVpi_Type = Integer32
_PaepvcSessionVpi_Object = MibTableColumn
paepvcSessionVpi = _PaepvcSessionVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 1),
    _PaepvcSessionVpi_Type()
)
paepvcSessionVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVpi.setStatus("current")
_PaepvcSessionVci_Type = Integer32
_PaepvcSessionVci_Object = MibTableColumn
paepvcSessionVci = _PaepvcSessionVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 2),
    _PaepvcSessionVci_Type()
)
paepvcSessionVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionVci.setStatus("current")


class _PaepvcSessionState_Type(Integer32):
    """Custom type paepvcSessionState based on Integer32"""
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
        *(("down", 1),
          ("ppp", 3),
          ("pppoe", 2),
          ("up", 4))
    )


_PaepvcSessionState_Type.__name__ = "Integer32"
_PaepvcSessionState_Object = MibTableColumn
paepvcSessionState = _PaepvcSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 3),
    _PaepvcSessionState_Type()
)
paepvcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionState.setStatus("current")
_PaepvcSessionId_Type = Integer32
_PaepvcSessionId_Object = MibTableColumn
paepvcSessionId = _PaepvcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 4),
    _PaepvcSessionId_Type()
)
paepvcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionId.setStatus("current")
_PaepvcSessionUptime_Type = Unsigned32
_PaepvcSessionUptime_Object = MibTableColumn
paepvcSessionUptime = _PaepvcSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 5),
    _PaepvcSessionUptime_Type()
)
paepvcSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setStatus("current")
if mibBuilder.loadTexts:
    paepvcSessionUptime.setUnits("second")
_PaepvcSessionacname_Type = DisplayString
_PaepvcSessionacname_Object = MibTableColumn
paepvcSessionacname = _PaepvcSessionacname_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 6),
    _PaepvcSessionacname_Type()
)
paepvcSessionacname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionacname.setStatus("current")
_PaepvcSessionsrvcname_Type = DisplayString
_PaepvcSessionsrvcname_Object = MibTableColumn
paepvcSessionsrvcname = _PaepvcSessionsrvcname_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 1, 1, 7),
    _PaepvcSessionsrvcname_Type()
)
paepvcSessionsrvcname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcSessionsrvcname.setStatus("current")
_PaepvcCountTable_Object = MibTable
paepvcCountTable = _PaepvcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2)
)
if mibBuilder.loadTexts:
    paepvcCountTable.setStatus("current")
_PaepvcCountEntry_Object = MibTableRow
paepvcCountEntry = _PaepvcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1)
)
paepvcCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-MIB", "paepvcCountVpi"),
    (0, "E5-111-MIB", "paepvcCountVci"),
)
if mibBuilder.loadTexts:
    paepvcCountEntry.setStatus("current")
_PaepvcCountVpi_Type = Integer32
_PaepvcCountVpi_Object = MibTableColumn
paepvcCountVpi = _PaepvcCountVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 1),
    _PaepvcCountVpi_Type()
)
paepvcCountVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVpi.setStatus("current")
_PaepvcCountVci_Type = Integer32
_PaepvcCountVci_Object = MibTableColumn
paepvcCountVci = _PaepvcCountVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 2),
    _PaepvcCountVci_Type()
)
paepvcCountVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountVci.setStatus("current")
_PaepvcCountPppLcpCfgReqRx_Type = Unsigned32
_PaepvcCountPppLcpCfgReqRx_Object = MibTableColumn
paepvcCountPppLcpCfgReqRx = _PaepvcCountPppLcpCfgReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 3),
    _PaepvcCountPppLcpCfgReqRx_Type()
)
paepvcCountPppLcpCfgReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpCfgReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReqRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReqRx_Object = MibTableColumn
paepvcCountPppLcpEchoReqRx = _PaepvcCountPppLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 4),
    _PaepvcCountPppLcpEchoReqRx_Type()
)
paepvcCountPppLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReqRx.setStatus("current")
_PaepvcCountPppLcpEchoReplyRx_Type = Unsigned32
_PaepvcCountPppLcpEchoReplyRx_Object = MibTableColumn
paepvcCountPppLcpEchoReplyRx = _PaepvcCountPppLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 5),
    _PaepvcCountPppLcpEchoReplyRx_Type()
)
paepvcCountPppLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPppLcpEchoReplyRx.setStatus("current")
_PaepvcCountPadiTx_Type = Unsigned32
_PaepvcCountPadiTx_Object = MibTableColumn
paepvcCountPadiTx = _PaepvcCountPadiTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 6),
    _PaepvcCountPadiTx_Type()
)
paepvcCountPadiTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadiTx.setStatus("current")
_PaepvcCountPadoRx_Type = Unsigned32
_PaepvcCountPadoRx_Object = MibTableColumn
paepvcCountPadoRx = _PaepvcCountPadoRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 7),
    _PaepvcCountPadoRx_Type()
)
paepvcCountPadoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadoRx.setStatus("current")
_PaepvcCountPadrTx_Type = Unsigned32
_PaepvcCountPadrTx_Object = MibTableColumn
paepvcCountPadrTx = _PaepvcCountPadrTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 8),
    _PaepvcCountPadrTx_Type()
)
paepvcCountPadrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadrTx.setStatus("current")
_PaepvcCountPadsRx_Type = Unsigned32
_PaepvcCountPadsRx_Object = MibTableColumn
paepvcCountPadsRx = _PaepvcCountPadsRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 9),
    _PaepvcCountPadsRx_Type()
)
paepvcCountPadsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadsRx.setStatus("current")
_PaepvcCountPadtTx_Type = Unsigned32
_PaepvcCountPadtTx_Object = MibTableColumn
paepvcCountPadtTx = _PaepvcCountPadtTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 10),
    _PaepvcCountPadtTx_Type()
)
paepvcCountPadtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtTx.setStatus("current")
_PaepvcCountPadtRx_Type = Unsigned32
_PaepvcCountPadtRx_Object = MibTableColumn
paepvcCountPadtRx = _PaepvcCountPadtRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 11),
    _PaepvcCountPadtRx_Type()
)
paepvcCountPadtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountPadtRx.setStatus("current")
_PaepvcCountSrvcnameErrRx_Type = Unsigned32
_PaepvcCountSrvcnameErrRx_Object = MibTableColumn
paepvcCountSrvcnameErrRx = _PaepvcCountSrvcnameErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 12),
    _PaepvcCountSrvcnameErrRx_Type()
)
paepvcCountSrvcnameErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountSrvcnameErrRx.setStatus("current")
_PaepvcCountAcSystemErrRx_Type = Unsigned32
_PaepvcCountAcSystemErrRx_Object = MibTableColumn
paepvcCountAcSystemErrRx = _PaepvcCountAcSystemErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 13),
    _PaepvcCountAcSystemErrRx_Type()
)
paepvcCountAcSystemErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountAcSystemErrRx.setStatus("current")
_PaepvcCountGenericErrTx_Type = Unsigned32
_PaepvcCountGenericErrTx_Object = MibTableColumn
paepvcCountGenericErrTx = _PaepvcCountGenericErrTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 14),
    _PaepvcCountGenericErrTx_Type()
)
paepvcCountGenericErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrTx.setStatus("current")
_PaepvcCountGenericErrRx_Type = Unsigned32
_PaepvcCountGenericErrRx_Object = MibTableColumn
paepvcCountGenericErrRx = _PaepvcCountGenericErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 12, 2, 1, 15),
    _PaepvcCountGenericErrRx_Type()
)
paepvcCountGenericErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcCountGenericErrRx.setStatus("current")
_MacStats_ObjectIdentity = ObjectIdentity
macStats = _MacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13)
)
_MacDisplayTarget_Type = Integer32
_MacDisplayTarget_Object = MibScalar
macDisplayTarget = _MacDisplayTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 1),
    _MacDisplayTarget_Type()
)
macDisplayTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macDisplayTarget.setStatus("current")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("current")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 2, 1)
)
macEntry.setIndexNames(
    (0, "E5-111-MIB", "macAddress"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 2, 1, 1),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacPort_Type = Integer32
_MacPort_Object = MibTableColumn
macPort = _MacPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 2, 1, 2),
    _MacPort_Type()
)
macPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macPort.setStatus("current")


class _MacStatus_Type(Integer32):
    """Custom type macStatus based on Integer32"""
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


_MacStatus_Type.__name__ = "Integer32"
_MacStatus_Object = MibTableColumn
macStatus = _MacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 13, 2, 1, 3),
    _MacStatus_Type()
)
macStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macStatus.setStatus("current")
_IpbpvcStats_ObjectIdentity = ObjectIdentity
ipbpvcStats = _IpbpvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14)
)
_ArpproxyTable_Object = MibTable
arpproxyTable = _ArpproxyTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1)
)
if mibBuilder.loadTexts:
    arpproxyTable.setStatus("current")
_ArpproxyEntry_Object = MibTableRow
arpproxyEntry = _ArpproxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1)
)
arpproxyEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "arpproxyIp"),
)
if mibBuilder.loadTexts:
    arpproxyEntry.setStatus("current")
_ArpproxyIp_Type = IpAddress
_ArpproxyIp_Object = MibTableColumn
arpproxyIp = _ArpproxyIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 1),
    _ArpproxyIp_Type()
)
arpproxyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyIp.setStatus("current")
_ArpproxyMac_Type = MacAddress
_ArpproxyMac_Object = MibTableColumn
arpproxyMac = _ArpproxyMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 2),
    _ArpproxyMac_Type()
)
arpproxyMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyMac.setStatus("current")
_ArpproxyIfIndex_Type = Integer32
_ArpproxyIfIndex_Object = MibTableColumn
arpproxyIfIndex = _ArpproxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 3),
    _ArpproxyIfIndex_Type()
)
arpproxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyIfIndex.setStatus("current")
_ArpproxyVpi_Type = Integer32
_ArpproxyVpi_Object = MibTableColumn
arpproxyVpi = _ArpproxyVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 4),
    _ArpproxyVpi_Type()
)
arpproxyVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyVpi.setStatus("current")
_ArpproxyVci_Type = Integer32
_ArpproxyVci_Object = MibTableColumn
arpproxyVci = _ArpproxyVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 5),
    _ArpproxyVci_Type()
)
arpproxyVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyVci.setStatus("current")
_ArpproxyInterfaceIp_Type = IpAddress
_ArpproxyInterfaceIp_Object = MibTableColumn
arpproxyInterfaceIp = _ArpproxyInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 6),
    _ArpproxyInterfaceIp_Type()
)
arpproxyInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceIp.setStatus("current")
_ArpproxyInterfaceMask_Type = Integer32
_ArpproxyInterfaceMask_Object = MibTableColumn
arpproxyInterfaceMask = _ArpproxyInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 7),
    _ArpproxyInterfaceMask_Type()
)
arpproxyInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceMask.setStatus("current")
_ArpproxyInterfaceVid_Type = VlanIndex
_ArpproxyInterfaceVid_Object = MibTableColumn
arpproxyInterfaceVid = _ArpproxyInterfaceVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 8),
    _ArpproxyInterfaceVid_Type()
)
arpproxyInterfaceVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyInterfaceVid.setStatus("current")


class _ArpproxyDhcpIp_Type(Integer32):
    """Custom type arpproxyDhcpIp based on Integer32"""
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


_ArpproxyDhcpIp_Type.__name__ = "Integer32"
_ArpproxyDhcpIp_Object = MibTableColumn
arpproxyDhcpIp = _ArpproxyDhcpIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 9),
    _ArpproxyDhcpIp_Type()
)
arpproxyDhcpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyDhcpIp.setStatus("current")


class _ArpproxyType_Type(Integer32):
    """Custom type arpproxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_ArpproxyType_Type.__name__ = "Integer32"
_ArpproxyType_Object = MibTableColumn
arpproxyType = _ArpproxyType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 1, 1, 10),
    _ArpproxyType_Type()
)
arpproxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpproxyType.setStatus("current")
_IpbpvcIfDynamicTable_Object = MibTable
ipbpvcIfDynamicTable = _IpbpvcIfDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2)
)
if mibBuilder.loadTexts:
    ipbpvcIfDynamicTable.setStatus("current")
_IpbpvcIfDynamicEntry_Object = MibTableRow
ipbpvcIfDynamicEntry = _IpbpvcIfDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1)
)
ipbpvcIfDynamicEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcIfDynamicIp"),
    (0, "E5-111-MIB", "ipbpvcIfDynamicMask"),
    (0, "E5-111-MIB", "ipbpvcDomainVlanId"),
)
if mibBuilder.loadTexts:
    ipbpvcIfDynamicEntry.setStatus("current")
_IpbpvcIfDynamicIp_Type = IpAddress
_IpbpvcIfDynamicIp_Object = MibTableColumn
ipbpvcIfDynamicIp = _IpbpvcIfDynamicIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1, 1),
    _IpbpvcIfDynamicIp_Type()
)
ipbpvcIfDynamicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicIp.setStatus("current")
_IpbpvcIfDynamicMask_Type = Integer32
_IpbpvcIfDynamicMask_Object = MibTableColumn
ipbpvcIfDynamicMask = _IpbpvcIfDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1, 2),
    _IpbpvcIfDynamicMask_Type()
)
ipbpvcIfDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicMask.setStatus("current")
_IpbpvcIfDynamicIfIndex_Type = Integer32
_IpbpvcIfDynamicIfIndex_Object = MibTableColumn
ipbpvcIfDynamicIfIndex = _IpbpvcIfDynamicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1, 3),
    _IpbpvcIfDynamicIfIndex_Type()
)
ipbpvcIfDynamicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicIfIndex.setStatus("current")
_IpbpvcIfDynamicVpi_Type = Integer32
_IpbpvcIfDynamicVpi_Object = MibTableColumn
ipbpvcIfDynamicVpi = _IpbpvcIfDynamicVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1, 4),
    _IpbpvcIfDynamicVpi_Type()
)
ipbpvcIfDynamicVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicVpi.setStatus("current")
_IpbpvcIfDynamicVci_Type = Integer32
_IpbpvcIfDynamicVci_Object = MibTableColumn
ipbpvcIfDynamicVci = _IpbpvcIfDynamicVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 2, 1, 5),
    _IpbpvcIfDynamicVci_Type()
)
ipbpvcIfDynamicVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcIfDynamicVci.setStatus("current")
_IpbpvcRouteDynamicTable_Object = MibTable
ipbpvcRouteDynamicTable = _IpbpvcRouteDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3)
)
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicTable.setStatus("current")
_IpbpvcRouteDynamicEntry_Object = MibTableRow
ipbpvcRouteDynamicEntry = _IpbpvcRouteDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1)
)
ipbpvcRouteDynamicEntry.setIndexNames(
    (0, "E5-111-MIB", "ipbpvcDomainName"),
    (0, "E5-111-MIB", "ipbpvcRouteDynamicType"),
    (0, "E5-111-MIB", "ipbpvcRouteDynamicIp"),
    (0, "E5-111-MIB", "ipbpvcRouteDynamicMask"),
)
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicEntry.setStatus("current")


class _IpbpvcRouteDynamicType_Type(Integer32):
    """Custom type ipbpvcRouteDynamicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_IpbpvcRouteDynamicType_Type.__name__ = "Integer32"
_IpbpvcRouteDynamicType_Object = MibTableColumn
ipbpvcRouteDynamicType = _IpbpvcRouteDynamicType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 1),
    _IpbpvcRouteDynamicType_Type()
)
ipbpvcRouteDynamicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicType.setStatus("current")
_IpbpvcRouteDynamicIp_Type = IpAddress
_IpbpvcRouteDynamicIp_Object = MibTableColumn
ipbpvcRouteDynamicIp = _IpbpvcRouteDynamicIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 2),
    _IpbpvcRouteDynamicIp_Type()
)
ipbpvcRouteDynamicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicIp.setStatus("current")
_IpbpvcRouteDynamicMask_Type = Integer32
_IpbpvcRouteDynamicMask_Object = MibTableColumn
ipbpvcRouteDynamicMask = _IpbpvcRouteDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 3),
    _IpbpvcRouteDynamicMask_Type()
)
ipbpvcRouteDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicMask.setStatus("current")
_IpbpvcRouteDynamicNextHop_Type = IpAddress
_IpbpvcRouteDynamicNextHop_Object = MibTableColumn
ipbpvcRouteDynamicNextHop = _IpbpvcRouteDynamicNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 4),
    _IpbpvcRouteDynamicNextHop_Type()
)
ipbpvcRouteDynamicNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicNextHop.setStatus("current")
_IpbpvcRouteDynamicMetric_Type = Integer32
_IpbpvcRouteDynamicMetric_Object = MibTableColumn
ipbpvcRouteDynamicMetric = _IpbpvcRouteDynamicMetric_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 5),
    _IpbpvcRouteDynamicMetric_Type()
)
ipbpvcRouteDynamicMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicMetric.setStatus("current")
_IpbpvcRouteDynamicPriority_Type = Integer32
_IpbpvcRouteDynamicPriority_Object = MibTableColumn
ipbpvcRouteDynamicPriority = _IpbpvcRouteDynamicPriority_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 14, 3, 1, 6),
    _IpbpvcRouteDynamicPriority_Type()
)
ipbpvcRouteDynamicPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipbpvcRouteDynamicPriority.setStatus("current")
_VoipStats_ObjectIdentity = ObjectIdentity
voipStats = _VoipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15)
)
_VoipLineStatusTable_Object = MibTable
voipLineStatusTable = _VoipLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 1)
)
if mibBuilder.loadTexts:
    voipLineStatusTable.setStatus("current")
_VoipLineStatusEntry_Object = MibTableRow
voipLineStatusEntry = _VoipLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 1, 1)
)
voipLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipLineStatusEntry.setStatus("current")


class _VoipLineStatusPhoneStatus_Type(Integer32):
    """Custom type voipLineStatusPhoneStatus based on Integer32"""
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
        *(("bad", 8),
          ("disabled", 1),
          ("fault", 7),
          ("offHook", 3),
          ("onHook", 2),
          ("powerCutDown", 5),
          ("ringing", 4),
          ("testing", 6),
          ("uninitialized", 9))
    )


_VoipLineStatusPhoneStatus_Type.__name__ = "Integer32"
_VoipLineStatusPhoneStatus_Object = MibTableColumn
voipLineStatusPhoneStatus = _VoipLineStatusPhoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 1, 1, 1),
    _VoipLineStatusPhoneStatus_Type()
)
voipLineStatusPhoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineStatusPhoneStatus.setStatus("current")


class _VoipLineStatusServiceStatus_Type(Integer32):
    """Custom type voipLineStatusServiceStatus based on Integer32"""
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
        *(("alertingOffHook", 13),
          ("conversationCallee", 8),
          ("conversationCaller", 7),
          ("dialingOut", 5),
          ("dialingTimeout", 12),
          ("disabled", 1),
          ("faxModemCallee", 10),
          ("faxModemCaller", 9),
          ("idle", 3),
          ("outOfService", 2),
          ("powerCutDown", 14),
          ("ringing", 6),
          ("waitingForDialing", 4),
          ("waitingForOnHook", 11))
    )


_VoipLineStatusServiceStatus_Type.__name__ = "Integer32"
_VoipLineStatusServiceStatus_Object = MibTableColumn
voipLineStatusServiceStatus = _VoipLineStatusServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 1, 1, 2),
    _VoipLineStatusServiceStatus_Type()
)
voipLineStatusServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineStatusServiceStatus.setStatus("current")
_VoipLineInfoTable_Object = MibTable
voipLineInfoTable = _VoipLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2)
)
if mibBuilder.loadTexts:
    voipLineInfoTable.setStatus("current")
_VoipLineInfoEntry_Object = MibTableRow
voipLineInfoEntry = _VoipLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1)
)
voipLineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voipLineInfoEntry.setStatus("current")
_VoipLineInfoSipLocalUri_Type = OctetString
_VoipLineInfoSipLocalUri_Object = MibTableColumn
voipLineInfoSipLocalUri = _VoipLineInfoSipLocalUri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 1),
    _VoipLineInfoSipLocalUri_Type()
)
voipLineInfoSipLocalUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipLocalUri.setStatus("current")
_VoipLineInfoSipRemoteUri_Type = OctetString
_VoipLineInfoSipRemoteUri_Object = MibTableColumn
voipLineInfoSipRemoteUri = _VoipLineInfoSipRemoteUri_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 2),
    _VoipLineInfoSipRemoteUri_Type()
)
voipLineInfoSipRemoteUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipRemoteUri.setStatus("current")
_VoipLineInfoRtpTxCodecType_Type = OctetString
_VoipLineInfoRtpTxCodecType_Object = MibTableColumn
voipLineInfoRtpTxCodecType = _VoipLineInfoRtpTxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 3),
    _VoipLineInfoRtpTxCodecType_Type()
)
voipLineInfoRtpTxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxCodecType.setStatus("current")
_VoipLineInfoRtpRxCodecType_Type = OctetString
_VoipLineInfoRtpRxCodecType_Object = MibTableColumn
voipLineInfoRtpRxCodecType = _VoipLineInfoRtpRxCodecType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 4),
    _VoipLineInfoRtpRxCodecType_Type()
)
voipLineInfoRtpRxCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxCodecType.setStatus("current")
_VoipLineInfoRtpTxPt_Type = Integer32
_VoipLineInfoRtpTxPt_Object = MibTableColumn
voipLineInfoRtpTxPt = _VoipLineInfoRtpTxPt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 5),
    _VoipLineInfoRtpTxPt_Type()
)
voipLineInfoRtpTxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxPt.setStatus("current")
_VoipLineInfoRtpRxPt_Type = Integer32
_VoipLineInfoRtpRxPt_Object = MibTableColumn
voipLineInfoRtpRxPt = _VoipLineInfoRtpRxPt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 6),
    _VoipLineInfoRtpRxPt_Type()
)
voipLineInfoRtpRxPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxPt.setStatus("current")
_VoipLineInfoRtpLocalIp_Type = IpAddress
_VoipLineInfoRtpLocalIp_Object = MibTableColumn
voipLineInfoRtpLocalIp = _VoipLineInfoRtpLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 7),
    _VoipLineInfoRtpLocalIp_Type()
)
voipLineInfoRtpLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalIp.setStatus("current")
_VoipLineInfoRtpRemoteIp_Type = IpAddress
_VoipLineInfoRtpRemoteIp_Object = MibTableColumn
voipLineInfoRtpRemoteIp = _VoipLineInfoRtpRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 8),
    _VoipLineInfoRtpRemoteIp_Type()
)
voipLineInfoRtpRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemoteIp.setStatus("current")
_VoipLineInfoRtpLocalPort_Type = Integer32
_VoipLineInfoRtpLocalPort_Object = MibTableColumn
voipLineInfoRtpLocalPort = _VoipLineInfoRtpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 9),
    _VoipLineInfoRtpLocalPort_Type()
)
voipLineInfoRtpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalPort.setStatus("current")
_VoipLineInfoRtpRemotePort_Type = Integer32
_VoipLineInfoRtpRemotePort_Object = MibTableColumn
voipLineInfoRtpRemotePort = _VoipLineInfoRtpRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 10),
    _VoipLineInfoRtpRemotePort_Type()
)
voipLineInfoRtpRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemotePort.setStatus("current")
_VoipLineInfoSipLocalUri2_Type = OctetString
_VoipLineInfoSipLocalUri2_Object = MibTableColumn
voipLineInfoSipLocalUri2 = _VoipLineInfoSipLocalUri2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 11),
    _VoipLineInfoSipLocalUri2_Type()
)
voipLineInfoSipLocalUri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipLocalUri2.setStatus("current")
_VoipLineInfoSipRemoteUri2_Type = OctetString
_VoipLineInfoSipRemoteUri2_Object = MibTableColumn
voipLineInfoSipRemoteUri2 = _VoipLineInfoSipRemoteUri2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 12),
    _VoipLineInfoSipRemoteUri2_Type()
)
voipLineInfoSipRemoteUri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoSipRemoteUri2.setStatus("current")
_VoipLineInfoRtpTxCodecType2_Type = OctetString
_VoipLineInfoRtpTxCodecType2_Object = MibTableColumn
voipLineInfoRtpTxCodecType2 = _VoipLineInfoRtpTxCodecType2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 13),
    _VoipLineInfoRtpTxCodecType2_Type()
)
voipLineInfoRtpTxCodecType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxCodecType2.setStatus("current")
_VoipLineInfoRtpRxCodecType2_Type = OctetString
_VoipLineInfoRtpRxCodecType2_Object = MibTableColumn
voipLineInfoRtpRxCodecType2 = _VoipLineInfoRtpRxCodecType2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 14),
    _VoipLineInfoRtpRxCodecType2_Type()
)
voipLineInfoRtpRxCodecType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxCodecType2.setStatus("current")
_VoipLineInfoRtpTxPt2_Type = Integer32
_VoipLineInfoRtpTxPt2_Object = MibTableColumn
voipLineInfoRtpTxPt2 = _VoipLineInfoRtpTxPt2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 15),
    _VoipLineInfoRtpTxPt2_Type()
)
voipLineInfoRtpTxPt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpTxPt2.setStatus("current")
_VoipLineInfoRtpRxPt2_Type = Integer32
_VoipLineInfoRtpRxPt2_Object = MibTableColumn
voipLineInfoRtpRxPt2 = _VoipLineInfoRtpRxPt2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 16),
    _VoipLineInfoRtpRxPt2_Type()
)
voipLineInfoRtpRxPt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRxPt2.setStatus("current")
_VoipLineInfoRtpLocalIp2_Type = IpAddress
_VoipLineInfoRtpLocalIp2_Object = MibTableColumn
voipLineInfoRtpLocalIp2 = _VoipLineInfoRtpLocalIp2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 17),
    _VoipLineInfoRtpLocalIp2_Type()
)
voipLineInfoRtpLocalIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalIp2.setStatus("current")
_VoipLineInfoRtpRemoteIp2_Type = IpAddress
_VoipLineInfoRtpRemoteIp2_Object = MibTableColumn
voipLineInfoRtpRemoteIp2 = _VoipLineInfoRtpRemoteIp2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 18),
    _VoipLineInfoRtpRemoteIp2_Type()
)
voipLineInfoRtpRemoteIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemoteIp2.setStatus("current")
_VoipLineInfoRtpLocalPort2_Type = Integer32
_VoipLineInfoRtpLocalPort2_Object = MibTableColumn
voipLineInfoRtpLocalPort2 = _VoipLineInfoRtpLocalPort2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 19),
    _VoipLineInfoRtpLocalPort2_Type()
)
voipLineInfoRtpLocalPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpLocalPort2.setStatus("current")
_VoipLineInfoRtpRemotePort2_Type = Integer32
_VoipLineInfoRtpRemotePort2_Object = MibTableColumn
voipLineInfoRtpRemotePort2 = _VoipLineInfoRtpRemotePort2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 2, 1, 20),
    _VoipLineInfoRtpRemotePort2_Type()
)
voipLineInfoRtpRemotePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipLineInfoRtpRemotePort2.setStatus("current")
_VoipH248Status_ObjectIdentity = ObjectIdentity
voipH248Status = _VoipH248Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 3)
)
_VoipH248StatusMgName_Type = OctetString
_VoipH248StatusMgName_Object = MibScalar
voipH248StatusMgName = _VoipH248StatusMgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 3, 1),
    _VoipH248StatusMgName_Type()
)
voipH248StatusMgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatusMgName.setStatus("current")


class _VoipH248StatusMgStatus_Type(Integer32):
    """Custom type voipH248StatusMgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 7),
          ("disconnected", 6),
          ("registered", 3),
          ("registering", 2),
          ("unregistered", 5),
          ("unregistering", 4))
    )


_VoipH248StatusMgStatus_Type.__name__ = "Integer32"
_VoipH248StatusMgStatus_Object = MibScalar
voipH248StatusMgStatus = _VoipH248StatusMgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 3, 2),
    _VoipH248StatusMgStatus_Type()
)
voipH248StatusMgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipH248StatusMgStatus.setStatus("current")
_VoipActiveCallStat_ObjectIdentity = ObjectIdentity
voipActiveCallStat = _VoipActiveCallStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 4)
)
_VoipActiveCallStatCurrentActiveCalls_Type = Integer32
_VoipActiveCallStatCurrentActiveCalls_Object = MibScalar
voipActiveCallStatCurrentActiveCalls = _VoipActiveCallStatCurrentActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 4, 1),
    _VoipActiveCallStatCurrentActiveCalls_Type()
)
voipActiveCallStatCurrentActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipActiveCallStatCurrentActiveCalls.setStatus("current")
_VoipActiveCallStatFailAttempts_Type = Integer32
_VoipActiveCallStatFailAttempts_Object = MibScalar
voipActiveCallStatFailAttempts = _VoipActiveCallStatFailAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 15, 4, 2),
    _VoipActiveCallStatFailAttempts_Type()
)
voipActiveCallStatFailAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipActiveCallStatFailAttempts.setStatus("current")
_MacffStats_ObjectIdentity = ObjectIdentity
macffStats = _MacffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16)
)
_MacFfStatsTable_Object = MibTable
macFfStatsTable = _MacFfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1)
)
if mibBuilder.loadTexts:
    macFfStatsTable.setStatus("current")
_MacFfStatsEntry_Object = MibTableRow
macFfStatsEntry = _MacFfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1)
)
macFfStatsEntry.setIndexNames(
    (0, "E5-111-MIB", "macFfStatsIndex"),
)
if mibBuilder.loadTexts:
    macFfStatsEntry.setStatus("current")
_MacFfStatsIndex_Type = Integer32
_MacFfStatsIndex_Object = MibTableColumn
macFfStatsIndex = _MacFfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1, 1),
    _MacFfStatsIndex_Type()
)
macFfStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsIndex.setStatus("current")
_MacFfStatsVid_Type = VlanIndex
_MacFfStatsVid_Object = MibTableColumn
macFfStatsVid = _MacFfStatsVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1, 2),
    _MacFfStatsVid_Type()
)
macFfStatsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsVid.setStatus("current")
_MacFfStatsArIP_Type = IpAddress
_MacFfStatsArIP_Object = MibTableColumn
macFfStatsArIP = _MacFfStatsArIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1, 3),
    _MacFfStatsArIP_Type()
)
macFfStatsArIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsArIP.setStatus("current")
_MacFfStatsSrcIP_Type = IpAddress
_MacFfStatsSrcIP_Object = MibTableColumn
macFfStatsSrcIP = _MacFfStatsSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1, 4),
    _MacFfStatsSrcIP_Type()
)
macFfStatsSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsSrcIP.setStatus("current")
_MacFfStatsSrcMask_Type = Integer32
_MacFfStatsSrcMask_Object = MibTableColumn
macFfStatsSrcMask = _MacFfStatsSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 1, 1, 5),
    _MacFfStatsSrcMask_Type()
)
macFfStatsSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfStatsSrcMask.setStatus("current")
_MacFfArpTable_Object = MibTable
macFfArpTable = _MacFfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2)
)
if mibBuilder.loadTexts:
    macFfArpTable.setStatus("current")
_MacFfArpEntry_Object = MibTableRow
macFfArpEntry = _MacFfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2, 1)
)
macFfArpEntry.setIndexNames(
    (0, "E5-111-MIB", "macFfArpVid"),
    (0, "E5-111-MIB", "macFfArpIP"),
)
if mibBuilder.loadTexts:
    macFfArpEntry.setStatus("current")
_MacFfArpVid_Type = VlanIndex
_MacFfArpVid_Object = MibTableColumn
macFfArpVid = _MacFfArpVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2, 1, 1),
    _MacFfArpVid_Type()
)
macFfArpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpVid.setStatus("current")
_MacFfArpIP_Type = IpAddress
_MacFfArpIP_Object = MibTableColumn
macFfArpIP = _MacFfArpIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2, 1, 2),
    _MacFfArpIP_Type()
)
macFfArpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpIP.setStatus("current")
_MacFfArpPort_Type = Integer32
_MacFfArpPort_Object = MibTableColumn
macFfArpPort = _MacFfArpPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2, 1, 3),
    _MacFfArpPort_Type()
)
macFfArpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpPort.setStatus("current")
_MacFfArpMac_Type = PhysAddress
_MacFfArpMac_Object = MibTableColumn
macFfArpMac = _MacFfArpMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 2, 1, 4),
    _MacFfArpMac_Type()
)
macFfArpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpMac.setStatus("current")
_MacFfArpCounterTable_Object = MibTable
macFfArpCounterTable = _MacFfArpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3)
)
if mibBuilder.loadTexts:
    macFfArpCounterTable.setStatus("current")
_MacFfArpCounterEntry_Object = MibTableRow
macFfArpCounterEntry = _MacFfArpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1)
)
macFfArpCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macFfArpCounterEntry.setStatus("current")
_MacFfArpCounterRequestTX_Type = Counter32
_MacFfArpCounterRequestTX_Object = MibTableColumn
macFfArpCounterRequestTX = _MacFfArpCounterRequestTX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 1),
    _MacFfArpCounterRequestTX_Type()
)
macFfArpCounterRequestTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestTX.setStatus("current")
_MacFfArpCounterRequestRX_Type = Counter32
_MacFfArpCounterRequestRX_Object = MibTableColumn
macFfArpCounterRequestRX = _MacFfArpCounterRequestRX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 2),
    _MacFfArpCounterRequestRX_Type()
)
macFfArpCounterRequestRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestRX.setStatus("current")
_MacFfArpCounterRequestRXDrop_Type = Counter32
_MacFfArpCounterRequestRXDrop_Object = MibTableColumn
macFfArpCounterRequestRXDrop = _MacFfArpCounterRequestRXDrop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 3),
    _MacFfArpCounterRequestRXDrop_Type()
)
macFfArpCounterRequestRXDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterRequestRXDrop.setStatus("current")
_MacFfArpCounterReplyTX_Type = Counter32
_MacFfArpCounterReplyTX_Object = MibTableColumn
macFfArpCounterReplyTX = _MacFfArpCounterReplyTX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 4),
    _MacFfArpCounterReplyTX_Type()
)
macFfArpCounterReplyTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyTX.setStatus("current")
_MacFfArpCounterReplyRX_Type = Counter32
_MacFfArpCounterReplyRX_Object = MibTableColumn
macFfArpCounterReplyRX = _MacFfArpCounterReplyRX_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 5),
    _MacFfArpCounterReplyRX_Type()
)
macFfArpCounterReplyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyRX.setStatus("current")
_MacFfArpCounterReplyRXDrop_Type = Counter32
_MacFfArpCounterReplyRXDrop_Object = MibTableColumn
macFfArpCounterReplyRXDrop = _MacFfArpCounterReplyRXDrop_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 16, 3, 1, 6),
    _MacFfArpCounterReplyRXDrop_Type()
)
macFfArpCounterReplyRXDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFfArpCounterReplyRXDrop.setStatus("current")
_EnetStats_ObjectIdentity = ObjectIdentity
enetStats = _EnetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17)
)
_EnetSfpInfoTable_Object = MibTable
enetSfpInfoTable = _EnetSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2)
)
if mibBuilder.loadTexts:
    enetSfpInfoTable.setStatus("current")
_EnetSfpInfoEntry_Object = MibTableRow
enetSfpInfoEntry = _EnetSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1)
)
enetSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    enetSfpInfoEntry.setStatus("current")


class _EnetSfpInfoTxpower_Type(Integer32):
    """Custom type enetSfpInfoTxpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnetSfpInfoTxpower_Type.__name__ = "Integer32"
_EnetSfpInfoTxpower_Object = MibTableColumn
enetSfpInfoTxpower = _EnetSfpInfoTxpower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1, 1),
    _EnetSfpInfoTxpower_Type()
)
enetSfpInfoTxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTxpower.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTxpower.setUnits("10^-4 mW")


class _EnetSfpInfoRxpower_Type(Integer32):
    """Custom type enetSfpInfoRxpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnetSfpInfoRxpower_Type.__name__ = "Integer32"
_EnetSfpInfoRxpower_Object = MibTableColumn
enetSfpInfoRxpower = _EnetSfpInfoRxpower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1, 2),
    _EnetSfpInfoRxpower_Type()
)
enetSfpInfoRxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoRxpower.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoRxpower.setUnits("10^-4 C")


class _EnetSfpInfoTemperature_Type(Integer32):
    """Custom type enetSfpInfoTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_EnetSfpInfoTemperature_Type.__name__ = "Integer32"
_EnetSfpInfoTemperature_Object = MibTableColumn
enetSfpInfoTemperature = _EnetSfpInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1, 3),
    _EnetSfpInfoTemperature_Type()
)
enetSfpInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTemperature.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTemperature.setUnits("10^-4 C")


class _EnetSfpInfoTxBias_Type(Integer32):
    """Custom type enetSfpInfoTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131000),
    )


_EnetSfpInfoTxBias_Type.__name__ = "Integer32"
_EnetSfpInfoTxBias_Object = MibTableColumn
enetSfpInfoTxBias = _EnetSfpInfoTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1, 4),
    _EnetSfpInfoTxBias_Type()
)
enetSfpInfoTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoTxBias.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoTxBias.setUnits("10^-3 mA")


class _EnetSfpInfoVoltage_Type(Integer32):
    """Custom type enetSfpInfoVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_EnetSfpInfoVoltage_Type.__name__ = "Integer32"
_EnetSfpInfoVoltage_Object = MibTableColumn
enetSfpInfoVoltage = _EnetSfpInfoVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 17, 2, 1, 5),
    _EnetSfpInfoVoltage_Type()
)
enetSfpInfoVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSfpInfoVoltage.setStatus("current")
if mibBuilder.loadTexts:
    enetSfpInfoVoltage.setUnits("0.1mV")
_AdslStats_ObjectIdentity = ObjectIdentity
adslStats = _AdslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 18)
)
_AdslPortUtilTable_Object = MibTable
adslPortUtilTable = _AdslPortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 18, 1)
)
if mibBuilder.loadTexts:
    adslPortUtilTable.setStatus("current")
_AdslPortUtilEntry_Object = MibTableRow
adslPortUtilEntry = _AdslPortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 18, 1, 1)
)
adslPortUtilEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adslPortUtilEntry.setStatus("current")


class _AdslPortUtilTx_Type(Integer32):
    """Custom type adslPortUtilTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslPortUtilTx_Type.__name__ = "Integer32"
_AdslPortUtilTx_Object = MibTableColumn
adslPortUtilTx = _AdslPortUtilTx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 18, 1, 1, 1),
    _AdslPortUtilTx_Type()
)
adslPortUtilTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPortUtilTx.setStatus("current")


class _AdslPortUtilRx_Type(Integer32):
    """Custom type adslPortUtilRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdslPortUtilRx_Type.__name__ = "Integer32"
_AdslPortUtilRx_Object = MibTableColumn
adslPortUtilRx = _AdslPortUtilRx_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 13, 18, 1, 1, 2),
    _AdslPortUtilRx_Type()
)
adslPortUtilRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPortUtilRx.setStatus("current")
_Clear_ObjectIdentity = ObjectIdentity
clear = _Clear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 14)
)
_CounterClearTarget_Type = OctetString
_CounterClearTarget_Object = MibScalar
counterClearTarget = _CounterClearTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 14, 1),
    _CounterClearTarget_Type()
)
counterClearTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearTarget.setStatus("current")
_CounterClearOps_Type = Integer32
_CounterClearOps_Object = MibScalar
counterClearOps = _CounterClearOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 14, 2),
    _CounterClearOps_Type()
)
counterClearOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearOps.setStatus("current")


class _CounterClearVpi_Type(Integer32):
    """Custom type counterClearVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CounterClearVpi_Type.__name__ = "Integer32"
_CounterClearVpi_Object = MibScalar
counterClearVpi = _CounterClearVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 14, 3),
    _CounterClearVpi_Type()
)
counterClearVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVpi.setStatus("current")


class _CounterClearVci_Type(Integer32):
    """Custom type counterClearVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CounterClearVci_Type.__name__ = "Integer32"
_CounterClearVci_Object = MibScalar
counterClearVci = _CounterClearVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 14, 4),
    _CounterClearVci_Type()
)
counterClearVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearVci.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16)
)
_VoipArp_ObjectIdentity = ObjectIdentity
voipArp = _VoipArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1)
)
_VoipArpFlushOps_Type = Integer32
_VoipArpFlushOps_Object = MibScalar
voipArpFlushOps = _VoipArpFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1, 1),
    _VoipArpFlushOps_Type()
)
voipArpFlushOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipArpFlushOps.setStatus("current")
_VoipArpShowTable_Object = MibTable
voipArpShowTable = _VoipArpShowTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1, 2)
)
if mibBuilder.loadTexts:
    voipArpShowTable.setStatus("current")
_VoipArpShowEntry_Object = MibTableRow
voipArpShowEntry = _VoipArpShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1, 2, 1)
)
voipArpShowEntry.setIndexNames(
    (0, "E5-111-MIB", "voipArpShowIp"),
)
if mibBuilder.loadTexts:
    voipArpShowEntry.setStatus("current")
_VoipArpShowIp_Type = IpAddress
_VoipArpShowIp_Object = MibTableColumn
voipArpShowIp = _VoipArpShowIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1, 2, 1, 1),
    _VoipArpShowIp_Type()
)
voipArpShowIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipArpShowIp.setStatus("current")
_VoipArpShowMac_Type = PhysAddress
_VoipArpShowMac_Object = MibTableColumn
voipArpShowMac = _VoipArpShowMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 1, 2, 1, 2),
    _VoipArpShowMac_Type()
)
voipArpShowMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipArpShowMac.setStatus("current")
_VoipSip_ObjectIdentity = ObjectIdentity
voipSip = _VoipSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2)
)
_MaxNumOfVoipNumberPlan_Type = Integer32
_MaxNumOfVoipNumberPlan_Object = MibScalar
maxNumOfVoipNumberPlan = _MaxNumOfVoipNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 1),
    _MaxNumOfVoipNumberPlan_Type()
)
maxNumOfVoipNumberPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipNumberPlan.setStatus("current")
_VoipNumberPlanTable_Object = MibTable
voipNumberPlanTable = _VoipNumberPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2)
)
if mibBuilder.loadTexts:
    voipNumberPlanTable.setStatus("current")
_VoipNumberPlanEntry_Object = MibTableRow
voipNumberPlanEntry = _VoipNumberPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1)
)
voipNumberPlanEntry.setIndexNames(
    (0, "E5-111-MIB", "voipNumberPlanName"),
    (0, "E5-111-MIB", "voipNumberPlanIndex"),
)
if mibBuilder.loadTexts:
    voipNumberPlanEntry.setStatus("current")


class _VoipNumberPlanName_Type(DisplayString):
    """Custom type voipNumberPlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipNumberPlanName_Type.__name__ = "DisplayString"
_VoipNumberPlanName_Object = MibTableColumn
voipNumberPlanName = _VoipNumberPlanName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1, 1),
    _VoipNumberPlanName_Type()
)
voipNumberPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipNumberPlanName.setStatus("current")


class _VoipNumberPlanIndex_Type(Integer32):
    """Custom type voipNumberPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoipNumberPlanIndex_Type.__name__ = "Integer32"
_VoipNumberPlanIndex_Object = MibTableColumn
voipNumberPlanIndex = _VoipNumberPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1, 2),
    _VoipNumberPlanIndex_Type()
)
voipNumberPlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipNumberPlanIndex.setStatus("current")
_VoipNumberPlanPattern_Type = OctetString
_VoipNumberPlanPattern_Object = MibTableColumn
voipNumberPlanPattern = _VoipNumberPlanPattern_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1, 3),
    _VoipNumberPlanPattern_Type()
)
voipNumberPlanPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanPattern.setStatus("current")
_VoipNumberPlanRule_Type = OctetString
_VoipNumberPlanRule_Object = MibTableColumn
voipNumberPlanRule = _VoipNumberPlanRule_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1, 4),
    _VoipNumberPlanRule_Type()
)
voipNumberPlanRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanRule.setStatus("current")
_VoipNumberPlanRowStatus_Type = RowStatus
_VoipNumberPlanRowStatus_Object = MibTableColumn
voipNumberPlanRowStatus = _VoipNumberPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 2, 1, 5),
    _VoipNumberPlanRowStatus_Type()
)
voipNumberPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanRowStatus.setStatus("current")
_VoipNumberPlanDftTable_Object = MibTable
voipNumberPlanDftTable = _VoipNumberPlanDftTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 3)
)
if mibBuilder.loadTexts:
    voipNumberPlanDftTable.setStatus("current")
_VoipNumberPlanDftEntry_Object = MibTableRow
voipNumberPlanDftEntry = _VoipNumberPlanDftEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 3, 1)
)
voipNumberPlanDftEntry.setIndexNames(
    (0, "E5-111-MIB", "voipNumberPlanName"),
)
if mibBuilder.loadTexts:
    voipNumberPlanDftEntry.setStatus("current")
_VoipNumberPlanDftRule_Type = OctetString
_VoipNumberPlanDftRule_Object = MibTableColumn
voipNumberPlanDftRule = _VoipNumberPlanDftRule_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 3, 1, 1),
    _VoipNumberPlanDftRule_Type()
)
voipNumberPlanDftRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipNumberPlanDftRule.setStatus("current")
_DigitSetup_ObjectIdentity = ObjectIdentity
digitSetup = _DigitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4)
)
_TimeoutSetup_ObjectIdentity = ObjectIdentity
timeoutSetup = _TimeoutSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4, 1)
)


class _InitialTimeout_Type(Integer32):
    """Custom type initialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_InitialTimeout_Type.__name__ = "Integer32"
_InitialTimeout_Object = MibScalar
initialTimeout = _InitialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4, 1, 1),
    _InitialTimeout_Type()
)
initialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initialTimeout.setStatus("current")


class _InterDigitTimeout_Type(Integer32):
    """Custom type interDigitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_InterDigitTimeout_Type.__name__ = "Integer32"
_InterDigitTimeout_Object = MibScalar
interDigitTimeout = _InterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4, 1, 2),
    _InterDigitTimeout_Type()
)
interDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interDigitTimeout.setStatus("current")


class _DigitPauseTimeout_Type(Integer32):
    """Custom type digitPauseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DigitPauseTimeout_Type.__name__ = "Integer32"
_DigitPauseTimeout_Object = MibScalar
digitPauseTimeout = _DigitPauseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4, 1, 3),
    _DigitPauseTimeout_Type()
)
digitPauseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitPauseTimeout.setStatus("current")


class _MatchingTimeout_Type(Integer32):
    """Custom type matchingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MatchingTimeout_Type.__name__ = "Integer32"
_MatchingTimeout_Object = MibScalar
matchingTimeout = _MatchingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 2, 4, 1, 4),
    _MatchingTimeout_Type()
)
matchingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matchingTimeout.setStatus("current")
_VoipIp_ObjectIdentity = ObjectIdentity
voipIp = _VoipIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 3)
)
_VoipIpSetIp_Type = IpAddress
_VoipIpSetIp_Object = MibScalar
voipIpSetIp = _VoipIpSetIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 3, 1),
    _VoipIpSetIp_Type()
)
voipIpSetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetIp.setStatus("current")
_VoipIpSetVid_Type = VlanIndex
_VoipIpSetVid_Object = MibScalar
voipIpSetVid = _VoipIpSetVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 3, 2),
    _VoipIpSetVid_Type()
)
voipIpSetVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetVid.setStatus("current")


class _VoipIpSetMask_Type(Integer32):
    """Custom type voipIpSetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VoipIpSetMask_Type.__name__ = "Integer32"
_VoipIpSetMask_Object = MibScalar
voipIpSetMask = _VoipIpSetMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 3, 3),
    _VoipIpSetMask_Type()
)
voipIpSetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipIpSetMask.setStatus("current")
_VoipDns_ObjectIdentity = ObjectIdentity
voipDns = _VoipDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 4)
)
_VoipDnsIp_Type = IpAddress
_VoipDnsIp_Object = MibScalar
voipDnsIp = _VoipDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 4, 1),
    _VoipDnsIp_Type()
)
voipDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipDnsIp.setStatus("current")
_MaxNumOfVoipRoute_Type = Integer32
_MaxNumOfVoipRoute_Object = MibScalar
maxNumOfVoipRoute = _MaxNumOfVoipRoute_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 7),
    _MaxNumOfVoipRoute_Type()
)
maxNumOfVoipRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipRoute.setStatus("current")
_VoipRouteTable_Object = MibTable
voipRouteTable = _VoipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8)
)
if mibBuilder.loadTexts:
    voipRouteTable.setStatus("current")
_VoipRouteEntry_Object = MibTableRow
voipRouteEntry = _VoipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1)
)
voipRouteEntry.setIndexNames(
    (0, "E5-111-MIB", "voipRouteIp"),
    (0, "E5-111-MIB", "voipRouteGateway"),
    (0, "E5-111-MIB", "voipRouteMask"),
)
if mibBuilder.loadTexts:
    voipRouteEntry.setStatus("current")
_VoipRouteIp_Type = IpAddress
_VoipRouteIp_Object = MibTableColumn
voipRouteIp = _VoipRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1, 1),
    _VoipRouteIp_Type()
)
voipRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteIp.setStatus("current")
_VoipRouteGateway_Type = IpAddress
_VoipRouteGateway_Object = MibTableColumn
voipRouteGateway = _VoipRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1, 2),
    _VoipRouteGateway_Type()
)
voipRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteGateway.setStatus("current")


class _VoipRouteMask_Type(Integer32):
    """Custom type voipRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VoipRouteMask_Type.__name__ = "Integer32"
_VoipRouteMask_Object = MibTableColumn
voipRouteMask = _VoipRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1, 3),
    _VoipRouteMask_Type()
)
voipRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRouteMask.setStatus("current")


class _VoipRouteMetric_Type(Integer32):
    """Custom type voipRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_VoipRouteMetric_Type.__name__ = "Integer32"
_VoipRouteMetric_Object = MibTableColumn
voipRouteMetric = _VoipRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1, 4),
    _VoipRouteMetric_Type()
)
voipRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRouteMetric.setStatus("current")
_VoipRouteRowStatus_Type = RowStatus
_VoipRouteRowStatus_Object = MibTableColumn
voipRouteRowStatus = _VoipRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 8, 1, 5),
    _VoipRouteRowStatus_Type()
)
voipRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRouteRowStatus.setStatus("current")


class _VoipCountryCode_Type(Integer32):
    """Custom type voipCountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("usa", 1)
    )


_VoipCountryCode_Type.__name__ = "Integer32"
_VoipCountryCode_Object = MibScalar
voipCountryCode = _VoipCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 9),
    _VoipCountryCode_Type()
)
voipCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipCountryCode.setStatus("current")
_VoipH248_ObjectIdentity = ObjectIdentity
voipH248 = _VoipH248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10)
)
_MaxNumOfVoipH248MgConf_Type = Integer32
_MaxNumOfVoipH248MgConf_Object = MibScalar
maxNumOfVoipH248MgConf = _MaxNumOfVoipH248MgConf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 1),
    _MaxNumOfVoipH248MgConf_Type()
)
maxNumOfVoipH248MgConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfVoipH248MgConf.setStatus("current")
_VoipH248MgConf_ObjectIdentity = ObjectIdentity
voipH248MgConf = _VoipH248MgConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 2)
)
_VoipH248MgName_Type = DisplayString
_VoipH248MgName_Object = MibScalar
voipH248MgName = _VoipH248MgName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 2, 1),
    _VoipH248MgName_Type()
)
voipH248MgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgName.setStatus("current")


class _VoipH248MgEnable_Type(Integer32):
    """Custom type voipH248MgEnable based on Integer32"""
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


_VoipH248MgEnable_Type.__name__ = "Integer32"
_VoipH248MgEnable_Object = MibScalar
voipH248MgEnable = _VoipH248MgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 2, 2),
    _VoipH248MgEnable_Type()
)
voipH248MgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgEnable.setStatus("current")
_VoipH248MgH248Profile_Type = DisplayString
_VoipH248MgH248Profile_Object = MibScalar
voipH248MgH248Profile = _VoipH248MgH248Profile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 2, 3),
    _VoipH248MgH248Profile_Type()
)
voipH248MgH248Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgH248Profile.setStatus("current")


class _VoipH248MgPort_Type(Integer32):
    """Custom type voipH248MgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VoipH248MgPort_Type.__name__ = "Integer32"
_VoipH248MgPort_Object = MibScalar
voipH248MgPort = _VoipH248MgPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 10, 2, 4),
    _VoipH248MgPort_Type()
)
voipH248MgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipH248MgPort.setStatus("current")
_VoipRing_ObjectIdentity = ObjectIdentity
voipRing = _VoipRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11)
)
_VoipRingTable_Object = MibTable
voipRingTable = _VoipRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1)
)
if mibBuilder.loadTexts:
    voipRingTable.setStatus("current")
_VoipRingEntry_Object = MibTableRow
voipRingEntry = _VoipRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1)
)
voipRingEntry.setIndexNames(
    (0, "E5-111-MIB", "voipRingIndex"),
)
if mibBuilder.loadTexts:
    voipRingEntry.setStatus("current")


class _VoipRingIndex_Type(Integer32):
    """Custom type voipRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoipRingIndex_Type.__name__ = "Integer32"
_VoipRingIndex_Object = MibTableColumn
voipRingIndex = _VoipRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 1),
    _VoipRingIndex_Type()
)
voipRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipRingIndex.setStatus("current")


class _VoipRingName_Type(DisplayString):
    """Custom type voipRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_VoipRingName_Type.__name__ = "DisplayString"
_VoipRingName_Object = MibTableColumn
voipRingName = _VoipRingName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 2),
    _VoipRingName_Type()
)
voipRingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingName.setStatus("current")


class _VoipRingOn1_Type(Integer32):
    """Custom type voipRingOn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn1_Type.__name__ = "Integer32"
_VoipRingOn1_Object = MibTableColumn
voipRingOn1 = _VoipRingOn1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 3),
    _VoipRingOn1_Type()
)
voipRingOn1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn1.setStatus("current")


class _VoipRingOff1_Type(Integer32):
    """Custom type voipRingOff1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff1_Type.__name__ = "Integer32"
_VoipRingOff1_Object = MibTableColumn
voipRingOff1 = _VoipRingOff1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 4),
    _VoipRingOff1_Type()
)
voipRingOff1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff1.setStatus("current")


class _VoipRingOn2_Type(Integer32):
    """Custom type voipRingOn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn2_Type.__name__ = "Integer32"
_VoipRingOn2_Object = MibTableColumn
voipRingOn2 = _VoipRingOn2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 5),
    _VoipRingOn2_Type()
)
voipRingOn2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn2.setStatus("current")


class _VoipRingOff2_Type(Integer32):
    """Custom type voipRingOff2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff2_Type.__name__ = "Integer32"
_VoipRingOff2_Object = MibTableColumn
voipRingOff2 = _VoipRingOff2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 6),
    _VoipRingOff2_Type()
)
voipRingOff2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff2.setStatus("current")


class _VoipRingOn3_Type(Integer32):
    """Custom type voipRingOn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOn3_Type.__name__ = "Integer32"
_VoipRingOn3_Object = MibTableColumn
voipRingOn3 = _VoipRingOn3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 7),
    _VoipRingOn3_Type()
)
voipRingOn3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOn3.setStatus("current")


class _VoipRingOff3_Type(Integer32):
    """Custom type voipRingOff3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_VoipRingOff3_Type.__name__ = "Integer32"
_VoipRingOff3_Object = MibTableColumn
voipRingOff3 = _VoipRingOff3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 1, 1, 8),
    _VoipRingOff3_Type()
)
voipRingOff3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voipRingOff3.setStatus("current")


class _VoipRingSetDefault_Type(Integer32):
    """Custom type voipRingSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoipRingSetDefault_Type.__name__ = "Integer32"
_VoipRingSetDefault_Object = MibScalar
voipRingSetDefault = _VoipRingSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 11, 2),
    _VoipRingSetDefault_Type()
)
voipRingSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipRingSetDefault.setStatus("current")


class _VoipBootRegDelay_Type(Integer32):
    """Custom type voipBootRegDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VoipBootRegDelay_Type.__name__ = "Integer32"
_VoipBootRegDelay_Object = MibScalar
voipBootRegDelay = _VoipBootRegDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 12),
    _VoipBootRegDelay_Type()
)
voipBootRegDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipBootRegDelay.setStatus("current")
_VoipActiveCall_ObjectIdentity = ObjectIdentity
voipActiveCall = _VoipActiveCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 13)
)
_VoipActiveCallMaxActiveCalls_Type = Integer32
_VoipActiveCallMaxActiveCalls_Object = MibScalar
voipActiveCallMaxActiveCalls = _VoipActiveCallMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 13, 1),
    _VoipActiveCallMaxActiveCalls_Type()
)
voipActiveCallMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipActiveCallMaxActiveCalls.setStatus("current")
_VoipActiveCallThreshold_Type = Integer32
_VoipActiveCallThreshold_Object = MibScalar
voipActiveCallThreshold = _VoipActiveCallThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 13, 2),
    _VoipActiveCallThreshold_Type()
)
voipActiveCallThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipActiveCallThreshold.setStatus("current")


class _VoipMode_Type(Integer32):
    """Custom type voipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csip", 2),
          ("h248", 3),
          ("sip", 1))
    )


_VoipMode_Type.__name__ = "Integer32"
_VoipMode_Object = MibScalar
voipMode = _VoipMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 16, 100),
    _VoipMode_Type()
)
voipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipMode.setStatus("current")
_AesSeriesCommon_ObjectIdentity = ObjectIdentity
aesSeriesCommon = _AesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97)
)
_IesSeriesCommon_ObjectIdentity = ObjectIdentity
iesSeriesCommon = _IesSeriesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98)
)
_AccessSwitchCommonATM_ObjectIdentity = ObjectIdentity
accessSwitchCommonATM = _AccessSwitchCommonATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-111-MIB",
    **{"calixNetworks": calixNetworks,
       "calixRegistrations": calixRegistrations,
       "calixProducts": calixProducts,
       "e5x100": e5x100,
       "e5x111": e5x111,
       "alarmconf": alarmconf,
       "alarmOps": alarmOps,
       "alarmConfTable": alarmConfTable,
       "alarmConfEntry": alarmConfEntry,
       "alarmConfId": alarmConfId,
       "alarmConfFacility": alarmConfFacility,
       "alarmConfTarget": alarmConfTarget,
       "alarmConfSeverity": alarmConfSeverity,
       "alarmConfClearable": alarmConfClearable,
       "alarmCurrTable": alarmCurrTable,
       "alarmCurrEntry": alarmCurrEntry,
       "alarmCurrIndex": alarmCurrIndex,
       "alarmCurrOccurTime": alarmCurrOccurTime,
       "alarmCurrTrapOid": alarmCurrTrapOid,
       "alarmCurrParam1": alarmCurrParam1,
       "alarmCurrParam2": alarmCurrParam2,
       "alarmCurrParam3": alarmCurrParam3,
       "alarmCurrParam4": alarmCurrParam4,
       "alarmCurrParam5": alarmCurrParam5,
       "alarmCurrParam6": alarmCurrParam6,
       "alarmCurrParam7": alarmCurrParam7,
       "alarmCurrParam8": alarmCurrParam8,
       "alarmCurrTimeDescr": alarmCurrTimeDescr,
       "alarmCurrSeverity": alarmCurrSeverity,
       "alarmCurrDescr": alarmCurrDescr,
       "alarmSeverityPortTable": alarmSeverityPortTable,
       "alarmSeverityPortEntry": alarmSeverityPortEntry,
       "severityThresh": severityThresh,
       "diagnostic": diagnostic,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter,
       "mlt": mlt,
       "mltTarget": mltTarget,
       "mltOps": mltOps,
       "mltOption": mltOption,
       "mltForce": mltForce,
       "mltResult": mltResult,
       "mltVacTip": mltVacTip,
       "mltVacRing": mltVacRing,
       "mltVacDiff": mltVacDiff,
       "mltVdcTip": mltVdcTip,
       "mltVdcRing": mltVdcRing,
       "mltVdcDiff": mltVdcDiff,
       "mltRLoop": mltRLoop,
       "mltRtg": mltRtg,
       "mltRrg": mltRrg,
       "mltRtr": mltRtr,
       "mltCtg": mltCtg,
       "mltCrg": mltCrg,
       "mltCtr": mltCtr,
       "mltRen": mltRen,
       "mltVRing": mltVRing,
       "mltVMetering": mltVMetering,
       "mltDialToneDetected": mltDialToneDetected,
       "mltDetectedDtmfCount": mltDetectedDtmfCount,
       "mltDialToneDelay": mltDialToneDelay,
       "mltRelayTable": mltRelayTable,
       "mltRelayEntry": mltRelayEntry,
       "mltRelaySet": mltRelaySet,
       "multicast": multicast,
       "igmpEnable": igmpEnable,
       "mcastBandwidth": mcastBandwidth,
       "mcastDefaultBandwidth": mcastDefaultBandwidth,
       "maxNumOfMcastBw": maxNumOfMcastBw,
       "mcastBwTable": mcastBwTable,
       "mcastBwEntry": mcastBwEntry,
       "mcastBwIndex": mcastBwIndex,
       "mcastBwStartIp": mcastBwStartIp,
       "mcastBwEndIp": mcastBwEndIp,
       "mcastBwBandwidth": mcastBwBandwidth,
       "mcastBwRowStatus": mcastBwRowStatus,
       "mcastBwPortTable": mcastBwPortTable,
       "mcastBwPortEntry": mcastBwPortEntry,
       "mcastBwPortEnable": mcastBwPortEnable,
       "mcastBwPortBandwidth": mcastBwPortBandwidth,
       "igmpCount": igmpCount,
       "igmpCountPortTable": igmpCountPortTable,
       "igmpCountPortEntry": igmpCountPortEntry,
       "igmpCountPortEnable": igmpCountPortEnable,
       "igmpCountPortLimit": igmpCountPortLimit,
       "mvlan": mvlan,
       "maxNumOfMvlan": maxNumOfMvlan,
       "mvlanTable": mvlanTable,
       "mvlanEntry": mvlanEntry,
       "mvlanIndex": mvlanIndex,
       "mvlanName": mvlanName,
       "mvlanEgressPorts": mvlanEgressPorts,
       "mvlanUntaggedPorts": mvlanUntaggedPorts,
       "mvlanRowStatus": mvlanRowStatus,
       "mvlanTranslateTable": mvlanTranslateTable,
       "mvlanTranslateEntry": mvlanTranslateEntry,
       "mvlanTranslateIndex": mvlanTranslateIndex,
       "mvlanTranslateStartIp": mvlanTranslateStartIp,
       "mvlanTranslateEndIp": mvlanTranslateEndIp,
       "queryVid": queryVid,
       "maxNumOfQryVid": maxNumOfQryVid,
       "qryVidConfTable": qryVidConfTable,
       "qryVidConfEntry": qryVidConfEntry,
       "qryVid": qryVid,
       "qryVidRowStatus": qryVidRowStatus,
       "qryVidStatusTable": qryVidStatusTable,
       "qryVidStatusEntry": qryVidStatusEntry,
       "qryVidType": qryVidType,
       "igmpVersion": igmpVersion,
       "igmpLeaveMode": igmpLeaveMode,
       "igmpTimer": igmpTimer,
       "igmpQryInterval": igmpQryInterval,
       "igmpRobust": igmpRobust,
       "igmpQryRespInterval": igmpQryRespInterval,
       "igmpLastMemQryInterval": igmpLastMemQryInterval,
       "igmpLastMemQryRobust": igmpLastMemQryRobust,
       "auditQuery": auditQuery,
       "auditQryEnable": auditQryEnable,
       "auditQryInterval": auditQryInterval,
       "auditQryRobust": auditQryRobust,
       "igmpProfile": igmpProfile,
       "maxNumberOfIgmpProfiles": maxNumberOfIgmpProfiles,
       "igmpProfileTable": igmpProfileTable,
       "igmpProfileEntry": igmpProfileEntry,
       "igmpProfileName": igmpProfileName,
       "igmpProfileEnable": igmpProfileEnable,
       "igmpProfileMaxGroup": igmpProfileMaxGroup,
       "igmpProfileRowStatus": igmpProfileRowStatus,
       "igmpFilterTable": igmpFilterTable,
       "igmpFilterEntry": igmpFilterEntry,
       "igmpFilterIndex": igmpFilterIndex,
       "igmpFilterStartIp": igmpFilterStartIp,
       "igmpFilterEndIp": igmpFilterEndIp,
       "igmpProfilePortTable": igmpProfilePortTable,
       "igmpProfilePortEntry": igmpProfilePortEntry,
       "igmpProfilePortProfile": igmpProfilePortProfile,
       "port": port,
       "subrPortTable": subrPortTable,
       "subrPortEntry": subrPortEntry,
       "subrPortName": subrPortName,
       "subrPortTel": subrPortTel,
       "adslPort": adslPort,
       "adslLineConfTable": adslLineConfTable,
       "adslLineConfEntry": adslLineConfEntry,
       "adslLineConfAdslMode": adslLineConfAdslMode,
       "adslLineConfAnnexL": adslLineConfAnnexL,
       "adslLineConfAnnexM": adslLineConfAnnexM,
       "adslLineConfAnnexI": adslLineConfAnnexI,
       "adslLineConfOptionMask": adslLineConfOptionMask,
       "adslLineConfPowerMgmt": adslLineConfPowerMgmt,
       "adslLineConfPowerMode": adslLineConfPowerMode,
       "adslLineConfAturMaxTxPower": adslLineConfAturMaxTxPower,
       "adslLineConfAtucMaxTxPower": adslLineConfAtucMaxTxPower,
       "adslLineConfMaxRxPower": adslLineConfMaxRxPower,
       "adslLineConfAturCarrierMask": adslLineConfAturCarrierMask,
       "adslLineConfAtucCarrierMask0": adslLineConfAtucCarrierMask0,
       "adslLineConfAtucCarrierMask1": adslLineConfAtucCarrierMask1,
       "adslLineConfAturInp": adslLineConfAturInp,
       "adslLineConfAtucInp": adslLineConfAtucInp,
       "adslLineConfL0Time": adslLineConfL0Time,
       "adslLineConfL2Time": adslLineConfL2Time,
       "adslLineConfL2ATPR": adslLineConfL2ATPR,
       "adslLineConfL2ATPRT": adslLineConfL2ATPRT,
       "adslLineConfMaxL2Rate": adslLineConfMaxL2Rate,
       "adslLineConfMinL2Rate": adslLineConfMinL2Rate,
       "adslLineConfL0toL2Rate": adslLineConfL0toL2Rate,
       "adslLineConfNitro": adslLineConfNitro,
       "adslLineConfUSPhyr": adslLineConfUSPhyr,
       "adslLineConfDSPhyr": adslLineConfDSPhyr,
       "adslPortBatchSet": adslPortBatchSet,
       "adslPortTarget": adslPortTarget,
       "adslPortOps": adslPortOps,
       "adslPortOps2": adslPortOps2,
       "adslModeForBatchSet": adslModeForBatchSet,
       "adslLineProfileForBatchSet": adslLineProfileForBatchSet,
       "adslAlarmProfileForBatchSet": adslAlarmProfileForBatchSet,
       "adslOptionMaskForBatchSet": adslOptionMaskForBatchSet,
       "adslAturMaxTxPowerForBatchSet": adslAturMaxTxPowerForBatchSet,
       "adslAtucMaxTxPowerForBatchSet": adslAtucMaxTxPowerForBatchSet,
       "adslMaxRxPowerForBatchSet": adslMaxRxPowerForBatchSet,
       "adslAturCarrierMaskForBatchSet": adslAturCarrierMaskForBatchSet,
       "adslAtucCarrierMask0ForBatchSet": adslAtucCarrierMask0ForBatchSet,
       "adslAtucCarrierMask1ForBatchSet": adslAtucCarrierMask1ForBatchSet,
       "adslAturInpForBatchSet": adslAturInpForBatchSet,
       "adslAtucInpForBatchSet": adslAtucInpForBatchSet,
       "adslL0TimeForBatchSet": adslL0TimeForBatchSet,
       "adslL2TimeForBatchSet": adslL2TimeForBatchSet,
       "adslL2ATPRForBatchSet": adslL2ATPRForBatchSet,
       "adslL2ATPRTForBatchSet": adslL2ATPRTForBatchSet,
       "adslMaxL2RateForBatchSet": adslMaxL2RateForBatchSet,
       "adslMinL2RateForBatchSet": adslMinL2RateForBatchSet,
       "adslL0toL2RateForBatchSet": adslL0toL2RateForBatchSet,
       "adslLineStatusTable": adslLineStatusTable,
       "adslLineStatusEntry": adslLineStatusEntry,
       "adslLineStatusMode": adslLineStatusMode,
       "adslLineUpTime": adslLineUpTime,
       "powerMgmtParamTable": powerMgmtParamTable,
       "powerMgmtParamEntry": powerMgmtParamEntry,
       "powerMgmtL0Time": powerMgmtL0Time,
       "powerMgmtL2Time": powerMgmtL2Time,
       "powerMgmtL2Atpr": powerMgmtL2Atpr,
       "powerMgmtL2Atprt": powerMgmtL2Atprt,
       "powerMgmtL2MinRate": powerMgmtL2MinRate,
       "powerMgmtL2MaxRate": powerMgmtL2MaxRate,
       "powerMgmtL2ThreshRate": powerMgmtL2ThreshRate,
       "powerMgmtPSDTable": powerMgmtPSDTable,
       "powerMgmtPSDEntry": powerMgmtPSDEntry,
       "powerMgmtAtucMaxPSD": powerMgmtAtucMaxPSD,
       "powerMgmtAturMaxPSD": powerMgmtAturMaxPSD,
       "pvc": pvc,
       "maxNumOfPvcs": maxNumOfPvcs,
       "pvcTable": pvcTable,
       "pvcEntry": pvcEntry,
       "pvcVpi": pvcVpi,
       "pvcVci": pvcVci,
       "pvcPvid": pvcPvid,
       "pvcPriority": pvcPriority,
       "pvcProfileDS": pvcProfileDS,
       "pvcRowStatus": pvcRowStatus,
       "pvcProfileUS": pvcProfileUS,
       "pvcAcName": pvcAcName,
       "pvcServiceName": pvcServiceName,
       "pvcHelloTime": pvcHelloTime,
       "pvcStateTable": pvcStateTable,
       "pvcStateEntry": pvcStateEntry,
       "pvcStateVpi": pvcStateVpi,
       "pvcStateVci": pvcStateVci,
       "pvcStatePvid": pvcStatePvid,
       "pvcStatePriority": pvcStatePriority,
       "pvcStateChannelType": pvcStateChannelType,
       "pvcStateEncap": pvcStateEncap,
       "pvcUsRateLimitTable": pvcUsRateLimitTable,
       "pvcUsRateLimitEntry": pvcUsRateLimitEntry,
       "pvcUsRateLimitEnable": pvcUsRateLimitEnable,
       "pvcUsRateLimit": pvcUsRateLimit,
       "ppvc": ppvc,
       "maxNumOfPriorityPvcs": maxNumOfPriorityPvcs,
       "ppvcTable": ppvcTable,
       "ppvcEntry": ppvcEntry,
       "ppvcVpi": ppvcVpi,
       "ppvcVci": ppvcVci,
       "ppvcPvid": ppvcPvid,
       "ppvcEncap": ppvcEncap,
       "ppvcPriority": ppvcPriority,
       "ppvcRowStatus": ppvcRowStatus,
       "ppvcMemberTable": ppvcMemberTable,
       "ppvcMemberEntry": ppvcMemberEntry,
       "ppvcMemberVpi": ppvcMemberVpi,
       "ppvcMemberVci": ppvcMemberVci,
       "ppvcMemberPriority": ppvcMemberPriority,
       "ppvcMemberProfileDS": ppvcMemberProfileDS,
       "ppvcMemberRowStatus": ppvcMemberRowStatus,
       "ppvcMemberProfileUS": ppvcMemberProfileUS,
       "rpvc": rpvc,
       "rpvcGatewayTable": rpvcGatewayTable,
       "rpvcGatewayEntry": rpvcGatewayEntry,
       "rpvcGatewayIp": rpvcGatewayIp,
       "rpvcGatewayVlanId": rpvcGatewayVlanId,
       "rpvcGatewayRowStatus": rpvcGatewayRowStatus,
       "rpvcGatewayPriority": rpvcGatewayPriority,
       "rpvcTable": rpvcTable,
       "rpvcEntry": rpvcEntry,
       "rpvcVpi": rpvcVpi,
       "rpvcVci": rpvcVci,
       "rpvcDSProfile": rpvcDSProfile,
       "rpvcUSProfile": rpvcUSProfile,
       "rpvcIp": rpvcIp,
       "rpvcNetmask": rpvcNetmask,
       "rpvcGatewayIpAddress": rpvcGatewayIpAddress,
       "rpvcRowStatus": rpvcRowStatus,
       "rpvcRouteDomainTable": rpvcRouteDomainTable,
       "rpvcRouteDomainEntry": rpvcRouteDomainEntry,
       "rpvcRouteDomainVpi": rpvcRouteDomainVpi,
       "rpvcRouteDomainVci": rpvcRouteDomainVci,
       "rpvcRouteDomainIp": rpvcRouteDomainIp,
       "rpvcRouteDomainNetmask": rpvcRouteDomainNetmask,
       "rpvcRouteDomainRowStatus": rpvcRouteDomainRowStatus,
       "rpvcArpAgingTime": rpvcArpAgingTime,
       "rpvcArpFlush": rpvcArpFlush,
       "dsBcastDisableTable": dsBcastDisableTable,
       "dsBcastDisableEntry": dsBcastDisableEntry,
       "dsBcastDisableVlanId": dsBcastDisableVlanId,
       "dsBcastDisableRowStatus": dsBcastDisableRowStatus,
       "paepvc": paepvc,
       "paepvcTable": paepvcTable,
       "paepvcEntry": paepvcEntry,
       "paepvcVpi": paepvcVpi,
       "paepvcVci": paepvcVci,
       "paepvcPvid": paepvcPvid,
       "paepvcPriority": paepvcPriority,
       "paepvcProfileDS": paepvcProfileDS,
       "paepvcAcName": paepvcAcName,
       "paepvcServiceName": paepvcServiceName,
       "paepvcHelloTime": paepvcHelloTime,
       "paepvcRowStatus": paepvcRowStatus,
       "paepvcProfileUS": paepvcProfileUS,
       "paepvcCvid": paepvcCvid,
       "paepvcCPriority": paepvcCPriority,
       "tlspvc": tlspvc,
       "tlspvcTable": tlspvcTable,
       "tlspvcEntry": tlspvcEntry,
       "tlspvcVpi": tlspvcVpi,
       "tlspvcVci": tlspvcVci,
       "tlspvcSvid": tlspvcSvid,
       "tlspvcSpriority": tlspvcSpriority,
       "tlspvcProfileDS": tlspvcProfileDS,
       "tlspvcRowStatus": tlspvcRowStatus,
       "tlspvcProfileUS": tlspvcProfileUS,
       "ipbpvc": ipbpvc,
       "ipbpvcDomainTable": ipbpvcDomainTable,
       "ipbpvcDomainEntry": ipbpvcDomainEntry,
       "ipbpvcDomainName": ipbpvcDomainName,
       "ipbpvcDomainRowStatus": ipbpvcDomainRowStatus,
       "ipbpvcDomainVlanTable": ipbpvcDomainVlanTable,
       "ipbpvcDomainVlanEntry": ipbpvcDomainVlanEntry,
       "ipbpvcDomainVlanId": ipbpvcDomainVlanId,
       "ipbpvcDomainDhcpVlanEnable": ipbpvcDomainDhcpVlanEnable,
       "ipbpvcDomainVlanRowStatus": ipbpvcDomainVlanRowStatus,
       "ipbpvcEdgeRouterTable": ipbpvcEdgeRouterTable,
       "ipbpvcEdgeRouterEntry": ipbpvcEdgeRouterEntry,
       "ipbpvcEdgeRouterIp": ipbpvcEdgeRouterIp,
       "ipbpvcEdgeRouterVid": ipbpvcEdgeRouterVid,
       "ipbpvcEdgeRouterMask": ipbpvcEdgeRouterMask,
       "ipbpvcEdgeRouterRowStatus": ipbpvcEdgeRouterRowStatus,
       "ipbpvcInterfaceTable": ipbpvcInterfaceTable,
       "ipbpvcInterfaceEntry": ipbpvcInterfaceEntry,
       "ipbpvcInterfaceIp": ipbpvcInterfaceIp,
       "ipbpvcInterfaceMask": ipbpvcInterfaceMask,
       "ipbpvcInterfaceVid": ipbpvcInterfaceVid,
       "ipbpvcInterfaceIfIndex": ipbpvcInterfaceIfIndex,
       "ipbpvcInterfaceVpi": ipbpvcInterfaceVpi,
       "ipbpvcInterfaceVci": ipbpvcInterfaceVci,
       "ipbpvcInterfaceRowStatus": ipbpvcInterfaceRowStatus,
       "ipbpvcRouteTable": ipbpvcRouteTable,
       "ipbpvcRouteEntry": ipbpvcRouteEntry,
       "ipbpvcRouteIp": ipbpvcRouteIp,
       "ipbpvcRouteMask": ipbpvcRouteMask,
       "ipbpvcRouteNextHop": ipbpvcRouteNextHop,
       "ipbpvcRouteMetric": ipbpvcRouteMetric,
       "ipbpvcRoutePriority": ipbpvcRoutePriority,
       "ipbpvcRouteRowStatus": ipbpvcRouteRowStatus,
       "ipbpvcTable": ipbpvcTable,
       "ipbpvcEntry": ipbpvcEntry,
       "ipbpvcVpi": ipbpvcVpi,
       "ipbpvcVci": ipbpvcVci,
       "ipbpvcPvid": ipbpvcPvid,
       "ipbpvcEncap": ipbpvcEncap,
       "ipbpvcPriority": ipbpvcPriority,
       "ipbpvcProfile": ipbpvcProfile,
       "ipbpvcRowStatus": ipbpvcRowStatus,
       "ipbpvcProfileUS": ipbpvcProfileUS,
       "arpproxy": arpproxy,
       "arpproxyAge": arpproxyAge,
       "arpproxyFlush": arpproxyFlush,
       "arpproxyFlushTarget": arpproxyFlushTarget,
       "arpproxyFlushOps": arpproxyFlushOps,
       "arpproxyFlushEdgeRouterIp": arpproxyFlushEdgeRouterIp,
       "arpproxyFlushEdgeRouterVid": arpproxyFlushEdgeRouterVid,
       "arpproxyFlushInterfaceIp": arpproxyFlushInterfaceIp,
       "arpproxyFlushInterfaceMask": arpproxyFlushInterfaceMask,
       "arpproxyFlushInterfaceVid": arpproxyFlushInterfaceVid,
       "voipPort": voipPort,
       "voipSipLineConfTable": voipSipLineConfTable,
       "voipSipLineConfEntry": voipSipLineConfEntry,
       "voipSipLineConfSipProfile": voipSipLineConfSipProfile,
       "voipSipLineConfSipCallSvcProfile": voipSipLineConfSipCallSvcProfile,
       "voipSipLineConfDspProfile": voipSipLineConfDspProfile,
       "portOperations": portOperations,
       "voipPortTarget": voipPortTarget,
       "voipPortOps": voipPortOps,
       "voipPortEnableStatus": voipPortEnableStatus,
       "voipPortTelTable": voipPortTelTable,
       "voipPortTelEntry": voipPortTelEntry,
       "voipPortTel": voipPortTel,
       "voipPortGainTable": voipPortGainTable,
       "voipPortGainEntry": voipPortGainEntry,
       "voipPortTXGain": voipPortTXGain,
       "voipPortRXGain": voipPortRXGain,
       "voipH248LineConfTable": voipH248LineConfTable,
       "voipH248LineConfEntry": voipH248LineConfEntry,
       "voipH248LineConfMgName": voipH248LineConfMgName,
       "voipH248LineConfDspProfile": voipH248LineConfDspProfile,
       "voipH248LineConfVBDProfile": voipH248LineConfVBDProfile,
       "voipPortH248TerminationTable": voipPortH248TerminationTable,
       "voipPortH248TerminationEntry": voipPortH248TerminationEntry,
       "voipPortH248TermName": voipPortH248TermName,
       "dtpvc": dtpvc,
       "dtpvcTable": dtpvcTable,
       "dtpvcEntry": dtpvcEntry,
       "dtpvcVpi": dtpvcVpi,
       "dtpvcVci": dtpvcVci,
       "dtpvcSvid": dtpvcSvid,
       "dtpvcSpriority": dtpvcSpriority,
       "dtpvcCvid": dtpvcCvid,
       "dtpvcCpriority": dtpvcCpriority,
       "dtpvcDSProfile": dtpvcDSProfile,
       "dtpvcUSProfile": dtpvcUSProfile,
       "dtpvcRowStatus": dtpvcRowStatus,
       "dtpvcSuperChannel": dtpvcSuperChannel,
       "dtpvcAcName": dtpvcAcName,
       "dtpvcServiceName": dtpvcServiceName,
       "dtpvcHelloTime": dtpvcHelloTime,
       "dtpvcStateTable": dtpvcStateTable,
       "dtpvcStateEntry": dtpvcStateEntry,
       "dtpvcStateVpi": dtpvcStateVpi,
       "dtpvcStateVci": dtpvcStateVci,
       "dtpvcStateSvid": dtpvcStateSvid,
       "dtpvcStateSPriority": dtpvcStateSPriority,
       "dtpvcStateCvid": dtpvcStateCvid,
       "dtpvcStateCPriority": dtpvcStateCPriority,
       "dtpvcStateChannelType": dtpvcStateChannelType,
       "dtpvcStateEncap": dtpvcStateEncap,
       "snrMgn": snrMgn,
       "snrMgnTable": snrMgnTable,
       "snrMgnEntry": snrMgnEntry,
       "snrMgnMode": snrMgnMode,
       "snrMgnUcTarget": snrMgnUcTarget,
       "snrMgnUcMax": snrMgnUcMax,
       "snrMgnUcMin": snrMgnUcMin,
       "snrMgnUcDownshift": snrMgnUcDownshift,
       "snrMgnUcUpshift": snrMgnUcUpshift,
       "snrMgnUrTarget": snrMgnUrTarget,
       "snrMgnUrMax": snrMgnUrMax,
       "snrMgnUrMin": snrMgnUrMin,
       "snrMgnUrDownshift": snrMgnUrDownshift,
       "snrMgnUrUpshift": snrMgnUrUpshift,
       "dslRate": dslRate,
       "dslRateTable": dslRateTable,
       "dslRateEntry": dslRateEntry,
       "dslRateMode": dslRateMode,
       "dslRateLatencyMode": dslRateLatencyMode,
       "dslRateXtucMaxInterleaveDelay": dslRateXtucMaxInterleaveDelay,
       "dslRateXtucMaxTxRate": dslRateXtucMaxTxRate,
       "dslRateXtucMinTxRate": dslRateXtucMinTxRate,
       "dslRateXturMaxInterleaveDelay": dslRateXturMaxInterleaveDelay,
       "dslRateXturMaxTxRate": dslRateXturMaxTxRate,
       "dslRateXturMinTxRate": dslRateXturMinTxRate,
       "gbond": gbond,
       "gbondGroupTable": gbondGroupTable,
       "gbondGroupEntry": gbondGroupEntry,
       "gbondGroupName": gbondGroupName,
       "gbondGroupPorts": gbondGroupPorts,
       "gbondGroupUpRate": gbondGroupUpRate,
       "gbondGroupDownRate": gbondGroupDownRate,
       "gbondGroupRowStatus": gbondGroupRowStatus,
       "profile": profile,
       "voipProfile": voipProfile,
       "sipProfile": sipProfile,
       "maxNumOfSipProfiles": maxNumOfSipProfiles,
       "sipProfileTable": sipProfileTable,
       "sipProfileEntry": sipProfileEntry,
       "sipProfileName": sipProfileName,
       "sipProfileSipSvr": sipProfileSipSvr,
       "sipProfileRegSvr": sipProfileRegSvr,
       "sipProfileProxySvr": sipProfileProxySvr,
       "sipProfileSipPort": sipProfileSipPort,
       "sipProfileRegSvrPort": sipProfileRegSvrPort,
       "sipProfileProxySvrPort": sipProfileProxySvrPort,
       "sipProfileUriType": sipProfileUriType,
       "sipProfilePbit": sipProfilePbit,
       "sipProfileDscp": sipProfileDscp,
       "sipProfileKeepAlive": sipProfileKeepAlive,
       "sipProfileSe": sipProfileSe,
       "sipProfilePrack": sipProfilePrack,
       "sipProfileRowStatus": sipProfileRowStatus,
       "sipProfileRegExpire": sipProfileRegExpire,
       "maxNumOfSipCallSvcProfiles": maxNumOfSipCallSvcProfiles,
       "sipCallSvcProfileTable": sipCallSvcProfileTable,
       "sipCallSvcProfileEntry": sipCallSvcProfileEntry,
       "sipCallSvcProfileName": sipCallSvcProfileName,
       "sipCallSvcProfilePasswdOn": sipCallSvcProfilePasswdOn,
       "sipCallSvcProfilePasswd": sipCallSvcProfilePasswd,
       "sipCallSvcProfileNumberPlanOn": sipCallSvcProfileNumberPlanOn,
       "sipCallSvcProfileNumberPlanCc": sipCallSvcProfileNumberPlanCc,
       "sipCallSvcProfileNumberPlanNdc": sipCallSvcProfileNumberPlanNdc,
       "sipCallSvcProfileNumberPlanTable": sipCallSvcProfileNumberPlanTable,
       "sipCallSvcProfileStateMask": sipCallSvcProfileStateMask,
       "sipCallSvcProfileDtmf": sipCallSvcProfileDtmf,
       "sipCallSvcProfileFax": sipCallSvcProfileFax,
       "sipCallSvcProfileRowStatus": sipCallSvcProfileRowStatus,
       "sipCallSvcProfileFlashType": sipCallSvcProfileFlashType,
       "sipCallSvcProfileFlashInfo": sipCallSvcProfileFlashInfo,
       "sipCallSvcProfileSoftSwitchType": sipCallSvcProfileSoftSwitchType,
       "maxNumOfDspProfiles": maxNumOfDspProfiles,
       "dspProfileTable": dspProfileTable,
       "dspProfileEntry": dspProfileEntry,
       "dspProfileName": dspProfileName,
       "dspProfileCodec": dspProfileCodec,
       "dspProfilePlayBufferMinDelay": dspProfilePlayBufferMinDelay,
       "dspProfilePlayBufferMaxDelay": dspProfilePlayBufferMaxDelay,
       "dspProfileEchoTail": dspProfileEchoTail,
       "dspProfileRowStatus": dspProfileRowStatus,
       "dspProfileG711Vpi": dspProfileG711Vpi,
       "dspProfileG723Vpi": dspProfileG723Vpi,
       "dspProfileG726Vpi": dspProfileG726Vpi,
       "dspProfileG729Vpi": dspProfileG729Vpi,
       "h248Profile": h248Profile,
       "maxNumOfH248Profiles": maxNumOfH248Profiles,
       "h248ProfileTable": h248ProfileTable,
       "h248ProfileEntry": h248ProfileEntry,
       "h248ProfileName": h248ProfileName,
       "h248ProfileMgcSvr": h248ProfileMgcSvr,
       "h248ProfileMgcPort": h248ProfileMgcPort,
       "h248ProfileMgc2On": h248ProfileMgc2On,
       "h248ProfileMgc2Svr": h248ProfileMgc2Svr,
       "h248ProfileMgc2Port": h248ProfileMgc2Port,
       "h248ProfileTransport": h248ProfileTransport,
       "h248ProfileEncode": h248ProfileEncode,
       "h248ProfilePbit": h248ProfilePbit,
       "h248ProfileDscp": h248ProfileDscp,
       "h248ProfileRowStatus": h248ProfileRowStatus,
       "h248ProfileVbd": h248ProfileVbd,
       "h248ProfileEphemeralPrefix": h248ProfileEphemeralPrefix,
       "h248ProfileSoftswitch": h248ProfileSoftswitch,
       "h248ProfileForceVer": h248ProfileForceVer,
       "h248ProfileStartRTPPort": h248ProfileStartRTPPort,
       "h248ProfileEndRTPPort": h248ProfileEndRTPPort,
       "h248ProfileEphemeralStartNumber": h248ProfileEphemeralStartNumber,
       "h248ProfileEphemeralSuffixLength": h248ProfileEphemeralSuffixLength,
       "h248ProfilePhysicalPrefix": h248ProfilePhysicalPrefix,
       "h248ProfilePhysicalStartNumber": h248ProfilePhysicalStartNumber,
       "h248ProfilePhysicalSuffixLength": h248ProfilePhysicalSuffixLength,
       "switch": switch,
       "dscp": dscp,
       "dscpMappingTable": dscpMappingTable,
       "dscpMappingEntry": dscpMappingEntry,
       "dscpSrcCodePoint": dscpSrcCodePoint,
       "dscpMapPriority": dscpMapPriority,
       "dscpPortTable": dscpPortTable,
       "dscpPortEntry": dscpPortEntry,
       "dscpStatusEnable": dscpStatusEnable,
       "vlanIsolation": vlanIsolation,
       "vlanIsolationTable": vlanIsolationTable,
       "vlanIsolationEntry": vlanIsolationEntry,
       "vlanIsolationRowStatus": vlanIsolationRowStatus,
       "enetMtu": enetMtu,
       "enetMtuEntry": enetMtuEntry,
       "dhcp": dhcp,
       "dhcpRelay82Table": dhcpRelay82Table,
       "dhcpRelay82Entry": dhcpRelay82Entry,
       "dhcpRelay82PrimaryServer": dhcpRelay82PrimaryServer,
       "dhcpRelay82SecondaryServer": dhcpRelay82SecondaryServer,
       "dhcpRelay82ActiveServer": dhcpRelay82ActiveServer,
       "dhcpRelay82Enable": dhcpRelay82Enable,
       "dhcpRelay82Info": dhcpRelay82Info,
       "dhcpRelay82RelayMode": dhcpRelay82RelayMode,
       "dhcpRelay82Suboption2Enable": dhcpRelay82Suboption2Enable,
       "dhcpRelay82Suboption2Info": dhcpRelay82Suboption2Info,
       "dhcpRelay82EntryEnable": dhcpRelay82EntryEnable,
       "dhcpRelay82EntryOptionMode": dhcpRelay82EntryOptionMode,
       "dhcpRelay82VlanIp": dhcpRelay82VlanIp,
       "dhcpRelay82VlanMask": dhcpRelay82VlanMask,
       "dhcpRelay82VlanGateway": dhcpRelay82VlanGateway,
       "dhcpRelay82ThirdServer": dhcpRelay82ThirdServer,
       "dhcpRelay82FourthServer": dhcpRelay82FourthServer,
       "dhcpRelay82FifthServer": dhcpRelay82FifthServer,
       "dhcpRelay82ServerVid": dhcpRelay82ServerVid,
       "dhcpRelayTest": dhcpRelayTest,
       "dhcpRelayTestVid": dhcpRelayTestVid,
       "dhcpRelayTestIp": dhcpRelayTestIp,
       "dhcpRelayTestOps": dhcpRelayTestOps,
       "dhcpRelayTestStatus": dhcpRelayTestStatus,
       "dhcpRelayArp": dhcpRelayArp,
       "dhcpRelayArpShowTable": dhcpRelayArpShowTable,
       "dhcpRelayArpShowEntry": dhcpRelayArpShowEntry,
       "dhcpRelayArpShowVid": dhcpRelayArpShowVid,
       "dhcpRelayArpShowIp": dhcpRelayArpShowIp,
       "dhcpRelayArpShowMac": dhcpRelayArpShowMac,
       "dhcpRelayArpFlushOps": dhcpRelayArpFlushOps,
       "macfilter": macfilter,
       "macFilterPortTable": macFilterPortTable,
       "macFilterPortEntry": macFilterPortEntry,
       "macFilterPortEnable": macFilterPortEnable,
       "macFilterPortMacCount": macFilterPortMacCount,
       "macFilterPortFilterMode": macFilterPortFilterMode,
       "maxNumOfMacFiltersInSystem": maxNumOfMacFiltersInSystem,
       "maxNumOfMacFiltersPerPort": maxNumOfMacFiltersPerPort,
       "currNumOfMacFiltersInSystem": currNumOfMacFiltersInSystem,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterAddr": macFilterAddr,
       "macFilterRowStatus": macFilterRowStatus,
       "macfilterBatchSet": macfilterBatchSet,
       "macfilterTarget": macfilterTarget,
       "macfilterOps": macfilterOps,
       "macFilterMacCountForBatchSet": macFilterMacCountForBatchSet,
       "ouiFilterTableOld": ouiFilterTableOld,
       "ouiFilterEntryOld": ouiFilterEntryOld,
       "ouiFilterAddrOld": ouiFilterAddrOld,
       "ouiFilterRowStatusOld": ouiFilterRowStatusOld,
       "maxNumOfOuiFiltersPerPort": maxNumOfOuiFiltersPerPort,
       "ouiFilterPortTable": ouiFilterPortTable,
       "ouiFilterPortEntry": ouiFilterPortEntry,
       "ouiFilterPortEnable": ouiFilterPortEnable,
       "ouiFilterPortFilterMode": ouiFilterPortFilterMode,
       "maxNumOfOuiFiltersInSystem": maxNumOfOuiFiltersInSystem,
       "maxNumOfOuiFiltersPerVlan": maxNumOfOuiFiltersPerVlan,
       "ouiFilterTable": ouiFilterTable,
       "ouiFilterEntry": ouiFilterEntry,
       "ouiFilterAddr": ouiFilterAddr,
       "ouiFilterRowStatus": ouiFilterRowStatus,
       "ouiFilterVlanTable": ouiFilterVlanTable,
       "ouiFilterVlanEntry": ouiFilterVlanEntry,
       "ouiFilterVlanEnable": ouiFilterVlanEnable,
       "ouiFilterVlanFilterMode": ouiFilterVlanFilterMode,
       "dhcpSnoop": dhcpSnoop,
       "dhcpSnoopPortTable": dhcpSnoopPortTable,
       "dhcpSnoopPortEntry": dhcpSnoopPortEntry,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopMaxcnt": dhcpSnoopMaxcnt,
       "dhcpSnoopSmacverifyEnable": dhcpSnoopSmacverifyEnable,
       "dhcpSnoopTarget": dhcpSnoopTarget,
       "dhcpSnoopOps": dhcpSnoopOps,
       "dhcpStaticTable": dhcpStaticTable,
       "dhcpStaticEntry": dhcpStaticEntry,
       "dhcpStaticIpAddr": dhcpStaticIpAddr,
       "dhcpStaticRowStatus": dhcpStaticRowStatus,
       "maxNumOfDhcpStaticIp": maxNumOfDhcpStaticIp,
       "dhcpSnoopMaxcntMode": dhcpSnoopMaxcntMode,
       "acl": acl,
       "aclSetTable": aclSetTable,
       "aclSetEntry": aclSetEntry,
       "aclSetVpi": aclSetVpi,
       "aclSetVci": aclSetVci,
       "aclSetProfileName": aclSetProfileName,
       "aclSetRowStatus": aclSetRowStatus,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileRuleName": aclProfileRuleName,
       "aclProfileRuleNumber": aclProfileRuleNumber,
       "aclProfileActionNumber": aclProfileActionNumber,
       "aclProfileRuleParamMask": aclProfileRuleParamMask,
       "aclProfileRuleEtype": aclProfileRuleEtype,
       "aclProfileRuleVid": aclProfileRuleVid,
       "aclProfileRuleSmac": aclProfileRuleSmac,
       "aclProfileRuleDmac": aclProfileRuleDmac,
       "aclProfileRulePriority": aclProfileRulePriority,
       "aclProfileRuleProtocol": aclProfileRuleProtocol,
       "aclProfileRuleSrcIP": aclProfileRuleSrcIP,
       "aclProfileRuleSrcIPMask": aclProfileRuleSrcIPMask,
       "aclProfileRuleDestIP": aclProfileRuleDestIP,
       "aclProfileRuleDestIPMask": aclProfileRuleDestIPMask,
       "aclProfileRuleStartTos": aclProfileRuleStartTos,
       "aclProfileRuleEndTos": aclProfileRuleEndTos,
       "aclProfileRuleSrcStartPort": aclProfileRuleSrcStartPort,
       "aclProfileRuleSrcEndPort": aclProfileRuleSrcEndPort,
       "aclProfileRuleDestStartPort": aclProfileRuleDestStartPort,
       "aclProfileRuleDestEndPort": aclProfileRuleDestEndPort,
       "aclProfileActionRate": aclProfileActionRate,
       "aclProfileActionrvlan": aclProfileActionrvlan,
       "aclProfileActionrpri": aclProfileActionrpri,
       "aclProfileRowStatus": aclProfileRowStatus,
       "pppoeAgent": pppoeAgent,
       "pppoeAgentTable": pppoeAgentTable,
       "pppoeAgentEntry": pppoeAgentEntry,
       "pppoeAgentEnable": pppoeAgentEnable,
       "pppoeAgentInfo": pppoeAgentInfo,
       "pppoeAgentRowStatus": pppoeAgentRowStatus,
       "pppoeAgentOptionMode": pppoeAgentOptionMode,
       "maxNumOfPppoeDhcpRelay82Conf": maxNumOfPppoeDhcpRelay82Conf,
       "macff": macff,
       "macFfTable": macFfTable,
       "macFfEntry": macFfEntry,
       "macFfIndex": macFfIndex,
       "macFfVid": macFfVid,
       "macFfArIP": macFfArIP,
       "macFfSrcIP": macFfSrcIP,
       "macFfSrcMask": macFfSrcMask,
       "macFfRowStatus": macFfRowStatus,
       "macFfArpFlush": macFfArpFlush,
       "maxNumOfMacFfVlanInSystem": maxNumOfMacFfVlanInSystem,
       "macFfVlanTable": macFfVlanTable,
       "macFfVlanEntry": macFfVlanEntry,
       "macFfVlanRowstatus": macFfVlanRowstatus,
       "macFfVlanUnknownUnicast": macFfVlanUnknownUnicast,
       "macFfStaticIPTable": macFfStaticIPTable,
       "macFfStaticIPEntry": macFfStaticIPEntry,
       "macFfStaticIPPort": macFfStaticIPPort,
       "macFfStaticIPVid": macFfStaticIPVid,
       "macFfstaticIP": macFfstaticIP,
       "macFfStaticIPMask": macFfStaticIPMask,
       "macFfStaticIPRowStatus": macFfStaticIPRowStatus,
       "sys": sys,
       "accessCtrl": accessCtrl,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "securedClientEnable": securedClientEnable,
       "extAlarm": extAlarm,
       "extAlarmTable": extAlarmTable,
       "extAlarmEntry": extAlarmEntry,
       "extAlarmIndex": extAlarmIndex,
       "extAlarmname": extAlarmname,
       "extAlarmstatus": extAlarmstatus,
       "extAlarmTriggeredMode": extAlarmTriggeredMode,
       "user": user,
       "userAuthMode": userAuthMode,
       "userAuthServerIp": userAuthServerIp,
       "userAuthServerPort": userAuthServerPort,
       "userAuthServerSecret": userAuthServerSecret,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userPassword": userPassword,
       "userPriviledge": userPriviledge,
       "userRowStatus": userRowStatus,
       "userAuthDefaultPriviledge": userAuthDefaultPriviledge,
       "usbCastCtrl": usbCastCtrl,
       "usBcastCtrlEnable": usBcastCtrlEnable,
       "usBcastCtrlRate": usBcastCtrlRate,
       "dsbCastCtrl": dsbCastCtrl,
       "dsBcastCtrlEnable": dsBcastCtrlEnable,
       "dsBcastCtrlRate": dsBcastCtrlRate,
       "stdioTimeout": stdioTimeout,
       "isConfigChanged": isConfigChanged,
       "fwUpgrade": fwUpgrade,
       "fwUpgradeVersion": fwUpgradeVersion,
       "fwUpgradeCheck": fwUpgradeCheck,
       "fwUpgradeStatus": fwUpgradeStatus,
       "delayedReboot": delayedReboot,
       "delayedRebootTimer": delayedRebootTimer,
       "delayedRebootRemainingTime": delayedRebootRemainingTime,
       "delayedRebootCancel": delayedRebootCancel,
       "trap": trap,
       "statistics": statistics,
       "igmpQueryCntTotal": igmpQueryCntTotal,
       "igmpReportCntTotal": igmpReportCntTotal,
       "igmpLeaveCntTotal": igmpLeaveCntTotal,
       "igmpNumOfActiveGroups": igmpNumOfActiveGroups,
       "igmpGroupTable": igmpGroupTable,
       "igmpGroupEntry": igmpGroupEntry,
       "igmpGroupIp": igmpGroupIp,
       "igmpGroupvid": igmpGroupvid,
       "igmpGroupnumberOfMembers": igmpGroupnumberOfMembers,
       "igmpGroupMemberPorts": igmpGroupMemberPorts,
       "igmpGroupPortTable": igmpGroupPortTable,
       "igmpGroupPortEntry": igmpGroupPortEntry,
       "igmpGroupPortIp": igmpGroupPortIp,
       "igmpGroupPortvid": igmpGroupPortvid,
       "igmpGroupV2Table": igmpGroupV2Table,
       "igmpGroupV2Entry": igmpGroupV2Entry,
       "igmpGroupV2Vid": igmpGroupV2Vid,
       "igmpGroupV2Ip": igmpGroupV2Ip,
       "igmpGroupV2NumOfMembers": igmpGroupV2NumOfMembers,
       "igmpGroupV2MemberPorts": igmpGroupV2MemberPorts,
       "igmpGroupPortV2Table": igmpGroupPortV2Table,
       "igmpGroupPortV2Entry": igmpGroupPortV2Entry,
       "igmpGroupPortV2Vid": igmpGroupPortV2Vid,
       "igmpGroupPortV2Ip": igmpGroupPortV2Ip,
       "igmpGroupPortV2SourceIp": igmpGroupPortV2SourceIp,
       "igmpPortCtrlPduTable": igmpPortCtrlPduTable,
       "igmpPortCtrlPduEntry": igmpPortCtrlPduEntry,
       "igmpPortCtrlPduQueryCnt": igmpPortCtrlPduQueryCnt,
       "igmpPortCtrlPduReportCnt": igmpPortCtrlPduReportCnt,
       "igmpPortCtrlPduLeaveCnt": igmpPortCtrlPduLeaveCnt,
       "igmpPortNumOfActiveGroups": igmpPortNumOfActiveGroups,
       "igmpPortCtrlAuditLeaveCnt": igmpPortCtrlAuditLeaveCnt,
       "dhcpStats": dhcpStats,
       "dhcpSnoopIpTable": dhcpSnoopIpTable,
       "dhcpSnoopIpEntry": dhcpSnoopIpEntry,
       "dhcpSnoopIp": dhcpSnoopIp,
       "dhcpSnoopMac": dhcpSnoopMac,
       "dhcpSnoopVid": dhcpSnoopVid,
       "dhcpSnoopMask": dhcpSnoopMask,
       "dhcpSnoopGateway": dhcpSnoopGateway,
       "dhcpSnoopRouteMap": dhcpSnoopRouteMap,
       "dhcpSnoopCounterTable": dhcpSnoopCounterTable,
       "dhcpSnoopCounterEntry": dhcpSnoopCounterEntry,
       "dhcpDiscovery": dhcpDiscovery,
       "dhcpOffer": dhcpOffer,
       "dhcpRequest": dhcpRequest,
       "dhcpAck": dhcpAck,
       "dhcpAckBySnoopFull": dhcpAckBySnoopFull,
       "dhcpRouteTable": dhcpRouteTable,
       "dhcpRouteEntry": dhcpRouteEntry,
       "dhcpRouteIndex": dhcpRouteIndex,
       "dhcpRouteVid": dhcpRouteVid,
       "dhcpRouteIP": dhcpRouteIP,
       "dhcpRouteMask": dhcpRouteMask,
       "dhcpRouteGwIP": dhcpRouteGwIP,
       "paepvcStats": paepvcStats,
       "paepvcSessionTable": paepvcSessionTable,
       "paepvcSessionEntry": paepvcSessionEntry,
       "paepvcSessionVpi": paepvcSessionVpi,
       "paepvcSessionVci": paepvcSessionVci,
       "paepvcSessionState": paepvcSessionState,
       "paepvcSessionId": paepvcSessionId,
       "paepvcSessionUptime": paepvcSessionUptime,
       "paepvcSessionacname": paepvcSessionacname,
       "paepvcSessionsrvcname": paepvcSessionsrvcname,
       "paepvcCountTable": paepvcCountTable,
       "paepvcCountEntry": paepvcCountEntry,
       "paepvcCountVpi": paepvcCountVpi,
       "paepvcCountVci": paepvcCountVci,
       "paepvcCountPppLcpCfgReqRx": paepvcCountPppLcpCfgReqRx,
       "paepvcCountPppLcpEchoReqRx": paepvcCountPppLcpEchoReqRx,
       "paepvcCountPppLcpEchoReplyRx": paepvcCountPppLcpEchoReplyRx,
       "paepvcCountPadiTx": paepvcCountPadiTx,
       "paepvcCountPadoRx": paepvcCountPadoRx,
       "paepvcCountPadrTx": paepvcCountPadrTx,
       "paepvcCountPadsRx": paepvcCountPadsRx,
       "paepvcCountPadtTx": paepvcCountPadtTx,
       "paepvcCountPadtRx": paepvcCountPadtRx,
       "paepvcCountSrvcnameErrRx": paepvcCountSrvcnameErrRx,
       "paepvcCountAcSystemErrRx": paepvcCountAcSystemErrRx,
       "paepvcCountGenericErrTx": paepvcCountGenericErrTx,
       "paepvcCountGenericErrRx": paepvcCountGenericErrRx,
       "macStats": macStats,
       "macDisplayTarget": macDisplayTarget,
       "macTable": macTable,
       "macEntry": macEntry,
       "macAddress": macAddress,
       "macPort": macPort,
       "macStatus": macStatus,
       "ipbpvcStats": ipbpvcStats,
       "arpproxyTable": arpproxyTable,
       "arpproxyEntry": arpproxyEntry,
       "arpproxyIp": arpproxyIp,
       "arpproxyMac": arpproxyMac,
       "arpproxyIfIndex": arpproxyIfIndex,
       "arpproxyVpi": arpproxyVpi,
       "arpproxyVci": arpproxyVci,
       "arpproxyInterfaceIp": arpproxyInterfaceIp,
       "arpproxyInterfaceMask": arpproxyInterfaceMask,
       "arpproxyInterfaceVid": arpproxyInterfaceVid,
       "arpproxyDhcpIp": arpproxyDhcpIp,
       "arpproxyType": arpproxyType,
       "ipbpvcIfDynamicTable": ipbpvcIfDynamicTable,
       "ipbpvcIfDynamicEntry": ipbpvcIfDynamicEntry,
       "ipbpvcIfDynamicIp": ipbpvcIfDynamicIp,
       "ipbpvcIfDynamicMask": ipbpvcIfDynamicMask,
       "ipbpvcIfDynamicIfIndex": ipbpvcIfDynamicIfIndex,
       "ipbpvcIfDynamicVpi": ipbpvcIfDynamicVpi,
       "ipbpvcIfDynamicVci": ipbpvcIfDynamicVci,
       "ipbpvcRouteDynamicTable": ipbpvcRouteDynamicTable,
       "ipbpvcRouteDynamicEntry": ipbpvcRouteDynamicEntry,
       "ipbpvcRouteDynamicType": ipbpvcRouteDynamicType,
       "ipbpvcRouteDynamicIp": ipbpvcRouteDynamicIp,
       "ipbpvcRouteDynamicMask": ipbpvcRouteDynamicMask,
       "ipbpvcRouteDynamicNextHop": ipbpvcRouteDynamicNextHop,
       "ipbpvcRouteDynamicMetric": ipbpvcRouteDynamicMetric,
       "ipbpvcRouteDynamicPriority": ipbpvcRouteDynamicPriority,
       "voipStats": voipStats,
       "voipLineStatusTable": voipLineStatusTable,
       "voipLineStatusEntry": voipLineStatusEntry,
       "voipLineStatusPhoneStatus": voipLineStatusPhoneStatus,
       "voipLineStatusServiceStatus": voipLineStatusServiceStatus,
       "voipLineInfoTable": voipLineInfoTable,
       "voipLineInfoEntry": voipLineInfoEntry,
       "voipLineInfoSipLocalUri": voipLineInfoSipLocalUri,
       "voipLineInfoSipRemoteUri": voipLineInfoSipRemoteUri,
       "voipLineInfoRtpTxCodecType": voipLineInfoRtpTxCodecType,
       "voipLineInfoRtpRxCodecType": voipLineInfoRtpRxCodecType,
       "voipLineInfoRtpTxPt": voipLineInfoRtpTxPt,
       "voipLineInfoRtpRxPt": voipLineInfoRtpRxPt,
       "voipLineInfoRtpLocalIp": voipLineInfoRtpLocalIp,
       "voipLineInfoRtpRemoteIp": voipLineInfoRtpRemoteIp,
       "voipLineInfoRtpLocalPort": voipLineInfoRtpLocalPort,
       "voipLineInfoRtpRemotePort": voipLineInfoRtpRemotePort,
       "voipLineInfoSipLocalUri2": voipLineInfoSipLocalUri2,
       "voipLineInfoSipRemoteUri2": voipLineInfoSipRemoteUri2,
       "voipLineInfoRtpTxCodecType2": voipLineInfoRtpTxCodecType2,
       "voipLineInfoRtpRxCodecType2": voipLineInfoRtpRxCodecType2,
       "voipLineInfoRtpTxPt2": voipLineInfoRtpTxPt2,
       "voipLineInfoRtpRxPt2": voipLineInfoRtpRxPt2,
       "voipLineInfoRtpLocalIp2": voipLineInfoRtpLocalIp2,
       "voipLineInfoRtpRemoteIp2": voipLineInfoRtpRemoteIp2,
       "voipLineInfoRtpLocalPort2": voipLineInfoRtpLocalPort2,
       "voipLineInfoRtpRemotePort2": voipLineInfoRtpRemotePort2,
       "voipH248Status": voipH248Status,
       "voipH248StatusMgName": voipH248StatusMgName,
       "voipH248StatusMgStatus": voipH248StatusMgStatus,
       "voipActiveCallStat": voipActiveCallStat,
       "voipActiveCallStatCurrentActiveCalls": voipActiveCallStatCurrentActiveCalls,
       "voipActiveCallStatFailAttempts": voipActiveCallStatFailAttempts,
       "macffStats": macffStats,
       "macFfStatsTable": macFfStatsTable,
       "macFfStatsEntry": macFfStatsEntry,
       "macFfStatsIndex": macFfStatsIndex,
       "macFfStatsVid": macFfStatsVid,
       "macFfStatsArIP": macFfStatsArIP,
       "macFfStatsSrcIP": macFfStatsSrcIP,
       "macFfStatsSrcMask": macFfStatsSrcMask,
       "macFfArpTable": macFfArpTable,
       "macFfArpEntry": macFfArpEntry,
       "macFfArpVid": macFfArpVid,
       "macFfArpIP": macFfArpIP,
       "macFfArpPort": macFfArpPort,
       "macFfArpMac": macFfArpMac,
       "macFfArpCounterTable": macFfArpCounterTable,
       "macFfArpCounterEntry": macFfArpCounterEntry,
       "macFfArpCounterRequestTX": macFfArpCounterRequestTX,
       "macFfArpCounterRequestRX": macFfArpCounterRequestRX,
       "macFfArpCounterRequestRXDrop": macFfArpCounterRequestRXDrop,
       "macFfArpCounterReplyTX": macFfArpCounterReplyTX,
       "macFfArpCounterReplyRX": macFfArpCounterReplyRX,
       "macFfArpCounterReplyRXDrop": macFfArpCounterReplyRXDrop,
       "enetStats": enetStats,
       "enetSfpInfoTable": enetSfpInfoTable,
       "enetSfpInfoEntry": enetSfpInfoEntry,
       "enetSfpInfoTxpower": enetSfpInfoTxpower,
       "enetSfpInfoRxpower": enetSfpInfoRxpower,
       "enetSfpInfoTemperature": enetSfpInfoTemperature,
       "enetSfpInfoTxBias": enetSfpInfoTxBias,
       "enetSfpInfoVoltage": enetSfpInfoVoltage,
       "adslStats": adslStats,
       "adslPortUtilTable": adslPortUtilTable,
       "adslPortUtilEntry": adslPortUtilEntry,
       "adslPortUtilTx": adslPortUtilTx,
       "adslPortUtilRx": adslPortUtilRx,
       "clear": clear,
       "counterClearTarget": counterClearTarget,
       "counterClearOps": counterClearOps,
       "counterClearVpi": counterClearVpi,
       "counterClearVci": counterClearVci,
       "voip": voip,
       "voipArp": voipArp,
       "voipArpFlushOps": voipArpFlushOps,
       "voipArpShowTable": voipArpShowTable,
       "voipArpShowEntry": voipArpShowEntry,
       "voipArpShowIp": voipArpShowIp,
       "voipArpShowMac": voipArpShowMac,
       "voipSip": voipSip,
       "maxNumOfVoipNumberPlan": maxNumOfVoipNumberPlan,
       "voipNumberPlanTable": voipNumberPlanTable,
       "voipNumberPlanEntry": voipNumberPlanEntry,
       "voipNumberPlanName": voipNumberPlanName,
       "voipNumberPlanIndex": voipNumberPlanIndex,
       "voipNumberPlanPattern": voipNumberPlanPattern,
       "voipNumberPlanRule": voipNumberPlanRule,
       "voipNumberPlanRowStatus": voipNumberPlanRowStatus,
       "voipNumberPlanDftTable": voipNumberPlanDftTable,
       "voipNumberPlanDftEntry": voipNumberPlanDftEntry,
       "voipNumberPlanDftRule": voipNumberPlanDftRule,
       "digitSetup": digitSetup,
       "timeoutSetup": timeoutSetup,
       "initialTimeout": initialTimeout,
       "interDigitTimeout": interDigitTimeout,
       "digitPauseTimeout": digitPauseTimeout,
       "matchingTimeout": matchingTimeout,
       "voipIp": voipIp,
       "voipIpSetIp": voipIpSetIp,
       "voipIpSetVid": voipIpSetVid,
       "voipIpSetMask": voipIpSetMask,
       "voipDns": voipDns,
       "voipDnsIp": voipDnsIp,
       "maxNumOfVoipRoute": maxNumOfVoipRoute,
       "voipRouteTable": voipRouteTable,
       "voipRouteEntry": voipRouteEntry,
       "voipRouteIp": voipRouteIp,
       "voipRouteGateway": voipRouteGateway,
       "voipRouteMask": voipRouteMask,
       "voipRouteMetric": voipRouteMetric,
       "voipRouteRowStatus": voipRouteRowStatus,
       "voipCountryCode": voipCountryCode,
       "voipH248": voipH248,
       "maxNumOfVoipH248MgConf": maxNumOfVoipH248MgConf,
       "voipH248MgConf": voipH248MgConf,
       "voipH248MgName": voipH248MgName,
       "voipH248MgEnable": voipH248MgEnable,
       "voipH248MgH248Profile": voipH248MgH248Profile,
       "voipH248MgPort": voipH248MgPort,
       "voipRing": voipRing,
       "voipRingTable": voipRingTable,
       "voipRingEntry": voipRingEntry,
       "voipRingIndex": voipRingIndex,
       "voipRingName": voipRingName,
       "voipRingOn1": voipRingOn1,
       "voipRingOff1": voipRingOff1,
       "voipRingOn2": voipRingOn2,
       "voipRingOff2": voipRingOff2,
       "voipRingOn3": voipRingOn3,
       "voipRingOff3": voipRingOff3,
       "voipRingSetDefault": voipRingSetDefault,
       "voipBootRegDelay": voipBootRegDelay,
       "voipActiveCall": voipActiveCall,
       "voipActiveCallMaxActiveCalls": voipActiveCallMaxActiveCalls,
       "voipActiveCallThreshold": voipActiveCallThreshold,
       "voipMode": voipMode,
       "aesSeriesCommon": aesSeriesCommon,
       "iesSeriesCommon": iesSeriesCommon,
       "accessSwitchCommonATM": accessSwitchCommonATM}
)
