# SNMP MIB module (CISCO-CABLE-QOS-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-QOS-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:39 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableQosMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341)
)
ciscoCableQosMonitorMIB.setRevisions(
        ("2004-02-20 00:00",
         "2003-04-03 00:00",
         "2003-03-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CCQMRuleDirection(Integer32, TextualConvention):
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
        *(("bidirection", 3),
          ("downstream", 2),
          ("upstream", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCableQosMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableQosMonitorMIBObjects = _CiscoCableQosMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1)
)
_CcqmEnforceRuleObjects_ObjectIdentity = ObjectIdentity
ccqmEnforceRuleObjects = _CcqmEnforceRuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1)
)
_CcqmCmtsEnforceRuleTable_Object = MibTable
ccqmCmtsEnforceRuleTable = _CcqmCmtsEnforceRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccqmCmtsEnforceRuleTable.setStatus("current")
_CcqmCmtsEnforceRuleEntry_Object = MibTableRow
ccqmCmtsEnforceRuleEntry = _CcqmCmtsEnforceRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1)
)
ccqmCmtsEnforceRuleEntry.setIndexNames(
    (0, "CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleName"),
)
if mibBuilder.loadTexts:
    ccqmCmtsEnforceRuleEntry.setStatus("current")


class _CcqmCmtsEnfRuleName_Type(DisplayString):
    """Custom type ccqmCmtsEnfRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CcqmCmtsEnfRuleName_Type.__name__ = "DisplayString"
_CcqmCmtsEnfRuleName_Object = MibTableColumn
ccqmCmtsEnfRuleName = _CcqmCmtsEnfRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 1),
    _CcqmCmtsEnfRuleName_Type()
)
ccqmCmtsEnfRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleName.setStatus("current")


class _CcqmCmtsEnfRuleRegQoS_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleRegQoS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CcqmCmtsEnfRuleRegQoS_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleRegQoS_Object = MibTableColumn
ccqmCmtsEnfRuleRegQoS = _CcqmCmtsEnfRuleRegQoS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 2),
    _CcqmCmtsEnfRuleRegQoS_Type()
)
ccqmCmtsEnfRuleRegQoS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleRegQoS.setStatus("current")


class _CcqmCmtsEnfRuleEnfQos_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleEnfQos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CcqmCmtsEnfRuleEnfQos_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleEnfQos_Object = MibTableColumn
ccqmCmtsEnfRuleEnfQos = _CcqmCmtsEnfRuleEnfQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 3),
    _CcqmCmtsEnfRuleEnfQos_Type()
)
ccqmCmtsEnfRuleEnfQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleEnfQos.setStatus("current")


class _CcqmCmtsEnfRuleMonDuration_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleMonDuration based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 44640),
    )


_CcqmCmtsEnfRuleMonDuration_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleMonDuration_Object = MibTableColumn
ccqmCmtsEnfRuleMonDuration = _CcqmCmtsEnfRuleMonDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 4),
    _CcqmCmtsEnfRuleMonDuration_Type()
)
ccqmCmtsEnfRuleMonDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleMonDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleMonDuration.setUnits("minutes")
_CcqmCmtsEnfRuleSampleRate_Type = Unsigned32
_CcqmCmtsEnfRuleSampleRate_Object = MibTableColumn
ccqmCmtsEnfRuleSampleRate = _CcqmCmtsEnfRuleSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 5),
    _CcqmCmtsEnfRuleSampleRate_Type()
)
ccqmCmtsEnfRuleSampleRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSampleRate.setUnits("minutes")


class _CcqmCmtsEnfRulePenaltyPeriod_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRulePenaltyPeriod based on Unsigned32"""
    defaultValue = 10080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_CcqmCmtsEnfRulePenaltyPeriod_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRulePenaltyPeriod_Object = MibTableColumn
