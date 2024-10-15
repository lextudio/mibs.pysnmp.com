# SNMP MIB module (ChrComPmOpticsOCH-Day-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmOpticsOCH-Day-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:16 2024
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

(chrComIfifIndex,) = mibBuilder.importSymbols(
    "ChrComIfifTable-MIB",
    "chrComIfifIndex")

(TruthValue,) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "TruthValue")

(chrComPmOptics,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmOptics")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChrComPmOpticsOCH_DayTable_Object = MibTable
chrComPmOpticsOCH_DayTable = _ChrComPmOpticsOCH_DayTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15)
)
if mibBuilder.loadTexts:
    chrComPmOpticsOCH_DayTable.setStatus("current")
_ChrComPmOpticsOCH_DayEntry_Object = MibTableRow
chrComPmOpticsOCH_DayEntry = _ChrComPmOpticsOCH_DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1)
)
chrComPmOpticsOCH_DayEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ChrComPmOpticsOCH-Day-MIB", "chrComPmOpticsDayNumber"),
)
if mibBuilder.loadTexts:
    chrComPmOpticsOCH_DayEntry.setStatus("current")


class _ChrComPmOpticsDayNumber_Type(Unsigned32):
    """Custom type chrComPmOpticsDayNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChrComPmOpticsDayNumber_Type.__name__ = "Unsigned32"
_ChrComPmOpticsDayNumber_Object = MibTableColumn
chrComPmOpticsDayNumber = _ChrComPmOpticsDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 1),
    _ChrComPmOpticsDayNumber_Type()
)
chrComPmOpticsDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsDayNumber.setStatus("current")
_ChrComPmOpticsSuspectedIntrvl_Type = TruthValue
_ChrComPmOpticsSuspectedIntrvl_Object = MibTableColumn
chrComPmOpticsSuspectedIntrvl = _ChrComPmOpticsSuspectedIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 2),
    _ChrComPmOpticsSuspectedIntrvl_Type()
)
chrComPmOpticsSuspectedIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSuspectedIntrvl.setStatus("current")


class _ChrComPmOpticsElapsedTime_Type(Unsigned32):
    """Custom type chrComPmOpticsElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmOpticsElapsedTime_Object = MibTableColumn
chrComPmOpticsElapsedTime = _ChrComPmOpticsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 3),
    _ChrComPmOpticsElapsedTime_Type()
)
chrComPmOpticsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsElapsedTime.setStatus("current")


class _ChrComPmOpticsSuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmOpticsSuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsSuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmOpticsSuppressedIntrvls_Object = MibTableColumn
chrComPmOpticsSuppressedIntrvls = _ChrComPmOpticsSuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 4),
    _ChrComPmOpticsSuppressedIntrvls_Type()
)
chrComPmOpticsSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSuppressedIntrvls.setStatus("current")


class _ChrComPmOpticsORS_R_Type(Gauge32):
    """Custom type chrComPmOpticsORS_R based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsORS_R_Type.__name__ = "Gauge32"
_ChrComPmOpticsORS_R_Object = MibScalar
chrComPmOpticsORS_R = _ChrComPmOpticsORS_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 5),
    _ChrComPmOpticsORS_R_Type()
)
chrComPmOpticsORS_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsORS_R.setStatus("current")


class _ChrComPmOpticsSES_R_Type(Gauge32):
    """Custom type chrComPmOpticsSES_R based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsSES_R_Type.__name__ = "Gauge32"
_ChrComPmOpticsSES_R_Object = MibScalar
chrComPmOpticsSES_R = _ChrComPmOpticsSES_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 6),
    _ChrComPmOpticsSES_R_Type()
)
chrComPmOpticsSES_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSES_R.setStatus("current")


