# SNMP MIB module (INTEL-LAN-ADAPTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-LAN-ADAPTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:52 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

intellan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3183)
)
intellan.setRevisions(
        ("2012-10-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Nic_products_ObjectIdentity = ObjectIdentity
nic_products = _Nic_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7)
)
_Intel_lan_adapters_ObjectIdentity = ObjectIdentity
intel_lan_adapters = _Intel_lan_adapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2)
)
_Component_description_ObjectIdentity = ObjectIdentity
component_description = _Component_description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1)
)
_Company_Type = DisplayString
_Company_Object = MibScalar
company = _Company_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 1),
    _Company_Type()
)
company.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    company.setStatus("current")
_Description_Type = DisplayString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")
_OperatingSystem_Type = DisplayString
_OperatingSystem_Object = MibScalar
operatingSystem = _OperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 3),
    _OperatingSystem_Type()
)
operatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatingSystem.setStatus("current")
_MibVersion1_4_3_Type = DisplayString
_MibVersion1_4_3_Object = MibScalar
mibVersion1_4_3 = _MibVersion1_4_3_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 4),
    _MibVersion1_4_3_Type()
)
mibVersion1_4_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibVersion1_4_3.setStatus("current")
_MibVersionSupported_Type = DisplayString
_MibVersionSupported_Object = MibScalar
mibVersionSupported = _MibVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 5),
    _MibVersionSupported_Type()
)
mibVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibVersionSupported.setStatus("current")
_AgentExtensionVersion_Type = DisplayString
_AgentExtensionVersion_Object = MibScalar
agentExtensionVersion = _AgentExtensionVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 6),
    _AgentExtensionVersion_Type()
)
agentExtensionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentExtensionVersion.setStatus("current")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("baseDriverLoadedAnsLoaded", 3),
          ("baseDriverLoadedAnsNotLoaded", 1),
          ("baseDriverNotLoadedAnsLoaded", 2),
          ("baseDriverNotLoadedAnsNotLoaded", 0))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 1, 7),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_AdaptersTables_ObjectIdentity = ObjectIdentity
adaptersTables = _AdaptersTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2)
)
_GenericAdaptersAttrTables_ObjectIdentity = ObjectIdentity
genericAdaptersAttrTables = _GenericAdaptersAttrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1)
)
_GenericAdaptersAttrTable_Object = MibTable
genericAdaptersAttrTable = _GenericAdaptersAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    genericAdaptersAttrTable.setStatus("current")
_GenericAdapterAttrEntry_Object = MibTableRow
genericAdapterAttrEntry = _GenericAdapterAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1, 1)
)
genericAdapterAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "adapterIndex"),
)
if mibBuilder.loadTexts:
    genericAdapterAttrEntry.setStatus("current")
_AdapterIndex_Type = InterfaceIndex
_AdapterIndex_Object = MibTableColumn
adapterIndex = _AdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1, 1, 1),
    _AdapterIndex_Type()
)
adapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterIndex.setStatus("current")
_AdapterName_Type = DisplayString
_AdapterName_Object = MibTableColumn
adapterName = _AdapterName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1, 1, 2),
    _AdapterName_Type()
)
adapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterName.setStatus("current")


class _AdapterType_Type(Integer32):
    """Custom type adapterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 0),
          ("teamMember", 1),
          ("virtual", 2))
    )


_AdapterType_Type.__name__ = "Integer32"
_AdapterType_Object = MibTableColumn
adapterType = _AdapterType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1, 1, 3),
    _AdapterType_Type()
)
adapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterType.setStatus("current")


class _AdapterDriverLoadStatus_Type(Integer32):
    """Custom type adapterDriverLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 0),
          ("notLoaded", 1))
    )


_AdapterDriverLoadStatus_Type.__name__ = "Integer32"
_AdapterDriverLoadStatus_Object = MibTableColumn
adapterDriverLoadStatus = _AdapterDriverLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 1, 1, 4),
    _AdapterDriverLoadStatus_Type()
)
adapterDriverLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverLoadStatus.setStatus("current")
_GenericAdaptersDriversAttrTable_Object = MibTable
genericAdaptersDriversAttrTable = _GenericAdaptersDriversAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    genericAdaptersDriversAttrTable.setStatus("current")
_GenericAdapterDriverAttrEntry_Object = MibTableRow
genericAdapterDriverAttrEntry = _GenericAdapterDriverAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1)
)
genericAdapterDriverAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "adapterIndex"),
)
if mibBuilder.loadTexts:
    genericAdapterDriverAttrEntry.setStatus("current")
_AdapterDriverName_Type = DisplayString
_AdapterDriverName_Object = MibTableColumn
adapterDriverName = _AdapterDriverName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 1),
    _AdapterDriverName_Type()
)
adapterDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverName.setStatus("current")
_AdapterDriverInfo_Type = DisplayString
_AdapterDriverInfo_Object = MibTableColumn
adapterDriverInfo = _AdapterDriverInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 2),
    _AdapterDriverInfo_Type()
)
adapterDriverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverInfo.setStatus("current")
_AdapterDriverVersion_Type = DisplayString
_AdapterDriverVersion_Object = MibTableColumn
adapterDriverVersion = _AdapterDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 3),
    _AdapterDriverVersion_Type()
)
adapterDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverVersion.setStatus("current")
_AdapterDriverPath_Type = DisplayString
_AdapterDriverPath_Object = MibTableColumn
adapterDriverPath = _AdapterDriverPath_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 4),
    _AdapterDriverPath_Type()
)
adapterDriverPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverPath.setStatus("current")
_AdapterDriverDate_Type = DisplayString
_AdapterDriverDate_Object = MibTableColumn
adapterDriverDate = _AdapterDriverDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 5),
    _AdapterDriverDate_Type()
)
adapterDriverDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverDate.setStatus("current")
_AdapterDriverSize_Type = DisplayString
_AdapterDriverSize_Object = MibTableColumn
adapterDriverSize = _AdapterDriverSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 6),
    _AdapterDriverSize_Type()
)
adapterDriverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterDriverSize.setStatus("current")
_AdapterIpAddress_Type = DisplayString
_AdapterIpAddress_Object = MibTableColumn
adapterIpAddress = _AdapterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 2, 1, 7),
    _AdapterIpAddress_Type()
)
adapterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterIpAddress.setStatus("current")
_GenericAdaptersTrafficStatsAttrTable_Object = MibTable
genericAdaptersTrafficStatsAttrTable = _GenericAdaptersTrafficStatsAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    genericAdaptersTrafficStatsAttrTable.setStatus("current")
_GenericAdapterTrafficStatsAttrEntry_Object = MibTableRow
genericAdapterTrafficStatsAttrEntry = _GenericAdapterTrafficStatsAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1)
)
genericAdapterTrafficStatsAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "adapterIndex"),
)
if mibBuilder.loadTexts:
    genericAdapterTrafficStatsAttrEntry.setStatus("current")
