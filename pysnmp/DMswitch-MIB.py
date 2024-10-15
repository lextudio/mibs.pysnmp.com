# SNMP MIB module (DMswitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMswitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:46 2024
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

(datacomAccessDevicesMIBs,) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomAccessDevicesMIBs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dmSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ValidStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )



class KeySegment(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class StaPathCostMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DmSwitchMIBObjects_ObjectIdentity = ObjectIdentity
dmSwitchMIBObjects = _DmSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1)
)
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 1),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1)
)
switchInfoEntry.setIndexNames(
    (0, "DMswitch-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")
_SwHardwareVer_Type = Integer32
_SwHardwareVer_Object = MibTableColumn
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 2),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwBootLoaderVer_Type(DisplayString):
    """Custom type swBootLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootLoaderVer_Type.__name__ = "DisplayString"
_SwBootLoaderVer_Object = MibTableColumn
swBootLoaderVer = _SwBootLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 3),
    _SwBootLoaderVer_Type()
)
swBootLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootLoaderVer.setStatus("current")


class _SwFirmwareVer_Type(DisplayString):
    """Custom type swFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwFirmwareVer_Type.__name__ = "DisplayString"
_SwFirmwareVer_Object = MibTableColumn
swFirmwareVer = _SwFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 4),
    _SwFirmwareVer_Type()
)
swFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 5),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
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
        *(("externalPower", 4),
          ("internalAndRedundantPower", 3),
          ("internalPower", 1),
          ("redundantPower", 2))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 6),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupMaster", 2),
          ("master", 1),
          ("slave", 3))
    )


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 7),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibTableColumn
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 8),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwProdName_Type(DisplayString):
    """Custom type swProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdName_Type.__name__ = "DisplayString"
_SwProdName_Object = MibTableColumn
swProdName = _SwProdName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 9),
    _SwProdName_Type()
)
swProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdName.setStatus("current")


class _SwProdModelId_Type(Integer32):
    """Custom type swProdModelId based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("dmSwitch2204G1", 1),
          ("dmSwitch2304G1", 2),
          ("dmSwitch3224F1", 3),
          ("dmSwitch3224F2", 5),
          ("dmSwitch3224F3", 7),
          ("dmSwitch3324F1", 4),
          ("dmSwitch3324F2", 6),
          ("dmSwitch3324F3", 8),
          ("eth10gx2xstm4", 29),
          ("eth10gx32xe1", 27),
          ("eth10gx4xstm1", 28),
          ("eth12gx", 11),
          ("eth12gxEth1x10gx", 15),
          ("eth16gx2x10gx4xstm1hseries", 55),
          ("eth16gx4xstm1hseries", 56),
          ("eth1x10gx", 13),
          ("eth20gt4gc", 37),
          ("eth20gt4gc2xss", 52),
          ("eth20gt4gc2xx", 38),
          ("eth20gt4gc2xxs", 40),
          ("eth20gt4gc4xs", 66),
          ("eth20gt4gc4xx", 41),
          ("eth20gt4gcs", 39),
          ("eth20gx2x10gx32xe1hseries", 54),
          ("eth20gx32xe1hseries", 53),
          ("eth24gt", 16),
          ("eth24gthseries", 50),
          ("eth24gx", 12),
          ("eth24gx2x10gxeseries", 57),
          ("eth24gx2x10gxhseriesII", 65),
          ("eth24gx2xx", 33),
          ("eth24gx2xxs", 35),
          ("eth24gx4gx", 32),
          ("eth24gx4xs", 71),
          ("eth24gx4xx", 36),
          ("eth24gxEth2x10gx", 20),
          ("eth24gxEth2x10gxhseries", 23),
          ("eth24gxeseries", 58),
          ("eth24gxhseries", 25),
          ("eth24gxhseriesII", 67),
          ("eth24gxlseries", 31),
          ("eth24gxs", 34),
          ("eth2x10gx", 14),
          ("eth2x10gxhseries", 26),
          ("eth2x10gxhseriesII", 68),
          ("eth44gt4gc", 42),
          ("eth44gt4gc2xs", 47),
          ("eth44gt4gc2xss", 48),
          ("eth44gt4gc2xx", 43),
          ("eth44gt4gc2xxs", 45),
          ("eth44gt4gc2xxsmplsdc", 63),
          ("eth44gt4gc4xs", 49),
          ("eth44gt4gc4xx", 46),
          ("eth44gt4gc4xxmplsdc", 64),
          ("eth44gt4gcs", 44),
          ("eth44gt4gcsmplsdc", 62),
          ("eth48gt", 17),
          ("eth48gteseries", 60),
          ("eth48gthseries", 51),
          ("eth48gx", 21),
          ("eth48gxhseries", 24),
          ("eth48gxhseriesII", 69),
          ("eth4x10gxeseries", 59),
          ("eth4x10gxhseries", 22),
          ("eth4x10gxhseriesII", 70),
          ("mpu192", 9),
          ("mpu384", 10),
          ("mpu512", 30),
          ("mpu960", 61))
    )


_SwProdModelId_Type.__name__ = "Integer32"
_SwProdModelId_Object = MibTableColumn
swProdModelId = _SwProdModelId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 10),
    _SwProdModelId_Type()
)
swProdModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdModelId.setStatus("current")


class _SwFirmwareReleaseDate_Type(DisplayString):
    """Custom type swFirmwareReleaseDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFirmwareReleaseDate_Type.__name__ = "DisplayString"
_SwFirmwareReleaseDate_Object = MibTableColumn
swFirmwareReleaseDate = _SwFirmwareReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 11),
    _SwFirmwareReleaseDate_Type()
)
swFirmwareReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareReleaseDate.setStatus("current")
_SwTemperature_Type = Integer32
_SwTemperature_Object = MibTableColumn
swTemperature = _SwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 12),
    _SwTemperature_Type()
)
swTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTemperature.setStatus("current")
_SwG704IntfNumber_Type = Integer32
_SwG704IntfNumber_Object = MibTableColumn
swG704IntfNumber = _SwG704IntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 13),
    _SwG704IntfNumber_Type()
)
swG704IntfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swG704IntfNumber.setStatus("current")
_SwE1cIntfNumber_Type = Integer32
_SwE1cIntfNumber_Object = MibTableColumn
swE1cIntfNumber = _SwE1cIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 14),
    _SwE1cIntfNumber_Type()
)
swE1cIntfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swE1cIntfNumber.setStatus("current")
_SwBundleIntfNumber_Type = Integer32
_SwBundleIntfNumber_Object = MibTableColumn
swBundleIntfNumber = _SwBundleIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 15),
    _SwBundleIntfNumber_Type()
)
swBundleIntfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBundleIntfNumber.setStatus("current")
_SwPtpIntfNumber_Type = Integer32
_SwPtpIntfNumber_Object = MibTableColumn
swPtpIntfNumber = _SwPtpIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 16),
    _SwPtpIntfNumber_Type()
)
swPtpIntfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPtpIntfNumber.setStatus("current")
_SwSdhIntfNumber_Type = Integer32
_SwSdhIntfNumber_Object = MibTableColumn
swSdhIntfNumber = _SwSdhIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 17),
    _SwSdhIntfNumber_Type()
)
swSdhIntfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSdhIntfNumber.setStatus("current")
_SwVC4Number_Type = Integer32
_SwVC4Number_Object = MibTableColumn
swVC4Number = _SwVC4Number_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 18),
    _SwVC4Number_Type()
)
swVC4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVC4Number.setStatus("current")
_SwVC12Number_Type = Integer32
_SwVC12Number_Object = MibTableColumn
swVC12Number = _SwVC12Number_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 2, 1, 19),
    _SwVC12Number_Type()
)
swVC12Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVC12Number.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3)
)


class _SwProdManufacturer_Type(DisplayString):
    """Custom type swProdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdManufacturer_Type.__name__ = "DisplayString"
_SwProdManufacturer_Object = MibScalar
swProdManufacturer = _SwProdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3, 2),
    _SwProdManufacturer_Type()
)
swProdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdManufacturer.setStatus("current")


class _SwProdDescription_Type(DisplayString):
    """Custom type swProdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdDescription_Type.__name__ = "DisplayString"
_SwProdDescription_Object = MibScalar
swProdDescription = _SwProdDescription_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3, 3),
    _SwProdDescription_Type()
)
swProdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdDescription.setStatus("current")


class _SwProdUrl_Type(DisplayString):
    """Custom type swProdUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdUrl_Type.__name__ = "DisplayString"
_SwProdUrl_Object = MibScalar
swProdUrl = _SwProdUrl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3, 6),
    _SwIdentifier_Type()
)
swIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIdentifier.setStatus("current")


class _SwVendorId_Type(Integer32):
    """Custom type swVendorId based on Integer32"""
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
              9,
              2000000254,
              2000000255)
        )
    )
    namedValues = NamedValues(
        *(("asga", 3),
          ("datacom", 1),
          ("digitel", 5),
          ("elebra", 7),
          ("ieru", 2),
          ("infNotAvailable", 2000000255),
          ("none", 6),
          ("objectNonexistentInModel", 2000000254),
          ("osp", 9),
          ("parks", 4))
    )


_SwVendorId_Type.__name__ = "Integer32"
_SwVendorId_Object = MibScalar
swVendorId = _SwVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 3, 7),
    _SwVendorId_Type()
)
swVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVendorId.setStatus("mandatory")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 4)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 4, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "DMswitch-MIB", "swIndivPowerUnitIndex"),
    (0, "DMswitch-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 4, 1, 1),
    _SwIndivPowerUnitIndex_Type()
)
swIndivPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerUnitIndex.setStatus("current")


class _SwIndivPowerIndex_Type(Integer32):
    """Custom type swIndivPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SwIndivPowerIndex_Type.__name__ = "Integer32"
_SwIndivPowerIndex_Object = MibTableColumn
swIndivPowerIndex = _SwIndivPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 4, 1, 2),
    _SwIndivPowerIndex_Type()
)
swIndivPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerIndex.setStatus("current")


class _SwIndivPowerStatus_Type(Integer32):
    """Custom type swIndivPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("notPresent", 3),
          ("red", 1))
    )


_SwIndivPowerStatus_Type.__name__ = "Integer32"
_SwIndivPowerStatus_Object = MibTableColumn
swIndivPowerStatus = _SwIndivPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 4, 1, 3),
    _SwIndivPowerStatus_Type()
)
swIndivPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerStatus.setStatus("current")
_SwitchIndivFanTable_Object = MibTable
switchIndivFanTable = _SwitchIndivFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 5)
)
if mibBuilder.loadTexts:
    switchIndivFanTable.setStatus("current")
_SwitchIndivFanEntry_Object = MibTableRow
switchIndivFanEntry = _SwitchIndivFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 5, 1)
)
switchIndivFanEntry.setIndexNames(
    (0, "DMswitch-MIB", "swIndivFanUnitIndex"),
    (0, "DMswitch-MIB", "swIndivFanIndex"),
)
if mibBuilder.loadTexts:
    switchIndivFanEntry.setStatus("current")
_SwIndivFanUnitIndex_Type = Integer32
_SwIndivFanUnitIndex_Object = MibTableColumn
swIndivFanUnitIndex = _SwIndivFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 5, 1, 1),
    _SwIndivFanUnitIndex_Type()
)
swIndivFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivFanUnitIndex.setStatus("current")


class _SwIndivFanIndex_Type(Integer32):
    """Custom type swIndivFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SwIndivFanIndex_Type.__name__ = "Integer32"
_SwIndivFanIndex_Object = MibTableColumn
swIndivFanIndex = _SwIndivFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 5, 1, 2),
    _SwIndivFanIndex_Type()
)
swIndivFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivFanIndex.setStatus("current")


class _SwIndivFanStatus_Type(Integer32):
    """Custom type swIndivFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("red", 1))
    )


_SwIndivFanStatus_Type.__name__ = "Integer32"
_SwIndivFanStatus_Object = MibTableColumn
swIndivFanStatus = _SwIndivFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 5, 1, 3),
    _SwIndivFanStatus_Type()
)
swIndivFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivFanStatus.setStatus("current")
_SwitchIndivAlarmTable_Object = MibTable
switchIndivAlarmTable = _SwitchIndivAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivAlarmTable.setStatus("current")
_SwitchIndivAlarmEntry_Object = MibTableRow
switchIndivAlarmEntry = _SwitchIndivAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 6, 1)
)
switchIndivAlarmEntry.setIndexNames(
    (0, "DMswitch-MIB", "swIndivAlarmUnitIndex"),
    (0, "DMswitch-MIB", "swIndivAlarmIndex"),
)
if mibBuilder.loadTexts:
    switchIndivAlarmEntry.setStatus("current")
_SwIndivAlarmUnitIndex_Type = Integer32
_SwIndivAlarmUnitIndex_Object = MibTableColumn
swIndivAlarmUnitIndex = _SwIndivAlarmUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 6, 1, 1),
    _SwIndivAlarmUnitIndex_Type()
)
swIndivAlarmUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivAlarmUnitIndex.setStatus("current")


class _SwIndivAlarmIndex_Type(Integer32):
    """Custom type swIndivAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwIndivAlarmIndex_Type.__name__ = "Integer32"
_SwIndivAlarmIndex_Object = MibTableColumn
swIndivAlarmIndex = _SwIndivAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 6, 1, 2),
    _SwIndivAlarmIndex_Type()
)
swIndivAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivAlarmIndex.setStatus("current")


class _SwIndivAlarmStatus_Type(Integer32):
    """Custom type swIndivAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("deactivated", 1))
    )


_SwIndivAlarmStatus_Type.__name__ = "Integer32"
_SwIndivAlarmStatus_Object = MibTableColumn
swIndivAlarmStatus = _SwIndivAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 6, 1, 3),
    _SwIndivAlarmStatus_Type()
)
swIndivAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivAlarmStatus.setStatus("current")
_SwitchResObj_Type = Integer32
_SwitchResObj_Object = MibScalar
switchResObj = _SwitchResObj_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 7),
    _SwitchResObj_Type()
)
switchResObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchResObj.setStatus("current")


class _SwHashConfig_Type(DisplayString):
    """Custom type swHashConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwHashConfig_Type.__name__ = "DisplayString"
_SwHashConfig_Object = MibScalar
swHashConfig = _SwHashConfig_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 8),
    _SwHashConfig_Type()
)
swHashConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHashConfig.setStatus("current")


class _SwHashStatus_Type(DisplayString):
    """Custom type swHashStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwHashStatus_Type.__name__ = "DisplayString"
_SwHashStatus_Object = MibScalar
swHashStatus = _SwHashStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 9),
    _SwHashStatus_Type()
)
swHashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHashStatus.setStatus("current")
_SwCpuUsage_Type = Integer32
_SwCpuUsage_Object = MibScalar
swCpuUsage = _SwCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 10),
    _SwCpuUsage_Type()
)
swCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsage.setStatus("current")
_SwMemUsage_Type = Integer32
_SwMemUsage_Object = MibScalar
swMemUsage = _SwMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 11),
    _SwMemUsage_Type()
)
swMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsage.setStatus("current")
_SwitchMacAddrUsageTable_Object = MibTable
switchMacAddrUsageTable = _SwitchMacAddrUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 12)
)
if mibBuilder.loadTexts:
    switchMacAddrUsageTable.setStatus("current")
_SwitchMacAddrUsageEntry_Object = MibTableRow
switchMacAddrUsageEntry = _SwitchMacAddrUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 12, 1)
)
switchMacAddrUsageEntry.setIndexNames(
    (0, "DMswitch-MIB", "swMacAddrUnitIndex"),
)
if mibBuilder.loadTexts:
    switchMacAddrUsageEntry.setStatus("current")
_SwMacAddrUnitIndex_Type = Integer32
_SwMacAddrUnitIndex_Object = MibTableColumn
swMacAddrUnitIndex = _SwMacAddrUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 12, 1, 1),
    _SwMacAddrUnitIndex_Type()
)
swMacAddrUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacAddrUnitIndex.setStatus("current")
_SwMacAddrUsageValue_Type = Integer32
_SwMacAddrUsageValue_Object = MibTableColumn
swMacAddrUsageValue = _SwMacAddrUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 12, 1, 2),
    _SwMacAddrUsageValue_Type()
)
swMacAddrUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacAddrUsageValue.setStatus("current")
_SwSlotNumber_Type = Integer32
_SwSlotNumber_Object = MibScalar
swSlotNumber = _SwSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 13),
    _SwSlotNumber_Type()
)
swSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSlotNumber.setStatus("current")
_SwitchMpuTable_Object = MibTable
switchMpuTable = _SwitchMpuTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14)
)
if mibBuilder.loadTexts:
    switchMpuTable.setStatus("current")
_SwitchMpuEntry_Object = MibTableRow
switchMpuEntry = _SwitchMpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1)
)
switchMpuEntry.setIndexNames(
    (0, "DMswitch-MIB", "swMpuIndex"),
)
if mibBuilder.loadTexts:
    switchMpuEntry.setStatus("current")
_SwMpuIndex_Type = Integer32
_SwMpuIndex_Object = MibTableColumn
swMpuIndex = _SwMpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1, 1),
    _SwMpuIndex_Type()
)
swMpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMpuIndex.setStatus("current")


class _SwMpuBootLoaderVer_Type(DisplayString):
    """Custom type swMpuBootLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMpuBootLoaderVer_Type.__name__ = "DisplayString"
_SwMpuBootLoaderVer_Object = MibTableColumn
swMpuBootLoaderVer = _SwMpuBootLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1, 2),
    _SwMpuBootLoaderVer_Type()
)
swMpuBootLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMpuBootLoaderVer.setStatus("current")


class _SwMpuRoleInSystem_Type(Integer32):
    """Custom type swMpuRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SwMpuRoleInSystem_Type.__name__ = "Integer32"
