# SNMP MIB module (INTELCORPORATIONICMBGENERICCHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATIONICMBGENERICCHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:18 2024
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




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
_Server_products_ObjectIdentity = ObjectIdentity
server_products = _Server_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6)
)
_Platforms_ObjectIdentity = ObjectIdentity
platforms = _Platforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2)
)
_IcmbChassis_ObjectIdentity = ObjectIdentity
icmbChassis = _IcmbChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TIcmbState_Object = MibTable
tIcmbState = _TIcmbState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12)
)
if mibBuilder.loadTexts:
    tIcmbState.setStatus("mandatory")
_EIcmbState_Object = MibTableRow
eIcmbState = _EIcmbState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1)
)
eIcmbState.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eIcmbState.setStatus("mandatory")


class _A12ChassisAvailable_Type(Integer32):
    """Custom type a12ChassisAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vAvailable", 0),
          ("vGoingNonaccessible", 6),
          ("vInitializing", 3),
          ("vNonaccessible", 5),
          ("vShuttingDown", 1),
          ("vUnavailable", 2),
          ("vUnknown", 4))
    )


_A12ChassisAvailable_Type.__name__ = "Integer32"
_A12ChassisAvailable_Object = MibTableColumn
a12ChassisAvailable = _A12ChassisAvailable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 1),
    _A12ChassisAvailable_Type()
)
a12ChassisAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12ChassisAvailable.setStatus("mandatory")
_A12IcmbId_Type = DmiInteger
_A12IcmbId_Object = MibTableColumn
a12IcmbId = _A12IcmbId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 2),
    _A12IcmbId_Type()
)
a12IcmbId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12IcmbId.setStatus("mandatory")
_A12SdrDeviceId_Type = DmiInteger
_A12SdrDeviceId_Object = MibTableColumn
a12SdrDeviceId = _A12SdrDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 3),
    _A12SdrDeviceId_Type()
)
a12SdrDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SdrDeviceId.setStatus("mandatory")
_A12SelDeviceId_Type = DmiInteger
_A12SelDeviceId_Object = MibTableColumn
a12SelDeviceId = _A12SelDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 4),
    _A12SelDeviceId_Type()
)
a12SelDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SelDeviceId.setStatus("mandatory")
_A12SmDeviceId_Type = DmiInteger
_A12SmDeviceId_Object = MibTableColumn
a12SmDeviceId = _A12SmDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 5),
    _A12SmDeviceId_Type()
)
a12SmDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SmDeviceId.setStatus("mandatory")


class _A12SdrReadState_Type(Integer32):
    """Custom type a12SdrReadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A12SdrReadState_Type.__name__ = "Integer32"
_A12SdrReadState_Object = MibTableColumn
a12SdrReadState = _A12SdrReadState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 6),
    _A12SdrReadState_Type()
)
a12SdrReadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12SdrReadState.setStatus("mandatory")
_A12EventPollingPeriod_Type = DmiInteger
_A12EventPollingPeriod_Object = MibTableColumn
a12EventPollingPeriod = _A12EventPollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 7),
    _A12EventPollingPeriod_Type()
)
a12EventPollingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12EventPollingPeriod.setStatus("mandatory")
_A12EventCount_Type = DmiInteger
_A12EventCount_Object = MibTableColumn
a12EventCount = _A12EventCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 8),
    _A12EventCount_Type()
)
a12EventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventCount.setStatus("mandatory")


class _A12ManageChassis_Type(Integer32):
    """Custom type a12ManageChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A12ManageChassis_Type.__name__ = "Integer32"
_A12ManageChassis_Object = MibTableColumn
a12ManageChassis = _A12ManageChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 9),
    _A12ManageChassis_Type()
)
a12ManageChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12ManageChassis.setStatus("mandatory")
_A12SetAvailablityState_Type = DmiInteger
_A12SetAvailablityState_Object = MibTableColumn
a12SetAvailablityState = _A12SetAvailablityState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 10),
    _A12SetAvailablityState_Type()
)
a12SetAvailablityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12SetAvailablityState.setStatus("mandatory")
_A12UniqueId_Type = DmiOctetstring
_A12UniqueId_Object = MibTableColumn
a12UniqueId = _A12UniqueId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 11),
    _A12UniqueId_Type()
)
a12UniqueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12UniqueId.setStatus("mandatory")


class _A12PreviousAvailabilityStatus_Type(Integer32):
    """Custom type a12PreviousAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vAvailable", 0),
          ("vInitializing", 3),
          ("vShuttingDown", 1),
          ("vUnavailable", 2))
    )


_A12PreviousAvailabilityStatus_Type.__name__ = "Integer32"
_A12PreviousAvailabilityStatus_Object = MibTableColumn
a12PreviousAvailabilityStatus = _A12PreviousAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 12, 1, 12),
    _A12PreviousAvailabilityStatus_Type()
)
a12PreviousAvailabilityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12PreviousAvailabilityStatus.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1)
)
eOperationalState.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a31OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A31OperationalStateInstanceIndex_Type = DmiInteger
_A31OperationalStateInstanceIndex_Object = MibTableColumn
a31OperationalStateInstanceIndex = _A31OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 1),
    _A31OperationalStateInstanceIndex_Type()
)
a31OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31OperationalStateInstanceIndex.setStatus("mandatory")
_A31DeviceGroupIndex_Type = DmiInteger
_A31DeviceGroupIndex_Object = MibTableColumn
a31DeviceGroupIndex = _A31DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 2),
    _A31DeviceGroupIndex_Type()
)
a31DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31DeviceGroupIndex.setStatus("mandatory")


class _A31OperationalStatus_Type(Integer32):
    """Custom type a31OperationalStatus based on Integer32"""
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
        *(("vDisabled", 4),
          ("vEnabled", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31OperationalStatus_Type.__name__ = "Integer32"
_A31OperationalStatus_Object = MibTableColumn
a31OperationalStatus = _A31OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 3),
    _A31OperationalStatus_Type()
)
a31OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31OperationalStatus.setStatus("mandatory")


class _A31UsageState_Type(Integer32):
    """Custom type a31UsageState based on Integer32"""
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
        *(("vActive", 4),
          ("vBusy", 5),
          ("vIdle", 3),
          ("vNotApplicable", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31UsageState_Type.__name__ = "Integer32"
_A31UsageState_Object = MibTableColumn
a31UsageState = _A31UsageState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 4),
    _A31UsageState_Type()
)
a31UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31UsageState.setStatus("mandatory")