_AdapterRxPackets_Type = Counter32
_AdapterRxPackets_Object = MibTableColumn
adapterRxPackets = _AdapterRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 1),
    _AdapterRxPackets_Type()
)
adapterRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRxPackets.setStatus("current")
_AdapterTxPackets_Type = Counter32
_AdapterTxPackets_Object = MibTableColumn
adapterTxPackets = _AdapterTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 2),
    _AdapterTxPackets_Type()
)
adapterTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTxPackets.setStatus("current")
_AdapterRxBytes_Type = Counter32
_AdapterRxBytes_Object = MibTableColumn
adapterRxBytes = _AdapterRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 3),
    _AdapterRxBytes_Type()
)
adapterRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRxBytes.setStatus("current")
_AdapterTxBytes_Type = Counter32
_AdapterTxBytes_Object = MibTableColumn
adapterTxBytes = _AdapterTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 4),
    _AdapterTxBytes_Type()
)
adapterTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTxBytes.setStatus("current")
_AdapterRxErrors_Type = Counter32
_AdapterRxErrors_Object = MibTableColumn
adapterRxErrors = _AdapterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 5),
    _AdapterRxErrors_Type()
)
adapterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRxErrors.setStatus("current")
_AdapterTxErrors_Type = Counter32
_AdapterTxErrors_Object = MibTableColumn
adapterTxErrors = _AdapterTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 6),
    _AdapterTxErrors_Type()
)
adapterTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTxErrors.setStatus("current")
_AdapterRxDropped_Type = Counter32
_AdapterRxDropped_Object = MibTableColumn
adapterRxDropped = _AdapterRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 7),
    _AdapterRxDropped_Type()
)
adapterRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRxDropped.setStatus("current")
_AdapterTxDropped_Type = Counter32
_AdapterTxDropped_Object = MibTableColumn
adapterTxDropped = _AdapterTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 8),
    _AdapterTxDropped_Type()
)
adapterTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterTxDropped.setStatus("current")
_AdapterRxMulticast_Type = Counter32
_AdapterRxMulticast_Object = MibTableColumn
adapterRxMulticast = _AdapterRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 9),
    _AdapterRxMulticast_Type()
)
adapterRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRxMulticast.setStatus("current")
_AdapterCollisions_Type = Counter32
_AdapterCollisions_Object = MibTableColumn
adapterCollisions = _AdapterCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 1, 3, 1, 10),
    _AdapterCollisions_Type()
)
adapterCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterCollisions.setStatus("current")
_PhysicalAdaptersAttrTables_ObjectIdentity = ObjectIdentity
physicalAdaptersAttrTables = _PhysicalAdaptersAttrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2)
)
_PhysicalAdaptersAttrTable_Object = MibTable
physicalAdaptersAttrTable = _PhysicalAdaptersAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    physicalAdaptersAttrTable.setStatus("current")
_PhysicalAdapterAttrEntry_Object = MibTableRow
physicalAdapterAttrEntry = _PhysicalAdapterAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1)
)
physicalAdapterAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex"),
)
if mibBuilder.loadTexts:
    physicalAdapterAttrEntry.setStatus("current")
_PhysicalAdapterIndex_Type = InterfaceIndex
_PhysicalAdapterIndex_Object = MibTableColumn
physicalAdapterIndex = _PhysicalAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 1),
    _PhysicalAdapterIndex_Type()
)
physicalAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterIndex.setStatus("current")


class _PhysicalAdapterLinkStatus_Type(Integer32):
    """Custom type physicalAdapterLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("link-up", 0),
          ("not-available", -1))
    )


_PhysicalAdapterLinkStatus_Type.__name__ = "Integer32"
_PhysicalAdapterLinkStatus_Object = MibTableColumn
physicalAdapterLinkStatus = _PhysicalAdapterLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 2),
    _PhysicalAdapterLinkStatus_Type()
)
physicalAdapterLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterLinkStatus.setStatus("current")
_PhysicalAdapterLinkStatusChangesCounter_Type = Counter32
_PhysicalAdapterLinkStatusChangesCounter_Object = MibTableColumn
physicalAdapterLinkStatusChangesCounter = _PhysicalAdapterLinkStatusChangesCounter_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 3),
    _PhysicalAdapterLinkStatusChangesCounter_Type()
)
physicalAdapterLinkStatusChangesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterLinkStatusChangesCounter.setStatus("current")
_PhysicalAdapterSpeed_Type = Gauge32
_PhysicalAdapterSpeed_Object = MibTableColumn
physicalAdapterSpeed = _PhysicalAdapterSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 4),
    _PhysicalAdapterSpeed_Type()
)
physicalAdapterSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterSpeed.setStatus("current")


class _PhysicalAdapterDplxMode_Type(Integer32):
    """Custom type physicalAdapterDplxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("not-available", 0))
    )


_PhysicalAdapterDplxMode_Type.__name__ = "Integer32"
_PhysicalAdapterDplxMode_Object = MibTableColumn
physicalAdapterDplxMode = _PhysicalAdapterDplxMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 5),
    _PhysicalAdapterDplxMode_Type()
)
physicalAdapterDplxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterDplxMode.setStatus("current")


class _PhysicalAdapterAutoNegotiation_Type(Integer32):
    """Custom type physicalAdapterAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_PhysicalAdapterAutoNegotiation_Type.__name__ = "Integer32"
_PhysicalAdapterAutoNegotiation_Object = MibTableColumn
physicalAdapterAutoNegotiation = _PhysicalAdapterAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 6),
    _PhysicalAdapterAutoNegotiation_Type()
)
physicalAdapterAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterAutoNegotiation.setStatus("current")
_PhysicalAdapterPciBus_Type = Integer32
_PhysicalAdapterPciBus_Object = MibTableColumn
physicalAdapterPciBus = _PhysicalAdapterPciBus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 7),
    _PhysicalAdapterPciBus_Type()
)
physicalAdapterPciBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterPciBus.setStatus("current")
_PhysicalAdapterPciSlot_Type = Integer32
_PhysicalAdapterPciSlot_Object = MibTableColumn
physicalAdapterPciSlot = _PhysicalAdapterPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 8),
    _PhysicalAdapterPciSlot_Type()
)
physicalAdapterPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterPciSlot.setStatus("current")
_PhysicalAdapterIrq_Type = Integer32
_PhysicalAdapterIrq_Object = MibTableColumn
physicalAdapterIrq = _PhysicalAdapterIrq_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 9),
    _PhysicalAdapterIrq_Type()
)
physicalAdapterIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterIrq.setStatus("current")
_PhysicalAdapterCurrentNA_Type = PhysAddress
_PhysicalAdapterCurrentNA_Object = MibTableColumn
physicalAdapterCurrentNA = _PhysicalAdapterCurrentNA_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 10),
    _PhysicalAdapterCurrentNA_Type()
)
physicalAdapterCurrentNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterCurrentNA.setStatus("current")
_PhysicalAdapterPermanentNA_Type = PhysAddress
_PhysicalAdapterPermanentNA_Object = MibTableColumn
physicalAdapterPermanentNA = _PhysicalAdapterPermanentNA_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 11),
    _PhysicalAdapterPermanentNA_Type()
)
physicalAdapterPermanentNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterPermanentNA.setStatus("current")


class _PhysicalAdapterOnlineDiagStatus_Type(Integer32):
    """Custom type physicalAdapterOnlineDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("not-available", -1),
          ("passed", 1))
    )


_PhysicalAdapterOnlineDiagStatus_Type.__name__ = "Integer32"
_PhysicalAdapterOnlineDiagStatus_Object = MibTableColumn
physicalAdapterOnlineDiagStatus = _PhysicalAdapterOnlineDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 12),
    _PhysicalAdapterOnlineDiagStatus_Type()
)
physicalAdapterOnlineDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterOnlineDiagStatus.setStatus("current")


