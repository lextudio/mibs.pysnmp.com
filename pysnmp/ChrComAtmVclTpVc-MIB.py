# SNMP MIB module (ChrComAtmVclTpVc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComAtmVclTpVc-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:33 2024
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

(OperStatus,) = mibBuilder.importSymbols(
    "CISCO-RHINO-MIB",
    "OperStatus")

(TruthValue,) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "TruthValue")

(chrComAtmVcl,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComAtmVcl")

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

_ChrComAtmVclTpVcTable_Object = MibTable
chrComAtmVclTpVcTable = _ChrComAtmVclTpVcTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    chrComAtmVclTpVcTable.setStatus("current")
_ChrComAtmVclTpVcEntry_Object = MibTableRow
chrComAtmVclTpVcEntry = _ChrComAtmVclTpVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1)
)
chrComAtmVclTpVcEntry.setIndexNames(
    (0, "ChrComAtmVclTpVc-MIB", "chrComAtmVclifIndex"),
    (0, "ChrComAtmVclTpVc-MIB", "chrComAtmVclAtmVclVpi"),
    (0, "ChrComAtmVclTpVc-MIB", "chrComAtmVclAtmVclVci"),
)
if mibBuilder.loadTexts:
    chrComAtmVclTpVcEntry.setStatus("current")


class _ChrComAtmVclifIndex_Type(Unsigned32):
    """Custom type chrComAtmVclifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVclifIndex_Type.__name__ = "Unsigned32"
_ChrComAtmVclifIndex_Object = MibTableColumn
chrComAtmVclifIndex = _ChrComAtmVclifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 1),
    _ChrComAtmVclifIndex_Type()
)
chrComAtmVclifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclifIndex.setStatus("current")


class _ChrComAtmVclAtmVclVpi_Type(Unsigned32):
    """Custom type chrComAtmVclAtmVclVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVclAtmVclVpi_Type.__name__ = "Unsigned32"
_ChrComAtmVclAtmVclVpi_Object = MibTableColumn
chrComAtmVclAtmVclVpi = _ChrComAtmVclAtmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 2),
    _ChrComAtmVclAtmVclVpi_Type()
)
chrComAtmVclAtmVclVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclAtmVclVpi.setStatus("current")


class _ChrComAtmVclAtmVclVci_Type(Unsigned32):
    """Custom type chrComAtmVclAtmVclVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVclAtmVclVci_Type.__name__ = "Unsigned32"
_ChrComAtmVclAtmVclVci_Object = MibTableColumn
chrComAtmVclAtmVclVci = _ChrComAtmVclAtmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 3),
    _ChrComAtmVclAtmVclVci_Type()
)
chrComAtmVclAtmVclVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclAtmVclVci.setStatus("current")
_ChrComAtmVclCCSource_Type = TruthValue
_ChrComAtmVclCCSource_Object = MibTableColumn
chrComAtmVclCCSource = _ChrComAtmVclCCSource_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 4),
    _ChrComAtmVclCCSource_Type()
)
chrComAtmVclCCSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclCCSource.setStatus("current")
_ChrComAtmVclCCSink_Type = TruthValue
_ChrComAtmVclCCSink_Object = MibTableColumn
chrComAtmVclCCSink = _ChrComAtmVclCCSink_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 5),
    _ChrComAtmVclCCSink_Type()
)
chrComAtmVclCCSink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclCCSink.setStatus("current")
_ChrComAtmVclTPOperStatus_Type = OperStatus
_ChrComAtmVclTPOperStatus_Object = MibTableColumn
chrComAtmVclTPOperStatus = _ChrComAtmVclTPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 6),
    _ChrComAtmVclTPOperStatus_Type()
)
chrComAtmVclTPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComAtmVclTPOperStatus.setStatus("current")


class _ChrComAtmVclAlarmVector_Type(Integer32):
    """Custom type chrComAtmVclAlarmVector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComAtmVclAlarmVector_Type.__name__ = "Integer32"
_ChrComAtmVclAlarmVector_Object = MibTableColumn
chrComAtmVclAlarmVector = _ChrComAtmVclAlarmVector_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 7),
    _ChrComAtmVclAlarmVector_Type()
)
chrComAtmVclAlarmVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComAtmVclAlarmVector.setStatus("current")


class _ChrComAtmVclAlarmSeverityProfileIndex_Type(Unsigned32):
    """Custom type chrComAtmVclAlarmSeverityProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVclAlarmSeverityProfileIndex_Type.__name__ = "Unsigned32"
_ChrComAtmVclAlarmSeverityProfileIndex_Object = MibTableColumn
chrComAtmVclAlarmSeverityProfileIndex = _ChrComAtmVclAlarmSeverityProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2, 2, 1, 8),
    _ChrComAtmVclAlarmSeverityProfileIndex_Type()
)
chrComAtmVclAlarmSeverityProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVclAlarmSeverityProfileIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComAtmVclTpVc-MIB",
    **{"chrComAtmVclTpVcTable": chrComAtmVclTpVcTable,
       "chrComAtmVclTpVcEntry": chrComAtmVclTpVcEntry,
       "chrComAtmVclifIndex": chrComAtmVclifIndex,
       "chrComAtmVclAtmVclVpi": chrComAtmVclAtmVclVpi,
       "chrComAtmVclAtmVclVci": chrComAtmVclAtmVclVci,
       "chrComAtmVclCCSource": chrComAtmVclCCSource,
       "chrComAtmVclCCSink": chrComAtmVclCCSink,
       "chrComAtmVclTPOperStatus": chrComAtmVclTPOperStatus,
       "chrComAtmVclAlarmVector": chrComAtmVclAlarmVector,
       "chrComAtmVclAlarmSeverityProfileIndex": chrComAtmVclAlarmSeverityProfileIndex}
)