class _A31AvailabilityStatus_Type(Integer32):
    """Custom type a31AvailabilityStatus based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("vDegraded", 10),
          ("vInTest", 5),
          ("vInstallError", 12),
          ("vNotApplicable", 6),
          ("vNotInstalled", 11),
          ("vOffDuty", 9),
          ("vOffLine", 8),
          ("vOther", 1),
          ("vPowerOff", 7),
          ("vPowerSave", 13),
          ("vRunning", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A31AvailabilityStatus_Type.__name__ = "Integer32"
_A31AvailabilityStatus_Object = MibTableColumn
a31AvailabilityStatus = _A31AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 5),
    _A31AvailabilityStatus_Type()
)
a31AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31AvailabilityStatus.setStatus("mandatory")


class _A31AdministrativeState_Type(Integer32):
    """Custom type a31AdministrativeState based on Integer32"""
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
        *(("vLocked", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vShuttingDown", 6),
          ("vUnknown", 2),
          ("vUnlocked", 4))
    )


_A31AdministrativeState_Type.__name__ = "Integer32"
_A31AdministrativeState_Object = MibTableColumn
a31AdministrativeState = _A31AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 6),
    _A31AdministrativeState_Type()
)
a31AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31AdministrativeState.setStatus("mandatory")
_A31FatalErrorCount_Type = DmiCounter
_A31FatalErrorCount_Object = MibTableColumn
a31FatalErrorCount = _A31FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 7),
    _A31FatalErrorCount_Type()
)
a31FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31FatalErrorCount.setStatus("mandatory")
_A31MajorErrorCount_Type = DmiCounter
_A31MajorErrorCount_Object = MibTableColumn
a31MajorErrorCount = _A31MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 8),
    _A31MajorErrorCount_Type()
)
a31MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31MajorErrorCount.setStatus("mandatory")
_A31WarningErrorCount_Type = DmiCounter
_A31WarningErrorCount_Object = MibTableColumn
a31WarningErrorCount = _A31WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 9),
    _A31WarningErrorCount_Type()
)
a31WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31WarningErrorCount.setStatus("mandatory")


class _A31CurrentErrorStatus_Type(Integer32):
    """Custom type a31CurrentErrorStatus based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31CurrentErrorStatus_Type.__name__ = "Integer32"
_A31CurrentErrorStatus_Object = MibTableColumn
a31CurrentErrorStatus = _A31CurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 31, 1, 10),
    _A31CurrentErrorStatus_Type()
)
a31CurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31CurrentErrorStatus.setStatus("mandatory")
_TFieldReplaceableUnit_Object = MibTable
tFieldReplaceableUnit = _TFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93)
)
if mibBuilder.loadTexts:
    tFieldReplaceableUnit.setStatus("mandatory")
_EFieldReplaceableUnit_Object = MibTableRow
eFieldReplaceableUnit = _EFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1)
)
eFieldReplaceableUnit.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a93FruIndex"),
)
if mibBuilder.loadTexts:
    eFieldReplaceableUnit.setStatus("mandatory")
_A93FruIndex_Type = DmiInteger
_A93FruIndex_Object = MibTableColumn
a93FruIndex = _A93FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 1),
    _A93FruIndex_Type()
)
a93FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93FruIndex.setStatus("mandatory")
_A93DeviceGroupIndex_Type = DmiInteger
_A93DeviceGroupIndex_Object = MibTableColumn
a93DeviceGroupIndex = _A93DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 2),
    _A93DeviceGroupIndex_Type()
)
a93DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93DeviceGroupIndex.setStatus("mandatory")
_A93Description_Type = DmiDisplaystring
_A93Description_Object = MibTableColumn
a93Description = _A93Description_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 3),
    _A93Description_Type()
)
a93Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93Description.setStatus("mandatory")
_A93Manufacturer_Type = DmiDisplaystring
_A93Manufacturer_Object = MibTableColumn
a93Manufacturer = _A93Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 4),
    _A93Manufacturer_Type()
)
a93Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93Manufacturer.setStatus("mandatory")
_A93Model_Type = DmiDisplaystring
_A93Model_Object = MibTableColumn
a93Model = _A93Model_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 5),
    _A93Model_Type()
)
a93Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93Model.setStatus("mandatory")
_A93PartNumber_Type = DmiDisplaystring
_A93PartNumber_Object = MibTableColumn
a93PartNumber = _A93PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 6),
    _A93PartNumber_Type()
)
a93PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93PartNumber.setStatus("mandatory")
_A93FruSerialNumber_Type = DmiDisplaystring
_A93FruSerialNumber_Object = MibTableColumn
a93FruSerialNumber = _A93FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 7),
    _A93FruSerialNumber_Type()
)
a93FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93FruSerialNumber.setStatus("mandatory")
_A93RevisionLevel_Type = DmiDisplaystring
_A93RevisionLevel_Object = MibTableColumn
a93RevisionLevel = _A93RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 8),
    _A93RevisionLevel_Type()
)
a93RevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93RevisionLevel.setStatus("mandatory")
_A93WarrantyStartDate_Type = DmiDateX
_A93WarrantyStartDate_Object = MibTableColumn
a93WarrantyStartDate = _A93WarrantyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 9),
    _A93WarrantyStartDate_Type()
)
a93WarrantyStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93WarrantyStartDate.setStatus("mandatory")
_A93WarrantyDuration_Type = DmiInteger
_A93WarrantyDuration_Object = MibTableColumn
a93WarrantyDuration = _A93WarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 10),
    _A93WarrantyDuration_Type()
)
a93WarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93WarrantyDuration.setStatus("mandatory")
_A93SupportPhoneNumber_Type = DmiDisplaystring
_A93SupportPhoneNumber_Object = MibTableColumn
a93SupportPhoneNumber = _A93SupportPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 11),
    _A93SupportPhoneNumber_Type()
)
a93SupportPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93SupportPhoneNumber.setStatus("mandatory")
_A93FruInternetUniformResourceLocator_Type = DmiDisplaystring
_A93FruInternetUniformResourceLocator_Object = MibTableColumn
a93FruInternetUniformResourceLocator = _A93FruInternetUniformResourceLocator_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 93, 1, 12),
    _A93FruInternetUniformResourceLocator_Type()
)
a93FruInternetUniformResourceLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a93FruInternetUniformResourceLocator.setStatus("mandatory")
_TEventGenerationForPhysicalContainer_Object = MibTable
tEventGenerationForPhysicalContainer = _TEventGenerationForPhysicalContainer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116)
)
if mibBuilder.loadTexts:
    tEventGenerationForPhysicalContainer.setStatus("mandatory")