class _PhysicalAdapterExpressTeamed_Type(Integer32):
    """Custom type physicalAdapterExpressTeamed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_PhysicalAdapterExpressTeamed_Type.__name__ = "Integer32"
_PhysicalAdapterExpressTeamed_Object = MibTableColumn
physicalAdapterExpressTeamed = _PhysicalAdapterExpressTeamed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 13),
    _PhysicalAdapterExpressTeamed_Type()
)
physicalAdapterExpressTeamed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterExpressTeamed.setStatus("current")
_PhysicalAdapterExpressTeamBundleId_Type = Integer32
_PhysicalAdapterExpressTeamBundleId_Object = MibTableColumn
physicalAdapterExpressTeamBundleId = _PhysicalAdapterExpressTeamBundleId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 1, 1, 14),
    _PhysicalAdapterExpressTeamBundleId_Type()
)
physicalAdapterExpressTeamBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterExpressTeamBundleId.setStatus("current")
_PhysicalAdaptersAttrOffloadTable_Object = MibTable
physicalAdaptersAttrOffloadTable = _PhysicalAdaptersAttrOffloadTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    physicalAdaptersAttrOffloadTable.setStatus("current")
_PhysicalAdapterAttrOffloadEntry_Object = MibTableRow
physicalAdapterAttrOffloadEntry = _PhysicalAdapterAttrOffloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1)
)
physicalAdapterAttrOffloadEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex"),
)
if mibBuilder.loadTexts:
    physicalAdapterAttrOffloadEntry.setStatus("current")


class _PhysicalAdapterTcpRxChecksumOffLoadEnable_Type(Integer32):
    """Custom type physicalAdapterTcpRxChecksumOffLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_PhysicalAdapterTcpRxChecksumOffLoadEnable_Type.__name__ = "Integer32"
_PhysicalAdapterTcpRxChecksumOffLoadEnable_Object = MibTableColumn
physicalAdapterTcpRxChecksumOffLoadEnable = _PhysicalAdapterTcpRxChecksumOffLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 1),
    _PhysicalAdapterTcpRxChecksumOffLoadEnable_Type()
)
physicalAdapterTcpRxChecksumOffLoadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterTcpRxChecksumOffLoadEnable.setStatus("current")
_PhysicalAdapterTcpRxChecksumBad_Type = Counter32
_PhysicalAdapterTcpRxChecksumBad_Object = MibTableColumn
physicalAdapterTcpRxChecksumBad = _PhysicalAdapterTcpRxChecksumBad_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 2),
    _PhysicalAdapterTcpRxChecksumBad_Type()
)
physicalAdapterTcpRxChecksumBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterTcpRxChecksumBad.setStatus("current")


class _PhysicalAdapterTcpTxChecksumOffLoadEnable_Type(Integer32):
    """Custom type physicalAdapterTcpTxChecksumOffLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_PhysicalAdapterTcpTxChecksumOffLoadEnable_Type.__name__ = "Integer32"
_PhysicalAdapterTcpTxChecksumOffLoadEnable_Object = MibTableColumn
physicalAdapterTcpTxChecksumOffLoadEnable = _PhysicalAdapterTcpTxChecksumOffLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 3),
    _PhysicalAdapterTcpTxChecksumOffLoadEnable_Type()
)
physicalAdapterTcpTxChecksumOffLoadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterTcpTxChecksumOffLoadEnable.setStatus("current")


class _PhysicalAdapterIpv4RxChecksumOffLoadEnable_Type(Integer32):
    """Custom type physicalAdapterIpv4RxChecksumOffLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_PhysicalAdapterIpv4RxChecksumOffLoadEnable_Type.__name__ = "Integer32"
_PhysicalAdapterIpv4RxChecksumOffLoadEnable_Object = MibTableColumn
physicalAdapterIpv4RxChecksumOffLoadEnable = _PhysicalAdapterIpv4RxChecksumOffLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 4),
    _PhysicalAdapterIpv4RxChecksumOffLoadEnable_Type()
)
physicalAdapterIpv4RxChecksumOffLoadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterIpv4RxChecksumOffLoadEnable.setStatus("current")


class _PhysicalAdapterIpv4TxChecksumOffLoadEnable_Type(Integer32):
    """Custom type physicalAdapterIpv4TxChecksumOffLoadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_PhysicalAdapterIpv4TxChecksumOffLoadEnable_Type.__name__ = "Integer32"
_PhysicalAdapterIpv4TxChecksumOffLoadEnable_Object = MibTableColumn
physicalAdapterIpv4TxChecksumOffLoadEnable = _PhysicalAdapterIpv4TxChecksumOffLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 5),
    _PhysicalAdapterIpv4TxChecksumOffLoadEnable_Type()
)
physicalAdapterIpv4TxChecksumOffLoadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterIpv4TxChecksumOffLoadEnable.setStatus("current")


class _PhysicalAdapterIpv4TCPSegmentationOffLoadEnable_Type(Integer32):
    """Custom type physicalAdapterIpv4TCPSegmentationOffLoadEnable based on Integer32"""
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


_PhysicalAdapterIpv4TCPSegmentationOffLoadEnable_Type.__name__ = "Integer32"
_PhysicalAdapterIpv4TCPSegmentationOffLoadEnable_Object = MibTableColumn
physicalAdapterIpv4TCPSegmentationOffLoadEnable = _PhysicalAdapterIpv4TCPSegmentationOffLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 2, 2, 1, 6),
    _PhysicalAdapterIpv4TCPSegmentationOffLoadEnable_Type()
)
physicalAdapterIpv4TCPSegmentationOffLoadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalAdapterIpv4TCPSegmentationOffLoadEnable.setStatus("current")
_VirtualAdaptersAttrTables_ObjectIdentity = ObjectIdentity
virtualAdaptersAttrTables = _VirtualAdaptersAttrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3)
)
_VirtualAdaptersAttrTable_Object = MibTable
virtualAdaptersAttrTable = _VirtualAdaptersAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    virtualAdaptersAttrTable.setStatus("current")
_VirtualAdapterAttrEntry_Object = MibTableRow
virtualAdapterAttrEntry = _VirtualAdapterAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 1, 1)
)
virtualAdapterAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "virtualAdapterIndex"),
)
if mibBuilder.loadTexts:
    virtualAdapterAttrEntry.setStatus("current")
_VirtualAdapterIndex_Type = InterfaceIndex
_VirtualAdapterIndex_Object = MibTableColumn
virtualAdapterIndex = _VirtualAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 1, 1, 1),
    _VirtualAdapterIndex_Type()
)
virtualAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAdapterIndex.setStatus("current")
_VirtualAdapterAnsId_Type = Integer32
_VirtualAdapterAnsId_Object = MibTableColumn
virtualAdapterAnsId = _VirtualAdapterAnsId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 1, 1, 2),
    _VirtualAdapterAnsId_Type()
)
virtualAdapterAnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAdapterAnsId.setStatus("current")
_VirtualAdaptersVlanAttrTable_Object = MibTable
virtualAdaptersVlanAttrTable = _VirtualAdaptersVlanAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    virtualAdaptersVlanAttrTable.setStatus("current")
_VirtualAdapterVlanAttrEntry_Object = MibTableRow
virtualAdapterVlanAttrEntry = _VirtualAdapterVlanAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 2, 1)
)
virtualAdapterVlanAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "virtualAdapterIndex"),
)
if mibBuilder.loadTexts:
    virtualAdapterVlanAttrEntry.setStatus("current")


class _VirtualAdapterVlanId_Type(Integer32):
    """Custom type virtualAdapterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_VirtualAdapterVlanId_Type.__name__ = "Integer32"
