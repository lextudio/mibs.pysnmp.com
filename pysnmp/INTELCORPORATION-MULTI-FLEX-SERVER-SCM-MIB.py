# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:10 2024
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

(chassis,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    "chassis")

(groups,
 regModule) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "groups",
    "regModule")

(FaultLedStates,
 INT32withException,
 IdromBinary16,
 Index,
 Power,
 PowerLedStates,
 Presence) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "FaultLedStates",
    "INT32withException",
    "IdromBinary16",
    "Index",
    "Power",
    "PowerLedStates",
    "Presence")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerScmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 14)
)
multiFlexServerScmMibModule.setRevisions(
        ("2007-09-29 00:00",
         "2007-08-16 13:00",
         "2007-08-10 15:30",
         "2007-08-06 13:00",
         "2007-07-16 13:30",
         "2007-06-18 13:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-23 11:00",
         "2007-05-17 11:30",
         "2007-04-18 19:05",
         "2007-04-09 10:30",
         "2007-03-12 18:00",
         "2007-03-10 18:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2007-01-15 17:00",
         "2007-01-05 10:20",
         "2006-12-28 15:30",
         "2006-12-08 13:30",
         "2006-12-05 10:30",
         "2006-12-04 16:00",
         "2006-11-28 15:30",
         "2006-11-07 07:01",
         "2006-10-02 06:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxScms_Type = Unsigned32
_MaxScms_Object = MibScalar
maxScms = _MaxScms_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 14),
    _MaxScms_Type()
)
maxScms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxScms.setStatus("current")
_NumOfScms_Type = Integer32
_NumOfScms_Object = MibScalar
numOfScms = _NumOfScms_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 24),
    _NumOfScms_Type()
)
numOfScms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfScms.setStatus("current")
_ScmPresenceMask_Type = DisplayString
_ScmPresenceMask_Object = MibScalar
scmPresenceMask = _ScmPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 34),
    _ScmPresenceMask_Type()
)
scmPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPresenceMask.setStatus("current")
_Scms_ObjectIdentity = ObjectIdentity
scms = _Scms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204)
)
if mibBuilder.loadTexts:
    scms.setStatus("current")
_ScmTable_Object = MibTable
scmTable = _ScmTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1)
)
if mibBuilder.loadTexts:
    scmTable.setStatus("current")
_ScmEntry_Object = MibTableRow
scmEntry = _ScmEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1)
)
scmEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmIndex"),
)
if mibBuilder.loadTexts:
    scmEntry.setStatus("current")
_ScmIndex_Type = Index
_ScmIndex_Object = MibTableColumn
scmIndex = _ScmIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 1),
    _ScmIndex_Type()
)
scmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmIndex.setStatus("current")
_ScmPresence_Type = Presence
_ScmPresence_Object = MibTableColumn
scmPresence = _ScmPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 2),
    _ScmPresence_Type()
)
scmPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPresence.setStatus("current")
_ScmVendor_Type = DisplayString
_ScmVendor_Object = MibTableColumn
scmVendor = _ScmVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 3),
    _ScmVendor_Type()
)
scmVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmVendor.setStatus("current")
_ScmMfgDate_Type = DisplayString
_ScmMfgDate_Object = MibTableColumn
scmMfgDate = _ScmMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 4),
    _ScmMfgDate_Type()
)
scmMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMfgDate.setStatus("current")
_ScmDeviceName_Type = DisplayString
_ScmDeviceName_Object = MibTableColumn
scmDeviceName = _ScmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 5),
    _ScmDeviceName_Type()
)
scmDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDeviceName.setStatus("current")
_ScmPart_Type = IdromBinary16
_ScmPart_Object = MibTableColumn
scmPart = _ScmPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 6),
    _ScmPart_Type()
)
scmPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPart.setStatus("current")
_ScmSerialNo_Type = IdromBinary16
_ScmSerialNo_Object = MibTableColumn
scmSerialNo = _ScmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 7),
    _ScmSerialNo_Type()
)
scmSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmSerialNo.setStatus("current")
_ScmMaximumPower_Type = Power
_ScmMaximumPower_Object = MibTableColumn
scmMaximumPower = _ScmMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 8),
    _ScmMaximumPower_Type()
)
scmMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMaximumPower.setStatus("current")
_ScmNominalPower_Type = Power
_ScmNominalPower_Object = MibTableColumn
scmNominalPower = _ScmNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 9),
    _ScmNominalPower_Type()
)
scmNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNominalPower.setStatus("current")
_ScmAssetTag_Type = IdromBinary16
_ScmAssetTag_Object = MibTableColumn
scmAssetTag = _ScmAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 10),
    _ScmAssetTag_Type()
)
scmAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmAssetTag.setStatus("current")
_ScmManagementMac_Type = PhysAddress
_ScmManagementMac_Object = MibTableColumn
scmManagementMac = _ScmManagementMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 11),
    _ScmManagementMac_Type()
)
scmManagementMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmManagementMac.setStatus("current")
_ScmWWN_Type = DisplayString
_ScmWWN_Object = MibTableColumn
scmWWN = _ScmWWN_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 12),
    _ScmWWN_Type()
)
scmWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmWWN.setStatus("current")


