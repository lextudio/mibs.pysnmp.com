# SNMP MIB module (Olicom-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Olicom-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:52 2024
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
    "NotificationType",
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class IPXAddress(OctetString):
    """Custom type IPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Olicom_ObjectIdentity = ObjectIdentity
olicom = _Olicom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 1)
)
_InfoHardwareProductId_Type = DisplayString
_InfoHardwareProductId_Object = MibScalar
infoHardwareProductId = _InfoHardwareProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 1),
    _InfoHardwareProductId_Type()
)
infoHardwareProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareProductId.setStatus("mandatory")
_InfoHardwareVersion_Type = DisplayString
_InfoHardwareVersion_Object = MibScalar
infoHardwareVersion = _InfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 2),
    _InfoHardwareVersion_Type()
)
infoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareVersion.setStatus("mandatory")
_InfoHardwareECOLevel_Type = DisplayString
_InfoHardwareECOLevel_Object = MibScalar
infoHardwareECOLevel = _InfoHardwareECOLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 3),
    _InfoHardwareECOLevel_Type()
)
infoHardwareECOLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareECOLevel.setStatus("mandatory")
_InfoHardwareSerialNumber_Type = DisplayString
_InfoHardwareSerialNumber_Object = MibScalar
infoHardwareSerialNumber = _InfoHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 4),
    _InfoHardwareSerialNumber_Type()
)
infoHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareSerialNumber.setStatus("mandatory")
_InfoHardwareOptionTable_Object = MibTable
infoHardwareOptionTable = _InfoHardwareOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 5)
)
if mibBuilder.loadTexts:
    infoHardwareOptionTable.setStatus("mandatory")
_InfoHardwareOptionTableEntry_Object = MibTableRow
infoHardwareOptionTableEntry = _InfoHardwareOptionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 5, 1)
)
infoHardwareOptionTableEntry.setIndexNames(
    (0, "Olicom-MIB", "infoHardwareOptionNo"),
)
if mibBuilder.loadTexts:
    infoHardwareOptionTableEntry.setStatus("mandatory")
_InfoHardwareOptionNo_Type = Integer32
_InfoHardwareOptionNo_Object = MibTableColumn
infoHardwareOptionNo = _InfoHardwareOptionNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 5, 1, 1),
    _InfoHardwareOptionNo_Type()
)
infoHardwareOptionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareOptionNo.setStatus("mandatory")
_InfoHardwareOption_Type = DisplayString
_InfoHardwareOption_Object = MibTableColumn
infoHardwareOption = _InfoHardwareOption_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 5, 1, 2),
    _InfoHardwareOption_Type()
)
infoHardwareOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareOption.setStatus("mandatory")
_InfoSoftwareProductId_Type = DisplayString
_InfoSoftwareProductId_Object = MibScalar
infoSoftwareProductId = _InfoSoftwareProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 6),
    _InfoSoftwareProductId_Type()
)
infoSoftwareProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareProductId.setStatus("mandatory")
_InfoSoftwareVersion_Type = DisplayString
_InfoSoftwareVersion_Object = MibScalar
infoSoftwareVersion = _InfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 7),
    _InfoSoftwareVersion_Type()
)
infoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVersion.setStatus("mandatory")
_InfoSoftwareECOLevel_Type = DisplayString
_InfoSoftwareECOLevel_Object = MibScalar
infoSoftwareECOLevel = _InfoSoftwareECOLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 8),
    _InfoSoftwareECOLevel_Type()
)
infoSoftwareECOLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareECOLevel.setStatus("mandatory")
_InfoSoftwareOptionTable_Object = MibTable
infoSoftwareOptionTable = _InfoSoftwareOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 9)
)
if mibBuilder.loadTexts:
    infoSoftwareOptionTable.setStatus("mandatory")
_InfoSoftwareOptionTableEntry_Object = MibTableRow
infoSoftwareOptionTableEntry = _InfoSoftwareOptionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 9, 1)
)
infoSoftwareOptionTableEntry.setIndexNames(
    (0, "Olicom-MIB", "infoSoftwareOptionNo"),
)
if mibBuilder.loadTexts:
    infoSoftwareOptionTableEntry.setStatus("mandatory")
_InfoSoftwareOptionNo_Type = Integer32
_InfoSoftwareOptionNo_Object = MibTableColumn
infoSoftwareOptionNo = _InfoSoftwareOptionNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 9, 1, 1),
    _InfoSoftwareOptionNo_Type()
)
infoSoftwareOptionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareOptionNo.setStatus("mandatory")
_InfoSoftwareOption_Type = DisplayString
_InfoSoftwareOption_Object = MibTableColumn
infoSoftwareOption = _InfoSoftwareOption_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 9, 1, 2),
    _InfoSoftwareOption_Type()
)
infoSoftwareOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareOption.setStatus("mandatory")
_InfoSoftwareMIBsTable_Object = MibTable
infoSoftwareMIBsTable = _InfoSoftwareMIBsTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 10)
)
if mibBuilder.loadTexts:
    infoSoftwareMIBsTable.setStatus("mandatory")
_InfoSoftwareMIBsTableEntry_Object = MibTableRow
infoSoftwareMIBsTableEntry = _InfoSoftwareMIBsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 10, 1)
)
infoSoftwareMIBsTableEntry.setIndexNames(
    (0, "Olicom-MIB", "infoSoftwareMIBsNo"),
)
if mibBuilder.loadTexts:
    infoSoftwareMIBsTableEntry.setStatus("mandatory")
_InfoSoftwareMIBsNo_Type = Integer32
_InfoSoftwareMIBsNo_Object = MibTableColumn
infoSoftwareMIBsNo = _InfoSoftwareMIBsNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 10, 1, 1),
    _InfoSoftwareMIBsNo_Type()
)
infoSoftwareMIBsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareMIBsNo.setStatus("mandatory")
_InfoSoftwareMIBsObjectID_Type = ObjectIdentifier
_InfoSoftwareMIBsObjectID_Object = MibTableColumn
infoSoftwareMIBsObjectID = _InfoSoftwareMIBsObjectID_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 10, 1, 2),
    _InfoSoftwareMIBsObjectID_Type()
)
infoSoftwareMIBsObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareMIBsObjectID.setStatus("mandatory")
_InfoSoftwareMIBsDescription_Type = DisplayString
_InfoSoftwareMIBsDescription_Object = MibTableColumn
infoSoftwareMIBsDescription = _InfoSoftwareMIBsDescription_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 10, 1, 3),
    _InfoSoftwareMIBsDescription_Type()
)
infoSoftwareMIBsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareMIBsDescription.setStatus("mandatory")
_InfoXtraSwTable_Object = MibTable
infoXtraSwTable = _InfoXtraSwTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11)
)
if mibBuilder.loadTexts:
    infoXtraSwTable.setStatus("optional")
_InfoXtraSwEntry_Object = MibTableRow
infoXtraSwEntry = _InfoXtraSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1)
)
infoXtraSwEntry.setIndexNames(
    (0, "Olicom-MIB", "infoXtraSwIndex"),
)
if mibBuilder.loadTexts:
    infoXtraSwEntry.setStatus("optional")
_InfoXtraSwIndex_Type = Integer32
_InfoXtraSwIndex_Object = MibTableColumn
infoXtraSwIndex = _InfoXtraSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 1),
    _InfoXtraSwIndex_Type()
)
infoXtraSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwIndex.setStatus("optional")
_InfoXtraSwFileUse_Type = Integer32
_InfoXtraSwFileUse_Object = MibTableColumn
infoXtraSwFileUse = _InfoXtraSwFileUse_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 2),
    _InfoXtraSwFileUse_Type()
)
infoXtraSwFileUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwFileUse.setStatus("optional")
_InfoXtraSwProductId_Type = DisplayString
_InfoXtraSwProductId_Object = MibTableColumn
infoXtraSwProductId = _InfoXtraSwProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 3),
    _InfoXtraSwProductId_Type()
)
infoXtraSwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwProductId.setStatus("optional")
_InfoXtraSwVersion_Type = DisplayString
_InfoXtraSwVersion_Object = MibTableColumn
infoXtraSwVersion = _InfoXtraSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 4),
    _InfoXtraSwVersion_Type()
)
infoXtraSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwVersion.setStatus("optional")
_InfoXtraSwEcoLevel_Type = DisplayString
_InfoXtraSwEcoLevel_Object = MibTableColumn
infoXtraSwEcoLevel = _InfoXtraSwEcoLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 5),
    _InfoXtraSwEcoLevel_Type()
)
infoXtraSwEcoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwEcoLevel.setStatus("optional")
_InfoXtraSwSerialNumber_Type = DisplayString
_InfoXtraSwSerialNumber_Object = MibTableColumn
infoXtraSwSerialNumber = _InfoXtraSwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 6),
    _InfoXtraSwSerialNumber_Type()
)
infoXtraSwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwSerialNumber.setStatus("optional")
_InfoXtraSwOptions_Type = OctetString
_InfoXtraSwOptions_Object = MibTableColumn
infoXtraSwOptions = _InfoXtraSwOptions_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 11, 1, 7),
    _InfoXtraSwOptions_Type()
)
infoXtraSwOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoXtraSwOptions.setStatus("optional")
_InfoModuleTable_Object = MibTable
infoModuleTable = _InfoModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12)
)
if mibBuilder.loadTexts:
    infoModuleTable.setStatus("mandatory")
_InfoModuleEntry_Object = MibTableRow
infoModuleEntry = _InfoModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1)
)
infoModuleEntry.setIndexNames(
    (0, "Olicom-MIB", "infoModuleIndex"),
)
if mibBuilder.loadTexts:
    infoModuleEntry.setStatus("mandatory")
_InfoModuleIndex_Type = Integer32
_InfoModuleIndex_Object = MibTableColumn
infoModuleIndex = _InfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1, 1),
    _InfoModuleIndex_Type()
)
infoModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModuleIndex.setStatus("mandatory")
_InfoModuleHwProductId_Type = DisplayString
_InfoModuleHwProductId_Object = MibTableColumn
infoModuleHwProductId = _InfoModuleHwProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1, 2),
    _InfoModuleHwProductId_Type()
)
infoModuleHwProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModuleHwProductId.setStatus("mandatory")
_InfoModuleHwVersion_Type = DisplayString
_InfoModuleHwVersion_Object = MibTableColumn
infoModuleHwVersion = _InfoModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1, 3),
    _InfoModuleHwVersion_Type()
)
infoModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModuleHwVersion.setStatus("mandatory")
_InfoModuleHwSerialNumber_Type = DisplayString
_InfoModuleHwSerialNumber_Object = MibTableColumn
infoModuleHwSerialNumber = _InfoModuleHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1, 4),
    _InfoModuleHwSerialNumber_Type()
)
infoModuleHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModuleHwSerialNumber.setStatus("mandatory")
_InfoModuleBootpromVersion_Type = DisplayString
_InfoModuleBootpromVersion_Object = MibTableColumn
infoModuleBootpromVersion = _InfoModuleBootpromVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 12, 1, 5),
    _InfoModuleBootpromVersion_Type()
)
infoModuleBootpromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModuleBootpromVersion.setStatus("mandatory")
_InfoSwImageTable_Object = MibTable
infoSwImageTable = _InfoSwImageTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13)
)
if mibBuilder.loadTexts:
    infoSwImageTable.setStatus("mandatory")
_InfoSwImageEntry_Object = MibTableRow
infoSwImageEntry = _InfoSwImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1)
)
infoSwImageEntry.setIndexNames(
    (0, "Olicom-MIB", "infoSwImageModuleIndex"),
    (0, "Olicom-MIB", "infoSwImageNo"),
)
if mibBuilder.loadTexts:
    infoSwImageEntry.setStatus("mandatory")
_InfoSwImageModuleIndex_Type = Integer32
_InfoSwImageModuleIndex_Object = MibTableColumn
infoSwImageModuleIndex = _InfoSwImageModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1, 1),
    _InfoSwImageModuleIndex_Type()
)
infoSwImageModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwImageModuleIndex.setStatus("mandatory")
_InfoSwImageNo_Type = Integer32
_InfoSwImageNo_Object = MibTableColumn
infoSwImageNo = _InfoSwImageNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1, 2),
    _InfoSwImageNo_Type()
)
infoSwImageNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwImageNo.setStatus("mandatory")
_InfoSwImageProductId_Type = DisplayString
_InfoSwImageProductId_Object = MibTableColumn
infoSwImageProductId = _InfoSwImageProductId_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1, 3),
    _InfoSwImageProductId_Type()
)
infoSwImageProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwImageProductId.setStatus("mandatory")
_InfoSwImageVersion_Type = DisplayString
_InfoSwImageVersion_Object = MibTableColumn
infoSwImageVersion = _InfoSwImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1, 4),
    _InfoSwImageVersion_Type()
)
infoSwImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwImageVersion.setStatus("mandatory")
_InfoSwImageDownloadTime_Type = Integer32
_InfoSwImageDownloadTime_Object = MibTableColumn
infoSwImageDownloadTime = _InfoSwImageDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 1, 13, 1, 5),
    _InfoSwImageDownloadTime_Type()
)
infoSwImageDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwImageDownloadTime.setStatus("mandatory")
_Ocmibs_ObjectIdentity = ObjectIdentity
ocmibs = _Ocmibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2)
)
_OcmibsBridgeMIB_ObjectIdentity = ObjectIdentity
ocmibsBridgeMIB = _OcmibsBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 1)
)
_OcmibsCauMIB_ObjectIdentity = ObjectIdentity
ocmibsCauMIB = _OcmibsCauMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 2)
)
_OcmibsCamMIB_ObjectIdentity = ObjectIdentity
ocmibsCamMIB = _OcmibsCamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 3)
)
_OcmibsEhubMIB_ObjectIdentity = ObjectIdentity
ocmibsEhubMIB = _OcmibsEhubMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 4)
)
_OcmibsOc8100MIB_ObjectIdentity = ObjectIdentity
ocmibsOc8100MIB = _OcmibsOc8100MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 5)
)
_OcmibsCrossfireAtmMIB_ObjectIdentity = ObjectIdentity
ocmibsCrossfireAtmMIB = _OcmibsCrossfireAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 6)
)
_OcmibsOc8200MIB_ObjectIdentity = ObjectIdentity
ocmibsOc8200MIB = _OcmibsOc8200MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 7)
)
_OcmibsOc8600MIB_ObjectIdentity = ObjectIdentity
ocmibsOc8600MIB = _OcmibsOc8600MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 8)
)
_OcmibsOc84x0MIB_ObjectIdentity = ObjectIdentity
ocmibsOc84x0MIB = _OcmibsOc84x0MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 9)
)
_OcmibsLanSwitchMIB_ObjectIdentity = ObjectIdentity
ocmibsLanSwitchMIB = _OcmibsLanSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 10)
)
_OcmibsVlanMIB_ObjectIdentity = ObjectIdentity
ocmibsVlanMIB = _OcmibsVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 11)
)
_OcmibsSmartStatusMIB_ObjectIdentity = ObjectIdentity
ocmibsSmartStatusMIB = _OcmibsSmartStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 12)
)
_OcmibsCf871xMIB_ObjectIdentity = ObjectIdentity
ocmibsCf871xMIB = _OcmibsCf871xMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 13)
)
_AtmUplinkMIB_ObjectIdentity = ObjectIdentity
atmUplinkMIB = _AtmUplinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 2, 14)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 3)
)
_LmpMib_ObjectIdentity = ObjectIdentity
lmpMib = _LmpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 3, 1)
)
_Inet_ObjectIdentity = ObjectIdentity
inet = _Inet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 4)
)


class _InetMacAddrForm_Type(Integer32):
    """Custom type inetMacAddrForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 1),
          ("non-canonical", 2))
    )


