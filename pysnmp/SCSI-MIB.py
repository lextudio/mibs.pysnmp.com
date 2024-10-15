# SNMP MIB module (SCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:04 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

scsiMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 139)
)
scsiMIB.setRevisions(
        ("2006-03-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScsiLUN(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(8, 8),
    )



class ScsiIndexValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ScsiPortIndexValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIndexValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 262),
    )



class ScsiName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 262),
    )



class ScsiLuNameOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



class ScsiDeviceOrPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("other", 3),
          ("port", 2))
    )



class ScsiIdCodeSet(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class ScsiIdAssociation(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class ScsiIdType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class ScsiIdValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ScsiHrSWInstalledIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ScsiNotifications_ObjectIdentity = ObjectIdentity
scsiNotifications = _ScsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 0)
)
_ScsiNotificationsPrefix_ObjectIdentity = ObjectIdentity
scsiNotificationsPrefix = _ScsiNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 0, 0)
)
_ScsiAdmin_ObjectIdentity = ObjectIdentity
scsiAdmin = _ScsiAdmin_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1)
)
_ScsiTransportTypes_ObjectIdentity = ObjectIdentity
scsiTransportTypes = _ScsiTransportTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1)
)
_ScsiTransportOther_ObjectIdentity = ObjectIdentity
scsiTransportOther = _ScsiTransportOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 1)
)
if mibBuilder.loadTexts:
    scsiTransportOther.setStatus("current")
_ScsiTransportSPI_ObjectIdentity = ObjectIdentity
scsiTransportSPI = _ScsiTransportSPI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 2)
)
if mibBuilder.loadTexts:
    scsiTransportSPI.setStatus("current")
_ScsiTransportFCP_ObjectIdentity = ObjectIdentity
scsiTransportFCP = _ScsiTransportFCP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 3)
)
if mibBuilder.loadTexts:
    scsiTransportFCP.setStatus("current")
_ScsiTransportSRP_ObjectIdentity = ObjectIdentity
scsiTransportSRP = _ScsiTransportSRP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 4)
)
if mibBuilder.loadTexts:
    scsiTransportSRP.setStatus("current")
_ScsiTransportISCSI_ObjectIdentity = ObjectIdentity
scsiTransportISCSI = _ScsiTransportISCSI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 5)
)
if mibBuilder.loadTexts:
    scsiTransportISCSI.setStatus("current")
_ScsiTransportSBP_ObjectIdentity = ObjectIdentity
scsiTransportSBP = _ScsiTransportSBP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 6)
)
if mibBuilder.loadTexts:
    scsiTransportSBP.setStatus("current")
_ScsiTransportSAS_ObjectIdentity = ObjectIdentity
scsiTransportSAS = _ScsiTransportSAS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 1, 1, 7)
)
if mibBuilder.loadTexts:
    scsiTransportSAS.setStatus("current")
_ScsiObjects_ObjectIdentity = ObjectIdentity
scsiObjects = _ScsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2)
)
_ScsiGeneral_ObjectIdentity = ObjectIdentity
scsiGeneral = _ScsiGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 1)
)
_ScsiInstanceTable_Object = MibTable
scsiInstanceTable = _ScsiInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1)
)
if mibBuilder.loadTexts:
    scsiInstanceTable.setStatus("current")
_ScsiInstanceEntry_Object = MibTableRow
scsiInstanceEntry = _ScsiInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1)
)
scsiInstanceEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
)
if mibBuilder.loadTexts:
    scsiInstanceEntry.setStatus("current")
_ScsiInstIndex_Type = ScsiIndexValue
_ScsiInstIndex_Object = MibTableColumn
scsiInstIndex = _ScsiInstIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 1),
    _ScsiInstIndex_Type()
)
scsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiInstIndex.setStatus("current")


class _ScsiInstAlias_Type(SnmpAdminString):
    """Custom type scsiInstAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiInstAlias_Type.__name__ = "SnmpAdminString"
_ScsiInstAlias_Object = MibTableColumn
scsiInstAlias = _ScsiInstAlias_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 2),
    _ScsiInstAlias_Type()
)
scsiInstAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiInstAlias.setStatus("current")
_ScsiInstSoftwareIndex_Type = ScsiHrSWInstalledIndexOrZero
_ScsiInstSoftwareIndex_Object = MibTableColumn
scsiInstSoftwareIndex = _ScsiInstSoftwareIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 3),
    _ScsiInstSoftwareIndex_Type()
)
scsiInstSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiInstSoftwareIndex.setStatus("current")
_ScsiInstVendorVersion_Type = SnmpAdminString
_ScsiInstVendorVersion_Object = MibTableColumn
scsiInstVendorVersion = _ScsiInstVendorVersion_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 4),
    _ScsiInstVendorVersion_Type()
)
scsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiInstVendorVersion.setStatus("current")


class _ScsiInstScsiNotificationsEnable_Type(TruthValue):
    """Custom type scsiInstScsiNotificationsEnable based on TruthValue"""


_ScsiInstScsiNotificationsEnable_Object = MibTableColumn
scsiInstScsiNotificationsEnable = _ScsiInstScsiNotificationsEnable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 5),
    _ScsiInstScsiNotificationsEnable_Type()
)
scsiInstScsiNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiInstScsiNotificationsEnable.setStatus("current")


class _ScsiInstStorageType_Type(StorageType):
    """Custom type scsiInstStorageType based on StorageType"""


_ScsiInstStorageType_Object = MibTableColumn
scsiInstStorageType = _ScsiInstStorageType_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 1, 1, 6),
    _ScsiInstStorageType_Type()
)
scsiInstStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiInstStorageType.setStatus("current")
_ScsiDeviceTable_Object = MibTable
scsiDeviceTable = _ScsiDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2)
)
if mibBuilder.loadTexts:
    scsiDeviceTable.setStatus("current")
_ScsiDeviceEntry_Object = MibTableRow
scsiDeviceEntry = _ScsiDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2, 1)
)
scsiDeviceEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiDeviceEntry.setStatus("current")
_ScsiDeviceIndex_Type = ScsiIndexValue
_ScsiDeviceIndex_Object = MibTableColumn
scsiDeviceIndex = _ScsiDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2, 1, 1),
    _ScsiDeviceIndex_Type()
)
scsiDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDeviceIndex.setStatus("current")


class _ScsiDeviceAlias_Type(SnmpAdminString):
    """Custom type scsiDeviceAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiDeviceAlias_Type.__name__ = "SnmpAdminString"
_ScsiDeviceAlias_Object = MibTableColumn
scsiDeviceAlias = _ScsiDeviceAlias_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2, 1, 2),
    _ScsiDeviceAlias_Type()
)
scsiDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiDeviceAlias.setStatus("current")


class _ScsiDeviceRole_Type(Bits):
    """Custom type scsiDeviceRole based on Bits"""
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 0))
    )

_ScsiDeviceRole_Type.__name__ = "Bits"
_ScsiDeviceRole_Object = MibTableColumn
scsiDeviceRole = _ScsiDeviceRole_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2, 1, 3),
    _ScsiDeviceRole_Type()
)
scsiDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDeviceRole.setStatus("current")
_ScsiDevicePortNumber_Type = Unsigned32
_ScsiDevicePortNumber_Object = MibTableColumn
scsiDevicePortNumber = _ScsiDevicePortNumber_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 2, 1, 4),
    _ScsiDevicePortNumber_Type()
)
scsiDevicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDevicePortNumber.setStatus("current")
_ScsiPortTable_Object = MibTable
scsiPortTable = _ScsiPortTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3)
)
if mibBuilder.loadTexts:
    scsiPortTable.setStatus("current")
_ScsiPortEntry_Object = MibTableRow
scsiPortEntry = _ScsiPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3, 1)
)
scsiPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiPortEntry.setStatus("current")
_ScsiPortIndex_Type = ScsiIndexValue
_ScsiPortIndex_Object = MibTableColumn
scsiPortIndex = _ScsiPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3, 1, 1),
    _ScsiPortIndex_Type()
)
scsiPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiPortIndex.setStatus("current")


class _ScsiPortRole_Type(Bits):
    """Custom type scsiPortRole based on Bits"""
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 0))
    )

