# SNMP MIB module (INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:22 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Server_management_ObjectIdentity = ObjectIdentity
server_management = _Server_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3)
)
_Lra_ObjectIdentity = ObjectIdentity
lra = _Lra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TNameTable_Object = MibTable
tNameTable = _TNameTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tNameTable.setStatus("mandatory")
_ENameTable_Object = MibTableRow
eNameTable = _ENameTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1)
)
eNameTable.setIndexNames(
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a2MifId"),
)
if mibBuilder.loadTexts:
    eNameTable.setStatus("mandatory")


class _A2MifId_Type(Integer32):
    """Custom type a2MifId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              99)
        )
    )
    namedValues = NamedValues(
        *(("vAdaptecCioScsi", 9),
          ("vAdaptecScsi", 2),
          ("vAmiRaid", 7),
          ("vBaseboard", 1),
          ("vIntelNic", 11),
          ("vLsiScsi211", 12),
          ("vMylexGamRaid", 8),
          ("vMylexRaid", 3),
          ("vNic", 4),
          ("vSymbiosScsi", 10),
          ("vSymbiosSdms", 6),
          ("vTestmif", 99),
          ("vUnknown", 0),
          ("vUps", 5))
    )


_A2MifId_Type.__name__ = "Integer32"
_A2MifId_Object = MibTableColumn
a2MifId = _A2MifId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1, 1),
    _A2MifId_Type()
)
a2MifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MifId.setStatus("mandatory")
_A2ComponentName_Type = DmiDisplaystring
_A2ComponentName_Object = MibTableColumn
a2ComponentName = _A2ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 2, 1, 2),
    _A2ComponentName_Type()
)
a2ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ComponentName.setStatus("mandatory")
_TActionsTable_Object = MibTable
tActionsTable = _TActionsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tActionsTable.setStatus("mandatory")
_EActionsTable_Object = MibTableRow
eActionsTable = _EActionsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1)
)
eActionsTable.setIndexNames(
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4RelatedMif"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Group"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Instance"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Attribute"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Value"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a4Severity"),
)
if mibBuilder.loadTexts:
    eActionsTable.setStatus("mandatory")


class _A4RelatedMif_Type(Integer32):
    """Custom type a4RelatedMif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              99)
        )
    )
    namedValues = NamedValues(
        *(("vAdaptecCioScsi", 9),
          ("vAdaptecScsi", 2),
          ("vAmiRaid", 7),
          ("vBaseboard", 1),
          ("vIntelNic", 11),
          ("vLsiScsi211", 12),
          ("vMylexGamRaid", 8),
          ("vMylexRaid", 3),
          ("vNic", 4),
          ("vSymbiosScsi", 10),
          ("vSymbiosSdms", 6),
          ("vTestmif", 99),
          ("vUnknown", 0),
          ("vUps", 5))
    )


