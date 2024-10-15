# SNMP MIB module (SDSL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SDSL-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:12 2024
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

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nncSdslStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncSdslStatisticsObjects_ObjectIdentity = ObjectIdentity
nncSdslStatisticsObjects = _NncSdslStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1)
)
_NncSdslLineStatusTable_Object = MibTable
nncSdslLineStatusTable = _NncSdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 1)
)
if mibBuilder.loadTexts:
    nncSdslLineStatusTable.setStatus("current")
_NncSdslLineStatusEntry_Object = MibTableRow
nncSdslLineStatusEntry = _NncSdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 1, 1)
)
nncSdslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslLineStatusEntry.setStatus("current")


class _NncSdslLineStatus_Type(Integer32):
    """Custom type nncSdslLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 34),
    )


_NncSdslLineStatus_Type.__name__ = "Integer32"
_NncSdslLineStatus_Object = MibTableColumn
nncSdslLineStatus = _NncSdslLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 1, 1, 1),
    _NncSdslLineStatus_Type()
)
nncSdslLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslLineStatus.setStatus("current")
_NncSdslNearEndRawTable_Object = MibTable
nncSdslNearEndRawTable = _NncSdslNearEndRawTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2)
)
if mibBuilder.loadTexts:
    nncSdslNearEndRawTable.setStatus("current")
_NncSdslNearEndRawEntry_Object = MibTableRow
nncSdslNearEndRawEntry = _NncSdslNearEndRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1)
)
nncSdslNearEndRawEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslNearEndRawEntry.setStatus("current")
_NncSdslNearEndRawLOS_Type = Counter32
_NncSdslNearEndRawLOS_Object = MibTableColumn
nncSdslNearEndRawLOS = _NncSdslNearEndRawLOS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1, 1),
    _NncSdslNearEndRawLOS_Type()
)
nncSdslNearEndRawLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndRawLOS.setStatus("current")
_NncSdslNearEndRawLowNM_Type = Counter32
_NncSdslNearEndRawLowNM_Object = MibTableColumn
nncSdslNearEndRawLowNM = _NncSdslNearEndRawLowNM_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1, 2),
    _NncSdslNearEndRawLowNM_Type()
)
nncSdslNearEndRawLowNM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndRawLowNM.setStatus("current")
_NncSdslNearEndRawLPR_Type = Counter32
_NncSdslNearEndRawLPR_Object = MibTableColumn
nncSdslNearEndRawLPR = _NncSdslNearEndRawLPR_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1, 3),
    _NncSdslNearEndRawLPR_Type()
)
nncSdslNearEndRawLPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndRawLPR.setStatus("current")
_NncSdslNearEndRawLOCD_Type = Counter32
_NncSdslNearEndRawLOCD_Object = MibTableColumn
nncSdslNearEndRawLOCD = _NncSdslNearEndRawLOCD_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1, 4),
    _NncSdslNearEndRawLOCD_Type()
)
nncSdslNearEndRawLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndRawLOCD.setStatus("current")
_NncSdslNearEndRawCRCError_Type = Counter32
_NncSdslNearEndRawCRCError_Object = MibTableColumn
nncSdslNearEndRawCRCError = _NncSdslNearEndRawCRCError_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 2, 1, 5),
    _NncSdslNearEndRawCRCError_Type()
)
nncSdslNearEndRawCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndRawCRCError.setStatus("current")
_NncSdslNearEndCurr15MinTable_Object = MibTable
nncSdslNearEndCurr15MinTable = _NncSdslNearEndCurr15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3)
)
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinTable.setStatus("current")
_NncSdslNearEndCurr15MinEntry_Object = MibTableRow
nncSdslNearEndCurr15MinEntry = _NncSdslNearEndCurr15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1)
)
nncSdslNearEndCurr15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinEntry.setStatus("current")


class _NncSdslNearEndCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type nncSdslNearEndCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_NncSdslNearEndCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_NncSdslNearEndCurr15MinTimeElapsed_Object = MibTableColumn
nncSdslNearEndCurr15MinTimeElapsed = _NncSdslNearEndCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 1),
    _NncSdslNearEndCurr15MinTimeElapsed_Type()
)
nncSdslNearEndCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinTimeElapsed.setUnits("seconds")
_NncSdslNearEndCurr15MinLOSS_Type = Gauge32
_NncSdslNearEndCurr15MinLOSS_Object = MibTableColumn
nncSdslNearEndCurr15MinLOSS = _NncSdslNearEndCurr15MinLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 2),
    _NncSdslNearEndCurr15MinLOSS_Type()
)
nncSdslNearEndCurr15MinLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinLOSS.setStatus("current")
_NncSdslNearEndCurr15MinLOSWS_Type = Gauge32
_NncSdslNearEndCurr15MinLOSWS_Object = MibTableColumn
nncSdslNearEndCurr15MinLOSWS = _NncSdslNearEndCurr15MinLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 3),
    _NncSdslNearEndCurr15MinLOSWS_Type()
)
nncSdslNearEndCurr15MinLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinLOSWS.setStatus("current")
_NncSdslNearEndCurr15MinLowNMS_Type = Gauge32
_NncSdslNearEndCurr15MinLowNMS_Object = MibTableColumn
nncSdslNearEndCurr15MinLowNMS = _NncSdslNearEndCurr15MinLowNMS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 4),
    _NncSdslNearEndCurr15MinLowNMS_Type()
)
nncSdslNearEndCurr15MinLowNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinLowNMS.setStatus("current")
_NncSdslNearEndCurr15MinLPRS_Type = Gauge32
_NncSdslNearEndCurr15MinLPRS_Object = MibTableColumn
nncSdslNearEndCurr15MinLPRS = _NncSdslNearEndCurr15MinLPRS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 5),
    _NncSdslNearEndCurr15MinLPRS_Type()
)
nncSdslNearEndCurr15MinLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinLPRS.setStatus("current")
_NncSdslNearEndCurr15MinErrS_Type = Gauge32
_NncSdslNearEndCurr15MinErrS_Object = MibTableColumn
nncSdslNearEndCurr15MinErrS = _NncSdslNearEndCurr15MinErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 3, 1, 6),
    _NncSdslNearEndCurr15MinErrS_Type()
)
nncSdslNearEndCurr15MinErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr15MinErrS.setStatus("current")
_NncSdslNearEndCurr1DayTable_Object = MibTable
nncSdslNearEndCurr1DayTable = _NncSdslNearEndCurr1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4)
)
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayTable.setStatus("current")
_NncSdslNearEndCurr1DayEntry_Object = MibTableRow
nncSdslNearEndCurr1DayEntry = _NncSdslNearEndCurr1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1)
)
nncSdslNearEndCurr1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayEntry.setStatus("current")
_NncSdslNearEndCurr1DayTimeElapsed_Type = Gauge32
_NncSdslNearEndCurr1DayTimeElapsed_Object = MibTableColumn
nncSdslNearEndCurr1DayTimeElapsed = _NncSdslNearEndCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 1),
    _NncSdslNearEndCurr1DayTimeElapsed_Type()
)
nncSdslNearEndCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayTimeElapsed.setUnits("seconds")
_NncSdslNearEndCurr1DayLOSS_Type = Gauge32
_NncSdslNearEndCurr1DayLOSS_Object = MibTableColumn
nncSdslNearEndCurr1DayLOSS = _NncSdslNearEndCurr1DayLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 2),
    _NncSdslNearEndCurr1DayLOSS_Type()
)
nncSdslNearEndCurr1DayLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayLOSS.setStatus("current")
_NncSdslNearEndCurr1DayLOSWS_Type = Gauge32
_NncSdslNearEndCurr1DayLOSWS_Object = MibTableColumn
nncSdslNearEndCurr1DayLOSWS = _NncSdslNearEndCurr1DayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 3),
    _NncSdslNearEndCurr1DayLOSWS_Type()
)
nncSdslNearEndCurr1DayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayLOSWS.setStatus("current")
_NncSdslNearEndCurr1DayLowNMS_Type = Gauge32
_NncSdslNearEndCurr1DayLowNMS_Object = MibTableColumn
nncSdslNearEndCurr1DayLowNMS = _NncSdslNearEndCurr1DayLowNMS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 4),
    _NncSdslNearEndCurr1DayLowNMS_Type()
)
nncSdslNearEndCurr1DayLowNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayLowNMS.setStatus("current")
_NncSdslNearEndCurr1DayLPRS_Type = Gauge32
_NncSdslNearEndCurr1DayLPRS_Object = MibTableColumn
nncSdslNearEndCurr1DayLPRS = _NncSdslNearEndCurr1DayLPRS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 5),
    _NncSdslNearEndCurr1DayLPRS_Type()
)
nncSdslNearEndCurr1DayLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayLPRS.setStatus("current")
_NncSdslNearEndCurr1DayErrS_Type = Gauge32
_NncSdslNearEndCurr1DayErrS_Object = MibTableColumn
nncSdslNearEndCurr1DayErrS = _NncSdslNearEndCurr1DayErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 4, 1, 6),
    _NncSdslNearEndCurr1DayErrS_Type()
)
nncSdslNearEndCurr1DayErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndCurr1DayErrS.setStatus("current")
_NncSdslNearEndPrev1DayTable_Object = MibTable
nncSdslNearEndPrev1DayTable = _NncSdslNearEndPrev1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5)
)
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayTable.setStatus("current")
_NncSdslNearEndPrev1DayEntry_Object = MibTableRow
nncSdslNearEndPrev1DayEntry = _NncSdslNearEndPrev1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1)
)
nncSdslNearEndPrev1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayEntry.setStatus("current")
_NncSdslNearEndPrev1DayMoniSecs_Type = Gauge32
_NncSdslNearEndPrev1DayMoniSecs_Object = MibTableColumn
nncSdslNearEndPrev1DayMoniSecs = _NncSdslNearEndPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 1),
    _NncSdslNearEndPrev1DayMoniSecs_Type()
)
nncSdslNearEndPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayMoniSecs.setUnits("seconds")
_NncSdslNearEndPrev1DayLOSS_Type = Gauge32
_NncSdslNearEndPrev1DayLOSS_Object = MibTableColumn
nncSdslNearEndPrev1DayLOSS = _NncSdslNearEndPrev1DayLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 2),
    _NncSdslNearEndPrev1DayLOSS_Type()
)
nncSdslNearEndPrev1DayLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayLOSS.setStatus("current")
_NncSdslNearEndPrev1DayLOSWS_Type = Gauge32
_NncSdslNearEndPrev1DayLOSWS_Object = MibTableColumn
nncSdslNearEndPrev1DayLOSWS = _NncSdslNearEndPrev1DayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 3),
    _NncSdslNearEndPrev1DayLOSWS_Type()
)
nncSdslNearEndPrev1DayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayLOSWS.setStatus("current")
_NncSdslNearEndPrev1DayLowNMS_Type = Gauge32
_NncSdslNearEndPrev1DayLowNMS_Object = MibTableColumn
nncSdslNearEndPrev1DayLowNMS = _NncSdslNearEndPrev1DayLowNMS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 4),
    _NncSdslNearEndPrev1DayLowNMS_Type()
)
nncSdslNearEndPrev1DayLowNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayLowNMS.setStatus("current")
_NncSdslNearEndPrev1DayLPRS_Type = Gauge32
_NncSdslNearEndPrev1DayLPRS_Object = MibTableColumn
nncSdslNearEndPrev1DayLPRS = _NncSdslNearEndPrev1DayLPRS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 5),
    _NncSdslNearEndPrev1DayLPRS_Type()
)
nncSdslNearEndPrev1DayLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayLPRS.setStatus("current")
_NncSdslNearEndPrev1DayErrS_Type = Gauge32
_NncSdslNearEndPrev1DayErrS_Object = MibTableColumn
nncSdslNearEndPrev1DayErrS = _NncSdslNearEndPrev1DayErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 6),
    _NncSdslNearEndPrev1DayErrS_Type()
)
nncSdslNearEndPrev1DayErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayErrS.setStatus("current")
_NncSdslNearEndPrev1DayValidData_Type = TruthValue
_NncSdslNearEndPrev1DayValidData_Object = MibTableColumn
nncSdslNearEndPrev1DayValidData = _NncSdslNearEndPrev1DayValidData_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 5, 1, 7),
    _NncSdslNearEndPrev1DayValidData_Type()
)
nncSdslNearEndPrev1DayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndPrev1DayValidData.setStatus("current")
_NncSdslFarEndAllTable_Object = MibTable
nncSdslFarEndAllTable = _NncSdslFarEndAllTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6)
)
if mibBuilder.loadTexts:
    nncSdslFarEndAllTable.setStatus("current")
_NncSdslFarEndAllEntry_Object = MibTableRow
nncSdslFarEndAllEntry = _NncSdslFarEndAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1)
)
nncSdslFarEndAllEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncSdslFarEndAllEntry.setStatus("current")
_NncSdslFarEndRawLOCD_Type = Counter32
_NncSdslFarEndRawLOCD_Object = MibTableColumn
nncSdslFarEndRawLOCD = _NncSdslFarEndRawLOCD_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 1),
    _NncSdslFarEndRawLOCD_Type()
)
nncSdslFarEndRawLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndRawLOCD.setStatus("current")


class _NncSdslFarEndCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type nncSdslFarEndCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_NncSdslFarEndCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_NncSdslFarEndCurr15MinTimeElapsed_Object = MibTableColumn
nncSdslFarEndCurr15MinTimeElapsed = _NncSdslFarEndCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 2),
    _NncSdslFarEndCurr15MinTimeElapsed_Type()
)
nncSdslFarEndCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr15MinTimeElapsed.setUnits("seconds")
_NncSdslFarEndCurr15MinErrS_Type = Gauge32
_NncSdslFarEndCurr15MinErrS_Object = MibTableColumn
nncSdslFarEndCurr15MinErrS = _NncSdslFarEndCurr15MinErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 3),
    _NncSdslFarEndCurr15MinErrS_Type()
)
nncSdslFarEndCurr15MinErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr15MinErrS.setStatus("current")
_NncSdslFarEndCurr1DayTimeElapsed_Type = Gauge32
_NncSdslFarEndCurr1DayTimeElapsed_Object = MibTableColumn
nncSdslFarEndCurr1DayTimeElapsed = _NncSdslFarEndCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 4),
    _NncSdslFarEndCurr1DayTimeElapsed_Type()
)
nncSdslFarEndCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr1DayTimeElapsed.setUnits("seconds")
_NncSdslFarEndCurr1DayErrS_Type = Gauge32
_NncSdslFarEndCurr1DayErrS_Object = MibTableColumn
nncSdslFarEndCurr1DayErrS = _NncSdslFarEndCurr1DayErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 5),
    _NncSdslFarEndCurr1DayErrS_Type()
)
nncSdslFarEndCurr1DayErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndCurr1DayErrS.setStatus("current")
_NncSdslFarEndPrev1DayMoniSecs_Type = Gauge32
_NncSdslFarEndPrev1DayMoniSecs_Object = MibTableColumn
nncSdslFarEndPrev1DayMoniSecs = _NncSdslFarEndPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 6),
    _NncSdslFarEndPrev1DayMoniSecs_Type()
)
nncSdslFarEndPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    nncSdslFarEndPrev1DayMoniSecs.setUnits("seconds")
_NncSdslFarEndPrev1DayErrS_Type = Gauge32
_NncSdslFarEndPrev1DayErrS_Object = MibTableColumn
nncSdslFarEndPrev1DayErrS = _NncSdslFarEndPrev1DayErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 7),
    _NncSdslFarEndPrev1DayErrS_Type()
)
nncSdslFarEndPrev1DayErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndPrev1DayErrS.setStatus("current")
_NncSdslFarEndPrev1DayValidData_Type = TruthValue
_NncSdslFarEndPrev1DayValidData_Object = MibTableColumn
nncSdslFarEndPrev1DayValidData = _NncSdslFarEndPrev1DayValidData_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 6, 1, 8),
    _NncSdslFarEndPrev1DayValidData_Type()
)
nncSdslFarEndPrev1DayValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndPrev1DayValidData.setStatus("current")
_NncSdslNearEndIntTable_Object = MibTable
nncSdslNearEndIntTable = _NncSdslNearEndIntTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7)
)
if mibBuilder.loadTexts:
    nncSdslNearEndIntTable.setStatus("current")
_NncSdslNearEndIntEntry_Object = MibTableRow
nncSdslNearEndIntEntry = _NncSdslNearEndIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1)
)
nncSdslNearEndIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SDSL-STATS-MIB", "nncSdslNearEndIntNumber"),
)
if mibBuilder.loadTexts:
    nncSdslNearEndIntEntry.setStatus("current")


class _NncSdslNearEndIntNumber_Type(Integer32):
    """Custom type nncSdslNearEndIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncSdslNearEndIntNumber_Type.__name__ = "Integer32"