_VirtualAdapterVlanId_Object = MibTableColumn
virtualAdapterVlanId = _VirtualAdapterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 3, 2, 1, 1),
    _VirtualAdapterVlanId_Type()
)
virtualAdapterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAdapterVlanId.setStatus("current")
_AnsAttrTables_ObjectIdentity = ObjectIdentity
ansAttrTables = _AnsAttrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4)
)
_AnsAttrTable_Object = MibTable
ansAttrTable = _AnsAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ansAttrTable.setStatus("current")
_AnsAttrEntry_Object = MibTableRow
ansAttrEntry = _AnsAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 1, 1)
)
ansAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "ansId"),
)
if mibBuilder.loadTexts:
    ansAttrEntry.setStatus("current")
_AnsId_Type = Integer32
_AnsId_Object = MibTableColumn
ansId = _AnsId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 1, 1, 1),
    _AnsId_Type()
)
ansId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansId.setStatus("current")
_AnsNumberOfMembers_Type = Integer32
_AnsNumberOfMembers_Object = MibTableColumn
ansNumberOfMembers = _AnsNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 1, 1, 2),
    _AnsNumberOfMembers_Type()
)
ansNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansNumberOfMembers.setStatus("current")
_AnsNumberOfVirtualAdapters_Type = Integer32
_AnsNumberOfVirtualAdapters_Object = MibTableColumn
ansNumberOfVirtualAdapters = _AnsNumberOfVirtualAdapters_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 1, 1, 3),
    _AnsNumberOfVirtualAdapters_Type()
)
ansNumberOfVirtualAdapters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansNumberOfVirtualAdapters.setStatus("current")
_AnsVlansAttrTable_Object = MibTable
ansVlansAttrTable = _AnsVlansAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ansVlansAttrTable.setStatus("current")
_AnsVlanAttrEntry_Object = MibTableRow
ansVlanAttrEntry = _AnsVlanAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 2, 1)
)
ansVlanAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "ansId"),
)
if mibBuilder.loadTexts:
    ansVlanAttrEntry.setStatus("current")


class _AnsVlanTaggingType_Type(Integer32):
    """Custom type ansVlanTaggingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag-802-1P", 2),
          ("tag-802-1Q", 1),
          ("tag-802-3AC", 3),
          ("tag-iSL", 4))
    )


_AnsVlanTaggingType_Type.__name__ = "Integer32"
_AnsVlanTaggingType_Object = MibTableColumn
ansVlanTaggingType = _AnsVlanTaggingType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 2, 1, 1),
    _AnsVlanTaggingType_Type()
)
ansVlanTaggingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansVlanTaggingType.setStatus("current")
_AnsTeamsAttrTable_Object = MibTable
ansTeamsAttrTable = _AnsTeamsAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    ansTeamsAttrTable.setStatus("current")
_AnsTeamAttrEntry_Object = MibTableRow
ansTeamAttrEntry = _AnsTeamAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1)
)
ansTeamAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "ansId"),
)
if mibBuilder.loadTexts:
    ansTeamAttrEntry.setStatus("current")
_AnsTeamName_Type = DisplayString
_AnsTeamName_Object = MibTableColumn
ansTeamName = _AnsTeamName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 1),
    _AnsTeamName_Type()
)
ansTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamName.setStatus("current")


class _AnsTeamMode_Type(Integer32):
    """Custom type ansTeamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("adapter-fault-tolerance", 0),
          ("adaptive-load-balancing", 1),
          ("iEEE-802-3ad", 4),
          ("none", 6),
          ("static-link-aggregation", 2),
          ("switch-fault-tolerance", 5))
    )


_AnsTeamMode_Type.__name__ = "Integer32"
_AnsTeamMode_Object = MibTableColumn
ansTeamMode = _AnsTeamMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 2),
    _AnsTeamMode_Type()
)
ansTeamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamMode.setStatus("current")


class _AnsTeamLinkState_Type(Integer32):
    """Custom type ansTeamLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 0))
    )


_AnsTeamLinkState_Type.__name__ = "Integer32"
_AnsTeamLinkState_Object = MibTableColumn
ansTeamLinkState = _AnsTeamLinkState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 3),
    _AnsTeamLinkState_Type()
)
ansTeamLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamLinkState.setStatus("current")
_AnsTeamSpeed_Type = Gauge32
_AnsTeamSpeed_Object = MibTableColumn
ansTeamSpeed = _AnsTeamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 4),
    _AnsTeamSpeed_Type()
)
ansTeamSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamSpeed.setStatus("current")


class _AnsTeamProbesState_Type(Integer32):
    """Custom type ansTeamProbesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("probes-disabled", 1),
          ("probes-enabled", 0))
    )


_AnsTeamProbesState_Type.__name__ = "Integer32"
_AnsTeamProbesState_Object = MibTableColumn
ansTeamProbesState = _AnsTeamProbesState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 5),
    _AnsTeamProbesState_Type()
)
ansTeamProbesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamProbesState.setStatus("current")


class _AnsTeamProbesMode_Type(Integer32):
    """Custom type ansTeamProbesMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 0),
          ("multicast", 1),
          ("not-available", 2))
    )


_AnsTeamProbesMode_Type.__name__ = "Integer32"
_AnsTeamProbesMode_Object = MibTableColumn
ansTeamProbesMode = _AnsTeamProbesMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 6),
    _AnsTeamProbesMode_Type()
)
ansTeamProbesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamProbesMode.setStatus("current")


class _AnsTeamLoadBalanceRefresh_Type(Integer32):
    """Custom type ansTeamLoadBalanceRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("not-available", 0)
    )


_AnsTeamLoadBalanceRefresh_Type.__name__ = "Integer32"
_AnsTeamLoadBalanceRefresh_Object = MibTableColumn
ansTeamLoadBalanceRefresh = _AnsTeamLoadBalanceRefresh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 7),
    _AnsTeamLoadBalanceRefresh_Type()
)
ansTeamLoadBalanceRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamLoadBalanceRefresh.setStatus("current")


class _AnsTeamProbesSendTime_Type(Integer32):
    """Custom type ansTeamProbesSendTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("not-available", 0)
    )


_AnsTeamProbesSendTime_Type.__name__ = "Integer32"
_AnsTeamProbesSendTime_Object = MibTableColumn
ansTeamProbesSendTime = _AnsTeamProbesSendTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 8),
    _AnsTeamProbesSendTime_Type()
)
ansTeamProbesSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamProbesSendTime.setStatus("current")


class _AnsTeamPreferredPrimaryIndex_Type(Integer32):
    """Custom type ansTeamPreferredPrimaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("not-available", -1)
    )


_AnsTeamPreferredPrimaryIndex_Type.__name__ = "Integer32"
_AnsTeamPreferredPrimaryIndex_Object = MibTableColumn
ansTeamPreferredPrimaryIndex = _AnsTeamPreferredPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 9),
    _AnsTeamPreferredPrimaryIndex_Type()
)
ansTeamPreferredPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamPreferredPrimaryIndex.setStatus("current")


