# SNMP MIB module (HPNSATRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSATRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:28 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaECC_ObjectIdentity = ObjectIdentity
hpnsaECC = _HpnsaECC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6)
)
_HpnsaRemoteAssist_ObjectIdentity = ObjectIdentity
hpnsaRemoteAssist = _HpnsaRemoteAssist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8)
)
_Hpnr_ObjectIdentity = ObjectIdentity
hpnr = _Hpnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16)
)
_HpNetRAID_ObjectIdentity = ObjectIdentity
hpNetRAID = _HpNetRAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1)
)
_HpNetRaidMib_ObjectIdentity = ObjectIdentity
hpNetRaidMib = _HpNetRaidMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1, 1)
)
_RaidTraps_ObjectIdentity = ObjectIdentity
raidTraps = _RaidTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200)
)
_RtAdapterNumber_Type = Integer32
_RtAdapterNumber_Object = MibScalar
rtAdapterNumber = _RtAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1001),
    _RtAdapterNumber_Type()
)
rtAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtAdapterNumber.setStatus("mandatory")
_RtLogicalDriveNumber_Type = Integer32
_RtLogicalDriveNumber_Object = MibScalar
rtLogicalDriveNumber = _RtLogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1002),
    _RtLogicalDriveNumber_Type()
)
rtLogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtLogicalDriveNumber.setStatus("mandatory")
_RtChannelNumber_Type = Integer32
_RtChannelNumber_Object = MibScalar
rtChannelNumber = _RtChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1003),
    _RtChannelNumber_Type()
)
rtChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtChannelNumber.setStatus("mandatory")
_RtTargetID_Type = Integer32
_RtTargetID_Object = MibScalar
rtTargetID = _RtTargetID_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1004),
    _RtTargetID_Type()
)
rtTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtTargetID.setStatus("mandatory")
_RtOldDriveState_Type = DisplayString
_RtOldDriveState_Object = MibScalar
rtOldDriveState = _RtOldDriveState_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1005),
    _RtOldDriveState_Type()
)
rtOldDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtOldDriveState.setStatus("mandatory")
_RtNewDriveState_Type = DisplayString
_RtNewDriveState_Object = MibScalar
rtNewDriveState = _RtNewDriveState_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1006),
    _RtNewDriveState_Type()
)
rtNewDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtNewDriveState.setStatus("mandatory")
_RtSenseKey_Type = Integer32
_RtSenseKey_Object = MibScalar
rtSenseKey = _RtSenseKey_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1007),
    _RtSenseKey_Type()
)
rtSenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtSenseKey.setStatus("mandatory")
_RtASC_Type = Integer32
_RtASC_Object = MibScalar
rtASC = _RtASC_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1008),
    _RtASC_Type()
)
rtASC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtASC.setStatus("mandatory")
_RtASCQ_Type = Integer32
_RtASCQ_Object = MibScalar
rtASCQ = _RtASCQ_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1009),
    _RtASCQ_Type()
)
rtASCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtASCQ.setStatus("mandatory")
_RtDriveVendor_Type = DisplayString
_RtDriveVendor_Object = MibScalar
rtDriveVendor = _RtDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 1010),
    _RtDriveVendor_Type()
)
rtDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtDriveVendor.setStatus("mandatory")
_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Storagemanagement_ObjectIdentity = ObjectIdentity
storagemanagement = _Storagemanagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2)
)
_Cyclone_ObjectIdentity = ObjectIdentity
cyclone = _Cyclone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 5)
)
_CycTraps_ObjectIdentity = ObjectIdentity
cycTraps = _CycTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000)
)


class _CycManagerID_Type(DisplayString):
    """Custom type cycManagerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycManagerID_Type.__name__ = "DisplayString"
_CycManagerID_Object = MibScalar
cycManagerID = _CycManagerID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9001),
    _CycManagerID_Type()
)
cycManagerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycManagerID.setStatus("mandatory")


class _CycHostAdapterID_Type(DisplayString):
    """Custom type cycHostAdapterID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycHostAdapterID_Type.__name__ = "DisplayString"
_CycHostAdapterID_Object = MibScalar
cycHostAdapterID = _CycHostAdapterID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9002),
    _CycHostAdapterID_Type()
)
cycHostAdapterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycHostAdapterID.setStatus("mandatory")
_CycHostAdapterNumber_Type = Integer32
_CycHostAdapterNumber_Object = MibScalar
cycHostAdapterNumber = _CycHostAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9003),
    _CycHostAdapterNumber_Type()
)
cycHostAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycHostAdapterNumber.setStatus("mandatory")


class _CycVendor_Type(DisplayString):
    """Custom type cycVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CycVendor_Type.__name__ = "DisplayString"
_CycVendor_Object = MibScalar
cycVendor = _CycVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9004),
    _CycVendor_Type()
)
cycVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycVendor.setStatus("mandatory")


class _CycProduct_Type(DisplayString):
    """Custom type cycProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycProduct_Type.__name__ = "DisplayString"
_CycProduct_Object = MibScalar
cycProduct = _CycProduct_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9005),
    _CycProduct_Type()
)
cycProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycProduct.setStatus("mandatory")


class _CycControllerModel_Type(DisplayString):
    """Custom type cycControllerModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycControllerModel_Type.__name__ = "DisplayString"
_CycControllerModel_Object = MibScalar
cycControllerModel = _CycControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9006),
    _CycControllerModel_Type()
)
cycControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycControllerModel.setStatus("mandatory")
_CycBusNumber_Type = Integer32
_CycBusNumber_Object = MibScalar
cycBusNumber = _CycBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9007),
    _CycBusNumber_Type()
)
cycBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycBusNumber.setStatus("mandatory")
_CycChannelNumber_Type = Integer32
_CycChannelNumber_Object = MibScalar
cycChannelNumber = _CycChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9008),
    _CycChannelNumber_Type()
)
cycChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycChannelNumber.setStatus("mandatory")
_CycScsiTargetID_Type = Integer32
_CycScsiTargetID_Object = MibScalar
cycScsiTargetID = _CycScsiTargetID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9009),
    _CycScsiTargetID_Type()
)
cycScsiTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycScsiTargetID.setStatus("mandatory")
_CycLun_Type = Integer32
_CycLun_Object = MibScalar
cycLun = _CycLun_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9010),
    _CycLun_Type()
)
cycLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycLun.setStatus("mandatory")


class _CycArrayName_Type(DisplayString):
    """Custom type cycArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycArrayName_Type.__name__ = "DisplayString"
