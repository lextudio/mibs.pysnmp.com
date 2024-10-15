# SNMP MIB module (Nortel-MsCarrier-MscPassport-LaneClientMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-LaneClientMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:45 2024
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

(Counter32,
 DisplayString,
 Integer32,
 InterfaceIndex,
 MacAddress,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DashedHexString,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DashedHexString",
    "HexString",
    "Link",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscLec_ObjectIdentity = ObjectIdentity
mscLec = _MscLec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124)
)
_MscLecRowStatusTable_Object = MibTable
mscLecRowStatusTable = _MscLecRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1)
)
if mibBuilder.loadTexts:
    mscLecRowStatusTable.setStatus("mandatory")
_MscLecRowStatusEntry_Object = MibTableRow
mscLecRowStatusEntry = _MscLecRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1, 1)
)
mscLecRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecRowStatusEntry.setStatus("mandatory")
_MscLecRowStatus_Type = RowStatus
_MscLecRowStatus_Object = MibTableColumn
mscLecRowStatus = _MscLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1, 1, 1),
    _MscLecRowStatus_Type()
)
mscLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecRowStatus.setStatus("mandatory")
_MscLecComponentName_Type = DisplayString
_MscLecComponentName_Object = MibTableColumn
mscLecComponentName = _MscLecComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1, 1, 2),
    _MscLecComponentName_Type()
)
mscLecComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecComponentName.setStatus("mandatory")
_MscLecStorageType_Type = StorageType
_MscLecStorageType_Object = MibTableColumn
mscLecStorageType = _MscLecStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1, 1, 4),
    _MscLecStorageType_Type()
)
mscLecStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecStorageType.setStatus("mandatory")


class _MscLecIndex_Type(Integer32):
    """Custom type mscLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscLecIndex_Type.__name__ = "Integer32"
_MscLecIndex_Object = MibTableColumn
mscLecIndex = _MscLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 1, 1, 10),
    _MscLecIndex_Type()
)
mscLecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLecIndex.setStatus("mandatory")
_MscLecLeArp_ObjectIdentity = ObjectIdentity
mscLecLeArp = _MscLecLeArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2)
)
_MscLecLeArpRowStatusTable_Object = MibTable
mscLecLeArpRowStatusTable = _MscLecLeArpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1)
)
if mibBuilder.loadTexts:
    mscLecLeArpRowStatusTable.setStatus("mandatory")
_MscLecLeArpRowStatusEntry_Object = MibTableRow
mscLecLeArpRowStatusEntry = _MscLecLeArpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1, 1)
)
mscLecLeArpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecLeArpIndex"),
)
if mibBuilder.loadTexts:
    mscLecLeArpRowStatusEntry.setStatus("mandatory")
_MscLecLeArpRowStatus_Type = RowStatus
_MscLecLeArpRowStatus_Object = MibTableColumn
mscLecLeArpRowStatus = _MscLecLeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1, 1, 1),
    _MscLecLeArpRowStatus_Type()
)
mscLecLeArpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpRowStatus.setStatus("mandatory")
_MscLecLeArpComponentName_Type = DisplayString
_MscLecLeArpComponentName_Object = MibTableColumn
mscLecLeArpComponentName = _MscLecLeArpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1, 1, 2),
    _MscLecLeArpComponentName_Type()
)
mscLecLeArpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpComponentName.setStatus("mandatory")
_MscLecLeArpStorageType_Type = StorageType
_MscLecLeArpStorageType_Object = MibTableColumn
mscLecLeArpStorageType = _MscLecLeArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1, 1, 4),
    _MscLecLeArpStorageType_Type()
)
mscLecLeArpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpStorageType.setStatus("mandatory")


class _MscLecLeArpIndex_Type(DashedHexString):
    """Custom type mscLecLeArpIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLecLeArpIndex_Type.__name__ = "DashedHexString"
_MscLecLeArpIndex_Object = MibTableColumn
mscLecLeArpIndex = _MscLecLeArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 1, 1, 10),
    _MscLecLeArpIndex_Type()
)
mscLecLeArpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLecLeArpIndex.setStatus("mandatory")
_MscLecLeArpOperTable_Object = MibTable
mscLecLeArpOperTable = _MscLecLeArpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 10)
)
if mibBuilder.loadTexts:
    mscLecLeArpOperTable.setStatus("mandatory")
_MscLecLeArpOperEntry_Object = MibTableRow
mscLecLeArpOperEntry = _MscLecLeArpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 10, 1)
)
mscLecLeArpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecLeArpIndex"),
)
if mibBuilder.loadTexts:
    mscLecLeArpOperEntry.setStatus("mandatory")


class _MscLecLeArpAtmAddress_Type(HexString):
    """Custom type mscLecLeArpAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscLecLeArpAtmAddress_Type.__name__ = "HexString"
_MscLecLeArpAtmAddress_Object = MibTableColumn
mscLecLeArpAtmAddress = _MscLecLeArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 10, 1, 1),
    _MscLecLeArpAtmAddress_Type()
)
mscLecLeArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpAtmAddress.setStatus("mandatory")


class _MscLecLeArpIsRemoteAddress_Type(Integer32):
    """Custom type mscLecLeArpIsRemoteAddress based on Integer32"""
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


_MscLecLeArpIsRemoteAddress_Type.__name__ = "Integer32"
_MscLecLeArpIsRemoteAddress_Object = MibTableColumn
mscLecLeArpIsRemoteAddress = _MscLecLeArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 10, 1, 2),
    _MscLecLeArpIsRemoteAddress_Type()
)
mscLecLeArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpIsRemoteAddress.setStatus("mandatory")


class _MscLecLeArpConnectionId_Type(Unsigned32):
    """Custom type mscLecLeArpConnectionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_MscLecLeArpConnectionId_Type.__name__ = "Unsigned32"