_EEventGenerationForPhysicalContainer_Object = MibTableRow
eEventGenerationForPhysicalContainer = _EEventGenerationForPhysicalContainer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1)
)
eEventGenerationForPhysicalContainer.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPhysicalContainer.setStatus("mandatory")


class _A116EventType_Type(Integer32):
    """Custom type a116EventType based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("vConfigurationError", 7),
          ("vContainerSecurityBreach", 6),
          ("vContainerSecurityStatusOk", 256),
          ("vCoolingDeviceStatusChange", 3),
          ("vLogicalDeviceStatusChange", 5),
          ("vPhysicalDeviceStatusChange", 4),
          ("vPowerSupplyStatusChange", 2),
          ("vSecuritySettingsChange", 1))
    )


_A116EventType_Type.__name__ = "Integer32"
_A116EventType_Object = MibTableColumn
a116EventType = _A116EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 1),
    _A116EventType_Type()
)
a116EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventType.setStatus("mandatory")


class _A116EventSeverity_Type(Integer32):
    """Custom type a116EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical1", 8),
          ("vNon-recoverable1", 32),
          ("vOk", 4))
    )


_A116EventSeverity_Type.__name__ = "Integer32"
_A116EventSeverity_Object = MibTableColumn
a116EventSeverity = _A116EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 2),
    _A116EventSeverity_Type()
)
a116EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSeverity.setStatus("mandatory")


class _A116IsEventState_based_Type(Integer32):
    """Custom type a116IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A116IsEventState_based_Type.__name__ = "Integer32"
_A116IsEventState_based_Object = MibScalar
a116IsEventState_based = _A116IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 3),
    _A116IsEventState_based_Type()
)
a116IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116IsEventState_based.setStatus("mandatory")
_A116EventStateKey_Type = DmiInteger
_A116EventStateKey_Object = MibTableColumn
a116EventStateKey = _A116EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 4),
    _A116EventStateKey_Type()
)
a116EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventStateKey.setStatus("mandatory")
_A116AssociatedGroup_Type = DmiDisplaystring
_A116AssociatedGroup_Object = MibTableColumn
a116AssociatedGroup = _A116AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 5),
    _A116AssociatedGroup_Type()
)
a116AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116AssociatedGroup.setStatus("mandatory")


class _A116EventSystem_Type(Integer32):
    """Custom type a116EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A116EventSystem_Type.__name__ = "Integer32"
_A116EventSystem_Object = MibTableColumn
a116EventSystem = _A116EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 6),
    _A116EventSystem_Type()
)
a116EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSystem.setStatus("mandatory")


class _A116EventSubsystem_Type(Integer32):
    """Custom type a116EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A116EventSubsystem_Type.__name__ = "Integer32"
_A116EventSubsystem_Object = MibTableColumn
a116EventSubsystem = _A116EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 7),
    _A116EventSubsystem_Type()
)
a116EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSubsystem.setStatus("mandatory")
_TPhysicalContainerGlobalTable_Object = MibTable
tPhysicalContainerGlobalTable = _TPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127)
)
if mibBuilder.loadTexts:
    tPhysicalContainerGlobalTable.setStatus("mandatory")
_EPhysicalContainerGlobalTable_Object = MibTableRow
ePhysicalContainerGlobalTable = _EPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1)
)
ePhysicalContainerGlobalTable.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a127ContainerIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalContainerGlobalTable.setStatus("mandatory")


class _A127ContainerOrChassisType_Type(Integer32):
    """Custom type a127ContainerOrChassisType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("vAllInOne", 13),
          ("vBusExpansionChassis", 20),
          ("vDesktop", 3),
          ("vDockingStation", 12),
          ("vExpansionChassis", 18),
          ("vHandHeld", 11),
          ("vLaptop", 9),
          ("vLowProfileDesktop", 4),
          ("vLunchBox", 16),
          ("vMainSystemChassis", 17),
          ("vMiniTower", 6),
          ("vNotebook", 10),
          ("vOther", 1),
          ("vPeripheralChassis", 21),
          ("vPizzaBox", 5),
          ("vPortable", 8),
          ("vRackMountChassis", 23),
          ("vRaidChassis", 22),
          ("vSpace-saving", 15),
          ("vSubNotebook", 14),
          ("vSubchassis", 19),
          ("vTower", 7),
          ("vUnknown", 2))
    )


_A127ContainerOrChassisType_Type.__name__ = "Integer32"
_A127ContainerOrChassisType_Object = MibTableColumn
a127ContainerOrChassisType = _A127ContainerOrChassisType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 1),
    _A127ContainerOrChassisType_Type()
)
a127ContainerOrChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127ContainerOrChassisType.setStatus("mandatory")
_A127AssetTag_Type = DmiDisplaystring
_A127AssetTag_Object = MibTableColumn
a127AssetTag = _A127AssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 2),
    _A127AssetTag_Type()
)
a127AssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a127AssetTag.setStatus("mandatory")


class _A127ChassisLockPresent_Type(Integer32):
    """Custom type a127ChassisLockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A127ChassisLockPresent_Type.__name__ = "Integer32"
_A127ChassisLockPresent_Object = MibTableColumn
a127ChassisLockPresent = _A127ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 3),
    _A127ChassisLockPresent_Type()
)
a127ChassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127ChassisLockPresent.setStatus("mandatory")


class _A127BootupState_Type(Integer32):
    """Custom type a127BootupState based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A127BootupState_Type.__name__ = "Integer32"
_A127BootupState_Object = MibTableColumn
a127BootupState = _A127BootupState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 4),
    _A127BootupState_Type()
)
a127BootupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127BootupState.setStatus("mandatory")


class _A127PowerState_Type(Integer32):
    """Custom type a127PowerState based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A127PowerState_Type.__name__ = "Integer32"
_A127PowerState_Object = MibTableColumn
a127PowerState = _A127PowerState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 5),
    _A127PowerState_Type()
)
a127PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127PowerState.setStatus("mandatory")


class _A127ThermalState_Type(Integer32):
    """Custom type a127ThermalState based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A127ThermalState_Type.__name__ = "Integer32"
