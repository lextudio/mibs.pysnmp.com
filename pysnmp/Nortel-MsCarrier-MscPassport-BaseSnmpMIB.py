# SNMP MIB module (Nortel-MsCarrier-MscPassport-BaseSnmpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BaseSnmpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:59 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex")

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

_MscVrSnmp_ObjectIdentity = ObjectIdentity
mscVrSnmp = _MscVrSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8)
)
_MscVrSnmpRowStatusTable_Object = MibTable
mscVrSnmpRowStatusTable = _MscVrSnmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpRowStatusTable.setStatus("mandatory")
_MscVrSnmpRowStatusEntry_Object = MibTableRow
mscVrSnmpRowStatusEntry = _MscVrSnmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1, 1)
)
mscVrSnmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpRowStatusEntry.setStatus("mandatory")
_MscVrSnmpRowStatus_Type = RowStatus
_MscVrSnmpRowStatus_Object = MibTableColumn
mscVrSnmpRowStatus = _MscVrSnmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1, 1, 1),
    _MscVrSnmpRowStatus_Type()
)
mscVrSnmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpRowStatus.setStatus("mandatory")
_MscVrSnmpComponentName_Type = DisplayString
_MscVrSnmpComponentName_Object = MibTableColumn
mscVrSnmpComponentName = _MscVrSnmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1, 1, 2),
    _MscVrSnmpComponentName_Type()
)
mscVrSnmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpComponentName.setStatus("mandatory")
_MscVrSnmpStorageType_Type = StorageType
_MscVrSnmpStorageType_Object = MibTableColumn
mscVrSnmpStorageType = _MscVrSnmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1, 1, 4),
    _MscVrSnmpStorageType_Type()
)
mscVrSnmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpStorageType.setStatus("mandatory")
_MscVrSnmpIndex_Type = NonReplicated
_MscVrSnmpIndex_Object = MibTableColumn
mscVrSnmpIndex = _MscVrSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 1, 1, 10),
    _MscVrSnmpIndex_Type()
)
mscVrSnmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpIndex.setStatus("mandatory")
_MscVrSnmpSys_ObjectIdentity = ObjectIdentity
mscVrSnmpSys = _MscVrSnmpSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2)
)
_MscVrSnmpSysRowStatusTable_Object = MibTable
mscVrSnmpSysRowStatusTable = _MscVrSnmpSysRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpSysRowStatusTable.setStatus("mandatory")
_MscVrSnmpSysRowStatusEntry_Object = MibTableRow
mscVrSnmpSysRowStatusEntry = _MscVrSnmpSysRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1, 1)
)
mscVrSnmpSysRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpSysRowStatusEntry.setStatus("mandatory")
_MscVrSnmpSysRowStatus_Type = RowStatus
_MscVrSnmpSysRowStatus_Object = MibTableColumn
mscVrSnmpSysRowStatus = _MscVrSnmpSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1, 1, 1),
    _MscVrSnmpSysRowStatus_Type()
)
mscVrSnmpSysRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysRowStatus.setStatus("mandatory")
_MscVrSnmpSysComponentName_Type = DisplayString
_MscVrSnmpSysComponentName_Object = MibTableColumn
mscVrSnmpSysComponentName = _MscVrSnmpSysComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1, 1, 2),
    _MscVrSnmpSysComponentName_Type()
)
mscVrSnmpSysComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysComponentName.setStatus("mandatory")
_MscVrSnmpSysStorageType_Type = StorageType
_MscVrSnmpSysStorageType_Object = MibTableColumn
mscVrSnmpSysStorageType = _MscVrSnmpSysStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1, 1, 4),
    _MscVrSnmpSysStorageType_Type()
)
mscVrSnmpSysStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysStorageType.setStatus("mandatory")
_MscVrSnmpSysIndex_Type = NonReplicated
_MscVrSnmpSysIndex_Object = MibTableColumn
mscVrSnmpSysIndex = _MscVrSnmpSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 1, 1, 10),
    _MscVrSnmpSysIndex_Type()
)
mscVrSnmpSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpSysIndex.setStatus("mandatory")
_MscVrSnmpSysProvTable_Object = MibTable
mscVrSnmpSysProvTable = _MscVrSnmpSysProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpSysProvTable.setStatus("mandatory")
_MscVrSnmpSysProvEntry_Object = MibTableRow
mscVrSnmpSysProvEntry = _MscVrSnmpSysProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 10, 1)
)
mscVrSnmpSysProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpSysProvEntry.setStatus("mandatory")


class _MscVrSnmpSysContact_Type(AsciiString):
    """Custom type mscVrSnmpSysContact based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrSnmpSysContact_Type.__name__ = "AsciiString"
_MscVrSnmpSysContact_Object = MibTableColumn
mscVrSnmpSysContact = _MscVrSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 10, 1, 1),
    _MscVrSnmpSysContact_Type()
)
mscVrSnmpSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpSysContact.setStatus("mandatory")


class _MscVrSnmpSysName_Type(AsciiString):
    """Custom type mscVrSnmpSysName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrSnmpSysName_Type.__name__ = "AsciiString"
_MscVrSnmpSysName_Object = MibTableColumn
mscVrSnmpSysName = _MscVrSnmpSysName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 10, 1, 2),
    _MscVrSnmpSysName_Type()
)
mscVrSnmpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpSysName.setStatus("mandatory")


class _MscVrSnmpSysLocation_Type(AsciiString):
    """Custom type mscVrSnmpSysLocation based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrSnmpSysLocation_Type.__name__ = "AsciiString"
_MscVrSnmpSysLocation_Object = MibTableColumn
mscVrSnmpSysLocation = _MscVrSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 10, 1, 3),
    _MscVrSnmpSysLocation_Type()
)
mscVrSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpSysLocation.setStatus("mandatory")
_MscVrSnmpSysOpTable_Object = MibTable
mscVrSnmpSysOpTable = _MscVrSnmpSysOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrSnmpSysOpTable.setStatus("mandatory")
_MscVrSnmpSysOpEntry_Object = MibTableRow
mscVrSnmpSysOpEntry = _MscVrSnmpSysOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11, 1)
)
mscVrSnmpSysOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpSysIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpSysOpEntry.setStatus("mandatory")


class _MscVrSnmpSysDescription_Type(AsciiString):
    """Custom type mscVrSnmpSysDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrSnmpSysDescription_Type.__name__ = "AsciiString"
_MscVrSnmpSysDescription_Object = MibTableColumn
mscVrSnmpSysDescription = _MscVrSnmpSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11, 1, 1),
    _MscVrSnmpSysDescription_Type()
)
mscVrSnmpSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysDescription.setStatus("mandatory")
_MscVrSnmpSysObjectId_Type = ObjectIdentifier
_MscVrSnmpSysObjectId_Object = MibTableColumn
mscVrSnmpSysObjectId = _MscVrSnmpSysObjectId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11, 1, 2),
    _MscVrSnmpSysObjectId_Type()
)
mscVrSnmpSysObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysObjectId.setStatus("mandatory")


class _MscVrSnmpSysUpTime_Type(Unsigned32):
    """Custom type mscVrSnmpSysUpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpSysUpTime_Type.__name__ = "Unsigned32"
_MscVrSnmpSysUpTime_Object = MibTableColumn
mscVrSnmpSysUpTime = _MscVrSnmpSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11, 1, 3),
    _MscVrSnmpSysUpTime_Type()
)
mscVrSnmpSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysUpTime.setStatus("mandatory")


class _MscVrSnmpSysServices_Type(Unsigned32):
    """Custom type mscVrSnmpSysServices based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscVrSnmpSysServices_Type.__name__ = "Unsigned32"
_MscVrSnmpSysServices_Object = MibTableColumn
mscVrSnmpSysServices = _MscVrSnmpSysServices_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 2, 11, 1, 4),
    _MscVrSnmpSysServices_Type()
)
mscVrSnmpSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpSysServices.setStatus("mandatory")
_MscVrSnmpCom_ObjectIdentity = ObjectIdentity
mscVrSnmpCom = _MscVrSnmpCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3)
)
_MscVrSnmpComRowStatusTable_Object = MibTable
mscVrSnmpComRowStatusTable = _MscVrSnmpComRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpComRowStatusTable.setStatus("mandatory")
_MscVrSnmpComRowStatusEntry_Object = MibTableRow
mscVrSnmpComRowStatusEntry = _MscVrSnmpComRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1, 1)
)
mscVrSnmpComRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpComRowStatusEntry.setStatus("mandatory")
_MscVrSnmpComRowStatus_Type = RowStatus
_MscVrSnmpComRowStatus_Object = MibTableColumn
mscVrSnmpComRowStatus = _MscVrSnmpComRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1, 1, 1),
    _MscVrSnmpComRowStatus_Type()
)
mscVrSnmpComRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComRowStatus.setStatus("mandatory")
_MscVrSnmpComComponentName_Type = DisplayString
_MscVrSnmpComComponentName_Object = MibTableColumn
mscVrSnmpComComponentName = _MscVrSnmpComComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1, 1, 2),
    _MscVrSnmpComComponentName_Type()
)
mscVrSnmpComComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpComComponentName.setStatus("mandatory")
_MscVrSnmpComStorageType_Type = StorageType
_MscVrSnmpComStorageType_Object = MibTableColumn
mscVrSnmpComStorageType = _MscVrSnmpComStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1, 1, 4),
    _MscVrSnmpComStorageType_Type()
)
mscVrSnmpComStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpComStorageType.setStatus("mandatory")


class _MscVrSnmpComIndex_Type(Integer32):
    """Custom type mscVrSnmpComIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpComIndex_Type.__name__ = "Integer32"
_MscVrSnmpComIndex_Object = MibTableColumn
mscVrSnmpComIndex = _MscVrSnmpComIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 1, 1, 10),
    _MscVrSnmpComIndex_Type()
)
mscVrSnmpComIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpComIndex.setStatus("mandatory")
_MscVrSnmpComMan_ObjectIdentity = ObjectIdentity
mscVrSnmpComMan = _MscVrSnmpComMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2)
)
_MscVrSnmpComManRowStatusTable_Object = MibTable
mscVrSnmpComManRowStatusTable = _MscVrSnmpComManRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpComManRowStatusTable.setStatus("mandatory")
_MscVrSnmpComManRowStatusEntry_Object = MibTableRow
mscVrSnmpComManRowStatusEntry = _MscVrSnmpComManRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1, 1)
)
mscVrSnmpComManRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComManIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpComManRowStatusEntry.setStatus("mandatory")
_MscVrSnmpComManRowStatus_Type = RowStatus
_MscVrSnmpComManRowStatus_Object = MibTableColumn
mscVrSnmpComManRowStatus = _MscVrSnmpComManRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1, 1, 1),
    _MscVrSnmpComManRowStatus_Type()
)
mscVrSnmpComManRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComManRowStatus.setStatus("mandatory")
_MscVrSnmpComManComponentName_Type = DisplayString
_MscVrSnmpComManComponentName_Object = MibTableColumn
mscVrSnmpComManComponentName = _MscVrSnmpComManComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1, 1, 2),
    _MscVrSnmpComManComponentName_Type()
)
mscVrSnmpComManComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpComManComponentName.setStatus("mandatory")
_MscVrSnmpComManStorageType_Type = StorageType
_MscVrSnmpComManStorageType_Object = MibTableColumn
mscVrSnmpComManStorageType = _MscVrSnmpComManStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1, 1, 4),
    _MscVrSnmpComManStorageType_Type()
)
mscVrSnmpComManStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpComManStorageType.setStatus("mandatory")


class _MscVrSnmpComManIndex_Type(Integer32):
    """Custom type mscVrSnmpComManIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrSnmpComManIndex_Type.__name__ = "Integer32"
_MscVrSnmpComManIndex_Object = MibTableColumn
mscVrSnmpComManIndex = _MscVrSnmpComManIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 1, 1, 10),
    _MscVrSnmpComManIndex_Type()
)
mscVrSnmpComManIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpComManIndex.setStatus("mandatory")
_MscVrSnmpComManProvTable_Object = MibTable
mscVrSnmpComManProvTable = _MscVrSnmpComManProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpComManProvTable.setStatus("mandatory")
_MscVrSnmpComManProvEntry_Object = MibTableRow
mscVrSnmpComManProvEntry = _MscVrSnmpComManProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 10, 1)
)
mscVrSnmpComManProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComManIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpComManProvEntry.setStatus("mandatory")