_MscLecLeArpConnectionId_Object = MibTableColumn
mscLecLeArpConnectionId = _MscLecLeArpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 2, 10, 1, 3),
    _MscLecLeArpConnectionId_Type()
)
mscLecLeArpConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLeArpConnectionId.setStatus("mandatory")
_MscLecConn_ObjectIdentity = ObjectIdentity
mscLecConn = _MscLecConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3)
)
_MscLecConnRowStatusTable_Object = MibTable
mscLecConnRowStatusTable = _MscLecConnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1)
)
if mibBuilder.loadTexts:
    mscLecConnRowStatusTable.setStatus("mandatory")
_MscLecConnRowStatusEntry_Object = MibTableRow
mscLecConnRowStatusEntry = _MscLecConnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1, 1)
)
mscLecConnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnIndex"),
)
if mibBuilder.loadTexts:
    mscLecConnRowStatusEntry.setStatus("mandatory")
_MscLecConnRowStatus_Type = RowStatus
_MscLecConnRowStatus_Object = MibTableColumn
mscLecConnRowStatus = _MscLecConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1, 1, 1),
    _MscLecConnRowStatus_Type()
)
mscLecConnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnRowStatus.setStatus("mandatory")
_MscLecConnComponentName_Type = DisplayString
_MscLecConnComponentName_Object = MibTableColumn
mscLecConnComponentName = _MscLecConnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1, 1, 2),
    _MscLecConnComponentName_Type()
)
mscLecConnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnComponentName.setStatus("mandatory")
_MscLecConnStorageType_Type = StorageType
_MscLecConnStorageType_Object = MibTableColumn
mscLecConnStorageType = _MscLecConnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1, 1, 4),
    _MscLecConnStorageType_Type()
)
mscLecConnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnStorageType.setStatus("mandatory")


class _MscLecConnIndex_Type(Integer32):
    """Custom type mscLecConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_MscLecConnIndex_Type.__name__ = "Integer32"
_MscLecConnIndex_Object = MibTableColumn
mscLecConnIndex = _MscLecConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 1, 1, 10),
    _MscLecConnIndex_Type()
)
mscLecConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLecConnIndex.setStatus("mandatory")
_MscLecConnAtmCon_ObjectIdentity = ObjectIdentity
mscLecConnAtmCon = _MscLecConnAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2)
)
_MscLecConnAtmConRowStatusTable_Object = MibTable
mscLecConnAtmConRowStatusTable = _MscLecConnAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscLecConnAtmConRowStatusTable.setStatus("mandatory")
_MscLecConnAtmConRowStatusEntry_Object = MibTableRow
mscLecConnAtmConRowStatusEntry = _MscLecConnAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1, 1)
)
mscLecConnAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscLecConnAtmConRowStatusEntry.setStatus("mandatory")
_MscLecConnAtmConRowStatus_Type = RowStatus
_MscLecConnAtmConRowStatus_Object = MibTableColumn
mscLecConnAtmConRowStatus = _MscLecConnAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1, 1, 1),
    _MscLecConnAtmConRowStatus_Type()
)
mscLecConnAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnAtmConRowStatus.setStatus("mandatory")
_MscLecConnAtmConComponentName_Type = DisplayString
_MscLecConnAtmConComponentName_Object = MibTableColumn
mscLecConnAtmConComponentName = _MscLecConnAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1, 1, 2),
    _MscLecConnAtmConComponentName_Type()
)
mscLecConnAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnAtmConComponentName.setStatus("mandatory")
_MscLecConnAtmConStorageType_Type = StorageType
_MscLecConnAtmConStorageType_Object = MibTableColumn
mscLecConnAtmConStorageType = _MscLecConnAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1, 1, 4),
    _MscLecConnAtmConStorageType_Type()
)
mscLecConnAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnAtmConStorageType.setStatus("mandatory")
_MscLecConnAtmConIndex_Type = NonReplicated
_MscLecConnAtmConIndex_Object = MibTableColumn
mscLecConnAtmConIndex = _MscLecConnAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 1, 1, 10),
    _MscLecConnAtmConIndex_Type()
)
mscLecConnAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLecConnAtmConIndex.setStatus("mandatory")
_MscLecConnAtmConOperTable_Object = MibTable
mscLecConnAtmConOperTable = _MscLecConnAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscLecConnAtmConOperTable.setStatus("mandatory")
_MscLecConnAtmConOperEntry_Object = MibTableRow
mscLecConnAtmConOperEntry = _MscLecConnAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 10, 1)
)
mscLecConnAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscLecConnAtmConOperEntry.setStatus("mandatory")
_MscLecConnAtmConNextHop_Type = RowPointer
_MscLecConnAtmConNextHop_Object = MibTableColumn
mscLecConnAtmConNextHop = _MscLecConnAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 2, 10, 1, 1),
    _MscLecConnAtmConNextHop_Type()
)
mscLecConnAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnAtmConNextHop.setStatus("mandatory")
_MscLecConnOperTable_Object = MibTable
mscLecConnOperTable = _MscLecConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 10)
)
if mibBuilder.loadTexts:
    mscLecConnOperTable.setStatus("mandatory")
_MscLecConnOperEntry_Object = MibTableRow
mscLecConnOperEntry = _MscLecConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 10, 1)
)
mscLecConnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnIndex"),
)
if mibBuilder.loadTexts:
    mscLecConnOperEntry.setStatus("mandatory")


class _MscLecConnRemoteAtmAddress_Type(HexString):
    """Custom type mscLecConnRemoteAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MscLecConnRemoteAtmAddress_Type.__name__ = "HexString"
