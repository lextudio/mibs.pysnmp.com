# SNMP MIB module (CYAN-S64-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-S64-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:16 2024
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
 CyanNimTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSdhSnSignalLabelTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanNimTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSdhSnSignalLabelTc",
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

cyanS64Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250)
)
cyanS64Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanS64MibObjects_ObjectIdentity = ObjectIdentity
cyanS64MibObjects = _CyanS64MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1)
)
_CyanS64Table_Object = MibTable
cyanS64Table = _CyanS64Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1)
)
if mibBuilder.loadTexts:
    cyanS64Table.setStatus("current")
_CyanS64Entry_Object = MibTableRow
cyanS64Entry = _CyanS64Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1)
)
cyanS64Entry.setIndexNames(
    (0, "CYAN-S64-MIB", "cyanS64ShelfId"),
    (0, "CYAN-S64-MIB", "cyanS64ModuleId"),
    (0, "CYAN-S64-MIB", "cyanS64S64Id"),
)
if mibBuilder.loadTexts:
    cyanS64Entry.setStatus("current")


class _CyanS64ShelfId_Type(Unsigned32):
    """Custom type cyanS64ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanS64ShelfId_Type.__name__ = "Unsigned32"
_CyanS64ShelfId_Object = MibTableColumn
cyanS64ShelfId = _CyanS64ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 1),
    _CyanS64ShelfId_Type()
)
cyanS64ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanS64ShelfId.setStatus("current")
_CyanS64ModuleId_Type = Unsigned32
_CyanS64ModuleId_Object = MibTableColumn
cyanS64ModuleId = _CyanS64ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 2),
    _CyanS64ModuleId_Type()
)
cyanS64ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanS64ModuleId.setStatus("current")
_CyanS64S64Id_Type = Unsigned32
_CyanS64S64Id_Object = MibTableColumn
cyanS64S64Id = _CyanS64S64Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 3),
    _CyanS64S64Id_Type()
)
cyanS64S64Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanS64S64Id.setStatus("current")
_CyanS64Accepted_Type = CyanSdhSnSignalLabelTc
_CyanS64Accepted_Object = MibTableColumn
cyanS64Accepted = _CyanS64Accepted_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 4),
    _CyanS64Accepted_Type()
)
cyanS64Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64Accepted.setStatus("current")
_CyanS64AdminState_Type = CyanAdminStateTc
_CyanS64AdminState_Object = MibTableColumn
cyanS64AdminState = _CyanS64AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 5),
    _CyanS64AdminState_Type()
)
cyanS64AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64AdminState.setStatus("current")
_CyanS64AutoinserviceSoakTimeSec_Type = Integer32
_CyanS64AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanS64AutoinserviceSoakTimeSec = _CyanS64AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 6),
    _CyanS64AutoinserviceSoakTimeSec_Type()
)
cyanS64AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64AutoinserviceSoakTimeSec.setStatus("current")


class _CyanS64Description_Type(DisplayString):
    """Custom type cyanS64Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanS64Description_Type.__name__ = "DisplayString"
_CyanS64Description_Object = MibTableColumn
cyanS64Description = _CyanS64Description_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 7),
    _CyanS64Description_Type()
)
cyanS64Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64Description.setStatus("current")
_CyanS64Expected_Type = CyanSdhSnSignalLabelTc
_CyanS64Expected_Object = MibTableColumn
cyanS64Expected = _CyanS64Expected_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 8),
    _CyanS64Expected_Type()
)
cyanS64Expected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64Expected.setStatus("current")
_CyanS64Inserted_Type = CyanSdhSnSignalLabelTc
_CyanS64Inserted_Object = MibTableColumn
cyanS64Inserted = _CyanS64Inserted_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 9),
    _CyanS64Inserted_Type()
)
cyanS64Inserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64Inserted.setStatus("current")
_CyanS64Monitorterminate_Type = CyanNimTc
_CyanS64Monitorterminate_Object = MibTableColumn
cyanS64Monitorterminate = _CyanS64Monitorterminate_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 10),
    _CyanS64Monitorterminate_Type()
)
cyanS64Monitorterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64Monitorterminate.setStatus("current")
_CyanS64OperState_Type = CyanOpStateTc
_CyanS64OperState_Object = MibTableColumn
cyanS64OperState = _CyanS64OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 11),
    _CyanS64OperState_Type()
)
cyanS64OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64OperState.setStatus("current")
_CyanS64OperStateQual_Type = CyanOpStateQualTc
_CyanS64OperStateQual_Object = MibTableColumn
cyanS64OperStateQual = _CyanS64OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 12),
    _CyanS64OperStateQual_Type()
)
cyanS64OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64OperStateQual.setStatus("current")
_CyanS64SecServState_Type = CyanSecServiceStateTc
_CyanS64SecServState_Object = MibTableColumn
cyanS64SecServState = _CyanS64SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 1, 1, 1, 13),
    _CyanS64SecServState_Type()
)
cyanS64SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanS64SecServState.setStatus("current")

# Managed Objects groups

cyanS64ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 20)
)
cyanS64ObjectGroup.setObjects(
      *(("CYAN-S64-MIB", "cyanS64Accepted"),
        ("CYAN-S64-MIB", "cyanS64AdminState"),
        ("CYAN-S64-MIB", "cyanS64AutoinserviceSoakTimeSec"),
        ("CYAN-S64-MIB", "cyanS64Description"),
        ("CYAN-S64-MIB", "cyanS64Expected"),
        ("CYAN-S64-MIB", "cyanS64Inserted"),
        ("CYAN-S64-MIB", "cyanS64Monitorterminate"),
        ("CYAN-S64-MIB", "cyanS64OperState"),
        ("CYAN-S64-MIB", "cyanS64OperStateQual"),
        ("CYAN-S64-MIB", "cyanS64SecServState"))
)
if mibBuilder.loadTexts:
    cyanS64ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanS64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 250, 30)
)
if mibBuilder.loadTexts:
    cyanS64Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-S64-MIB",
    **{"cyanS64Module": cyanS64Module,
       "cyanS64MibObjects": cyanS64MibObjects,
       "cyanS64Table": cyanS64Table,
       "cyanS64Entry": cyanS64Entry,
       "cyanS64ShelfId": cyanS64ShelfId,
       "cyanS64ModuleId": cyanS64ModuleId,
       "cyanS64S64Id": cyanS64S64Id,
       "cyanS64Accepted": cyanS64Accepted,
       "cyanS64AdminState": cyanS64AdminState,
       "cyanS64AutoinserviceSoakTimeSec": cyanS64AutoinserviceSoakTimeSec,
       "cyanS64Description": cyanS64Description,
       "cyanS64Expected": cyanS64Expected,
       "cyanS64Inserted": cyanS64Inserted,
       "cyanS64Monitorterminate": cyanS64Monitorterminate,
       "cyanS64OperState": cyanS64OperState,
       "cyanS64OperStateQual": cyanS64OperStateQual,
       "cyanS64SecServState": cyanS64SecServState,
       "cyanS64ObjectGroup": cyanS64ObjectGroup,
       "cyanS64Compliance": cyanS64Compliance}
)