_SwMpuRoleInSystem_Object = MibTableColumn
swMpuRoleInSystem = _SwMpuRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1, 3),
    _SwMpuRoleInSystem_Type()
)
swMpuRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMpuRoleInSystem.setStatus("current")


class _SwMpuSerialNumber_Type(DisplayString):
    """Custom type swMpuSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwMpuSerialNumber_Type.__name__ = "DisplayString"
_SwMpuSerialNumber_Object = MibTableColumn
swMpuSerialNumber = _SwMpuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1, 4),
    _SwMpuSerialNumber_Type()
)
swMpuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMpuSerialNumber.setStatus("current")


class _SwMpuModelId_Type(Integer32):
    """Custom type swMpuModelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("mpu192", 9),
          ("mpu384", 10))
    )


_SwMpuModelId_Type.__name__ = "Integer32"
_SwMpuModelId_Object = MibTableColumn
swMpuModelId = _SwMpuModelId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 14, 1, 5),
    _SwMpuModelId_Type()
)
swMpuModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMpuModelId.setStatus("current")


class _SwHashHardware_Type(DisplayString):
    """Custom type swHashHardware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SwHashHardware_Type.__name__ = "DisplayString"
_SwHashHardware_Object = MibScalar
swHashHardware = _SwHashHardware_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 15),
    _SwHashHardware_Type()
)
swHashHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHashHardware.setStatus("current")
_SwitchIndivAlarmOutTable_Object = MibTable
switchIndivAlarmOutTable = _SwitchIndivAlarmOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 16)
)
if mibBuilder.loadTexts:
    switchIndivAlarmOutTable.setStatus("current")
_SwitchIndivAlarmOutEntry_Object = MibTableRow
switchIndivAlarmOutEntry = _SwitchIndivAlarmOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 16, 1)
)
switchIndivAlarmOutEntry.setIndexNames(
    (0, "DMswitch-MIB", "swIndivAlarmOutUnitIndex"),
)
if mibBuilder.loadTexts:
    switchIndivAlarmOutEntry.setStatus("current")
_SwIndivAlarmOutUnitIndex_Type = Integer32
_SwIndivAlarmOutUnitIndex_Object = MibTableColumn
swIndivAlarmOutUnitIndex = _SwIndivAlarmOutUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 16, 1, 1),
    _SwIndivAlarmOutUnitIndex_Type()
)
swIndivAlarmOutUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivAlarmOutUnitIndex.setStatus("current")


class _SwIndivAlarmOutStatus_Type(Integer32):
    """Custom type swIndivAlarmOutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("deactivated", 1))
    )


_SwIndivAlarmOutStatus_Type.__name__ = "Integer32"
_SwIndivAlarmOutStatus_Object = MibTableColumn
swIndivAlarmOutStatus = _SwIndivAlarmOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 16, 1, 2),
    _SwIndivAlarmOutStatus_Type()
)
swIndivAlarmOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivAlarmOutStatus.setStatus("current")


class _SwChassisModel_Type(Integer32):
    """Custom type swChassisModel based on Integer32"""
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
              2000000254,
              2000000255)
        )
    )
    namedValues = NamedValues(
        *(("dmSwitch3000", 1),
          ("dmSwitch4001", 2),
          ("dmSwitch4001L", 3),
          ("dmSwitch4001NewFan", 8),
          ("dmSwitch4001S", 4),
          ("dmSwitch4004", 5),
          ("dmSwitch4008", 6),
          ("dmSwitch4008HighSpeed", 7),
          ("dmSwitch4100", 9),
          ("infNotAvailable", 2000000255),
          ("objectNonexistentInModel", 2000000254))
    )


_SwChassisModel_Type.__name__ = "Integer32"
_SwChassisModel_Object = MibScalar
swChassisModel = _SwChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 17),
    _SwChassisModel_Type()
)
swChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisModel.setStatus("current")
_SwitchSessionTable_Object = MibTable
switchSessionTable = _SwitchSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18)
)
if mibBuilder.loadTexts:
    switchSessionTable.setStatus("current")
_SwitchSessionEntry_Object = MibTableRow
switchSessionEntry = _SwitchSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1)
)
switchSessionEntry.setIndexNames(
    (0, "DMswitch-MIB", "swSessionUnitIndex"),
)
if mibBuilder.loadTexts:
    switchSessionEntry.setStatus("current")
_SwSessionUnitIndex_Type = Integer32
_SwSessionUnitIndex_Object = MibTableColumn
swSessionUnitIndex = _SwSessionUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1, 1),
    _SwSessionUnitIndex_Type()
)
swSessionUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSessionUnitIndex.setStatus("current")


class _SwSessionName_Type(DisplayString):
    """Custom type swSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwSessionName_Type.__name__ = "DisplayString"
_SwSessionName_Object = MibTableColumn
swSessionName = _SwSessionName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1, 2),
    _SwSessionName_Type()
)
swSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSessionName.setStatus("current")


class _SwSessionUptime_Type(DisplayString):
    """Custom type swSessionUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwSessionUptime_Type.__name__ = "DisplayString"
_SwSessionUptime_Object = MibTableColumn
swSessionUptime = _SwSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1, 3),
    _SwSessionUptime_Type()
)
swSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSessionUptime.setStatus("current")
_SwSessionPid_Type = Integer32
_SwSessionPid_Object = MibTableColumn
swSessionPid = _SwSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1, 4),
    _SwSessionPid_Type()
)
swSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSessionPid.setStatus("current")


class _SwSessionSrcIP_Type(DisplayString):
    """Custom type swSessionSrcIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwSessionSrcIP_Type.__name__ = "DisplayString"
_SwSessionSrcIP_Object = MibTableColumn
swSessionSrcIP = _SwSessionSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 1, 18, 1, 5),
    _SwSessionSrcIP_Type()
)
swSessionSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSessionSrcIP.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "DMswitch-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("hundredBaseFX", 3),
          ("hundredBaseFxScMultiMode", 10),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseTX", 2),
          ("other", 1),
          ("tenG", 11),
          ("tenGSfp", 12),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 4),
          ("thousandBaseSfp", 8),
          ("thousandBaseT", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
        *(("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("fullDuplex10000", 8),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("reserved", 1))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 1

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
        *(("backPressure", 3),
          ("disabled", 2),
          ("dot3xFlowControlRx", 5),
          ("dot3xFlowControlRxTx", 4),
          ("dot3xFlowControlTx", 6),
          ("enabled", 1))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Bits):
    """Custom type portCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot3xFlowControlRx", 8),
          ("dot3xFlowControlRxTx", 7),
          ("dot3xFlowControlTx", 9),
          ("portCap10000full", 6),
          ("portCap1000full", 5),
          ("portCap1000half", 4),
          ("portCap100full", 3),
          ("portCap100half", 2),
          ("portCap10full", 1),
          ("portCap10half", 0))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")


class _PortAutonegotiation_Type(Integer32):
    """Custom type portAutonegotiation based on Integer32"""
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


_PortAutonegotiation_Type.__name__ = "Integer32"
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
        *(("down", 9),
          ("error", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("fullDuplex10000", 8),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("backPressure", 2),
          ("disable", 6),
          ("dot3xFlowControlRx", 4),
          ("dot3xFlowControlRxTx", 3),
          ("dot3xFlowControlTx", 5),
          ("error", 1))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")


class _PortMdiStatus_Type(Integer32):
    """Custom type portMdiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("normal", 2),
          ("xover", 3))
    )


_PortMdiStatus_Type.__name__ = "Integer32"
_PortMdiStatus_Object = MibTableColumn
portMdiStatus = _PortMdiStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 10),
    _PortMdiStatus_Type()
)
portMdiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMdiStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 2, 1, 1, 11),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "DMswitch-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3, 1, 2),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkCreation_Type(Integer32):
    """Custom type trunkCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 2),
          ("static", 1))
    )


_TrunkCreation_Type.__name__ = "Integer32"
_TrunkCreation_Object = MibTableColumn
trunkCreation = _TrunkCreation_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "DMswitch-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")


class _LacpPortStatus_Type(Integer32):
    """Custom type lacpPortStatus based on Integer32"""
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


_LacpPortStatus_Type.__name__ = "Integer32"
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""


_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1)
)
staPortEntry.setIndexNames(
    (0, "DMswitch-MIB", "staPortIndex"),
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortIndex_Type = Integer32
_StaPortIndex_Object = MibTableColumn
staPortIndex = _StaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 1),
    _StaPortIndex_Type()
)
staPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPortIndex.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 2),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 3),
    _StaPortOperEdgePort_Type()
)
staPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperEdgePort.setStatus("current")


class _StaPortAdminPointToPoint_Type(Integer32):
    """Custom type staPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_StaPortAdminPointToPoint_Type.__name__ = "Integer32"
_StaPortAdminPointToPoint_Object = MibTableColumn
staPortAdminPointToPoint = _StaPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 4),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 5),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortLongPathCost_Type(Integer32):
    """Custom type staPortLongPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongPathCost_Type.__name__ = "Integer32"
_StaPortLongPathCost_Object = MibTableColumn
staPortLongPathCost = _StaPortLongPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 6),
    _StaPortLongPathCost_Type()
)
staPortLongPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongPathCost.setStatus("current")


class _StaPortSystemStatus_Type(EnabledStatus):
    """Custom type staPortSystemStatus based on EnabledStatus"""


_StaPortSystemStatus_Object = MibTableColumn
staPortSystemStatus = _StaPortSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 2, 1, 7),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaProtocolType_Type(Integer32):
    """Custom type staProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 5, 3),
    _StaProtocolType_Type()
)
staProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staProtocolType.setStatus("current")
_TftpMgt_ObjectIdentity = ObjectIdentity
tftpMgt = _TftpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 6)
)


class _TftpFile_Type(DisplayString):
    """Custom type tftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpFile_Type.__name__ = "DisplayString"
_TftpFile_Object = MibScalar
tftpFile = _TftpFile_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 6, 1),
    _TftpFile_Type()
)
tftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFile.setStatus("current")


class _TftpFlashConfig_Type(Integer32):
    """Custom type tftpFlashConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TftpFlashConfig_Type.__name__ = "Integer32"
_TftpFlashConfig_Object = MibScalar
tftpFlashConfig = _TftpFlashConfig_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 6, 2),
    _TftpFlashConfig_Type()
)
tftpFlashConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFlashConfig.setStatus("current")
_TftpServer_Type = IpAddress
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 6, 3),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
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
        *(("downloadToFirmware", 4),
          ("downloadToFlashConfig", 1),
          ("downloadToRunningConfig", 2),
          ("downloadToStartupConfig", 3),
          ("notDownloading", 8),
          ("uploadFromFlashConfig", 5),
          ("uploadFromRunningConfig", 6),
          ("uploadFromStartupConfig", 7))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 6, 4),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 7)
)


class _RestartFirmware_Type(Integer32):
    """Custom type restartFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RestartFirmware_Type.__name__ = "Integer32"
_RestartFirmware_Object = MibScalar
restartFirmware = _RestartFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 7, 1),
    _RestartFirmware_Type()
)
restartFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartFirmware.setStatus("current")


class _RestartConfig_Type(Integer32):
    """Custom type restartConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RestartConfig_Type.__name__ = "Integer32"
_RestartConfig_Object = MibScalar
restartConfig = _RestartConfig_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 7, 2),
    _RestartConfig_Type()
)
restartConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartConfig.setStatus("current")


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8)
)
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibScalar
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8, 2)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8, 2, 1)
)
mirrorEntry.setIndexNames(
    (0, "DMswitch-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8, 2, 1, 1),
    _MirrorSourcePort_Type()
)
mirrorSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorSourcePort.setStatus("current")


class _MirrorType_Type(Integer32):
    """Custom type mirrorType based on Integer32"""
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
        *(("all", 3),
          ("disable", 4),
          ("rx", 1),
          ("tx", 2))
    )


_MirrorType_Type.__name__ = "Integer32"
_MirrorType_Object = MibTableColumn
mirrorType = _MirrorType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 8, 2, 1, 2),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9)
)


class _IgmpSnoopStatus_Type(Integer32):
    """Custom type igmpSnoopStatus based on Integer32"""
    defaultValue = 1

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


_IgmpSnoopStatus_Type.__name__ = "Integer32"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(Integer32):
    """Custom type igmpSnoopQuerier based on Integer32"""
    defaultValue = 1

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


_IgmpSnoopQuerier_Type.__name__ = "Integer32"
_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 2),
    _IgmpSnoopQuerier_Type()
)
igmpSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQuerier.setStatus("current")


class _IgmpSnoopQueryCount_Type(Integer32):
    """Custom type igmpSnoopQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_IgmpSnoopQueryCount_Type.__name__ = "Integer32"
_IgmpSnoopQueryCount_Object = MibScalar
igmpSnoopQueryCount = _IgmpSnoopQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 3),
    _IgmpSnoopQueryCount_Type()
)
igmpSnoopQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryCount.setStatus("current")


class _IgmpSnoopQueryInterval_Type(Integer32):
    """Custom type igmpSnoopQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_IgmpSnoopQueryInterval_Type.__name__ = "Integer32"
_IgmpSnoopQueryInterval_Object = MibScalar
igmpSnoopQueryInterval = _IgmpSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 4),
    _IgmpSnoopQueryInterval_Type()
)
igmpSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryInterval.setStatus("current")


class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("current")


class _IgmpSnoopQueryTimeout_Type(Integer32):
    """Custom type igmpSnoopQueryTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_IgmpSnoopQueryTimeout_Type.__name__ = "Integer32"
_IgmpSnoopQueryTimeout_Object = MibScalar
igmpSnoopQueryTimeout = _IgmpSnoopQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 6),
    _IgmpSnoopQueryTimeout_Type()
)
igmpSnoopQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryTimeout.setStatus("current")


class _IgmpSnoopVersion_Type(Integer32):
    """Custom type igmpSnoopVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "DMswitch-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "DMswitch-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "DMswitch-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "DMswitch-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "DMswitch-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "DMswitch-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10)
)


class _IpAddressMode_Type(Integer32):
    """Custom type ipAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_IpAddressMode_Type.__name__ = "Integer32"
_IpAddressMode_Object = MibScalar
ipAddressMode = _IpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 1),
    _IpAddressMode_Type()
)
ipAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressMode.setStatus("current")
_IpDefaultGateway_Type = IpAddress
_IpDefaultGateway_Object = MibScalar
ipDefaultGateway = _IpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 2),
    _IpDefaultGateway_Type()
)
ipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGateway.setStatus("current")
_IpPrimaryDnsServer_Type = IpAddress
_IpPrimaryDnsServer_Object = MibScalar
ipPrimaryDnsServer = _IpPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 3),
    _IpPrimaryDnsServer_Type()
)
ipPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPrimaryDnsServer.setStatus("current")
_IpSecondaryDnsServer_Type = IpAddress
_IpSecondaryDnsServer_Object = MibScalar
ipSecondaryDnsServer = _IpSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 4),
    _IpSecondaryDnsServer_Type()
)
ipSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecondaryDnsServer.setStatus("current")


class _IpHttpState_Type(Integer32):
    """Custom type ipHttpState based on Integer32"""
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


_IpHttpState_Type.__name__ = "Integer32"
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 5),
    _IpHttpState_Type()
)
ipHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpState.setStatus("current")


class _IpHttpPort_Type(Integer32):
    """Custom type ipHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpPort_Type.__name__ = "Integer32"
_IpHttpPort_Object = MibScalar
ipHttpPort = _IpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 6),
    _IpHttpPort_Type()
)
ipHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpPort.setStatus("current")


class _IpHttpsState_Type(Integer32):
    """Custom type ipHttpsState based on Integer32"""
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


_IpHttpsState_Type.__name__ = "Integer32"
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 7),
    _IpHttpsState_Type()
)
ipHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsState.setStatus("current")


class _IpHttpsPort_Type(Integer32):
    """Custom type ipHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpsPort_Type.__name__ = "Integer32"
_IpHttpsPort_Object = MibScalar
ipHttpsPort = _IpHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 8),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")


class _IpTelnetState_Type(Integer32):
    """Custom type ipTelnetState based on Integer32"""
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


_IpTelnetState_Type.__name__ = "Integer32"
_IpTelnetState_Object = MibScalar
ipTelnetState = _IpTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 10, 9),
    _IpTelnetState_Type()
)
ipTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTelnetState.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "DMswitch-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")


class _BcastStormStatus_Type(Integer32):
    """Custom type bcastStormStatus based on Integer32"""
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


_BcastStormStatus_Type.__name__ = "Integer32"
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")
_BcastStormPacketRate_Type = Integer32
_BcastStormPacketRate_Object = MibTableColumn
bcastStormPacketRate = _BcastStormPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 11, 1, 1, 3),
    _BcastStormPacketRate_Type()
)
bcastStormPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPacketRate.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "DMswitch-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanAddressMethod_Type(Integer32):
    """Custom type vlanAddressMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("user", 1))
    )


_VlanAddressMethod_Type.__name__ = "Integer32"
_VlanAddressMethod_Object = MibTableColumn
vlanAddressMethod = _VlanAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13)
)
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13, 1)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13, 1, 1)
)
prioWrrEntry.setIndexNames(
    (0, "DMswitch-MIB", "prioWrrTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrEntry.setStatus("current")


class _PrioWrrTrafficClass_Type(Integer32):
    """Custom type prioWrrTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrTrafficClass_Type.__name__ = "Integer32"
_PrioWrrTrafficClass_Object = MibTableColumn
prioWrrTrafficClass = _PrioWrrTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13, 1, 1, 1),
    _PrioWrrTrafficClass_Type()
)
prioWrrTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrTrafficClass.setStatus("current")


