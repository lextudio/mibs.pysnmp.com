# SNMP MIB module (Nortel-Magellan-Passport-LaneClientMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-LaneClientMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:06 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DashedHexString",
    "HexString",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Lec_ObjectIdentity = ObjectIdentity
lec = _Lec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124)
)
_LecRowStatusTable_Object = MibTable
lecRowStatusTable = _LecRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1)
)
if mibBuilder.loadTexts:
    lecRowStatusTable.setStatus("mandatory")
_LecRowStatusEntry_Object = MibTableRow
lecRowStatusEntry = _LecRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1)
)
lecRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecRowStatusEntry.setStatus("mandatory")
_LecRowStatus_Type = RowStatus
_LecRowStatus_Object = MibTableColumn
lecRowStatus = _LecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 1),
    _LecRowStatus_Type()
)
lecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecRowStatus.setStatus("mandatory")
_LecComponentName_Type = DisplayString
_LecComponentName_Object = MibTableColumn
lecComponentName = _LecComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 2),
    _LecComponentName_Type()
)
lecComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecComponentName.setStatus("mandatory")
_LecStorageType_Type = StorageType
_LecStorageType_Object = MibTableColumn
lecStorageType = _LecStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 4),
    _LecStorageType_Type()
)
lecStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecStorageType.setStatus("mandatory")


class _LecIndex_Type(Integer32):
    """Custom type lecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LecIndex_Type.__name__ = "Integer32"
_LecIndex_Object = MibTableColumn
lecIndex = _LecIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 1, 1, 10),
    _LecIndex_Type()
)
lecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecIndex.setStatus("mandatory")
_LecLeArp_ObjectIdentity = ObjectIdentity
lecLeArp = _LecLeArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2)
)
_LecLeArpRowStatusTable_Object = MibTable
lecLeArpRowStatusTable = _LecLeArpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1)
)
if mibBuilder.loadTexts:
    lecLeArpRowStatusTable.setStatus("mandatory")
_LecLeArpRowStatusEntry_Object = MibTableRow
lecLeArpRowStatusEntry = _LecLeArpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1)
)
lecLeArpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecLeArpIndex"),
)
if mibBuilder.loadTexts:
    lecLeArpRowStatusEntry.setStatus("mandatory")
_LecLeArpRowStatus_Type = RowStatus
_LecLeArpRowStatus_Object = MibTableColumn
lecLeArpRowStatus = _LecLeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 1),
    _LecLeArpRowStatus_Type()
)
lecLeArpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpRowStatus.setStatus("mandatory")
_LecLeArpComponentName_Type = DisplayString
_LecLeArpComponentName_Object = MibTableColumn
lecLeArpComponentName = _LecLeArpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 2),
    _LecLeArpComponentName_Type()
)
lecLeArpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpComponentName.setStatus("mandatory")
_LecLeArpStorageType_Type = StorageType
_LecLeArpStorageType_Object = MibTableColumn
lecLeArpStorageType = _LecLeArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 4),
    _LecLeArpStorageType_Type()
)
lecLeArpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpStorageType.setStatus("mandatory")


class _LecLeArpIndex_Type(DashedHexString):
    """Custom type lecLeArpIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LecLeArpIndex_Type.__name__ = "DashedHexString"
_LecLeArpIndex_Object = MibTableColumn
lecLeArpIndex = _LecLeArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 1, 1, 10),
    _LecLeArpIndex_Type()
)
lecLeArpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecLeArpIndex.setStatus("mandatory")
_LecLeArpOperTable_Object = MibTable
lecLeArpOperTable = _LecLeArpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10)
)
if mibBuilder.loadTexts:
    lecLeArpOperTable.setStatus("mandatory")
_LecLeArpOperEntry_Object = MibTableRow
lecLeArpOperEntry = _LecLeArpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1)
)
lecLeArpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecLeArpIndex"),
)
if mibBuilder.loadTexts:
    lecLeArpOperEntry.setStatus("mandatory")


class _LecLeArpAtmAddress_Type(HexString):
    """Custom type lecLeArpAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LecLeArpAtmAddress_Type.__name__ = "HexString"
_LecLeArpAtmAddress_Object = MibTableColumn
lecLeArpAtmAddress = _LecLeArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 1),
    _LecLeArpAtmAddress_Type()
)
lecLeArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpAtmAddress.setStatus("mandatory")


class _LecLeArpIsRemoteAddress_Type(Integer32):
    """Custom type lecLeArpIsRemoteAddress based on Integer32"""
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


_LecLeArpIsRemoteAddress_Type.__name__ = "Integer32"
_LecLeArpIsRemoteAddress_Object = MibTableColumn
lecLeArpIsRemoteAddress = _LecLeArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 2),
    _LecLeArpIsRemoteAddress_Type()
)
lecLeArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpIsRemoteAddress.setStatus("mandatory")


class _LecLeArpConnectionId_Type(Unsigned32):
    """Custom type lecLeArpConnectionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_LecLeArpConnectionId_Type.__name__ = "Unsigned32"
