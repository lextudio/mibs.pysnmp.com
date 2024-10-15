# SNMP MIB module (GBOND-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBOND-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:02 2024
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

(gBondMIB,) = mibBuilder.importSymbols(
    "GBOND-MIB",
    "gBondMIB")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

gBondAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1)
)
gBondAtmMIB.setRevisions(
        ("2007-05-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GBondAtmObjects_ObjectIdentity = ObjectIdentity
gBondAtmObjects = _GBondAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 1)
)
_GBondAtmPort_ObjectIdentity = ObjectIdentity
gBondAtmPort = _GBondAtmPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1)
)
_GBondAtmPortConfTable_Object = MibTable
gBondAtmPortConfTable = _GBondAtmPortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gBondAtmPortConfTable.setStatus("current")
_GBondAtmPortConfEntry_Object = MibTableRow
gBondAtmPortConfEntry = _GBondAtmPortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1)
)
gBondAtmPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondAtmPortConfEntry.setStatus("current")


class _GBondAtmUpMaxDataRate_Type(Unsigned32):
    """Custom type gBondAtmUpMaxDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
        ValueRangeConstraint(9999999, 9999999),
    )


_GBondAtmUpMaxDataRate_Type.__name__ = "Unsigned32"
_GBondAtmUpMaxDataRate_Object = MibTableColumn
gBondAtmUpMaxDataRate = _GBondAtmUpMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1, 1),
    _GBondAtmUpMaxDataRate_Type()
)
gBondAtmUpMaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondAtmUpMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondAtmUpMaxDataRate.setUnits("Kbps")


class _GBondAtmDownMaxDataRate_Type(Unsigned32):
    """Custom type gBondAtmDownMaxDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
        ValueRangeConstraint(9999999, 9999999),
    )


_GBondAtmDownMaxDataRate_Type.__name__ = "Unsigned32"
_GBondAtmDownMaxDataRate_Object = MibTableColumn
gBondAtmDownMaxDataRate = _GBondAtmDownMaxDataRate_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1, 2),
    _GBondAtmDownMaxDataRate_Type()
)
gBondAtmDownMaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondAtmDownMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    gBondAtmDownMaxDataRate.setUnits("Kbps")


class _GBondAtmUpDiffDelayTolerence_Type(Unsigned32):
    """Custom type gBondAtmUpDiffDelayTolerence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8176),
    )


_GBondAtmUpDiffDelayTolerence_Type.__name__ = "Unsigned32"
_GBondAtmUpDiffDelayTolerence_Object = MibTableColumn
gBondAtmUpDiffDelayTolerence = _GBondAtmUpDiffDelayTolerence_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1, 3),
    _GBondAtmUpDiffDelayTolerence_Type()
)
gBondAtmUpDiffDelayTolerence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondAtmUpDiffDelayTolerence.setStatus("current")
if mibBuilder.loadTexts:
    gBondAtmUpDiffDelayTolerence.setUnits("milliseconds")


class _GBondAtmDownDiffDelayTolerence_Type(Unsigned32):
    """Custom type gBondAtmDownDiffDelayTolerence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8176),
    )


_GBondAtmDownDiffDelayTolerence_Type.__name__ = "Unsigned32"
_GBondAtmDownDiffDelayTolerence_Object = MibTableColumn
gBondAtmDownDiffDelayTolerence = _GBondAtmDownDiffDelayTolerence_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 1, 1, 4),
    _GBondAtmDownDiffDelayTolerence_Type()
)
gBondAtmDownDiffDelayTolerence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gBondAtmDownDiffDelayTolerence.setStatus("current")
if mibBuilder.loadTexts:
    gBondAtmDownDiffDelayTolerence.setUnits("milliseconds")
