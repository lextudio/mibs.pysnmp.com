# SNMP MIB module (CYAN-RS64-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-RS64-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:15 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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

cyanRS64Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220)
)
cyanRS64Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanRS64MibObjects_ObjectIdentity = ObjectIdentity
cyanRS64MibObjects = _CyanRS64MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1)
)
_CyanRS64Table_Object = MibTable
cyanRS64Table = _CyanRS64Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1)
)
if mibBuilder.loadTexts:
    cyanRS64Table.setStatus("current")
_CyanRS64Entry_Object = MibTableRow
cyanRS64Entry = _CyanRS64Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1)
)
cyanRS64Entry.setIndexNames(
    (0, "CYAN-RS64-MIB", "cyanRS64ShelfId"),
    (0, "CYAN-RS64-MIB", "cyanRS64ModuleId"),
    (0, "CYAN-RS64-MIB", "cyanRS64RS64Id"),
)
if mibBuilder.loadTexts:
    cyanRS64Entry.setStatus("current")


class _CyanRS64ShelfId_Type(Unsigned32):
    """Custom type cyanRS64ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanRS64ShelfId_Type.__name__ = "Unsigned32"
_CyanRS64ShelfId_Object = MibTableColumn
cyanRS64ShelfId = _CyanRS64ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 1),
    _CyanRS64ShelfId_Type()
)
cyanRS64ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanRS64ShelfId.setStatus("current")
_CyanRS64ModuleId_Type = Unsigned32
_CyanRS64ModuleId_Object = MibTableColumn
cyanRS64ModuleId = _CyanRS64ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 2),
    _CyanRS64ModuleId_Type()
)
cyanRS64ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanRS64ModuleId.setStatus("current")
_CyanRS64RS64Id_Type = Unsigned32
_CyanRS64RS64Id_Object = MibTableColumn
cyanRS64RS64Id = _CyanRS64RS64Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 3),
    _CyanRS64RS64Id_Type()
)
cyanRS64RS64Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanRS64RS64Id.setStatus("current")
_CyanRS64AdminState_Type = CyanAdminStateTc
_CyanRS64AdminState_Object = MibTableColumn
cyanRS64AdminState = _CyanRS64AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 4),
    _CyanRS64AdminState_Type()
)
cyanRS64AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRS64AdminState.setStatus("current")
_CyanRS64AutoinserviceSoakTimeSec_Type = Integer32
_CyanRS64AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanRS64AutoinserviceSoakTimeSec = _CyanRS64AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 5),
    _CyanRS64AutoinserviceSoakTimeSec_Type()
)
cyanRS64AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRS64AutoinserviceSoakTimeSec.setStatus("current")
_CyanRS64OperState_Type = CyanOpStateTc
_CyanRS64OperState_Object = MibTableColumn
cyanRS64OperState = _CyanRS64OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 6),
    _CyanRS64OperState_Type()
)
cyanRS64OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRS64OperState.setStatus("current")
_CyanRS64OperStateQual_Type = CyanOpStateQualTc
_CyanRS64OperStateQual_Object = MibTableColumn
cyanRS64OperStateQual = _CyanRS64OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 7),
    _CyanRS64OperStateQual_Type()
)
cyanRS64OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRS64OperStateQual.setStatus("current")
_CyanRS64SecServState_Type = CyanSecServiceStateTc
_CyanRS64SecServState_Object = MibTableColumn
cyanRS64SecServState = _CyanRS64SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 8),
    _CyanRS64SecServState_Type()
)
cyanRS64SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanRS64SecServState.setStatus("current")

# Managed Objects groups

cyanRS64ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 20)
)
cyanRS64ObjectGroup.setObjects(
      *(("CYAN-RS64-MIB", "cyanRS64AdminState"),
        ("CYAN-RS64-MIB", "cyanRS64AutoinserviceSoakTimeSec"),
        ("CYAN-RS64-MIB", "cyanRS64OperState"),
        ("CYAN-RS64-MIB", "cyanRS64OperStateQual"),
        ("CYAN-RS64-MIB", "cyanRS64SecServState"))
)
if mibBuilder.loadTexts:
    cyanRS64ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanRS64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 30)
)
if mibBuilder.loadTexts:
    cyanRS64Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-RS64-MIB",
    **{"cyanRS64Module": cyanRS64Module,
       "cyanRS64MibObjects": cyanRS64MibObjects,
       "cyanRS64Table": cyanRS64Table,
       "cyanRS64Entry": cyanRS64Entry,
       "cyanRS64ShelfId": cyanRS64ShelfId,
       "cyanRS64ModuleId": cyanRS64ModuleId,
       "cyanRS64RS64Id": cyanRS64RS64Id,
       "cyanRS64AdminState": cyanRS64AdminState,
       "cyanRS64AutoinserviceSoakTimeSec": cyanRS64AutoinserviceSoakTimeSec,
       "cyanRS64OperState": cyanRS64OperState,
       "cyanRS64OperStateQual": cyanRS64OperStateQual,
       "cyanRS64SecServState": cyanRS64SecServState,
       "cyanRS64ObjectGroup": cyanRS64ObjectGroup,
       "cyanRS64Compliance": cyanRS64Compliance}
)
