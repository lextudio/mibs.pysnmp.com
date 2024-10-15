# SNMP MIB module (LUMINOUS-PROVISIONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LUMINOUS-PROVISIONING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:29 2024
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

(LumDescr,
 LumName,
 LumPortNum,
 LumSlotNum,
 LumTdmType) = mibBuilder.importSymbols(
    "LUMINOUS-TC-MIB",
    "LumDescr",
    "LumName",
    "LumPortNum",
    "LumSlotNum",
    "LumTdmType")

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
 ObjectName,
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumProvisioningMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2)
)
lumProvisioningMIB.setRevisions(
        ("1901-06-13 00:00",
         "1900-08-22 00:00",
         "1900-07-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Luminous_ObjectIdentity = ObjectIdentity
luminous = _Luminous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614)
)
_LumADM_ObjectIdentity = ObjectIdentity
lumADM = _LumADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1)
)
_LumTdmCrossConnect_ObjectIdentity = ObjectIdentity
lumTdmCrossConnect = _LumTdmCrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2)
)
_LumTdmCrossConnectTable_Object = MibTable
lumTdmCrossConnectTable = _LumTdmCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lumTdmCrossConnectTable.setStatus("current")
_LumTdmCrossConnectEntry_Object = MibTableRow
lumTdmCrossConnectEntry = _LumTdmCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1)
)
lumTdmCrossConnectEntry.setIndexNames(
    (0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalCardSlotId"),
    (0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalPortNumber"),
)
if mibBuilder.loadTexts:
    lumTdmCrossConnectEntry.setStatus("current")
_LumTdmLocalCardSlotId_Type = LumSlotNum
_LumTdmLocalCardSlotId_Object = MibTableColumn
lumTdmLocalCardSlotId = _LumTdmLocalCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 1),
    _LumTdmLocalCardSlotId_Type()
)
lumTdmLocalCardSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmLocalCardSlotId.setStatus("current")
_LumTdmLocalPortNumber_Type = LumPortNum
_LumTdmLocalPortNumber_Object = MibTableColumn
lumTdmLocalPortNumber = _LumTdmLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 2),
    _LumTdmLocalPortNumber_Type()
)
lumTdmLocalPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmLocalPortNumber.setStatus("current")


class _LumTdmConnectNodeIP_Type(IpAddress):
    """Custom type lumTdmConnectNodeIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_LumTdmConnectNodeIP_Object = MibTableColumn
lumTdmConnectNodeIP = _LumTdmConnectNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 3),
    _LumTdmConnectNodeIP_Type()
)
lumTdmConnectNodeIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectNodeIP.setStatus("current")
_LumTdmConnectCardSlotId_Type = LumSlotNum
_LumTdmConnectCardSlotId_Object = MibTableColumn
lumTdmConnectCardSlotId = _LumTdmConnectCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 4),
    _LumTdmConnectCardSlotId_Type()
)
lumTdmConnectCardSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectCardSlotId.setStatus("current")
_LumTdmConnectPortNumber_Type = LumPortNum
_LumTdmConnectPortNumber_Object = MibTableColumn
lumTdmConnectPortNumber = _LumTdmConnectPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 5),
    _LumTdmConnectPortNumber_Type()
)
lumTdmConnectPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectPortNumber.setStatus("current")


class _LumTdmConnectNumber_Type(Integer32):
    """Custom type lumTdmConnectNumber based on Integer32"""
    defaultValue = 1


_LumTdmConnectNumber_Object = MibTableColumn
lumTdmConnectNumber = _LumTdmConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 6),
    _LumTdmConnectNumber_Type()
)
lumTdmConnectNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectNumber.setStatus("current")
_LumTdmConnectionName_Type = LumDescr
_LumTdmConnectionName_Object = MibTableColumn
lumTdmConnectionName = _LumTdmConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 7),
    _LumTdmConnectionName_Type()
)
lumTdmConnectionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectionName.setStatus("current")


class _LumTdmConnectionStartTime_Type(DateAndTime):
    """Custom type lumTdmConnectionStartTime based on DateAndTime"""
    defaultValue = OctetString("00000000000")


_LumTdmConnectionStartTime_Object = MibTableColumn
lumTdmConnectionStartTime = _LumTdmConnectionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 8),
    _LumTdmConnectionStartTime_Type()
)
lumTdmConnectionStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectionStartTime.setStatus("current")


class _LumTdmConnectionStopTime_Type(DateAndTime):
    """Custom type lumTdmConnectionStopTime based on DateAndTime"""
    defaultValue = OctetString("00000000000")


_LumTdmConnectionStopTime_Object = MibTableColumn
lumTdmConnectionStopTime = _LumTdmConnectionStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 9),
    _LumTdmConnectionStopTime_Type()
)
lumTdmConnectionStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectionStopTime.setStatus("current")


class _LumTdmConnectConfigParam_Type(Integer32):
    """Custom type lumTdmConnectConfigParam based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("slc96", 2))
    )