_GBondAtmPortStatusTable_Object = MibTable
gBondAtmPortStatusTable = _GBondAtmPortStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gBondAtmPortStatusTable.setStatus("current")
_GBondAtmPortStatusEntry_Object = MibTableRow
gBondAtmPortStatusEntry = _GBondAtmPortStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 2, 1)
)
gBondAtmPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gBondAtmPortStatusEntry.setStatus("current")
_GBondAtmShowTime_Type = TimeTicks
_GBondAtmShowTime_Object = MibTableColumn
gBondAtmShowTime = _GBondAtmShowTime_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 2, 1, 1),
    _GBondAtmShowTime_Type()
)
gBondAtmShowTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondAtmShowTime.setStatus("current")
if mibBuilder.loadTexts:
    gBondAtmShowTime.setUnits("seconds")
_GBondAtmUpRxCellLossCount_Type = Counter32
_GBondAtmUpRxCellLossCount_Object = MibTableColumn
gBondAtmUpRxCellLossCount = _GBondAtmUpRxCellLossCount_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 2, 1, 2),
    _GBondAtmUpRxCellLossCount_Type()
)
gBondAtmUpRxCellLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondAtmUpRxCellLossCount.setStatus("current")
_GBondAtmDownRxCellLossCount_Type = Counter32
_GBondAtmDownRxCellLossCount_Object = MibTableColumn
gBondAtmDownRxCellLossCount = _GBondAtmDownRxCellLossCount_Object(
    (1, 3, 6, 1, 2, 1, 211, 1, 1, 1, 2, 1, 3),
    _GBondAtmDownRxCellLossCount_Type()
)
gBondAtmDownRxCellLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gBondAtmDownRxCellLossCount.setStatus("current")
_GBondAtmConformance_ObjectIdentity = ObjectIdentity
gBondAtmConformance = _GBondAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 2)
)
_GBondAtmGroups_ObjectIdentity = ObjectIdentity
gBondAtmGroups = _GBondAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 1)
)
_GBondAtmCompliances_ObjectIdentity = ObjectIdentity
gBondAtmCompliances = _GBondAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 2)
)

# Managed Objects groups

gBondAtmBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 1, 1)
)
gBondAtmBasicGroup.setObjects(
      *(("GBOND-ATM-MIB", "gBondAtmUpMaxDataRate"),
        ("GBOND-ATM-MIB", "gBondAtmDownMaxDataRate"),
        ("GBOND-ATM-MIB", "gBondAtmUpDiffDelayTolerence"),
        ("GBOND-ATM-MIB", "gBondAtmDownDiffDelayTolerence"),
        ("GBOND-ATM-MIB", "gBondAtmShowTime"),
        ("GBOND-ATM-MIB", "gBondAtmUpRxCellLossCount"),
        ("GBOND-ATM-MIB", "gBondAtmDownRxCellLossCount"))
)
if mibBuilder.loadTexts:
    gBondAtmBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gBondAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 211, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gBondAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBOND-ATM-MIB",
    **{"gBondAtmMIB": gBondAtmMIB,
       "gBondAtmObjects": gBondAtmObjects,
       "gBondAtmPort": gBondAtmPort,
       "gBondAtmPortConfTable": gBondAtmPortConfTable,
       "gBondAtmPortConfEntry": gBondAtmPortConfEntry,
       "gBondAtmUpMaxDataRate": gBondAtmUpMaxDataRate,
       "gBondAtmDownMaxDataRate": gBondAtmDownMaxDataRate,
       "gBondAtmUpDiffDelayTolerence": gBondAtmUpDiffDelayTolerence,
       "gBondAtmDownDiffDelayTolerence": gBondAtmDownDiffDelayTolerence,
       "gBondAtmPortStatusTable": gBondAtmPortStatusTable,
       "gBondAtmPortStatusEntry": gBondAtmPortStatusEntry,
       "gBondAtmShowTime": gBondAtmShowTime,
       "gBondAtmUpRxCellLossCount": gBondAtmUpRxCellLossCount,
       "gBondAtmDownRxCellLossCount": gBondAtmDownRxCellLossCount,
       "gBondAtmConformance": gBondAtmConformance,
       "gBondAtmGroups": gBondAtmGroups,
       "gBondAtmBasicGroup": gBondAtmBasicGroup,
       "gBondAtmCompliances": gBondAtmCompliances,
       "gBondAtmCompliance": gBondAtmCompliance}
)