class _PrioWrrWeight_Type(Integer32):
    """Custom type prioWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PrioWrrWeight_Type.__name__ = "Integer32"
_PrioWrrWeight_Object = MibTableColumn
prioWrrWeight = _PrioWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13, 1, 1, 2),
    _PrioWrrWeight_Type()
)
prioWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrWeight.setStatus("current")


class _PrioQueueMode_Type(Integer32):
    """Custom type prioQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 2),
          ("wrr", 1))
    )


_PrioQueueMode_Type.__name__ = "Integer32"
_PrioQueueMode_Object = MibScalar
prioQueueMode = _PrioQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 13, 2),
    _PrioQueueMode_Type()
)
prioQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueMode.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "DMswitch-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("current")


class _TrapDestCommunity_Type(OctetString):
    """Custom type trapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrapDestCommunity_Type.__name__ = "OctetString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")


class _TrapDestStatus_Type(Integer32):
    """Custom type trapDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrapDestStatus_Type.__name__ = "Integer32"
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1, 1, 3),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("current")


class _TrapDestVersion_Type(Integer32):
    """Custom type trapDestVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TrapDestVersion_Type.__name__ = "Integer32"
_TrapDestVersion_Object = MibTableColumn
trapDestVersion = _TrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 1, 1, 4),
    _TrapDestVersion_Type()
)
trapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestVersion.setStatus("current")
_TrapVar_ObjectIdentity = ObjectIdentity
trapVar = _TrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2)
)


class _TrapForbiddenAccessMode_Type(Integer32):
    """Custom type trapForbiddenAccessMode based on Integer32"""
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
        *(("snmp", 2),
          ("ssh", 4),
          ("telnet", 3),
          ("web", 1))
    )


_TrapForbiddenAccessMode_Type.__name__ = "Integer32"
_TrapForbiddenAccessMode_Object = MibScalar
trapForbiddenAccessMode = _TrapForbiddenAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 1),
    _TrapForbiddenAccessMode_Type()
)
trapForbiddenAccessMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapForbiddenAccessMode.setStatus("current")
_TrapForbiddenAccessIp_Type = Integer32
_TrapForbiddenAccessIp_Object = MibScalar
trapForbiddenAccessIp = _TrapForbiddenAccessIp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 2),
    _TrapForbiddenAccessIp_Type()
)
trapForbiddenAccessIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapForbiddenAccessIp.setStatus("current")
_TrapLoginUserName_Type = DisplayString
_TrapLoginUserName_Object = MibScalar
trapLoginUserName = _TrapLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 3),
    _TrapLoginUserName_Type()
)
trapLoginUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapLoginUserName.setStatus("current")
_TrapConfigSavePartition_Type = Integer32
_TrapConfigSavePartition_Object = MibScalar
trapConfigSavePartition = _TrapConfigSavePartition_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 4),
    _TrapConfigSavePartition_Type()
)
trapConfigSavePartition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapConfigSavePartition.setStatus("current")


class _TrapSfpPresenceStatus_Type(Integer32):
    """Custom type trapSfpPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absentee", 1),
          ("present", 2))
    )


_TrapSfpPresenceStatus_Type.__name__ = "Integer32"
_TrapSfpPresenceStatus_Object = MibScalar
trapSfpPresenceStatus = _TrapSfpPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 5),
    _TrapSfpPresenceStatus_Type()
)
trapSfpPresenceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSfpPresenceStatus.setStatus("current")


class _TrapInfAlarmVal_Type(Integer32):
    """Custom type trapInfAlarmVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("deactivated", 1),
          ("unstable", 3))
    )


_TrapInfAlarmVal_Type.__name__ = "Integer32"
_TrapInfAlarmVal_Object = MibScalar
trapInfAlarmVal = _TrapInfAlarmVal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 6),
    _TrapInfAlarmVal_Type()
)
trapInfAlarmVal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapInfAlarmVal.setStatus("current")
_TrapDuplicatedIpVlan_Type = Integer32
_TrapDuplicatedIpVlan_Object = MibScalar
trapDuplicatedIpVlan = _TrapDuplicatedIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 7),
    _TrapDuplicatedIpVlan_Type()
)
trapDuplicatedIpVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDuplicatedIpVlan.setStatus("current")
_TrapDuplicatedIpAddress_Type = Integer32
_TrapDuplicatedIpAddress_Object = MibScalar
trapDuplicatedIpAddress = _TrapDuplicatedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 8),
    _TrapDuplicatedIpAddress_Type()
)
trapDuplicatedIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDuplicatedIpAddress.setStatus("current")
_TrapDuplicatedIpMacAddress_Type = MacAddress
_TrapDuplicatedIpMacAddress_Object = MibScalar
trapDuplicatedIpMacAddress = _TrapDuplicatedIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 9),
    _TrapDuplicatedIpMacAddress_Type()
)
trapDuplicatedIpMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDuplicatedIpMacAddress.setStatus("current")
_TrapEapsDomainName_Type = DisplayString
_TrapEapsDomainName_Object = MibScalar
trapEapsDomainName = _TrapEapsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 10),
    _TrapEapsDomainName_Type()
)
trapEapsDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapEapsDomainName.setStatus("current")
_TrapEapsDomainId_Type = Integer32
_TrapEapsDomainId_Object = MibScalar
trapEapsDomainId = _TrapEapsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 11),
    _TrapEapsDomainId_Type()
)
trapEapsDomainId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapEapsDomainId.setStatus("current")


class _TrapEapsStatus_Type(Integer32):
    """Custom type trapEapsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("links-down", 4),
          ("links-up", 3),
          ("pre-forwarding", 5))
    )


_TrapEapsStatus_Type.__name__ = "Integer32"
_TrapEapsStatus_Object = MibScalar
trapEapsStatus = _TrapEapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 12),
    _TrapEapsStatus_Type()
)
trapEapsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapEapsStatus.setStatus("current")
_TrapTemperature_Type = Integer32
_TrapTemperature_Object = MibScalar
trapTemperature = _TrapTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 13),
    _TrapTemperature_Type()
)
trapTemperature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTemperature.setStatus("current")
_TrapFuseId_Type = Integer32
_TrapFuseId_Object = MibScalar
trapFuseId = _TrapFuseId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 14),
    _TrapFuseId_Type()
)
trapFuseId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapFuseId.setStatus("current")


class _TrapFuseStatus_Type(Integer32):
    """Custom type trapFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("normal", 1))
    )


_TrapFuseStatus_Type.__name__ = "Integer32"
_TrapFuseStatus_Object = MibScalar
trapFuseStatus = _TrapFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 15),
    _TrapFuseStatus_Type()
)
trapFuseStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapFuseStatus.setStatus("current")


class _TrapFansBoardPresenceStatus_Type(Integer32):
    """Custom type trapFansBoardPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absentee", 1),
          ("present", 2))
    )


_TrapFansBoardPresenceStatus_Type.__name__ = "Integer32"
_TrapFansBoardPresenceStatus_Object = MibScalar
trapFansBoardPresenceStatus = _TrapFansBoardPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 16),
    _TrapFansBoardPresenceStatus_Type()
)
trapFansBoardPresenceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapFansBoardPresenceStatus.setStatus("current")


class _TrapStandbyMpuPresenceStatus_Type(Integer32):
    """Custom type trapStandbyMpuPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absentee", 1),
          ("present", 2))
    )


_TrapStandbyMpuPresenceStatus_Type.__name__ = "Integer32"
_TrapStandbyMpuPresenceStatus_Object = MibScalar
trapStandbyMpuPresenceStatus = _TrapStandbyMpuPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 17),
    _TrapStandbyMpuPresenceStatus_Type()
)
trapStandbyMpuPresenceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapStandbyMpuPresenceStatus.setStatus("current")
_TrapMacAddressMove_Type = MacAddress
_TrapMacAddressMove_Object = MibScalar
trapMacAddressMove = _TrapMacAddressMove_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 18),
    _TrapMacAddressMove_Type()
)
trapMacAddressMove.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMacAddressMove.setStatus("current")
_TrapMemFree_Type = Integer32
_TrapMemFree_Object = MibScalar
trapMemFree = _TrapMemFree_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 19),
    _TrapMemFree_Type()
)
trapMemFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMemFree.setStatus("current")
_TrapBootloaderNew_Type = DisplayString
_TrapBootloaderNew_Object = MibScalar
trapBootloaderNew = _TrapBootloaderNew_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 20),
    _TrapBootloaderNew_Type()
)
trapBootloaderNew.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapBootloaderNew.setStatus("current")
_TrapDevNo_Type = Integer32
_TrapDevNo_Object = MibScalar
trapDevNo = _TrapDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 21),
    _TrapDevNo_Type()
)
trapDevNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDevNo.setStatus("current")
_TrapDevLocalId_Type = Integer32
_TrapDevLocalId_Object = MibScalar
trapDevLocalId = _TrapDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 22),
    _TrapDevLocalId_Type()
)
trapDevLocalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDevLocalId.setStatus("current")


class _TrapCesopTdmStatus_Type(Integer32):
    """Custom type trapCesopTdmStatus based on Integer32"""
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
        *(("ais", 2),
          ("lof", 3),
          ("los", 1),
          ("ok", 0))
    )


_TrapCesopTdmStatus_Type.__name__ = "Integer32"
_TrapCesopTdmStatus_Object = MibScalar
trapCesopTdmStatus = _TrapCesopTdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 23),
    _TrapCesopTdmStatus_Type()
)
trapCesopTdmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopTdmStatus.setStatus("current")


class _TrapCesopTdmRemoteStatus_Type(Integer32):
    """Custom type trapCesopTdmRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("ralm", 5))
    )


_TrapCesopTdmRemoteStatus_Type.__name__ = "Integer32"
_TrapCesopTdmRemoteStatus_Object = MibScalar
trapCesopTdmRemoteStatus = _TrapCesopTdmRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 24),
    _TrapCesopTdmRemoteStatus_Type()
)
trapCesopTdmRemoteStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopTdmRemoteStatus.setStatus("current")


class _TrapCesopTdmCasStatus_Type(Integer32):
    """Custom type trapCesopTdmCasStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lom", 4),
          ("ok", 0))
    )


_TrapCesopTdmCasStatus_Type.__name__ = "Integer32"
_TrapCesopTdmCasStatus_Object = MibScalar
trapCesopTdmCasStatus = _TrapCesopTdmCasStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 25),
    _TrapCesopTdmCasStatus_Type()
)
trapCesopTdmCasStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopTdmCasStatus.setStatus("current")


class _TrapCesopTdmCrcStatus_Type(Integer32):
    """Custom type trapCesopTdmCrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6)
        )
    )
    namedValues = NamedValues(
        *(("crc", 6),
          ("ok", 0))
    )


_TrapCesopTdmCrcStatus_Type.__name__ = "Integer32"
_TrapCesopTdmCrcStatus_Object = MibScalar
trapCesopTdmCrcStatus = _TrapCesopTdmCrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 26),
    _TrapCesopTdmCrcStatus_Type()
)
trapCesopTdmCrcStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopTdmCrcStatus.setStatus("current")


class _TrapCesopBundleLocalTdmStatus_Type(Integer32):
    """Custom type trapCesopBundleLocalTdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 0),
          ("rdi", 2))
    )


_TrapCesopBundleLocalTdmStatus_Type.__name__ = "Integer32"
_TrapCesopBundleLocalTdmStatus_Object = MibScalar
trapCesopBundleLocalTdmStatus = _TrapCesopBundleLocalTdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 27),
    _TrapCesopBundleLocalTdmStatus_Type()
)
trapCesopBundleLocalTdmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundleLocalTdmStatus.setStatus("current")


class _TrapCesopBundleRemoteTdmStatus_Type(Integer32):
    """Custom type trapCesopBundleRemoteTdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 0),
          ("rdi", 2))
    )


_TrapCesopBundleRemoteTdmStatus_Type.__name__ = "Integer32"
_TrapCesopBundleRemoteTdmStatus_Object = MibScalar
trapCesopBundleRemoteTdmStatus = _TrapCesopBundleRemoteTdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 28),
    _TrapCesopBundleRemoteTdmStatus_Type()
)
trapCesopBundleRemoteTdmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundleRemoteTdmStatus.setStatus("current")


class _TrapCesopBundleLocalStatus_Type(Integer32):
    """Custom type trapCesopBundleLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 0))
    )


_TrapCesopBundleLocalStatus_Type.__name__ = "Integer32"
_TrapCesopBundleLocalStatus_Object = MibScalar
trapCesopBundleLocalStatus = _TrapCesopBundleLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 29),
    _TrapCesopBundleLocalStatus_Type()
)
trapCesopBundleLocalStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundleLocalStatus.setStatus("current")


class _TrapCesopBundleRemoteStatus_Type(Integer32):
    """Custom type trapCesopBundleRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 0))
    )


_TrapCesopBundleRemoteStatus_Type.__name__ = "Integer32"
_TrapCesopBundleRemoteStatus_Object = MibScalar
trapCesopBundleRemoteStatus = _TrapCesopBundleRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 30),
    _TrapCesopBundleRemoteStatus_Type()
)
trapCesopBundleRemoteStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundleRemoteStatus.setStatus("current")


class _TrapCesopBundlePktMismatchStatus_Type(Integer32):
    """Custom type trapCesopBundlePktMismatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 3),
          ("ok", 0))
    )


_TrapCesopBundlePktMismatchStatus_Type.__name__ = "Integer32"
_TrapCesopBundlePktMismatchStatus_Object = MibScalar
trapCesopBundlePktMismatchStatus = _TrapCesopBundlePktMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 31),
    _TrapCesopBundlePktMismatchStatus_Type()
)
trapCesopBundlePktMismatchStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundlePktMismatchStatus.setStatus("current")


class _TrapCesopBundleNextHopStatus_Type(Integer32):
    """Custom type trapCesopBundleNextHopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("up", 0))
    )


_TrapCesopBundleNextHopStatus_Type.__name__ = "Integer32"
_TrapCesopBundleNextHopStatus_Object = MibScalar
trapCesopBundleNextHopStatus = _TrapCesopBundleNextHopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 32),
    _TrapCesopBundleNextHopStatus_Type()
)
trapCesopBundleNextHopStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopBundleNextHopStatus.setStatus("current")
_TrapCesopClockAdapLinkQuality_Type = Integer32
_TrapCesopClockAdapLinkQuality_Object = MibScalar
trapCesopClockAdapLinkQuality = _TrapCesopClockAdapLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 33),
    _TrapCesopClockAdapLinkQuality_Type()
)
trapCesopClockAdapLinkQuality.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopClockAdapLinkQuality.setStatus("current")


class _TrapCesopClockSourceStatus_Type(Integer32):
    """Custom type trapCesopClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("out-of-limits", 1))
    )


_TrapCesopClockSourceStatus_Type.__name__ = "Integer32"
_TrapCesopClockSourceStatus_Object = MibScalar
trapCesopClockSourceStatus = _TrapCesopClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 34),
    _TrapCesopClockSourceStatus_Type()
)
trapCesopClockSourceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopClockSourceStatus.setStatus("current")


class _TrapBroadcastStormControlStatus_Type(Integer32):
    """Custom type trapBroadcastStormControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("out-of-limits", 2))
    )


_TrapBroadcastStormControlStatus_Type.__name__ = "Integer32"
_TrapBroadcastStormControlStatus_Object = MibScalar
trapBroadcastStormControlStatus = _TrapBroadcastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 35),
    _TrapBroadcastStormControlStatus_Type()
)
trapBroadcastStormControlStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapBroadcastStormControlStatus.setStatus("current")
_TrapBroadcastStormControlPPS_Type = Integer32
_TrapBroadcastStormControlPPS_Object = MibScalar
trapBroadcastStormControlPPS = _TrapBroadcastStormControlPPS_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 36),
    _TrapBroadcastStormControlPPS_Type()
)
trapBroadcastStormControlPPS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapBroadcastStormControlPPS.setStatus("current")


class _TrapMulticastStormControlStatus_Type(Integer32):
    """Custom type trapMulticastStormControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("out-of-limits", 2))
    )


_TrapMulticastStormControlStatus_Type.__name__ = "Integer32"
_TrapMulticastStormControlStatus_Object = MibScalar
trapMulticastStormControlStatus = _TrapMulticastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 37),
    _TrapMulticastStormControlStatus_Type()
)
trapMulticastStormControlStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMulticastStormControlStatus.setStatus("current")
_TrapMulticastStormControlPPS_Type = Integer32
_TrapMulticastStormControlPPS_Object = MibScalar
trapMulticastStormControlPPS = _TrapMulticastStormControlPPS_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 38),
    _TrapMulticastStormControlPPS_Type()
)
trapMulticastStormControlPPS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMulticastStormControlPPS.setStatus("current")


class _TrapStatusLDP_Type(Integer32):
    """Custom type trapStatusLDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("down", 2),
          ("up", 1))
    )


_TrapStatusLDP_Type.__name__ = "Integer32"
_TrapStatusLDP_Object = MibScalar
trapStatusLDP = _TrapStatusLDP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 39),
    _TrapStatusLDP_Type()
)
trapStatusLDP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapStatusLDP.setStatus("current")
_TrapIdLDP_Type = Integer32
_TrapIdLDP_Object = MibScalar
trapIdLDP = _TrapIdLDP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 40),
    _TrapIdLDP_Type()
)
trapIdLDP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIdLDP.setStatus("current")


class _TrapStatusTunnelRSVP_Type(Integer32):
    """Custom type trapStatusTunnelRSVP based on Integer32"""
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
        *(("deleted", 3),
          ("down", 2),
          ("rerouted", 4),
          ("up", 1))
    )


