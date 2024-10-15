# SNMP MIB module (UMSASSETID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMSASSETID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:30 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Boolean,
 Datetime,
 Real32,
 Real64,
 Sint16,
 Sint32,
 Sint64,
 Sint8,
 String,
 Uint16,
 Uint32,
 Uint64,
 Uint8,
 ibmpsgAssetID) = mibBuilder.importSymbols(
    "UMS-MIB",
    "Boolean",
    "Datetime",
    "Real32",
    "Real64",
    "Sint16",
    "Sint32",
    "Sint64",
    "Sint8",
    "String",
    "Uint16",
    "Uint32",
    "Uint64",
    "Uint8",
    "ibmpsgAssetID")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IBMPSGSerialNumberInformationTable_Object = MibTable
iBMPSGSerialNumberInformationTable = _IBMPSGSerialNumberInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1)
)
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationTable.setStatus("mandatory")
_IBMPSGSerialNumberInformationEntry_Object = MibTableRow
iBMPSGSerialNumberInformationEntry = _IBMPSGSerialNumberInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1)
)
iBMPSGSerialNumberInformationEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGSerialNumberInformationKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationEntry.setStatus("mandatory")
_IBMPSGSerialNumberInformationKeyIndex_Type = String
_IBMPSGSerialNumberInformationKeyIndex_Object = MibTableColumn
iBMPSGSerialNumberInformationKeyIndex = _IBMPSGSerialNumberInformationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 1),
    _IBMPSGSerialNumberInformationKeyIndex_Type()
)
iBMPSGSerialNumberInformationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationKeyIndex.setStatus("mandatory")
_IBMPSGSerialNumberInformationName_Type = String
_IBMPSGSerialNumberInformationName_Object = MibTableColumn
iBMPSGSerialNumberInformationName = _IBMPSGSerialNumberInformationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 2),
    _IBMPSGSerialNumberInformationName_Type()
)
iBMPSGSerialNumberInformationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationName.setStatus("mandatory")
_IBMPSGSerialNumberInformationSerialNumber_Type = String
_IBMPSGSerialNumberInformationSerialNumber_Object = MibTableColumn
iBMPSGSerialNumberInformationSerialNumber = _IBMPSGSerialNumberInformationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 3),
    _IBMPSGSerialNumberInformationSerialNumber_Type()
)
iBMPSGSerialNumberInformationSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationSerialNumber.setStatus("mandatory")
_IBMPSGSerialNumberInformationManufacturer_Type = String
_IBMPSGSerialNumberInformationManufacturer_Object = MibTableColumn
iBMPSGSerialNumberInformationManufacturer = _IBMPSGSerialNumberInformationManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 4),
    _IBMPSGSerialNumberInformationManufacturer_Type()
)
iBMPSGSerialNumberInformationManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationManufacturer.setStatus("mandatory")
_IBMPSGSerialNumberInformationModel_Type = String
_IBMPSGSerialNumberInformationModel_Object = MibTableColumn
iBMPSGSerialNumberInformationModel = _IBMPSGSerialNumberInformationModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 5),
    _IBMPSGSerialNumberInformationModel_Type()
)
iBMPSGSerialNumberInformationModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationModel.setStatus("mandatory")
_IBMPSGSerialNumberInformationVersion_Type = String
_IBMPSGSerialNumberInformationVersion_Object = MibTableColumn
iBMPSGSerialNumberInformationVersion = _IBMPSGSerialNumberInformationVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 6),
    _IBMPSGSerialNumberInformationVersion_Type()
)
iBMPSGSerialNumberInformationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationVersion.setStatus("mandatory")
_IBMPSGSerialNumberInformationOtherIdentifyingInfo_Type = String
_IBMPSGSerialNumberInformationOtherIdentifyingInfo_Object = MibTableColumn
iBMPSGSerialNumberInformationOtherIdentifyingInfo = _IBMPSGSerialNumberInformationOtherIdentifyingInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 1, 1, 7),
    _IBMPSGSerialNumberInformationOtherIdentifyingInfo_Type()
)
iBMPSGSerialNumberInformationOtherIdentifyingInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSerialNumberInformationOtherIdentifyingInfo.setStatus("mandatory")
_IBMPSGComputerSystemTable_Object = MibTable
iBMPSGComputerSystemTable = _IBMPSGComputerSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2)
)
if mibBuilder.loadTexts:
    iBMPSGComputerSystemTable.setStatus("mandatory")
