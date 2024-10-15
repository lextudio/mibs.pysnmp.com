# SNMP MIB module (Fore-Adapter-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Adapter-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:48 2024
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

(EntryStatus,
 NsapAddr,
 SpansAddress,
 systems) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "EntryStatus",
    "NsapAddr",
    "SpansAddress",
    "systems")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmAdapter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1)
)


# Types definitions



class IpHeader(OctetString):
    """Custom type IpHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdapterGroup_ObjectIdentity = ObjectIdentity
adapterGroup = _AdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1)
)
_AdapterTable_Object = MibTable
adapterTable = _AdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adapterTable.setStatus("current")
_AdapterEntry_Object = MibTableRow
adapterEntry = _AdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1)
)
adapterEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "adapterInterface"),
)
if mibBuilder.loadTexts:
    adapterEntry.setStatus("current")
_AdapterInterface_Type = Integer32
_AdapterInterface_Object = MibTableColumn
adapterInterface = _AdapterInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 1),
    _AdapterInterface_Type()
)
adapterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterInterface.setStatus("current")
_AdapterSerialNumber_Type = Integer32
_AdapterSerialNumber_Object = MibTableColumn
adapterSerialNumber = _AdapterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 2),
    _AdapterSerialNumber_Type()
)
adapterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterSerialNumber.setStatus("current")
_AdapterHardwareVersion_Type = Integer32
_AdapterHardwareVersion_Object = MibTableColumn
adapterHardwareVersion = _AdapterHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 3),
    _AdapterHardwareVersion_Type()
)
adapterHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterHardwareVersion.setStatus("current")
_AdapterHardwareSpeed_Type = Integer32
_AdapterHardwareSpeed_Object = MibTableColumn
adapterHardwareSpeed = _AdapterHardwareSpeed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 4),
    _AdapterHardwareSpeed_Type()
)
adapterHardwareSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterHardwareSpeed.setStatus("current")
_AdapterFirmwareVersion_Type = Integer32
_AdapterFirmwareVersion_Object = MibTableColumn
adapterFirmwareVersion = _AdapterFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 5),
    _AdapterFirmwareVersion_Type()
)
adapterFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFirmwareVersion.setStatus("current")
_AdapterSoftwareVersion_Type = Integer32
_AdapterSoftwareVersion_Object = MibTableColumn
adapterSoftwareVersion = _AdapterSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 6),
    _AdapterSoftwareVersion_Type()
)
adapterSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterSoftwareVersion.setStatus("current")
_AdapterTransmitBufferSize_Type = Integer32
_AdapterTransmitBufferSize_Object = MibTableColumn
adapterTransmitBufferSize = _AdapterTransmitBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 7),
    _AdapterTransmitBufferSize_Type()
)
adapterTransmitBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTransmitBufferSize.setStatus("current")
_AdapterTransmitQueueLength_Type = Gauge32
_AdapterTransmitQueueLength_Object = MibTableColumn
adapterTransmitQueueLength = _AdapterTransmitQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 8),
    _AdapterTransmitQueueLength_Type()
)
adapterTransmitQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTransmitQueueLength.setStatus("current")
_AdapterReceiveBufferSize_Type = Integer32
_AdapterReceiveBufferSize_Object = MibTableColumn
adapterReceiveBufferSize = _AdapterReceiveBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 9),
    _AdapterReceiveBufferSize_Type()
)
adapterReceiveBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterReceiveBufferSize.setStatus("current")
_AdapterReceiveQueueLength_Type = Gauge32
_AdapterReceiveQueueLength_Object = MibTableColumn
adapterReceiveQueueLength = _AdapterReceiveQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 10),
    _AdapterReceiveQueueLength_Type()
)
adapterReceiveQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterReceiveQueueLength.setStatus("current")


class _AdapterOperStatus_Type(Integer32):
    """Custom type adapterOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_AdapterOperStatus_Type.__name__ = "Integer32"
_AdapterOperStatus_Object = MibTableColumn
adapterOperStatus = _AdapterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 11),
    _AdapterOperStatus_Type()
)
adapterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterOperStatus.setStatus("current")


class _AdapterCarrier_Type(Integer32):
    """Custom type adapterCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("carrier", 1),
          ("noCarrier", 2))
    )


_AdapterCarrier_Type.__name__ = "Integer32"
_AdapterCarrier_Object = MibTableColumn
adapterCarrier = _AdapterCarrier_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 12),
    _AdapterCarrier_Type()
)
adapterCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterCarrier.setStatus("current")
_AdapterAddress_Type = SpansAddress
_AdapterAddress_Object = MibTableColumn
adapterAddress = _AdapterAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 13),
    _AdapterAddress_Type()
)
adapterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterAddress.setStatus("current")
_AdapterUptime_Type = TimeTicks
_AdapterUptime_Object = MibTableColumn
adapterUptime = _AdapterUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 14),
    _AdapterUptime_Type()
)
adapterUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterUptime.setStatus("current")


class _AdapterPhyLayer_Type(Integer32):
    """Custom type adapterPhyLayer based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("phy-4B5B-MMODE-100", 1),
          ("phy-4B5B-MMODE-140", 2),
          ("phy-4B5B-SMODE-100", 6),
          ("phy-4B5B-SMODE-140", 7),
          ("phy-ASX-100", 3),
          ("phy-OC3-MMODE-SC", 5),
          ("phy-OC3-MMODE-ST", 4),
          ("phy-OC3-SMODE-LONG", 9),
          ("phy-OC3-SMODE-SHORT", 8),
          ("phy-STP1-SONET", 11),
          ("phy-UTP5-SONET", 10))
    )


