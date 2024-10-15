# SNMP MIB module (CISCO-SCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:04 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoScsiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95)
)
ciscoScsiMIB.setRevisions(
        ("2002-12-31 00:00",
         "2002-11-08 00:00",
         "2002-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScsiLUNOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(8, 8),
    )



class ScsiIndexValue(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ScsiPortIndexValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIndexValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(11, 11),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(256, 256),
        ValueSizeConstraint(258, 258),
        ValueSizeConstraint(262, 262),
    )



class ScsiName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(256, 256),
        ValueSizeConstraint(258, 258),
        ValueSizeConstraint(262, 262),
    )



class ScsiNameIdOrZero(OctetString, TextualConvention):
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
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class ScsiIdAssociation(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class ScsiIdType(Unsigned32, TextualConvention):
    status = "current"
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



class HrSWInstalledIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoScsiObjects_ObjectIdentity = ObjectIdentity
ciscoScsiObjects = _CiscoScsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1)
)
_CiscoScsiTransportTypes_ObjectIdentity = ObjectIdentity
ciscoScsiTransportTypes = _CiscoScsiTransportTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1)
)
_CiscoScsiTranportOther_ObjectIdentity = ObjectIdentity
ciscoScsiTranportOther = _CiscoScsiTranportOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 1)
)
_CiscoScsiTranportSPI_ObjectIdentity = ObjectIdentity
ciscoScsiTranportSPI = _CiscoScsiTranportSPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 2)
)
_CiscoScsiTransportFCP_ObjectIdentity = ObjectIdentity
ciscoScsiTransportFCP = _CiscoScsiTransportFCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 3)
)
_CiscoScsiTransportSRP_ObjectIdentity = ObjectIdentity
ciscoScsiTransportSRP = _CiscoScsiTransportSRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 4)
)
_CiscoScsiTransportISCSI_ObjectIdentity = ObjectIdentity
ciscoScsiTransportISCSI = _CiscoScsiTransportISCSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 5)
)
_CiscoScsiTransportSBP_ObjectIdentity = ObjectIdentity
ciscoScsiTransportSBP = _CiscoScsiTransportSBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 1, 6)
)
_CiscoScsiGeneral_ObjectIdentity = ObjectIdentity
ciscoScsiGeneral = _CiscoScsiGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2)
)
_CiscoScsiInstanceTable_Object = MibTable
ciscoScsiInstanceTable = _CiscoScsiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiInstanceTable.setStatus("current")
_CiscoScsiInstanceEntry_Object = MibTableRow
ciscoScsiInstanceEntry = _CiscoScsiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1)
)
ciscoScsiInstanceEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiInstanceEntry.setStatus("current")
_CiscoScsiInstIndex_Type = ScsiIndexValue
_CiscoScsiInstIndex_Object = MibTableColumn
ciscoScsiInstIndex = _CiscoScsiInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1, 1),
    _CiscoScsiInstIndex_Type()
)
ciscoScsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiInstIndex.setStatus("current")


class _CiscoScsiInstAlias_Type(SnmpAdminString):
    """Custom type ciscoScsiInstAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiInstAlias_Type.__name__ = "SnmpAdminString"
_CiscoScsiInstAlias_Object = MibTableColumn
ciscoScsiInstAlias = _CiscoScsiInstAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1, 2),
    _CiscoScsiInstAlias_Type()
)
ciscoScsiInstAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoScsiInstAlias.setStatus("current")
_CiscoScsiInstSoftwareIndex_Type = HrSWInstalledIndexOrZero
_CiscoScsiInstSoftwareIndex_Object = MibTableColumn
ciscoScsiInstSoftwareIndex = _CiscoScsiInstSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1, 3),
    _CiscoScsiInstSoftwareIndex_Type()
)
ciscoScsiInstSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiInstSoftwareIndex.setStatus("current")


class _CiscoScsiInstVendorVersion_Type(SnmpAdminString):
    """Custom type ciscoScsiInstVendorVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiInstVendorVersion_Type.__name__ = "SnmpAdminString"
_CiscoScsiInstVendorVersion_Object = MibTableColumn
ciscoScsiInstVendorVersion = _CiscoScsiInstVendorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1, 4),
    _CiscoScsiInstVendorVersion_Type()
)
ciscoScsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiInstVendorVersion.setStatus("current")


class _CiscoScsiInstNotifEnable_Type(TruthValue):
    """Custom type ciscoScsiInstNotifEnable based on TruthValue"""


_CiscoScsiInstNotifEnable_Object = MibTableColumn
ciscoScsiInstNotifEnable = _CiscoScsiInstNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 1, 1, 5),
    _CiscoScsiInstNotifEnable_Type()
)
ciscoScsiInstNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoScsiInstNotifEnable.setStatus("current")
_CiscoScsiDeviceTable_Object = MibTable
ciscoScsiDeviceTable = _CiscoScsiDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiDeviceTable.setStatus("current")
_CiscoScsiDeviceEntry_Object = MibTableRow
ciscoScsiDeviceEntry = _CiscoScsiDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1)
)
ciscoScsiDeviceEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiDeviceEntry.setStatus("current")
_CiscoScsiDeviceIndex_Type = ScsiIndexValue
_CiscoScsiDeviceIndex_Object = MibTableColumn
ciscoScsiDeviceIndex = _CiscoScsiDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1, 1),
    _CiscoScsiDeviceIndex_Type()
)
ciscoScsiDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiDeviceIndex.setStatus("current")