class _MscVrSnmpComManTransportAddress_Type(AsciiString):
    """Custom type mscVrSnmpComManTransportAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_MscVrSnmpComManTransportAddress_Type.__name__ = "AsciiString"
_MscVrSnmpComManTransportAddress_Object = MibTableColumn
mscVrSnmpComManTransportAddress = _MscVrSnmpComManTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 10, 1, 1),
    _MscVrSnmpComManTransportAddress_Type()
)
mscVrSnmpComManTransportAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComManTransportAddress.setStatus("mandatory")


class _MscVrSnmpComManPrivileges_Type(OctetString):
    """Custom type mscVrSnmpComManPrivileges based on OctetString"""
    defaultHexValue = "40"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrSnmpComManPrivileges_Type.__name__ = "OctetString"
_MscVrSnmpComManPrivileges_Object = MibTableColumn
mscVrSnmpComManPrivileges = _MscVrSnmpComManPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 2, 10, 1, 2),
    _MscVrSnmpComManPrivileges_Type()
)
mscVrSnmpComManPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComManPrivileges.setStatus("mandatory")
_MscVrSnmpComProvTable_Object = MibTable
mscVrSnmpComProvTable = _MscVrSnmpComProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpComProvTable.setStatus("mandatory")
_MscVrSnmpComProvEntry_Object = MibTableRow
mscVrSnmpComProvEntry = _MscVrSnmpComProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10, 1)
)
mscVrSnmpComProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpComIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpComProvEntry.setStatus("mandatory")


class _MscVrSnmpComCommunityString_Type(AsciiString):
    """Custom type mscVrSnmpComCommunityString based on AsciiString"""
    defaultHexValue = "7075626c6963"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MscVrSnmpComCommunityString_Type.__name__ = "AsciiString"
_MscVrSnmpComCommunityString_Object = MibTableColumn
mscVrSnmpComCommunityString = _MscVrSnmpComCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10, 1, 1),
    _MscVrSnmpComCommunityString_Type()
)
mscVrSnmpComCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComCommunityString.setStatus("mandatory")


class _MscVrSnmpComAccessMode_Type(Integer32):
    """Custom type mscVrSnmpComAccessMode based on Integer32"""
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


_MscVrSnmpComAccessMode_Type.__name__ = "Integer32"
_MscVrSnmpComAccessMode_Object = MibTableColumn
mscVrSnmpComAccessMode = _MscVrSnmpComAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10, 1, 3),
    _MscVrSnmpComAccessMode_Type()
)
mscVrSnmpComAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComAccessMode.setStatus("mandatory")


class _MscVrSnmpComViewIndex_Type(Unsigned32):
    """Custom type mscVrSnmpComViewIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpComViewIndex_Type.__name__ = "Unsigned32"
_MscVrSnmpComViewIndex_Object = MibTableColumn
mscVrSnmpComViewIndex = _MscVrSnmpComViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10, 1, 4),
    _MscVrSnmpComViewIndex_Type()
)
mscVrSnmpComViewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComViewIndex.setStatus("mandatory")


class _MscVrSnmpComTDomain_Type(Integer32):
    """Custom type mscVrSnmpComTDomain based on Integer32"""
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


_MscVrSnmpComTDomain_Type.__name__ = "Integer32"
_MscVrSnmpComTDomain_Object = MibTableColumn
mscVrSnmpComTDomain = _MscVrSnmpComTDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 3, 10, 1, 5),
    _MscVrSnmpComTDomain_Type()
)
mscVrSnmpComTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpComTDomain.setStatus("mandatory")
_MscVrSnmpAcl_ObjectIdentity = ObjectIdentity
mscVrSnmpAcl = _MscVrSnmpAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4)
)
_MscVrSnmpAclRowStatusTable_Object = MibTable
mscVrSnmpAclRowStatusTable = _MscVrSnmpAclRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpAclRowStatusTable.setStatus("obsolete")
_MscVrSnmpAclRowStatusEntry_Object = MibTableRow
mscVrSnmpAclRowStatusEntry = _MscVrSnmpAclRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1)
)
mscVrSnmpAclRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclTargetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclSubjectIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclResourcesIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpAclRowStatusEntry.setStatus("obsolete")
_MscVrSnmpAclRowStatus_Type = RowStatus
_MscVrSnmpAclRowStatus_Object = MibTableColumn
mscVrSnmpAclRowStatus = _MscVrSnmpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 1),
    _MscVrSnmpAclRowStatus_Type()
)
mscVrSnmpAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAclRowStatus.setStatus("obsolete")
_MscVrSnmpAclComponentName_Type = DisplayString
_MscVrSnmpAclComponentName_Object = MibTableColumn
mscVrSnmpAclComponentName = _MscVrSnmpAclComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 2),
    _MscVrSnmpAclComponentName_Type()
)
mscVrSnmpAclComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpAclComponentName.setStatus("obsolete")
_MscVrSnmpAclStorageType_Type = StorageType
_MscVrSnmpAclStorageType_Object = MibTableColumn
mscVrSnmpAclStorageType = _MscVrSnmpAclStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 4),
    _MscVrSnmpAclStorageType_Type()
)
mscVrSnmpAclStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpAclStorageType.setStatus("obsolete")


class _MscVrSnmpAclTargetIndex_Type(Integer32):
    """Custom type mscVrSnmpAclTargetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MscVrSnmpAclTargetIndex_Type.__name__ = "Integer32"
_MscVrSnmpAclTargetIndex_Object = MibTableColumn
mscVrSnmpAclTargetIndex = _MscVrSnmpAclTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 10),
    _MscVrSnmpAclTargetIndex_Type()
)
mscVrSnmpAclTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpAclTargetIndex.setStatus("obsolete")


class _MscVrSnmpAclSubjectIndex_Type(Integer32):
    """Custom type mscVrSnmpAclSubjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MscVrSnmpAclSubjectIndex_Type.__name__ = "Integer32"
_MscVrSnmpAclSubjectIndex_Object = MibTableColumn
mscVrSnmpAclSubjectIndex = _MscVrSnmpAclSubjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 11),
    _MscVrSnmpAclSubjectIndex_Type()
)
mscVrSnmpAclSubjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpAclSubjectIndex.setStatus("obsolete")


class _MscVrSnmpAclResourcesIndex_Type(Integer32):
    """Custom type mscVrSnmpAclResourcesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MscVrSnmpAclResourcesIndex_Type.__name__ = "Integer32"
_MscVrSnmpAclResourcesIndex_Object = MibTableColumn
mscVrSnmpAclResourcesIndex = _MscVrSnmpAclResourcesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 1, 1, 12),
    _MscVrSnmpAclResourcesIndex_Type()
)
mscVrSnmpAclResourcesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpAclResourcesIndex.setStatus("obsolete")
_MscVrSnmpAclProvTable_Object = MibTable
mscVrSnmpAclProvTable = _MscVrSnmpAclProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpAclProvTable.setStatus("obsolete")
_MscVrSnmpAclProvEntry_Object = MibTableRow
mscVrSnmpAclProvEntry = _MscVrSnmpAclProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 10, 1)
)
mscVrSnmpAclProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclTargetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclSubjectIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpAclResourcesIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpAclProvEntry.setStatus("obsolete")


class _MscVrSnmpAclPrivileges_Type(OctetString):
    """Custom type mscVrSnmpAclPrivileges based on OctetString"""
    defaultHexValue = "60"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrSnmpAclPrivileges_Type.__name__ = "OctetString"
_MscVrSnmpAclPrivileges_Object = MibTableColumn
mscVrSnmpAclPrivileges = _MscVrSnmpAclPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 10, 1, 1),
    _MscVrSnmpAclPrivileges_Type()
)
mscVrSnmpAclPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAclPrivileges.setStatus("obsolete")


class _MscVrSnmpAclRowStorageType_Type(Integer32):
    """Custom type mscVrSnmpAclRowStorageType based on Integer32"""
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


_MscVrSnmpAclRowStorageType_Type.__name__ = "Integer32"
_MscVrSnmpAclRowStorageType_Object = MibTableColumn
mscVrSnmpAclRowStorageType = _MscVrSnmpAclRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 10, 1, 2),
    _MscVrSnmpAclRowStorageType_Type()
)
mscVrSnmpAclRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAclRowStorageType.setStatus("obsolete")


class _MscVrSnmpAclStdRowStatus_Type(Integer32):
    """Custom type mscVrSnmpAclStdRowStatus based on Integer32"""
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


_MscVrSnmpAclStdRowStatus_Type.__name__ = "Integer32"
_MscVrSnmpAclStdRowStatus_Object = MibTableColumn
mscVrSnmpAclStdRowStatus = _MscVrSnmpAclStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 4, 10, 1, 3),
    _MscVrSnmpAclStdRowStatus_Type()
)
mscVrSnmpAclStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAclStdRowStatus.setStatus("obsolete")
_MscVrSnmpParty_ObjectIdentity = ObjectIdentity
mscVrSnmpParty = _MscVrSnmpParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5)
)
_MscVrSnmpPartyRowStatusTable_Object = MibTable
mscVrSnmpPartyRowStatusTable = _MscVrSnmpPartyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyRowStatusTable.setStatus("obsolete")
_MscVrSnmpPartyRowStatusEntry_Object = MibTableRow
mscVrSnmpPartyRowStatusEntry = _MscVrSnmpPartyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1, 1)
)
mscVrSnmpPartyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyRowStatusEntry.setStatus("obsolete")
_MscVrSnmpPartyRowStatus_Type = RowStatus
_MscVrSnmpPartyRowStatus_Object = MibTableColumn
mscVrSnmpPartyRowStatus = _MscVrSnmpPartyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1, 1, 1),
    _MscVrSnmpPartyRowStatus_Type()
)
mscVrSnmpPartyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyRowStatus.setStatus("obsolete")
_MscVrSnmpPartyComponentName_Type = DisplayString
_MscVrSnmpPartyComponentName_Object = MibTableColumn
mscVrSnmpPartyComponentName = _MscVrSnmpPartyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1, 1, 2),
    _MscVrSnmpPartyComponentName_Type()
)
mscVrSnmpPartyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpPartyComponentName.setStatus("obsolete")
_MscVrSnmpPartyStorageType_Type = StorageType
_MscVrSnmpPartyStorageType_Object = MibTableColumn
mscVrSnmpPartyStorageType = _MscVrSnmpPartyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1, 1, 4),
    _MscVrSnmpPartyStorageType_Type()
)
mscVrSnmpPartyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpPartyStorageType.setStatus("obsolete")
_MscVrSnmpPartyIdentityIndex_Type = ObjectIdentifier
_MscVrSnmpPartyIdentityIndex_Object = MibTableColumn
mscVrSnmpPartyIdentityIndex = _MscVrSnmpPartyIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 1, 1, 10),
    _MscVrSnmpPartyIdentityIndex_Type()
)
mscVrSnmpPartyIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpPartyIdentityIndex.setStatus("obsolete")
_MscVrSnmpPartyProvTable_Object = MibTable
mscVrSnmpPartyProvTable = _MscVrSnmpPartyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyProvTable.setStatus("obsolete")
_MscVrSnmpPartyProvEntry_Object = MibTableRow
mscVrSnmpPartyProvEntry = _MscVrSnmpPartyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1)
)
mscVrSnmpPartyProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyProvEntry.setStatus("obsolete")


class _MscVrSnmpPartyStdIndex_Type(Unsigned32):
    """Custom type mscVrSnmpPartyStdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_MscVrSnmpPartyStdIndex_Type.__name__ = "Unsigned32"
_MscVrSnmpPartyStdIndex_Object = MibTableColumn
mscVrSnmpPartyStdIndex = _MscVrSnmpPartyStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 1),
    _MscVrSnmpPartyStdIndex_Type()
)
mscVrSnmpPartyStdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpPartyStdIndex.setStatus("obsolete")


class _MscVrSnmpPartyTDomain_Type(Integer32):
    """Custom type mscVrSnmpPartyTDomain based on Integer32"""
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


_MscVrSnmpPartyTDomain_Type.__name__ = "Integer32"
_MscVrSnmpPartyTDomain_Object = MibTableColumn
mscVrSnmpPartyTDomain = _MscVrSnmpPartyTDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 2),
    _MscVrSnmpPartyTDomain_Type()
)
mscVrSnmpPartyTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyTDomain.setStatus("obsolete")


