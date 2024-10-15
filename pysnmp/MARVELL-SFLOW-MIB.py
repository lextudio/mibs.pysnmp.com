# SNMP MIB module (MARVELL-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:21 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlsFlowMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 147)
)
rlsFlowMib.setRevisions(
        ("2009-10-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlsFlowStatisticsTable_Object = MibTable
rlsFlowStatisticsTable = _RlsFlowStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1)
)
if mibBuilder.loadTexts:
    rlsFlowStatisticsTable.setStatus("current")
_RlsFlowStatisticsEntry_Object = MibTableRow
rlsFlowStatisticsEntry = _RlsFlowStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1, 1)
)
rlsFlowStatisticsEntry.setIndexNames(
    (0, "MARVELL-SFLOW-MIB", "rlsFlowDataSource"),
)
if mibBuilder.loadTexts:
    rlsFlowStatisticsEntry.setStatus("current")
_RlsFlowDataSource_Type = ObjectIdentifier
_RlsFlowDataSource_Object = MibTableColumn
rlsFlowDataSource = _RlsFlowDataSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 1),
    _RlsFlowDataSource_Type()
)
rlsFlowDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsFlowDataSource.setStatus("current")
_RlsFlowStatisticsSampledPackets_Type = Counter32
_RlsFlowStatisticsSampledPackets_Object = MibTableColumn
rlsFlowStatisticsSampledPackets = _RlsFlowStatisticsSampledPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 2),
    _RlsFlowStatisticsSampledPackets_Type()
)
rlsFlowStatisticsSampledPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsFlowStatisticsSampledPackets.setStatus("current")
_RlsFlowStatisticsDatagramSent_Type = Counter32
_RlsFlowStatisticsDatagramSent_Object = MibTableColumn
rlsFlowStatisticsDatagramSent = _RlsFlowStatisticsDatagramSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 3),
    _RlsFlowStatisticsDatagramSent_Type()
)
rlsFlowStatisticsDatagramSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsFlowStatisticsDatagramSent.setStatus("current")


class _RlsFlowStatisticsAction_Type(Integer32):
    """Custom type rlsFlowStatisticsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_RlsFlowStatisticsAction_Type.__name__ = "Integer32"
_RlsFlowStatisticsAction_Object = MibTableColumn
rlsFlowStatisticsAction = _RlsFlowStatisticsAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 1, 1, 4),
    _RlsFlowStatisticsAction_Type()
)
rlsFlowStatisticsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlsFlowStatisticsAction.setStatus("current")


class _RlsFlowStatisticsReset_Type(Integer32):
    """Custom type rlsFlowStatisticsReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_RlsFlowStatisticsReset_Type.__name__ = "Integer32"
_RlsFlowStatisticsReset_Object = MibScalar
rlsFlowStatisticsReset = _RlsFlowStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 147, 2),
    _RlsFlowStatisticsReset_Type()
)
rlsFlowStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlsFlowStatisticsReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-SFLOW-MIB",
    **{"rlsFlowMib": rlsFlowMib,
       "rlsFlowStatisticsTable": rlsFlowStatisticsTable,
       "rlsFlowStatisticsEntry": rlsFlowStatisticsEntry,
       "rlsFlowDataSource": rlsFlowDataSource,
       "rlsFlowStatisticsSampledPackets": rlsFlowStatisticsSampledPackets,
       "rlsFlowStatisticsDatagramSent": rlsFlowStatisticsDatagramSent,
       "rlsFlowStatisticsAction": rlsFlowStatisticsAction,
       "rlsFlowStatisticsReset": rlsFlowStatisticsReset}
)
