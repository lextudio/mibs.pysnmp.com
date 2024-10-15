# SNMP MIB module (SCHLEIFENBAUER-DATABUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCHLEIFENBAUER-DATABUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:02 2024
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

(schleifenbauerMgmt,) = mibBuilder.importSymbols(
    "SCHLEIFENBAUER-SMI",
    "schleifenbauerMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

schleifenbauerDatabusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1)
)
schleifenbauerDatabusMIB.setRevisions(
        ("2016-10-21 00:00",
         "2016-06-16 00:00",
         "2016-05-10 00:00",
         "2016-03-24 00:00",
         "2016-02-19 00:00",
         "2015-10-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DeciValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )



class KiloWattHour(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class DeciAmpere(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )



class DeciCelsius(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9900),
    )



class DeciPercent(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class DeciVolt(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )



class MilliSecond(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class Second(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_SdbMIBNotifications_ObjectIdentity = ObjectIdentity
sdbMIBNotifications = _SdbMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0)
)
_SdbMIBObjects_ObjectIdentity = ObjectIdentity
sdbMIBObjects = _SdbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1)
)
_SdbMgmt_ObjectIdentity = ObjectIdentity
sdbMgmt = _SdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1)
)
_SdbMgmtStatus_ObjectIdentity = ObjectIdentity
sdbMgmtStatus = _SdbMgmtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1)
)


class _SdbMgmtStsDevices_Type(Integer32):
    """Custom type sdbMgmtStsDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SdbMgmtStsDevices_Type.__name__ = "Integer32"
_SdbMgmtStsDevices_Object = MibScalar
sdbMgmtStsDevices = _SdbMgmtStsDevices_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 1),
    _SdbMgmtStsDevices_Type()
)
sdbMgmtStsDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsDevices.setStatus("current")


class _SdbMgmtStsAddressableDevices_Type(Integer32):
    """Custom type sdbMgmtStsAddressableDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdbMgmtStsAddressableDevices_Type.__name__ = "Integer32"
_SdbMgmtStsAddressableDevices_Object = MibScalar
sdbMgmtStsAddressableDevices = _SdbMgmtStsAddressableDevices_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 2),
    _SdbMgmtStsAddressableDevices_Type()
)
sdbMgmtStsAddressableDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsAddressableDevices.setStatus("current")


class _SdbMgmtStsNewDevices_Type(Integer32):
    """Custom type sdbMgmtStsNewDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdbMgmtStsNewDevices_Type.__name__ = "Integer32"
_SdbMgmtStsNewDevices_Object = MibScalar
sdbMgmtStsNewDevices = _SdbMgmtStsNewDevices_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 3),
    _SdbMgmtStsNewDevices_Type()
)
sdbMgmtStsNewDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsNewDevices.setStatus("current")


class _SdbMgmtStsDuplicateDevices_Type(Integer32):
    """Custom type sdbMgmtStsDuplicateDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdbMgmtStsDuplicateDevices_Type.__name__ = "Integer32"
_SdbMgmtStsDuplicateDevices_Object = MibScalar
sdbMgmtStsDuplicateDevices = _SdbMgmtStsDuplicateDevices_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 4),
    _SdbMgmtStsDuplicateDevices_Type()
)
sdbMgmtStsDuplicateDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsDuplicateDevices.setStatus("current")


class _SdbMgmtStsRingState_Type(Integer32):
    """Custom type sdbMgmtStsRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_SdbMgmtStsRingState_Type.__name__ = "Integer32"
_SdbMgmtStsRingState_Object = MibScalar
sdbMgmtStsRingState = _SdbMgmtStsRingState_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 5),
    _SdbMgmtStsRingState_Type()
)
sdbMgmtStsRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsRingState.setStatus("current")


class _SdbMgmtStsRingBreachIndex_Type(Integer32):
    """Custom type sdbMgmtStsRingBreachIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbMgmtStsRingBreachIndex_Type.__name__ = "Integer32"
_SdbMgmtStsRingBreachIndex_Object = MibScalar
sdbMgmtStsRingBreachIndex = _SdbMgmtStsRingBreachIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 1, 6),
    _SdbMgmtStsRingBreachIndex_Type()
)
sdbMgmtStsRingBreachIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtStsRingBreachIndex.setStatus("current")
_SdbMgmtControl_ObjectIdentity = ObjectIdentity
sdbMgmtControl = _SdbMgmtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2)
)


class _SdbMgmtCtrlScan_Type(Integer32):
    """Custom type sdbMgmtCtrlScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("scan", 1))
    )


_SdbMgmtCtrlScan_Type.__name__ = "Integer32"
_SdbMgmtCtrlScan_Object = MibScalar
sdbMgmtCtrlScan = _SdbMgmtCtrlScan_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 1),
    _SdbMgmtCtrlScan_Type()
)
sdbMgmtCtrlScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbMgmtCtrlScan.setStatus("current")


class _SdbMgmtCtrlRenumberAllFromN_Type(Integer32):
    """Custom type sdbMgmtCtrlRenumberAllFromN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbMgmtCtrlRenumberAllFromN_Type.__name__ = "Integer32"
_SdbMgmtCtrlRenumberAllFromN_Object = MibScalar
sdbMgmtCtrlRenumberAllFromN = _SdbMgmtCtrlRenumberAllFromN_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 2),
    _SdbMgmtCtrlRenumberAllFromN_Type()
)
sdbMgmtCtrlRenumberAllFromN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbMgmtCtrlRenumberAllFromN.setStatus("current")


class _SdbMgmtCtrlRenumberZeros_Type(Integer32):
    """Custom type sdbMgmtCtrlRenumberZeros based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("renumber", 1))
    )


_SdbMgmtCtrlRenumberZeros_Type.__name__ = "Integer32"
_SdbMgmtCtrlRenumberZeros_Object = MibScalar
sdbMgmtCtrlRenumberZeros = _SdbMgmtCtrlRenumberZeros_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 3),
    _SdbMgmtCtrlRenumberZeros_Type()
)
sdbMgmtCtrlRenumberZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbMgmtCtrlRenumberZeros.setStatus("current")
_SdbMgmtCtrlDevicesTable_Object = MibTable
sdbMgmtCtrlDevicesTable = _SdbMgmtCtrlDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevicesTable.setStatus("current")
_SdbMgmtCtrlDevicesEntry_Object = MibTableRow
sdbMgmtCtrlDevicesEntry = _SdbMgmtCtrlDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1)
)
sdbMgmtCtrlDevicesEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlDevIndex"),
)
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevicesEntry.setStatus("current")


class _SdbMgmtCtrlDevIndex_Type(Integer32):
    """Custom type sdbMgmtCtrlDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdbMgmtCtrlDevIndex_Type.__name__ = "Integer32"
_SdbMgmtCtrlDevIndex_Object = MibTableColumn
sdbMgmtCtrlDevIndex = _SdbMgmtCtrlDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1, 1),
    _SdbMgmtCtrlDevIndex_Type()
)
sdbMgmtCtrlDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevIndex.setStatus("current")


class _SdbMgmtCtrlDevUnitAddress_Type(Integer32):
    """Custom type sdbMgmtCtrlDevUnitAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbMgmtCtrlDevUnitAddress_Type.__name__ = "Integer32"
_SdbMgmtCtrlDevUnitAddress_Object = MibTableColumn
sdbMgmtCtrlDevUnitAddress = _SdbMgmtCtrlDevUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1, 2),
    _SdbMgmtCtrlDevUnitAddress_Type()
)
sdbMgmtCtrlDevUnitAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevUnitAddress.setStatus("current")


class _SdbMgmtCtrlDevHardwareAddress_Type(DisplayString):
    """Custom type sdbMgmtCtrlDevHardwareAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_SdbMgmtCtrlDevHardwareAddress_Type.__name__ = "DisplayString"
_SdbMgmtCtrlDevHardwareAddress_Object = MibTableColumn
sdbMgmtCtrlDevHardwareAddress = _SdbMgmtCtrlDevHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1, 3),
    _SdbMgmtCtrlDevHardwareAddress_Type()
)
sdbMgmtCtrlDevHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevHardwareAddress.setStatus("current")


class _SdbMgmtCtrlDevIsNew_Type(Integer32):
    """Custom type sdbMgmtCtrlDevIsNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SdbMgmtCtrlDevIsNew_Type.__name__ = "Integer32"
_SdbMgmtCtrlDevIsNew_Object = MibTableColumn
sdbMgmtCtrlDevIsNew = _SdbMgmtCtrlDevIsNew_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1, 4),
    _SdbMgmtCtrlDevIsNew_Type()
)
sdbMgmtCtrlDevIsNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevIsNew.setStatus("current")


class _SdbMgmtCtrlDevIsDuplicate_Type(Integer32):
    """Custom type sdbMgmtCtrlDevIsDuplicate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SdbMgmtCtrlDevIsDuplicate_Type.__name__ = "Integer32"
