# SNMP MIB module (DNOS-DEVICE-FILESYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-DEVICE-FILESYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:53 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

fastpathDeviceFileSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44)
)
fastpathDeviceFileSystem.setRevisions(
        ("2011-01-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDeviceFileSystemGroup_ObjectIdentity = ObjectIdentity
agentDeviceFileSystemGroup = _AgentDeviceFileSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1)
)
_AgentDeviceFileSystemTable_Object = MibTable
agentDeviceFileSystemTable = _AgentDeviceFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1)
)
if mibBuilder.loadTexts:
    agentDeviceFileSystemTable.setStatus("current")
_AgentDeviceFileSystemEntry_Object = MibTableRow
agentDeviceFileSystemEntry = _AgentDeviceFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1)
)
agentDeviceFileSystemEntry.setIndexNames(
    (0, "DNOS-DEVICE-FILESYSTEM-MIB", "agentDeviceFileSystemIndex"),
)
if mibBuilder.loadTexts:
    agentDeviceFileSystemEntry.setStatus("current")


class _AgentDeviceFileSystemIndex_Type(Integer32):
    """Custom type agentDeviceFileSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AgentDeviceFileSystemIndex_Type.__name__ = "Integer32"
_AgentDeviceFileSystemIndex_Object = MibTableColumn
agentDeviceFileSystemIndex = _AgentDeviceFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 1),
    _AgentDeviceFileSystemIndex_Type()
)
agentDeviceFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemIndex.setStatus("current")


class _AgentDeviceFileSystemStatus_Type(Integer32):
    """Custom type agentDeviceFileSystemStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("invalid", 3))
    )


_AgentDeviceFileSystemStatus_Type.__name__ = "Integer32"
_AgentDeviceFileSystemStatus_Object = MibTableColumn
agentDeviceFileSystemStatus = _AgentDeviceFileSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 2),
    _AgentDeviceFileSystemStatus_Type()
)
agentDeviceFileSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemStatus.setStatus("current")
_AgentDeviceFileSystemVendorID_Type = DisplayString
_AgentDeviceFileSystemVendorID_Object = MibTableColumn
agentDeviceFileSystemVendorID = _AgentDeviceFileSystemVendorID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 3),
    _AgentDeviceFileSystemVendorID_Type()
)
agentDeviceFileSystemVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemVendorID.setStatus("current")
_AgentDeviceFileSystemProductID_Type = DisplayString
_AgentDeviceFileSystemProductID_Object = MibTableColumn
agentDeviceFileSystemProductID = _AgentDeviceFileSystemProductID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 4),
    _AgentDeviceFileSystemProductID_Type()
)
agentDeviceFileSystemProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemProductID.setStatus("current")
_AgentDeviceFileSystemManufacturer_Type = DisplayString
_AgentDeviceFileSystemManufacturer_Object = MibTableColumn
agentDeviceFileSystemManufacturer = _AgentDeviceFileSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 5),
    _AgentDeviceFileSystemManufacturer_Type()
)
agentDeviceFileSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemManufacturer.setStatus("current")
_AgentDeviceFileSystemSerialNumber_Type = DisplayString
_AgentDeviceFileSystemSerialNumber_Object = MibTableColumn
agentDeviceFileSystemSerialNumber = _AgentDeviceFileSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 6),
    _AgentDeviceFileSystemSerialNumber_Type()
)
agentDeviceFileSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemSerialNumber.setStatus("current")
_AgentDeviceFileSystemVersion_Type = DisplayString
_AgentDeviceFileSystemVersion_Object = MibTableColumn
agentDeviceFileSystemVersion = _AgentDeviceFileSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 7),
    _AgentDeviceFileSystemVersion_Type()
)
agentDeviceFileSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemVersion.setStatus("current")
_AgentDeviceFileSystemProtocol_Type = DisplayString
_AgentDeviceFileSystemProtocol_Object = MibTableColumn
agentDeviceFileSystemProtocol = _AgentDeviceFileSystemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 8),
    _AgentDeviceFileSystemProtocol_Type()
)
agentDeviceFileSystemProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemProtocol.setStatus("current")
_AgentDeviceFileSystemClass_Type = DisplayString
_AgentDeviceFileSystemClass_Object = MibTableColumn
agentDeviceFileSystemClass = _AgentDeviceFileSystemClass_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 9),
    _AgentDeviceFileSystemClass_Type()
)
agentDeviceFileSystemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemClass.setStatus("current")
_AgentDeviceFileSystemSubclass_Type = DisplayString
_AgentDeviceFileSystemSubclass_Object = MibTableColumn
agentDeviceFileSystemSubclass = _AgentDeviceFileSystemSubclass_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 10),
    _AgentDeviceFileSystemSubclass_Type()
)
agentDeviceFileSystemSubclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemSubclass.setStatus("current")
_AgentDeviceFileSystemTotalSize_Type = DisplayString
_AgentDeviceFileSystemTotalSize_Object = MibTableColumn
agentDeviceFileSystemTotalSize = _AgentDeviceFileSystemTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 11),
    _AgentDeviceFileSystemTotalSize_Type()
)
agentDeviceFileSystemTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemTotalSize.setStatus("current")
_AgentDeviceFileSystemBytesUsed_Type = DisplayString
_AgentDeviceFileSystemBytesUsed_Object = MibTableColumn
agentDeviceFileSystemBytesUsed = _AgentDeviceFileSystemBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 12),
    _AgentDeviceFileSystemBytesUsed_Type()
)
agentDeviceFileSystemBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemBytesUsed.setStatus("current")
_AgentDeviceFileSystemBytesFree_Type = DisplayString
_AgentDeviceFileSystemBytesFree_Object = MibTableColumn
agentDeviceFileSystemBytesFree = _AgentDeviceFileSystemBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 13),
    _AgentDeviceFileSystemBytesFree_Type()
)
agentDeviceFileSystemBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemBytesFree.setStatus("current")


