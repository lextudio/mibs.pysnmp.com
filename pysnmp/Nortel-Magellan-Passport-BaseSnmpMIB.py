# SNMP MIB module (Nortel-Magellan-Passport-BaseSnmpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-BaseSnmpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:25 2024
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

(DisplayString,
 Integer32,
 RowStatus,
 Status,
 StorageType,
 TruthValue,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "Status",
    "StorageType",
    "TruthValue",
    "Unsigned32")

(AsciiString,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "HexString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrSnmp_ObjectIdentity = ObjectIdentity
vrSnmp = _VrSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8)
)
_VrSnmpRowStatusTable_Object = MibTable
vrSnmpRowStatusTable = _VrSnmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1)
)
if mibBuilder.loadTexts:
    vrSnmpRowStatusTable.setStatus("mandatory")
_VrSnmpRowStatusEntry_Object = MibTableRow
vrSnmpRowStatusEntry = _VrSnmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1, 1)
)
vrSnmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpRowStatusEntry.setStatus("mandatory")
_VrSnmpRowStatus_Type = RowStatus
_VrSnmpRowStatus_Object = MibTableColumn
vrSnmpRowStatus = _VrSnmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1, 1, 1),
    _VrSnmpRowStatus_Type()
)
vrSnmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpRowStatus.setStatus("mandatory")
_VrSnmpComponentName_Type = DisplayString
_VrSnmpComponentName_Object = MibTableColumn
vrSnmpComponentName = _VrSnmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1, 1, 2),
    _VrSnmpComponentName_Type()
)
vrSnmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpComponentName.setStatus("mandatory")
_VrSnmpStorageType_Type = StorageType
_VrSnmpStorageType_Object = MibTableColumn
vrSnmpStorageType = _VrSnmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1, 1, 4),
    _VrSnmpStorageType_Type()
)
vrSnmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpStorageType.setStatus("mandatory")
_VrSnmpIndex_Type = NonReplicated
_VrSnmpIndex_Object = MibTableColumn
vrSnmpIndex = _VrSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 1, 1, 10),
    _VrSnmpIndex_Type()
)
vrSnmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpIndex.setStatus("mandatory")
_VrSnmpSys_ObjectIdentity = ObjectIdentity
vrSnmpSys = _VrSnmpSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2)
)
_VrSnmpSysRowStatusTable_Object = MibTable
vrSnmpSysRowStatusTable = _VrSnmpSysRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrSnmpSysRowStatusTable.setStatus("mandatory")
_VrSnmpSysRowStatusEntry_Object = MibTableRow
vrSnmpSysRowStatusEntry = _VrSnmpSysRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1, 1)
)
vrSnmpSysRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpSysRowStatusEntry.setStatus("mandatory")
_VrSnmpSysRowStatus_Type = RowStatus
_VrSnmpSysRowStatus_Object = MibTableColumn
vrSnmpSysRowStatus = _VrSnmpSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1, 1, 1),
    _VrSnmpSysRowStatus_Type()
)
vrSnmpSysRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysRowStatus.setStatus("mandatory")
_VrSnmpSysComponentName_Type = DisplayString
_VrSnmpSysComponentName_Object = MibTableColumn
vrSnmpSysComponentName = _VrSnmpSysComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1, 1, 2),
    _VrSnmpSysComponentName_Type()
)
vrSnmpSysComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysComponentName.setStatus("mandatory")
_VrSnmpSysStorageType_Type = StorageType
_VrSnmpSysStorageType_Object = MibTableColumn
vrSnmpSysStorageType = _VrSnmpSysStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1, 1, 4),
    _VrSnmpSysStorageType_Type()
)
vrSnmpSysStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysStorageType.setStatus("mandatory")
_VrSnmpSysIndex_Type = NonReplicated
_VrSnmpSysIndex_Object = MibTableColumn
vrSnmpSysIndex = _VrSnmpSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 1, 1, 10),
    _VrSnmpSysIndex_Type()
)
vrSnmpSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpSysIndex.setStatus("mandatory")
_VrSnmpSysProvTable_Object = MibTable
vrSnmpSysProvTable = _VrSnmpSysProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 10)
)
if mibBuilder.loadTexts:
    vrSnmpSysProvTable.setStatus("mandatory")
_VrSnmpSysProvEntry_Object = MibTableRow
vrSnmpSysProvEntry = _VrSnmpSysProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 10, 1)
)
vrSnmpSysProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpSysProvEntry.setStatus("mandatory")


class _VrSnmpSysContact_Type(AsciiString):
    """Custom type vrSnmpSysContact based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrSnmpSysContact_Type.__name__ = "AsciiString"
_VrSnmpSysContact_Object = MibTableColumn
vrSnmpSysContact = _VrSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 10, 1, 1),
    _VrSnmpSysContact_Type()
)
vrSnmpSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpSysContact.setStatus("mandatory")


class _VrSnmpSysName_Type(AsciiString):
    """Custom type vrSnmpSysName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrSnmpSysName_Type.__name__ = "AsciiString"
_VrSnmpSysName_Object = MibTableColumn
vrSnmpSysName = _VrSnmpSysName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 10, 1, 2),
    _VrSnmpSysName_Type()
)
vrSnmpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpSysName.setStatus("mandatory")


class _VrSnmpSysLocation_Type(AsciiString):
    """Custom type vrSnmpSysLocation based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrSnmpSysLocation_Type.__name__ = "AsciiString"
_VrSnmpSysLocation_Object = MibTableColumn
vrSnmpSysLocation = _VrSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 10, 1, 3),
    _VrSnmpSysLocation_Type()
)
vrSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpSysLocation.setStatus("mandatory")
_VrSnmpSysOpTable_Object = MibTable
vrSnmpSysOpTable = _VrSnmpSysOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11)
)
if mibBuilder.loadTexts:
    vrSnmpSysOpTable.setStatus("mandatory")
_VrSnmpSysOpEntry_Object = MibTableRow
vrSnmpSysOpEntry = _VrSnmpSysOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11, 1)
)
vrSnmpSysOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpSysOpEntry.setStatus("mandatory")


class _VrSnmpSysDescription_Type(AsciiString):
    """Custom type vrSnmpSysDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrSnmpSysDescription_Type.__name__ = "AsciiString"
_VrSnmpSysDescription_Object = MibTableColumn
vrSnmpSysDescription = _VrSnmpSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11, 1, 1),
    _VrSnmpSysDescription_Type()
)
vrSnmpSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysDescription.setStatus("mandatory")
_VrSnmpSysObjectId_Type = ObjectIdentifier
_VrSnmpSysObjectId_Object = MibTableColumn
vrSnmpSysObjectId = _VrSnmpSysObjectId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11, 1, 2),
    _VrSnmpSysObjectId_Type()
)
vrSnmpSysObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysObjectId.setStatus("mandatory")


class _VrSnmpSysUpTime_Type(Unsigned32):
    """Custom type vrSnmpSysUpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpSysUpTime_Type.__name__ = "Unsigned32"
_VrSnmpSysUpTime_Object = MibTableColumn
vrSnmpSysUpTime = _VrSnmpSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11, 1, 3),
    _VrSnmpSysUpTime_Type()
)
vrSnmpSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysUpTime.setStatus("mandatory")


class _VrSnmpSysServices_Type(Unsigned32):
    """Custom type vrSnmpSysServices based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VrSnmpSysServices_Type.__name__ = "Unsigned32"
_VrSnmpSysServices_Object = MibTableColumn
vrSnmpSysServices = _VrSnmpSysServices_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 2, 11, 1, 4),
    _VrSnmpSysServices_Type()
)
vrSnmpSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpSysServices.setStatus("mandatory")
_VrSnmpCom_ObjectIdentity = ObjectIdentity
vrSnmpCom = _VrSnmpCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3)
)
_VrSnmpComRowStatusTable_Object = MibTable
vrSnmpComRowStatusTable = _VrSnmpComRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vrSnmpComRowStatusTable.setStatus("mandatory")
_VrSnmpComRowStatusEntry_Object = MibTableRow
vrSnmpComRowStatusEntry = _VrSnmpComRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1, 1)
)
vrSnmpComRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpComRowStatusEntry.setStatus("mandatory")
_VrSnmpComRowStatus_Type = RowStatus
_VrSnmpComRowStatus_Object = MibTableColumn
vrSnmpComRowStatus = _VrSnmpComRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1, 1, 1),
    _VrSnmpComRowStatus_Type()
)
vrSnmpComRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComRowStatus.setStatus("mandatory")
_VrSnmpComComponentName_Type = DisplayString
_VrSnmpComComponentName_Object = MibTableColumn
vrSnmpComComponentName = _VrSnmpComComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1, 1, 2),
    _VrSnmpComComponentName_Type()
)
vrSnmpComComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpComComponentName.setStatus("mandatory")
_VrSnmpComStorageType_Type = StorageType
_VrSnmpComStorageType_Object = MibTableColumn
vrSnmpComStorageType = _VrSnmpComStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1, 1, 4),
    _VrSnmpComStorageType_Type()
)
vrSnmpComStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpComStorageType.setStatus("mandatory")


class _VrSnmpComIndex_Type(Integer32):
    """Custom type vrSnmpComIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpComIndex_Type.__name__ = "Integer32"
_VrSnmpComIndex_Object = MibTableColumn
vrSnmpComIndex = _VrSnmpComIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 1, 1, 10),
    _VrSnmpComIndex_Type()
)
vrSnmpComIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpComIndex.setStatus("mandatory")
_VrSnmpComMan_ObjectIdentity = ObjectIdentity
vrSnmpComMan = _VrSnmpComMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2)
)
_VrSnmpComManRowStatusTable_Object = MibTable
vrSnmpComManRowStatusTable = _VrSnmpComManRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrSnmpComManRowStatusTable.setStatus("mandatory")
_VrSnmpComManRowStatusEntry_Object = MibTableRow
vrSnmpComManRowStatusEntry = _VrSnmpComManRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1, 1)
)
vrSnmpComManRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComManIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpComManRowStatusEntry.setStatus("mandatory")
_VrSnmpComManRowStatus_Type = RowStatus
_VrSnmpComManRowStatus_Object = MibTableColumn
vrSnmpComManRowStatus = _VrSnmpComManRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1, 1, 1),
    _VrSnmpComManRowStatus_Type()
)
vrSnmpComManRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComManRowStatus.setStatus("mandatory")
_VrSnmpComManComponentName_Type = DisplayString
_VrSnmpComManComponentName_Object = MibTableColumn
vrSnmpComManComponentName = _VrSnmpComManComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1, 1, 2),
    _VrSnmpComManComponentName_Type()
)
vrSnmpComManComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpComManComponentName.setStatus("mandatory")
_VrSnmpComManStorageType_Type = StorageType
_VrSnmpComManStorageType_Object = MibTableColumn
vrSnmpComManStorageType = _VrSnmpComManStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1, 1, 4),
    _VrSnmpComManStorageType_Type()
)
vrSnmpComManStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpComManStorageType.setStatus("mandatory")


class _VrSnmpComManIndex_Type(Integer32):
    """Custom type vrSnmpComManIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrSnmpComManIndex_Type.__name__ = "Integer32"
_VrSnmpComManIndex_Object = MibTableColumn
vrSnmpComManIndex = _VrSnmpComManIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 1, 1, 10),
    _VrSnmpComManIndex_Type()
)
vrSnmpComManIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpComManIndex.setStatus("mandatory")
_VrSnmpComManProvTable_Object = MibTable
vrSnmpComManProvTable = _VrSnmpComManProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrSnmpComManProvTable.setStatus("mandatory")
_VrSnmpComManProvEntry_Object = MibTableRow
vrSnmpComManProvEntry = _VrSnmpComManProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 10, 1)
)
vrSnmpComManProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComManIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpComManProvEntry.setStatus("mandatory")


