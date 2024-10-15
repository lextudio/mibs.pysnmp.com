# SNMP MIB module (ZIPLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZIPLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:48 2024
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

(ctResource,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctResource")

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

_CtZiplock_ObjectIdentity = ObjectIdentity
ctZiplock = _CtZiplock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3)
)
_CtZiplockTable_Object = MibTable
ctZiplockTable = _CtZiplockTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ctZiplockTable.setStatus("mandatory")
_CtZiplockEntry_Object = MibTableRow
ctZiplockEntry = _CtZiplockEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1)
)
ctZiplockEntry.setIndexNames(
    (0, "ZIPLOCK-MIB", "ctZiplockNumber"),
)
if mibBuilder.loadTexts:
    ctZiplockEntry.setStatus("mandatory")
_CtZiplockNumber_Type = Integer32
_CtZiplockNumber_Object = MibTableColumn
ctZiplockNumber = _CtZiplockNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 1),
    _CtZiplockNumber_Type()
)
ctZiplockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctZiplockNumber.setStatus("mandatory")
_CtZiplockPresence_Type = Integer32
_CtZiplockPresence_Object = MibTableColumn
ctZiplockPresence = _CtZiplockPresence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 2),
    _CtZiplockPresence_Type()
)
ctZiplockPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctZiplockPresence.setStatus("mandatory")
_CtZiplockRevision_Type = Integer32
_CtZiplockRevision_Object = MibTableColumn
ctZiplockRevision = _CtZiplockRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 3),
    _CtZiplockRevision_Type()
)
ctZiplockRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctZiplockRevision.setStatus("mandatory")
_CtZiplockStatus_Type = Integer32
_CtZiplockStatus_Object = MibTableColumn
ctZiplockStatus = _CtZiplockStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 4),
    _CtZiplockStatus_Type()
)
ctZiplockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctZiplockStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZIPLOCK-MIB",
    **{"ctZiplock": ctZiplock,
       "ctZiplockTable": ctZiplockTable,
       "ctZiplockEntry": ctZiplockEntry,
       "ctZiplockNumber": ctZiplockNumber,
       "ctZiplockPresence": ctZiplockPresence,
       "ctZiplockRevision": ctZiplockRevision,
       "ctZiplockStatus": ctZiplockStatus}
)