_InetMacAddrForm_Type.__name__ = "Integer32"
_InetMacAddrForm_Object = MibScalar
inetMacAddrForm = _InetMacAddrForm_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 1),
    _InetMacAddrForm_Type()
)
inetMacAddrForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetMacAddrForm.setStatus("mandatory")


class _InetEnableRwho_Type(Integer32):
    """Custom type inetEnableRwho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_InetEnableRwho_Type.__name__ = "Integer32"
_InetEnableRwho_Object = MibScalar
inetEnableRwho = _InetEnableRwho_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 2),
    _InetEnableRwho_Type()
)
inetEnableRwho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetEnableRwho.setStatus("mandatory")


class _InetEnableRIP_Type(Integer32):
    """Custom type inetEnableRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_InetEnableRIP_Type.__name__ = "Integer32"
_InetEnableRIP_Object = MibScalar
inetEnableRIP = _InetEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 3),
    _InetEnableRIP_Type()
)
inetEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetEnableRIP.setStatus("mandatory")
_InetCommunityMaxEntries_Type = Integer32
_InetCommunityMaxEntries_Object = MibScalar
inetCommunityMaxEntries = _InetCommunityMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 4),
    _InetCommunityMaxEntries_Type()
)
inetCommunityMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCommunityMaxEntries.setStatus("mandatory")
_InetCommunityTable_Object = MibTable
inetCommunityTable = _InetCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5)
)
if mibBuilder.loadTexts:
    inetCommunityTable.setStatus("mandatory")
_InetCommunityTableEntry_Object = MibTableRow
inetCommunityTableEntry = _InetCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1)
)
inetCommunityTableEntry.setIndexNames(
    (0, "Olicom-MIB", "inetCommunityNo"),
)
if mibBuilder.loadTexts:
    inetCommunityTableEntry.setStatus("mandatory")
_InetCommunityNo_Type = Integer32
_InetCommunityNo_Object = MibTableColumn
inetCommunityNo = _InetCommunityNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 1),
    _InetCommunityNo_Type()
)
inetCommunityNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCommunityNo.setStatus("mandatory")
_InetCommunityName_Type = DisplayString
_InetCommunityName_Object = MibTableColumn
inetCommunityName = _InetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 2),
    _InetCommunityName_Type()
)
inetCommunityName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityName.setStatus("mandatory")
_InetCommunityIPAddress_Type = IpAddress
_InetCommunityIPAddress_Object = MibTableColumn
inetCommunityIPAddress = _InetCommunityIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 3),
    _InetCommunityIPAddress_Type()
)
inetCommunityIPAddress.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityIPAddress.setStatus("mandatory")


class _InetCommunityAccess_Type(Integer32):
    """Custom type inetCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_InetCommunityAccess_Type.__name__ = "Integer32"
_InetCommunityAccess_Object = MibTableColumn
inetCommunityAccess = _InetCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 4),
    _InetCommunityAccess_Type()
)
inetCommunityAccess.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityAccess.setStatus("mandatory")
_InetCommunityDelete_Type = Integer32
_InetCommunityDelete_Object = MibTableColumn
inetCommunityDelete = _InetCommunityDelete_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 5),
    _InetCommunityDelete_Type()
)
inetCommunityDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityDelete.setStatus("mandatory")
_InetCommunityIPXAddress_Type = IPXAddress
_InetCommunityIPXAddress_Object = MibTableColumn
inetCommunityIPXAddress = _InetCommunityIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 6),
    _InetCommunityIPXAddress_Type()
)
inetCommunityIPXAddress.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityIPXAddress.setStatus("mandatory")
_InetCommunityTransportProtocols_Type = Integer32
_InetCommunityTransportProtocols_Object = MibTableColumn
inetCommunityTransportProtocols = _InetCommunityTransportProtocols_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 7),
    _InetCommunityTransportProtocols_Type()
)
inetCommunityTransportProtocols.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityTransportProtocols.setStatus("mandatory")
_InetCommunityMACAddress_Type = MacAddress
_InetCommunityMACAddress_Object = MibTableColumn
inetCommunityMACAddress = _InetCommunityMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 5, 1, 8),
    _InetCommunityMACAddress_Type()
)
inetCommunityMACAddress.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetCommunityMACAddress.setStatus("mandatory")
_InetTrapMaxEntries_Type = Integer32
_InetTrapMaxEntries_Object = MibScalar
inetTrapMaxEntries = _InetTrapMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 6),
    _InetTrapMaxEntries_Type()
)
inetTrapMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetTrapMaxEntries.setStatus("mandatory")
_InetTrapTable_Object = MibTable
inetTrapTable = _InetTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7)
)
if mibBuilder.loadTexts:
    inetTrapTable.setStatus("mandatory")
_InetTrapTableEntry_Object = MibTableRow
inetTrapTableEntry = _InetTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1)
)
inetTrapTableEntry.setIndexNames(
    (0, "Olicom-MIB", "inetTrapIndex"),
)
if mibBuilder.loadTexts:
    inetTrapTableEntry.setStatus("mandatory")
_InetTrapCommunity_Type = DisplayString
_InetTrapCommunity_Object = MibTableColumn
inetTrapCommunity = _InetTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 1),
    _InetTrapCommunity_Type()
)
inetTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapCommunity.setStatus("mandatory")
_InetTrapDestIPAddress_Type = IpAddress
_InetTrapDestIPAddress_Object = MibTableColumn
inetTrapDestIPAddress = _InetTrapDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 2),
    _InetTrapDestIPAddress_Type()
)
inetTrapDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapDestIPAddress.setStatus("mandatory")
_InetTrapEventDisableMask_Type = OctetString
_InetTrapEventDisableMask_Object = MibTableColumn
inetTrapEventDisableMask = _InetTrapEventDisableMask_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 3),
    _InetTrapEventDisableMask_Type()
)
inetTrapEventDisableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapEventDisableMask.setStatus("deprecated")
_InetTrapDelete_Type = Integer32
_InetTrapDelete_Object = MibTableColumn
inetTrapDelete = _InetTrapDelete_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 4),
    _InetTrapDelete_Type()
)
inetTrapDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    inetTrapDelete.setStatus("mandatory")


class _InetTrapDestUDPPort_Type(Integer32):
    """Custom type inetTrapDestUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_InetTrapDestUDPPort_Type.__name__ = "Integer32"
_InetTrapDestUDPPort_Object = MibTableColumn
inetTrapDestUDPPort = _InetTrapDestUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 5),
    _InetTrapDestUDPPort_Type()
)
inetTrapDestUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapDestUDPPort.setStatus("mandatory")
_InetTrapIndex_Type = Integer32
_InetTrapIndex_Object = MibTableColumn
inetTrapIndex = _InetTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 6),
    _InetTrapIndex_Type()
)
inetTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetTrapIndex.setStatus("mandatory")
_InetTrapDestIPXAddress_Type = IPXAddress
_InetTrapDestIPXAddress_Object = MibTableColumn
inetTrapDestIPXAddress = _InetTrapDestIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 7),
    _InetTrapDestIPXAddress_Type()
)
inetTrapDestIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapDestIPXAddress.setStatus("mandatory")
_InetTrapTransportProtocols_Type = Integer32
_InetTrapTransportProtocols_Object = MibTableColumn
inetTrapTransportProtocols = _InetTrapTransportProtocols_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 8),
    _InetTrapTransportProtocols_Type()
)
inetTrapTransportProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapTransportProtocols.setStatus("mandatory")


class _InetTrapIPEncapsulation_Type(Integer32):
    """Custom type inetTrapIPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_InetTrapIPEncapsulation_Type.__name__ = "Integer32"
_InetTrapIPEncapsulation_Object = MibTableColumn
inetTrapIPEncapsulation = _InetTrapIPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 9),
    _InetTrapIPEncapsulation_Type()
)
inetTrapIPEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapIPEncapsulation.setStatus("mandatory")


class _InetTrapIPXEncapsulation_Type(Integer32):
    """Custom type inetTrapIPXEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_InetTrapIPXEncapsulation_Type.__name__ = "Integer32"