class _CiscoScsiDeviceAlias_Type(SnmpAdminString):
    """Custom type ciscoScsiDeviceAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiDeviceAlias_Type.__name__ = "SnmpAdminString"
_CiscoScsiDeviceAlias_Object = MibTableColumn
ciscoScsiDeviceAlias = _CiscoScsiDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1, 2),
    _CiscoScsiDeviceAlias_Type()
)
ciscoScsiDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoScsiDeviceAlias.setStatus("current")


class _CiscoScsiDeviceRole_Type(Bits):
    """Custom type ciscoScsiDeviceRole based on Bits"""
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 0))
    )

_CiscoScsiDeviceRole_Type.__name__ = "Bits"
_CiscoScsiDeviceRole_Object = MibTableColumn
ciscoScsiDeviceRole = _CiscoScsiDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1, 3),
    _CiscoScsiDeviceRole_Type()
)
ciscoScsiDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDeviceRole.setStatus("current")
_CiscoScsiDevicePortNumber_Type = Unsigned32
_CiscoScsiDevicePortNumber_Object = MibTableColumn
ciscoScsiDevicePortNumber = _CiscoScsiDevicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1, 4),
    _CiscoScsiDevicePortNumber_Type()
)
ciscoScsiDevicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDevicePortNumber.setStatus("current")
_CiscoScsiDeviceResets_Type = Counter32
_CiscoScsiDeviceResets_Object = MibTableColumn
ciscoScsiDeviceResets = _CiscoScsiDeviceResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 2, 1, 5),
    _CiscoScsiDeviceResets_Type()
)
ciscoScsiDeviceResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDeviceResets.setStatus("current")
_CiscoScsiPortTable_Object = MibTable
ciscoScsiPortTable = _CiscoScsiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ciscoScsiPortTable.setStatus("current")
_CiscoScsiPortEntry_Object = MibTableRow
ciscoScsiPortEntry = _CiscoScsiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3, 1)
)
ciscoScsiPortEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiPortIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiPortEntry.setStatus("current")
_CiscoScsiPortIndex_Type = ScsiIndexValue
_CiscoScsiPortIndex_Object = MibTableColumn
ciscoScsiPortIndex = _CiscoScsiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3, 1, 1),
    _CiscoScsiPortIndex_Type()
)
ciscoScsiPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiPortIndex.setStatus("current")


class _CiscoScsiPortRole_Type(Bits):
    """Custom type ciscoScsiPortRole based on Bits"""
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 0))
    )

_CiscoScsiPortRole_Type.__name__ = "Bits"
_CiscoScsiPortRole_Object = MibTableColumn
ciscoScsiPortRole = _CiscoScsiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3, 1, 2),
    _CiscoScsiPortRole_Type()
)
ciscoScsiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiPortRole.setStatus("current")
_CiscoScsiPortTrnsptPtr_Type = RowPointer
_CiscoScsiPortTrnsptPtr_Object = MibTableColumn
ciscoScsiPortTrnsptPtr = _CiscoScsiPortTrnsptPtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3, 1, 3),
    _CiscoScsiPortTrnsptPtr_Type()
)
ciscoScsiPortTrnsptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiPortTrnsptPtr.setStatus("current")
_CiscoScsiPortBusyStatuses_Type = Counter32
_CiscoScsiPortBusyStatuses_Object = MibTableColumn
ciscoScsiPortBusyStatuses = _CiscoScsiPortBusyStatuses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 3, 1, 4),
    _CiscoScsiPortBusyStatuses_Type()
)
ciscoScsiPortBusyStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiPortBusyStatuses.setStatus("current")
_CiscoScsiTrnsptTable_Object = MibTable
ciscoScsiTrnsptTable = _CiscoScsiTrnsptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ciscoScsiTrnsptTable.setStatus("current")
_CiscoScsiTrnsptEntry_Object = MibTableRow
ciscoScsiTrnsptEntry = _CiscoScsiTrnsptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5, 1)
)
ciscoScsiTrnsptEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiTrnsptIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiTrnsptEntry.setStatus("current")
_CiscoScsiTrnsptIndex_Type = ScsiIndexValue
_CiscoScsiTrnsptIndex_Object = MibTableColumn
ciscoScsiTrnsptIndex = _CiscoScsiTrnsptIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5, 1, 1),
    _CiscoScsiTrnsptIndex_Type()
)
ciscoScsiTrnsptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiTrnsptIndex.setStatus("current")
_CiscoScsiTrnsptType_Type = AutonomousType
_CiscoScsiTrnsptType_Object = MibTableColumn
ciscoScsiTrnsptType = _CiscoScsiTrnsptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5, 1, 2),
    _CiscoScsiTrnsptType_Type()
)
ciscoScsiTrnsptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTrnsptType.setStatus("current")
_CiscoScsiTrnsptPointer_Type = RowPointer
_CiscoScsiTrnsptPointer_Object = MibTableColumn
ciscoScsiTrnsptPointer = _CiscoScsiTrnsptPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5, 1, 3),
    _CiscoScsiTrnsptPointer_Type()
)
ciscoScsiTrnsptPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTrnsptPointer.setStatus("current")
_CiscoScsiTrnsptDevName_Type = ScsiName
_CiscoScsiTrnsptDevName_Object = MibTableColumn
ciscoScsiTrnsptDevName = _CiscoScsiTrnsptDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 2, 5, 1, 4),
    _CiscoScsiTrnsptDevName_Type()
)
ciscoScsiTrnsptDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTrnsptDevName.setStatus("current")
_CiscoScsiInitiator_ObjectIdentity = ObjectIdentity
ciscoScsiInitiator = _CiscoScsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3)
)
_CiscoScsiIntrDevTable_Object = MibTable
ciscoScsiIntrDevTable = _CiscoScsiIntrDevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiIntrDevTable.setStatus("current")
_CiscoScsiIntrDevEntry_Object = MibTableRow
ciscoScsiIntrDevEntry = _CiscoScsiIntrDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 1, 1)
)
ciscoScsiIntrDevEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiIntrDevEntry.setStatus("current")


class _CiscoScsiIntrDevAccMode_Type(Integer32):
    """Custom type ciscoScsiIntrDevAccMode based on Integer32"""
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


_CiscoScsiIntrDevAccMode_Type.__name__ = "Integer32"
_CiscoScsiIntrDevAccMode_Object = MibTableColumn
ciscoScsiIntrDevAccMode = _CiscoScsiIntrDevAccMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 1, 1, 1),
    _CiscoScsiIntrDevAccMode_Type()
)
ciscoScsiIntrDevAccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoScsiIntrDevAccMode.setStatus("current")
_CiscoScsiIntrDevOutResets_Type = Counter32
_CiscoScsiIntrDevOutResets_Object = MibTableColumn
ciscoScsiIntrDevOutResets = _CiscoScsiIntrDevOutResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 1, 1, 2),
    _CiscoScsiIntrDevOutResets_Type()
)
ciscoScsiIntrDevOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrDevOutResets.setStatus("current")
_CiscoScsiIntrPrtTable_Object = MibTable
ciscoScsiIntrPrtTable = _CiscoScsiIntrPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtTable.setStatus("current")
_CiscoScsiIntrPrtEntry_Object = MibTableRow
ciscoScsiIntrPrtEntry = _CiscoScsiIntrPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1)
)
ciscoScsiIntrPrtEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiPortIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtEntry.setStatus("current")
_CiscoScsiIntrPrtName_Type = ScsiName
_CiscoScsiIntrPrtName_Object = MibTableColumn
ciscoScsiIntrPrtName = _CiscoScsiIntrPrtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 1),
    _CiscoScsiIntrPrtName_Type()
)
ciscoScsiIntrPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtName.setStatus("current")
_CiscoScsiIntrPrtIdentifier_Type = ScsiIdentifier
_CiscoScsiIntrPrtIdentifier_Object = MibTableColumn
ciscoScsiIntrPrtIdentifier = _CiscoScsiIntrPrtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 2),
    _CiscoScsiIntrPrtIdentifier_Type()
)
ciscoScsiIntrPrtIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtIdentifier.setStatus("current")
_CiscoScsiIntrPrtOutCommands_Type = Counter32
_CiscoScsiIntrPrtOutCommands_Object = MibTableColumn
ciscoScsiIntrPrtOutCommands = _CiscoScsiIntrPrtOutCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 3),
    _CiscoScsiIntrPrtOutCommands_Type()
)
ciscoScsiIntrPrtOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtOutCommands.setUnits("commands")
_CiscoScsiIntrPrtWrMegaBytes_Type = Counter32
_CiscoScsiIntrPrtWrMegaBytes_Object = MibTableColumn
ciscoScsiIntrPrtWrMegaBytes = _CiscoScsiIntrPrtWrMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 4),
    _CiscoScsiIntrPrtWrMegaBytes_Type()
)
ciscoScsiIntrPrtWrMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtWrMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtWrMegaBytes.setUnits("Megabytes")
_CiscoScsiIntrPrtReadMegaBytes_Type = Counter32
_CiscoScsiIntrPrtReadMegaBytes_Object = MibTableColumn
ciscoScsiIntrPrtReadMegaBytes = _CiscoScsiIntrPrtReadMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 5),
    _CiscoScsiIntrPrtReadMegaBytes_Type()
)
ciscoScsiIntrPrtReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtReadMegaBytes.setUnits("Megabytes")
_CiscoScsiIntrPrtHSOutCommands_Type = Counter64
_CiscoScsiIntrPrtHSOutCommands_Object = MibTableColumn
ciscoScsiIntrPrtHSOutCommands = _CiscoScsiIntrPrtHSOutCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 3, 1, 6),
    _CiscoScsiIntrPrtHSOutCommands_Type()
)
ciscoScsiIntrPrtHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiIntrPrtHSOutCommands.setUnits("commands")
_CiscoScsiRemoteTarget_ObjectIdentity = ObjectIdentity
ciscoScsiRemoteTarget = _CiscoScsiRemoteTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4)
)
_CiscoScsiDscTgtTable_Object = MibTable
ciscoScsiDscTgtTable = _CiscoScsiDscTgtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiDscTgtTable.setStatus("current")
_CiscoScsiDscTgtEntry_Object = MibTableRow
ciscoScsiDscTgtEntry = _CiscoScsiDscTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1)
)
ciscoScsiDscTgtEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIntrPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiDscTgtEntry.setStatus("current")
_CiscoScsiDscTgtIntrPortIndex_Type = ScsiPortIndexValueOrZero
_CiscoScsiDscTgtIntrPortIndex_Object = MibTableColumn
ciscoScsiDscTgtIntrPortIndex = _CiscoScsiDscTgtIntrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 1),
    _CiscoScsiDscTgtIntrPortIndex_Type()
)
ciscoScsiDscTgtIntrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtIntrPortIndex.setStatus("current")
_CiscoScsiDscTgtIndex_Type = ScsiIndexValue
_CiscoScsiDscTgtIndex_Object = MibTableColumn
ciscoScsiDscTgtIndex = _CiscoScsiDscTgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 2),
    _CiscoScsiDscTgtIndex_Type()
)
ciscoScsiDscTgtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtIndex.setStatus("current")
_CiscoScsiDscTgtDevOrPort_Type = ScsiDeviceOrPort
_CiscoScsiDscTgtDevOrPort_Object = MibTableColumn
ciscoScsiDscTgtDevOrPort = _CiscoScsiDscTgtDevOrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 3),
    _CiscoScsiDscTgtDevOrPort_Type()
)
ciscoScsiDscTgtDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtDevOrPort.setStatus("current")
_CiscoScsiDscTgtName_Type = ScsiName
_CiscoScsiDscTgtName_Object = MibTableColumn
ciscoScsiDscTgtName = _CiscoScsiDscTgtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 4),
    _CiscoScsiDscTgtName_Type()
)
ciscoScsiDscTgtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtName.setStatus("current")


class _CiscoScsiDscTgtConfigured_Type(TruthValue):
    """Custom type ciscoScsiDscTgtConfigured based on TruthValue"""


_CiscoScsiDscTgtConfigured_Object = MibTableColumn
ciscoScsiDscTgtConfigured = _CiscoScsiDscTgtConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 5),
    _CiscoScsiDscTgtConfigured_Type()
)
ciscoScsiDscTgtConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtConfigured.setStatus("current")
_CiscoScsiDscTgtDiscovered_Type = TruthValue
_CiscoScsiDscTgtDiscovered_Object = MibTableColumn
ciscoScsiDscTgtDiscovered = _CiscoScsiDscTgtDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 6),
    _CiscoScsiDscTgtDiscovered_Type()
)
ciscoScsiDscTgtDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtDiscovered.setStatus("current")
_CiscoScsiDscTgtInCommands_Type = Counter32
_CiscoScsiDscTgtInCommands_Object = MibTableColumn
ciscoScsiDscTgtInCommands = _CiscoScsiDscTgtInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 7),
    _CiscoScsiDscTgtInCommands_Type()
)
ciscoScsiDscTgtInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtInCommands.setUnits("commands")
_CiscoScsiDscTgtWrMegaBytes_Type = Counter32
_CiscoScsiDscTgtWrMegaBytes_Object = MibTableColumn
ciscoScsiDscTgtWrMegaBytes = _CiscoScsiDscTgtWrMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 8),
    _CiscoScsiDscTgtWrMegaBytes_Type()
)
ciscoScsiDscTgtWrMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtWrMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtWrMegaBytes.setUnits("Megabytes")
_CiscoScsiDscTgtReadMegaBytes_Type = Counter32
_CiscoScsiDscTgtReadMegaBytes_Object = MibTableColumn
ciscoScsiDscTgtReadMegaBytes = _CiscoScsiDscTgtReadMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 9),
    _CiscoScsiDscTgtReadMegaBytes_Type()
)
ciscoScsiDscTgtReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtReadMegaBytes.setUnits("Megabytes")
_CiscoScsiDscTgtHSInCommands_Type = Counter64
_CiscoScsiDscTgtHSInCommands_Object = MibTableColumn
ciscoScsiDscTgtHSInCommands = _CiscoScsiDscTgtHSInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 10),
    _CiscoScsiDscTgtHSInCommands_Type()
)
ciscoScsiDscTgtHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtHSInCommands.setUnits("commands")
_CiscoScsiDscTgtLastCreation_Type = TimeStamp
_CiscoScsiDscTgtLastCreation_Object = MibTableColumn
ciscoScsiDscTgtLastCreation = _CiscoScsiDscTgtLastCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 11),
    _CiscoScsiDscTgtLastCreation_Type()
)
ciscoScsiDscTgtLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtLastCreation.setStatus("current")
_CiscoScsiDscTgtRowStatus_Type = RowStatus
_CiscoScsiDscTgtRowStatus_Object = MibTableColumn
ciscoScsiDscTgtRowStatus = _CiscoScsiDscTgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 1, 1, 12),
    _CiscoScsiDscTgtRowStatus_Type()
)
ciscoScsiDscTgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiDscTgtRowStatus.setStatus("current")
_CiscoScsiDscLunTable_Object = MibTable
ciscoScsiDscLunTable = _CiscoScsiDscLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiDscLunTable.setStatus("current")
_CiscoScsiDscLunEntry_Object = MibTableRow
ciscoScsiDscLunEntry = _CiscoScsiDscLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 2, 1)
)
ciscoScsiDscLunEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIntrPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscLunIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiDscLunEntry.setStatus("current")
_CiscoScsiDscLunIndex_Type = ScsiIndexValue
_CiscoScsiDscLunIndex_Object = MibTableColumn
ciscoScsiDscLunIndex = _CiscoScsiDscLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 2, 1, 1),
    _CiscoScsiDscLunIndex_Type()
)
ciscoScsiDscLunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIndex.setStatus("current")
_CiscoScsiDscLunLun_Type = ScsiLUNOrZero
_CiscoScsiDscLunLun_Object = MibTableColumn
ciscoScsiDscLunLun = _CiscoScsiDscLunLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 2, 1, 2),
    _CiscoScsiDscLunLun_Type()
)
ciscoScsiDscLunLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscLunLun.setStatus("current")
_CiscoScsiDscLunIdTable_Object = MibTable
ciscoScsiDscLunIdTable = _CiscoScsiDscLunIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdTable.setStatus("current")
_CiscoScsiDscLunIdEntry_Object = MibTableRow
ciscoScsiDscLunIdEntry = _CiscoScsiDscLunIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1)
)
ciscoScsiDscLunIdEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIntrPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscTgtIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscLunIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDscLunIdIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdEntry.setStatus("current")
_CiscoScsiDscLunIdIndex_Type = ScsiIndexValue
_CiscoScsiDscLunIdIndex_Object = MibTableColumn
ciscoScsiDscLunIdIndex = _CiscoScsiDscLunIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1, 1),
    _CiscoScsiDscLunIdIndex_Type()
)
ciscoScsiDscLunIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdIndex.setStatus("current")
_CiscoScsiDscLunIdCodeSet_Type = ScsiIdCodeSet
_CiscoScsiDscLunIdCodeSet_Object = MibTableColumn
ciscoScsiDscLunIdCodeSet = _CiscoScsiDscLunIdCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1, 2),
    _CiscoScsiDscLunIdCodeSet_Type()
)
ciscoScsiDscLunIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdCodeSet.setStatus("current")
_CiscoScsiDscLunIdAssociation_Type = ScsiIdAssociation
_CiscoScsiDscLunIdAssociation_Object = MibTableColumn
ciscoScsiDscLunIdAssociation = _CiscoScsiDscLunIdAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1, 3),
    _CiscoScsiDscLunIdAssociation_Type()
)
ciscoScsiDscLunIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdAssociation.setStatus("current")
_CiscoScsiDscLunIdType_Type = ScsiIdType
_CiscoScsiDscLunIdType_Object = MibTableColumn
ciscoScsiDscLunIdType = _CiscoScsiDscLunIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1, 4),
    _CiscoScsiDscLunIdType_Type()
)
ciscoScsiDscLunIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdType.setStatus("current")
_CiscoScsiDscLunIdValue_Type = ScsiIdValue
_CiscoScsiDscLunIdValue_Object = MibTableColumn
ciscoScsiDscLunIdValue = _CiscoScsiDscLunIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 3, 1, 5),
    _CiscoScsiDscLunIdValue_Type()
)
ciscoScsiDscLunIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiDscLunIdValue.setStatus("current")
_CiscoScsiAttTgtPortTable_Object = MibTable
ciscoScsiAttTgtPortTable = _CiscoScsiAttTgtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortTable.setStatus("current")
_CiscoScsiAttTgtPortEntry_Object = MibTableRow
ciscoScsiAttTgtPortEntry = _CiscoScsiAttTgtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6, 1)
)
ciscoScsiAttTgtPortEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiAttTgtPortIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortEntry.setStatus("current")
_CiscoScsiAttTgtPortIndex_Type = ScsiIndexValue
_CiscoScsiAttTgtPortIndex_Object = MibTableColumn
ciscoScsiAttTgtPortIndex = _CiscoScsiAttTgtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6, 1, 1),
    _CiscoScsiAttTgtPortIndex_Type()
)
ciscoScsiAttTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortIndex.setStatus("current")
_CiscoScsiAttTgtPortDscTgtIdx_Type = ScsiIndexValueOrZero
_CiscoScsiAttTgtPortDscTgtIdx_Object = MibTableColumn
ciscoScsiAttTgtPortDscTgtIdx = _CiscoScsiAttTgtPortDscTgtIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6, 1, 2),
    _CiscoScsiAttTgtPortDscTgtIdx_Type()
)
ciscoScsiAttTgtPortDscTgtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortDscTgtIdx.setStatus("current")
_CiscoScsiAttTgtPortName_Type = ScsiName
_CiscoScsiAttTgtPortName_Object = MibTableColumn
ciscoScsiAttTgtPortName = _CiscoScsiAttTgtPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6, 1, 3),
    _CiscoScsiAttTgtPortName_Type()
)
ciscoScsiAttTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortName.setStatus("current")
_CiscoScsiAttTgtPortIdentifier_Type = ScsiIdentifier
_CiscoScsiAttTgtPortIdentifier_Object = MibTableColumn
ciscoScsiAttTgtPortIdentifier = _CiscoScsiAttTgtPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 3, 4, 6, 1, 4),
    _CiscoScsiAttTgtPortIdentifier_Type()
)
ciscoScsiAttTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttTgtPortIdentifier.setStatus("current")
_CiscoScsiTarget_ObjectIdentity = ObjectIdentity
ciscoScsiTarget = _CiscoScsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4)
)
_CiscoScsiTgtDevTable_Object = MibTable
ciscoScsiTgtDevTable = _CiscoScsiTgtDevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiTgtDevTable.setStatus("current")
_CiscoScsiTgtDevEntry_Object = MibTableRow
ciscoScsiTgtDevEntry = _CiscoScsiTgtDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 1, 1)
)
ciscoScsiTgtDevEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiTgtDevEntry.setStatus("current")
_CiscoScsiTgtDevNumberOfLUs_Type = Gauge32
_CiscoScsiTgtDevNumberOfLUs_Object = MibTableColumn
ciscoScsiTgtDevNumberOfLUs = _CiscoScsiTgtDevNumberOfLUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 1, 1, 1),
    _CiscoScsiTgtDevNumberOfLUs_Type()
)
ciscoScsiTgtDevNumberOfLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtDevNumberOfLUs.setStatus("current")


class _CiscoScsiTgtDeviceStatus_Type(Integer32):
    """Custom type ciscoScsiTgtDeviceStatus based on Integer32"""
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


_CiscoScsiTgtDeviceStatus_Type.__name__ = "Integer32"
_CiscoScsiTgtDeviceStatus_Object = MibTableColumn
ciscoScsiTgtDeviceStatus = _CiscoScsiTgtDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 1, 1, 2),
    _CiscoScsiTgtDeviceStatus_Type()
)
ciscoScsiTgtDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtDeviceStatus.setStatus("current")
_CiscoScsiTgtDevNonAccLUs_Type = Gauge32
_CiscoScsiTgtDevNonAccLUs_Object = MibTableColumn
ciscoScsiTgtDevNonAccLUs = _CiscoScsiTgtDevNonAccLUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 1, 1, 3),
    _CiscoScsiTgtDevNonAccLUs_Type()
)
ciscoScsiTgtDevNonAccLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtDevNonAccLUs.setStatus("current")
_CiscoScsiTgtPortTable_Object = MibTable
ciscoScsiTgtPortTable = _CiscoScsiTgtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiTgtPortTable.setStatus("current")
_CiscoScsiTgtPortEntry_Object = MibTableRow
ciscoScsiTgtPortEntry = _CiscoScsiTgtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1)
)
ciscoScsiTgtPortEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiPortIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiTgtPortEntry.setStatus("current")
_CiscoScsiTgtPortName_Type = ScsiName
_CiscoScsiTgtPortName_Object = MibTableColumn
ciscoScsiTgtPortName = _CiscoScsiTgtPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 1),
    _CiscoScsiTgtPortName_Type()
)
ciscoScsiTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortName.setStatus("current")
_CiscoScsiTgtPortIdentifier_Type = ScsiIdentifier
_CiscoScsiTgtPortIdentifier_Object = MibTableColumn
ciscoScsiTgtPortIdentifier = _CiscoScsiTgtPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 2),
    _CiscoScsiTgtPortIdentifier_Type()
)
ciscoScsiTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortIdentifier.setStatus("current")
_CiscoScsiTgtPortInCommands_Type = Counter32
_CiscoScsiTgtPortInCommands_Object = MibTableColumn
ciscoScsiTgtPortInCommands = _CiscoScsiTgtPortInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 3),
    _CiscoScsiTgtPortInCommands_Type()
)
ciscoScsiTgtPortInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortInCommands.setUnits("commands")
_CiscoScsiTgtPortWrMegaBytes_Type = Counter32
_CiscoScsiTgtPortWrMegaBytes_Object = MibTableColumn
ciscoScsiTgtPortWrMegaBytes = _CiscoScsiTgtPortWrMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 4),
    _CiscoScsiTgtPortWrMegaBytes_Type()
)
ciscoScsiTgtPortWrMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortWrMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortWrMegaBytes.setUnits("Megabytes")
_CiscoScsiTgtPortReadMegaBytes_Type = Counter32
_CiscoScsiTgtPortReadMegaBytes_Object = MibTableColumn
ciscoScsiTgtPortReadMegaBytes = _CiscoScsiTgtPortReadMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 5),
    _CiscoScsiTgtPortReadMegaBytes_Type()
)
ciscoScsiTgtPortReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortReadMegaBytes.setUnits("Megabytes")
_CiscoScsiTgtPortHSInCommands_Type = Counter64
_CiscoScsiTgtPortHSInCommands_Object = MibTableColumn
ciscoScsiTgtPortHSInCommands = _CiscoScsiTgtPortHSInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 2, 1, 6),
    _CiscoScsiTgtPortHSInCommands_Type()
)
ciscoScsiTgtPortHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiTgtPortHSInCommands.setUnits("commands")
_CiscoScsiRemoteInitiators_ObjectIdentity = ObjectIdentity
ciscoScsiRemoteInitiators = _CiscoScsiRemoteInitiators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3)
)
_CiscoScsiAuthorizedIntrTable_Object = MibTable
ciscoScsiAuthorizedIntrTable = _CiscoScsiAuthorizedIntrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiAuthorizedIntrTable.setStatus("current")
_CiscoScsiAuthorizedIntrEntry_Object = MibTableRow
ciscoScsiAuthorizedIntrEntry = _CiscoScsiAuthorizedIntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1)
)
ciscoScsiAuthorizedIntrEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiAuthIntrTgtPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiAuthIntrIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiAuthorizedIntrEntry.setStatus("current")
_CiscoScsiAuthIntrTgtPortIndex_Type = ScsiPortIndexValueOrZero
_CiscoScsiAuthIntrTgtPortIndex_Object = MibTableColumn
ciscoScsiAuthIntrTgtPortIndex = _CiscoScsiAuthIntrTgtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 1),
    _CiscoScsiAuthIntrTgtPortIndex_Type()
)
ciscoScsiAuthIntrTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrTgtPortIndex.setStatus("current")
_CiscoScsiAuthIntrIndex_Type = ScsiIndexValue
_CiscoScsiAuthIntrIndex_Object = MibTableColumn
ciscoScsiAuthIntrIndex = _CiscoScsiAuthIntrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 2),
    _CiscoScsiAuthIntrIndex_Type()
)
ciscoScsiAuthIntrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrIndex.setStatus("current")
_CiscoScsiAuthIntrDevOrPort_Type = ScsiDeviceOrPort
_CiscoScsiAuthIntrDevOrPort_Object = MibTableColumn
ciscoScsiAuthIntrDevOrPort = _CiscoScsiAuthIntrDevOrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 3),
    _CiscoScsiAuthIntrDevOrPort_Type()
)
ciscoScsiAuthIntrDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrDevOrPort.setStatus("current")
_CiscoScsiAuthIntrName_Type = ScsiName
_CiscoScsiAuthIntrName_Object = MibTableColumn
ciscoScsiAuthIntrName = _CiscoScsiAuthIntrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 4),
    _CiscoScsiAuthIntrName_Type()
)
ciscoScsiAuthIntrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrName.setStatus("current")
_CiscoScsiAuthIntrLunMapIndex_Type = ScsiIndexValueOrZero
_CiscoScsiAuthIntrLunMapIndex_Object = MibTableColumn
ciscoScsiAuthIntrLunMapIndex = _CiscoScsiAuthIntrLunMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 5),
    _CiscoScsiAuthIntrLunMapIndex_Type()
)
ciscoScsiAuthIntrLunMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrLunMapIndex.setStatus("current")
_CiscoScsiAuthIntrAttachedTimes_Type = Counter32
_CiscoScsiAuthIntrAttachedTimes_Object = MibTableColumn
ciscoScsiAuthIntrAttachedTimes = _CiscoScsiAuthIntrAttachedTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 6),
    _CiscoScsiAuthIntrAttachedTimes_Type()
)
ciscoScsiAuthIntrAttachedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrAttachedTimes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrAttachedTimes.setUnits("Times")
_CiscoScsiAuthIntrOutCommands_Type = Counter32
_CiscoScsiAuthIntrOutCommands_Object = MibTableColumn
ciscoScsiAuthIntrOutCommands = _CiscoScsiAuthIntrOutCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 7),
    _CiscoScsiAuthIntrOutCommands_Type()
)
ciscoScsiAuthIntrOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrOutCommands.setUnits("commands")
_CiscoScsiAuthIntrReadMegaBytes_Type = Counter32
_CiscoScsiAuthIntrReadMegaBytes_Object = MibTableColumn
ciscoScsiAuthIntrReadMegaBytes = _CiscoScsiAuthIntrReadMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 8),
    _CiscoScsiAuthIntrReadMegaBytes_Type()
)
ciscoScsiAuthIntrReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrReadMegaBytes.setUnits("Megabytes")
_CiscoScsiAuthIntrWrMegaBytes_Type = Counter32
_CiscoScsiAuthIntrWrMegaBytes_Object = MibTableColumn
ciscoScsiAuthIntrWrMegaBytes = _CiscoScsiAuthIntrWrMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 9),
    _CiscoScsiAuthIntrWrMegaBytes_Type()
)
ciscoScsiAuthIntrWrMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrWrMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrWrMegaBytes.setUnits("Megabytes")
_CiscoScsiAuthIntrHSOutCommands_Type = Counter64
_CiscoScsiAuthIntrHSOutCommands_Object = MibTableColumn
ciscoScsiAuthIntrHSOutCommands = _CiscoScsiAuthIntrHSOutCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 10),
    _CiscoScsiAuthIntrHSOutCommands_Type()
)
ciscoScsiAuthIntrHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrHSOutCommands.setUnits("commands")
_CiscoScsiAuthIntrLastCreation_Type = TimeStamp
_CiscoScsiAuthIntrLastCreation_Object = MibTableColumn
ciscoScsiAuthIntrLastCreation = _CiscoScsiAuthIntrLastCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 11),
    _CiscoScsiAuthIntrLastCreation_Type()
)
ciscoScsiAuthIntrLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrLastCreation.setStatus("current")
_CiscoScsiAuthIntrRowStatus_Type = RowStatus
_CiscoScsiAuthIntrRowStatus_Object = MibTableColumn
ciscoScsiAuthIntrRowStatus = _CiscoScsiAuthIntrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 1, 1, 12),
    _CiscoScsiAuthIntrRowStatus_Type()
)
ciscoScsiAuthIntrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiAuthIntrRowStatus.setStatus("current")
_CiscoScsiAttIntrPrtTable_Object = MibTable
ciscoScsiAttIntrPrtTable = _CiscoScsiAttIntrPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtTable.setStatus("current")
_CiscoScsiAttIntrPrtEntry_Object = MibTableRow
ciscoScsiAttIntrPrtEntry = _CiscoScsiAttIntrPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2, 1)
)
ciscoScsiAttIntrPrtEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiPortIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiAttIntrPrtIdx"),
)
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtEntry.setStatus("current")
_CiscoScsiAttIntrPrtIdx_Type = ScsiIndexValue
_CiscoScsiAttIntrPrtIdx_Object = MibTableColumn
ciscoScsiAttIntrPrtIdx = _CiscoScsiAttIntrPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2, 1, 1),
    _CiscoScsiAttIntrPrtIdx_Type()
)
ciscoScsiAttIntrPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtIdx.setStatus("current")
_CiscoScsiAttIntrPrtAuthIntrIdx_Type = ScsiIndexValueOrZero
_CiscoScsiAttIntrPrtAuthIntrIdx_Object = MibTableColumn
ciscoScsiAttIntrPrtAuthIntrIdx = _CiscoScsiAttIntrPrtAuthIntrIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2, 1, 2),
    _CiscoScsiAttIntrPrtAuthIntrIdx_Type()
)
ciscoScsiAttIntrPrtAuthIntrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtAuthIntrIdx.setStatus("current")
_CiscoScsiAttIntrPrtName_Type = ScsiName
_CiscoScsiAttIntrPrtName_Object = MibTableColumn
ciscoScsiAttIntrPrtName = _CiscoScsiAttIntrPrtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2, 1, 3),
    _CiscoScsiAttIntrPrtName_Type()
)
ciscoScsiAttIntrPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtName.setStatus("current")
_CiscoScsiAttIntrPrtId_Type = ScsiIdentifier
_CiscoScsiAttIntrPrtId_Object = MibTableColumn
ciscoScsiAttIntrPrtId = _CiscoScsiAttIntrPrtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 4, 3, 2, 1, 4),
    _CiscoScsiAttIntrPrtId_Type()
)
ciscoScsiAttIntrPrtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiAttIntrPrtId.setStatus("current")
_CiscoScsiLogicalUnit_ObjectIdentity = ObjectIdentity
ciscoScsiLogicalUnit = _CiscoScsiLogicalUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5)
)
_CiscoScsiLuTable_Object = MibTable
ciscoScsiLuTable = _CiscoScsiLuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiLuTable.setStatus("current")
_CiscoScsiLuEntry_Object = MibTableRow
ciscoScsiLuEntry = _CiscoScsiLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1)
)
ciscoScsiLuEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiLuIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiLuEntry.setStatus("current")
_CiscoScsiLuIndex_Type = ScsiIndexValue
_CiscoScsiLuIndex_Object = MibTableColumn
ciscoScsiLuIndex = _CiscoScsiLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 1),
    _CiscoScsiLuIndex_Type()
)
ciscoScsiLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiLuIndex.setStatus("current")
_CiscoScsiLuDefaultLun_Type = ScsiLUNOrZero
_CiscoScsiLuDefaultLun_Object = MibTableColumn
ciscoScsiLuDefaultLun = _CiscoScsiLuDefaultLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 2),
    _CiscoScsiLuDefaultLun_Type()
)
ciscoScsiLuDefaultLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuDefaultLun.setStatus("current")
_CiscoScsiLuWwnName_Type = ScsiNameIdOrZero
_CiscoScsiLuWwnName_Object = MibTableColumn
ciscoScsiLuWwnName = _CiscoScsiLuWwnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 3),
    _CiscoScsiLuWwnName_Type()
)
ciscoScsiLuWwnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuWwnName.setStatus("current")


class _CiscoScsiLuVendorId_Type(SnmpAdminString):
    """Custom type ciscoScsiLuVendorId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiLuVendorId_Type.__name__ = "SnmpAdminString"
