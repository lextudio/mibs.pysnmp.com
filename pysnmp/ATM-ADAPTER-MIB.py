# SNMP MIB module (ATM-ADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-ADAPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:47 2024
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_AtmAdapter_ObjectIdentity = ObjectIdentity
atmAdapter = _AtmAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29)
)
_AtmAdapterAdmin_ObjectIdentity = ObjectIdentity
atmAdapterAdmin = _AtmAdapterAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1)
)
_AtmfTrap_ObjectIdentity = ObjectIdentity
atmfTrap = _AtmfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1)
)
_MuxatmTrap_Type = Integer32
_MuxatmTrap_Object = MibScalar
muxatmTrap = _MuxatmTrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 1),
    _MuxatmTrap_Type()
)
muxatmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxatmTrap.setStatus("mandatory")
_MuxatmString_Type = DisplayString
_MuxatmString_Object = MibScalar
muxatmString = _MuxatmString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 2),
    _MuxatmString_Type()
)
muxatmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxatmString.setStatus("mandatory")
_AtmfTransmissionTypes_ObjectIdentity = ObjectIdentity
atmfTransmissionTypes = _AtmfTransmissionTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2)
)
_AtmfUnknownType_ObjectIdentity = ObjectIdentity
atmfUnknownType = _AtmfUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 1)
)
_AtmfSonetSTS3c_ObjectIdentity = ObjectIdentity
atmfSonetSTS3c = _AtmfSonetSTS3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 2)
)
_AtmfDs3_ObjectIdentity = ObjectIdentity
atmfDs3 = _AtmfDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 3)
)
_Atmf4B5B_ObjectIdentity = ObjectIdentity
atmf4B5B = _Atmf4B5B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 4)
)
_Atmf8B10B_ObjectIdentity = ObjectIdentity
atmf8B10B = _Atmf8B10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 5)
)
_AtmfMediaTypes_ObjectIdentity = ObjectIdentity
atmfMediaTypes = _AtmfMediaTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3)
)
_AtmfMediaUnknownType_ObjectIdentity = ObjectIdentity
atmfMediaUnknownType = _AtmfMediaUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 1)
)
_AtmfMediaCoaxCable_ObjectIdentity = ObjectIdentity
atmfMediaCoaxCable = _AtmfMediaCoaxCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 2)
)
_AtmfMediaSingleMode_ObjectIdentity = ObjectIdentity
atmfMediaSingleMode = _AtmfMediaSingleMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 3)
)
_AtmfMediaMultiMode_ObjectIdentity = ObjectIdentity
atmfMediaMultiMode = _AtmfMediaMultiMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 4)
)
_AtmfMediaStp_ObjectIdentity = ObjectIdentity
atmfMediaStp = _AtmfMediaStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 5)
)
_AtmfMediaUtp_ObjectIdentity = ObjectIdentity
atmfMediaUtp = _AtmfMediaUtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 6)
)
_AtmfTypes_ObjectIdentity = ObjectIdentity
atmfTypes = _AtmfTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4)
)
_AtmfUnknownAdapterType_ObjectIdentity = ObjectIdentity
atmfUnknownAdapterType = _AtmfUnknownAdapterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 1)
)
_AtmfTurbowaysATM_100_ObjectIdentity = ObjectIdentity
atmfTurbowaysATM_100 = _AtmfTurbowaysATM_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 2)
)
_AtmAdapterMib_ObjectIdentity = ObjectIdentity
atmAdapterMib = _AtmAdapterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2)
)
_AtmfAdapterGroup_ObjectIdentity = ObjectIdentity
atmfAdapterGroup = _AtmfAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1)
)
_AtmfAdapterTable_Object = MibTable
atmfAdapterTable = _AtmfAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmfAdapterTable.setStatus("mandatory")
_AtmfAdapterEntry_Object = MibTableRow
atmfAdapterEntry = _AtmfAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1)
)
atmfAdapterEntry.setIndexNames(
    (0, "ATM-ADAPTER-MIB", "atmfAdapterIndex"),
)
if mibBuilder.loadTexts:
    atmfAdapterEntry.setStatus("mandatory")