_LumTdmConnectConfigParam_Type.__name__ = "Integer32"
_LumTdmConnectConfigParam_Object = MibTableColumn
lumTdmConnectConfigParam = _LumTdmConnectConfigParam_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 10),
    _LumTdmConnectConfigParam_Type()
)
lumTdmConnectConfigParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumTdmConnectConfigParam.setStatus("current")
_LumTdmConnectionUpTime_Type = TimeTicks
_LumTdmConnectionUpTime_Object = MibTableColumn
lumTdmConnectionUpTime = _LumTdmConnectionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 11),
    _LumTdmConnectionUpTime_Type()
)
lumTdmConnectionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumTdmConnectionUpTime.setStatus("current")
_LumTdmConnectionStatus_Type = RowStatus
_LumTdmConnectionStatus_Object = MibTableColumn
lumTdmConnectionStatus = _LumTdmConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 12),
    _LumTdmConnectionStatus_Type()
)
lumTdmConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumTdmConnectionStatus.setStatus("current")
_LumTdmConnectType_Type = LumTdmType
_LumTdmConnectType_Object = MibTableColumn
lumTdmConnectType = _LumTdmConnectType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 13),
    _LumTdmConnectType_Type()
)
lumTdmConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumTdmConnectType.setStatus("current")
_LumDPProvision_ObjectIdentity = ObjectIdentity
lumDPProvision = _LumDPProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3)
)
_LumDPProvisionTable_Object = MibTable
lumDPProvisionTable = _LumDPProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lumDPProvisionTable.setStatus("current")
_LumDPProvisionEntry_Object = MibTableRow
lumDPProvisionEntry = _LumDPProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1)
)
lumDPProvisionEntry.setIndexNames(
    (0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalCardSlotId"),
    (0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalPortNumber"),
    (0, "LUMINOUS-PROVISIONING-MIB", "lumDPConnectNumber"),
)
if mibBuilder.loadTexts:
    lumDPProvisionEntry.setStatus("current")
_LumDPLocalCardSlotId_Type = LumSlotNum
_LumDPLocalCardSlotId_Object = MibTableColumn
lumDPLocalCardSlotId = _LumDPLocalCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 1),
    _LumDPLocalCardSlotId_Type()
)
lumDPLocalCardSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPLocalCardSlotId.setStatus("current")
_LumDPLocalPortNumber_Type = LumPortNum
_LumDPLocalPortNumber_Object = MibTableColumn
lumDPLocalPortNumber = _LumDPLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 2),
    _LumDPLocalPortNumber_Type()
)
lumDPLocalPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPLocalPortNumber.setStatus("current")
_LumDPConnectNumber_Type = Integer32
_LumDPConnectNumber_Object = MibTableColumn
lumDPConnectNumber = _LumDPConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 3),
    _LumDPConnectNumber_Type()
)
lumDPConnectNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectNumber.setStatus("current")
_LumDPConnectNodeIP_Type = IpAddress
_LumDPConnectNodeIP_Object = MibTableColumn
lumDPConnectNodeIP = _LumDPConnectNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 4),
    _LumDPConnectNodeIP_Type()
)
lumDPConnectNodeIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectNodeIP.setStatus("current")
_LumDPConnectCardSlotId_Type = LumSlotNum
_LumDPConnectCardSlotId_Object = MibTableColumn
lumDPConnectCardSlotId = _LumDPConnectCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 5),
    _LumDPConnectCardSlotId_Type()
)
lumDPConnectCardSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectCardSlotId.setStatus("current")
_LumDPConnectPortNumber_Type = LumPortNum
_LumDPConnectPortNumber_Object = MibTableColumn
lumDPConnectPortNumber = _LumDPConnectPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 6),
    _LumDPConnectPortNumber_Type()
)
lumDPConnectPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectPortNumber.setStatus("current")
_LumDPConnectionName_Type = LumDescr
_LumDPConnectionName_Object = MibTableColumn
lumDPConnectionName = _LumDPConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 7),
    _LumDPConnectionName_Type()
)
lumDPConnectionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectionName.setStatus("current")


class _LumDPConnectionStartTime_Type(DateAndTime):
    """Custom type lumDPConnectionStartTime based on DateAndTime"""
    defaultValue = OctetString("00000000000")