_LecLeArpConnectionId_Object = MibTableColumn
lecLeArpConnectionId = _LecLeArpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 2, 10, 1, 3),
    _LecLeArpConnectionId_Type()
)
lecLeArpConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLeArpConnectionId.setStatus("mandatory")
_LecConn_ObjectIdentity = ObjectIdentity
lecConn = _LecConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3)
)
_LecConnRowStatusTable_Object = MibTable
lecConnRowStatusTable = _LecConnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1)
)
if mibBuilder.loadTexts:
    lecConnRowStatusTable.setStatus("mandatory")
_LecConnRowStatusEntry_Object = MibTableRow
lecConnRowStatusEntry = _LecConnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1)
)
lecConnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"),
)
if mibBuilder.loadTexts:
    lecConnRowStatusEntry.setStatus("mandatory")
_LecConnRowStatus_Type = RowStatus
_LecConnRowStatus_Object = MibTableColumn
lecConnRowStatus = _LecConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 1),
    _LecConnRowStatus_Type()
)
lecConnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnRowStatus.setStatus("mandatory")
_LecConnComponentName_Type = DisplayString
_LecConnComponentName_Object = MibTableColumn
lecConnComponentName = _LecConnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 2),
    _LecConnComponentName_Type()
)
lecConnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnComponentName.setStatus("mandatory")
_LecConnStorageType_Type = StorageType
_LecConnStorageType_Object = MibTableColumn
lecConnStorageType = _LecConnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 4),
    _LecConnStorageType_Type()
)
lecConnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnStorageType.setStatus("mandatory")


class _LecConnIndex_Type(Integer32):
    """Custom type lecConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_LecConnIndex_Type.__name__ = "Integer32"
_LecConnIndex_Object = MibTableColumn
lecConnIndex = _LecConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 1, 1, 10),
    _LecConnIndex_Type()
)
lecConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecConnIndex.setStatus("mandatory")
_LecConnAtmCon_ObjectIdentity = ObjectIdentity
lecConnAtmCon = _LecConnAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2)
)
_LecConnAtmConRowStatusTable_Object = MibTable
lecConnAtmConRowStatusTable = _LecConnAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lecConnAtmConRowStatusTable.setStatus("mandatory")
_LecConnAtmConRowStatusEntry_Object = MibTableRow
lecConnAtmConRowStatusEntry = _LecConnAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1)
)
lecConnAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnAtmConIndex"),
)
if mibBuilder.loadTexts:
    lecConnAtmConRowStatusEntry.setStatus("mandatory")
_LecConnAtmConRowStatus_Type = RowStatus
_LecConnAtmConRowStatus_Object = MibTableColumn
lecConnAtmConRowStatus = _LecConnAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 1),
    _LecConnAtmConRowStatus_Type()
)
lecConnAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnAtmConRowStatus.setStatus("mandatory")
_LecConnAtmConComponentName_Type = DisplayString
_LecConnAtmConComponentName_Object = MibTableColumn
lecConnAtmConComponentName = _LecConnAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 2),
    _LecConnAtmConComponentName_Type()
)
lecConnAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnAtmConComponentName.setStatus("mandatory")
_LecConnAtmConStorageType_Type = StorageType
_LecConnAtmConStorageType_Object = MibTableColumn
lecConnAtmConStorageType = _LecConnAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 4),
    _LecConnAtmConStorageType_Type()
)
lecConnAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnAtmConStorageType.setStatus("mandatory")
_LecConnAtmConIndex_Type = NonReplicated
_LecConnAtmConIndex_Object = MibTableColumn
lecConnAtmConIndex = _LecConnAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 1, 1, 10),
    _LecConnAtmConIndex_Type()
)
lecConnAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecConnAtmConIndex.setStatus("mandatory")
_LecConnAtmConOperTable_Object = MibTable
lecConnAtmConOperTable = _LecConnAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10)
)
if mibBuilder.loadTexts:
    lecConnAtmConOperTable.setStatus("mandatory")
_LecConnAtmConOperEntry_Object = MibTableRow
lecConnAtmConOperEntry = _LecConnAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10, 1)
)
lecConnAtmConOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnAtmConIndex"),
)
if mibBuilder.loadTexts:
    lecConnAtmConOperEntry.setStatus("mandatory")
_LecConnAtmConNextHop_Type = RowPointer
_LecConnAtmConNextHop_Object = MibTableColumn
lecConnAtmConNextHop = _LecConnAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 2, 10, 1, 1),
    _LecConnAtmConNextHop_Type()
)
lecConnAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnAtmConNextHop.setStatus("mandatory")
_LecConnOperTable_Object = MibTable
lecConnOperTable = _LecConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10)
)
if mibBuilder.loadTexts:
    lecConnOperTable.setStatus("mandatory")
_LecConnOperEntry_Object = MibTableRow
lecConnOperEntry = _LecConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1)
)
lecConnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"),
)
if mibBuilder.loadTexts:
    lecConnOperEntry.setStatus("mandatory")


class _LecConnRemoteAtmAddress_Type(HexString):
    """Custom type lecConnRemoteAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LecConnRemoteAtmAddress_Type.__name__ = "HexString"