_A127ThermalState_Object = MibTableColumn
a127ThermalState = _A127ThermalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 6),
    _A127ThermalState_Type()
)
a127ThermalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127ThermalState.setStatus("mandatory")
_A127FruGroupIndex_Type = DmiInteger
_A127FruGroupIndex_Object = MibTableColumn
a127FruGroupIndex = _A127FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 7),
    _A127FruGroupIndex_Type()
)
a127FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127FruGroupIndex.setStatus("mandatory")
_A127OperationalGroupIndex_Type = DmiInteger
_A127OperationalGroupIndex_Object = MibTableColumn
a127OperationalGroupIndex = _A127OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 8),
    _A127OperationalGroupIndex_Type()
)
a127OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127OperationalGroupIndex.setStatus("mandatory")
_A127ContainerIndex_Type = DmiInteger
_A127ContainerIndex_Object = MibTableColumn
a127ContainerIndex = _A127ContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 9),
    _A127ContainerIndex_Type()
)
a127ContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127ContainerIndex.setStatus("mandatory")
_A127ContainerName_Type = DmiDisplaystring
_A127ContainerName_Object = MibTableColumn
a127ContainerName = _A127ContainerName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 10),
    _A127ContainerName_Type()
)
a127ContainerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a127ContainerName.setStatus("mandatory")
_A127ContainerLocation_Type = DmiDisplaystring
_A127ContainerLocation_Object = MibTableColumn
a127ContainerLocation = _A127ContainerLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 11),
    _A127ContainerLocation_Type()
)
a127ContainerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a127ContainerLocation.setStatus("mandatory")


class _A127ContainerSecurityStatus_Type(Integer32):
    """Custom type a127ContainerSecurityStatus based on Integer32"""
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
        *(("vContainerSecurityBreachAttempted", 4),
          ("vContainerSecurityBreached", 5),
          ("vNoSecurityBreachDetected", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A127ContainerSecurityStatus_Type.__name__ = "Integer32"
_A127ContainerSecurityStatus_Object = MibTableColumn
a127ContainerSecurityStatus = _A127ContainerSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 127, 1, 12),
    _A127ContainerSecurityStatus_Type()
)
a127ContainerSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a127ContainerSecurityStatus.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1001)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1001, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A1001MibName_Type = DmiDisplaystring
_A1001MibName_Object = MibTableColumn
a1001MibName = _A1001MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1001, 1, 1),
    _A1001MibName_Type()
)
a1001MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibName.setStatus("mandatory")
_A1001MibOid_Type = DmiDisplaystring
_A1001MibOid_Object = MibTableColumn
a1001MibOid = _A1001MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1001, 1, 2),
    _A1001MibOid_Type()
)
a1001MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibOid.setStatus("mandatory")
_A1001DisableTrap_Type = DmiInteger
_A1001DisableTrap_Object = MibTableColumn
a1001DisableTrap = _A1001DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1001, 1, 3),
    _A1001DisableTrap_Type()
)
a1001DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1001DisableTrap.setStatus("mandatory")
_TSystemControl_Object = MibTable
tSystemControl = _TSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004)
)
if mibBuilder.loadTexts:
    tSystemControl.setStatus("mandatory")
_ESystemControl_Object = MibTableRow
eSystemControl = _ESystemControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1)
)
eSystemControl.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1004Selfid"),
)
if mibBuilder.loadTexts:
    eSystemControl.setStatus("mandatory")
_A1004Selfid_Type = DmiInteger
_A1004Selfid_Object = MibTableColumn
a1004Selfid = _A1004Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 1),
    _A1004Selfid_Type()
)
a1004Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004Selfid.setStatus("mandatory")


class _A1004ResetSystem_Type(Integer32):
    """Custom type a1004ResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotReset", 0),
          ("vInitiateReset", 1))
    )


_A1004ResetSystem_Type.__name__ = "Integer32"
_A1004ResetSystem_Object = MibTableColumn
a1004ResetSystem = _A1004ResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 2),
    _A1004ResetSystem_Type()
)
a1004ResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ResetSystem.setStatus("mandatory")
_A1004TimedResetIncrement_Type = DmiInteger
_A1004TimedResetIncrement_Object = MibTableColumn
a1004TimedResetIncrement = _A1004TimedResetIncrement_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 3),
    _A1004TimedResetIncrement_Type()
)
a1004TimedResetIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004TimedResetIncrement.setStatus("mandatory")
_A1004TimedResetResolution_Type = DmiInteger
_A1004TimedResetResolution_Object = MibTableColumn
a1004TimedResetResolution = _A1004TimedResetResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 4),
    _A1004TimedResetResolution_Type()
)
a1004TimedResetResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004TimedResetResolution.setStatus("mandatory")
_A1004TimeUntilSystemReset_Type = DmiInteger
_A1004TimeUntilSystemReset_Object = MibTableColumn
a1004TimeUntilSystemReset = _A1004TimeUntilSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 5),
    _A1004TimeUntilSystemReset_Type()
)
a1004TimeUntilSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004TimeUntilSystemReset.setStatus("mandatory")


class _A1004SystemPowerCapabilities_Type(Integer32):
    """Custom type a1004SystemPowerCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vOffOnly", 3),
          ("vOnAndOff", 2),
          ("vOnOnly", 4),
          ("vUnknown", 0),
          ("vUnsupported", 1))
    )


_A1004SystemPowerCapabilities_Type.__name__ = "Integer32"
_A1004SystemPowerCapabilities_Object = MibTableColumn
a1004SystemPowerCapabilities = _A1004SystemPowerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 6),
    _A1004SystemPowerCapabilities_Type()
)
a1004SystemPowerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004SystemPowerCapabilities.setStatus("mandatory")


class _A1004SystemPowerStatus_Type(Integer32):
    """Custom type a1004SystemPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A1004SystemPowerStatus_Type.__name__ = "Integer32"
_A1004SystemPowerStatus_Object = MibTableColumn
a1004SystemPowerStatus = _A1004SystemPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 7),
    _A1004SystemPowerStatus_Type()
)
a1004SystemPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004SystemPowerStatus.setStatus("mandatory")


class _A1004EventLoggingCapability_Type(Integer32):
    """Custom type a1004EventLoggingCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vActive", 2),
          ("vInactive", 3),
          ("vUnknown", 0),
          ("vUnsupported", 1))
    )