_IBMPSGComputerSystemEntry_Object = MibTableRow
iBMPSGComputerSystemEntry = _IBMPSGComputerSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1)
)
iBMPSGComputerSystemEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGComputerSystemKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGComputerSystemEntry.setStatus("mandatory")
_IBMPSGComputerSystemKeyIndex_Type = String
_IBMPSGComputerSystemKeyIndex_Object = MibTableColumn
iBMPSGComputerSystemKeyIndex = _IBMPSGComputerSystemKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1, 1),
    _IBMPSGComputerSystemKeyIndex_Type()
)
iBMPSGComputerSystemKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemKeyIndex.setStatus("mandatory")
_IBMPSGComputerSystemName_Type = String
_IBMPSGComputerSystemName_Object = MibTableColumn
iBMPSGComputerSystemName = _IBMPSGComputerSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1, 2),
    _IBMPSGComputerSystemName_Type()
)
iBMPSGComputerSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemName.setStatus("mandatory")
_IBMPSGComputerSystemModel_Type = String
_IBMPSGComputerSystemModel_Object = MibTableColumn
iBMPSGComputerSystemModel = _IBMPSGComputerSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1, 3),
    _IBMPSGComputerSystemModel_Type()
)
iBMPSGComputerSystemModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemModel.setStatus("mandatory")
_IBMPSGComputerSystemPrimaryOwnerContact_Type = String
_IBMPSGComputerSystemPrimaryOwnerContact_Object = MibTableColumn
iBMPSGComputerSystemPrimaryOwnerContact = _IBMPSGComputerSystemPrimaryOwnerContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1, 4),
    _IBMPSGComputerSystemPrimaryOwnerContact_Type()
)
iBMPSGComputerSystemPrimaryOwnerContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemPrimaryOwnerContact.setStatus("mandatory")
_IBMPSGComputerSystemStatus_Type = String
_IBMPSGComputerSystemStatus_Object = MibTableColumn
iBMPSGComputerSystemStatus = _IBMPSGComputerSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 2, 1, 5),
    _IBMPSGComputerSystemStatus_Type()
)
iBMPSGComputerSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemStatus.setStatus("mandatory")
_IBMPSGComputerSystemDetailsTable_Object = MibTable
iBMPSGComputerSystemDetailsTable = _IBMPSGComputerSystemDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3)
)
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsTable.setStatus("mandatory")
_IBMPSGComputerSystemDetailsEntry_Object = MibTableRow
iBMPSGComputerSystemDetailsEntry = _IBMPSGComputerSystemDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1)
)
iBMPSGComputerSystemDetailsEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGComputerSystemDetailsKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsEntry.setStatus("mandatory")
_IBMPSGComputerSystemDetailsKeyIndex_Type = String
_IBMPSGComputerSystemDetailsKeyIndex_Object = MibTableColumn
iBMPSGComputerSystemDetailsKeyIndex = _IBMPSGComputerSystemDetailsKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 1),
    _IBMPSGComputerSystemDetailsKeyIndex_Type()
)
iBMPSGComputerSystemDetailsKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsKeyIndex.setStatus("mandatory")
_IBMPSGComputerSystemDetailsName_Type = String
_IBMPSGComputerSystemDetailsName_Object = MibTableColumn
iBMPSGComputerSystemDetailsName = _IBMPSGComputerSystemDetailsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 2),
    _IBMPSGComputerSystemDetailsName_Type()
)
iBMPSGComputerSystemDetailsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsName.setStatus("mandatory")
_IBMPSGComputerSystemDetailsSystemUUID_Type = String
_IBMPSGComputerSystemDetailsSystemUUID_Object = MibTableColumn
iBMPSGComputerSystemDetailsSystemUUID = _IBMPSGComputerSystemDetailsSystemUUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 3),
    _IBMPSGComputerSystemDetailsSystemUUID_Type()
)
iBMPSGComputerSystemDetailsSystemUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsSystemUUID.setStatus("mandatory")
_IBMPSGComputerSystemDetailsAssetNumber_Type = String
_IBMPSGComputerSystemDetailsAssetNumber_Object = MibTableColumn
iBMPSGComputerSystemDetailsAssetNumber = _IBMPSGComputerSystemDetailsAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 4),
    _IBMPSGComputerSystemDetailsAssetNumber_Type()
)
iBMPSGComputerSystemDetailsAssetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsAssetNumber.setStatus("mandatory")
_IBMPSGComputerSystemDetailsAssetIdTag_Type = String
_IBMPSGComputerSystemDetailsAssetIdTag_Object = MibTableColumn
iBMPSGComputerSystemDetailsAssetIdTag = _IBMPSGComputerSystemDetailsAssetIdTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 5),
    _IBMPSGComputerSystemDetailsAssetIdTag_Type()
)
iBMPSGComputerSystemDetailsAssetIdTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsAssetIdTag.setStatus("mandatory")
_IBMPSGComputerSystemDetailsLastInventoried_Type = Datetime
_IBMPSGComputerSystemDetailsLastInventoried_Object = MibTableColumn
iBMPSGComputerSystemDetailsLastInventoried = _IBMPSGComputerSystemDetailsLastInventoried_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 6),
    _IBMPSGComputerSystemDetailsLastInventoried_Type()
)
iBMPSGComputerSystemDetailsLastInventoried.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsLastInventoried.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPurchaseDate_Type = Datetime
_IBMPSGComputerSystemDetailsPurchaseDate_Object = MibTableColumn
iBMPSGComputerSystemDetailsPurchaseDate = _IBMPSGComputerSystemDetailsPurchaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 7),
    _IBMPSGComputerSystemDetailsPurchaseDate_Type()
)
iBMPSGComputerSystemDetailsPurchaseDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPurchaseDate.setStatus("mandatory")
_IBMPSGComputerSystemDetailsModel_Type = String
_IBMPSGComputerSystemDetailsModel_Object = MibTableColumn
iBMPSGComputerSystemDetailsModel = _IBMPSGComputerSystemDetailsModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 8),
    _IBMPSGComputerSystemDetailsModel_Type()
)
iBMPSGComputerSystemDetailsModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsModel.setStatus("mandatory")
_IBMPSGComputerSystemDetailsProductName_Type = String
_IBMPSGComputerSystemDetailsProductName_Object = MibTableColumn
iBMPSGComputerSystemDetailsProductName = _IBMPSGComputerSystemDetailsProductName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 9),
    _IBMPSGComputerSystemDetailsProductName_Type()
)
iBMPSGComputerSystemDetailsProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsProductName.setStatus("mandatory")
_IBMPSGComputerSystemDetailsSerialNumber_Type = String
_IBMPSGComputerSystemDetailsSerialNumber_Object = MibTableColumn
iBMPSGComputerSystemDetailsSerialNumber = _IBMPSGComputerSystemDetailsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 10),
    _IBMPSGComputerSystemDetailsSerialNumber_Type()
)
iBMPSGComputerSystemDetailsSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsSerialNumber.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedLabel1_Type = String
_IBMPSGComputerSystemDetailsPersonalizedLabel1_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedLabel1 = _IBMPSGComputerSystemDetailsPersonalizedLabel1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 11),
    _IBMPSGComputerSystemDetailsPersonalizedLabel1_Type()
)
iBMPSGComputerSystemDetailsPersonalizedLabel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedLabel1.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedData1_Type = String
_IBMPSGComputerSystemDetailsPersonalizedData1_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedData1 = _IBMPSGComputerSystemDetailsPersonalizedData1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 12),
    _IBMPSGComputerSystemDetailsPersonalizedData1_Type()
)
iBMPSGComputerSystemDetailsPersonalizedData1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedData1.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedLabel2_Type = String
_IBMPSGComputerSystemDetailsPersonalizedLabel2_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedLabel2 = _IBMPSGComputerSystemDetailsPersonalizedLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 13),
    _IBMPSGComputerSystemDetailsPersonalizedLabel2_Type()
)
iBMPSGComputerSystemDetailsPersonalizedLabel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedLabel2.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedData2_Type = String
_IBMPSGComputerSystemDetailsPersonalizedData2_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedData2 = _IBMPSGComputerSystemDetailsPersonalizedData2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 14),
    _IBMPSGComputerSystemDetailsPersonalizedData2_Type()
)
iBMPSGComputerSystemDetailsPersonalizedData2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedData2.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedLabel3_Type = String
_IBMPSGComputerSystemDetailsPersonalizedLabel3_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedLabel3 = _IBMPSGComputerSystemDetailsPersonalizedLabel3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 15),
    _IBMPSGComputerSystemDetailsPersonalizedLabel3_Type()
)
iBMPSGComputerSystemDetailsPersonalizedLabel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedLabel3.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedData3_Type = String
_IBMPSGComputerSystemDetailsPersonalizedData3_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedData3 = _IBMPSGComputerSystemDetailsPersonalizedData3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 16),
    _IBMPSGComputerSystemDetailsPersonalizedData3_Type()
)
iBMPSGComputerSystemDetailsPersonalizedData3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedData3.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedLabel4_Type = String
_IBMPSGComputerSystemDetailsPersonalizedLabel4_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedLabel4 = _IBMPSGComputerSystemDetailsPersonalizedLabel4_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 17),
    _IBMPSGComputerSystemDetailsPersonalizedLabel4_Type()
)
iBMPSGComputerSystemDetailsPersonalizedLabel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedLabel4.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedData4_Type = String
_IBMPSGComputerSystemDetailsPersonalizedData4_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedData4 = _IBMPSGComputerSystemDetailsPersonalizedData4_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 18),
    _IBMPSGComputerSystemDetailsPersonalizedData4_Type()
)
iBMPSGComputerSystemDetailsPersonalizedData4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedData4.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedLabel5_Type = String
_IBMPSGComputerSystemDetailsPersonalizedLabel5_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedLabel5 = _IBMPSGComputerSystemDetailsPersonalizedLabel5_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 19),
    _IBMPSGComputerSystemDetailsPersonalizedLabel5_Type()
)
iBMPSGComputerSystemDetailsPersonalizedLabel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedLabel5.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPersonalizedData5_Type = String
_IBMPSGComputerSystemDetailsPersonalizedData5_Object = MibTableColumn
iBMPSGComputerSystemDetailsPersonalizedData5 = _IBMPSGComputerSystemDetailsPersonalizedData5_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 20),
    _IBMPSGComputerSystemDetailsPersonalizedData5_Type()
)
iBMPSGComputerSystemDetailsPersonalizedData5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPersonalizedData5.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPrimaryOwnerName_Type = String
_IBMPSGComputerSystemDetailsPrimaryOwnerName_Object = MibTableColumn
iBMPSGComputerSystemDetailsPrimaryOwnerName = _IBMPSGComputerSystemDetailsPrimaryOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 21),
    _IBMPSGComputerSystemDetailsPrimaryOwnerName_Type()
)
iBMPSGComputerSystemDetailsPrimaryOwnerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPrimaryOwnerName.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPrimaryOwnerPhone_Type = String
_IBMPSGComputerSystemDetailsPrimaryOwnerPhone_Object = MibTableColumn
iBMPSGComputerSystemDetailsPrimaryOwnerPhone = _IBMPSGComputerSystemDetailsPrimaryOwnerPhone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 22),
    _IBMPSGComputerSystemDetailsPrimaryOwnerPhone_Type()
)
iBMPSGComputerSystemDetailsPrimaryOwnerPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPrimaryOwnerPhone.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPrimaryOwnerDepartment_Type = String
_IBMPSGComputerSystemDetailsPrimaryOwnerDepartment_Object = MibTableColumn
iBMPSGComputerSystemDetailsPrimaryOwnerDepartment = _IBMPSGComputerSystemDetailsPrimaryOwnerDepartment_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 23),
    _IBMPSGComputerSystemDetailsPrimaryOwnerDepartment_Type()
)
iBMPSGComputerSystemDetailsPrimaryOwnerDepartment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPrimaryOwnerDepartment.setStatus("mandatory")
_IBMPSGComputerSystemDetailsPrimaryOwnerPosition_Type = String
_IBMPSGComputerSystemDetailsPrimaryOwnerPosition_Object = MibTableColumn
iBMPSGComputerSystemDetailsPrimaryOwnerPosition = _IBMPSGComputerSystemDetailsPrimaryOwnerPosition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 24),
    _IBMPSGComputerSystemDetailsPrimaryOwnerPosition_Type()
)
iBMPSGComputerSystemDetailsPrimaryOwnerPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsPrimaryOwnerPosition.setStatus("mandatory")
_IBMPSGComputerSystemDetailsSystemLocation_Type = String
_IBMPSGComputerSystemDetailsSystemLocation_Object = MibTableColumn
iBMPSGComputerSystemDetailsSystemLocation = _IBMPSGComputerSystemDetailsSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 25),
    _IBMPSGComputerSystemDetailsSystemLocation_Type()
)
iBMPSGComputerSystemDetailsSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsSystemLocation.setStatus("mandatory")
_IBMPSGComputerSystemDetailsAssetIDStringArea_Type = Uint32
_IBMPSGComputerSystemDetailsAssetIDStringArea_Object = MibTableColumn
iBMPSGComputerSystemDetailsAssetIDStringArea = _IBMPSGComputerSystemDetailsAssetIDStringArea_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 26),
    _IBMPSGComputerSystemDetailsAssetIDStringArea_Type()
)
iBMPSGComputerSystemDetailsAssetIDStringArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsAssetIDStringArea.setStatus("mandatory")
_IBMPSGComputerSystemDetailsLocalDateTime_Type = Datetime
_IBMPSGComputerSystemDetailsLocalDateTime_Object = MibTableColumn
iBMPSGComputerSystemDetailsLocalDateTime = _IBMPSGComputerSystemDetailsLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 27),
    _IBMPSGComputerSystemDetailsLocalDateTime_Type()
)
iBMPSGComputerSystemDetailsLocalDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsLocalDateTime.setStatus("mandatory")
_IBMPSGComputerSystemDetailsLCCMProfile_Type = String
_IBMPSGComputerSystemDetailsLCCMProfile_Object = MibTableColumn
iBMPSGComputerSystemDetailsLCCMProfile = _IBMPSGComputerSystemDetailsLCCMProfile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 28),
    _IBMPSGComputerSystemDetailsLCCMProfile_Type()
)
iBMPSGComputerSystemDetailsLCCMProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsLCCMProfile.setStatus("mandatory")
_IBMPSGComputerSystemDetailsLCCMUpdateTime_Type = Datetime
_IBMPSGComputerSystemDetailsLCCMUpdateTime_Object = MibTableColumn
iBMPSGComputerSystemDetailsLCCMUpdateTime = _IBMPSGComputerSystemDetailsLCCMUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 3, 1, 29),
    _IBMPSGComputerSystemDetailsLCCMUpdateTime_Type()
)
iBMPSGComputerSystemDetailsLCCMUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGComputerSystemDetailsLCCMUpdateTime.setStatus("mandatory")
_IBMPSGLeaseTable_Object = MibTable
iBMPSGLeaseTable = _IBMPSGLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4)
)
if mibBuilder.loadTexts:
    iBMPSGLeaseTable.setStatus("mandatory")
