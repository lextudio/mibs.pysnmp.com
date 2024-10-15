# SNMP MIB module (ADSL-LINE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL-LINE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:56 2024
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

(adslAtucIntervalEntry,
 adslAtucPerfDataEntry,
 adslAturIntervalEntry,
 adslAturPerfDataEntry,
 adslLineAlarmConfProfileEntry,
 adslLineConfProfileEntry,
 adslLineEntry,
 adslMIB) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslAtucIntervalEntry",
    "adslAtucPerfDataEntry",
    "adslAturIntervalEntry",
    "adslAturPerfDataEntry",
    "adslLineAlarmConfProfileEntry",
    "adslLineConfProfileEntry",
    "adslLineEntry",
    "adslMIB")

(AdslPerfCurrDayCount,
 AdslPerfPrevDayCount) = mibBuilder.importSymbols(
    "ADSL-TC-MIB",
    "AdslPerfCurrDayCount",
    "AdslPerfPrevDayCount")

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

adslExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3)
)
adslExtMIB.setRevisions(
        ("2002-12-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdslTransmissionModeType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AdslExtMibObjects_ObjectIdentity = ObjectIdentity
adslExtMibObjects = _AdslExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1)
)
_AdslLineExtTable_Object = MibTable
adslLineExtTable = _AdslLineExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17)
)
if mibBuilder.loadTexts:
    adslLineExtTable.setStatus("current")
_AdslLineExtEntry_Object = MibTableRow
adslLineExtEntry = _AdslLineExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1)
)
if mibBuilder.loadTexts:
    adslLineExtEntry.setStatus("current")
_AdslLineTransAtucCap_Type = AdslTransmissionModeType
_AdslLineTransAtucCap_Object = MibTableColumn
adslLineTransAtucCap = _AdslLineTransAtucCap_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 1),
    _AdslLineTransAtucCap_Type()
)
adslLineTransAtucCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineTransAtucCap.setStatus("current")
_AdslLineTransAtucConfig_Type = AdslTransmissionModeType
_AdslLineTransAtucConfig_Object = MibTableColumn
adslLineTransAtucConfig = _AdslLineTransAtucConfig_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 2),
    _AdslLineTransAtucConfig_Type()
)
adslLineTransAtucConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineTransAtucConfig.setStatus("current")
_AdslLineTransAtucActual_Type = AdslTransmissionModeType
_AdslLineTransAtucActual_Object = MibTableColumn
adslLineTransAtucActual = _AdslLineTransAtucActual_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 3),
    _AdslLineTransAtucActual_Type()
)
adslLineTransAtucActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineTransAtucActual.setStatus("current")


class _AdslLineGlitePowerState_Type(Integer32):
    """Custom type adslLineGlitePowerState based on Integer32"""
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
        *(("l0", 2),
          ("l1", 3),
          ("l3", 4),
          ("none", 1))
    )


_AdslLineGlitePowerState_Type.__name__ = "Integer32"
_AdslLineGlitePowerState_Object = MibTableColumn
adslLineGlitePowerState = _AdslLineGlitePowerState_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 4),
    _AdslLineGlitePowerState_Type()
)
adslLineGlitePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineGlitePowerState.setStatus("current")
_AdslLineConfProfileDualLite_Type = SnmpAdminString
_AdslLineConfProfileDualLite_Object = MibTableColumn
adslLineConfProfileDualLite = _AdslLineConfProfileDualLite_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 5),
    _AdslLineConfProfileDualLite_Type()
)
adslLineConfProfileDualLite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslLineConfProfileDualLite.setStatus("current")
_AdslAtucPerfDataExtTable_Object = MibTable
adslAtucPerfDataExtTable = _AdslAtucPerfDataExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18)
)
if mibBuilder.loadTexts:
    adslAtucPerfDataExtTable.setStatus("current")
_AdslAtucPerfDataExtEntry_Object = MibTableRow
adslAtucPerfDataExtEntry = _AdslAtucPerfDataExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1)
)
if mibBuilder.loadTexts:
    adslAtucPerfDataExtEntry.setStatus("current")