_InetTrapIPXEncapsulation_Object = MibTableColumn
inetTrapIPXEncapsulation = _InetTrapIPXEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 7, 1, 10),
    _InetTrapIPXEncapsulation_Type()
)
inetTrapIPXEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetTrapIPXEncapsulation.setStatus("mandatory")


class _InetDefaultIPEncapsulation_Type(Integer32):
    """Custom type inetDefaultIPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_InetDefaultIPEncapsulation_Type.__name__ = "Integer32"
_InetDefaultIPEncapsulation_Object = MibScalar
inetDefaultIPEncapsulation = _InetDefaultIPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 8),
    _InetDefaultIPEncapsulation_Type()
)
inetDefaultIPEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetDefaultIPEncapsulation.setStatus("mandatory")


class _InetDefaultIPXEncapsulation_Type(Integer32):
    """Custom type inetDefaultIPXEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_InetDefaultIPXEncapsulation_Type.__name__ = "Integer32"
_InetDefaultIPXEncapsulation_Object = MibScalar
inetDefaultIPXEncapsulation = _InetDefaultIPXEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 9),
    _InetDefaultIPXEncapsulation_Type()
)
inetDefaultIPXEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetDefaultIPXEncapsulation.setStatus("mandatory")
_InetIPAddressTable_Object = MibTable
inetIPAddressTable = _InetIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10)
)
if mibBuilder.loadTexts:
    inetIPAddressTable.setStatus("mandatory")
_InetIPAddressEntry_Object = MibTableRow
inetIPAddressEntry = _InetIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1)
)
inetIPAddressEntry.setIndexNames(
    (0, "Olicom-MIB", "inetIPAddressIfNumber"),
)
if mibBuilder.loadTexts:
    inetIPAddressEntry.setStatus("mandatory")
_InetIPAddressIfNumber_Type = Integer32
_InetIPAddressIfNumber_Object = MibTableColumn
inetIPAddressIfNumber = _InetIPAddressIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 1),
    _InetIPAddressIfNumber_Type()
)
inetIPAddressIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetIPAddressIfNumber.setStatus("mandatory")
_InetIPAddressIPAddress_Type = IpAddress
_InetIPAddressIPAddress_Object = MibTableColumn
inetIPAddressIPAddress = _InetIPAddressIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 2),
    _InetIPAddressIPAddress_Type()
)
inetIPAddressIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressIPAddress.setStatus("mandatory")
_InetIPAddressNetmask_Type = IpAddress
_InetIPAddressNetmask_Object = MibTableColumn
inetIPAddressNetmask = _InetIPAddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 3),
    _InetIPAddressNetmask_Type()
)
inetIPAddressNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressNetmask.setStatus("mandatory")
_InetIPAddressDefaultGateway_Type = IpAddress
_InetIPAddressDefaultGateway_Object = MibTableColumn
inetIPAddressDefaultGateway = _InetIPAddressDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 4),
    _InetIPAddressDefaultGateway_Type()
)
inetIPAddressDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressDefaultGateway.setStatus("mandatory")


class _InetIPAddressEnableRwho_Type(Integer32):
    """Custom type inetIPAddressEnableRwho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_InetIPAddressEnableRwho_Type.__name__ = "Integer32"
_InetIPAddressEnableRwho_Object = MibTableColumn
inetIPAddressEnableRwho = _InetIPAddressEnableRwho_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 5),
    _InetIPAddressEnableRwho_Type()
)
inetIPAddressEnableRwho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressEnableRwho.setStatus("optional")


class _InetIPAddressEnableRIP_Type(Integer32):
    """Custom type inetIPAddressEnableRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_InetIPAddressEnableRIP_Type.__name__ = "Integer32"
_InetIPAddressEnableRIP_Object = MibTableColumn
inetIPAddressEnableRIP = _InetIPAddressEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 6),
    _InetIPAddressEnableRIP_Type()
)
inetIPAddressEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressEnableRIP.setStatus("optional")


class _InetIPAddressIPEncapsulation_Type(Integer32):
    """Custom type inetIPAddressIPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("media-default", 4),
          ("snap", 3))
    )


_InetIPAddressIPEncapsulation_Type.__name__ = "Integer32"
_InetIPAddressIPEncapsulation_Object = MibTableColumn
inetIPAddressIPEncapsulation = _InetIPAddressIPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 10, 1, 7),
    _InetIPAddressIPEncapsulation_Type()
)
inetIPAddressIPEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetIPAddressIPEncapsulation.setStatus("mandatory")


class _InetSlipBaudrate_Type(Integer32):
    """Custom type inetSlipBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1),
          ("b19200", 5),
          ("b2400", 2),
          ("b38400", 6),
          ("b4800", 3),
          ("b9600", 4))
    )


_InetSlipBaudrate_Type.__name__ = "Integer32"
_InetSlipBaudrate_Object = MibScalar
inetSlipBaudrate = _InetSlipBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 11),
    _InetSlipBaudrate_Type()
)
inetSlipBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipBaudrate.setStatus("optional")


class _InetSlipParity_Type(Integer32):
    """Custom type inetSlipParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_InetSlipParity_Type.__name__ = "Integer32"
_InetSlipParity_Object = MibScalar
inetSlipParity = _InetSlipParity_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 12),
    _InetSlipParity_Type()
)
inetSlipParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipParity.setStatus("optional")


class _InetSlipStopbits_Type(Integer32):
    """Custom type inetSlipStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_InetSlipStopbits_Type.__name__ = "Integer32"
_InetSlipStopbits_Object = MibScalar
inetSlipStopbits = _InetSlipStopbits_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 13),
    _InetSlipStopbits_Type()
)
inetSlipStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipStopbits.setStatus("optional")


class _InetSlipModemInit_Type(DisplayString):
    """Custom type inetSlipModemInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InetSlipModemInit_Type.__name__ = "DisplayString"
_InetSlipModemInit_Object = MibScalar
inetSlipModemInit = _InetSlipModemInit_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 14),
    _InetSlipModemInit_Type()
)
inetSlipModemInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipModemInit.setStatus("optional")


class _InetSlipHeaderCompressionEnabled_Type(Integer32):
    """Custom type inetSlipHeaderCompressionEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_InetSlipHeaderCompressionEnabled_Type.__name__ = "Integer32"
_InetSlipHeaderCompressionEnabled_Object = MibScalar
inetSlipHeaderCompressionEnabled = _InetSlipHeaderCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 15),
    _InetSlipHeaderCompressionEnabled_Type()
)
inetSlipHeaderCompressionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipHeaderCompressionEnabled.setStatus("optional")
_InetSlipMaxMtuSize_Type = Integer32
_InetSlipMaxMtuSize_Object = MibScalar
inetSlipMaxMtuSize = _InetSlipMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 16),
    _InetSlipMaxMtuSize_Type()
)
inetSlipMaxMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipMaxMtuSize.setStatus("optional")
_InetSlipMaxMruSize_Type = Integer32
_InetSlipMaxMruSize_Object = MibScalar
inetSlipMaxMruSize = _InetSlipMaxMruSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 17),
    _InetSlipMaxMruSize_Type()
)
inetSlipMaxMruSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inetSlipMaxMruSize.setStatus("optional")


class _SCallbackEnable_Type(Integer32):
    """Custom type sCallbackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SCallbackEnable_Type.__name__ = "Integer32"
_SCallbackEnable_Object = MibScalar
sCallbackEnable = _SCallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 18),
    _SCallbackEnable_Type()
)
sCallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCallbackEnable.setStatus("deprecated")


class _SCallbackPhoneNumber_Type(DisplayString):
    """Custom type sCallbackPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SCallbackPhoneNumber_Type.__name__ = "DisplayString"
_SCallbackPhoneNumber_Object = MibScalar
sCallbackPhoneNumber = _SCallbackPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 19),
    _SCallbackPhoneNumber_Type()
)
sCallbackPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCallbackPhoneNumber.setStatus("deprecated")


class _SCalloutEnable_Type(Integer32):
    """Custom type sCalloutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SCalloutEnable_Type.__name__ = "Integer32"
_SCalloutEnable_Object = MibScalar
sCalloutEnable = _SCalloutEnable_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 20),
    _SCalloutEnable_Type()
)
sCalloutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCalloutEnable.setStatus("deprecated")


class _SCalloutPhoneNumber_Type(DisplayString):
    """Custom type sCalloutPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SCalloutPhoneNumber_Type.__name__ = "DisplayString"
_SCalloutPhoneNumber_Object = MibScalar
sCalloutPhoneNumber = _SCalloutPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 4, 21),
    _SCalloutPhoneNumber_Type()
)
sCalloutPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCalloutPhoneNumber.setStatus("deprecated")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 5)
)
_ControlRestart_Type = Integer32
_ControlRestart_Object = MibScalar
controlRestart = _ControlRestart_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 1),
    _ControlRestart_Type()
)
controlRestart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    controlRestart.setStatus("mandatory")
_ControlConfigChangeCounter_Type = Integer32
_ControlConfigChangeCounter_Object = MibScalar
controlConfigChangeCounter = _ControlConfigChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 2),
    _ControlConfigChangeCounter_Type()
)
controlConfigChangeCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlConfigChangeCounter.setStatus("mandatory")
_ControlTrapTable_Object = MibTable
controlTrapTable = _ControlTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3)
)
if mibBuilder.loadTexts:
    controlTrapTable.setStatus("mandatory")
_ControlTrapTableEntry_Object = MibTableRow
controlTrapTableEntry = _ControlTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1)
)
controlTrapTableEntry.setIndexNames(
    (0, "Olicom-MIB", "controlTrapIndex"),
    (0, "Olicom-MIB", "controlTrapMIBIndex"),
    (0, "Olicom-MIB", "controlTrapNumber"),
)
if mibBuilder.loadTexts:
    controlTrapTableEntry.setStatus("mandatory")
_ControlTrapIndex_Type = Integer32
_ControlTrapIndex_Object = MibTableColumn
controlTrapIndex = _ControlTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1, 1),
    _ControlTrapIndex_Type()
)
controlTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTrapIndex.setStatus("mandatory")
_ControlTrapMIBIndex_Type = Integer32
_ControlTrapMIBIndex_Object = MibTableColumn
controlTrapMIBIndex = _ControlTrapMIBIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1, 2),
    _ControlTrapMIBIndex_Type()
)
controlTrapMIBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTrapMIBIndex.setStatus("mandatory")
_ControlTrapNumber_Type = Integer32
_ControlTrapNumber_Object = MibTableColumn
controlTrapNumber = _ControlTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1, 3),
    _ControlTrapNumber_Type()
)
controlTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTrapNumber.setStatus("mandatory")
_ControlTrapDescription_Type = DisplayString
_ControlTrapDescription_Object = MibTableColumn
controlTrapDescription = _ControlTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1, 4),
    _ControlTrapDescription_Type()
)
controlTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTrapDescription.setStatus("mandatory")


class _ControlTrapGeneration_Type(Integer32):
    """Custom type controlTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("never", 1))
    )


_ControlTrapGeneration_Type.__name__ = "Integer32"
_ControlTrapGeneration_Object = MibTableColumn
controlTrapGeneration = _ControlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 3, 1, 5),
    _ControlTrapGeneration_Type()
)
controlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTrapGeneration.setStatus("mandatory")


class _ControlLoadProtocol_Type(Integer32):
    """Custom type controlLoadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bootp-tftp", 3),
          ("ibm-hlm", 2),
          ("ibm-rpl", 1),
          ("olicom-remote-software-update", 5),
          ("olicom-rpl", 4))
    )


_ControlLoadProtocol_Type.__name__ = "Integer32"
_ControlLoadProtocol_Object = MibScalar
controlLoadProtocol = _ControlLoadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 4),
    _ControlLoadProtocol_Type()
)
controlLoadProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadProtocol.setStatus("mandatory")