class _VrSnmpComManTransportAddress_Type(AsciiString):
    """Custom type vrSnmpComManTransportAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_VrSnmpComManTransportAddress_Type.__name__ = "AsciiString"
_VrSnmpComManTransportAddress_Object = MibTableColumn
vrSnmpComManTransportAddress = _VrSnmpComManTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 10, 1, 1),
    _VrSnmpComManTransportAddress_Type()
)
vrSnmpComManTransportAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComManTransportAddress.setStatus("mandatory")


class _VrSnmpComManPrivileges_Type(OctetString):
    """Custom type vrSnmpComManPrivileges based on OctetString"""
    defaultHexValue = "40"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrSnmpComManPrivileges_Type.__name__ = "OctetString"
_VrSnmpComManPrivileges_Object = MibTableColumn
vrSnmpComManPrivileges = _VrSnmpComManPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 2, 10, 1, 2),
    _VrSnmpComManPrivileges_Type()
)
vrSnmpComManPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComManPrivileges.setStatus("mandatory")
_VrSnmpComProvTable_Object = MibTable
vrSnmpComProvTable = _VrSnmpComProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10)
)
if mibBuilder.loadTexts:
    vrSnmpComProvTable.setStatus("mandatory")
_VrSnmpComProvEntry_Object = MibTableRow
vrSnmpComProvEntry = _VrSnmpComProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10, 1)
)
vrSnmpComProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpComIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpComProvEntry.setStatus("mandatory")


class _VrSnmpComCommunityString_Type(AsciiString):
    """Custom type vrSnmpComCommunityString based on AsciiString"""
    defaultHexValue = "7075626c6963"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_VrSnmpComCommunityString_Type.__name__ = "AsciiString"
_VrSnmpComCommunityString_Object = MibTableColumn
vrSnmpComCommunityString = _VrSnmpComCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10, 1, 1),
    _VrSnmpComCommunityString_Type()
)
vrSnmpComCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComCommunityString.setStatus("mandatory")


class _VrSnmpComAccessMode_Type(Integer32):
    """Custom type vrSnmpComAccessMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_VrSnmpComAccessMode_Type.__name__ = "Integer32"
_VrSnmpComAccessMode_Object = MibTableColumn
vrSnmpComAccessMode = _VrSnmpComAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10, 1, 3),
    _VrSnmpComAccessMode_Type()
)
vrSnmpComAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComAccessMode.setStatus("mandatory")


class _VrSnmpComViewIndex_Type(Unsigned32):
    """Custom type vrSnmpComViewIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpComViewIndex_Type.__name__ = "Unsigned32"
_VrSnmpComViewIndex_Object = MibTableColumn
vrSnmpComViewIndex = _VrSnmpComViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10, 1, 4),
    _VrSnmpComViewIndex_Type()
)
vrSnmpComViewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComViewIndex.setStatus("mandatory")


class _VrSnmpComTDomain_Type(Integer32):
    """Custom type vrSnmpComTDomain based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmpUdpDomain", 1)
    )


_VrSnmpComTDomain_Type.__name__ = "Integer32"
_VrSnmpComTDomain_Object = MibTableColumn
vrSnmpComTDomain = _VrSnmpComTDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 3, 10, 1, 5),
    _VrSnmpComTDomain_Type()
)
vrSnmpComTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpComTDomain.setStatus("mandatory")
_VrSnmpAcl_ObjectIdentity = ObjectIdentity
vrSnmpAcl = _VrSnmpAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4)
)
_VrSnmpAclRowStatusTable_Object = MibTable
vrSnmpAclRowStatusTable = _VrSnmpAclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1)
)
if mibBuilder.loadTexts:
    vrSnmpAclRowStatusTable.setStatus("obsolete")
_VrSnmpAclRowStatusEntry_Object = MibTableRow
vrSnmpAclRowStatusEntry = _VrSnmpAclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1)
)
vrSnmpAclRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclTargetIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclSubjectIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclResourcesIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpAclRowStatusEntry.setStatus("obsolete")
_VrSnmpAclRowStatus_Type = RowStatus
_VrSnmpAclRowStatus_Object = MibTableColumn
vrSnmpAclRowStatus = _VrSnmpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 1),
    _VrSnmpAclRowStatus_Type()
)
vrSnmpAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAclRowStatus.setStatus("obsolete")
_VrSnmpAclComponentName_Type = DisplayString
_VrSnmpAclComponentName_Object = MibTableColumn
vrSnmpAclComponentName = _VrSnmpAclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 2),
    _VrSnmpAclComponentName_Type()
)
vrSnmpAclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpAclComponentName.setStatus("obsolete")
_VrSnmpAclStorageType_Type = StorageType
_VrSnmpAclStorageType_Object = MibTableColumn
vrSnmpAclStorageType = _VrSnmpAclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 4),
    _VrSnmpAclStorageType_Type()
)
vrSnmpAclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpAclStorageType.setStatus("obsolete")


class _VrSnmpAclTargetIndex_Type(Integer32):
    """Custom type vrSnmpAclTargetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_VrSnmpAclTargetIndex_Type.__name__ = "Integer32"
_VrSnmpAclTargetIndex_Object = MibTableColumn
vrSnmpAclTargetIndex = _VrSnmpAclTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 10),
    _VrSnmpAclTargetIndex_Type()
)
vrSnmpAclTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpAclTargetIndex.setStatus("obsolete")


class _VrSnmpAclSubjectIndex_Type(Integer32):
    """Custom type vrSnmpAclSubjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_VrSnmpAclSubjectIndex_Type.__name__ = "Integer32"
_VrSnmpAclSubjectIndex_Object = MibTableColumn
vrSnmpAclSubjectIndex = _VrSnmpAclSubjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 11),
    _VrSnmpAclSubjectIndex_Type()
)
vrSnmpAclSubjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpAclSubjectIndex.setStatus("obsolete")


class _VrSnmpAclResourcesIndex_Type(Integer32):
    """Custom type vrSnmpAclResourcesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_VrSnmpAclResourcesIndex_Type.__name__ = "Integer32"
_VrSnmpAclResourcesIndex_Object = MibTableColumn
vrSnmpAclResourcesIndex = _VrSnmpAclResourcesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 1, 1, 12),
    _VrSnmpAclResourcesIndex_Type()
)
vrSnmpAclResourcesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpAclResourcesIndex.setStatus("obsolete")
_VrSnmpAclProvTable_Object = MibTable
vrSnmpAclProvTable = _VrSnmpAclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 10)
)
if mibBuilder.loadTexts:
    vrSnmpAclProvTable.setStatus("obsolete")
_VrSnmpAclProvEntry_Object = MibTableRow
vrSnmpAclProvEntry = _VrSnmpAclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 10, 1)
)
vrSnmpAclProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclTargetIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclSubjectIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpAclResourcesIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpAclProvEntry.setStatus("obsolete")


class _VrSnmpAclPrivileges_Type(OctetString):
    """Custom type vrSnmpAclPrivileges based on OctetString"""
    defaultHexValue = "60"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrSnmpAclPrivileges_Type.__name__ = "OctetString"
_VrSnmpAclPrivileges_Object = MibTableColumn
vrSnmpAclPrivileges = _VrSnmpAclPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 10, 1, 1),
    _VrSnmpAclPrivileges_Type()
)
vrSnmpAclPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAclPrivileges.setStatus("obsolete")


class _VrSnmpAclRowStorageType_Type(Integer32):
    """Custom type vrSnmpAclRowStorageType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("nonVolatile", 3)
    )


_VrSnmpAclRowStorageType_Type.__name__ = "Integer32"
_VrSnmpAclRowStorageType_Object = MibTableColumn
vrSnmpAclRowStorageType = _VrSnmpAclRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 10, 1, 2),
    _VrSnmpAclRowStorageType_Type()
)
vrSnmpAclRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAclRowStorageType.setStatus("obsolete")


class _VrSnmpAclStdRowStatus_Type(Integer32):
    """Custom type vrSnmpAclStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_VrSnmpAclStdRowStatus_Type.__name__ = "Integer32"
_VrSnmpAclStdRowStatus_Object = MibTableColumn
vrSnmpAclStdRowStatus = _VrSnmpAclStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 4, 10, 1, 3),
    _VrSnmpAclStdRowStatus_Type()
)
vrSnmpAclStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAclStdRowStatus.setStatus("obsolete")
_VrSnmpParty_ObjectIdentity = ObjectIdentity
vrSnmpParty = _VrSnmpParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5)
)
_VrSnmpPartyRowStatusTable_Object = MibTable
vrSnmpPartyRowStatusTable = _VrSnmpPartyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1)
)
if mibBuilder.loadTexts:
    vrSnmpPartyRowStatusTable.setStatus("obsolete")
_VrSnmpPartyRowStatusEntry_Object = MibTableRow
vrSnmpPartyRowStatusEntry = _VrSnmpPartyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1, 1)
)
vrSnmpPartyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpPartyRowStatusEntry.setStatus("obsolete")
_VrSnmpPartyRowStatus_Type = RowStatus
_VrSnmpPartyRowStatus_Object = MibTableColumn
vrSnmpPartyRowStatus = _VrSnmpPartyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1, 1, 1),
    _VrSnmpPartyRowStatus_Type()
)
vrSnmpPartyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyRowStatus.setStatus("obsolete")
_VrSnmpPartyComponentName_Type = DisplayString
_VrSnmpPartyComponentName_Object = MibTableColumn
vrSnmpPartyComponentName = _VrSnmpPartyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1, 1, 2),
    _VrSnmpPartyComponentName_Type()
)
vrSnmpPartyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpPartyComponentName.setStatus("obsolete")
_VrSnmpPartyStorageType_Type = StorageType
_VrSnmpPartyStorageType_Object = MibTableColumn
vrSnmpPartyStorageType = _VrSnmpPartyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1, 1, 4),
    _VrSnmpPartyStorageType_Type()
)
vrSnmpPartyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpPartyStorageType.setStatus("obsolete")
_VrSnmpPartyIdentityIndex_Type = ObjectIdentifier
_VrSnmpPartyIdentityIndex_Object = MibTableColumn
vrSnmpPartyIdentityIndex = _VrSnmpPartyIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 1, 1, 10),
    _VrSnmpPartyIdentityIndex_Type()
)
vrSnmpPartyIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpPartyIdentityIndex.setStatus("obsolete")
_VrSnmpPartyProvTable_Object = MibTable
vrSnmpPartyProvTable = _VrSnmpPartyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10)
)
if mibBuilder.loadTexts:
    vrSnmpPartyProvTable.setStatus("obsolete")
_VrSnmpPartyProvEntry_Object = MibTableRow
vrSnmpPartyProvEntry = _VrSnmpPartyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1)
)
vrSnmpPartyProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpPartyProvEntry.setStatus("obsolete")


class _VrSnmpPartyStdIndex_Type(Unsigned32):
    """Custom type vrSnmpPartyStdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_VrSnmpPartyStdIndex_Type.__name__ = "Unsigned32"
_VrSnmpPartyStdIndex_Object = MibTableColumn
vrSnmpPartyStdIndex = _VrSnmpPartyStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 1),
    _VrSnmpPartyStdIndex_Type()
)
vrSnmpPartyStdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpPartyStdIndex.setStatus("obsolete")


class _VrSnmpPartyTDomain_Type(Integer32):
    """Custom type vrSnmpPartyTDomain based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("snmpUdpDomain", 1)
    )


_VrSnmpPartyTDomain_Type.__name__ = "Integer32"
_VrSnmpPartyTDomain_Object = MibTableColumn
vrSnmpPartyTDomain = _VrSnmpPartyTDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 2),
    _VrSnmpPartyTDomain_Type()
)
vrSnmpPartyTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyTDomain.setStatus("obsolete")


class _VrSnmpPartyTransportAddress_Type(AsciiString):
    """Custom type vrSnmpPartyTransportAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_VrSnmpPartyTransportAddress_Type.__name__ = "AsciiString"
_VrSnmpPartyTransportAddress_Object = MibTableColumn
vrSnmpPartyTransportAddress = _VrSnmpPartyTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 3),
    _VrSnmpPartyTransportAddress_Type()
)
vrSnmpPartyTransportAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyTransportAddress.setStatus("obsolete")