class _ScmSCSIProtocol_Type(Integer32):
    """Custom type scmSCSIProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("other", 1),
          ("scsi2", 2),
          ("scsi3", 3),
          ("unknown", -16))
    )


_ScmSCSIProtocol_Type.__name__ = "Integer32"
_ScmSCSIProtocol_Object = MibTableColumn
scmSCSIProtocol = _ScmSCSIProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 13),
    _ScmSCSIProtocol_Type()
)
scmSCSIProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmSCSIProtocol.setStatus("current")
_ScmPowerLed_Type = PowerLedStates
_ScmPowerLed_Object = MibTableColumn
scmPowerLed = _ScmPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 14),
    _ScmPowerLed_Type()
)
scmPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPowerLed.setStatus("current")
_ScmFaultLed_Type = FaultLedStates
_ScmFaultLed_Object = MibTableColumn
scmFaultLed = _ScmFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 15),
    _ScmFaultLed_Type()
)
scmFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmFaultLed.setStatus("current")
_ScmFirmwareVersion_Type = DisplayString
_ScmFirmwareVersion_Object = MibTableColumn
scmFirmwareVersion = _ScmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 16),
    _ScmFirmwareVersion_Type()
)
scmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmFirmwareVersion.setStatus("current")
_ScmOpStatus_Type = DisplayString
_ScmOpStatus_Object = MibTableColumn
scmOpStatus = _ScmOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 17),
    _ScmOpStatus_Type()
)
scmOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmOpStatus.setStatus("current")


class _ScmRole_Type(Integer32):
    """Custom type scmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("primary", 1),
          ("secondary", 0),
          ("unavailable", -1),
          ("unknown", -16))
    )