class _ControlLoadFilename_Type(DisplayString):
    """Custom type controlLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ControlLoadFilename_Type.__name__ = "DisplayString"
_ControlLoadFilename_Object = MibScalar
controlLoadFilename = _ControlLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 5),
    _ControlLoadFilename_Type()
)
controlLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadFilename.setStatus("mandatory")
_ControlLoadServerMACAddress_Type = MacAddress
_ControlLoadServerMACAddress_Object = MibScalar
controlLoadServerMACAddress = _ControlLoadServerMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 6),
    _ControlLoadServerMACAddress_Type()
)
controlLoadServerMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadServerMACAddress.setStatus("optional")
_ControlLoadServerIPAddress_Type = IpAddress
_ControlLoadServerIPAddress_Object = MibScalar
controlLoadServerIPAddress = _ControlLoadServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 7),
    _ControlLoadServerIPAddress_Type()
)
controlLoadServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadServerIPAddress.setStatus("optional")
_ControlLoadServerIPXAddress_Type = IPXAddress
_ControlLoadServerIPXAddress_Object = MibScalar
controlLoadServerIPXAddress = _ControlLoadServerIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 8),
    _ControlLoadServerIPXAddress_Type()
)
controlLoadServerIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadServerIPXAddress.setStatus("optional")


class _ControlLoadStart_Type(Integer32):
    """Custom type controlLoadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("badFile", 8),
          ("completed", 5),
          ("finishing", 4),
          ("flashFailure", 7),
          ("inProgress", 3),
          ("notInitiated", 1),
          ("protocolFailure", 6),
          ("starting", 2))
    )


_ControlLoadStart_Type.__name__ = "Integer32"
_ControlLoadStart_Object = MibScalar
controlLoadStart = _ControlLoadStart_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 9),
    _ControlLoadStart_Type()
)
controlLoadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLoadStart.setStatus("mandatory")
_ControlTime_Type = Integer32
_ControlTime_Object = MibScalar
controlTime = _ControlTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 10),
    _ControlTime_Type()
)
controlTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTime.setStatus("mandatory")


class _ControlEnableRmon_Type(Integer32):
    """Custom type controlEnableRmon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ControlEnableRmon_Type.__name__ = "Integer32"
_ControlEnableRmon_Object = MibScalar
controlEnableRmon = _ControlEnableRmon_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 11),
    _ControlEnableRmon_Type()
)
controlEnableRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlEnableRmon.setStatus("optional")


class _ControlAutoRestart_Type(Integer32):
    """Custom type controlAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ControlAutoRestart_Type.__name__ = "Integer32"
_ControlAutoRestart_Object = MibScalar
controlAutoRestart = _ControlAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 12),
    _ControlAutoRestart_Type()
)
controlAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlAutoRestart.setStatus("optional")
_ControlSwAdminStatus_Type = Integer32
_ControlSwAdminStatus_Object = MibScalar
controlSwAdminStatus = _ControlSwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 13),
    _ControlSwAdminStatus_Type()
)
controlSwAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSwAdminStatus.setStatus("optional")
_ControlFlashConfigSize_Type = Integer32
_ControlFlashConfigSize_Object = MibScalar
controlFlashConfigSize = _ControlFlashConfigSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 15),
    _ControlFlashConfigSize_Type()
)
controlFlashConfigSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlFlashConfigSize.setStatus("optional")
_ControlFlashConfigFree_Type = Integer32
_ControlFlashConfigFree_Object = MibScalar
controlFlashConfigFree = _ControlFlashConfigFree_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 16),
    _ControlFlashConfigFree_Type()
)
controlFlashConfigFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlFlashConfigFree.setStatus("optional")


class _ControlFlashConfigState_Type(Integer32):
    """Custom type controlFlashConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("acceptTemporary", 6),
          ("corrupted", 3),
          ("default", 2),
          ("normal", 1),
          ("rejectTemporary", 7),
          ("rewrite", 8),
          ("temporary", 4),
          ("testTemporary", 5))
    )


_ControlFlashConfigState_Type.__name__ = "Integer32"
_ControlFlashConfigState_Object = MibScalar
controlFlashConfigState = _ControlFlashConfigState_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 17),
    _ControlFlashConfigState_Type()
)
controlFlashConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlFlashConfigState.setStatus("optional")
_ControlDelayedRestart_Type = Integer32
_ControlDelayedRestart_Object = MibScalar
controlDelayedRestart = _ControlDelayedRestart_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 18),
    _ControlDelayedRestart_Type()
)
controlDelayedRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlDelayedRestart.setStatus("mandatory")
_ControlLoadProggress_Type = Integer32
_ControlLoadProggress_Object = MibScalar
controlLoadProggress = _ControlLoadProggress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 19),
    _ControlLoadProggress_Type()
)
controlLoadProggress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLoadProggress.setStatus("mandatory")
_ControlLoadFileSize_Type = Integer32
_ControlLoadFileSize_Object = MibScalar
controlLoadFileSize = _ControlLoadFileSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 20),
    _ControlLoadFileSize_Type()
)
controlLoadFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLoadFileSize.setStatus("mandatory")
_ControlTftpClient_ObjectIdentity = ObjectIdentity
controlTftpClient = _ControlTftpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 5, 21)
)
_ControlTftpMaxSessions_Type = Integer32
_ControlTftpMaxSessions_Object = MibScalar
controlTftpMaxSessions = _ControlTftpMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 1),
    _ControlTftpMaxSessions_Type()
)
controlTftpMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpMaxSessions.setStatus("optional")
_ControlTftpNextSessionIndex_Type = Integer32
_ControlTftpNextSessionIndex_Object = MibScalar
controlTftpNextSessionIndex = _ControlTftpNextSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 2),
    _ControlTftpNextSessionIndex_Type()
)
controlTftpNextSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpNextSessionIndex.setStatus("optional")
_ControlTftpSessionTable_Object = MibTable
controlTftpSessionTable = _ControlTftpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3)
)
if mibBuilder.loadTexts:
    controlTftpSessionTable.setStatus("optional")
_ControlTftpSessionEntry_Object = MibTableRow
controlTftpSessionEntry = _ControlTftpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1)
)
controlTftpSessionEntry.setIndexNames(
    (0, "Olicom-MIB", "controlTftpSessionIndex"),
)
if mibBuilder.loadTexts:
    controlTftpSessionEntry.setStatus("mandatory")
_ControlTftpSessionIndex_Type = Integer32
_ControlTftpSessionIndex_Object = MibTableColumn
controlTftpSessionIndex = _ControlTftpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 1),
    _ControlTftpSessionIndex_Type()
)
controlTftpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpSessionIndex.setStatus("mandatory")
_ControlTftpSessionRowStatus_Type = RowStatus
_ControlTftpSessionRowStatus_Object = MibTableColumn
controlTftpSessionRowStatus = _ControlTftpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 2),
    _ControlTftpSessionRowStatus_Type()
)
controlTftpSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTftpSessionRowStatus.setStatus("mandatory")


class _ControlTftpSessionDirection_Type(Integer32):
    """Custom type controlTftpSessionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ControlTftpSessionDirection_Type.__name__ = "Integer32"
_ControlTftpSessionDirection_Object = MibTableColumn
controlTftpSessionDirection = _ControlTftpSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 3),
    _ControlTftpSessionDirection_Type()
)
controlTftpSessionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTftpSessionDirection.setStatus("mandatory")
_ControlTftpSessionServerAddress_Type = IpAddress
_ControlTftpSessionServerAddress_Object = MibTableColumn
controlTftpSessionServerAddress = _ControlTftpSessionServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 4),
    _ControlTftpSessionServerAddress_Type()
)
controlTftpSessionServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTftpSessionServerAddress.setStatus("mandatory")
_ControlTftpSessionServerFile_Type = DisplayString
_ControlTftpSessionServerFile_Object = MibTableColumn
controlTftpSessionServerFile = _ControlTftpSessionServerFile_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 5),
    _ControlTftpSessionServerFile_Type()
)
controlTftpSessionServerFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTftpSessionServerFile.setStatus("mandatory")
_ControlTftpSessionLocalFile_Type = DisplayString
_ControlTftpSessionLocalFile_Object = MibTableColumn
controlTftpSessionLocalFile = _ControlTftpSessionLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 6),
    _ControlTftpSessionLocalFile_Type()
)
controlTftpSessionLocalFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTftpSessionLocalFile.setStatus("mandatory")


class _ControlTftpSessionStatus_Type(Integer32):
    """Custom type controlTftpSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("badFile", 8),
          ("completed", 5),
          ("finishing", 4),
          ("flashFailure", 7),
          ("inProgress", 3),
          ("notInitiated", 1),
          ("protocolFailure", 6),
          ("starting", 2))
    )


_ControlTftpSessionStatus_Type.__name__ = "Integer32"
_ControlTftpSessionStatus_Object = MibTableColumn
controlTftpSessionStatus = _ControlTftpSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 7),
    _ControlTftpSessionStatus_Type()
)
controlTftpSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpSessionStatus.setStatus("mandatory")
_ControlTftpSessionProgress_Type = Integer32
_ControlTftpSessionProgress_Object = MibTableColumn
controlTftpSessionProgress = _ControlTftpSessionProgress_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 8),
    _ControlTftpSessionProgress_Type()
)
controlTftpSessionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpSessionProgress.setStatus("mandatory")
_ControlTftpSessionFileSize_Type = Integer32
_ControlTftpSessionFileSize_Object = MibTableColumn
controlTftpSessionFileSize = _ControlTftpSessionFileSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 21, 3, 1, 9),
    _ControlTftpSessionFileSize_Type()
)
controlTftpSessionFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlTftpSessionFileSize.setStatus("mandatory")


class _ControlRestartType_Type(Integer32):
    """Custom type controlRestartType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("soft", 1))
    )


_ControlRestartType_Type.__name__ = "Integer32"
_ControlRestartType_Object = MibScalar
controlRestartType = _ControlRestartType_Object(
    (1, 3, 6, 1, 4, 1, 285, 5, 22),
    _ControlRestartType_Type()
)
controlRestartType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRestartType.setStatus("mandatory")
_Obm_ObjectIdentity = ObjectIdentity
obm = _Obm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 6)
)


class _ObmEnable_Type(Integer32):
    """Custom type obmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ObmEnable_Type.__name__ = "Integer32"
_ObmEnable_Object = MibScalar
obmEnable = _ObmEnable_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 1),
    _ObmEnable_Type()
)
obmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmEnable.setStatus("mandatory")


class _ObmPassword_Type(DisplayString):
    """Custom type obmPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ObmPassword_Type.__name__ = "DisplayString"
_ObmPassword_Object = MibScalar
obmPassword = _ObmPassword_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 2),
    _ObmPassword_Type()
)
obmPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmPassword.setStatus("mandatory")


class _ObmBaudrate_Type(Integer32):
    """Custom type obmBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto", 12),
          ("b115200", 8),
          ("b1200", 1),
          ("b19200", 5),
          ("b230400", 9),
          ("b2400", 2),
          ("b38400", 6),
          ("b460800", 10),
          ("b4800", 3),
          ("b57600", 7),
          ("b921600", 11),
          ("b9600", 4))
    )


_ObmBaudrate_Type.__name__ = "Integer32"
_ObmBaudrate_Object = MibScalar
obmBaudrate = _ObmBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 3),
    _ObmBaudrate_Type()
)
obmBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmBaudrate.setStatus("mandatory")


class _ObmParity_Type(Integer32):
    """Custom type obmParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_ObmParity_Type.__name__ = "Integer32"
_ObmParity_Object = MibScalar
obmParity = _ObmParity_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 4),
    _ObmParity_Type()
)
obmParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmParity.setStatus("mandatory")


class _ObmStopbits_Type(Integer32):
    """Custom type obmStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_ObmStopbits_Type.__name__ = "Integer32"
_ObmStopbits_Object = MibScalar
obmStopbits = _ObmStopbits_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 5),
    _ObmStopbits_Type()
)
obmStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmStopbits.setStatus("mandatory")


class _ObmModemInit_Type(DisplayString):
    """Custom type obmModemInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ObmModemInit_Type.__name__ = "DisplayString"
