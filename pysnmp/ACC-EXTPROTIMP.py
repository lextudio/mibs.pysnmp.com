# SNMP MIB module (ACC-EXTPROTIMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-EXTPROTIMP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:12 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccExtProtImp_ObjectIdentity = ObjectIdentity
accExtProtImp = _AccExtProtImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35)
)
_AccExtProtImpTable_Object = MibTable
accExtProtImpTable = _AccExtProtImpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    accExtProtImpTable.setStatus("mandatory")
_AccExtProtImpEntry_Object = MibTableRow
accExtProtImpEntry = _AccExtProtImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1)
)
accExtProtImpEntry.setIndexNames(
    (0, "ACC-EXTPROTIMP", "accExtProtImpProtocol"),
)
if mibBuilder.loadTexts:
    accExtProtImpEntry.setStatus("mandatory")


class _AccExtProtImpProtocol_Type(Integer32):
    """Custom type accExtProtImpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("rip", 1),
          ("static", 3))
    )


_AccExtProtImpProtocol_Type.__name__ = "Integer32"
_AccExtProtImpProtocol_Object = MibTableColumn
accExtProtImpProtocol = _AccExtProtImpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1, 1),
    _AccExtProtImpProtocol_Type()
)
accExtProtImpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accExtProtImpProtocol.setStatus("mandatory")


class _AccExtProtImpAllowed_Type(Integer32):
    """Custom type accExtProtImpAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccExtProtImpAllowed_Type.__name__ = "Integer32"
_AccExtProtImpAllowed_Object = MibTableColumn
accExtProtImpAllowed = _AccExtProtImpAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1, 2),
    _AccExtProtImpAllowed_Type()
)
accExtProtImpAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accExtProtImpAllowed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-EXTPROTIMP",
    **{"accExtProtImp": accExtProtImp,
       "accExtProtImpTable": accExtProtImpTable,
       "accExtProtImpEntry": accExtProtImpEntry,
       "accExtProtImpProtocol": accExtProtImpProtocol,
       "accExtProtImpAllowed": accExtProtImpAllowed}
)
