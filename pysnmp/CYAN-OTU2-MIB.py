# SNMP MIB module (CYAN-OTU2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-OTU2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:12 2024
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
 CyanEnDisabledTc,
 CyanFecModeTc,
 CyanLayerRateTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanFecModeTc",
    "CyanLayerRateTc",
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

cyanOTU2Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190)
)
cyanOTU2Module.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanOTU2MibObjects_ObjectIdentity = ObjectIdentity
cyanOTU2MibObjects = _CyanOTU2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1)
)
_CyanOTU2Table_Object = MibTable
cyanOTU2Table = _CyanOTU2Table_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1)
)
if mibBuilder.loadTexts:
    cyanOTU2Table.setStatus("current")
_CyanOTU2Entry_Object = MibTableRow
cyanOTU2Entry = _CyanOTU2Entry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1)
)
cyanOTU2Entry.setIndexNames(
    (0, "CYAN-OTU2-MIB", "cyanOTU2ShelfId"),
    (0, "CYAN-OTU2-MIB", "cyanOTU2ModuleId"),
    (0, "CYAN-OTU2-MIB", "cyanOTU2OTU2Id"),
)
if mibBuilder.loadTexts:
    cyanOTU2Entry.setStatus("current")


class _CyanOTU2ShelfId_Type(Unsigned32):
    """Custom type cyanOTU2ShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanOTU2ShelfId_Type.__name__ = "Unsigned32"
_CyanOTU2ShelfId_Object = MibTableColumn
cyanOTU2ShelfId = _CyanOTU2ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 1),
    _CyanOTU2ShelfId_Type()
)
cyanOTU2ShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanOTU2ShelfId.setStatus("current")
_CyanOTU2ModuleId_Type = Unsigned32
_CyanOTU2ModuleId_Object = MibTableColumn
cyanOTU2ModuleId = _CyanOTU2ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 2),
    _CyanOTU2ModuleId_Type()
)
cyanOTU2ModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanOTU2ModuleId.setStatus("current")
_CyanOTU2OTU2Id_Type = Unsigned32
_CyanOTU2OTU2Id_Object = MibTableColumn
cyanOTU2OTU2Id = _CyanOTU2OTU2Id_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 3),
    _CyanOTU2OTU2Id_Type()
)
cyanOTU2OTU2Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanOTU2OTU2Id.setStatus("current")
_CyanOTU2AdminState_Type = CyanAdminStateTc
_CyanOTU2AdminState_Object = MibTableColumn
cyanOTU2AdminState = _CyanOTU2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 4),
    _CyanOTU2AdminState_Type()
)
cyanOTU2AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2AdminState.setStatus("current")
_CyanOTU2AutoinserviceSoakTimeSec_Type = Integer32
_CyanOTU2AutoinserviceSoakTimeSec_Object = MibTableColumn
cyanOTU2AutoinserviceSoakTimeSec = _CyanOTU2AutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 5),
    _CyanOTU2AutoinserviceSoakTimeSec_Type()
)
cyanOTU2AutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2AutoinserviceSoakTimeSec.setStatus("current")
_CyanOTU2FecCorrectableBitErrorsCurrSec_Type = Unsigned32
_CyanOTU2FecCorrectableBitErrorsCurrSec_Object = MibTableColumn
cyanOTU2FecCorrectableBitErrorsCurrSec = _CyanOTU2FecCorrectableBitErrorsCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 6),
    _CyanOTU2FecCorrectableBitErrorsCurrSec_Type()
)
cyanOTU2FecCorrectableBitErrorsCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2FecCorrectableBitErrorsCurrSec.setStatus("current")
_CyanOTU2ForwardErrorCoding_Type = CyanFecModeTc
_CyanOTU2ForwardErrorCoding_Object = MibTableColumn
cyanOTU2ForwardErrorCoding = _CyanOTU2ForwardErrorCoding_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 7),
    _CyanOTU2ForwardErrorCoding_Type()
)
cyanOTU2ForwardErrorCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2ForwardErrorCoding.setStatus("current")
_CyanOTU2OperState_Type = CyanOpStateTc
_CyanOTU2OperState_Object = MibTableColumn
cyanOTU2OperState = _CyanOTU2OperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 8),
    _CyanOTU2OperState_Type()
)
cyanOTU2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2OperState.setStatus("current")
_CyanOTU2OperStateQual_Type = CyanOpStateQualTc
_CyanOTU2OperStateQual_Object = MibTableColumn
cyanOTU2OperStateQual = _CyanOTU2OperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 9),
    _CyanOTU2OperStateQual_Type()
)
cyanOTU2OperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2OperStateQual.setStatus("current")
_CyanOTU2RxFecErrorCorrection_Type = CyanEnDisabledTc
_CyanOTU2RxFecErrorCorrection_Object = MibTableColumn
cyanOTU2RxFecErrorCorrection = _CyanOTU2RxFecErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 10),
    _CyanOTU2RxFecErrorCorrection_Type()
)
cyanOTU2RxFecErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2RxFecErrorCorrection.setStatus("current")
_CyanOTU2SecServState_Type = CyanSecServiceStateTc
_CyanOTU2SecServState_Object = MibTableColumn
cyanOTU2SecServState = _CyanOTU2SecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 11),
    _CyanOTU2SecServState_Type()
)
cyanOTU2SecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2SecServState.setStatus("current")
_CyanOTU2SupportedRates_Type = CyanLayerRateTc
_CyanOTU2SupportedRates_Object = MibTableColumn
cyanOTU2SupportedRates = _CyanOTU2SupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 1, 1, 1, 12),
    _CyanOTU2SupportedRates_Type()
)
cyanOTU2SupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanOTU2SupportedRates.setStatus("current")

# Managed Objects groups

cyanOTU2ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 20)
)
cyanOTU2ObjectGroup.setObjects(
      *(("CYAN-OTU2-MIB", "cyanOTU2AdminState"),
        ("CYAN-OTU2-MIB", "cyanOTU2AutoinserviceSoakTimeSec"),
        ("CYAN-OTU2-MIB", "cyanOTU2FecCorrectableBitErrorsCurrSec"),
        ("CYAN-OTU2-MIB", "cyanOTU2ForwardErrorCoding"),
        ("CYAN-OTU2-MIB", "cyanOTU2OperState"),
        ("CYAN-OTU2-MIB", "cyanOTU2OperStateQual"),
        ("CYAN-OTU2-MIB", "cyanOTU2RxFecErrorCorrection"),
        ("CYAN-OTU2-MIB", "cyanOTU2SecServState"),
        ("CYAN-OTU2-MIB", "cyanOTU2SupportedRates"))
)
if mibBuilder.loadTexts:
    cyanOTU2ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanOTU2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 190, 30)
)
if mibBuilder.loadTexts:
    cyanOTU2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-OTU2-MIB",
    **{"cyanOTU2Module": cyanOTU2Module,
       "cyanOTU2MibObjects": cyanOTU2MibObjects,
       "cyanOTU2Table": cyanOTU2Table,
       "cyanOTU2Entry": cyanOTU2Entry,
       "cyanOTU2ShelfId": cyanOTU2ShelfId,
       "cyanOTU2ModuleId": cyanOTU2ModuleId,
       "cyanOTU2OTU2Id": cyanOTU2OTU2Id,
       "cyanOTU2AdminState": cyanOTU2AdminState,
       "cyanOTU2AutoinserviceSoakTimeSec": cyanOTU2AutoinserviceSoakTimeSec,
       "cyanOTU2FecCorrectableBitErrorsCurrSec": cyanOTU2FecCorrectableBitErrorsCurrSec,
       "cyanOTU2ForwardErrorCoding": cyanOTU2ForwardErrorCoding,
       "cyanOTU2OperState": cyanOTU2OperState,
       "cyanOTU2OperStateQual": cyanOTU2OperStateQual,
       "cyanOTU2RxFecErrorCorrection": cyanOTU2RxFecErrorCorrection,
       "cyanOTU2SecServState": cyanOTU2SecServState,
       "cyanOTU2SupportedRates": cyanOTU2SupportedRates,
       "cyanOTU2ObjectGroup": cyanOTU2ObjectGroup,
       "cyanOTU2Compliance": cyanOTU2Compliance}
)