_AtmfAdapterIndex_Type = Integer32
_AtmfAdapterIndex_Object = MibTableColumn
atmfAdapterIndex = _AtmfAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 1),
    _AtmfAdapterIndex_Type()
)
atmfAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterIndex.setStatus("mandatory")
_AtmfAdapterSerialNumber_Type = Integer32
_AtmfAdapterSerialNumber_Object = MibTableColumn
atmfAdapterSerialNumber = _AtmfAdapterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 2),
    _AtmfAdapterSerialNumber_Type()
)
atmfAdapterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterSerialNumber.setStatus("mandatory")
_AtmfAdapterDiagVersion_Type = Integer32
_AtmfAdapterDiagVersion_Object = MibTableColumn
atmfAdapterDiagVersion = _AtmfAdapterDiagVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 3),
    _AtmfAdapterDiagVersion_Type()
)
atmfAdapterDiagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterDiagVersion.setStatus("mandatory")
_AtmfAdapterSoftwareVersion_Type = Integer32
_AtmfAdapterSoftwareVersion_Object = MibTableColumn
atmfAdapterSoftwareVersion = _AtmfAdapterSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 4),
    _AtmfAdapterSoftwareVersion_Type()
)
atmfAdapterSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterSoftwareVersion.setStatus("mandatory")


class _AtmfAdapterTransmitBufSize_Type(Integer32):
    """Custom type atmfAdapterTransmitBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9180),
    )


_AtmfAdapterTransmitBufSize_Type.__name__ = "Integer32"
_AtmfAdapterTransmitBufSize_Object = MibTableColumn
atmfAdapterTransmitBufSize = _AtmfAdapterTransmitBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 5),
    _AtmfAdapterTransmitBufSize_Type()
)
atmfAdapterTransmitBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterTransmitBufSize.setStatus("mandatory")


class _AtmfAdapterReceiveBufSize_Type(Integer32):
    """Custom type atmfAdapterReceiveBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9180),
    )


_AtmfAdapterReceiveBufSize_Type.__name__ = "Integer32"
_AtmfAdapterReceiveBufSize_Object = MibTableColumn
atmfAdapterReceiveBufSize = _AtmfAdapterReceiveBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 6),
    _AtmfAdapterReceiveBufSize_Type()
)
atmfAdapterReceiveBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterReceiveBufSize.setStatus("mandatory")
_AtmfAdapterTransmissionType_Type = ObjectIdentifier
_AtmfAdapterTransmissionType_Object = MibTableColumn
atmfAdapterTransmissionType = _AtmfAdapterTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 7),
    _AtmfAdapterTransmissionType_Type()
)
atmfAdapterTransmissionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterTransmissionType.setStatus("mandatory")
_AtmfAdapterMediaType_Type = ObjectIdentifier
_AtmfAdapterMediaType_Object = MibTableColumn
atmfAdapterMediaType = _AtmfAdapterMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 8),
    _AtmfAdapterMediaType_Type()
)
atmfAdapterMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterMediaType.setStatus("mandatory")


class _AtmfAdapterOperStatus_Type(Integer32):
    """Custom type atmfAdapterOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("loopBack", 4),
          ("other", 1),
          ("outOfService", 3))
    )


_AtmfAdapterOperStatus_Type.__name__ = "Integer32"
_AtmfAdapterOperStatus_Object = MibTableColumn
atmfAdapterOperStatus = _AtmfAdapterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 9),
    _AtmfAdapterOperStatus_Type()
)
atmfAdapterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterOperStatus.setStatus("mandatory")
_AtmfAdapterType_Type = ObjectIdentifier
_AtmfAdapterType_Object = MibTableColumn
atmfAdapterType = _AtmfAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 10),
    _AtmfAdapterType_Type()
)
atmfAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAdapterType.setStatus("mandatory")
_AtmfAtmLayerGroup_ObjectIdentity = ObjectIdentity
atmfAtmLayerGroup = _AtmfAtmLayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2)
)
_AtmfAtmLayerTable_Object = MibTable
atmfAtmLayerTable = _AtmfAtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmfAtmLayerTable.setStatus("mandatory")
_AtmfAtmLayerEntry_Object = MibTableRow
atmfAtmLayerEntry = _AtmfAtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1)
)
atmfAtmLayerEntry.setIndexNames(
    (0, "ATM-ADAPTER-MIB", "atmfAtmLayerIndex"),
)
if mibBuilder.loadTexts:
    atmfAtmLayerEntry.setStatus("mandatory")
_AtmfAtmLayerIndex_Type = Integer32
_AtmfAtmLayerIndex_Object = MibTableColumn
atmfAtmLayerIndex = _AtmfAtmLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 1),
    _AtmfAtmLayerIndex_Type()
)
atmfAtmLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerIndex.setStatus("mandatory")


class _AtmfAtmLayerMaxVPCs_Type(Integer32):
    """Custom type atmfAtmLayerMaxVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfAtmLayerMaxVPCs_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVPCs_Object = MibTableColumn