class _AnsTeamCurrentPrimaryIndex_Type(Integer32):
    """Custom type ansTeamCurrentPrimaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("not-available", -1)
    )


_AnsTeamCurrentPrimaryIndex_Type.__name__ = "Integer32"
_AnsTeamCurrentPrimaryIndex_Object = MibTableColumn
ansTeamCurrentPrimaryIndex = _AnsTeamCurrentPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 10),
    _AnsTeamCurrentPrimaryIndex_Type()
)
ansTeamCurrentPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamCurrentPrimaryIndex.setStatus("current")


class _AnsTeamPreviousPrimaryIndex_Type(Integer32):
    """Custom type ansTeamPreviousPrimaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("not-available", -1)
    )


_AnsTeamPreviousPrimaryIndex_Type.__name__ = "Integer32"
_AnsTeamPreviousPrimaryIndex_Object = MibTableColumn
ansTeamPreviousPrimaryIndex = _AnsTeamPreviousPrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 11),
    _AnsTeamPreviousPrimaryIndex_Type()
)
ansTeamPreviousPrimaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamPreviousPrimaryIndex.setStatus("current")
_AnsTeamFailoverCounter_Type = Counter32
_AnsTeamFailoverCounter_Object = MibTableColumn
ansTeamFailoverCounter = _AnsTeamFailoverCounter_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 12),
    _AnsTeamFailoverCounter_Type()
)
ansTeamFailoverCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamFailoverCounter.setStatus("current")


class _AnsTeamSlaCompatible_Type(Integer32):
    """Custom type ansTeamSlaCompatible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-available", -1),
          ("yes", 0))
    )


_AnsTeamSlaCompatible_Type.__name__ = "Integer32"
_AnsTeamSlaCompatible_Object = MibTableColumn
ansTeamSlaCompatible = _AnsTeamSlaCompatible_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 13),
    _AnsTeamSlaCompatible_Type()
)
ansTeamSlaCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamSlaCompatible.setStatus("current")


class _AnsTeamAggrSelectionMode_Type(Integer32):
    """Custom type ansTeamAggrSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 0),
          ("count", 1),
          ("not-available", -1))
    )


_AnsTeamAggrSelectionMode_Type.__name__ = "Integer32"
_AnsTeamAggrSelectionMode_Object = MibTableColumn
ansTeamAggrSelectionMode = _AnsTeamAggrSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 14),
    _AnsTeamAggrSelectionMode_Type()
)
ansTeamAggrSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamAggrSelectionMode.setStatus("current")


class _AnsTeamRlbSupport_Type(Integer32):
    """Custom type ansTeamRlbSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("not-available", -1))
    )


_AnsTeamRlbSupport_Type.__name__ = "Integer32"
_AnsTeamRlbSupport_Object = MibTableColumn
ansTeamRlbSupport = _AnsTeamRlbSupport_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 4, 3, 1, 15),
    _AnsTeamRlbSupport_Type()
)
ansTeamRlbSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamRlbSupport.setStatus("current")
_AnsMembersAttrTables_ObjectIdentity = ObjectIdentity
ansMembersAttrTables = _AnsMembersAttrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5)
)
_AnsMembersAttrTable_Object = MibTable
ansMembersAttrTable = _AnsMembersAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ansMembersAttrTable.setStatus("current")
_AnsMemberAttrEntry_Object = MibTableRow
ansMemberAttrEntry = _AnsMemberAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 1, 1)
)
ansMemberAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "ansMemberIndex"),
)
if mibBuilder.loadTexts:
    ansMemberAttrEntry.setStatus("current")
_AnsMemberIndex_Type = InterfaceIndex
_AnsMemberIndex_Object = MibTableColumn
ansMemberIndex = _AnsMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 1, 1, 1),
    _AnsMemberIndex_Type()
)
ansMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansMemberIndex.setStatus("current")
_AnsMemberAnsId_Type = Integer32
_AnsMemberAnsId_Object = MibTableColumn
ansMemberAnsId = _AnsMemberAnsId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 1, 1, 2),
    _AnsMemberAnsId_Type()
)
ansMemberAnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansMemberAnsId.setStatus("current")
_AnsTeamMembersAttrTable_Object = MibTable
ansTeamMembersAttrTable = _AnsTeamMembersAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ansTeamMembersAttrTable.setStatus("current")
_AnsTeamMemberAttrEntry_Object = MibTableRow
ansTeamMemberAttrEntry = _AnsTeamMemberAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 2, 1)
)
ansTeamMemberAttrEntry.setIndexNames(
    (0, "INTEL-LAN-ADAPTERS-MIB", "ansMemberIndex"),
)
if mibBuilder.loadTexts:
    ansTeamMemberAttrEntry.setStatus("current")


class _AnsTeamMemberState_Type(Integer32):
    """Custom type ansTeamMemberState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("active-secondary", 3),
          ("disabled", 1),
          ("standby", 2))
    )


_AnsTeamMemberState_Type.__name__ = "Integer32"
_AnsTeamMemberState_Object = MibTableColumn
ansTeamMemberState = _AnsTeamMemberState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 2, 1, 1),
    _AnsTeamMemberState_Type()
)
ansTeamMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamMemberState.setStatus("current")
_AnsTeamMemberFailureCounter_Type = Counter32
_AnsTeamMemberFailureCounter_Object = MibTableColumn
ansTeamMemberFailureCounter = _AnsTeamMemberFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 2, 1, 2),
    _AnsTeamMemberFailureCounter_Type()
)
ansTeamMemberFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamMemberFailureCounter.setStatus("current")


