# SNMP MIB module (CTFRAMER-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTFRAMER-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:25 2024
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

(ctFramerConfig,
 ctIfPortPortNumber) = mibBuilder.importSymbols(
    "CTIF-EXT-MIB",
    "ctFramerConfig",
    "ctIfPortPortNumber")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_CtFramerBaseConfig_ObjectIdentity = ObjectIdentity
ctFramerBaseConfig = _CtFramerBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1)
)
_CtFramerConfigTable_Object = MibTable
ctFramerConfigTable = _CtFramerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    ctFramerConfigTable.setStatus("mandatory")
_CtFramerConfigEntry_Object = MibTableRow
ctFramerConfigEntry = _CtFramerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1)
)
ctFramerConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctFramerConfigEntry.setStatus("mandatory")


class _CtFramerStatsConfig_Type(Integer32):
    """Custom type ctFramerStatsConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtFramerStatsConfig_Type.__name__ = "Integer32"
_CtFramerStatsConfig_Object = MibTableColumn
ctFramerStatsConfig = _CtFramerStatsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 1),
    _CtFramerStatsConfig_Type()
)
ctFramerStatsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerStatsConfig.setStatus("mandatory")


class _CtFramerAlarmsConfig_Type(Integer32):
    """Custom type ctFramerAlarmsConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtFramerAlarmsConfig_Type.__name__ = "Integer32"
_CtFramerAlarmsConfig_Object = MibTableColumn
ctFramerAlarmsConfig = _CtFramerAlarmsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 2),
    _CtFramerAlarmsConfig_Type()
)
ctFramerAlarmsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerAlarmsConfig.setStatus("mandatory")


class _CtFramerMediumConfig_Type(Integer32):
    """Custom type ctFramerMediumConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_CtFramerMediumConfig_Type.__name__ = "Integer32"
_CtFramerMediumConfig_Object = MibTableColumn
ctFramerMediumConfig = _CtFramerMediumConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 3),
    _CtFramerMediumConfig_Type()
)
ctFramerMediumConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerMediumConfig.setStatus("mandatory")


class _CtFramerIdleCellsConfig_Type(Integer32):
    """Custom type ctFramerIdleCellsConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_CtFramerIdleCellsConfig_Type.__name__ = "Integer32"
_CtFramerIdleCellsConfig_Object = MibTableColumn
ctFramerIdleCellsConfig = _CtFramerIdleCellsConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 4),
    _CtFramerIdleCellsConfig_Type()
)
ctFramerIdleCellsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerIdleCellsConfig.setStatus("mandatory")


class _CtFramerCellPayScramConfig_Type(Integer32):
    """Custom type ctFramerCellPayScramConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtFramerCellPayScramConfig_Type.__name__ = "Integer32"
_CtFramerCellPayScramConfig_Object = MibTableColumn
ctFramerCellPayScramConfig = _CtFramerCellPayScramConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 5),
    _CtFramerCellPayScramConfig_Type()
)
ctFramerCellPayScramConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFramerCellPayScramConfig.setStatus("mandatory")
_CtFramerSonetConfig_ObjectIdentity = ObjectIdentity
ctFramerSonetConfig = _CtFramerSonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 2)
)
_CtFramerDS3Config_ObjectIdentity = ObjectIdentity
ctFramerDS3Config = _CtFramerDS3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTFRAMER-CONFIG-MIB",
    **{"ctFramerBaseConfig": ctFramerBaseConfig,
       "ctFramerConfigTable": ctFramerConfigTable,
       "ctFramerConfigEntry": ctFramerConfigEntry,
       "ctFramerStatsConfig": ctFramerStatsConfig,
       "ctFramerAlarmsConfig": ctFramerAlarmsConfig,
       "ctFramerMediumConfig": ctFramerMediumConfig,
       "ctFramerIdleCellsConfig": ctFramerIdleCellsConfig,
       "ctFramerCellPayScramConfig": ctFramerCellPayScramConfig,
       "ctFramerSonetConfig": ctFramerSonetConfig,
       "ctFramerDS3Config": ctFramerDS3Config}
)