class _MscVrSnmpPartyTransportAddress_Type(AsciiString):
    """Custom type mscVrSnmpPartyTransportAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_MscVrSnmpPartyTransportAddress_Type.__name__ = "AsciiString"
_MscVrSnmpPartyTransportAddress_Object = MibTableColumn
mscVrSnmpPartyTransportAddress = _MscVrSnmpPartyTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 3),
    _MscVrSnmpPartyTransportAddress_Type()
)
mscVrSnmpPartyTransportAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyTransportAddress.setStatus("obsolete")


class _MscVrSnmpPartyMaxMessageSize_Type(Unsigned32):
    """Custom type mscVrSnmpPartyMaxMessageSize based on Unsigned32"""
    defaultValue = 1400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65507),
    )


_MscVrSnmpPartyMaxMessageSize_Type.__name__ = "Unsigned32"
_MscVrSnmpPartyMaxMessageSize_Object = MibTableColumn
mscVrSnmpPartyMaxMessageSize = _MscVrSnmpPartyMaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 4),
    _MscVrSnmpPartyMaxMessageSize_Type()
)
mscVrSnmpPartyMaxMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyMaxMessageSize.setStatus("obsolete")
_MscVrSnmpPartyLocal_Type = TruthValue
_MscVrSnmpPartyLocal_Object = MibTableColumn
mscVrSnmpPartyLocal = _MscVrSnmpPartyLocal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 5),
    _MscVrSnmpPartyLocal_Type()
)
mscVrSnmpPartyLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyLocal.setStatus("obsolete")


class _MscVrSnmpPartyAuthProtocol_Type(Integer32):
    """Custom type mscVrSnmpPartyAuthProtocol based on Integer32"""
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


_MscVrSnmpPartyAuthProtocol_Type.__name__ = "Integer32"
_MscVrSnmpPartyAuthProtocol_Object = MibTableColumn
mscVrSnmpPartyAuthProtocol = _MscVrSnmpPartyAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 6),
    _MscVrSnmpPartyAuthProtocol_Type()
)
mscVrSnmpPartyAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyAuthProtocol.setStatus("obsolete")


class _MscVrSnmpPartyAuthPrivate_Type(HexString):
    """Custom type mscVrSnmpPartyAuthPrivate based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscVrSnmpPartyAuthPrivate_Type.__name__ = "HexString"
_MscVrSnmpPartyAuthPrivate_Object = MibTableColumn
mscVrSnmpPartyAuthPrivate = _MscVrSnmpPartyAuthPrivate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 7),
    _MscVrSnmpPartyAuthPrivate_Type()
)
mscVrSnmpPartyAuthPrivate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrSnmpPartyAuthPrivate.setStatus("obsolete")


class _MscVrSnmpPartyAuthPublic_Type(HexString):
    """Custom type mscVrSnmpPartyAuthPublic based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscVrSnmpPartyAuthPublic_Type.__name__ = "HexString"
_MscVrSnmpPartyAuthPublic_Object = MibTableColumn
mscVrSnmpPartyAuthPublic = _MscVrSnmpPartyAuthPublic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 8),
    _MscVrSnmpPartyAuthPublic_Type()
)
mscVrSnmpPartyAuthPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyAuthPublic.setStatus("obsolete")


class _MscVrSnmpPartyAuthLifetime_Type(Unsigned32):
    """Custom type mscVrSnmpPartyAuthLifetime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscVrSnmpPartyAuthLifetime_Type.__name__ = "Unsigned32"
_MscVrSnmpPartyAuthLifetime_Object = MibTableColumn
mscVrSnmpPartyAuthLifetime = _MscVrSnmpPartyAuthLifetime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 9),
    _MscVrSnmpPartyAuthLifetime_Type()
)
mscVrSnmpPartyAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyAuthLifetime.setStatus("obsolete")


class _MscVrSnmpPartyPrivProtocol_Type(Integer32):
    """Custom type mscVrSnmpPartyPrivProtocol based on Integer32"""
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


_MscVrSnmpPartyPrivProtocol_Type.__name__ = "Integer32"
_MscVrSnmpPartyPrivProtocol_Object = MibTableColumn
mscVrSnmpPartyPrivProtocol = _MscVrSnmpPartyPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 10),
    _MscVrSnmpPartyPrivProtocol_Type()
)
mscVrSnmpPartyPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyPrivProtocol.setStatus("obsolete")


class _MscVrSnmpPartyRowStorageType_Type(Integer32):
    """Custom type mscVrSnmpPartyRowStorageType based on Integer32"""
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


_MscVrSnmpPartyRowStorageType_Type.__name__ = "Integer32"
_MscVrSnmpPartyRowStorageType_Object = MibTableColumn
mscVrSnmpPartyRowStorageType = _MscVrSnmpPartyRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 11),
    _MscVrSnmpPartyRowStorageType_Type()
)
mscVrSnmpPartyRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyRowStorageType.setStatus("obsolete")


class _MscVrSnmpPartyStdRowStatus_Type(Integer32):
    """Custom type mscVrSnmpPartyStdRowStatus based on Integer32"""
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


_MscVrSnmpPartyStdRowStatus_Type.__name__ = "Integer32"
_MscVrSnmpPartyStdRowStatus_Object = MibTableColumn
mscVrSnmpPartyStdRowStatus = _MscVrSnmpPartyStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 10, 1, 12),
    _MscVrSnmpPartyStdRowStatus_Type()
)
mscVrSnmpPartyStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyStdRowStatus.setStatus("obsolete")
_MscVrSnmpPartyOpTable_Object = MibTable
mscVrSnmpPartyOpTable = _MscVrSnmpPartyOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 11)
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyOpTable.setStatus("obsolete")
_MscVrSnmpPartyOpEntry_Object = MibTableRow
mscVrSnmpPartyOpEntry = _MscVrSnmpPartyOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 11, 1)
)
mscVrSnmpPartyOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpPartyIdentityIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpPartyOpEntry.setStatus("obsolete")


class _MscVrSnmpPartyTrapNumbers_Type(Unsigned32):
    """Custom type mscVrSnmpPartyTrapNumbers based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpPartyTrapNumbers_Type.__name__ = "Unsigned32"
_MscVrSnmpPartyTrapNumbers_Object = MibTableColumn
mscVrSnmpPartyTrapNumbers = _MscVrSnmpPartyTrapNumbers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 11, 1, 1),
    _MscVrSnmpPartyTrapNumbers_Type()
)
mscVrSnmpPartyTrapNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpPartyTrapNumbers.setStatus("obsolete")


class _MscVrSnmpPartyAuthClock_Type(Unsigned32):
    """Custom type mscVrSnmpPartyAuthClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpPartyAuthClock_Type.__name__ = "Unsigned32"
_MscVrSnmpPartyAuthClock_Object = MibTableColumn
mscVrSnmpPartyAuthClock = _MscVrSnmpPartyAuthClock_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 5, 11, 1, 2),
    _MscVrSnmpPartyAuthClock_Type()
)
mscVrSnmpPartyAuthClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpPartyAuthClock.setStatus("obsolete")
_MscVrSnmpCon_ObjectIdentity = ObjectIdentity
mscVrSnmpCon = _MscVrSnmpCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6)
)
_MscVrSnmpConRowStatusTable_Object = MibTable
mscVrSnmpConRowStatusTable = _MscVrSnmpConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpConRowStatusTable.setStatus("obsolete")
_MscVrSnmpConRowStatusEntry_Object = MibTableRow
mscVrSnmpConRowStatusEntry = _MscVrSnmpConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1, 1)
)
mscVrSnmpConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpConIdentityIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpConRowStatusEntry.setStatus("obsolete")
_MscVrSnmpConRowStatus_Type = RowStatus
_MscVrSnmpConRowStatus_Object = MibTableColumn
mscVrSnmpConRowStatus = _MscVrSnmpConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1, 1, 1),
    _MscVrSnmpConRowStatus_Type()
)
mscVrSnmpConRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConRowStatus.setStatus("obsolete")
_MscVrSnmpConComponentName_Type = DisplayString
_MscVrSnmpConComponentName_Object = MibTableColumn
mscVrSnmpConComponentName = _MscVrSnmpConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1, 1, 2),
    _MscVrSnmpConComponentName_Type()
)
mscVrSnmpConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpConComponentName.setStatus("obsolete")
_MscVrSnmpConStorageType_Type = StorageType
_MscVrSnmpConStorageType_Object = MibTableColumn
mscVrSnmpConStorageType = _MscVrSnmpConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1, 1, 4),
    _MscVrSnmpConStorageType_Type()
)
mscVrSnmpConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpConStorageType.setStatus("obsolete")
_MscVrSnmpConIdentityIndex_Type = ObjectIdentifier
_MscVrSnmpConIdentityIndex_Object = MibTableColumn
mscVrSnmpConIdentityIndex = _MscVrSnmpConIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 1, 1, 10),
    _MscVrSnmpConIdentityIndex_Type()
)
mscVrSnmpConIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpConIdentityIndex.setStatus("obsolete")
_MscVrSnmpConProvTable_Object = MibTable
mscVrSnmpConProvTable = _MscVrSnmpConProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpConProvTable.setStatus("obsolete")
_MscVrSnmpConProvEntry_Object = MibTableRow
mscVrSnmpConProvEntry = _MscVrSnmpConProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1)
)
mscVrSnmpConProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpConIdentityIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpConProvEntry.setStatus("obsolete")


class _MscVrSnmpConStdIndex_Type(Unsigned32):
    """Custom type mscVrSnmpConStdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpConStdIndex_Type.__name__ = "Unsigned32"
_MscVrSnmpConStdIndex_Object = MibTableColumn
mscVrSnmpConStdIndex = _MscVrSnmpConStdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 1),
    _MscVrSnmpConStdIndex_Type()
)
mscVrSnmpConStdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpConStdIndex.setStatus("obsolete")


class _MscVrSnmpConLocal_Type(Integer32):
    """Custom type mscVrSnmpConLocal based on Integer32"""
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


_MscVrSnmpConLocal_Type.__name__ = "Integer32"
_MscVrSnmpConLocal_Object = MibTableColumn
mscVrSnmpConLocal = _MscVrSnmpConLocal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 2),
    _MscVrSnmpConLocal_Type()
)
mscVrSnmpConLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConLocal.setStatus("obsolete")


class _MscVrSnmpConViewIndex_Type(Unsigned32):
    """Custom type mscVrSnmpConViewIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpConViewIndex_Type.__name__ = "Unsigned32"
_MscVrSnmpConViewIndex_Object = MibTableColumn
mscVrSnmpConViewIndex = _MscVrSnmpConViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 3),
    _MscVrSnmpConViewIndex_Type()
)
mscVrSnmpConViewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConViewIndex.setStatus("obsolete")


class _MscVrSnmpConLocalTime_Type(Integer32):
    """Custom type mscVrSnmpConLocalTime based on Integer32"""
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


_MscVrSnmpConLocalTime_Type.__name__ = "Integer32"
_MscVrSnmpConLocalTime_Object = MibTableColumn
mscVrSnmpConLocalTime = _MscVrSnmpConLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 4),
    _MscVrSnmpConLocalTime_Type()
)
mscVrSnmpConLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConLocalTime.setStatus("obsolete")


class _MscVrSnmpConRowStorageType_Type(Integer32):
    """Custom type mscVrSnmpConRowStorageType based on Integer32"""
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


_MscVrSnmpConRowStorageType_Type.__name__ = "Integer32"
_MscVrSnmpConRowStorageType_Object = MibTableColumn
mscVrSnmpConRowStorageType = _MscVrSnmpConRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 5),
    _MscVrSnmpConRowStorageType_Type()
)
mscVrSnmpConRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConRowStorageType.setStatus("obsolete")


class _MscVrSnmpConStdRowStatus_Type(Integer32):
    """Custom type mscVrSnmpConStdRowStatus based on Integer32"""
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


_MscVrSnmpConStdRowStatus_Type.__name__ = "Integer32"
_MscVrSnmpConStdRowStatus_Object = MibTableColumn
mscVrSnmpConStdRowStatus = _MscVrSnmpConStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 6, 10, 1, 6),
    _MscVrSnmpConStdRowStatus_Type()
)
mscVrSnmpConStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpConStdRowStatus.setStatus("obsolete")
_MscVrSnmpView_ObjectIdentity = ObjectIdentity
mscVrSnmpView = _MscVrSnmpView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7)
)
_MscVrSnmpViewRowStatusTable_Object = MibTable
mscVrSnmpViewRowStatusTable = _MscVrSnmpViewRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpViewRowStatusTable.setStatus("mandatory")
_MscVrSnmpViewRowStatusEntry_Object = MibTableRow
mscVrSnmpViewRowStatusEntry = _MscVrSnmpViewRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1)
)
mscVrSnmpViewRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpViewIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpViewSubtreeIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpViewRowStatusEntry.setStatus("mandatory")
_MscVrSnmpViewRowStatus_Type = RowStatus
_MscVrSnmpViewRowStatus_Object = MibTableColumn
mscVrSnmpViewRowStatus = _MscVrSnmpViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1, 1),
    _MscVrSnmpViewRowStatus_Type()
)
mscVrSnmpViewRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpViewRowStatus.setStatus("mandatory")
_MscVrSnmpViewComponentName_Type = DisplayString
_MscVrSnmpViewComponentName_Object = MibTableColumn
mscVrSnmpViewComponentName = _MscVrSnmpViewComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1, 2),
    _MscVrSnmpViewComponentName_Type()
)
mscVrSnmpViewComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpViewComponentName.setStatus("mandatory")
_MscVrSnmpViewStorageType_Type = StorageType
_MscVrSnmpViewStorageType_Object = MibTableColumn
mscVrSnmpViewStorageType = _MscVrSnmpViewStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1, 4),
    _MscVrSnmpViewStorageType_Type()
)
mscVrSnmpViewStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpViewStorageType.setStatus("mandatory")