_AdslAtucPerfStatFastR_Type = Counter32
_AdslAtucPerfStatFastR_Object = MibTableColumn
adslAtucPerfStatFastR = _AdslAtucPerfStatFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 1),
    _AdslAtucPerfStatFastR_Type()
)
adslAtucPerfStatFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfStatFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfStatFastR.setUnits("line retrains")
_AdslAtucPerfStatFailedFastR_Type = Counter32
_AdslAtucPerfStatFailedFastR_Object = MibTableColumn
adslAtucPerfStatFailedFastR = _AdslAtucPerfStatFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 2),
    _AdslAtucPerfStatFailedFastR_Type()
)
adslAtucPerfStatFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfStatFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfStatFailedFastR.setUnits("line retrains")
_AdslAtucPerfStatSesL_Type = Counter32
_AdslAtucPerfStatSesL_Object = MibTableColumn
adslAtucPerfStatSesL = _AdslAtucPerfStatSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 3),
    _AdslAtucPerfStatSesL_Type()
)
adslAtucPerfStatSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfStatSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfStatSesL.setUnits("seconds")
_AdslAtucPerfStatUasL_Type = Counter32
_AdslAtucPerfStatUasL_Object = MibTableColumn
adslAtucPerfStatUasL = _AdslAtucPerfStatUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 4),
    _AdslAtucPerfStatUasL_Type()
)
adslAtucPerfStatUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfStatUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfStatUasL.setUnits("seconds")
_AdslAtucPerfCurr15MinFastR_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinFastR_Object = MibTableColumn
adslAtucPerfCurr15MinFastR = _AdslAtucPerfCurr15MinFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 5),
    _AdslAtucPerfCurr15MinFastR_Type()
)
adslAtucPerfCurr15MinFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinFastR.setUnits("seconds")
_AdslAtucPerfCurr15MinFailedFastR_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinFailedFastR_Object = MibTableColumn
adslAtucPerfCurr15MinFailedFastR = _AdslAtucPerfCurr15MinFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 6),
    _AdslAtucPerfCurr15MinFailedFastR_Type()
)
adslAtucPerfCurr15MinFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinFailedFastR.setUnits("seconds")
_AdslAtucPerfCurr15MinSesL_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinSesL_Object = MibTableColumn
adslAtucPerfCurr15MinSesL = _AdslAtucPerfCurr15MinSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 7),
    _AdslAtucPerfCurr15MinSesL_Type()
)
adslAtucPerfCurr15MinSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinSesL.setUnits("seconds")
_AdslAtucPerfCurr15MinUasL_Type = PerfCurrentCount
_AdslAtucPerfCurr15MinUasL_Object = MibTableColumn
adslAtucPerfCurr15MinUasL = _AdslAtucPerfCurr15MinUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 8),
    _AdslAtucPerfCurr15MinUasL_Type()
)
adslAtucPerfCurr15MinUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr15MinUasL.setUnits("seconds")
_AdslAtucPerfCurr1DayFastR_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayFastR_Object = MibTableColumn
adslAtucPerfCurr1DayFastR = _AdslAtucPerfCurr1DayFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 9),
    _AdslAtucPerfCurr1DayFastR_Type()
)
adslAtucPerfCurr1DayFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayFastR.setUnits("seconds")
_AdslAtucPerfCurr1DayFailedFastR_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayFailedFastR_Object = MibTableColumn
adslAtucPerfCurr1DayFailedFastR = _AdslAtucPerfCurr1DayFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 10),
    _AdslAtucPerfCurr1DayFailedFastR_Type()
)
adslAtucPerfCurr1DayFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayFailedFastR.setUnits("seconds")
_AdslAtucPerfCurr1DaySesL_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DaySesL_Object = MibTableColumn
adslAtucPerfCurr1DaySesL = _AdslAtucPerfCurr1DaySesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 11),
    _AdslAtucPerfCurr1DaySesL_Type()
)
adslAtucPerfCurr1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DaySesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DaySesL.setUnits("seconds")
_AdslAtucPerfCurr1DayUasL_Type = AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayUasL_Object = MibTableColumn
adslAtucPerfCurr1DayUasL = _AdslAtucPerfCurr1DayUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 12),
    _AdslAtucPerfCurr1DayUasL_Type()
)
adslAtucPerfCurr1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfCurr1DayUasL.setUnits("seconds")
_AdslAtucPerfPrev1DayFastR_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayFastR_Object = MibTableColumn
adslAtucPerfPrev1DayFastR = _AdslAtucPerfPrev1DayFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 13),
    _AdslAtucPerfPrev1DayFastR_Type()
)
adslAtucPerfPrev1DayFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayFastR.setUnits("seconds")
_AdslAtucPerfPrev1DayFailedFastR_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayFailedFastR_Object = MibTableColumn
adslAtucPerfPrev1DayFailedFastR = _AdslAtucPerfPrev1DayFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 14),
    _AdslAtucPerfPrev1DayFailedFastR_Type()
)
adslAtucPerfPrev1DayFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayFailedFastR.setUnits("seconds")
_AdslAtucPerfPrev1DaySesL_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DaySesL_Object = MibTableColumn
adslAtucPerfPrev1DaySesL = _AdslAtucPerfPrev1DaySesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 15),
    _AdslAtucPerfPrev1DaySesL_Type()
)
adslAtucPerfPrev1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DaySesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DaySesL.setUnits("seconds")
_AdslAtucPerfPrev1DayUasL_Type = AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayUasL_Object = MibTableColumn
adslAtucPerfPrev1DayUasL = _AdslAtucPerfPrev1DayUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 16),
    _AdslAtucPerfPrev1DayUasL_Type()
)
adslAtucPerfPrev1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucPerfPrev1DayUasL.setUnits("seconds")
_AdslAtucIntervalExtTable_Object = MibTable
adslAtucIntervalExtTable = _AdslAtucIntervalExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19)
)
if mibBuilder.loadTexts:
    adslAtucIntervalExtTable.setStatus("current")