_ObmModemInit_Object = MibScalar
obmModemInit = _ObmModemInit_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 6),
    _ObmModemInit_Type()
)
obmModemInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmModemInit.setStatus("mandatory")


class _ObmCallbackEnable_Type(Integer32):
    """Custom type obmCallbackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ObmCallbackEnable_Type.__name__ = "Integer32"
_ObmCallbackEnable_Object = MibScalar
obmCallbackEnable = _ObmCallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 7),
    _ObmCallbackEnable_Type()
)
obmCallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCallbackEnable.setStatus("mandatory")


class _ObmCallbackPhoneNumber_Type(DisplayString):
    """Custom type obmCallbackPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ObmCallbackPhoneNumber_Type.__name__ = "DisplayString"
_ObmCallbackPhoneNumber_Object = MibScalar
obmCallbackPhoneNumber = _ObmCallbackPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 8),
    _ObmCallbackPhoneNumber_Type()
)
obmCallbackPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCallbackPhoneNumber.setStatus("mandatory")


class _ObmCalloutEnable_Type(Integer32):
    """Custom type obmCalloutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ObmCalloutEnable_Type.__name__ = "Integer32"
_ObmCalloutEnable_Object = MibScalar
obmCalloutEnable = _ObmCalloutEnable_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 9),
    _ObmCalloutEnable_Type()
)
obmCalloutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCalloutEnable.setStatus("mandatory")


class _ObmCalloutPhoneNumber_Type(DisplayString):
    """Custom type obmCalloutPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ObmCalloutPhoneNumber_Type.__name__ = "DisplayString"
_ObmCalloutPhoneNumber_Object = MibScalar
obmCalloutPhoneNumber = _ObmCalloutPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 10),
    _ObmCalloutPhoneNumber_Type()
)
obmCalloutPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCalloutPhoneNumber.setStatus("mandatory")
_ObmCalloutTriggerEvent_Type = OctetString
_ObmCalloutTriggerEvent_Object = MibScalar
obmCalloutTriggerEvent = _ObmCalloutTriggerEvent_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 11),
    _ObmCalloutTriggerEvent_Type()
)
obmCalloutTriggerEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCalloutTriggerEvent.setStatus("mandatory")


class _ObmCalloutRetries_Type(Integer32):
    """Custom type obmCalloutRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ObmCalloutRetries_Type.__name__ = "Integer32"
_ObmCalloutRetries_Object = MibScalar
obmCalloutRetries = _ObmCalloutRetries_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 12),
    _ObmCalloutRetries_Type()
)
obmCalloutRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCalloutRetries.setStatus("mandatory")


class _ObmCalloutRetryTimer_Type(Integer32):
    """Custom type obmCalloutRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ObmCalloutRetryTimer_Type.__name__ = "Integer32"
_ObmCalloutRetryTimer_Object = MibScalar
obmCalloutRetryTimer = _ObmCalloutRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 13),
    _ObmCalloutRetryTimer_Type()
)
obmCalloutRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmCalloutRetryTimer.setStatus("mandatory")


class _ObmDelayedRecovery_Type(Integer32):
    """Custom type obmDelayedRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ObmDelayedRecovery_Type.__name__ = "Integer32"
_ObmDelayedRecovery_Object = MibScalar
obmDelayedRecovery = _ObmDelayedRecovery_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 14),
    _ObmDelayedRecovery_Type()
)
obmDelayedRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmDelayedRecovery.setStatus("mandatory")


class _ObmEnableTelnet_Type(Integer32):
    """Custom type obmEnableTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ObmEnableTelnet_Type.__name__ = "Integer32"
_ObmEnableTelnet_Object = MibScalar
obmEnableTelnet = _ObmEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 15),
    _ObmEnableTelnet_Type()
)
obmEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmEnableTelnet.setStatus("optional")


class _ObmConnectTimeout_Type(Integer32):
    """Custom type obmConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ObmConnectTimeout_Type.__name__ = "Integer32"
_ObmConnectTimeout_Object = MibScalar
obmConnectTimeout = _ObmConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 16),
    _ObmConnectTimeout_Type()
)
obmConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmConnectTimeout.setStatus("optional")


class _ObmDefaultOperationalMode_Type(Integer32):
    """Custom type obmDefaultOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asyncPPP", 3),
          ("autoSense", 1),
          ("serialConsole", 2))
    )


_ObmDefaultOperationalMode_Type.__name__ = "Integer32"
_ObmDefaultOperationalMode_Object = MibScalar
obmDefaultOperationalMode = _ObmDefaultOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 17),
    _ObmDefaultOperationalMode_Type()
)
obmDefaultOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmDefaultOperationalMode.setStatus("optional")


class _ObmInactivityTimeout_Type(Integer32):
    """Custom type obmInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ObmInactivityTimeout_Type.__name__ = "Integer32"
_ObmInactivityTimeout_Object = MibScalar
obmInactivityTimeout = _ObmInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 18),
    _ObmInactivityTimeout_Type()
)
obmInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmInactivityTimeout.setStatus("mandatory")


class _ObmDialType_Type(Integer32):
    """Custom type obmDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 1),
          ("tone", 2))
    )


_ObmDialType_Type.__name__ = "Integer32"
_ObmDialType_Object = MibScalar
obmDialType = _ObmDialType_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 19),
    _ObmDialType_Type()
)
obmDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmDialType.setStatus("mandatory")


class _ObmPasswordRead_Type(DisplayString):
    """Custom type obmPasswordRead based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ObmPasswordRead_Type.__name__ = "DisplayString"
_ObmPasswordRead_Object = MibScalar
obmPasswordRead = _ObmPasswordRead_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 20),
    _ObmPasswordRead_Type()
)
obmPasswordRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmPasswordRead.setStatus("mandatory")


class _ObmXonXoffHandshake_Type(Integer32):
    """Custom type obmXonXoffHandshake based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ObmXonXoffHandshake_Type.__name__ = "Integer32"
_ObmXonXoffHandshake_Object = MibScalar
obmXonXoffHandshake = _ObmXonXoffHandshake_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 21),
    _ObmXonXoffHandshake_Type()
)
obmXonXoffHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmXonXoffHandshake.setStatus("mandatory")


class _ObmRtsCtsHandshake_Type(Integer32):
    """Custom type obmRtsCtsHandshake based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ObmRtsCtsHandshake_Type.__name__ = "Integer32"
_ObmRtsCtsHandshake_Object = MibScalar
obmRtsCtsHandshake = _ObmRtsCtsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 22),
    _ObmRtsCtsHandshake_Type()
)
obmRtsCtsHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    obmRtsCtsHandshake.setStatus("mandatory")
_ObmDatabits_Type = Integer32
_ObmDatabits_Object = MibScalar
obmDatabits = _ObmDatabits_Object(
    (1, 3, 6, 1, 4, 1, 285, 6, 23),
    _ObmDatabits_Type()
)
obmDatabits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obmDatabits.setStatus("mandatory")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 7)
)
_ManagementTable_Object = MibTable
managementTable = _ManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1)
)
if mibBuilder.loadTexts:
    managementTable.setStatus("mandatory")
_ManagementTableEntry_Object = MibTableRow
managementTableEntry = _ManagementTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1, 1)
)
managementTableEntry.setIndexNames(
    (0, "Olicom-MIB", "managementNo"),
)
if mibBuilder.loadTexts:
    managementTableEntry.setStatus("mandatory")
_ManagementNo_Type = Integer32
_ManagementNo_Object = MibTableColumn
managementNo = _ManagementNo_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1, 1, 1),
    _ManagementNo_Type()
)
managementNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementNo.setStatus("mandatory")
_ManagementDescription_Type = DisplayString
_ManagementDescription_Object = MibTableColumn
managementDescription = _ManagementDescription_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1, 1, 2),
    _ManagementDescription_Type()
)
managementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDescription.setStatus("mandatory")


class _ManagementAssociationState_Type(Integer32):
    """Custom type managementAssociationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("na-association", 3),
          ("not-associated", 2))
    )


_ManagementAssociationState_Type.__name__ = "Integer32"
_ManagementAssociationState_Object = MibTableColumn
managementAssociationState = _ManagementAssociationState_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1, 1, 3),
    _ManagementAssociationState_Type()
)
managementAssociationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementAssociationState.setStatus("mandatory")
_ManagementPriority_Type = Integer32
_ManagementPriority_Object = MibTableColumn
managementPriority = _ManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 1, 1, 4),
    _ManagementPriority_Type()
)
managementPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPriority.setStatus("mandatory")
_ManagementSnmpAccessLogTable_Object = MibTable
managementSnmpAccessLogTable = _ManagementSnmpAccessLogTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2)
)
if mibBuilder.loadTexts:
    managementSnmpAccessLogTable.setStatus("optional")
_ManagementSnmpAccessLogEntry_Object = MibTableRow
managementSnmpAccessLogEntry = _ManagementSnmpAccessLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1)
)
managementSnmpAccessLogEntry.setIndexNames(
    (0, "Olicom-MIB", "managementSnmpAccessLogIndex"),
)
if mibBuilder.loadTexts:
    managementSnmpAccessLogEntry.setStatus("optional")


class _ManagementSnmpAccessLogIndex_Type(Integer32):
    """Custom type managementSnmpAccessLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ManagementSnmpAccessLogIndex_Type.__name__ = "Integer32"
_ManagementSnmpAccessLogIndex_Object = MibTableColumn
managementSnmpAccessLogIndex = _ManagementSnmpAccessLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1, 1),
    _ManagementSnmpAccessLogIndex_Type()
)
managementSnmpAccessLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpAccessLogIndex.setStatus("optional")
_ManagementSnmpAccessLogTimeStamp_Type = TimeTicks
_ManagementSnmpAccessLogTimeStamp_Object = MibTableColumn
managementSnmpAccessLogTimeStamp = _ManagementSnmpAccessLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1, 2),
    _ManagementSnmpAccessLogTimeStamp_Type()
)
managementSnmpAccessLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpAccessLogTimeStamp.setStatus("optional")
_ManagementSnmpAccessLogIpAddress_Type = IpAddress
_ManagementSnmpAccessLogIpAddress_Object = MibTableColumn
managementSnmpAccessLogIpAddress = _ManagementSnmpAccessLogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1, 3),
    _ManagementSnmpAccessLogIpAddress_Type()
)
managementSnmpAccessLogIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpAccessLogIpAddress.setStatus("optional")


class _ManagementSnmpAccessLogAccessRights_Type(Integer32):
    """Custom type managementSnmpAccessLogAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_ManagementSnmpAccessLogAccessRights_Type.__name__ = "Integer32"
_ManagementSnmpAccessLogAccessRights_Object = MibTableColumn
managementSnmpAccessLogAccessRights = _ManagementSnmpAccessLogAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1, 4),
    _ManagementSnmpAccessLogAccessRights_Type()
)
managementSnmpAccessLogAccessRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpAccessLogAccessRights.setStatus("optional")
_ManagementSnmpAccessLogCount_Type = Integer32
_ManagementSnmpAccessLogCount_Object = MibTableColumn
managementSnmpAccessLogCount = _ManagementSnmpAccessLogCount_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 2, 1, 5),
    _ManagementSnmpAccessLogCount_Type()
)
managementSnmpAccessLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpAccessLogCount.setStatus("optional")
_ManagementSnmpLastErrorReason_Type = DisplayString
_ManagementSnmpLastErrorReason_Object = MibScalar
managementSnmpLastErrorReason = _ManagementSnmpLastErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 285, 7, 3),
    _ManagementSnmpLastErrorReason_Type()
)
managementSnmpLastErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementSnmpLastErrorReason.setStatus("mandatory")
_Frontpanel_ObjectIdentity = ObjectIdentity
frontpanel = _Frontpanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 8)
)
_FrontpanelDisplay_Type = DisplayString
_FrontpanelDisplay_Object = MibScalar
frontpanelDisplay = _FrontpanelDisplay_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 1),
    _FrontpanelDisplay_Type()
)
frontpanelDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontpanelDisplay.setStatus("optional")