_A1004EventLoggingCapability_Type.__name__ = "Integer32"
_A1004EventLoggingCapability_Object = MibTableColumn
a1004EventLoggingCapability = _A1004EventLoggingCapability_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 8),
    _A1004EventLoggingCapability_Type()
)
a1004EventLoggingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004EventLoggingCapability.setStatus("mandatory")
_A1004WatchdogTimerIncrement_Type = DmiInteger
_A1004WatchdogTimerIncrement_Object = MibTableColumn
a1004WatchdogTimerIncrement = _A1004WatchdogTimerIncrement_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 9),
    _A1004WatchdogTimerIncrement_Type()
)
a1004WatchdogTimerIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004WatchdogTimerIncrement.setStatus("mandatory")
_A1004WatchdogTimerResolution_Type = DmiInteger
_A1004WatchdogTimerResolution_Object = MibTableColumn
a1004WatchdogTimerResolution = _A1004WatchdogTimerResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 10),
    _A1004WatchdogTimerResolution_Type()
)
a1004WatchdogTimerResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004WatchdogTimerResolution.setStatus("mandatory")
_A1004WatchdogUpdateInterval_Type = DmiInteger
_A1004WatchdogUpdateInterval_Object = MibTableColumn
a1004WatchdogUpdateInterval = _A1004WatchdogUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 11),
    _A1004WatchdogUpdateInterval_Type()
)
a1004WatchdogUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004WatchdogUpdateInterval.setStatus("mandatory")


class _A1004UseSystemWatchdogFeature_Type(Integer32):
    """Custom type a1004UseSystemWatchdogFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A1004UseSystemWatchdogFeature_Type.__name__ = "Integer32"
_A1004UseSystemWatchdogFeature_Object = MibTableColumn
a1004UseSystemWatchdogFeature = _A1004UseSystemWatchdogFeature_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 12),
    _A1004UseSystemWatchdogFeature_Type()
)
a1004UseSystemWatchdogFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004UseSystemWatchdogFeature.setStatus("mandatory")


class _A1004ResetSystemAfterDelay_Type(Integer32):
    """Custom type a1004ResetSystemAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A1004ResetSystemAfterDelay_Type.__name__ = "Integer32"
_A1004ResetSystemAfterDelay_Object = MibTableColumn
a1004ResetSystemAfterDelay = _A1004ResetSystemAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 13),
    _A1004ResetSystemAfterDelay_Type()
)
a1004ResetSystemAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ResetSystemAfterDelay.setStatus("mandatory")


class _A1004SavePersistentData_Type(Integer32):
    """Custom type a1004SavePersistentData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A1004SavePersistentData_Type.__name__ = "Integer32"
_A1004SavePersistentData_Object = MibTableColumn
a1004SavePersistentData = _A1004SavePersistentData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 15),
    _A1004SavePersistentData_Type()
)
a1004SavePersistentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004SavePersistentData.setStatus("mandatory")


class _A1004RestoreFactoryDefaults_Type(Integer32):
    """Custom type a1004RestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A1004RestoreFactoryDefaults_Type.__name__ = "Integer32"
_A1004RestoreFactoryDefaults_Object = MibTableColumn
a1004RestoreFactoryDefaults = _A1004RestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 16),
    _A1004RestoreFactoryDefaults_Type()
)
a1004RestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004RestoreFactoryDefaults.setStatus("mandatory")


class _A1004ShutdownOs_Type(Integer32):
    """Custom type a1004ShutdownOs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdown", 0),
          ("vShutdownOs", 1))
    )


_A1004ShutdownOs_Type.__name__ = "Integer32"
_A1004ShutdownOs_Object = MibTableColumn
a1004ShutdownOs = _A1004ShutdownOs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 17),
    _A1004ShutdownOs_Type()
)
a1004ShutdownOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOs.setStatus("mandatory")


class _A1004ShutdownOsAndPowerOff_Type(Integer32):
    """Custom type a1004ShutdownOsAndPowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdownAndPowerOff", 0),
          ("vShutdownAndPowerOff", 1))
    )


_A1004ShutdownOsAndPowerOff_Type.__name__ = "Integer32"
_A1004ShutdownOsAndPowerOff_Object = MibTableColumn
a1004ShutdownOsAndPowerOff = _A1004ShutdownOsAndPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 18),
    _A1004ShutdownOsAndPowerOff_Type()
)
a1004ShutdownOsAndPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOsAndPowerOff.setStatus("mandatory")


class _A1004ShutdownOsAndHardwareReset_Type(Integer32):
    """Custom type a1004ShutdownOsAndHardwareReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdownAndHardwareReset", 0),
          ("vShutdownAndHardwareReset", 1))
    )


_A1004ShutdownOsAndHardwareReset_Type.__name__ = "Integer32"
_A1004ShutdownOsAndHardwareReset_Object = MibTableColumn
a1004ShutdownOsAndHardwareReset = _A1004ShutdownOsAndHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 19),
    _A1004ShutdownOsAndHardwareReset_Type()
)
a1004ShutdownOsAndHardwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOsAndHardwareReset.setStatus("mandatory")


class _A1004IssueAHardwareNmi_Type(Integer32):
    """Custom type a1004IssueAHardwareNmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotIssueAnNmi", 0),
          ("vIssueAnNmi", 1))
    )


_A1004IssueAHardwareNmi_Type.__name__ = "Integer32"
_A1004IssueAHardwareNmi_Object = MibTableColumn
a1004IssueAHardwareNmi = _A1004IssueAHardwareNmi_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1004, 1, 20),
    _A1004IssueAHardwareNmi_Type()
)
a1004IssueAHardwareNmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004IssueAHardwareNmi.setStatus("mandatory")
_TSystemEventLog_Object = MibTable
tSystemEventLog = _TSystemEventLog_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006)
)
if mibBuilder.loadTexts:
    tSystemEventLog.setStatus("mandatory")
_ESystemEventLog_Object = MibTableRow
eSystemEventLog = _ESystemEventLog_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1)
)
eSystemEventLog.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1006Selfid"),
)
if mibBuilder.loadTexts:
    eSystemEventLog.setStatus("mandatory")