_MscLecConnRemoteAtmAddress_Object = MibTableColumn
mscLecConnRemoteAtmAddress = _MscLecConnRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 10, 1, 1),
    _MscLecConnRemoteAtmAddress_Type()
)
mscLecConnRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnRemoteAtmAddress.setStatus("mandatory")


class _MscLecConnAge_Type(Unsigned32):
    """Custom type mscLecConnAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscLecConnAge_Type.__name__ = "Unsigned32"
_MscLecConnAge_Object = MibTableColumn
mscLecConnAge = _MscLecConnAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 10, 1, 2),
    _MscLecConnAge_Type()
)
mscLecConnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnAge.setStatus("mandatory")


class _MscLecConnType_Type(Integer32):
    """Custom type mscLecConnType based on Integer32"""
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
        *(("configurationDirectVcc", 1),
          ("controlDirectVcc", 2),
          ("controlDistributeVcc", 3),
          ("dataDirectVcc", 4),
          ("defaultMulticastSendVcc", 5),
          ("multicastForward", 6))
    )


_MscLecConnType_Type.__name__ = "Integer32"
_MscLecConnType_Object = MibTableColumn
mscLecConnType = _MscLecConnType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 10, 1, 3),
    _MscLecConnType_Type()
)
mscLecConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnType.setStatus("mandatory")
_MscLecConnStatsTable_Object = MibTable
mscLecConnStatsTable = _MscLecConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 11)
)
if mibBuilder.loadTexts:
    mscLecConnStatsTable.setStatus("mandatory")
_MscLecConnStatsEntry_Object = MibTableRow
mscLecConnStatsEntry = _MscLecConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 11, 1)
)
mscLecConnStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecConnIndex"),
)
if mibBuilder.loadTexts:
    mscLecConnStatsEntry.setStatus("mandatory")
_MscLecConnOutFrames_Type = Counter32
_MscLecConnOutFrames_Object = MibTableColumn
mscLecConnOutFrames = _MscLecConnOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 11, 1, 1),
    _MscLecConnOutFrames_Type()
)
mscLecConnOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnOutFrames.setStatus("mandatory")
_MscLecConnInFrames_Type = Counter32
_MscLecConnInFrames_Object = MibTableColumn
mscLecConnInFrames = _MscLecConnInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 3, 11, 1, 2),
    _MscLecConnInFrames_Type()
)
mscLecConnInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConnInFrames.setStatus("mandatory")
_MscLecCidDataTable_Object = MibTable
mscLecCidDataTable = _MscLecCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 10)
)
if mibBuilder.loadTexts:
    mscLecCidDataTable.setStatus("mandatory")
_MscLecCidDataEntry_Object = MibTableRow
mscLecCidDataEntry = _MscLecCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 10, 1)
)
mscLecCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecCidDataEntry.setStatus("mandatory")


class _MscLecCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLecCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLecCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLecCustomerIdentifier_Object = MibTableColumn
mscLecCustomerIdentifier = _MscLecCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 10, 1, 1),
    _MscLecCustomerIdentifier_Type()
)
mscLecCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecCustomerIdentifier.setStatus("mandatory")
_MscLecIfEntryTable_Object = MibTable
mscLecIfEntryTable = _MscLecIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 11)
)
if mibBuilder.loadTexts:
    mscLecIfEntryTable.setStatus("mandatory")
_MscLecIfEntryEntry_Object = MibTableRow
mscLecIfEntryEntry = _MscLecIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 11, 1)
)
mscLecIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecIfEntryEntry.setStatus("mandatory")


class _MscLecIfAdminStatus_Type(Integer32):
    """Custom type mscLecIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscLecIfAdminStatus_Type.__name__ = "Integer32"
_MscLecIfAdminStatus_Object = MibTableColumn
mscLecIfAdminStatus = _MscLecIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 11, 1, 1),
    _MscLecIfAdminStatus_Type()
)
mscLecIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecIfAdminStatus.setStatus("mandatory")


class _MscLecIfIndex_Type(InterfaceIndex):
    """Custom type mscLecIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLecIfIndex_Type.__name__ = "InterfaceIndex"
_MscLecIfIndex_Object = MibTableColumn
mscLecIfIndex = _MscLecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 11, 1, 2),
    _MscLecIfIndex_Type()
)
mscLecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecIfIndex.setStatus("mandatory")
_MscLecMpTable_Object = MibTable
mscLecMpTable = _MscLecMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 12)
)
if mibBuilder.loadTexts:
    mscLecMpTable.setStatus("mandatory")
_MscLecMpEntry_Object = MibTableRow
mscLecMpEntry = _MscLecMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 12, 1)
)
mscLecMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecMpEntry.setStatus("mandatory")
_MscLecLinkToProtocolPort_Type = Link
_MscLecLinkToProtocolPort_Object = MibTableColumn
mscLecLinkToProtocolPort = _MscLecLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 12, 1, 1),
    _MscLecLinkToProtocolPort_Type()
)
mscLecLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecLinkToProtocolPort.setStatus("mandatory")
_MscLecProvTable_Object = MibTable
mscLecProvTable = _MscLecProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13)
)
if mibBuilder.loadTexts:
    mscLecProvTable.setStatus("mandatory")
_MscLecProvEntry_Object = MibTableRow
mscLecProvEntry = _MscLecProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1)
)
mscLecProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecProvEntry.setStatus("mandatory")


class _MscLecLanType_Type(Integer32):
    """Custom type mscLecLanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("unspecified", 1))
    )