_A4RelatedMif_Type.__name__ = "Integer32"
_A4RelatedMif_Object = MibTableColumn
a4RelatedMif = _A4RelatedMif_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 1),
    _A4RelatedMif_Type()
)
a4RelatedMif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4RelatedMif.setStatus("mandatory")
_A4Group_Type = DmiInteger
_A4Group_Object = MibTableColumn
a4Group = _A4Group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 2),
    _A4Group_Type()
)
a4Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Group.setStatus("mandatory")
_A4Instance_Type = DmiInteger
_A4Instance_Object = MibTableColumn
a4Instance = _A4Instance_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 3),
    _A4Instance_Type()
)
a4Instance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Instance.setStatus("mandatory")
_A4Attribute_Type = DmiInteger
_A4Attribute_Object = MibTableColumn
a4Attribute = _A4Attribute_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 4),
    _A4Attribute_Type()
)
a4Attribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Attribute.setStatus("mandatory")
_A4Value_Type = DmiInteger
_A4Value_Object = MibTableColumn
a4Value = _A4Value_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 5),
    _A4Value_Type()
)
a4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Value.setStatus("mandatory")
_A4Severity_Type = DmiInteger
_A4Severity_Object = MibTableColumn
a4Severity = _A4Severity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 6),
    _A4Severity_Type()
)
a4Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Severity.setStatus("mandatory")
_A4BeepSpeaker_Type = DmiInteger
_A4BeepSpeaker_Object = MibTableColumn
a4BeepSpeaker = _A4BeepSpeaker_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 7),
    _A4BeepSpeaker_Type()
)
a4BeepSpeaker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4BeepSpeaker.setStatus("mandatory")
_A4DisplayAlertMessageOnConsole_Type = DmiInteger
_A4DisplayAlertMessageOnConsole_Object = MibTableColumn
a4DisplayAlertMessageOnConsole = _A4DisplayAlertMessageOnConsole_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 8),
    _A4DisplayAlertMessageOnConsole_Type()
)
a4DisplayAlertMessageOnConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4DisplayAlertMessageOnConsole.setStatus("mandatory")
_A4LogToDisk_Type = DmiInteger
_A4LogToDisk_Object = MibTableColumn
a4LogToDisk = _A4LogToDisk_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 9),
    _A4LogToDisk_Type()
)
a4LogToDisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4LogToDisk.setStatus("mandatory")
_A4WriteToLcd_Type = DmiInteger
_A4WriteToLcd_Object = MibTableColumn
a4WriteToLcd = _A4WriteToLcd_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 10),
    _A4WriteToLcd_Type()
)
a4WriteToLcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4WriteToLcd.setStatus("mandatory")
_A4ShutdownTheOs_Type = DmiInteger
_A4ShutdownTheOs_Object = MibTableColumn
a4ShutdownTheOs = _A4ShutdownTheOs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 11),
    _A4ShutdownTheOs_Type()
)
a4ShutdownTheOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4ShutdownTheOs.setStatus("mandatory")
_A4ShutdownAndPowerOffTheSystem_Type = DmiInteger
_A4ShutdownAndPowerOffTheSystem_Object = MibTableColumn
a4ShutdownAndPowerOffTheSystem = _A4ShutdownAndPowerOffTheSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 12),
    _A4ShutdownAndPowerOffTheSystem_Type()
)
a4ShutdownAndPowerOffTheSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4ShutdownAndPowerOffTheSystem.setStatus("mandatory")
_A4ShutdownAndResetTheSystem_Type = DmiInteger
_A4ShutdownAndResetTheSystem_Object = MibTableColumn
a4ShutdownAndResetTheSystem = _A4ShutdownAndResetTheSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 13),
    _A4ShutdownAndResetTheSystem_Type()
)
a4ShutdownAndResetTheSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4ShutdownAndResetTheSystem.setStatus("mandatory")
_A4ImmediatePowerOff_Type = DmiInteger
_A4ImmediatePowerOff_Object = MibTableColumn
a4ImmediatePowerOff = _A4ImmediatePowerOff_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 14),
    _A4ImmediatePowerOff_Type()
)
a4ImmediatePowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4ImmediatePowerOff.setStatus("mandatory")
_A4ImmediateReset_Type = DmiInteger
_A4ImmediateReset_Object = MibTableColumn
a4ImmediateReset = _A4ImmediateReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 15),
    _A4ImmediateReset_Type()
)
a4ImmediateReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4ImmediateReset.setStatus("mandatory")
_A4BroadcastMessageOnNetwork_Type = DmiInteger
_A4BroadcastMessageOnNetwork_Object = MibTableColumn
a4BroadcastMessageOnNetwork = _A4BroadcastMessageOnNetwork_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 16),
    _A4BroadcastMessageOnNetwork_Type()
)
a4BroadcastMessageOnNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4BroadcastMessageOnNetwork.setStatus("mandatory")
_A4AmsAlertName_Type = DmiDisplaystring
_A4AmsAlertName_Object = MibTableColumn
a4AmsAlertName = _A4AmsAlertName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 17),
    _A4AmsAlertName_Type()
)
a4AmsAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AmsAlertName.setStatus("mandatory")
_A4Enabled_Type = DmiInteger
_A4Enabled_Object = MibTableColumn
a4Enabled = _A4Enabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 4, 1, 30),
    _A4Enabled_Type()
)
a4Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4Enabled.setStatus("mandatory")
_TActionsTableForStandardIndications_Object = MibTable
tActionsTableForStandardIndications = _TActionsTableForStandardIndications_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tActionsTableForStandardIndications.setStatus("mandatory")
_EActionsTableForStandardIndications_Object = MibTableRow
eActionsTableForStandardIndications = _EActionsTableForStandardIndications_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1)
)
eActionsTableForStandardIndications.setIndexNames(
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10RelatedMif"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventGenerationGroup"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventType"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Instance"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Reserved"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10Severity"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventSystem"),
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "a10EventSub-system"),
)
if mibBuilder.loadTexts:
    eActionsTableForStandardIndications.setStatus("mandatory")