class _MscVrSnmpViewIndex_Type(Integer32):
    """Custom type mscVrSnmpViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpViewIndex_Type.__name__ = "Integer32"
_MscVrSnmpViewIndex_Object = MibTableColumn
mscVrSnmpViewIndex = _MscVrSnmpViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1, 10),
    _MscVrSnmpViewIndex_Type()
)
mscVrSnmpViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpViewIndex.setStatus("mandatory")
_MscVrSnmpViewSubtreeIndex_Type = ObjectIdentifier
_MscVrSnmpViewSubtreeIndex_Object = MibTableColumn
mscVrSnmpViewSubtreeIndex = _MscVrSnmpViewSubtreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 1, 1, 11),
    _MscVrSnmpViewSubtreeIndex_Type()
)
mscVrSnmpViewSubtreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpViewSubtreeIndex.setStatus("mandatory")
_MscVrSnmpViewProvTable_Object = MibTable
mscVrSnmpViewProvTable = _MscVrSnmpViewProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpViewProvTable.setStatus("mandatory")
_MscVrSnmpViewProvEntry_Object = MibTableRow
mscVrSnmpViewProvEntry = _MscVrSnmpViewProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10, 1)
)
mscVrSnmpViewProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpViewIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpViewSubtreeIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpViewProvEntry.setStatus("mandatory")


class _MscVrSnmpViewMask_Type(HexString):
    """Custom type mscVrSnmpViewMask based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscVrSnmpViewMask_Type.__name__ = "HexString"
_MscVrSnmpViewMask_Object = MibTableColumn
mscVrSnmpViewMask = _MscVrSnmpViewMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10, 1, 1),
    _MscVrSnmpViewMask_Type()
)
mscVrSnmpViewMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpViewMask.setStatus("mandatory")


class _MscVrSnmpViewType_Type(Integer32):
    """Custom type mscVrSnmpViewType based on Integer32"""
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


_MscVrSnmpViewType_Type.__name__ = "Integer32"
_MscVrSnmpViewType_Object = MibTableColumn
mscVrSnmpViewType = _MscVrSnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10, 1, 2),
    _MscVrSnmpViewType_Type()
)
mscVrSnmpViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpViewType.setStatus("mandatory")


class _MscVrSnmpViewRowStorageType_Type(Integer32):
    """Custom type mscVrSnmpViewRowStorageType based on Integer32"""
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


_MscVrSnmpViewRowStorageType_Type.__name__ = "Integer32"
_MscVrSnmpViewRowStorageType_Object = MibTableColumn
mscVrSnmpViewRowStorageType = _MscVrSnmpViewRowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10, 1, 3),
    _MscVrSnmpViewRowStorageType_Type()
)
mscVrSnmpViewRowStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpViewRowStorageType.setStatus("mandatory")


class _MscVrSnmpViewStdRowStatus_Type(Integer32):
    """Custom type mscVrSnmpViewStdRowStatus based on Integer32"""
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


_MscVrSnmpViewStdRowStatus_Type.__name__ = "Integer32"
_MscVrSnmpViewStdRowStatus_Object = MibTableColumn
mscVrSnmpViewStdRowStatus = _MscVrSnmpViewStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 7, 10, 1, 4),
    _MscVrSnmpViewStdRowStatus_Type()
)
mscVrSnmpViewStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpViewStdRowStatus.setStatus("mandatory")
_MscVrSnmpOr_ObjectIdentity = ObjectIdentity
mscVrSnmpOr = _MscVrSnmpOr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8)
)
_MscVrSnmpOrRowStatusTable_Object = MibTable
mscVrSnmpOrRowStatusTable = _MscVrSnmpOrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpOrRowStatusTable.setStatus("mandatory")
_MscVrSnmpOrRowStatusEntry_Object = MibTableRow
mscVrSnmpOrRowStatusEntry = _MscVrSnmpOrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1, 1)
)
mscVrSnmpOrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpOrIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpOrRowStatusEntry.setStatus("mandatory")
_MscVrSnmpOrRowStatus_Type = RowStatus
_MscVrSnmpOrRowStatus_Object = MibTableColumn
mscVrSnmpOrRowStatus = _MscVrSnmpOrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1, 1, 1),
    _MscVrSnmpOrRowStatus_Type()
)
mscVrSnmpOrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOrRowStatus.setStatus("mandatory")
_MscVrSnmpOrComponentName_Type = DisplayString
_MscVrSnmpOrComponentName_Object = MibTableColumn
mscVrSnmpOrComponentName = _MscVrSnmpOrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1, 1, 2),
    _MscVrSnmpOrComponentName_Type()
)
mscVrSnmpOrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOrComponentName.setStatus("mandatory")
_MscVrSnmpOrStorageType_Type = StorageType
_MscVrSnmpOrStorageType_Object = MibTableColumn
mscVrSnmpOrStorageType = _MscVrSnmpOrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1, 1, 4),
    _MscVrSnmpOrStorageType_Type()
)
mscVrSnmpOrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOrStorageType.setStatus("mandatory")


class _MscVrSnmpOrIndex_Type(Integer32):
    """Custom type mscVrSnmpOrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MscVrSnmpOrIndex_Type.__name__ = "Integer32"
_MscVrSnmpOrIndex_Object = MibTableColumn
mscVrSnmpOrIndex = _MscVrSnmpOrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 1, 1, 10),
    _MscVrSnmpOrIndex_Type()
)
mscVrSnmpOrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpOrIndex.setStatus("mandatory")
_MscVrSnmpOrOrTable_Object = MibTable
mscVrSnmpOrOrTable = _MscVrSnmpOrOrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpOrOrTable.setStatus("mandatory")
_MscVrSnmpOrOrEntry_Object = MibTableRow
mscVrSnmpOrOrEntry = _MscVrSnmpOrOrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 10, 1)
)
mscVrSnmpOrOrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpOrIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpOrOrEntry.setStatus("mandatory")
_MscVrSnmpOrId_Type = ObjectIdentifier
_MscVrSnmpOrId_Object = MibTableColumn
mscVrSnmpOrId = _MscVrSnmpOrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 10, 1, 2),
    _MscVrSnmpOrId_Type()
)
mscVrSnmpOrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOrId.setStatus("mandatory")


class _MscVrSnmpOrDescr_Type(AsciiString):
    """Custom type mscVrSnmpOrDescr based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrSnmpOrDescr_Type.__name__ = "AsciiString"
_MscVrSnmpOrDescr_Object = MibTableColumn
mscVrSnmpOrDescr = _MscVrSnmpOrDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 8, 10, 1, 3),
    _MscVrSnmpOrDescr_Type()
)
mscVrSnmpOrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOrDescr.setStatus("mandatory")
_MscVrSnmpV2Stats_ObjectIdentity = ObjectIdentity
mscVrSnmpV2Stats = _MscVrSnmpV2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9)
)
_MscVrSnmpV2StatsRowStatusTable_Object = MibTable
mscVrSnmpV2StatsRowStatusTable = _MscVrSnmpV2StatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsRowStatusTable.setStatus("obsolete")
_MscVrSnmpV2StatsRowStatusEntry_Object = MibTableRow
mscVrSnmpV2StatsRowStatusEntry = _MscVrSnmpV2StatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1, 1)
)
mscVrSnmpV2StatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpV2StatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsRowStatusEntry.setStatus("obsolete")
_MscVrSnmpV2StatsRowStatus_Type = RowStatus
_MscVrSnmpV2StatsRowStatus_Object = MibTableColumn
mscVrSnmpV2StatsRowStatus = _MscVrSnmpV2StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1, 1, 1),
    _MscVrSnmpV2StatsRowStatus_Type()
)
mscVrSnmpV2StatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsRowStatus.setStatus("obsolete")
_MscVrSnmpV2StatsComponentName_Type = DisplayString
_MscVrSnmpV2StatsComponentName_Object = MibTableColumn
mscVrSnmpV2StatsComponentName = _MscVrSnmpV2StatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1, 1, 2),
    _MscVrSnmpV2StatsComponentName_Type()
)
mscVrSnmpV2StatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsComponentName.setStatus("obsolete")
_MscVrSnmpV2StatsStorageType_Type = StorageType
_MscVrSnmpV2StatsStorageType_Object = MibTableColumn
mscVrSnmpV2StatsStorageType = _MscVrSnmpV2StatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1, 1, 4),
    _MscVrSnmpV2StatsStorageType_Type()
)
mscVrSnmpV2StatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsStorageType.setStatus("obsolete")
_MscVrSnmpV2StatsIndex_Type = NonReplicated
_MscVrSnmpV2StatsIndex_Object = MibTableColumn
mscVrSnmpV2StatsIndex = _MscVrSnmpV2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 1, 1, 10),
    _MscVrSnmpV2StatsIndex_Type()
)
mscVrSnmpV2StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsIndex.setStatus("obsolete")
_MscVrSnmpV2StatsStatsTable_Object = MibTable
mscVrSnmpV2StatsStatsTable = _MscVrSnmpV2StatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsStatsTable.setStatus("obsolete")
_MscVrSnmpV2StatsStatsEntry_Object = MibTableRow
mscVrSnmpV2StatsStatsEntry = _MscVrSnmpV2StatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1)
)
mscVrSnmpV2StatsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpV2StatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsStatsEntry.setStatus("obsolete")


class _MscVrSnmpV2StatsPackets_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsPackets_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsPackets_Object = MibTableColumn
mscVrSnmpV2StatsPackets = _MscVrSnmpV2StatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 1),
    _MscVrSnmpV2StatsPackets_Type()
)
mscVrSnmpV2StatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsPackets.setStatus("obsolete")


class _MscVrSnmpV2StatsEncodingErrors_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsEncodingErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsEncodingErrors_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsEncodingErrors_Object = MibTableColumn
mscVrSnmpV2StatsEncodingErrors = _MscVrSnmpV2StatsEncodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 2),
    _MscVrSnmpV2StatsEncodingErrors_Type()
)
mscVrSnmpV2StatsEncodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsEncodingErrors.setStatus("obsolete")


class _MscVrSnmpV2StatsUnknownSrcParties_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsUnknownSrcParties based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsUnknownSrcParties_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsUnknownSrcParties_Object = MibTableColumn
mscVrSnmpV2StatsUnknownSrcParties = _MscVrSnmpV2StatsUnknownSrcParties_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 3),
    _MscVrSnmpV2StatsUnknownSrcParties_Type()
)
mscVrSnmpV2StatsUnknownSrcParties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsUnknownSrcParties.setStatus("obsolete")


class _MscVrSnmpV2StatsBadAuths_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsBadAuths based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsBadAuths_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsBadAuths_Object = MibTableColumn
mscVrSnmpV2StatsBadAuths = _MscVrSnmpV2StatsBadAuths_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 4),
    _MscVrSnmpV2StatsBadAuths_Type()
)
mscVrSnmpV2StatsBadAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsBadAuths.setStatus("obsolete")


class _MscVrSnmpV2StatsNotInLifetime_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsNotInLifetime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsNotInLifetime_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsNotInLifetime_Object = MibTableColumn
mscVrSnmpV2StatsNotInLifetime = _MscVrSnmpV2StatsNotInLifetime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 5),
    _MscVrSnmpV2StatsNotInLifetime_Type()
)
mscVrSnmpV2StatsNotInLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsNotInLifetime.setStatus("obsolete")


class _MscVrSnmpV2StatsWrongDigestValues_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsWrongDigestValues based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsWrongDigestValues_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsWrongDigestValues_Object = MibTableColumn
mscVrSnmpV2StatsWrongDigestValues = _MscVrSnmpV2StatsWrongDigestValues_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 6),
    _MscVrSnmpV2StatsWrongDigestValues_Type()
)
mscVrSnmpV2StatsWrongDigestValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsWrongDigestValues.setStatus("obsolete")


