# SNMP MIB module (DCLRA-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DCLRA-MIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:25 2024
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

(DmiDate,
 DmiInteger64,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiDate",
    "DmiInteger64",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfServiceLayerMIF_ObjectIdentity = ObjectIdentity
dmtfServiceLayerMIF = _DmtfServiceLayerMIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 1)
)
_DMTFComponentIDTable_Object = MibTable
dMTFComponentIDTable = _DMTFComponentIDTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dMTFComponentIDTable.setStatus("mandatory")
_DMTFComponentIDEntry_Object = MibTableRow
dMTFComponentIDEntry = _DMTFComponentIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1)
)
dMTFComponentIDEntry.setIndexNames(
    (0, "DCLRA-MIB-MIB", "DmiCompId"),
    (0, "DCLRA-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dMTFComponentIDEntry.setStatus("mandatory")
_ManufacturerAtt1_Type = DmiDisplaystring
_ManufacturerAtt1_Object = MibTableColumn
manufacturerAtt1 = _ManufacturerAtt1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 1),
    _ManufacturerAtt1_Type()
)
manufacturerAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturerAtt1.setStatus("mandatory")
_ProductAtt2_Type = DmiDisplaystring
_ProductAtt2_Object = MibTableColumn
productAtt2 = _ProductAtt2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 2),
    _ProductAtt2_Type()
)
productAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productAtt2.setStatus("mandatory")
_VersionAtt3_Type = DmiDisplaystring
_VersionAtt3_Object = MibTableColumn
versionAtt3 = _VersionAtt3_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 3),
    _VersionAtt3_Type()
)
versionAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionAtt3.setStatus("mandatory")
_SerialNumberAtt4_Type = DmiDisplaystring
_SerialNumberAtt4_Object = MibTableColumn
serialNumberAtt4 = _SerialNumberAtt4_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 4),
    _SerialNumberAtt4_Type()
)
serialNumberAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumberAtt4.setStatus("mandatory")
_InstallationAtt5_Type = DmiDate
_InstallationAtt5_Object = MibTableColumn
installationAtt5 = _InstallationAtt5_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 5),
    _InstallationAtt5_Type()
)
installationAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installationAtt5.setStatus("mandatory")


class _VerifyAtt6_Type(Integer32):
    """Custom type verifyAtt6 based on Integer32"""
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
        *(("anErrorOccurredCheckStatusCode", 0),
          ("reserved", 3),
          ("thisComponentDoesNotExist", 1),
          ("thisComponentExistsAndIsFunctioningCorrectly", 7),
          ("thisComponentExistsAndIsNotFunctioningCorrectly", 6),
          ("thisComponentExistsButTheFunctionalityIsUnknown", 5),
          ("thisComponentExistsButTheFunctionalityIsUntested", 4),
          ("verificationIsNotSupported", 2))
    )


_VerifyAtt6_Type.__name__ = "Integer32"
_VerifyAtt6_Object = MibTableColumn
verifyAtt6 = _VerifyAtt6_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 6),
    _VerifyAtt6_Type()
)
verifyAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verifyAtt6.setStatus("mandatory")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)
_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server2_ObjectIdentity = ObjectIdentity
server2 = _Server2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10891)
)
_DellLRAActionTableTable_Object = MibTable
dellLRAActionTableTable = _DellLRAActionTableTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313)
)
if mibBuilder.loadTexts:
    dellLRAActionTableTable.setStatus("mandatory")
_DellLRAActionTableEntry_Object = MibTableRow
dellLRAActionTableEntry = _DellLRAActionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1)
)
dellLRAActionTableEntry.setIndexNames(
    (0, "DCLRA-MIB-MIB", "DmiCompId"),
    (0, "DCLRA-MIB-MIB", "DmiGroupId"),
    (0, "DCLRA-MIB-MIB", "actionNameAtt1"),
)
if mibBuilder.loadTexts:
    dellLRAActionTableEntry.setStatus("mandatory")


class _DellLRAActionTableState_Type(Integer32):
    """Custom type dellLRAActionTableState based on Integer32"""
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


_DellLRAActionTableState_Type.__name__ = "Integer32"
_DellLRAActionTableState_Object = MibTableColumn
dellLRAActionTableState = _DellLRAActionTableState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 0),
    _DellLRAActionTableState_Type()
)
dellLRAActionTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLRAActionTableState.setStatus("mandatory")