class _VrSnmpPartyMaxMessageSize_Type(Unsigned32):
    """Custom type vrSnmpPartyMaxMessageSize based on Unsigned32"""
    defaultValue = 1400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65507),
    )


_VrSnmpPartyMaxMessageSize_Type.__name__ = "Unsigned32"
_VrSnmpPartyMaxMessageSize_Object = MibTableColumn
vrSnmpPartyMaxMessageSize = _VrSnmpPartyMaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 4),
    _VrSnmpPartyMaxMessageSize_Type()
)
vrSnmpPartyMaxMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyMaxMessageSize.setStatus("obsolete")
_VrSnmpPartyLocal_Type = TruthValue
_VrSnmpPartyLocal_Object = MibTableColumn
vrSnmpPartyLocal = _VrSnmpPartyLocal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 5),
    _VrSnmpPartyLocal_Type()
)
vrSnmpPartyLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyLocal.setStatus("obsolete")


class _VrSnmpPartyAuthProtocol_Type(Integer32):
    """Custom type vrSnmpPartyAuthProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("v2Md5AuthProtocol", 4))
    )


_VrSnmpPartyAuthProtocol_Type.__name__ = "Integer32"
_VrSnmpPartyAuthProtocol_Object = MibTableColumn
vrSnmpPartyAuthProtocol = _VrSnmpPartyAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 6),
    _VrSnmpPartyAuthProtocol_Type()
)
vrSnmpPartyAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyAuthProtocol.setStatus("obsolete")


class _VrSnmpPartyAuthPrivate_Type(HexString):
    """Custom type vrSnmpPartyAuthPrivate based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VrSnmpPartyAuthPrivate_Type.__name__ = "HexString"
_VrSnmpPartyAuthPrivate_Object = MibTableColumn
vrSnmpPartyAuthPrivate = _VrSnmpPartyAuthPrivate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 7),
    _VrSnmpPartyAuthPrivate_Type()
)
vrSnmpPartyAuthPrivate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrSnmpPartyAuthPrivate.setStatus("obsolete")


class _VrSnmpPartyAuthPublic_Type(HexString):
    """Custom type vrSnmpPartyAuthPublic based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VrSnmpPartyAuthPublic_Type.__name__ = "HexString"
_VrSnmpPartyAuthPublic_Object = MibTableColumn
vrSnmpPartyAuthPublic = _VrSnmpPartyAuthPublic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 8),
    _VrSnmpPartyAuthPublic_Type()
)
vrSnmpPartyAuthPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyAuthPublic.setStatus("obsolete")


class _VrSnmpPartyAuthLifetime_Type(Unsigned32):
    """Custom type vrSnmpPartyAuthLifetime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VrSnmpPartyAuthLifetime_Type.__name__ = "Unsigned32"
_VrSnmpPartyAuthLifetime_Object = MibTableColumn
vrSnmpPartyAuthLifetime = _VrSnmpPartyAuthLifetime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 9),
    _VrSnmpPartyAuthLifetime_Type()
)
vrSnmpPartyAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyAuthLifetime.setStatus("obsolete")


class _VrSnmpPartyPrivProtocol_Type(Integer32):
    """Custom type vrSnmpPartyPrivProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("noPriv", 2)
    )


_VrSnmpPartyPrivProtocol_Type.__name__ = "Integer32"
_VrSnmpPartyPrivProtocol_Object = MibTableColumn
vrSnmpPartyPrivProtocol = _VrSnmpPartyPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 10),
    _VrSnmpPartyPrivProtocol_Type()
)
vrSnmpPartyPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyPrivProtocol.setStatus("obsolete")


class _VrSnmpPartyRowStorageType_Type(Integer32):
    """Custom type vrSnmpPartyRowStorageType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("nonVolatile", 3)
    )


_VrSnmpPartyRowStorageType_Type.__name__ = "Integer32"
_VrSnmpPartyRowStorageType_Object = MibTableColumn
vrSnmpPartyRowStorageType = _VrSnmpPartyRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 11),
    _VrSnmpPartyRowStorageType_Type()
)
vrSnmpPartyRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyRowStorageType.setStatus("obsolete")


class _VrSnmpPartyStdRowStatus_Type(Integer32):
    """Custom type vrSnmpPartyStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_VrSnmpPartyStdRowStatus_Type.__name__ = "Integer32"
_VrSnmpPartyStdRowStatus_Object = MibTableColumn
vrSnmpPartyStdRowStatus = _VrSnmpPartyStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 10, 1, 12),
    _VrSnmpPartyStdRowStatus_Type()
)
vrSnmpPartyStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyStdRowStatus.setStatus("obsolete")
_VrSnmpPartyOpTable_Object = MibTable
vrSnmpPartyOpTable = _VrSnmpPartyOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 11)
)
if mibBuilder.loadTexts:
    vrSnmpPartyOpTable.setStatus("obsolete")
_VrSnmpPartyOpEntry_Object = MibTableRow
vrSnmpPartyOpEntry = _VrSnmpPartyOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 11, 1)
)
vrSnmpPartyOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpPartyOpEntry.setStatus("obsolete")


class _VrSnmpPartyTrapNumbers_Type(Unsigned32):
    """Custom type vrSnmpPartyTrapNumbers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpPartyTrapNumbers_Type.__name__ = "Unsigned32"
_VrSnmpPartyTrapNumbers_Object = MibTableColumn
vrSnmpPartyTrapNumbers = _VrSnmpPartyTrapNumbers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 11, 1, 1),
    _VrSnmpPartyTrapNumbers_Type()
)
vrSnmpPartyTrapNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpPartyTrapNumbers.setStatus("obsolete")


class _VrSnmpPartyAuthClock_Type(Unsigned32):
    """Custom type vrSnmpPartyAuthClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpPartyAuthClock_Type.__name__ = "Unsigned32"
_VrSnmpPartyAuthClock_Object = MibTableColumn
vrSnmpPartyAuthClock = _VrSnmpPartyAuthClock_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 5, 11, 1, 2),
    _VrSnmpPartyAuthClock_Type()
)
vrSnmpPartyAuthClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpPartyAuthClock.setStatus("obsolete")
_VrSnmpCon_ObjectIdentity = ObjectIdentity
vrSnmpCon = _VrSnmpCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6)
)
_VrSnmpConRowStatusTable_Object = MibTable
vrSnmpConRowStatusTable = _VrSnmpConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1)
)
if mibBuilder.loadTexts:
    vrSnmpConRowStatusTable.setStatus("obsolete")
_VrSnmpConRowStatusEntry_Object = MibTableRow
vrSnmpConRowStatusEntry = _VrSnmpConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1, 1)
)
vrSnmpConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpConIdentityIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpConRowStatusEntry.setStatus("obsolete")
_VrSnmpConRowStatus_Type = RowStatus
_VrSnmpConRowStatus_Object = MibTableColumn
vrSnmpConRowStatus = _VrSnmpConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1, 1, 1),
    _VrSnmpConRowStatus_Type()
)
vrSnmpConRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConRowStatus.setStatus("obsolete")
_VrSnmpConComponentName_Type = DisplayString
_VrSnmpConComponentName_Object = MibTableColumn
vrSnmpConComponentName = _VrSnmpConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1, 1, 2),
    _VrSnmpConComponentName_Type()
)
vrSnmpConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpConComponentName.setStatus("obsolete")
_VrSnmpConStorageType_Type = StorageType
_VrSnmpConStorageType_Object = MibTableColumn
vrSnmpConStorageType = _VrSnmpConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1, 1, 4),
    _VrSnmpConStorageType_Type()
)
vrSnmpConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpConStorageType.setStatus("obsolete")
_VrSnmpConIdentityIndex_Type = ObjectIdentifier
_VrSnmpConIdentityIndex_Object = MibTableColumn
vrSnmpConIdentityIndex = _VrSnmpConIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 1, 1, 10),
    _VrSnmpConIdentityIndex_Type()
)
vrSnmpConIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpConIdentityIndex.setStatus("obsolete")
_VrSnmpConProvTable_Object = MibTable
vrSnmpConProvTable = _VrSnmpConProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10)
)
if mibBuilder.loadTexts:
    vrSnmpConProvTable.setStatus("obsolete")
_VrSnmpConProvEntry_Object = MibTableRow
vrSnmpConProvEntry = _VrSnmpConProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1)
)
vrSnmpConProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpConIdentityIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpConProvEntry.setStatus("obsolete")


class _VrSnmpConStdIndex_Type(Unsigned32):
    """Custom type vrSnmpConStdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpConStdIndex_Type.__name__ = "Unsigned32"
_VrSnmpConStdIndex_Object = MibTableColumn
vrSnmpConStdIndex = _VrSnmpConStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 1),
    _VrSnmpConStdIndex_Type()
)
vrSnmpConStdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpConStdIndex.setStatus("obsolete")


class _VrSnmpConLocal_Type(Integer32):
    """Custom type vrSnmpConLocal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_VrSnmpConLocal_Type.__name__ = "Integer32"
_VrSnmpConLocal_Object = MibTableColumn
vrSnmpConLocal = _VrSnmpConLocal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 2),
    _VrSnmpConLocal_Type()
)
vrSnmpConLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConLocal.setStatus("obsolete")


class _VrSnmpConViewIndex_Type(Unsigned32):
    """Custom type vrSnmpConViewIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpConViewIndex_Type.__name__ = "Unsigned32"
_VrSnmpConViewIndex_Object = MibTableColumn
vrSnmpConViewIndex = _VrSnmpConViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 3),
    _VrSnmpConViewIndex_Type()
)
vrSnmpConViewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConViewIndex.setStatus("obsolete")


class _VrSnmpConLocalTime_Type(Integer32):
    """Custom type vrSnmpConLocalTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("currentTime", 1)
    )


_VrSnmpConLocalTime_Type.__name__ = "Integer32"
_VrSnmpConLocalTime_Object = MibTableColumn
vrSnmpConLocalTime = _VrSnmpConLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 4),
    _VrSnmpConLocalTime_Type()
)
vrSnmpConLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConLocalTime.setStatus("obsolete")


class _VrSnmpConRowStorageType_Type(Integer32):
    """Custom type vrSnmpConRowStorageType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("nonVolatile", 3)
    )


_VrSnmpConRowStorageType_Type.__name__ = "Integer32"
_VrSnmpConRowStorageType_Object = MibTableColumn
vrSnmpConRowStorageType = _VrSnmpConRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 5),
    _VrSnmpConRowStorageType_Type()
)
vrSnmpConRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConRowStorageType.setStatus("obsolete")


class _VrSnmpConStdRowStatus_Type(Integer32):
    """Custom type vrSnmpConStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_VrSnmpConStdRowStatus_Type.__name__ = "Integer32"
_VrSnmpConStdRowStatus_Object = MibTableColumn
vrSnmpConStdRowStatus = _VrSnmpConStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 6, 10, 1, 6),
    _VrSnmpConStdRowStatus_Type()
)
vrSnmpConStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpConStdRowStatus.setStatus("obsolete")
_VrSnmpView_ObjectIdentity = ObjectIdentity
vrSnmpView = _VrSnmpView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7)
)
_VrSnmpViewRowStatusTable_Object = MibTable
vrSnmpViewRowStatusTable = _VrSnmpViewRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1)
)
if mibBuilder.loadTexts:
    vrSnmpViewRowStatusTable.setStatus("mandatory")
_VrSnmpViewRowStatusEntry_Object = MibTableRow
vrSnmpViewRowStatusEntry = _VrSnmpViewRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1)
)
vrSnmpViewRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpViewIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpViewSubtreeIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpViewRowStatusEntry.setStatus("mandatory")
_VrSnmpViewRowStatus_Type = RowStatus
_VrSnmpViewRowStatus_Object = MibTableColumn
vrSnmpViewRowStatus = _VrSnmpViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1, 1),
    _VrSnmpViewRowStatus_Type()
)
vrSnmpViewRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpViewRowStatus.setStatus("mandatory")
_VrSnmpViewComponentName_Type = DisplayString
_VrSnmpViewComponentName_Object = MibTableColumn
vrSnmpViewComponentName = _VrSnmpViewComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1, 2),
    _VrSnmpViewComponentName_Type()
)
vrSnmpViewComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpViewComponentName.setStatus("mandatory")
_VrSnmpViewStorageType_Type = StorageType
_VrSnmpViewStorageType_Object = MibTableColumn
vrSnmpViewStorageType = _VrSnmpViewStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1, 4),
    _VrSnmpViewStorageType_Type()
)
vrSnmpViewStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpViewStorageType.setStatus("mandatory")


class _VrSnmpViewIndex_Type(Integer32):
    """Custom type vrSnmpViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpViewIndex_Type.__name__ = "Integer32"