class _MscVrSnmpV2StatsUnknownContexts_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsUnknownContexts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsUnknownContexts_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsUnknownContexts_Object = MibTableColumn
mscVrSnmpV2StatsUnknownContexts = _MscVrSnmpV2StatsUnknownContexts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 7),
    _MscVrSnmpV2StatsUnknownContexts_Type()
)
mscVrSnmpV2StatsUnknownContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsUnknownContexts.setStatus("obsolete")


class _MscVrSnmpV2StatsBadOperations_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsBadOperations based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsBadOperations_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsBadOperations_Object = MibTableColumn
mscVrSnmpV2StatsBadOperations = _MscVrSnmpV2StatsBadOperations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 8),
    _MscVrSnmpV2StatsBadOperations_Type()
)
mscVrSnmpV2StatsBadOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsBadOperations.setStatus("obsolete")


class _MscVrSnmpV2StatsSilentDrops_Type(Unsigned32):
    """Custom type mscVrSnmpV2StatsSilentDrops based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV2StatsSilentDrops_Type.__name__ = "Unsigned32"
_MscVrSnmpV2StatsSilentDrops_Object = MibTableColumn
mscVrSnmpV2StatsSilentDrops = _MscVrSnmpV2StatsSilentDrops_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 9, 10, 1, 9),
    _MscVrSnmpV2StatsSilentDrops_Type()
)
mscVrSnmpV2StatsSilentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV2StatsSilentDrops.setStatus("obsolete")
_MscVrSnmpV1Stats_ObjectIdentity = ObjectIdentity
mscVrSnmpV1Stats = _MscVrSnmpV1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10)
)
_MscVrSnmpV1StatsRowStatusTable_Object = MibTable
mscVrSnmpV1StatsRowStatusTable = _MscVrSnmpV1StatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsRowStatusTable.setStatus("mandatory")
_MscVrSnmpV1StatsRowStatusEntry_Object = MibTableRow
mscVrSnmpV1StatsRowStatusEntry = _MscVrSnmpV1StatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1, 1)
)
mscVrSnmpV1StatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpV1StatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsRowStatusEntry.setStatus("mandatory")
_MscVrSnmpV1StatsRowStatus_Type = RowStatus
_MscVrSnmpV1StatsRowStatus_Object = MibTableColumn
mscVrSnmpV1StatsRowStatus = _MscVrSnmpV1StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1, 1, 1),
    _MscVrSnmpV1StatsRowStatus_Type()
)
mscVrSnmpV1StatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsRowStatus.setStatus("mandatory")
_MscVrSnmpV1StatsComponentName_Type = DisplayString
_MscVrSnmpV1StatsComponentName_Object = MibTableColumn
mscVrSnmpV1StatsComponentName = _MscVrSnmpV1StatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1, 1, 2),
    _MscVrSnmpV1StatsComponentName_Type()
)
mscVrSnmpV1StatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsComponentName.setStatus("mandatory")
_MscVrSnmpV1StatsStorageType_Type = StorageType
_MscVrSnmpV1StatsStorageType_Object = MibTableColumn
mscVrSnmpV1StatsStorageType = _MscVrSnmpV1StatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1, 1, 4),
    _MscVrSnmpV1StatsStorageType_Type()
)
mscVrSnmpV1StatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsStorageType.setStatus("mandatory")
_MscVrSnmpV1StatsIndex_Type = NonReplicated
_MscVrSnmpV1StatsIndex_Object = MibTableColumn
mscVrSnmpV1StatsIndex = _MscVrSnmpV1StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 1, 1, 10),
    _MscVrSnmpV1StatsIndex_Type()
)
mscVrSnmpV1StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsIndex.setStatus("mandatory")
_MscVrSnmpV1StatsStatsTable_Object = MibTable
mscVrSnmpV1StatsStatsTable = _MscVrSnmpV1StatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsStatsTable.setStatus("mandatory")
_MscVrSnmpV1StatsStatsEntry_Object = MibTableRow
mscVrSnmpV1StatsStatsEntry = _MscVrSnmpV1StatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 10, 1)
)
mscVrSnmpV1StatsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpV1StatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsStatsEntry.setStatus("mandatory")


class _MscVrSnmpV1StatsBadCommunityNames_Type(Unsigned32):
    """Custom type mscVrSnmpV1StatsBadCommunityNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV1StatsBadCommunityNames_Type.__name__ = "Unsigned32"
_MscVrSnmpV1StatsBadCommunityNames_Object = MibTableColumn
mscVrSnmpV1StatsBadCommunityNames = _MscVrSnmpV1StatsBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 10, 1, 1),
    _MscVrSnmpV1StatsBadCommunityNames_Type()
)
mscVrSnmpV1StatsBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsBadCommunityNames.setStatus("mandatory")


class _MscVrSnmpV1StatsBadCommunityUses_Type(Unsigned32):
    """Custom type mscVrSnmpV1StatsBadCommunityUses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpV1StatsBadCommunityUses_Type.__name__ = "Unsigned32"
_MscVrSnmpV1StatsBadCommunityUses_Object = MibTableColumn
mscVrSnmpV1StatsBadCommunityUses = _MscVrSnmpV1StatsBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 10, 10, 1, 2),
    _MscVrSnmpV1StatsBadCommunityUses_Type()
)
mscVrSnmpV1StatsBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpV1StatsBadCommunityUses.setStatus("mandatory")
_MscVrSnmpMibIIStats_ObjectIdentity = ObjectIdentity
mscVrSnmpMibIIStats = _MscVrSnmpMibIIStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11)
)
_MscVrSnmpMibIIStatsRowStatusTable_Object = MibTable
mscVrSnmpMibIIStatsRowStatusTable = _MscVrSnmpMibIIStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1)
)
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsRowStatusTable.setStatus("mandatory")
_MscVrSnmpMibIIStatsRowStatusEntry_Object = MibTableRow
mscVrSnmpMibIIStatsRowStatusEntry = _MscVrSnmpMibIIStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1, 1)
)
mscVrSnmpMibIIStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpMibIIStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsRowStatusEntry.setStatus("mandatory")
_MscVrSnmpMibIIStatsRowStatus_Type = RowStatus
_MscVrSnmpMibIIStatsRowStatus_Object = MibTableColumn
mscVrSnmpMibIIStatsRowStatus = _MscVrSnmpMibIIStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1, 1, 1),
    _MscVrSnmpMibIIStatsRowStatus_Type()
)
mscVrSnmpMibIIStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsRowStatus.setStatus("mandatory")
_MscVrSnmpMibIIStatsComponentName_Type = DisplayString
_MscVrSnmpMibIIStatsComponentName_Object = MibTableColumn
mscVrSnmpMibIIStatsComponentName = _MscVrSnmpMibIIStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1, 1, 2),
    _MscVrSnmpMibIIStatsComponentName_Type()
)
mscVrSnmpMibIIStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsComponentName.setStatus("mandatory")
_MscVrSnmpMibIIStatsStorageType_Type = StorageType
_MscVrSnmpMibIIStatsStorageType_Object = MibTableColumn
mscVrSnmpMibIIStatsStorageType = _MscVrSnmpMibIIStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1, 1, 4),
    _MscVrSnmpMibIIStatsStorageType_Type()
)
mscVrSnmpMibIIStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsStorageType.setStatus("mandatory")
_MscVrSnmpMibIIStatsIndex_Type = NonReplicated
_MscVrSnmpMibIIStatsIndex_Object = MibTableColumn
mscVrSnmpMibIIStatsIndex = _MscVrSnmpMibIIStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 1, 1, 10),
    _MscVrSnmpMibIIStatsIndex_Type()
)
mscVrSnmpMibIIStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsIndex.setStatus("mandatory")
_MscVrSnmpMibIIStatsStatsTable_Object = MibTable
mscVrSnmpMibIIStatsStatsTable = _MscVrSnmpMibIIStatsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10)
)
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsStatsTable.setStatus("mandatory")
_MscVrSnmpMibIIStatsStatsEntry_Object = MibTableRow
mscVrSnmpMibIIStatsStatsEntry = _MscVrSnmpMibIIStatsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1)
)
mscVrSnmpMibIIStatsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpMibIIStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsStatsEntry.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInPackets_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInPackets_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInPackets_Object = MibTableColumn
mscVrSnmpMibIIStatsInPackets = _MscVrSnmpMibIIStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 1),
    _MscVrSnmpMibIIStatsInPackets_Type()
)
mscVrSnmpMibIIStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInPackets.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInBadCommunityNames_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInBadCommunityNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInBadCommunityNames_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInBadCommunityNames_Object = MibTableColumn
mscVrSnmpMibIIStatsInBadCommunityNames = _MscVrSnmpMibIIStatsInBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 2),
    _MscVrSnmpMibIIStatsInBadCommunityNames_Type()
)
mscVrSnmpMibIIStatsInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInBadCommunityNames.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInBadCommunityUses_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInBadCommunityUses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInBadCommunityUses_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInBadCommunityUses_Object = MibTableColumn
mscVrSnmpMibIIStatsInBadCommunityUses = _MscVrSnmpMibIIStatsInBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 3),
    _MscVrSnmpMibIIStatsInBadCommunityUses_Type()
)
mscVrSnmpMibIIStatsInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInBadCommunityUses.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInAsnParseErrs_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInAsnParseErrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInAsnParseErrs_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInAsnParseErrs_Object = MibTableColumn
mscVrSnmpMibIIStatsInAsnParseErrs = _MscVrSnmpMibIIStatsInAsnParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 4),
    _MscVrSnmpMibIIStatsInAsnParseErrs_Type()
)
mscVrSnmpMibIIStatsInAsnParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInAsnParseErrs.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutPackets_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutPackets_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutPackets_Object = MibTableColumn
mscVrSnmpMibIIStatsOutPackets = _MscVrSnmpMibIIStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 5),
    _MscVrSnmpMibIIStatsOutPackets_Type()
)
mscVrSnmpMibIIStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutPackets.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInBadVersions_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInBadVersions based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInBadVersions_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInBadVersions_Object = MibTableColumn
mscVrSnmpMibIIStatsInBadVersions = _MscVrSnmpMibIIStatsInBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 6),
    _MscVrSnmpMibIIStatsInBadVersions_Type()
)
mscVrSnmpMibIIStatsInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInBadVersions.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInTotalReqVars_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInTotalReqVars based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInTotalReqVars_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInTotalReqVars_Object = MibTableColumn
mscVrSnmpMibIIStatsInTotalReqVars = _MscVrSnmpMibIIStatsInTotalReqVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 7),
    _MscVrSnmpMibIIStatsInTotalReqVars_Type()
)
mscVrSnmpMibIIStatsInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInTotalReqVars.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInTotalSetVars_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInTotalSetVars based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInTotalSetVars_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInTotalSetVars_Object = MibTableColumn
mscVrSnmpMibIIStatsInTotalSetVars = _MscVrSnmpMibIIStatsInTotalSetVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 8),
    _MscVrSnmpMibIIStatsInTotalSetVars_Type()
)
mscVrSnmpMibIIStatsInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInTotalSetVars.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInGetRequests_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInGetRequests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInGetRequests_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInGetRequests_Object = MibTableColumn
mscVrSnmpMibIIStatsInGetRequests = _MscVrSnmpMibIIStatsInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 9),
    _MscVrSnmpMibIIStatsInGetRequests_Type()
)
mscVrSnmpMibIIStatsInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInGetRequests.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInGetNexts_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInGetNexts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInGetNexts_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInGetNexts_Object = MibTableColumn
mscVrSnmpMibIIStatsInGetNexts = _MscVrSnmpMibIIStatsInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 10),
    _MscVrSnmpMibIIStatsInGetNexts_Type()
)
mscVrSnmpMibIIStatsInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInGetNexts.setStatus("mandatory")


class _MscVrSnmpMibIIStatsInSetRequests_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsInSetRequests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsInSetRequests_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsInSetRequests_Object = MibTableColumn
mscVrSnmpMibIIStatsInSetRequests = _MscVrSnmpMibIIStatsInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 11),
    _MscVrSnmpMibIIStatsInSetRequests_Type()
)
mscVrSnmpMibIIStatsInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsInSetRequests.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutTooBigs_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutTooBigs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutTooBigs_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutTooBigs_Object = MibTableColumn
mscVrSnmpMibIIStatsOutTooBigs = _MscVrSnmpMibIIStatsOutTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 12),
    _MscVrSnmpMibIIStatsOutTooBigs_Type()
)
mscVrSnmpMibIIStatsOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutTooBigs.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutNoSuchNames_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutNoSuchNames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutNoSuchNames_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutNoSuchNames_Object = MibTableColumn
mscVrSnmpMibIIStatsOutNoSuchNames = _MscVrSnmpMibIIStatsOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 13),
    _MscVrSnmpMibIIStatsOutNoSuchNames_Type()
)
mscVrSnmpMibIIStatsOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutNoSuchNames.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutBadValues_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutBadValues based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutBadValues_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutBadValues_Object = MibTableColumn
mscVrSnmpMibIIStatsOutBadValues = _MscVrSnmpMibIIStatsOutBadValues_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 14),
    _MscVrSnmpMibIIStatsOutBadValues_Type()
)
mscVrSnmpMibIIStatsOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutBadValues.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutGenErrs_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutGenErrs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutGenErrs_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutGenErrs_Object = MibTableColumn
mscVrSnmpMibIIStatsOutGenErrs = _MscVrSnmpMibIIStatsOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 15),
    _MscVrSnmpMibIIStatsOutGenErrs_Type()
)
mscVrSnmpMibIIStatsOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutGenErrs.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutGetResponses_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutGetResponses based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutGetResponses_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutGetResponses_Object = MibTableColumn
mscVrSnmpMibIIStatsOutGetResponses = _MscVrSnmpMibIIStatsOutGetResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 16),
    _MscVrSnmpMibIIStatsOutGetResponses_Type()
)
mscVrSnmpMibIIStatsOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutGetResponses.setStatus("mandatory")


class _MscVrSnmpMibIIStatsOutTraps_Type(Unsigned32):
    """Custom type mscVrSnmpMibIIStatsOutTraps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpMibIIStatsOutTraps_Type.__name__ = "Unsigned32"