_SdbMgmtCtrlDevIsDuplicate_Object = MibTableColumn
sdbMgmtCtrlDevIsDuplicate = _SdbMgmtCtrlDevIsDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 1, 2, 4, 1, 5),
    _SdbMgmtCtrlDevIsDuplicate_Type()
)
sdbMgmtCtrlDevIsDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbMgmtCtrlDevIsDuplicate.setStatus("current")
_SdbDevice_ObjectIdentity = ObjectIdentity
sdbDevice = _SdbDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2)
)
_SdbDevIdentification_ObjectIdentity = ObjectIdentity
sdbDevIdentification = _SdbDevIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1)
)
_SdbDevIdTable_Object = MibTable
sdbDevIdTable = _SdbDevIdTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sdbDevIdTable.setStatus("current")
_SdbDevIdEntry_Object = MibTableRow
sdbDevIdEntry = _SdbDevIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1)
)
sdbDevIdEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevIdEntry.setStatus("current")


class _SdbDevIdSPDMVersion_Type(Integer32):
    """Custom type sdbDevIdSPDMVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SdbDevIdSPDMVersion_Type.__name__ = "Integer32"
_SdbDevIdSPDMVersion_Object = MibTableColumn
sdbDevIdSPDMVersion = _SdbDevIdSPDMVersion_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 1),
    _SdbDevIdSPDMVersion_Type()
)
sdbDevIdSPDMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdSPDMVersion.setStatus("current")


class _SdbDevIdFirmwareVersion_Type(Integer32):
    """Custom type sdbDevIdFirmwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SdbDevIdFirmwareVersion_Type.__name__ = "Integer32"
_SdbDevIdFirmwareVersion_Object = MibTableColumn
sdbDevIdFirmwareVersion = _SdbDevIdFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 2),
    _SdbDevIdFirmwareVersion_Type()
)
sdbDevIdFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdFirmwareVersion.setStatus("current")


class _SdbDevIdBuildNumber_Type(DisplayString):
    """Custom type sdbDevIdBuildNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SdbDevIdBuildNumber_Type.__name__ = "DisplayString"
_SdbDevIdBuildNumber_Object = MibTableColumn
sdbDevIdBuildNumber = _SdbDevIdBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 3),
    _SdbDevIdBuildNumber_Type()
)
sdbDevIdBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdBuildNumber.setStatus("current")


class _SdbDevIdSalesOrderNumber_Type(DisplayString):
    """Custom type sdbDevIdSalesOrderNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdbDevIdSalesOrderNumber_Type.__name__ = "DisplayString"
_SdbDevIdSalesOrderNumber_Object = MibTableColumn
sdbDevIdSalesOrderNumber = _SdbDevIdSalesOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 4),
    _SdbDevIdSalesOrderNumber_Type()
)
sdbDevIdSalesOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdSalesOrderNumber.setStatus("current")


class _SdbDevIdProductId_Type(DisplayString):
    """Custom type sdbDevIdProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdbDevIdProductId_Type.__name__ = "DisplayString"
_SdbDevIdProductId_Object = MibTableColumn
sdbDevIdProductId = _SdbDevIdProductId_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 5),
    _SdbDevIdProductId_Type()
)
sdbDevIdProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdProductId.setStatus("current")


class _SdbDevIdSerialNumber_Type(DisplayString):
    """Custom type sdbDevIdSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdbDevIdSerialNumber_Type.__name__ = "DisplayString"
_SdbDevIdSerialNumber_Object = MibTableColumn
sdbDevIdSerialNumber = _SdbDevIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 6),
    _SdbDevIdSerialNumber_Type()
)
sdbDevIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdSerialNumber.setStatus("current")


class _SdbDevIdHardwareAddress_Type(DisplayString):
    """Custom type sdbDevIdHardwareAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_SdbDevIdHardwareAddress_Type.__name__ = "DisplayString"
_SdbDevIdHardwareAddress_Object = MibTableColumn
sdbDevIdHardwareAddress = _SdbDevIdHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 7),
    _SdbDevIdHardwareAddress_Type()
)
sdbDevIdHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdHardwareAddress.setStatus("current")


class _SdbDevIdMacAddress_Type(DisplayString):
    """Custom type sdbDevIdMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_SdbDevIdMacAddress_Type.__name__ = "DisplayString"
_SdbDevIdMacAddress_Object = MibTableColumn
sdbDevIdMacAddress = _SdbDevIdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 8),
    _SdbDevIdMacAddress_Type()
)
sdbDevIdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevIdMacAddress.setStatus("current")


class _SdbDevIdUnitAddress_Type(Integer32):
    """Custom type sdbDevIdUnitAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbDevIdUnitAddress_Type.__name__ = "Integer32"
_SdbDevIdUnitAddress_Object = MibTableColumn
sdbDevIdUnitAddress = _SdbDevIdUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 9),
    _SdbDevIdUnitAddress_Type()
)
sdbDevIdUnitAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevIdUnitAddress.setStatus("current")


class _SdbDevIdName_Type(DisplayString):
    """Custom type sdbDevIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdbDevIdName_Type.__name__ = "DisplayString"
_SdbDevIdName_Object = MibTableColumn
sdbDevIdName = _SdbDevIdName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 10),
    _SdbDevIdName_Type()
)
sdbDevIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevIdName.setStatus("current")


class _SdbDevIdLocation_Type(DisplayString):
    """Custom type sdbDevIdLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdbDevIdLocation_Type.__name__ = "DisplayString"
_SdbDevIdLocation_Object = MibTableColumn
sdbDevIdLocation = _SdbDevIdLocation_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 11),
    _SdbDevIdLocation_Type()
)
sdbDevIdLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevIdLocation.setStatus("current")


class _SdbDevIdVanityTag_Type(DisplayString):
    """Custom type sdbDevIdVanityTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SdbDevIdVanityTag_Type.__name__ = "DisplayString"
_SdbDevIdVanityTag_Object = MibTableColumn
sdbDevIdVanityTag = _SdbDevIdVanityTag_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 12),
    _SdbDevIdVanityTag_Type()
)
sdbDevIdVanityTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevIdVanityTag.setStatus("current")


class _SdbDevIdIndex_Type(Integer32):
    """Custom type sdbDevIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SdbDevIdIndex_Type.__name__ = "Integer32"
_SdbDevIdIndex_Object = MibTableColumn
sdbDevIdIndex = _SdbDevIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 1, 1, 1, 13),
    _SdbDevIdIndex_Type()
)
sdbDevIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevIdIndex.setStatus("current")
_SdbDevConfiguration_ObjectIdentity = ObjectIdentity
sdbDevConfiguration = _SdbDevConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2)
)
_SdbDevCfTable_Object = MibTable
sdbDevCfTable = _SdbDevCfTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sdbDevCfTable.setStatus("current")
_SdbDevCfEntry_Object = MibTableRow
sdbDevCfEntry = _SdbDevCfEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1)
)
sdbDevCfEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevCfEntry.setStatus("current")


class _SdbDevCfPhases_Type(Integer32):
    """Custom type sdbDevCfPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(3, 3),
    )


_SdbDevCfPhases_Type.__name__ = "Integer32"
_SdbDevCfPhases_Object = MibTableColumn
sdbDevCfPhases = _SdbDevCfPhases_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 1),
    _SdbDevCfPhases_Type()
)
sdbDevCfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfPhases.setStatus("current")


class _SdbDevCfOutletsTotal_Type(Integer32):
    """Custom type sdbDevCfOutletsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevCfOutletsTotal_Type.__name__ = "Integer32"
_SdbDevCfOutletsTotal_Object = MibTableColumn
sdbDevCfOutletsTotal = _SdbDevCfOutletsTotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 2),
    _SdbDevCfOutletsTotal_Type()
)
sdbDevCfOutletsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfOutletsTotal.setStatus("current")


class _SdbDevCfOutletsSwitched_Type(Integer32):
    """Custom type sdbDevCfOutletsSwitched based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevCfOutletsSwitched_Type.__name__ = "Integer32"
_SdbDevCfOutletsSwitched_Object = MibTableColumn
sdbDevCfOutletsSwitched = _SdbDevCfOutletsSwitched_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 3),
    _SdbDevCfOutletsSwitched_Type()
)
sdbDevCfOutletsSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfOutletsSwitched.setStatus("current")


class _SdbDevCfOutletsMetered_Type(Integer32):
    """Custom type sdbDevCfOutletsMetered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevCfOutletsMetered_Type.__name__ = "Integer32"
_SdbDevCfOutletsMetered_Object = MibTableColumn
sdbDevCfOutletsMetered = _SdbDevCfOutletsMetered_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 4),
    _SdbDevCfOutletsMetered_Type()
)
sdbDevCfOutletsMetered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfOutletsMetered.setStatus("current")


class _SdbDevCfSensors_Type(Integer32):
    """Custom type sdbDevCfSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SdbDevCfSensors_Type.__name__ = "Integer32"
_SdbDevCfSensors_Object = MibTableColumn
sdbDevCfSensors = _SdbDevCfSensors_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 5),
    _SdbDevCfSensors_Type()
)
sdbDevCfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfSensors.setStatus("current")