atmfAtmLayerMaxVPCs = _AtmfAtmLayerMaxVPCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 2),
    _AtmfAtmLayerMaxVPCs_Type()
)
atmfAtmLayerMaxVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVPCs.setStatus("mandatory")


class _AtmfAtmLayerMaxVCCs_Type(Integer32):
    """Custom type atmfAtmLayerMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmfAtmLayerMaxVCCs_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVCCs_Object = MibTableColumn
atmfAtmLayerMaxVCCs = _AtmfAtmLayerMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 3),
    _AtmfAtmLayerMaxVCCs_Type()
)
atmfAtmLayerMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVCCs.setStatus("mandatory")


class _AtmfAtmLayerConfiguredVPCs_Type(Integer32):
    """Custom type atmfAtmLayerConfiguredVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfAtmLayerConfiguredVPCs_Type.__name__ = "Integer32"
_AtmfAtmLayerConfiguredVPCs_Object = MibTableColumn
atmfAtmLayerConfiguredVPCs = _AtmfAtmLayerConfiguredVPCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 4),
    _AtmfAtmLayerConfiguredVPCs_Type()
)
atmfAtmLayerConfiguredVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerConfiguredVPCs.setStatus("mandatory")


class _AtmfAtmLayerConfiguredVCCs_Type(Integer32):
    """Custom type atmfAtmLayerConfiguredVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmfAtmLayerConfiguredVCCs_Type.__name__ = "Integer32"
_AtmfAtmLayerConfiguredVCCs_Object = MibTableColumn
atmfAtmLayerConfiguredVCCs = _AtmfAtmLayerConfiguredVCCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 5),
    _AtmfAtmLayerConfiguredVCCs_Type()
)
atmfAtmLayerConfiguredVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerConfiguredVCCs.setStatus("mandatory")


class _AtmfAtmLayerMaxVpiBits_Type(Integer32):
    """Custom type atmfAtmLayerMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AtmfAtmLayerMaxVpiBits_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVpiBits_Object = MibTableColumn
atmfAtmLayerMaxVpiBits = _AtmfAtmLayerMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 6),
    _AtmfAtmLayerMaxVpiBits_Type()
)
atmfAtmLayerMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVpiBits.setStatus("mandatory")


class _AtmfAtmLayerMaxVciBits_Type(Integer32):
    """Custom type atmfAtmLayerMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmfAtmLayerMaxVciBits_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVciBits_Object = MibTableColumn
atmfAtmLayerMaxVciBits = _AtmfAtmLayerMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 7),
    _AtmfAtmLayerMaxVciBits_Type()
)
atmfAtmLayerMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVciBits.setStatus("mandatory")


class _AtmfAtmLayerUniType_Type(Integer32):
    """Custom type atmfAtmLayerUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_AtmfAtmLayerUniType_Type.__name__ = "Integer32"
_AtmfAtmLayerUniType_Object = MibTableColumn
atmfAtmLayerUniType = _AtmfAtmLayerUniType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 8),
    _AtmfAtmLayerUniType_Type()
)
atmfAtmLayerUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerUniType.setStatus("mandatory")
_AtmfAtmStatsGroup_ObjectIdentity = ObjectIdentity
atmfAtmStatsGroup = _AtmfAtmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3)
)
_AtmfAtmStatsTable_Object = MibTable
atmfAtmStatsTable = _AtmfAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1)
)
if mibBuilder.loadTexts:
    atmfAtmStatsTable.setStatus("mandatory")
_AtmfAtmStatsEntry_Object = MibTableRow
atmfAtmStatsEntry = _AtmfAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1)
)
atmfAtmStatsEntry.setIndexNames(
    (0, "ATM-ADAPTER-MIB", "atmfAtmStatsIndex"),
)
if mibBuilder.loadTexts:
    atmfAtmStatsEntry.setStatus("mandatory")