_MscVrSnmpMibIIStatsOutTraps_Object = MibTableColumn
mscVrSnmpMibIIStatsOutTraps = _MscVrSnmpMibIIStatsOutTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 11, 10, 1, 17),
    _MscVrSnmpMibIIStatsOutTraps_Type()
)
mscVrSnmpMibIIStatsOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMibIIStatsOutTraps.setStatus("mandatory")
_MscVrSnmpProvTable_Object = MibTable
mscVrSnmpProvTable = _MscVrSnmpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20)
)
if mibBuilder.loadTexts:
    mscVrSnmpProvTable.setStatus("mandatory")
_MscVrSnmpProvEntry_Object = MibTableRow
mscVrSnmpProvEntry = _MscVrSnmpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1)
)
mscVrSnmpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpProvEntry.setStatus("mandatory")
_MscVrSnmpV1EnableAuthenTraps_Type = Status
_MscVrSnmpV1EnableAuthenTraps_Object = MibTableColumn
mscVrSnmpV1EnableAuthenTraps = _MscVrSnmpV1EnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1, 1),
    _MscVrSnmpV1EnableAuthenTraps_Type()
)
mscVrSnmpV1EnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpV1EnableAuthenTraps.setStatus("mandatory")
_MscVrSnmpV2EnableAuthenTraps_Type = Status
_MscVrSnmpV2EnableAuthenTraps_Object = MibTableColumn
mscVrSnmpV2EnableAuthenTraps = _MscVrSnmpV2EnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1, 2),
    _MscVrSnmpV2EnableAuthenTraps_Type()
)
mscVrSnmpV2EnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpV2EnableAuthenTraps.setStatus("mandatory")
_MscVrSnmpAlarmsAsTraps_Type = Status
_MscVrSnmpAlarmsAsTraps_Object = MibTableColumn
mscVrSnmpAlarmsAsTraps = _MscVrSnmpAlarmsAsTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1, 3),
    _MscVrSnmpAlarmsAsTraps_Type()
)
mscVrSnmpAlarmsAsTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAlarmsAsTraps.setStatus("mandatory")


class _MscVrSnmpIpStack_Type(Integer32):
    """Custom type mscVrSnmpIpStack based on Integer32"""
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


_MscVrSnmpIpStack_Type.__name__ = "Integer32"
_MscVrSnmpIpStack_Object = MibTableColumn
mscVrSnmpIpStack = _MscVrSnmpIpStack_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1, 4),
    _MscVrSnmpIpStack_Type()
)
mscVrSnmpIpStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpIpStack.setStatus("mandatory")
_MscVrSnmpCidInEntTraps_Type = Status
_MscVrSnmpCidInEntTraps_Object = MibTableColumn
mscVrSnmpCidInEntTraps = _MscVrSnmpCidInEntTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 20, 1, 5),
    _MscVrSnmpCidInEntTraps_Type()
)
mscVrSnmpCidInEntTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpCidInEntTraps.setStatus("mandatory")
_MscVrSnmpStateTable_Object = MibTable
mscVrSnmpStateTable = _MscVrSnmpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21)
)
if mibBuilder.loadTexts:
    mscVrSnmpStateTable.setStatus("mandatory")
_MscVrSnmpStateEntry_Object = MibTableRow
mscVrSnmpStateEntry = _MscVrSnmpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1)
)
mscVrSnmpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpStateEntry.setStatus("mandatory")


class _MscVrSnmpAdminState_Type(Integer32):
    """Custom type mscVrSnmpAdminState based on Integer32"""
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


_MscVrSnmpAdminState_Type.__name__ = "Integer32"
_MscVrSnmpAdminState_Object = MibTableColumn
mscVrSnmpAdminState = _MscVrSnmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 1),
    _MscVrSnmpAdminState_Type()
)
mscVrSnmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpAdminState.setStatus("mandatory")


class _MscVrSnmpOperationalState_Type(Integer32):
    """Custom type mscVrSnmpOperationalState based on Integer32"""
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


_MscVrSnmpOperationalState_Type.__name__ = "Integer32"
_MscVrSnmpOperationalState_Object = MibTableColumn
mscVrSnmpOperationalState = _MscVrSnmpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 2),
    _MscVrSnmpOperationalState_Type()
)
mscVrSnmpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOperationalState.setStatus("mandatory")


class _MscVrSnmpUsageState_Type(Integer32):
    """Custom type mscVrSnmpUsageState based on Integer32"""
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


_MscVrSnmpUsageState_Type.__name__ = "Integer32"
_MscVrSnmpUsageState_Object = MibTableColumn
mscVrSnmpUsageState = _MscVrSnmpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 3),
    _MscVrSnmpUsageState_Type()
)
mscVrSnmpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpUsageState.setStatus("mandatory")


class _MscVrSnmpAvailabilityStatus_Type(OctetString):
    """Custom type mscVrSnmpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVrSnmpAvailabilityStatus_Type.__name__ = "OctetString"
_MscVrSnmpAvailabilityStatus_Object = MibTableColumn
mscVrSnmpAvailabilityStatus = _MscVrSnmpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 4),
    _MscVrSnmpAvailabilityStatus_Type()
)
mscVrSnmpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpAvailabilityStatus.setStatus("mandatory")


class _MscVrSnmpProceduralStatus_Type(OctetString):
    """Custom type mscVrSnmpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrSnmpProceduralStatus_Type.__name__ = "OctetString"
_MscVrSnmpProceduralStatus_Object = MibTableColumn
mscVrSnmpProceduralStatus = _MscVrSnmpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 5),
    _MscVrSnmpProceduralStatus_Type()
)
mscVrSnmpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpProceduralStatus.setStatus("mandatory")


class _MscVrSnmpControlStatus_Type(OctetString):
    """Custom type mscVrSnmpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrSnmpControlStatus_Type.__name__ = "OctetString"
_MscVrSnmpControlStatus_Object = MibTableColumn
mscVrSnmpControlStatus = _MscVrSnmpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 6),
    _MscVrSnmpControlStatus_Type()
)
mscVrSnmpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpControlStatus.setStatus("mandatory")


class _MscVrSnmpAlarmStatus_Type(OctetString):
    """Custom type mscVrSnmpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrSnmpAlarmStatus_Type.__name__ = "OctetString"
_MscVrSnmpAlarmStatus_Object = MibTableColumn
mscVrSnmpAlarmStatus = _MscVrSnmpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 7),
    _MscVrSnmpAlarmStatus_Type()
)
mscVrSnmpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpAlarmStatus.setStatus("mandatory")


class _MscVrSnmpStandbyStatus_Type(Integer32):
    """Custom type mscVrSnmpStandbyStatus based on Integer32"""
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


_MscVrSnmpStandbyStatus_Type.__name__ = "Integer32"
_MscVrSnmpStandbyStatus_Object = MibTableColumn
mscVrSnmpStandbyStatus = _MscVrSnmpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 8),
    _MscVrSnmpStandbyStatus_Type()
)
mscVrSnmpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpStandbyStatus.setStatus("mandatory")


class _MscVrSnmpUnknownStatus_Type(Integer32):
    """Custom type mscVrSnmpUnknownStatus based on Integer32"""
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


_MscVrSnmpUnknownStatus_Type.__name__ = "Integer32"
_MscVrSnmpUnknownStatus_Object = MibTableColumn
mscVrSnmpUnknownStatus = _MscVrSnmpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 21, 1, 9),
    _MscVrSnmpUnknownStatus_Type()
)
mscVrSnmpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpUnknownStatus.setStatus("mandatory")
_MscVrSnmpStatsTable_Object = MibTable
mscVrSnmpStatsTable = _MscVrSnmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22)
)
if mibBuilder.loadTexts:
    mscVrSnmpStatsTable.setStatus("mandatory")
_MscVrSnmpStatsEntry_Object = MibTableRow
mscVrSnmpStatsEntry = _MscVrSnmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1)
)
mscVrSnmpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrSnmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrSnmpStatsEntry.setStatus("mandatory")


class _MscVrSnmpLastOrChange_Type(Unsigned32):
    """Custom type mscVrSnmpLastOrChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpLastOrChange_Type.__name__ = "Unsigned32"
_MscVrSnmpLastOrChange_Object = MibTableColumn
mscVrSnmpLastOrChange = _MscVrSnmpLastOrChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1, 1),
    _MscVrSnmpLastOrChange_Type()
)
mscVrSnmpLastOrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpLastOrChange.setStatus("mandatory")


class _MscVrSnmpTrapsProcessed_Type(Unsigned32):
    """Custom type mscVrSnmpTrapsProcessed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpTrapsProcessed_Type.__name__ = "Unsigned32"
_MscVrSnmpTrapsProcessed_Object = MibTableColumn
mscVrSnmpTrapsProcessed = _MscVrSnmpTrapsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1, 2),
    _MscVrSnmpTrapsProcessed_Type()
)
mscVrSnmpTrapsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpTrapsProcessed.setStatus("mandatory")


class _MscVrSnmpTrapsDiscarded_Type(Unsigned32):
    """Custom type mscVrSnmpTrapsDiscarded based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpTrapsDiscarded_Type.__name__ = "Unsigned32"
_MscVrSnmpTrapsDiscarded_Object = MibTableColumn
mscVrSnmpTrapsDiscarded = _MscVrSnmpTrapsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1, 3),
    _MscVrSnmpTrapsDiscarded_Type()
)
mscVrSnmpTrapsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpTrapsDiscarded.setStatus("mandatory")


class _MscVrSnmpLastAuthFailure_Type(Unsigned32):
    """Custom type mscVrSnmpLastAuthFailure based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrSnmpLastAuthFailure_Type.__name__ = "Unsigned32"
_MscVrSnmpLastAuthFailure_Object = MibTableColumn
mscVrSnmpLastAuthFailure = _MscVrSnmpLastAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1, 4),
    _MscVrSnmpLastAuthFailure_Type()
)
mscVrSnmpLastAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpLastAuthFailure.setStatus("mandatory")