_TrapStatusTunnelRSVP_Type.__name__ = "Integer32"
_TrapStatusTunnelRSVP_Object = MibScalar
trapStatusTunnelRSVP = _TrapStatusTunnelRSVP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 41),
    _TrapStatusTunnelRSVP_Type()
)
trapStatusTunnelRSVP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapStatusTunnelRSVP.setStatus("current")
_TrapIdTunnelRSVP_Type = Integer32
_TrapIdTunnelRSVP_Object = MibScalar
trapIdTunnelRSVP = _TrapIdTunnelRSVP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 42),
    _TrapIdTunnelRSVP_Type()
)
trapIdTunnelRSVP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIdTunnelRSVP.setStatus("current")


class _TrapPanelStatus_Type(Integer32):
    """Custom type trapPanelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_TrapPanelStatus_Type.__name__ = "Integer32"
_TrapPanelStatus_Object = MibScalar
trapPanelStatus = _TrapPanelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 43),
    _TrapPanelStatus_Type()
)
trapPanelStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapPanelStatus.setStatus("current")
_TrapLSTGroup_Type = Integer32
_TrapLSTGroup_Object = MibScalar
trapLSTGroup = _TrapLSTGroup_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 44),
    _TrapLSTGroup_Type()
)
trapLSTGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapLSTGroup.setStatus("current")
_TrapMemL3Free_Type = Integer32
_TrapMemL3Free_Object = MibScalar
trapMemL3Free = _TrapMemL3Free_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 45),
    _TrapMemL3Free_Type()
)
trapMemL3Free.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMemL3Free.setStatus("current")
_TrapActiveMpuNsfId_Type = Integer32
_TrapActiveMpuNsfId_Object = MibScalar
trapActiveMpuNsfId = _TrapActiveMpuNsfId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 46),
    _TrapActiveMpuNsfId_Type()
)
trapActiveMpuNsfId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapActiveMpuNsfId.setStatus("current")
_TrapStandByMpuNsfId_Type = Integer32
_TrapStandByMpuNsfId_Object = MibScalar
trapStandByMpuNsfId = _TrapStandByMpuNsfId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 47),
    _TrapStandByMpuNsfId_Type()
)
trapStandByMpuNsfId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapStandByMpuNsfId.setStatus("current")
_TrapErpsDomainName_Type = DisplayString
_TrapErpsDomainName_Object = MibScalar
trapErpsDomainName = _TrapErpsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 48),
    _TrapErpsDomainName_Type()
)
trapErpsDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapErpsDomainName.setStatus("current")
_TrapErpsDomainId_Type = Integer32
_TrapErpsDomainId_Object = MibScalar
trapErpsDomainId = _TrapErpsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 49),
    _TrapErpsDomainId_Type()
)
trapErpsDomainId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapErpsDomainId.setStatus("current")


class _TrapErpsStatus_Type(Integer32):
    """Custom type trapErpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("init", 1),
          ("protection", 3))
    )


_TrapErpsStatus_Type.__name__ = "Integer32"
_TrapErpsStatus_Object = MibScalar
trapErpsStatus = _TrapErpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 50),
    _TrapErpsStatus_Type()
)
trapErpsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapErpsStatus.setStatus("current")


class _TrapCfmMdName_Type(DisplayString):
    """Custom type trapCfmMdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_TrapCfmMdName_Type.__name__ = "DisplayString"
_TrapCfmMdName_Object = MibScalar
trapCfmMdName = _TrapCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 51),
    _TrapCfmMdName_Type()
)
trapCfmMdName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCfmMdName.setStatus("current")


class _TrapCfmMaName_Type(DisplayString):
    """Custom type trapCfmMaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_TrapCfmMaName_Type.__name__ = "DisplayString"
_TrapCfmMaName_Object = MibScalar
trapCfmMaName = _TrapCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 52),
    _TrapCfmMaName_Type()
)
trapCfmMaName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCfmMaName.setStatus("current")


class _TrapCfmMepId_Type(Integer32):
    """Custom type trapCfmMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_TrapCfmMepId_Type.__name__ = "Integer32"
_TrapCfmMepId_Object = MibScalar
trapCfmMepId = _TrapCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 53),
    _TrapCfmMepId_Type()
)
trapCfmMepId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCfmMepId.setStatus("current")


class _TrapCfmVlan_Type(Integer32):
    """Custom type trapCfmVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TrapCfmVlan_Type.__name__ = "Integer32"
_TrapCfmVlan_Object = MibScalar
trapCfmVlan = _TrapCfmVlan_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 54),
    _TrapCfmVlan_Type()
)
trapCfmVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCfmVlan.setStatus("current")


class _TrapCfmDefect_Type(Integer32):
    """Custom type trapCfmDefect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("defErrorCCM", 4),
          ("defMACstatus", 2),
          ("defNone", 0),
          ("defRDICCM", 1),
          ("defRemoteCCM", 3),
          ("defXconCCM", 5))
    )


_TrapCfmDefect_Type.__name__ = "Integer32"
_TrapCfmDefect_Object = MibScalar
trapCfmDefect = _TrapCfmDefect_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 55),
    _TrapCfmDefect_Type()
)
trapCfmDefect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCfmDefect.setStatus("current")
_TrapEvcName_Type = DisplayString
_TrapEvcName_Object = MibScalar
trapEvcName = _TrapEvcName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 56),
    _TrapEvcName_Type()
)
trapEvcName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapEvcName.setStatus("current")


class _TrapEvcStatus_Type(Integer32):
    """Custom type trapEvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("newAndActive", 3),
          ("newAndNotActive", 1),
          ("newAndPartiallyActive", 5),
          ("notActive", 0),
          ("partiallyActive", 4))
    )


_TrapEvcStatus_Type.__name__ = "Integer32"
_TrapEvcStatus_Object = MibScalar
trapEvcStatus = _TrapEvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 57),
    _TrapEvcStatus_Type()
)
trapEvcStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapEvcStatus.setStatus("current")


class _TrapSyncSystemClockStatus_Type(Integer32):
    """Custom type trapSyncSystemClockStatus based on Integer32"""
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
        *(("acquiring", 3),
          ("freerun", 1),
          ("holdover", 2),
          ("locked", 4))
    )


_TrapSyncSystemClockStatus_Type.__name__ = "Integer32"
_TrapSyncSystemClockStatus_Object = MibScalar
trapSyncSystemClockStatus = _TrapSyncSystemClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 58),
    _TrapSyncSystemClockStatus_Type()
)
trapSyncSystemClockStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSyncSystemClockStatus.setStatus("current")


class _TrapCesopG704ClockSourceStatus_Type(Integer32):
    """Custom type trapCesopG704ClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dontcare", 7),
          ("fail", 10),
          ("locked", 9))
    )


_TrapCesopG704ClockSourceStatus_Type.__name__ = "Integer32"
_TrapCesopG704ClockSourceStatus_Object = MibScalar
trapCesopG704ClockSourceStatus = _TrapCesopG704ClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 59),
    _TrapCesopG704ClockSourceStatus_Type()
)
trapCesopG704ClockSourceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapCesopG704ClockSourceStatus.setStatus("current")


class _TrapSystemWarningsUnits_Type(Integer32):
    """Custom type trapSystemWarningsUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sysWarUnitsCommFail", 5),
          ("sysWarUnitsHsEnNoError", 1),
          ("sysWarUnitsHsEnWDifMod", 4),
          ("sysWarUnitsHsEnWES", 2),
          ("sysWarUnitsHsEnWHSDis", 3),
          ("sysWarUnitsL3", 7),
          ("sysWarUnitsMPLS", 6))
    )


_TrapSystemWarningsUnits_Type.__name__ = "Integer32"
_TrapSystemWarningsUnits_Object = MibScalar
trapSystemWarningsUnits = _TrapSystemWarningsUnits_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 60),
    _TrapSystemWarningsUnits_Type()
)
trapSystemWarningsUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSystemWarningsUnits.setStatus("current")


class _TrapSensorGroup_Type(Integer32):
    """Custom type trapSensorGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boardSensors", 1),
          ("chipsetSensors", 2))
    )


_TrapSensorGroup_Type.__name__ = "Integer32"
_TrapSensorGroup_Object = MibScalar
trapSensorGroup = _TrapSensorGroup_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 14, 2, 61),
    _TrapSensorGroup_Type()
)
trapSensorGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSensorGroup.setStatus("current")
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "DMswitch-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")


class _RlPortInputStatus_Type(Integer32):
    """Custom type rlPortInputStatus based on Integer32"""
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


_RlPortInputStatus_Type.__name__ = "Integer32"
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 2),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")


class _RlPortOutputStatus_Type(Integer32):
    """Custom type rlPortOutputStatus based on Integer32"""
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


_RlPortOutputStatus_Type.__name__ = "Integer32"
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 3),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")


class _RlPortInputRate_Type(Integer32):
    """Custom type rlPortInputRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_RlPortInputRate_Type.__name__ = "Integer32"
_RlPortInputRate_Object = MibTableColumn
rlPortInputRate = _RlPortInputRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 4),
    _RlPortInputRate_Type()
)
rlPortInputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputRate.setStatus("current")


class _RlPortInputBurst_Type(Integer32):
    """Custom type rlPortInputBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4096),
    )


_RlPortInputBurst_Type.__name__ = "Integer32"
_RlPortInputBurst_Object = MibTableColumn
rlPortInputBurst = _RlPortInputBurst_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 5),
    _RlPortInputBurst_Type()
)
rlPortInputBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputBurst.setStatus("current")


class _RlPortOutputRate_Type(Integer32):
    """Custom type rlPortOutputRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_RlPortOutputRate_Type.__name__ = "Integer32"
_RlPortOutputRate_Object = MibTableColumn
rlPortOutputRate = _RlPortOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 6),
    _RlPortOutputRate_Type()
)
rlPortOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputRate.setStatus("current")


class _RlPortOutputBurst_Type(Integer32):
    """Custom type rlPortOutputBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4096),
    )


_RlPortOutputBurst_Type.__name__ = "Integer32"
_RlPortOutputBurst_Object = MibTableColumn
rlPortOutputBurst = _RlPortOutputBurst_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 16, 1, 1, 7),
    _RlPortOutputBurst_Type()
)
rlPortOutputBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputBurst.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17)
)
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1)
)


class _RadiusServerPortNumber_Type(Integer32):
    """Custom type radiusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPortNumber_Type.__name__ = "Integer32"
_RadiusServerPortNumber_Object = MibScalar
radiusServerPortNumber = _RadiusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 2),
    _RadiusServerPortNumber_Type()
)
radiusServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPortNumber.setStatus("current")
_RadiusServerKey_Type = DisplayString
_RadiusServerKey_Object = MibScalar
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 3),
    _RadiusServerKey_Type()
)
radiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerKey.setStatus("current")


class _RadiusServerRetransmit_Type(Integer32):
    """Custom type radiusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerRetransmit_Type.__name__ = "Integer32"
_RadiusServerRetransmit_Object = MibScalar
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 4),
    _RadiusServerRetransmit_Type()
)
radiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerRetransmit.setStatus("current")


class _RadiusServerTimeout_Type(Integer32):
    """Custom type radiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerTimeout_Type.__name__ = "Integer32"
_RadiusServerTimeout_Object = MibScalar
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 5),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_RadiusMultipleServerTable_Object = MibTable
radiusMultipleServerTable = _RadiusMultipleServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7)
)
if mibBuilder.loadTexts:
    radiusMultipleServerTable.setStatus("current")
_RadiusMultipleServerEntry_Object = MibTableRow
radiusMultipleServerEntry = _RadiusMultipleServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1)
)
radiusMultipleServerEntry.setIndexNames(
    (0, "DMswitch-MIB", "radiusMultipleServerIndex"),
)
if mibBuilder.loadTexts:
    radiusMultipleServerEntry.setStatus("current")
_RadiusMultipleServerIndex_Type = Integer32
_RadiusMultipleServerIndex_Object = MibTableColumn
radiusMultipleServerIndex = _RadiusMultipleServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 1),
    _RadiusMultipleServerIndex_Type()
)
radiusMultipleServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusMultipleServerIndex.setStatus("current")
_RadiusMultipleServerAddress_Type = IpAddress
_RadiusMultipleServerAddress_Object = MibTableColumn
radiusMultipleServerAddress = _RadiusMultipleServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 2),
    _RadiusMultipleServerAddress_Type()
)
radiusMultipleServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerAddress.setStatus("current")


class _RadiusMultipleServerPortNumber_Type(Integer32):
    """Custom type radiusMultipleServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusMultipleServerPortNumber_Type.__name__ = "Integer32"
_RadiusMultipleServerPortNumber_Object = MibTableColumn
radiusMultipleServerPortNumber = _RadiusMultipleServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 3),
    _RadiusMultipleServerPortNumber_Type()
)
radiusMultipleServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerPortNumber.setStatus("current")
_RadiusMultipleServerKey_Type = DisplayString
_RadiusMultipleServerKey_Object = MibTableColumn
radiusMultipleServerKey = _RadiusMultipleServerKey_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 4),
    _RadiusMultipleServerKey_Type()
)
radiusMultipleServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMultipleServerKey.setStatus("current")


class _RadiusMultipleServerRetransmit_Type(Integer32):
    """Custom type radiusMultipleServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusMultipleServerRetransmit_Type.__name__ = "Integer32"
_RadiusMultipleServerRetransmit_Object = MibTableColumn
radiusMultipleServerRetransmit = _RadiusMultipleServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 5),
    _RadiusMultipleServerRetransmit_Type()
)
radiusMultipleServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMultipleServerRetransmit.setStatus("current")


class _RadiusMultipleServerTimeout_Type(Integer32):
    """Custom type radiusMultipleServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusMultipleServerTimeout_Type.__name__ = "Integer32"
_RadiusMultipleServerTimeout_Object = MibTableColumn
radiusMultipleServerTimeout = _RadiusMultipleServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 6),
    _RadiusMultipleServerTimeout_Type()
)
radiusMultipleServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMultipleServerTimeout.setStatus("current")
_RadiusMultipleServerStatus_Type = ValidStatus
_RadiusMultipleServerStatus_Object = MibTableColumn
radiusMultipleServerStatus = _RadiusMultipleServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 1, 7, 1, 8),
    _RadiusMultipleServerStatus_Type()
)
radiusMultipleServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerStatus.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 3),
    _SshServerMinorVersion_Type()
)
sshServerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMinorVersion.setStatus("current")


class _SshTimeout_Type(Integer32):
    """Custom type sshTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SshTimeout_Type.__name__ = "Integer32"
_SshTimeout_Object = MibScalar
sshTimeout = _SshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshTimeout.setUnits("seconds")