_AdapterPhyLayer_Type.__name__ = "Integer32"
_AdapterPhyLayer_Object = MibTableColumn
adapterPhyLayer = _AdapterPhyLayer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 15),
    _AdapterPhyLayer_Type()
)
adapterPhyLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterPhyLayer.setStatus("current")


class _AdapterType_Type(Integer32):
    """Custom type adapterType based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("type-ASX-100", 5),
          ("type-ASX-200", 10),
          ("type-ESA-200", 8),
          ("type-ESA-200PC", 12),
          ("type-ESA-200e", 17),
          ("type-GIA-100", 2),
          ("type-GIA-200", 15),
          ("type-GIA-200e", 18),
          ("type-HPA-200", 11),
          ("type-LANNET", 20),
          ("type-MCA-200", 9),
          ("type-MCA-200e", 22),
          ("type-NBA-200", 13),
          ("type-NXA-100", 4),
          ("type-PCA-200", 14),
          ("type-PCA-200e", 19),
          ("type-SBA-100", 1),
          ("type-SBA-200", 6),
          ("type-SBA-200e", 16),
          ("type-TCA-100", 3),
          ("type-VMA-200", 7),
          ("type-VMA-200e", 21))
    )


_AdapterType_Type.__name__ = "Integer32"
_AdapterType_Object = MibTableColumn
adapterType = _AdapterType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 16),
    _AdapterType_Type()
)
adapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterType.setStatus("current")
_AdapterFirmwareVersionText_Type = DisplayString
_AdapterFirmwareVersionText_Object = MibTableColumn
adapterFirmwareVersionText = _AdapterFirmwareVersionText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 17),
    _AdapterFirmwareVersionText_Type()
)
adapterFirmwareVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFirmwareVersionText.setStatus("current")
_AdapterSoftwareVersionText_Type = DisplayString
_AdapterSoftwareVersionText_Object = MibTableColumn
adapterSoftwareVersionText = _AdapterSoftwareVersionText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 1, 1, 1, 18),
    _AdapterSoftwareVersionText_Type()
)
adapterSoftwareVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterSoftwareVersionText.setStatus("current")
_PhyLayerGroup_ObjectIdentity = ObjectIdentity
phyLayerGroup = _PhyLayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2)
)
_PhyLayerTable_Object = MibTable
phyLayerTable = _PhyLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    phyLayerTable.setStatus("current")
_PhyLayerEntry_Object = MibTableRow
phyLayerEntry = _PhyLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2, 1, 1)
)
phyLayerEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "phyLayerInterface"),
)
if mibBuilder.loadTexts:
    phyLayerEntry.setStatus("current")
_PhyLayerInterface_Type = Integer32
_PhyLayerInterface_Object = MibTableColumn
phyLayerInterface = _PhyLayerInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2, 1, 1, 1),
    _PhyLayerInterface_Type()
)
phyLayerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLayerInterface.setStatus("current")
_PhyLayerFramingErrors_Type = Counter32
_PhyLayerFramingErrors_Object = MibTableColumn
phyLayerFramingErrors = _PhyLayerFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2, 1, 1, 2),
    _PhyLayerFramingErrors_Type()
)
phyLayerFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLayerFramingErrors.setStatus("current")
_PhyLayerHeaderCRCErrors_Type = Counter32
_PhyLayerHeaderCRCErrors_Object = MibTableColumn
phyLayerHeaderCRCErrors = _PhyLayerHeaderCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 2, 1, 1, 3),
    _PhyLayerHeaderCRCErrors_Type()
)
phyLayerHeaderCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyLayerHeaderCRCErrors.setStatus("current")
_AtmLayerGroup_ObjectIdentity = ObjectIdentity
atmLayerGroup = _AtmLayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3)
)
_AtmLayerTable_Object = MibTable
atmLayerTable = _AtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmLayerTable.setStatus("current")
_AtmLayerEntry_Object = MibTableRow
atmLayerEntry = _AtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1)
)
atmLayerEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "atmInterface"),
)
if mibBuilder.loadTexts:
    atmLayerEntry.setStatus("current")
_AtmInterface_Type = Integer32
_AtmInterface_Object = MibTableColumn
atmInterface = _AtmInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 1),
    _AtmInterface_Type()
)
atmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterface.setStatus("current")
_AtmTransmittedCells_Type = Counter32
_AtmTransmittedCells_Object = MibTableColumn
atmTransmittedCells = _AtmTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 2),
    _AtmTransmittedCells_Type()
)
atmTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTransmittedCells.setStatus("current")
_AtmReceivedCells_Type = Counter32
_AtmReceivedCells_Object = MibTableColumn
atmReceivedCells = _AtmReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 3),
    _AtmReceivedCells_Type()
)
atmReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmReceivedCells.setStatus("current")
_AtmOutOfRangeVPIs_Type = Counter32
_AtmOutOfRangeVPIs_Object = MibTableColumn
atmOutOfRangeVPIs = _AtmOutOfRangeVPIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 4),
    _AtmOutOfRangeVPIs_Type()
)
atmOutOfRangeVPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOutOfRangeVPIs.setStatus("current")
_AtmUnconnectedVPIs_Type = Counter32
_AtmUnconnectedVPIs_Object = MibTableColumn
atmUnconnectedVPIs = _AtmUnconnectedVPIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 5),
    _AtmUnconnectedVPIs_Type()
)
atmUnconnectedVPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmUnconnectedVPIs.setStatus("current")
_AtmOutOfRangeVCIs_Type = Counter32
_AtmOutOfRangeVCIs_Object = MibTableColumn
atmOutOfRangeVCIs = _AtmOutOfRangeVCIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 6),
    _AtmOutOfRangeVCIs_Type()
)
atmOutOfRangeVCIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOutOfRangeVCIs.setStatus("current")
_AtmUnconnectedVCIs_Type = Counter32
_AtmUnconnectedVCIs_Object = MibTableColumn
atmUnconnectedVCIs = _AtmUnconnectedVCIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 3, 1, 1, 7),
    _AtmUnconnectedVCIs_Type()
)
atmUnconnectedVCIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmUnconnectedVCIs.setStatus("current")
_AalGroup_ObjectIdentity = ObjectIdentity
aalGroup = _AalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4)
)
_Aal4Table_Object = MibTable
aal4Table = _Aal4Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aal4Table.setStatus("current")
_Aal4Entry_Object = MibTableRow
aal4Entry = _Aal4Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1)
)
aal4Entry.setIndexNames(
    (0, "Fore-Adapter-MIB", "aal4Interface"),
)
if mibBuilder.loadTexts:
    aal4Entry.setStatus("current")
_Aal4Interface_Type = Integer32
_Aal4Interface_Object = MibTableColumn
aal4Interface = _Aal4Interface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 1),
    _Aal4Interface_Type()
)
aal4Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4Interface.setStatus("current")
_Aal4TransmittedCells_Type = Counter32
_Aal4TransmittedCells_Object = MibTableColumn
aal4TransmittedCells = _Aal4TransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 2),
    _Aal4TransmittedCells_Type()
)
aal4TransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4TransmittedCells.setStatus("current")
_Aal4ReceivedCells_Type = Counter32
_Aal4ReceivedCells_Object = MibTableColumn
aal4ReceivedCells = _Aal4ReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 3),
    _Aal4ReceivedCells_Type()
)
aal4ReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4ReceivedCells.setStatus("current")
_Aal4TransmittedPDUs_Type = Counter32
_Aal4TransmittedPDUs_Object = MibTableColumn
aal4TransmittedPDUs = _Aal4TransmittedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 4),
    _Aal4TransmittedPDUs_Type()
)
aal4TransmittedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4TransmittedPDUs.setStatus("current")
_Aal4ReceivedPDUs_Type = Counter32
_Aal4ReceivedPDUs_Object = MibTableColumn
aal4ReceivedPDUs = _Aal4ReceivedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 5),
    _Aal4ReceivedPDUs_Type()
)
aal4ReceivedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4ReceivedPDUs.setStatus("current")
_Aal4PayloadCRCErrors_Type = Counter32
_Aal4PayloadCRCErrors_Object = MibTableColumn
aal4PayloadCRCErrors = _Aal4PayloadCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 6),
    _Aal4PayloadCRCErrors_Type()
)
aal4PayloadCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4PayloadCRCErrors.setStatus("current")
_Aal4SARProtocolErrors_Type = Counter32
_Aal4SARProtocolErrors_Object = MibTableColumn
aal4SARProtocolErrors = _Aal4SARProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 7),
    _Aal4SARProtocolErrors_Type()
)
aal4SARProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4SARProtocolErrors.setStatus("current")
_Aal4CSProtocolErrors_Type = Counter32
_Aal4CSProtocolErrors_Object = MibTableColumn
aal4CSProtocolErrors = _Aal4CSProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 8),
    _Aal4CSProtocolErrors_Type()
)
aal4CSProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4CSProtocolErrors.setStatus("current")
_Aal4CellsDiscards_Type = Counter32
_Aal4CellsDiscards_Object = MibTableColumn
aal4CellsDiscards = _Aal4CellsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 9),
    _Aal4CellsDiscards_Type()
)
aal4CellsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4CellsDiscards.setStatus("current")
_Aal4PDUsDiscards_Type = Counter32
_Aal4PDUsDiscards_Object = MibTableColumn
aal4PDUsDiscards = _Aal4PDUsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 1, 1, 10),
    _Aal4PDUsDiscards_Type()
)
aal4PDUsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal4PDUsDiscards.setStatus("current")
_Aal5Table_Object = MibTable
aal5Table = _Aal5Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    aal5Table.setStatus("current")
_Aal5Entry_Object = MibTableRow
aal5Entry = _Aal5Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1)
)
aal5Entry.setIndexNames(
    (0, "Fore-Adapter-MIB", "aal5Interface"),
)
if mibBuilder.loadTexts:
    aal5Entry.setStatus("current")
_Aal5Interface_Type = Integer32
_Aal5Interface_Object = MibTableColumn
aal5Interface = _Aal5Interface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 1),
    _Aal5Interface_Type()
)
aal5Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5Interface.setStatus("current")
_Aal5TransmittedCells_Type = Counter32
_Aal5TransmittedCells_Object = MibTableColumn
aal5TransmittedCells = _Aal5TransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 2),
    _Aal5TransmittedCells_Type()
)
aal5TransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5TransmittedCells.setStatus("current")
_Aal5ReceivedCells_Type = Counter32
_Aal5ReceivedCells_Object = MibTableColumn
aal5ReceivedCells = _Aal5ReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 3),
    _Aal5ReceivedCells_Type()
)
aal5ReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5ReceivedCells.setStatus("current")
_Aal5TransmittedPDUs_Type = Counter32
_Aal5TransmittedPDUs_Object = MibTableColumn
aal5TransmittedPDUs = _Aal5TransmittedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 4),
    _Aal5TransmittedPDUs_Type()
)
aal5TransmittedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5TransmittedPDUs.setStatus("current")
_Aal5ReceivedPDUs_Type = Counter32
_Aal5ReceivedPDUs_Object = MibTableColumn
aal5ReceivedPDUs = _Aal5ReceivedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 5),
    _Aal5ReceivedPDUs_Type()
)
aal5ReceivedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5ReceivedPDUs.setStatus("current")
_Aal5CRCErrors_Type = Counter32
_Aal5CRCErrors_Object = MibTableColumn
aal5CRCErrors = _Aal5CRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 6),
    _Aal5CRCErrors_Type()
)
aal5CRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CRCErrors.setStatus("current")
_Aal5CSProtocolErrors_Type = Counter32
_Aal5CSProtocolErrors_Object = MibTableColumn
aal5CSProtocolErrors = _Aal5CSProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 7),
    _Aal5CSProtocolErrors_Type()
)
aal5CSProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CSProtocolErrors.setStatus("current")
_Aal5CellsDiscards_Type = Counter32
_Aal5CellsDiscards_Object = MibTableColumn
aal5CellsDiscards = _Aal5CellsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 8),
    _Aal5CellsDiscards_Type()
)
aal5CellsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CellsDiscards.setStatus("current")
_Aal5PDUsDiscards_Type = Counter32
_Aal5PDUsDiscards_Object = MibTableColumn
aal5PDUsDiscards = _Aal5PDUsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 2, 1, 9),
    _Aal5PDUsDiscards_Type()
)
aal5PDUsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5PDUsDiscards.setStatus("current")
_Aal0Table_Object = MibTable
aal0Table = _Aal0Table_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    aal0Table.setStatus("current")
_Aal0Entry_Object = MibTableRow
aal0Entry = _Aal0Entry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3, 1)
)
aal0Entry.setIndexNames(
    (0, "Fore-Adapter-MIB", "aal0Interface"),
)
if mibBuilder.loadTexts:
    aal0Entry.setStatus("current")
_Aal0Interface_Type = Integer32
_Aal0Interface_Object = MibTableColumn
aal0Interface = _Aal0Interface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3, 1, 1),
    _Aal0Interface_Type()
)
aal0Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal0Interface.setStatus("current")
_Aal0TransmittedCells_Type = Counter32
_Aal0TransmittedCells_Object = MibTableColumn
aal0TransmittedCells = _Aal0TransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3, 1, 2),
    _Aal0TransmittedCells_Type()
)
aal0TransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal0TransmittedCells.setStatus("current")
_Aal0ReceivedCells_Type = Counter32
_Aal0ReceivedCells_Object = MibTableColumn
aal0ReceivedCells = _Aal0ReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3, 1, 3),
    _Aal0ReceivedCells_Type()
)
aal0ReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal0ReceivedCells.setStatus("current")
_Aal0CellsDiscards_Type = Counter32
_Aal0CellsDiscards_Object = MibTableColumn
aal0CellsDiscards = _Aal0CellsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 4, 3, 1, 4),
    _Aal0CellsDiscards_Type()
)
aal0CellsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal0CellsDiscards.setStatus("current")
_ConnGroup_ObjectIdentity = ObjectIdentity
connGroup = _ConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5)
)
_ConnTable_Object = MibTable
connTable = _ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    connTable.setStatus("current")
_ConnEntry_Object = MibTableRow
connEntry = _ConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1)
)
connEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "connInterface"),
    (0, "Fore-Adapter-MIB", "connDirection"),
    (0, "Fore-Adapter-MIB", "connVPI"),
    (0, "Fore-Adapter-MIB", "connVCI"),
)
if mibBuilder.loadTexts:
    connEntry.setStatus("current")
_ConnInterface_Type = Integer32
_ConnInterface_Object = MibTableColumn
connInterface = _ConnInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 1),
    _ConnInterface_Type()
)
connInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connInterface.setStatus("current")


class _ConnDirection_Type(Integer32):
    """Custom type connDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_ConnDirection_Type.__name__ = "Integer32"