_AdslAtucIntervalExtEntry_Object = MibTableRow
adslAtucIntervalExtEntry = _AdslAtucIntervalExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1)
)
if mibBuilder.loadTexts:
    adslAtucIntervalExtEntry.setStatus("current")
_AdslAtucIntervalFastR_Type = PerfIntervalCount
_AdslAtucIntervalFastR_Object = MibTableColumn
adslAtucIntervalFastR = _AdslAtucIntervalFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 1),
    _AdslAtucIntervalFastR_Type()
)
adslAtucIntervalFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalFastR.setUnits("seconds")
_AdslAtucIntervalFailedFastR_Type = PerfIntervalCount
_AdslAtucIntervalFailedFastR_Object = MibTableColumn
adslAtucIntervalFailedFastR = _AdslAtucIntervalFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 2),
    _AdslAtucIntervalFailedFastR_Type()
)
adslAtucIntervalFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalFailedFastR.setUnits("seconds")
_AdslAtucIntervalSesL_Type = PerfIntervalCount
_AdslAtucIntervalSesL_Object = MibTableColumn
adslAtucIntervalSesL = _AdslAtucIntervalSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 3),
    _AdslAtucIntervalSesL_Type()
)
adslAtucIntervalSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalSesL.setUnits("seconds")
_AdslAtucIntervalUasL_Type = PerfIntervalCount
_AdslAtucIntervalUasL_Object = MibTableColumn
adslAtucIntervalUasL = _AdslAtucIntervalUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 4),
    _AdslAtucIntervalUasL_Type()
)
adslAtucIntervalUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAtucIntervalUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucIntervalUasL.setUnits("seconds")
_AdslAturPerfDataExtTable_Object = MibTable
adslAturPerfDataExtTable = _AdslAturPerfDataExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20)
)
if mibBuilder.loadTexts:
    adslAturPerfDataExtTable.setStatus("current")
_AdslAturPerfDataExtEntry_Object = MibTableRow
adslAturPerfDataExtEntry = _AdslAturPerfDataExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1)
)
if mibBuilder.loadTexts:
    adslAturPerfDataExtEntry.setStatus("current")
