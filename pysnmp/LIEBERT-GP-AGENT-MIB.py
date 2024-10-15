# SNMP MIB module (LIEBERT-GP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:52 2024
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

(lgpConditionDescription,
 lgpConditionsPresent,
 lgpNetworkName) = mibBuilder.importSymbols(
    "LIEBERT-GP-CONDITIONS-MIB",
    "lgpConditionDescription",
    "lgpConditionsPresent",
    "lgpNetworkName")

(lgpAgentControl,
 lgpAgentDevice,
 lgpAgentIdent,
 lgpAgentNotifications,
 liebertAgentModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpAgentControl",
    "lgpAgentDevice",
    "lgpAgentIdent",
    "lgpAgentNotifications",
    "liebertAgentModuleReg")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

liebertAgentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 2, 1)
)
liebertAgentModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LgpAgentIdentManufacturer_Type(DisplayString):
    """Custom type lgpAgentIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpAgentIdentManufacturer_Type.__name__ = "DisplayString"
_LgpAgentIdentManufacturer_Object = MibScalar
lgpAgentIdentManufacturer = _LgpAgentIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 1),
    _LgpAgentIdentManufacturer_Type()
)
lgpAgentIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentManufacturer.setStatus("current")


class _LgpAgentIdentModel_Type(DisplayString):
    """Custom type lgpAgentIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpAgentIdentModel_Type.__name__ = "DisplayString"
_LgpAgentIdentModel_Object = MibScalar
lgpAgentIdentModel = _LgpAgentIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 2),
    _LgpAgentIdentModel_Type()
)
lgpAgentIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentModel.setStatus("current")


class _LgpAgentIdentFirmwareVersion_Type(DisplayString):
    """Custom type lgpAgentIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LgpAgentIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LgpAgentIdentFirmwareVersion_Object = MibScalar
lgpAgentIdentFirmwareVersion = _LgpAgentIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 3),
    _LgpAgentIdentFirmwareVersion_Type()
)
lgpAgentIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentFirmwareVersion.setStatus("current")


class _LgpAgentIdentSerialNumber_Type(DisplayString):
    """Custom type lgpAgentIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LgpAgentIdentSerialNumber_Type.__name__ = "DisplayString"
_LgpAgentIdentSerialNumber_Object = MibScalar
lgpAgentIdentSerialNumber = _LgpAgentIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 4),
    _LgpAgentIdentSerialNumber_Type()
)
lgpAgentIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentSerialNumber.setStatus("current")


class _LgpAgentIdentPartNumber_Type(DisplayString):
    """Custom type lgpAgentIdentPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpAgentIdentPartNumber_Type.__name__ = "DisplayString"
_LgpAgentIdentPartNumber_Object = MibScalar
lgpAgentIdentPartNumber = _LgpAgentIdentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 5),
    _LgpAgentIdentPartNumber_Type()
)
lgpAgentIdentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentPartNumber.setStatus("current")
_LgpAgentConnectedDeviceCount_Type = Unsigned32
_LgpAgentConnectedDeviceCount_Object = MibScalar
lgpAgentConnectedDeviceCount = _LgpAgentConnectedDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 6),
    _LgpAgentConnectedDeviceCount_Type()
)
lgpAgentConnectedDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentConnectedDeviceCount.setStatus("current")
_LgpAgentEventNotifications_ObjectIdentity = ObjectIdentity
lgpAgentEventNotifications = _LgpAgentEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0)
)
if mibBuilder.loadTexts:
    lgpAgentEventNotifications.setStatus("current")
_LgpAgentManagedDeviceTable_Object = MibTable
lgpAgentManagedDeviceTable = _LgpAgentManagedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lgpAgentManagedDeviceTable.setStatus("current")
_LgpAgentManagedDeviceEntry_Object = MibTableRow
lgpAgentManagedDeviceEntry = _LgpAgentManagedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1)
)
lgpAgentManagedDeviceEntry.setIndexNames(
    (0, "LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex"),
)
if mibBuilder.loadTexts:
    lgpAgentManagedDeviceEntry.setStatus("current")


class _LgpAgentDeviceIndex_Type(Integer32):
    """Custom type lgpAgentDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LgpAgentDeviceIndex_Type.__name__ = "Integer32"