class _MscVrSnmpMgrOfLastAuthFailure_Type(IpAddress):
    """Custom type mscVrSnmpMgrOfLastAuthFailure based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrSnmpMgrOfLastAuthFailure_Object = MibTableColumn
mscVrSnmpMgrOfLastAuthFailure = _MscVrSnmpMgrOfLastAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 8, 22, 1, 5),
    _MscVrSnmpMgrOfLastAuthFailure_Type()
)
mscVrSnmpMgrOfLastAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpMgrOfLastAuthFailure.setStatus("mandatory")
_MscVrInitSnmpConfig_ObjectIdentity = ObjectIdentity
mscVrInitSnmpConfig = _MscVrInitSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9)
)
_MscVrInitSnmpConfigRowStatusTable_Object = MibTable
mscVrInitSnmpConfigRowStatusTable = _MscVrInitSnmpConfigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigRowStatusTable.setStatus("obsolete")
_MscVrInitSnmpConfigRowStatusEntry_Object = MibTableRow
mscVrInitSnmpConfigRowStatusEntry = _MscVrInitSnmpConfigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1, 1)
)
mscVrInitSnmpConfigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrInitSnmpConfigIndex"),
)
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigRowStatusEntry.setStatus("obsolete")
_MscVrInitSnmpConfigRowStatus_Type = RowStatus
_MscVrInitSnmpConfigRowStatus_Object = MibTableColumn
mscVrInitSnmpConfigRowStatus = _MscVrInitSnmpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1, 1, 1),
    _MscVrInitSnmpConfigRowStatus_Type()
)
mscVrInitSnmpConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigRowStatus.setStatus("obsolete")
_MscVrInitSnmpConfigComponentName_Type = DisplayString
_MscVrInitSnmpConfigComponentName_Object = MibTableColumn
mscVrInitSnmpConfigComponentName = _MscVrInitSnmpConfigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1, 1, 2),
    _MscVrInitSnmpConfigComponentName_Type()
)
mscVrInitSnmpConfigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigComponentName.setStatus("obsolete")
_MscVrInitSnmpConfigStorageType_Type = StorageType
_MscVrInitSnmpConfigStorageType_Object = MibTableColumn
mscVrInitSnmpConfigStorageType = _MscVrInitSnmpConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1, 1, 4),
    _MscVrInitSnmpConfigStorageType_Type()
)
mscVrInitSnmpConfigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigStorageType.setStatus("obsolete")
_MscVrInitSnmpConfigIndex_Type = NonReplicated
_MscVrInitSnmpConfigIndex_Object = MibTableColumn
mscVrInitSnmpConfigIndex = _MscVrInitSnmpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 1, 1, 10),
    _MscVrInitSnmpConfigIndex_Type()
)
mscVrInitSnmpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigIndex.setStatus("obsolete")
_MscVrInitSnmpConfigProvTable_Object = MibTable
mscVrInitSnmpConfigProvTable = _MscVrInitSnmpConfigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigProvTable.setStatus("obsolete")
_MscVrInitSnmpConfigProvEntry_Object = MibTableRow
mscVrInitSnmpConfigProvEntry = _MscVrInitSnmpConfigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 10, 1)
)
mscVrInitSnmpConfigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseSnmpMIB", "mscVrInitSnmpConfigIndex"),
)
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigProvEntry.setStatus("obsolete")


class _MscVrInitSnmpConfigAgentAddress_Type(AsciiString):
    """Custom type mscVrInitSnmpConfigAgentAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MscVrInitSnmpConfigAgentAddress_Type.__name__ = "AsciiString"
_MscVrInitSnmpConfigAgentAddress_Object = MibTableColumn
mscVrInitSnmpConfigAgentAddress = _MscVrInitSnmpConfigAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 10, 1, 1),
    _MscVrInitSnmpConfigAgentAddress_Type()
)
mscVrInitSnmpConfigAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigAgentAddress.setStatus("obsolete")