_LecConnRemoteAtmAddress_Object = MibTableColumn
lecConnRemoteAtmAddress = _LecConnRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 1),
    _LecConnRemoteAtmAddress_Type()
)
lecConnRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnRemoteAtmAddress.setStatus("mandatory")


class _LecConnAge_Type(Unsigned32):
    """Custom type lecConnAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_LecConnAge_Type.__name__ = "Unsigned32"
_LecConnAge_Object = MibTableColumn
lecConnAge = _LecConnAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 2),
    _LecConnAge_Type()
)
lecConnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnAge.setStatus("mandatory")


class _LecConnType_Type(Integer32):
    """Custom type lecConnType based on Integer32"""
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


_LecConnType_Type.__name__ = "Integer32"
_LecConnType_Object = MibTableColumn
lecConnType = _LecConnType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 10, 1, 3),
    _LecConnType_Type()
)
lecConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnType.setStatus("mandatory")
_LecConnStatsTable_Object = MibTable
lecConnStatsTable = _LecConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11)
)
if mibBuilder.loadTexts:
    lecConnStatsTable.setStatus("mandatory")
_LecConnStatsEntry_Object = MibTableRow
lecConnStatsEntry = _LecConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1)
)
lecConnStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecConnIndex"),
)
if mibBuilder.loadTexts:
    lecConnStatsEntry.setStatus("mandatory")
_LecConnOutFrames_Type = Counter32
_LecConnOutFrames_Object = MibTableColumn
lecConnOutFrames = _LecConnOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1, 1),
    _LecConnOutFrames_Type()
)
lecConnOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnOutFrames.setStatus("mandatory")
_LecConnInFrames_Type = Counter32
_LecConnInFrames_Object = MibTableColumn
lecConnInFrames = _LecConnInFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 3, 11, 1, 2),
    _LecConnInFrames_Type()
)
lecConnInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConnInFrames.setStatus("mandatory")
_LecCidDataTable_Object = MibTable
lecCidDataTable = _LecCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10)
)
if mibBuilder.loadTexts:
    lecCidDataTable.setStatus("mandatory")
_LecCidDataEntry_Object = MibTableRow
lecCidDataEntry = _LecCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10, 1)
)
lecCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecCidDataEntry.setStatus("mandatory")


class _LecCustomerIdentifier_Type(Unsigned32):
    """Custom type lecCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LecCustomerIdentifier_Type.__name__ = "Unsigned32"
_LecCustomerIdentifier_Object = MibTableColumn
lecCustomerIdentifier = _LecCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 10, 1, 1),
    _LecCustomerIdentifier_Type()
)
lecCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecCustomerIdentifier.setStatus("mandatory")
_LecIfEntryTable_Object = MibTable
lecIfEntryTable = _LecIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11)
)
if mibBuilder.loadTexts:
    lecIfEntryTable.setStatus("mandatory")
_LecIfEntryEntry_Object = MibTableRow
lecIfEntryEntry = _LecIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1)
)
lecIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecIfEntryEntry.setStatus("mandatory")


class _LecIfAdminStatus_Type(Integer32):
    """Custom type lecIfAdminStatus based on Integer32"""
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


_LecIfAdminStatus_Type.__name__ = "Integer32"
_LecIfAdminStatus_Object = MibTableColumn
lecIfAdminStatus = _LecIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1, 1),
    _LecIfAdminStatus_Type()
)
lecIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecIfAdminStatus.setStatus("mandatory")


