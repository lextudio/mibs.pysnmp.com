# SNMP MIB module (ChrComIfOpticsOTS-SNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComIfOpticsOTS-SNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:49 2024
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

(chrComIfOptics,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComIfOptics")

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

_ChrComIfOpticsOTS_SNKTable_Object = MibTable
chrComIfOpticsOTS_SNKTable = _ChrComIfOpticsOTS_SNKTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    chrComIfOpticsOTS_SNKTable.setStatus("current")
_ChrComIfOpticsOTS_SNKEntry_Object = MibTableRow
chrComIfOpticsOTS_SNKEntry = _ChrComIfOpticsOTS_SNKEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1)
)
chrComIfOpticsOTS_SNKEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
)
if mibBuilder.loadTexts:
    chrComIfOpticsOTS_SNKEntry.setStatus("current")


class _ChrComIfOpticsOtsSnkInPower_Type(Integer32):
    """Custom type chrComIfOpticsOtsSnkInPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-501, 300),
    )


_ChrComIfOpticsOtsSnkInPower_Type.__name__ = "Integer32"
_ChrComIfOpticsOtsSnkInPower_Object = MibTableColumn
chrComIfOpticsOtsSnkInPower = _ChrComIfOpticsOtsSnkInPower_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 1),
    _ChrComIfOpticsOtsSnkInPower_Type()
)
chrComIfOpticsOtsSnkInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfOpticsOtsSnkInPower.setStatus("current")


class _ChrComIfOpticsOtsSnkLOOPThr_Type(Integer32):
    """Custom type chrComIfOpticsOtsSnkLOOPThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-501, 300),
    )


_ChrComIfOpticsOtsSnkLOOPThr_Type.__name__ = "Integer32"
_ChrComIfOpticsOtsSnkLOOPThr_Object = MibTableColumn
chrComIfOpticsOtsSnkLOOPThr = _ChrComIfOpticsOtsSnkLOOPThr_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 2),
    _ChrComIfOpticsOtsSnkLOOPThr_Type()
)
chrComIfOpticsOtsSnkLOOPThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfOpticsOtsSnkLOOPThr.setStatus("current")


class _ChrComIfOpticsAlarmVector_Type(Integer32):
    """Custom type chrComIfOpticsAlarmVector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComIfOpticsAlarmVector_Type.__name__ = "Integer32"
_ChrComIfOpticsAlarmVector_Object = MibTableColumn
chrComIfOpticsAlarmVector = _ChrComIfOpticsAlarmVector_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 3),
    _ChrComIfOpticsAlarmVector_Type()
)
chrComIfOpticsAlarmVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfOpticsAlarmVector.setStatus("current")


class _ChrComIfOpticsAlarmSeverityProfileIndex_Type(Unsigned32):
    """Custom type chrComIfOpticsAlarmSeverityProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfOpticsAlarmSeverityProfileIndex_Type.__name__ = "Unsigned32"
_ChrComIfOpticsAlarmSeverityProfileIndex_Object = MibTableColumn
chrComIfOpticsAlarmSeverityProfileIndex = _ChrComIfOpticsAlarmSeverityProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 4),
    _ChrComIfOpticsAlarmSeverityProfileIndex_Type()
)
chrComIfOpticsAlarmSeverityProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfOpticsAlarmSeverityProfileIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComIfOpticsOTS-SNK-MIB",
    **{"chrComIfOpticsOTS-SNKTable": chrComIfOpticsOTS_SNKTable,
       "chrComIfOpticsOTS-SNKEntry": chrComIfOpticsOTS_SNKEntry,
       "chrComIfOpticsOtsSnkInPower": chrComIfOpticsOtsSnkInPower,
       "chrComIfOpticsOtsSnkLOOPThr": chrComIfOpticsOtsSnkLOOPThr,
       "chrComIfOpticsAlarmVector": chrComIfOpticsAlarmVector,
       "chrComIfOpticsAlarmSeverityProfileIndex": chrComIfOpticsAlarmSeverityProfileIndex}
)