_LgpAgentDeviceIndex_Object = MibTableColumn
lgpAgentDeviceIndex = _LgpAgentDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 1),
    _LgpAgentDeviceIndex_Type()
)
lgpAgentDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceIndex.setStatus("current")
_LgpAgentDeviceId_Type = ObjectIdentifier
_LgpAgentDeviceId_Object = MibTableColumn
lgpAgentDeviceId = _LgpAgentDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 2),
    _LgpAgentDeviceId_Type()
)
lgpAgentDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceId.setStatus("current")


class _LgpAgentDeviceManufacturer_Type(DisplayString):
    """Custom type lgpAgentDeviceManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpAgentDeviceManufacturer_Type.__name__ = "DisplayString"
_LgpAgentDeviceManufacturer_Object = MibTableColumn
lgpAgentDeviceManufacturer = _LgpAgentDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 3),
    _LgpAgentDeviceManufacturer_Type()
)
lgpAgentDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceManufacturer.setStatus("current")


class _LgpAgentDeviceModel_Type(DisplayString):
    """Custom type lgpAgentDeviceModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpAgentDeviceModel_Type.__name__ = "DisplayString"
_LgpAgentDeviceModel_Object = MibTableColumn
lgpAgentDeviceModel = _LgpAgentDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 4),
    _LgpAgentDeviceModel_Type()
)
lgpAgentDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceModel.setStatus("current")


class _LgpAgentDeviceFirmwareVersion_Type(DisplayString):
    """Custom type lgpAgentDeviceFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LgpAgentDeviceFirmwareVersion_Type.__name__ = "DisplayString"
_LgpAgentDeviceFirmwareVersion_Object = MibTableColumn
lgpAgentDeviceFirmwareVersion = _LgpAgentDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 5),
    _LgpAgentDeviceFirmwareVersion_Type()
)
lgpAgentDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceFirmwareVersion.setStatus("current")
_LgpAgentDeviceUnitNumber_Type = Integer32
_LgpAgentDeviceUnitNumber_Object = MibTableColumn
lgpAgentDeviceUnitNumber = _LgpAgentDeviceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 6),
    _LgpAgentDeviceUnitNumber_Type()
)
lgpAgentDeviceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceUnitNumber.setStatus("current")


class _LgpAgentDeviceSerialNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LgpAgentDeviceSerialNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceSerialNumber_Object = MibTableColumn
lgpAgentDeviceSerialNumber = _LgpAgentDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 7),
    _LgpAgentDeviceSerialNumber_Type()
)
lgpAgentDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceSerialNumber.setStatus("current")


class _LgpAgentDeviceManufactureDate_Type(DisplayString):
    """Custom type lgpAgentDeviceManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_LgpAgentDeviceManufactureDate_Type.__name__ = "DisplayString"
_LgpAgentDeviceManufactureDate_Object = MibTableColumn
lgpAgentDeviceManufactureDate = _LgpAgentDeviceManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 8),
    _LgpAgentDeviceManufactureDate_Type()
)
lgpAgentDeviceManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceManufactureDate.setStatus("current")


class _LgpAgentDeviceServiceContact_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceContact_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceContact_Object = MibTableColumn
lgpAgentDeviceServiceContact = _LgpAgentDeviceServiceContact_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 9),
    _LgpAgentDeviceServiceContact_Type()
)
lgpAgentDeviceServiceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceContact.setStatus("current")


class _LgpAgentDeviceServicePhoneNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceServicePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServicePhoneNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceServicePhoneNumber_Object = MibTableColumn
lgpAgentDeviceServicePhoneNumber = _LgpAgentDeviceServicePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 10),
    _LgpAgentDeviceServicePhoneNumber_Type()
)
lgpAgentDeviceServicePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServicePhoneNumber.setStatus("current")


class _LgpAgentDeviceServiceAddrLine1_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine1_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine1_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine1 = _LgpAgentDeviceServiceAddrLine1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 11),
    _LgpAgentDeviceServiceAddrLine1_Type()
)
lgpAgentDeviceServiceAddrLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine1.setStatus("current")


class _LgpAgentDeviceServiceAddrLine2_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine2_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine2_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine2 = _LgpAgentDeviceServiceAddrLine2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 12),
    _LgpAgentDeviceServiceAddrLine2_Type()
)
lgpAgentDeviceServiceAddrLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine2.setStatus("current")


class _LgpAgentDeviceServiceAddrLine3_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine3_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine3_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine3 = _LgpAgentDeviceServiceAddrLine3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 13),
    _LgpAgentDeviceServiceAddrLine3_Type()
)
lgpAgentDeviceServiceAddrLine3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine3.setStatus("current")