_MscLecLanType_Type.__name__ = "Integer32"
_MscLecLanType_Object = MibTableColumn
mscLecLanType = _MscLecLanType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 1),
    _MscLecLanType_Type()
)
mscLecLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecLanType.setStatus("mandatory")


class _MscLecMaxFrameSize_Type(Integer32):
    """Custom type mscLecMaxFrameSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1516,
              1580,
              4544,
              9234,
              18190)
        )
    )
    namedValues = NamedValues(
        *(("n1516", 1516),
          ("n1580", 1580),
          ("n18190", 18190),
          ("n4544", 4544),
          ("n9234", 9234),
          ("unspecified", 0))
    )


_MscLecMaxFrameSize_Type.__name__ = "Integer32"
_MscLecMaxFrameSize_Object = MibTableColumn
mscLecMaxFrameSize = _MscLecMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 2),
    _MscLecMaxFrameSize_Type()
)
mscLecMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecMaxFrameSize.setStatus("mandatory")


class _MscLecLanName_Type(AsciiString):
    """Custom type mscLecLanName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscLecLanName_Type.__name__ = "AsciiString"
_MscLecLanName_Object = MibTableColumn
mscLecLanName = _MscLecLanName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 3),
    _MscLecLanName_Type()
)
mscLecLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecLanName.setStatus("mandatory")


class _MscLecV2Capable_Type(Integer32):
    """Custom type mscLecV2Capable based on Integer32"""
    defaultValue = 1

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


_MscLecV2Capable_Type.__name__ = "Integer32"
_MscLecV2Capable_Object = MibTableColumn
mscLecV2Capable = _MscLecV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 4),
    _MscLecV2Capable_Type()
)
mscLecV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecV2Capable.setStatus("mandatory")


class _MscLecLecsAddress_Type(HexString):
    """Custom type mscLecLecsAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLecLecsAddress_Type.__name__ = "HexString"
_MscLecLecsAddress_Object = MibTableColumn
mscLecLecsAddress = _MscLecLecsAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 5),
    _MscLecLecsAddress_Type()
)
mscLecLecsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecLecsAddress.setStatus("mandatory")


class _MscLecLesAddress_Type(HexString):
    """Custom type mscLecLesAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLecLesAddress_Type.__name__ = "HexString"
_MscLecLesAddress_Object = MibTableColumn
mscLecLesAddress = _MscLecLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 6),
    _MscLecLesAddress_Type()
)
mscLecLesAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecLesAddress.setStatus("mandatory")


class _MscLecMaxDataSvcs_Type(Unsigned32):
    """Custom type mscLecMaxDataSvcs based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1018),
    )


_MscLecMaxDataSvcs_Type.__name__ = "Unsigned32"
_MscLecMaxDataSvcs_Object = MibTableColumn
mscLecMaxDataSvcs = _MscLecMaxDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 7),
    _MscLecMaxDataSvcs_Type()
)
mscLecMaxDataSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecMaxDataSvcs.setStatus("mandatory")


class _MscLecMaxArpEntries_Type(Unsigned32):
    """Custom type mscLecMaxArpEntries based on Unsigned32"""
    defaultValue = 5120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 10240),
    )


_MscLecMaxArpEntries_Type.__name__ = "Unsigned32"
_MscLecMaxArpEntries_Object = MibTableColumn
mscLecMaxArpEntries = _MscLecMaxArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 8),
    _MscLecMaxArpEntries_Type()
)
mscLecMaxArpEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecMaxArpEntries.setStatus("mandatory")
_MscLecIlsForwarder_Type = Link
_MscLecIlsForwarder_Object = MibTableColumn
mscLecIlsForwarder = _MscLecIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 13, 1, 9),
    _MscLecIlsForwarder_Type()
)
mscLecIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLecIlsForwarder.setStatus("mandatory")
_MscLecStateTable_Object = MibTable
mscLecStateTable = _MscLecStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 15)
)
if mibBuilder.loadTexts:
    mscLecStateTable.setStatus("mandatory")
_MscLecStateEntry_Object = MibTableRow
mscLecStateEntry = _MscLecStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 15, 1)
)
mscLecStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecStateEntry.setStatus("mandatory")


class _MscLecAdminState_Type(Integer32):
    """Custom type mscLecAdminState based on Integer32"""
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


_MscLecAdminState_Type.__name__ = "Integer32"
_MscLecAdminState_Object = MibTableColumn
mscLecAdminState = _MscLecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 15, 1, 1),
    _MscLecAdminState_Type()
)
mscLecAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecAdminState.setStatus("mandatory")


class _MscLecOperationalState_Type(Integer32):
    """Custom type mscLecOperationalState based on Integer32"""
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


_MscLecOperationalState_Type.__name__ = "Integer32"
_MscLecOperationalState_Object = MibTableColumn
mscLecOperationalState = _MscLecOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 15, 1, 2),
    _MscLecOperationalState_Type()
)
mscLecOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecOperationalState.setStatus("mandatory")


class _MscLecUsageState_Type(Integer32):
    """Custom type mscLecUsageState based on Integer32"""
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


_MscLecUsageState_Type.__name__ = "Integer32"
_MscLecUsageState_Object = MibTableColumn
mscLecUsageState = _MscLecUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 15, 1, 3),
    _MscLecUsageState_Type()
)
mscLecUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecUsageState.setStatus("mandatory")
_MscLecOperStatusTable_Object = MibTable
mscLecOperStatusTable = _MscLecOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 16)
)
if mibBuilder.loadTexts:
    mscLecOperStatusTable.setStatus("mandatory")
_MscLecOperStatusEntry_Object = MibTableRow
mscLecOperStatusEntry = _MscLecOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 16, 1)
)
mscLecOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecOperStatusEntry.setStatus("mandatory")


class _MscLecSnmpOperStatus_Type(Integer32):
    """Custom type mscLecSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscLecSnmpOperStatus_Type.__name__ = "Integer32"