class _ActionNameAtt1_Type(Integer32):
    """Custom type actionNameAtt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              7,
              13,
              14,
              160,
              168,
              172,
              200,
              202,
              204,
              206,
              208,
              210,
              212,
              214,
              220,
              225)
        )
    )
    namedValues = NamedValues(
        *(("aPCSystemOnLowBatteryPower", 14),
          ("aPCSystemOnLowUtilityPower", 13),
          ("adaptecHostAdapterFailed", 3),
          ("adaptecLogicalUnitFailed", 7),
          ("chassisIntrusionDetected", 220),
          ("currentSensorDetectedAFailure", 206),
          ("currentSensorWarningDetected", 208),
          ("fanSensorDetectedAFailure", 168),
          ("fanSensorWarningDetected", 204),
          ("lostConnectionToDiskPod", 225),
          ("powerSupplyDegradedRedundancyDetected", 212),
          ("powerSupplyDetectedAFailure", 214),
          ("powerSupplyLostRedundancyDetected", 210),
          ("temperatureSensorDetectedAFailure", 160),
          ("temperatureSensorWarningDetected", 200),
          ("unknown", 0),
          ("voltageSensorDetectedAFailure", 172),
          ("voltageSensorWarningDetected", 202))
    )


_ActionNameAtt1_Type.__name__ = "Integer32"
_ActionNameAtt1_Object = MibTableColumn
actionNameAtt1 = _ActionNameAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 1),
    _ActionNameAtt1_Type()
)
actionNameAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionNameAtt1.setStatus("mandatory")
_ActionResponseAtt2_Type = DmiDisplaystring
_ActionResponseAtt2_Object = MibTableColumn
actionResponseAtt2 = _ActionResponseAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 2),
    _ActionResponseAtt2_Type()
)
actionResponseAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionResponseAtt2.setStatus("mandatory")
_ActionExecuteAtt3_Type = DmiDisplaystring
_ActionExecuteAtt3_Object = MibTableColumn
actionExecuteAtt3 = _ActionExecuteAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 3),
    _ActionExecuteAtt3_Type()
)
actionExecuteAtt3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionExecuteAtt3.setStatus("mandatory")
_ActionSourceAtt4_Type = DmiDisplaystring
_ActionSourceAtt4_Object = MibTableColumn
actionSourceAtt4 = _ActionSourceAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 4),
    _ActionSourceAtt4_Type()
)
actionSourceAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionSourceAtt4.setStatus("mandatory")
_UDPInformationAtt5_Type = DmiDisplaystring
_UDPInformationAtt5_Object = MibTableColumn
uDPInformationAtt5 = _UDPInformationAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 5),
    _UDPInformationAtt5_Type()
)
uDPInformationAtt5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uDPInformationAtt5.setStatus("mandatory")
_DellLRACapabilitiesTable_Object = MibTable
dellLRACapabilitiesTable = _DellLRACapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 314)
)
if mibBuilder.loadTexts:
    dellLRACapabilitiesTable.setStatus("mandatory")
_DellLRACapabilitiesEntry_Object = MibTableRow
dellLRACapabilitiesEntry = _DellLRACapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 314, 1)
)
dellLRACapabilitiesEntry.setIndexNames(
    (0, "DCLRA-MIB-MIB", "DmiCompId"),
    (0, "DCLRA-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dellLRACapabilitiesEntry.setStatus("mandatory")
_LRACapabilitiesAtt1_Type = DmiInteger
_LRACapabilitiesAtt1_Object = MibTableColumn
lRACapabilitiesAtt1 = _LRACapabilitiesAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 314, 1, 1),
    _LRACapabilitiesAtt1_Type()
)
lRACapabilitiesAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lRACapabilitiesAtt1.setStatus("mandatory")
_DellLRABeepActionTable_Object = MibTable
dellLRABeepActionTable = _DellLRABeepActionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 315)
)
if mibBuilder.loadTexts:
    dellLRABeepActionTable.setStatus("mandatory")
_DellLRABeepActionEntry_Object = MibTableRow
dellLRABeepActionEntry = _DellLRABeepActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 315, 1)
)
dellLRABeepActionEntry.setIndexNames(
    (0, "DCLRA-MIB-MIB", "DmiCompId"),
    (0, "DCLRA-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dellLRABeepActionEntry.setStatus("mandatory")
_BeepClearAtt1_Type = DmiDisplaystring
_BeepClearAtt1_Object = MibTableColumn
beepClearAtt1 = _BeepClearAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 315, 1, 1),
    _BeepClearAtt1_Type()
)
beepClearAtt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beepClearAtt1.setStatus("mandatory")
_BeepDelayAtt2_Type = DmiDisplaystring
_BeepDelayAtt2_Object = MibTableColumn
beepDelayAtt2 = _BeepDelayAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 315, 1, 2),
    _BeepDelayAtt2_Type()
)
beepDelayAtt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beepDelayAtt2.setStatus("mandatory")
_DELLSystemsManagementSoftwareTable_Object = MibTable
dELLSystemsManagementSoftwareTable = _DELLSystemsManagementSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400)
)
if mibBuilder.loadTexts:
    dELLSystemsManagementSoftwareTable.setStatus("mandatory")
_DELLSystemsManagementSoftwareEntry_Object = MibTableRow
dELLSystemsManagementSoftwareEntry = _DELLSystemsManagementSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1)
)
dELLSystemsManagementSoftwareEntry.setIndexNames(
    (0, "DCLRA-MIB-MIB", "DmiCompId"),
    (0, "DCLRA-MIB-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dELLSystemsManagementSoftwareEntry.setStatus("mandatory")
_ProductAtt1_Type = DmiDisplaystring
_ProductAtt1_Object = MibTableColumn
productAtt1 = _ProductAtt1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 1),
    _ProductAtt1_Type()
)
productAtt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productAtt1.setStatus("mandatory")
_VersionAtt2_Type = DmiDisplaystring
_VersionAtt2_Object = MibTableColumn
versionAtt2 = _VersionAtt2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 2),
    _VersionAtt2_Type()
)
versionAtt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionAtt2.setStatus("mandatory")
_BuildNumberAtt3_Type = DmiInteger
_BuildNumberAtt3_Object = MibTableColumn
buildNumberAtt3 = _BuildNumberAtt3_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 3),
    _BuildNumberAtt3_Type()
)
buildNumberAtt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildNumberAtt3.setStatus("mandatory")
_DescriptionAtt4_Type = DmiDisplaystring
_DescriptionAtt4_Object = MibTableColumn
descriptionAtt4 = _DescriptionAtt4_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 4),
    _DescriptionAtt4_Type()
)
descriptionAtt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descriptionAtt4.setStatus("mandatory")
_SupportedProtocolsAtt5_Type = DmiInteger
_SupportedProtocolsAtt5_Object = MibTableColumn
supportedProtocolsAtt5 = _SupportedProtocolsAtt5_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 5),
    _SupportedProtocolsAtt5_Type()
)
supportedProtocolsAtt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportedProtocolsAtt5.setStatus("mandatory")


class _PreferredProtocolAtt6_Type(Integer32):
    """Custom type preferredProtocolAtt6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cIMOM", 4),
          ("dMIRPC", 2),
          ("sNMP", 1))
    )