_AdslAturPerfStatSesL_Type = Counter32
_AdslAturPerfStatSesL_Object = MibTableColumn
adslAturPerfStatSesL = _AdslAturPerfStatSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 1),
    _AdslAturPerfStatSesL_Type()
)
adslAturPerfStatSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfStatSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfStatSesL.setUnits("seconds")
_AdslAturPerfStatUasL_Type = Counter32
_AdslAturPerfStatUasL_Object = MibTableColumn
adslAturPerfStatUasL = _AdslAturPerfStatUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 2),
    _AdslAturPerfStatUasL_Type()
)
adslAturPerfStatUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfStatUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfStatUasL.setUnits("seconds")
_AdslAturPerfCurr15MinSesL_Type = PerfCurrentCount
_AdslAturPerfCurr15MinSesL_Object = MibTableColumn
adslAturPerfCurr15MinSesL = _AdslAturPerfCurr15MinSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 3),
    _AdslAturPerfCurr15MinSesL_Type()
)
adslAturPerfCurr15MinSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinSesL.setUnits("seconds")
_AdslAturPerfCurr15MinUasL_Type = PerfCurrentCount
_AdslAturPerfCurr15MinUasL_Object = MibTableColumn
adslAturPerfCurr15MinUasL = _AdslAturPerfCurr15MinUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 4),
    _AdslAturPerfCurr15MinUasL_Type()
)
adslAturPerfCurr15MinUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr15MinUasL.setUnits("seconds")
_AdslAturPerfCurr1DaySesL_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DaySesL_Object = MibTableColumn
adslAturPerfCurr1DaySesL = _AdslAturPerfCurr1DaySesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 5),
    _AdslAturPerfCurr1DaySesL_Type()
)
adslAturPerfCurr1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DaySesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DaySesL.setUnits("seconds")
_AdslAturPerfCurr1DayUasL_Type = AdslPerfCurrDayCount
_AdslAturPerfCurr1DayUasL_Object = MibTableColumn
adslAturPerfCurr1DayUasL = _AdslAturPerfCurr1DayUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 6),
    _AdslAturPerfCurr1DayUasL_Type()
)
adslAturPerfCurr1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfCurr1DayUasL.setUnits("seconds")
_AdslAturPerfPrev1DaySesL_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DaySesL_Object = MibTableColumn
adslAturPerfPrev1DaySesL = _AdslAturPerfPrev1DaySesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 7),
    _AdslAturPerfPrev1DaySesL_Type()
)
adslAturPerfPrev1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DaySesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DaySesL.setUnits("seconds")
_AdslAturPerfPrev1DayUasL_Type = AdslPerfPrevDayCount
_AdslAturPerfPrev1DayUasL_Object = MibTableColumn
adslAturPerfPrev1DayUasL = _AdslAturPerfPrev1DayUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 8),
    _AdslAturPerfPrev1DayUasL_Type()
)
adslAturPerfPrev1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturPerfPrev1DayUasL.setUnits("seconds")
_AdslAturIntervalExtTable_Object = MibTable
adslAturIntervalExtTable = _AdslAturIntervalExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21)
)
if mibBuilder.loadTexts:
    adslAturIntervalExtTable.setStatus("current")
_AdslAturIntervalExtEntry_Object = MibTableRow
adslAturIntervalExtEntry = _AdslAturIntervalExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1)
)
if mibBuilder.loadTexts:
    adslAturIntervalExtEntry.setStatus("current")
_AdslAturIntervalSesL_Type = PerfIntervalCount
_AdslAturIntervalSesL_Object = MibTableColumn
adslAturIntervalSesL = _AdslAturIntervalSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 1),
    _AdslAturIntervalSesL_Type()
)
adslAturIntervalSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalSesL.setUnits("seconds")
_AdslAturIntervalUasL_Type = PerfIntervalCount
_AdslAturIntervalUasL_Object = MibTableColumn
adslAturIntervalUasL = _AdslAturIntervalUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 2),
    _AdslAturIntervalUasL_Type()
)
adslAturIntervalUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslAturIntervalUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturIntervalUasL.setUnits("seconds")
_AdslConfProfileExtTable_Object = MibTable
adslConfProfileExtTable = _AdslConfProfileExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22)
)
if mibBuilder.loadTexts:
    adslConfProfileExtTable.setStatus("current")
