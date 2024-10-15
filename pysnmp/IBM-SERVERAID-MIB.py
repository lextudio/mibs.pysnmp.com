# SNMP MIB module (IBM-SERVERAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-SERVERAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:39 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_IbmServeRaid_ObjectIdentity = ObjectIdentity
ibmServeRaid = _IbmServeRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167)
)
_IbmServeRaidMIB_ObjectIdentity = ObjectIdentity
ibmServeRaidMIB = _IbmServeRaidMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2)
)
_IbmServeRaidNotifications_ObjectIdentity = ObjectIdentity
ibmServeRaidNotifications = _IbmServeRaidNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0)
)
_IbmServeRaidMibObjects_ObjectIdentity = ObjectIdentity
ibmServeRaidMibObjects = _IbmServeRaidMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1)
)
_IbmServeRaidAgentInfo_ObjectIdentity = ObjectIdentity
ibmServeRaidAgentInfo = _IbmServeRaidAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1)
)
_IbmServeRaidAgentKeyIndex_Type = SnmpAdminString
_IbmServeRaidAgentKeyIndex_Object = MibScalar
ibmServeRaidAgentKeyIndex = _IbmServeRaidAgentKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 1),
    _IbmServeRaidAgentKeyIndex_Type()
)
ibmServeRaidAgentKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentKeyIndex.setStatus("mandatory")
_IbmServeRaidAgentId_Type = SnmpAdminString
_IbmServeRaidAgentId_Object = MibScalar
ibmServeRaidAgentId = _IbmServeRaidAgentId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 2),
    _IbmServeRaidAgentId_Type()
)
ibmServeRaidAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentId.setStatus("mandatory")
_IbmServeRaidAgentCompany_Type = SnmpAdminString
_IbmServeRaidAgentCompany_Object = MibScalar
ibmServeRaidAgentCompany = _IbmServeRaidAgentCompany_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 3),
    _IbmServeRaidAgentCompany_Type()
)
ibmServeRaidAgentCompany.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentCompany.setStatus("mandatory")
_IbmServeRaidAgentVersion_Type = SnmpAdminString
_IbmServeRaidAgentVersion_Object = MibScalar
ibmServeRaidAgentVersion = _IbmServeRaidAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 4),
    _IbmServeRaidAgentVersion_Type()
)
ibmServeRaidAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentVersion.setStatus("mandatory")
_IbmServeRaidAgentBuildDate_Type = DateAndTime
_IbmServeRaidAgentBuildDate_Object = MibScalar
ibmServeRaidAgentBuildDate = _IbmServeRaidAgentBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 5),
    _IbmServeRaidAgentBuildDate_Type()
)
ibmServeRaidAgentBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentBuildDate.setStatus("mandatory")
_IbmServeRaidAgentVersionMajor_Type = Integer32
_IbmServeRaidAgentVersionMajor_Object = MibScalar
ibmServeRaidAgentVersionMajor = _IbmServeRaidAgentVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 6),
    _IbmServeRaidAgentVersionMajor_Type()
)
ibmServeRaidAgentVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentVersionMajor.setStatus("mandatory")
_IbmServeRaidAgentVersionMinor_Type = Integer32
_IbmServeRaidAgentVersionMinor_Object = MibScalar
ibmServeRaidAgentVersionMinor = _IbmServeRaidAgentVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 1, 7),
    _IbmServeRaidAgentVersionMinor_Type()
)
ibmServeRaidAgentVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidAgentVersionMinor.setStatus("mandatory")
_IbmServeRaidInfo_ObjectIdentity = ObjectIdentity
ibmServeRaidInfo = _IbmServeRaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2)
)
_IbmServeRaidControllerTable_Object = MibTable
ibmServeRaidControllerTable = _IbmServeRaidControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerTable.setStatus("mandatory")
_IbmServeRaidControllerEntry_Object = MibTableRow
ibmServeRaidControllerEntry = _IbmServeRaidControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1)
)
ibmServeRaidControllerEntry.setIndexNames(
    (0, "IBM-SERVERAID-MIB", "ibmServeRaidKeyIndex"),
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerEntry.setStatus("mandatory")
_IbmServeRaidKeyIndex_Type = SnmpAdminString
_IbmServeRaidKeyIndex_Object = MibTableColumn
ibmServeRaidKeyIndex = _IbmServeRaidKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 1),
    _IbmServeRaidKeyIndex_Type()
)
ibmServeRaidKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidKeyIndex.setStatus("mandatory")