class _ChrComPmOpticsUAS_R_Type(Gauge32):
    """Custom type chrComPmOpticsUAS_R based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsUAS_R_Type.__name__ = "Gauge32"
_ChrComPmOpticsUAS_R_Object = MibScalar
chrComPmOpticsUAS_R = _ChrComPmOpticsUAS_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 7),
    _ChrComPmOpticsUAS_R_Type()
)
chrComPmOpticsUAS_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsUAS_R.setStatus("current")


class _ChrComPmOpticsORS_S_Type(Gauge32):
    """Custom type chrComPmOpticsORS_S based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsORS_S_Type.__name__ = "Gauge32"
_ChrComPmOpticsORS_S_Object = MibScalar
chrComPmOpticsORS_S = _ChrComPmOpticsORS_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 8),
    _ChrComPmOpticsORS_S_Type()
)
chrComPmOpticsORS_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsORS_S.setStatus("current")


class _ChrComPmOpticsSES_S_Type(Gauge32):
    """Custom type chrComPmOpticsSES_S based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsSES_S_Type.__name__ = "Gauge32"
_ChrComPmOpticsSES_S_Object = MibScalar
chrComPmOpticsSES_S = _ChrComPmOpticsSES_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 9),
    _ChrComPmOpticsSES_S_Type()
)
chrComPmOpticsSES_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSES_S.setStatus("current")


class _ChrComPmOpticsUAS_S_Type(Gauge32):
    """Custom type chrComPmOpticsUAS_S based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsUAS_S_Type.__name__ = "Gauge32"
_ChrComPmOpticsUAS_S_Object = MibScalar
chrComPmOpticsUAS_S = _ChrComPmOpticsUAS_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 10),
    _ChrComPmOpticsUAS_S_Type()
)
chrComPmOpticsUAS_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsUAS_S.setStatus("current")


class _ChrComPmOpticsMean_R_Type(Integer32):
    """Custom type chrComPmOpticsMean_R based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMean_R_Type.__name__ = "Integer32"
_ChrComPmOpticsMean_R_Object = MibScalar
chrComPmOpticsMean_R = _ChrComPmOpticsMean_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 11),
    _ChrComPmOpticsMean_R_Type()
)
chrComPmOpticsMean_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMean_R.setStatus("current")


class _ChrComPmOpticsMax_R_Type(Integer32):
    """Custom type chrComPmOpticsMax_R based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMax_R_Type.__name__ = "Integer32"
_ChrComPmOpticsMax_R_Object = MibScalar
chrComPmOpticsMax_R = _ChrComPmOpticsMax_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 12),
    _ChrComPmOpticsMax_R_Type()
)
chrComPmOpticsMax_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMax_R.setStatus("current")


class _ChrComPmOpticsMin_R_Type(Integer32):
    """Custom type chrComPmOpticsMin_R based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMin_R_Type.__name__ = "Integer32"
_ChrComPmOpticsMin_R_Object = MibScalar
chrComPmOpticsMin_R = _ChrComPmOpticsMin_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 13),
    _ChrComPmOpticsMin_R_Type()
)
chrComPmOpticsMin_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMin_R.setStatus("current")


class _ChrComPmOpticsSD_R_Type(Integer32):
    """Custom type chrComPmOpticsSD_R based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsSD_R_Type.__name__ = "Integer32"
_ChrComPmOpticsSD_R_Object = MibScalar
chrComPmOpticsSD_R = _ChrComPmOpticsSD_R_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 14),
    _ChrComPmOpticsSD_R_Type()
)
chrComPmOpticsSD_R.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSD_R.setStatus("current")


class _ChrComPmOpticsMean_S_Type(Integer32):
    """Custom type chrComPmOpticsMean_S based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMean_S_Type.__name__ = "Integer32"
_ChrComPmOpticsMean_S_Object = MibScalar
chrComPmOpticsMean_S = _ChrComPmOpticsMean_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 15),
    _ChrComPmOpticsMean_S_Type()
)
chrComPmOpticsMean_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMean_S.setStatus("current")


class _ChrComPmOpticsMax_S_Type(Integer32):
    """Custom type chrComPmOpticsMax_S based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMax_S_Type.__name__ = "Integer32"