class _LecIfIndex_Type(InterfaceIndex):
    """Custom type lecIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LecIfIndex_Type.__name__ = "InterfaceIndex"
_LecIfIndex_Object = MibTableColumn
lecIfIndex = _LecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 11, 1, 2),
    _LecIfIndex_Type()
)
lecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecIfIndex.setStatus("mandatory")
_LecMpTable_Object = MibTable
lecMpTable = _LecMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12)
)
if mibBuilder.loadTexts:
    lecMpTable.setStatus("mandatory")
_LecMpEntry_Object = MibTableRow
lecMpEntry = _LecMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12, 1)
)
lecMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecMpEntry.setStatus("mandatory")
_LecLinkToProtocolPort_Type = Link
_LecLinkToProtocolPort_Object = MibTableColumn
lecLinkToProtocolPort = _LecLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 12, 1, 1),
    _LecLinkToProtocolPort_Type()
)
lecLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLinkToProtocolPort.setStatus("mandatory")
_LecProvTable_Object = MibTable
lecProvTable = _LecProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13)
)
if mibBuilder.loadTexts:
    lecProvTable.setStatus("mandatory")
_LecProvEntry_Object = MibTableRow
lecProvEntry = _LecProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1)
)
lecProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecProvEntry.setStatus("mandatory")


class _LecLanType_Type(Integer32):
    """Custom type lecLanType based on Integer32"""
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


_LecLanType_Type.__name__ = "Integer32"
_LecLanType_Object = MibTableColumn
lecLanType = _LecLanType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 1),
    _LecLanType_Type()
)
lecLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLanType.setStatus("mandatory")


class _LecMaxFrameSize_Type(Integer32):
    """Custom type lecMaxFrameSize based on Integer32"""
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


_LecMaxFrameSize_Type.__name__ = "Integer32"
_LecMaxFrameSize_Object = MibTableColumn
lecMaxFrameSize = _LecMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 2),
    _LecMaxFrameSize_Type()
)
lecMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxFrameSize.setStatus("mandatory")


class _LecLanName_Type(AsciiString):
    """Custom type lecLanName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecLanName_Type.__name__ = "AsciiString"
_LecLanName_Object = MibTableColumn
lecLanName = _LecLanName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 3),
    _LecLanName_Type()
)
lecLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLanName.setStatus("mandatory")


class _LecV2Capable_Type(Integer32):
    """Custom type lecV2Capable based on Integer32"""
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


_LecV2Capable_Type.__name__ = "Integer32"
_LecV2Capable_Object = MibTableColumn
lecV2Capable = _LecV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 4),
    _LecV2Capable_Type()
)
lecV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecV2Capable.setStatus("mandatory")


class _LecLecsAddress_Type(HexString):
    """Custom type lecLecsAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecLecsAddress_Type.__name__ = "HexString"
_LecLecsAddress_Object = MibTableColumn
lecLecsAddress = _LecLecsAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 5),
    _LecLecsAddress_Type()
)
lecLecsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLecsAddress.setStatus("mandatory")


class _LecLesAddress_Type(HexString):
    """Custom type lecLesAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecLesAddress_Type.__name__ = "HexString"
_LecLesAddress_Object = MibTableColumn
lecLesAddress = _LecLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 6),
    _LecLesAddress_Type()
)
lecLesAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecLesAddress.setStatus("mandatory")


