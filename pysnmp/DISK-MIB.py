# SNMP MIB module (DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:14 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

deviceDiskMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DiskStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("bad", 8),
          ("empty", 7),
          ("initializing", 2),
          ("inserted", 3),
          ("not-present", 6),
          ("offline", 4),
          ("present", 1),
          ("removed", 5),
          ("unknown", 9))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceDiskMIBObjects_ObjectIdentity = ObjectIdentity
deviceDiskMIBObjects = _DeviceDiskMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1)
)
_DeviceDiskValues_ObjectIdentity = ObjectIdentity
deviceDiskValues = _DeviceDiskValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1)
)
_DeviceDiskValueTable_Object = MibTable
deviceDiskValueTable = _DeviceDiskValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceDiskValueTable.setStatus("current")
_DeviceDiskValueEntry_Object = MibTableRow
deviceDiskValueEntry = _DeviceDiskValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1)
)
deviceDiskValueEntry.setIndexNames(
    (0, "DISK-MIB", "deviceDiskIndex"),
)
if mibBuilder.loadTexts:
    deviceDiskValueEntry.setStatus("current")


class _DeviceDiskIndex_Type(Integer32):
    """Custom type deviceDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceDiskIndex_Type.__name__ = "Integer32"
_DeviceDiskIndex_Object = MibTableColumn
deviceDiskIndex = _DeviceDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 1),
    _DeviceDiskIndex_Type()
)
deviceDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceDiskIndex.setStatus("current")
_DeviceDiskTrapEnabled_Type = TruthValue
_DeviceDiskTrapEnabled_Object = MibTableColumn
deviceDiskTrapEnabled = _DeviceDiskTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 2),
    _DeviceDiskTrapEnabled_Type()
)
deviceDiskTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceDiskTrapEnabled.setStatus("current")
_DeviceDiskStatus_Type = DiskStatus
_DeviceDiskStatus_Object = MibTableColumn
deviceDiskStatus = _DeviceDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 3),
    _DeviceDiskStatus_Type()
)
deviceDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskStatus.setStatus("current")
_DeviceDiskTimeStamp_Type = TimeStamp
_DeviceDiskTimeStamp_Object = MibTableColumn
deviceDiskTimeStamp = _DeviceDiskTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 4),
    _DeviceDiskTimeStamp_Type()
)
deviceDiskTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskTimeStamp.setStatus("current")
_DeviceDiskVendor_Type = DisplayString
_DeviceDiskVendor_Object = MibTableColumn
deviceDiskVendor = _DeviceDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 5),
    _DeviceDiskVendor_Type()
)
deviceDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskVendor.setStatus("current")
_DeviceDiskProduct_Type = DisplayString
_DeviceDiskProduct_Object = MibTableColumn
deviceDiskProduct = _DeviceDiskProduct_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 6),
    _DeviceDiskProduct_Type()
)
deviceDiskProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskProduct.setStatus("current")
_DeviceDiskRevision_Type = DisplayString
_DeviceDiskRevision_Object = MibTableColumn
deviceDiskRevision = _DeviceDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 7),
    _DeviceDiskRevision_Type()
)
deviceDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskRevision.setStatus("current")
_DeviceDiskSerialN_Type = DisplayString
_DeviceDiskSerialN_Object = MibTableColumn
deviceDiskSerialN = _DeviceDiskSerialN_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 8),
    _DeviceDiskSerialN_Type()
)
deviceDiskSerialN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskSerialN.setStatus("current")
_DeviceDiskBlockSize_Type = Counter32
_DeviceDiskBlockSize_Object = MibTableColumn
deviceDiskBlockSize = _DeviceDiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 9),
    _DeviceDiskBlockSize_Type()
)
deviceDiskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskBlockSize.setStatus("current")
_DeviceDiskBlockCount_Type = Counter32
_DeviceDiskBlockCount_Object = MibTableColumn
deviceDiskBlockCount = _DeviceDiskBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 10),
    _DeviceDiskBlockCount_Type()
)
deviceDiskBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskBlockCount.setStatus("current")
_DeviceDiskMIBNotifications_ObjectIdentity = ObjectIdentity
deviceDiskMIBNotifications = _DeviceDiskMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2)
)
_DeviceDiskMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
deviceDiskMIBNotificationsPrefix = _DeviceDiskMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

deviceDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0, 1)
)
deviceDiskTrap.setObjects(
    ("DISK-MIB", "deviceDiskStatus")
)
if mibBuilder.loadTexts:
    deviceDiskTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISK-MIB",
    **{"DiskStatus": DiskStatus,
       "deviceDiskMIB": deviceDiskMIB,
       "deviceDiskMIBObjects": deviceDiskMIBObjects,
       "deviceDiskValues": deviceDiskValues,
       "deviceDiskValueTable": deviceDiskValueTable,
       "deviceDiskValueEntry": deviceDiskValueEntry,
       "deviceDiskIndex": deviceDiskIndex,
       "deviceDiskTrapEnabled": deviceDiskTrapEnabled,
       "deviceDiskStatus": deviceDiskStatus,
       "deviceDiskTimeStamp": deviceDiskTimeStamp,
       "deviceDiskVendor": deviceDiskVendor,
       "deviceDiskProduct": deviceDiskProduct,
       "deviceDiskRevision": deviceDiskRevision,
       "deviceDiskSerialN": deviceDiskSerialN,
       "deviceDiskBlockSize": deviceDiskBlockSize,
       "deviceDiskBlockCount": deviceDiskBlockCount,
       "deviceDiskMIBNotifications": deviceDiskMIBNotifications,
       "deviceDiskMIBNotificationsPrefix": deviceDiskMIBNotificationsPrefix,
       "deviceDiskTrap": deviceDiskTrap}
)