_VrSnmpViewIndex_Object = MibTableColumn
vrSnmpViewIndex = _VrSnmpViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1, 10),
    _VrSnmpViewIndex_Type()
)
vrSnmpViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpViewIndex.setStatus("mandatory")
_VrSnmpViewSubtreeIndex_Type = ObjectIdentifier
_VrSnmpViewSubtreeIndex_Object = MibTableColumn
vrSnmpViewSubtreeIndex = _VrSnmpViewSubtreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 1, 1, 11),
    _VrSnmpViewSubtreeIndex_Type()
)
vrSnmpViewSubtreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpViewSubtreeIndex.setStatus("mandatory")
_VrSnmpViewProvTable_Object = MibTable
vrSnmpViewProvTable = _VrSnmpViewProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10)
)
if mibBuilder.loadTexts:
    vrSnmpViewProvTable.setStatus("mandatory")
_VrSnmpViewProvEntry_Object = MibTableRow
vrSnmpViewProvEntry = _VrSnmpViewProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10, 1)
)
vrSnmpViewProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpViewIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpViewSubtreeIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpViewProvEntry.setStatus("mandatory")


class _VrSnmpViewMask_Type(HexString):
    """Custom type vrSnmpViewMask based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VrSnmpViewMask_Type.__name__ = "HexString"
_VrSnmpViewMask_Object = MibTableColumn
vrSnmpViewMask = _VrSnmpViewMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10, 1, 1),
    _VrSnmpViewMask_Type()
)
vrSnmpViewMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpViewMask.setStatus("mandatory")


class _VrSnmpViewType_Type(Integer32):
    """Custom type vrSnmpViewType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excludedSubtree", 2),
          ("includedSubtree", 1))
    )


_VrSnmpViewType_Type.__name__ = "Integer32"
_VrSnmpViewType_Object = MibTableColumn
vrSnmpViewType = _VrSnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10, 1, 2),
    _VrSnmpViewType_Type()
)
vrSnmpViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpViewType.setStatus("mandatory")


class _VrSnmpViewRowStorageType_Type(Integer32):
    """Custom type vrSnmpViewRowStorageType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("nonVolatile", 3)
    )


_VrSnmpViewRowStorageType_Type.__name__ = "Integer32"
_VrSnmpViewRowStorageType_Object = MibTableColumn
vrSnmpViewRowStorageType = _VrSnmpViewRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10, 1, 3),
    _VrSnmpViewRowStorageType_Type()
)
vrSnmpViewRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpViewRowStorageType.setStatus("mandatory")


class _VrSnmpViewStdRowStatus_Type(Integer32):
    """Custom type vrSnmpViewStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_VrSnmpViewStdRowStatus_Type.__name__ = "Integer32"
_VrSnmpViewStdRowStatus_Object = MibTableColumn
vrSnmpViewStdRowStatus = _VrSnmpViewStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 7, 10, 1, 4),
    _VrSnmpViewStdRowStatus_Type()
)
vrSnmpViewStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpViewStdRowStatus.setStatus("mandatory")
_VrSnmpOr_ObjectIdentity = ObjectIdentity
vrSnmpOr = _VrSnmpOr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8)
)
_VrSnmpOrRowStatusTable_Object = MibTable
vrSnmpOrRowStatusTable = _VrSnmpOrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1)
)
if mibBuilder.loadTexts:
    vrSnmpOrRowStatusTable.setStatus("mandatory")
_VrSnmpOrRowStatusEntry_Object = MibTableRow
vrSnmpOrRowStatusEntry = _VrSnmpOrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1, 1)
)
vrSnmpOrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpOrIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpOrRowStatusEntry.setStatus("mandatory")
_VrSnmpOrRowStatus_Type = RowStatus
_VrSnmpOrRowStatus_Object = MibTableColumn
vrSnmpOrRowStatus = _VrSnmpOrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1, 1, 1),
    _VrSnmpOrRowStatus_Type()
)
vrSnmpOrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOrRowStatus.setStatus("mandatory")
_VrSnmpOrComponentName_Type = DisplayString
_VrSnmpOrComponentName_Object = MibTableColumn
vrSnmpOrComponentName = _VrSnmpOrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1, 1, 2),
    _VrSnmpOrComponentName_Type()
)
vrSnmpOrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOrComponentName.setStatus("mandatory")
_VrSnmpOrStorageType_Type = StorageType
_VrSnmpOrStorageType_Object = MibTableColumn
vrSnmpOrStorageType = _VrSnmpOrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1, 1, 4),
    _VrSnmpOrStorageType_Type()
)
vrSnmpOrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOrStorageType.setStatus("mandatory")


class _VrSnmpOrIndex_Type(Integer32):
    """Custom type vrSnmpOrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrSnmpOrIndex_Type.__name__ = "Integer32"
_VrSnmpOrIndex_Object = MibTableColumn
vrSnmpOrIndex = _VrSnmpOrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 1, 1, 10),
    _VrSnmpOrIndex_Type()
)
vrSnmpOrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpOrIndex.setStatus("mandatory")
_VrSnmpOrOrTable_Object = MibTable
vrSnmpOrOrTable = _VrSnmpOrOrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 10)
)
if mibBuilder.loadTexts:
    vrSnmpOrOrTable.setStatus("mandatory")
_VrSnmpOrOrEntry_Object = MibTableRow
vrSnmpOrOrEntry = _VrSnmpOrOrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 10, 1)
)
vrSnmpOrOrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpOrIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpOrOrEntry.setStatus("mandatory")
_VrSnmpOrId_Type = ObjectIdentifier
_VrSnmpOrId_Object = MibTableColumn
vrSnmpOrId = _VrSnmpOrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 10, 1, 2),
    _VrSnmpOrId_Type()
)
vrSnmpOrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOrId.setStatus("mandatory")


class _VrSnmpOrDescr_Type(AsciiString):
    """Custom type vrSnmpOrDescr based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrSnmpOrDescr_Type.__name__ = "AsciiString"
_VrSnmpOrDescr_Object = MibTableColumn
vrSnmpOrDescr = _VrSnmpOrDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 8, 10, 1, 3),
    _VrSnmpOrDescr_Type()
)
vrSnmpOrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOrDescr.setStatus("mandatory")
_VrSnmpV2Stats_ObjectIdentity = ObjectIdentity
vrSnmpV2Stats = _VrSnmpV2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9)
)
_VrSnmpV2StatsRowStatusTable_Object = MibTable
vrSnmpV2StatsRowStatusTable = _VrSnmpV2StatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1)
)
if mibBuilder.loadTexts:
    vrSnmpV2StatsRowStatusTable.setStatus("obsolete")
_VrSnmpV2StatsRowStatusEntry_Object = MibTableRow
vrSnmpV2StatsRowStatusEntry = _VrSnmpV2StatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1, 1)
)
vrSnmpV2StatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpV2StatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpV2StatsRowStatusEntry.setStatus("obsolete")
_VrSnmpV2StatsRowStatus_Type = RowStatus
_VrSnmpV2StatsRowStatus_Object = MibTableColumn
vrSnmpV2StatsRowStatus = _VrSnmpV2StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1, 1, 1),
    _VrSnmpV2StatsRowStatus_Type()
)
vrSnmpV2StatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsRowStatus.setStatus("obsolete")
_VrSnmpV2StatsComponentName_Type = DisplayString
_VrSnmpV2StatsComponentName_Object = MibTableColumn
vrSnmpV2StatsComponentName = _VrSnmpV2StatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1, 1, 2),
    _VrSnmpV2StatsComponentName_Type()
)
vrSnmpV2StatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsComponentName.setStatus("obsolete")
_VrSnmpV2StatsStorageType_Type = StorageType
_VrSnmpV2StatsStorageType_Object = MibTableColumn
vrSnmpV2StatsStorageType = _VrSnmpV2StatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1, 1, 4),
    _VrSnmpV2StatsStorageType_Type()
)
vrSnmpV2StatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsStorageType.setStatus("obsolete")
_VrSnmpV2StatsIndex_Type = NonReplicated
_VrSnmpV2StatsIndex_Object = MibTableColumn
vrSnmpV2StatsIndex = _VrSnmpV2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 1, 1, 10),
    _VrSnmpV2StatsIndex_Type()
)
vrSnmpV2StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpV2StatsIndex.setStatus("obsolete")
_VrSnmpV2StatsStatsTable_Object = MibTable
vrSnmpV2StatsStatsTable = _VrSnmpV2StatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10)
)
if mibBuilder.loadTexts:
    vrSnmpV2StatsStatsTable.setStatus("obsolete")
_VrSnmpV2StatsStatsEntry_Object = MibTableRow
vrSnmpV2StatsStatsEntry = _VrSnmpV2StatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1)
)
vrSnmpV2StatsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpV2StatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpV2StatsStatsEntry.setStatus("obsolete")


class _VrSnmpV2StatsPackets_Type(Unsigned32):
    """Custom type vrSnmpV2StatsPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsPackets_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsPackets_Object = MibTableColumn
vrSnmpV2StatsPackets = _VrSnmpV2StatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 1),
    _VrSnmpV2StatsPackets_Type()
)
vrSnmpV2StatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsPackets.setStatus("obsolete")


class _VrSnmpV2StatsEncodingErrors_Type(Unsigned32):
    """Custom type vrSnmpV2StatsEncodingErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsEncodingErrors_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsEncodingErrors_Object = MibTableColumn
vrSnmpV2StatsEncodingErrors = _VrSnmpV2StatsEncodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 2),
    _VrSnmpV2StatsEncodingErrors_Type()
)
vrSnmpV2StatsEncodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsEncodingErrors.setStatus("obsolete")


class _VrSnmpV2StatsUnknownSrcParties_Type(Unsigned32):
    """Custom type vrSnmpV2StatsUnknownSrcParties based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsUnknownSrcParties_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsUnknownSrcParties_Object = MibTableColumn
vrSnmpV2StatsUnknownSrcParties = _VrSnmpV2StatsUnknownSrcParties_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 3),
    _VrSnmpV2StatsUnknownSrcParties_Type()
)
vrSnmpV2StatsUnknownSrcParties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsUnknownSrcParties.setStatus("obsolete")


class _VrSnmpV2StatsBadAuths_Type(Unsigned32):
    """Custom type vrSnmpV2StatsBadAuths based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsBadAuths_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsBadAuths_Object = MibTableColumn
vrSnmpV2StatsBadAuths = _VrSnmpV2StatsBadAuths_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 4),
    _VrSnmpV2StatsBadAuths_Type()
)
vrSnmpV2StatsBadAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsBadAuths.setStatus("obsolete")


class _VrSnmpV2StatsNotInLifetime_Type(Unsigned32):
    """Custom type vrSnmpV2StatsNotInLifetime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsNotInLifetime_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsNotInLifetime_Object = MibTableColumn
vrSnmpV2StatsNotInLifetime = _VrSnmpV2StatsNotInLifetime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 5),
    _VrSnmpV2StatsNotInLifetime_Type()
)
vrSnmpV2StatsNotInLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsNotInLifetime.setStatus("obsolete")


class _VrSnmpV2StatsWrongDigestValues_Type(Unsigned32):
    """Custom type vrSnmpV2StatsWrongDigestValues based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsWrongDigestValues_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsWrongDigestValues_Object = MibTableColumn
vrSnmpV2StatsWrongDigestValues = _VrSnmpV2StatsWrongDigestValues_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 6),
    _VrSnmpV2StatsWrongDigestValues_Type()
)
vrSnmpV2StatsWrongDigestValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsWrongDigestValues.setStatus("obsolete")


