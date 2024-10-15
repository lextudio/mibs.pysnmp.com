# SNMP MIB module (ChrComPmSonetSNT-S-Day-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmSonetSNT-S-Day-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:40 2024
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

(chrComPmSonet,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmSonet")

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

_ChrComPmSonetSNT_S_DayTable_Object = MibTable
chrComPmSonetSNT_S_DayTable = _ChrComPmSonetSNT_S_DayTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    chrComPmSonetSNT_S_DayTable.setStatus("current")
_ChrComPmSonetSNT_S_DayEntry_Object = MibTableRow
chrComPmSonetSNT_S_DayEntry = _ChrComPmSonetSNT_S_DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1)
)
chrComPmSonetSNT_S_DayEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ChrComPmSonetSNT-S-Day-MIB", "chrComPmSonetDayNumber"),
)
if mibBuilder.loadTexts:
    chrComPmSonetSNT_S_DayEntry.setStatus("current")


class _ChrComPmSonetDayNumber_Type(Unsigned32):
    """Custom type chrComPmSonetDayNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChrComPmSonetDayNumber_Type.__name__ = "Unsigned32"
_ChrComPmSonetDayNumber_Object = MibTableColumn
chrComPmSonetDayNumber = _ChrComPmSonetDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 1),
    _ChrComPmSonetDayNumber_Type()
)
chrComPmSonetDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetDayNumber.setStatus("current")
_ChrComPmSonetSuspectedInterval_Type = TruthValue
_ChrComPmSonetSuspectedInterval_Object = MibTableColumn
chrComPmSonetSuspectedInterval = _ChrComPmSonetSuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 2),
    _ChrComPmSonetSuspectedInterval_Type()
)
chrComPmSonetSuspectedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetSuspectedInterval.setStatus("current")


class _ChrComPmSonetElapsedTime_Type(Unsigned32):
    """Custom type chrComPmSonetElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmSonetElapsedTime_Object = MibTableColumn
chrComPmSonetElapsedTime = _ChrComPmSonetElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 3),
    _ChrComPmSonetElapsedTime_Type()
)
chrComPmSonetElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetElapsedTime.setStatus("current")


class _ChrComPmSonetSuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmSonetSuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetSuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmSonetSuppressedIntrvls_Object = MibTableColumn
chrComPmSonetSuppressedIntrvls = _ChrComPmSonetSuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 4),
    _ChrComPmSonetSuppressedIntrvls_Type()
)
chrComPmSonetSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetSuppressedIntrvls.setStatus("current")


class _ChrComPmSonetES_Type(Gauge32):
    """Custom type chrComPmSonetES based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetES_Type.__name__ = "Gauge32"
_ChrComPmSonetES_Object = MibTableColumn
chrComPmSonetES = _ChrComPmSonetES_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 5),
    _ChrComPmSonetES_Type()
)
chrComPmSonetES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetES.setStatus("current")


class _ChrComPmSonetSES_Type(Gauge32):
    """Custom type chrComPmSonetSES based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetSES_Type.__name__ = "Gauge32"
_ChrComPmSonetSES_Object = MibTableColumn
chrComPmSonetSES = _ChrComPmSonetSES_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 6),
    _ChrComPmSonetSES_Type()
)
chrComPmSonetSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetSES.setStatus("current")


class _ChrComPmSonetSEFS_Type(Gauge32):
    """Custom type chrComPmSonetSEFS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetSEFS_Type.__name__ = "Gauge32"
_ChrComPmSonetSEFS_Object = MibTableColumn
chrComPmSonetSEFS = _ChrComPmSonetSEFS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 7),
    _ChrComPmSonetSEFS_Type()
)
chrComPmSonetSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetSEFS.setStatus("current")


class _ChrComPmSonetCV_Type(Gauge32):
    """Custom type chrComPmSonetCV based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetCV_Type.__name__ = "Gauge32"
_ChrComPmSonetCV_Object = MibTableColumn
chrComPmSonetCV = _ChrComPmSonetCV_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 8),
    _ChrComPmSonetCV_Type()
)
chrComPmSonetCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetCV.setStatus("current")


class _ChrComPmSonetThresholdProfIndex_Type(Unsigned32):
    """Custom type chrComPmSonetThresholdProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetThresholdProfIndex_Type.__name__ = "Unsigned32"
_ChrComPmSonetThresholdProfIndex_Object = MibTableColumn
chrComPmSonetThresholdProfIndex = _ChrComPmSonetThresholdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 9),
    _ChrComPmSonetThresholdProfIndex_Type()
)
chrComPmSonetThresholdProfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetThresholdProfIndex.setStatus("current")
_ChrComPmSonetResetPmCountersAction_Type = TruthValue
_ChrComPmSonetResetPmCountersAction_Object = MibTableColumn
chrComPmSonetResetPmCountersAction = _ChrComPmSonetResetPmCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 3, 1, 10),
    _ChrComPmSonetResetPmCountersAction_Type()
)
chrComPmSonetResetPmCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmSonetResetPmCountersAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmSonetSNT-S-Day-MIB",
    **{"chrComPmSonetSNT-S-DayTable": chrComPmSonetSNT_S_DayTable,
       "chrComPmSonetSNT-S-DayEntry": chrComPmSonetSNT_S_DayEntry,
       "chrComPmSonetDayNumber": chrComPmSonetDayNumber,
       "chrComPmSonetSuspectedInterval": chrComPmSonetSuspectedInterval,
       "chrComPmSonetElapsedTime": chrComPmSonetElapsedTime,
       "chrComPmSonetSuppressedIntrvls": chrComPmSonetSuppressedIntrvls,
       "chrComPmSonetES": chrComPmSonetES,
       "chrComPmSonetSES": chrComPmSonetSES,
       "chrComPmSonetSEFS": chrComPmSonetSEFS,
       "chrComPmSonetCV": chrComPmSonetCV,
       "chrComPmSonetThresholdProfIndex": chrComPmSonetThresholdProfIndex,
       "chrComPmSonetResetPmCountersAction": chrComPmSonetResetPmCountersAction}
)
