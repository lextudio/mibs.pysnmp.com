# SNMP MIB module (CYAN-MS64-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-MS64-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:10 2024
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
 CyanChannelIdTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc,
 CyanSsBitsTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanChannelIdTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc",
    "CyanSsBitsTc")

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

cyanMS64Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230)
)
cyanMS64Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanMS64MibObjects_ObjectIdentity = ObjectIdentity
cyanMS64MibObjects = _CyanMS64MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1)
)
_CyanMS64Table_Object = MibTable
cyanMS64Table = _CyanMS64Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1)
)
if mibBuilder.loadTexts:
    cyanMS64Table.setStatus("current")
_CyanMS64Entry_Object = MibTableRow
cyanMS64Entry = _CyanMS64Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1)
)
cyanMS64Entry.setIndexNames(
    (0, "CYAN-MS64-MIB", "cyanMS64ShelfId"),
    (0, "CYAN-MS64-MIB", "cyanMS64ModuleId"),
    (0, "CYAN-MS64-MIB", "cyanMS64MS64Id"),
)
if mibBuilder.loadTexts:
    cyanMS64Entry.setStatus("current")


class _CyanMS64ShelfId_Type(Unsigned32):
    """Custom type cyanMS64ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanMS64ShelfId_Type.__name__ = "Unsigned32"
_CyanMS64ShelfId_Object = MibTableColumn
cyanMS64ShelfId = _CyanMS64ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 1),
    _CyanMS64ShelfId_Type()
)
cyanMS64ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanMS64ShelfId.setStatus("current")
_CyanMS64ModuleId_Type = Unsigned32
_CyanMS64ModuleId_Object = MibTableColumn
cyanMS64ModuleId = _CyanMS64ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 2),
    _CyanMS64ModuleId_Type()
)
cyanMS64ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanMS64ModuleId.setStatus("current")
_CyanMS64MS64Id_Type = Unsigned32
_CyanMS64MS64Id_Object = MibTableColumn
cyanMS64MS64Id = _CyanMS64MS64Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 3),
    _CyanMS64MS64Id_Type()
)
cyanMS64MS64Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanMS64MS64Id.setStatus("current")
_CyanMS64Accepted_Type = CyanSsBitsTc
_CyanMS64Accepted_Object = MibTableColumn
cyanMS64Accepted = _CyanMS64Accepted_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 4),
    _CyanMS64Accepted_Type()
)
cyanMS64Accepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64Accepted.setStatus("current")
_CyanMS64AdminState_Type = CyanAdminStateTc
_CyanMS64AdminState_Object = MibTableColumn
cyanMS64AdminState = _CyanMS64AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 5),
    _CyanMS64AdminState_Type()
)
cyanMS64AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64AdminState.setStatus("current")
_CyanMS64AutoinserviceSoakTimeSec_Type = Integer32
_CyanMS64AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanMS64AutoinserviceSoakTimeSec = _CyanMS64AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 6),
    _CyanMS64AutoinserviceSoakTimeSec_Type()
)
cyanMS64AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64AutoinserviceSoakTimeSec.setStatus("current")
_CyanMS64ChannelId_Type = CyanChannelIdTc
_CyanMS64ChannelId_Object = MibTableColumn
cyanMS64ChannelId = _CyanMS64ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 7),
    _CyanMS64ChannelId_Type()
)
cyanMS64ChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64ChannelId.setStatus("current")
_CyanMS64Inserted_Type = CyanSsBitsTc
_CyanMS64Inserted_Object = MibTableColumn
cyanMS64Inserted = _CyanMS64Inserted_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 8),
    _CyanMS64Inserted_Type()
)
cyanMS64Inserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64Inserted.setStatus("current")
_CyanMS64OperState_Type = CyanOpStateTc
_CyanMS64OperState_Object = MibTableColumn
cyanMS64OperState = _CyanMS64OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 9),
    _CyanMS64OperState_Type()
)
cyanMS64OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64OperState.setStatus("current")
_CyanMS64OperStateQual_Type = CyanOpStateQualTc
_CyanMS64OperStateQual_Object = MibTableColumn
cyanMS64OperStateQual = _CyanMS64OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 10),
    _CyanMS64OperStateQual_Type()
)
cyanMS64OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64OperStateQual.setStatus("current")
_CyanMS64SecServState_Type = CyanSecServiceStateTc
_CyanMS64SecServState_Object = MibTableColumn
cyanMS64SecServState = _CyanMS64SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 11),
    _CyanMS64SecServState_Type()
)
cyanMS64SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanMS64SecServState.setStatus("current")

# Managed Objects groups

cyanMS64ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 20)
)
cyanMS64ObjectGroup.setObjects(
      *(("CYAN-MS64-MIB", "cyanMS64Accepted"),
        ("CYAN-MS64-MIB", "cyanMS64AdminState"),
        ("CYAN-MS64-MIB", "cyanMS64AutoinserviceSoakTimeSec"),
        ("CYAN-MS64-MIB", "cyanMS64ChannelId"),
        ("CYAN-MS64-MIB", "cyanMS64Inserted"),
        ("CYAN-MS64-MIB", "cyanMS64OperState"),
        ("CYAN-MS64-MIB", "cyanMS64OperStateQual"),
        ("CYAN-MS64-MIB", "cyanMS64SecServState"))
)
if mibBuilder.loadTexts:
    cyanMS64ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanMS64Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 30)
)
if mibBuilder.loadTexts:
    cyanMS64Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-MS64-MIB",
    **{"cyanMS64Module": cyanMS64Module,
       "cyanMS64MibObjects": cyanMS64MibObjects,
       "cyanMS64Table": cyanMS64Table,
       "cyanMS64Entry": cyanMS64Entry,
       "cyanMS64ShelfId": cyanMS64ShelfId,
       "cyanMS64ModuleId": cyanMS64ModuleId,
       "cyanMS64MS64Id": cyanMS64MS64Id,
       "cyanMS64Accepted": cyanMS64Accepted,
       "cyanMS64AdminState": cyanMS64AdminState,
       "cyanMS64AutoinserviceSoakTimeSec": cyanMS64AutoinserviceSoakTimeSec,
       "cyanMS64ChannelId": cyanMS64ChannelId,
       "cyanMS64Inserted": cyanMS64Inserted,
       "cyanMS64OperState": cyanMS64OperState,
       "cyanMS64OperStateQual": cyanMS64OperStateQual,
       "cyanMS64SecServState": cyanMS64SecServState,
       "cyanMS64ObjectGroup": cyanMS64ObjectGroup,
       "cyanMS64Compliance": cyanMS64Compliance}
)