ccqmCmtsEnfRulePenaltyPeriod = _CcqmCmtsEnfRulePenaltyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 6),
    _CcqmCmtsEnfRulePenaltyPeriod_Type()
)
ccqmCmtsEnfRulePenaltyPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRulePenaltyPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRulePenaltyPeriod.setUnits("minutes")
_CcqmCmtsEnfRuleByteCount_Type = Unsigned32
_CcqmCmtsEnfRuleByteCount_Object = MibTableColumn
ccqmCmtsEnfRuleByteCount = _CcqmCmtsEnfRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 7),
    _CcqmCmtsEnfRuleByteCount_Type()
)
ccqmCmtsEnfRuleByteCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleByteCount.setStatus("obsolete")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleByteCount.setUnits("1000 bytes")
_CcqmCmtsEnfRuleDirection_Type = CCQMRuleDirection
_CcqmCmtsEnfRuleDirection_Object = MibTableColumn
ccqmCmtsEnfRuleDirection = _CcqmCmtsEnfRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 8),
    _CcqmCmtsEnfRuleDirection_Type()
)
ccqmCmtsEnfRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleDirection.setStatus("current")


class _CcqmCmtsEnfRuleAutoEnforce_Type(TruthValue):
    """Custom type ccqmCmtsEnfRuleAutoEnforce based on TruthValue"""


_CcqmCmtsEnfRuleAutoEnforce_Object = MibTableColumn
ccqmCmtsEnfRuleAutoEnforce = _CcqmCmtsEnfRuleAutoEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 9),
    _CcqmCmtsEnfRuleAutoEnforce_Type()
)
ccqmCmtsEnfRuleAutoEnforce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleAutoEnforce.setStatus("current")
_CcqmCmtsEnfRuleRowStatus_Type = RowStatus
_CcqmCmtsEnfRuleRowStatus_Object = MibTableColumn
ccqmCmtsEnfRuleRowStatus = _CcqmCmtsEnfRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 10),
    _CcqmCmtsEnfRuleRowStatus_Type()
)
ccqmCmtsEnfRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleRowStatus.setStatus("current")
_CcqmCmtsEnfRuleAvgRate_Type = Unsigned32
_CcqmCmtsEnfRuleAvgRate_Object = MibTableColumn
ccqmCmtsEnfRuleAvgRate = _CcqmCmtsEnfRuleAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 11),
    _CcqmCmtsEnfRuleAvgRate_Type()
)
ccqmCmtsEnfRuleAvgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleAvgRate.setUnits("kbits/sec")


class _CcqmCmtsEnfRuleDocsVer_Type(Integer32):
    """Custom type ccqmCmtsEnfRuleDocsVer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis10", 2),
          ("others", 1))
    )


_CcqmCmtsEnfRuleDocsVer_Type.__name__ = "Integer32"
_CcqmCmtsEnfRuleDocsVer_Object = MibTableColumn
ccqmCmtsEnfRuleDocsVer = _CcqmCmtsEnfRuleDocsVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 12),
    _CcqmCmtsEnfRuleDocsVer_Type()
)
ccqmCmtsEnfRuleDocsVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleDocsVer.setStatus("current")


class _CcqmCmtsEnfRuleRegSerClassName_Type(DisplayString):
    """Custom type ccqmCmtsEnfRuleRegSerClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcqmCmtsEnfRuleRegSerClassName_Type.__name__ = "DisplayString"
_CcqmCmtsEnfRuleRegSerClassName_Object = MibTableColumn
ccqmCmtsEnfRuleRegSerClassName = _CcqmCmtsEnfRuleRegSerClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 13),
    _CcqmCmtsEnfRuleRegSerClassName_Type()
)
ccqmCmtsEnfRuleRegSerClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleRegSerClassName.setStatus("current")


class _CcqmCmtsEnfRuleEnfSerClassName_Type(DisplayString):
    """Custom type ccqmCmtsEnfRuleEnfSerClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcqmCmtsEnfRuleEnfSerClassName_Type.__name__ = "DisplayString"
_CcqmCmtsEnfRuleEnfSerClassName_Object = MibTableColumn
ccqmCmtsEnfRuleEnfSerClassName = _CcqmCmtsEnfRuleEnfSerClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 14),
    _CcqmCmtsEnfRuleEnfSerClassName_Type()
)
ccqmCmtsEnfRuleEnfSerClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleEnfSerClassName.setStatus("current")


class _CcqmCmtsEnfRuleMonType_Type(Integer32):
    """Custom type ccqmCmtsEnfRuleMonType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("peakOffPeak", 2))
    )