_ScsiPortRole_Type.__name__ = "Bits"
_ScsiPortRole_Object = MibTableColumn
scsiPortRole = _ScsiPortRole_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3, 1, 2),
    _ScsiPortRole_Type()
)
scsiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortRole.setStatus("current")
_ScsiPortTransportPtr_Type = RowPointer
_ScsiPortTransportPtr_Object = MibTableColumn
scsiPortTransportPtr = _ScsiPortTransportPtr_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3, 1, 3),
    _ScsiPortTransportPtr_Type()
)
scsiPortTransportPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortTransportPtr.setStatus("current")
_ScsiPortBusyStatuses_Type = Counter32
_ScsiPortBusyStatuses_Object = MibTableColumn
scsiPortBusyStatuses = _ScsiPortBusyStatuses_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 3, 1, 4),
    _ScsiPortBusyStatuses_Type()
)
scsiPortBusyStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortBusyStatuses.setStatus("current")
_ScsiTransportTable_Object = MibTable
scsiTransportTable = _ScsiTransportTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5)
)
if mibBuilder.loadTexts:
    scsiTransportTable.setStatus("current")
_ScsiTransportEntry_Object = MibTableRow
scsiTransportEntry = _ScsiTransportEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5, 1)
)
scsiTransportEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiTransportIndex"),
)
if mibBuilder.loadTexts:
    scsiTransportEntry.setStatus("current")
_ScsiTransportIndex_Type = ScsiIndexValue
_ScsiTransportIndex_Object = MibTableColumn
scsiTransportIndex = _ScsiTransportIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5, 1, 1),
    _ScsiTransportIndex_Type()
)
scsiTransportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiTransportIndex.setStatus("current")
_ScsiTransportType_Type = AutonomousType
_ScsiTransportType_Object = MibTableColumn
scsiTransportType = _ScsiTransportType_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5, 1, 2),
    _ScsiTransportType_Type()
)
scsiTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTransportType.setStatus("current")
_ScsiTransportPointer_Type = RowPointer
_ScsiTransportPointer_Object = MibTableColumn
scsiTransportPointer = _ScsiTransportPointer_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5, 1, 3),
    _ScsiTransportPointer_Type()
)
scsiTransportPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTransportPointer.setStatus("current")
_ScsiTransportDevName_Type = ScsiName
_ScsiTransportDevName_Object = MibTableColumn
scsiTransportDevName = _ScsiTransportDevName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 1, 5, 1, 4),
    _ScsiTransportDevName_Type()
)
scsiTransportDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTransportDevName.setStatus("current")
_ScsiInitiatorDevice_ObjectIdentity = ObjectIdentity
scsiInitiatorDevice = _ScsiInitiatorDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 2)
)
_ScsiIntrDevTable_Object = MibTable
scsiIntrDevTable = _ScsiIntrDevTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 1)
)
if mibBuilder.loadTexts:
    scsiIntrDevTable.setStatus("current")
_ScsiIntrDevEntry_Object = MibTableRow
scsiIntrDevEntry = _ScsiIntrDevEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 1, 1)
)
scsiIntrDevEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiIntrDevEntry.setStatus("current")