class _IbmServeRaidControllerId_Type(Integer32):
    """Custom type ibmServeRaidControllerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmServeRaidControllerId_Type.__name__ = "Integer32"
_IbmServeRaidControllerId_Object = MibTableColumn
ibmServeRaidControllerId = _IbmServeRaidControllerId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 2),
    _IbmServeRaidControllerId_Type()
)
ibmServeRaidControllerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidControllerId.setStatus("mandatory")
_IbmServeRaidModel_Type = SnmpAdminString
_IbmServeRaidModel_Object = MibTableColumn
ibmServeRaidModel = _IbmServeRaidModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 3),
    _IbmServeRaidModel_Type()
)
ibmServeRaidModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidModel.setStatus("mandatory")
_IbmServeRaidFirmwareVersion_Type = SnmpAdminString
_IbmServeRaidFirmwareVersion_Object = MibTableColumn
ibmServeRaidFirmwareVersion = _IbmServeRaidFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 4),
    _IbmServeRaidFirmwareVersion_Type()
)
ibmServeRaidFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidFirmwareVersion.setStatus("mandatory")
_IbmServeRaidBiosVersion_Type = SnmpAdminString
_IbmServeRaidBiosVersion_Object = MibTableColumn
ibmServeRaidBiosVersion = _IbmServeRaidBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 5),
    _IbmServeRaidBiosVersion_Type()
)
ibmServeRaidBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidBiosVersion.setStatus("mandatory")
_IbmServeRaidDefaultRebuildRate_Type = SnmpAdminString
_IbmServeRaidDefaultRebuildRate_Object = MibTableColumn
ibmServeRaidDefaultRebuildRate = _IbmServeRaidDefaultRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 6),
    _IbmServeRaidDefaultRebuildRate_Type()
)
ibmServeRaidDefaultRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidDefaultRebuildRate.setStatus("mandatory")
_IbmServeRaidNumChannels_Type = Gauge32
_IbmServeRaidNumChannels_Object = MibTableColumn
ibmServeRaidNumChannels = _IbmServeRaidNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 7),
    _IbmServeRaidNumChannels_Type()
)
ibmServeRaidNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidNumChannels.setStatus("mandatory")
_IbmServeRaidMaxChannels_Type = Integer32
_IbmServeRaidMaxChannels_Object = MibTableColumn
ibmServeRaidMaxChannels = _IbmServeRaidMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 8),
    _IbmServeRaidMaxChannels_Type()
)
ibmServeRaidMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidMaxChannels.setStatus("mandatory")
_IbmServeRaidNumLogicalDrives_Type = Gauge32
_IbmServeRaidNumLogicalDrives_Object = MibTableColumn
ibmServeRaidNumLogicalDrives = _IbmServeRaidNumLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 9),
    _IbmServeRaidNumLogicalDrives_Type()
)
ibmServeRaidNumLogicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidNumLogicalDrives.setStatus("mandatory")
_IbmServeRaidMaxLogicalDrives_Type = Integer32
_IbmServeRaidMaxLogicalDrives_Object = MibTableColumn
ibmServeRaidMaxLogicalDrives = _IbmServeRaidMaxLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 10),
    _IbmServeRaidMaxLogicalDrives_Type()
)
ibmServeRaidMaxLogicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidMaxLogicalDrives.setStatus("mandatory")
_IbmServeRaidNumPhysicalDevices_Type = Gauge32
_IbmServeRaidNumPhysicalDevices_Object = MibTableColumn
ibmServeRaidNumPhysicalDevices = _IbmServeRaidNumPhysicalDevices_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 11),
    _IbmServeRaidNumPhysicalDevices_Type()
)
ibmServeRaidNumPhysicalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidNumPhysicalDevices.setStatus("mandatory")
_IbmServeRaidMaxPhysicalDevices_Type = Integer32
_IbmServeRaidMaxPhysicalDevices_Object = MibTableColumn
ibmServeRaidMaxPhysicalDevices = _IbmServeRaidMaxPhysicalDevices_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 12),
    _IbmServeRaidMaxPhysicalDevices_Type()
)
ibmServeRaidMaxPhysicalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidMaxPhysicalDevices.setStatus("mandatory")
_IbmServeRaidStripeSize_Type = Integer32
_IbmServeRaidStripeSize_Object = MibTableColumn
ibmServeRaidStripeSize = _IbmServeRaidStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 13),
    _IbmServeRaidStripeSize_Type()
)
ibmServeRaidStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidStripeSize.setStatus("mandatory")
_IbmServeRaidSlotNumber_Type = Integer32
_IbmServeRaidSlotNumber_Object = MibTableColumn
ibmServeRaidSlotNumber = _IbmServeRaidSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 14),
    _IbmServeRaidSlotNumber_Type()
)
ibmServeRaidSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidSlotNumber.setStatus("mandatory")
_IbmServeRaidVendorName_Type = SnmpAdminString
_IbmServeRaidVendorName_Object = MibTableColumn
ibmServeRaidVendorName = _IbmServeRaidVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 15),
    _IbmServeRaidVendorName_Type()
)
ibmServeRaidVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidVendorName.setStatus("mandatory")


class _IbmServeRaidGeneralStatus_Type(Integer32):
    """Custom type ibmServeRaidGeneralStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_IbmServeRaidGeneralStatus_Type.__name__ = "Integer32"
_IbmServeRaidGeneralStatus_Object = MibTableColumn
ibmServeRaidGeneralStatus = _IbmServeRaidGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 1, 1, 16),
    _IbmServeRaidGeneralStatus_Type()
)
ibmServeRaidGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidGeneralStatus.setStatus("mandatory")
_IbmServeRaidPhysDeviceTable_Object = MibTable
ibmServeRaidPhysDeviceTable = _IbmServeRaidPhysDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceTable.setStatus("mandatory")
_IbmServeRaidPhysDeviceEntry_Object = MibTableRow
ibmServeRaidPhysDeviceEntry = _IbmServeRaidPhysDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1)
)
ibmServeRaidPhysDeviceEntry.setIndexNames(
    (0, "IBM-SERVERAID-MIB", "ibmServeRaidPhysDeviceKeyIndex"),
)
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceEntry.setStatus("mandatory")
_IbmServeRaidPhysDeviceKeyIndex_Type = SnmpAdminString
_IbmServeRaidPhysDeviceKeyIndex_Object = MibTableColumn
ibmServeRaidPhysDeviceKeyIndex = _IbmServeRaidPhysDeviceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 1),
    _IbmServeRaidPhysDeviceKeyIndex_Type()
)
ibmServeRaidPhysDeviceKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceKeyIndex.setStatus("mandatory")