_CiscoScsiLuVendorId_Object = MibTableColumn
ciscoScsiLuVendorId = _CiscoScsiLuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 4),
    _CiscoScsiLuVendorId_Type()
)
ciscoScsiLuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuVendorId.setStatus("current")


class _CiscoScsiLuProductId_Type(SnmpAdminString):
    """Custom type ciscoScsiLuProductId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiLuProductId_Type.__name__ = "SnmpAdminString"
_CiscoScsiLuProductId_Object = MibTableColumn
ciscoScsiLuProductId = _CiscoScsiLuProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 5),
    _CiscoScsiLuProductId_Type()
)
ciscoScsiLuProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuProductId.setStatus("current")


class _CiscoScsiLuRevisionId_Type(SnmpAdminString):
    """Custom type ciscoScsiLuRevisionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CiscoScsiLuRevisionId_Type.__name__ = "SnmpAdminString"
_CiscoScsiLuRevisionId_Object = MibTableColumn
ciscoScsiLuRevisionId = _CiscoScsiLuRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 6),
    _CiscoScsiLuRevisionId_Type()
)
ciscoScsiLuRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuRevisionId.setStatus("current")
_CiscoScsiLuPeripheralType_Type = Unsigned32
_CiscoScsiLuPeripheralType_Object = MibTableColumn
ciscoScsiLuPeripheralType = _CiscoScsiLuPeripheralType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 7),
    _CiscoScsiLuPeripheralType_Type()
)
ciscoScsiLuPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuPeripheralType.setStatus("current")