class _SdbDevCfMaximumLoad_Type(Integer32):
    """Custom type sdbDevCfMaximumLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
    )


_SdbDevCfMaximumLoad_Type.__name__ = "Integer32"
_SdbDevCfMaximumLoad_Object = MibTableColumn
sdbDevCfMaximumLoad = _SdbDevCfMaximumLoad_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 2, 1, 1, 6),
    _SdbDevCfMaximumLoad_Type()
)
sdbDevCfMaximumLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevCfMaximumLoad.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevCfMaximumLoad.setUnits("A")
_SdbDevSystemStatus_ObjectIdentity = ObjectIdentity
sdbDevSystemStatus = _SdbDevSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3)
)
_SdbDevSsTable_Object = MibTable
sdbDevSsTable = _SdbDevSsTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sdbDevSsTable.setStatus("current")
_SdbDevSsEntry_Object = MibTableRow
sdbDevSsEntry = _SdbDevSsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1)
)
sdbDevSsEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevSsEntry.setStatus("current")


class _SdbDevSsDeviceStatusCode_Type(Integer32):
    """Custom type sdbDevSsDeviceStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdbDevSsDeviceStatusCode_Type.__name__ = "Integer32"
_SdbDevSsDeviceStatusCode_Object = MibTableColumn
sdbDevSsDeviceStatusCode = _SdbDevSsDeviceStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 1),
    _SdbDevSsDeviceStatusCode_Type()
)
sdbDevSsDeviceStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsDeviceStatusCode.setStatus("current")


class _SdbDevSsTemperatureAlert_Type(Integer32):
    """Custom type sdbDevSsTemperatureAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SdbDevSsTemperatureAlert_Type.__name__ = "Integer32"
_SdbDevSsTemperatureAlert_Object = MibTableColumn
sdbDevSsTemperatureAlert = _SdbDevSsTemperatureAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 2),
    _SdbDevSsTemperatureAlert_Type()
)
sdbDevSsTemperatureAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsTemperatureAlert.setStatus("current")


class _SdbDevSsInputCurrentAlert_Type(Integer32):
    """Custom type sdbDevSsInputCurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SdbDevSsInputCurrentAlert_Type.__name__ = "Integer32"
_SdbDevSsInputCurrentAlert_Object = MibTableColumn
sdbDevSsInputCurrentAlert = _SdbDevSsInputCurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 3),
    _SdbDevSsInputCurrentAlert_Type()
)
sdbDevSsInputCurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsInputCurrentAlert.setStatus("current")


class _SdbDevSsOutletCurrentAlert_Type(Integer32):
    """Custom type sdbDevSsOutletCurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevSsOutletCurrentAlert_Type.__name__ = "Integer32"
_SdbDevSsOutletCurrentAlert_Object = MibTableColumn
sdbDevSsOutletCurrentAlert = _SdbDevSsOutletCurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 4),
    _SdbDevSsOutletCurrentAlert_Type()
)
sdbDevSsOutletCurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsOutletCurrentAlert.setStatus("current")


class _SdbDevSsInputVoltageAlert_Type(Integer32):
    """Custom type sdbDevSsInputVoltageAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SdbDevSsInputVoltageAlert_Type.__name__ = "Integer32"
_SdbDevSsInputVoltageAlert_Object = MibTableColumn
sdbDevSsInputVoltageAlert = _SdbDevSsInputVoltageAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 5),
    _SdbDevSsInputVoltageAlert_Type()
)
sdbDevSsInputVoltageAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsInputVoltageAlert.setStatus("current")


class _SdbDevSsOutletCurrentDropAlert_Type(Integer32):
    """Custom type sdbDevSsOutletCurrentDropAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevSsOutletCurrentDropAlert_Type.__name__ = "Integer32"
_SdbDevSsOutletCurrentDropAlert_Object = MibTableColumn
sdbDevSsOutletCurrentDropAlert = _SdbDevSsOutletCurrentDropAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 6),
    _SdbDevSsOutletCurrentDropAlert_Type()
)
sdbDevSsOutletCurrentDropAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsOutletCurrentDropAlert.setStatus("current")


class _SdbDevSsInputCurrentDropAlert_Type(Integer32):
    """Custom type sdbDevSsInputCurrentDropAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SdbDevSsInputCurrentDropAlert_Type.__name__ = "Integer32"
_SdbDevSsInputCurrentDropAlert_Object = MibTableColumn
sdbDevSsInputCurrentDropAlert = _SdbDevSsInputCurrentDropAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 7),
    _SdbDevSsInputCurrentDropAlert_Type()
)
sdbDevSsInputCurrentDropAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsInputCurrentDropAlert.setStatus("current")


class _SdbDevSsSensorChangeAlert_Type(Integer32):
    """Custom type sdbDevSsSensorChangeAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SdbDevSsSensorChangeAlert_Type.__name__ = "Integer32"
_SdbDevSsSensorChangeAlert_Object = MibTableColumn
sdbDevSsSensorChangeAlert = _SdbDevSsSensorChangeAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 8),
    _SdbDevSsSensorChangeAlert_Type()
)
sdbDevSsSensorChangeAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsSensorChangeAlert.setStatus("current")


class _SdbDevSsOutletVoltageDropAlert_Type(Integer32):
    """Custom type sdbDevSsOutletVoltageDropAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SdbDevSsOutletVoltageDropAlert_Type.__name__ = "Integer32"
_SdbDevSsOutletVoltageDropAlert_Object = MibTableColumn
sdbDevSsOutletVoltageDropAlert = _SdbDevSsOutletVoltageDropAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 3, 1, 1, 9),
    _SdbDevSsOutletVoltageDropAlert_Type()
)
sdbDevSsOutletVoltageDropAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSsOutletVoltageDropAlert.setStatus("current")
_SdbDevReset_ObjectIdentity = ObjectIdentity
sdbDevReset = _SdbDevReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4)
)
_SdbDevRsTable_Object = MibTable
sdbDevRsTable = _SdbDevRsTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sdbDevRsTable.setStatus("current")
_SdbDevRsEntry_Object = MibTableRow
sdbDevRsEntry = _SdbDevRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1)
)
sdbDevRsEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevRsEntry.setStatus("current")


class _SdbDevRsReboot_Type(Integer32):
    """Custom type sdbDevRsReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reboot", 1))
    )


_SdbDevRsReboot_Type.__name__ = "Integer32"
_SdbDevRsReboot_Object = MibTableColumn
sdbDevRsReboot = _SdbDevRsReboot_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1, 1),
    _SdbDevRsReboot_Type()
)
sdbDevRsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevRsReboot.setStatus("current")


class _SdbDevRsResetAlerts_Type(Integer32):
    """Custom type sdbDevRsResetAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reset", 1))
    )


_SdbDevRsResetAlerts_Type.__name__ = "Integer32"
_SdbDevRsResetAlerts_Object = MibTableColumn
sdbDevRsResetAlerts = _SdbDevRsResetAlerts_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1, 2),
    _SdbDevRsResetAlerts_Type()
)
sdbDevRsResetAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevRsResetAlerts.setStatus("current")


class _SdbDevRsZeroInputKWhSubtotal_Type(Integer32):
    """Custom type sdbDevRsZeroInputKWhSubtotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("zero", 1))
    )


_SdbDevRsZeroInputKWhSubtotal_Type.__name__ = "Integer32"
_SdbDevRsZeroInputKWhSubtotal_Object = MibTableColumn
sdbDevRsZeroInputKWhSubtotal = _SdbDevRsZeroInputKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1, 3),
    _SdbDevRsZeroInputKWhSubtotal_Type()
)
sdbDevRsZeroInputKWhSubtotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevRsZeroInputKWhSubtotal.setStatus("current")


class _SdbDevRsZeroOutletKWhSubtotal_Type(Integer32):
    """Custom type sdbDevRsZeroOutletKWhSubtotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("zero", 1))
    )


_SdbDevRsZeroOutletKWhSubtotal_Type.__name__ = "Integer32"
_SdbDevRsZeroOutletKWhSubtotal_Object = MibTableColumn
sdbDevRsZeroOutletKWhSubtotal = _SdbDevRsZeroOutletKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1, 4),
    _SdbDevRsZeroOutletKWhSubtotal_Type()
)
sdbDevRsZeroOutletKWhSubtotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevRsZeroOutletKWhSubtotal.setStatus("current")


class _SdbDevRsResetPeaksAndDips_Type(Integer32):
    """Custom type sdbDevRsResetPeaksAndDips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reset", 1))
    )


_SdbDevRsResetPeaksAndDips_Type.__name__ = "Integer32"
_SdbDevRsResetPeaksAndDips_Object = MibTableColumn
sdbDevRsResetPeaksAndDips = _SdbDevRsResetPeaksAndDips_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 4, 1, 1, 5),
    _SdbDevRsResetPeaksAndDips_Type()
)
sdbDevRsResetPeaksAndDips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevRsResetPeaksAndDips.setStatus("current")
_SdbDevSettings_ObjectIdentity = ObjectIdentity
sdbDevSettings = _SdbDevSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5)
)
_SdbDevStTable_Object = MibTable
sdbDevStTable = _SdbDevStTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sdbDevStTable.setStatus("current")
_SdbDevStEntry_Object = MibTableRow
sdbDevStEntry = _SdbDevStEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1)
)
sdbDevStEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevStEntry.setStatus("current")


class _SdbDevStAutoResetAlerts_Type(Integer32):
    """Custom type sdbDevStAutoResetAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbDevStAutoResetAlerts_Type.__name__ = "Integer32"