_ChrComPmOpticsMax_S_Object = MibScalar
chrComPmOpticsMax_S = _ChrComPmOpticsMax_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 16),
    _ChrComPmOpticsMax_S_Type()
)
chrComPmOpticsMax_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMax_S.setStatus("current")


class _ChrComPmOpticsMin_S_Type(Gauge32):
    """Custom type chrComPmOpticsMin_S based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsMin_S_Type.__name__ = "Gauge32"
_ChrComPmOpticsMin_S_Object = MibScalar
chrComPmOpticsMin_S = _ChrComPmOpticsMin_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 17),
    _ChrComPmOpticsMin_S_Type()
)
chrComPmOpticsMin_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMin_S.setStatus("current")


class _ChrComPmOpticsSD_S_Type(Integer32):
    """Custom type chrComPmOpticsSD_S based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsSD_S_Type.__name__ = "Integer32"
_ChrComPmOpticsSD_S_Object = MibScalar
chrComPmOpticsSD_S = _ChrComPmOpticsSD_S_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 18),
    _ChrComPmOpticsSD_S_Type()
)
chrComPmOpticsSD_S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSD_S.setStatus("current")


class _ChrComPmOpticsThresholdProfIndex_Type(Unsigned32):
    """Custom type chrComPmOpticsThresholdProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsThresholdProfIndex_Type.__name__ = "Unsigned32"
_ChrComPmOpticsThresholdProfIndex_Object = MibTableColumn
chrComPmOpticsThresholdProfIndex = _ChrComPmOpticsThresholdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 19),
    _ChrComPmOpticsThresholdProfIndex_Type()
)
chrComPmOpticsThresholdProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmOpticsThresholdProfIndex.setStatus("current")
_ChrComPmOpticsResetCountersAction_Type = TruthValue
_ChrComPmOpticsResetCountersAction_Object = MibTableColumn
chrComPmOpticsResetCountersAction = _ChrComPmOpticsResetCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 15, 1, 20),
    _ChrComPmOpticsResetCountersAction_Type()
)
chrComPmOpticsResetCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmOpticsResetCountersAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmOpticsOCH-Day-MIB",
    **{"chrComPmOpticsOCH-DayTable": chrComPmOpticsOCH_DayTable,
       "chrComPmOpticsOCH-DayEntry": chrComPmOpticsOCH_DayEntry,
       "chrComPmOpticsDayNumber": chrComPmOpticsDayNumber,
       "chrComPmOpticsSuspectedIntrvl": chrComPmOpticsSuspectedIntrvl,
       "chrComPmOpticsElapsedTime": chrComPmOpticsElapsedTime,
       "chrComPmOpticsSuppressedIntrvls": chrComPmOpticsSuppressedIntrvls,
       "chrComPmOpticsORS-R": chrComPmOpticsORS_R,
       "chrComPmOpticsSES-R": chrComPmOpticsSES_R,
       "chrComPmOpticsUAS-R": chrComPmOpticsUAS_R,
       "chrComPmOpticsORS-S": chrComPmOpticsORS_S,
       "chrComPmOpticsSES-S": chrComPmOpticsSES_S,
       "chrComPmOpticsUAS-S": chrComPmOpticsUAS_S,
       "chrComPmOpticsMean-R": chrComPmOpticsMean_R,
       "chrComPmOpticsMax-R": chrComPmOpticsMax_R,
       "chrComPmOpticsMin-R": chrComPmOpticsMin_R,
       "chrComPmOpticsSD-R": chrComPmOpticsSD_R,
       "chrComPmOpticsMean-S": chrComPmOpticsMean_S,
       "chrComPmOpticsMax-S": chrComPmOpticsMax_S,
       "chrComPmOpticsMin-S": chrComPmOpticsMin_S,
       "chrComPmOpticsSD-S": chrComPmOpticsSD_S,
       "chrComPmOpticsThresholdProfIndex": chrComPmOpticsThresholdProfIndex,
       "chrComPmOpticsResetCountersAction": chrComPmOpticsResetCountersAction}
)