_CcqmCmtsEnfRuleMonType_Type.__name__ = "Integer32"
_CcqmCmtsEnfRuleMonType_Object = MibTableColumn
ccqmCmtsEnfRuleMonType = _CcqmCmtsEnfRuleMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 15),
    _CcqmCmtsEnfRuleMonType_Type()
)
ccqmCmtsEnfRuleMonType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleMonType.setStatus("current")


class _CcqmCmtsEnfRuleFirstPeakTime_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleFirstPeakTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcqmCmtsEnfRuleFirstPeakTime_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleFirstPeakTime_Object = MibTableColumn
ccqmCmtsEnfRuleFirstPeakTime = _CcqmCmtsEnfRuleFirstPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 16),
    _CcqmCmtsEnfRuleFirstPeakTime_Type()
)
ccqmCmtsEnfRuleFirstPeakTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleFirstPeakTime.setStatus("current")


class _CcqmCmtsEnfRuleFirstDuration_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleFirstDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1440),
    )


_CcqmCmtsEnfRuleFirstDuration_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleFirstDuration_Object = MibTableColumn
ccqmCmtsEnfRuleFirstDuration = _CcqmCmtsEnfRuleFirstDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 17),
    _CcqmCmtsEnfRuleFirstDuration_Type()
)
ccqmCmtsEnfRuleFirstDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleFirstDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleFirstDuration.setUnits("minutes")
_CcqmCmtsEnfRuleFirstAvgRate_Type = Unsigned32
_CcqmCmtsEnfRuleFirstAvgRate_Object = MibTableColumn
ccqmCmtsEnfRuleFirstAvgRate = _CcqmCmtsEnfRuleFirstAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 18),
    _CcqmCmtsEnfRuleFirstAvgRate_Type()
)
ccqmCmtsEnfRuleFirstAvgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleFirstAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleFirstAvgRate.setUnits("kbits/sec")


class _CcqmCmtsEnfRuleSecondPeakTime_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleSecondPeakTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcqmCmtsEnfRuleSecondPeakTime_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleSecondPeakTime_Object = MibTableColumn
ccqmCmtsEnfRuleSecondPeakTime = _CcqmCmtsEnfRuleSecondPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 19),
    _CcqmCmtsEnfRuleSecondPeakTime_Type()
)
ccqmCmtsEnfRuleSecondPeakTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSecondPeakTime.setStatus("current")


class _CcqmCmtsEnfRuleSecondDuration_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleSecondDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1380),
    )


_CcqmCmtsEnfRuleSecondDuration_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleSecondDuration_Object = MibTableColumn
ccqmCmtsEnfRuleSecondDuration = _CcqmCmtsEnfRuleSecondDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 20),
    _CcqmCmtsEnfRuleSecondDuration_Type()
)
ccqmCmtsEnfRuleSecondDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSecondDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSecondDuration.setUnits("minutes")
_CcqmCmtsEnfRuleSecondAvgRate_Type = Unsigned32
_CcqmCmtsEnfRuleSecondAvgRate_Object = MibTableColumn
ccqmCmtsEnfRuleSecondAvgRate = _CcqmCmtsEnfRuleSecondAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 21),
    _CcqmCmtsEnfRuleSecondAvgRate_Type()
)
ccqmCmtsEnfRuleSecondAvgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSecondAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleSecondAvgRate.setUnits("kbits/sec")