_ConnDirection_Object = MibTableColumn
connDirection = _ConnDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 2),
    _ConnDirection_Type()
)
connDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connDirection.setStatus("current")
_ConnVPI_Type = Integer32
_ConnVPI_Object = MibTableColumn
connVPI = _ConnVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 3),
    _ConnVPI_Type()
)
connVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVPI.setStatus("current")
_ConnVCI_Type = Integer32
_ConnVCI_Object = MibTableColumn
connVCI = _ConnVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 4),
    _ConnVCI_Type()
)
connVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVCI.setStatus("current")
_ConnLocalSAP_Type = Integer32
_ConnLocalSAP_Object = MibTableColumn
connLocalSAP = _ConnLocalSAP_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 5),
    _ConnLocalSAP_Type()
)
connLocalSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalSAP.setStatus("current")
_ConnRemoteSAP_Type = Integer32
_ConnRemoteSAP_Object = MibTableColumn
connRemoteSAP = _ConnRemoteSAP_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 6),
    _ConnRemoteSAP_Type()
)
connRemoteSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteSAP.setStatus("current")
_ConnRemoteAddress_Type = SpansAddress
_ConnRemoteAddress_Object = MibTableColumn
connRemoteAddress = _ConnRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 7),
    _ConnRemoteAddress_Type()
)
connRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteAddress.setStatus("current")
_ConnPeakBandwidth_Type = Integer32
_ConnPeakBandwidth_Object = MibTableColumn
connPeakBandwidth = _ConnPeakBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 8),
    _ConnPeakBandwidth_Type()
)
connPeakBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPeakBandwidth.setStatus("current")
_ConnMeanBandwidth_Type = Integer32
_ConnMeanBandwidth_Object = MibTableColumn
connMeanBandwidth = _ConnMeanBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 9),
    _ConnMeanBandwidth_Type()
)
connMeanBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMeanBandwidth.setStatus("current")
_ConnMeanBurst_Type = Integer32
_ConnMeanBurst_Object = MibTableColumn
connMeanBurst = _ConnMeanBurst_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 10),
    _ConnMeanBurst_Type()
)
connMeanBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMeanBurst.setStatus("current")
_ConnUptime_Type = TimeTicks
_ConnUptime_Object = MibTableColumn
connUptime = _ConnUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 5, 1, 1, 11),
    _ConnUptime_Type()
)
connUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUptime.setStatus("current")
_SonetGroup_ObjectIdentity = ObjectIdentity
sonetGroup = _SonetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 6)
)
_SonetAdapterConfGroup_ObjectIdentity = ObjectIdentity
sonetAdapterConfGroup = _SonetAdapterConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 6, 1)
)
_SonetAdapterStatsGroup_ObjectIdentity = ObjectIdentity
sonetAdapterStatsGroup = _SonetAdapterStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 6, 2)
)
_StatsGroup_ObjectIdentity = ObjectIdentity
statsGroup = _StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 7)
)
_AtmIpGroup_ObjectIdentity = ObjectIdentity
atmIpGroup = _AtmIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8)
)
_AtmarpGroup_ObjectIdentity = ObjectIdentity
atmarpGroup = _AtmarpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1)
)