_MscLecSnmpOperStatus_Object = MibTableColumn
mscLecSnmpOperStatus = _MscLecSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 16, 1, 1),
    _MscLecSnmpOperStatus_Type()
)
mscLecSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecSnmpOperStatus.setStatus("mandatory")
_MscLecOperTable_Object = MibTable
mscLecOperTable = _MscLecOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17)
)
if mibBuilder.loadTexts:
    mscLecOperTable.setStatus("mandatory")
_MscLecOperEntry_Object = MibTableRow
mscLecOperEntry = _MscLecOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1)
)
mscLecOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecOperEntry.setStatus("mandatory")


class _MscLecActualLanType_Type(Integer32):
    """Custom type mscLecActualLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("unspecified", 1))
    )


_MscLecActualLanType_Type.__name__ = "Integer32"
_MscLecActualLanType_Object = MibTableColumn
mscLecActualLanType = _MscLecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 1),
    _MscLecActualLanType_Type()
)
mscLecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualLanType.setStatus("mandatory")


class _MscLecActualMaxFrameSize_Type(Integer32):
    """Custom type mscLecActualMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1516,
              1580,
              4544,
              9234,
              18190)
        )
    )
    namedValues = NamedValues(
        *(("n1516", 1516),
          ("n1580", 1580),
          ("n18190", 18190),
          ("n4544", 4544),
          ("n9234", 9234),
          ("unspecified", 0))
    )


_MscLecActualMaxFrameSize_Type.__name__ = "Integer32"
_MscLecActualMaxFrameSize_Object = MibTableColumn
mscLecActualMaxFrameSize = _MscLecActualMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 2),
    _MscLecActualMaxFrameSize_Type()
)
mscLecActualMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualMaxFrameSize.setStatus("mandatory")


class _MscLecActualLanName_Type(AsciiString):
    """Custom type mscLecActualLanName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscLecActualLanName_Type.__name__ = "AsciiString"
_MscLecActualLanName_Object = MibTableColumn
mscLecActualLanName = _MscLecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 3),
    _MscLecActualLanName_Type()
)
mscLecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualLanName.setStatus("mandatory")


class _MscLecElanId_Type(Unsigned32):
    """Custom type mscLecElanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLecElanId_Type.__name__ = "Unsigned32"
_MscLecElanId_Object = MibTableColumn
mscLecElanId = _MscLecElanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 4),
    _MscLecElanId_Type()
)
mscLecElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecElanId.setStatus("mandatory")


class _MscLecActualV2Capable_Type(Integer32):
    """Custom type mscLecActualV2Capable based on Integer32"""
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


_MscLecActualV2Capable_Type.__name__ = "Integer32"
_MscLecActualV2Capable_Object = MibTableColumn
mscLecActualV2Capable = _MscLecActualV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 5),
    _MscLecActualV2Capable_Type()
)
mscLecActualV2Capable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualV2Capable.setStatus("mandatory")


class _MscLecConfigurationSource_Type(Integer32):
    """Custom type mscLecConfigurationSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("didNotUseLecs", 5),
          ("gotLecsAddressViaIlmi", 2),
          ("usedLecsPvc", 4),
          ("usedProvisionedLecsAddress", 1),
          ("usedWellKnownLecsAddress", 3))
    )


_MscLecConfigurationSource_Type.__name__ = "Integer32"
_MscLecConfigurationSource_Object = MibTableColumn
mscLecConfigurationSource = _MscLecConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 6),
    _MscLecConfigurationSource_Type()
)
mscLecConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecConfigurationSource.setStatus("mandatory")


class _MscLecActualLecsAddress_Type(HexString):
    """Custom type mscLecActualLecsAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLecActualLecsAddress_Type.__name__ = "HexString"
_MscLecActualLecsAddress_Object = MibTableColumn
mscLecActualLecsAddress = _MscLecActualLecsAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 7),
    _MscLecActualLecsAddress_Type()
)
mscLecActualLecsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualLecsAddress.setStatus("mandatory")


class _MscLecActualLesAddress_Type(HexString):
    """Custom type mscLecActualLesAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLecActualLesAddress_Type.__name__ = "HexString"
_MscLecActualLesAddress_Object = MibTableColumn
mscLecActualLesAddress = _MscLecActualLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 8),
    _MscLecActualLesAddress_Type()
)
mscLecActualLesAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecActualLesAddress.setStatus("mandatory")


class _MscLecAtmAddress_Type(HexString):
    """Custom type mscLecAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLecAtmAddress_Type.__name__ = "HexString"
_MscLecAtmAddress_Object = MibTableColumn
mscLecAtmAddress = _MscLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 9),
    _MscLecAtmAddress_Type()
)
mscLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecAtmAddress.setStatus("mandatory")