class _LgpAgentDeviceServiceAddrLine4_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine4_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine4_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine4 = _LgpAgentDeviceServiceAddrLine4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 14),
    _LgpAgentDeviceServiceAddrLine4_Type()
)
lgpAgentDeviceServiceAddrLine4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine4.setStatus("current")


class _LgpAgentDeviceUnitName_Type(DisplayString):
    """Custom type lgpAgentDeviceUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceUnitName_Type.__name__ = "DisplayString"
_LgpAgentDeviceUnitName_Object = MibTableColumn
lgpAgentDeviceUnitName = _LgpAgentDeviceUnitName_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 15),
    _LgpAgentDeviceUnitName_Type()
)
lgpAgentDeviceUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceUnitName.setStatus("current")


class _LgpAgentDeviceSiteIdentifier_Type(DisplayString):
    """Custom type lgpAgentDeviceSiteIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceSiteIdentifier_Type.__name__ = "DisplayString"
_LgpAgentDeviceSiteIdentifier_Object = MibTableColumn
lgpAgentDeviceSiteIdentifier = _LgpAgentDeviceSiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 16),
    _LgpAgentDeviceSiteIdentifier_Type()
)
lgpAgentDeviceSiteIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceSiteIdentifier.setStatus("current")


class _LgpAgentDeviceTagNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceTagNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceTagNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceTagNumber_Object = MibTableColumn
lgpAgentDeviceTagNumber = _LgpAgentDeviceTagNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 17),
    _LgpAgentDeviceTagNumber_Type()
)
lgpAgentDeviceTagNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceTagNumber.setStatus("current")


class _LgpAgentDeviceOrderLine1_Type(DisplayString):
    """Custom type lgpAgentDeviceOrderLine1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceOrderLine1_Type.__name__ = "DisplayString"
_LgpAgentDeviceOrderLine1_Object = MibTableColumn
lgpAgentDeviceOrderLine1 = _LgpAgentDeviceOrderLine1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 18),
    _LgpAgentDeviceOrderLine1_Type()
)
lgpAgentDeviceOrderLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceOrderLine1.setStatus("current")


class _LgpAgentDeviceOrderLine2_Type(DisplayString):
    """Custom type lgpAgentDeviceOrderLine2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceOrderLine2_Type.__name__ = "DisplayString"
_LgpAgentDeviceOrderLine2_Object = MibTableColumn
lgpAgentDeviceOrderLine2 = _LgpAgentDeviceOrderLine2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 19),
    _LgpAgentDeviceOrderLine2_Type()
)
lgpAgentDeviceOrderLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceOrderLine2.setStatus("current")
_LgpAgentReboot_Type = Integer32
_LgpAgentReboot_Object = MibScalar
lgpAgentReboot = _LgpAgentReboot_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5, 1),
    _LgpAgentReboot_Type()
)
lgpAgentReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentReboot.setStatus("current")


class _LgpAgentTelnetEnabled_Type(Integer32):
    """Custom type lgpAgentTelnetEnabled based on Integer32"""
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


_LgpAgentTelnetEnabled_Type.__name__ = "Integer32"
_LgpAgentTelnetEnabled_Object = MibScalar
lgpAgentTelnetEnabled = _LgpAgentTelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5, 2),
    _LgpAgentTelnetEnabled_Type()
)
lgpAgentTelnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentTelnetEnabled.setStatus("current")


class _LgpAgentVelocityServerEnabled_Type(Integer32):
    """Custom type lgpAgentVelocityServerEnabled based on Integer32"""
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


_LgpAgentVelocityServerEnabled_Type.__name__ = "Integer32"
_LgpAgentVelocityServerEnabled_Object = MibScalar
lgpAgentVelocityServerEnabled = _LgpAgentVelocityServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5, 3),
    _LgpAgentVelocityServerEnabled_Type()
)
lgpAgentVelocityServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentVelocityServerEnabled.setStatus("current")