class _MscVrInitSnmpConfigManagerAddress_Type(AsciiString):
    """Custom type mscVrInitSnmpConfigManagerAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MscVrInitSnmpConfigManagerAddress_Type.__name__ = "AsciiString"
_MscVrInitSnmpConfigManagerAddress_Object = MibTableColumn
mscVrInitSnmpConfigManagerAddress = _MscVrInitSnmpConfigManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 9, 10, 1, 2),
    _MscVrInitSnmpConfigManagerAddress_Type()
)
mscVrInitSnmpConfigManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrInitSnmpConfigManagerAddress.setStatus("obsolete")
_BaseSnmpMIB_ObjectIdentity = ObjectIdentity
baseSnmpMIB = _BaseSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36)
)
_BaseSnmpGroup_ObjectIdentity = ObjectIdentity
baseSnmpGroup = _BaseSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 1)
)
_BaseSnmpGroupCA_ObjectIdentity = ObjectIdentity
baseSnmpGroupCA = _BaseSnmpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 1, 1)
)
_BaseSnmpGroupCA02_ObjectIdentity = ObjectIdentity
baseSnmpGroupCA02 = _BaseSnmpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 1, 1, 3)
)
_BaseSnmpGroupCA02A_ObjectIdentity = ObjectIdentity
baseSnmpGroupCA02A = _BaseSnmpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 1, 1, 3, 2)
)
_BaseSnmpCapabilities_ObjectIdentity = ObjectIdentity
baseSnmpCapabilities = _BaseSnmpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 3)
)
_BaseSnmpCapabilitiesCA_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesCA = _BaseSnmpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 3, 1)
)
_BaseSnmpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesCA02 = _BaseSnmpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 3, 1, 3)
)
_BaseSnmpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
baseSnmpCapabilitiesCA02A = _BaseSnmpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 36, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BaseSnmpMIB",
    **{"mscVrSnmp": mscVrSnmp,
       "mscVrSnmpRowStatusTable": mscVrSnmpRowStatusTable,
       "mscVrSnmpRowStatusEntry": mscVrSnmpRowStatusEntry,
       "mscVrSnmpRowStatus": mscVrSnmpRowStatus,
       "mscVrSnmpComponentName": mscVrSnmpComponentName,
       "mscVrSnmpStorageType": mscVrSnmpStorageType,
       "mscVrSnmpIndex": mscVrSnmpIndex,
       "mscVrSnmpSys": mscVrSnmpSys,
       "mscVrSnmpSysRowStatusTable": mscVrSnmpSysRowStatusTable,
       "mscVrSnmpSysRowStatusEntry": mscVrSnmpSysRowStatusEntry,
       "mscVrSnmpSysRowStatus": mscVrSnmpSysRowStatus,
       "mscVrSnmpSysComponentName": mscVrSnmpSysComponentName,
       "mscVrSnmpSysStorageType": mscVrSnmpSysStorageType,
       "mscVrSnmpSysIndex": mscVrSnmpSysIndex,
       "mscVrSnmpSysProvTable": mscVrSnmpSysProvTable,
       "mscVrSnmpSysProvEntry": mscVrSnmpSysProvEntry,
       "mscVrSnmpSysContact": mscVrSnmpSysContact,
       "mscVrSnmpSysName": mscVrSnmpSysName,
       "mscVrSnmpSysLocation": mscVrSnmpSysLocation,
       "mscVrSnmpSysOpTable": mscVrSnmpSysOpTable,
       "mscVrSnmpSysOpEntry": mscVrSnmpSysOpEntry,
       "mscVrSnmpSysDescription": mscVrSnmpSysDescription,
       "mscVrSnmpSysObjectId": mscVrSnmpSysObjectId,
       "mscVrSnmpSysUpTime": mscVrSnmpSysUpTime,
       "mscVrSnmpSysServices": mscVrSnmpSysServices,
       "mscVrSnmpCom": mscVrSnmpCom,
       "mscVrSnmpComRowStatusTable": mscVrSnmpComRowStatusTable,
       "mscVrSnmpComRowStatusEntry": mscVrSnmpComRowStatusEntry,
       "mscVrSnmpComRowStatus": mscVrSnmpComRowStatus,
       "mscVrSnmpComComponentName": mscVrSnmpComComponentName,
       "mscVrSnmpComStorageType": mscVrSnmpComStorageType,
       "mscVrSnmpComIndex": mscVrSnmpComIndex,
       "mscVrSnmpComMan": mscVrSnmpComMan,
       "mscVrSnmpComManRowStatusTable": mscVrSnmpComManRowStatusTable,
       "mscVrSnmpComManRowStatusEntry": mscVrSnmpComManRowStatusEntry,
       "mscVrSnmpComManRowStatus": mscVrSnmpComManRowStatus,
       "mscVrSnmpComManComponentName": mscVrSnmpComManComponentName,
       "mscVrSnmpComManStorageType": mscVrSnmpComManStorageType,
       "mscVrSnmpComManIndex": mscVrSnmpComManIndex,
       "mscVrSnmpComManProvTable": mscVrSnmpComManProvTable,
       "mscVrSnmpComManProvEntry": mscVrSnmpComManProvEntry,
       "mscVrSnmpComManTransportAddress": mscVrSnmpComManTransportAddress,
       "mscVrSnmpComManPrivileges": mscVrSnmpComManPrivileges,
       "mscVrSnmpComProvTable": mscVrSnmpComProvTable,
       "mscVrSnmpComProvEntry": mscVrSnmpComProvEntry,
       "mscVrSnmpComCommunityString": mscVrSnmpComCommunityString,
       "mscVrSnmpComAccessMode": mscVrSnmpComAccessMode,
       "mscVrSnmpComViewIndex": mscVrSnmpComViewIndex,
       "mscVrSnmpComTDomain": mscVrSnmpComTDomain,
       "mscVrSnmpAcl": mscVrSnmpAcl,
       "mscVrSnmpAclRowStatusTable": mscVrSnmpAclRowStatusTable,
       "mscVrSnmpAclRowStatusEntry": mscVrSnmpAclRowStatusEntry,
       "mscVrSnmpAclRowStatus": mscVrSnmpAclRowStatus,
       "mscVrSnmpAclComponentName": mscVrSnmpAclComponentName,
       "mscVrSnmpAclStorageType": mscVrSnmpAclStorageType,
       "mscVrSnmpAclTargetIndex": mscVrSnmpAclTargetIndex,
       "mscVrSnmpAclSubjectIndex": mscVrSnmpAclSubjectIndex,
       "mscVrSnmpAclResourcesIndex": mscVrSnmpAclResourcesIndex,
       "mscVrSnmpAclProvTable": mscVrSnmpAclProvTable,
       "mscVrSnmpAclProvEntry": mscVrSnmpAclProvEntry,
       "mscVrSnmpAclPrivileges": mscVrSnmpAclPrivileges,
       "mscVrSnmpAclRowStorageType": mscVrSnmpAclRowStorageType,
       "mscVrSnmpAclStdRowStatus": mscVrSnmpAclStdRowStatus,
       "mscVrSnmpParty": mscVrSnmpParty,
       "mscVrSnmpPartyRowStatusTable": mscVrSnmpPartyRowStatusTable,
       "mscVrSnmpPartyRowStatusEntry": mscVrSnmpPartyRowStatusEntry,
       "mscVrSnmpPartyRowStatus": mscVrSnmpPartyRowStatus,
       "mscVrSnmpPartyComponentName": mscVrSnmpPartyComponentName,
       "mscVrSnmpPartyStorageType": mscVrSnmpPartyStorageType,
       "mscVrSnmpPartyIdentityIndex": mscVrSnmpPartyIdentityIndex,
       "mscVrSnmpPartyProvTable": mscVrSnmpPartyProvTable,
       "mscVrSnmpPartyProvEntry": mscVrSnmpPartyProvEntry,
       "mscVrSnmpPartyStdIndex": mscVrSnmpPartyStdIndex,
       "mscVrSnmpPartyTDomain": mscVrSnmpPartyTDomain,
       "mscVrSnmpPartyTransportAddress": mscVrSnmpPartyTransportAddress,
       "mscVrSnmpPartyMaxMessageSize": mscVrSnmpPartyMaxMessageSize,
       "mscVrSnmpPartyLocal": mscVrSnmpPartyLocal,
       "mscVrSnmpPartyAuthProtocol": mscVrSnmpPartyAuthProtocol,
       "mscVrSnmpPartyAuthPrivate": mscVrSnmpPartyAuthPrivate,
       "mscVrSnmpPartyAuthPublic": mscVrSnmpPartyAuthPublic,
       "mscVrSnmpPartyAuthLifetime": mscVrSnmpPartyAuthLifetime,
       "mscVrSnmpPartyPrivProtocol": mscVrSnmpPartyPrivProtocol,
       "mscVrSnmpPartyRowStorageType": mscVrSnmpPartyRowStorageType,
       "mscVrSnmpPartyStdRowStatus": mscVrSnmpPartyStdRowStatus,
       "mscVrSnmpPartyOpTable": mscVrSnmpPartyOpTable,
       "mscVrSnmpPartyOpEntry": mscVrSnmpPartyOpEntry,
       "mscVrSnmpPartyTrapNumbers": mscVrSnmpPartyTrapNumbers,
       "mscVrSnmpPartyAuthClock": mscVrSnmpPartyAuthClock,
       "mscVrSnmpCon": mscVrSnmpCon,
       "mscVrSnmpConRowStatusTable": mscVrSnmpConRowStatusTable,
       "mscVrSnmpConRowStatusEntry": mscVrSnmpConRowStatusEntry,
       "mscVrSnmpConRowStatus": mscVrSnmpConRowStatus,
       "mscVrSnmpConComponentName": mscVrSnmpConComponentName,
       "mscVrSnmpConStorageType": mscVrSnmpConStorageType,
       "mscVrSnmpConIdentityIndex": mscVrSnmpConIdentityIndex,
       "mscVrSnmpConProvTable": mscVrSnmpConProvTable,
       "mscVrSnmpConProvEntry": mscVrSnmpConProvEntry,
       "mscVrSnmpConStdIndex": mscVrSnmpConStdIndex,
       "mscVrSnmpConLocal": mscVrSnmpConLocal,
       "mscVrSnmpConViewIndex": mscVrSnmpConViewIndex,
       "mscVrSnmpConLocalTime": mscVrSnmpConLocalTime,
       "mscVrSnmpConRowStorageType": mscVrSnmpConRowStorageType,
       "mscVrSnmpConStdRowStatus": mscVrSnmpConStdRowStatus,
       "mscVrSnmpView": mscVrSnmpView,
       "mscVrSnmpViewRowStatusTable": mscVrSnmpViewRowStatusTable,
       "mscVrSnmpViewRowStatusEntry": mscVrSnmpViewRowStatusEntry,
       "mscVrSnmpViewRowStatus": mscVrSnmpViewRowStatus,
       "mscVrSnmpViewComponentName": mscVrSnmpViewComponentName,
       "mscVrSnmpViewStorageType": mscVrSnmpViewStorageType,
       "mscVrSnmpViewIndex": mscVrSnmpViewIndex,
       "mscVrSnmpViewSubtreeIndex": mscVrSnmpViewSubtreeIndex,
       "mscVrSnmpViewProvTable": mscVrSnmpViewProvTable,
       "mscVrSnmpViewProvEntry": mscVrSnmpViewProvEntry,
       "mscVrSnmpViewMask": mscVrSnmpViewMask,
       "mscVrSnmpViewType": mscVrSnmpViewType,
       "mscVrSnmpViewRowStorageType": mscVrSnmpViewRowStorageType,
       "mscVrSnmpViewStdRowStatus": mscVrSnmpViewStdRowStatus,
       "mscVrSnmpOr": mscVrSnmpOr,
       "mscVrSnmpOrRowStatusTable": mscVrSnmpOrRowStatusTable,
       "mscVrSnmpOrRowStatusEntry": mscVrSnmpOrRowStatusEntry,
       "mscVrSnmpOrRowStatus": mscVrSnmpOrRowStatus,
       "mscVrSnmpOrComponentName": mscVrSnmpOrComponentName,
       "mscVrSnmpOrStorageType": mscVrSnmpOrStorageType,
       "mscVrSnmpOrIndex": mscVrSnmpOrIndex,
       "mscVrSnmpOrOrTable": mscVrSnmpOrOrTable,
       "mscVrSnmpOrOrEntry": mscVrSnmpOrOrEntry,
       "mscVrSnmpOrId": mscVrSnmpOrId,
       "mscVrSnmpOrDescr": mscVrSnmpOrDescr,
       "mscVrSnmpV2Stats": mscVrSnmpV2Stats,
       "mscVrSnmpV2StatsRowStatusTable": mscVrSnmpV2StatsRowStatusTable,
       "mscVrSnmpV2StatsRowStatusEntry": mscVrSnmpV2StatsRowStatusEntry,
       "mscVrSnmpV2StatsRowStatus": mscVrSnmpV2StatsRowStatus,
       "mscVrSnmpV2StatsComponentName": mscVrSnmpV2StatsComponentName,
       "mscVrSnmpV2StatsStorageType": mscVrSnmpV2StatsStorageType,
       "mscVrSnmpV2StatsIndex": mscVrSnmpV2StatsIndex,
       "mscVrSnmpV2StatsStatsTable": mscVrSnmpV2StatsStatsTable,
       "mscVrSnmpV2StatsStatsEntry": mscVrSnmpV2StatsStatsEntry,
       "mscVrSnmpV2StatsPackets": mscVrSnmpV2StatsPackets,
       "mscVrSnmpV2StatsEncodingErrors": mscVrSnmpV2StatsEncodingErrors,
       "mscVrSnmpV2StatsUnknownSrcParties": mscVrSnmpV2StatsUnknownSrcParties,
       "mscVrSnmpV2StatsBadAuths": mscVrSnmpV2StatsBadAuths,
       "mscVrSnmpV2StatsNotInLifetime": mscVrSnmpV2StatsNotInLifetime,
       "mscVrSnmpV2StatsWrongDigestValues": mscVrSnmpV2StatsWrongDigestValues,
       "mscVrSnmpV2StatsUnknownContexts": mscVrSnmpV2StatsUnknownContexts,
       "mscVrSnmpV2StatsBadOperations": mscVrSnmpV2StatsBadOperations,
       "mscVrSnmpV2StatsSilentDrops": mscVrSnmpV2StatsSilentDrops,
       "mscVrSnmpV1Stats": mscVrSnmpV1Stats,
       "mscVrSnmpV1StatsRowStatusTable": mscVrSnmpV1StatsRowStatusTable,
       "mscVrSnmpV1StatsRowStatusEntry": mscVrSnmpV1StatsRowStatusEntry,
       "mscVrSnmpV1StatsRowStatus": mscVrSnmpV1StatsRowStatus,
       "mscVrSnmpV1StatsComponentName": mscVrSnmpV1StatsComponentName,
       "mscVrSnmpV1StatsStorageType": mscVrSnmpV1StatsStorageType,
       "mscVrSnmpV1StatsIndex": mscVrSnmpV1StatsIndex,
       "mscVrSnmpV1StatsStatsTable": mscVrSnmpV1StatsStatsTable,
       "mscVrSnmpV1StatsStatsEntry": mscVrSnmpV1StatsStatsEntry,
       "mscVrSnmpV1StatsBadCommunityNames": mscVrSnmpV1StatsBadCommunityNames,
       "mscVrSnmpV1StatsBadCommunityUses": mscVrSnmpV1StatsBadCommunityUses,
       "mscVrSnmpMibIIStats": mscVrSnmpMibIIStats,
       "mscVrSnmpMibIIStatsRowStatusTable": mscVrSnmpMibIIStatsRowStatusTable,
       "mscVrSnmpMibIIStatsRowStatusEntry": mscVrSnmpMibIIStatsRowStatusEntry,
       "mscVrSnmpMibIIStatsRowStatus": mscVrSnmpMibIIStatsRowStatus,
       "mscVrSnmpMibIIStatsComponentName": mscVrSnmpMibIIStatsComponentName,
       "mscVrSnmpMibIIStatsStorageType": mscVrSnmpMibIIStatsStorageType,
       "mscVrSnmpMibIIStatsIndex": mscVrSnmpMibIIStatsIndex,
       "mscVrSnmpMibIIStatsStatsTable": mscVrSnmpMibIIStatsStatsTable,
       "mscVrSnmpMibIIStatsStatsEntry": mscVrSnmpMibIIStatsStatsEntry,
       "mscVrSnmpMibIIStatsInPackets": mscVrSnmpMibIIStatsInPackets,
       "mscVrSnmpMibIIStatsInBadCommunityNames": mscVrSnmpMibIIStatsInBadCommunityNames,
       "mscVrSnmpMibIIStatsInBadCommunityUses": mscVrSnmpMibIIStatsInBadCommunityUses,
       "mscVrSnmpMibIIStatsInAsnParseErrs": mscVrSnmpMibIIStatsInAsnParseErrs,
       "mscVrSnmpMibIIStatsOutPackets": mscVrSnmpMibIIStatsOutPackets,
       "mscVrSnmpMibIIStatsInBadVersions": mscVrSnmpMibIIStatsInBadVersions,
       "mscVrSnmpMibIIStatsInTotalReqVars": mscVrSnmpMibIIStatsInTotalReqVars,
       "mscVrSnmpMibIIStatsInTotalSetVars": mscVrSnmpMibIIStatsInTotalSetVars,
       "mscVrSnmpMibIIStatsInGetRequests": mscVrSnmpMibIIStatsInGetRequests,
       "mscVrSnmpMibIIStatsInGetNexts": mscVrSnmpMibIIStatsInGetNexts,
       "mscVrSnmpMibIIStatsInSetRequests": mscVrSnmpMibIIStatsInSetRequests,
       "mscVrSnmpMibIIStatsOutTooBigs": mscVrSnmpMibIIStatsOutTooBigs,
       "mscVrSnmpMibIIStatsOutNoSuchNames": mscVrSnmpMibIIStatsOutNoSuchNames,
       "mscVrSnmpMibIIStatsOutBadValues": mscVrSnmpMibIIStatsOutBadValues,
       "mscVrSnmpMibIIStatsOutGenErrs": mscVrSnmpMibIIStatsOutGenErrs,
       "mscVrSnmpMibIIStatsOutGetResponses": mscVrSnmpMibIIStatsOutGetResponses,
       "mscVrSnmpMibIIStatsOutTraps": mscVrSnmpMibIIStatsOutTraps,
       "mscVrSnmpProvTable": mscVrSnmpProvTable,
       "mscVrSnmpProvEntry": mscVrSnmpProvEntry,
       "mscVrSnmpV1EnableAuthenTraps": mscVrSnmpV1EnableAuthenTraps,
       "mscVrSnmpV2EnableAuthenTraps": mscVrSnmpV2EnableAuthenTraps,
       "mscVrSnmpAlarmsAsTraps": mscVrSnmpAlarmsAsTraps,
       "mscVrSnmpIpStack": mscVrSnmpIpStack,
       "mscVrSnmpCidInEntTraps": mscVrSnmpCidInEntTraps,
       "mscVrSnmpStateTable": mscVrSnmpStateTable,
       "mscVrSnmpStateEntry": mscVrSnmpStateEntry,
       "mscVrSnmpAdminState": mscVrSnmpAdminState,
       "mscVrSnmpOperationalState": mscVrSnmpOperationalState,
       "mscVrSnmpUsageState": mscVrSnmpUsageState,
       "mscVrSnmpAvailabilityStatus": mscVrSnmpAvailabilityStatus,
       "mscVrSnmpProceduralStatus": mscVrSnmpProceduralStatus,
       "mscVrSnmpControlStatus": mscVrSnmpControlStatus,
       "mscVrSnmpAlarmStatus": mscVrSnmpAlarmStatus,
       "mscVrSnmpStandbyStatus": mscVrSnmpStandbyStatus,
       "mscVrSnmpUnknownStatus": mscVrSnmpUnknownStatus,
       "mscVrSnmpStatsTable": mscVrSnmpStatsTable,
       "mscVrSnmpStatsEntry": mscVrSnmpStatsEntry,
       "mscVrSnmpLastOrChange": mscVrSnmpLastOrChange,
       "mscVrSnmpTrapsProcessed": mscVrSnmpTrapsProcessed,
       "mscVrSnmpTrapsDiscarded": mscVrSnmpTrapsDiscarded,
       "mscVrSnmpLastAuthFailure": mscVrSnmpLastAuthFailure,
       "mscVrSnmpMgrOfLastAuthFailure": mscVrSnmpMgrOfLastAuthFailure,
       "mscVrInitSnmpConfig": mscVrInitSnmpConfig,
       "mscVrInitSnmpConfigRowStatusTable": mscVrInitSnmpConfigRowStatusTable,
       "mscVrInitSnmpConfigRowStatusEntry": mscVrInitSnmpConfigRowStatusEntry,
       "mscVrInitSnmpConfigRowStatus": mscVrInitSnmpConfigRowStatus,
       "mscVrInitSnmpConfigComponentName": mscVrInitSnmpConfigComponentName,
       "mscVrInitSnmpConfigStorageType": mscVrInitSnmpConfigStorageType,
       "mscVrInitSnmpConfigIndex": mscVrInitSnmpConfigIndex,
       "mscVrInitSnmpConfigProvTable": mscVrInitSnmpConfigProvTable,
       "mscVrInitSnmpConfigProvEntry": mscVrInitSnmpConfigProvEntry,
       "mscVrInitSnmpConfigAgentAddress": mscVrInitSnmpConfigAgentAddress,
       "mscVrInitSnmpConfigManagerAddress": mscVrInitSnmpConfigManagerAddress,
       "baseSnmpMIB": baseSnmpMIB,
       "baseSnmpGroup": baseSnmpGroup,
       "baseSnmpGroupCA": baseSnmpGroupCA,
       "baseSnmpGroupCA02": baseSnmpGroupCA02,
       "baseSnmpGroupCA02A": baseSnmpGroupCA02A,
       "baseSnmpCapabilities": baseSnmpCapabilities,
       "baseSnmpCapabilitiesCA": baseSnmpCapabilitiesCA,
       "baseSnmpCapabilitiesCA02": baseSnmpCapabilitiesCA02,
       "baseSnmpCapabilitiesCA02A": baseSnmpCapabilitiesCA02A}
)