_SdbDevStAutoResetAlerts_Object = MibTableColumn
sdbDevStAutoResetAlerts = _SdbDevStAutoResetAlerts_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 2),
    _SdbDevStAutoResetAlerts_Type()
)
sdbDevStAutoResetAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStAutoResetAlerts.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevStAutoResetAlerts.setUnits("seconds")


class _SdbDevStExtendedNames_Type(Integer32):
    """Custom type sdbDevStExtendedNames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SdbDevStExtendedNames_Type.__name__ = "Integer32"
_SdbDevStExtendedNames_Object = MibTableColumn
sdbDevStExtendedNames = _SdbDevStExtendedNames_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 3),
    _SdbDevStExtendedNames_Type()
)
sdbDevStExtendedNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStExtendedNames.setStatus("current")


class _SdbDevStPeakDuration_Type(MilliSecond):
    """Custom type sdbDevStPeakDuration based on MilliSecond"""
    subtypeSpec = MilliSecond.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbDevStPeakDuration_Type.__name__ = "MilliSecond"
_SdbDevStPeakDuration_Object = MibTableColumn
sdbDevStPeakDuration = _SdbDevStPeakDuration_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 4),
    _SdbDevStPeakDuration_Type()
)
sdbDevStPeakDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStPeakDuration.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevStPeakDuration.setUnits("ms")


class _SdbDevStFixedOutletDelay_Type(MilliSecond):
    """Custom type sdbDevStFixedOutletDelay based on MilliSecond"""
    subtypeSpec = MilliSecond.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_SdbDevStFixedOutletDelay_Type.__name__ = "MilliSecond"
_SdbDevStFixedOutletDelay_Object = MibTableColumn
sdbDevStFixedOutletDelay = _SdbDevStFixedOutletDelay_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 5),
    _SdbDevStFixedOutletDelay_Type()
)
sdbDevStFixedOutletDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStFixedOutletDelay.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevStFixedOutletDelay.setUnits("ms")


class _SdbDevStPowerSaverMode_Type(Second):
    """Custom type sdbDevStPowerSaverMode based on Second"""
    subtypeSpec = Second.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(240, 240),
    )


_SdbDevStPowerSaverMode_Type.__name__ = "Second"
_SdbDevStPowerSaverMode_Object = MibTableColumn
sdbDevStPowerSaverMode = _SdbDevStPowerSaverMode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 6),
    _SdbDevStPowerSaverMode_Type()
)
sdbDevStPowerSaverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStPowerSaverMode.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevStPowerSaverMode.setUnits("s")


class _SdbDevStOutletPowerUpMode_Type(Integer32):
    """Custom type sdbDevStOutletPowerUpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("sameState", 1),
          ("sameStateDelayed", 2))
    )


_SdbDevStOutletPowerUpMode_Type.__name__ = "Integer32"
_SdbDevStOutletPowerUpMode_Object = MibTableColumn
sdbDevStOutletPowerUpMode = _SdbDevStOutletPowerUpMode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 7),
    _SdbDevStOutletPowerUpMode_Type()
)
sdbDevStOutletPowerUpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStOutletPowerUpMode.setStatus("current")


class _SdbDevStMaximumTemperature_Type(Integer32):
    """Custom type sdbDevStMaximumTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SdbDevStMaximumTemperature_Type.__name__ = "Integer32"
_SdbDevStMaximumTemperature_Object = MibTableColumn
sdbDevStMaximumTemperature = _SdbDevStMaximumTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 8),
    _SdbDevStMaximumTemperature_Type()
)
sdbDevStMaximumTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStMaximumTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevStMaximumTemperature.setUnits("degrees Celsius")


class _SdbDevStDisplayOrientation_Type(Integer32):
    """Custom type sdbDevStDisplayOrientation based on Integer32"""
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
        *(("horizontalDisplayAtLeft", 3),
          ("horizontalDisplayAtRight", 4),
          ("noDisplay", 0),
          ("verticalDisplayOnTop", 1),
          ("verticalDisplayUpsideDown", 2))
    )


_SdbDevStDisplayOrientation_Type.__name__ = "Integer32"
_SdbDevStDisplayOrientation_Object = MibTableColumn
sdbDevStDisplayOrientation = _SdbDevStDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 9),
    _SdbDevStDisplayOrientation_Type()
)
sdbDevStDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStDisplayOrientation.setStatus("current")


class _SdbDevStLocalAlertReset_Type(Integer32):
    """Custom type sdbDevStLocalAlertReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("notAllowed", 0))
    )


_SdbDevStLocalAlertReset_Type.__name__ = "Integer32"
_SdbDevStLocalAlertReset_Object = MibTableColumn
sdbDevStLocalAlertReset = _SdbDevStLocalAlertReset_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 10),
    _SdbDevStLocalAlertReset_Type()
)
sdbDevStLocalAlertReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStLocalAlertReset.setStatus("current")


class _SdbDevStCurrentDropDetection_Type(Integer32):
    """Custom type sdbDevStCurrentDropDetection based on Integer32"""
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
        *(("inputsAndOutlets", 3),
          ("inputsOnly", 1),
          ("off", 0),
          ("outletsOnly", 2))
    )


_SdbDevStCurrentDropDetection_Type.__name__ = "Integer32"
_SdbDevStCurrentDropDetection_Object = MibTableColumn
sdbDevStCurrentDropDetection = _SdbDevStCurrentDropDetection_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 5, 1, 1, 11),
    _SdbDevStCurrentDropDetection_Type()
)
sdbDevStCurrentDropDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevStCurrentDropDetection.setStatus("current")
_SdbDevInput_ObjectIdentity = ObjectIdentity
sdbDevInput = _SdbDevInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6)
)
_SdbDevInTable_Object = MibTable
sdbDevInTable = _SdbDevInTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sdbDevInTable.setStatus("current")
_SdbDevInEntry_Object = MibTableRow
sdbDevInEntry = _SdbDevInEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1)
)
sdbDevInEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInIndex"),
)
if mibBuilder.loadTexts:
    sdbDevInEntry.setStatus("current")


class _SdbDevInIndex_Type(Integer32):
    """Custom type sdbDevInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SdbDevInIndex_Type.__name__ = "Integer32"
_SdbDevInIndex_Object = MibTableColumn
sdbDevInIndex = _SdbDevInIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 1),
    _SdbDevInIndex_Type()
)
sdbDevInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevInIndex.setStatus("current")
_SdbDevInKWhTotal_Type = KiloWattHour
_SdbDevInKWhTotal_Object = MibTableColumn
sdbDevInKWhTotal = _SdbDevInKWhTotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 2),
    _SdbDevInKWhTotal_Type()
)
sdbDevInKWhTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInKWhTotal.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInKWhTotal.setUnits("kWh")
_SdbDevInKWhSubtotal_Type = KiloWattHour
_SdbDevInKWhSubtotal_Object = MibTableColumn
sdbDevInKWhSubtotal = _SdbDevInKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 3),
    _SdbDevInKWhSubtotal_Type()
)
sdbDevInKWhSubtotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInKWhSubtotal.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInKWhSubtotal.setUnits("kWh")
_SdbDevInPowerFactor_Type = DeciPercent
_SdbDevInPowerFactor_Object = MibTableColumn
sdbDevInPowerFactor = _SdbDevInPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 4),
    _SdbDevInPowerFactor_Type()
)
sdbDevInPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInPowerFactor.setUnits("%")
_SdbDevInActualCurrent_Type = DeciAmpere
_SdbDevInActualCurrent_Object = MibTableColumn
sdbDevInActualCurrent = _SdbDevInActualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 5),
    _SdbDevInActualCurrent_Type()
)
sdbDevInActualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInActualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInActualCurrent.setUnits("A")
_SdbDevInPeakCurrent_Type = DeciAmpere
_SdbDevInPeakCurrent_Object = MibTableColumn
sdbDevInPeakCurrent = _SdbDevInPeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 6),
    _SdbDevInPeakCurrent_Type()
)
sdbDevInPeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInPeakCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInPeakCurrent.setUnits("A")
_SdbDevInActualVoltage_Type = DeciVolt
_SdbDevInActualVoltage_Object = MibTableColumn
sdbDevInActualVoltage = _SdbDevInActualVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 7),
    _SdbDevInActualVoltage_Type()
)
sdbDevInActualVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInActualVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInActualVoltage.setUnits("V")
_SdbDevInMinVoltage_Type = DeciVolt
_SdbDevInMinVoltage_Object = MibTableColumn
sdbDevInMinVoltage = _SdbDevInMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 8),
    _SdbDevInMinVoltage_Type()
)
sdbDevInMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInMinVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInMinVoltage.setUnits("V")


class _SdbDevInPowerVoltAmpere_Type(Integer32):
    """Custom type sdbDevInPowerVoltAmpere based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )


_SdbDevInPowerVoltAmpere_Type.__name__ = "Integer32"
_SdbDevInPowerVoltAmpere_Object = MibTableColumn
sdbDevInPowerVoltAmpere = _SdbDevInPowerVoltAmpere_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 9),
    _SdbDevInPowerVoltAmpere_Type()
)
sdbDevInPowerVoltAmpere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInPowerVoltAmpere.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInPowerVoltAmpere.setUnits("VA")