class _CcqmCmtsEnfRuleOffPeakDuration_Type(Unsigned32):
    """Custom type ccqmCmtsEnfRuleOffPeakDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1380),
    )


_CcqmCmtsEnfRuleOffPeakDuration_Type.__name__ = "Unsigned32"
_CcqmCmtsEnfRuleOffPeakDuration_Object = MibTableColumn
ccqmCmtsEnfRuleOffPeakDuration = _CcqmCmtsEnfRuleOffPeakDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 22),
    _CcqmCmtsEnfRuleOffPeakDuration_Type()
)
ccqmCmtsEnfRuleOffPeakDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleOffPeakDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleOffPeakDuration.setUnits("minutes")
_CcqmCmtsEnfRuleOffPeakAvgRate_Type = Unsigned32
_CcqmCmtsEnfRuleOffPeakAvgRate_Object = MibTableColumn
ccqmCmtsEnfRuleOffPeakAvgRate = _CcqmCmtsEnfRuleOffPeakAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 1, 1, 1, 23),
    _CcqmCmtsEnfRuleOffPeakAvgRate_Type()
)
ccqmCmtsEnfRuleOffPeakAvgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleOffPeakAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsEnfRuleOffPeakAvgRate.setUnits("kbits/sec")
_CcqmRuleViolateObjects_ObjectIdentity = ObjectIdentity
ccqmRuleViolateObjects = _CcqmRuleViolateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2)
)
_CcqmEnfRuleViolateTable_Object = MibTable
ccqmEnfRuleViolateTable = _CcqmEnfRuleViolateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateTable.setStatus("current")
_CcqmEnfRuleViolateEntry_Object = MibTableRow
ccqmEnfRuleViolateEntry = _CcqmEnfRuleViolateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1)
)
ccqmEnfRuleViolateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateID"),
)
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateEntry.setStatus("current")
_CcqmEnfRuleViolateID_Type = Unsigned32
_CcqmEnfRuleViolateID_Object = MibTableColumn
ccqmEnfRuleViolateID = _CcqmEnfRuleViolateID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 1),
    _CcqmEnfRuleViolateID_Type()
)
ccqmEnfRuleViolateID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateID.setStatus("current")
_CcqmEnfRuleViolateMacAddr_Type = MacAddress
_CcqmEnfRuleViolateMacAddr_Object = MibTableColumn
ccqmEnfRuleViolateMacAddr = _CcqmEnfRuleViolateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 2),
    _CcqmEnfRuleViolateMacAddr_Type()
)
ccqmEnfRuleViolateMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateMacAddr.setStatus("current")


class _CcqmEnfRuleViolateRuleName_Type(DisplayString):
    """Custom type ccqmEnfRuleViolateRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CcqmEnfRuleViolateRuleName_Type.__name__ = "DisplayString"
_CcqmEnfRuleViolateRuleName_Object = MibTableColumn
ccqmEnfRuleViolateRuleName = _CcqmEnfRuleViolateRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 3),
    _CcqmEnfRuleViolateRuleName_Type()
)
ccqmEnfRuleViolateRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateRuleName.setStatus("current")
_CcqmEnfRuleViolateByteCount_Type = Unsigned32
_CcqmEnfRuleViolateByteCount_Object = MibTableColumn
ccqmEnfRuleViolateByteCount = _CcqmEnfRuleViolateByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 4),
    _CcqmEnfRuleViolateByteCount_Type()
)
ccqmEnfRuleViolateByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateByteCount.setStatus("current")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateByteCount.setUnits("kbytes")
_CcqmEnfRuleViolateLastDetectTime_Type = DateAndTime
_CcqmEnfRuleViolateLastDetectTime_Object = MibTableColumn
ccqmEnfRuleViolateLastDetectTime = _CcqmEnfRuleViolateLastDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 5),
    _CcqmEnfRuleViolateLastDetectTime_Type()
)
ccqmEnfRuleViolateLastDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateLastDetectTime.setStatus("current")
_CcqmEnfRuleViolatePenaltyExpTime_Type = DateAndTime
_CcqmEnfRuleViolatePenaltyExpTime_Object = MibTableColumn
ccqmEnfRuleViolatePenaltyExpTime = _CcqmEnfRuleViolatePenaltyExpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 2, 1, 6),
    _CcqmEnfRuleViolatePenaltyExpTime_Type()
)
ccqmEnfRuleViolatePenaltyExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolatePenaltyExpTime.setStatus("current")