_ScmRole_Type.__name__ = "Integer32"
_ScmRole_Object = MibTableColumn
scmRole = _ScmRole_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 18),
    _ScmRole_Type()
)
scmRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmRole.setStatus("current")
_ScmReadinessStatus_Type = DisplayString
_ScmReadinessStatus_Object = MibTableColumn
scmReadinessStatus = _ScmReadinessStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 19),
    _ScmReadinessStatus_Type()
)
scmReadinessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmReadinessStatus.setStatus("current")
_ScmNumOfPoolsPresent_Type = INT32withException
_ScmNumOfPoolsPresent_Object = MibTableColumn
scmNumOfPoolsPresent = _ScmNumOfPoolsPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 20),
    _ScmNumOfPoolsPresent_Type()
)
scmNumOfPoolsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPoolsPresent.setStatus("current")
_ScmNumOfPhysicalDrivesPresent_Type = INT32withException
_ScmNumOfPhysicalDrivesPresent_Object = MibTableColumn
scmNumOfPhysicalDrivesPresent = _ScmNumOfPhysicalDrivesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 21),
    _ScmNumOfPhysicalDrivesPresent_Type()
)
scmNumOfPhysicalDrivesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesPresent.setStatus("current")
_ScmNumOfPhysicalDrivesOnline_Type = INT32withException
_ScmNumOfPhysicalDrivesOnline_Object = MibTableColumn
scmNumOfPhysicalDrivesOnline = _ScmNumOfPhysicalDrivesOnline_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 22),
    _ScmNumOfPhysicalDrivesOnline_Type()
)
scmNumOfPhysicalDrivesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesOnline.setStatus("current")
_ScmNumOfPhysicalDrivesOffline_Type = INT32withException
_ScmNumOfPhysicalDrivesOffline_Object = MibTableColumn
scmNumOfPhysicalDrivesOffline = _ScmNumOfPhysicalDrivesOffline_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 23),
    _ScmNumOfPhysicalDrivesOffline_Type()
)
scmNumOfPhysicalDrivesOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesOffline.setStatus("current")
_ScmNumOfPhysicalDrivesWithPFA_Type = INT32withException
_ScmNumOfPhysicalDrivesWithPFA_Object = MibTableColumn
scmNumOfPhysicalDrivesWithPFA = _ScmNumOfPhysicalDrivesWithPFA_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 24),
    _ScmNumOfPhysicalDrivesWithPFA_Type()
)
scmNumOfPhysicalDrivesWithPFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesWithPFA.setStatus("current")
_ScmNumOfPhysicalDrivesRebuilding_Type = INT32withException
_ScmNumOfPhysicalDrivesRebuilding_Object = MibTableColumn
scmNumOfPhysicalDrivesRebuilding = _ScmNumOfPhysicalDrivesRebuilding_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 25),
    _ScmNumOfPhysicalDrivesRebuilding_Type()
)
scmNumOfPhysicalDrivesRebuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesRebuilding.setStatus("current")
_ScmNumOfPhysicalDrivesMissing_Type = INT32withException
_ScmNumOfPhysicalDrivesMissing_Object = MibTableColumn
scmNumOfPhysicalDrivesMissing = _ScmNumOfPhysicalDrivesMissing_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 26),
    _ScmNumOfPhysicalDrivesMissing_Type()
)
scmNumOfPhysicalDrivesMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesMissing.setStatus("current")
_ScmNumOfPhysicalDrivesUnconfigured_Type = INT32withException
_ScmNumOfPhysicalDrivesUnconfigured_Object = MibTableColumn
scmNumOfPhysicalDrivesUnconfigured = _ScmNumOfPhysicalDrivesUnconfigured_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 27),
    _ScmNumOfPhysicalDrivesUnconfigured_Type()
)
scmNumOfPhysicalDrivesUnconfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfPhysicalDrivesUnconfigured.setStatus("current")
_ScmNumOfVirtualDrivesPresent_Type = INT32withException
_ScmNumOfVirtualDrivesPresent_Object = MibTableColumn
scmNumOfVirtualDrivesPresent = _ScmNumOfVirtualDrivesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 28),
    _ScmNumOfVirtualDrivesPresent_Type()
)
scmNumOfVirtualDrivesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfVirtualDrivesPresent.setStatus("current")
_ScmNumOfVirtualDrivesOnline_Type = INT32withException
_ScmNumOfVirtualDrivesOnline_Object = MibTableColumn
scmNumOfVirtualDrivesOnline = _ScmNumOfVirtualDrivesOnline_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 29),
    _ScmNumOfVirtualDrivesOnline_Type()
)
scmNumOfVirtualDrivesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfVirtualDrivesOnline.setStatus("current")
_ScmNumOfVirtualDrivesOffline_Type = INT32withException
_ScmNumOfVirtualDrivesOffline_Object = MibTableColumn
scmNumOfVirtualDrivesOffline = _ScmNumOfVirtualDrivesOffline_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 30),
    _ScmNumOfVirtualDrivesOffline_Type()
)
scmNumOfVirtualDrivesOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfVirtualDrivesOffline.setStatus("current")
_ScmNumOfVirtualDrivesCritical_Type = INT32withException
_ScmNumOfVirtualDrivesCritical_Object = MibTableColumn
scmNumOfVirtualDrivesCritical = _ScmNumOfVirtualDrivesCritical_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 31),
    _ScmNumOfVirtualDrivesCritical_Type()
)
scmNumOfVirtualDrivesCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfVirtualDrivesCritical.setStatus("current")
_ScmNumOfGlobalSparesPresent_Type = INT32withException
_ScmNumOfGlobalSparesPresent_Object = MibTableColumn
scmNumOfGlobalSparesPresent = _ScmNumOfGlobalSparesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 32),
    _ScmNumOfGlobalSparesPresent_Type()
)
scmNumOfGlobalSparesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfGlobalSparesPresent.setStatus("current")
_ScmNumOfDedicatedSparesPresent_Type = INT32withException
_ScmNumOfDedicatedSparesPresent_Object = MibTableColumn
scmNumOfDedicatedSparesPresent = _ScmNumOfDedicatedSparesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 33),
    _ScmNumOfDedicatedSparesPresent_Type()
)
scmNumOfDedicatedSparesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfDedicatedSparesPresent.setStatus("current")
_ScmNumOfRevertibleGlobalSparesPresent_Type = INT32withException
_ScmNumOfRevertibleGlobalSparesPresent_Object = MibTableColumn
scmNumOfRevertibleGlobalSparesPresent = _ScmNumOfRevertibleGlobalSparesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 34),
    _ScmNumOfRevertibleGlobalSparesPresent_Type()
)
scmNumOfRevertibleGlobalSparesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfRevertibleGlobalSparesPresent.setStatus("current")
_ScmNumOfRevertibleGlobalSparesUsed_Type = INT32withException
_ScmNumOfRevertibleGlobalSparesUsed_Object = MibTableColumn
scmNumOfRevertibleGlobalSparesUsed = _ScmNumOfRevertibleGlobalSparesUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 35),
    _ScmNumOfRevertibleGlobalSparesUsed_Type()
)
scmNumOfRevertibleGlobalSparesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfRevertibleGlobalSparesUsed.setStatus("current")
_ScmNumOfRevertibleDedicatedSparesPresent_Type = INT32withException
_ScmNumOfRevertibleDedicatedSparesPresent_Object = MibTableColumn
scmNumOfRevertibleDedicatedSparesPresent = _ScmNumOfRevertibleDedicatedSparesPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 36),
    _ScmNumOfRevertibleDedicatedSparesPresent_Type()
)
scmNumOfRevertibleDedicatedSparesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfRevertibleDedicatedSparesPresent.setStatus("current")
_ScmNumOfRevertibleDedicatedSparesUsed_Type = INT32withException
_ScmNumOfRevertibleDedicatedSparesUsed_Object = MibTableColumn
scmNumOfRevertibleDedicatedSparesUsed = _ScmNumOfRevertibleDedicatedSparesUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 37),
    _ScmNumOfRevertibleDedicatedSparesUsed_Type()
)
scmNumOfRevertibleDedicatedSparesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfRevertibleDedicatedSparesUsed.setStatus("current")
_ScmNumOfBGAs_Type = INT32withException
_ScmNumOfBGAs_Object = MibTableColumn
scmNumOfBGAs = _ScmNumOfBGAs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 38),
    _ScmNumOfBGAs_Type()
)
scmNumOfBGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNumOfBGAs.setStatus("current")
_ScmPowerOnHours_Type = INT32withException
_ScmPowerOnHours_Object = MibTableColumn
scmPowerOnHours = _ScmPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 39),
    _ScmPowerOnHours_Type()
)
scmPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPowerOnHours.setStatus("current")
_ScmDirtyCachePercentage_Type = INT32withException
_ScmDirtyCachePercentage_Object = MibTableColumn
scmDirtyCachePercentage = _ScmDirtyCachePercentage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 40),
    _ScmDirtyCachePercentage_Type()
)
scmDirtyCachePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDirtyCachePercentage.setStatus("current")
_ScmCacheUsagePercentage_Type = INT32withException
_ScmCacheUsagePercentage_Object = MibTableColumn
scmCacheUsagePercentage = _ScmCacheUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 1, 1, 41),
    _ScmCacheUsagePercentage_Type()
)
scmCacheUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCacheUsagePercentage.setStatus("current")
_ScmStatsTable_Object = MibTable
scmStatsTable = _ScmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2)
)
if mibBuilder.loadTexts:
    scmStatsTable.setStatus("current")