class _LecMaxDataSvcs_Type(Unsigned32):
    """Custom type lecMaxDataSvcs based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1018),
    )


_LecMaxDataSvcs_Type.__name__ = "Unsigned32"
_LecMaxDataSvcs_Object = MibTableColumn
lecMaxDataSvcs = _LecMaxDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 7),
    _LecMaxDataSvcs_Type()
)
lecMaxDataSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxDataSvcs.setStatus("mandatory")


class _LecMaxArpEntries_Type(Unsigned32):
    """Custom type lecMaxArpEntries based on Unsigned32"""
    defaultValue = 5120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 10240),
    )


_LecMaxArpEntries_Type.__name__ = "Unsigned32"
_LecMaxArpEntries_Object = MibTableColumn
lecMaxArpEntries = _LecMaxArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 8),
    _LecMaxArpEntries_Type()
)
lecMaxArpEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecMaxArpEntries.setStatus("mandatory")
_LecIlsForwarder_Type = Link
_LecIlsForwarder_Object = MibTableColumn
lecIlsForwarder = _LecIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 13, 1, 9),
    _LecIlsForwarder_Type()
)
lecIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecIlsForwarder.setStatus("mandatory")
_LecStateTable_Object = MibTable
lecStateTable = _LecStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15)
)
if mibBuilder.loadTexts:
    lecStateTable.setStatus("mandatory")
_LecStateEntry_Object = MibTableRow
lecStateEntry = _LecStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1)
)
lecStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecStateEntry.setStatus("mandatory")


class _LecAdminState_Type(Integer32):
    """Custom type lecAdminState based on Integer32"""
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


_LecAdminState_Type.__name__ = "Integer32"
_LecAdminState_Object = MibTableColumn
lecAdminState = _LecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 1),
    _LecAdminState_Type()
)
lecAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecAdminState.setStatus("mandatory")


class _LecOperationalState_Type(Integer32):
    """Custom type lecOperationalState based on Integer32"""
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


_LecOperationalState_Type.__name__ = "Integer32"
_LecOperationalState_Object = MibTableColumn
lecOperationalState = _LecOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 2),
    _LecOperationalState_Type()
)
lecOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecOperationalState.setStatus("mandatory")


class _LecUsageState_Type(Integer32):
    """Custom type lecUsageState based on Integer32"""
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


_LecUsageState_Type.__name__ = "Integer32"
_LecUsageState_Object = MibTableColumn
lecUsageState = _LecUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 15, 1, 3),
    _LecUsageState_Type()
)
lecUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecUsageState.setStatus("mandatory")
_LecOperStatusTable_Object = MibTable
lecOperStatusTable = _LecOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16)
)
if mibBuilder.loadTexts:
    lecOperStatusTable.setStatus("mandatory")
_LecOperStatusEntry_Object = MibTableRow
lecOperStatusEntry = _LecOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16, 1)
)
lecOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecOperStatusEntry.setStatus("mandatory")


class _LecSnmpOperStatus_Type(Integer32):
    """Custom type lecSnmpOperStatus based on Integer32"""
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


_LecSnmpOperStatus_Type.__name__ = "Integer32"
_LecSnmpOperStatus_Object = MibTableColumn
lecSnmpOperStatus = _LecSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 16, 1, 1),
    _LecSnmpOperStatus_Type()
)
lecSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecSnmpOperStatus.setStatus("mandatory")
_LecOperTable_Object = MibTable
lecOperTable = _LecOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17)
)
if mibBuilder.loadTexts:
    lecOperTable.setStatus("mandatory")
_LecOperEntry_Object = MibTableRow
lecOperEntry = _LecOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1)
)
lecOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecOperEntry.setStatus("mandatory")


class _LecActualLanType_Type(Integer32):
    """Custom type lecActualLanType based on Integer32"""
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


_LecActualLanType_Type.__name__ = "Integer32"
_LecActualLanType_Object = MibTableColumn
lecActualLanType = _LecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 1),
    _LecActualLanType_Type()
)
lecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanType.setStatus("mandatory")


class _LecActualMaxFrameSize_Type(Integer32):
    """Custom type lecActualMaxFrameSize based on Integer32"""
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


_LecActualMaxFrameSize_Type.__name__ = "Integer32"
_LecActualMaxFrameSize_Object = MibTableColumn
lecActualMaxFrameSize = _LecActualMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 2),
    _LecActualMaxFrameSize_Type()
)
lecActualMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualMaxFrameSize.setStatus("mandatory")


class _LecActualLanName_Type(AsciiString):
    """Custom type lecActualLanName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecActualLanName_Type.__name__ = "AsciiString"
_LecActualLanName_Object = MibTableColumn
lecActualLanName = _LecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 3),
    _LecActualLanName_Type()
)
lecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanName.setStatus("mandatory")


class _LecElanId_Type(Unsigned32):
    """Custom type lecElanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LecElanId_Type.__name__ = "Unsigned32"
_LecElanId_Object = MibTableColumn
lecElanId = _LecElanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 4),
    _LecElanId_Type()
)
lecElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecElanId.setStatus("mandatory")


class _LecActualV2Capable_Type(Integer32):
    """Custom type lecActualV2Capable based on Integer32"""
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


_LecActualV2Capable_Type.__name__ = "Integer32"
_LecActualV2Capable_Object = MibTableColumn
lecActualV2Capable = _LecActualV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 5),
    _LecActualV2Capable_Type()
)
lecActualV2Capable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualV2Capable.setStatus("mandatory")


class _LecConfigurationSource_Type(Integer32):
    """Custom type lecConfigurationSource based on Integer32"""
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


_LecConfigurationSource_Type.__name__ = "Integer32"
_LecConfigurationSource_Object = MibTableColumn
lecConfigurationSource = _LecConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 6),
    _LecConfigurationSource_Type()
)
lecConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigurationSource.setStatus("mandatory")


class _LecActualLecsAddress_Type(HexString):
    """Custom type lecActualLecsAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecActualLecsAddress_Type.__name__ = "HexString"
_LecActualLecsAddress_Object = MibTableColumn
lecActualLecsAddress = _LecActualLecsAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 7),
    _LecActualLecsAddress_Type()
)
lecActualLecsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLecsAddress.setStatus("mandatory")


class _LecActualLesAddress_Type(HexString):
    """Custom type lecActualLesAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecActualLesAddress_Type.__name__ = "HexString"
_LecActualLesAddress_Object = MibTableColumn
lecActualLesAddress = _LecActualLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 8),
    _LecActualLesAddress_Type()
)
lecActualLesAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLesAddress.setStatus("mandatory")


class _LecAtmAddress_Type(HexString):
    """Custom type lecAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecAtmAddress_Type.__name__ = "HexString"
_LecAtmAddress_Object = MibTableColumn
lecAtmAddress = _LecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 9),
    _LecAtmAddress_Type()
)
lecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecAtmAddress.setStatus("mandatory")