_A1006Selfid_Type = DmiInteger
_A1006Selfid_Object = MibTableColumn
a1006Selfid = _A1006Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1, 1),
    _A1006Selfid_Type()
)
a1006Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006Selfid.setStatus("mandatory")
_A1006Timestamp_Type = DmiDateX
_A1006Timestamp_Object = MibTableColumn
a1006Timestamp = _A1006Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1, 2),
    _A1006Timestamp_Type()
)
a1006Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006Timestamp.setStatus("mandatory")
_A1006RecordType_Type = DmiInteger
_A1006RecordType_Object = MibTableColumn
a1006RecordType = _A1006RecordType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1, 3),
    _A1006RecordType_Type()
)
a1006RecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordType.setStatus("mandatory")
_A1006RecordLength_Type = DmiInteger
_A1006RecordLength_Object = MibTableColumn
a1006RecordLength = _A1006RecordLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1, 4),
    _A1006RecordLength_Type()
)
a1006RecordLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordLength.setStatus("mandatory")
_A1006RecordData_Type = DmiOctetstring
_A1006RecordData_Object = MibTableColumn
a1006RecordData = _A1006RecordData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1006, 1, 5),
    _A1006RecordData_Type()
)
a1006RecordData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordData.setStatus("mandatory")
_TEventGenerationForIcmbState_Object = MibTable
tEventGenerationForIcmbState = _TEventGenerationForIcmbState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007)
)
if mibBuilder.loadTexts:
    tEventGenerationForIcmbState.setStatus("mandatory")
_EEventGenerationForIcmbState_Object = MibTableRow
eEventGenerationForIcmbState = _EEventGenerationForIcmbState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1)
)
eEventGenerationForIcmbState.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForIcmbState.setStatus("mandatory")


class _A1007EventType_Type(Integer32):
    """Custom type a1007EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vChassisAvailabilityChange", 1)
    )


_A1007EventType_Type.__name__ = "Integer32"
_A1007EventType_Object = MibTableColumn
a1007EventType = _A1007EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 1),
    _A1007EventType_Type()
)
a1007EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007EventType.setStatus("mandatory")


class _A1007EventSeverity_Type(Integer32):
    """Custom type a1007EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A1007EventSeverity_Type.__name__ = "Integer32"
_A1007EventSeverity_Object = MibTableColumn
a1007EventSeverity = _A1007EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 2),
    _A1007EventSeverity_Type()
)
a1007EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007EventSeverity.setStatus("mandatory")


class _A1007IsEventState_based_Type(Integer32):
    """Custom type a1007IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A1007IsEventState_based_Type.__name__ = "Integer32"
_A1007IsEventState_based_Object = MibScalar
a1007IsEventState_based = _A1007IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 3),
    _A1007IsEventState_based_Type()
)
a1007IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007IsEventState_based.setStatus("mandatory")
_A1007EventStateKey_Type = DmiInteger
_A1007EventStateKey_Object = MibTableColumn
a1007EventStateKey = _A1007EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 4),
    _A1007EventStateKey_Type()
)
a1007EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007EventStateKey.setStatus("mandatory")
_A1007AssociatedGroup_Type = DmiDisplaystring
_A1007AssociatedGroup_Object = MibTableColumn
a1007AssociatedGroup = _A1007AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 5),
    _A1007AssociatedGroup_Type()
)
a1007AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007AssociatedGroup.setStatus("mandatory")


class _A1007EventSystem_Type(Integer32):
    """Custom type a1007EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A1007EventSystem_Type.__name__ = "Integer32"
_A1007EventSystem_Object = MibTableColumn
a1007EventSystem = _A1007EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 6),
    _A1007EventSystem_Type()
)
a1007EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007EventSystem.setStatus("mandatory")


class _A1007EventSubsystem_Type(Integer32):
    """Custom type a1007EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A1007EventSubsystem_Type.__name__ = "Integer32"
_A1007EventSubsystem_Object = MibTableColumn
a1007EventSubsystem = _A1007EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 7),
    _A1007EventSubsystem_Type()
)
a1007EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1007EventSubsystem.setStatus("mandatory")
_TEifControl_Object = MibTable
tEifControl = _TEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000)
)
if mibBuilder.loadTexts:
    tEifControl.setStatus("mandatory")
_EEifControl_Object = MibTableRow
eEifControl = _EEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000, 1)
)
eEifControl.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eEifControl.setStatus("mandatory")


class _A2000Status_Type(Integer32):
    """Custom type a2000Status based on Integer32"""
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
        *(("vConstructedOnly", 4),
          ("vCreatedOnly", 3),
          ("vFullyOperational", 5),
          ("vIdle1", 6),
          ("vOther1", 1),
          ("vUnknown1", 2))
    )


_A2000Status_Type.__name__ = "Integer32"
_A2000Status_Object = MibTableColumn
a2000Status = _A2000Status_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000, 1, 1),
    _A2000Status_Type()
)
a2000Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000Status.setStatus("mandatory")
_A2000DimContext_Type = DmiOctetstring
_A2000DimContext_Object = MibTableColumn
a2000DimContext = _A2000DimContext_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000, 1, 2),
    _A2000DimContext_Type()
)
a2000DimContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000DimContext.setStatus("mandatory")
_A2000PersistentDataWriteDelay_Type = DmiInteger
_A2000PersistentDataWriteDelay_Object = MibTableColumn
a2000PersistentDataWriteDelay = _A2000PersistentDataWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000, 1, 3),
    _A2000PersistentDataWriteDelay_Type()
)
a2000PersistentDataWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2000PersistentDataWriteDelay.setStatus("mandatory")
_A2000EifInterfaceName_Type = DmiDisplaystring
_A2000EifInterfaceName_Object = MibTableColumn
a2000EifInterfaceName = _A2000EifInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2000, 1, 4),
    _A2000EifInterfaceName_Type()
)
a2000EifInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2000EifInterfaceName.setStatus("mandatory")
_TEifExtensionList_Object = MibTable
tEifExtensionList = _TEifExtensionList_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2001)
)
if mibBuilder.loadTexts:
    tEifExtensionList.setStatus("mandatory")
_EEifExtensionList_Object = MibTableRow
eEifExtensionList = _EEifExtensionList_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2001, 1)
)
eEifExtensionList.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2001Index"),
)
if mibBuilder.loadTexts:
    eEifExtensionList.setStatus("mandatory")
_A2001Index_Type = DmiInteger
_A2001Index_Object = MibTableColumn
a2001Index = _A2001Index_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2001, 1, 1),
    _A2001Index_Type()
)
a2001Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2001Index.setStatus("mandatory")
_A2001Filename_Type = DmiDisplaystring
_A2001Filename_Object = MibTableColumn
a2001Filename = _A2001Filename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2001, 1, 2),
    _A2001Filename_Type()
)
a2001Filename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2001Filename.setStatus("mandatory")
_TEventGenerationForEifControl_Object = MibTable
tEventGenerationForEifControl = _TEventGenerationForEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002)
)
if mibBuilder.loadTexts:
    tEventGenerationForEifControl.setStatus("mandatory")
_EEventGenerationForEifControl_Object = MibTableRow
eEventGenerationForEifControl = _EEventGenerationForEifControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1)
)
eEventGenerationForEifControl.setIndexNames(
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForEifControl.setStatus("mandatory")


class _A2002EventType_Type(Integer32):
    """Custom type a2002EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNoDimContextsCreated", 1)
    )