class _MscLecMacAddress_Type(MacAddress):
    """Custom type mscLecMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLecMacAddress_Type.__name__ = "MacAddress"
_MscLecMacAddress_Object = MibTableColumn
mscLecMacAddress = _MscLecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 10),
    _MscLecMacAddress_Type()
)
mscLecMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecMacAddress.setStatus("mandatory")


class _MscLecLecId_Type(Unsigned32):
    """Custom type mscLecLecId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_MscLecLecId_Type.__name__ = "Unsigned32"
_MscLecLecId_Object = MibTableColumn
mscLecLecId = _MscLecLecId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 11),
    _MscLecLecId_Type()
)
mscLecLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLecId.setStatus("mandatory")


class _MscLecInterfaceState_Type(Integer32):
    """Custom type mscLecInterfaceState based on Integer32"""
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_MscLecInterfaceState_Type.__name__ = "Integer32"
_MscLecInterfaceState_Object = MibTableColumn
mscLecInterfaceState = _MscLecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 12),
    _MscLecInterfaceState_Type()
)
mscLecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecInterfaceState.setStatus("mandatory")


class _MscLecLastFailureResponseCode_Type(Integer32):
    """Custom type mscLecLastFailureResponseCode based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 9),
          ("duplicateAtmAddress", 7),
          ("duplicateLanDestination", 6),
          ("insufficientInformation", 15),
          ("insufficientResources", 8),
          ("invalidAtmAddress", 12),
          ("invalidLanDestination", 11),
          ("invalidRequestParameters", 5),
          ("invalidRequesterId", 10),
          ("leConfigureError", 14),
          ("noConfiguration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4))
    )


_MscLecLastFailureResponseCode_Type.__name__ = "Integer32"
_MscLecLastFailureResponseCode_Object = MibTableColumn
mscLecLastFailureResponseCode = _MscLecLastFailureResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 13),
    _MscLecLastFailureResponseCode_Type()
)
mscLecLastFailureResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLastFailureResponseCode.setStatus("mandatory")


class _MscLecLastFailureState_Type(Integer32):
    """Custom type mscLecLastFailureState based on Integer32"""
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_MscLecLastFailureState_Type.__name__ = "Integer32"
_MscLecLastFailureState_Object = MibTableColumn
mscLecLastFailureState = _MscLecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 17, 1, 14),
    _MscLecLastFailureState_Type()
)
mscLecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecLastFailureState.setStatus("mandatory")
_MscLecStatsTable_Object = MibTable
mscLecStatsTable = _MscLecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18)
)
if mibBuilder.loadTexts:
    mscLecStatsTable.setStatus("mandatory")
_MscLecStatsEntry_Object = MibTableRow
mscLecStatsEntry = _MscLecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1)
)
mscLecStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LaneClientMIB", "mscLecIndex"),
)
if mibBuilder.loadTexts:
    mscLecStatsEntry.setStatus("mandatory")
_MscLecArpRequestsOut_Type = Counter32
_MscLecArpRequestsOut_Object = MibTableColumn
mscLecArpRequestsOut = _MscLecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 1),
    _MscLecArpRequestsOut_Type()
)
mscLecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecArpRequestsOut.setStatus("mandatory")
_MscLecArpRepliesIn_Type = Counter32
_MscLecArpRepliesIn_Object = MibTableColumn
mscLecArpRepliesIn = _MscLecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 2),
    _MscLecArpRepliesIn_Type()
)
mscLecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecArpRepliesIn.setStatus("mandatory")
_MscLecArpRequestsIn_Type = Counter32
_MscLecArpRequestsIn_Object = MibTableColumn
mscLecArpRequestsIn = _MscLecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 3),
    _MscLecArpRequestsIn_Type()
)
mscLecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecArpRequestsIn.setStatus("mandatory")
_MscLecArpRepliesOut_Type = Counter32
_MscLecArpRepliesOut_Object = MibTableColumn
mscLecArpRepliesOut = _MscLecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 4),
    _MscLecArpRepliesOut_Type()
)
mscLecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecArpRepliesOut.setStatus("mandatory")
_MscLecControlFramesOut_Type = Counter32
_MscLecControlFramesOut_Object = MibTableColumn
mscLecControlFramesOut = _MscLecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 5),
    _MscLecControlFramesOut_Type()
)
mscLecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecControlFramesOut.setStatus("mandatory")
_MscLecControlFramesIn_Type = Counter32
_MscLecControlFramesIn_Object = MibTableColumn
mscLecControlFramesIn = _MscLecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 6),
    _MscLecControlFramesIn_Type()
)
mscLecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecControlFramesIn.setStatus("mandatory")
_MscLecSvcFailures_Type = Counter32
_MscLecSvcFailures_Object = MibTableColumn
mscLecSvcFailures = _MscLecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 7),
    _MscLecSvcFailures_Type()
)
mscLecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecSvcFailures.setStatus("mandatory")


class _MscLecCurrDataSvcs_Type(Unsigned32):
    """Custom type mscLecCurrDataSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscLecCurrDataSvcs_Type.__name__ = "Unsigned32"
_MscLecCurrDataSvcs_Object = MibTableColumn
mscLecCurrDataSvcs = _MscLecCurrDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 8),
    _MscLecCurrDataSvcs_Type()
)
mscLecCurrDataSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecCurrDataSvcs.setStatus("mandatory")