class _FrontpanelKeyboardAccess_Type(Integer32):
    """Custom type frontpanelKeyboardAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 1),
          ("status-only", 2))
    )


_FrontpanelKeyboardAccess_Type.__name__ = "Integer32"
_FrontpanelKeyboardAccess_Object = MibScalar
frontpanelKeyboardAccess = _FrontpanelKeyboardAccess_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 2),
    _FrontpanelKeyboardAccess_Type()
)
frontpanelKeyboardAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontpanelKeyboardAccess.setStatus("optional")
_FrontpanelErrorcode_Type = Integer32
_FrontpanelErrorcode_Object = MibScalar
frontpanelErrorcode = _FrontpanelErrorcode_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 3),
    _FrontpanelErrorcode_Type()
)
frontpanelErrorcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontpanelErrorcode.setStatus("optional")


class _FrontpanelErrorLED_Type(Integer32):
    """Custom type frontpanelErrorLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("led-flashing", 4),
          ("led-off", 2),
          ("led-on-steady", 3),
          ("led-unknown", 1))
    )


_FrontpanelErrorLED_Type.__name__ = "Integer32"
_FrontpanelErrorLED_Object = MibScalar
frontpanelErrorLED = _FrontpanelErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 4),
    _FrontpanelErrorLED_Type()
)
frontpanelErrorLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontpanelErrorLED.setStatus("optional")
_FrontpanelDefaultDisplay_Type = Integer32
_FrontpanelDefaultDisplay_Object = MibScalar
frontpanelDefaultDisplay = _FrontpanelDefaultDisplay_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 5),
    _FrontpanelDefaultDisplay_Type()
)
frontpanelDefaultDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontpanelDefaultDisplay.setStatus("optional")


class _FrontpanelKeyPress_Type(Integer32):
    """Custom type frontpanelKeyPress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(400,
              401,
              402,
              403,
              404)
        )
    )
    namedValues = NamedValues(
        *(("key-down", 402),
          ("key-enter", 400),
          ("key-left", 403),
          ("key-right", 404),
          ("key-up", 401))
    )


_FrontpanelKeyPress_Type.__name__ = "Integer32"
_FrontpanelKeyPress_Object = MibScalar
frontpanelKeyPress = _FrontpanelKeyPress_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 6),
    _FrontpanelKeyPress_Type()
)
frontpanelKeyPress.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frontpanelKeyPress.setStatus("optional")
_FrontpanelDisplayLogTable_Object = MibTable
frontpanelDisplayLogTable = _FrontpanelDisplayLogTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 7)
)
if mibBuilder.loadTexts:
    frontpanelDisplayLogTable.setStatus("optional")
_FrontpanelDisplayLogEntry_Object = MibTableRow
frontpanelDisplayLogEntry = _FrontpanelDisplayLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 7, 1)
)
frontpanelDisplayLogEntry.setIndexNames(
    (0, "Olicom-MIB", "frontpanelDisplayLogIndex"),
)
if mibBuilder.loadTexts:
    frontpanelDisplayLogEntry.setStatus("optional")
_FrontpanelDisplayLogIndex_Type = Integer32
_FrontpanelDisplayLogIndex_Object = MibTableColumn
frontpanelDisplayLogIndex = _FrontpanelDisplayLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 7, 1, 1),
    _FrontpanelDisplayLogIndex_Type()
)
frontpanelDisplayLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frontpanelDisplayLogIndex.setStatus("optional")
_FrontpanelDisplayLogTimeStamp_Type = TimeTicks
_FrontpanelDisplayLogTimeStamp_Object = MibTableColumn
frontpanelDisplayLogTimeStamp = _FrontpanelDisplayLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 7, 1, 2),
    _FrontpanelDisplayLogTimeStamp_Type()
)
frontpanelDisplayLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frontpanelDisplayLogTimeStamp.setStatus("optional")
_FrontpanelDisplayLogDisplayText_Type = DisplayString
_FrontpanelDisplayLogDisplayText_Object = MibTableColumn
frontpanelDisplayLogDisplayText = _FrontpanelDisplayLogDisplayText_Object(
    (1, 3, 6, 1, 4, 1, 285, 8, 7, 1, 3),
    _FrontpanelDisplayLogDisplayText_Type()
)
frontpanelDisplayLogDisplayText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frontpanelDisplayLogDisplayText.setStatus("optional")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9)
)
_TokenRingBridgeSR_ObjectIdentity = ObjectIdentity
tokenRingBridgeSR = _TokenRingBridgeSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 1)
)
_ControlledAccessUnit_ObjectIdentity = ObjectIdentity
controlledAccessUnit = _ControlledAccessUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 2)
)
_ControlledAttachmentModule_ObjectIdentity = ObjectIdentity
controlledAttachmentModule = _ControlledAttachmentModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 3)
)
_EtherNetAttachmentHUB_ObjectIdentity = ObjectIdentity
etherNetAttachmentHUB = _EtherNetAttachmentHUB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 4)
)
_TokenRingRemoteBridgeAndCAM_ObjectIdentity = ObjectIdentity
tokenRingRemoteBridgeAndCAM = _TokenRingRemoteBridgeAndCAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 5)
)
_TokenRingMultiPortBridge_ObjectIdentity = ObjectIdentity
tokenRingMultiPortBridge = _TokenRingMultiPortBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 6)
)
_DesktopManagementAgent_ObjectIdentity = ObjectIdentity
desktopManagementAgent = _DesktopManagementAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 7)
)
_LocalPCBridge_ObjectIdentity = ObjectIdentity
localPCBridge = _LocalPCBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 8)
)
_RemoteDOSPCBridge_ObjectIdentity = ObjectIdentity
remoteDOSPCBridge = _RemoteDOSPCBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 9)
)
_RemoteOS2PCBridge_ObjectIdentity = ObjectIdentity
remoteOS2PCBridge = _RemoteOS2PCBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 10)
)
_TokenRingSwitchOc8100_ObjectIdentity = ObjectIdentity
tokenRingSwitchOc8100 = _TokenRingSwitchOc8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 11)
)
_CrossfireAtmSwitch_ObjectIdentity = ObjectIdentity
crossfireAtmSwitch = _CrossfireAtmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 12)
)
_EthernetSwitchOc8200_ObjectIdentity = ObjectIdentity
ethernetSwitchOc8200 = _EthernetSwitchOc8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 13)
)
_TokenRingSwitchOc8600_ObjectIdentity = ObjectIdentity
tokenRingSwitchOc8600 = _TokenRingSwitchOc8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 14)
)
_TokenRingSwitchOc8007_ObjectIdentity = ObjectIdentity
tokenRingSwitchOc8007 = _TokenRingSwitchOc8007_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 15)
)
_CrossfireAtmSwitchOc8008_ObjectIdentity = ObjectIdentity
crossfireAtmSwitchOc8008 = _CrossfireAtmSwitchOc8008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 16)
)
_FastEthernetSwitchOc8400_ObjectIdentity = ObjectIdentity
fastEthernetSwitchOc8400 = _FastEthernetSwitchOc8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 17)
)
_FastEthernetSwitchOc8420_ObjectIdentity = ObjectIdentity
fastEthernetSwitchOc8420 = _FastEthernetSwitchOc8420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 18)
)
_LanscoutOc5020_ObjectIdentity = ObjectIdentity
lanscoutOc5020 = _LanscoutOc5020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 19)
)
_CrossfireAtmSwitchCf9200_ObjectIdentity = ObjectIdentity
crossfireAtmSwitchCf9200 = _CrossfireAtmSwitchCf9200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 20)
)
_CrossfireRouterCf7100_ObjectIdentity = ObjectIdentity
crossfireRouterCf7100 = _CrossfireRouterCf7100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 21)
)
_TokenRingSwitchCf8500_ObjectIdentity = ObjectIdentity
tokenRingSwitchCf8500 = _TokenRingSwitchCf8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 22)
)
_EthernetSwitchCf8711_ObjectIdentity = ObjectIdentity
ethernetSwitchCf8711 = _EthernetSwitchCf8711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 23)
)
_EthernetSwitchCf8720_ObjectIdentity = ObjectIdentity
ethernetSwitchCf8720 = _EthernetSwitchCf8720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 24)
)
_EthernetSwitchCf8810_ObjectIdentity = ObjectIdentity
ethernetSwitchCf8810 = _EthernetSwitchCf8810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 9, 25)
)
_Errorlog_ObjectIdentity = ObjectIdentity
errorlog = _Errorlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 10)
)
_ErrorlogTable_Object = MibTable
errorlogTable = _ErrorlogTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1)
)
if mibBuilder.loadTexts:
    errorlogTable.setStatus("optional")
_ErrorlogEntry_Object = MibTableRow
errorlogEntry = _ErrorlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1)
)
errorlogEntry.setIndexNames(
    (0, "Olicom-MIB", "errorlogNumber"),
)
if mibBuilder.loadTexts:
    errorlogEntry.setStatus("optional")
_ErrorlogNumber_Type = Integer32
_ErrorlogNumber_Object = MibTableColumn
errorlogNumber = _ErrorlogNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 1),
    _ErrorlogNumber_Type()
)
errorlogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogNumber.setStatus("optional")
_ErrorlogTimeStamp_Type = TimeTicks
_ErrorlogTimeStamp_Object = MibTableColumn
errorlogTimeStamp = _ErrorlogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 2),
    _ErrorlogTimeStamp_Type()
)
errorlogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTimeStamp.setStatus("optional")
_ErrorlogErrorDescription_Type = DisplayString
_ErrorlogErrorDescription_Object = MibTableColumn
errorlogErrorDescription = _ErrorlogErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 3),
    _ErrorlogErrorDescription_Type()
)
errorlogErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogErrorDescription.setStatus("optional")
_ErrorlogErrorData_Type = OctetString
_ErrorlogErrorData_Object = MibTableColumn
errorlogErrorData = _ErrorlogErrorData_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 4),
    _ErrorlogErrorData_Type()
)
errorlogErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogErrorData.setStatus("optional")
_ErrorlogTime_Type = Integer32
_ErrorlogTime_Object = MibTableColumn
errorlogTime = _ErrorlogTime_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 5),
    _ErrorlogTime_Type()
)
errorlogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTime.setStatus("optional")
_ErrorlogTimeRemoved_Type = Integer32
_ErrorlogTimeRemoved_Object = MibTableColumn
errorlogTimeRemoved = _ErrorlogTimeRemoved_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 6),
    _ErrorlogTimeRemoved_Type()
)
errorlogTimeRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTimeRemoved.setStatus("optional")


class _ErrorlogCategory_Type(Integer32):
    """Custom type errorlogCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootload", 1),
          ("operational", 3),
          ("startup", 2))
    )


_ErrorlogCategory_Type.__name__ = "Integer32"
_ErrorlogCategory_Object = MibTableColumn
errorlogCategory = _ErrorlogCategory_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 7),
    _ErrorlogCategory_Type()
)
errorlogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogCategory.setStatus("optional")


