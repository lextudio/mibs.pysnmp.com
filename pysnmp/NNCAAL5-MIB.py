# SNMP MIB module (NNCAAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCAAL5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:15 2024
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncAAL5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncAAL5Objects_ObjectIdentity = ObjectIdentity
nncAAL5Objects = _NncAAL5Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1)
)
_NncAAL5Configuration_ObjectIdentity = ObjectIdentity
nncAAL5Configuration = _NncAAL5Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 1)
)
_NncAAL5Statistics_ObjectIdentity = ObjectIdentity
nncAAL5Statistics = _NncAAL5Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2)
)
_NncAAL5StatisticsTable_Object = MibTable
nncAAL5StatisticsTable = _NncAAL5StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nncAAL5StatisticsTable.setStatus("current")
_NncAAL5StatisticsEntry_Object = MibTableRow
nncAAL5StatisticsEntry = _NncAAL5StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1)
)
nncAAL5StatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncAAL5StatisticsEntry.setStatus("current")
_NncAAL5RxPDUs_Type = Counter32
_NncAAL5RxPDUs_Object = MibTableColumn
nncAAL5RxPDUs = _NncAAL5RxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 1),
    _NncAAL5RxPDUs_Type()
)
nncAAL5RxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5RxPDUs.setStatus("current")
_NncAAL5TxPDUs_Type = Counter32
_NncAAL5TxPDUs_Object = MibTableColumn
nncAAL5TxPDUs = _NncAAL5TxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 2),
    _NncAAL5TxPDUs_Type()
)
nncAAL5TxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5TxPDUs.setStatus("current")
_NncAAL5Crc32PDUErrors_Type = Counter32
_NncAAL5Crc32PDUErrors_Object = MibTableColumn
nncAAL5Crc32PDUErrors = _NncAAL5Crc32PDUErrors_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 3),
    _NncAAL5Crc32PDUErrors_Type()
)
nncAAL5Crc32PDUErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5Crc32PDUErrors.setStatus("current")
_NncAAL5InvalidFormatPDU_Type = Counter32
_NncAAL5InvalidFormatPDU_Object = MibTableColumn
nncAAL5InvalidFormatPDU = _NncAAL5InvalidFormatPDU_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 4),
    _NncAAL5InvalidFormatPDU_Type()
)
nncAAL5InvalidFormatPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5InvalidFormatPDU.setStatus("current")
_NncAAL5OversizedSDU_Type = Counter32
_NncAAL5OversizedSDU_Object = MibTableColumn
nncAAL5OversizedSDU = _NncAAL5OversizedSDU_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 5),
    _NncAAL5OversizedSDU_Type()
)
nncAAL5OversizedSDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5OversizedSDU.setStatus("current")
_NncAAL5InvalidFields_Type = Counter32
_NncAAL5InvalidFields_Object = MibTableColumn
nncAAL5InvalidFields = _NncAAL5InvalidFields_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 6),
    _NncAAL5InvalidFields_Type()
)
nncAAL5InvalidFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5InvalidFields.setStatus("current")
_NncAAL5ReassemblyTimerExpirations_Type = Counter32
_NncAAL5ReassemblyTimerExpirations_Object = MibTableColumn
nncAAL5ReassemblyTimerExpirations = _NncAAL5ReassemblyTimerExpirations_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 1, 2, 1, 1, 7),
    _NncAAL5ReassemblyTimerExpirations_Type()
)
nncAAL5ReassemblyTimerExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAAL5ReassemblyTimerExpirations.setStatus("current")
_NncAAL5Traps_ObjectIdentity = ObjectIdentity
nncAAL5Traps = _NncAAL5Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 2)
)
_NncAAL5Groups_ObjectIdentity = ObjectIdentity
nncAAL5Groups = _NncAAL5Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 3)
)
_NncAAL5Compliances_ObjectIdentity = ObjectIdentity
nncAAL5Compliances = _NncAAL5Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 4)
)

# Managed Objects groups

nncAAL5BasicStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 3, 1)
)
nncAAL5BasicStatisticsGroup.setObjects(
      *(("NNCAAL5-MIB", "nncAAL5RxPDUs"),
        ("NNCAAL5-MIB", "nncAAL5TxPDUs"),
        ("NNCAAL5-MIB", "nncAAL5Crc32PDUErrors"),
        ("NNCAAL5-MIB", "nncAAL5InvalidFormatPDU"),
        ("NNCAAL5-MIB", "nncAAL5OversizedSDU"),
        ("NNCAAL5-MIB", "nncAAL5InvalidFields"),
        ("NNCAAL5-MIB", "nncAAL5ReassemblyTimerExpirations"))
)
if mibBuilder.loadTexts:
    nncAAL5BasicStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncAAL5Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 71, 4, 1)
)
if mibBuilder.loadTexts:
    nncAAL5Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCAAL5-MIB",
    **{"nncAAL5": nncAAL5,
       "nncAAL5Objects": nncAAL5Objects,
       "nncAAL5Configuration": nncAAL5Configuration,
       "nncAAL5Statistics": nncAAL5Statistics,
       "nncAAL5StatisticsTable": nncAAL5StatisticsTable,
       "nncAAL5StatisticsEntry": nncAAL5StatisticsEntry,
       "nncAAL5RxPDUs": nncAAL5RxPDUs,
       "nncAAL5TxPDUs": nncAAL5TxPDUs,
       "nncAAL5Crc32PDUErrors": nncAAL5Crc32PDUErrors,
       "nncAAL5InvalidFormatPDU": nncAAL5InvalidFormatPDU,
       "nncAAL5OversizedSDU": nncAAL5OversizedSDU,
       "nncAAL5InvalidFields": nncAAL5InvalidFields,
       "nncAAL5ReassemblyTimerExpirations": nncAAL5ReassemblyTimerExpirations,
       "nncAAL5Traps": nncAAL5Traps,
       "nncAAL5Groups": nncAAL5Groups,
       "nncAAL5BasicStatisticsGroup": nncAAL5BasicStatisticsGroup,
       "nncAAL5Compliances": nncAAL5Compliances,
       "nncAAL5Compliance": nncAAL5Compliance}
)