class _AtmarpFlushTable_Type(Integer32):
    """Custom type atmarpFlushTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmarpFlushTable_Type.__name__ = "Integer32"
_AtmarpFlushTable_Object = MibScalar
atmarpFlushTable = _AtmarpFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 1),
    _AtmarpFlushTable_Type()
)
atmarpFlushTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpFlushTable.setStatus("current")
_AtmarpTable_Object = MibTable
atmarpTable = _AtmarpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    atmarpTable.setStatus("current")
_AtmarpEntry_Object = MibTableRow
atmarpEntry = _AtmarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1)
)
atmarpEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "atmarpIpAddress"),
)
if mibBuilder.loadTexts:
    atmarpEntry.setStatus("current")
_AtmarpIpAddress_Type = IpAddress
_AtmarpIpAddress_Object = MibTableColumn
atmarpIpAddress = _AtmarpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 1),
    _AtmarpIpAddress_Type()
)
atmarpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmarpIpAddress.setStatus("current")
_AtmarpInterface_Type = Integer32
_AtmarpInterface_Object = MibTableColumn
atmarpInterface = _AtmarpInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 2),
    _AtmarpInterface_Type()
)
atmarpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpInterface.setStatus("current")
_AtmarpSpansAddress_Type = SpansAddress
_AtmarpSpansAddress_Object = MibTableColumn
atmarpSpansAddress = _AtmarpSpansAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 3),
    _AtmarpSpansAddress_Type()
)
atmarpSpansAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmarpSpansAddress.setStatus("current")
_AtmarpNsapAddress_Type = NsapAddr
_AtmarpNsapAddress_Object = MibTableColumn
atmarpNsapAddress = _AtmarpNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 4),
    _AtmarpNsapAddress_Type()
)
atmarpNsapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpNsapAddress.setStatus("current")
_AtmarpVPI_Type = Integer32
_AtmarpVPI_Object = MibTableColumn
atmarpVPI = _AtmarpVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 5),
    _AtmarpVPI_Type()
)
atmarpVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpVPI.setStatus("current")
_AtmarpVCI_Type = Integer32
_AtmarpVCI_Object = MibTableColumn
atmarpVCI = _AtmarpVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 6),
    _AtmarpVCI_Type()
)
atmarpVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpVCI.setStatus("current")


class _AtmarpConnType_Type(Integer32):
    """Custom type atmarpConnType based on Integer32"""
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
        *(("classicalIpPVC", 3),
          ("classicalIpSVC", 4),
          ("foreIpPVC", 1),
          ("foreIpSVC", 2))
    )


_AtmarpConnType_Type.__name__ = "Integer32"
_AtmarpConnType_Object = MibTableColumn
atmarpConnType = _AtmarpConnType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 7),
    _AtmarpConnType_Type()
)
atmarpConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpConnType.setStatus("current")


class _AtmarpAALType_Type(Integer32):
    """Custom type atmarpAALType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal34", 1),
          ("aal5", 2))
    )