class _CcqmEnfRuleViolateNotifEnable_Type(TruthValue):
    """Custom type ccqmEnfRuleViolateNotifEnable based on TruthValue"""


_CcqmEnfRuleViolateNotifEnable_Object = MibScalar
ccqmEnfRuleViolateNotifEnable = _CcqmEnfRuleViolateNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 2, 3),
    _CcqmEnfRuleViolateNotifEnable_Type()
)
ccqmEnfRuleViolateNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateNotifEnable.setStatus("current")
_CcqmRuleIfBwUtilObjects_ObjectIdentity = ObjectIdentity
ccqmRuleIfBwUtilObjects = _CcqmRuleIfBwUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3)
)
_CcqmCmtsIfBwUtilTable_Object = MibTable
ccqmCmtsIfBwUtilTable = _CcqmCmtsIfBwUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilTable.setStatus("current")
_CcqmCmtsIfBwUtilEntry_Object = MibTableRow
ccqmCmtsIfBwUtilEntry = _CcqmCmtsIfBwUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3, 1, 1)
)
ccqmCmtsIfBwUtilEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilEntry.setStatus("current")


class _CcqmCmtsIfBwUtilUpThreshold_Type(Unsigned32):
    """Custom type ccqmCmtsIfBwUtilUpThreshold based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcqmCmtsIfBwUtilUpThreshold_Type.__name__ = "Unsigned32"
_CcqmCmtsIfBwUtilUpThreshold_Object = MibTableColumn
ccqmCmtsIfBwUtilUpThreshold = _CcqmCmtsIfBwUtilUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3, 1, 1, 1),
    _CcqmCmtsIfBwUtilUpThreshold_Type()
)
ccqmCmtsIfBwUtilUpThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilUpThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilUpThreshold.setUnits("percent")


class _CcqmCmtsIfBwUtilLoThreshold_Type(Unsigned32):
    """Custom type ccqmCmtsIfBwUtilLoThreshold based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcqmCmtsIfBwUtilLoThreshold_Type.__name__ = "Unsigned32"
_CcqmCmtsIfBwUtilLoThreshold_Object = MibTableColumn
ccqmCmtsIfBwUtilLoThreshold = _CcqmCmtsIfBwUtilLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3, 1, 1, 2),
    _CcqmCmtsIfBwUtilLoThreshold_Type()
)
ccqmCmtsIfBwUtilLoThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilLoThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilLoThreshold.setUnits("percent")
_CcqmCmtsIfBwUtilRowStatus_Type = RowStatus
_CcqmCmtsIfBwUtilRowStatus_Object = MibTableColumn
ccqmCmtsIfBwUtilRowStatus = _CcqmCmtsIfBwUtilRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 1, 3, 1, 1, 3),
    _CcqmCmtsIfBwUtilRowStatus_Type()
)
ccqmCmtsIfBwUtilRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccqmCmtsIfBwUtilRowStatus.setStatus("current")
_CcqmMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ccqmMIBNotificationsPrefix = _CcqmMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 2)
)
_CcqmMIBNotifications_ObjectIdentity = ObjectIdentity
ccqmMIBNotifications = _CcqmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 2, 0)
)
_CcqmMIBConformance_ObjectIdentity = ObjectIdentity
ccqmMIBConformance = _CcqmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3)
)
_CcqmMIBCompliances_ObjectIdentity = ObjectIdentity
ccqmMIBCompliances = _CcqmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 1)
)
_CcqmMIBGroups_ObjectIdentity = ObjectIdentity
ccqmMIBGroups = _CcqmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2)
)

# Managed Objects groups

ccqmEnfRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2, 1)
)
ccqmEnfRuleGroup.setObjects(
      *(("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleRegQoS"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleEnfQos"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleMonDuration"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleSampleRate"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRulePenaltyPeriod"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleByteCount"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleDirection"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleAutoEnforce"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ccqmEnfRuleGroup.setStatus("obsolete")

ccqmEnfRuleViolateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2, 2)
)
ccqmEnfRuleViolateGroup.setObjects(
      *(("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateRuleName"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateMacAddr"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateByteCount"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateLastDetectTime"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolatePenaltyExpTime"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateNotifEnable"))
)
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateGroup.setStatus("current")

ccqmEnfRuleGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2, 4)
)
ccqmEnfRuleGroupRev1.setObjects(
      *(("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleRegQoS"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleEnfQos"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleMonDuration"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleSampleRate"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRulePenaltyPeriod"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleDirection"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleAutoEnforce"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleRowStatus"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleAvgRate"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleDocsVer"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleRegSerClassName"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleEnfSerClassName"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleMonType"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleFirstPeakTime"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleFirstDuration"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleFirstAvgRate"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleSecondPeakTime"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleSecondDuration"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleSecondAvgRate"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleOffPeakDuration"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsEnfRuleOffPeakAvgRate"))
)
if mibBuilder.loadTexts:
    ccqmEnfRuleGroupRev1.setStatus("current")

ccqmCmtsRuleIfBwUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2, 5)
)
ccqmCmtsRuleIfBwUtilGroup.setObjects(
      *(("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsIfBwUtilUpThreshold"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsIfBwUtilLoThreshold"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmCmtsIfBwUtilRowStatus"))
)
if mibBuilder.loadTexts:
    ccqmCmtsRuleIfBwUtilGroup.setStatus("current")


# Notification objects

ccqmEnfRuleViolateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 2, 0, 1)
)
ccqmEnfRuleViolateNotification.setObjects(
      *(("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateMacAddr"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateRuleName"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolatePenaltyExpTime"),
        ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateByteCount"))
)
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateNotification.setStatus(
        "current"
    )


# Notifications groups

ccqmEnfRuleViolateNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 2, 3)
)
ccqmEnfRuleViolateNotifGroup.setObjects(
    ("CISCO-CABLE-QOS-MONITOR-MIB", "ccqmEnfRuleViolateNotification")
)
if mibBuilder.loadTexts:
    ccqmEnfRuleViolateNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ccqmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccqmCompliance.setStatus(
        "obsolete"
    )

ccqmComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 341, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccqmComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-QOS-MONITOR-MIB",
    **{"CCQMRuleDirection": CCQMRuleDirection,
       "ciscoCableQosMonitorMIB": ciscoCableQosMonitorMIB,
       "ciscoCableQosMonitorMIBObjects": ciscoCableQosMonitorMIBObjects,
       "ccqmEnforceRuleObjects": ccqmEnforceRuleObjects,
       "ccqmCmtsEnforceRuleTable": ccqmCmtsEnforceRuleTable,
       "ccqmCmtsEnforceRuleEntry": ccqmCmtsEnforceRuleEntry,
       "ccqmCmtsEnfRuleName": ccqmCmtsEnfRuleName,
       "ccqmCmtsEnfRuleRegQoS": ccqmCmtsEnfRuleRegQoS,
       "ccqmCmtsEnfRuleEnfQos": ccqmCmtsEnfRuleEnfQos,
       "ccqmCmtsEnfRuleMonDuration": ccqmCmtsEnfRuleMonDuration,
       "ccqmCmtsEnfRuleSampleRate": ccqmCmtsEnfRuleSampleRate,
       "ccqmCmtsEnfRulePenaltyPeriod": ccqmCmtsEnfRulePenaltyPeriod,
       "ccqmCmtsEnfRuleByteCount": ccqmCmtsEnfRuleByteCount,
       "ccqmCmtsEnfRuleDirection": ccqmCmtsEnfRuleDirection,
       "ccqmCmtsEnfRuleAutoEnforce": ccqmCmtsEnfRuleAutoEnforce,
       "ccqmCmtsEnfRuleRowStatus": ccqmCmtsEnfRuleRowStatus,
       "ccqmCmtsEnfRuleAvgRate": ccqmCmtsEnfRuleAvgRate,
       "ccqmCmtsEnfRuleDocsVer": ccqmCmtsEnfRuleDocsVer,
       "ccqmCmtsEnfRuleRegSerClassName": ccqmCmtsEnfRuleRegSerClassName,
       "ccqmCmtsEnfRuleEnfSerClassName": ccqmCmtsEnfRuleEnfSerClassName,
       "ccqmCmtsEnfRuleMonType": ccqmCmtsEnfRuleMonType,
       "ccqmCmtsEnfRuleFirstPeakTime": ccqmCmtsEnfRuleFirstPeakTime,
       "ccqmCmtsEnfRuleFirstDuration": ccqmCmtsEnfRuleFirstDuration,
       "ccqmCmtsEnfRuleFirstAvgRate": ccqmCmtsEnfRuleFirstAvgRate,
       "ccqmCmtsEnfRuleSecondPeakTime": ccqmCmtsEnfRuleSecondPeakTime,
       "ccqmCmtsEnfRuleSecondDuration": ccqmCmtsEnfRuleSecondDuration,
       "ccqmCmtsEnfRuleSecondAvgRate": ccqmCmtsEnfRuleSecondAvgRate,
       "ccqmCmtsEnfRuleOffPeakDuration": ccqmCmtsEnfRuleOffPeakDuration,
       "ccqmCmtsEnfRuleOffPeakAvgRate": ccqmCmtsEnfRuleOffPeakAvgRate,
       "ccqmRuleViolateObjects": ccqmRuleViolateObjects,
       "ccqmEnfRuleViolateTable": ccqmEnfRuleViolateTable,
       "ccqmEnfRuleViolateEntry": ccqmEnfRuleViolateEntry,
       "ccqmEnfRuleViolateID": ccqmEnfRuleViolateID,
       "ccqmEnfRuleViolateMacAddr": ccqmEnfRuleViolateMacAddr,
       "ccqmEnfRuleViolateRuleName": ccqmEnfRuleViolateRuleName,
       "ccqmEnfRuleViolateByteCount": ccqmEnfRuleViolateByteCount,
       "ccqmEnfRuleViolateLastDetectTime": ccqmEnfRuleViolateLastDetectTime,
       "ccqmEnfRuleViolatePenaltyExpTime": ccqmEnfRuleViolatePenaltyExpTime,
       "ccqmEnfRuleViolateNotifEnable": ccqmEnfRuleViolateNotifEnable,
       "ccqmRuleIfBwUtilObjects": ccqmRuleIfBwUtilObjects,
       "ccqmCmtsIfBwUtilTable": ccqmCmtsIfBwUtilTable,
       "ccqmCmtsIfBwUtilEntry": ccqmCmtsIfBwUtilEntry,
       "ccqmCmtsIfBwUtilUpThreshold": ccqmCmtsIfBwUtilUpThreshold,
       "ccqmCmtsIfBwUtilLoThreshold": ccqmCmtsIfBwUtilLoThreshold,
       "ccqmCmtsIfBwUtilRowStatus": ccqmCmtsIfBwUtilRowStatus,
       "ccqmMIBNotificationsPrefix": ccqmMIBNotificationsPrefix,
       "ccqmMIBNotifications": ccqmMIBNotifications,
       "ccqmEnfRuleViolateNotification": ccqmEnfRuleViolateNotification,
       "ccqmMIBConformance": ccqmMIBConformance,
       "ccqmMIBCompliances": ccqmMIBCompliances,
       "ccqmCompliance": ccqmCompliance,
       "ccqmComplianceRev1": ccqmComplianceRev1,
       "ccqmMIBGroups": ccqmMIBGroups,
       "ccqmEnfRuleGroup": ccqmEnfRuleGroup,
       "ccqmEnfRuleViolateGroup": ccqmEnfRuleViolateGroup,
       "ccqmEnfRuleViolateNotifGroup": ccqmEnfRuleViolateNotifGroup,
       "ccqmEnfRuleGroupRev1": ccqmEnfRuleGroupRev1,
       "ccqmCmtsRuleIfBwUtilGroup": ccqmCmtsRuleIfBwUtilGroup}
)