_ScmStatsEntry_Object = MibTableRow
scmStatsEntry = _ScmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1)
)
if mibBuilder.loadTexts:
    scmStatsEntry.setStatus("current")
_ScmStatsDataTransferred_Type = Counter64
_ScmStatsDataTransferred_Object = MibTableColumn
scmStatsDataTransferred = _ScmStatsDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 1),
    _ScmStatsDataTransferred_Type()
)
scmStatsDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsDataTransferred.setStatus("current")
_ScmStatsReadDataTransferred_Type = Counter64
_ScmStatsReadDataTransferred_Object = MibTableColumn
scmStatsReadDataTransferred = _ScmStatsReadDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 2),
    _ScmStatsReadDataTransferred_Type()
)
scmStatsReadDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsReadDataTransferred.setStatus("current")
_ScmStatsWriteDataTransferred_Type = Counter64
_ScmStatsWriteDataTransferred_Object = MibTableColumn
scmStatsWriteDataTransferred = _ScmStatsWriteDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 3),
    _ScmStatsWriteDataTransferred_Type()
)
scmStatsWriteDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsWriteDataTransferred.setStatus("current")
_ScmStatsNumOfErrors_Type = Integer32
_ScmStatsNumOfErrors_Object = MibTableColumn
scmStatsNumOfErrors = _ScmStatsNumOfErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 4),
    _ScmStatsNumOfErrors_Type()
)
scmStatsNumOfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfErrors.setStatus("current")
_ScmStatsNumOfNonRWErrors_Type = Integer32
_ScmStatsNumOfNonRWErrors_Object = MibTableColumn
scmStatsNumOfNonRWErrors = _ScmStatsNumOfNonRWErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 5),
    _ScmStatsNumOfNonRWErrors_Type()
)
scmStatsNumOfNonRWErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfNonRWErrors.setStatus("current")
_ScmStatsNumOfReadErrors_Type = Integer32
_ScmStatsNumOfReadErrors_Object = MibTableColumn
scmStatsNumOfReadErrors = _ScmStatsNumOfReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 6),
    _ScmStatsNumOfReadErrors_Type()
)
scmStatsNumOfReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfReadErrors.setStatus("current")
_ScmStatsNumOfWriteErrors_Type = Integer32
_ScmStatsNumOfWriteErrors_Object = MibTableColumn
scmStatsNumOfWriteErrors = _ScmStatsNumOfWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 7),
    _ScmStatsNumOfWriteErrors_Type()
)
scmStatsNumOfWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfWriteErrors.setStatus("current")
_ScmStatsNumOfIORequests_Type = Counter64
_ScmStatsNumOfIORequests_Object = MibTableColumn
scmStatsNumOfIORequests = _ScmStatsNumOfIORequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 8),
    _ScmStatsNumOfIORequests_Type()
)
scmStatsNumOfIORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfIORequests.setStatus("current")
_ScmStatsNumOfNonRWRequests_Type = Counter64
_ScmStatsNumOfNonRWRequests_Object = MibTableColumn
scmStatsNumOfNonRWRequests = _ScmStatsNumOfNonRWRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 9),
    _ScmStatsNumOfNonRWRequests_Type()
)
scmStatsNumOfNonRWRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfNonRWRequests.setStatus("current")
_ScmStatsNumOfReadRequests_Type = Counter64
_ScmStatsNumOfReadRequests_Object = MibTableColumn
scmStatsNumOfReadRequests = _ScmStatsNumOfReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 10),
    _ScmStatsNumOfReadRequests_Type()
)
scmStatsNumOfReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfReadRequests.setStatus("current")
_ScmStatsNumOfWriteRequests_Type = Counter64
_ScmStatsNumOfWriteRequests_Object = MibTableColumn
scmStatsNumOfWriteRequests = _ScmStatsNumOfWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 11),
    _ScmStatsNumOfWriteRequests_Type()
)
scmStatsNumOfWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsNumOfWriteRequests.setStatus("current")
_ScmStatsStartTime_Type = Counter64
_ScmStatsStartTime_Object = MibTableColumn
scmStatsStartTime = _ScmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 12),
    _ScmStatsStartTime_Type()
)
scmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsStartTime.setStatus("current")
_ScmStatsCollectionTime_Type = Counter64
_ScmStatsCollectionTime_Object = MibTableColumn
scmStatsCollectionTime = _ScmStatsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 2, 1, 13),
    _ScmStatsCollectionTime_Type()
)
scmStatsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmStatsCollectionTime.setStatus("current")
_ScmBatteryTable_Object = MibTable
scmBatteryTable = _ScmBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3)
)
if mibBuilder.loadTexts:
    scmBatteryTable.setStatus("current")