class _A10RelatedMif_Type(Integer32):
    """Custom type a10RelatedMif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              99)
        )
    )
    namedValues = NamedValues(
        *(("vAdaptecCioScsi", 9),
          ("vAdaptecScsi", 2),
          ("vAmiRaid", 7),
          ("vBaseboard", 1),
          ("vIntelNic", 11),
          ("vLsiScsi211", 12),
          ("vMylexGamRaid", 8),
          ("vMylexRaid", 3),
          ("vNic", 4),
          ("vSymbiosScsi", 10),
          ("vSymbiosSdms", 6),
          ("vTestmif", 99),
          ("vUnknown", 0),
          ("vUps", 5))
    )


_A10RelatedMif_Type.__name__ = "Integer32"
_A10RelatedMif_Object = MibTableColumn
a10RelatedMif = _A10RelatedMif_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 1),
    _A10RelatedMif_Type()
)
a10RelatedMif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10RelatedMif.setStatus("mandatory")
_A10EventGenerationGroup_Type = DmiInteger
_A10EventGenerationGroup_Object = MibTableColumn
a10EventGenerationGroup = _A10EventGenerationGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 2),
    _A10EventGenerationGroup_Type()
)
a10EventGenerationGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventGenerationGroup.setStatus("mandatory")
_A10EventType_Type = DmiInteger
_A10EventType_Object = MibTableColumn
a10EventType = _A10EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 3),
    _A10EventType_Type()
)
a10EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventType.setStatus("mandatory")
_A10Instance_Type = DmiInteger
_A10Instance_Object = MibTableColumn
a10Instance = _A10Instance_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 4),
    _A10Instance_Type()
)
a10Instance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10Instance.setStatus("mandatory")
_A10Reserved_Type = DmiInteger
_A10Reserved_Object = MibScalar
a10Reserved = _A10Reserved_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 5),
    _A10Reserved_Type()
)
a10Reserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10Reserved.setStatus("mandatory")
_A10Severity_Type = DmiInteger
_A10Severity_Object = MibTableColumn
a10Severity = _A10Severity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 6),
    _A10Severity_Type()
)
a10Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10Severity.setStatus("mandatory")
_A10BeepSpeaker_Type = DmiInteger
_A10BeepSpeaker_Object = MibTableColumn
a10BeepSpeaker = _A10BeepSpeaker_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 7),
    _A10BeepSpeaker_Type()
)
a10BeepSpeaker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10BeepSpeaker.setStatus("mandatory")
_A10DisplayAlertMessageOnConsole_Type = DmiInteger
_A10DisplayAlertMessageOnConsole_Object = MibTableColumn
a10DisplayAlertMessageOnConsole = _A10DisplayAlertMessageOnConsole_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 8),
    _A10DisplayAlertMessageOnConsole_Type()
)
a10DisplayAlertMessageOnConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10DisplayAlertMessageOnConsole.setStatus("mandatory")
_A10LogToDisk_Type = DmiInteger
_A10LogToDisk_Object = MibTableColumn
a10LogToDisk = _A10LogToDisk_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 9),
    _A10LogToDisk_Type()
)
a10LogToDisk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10LogToDisk.setStatus("mandatory")
_A10WriteToLcd_Type = DmiInteger
_A10WriteToLcd_Object = MibTableColumn
a10WriteToLcd = _A10WriteToLcd_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 10),
    _A10WriteToLcd_Type()
)
a10WriteToLcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10WriteToLcd.setStatus("mandatory")
_A10ShutdownTheOs_Type = DmiInteger
_A10ShutdownTheOs_Object = MibTableColumn
a10ShutdownTheOs = _A10ShutdownTheOs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 11),
    _A10ShutdownTheOs_Type()
)
a10ShutdownTheOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ShutdownTheOs.setStatus("mandatory")
_A10ShutdownAndPowerOffTheSystem_Type = DmiInteger
_A10ShutdownAndPowerOffTheSystem_Object = MibTableColumn
a10ShutdownAndPowerOffTheSystem = _A10ShutdownAndPowerOffTheSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 12),
    _A10ShutdownAndPowerOffTheSystem_Type()
)
a10ShutdownAndPowerOffTheSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ShutdownAndPowerOffTheSystem.setStatus("mandatory")
_A10ShutdownAndResetTheSystem_Type = DmiInteger
_A10ShutdownAndResetTheSystem_Object = MibTableColumn
a10ShutdownAndResetTheSystem = _A10ShutdownAndResetTheSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 13),
    _A10ShutdownAndResetTheSystem_Type()
)
a10ShutdownAndResetTheSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ShutdownAndResetTheSystem.setStatus("mandatory")
_A10ImmediatePowerOff_Type = DmiInteger
_A10ImmediatePowerOff_Object = MibTableColumn
a10ImmediatePowerOff = _A10ImmediatePowerOff_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 14),
    _A10ImmediatePowerOff_Type()
)
a10ImmediatePowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ImmediatePowerOff.setStatus("mandatory")
_A10ImmediateReset_Type = DmiInteger
_A10ImmediateReset_Object = MibTableColumn
a10ImmediateReset = _A10ImmediateReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 15),
    _A10ImmediateReset_Type()
)
a10ImmediateReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ImmediateReset.setStatus("mandatory")
_A10BroadcastMessageOnNetwork_Type = DmiInteger
_A10BroadcastMessageOnNetwork_Object = MibTableColumn
a10BroadcastMessageOnNetwork = _A10BroadcastMessageOnNetwork_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 16),
    _A10BroadcastMessageOnNetwork_Type()
)
a10BroadcastMessageOnNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10BroadcastMessageOnNetwork.setStatus("mandatory")
_A10AmsAlertName_Type = DmiDisplaystring
_A10AmsAlertName_Object = MibTableColumn
a10AmsAlertName = _A10AmsAlertName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 17),
    _A10AmsAlertName_Type()
)
a10AmsAlertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10AmsAlertName.setStatus("mandatory")
_A10ImmediateNmi_Type = DmiInteger
_A10ImmediateNmi_Object = MibTableColumn
a10ImmediateNmi = _A10ImmediateNmi_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 18),
    _A10ImmediateNmi_Type()
)
a10ImmediateNmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ImmediateNmi.setStatus("mandatory")
_A10Page_Type = DmiInteger
_A10Page_Object = MibTableColumn
a10Page = _A10Page_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 19),
    _A10Page_Type()
)
a10Page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10Page.setStatus("mandatory")
_A10Email_Type = DmiInteger
_A10Email_Object = MibTableColumn
a10Email = _A10Email_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 20),
    _A10Email_Type()
)
a10Email.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10Email.setStatus("mandatory")
_A10Enabled_Type = DmiInteger
_A10Enabled_Object = MibTableColumn
a10Enabled = _A10Enabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 30),
    _A10Enabled_Type()
)
a10Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10Enabled.setStatus("mandatory")
_A10EventSystem_Type = DmiInteger
_A10EventSystem_Object = MibTableColumn
a10EventSystem = _A10EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 31),
    _A10EventSystem_Type()
)
a10EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventSystem.setStatus("mandatory")
_A10EventSub_system_Type = DmiInteger
_A10EventSub_system_Object = MibScalar
a10EventSub_system = _A10EventSub_system_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 10, 1, 32),
    _A10EventSub_system_Type()
)
a10EventSub_system.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventSub_system.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 10, 3, 1, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELLANDESKSERVERMANAGER-LOCALRESPONSEA-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-management": server_management,
       "software": software,
       "lra": lra,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tNameTable": tNameTable,
       "eNameTable": eNameTable,
       "a2MifId": a2MifId,
       "a2ComponentName": a2ComponentName,
       "tActionsTable": tActionsTable,
       "eActionsTable": eActionsTable,
       "a4RelatedMif": a4RelatedMif,
       "a4Group": a4Group,
       "a4Instance": a4Instance,
       "a4Attribute": a4Attribute,
       "a4Value": a4Value,
       "a4Severity": a4Severity,
       "a4BeepSpeaker": a4BeepSpeaker,
       "a4DisplayAlertMessageOnConsole": a4DisplayAlertMessageOnConsole,
       "a4LogToDisk": a4LogToDisk,
       "a4WriteToLcd": a4WriteToLcd,
       "a4ShutdownTheOs": a4ShutdownTheOs,
       "a4ShutdownAndPowerOffTheSystem": a4ShutdownAndPowerOffTheSystem,
       "a4ShutdownAndResetTheSystem": a4ShutdownAndResetTheSystem,
       "a4ImmediatePowerOff": a4ImmediatePowerOff,
       "a4ImmediateReset": a4ImmediateReset,
       "a4BroadcastMessageOnNetwork": a4BroadcastMessageOnNetwork,
       "a4AmsAlertName": a4AmsAlertName,
       "a4Enabled": a4Enabled,
       "tActionsTableForStandardIndications": tActionsTableForStandardIndications,
       "eActionsTableForStandardIndications": eActionsTableForStandardIndications,
       "a10RelatedMif": a10RelatedMif,
       "a10EventGenerationGroup": a10EventGenerationGroup,
       "a10EventType": a10EventType,
       "a10Instance": a10Instance,
       "a10Reserved": a10Reserved,
       "a10Severity": a10Severity,
       "a10BeepSpeaker": a10BeepSpeaker,
       "a10DisplayAlertMessageOnConsole": a10DisplayAlertMessageOnConsole,
       "a10LogToDisk": a10LogToDisk,
       "a10WriteToLcd": a10WriteToLcd,
       "a10ShutdownTheOs": a10ShutdownTheOs,
       "a10ShutdownAndPowerOffTheSystem": a10ShutdownAndPowerOffTheSystem,
       "a10ShutdownAndResetTheSystem": a10ShutdownAndResetTheSystem,
       "a10ImmediatePowerOff": a10ImmediatePowerOff,
       "a10ImmediateReset": a10ImmediateReset,
       "a10BroadcastMessageOnNetwork": a10BroadcastMessageOnNetwork,
       "a10AmsAlertName": a10AmsAlertName,
       "a10ImmediateNmi": a10ImmediateNmi,
       "a10Page": a10Page,
       "a10Email": a10Email,
       "a10Enabled": a10Enabled,
       "a10EventSystem": a10EventSystem,
       "a10EventSub-system": a10EventSub_system,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap}
)
