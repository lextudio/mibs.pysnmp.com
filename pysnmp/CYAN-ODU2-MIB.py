# SNMP MIB module (CYAN-ODU2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-ODU2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:11 2024
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
 CyanLayerRateTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanOpuPayloadTypeTc,
 CyanSecServiceStateTc,
 CyanTPConnectionStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanLayerRateTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanOpuPayloadTypeTc",
    "CyanSecServiceStateTc",
    "CyanTPConnectionStateTc")

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

cyanODU2Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200)
)
cyanODU2Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanODU2MibObjects_ObjectIdentity = ObjectIdentity
cyanODU2MibObjects = _CyanODU2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1)
)
_CyanODU2Table_Object = MibTable
cyanODU2Table = _CyanODU2Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1)
)
if mibBuilder.loadTexts:
    cyanODU2Table.setStatus("current")
_CyanODU2Entry_Object = MibTableRow
cyanODU2Entry = _CyanODU2Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1)
)
cyanODU2Entry.setIndexNames(
    (0, "CYAN-ODU2-MIB", "cyanODU2ShelfId"),
    (0, "CYAN-ODU2-MIB", "cyanODU2ModuleId"),
    (0, "CYAN-ODU2-MIB", "cyanODU2ODU2Id"),
)
if mibBuilder.loadTexts:
    cyanODU2Entry.setStatus("current")


class _CyanODU2ShelfId_Type(Unsigned32):
    """Custom type cyanODU2ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanODU2ShelfId_Type.__name__ = "Unsigned32"
_CyanODU2ShelfId_Object = MibTableColumn
cyanODU2ShelfId = _CyanODU2ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 1),
    _CyanODU2ShelfId_Type()
)
cyanODU2ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanODU2ShelfId.setStatus("current")
_CyanODU2ModuleId_Type = Unsigned32
_CyanODU2ModuleId_Object = MibTableColumn
cyanODU2ModuleId = _CyanODU2ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 2),
    _CyanODU2ModuleId_Type()
)
cyanODU2ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanODU2ModuleId.setStatus("current")
_CyanODU2ODU2Id_Type = Unsigned32
_CyanODU2ODU2Id_Object = MibTableColumn
cyanODU2ODU2Id = _CyanODU2ODU2Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 3),
    _CyanODU2ODU2Id_Type()
)
cyanODU2ODU2Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanODU2ODU2Id.setStatus("current")
_CyanODU2AcceptedPayloadType_Type = CyanOpuPayloadTypeTc
_CyanODU2AcceptedPayloadType_Object = MibTableColumn
cyanODU2AcceptedPayloadType = _CyanODU2AcceptedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 4),
    _CyanODU2AcceptedPayloadType_Type()
)
cyanODU2AcceptedPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2AcceptedPayloadType.setStatus("current")
_CyanODU2AdaptationType_Type = CyanOpuPayloadTypeTc
_CyanODU2AdaptationType_Object = MibTableColumn
cyanODU2AdaptationType = _CyanODU2AdaptationType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 5),
    _CyanODU2AdaptationType_Type()
)
cyanODU2AdaptationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2AdaptationType.setStatus("current")
_CyanODU2AdminState_Type = CyanAdminStateTc
_CyanODU2AdminState_Object = MibTableColumn
cyanODU2AdminState = _CyanODU2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 6),
    _CyanODU2AdminState_Type()
)
cyanODU2AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2AdminState.setStatus("current")
_CyanODU2AutoinserviceSoakTimeSec_Type = Integer32
_CyanODU2AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanODU2AutoinserviceSoakTimeSec = _CyanODU2AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 7),
    _CyanODU2AutoinserviceSoakTimeSec_Type()
)
cyanODU2AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2AutoinserviceSoakTimeSec.setStatus("current")
_CyanODU2ConnectionState_Type = CyanTPConnectionStateTc
_CyanODU2ConnectionState_Object = MibTableColumn
cyanODU2ConnectionState = _CyanODU2ConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 8),
    _CyanODU2ConnectionState_Type()
)
cyanODU2ConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2ConnectionState.setStatus("current")
_CyanODU2OperState_Type = CyanOpStateTc
_CyanODU2OperState_Object = MibTableColumn
cyanODU2OperState = _CyanODU2OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 9),
    _CyanODU2OperState_Type()
)
cyanODU2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2OperState.setStatus("current")
_CyanODU2OperStateQual_Type = CyanOpStateQualTc
_CyanODU2OperStateQual_Object = MibTableColumn
cyanODU2OperStateQual = _CyanODU2OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 10),
    _CyanODU2OperStateQual_Type()
)
cyanODU2OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2OperStateQual.setStatus("current")
_CyanODU2SecServState_Type = CyanSecServiceStateTc
_CyanODU2SecServState_Object = MibTableColumn
cyanODU2SecServState = _CyanODU2SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 11),
    _CyanODU2SecServState_Type()
)
cyanODU2SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2SecServState.setStatus("current")
_CyanODU2SupportedRates_Type = CyanLayerRateTc
_CyanODU2SupportedRates_Object = MibTableColumn
cyanODU2SupportedRates = _CyanODU2SupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 1, 1, 1, 12),
    _CyanODU2SupportedRates_Type()
)
cyanODU2SupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanODU2SupportedRates.setStatus("current")

# Managed Objects groups

cyanODU2ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 20)
)
cyanODU2ObjectGroup.setObjects(
      *(("CYAN-ODU2-MIB", "cyanODU2AcceptedPayloadType"),
        ("CYAN-ODU2-MIB", "cyanODU2AdaptationType"),
        ("CYAN-ODU2-MIB", "cyanODU2AdminState"),
        ("CYAN-ODU2-MIB", "cyanODU2AutoinserviceSoakTimeSec"),
        ("CYAN-ODU2-MIB", "cyanODU2ConnectionState"),
        ("CYAN-ODU2-MIB", "cyanODU2OperState"),
        ("CYAN-ODU2-MIB", "cyanODU2OperStateQual"),
        ("CYAN-ODU2-MIB", "cyanODU2SecServState"),
        ("CYAN-ODU2-MIB", "cyanODU2SupportedRates"))
)
if mibBuilder.loadTexts:
    cyanODU2ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanODU2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 200, 30)
)
if mibBuilder.loadTexts:
    cyanODU2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-ODU2-MIB",
    **{"cyanODU2Module": cyanODU2Module,
       "cyanODU2MibObjects": cyanODU2MibObjects,
       "cyanODU2Table": cyanODU2Table,
       "cyanODU2Entry": cyanODU2Entry,
       "cyanODU2ShelfId": cyanODU2ShelfId,
       "cyanODU2ModuleId": cyanODU2ModuleId,
       "cyanODU2ODU2Id": cyanODU2ODU2Id,
       "cyanODU2AcceptedPayloadType": cyanODU2AcceptedPayloadType,
       "cyanODU2AdaptationType": cyanODU2AdaptationType,
       "cyanODU2AdminState": cyanODU2AdminState,
       "cyanODU2AutoinserviceSoakTimeSec": cyanODU2AutoinserviceSoakTimeSec,
       "cyanODU2ConnectionState": cyanODU2ConnectionState,
       "cyanODU2OperState": cyanODU2OperState,
       "cyanODU2OperStateQual": cyanODU2OperStateQual,
       "cyanODU2SecServState": cyanODU2SecServState,
       "cyanODU2SupportedRates": cyanODU2SupportedRates,
       "cyanODU2ObjectGroup": cyanODU2ObjectGroup,
       "cyanODU2Compliance": cyanODU2Compliance}
)