_LumDPConnectionStartTime_Object = MibTableColumn
lumDPConnectionStartTime = _LumDPConnectionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 8),
    _LumDPConnectionStartTime_Type()
)
lumDPConnectionStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectionStartTime.setStatus("current")


class _LumDPConnectionStopTime_Type(DateAndTime):
    """Custom type lumDPConnectionStopTime based on DateAndTime"""
    defaultValue = OctetString("00000000000")


_LumDPConnectionStopTime_Object = MibTableColumn
lumDPConnectionStopTime = _LumDPConnectionStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 9),
    _LumDPConnectionStopTime_Type()
)
lumDPConnectionStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConnectionStopTime.setStatus("current")


class _LumDPCategory_Type(Integer32):
    """Custom type lumDPCategory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicIP", 3),
          ("staticIP", 2),
          ("wireModel", 1))
    )


_LumDPCategory_Type.__name__ = "Integer32"
_LumDPCategory_Object = MibTableColumn
lumDPCategory = _LumDPCategory_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 10),
    _LumDPCategory_Type()
)
lumDPCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPCategory.setStatus("current")


class _LumDPClassOfService_Type(Integer32):
    """Custom type lumDPClassOfService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assuredForwarding", 3),
          ("bestEffort", 1),
          ("expressForwarding", 2))
    )


_LumDPClassOfService_Type.__name__ = "Integer32"
_LumDPClassOfService_Object = MibTableColumn
lumDPClassOfService = _LumDPClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 11),
    _LumDPClassOfService_Type()
)
lumDPClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPClassOfService.setStatus("current")
_LumDPPeakBandwidth_Type = Integer32
_LumDPPeakBandwidth_Object = MibTableColumn
lumDPPeakBandwidth = _LumDPPeakBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 12),
    _LumDPPeakBandwidth_Type()
)
lumDPPeakBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPPeakBandwidth.setStatus("current")
_LumDPSustainedBandwidth_Type = Integer32
_LumDPSustainedBandwidth_Object = MibTableColumn
lumDPSustainedBandwidth = _LumDPSustainedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 13),
    _LumDPSustainedBandwidth_Type()
)
lumDPSustainedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPSustainedBandwidth.setStatus("current")
_LumDPMaximumBurstSize_Type = Integer32
_LumDPMaximumBurstSize_Object = MibTableColumn
lumDPMaximumBurstSize = _LumDPMaximumBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 14),
    _LumDPMaximumBurstSize_Type()
)
lumDPMaximumBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPMaximumBurstSize.setStatus("current")


class _LumDPNonConformingAction_Type(Integer32):
    """Custom type lumDPNonConformingAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("markDown", 2),
          ("off", 1))
    )


_LumDPNonConformingAction_Type.__name__ = "Integer32"
_LumDPNonConformingAction_Object = MibTableColumn
lumDPNonConformingAction = _LumDPNonConformingAction_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 15),
    _LumDPNonConformingAction_Type()
)
lumDPNonConformingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPNonConformingAction.setStatus("current")


class _LumDPProtectionType_Type(Integer32):
    """Custom type lumDPProtectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 2),
          ("unprotected", 1))
    )