class _ScsiIntrDevTgtAccessMode_Type(Integer32):
    """Custom type scsiIntrDevTgtAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoEnable", 2),
          ("manualEnable", 3),
          ("unknown", 1))
    )


_ScsiIntrDevTgtAccessMode_Type.__name__ = "Integer32"
_ScsiIntrDevTgtAccessMode_Object = MibTableColumn
scsiIntrDevTgtAccessMode = _ScsiIntrDevTgtAccessMode_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 1, 1, 1),
    _ScsiIntrDevTgtAccessMode_Type()
)
scsiIntrDevTgtAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiIntrDevTgtAccessMode.setStatus("current")
_ScsiIntrDevOutResets_Type = Counter32
_ScsiIntrDevOutResets_Object = MibTableColumn
scsiIntrDevOutResets = _ScsiIntrDevOutResets_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 1, 1, 2),
    _ScsiIntrDevOutResets_Type()
)
scsiIntrDevOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrDevOutResets.setStatus("current")
_ScsiIntrPortTable_Object = MibTable
scsiIntrPortTable = _ScsiIntrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2)
)
if mibBuilder.loadTexts:
    scsiIntrPortTable.setStatus("current")
_ScsiIntrPortEntry_Object = MibTableRow
scsiIntrPortEntry = _ScsiIntrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1)
)
scsiIntrPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiIntrPortEntry.setStatus("current")
_ScsiIntrPortName_Type = ScsiName
_ScsiIntrPortName_Object = MibTableColumn
scsiIntrPortName = _ScsiIntrPortName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 1),
    _ScsiIntrPortName_Type()
)
scsiIntrPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortName.setStatus("current")
_ScsiIntrPortIdentifier_Type = ScsiIdentifier
_ScsiIntrPortIdentifier_Object = MibTableColumn
scsiIntrPortIdentifier = _ScsiIntrPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 2),
    _ScsiIntrPortIdentifier_Type()
)
scsiIntrPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortIdentifier.setStatus("current")
_ScsiIntrPortOutCommands_Type = Counter32
_ScsiIntrPortOutCommands_Object = MibTableColumn
scsiIntrPortOutCommands = _ScsiIntrPortOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 3),
    _ScsiIntrPortOutCommands_Type()
)
scsiIntrPortOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPortOutCommands.setUnits("commands")
_ScsiIntrPortWrittenMegaBytes_Type = Counter32
_ScsiIntrPortWrittenMegaBytes_Object = MibTableColumn
scsiIntrPortWrittenMegaBytes = _ScsiIntrPortWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 4),
    _ScsiIntrPortWrittenMegaBytes_Type()
)
scsiIntrPortWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPortWrittenMegaBytes.setUnits("Megabytes")
_ScsiIntrPortReadMegaBytes_Type = Counter32
_ScsiIntrPortReadMegaBytes_Object = MibTableColumn
scsiIntrPortReadMegaBytes = _ScsiIntrPortReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 5),
    _ScsiIntrPortReadMegaBytes_Type()
)
scsiIntrPortReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPortReadMegaBytes.setUnits("Megabytes")
_ScsiIntrPortHSOutCommands_Type = Counter64
_ScsiIntrPortHSOutCommands_Object = MibTableColumn
scsiIntrPortHSOutCommands = _ScsiIntrPortHSOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 2, 1, 6),
    _ScsiIntrPortHSOutCommands_Type()
)
scsiIntrPortHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPortHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPortHSOutCommands.setUnits("commands")
_ScsiRemoteTgtDev_ObjectIdentity = ObjectIdentity
scsiRemoteTgtDev = _ScsiRemoteTgtDev_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3)
)
_ScsiDscTgtTable_Object = MibTable
scsiDscTgtTable = _ScsiDscTgtTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    scsiDscTgtTable.setStatus("current")
_ScsiDscTgtEntry_Object = MibTableRow
scsiDscTgtEntry = _ScsiDscTgtEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1)
)
scsiDscTgtEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
)
if mibBuilder.loadTexts:
    scsiDscTgtEntry.setStatus("current")
_ScsiDscTgtIntrPortIndex_Type = ScsiPortIndexValueOrZero
_ScsiDscTgtIntrPortIndex_Object = MibTableColumn
scsiDscTgtIntrPortIndex = _ScsiDscTgtIntrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 1),
    _ScsiDscTgtIntrPortIndex_Type()
)
scsiDscTgtIntrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscTgtIntrPortIndex.setStatus("current")
_ScsiDscTgtIndex_Type = ScsiIndexValue
_ScsiDscTgtIndex_Object = MibTableColumn
scsiDscTgtIndex = _ScsiDscTgtIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 2),
    _ScsiDscTgtIndex_Type()
)
scsiDscTgtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscTgtIndex.setStatus("current")
_ScsiDscTgtDevOrPort_Type = ScsiDeviceOrPort
_ScsiDscTgtDevOrPort_Object = MibTableColumn
scsiDscTgtDevOrPort = _ScsiDscTgtDevOrPort_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 3),
    _ScsiDscTgtDevOrPort_Type()
)
scsiDscTgtDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtDevOrPort.setStatus("current")
_ScsiDscTgtName_Type = ScsiName
_ScsiDscTgtName_Object = MibTableColumn
scsiDscTgtName = _ScsiDscTgtName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 4),
    _ScsiDscTgtName_Type()
)
scsiDscTgtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtName.setStatus("current")


class _ScsiDscTgtConfigured_Type(TruthValue):
    """Custom type scsiDscTgtConfigured based on TruthValue"""


_ScsiDscTgtConfigured_Object = MibTableColumn
scsiDscTgtConfigured = _ScsiDscTgtConfigured_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 5),
    _ScsiDscTgtConfigured_Type()
)
scsiDscTgtConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtConfigured.setStatus("current")
_ScsiDscTgtDiscovered_Type = TruthValue
_ScsiDscTgtDiscovered_Object = MibTableColumn
scsiDscTgtDiscovered = _ScsiDscTgtDiscovered_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 6),
    _ScsiDscTgtDiscovered_Type()
)
scsiDscTgtDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtDiscovered.setStatus("current")
_ScsiDscTgtInCommands_Type = Counter32
_ScsiDscTgtInCommands_Object = MibTableColumn
scsiDscTgtInCommands = _ScsiDscTgtInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 7),
    _ScsiDscTgtInCommands_Type()
)
scsiDscTgtInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtInCommands.setUnits("commands")
_ScsiDscTgtWrittenMegaBytes_Type = Counter32
_ScsiDscTgtWrittenMegaBytes_Object = MibTableColumn
scsiDscTgtWrittenMegaBytes = _ScsiDscTgtWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 8),
    _ScsiDscTgtWrittenMegaBytes_Type()
)
scsiDscTgtWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtWrittenMegaBytes.setUnits("Megabytes")
_ScsiDscTgtReadMegaBytes_Type = Counter32
_ScsiDscTgtReadMegaBytes_Object = MibTableColumn
scsiDscTgtReadMegaBytes = _ScsiDscTgtReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 9),
    _ScsiDscTgtReadMegaBytes_Type()
)
scsiDscTgtReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtReadMegaBytes.setUnits("Megabytes")
_ScsiDscTgtHSInCommands_Type = Counter64
_ScsiDscTgtHSInCommands_Object = MibTableColumn
scsiDscTgtHSInCommands = _ScsiDscTgtHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 10),
    _ScsiDscTgtHSInCommands_Type()
)
scsiDscTgtHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtHSInCommands.setUnits("commands")
_ScsiDscTgtLastCreation_Type = TimeStamp
_ScsiDscTgtLastCreation_Object = MibTableColumn
scsiDscTgtLastCreation = _ScsiDscTgtLastCreation_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 11),
    _ScsiDscTgtLastCreation_Type()
)
scsiDscTgtLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtLastCreation.setStatus("current")
_ScsiDscTgtRowStatus_Type = RowStatus
_ScsiDscTgtRowStatus_Object = MibTableColumn
scsiDscTgtRowStatus = _ScsiDscTgtRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 1, 1, 12),
    _ScsiDscTgtRowStatus_Type()
)
scsiDscTgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtRowStatus.setStatus("current")
_ScsiDscLunTable_Object = MibTable
scsiDscLunTable = _ScsiDscLunTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    scsiDscLunTable.setStatus("current")
_ScsiDscLunEntry_Object = MibTableRow
scsiDscLunEntry = _ScsiDscLunEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 2, 1)
)
scsiDscLunEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
    (0, "SCSI-MIB", "scsiDscLunIndex"),
)
if mibBuilder.loadTexts:
    scsiDscLunEntry.setStatus("current")
_ScsiDscLunIndex_Type = ScsiIndexValue
_ScsiDscLunIndex_Object = MibTableColumn
scsiDscLunIndex = _ScsiDscLunIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 2, 1, 1),
    _ScsiDscLunIndex_Type()
)
scsiDscLunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscLunIndex.setStatus("current")
_ScsiDscLunLun_Type = ScsiLUN
_ScsiDscLunLun_Object = MibTableColumn
scsiDscLunLun = _ScsiDscLunLun_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 2, 1, 2),
    _ScsiDscLunLun_Type()
)
scsiDscLunLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunLun.setStatus("current")
_ScsiDscLunIdTable_Object = MibTable
scsiDscLunIdTable = _ScsiDscLunIdTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    scsiDscLunIdTable.setStatus("current")
_ScsiDscLunIdEntry_Object = MibTableRow
scsiDscLunIdEntry = _ScsiDscLunIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1)
)
scsiDscLunIdEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
    (0, "SCSI-MIB", "scsiDscLunIndex"),
    (0, "SCSI-MIB", "scsiDscLunIdIndex"),
)
if mibBuilder.loadTexts:
    scsiDscLunIdEntry.setStatus("current")
_ScsiDscLunIdIndex_Type = ScsiIndexValue
_ScsiDscLunIdIndex_Object = MibTableColumn
scsiDscLunIdIndex = _ScsiDscLunIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1, 1),
    _ScsiDscLunIdIndex_Type()
)
scsiDscLunIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscLunIdIndex.setStatus("current")
_ScsiDscLunIdCodeSet_Type = ScsiIdCodeSet
_ScsiDscLunIdCodeSet_Object = MibTableColumn
scsiDscLunIdCodeSet = _ScsiDscLunIdCodeSet_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1, 2),
    _ScsiDscLunIdCodeSet_Type()
)
scsiDscLunIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdCodeSet.setStatus("current")
_ScsiDscLunIdAssociation_Type = ScsiIdAssociation
_ScsiDscLunIdAssociation_Object = MibTableColumn
scsiDscLunIdAssociation = _ScsiDscLunIdAssociation_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1, 3),
    _ScsiDscLunIdAssociation_Type()
)
scsiDscLunIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdAssociation.setStatus("current")
_ScsiDscLunIdType_Type = ScsiIdType
_ScsiDscLunIdType_Object = MibTableColumn
scsiDscLunIdType = _ScsiDscLunIdType_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1, 4),
    _ScsiDscLunIdType_Type()
)
scsiDscLunIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdType.setStatus("current")
_ScsiDscLunIdValue_Type = ScsiIdValue
_ScsiDscLunIdValue_Object = MibTableColumn
scsiDscLunIdValue = _ScsiDscLunIdValue_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 3, 1, 5),
    _ScsiDscLunIdValue_Type()
)
scsiDscLunIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdValue.setStatus("current")
_ScsiAttTgtPortTable_Object = MibTable
scsiAttTgtPortTable = _ScsiAttTgtPortTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    scsiAttTgtPortTable.setStatus("current")
_ScsiAttTgtPortEntry_Object = MibTableRow
scsiAttTgtPortEntry = _ScsiAttTgtPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4, 1)
)
scsiAttTgtPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
    (0, "SCSI-MIB", "scsiAttTgtPortIndex"),
)
if mibBuilder.loadTexts:
    scsiAttTgtPortEntry.setStatus("current")
_ScsiAttTgtPortIndex_Type = ScsiIndexValue
_ScsiAttTgtPortIndex_Object = MibTableColumn
scsiAttTgtPortIndex = _ScsiAttTgtPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4, 1, 1),
    _ScsiAttTgtPortIndex_Type()
)
scsiAttTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAttTgtPortIndex.setStatus("current")
_ScsiAttTgtPortDscTgtIdx_Type = ScsiIndexValueOrZero
_ScsiAttTgtPortDscTgtIdx_Object = MibTableColumn
scsiAttTgtPortDscTgtIdx = _ScsiAttTgtPortDscTgtIdx_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4, 1, 2),
    _ScsiAttTgtPortDscTgtIdx_Type()
)
scsiAttTgtPortDscTgtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortDscTgtIdx.setStatus("current")
_ScsiAttTgtPortName_Type = ScsiName
_ScsiAttTgtPortName_Object = MibTableColumn
scsiAttTgtPortName = _ScsiAttTgtPortName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4, 1, 3),
    _ScsiAttTgtPortName_Type()
)
scsiAttTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortName.setStatus("current")
_ScsiAttTgtPortIdentifier_Type = ScsiIdentifier
_ScsiAttTgtPortIdentifier_Object = MibTableColumn
scsiAttTgtPortIdentifier = _ScsiAttTgtPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 2, 3, 4, 1, 4),
    _ScsiAttTgtPortIdentifier_Type()
)
scsiAttTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortIdentifier.setStatus("current")
_ScsiTargetDevice_ObjectIdentity = ObjectIdentity
scsiTargetDevice = _ScsiTargetDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 3)
)
_ScsiTgtDevTable_Object = MibTable
scsiTgtDevTable = _ScsiTgtDevTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1)
)
if mibBuilder.loadTexts:
    scsiTgtDevTable.setStatus("current")
_ScsiTgtDevEntry_Object = MibTableRow
scsiTgtDevEntry = _ScsiTgtDevEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1, 1)
)
scsiTgtDevEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiTgtDevEntry.setStatus("current")
_ScsiTgtDevNumberOfLUs_Type = Gauge32
_ScsiTgtDevNumberOfLUs_Object = MibTableColumn
scsiTgtDevNumberOfLUs = _ScsiTgtDevNumberOfLUs_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1, 1, 1),
    _ScsiTgtDevNumberOfLUs_Type()
)
scsiTgtDevNumberOfLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDevNumberOfLUs.setStatus("current")


class _ScsiTgtDeviceStatus_Type(Integer32):
    """Custom type scsiTgtDeviceStatus based on Integer32"""
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
        *(("abnormal", 5),
          ("available", 2),
          ("broken", 3),
          ("nonAddrFailAbnormal", 8),
          ("nonAddrFailReadying", 7),
          ("nonAddrFailure", 6),
          ("readying", 4),
          ("unknown", 1))
    )


_ScsiTgtDeviceStatus_Type.__name__ = "Integer32"
_ScsiTgtDeviceStatus_Object = MibTableColumn
scsiTgtDeviceStatus = _ScsiTgtDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1, 1, 2),
    _ScsiTgtDeviceStatus_Type()
)
scsiTgtDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDeviceStatus.setStatus("current")
_ScsiTgtDevNonAccessibleLUs_Type = Gauge32
_ScsiTgtDevNonAccessibleLUs_Object = MibTableColumn
scsiTgtDevNonAccessibleLUs = _ScsiTgtDevNonAccessibleLUs_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1, 1, 3),
    _ScsiTgtDevNonAccessibleLUs_Type()
)
scsiTgtDevNonAccessibleLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDevNonAccessibleLUs.setStatus("current")
_ScsiTgtDevResets_Type = Counter32
_ScsiTgtDevResets_Object = MibTableColumn
scsiTgtDevResets = _ScsiTgtDevResets_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 1, 1, 4),
    _ScsiTgtDevResets_Type()
)
scsiTgtDevResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDevResets.setStatus("current")
_ScsiTgtPortTable_Object = MibTable
scsiTgtPortTable = _ScsiTgtPortTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2)
)
if mibBuilder.loadTexts:
    scsiTgtPortTable.setStatus("current")
_ScsiTgtPortEntry_Object = MibTableRow
scsiTgtPortEntry = _ScsiTgtPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1)
)
scsiTgtPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiTgtPortEntry.setStatus("current")
_ScsiTgtPortName_Type = ScsiName
_ScsiTgtPortName_Object = MibTableColumn
scsiTgtPortName = _ScsiTgtPortName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 1),
    _ScsiTgtPortName_Type()
)
scsiTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortName.setStatus("current")
_ScsiTgtPortIdentifier_Type = ScsiIdentifier
_ScsiTgtPortIdentifier_Object = MibTableColumn
scsiTgtPortIdentifier = _ScsiTgtPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 2),
    _ScsiTgtPortIdentifier_Type()
)
scsiTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortIdentifier.setStatus("current")
_ScsiTgtPortInCommands_Type = Counter32
_ScsiTgtPortInCommands_Object = MibTableColumn
scsiTgtPortInCommands = _ScsiTgtPortInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 3),
    _ScsiTgtPortInCommands_Type()
)
scsiTgtPortInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortInCommands.setUnits("commands")
_ScsiTgtPortWrittenMegaBytes_Type = Counter32
_ScsiTgtPortWrittenMegaBytes_Object = MibTableColumn
scsiTgtPortWrittenMegaBytes = _ScsiTgtPortWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 4),
    _ScsiTgtPortWrittenMegaBytes_Type()
)
scsiTgtPortWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortWrittenMegaBytes.setUnits("Megabytes")
_ScsiTgtPortReadMegaBytes_Type = Counter32
_ScsiTgtPortReadMegaBytes_Object = MibTableColumn
scsiTgtPortReadMegaBytes = _ScsiTgtPortReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 5),
    _ScsiTgtPortReadMegaBytes_Type()
)
scsiTgtPortReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortReadMegaBytes.setUnits("Megabytes")
_ScsiTgtPortHSInCommands_Type = Counter64
_ScsiTgtPortHSInCommands_Object = MibTableColumn
scsiTgtPortHSInCommands = _ScsiTgtPortHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 2, 1, 6),
    _ScsiTgtPortHSInCommands_Type()
)
scsiTgtPortHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortHSInCommands.setUnits("commands")
_ScsiRemoteIntrDev_ObjectIdentity = ObjectIdentity
scsiRemoteIntrDev = _ScsiRemoteIntrDev_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3)
)
_ScsiAuthorizedIntrTable_Object = MibTable
scsiAuthorizedIntrTable = _ScsiAuthorizedIntrTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    scsiAuthorizedIntrTable.setStatus("current")
_ScsiAuthorizedIntrEntry_Object = MibTableRow
scsiAuthorizedIntrEntry = _ScsiAuthorizedIntrEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1)
)
scsiAuthorizedIntrEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiAuthIntrTgtPortIndex"),
    (0, "SCSI-MIB", "scsiAuthIntrIndex"),
)
if mibBuilder.loadTexts:
    scsiAuthorizedIntrEntry.setStatus("current")
_ScsiAuthIntrTgtPortIndex_Type = ScsiPortIndexValueOrZero
_ScsiAuthIntrTgtPortIndex_Object = MibTableColumn
scsiAuthIntrTgtPortIndex = _ScsiAuthIntrTgtPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 1),
    _ScsiAuthIntrTgtPortIndex_Type()
)
scsiAuthIntrTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAuthIntrTgtPortIndex.setStatus("current")
_ScsiAuthIntrIndex_Type = ScsiIndexValue
_ScsiAuthIntrIndex_Object = MibTableColumn
scsiAuthIntrIndex = _ScsiAuthIntrIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 2),
    _ScsiAuthIntrIndex_Type()
)
scsiAuthIntrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAuthIntrIndex.setStatus("current")
_ScsiAuthIntrDevOrPort_Type = ScsiDeviceOrPort
_ScsiAuthIntrDevOrPort_Object = MibTableColumn
scsiAuthIntrDevOrPort = _ScsiAuthIntrDevOrPort_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 3),
    _ScsiAuthIntrDevOrPort_Type()
)
scsiAuthIntrDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrDevOrPort.setStatus("current")
_ScsiAuthIntrName_Type = ScsiName
_ScsiAuthIntrName_Object = MibTableColumn
scsiAuthIntrName = _ScsiAuthIntrName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 4),
    _ScsiAuthIntrName_Type()
)
scsiAuthIntrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrName.setStatus("current")
_ScsiAuthIntrLunMapIndex_Type = ScsiIndexValueOrZero
_ScsiAuthIntrLunMapIndex_Object = MibTableColumn
scsiAuthIntrLunMapIndex = _ScsiAuthIntrLunMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 5),
    _ScsiAuthIntrLunMapIndex_Type()
)
scsiAuthIntrLunMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrLunMapIndex.setStatus("current")
_ScsiAuthIntrAttachedTimes_Type = Counter32
_ScsiAuthIntrAttachedTimes_Object = MibTableColumn
scsiAuthIntrAttachedTimes = _ScsiAuthIntrAttachedTimes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 6),
    _ScsiAuthIntrAttachedTimes_Type()
)
scsiAuthIntrAttachedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrAttachedTimes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrAttachedTimes.setUnits("Times")
_ScsiAuthIntrOutCommands_Type = Counter32
_ScsiAuthIntrOutCommands_Object = MibTableColumn
scsiAuthIntrOutCommands = _ScsiAuthIntrOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 7),
    _ScsiAuthIntrOutCommands_Type()
)
scsiAuthIntrOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrOutCommands.setUnits("commands")
_ScsiAuthIntrReadMegaBytes_Type = Counter32
_ScsiAuthIntrReadMegaBytes_Object = MibTableColumn
scsiAuthIntrReadMegaBytes = _ScsiAuthIntrReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 8),
    _ScsiAuthIntrReadMegaBytes_Type()
)
scsiAuthIntrReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrReadMegaBytes.setUnits("Megabytes")
_ScsiAuthIntrWrittenMegaBytes_Type = Counter32
_ScsiAuthIntrWrittenMegaBytes_Object = MibTableColumn
scsiAuthIntrWrittenMegaBytes = _ScsiAuthIntrWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 9),
    _ScsiAuthIntrWrittenMegaBytes_Type()
)
scsiAuthIntrWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrWrittenMegaBytes.setUnits("Megabytes")
_ScsiAuthIntrHSOutCommands_Type = Counter64
_ScsiAuthIntrHSOutCommands_Object = MibTableColumn
scsiAuthIntrHSOutCommands = _ScsiAuthIntrHSOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 10),
    _ScsiAuthIntrHSOutCommands_Type()
)
scsiAuthIntrHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrHSOutCommands.setUnits("commands")
_ScsiAuthIntrLastCreation_Type = TimeStamp
_ScsiAuthIntrLastCreation_Object = MibTableColumn
scsiAuthIntrLastCreation = _ScsiAuthIntrLastCreation_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 11),
    _ScsiAuthIntrLastCreation_Type()
)
scsiAuthIntrLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrLastCreation.setStatus("current")
_ScsiAuthIntrRowStatus_Type = RowStatus
_ScsiAuthIntrRowStatus_Object = MibTableColumn
scsiAuthIntrRowStatus = _ScsiAuthIntrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 1, 1, 12),
    _ScsiAuthIntrRowStatus_Type()
)
scsiAuthIntrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrRowStatus.setStatus("current")
_ScsiAttIntrPortTable_Object = MibTable
scsiAttIntrPortTable = _ScsiAttIntrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    scsiAttIntrPortTable.setStatus("current")
_ScsiAttIntrPortEntry_Object = MibTableRow
scsiAttIntrPortEntry = _ScsiAttIntrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2, 1)
)
scsiAttIntrPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
    (0, "SCSI-MIB", "scsiAttIntrPortIndex"),
)
if mibBuilder.loadTexts:
    scsiAttIntrPortEntry.setStatus("current")
_ScsiAttIntrPortIndex_Type = ScsiIndexValue
_ScsiAttIntrPortIndex_Object = MibTableColumn
scsiAttIntrPortIndex = _ScsiAttIntrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2, 1, 1),
    _ScsiAttIntrPortIndex_Type()
)
scsiAttIntrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAttIntrPortIndex.setStatus("current")
_ScsiAttIntrPortAuthIntrIdx_Type = ScsiIndexValueOrZero
_ScsiAttIntrPortAuthIntrIdx_Object = MibTableColumn
scsiAttIntrPortAuthIntrIdx = _ScsiAttIntrPortAuthIntrIdx_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2, 1, 2),
    _ScsiAttIntrPortAuthIntrIdx_Type()
)
scsiAttIntrPortAuthIntrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPortAuthIntrIdx.setStatus("current")
_ScsiAttIntrPortName_Type = ScsiName
_ScsiAttIntrPortName_Object = MibTableColumn
scsiAttIntrPortName = _ScsiAttIntrPortName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2, 1, 3),
    _ScsiAttIntrPortName_Type()
)
scsiAttIntrPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPortName.setStatus("current")
_ScsiAttIntrPortIdentifier_Type = ScsiIdentifier
_ScsiAttIntrPortIdentifier_Object = MibTableColumn
scsiAttIntrPortIdentifier = _ScsiAttIntrPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 3, 3, 2, 1, 4),
    _ScsiAttIntrPortIdentifier_Type()
)
scsiAttIntrPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPortIdentifier.setStatus("current")
_ScsiLogicalUnit_ObjectIdentity = ObjectIdentity
scsiLogicalUnit = _ScsiLogicalUnit_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 2, 4)
)
_ScsiLuTable_Object = MibTable
scsiLuTable = _ScsiLuTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1)
)
if mibBuilder.loadTexts:
    scsiLuTable.setStatus("current")
_ScsiLuEntry_Object = MibTableRow
scsiLuEntry = _ScsiLuEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1)
)
scsiLuEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLuIndex"),
)
if mibBuilder.loadTexts:
    scsiLuEntry.setStatus("current")
_ScsiLuIndex_Type = ScsiIndexValue
_ScsiLuIndex_Object = MibTableColumn
scsiLuIndex = _ScsiLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 1),
    _ScsiLuIndex_Type()
)
scsiLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLuIndex.setStatus("current")
_ScsiLuDefaultLun_Type = ScsiLUN
_ScsiLuDefaultLun_Object = MibTableColumn
scsiLuDefaultLun = _ScsiLuDefaultLun_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 2),
    _ScsiLuDefaultLun_Type()
)
scsiLuDefaultLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuDefaultLun.setStatus("current")
_ScsiLuWwnName_Type = ScsiLuNameOrZero
_ScsiLuWwnName_Object = MibTableColumn
scsiLuWwnName = _ScsiLuWwnName_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 3),
    _ScsiLuWwnName_Type()
)
scsiLuWwnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuWwnName.setStatus("current")
_ScsiLuVendorId_Type = SnmpAdminString
_ScsiLuVendorId_Object = MibTableColumn
scsiLuVendorId = _ScsiLuVendorId_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 4),
    _ScsiLuVendorId_Type()
)
scsiLuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuVendorId.setStatus("current")
_ScsiLuProductId_Type = SnmpAdminString
_ScsiLuProductId_Object = MibTableColumn
scsiLuProductId = _ScsiLuProductId_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 5),
    _ScsiLuProductId_Type()
)
scsiLuProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuProductId.setStatus("current")
_ScsiLuRevisionId_Type = SnmpAdminString
_ScsiLuRevisionId_Object = MibTableColumn
scsiLuRevisionId = _ScsiLuRevisionId_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 6),
    _ScsiLuRevisionId_Type()
)
scsiLuRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuRevisionId.setStatus("current")
_ScsiLuPeripheralType_Type = Unsigned32
_ScsiLuPeripheralType_Object = MibTableColumn
scsiLuPeripheralType = _ScsiLuPeripheralType_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 7),
    _ScsiLuPeripheralType_Type()
)
scsiLuPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuPeripheralType.setStatus("current")


class _ScsiLuStatus_Type(Integer32):
    """Custom type scsiLuStatus based on Integer32"""
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
        *(("abnormal", 6),
          ("available", 2),
          ("broken", 4),
          ("notAvailable", 3),
          ("readying", 5),
          ("unknown", 1))
    )


_ScsiLuStatus_Type.__name__ = "Integer32"
_ScsiLuStatus_Object = MibTableColumn
scsiLuStatus = _ScsiLuStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 8),
    _ScsiLuStatus_Type()
)
scsiLuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuStatus.setStatus("current")


class _ScsiLuState_Type(Bits):
    """Custom type scsiLuState based on Bits"""
    namedValues = NamedValues(
        *(("dataLost", 0),
          ("dynamicReconfigurationInProgress", 1),
          ("exposed", 2),
          ("fractionallyExposed", 3),
          ("partiallyExposed", 4),
          ("protectedRebuild", 5),
          ("protectionDisabled", 6),
          ("rebuild", 7),
          ("recalculate", 8),
          ("spareInUse", 9),
          ("verifyInProgress", 10))
    )

_ScsiLuState_Type.__name__ = "Bits"
_ScsiLuState_Object = MibTableColumn
scsiLuState = _ScsiLuState_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 9),
    _ScsiLuState_Type()
)
scsiLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuState.setStatus("current")
_ScsiLuInCommands_Type = Counter32
_ScsiLuInCommands_Object = MibTableColumn
scsiLuInCommands = _ScsiLuInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 10),
    _ScsiLuInCommands_Type()
)
scsiLuInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuInCommands.setUnits("commands")
_ScsiLuReadMegaBytes_Type = Counter32
_ScsiLuReadMegaBytes_Object = MibTableColumn
scsiLuReadMegaBytes = _ScsiLuReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 11),
    _ScsiLuReadMegaBytes_Type()
)
scsiLuReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuReadMegaBytes.setUnits("Megabytes")
_ScsiLuWrittenMegaBytes_Type = Counter32
_ScsiLuWrittenMegaBytes_Object = MibTableColumn
scsiLuWrittenMegaBytes = _ScsiLuWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 12),
    _ScsiLuWrittenMegaBytes_Type()
)
scsiLuWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuWrittenMegaBytes.setUnits("Megabytes")
_ScsiLuInResets_Type = Counter32
_ScsiLuInResets_Object = MibTableColumn
scsiLuInResets = _ScsiLuInResets_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 13),
    _ScsiLuInResets_Type()
)
scsiLuInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuInResets.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuInResets.setUnits("resets")
_ScsiLuOutTaskSetFullStatus_Type = Counter32
_ScsiLuOutTaskSetFullStatus_Object = MibTableColumn
scsiLuOutTaskSetFullStatus = _ScsiLuOutTaskSetFullStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 14),
    _ScsiLuOutTaskSetFullStatus_Type()
)
scsiLuOutTaskSetFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuOutTaskSetFullStatus.setStatus("current")
_ScsiLuHSInCommands_Type = Counter64
_ScsiLuHSInCommands_Object = MibTableColumn
scsiLuHSInCommands = _ScsiLuHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 15),
    _ScsiLuHSInCommands_Type()
)
scsiLuHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuHSInCommands.setUnits("commands")
_ScsiLuLastCreation_Type = TimeStamp
_ScsiLuLastCreation_Object = MibTableColumn
scsiLuLastCreation = _ScsiLuLastCreation_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 1, 1, 16),
    _ScsiLuLastCreation_Type()
)
scsiLuLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuLastCreation.setStatus("current")
_ScsiLuIdTable_Object = MibTable
scsiLuIdTable = _ScsiLuIdTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2)
)
if mibBuilder.loadTexts:
    scsiLuIdTable.setStatus("current")
_ScsiLuIdEntry_Object = MibTableRow
scsiLuIdEntry = _ScsiLuIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1)
)
scsiLuIdEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLuIndex"),
    (0, "SCSI-MIB", "scsiLuIdIndex"),
)
if mibBuilder.loadTexts:
    scsiLuIdEntry.setStatus("current")
_ScsiLuIdIndex_Type = ScsiIndexValue
_ScsiLuIdIndex_Object = MibTableColumn
scsiLuIdIndex = _ScsiLuIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1, 1),
    _ScsiLuIdIndex_Type()
)
scsiLuIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLuIdIndex.setStatus("current")
_ScsiLuIdCodeSet_Type = ScsiIdCodeSet
_ScsiLuIdCodeSet_Object = MibTableColumn
scsiLuIdCodeSet = _ScsiLuIdCodeSet_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1, 2),
    _ScsiLuIdCodeSet_Type()
)
scsiLuIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdCodeSet.setStatus("current")
_ScsiLuIdAssociation_Type = ScsiIdAssociation
_ScsiLuIdAssociation_Object = MibTableColumn
scsiLuIdAssociation = _ScsiLuIdAssociation_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1, 3),
    _ScsiLuIdAssociation_Type()
)
scsiLuIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdAssociation.setStatus("current")
_ScsiLuIdType_Type = ScsiIdType
_ScsiLuIdType_Object = MibTableColumn
scsiLuIdType = _ScsiLuIdType_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1, 4),
    _ScsiLuIdType_Type()
)
scsiLuIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdType.setStatus("current")
_ScsiLuIdValue_Type = ScsiIdValue
_ScsiLuIdValue_Object = MibTableColumn
scsiLuIdValue = _ScsiLuIdValue_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 2, 1, 5),
    _ScsiLuIdValue_Type()
)
scsiLuIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdValue.setStatus("current")
_ScsiLunMapTable_Object = MibTable
scsiLunMapTable = _ScsiLunMapTable_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3)
)
if mibBuilder.loadTexts:
    scsiLunMapTable.setStatus("current")
_ScsiLunMapEntry_Object = MibTableRow
scsiLunMapEntry = _ScsiLunMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3, 1)
)
scsiLunMapEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLunMapIndex"),
    (0, "SCSI-MIB", "scsiLunMapLun"),
)
if mibBuilder.loadTexts:
    scsiLunMapEntry.setStatus("current")
_ScsiLunMapIndex_Type = ScsiIndexValue
_ScsiLunMapIndex_Object = MibTableColumn
scsiLunMapIndex = _ScsiLunMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3, 1, 1),
    _ScsiLunMapIndex_Type()
)
scsiLunMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLunMapIndex.setStatus("current")
_ScsiLunMapLun_Type = ScsiLUN
_ScsiLunMapLun_Object = MibTableColumn
scsiLunMapLun = _ScsiLunMapLun_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3, 1, 2),
    _ScsiLunMapLun_Type()
)
scsiLunMapLun.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLunMapLun.setStatus("current")
_ScsiLunMapLuIndex_Type = ScsiIndexValue
_ScsiLunMapLuIndex_Object = MibTableColumn
scsiLunMapLuIndex = _ScsiLunMapLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3, 1, 3),
    _ScsiLunMapLuIndex_Type()
)
scsiLunMapLuIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLunMapLuIndex.setStatus("current")
_ScsiLunMapRowStatus_Type = RowStatus
_ScsiLunMapRowStatus_Object = MibTableColumn
scsiLunMapRowStatus = _ScsiLunMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 139, 2, 4, 3, 1, 4),
    _ScsiLunMapRowStatus_Type()
)
scsiLunMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLunMapRowStatus.setStatus("current")
_ScsiConformance_ObjectIdentity = ObjectIdentity
scsiConformance = _ScsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 3)
)
_ScsiCompliances_ObjectIdentity = ObjectIdentity
scsiCompliances = _ScsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 3, 1)
)
_ScsiGroups_ObjectIdentity = ObjectIdentity
scsiGroups = _ScsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 139, 3, 2)
)

# Managed Objects groups

scsiDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 1)
)
scsiDeviceGroup.setObjects(
      *(("SCSI-MIB", "scsiInstAlias"),
        ("SCSI-MIB", "scsiInstSoftwareIndex"),
        ("SCSI-MIB", "scsiInstVendorVersion"),
        ("SCSI-MIB", "scsiInstScsiNotificationsEnable"),
        ("SCSI-MIB", "scsiInstStorageType"),
        ("SCSI-MIB", "scsiDeviceAlias"),
        ("SCSI-MIB", "scsiDeviceRole"),
        ("SCSI-MIB", "scsiDevicePortNumber"),
        ("SCSI-MIB", "scsiPortRole"),
        ("SCSI-MIB", "scsiPortTransportPtr"),
        ("SCSI-MIB", "scsiTransportType"),
        ("SCSI-MIB", "scsiTransportPointer"),
        ("SCSI-MIB", "scsiTransportDevName"))
)
if mibBuilder.loadTexts:
    scsiDeviceGroup.setStatus("current")

scsiInitiatorDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 2)
)
scsiInitiatorDeviceGroup.setObjects(
      *(("SCSI-MIB", "scsiIntrDevTgtAccessMode"),
        ("SCSI-MIB", "scsiIntrPortName"),
        ("SCSI-MIB", "scsiIntrPortIdentifier"),
        ("SCSI-MIB", "scsiAttTgtPortDscTgtIdx"),
        ("SCSI-MIB", "scsiAttTgtPortName"),
        ("SCSI-MIB", "scsiAttTgtPortIdentifier"))
)
if mibBuilder.loadTexts:
    scsiInitiatorDeviceGroup.setStatus("current")

scsiDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 3)
)
scsiDiscoveryGroup.setObjects(
      *(("SCSI-MIB", "scsiDscTgtDevOrPort"),
        ("SCSI-MIB", "scsiDscTgtName"),
        ("SCSI-MIB", "scsiDscTgtConfigured"),
        ("SCSI-MIB", "scsiDscTgtDiscovered"),
        ("SCSI-MIB", "scsiDscTgtRowStatus"),
        ("SCSI-MIB", "scsiDscTgtLastCreation"),
        ("SCSI-MIB", "scsiDscLunLun"),
        ("SCSI-MIB", "scsiDscLunIdCodeSet"),
        ("SCSI-MIB", "scsiDscLunIdAssociation"),
        ("SCSI-MIB", "scsiDscLunIdType"),
        ("SCSI-MIB", "scsiDscLunIdValue"))
)
if mibBuilder.loadTexts:
    scsiDiscoveryGroup.setStatus("current")

scsiTargetDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 4)
)
scsiTargetDeviceGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtDevNumberOfLUs"),
        ("SCSI-MIB", "scsiTgtDeviceStatus"),
        ("SCSI-MIB", "scsiTgtDevNonAccessibleLUs"),
        ("SCSI-MIB", "scsiTgtPortName"),
        ("SCSI-MIB", "scsiTgtPortIdentifier"),
        ("SCSI-MIB", "scsiAttIntrPortAuthIntrIdx"),
        ("SCSI-MIB", "scsiAttIntrPortName"),
        ("SCSI-MIB", "scsiAttIntrPortIdentifier"),
        ("SCSI-MIB", "scsiLuDefaultLun"),
        ("SCSI-MIB", "scsiLuWwnName"),
        ("SCSI-MIB", "scsiLuVendorId"),
        ("SCSI-MIB", "scsiLuProductId"),
        ("SCSI-MIB", "scsiLuRevisionId"),
        ("SCSI-MIB", "scsiLuPeripheralType"),
        ("SCSI-MIB", "scsiLuStatus"),
        ("SCSI-MIB", "scsiLuState"),
        ("SCSI-MIB", "scsiLuLastCreation"),
        ("SCSI-MIB", "scsiLuIdCodeSet"),
        ("SCSI-MIB", "scsiLuIdAssociation"),
        ("SCSI-MIB", "scsiLuIdType"),
        ("SCSI-MIB", "scsiLuIdValue"))
)
if mibBuilder.loadTexts:
    scsiTargetDeviceGroup.setStatus("current")

scsiLunMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 5)
)
scsiLunMapGroup.setObjects(
      *(("SCSI-MIB", "scsiLunMapLuIndex"),
        ("SCSI-MIB", "scsiLunMapRowStatus"),
        ("SCSI-MIB", "scsiAuthIntrDevOrPort"),
        ("SCSI-MIB", "scsiAuthIntrName"),
        ("SCSI-MIB", "scsiAuthIntrLunMapIndex"),
        ("SCSI-MIB", "scsiAuthIntrLastCreation"),
        ("SCSI-MIB", "scsiAuthIntrRowStatus"))
)
if mibBuilder.loadTexts:
    scsiLunMapGroup.setStatus("current")

scsiTargetDevStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 6)
)
scsiTargetDevStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtDevResets"),
        ("SCSI-MIB", "scsiTgtPortInCommands"),
        ("SCSI-MIB", "scsiTgtPortWrittenMegaBytes"),
        ("SCSI-MIB", "scsiTgtPortReadMegaBytes"),
        ("SCSI-MIB", "scsiLuInCommands"),
        ("SCSI-MIB", "scsiLuReadMegaBytes"),
        ("SCSI-MIB", "scsiLuWrittenMegaBytes"),
        ("SCSI-MIB", "scsiLuInResets"),
        ("SCSI-MIB", "scsiLuOutTaskSetFullStatus"))
)
if mibBuilder.loadTexts:
    scsiTargetDevStatsGroup.setStatus("current")

scsiTargetDevHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 7)
)
scsiTargetDevHSStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtPortHSInCommands"),
        ("SCSI-MIB", "scsiLuHSInCommands"))
)
if mibBuilder.loadTexts:
    scsiTargetDevHSStatsGroup.setStatus("current")

scsiLunMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 8)
)
scsiLunMapStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiAuthIntrAttachedTimes"),
        ("SCSI-MIB", "scsiAuthIntrOutCommands"),
        ("SCSI-MIB", "scsiAuthIntrReadMegaBytes"),
        ("SCSI-MIB", "scsiAuthIntrWrittenMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiLunMapStatsGroup.setStatus("current")

scsiLunMapHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 9)
)
scsiLunMapHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiAuthIntrHSOutCommands")
)
if mibBuilder.loadTexts:
    scsiLunMapHSStatsGroup.setStatus("current")

scsiInitiatorDevStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 10)
)
scsiInitiatorDevStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiIntrDevOutResets"),
        ("SCSI-MIB", "scsiIntrPortOutCommands"),
        ("SCSI-MIB", "scsiIntrPortWrittenMegaBytes"),
        ("SCSI-MIB", "scsiIntrPortReadMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiInitiatorDevStatsGroup.setStatus("current")

scsiInitiatorDevHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 11)
)
scsiInitiatorDevHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiIntrPortHSOutCommands")
)
if mibBuilder.loadTexts:
    scsiInitiatorDevHSStatsGroup.setStatus("current")

scsiDiscoveryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 12)
)
scsiDiscoveryStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiDscTgtInCommands"),
        ("SCSI-MIB", "scsiDscTgtReadMegaBytes"),
        ("SCSI-MIB", "scsiDscTgtWrittenMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiDiscoveryStatsGroup.setStatus("current")

scsiDiscoveryHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 13)
)
scsiDiscoveryHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiDscTgtHSInCommands")
)
if mibBuilder.loadTexts:
    scsiDiscoveryHSStatsGroup.setStatus("current")

scsiDeviceStatGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 14)
)
scsiDeviceStatGroup.setObjects(
    ("SCSI-MIB", "scsiPortBusyStatuses")
)
if mibBuilder.loadTexts:
    scsiDeviceStatGroup.setStatus("current")


# Notification objects

scsiTgtDeviceStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 139, 0, 0, 1)
)
scsiTgtDeviceStatusChanged.setObjects(
    ("SCSI-MIB", "scsiTgtDeviceStatus")
)
if mibBuilder.loadTexts:
    scsiTgtDeviceStatusChanged.setStatus(
        "current"
    )

scsiLuStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 139, 0, 0, 2)
)
scsiLuStatusChanged.setObjects(
    ("SCSI-MIB", "scsiLuStatus")
)
if mibBuilder.loadTexts:
    scsiLuStatusChanged.setStatus(
        "current"
    )


# Notifications groups

scsiTgtDevLuNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 139, 3, 2, 15)
)
scsiTgtDevLuNotificationsGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtDeviceStatusChanged"),
        ("SCSI-MIB", "scsiLuStatusChanged"))
)
if mibBuilder.loadTexts:
    scsiTgtDevLuNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

scsiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 139, 3, 1, 1)
)
if mibBuilder.loadTexts:
    scsiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCSI-MIB",
    **{"ScsiLUN": ScsiLUN,
       "ScsiIndexValue": ScsiIndexValue,
       "ScsiPortIndexValueOrZero": ScsiPortIndexValueOrZero,
       "ScsiIndexValueOrZero": ScsiIndexValueOrZero,
       "ScsiIdentifier": ScsiIdentifier,
       "ScsiName": ScsiName,
       "ScsiLuNameOrZero": ScsiLuNameOrZero,
       "ScsiDeviceOrPort": ScsiDeviceOrPort,
       "ScsiIdCodeSet": ScsiIdCodeSet,
       "ScsiIdAssociation": ScsiIdAssociation,
       "ScsiIdType": ScsiIdType,
       "ScsiIdValue": ScsiIdValue,
       "ScsiHrSWInstalledIndexOrZero": ScsiHrSWInstalledIndexOrZero,
       "scsiMIB": scsiMIB,
       "scsiNotifications": scsiNotifications,
       "scsiNotificationsPrefix": scsiNotificationsPrefix,
       "scsiTgtDeviceStatusChanged": scsiTgtDeviceStatusChanged,
       "scsiLuStatusChanged": scsiLuStatusChanged,
       "scsiAdmin": scsiAdmin,
       "scsiTransportTypes": scsiTransportTypes,
       "scsiTransportOther": scsiTransportOther,
       "scsiTransportSPI": scsiTransportSPI,
       "scsiTransportFCP": scsiTransportFCP,
       "scsiTransportSRP": scsiTransportSRP,
       "scsiTransportISCSI": scsiTransportISCSI,
       "scsiTransportSBP": scsiTransportSBP,
       "scsiTransportSAS": scsiTransportSAS,
       "scsiObjects": scsiObjects,
       "scsiGeneral": scsiGeneral,
       "scsiInstanceTable": scsiInstanceTable,
       "scsiInstanceEntry": scsiInstanceEntry,
       "scsiInstIndex": scsiInstIndex,
       "scsiInstAlias": scsiInstAlias,
       "scsiInstSoftwareIndex": scsiInstSoftwareIndex,
       "scsiInstVendorVersion": scsiInstVendorVersion,
       "scsiInstScsiNotificationsEnable": scsiInstScsiNotificationsEnable,
       "scsiInstStorageType": scsiInstStorageType,
       "scsiDeviceTable": scsiDeviceTable,
       "scsiDeviceEntry": scsiDeviceEntry,
       "scsiDeviceIndex": scsiDeviceIndex,
       "scsiDeviceAlias": scsiDeviceAlias,
       "scsiDeviceRole": scsiDeviceRole,
       "scsiDevicePortNumber": scsiDevicePortNumber,
       "scsiPortTable": scsiPortTable,
       "scsiPortEntry": scsiPortEntry,
       "scsiPortIndex": scsiPortIndex,
       "scsiPortRole": scsiPortRole,
       "scsiPortTransportPtr": scsiPortTransportPtr,
       "scsiPortBusyStatuses": scsiPortBusyStatuses,
       "scsiTransportTable": scsiTransportTable,
       "scsiTransportEntry": scsiTransportEntry,
       "scsiTransportIndex": scsiTransportIndex,
       "scsiTransportType": scsiTransportType,
       "scsiTransportPointer": scsiTransportPointer,
       "scsiTransportDevName": scsiTransportDevName,
       "scsiInitiatorDevice": scsiInitiatorDevice,
       "scsiIntrDevTable": scsiIntrDevTable,
       "scsiIntrDevEntry": scsiIntrDevEntry,
       "scsiIntrDevTgtAccessMode": scsiIntrDevTgtAccessMode,
       "scsiIntrDevOutResets": scsiIntrDevOutResets,
       "scsiIntrPortTable": scsiIntrPortTable,
       "scsiIntrPortEntry": scsiIntrPortEntry,
       "scsiIntrPortName": scsiIntrPortName,
       "scsiIntrPortIdentifier": scsiIntrPortIdentifier,
       "scsiIntrPortOutCommands": scsiIntrPortOutCommands,
       "scsiIntrPortWrittenMegaBytes": scsiIntrPortWrittenMegaBytes,
       "scsiIntrPortReadMegaBytes": scsiIntrPortReadMegaBytes,
       "scsiIntrPortHSOutCommands": scsiIntrPortHSOutCommands,
       "scsiRemoteTgtDev": scsiRemoteTgtDev,
       "scsiDscTgtTable": scsiDscTgtTable,
       "scsiDscTgtEntry": scsiDscTgtEntry,
       "scsiDscTgtIntrPortIndex": scsiDscTgtIntrPortIndex,
       "scsiDscTgtIndex": scsiDscTgtIndex,
       "scsiDscTgtDevOrPort": scsiDscTgtDevOrPort,
       "scsiDscTgtName": scsiDscTgtName,
       "scsiDscTgtConfigured": scsiDscTgtConfigured,
       "scsiDscTgtDiscovered": scsiDscTgtDiscovered,
       "scsiDscTgtInCommands": scsiDscTgtInCommands,
       "scsiDscTgtWrittenMegaBytes": scsiDscTgtWrittenMegaBytes,
       "scsiDscTgtReadMegaBytes": scsiDscTgtReadMegaBytes,
       "scsiDscTgtHSInCommands": scsiDscTgtHSInCommands,
       "scsiDscTgtLastCreation": scsiDscTgtLastCreation,
       "scsiDscTgtRowStatus": scsiDscTgtRowStatus,
       "scsiDscLunTable": scsiDscLunTable,
       "scsiDscLunEntry": scsiDscLunEntry,
       "scsiDscLunIndex": scsiDscLunIndex,
       "scsiDscLunLun": scsiDscLunLun,
       "scsiDscLunIdTable": scsiDscLunIdTable,
       "scsiDscLunIdEntry": scsiDscLunIdEntry,
       "scsiDscLunIdIndex": scsiDscLunIdIndex,
       "scsiDscLunIdCodeSet": scsiDscLunIdCodeSet,
       "scsiDscLunIdAssociation": scsiDscLunIdAssociation,
       "scsiDscLunIdType": scsiDscLunIdType,
       "scsiDscLunIdValue": scsiDscLunIdValue,
       "scsiAttTgtPortTable": scsiAttTgtPortTable,
       "scsiAttTgtPortEntry": scsiAttTgtPortEntry,
       "scsiAttTgtPortIndex": scsiAttTgtPortIndex,
       "scsiAttTgtPortDscTgtIdx": scsiAttTgtPortDscTgtIdx,
       "scsiAttTgtPortName": scsiAttTgtPortName,
       "scsiAttTgtPortIdentifier": scsiAttTgtPortIdentifier,
       "scsiTargetDevice": scsiTargetDevice,
       "scsiTgtDevTable": scsiTgtDevTable,
       "scsiTgtDevEntry": scsiTgtDevEntry,
       "scsiTgtDevNumberOfLUs": scsiTgtDevNumberOfLUs,
       "scsiTgtDeviceStatus": scsiTgtDeviceStatus,
       "scsiTgtDevNonAccessibleLUs": scsiTgtDevNonAccessibleLUs,
       "scsiTgtDevResets": scsiTgtDevResets,
       "scsiTgtPortTable": scsiTgtPortTable,
       "scsiTgtPortEntry": scsiTgtPortEntry,
       "scsiTgtPortName": scsiTgtPortName,
       "scsiTgtPortIdentifier": scsiTgtPortIdentifier,
       "scsiTgtPortInCommands": scsiTgtPortInCommands,
       "scsiTgtPortWrittenMegaBytes": scsiTgtPortWrittenMegaBytes,
       "scsiTgtPortReadMegaBytes": scsiTgtPortReadMegaBytes,
       "scsiTgtPortHSInCommands": scsiTgtPortHSInCommands,
       "scsiRemoteIntrDev": scsiRemoteIntrDev,
       "scsiAuthorizedIntrTable": scsiAuthorizedIntrTable,
       "scsiAuthorizedIntrEntry": scsiAuthorizedIntrEntry,
       "scsiAuthIntrTgtPortIndex": scsiAuthIntrTgtPortIndex,
       "scsiAuthIntrIndex": scsiAuthIntrIndex,
       "scsiAuthIntrDevOrPort": scsiAuthIntrDevOrPort,
       "scsiAuthIntrName": scsiAuthIntrName,
       "scsiAuthIntrLunMapIndex": scsiAuthIntrLunMapIndex,
       "scsiAuthIntrAttachedTimes": scsiAuthIntrAttachedTimes,
       "scsiAuthIntrOutCommands": scsiAuthIntrOutCommands,
       "scsiAuthIntrReadMegaBytes": scsiAuthIntrReadMegaBytes,
       "scsiAuthIntrWrittenMegaBytes": scsiAuthIntrWrittenMegaBytes,
       "scsiAuthIntrHSOutCommands": scsiAuthIntrHSOutCommands,
       "scsiAuthIntrLastCreation": scsiAuthIntrLastCreation,
       "scsiAuthIntrRowStatus": scsiAuthIntrRowStatus,
       "scsiAttIntrPortTable": scsiAttIntrPortTable,
       "scsiAttIntrPortEntry": scsiAttIntrPortEntry,
       "scsiAttIntrPortIndex": scsiAttIntrPortIndex,
       "scsiAttIntrPortAuthIntrIdx": scsiAttIntrPortAuthIntrIdx,
       "scsiAttIntrPortName": scsiAttIntrPortName,
       "scsiAttIntrPortIdentifier": scsiAttIntrPortIdentifier,
       "scsiLogicalUnit": scsiLogicalUnit,
       "scsiLuTable": scsiLuTable,
       "scsiLuEntry": scsiLuEntry,
       "scsiLuIndex": scsiLuIndex,
       "scsiLuDefaultLun": scsiLuDefaultLun,
       "scsiLuWwnName": scsiLuWwnName,
       "scsiLuVendorId": scsiLuVendorId,
       "scsiLuProductId": scsiLuProductId,
       "scsiLuRevisionId": scsiLuRevisionId,
       "scsiLuPeripheralType": scsiLuPeripheralType,
       "scsiLuStatus": scsiLuStatus,
       "scsiLuState": scsiLuState,
       "scsiLuInCommands": scsiLuInCommands,
       "scsiLuReadMegaBytes": scsiLuReadMegaBytes,
       "scsiLuWrittenMegaBytes": scsiLuWrittenMegaBytes,
       "scsiLuInResets": scsiLuInResets,
       "scsiLuOutTaskSetFullStatus": scsiLuOutTaskSetFullStatus,
       "scsiLuHSInCommands": scsiLuHSInCommands,
       "scsiLuLastCreation": scsiLuLastCreation,
       "scsiLuIdTable": scsiLuIdTable,
       "scsiLuIdEntry": scsiLuIdEntry,
       "scsiLuIdIndex": scsiLuIdIndex,
       "scsiLuIdCodeSet": scsiLuIdCodeSet,
       "scsiLuIdAssociation": scsiLuIdAssociation,
       "scsiLuIdType": scsiLuIdType,
       "scsiLuIdValue": scsiLuIdValue,
       "scsiLunMapTable": scsiLunMapTable,
       "scsiLunMapEntry": scsiLunMapEntry,
       "scsiLunMapIndex": scsiLunMapIndex,
       "scsiLunMapLun": scsiLunMapLun,
       "scsiLunMapLuIndex": scsiLunMapLuIndex,
       "scsiLunMapRowStatus": scsiLunMapRowStatus,
       "scsiConformance": scsiConformance,
       "scsiCompliances": scsiCompliances,
       "scsiCompliance": scsiCompliance,
       "scsiGroups": scsiGroups,
       "scsiDeviceGroup": scsiDeviceGroup,
       "scsiInitiatorDeviceGroup": scsiInitiatorDeviceGroup,
       "scsiDiscoveryGroup": scsiDiscoveryGroup,
       "scsiTargetDeviceGroup": scsiTargetDeviceGroup,
       "scsiLunMapGroup": scsiLunMapGroup,
       "scsiTargetDevStatsGroup": scsiTargetDevStatsGroup,
       "scsiTargetDevHSStatsGroup": scsiTargetDevHSStatsGroup,
       "scsiLunMapStatsGroup": scsiLunMapStatsGroup,
       "scsiLunMapHSStatsGroup": scsiLunMapHSStatsGroup,
       "scsiInitiatorDevStatsGroup": scsiInitiatorDevStatsGroup,
       "scsiInitiatorDevHSStatsGroup": scsiInitiatorDevHSStatsGroup,
       "scsiDiscoveryStatsGroup": scsiDiscoveryStatsGroup,
       "scsiDiscoveryHSStatsGroup": scsiDiscoveryHSStatsGroup,
       "scsiDeviceStatGroup": scsiDeviceStatGroup,
       "scsiTgtDevLuNotificationsGroup": scsiTgtDevLuNotificationsGroup}
)