_ScmBatteryEntry_Object = MibTableRow
scmBatteryEntry = _ScmBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1)
)
if mibBuilder.loadTexts:
    scmBatteryEntry.setStatus("current")
_ScmBatteryPresence_Type = Presence
_ScmBatteryPresence_Object = MibTableColumn
scmBatteryPresence = _ScmBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 1),
    _ScmBatteryPresence_Type()
)
scmBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryPresence.setStatus("current")
_ScmBatteryVendor_Type = DisplayString
_ScmBatteryVendor_Object = MibTableColumn
scmBatteryVendor = _ScmBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 2),
    _ScmBatteryVendor_Type()
)
scmBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryVendor.setStatus("current")
_ScmBatteryMfgDate_Type = DisplayString
_ScmBatteryMfgDate_Object = MibTableColumn
scmBatteryMfgDate = _ScmBatteryMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 3),
    _ScmBatteryMfgDate_Type()
)
scmBatteryMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryMfgDate.setStatus("current")
_ScmBatteryDeviceName_Type = DisplayString
_ScmBatteryDeviceName_Object = MibTableColumn
scmBatteryDeviceName = _ScmBatteryDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 4),
    _ScmBatteryDeviceName_Type()
)
scmBatteryDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryDeviceName.setStatus("current")
_ScmBatteryPart_Type = IdromBinary16
_ScmBatteryPart_Object = MibTableColumn
scmBatteryPart = _ScmBatteryPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 5),
    _ScmBatteryPart_Type()
)
scmBatteryPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryPart.setStatus("current")
_ScmBatterySerialNo_Type = IdromBinary16
_ScmBatterySerialNo_Object = MibTableColumn
scmBatterySerialNo = _ScmBatterySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 6),
    _ScmBatterySerialNo_Type()
)
scmBatterySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatterySerialNo.setStatus("current")
_ScmBatteryMaximumPower_Type = Power
_ScmBatteryMaximumPower_Object = MibTableColumn
scmBatteryMaximumPower = _ScmBatteryMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 7),
    _ScmBatteryMaximumPower_Type()
)
scmBatteryMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryMaximumPower.setStatus("current")
_ScmBatteryNominalPower_Type = Power
_ScmBatteryNominalPower_Object = MibTableColumn
scmBatteryNominalPower = _ScmBatteryNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 8),
    _ScmBatteryNominalPower_Type()
)
scmBatteryNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryNominalPower.setStatus("current")
_ScmBatteryAssetTag_Type = IdromBinary16
_ScmBatteryAssetTag_Object = MibTableColumn
scmBatteryAssetTag = _ScmBatteryAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 9),
    _ScmBatteryAssetTag_Type()
)
scmBatteryAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryAssetTag.setStatus("current")
_ScmBatteryDeviceChemistry_Type = DisplayString
_ScmBatteryDeviceChemistry_Object = MibTableColumn
scmBatteryDeviceChemistry = _ScmBatteryDeviceChemistry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 10),
    _ScmBatteryDeviceChemistry_Type()
)
scmBatteryDeviceChemistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryDeviceChemistry.setStatus("current")
_ScmBatteryTemperature_Type = INT32withException
_ScmBatteryTemperature_Object = MibTableColumn
scmBatteryTemperature = _ScmBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 11),
    _ScmBatteryTemperature_Type()
)
scmBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryTemperature.setStatus("current")
_ScmBatteryTempChargeThreshold_Type = INT32withException
_ScmBatteryTempChargeThreshold_Object = MibTableColumn
scmBatteryTempChargeThreshold = _ScmBatteryTempChargeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 12),
    _ScmBatteryTempChargeThreshold_Type()
)
scmBatteryTempChargeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryTempChargeThreshold.setStatus("current")
_ScmBatteryTempDisChargeThreshold_Type = INT32withException
_ScmBatteryTempDisChargeThreshold_Object = MibTableColumn
scmBatteryTempDisChargeThreshold = _ScmBatteryTempDisChargeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 13),
    _ScmBatteryTempDisChargeThreshold_Type()
)
scmBatteryTempDisChargeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryTempDisChargeThreshold.setStatus("current")
_ScmBatteryCycleCount_Type = INT32withException
_ScmBatteryCycleCount_Object = MibTableColumn
scmBatteryCycleCount = _ScmBatteryCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 14),
    _ScmBatteryCycleCount_Type()
)
scmBatteryCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryCycleCount.setStatus("current")
_ScmBatteryRemainCapacity_Type = INT32withException
_ScmBatteryRemainCapacity_Object = MibTableColumn
scmBatteryRemainCapacity = _ScmBatteryRemainCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 15),
    _ScmBatteryRemainCapacity_Type()
)
scmBatteryRemainCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryRemainCapacity.setStatus("current")
_ScmBatteryVoltage_Type = INT32withException
_ScmBatteryVoltage_Object = MibTableColumn
scmBatteryVoltage = _ScmBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 16),
    _ScmBatteryVoltage_Type()
)
scmBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryVoltage.setStatus("current")
_ScmBatteryCurrent_Type = INT32withException
_ScmBatteryCurrent_Object = MibTableColumn
scmBatteryCurrent = _ScmBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 17),
    _ScmBatteryCurrent_Type()
)
scmBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryCurrent.setStatus("current")
_ScmBatteryStatus_Type = DisplayString
_ScmBatteryStatus_Object = MibTableColumn
scmBatteryStatus = _ScmBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 18),
    _ScmBatteryStatus_Type()
)
scmBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryStatus.setStatus("current")