class _AgentDeviceFileSystemUnmount_Type(Integer32):
    """Custom type agentDeviceFileSystemUnmount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unmount", 1))
    )


_AgentDeviceFileSystemUnmount_Type.__name__ = "Integer32"
_AgentDeviceFileSystemUnmount_Object = MibTableColumn
agentDeviceFileSystemUnmount = _AgentDeviceFileSystemUnmount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 1, 1, 14),
    _AgentDeviceFileSystemUnmount_Type()
)
agentDeviceFileSystemUnmount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDeviceFileSystemUnmount.setStatus("current")
_AgentDeviceFileSystemContentTable_Object = MibTable
agentDeviceFileSystemContentTable = _AgentDeviceFileSystemContentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2)
)
if mibBuilder.loadTexts:
    agentDeviceFileSystemContentTable.setStatus("current")
_AgentDeviceFileSystemContentEntry_Object = MibTableRow
agentDeviceFileSystemContentEntry = _AgentDeviceFileSystemContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2, 1)
)
agentDeviceFileSystemContentEntry.setIndexNames(
    (0, "DNOS-DEVICE-FILESYSTEM-MIB", "agentDevFileSystemIndex"),
    (0, "DNOS-DEVICE-FILESYSTEM-MIB", "agentDeviceFileSystemContentFileName"),
)
if mibBuilder.loadTexts:
    agentDeviceFileSystemContentEntry.setStatus("current")


class _AgentDevFileSystemIndex_Type(Integer32):
    """Custom type agentDevFileSystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AgentDevFileSystemIndex_Type.__name__ = "Integer32"
_AgentDevFileSystemIndex_Object = MibTableColumn
agentDevFileSystemIndex = _AgentDevFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2, 1, 1),
    _AgentDevFileSystemIndex_Type()
)
agentDevFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDevFileSystemIndex.setStatus("current")
_AgentDeviceFileSystemContentFileName_Type = DisplayString
_AgentDeviceFileSystemContentFileName_Object = MibTableColumn
agentDeviceFileSystemContentFileName = _AgentDeviceFileSystemContentFileName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2, 1, 2),
    _AgentDeviceFileSystemContentFileName_Type()
)
agentDeviceFileSystemContentFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemContentFileName.setStatus("current")
_AgentDeviceFileSystemContentFileSize_Type = Unsigned32
_AgentDeviceFileSystemContentFileSize_Object = MibTableColumn
agentDeviceFileSystemContentFileSize = _AgentDeviceFileSystemContentFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2, 1, 3),
    _AgentDeviceFileSystemContentFileSize_Type()
)
agentDeviceFileSystemContentFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemContentFileSize.setStatus("current")
_AgentDeviceFileSystemContentFileModificationTime_Type = DateAndTime
_AgentDeviceFileSystemContentFileModificationTime_Object = MibTableColumn
agentDeviceFileSystemContentFileModificationTime = _AgentDeviceFileSystemContentFileModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 44, 1, 2, 1, 4),
    _AgentDeviceFileSystemContentFileModificationTime_Type()
)
agentDeviceFileSystemContentFileModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDeviceFileSystemContentFileModificationTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-DEVICE-FILESYSTEM-MIB",
    **{"fastpathDeviceFileSystem": fastpathDeviceFileSystem,
       "agentDeviceFileSystemGroup": agentDeviceFileSystemGroup,
       "agentDeviceFileSystemTable": agentDeviceFileSystemTable,
       "agentDeviceFileSystemEntry": agentDeviceFileSystemEntry,
       "agentDeviceFileSystemIndex": agentDeviceFileSystemIndex,
       "agentDeviceFileSystemStatus": agentDeviceFileSystemStatus,
       "agentDeviceFileSystemVendorID": agentDeviceFileSystemVendorID,
       "agentDeviceFileSystemProductID": agentDeviceFileSystemProductID,
       "agentDeviceFileSystemManufacturer": agentDeviceFileSystemManufacturer,
       "agentDeviceFileSystemSerialNumber": agentDeviceFileSystemSerialNumber,
       "agentDeviceFileSystemVersion": agentDeviceFileSystemVersion,
       "agentDeviceFileSystemProtocol": agentDeviceFileSystemProtocol,
       "agentDeviceFileSystemClass": agentDeviceFileSystemClass,
       "agentDeviceFileSystemSubclass": agentDeviceFileSystemSubclass,
       "agentDeviceFileSystemTotalSize": agentDeviceFileSystemTotalSize,
       "agentDeviceFileSystemBytesUsed": agentDeviceFileSystemBytesUsed,
       "agentDeviceFileSystemBytesFree": agentDeviceFileSystemBytesFree,
       "agentDeviceFileSystemUnmount": agentDeviceFileSystemUnmount,
       "agentDeviceFileSystemContentTable": agentDeviceFileSystemContentTable,
       "agentDeviceFileSystemContentEntry": agentDeviceFileSystemContentEntry,
       "agentDevFileSystemIndex": agentDevFileSystemIndex,
       "agentDeviceFileSystemContentFileName": agentDeviceFileSystemContentFileName,
       "agentDeviceFileSystemContentFileSize": agentDeviceFileSystemContentFileSize,
       "agentDeviceFileSystemContentFileModificationTime": agentDeviceFileSystemContentFileModificationTime}
)