class _LecMacAddress_Type(MacAddress):
    """Custom type lecMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LecMacAddress_Type.__name__ = "MacAddress"
_LecMacAddress_Object = MibTableColumn
lecMacAddress = _LecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 10),
    _LecMacAddress_Type()
)
lecMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacAddress.setStatus("mandatory")


class _LecLecId_Type(Unsigned32):
    """Custom type lecLecId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_LecLecId_Type.__name__ = "Unsigned32"
_LecLecId_Object = MibTableColumn
lecLecId = _LecLecId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 11),
    _LecLecId_Type()
)
lecLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLecId.setStatus("mandatory")


class _LecInterfaceState_Type(Integer32):
    """Custom type lecInterfaceState based on Integer32"""
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


_LecInterfaceState_Type.__name__ = "Integer32"
_LecInterfaceState_Object = MibTableColumn
lecInterfaceState = _LecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 12),
    _LecInterfaceState_Type()
)
lecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecInterfaceState.setStatus("mandatory")


class _LecLastFailureResponseCode_Type(Integer32):
    """Custom type lecLastFailureResponseCode based on Integer32"""
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


_LecLastFailureResponseCode_Type.__name__ = "Integer32"
_LecLastFailureResponseCode_Object = MibTableColumn
lecLastFailureResponseCode = _LecLastFailureResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 13),
    _LecLastFailureResponseCode_Type()
)
lecLastFailureResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureResponseCode.setStatus("mandatory")


class _LecLastFailureState_Type(Integer32):
    """Custom type lecLastFailureState based on Integer32"""
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


_LecLastFailureState_Type.__name__ = "Integer32"
_LecLastFailureState_Object = MibTableColumn
lecLastFailureState = _LecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 17, 1, 14),
    _LecLastFailureState_Type()
)
lecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureState.setStatus("mandatory")
_LecStatsTable_Object = MibTable
lecStatsTable = _LecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18)
)
if mibBuilder.loadTexts:
    lecStatsTable.setStatus("mandatory")
_LecStatsEntry_Object = MibTableRow
lecStatsEntry = _LecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1)
)
lecStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LaneClientMIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecStatsEntry.setStatus("mandatory")
_LecArpRequestsOut_Type = Counter32
_LecArpRequestsOut_Object = MibTableColumn
lecArpRequestsOut = _LecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 1),
    _LecArpRequestsOut_Type()
)
lecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsOut.setStatus("mandatory")
_LecArpRepliesIn_Type = Counter32
_LecArpRepliesIn_Object = MibTableColumn
lecArpRepliesIn = _LecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 2),
    _LecArpRepliesIn_Type()
)
lecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesIn.setStatus("mandatory")
_LecArpRequestsIn_Type = Counter32
_LecArpRequestsIn_Object = MibTableColumn
lecArpRequestsIn = _LecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 3),
    _LecArpRequestsIn_Type()
)
lecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsIn.setStatus("mandatory")
_LecArpRepliesOut_Type = Counter32
_LecArpRepliesOut_Object = MibTableColumn
lecArpRepliesOut = _LecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 4),
    _LecArpRepliesOut_Type()
)
lecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesOut.setStatus("mandatory")
_LecControlFramesOut_Type = Counter32
_LecControlFramesOut_Object = MibTableColumn
lecControlFramesOut = _LecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 5),
    _LecControlFramesOut_Type()
)
lecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesOut.setStatus("mandatory")
_LecControlFramesIn_Type = Counter32
_LecControlFramesIn_Object = MibTableColumn
lecControlFramesIn = _LecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 6),
    _LecControlFramesIn_Type()
)
lecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesIn.setStatus("mandatory")
_LecSvcFailures_Type = Counter32
_LecSvcFailures_Object = MibTableColumn
lecSvcFailures = _LecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 7),
    _LecSvcFailures_Type()
)
lecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecSvcFailures.setStatus("mandatory")


class _LecCurrDataSvcs_Type(Unsigned32):
    """Custom type lecCurrDataSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_LecCurrDataSvcs_Type.__name__ = "Unsigned32"
_LecCurrDataSvcs_Object = MibTableColumn
lecCurrDataSvcs = _LecCurrDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 8),
    _LecCurrDataSvcs_Type()
)
lecCurrDataSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecCurrDataSvcs.setStatus("mandatory")


class _LecPeakDataSvcs_Type(Unsigned32):
    """Custom type lecPeakDataSvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_LecPeakDataSvcs_Type.__name__ = "Unsigned32"
_LecPeakDataSvcs_Object = MibTableColumn
lecPeakDataSvcs = _LecPeakDataSvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 9),
    _LecPeakDataSvcs_Type()
)
lecPeakDataSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecPeakDataSvcs.setStatus("mandatory")