_PreferredProtocolAtt6_Type.__name__ = "Integer32"
_PreferredProtocolAtt6_Object = MibTableColumn
preferredProtocolAtt6 = _PreferredProtocolAtt6_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 6),
    _PreferredProtocolAtt6_Type()
)
preferredProtocolAtt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preferredProtocolAtt6.setStatus("mandatory")
_DMIRPCTypesAtt7_Type = DmiDisplaystring
_DMIRPCTypesAtt7_Object = MibTableColumn
dMIRPCTypesAtt7 = _DMIRPCTypesAtt7_Object(
    (1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 7),
    _DMIRPCTypesAtt7_Type()
)
dMIRPCTypesAtt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dMIRPCTypesAtt7.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCLRA-MIB-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfServiceLayerMIF": dmtfServiceLayerMIF,
       "dMTFComponentIDTable": dMTFComponentIDTable,
       "dMTFComponentIDEntry": dMTFComponentIDEntry,
       "manufacturerAtt1": manufacturerAtt1,
       "productAtt2": productAtt2,
       "versionAtt3": versionAtt3,
       "serialNumberAtt4": serialNumberAtt4,
       "installationAtt5": installationAtt5,
       "verifyAtt6": verifyAtt6,
       "dmtfDynOids": dmtfDynOids,
       "dell": dell,
       "server2": server2,
       "dellLRAActionTableTable": dellLRAActionTableTable,
       "dellLRAActionTableEntry": dellLRAActionTableEntry,
       "dellLRAActionTableState": dellLRAActionTableState,
       "actionNameAtt1": actionNameAtt1,
       "actionResponseAtt2": actionResponseAtt2,
       "actionExecuteAtt3": actionExecuteAtt3,
       "actionSourceAtt4": actionSourceAtt4,
       "uDPInformationAtt5": uDPInformationAtt5,
       "dellLRACapabilitiesTable": dellLRACapabilitiesTable,
       "dellLRACapabilitiesEntry": dellLRACapabilitiesEntry,
       "lRACapabilitiesAtt1": lRACapabilitiesAtt1,
       "dellLRABeepActionTable": dellLRABeepActionTable,
       "dellLRABeepActionEntry": dellLRABeepActionEntry,
       "beepClearAtt1": beepClearAtt1,
       "beepDelayAtt2": beepDelayAtt2,
       "dELLSystemsManagementSoftwareTable": dELLSystemsManagementSoftwareTable,
       "dELLSystemsManagementSoftwareEntry": dELLSystemsManagementSoftwareEntry,
       "productAtt1": productAtt1,
       "versionAtt2": versionAtt2,
       "buildNumberAtt3": buildNumberAtt3,
       "descriptionAtt4": descriptionAtt4,
       "supportedProtocolsAtt5": supportedProtocolsAtt5,
       "preferredProtocolAtt6": preferredProtocolAtt6,
       "dMIRPCTypesAtt7": dMIRPCTypesAtt7}
)