class _CiscoScsiLuStatus_Type(Integer32):
    """Custom type ciscoScsiLuStatus based on Integer32"""
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


_CiscoScsiLuStatus_Type.__name__ = "Integer32"
_CiscoScsiLuStatus_Object = MibTableColumn
ciscoScsiLuStatus = _CiscoScsiLuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 8),
    _CiscoScsiLuStatus_Type()
)
ciscoScsiLuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuStatus.setStatus("current")


class _CiscoScsiLuState_Type(Bits):
    """Custom type ciscoScsiLuState based on Bits"""
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

_CiscoScsiLuState_Type.__name__ = "Bits"
_CiscoScsiLuState_Object = MibTableColumn
ciscoScsiLuState = _CiscoScsiLuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 9),
    _CiscoScsiLuState_Type()
)
ciscoScsiLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuState.setStatus("current")
_CiscoScsiLuInCommands_Type = Counter32
_CiscoScsiLuInCommands_Object = MibTableColumn
ciscoScsiLuInCommands = _CiscoScsiLuInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 10),
    _CiscoScsiLuInCommands_Type()
)
ciscoScsiLuInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiLuInCommands.setUnits("commands")
_CiscoScsiLuReadMegaBytes_Type = Counter32
_CiscoScsiLuReadMegaBytes_Object = MibTableColumn
ciscoScsiLuReadMegaBytes = _CiscoScsiLuReadMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 11),
    _CiscoScsiLuReadMegaBytes_Type()
)
ciscoScsiLuReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiLuReadMegaBytes.setUnits("Megabytes")
_CiscoScsiLuWrittenMegaBytes_Type = Counter32
_CiscoScsiLuWrittenMegaBytes_Object = MibTableColumn
ciscoScsiLuWrittenMegaBytes = _CiscoScsiLuWrittenMegaBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 12),
    _CiscoScsiLuWrittenMegaBytes_Type()
)
ciscoScsiLuWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiLuWrittenMegaBytes.setUnits("Megabytes")
_CiscoScsiLuInResets_Type = Counter32
_CiscoScsiLuInResets_Object = MibTableColumn
ciscoScsiLuInResets = _CiscoScsiLuInResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 13),
    _CiscoScsiLuInResets_Type()
)
ciscoScsiLuInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuInResets.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiLuInResets.setUnits("resets")
_CiscoScsiLuOutQueueFullStatus_Type = Counter32
_CiscoScsiLuOutQueueFullStatus_Object = MibTableColumn
ciscoScsiLuOutQueueFullStatus = _CiscoScsiLuOutQueueFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 14),
    _CiscoScsiLuOutQueueFullStatus_Type()
)
ciscoScsiLuOutQueueFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuOutQueueFullStatus.setStatus("current")
_CiscoScsiLuHSInCommands_Type = Counter64
_CiscoScsiLuHSInCommands_Object = MibTableColumn
ciscoScsiLuHSInCommands = _CiscoScsiLuHSInCommands_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 1, 1, 15),
    _CiscoScsiLuHSInCommands_Type()
)
ciscoScsiLuHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    ciscoScsiLuHSInCommands.setUnits("commands")
_CiscoScsiLuIdTable_Object = MibTable
ciscoScsiLuIdTable = _CiscoScsiLuIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiLuIdTable.setStatus("current")
_CiscoScsiLuIdEntry_Object = MibTableRow
ciscoScsiLuIdEntry = _CiscoScsiLuIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1)
)
ciscoScsiLuIdEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiLuIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiLuIdIndex"),
)
if mibBuilder.loadTexts:
    ciscoScsiLuIdEntry.setStatus("current")
