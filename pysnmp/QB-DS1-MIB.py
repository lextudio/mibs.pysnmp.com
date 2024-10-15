# SNMP MIB module (QB-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:41 2024
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

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

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

qbDs1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QbDs1Objects_ObjectIdentity = ObjectIdentity
qbDs1Objects = _QbDs1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 1)
)
_QbDs1Tables_ObjectIdentity = ObjectIdentity
qbDs1Tables = _QbDs1Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2)
)
_QbDsx1ConfigTable_Object = MibTable
qbDsx1ConfigTable = _QbDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    qbDsx1ConfigTable.setStatus("current")
_QbDsx1ConfigEntry_Object = MibTableRow
qbDsx1ConfigEntry = _QbDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qbDsx1ConfigEntry.setStatus("current")


class _Qbdsx1ClockMode_Type(Integer32):
    """Custom type qbdsx1ClockMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("srts", 2))
    )


_Qbdsx1ClockMode_Type.__name__ = "Integer32"
_Qbdsx1ClockMode_Object = MibTableColumn
qbdsx1ClockMode = _Qbdsx1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1, 1, 1),
    _Qbdsx1ClockMode_Type()
)
qbdsx1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbdsx1ClockMode.setStatus("current")
_QbDsx1StatTable_Object = MibTable
qbDsx1StatTable = _QbDsx1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2)
)
if mibBuilder.loadTexts:
    qbDsx1StatTable.setStatus("current")
_QbDsx1StatEnry_Object = MibTableRow
qbDsx1StatEnry = _QbDsx1StatEnry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2, 1)
)
qbDsx1StatEnry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbDsx1StatEnry.setStatus("current")
_QbDsx1StatBPVs_Type = Counter32
_QbDsx1StatBPVs_Object = MibTableColumn
qbDsx1StatBPVs = _QbDsx1StatBPVs_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2, 1, 1),
    _QbDsx1StatBPVs_Type()
)
qbDsx1StatBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDsx1StatBPVs.setStatus("current")
_QbDs1Conformance_ObjectIdentity = ObjectIdentity
qbDs1Conformance = _QbDs1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 3)
)
_QbDs1Compliances_ObjectIdentity = ObjectIdentity
qbDs1Compliances = _QbDs1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 1)
)
_QbDs1Groups_ObjectIdentity = ObjectIdentity
qbDs1Groups = _QbDs1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("QB-DS1-MIB",
     "qbDsx1ConfigEntry")
)
qbDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

qbDs1AllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 2, 1)
)
qbDs1AllGroup.setObjects(
    ("QB-DS1-MIB", "qbdsx1ClockMode")
)
if mibBuilder.loadTexts:
    qbDs1AllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbDs1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbDs1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-DS1-MIB",
    **{"qbDs1MIB": qbDs1MIB,
       "qbDs1Objects": qbDs1Objects,
       "qbDs1Tables": qbDs1Tables,
       "qbDsx1ConfigTable": qbDsx1ConfigTable,
       "qbDsx1ConfigEntry": qbDsx1ConfigEntry,
       "qbdsx1ClockMode": qbdsx1ClockMode,
       "qbDsx1StatTable": qbDsx1StatTable,
       "qbDsx1StatEnry": qbDsx1StatEnry,
       "qbDsx1StatBPVs": qbDsx1StatBPVs,
       "qbDs1Conformance": qbDs1Conformance,
       "qbDs1Compliances": qbDs1Compliances,
       "qbDs1Compliance": qbDs1Compliance,
       "qbDs1Groups": qbDs1Groups,
       "qbDs1AllGroup": qbDs1AllGroup}
)
