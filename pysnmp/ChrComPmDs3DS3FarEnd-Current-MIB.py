# SNMP MIB module (ChrComPmDs3DS3FarEnd-Current-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmDs3DS3FarEnd-Current-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:10 2024
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

(chrComPmDs3,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmDs3")

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

_ChrComPmDs3DS3FarEnd_CurrentTable_Object = MibTable
chrComPmDs3DS3FarEnd_CurrentTable = _ChrComPmDs3DS3FarEnd_CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13)
)
if mibBuilder.loadTexts:
    chrComPmDs3DS3FarEnd_CurrentTable.setStatus("current")
_ChrComPmDs3DS3FarEnd_CurrentEntry_Object = MibTableRow
chrComPmDs3DS3FarEnd_CurrentEntry = _ChrComPmDs3DS3FarEnd_CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1)
)
chrComPmDs3DS3FarEnd_CurrentEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
)
if mibBuilder.loadTexts:
    chrComPmDs3DS3FarEnd_CurrentEntry.setStatus("current")
_ChrComPmDs3SuspectedInterval_Type = TruthValue
_ChrComPmDs3SuspectedInterval_Object = MibTableColumn
chrComPmDs3SuspectedInterval = _ChrComPmDs3SuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 1),
    _ChrComPmDs3SuspectedInterval_Type()
)
chrComPmDs3SuspectedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3SuspectedInterval.setStatus("current")


class _ChrComPmDs3ElapsedTime_Type(Unsigned32):
    """Custom type chrComPmDs3ElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3ElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmDs3ElapsedTime_Object = MibTableColumn
chrComPmDs3ElapsedTime = _ChrComPmDs3ElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 2),
    _ChrComPmDs3ElapsedTime_Type()
)
chrComPmDs3ElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3ElapsedTime.setStatus("current")


class _ChrComPmDs3SuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmDs3SuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3SuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmDs3SuppressedIntrvls_Object = MibTableColumn
chrComPmDs3SuppressedIntrvls = _ChrComPmDs3SuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 3),
    _ChrComPmDs3SuppressedIntrvls_Type()
)
chrComPmDs3SuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3SuppressedIntrvls.setStatus("current")


class _ChrComPmDs3CCV_Type(Gauge32):
    """Custom type chrComPmDs3CCV based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3CCV_Type.__name__ = "Gauge32"
_ChrComPmDs3CCV_Object = MibTableColumn
chrComPmDs3CCV = _ChrComPmDs3CCV_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 4),
    _ChrComPmDs3CCV_Type()
)
chrComPmDs3CCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3CCV.setStatus("current")


class _ChrComPmDs3CES_Type(Gauge32):
    """Custom type chrComPmDs3CES based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3CES_Type.__name__ = "Gauge32"
_ChrComPmDs3CES_Object = MibTableColumn
chrComPmDs3CES = _ChrComPmDs3CES_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 5),
    _ChrComPmDs3CES_Type()
)
chrComPmDs3CES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3CES.setStatus("current")


class _ChrComPmDs3CSES_Type(Gauge32):
    """Custom type chrComPmDs3CSES based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3CSES_Type.__name__ = "Gauge32"
_ChrComPmDs3CSES_Object = MibTableColumn
chrComPmDs3CSES = _ChrComPmDs3CSES_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 6),
    _ChrComPmDs3CSES_Type()
)
chrComPmDs3CSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3CSES.setStatus("current")


class _ChrComPmDs3SAS_Type(Gauge32):
    """Custom type chrComPmDs3SAS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3SAS_Type.__name__ = "Gauge32"
_ChrComPmDs3SAS_Object = MibTableColumn
chrComPmDs3SAS = _ChrComPmDs3SAS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 7),
    _ChrComPmDs3SAS_Type()
)
chrComPmDs3SAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3SAS.setStatus("current")


class _ChrComPmDs3UASCP_Type(Gauge32):
    """Custom type chrComPmDs3UASCP based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3UASCP_Type.__name__ = "Gauge32"
_ChrComPmDs3UASCP_Object = MibTableColumn
chrComPmDs3UASCP = _ChrComPmDs3UASCP_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 8),
    _ChrComPmDs3UASCP_Type()
)
chrComPmDs3UASCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3UASCP.setStatus("current")


class _ChrComPmDs3ESPLCP_Type(Gauge32):
    """Custom type chrComPmDs3ESPLCP based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3ESPLCP_Type.__name__ = "Gauge32"
_ChrComPmDs3ESPLCP_Object = MibTableColumn
chrComPmDs3ESPLCP = _ChrComPmDs3ESPLCP_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 9),
    _ChrComPmDs3ESPLCP_Type()
)
chrComPmDs3ESPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmDs3ESPLCP.setStatus("current")


class _ChrComPmDs3ThresholdProfIndex_Type(Unsigned32):
    """Custom type chrComPmDs3ThresholdProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmDs3ThresholdProfIndex_Type.__name__ = "Unsigned32"
_ChrComPmDs3ThresholdProfIndex_Object = MibTableColumn
chrComPmDs3ThresholdProfIndex = _ChrComPmDs3ThresholdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 10),
    _ChrComPmDs3ThresholdProfIndex_Type()
)
chrComPmDs3ThresholdProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmDs3ThresholdProfIndex.setStatus("current")
_ChrComPmDs3ResetPmCountersAction_Type = TruthValue
_ChrComPmDs3ResetPmCountersAction_Object = MibTableColumn
chrComPmDs3ResetPmCountersAction = _ChrComPmDs3ResetPmCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 13, 1, 11),
    _ChrComPmDs3ResetPmCountersAction_Type()
)
chrComPmDs3ResetPmCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmDs3ResetPmCountersAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmDs3DS3FarEnd-Current-MIB",
    **{"chrComPmDs3DS3FarEnd-CurrentTable": chrComPmDs3DS3FarEnd_CurrentTable,
       "chrComPmDs3DS3FarEnd-CurrentEntry": chrComPmDs3DS3FarEnd_CurrentEntry,
       "chrComPmDs3SuspectedInterval": chrComPmDs3SuspectedInterval,
       "chrComPmDs3ElapsedTime": chrComPmDs3ElapsedTime,
       "chrComPmDs3SuppressedIntrvls": chrComPmDs3SuppressedIntrvls,
       "chrComPmDs3CCV": chrComPmDs3CCV,
       "chrComPmDs3CES": chrComPmDs3CES,
       "chrComPmDs3CSES": chrComPmDs3CSES,
       "chrComPmDs3SAS": chrComPmDs3SAS,
       "chrComPmDs3UASCP": chrComPmDs3UASCP,
       "chrComPmDs3ESPLCP": chrComPmDs3ESPLCP,
       "chrComPmDs3ThresholdProfIndex": chrComPmDs3ThresholdProfIndex,
       "chrComPmDs3ResetPmCountersAction": chrComPmDs3ResetPmCountersAction}
)