_CiscoScsiLuIdIndex_Type = ScsiIndexValue
_CiscoScsiLuIdIndex_Object = MibTableColumn
ciscoScsiLuIdIndex = _CiscoScsiLuIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1, 1),
    _CiscoScsiLuIdIndex_Type()
)
ciscoScsiLuIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiLuIdIndex.setStatus("current")
_CiscoScsiLuIdCodeSet_Type = ScsiIdCodeSet
_CiscoScsiLuIdCodeSet_Object = MibTableColumn
ciscoScsiLuIdCodeSet = _CiscoScsiLuIdCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1, 2),
    _CiscoScsiLuIdCodeSet_Type()
)
ciscoScsiLuIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuIdCodeSet.setStatus("current")
_CiscoScsiLuIdAssociation_Type = ScsiIdAssociation
_CiscoScsiLuIdAssociation_Object = MibTableColumn
ciscoScsiLuIdAssociation = _CiscoScsiLuIdAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1, 3),
    _CiscoScsiLuIdAssociation_Type()
)
ciscoScsiLuIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuIdAssociation.setStatus("current")
_CiscoScsiLuIdType_Type = ScsiIdType
_CiscoScsiLuIdType_Object = MibTableColumn
ciscoScsiLuIdType = _CiscoScsiLuIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1, 4),
    _CiscoScsiLuIdType_Type()
)
ciscoScsiLuIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuIdType.setStatus("current")
_CiscoScsiLuIdValue_Type = ScsiIdValue
_CiscoScsiLuIdValue_Object = MibTableColumn
ciscoScsiLuIdValue = _CiscoScsiLuIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 2, 1, 5),
    _CiscoScsiLuIdValue_Type()
)
ciscoScsiLuIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiLuIdValue.setStatus("current")
_CiscoScsiLunMapTable_Object = MibTable
ciscoScsiLunMapTable = _CiscoScsiLunMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ciscoScsiLunMapTable.setStatus("current")
_CiscoScsiLunMapEntry_Object = MibTableRow
ciscoScsiLunMapEntry = _CiscoScsiLunMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3, 1)
)
ciscoScsiLunMapEntry.setIndexNames(
    (0, "CISCO-SCSI-MIB", "ciscoScsiInstIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiDeviceIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiLunMapIndex"),
    (0, "CISCO-SCSI-MIB", "ciscoScsiLunMapLun"),
)
if mibBuilder.loadTexts:
    ciscoScsiLunMapEntry.setStatus("current")