class _IbmServeRaidPhysDeviceChannelNr_Type(Integer32):
    """Custom type ibmServeRaidPhysDeviceChannelNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmServeRaidPhysDeviceChannelNr_Type.__name__ = "Integer32"
_IbmServeRaidPhysDeviceChannelNr_Object = MibTableColumn
ibmServeRaidPhysDeviceChannelNr = _IbmServeRaidPhysDeviceChannelNr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 2),
    _IbmServeRaidPhysDeviceChannelNr_Type()
)
ibmServeRaidPhysDeviceChannelNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceChannelNr.setStatus("mandatory")


class _IbmServeRaidPhysDeviceDevNr_Type(Integer32):
    """Custom type ibmServeRaidPhysDeviceDevNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmServeRaidPhysDeviceDevNr_Type.__name__ = "Integer32"
_IbmServeRaidPhysDeviceDevNr_Object = MibTableColumn
ibmServeRaidPhysDeviceDevNr = _IbmServeRaidPhysDeviceDevNr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 3),
    _IbmServeRaidPhysDeviceDevNr_Type()
)
ibmServeRaidPhysDeviceDevNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceDevNr.setStatus("mandatory")
_IbmServeRaidPhysDeviceModel_Type = SnmpAdminString
_IbmServeRaidPhysDeviceModel_Object = MibTableColumn
ibmServeRaidPhysDeviceModel = _IbmServeRaidPhysDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 4),
    _IbmServeRaidPhysDeviceModel_Type()
)
ibmServeRaidPhysDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceModel.setStatus("mandatory")
_IbmServeRaidPhysDeviceCapacity_Type = Integer32
_IbmServeRaidPhysDeviceCapacity_Object = MibTableColumn
ibmServeRaidPhysDeviceCapacity = _IbmServeRaidPhysDeviceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 5),
    _IbmServeRaidPhysDeviceCapacity_Type()
)
ibmServeRaidPhysDeviceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceCapacity.setStatus("mandatory")


class _IbmServeRaidPhysDeviceStatus_Type(Integer32):
    """Custom type ibmServeRaidPhysDeviceStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dead", 1),
          ("empty", 7),
          ("online", 2),
          ("ready", 6),
          ("rebuild", 4),
          ("spare", 5),
          ("standby", 3),
          ("unknown", 9))
    )


_IbmServeRaidPhysDeviceStatus_Type.__name__ = "Integer32"
_IbmServeRaidPhysDeviceStatus_Object = MibTableColumn
ibmServeRaidPhysDeviceStatus = _IbmServeRaidPhysDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 6),
    _IbmServeRaidPhysDeviceStatus_Type()
)
ibmServeRaidPhysDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceStatus.setStatus("mandatory")
_IbmServeRaidPhysDeviceDiskConfigured_Type = TruthValue
_IbmServeRaidPhysDeviceDiskConfigured_Object = MibTableColumn
ibmServeRaidPhysDeviceDiskConfigured = _IbmServeRaidPhysDeviceDiskConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 7),
    _IbmServeRaidPhysDeviceDiskConfigured_Type()
)
ibmServeRaidPhysDeviceDiskConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceDiskConfigured.setStatus("mandatory")


class _IbmServeRaidPhysDeviceScsiType_Type(Integer32):
    """Custom type ibmServeRaidPhysDeviceScsiType based on Integer32"""
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
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cdRom", 6),
          ("commDev", 10),
          ("disk", 1),
          ("enclosure", 97),
          ("host", 98),
          ("jukebox", 9),
          ("optical", 8),
          ("printer", 3),
          ("processor", 4),
          ("scanner", 7),
          ("tape", 2),
          ("unknown", 99),
          ("writeOnce", 5))
    )


_IbmServeRaidPhysDeviceScsiType_Type.__name__ = "Integer32"
_IbmServeRaidPhysDeviceScsiType_Object = MibTableColumn
ibmServeRaidPhysDeviceScsiType = _IbmServeRaidPhysDeviceScsiType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 8),
    _IbmServeRaidPhysDeviceScsiType_Type()
)
ibmServeRaidPhysDeviceScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDeviceScsiType.setStatus("mandatory")


class _IbmServeRaidPhysDevicePfaStatus_Type(Integer32):
    """Custom type ibmServeRaidPhysDevicePfaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failurePredicted", 2),
          ("ok", 1))
    )


_IbmServeRaidPhysDevicePfaStatus_Type.__name__ = "Integer32"
_IbmServeRaidPhysDevicePfaStatus_Object = MibTableColumn
ibmServeRaidPhysDevicePfaStatus = _IbmServeRaidPhysDevicePfaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 2, 1, 9),
    _IbmServeRaidPhysDevicePfaStatus_Type()
)
ibmServeRaidPhysDevicePfaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidPhysDevicePfaStatus.setStatus("mandatory")
_IbmServeRaidLogicalTable_Object = MibTable
ibmServeRaidLogicalTable = _IbmServeRaidLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalTable.setStatus("mandatory")
_IbmServeRaidLogicalEntry_Object = MibTableRow
ibmServeRaidLogicalEntry = _IbmServeRaidLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1)
)
ibmServeRaidLogicalEntry.setIndexNames(
    (0, "IBM-SERVERAID-MIB", "ibmServeRaidLogicalKeyIndex"),
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalEntry.setStatus("mandatory")
_IbmServeRaidLogicalKeyIndex_Type = SnmpAdminString
_IbmServeRaidLogicalKeyIndex_Object = MibTableColumn
ibmServeRaidLogicalKeyIndex = _IbmServeRaidLogicalKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 1),
    _IbmServeRaidLogicalKeyIndex_Type()
)
ibmServeRaidLogicalKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalKeyIndex.setStatus("mandatory")