class _SshKeySize_Type(Integer32):
    """Custom type sshKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 896),
    )


_SshKeySize_Type.__name__ = "Integer32"
_SshKeySize_Object = MibScalar
sshKeySize = _SshKeySize_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 5),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey_Type = KeySegment
_SshRsaHostKey_Object = MibScalar
sshRsaHostKey = _SshRsaHostKey_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 6),
    _SshRsaHostKey_Type()
)
sshRsaHostKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey.setStatus("current")
_SshDsaHostKey_Type = KeySegment
_SshDsaHostKey_Object = MibScalar
sshDsaHostKey = _SshDsaHostKey_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 7),
    _SshDsaHostKey_Type()
)
sshDsaHostKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey.setStatus("current")


class _SshHostKeyGenAction_Type(Integer32):
    """Custom type sshHostKeyGenAction based on Integer32"""
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
        *(("genBothKeys", 4),
          ("genDsaKey", 3),
          ("genRsaKey", 2),
          ("noGen", 1))
    )


_SshHostKeyGenAction_Type.__name__ = "Integer32"
_SshHostKeyGenAction_Object = MibScalar
sshHostKeyGenAction = _SshHostKeyGenAction_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 8),
    _SshHostKeyGenAction_Type()
)
sshHostKeyGenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyGenAction.setStatus("current")


class _SshHostKeyDelAction_Type(Integer32):
    """Custom type sshHostKeyDelAction based on Integer32"""
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
        *(("delBothKeys", 4),
          ("delDsaKey", 3),
          ("delRsaKey", 2),
          ("noDel", 1))
    )


_SshHostKeyDelAction_Type.__name__ = "Integer32"
_SshHostKeyDelAction_Object = MibScalar
sshHostKeyDelAction = _SshHostKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 2, 9),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3)
)
_IpFilterSnmpTable_Object = MibTable
ipFilterSnmpTable = _IpFilterSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    ipFilterSnmpTable.setStatus("current")
_IpFilterSnmpEntry_Object = MibTableRow
ipFilterSnmpEntry = _IpFilterSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 1, 1)
)
ipFilterSnmpEntry.setIndexNames(
    (0, "DMswitch-MIB", "ipFilterSnmpAddress"),
    (0, "DMswitch-MIB", "ipFilterSnmpMask"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpEntry.setStatus("current")
_IpFilterSnmpAddress_Type = IpAddress
_IpFilterSnmpAddress_Object = MibTableColumn
ipFilterSnmpAddress = _IpFilterSnmpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 1, 1, 1),
    _IpFilterSnmpAddress_Type()
)
ipFilterSnmpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpAddress.setStatus("current")
_IpFilterSnmpMask_Type = IpAddress
_IpFilterSnmpMask_Object = MibTableColumn
ipFilterSnmpMask = _IpFilterSnmpMask_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 1, 1, 2),
    _IpFilterSnmpMask_Type()
)
ipFilterSnmpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpMask.setStatus("current")
_IpFilterSnmpStatus_Type = ValidStatus
_IpFilterSnmpStatus_Object = MibTableColumn
ipFilterSnmpStatus = _IpFilterSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 1, 1, 3),
    _IpFilterSnmpStatus_Type()
)
ipFilterSnmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpStatus.setStatus("current")
_IpFilterHTTPTable_Object = MibTable
ipFilterHTTPTable = _IpFilterHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 2)
)
if mibBuilder.loadTexts:
    ipFilterHTTPTable.setStatus("current")
_IpFilterHTTPEntry_Object = MibTableRow
ipFilterHTTPEntry = _IpFilterHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 2, 1)
)
ipFilterHTTPEntry.setIndexNames(
    (0, "DMswitch-MIB", "ipFilterHTTPAddress"),
    (0, "DMswitch-MIB", "ipFilterHTTPMask"),
)
if mibBuilder.loadTexts:
    ipFilterHTTPEntry.setStatus("current")
_IpFilterHTTPAddress_Type = IpAddress
_IpFilterHTTPAddress_Object = MibTableColumn
ipFilterHTTPAddress = _IpFilterHTTPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 2, 1, 1),
    _IpFilterHTTPAddress_Type()
)
ipFilterHTTPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPAddress.setStatus("current")
_IpFilterHTTPMask_Type = IpAddress
_IpFilterHTTPMask_Object = MibTableColumn
ipFilterHTTPMask = _IpFilterHTTPMask_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 2, 1, 2),
    _IpFilterHTTPMask_Type()
)
ipFilterHTTPMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPMask.setStatus("current")
_IpFilterHTTPStatus_Type = ValidStatus
_IpFilterHTTPStatus_Object = MibTableColumn
ipFilterHTTPStatus = _IpFilterHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 2, 1, 3),
    _IpFilterHTTPStatus_Type()
)
ipFilterHTTPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPStatus.setStatus("current")
_IpFilterTelnetTable_Object = MibTable
ipFilterTelnetTable = _IpFilterTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 3)
)
if mibBuilder.loadTexts:
    ipFilterTelnetTable.setStatus("current")
_IpFilterTelnetEntry_Object = MibTableRow
ipFilterTelnetEntry = _IpFilterTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 3, 1)
)
ipFilterTelnetEntry.setIndexNames(
    (0, "DMswitch-MIB", "ipFilterTelnetAddress"),
    (0, "DMswitch-MIB", "ipFilterTelnetMask"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetEntry.setStatus("current")
_IpFilterTelnetAddress_Type = IpAddress
_IpFilterTelnetAddress_Object = MibTableColumn
ipFilterTelnetAddress = _IpFilterTelnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 3, 1, 1),
    _IpFilterTelnetAddress_Type()
)
ipFilterTelnetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetAddress.setStatus("current")
_IpFilterTelnetMask_Type = IpAddress
_IpFilterTelnetMask_Object = MibTableColumn
ipFilterTelnetMask = _IpFilterTelnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 3, 1, 2),
    _IpFilterTelnetMask_Type()
)
ipFilterTelnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetMask.setStatus("current")
_IpFilterTelnetStatus_Type = ValidStatus
_IpFilterTelnetStatus_Object = MibTableColumn
ipFilterTelnetStatus = _IpFilterTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 3, 1, 3),
    _IpFilterTelnetStatus_Type()
)
ipFilterTelnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetStatus.setStatus("current")
_IpFilterSSHTable_Object = MibTable
ipFilterSSHTable = _IpFilterSSHTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 4)
)
if mibBuilder.loadTexts:
    ipFilterSSHTable.setStatus("current")
_IpFilterSSHEntry_Object = MibTableRow
ipFilterSSHEntry = _IpFilterSSHEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 4, 1)
)
ipFilterSSHEntry.setIndexNames(
    (0, "DMswitch-MIB", "ipFilterSSHAddress"),
    (0, "DMswitch-MIB", "ipFilterSSHMask"),
)
if mibBuilder.loadTexts:
    ipFilterSSHEntry.setStatus("current")
_IpFilterSSHAddress_Type = IpAddress
_IpFilterSSHAddress_Object = MibTableColumn
ipFilterSSHAddress = _IpFilterSSHAddress_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 4, 1, 1),
    _IpFilterSSHAddress_Type()
)
ipFilterSSHAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSSHAddress.setStatus("current")
_IpFilterSSHMask_Type = IpAddress
_IpFilterSSHMask_Object = MibTableColumn
ipFilterSSHMask = _IpFilterSSHMask_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 4, 1, 2),
    _IpFilterSSHMask_Type()
)
ipFilterSSHMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSSHMask.setStatus("current")
_IpFilterSSHStatus_Type = ValidStatus
_IpFilterSSHStatus_Object = MibTableColumn
ipFilterSSHStatus = _IpFilterSSHStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 17, 3, 4, 1, 3),
    _IpFilterSSHStatus_Type()
)
ipFilterSSHStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSSHStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19)
)


class _SysLogStatus_Type(Integer32):
    """Custom type sysLogStatus based on Integer32"""
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


_SysLogStatus_Type.__name__ = "Integer32"
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 1),
    _SysLogStatus_Type()
)
sysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogStatus.setStatus("current")


class _SysLogHistoryFlashLevel_Type(Integer32):
    """Custom type sysLogHistoryFlashLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryFlashLevel_Type.__name__ = "Integer32"
_SysLogHistoryFlashLevel_Object = MibScalar
sysLogHistoryFlashLevel = _SysLogHistoryFlashLevel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 2),
    _SysLogHistoryFlashLevel_Type()
)
sysLogHistoryFlashLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryFlashLevel.setStatus("current")


class _SysLogHistoryRamLevel_Type(Integer32):
    """Custom type sysLogHistoryRamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryRamLevel_Type.__name__ = "Integer32"
_SysLogHistoryRamLevel_Object = MibScalar
sysLogHistoryRamLevel = _SysLogHistoryRamLevel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 1),
    _RemoteLogStatus_Type()
)
remoteLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogStatus.setStatus("current")


class _RemoteLogLevel_Type(Integer32):
    """Custom type remoteLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RemoteLogLevel_Type.__name__ = "Integer32"
_RemoteLogLevel_Object = MibScalar
remoteLogLevel = _RemoteLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 2),
    _RemoteLogLevel_Type()
)
remoteLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogLevel.setStatus("current")


class _RemoteLogFacilityType_Type(Integer32):
    """Custom type remoteLogFacilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
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
        *(("localUse0", 16),
          ("localUse1", 17),
          ("localUse2", 18),
          ("localUse3", 19),
          ("localUse4", 20),
          ("localUse5", 21),
          ("localUse6", 22),
          ("localUse7", 23))
    )


_RemoteLogFacilityType_Type.__name__ = "Integer32"
_RemoteLogFacilityType_Object = MibScalar
remoteLogFacilityType = _RemoteLogFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "DMswitch-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1)
)


class _SntpStatus_Type(Integer32):
    """Custom type sntpStatus based on Integer32"""
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


_SntpStatus_Type.__name__ = "Integer32"
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpPollInterval_Type(Integer32):
    """Custom type sntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_SntpPollInterval_Type.__name__ = "Integer32"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 2),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 3, 1)
)
sntpServerEntry.setIndexNames(
    (0, "DMswitch-MIB", "sntpServerIp"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")
_SntpServerIp_Type = IpAddress
_SntpServerIp_Object = MibTableColumn
sntpServerIp = _SntpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 3, 1, 1),
    _SntpServerIp_Type()
)
sntpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerIp.setStatus("current")
_SntpServerStatus_Type = ValidStatus
_SntpServerStatus_Object = MibTableColumn
sntpServerStatus = _SntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 1, 3, 1, 2),
    _SntpServerStatus_Type()
)
sntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerStatus.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 2),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 20, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "DMswitch-MIB", "fileInfoUnitID"),
    (0, "DMswitch-MIB", "fileInfoFileIndex"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 1),
    _FileInfoUnitID_Type()
)
fileInfoUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoUnitID.setStatus("current")
_FileInfoFileIndex_Type = Integer32
_FileInfoFileIndex_Object = MibTableColumn
fileInfoFileIndex = _FileInfoFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 2),
    _FileInfoFileIndex_Type()
)
fileInfoFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoFileIndex.setStatus("current")
_FileInfoFlashId_Type = Integer32
_FileInfoFlashId_Object = MibTableColumn
fileInfoFlashId = _FileInfoFlashId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 3),
    _FileInfoFlashId_Type()
)
fileInfoFlashId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFlashId.setStatus("current")


class _FileInfoFileName_Type(DisplayString):
    """Custom type fileInfoFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileInfoFileName_Type.__name__ = "DisplayString"
_FileInfoFileName_Object = MibTableColumn
fileInfoFileName = _FileInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 4),
    _FileInfoFileName_Type()
)
fileInfoFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileName.setStatus("current")


class _FileInfoFileType_Type(Integer32):
    """Custom type fileInfoFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("firmware", 1))
    )


_FileInfoFileType_Type.__name__ = "Integer32"
_FileInfoFileType_Object = MibTableColumn
fileInfoFileType = _FileInfoFileType_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 5),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 6),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 7),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileInfoFileSize.setUnits("bytes")


class _FileInfoCreationTime_Type(DisplayString):
    """Custom type fileInfoCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_FileInfoCreationTime_Type.__name__ = "DisplayString"
_FileInfoCreationTime_Object = MibTableColumn
fileInfoCreationTime = _FileInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 8),
    _FileInfoCreationTime_Type()
)
fileInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoCreationTime.setStatus("current")


class _FileInfoDelete_Type(Integer32):
    """Custom type fileInfoDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("noDelete", 1))
    )


_FileInfoDelete_Type.__name__ = "Integer32"
_FileInfoDelete_Object = MibTableColumn
fileInfoDelete = _FileInfoDelete_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 21, 1, 1, 9),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_CountMgt_ObjectIdentity = ObjectIdentity
countMgt = _CountMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 22)
)
_CountHoldPktsTable_Object = MibTable
countHoldPktsTable = _CountHoldPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 22, 1)
)
if mibBuilder.loadTexts:
    countHoldPktsTable.setStatus("current")
_CountHoldPktsEntry_Object = MibTableRow
countHoldPktsEntry = _CountHoldPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 22, 1, 1)
)
countHoldPktsEntry.setIndexNames(
    (0, "DMswitch-MIB", "interfaceNumber"),
)
if mibBuilder.loadTexts:
    countHoldPktsEntry.setStatus("current")
_InterfaceNumber_Type = Integer32
_InterfaceNumber_Object = MibTableColumn
interfaceNumber = _InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 22, 1, 1, 1),
    _InterfaceNumber_Type()
)
interfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumber.setStatus("current")
_CountHoldPkts_Type = Counter64
_CountHoldPkts_Object = MibTableColumn
countHoldPkts = _CountHoldPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 22, 1, 1, 2),
    _CountHoldPkts_Type()
)
countHoldPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countHoldPkts.setStatus("current")
_FilterCounterMgt_ObjectIdentity = ObjectIdentity
filterCounterMgt = _FilterCounterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23)
)
_FilterCounterInfoTable_Object = MibTable
filterCounterInfoTable = _FilterCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 1)
)
if mibBuilder.loadTexts:
    filterCounterInfoTable.setStatus("current")
_FilterCounterInfoEntry_Object = MibTableRow
filterCounterInfoEntry = _FilterCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 1, 1)
)
filterCounterInfoEntry.setIndexNames(
    (0, "DMswitch-MIB", "filterCounterInfoIndex"),
)
if mibBuilder.loadTexts:
    filterCounterInfoEntry.setStatus("current")
_FilterCounterInfoIndex_Type = Integer32
_FilterCounterInfoIndex_Object = MibTableColumn
filterCounterInfoIndex = _FilterCounterInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 1, 1, 1),
    _FilterCounterInfoIndex_Type()
)
filterCounterInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCounterInfoIndex.setStatus("current")


class _FilterCounterInfoRemark_Type(DisplayString):
    """Custom type filterCounterInfoRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FilterCounterInfoRemark_Type.__name__ = "DisplayString"
_FilterCounterInfoRemark_Object = MibTableColumn
filterCounterInfoRemark = _FilterCounterInfoRemark_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 1, 1, 2),
    _FilterCounterInfoRemark_Type()
)
filterCounterInfoRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCounterInfoRemark.setStatus("current")
_FilterCounterValueTable_Object = MibTable
filterCounterValueTable = _FilterCounterValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 2)
)
if mibBuilder.loadTexts:
    filterCounterValueTable.setStatus("current")
_FilterCounterValueEntry_Object = MibTableRow
filterCounterValueEntry = _FilterCounterValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 2, 1)
)
filterCounterValueEntry.setIndexNames(
    (0, "DMswitch-MIB", "filterCounterInfoIndex"),
    (0, "DMswitch-MIB", "filterCounterValueIndex"),
)
if mibBuilder.loadTexts:
    filterCounterValueEntry.setStatus("current")
_FilterCounterValueIndex_Type = Integer32
_FilterCounterValueIndex_Object = MibTableColumn
filterCounterValueIndex = _FilterCounterValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 2, 1, 1),
    _FilterCounterValueIndex_Type()
)
filterCounterValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCounterValueIndex.setStatus("current")
_FilterCounterValue_Type = Counter64
_FilterCounterValue_Object = MibTableColumn
filterCounterValue = _FilterCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 23, 2, 1, 2),
    _FilterCounterValue_Type()
)
filterCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCounterValue.setStatus("current")
_EapsMgt_ObjectIdentity = ObjectIdentity
eapsMgt = _EapsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24)
)
_EapsInfoTable_Object = MibTable
eapsInfoTable = _EapsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1)
)
if mibBuilder.loadTexts:
    eapsInfoTable.setStatus("current")
_EapsInfoEntry_Object = MibTableRow
eapsInfoEntry = _EapsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1, 1)
)
eapsInfoEntry.setIndexNames(
    (0, "DMswitch-MIB", "eapsInfoId"),
)
if mibBuilder.loadTexts:
    eapsInfoEntry.setStatus("current")
_EapsInfoId_Type = Integer32
_EapsInfoId_Object = MibTableColumn
eapsInfoId = _EapsInfoId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1, 1, 1),
    _EapsInfoId_Type()
)
eapsInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsInfoId.setStatus("current")


class _EapsInfoName_Type(DisplayString):
    """Custom type eapsInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapsInfoName_Type.__name__ = "DisplayString"
_EapsInfoName_Object = MibTableColumn
eapsInfoName = _EapsInfoName_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1, 1, 2),
    _EapsInfoName_Type()
)
eapsInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsInfoName.setStatus("current")


class _EapsInfoMode_Type(Integer32):
    """Custom type eapsInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("master", 1),
          ("transit", 2))
    )


_EapsInfoMode_Type.__name__ = "Integer32"
_EapsInfoMode_Object = MibTableColumn
eapsInfoMode = _EapsInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1, 1, 3),
    _EapsInfoMode_Type()
)
eapsInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsInfoMode.setStatus("current")


class _EapsInfoState_Type(Integer32):
    """Custom type eapsInfoState based on Integer32"""
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
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("init", 6),
          ("linkdown", 4),
          ("linksup", 3),
          ("preforwarding", 5))
    )


_EapsInfoState_Type.__name__ = "Integer32"
_EapsInfoState_Object = MibTableColumn
eapsInfoState = _EapsInfoState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 24, 1, 1, 4),
    _EapsInfoState_Type()
)
eapsInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsInfoState.setStatus("current")
_CfmProbeMgmt_ObjectIdentity = ObjectIdentity
cfmProbeMgmt = _CfmProbeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25)
)
_CfmProbeDmTable_Object = MibTable
cfmProbeDmTable = _CfmProbeDmTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cfmProbeDmTable.setStatus("current")
_CfmProbeDmEntry_Object = MibTableRow
cfmProbeDmEntry = _CfmProbeDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1, 1)
)
cfmProbeDmEntry.setIndexNames(
    (0, "DMswitch-MIB", "cfmProbeDmIndex"),
)
if mibBuilder.loadTexts:
    cfmProbeDmEntry.setStatus("current")


class _CfmProbeDmIndex_Type(Integer32):
    """Custom type cfmProbeDmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CfmProbeDmIndex_Type.__name__ = "Integer32"
_CfmProbeDmIndex_Object = MibTableColumn
cfmProbeDmIndex = _CfmProbeDmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1, 1, 1),
    _CfmProbeDmIndex_Type()
)
cfmProbeDmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmProbeDmIndex.setStatus("current")
_CfmProbeDmAvgDelay_Type = Integer32
_CfmProbeDmAvgDelay_Object = MibTableColumn
cfmProbeDmAvgDelay = _CfmProbeDmAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1, 1, 2),
    _CfmProbeDmAvgDelay_Type()
)
cfmProbeDmAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmProbeDmAvgDelay.setStatus("current")
_CfmProbeDmAvgJitter_Type = Integer32
_CfmProbeDmAvgJitter_Object = MibTableColumn
cfmProbeDmAvgJitter = _CfmProbeDmAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1, 1, 3),
    _CfmProbeDmAvgJitter_Type()
)
cfmProbeDmAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmProbeDmAvgJitter.setStatus("current")
_CfmProbeDmLoss_Type = Integer32
_CfmProbeDmLoss_Object = MibTableColumn
cfmProbeDmLoss = _CfmProbeDmLoss_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 25, 1, 1, 4),
    _CfmProbeDmLoss_Type()
)
cfmProbeDmLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmProbeDmLoss.setStatus("current")
_CpumonMgmt_ObjectIdentity = ObjectIdentity
cpumonMgmt = _CpumonMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26)
)
_CpuActiveUsageTable_Object = MibTable
cpuActiveUsageTable = _CpuActiveUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cpuActiveUsageTable.setStatus("current")
_CpuActiveUsageEntry_Object = MibTableRow
cpuActiveUsageEntry = _CpuActiveUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 1, 1)
)
cpuActiveUsageEntry.setIndexNames(
    (0, "DMswitch-MIB", "cpuActiveUsageIndex"),
)
if mibBuilder.loadTexts:
    cpuActiveUsageEntry.setStatus("current")