_CiscoScsiLunMapIndex_Type = ScsiIndexValue
_CiscoScsiLunMapIndex_Object = MibTableColumn
ciscoScsiLunMapIndex = _CiscoScsiLunMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3, 1, 1),
    _CiscoScsiLunMapIndex_Type()
)
ciscoScsiLunMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiLunMapIndex.setStatus("current")
_CiscoScsiLunMapLun_Type = ScsiLUNOrZero
_CiscoScsiLunMapLun_Object = MibTableColumn
ciscoScsiLunMapLun = _CiscoScsiLunMapLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3, 1, 2),
    _CiscoScsiLunMapLun_Type()
)
ciscoScsiLunMapLun.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiLunMapLun.setStatus("current")
_CiscoScsiLunMapLuIndex_Type = ScsiIndexValue
_CiscoScsiLunMapLuIndex_Object = MibTableColumn
ciscoScsiLunMapLuIndex = _CiscoScsiLunMapLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3, 1, 3),
    _CiscoScsiLunMapLuIndex_Type()
)
ciscoScsiLunMapLuIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiLunMapLuIndex.setStatus("current")
_CiscoScsiLunMapRowStatus_Type = RowStatus
_CiscoScsiLunMapRowStatus_Object = MibTableColumn
ciscoScsiLunMapRowStatus = _CiscoScsiLunMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 1, 5, 3, 1, 4),
    _CiscoScsiLunMapRowStatus_Type()
)
ciscoScsiLunMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiLunMapRowStatus.setStatus("current")
_CiscoScsiNotification_ObjectIdentity = ObjectIdentity
ciscoScsiNotification = _CiscoScsiNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 2)
)
_CiscoScsiNotifications_ObjectIdentity = ObjectIdentity
ciscoScsiNotifications = _CiscoScsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 2, 0)
)
_CiscoScsiConformance_ObjectIdentity = ObjectIdentity
ciscoScsiConformance = _CiscoScsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3)
)
_CiscoScsiCompliances_ObjectIdentity = ObjectIdentity
ciscoScsiCompliances = _CiscoScsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 1)
)
_CiscoScsiGroups_ObjectIdentity = ObjectIdentity
ciscoScsiGroups = _CiscoScsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2)
)

# Managed Objects groups

ciscoScsiDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 1)
)
ciscoScsiDeviceGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiInstAlias"),
        ("CISCO-SCSI-MIB", "ciscoScsiInstSoftwareIndex"),
        ("CISCO-SCSI-MIB", "ciscoScsiInstVendorVersion"),
        ("CISCO-SCSI-MIB", "ciscoScsiInstNotifEnable"),
        ("CISCO-SCSI-MIB", "ciscoScsiDeviceAlias"),
        ("CISCO-SCSI-MIB", "ciscoScsiDeviceRole"),
        ("CISCO-SCSI-MIB", "ciscoScsiDevicePortNumber"),
        ("CISCO-SCSI-MIB", "ciscoScsiPortRole"),
        ("CISCO-SCSI-MIB", "ciscoScsiPortTrnsptPtr"),
        ("CISCO-SCSI-MIB", "ciscoScsiTrnsptType"),
        ("CISCO-SCSI-MIB", "ciscoScsiTrnsptPointer"),
        ("CISCO-SCSI-MIB", "ciscoScsiTrnsptDevName"))
)
if mibBuilder.loadTexts:
    ciscoScsiDeviceGroup.setStatus("current")

ciscoScsiInitiatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 2)
)
ciscoScsiInitiatorGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiIntrDevAccMode"),
        ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtName"),
        ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtIdentifier"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttTgtPortDscTgtIdx"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttTgtPortName"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttTgtPortIdentifier"))
)
if mibBuilder.loadTexts:
    ciscoScsiInitiatorGroup.setStatus("current")

ciscoScsiDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 3)
)
ciscoScsiDiscoveryGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiDscTgtDevOrPort"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtName"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtConfigured"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtDiscovered"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtRowStatus"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtLastCreation"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscLunLun"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscLunIdCodeSet"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscLunIdAssociation"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscLunIdType"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscLunIdValue"))
)
if mibBuilder.loadTexts:
    ciscoScsiDiscoveryGroup.setStatus("current")

ciscoScsiTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 4)
)
ciscoScsiTargetGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiTgtDevNumberOfLUs"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtDeviceStatus"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtDevNonAccLUs"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtPortName"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtPortIdentifier"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttIntrPrtAuthIntrIdx"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttIntrPrtName"),
        ("CISCO-SCSI-MIB", "ciscoScsiAttIntrPrtId"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuDefaultLun"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuWwnName"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuVendorId"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuProductId"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuRevisionId"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuPeripheralType"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuStatus"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuState"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuIdCodeSet"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuIdAssociation"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuIdType"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuIdValue"))
)
if mibBuilder.loadTexts:
    ciscoScsiTargetGroup.setStatus("current")

ciscoScsiLunMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 5)
)
ciscoScsiLunMapGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiLunMapLuIndex"),
        ("CISCO-SCSI-MIB", "ciscoScsiLunMapRowStatus"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrDevOrPort"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrName"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrLunMapIndex"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrLastCreation"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoScsiLunMapGroup.setStatus("current")

ciscoScsiTargetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 6)
)
ciscoScsiTargetStatsGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiTgtPortInCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtPortWrMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiTgtPortReadMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuInCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuReadMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuWrittenMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuInResets"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuOutQueueFullStatus"))
)
if mibBuilder.loadTexts:
    ciscoScsiTargetStatsGroup.setStatus("current")

ciscoScsiTargetHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 7)
)
ciscoScsiTargetHSStatsGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiTgtPortHSInCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuHSInCommands"))
)
if mibBuilder.loadTexts:
    ciscoScsiTargetHSStatsGroup.setStatus("current")

ciscoScsiLunMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 8)
)
ciscoScsiLunMapStatsGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiAuthIntrAttachedTimes"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrOutCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrReadMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrWrMegaBytes"))
)
if mibBuilder.loadTexts:
    ciscoScsiLunMapStatsGroup.setStatus("current")

ciscoScsiLunMapHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 9)
)
ciscoScsiLunMapHSStatsGroup.setObjects(
    ("CISCO-SCSI-MIB", "ciscoScsiAuthIntrHSOutCommands")
)
if mibBuilder.loadTexts:
    ciscoScsiLunMapHSStatsGroup.setStatus("current")

ciscoScsiInitiatorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 10)
)
ciscoScsiInitiatorStatsGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiIntrDevOutResets"),
        ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtOutCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtWrMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtReadMegaBytes"))
)
if mibBuilder.loadTexts:
    ciscoScsiInitiatorStatsGroup.setStatus("current")

ciscoScsiInitiatorHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 11)
)
ciscoScsiInitiatorHSStatsGroup.setObjects(
    ("CISCO-SCSI-MIB", "ciscoScsiIntrPrtHSOutCommands")
)
if mibBuilder.loadTexts:
    ciscoScsiInitiatorHSStatsGroup.setStatus("current")

ciscoScsiDiscoveryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 12)
)
ciscoScsiDiscoveryStatsGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiDscTgtInCommands"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtReadMegaBytes"),
        ("CISCO-SCSI-MIB", "ciscoScsiDscTgtWrMegaBytes"))
)
if mibBuilder.loadTexts:
    ciscoScsiDiscoveryStatsGroup.setStatus("current")

ciscoScsiDiscoveryHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 13)
)
ciscoScsiDiscoveryHSStatsGroup.setObjects(
    ("CISCO-SCSI-MIB", "ciscoScsiDscTgtHSInCommands")
)
if mibBuilder.loadTexts:
    ciscoScsiDiscoveryHSStatsGroup.setStatus("current")

ciscoScsiDeviceStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 14)
)
ciscoScsiDeviceStatGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiDeviceResets"),
        ("CISCO-SCSI-MIB", "ciscoScsiPortBusyStatuses"))
)
if mibBuilder.loadTexts:
    ciscoScsiDeviceStatGroup.setStatus("current")


# Notification objects

ciscoScsiTgtDevStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 2, 0, 1)
)
ciscoScsiTgtDevStatusChanged.setObjects(
    ("CISCO-SCSI-MIB", "ciscoScsiTgtDeviceStatus")
)
if mibBuilder.loadTexts:
    ciscoScsiTgtDevStatusChanged.setStatus(
        "current"
    )

ciscoScsiLuStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 2, 0, 2)
)
ciscoScsiLuStatusChanged.setObjects(
    ("CISCO-SCSI-MIB", "ciscoScsiLuStatus")
)
if mibBuilder.loadTexts:
    ciscoScsiLuStatusChanged.setStatus(
        "current"
    )


# Notifications groups

ciscoScsiNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 2, 15)
)
ciscoScsiNotifGroup.setObjects(
      *(("CISCO-SCSI-MIB", "ciscoScsiTgtDevStatusChanged"),
        ("CISCO-SCSI-MIB", "ciscoScsiLuStatusChanged"))
)
if mibBuilder.loadTexts:
    ciscoScsiNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoScsiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 95, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SCSI-MIB",
    **{"ScsiLUNOrZero": ScsiLUNOrZero,
       "ScsiIndexValue": ScsiIndexValue,
       "ScsiPortIndexValueOrZero": ScsiPortIndexValueOrZero,
       "ScsiIndexValueOrZero": ScsiIndexValueOrZero,
       "ScsiIdentifier": ScsiIdentifier,
       "ScsiName": ScsiName,
       "ScsiNameIdOrZero": ScsiNameIdOrZero,
       "ScsiDeviceOrPort": ScsiDeviceOrPort,
       "ScsiIdCodeSet": ScsiIdCodeSet,
       "ScsiIdAssociation": ScsiIdAssociation,
       "ScsiIdType": ScsiIdType,
       "ScsiIdValue": ScsiIdValue,
       "HrSWInstalledIndexOrZero": HrSWInstalledIndexOrZero,
       "ciscoScsiMIB": ciscoScsiMIB,
       "ciscoScsiObjects": ciscoScsiObjects,
       "ciscoScsiTransportTypes": ciscoScsiTransportTypes,
       "ciscoScsiTranportOther": ciscoScsiTranportOther,
       "ciscoScsiTranportSPI": ciscoScsiTranportSPI,
       "ciscoScsiTransportFCP": ciscoScsiTransportFCP,
       "ciscoScsiTransportSRP": ciscoScsiTransportSRP,
       "ciscoScsiTransportISCSI": ciscoScsiTransportISCSI,
       "ciscoScsiTransportSBP": ciscoScsiTransportSBP,
       "ciscoScsiGeneral": ciscoScsiGeneral,
       "ciscoScsiInstanceTable": ciscoScsiInstanceTable,
       "ciscoScsiInstanceEntry": ciscoScsiInstanceEntry,
       "ciscoScsiInstIndex": ciscoScsiInstIndex,
       "ciscoScsiInstAlias": ciscoScsiInstAlias,
       "ciscoScsiInstSoftwareIndex": ciscoScsiInstSoftwareIndex,
       "ciscoScsiInstVendorVersion": ciscoScsiInstVendorVersion,
       "ciscoScsiInstNotifEnable": ciscoScsiInstNotifEnable,
       "ciscoScsiDeviceTable": ciscoScsiDeviceTable,
       "ciscoScsiDeviceEntry": ciscoScsiDeviceEntry,
       "ciscoScsiDeviceIndex": ciscoScsiDeviceIndex,
       "ciscoScsiDeviceAlias": ciscoScsiDeviceAlias,
       "ciscoScsiDeviceRole": ciscoScsiDeviceRole,
       "ciscoScsiDevicePortNumber": ciscoScsiDevicePortNumber,
       "ciscoScsiDeviceResets": ciscoScsiDeviceResets,
       "ciscoScsiPortTable": ciscoScsiPortTable,
       "ciscoScsiPortEntry": ciscoScsiPortEntry,
       "ciscoScsiPortIndex": ciscoScsiPortIndex,
       "ciscoScsiPortRole": ciscoScsiPortRole,
       "ciscoScsiPortTrnsptPtr": ciscoScsiPortTrnsptPtr,
       "ciscoScsiPortBusyStatuses": ciscoScsiPortBusyStatuses,
       "ciscoScsiTrnsptTable": ciscoScsiTrnsptTable,
       "ciscoScsiTrnsptEntry": ciscoScsiTrnsptEntry,
       "ciscoScsiTrnsptIndex": ciscoScsiTrnsptIndex,
       "ciscoScsiTrnsptType": ciscoScsiTrnsptType,
       "ciscoScsiTrnsptPointer": ciscoScsiTrnsptPointer,
       "ciscoScsiTrnsptDevName": ciscoScsiTrnsptDevName,
       "ciscoScsiInitiator": ciscoScsiInitiator,
       "ciscoScsiIntrDevTable": ciscoScsiIntrDevTable,
       "ciscoScsiIntrDevEntry": ciscoScsiIntrDevEntry,
       "ciscoScsiIntrDevAccMode": ciscoScsiIntrDevAccMode,
       "ciscoScsiIntrDevOutResets": ciscoScsiIntrDevOutResets,
       "ciscoScsiIntrPrtTable": ciscoScsiIntrPrtTable,
       "ciscoScsiIntrPrtEntry": ciscoScsiIntrPrtEntry,
       "ciscoScsiIntrPrtName": ciscoScsiIntrPrtName,
       "ciscoScsiIntrPrtIdentifier": ciscoScsiIntrPrtIdentifier,
       "ciscoScsiIntrPrtOutCommands": ciscoScsiIntrPrtOutCommands,
       "ciscoScsiIntrPrtWrMegaBytes": ciscoScsiIntrPrtWrMegaBytes,
       "ciscoScsiIntrPrtReadMegaBytes": ciscoScsiIntrPrtReadMegaBytes,
       "ciscoScsiIntrPrtHSOutCommands": ciscoScsiIntrPrtHSOutCommands,
       "ciscoScsiRemoteTarget": ciscoScsiRemoteTarget,
       "ciscoScsiDscTgtTable": ciscoScsiDscTgtTable,
       "ciscoScsiDscTgtEntry": ciscoScsiDscTgtEntry,
       "ciscoScsiDscTgtIntrPortIndex": ciscoScsiDscTgtIntrPortIndex,
       "ciscoScsiDscTgtIndex": ciscoScsiDscTgtIndex,
       "ciscoScsiDscTgtDevOrPort": ciscoScsiDscTgtDevOrPort,
       "ciscoScsiDscTgtName": ciscoScsiDscTgtName,
       "ciscoScsiDscTgtConfigured": ciscoScsiDscTgtConfigured,
       "ciscoScsiDscTgtDiscovered": ciscoScsiDscTgtDiscovered,
       "ciscoScsiDscTgtInCommands": ciscoScsiDscTgtInCommands,
       "ciscoScsiDscTgtWrMegaBytes": ciscoScsiDscTgtWrMegaBytes,
       "ciscoScsiDscTgtReadMegaBytes": ciscoScsiDscTgtReadMegaBytes,
       "ciscoScsiDscTgtHSInCommands": ciscoScsiDscTgtHSInCommands,
       "ciscoScsiDscTgtLastCreation": ciscoScsiDscTgtLastCreation,
       "ciscoScsiDscTgtRowStatus": ciscoScsiDscTgtRowStatus,
       "ciscoScsiDscLunTable": ciscoScsiDscLunTable,
       "ciscoScsiDscLunEntry": ciscoScsiDscLunEntry,
       "ciscoScsiDscLunIndex": ciscoScsiDscLunIndex,
       "ciscoScsiDscLunLun": ciscoScsiDscLunLun,
       "ciscoScsiDscLunIdTable": ciscoScsiDscLunIdTable,
       "ciscoScsiDscLunIdEntry": ciscoScsiDscLunIdEntry,
       "ciscoScsiDscLunIdIndex": ciscoScsiDscLunIdIndex,
       "ciscoScsiDscLunIdCodeSet": ciscoScsiDscLunIdCodeSet,
       "ciscoScsiDscLunIdAssociation": ciscoScsiDscLunIdAssociation,
       "ciscoScsiDscLunIdType": ciscoScsiDscLunIdType,
       "ciscoScsiDscLunIdValue": ciscoScsiDscLunIdValue,
       "ciscoScsiAttTgtPortTable": ciscoScsiAttTgtPortTable,
       "ciscoScsiAttTgtPortEntry": ciscoScsiAttTgtPortEntry,
       "ciscoScsiAttTgtPortIndex": ciscoScsiAttTgtPortIndex,
       "ciscoScsiAttTgtPortDscTgtIdx": ciscoScsiAttTgtPortDscTgtIdx,
       "ciscoScsiAttTgtPortName": ciscoScsiAttTgtPortName,
       "ciscoScsiAttTgtPortIdentifier": ciscoScsiAttTgtPortIdentifier,
       "ciscoScsiTarget": ciscoScsiTarget,
       "ciscoScsiTgtDevTable": ciscoScsiTgtDevTable,
       "ciscoScsiTgtDevEntry": ciscoScsiTgtDevEntry,
       "ciscoScsiTgtDevNumberOfLUs": ciscoScsiTgtDevNumberOfLUs,
       "ciscoScsiTgtDeviceStatus": ciscoScsiTgtDeviceStatus,
       "ciscoScsiTgtDevNonAccLUs": ciscoScsiTgtDevNonAccLUs,
       "ciscoScsiTgtPortTable": ciscoScsiTgtPortTable,
       "ciscoScsiTgtPortEntry": ciscoScsiTgtPortEntry,
       "ciscoScsiTgtPortName": ciscoScsiTgtPortName,
       "ciscoScsiTgtPortIdentifier": ciscoScsiTgtPortIdentifier,
       "ciscoScsiTgtPortInCommands": ciscoScsiTgtPortInCommands,
       "ciscoScsiTgtPortWrMegaBytes": ciscoScsiTgtPortWrMegaBytes,
       "ciscoScsiTgtPortReadMegaBytes": ciscoScsiTgtPortReadMegaBytes,
       "ciscoScsiTgtPortHSInCommands": ciscoScsiTgtPortHSInCommands,
       "ciscoScsiRemoteInitiators": ciscoScsiRemoteInitiators,
       "ciscoScsiAuthorizedIntrTable": ciscoScsiAuthorizedIntrTable,
       "ciscoScsiAuthorizedIntrEntry": ciscoScsiAuthorizedIntrEntry,
       "ciscoScsiAuthIntrTgtPortIndex": ciscoScsiAuthIntrTgtPortIndex,
       "ciscoScsiAuthIntrIndex": ciscoScsiAuthIntrIndex,
       "ciscoScsiAuthIntrDevOrPort": ciscoScsiAuthIntrDevOrPort,
       "ciscoScsiAuthIntrName": ciscoScsiAuthIntrName,
       "ciscoScsiAuthIntrLunMapIndex": ciscoScsiAuthIntrLunMapIndex,
       "ciscoScsiAuthIntrAttachedTimes": ciscoScsiAuthIntrAttachedTimes,
       "ciscoScsiAuthIntrOutCommands": ciscoScsiAuthIntrOutCommands,
       "ciscoScsiAuthIntrReadMegaBytes": ciscoScsiAuthIntrReadMegaBytes,
       "ciscoScsiAuthIntrWrMegaBytes": ciscoScsiAuthIntrWrMegaBytes,
       "ciscoScsiAuthIntrHSOutCommands": ciscoScsiAuthIntrHSOutCommands,
       "ciscoScsiAuthIntrLastCreation": ciscoScsiAuthIntrLastCreation,
       "ciscoScsiAuthIntrRowStatus": ciscoScsiAuthIntrRowStatus,
       "ciscoScsiAttIntrPrtTable": ciscoScsiAttIntrPrtTable,
       "ciscoScsiAttIntrPrtEntry": ciscoScsiAttIntrPrtEntry,
       "ciscoScsiAttIntrPrtIdx": ciscoScsiAttIntrPrtIdx,
       "ciscoScsiAttIntrPrtAuthIntrIdx": ciscoScsiAttIntrPrtAuthIntrIdx,
       "ciscoScsiAttIntrPrtName": ciscoScsiAttIntrPrtName,
       "ciscoScsiAttIntrPrtId": ciscoScsiAttIntrPrtId,
       "ciscoScsiLogicalUnit": ciscoScsiLogicalUnit,
       "ciscoScsiLuTable": ciscoScsiLuTable,
       "ciscoScsiLuEntry": ciscoScsiLuEntry,
       "ciscoScsiLuIndex": ciscoScsiLuIndex,
       "ciscoScsiLuDefaultLun": ciscoScsiLuDefaultLun,
       "ciscoScsiLuWwnName": ciscoScsiLuWwnName,
       "ciscoScsiLuVendorId": ciscoScsiLuVendorId,
       "ciscoScsiLuProductId": ciscoScsiLuProductId,
       "ciscoScsiLuRevisionId": ciscoScsiLuRevisionId,
       "ciscoScsiLuPeripheralType": ciscoScsiLuPeripheralType,
       "ciscoScsiLuStatus": ciscoScsiLuStatus,
       "ciscoScsiLuState": ciscoScsiLuState,
       "ciscoScsiLuInCommands": ciscoScsiLuInCommands,
       "ciscoScsiLuReadMegaBytes": ciscoScsiLuReadMegaBytes,
       "ciscoScsiLuWrittenMegaBytes": ciscoScsiLuWrittenMegaBytes,
       "ciscoScsiLuInResets": ciscoScsiLuInResets,
       "ciscoScsiLuOutQueueFullStatus": ciscoScsiLuOutQueueFullStatus,
       "ciscoScsiLuHSInCommands": ciscoScsiLuHSInCommands,
       "ciscoScsiLuIdTable": ciscoScsiLuIdTable,
       "ciscoScsiLuIdEntry": ciscoScsiLuIdEntry,
       "ciscoScsiLuIdIndex": ciscoScsiLuIdIndex,
       "ciscoScsiLuIdCodeSet": ciscoScsiLuIdCodeSet,
       "ciscoScsiLuIdAssociation": ciscoScsiLuIdAssociation,
       "ciscoScsiLuIdType": ciscoScsiLuIdType,
       "ciscoScsiLuIdValue": ciscoScsiLuIdValue,
       "ciscoScsiLunMapTable": ciscoScsiLunMapTable,
       "ciscoScsiLunMapEntry": ciscoScsiLunMapEntry,
       "ciscoScsiLunMapIndex": ciscoScsiLunMapIndex,
       "ciscoScsiLunMapLun": ciscoScsiLunMapLun,
       "ciscoScsiLunMapLuIndex": ciscoScsiLunMapLuIndex,
       "ciscoScsiLunMapRowStatus": ciscoScsiLunMapRowStatus,
       "ciscoScsiNotification": ciscoScsiNotification,
       "ciscoScsiNotifications": ciscoScsiNotifications,
       "ciscoScsiTgtDevStatusChanged": ciscoScsiTgtDevStatusChanged,
       "ciscoScsiLuStatusChanged": ciscoScsiLuStatusChanged,
       "ciscoScsiConformance": ciscoScsiConformance,
       "ciscoScsiCompliances": ciscoScsiCompliances,
       "ciscoScsiCompliance": ciscoScsiCompliance,
       "ciscoScsiGroups": ciscoScsiGroups,
       "ciscoScsiDeviceGroup": ciscoScsiDeviceGroup,
       "ciscoScsiInitiatorGroup": ciscoScsiInitiatorGroup,
       "ciscoScsiDiscoveryGroup": ciscoScsiDiscoveryGroup,
       "ciscoScsiTargetGroup": ciscoScsiTargetGroup,
       "ciscoScsiLunMapGroup": ciscoScsiLunMapGroup,
       "ciscoScsiTargetStatsGroup": ciscoScsiTargetStatsGroup,
       "ciscoScsiTargetHSStatsGroup": ciscoScsiTargetHSStatsGroup,
       "ciscoScsiLunMapStatsGroup": ciscoScsiLunMapStatsGroup,
       "ciscoScsiLunMapHSStatsGroup": ciscoScsiLunMapHSStatsGroup,
       "ciscoScsiInitiatorStatsGroup": ciscoScsiInitiatorStatsGroup,
       "ciscoScsiInitiatorHSStatsGroup": ciscoScsiInitiatorHSStatsGroup,
       "ciscoScsiDiscoveryStatsGroup": ciscoScsiDiscoveryStatsGroup,
       "ciscoScsiDiscoveryHSStatsGroup": ciscoScsiDiscoveryHSStatsGroup,
       "ciscoScsiDeviceStatGroup": ciscoScsiDeviceStatGroup,
       "ciscoScsiNotifGroup": ciscoScsiNotifGroup}
)