_CycArrayName_Object = MibScalar
cycArrayName = _CycArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9011),
    _CycArrayName_Type()
)
cycArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycArrayName.setStatus("mandatory")
_CycMisCompares_Type = Integer32
_CycMisCompares_Object = MibScalar
cycMisCompares = _CycMisCompares_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9012),
    _CycMisCompares_Type()
)
cycMisCompares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycMisCompares.setStatus("mandatory")
_CycDriver_Type = Integer32
_CycDriver_Object = MibScalar
cycDriver = _CycDriver_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9013),
    _CycDriver_Type()
)
cycDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycDriver.setStatus("mandatory")
_CycManager_Type = Integer32
_CycManager_Object = MibScalar
cycManager = _CycManager_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9014),
    _CycManager_Type()
)
cycManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycManager.setStatus("mandatory")


class _CycOldArrayName_Type(DisplayString):
    """Custom type cycOldArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycOldArrayName_Type.__name__ = "DisplayString"
_CycOldArrayName_Object = MibScalar
cycOldArrayName = _CycOldArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9015),
    _CycOldArrayName_Type()
)
cycOldArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycOldArrayName.setStatus("mandatory")


class _CycNewArrayName_Type(DisplayString):
    """Custom type cycNewArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycNewArrayName_Type.__name__ = "DisplayString"
_CycNewArrayName_Object = MibScalar
cycNewArrayName = _CycNewArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9016),
    _CycNewArrayName_Type()
)
cycNewArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycNewArrayName.setStatus("mandatory")
_CycPriority_Type = Integer32
_CycPriority_Object = MibScalar
cycPriority = _CycPriority_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9017),
    _CycPriority_Type()
)
cycPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycPriority.setStatus("mandatory")
_CycSenseInfo_Type = Integer32
_CycSenseInfo_Object = MibScalar
cycSenseInfo = _CycSenseInfo_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9018),
    _CycSenseInfo_Type()
)
cycSenseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycSenseInfo.setStatus("mandatory")
_AdaptecNm_ObjectIdentity = ObjectIdentity
adaptecNm = _AdaptecNm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 4)
)
_AdaptecNmScsiStatus_ObjectIdentity = ObjectIdentity
adaptecNmScsiStatus = _AdaptecNmScsiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 4, 1)
)

# Managed Objects groups


# Notification objects

hpnsaStorageCapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 4096)
)
if mibBuilder.loadTexts:
    hpnsaStorageCapWarning.setStatus(
        ""
    )

hpnsaStorageCapMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 4097)
)
if mibBuilder.loadTexts:
    hpnsaStorageCapMinor.setStatus(
        ""
    )

hpnsaStorageCapMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 4098)
)
if mibBuilder.loadTexts:
    hpnsaStorageCapMajor.setStatus(
        ""
    )

hpnsaPostError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 4356)
)
if mibBuilder.loadTexts:
    hpnsaPostError.setStatus(
        ""
    )

hpnsaDiskSysDefects = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8210)
)
if mibBuilder.loadTexts:
    hpnsaDiskSysDefects.setStatus(
        ""
    )

hpnsaDaCacheError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8609)
)
if mibBuilder.loadTexts:
    hpnsaDaCacheError.setStatus(
        ""
    )

hpnsaDaLogicalDriveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8625)
)
if mibBuilder.loadTexts:
    hpnsaDaLogicalDriveTrap.setStatus(
        ""
    )

hpnsaDaLogicalDriveNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8626)
)
if mibBuilder.loadTexts:
    hpnsaDaLogicalDriveNotAvailable.setStatus(
        ""
    )

hpnsaDaHotSpareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8641)
)
if mibBuilder.loadTexts:
    hpnsaDaHotSpareFailure.setStatus(
        ""
    )

hpnsaDaHotSpareSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8642)
)
if mibBuilder.loadTexts:
    hpnsaDaHotSpareSuccess.setStatus(
        ""
    )

hpnsaDaHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8657)
)
if mibBuilder.loadTexts:
    hpnsaDaHardDiskFailure.setStatus(
        ""
    )

hpnsaDaParityThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8673)
)
if mibBuilder.loadTexts:
    hpnsaDaParityThresholdTrap.setStatus(
        ""
    )

hpnsaDaSoftErrorThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8674)
)
if mibBuilder.loadTexts:
    hpnsaDaSoftErrorThresholdTrap.setStatus(
        ""
    )

hpnsaDaHardwareThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8675)
)
if mibBuilder.loadTexts:
    hpnsaDaHardwareThresholdTrap.setStatus(
        ""
    )

hpnsaDaMiscThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8676)
)
if mibBuilder.loadTexts:
    hpnsaDaMiscThresholdTrap.setStatus(
        ""
    )

hpnsaDaControllerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 8677)
)
if mibBuilder.loadTexts:
    hpnsaDaControllerTrap.setStatus(
        ""
    )

hpnsaRPSAbnormalCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9101)
)
if mibBuilder.loadTexts:
    hpnsaRPSAbnormalCondition.setStatus(
        ""
    )

hpnsaRPSACPowerSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9103)
)
if mibBuilder.loadTexts:
    hpnsaRPSACPowerSourceFailure.setStatus(
        ""
    )

hpnsaRPSPsuFailureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9105)
)
if mibBuilder.loadTexts:
    hpnsaRPSPsuFailureDetected.setStatus(
        ""
    )

hpnsaRPSDCShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9106)
)
if mibBuilder.loadTexts:
    hpnsaRPSDCShutdown.setStatus(
        ""
    )

hpnsaRPSPsuRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9107)
)
if mibBuilder.loadTexts:
    hpnsaRPSPsuRemoved.setStatus(
        ""
    )

hpnsaRPSPsuInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9108)
)
if mibBuilder.loadTexts:
    hpnsaRPSPsuInserted.setStatus(
        ""
    )

hpnsaRPSPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9109)
)
if mibBuilder.loadTexts:
    hpnsaRPSPowerRestored.setStatus(
        ""
    )

hpnsaRPSWarningExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9110)
)
if mibBuilder.loadTexts:
    hpnsaRPSWarningExceeded.setStatus(
        ""
    )

hpnsaRPSEmergencyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 9111)
)
if mibBuilder.loadTexts:
    hpnsaRPSEmergencyExceeded.setStatus(
        ""
    )

hpnsaTempMonitorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 12288)
)
if mibBuilder.loadTexts:
    hpnsaTempMonitorError.setStatus(
        ""
    )

hpnsaTempTrapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 12289)
)
if mibBuilder.loadTexts:
    hpnsaTempTrapWarning.setStatus(
        ""
    )

hpnsaTempTrapEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 12290)
)
if mibBuilder.loadTexts:
    hpnsaTempTrapEmergency.setStatus(
        ""
    )

hpnsaNicReceiveErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16385)
)
if mibBuilder.loadTexts:
    hpnsaNicReceiveErrors.setStatus(
        ""
    )

hpnsaNicTransmitErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16386)
)
if mibBuilder.loadTexts:
    hpnsaNicTransmitErrors.setStatus(
        ""
    )

hpnsaNicAdapterReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16387)
)
if mibBuilder.loadTexts:
    hpnsaNicAdapterReset.setStatus(
        ""
    )

hpnsaNicAlignmentErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16388)
)
if mibBuilder.loadTexts:
    hpnsaNicAlignmentErrors.setStatus(
        ""
    )

hpnsaNicGiantFrameErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16389)
)
if mibBuilder.loadTexts:
    hpnsaNicGiantFrameErrors.setStatus(
        ""
    )

hpnsaNicHardwareMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16390)
)
if mibBuilder.loadTexts:
    hpnsaNicHardwareMismatch.setStatus(
        ""
    )

hpnsaNicLateCollision = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16391)
)
if mibBuilder.loadTexts:
    hpnsaNicLateCollision.setStatus(
        ""
    )

hpnsaNicExcessiveCollision = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16392)
)
if mibBuilder.loadTexts:
    hpnsaNicExcessiveCollision.setStatus(
        ""
    )

hpnsaNicCarrierSenseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16393)
)
if mibBuilder.loadTexts:
    hpnsaNicCarrierSenseError.setStatus(
        ""
    )

hpnsaNicDeferralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16394)
)
if mibBuilder.loadTexts:
    hpnsaNicDeferralError.setStatus(
        ""
    )

hpnsaNicNoECBError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16395)
)
if mibBuilder.loadTexts:
    hpnsaNicNoECBError.setStatus(
        ""
    )

hpnsaNicReceiveOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16396)
)
if mibBuilder.loadTexts:
    hpnsaNicReceiveOverflow.setStatus(
        ""
    )

hpnsaNicUtilCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16397)
)
if mibBuilder.loadTexts:
    hpnsaNicUtilCount.setStatus(
        ""
    )

hpnsaNicAdapterMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16398)
)
if mibBuilder.loadTexts:
    hpnsaNicAdapterMismatch.setStatus(
        ""
    )

hpnsaNicTxFIFOUnderrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16399)
)
if mibBuilder.loadTexts:
    hpnsaNicTxFIFOUnderrun.setStatus(
        ""
    )

hpnsaNicTxTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16400)
)
if mibBuilder.loadTexts:
    hpnsaNicTxTimeOut.setStatus(
        ""
    )

hpnsaNicRxFIFOOverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16401)
)
if mibBuilder.loadTexts:
    hpnsaNicRxFIFOOverrun.setStatus(
        ""
    )

hpnsaNicRxFalseInterrupts = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16402)
)
if mibBuilder.loadTexts:
    hpnsaNicRxFalseInterrupts.setStatus(
        ""
    )

hpnsaNicPagingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16403)
)
if mibBuilder.loadTexts:
    hpnsaNicPagingError.setStatus(
        ""
    )

hpnsaNicTimedOutDMA = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16404)
)
if mibBuilder.loadTexts:
    hpnsaNicTimedOutDMA.setStatus(
        ""
    )

hpnsaNicTxNoResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16405)
)
if mibBuilder.loadTexts:
    hpnsaNicTxNoResources.setStatus(
        ""
    )

hpnsaNicTxExcessiveFrags = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16406)
)
if mibBuilder.loadTexts:
    hpnsaNicTxExcessiveFrags.setStatus(
        ""
    )

hpnsaNicRxLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16407)
)
if mibBuilder.loadTexts:
    hpnsaNicRxLow.setStatus(
        ""
    )

hpnsaNicRxEmpty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 16408)
)
if mibBuilder.loadTexts:
    hpnsaNicRxEmpty.setStatus(
        ""
    )

hpnsaParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20528)
)
if mibBuilder.loadTexts:
    hpnsaParityError.setStatus(
        ""
    )

hpnsaBusTimeoutError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20544)
)
if mibBuilder.loadTexts:
    hpnsaBusTimeoutError.setStatus(
        ""
    )

hpnsaIOChannelCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20560)
)
if mibBuilder.loadTexts:
    hpnsaIOChannelCheck.setStatus(
        ""
    )

hpnsaSoftwareNMI = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20576)
)
if mibBuilder.loadTexts:
    hpnsaSoftwareNMI.setStatus(
        ""
    )

hpnsaPostMemoryResize = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20592)
)
if mibBuilder.loadTexts:
    hpnsaPostMemoryResize.setStatus(
        ""
    )

hpnsaPciParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20624)
)
if mibBuilder.loadTexts:
    hpnsaPciParityError.setStatus(
        ""
    )

hpnsaPciSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20640)
)
if mibBuilder.loadTexts:
    hpnsaPciSystemError.setStatus(
        ""
    )

hpnsaCPUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20656)
)
if mibBuilder.loadTexts:
    hpnsaCPUFailure.setStatus(
        ""
    )

hpnsaFailsafeTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20672)
)
if mibBuilder.loadTexts:
    hpnsaFailsafeTimeout.setStatus(
        ""
    )

hpnsaErrorLoggingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20704)
)
if mibBuilder.loadTexts:
    hpnsaErrorLoggingDisabled.setStatus(
        ""
    )

hpnsaSystemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20736)
)
if mibBuilder.loadTexts:
    hpnsaSystemWarning.setStatus(
        ""
    )

hpnsaSystemCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20737)
)
if mibBuilder.loadTexts:
    hpnsaSystemCritical.setStatus(
        ""
    )

hpnsaVoltEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20738)
)
if mibBuilder.loadTexts:
    hpnsaVoltEmergency.setStatus(
        ""
    )

hpnsaVoltWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20739)
)
if mibBuilder.loadTexts:
    hpnsaVoltWarning.setStatus(
        ""
    )

hpnsaASRServerRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20752)
)
if mibBuilder.loadTexts:
    hpnsaASRServerRestart.setStatus(
        ""
    )

hpnsaSystemReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 20800)
)
if mibBuilder.loadTexts:
    hpnsaSystemReconfig.setStatus(
        ""
    )

hpnsaHotSwapTempMonitorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24449)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapTempMonitorError.setStatus(
        ""
    )

hpnsaHotSwapTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24451)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapTempWarning.setStatus(
        ""
    )

hpnsaHotSwapTempEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24452)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapTempEmergency.setStatus(
        ""
    )

hpnsaHotSwapPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24453)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapPowerFailure.setStatus(
        ""
    )

hpnsaHotSwapDeviceRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24454)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapDeviceRemoved.setStatus(
        ""
    )

hpnsaHotSwapDeviceInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 0, 24455)
)
if mibBuilder.loadTexts:
    hpnsaHotSwapDeviceInserted.setStatus(
        ""
    )

hpnsaEccErrorCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4353)
)
if mibBuilder.loadTexts:
    hpnsaEccErrorCorrected.setStatus(
        ""
    )

hpnsaEccSBEOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4354)
)
if mibBuilder.loadTexts:
    hpnsaEccSBEOverflow.setStatus(
        ""
    )

hpnsaEccMemoryResize = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4355)
)
if mibBuilder.loadTexts:
    hpnsaEccMemoryResize.setStatus(
        ""
    )

hpnsaEccMultiBitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4357)
)
if mibBuilder.loadTexts:
    hpnsaEccMultiBitError.setStatus(
        ""
    )

hpnsaEccMultiBitErrorOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 6, 0, 4358)
)
if mibBuilder.loadTexts:
    hpnsaEccMultiBitErrorOverflow.setStatus(
        ""
    )

hpnsaRAVoltServerPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 109)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltServerPowerFailure.setStatus(
        ""
    )

hpnsaRAVoltMinus12VUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 111)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltMinus12VUpper.setStatus(
        ""
    )

hpnsaRAVoltPlus3VUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 113)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus3VUpper.setStatus(
        ""
    )

hpnsaRAVoltPlus5VUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 114)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus5VUpper.setStatus(
        ""
    )

hpnsaRAVoltPlus12VUpper = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 115)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus12VUpper.setStatus(
        ""
    )

hpnsaRAVoltMinus12VLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 121)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltMinus12VLower.setStatus(
        ""
    )

hpnsaRAVoltBatteryLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 122)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltBatteryLower.setStatus(
        ""
    )

hpnsaRAVoltPlus3VLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 123)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus3VLower.setStatus(
        ""
    )

hpnsaRAVoltPlus5VLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 124)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus5VLower.setStatus(
        ""
    )

hpnsaRAVoltPlus12VLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 125)
)
if mibBuilder.loadTexts:
    hpnsaRAVoltPlus12VLower.setStatus(
        ""
    )

hpnsaRATempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 211)
)
if mibBuilder.loadTexts:
    hpnsaRATempWarning.setStatus(
        ""
    )

hpnsaRATempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 221)
)
if mibBuilder.loadTexts:
    hpnsaRATempShutdown.setStatus(
        ""
    )

hpnsaRATempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 231)
)
if mibBuilder.loadTexts:
    hpnsaRATempCritical.setStatus(
        ""
    )

hpnsaRASuccessfulLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 401)
)
if mibBuilder.loadTexts:
    hpnsaRASuccessfulLogin.setStatus(
        ""
    )

hpnsaRAIllegalLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 402)
)
if mibBuilder.loadTexts:
    hpnsaRAIllegalLogin.setStatus(
        ""
    )

hpnsaRALowBatteryCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 403)
)
if mibBuilder.loadTexts:
    hpnsaRALowBatteryCharge.setStatus(
        ""
    )

hpnsaRABoardShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 404)
)
if mibBuilder.loadTexts:
    hpnsaRABoardShutDown.setStatus(
        ""
    )

hpnsaRAAdminstratorLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 405)
)
if mibBuilder.loadTexts:
    hpnsaRAAdminstratorLogout.setStatus(
        ""
    )

hpnsaRAAdministratorAutologout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 406)
)
if mibBuilder.loadTexts:
    hpnsaRAAdministratorAutologout.setStatus(
        ""
    )

hpnsaRAAdministratorConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 407)
)
if mibBuilder.loadTexts:
    hpnsaRAAdministratorConnectionLost.setStatus(
        ""
    )

hpnsaRAAdministratorDialbackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 408)
)
if mibBuilder.loadTexts:
    hpnsaRAAdministratorDialbackFailed.setStatus(
        ""
    )

hpnsaRAASRHangNOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 501)
)
if mibBuilder.loadTexts:
    hpnsaRAASRHangNOS.setStatus(
        ""
    )

hpnsaRAASRServerRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 502)
)
if mibBuilder.loadTexts:
    hpnsaRAASRServerRestart.setStatus(
        ""
    )

hpnsaRAASRTimerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 503)
)
if mibBuilder.loadTexts:
    hpnsaRAASRTimerEnabled.setStatus(
        ""
    )

hpnsaRAASRTimerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 504)
)
if mibBuilder.loadTexts:
    hpnsaRAASRTimerDisabled.setStatus(
        ""
    )

hpnsaRARemoteInitiatedCtrlAltDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 601)
)
if mibBuilder.loadTexts:
    hpnsaRARemoteInitiatedCtrlAltDel.setStatus(
        ""
    )

hpnsaRARemoteInitiatedReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 602)
)
if mibBuilder.loadTexts:
    hpnsaRARemoteInitiatedReset.setStatus(
        ""
    )

hpnsaRARemoteInitiatedPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 603)
)
if mibBuilder.loadTexts:
    hpnsaRARemoteInitiatedPowerDown.setStatus(
        ""
    )

hpnsaRAInitServerBIOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 701)
)
if mibBuilder.loadTexts:
    hpnsaRAInitServerBIOS.setStatus(
        ""
    )

hpnsaRABusUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 800)
)
if mibBuilder.loadTexts:
    hpnsaRABusUtilization.setStatus(
        ""
    )

hpnsaRATestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 900)
)
if mibBuilder.loadTexts:
    hpnsaRATestNotification.setStatus(
        ""
    )

hpnsaRATAPNoConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 901)
)
if mibBuilder.loadTexts:
    hpnsaRATAPNoConnect.setStatus(
        ""
    )

hpnsaRATAPParam1Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 902)
)
if mibBuilder.loadTexts:
    hpnsaRATAPParam1Error.setStatus(
        ""
    )

hpnsaRATAPParam2Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 903)
)
if mibBuilder.loadTexts:
    hpnsaRATAPParam2Error.setStatus(
        ""
    )

hpnsaRATAPParam3Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 8, 0, 904)
)
if mibBuilder.loadTexts:
    hpnsaRATAPParam3Error.setStatus(
        ""
    )

rtConfigUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9001)
)
rtConfigUpdated.setObjects(
    ("HPNSATRAP-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtConfigUpdated.setStatus(
        ""
    )

rtPhysicalDriveStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9002)
)
rtPhysicalDriveStateChange.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtChannelNumber"),
        ("HPNSATRAP-MIB", "rtTargetID"),
        ("HPNSATRAP-MIB", "rtOldDriveState"),
        ("HPNSATRAP-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateChange.setStatus(
        ""
    )

rtLogicalDriveStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9003)
)
rtLogicalDriveStateChange.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"),
        ("HPNSATRAP-MIB", "rtOldDriveState"),
        ("HPNSATRAP-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateChange.setStatus(
        ""
    )

rtInitializeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9004)
)
rtInitializeStarted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeStarted.setStatus(
        ""
    )

rtInitializeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9005)
)
rtInitializeCompleted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeCompleted.setStatus(
        ""
    )

rtInitializeAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9006)
)
rtInitializeAborted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeAborted.setStatus(
        ""
    )

rtInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9007)
)
rtInitializeFailed.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeFailed.setStatus(
        ""
    )

rtCheckConsistencyStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9008)
)
rtCheckConsistencyStarted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyStarted.setStatus(
        ""
    )

rtCheckConsistencyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9009)
)
rtCheckConsistencyCompleted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyCompleted.setStatus(
        ""
    )

rtCheckConsistencyAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9010)
)
rtCheckConsistencyAborted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyAborted.setStatus(
        ""
    )

rtConsistencyCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9011)
)
rtConsistencyCorrected.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtConsistencyCorrected.setStatus(
        ""
    )

rtCheckConsistencyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9012)
)
rtCheckConsistencyFailed.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyFailed.setStatus(
        ""
    )

rtReconstructionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9013)
)
rtReconstructionStarted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionStarted.setStatus(
        ""
    )

rtReconstructionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9014)
)
rtReconstructionCompleted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionCompleted.setStatus(
        ""
    )

rtReconstructionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9015)
)
rtReconstructionFailed.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionFailed.setStatus(
        ""
    )

rtPredictiveFailuresFalse = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9016)
)
rtPredictiveFailuresFalse.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtChannelNumber"),
        ("HPNSATRAP-MIB", "rtTargetID"),
        ("HPNSATRAP-MIB", "rtDriveVendor"),
        ("HPNSATRAP-MIB", "rtSenseKey"),
        ("HPNSATRAP-MIB", "rtASC"),
        ("HPNSATRAP-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtPredictiveFailuresFalse.setStatus(
        ""
    )

rtPredictiveFailuresExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9017)
)
rtPredictiveFailuresExceeded.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtChannelNumber"),
        ("HPNSATRAP-MIB", "rtTargetID"),
        ("HPNSATRAP-MIB", "rtDriveVendor"),
        ("HPNSATRAP-MIB", "rtSenseKey"),
        ("HPNSATRAP-MIB", "rtASC"),
        ("HPNSATRAP-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtPredictiveFailuresExceeded.setStatus(
        ""
    )

rtCheckConditionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9018)
)
rtCheckConditionStatus.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtChannelNumber"),
        ("HPNSATRAP-MIB", "rtTargetID"),
        ("HPNSATRAP-MIB", "rtSenseKey"),
        ("HPNSATRAP-MIB", "rtASC"),
        ("HPNSATRAP-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtCheckConditionStatus.setStatus(
        ""
    )

rtNewDriveInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9019)
)
rtNewDriveInserted.setObjects(
      *(("HPNSATRAP-MIB", "rtAdapterNumber"),
        ("HPNSATRAP-MIB", "rtChannelNumber"),
        ("HPNSATRAP-MIB", "rtTargetID"))
)
if mibBuilder.loadTexts:
    rtNewDriveInserted.setStatus(
        ""
    )

rtBatteryMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9020)
)
rtBatteryMissing.setObjects(
    ("HPNSATRAP-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryMissing.setStatus(
        ""
    )

rtBatteryVolatageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9021)
)
rtBatteryVolatageLow.setObjects(
    ("HPNSATRAP-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryVolatageLow.setStatus(
        ""
    )

rtBatteryTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16, 1, 1, 200, 0, 9022)
)
rtBatteryTemperatureHigh.setObjects(
    ("HPNSATRAP-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryTemperatureHigh.setStatus(
        ""
    )

cycSNMPAgentIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 101)
)
if mibBuilder.loadTexts:
    cycSNMPAgentIsUp.setStatus(
        ""
    )

cycSNMPAgentIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 102)
)
if mibBuilder.loadTexts:
    cycSNMPAgentIsDown.setStatus(
        ""
    )

cycDuplicateHostAdapter = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 107)
)
if mibBuilder.loadTexts:
    cycDuplicateHostAdapter.setStatus(
        ""
    )

cycHostAdapterDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 108)
)
cycHostAdapterDiscovered.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycHostAdapterID"),
        ("HPNSATRAP-MIB", "cycManagerID"))
)
if mibBuilder.loadTexts:
    cycHostAdapterDiscovered.setStatus(
        ""
    )

cycHostAdapterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 109)
)
cycHostAdapterChanged.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycHostAdapterID"),
        ("HPNSATRAP-MIB", "cycManagerID"))
)
if mibBuilder.loadTexts:
    cycHostAdapterChanged.setStatus(
        ""
    )

cycHostAdapterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 110)
)
cycHostAdapterFailed.setObjects(
    ("HPNSATRAP-MIB", "cycHostAdapterNumber")
)
if mibBuilder.loadTexts:
    cycHostAdapterFailed.setStatus(
        ""
    )

cycHostAdapterRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 111)
)
cycHostAdapterRecovered.setObjects(
    ("HPNSATRAP-MIB", "cycHostAdapterNumber")
)
if mibBuilder.loadTexts:
    cycHostAdapterRecovered.setStatus(
        ""
    )

cycDeviceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 112)
)
cycDeviceFailed.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycScsiTargetID"),
        ("HPNSATRAP-MIB", "cycLun"))
)
if mibBuilder.loadTexts:
    cycDeviceFailed.setStatus(
        ""
    )

cycDeviceDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 113)
)
cycDeviceDiscovered.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycScsiTargetID"),
        ("HPNSATRAP-MIB", "cycLun"),
        ("HPNSATRAP-MIB", "cycVendor"),
        ("HPNSATRAP-MIB", "cycProduct"))
)
if mibBuilder.loadTexts:
    cycDeviceDiscovered.setStatus(
        ""
    )

cycDeviceRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 114)
)
cycDeviceRecovered.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycScsiTargetID"),
        ("HPNSATRAP-MIB", "cycLun"))
)
if mibBuilder.loadTexts:
    cycDeviceRecovered.setStatus(
        ""
    )

cycDeviceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 115)
)
cycDeviceChanged.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycScsiTargetID"),
        ("HPNSATRAP-MIB", "cycLun"),
        ("HPNSATRAP-MIB", "cycVendor"),
        ("HPNSATRAP-MIB", "cycProduct"))
)
if mibBuilder.loadTexts:
    cycDeviceChanged.setStatus(
        ""
    )

cycPredictiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 116)
)
cycPredictiveFailure.setObjects(
      *(("HPNSATRAP-MIB", "cycHostAdapterNumber"),
        ("HPNSATRAP-MIB", "cycScsiTargetID"),
        ("HPNSATRAP-MIB", "cycLun"),
        ("HPNSATRAP-MIB", "cycVendor"),
        ("HPNSATRAP-MIB", "cycProduct"),
        ("HPNSATRAP-MIB", "cycSenseInfo"))
)
if mibBuilder.loadTexts:
    cycPredictiveFailure.setStatus(
        ""
    )

cycAspiDatabaseCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 117)
)
if mibBuilder.loadTexts:
    cycAspiDatabaseCleared.setStatus(
        ""
    )

cycAspiCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 118)
)
if mibBuilder.loadTexts:
    cycAspiCrash.setStatus(
        ""
    )

cycAspiNoMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 119)
)
if mibBuilder.loadTexts:
    cycAspiNoMemory.setStatus(
        ""
    )

cycAspiFileWriteOpenError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 120)
)
if mibBuilder.loadTexts:
    cycAspiFileWriteOpenError.setStatus(
        ""
    )

cycAspiFileWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 121)
)
if mibBuilder.loadTexts:
    cycAspiFileWriteError.setStatus(
        ""
    )

cycAspiNoDeviceFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 122)
)
if mibBuilder.loadTexts:
    cycAspiNoDeviceFile.setStatus(
        ""
    )

cycAspiNoMemoryReading = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 123)
)
if mibBuilder.loadTexts:
    cycAspiNoMemoryReading.setStatus(
        ""
    )

cycAspiFileReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 124)
)
if mibBuilder.loadTexts:
    cycAspiFileReadError.setStatus(
        ""
    )

cycAspiBadFileMagic = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 125)
)
if mibBuilder.loadTexts:
    cycAspiBadFileMagic.setStatus(
        ""
    )

hpnsaScsiStatusCorruptedDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8193)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusCorruptedDB.setStatus(
        ""
    )

hpnsaScsiStatusUnloadedNLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8194)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusUnloadedNLM.setStatus(
        ""
    )

hpnsaScsiStatusFailedHBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8196)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusFailedHBA.setStatus(
        ""
    )

hpnsaScsiStatusRecoveredHBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8197)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusRecoveredHBA.setStatus(
        ""
    )

hpnsaScsiStatusDiscoveredHBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8198)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDiscoveredHBA.setStatus(
        ""
    )

hpnsaScsiStatusDeviceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8199)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDeviceFailed.setStatus(
        ""
    )

hpnsaScsiStatusDeviceRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8200)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDeviceRecovered.setStatus(
        ""
    )

hpnsaScsiStatusDeviceDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8201)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDeviceDiscovered.setStatus(
        ""
    )

hpnsaScsiStatusChangedHBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8205)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusChangedHBA.setStatus(
        ""
    )

hpnsaScsiStatusDeviceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8206)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDeviceChanged.setStatus(
        ""
    )

hpnsaScsiStatusTimeoutHBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8208)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusTimeoutHBA.setStatus(
        ""
    )

hpnsaScsiStatusDeviceTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 4, 1, 0, 8209)
)
if mibBuilder.loadTexts:
    hpnsaScsiStatusDeviceTimeout.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSATRAP-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaStorageCapWarning": hpnsaStorageCapWarning,
       "hpnsaStorageCapMinor": hpnsaStorageCapMinor,
       "hpnsaStorageCapMajor": hpnsaStorageCapMajor,
       "hpnsaPostError": hpnsaPostError,
       "hpnsaDiskSysDefects": hpnsaDiskSysDefects,
       "hpnsaDaCacheError": hpnsaDaCacheError,
       "hpnsaDaLogicalDriveTrap": hpnsaDaLogicalDriveTrap,
       "hpnsaDaLogicalDriveNotAvailable": hpnsaDaLogicalDriveNotAvailable,
       "hpnsaDaHotSpareFailure": hpnsaDaHotSpareFailure,
       "hpnsaDaHotSpareSuccess": hpnsaDaHotSpareSuccess,
       "hpnsaDaHardDiskFailure": hpnsaDaHardDiskFailure,
       "hpnsaDaParityThresholdTrap": hpnsaDaParityThresholdTrap,
       "hpnsaDaSoftErrorThresholdTrap": hpnsaDaSoftErrorThresholdTrap,
       "hpnsaDaHardwareThresholdTrap": hpnsaDaHardwareThresholdTrap,
       "hpnsaDaMiscThresholdTrap": hpnsaDaMiscThresholdTrap,
       "hpnsaDaControllerTrap": hpnsaDaControllerTrap,
       "hpnsaRPSAbnormalCondition": hpnsaRPSAbnormalCondition,
       "hpnsaRPSACPowerSourceFailure": hpnsaRPSACPowerSourceFailure,
       "hpnsaRPSPsuFailureDetected": hpnsaRPSPsuFailureDetected,
       "hpnsaRPSDCShutdown": hpnsaRPSDCShutdown,
       "hpnsaRPSPsuRemoved": hpnsaRPSPsuRemoved,
       "hpnsaRPSPsuInserted": hpnsaRPSPsuInserted,
       "hpnsaRPSPowerRestored": hpnsaRPSPowerRestored,
       "hpnsaRPSWarningExceeded": hpnsaRPSWarningExceeded,
       "hpnsaRPSEmergencyExceeded": hpnsaRPSEmergencyExceeded,
       "hpnsaTempMonitorError": hpnsaTempMonitorError,
       "hpnsaTempTrapWarning": hpnsaTempTrapWarning,
       "hpnsaTempTrapEmergency": hpnsaTempTrapEmergency,
       "hpnsaNicReceiveErrors": hpnsaNicReceiveErrors,
       "hpnsaNicTransmitErrors": hpnsaNicTransmitErrors,
       "hpnsaNicAdapterReset": hpnsaNicAdapterReset,
       "hpnsaNicAlignmentErrors": hpnsaNicAlignmentErrors,
       "hpnsaNicGiantFrameErrors": hpnsaNicGiantFrameErrors,
       "hpnsaNicHardwareMismatch": hpnsaNicHardwareMismatch,
       "hpnsaNicLateCollision": hpnsaNicLateCollision,
       "hpnsaNicExcessiveCollision": hpnsaNicExcessiveCollision,
       "hpnsaNicCarrierSenseError": hpnsaNicCarrierSenseError,
       "hpnsaNicDeferralError": hpnsaNicDeferralError,
       "hpnsaNicNoECBError": hpnsaNicNoECBError,
       "hpnsaNicReceiveOverflow": hpnsaNicReceiveOverflow,
       "hpnsaNicUtilCount": hpnsaNicUtilCount,
       "hpnsaNicAdapterMismatch": hpnsaNicAdapterMismatch,
       "hpnsaNicTxFIFOUnderrun": hpnsaNicTxFIFOUnderrun,
       "hpnsaNicTxTimeOut": hpnsaNicTxTimeOut,
       "hpnsaNicRxFIFOOverrun": hpnsaNicRxFIFOOverrun,
       "hpnsaNicRxFalseInterrupts": hpnsaNicRxFalseInterrupts,
       "hpnsaNicPagingError": hpnsaNicPagingError,
       "hpnsaNicTimedOutDMA": hpnsaNicTimedOutDMA,
       "hpnsaNicTxNoResources": hpnsaNicTxNoResources,
       "hpnsaNicTxExcessiveFrags": hpnsaNicTxExcessiveFrags,
       "hpnsaNicRxLow": hpnsaNicRxLow,
       "hpnsaNicRxEmpty": hpnsaNicRxEmpty,
       "hpnsaParityError": hpnsaParityError,
       "hpnsaBusTimeoutError": hpnsaBusTimeoutError,
       "hpnsaIOChannelCheck": hpnsaIOChannelCheck,
       "hpnsaSoftwareNMI": hpnsaSoftwareNMI,
       "hpnsaPostMemoryResize": hpnsaPostMemoryResize,
       "hpnsaPciParityError": hpnsaPciParityError,
       "hpnsaPciSystemError": hpnsaPciSystemError,
       "hpnsaCPUFailure": hpnsaCPUFailure,
       "hpnsaFailsafeTimeout": hpnsaFailsafeTimeout,
       "hpnsaErrorLoggingDisabled": hpnsaErrorLoggingDisabled,
       "hpnsaSystemWarning": hpnsaSystemWarning,
       "hpnsaSystemCritical": hpnsaSystemCritical,
       "hpnsaVoltEmergency": hpnsaVoltEmergency,
       "hpnsaVoltWarning": hpnsaVoltWarning,
       "hpnsaASRServerRestart": hpnsaASRServerRestart,
       "hpnsaSystemReconfig": hpnsaSystemReconfig,
       "hpnsaHotSwapTempMonitorError": hpnsaHotSwapTempMonitorError,
       "hpnsaHotSwapTempWarning": hpnsaHotSwapTempWarning,
       "hpnsaHotSwapTempEmergency": hpnsaHotSwapTempEmergency,
       "hpnsaHotSwapPowerFailure": hpnsaHotSwapPowerFailure,
       "hpnsaHotSwapDeviceRemoved": hpnsaHotSwapDeviceRemoved,
       "hpnsaHotSwapDeviceInserted": hpnsaHotSwapDeviceInserted,
       "hpnsaECC": hpnsaECC,
       "hpnsaEccErrorCorrected": hpnsaEccErrorCorrected,
       "hpnsaEccSBEOverflow": hpnsaEccSBEOverflow,
       "hpnsaEccMemoryResize": hpnsaEccMemoryResize,
       "hpnsaEccMultiBitError": hpnsaEccMultiBitError,
       "hpnsaEccMultiBitErrorOverflow": hpnsaEccMultiBitErrorOverflow,
       "hpnsaRemoteAssist": hpnsaRemoteAssist,
       "hpnsaRAVoltServerPowerFailure": hpnsaRAVoltServerPowerFailure,
       "hpnsaRAVoltMinus12VUpper": hpnsaRAVoltMinus12VUpper,
       "hpnsaRAVoltPlus3VUpper": hpnsaRAVoltPlus3VUpper,
       "hpnsaRAVoltPlus5VUpper": hpnsaRAVoltPlus5VUpper,
       "hpnsaRAVoltPlus12VUpper": hpnsaRAVoltPlus12VUpper,
       "hpnsaRAVoltMinus12VLower": hpnsaRAVoltMinus12VLower,
       "hpnsaRAVoltBatteryLower": hpnsaRAVoltBatteryLower,
       "hpnsaRAVoltPlus3VLower": hpnsaRAVoltPlus3VLower,
       "hpnsaRAVoltPlus5VLower": hpnsaRAVoltPlus5VLower,
       "hpnsaRAVoltPlus12VLower": hpnsaRAVoltPlus12VLower,
       "hpnsaRATempWarning": hpnsaRATempWarning,
       "hpnsaRATempShutdown": hpnsaRATempShutdown,
       "hpnsaRATempCritical": hpnsaRATempCritical,
       "hpnsaRASuccessfulLogin": hpnsaRASuccessfulLogin,
       "hpnsaRAIllegalLogin": hpnsaRAIllegalLogin,
       "hpnsaRALowBatteryCharge": hpnsaRALowBatteryCharge,
       "hpnsaRABoardShutDown": hpnsaRABoardShutDown,
       "hpnsaRAAdminstratorLogout": hpnsaRAAdminstratorLogout,
       "hpnsaRAAdministratorAutologout": hpnsaRAAdministratorAutologout,
       "hpnsaRAAdministratorConnectionLost": hpnsaRAAdministratorConnectionLost,
       "hpnsaRAAdministratorDialbackFailed": hpnsaRAAdministratorDialbackFailed,
       "hpnsaRAASRHangNOS": hpnsaRAASRHangNOS,
       "hpnsaRAASRServerRestart": hpnsaRAASRServerRestart,
       "hpnsaRAASRTimerEnabled": hpnsaRAASRTimerEnabled,
       "hpnsaRAASRTimerDisabled": hpnsaRAASRTimerDisabled,
       "hpnsaRARemoteInitiatedCtrlAltDel": hpnsaRARemoteInitiatedCtrlAltDel,
       "hpnsaRARemoteInitiatedReset": hpnsaRARemoteInitiatedReset,
       "hpnsaRARemoteInitiatedPowerDown": hpnsaRARemoteInitiatedPowerDown,
       "hpnsaRAInitServerBIOS": hpnsaRAInitServerBIOS,
       "hpnsaRABusUtilization": hpnsaRABusUtilization,
       "hpnsaRATestNotification": hpnsaRATestNotification,
       "hpnsaRATAPNoConnect": hpnsaRATAPNoConnect,
       "hpnsaRATAPParam1Error": hpnsaRATAPParam1Error,
       "hpnsaRATAPParam2Error": hpnsaRATAPParam2Error,
       "hpnsaRATAPParam3Error": hpnsaRATAPParam3Error,
       "hpnr": hpnr,
       "hpNetRAID": hpNetRAID,
       "hpNetRaidMib": hpNetRaidMib,
       "raidTraps": raidTraps,
       "rtConfigUpdated": rtConfigUpdated,
       "rtPhysicalDriveStateChange": rtPhysicalDriveStateChange,
       "rtLogicalDriveStateChange": rtLogicalDriveStateChange,
       "rtInitializeStarted": rtInitializeStarted,
       "rtInitializeCompleted": rtInitializeCompleted,
       "rtInitializeAborted": rtInitializeAborted,
       "rtInitializeFailed": rtInitializeFailed,
       "rtCheckConsistencyStarted": rtCheckConsistencyStarted,
       "rtCheckConsistencyCompleted": rtCheckConsistencyCompleted,
       "rtCheckConsistencyAborted": rtCheckConsistencyAborted,
       "rtConsistencyCorrected": rtConsistencyCorrected,
       "rtCheckConsistencyFailed": rtCheckConsistencyFailed,
       "rtReconstructionStarted": rtReconstructionStarted,
       "rtReconstructionCompleted": rtReconstructionCompleted,
       "rtReconstructionFailed": rtReconstructionFailed,
       "rtPredictiveFailuresFalse": rtPredictiveFailuresFalse,
       "rtPredictiveFailuresExceeded": rtPredictiveFailuresExceeded,
       "rtCheckConditionStatus": rtCheckConditionStatus,
       "rtNewDriveInserted": rtNewDriveInserted,
       "rtBatteryMissing": rtBatteryMissing,
       "rtBatteryVolatageLow": rtBatteryVolatageLow,
       "rtBatteryTemperatureHigh": rtBatteryTemperatureHigh,
       "rtAdapterNumber": rtAdapterNumber,
       "rtLogicalDriveNumber": rtLogicalDriveNumber,
       "rtChannelNumber": rtChannelNumber,
       "rtTargetID": rtTargetID,
       "rtOldDriveState": rtOldDriveState,
       "rtNewDriveState": rtNewDriveState,
       "rtSenseKey": rtSenseKey,
       "rtASC": rtASC,
       "rtASCQ": rtASCQ,
       "rtDriveVendor": rtDriveVendor,
       "adaptec": adaptec,
       "storagemanagement": storagemanagement,
       "cyclone": cyclone,
       "cycSNMPAgentIsUp": cycSNMPAgentIsUp,
       "cycSNMPAgentIsDown": cycSNMPAgentIsDown,
       "cycDuplicateHostAdapter": cycDuplicateHostAdapter,
       "cycHostAdapterDiscovered": cycHostAdapterDiscovered,
       "cycHostAdapterChanged": cycHostAdapterChanged,
       "cycHostAdapterFailed": cycHostAdapterFailed,
       "cycHostAdapterRecovered": cycHostAdapterRecovered,
       "cycDeviceFailed": cycDeviceFailed,
       "cycDeviceDiscovered": cycDeviceDiscovered,
       "cycDeviceRecovered": cycDeviceRecovered,
       "cycDeviceChanged": cycDeviceChanged,
       "cycPredictiveFailure": cycPredictiveFailure,
       "cycAspiDatabaseCleared": cycAspiDatabaseCleared,
       "cycAspiCrash": cycAspiCrash,
       "cycAspiNoMemory": cycAspiNoMemory,
       "cycAspiFileWriteOpenError": cycAspiFileWriteOpenError,
       "cycAspiFileWriteError": cycAspiFileWriteError,
       "cycAspiNoDeviceFile": cycAspiNoDeviceFile,
       "cycAspiNoMemoryReading": cycAspiNoMemoryReading,
       "cycAspiFileReadError": cycAspiFileReadError,
       "cycAspiBadFileMagic": cycAspiBadFileMagic,
       "cycTraps": cycTraps,
       "cycManagerID": cycManagerID,
       "cycHostAdapterID": cycHostAdapterID,
       "cycHostAdapterNumber": cycHostAdapterNumber,
       "cycVendor": cycVendor,
       "cycProduct": cycProduct,
       "cycControllerModel": cycControllerModel,
       "cycBusNumber": cycBusNumber,
       "cycChannelNumber": cycChannelNumber,
       "cycScsiTargetID": cycScsiTargetID,
       "cycLun": cycLun,
       "cycArrayName": cycArrayName,
       "cycMisCompares": cycMisCompares,
       "cycDriver": cycDriver,
       "cycManager": cycManager,
       "cycOldArrayName": cycOldArrayName,
       "cycNewArrayName": cycNewArrayName,
       "cycPriority": cycPriority,
       "cycSenseInfo": cycSenseInfo,
       "adaptecNm": adaptecNm,
       "adaptecNmScsiStatus": adaptecNmScsiStatus,
       "hpnsaScsiStatusCorruptedDB": hpnsaScsiStatusCorruptedDB,
       "hpnsaScsiStatusUnloadedNLM": hpnsaScsiStatusUnloadedNLM,
       "hpnsaScsiStatusFailedHBA": hpnsaScsiStatusFailedHBA,
       "hpnsaScsiStatusRecoveredHBA": hpnsaScsiStatusRecoveredHBA,
       "hpnsaScsiStatusDiscoveredHBA": hpnsaScsiStatusDiscoveredHBA,
       "hpnsaScsiStatusDeviceFailed": hpnsaScsiStatusDeviceFailed,
       "hpnsaScsiStatusDeviceRecovered": hpnsaScsiStatusDeviceRecovered,
       "hpnsaScsiStatusDeviceDiscovered": hpnsaScsiStatusDeviceDiscovered,
       "hpnsaScsiStatusChangedHBA": hpnsaScsiStatusChangedHBA,
       "hpnsaScsiStatusDeviceChanged": hpnsaScsiStatusDeviceChanged,
       "hpnsaScsiStatusTimeoutHBA": hpnsaScsiStatusTimeoutHBA,
       "hpnsaScsiStatusDeviceTimeout": hpnsaScsiStatusDeviceTimeout}
)