class _SdbDevInPowerWatt_Type(Integer32):
    """Custom type sdbDevInPowerWatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )


_SdbDevInPowerWatt_Type.__name__ = "Integer32"
_SdbDevInPowerWatt_Object = MibTableColumn
sdbDevInPowerWatt = _SdbDevInPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 10),
    _SdbDevInPowerWatt_Type()
)
sdbDevInPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevInPowerWatt.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInPowerWatt.setUnits("W")
_SdbDevInMaxAmps_Type = DeciAmpere
_SdbDevInMaxAmps_Object = MibTableColumn
sdbDevInMaxAmps = _SdbDevInMaxAmps_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 11),
    _SdbDevInMaxAmps_Type()
)
sdbDevInMaxAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevInMaxAmps.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevInMaxAmps.setUnits("A")


class _SdbDevInCTRatio_Type(Integer32):
    """Custom type sdbDevInCTRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdbDevInCTRatio_Type.__name__ = "Integer32"
_SdbDevInCTRatio_Object = MibTableColumn
sdbDevInCTRatio = _SdbDevInCTRatio_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 12),
    _SdbDevInCTRatio_Type()
)
sdbDevInCTRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevInCTRatio.setStatus("current")


class _SdbDevInName_Type(DisplayString):
    """Custom type sdbDevInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SdbDevInName_Type.__name__ = "DisplayString"
_SdbDevInName_Object = MibTableColumn
sdbDevInName = _SdbDevInName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 13),
    _SdbDevInName_Type()
)
sdbDevInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevInName.setStatus("current")


class _SdbDevInZeroKWhSubtotal_Type(Integer32):
    """Custom type sdbDevInZeroKWhSubtotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("zero", 1))
    )


_SdbDevInZeroKWhSubtotal_Type.__name__ = "Integer32"
_SdbDevInZeroKWhSubtotal_Object = MibTableColumn
sdbDevInZeroKWhSubtotal = _SdbDevInZeroKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 6, 1, 1, 14),
    _SdbDevInZeroKWhSubtotal_Type()
)
sdbDevInZeroKWhSubtotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevInZeroKWhSubtotal.setStatus("current")
_SdbDevOutlet_ObjectIdentity = ObjectIdentity
sdbDevOutlet = _SdbDevOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7)
)
_SdbDevOutTable_Object = MibTable
sdbDevOutTable = _SdbDevOutTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sdbDevOutTable.setStatus("current")
_SdbDevOutEntry_Object = MibTableRow
sdbDevOutEntry = _SdbDevOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 1, 1)
)
sdbDevOutEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutIndex"),
)
if mibBuilder.loadTexts:
    sdbDevOutEntry.setStatus("current")


class _SdbDevOutIndex_Type(Integer32):
    """Custom type sdbDevOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SdbDevOutIndex_Type.__name__ = "Integer32"
_SdbDevOutIndex_Object = MibTableColumn
sdbDevOutIndex = _SdbDevOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 1, 1, 1),
    _SdbDevOutIndex_Type()
)
sdbDevOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevOutIndex.setStatus("current")


class _SdbDevOutName_Type(DisplayString):
    """Custom type sdbDevOutName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SdbDevOutName_Type.__name__ = "DisplayString"
_SdbDevOutName_Object = MibTableColumn
sdbDevOutName = _SdbDevOutName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 1, 1, 2),
    _SdbDevOutName_Type()
)
sdbDevOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutName.setStatus("current")
_SdbDevOutMtTable_Object = MibTable
sdbDevOutMtTable = _SdbDevOutMtTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    sdbDevOutMtTable.setStatus("current")
_SdbDevOutMtEntry_Object = MibTableRow
sdbDevOutMtEntry = _SdbDevOutMtEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1)
)
sdbDevOutMtEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtIndex"),
)
if mibBuilder.loadTexts:
    sdbDevOutMtEntry.setStatus("current")


class _SdbDevOutMtIndex_Type(Integer32):
    """Custom type sdbDevOutMtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SdbDevOutMtIndex_Type.__name__ = "Integer32"
_SdbDevOutMtIndex_Object = MibTableColumn
sdbDevOutMtIndex = _SdbDevOutMtIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 1),
    _SdbDevOutMtIndex_Type()
)
sdbDevOutMtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevOutMtIndex.setStatus("current")
_SdbDevOutMtKWhTotal_Type = KiloWattHour
_SdbDevOutMtKWhTotal_Object = MibTableColumn
sdbDevOutMtKWhTotal = _SdbDevOutMtKWhTotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 2),
    _SdbDevOutMtKWhTotal_Type()
)
sdbDevOutMtKWhTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtKWhTotal.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtKWhTotal.setUnits("kWh")
_SdbDevOutMtKWhSubtotal_Type = KiloWattHour
_SdbDevOutMtKWhSubtotal_Object = MibTableColumn
sdbDevOutMtKWhSubtotal = _SdbDevOutMtKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 3),
    _SdbDevOutMtKWhSubtotal_Type()
)
sdbDevOutMtKWhSubtotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtKWhSubtotal.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtKWhSubtotal.setUnits("kWh")
_SdbDevOutMtPowerFactor_Type = DeciPercent
_SdbDevOutMtPowerFactor_Object = MibTableColumn
sdbDevOutMtPowerFactor = _SdbDevOutMtPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 4),
    _SdbDevOutMtPowerFactor_Type()
)
sdbDevOutMtPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerFactor.setUnits("%")
_SdbDevOutMtActualCurrent_Type = DeciAmpere
_SdbDevOutMtActualCurrent_Object = MibTableColumn
sdbDevOutMtActualCurrent = _SdbDevOutMtActualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 5),
    _SdbDevOutMtActualCurrent_Type()
)
sdbDevOutMtActualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtActualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtActualCurrent.setUnits("A")
_SdbDevOutMtPeakCurrent_Type = DeciAmpere
_SdbDevOutMtPeakCurrent_Object = MibTableColumn
sdbDevOutMtPeakCurrent = _SdbDevOutMtPeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 6),
    _SdbDevOutMtPeakCurrent_Type()
)
sdbDevOutMtPeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtPeakCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtPeakCurrent.setUnits("A")
_SdbDevOutMtActualVoltage_Type = DeciVolt
_SdbDevOutMtActualVoltage_Object = MibTableColumn
sdbDevOutMtActualVoltage = _SdbDevOutMtActualVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 7),
    _SdbDevOutMtActualVoltage_Type()
)
sdbDevOutMtActualVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtActualVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtActualVoltage.setUnits("V")
_SdbDevOutMtMaxAmps_Type = DeciAmpere
_SdbDevOutMtMaxAmps_Object = MibTableColumn
sdbDevOutMtMaxAmps = _SdbDevOutMtMaxAmps_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 8),
    _SdbDevOutMtMaxAmps_Type()
)
sdbDevOutMtMaxAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutMtMaxAmps.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtMaxAmps.setUnits("A")


class _SdbDevOutMtCTRatio_Type(Integer32):
    """Custom type sdbDevOutMtCTRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdbDevOutMtCTRatio_Type.__name__ = "Integer32"
_SdbDevOutMtCTRatio_Object = MibTableColumn
sdbDevOutMtCTRatio = _SdbDevOutMtCTRatio_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 9),
    _SdbDevOutMtCTRatio_Type()
)
sdbDevOutMtCTRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutMtCTRatio.setStatus("current")


class _SdbDevOutMtPowerVoltAmpere_Type(Integer32):
    """Custom type sdbDevOutMtPowerVoltAmpere based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )


_SdbDevOutMtPowerVoltAmpere_Type.__name__ = "Integer32"
_SdbDevOutMtPowerVoltAmpere_Object = MibTableColumn
sdbDevOutMtPowerVoltAmpere = _SdbDevOutMtPowerVoltAmpere_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 10),
    _SdbDevOutMtPowerVoltAmpere_Type()
)
sdbDevOutMtPowerVoltAmpere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerVoltAmpere.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerVoltAmpere.setUnits("VA")


class _SdbDevOutMtPowerWatt_Type(Integer32):
    """Custom type sdbDevOutMtPowerWatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )


_SdbDevOutMtPowerWatt_Type.__name__ = "Integer32"
_SdbDevOutMtPowerWatt_Object = MibTableColumn
sdbDevOutMtPowerWatt = _SdbDevOutMtPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 2, 1, 11),
    _SdbDevOutMtPowerWatt_Type()
)
sdbDevOutMtPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerWatt.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutMtPowerWatt.setUnits("W")
_SdbDevOutSwTable_Object = MibTable
sdbDevOutSwTable = _SdbDevOutSwTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    sdbDevOutSwTable.setStatus("current")
_SdbDevOutSwEntry_Object = MibTableRow
sdbDevOutSwEntry = _SdbDevOutSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1)
)
sdbDevOutSwEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwIndex"),
)
if mibBuilder.loadTexts:
    sdbDevOutSwEntry.setStatus("current")