class _MscLecPeakDataSvcs_Type(Unsigned32):
    """Custom type mscLecPeakDataSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscLecPeakDataSvcs_Type.__name__ = "Unsigned32"
_MscLecPeakDataSvcs_Object = MibTableColumn
mscLecPeakDataSvcs = _MscLecPeakDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 9),
    _MscLecPeakDataSvcs_Type()
)
mscLecPeakDataSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecPeakDataSvcs.setStatus("mandatory")


class _MscLecCurrArpEntries_Type(Unsigned32):
    """Custom type mscLecCurrArpEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscLecCurrArpEntries_Type.__name__ = "Unsigned32"
_MscLecCurrArpEntries_Object = MibTableColumn
mscLecCurrArpEntries = _MscLecCurrArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 10),
    _MscLecCurrArpEntries_Type()
)
mscLecCurrArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecCurrArpEntries.setStatus("mandatory")


class _MscLecPeakArpEntries_Type(Unsigned32):
    """Custom type mscLecPeakArpEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscLecPeakArpEntries_Type.__name__ = "Unsigned32"
_MscLecPeakArpEntries_Object = MibTableColumn
mscLecPeakArpEntries = _MscLecPeakArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 11),
    _MscLecPeakArpEntries_Type()
)
mscLecPeakArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecPeakArpEntries.setStatus("mandatory")
_MscLecBadControlFrames_Type = Counter32
_MscLecBadControlFrames_Object = MibTableColumn
mscLecBadControlFrames = _MscLecBadControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 12),
    _MscLecBadControlFrames_Type()
)
mscLecBadControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecBadControlFrames.setStatus("mandatory")
_MscLecProtocolViolations_Type = Counter32
_MscLecProtocolViolations_Object = MibTableColumn
mscLecProtocolViolations = _MscLecProtocolViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 13),
    _MscLecProtocolViolations_Type()
)
mscLecProtocolViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecProtocolViolations.setStatus("mandatory")
_MscLecUnsupportedTlvs_Type = Counter32
_MscLecUnsupportedTlvs_Object = MibTableColumn
mscLecUnsupportedTlvs = _MscLecUnsupportedTlvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 124, 18, 1, 14),
    _MscLecUnsupportedTlvs_Type()
)
mscLecUnsupportedTlvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLecUnsupportedTlvs.setStatus("mandatory")
_LaneClientMIB_ObjectIdentity = ObjectIdentity
laneClientMIB = _LaneClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71)
)
_LaneClientGroup_ObjectIdentity = ObjectIdentity
laneClientGroup = _LaneClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 1)
)
_LaneClientGroupCA_ObjectIdentity = ObjectIdentity
laneClientGroupCA = _LaneClientGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 1, 1)
)
_LaneClientGroupCA02_ObjectIdentity = ObjectIdentity
laneClientGroupCA02 = _LaneClientGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 1, 1, 3)
)
_LaneClientGroupCA02A_ObjectIdentity = ObjectIdentity
laneClientGroupCA02A = _LaneClientGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 1, 1, 3, 2)
)
_LaneClientCapabilities_ObjectIdentity = ObjectIdentity
laneClientCapabilities = _LaneClientCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 3)
)
_LaneClientCapabilitiesCA_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesCA = _LaneClientCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 3, 1)
)
_LaneClientCapabilitiesCA02_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesCA02 = _LaneClientCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 3, 1, 3)
)
_LaneClientCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesCA02A = _LaneClientCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 71, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-LaneClientMIB",
    **{"mscLec": mscLec,
       "mscLecRowStatusTable": mscLecRowStatusTable,
       "mscLecRowStatusEntry": mscLecRowStatusEntry,
       "mscLecRowStatus": mscLecRowStatus,
       "mscLecComponentName": mscLecComponentName,
       "mscLecStorageType": mscLecStorageType,
       "mscLecIndex": mscLecIndex,
       "mscLecLeArp": mscLecLeArp,
       "mscLecLeArpRowStatusTable": mscLecLeArpRowStatusTable,
       "mscLecLeArpRowStatusEntry": mscLecLeArpRowStatusEntry,
       "mscLecLeArpRowStatus": mscLecLeArpRowStatus,
       "mscLecLeArpComponentName": mscLecLeArpComponentName,
       "mscLecLeArpStorageType": mscLecLeArpStorageType,
       "mscLecLeArpIndex": mscLecLeArpIndex,
       "mscLecLeArpOperTable": mscLecLeArpOperTable,
       "mscLecLeArpOperEntry": mscLecLeArpOperEntry,
       "mscLecLeArpAtmAddress": mscLecLeArpAtmAddress,
       "mscLecLeArpIsRemoteAddress": mscLecLeArpIsRemoteAddress,
       "mscLecLeArpConnectionId": mscLecLeArpConnectionId,
       "mscLecConn": mscLecConn,
       "mscLecConnRowStatusTable": mscLecConnRowStatusTable,
       "mscLecConnRowStatusEntry": mscLecConnRowStatusEntry,
       "mscLecConnRowStatus": mscLecConnRowStatus,
       "mscLecConnComponentName": mscLecConnComponentName,
       "mscLecConnStorageType": mscLecConnStorageType,
       "mscLecConnIndex": mscLecConnIndex,
       "mscLecConnAtmCon": mscLecConnAtmCon,
       "mscLecConnAtmConRowStatusTable": mscLecConnAtmConRowStatusTable,
       "mscLecConnAtmConRowStatusEntry": mscLecConnAtmConRowStatusEntry,
       "mscLecConnAtmConRowStatus": mscLecConnAtmConRowStatus,
       "mscLecConnAtmConComponentName": mscLecConnAtmConComponentName,
       "mscLecConnAtmConStorageType": mscLecConnAtmConStorageType,
       "mscLecConnAtmConIndex": mscLecConnAtmConIndex,
       "mscLecConnAtmConOperTable": mscLecConnAtmConOperTable,
       "mscLecConnAtmConOperEntry": mscLecConnAtmConOperEntry,
       "mscLecConnAtmConNextHop": mscLecConnAtmConNextHop,
       "mscLecConnOperTable": mscLecConnOperTable,
       "mscLecConnOperEntry": mscLecConnOperEntry,
       "mscLecConnRemoteAtmAddress": mscLecConnRemoteAtmAddress,
       "mscLecConnAge": mscLecConnAge,
       "mscLecConnType": mscLecConnType,
       "mscLecConnStatsTable": mscLecConnStatsTable,
       "mscLecConnStatsEntry": mscLecConnStatsEntry,
       "mscLecConnOutFrames": mscLecConnOutFrames,
       "mscLecConnInFrames": mscLecConnInFrames,
       "mscLecCidDataTable": mscLecCidDataTable,
       "mscLecCidDataEntry": mscLecCidDataEntry,
       "mscLecCustomerIdentifier": mscLecCustomerIdentifier,
       "mscLecIfEntryTable": mscLecIfEntryTable,
       "mscLecIfEntryEntry": mscLecIfEntryEntry,
       "mscLecIfAdminStatus": mscLecIfAdminStatus,
       "mscLecIfIndex": mscLecIfIndex,
       "mscLecMpTable": mscLecMpTable,
       "mscLecMpEntry": mscLecMpEntry,
       "mscLecLinkToProtocolPort": mscLecLinkToProtocolPort,
       "mscLecProvTable": mscLecProvTable,
       "mscLecProvEntry": mscLecProvEntry,
       "mscLecLanType": mscLecLanType,
       "mscLecMaxFrameSize": mscLecMaxFrameSize,
       "mscLecLanName": mscLecLanName,
       "mscLecV2Capable": mscLecV2Capable,
       "mscLecLecsAddress": mscLecLecsAddress,
       "mscLecLesAddress": mscLecLesAddress,
       "mscLecMaxDataSvcs": mscLecMaxDataSvcs,
       "mscLecMaxArpEntries": mscLecMaxArpEntries,
       "mscLecIlsForwarder": mscLecIlsForwarder,
       "mscLecStateTable": mscLecStateTable,
       "mscLecStateEntry": mscLecStateEntry,
       "mscLecAdminState": mscLecAdminState,
       "mscLecOperationalState": mscLecOperationalState,
       "mscLecUsageState": mscLecUsageState,
       "mscLecOperStatusTable": mscLecOperStatusTable,
       "mscLecOperStatusEntry": mscLecOperStatusEntry,
       "mscLecSnmpOperStatus": mscLecSnmpOperStatus,
       "mscLecOperTable": mscLecOperTable,
       "mscLecOperEntry": mscLecOperEntry,
       "mscLecActualLanType": mscLecActualLanType,
       "mscLecActualMaxFrameSize": mscLecActualMaxFrameSize,
       "mscLecActualLanName": mscLecActualLanName,
       "mscLecElanId": mscLecElanId,
       "mscLecActualV2Capable": mscLecActualV2Capable,
       "mscLecConfigurationSource": mscLecConfigurationSource,
       "mscLecActualLecsAddress": mscLecActualLecsAddress,
       "mscLecActualLesAddress": mscLecActualLesAddress,
       "mscLecAtmAddress": mscLecAtmAddress,
       "mscLecMacAddress": mscLecMacAddress,
       "mscLecLecId": mscLecLecId,
       "mscLecInterfaceState": mscLecInterfaceState,
       "mscLecLastFailureResponseCode": mscLecLastFailureResponseCode,
       "mscLecLastFailureState": mscLecLastFailureState,
       "mscLecStatsTable": mscLecStatsTable,
       "mscLecStatsEntry": mscLecStatsEntry,
       "mscLecArpRequestsOut": mscLecArpRequestsOut,
       "mscLecArpRepliesIn": mscLecArpRepliesIn,
       "mscLecArpRequestsIn": mscLecArpRequestsIn,
       "mscLecArpRepliesOut": mscLecArpRepliesOut,
       "mscLecControlFramesOut": mscLecControlFramesOut,
       "mscLecControlFramesIn": mscLecControlFramesIn,
       "mscLecSvcFailures": mscLecSvcFailures,
       "mscLecCurrDataSvcs": mscLecCurrDataSvcs,
       "mscLecPeakDataSvcs": mscLecPeakDataSvcs,
       "mscLecCurrArpEntries": mscLecCurrArpEntries,
       "mscLecPeakArpEntries": mscLecPeakArpEntries,
       "mscLecBadControlFrames": mscLecBadControlFrames,
       "mscLecProtocolViolations": mscLecProtocolViolations,
       "mscLecUnsupportedTlvs": mscLecUnsupportedTlvs,
       "laneClientMIB": laneClientMIB,
       "laneClientGroup": laneClientGroup,
       "laneClientGroupCA": laneClientGroupCA,
       "laneClientGroupCA02": laneClientGroupCA02,
       "laneClientGroupCA02A": laneClientGroupCA02A,
       "laneClientCapabilities": laneClientCapabilities,
       "laneClientCapabilitiesCA": laneClientCapabilitiesCA,
       "laneClientCapabilitiesCA02": laneClientCapabilitiesCA02,
       "laneClientCapabilitiesCA02A": laneClientCapabilitiesCA02A}
)