class _VrSnmpV2StatsUnknownContexts_Type(Unsigned32):
    """Custom type vrSnmpV2StatsUnknownContexts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsUnknownContexts_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsUnknownContexts_Object = MibTableColumn
vrSnmpV2StatsUnknownContexts = _VrSnmpV2StatsUnknownContexts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 7),
    _VrSnmpV2StatsUnknownContexts_Type()
)
vrSnmpV2StatsUnknownContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsUnknownContexts.setStatus("obsolete")


class _VrSnmpV2StatsBadOperations_Type(Unsigned32):
    """Custom type vrSnmpV2StatsBadOperations based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsBadOperations_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsBadOperations_Object = MibTableColumn
vrSnmpV2StatsBadOperations = _VrSnmpV2StatsBadOperations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 8),
    _VrSnmpV2StatsBadOperations_Type()
)
vrSnmpV2StatsBadOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsBadOperations.setStatus("obsolete")


class _VrSnmpV2StatsSilentDrops_Type(Unsigned32):
    """Custom type vrSnmpV2StatsSilentDrops based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV2StatsSilentDrops_Type.__name__ = "Unsigned32"
_VrSnmpV2StatsSilentDrops_Object = MibTableColumn
vrSnmpV2StatsSilentDrops = _VrSnmpV2StatsSilentDrops_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 9, 10, 1, 9),
    _VrSnmpV2StatsSilentDrops_Type()
)
vrSnmpV2StatsSilentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV2StatsSilentDrops.setStatus("obsolete")
_VrSnmpV1Stats_ObjectIdentity = ObjectIdentity
vrSnmpV1Stats = _VrSnmpV1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10)
)
_VrSnmpV1StatsRowStatusTable_Object = MibTable
vrSnmpV1StatsRowStatusTable = _VrSnmpV1StatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1)
)
if mibBuilder.loadTexts:
    vrSnmpV1StatsRowStatusTable.setStatus("mandatory")
_VrSnmpV1StatsRowStatusEntry_Object = MibTableRow
vrSnmpV1StatsRowStatusEntry = _VrSnmpV1StatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1, 1)
)
vrSnmpV1StatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpV1StatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpV1StatsRowStatusEntry.setStatus("mandatory")
_VrSnmpV1StatsRowStatus_Type = RowStatus
_VrSnmpV1StatsRowStatus_Object = MibTableColumn
vrSnmpV1StatsRowStatus = _VrSnmpV1StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1, 1, 1),
    _VrSnmpV1StatsRowStatus_Type()
)
vrSnmpV1StatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV1StatsRowStatus.setStatus("mandatory")
_VrSnmpV1StatsComponentName_Type = DisplayString
_VrSnmpV1StatsComponentName_Object = MibTableColumn
vrSnmpV1StatsComponentName = _VrSnmpV1StatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1, 1, 2),
    _VrSnmpV1StatsComponentName_Type()
)
vrSnmpV1StatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV1StatsComponentName.setStatus("mandatory")
_VrSnmpV1StatsStorageType_Type = StorageType
_VrSnmpV1StatsStorageType_Object = MibTableColumn
vrSnmpV1StatsStorageType = _VrSnmpV1StatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1, 1, 4),
    _VrSnmpV1StatsStorageType_Type()
)
vrSnmpV1StatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV1StatsStorageType.setStatus("mandatory")
_VrSnmpV1StatsIndex_Type = NonReplicated
_VrSnmpV1StatsIndex_Object = MibTableColumn
vrSnmpV1StatsIndex = _VrSnmpV1StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 1, 1, 10),
    _VrSnmpV1StatsIndex_Type()
)
vrSnmpV1StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpV1StatsIndex.setStatus("mandatory")
_VrSnmpV1StatsStatsTable_Object = MibTable
vrSnmpV1StatsStatsTable = _VrSnmpV1StatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 10)
)
if mibBuilder.loadTexts:
    vrSnmpV1StatsStatsTable.setStatus("mandatory")
_VrSnmpV1StatsStatsEntry_Object = MibTableRow
vrSnmpV1StatsStatsEntry = _VrSnmpV1StatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 10, 1)
)
vrSnmpV1StatsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpV1StatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpV1StatsStatsEntry.setStatus("mandatory")


class _VrSnmpV1StatsBadCommunityNames_Type(Unsigned32):
    """Custom type vrSnmpV1StatsBadCommunityNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV1StatsBadCommunityNames_Type.__name__ = "Unsigned32"
_VrSnmpV1StatsBadCommunityNames_Object = MibTableColumn
vrSnmpV1StatsBadCommunityNames = _VrSnmpV1StatsBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 10, 1, 1),
    _VrSnmpV1StatsBadCommunityNames_Type()
)
vrSnmpV1StatsBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV1StatsBadCommunityNames.setStatus("mandatory")


class _VrSnmpV1StatsBadCommunityUses_Type(Unsigned32):
    """Custom type vrSnmpV1StatsBadCommunityUses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpV1StatsBadCommunityUses_Type.__name__ = "Unsigned32"
_VrSnmpV1StatsBadCommunityUses_Object = MibTableColumn
vrSnmpV1StatsBadCommunityUses = _VrSnmpV1StatsBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 10, 10, 1, 2),
    _VrSnmpV1StatsBadCommunityUses_Type()
)
vrSnmpV1StatsBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpV1StatsBadCommunityUses.setStatus("mandatory")
_VrSnmpMibIIStats_ObjectIdentity = ObjectIdentity
vrSnmpMibIIStats = _VrSnmpMibIIStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11)
)
_VrSnmpMibIIStatsRowStatusTable_Object = MibTable
vrSnmpMibIIStatsRowStatusTable = _VrSnmpMibIIStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1)
)
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsRowStatusTable.setStatus("mandatory")
_VrSnmpMibIIStatsRowStatusEntry_Object = MibTableRow
vrSnmpMibIIStatsRowStatusEntry = _VrSnmpMibIIStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1, 1)
)
vrSnmpMibIIStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpMibIIStatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsRowStatusEntry.setStatus("mandatory")
_VrSnmpMibIIStatsRowStatus_Type = RowStatus
_VrSnmpMibIIStatsRowStatus_Object = MibTableColumn
vrSnmpMibIIStatsRowStatus = _VrSnmpMibIIStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1, 1, 1),
    _VrSnmpMibIIStatsRowStatus_Type()
)
vrSnmpMibIIStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsRowStatus.setStatus("mandatory")
_VrSnmpMibIIStatsComponentName_Type = DisplayString
_VrSnmpMibIIStatsComponentName_Object = MibTableColumn
vrSnmpMibIIStatsComponentName = _VrSnmpMibIIStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1, 1, 2),
    _VrSnmpMibIIStatsComponentName_Type()
)
vrSnmpMibIIStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsComponentName.setStatus("mandatory")
_VrSnmpMibIIStatsStorageType_Type = StorageType
_VrSnmpMibIIStatsStorageType_Object = MibTableColumn
vrSnmpMibIIStatsStorageType = _VrSnmpMibIIStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1, 1, 4),
    _VrSnmpMibIIStatsStorageType_Type()
)
vrSnmpMibIIStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsStorageType.setStatus("mandatory")
_VrSnmpMibIIStatsIndex_Type = NonReplicated
_VrSnmpMibIIStatsIndex_Object = MibTableColumn
vrSnmpMibIIStatsIndex = _VrSnmpMibIIStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 1, 1, 10),
    _VrSnmpMibIIStatsIndex_Type()
)
vrSnmpMibIIStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsIndex.setStatus("mandatory")
_VrSnmpMibIIStatsStatsTable_Object = MibTable
vrSnmpMibIIStatsStatsTable = _VrSnmpMibIIStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10)
)
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsStatsTable.setStatus("mandatory")
_VrSnmpMibIIStatsStatsEntry_Object = MibTableRow
vrSnmpMibIIStatsStatsEntry = _VrSnmpMibIIStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1)
)
vrSnmpMibIIStatsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpMibIIStatsIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsStatsEntry.setStatus("mandatory")


class _VrSnmpMibIIStatsInPackets_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInPackets_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInPackets_Object = MibTableColumn
vrSnmpMibIIStatsInPackets = _VrSnmpMibIIStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 1),
    _VrSnmpMibIIStatsInPackets_Type()
)
vrSnmpMibIIStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInPackets.setStatus("mandatory")


class _VrSnmpMibIIStatsInBadCommunityNames_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInBadCommunityNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInBadCommunityNames_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInBadCommunityNames_Object = MibTableColumn
vrSnmpMibIIStatsInBadCommunityNames = _VrSnmpMibIIStatsInBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 2),
    _VrSnmpMibIIStatsInBadCommunityNames_Type()
)
vrSnmpMibIIStatsInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInBadCommunityNames.setStatus("mandatory")


class _VrSnmpMibIIStatsInBadCommunityUses_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInBadCommunityUses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInBadCommunityUses_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInBadCommunityUses_Object = MibTableColumn
vrSnmpMibIIStatsInBadCommunityUses = _VrSnmpMibIIStatsInBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 3),
    _VrSnmpMibIIStatsInBadCommunityUses_Type()
)
vrSnmpMibIIStatsInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInBadCommunityUses.setStatus("mandatory")


class _VrSnmpMibIIStatsInAsnParseErrs_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInAsnParseErrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInAsnParseErrs_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInAsnParseErrs_Object = MibTableColumn
vrSnmpMibIIStatsInAsnParseErrs = _VrSnmpMibIIStatsInAsnParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 4),
    _VrSnmpMibIIStatsInAsnParseErrs_Type()
)
vrSnmpMibIIStatsInAsnParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInAsnParseErrs.setStatus("mandatory")


class _VrSnmpMibIIStatsOutPackets_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutPackets_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutPackets_Object = MibTableColumn
vrSnmpMibIIStatsOutPackets = _VrSnmpMibIIStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 5),
    _VrSnmpMibIIStatsOutPackets_Type()
)
vrSnmpMibIIStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutPackets.setStatus("mandatory")


class _VrSnmpMibIIStatsInBadVersions_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInBadVersions based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInBadVersions_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInBadVersions_Object = MibTableColumn
vrSnmpMibIIStatsInBadVersions = _VrSnmpMibIIStatsInBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 6),
    _VrSnmpMibIIStatsInBadVersions_Type()
)
vrSnmpMibIIStatsInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInBadVersions.setStatus("mandatory")


class _VrSnmpMibIIStatsInTotalReqVars_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInTotalReqVars based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInTotalReqVars_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInTotalReqVars_Object = MibTableColumn
vrSnmpMibIIStatsInTotalReqVars = _VrSnmpMibIIStatsInTotalReqVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 7),
    _VrSnmpMibIIStatsInTotalReqVars_Type()
)
vrSnmpMibIIStatsInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInTotalReqVars.setStatus("mandatory")


class _VrSnmpMibIIStatsInTotalSetVars_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInTotalSetVars based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInTotalSetVars_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInTotalSetVars_Object = MibTableColumn
vrSnmpMibIIStatsInTotalSetVars = _VrSnmpMibIIStatsInTotalSetVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 8),
    _VrSnmpMibIIStatsInTotalSetVars_Type()
)
vrSnmpMibIIStatsInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInTotalSetVars.setStatus("mandatory")


class _VrSnmpMibIIStatsInGetRequests_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInGetRequests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInGetRequests_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInGetRequests_Object = MibTableColumn
vrSnmpMibIIStatsInGetRequests = _VrSnmpMibIIStatsInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 9),
    _VrSnmpMibIIStatsInGetRequests_Type()
)
vrSnmpMibIIStatsInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInGetRequests.setStatus("mandatory")


class _VrSnmpMibIIStatsInGetNexts_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInGetNexts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInGetNexts_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInGetNexts_Object = MibTableColumn
vrSnmpMibIIStatsInGetNexts = _VrSnmpMibIIStatsInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 10),
    _VrSnmpMibIIStatsInGetNexts_Type()
)
vrSnmpMibIIStatsInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInGetNexts.setStatus("mandatory")


class _VrSnmpMibIIStatsInSetRequests_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsInSetRequests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsInSetRequests_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsInSetRequests_Object = MibTableColumn
vrSnmpMibIIStatsInSetRequests = _VrSnmpMibIIStatsInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 11),
    _VrSnmpMibIIStatsInSetRequests_Type()
)
vrSnmpMibIIStatsInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsInSetRequests.setStatus("mandatory")


class _VrSnmpMibIIStatsOutTooBigs_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutTooBigs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutTooBigs_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutTooBigs_Object = MibTableColumn
vrSnmpMibIIStatsOutTooBigs = _VrSnmpMibIIStatsOutTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 12),
    _VrSnmpMibIIStatsOutTooBigs_Type()
)
vrSnmpMibIIStatsOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutTooBigs.setStatus("mandatory")


class _VrSnmpMibIIStatsOutNoSuchNames_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutNoSuchNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutNoSuchNames_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutNoSuchNames_Object = MibTableColumn
vrSnmpMibIIStatsOutNoSuchNames = _VrSnmpMibIIStatsOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 13),
    _VrSnmpMibIIStatsOutNoSuchNames_Type()
)
vrSnmpMibIIStatsOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutNoSuchNames.setStatus("mandatory")


class _VrSnmpMibIIStatsOutBadValues_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutBadValues based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutBadValues_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutBadValues_Object = MibTableColumn
vrSnmpMibIIStatsOutBadValues = _VrSnmpMibIIStatsOutBadValues_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 14),
    _VrSnmpMibIIStatsOutBadValues_Type()
)
vrSnmpMibIIStatsOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutBadValues.setStatus("mandatory")


class _VrSnmpMibIIStatsOutGenErrs_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutGenErrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutGenErrs_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutGenErrs_Object = MibTableColumn
vrSnmpMibIIStatsOutGenErrs = _VrSnmpMibIIStatsOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 15),
    _VrSnmpMibIIStatsOutGenErrs_Type()
)
vrSnmpMibIIStatsOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutGenErrs.setStatus("mandatory")


class _VrSnmpMibIIStatsOutGetResponses_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutGetResponses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutGetResponses_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutGetResponses_Object = MibTableColumn
vrSnmpMibIIStatsOutGetResponses = _VrSnmpMibIIStatsOutGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 16),
    _VrSnmpMibIIStatsOutGetResponses_Type()
)
vrSnmpMibIIStatsOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutGetResponses.setStatus("mandatory")


class _VrSnmpMibIIStatsOutTraps_Type(Unsigned32):
    """Custom type vrSnmpMibIIStatsOutTraps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpMibIIStatsOutTraps_Type.__name__ = "Unsigned32"