class _AnsTeamMemberPriority_Type(Integer32):
    """Custom type ansTeamMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_AnsTeamMemberPriority_Type.__name__ = "Integer32"
_AnsTeamMemberPriority_Object = MibTableColumn
ansTeamMemberPriority = _AnsTeamMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 2, 5, 2, 1, 3),
    _AnsTeamMemberPriority_Type()
)
ansTeamMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansTeamMemberPriority.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3)
)
_PhysicalAdaptersEvents_ObjectIdentity = ObjectIdentity
physicalAdaptersEvents = _PhysicalAdaptersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1)
)
_PhysicalAdaptersTraps_ObjectIdentity = ObjectIdentity
physicalAdaptersTraps = _PhysicalAdaptersTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1)
)


class _PhysicalAdapterLinkUpDownTrapEnable_Type(Integer32):
    """Custom type physicalAdapterLinkUpDownTrapEnable based on Integer32"""
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


_PhysicalAdapterLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_PhysicalAdapterLinkUpDownTrapEnable_Object = MibScalar
physicalAdapterLinkUpDownTrapEnable = _PhysicalAdapterLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 2),
    _PhysicalAdapterLinkUpDownTrapEnable_Type()
)
physicalAdapterLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalAdapterLinkUpDownTrapEnable.setStatus("current")


class _PhysicalAdapterAddedRemovedTrapEnable_Type(Integer32):
    """Custom type physicalAdapterAddedRemovedTrapEnable based on Integer32"""
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


_PhysicalAdapterAddedRemovedTrapEnable_Type.__name__ = "Integer32"
_PhysicalAdapterAddedRemovedTrapEnable_Object = MibScalar
physicalAdapterAddedRemovedTrapEnable = _PhysicalAdapterAddedRemovedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 3),
    _PhysicalAdapterAddedRemovedTrapEnable_Type()
)
physicalAdapterAddedRemovedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalAdapterAddedRemovedTrapEnable.setStatus("current")


class _PhysicalAdapterOnlineDiagPassedFailedTrapEnable_Type(Integer32):
    """Custom type physicalAdapterOnlineDiagPassedFailedTrapEnable based on Integer32"""
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


_PhysicalAdapterOnlineDiagPassedFailedTrapEnable_Type.__name__ = "Integer32"
_PhysicalAdapterOnlineDiagPassedFailedTrapEnable_Object = MibScalar
physicalAdapterOnlineDiagPassedFailedTrapEnable = _PhysicalAdapterOnlineDiagPassedFailedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 4),
    _PhysicalAdapterOnlineDiagPassedFailedTrapEnable_Type()
)
physicalAdapterOnlineDiagPassedFailedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalAdapterOnlineDiagPassedFailedTrapEnable.setStatus("current")
_VirtualAdaptersEvents_ObjectIdentity = ObjectIdentity
virtualAdaptersEvents = _VirtualAdaptersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 2)
)
_VirtualAdaptersTraps_ObjectIdentity = ObjectIdentity
virtualAdaptersTraps = _VirtualAdaptersTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 2, 1)
)


class _VirtualAdaptersTrapEnable_Type(Integer32):
    """Custom type virtualAdaptersTrapEnable based on Integer32"""
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


_VirtualAdaptersTrapEnable_Type.__name__ = "Integer32"
_VirtualAdaptersTrapEnable_Object = MibScalar
virtualAdaptersTrapEnable = _VirtualAdaptersTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 2, 2),
    _VirtualAdaptersTrapEnable_Type()
)
virtualAdaptersTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualAdaptersTrapEnable.setStatus("current")
_AnsEvents_ObjectIdentity = ObjectIdentity
ansEvents = _AnsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3)
)
_AnsTraps_ObjectIdentity = ObjectIdentity
ansTraps = _AnsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3, 1)
)


class _AnsTrapEnable_Type(Integer32):
    """Custom type ansTrapEnable based on Integer32"""
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


_AnsTrapEnable_Type.__name__ = "Integer32"
_AnsTrapEnable_Object = MibScalar
ansTrapEnable = _AnsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3, 2),
    _AnsTrapEnable_Type()
)
ansTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansTrapEnable.setStatus("current")
_TeamMembersEvents_ObjectIdentity = ObjectIdentity
teamMembersEvents = _TeamMembersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 4)
)
_TeamMembersTraps_ObjectIdentity = ObjectIdentity
teamMembersTraps = _TeamMembersTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 4, 1)
)


class _TeamMemberTrapEnable_Type(Integer32):
    """Custom type teamMemberTrapEnable based on Integer32"""
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


_TeamMemberTrapEnable_Type.__name__ = "Integer32"
_TeamMemberTrapEnable_Object = MibScalar
teamMemberTrapEnable = _TeamMemberTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 4, 2),
    _TeamMemberTrapEnable_Type()
)
teamMemberTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teamMemberTrapEnable.setStatus("current")
_Intellan_conformance_ObjectIdentity = ObjectIdentity
intellan_conformance = _Intellan_conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1)
)
_PhyAdapterGroups_ObjectIdentity = ObjectIdentity
phyAdapterGroups = _PhyAdapterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1)
)
_PhyAdapterNotificationGroups_ObjectIdentity = ObjectIdentity
phyAdapterNotificationGroups = _PhyAdapterNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 2)
)
_MiscGroups_ObjectIdentity = ObjectIdentity
miscGroups = _MiscGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 3)
)
_VtAdapterGroups_ObjectIdentity = ObjectIdentity
vtAdapterGroups = _VtAdapterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 4)
)
_VtAdapterNotificationGroups_ObjectIdentity = ObjectIdentity
vtAdapterNotificationGroups = _VtAdapterNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 5)
)
_AnsGroups_ObjectIdentity = ObjectIdentity
ansGroups = _AnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 6)
)
_AnsNotificationGroups_ObjectIdentity = ObjectIdentity
ansNotificationGroups = _AnsNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 7)
)
_TeamGroups_ObjectIdentity = ObjectIdentity
teamGroups = _TeamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 8)
)
_TeamNotificationGroups_ObjectIdentity = ObjectIdentity
teamNotificationGroups = _TeamNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 9)
)
_IntellanCompliances_ObjectIdentity = ObjectIdentity
intellanCompliances = _IntellanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 10)
)

# Managed Objects groups

phyAdapterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 1)
)
phyAdapterGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterOnlineDiagPassedFailedTrapEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterAddedRemovedTrapEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterLinkUpDownTrapEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIpv4TCPSegmentationOffLoadEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIpv4TxChecksumOffLoadEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIpv4RxChecksumOffLoadEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterTcpTxChecksumOffLoadEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterTcpRxChecksumBad"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterTcpRxChecksumOffLoadEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterExpressTeamBundleId"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterExpressTeamed"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterOnlineDiagStatus"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterPermanentNA"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterCurrentNA"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIrq"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterPciSlot"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterPciBus"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterAutoNegotiation"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterDplxMode"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterSpeed"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterLinkStatusChangesCounter"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterLinkStatus"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterCollisions"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterRxMulticast"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterTxDropped"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterRxDropped"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterTxErrors"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterRxErrors"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterTxBytes"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterRxBytes"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterTxPackets"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterRxPackets"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterIpAddress"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverSize"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverDate"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverPath"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverVersion"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverInfo"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverName"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterDriverLoadStatus"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterType"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterName"),
        ("INTEL-LAN-ADAPTERS-MIB", "adapterIndex"))
)
if mibBuilder.loadTexts:
    phyAdapterGroup.setStatus("current")

miscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 3, 1)
)
miscGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "status"),
        ("INTEL-LAN-ADAPTERS-MIB", "agentExtensionVersion"),
        ("INTEL-LAN-ADAPTERS-MIB", "mibVersionSupported"),
        ("INTEL-LAN-ADAPTERS-MIB", "mibVersion1_4_3"),
        ("INTEL-LAN-ADAPTERS-MIB", "operatingSystem"),
        ("INTEL-LAN-ADAPTERS-MIB", "description"),
        ("INTEL-LAN-ADAPTERS-MIB", "company"))
)
if mibBuilder.loadTexts:
    miscGroup.setStatus("current")

vtAdapterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 4, 1)
)
vtAdapterGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "virtualAdaptersTrapEnable"),
        ("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterVlanId"),
        ("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterAnsId"),
        ("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterIndex"))
)
if mibBuilder.loadTexts:
    vtAdapterGroup.setStatus("current")

ansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 6, 1)
)
ansGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "ansId"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansNumberOfMembers"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansNumberOfVirtualAdapters"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansVlanTaggingType"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamName"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamMode"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamLinkState"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamSpeed"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamProbesState"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamProbesMode"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamLoadBalanceRefresh"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamProbesSendTime"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamPreferredPrimaryIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamCurrentPrimaryIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamPreviousPrimaryIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamFailoverCounter"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamSlaCompatible"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamAggrSelectionMode"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamRlbSupport"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansMemberIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansMemberAnsId"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamMemberState"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamMemberFailureCounter"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamMemberPriority"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTrapEnable"))
)
if mibBuilder.loadTexts:
    ansGroup.setStatus("current")

teamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 8, 1)
)
teamGroup.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "teamMemberTrapEnable")
)
if mibBuilder.loadTexts:
    teamGroup.setStatus("current")


# Notification objects

physicalAdapterLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 1)
)
physicalAdapterLinkUpTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterLinkUpTrap.setStatus(
        "current"
    )

physicalAdapterLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 2)
)
physicalAdapterLinkDownTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterLinkDownTrap.setStatus(
        "current"
    )

physicalAdapterAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 3)
)
physicalAdapterAddedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterAddedTrap.setStatus(
        "current"
    )

physicalAdapterRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 4)
)
physicalAdapterRemovedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterRemovedTrap.setStatus(
        "current"
    )

physicalAdapterOnlineDiagPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 5)
)
physicalAdapterOnlineDiagPassedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterOnlineDiagPassedTrap.setStatus(
        "current"
    )

physicalAdapterOnlineDiagFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 1, 1, 6)
)
physicalAdapterOnlineDiagFailedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterIndex")
)
if mibBuilder.loadTexts:
    physicalAdapterOnlineDiagFailedTrap.setStatus(
        "current"
    )

virtualAdapterAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 2, 1, 1)
)
virtualAdapterAddedTrap.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansId"))
)
if mibBuilder.loadTexts:
    virtualAdapterAddedTrap.setStatus(
        "current"
    )

virtualAdapterRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 2, 1, 2)
)
virtualAdapterRemovedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterIndex")
)
if mibBuilder.loadTexts:
    virtualAdapterRemovedTrap.setStatus(
        "current"
    )

ansTeamFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3, 1, 1)
)
ansTeamFailoverTrap.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "ansId"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamCurrentPrimaryIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansTeamPreviousPrimaryIndex"))
)
if mibBuilder.loadTexts:
    ansTeamFailoverTrap.setStatus(
        "current"
    )

ansAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3, 1, 2)
)
ansAddedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "ansId")
)
if mibBuilder.loadTexts:
    ansAddedTrap.setStatus(
        "current"
    )

ansRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 3, 1, 3)
)
ansRemovedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "ansId")
)
if mibBuilder.loadTexts:
    ansRemovedTrap.setStatus(
        "current"
    )

teamMemberAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 4, 1, 1)
)
teamMemberAddedTrap.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "ansMemberIndex"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansId"))
)
if mibBuilder.loadTexts:
    teamMemberAddedTrap.setStatus(
        "current"
    )

teamMemberRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 7, 2, 3, 4, 1, 2)
)
teamMemberRemovedTrap.setObjects(
    ("INTEL-LAN-ADAPTERS-MIB", "ansMemberIndex")
)
if mibBuilder.loadTexts:
    teamMemberRemovedTrap.setStatus(
        "current"
    )


# Notifications groups

phyAdapterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 2, 1)
)
phyAdapterNotificationGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterOnlineDiagFailedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterOnlineDiagPassedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterRemovedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterAddedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterLinkDownTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "physicalAdapterLinkUpTrap"))
)
if mibBuilder.loadTexts:
    phyAdapterNotificationGroup.setStatus(
        "current"
    )

vtAdapterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 5, 1)
)
vtAdapterNotificationGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterRemovedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "virtualAdapterAddedTrap"))
)
if mibBuilder.loadTexts:
    vtAdapterNotificationGroup.setStatus(
        "current"
    )

ansNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 7, 1)
)
ansNotificationGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "ansTeamFailoverTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansAddedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "ansRemovedTrap"))
)
if mibBuilder.loadTexts:
    ansNotificationGroup.setStatus(
        "current"
    )

teamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3183, 1, 9, 1)
)
teamNotificationGroup.setObjects(
      *(("INTEL-LAN-ADAPTERS-MIB", "teamMemberAddedTrap"),
        ("INTEL-LAN-ADAPTERS-MIB", "teamMemberRemovedTrap"))
)
if mibBuilder.loadTexts:
    teamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

intellan_compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3183, 1, 10, 1)
)
if mibBuilder.loadTexts:
    intellan_compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-LAN-ADAPTERS-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "intel": intel,
       "products": products,
       "nic-products": nic_products,
       "intel-lan-adapters": intel_lan_adapters,
       "component-description": component_description,
       "company": company,
       "description": description,
       "operatingSystem": operatingSystem,
       "mibVersion1-4-3": mibVersion1_4_3,
       "mibVersionSupported": mibVersionSupported,
       "agentExtensionVersion": agentExtensionVersion,
       "status": status,
       "adaptersTables": adaptersTables,
       "genericAdaptersAttrTables": genericAdaptersAttrTables,
       "genericAdaptersAttrTable": genericAdaptersAttrTable,
       "genericAdapterAttrEntry": genericAdapterAttrEntry,
       "adapterIndex": adapterIndex,
       "adapterName": adapterName,
       "adapterType": adapterType,
       "adapterDriverLoadStatus": adapterDriverLoadStatus,
       "genericAdaptersDriversAttrTable": genericAdaptersDriversAttrTable,
       "genericAdapterDriverAttrEntry": genericAdapterDriverAttrEntry,
       "adapterDriverName": adapterDriverName,
       "adapterDriverInfo": adapterDriverInfo,
       "adapterDriverVersion": adapterDriverVersion,
       "adapterDriverPath": adapterDriverPath,
       "adapterDriverDate": adapterDriverDate,
       "adapterDriverSize": adapterDriverSize,
       "adapterIpAddress": adapterIpAddress,
       "genericAdaptersTrafficStatsAttrTable": genericAdaptersTrafficStatsAttrTable,
       "genericAdapterTrafficStatsAttrEntry": genericAdapterTrafficStatsAttrEntry,
       "adapterRxPackets": adapterRxPackets,
       "adapterTxPackets": adapterTxPackets,
       "adapterRxBytes": adapterRxBytes,
       "adapterTxBytes": adapterTxBytes,
       "adapterRxErrors": adapterRxErrors,
       "adapterTxErrors": adapterTxErrors,
       "adapterRxDropped": adapterRxDropped,
       "adapterTxDropped": adapterTxDropped,
       "adapterRxMulticast": adapterRxMulticast,
       "adapterCollisions": adapterCollisions,
       "physicalAdaptersAttrTables": physicalAdaptersAttrTables,
       "physicalAdaptersAttrTable": physicalAdaptersAttrTable,
       "physicalAdapterAttrEntry": physicalAdapterAttrEntry,
       "physicalAdapterIndex": physicalAdapterIndex,
       "physicalAdapterLinkStatus": physicalAdapterLinkStatus,
       "physicalAdapterLinkStatusChangesCounter": physicalAdapterLinkStatusChangesCounter,
       "physicalAdapterSpeed": physicalAdapterSpeed,
       "physicalAdapterDplxMode": physicalAdapterDplxMode,
       "physicalAdapterAutoNegotiation": physicalAdapterAutoNegotiation,
       "physicalAdapterPciBus": physicalAdapterPciBus,
       "physicalAdapterPciSlot": physicalAdapterPciSlot,
       "physicalAdapterIrq": physicalAdapterIrq,
       "physicalAdapterCurrentNA": physicalAdapterCurrentNA,
       "physicalAdapterPermanentNA": physicalAdapterPermanentNA,
       "physicalAdapterOnlineDiagStatus": physicalAdapterOnlineDiagStatus,
       "physicalAdapterExpressTeamed": physicalAdapterExpressTeamed,
       "physicalAdapterExpressTeamBundleId": physicalAdapterExpressTeamBundleId,
       "physicalAdaptersAttrOffloadTable": physicalAdaptersAttrOffloadTable,
       "physicalAdapterAttrOffloadEntry": physicalAdapterAttrOffloadEntry,
       "physicalAdapterTcpRxChecksumOffLoadEnable": physicalAdapterTcpRxChecksumOffLoadEnable,
       "physicalAdapterTcpRxChecksumBad": physicalAdapterTcpRxChecksumBad,
       "physicalAdapterTcpTxChecksumOffLoadEnable": physicalAdapterTcpTxChecksumOffLoadEnable,
       "physicalAdapterIpv4RxChecksumOffLoadEnable": physicalAdapterIpv4RxChecksumOffLoadEnable,
       "physicalAdapterIpv4TxChecksumOffLoadEnable": physicalAdapterIpv4TxChecksumOffLoadEnable,
       "physicalAdapterIpv4TCPSegmentationOffLoadEnable": physicalAdapterIpv4TCPSegmentationOffLoadEnable,
       "virtualAdaptersAttrTables": virtualAdaptersAttrTables,
       "virtualAdaptersAttrTable": virtualAdaptersAttrTable,
       "virtualAdapterAttrEntry": virtualAdapterAttrEntry,
       "virtualAdapterIndex": virtualAdapterIndex,
       "virtualAdapterAnsId": virtualAdapterAnsId,
       "virtualAdaptersVlanAttrTable": virtualAdaptersVlanAttrTable,
       "virtualAdapterVlanAttrEntry": virtualAdapterVlanAttrEntry,
       "virtualAdapterVlanId": virtualAdapterVlanId,
       "ansAttrTables": ansAttrTables,
       "ansAttrTable": ansAttrTable,
       "ansAttrEntry": ansAttrEntry,
       "ansId": ansId,
       "ansNumberOfMembers": ansNumberOfMembers,
       "ansNumberOfVirtualAdapters": ansNumberOfVirtualAdapters,
       "ansVlansAttrTable": ansVlansAttrTable,
       "ansVlanAttrEntry": ansVlanAttrEntry,
       "ansVlanTaggingType": ansVlanTaggingType,
       "ansTeamsAttrTable": ansTeamsAttrTable,
       "ansTeamAttrEntry": ansTeamAttrEntry,
       "ansTeamName": ansTeamName,
       "ansTeamMode": ansTeamMode,
       "ansTeamLinkState": ansTeamLinkState,
       "ansTeamSpeed": ansTeamSpeed,
       "ansTeamProbesState": ansTeamProbesState,
       "ansTeamProbesMode": ansTeamProbesMode,
       "ansTeamLoadBalanceRefresh": ansTeamLoadBalanceRefresh,
       "ansTeamProbesSendTime": ansTeamProbesSendTime,
       "ansTeamPreferredPrimaryIndex": ansTeamPreferredPrimaryIndex,
       "ansTeamCurrentPrimaryIndex": ansTeamCurrentPrimaryIndex,
       "ansTeamPreviousPrimaryIndex": ansTeamPreviousPrimaryIndex,
       "ansTeamFailoverCounter": ansTeamFailoverCounter,
       "ansTeamSlaCompatible": ansTeamSlaCompatible,
       "ansTeamAggrSelectionMode": ansTeamAggrSelectionMode,
       "ansTeamRlbSupport": ansTeamRlbSupport,
       "ansMembersAttrTables": ansMembersAttrTables,
       "ansMembersAttrTable": ansMembersAttrTable,
       "ansMemberAttrEntry": ansMemberAttrEntry,
       "ansMemberIndex": ansMemberIndex,
       "ansMemberAnsId": ansMemberAnsId,
       "ansTeamMembersAttrTable": ansTeamMembersAttrTable,
       "ansTeamMemberAttrEntry": ansTeamMemberAttrEntry,
       "ansTeamMemberState": ansTeamMemberState,
       "ansTeamMemberFailureCounter": ansTeamMemberFailureCounter,
       "ansTeamMemberPriority": ansTeamMemberPriority,
       "events": events,
       "physicalAdaptersEvents": physicalAdaptersEvents,
       "physicalAdaptersTraps": physicalAdaptersTraps,
       "physicalAdapterLinkUpTrap": physicalAdapterLinkUpTrap,
       "physicalAdapterLinkDownTrap": physicalAdapterLinkDownTrap,
       "physicalAdapterAddedTrap": physicalAdapterAddedTrap,
       "physicalAdapterRemovedTrap": physicalAdapterRemovedTrap,
       "physicalAdapterOnlineDiagPassedTrap": physicalAdapterOnlineDiagPassedTrap,
       "physicalAdapterOnlineDiagFailedTrap": physicalAdapterOnlineDiagFailedTrap,
       "physicalAdapterLinkUpDownTrapEnable": physicalAdapterLinkUpDownTrapEnable,
       "physicalAdapterAddedRemovedTrapEnable": physicalAdapterAddedRemovedTrapEnable,
       "physicalAdapterOnlineDiagPassedFailedTrapEnable": physicalAdapterOnlineDiagPassedFailedTrapEnable,
       "virtualAdaptersEvents": virtualAdaptersEvents,
       "virtualAdaptersTraps": virtualAdaptersTraps,
       "virtualAdapterAddedTrap": virtualAdapterAddedTrap,
       "virtualAdapterRemovedTrap": virtualAdapterRemovedTrap,
       "virtualAdaptersTrapEnable": virtualAdaptersTrapEnable,
       "ansEvents": ansEvents,
       "ansTraps": ansTraps,
       "ansTeamFailoverTrap": ansTeamFailoverTrap,
       "ansAddedTrap": ansAddedTrap,
       "ansRemovedTrap": ansRemovedTrap,
       "ansTrapEnable": ansTrapEnable,
       "teamMembersEvents": teamMembersEvents,
       "teamMembersTraps": teamMembersTraps,
       "teamMemberAddedTrap": teamMemberAddedTrap,
       "teamMemberRemovedTrap": teamMemberRemovedTrap,
       "teamMemberTrapEnable": teamMemberTrapEnable,
       "intellan": intellan,
       "intellan-conformance": intellan_conformance,
       "phyAdapterGroups": phyAdapterGroups,
       "phyAdapterGroup": phyAdapterGroup,
       "phyAdapterNotificationGroups": phyAdapterNotificationGroups,
       "phyAdapterNotificationGroup": phyAdapterNotificationGroup,
       "miscGroups": miscGroups,
       "miscGroup": miscGroup,
       "vtAdapterGroups": vtAdapterGroups,
       "vtAdapterGroup": vtAdapterGroup,
       "vtAdapterNotificationGroups": vtAdapterNotificationGroups,
       "vtAdapterNotificationGroup": vtAdapterNotificationGroup,
       "ansGroups": ansGroups,
       "ansGroup": ansGroup,
       "ansNotificationGroups": ansNotificationGroups,
       "ansNotificationGroup": ansNotificationGroup,
       "teamGroups": teamGroups,
       "teamGroup": teamGroup,
       "teamNotificationGroups": teamNotificationGroups,
       "teamNotificationGroup": teamNotificationGroup,
       "intellanCompliances": intellanCompliances,
       "intellan-compliance": intellan_compliance}
)