_A2002EventType_Type.__name__ = "Integer32"
_A2002EventType_Object = MibTableColumn
a2002EventType = _A2002EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 1),
    _A2002EventType_Type()
)
a2002EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventType.setStatus("mandatory")


class _A2002EventSeverity_Type(Integer32):
    """Custom type a2002EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A2002EventSeverity_Type.__name__ = "Integer32"
_A2002EventSeverity_Object = MibTableColumn
a2002EventSeverity = _A2002EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 2),
    _A2002EventSeverity_Type()
)
a2002EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSeverity.setStatus("mandatory")


class _A2002IsEventState_based_Type(Integer32):
    """Custom type a2002IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A2002IsEventState_based_Type.__name__ = "Integer32"
_A2002IsEventState_based_Object = MibScalar
a2002IsEventState_based = _A2002IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 3),
    _A2002IsEventState_based_Type()
)
a2002IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002IsEventState_based.setStatus("mandatory")
_A2002EventStateKey_Type = DmiInteger
_A2002EventStateKey_Object = MibTableColumn
a2002EventStateKey = _A2002EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 4),
    _A2002EventStateKey_Type()
)
a2002EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventStateKey.setStatus("mandatory")
_A2002AssociatedGroup_Type = DmiDisplaystring
_A2002AssociatedGroup_Object = MibTableColumn
a2002AssociatedGroup = _A2002AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 5),
    _A2002AssociatedGroup_Type()
)
a2002AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002AssociatedGroup.setStatus("mandatory")


class _A2002EventSystem_Type(Integer32):
    """Custom type a2002EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A2002EventSystem_Type.__name__ = "Integer32"
_A2002EventSystem_Object = MibTableColumn
a2002EventSystem = _A2002EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 6),
    _A2002EventSystem_Type()
)
a2002EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSystem.setStatus("mandatory")


class _A2002EventSubsystem_Type(Integer32):
    """Custom type a2002EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A2002EventSubsystem_Type.__name__ = "Integer32"
_A2002EventSubsystem_Object = MibTableColumn
a2002EventSubsystem = _A2002EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 7),
    _A2002EventSubsystem_Type()
)
a2002EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2002EventSubsystem.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1ForPhysicalContainer = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 0, 6)
)
trap1ForPhysicalContainer.setObjects(
      *(("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventType"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSeverity"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116IsEventState_based"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventStateKey"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116AssociatedGroup"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSystem"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSubsystem"))
)
if mibBuilder.loadTexts:
    trap1ForPhysicalContainer.setStatus(
        ""
    )

trap2ForPhysicalContainer = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 116, 1, 0, 256)
)
trap2ForPhysicalContainer.setObjects(
      *(("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventType"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSeverity"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116IsEventState_based"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventStateKey"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116AssociatedGroup"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSystem"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a116EventSubsystem"))
)
if mibBuilder.loadTexts:
    trap2ForPhysicalContainer.setStatus(
        ""
    )

trap1ForIcmbState = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 1007, 1, 0, 1)
)
trap1ForIcmbState.setObjects(
      *(("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007EventType"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007EventSeverity"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007IsEventState_based"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007EventStateKey"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007AssociatedGroup"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007EventSystem"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a1007EventSubsystem"))
)
if mibBuilder.loadTexts:
    trap1ForIcmbState.setStatus(
        ""
    )