_AdslConfProfileExtEntry_Object = MibTableRow
adslConfProfileExtEntry = _AdslConfProfileExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1)
)
if mibBuilder.loadTexts:
    adslConfProfileExtEntry.setStatus("current")


class _AdslConfProfileLineType_Type(Integer32):
    """Custom type adslConfProfileLineType based on Integer32"""
    defaultValue = 2

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
        *(("fastAndInterleaved", 5),
          ("fastOnly", 2),
          ("fastOrInterleaved", 4),
          ("interleavedOnly", 3),
          ("noChannel", 1))
    )


_AdslConfProfileLineType_Type.__name__ = "Integer32"
_AdslConfProfileLineType_Object = MibTableColumn
adslConfProfileLineType = _AdslConfProfileLineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1, 1),
    _AdslConfProfileLineType_Type()
)
adslConfProfileLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslConfProfileLineType.setStatus("current")
_AdslAlarmConfProfileExtTable_Object = MibTable
adslAlarmConfProfileExtTable = _AdslAlarmConfProfileExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23)
)
if mibBuilder.loadTexts:
    adslAlarmConfProfileExtTable.setStatus("current")
_AdslAlarmConfProfileExtEntry_Object = MibTableRow
adslAlarmConfProfileExtEntry = _AdslAlarmConfProfileExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1)
)
if mibBuilder.loadTexts:
    adslAlarmConfProfileExtEntry.setStatus("current")


class _AdslAtucThreshold15MinFailedFastR_Type(Integer32):
    """Custom type adslAtucThreshold15MinFailedFastR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThreshold15MinFailedFastR_Type.__name__ = "Integer32"
_AdslAtucThreshold15MinFailedFastR_Object = MibTableColumn
adslAtucThreshold15MinFailedFastR = _AdslAtucThreshold15MinFailedFastR_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 1),
    _AdslAtucThreshold15MinFailedFastR_Type()
)
adslAtucThreshold15MinFailedFastR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinFailedFastR.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinFailedFastR.setUnits("seconds")


class _AdslAtucThreshold15MinSesL_Type(Integer32):
    """Custom type adslAtucThreshold15MinSesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThreshold15MinSesL_Type.__name__ = "Integer32"
_AdslAtucThreshold15MinSesL_Object = MibTableColumn
adslAtucThreshold15MinSesL = _AdslAtucThreshold15MinSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 2),
    _AdslAtucThreshold15MinSesL_Type()
)
adslAtucThreshold15MinSesL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinSesL.setUnits("seconds")


class _AdslAtucThreshold15MinUasL_Type(Integer32):
    """Custom type adslAtucThreshold15MinUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAtucThreshold15MinUasL_Type.__name__ = "Integer32"
_AdslAtucThreshold15MinUasL_Object = MibTableColumn
adslAtucThreshold15MinUasL = _AdslAtucThreshold15MinUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 3),
    _AdslAtucThreshold15MinUasL_Type()
)
adslAtucThreshold15MinUasL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAtucThreshold15MinUasL.setUnits("seconds")


class _AdslAturThreshold15MinSesL_Type(Integer32):
    """Custom type adslAturThreshold15MinSesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThreshold15MinSesL_Type.__name__ = "Integer32"
_AdslAturThreshold15MinSesL_Object = MibTableColumn
adslAturThreshold15MinSesL = _AdslAturThreshold15MinSesL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 4),
    _AdslAturThreshold15MinSesL_Type()
)
adslAturThreshold15MinSesL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshold15MinSesL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshold15MinSesL.setUnits("seconds")