class _IbmServeRaidLogicalDriveNum_Type(Integer32):
    """Custom type ibmServeRaidLogicalDriveNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmServeRaidLogicalDriveNum_Type.__name__ = "Integer32"
_IbmServeRaidLogicalDriveNum_Object = MibTableColumn
ibmServeRaidLogicalDriveNum = _IbmServeRaidLogicalDriveNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 2),
    _IbmServeRaidLogicalDriveNum_Type()
)
ibmServeRaidLogicalDriveNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalDriveNum.setStatus("mandatory")


class _IbmServeRaidLogicalStatus_Type(Integer32):
    """Custom type ibmServeRaidLogicalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("free", 5),
          ("migrating", 4),
          ("offline", 3),
          ("online", 1),
          ("unknown", 9))
    )


_IbmServeRaidLogicalStatus_Type.__name__ = "Integer32"
_IbmServeRaidLogicalStatus_Object = MibTableColumn
ibmServeRaidLogicalStatus = _IbmServeRaidLogicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 3),
    _IbmServeRaidLogicalStatus_Type()
)
ibmServeRaidLogicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalStatus.setStatus("mandatory")
_IbmServeRaidLogicalSize_Type = Integer32
_IbmServeRaidLogicalSize_Object = MibTableColumn
ibmServeRaidLogicalSize = _IbmServeRaidLogicalSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 4),
    _IbmServeRaidLogicalSize_Type()
)
ibmServeRaidLogicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalSize.setStatus("mandatory")
_IbmServeRaidLogicalRaidLevel_Type = SnmpAdminString
_IbmServeRaidLogicalRaidLevel_Object = MibTableColumn
ibmServeRaidLogicalRaidLevel = _IbmServeRaidLogicalRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 5),
    _IbmServeRaidLogicalRaidLevel_Type()
)
ibmServeRaidLogicalRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalRaidLevel.setStatus("mandatory")