_CpuActiveUsageIndex_Type = Integer32
_CpuActiveUsageIndex_Object = MibTableColumn
cpuActiveUsageIndex = _CpuActiveUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 1, 1, 1),
    _CpuActiveUsageIndex_Type()
)
cpuActiveUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuActiveUsageIndex.setStatus("current")
_CpuActiveUsageValue_Type = Integer32
_CpuActiveUsageValue_Object = MibTableColumn
cpuActiveUsageValue = _CpuActiveUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 1, 1, 2),
    _CpuActiveUsageValue_Type()
)
cpuActiveUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuActiveUsageValue.setStatus("current")
_MemActiveUsageTable_Object = MibTable
memActiveUsageTable = _MemActiveUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 2)
)
if mibBuilder.loadTexts:
    memActiveUsageTable.setStatus("current")
_MemActiveUsageEntry_Object = MibTableRow
memActiveUsageEntry = _MemActiveUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 2, 1)
)
memActiveUsageEntry.setIndexNames(
    (0, "DMswitch-MIB", "memActiveUsageIndex"),
)
if mibBuilder.loadTexts:
    memActiveUsageEntry.setStatus("current")
_MemActiveUsageIndex_Type = Integer32
_MemActiveUsageIndex_Object = MibTableColumn
memActiveUsageIndex = _MemActiveUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 2, 1, 1),
    _MemActiveUsageIndex_Type()
)
memActiveUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    memActiveUsageIndex.setStatus("current")
_MemActiveUsageValue_Type = Integer32
_MemActiveUsageValue_Object = MibTableColumn
memActiveUsageValue = _MemActiveUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 2, 1, 2),
    _MemActiveUsageValue_Type()
)
memActiveUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveUsageValue.setStatus("current")
_CpuStandbyUsageTable_Object = MibTable
cpuStandbyUsageTable = _CpuStandbyUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 3)
)
if mibBuilder.loadTexts:
    cpuStandbyUsageTable.setStatus("current")
_CpuStandbyUsageEntry_Object = MibTableRow
cpuStandbyUsageEntry = _CpuStandbyUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 3, 1)
)
cpuStandbyUsageEntry.setIndexNames(
    (0, "DMswitch-MIB", "cpuStandbyUsageIndex"),
)
if mibBuilder.loadTexts:
    cpuStandbyUsageEntry.setStatus("current")
_CpuStandbyUsageIndex_Type = Integer32
_CpuStandbyUsageIndex_Object = MibTableColumn
cpuStandbyUsageIndex = _CpuStandbyUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 3, 1, 1),
    _CpuStandbyUsageIndex_Type()
)
cpuStandbyUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuStandbyUsageIndex.setStatus("current")
_CpuStandbyUsageValue_Type = Integer32
_CpuStandbyUsageValue_Object = MibTableColumn
cpuStandbyUsageValue = _CpuStandbyUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 3, 1, 2),
    _CpuStandbyUsageValue_Type()
)
cpuStandbyUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStandbyUsageValue.setStatus("current")
_MemStandbyUsageTable_Object = MibTable
memStandbyUsageTable = _MemStandbyUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 4)
)
if mibBuilder.loadTexts:
    memStandbyUsageTable.setStatus("current")
_MemStandbyUsageEntry_Object = MibTableRow
memStandbyUsageEntry = _MemStandbyUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 4, 1)
)
memStandbyUsageEntry.setIndexNames(
    (0, "DMswitch-MIB", "memStandbyUsageIndex"),
)
if mibBuilder.loadTexts:
    memStandbyUsageEntry.setStatus("current")
_MemStandbyUsageIndex_Type = Integer32
_MemStandbyUsageIndex_Object = MibTableColumn
memStandbyUsageIndex = _MemStandbyUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 4, 1, 1),
    _MemStandbyUsageIndex_Type()
)
memStandbyUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    memStandbyUsageIndex.setStatus("current")
_MemStandbyUsageValue_Type = Integer32
_MemStandbyUsageValue_Object = MibTableColumn
memStandbyUsageValue = _MemStandbyUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 26, 4, 1, 2),
    _MemStandbyUsageValue_Type()
)
memStandbyUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memStandbyUsageValue.setStatus("current")
_QueuePortMgmt_ObjectIdentity = ObjectIdentity
queuePortMgmt = _QueuePortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27)
)
_QueuePortTable_Object = MibTable
queuePortTable = _QueuePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1)
)
if mibBuilder.loadTexts:
    queuePortTable.setStatus("current")
_QueuePortEntry_Object = MibTableRow
queuePortEntry = _QueuePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1)
)
queuePortEntry.setIndexNames(
    (0, "DMswitch-MIB", "queuePortIfIndex"),
    (0, "DMswitch-MIB", "queuePortQueueIndex"),
)
if mibBuilder.loadTexts:
    queuePortEntry.setStatus("current")
_QueuePortIfIndex_Type = Integer32
_QueuePortIfIndex_Object = MibTableColumn
queuePortIfIndex = _QueuePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 1),
    _QueuePortIfIndex_Type()
)
queuePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queuePortIfIndex.setStatus("current")
_QueuePortQueueIndex_Type = Integer32
_QueuePortQueueIndex_Object = MibTableColumn
queuePortQueueIndex = _QueuePortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 2),
    _QueuePortQueueIndex_Type()
)
queuePortQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queuePortQueueIndex.setStatus("current")
_QueuePortSentPackets_Type = Counter64
_QueuePortSentPackets_Object = MibTableColumn
queuePortSentPackets = _QueuePortSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 3),
    _QueuePortSentPackets_Type()
)
queuePortSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortSentPackets.setStatus("current")
_QueuePortSentBytes_Type = Counter64
_QueuePortSentBytes_Object = MibTableColumn
queuePortSentBytes = _QueuePortSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 4),
    _QueuePortSentBytes_Type()
)
queuePortSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortSentBytes.setStatus("current")
_QueuePortDroppedPackets_Type = Counter64
_QueuePortDroppedPackets_Object = MibTableColumn
queuePortDroppedPackets = _QueuePortDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 5),
    _QueuePortDroppedPackets_Type()
)
queuePortDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortDroppedPackets.setStatus("current")
_QueuePortDroppedBytes_Type = Counter64
_QueuePortDroppedBytes_Object = MibTableColumn
queuePortDroppedBytes = _QueuePortDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 27, 1, 1, 6),
    _QueuePortDroppedBytes_Type()
)
queuePortDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortDroppedBytes.setStatus("current")
_DdTransceiversMgmt_ObjectIdentity = ObjectIdentity
ddTransceiversMgmt = _DdTransceiversMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28)
)
_DdTransceiversTable_Object = MibTable
ddTransceiversTable = _DdTransceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1)
)
if mibBuilder.loadTexts:
    ddTransceiversTable.setStatus("current")
_DdTransceiversEntry_Object = MibTableRow
ddTransceiversEntry = _DdTransceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1)
)
ddTransceiversEntry.setIndexNames(
    (0, "DMswitch-MIB", "ddTransceiversIfIndex"),
)
if mibBuilder.loadTexts:
    ddTransceiversEntry.setStatus("current")
_DdTransceiversIfIndex_Type = Integer32
_DdTransceiversIfIndex_Object = MibTableColumn
ddTransceiversIfIndex = _DdTransceiversIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 1),
    _DdTransceiversIfIndex_Type()
)
ddTransceiversIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddTransceiversIfIndex.setStatus("current")


class _DdTransceiversTemperature_Type(DisplayString):
    """Custom type ddTransceiversTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DdTransceiversTemperature_Type.__name__ = "DisplayString"
_DdTransceiversTemperature_Object = MibTableColumn
ddTransceiversTemperature = _DdTransceiversTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 2),
    _DdTransceiversTemperature_Type()
)
ddTransceiversTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddTransceiversTemperature.setStatus("current")


class _DdTransceiversVcc3v3_Type(DisplayString):
    """Custom type ddTransceiversVcc3v3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DdTransceiversVcc3v3_Type.__name__ = "DisplayString"
_DdTransceiversVcc3v3_Object = MibTableColumn
ddTransceiversVcc3v3 = _DdTransceiversVcc3v3_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 3),
    _DdTransceiversVcc3v3_Type()
)
ddTransceiversVcc3v3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddTransceiversVcc3v3.setStatus("current")


class _DdTransceiversRxPower_Type(DisplayString):
    """Custom type ddTransceiversRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DdTransceiversRxPower_Type.__name__ = "DisplayString"
_DdTransceiversRxPower_Object = MibTableColumn
ddTransceiversRxPower = _DdTransceiversRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 4),
    _DdTransceiversRxPower_Type()
)
ddTransceiversRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddTransceiversRxPower.setStatus("current")


class _DdTransceiversTxPower_Type(DisplayString):
    """Custom type ddTransceiversTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DdTransceiversTxPower_Type.__name__ = "DisplayString"
_DdTransceiversTxPower_Object = MibTableColumn
ddTransceiversTxPower = _DdTransceiversTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 5),
    _DdTransceiversTxPower_Type()
)
ddTransceiversTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddTransceiversTxPower.setStatus("current")