_VrSnmpMibIIStatsOutTraps_Object = MibTableColumn
vrSnmpMibIIStatsOutTraps = _VrSnmpMibIIStatsOutTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 11, 10, 1, 17),
    _VrSnmpMibIIStatsOutTraps_Type()
)
vrSnmpMibIIStatsOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMibIIStatsOutTraps.setStatus("mandatory")
_VrSnmpProvTable_Object = MibTable
vrSnmpProvTable = _VrSnmpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20)
)
if mibBuilder.loadTexts:
    vrSnmpProvTable.setStatus("mandatory")
_VrSnmpProvEntry_Object = MibTableRow
vrSnmpProvEntry = _VrSnmpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1)
)
vrSnmpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpProvEntry.setStatus("mandatory")
_VrSnmpV1EnableAuthenTraps_Type = Status
_VrSnmpV1EnableAuthenTraps_Object = MibTableColumn
vrSnmpV1EnableAuthenTraps = _VrSnmpV1EnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1, 1),
    _VrSnmpV1EnableAuthenTraps_Type()
)
vrSnmpV1EnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpV1EnableAuthenTraps.setStatus("mandatory")
_VrSnmpV2EnableAuthenTraps_Type = Status
_VrSnmpV2EnableAuthenTraps_Object = MibTableColumn
vrSnmpV2EnableAuthenTraps = _VrSnmpV2EnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1, 2),
    _VrSnmpV2EnableAuthenTraps_Type()
)
vrSnmpV2EnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpV2EnableAuthenTraps.setStatus("mandatory")
_VrSnmpAlarmsAsTraps_Type = Status
_VrSnmpAlarmsAsTraps_Object = MibTableColumn
vrSnmpAlarmsAsTraps = _VrSnmpAlarmsAsTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1, 3),
    _VrSnmpAlarmsAsTraps_Type()
)
vrSnmpAlarmsAsTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAlarmsAsTraps.setStatus("mandatory")


class _VrSnmpIpStack_Type(Integer32):
    """Custom type vrSnmpIpStack based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipiFrIpiVc", 2),
          ("vrIp", 1))
    )


_VrSnmpIpStack_Type.__name__ = "Integer32"
_VrSnmpIpStack_Object = MibTableColumn
vrSnmpIpStack = _VrSnmpIpStack_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1, 4),
    _VrSnmpIpStack_Type()
)
vrSnmpIpStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpIpStack.setStatus("mandatory")
_VrSnmpCidInEntTraps_Type = Status
_VrSnmpCidInEntTraps_Object = MibTableColumn
vrSnmpCidInEntTraps = _VrSnmpCidInEntTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 20, 1, 5),
    _VrSnmpCidInEntTraps_Type()
)
vrSnmpCidInEntTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpCidInEntTraps.setStatus("mandatory")
_VrSnmpStateTable_Object = MibTable
vrSnmpStateTable = _VrSnmpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21)
)
if mibBuilder.loadTexts:
    vrSnmpStateTable.setStatus("mandatory")
_VrSnmpStateEntry_Object = MibTableRow
vrSnmpStateEntry = _VrSnmpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1)
)
vrSnmpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpStateEntry.setStatus("mandatory")


class _VrSnmpAdminState_Type(Integer32):
    """Custom type vrSnmpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_VrSnmpAdminState_Type.__name__ = "Integer32"
_VrSnmpAdminState_Object = MibTableColumn
vrSnmpAdminState = _VrSnmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 1),
    _VrSnmpAdminState_Type()
)
vrSnmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpAdminState.setStatus("mandatory")


class _VrSnmpOperationalState_Type(Integer32):
    """Custom type vrSnmpOperationalState based on Integer32"""
    defaultValue = 0

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


_VrSnmpOperationalState_Type.__name__ = "Integer32"
_VrSnmpOperationalState_Object = MibTableColumn
vrSnmpOperationalState = _VrSnmpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 2),
    _VrSnmpOperationalState_Type()
)
vrSnmpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOperationalState.setStatus("mandatory")


class _VrSnmpUsageState_Type(Integer32):
    """Custom type vrSnmpUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_VrSnmpUsageState_Type.__name__ = "Integer32"
_VrSnmpUsageState_Object = MibTableColumn
vrSnmpUsageState = _VrSnmpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 3),
    _VrSnmpUsageState_Type()
)
vrSnmpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpUsageState.setStatus("mandatory")


class _VrSnmpAvailabilityStatus_Type(OctetString):
    """Custom type vrSnmpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VrSnmpAvailabilityStatus_Type.__name__ = "OctetString"
_VrSnmpAvailabilityStatus_Object = MibTableColumn
vrSnmpAvailabilityStatus = _VrSnmpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 4),
    _VrSnmpAvailabilityStatus_Type()
)
vrSnmpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpAvailabilityStatus.setStatus("mandatory")


class _VrSnmpProceduralStatus_Type(OctetString):
    """Custom type vrSnmpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrSnmpProceduralStatus_Type.__name__ = "OctetString"
_VrSnmpProceduralStatus_Object = MibTableColumn
vrSnmpProceduralStatus = _VrSnmpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 5),
    _VrSnmpProceduralStatus_Type()
)
vrSnmpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpProceduralStatus.setStatus("mandatory")


class _VrSnmpControlStatus_Type(OctetString):
    """Custom type vrSnmpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrSnmpControlStatus_Type.__name__ = "OctetString"
_VrSnmpControlStatus_Object = MibTableColumn
vrSnmpControlStatus = _VrSnmpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 6),
    _VrSnmpControlStatus_Type()
)
vrSnmpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpControlStatus.setStatus("mandatory")


class _VrSnmpAlarmStatus_Type(OctetString):
    """Custom type vrSnmpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrSnmpAlarmStatus_Type.__name__ = "OctetString"
_VrSnmpAlarmStatus_Object = MibTableColumn
vrSnmpAlarmStatus = _VrSnmpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 7),
    _VrSnmpAlarmStatus_Type()
)
vrSnmpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpAlarmStatus.setStatus("mandatory")


class _VrSnmpStandbyStatus_Type(Integer32):
    """Custom type vrSnmpStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_VrSnmpStandbyStatus_Type.__name__ = "Integer32"
_VrSnmpStandbyStatus_Object = MibTableColumn
vrSnmpStandbyStatus = _VrSnmpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 8),
    _VrSnmpStandbyStatus_Type()
)
vrSnmpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpStandbyStatus.setStatus("mandatory")


class _VrSnmpUnknownStatus_Type(Integer32):
    """Custom type vrSnmpUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_VrSnmpUnknownStatus_Type.__name__ = "Integer32"
_VrSnmpUnknownStatus_Object = MibTableColumn
vrSnmpUnknownStatus = _VrSnmpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 21, 1, 9),
    _VrSnmpUnknownStatus_Type()
)
vrSnmpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpUnknownStatus.setStatus("mandatory")
_VrSnmpStatsTable_Object = MibTable
vrSnmpStatsTable = _VrSnmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22)
)
if mibBuilder.loadTexts:
    vrSnmpStatsTable.setStatus("mandatory")
_VrSnmpStatsEntry_Object = MibTableRow
vrSnmpStatsEntry = _VrSnmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1)
)
vrSnmpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrSnmpIndex"),
)
if mibBuilder.loadTexts:
    vrSnmpStatsEntry.setStatus("mandatory")


class _VrSnmpLastOrChange_Type(Unsigned32):
    """Custom type vrSnmpLastOrChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpLastOrChange_Type.__name__ = "Unsigned32"
_VrSnmpLastOrChange_Object = MibTableColumn
vrSnmpLastOrChange = _VrSnmpLastOrChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1, 1),
    _VrSnmpLastOrChange_Type()
)
vrSnmpLastOrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpLastOrChange.setStatus("mandatory")


class _VrSnmpTrapsProcessed_Type(Unsigned32):
    """Custom type vrSnmpTrapsProcessed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpTrapsProcessed_Type.__name__ = "Unsigned32"
_VrSnmpTrapsProcessed_Object = MibTableColumn
vrSnmpTrapsProcessed = _VrSnmpTrapsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1, 2),
    _VrSnmpTrapsProcessed_Type()
)
vrSnmpTrapsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpTrapsProcessed.setStatus("mandatory")


class _VrSnmpTrapsDiscarded_Type(Unsigned32):
    """Custom type vrSnmpTrapsDiscarded based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpTrapsDiscarded_Type.__name__ = "Unsigned32"
_VrSnmpTrapsDiscarded_Object = MibTableColumn
vrSnmpTrapsDiscarded = _VrSnmpTrapsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1, 3),
    _VrSnmpTrapsDiscarded_Type()
)
vrSnmpTrapsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpTrapsDiscarded.setStatus("mandatory")