_AtmarpAALType_Type.__name__ = "Integer32"
_AtmarpAALType_Object = MibTableColumn
atmarpAALType = _AtmarpAALType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 8),
    _AtmarpAALType_Type()
)
atmarpAALType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpAALType.setStatus("current")
_AtmarpPeakBandwidth_Type = Integer32
_AtmarpPeakBandwidth_Object = MibTableColumn
atmarpPeakBandwidth = _AtmarpPeakBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 9),
    _AtmarpPeakBandwidth_Type()
)
atmarpPeakBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpPeakBandwidth.setStatus("current")


class _AtmarpConnDirection_Type(Integer32):
    """Custom type atmarpConnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("outgoing", 1),
          ("pending", 3))
    )


_AtmarpConnDirection_Type.__name__ = "Integer32"
_AtmarpConnDirection_Object = MibTableColumn
atmarpConnDirection = _AtmarpConnDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 10),
    _AtmarpConnDirection_Type()
)
atmarpConnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmarpConnDirection.setStatus("current")


class _AtmarpEntryValidity_Type(Integer32):
    """Custom type atmarpEntryValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtmarpEntryValidity_Type.__name__ = "Integer32"
_AtmarpEntryValidity_Object = MibTableColumn
atmarpEntryValidity = _AtmarpEntryValidity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 11),
    _AtmarpEntryValidity_Type()
)
atmarpEntryValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmarpEntryValidity.setStatus("current")