_IBMPSGLeaseEntry_Object = MibTableRow
iBMPSGLeaseEntry = _IBMPSGLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1)
)
iBMPSGLeaseEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGLeaseKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGLeaseEntry.setStatus("mandatory")
_IBMPSGLeaseKeyIndex_Type = String
_IBMPSGLeaseKeyIndex_Object = MibTableColumn
iBMPSGLeaseKeyIndex = _IBMPSGLeaseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 1),
    _IBMPSGLeaseKeyIndex_Type()
)
iBMPSGLeaseKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseKeyIndex.setStatus("mandatory")
_IBMPSGLeaseName_Type = String
_IBMPSGLeaseName_Object = MibTableColumn
iBMPSGLeaseName = _IBMPSGLeaseName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 2),
    _IBMPSGLeaseName_Type()
)
iBMPSGLeaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseName.setStatus("mandatory")
_IBMPSGLeaseLessor_Type = String
_IBMPSGLeaseLessor_Object = MibTableColumn
iBMPSGLeaseLessor = _IBMPSGLeaseLessor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 3),
    _IBMPSGLeaseLessor_Type()
)
iBMPSGLeaseLessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLessor.setStatus("mandatory")
_IBMPSGLeaseBuyout_Type = Uint32
_IBMPSGLeaseBuyout_Object = MibTableColumn
iBMPSGLeaseBuyout = _IBMPSGLeaseBuyout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 4),
    _IBMPSGLeaseBuyout_Type()
)
iBMPSGLeaseBuyout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseBuyout.setStatus("mandatory")
_IBMPSGLeaseLRF_Type = Uint8
_IBMPSGLeaseLRF_Object = MibTableColumn
iBMPSGLeaseLRF = _IBMPSGLeaseLRF_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 5),
    _IBMPSGLeaseLRF_Type()
)
iBMPSGLeaseLRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLRF.setStatus("mandatory")
_IBMPSGLeaseLeaseStartDate_Type = Datetime
_IBMPSGLeaseLeaseStartDate_Object = MibTableColumn
iBMPSGLeaseLeaseStartDate = _IBMPSGLeaseLeaseStartDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 6),
    _IBMPSGLeaseLeaseStartDate_Type()
)
iBMPSGLeaseLeaseStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLeaseStartDate.setStatus("mandatory")
_IBMPSGLeaseLeaseEndDate_Type = Datetime
_IBMPSGLeaseLeaseEndDate_Object = MibTableColumn
iBMPSGLeaseLeaseEndDate = _IBMPSGLeaseLeaseEndDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 7),
    _IBMPSGLeaseLeaseEndDate_Type()
)
iBMPSGLeaseLeaseEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLeaseEndDate.setStatus("mandatory")
_IBMPSGLeaseFMV_Type = Uint32
_IBMPSGLeaseFMV_Object = MibTableColumn
iBMPSGLeaseFMV = _IBMPSGLeaseFMV_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 8),
    _IBMPSGLeaseFMV_Type()
)
iBMPSGLeaseFMV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseFMV.setStatus("mandatory")
_IBMPSGLeaseLeaseTerm_Type = Uint8
_IBMPSGLeaseLeaseTerm_Object = MibTableColumn
iBMPSGLeaseLeaseTerm = _IBMPSGLeaseLeaseTerm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 9),
    _IBMPSGLeaseLeaseTerm_Type()
)
iBMPSGLeaseLeaseTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLeaseTerm.setStatus("mandatory")
_IBMPSGLeaseLeasePayment_Type = String
_IBMPSGLeaseLeasePayment_Object = MibTableColumn
iBMPSGLeaseLeasePayment = _IBMPSGLeaseLeasePayment_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 4, 1, 10),
    _IBMPSGLeaseLeasePayment_Type()
)
iBMPSGLeaseLeasePayment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGLeaseLeasePayment.setStatus("mandatory")
_IBMPSGWarrantyTable_Object = MibTable
iBMPSGWarrantyTable = _IBMPSGWarrantyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5)
)
if mibBuilder.loadTexts:
    iBMPSGWarrantyTable.setStatus("mandatory")