_NncSdslNearEndIntNumber_Object = MibTableColumn
nncSdslNearEndIntNumber = _NncSdslNearEndIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 1),
    _NncSdslNearEndIntNumber_Type()
)
nncSdslNearEndIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncSdslNearEndIntNumber.setStatus("current")
_NncSdslNearEndIntLOSS_Type = Gauge32
_NncSdslNearEndIntLOSS_Object = MibTableColumn
nncSdslNearEndIntLOSS = _NncSdslNearEndIntLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 2),
    _NncSdslNearEndIntLOSS_Type()
)
nncSdslNearEndIntLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntLOSS.setStatus("current")
_NncSdslNearEndIntLOSWS_Type = Gauge32
_NncSdslNearEndIntLOSWS_Object = MibTableColumn
nncSdslNearEndIntLOSWS = _NncSdslNearEndIntLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 3),
    _NncSdslNearEndIntLOSWS_Type()
)
nncSdslNearEndIntLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntLOSWS.setStatus("current")
_NncSdslNearEndIntLowNMS_Type = Gauge32
_NncSdslNearEndIntLowNMS_Object = MibTableColumn
nncSdslNearEndIntLowNMS = _NncSdslNearEndIntLowNMS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 4),
    _NncSdslNearEndIntLowNMS_Type()
)
nncSdslNearEndIntLowNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntLowNMS.setStatus("current")
_NncSdslNearEndIntLPRS_Type = Gauge32
_NncSdslNearEndIntLPRS_Object = MibTableColumn
nncSdslNearEndIntLPRS = _NncSdslNearEndIntLPRS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 5),
    _NncSdslNearEndIntLPRS_Type()
)
nncSdslNearEndIntLPRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntLPRS.setStatus("current")
_NncSdslNearEndIntErrS_Type = Gauge32
_NncSdslNearEndIntErrS_Object = MibTableColumn
nncSdslNearEndIntErrS = _NncSdslNearEndIntErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 6),
    _NncSdslNearEndIntErrS_Type()
)
nncSdslNearEndIntErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntErrS.setStatus("current")
_NncSdslNearEndIntValidData_Type = TruthValue
_NncSdslNearEndIntValidData_Object = MibTableColumn
nncSdslNearEndIntValidData = _NncSdslNearEndIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 7, 1, 7),
    _NncSdslNearEndIntValidData_Type()
)
nncSdslNearEndIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslNearEndIntValidData.setStatus("current")
_NncSdslFarEndIntTable_Object = MibTable
nncSdslFarEndIntTable = _NncSdslFarEndIntTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 8)
)
if mibBuilder.loadTexts:
    nncSdslFarEndIntTable.setStatus("current")