class _IbmServeRaidLogicalWriteCacheMode_Type(Integer32):
    """Custom type ibmServeRaidLogicalWriteCacheMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeBack", 1),
          ("writeThrough", 2))
    )


_IbmServeRaidLogicalWriteCacheMode_Type.__name__ = "Integer32"
_IbmServeRaidLogicalWriteCacheMode_Object = MibTableColumn
ibmServeRaidLogicalWriteCacheMode = _IbmServeRaidLogicalWriteCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 2, 3, 1, 6),
    _IbmServeRaidLogicalWriteCacheMode_Type()
)
ibmServeRaidLogicalWriteCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmServeRaidLogicalWriteCacheMode.setStatus("mandatory")
_IbmServeRaidTrapInfo_ObjectIdentity = ObjectIdentity
ibmServeRaidTrapInfo = _IbmServeRaidTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3)
)
_IbmServeRaidTrapController_Type = Integer32
_IbmServeRaidTrapController_Object = MibScalar
ibmServeRaidTrapController = _IbmServeRaidTrapController_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 1),
    _IbmServeRaidTrapController_Type()
)
ibmServeRaidTrapController.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapController.setStatus("mandatory")
_IbmServeRaidTrapLogicalDrive_Type = Integer32
_IbmServeRaidTrapLogicalDrive_Object = MibScalar
ibmServeRaidTrapLogicalDrive = _IbmServeRaidTrapLogicalDrive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 2),
    _IbmServeRaidTrapLogicalDrive_Type()
)
ibmServeRaidTrapLogicalDrive.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapLogicalDrive.setStatus("mandatory")
_IbmServeRaidTrapChannel_Type = Integer32
_IbmServeRaidTrapChannel_Object = MibScalar
ibmServeRaidTrapChannel = _IbmServeRaidTrapChannel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 3),
    _IbmServeRaidTrapChannel_Type()
)
ibmServeRaidTrapChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapChannel.setStatus("mandatory")
_IbmServeRaidTrapScsiId_Type = Integer32
_IbmServeRaidTrapScsiId_Object = MibScalar
ibmServeRaidTrapScsiId = _IbmServeRaidTrapScsiId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 4),
    _IbmServeRaidTrapScsiId_Type()
)
ibmServeRaidTrapScsiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapScsiId.setStatus("mandatory")
_IbmServeRaidTrapFan_Type = Integer32
_IbmServeRaidTrapFan_Object = MibScalar
ibmServeRaidTrapFan = _IbmServeRaidTrapFan_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 5),
    _IbmServeRaidTrapFan_Type()
)
ibmServeRaidTrapFan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapFan.setStatus("mandatory")
_IbmServeRaidTrapPowerSupply_Type = Integer32
_IbmServeRaidTrapPowerSupply_Object = MibScalar
ibmServeRaidTrapPowerSupply = _IbmServeRaidTrapPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 6),
    _IbmServeRaidTrapPowerSupply_Type()
)
ibmServeRaidTrapPowerSupply.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapPowerSupply.setStatus("mandatory")
_IbmServeRaidTrapErrorCode_Type = Integer32
_IbmServeRaidTrapErrorCode_Object = MibScalar
ibmServeRaidTrapErrorCode = _IbmServeRaidTrapErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 7),
    _IbmServeRaidTrapErrorCode_Type()
)
ibmServeRaidTrapErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapErrorCode.setStatus("mandatory")
_IbmServeRaidTrapServerName_Type = SnmpAdminString
_IbmServeRaidTrapServerName_Object = MibScalar
ibmServeRaidTrapServerName = _IbmServeRaidTrapServerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 8),
    _IbmServeRaidTrapServerName_Type()
)
ibmServeRaidTrapServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapServerName.setStatus("mandatory")
_IbmServeRaidTrapArray_Type = SnmpAdminString
_IbmServeRaidTrapArray_Object = MibScalar
ibmServeRaidTrapArray = _IbmServeRaidTrapArray_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 9),
    _IbmServeRaidTrapArray_Type()
)
ibmServeRaidTrapArray.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapArray.setStatus("mandatory")
_IbmServeRaidTrapFru_Type = SnmpAdminString
_IbmServeRaidTrapFru_Object = MibScalar
ibmServeRaidTrapFru = _IbmServeRaidTrapFru_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 1, 3, 10),
    _IbmServeRaidTrapFru_Type()
)
ibmServeRaidTrapFru.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmServeRaidTrapFru.setStatus("mandatory")
_IbmServeRaidConformance_ObjectIdentity = ObjectIdentity
ibmServeRaidConformance = _IbmServeRaidConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2)
)
_IbmServeRaidCompliances_ObjectIdentity = ObjectIdentity
ibmServeRaidCompliances = _IbmServeRaidCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 1)
)
_IbmServeRaidCompliance_ObjectIdentity = ObjectIdentity
ibmServeRaidCompliance = _IbmServeRaidCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 1, 1)
)
_IbmServeRaidGroups_ObjectIdentity = ObjectIdentity
ibmServeRaidGroups = _IbmServeRaidGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2)
)
_IbmServeRaidAgentGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidAgentGroup = _IbmServeRaidAgentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 1)
)
_IbmServeRaidControllerGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidControllerGroup = _IbmServeRaidControllerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 2)
)
_IbmServeRaidPhysicalGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidPhysicalGroup = _IbmServeRaidPhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 3)
)
_IbmServeRaidLogicalGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidLogicalGroup = _IbmServeRaidLogicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 4)
)
_IbmServeRaidTrapInfoGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidTrapInfoGroup = _IbmServeRaidTrapInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 5)
)
_IbmServeRaidNotificationsGroup_ObjectIdentity = ObjectIdentity
ibmServeRaidNotificationsGroup = _IbmServeRaidNotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 2, 2, 6)
)

# Managed Objects groups


# Notification objects

ibmServeRaidNoControllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 201)
)
ibmServeRaidNoControllers.setObjects(
    ("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName")
)
if mibBuilder.loadTexts:
    ibmServeRaidNoControllers.setStatus(
        ""
    )

ibmServeRaidControllerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 202)
)
ibmServeRaidControllerFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerFail.setStatus(
        ""
    )

ibmServeRaidDeadBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 203)
)
ibmServeRaidDeadBattery.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDeadBattery.setStatus(
        ""
    )

ibmServeRaidDeadBatteryCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 204)
)
ibmServeRaidDeadBatteryCache.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDeadBatteryCache.setStatus(
        ""
    )

ibmServeRaidPollingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 205)
)
ibmServeRaidPollingFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPollingFail.setStatus(
        ""
    )

ibmServeRaidConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 206)
)
ibmServeRaidConfigFail.setObjects(
    ("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName")
)
if mibBuilder.loadTexts:
    ibmServeRaidConfigFail.setStatus(
        ""
    )

ibmServeRaidControllerAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 207)
)
ibmServeRaidControllerAdded.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerAdded.setStatus(
        ""
    )

ibmServeRaidControllerReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 208)
)
ibmServeRaidControllerReplaced.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerReplaced.setStatus(
        ""
    )

ibmServeRaidControllerFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 209)
)
ibmServeRaidControllerFailover.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidControllerFailover.setStatus(
        ""
    )

ibmServeRaidLogicalDriveCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 301)
)
ibmServeRaidLogicalDriveCritical.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalDriveCritical.setStatus(
        ""
    )

ibmServeRaidLogicalDriveBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 302)
)
ibmServeRaidLogicalDriveBlocked.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalDriveBlocked.setStatus(
        ""
    )

ibmServeRaidLogicalDriveOffLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 303)
)
ibmServeRaidLogicalDriveOffLine.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalDriveOffLine.setStatus(
        ""
    )

ibmServeRaidRebuildDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 304)
)
ibmServeRaidRebuildDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidRebuildDetected.setStatus(
        ""
    )

ibmServeRaidRebuildComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 305)
)
ibmServeRaidRebuildComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidRebuildComplete.setStatus(
        ""
    )

ibmServeRaidRebuildFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 306)
)
ibmServeRaidRebuildFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidRebuildFail.setStatus(
        ""
    )

ibmServeRaidSyncDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 307)
)
ibmServeRaidSyncDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidSyncDetected.setStatus(
        ""
    )

ibmServeRaidSyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 308)
)
ibmServeRaidSyncComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidSyncComplete.setStatus(
        ""
    )

ibmServeRaidSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 309)
)
ibmServeRaidSyncFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidSyncFail.setStatus(
        ""
    )

ibmServeRaidMigrationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 310)
)
ibmServeRaidMigrationDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidMigrationDetected.setStatus(
        ""
    )

ibmServeRaidMigrationComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 311)
)
ibmServeRaidMigrationComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidMigrationComplete.setStatus(
        ""
    )

ibmServeRaidMigrationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 312)
)
ibmServeRaidMigrationFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidMigrationFail.setStatus(
        ""
    )

ibmServeRaidCompressionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 313)
)
ibmServeRaidCompressionDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidCompressionDetected.setStatus(
        ""
    )

ibmServeRaidCompressionComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 314)
)
ibmServeRaidCompressionComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidCompressionComplete.setStatus(
        ""
    )

ibmServeRaidcompressionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 315)
)
ibmServeRaidcompressionFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidcompressionFail.setStatus(
        ""
    )

ibmServeRaidDecompressionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 316)
)
ibmServeRaidDecompressionDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDecompressionDetected.setStatus(
        ""
    )

ibmServeRaidDecompressionComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 317)
)
ibmServeRaidDecompressionComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDecompressionComplete.setStatus(
        ""
    )

ibmServeRaidDecompressionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 318)
)
ibmServeRaidDecompressionFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDecompressionFail.setStatus(
        ""
    )

ibmServeRaidFlashCopyDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 319)
)
ibmServeRaidFlashCopyDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFlashCopyDetected.setStatus(
        ""
    )

ibmServeRaidFlashCopyComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 320)
)
ibmServeRaidFlashCopyComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFlashCopyComplete.setStatus(
        ""
    )

ibmServeRaidFlashCopyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 321)
)
ibmServeRaidFlashCopyFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFlashCopyFail.setStatus(
        ""
    )

ibmServeRaidArrayRebuildDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 322)
)
ibmServeRaidArrayRebuildDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayRebuildDetected.setStatus(
        ""
    )

ibmServeRaidArrayRebuildComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 323)
)
ibmServeRaidArrayRebuildComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayRebuildComplete.setStatus(
        ""
    )

ibmServeRaidArrayRebuildFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 324)
)
ibmServeRaidArrayRebuildFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayRebuildFail.setStatus(
        ""
    )

ibmServeRaidArraySyncDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 325)
)
ibmServeRaidArraySyncDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArraySyncDetected.setStatus(
        ""
    )

ibmServeRaidArraySyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 326)
)
ibmServeRaidArraySyncComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArraySyncComplete.setStatus(
        ""
    )

ibmServeRaidArraySyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 327)
)
ibmServeRaidArraySyncFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArraySyncFail.setStatus(
        ""
    )

ibmServeRaidArrayFlashCopyDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 328)
)
ibmServeRaidArrayFlashCopyDetected.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayFlashCopyDetected.setStatus(
        ""
    )

ibmServeRaidArrayFlashCopyComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 329)
)
ibmServeRaidArrayFlashCopyComplete.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayFlashCopyComplete.setStatus(
        ""
    )

ibmServeRaidArrayFlashCopyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 330)
)
ibmServeRaidArrayFlashCopyFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapArray"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapErrorCode"))
)
if mibBuilder.loadTexts:
    ibmServeRaidArrayFlashCopyFail.setStatus(
        ""
    )

ibmServeRaidLogicalDriveUnblocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 331)
)
ibmServeRaidLogicalDriveUnblocked.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapLogicalDrive"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"))
)
if mibBuilder.loadTexts:
    ibmServeRaidLogicalDriveUnblocked.setStatus(
        ""
    )

ibmServeRaidDefunctDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 401)
)
ibmServeRaidDefunctDrive.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDefunctDrive.setStatus(
        ""
    )

ibmServeRaidPfaDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 402)
)
ibmServeRaidPfaDrive.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPfaDrive.setStatus(
        ""
    )

ibmServeRaidDefunctReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 403)
)
ibmServeRaidDefunctReplaced.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDefunctReplaced.setStatus(
        ""
    )

ibmServeRaidDefunctDriveFru = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 404)
)
ibmServeRaidDefunctDriveFru.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFru"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidDefunctDriveFru.setStatus(
        ""
    )

ibmServeRaidPfaDriveFru = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 405)
)
ibmServeRaidPfaDriveFru.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFru"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPfaDriveFru.setStatus(
        ""
    )

ibmServeRaidUnsupportedDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 406)
)
ibmServeRaidUnsupportedDrive.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapScsiId"))
)
if mibBuilder.loadTexts:
    ibmServeRaidUnsupportedDrive.setStatus(
        ""
    )

ibmServeRaidEnclosureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 501)
)
ibmServeRaidEnclosureOK.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidEnclosureOK.setStatus(
        ""
    )

ibmServeRaidEnclosureFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 502)
)
ibmServeRaidEnclosureFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidEnclosureFail.setStatus(
        ""
    )

ibmServeRaidFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 503)
)
ibmServeRaidFanOk.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFan"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFanOk.setStatus(
        ""
    )

ibmServeRaidFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 504)
)
ibmServeRaidFanFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFan"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFanFail.setStatus(
        ""
    )

ibmServeRaidFanInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 505)
)
ibmServeRaidFanInstalled.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFan"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFanInstalled.setStatus(
        ""
    )

ibmServeRaidFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 506)
)
ibmServeRaidFanRemoved.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapFan"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidFanRemoved.setStatus(
        ""
    )

ibmServeRaidTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 507)
)
ibmServeRaidTempOk.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidTempOk.setStatus(
        ""
    )

ibmServeRaidTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 508)
)
ibmServeRaidTempFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidTempFail.setStatus(
        ""
    )

ibmServeRaidPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 509)
)
ibmServeRaidPowerSupplyOk.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapPowerSupply"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPowerSupplyOk.setStatus(
        ""
    )

ibmServeRaidPowerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 510)
)
ibmServeRaidPowerSupplyFail.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapPowerSupply"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPowerSupplyFail.setStatus(
        ""
    )

ibmServeRaidPowerSupplyInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 511)
)
ibmServeRaidPowerSupplyInstalled.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapPowerSupply"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPowerSupplyInstalled.setStatus(
        ""
    )

ibmServeRaidPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 512)
)
ibmServeRaidPowerSupplyRemoved.setObjects(
      *(("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapPowerSupply"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapController"),
        ("IBM-SERVERAID-MIB", "ibmServeRaidTrapChannel"))
)
if mibBuilder.loadTexts:
    ibmServeRaidPowerSupplyRemoved.setStatus(
        ""
    )

ibmServeRaidTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 167, 2, 0, 601)
)
ibmServeRaidTestTrap.setObjects(
    ("IBM-SERVERAID-MIB", "ibmServeRaidTrapServerName")
)
if mibBuilder.loadTexts:
    ibmServeRaidTestTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-SERVERAID-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibmServeRaid": ibmServeRaid,
       "ibmServeRaidMIB": ibmServeRaidMIB,
       "ibmServeRaidNotifications": ibmServeRaidNotifications,
       "ibmServeRaidNoControllers": ibmServeRaidNoControllers,
       "ibmServeRaidControllerFail": ibmServeRaidControllerFail,
       "ibmServeRaidDeadBattery": ibmServeRaidDeadBattery,
       "ibmServeRaidDeadBatteryCache": ibmServeRaidDeadBatteryCache,
       "ibmServeRaidPollingFail": ibmServeRaidPollingFail,
       "ibmServeRaidConfigFail": ibmServeRaidConfigFail,
       "ibmServeRaidControllerAdded": ibmServeRaidControllerAdded,
       "ibmServeRaidControllerReplaced": ibmServeRaidControllerReplaced,
       "ibmServeRaidControllerFailover": ibmServeRaidControllerFailover,
       "ibmServeRaidLogicalDriveCritical": ibmServeRaidLogicalDriveCritical,
       "ibmServeRaidLogicalDriveBlocked": ibmServeRaidLogicalDriveBlocked,
       "ibmServeRaidLogicalDriveOffLine": ibmServeRaidLogicalDriveOffLine,
       "ibmServeRaidRebuildDetected": ibmServeRaidRebuildDetected,
       "ibmServeRaidRebuildComplete": ibmServeRaidRebuildComplete,
       "ibmServeRaidRebuildFail": ibmServeRaidRebuildFail,
       "ibmServeRaidSyncDetected": ibmServeRaidSyncDetected,
       "ibmServeRaidSyncComplete": ibmServeRaidSyncComplete,
       "ibmServeRaidSyncFail": ibmServeRaidSyncFail,
       "ibmServeRaidMigrationDetected": ibmServeRaidMigrationDetected,
       "ibmServeRaidMigrationComplete": ibmServeRaidMigrationComplete,
       "ibmServeRaidMigrationFail": ibmServeRaidMigrationFail,
       "ibmServeRaidCompressionDetected": ibmServeRaidCompressionDetected,
       "ibmServeRaidCompressionComplete": ibmServeRaidCompressionComplete,
       "ibmServeRaidcompressionFail": ibmServeRaidcompressionFail,
       "ibmServeRaidDecompressionDetected": ibmServeRaidDecompressionDetected,
       "ibmServeRaidDecompressionComplete": ibmServeRaidDecompressionComplete,
       "ibmServeRaidDecompressionFail": ibmServeRaidDecompressionFail,
       "ibmServeRaidFlashCopyDetected": ibmServeRaidFlashCopyDetected,
       "ibmServeRaidFlashCopyComplete": ibmServeRaidFlashCopyComplete,
       "ibmServeRaidFlashCopyFail": ibmServeRaidFlashCopyFail,
       "ibmServeRaidArrayRebuildDetected": ibmServeRaidArrayRebuildDetected,
       "ibmServeRaidArrayRebuildComplete": ibmServeRaidArrayRebuildComplete,
       "ibmServeRaidArrayRebuildFail": ibmServeRaidArrayRebuildFail,
       "ibmServeRaidArraySyncDetected": ibmServeRaidArraySyncDetected,
       "ibmServeRaidArraySyncComplete": ibmServeRaidArraySyncComplete,
       "ibmServeRaidArraySyncFail": ibmServeRaidArraySyncFail,
       "ibmServeRaidArrayFlashCopyDetected": ibmServeRaidArrayFlashCopyDetected,
       "ibmServeRaidArrayFlashCopyComplete": ibmServeRaidArrayFlashCopyComplete,
       "ibmServeRaidArrayFlashCopyFail": ibmServeRaidArrayFlashCopyFail,
       "ibmServeRaidLogicalDriveUnblocked": ibmServeRaidLogicalDriveUnblocked,
       "ibmServeRaidDefunctDrive": ibmServeRaidDefunctDrive,
       "ibmServeRaidPfaDrive": ibmServeRaidPfaDrive,
       "ibmServeRaidDefunctReplaced": ibmServeRaidDefunctReplaced,
       "ibmServeRaidDefunctDriveFru": ibmServeRaidDefunctDriveFru,
       "ibmServeRaidPfaDriveFru": ibmServeRaidPfaDriveFru,
       "ibmServeRaidUnsupportedDrive": ibmServeRaidUnsupportedDrive,
       "ibmServeRaidEnclosureOK": ibmServeRaidEnclosureOK,
       "ibmServeRaidEnclosureFail": ibmServeRaidEnclosureFail,
       "ibmServeRaidFanOk": ibmServeRaidFanOk,
       "ibmServeRaidFanFail": ibmServeRaidFanFail,
       "ibmServeRaidFanInstalled": ibmServeRaidFanInstalled,
       "ibmServeRaidFanRemoved": ibmServeRaidFanRemoved,
       "ibmServeRaidTempOk": ibmServeRaidTempOk,
       "ibmServeRaidTempFail": ibmServeRaidTempFail,
       "ibmServeRaidPowerSupplyOk": ibmServeRaidPowerSupplyOk,
       "ibmServeRaidPowerSupplyFail": ibmServeRaidPowerSupplyFail,
       "ibmServeRaidPowerSupplyInstalled": ibmServeRaidPowerSupplyInstalled,
       "ibmServeRaidPowerSupplyRemoved": ibmServeRaidPowerSupplyRemoved,
       "ibmServeRaidTestTrap": ibmServeRaidTestTrap,
       "ibmServeRaidMibObjects": ibmServeRaidMibObjects,
       "ibmServeRaidAgentInfo": ibmServeRaidAgentInfo,
       "ibmServeRaidAgentKeyIndex": ibmServeRaidAgentKeyIndex,
       "ibmServeRaidAgentId": ibmServeRaidAgentId,
       "ibmServeRaidAgentCompany": ibmServeRaidAgentCompany,
       "ibmServeRaidAgentVersion": ibmServeRaidAgentVersion,
       "ibmServeRaidAgentBuildDate": ibmServeRaidAgentBuildDate,
       "ibmServeRaidAgentVersionMajor": ibmServeRaidAgentVersionMajor,
       "ibmServeRaidAgentVersionMinor": ibmServeRaidAgentVersionMinor,
       "ibmServeRaidInfo": ibmServeRaidInfo,
       "ibmServeRaidControllerTable": ibmServeRaidControllerTable,
       "ibmServeRaidControllerEntry": ibmServeRaidControllerEntry,
       "ibmServeRaidKeyIndex": ibmServeRaidKeyIndex,
       "ibmServeRaidControllerId": ibmServeRaidControllerId,
       "ibmServeRaidModel": ibmServeRaidModel,
       "ibmServeRaidFirmwareVersion": ibmServeRaidFirmwareVersion,
       "ibmServeRaidBiosVersion": ibmServeRaidBiosVersion,
       "ibmServeRaidDefaultRebuildRate": ibmServeRaidDefaultRebuildRate,
       "ibmServeRaidNumChannels": ibmServeRaidNumChannels,
       "ibmServeRaidMaxChannels": ibmServeRaidMaxChannels,
       "ibmServeRaidNumLogicalDrives": ibmServeRaidNumLogicalDrives,
       "ibmServeRaidMaxLogicalDrives": ibmServeRaidMaxLogicalDrives,
       "ibmServeRaidNumPhysicalDevices": ibmServeRaidNumPhysicalDevices,
       "ibmServeRaidMaxPhysicalDevices": ibmServeRaidMaxPhysicalDevices,
       "ibmServeRaidStripeSize": ibmServeRaidStripeSize,
       "ibmServeRaidSlotNumber": ibmServeRaidSlotNumber,
       "ibmServeRaidVendorName": ibmServeRaidVendorName,
       "ibmServeRaidGeneralStatus": ibmServeRaidGeneralStatus,
       "ibmServeRaidPhysDeviceTable": ibmServeRaidPhysDeviceTable,
       "ibmServeRaidPhysDeviceEntry": ibmServeRaidPhysDeviceEntry,
       "ibmServeRaidPhysDeviceKeyIndex": ibmServeRaidPhysDeviceKeyIndex,
       "ibmServeRaidPhysDeviceChannelNr": ibmServeRaidPhysDeviceChannelNr,
       "ibmServeRaidPhysDeviceDevNr": ibmServeRaidPhysDeviceDevNr,
       "ibmServeRaidPhysDeviceModel": ibmServeRaidPhysDeviceModel,
       "ibmServeRaidPhysDeviceCapacity": ibmServeRaidPhysDeviceCapacity,
       "ibmServeRaidPhysDeviceStatus": ibmServeRaidPhysDeviceStatus,
       "ibmServeRaidPhysDeviceDiskConfigured": ibmServeRaidPhysDeviceDiskConfigured,
       "ibmServeRaidPhysDeviceScsiType": ibmServeRaidPhysDeviceScsiType,
       "ibmServeRaidPhysDevicePfaStatus": ibmServeRaidPhysDevicePfaStatus,
       "ibmServeRaidLogicalTable": ibmServeRaidLogicalTable,
       "ibmServeRaidLogicalEntry": ibmServeRaidLogicalEntry,
       "ibmServeRaidLogicalKeyIndex": ibmServeRaidLogicalKeyIndex,
       "ibmServeRaidLogicalDriveNum": ibmServeRaidLogicalDriveNum,
       "ibmServeRaidLogicalStatus": ibmServeRaidLogicalStatus,
       "ibmServeRaidLogicalSize": ibmServeRaidLogicalSize,
       "ibmServeRaidLogicalRaidLevel": ibmServeRaidLogicalRaidLevel,
       "ibmServeRaidLogicalWriteCacheMode": ibmServeRaidLogicalWriteCacheMode,
       "ibmServeRaidTrapInfo": ibmServeRaidTrapInfo,
       "ibmServeRaidTrapController": ibmServeRaidTrapController,
       "ibmServeRaidTrapLogicalDrive": ibmServeRaidTrapLogicalDrive,
       "ibmServeRaidTrapChannel": ibmServeRaidTrapChannel,
       "ibmServeRaidTrapScsiId": ibmServeRaidTrapScsiId,
       "ibmServeRaidTrapFan": ibmServeRaidTrapFan,
       "ibmServeRaidTrapPowerSupply": ibmServeRaidTrapPowerSupply,
       "ibmServeRaidTrapErrorCode": ibmServeRaidTrapErrorCode,
       "ibmServeRaidTrapServerName": ibmServeRaidTrapServerName,
       "ibmServeRaidTrapArray": ibmServeRaidTrapArray,
       "ibmServeRaidTrapFru": ibmServeRaidTrapFru,
       "ibmServeRaidConformance": ibmServeRaidConformance,
       "ibmServeRaidCompliances": ibmServeRaidCompliances,
       "ibmServeRaidCompliance": ibmServeRaidCompliance,
       "ibmServeRaidGroups": ibmServeRaidGroups,
       "ibmServeRaidAgentGroup": ibmServeRaidAgentGroup,
       "ibmServeRaidControllerGroup": ibmServeRaidControllerGroup,
       "ibmServeRaidPhysicalGroup": ibmServeRaidPhysicalGroup,
       "ibmServeRaidLogicalGroup": ibmServeRaidLogicalGroup,
       "ibmServeRaidTrapInfoGroup": ibmServeRaidTrapInfoGroup,
       "ibmServeRaidNotificationsGroup": ibmServeRaidNotificationsGroup}
)