_IBMPSGWarrantyEntry_Object = MibTableRow
iBMPSGWarrantyEntry = _IBMPSGWarrantyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1)
)
iBMPSGWarrantyEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGWarrantyKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGWarrantyEntry.setStatus("mandatory")
_IBMPSGWarrantyKeyIndex_Type = String
_IBMPSGWarrantyKeyIndex_Object = MibTableColumn
iBMPSGWarrantyKeyIndex = _IBMPSGWarrantyKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 1),
    _IBMPSGWarrantyKeyIndex_Type()
)
iBMPSGWarrantyKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyKeyIndex.setStatus("mandatory")
_IBMPSGWarrantyName_Type = String
_IBMPSGWarrantyName_Object = MibTableColumn
iBMPSGWarrantyName = _IBMPSGWarrantyName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 2),
    _IBMPSGWarrantyName_Type()
)
iBMPSGWarrantyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyName.setStatus("mandatory")
_IBMPSGWarrantyWarrantyDuration_Type = Uint8
_IBMPSGWarrantyWarrantyDuration_Object = MibTableColumn
iBMPSGWarrantyWarrantyDuration = _IBMPSGWarrantyWarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 3),
    _IBMPSGWarrantyWarrantyDuration_Type()
)
iBMPSGWarrantyWarrantyDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyWarrantyDuration.setStatus("mandatory")
_IBMPSGWarrantyWarrantyDurationUnit_Type = Uint8
_IBMPSGWarrantyWarrantyDurationUnit_Object = MibTableColumn
iBMPSGWarrantyWarrantyDurationUnit = _IBMPSGWarrantyWarrantyDurationUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 4),
    _IBMPSGWarrantyWarrantyDurationUnit_Type()
)
iBMPSGWarrantyWarrantyDurationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyWarrantyDurationUnit.setStatus("mandatory")
_IBMPSGWarrantyWarrantyEndDate_Type = Datetime
_IBMPSGWarrantyWarrantyEndDate_Object = MibTableColumn
iBMPSGWarrantyWarrantyEndDate = _IBMPSGWarrantyWarrantyEndDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 5),
    _IBMPSGWarrantyWarrantyEndDate_Type()
)
iBMPSGWarrantyWarrantyEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyWarrantyEndDate.setStatus("mandatory")
_IBMPSGWarrantyWarrantyCost_Type = String
_IBMPSGWarrantyWarrantyCost_Object = MibTableColumn
iBMPSGWarrantyWarrantyCost = _IBMPSGWarrantyWarrantyCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 5, 1, 6),
    _IBMPSGWarrantyWarrantyCost_Type()
)
iBMPSGWarrantyWarrantyCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWarrantyWarrantyCost.setStatus("mandatory")
_IBMPSGFRUTable_Object = MibTable
iBMPSGFRUTable = _IBMPSGFRUTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6)
)
if mibBuilder.loadTexts:
    iBMPSGFRUTable.setStatus("mandatory")
