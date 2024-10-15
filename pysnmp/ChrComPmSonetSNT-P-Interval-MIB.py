# SNMP MIB module (ChrComPmSonetSNT-P-Interval-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmSonetSNT-P-Interval-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:35 2024
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

_ChrComPmSonetSNT_P_IntervalTable_Object = MibTable
chrComPmSonetSNT_P_IntervalTable = _ChrComPmSonetSNT_P_IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11)
)
if mibBuilder.loadTexts:
    chrComPmSonetSNT_P_IntervalTable.setStatus("current")
_ChrComPmSonetSNT_P_IntervalEntry_Object = MibTableRow
chrComPmSonetSNT_P_IntervalEntry = _ChrComPmSonetSNT_P_IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1)
)
chrComPmSonetSNT_P_IntervalEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ChrComPmSonetSNT-P-Interval-MIB", "chrComPmSonetIntervalNumber"),
)
if mibBuilder.loadTexts:
    chrComPmSonetSNT_P_IntervalEntry.setStatus("current")


class _ChrComPmSonetIntervalNumber_Type(Unsigned32):
    """Custom type chrComPmSonetIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChrComPmSonetIntervalNumber_Type.__name__ = "Unsigned32"
_ChrComPmSonetIntervalNumber_Object = MibTableColumn
chrComPmSonetIntervalNumber = _ChrComPmSonetIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 1),
    _ChrComPmSonetIntervalNumber_Type()
)
chrComPmSonetIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetIntervalNumber.setStatus("current")
_ChrComPmSonetSuspectedInterval_Type = TruthValue
_ChrComPmSonetSuspectedInterval_Object = MibTableColumn
chrComPmSonetSuspectedInterval = _ChrComPmSonetSuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 6),
    _ChrComPmSonetSES_Type()
)
chrComPmSonetSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetSES.setStatus("current")


class _ChrComPmSonetCV_Type(Gauge32):
    """Custom type chrComPmSonetCV based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetCV_Type.__name__ = "Gauge32"
_ChrComPmSonetCV_Object = MibTableColumn
chrComPmSonetCV = _ChrComPmSonetCV_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 7),
    _ChrComPmSonetCV_Type()
)
chrComPmSonetCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetCV.setStatus("current")


class _ChrComPmSonetUAS_Type(Gauge32):
    """Custom type chrComPmSonetUAS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetUAS_Type.__name__ = "Gauge32"
_ChrComPmSonetUAS_Object = MibTableColumn
chrComPmSonetUAS = _ChrComPmSonetUAS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 8),
    _ChrComPmSonetUAS_Type()
)
chrComPmSonetUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetUAS.setStatus("current")


class _ChrComPmSonetPS_Type(Gauge32):
    """Custom type chrComPmSonetPS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmSonetPS_Type.__name__ = "Gauge32"
_ChrComPmSonetPS_Object = MibTableColumn
chrComPmSonetPS = _ChrComPmSonetPS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 9),
    _ChrComPmSonetPS_Type()
)
chrComPmSonetPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmSonetPS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmSonetSNT-P-Interval-MIB",
    **{"chrComPmSonetSNT-P-IntervalTable": chrComPmSonetSNT_P_IntervalTable,
       "chrComPmSonetSNT-P-IntervalEntry": chrComPmSonetSNT_P_IntervalEntry,
       "chrComPmSonetIntervalNumber": chrComPmSonetIntervalNumber,
       "chrComPmSonetSuspectedInterval": chrComPmSonetSuspectedInterval,
       "chrComPmSonetElapsedTime": chrComPmSonetElapsedTime,
       "chrComPmSonetSuppressedIntrvls": chrComPmSonetSuppressedIntrvls,
       "chrComPmSonetES": chrComPmSonetES,
       "chrComPmSonetSES": chrComPmSonetSES,
       "chrComPmSonetCV": chrComPmSonetCV,
       "chrComPmSonetUAS": chrComPmSonetUAS,
       "chrComPmSonetPS": chrComPmSonetPS}
)