trap1ForEifControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5, 1, 2002, 1, 0, 1)
)
trap1ForEifControl.setObjects(
      *(("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002EventType"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002EventSeverity"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002IsEventState_based"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002EventStateKey"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002AssociatedGroup"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002EventSystem"),
        ("INTELCORPORATIONICMBGENERICCHASSIS-MIB", "a2002EventSubsystem"))
)
if mibBuilder.loadTexts:
    trap1ForEifControl.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATIONICMBGENERICCHASSIS-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-products": server_products,
       "platforms": platforms,
       "icmbChassis": icmbChassis,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tIcmbState": tIcmbState,
       "eIcmbState": eIcmbState,
       "a12ChassisAvailable": a12ChassisAvailable,
       "a12IcmbId": a12IcmbId,
       "a12SdrDeviceId": a12SdrDeviceId,
       "a12SelDeviceId": a12SelDeviceId,
       "a12SmDeviceId": a12SmDeviceId,
       "a12SdrReadState": a12SdrReadState,
       "a12EventPollingPeriod": a12EventPollingPeriod,
       "a12EventCount": a12EventCount,
       "a12ManageChassis": a12ManageChassis,
       "a12SetAvailablityState": a12SetAvailablityState,
       "a12UniqueId": a12UniqueId,
       "a12PreviousAvailabilityStatus": a12PreviousAvailabilityStatus,
       "tOperationalState": tOperationalState,
       "eOperationalState": eOperationalState,
       "a31OperationalStateInstanceIndex": a31OperationalStateInstanceIndex,
       "a31DeviceGroupIndex": a31DeviceGroupIndex,
       "a31OperationalStatus": a31OperationalStatus,
       "a31UsageState": a31UsageState,
       "a31AvailabilityStatus": a31AvailabilityStatus,
       "a31AdministrativeState": a31AdministrativeState,
       "a31FatalErrorCount": a31FatalErrorCount,
       "a31MajorErrorCount": a31MajorErrorCount,
       "a31WarningErrorCount": a31WarningErrorCount,
       "a31CurrentErrorStatus": a31CurrentErrorStatus,
       "tFieldReplaceableUnit": tFieldReplaceableUnit,
       "eFieldReplaceableUnit": eFieldReplaceableUnit,
       "a93FruIndex": a93FruIndex,
       "a93DeviceGroupIndex": a93DeviceGroupIndex,
       "a93Description": a93Description,
       "a93Manufacturer": a93Manufacturer,
       "a93Model": a93Model,
       "a93PartNumber": a93PartNumber,
       "a93FruSerialNumber": a93FruSerialNumber,
       "a93RevisionLevel": a93RevisionLevel,
       "a93WarrantyStartDate": a93WarrantyStartDate,
       "a93WarrantyDuration": a93WarrantyDuration,
       "a93SupportPhoneNumber": a93SupportPhoneNumber,
       "a93FruInternetUniformResourceLocator": a93FruInternetUniformResourceLocator,
       "tEventGenerationForPhysicalContainer": tEventGenerationForPhysicalContainer,
       "eEventGenerationForPhysicalContainer": eEventGenerationForPhysicalContainer,
       "trap1ForPhysicalContainer": trap1ForPhysicalContainer,
       "trap2ForPhysicalContainer": trap2ForPhysicalContainer,
       "a116EventType": a116EventType,
       "a116EventSeverity": a116EventSeverity,
       "a116IsEventState-based": a116IsEventState_based,
       "a116EventStateKey": a116EventStateKey,
       "a116AssociatedGroup": a116AssociatedGroup,
       "a116EventSystem": a116EventSystem,
       "a116EventSubsystem": a116EventSubsystem,
       "tPhysicalContainerGlobalTable": tPhysicalContainerGlobalTable,
       "ePhysicalContainerGlobalTable": ePhysicalContainerGlobalTable,
       "a127ContainerOrChassisType": a127ContainerOrChassisType,
       "a127AssetTag": a127AssetTag,
       "a127ChassisLockPresent": a127ChassisLockPresent,
       "a127BootupState": a127BootupState,
       "a127PowerState": a127PowerState,
       "a127ThermalState": a127ThermalState,
       "a127FruGroupIndex": a127FruGroupIndex,
       "a127OperationalGroupIndex": a127OperationalGroupIndex,
       "a127ContainerIndex": a127ContainerIndex,
       "a127ContainerName": a127ContainerName,
       "a127ContainerLocation": a127ContainerLocation,
       "a127ContainerSecurityStatus": a127ContainerSecurityStatus,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a1001MibName": a1001MibName,
       "a1001MibOid": a1001MibOid,
       "a1001DisableTrap": a1001DisableTrap,
       "tSystemControl": tSystemControl,
       "eSystemControl": eSystemControl,
       "a1004Selfid": a1004Selfid,
       "a1004ResetSystem": a1004ResetSystem,
       "a1004TimedResetIncrement": a1004TimedResetIncrement,
       "a1004TimedResetResolution": a1004TimedResetResolution,
       "a1004TimeUntilSystemReset": a1004TimeUntilSystemReset,
       "a1004SystemPowerCapabilities": a1004SystemPowerCapabilities,
       "a1004SystemPowerStatus": a1004SystemPowerStatus,
       "a1004EventLoggingCapability": a1004EventLoggingCapability,
       "a1004WatchdogTimerIncrement": a1004WatchdogTimerIncrement,
       "a1004WatchdogTimerResolution": a1004WatchdogTimerResolution,
       "a1004WatchdogUpdateInterval": a1004WatchdogUpdateInterval,
       "a1004UseSystemWatchdogFeature": a1004UseSystemWatchdogFeature,
       "a1004ResetSystemAfterDelay": a1004ResetSystemAfterDelay,
       "a1004SavePersistentData": a1004SavePersistentData,
       "a1004RestoreFactoryDefaults": a1004RestoreFactoryDefaults,
       "a1004ShutdownOs": a1004ShutdownOs,
       "a1004ShutdownOsAndPowerOff": a1004ShutdownOsAndPowerOff,
       "a1004ShutdownOsAndHardwareReset": a1004ShutdownOsAndHardwareReset,
       "a1004IssueAHardwareNmi": a1004IssueAHardwareNmi,
       "tSystemEventLog": tSystemEventLog,
       "eSystemEventLog": eSystemEventLog,
       "a1006Selfid": a1006Selfid,
       "a1006Timestamp": a1006Timestamp,
       "a1006RecordType": a1006RecordType,
       "a1006RecordLength": a1006RecordLength,
       "a1006RecordData": a1006RecordData,
       "tEventGenerationForIcmbState": tEventGenerationForIcmbState,
       "eEventGenerationForIcmbState": eEventGenerationForIcmbState,
       "trap1ForIcmbState": trap1ForIcmbState,
       "a1007EventType": a1007EventType,
       "a1007EventSeverity": a1007EventSeverity,
       "a1007IsEventState-based": a1007IsEventState_based,
       "a1007EventStateKey": a1007EventStateKey,
       "a1007AssociatedGroup": a1007AssociatedGroup,
       "a1007EventSystem": a1007EventSystem,
       "a1007EventSubsystem": a1007EventSubsystem,
       "tEifControl": tEifControl,
       "eEifControl": eEifControl,
       "a2000Status": a2000Status,
       "a2000DimContext": a2000DimContext,
       "a2000PersistentDataWriteDelay": a2000PersistentDataWriteDelay,
       "a2000EifInterfaceName": a2000EifInterfaceName,
       "tEifExtensionList": tEifExtensionList,
       "eEifExtensionList": eEifExtensionList,
       "a2001Index": a2001Index,
       "a2001Filename": a2001Filename,
       "tEventGenerationForEifControl": tEventGenerationForEifControl,
       "eEventGenerationForEifControl": eEventGenerationForEifControl,
       "trap1ForEifControl": trap1ForEifControl,
       "a2002EventType": a2002EventType,
       "a2002EventSeverity": a2002EventSeverity,
       "a2002IsEventState-based": a2002IsEventState_based,
       "a2002EventStateKey": a2002EventStateKey,
       "a2002AssociatedGroup": a2002AssociatedGroup,
       "a2002EventSystem": a2002EventSystem,
       "a2002EventSubsystem": a2002EventSubsystem}
)