class _ErrorlogSeverity_Type(Integer32):
    """Custom type errorlogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 6),
          ("critical", 5),
          ("debug", 8),
          ("error", 4),
          ("fatal", 9),
          ("information", 1),
          ("notice", 2),
          ("panic", 7),
          ("warning", 3))
    )


_ErrorlogSeverity_Type.__name__ = "Integer32"
_ErrorlogSeverity_Object = MibTableColumn
errorlogSeverity = _ErrorlogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 8),
    _ErrorlogSeverity_Type()
)
errorlogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogSeverity.setStatus("optional")
_ErrorlogPhysicalIf_Type = Integer32
_ErrorlogPhysicalIf_Object = MibTableColumn
errorlogPhysicalIf = _ErrorlogPhysicalIf_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 9),
    _ErrorlogPhysicalIf_Type()
)
errorlogPhysicalIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogPhysicalIf.setStatus("optional")
_ErrorlogVirtualIf_Type = Integer32
_ErrorlogVirtualIf_Object = MibTableColumn
errorlogVirtualIf = _ErrorlogVirtualIf_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 1, 1, 10),
    _ErrorlogVirtualIf_Type()
)
errorlogVirtualIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogVirtualIf.setStatus("optional")


class _ErrorlogTraceControl_Type(Integer32):
    """Custom type errorlogTraceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("erase-log", 4),
          ("log-empty", 1),
          ("log-present", 2),
          ("save-log", 3))
    )


_ErrorlogTraceControl_Type.__name__ = "Integer32"
_ErrorlogTraceControl_Object = MibScalar
errorlogTraceControl = _ErrorlogTraceControl_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 2),
    _ErrorlogTraceControl_Type()
)
errorlogTraceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogTraceControl.setStatus("optional")
_ErrorlogTraceMaskCurrent_Type = OctetString
_ErrorlogTraceMaskCurrent_Object = MibScalar
errorlogTraceMaskCurrent = _ErrorlogTraceMaskCurrent_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 3),
    _ErrorlogTraceMaskCurrent_Type()
)
errorlogTraceMaskCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogTraceMaskCurrent.setStatus("optional")
_ErrorlogTraceMaskInitial_Type = OctetString
_ErrorlogTraceMaskInitial_Object = MibScalar
errorlogTraceMaskInitial = _ErrorlogTraceMaskInitial_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 4),
    _ErrorlogTraceMaskInitial_Type()
)
errorlogTraceMaskInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogTraceMaskInitial.setStatus("optional")
_ErrorlogTraceMaskOperational_Type = OctetString
_ErrorlogTraceMaskOperational_Object = MibScalar
errorlogTraceMaskOperational = _ErrorlogTraceMaskOperational_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 5),
    _ErrorlogTraceMaskOperational_Type()
)
errorlogTraceMaskOperational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogTraceMaskOperational.setStatus("optional")
_ErrorlogTraceLogSize_Type = Integer32
_ErrorlogTraceLogSize_Object = MibScalar
errorlogTraceLogSize = _ErrorlogTraceLogSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 6),
    _ErrorlogTraceLogSize_Type()
)
errorlogTraceLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogTraceLogSize.setStatus("optional")
_ErrorlogTraceSliceTable_Object = MibTable
errorlogTraceSliceTable = _ErrorlogTraceSliceTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 7)
)
if mibBuilder.loadTexts:
    errorlogTraceSliceTable.setStatus("optional")
_ErrorlogTraceSliceTableEntry_Object = MibTableRow
errorlogTraceSliceTableEntry = _ErrorlogTraceSliceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 7, 1)
)
errorlogTraceSliceTableEntry.setIndexNames(
    (0, "Olicom-MIB", "errorlogTraceSliceNumber"),
    (0, "Olicom-MIB", "errorlogTraceSliceSize"),
)
if mibBuilder.loadTexts:
    errorlogTraceSliceTableEntry.setStatus("optional")
_ErrorlogTraceSliceNumber_Type = Integer32
_ErrorlogTraceSliceNumber_Object = MibTableColumn
errorlogTraceSliceNumber = _ErrorlogTraceSliceNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 7, 1, 1),
    _ErrorlogTraceSliceNumber_Type()
)
errorlogTraceSliceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTraceSliceNumber.setStatus("optional")


class _ErrorlogTraceSliceSize_Type(Integer32):
    """Custom type errorlogTraceSliceSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ErrorlogTraceSliceSize_Type.__name__ = "Integer32"
_ErrorlogTraceSliceSize_Object = MibTableColumn
errorlogTraceSliceSize = _ErrorlogTraceSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 7, 1, 2),
    _ErrorlogTraceSliceSize_Type()
)
errorlogTraceSliceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTraceSliceSize.setStatus("optional")
_ErrorlogTraceSliceData_Type = OctetString
_ErrorlogTraceSliceData_Object = MibTableColumn
errorlogTraceSliceData = _ErrorlogTraceSliceData_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 7, 1, 3),
    _ErrorlogTraceSliceData_Type()
)
errorlogTraceSliceData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorlogTraceSliceData.setStatus("optional")
_ErrorlogStoredSeverityLevel_Type = Integer32
_ErrorlogStoredSeverityLevel_Object = MibScalar
errorlogStoredSeverityLevel = _ErrorlogStoredSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 285, 10, 8),
    _ErrorlogStoredSeverityLevel_Type()
)
errorlogStoredSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorlogStoredSeverityLevel.setStatus("optional")
_Trconfig_ObjectIdentity = ObjectIdentity
trconfig = _Trconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 285, 11)
)
_TrconfigTable_Object = MibTable
trconfigTable = _TrconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1)
)
if mibBuilder.loadTexts:
    trconfigTable.setStatus("optional")
_TrconfigEntry_Object = MibTableRow
trconfigEntry = _TrconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1, 1)
)
trconfigEntry.setIndexNames(
    (0, "Olicom-MIB", "trconfigIfNumber"),
)
if mibBuilder.loadTexts:
    trconfigEntry.setStatus("optional")
_TrconfigIfNumber_Type = Integer32
_TrconfigIfNumber_Object = MibTableColumn
trconfigIfNumber = _TrconfigIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1, 1, 1),
    _TrconfigIfNumber_Type()
)
trconfigIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trconfigIfNumber.setStatus("optional")
_TrconfigBurntInAddress_Type = MacAddress
_TrconfigBurntInAddress_Object = MibTableColumn
trconfigBurntInAddress = _TrconfigBurntInAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1, 1, 2),
    _TrconfigBurntInAddress_Type()
)
trconfigBurntInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trconfigBurntInAddress.setStatus("optional")
_TrconfigLocalAddress_Type = MacAddress
_TrconfigLocalAddress_Object = MibTableColumn
trconfigLocalAddress = _TrconfigLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1, 1, 3),
    _TrconfigLocalAddress_Type()
)
trconfigLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trconfigLocalAddress.setStatus("optional")


class _TrconfigEarlyTokenRelease_Type(Integer32):
    """Custom type trconfigEarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TrconfigEarlyTokenRelease_Type.__name__ = "Integer32"
_TrconfigEarlyTokenRelease_Object = MibTableColumn
trconfigEarlyTokenRelease = _TrconfigEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 285, 11, 1, 1, 4),
    _TrconfigEarlyTokenRelease_Type()
)
trconfigEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trconfigEarlyTokenRelease.setStatus("optional")

# Managed Objects groups


# Notification objects

obmCallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 0, 1)
)
obmCallback.setObjects(
    ("Olicom-MIB", "obmCallbackPhoneNumber")
)
if mibBuilder.loadTexts:
    obmCallback.setStatus(
        ""
    )