class _LgpAgentWebServerMode_Type(Integer32):
    """Custom type lgpAgentWebServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("http", 1),
          ("https", 2))
    )


_LgpAgentWebServerMode_Type.__name__ = "Integer32"
_LgpAgentWebServerMode_Object = MibScalar
lgpAgentWebServerMode = _LgpAgentWebServerMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5, 4),
    _LgpAgentWebServerMode_Type()
)
lgpAgentWebServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentWebServerMode.setStatus("current")

# Managed Objects groups


# Notification objects

lgpAgentDeviceCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 1)
)
lgpAgentDeviceCommunicationLost.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentDeviceCommunicationLost.setStatus(
        "current"
    )

lgpAgentFirmwareUpdateSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 5)
)
lgpAgentFirmwareUpdateSuccessful.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentFirmwareUpdateSuccessful.setStatus(
        "current"
    )

lgpAgentFirmwareCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 6)
)
lgpAgentFirmwareCorrupt.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentFirmwareCorrupt.setStatus(
        "current"
    )

lgpAgentHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 7)
)
lgpAgentHeartbeat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionsPresent"),
        ("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount"))
)
if mibBuilder.loadTexts:
    lgpAgentHeartbeat.setStatus(
        "current"
    )

lgpAgentDnsLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 8)
)
lgpAgentDnsLookupFailure.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpNetworkName"))
)
if mibBuilder.loadTexts:
    lgpAgentDnsLookupFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-AGENT-MIB",
    **{"liebertAgentModule": liebertAgentModule,
       "lgpAgentIdentManufacturer": lgpAgentIdentManufacturer,
       "lgpAgentIdentModel": lgpAgentIdentModel,
       "lgpAgentIdentFirmwareVersion": lgpAgentIdentFirmwareVersion,
       "lgpAgentIdentSerialNumber": lgpAgentIdentSerialNumber,
       "lgpAgentIdentPartNumber": lgpAgentIdentPartNumber,
       "lgpAgentConnectedDeviceCount": lgpAgentConnectedDeviceCount,
       "lgpAgentEventNotifications": lgpAgentEventNotifications,
       "lgpAgentDeviceCommunicationLost": lgpAgentDeviceCommunicationLost,
       "lgpAgentFirmwareUpdateSuccessful": lgpAgentFirmwareUpdateSuccessful,
       "lgpAgentFirmwareCorrupt": lgpAgentFirmwareCorrupt,
       "lgpAgentHeartbeat": lgpAgentHeartbeat,
       "lgpAgentDnsLookupFailure": lgpAgentDnsLookupFailure,
       "lgpAgentManagedDeviceTable": lgpAgentManagedDeviceTable,
       "lgpAgentManagedDeviceEntry": lgpAgentManagedDeviceEntry,
       "lgpAgentDeviceIndex": lgpAgentDeviceIndex,
       "lgpAgentDeviceId": lgpAgentDeviceId,
       "lgpAgentDeviceManufacturer": lgpAgentDeviceManufacturer,
       "lgpAgentDeviceModel": lgpAgentDeviceModel,
       "lgpAgentDeviceFirmwareVersion": lgpAgentDeviceFirmwareVersion,
       "lgpAgentDeviceUnitNumber": lgpAgentDeviceUnitNumber,
       "lgpAgentDeviceSerialNumber": lgpAgentDeviceSerialNumber,
       "lgpAgentDeviceManufactureDate": lgpAgentDeviceManufactureDate,
       "lgpAgentDeviceServiceContact": lgpAgentDeviceServiceContact,
       "lgpAgentDeviceServicePhoneNumber": lgpAgentDeviceServicePhoneNumber,
       "lgpAgentDeviceServiceAddrLine1": lgpAgentDeviceServiceAddrLine1,
       "lgpAgentDeviceServiceAddrLine2": lgpAgentDeviceServiceAddrLine2,
       "lgpAgentDeviceServiceAddrLine3": lgpAgentDeviceServiceAddrLine3,
       "lgpAgentDeviceServiceAddrLine4": lgpAgentDeviceServiceAddrLine4,
       "lgpAgentDeviceUnitName": lgpAgentDeviceUnitName,
       "lgpAgentDeviceSiteIdentifier": lgpAgentDeviceSiteIdentifier,
       "lgpAgentDeviceTagNumber": lgpAgentDeviceTagNumber,
       "lgpAgentDeviceOrderLine1": lgpAgentDeviceOrderLine1,
       "lgpAgentDeviceOrderLine2": lgpAgentDeviceOrderLine2,
       "lgpAgentReboot": lgpAgentReboot,
       "lgpAgentTelnetEnabled": lgpAgentTelnetEnabled,
       "lgpAgentVelocityServerEnabled": lgpAgentVelocityServerEnabled,
       "lgpAgentWebServerMode": lgpAgentWebServerMode}
)
