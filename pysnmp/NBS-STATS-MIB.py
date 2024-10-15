# SNMP MIB module (NBS-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:02 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 233)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsStatInfoGrp_ObjectIdentity = ObjectIdentity
nbsStatInfoGrp = _NbsStatInfoGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 233, 1)
)
if mibBuilder.loadTexts:
    nbsStatInfoGrp.setStatus("current")
_NbsStatInfoTable_Object = MibTable
nbsStatInfoTable = _NbsStatInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 233, 1, 10)
)
if mibBuilder.loadTexts:
    nbsStatInfoTable.setStatus("current")
_NbsStatInfoEntry_Object = MibTableRow
nbsStatInfoEntry = _NbsStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1)
)
nbsStatInfoEntry.setIndexNames(
    (0, "NBS-STATS-MIB", "nbsStatInfoIndex"),
)
if mibBuilder.loadTexts:
    nbsStatInfoEntry.setStatus("current")
_NbsStatInfoIndex_Type = InterfaceIndex
_NbsStatInfoIndex_Object = MibTableColumn
nbsStatInfoIndex = _NbsStatInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 1),
    _NbsStatInfoIndex_Type()
)
nbsStatInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStatInfoIndex.setStatus("current")


class _NbsStatInfoCounters_Type(Integer32):
    """Custom type nbsStatInfoCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsStatInfoCounters_Type.__name__ = "Integer32"
_NbsStatInfoCounters_Object = MibTableColumn
nbsStatInfoCounters = _NbsStatInfoCounters_Object(
    (1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 2),
    _NbsStatInfoCounters_Type()
)
nbsStatInfoCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsStatInfoCounters.setStatus("current")


class _NbsStatInfoPmData_Type(Integer32):
    """Custom type nbsStatInfoPmData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsStatInfoPmData_Type.__name__ = "Integer32"
_NbsStatInfoPmData_Object = MibTableColumn
nbsStatInfoPmData = _NbsStatInfoPmData_Object(
    (1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 3),
    _NbsStatInfoPmData_Type()
)
nbsStatInfoPmData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsStatInfoPmData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-STATS-MIB",
    **{"nbsStatsMib": nbsStatsMib,
       "nbsStatInfoGrp": nbsStatInfoGrp,
       "nbsStatInfoTable": nbsStatInfoTable,
       "nbsStatInfoEntry": nbsStatInfoEntry,
       "nbsStatInfoIndex": nbsStatInfoIndex,
       "nbsStatInfoCounters": nbsStatInfoCounters,
       "nbsStatInfoPmData": nbsStatInfoPmData}
)