_NncSdslFarEndIntEntry_Object = MibTableRow
nncSdslFarEndIntEntry = _NncSdslFarEndIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 8, 1)
)
nncSdslFarEndIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SDSL-STATS-MIB", "nncSdslFarEndIntNumber"),
)
if mibBuilder.loadTexts:
    nncSdslFarEndIntEntry.setStatus("current")


class _NncSdslFarEndIntNumber_Type(Integer32):
    """Custom type nncSdslFarEndIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncSdslFarEndIntNumber_Type.__name__ = "Integer32"
_NncSdslFarEndIntNumber_Object = MibTableColumn
nncSdslFarEndIntNumber = _NncSdslFarEndIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 8, 1, 1),
    _NncSdslFarEndIntNumber_Type()
)
nncSdslFarEndIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncSdslFarEndIntNumber.setStatus("current")
_NncSdslFarEndIntErrS_Type = Gauge32
_NncSdslFarEndIntErrS_Object = MibTableColumn
nncSdslFarEndIntErrS = _NncSdslFarEndIntErrS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 8, 1, 2),
    _NncSdslFarEndIntErrS_Type()
)
nncSdslFarEndIntErrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndIntErrS.setStatus("current")
_NncSdslFarEndIntValidData_Type = TruthValue
_NncSdslFarEndIntValidData_Object = MibTableColumn
nncSdslFarEndIntValidData = _NncSdslFarEndIntValidData_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 64, 1, 8, 1, 3),
    _NncSdslFarEndIntValidData_Type()
)
nncSdslFarEndIntValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncSdslFarEndIntValidData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDSL-STATS-MIB",
    **{"nncSdslStatistics": nncSdslStatistics,
       "nncSdslStatisticsObjects": nncSdslStatisticsObjects,
       "nncSdslLineStatusTable": nncSdslLineStatusTable,
       "nncSdslLineStatusEntry": nncSdslLineStatusEntry,
       "nncSdslLineStatus": nncSdslLineStatus,
       "nncSdslNearEndRawTable": nncSdslNearEndRawTable,
       "nncSdslNearEndRawEntry": nncSdslNearEndRawEntry,
       "nncSdslNearEndRawLOS": nncSdslNearEndRawLOS,
       "nncSdslNearEndRawLowNM": nncSdslNearEndRawLowNM,
       "nncSdslNearEndRawLPR": nncSdslNearEndRawLPR,
       "nncSdslNearEndRawLOCD": nncSdslNearEndRawLOCD,
       "nncSdslNearEndRawCRCError": nncSdslNearEndRawCRCError,
       "nncSdslNearEndCurr15MinTable": nncSdslNearEndCurr15MinTable,
       "nncSdslNearEndCurr15MinEntry": nncSdslNearEndCurr15MinEntry,
       "nncSdslNearEndCurr15MinTimeElapsed": nncSdslNearEndCurr15MinTimeElapsed,
       "nncSdslNearEndCurr15MinLOSS": nncSdslNearEndCurr15MinLOSS,
       "nncSdslNearEndCurr15MinLOSWS": nncSdslNearEndCurr15MinLOSWS,
       "nncSdslNearEndCurr15MinLowNMS": nncSdslNearEndCurr15MinLowNMS,
       "nncSdslNearEndCurr15MinLPRS": nncSdslNearEndCurr15MinLPRS,
       "nncSdslNearEndCurr15MinErrS": nncSdslNearEndCurr15MinErrS,
       "nncSdslNearEndCurr1DayTable": nncSdslNearEndCurr1DayTable,
       "nncSdslNearEndCurr1DayEntry": nncSdslNearEndCurr1DayEntry,
       "nncSdslNearEndCurr1DayTimeElapsed": nncSdslNearEndCurr1DayTimeElapsed,
       "nncSdslNearEndCurr1DayLOSS": nncSdslNearEndCurr1DayLOSS,
       "nncSdslNearEndCurr1DayLOSWS": nncSdslNearEndCurr1DayLOSWS,
       "nncSdslNearEndCurr1DayLowNMS": nncSdslNearEndCurr1DayLowNMS,
       "nncSdslNearEndCurr1DayLPRS": nncSdslNearEndCurr1DayLPRS,
       "nncSdslNearEndCurr1DayErrS": nncSdslNearEndCurr1DayErrS,
       "nncSdslNearEndPrev1DayTable": nncSdslNearEndPrev1DayTable,
       "nncSdslNearEndPrev1DayEntry": nncSdslNearEndPrev1DayEntry,
       "nncSdslNearEndPrev1DayMoniSecs": nncSdslNearEndPrev1DayMoniSecs,
       "nncSdslNearEndPrev1DayLOSS": nncSdslNearEndPrev1DayLOSS,
       "nncSdslNearEndPrev1DayLOSWS": nncSdslNearEndPrev1DayLOSWS,
       "nncSdslNearEndPrev1DayLowNMS": nncSdslNearEndPrev1DayLowNMS,
       "nncSdslNearEndPrev1DayLPRS": nncSdslNearEndPrev1DayLPRS,
       "nncSdslNearEndPrev1DayErrS": nncSdslNearEndPrev1DayErrS,
       "nncSdslNearEndPrev1DayValidData": nncSdslNearEndPrev1DayValidData,
       "nncSdslFarEndAllTable": nncSdslFarEndAllTable,
       "nncSdslFarEndAllEntry": nncSdslFarEndAllEntry,
       "nncSdslFarEndRawLOCD": nncSdslFarEndRawLOCD,
       "nncSdslFarEndCurr15MinTimeElapsed": nncSdslFarEndCurr15MinTimeElapsed,
       "nncSdslFarEndCurr15MinErrS": nncSdslFarEndCurr15MinErrS,
       "nncSdslFarEndCurr1DayTimeElapsed": nncSdslFarEndCurr1DayTimeElapsed,
       "nncSdslFarEndCurr1DayErrS": nncSdslFarEndCurr1DayErrS,
       "nncSdslFarEndPrev1DayMoniSecs": nncSdslFarEndPrev1DayMoniSecs,
       "nncSdslFarEndPrev1DayErrS": nncSdslFarEndPrev1DayErrS,
       "nncSdslFarEndPrev1DayValidData": nncSdslFarEndPrev1DayValidData,
       "nncSdslNearEndIntTable": nncSdslNearEndIntTable,
       "nncSdslNearEndIntEntry": nncSdslNearEndIntEntry,
       "nncSdslNearEndIntNumber": nncSdslNearEndIntNumber,
       "nncSdslNearEndIntLOSS": nncSdslNearEndIntLOSS,
       "nncSdslNearEndIntLOSWS": nncSdslNearEndIntLOSWS,
       "nncSdslNearEndIntLowNMS": nncSdslNearEndIntLowNMS,
       "nncSdslNearEndIntLPRS": nncSdslNearEndIntLPRS,
       "nncSdslNearEndIntErrS": nncSdslNearEndIntErrS,
       "nncSdslNearEndIntValidData": nncSdslNearEndIntValidData,
       "nncSdslFarEndIntTable": nncSdslFarEndIntTable,
       "nncSdslFarEndIntEntry": nncSdslFarEndIntEntry,
       "nncSdslFarEndIntNumber": nncSdslFarEndIntNumber,
       "nncSdslFarEndIntErrS": nncSdslFarEndIntErrS,
       "nncSdslFarEndIntValidData": nncSdslFarEndIntValidData}
)
