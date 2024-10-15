# SNMP MIB module (ChrComIfOpticsOTS-SRC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComIfOpticsOTS-SRC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:50 2024
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

_ChrComIfOpticsOTS_SRCTable_Object = MibTable
chrComIfOpticsOTS_SRCTable = _ChrComIfOpticsOTS_SRCTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    chrComIfOpticsOTS_SRCTable.setStatus("current")
_ChrComIfOpticsOTS_SRCEntry_Object = MibTableRow
chrComIfOpticsOTS_SRCEntry = _ChrComIfOpticsOTS_SRCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1)
)
chrComIfOpticsOTS_SRCEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
)
if mibBuilder.loadTexts:
    chrComIfOpticsOTS_SRCEntry.setStatus("current")


class _ChrComIfOpticsOtsSrcOutPower_Type(Integer32):
    """Custom type chrComIfOpticsOtsSrcOutPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-501, 300),
    )


_ChrComIfOpticsOtsSrcOutPower_Type.__name__ = "Integer32"
_ChrComIfOpticsOtsSrcOutPower_Object = MibTableColumn
chrComIfOpticsOtsSrcOutPower = _ChrComIfOpticsOtsSrcOutPower_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 1),
    _ChrComIfOpticsOtsSrcOutPower_Type()
)
chrComIfOpticsOtsSrcOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComIfOpticsOtsSrcOutPower.setStatus("current")


class _ChrComIfOpticsOtsSrcLOOPThr_Type(Integer32):
    """Custom type chrComIfOpticsOtsSrcLOOPThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-501, 300),
    )


_ChrComIfOpticsOtsSrcLOOPThr_Type.__name__ = "Integer32"
_ChrComIfOpticsOtsSrcLOOPThr_Object = MibTableColumn
chrComIfOpticsOtsSrcLOOPThr = _ChrComIfOpticsOtsSrcLOOPThr_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 2),
    _ChrComIfOpticsOtsSrcLOOPThr_Type()
)
chrComIfOpticsOtsSrcLOOPThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfOpticsOtsSrcLOOPThr.setStatus("current")


class _ChrComIfOpticsOtsSrcSafetyThr_Type(Integer32):
    """Custom type chrComIfOpticsOtsSrcSafetyThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-501, 300),
    )


_ChrComIfOpticsOtsSrcSafetyThr_Type.__name__ = "Integer32"
_ChrComIfOpticsOtsSrcSafetyThr_Object = MibTableColumn
chrComIfOpticsOtsSrcSafetyThr = _ChrComIfOpticsOtsSrcSafetyThr_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 3),
    _ChrComIfOpticsOtsSrcSafetyThr_Type()
)
chrComIfOpticsOtsSrcSafetyThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComIfOpticsOtsSrcSafetyThr.setStatus("current")


class _ChrComIfOpticsAlarmVector_Type(Unsigned32):
    """Custom type chrComIfOpticsAlarmVector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComIfOpticsAlarmVector_Type.__name__ = "Unsigned32"
_ChrComIfOpticsAlarmVector_Object = MibTableColumn
chrComIfOpticsAlarmVector = _ChrComIfOpticsAlarmVector_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 5),
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
    "ChrComIfOpticsOTS-SRC-MIB",
    **{"chrComIfOpticsOTS-SRCTable": chrComIfOpticsOTS_SRCTable,
       "chrComIfOpticsOTS-SRCEntry": chrComIfOpticsOTS_SRCEntry,
       "chrComIfOpticsOtsSrcOutPower": chrComIfOpticsOtsSrcOutPower,
       "chrComIfOpticsOtsSrcLOOPThr": chrComIfOpticsOtsSrcLOOPThr,
       "chrComIfOpticsOtsSrcSafetyThr": chrComIfOpticsOtsSrcSafetyThr,
       "chrComIfOpticsAlarmVector": chrComIfOpticsAlarmVector,
       "chrComIfOpticsAlarmSeverityProfileIndex": chrComIfOpticsAlarmSeverityProfileIndex}
)
