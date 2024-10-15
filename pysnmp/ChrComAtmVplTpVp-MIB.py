# SNMP MIB module (ChrComAtmVplTpVp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComAtmVplTpVp-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:34 2024
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

(chrComAtmVpl,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComAtmVpl")

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

_ChrComAtmVplTpVpTable_Object = MibTable
chrComAtmVplTpVpTable = _ChrComAtmVplTpVpTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    chrComAtmVplTpVpTable.setStatus("current")
_ChrComAtmVplTpVpEntry_Object = MibTableRow
chrComAtmVplTpVpEntry = _ChrComAtmVplTpVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1)
)
chrComAtmVplTpVpEntry.setIndexNames(
    (0, "ChrComAtmVplTpVp-MIB", "chrComAtmVplifIndex"),
    (0, "ChrComAtmVplTpVp-MIB", "chrComAtmVplAtmVplVpi"),
)
if mibBuilder.loadTexts:
    chrComAtmVplTpVpEntry.setStatus("current")


class _ChrComAtmVplifIndex_Type(Unsigned32):
    """Custom type chrComAtmVplifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVplifIndex_Type.__name__ = "Unsigned32"
_ChrComAtmVplifIndex_Object = MibTableColumn
chrComAtmVplifIndex = _ChrComAtmVplifIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 1),
    _ChrComAtmVplifIndex_Type()
)
chrComAtmVplifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVplifIndex.setStatus("current")


class _ChrComAtmVplAtmVplVpi_Type(Unsigned32):
    """Custom type chrComAtmVplAtmVplVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVplAtmVplVpi_Type.__name__ = "Unsigned32"
_ChrComAtmVplAtmVplVpi_Object = MibTableColumn
chrComAtmVplAtmVplVpi = _ChrComAtmVplAtmVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 2),
    _ChrComAtmVplAtmVplVpi_Type()
)
chrComAtmVplAtmVplVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVplAtmVplVpi.setStatus("current")
_ChrComAtmVplCCSource_Type = TruthValue
_ChrComAtmVplCCSource_Object = MibTableColumn
chrComAtmVplCCSource = _ChrComAtmVplCCSource_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 3),
    _ChrComAtmVplCCSource_Type()
)
chrComAtmVplCCSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVplCCSource.setStatus("current")
_ChrComAtmVplCCSink_Type = TruthValue
_ChrComAtmVplCCSink_Object = MibTableColumn
chrComAtmVplCCSink = _ChrComAtmVplCCSink_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 4),
    _ChrComAtmVplCCSink_Type()
)
chrComAtmVplCCSink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVplCCSink.setStatus("current")
_ChrComAtmVplTPOperStatus_Type = OperStatus
_ChrComAtmVplTPOperStatus_Object = MibTableColumn
chrComAtmVplTPOperStatus = _ChrComAtmVplTPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 5),
    _ChrComAtmVplTPOperStatus_Type()
)
chrComAtmVplTPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComAtmVplTPOperStatus.setStatus("current")


class _ChrComAtmVplAlarmVector_Type(Integer32):
    """Custom type chrComAtmVplAlarmVector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComAtmVplAlarmVector_Type.__name__ = "Integer32"
_ChrComAtmVplAlarmVector_Object = MibTableColumn
chrComAtmVplAlarmVector = _ChrComAtmVplAlarmVector_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 6),
    _ChrComAtmVplAlarmVector_Type()
)
chrComAtmVplAlarmVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComAtmVplAlarmVector.setStatus("current")


class _ChrComAtmVplAlarmSeverityProfileIndex_Type(Unsigned32):
    """Custom type chrComAtmVplAlarmSeverityProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComAtmVplAlarmSeverityProfileIndex_Type.__name__ = "Unsigned32"
_ChrComAtmVplAlarmSeverityProfileIndex_Object = MibTableColumn
chrComAtmVplAlarmSeverityProfileIndex = _ChrComAtmVplAlarmSeverityProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1, 2, 1, 7),
    _ChrComAtmVplAlarmSeverityProfileIndex_Type()
)
chrComAtmVplAlarmSeverityProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComAtmVplAlarmSeverityProfileIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComAtmVplTpVp-MIB",
    **{"chrComAtmVplTpVpTable": chrComAtmVplTpVpTable,
       "chrComAtmVplTpVpEntry": chrComAtmVplTpVpEntry,
       "chrComAtmVplifIndex": chrComAtmVplifIndex,
       "chrComAtmVplAtmVplVpi": chrComAtmVplAtmVplVpi,
       "chrComAtmVplCCSource": chrComAtmVplCCSource,
       "chrComAtmVplCCSink": chrComAtmVplCCSink,
       "chrComAtmVplTPOperStatus": chrComAtmVplTPOperStatus,
       "chrComAtmVplAlarmVector": chrComAtmVplAlarmVector,
       "chrComAtmVplAlarmSeverityProfileIndex": chrComAtmVplAlarmSeverityProfileIndex}
)
