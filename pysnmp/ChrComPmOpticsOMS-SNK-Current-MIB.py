# SNMP MIB module (ChrComPmOpticsOMS-SNK-Current-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmOpticsOMS-SNK-Current-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:18 2024
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

_ChrComPmOpticsOMS_SNK_CurrentTable_Object = MibTable
chrComPmOpticsOMS_SNK_CurrentTable = _ChrComPmOpticsOMS_SNK_CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7)
)
if mibBuilder.loadTexts:
    chrComPmOpticsOMS_SNK_CurrentTable.setStatus("current")
_ChrComPmOpticsOMS_SNK_CurrentEntry_Object = MibTableRow
chrComPmOpticsOMS_SNK_CurrentEntry = _ChrComPmOpticsOMS_SNK_CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1)
)
chrComPmOpticsOMS_SNK_CurrentEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
)
if mibBuilder.loadTexts:
    chrComPmOpticsOMS_SNK_CurrentEntry.setStatus("current")
_ChrComPmOpticsSuspectedIntrvl_Type = TruthValue
_ChrComPmOpticsSuspectedIntrvl_Object = MibTableColumn
chrComPmOpticsSuspectedIntrvl = _ChrComPmOpticsSuspectedIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 3),
    _ChrComPmOpticsSuppressedIntrvls_Type()
)
chrComPmOpticsSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSuppressedIntrvls.setStatus("current")


class _ChrComPmOpticsORS_Type(Gauge32):
    """Custom type chrComPmOpticsORS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsORS_Type.__name__ = "Gauge32"
_ChrComPmOpticsORS_Object = MibTableColumn
chrComPmOpticsORS = _ChrComPmOpticsORS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 4),
    _ChrComPmOpticsORS_Type()
)
chrComPmOpticsORS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsORS.setStatus("current")


class _ChrComPmOpticsSES_Type(Gauge32):
    """Custom type chrComPmOpticsSES based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsSES_Type.__name__ = "Gauge32"
_ChrComPmOpticsSES_Object = MibTableColumn
chrComPmOpticsSES = _ChrComPmOpticsSES_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 5),
    _ChrComPmOpticsSES_Type()
)
chrComPmOpticsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSES.setStatus("current")


class _ChrComPmOpticsUAS_Type(Gauge32):
    """Custom type chrComPmOpticsUAS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsUAS_Type.__name__ = "Gauge32"
_ChrComPmOpticsUAS_Object = MibTableColumn
chrComPmOpticsUAS = _ChrComPmOpticsUAS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 6),
    _ChrComPmOpticsUAS_Type()
)
chrComPmOpticsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsUAS.setStatus("current")


class _ChrComPmOpticsMean_Type(Integer32):
    """Custom type chrComPmOpticsMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMean_Type.__name__ = "Integer32"
_ChrComPmOpticsMean_Object = MibTableColumn
chrComPmOpticsMean = _ChrComPmOpticsMean_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 7),
    _ChrComPmOpticsMean_Type()
)
chrComPmOpticsMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMean.setStatus("current")


class _ChrComPmOpticsMax_Type(Integer32):
    """Custom type chrComPmOpticsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMax_Type.__name__ = "Integer32"
_ChrComPmOpticsMax_Object = MibTableColumn
chrComPmOpticsMax = _ChrComPmOpticsMax_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 8),
    _ChrComPmOpticsMax_Type()
)
chrComPmOpticsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMax.setStatus("current")


class _ChrComPmOpticsMin_Type(Integer32):
    """Custom type chrComPmOpticsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsMin_Type.__name__ = "Integer32"
_ChrComPmOpticsMin_Object = MibTableColumn
chrComPmOpticsMin = _ChrComPmOpticsMin_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 9),
    _ChrComPmOpticsMin_Type()
)
chrComPmOpticsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsMin.setStatus("current")


class _ChrComPmOpticsSD_Type(Integer32):
    """Custom type chrComPmOpticsSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChrComPmOpticsSD_Type.__name__ = "Integer32"
_ChrComPmOpticsSD_Object = MibTableColumn
chrComPmOpticsSD = _ChrComPmOpticsSD_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 10),
    _ChrComPmOpticsSD_Type()
)
chrComPmOpticsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmOpticsSD.setStatus("current")


class _ChrComPmOpticsThresholdProfIndex_Type(Unsigned32):
    """Custom type chrComPmOpticsThresholdProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmOpticsThresholdProfIndex_Type.__name__ = "Unsigned32"
_ChrComPmOpticsThresholdProfIndex_Object = MibTableColumn
chrComPmOpticsThresholdProfIndex = _ChrComPmOpticsThresholdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 11),
    _ChrComPmOpticsThresholdProfIndex_Type()
)
chrComPmOpticsThresholdProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmOpticsThresholdProfIndex.setStatus("current")
_ChrComPmOpticsResetCountersAction_Type = TruthValue
_ChrComPmOpticsResetCountersAction_Object = MibTableColumn
chrComPmOpticsResetCountersAction = _ChrComPmOpticsResetCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 7, 1, 12),
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
    "ChrComPmOpticsOMS-SNK-Current-MIB",
    **{"chrComPmOpticsOMS-SNK-CurrentTable": chrComPmOpticsOMS_SNK_CurrentTable,
       "chrComPmOpticsOMS-SNK-CurrentEntry": chrComPmOpticsOMS_SNK_CurrentEntry,
       "chrComPmOpticsSuspectedIntrvl": chrComPmOpticsSuspectedIntrvl,
       "chrComPmOpticsElapsedTime": chrComPmOpticsElapsedTime,
       "chrComPmOpticsSuppressedIntrvls": chrComPmOpticsSuppressedIntrvls,
       "chrComPmOpticsORS": chrComPmOpticsORS,
       "chrComPmOpticsSES": chrComPmOpticsSES,
       "chrComPmOpticsUAS": chrComPmOpticsUAS,
       "chrComPmOpticsMean": chrComPmOpticsMean,
       "chrComPmOpticsMax": chrComPmOpticsMax,
       "chrComPmOpticsMin": chrComPmOpticsMin,
       "chrComPmOpticsSD": chrComPmOpticsSD,
       "chrComPmOpticsThresholdProfIndex": chrComPmOpticsThresholdProfIndex,
       "chrComPmOpticsResetCountersAction": chrComPmOpticsResetCountersAction}
)