class _DdTransceiversTxBias_Type(DisplayString):
    """Custom type ddTransceiversTxBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DdTransceiversTxBias_Type.__name__ = "DisplayString"
_DdTransceiversTxBias_Object = MibTableColumn
ddTransceiversTxBias = _DdTransceiversTxBias_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 1, 28, 1, 1, 6),
    _DdTransceiversTxBias_Type()
)
ddTransceiversTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddTransceiversTxBias.setStatus("current")
_DmSwitchNotifications_ObjectIdentity = ObjectIdentity
dmSwitchNotifications = _DmSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2)
)
_DmSwitchTraps_ObjectIdentity = ObjectIdentity
dmSwitchTraps = _DmSwitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1)
)
_DmSwitchTrapsPrefix_ObjectIdentity = ObjectIdentity
dmSwitchTrapsPrefix = _DmSwitchTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0)
)
_DmSwitchConformance_ObjectIdentity = ObjectIdentity
dmSwitchConformance = _DmSwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 3)
)

# Managed Objects groups


# Notification objects

swLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40001)
)
swLoginFailTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapLoginUserName"))
)
if mibBuilder.loadTexts:
    swLoginFailTrap.setStatus(
        "current"
    )

swLoginSucessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40002)
)
swLoginSucessTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapLoginUserName"))
)
if mibBuilder.loadTexts:
    swLoginSucessTrap.setStatus(
        "current"
    )

swStackAttachTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40003)
)
swStackAttachTrap.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "swSerialNumber"))
)
if mibBuilder.loadTexts:
    swStackAttachTrap.setStatus(
        "current"
    )

swStackDetachTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40004)
)
swStackDetachTrap.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "swSerialNumber"))
)
if mibBuilder.loadTexts:
    swStackDetachTrap.setStatus(
        "current"
    )

swForbiddenAccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40005)
)
swForbiddenAccessTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapForbiddenAccessMode"),
        ("DMswitch-MIB", "trapForbiddenAccessIp"))
)
if mibBuilder.loadTexts:
    swForbiddenAccessTrap.setStatus(
        "current"
    )

swSfpPresenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40006)
)
swSfpPresenceTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapSfpPresenceStatus"))
)
if mibBuilder.loadTexts:
    swSfpPresenceTrap.setStatus(
        "current"
    )

swConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40007)
)
swConfigChangeTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swConfigChangeTrap.setStatus(
        "current"
    )

swConfigSaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40008)
)
swConfigSaveTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapConfigSavePartition"))
)
if mibBuilder.loadTexts:
    swConfigSaveTrap.setStatus(
        "current"
    )

swFanStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40009)
)
swFanStatusChangeTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "swIndivFanUnitIndex"),
        ("DMswitch-MIB", "swIndivFanIndex"),
        ("DMswitch-MIB", "swIndivFanStatus"))
)
if mibBuilder.loadTexts:
    swFanStatusChangeTrap.setStatus(
        "current"
    )

swTrapsLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40010)
)
if mibBuilder.loadTexts:
    swTrapsLostTrap.setStatus(
        "current"
    )

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40011)
)
swPowerStatusChangeTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "swIndivPowerUnitIndex"),
        ("DMswitch-MIB", "swIndivPowerIndex"),
        ("DMswitch-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40012)
)
swAlarmTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "swIndivAlarmUnitIndex"),
        ("DMswitch-MIB", "swIndivAlarmIndex"),
        ("DMswitch-MIB", "swIndivAlarmStatus"))
)
if mibBuilder.loadTexts:
    swAlarmTrap.setStatus(
        "current"
    )

swDuplicatedIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40013)
)
swDuplicatedIp.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapDuplicatedIpVlan"),
        ("DMswitch-MIB", "trapDuplicatedIpAddress"),
        ("DMswitch-MIB", "trapDuplicatedIpMacAddress"))
)
if mibBuilder.loadTexts:
    swDuplicatedIp.setStatus(
        "current"
    )

swLoopbackOnPortDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40014)
)
swLoopbackOnPortDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swLoopbackOnPortDetected.setStatus(
        "current"
    )

swLoopbackOnPortNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40015)
)
swLoopbackOnPortNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swLoopbackOnPortNoMoreDetected.setStatus(
        "current"
    )

swUnidirLinkDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40016)
)
swUnidirLinkDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swUnidirLinkDetected.setStatus(
        "current"
    )

swUnidirLinkRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40017)
)
swUnidirLinkRecovered.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swUnidirLinkRecovered.setStatus(
        "current"
    )

swCriticalEventDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40018)
)
swCriticalEventDetected.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swCriticalEventDetected.setStatus(
        "current"
    )

swCriticalEventRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40019)
)
swCriticalEventRecovered.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swCriticalEventRecovered.setStatus(
        "current"
    )

swLinkFlapDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40020)
)
swLinkFlapDetected.setObjects(
    ("DMswitch-MIB", "portIndex")
)
if mibBuilder.loadTexts:
    swLinkFlapDetected.setStatus(
        "current"
    )

swLinkFlapNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40021)
)
swLinkFlapNoMoreDetected.setObjects(
    ("DMswitch-MIB", "portIndex")
)
if mibBuilder.loadTexts:
    swLinkFlapNoMoreDetected.setStatus(
        "current"
    )

swEapsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40022)
)
swEapsStatusChange.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapEapsDomainId"),
        ("DMswitch-MIB", "trapEapsDomainName"),
        ("DMswitch-MIB", "trapEapsStatus"))
)
if mibBuilder.loadTexts:
    swEapsStatusChange.setStatus(
        "current"
    )

swPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40023)
)
swPortSecurityViolation.setObjects(
    ("DMswitch-MIB", "portIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityViolation.setStatus(
        "current"
    )

swHighTemperatureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40024)
)
swHighTemperatureDetected.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapTemperature"))
)
if mibBuilder.loadTexts:
    swHighTemperatureDetected.setStatus(
        "current"
    )

swHighTemperatureNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40025)
)
swHighTemperatureNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapTemperature"))
)
if mibBuilder.loadTexts:
    swHighTemperatureNoMoreDetected.setStatus(
        "current"
    )

swFuseStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40026)
)
swFuseStatusChange.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapFuseId"),
        ("DMswitch-MIB", "trapFuseStatus"))
)
if mibBuilder.loadTexts:
    swFuseStatusChange.setStatus(
        "current"
    )

swFansBoardPresenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40027)
)
swFansBoardPresenceTrap.setObjects(
    ("DMswitch-MIB", "trapFansBoardPresenceStatus")
)
if mibBuilder.loadTexts:
    swFansBoardPresenceTrap.setStatus(
        "current"
    )

swStandbyMpuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40028)
)
swStandbyMpuTrap.setObjects(
      *(("DMswitch-MIB", "swMpuIndex"),
        ("DMswitch-MIB", "swMpuSerialNumber"),
        ("DMswitch-MIB", "swMpuModelId"),
        ("DMswitch-MIB", "trapStandbyMpuPresenceStatus"))
)
if mibBuilder.loadTexts:
    swStandbyMpuTrap.setStatus(
        "current"
    )

swNonHomologSfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40029)
)
swNonHomologSfpTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swNonHomologSfpTrap.setStatus(
        "current"
    )

swHighCpuUsageDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40030)
)
swHighCpuUsageDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swHighCpuUsageDetected.setStatus(
        "current"
    )

swHighCpuUsageNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40031)
)
swHighCpuUsageNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swHighCpuUsageNoMoreDetected.setStatus(
        "current"
    )

swDuplicatedMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40032)
)
swDuplicatedMac.setObjects(
    ("DMswitch-MIB", "trapMacAddressMove")
)
if mibBuilder.loadTexts:
    swDuplicatedMac.setStatus(
        "current"
    )

swHighMemoryUsageDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40033)
)
swHighMemoryUsageDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapMemFree"))
)
if mibBuilder.loadTexts:
    swHighMemoryUsageDetected.setStatus(
        "current"
    )

swHighMemoryUsageNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40034)
)
swHighMemoryUsageNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapMemFree"))
)
if mibBuilder.loadTexts:
    swHighMemoryUsageNoMoreDetected.setStatus(
        "current"
    )

swNewBootloaderVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40035)
)
swNewBootloaderVersion.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapBootloaderNew"))
)
if mibBuilder.loadTexts:
    swNewBootloaderVersion.setStatus(
        "current"
    )

swCesopTdmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40036)
)
swCesopTdmStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopTdmStatus"))
)
if mibBuilder.loadTexts:
    swCesopTdmStatusTrap.setStatus(
        "current"
    )

swCesopTdmRemoteStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40037)
)
swCesopTdmRemoteStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopTdmRemoteStatus"))
)
if mibBuilder.loadTexts:
    swCesopTdmRemoteStatusTrap.setStatus(
        "current"
    )

swCesopTdmCasStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40038)
)
swCesopTdmCasStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopTdmCasStatus"))
)
if mibBuilder.loadTexts:
    swCesopTdmCasStatusTrap.setStatus(
        "current"
    )

swCesopTdmCrcStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40039)
)
swCesopTdmCrcStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopTdmCrcStatus"))
)
if mibBuilder.loadTexts:
    swCesopTdmCrcStatusTrap.setStatus(
        "current"
    )

swCesopBundleLocalTdmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40040)
)
swCesopBundleLocalTdmStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundleLocalTdmStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundleLocalTdmStatusTrap.setStatus(
        "current"
    )

swCesopBundleRemoteTdmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40041)
)
swCesopBundleRemoteTdmStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundleRemoteTdmStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundleRemoteTdmStatusTrap.setStatus(
        "current"
    )

swCesopBundleLocalStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40042)
)
swCesopBundleLocalStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundleLocalStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundleLocalStatusTrap.setStatus(
        "current"
    )

swCesopBundleRemoteStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40043)
)
swCesopBundleRemoteStatusTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundleRemoteStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundleRemoteStatusTrap.setStatus(
        "current"
    )

swCesopBundlePktMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40044)
)
swCesopBundlePktMismatchTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundlePktMismatchStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundlePktMismatchTrap.setStatus(
        "current"
    )

swCesopBundleNextHopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40045)
)
swCesopBundleNextHopTrap.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopBundleNextHopStatus"))
)
if mibBuilder.loadTexts:
    swCesopBundleNextHopTrap.setStatus(
        "current"
    )

swCesopClockAdapLinkQualityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40046)
)
swCesopClockAdapLinkQualityTrap.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopClockAdapLinkQuality"))
)
if mibBuilder.loadTexts:
    swCesopClockAdapLinkQualityTrap.setStatus(
        "current"
    )

swCesopClockSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40047)
)
swCesopClockSourceTrap.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCesopClockSourceStatus"))
)
if mibBuilder.loadTexts:
    swCesopClockSourceTrap.setStatus(
        "current"
    )

swRemoteDeviceReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40048)
)
swRemoteDeviceReady.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swRemoteDeviceReady.setStatus(
        "current"
    )

swRemoteDeviceLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40049)
)
swRemoteDeviceLost.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swRemoteDeviceLost.setStatus(
        "current"
    )

swRemoteDeviceConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40050)
)
swRemoteDeviceConfigFail.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swRemoteDeviceConfigFail.setStatus(
        "current"
    )

swRemoteDeviceConfigForced = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40051)
)
swRemoteDeviceConfigForced.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swRemoteDeviceConfigForced.setStatus(
        "current"
    )

swFanFuseStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40052)
)
swFanFuseStatusChange.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapFuseId"),
        ("DMswitch-MIB", "trapFuseStatus"))
)
if mibBuilder.loadTexts:
    swFanFuseStatusChange.setStatus(
        "current"
    )

swDyingGaspPackReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40053)
)
swDyingGaspPackReceived.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swDyingGaspPackReceived.setStatus(
        "current"
    )

swBroadcastStormCheckChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40054)
)
swBroadcastStormCheckChange.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapBroadcastStormControlStatus"),
        ("DMswitch-MIB", "trapBroadcastStormControlPPS"))
)
if mibBuilder.loadTexts:
    swBroadcastStormCheckChange.setStatus(
        "current"
    )

swMulticastStormCheckChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40055)
)
swMulticastStormCheckChange.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapMulticastStormControlStatus"),
        ("DMswitch-MIB", "trapMulticastStormControlPPS"))
)
if mibBuilder.loadTexts:
    swMulticastStormCheckChange.setStatus(
        "current"
    )

swBpduProtectLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40056)
)
swBpduProtectLimit.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swBpduProtectLimit.setStatus(
        "current"
    )

swChangeStatusLDP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40057)
)
swChangeStatusLDP.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapStatusLDP"),
        ("DMswitch-MIB", "trapIdLDP"))
)
if mibBuilder.loadTexts:
    swChangeStatusLDP.setStatus(
        "current"
    )

swChangeStatusTunnelRSVP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40058)
)
swChangeStatusTunnelRSVP.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapStatusTunnelRSVP"),
        ("DMswitch-MIB", "trapIdTunnelRSVP"))
)
if mibBuilder.loadTexts:
    swChangeStatusTunnelRSVP.setStatus(
        "current"
    )

swBpduProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40059)
)
swBpduProtect.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swBpduProtect.setStatus(
        "current"
    )

swRouteTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40060)
)
swRouteTableFull.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swRouteTableFull.setStatus(
        "current"
    )

swPanelStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40061)
)
swPanelStatusTrap.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapPanelStatus"))
)
if mibBuilder.loadTexts:
    swPanelStatusTrap.setStatus(
        "current"
    )

swLSTGroupLinkStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40062)
)
swLSTGroupLinkStatusDown.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapLSTGroup"))
)
if mibBuilder.loadTexts:
    swLSTGroupLinkStatusDown.setStatus(
        "current"
    )

swLSTGroupLinkStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40063)
)
swLSTGroupLinkStatusUp.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapLSTGroup"))
)
if mibBuilder.loadTexts:
    swLSTGroupLinkStatusUp.setStatus(
        "current"
    )

swHighCpuL3UsageDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40064)
)
swHighCpuL3UsageDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swHighCpuL3UsageDetected.setStatus(
        "current"
    )

swHighCpuL3UsageNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40065)
)
swHighCpuL3UsageNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swHighCpuL3UsageNoMoreDetected.setStatus(
        "current"
    )

swHighMemoryL3UsageDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40066)
)
swHighMemoryL3UsageDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapMemL3Free"))
)
if mibBuilder.loadTexts:
    swHighMemoryL3UsageDetected.setStatus(
        "current"
    )

swHighMemoryL3UsageNoMoreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40067)
)
swHighMemoryL3UsageNoMoreDetected.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapMemL3Free"))
)
if mibBuilder.loadTexts:
    swHighMemoryL3UsageNoMoreDetected.setStatus(
        "current"
    )

swMpuNsfIdDiffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40068)
)
swMpuNsfIdDiffers.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapActiveMpuNsfId"),
        ("DMswitch-MIB", "trapStandByMpuNsfId"))
)
if mibBuilder.loadTexts:
    swMpuNsfIdDiffers.setStatus(
        "current"
    )

swErpsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40069)
)
swErpsStatusChange.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapErpsDomainId"),
        ("DMswitch-MIB", "trapErpsDomainName"),
        ("DMswitch-MIB", "trapErpsStatus"))
)
if mibBuilder.loadTexts:
    swErpsStatusChange.setStatus(
        "current"
    )

swCfmDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40070)
)
swCfmDefect.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapCfmMdName"),
        ("DMswitch-MIB", "trapCfmMaName"),
        ("DMswitch-MIB", "trapCfmMepId"),
        ("DMswitch-MIB", "trapCfmVlan"),
        ("DMswitch-MIB", "trapCfmDefect"))
)
if mibBuilder.loadTexts:
    swCfmDefect.setStatus(
        "current"
    )

swLldpRemoteChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40071)
)
swLldpRemoteChange.setObjects(
      *(("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swLldpRemoteChange.setStatus(
        "current"
    )

swPoeOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40072)
)
swPoeOverCurrent.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swPoeOverCurrent.setStatus(
        "current"
    )

swPoePowerRestriction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40073)
)
swPoePowerRestriction.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"))
)
if mibBuilder.loadTexts:
    swPoePowerRestriction.setStatus(
        "current"
    )

swCoreDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40074)
)
swCoreDump.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swCoreDump.setStatus(
        "current"
    )

swElmiEvcStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40075)
)
swElmiEvcStatus.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapEvcName"),
        ("DMswitch-MIB", "trapEvcStatus"))
)
if mibBuilder.loadTexts:
    swElmiEvcStatus.setStatus(
        "current"
    )

swSyncSystemClockSwitchHier = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40076)
)
swSyncSystemClockSwitchHier.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swSyncSystemClockSwitchHier.setStatus(
        "current"
    )

swSyncSystemClockStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40077)
)
swSyncSystemClockStatus.setObjects(
      *(("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapSyncSystemClockStatus"))
)
if mibBuilder.loadTexts:
    swSyncSystemClockStatus.setStatus(
        "current"
    )

swHostTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40078)
)
swHostTableFull.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"))
)
if mibBuilder.loadTexts:
    swHostTableFull.setStatus(
        "current"
    )

swSyncG704ClockStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40079)
)
swSyncG704ClockStatus.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapCesopG704ClockSourceStatus"))
)
if mibBuilder.loadTexts:
    swSyncG704ClockStatus.setStatus(
        "current"
    )

swSystemWarningsUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40080)
)
swSystemWarningsUnits.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "trapSystemWarningsUnits"))
)
if mibBuilder.loadTexts:
    swSystemWarningsUnits.setStatus(
        "current"
    )

swRebootDueToOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5, 201, 2, 1, 0, 40081)
)
swRebootDueToOvertemp.setObjects(
      *(("DMswitch-MIB", "trapDevNo"),
        ("DMswitch-MIB", "trapDevLocalId"),
        ("DMswitch-MIB", "swUnitIndex"),
        ("DMswitch-MIB", "portIndex"),
        ("DMswitch-MIB", "trapSensorGroup"),
        ("DMswitch-MIB", "trapTemperature"))
)
if mibBuilder.loadTexts:
    swRebootDueToOvertemp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMswitch-MIB",
    **{"ValidStatus": ValidStatus,
       "KeySegment": KeySegment,
       "StaPathCostMode": StaPathCostMode,
       "dmSwitchMIB": dmSwitchMIB,
       "dmSwitchMIBObjects": dmSwitchMIBObjects,
       "switchMgt": switchMgt,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swHardwareVer": swHardwareVer,
       "swBootLoaderVer": swBootLoaderVer,
       "swFirmwareVer": swFirmwareVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swRoleInSystem": swRoleInSystem,
       "swSerialNumber": swSerialNumber,
       "swProdName": swProdName,
       "swProdModelId": swProdModelId,
       "swFirmwareReleaseDate": swFirmwareReleaseDate,
       "swTemperature": swTemperature,
       "swG704IntfNumber": swG704IntfNumber,
       "swE1cIntfNumber": swE1cIntfNumber,
       "swBundleIntfNumber": swBundleIntfNumber,
       "swPtpIntfNumber": swPtpIntfNumber,
       "swSdhIntfNumber": swSdhIntfNumber,
       "swVC4Number": swVC4Number,
       "swVC12Number": swVC12Number,
       "switchProductId": switchProductId,
       "swProdManufacturer": swProdManufacturer,
       "swProdDescription": swProdDescription,
       "swProdUrl": swProdUrl,
       "swIdentifier": swIdentifier,
       "swVendorId": swVendorId,
       "switchIndivPowerTable": switchIndivPowerTable,
       "switchIndivPowerEntry": switchIndivPowerEntry,
       "swIndivPowerUnitIndex": swIndivPowerUnitIndex,
       "swIndivPowerIndex": swIndivPowerIndex,
       "swIndivPowerStatus": swIndivPowerStatus,
       "switchIndivFanTable": switchIndivFanTable,
       "switchIndivFanEntry": switchIndivFanEntry,
       "swIndivFanUnitIndex": swIndivFanUnitIndex,
       "swIndivFanIndex": swIndivFanIndex,
       "swIndivFanStatus": swIndivFanStatus,
       "switchIndivAlarmTable": switchIndivAlarmTable,
       "switchIndivAlarmEntry": switchIndivAlarmEntry,
       "swIndivAlarmUnitIndex": swIndivAlarmUnitIndex,
       "swIndivAlarmIndex": swIndivAlarmIndex,
       "swIndivAlarmStatus": swIndivAlarmStatus,
       "switchResObj": switchResObj,
       "swHashConfig": swHashConfig,
       "swHashStatus": swHashStatus,
       "swCpuUsage": swCpuUsage,
       "swMemUsage": swMemUsage,
       "switchMacAddrUsageTable": switchMacAddrUsageTable,
       "switchMacAddrUsageEntry": switchMacAddrUsageEntry,
       "swMacAddrUnitIndex": swMacAddrUnitIndex,
       "swMacAddrUsageValue": swMacAddrUsageValue,
       "swSlotNumber": swSlotNumber,
       "switchMpuTable": switchMpuTable,
       "switchMpuEntry": switchMpuEntry,
       "swMpuIndex": swMpuIndex,
       "swMpuBootLoaderVer": swMpuBootLoaderVer,
       "swMpuRoleInSystem": swMpuRoleInSystem,
       "swMpuSerialNumber": swMpuSerialNumber,
       "swMpuModelId": swMpuModelId,
       "swHashHardware": swHashHardware,
       "switchIndivAlarmOutTable": switchIndivAlarmOutTable,
       "switchIndivAlarmOutEntry": switchIndivAlarmOutEntry,
       "swIndivAlarmOutUnitIndex": swIndivAlarmOutUnitIndex,
       "swIndivAlarmOutStatus": swIndivAlarmOutStatus,
       "swChassisModel": swChassisModel,
       "switchSessionTable": switchSessionTable,
       "switchSessionEntry": switchSessionEntry,
       "swSessionUnitIndex": swSessionUnitIndex,
       "swSessionName": swSessionName,
       "swSessionUptime": swSessionUptime,
       "swSessionPid": swSessionPid,
       "swSessionSrcIP": swSessionSrcIP,
       "portMgt": portMgt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "portMdiStatus": portMdiStatus,
       "portTrunkIndex": portTrunkIndex,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortIndex": staPortIndex,
       "staPortAdminEdgePort": staPortAdminEdgePort,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortLongPathCost": staPortLongPathCost,
       "staPortSystemStatus": staPortSystemStatus,
       "staProtocolType": staProtocolType,
       "tftpMgt": tftpMgt,
       "tftpFile": tftpFile,
       "tftpFlashConfig": tftpFlashConfig,
       "tftpServer": tftpServer,
       "tftpAction": tftpAction,
       "restartMgt": restartMgt,
       "restartFirmware": restartFirmware,
       "restartConfig": restartConfig,
       "restartControl": restartControl,
       "mirrorMgt": mirrorMgt,
       "mirrorDestinationPort": mirrorDestinationPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorSourcePort": mirrorSourcePort,
       "mirrorType": mirrorType,
       "igmpSnoopMgt": igmpSnoopMgt,
       "igmpSnoopStatus": igmpSnoopStatus,
       "igmpSnoopQuerier": igmpSnoopQuerier,
       "igmpSnoopQueryCount": igmpSnoopQueryCount,
       "igmpSnoopQueryInterval": igmpSnoopQueryInterval,
       "igmpSnoopQueryMaxResponseTime": igmpSnoopQueryMaxResponseTime,
       "igmpSnoopQueryTimeout": igmpSnoopQueryTimeout,
       "igmpSnoopVersion": igmpSnoopVersion,
       "igmpSnoopRouterCurrentTable": igmpSnoopRouterCurrentTable,
       "igmpSnoopRouterCurrentEntry": igmpSnoopRouterCurrentEntry,
       "igmpSnoopRouterCurrentVlanIndex": igmpSnoopRouterCurrentVlanIndex,
       "igmpSnoopRouterCurrentPorts": igmpSnoopRouterCurrentPorts,
       "igmpSnoopRouterStaticTable": igmpSnoopRouterStaticTable,
       "igmpSnoopRouterStaticEntry": igmpSnoopRouterStaticEntry,
       "igmpSnoopRouterStaticVlanIndex": igmpSnoopRouterStaticVlanIndex,
       "igmpSnoopRouterStaticPorts": igmpSnoopRouterStaticPorts,
       "igmpSnoopMulticastCurrentTable": igmpSnoopMulticastCurrentTable,
       "igmpSnoopMulticastCurrentEntry": igmpSnoopMulticastCurrentEntry,
       "igmpSnoopMulticastCurrentVlanIndex": igmpSnoopMulticastCurrentVlanIndex,
       "igmpSnoopMulticastCurrentIpAddress": igmpSnoopMulticastCurrentIpAddress,
       "igmpSnoopMulticastCurrentPorts": igmpSnoopMulticastCurrentPorts,
       "igmpSnoopMulticastStaticTable": igmpSnoopMulticastStaticTable,
       "igmpSnoopMulticastStaticEntry": igmpSnoopMulticastStaticEntry,
       "igmpSnoopMulticastStaticVlanIndex": igmpSnoopMulticastStaticVlanIndex,
       "igmpSnoopMulticastStaticIpAddress": igmpSnoopMulticastStaticIpAddress,
       "igmpSnoopMulticastStaticPorts": igmpSnoopMulticastStaticPorts,
       "ipMgt": ipMgt,
       "ipAddressMode": ipAddressMode,
       "ipDefaultGateway": ipDefaultGateway,
       "ipPrimaryDnsServer": ipPrimaryDnsServer,
       "ipSecondaryDnsServer": ipSecondaryDnsServer,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "ipHttpsState": ipHttpsState,
       "ipHttpsPort": ipHttpsPort,
       "ipTelnetState": ipTelnetState,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormPacketRate": bcastStormPacketRate,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "priorityMgt": priorityMgt,
       "prioWrrTable": prioWrrTable,
       "prioWrrEntry": prioWrrEntry,
       "prioWrrTrafficClass": prioWrrTrafficClass,
       "prioWrrWeight": prioWrrWeight,
       "prioQueueMode": prioQueueMode,
       "trapDestMgt": trapDestMgt,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestAddress": trapDestAddress,
       "trapDestCommunity": trapDestCommunity,
       "trapDestStatus": trapDestStatus,
       "trapDestVersion": trapDestVersion,
       "trapVar": trapVar,
       "trapForbiddenAccessMode": trapForbiddenAccessMode,
       "trapForbiddenAccessIp": trapForbiddenAccessIp,
       "trapLoginUserName": trapLoginUserName,
       "trapConfigSavePartition": trapConfigSavePartition,
       "trapSfpPresenceStatus": trapSfpPresenceStatus,
       "trapInfAlarmVal": trapInfAlarmVal,
       "trapDuplicatedIpVlan": trapDuplicatedIpVlan,
       "trapDuplicatedIpAddress": trapDuplicatedIpAddress,
       "trapDuplicatedIpMacAddress": trapDuplicatedIpMacAddress,
       "trapEapsDomainName": trapEapsDomainName,
       "trapEapsDomainId": trapEapsDomainId,
       "trapEapsStatus": trapEapsStatus,
       "trapTemperature": trapTemperature,
       "trapFuseId": trapFuseId,
       "trapFuseStatus": trapFuseStatus,
       "trapFansBoardPresenceStatus": trapFansBoardPresenceStatus,
       "trapStandbyMpuPresenceStatus": trapStandbyMpuPresenceStatus,
       "trapMacAddressMove": trapMacAddressMove,
       "trapMemFree": trapMemFree,
       "trapBootloaderNew": trapBootloaderNew,
       "trapDevNo": trapDevNo,
       "trapDevLocalId": trapDevLocalId,
       "trapCesopTdmStatus": trapCesopTdmStatus,
       "trapCesopTdmRemoteStatus": trapCesopTdmRemoteStatus,
       "trapCesopTdmCasStatus": trapCesopTdmCasStatus,
       "trapCesopTdmCrcStatus": trapCesopTdmCrcStatus,
       "trapCesopBundleLocalTdmStatus": trapCesopBundleLocalTdmStatus,
       "trapCesopBundleRemoteTdmStatus": trapCesopBundleRemoteTdmStatus,
       "trapCesopBundleLocalStatus": trapCesopBundleLocalStatus,
       "trapCesopBundleRemoteStatus": trapCesopBundleRemoteStatus,
       "trapCesopBundlePktMismatchStatus": trapCesopBundlePktMismatchStatus,
       "trapCesopBundleNextHopStatus": trapCesopBundleNextHopStatus,
       "trapCesopClockAdapLinkQuality": trapCesopClockAdapLinkQuality,
       "trapCesopClockSourceStatus": trapCesopClockSourceStatus,
       "trapBroadcastStormControlStatus": trapBroadcastStormControlStatus,
       "trapBroadcastStormControlPPS": trapBroadcastStormControlPPS,
       "trapMulticastStormControlStatus": trapMulticastStormControlStatus,
       "trapMulticastStormControlPPS": trapMulticastStormControlPPS,
       "trapStatusLDP": trapStatusLDP,
       "trapIdLDP": trapIdLDP,
       "trapStatusTunnelRSVP": trapStatusTunnelRSVP,
       "trapIdTunnelRSVP": trapIdTunnelRSVP,
       "trapPanelStatus": trapPanelStatus,
       "trapLSTGroup": trapLSTGroup,
       "trapMemL3Free": trapMemL3Free,
       "trapActiveMpuNsfId": trapActiveMpuNsfId,
       "trapStandByMpuNsfId": trapStandByMpuNsfId,
       "trapErpsDomainName": trapErpsDomainName,
       "trapErpsDomainId": trapErpsDomainId,
       "trapErpsStatus": trapErpsStatus,
       "trapCfmMdName": trapCfmMdName,
       "trapCfmMaName": trapCfmMaName,
       "trapCfmMepId": trapCfmMepId,
       "trapCfmVlan": trapCfmVlan,
       "trapCfmDefect": trapCfmDefect,
       "trapEvcName": trapEvcName,
       "trapEvcStatus": trapEvcStatus,
       "trapSyncSystemClockStatus": trapSyncSystemClockStatus,
       "trapCesopG704ClockSourceStatus": trapCesopG704ClockSourceStatus,
       "trapSystemWarningsUnits": trapSystemWarningsUnits,
       "trapSensorGroup": trapSensorGroup,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "rlPortInputRate": rlPortInputRate,
       "rlPortInputBurst": rlPortInputBurst,
       "rlPortOutputRate": rlPortOutputRate,
       "rlPortOutputBurst": rlPortOutputBurst,
       "securityMgt": securityMgt,
       "radiusMgt": radiusMgt,
       "radiusServerPortNumber": radiusServerPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "radiusMultipleServerTable": radiusMultipleServerTable,
       "radiusMultipleServerEntry": radiusMultipleServerEntry,
       "radiusMultipleServerIndex": radiusMultipleServerIndex,
       "radiusMultipleServerAddress": radiusMultipleServerAddress,
       "radiusMultipleServerPortNumber": radiusMultipleServerPortNumber,
       "radiusMultipleServerKey": radiusMultipleServerKey,
       "radiusMultipleServerRetransmit": radiusMultipleServerRetransmit,
       "radiusMultipleServerTimeout": radiusMultipleServerTimeout,
       "radiusMultipleServerStatus": radiusMultipleServerStatus,
       "sshMgt": sshMgt,
       "sshServerStatus": sshServerStatus,
       "sshServerMajorVersion": sshServerMajorVersion,
       "sshServerMinorVersion": sshServerMinorVersion,
       "sshTimeout": sshTimeout,
       "sshKeySize": sshKeySize,
       "sshRsaHostKey": sshRsaHostKey,
       "sshDsaHostKey": sshDsaHostKey,
       "sshHostKeyGenAction": sshHostKeyGenAction,
       "sshHostKeyDelAction": sshHostKeyDelAction,
       "ipFilterMgt": ipFilterMgt,
       "ipFilterSnmpTable": ipFilterSnmpTable,
       "ipFilterSnmpEntry": ipFilterSnmpEntry,
       "ipFilterSnmpAddress": ipFilterSnmpAddress,
       "ipFilterSnmpMask": ipFilterSnmpMask,
       "ipFilterSnmpStatus": ipFilterSnmpStatus,
       "ipFilterHTTPTable": ipFilterHTTPTable,
       "ipFilterHTTPEntry": ipFilterHTTPEntry,
       "ipFilterHTTPAddress": ipFilterHTTPAddress,
       "ipFilterHTTPMask": ipFilterHTTPMask,
       "ipFilterHTTPStatus": ipFilterHTTPStatus,
       "ipFilterTelnetTable": ipFilterTelnetTable,
       "ipFilterTelnetEntry": ipFilterTelnetEntry,
       "ipFilterTelnetAddress": ipFilterTelnetAddress,
       "ipFilterTelnetMask": ipFilterTelnetMask,
       "ipFilterTelnetStatus": ipFilterTelnetStatus,
       "ipFilterSSHTable": ipFilterSSHTable,
       "ipFilterSSHEntry": ipFilterSSHEntry,
       "ipFilterSSHAddress": ipFilterSSHAddress,
       "ipFilterSSHMask": ipFilterSSHMask,
       "ipFilterSSHStatus": ipFilterSSHStatus,
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "remoteLogMgt": remoteLogMgt,
       "remoteLogStatus": remoteLogStatus,
       "remoteLogLevel": remoteLogLevel,
       "remoteLogFacilityType": remoteLogFacilityType,
       "remoteLogServerTable": remoteLogServerTable,
       "remoteLogServerEntry": remoteLogServerEntry,
       "remoteLogServerIp": remoteLogServerIp,
       "remoteLogServerStatus": remoteLogServerStatus,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIp": sntpServerIp,
       "sntpServerStatus": sntpServerStatus,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "sysTimeZoneName": sysTimeZoneName,
       "fileMgt": fileMgt,
       "fileInfoTable": fileInfoTable,
       "fileInfoEntry": fileInfoEntry,
       "fileInfoUnitID": fileInfoUnitID,
       "fileInfoFileIndex": fileInfoFileIndex,
       "fileInfoFlashId": fileInfoFlashId,
       "fileInfoFileName": fileInfoFileName,
       "fileInfoFileType": fileInfoFileType,
       "fileInfoIsStartUp": fileInfoIsStartUp,
       "fileInfoFileSize": fileInfoFileSize,
       "fileInfoCreationTime": fileInfoCreationTime,
       "fileInfoDelete": fileInfoDelete,
       "countMgt": countMgt,
       "countHoldPktsTable": countHoldPktsTable,
       "countHoldPktsEntry": countHoldPktsEntry,
       "interfaceNumber": interfaceNumber,
       "countHoldPkts": countHoldPkts,
       "filterCounterMgt": filterCounterMgt,
       "filterCounterInfoTable": filterCounterInfoTable,
       "filterCounterInfoEntry": filterCounterInfoEntry,
       "filterCounterInfoIndex": filterCounterInfoIndex,
       "filterCounterInfoRemark": filterCounterInfoRemark,
       "filterCounterValueTable": filterCounterValueTable,
       "filterCounterValueEntry": filterCounterValueEntry,
       "filterCounterValueIndex": filterCounterValueIndex,
       "filterCounterValue": filterCounterValue,
       "eapsMgt": eapsMgt,
       "eapsInfoTable": eapsInfoTable,
       "eapsInfoEntry": eapsInfoEntry,
       "eapsInfoId": eapsInfoId,
       "eapsInfoName": eapsInfoName,
       "eapsInfoMode": eapsInfoMode,
       "eapsInfoState": eapsInfoState,
       "cfmProbeMgmt": cfmProbeMgmt,
       "cfmProbeDmTable": cfmProbeDmTable,
       "cfmProbeDmEntry": cfmProbeDmEntry,
       "cfmProbeDmIndex": cfmProbeDmIndex,
       "cfmProbeDmAvgDelay": cfmProbeDmAvgDelay,
       "cfmProbeDmAvgJitter": cfmProbeDmAvgJitter,
       "cfmProbeDmLoss": cfmProbeDmLoss,
       "cpumonMgmt": cpumonMgmt,
       "cpuActiveUsageTable": cpuActiveUsageTable,
       "cpuActiveUsageEntry": cpuActiveUsageEntry,
       "cpuActiveUsageIndex": cpuActiveUsageIndex,
       "cpuActiveUsageValue": cpuActiveUsageValue,
       "memActiveUsageTable": memActiveUsageTable,
       "memActiveUsageEntry": memActiveUsageEntry,
       "memActiveUsageIndex": memActiveUsageIndex,
       "memActiveUsageValue": memActiveUsageValue,
       "cpuStandbyUsageTable": cpuStandbyUsageTable,
       "cpuStandbyUsageEntry": cpuStandbyUsageEntry,
       "cpuStandbyUsageIndex": cpuStandbyUsageIndex,
       "cpuStandbyUsageValue": cpuStandbyUsageValue,
       "memStandbyUsageTable": memStandbyUsageTable,
       "memStandbyUsageEntry": memStandbyUsageEntry,
       "memStandbyUsageIndex": memStandbyUsageIndex,
       "memStandbyUsageValue": memStandbyUsageValue,
       "queuePortMgmt": queuePortMgmt,
       "queuePortTable": queuePortTable,
       "queuePortEntry": queuePortEntry,
       "queuePortIfIndex": queuePortIfIndex,
       "queuePortQueueIndex": queuePortQueueIndex,
       "queuePortSentPackets": queuePortSentPackets,
       "queuePortSentBytes": queuePortSentBytes,
       "queuePortDroppedPackets": queuePortDroppedPackets,
       "queuePortDroppedBytes": queuePortDroppedBytes,
       "ddTransceiversMgmt": ddTransceiversMgmt,
       "ddTransceiversTable": ddTransceiversTable,
       "ddTransceiversEntry": ddTransceiversEntry,
       "ddTransceiversIfIndex": ddTransceiversIfIndex,
       "ddTransceiversTemperature": ddTransceiversTemperature,
       "ddTransceiversVcc3v3": ddTransceiversVcc3v3,
       "ddTransceiversRxPower": ddTransceiversRxPower,
       "ddTransceiversTxPower": ddTransceiversTxPower,
       "ddTransceiversTxBias": ddTransceiversTxBias,
       "dmSwitchNotifications": dmSwitchNotifications,
       "dmSwitchTraps": dmSwitchTraps,
       "dmSwitchTrapsPrefix": dmSwitchTrapsPrefix,
       "swLoginFailTrap": swLoginFailTrap,
       "swLoginSucessTrap": swLoginSucessTrap,
       "swStackAttachTrap": swStackAttachTrap,
       "swStackDetachTrap": swStackDetachTrap,
       "swForbiddenAccessTrap": swForbiddenAccessTrap,
       "swSfpPresenceTrap": swSfpPresenceTrap,
       "swConfigChangeTrap": swConfigChangeTrap,
       "swConfigSaveTrap": swConfigSaveTrap,
       "swFanStatusChangeTrap": swFanStatusChangeTrap,
       "swTrapsLostTrap": swTrapsLostTrap,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swAlarmTrap": swAlarmTrap,
       "swDuplicatedIp": swDuplicatedIp,
       "swLoopbackOnPortDetected": swLoopbackOnPortDetected,
       "swLoopbackOnPortNoMoreDetected": swLoopbackOnPortNoMoreDetected,
       "swUnidirLinkDetected": swUnidirLinkDetected,
       "swUnidirLinkRecovered": swUnidirLinkRecovered,
       "swCriticalEventDetected": swCriticalEventDetected,
       "swCriticalEventRecovered": swCriticalEventRecovered,
       "swLinkFlapDetected": swLinkFlapDetected,
       "swLinkFlapNoMoreDetected": swLinkFlapNoMoreDetected,
       "swEapsStatusChange": swEapsStatusChange,
       "swPortSecurityViolation": swPortSecurityViolation,
       "swHighTemperatureDetected": swHighTemperatureDetected,
       "swHighTemperatureNoMoreDetected": swHighTemperatureNoMoreDetected,
       "swFuseStatusChange": swFuseStatusChange,
       "swFansBoardPresenceTrap": swFansBoardPresenceTrap,
       "swStandbyMpuTrap": swStandbyMpuTrap,
       "swNonHomologSfpTrap": swNonHomologSfpTrap,
       "swHighCpuUsageDetected": swHighCpuUsageDetected,
       "swHighCpuUsageNoMoreDetected": swHighCpuUsageNoMoreDetected,
       "swDuplicatedMac": swDuplicatedMac,
       "swHighMemoryUsageDetected": swHighMemoryUsageDetected,
       "swHighMemoryUsageNoMoreDetected": swHighMemoryUsageNoMoreDetected,
       "swNewBootloaderVersion": swNewBootloaderVersion,
       "swCesopTdmStatusTrap": swCesopTdmStatusTrap,
       "swCesopTdmRemoteStatusTrap": swCesopTdmRemoteStatusTrap,
       "swCesopTdmCasStatusTrap": swCesopTdmCasStatusTrap,
       "swCesopTdmCrcStatusTrap": swCesopTdmCrcStatusTrap,
       "swCesopBundleLocalTdmStatusTrap": swCesopBundleLocalTdmStatusTrap,
       "swCesopBundleRemoteTdmStatusTrap": swCesopBundleRemoteTdmStatusTrap,
       "swCesopBundleLocalStatusTrap": swCesopBundleLocalStatusTrap,
       "swCesopBundleRemoteStatusTrap": swCesopBundleRemoteStatusTrap,
       "swCesopBundlePktMismatchTrap": swCesopBundlePktMismatchTrap,
       "swCesopBundleNextHopTrap": swCesopBundleNextHopTrap,
       "swCesopClockAdapLinkQualityTrap": swCesopClockAdapLinkQualityTrap,
       "swCesopClockSourceTrap": swCesopClockSourceTrap,
       "swRemoteDeviceReady": swRemoteDeviceReady,
       "swRemoteDeviceLost": swRemoteDeviceLost,
       "swRemoteDeviceConfigFail": swRemoteDeviceConfigFail,
       "swRemoteDeviceConfigForced": swRemoteDeviceConfigForced,
       "swFanFuseStatusChange": swFanFuseStatusChange,
       "swDyingGaspPackReceived": swDyingGaspPackReceived,
       "swBroadcastStormCheckChange": swBroadcastStormCheckChange,
       "swMulticastStormCheckChange": swMulticastStormCheckChange,
       "swBpduProtectLimit": swBpduProtectLimit,
       "swChangeStatusLDP": swChangeStatusLDP,
       "swChangeStatusTunnelRSVP": swChangeStatusTunnelRSVP,
       "swBpduProtect": swBpduProtect,
       "swRouteTableFull": swRouteTableFull,
       "swPanelStatusTrap": swPanelStatusTrap,
       "swLSTGroupLinkStatusDown": swLSTGroupLinkStatusDown,
       "swLSTGroupLinkStatusUp": swLSTGroupLinkStatusUp,
       "swHighCpuL3UsageDetected": swHighCpuL3UsageDetected,
       "swHighCpuL3UsageNoMoreDetected": swHighCpuL3UsageNoMoreDetected,
       "swHighMemoryL3UsageDetected": swHighMemoryL3UsageDetected,
       "swHighMemoryL3UsageNoMoreDetected": swHighMemoryL3UsageNoMoreDetected,
       "swMpuNsfIdDiffers": swMpuNsfIdDiffers,
       "swErpsStatusChange": swErpsStatusChange,
       "swCfmDefect": swCfmDefect,
       "swLldpRemoteChange": swLldpRemoteChange,
       "swPoeOverCurrent": swPoeOverCurrent,
       "swPoePowerRestriction": swPoePowerRestriction,
       "swCoreDump": swCoreDump,
       "swElmiEvcStatus": swElmiEvcStatus,
       "swSyncSystemClockSwitchHier": swSyncSystemClockSwitchHier,
       "swSyncSystemClockStatus": swSyncSystemClockStatus,
       "swHostTableFull": swHostTableFull,
       "swSyncG704ClockStatus": swSyncG704ClockStatus,
       "swSystemWarningsUnits": swSystemWarningsUnits,
       "swRebootDueToOvertemp": swRebootDueToOvertemp,
       "dmSwitchConformance": dmSwitchConformance}
)