class _SdbDevOutSwIndex_Type(Integer32):
    """Custom type sdbDevOutSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SdbDevOutSwIndex_Type.__name__ = "Integer32"
_SdbDevOutSwIndex_Object = MibTableColumn
sdbDevOutSwIndex = _SdbDevOutSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 1),
    _SdbDevOutSwIndex_Type()
)
sdbDevOutSwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevOutSwIndex.setStatus("current")


class _SdbDevOutSwCurrentState_Type(Integer32):
    """Custom type sdbDevOutSwCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SdbDevOutSwCurrentState_Type.__name__ = "Integer32"
_SdbDevOutSwCurrentState_Object = MibTableColumn
sdbDevOutSwCurrentState = _SdbDevOutSwCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 2),
    _SdbDevOutSwCurrentState_Type()
)
sdbDevOutSwCurrentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutSwCurrentState.setStatus("current")


class _SdbDevOutSwScheduled_Type(Integer32):
    """Custom type sdbDevOutSwScheduled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("scheduled", 1))
    )


_SdbDevOutSwScheduled_Type.__name__ = "Integer32"
_SdbDevOutSwScheduled_Object = MibTableColumn
sdbDevOutSwScheduled = _SdbDevOutSwScheduled_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 3),
    _SdbDevOutSwScheduled_Type()
)
sdbDevOutSwScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevOutSwScheduled.setStatus("current")


class _SdbDevOutSwUnlock_Type(Integer32):
    """Custom type sdbDevOutSwUnlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_SdbDevOutSwUnlock_Type.__name__ = "Integer32"
_SdbDevOutSwUnlock_Object = MibTableColumn
sdbDevOutSwUnlock = _SdbDevOutSwUnlock_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 4),
    _SdbDevOutSwUnlock_Type()
)
sdbDevOutSwUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutSwUnlock.setStatus("current")


class _SdbDevOutSwIndividualOutletDelay_Type(Second):
    """Custom type sdbDevOutSwIndividualOutletDelay based on Second"""
    subtypeSpec = Second.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdbDevOutSwIndividualOutletDelay_Type.__name__ = "Second"
_SdbDevOutSwIndividualOutletDelay_Object = MibTableColumn
sdbDevOutSwIndividualOutletDelay = _SdbDevOutSwIndividualOutletDelay_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 5),
    _SdbDevOutSwIndividualOutletDelay_Type()
)
sdbDevOutSwIndividualOutletDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutSwIndividualOutletDelay.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevOutSwIndividualOutletDelay.setUnits("s")


class _SdbDevOutSwReboot_Type(Integer32):
    """Custom type sdbDevOutSwReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reboot", 1))
    )


_SdbDevOutSwReboot_Type.__name__ = "Integer32"
_SdbDevOutSwReboot_Object = MibTableColumn
sdbDevOutSwReboot = _SdbDevOutSwReboot_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 7, 3, 1, 6),
    _SdbDevOutSwReboot_Type()
)
sdbDevOutSwReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevOutSwReboot.setStatus("current")
_SdbDevSensor_ObjectIdentity = ObjectIdentity
sdbDevSensor = _SdbDevSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8)
)
_SdbDevMeasuresTable_Object = MibTable
sdbDevMeasuresTable = _SdbDevMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    sdbDevMeasuresTable.setStatus("current")
_SdbDevMeasuresEntry_Object = MibTableRow
sdbDevMeasuresEntry = _SdbDevMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1, 1)
)
sdbDevMeasuresEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
)
if mibBuilder.loadTexts:
    sdbDevMeasuresEntry.setStatus("current")
_SdbDevMsIntTemperature_Type = DeciCelsius
_SdbDevMsIntTemperature_Object = MibTableColumn
sdbDevMsIntTemperature = _SdbDevMsIntTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1, 1, 1),
    _SdbDevMsIntTemperature_Type()
)
sdbDevMsIntTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevMsIntTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevMsIntTemperature.setUnits("degrees Celsius")
_SdbDevMsExtTemperature_Type = DeciCelsius
_SdbDevMsExtTemperature_Object = MibTableColumn
sdbDevMsExtTemperature = _SdbDevMsExtTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1, 1, 2),
    _SdbDevMsExtTemperature_Type()
)
sdbDevMsExtTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevMsExtTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevMsExtTemperature.setUnits("degrees Celsius")
_SdbDevMsIntTemperaturePeak_Type = DeciCelsius
_SdbDevMsIntTemperaturePeak_Object = MibTableColumn
sdbDevMsIntTemperaturePeak = _SdbDevMsIntTemperaturePeak_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1, 1, 3),
    _SdbDevMsIntTemperaturePeak_Type()
)
sdbDevMsIntTemperaturePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevMsIntTemperaturePeak.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevMsIntTemperaturePeak.setUnits("degrees Celsius")
_SdbDevMsExtTemperaturePeak_Type = DeciCelsius
_SdbDevMsExtTemperaturePeak_Object = MibTableColumn
sdbDevMsExtTemperaturePeak = _SdbDevMsExtTemperaturePeak_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 1, 1, 4),
    _SdbDevMsExtTemperaturePeak_Type()
)
sdbDevMsExtTemperaturePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevMsExtTemperaturePeak.setStatus("current")
if mibBuilder.loadTexts:
    sdbDevMsExtTemperaturePeak.setUnits("degrees Celsius")
_SdbDevSnsTable_Object = MibTable
sdbDevSnsTable = _SdbDevSnsTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    sdbDevSnsTable.setStatus("current")
_SdbDevSnsEntry_Object = MibTableRow
sdbDevSnsEntry = _SdbDevSnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2, 1)
)
sdbDevSnsEntry.setIndexNames(
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdIndex"),
    (0, "SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSnsIndex"),
)
if mibBuilder.loadTexts:
    sdbDevSnsEntry.setStatus("current")


class _SdbDevSnsIndex_Type(Integer32):
    """Custom type sdbDevSnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SdbDevSnsIndex_Type.__name__ = "Integer32"
_SdbDevSnsIndex_Object = MibTableColumn
sdbDevSnsIndex = _SdbDevSnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2, 1, 1),
    _SdbDevSnsIndex_Type()
)
sdbDevSnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdbDevSnsIndex.setStatus("current")


class _SdbDevSnsType_Type(DisplayString):
    """Custom type sdbDevSnsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdbDevSnsType_Type.__name__ = "DisplayString"
_SdbDevSnsType_Object = MibTableColumn
sdbDevSnsType = _SdbDevSnsType_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2, 1, 2),
    _SdbDevSnsType_Type()
)
sdbDevSnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSnsType.setStatus("current")


class _SdbDevSnsValue_Type(DeciValue):
    """Custom type sdbDevSnsValue based on DeciValue"""
    subtypeSpec = DeciValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 327680),
    )


_SdbDevSnsValue_Type.__name__ = "DeciValue"
_SdbDevSnsValue_Object = MibTableColumn
sdbDevSnsValue = _SdbDevSnsValue_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2, 1, 3),
    _SdbDevSnsValue_Type()
)
sdbDevSnsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdbDevSnsValue.setStatus("current")


class _SdbDevSnsName_Type(DisplayString):
    """Custom type sdbDevSnsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SdbDevSnsName_Type.__name__ = "DisplayString"
_SdbDevSnsName_Object = MibTableColumn
sdbDevSnsName = _SdbDevSnsName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 1, 2, 8, 2, 1, 4),
    _SdbDevSnsName_Type()
)
sdbDevSnsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdbDevSnsName.setStatus("current")
_SdbMIBConformance_ObjectIdentity = ObjectIdentity
sdbMIBConformance = _SdbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2)
)
_SdbMIBCompliances_ObjectIdentity = ObjectIdentity
sdbMIBCompliances = _SdbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 1)
)
_SdbMIBGroups_ObjectIdentity = ObjectIdentity
sdbMIBGroups = _SdbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2)
)

# Managed Objects groups

sdbMIBDevIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 3)
)
sdbMIBDevIdGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdSPDMVersion"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdFirmwareVersion"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdSalesOrderNumber"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdProductId"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdSerialNumber"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdHardwareAddress"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdUnitAddress"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdName"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdLocation"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdVanityTag"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdMacAddress"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevIdBuildNumber"))
)
if mibBuilder.loadTexts:
    sdbMIBDevIdGroup.setStatus("current")

sdbMIBDevCfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 4)
)
sdbMIBDevCfGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfPhases"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfOutletsTotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfOutletsSwitched"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfOutletsMetered"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfMaximumLoad"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevCfSensors"))
)
if mibBuilder.loadTexts:
    sdbMIBDevCfGroup.setStatus("current")

sdbMIBDevSsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 5)
)
sdbMIBDevSsGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsDeviceStatusCode"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsTemperatureAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputCurrentAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletCurrentAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputVoltageAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletCurrentDropAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputCurrentDropAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsSensorChangeAlert"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletVoltageDropAlert"))
)
if mibBuilder.loadTexts:
    sdbMIBDevSsGroup.setStatus("current")

sdbMIBDevRsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 6)
)
sdbMIBDevRsGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevRsResetAlerts"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevRsResetPeaksAndDips"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevRsReboot"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevRsZeroInputKWhSubtotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevRsZeroOutletKWhSubtotal"))
)
if mibBuilder.loadTexts:
    sdbMIBDevRsGroup.setStatus("current")

sdbMIBDevStGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 7)
)
sdbMIBDevStGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStAutoResetAlerts"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStExtendedNames"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStPeakDuration"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStLocalAlertReset"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStFixedOutletDelay"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStPowerSaverMode"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStOutletPowerUpMode"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStMaximumTemperature"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStDisplayOrientation"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevStCurrentDropDetection"))
)
if mibBuilder.loadTexts:
    sdbMIBDevStGroup.setStatus("current")

sdbMIBDevInGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 8)
)
sdbMIBDevInGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInKWhTotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInKWhSubtotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInPowerFactor"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInActualCurrent"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInPeakCurrent"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInActualVoltage"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInMinVoltage"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInPowerVoltAmpere"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInPowerWatt"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInMaxAmps"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInCTRatio"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInName"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevInZeroKWhSubtotal"))
)
if mibBuilder.loadTexts:
    sdbMIBDevInGroup.setStatus("current")

sdbMIBDevOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 9)
)
sdbMIBDevOutGroup.setObjects(
    ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutName")
)
if mibBuilder.loadTexts:
    sdbMIBDevOutGroup.setStatus("current")

sdbMIBDevOutMtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 10)
)
sdbMIBDevOutMtGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtKWhTotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtKWhSubtotal"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtPowerFactor"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtActualCurrent"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtPeakCurrent"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtActualVoltage"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtMaxAmps"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtCTRatio"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtPowerVoltAmpere"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutMtPowerWatt"))
)
if mibBuilder.loadTexts:
    sdbMIBDevOutMtGroup.setStatus("current")

sdbMIBDevOutSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 11)
)
sdbMIBDevOutSwGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwCurrentState"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwScheduled"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwUnlock"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwIndividualOutletDelay"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevOutSwReboot"))
)
if mibBuilder.loadTexts:
    sdbMIBDevOutSwGroup.setStatus("current")

sdbMIBDevSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 12)
)
sdbMIBDevSensorGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSnsType"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSnsValue"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSnsName"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevMsIntTemperature"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevMsExtTemperature"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevMsIntTemperaturePeak"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevMsExtTemperaturePeak"))
)
if mibBuilder.loadTexts:
    sdbMIBDevSensorGroup.setStatus("current")

sdbMIBMgmtStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 13)
)
sdbMIBMgmtStatusGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsDevices"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsAddressableDevices"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsNewDevices"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsDuplicateDevices"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsRingState"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsRingBreachIndex"))
)
if mibBuilder.loadTexts:
    sdbMIBMgmtStatusGroup.setStatus("current")

sdbMIBMgmtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 14)
)
sdbMIBMgmtControlGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlScan"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlRenumberAllFromN"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlRenumberZeros"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlDevUnitAddress"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlDevHardwareAddress"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlDevIsNew"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtCtrlDevIsDuplicate"))
)
if mibBuilder.loadTexts:
    sdbMIBMgmtControlGroup.setStatus("current")


# Notification objects

sdbDevSsDeviceStatusCodeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 1)
)
if mibBuilder.loadTexts:
    sdbDevSsDeviceStatusCodeChanged.setStatus(
        "current"
    )

sdbDevSsTemperatureAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 2)
)
if mibBuilder.loadTexts:
    sdbDevSsTemperatureAlertDetected.setStatus(
        "current"
    )

sdbDevSsInputCurrentAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 3)
)
if mibBuilder.loadTexts:
    sdbDevSsInputCurrentAlertDetected.setStatus(
        "current"
    )

sdbDevSsOutletCurrentAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 4)
)
if mibBuilder.loadTexts:
    sdbDevSsOutletCurrentAlertDetected.setStatus(
        "current"
    )

sdbDevSsInputVoltageAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 5)
)
if mibBuilder.loadTexts:
    sdbDevSsInputVoltageAlertDetected.setStatus(
        "current"
    )

sdbDevSsOutletCurrentDropAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 6)
)
if mibBuilder.loadTexts:
    sdbDevSsOutletCurrentDropAlertDetected.setStatus(
        "current"
    )

sdbDevSsInputCurrentDropAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 7)
)
if mibBuilder.loadTexts:
    sdbDevSsInputCurrentDropAlertDetected.setStatus(
        "current"
    )

sdbDevSsSensorChangeAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 8)
)
if mibBuilder.loadTexts:
    sdbDevSsSensorChangeAlertDetected.setStatus(
        "current"
    )

sdbMgmtStsRingStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 9)
)
if mibBuilder.loadTexts:
    sdbMgmtStsRingStateChanged.setStatus(
        "current"
    )

sdbDevSsOutletVoltageDropAlertDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 0, 10)
)
if mibBuilder.loadTexts:
    sdbDevSsOutletVoltageDropAlertDetected.setStatus(
        "current"
    )


# Notifications groups

sdbMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 2, 1)
)
sdbMIBNotificationGroup.setObjects(
      *(("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsDeviceStatusCodeChanged"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsTemperatureAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputCurrentAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletCurrentAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputVoltageAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletCurrentDropAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsInputCurrentDropAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsSensorChangeAlertDetected"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbMgmtStsRingStateChanged"),
        ("SCHLEIFENBAUER-DATABUS-MIB", "sdbDevSsOutletVoltageDropAlertDetected"))
)
if mibBuilder.loadTexts:
    sdbMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sdbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31034, 12, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sdbMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCHLEIFENBAUER-DATABUS-MIB",
    **{"DeciValue": DeciValue,
       "KiloWattHour": KiloWattHour,
       "DeciAmpere": DeciAmpere,
       "DeciCelsius": DeciCelsius,
       "DeciPercent": DeciPercent,
       "DeciVolt": DeciVolt,
       "MilliSecond": MilliSecond,
       "Second": Second,
       "schleifenbauerDatabusMIB": schleifenbauerDatabusMIB,
       "sdbMIBNotifications": sdbMIBNotifications,
       "sdbDevSsDeviceStatusCodeChanged": sdbDevSsDeviceStatusCodeChanged,
       "sdbDevSsTemperatureAlertDetected": sdbDevSsTemperatureAlertDetected,
       "sdbDevSsInputCurrentAlertDetected": sdbDevSsInputCurrentAlertDetected,
       "sdbDevSsOutletCurrentAlertDetected": sdbDevSsOutletCurrentAlertDetected,
       "sdbDevSsInputVoltageAlertDetected": sdbDevSsInputVoltageAlertDetected,
       "sdbDevSsOutletCurrentDropAlertDetected": sdbDevSsOutletCurrentDropAlertDetected,
       "sdbDevSsInputCurrentDropAlertDetected": sdbDevSsInputCurrentDropAlertDetected,
       "sdbDevSsSensorChangeAlertDetected": sdbDevSsSensorChangeAlertDetected,
       "sdbMgmtStsRingStateChanged": sdbMgmtStsRingStateChanged,
       "sdbDevSsOutletVoltageDropAlertDetected": sdbDevSsOutletVoltageDropAlertDetected,
       "sdbMIBObjects": sdbMIBObjects,
       "sdbMgmt": sdbMgmt,
       "sdbMgmtStatus": sdbMgmtStatus,
       "sdbMgmtStsDevices": sdbMgmtStsDevices,
       "sdbMgmtStsAddressableDevices": sdbMgmtStsAddressableDevices,
       "sdbMgmtStsNewDevices": sdbMgmtStsNewDevices,
       "sdbMgmtStsDuplicateDevices": sdbMgmtStsDuplicateDevices,
       "sdbMgmtStsRingState": sdbMgmtStsRingState,
       "sdbMgmtStsRingBreachIndex": sdbMgmtStsRingBreachIndex,
       "sdbMgmtControl": sdbMgmtControl,
       "sdbMgmtCtrlScan": sdbMgmtCtrlScan,
       "sdbMgmtCtrlRenumberAllFromN": sdbMgmtCtrlRenumberAllFromN,
       "sdbMgmtCtrlRenumberZeros": sdbMgmtCtrlRenumberZeros,
       "sdbMgmtCtrlDevicesTable": sdbMgmtCtrlDevicesTable,
       "sdbMgmtCtrlDevicesEntry": sdbMgmtCtrlDevicesEntry,
       "sdbMgmtCtrlDevIndex": sdbMgmtCtrlDevIndex,
       "sdbMgmtCtrlDevUnitAddress": sdbMgmtCtrlDevUnitAddress,
       "sdbMgmtCtrlDevHardwareAddress": sdbMgmtCtrlDevHardwareAddress,
       "sdbMgmtCtrlDevIsNew": sdbMgmtCtrlDevIsNew,
       "sdbMgmtCtrlDevIsDuplicate": sdbMgmtCtrlDevIsDuplicate,
       "sdbDevice": sdbDevice,
       "sdbDevIdentification": sdbDevIdentification,
       "sdbDevIdTable": sdbDevIdTable,
       "sdbDevIdEntry": sdbDevIdEntry,
       "sdbDevIdSPDMVersion": sdbDevIdSPDMVersion,
       "sdbDevIdFirmwareVersion": sdbDevIdFirmwareVersion,
       "sdbDevIdBuildNumber": sdbDevIdBuildNumber,
       "sdbDevIdSalesOrderNumber": sdbDevIdSalesOrderNumber,
       "sdbDevIdProductId": sdbDevIdProductId,
       "sdbDevIdSerialNumber": sdbDevIdSerialNumber,
       "sdbDevIdHardwareAddress": sdbDevIdHardwareAddress,
       "sdbDevIdMacAddress": sdbDevIdMacAddress,
       "sdbDevIdUnitAddress": sdbDevIdUnitAddress,
       "sdbDevIdName": sdbDevIdName,
       "sdbDevIdLocation": sdbDevIdLocation,
       "sdbDevIdVanityTag": sdbDevIdVanityTag,
       "sdbDevIdIndex": sdbDevIdIndex,
       "sdbDevConfiguration": sdbDevConfiguration,
       "sdbDevCfTable": sdbDevCfTable,
       "sdbDevCfEntry": sdbDevCfEntry,
       "sdbDevCfPhases": sdbDevCfPhases,
       "sdbDevCfOutletsTotal": sdbDevCfOutletsTotal,
       "sdbDevCfOutletsSwitched": sdbDevCfOutletsSwitched,
       "sdbDevCfOutletsMetered": sdbDevCfOutletsMetered,
       "sdbDevCfSensors": sdbDevCfSensors,
       "sdbDevCfMaximumLoad": sdbDevCfMaximumLoad,
       "sdbDevSystemStatus": sdbDevSystemStatus,
       "sdbDevSsTable": sdbDevSsTable,
       "sdbDevSsEntry": sdbDevSsEntry,
       "sdbDevSsDeviceStatusCode": sdbDevSsDeviceStatusCode,
       "sdbDevSsTemperatureAlert": sdbDevSsTemperatureAlert,
       "sdbDevSsInputCurrentAlert": sdbDevSsInputCurrentAlert,
       "sdbDevSsOutletCurrentAlert": sdbDevSsOutletCurrentAlert,
       "sdbDevSsInputVoltageAlert": sdbDevSsInputVoltageAlert,
       "sdbDevSsOutletCurrentDropAlert": sdbDevSsOutletCurrentDropAlert,
       "sdbDevSsInputCurrentDropAlert": sdbDevSsInputCurrentDropAlert,
       "sdbDevSsSensorChangeAlert": sdbDevSsSensorChangeAlert,
       "sdbDevSsOutletVoltageDropAlert": sdbDevSsOutletVoltageDropAlert,
       "sdbDevReset": sdbDevReset,
       "sdbDevRsTable": sdbDevRsTable,
       "sdbDevRsEntry": sdbDevRsEntry,
       "sdbDevRsReboot": sdbDevRsReboot,
       "sdbDevRsResetAlerts": sdbDevRsResetAlerts,
       "sdbDevRsZeroInputKWhSubtotal": sdbDevRsZeroInputKWhSubtotal,
       "sdbDevRsZeroOutletKWhSubtotal": sdbDevRsZeroOutletKWhSubtotal,
       "sdbDevRsResetPeaksAndDips": sdbDevRsResetPeaksAndDips,
       "sdbDevSettings": sdbDevSettings,
       "sdbDevStTable": sdbDevStTable,
       "sdbDevStEntry": sdbDevStEntry,
       "sdbDevStAutoResetAlerts": sdbDevStAutoResetAlerts,
       "sdbDevStExtendedNames": sdbDevStExtendedNames,
       "sdbDevStPeakDuration": sdbDevStPeakDuration,
       "sdbDevStFixedOutletDelay": sdbDevStFixedOutletDelay,
       "sdbDevStPowerSaverMode": sdbDevStPowerSaverMode,
       "sdbDevStOutletPowerUpMode": sdbDevStOutletPowerUpMode,
       "sdbDevStMaximumTemperature": sdbDevStMaximumTemperature,
       "sdbDevStDisplayOrientation": sdbDevStDisplayOrientation,
       "sdbDevStLocalAlertReset": sdbDevStLocalAlertReset,
       "sdbDevStCurrentDropDetection": sdbDevStCurrentDropDetection,
       "sdbDevInput": sdbDevInput,
       "sdbDevInTable": sdbDevInTable,
       "sdbDevInEntry": sdbDevInEntry,
       "sdbDevInIndex": sdbDevInIndex,
       "sdbDevInKWhTotal": sdbDevInKWhTotal,
       "sdbDevInKWhSubtotal": sdbDevInKWhSubtotal,
       "sdbDevInPowerFactor": sdbDevInPowerFactor,
       "sdbDevInActualCurrent": sdbDevInActualCurrent,
       "sdbDevInPeakCurrent": sdbDevInPeakCurrent,
       "sdbDevInActualVoltage": sdbDevInActualVoltage,
       "sdbDevInMinVoltage": sdbDevInMinVoltage,
       "sdbDevInPowerVoltAmpere": sdbDevInPowerVoltAmpere,
       "sdbDevInPowerWatt": sdbDevInPowerWatt,
       "sdbDevInMaxAmps": sdbDevInMaxAmps,
       "sdbDevInCTRatio": sdbDevInCTRatio,
       "sdbDevInName": sdbDevInName,
       "sdbDevInZeroKWhSubtotal": sdbDevInZeroKWhSubtotal,
       "sdbDevOutlet": sdbDevOutlet,
       "sdbDevOutTable": sdbDevOutTable,
       "sdbDevOutEntry": sdbDevOutEntry,
       "sdbDevOutIndex": sdbDevOutIndex,
       "sdbDevOutName": sdbDevOutName,
       "sdbDevOutMtTable": sdbDevOutMtTable,
       "sdbDevOutMtEntry": sdbDevOutMtEntry,
       "sdbDevOutMtIndex": sdbDevOutMtIndex,
       "sdbDevOutMtKWhTotal": sdbDevOutMtKWhTotal,
       "sdbDevOutMtKWhSubtotal": sdbDevOutMtKWhSubtotal,
       "sdbDevOutMtPowerFactor": sdbDevOutMtPowerFactor,
       "sdbDevOutMtActualCurrent": sdbDevOutMtActualCurrent,
       "sdbDevOutMtPeakCurrent": sdbDevOutMtPeakCurrent,
       "sdbDevOutMtActualVoltage": sdbDevOutMtActualVoltage,
       "sdbDevOutMtMaxAmps": sdbDevOutMtMaxAmps,
       "sdbDevOutMtCTRatio": sdbDevOutMtCTRatio,
       "sdbDevOutMtPowerVoltAmpere": sdbDevOutMtPowerVoltAmpere,
       "sdbDevOutMtPowerWatt": sdbDevOutMtPowerWatt,
       "sdbDevOutSwTable": sdbDevOutSwTable,
       "sdbDevOutSwEntry": sdbDevOutSwEntry,
       "sdbDevOutSwIndex": sdbDevOutSwIndex,
       "sdbDevOutSwCurrentState": sdbDevOutSwCurrentState,
       "sdbDevOutSwScheduled": sdbDevOutSwScheduled,
       "sdbDevOutSwUnlock": sdbDevOutSwUnlock,
       "sdbDevOutSwIndividualOutletDelay": sdbDevOutSwIndividualOutletDelay,
       "sdbDevOutSwReboot": sdbDevOutSwReboot,
       "sdbDevSensor": sdbDevSensor,
       "sdbDevMeasuresTable": sdbDevMeasuresTable,
       "sdbDevMeasuresEntry": sdbDevMeasuresEntry,
       "sdbDevMsIntTemperature": sdbDevMsIntTemperature,
       "sdbDevMsExtTemperature": sdbDevMsExtTemperature,
       "sdbDevMsIntTemperaturePeak": sdbDevMsIntTemperaturePeak,
       "sdbDevMsExtTemperaturePeak": sdbDevMsExtTemperaturePeak,
       "sdbDevSnsTable": sdbDevSnsTable,
       "sdbDevSnsEntry": sdbDevSnsEntry,
       "sdbDevSnsIndex": sdbDevSnsIndex,
       "sdbDevSnsType": sdbDevSnsType,
       "sdbDevSnsValue": sdbDevSnsValue,
       "sdbDevSnsName": sdbDevSnsName,
       "sdbMIBConformance": sdbMIBConformance,
       "sdbMIBCompliances": sdbMIBCompliances,
       "sdbMIBCompliance": sdbMIBCompliance,
       "sdbMIBGroups": sdbMIBGroups,
       "sdbMIBNotificationGroup": sdbMIBNotificationGroup,
       "sdbMIBDevIdGroup": sdbMIBDevIdGroup,
       "sdbMIBDevCfGroup": sdbMIBDevCfGroup,
       "sdbMIBDevSsGroup": sdbMIBDevSsGroup,
       "sdbMIBDevRsGroup": sdbMIBDevRsGroup,
       "sdbMIBDevStGroup": sdbMIBDevStGroup,
       "sdbMIBDevInGroup": sdbMIBDevInGroup,
       "sdbMIBDevOutGroup": sdbMIBDevOutGroup,
       "sdbMIBDevOutMtGroup": sdbMIBDevOutMtGroup,
       "sdbMIBDevOutSwGroup": sdbMIBDevOutSwGroup,
       "sdbMIBDevSensorGroup": sdbMIBDevSensorGroup,
       "sdbMIBMgmtStatusGroup": sdbMIBMgmtStatusGroup,
       "sdbMIBMgmtControlGroup": sdbMIBMgmtControlGroup}
)