class _AtmarpEntryType_Type(Integer32):
    """Custom type atmarpEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AtmarpEntryType_Type.__name__ = "Integer32"
_AtmarpEntryType_Object = MibTableColumn
atmarpEntryType = _AtmarpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 12),
    _AtmarpEntryType_Type()
)
atmarpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmarpEntryType.setStatus("current")
_AtmarpEntryStatus_Type = EntryStatus
_AtmarpEntryStatus_Object = MibTableColumn
atmarpEntryStatus = _AtmarpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 1, 2, 1, 13),
    _AtmarpEntryStatus_Type()
)
atmarpEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmarpEntryStatus.setStatus("current")
_ClassicalIpGroup_ObjectIdentity = ObjectIdentity
classicalIpGroup = _ClassicalIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2)
)
_ClassicalIpArpTable_Object = MibTable
classicalIpArpTable = _ClassicalIpArpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    classicalIpArpTable.setStatus("current")
_ClassicalIpArpEntry_Object = MibTableRow
classicalIpArpEntry = _ClassicalIpArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1)
)
classicalIpArpEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "classicalIpArpIfIndex"),
    (0, "Fore-Adapter-MIB", "classicalIpArpServerIndex"),
)
if mibBuilder.loadTexts:
    classicalIpArpEntry.setStatus("current")
_ClassicalIpArpIfIndex_Type = Integer32
_ClassicalIpArpIfIndex_Object = MibTableColumn
classicalIpArpIfIndex = _ClassicalIpArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 1),
    _ClassicalIpArpIfIndex_Type()
)
classicalIpArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classicalIpArpIfIndex.setStatus("current")
_ClassicalIpArpServerIndex_Type = Integer32
_ClassicalIpArpServerIndex_Object = MibTableColumn
classicalIpArpServerIndex = _ClassicalIpArpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 2),
    _ClassicalIpArpServerIndex_Type()
)
classicalIpArpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classicalIpArpServerIndex.setStatus("current")


class _ClassicalIpArpServer_Type(Integer32):
    """Custom type classicalIpArpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ClassicalIpArpServer_Type.__name__ = "Integer32"
_ClassicalIpArpServer_Object = MibTableColumn
classicalIpArpServer = _ClassicalIpArpServer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 3),
    _ClassicalIpArpServer_Type()
)
classicalIpArpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classicalIpArpServer.setStatus("current")


class _ClassicalIpArpServerConfigType_Type(Integer32):
    """Custom type classicalIpArpServerConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualConfig", 1),
          ("wellKnown", 2))
    )


_ClassicalIpArpServerConfigType_Type.__name__ = "Integer32"
_ClassicalIpArpServerConfigType_Object = MibTableColumn
classicalIpArpServerConfigType = _ClassicalIpArpServerConfigType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 4),
    _ClassicalIpArpServerConfigType_Type()
)
classicalIpArpServerConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classicalIpArpServerConfigType.setStatus("current")
_ClassicalIpWellKnownArpServerAddr_Type = NsapAddr
_ClassicalIpWellKnownArpServerAddr_Object = MibTableColumn
classicalIpWellKnownArpServerAddr = _ClassicalIpWellKnownArpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 5),
    _ClassicalIpWellKnownArpServerAddr_Type()
)
classicalIpWellKnownArpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classicalIpWellKnownArpServerAddr.setStatus("current")
_ClassicalIpManualConfigArpServerAddr_Type = NsapAddr
_ClassicalIpManualConfigArpServerAddr_Object = MibTableColumn
classicalIpManualConfigArpServerAddr = _ClassicalIpManualConfigArpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 2, 1, 1, 6),
    _ClassicalIpManualConfigArpServerAddr_Type()
)
classicalIpManualConfigArpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classicalIpManualConfigArpServerAddr.setStatus("current")
_IpFilterGroup_ObjectIdentity = ObjectIdentity
ipFilterGroup = _IpFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3)
)
_IpFilterConfGroup_ObjectIdentity = ObjectIdentity
ipFilterConfGroup = _IpFilterConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1)
)
_IpFilterTable_Object = MibTable
ipFilterTable = _IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipFilterTable.setStatus("current")
_IpFilterEntry_Object = MibTableRow
ipFilterEntry = _IpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 1, 1)
)
ipFilterEntry.setIndexNames(
    (0, "Fore-Adapter-MIB", "ipFilterIpAddress"),
    (0, "Fore-Adapter-MIB", "ipFilterMask"),
)
if mibBuilder.loadTexts:
    ipFilterEntry.setStatus("current")
_IpFilterIpAddress_Type = IpAddress
_IpFilterIpAddress_Object = MibTableColumn
ipFilterIpAddress = _IpFilterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 1, 1, 1),
    _IpFilterIpAddress_Type()
)
ipFilterIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterIpAddress.setStatus("current")
_IpFilterMask_Type = IpAddress
_IpFilterMask_Object = MibTableColumn
ipFilterMask = _IpFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 1, 1, 2),
    _IpFilterMask_Type()
)
ipFilterMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterMask.setStatus("current")
_IpFilterRowStatus_Type = RowStatus
_IpFilterRowStatus_Object = MibTableColumn
ipFilterRowStatus = _IpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 1, 1, 3),
    _IpFilterRowStatus_Type()
)
ipFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterRowStatus.setStatus("current")


class _IpFilterNoSSR_Type(Integer32):
    """Custom type ipFilterNoSSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpFilterNoSSR_Type.__name__ = "Integer32"