class _VrSnmpLastAuthFailure_Type(Unsigned32):
    """Custom type vrSnmpLastAuthFailure based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrSnmpLastAuthFailure_Type.__name__ = "Unsigned32"
_VrSnmpLastAuthFailure_Object = MibTableColumn
vrSnmpLastAuthFailure = _VrSnmpLastAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1, 4),
    _VrSnmpLastAuthFailure_Type()
)
vrSnmpLastAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpLastAuthFailure.setStatus("mandatory")


class _VrSnmpMgrOfLastAuthFailure_Type(IpAddress):
    """Custom type vrSnmpMgrOfLastAuthFailure based on IpAddress"""
    defaultHexValue = "00000000"


_VrSnmpMgrOfLastAuthFailure_Object = MibTableColumn
vrSnmpMgrOfLastAuthFailure = _VrSnmpMgrOfLastAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 8, 22, 1, 5),
    _VrSnmpMgrOfLastAuthFailure_Type()
)
vrSnmpMgrOfLastAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpMgrOfLastAuthFailure.setStatus("mandatory")
_VrInitSnmpConfig_ObjectIdentity = ObjectIdentity
vrInitSnmpConfig = _VrInitSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9)
)
_VrInitSnmpConfigRowStatusTable_Object = MibTable
vrInitSnmpConfigRowStatusTable = _VrInitSnmpConfigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1)
)
if mibBuilder.loadTexts:
    vrInitSnmpConfigRowStatusTable.setStatus("obsolete")
_VrInitSnmpConfigRowStatusEntry_Object = MibTableRow
vrInitSnmpConfigRowStatusEntry = _VrInitSnmpConfigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1, 1)
)
vrInitSnmpConfigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrInitSnmpConfigIndex"),
)
if mibBuilder.loadTexts:
    vrInitSnmpConfigRowStatusEntry.setStatus("obsolete")
_VrInitSnmpConfigRowStatus_Type = RowStatus
_VrInitSnmpConfigRowStatus_Object = MibTableColumn
vrInitSnmpConfigRowStatus = _VrInitSnmpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1, 1, 1),
    _VrInitSnmpConfigRowStatus_Type()
)
vrInitSnmpConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrInitSnmpConfigRowStatus.setStatus("obsolete")
_VrInitSnmpConfigComponentName_Type = DisplayString
_VrInitSnmpConfigComponentName_Object = MibTableColumn
vrInitSnmpConfigComponentName = _VrInitSnmpConfigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1, 1, 2),
    _VrInitSnmpConfigComponentName_Type()
)
vrInitSnmpConfigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrInitSnmpConfigComponentName.setStatus("obsolete")
_VrInitSnmpConfigStorageType_Type = StorageType
_VrInitSnmpConfigStorageType_Object = MibTableColumn
vrInitSnmpConfigStorageType = _VrInitSnmpConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1, 1, 4),
    _VrInitSnmpConfigStorageType_Type()
)
vrInitSnmpConfigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrInitSnmpConfigStorageType.setStatus("obsolete")
_VrInitSnmpConfigIndex_Type = NonReplicated
_VrInitSnmpConfigIndex_Object = MibTableColumn
vrInitSnmpConfigIndex = _VrInitSnmpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 1, 1, 10),
    _VrInitSnmpConfigIndex_Type()
)
vrInitSnmpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrInitSnmpConfigIndex.setStatus("obsolete")
_VrInitSnmpConfigProvTable_Object = MibTable
vrInitSnmpConfigProvTable = _VrInitSnmpConfigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 10)
)
if mibBuilder.loadTexts:
    vrInitSnmpConfigProvTable.setStatus("obsolete")
_VrInitSnmpConfigProvEntry_Object = MibTableRow
vrInitSnmpConfigProvEntry = _VrInitSnmpConfigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 10, 1)
)
vrInitSnmpConfigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-BaseSnmpMIB", "vrInitSnmpConfigIndex"),
)
if mibBuilder.loadTexts:
    vrInitSnmpConfigProvEntry.setStatus("obsolete")


class _VrInitSnmpConfigAgentAddress_Type(AsciiString):
    """Custom type vrInitSnmpConfigAgentAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_VrInitSnmpConfigAgentAddress_Type.__name__ = "AsciiString"
_VrInitSnmpConfigAgentAddress_Object = MibTableColumn
vrInitSnmpConfigAgentAddress = _VrInitSnmpConfigAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 10, 1, 1),
    _VrInitSnmpConfigAgentAddress_Type()
)
vrInitSnmpConfigAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrInitSnmpConfigAgentAddress.setStatus("obsolete")