class _AdslAturThreshold15MinUasL_Type(Integer32):
    """Custom type adslAturThreshold15MinUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdslAturThreshold15MinUasL_Type.__name__ = "Integer32"
_AdslAturThreshold15MinUasL_Object = MibTableColumn
adslAturThreshold15MinUasL = _AdslAturThreshold15MinUasL_Object(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 5),
    _AdslAturThreshold15MinUasL_Type()
)
adslAturThreshold15MinUasL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adslAturThreshold15MinUasL.setStatus("current")
if mibBuilder.loadTexts:
    adslAturThreshold15MinUasL.setUnits("seconds")
_AdslExtTraps_ObjectIdentity = ObjectIdentity
adslExtTraps = _AdslExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24)
)
_AdslExtAtucTraps_ObjectIdentity = ObjectIdentity
adslExtAtucTraps = _AdslExtAtucTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1)
)
_AdslExtAtucTrapsPrefix_ObjectIdentity = ObjectIdentity
adslExtAtucTrapsPrefix = _AdslExtAtucTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0)
)
_AdslExtAturTraps_ObjectIdentity = ObjectIdentity
adslExtAturTraps = _AdslExtAturTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2)
)
_AdslExtAturTrapsPrefix_ObjectIdentity = ObjectIdentity
adslExtAturTrapsPrefix = _AdslExtAturTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0)
)
_AdslExtConformance_ObjectIdentity = ObjectIdentity
adslExtConformance = _AdslExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2)
)
_AdslExtGroups_ObjectIdentity = ObjectIdentity
adslExtGroups = _AdslExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1)
)
_AdslExtCompliances_ObjectIdentity = ObjectIdentity
adslExtCompliances = _AdslExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2)
)
adslLineEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslLineExtEntry")
)
adslLineExtEntry.setIndexNames(*adslLineEntry.getIndexNames())
adslAtucPerfDataEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslAtucPerfDataExtEntry")
)
adslAtucPerfDataExtEntry.setIndexNames(*adslAtucPerfDataEntry.getIndexNames())
adslAtucIntervalEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslAtucIntervalExtEntry")
)
adslAtucIntervalExtEntry.setIndexNames(*adslAtucIntervalEntry.getIndexNames())
adslAturPerfDataEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslAturPerfDataExtEntry")
)
adslAturPerfDataExtEntry.setIndexNames(*adslAturPerfDataEntry.getIndexNames())
adslAturIntervalEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslAturIntervalExtEntry")
)
adslAturIntervalExtEntry.setIndexNames(*adslAturIntervalEntry.getIndexNames())
adslLineConfProfileEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslConfProfileExtEntry")
)
adslConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions(
    ("ADSL-LINE-EXT-MIB",
     "adslAlarmConfProfileExtEntry")
)
adslAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())

# Managed Objects groups

adslExtLineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 1)
)
adslExtLineGroup.setObjects(
      *(("ADSL-LINE-EXT-MIB", "adslLineConfProfileDualLite"),
        ("ADSL-LINE-EXT-MIB", "adslLineTransAtucCap"),
        ("ADSL-LINE-EXT-MIB", "adslLineTransAtucConfig"),
        ("ADSL-LINE-EXT-MIB", "adslLineTransAtucActual"),
        ("ADSL-LINE-EXT-MIB", "adslLineGlitePowerState"))
)
if mibBuilder.loadTexts:
    adslExtLineGroup.setStatus("current")

adslExtAtucPhysPerfCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 2)
)
adslExtAtucPhysPerfCounterGroup.setObjects(
      *(("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DaySesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DaySesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucIntervalSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucIntervalUasL"))
)
if mibBuilder.loadTexts:
    adslExtAtucPhysPerfCounterGroup.setStatus("current")

adslExtAturPhysPerfCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 3)
)
adslExtAturPhysPerfCounterGroup.setObjects(
      *(("ADSL-LINE-EXT-MIB", "adslAturPerfStatSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfStatUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DaySesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DayUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DaySesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DayUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAturIntervalSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturIntervalUasL"))
)
if mibBuilder.loadTexts:
    adslExtAturPhysPerfCounterGroup.setStatus("current")

adslExtLineConfProfileControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 4)
)
adslExtLineConfProfileControlGroup.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslConfProfileLineType")
)
if mibBuilder.loadTexts:
    adslExtLineConfProfileControlGroup.setStatus("current")

adslExtLineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 5)
)
adslExtLineAlarmConfProfileGroup.setObjects(
      *(("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinFailedFastR"),
        ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinUasL"),
        ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinSesL"),
        ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinUasL"))
)
if mibBuilder.loadTexts:
    adslExtLineAlarmConfProfileGroup.setStatus("current")


# Notification objects

adslAtucFailedFastRThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 1)
)
adslAtucFailedFastRThreshTrap.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR")
)
if mibBuilder.loadTexts:
    adslAtucFailedFastRThreshTrap.setStatus(
        "current"
    )

adslAtucSesLThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 2)
)
adslAtucSesLThreshTrap.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL")
)
if mibBuilder.loadTexts:
    adslAtucSesLThreshTrap.setStatus(
        "current"
    )

adslAtucUasLThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 3)
)
adslAtucUasLThreshTrap.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL")
)
if mibBuilder.loadTexts:
    adslAtucUasLThreshTrap.setStatus(
        "current"
    )

adslAturSesLThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 1)
)
adslAturSesLThreshTrap.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL")
)
if mibBuilder.loadTexts:
    adslAturSesLThreshTrap.setStatus(
        "current"
    )

adslAturUasLThreshTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 2)
)
adslAturUasLThreshTrap.setObjects(
    ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL")
)
if mibBuilder.loadTexts:
    adslAturUasLThreshTrap.setStatus(
        "current"
    )


# Notifications groups

adslExtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 6)
)
adslExtNotificationsGroup.setObjects(
      *(("ADSL-LINE-EXT-MIB", "adslAtucFailedFastRThreshTrap"),
        ("ADSL-LINE-EXT-MIB", "adslAtucSesLThreshTrap"),
        ("ADSL-LINE-EXT-MIB", "adslAtucUasLThreshTrap"),
        ("ADSL-LINE-EXT-MIB", "adslAturSesLThreshTrap"),
        ("ADSL-LINE-EXT-MIB", "adslAturUasLThreshTrap"))
)
if mibBuilder.loadTexts:
    adslExtNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adslExtLineMibAtucCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adslExtLineMibAtucCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL-LINE-EXT-MIB",
    **{"AdslTransmissionModeType": AdslTransmissionModeType,
       "adslExtMIB": adslExtMIB,
       "adslExtMibObjects": adslExtMibObjects,
       "adslLineExtTable": adslLineExtTable,
       "adslLineExtEntry": adslLineExtEntry,
       "adslLineTransAtucCap": adslLineTransAtucCap,
       "adslLineTransAtucConfig": adslLineTransAtucConfig,
       "adslLineTransAtucActual": adslLineTransAtucActual,
       "adslLineGlitePowerState": adslLineGlitePowerState,
       "adslLineConfProfileDualLite": adslLineConfProfileDualLite,
       "adslAtucPerfDataExtTable": adslAtucPerfDataExtTable,
       "adslAtucPerfDataExtEntry": adslAtucPerfDataExtEntry,
       "adslAtucPerfStatFastR": adslAtucPerfStatFastR,
       "adslAtucPerfStatFailedFastR": adslAtucPerfStatFailedFastR,
       "adslAtucPerfStatSesL": adslAtucPerfStatSesL,
       "adslAtucPerfStatUasL": adslAtucPerfStatUasL,
       "adslAtucPerfCurr15MinFastR": adslAtucPerfCurr15MinFastR,
       "adslAtucPerfCurr15MinFailedFastR": adslAtucPerfCurr15MinFailedFastR,
       "adslAtucPerfCurr15MinSesL": adslAtucPerfCurr15MinSesL,
       "adslAtucPerfCurr15MinUasL": adslAtucPerfCurr15MinUasL,
       "adslAtucPerfCurr1DayFastR": adslAtucPerfCurr1DayFastR,
       "adslAtucPerfCurr1DayFailedFastR": adslAtucPerfCurr1DayFailedFastR,
       "adslAtucPerfCurr1DaySesL": adslAtucPerfCurr1DaySesL,
       "adslAtucPerfCurr1DayUasL": adslAtucPerfCurr1DayUasL,
       "adslAtucPerfPrev1DayFastR": adslAtucPerfPrev1DayFastR,
       "adslAtucPerfPrev1DayFailedFastR": adslAtucPerfPrev1DayFailedFastR,
       "adslAtucPerfPrev1DaySesL": adslAtucPerfPrev1DaySesL,
       "adslAtucPerfPrev1DayUasL": adslAtucPerfPrev1DayUasL,
       "adslAtucIntervalExtTable": adslAtucIntervalExtTable,
       "adslAtucIntervalExtEntry": adslAtucIntervalExtEntry,
       "adslAtucIntervalFastR": adslAtucIntervalFastR,
       "adslAtucIntervalFailedFastR": adslAtucIntervalFailedFastR,
       "adslAtucIntervalSesL": adslAtucIntervalSesL,
       "adslAtucIntervalUasL": adslAtucIntervalUasL,
       "adslAturPerfDataExtTable": adslAturPerfDataExtTable,
       "adslAturPerfDataExtEntry": adslAturPerfDataExtEntry,
       "adslAturPerfStatSesL": adslAturPerfStatSesL,
       "adslAturPerfStatUasL": adslAturPerfStatUasL,
       "adslAturPerfCurr15MinSesL": adslAturPerfCurr15MinSesL,
       "adslAturPerfCurr15MinUasL": adslAturPerfCurr15MinUasL,
       "adslAturPerfCurr1DaySesL": adslAturPerfCurr1DaySesL,
       "adslAturPerfCurr1DayUasL": adslAturPerfCurr1DayUasL,
       "adslAturPerfPrev1DaySesL": adslAturPerfPrev1DaySesL,
       "adslAturPerfPrev1DayUasL": adslAturPerfPrev1DayUasL,
       "adslAturIntervalExtTable": adslAturIntervalExtTable,
       "adslAturIntervalExtEntry": adslAturIntervalExtEntry,
       "adslAturIntervalSesL": adslAturIntervalSesL,
       "adslAturIntervalUasL": adslAturIntervalUasL,
       "adslConfProfileExtTable": adslConfProfileExtTable,
       "adslConfProfileExtEntry": adslConfProfileExtEntry,
       "adslConfProfileLineType": adslConfProfileLineType,
       "adslAlarmConfProfileExtTable": adslAlarmConfProfileExtTable,
       "adslAlarmConfProfileExtEntry": adslAlarmConfProfileExtEntry,
       "adslAtucThreshold15MinFailedFastR": adslAtucThreshold15MinFailedFastR,
       "adslAtucThreshold15MinSesL": adslAtucThreshold15MinSesL,
       "adslAtucThreshold15MinUasL": adslAtucThreshold15MinUasL,
       "adslAturThreshold15MinSesL": adslAturThreshold15MinSesL,
       "adslAturThreshold15MinUasL": adslAturThreshold15MinUasL,
       "adslExtTraps": adslExtTraps,
       "adslExtAtucTraps": adslExtAtucTraps,
       "adslExtAtucTrapsPrefix": adslExtAtucTrapsPrefix,
       "adslAtucFailedFastRThreshTrap": adslAtucFailedFastRThreshTrap,
       "adslAtucSesLThreshTrap": adslAtucSesLThreshTrap,
       "adslAtucUasLThreshTrap": adslAtucUasLThreshTrap,
       "adslExtAturTraps": adslExtAturTraps,
       "adslExtAturTrapsPrefix": adslExtAturTrapsPrefix,
       "adslAturSesLThreshTrap": adslAturSesLThreshTrap,
       "adslAturUasLThreshTrap": adslAturUasLThreshTrap,
       "adslExtConformance": adslExtConformance,
       "adslExtGroups": adslExtGroups,
       "adslExtLineGroup": adslExtLineGroup,
       "adslExtAtucPhysPerfCounterGroup": adslExtAtucPhysPerfCounterGroup,
       "adslExtAturPhysPerfCounterGroup": adslExtAturPhysPerfCounterGroup,
       "adslExtLineConfProfileControlGroup": adslExtLineConfProfileControlGroup,
       "adslExtLineAlarmConfProfileGroup": adslExtLineAlarmConfProfileGroup,
       "adslExtNotificationsGroup": adslExtNotificationsGroup,
       "adslExtCompliances": adslExtCompliances,
       "adslExtLineMibAtucCompliance": adslExtLineMibAtucCompliance}
)