obmCallout = NotificationType(
    (1, 3, 6, 1, 4, 1, 285, 0, 2)
)
obmCallout.setObjects(
      *(("Olicom-MIB", "obmCalloutPhoneNumber"),
        ("Olicom-MIB", "obmCalloutTriggerEvent"))
)
if mibBuilder.loadTexts:
    obmCallout.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Olicom-MIB",
    **{"MacAddress": MacAddress,
       "IPXAddress": IPXAddress,
       "RowStatus": RowStatus,
       "olicom": olicom,
       "obmCallback": obmCallback,
       "obmCallout": obmCallout,
       "info": info,
       "infoHardwareProductId": infoHardwareProductId,
       "infoHardwareVersion": infoHardwareVersion,
       "infoHardwareECOLevel": infoHardwareECOLevel,
       "infoHardwareSerialNumber": infoHardwareSerialNumber,
       "infoHardwareOptionTable": infoHardwareOptionTable,
       "infoHardwareOptionTableEntry": infoHardwareOptionTableEntry,
       "infoHardwareOptionNo": infoHardwareOptionNo,
       "infoHardwareOption": infoHardwareOption,
       "infoSoftwareProductId": infoSoftwareProductId,
       "infoSoftwareVersion": infoSoftwareVersion,
       "infoSoftwareECOLevel": infoSoftwareECOLevel,
       "infoSoftwareOptionTable": infoSoftwareOptionTable,
       "infoSoftwareOptionTableEntry": infoSoftwareOptionTableEntry,
       "infoSoftwareOptionNo": infoSoftwareOptionNo,
       "infoSoftwareOption": infoSoftwareOption,
       "infoSoftwareMIBsTable": infoSoftwareMIBsTable,
       "infoSoftwareMIBsTableEntry": infoSoftwareMIBsTableEntry,
       "infoSoftwareMIBsNo": infoSoftwareMIBsNo,
       "infoSoftwareMIBsObjectID": infoSoftwareMIBsObjectID,
       "infoSoftwareMIBsDescription": infoSoftwareMIBsDescription,
       "infoXtraSwTable": infoXtraSwTable,
       "infoXtraSwEntry": infoXtraSwEntry,
       "infoXtraSwIndex": infoXtraSwIndex,
       "infoXtraSwFileUse": infoXtraSwFileUse,
       "infoXtraSwProductId": infoXtraSwProductId,
       "infoXtraSwVersion": infoXtraSwVersion,
       "infoXtraSwEcoLevel": infoXtraSwEcoLevel,
       "infoXtraSwSerialNumber": infoXtraSwSerialNumber,
       "infoXtraSwOptions": infoXtraSwOptions,
       "infoModuleTable": infoModuleTable,
       "infoModuleEntry": infoModuleEntry,
       "infoModuleIndex": infoModuleIndex,
       "infoModuleHwProductId": infoModuleHwProductId,
       "infoModuleHwVersion": infoModuleHwVersion,
       "infoModuleHwSerialNumber": infoModuleHwSerialNumber,
       "infoModuleBootpromVersion": infoModuleBootpromVersion,
       "infoSwImageTable": infoSwImageTable,
       "infoSwImageEntry": infoSwImageEntry,
       "infoSwImageModuleIndex": infoSwImageModuleIndex,
       "infoSwImageNo": infoSwImageNo,
       "infoSwImageProductId": infoSwImageProductId,
       "infoSwImageVersion": infoSwImageVersion,
       "infoSwImageDownloadTime": infoSwImageDownloadTime,
       "ocmibs": ocmibs,
       "ocmibsBridgeMIB": ocmibsBridgeMIB,
       "ocmibsCauMIB": ocmibsCauMIB,
       "ocmibsCamMIB": ocmibsCamMIB,
       "ocmibsEhubMIB": ocmibsEhubMIB,
       "ocmibsOc8100MIB": ocmibsOc8100MIB,
       "ocmibsCrossfireAtmMIB": ocmibsCrossfireAtmMIB,
       "ocmibsOc8200MIB": ocmibsOc8200MIB,
       "ocmibsOc8600MIB": ocmibsOc8600MIB,
       "ocmibsOc84x0MIB": ocmibsOc84x0MIB,
       "ocmibsLanSwitchMIB": ocmibsLanSwitchMIB,
       "ocmibsVlanMIB": ocmibsVlanMIB,
       "ocmibsSmartStatusMIB": ocmibsSmartStatusMIB,
       "ocmibsCf871xMIB": ocmibsCf871xMIB,
       "atmUplinkMIB": atmUplinkMIB,
       "temporary": temporary,
       "lmpMib": lmpMib,
       "inet": inet,
       "inetMacAddrForm": inetMacAddrForm,
       "inetEnableRwho": inetEnableRwho,
       "inetEnableRIP": inetEnableRIP,
       "inetCommunityMaxEntries": inetCommunityMaxEntries,
       "inetCommunityTable": inetCommunityTable,
       "inetCommunityTableEntry": inetCommunityTableEntry,
       "inetCommunityNo": inetCommunityNo,
       "inetCommunityName": inetCommunityName,
       "inetCommunityIPAddress": inetCommunityIPAddress,
       "inetCommunityAccess": inetCommunityAccess,
       "inetCommunityDelete": inetCommunityDelete,
       "inetCommunityIPXAddress": inetCommunityIPXAddress,
       "inetCommunityTransportProtocols": inetCommunityTransportProtocols,
       "inetCommunityMACAddress": inetCommunityMACAddress,
       "inetTrapMaxEntries": inetTrapMaxEntries,
       "inetTrapTable": inetTrapTable,
       "inetTrapTableEntry": inetTrapTableEntry,
       "inetTrapCommunity": inetTrapCommunity,
       "inetTrapDestIPAddress": inetTrapDestIPAddress,
       "inetTrapEventDisableMask": inetTrapEventDisableMask,
       "inetTrapDelete": inetTrapDelete,
       "inetTrapDestUDPPort": inetTrapDestUDPPort,
       "inetTrapIndex": inetTrapIndex,
       "inetTrapDestIPXAddress": inetTrapDestIPXAddress,
       "inetTrapTransportProtocols": inetTrapTransportProtocols,
       "inetTrapIPEncapsulation": inetTrapIPEncapsulation,
       "inetTrapIPXEncapsulation": inetTrapIPXEncapsulation,
       "inetDefaultIPEncapsulation": inetDefaultIPEncapsulation,
       "inetDefaultIPXEncapsulation": inetDefaultIPXEncapsulation,
       "inetIPAddressTable": inetIPAddressTable,
       "inetIPAddressEntry": inetIPAddressEntry,
       "inetIPAddressIfNumber": inetIPAddressIfNumber,
       "inetIPAddressIPAddress": inetIPAddressIPAddress,
       "inetIPAddressNetmask": inetIPAddressNetmask,
       "inetIPAddressDefaultGateway": inetIPAddressDefaultGateway,
       "inetIPAddressEnableRwho": inetIPAddressEnableRwho,
       "inetIPAddressEnableRIP": inetIPAddressEnableRIP,
       "inetIPAddressIPEncapsulation": inetIPAddressIPEncapsulation,
       "inetSlipBaudrate": inetSlipBaudrate,
       "inetSlipParity": inetSlipParity,
       "inetSlipStopbits": inetSlipStopbits,
       "inetSlipModemInit": inetSlipModemInit,
       "inetSlipHeaderCompressionEnabled": inetSlipHeaderCompressionEnabled,
       "inetSlipMaxMtuSize": inetSlipMaxMtuSize,
       "inetSlipMaxMruSize": inetSlipMaxMruSize,
       "sCallbackEnable": sCallbackEnable,
       "sCallbackPhoneNumber": sCallbackPhoneNumber,
       "sCalloutEnable": sCalloutEnable,
       "sCalloutPhoneNumber": sCalloutPhoneNumber,
       "control": control,
       "controlRestart": controlRestart,
       "controlConfigChangeCounter": controlConfigChangeCounter,
       "controlTrapTable": controlTrapTable,
       "controlTrapTableEntry": controlTrapTableEntry,
       "controlTrapIndex": controlTrapIndex,
       "controlTrapMIBIndex": controlTrapMIBIndex,
       "controlTrapNumber": controlTrapNumber,
       "controlTrapDescription": controlTrapDescription,
       "controlTrapGeneration": controlTrapGeneration,
       "controlLoadProtocol": controlLoadProtocol,
       "controlLoadFilename": controlLoadFilename,
       "controlLoadServerMACAddress": controlLoadServerMACAddress,
       "controlLoadServerIPAddress": controlLoadServerIPAddress,
       "controlLoadServerIPXAddress": controlLoadServerIPXAddress,
       "controlLoadStart": controlLoadStart,
       "controlTime": controlTime,
       "controlEnableRmon": controlEnableRmon,
       "controlAutoRestart": controlAutoRestart,
       "controlSwAdminStatus": controlSwAdminStatus,
       "controlFlashConfigSize": controlFlashConfigSize,
       "controlFlashConfigFree": controlFlashConfigFree,
       "controlFlashConfigState": controlFlashConfigState,
       "controlDelayedRestart": controlDelayedRestart,
       "controlLoadProggress": controlLoadProggress,
       "controlLoadFileSize": controlLoadFileSize,
       "controlTftpClient": controlTftpClient,
       "controlTftpMaxSessions": controlTftpMaxSessions,
       "controlTftpNextSessionIndex": controlTftpNextSessionIndex,
       "controlTftpSessionTable": controlTftpSessionTable,
       "controlTftpSessionEntry": controlTftpSessionEntry,
       "controlTftpSessionIndex": controlTftpSessionIndex,
       "controlTftpSessionRowStatus": controlTftpSessionRowStatus,
       "controlTftpSessionDirection": controlTftpSessionDirection,
       "controlTftpSessionServerAddress": controlTftpSessionServerAddress,
       "controlTftpSessionServerFile": controlTftpSessionServerFile,
       "controlTftpSessionLocalFile": controlTftpSessionLocalFile,
       "controlTftpSessionStatus": controlTftpSessionStatus,
       "controlTftpSessionProgress": controlTftpSessionProgress,
       "controlTftpSessionFileSize": controlTftpSessionFileSize,
       "controlRestartType": controlRestartType,
       "obm": obm,
       "obmEnable": obmEnable,
       "obmPassword": obmPassword,
       "obmBaudrate": obmBaudrate,
       "obmParity": obmParity,
       "obmStopbits": obmStopbits,
       "obmModemInit": obmModemInit,
       "obmCallbackEnable": obmCallbackEnable,
       "obmCallbackPhoneNumber": obmCallbackPhoneNumber,
       "obmCalloutEnable": obmCalloutEnable,
       "obmCalloutPhoneNumber": obmCalloutPhoneNumber,
       "obmCalloutTriggerEvent": obmCalloutTriggerEvent,
       "obmCalloutRetries": obmCalloutRetries,
       "obmCalloutRetryTimer": obmCalloutRetryTimer,
       "obmDelayedRecovery": obmDelayedRecovery,
       "obmEnableTelnet": obmEnableTelnet,
       "obmConnectTimeout": obmConnectTimeout,
       "obmDefaultOperationalMode": obmDefaultOperationalMode,
       "obmInactivityTimeout": obmInactivityTimeout,
       "obmDialType": obmDialType,
       "obmPasswordRead": obmPasswordRead,
       "obmXonXoffHandshake": obmXonXoffHandshake,
       "obmRtsCtsHandshake": obmRtsCtsHandshake,
       "obmDatabits": obmDatabits,
       "management": management,
       "managementTable": managementTable,
       "managementTableEntry": managementTableEntry,
       "managementNo": managementNo,
       "managementDescription": managementDescription,
       "managementAssociationState": managementAssociationState,
       "managementPriority": managementPriority,
       "managementSnmpAccessLogTable": managementSnmpAccessLogTable,
       "managementSnmpAccessLogEntry": managementSnmpAccessLogEntry,
       "managementSnmpAccessLogIndex": managementSnmpAccessLogIndex,
       "managementSnmpAccessLogTimeStamp": managementSnmpAccessLogTimeStamp,
       "managementSnmpAccessLogIpAddress": managementSnmpAccessLogIpAddress,
       "managementSnmpAccessLogAccessRights": managementSnmpAccessLogAccessRights,
       "managementSnmpAccessLogCount": managementSnmpAccessLogCount,
       "managementSnmpLastErrorReason": managementSnmpLastErrorReason,
       "frontpanel": frontpanel,
       "frontpanelDisplay": frontpanelDisplay,
       "frontpanelKeyboardAccess": frontpanelKeyboardAccess,
       "frontpanelErrorcode": frontpanelErrorcode,
       "frontpanelErrorLED": frontpanelErrorLED,
       "frontpanelDefaultDisplay": frontpanelDefaultDisplay,
       "frontpanelKeyPress": frontpanelKeyPress,
       "frontpanelDisplayLogTable": frontpanelDisplayLogTable,
       "frontpanelDisplayLogEntry": frontpanelDisplayLogEntry,
       "frontpanelDisplayLogIndex": frontpanelDisplayLogIndex,
       "frontpanelDisplayLogTimeStamp": frontpanelDisplayLogTimeStamp,
       "frontpanelDisplayLogDisplayText": frontpanelDisplayLogDisplayText,
       "products": products,
       "tokenRingBridgeSR": tokenRingBridgeSR,
       "controlledAccessUnit": controlledAccessUnit,
       "controlledAttachmentModule": controlledAttachmentModule,
       "etherNetAttachmentHUB": etherNetAttachmentHUB,
       "tokenRingRemoteBridgeAndCAM": tokenRingRemoteBridgeAndCAM,
       "tokenRingMultiPortBridge": tokenRingMultiPortBridge,
       "desktopManagementAgent": desktopManagementAgent,
       "localPCBridge": localPCBridge,
       "remoteDOSPCBridge": remoteDOSPCBridge,
       "remoteOS2PCBridge": remoteOS2PCBridge,
       "tokenRingSwitchOc8100": tokenRingSwitchOc8100,
       "crossfireAtmSwitch": crossfireAtmSwitch,
       "ethernetSwitchOc8200": ethernetSwitchOc8200,
       "tokenRingSwitchOc8600": tokenRingSwitchOc8600,
       "tokenRingSwitchOc8007": tokenRingSwitchOc8007,
       "crossfireAtmSwitchOc8008": crossfireAtmSwitchOc8008,
       "fastEthernetSwitchOc8400": fastEthernetSwitchOc8400,
       "fastEthernetSwitchOc8420": fastEthernetSwitchOc8420,
       "lanscoutOc5020": lanscoutOc5020,
       "crossfireAtmSwitchCf9200": crossfireAtmSwitchCf9200,
       "crossfireRouterCf7100": crossfireRouterCf7100,
       "tokenRingSwitchCf8500": tokenRingSwitchCf8500,
       "ethernetSwitchCf8711": ethernetSwitchCf8711,
       "ethernetSwitchCf8720": ethernetSwitchCf8720,
       "ethernetSwitchCf8810": ethernetSwitchCf8810,
       "errorlog": errorlog,
       "errorlogTable": errorlogTable,
       "errorlogEntry": errorlogEntry,
       "errorlogNumber": errorlogNumber,
       "errorlogTimeStamp": errorlogTimeStamp,
       "errorlogErrorDescription": errorlogErrorDescription,
       "errorlogErrorData": errorlogErrorData,
       "errorlogTime": errorlogTime,
       "errorlogTimeRemoved": errorlogTimeRemoved,
       "errorlogCategory": errorlogCategory,
       "errorlogSeverity": errorlogSeverity,
       "errorlogPhysicalIf": errorlogPhysicalIf,
       "errorlogVirtualIf": errorlogVirtualIf,
       "errorlogTraceControl": errorlogTraceControl,
       "errorlogTraceMaskCurrent": errorlogTraceMaskCurrent,
       "errorlogTraceMaskInitial": errorlogTraceMaskInitial,
       "errorlogTraceMaskOperational": errorlogTraceMaskOperational,
       "errorlogTraceLogSize": errorlogTraceLogSize,
       "errorlogTraceSliceTable": errorlogTraceSliceTable,
       "errorlogTraceSliceTableEntry": errorlogTraceSliceTableEntry,
       "errorlogTraceSliceNumber": errorlogTraceSliceNumber,
       "errorlogTraceSliceSize": errorlogTraceSliceSize,
       "errorlogTraceSliceData": errorlogTraceSliceData,
       "errorlogStoredSeverityLevel": errorlogStoredSeverityLevel,
       "trconfig": trconfig,
       "trconfigTable": trconfigTable,
       "trconfigEntry": trconfigEntry,
       "trconfigIfNumber": trconfigIfNumber,
       "trconfigBurntInAddress": trconfigBurntInAddress,
       "trconfigLocalAddress": trconfigLocalAddress,
       "trconfigEarlyTokenRelease": trconfigEarlyTokenRelease}
)