class _VrInitSnmpConfigManagerAddress_Type(AsciiString):
    """Custom type vrInitSnmpConfigManagerAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_VrInitSnmpConfigManagerAddress_Type.__name__ = "AsciiString"
_VrInitSnmpConfigManagerAddress_Object = MibTableColumn
vrInitSnmpConfigManagerAddress = _VrInitSnmpConfigManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 9, 10, 1, 2),
    _VrInitSnmpConfigManagerAddress_Type()
)
vrInitSnmpConfigManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrInitSnmpConfigManagerAddress.setStatus("obsolete")
_BaseSnmpMIB_ObjectIdentity = ObjectIdentity
baseSnmpMIB = _BaseSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36)
)
_BaseSnmpGroup_ObjectIdentity = ObjectIdentity
baseSnmpGroup = _BaseSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 1)
)
_BaseSnmpGroupBD_ObjectIdentity = ObjectIdentity
baseSnmpGroupBD = _BaseSnmpGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 1, 4)
)
_BaseSnmpGroupBD01_ObjectIdentity = ObjectIdentity
baseSnmpGroupBD01 = _BaseSnmpGroupBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 1, 4, 2)
)
_BaseSnmpGroupBD01A_ObjectIdentity = ObjectIdentity
baseSnmpGroupBD01A = _BaseSnmpGroupBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 1, 4, 2, 2)
)
_BaseSnmpCapabilities_ObjectIdentity = ObjectIdentity
baseSnmpCapabilities = _BaseSnmpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 3)
)
_BaseSnmpCapabilitiesBD_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesBD = _BaseSnmpCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 3, 4)
)
_BaseSnmpCapabilitiesBD01_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesBD01 = _BaseSnmpCapabilitiesBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 3, 4, 2)
)
_BaseSnmpCapabilitiesBD01A_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesBD01A = _BaseSnmpCapabilitiesBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 36, 3, 4, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-BaseSnmpMIB",
    **{"vrSnmp": vrSnmp,
       "vrSnmpRowStatusTable": vrSnmpRowStatusTable,
       "vrSnmpRowStatusEntry": vrSnmpRowStatusEntry,
       "vrSnmpRowStatus": vrSnmpRowStatus,
       "vrSnmpComponentName": vrSnmpComponentName,
       "vrSnmpStorageType": vrSnmpStorageType,
       "vrSnmpIndex": vrSnmpIndex,
       "vrSnmpSys": vrSnmpSys,
       "vrSnmpSysRowStatusTable": vrSnmpSysRowStatusTable,
       "vrSnmpSysRowStatusEntry": vrSnmpSysRowStatusEntry,
       "vrSnmpSysRowStatus": vrSnmpSysRowStatus,
       "vrSnmpSysComponentName": vrSnmpSysComponentName,
       "vrSnmpSysStorageType": vrSnmpSysStorageType,
       "vrSnmpSysIndex": vrSnmpSysIndex,
       "vrSnmpSysProvTable": vrSnmpSysProvTable,
       "vrSnmpSysProvEntry": vrSnmpSysProvEntry,
       "vrSnmpSysContact": vrSnmpSysContact,
       "vrSnmpSysName": vrSnmpSysName,
       "vrSnmpSysLocation": vrSnmpSysLocation,
       "vrSnmpSysOpTable": vrSnmpSysOpTable,
       "vrSnmpSysOpEntry": vrSnmpSysOpEntry,
       "vrSnmpSysDescription": vrSnmpSysDescription,
       "vrSnmpSysObjectId": vrSnmpSysObjectId,
       "vrSnmpSysUpTime": vrSnmpSysUpTime,
       "vrSnmpSysServices": vrSnmpSysServices,
       "vrSnmpCom": vrSnmpCom,
       "vrSnmpComRowStatusTable": vrSnmpComRowStatusTable,
       "vrSnmpComRowStatusEntry": vrSnmpComRowStatusEntry,
       "vrSnmpComRowStatus": vrSnmpComRowStatus,
       "vrSnmpComComponentName": vrSnmpComComponentName,
       "vrSnmpComStorageType": vrSnmpComStorageType,
       "vrSnmpComIndex": vrSnmpComIndex,
       "vrSnmpComMan": vrSnmpComMan,
       "vrSnmpComManRowStatusTable": vrSnmpComManRowStatusTable,
       "vrSnmpComManRowStatusEntry": vrSnmpComManRowStatusEntry,
       "vrSnmpComManRowStatus": vrSnmpComManRowStatus,
       "vrSnmpComManComponentName": vrSnmpComManComponentName,
       "vrSnmpComManStorageType": vrSnmpComManStorageType,
       "vrSnmpComManIndex": vrSnmpComManIndex,
       "vrSnmpComManProvTable": vrSnmpComManProvTable,
       "vrSnmpComManProvEntry": vrSnmpComManProvEntry,
       "vrSnmpComManTransportAddress": vrSnmpComManTransportAddress,
       "vrSnmpComManPrivileges": vrSnmpComManPrivileges,
       "vrSnmpComProvTable": vrSnmpComProvTable,
       "vrSnmpComProvEntry": vrSnmpComProvEntry,
       "vrSnmpComCommunityString": vrSnmpComCommunityString,
       "vrSnmpComAccessMode": vrSnmpComAccessMode,
       "vrSnmpComViewIndex": vrSnmpComViewIndex,
       "vrSnmpComTDomain": vrSnmpComTDomain,
       "vrSnmpAcl": vrSnmpAcl,
       "vrSnmpAclRowStatusTable": vrSnmpAclRowStatusTable,
       "vrSnmpAclRowStatusEntry": vrSnmpAclRowStatusEntry,
       "vrSnmpAclRowStatus": vrSnmpAclRowStatus,
       "vrSnmpAclComponentName": vrSnmpAclComponentName,
       "vrSnmpAclStorageType": vrSnmpAclStorageType,
       "vrSnmpAclTargetIndex": vrSnmpAclTargetIndex,
       "vrSnmpAclSubjectIndex": vrSnmpAclSubjectIndex,
       "vrSnmpAclResourcesIndex": vrSnmpAclResourcesIndex,
       "vrSnmpAclProvTable": vrSnmpAclProvTable,
       "vrSnmpAclProvEntry": vrSnmpAclProvEntry,
       "vrSnmpAclPrivileges": vrSnmpAclPrivileges,
       "vrSnmpAclRowStorageType": vrSnmpAclRowStorageType,
       "vrSnmpAclStdRowStatus": vrSnmpAclStdRowStatus,
       "vrSnmpParty": vrSnmpParty,
       "vrSnmpPartyRowStatusTable": vrSnmpPartyRowStatusTable,
       "vrSnmpPartyRowStatusEntry": vrSnmpPartyRowStatusEntry,
       "vrSnmpPartyRowStatus": vrSnmpPartyRowStatus,
       "vrSnmpPartyComponentName": vrSnmpPartyComponentName,
       "vrSnmpPartyStorageType": vrSnmpPartyStorageType,
       "vrSnmpPartyIdentityIndex": vrSnmpPartyIdentityIndex,
       "vrSnmpPartyProvTable": vrSnmpPartyProvTable,
       "vrSnmpPartyProvEntry": vrSnmpPartyProvEntry,
       "vrSnmpPartyStdIndex": vrSnmpPartyStdIndex,
       "vrSnmpPartyTDomain": vrSnmpPartyTDomain,
       "vrSnmpPartyTransportAddress": vrSnmpPartyTransportAddress,
       "vrSnmpPartyMaxMessageSize": vrSnmpPartyMaxMessageSize,
       "vrSnmpPartyLocal": vrSnmpPartyLocal,
       "vrSnmpPartyAuthProtocol": vrSnmpPartyAuthProtocol,
       "vrSnmpPartyAuthPrivate": vrSnmpPartyAuthPrivate,
       "vrSnmpPartyAuthPublic": vrSnmpPartyAuthPublic,
       "vrSnmpPartyAuthLifetime": vrSnmpPartyAuthLifetime,
       "vrSnmpPartyPrivProtocol": vrSnmpPartyPrivProtocol,
       "vrSnmpPartyRowStorageType": vrSnmpPartyRowStorageType,
       "vrSnmpPartyStdRowStatus": vrSnmpPartyStdRowStatus,
       "vrSnmpPartyOpTable": vrSnmpPartyOpTable,
       "vrSnmpPartyOpEntry": vrSnmpPartyOpEntry,
       "vrSnmpPartyTrapNumbers": vrSnmpPartyTrapNumbers,
       "vrSnmpPartyAuthClock": vrSnmpPartyAuthClock,
       "vrSnmpCon": vrSnmpCon,
       "vrSnmpConRowStatusTable": vrSnmpConRowStatusTable,
       "vrSnmpConRowStatusEntry": vrSnmpConRowStatusEntry,
       "vrSnmpConRowStatus": vrSnmpConRowStatus,
       "vrSnmpConComponentName": vrSnmpConComponentName,
       "vrSnmpConStorageType": vrSnmpConStorageType,
       "vrSnmpConIdentityIndex": vrSnmpConIdentityIndex,
       "vrSnmpConProvTable": vrSnmpConProvTable,
       "vrSnmpConProvEntry": vrSnmpConProvEntry,
       "vrSnmpConStdIndex": vrSnmpConStdIndex,
       "vrSnmpConLocal": vrSnmpConLocal,
       "vrSnmpConViewIndex": vrSnmpConViewIndex,
       "vrSnmpConLocalTime": vrSnmpConLocalTime,
       "vrSnmpConRowStorageType": vrSnmpConRowStorageType,
       "vrSnmpConStdRowStatus": vrSnmpConStdRowStatus,
       "vrSnmpView": vrSnmpView,
       "vrSnmpViewRowStatusTable": vrSnmpViewRowStatusTable,
       "vrSnmpViewRowStatusEntry": vrSnmpViewRowStatusEntry,
       "vrSnmpViewRowStatus": vrSnmpViewRowStatus,
       "vrSnmpViewComponentName": vrSnmpViewComponentName,
       "vrSnmpViewStorageType": vrSnmpViewStorageType,
       "vrSnmpViewIndex": vrSnmpViewIndex,
       "vrSnmpViewSubtreeIndex": vrSnmpViewSubtreeIndex,
       "vrSnmpViewProvTable": vrSnmpViewProvTable,
       "vrSnmpViewProvEntry": vrSnmpViewProvEntry,
       "vrSnmpViewMask": vrSnmpViewMask,
       "vrSnmpViewType": vrSnmpViewType,
       "vrSnmpViewRowStorageType": vrSnmpViewRowStorageType,
       "vrSnmpViewStdRowStatus": vrSnmpViewStdRowStatus,
       "vrSnmpOr": vrSnmpOr,
       "vrSnmpOrRowStatusTable": vrSnmpOrRowStatusTable,
       "vrSnmpOrRowStatusEntry": vrSnmpOrRowStatusEntry,
       "vrSnmpOrRowStatus": vrSnmpOrRowStatus,
       "vrSnmpOrComponentName": vrSnmpOrComponentName,
       "vrSnmpOrStorageType": vrSnmpOrStorageType,
       "vrSnmpOrIndex": vrSnmpOrIndex,
       "vrSnmpOrOrTable": vrSnmpOrOrTable,
       "vrSnmpOrOrEntry": vrSnmpOrOrEntry,
       "vrSnmpOrId": vrSnmpOrId,
       "vrSnmpOrDescr": vrSnmpOrDescr,
       "vrSnmpV2Stats": vrSnmpV2Stats,
       "vrSnmpV2StatsRowStatusTable": vrSnmpV2StatsRowStatusTable,
       "vrSnmpV2StatsRowStatusEntry": vrSnmpV2StatsRowStatusEntry,
       "vrSnmpV2StatsRowStatus": vrSnmpV2StatsRowStatus,
       "vrSnmpV2StatsComponentName": vrSnmpV2StatsComponentName,
       "vrSnmpV2StatsStorageType": vrSnmpV2StatsStorageType,
       "vrSnmpV2StatsIndex": vrSnmpV2StatsIndex,
       "vrSnmpV2StatsStatsTable": vrSnmpV2StatsStatsTable,
       "vrSnmpV2StatsStatsEntry": vrSnmpV2StatsStatsEntry,
       "vrSnmpV2StatsPackets": vrSnmpV2StatsPackets,
       "vrSnmpV2StatsEncodingErrors": vrSnmpV2StatsEncodingErrors,
       "vrSnmpV2StatsUnknownSrcParties": vrSnmpV2StatsUnknownSrcParties,
       "vrSnmpV2StatsBadAuths": vrSnmpV2StatsBadAuths,
       "vrSnmpV2StatsNotInLifetime": vrSnmpV2StatsNotInLifetime,
       "vrSnmpV2StatsWrongDigestValues": vrSnmpV2StatsWrongDigestValues,
       "vrSnmpV2StatsUnknownContexts": vrSnmpV2StatsUnknownContexts,
       "vrSnmpV2StatsBadOperations": vrSnmpV2StatsBadOperations,
       "vrSnmpV2StatsSilentDrops": vrSnmpV2StatsSilentDrops,
       "vrSnmpV1Stats": vrSnmpV1Stats,
       "vrSnmpV1StatsRowStatusTable": vrSnmpV1StatsRowStatusTable,
       "vrSnmpV1StatsRowStatusEntry": vrSnmpV1StatsRowStatusEntry,
       "vrSnmpV1StatsRowStatus": vrSnmpV1StatsRowStatus,
       "vrSnmpV1StatsComponentName": vrSnmpV1StatsComponentName,
       "vrSnmpV1StatsStorageType": vrSnmpV1StatsStorageType,
       "vrSnmpV1StatsIndex": vrSnmpV1StatsIndex,
       "vrSnmpV1StatsStatsTable": vrSnmpV1StatsStatsTable,
       "vrSnmpV1StatsStatsEntry": vrSnmpV1StatsStatsEntry,
       "vrSnmpV1StatsBadCommunityNames": vrSnmpV1StatsBadCommunityNames,
       "vrSnmpV1StatsBadCommunityUses": vrSnmpV1StatsBadCommunityUses,
       "vrSnmpMibIIStats": vrSnmpMibIIStats,
       "vrSnmpMibIIStatsRowStatusTable": vrSnmpMibIIStatsRowStatusTable,
       "vrSnmpMibIIStatsRowStatusEntry": vrSnmpMibIIStatsRowStatusEntry,
       "vrSnmpMibIIStatsRowStatus": vrSnmpMibIIStatsRowStatus,
       "vrSnmpMibIIStatsComponentName": vrSnmpMibIIStatsComponentName,
       "vrSnmpMibIIStatsStorageType": vrSnmpMibIIStatsStorageType,
       "vrSnmpMibIIStatsIndex": vrSnmpMibIIStatsIndex,
       "vrSnmpMibIIStatsStatsTable": vrSnmpMibIIStatsStatsTable,
       "vrSnmpMibIIStatsStatsEntry": vrSnmpMibIIStatsStatsEntry,
       "vrSnmpMibIIStatsInPackets": vrSnmpMibIIStatsInPackets,
       "vrSnmpMibIIStatsInBadCommunityNames": vrSnmpMibIIStatsInBadCommunityNames,
       "vrSnmpMibIIStatsInBadCommunityUses": vrSnmpMibIIStatsInBadCommunityUses,
       "vrSnmpMibIIStatsInAsnParseErrs": vrSnmpMibIIStatsInAsnParseErrs,
       "vrSnmpMibIIStatsOutPackets": vrSnmpMibIIStatsOutPackets,
       "vrSnmpMibIIStatsInBadVersions": vrSnmpMibIIStatsInBadVersions,
       "vrSnmpMibIIStatsInTotalReqVars": vrSnmpMibIIStatsInTotalReqVars,
       "vrSnmpMibIIStatsInTotalSetVars": vrSnmpMibIIStatsInTotalSetVars,
       "vrSnmpMibIIStatsInGetRequests": vrSnmpMibIIStatsInGetRequests,
       "vrSnmpMibIIStatsInGetNexts": vrSnmpMibIIStatsInGetNexts,
       "vrSnmpMibIIStatsInSetRequests": vrSnmpMibIIStatsInSetRequests,
       "vrSnmpMibIIStatsOutTooBigs": vrSnmpMibIIStatsOutTooBigs,
       "vrSnmpMibIIStatsOutNoSuchNames": vrSnmpMibIIStatsOutNoSuchNames,
       "vrSnmpMibIIStatsOutBadValues": vrSnmpMibIIStatsOutBadValues,
       "vrSnmpMibIIStatsOutGenErrs": vrSnmpMibIIStatsOutGenErrs,
       "vrSnmpMibIIStatsOutGetResponses": vrSnmpMibIIStatsOutGetResponses,
       "vrSnmpMibIIStatsOutTraps": vrSnmpMibIIStatsOutTraps,
       "vrSnmpProvTable": vrSnmpProvTable,
       "vrSnmpProvEntry": vrSnmpProvEntry,
       "vrSnmpV1EnableAuthenTraps": vrSnmpV1EnableAuthenTraps,
       "vrSnmpV2EnableAuthenTraps": vrSnmpV2EnableAuthenTraps,
       "vrSnmpAlarmsAsTraps": vrSnmpAlarmsAsTraps,
       "vrSnmpIpStack": vrSnmpIpStack,
       "vrSnmpCidInEntTraps": vrSnmpCidInEntTraps,
       "vrSnmpStateTable": vrSnmpStateTable,
       "vrSnmpStateEntry": vrSnmpStateEntry,
       "vrSnmpAdminState": vrSnmpAdminState,
       "vrSnmpOperationalState": vrSnmpOperationalState,
       "vrSnmpUsageState": vrSnmpUsageState,
       "vrSnmpAvailabilityStatus": vrSnmpAvailabilityStatus,
       "vrSnmpProceduralStatus": vrSnmpProceduralStatus,
       "vrSnmpControlStatus": vrSnmpControlStatus,
       "vrSnmpAlarmStatus": vrSnmpAlarmStatus,
       "vrSnmpStandbyStatus": vrSnmpStandbyStatus,
       "vrSnmpUnknownStatus": vrSnmpUnknownStatus,
       "vrSnmpStatsTable": vrSnmpStatsTable,
       "vrSnmpStatsEntry": vrSnmpStatsEntry,
       "vrSnmpLastOrChange": vrSnmpLastOrChange,
       "vrSnmpTrapsProcessed": vrSnmpTrapsProcessed,
       "vrSnmpTrapsDiscarded": vrSnmpTrapsDiscarded,
       "vrSnmpLastAuthFailure": vrSnmpLastAuthFailure,
       "vrSnmpMgrOfLastAuthFailure": vrSnmpMgrOfLastAuthFailure,
       "vrInitSnmpConfig": vrInitSnmpConfig,
       "vrInitSnmpConfigRowStatusTable": vrInitSnmpConfigRowStatusTable,
       "vrInitSnmpConfigRowStatusEntry": vrInitSnmpConfigRowStatusEntry,
       "vrInitSnmpConfigRowStatus": vrInitSnmpConfigRowStatus,
       "vrInitSnmpConfigComponentName": vrInitSnmpConfigComponentName,
       "vrInitSnmpConfigStorageType": vrInitSnmpConfigStorageType,
       "vrInitSnmpConfigIndex": vrInitSnmpConfigIndex,
       "vrInitSnmpConfigProvTable": vrInitSnmpConfigProvTable,
       "vrInitSnmpConfigProvEntry": vrInitSnmpConfigProvEntry,
       "vrInitSnmpConfigAgentAddress": vrInitSnmpConfigAgentAddress,
       "vrInitSnmpConfigManagerAddress": vrInitSnmpConfigManagerAddress,
       "baseSnmpMIB": baseSnmpMIB,
       "baseSnmpGroup": baseSnmpGroup,
       "baseSnmpGroupBD": baseSnmpGroupBD,
       "baseSnmpGroupBD01": baseSnmpGroupBD01,
       "baseSnmpGroupBD01A": baseSnmpGroupBD01A,
       "baseSnmpCapabilities": baseSnmpCapabilities,
       "baseSnmpCapabilitiesBD": baseSnmpCapabilitiesBD,
       "baseSnmpCapabilitiesBD01": baseSnmpCapabilitiesBD01,
       "baseSnmpCapabilitiesBD01A": baseSnmpCapabilitiesBD01A}
)
