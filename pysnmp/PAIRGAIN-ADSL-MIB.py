# SNMP MIB module (PAIRGAIN-ADSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-ADSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:13 2024
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

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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

pgAdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgAdslMIBObjects_ObjectIdentity = ObjectIdentity
pgAdslMIBObjects = _PgAdslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1)
)
_PgAdslClearStatTable_Object = MibTable
pgAdslClearStatTable = _PgAdslClearStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1)
)
if mibBuilder.loadTexts:
    pgAdslClearStatTable.setStatus("current")
_PgAdslClearStatEntry_Object = MibTableRow
pgAdslClearStatEntry = _PgAdslClearStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1)
)
pgAdslClearStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgAdslClearStatEntry.setStatus("current")


class _PgAdslAtucClearStat_Type(Integer32):
    """Custom type pgAdslAtucClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PgAdslAtucClearStat_Type.__name__ = "Integer32"
_PgAdslAtucClearStat_Object = MibTableColumn
pgAdslAtucClearStat = _PgAdslAtucClearStat_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1, 1),
    _PgAdslAtucClearStat_Type()
)
pgAdslAtucClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAdslAtucClearStat.setStatus("current")


class _PgAdslAturClearStat_Type(Integer32):
    """Custom type pgAdslAturClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PgAdslAturClearStat_Type.__name__ = "Integer32"
_PgAdslAturClearStat_Object = MibTableColumn
pgAdslAturClearStat = _PgAdslAturClearStat_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 15, 1, 1, 1, 2),
    _PgAdslAturClearStat_Type()
)
pgAdslAturClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAdslAturClearStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-ADSL-MIB",
    **{"pgAdslMIB": pgAdslMIB,
       "pgAdslMIBObjects": pgAdslMIBObjects,
       "pgAdslClearStatTable": pgAdslClearStatTable,
       "pgAdslClearStatEntry": pgAdslClearStatEntry,
       "pgAdslAtucClearStat": pgAdslAtucClearStat,
       "pgAdslAturClearStat": pgAdslAturClearStat}
)