_AtmfAtmStatsIndex_Type = Integer32
_AtmfAtmStatsIndex_Object = MibTableColumn
atmfAtmStatsIndex = _AtmfAtmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 1),
    _AtmfAtmStatsIndex_Type()
)
atmfAtmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmStatsIndex.setStatus("mandatory")
_AtmfAtmStatsReceivedCells_Type = Counter32
_AtmfAtmStatsReceivedCells_Object = MibTableColumn
atmfAtmStatsReceivedCells = _AtmfAtmStatsReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 2),
    _AtmfAtmStatsReceivedCells_Type()
)
atmfAtmStatsReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmStatsReceivedCells.setStatus("mandatory")
_AtmfAtmStatsDroppedPackets_Type = Counter32
_AtmfAtmStatsDroppedPackets_Object = MibTableColumn
atmfAtmStatsDroppedPackets = _AtmfAtmStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 3),
    _AtmfAtmStatsDroppedPackets_Type()
)
atmfAtmStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmStatsDroppedPackets.setStatus("mandatory")
_AtmfAtmStatsTransmittedCells_Type = Counter32
_AtmfAtmStatsTransmittedCells_Object = MibTableColumn
atmfAtmStatsTransmittedCells = _AtmfAtmStatsTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 4),
    _AtmfAtmStatsTransmittedCells_Type()
)
atmfAtmStatsTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmStatsTransmittedCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-ADAPTER-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "atmAdapter": atmAdapter,
       "atmAdapterAdmin": atmAdapterAdmin,
       "atmfTrap": atmfTrap,
       "muxatmTrap": muxatmTrap,
       "muxatmString": muxatmString,
       "atmfTransmissionTypes": atmfTransmissionTypes,
       "atmfUnknownType": atmfUnknownType,
       "atmfSonetSTS3c": atmfSonetSTS3c,
       "atmfDs3": atmfDs3,
       "atmf4B5B": atmf4B5B,
       "atmf8B10B": atmf8B10B,
       "atmfMediaTypes": atmfMediaTypes,
       "atmfMediaUnknownType": atmfMediaUnknownType,
       "atmfMediaCoaxCable": atmfMediaCoaxCable,
       "atmfMediaSingleMode": atmfMediaSingleMode,
       "atmfMediaMultiMode": atmfMediaMultiMode,
       "atmfMediaStp": atmfMediaStp,
       "atmfMediaUtp": atmfMediaUtp,
       "atmfTypes": atmfTypes,
       "atmfUnknownAdapterType": atmfUnknownAdapterType,
       "atmfTurbowaysATM-100": atmfTurbowaysATM_100,
       "atmAdapterMib": atmAdapterMib,
       "atmfAdapterGroup": atmfAdapterGroup,
       "atmfAdapterTable": atmfAdapterTable,
       "atmfAdapterEntry": atmfAdapterEntry,
       "atmfAdapterIndex": atmfAdapterIndex,
       "atmfAdapterSerialNumber": atmfAdapterSerialNumber,
       "atmfAdapterDiagVersion": atmfAdapterDiagVersion,
       "atmfAdapterSoftwareVersion": atmfAdapterSoftwareVersion,
       "atmfAdapterTransmitBufSize": atmfAdapterTransmitBufSize,
       "atmfAdapterReceiveBufSize": atmfAdapterReceiveBufSize,
       "atmfAdapterTransmissionType": atmfAdapterTransmissionType,
       "atmfAdapterMediaType": atmfAdapterMediaType,
       "atmfAdapterOperStatus": atmfAdapterOperStatus,
       "atmfAdapterType": atmfAdapterType,
       "atmfAtmLayerGroup": atmfAtmLayerGroup,
       "atmfAtmLayerTable": atmfAtmLayerTable,
       "atmfAtmLayerEntry": atmfAtmLayerEntry,
       "atmfAtmLayerIndex": atmfAtmLayerIndex,
       "atmfAtmLayerMaxVPCs": atmfAtmLayerMaxVPCs,
       "atmfAtmLayerMaxVCCs": atmfAtmLayerMaxVCCs,
       "atmfAtmLayerConfiguredVPCs": atmfAtmLayerConfiguredVPCs,
       "atmfAtmLayerConfiguredVCCs": atmfAtmLayerConfiguredVCCs,
       "atmfAtmLayerMaxVpiBits": atmfAtmLayerMaxVpiBits,
       "atmfAtmLayerMaxVciBits": atmfAtmLayerMaxVciBits,
       "atmfAtmLayerUniType": atmfAtmLayerUniType,
       "atmfAtmStatsGroup": atmfAtmStatsGroup,
       "atmfAtmStatsTable": atmfAtmStatsTable,
       "atmfAtmStatsEntry": atmfAtmStatsEntry,
       "atmfAtmStatsIndex": atmfAtmStatsIndex,
       "atmfAtmStatsReceivedCells": atmfAtmStatsReceivedCells,
       "atmfAtmStatsDroppedPackets": atmfAtmStatsDroppedPackets,
       "atmfAtmStatsTransmittedCells": atmfAtmStatsTransmittedCells}
)