class _ScmBatteryCellType_Type(Integer32):
    """Custom type scmBatteryCellType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourCell", 4),
          ("notApplicable", -32),
          ("twoCell", 2),
          ("unknown", -16))
    )


_ScmBatteryCellType_Type.__name__ = "Integer32"
_ScmBatteryCellType_Object = MibTableColumn
scmBatteryCellType = _ScmBatteryCellType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 19),
    _ScmBatteryCellType_Type()
)
scmBatteryCellType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryCellType.setStatus("current")
_ScmBatteryHoldTime_Type = INT32withException
_ScmBatteryHoldTime_Object = MibTableColumn
scmBatteryHoldTime = _ScmBatteryHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 204, 3, 1, 20),
    _ScmBatteryHoldTime_Type()
)
scmBatteryHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBatteryHoldTime.setStatus("current")
scmEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB",
     "scmStatsEntry")
)
scmStatsEntry.setIndexNames(*scmEntry.getIndexNames())
scmEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB",
     "scmBatteryEntry")
)
scmBatteryEntry.setIndexNames(*scmEntry.getIndexNames())

# Managed Objects groups

ctlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 14)
)
ctlGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "maxScms"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "numOfScms"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmManagementMac"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmWWN"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmSCSIProtocol"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmPowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmFirmwareVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmOpStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmRole"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmReadinessStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPoolsPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesOnline"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesOffline"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesWithPFA"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesRebuilding"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesMissing"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfPhysicalDrivesUnconfigured"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfVirtualDrivesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfVirtualDrivesOnline"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfVirtualDrivesOffline"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfVirtualDrivesCritical"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfGlobalSparesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfDedicatedSparesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfRevertibleGlobalSparesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfRevertibleGlobalSparesUsed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfRevertibleDedicatedSparesPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfRevertibleDedicatedSparesUsed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmNumOfBGAs"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmPowerOnHours"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmDirtyCachePercentage"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmCacheUsagePercentage"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsReadDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsWriteDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfNonRWErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfReadErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfWriteErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfIORequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfNonRWRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfReadRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsNumOfWriteRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsStartTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmStatsCollectionTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatterySerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryDeviceChemistry"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryTemperature"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryTempChargeThreshold"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryTempDisChargeThreshold"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryCycleCount"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryRemainCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryVoltage"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryCurrent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryCellType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB", "scmBatteryHoldTime"))
)
if mibBuilder.loadTexts:
    ctlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-SCM-MIB",
    **{"multiFlexServerScmMibModule": multiFlexServerScmMibModule,
       "ctlGroup": ctlGroup,
       "maxScms": maxScms,
       "numOfScms": numOfScms,
       "scmPresenceMask": scmPresenceMask,
       "scms": scms,
       "scmTable": scmTable,
       "scmEntry": scmEntry,
       "scmIndex": scmIndex,
       "scmPresence": scmPresence,
       "scmVendor": scmVendor,
       "scmMfgDate": scmMfgDate,
       "scmDeviceName": scmDeviceName,
       "scmPart": scmPart,
       "scmSerialNo": scmSerialNo,
       "scmMaximumPower": scmMaximumPower,
       "scmNominalPower": scmNominalPower,
       "scmAssetTag": scmAssetTag,
       "scmManagementMac": scmManagementMac,
       "scmWWN": scmWWN,
       "scmSCSIProtocol": scmSCSIProtocol,
       "scmPowerLed": scmPowerLed,
       "scmFaultLed": scmFaultLed,
       "scmFirmwareVersion": scmFirmwareVersion,
       "scmOpStatus": scmOpStatus,
       "scmRole": scmRole,
       "scmReadinessStatus": scmReadinessStatus,
       "scmNumOfPoolsPresent": scmNumOfPoolsPresent,
       "scmNumOfPhysicalDrivesPresent": scmNumOfPhysicalDrivesPresent,
       "scmNumOfPhysicalDrivesOnline": scmNumOfPhysicalDrivesOnline,
       "scmNumOfPhysicalDrivesOffline": scmNumOfPhysicalDrivesOffline,
       "scmNumOfPhysicalDrivesWithPFA": scmNumOfPhysicalDrivesWithPFA,
       "scmNumOfPhysicalDrivesRebuilding": scmNumOfPhysicalDrivesRebuilding,
       "scmNumOfPhysicalDrivesMissing": scmNumOfPhysicalDrivesMissing,
       "scmNumOfPhysicalDrivesUnconfigured": scmNumOfPhysicalDrivesUnconfigured,
       "scmNumOfVirtualDrivesPresent": scmNumOfVirtualDrivesPresent,
       "scmNumOfVirtualDrivesOnline": scmNumOfVirtualDrivesOnline,
       "scmNumOfVirtualDrivesOffline": scmNumOfVirtualDrivesOffline,
       "scmNumOfVirtualDrivesCritical": scmNumOfVirtualDrivesCritical,
       "scmNumOfGlobalSparesPresent": scmNumOfGlobalSparesPresent,
       "scmNumOfDedicatedSparesPresent": scmNumOfDedicatedSparesPresent,
       "scmNumOfRevertibleGlobalSparesPresent": scmNumOfRevertibleGlobalSparesPresent,
       "scmNumOfRevertibleGlobalSparesUsed": scmNumOfRevertibleGlobalSparesUsed,
       "scmNumOfRevertibleDedicatedSparesPresent": scmNumOfRevertibleDedicatedSparesPresent,
       "scmNumOfRevertibleDedicatedSparesUsed": scmNumOfRevertibleDedicatedSparesUsed,
       "scmNumOfBGAs": scmNumOfBGAs,
       "scmPowerOnHours": scmPowerOnHours,
       "scmDirtyCachePercentage": scmDirtyCachePercentage,
       "scmCacheUsagePercentage": scmCacheUsagePercentage,
       "scmStatsTable": scmStatsTable,
       "scmStatsEntry": scmStatsEntry,
       "scmStatsDataTransferred": scmStatsDataTransferred,
       "scmStatsReadDataTransferred": scmStatsReadDataTransferred,
       "scmStatsWriteDataTransferred": scmStatsWriteDataTransferred,
       "scmStatsNumOfErrors": scmStatsNumOfErrors,
       "scmStatsNumOfNonRWErrors": scmStatsNumOfNonRWErrors,
       "scmStatsNumOfReadErrors": scmStatsNumOfReadErrors,
       "scmStatsNumOfWriteErrors": scmStatsNumOfWriteErrors,
       "scmStatsNumOfIORequests": scmStatsNumOfIORequests,
       "scmStatsNumOfNonRWRequests": scmStatsNumOfNonRWRequests,
       "scmStatsNumOfReadRequests": scmStatsNumOfReadRequests,
       "scmStatsNumOfWriteRequests": scmStatsNumOfWriteRequests,
       "scmStatsStartTime": scmStatsStartTime,
       "scmStatsCollectionTime": scmStatsCollectionTime,
       "scmBatteryTable": scmBatteryTable,
       "scmBatteryEntry": scmBatteryEntry,
       "scmBatteryPresence": scmBatteryPresence,
       "scmBatteryVendor": scmBatteryVendor,
       "scmBatteryMfgDate": scmBatteryMfgDate,
       "scmBatteryDeviceName": scmBatteryDeviceName,
       "scmBatteryPart": scmBatteryPart,
       "scmBatterySerialNo": scmBatterySerialNo,
       "scmBatteryMaximumPower": scmBatteryMaximumPower,
       "scmBatteryNominalPower": scmBatteryNominalPower,
       "scmBatteryAssetTag": scmBatteryAssetTag,
       "scmBatteryDeviceChemistry": scmBatteryDeviceChemistry,
       "scmBatteryTemperature": scmBatteryTemperature,
       "scmBatteryTempChargeThreshold": scmBatteryTempChargeThreshold,
       "scmBatteryTempDisChargeThreshold": scmBatteryTempDisChargeThreshold,
       "scmBatteryCycleCount": scmBatteryCycleCount,
       "scmBatteryRemainCapacity": scmBatteryRemainCapacity,
       "scmBatteryVoltage": scmBatteryVoltage,
       "scmBatteryCurrent": scmBatteryCurrent,
       "scmBatteryStatus": scmBatteryStatus,
       "scmBatteryCellType": scmBatteryCellType,
       "scmBatteryHoldTime": scmBatteryHoldTime}
)