class _LecCurrArpEntries_Type(Unsigned32):
    """Custom type lecCurrArpEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_LecCurrArpEntries_Type.__name__ = "Unsigned32"
_LecCurrArpEntries_Object = MibTableColumn
lecCurrArpEntries = _LecCurrArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 10),
    _LecCurrArpEntries_Type()
)
lecCurrArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecCurrArpEntries.setStatus("mandatory")


class _LecPeakArpEntries_Type(Unsigned32):
    """Custom type lecPeakArpEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_LecPeakArpEntries_Type.__name__ = "Unsigned32"
_LecPeakArpEntries_Object = MibTableColumn
lecPeakArpEntries = _LecPeakArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 11),
    _LecPeakArpEntries_Type()
)
lecPeakArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecPeakArpEntries.setStatus("mandatory")
_LecBadControlFrames_Type = Counter32
_LecBadControlFrames_Object = MibTableColumn
lecBadControlFrames = _LecBadControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 12),
    _LecBadControlFrames_Type()
)
lecBadControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecBadControlFrames.setStatus("mandatory")
_LecProtocolViolations_Type = Counter32
_LecProtocolViolations_Object = MibTableColumn
lecProtocolViolations = _LecProtocolViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 13),
    _LecProtocolViolations_Type()
)
lecProtocolViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecProtocolViolations.setStatus("mandatory")
_LecUnsupportedTlvs_Type = Counter32
_LecUnsupportedTlvs_Object = MibTableColumn
lecUnsupportedTlvs = _LecUnsupportedTlvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 124, 18, 1, 14),
    _LecUnsupportedTlvs_Type()
)
lecUnsupportedTlvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecUnsupportedTlvs.setStatus("mandatory")
_LaneClientMIB_ObjectIdentity = ObjectIdentity
laneClientMIB = _LaneClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71)
)
_LaneClientGroup_ObjectIdentity = ObjectIdentity
laneClientGroup = _LaneClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1)
)
_LaneClientGroupBE_ObjectIdentity = ObjectIdentity
laneClientGroupBE = _LaneClientGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5)
)
_LaneClientGroupBE00_ObjectIdentity = ObjectIdentity
laneClientGroupBE00 = _LaneClientGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5, 1)
)
_LaneClientGroupBE00A_ObjectIdentity = ObjectIdentity
laneClientGroupBE00A = _LaneClientGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 1, 5, 1, 2)
)
_LaneClientCapabilities_ObjectIdentity = ObjectIdentity
laneClientCapabilities = _LaneClientCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3)
)
_LaneClientCapabilitiesBE_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesBE = _LaneClientCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5)
)
_LaneClientCapabilitiesBE00_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesBE00 = _LaneClientCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5, 1)
)
_LaneClientCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
laneClientCapabilitiesBE00A = _LaneClientCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 71, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-LaneClientMIB",
    **{"lec": lec,
       "lecRowStatusTable": lecRowStatusTable,
       "lecRowStatusEntry": lecRowStatusEntry,
       "lecRowStatus": lecRowStatus,
       "lecComponentName": lecComponentName,
       "lecStorageType": lecStorageType,
       "lecIndex": lecIndex,
       "lecLeArp": lecLeArp,
       "lecLeArpRowStatusTable": lecLeArpRowStatusTable,
       "lecLeArpRowStatusEntry": lecLeArpRowStatusEntry,
       "lecLeArpRowStatus": lecLeArpRowStatus,
       "lecLeArpComponentName": lecLeArpComponentName,
       "lecLeArpStorageType": lecLeArpStorageType,
       "lecLeArpIndex": lecLeArpIndex,
       "lecLeArpOperTable": lecLeArpOperTable,
       "lecLeArpOperEntry": lecLeArpOperEntry,
       "lecLeArpAtmAddress": lecLeArpAtmAddress,
       "lecLeArpIsRemoteAddress": lecLeArpIsRemoteAddress,
       "lecLeArpConnectionId": lecLeArpConnectionId,
       "lecConn": lecConn,
       "lecConnRowStatusTable": lecConnRowStatusTable,
       "lecConnRowStatusEntry": lecConnRowStatusEntry,
       "lecConnRowStatus": lecConnRowStatus,
       "lecConnComponentName": lecConnComponentName,
       "lecConnStorageType": lecConnStorageType,
       "lecConnIndex": lecConnIndex,
       "lecConnAtmCon": lecConnAtmCon,
       "lecConnAtmConRowStatusTable": lecConnAtmConRowStatusTable,
       "lecConnAtmConRowStatusEntry": lecConnAtmConRowStatusEntry,
       "lecConnAtmConRowStatus": lecConnAtmConRowStatus,
       "lecConnAtmConComponentName": lecConnAtmConComponentName,
       "lecConnAtmConStorageType": lecConnAtmConStorageType,
       "lecConnAtmConIndex": lecConnAtmConIndex,
       "lecConnAtmConOperTable": lecConnAtmConOperTable,
       "lecConnAtmConOperEntry": lecConnAtmConOperEntry,
       "lecConnAtmConNextHop": lecConnAtmConNextHop,
       "lecConnOperTable": lecConnOperTable,
       "lecConnOperEntry": lecConnOperEntry,
       "lecConnRemoteAtmAddress": lecConnRemoteAtmAddress,
       "lecConnAge": lecConnAge,
       "lecConnType": lecConnType,
       "lecConnStatsTable": lecConnStatsTable,
       "lecConnStatsEntry": lecConnStatsEntry,
       "lecConnOutFrames": lecConnOutFrames,
       "lecConnInFrames": lecConnInFrames,
       "lecCidDataTable": lecCidDataTable,
       "lecCidDataEntry": lecCidDataEntry,
       "lecCustomerIdentifier": lecCustomerIdentifier,
       "lecIfEntryTable": lecIfEntryTable,
       "lecIfEntryEntry": lecIfEntryEntry,
       "lecIfAdminStatus": lecIfAdminStatus,
       "lecIfIndex": lecIfIndex,
       "lecMpTable": lecMpTable,
       "lecMpEntry": lecMpEntry,
       "lecLinkToProtocolPort": lecLinkToProtocolPort,
       "lecProvTable": lecProvTable,
       "lecProvEntry": lecProvEntry,
       "lecLanType": lecLanType,
       "lecMaxFrameSize": lecMaxFrameSize,
       "lecLanName": lecLanName,
       "lecV2Capable": lecV2Capable,
       "lecLecsAddress": lecLecsAddress,
       "lecLesAddress": lecLesAddress,
       "lecMaxDataSvcs": lecMaxDataSvcs,
       "lecMaxArpEntries": lecMaxArpEntries,
       "lecIlsForwarder": lecIlsForwarder,
       "lecStateTable": lecStateTable,
       "lecStateEntry": lecStateEntry,
       "lecAdminState": lecAdminState,
       "lecOperationalState": lecOperationalState,
       "lecUsageState": lecUsageState,
       "lecOperStatusTable": lecOperStatusTable,
       "lecOperStatusEntry": lecOperStatusEntry,
       "lecSnmpOperStatus": lecSnmpOperStatus,
       "lecOperTable": lecOperTable,
       "lecOperEntry": lecOperEntry,
       "lecActualLanType": lecActualLanType,
       "lecActualMaxFrameSize": lecActualMaxFrameSize,
       "lecActualLanName": lecActualLanName,
       "lecElanId": lecElanId,
       "lecActualV2Capable": lecActualV2Capable,
       "lecConfigurationSource": lecConfigurationSource,
       "lecActualLecsAddress": lecActualLecsAddress,
       "lecActualLesAddress": lecActualLesAddress,
       "lecAtmAddress": lecAtmAddress,
       "lecMacAddress": lecMacAddress,
       "lecLecId": lecLecId,
       "lecInterfaceState": lecInterfaceState,
       "lecLastFailureResponseCode": lecLastFailureResponseCode,
       "lecLastFailureState": lecLastFailureState,
       "lecStatsTable": lecStatsTable,
       "lecStatsEntry": lecStatsEntry,
       "lecArpRequestsOut": lecArpRequestsOut,
       "lecArpRepliesIn": lecArpRepliesIn,
       "lecArpRequestsIn": lecArpRequestsIn,
       "lecArpRepliesOut": lecArpRepliesOut,
       "lecControlFramesOut": lecControlFramesOut,
       "lecControlFramesIn": lecControlFramesIn,
       "lecSvcFailures": lecSvcFailures,
       "lecCurrDataSvcs": lecCurrDataSvcs,
       "lecPeakDataSvcs": lecPeakDataSvcs,
       "lecCurrArpEntries": lecCurrArpEntries,
       "lecPeakArpEntries": lecPeakArpEntries,
       "lecBadControlFrames": lecBadControlFrames,
       "lecProtocolViolations": lecProtocolViolations,
       "lecUnsupportedTlvs": lecUnsupportedTlvs,
       "laneClientMIB": laneClientMIB,
       "laneClientGroup": laneClientGroup,
       "laneClientGroupBE": laneClientGroupBE,
       "laneClientGroupBE00": laneClientGroupBE00,
       "laneClientGroupBE00A": laneClientGroupBE00A,
       "laneClientCapabilities": laneClientCapabilities,
       "laneClientCapabilitiesBE": laneClientCapabilitiesBE,
       "laneClientCapabilitiesBE00": laneClientCapabilitiesBE00,
       "laneClientCapabilitiesBE00A": laneClientCapabilitiesBE00A}
)
