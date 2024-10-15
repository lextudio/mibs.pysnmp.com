# SNMP MIB module (CYAN-AUG64-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-AUG64-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:03 2024
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
 CyanAugStructureTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanAugStructureTc",
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

cyanAUG64Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240)
)
cyanAUG64Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanAUG64MibObjects_ObjectIdentity = ObjectIdentity
cyanAUG64MibObjects = _CyanAUG64MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1)
)
_CyanAUG64Table_Object = MibTable
cyanAUG64Table = _CyanAUG64Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1)
)
if mibBuilder.loadTexts:
    cyanAUG64Table.setStatus("current")
_CyanAUG64Entry_Object = MibTableRow
cyanAUG64Entry = _CyanAUG64Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1)
)
cyanAUG64Entry.setIndexNames(
    (0, "CYAN-AUG64-MIB", "cyanAUG64ShelfId"),
    (0, "CYAN-AUG64-MIB", "cyanAUG64ModuleId"),
    (0, "CYAN-AUG64-MIB", "cyanAUG64AUG64Id"),
)
if mibBuilder.loadTexts:
    cyanAUG64Entry.setStatus("current")


class _CyanAUG64ShelfId_Type(Unsigned32):
    """Custom type cyanAUG64ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanAUG64ShelfId_Type.__name__ = "Unsigned32"
_CyanAUG64ShelfId_Object = MibTableColumn
cyanAUG64ShelfId = _CyanAUG64ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 1),
    _CyanAUG64ShelfId_Type()
)
cyanAUG64ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanAUG64ShelfId.setStatus("current")
_CyanAUG64ModuleId_Type = Unsigned32
_CyanAUG64ModuleId_Object = MibTableColumn
cyanAUG64ModuleId = _CyanAUG64ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 2),
    _CyanAUG64ModuleId_Type()
)
cyanAUG64ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanAUG64ModuleId.setStatus("current")
_CyanAUG64AUG64Id_Type = Unsigned32
_CyanAUG64AUG64Id_Object = MibTableColumn
cyanAUG64AUG64Id = _CyanAUG64AUG64Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 3),
    _CyanAUG64AUG64Id_Type()
)
cyanAUG64AUG64Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanAUG64AUG64Id.setStatus("current")
_CyanAUG64AdminState_Type = CyanAdminStateTc
_CyanAUG64AdminState_Object = MibTableColumn
cyanAUG64AdminState = _CyanAUG64AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 4),
    _CyanAUG64AdminState_Type()
)
cyanAUG64AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64AdminState.setStatus("current")
_CyanAUG64AutoinserviceSoakTimeSec_Type = Integer32
_CyanAUG64AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanAUG64AutoinserviceSoakTimeSec = _CyanAUG64AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 5),
    _CyanAUG64AutoinserviceSoakTimeSec_Type()
)
cyanAUG64AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64AutoinserviceSoakTimeSec.setStatus("current")


class _CyanAUG64Description_Type(DisplayString):
    """Custom type cyanAUG64Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanAUG64Description_Type.__name__ = "DisplayString"
_CyanAUG64Description_Object = MibTableColumn
cyanAUG64Description = _CyanAUG64Description_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 6),
    _CyanAUG64Description_Type()
)
cyanAUG64Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64Description.setStatus("current")
_CyanAUG64OperState_Type = CyanOpStateTc
_CyanAUG64OperState_Object = MibTableColumn
cyanAUG64OperState = _CyanAUG64OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 7),
    _CyanAUG64OperState_Type()
)
cyanAUG64OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64OperState.setStatus("current")
_CyanAUG64OperStateQual_Type = CyanOpStateQualTc
_CyanAUG64OperStateQual_Object = MibTableColumn
cyanAUG64OperStateQual = _CyanAUG64OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 8),
    _CyanAUG64OperStateQual_Type()
)
cyanAUG64OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64OperStateQual.setStatus("current")
_CyanAUG64SecServState_Type = CyanSecServiceStateTc
_CyanAUG64SecServState_Object = MibTableColumn
cyanAUG64SecServState = _CyanAUG64SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 9),
    _CyanAUG64SecServState_Type()
)
cyanAUG64SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64SecServState.setStatus("current")
_CyanAUG64StsaugStructure_Type = CyanAugStructureTc
_CyanAUG64StsaugStructure_Object = MibTableColumn
cyanAUG64StsaugStructure = _CyanAUG64StsaugStructure_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 10),
    _CyanAUG64StsaugStructure_Type()
)
cyanAUG64StsaugStructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAUG64StsaugStructure.setStatus("current")

# Managed Objects groups

cyanAUG64ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 20)
)
cyanAUG64ObjectGroup.setObjects(
      *(("CYAN-AUG64-MIB", "cyanAUG64AdminState"),
        ("CYAN-AUG64-MIB", "cyanAUG64AutoinserviceSoakTimeSec"),
        ("CYAN-AUG64-MIB", "cyanAUG64Description"),
        ("CYAN-AUG64-MIB", "cyanAUG64OperState"),
        ("CYAN-AUG64-MIB", "cyanAUG64OperStateQual"),
        ("CYAN-AUG64-MIB", "cyanAUG64SecServState"),
        ("CYAN-AUG64-MIB", "cyanAUG64StsaugStructure"))
)
if mibBuilder.loadTexts:
    cyanAUG64ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanAUG64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 30)
)
if mibBuilder.loadTexts:
    cyanAUG64Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-AUG64-MIB",
    **{"cyanAUG64Module": cyanAUG64Module,
       "cyanAUG64MibObjects": cyanAUG64MibObjects,
       "cyanAUG64Table": cyanAUG64Table,
       "cyanAUG64Entry": cyanAUG64Entry,
       "cyanAUG64ShelfId": cyanAUG64ShelfId,
       "cyanAUG64ModuleId": cyanAUG64ModuleId,
       "cyanAUG64AUG64Id": cyanAUG64AUG64Id,
       "cyanAUG64AdminState": cyanAUG64AdminState,
       "cyanAUG64AutoinserviceSoakTimeSec": cyanAUG64AutoinserviceSoakTimeSec,
       "cyanAUG64Description": cyanAUG64Description,
       "cyanAUG64OperState": cyanAUG64OperState,
       "cyanAUG64OperStateQual": cyanAUG64OperStateQual,
       "cyanAUG64SecServState": cyanAUG64SecServState,
       "cyanAUG64StsaugStructure": cyanAUG64StsaugStructure,
       "cyanAUG64ObjectGroup": cyanAUG64ObjectGroup,
       "cyanAUG64Compliance": cyanAUG64Compliance}
)