_LumDPProtectionType_Type.__name__ = "Integer32"
_LumDPProtectionType_Object = MibTableColumn
lumDPProtectionType = _LumDPProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 16),
    _LumDPProtectionType_Type()
)
lumDPProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPProtectionType.setStatus("current")
_LumDPFacilityProtection_Type = Integer32
_LumDPFacilityProtection_Object = MibTableColumn
lumDPFacilityProtection = _LumDPFacilityProtection_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 17),
    _LumDPFacilityProtection_Type()
)
lumDPFacilityProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPFacilityProtection.setStatus("current")
_LumDPIpPrefix1_Type = IpAddress
_LumDPIpPrefix1_Object = MibTableColumn
lumDPIpPrefix1 = _LumDPIpPrefix1_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 18),
    _LumDPIpPrefix1_Type()
)
lumDPIpPrefix1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPIpPrefix1.setStatus("current")
_LumDPIpPrefix2_Type = IpAddress
_LumDPIpPrefix2_Object = MibTableColumn
lumDPIpPrefix2 = _LumDPIpPrefix2_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 19),
    _LumDPIpPrefix2_Type()
)
lumDPIpPrefix2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPIpPrefix2.setStatus("current")
_LumDPIpPrefix3_Type = IpAddress
_LumDPIpPrefix3_Object = MibTableColumn
lumDPIpPrefix3 = _LumDPIpPrefix3_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 20),
    _LumDPIpPrefix3_Type()
)
lumDPIpPrefix3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPIpPrefix3.setStatus("current")
_LumDPConfigFile_Type = DisplayString
_LumDPConfigFile_Object = MibTableColumn
lumDPConfigFile = _LumDPConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 21),
    _LumDPConfigFile_Type()
)
lumDPConfigFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPConfigFile.setStatus("current")
_LumDPVLANId_Type = Integer32
_LumDPVLANId_Object = MibTableColumn
lumDPVLANId = _LumDPVLANId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 22),
    _LumDPVLANId_Type()
)
lumDPVLANId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPVLANId.setStatus("current")
_LumDPBufferSize_Type = Integer32
_LumDPBufferSize_Object = MibTableColumn
lumDPBufferSize = _LumDPBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 23),
    _LumDPBufferSize_Type()
)
lumDPBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lumDPBufferSize.setStatus("current")
_LumDPConnectionUpTime_Type = TimeTicks
_LumDPConnectionUpTime_Object = MibTableColumn
lumDPConnectionUpTime = _LumDPConnectionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 24),
    _LumDPConnectionUpTime_Type()
)
lumDPConnectionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumDPConnectionUpTime.setStatus("current")
_LumDPConnectionStatus_Type = RowStatus
_LumDPConnectionStatus_Object = MibTableColumn
lumDPConnectionStatus = _LumDPConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 25),
    _LumDPConnectionStatus_Type()
)
lumDPConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDPConnectionStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUMINOUS-PROVISIONING-MIB",
    **{"luminous": luminous,
       "lumADM": lumADM,
       "lumProvisioningMIB": lumProvisioningMIB,
       "lumTdmCrossConnect": lumTdmCrossConnect,
       "lumTdmCrossConnectTable": lumTdmCrossConnectTable,
       "lumTdmCrossConnectEntry": lumTdmCrossConnectEntry,
       "lumTdmLocalCardSlotId": lumTdmLocalCardSlotId,
       "lumTdmLocalPortNumber": lumTdmLocalPortNumber,
       "lumTdmConnectNodeIP": lumTdmConnectNodeIP,
       "lumTdmConnectCardSlotId": lumTdmConnectCardSlotId,
       "lumTdmConnectPortNumber": lumTdmConnectPortNumber,
       "lumTdmConnectNumber": lumTdmConnectNumber,
       "lumTdmConnectionName": lumTdmConnectionName,
       "lumTdmConnectionStartTime": lumTdmConnectionStartTime,
       "lumTdmConnectionStopTime": lumTdmConnectionStopTime,
       "lumTdmConnectConfigParam": lumTdmConnectConfigParam,
       "lumTdmConnectionUpTime": lumTdmConnectionUpTime,
       "lumTdmConnectionStatus": lumTdmConnectionStatus,
       "lumTdmConnectType": lumTdmConnectType,
       "lumDPProvision": lumDPProvision,
       "lumDPProvisionTable": lumDPProvisionTable,
       "lumDPProvisionEntry": lumDPProvisionEntry,
       "lumDPLocalCardSlotId": lumDPLocalCardSlotId,
       "lumDPLocalPortNumber": lumDPLocalPortNumber,
       "lumDPConnectNumber": lumDPConnectNumber,
       "lumDPConnectNodeIP": lumDPConnectNodeIP,
       "lumDPConnectCardSlotId": lumDPConnectCardSlotId,
       "lumDPConnectPortNumber": lumDPConnectPortNumber,
       "lumDPConnectionName": lumDPConnectionName,
       "lumDPConnectionStartTime": lumDPConnectionStartTime,
       "lumDPConnectionStopTime": lumDPConnectionStopTime,
       "lumDPCategory": lumDPCategory,
       "lumDPClassOfService": lumDPClassOfService,
       "lumDPPeakBandwidth": lumDPPeakBandwidth,
       "lumDPSustainedBandwidth": lumDPSustainedBandwidth,
       "lumDPMaximumBurstSize": lumDPMaximumBurstSize,
       "lumDPNonConformingAction": lumDPNonConformingAction,
       "lumDPProtectionType": lumDPProtectionType,
       "lumDPFacilityProtection": lumDPFacilityProtection,
       "lumDPIpPrefix1": lumDPIpPrefix1,
       "lumDPIpPrefix2": lumDPIpPrefix2,
       "lumDPIpPrefix3": lumDPIpPrefix3,
       "lumDPConfigFile": lumDPConfigFile,
       "lumDPVLANId": lumDPVLANId,
       "lumDPBufferSize": lumDPBufferSize,
       "lumDPConnectionUpTime": lumDPConnectionUpTime,
       "lumDPConnectionStatus": lumDPConnectionStatus}
)