_IpFilterNoSSR_Object = MibScalar
ipFilterNoSSR = _IpFilterNoSSR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 2),
    _IpFilterNoSSR_Type()
)
ipFilterNoSSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterNoSSR.setStatus("current")


class _IpFilterNoLSR_Type(Integer32):
    """Custom type ipFilterNoLSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpFilterNoLSR_Type.__name__ = "Integer32"
_IpFilterNoLSR_Object = MibScalar
ipFilterNoLSR = _IpFilterNoLSR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 3),
    _IpFilterNoLSR_Type()
)
ipFilterNoLSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterNoLSR.setStatus("current")


class _IpFilterNoInBand_Type(Integer32):
    """Custom type ipFilterNoInBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpFilterNoInBand_Type.__name__ = "Integer32"
_IpFilterNoInBand_Object = MibScalar
ipFilterNoInBand = _IpFilterNoInBand_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 1, 4),
    _IpFilterNoInBand_Type()
)
ipFilterNoInBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterNoInBand.setStatus("current")
_IpFilterStatsGroup_ObjectIdentity = ObjectIdentity
ipFilterStatsGroup = _IpFilterStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2)
)
_IpFilterStatsIpHeader_Type = IpHeader
_IpFilterStatsIpHeader_Object = MibScalar
ipFilterStatsIpHeader = _IpFilterStatsIpHeader_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 1),
    _IpFilterStatsIpHeader_Type()
)
ipFilterStatsIpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsIpHeader.setStatus("current")
_IpFilterStatsTimeOccured_Type = TimeTicks
_IpFilterStatsTimeOccured_Object = MibScalar
ipFilterStatsTimeOccured = _IpFilterStatsTimeOccured_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 2),
    _IpFilterStatsTimeOccured_Type()
)
ipFilterStatsTimeOccured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsTimeOccured.setStatus("current")
_IpFilterStatsViolations_Type = Counter32
_IpFilterStatsViolations_Object = MibScalar
ipFilterStatsViolations = _IpFilterStatsViolations_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 3),
    _IpFilterStatsViolations_Type()
)
ipFilterStatsViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsViolations.setStatus("current")
_IpFilterStatsVPI_Type = Integer32
_IpFilterStatsVPI_Object = MibScalar
ipFilterStatsVPI = _IpFilterStatsVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 4),
    _IpFilterStatsVPI_Type()
)
ipFilterStatsVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsVPI.setStatus("current")
_IpFilterStatsVCI_Type = Integer32
_IpFilterStatsVCI_Object = MibScalar
ipFilterStatsVCI = _IpFilterStatsVCI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 5),
    _IpFilterStatsVCI_Type()
)
ipFilterStatsVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsVCI.setStatus("current")
_IpFilterStatsIfName_Type = DisplayString
_IpFilterStatsIfName_Object = MibScalar
ipFilterStatsIfName = _IpFilterStatsIfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 6),
    _IpFilterStatsIfName_Type()
)
ipFilterStatsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsIfName.setStatus("current")
_IpFilterStatsReasonText_Type = DisplayString
_IpFilterStatsReasonText_Object = MibScalar
ipFilterStatsReasonText = _IpFilterStatsReasonText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 7),
    _IpFilterStatsReasonText_Type()
)
ipFilterStatsReasonText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsReasonText.setStatus("current")
_IpFilterStatsSrcIpAddr_Type = IpAddress
_IpFilterStatsSrcIpAddr_Object = MibScalar
ipFilterStatsSrcIpAddr = _IpFilterStatsSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 1, 8, 3, 2, 8),
    _IpFilterStatsSrcIpAddr_Type()
)
ipFilterStatsSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterStatsSrcIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Adapter-MIB",
    **{"IpHeader": IpHeader,
       "atmAdapter": atmAdapter,
       "adapterGroup": adapterGroup,
       "adapterTable": adapterTable,
       "adapterEntry": adapterEntry,
       "adapterInterface": adapterInterface,
       "adapterSerialNumber": adapterSerialNumber,
       "adapterHardwareVersion": adapterHardwareVersion,
       "adapterHardwareSpeed": adapterHardwareSpeed,
       "adapterFirmwareVersion": adapterFirmwareVersion,
       "adapterSoftwareVersion": adapterSoftwareVersion,
       "adapterTransmitBufferSize": adapterTransmitBufferSize,
       "adapterTransmitQueueLength": adapterTransmitQueueLength,
       "adapterReceiveBufferSize": adapterReceiveBufferSize,
       "adapterReceiveQueueLength": adapterReceiveQueueLength,
       "adapterOperStatus": adapterOperStatus,
       "adapterCarrier": adapterCarrier,
       "adapterAddress": adapterAddress,
       "adapterUptime": adapterUptime,
       "adapterPhyLayer": adapterPhyLayer,
       "adapterType": adapterType,
       "adapterFirmwareVersionText": adapterFirmwareVersionText,
       "adapterSoftwareVersionText": adapterSoftwareVersionText,
       "phyLayerGroup": phyLayerGroup,
       "phyLayerTable": phyLayerTable,
       "phyLayerEntry": phyLayerEntry,
       "phyLayerInterface": phyLayerInterface,
       "phyLayerFramingErrors": phyLayerFramingErrors,
       "phyLayerHeaderCRCErrors": phyLayerHeaderCRCErrors,
       "atmLayerGroup": atmLayerGroup,
       "atmLayerTable": atmLayerTable,
       "atmLayerEntry": atmLayerEntry,
       "atmInterface": atmInterface,
       "atmTransmittedCells": atmTransmittedCells,
       "atmReceivedCells": atmReceivedCells,
       "atmOutOfRangeVPIs": atmOutOfRangeVPIs,
       "atmUnconnectedVPIs": atmUnconnectedVPIs,
       "atmOutOfRangeVCIs": atmOutOfRangeVCIs,
       "atmUnconnectedVCIs": atmUnconnectedVCIs,
       "aalGroup": aalGroup,
       "aal4Table": aal4Table,
       "aal4Entry": aal4Entry,
       "aal4Interface": aal4Interface,
       "aal4TransmittedCells": aal4TransmittedCells,
       "aal4ReceivedCells": aal4ReceivedCells,
       "aal4TransmittedPDUs": aal4TransmittedPDUs,
       "aal4ReceivedPDUs": aal4ReceivedPDUs,
       "aal4PayloadCRCErrors": aal4PayloadCRCErrors,
       "aal4SARProtocolErrors": aal4SARProtocolErrors,
       "aal4CSProtocolErrors": aal4CSProtocolErrors,
       "aal4CellsDiscards": aal4CellsDiscards,
       "aal4PDUsDiscards": aal4PDUsDiscards,
       "aal5Table": aal5Table,
       "aal5Entry": aal5Entry,
       "aal5Interface": aal5Interface,
       "aal5TransmittedCells": aal5TransmittedCells,
       "aal5ReceivedCells": aal5ReceivedCells,
       "aal5TransmittedPDUs": aal5TransmittedPDUs,
       "aal5ReceivedPDUs": aal5ReceivedPDUs,
       "aal5CRCErrors": aal5CRCErrors,
       "aal5CSProtocolErrors": aal5CSProtocolErrors,
       "aal5CellsDiscards": aal5CellsDiscards,
       "aal5PDUsDiscards": aal5PDUsDiscards,
       "aal0Table": aal0Table,
       "aal0Entry": aal0Entry,
       "aal0Interface": aal0Interface,
       "aal0TransmittedCells": aal0TransmittedCells,
       "aal0ReceivedCells": aal0ReceivedCells,
       "aal0CellsDiscards": aal0CellsDiscards,
       "connGroup": connGroup,
       "connTable": connTable,
       "connEntry": connEntry,
       "connInterface": connInterface,
       "connDirection": connDirection,
       "connVPI": connVPI,
       "connVCI": connVCI,
       "connLocalSAP": connLocalSAP,
       "connRemoteSAP": connRemoteSAP,
       "connRemoteAddress": connRemoteAddress,
       "connPeakBandwidth": connPeakBandwidth,
       "connMeanBandwidth": connMeanBandwidth,
       "connMeanBurst": connMeanBurst,
       "connUptime": connUptime,
       "sonetGroup": sonetGroup,
       "sonetAdapterConfGroup": sonetAdapterConfGroup,
       "sonetAdapterStatsGroup": sonetAdapterStatsGroup,
       "statsGroup": statsGroup,
       "atmIpGroup": atmIpGroup,
       "atmarpGroup": atmarpGroup,
       "atmarpFlushTable": atmarpFlushTable,
       "atmarpTable": atmarpTable,
       "atmarpEntry": atmarpEntry,
       "atmarpIpAddress": atmarpIpAddress,
       "atmarpInterface": atmarpInterface,
       "atmarpSpansAddress": atmarpSpansAddress,
       "atmarpNsapAddress": atmarpNsapAddress,
       "atmarpVPI": atmarpVPI,
       "atmarpVCI": atmarpVCI,
       "atmarpConnType": atmarpConnType,
       "atmarpAALType": atmarpAALType,
       "atmarpPeakBandwidth": atmarpPeakBandwidth,
       "atmarpConnDirection": atmarpConnDirection,
       "atmarpEntryValidity": atmarpEntryValidity,
       "atmarpEntryType": atmarpEntryType,
       "atmarpEntryStatus": atmarpEntryStatus,
       "classicalIpGroup": classicalIpGroup,
       "classicalIpArpTable": classicalIpArpTable,
       "classicalIpArpEntry": classicalIpArpEntry,
       "classicalIpArpIfIndex": classicalIpArpIfIndex,
       "classicalIpArpServerIndex": classicalIpArpServerIndex,
       "classicalIpArpServer": classicalIpArpServer,
       "classicalIpArpServerConfigType": classicalIpArpServerConfigType,
       "classicalIpWellKnownArpServerAddr": classicalIpWellKnownArpServerAddr,
       "classicalIpManualConfigArpServerAddr": classicalIpManualConfigArpServerAddr,
       "ipFilterGroup": ipFilterGroup,
       "ipFilterConfGroup": ipFilterConfGroup,
       "ipFilterTable": ipFilterTable,
       "ipFilterEntry": ipFilterEntry,
       "ipFilterIpAddress": ipFilterIpAddress,
       "ipFilterMask": ipFilterMask,
       "ipFilterRowStatus": ipFilterRowStatus,
       "ipFilterNoSSR": ipFilterNoSSR,
       "ipFilterNoLSR": ipFilterNoLSR,
       "ipFilterNoInBand": ipFilterNoInBand,
       "ipFilterStatsGroup": ipFilterStatsGroup,
       "ipFilterStatsIpHeader": ipFilterStatsIpHeader,
       "ipFilterStatsTimeOccured": ipFilterStatsTimeOccured,
       "ipFilterStatsViolations": ipFilterStatsViolations,
       "ipFilterStatsVPI": ipFilterStatsVPI,
       "ipFilterStatsVCI": ipFilterStatsVCI,
       "ipFilterStatsIfName": ipFilterStatsIfName,
       "ipFilterStatsReasonText": ipFilterStatsReasonText,
       "ipFilterStatsSrcIpAddr": ipFilterStatsSrcIpAddr}
)