_IBMPSGFRUEntry_Object = MibTableRow
iBMPSGFRUEntry = _IBMPSGFRUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1)
)
iBMPSGFRUEntry.setIndexNames(
    (0, "UMSASSETID-MIB", "iBMPSGFRUKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGFRUEntry.setStatus("mandatory")
_IBMPSGFRUKeyIndex_Type = String
_IBMPSGFRUKeyIndex_Object = MibTableColumn
iBMPSGFRUKeyIndex = _IBMPSGFRUKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 1),
    _IBMPSGFRUKeyIndex_Type()
)
iBMPSGFRUKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUKeyIndex.setStatus("mandatory")
_IBMPSGFRUName_Type = String
_IBMPSGFRUName_Object = MibTableColumn
iBMPSGFRUName = _IBMPSGFRUName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 2),
    _IBMPSGFRUName_Type()
)
iBMPSGFRUName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUName.setStatus("mandatory")
_IBMPSGFRUFRUNumber_Type = String
_IBMPSGFRUFRUNumber_Object = MibTableColumn
iBMPSGFRUFRUNumber = _IBMPSGFRUFRUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 3),
    _IBMPSGFRUFRUNumber_Type()
)
iBMPSGFRUFRUNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUFRUNumber.setStatus("mandatory")
_IBMPSGFRUIdentifyingNumber_Type = String
_IBMPSGFRUIdentifyingNumber_Object = MibTableColumn
iBMPSGFRUIdentifyingNumber = _IBMPSGFRUIdentifyingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 4),
    _IBMPSGFRUIdentifyingNumber_Type()
)
iBMPSGFRUIdentifyingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUIdentifyingNumber.setStatus("mandatory")
_IBMPSGFRUVendor_Type = String
_IBMPSGFRUVendor_Object = MibTableColumn
iBMPSGFRUVendor = _IBMPSGFRUVendor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 5),
    _IBMPSGFRUVendor_Type()
)
iBMPSGFRUVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUVendor.setStatus("mandatory")
_IBMPSGFRURevisionLevel_Type = String
_IBMPSGFRURevisionLevel_Object = MibTableColumn
iBMPSGFRURevisionLevel = _IBMPSGFRURevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 6),
    _IBMPSGFRURevisionLevel_Type()
)
iBMPSGFRURevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRURevisionLevel.setStatus("mandatory")
_IBMPSGFRUDescription_Type = String
_IBMPSGFRUDescription_Object = MibTableColumn
iBMPSGFRUDescription = _IBMPSGFRUDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 60, 6, 1, 7),
    _IBMPSGFRUDescription_Type()
)
iBMPSGFRUDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFRUDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMSASSETID-MIB",
    **{"iBMPSGSerialNumberInformationTable": iBMPSGSerialNumberInformationTable,
       "iBMPSGSerialNumberInformationEntry": iBMPSGSerialNumberInformationEntry,
       "iBMPSGSerialNumberInformationKeyIndex": iBMPSGSerialNumberInformationKeyIndex,
       "iBMPSGSerialNumberInformationName": iBMPSGSerialNumberInformationName,
       "iBMPSGSerialNumberInformationSerialNumber": iBMPSGSerialNumberInformationSerialNumber,
       "iBMPSGSerialNumberInformationManufacturer": iBMPSGSerialNumberInformationManufacturer,
       "iBMPSGSerialNumberInformationModel": iBMPSGSerialNumberInformationModel,
       "iBMPSGSerialNumberInformationVersion": iBMPSGSerialNumberInformationVersion,
       "iBMPSGSerialNumberInformationOtherIdentifyingInfo": iBMPSGSerialNumberInformationOtherIdentifyingInfo,
       "iBMPSGComputerSystemTable": iBMPSGComputerSystemTable,
       "iBMPSGComputerSystemEntry": iBMPSGComputerSystemEntry,
       "iBMPSGComputerSystemKeyIndex": iBMPSGComputerSystemKeyIndex,
       "iBMPSGComputerSystemName": iBMPSGComputerSystemName,
       "iBMPSGComputerSystemModel": iBMPSGComputerSystemModel,
       "iBMPSGComputerSystemPrimaryOwnerContact": iBMPSGComputerSystemPrimaryOwnerContact,
       "iBMPSGComputerSystemStatus": iBMPSGComputerSystemStatus,
       "iBMPSGComputerSystemDetailsTable": iBMPSGComputerSystemDetailsTable,
       "iBMPSGComputerSystemDetailsEntry": iBMPSGComputerSystemDetailsEntry,
       "iBMPSGComputerSystemDetailsKeyIndex": iBMPSGComputerSystemDetailsKeyIndex,
       "iBMPSGComputerSystemDetailsName": iBMPSGComputerSystemDetailsName,
       "iBMPSGComputerSystemDetailsSystemUUID": iBMPSGComputerSystemDetailsSystemUUID,
       "iBMPSGComputerSystemDetailsAssetNumber": iBMPSGComputerSystemDetailsAssetNumber,
       "iBMPSGComputerSystemDetailsAssetIdTag": iBMPSGComputerSystemDetailsAssetIdTag,
       "iBMPSGComputerSystemDetailsLastInventoried": iBMPSGComputerSystemDetailsLastInventoried,
       "iBMPSGComputerSystemDetailsPurchaseDate": iBMPSGComputerSystemDetailsPurchaseDate,
       "iBMPSGComputerSystemDetailsModel": iBMPSGComputerSystemDetailsModel,
       "iBMPSGComputerSystemDetailsProductName": iBMPSGComputerSystemDetailsProductName,
       "iBMPSGComputerSystemDetailsSerialNumber": iBMPSGComputerSystemDetailsSerialNumber,
       "iBMPSGComputerSystemDetailsPersonalizedLabel1": iBMPSGComputerSystemDetailsPersonalizedLabel1,
       "iBMPSGComputerSystemDetailsPersonalizedData1": iBMPSGComputerSystemDetailsPersonalizedData1,
       "iBMPSGComputerSystemDetailsPersonalizedLabel2": iBMPSGComputerSystemDetailsPersonalizedLabel2,
       "iBMPSGComputerSystemDetailsPersonalizedData2": iBMPSGComputerSystemDetailsPersonalizedData2,
       "iBMPSGComputerSystemDetailsPersonalizedLabel3": iBMPSGComputerSystemDetailsPersonalizedLabel3,
       "iBMPSGComputerSystemDetailsPersonalizedData3": iBMPSGComputerSystemDetailsPersonalizedData3,
       "iBMPSGComputerSystemDetailsPersonalizedLabel4": iBMPSGComputerSystemDetailsPersonalizedLabel4,
       "iBMPSGComputerSystemDetailsPersonalizedData4": iBMPSGComputerSystemDetailsPersonalizedData4,
       "iBMPSGComputerSystemDetailsPersonalizedLabel5": iBMPSGComputerSystemDetailsPersonalizedLabel5,
       "iBMPSGComputerSystemDetailsPersonalizedData5": iBMPSGComputerSystemDetailsPersonalizedData5,
       "iBMPSGComputerSystemDetailsPrimaryOwnerName": iBMPSGComputerSystemDetailsPrimaryOwnerName,
       "iBMPSGComputerSystemDetailsPrimaryOwnerPhone": iBMPSGComputerSystemDetailsPrimaryOwnerPhone,
       "iBMPSGComputerSystemDetailsPrimaryOwnerDepartment": iBMPSGComputerSystemDetailsPrimaryOwnerDepartment,
       "iBMPSGComputerSystemDetailsPrimaryOwnerPosition": iBMPSGComputerSystemDetailsPrimaryOwnerPosition,
       "iBMPSGComputerSystemDetailsSystemLocation": iBMPSGComputerSystemDetailsSystemLocation,
       "iBMPSGComputerSystemDetailsAssetIDStringArea": iBMPSGComputerSystemDetailsAssetIDStringArea,
       "iBMPSGComputerSystemDetailsLocalDateTime": iBMPSGComputerSystemDetailsLocalDateTime,
       "iBMPSGComputerSystemDetailsLCCMProfile": iBMPSGComputerSystemDetailsLCCMProfile,
       "iBMPSGComputerSystemDetailsLCCMUpdateTime": iBMPSGComputerSystemDetailsLCCMUpdateTime,
       "iBMPSGLeaseTable": iBMPSGLeaseTable,
       "iBMPSGLeaseEntry": iBMPSGLeaseEntry,
       "iBMPSGLeaseKeyIndex": iBMPSGLeaseKeyIndex,
       "iBMPSGLeaseName": iBMPSGLeaseName,
       "iBMPSGLeaseLessor": iBMPSGLeaseLessor,
       "iBMPSGLeaseBuyout": iBMPSGLeaseBuyout,
       "iBMPSGLeaseLRF": iBMPSGLeaseLRF,
       "iBMPSGLeaseLeaseStartDate": iBMPSGLeaseLeaseStartDate,
       "iBMPSGLeaseLeaseEndDate": iBMPSGLeaseLeaseEndDate,
       "iBMPSGLeaseFMV": iBMPSGLeaseFMV,
       "iBMPSGLeaseLeaseTerm": iBMPSGLeaseLeaseTerm,
       "iBMPSGLeaseLeasePayment": iBMPSGLeaseLeasePayment,
       "iBMPSGWarrantyTable": iBMPSGWarrantyTable,
       "iBMPSGWarrantyEntry": iBMPSGWarrantyEntry,
       "iBMPSGWarrantyKeyIndex": iBMPSGWarrantyKeyIndex,
       "iBMPSGWarrantyName": iBMPSGWarrantyName,
       "iBMPSGWarrantyWarrantyDuration": iBMPSGWarrantyWarrantyDuration,
       "iBMPSGWarrantyWarrantyDurationUnit": iBMPSGWarrantyWarrantyDurationUnit,
       "iBMPSGWarrantyWarrantyEndDate": iBMPSGWarrantyWarrantyEndDate,
       "iBMPSGWarrantyWarrantyCost": iBMPSGWarrantyWarrantyCost,
       "iBMPSGFRUTable": iBMPSGFRUTable,
       "iBMPSGFRUEntry": iBMPSGFRUEntry,
       "iBMPSGFRUKeyIndex": iBMPSGFRUKeyIndex,
       "iBMPSGFRUName": iBMPSGFRUName,
       "iBMPSGFRUFRUNumber": iBMPSGFRUFRUNumber,
       "iBMPSGFRUIdentifyingNumber": iBMPSGFRUIdentifyingNumber,
       "iBMPSGFRUVendor": iBMPSGFRUVendor,
       "iBMPSGFRURevisionLevel": iBMPSGFRURevisionLevel,
       "iBMPSGFRUDescription": iBMPSGFRUDescription}
)
