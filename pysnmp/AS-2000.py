# SNMP MIB module (AS-2000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AS-2000
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:47 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_OrinocoProducts_ObjectIdentity = ObjectIdentity
orinocoProducts = _OrinocoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 4)
)
_As2000Product_ObjectIdentity = ObjectIdentity
as2000Product = _As2000Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 4, 4)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_Orinoco_ObjectIdentity = ObjectIdentity
orinoco = _Orinoco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4)
)
_As2000_ObjectIdentity = ObjectIdentity
as2000 = _As2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3)
)
_OrinocoInterface_ObjectIdentity = ObjectIdentity
orinocoInterface = _OrinocoInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3)
)
_OrinocoPHY_ObjectIdentity = ObjectIdentity
orinocoPHY = _OrinocoPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2)
)
_PliSystemName_Type = DisplayString
_PliSystemName_Object = MibScalar
pliSystemName = _PliSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 1),
    _PliSystemName_Type()
)
pliSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliSystemName.setStatus("mandatory")
_PsWlanIfTable_Object = MibTable
psWlanIfTable = _PsWlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    psWlanIfTable.setStatus("mandatory")
_PsWlanIfEntry_Object = MibTableRow
psWlanIfEntry = _PsWlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1)
)
psWlanIfEntry.setIndexNames(
    (0, "AS-2000", "pliWlanIfIndex"),
)
if mibBuilder.loadTexts:
    psWlanIfEntry.setStatus("mandatory")
_PliWlanIfIndex_Type = Integer32
_PliWlanIfIndex_Object = MibTableColumn
pliWlanIfIndex = _PliWlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 1),
    _PliWlanIfIndex_Type()
)
pliWlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfIndex.setStatus("mandatory")
_PliWlanIfNetworkName_Type = DisplayString
_PliWlanIfNetworkName_Object = MibTableColumn
pliWlanIfNetworkName = _PliWlanIfNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 2),
    _PliWlanIfNetworkName_Type()
)
pliWlanIfNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfNetworkName.setStatus("mandatory")
_PliWlanIfMACAddress_Type = PhysAddress
_PliWlanIfMACAddress_Object = MibTableColumn
pliWlanIfMACAddress = _PliWlanIfMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 3),
    _PliWlanIfMACAddress_Type()
)
pliWlanIfMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfMACAddress.setStatus("mandatory")


class _PliWlanIfMediumReservation_Type(Integer32):
    """Custom type pliWlanIfMediumReservation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_PliWlanIfMediumReservation_Type.__name__ = "Integer32"
_PliWlanIfMediumReservation_Object = MibTableColumn
pliWlanIfMediumReservation = _PliWlanIfMediumReservation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 4),
    _PliWlanIfMediumReservation_Type()
)
pliWlanIfMediumReservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfMediumReservation.setStatus("mandatory")
_PliWlanIfTransmitRate_Type = Integer32
_PliWlanIfTransmitRate_Object = MibTableColumn
pliWlanIfTransmitRate = _PliWlanIfTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 5),
    _PliWlanIfTransmitRate_Type()
)
pliWlanIfTransmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfTransmitRate.setStatus("mandatory")


class _PliWlanIfOperatingFrequency_Type(Integer32):
    """Custom type pliWlanIfOperatingFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_PliWlanIfOperatingFrequency_Type.__name__ = "Integer32"
_PliWlanIfOperatingFrequency_Object = MibTableColumn
pliWlanIfOperatingFrequency = _PliWlanIfOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 6),
    _PliWlanIfOperatingFrequency_Type()
)
pliWlanIfOperatingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfOperatingFrequency.setStatus("mandatory")
_PliWlanIfAPDensity_Type = Integer32
_PliWlanIfAPDensity_Object = MibTableColumn
pliWlanIfAPDensity = _PliWlanIfAPDensity_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 7),
    _PliWlanIfAPDensity_Type()
)
pliWlanIfAPDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfAPDensity.setStatus("mandatory")
_PliWlanIfClosedSystem_Type = Integer32
_PliWlanIfClosedSystem_Object = MibTableColumn
pliWlanIfClosedSystem = _PliWlanIfClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 8),
    _PliWlanIfClosedSystem_Type()
)
pliWlanIfClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliWlanIfClosedSystem.setStatus("mandatory")
_PliWlanIfAllowedTransmitRates_Type = Integer32
_PliWlanIfAllowedTransmitRates_Object = MibTableColumn
pliWlanIfAllowedTransmitRates = _PliWlanIfAllowedTransmitRates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 9),
    _PliWlanIfAllowedTransmitRates_Type()
)
pliWlanIfAllowedTransmitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfAllowedTransmitRates.setStatus("mandatory")
_PliWlanIfRegulatoryDomainList_Type = OctetString
_PliWlanIfRegulatoryDomainList_Object = MibTableColumn
pliWlanIfRegulatoryDomainList = _PliWlanIfRegulatoryDomainList_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 10),
    _PliWlanIfRegulatoryDomainList_Type()
)
pliWlanIfRegulatoryDomainList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfRegulatoryDomainList.setStatus("mandatory")
_PliWlanIfAllowedOperatingFrequencies_Type = Integer32
_PliWlanIfAllowedOperatingFrequencies_Object = MibTableColumn
pliWlanIfAllowedOperatingFrequencies = _PliWlanIfAllowedOperatingFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 11),
    _PliWlanIfAllowedOperatingFrequencies_Type()
)
pliWlanIfAllowedOperatingFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfAllowedOperatingFrequencies.setStatus("mandatory")
_PliWlanIfCapabilityOptions_Type = Integer32
_PliWlanIfCapabilityOptions_Object = MibTableColumn
pliWlanIfCapabilityOptions = _PliWlanIfCapabilityOptions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 12),
    _PliWlanIfCapabilityOptions_Type()
)
pliWlanIfCapabilityOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfCapabilityOptions.setStatus("mandatory")
_PliWlanIfProfileCode_Type = Integer32
_PliWlanIfProfileCode_Object = MibTableColumn
pliWlanIfProfileCode = _PliWlanIfProfileCode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 2, 2, 1, 13),
    _PliWlanIfProfileCode_Type()
)
pliWlanIfProfileCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliWlanIfProfileCode.setStatus("mandatory")
_OrinocoDriver_ObjectIdentity = ObjectIdentity
orinocoDriver = _OrinocoDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 4)
)
_PliDriverName_Type = DisplayString
_PliDriverName_Object = MibScalar
pliDriverName = _PliDriverName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 4, 1),
    _PliDriverName_Type()
)
pliDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliDriverName.setStatus("mandatory")
_PliDriverVersion_Type = DisplayString
_PliDriverVersion_Object = MibScalar
pliDriverVersion = _PliDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 3, 4, 2),
    _PliDriverVersion_Type()
)
pliDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliDriverVersion.setStatus("mandatory")
_OrinocoSNMPSetup_ObjectIdentity = ObjectIdentity
orinocoSNMPSetup = _OrinocoSNMPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4)
)
_PsSNMPReadPassword_Type = DisplayString
_PsSNMPReadPassword_Object = MibScalar
psSNMPReadPassword = _PsSNMPReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 1),
    _PsSNMPReadPassword_Type()
)
psSNMPReadPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psSNMPReadPassword.setStatus("mandatory")
_PsSNMPReadWritePassword_Type = DisplayString
_PsSNMPReadWritePassword_Object = MibScalar
psSNMPReadWritePassword = _PsSNMPReadWritePassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 2),
    _PsSNMPReadWritePassword_Type()
)
psSNMPReadWritePassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psSNMPReadWritePassword.setStatus("mandatory")
_PsSNMPTrapHostIPAddress_Type = IpAddress
_PsSNMPTrapHostIPAddress_Object = MibScalar
psSNMPTrapHostIPAddress = _PsSNMPTrapHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 3),
    _PsSNMPTrapHostIPAddress_Type()
)
psSNMPTrapHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSNMPTrapHostIPAddress.setStatus("mandatory")
_PsSNMPTrapHostPassword_Type = DisplayString
_PsSNMPTrapHostPassword_Object = MibScalar
psSNMPTrapHostPassword = _PsSNMPTrapHostPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 4),
    _PsSNMPTrapHostPassword_Type()
)
psSNMPTrapHostPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSNMPTrapHostPassword.setStatus("mandatory")
_PsSNMPManagerCount_Type = Integer32
_PsSNMPManagerCount_Object = MibScalar
psSNMPManagerCount = _PsSNMPManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 5),
    _PsSNMPManagerCount_Type()
)
psSNMPManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSNMPManagerCount.setStatus("mandatory")
_PsSNMPAccessTable_Object = MibTable
psSNMPAccessTable = _PsSNMPAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6)
)
if mibBuilder.loadTexts:
    psSNMPAccessTable.setStatus("mandatory")
_PsSNMPAccessTableEntry_Object = MibTableRow
psSNMPAccessTableEntry = _PsSNMPAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6, 1)
)
psSNMPAccessTableEntry.setIndexNames(
    (0, "AS-2000", "psSNMPManagerIndex"),
)
if mibBuilder.loadTexts:
    psSNMPAccessTableEntry.setStatus("mandatory")
_ManagerIndex_Type = Integer32
_ManagerIndex_Object = MibTableColumn
managerIndex = _ManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6, 1, 1),
    _ManagerIndex_Type()
)
managerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerIndex.setStatus("mandatory")
_ManagerIPAddress_Type = IpAddress
_ManagerIPAddress_Object = MibTableColumn
managerIPAddress = _ManagerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6, 1, 2),
    _ManagerIPAddress_Type()
)
managerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPAddress.setStatus("mandatory")
_ManagerSubnetMask_Type = IpAddress
_ManagerSubnetMask_Object = MibTableColumn
managerSubnetMask = _ManagerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6, 1, 3),
    _ManagerSubnetMask_Type()
)
managerSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerSubnetMask.setStatus("mandatory")


class _ManagerStatus_Type(Integer32):
    """Custom type managerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("enable", 1))
    )


_ManagerStatus_Type.__name__ = "Integer32"
_ManagerStatus_Object = MibTableColumn
managerStatus = _ManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 6, 1, 4),
    _ManagerStatus_Type()
)
managerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerStatus.setStatus("mandatory")
_PsSNMPInBadManagers_Type = Counter32
_PsSNMPInBadManagers_Object = MibScalar
psSNMPInBadManagers = _PsSNMPInBadManagers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 7),
    _PsSNMPInBadManagers_Type()
)
psSNMPInBadManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSNMPInBadManagers.setStatus("mandatory")
_PsTestSNMPReadWritePassword_Type = DisplayString
_PsTestSNMPReadWritePassword_Object = MibScalar
psTestSNMPReadWritePassword = _PsTestSNMPReadWritePassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 4, 8),
    _PsTestSNMPReadWritePassword_Type()
)
psTestSNMPReadWritePassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psTestSNMPReadWritePassword.setStatus("mandatory")
_OrinocoPPPSetup_ObjectIdentity = ObjectIdentity
orinocoPPPSetup = _OrinocoPPPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5)
)
_PsPPPIPAddressAssignmentType_Type = Integer32
_PsPPPIPAddressAssignmentType_Object = MibScalar
psPPPIPAddressAssignmentType = _PsPPPIPAddressAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 1),
    _PsPPPIPAddressAssignmentType_Type()
)
psPPPIPAddressAssignmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPIPAddressAssignmentType.setStatus("mandatory")
_PsPPPNoOfMACIPMappingEntries_Type = Integer32
_PsPPPNoOfMACIPMappingEntries_Object = MibScalar
psPPPNoOfMACIPMappingEntries = _PsPPPNoOfMACIPMappingEntries_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 2),
    _PsPPPNoOfMACIPMappingEntries_Type()
)
psPPPNoOfMACIPMappingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPPPNoOfMACIPMappingEntries.setStatus("mandatory")
_PsPPPMACIPMappingTable_Object = MibTable
psPPPMACIPMappingTable = _PsPPPMACIPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3)
)
if mibBuilder.loadTexts:
    psPPPMACIPMappingTable.setStatus("mandatory")
_PsPPPMACIPMappingTableEntry_Object = MibTableRow
psPPPMACIPMappingTableEntry = _PsPPPMACIPMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1)
)
psPPPMACIPMappingTableEntry.setIndexNames(
    (0, "AS-2000", "psPPPMACIPTableIndex"),
)
if mibBuilder.loadTexts:
    psPPPMACIPMappingTableEntry.setStatus("mandatory")
_MACIPIndex_Type = Integer32
_MACIPIndex_Object = MibTableColumn
mACIPIndex = _MACIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1, 1),
    _MACIPIndex_Type()
)
mACIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mACIPIndex.setStatus("mandatory")
_MACAddress_Type = PhysAddress
_MACAddress_Object = MibTableColumn
mACAddress = _MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1, 2),
    _MACAddress_Type()
)
mACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mACAddress.setStatus("mandatory")
_IPAddress_Type = IpAddress
_IPAddress_Object = MibTableColumn
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1, 3),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPAddress.setStatus("mandatory")
_Comment_Type = DisplayString
_Comment_Object = MibTableColumn
comment = _Comment_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1, 4),
    _Comment_Type()
)
comment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comment.setStatus("mandatory")


class _EntryStatus_Type(Integer32):
    """Custom type entryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("enable", 1))
    )


_EntryStatus_Type.__name__ = "Integer32"
_EntryStatus_Object = MibTableColumn
entryStatus = _EntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 3, 1, 5),
    _EntryStatus_Type()
)
entryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entryStatus.setStatus("mandatory")
_PsPPPKeepAliveInterval_Type = Integer32
_PsPPPKeepAliveInterval_Object = MibScalar
psPPPKeepAliveInterval = _PsPPPKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 4),
    _PsPPPKeepAliveInterval_Type()
)
psPPPKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPKeepAliveInterval.setStatus("mandatory")
_PsPPPNoOfKeepAliveTimeouts_Type = Integer32
_PsPPPNoOfKeepAliveTimeouts_Object = MibScalar
psPPPNoOfKeepAliveTimeouts = _PsPPPNoOfKeepAliveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 5),
    _PsPPPNoOfKeepAliveTimeouts_Type()
)
psPPPNoOfKeepAliveTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPNoOfKeepAliveTimeouts.setStatus("mandatory")
_PsPPPPrimaryDNSIPAddress_Type = IpAddress
_PsPPPPrimaryDNSIPAddress_Object = MibScalar
psPPPPrimaryDNSIPAddress = _PsPPPPrimaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 6),
    _PsPPPPrimaryDNSIPAddress_Type()
)
psPPPPrimaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPPrimaryDNSIPAddress.setStatus("mandatory")
_PsPPPSecondaryDNSIPAddress_Type = IpAddress
_PsPPPSecondaryDNSIPAddress_Object = MibScalar
psPPPSecondaryDNSIPAddress = _PsPPPSecondaryDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 7),
    _PsPPPSecondaryDNSIPAddress_Type()
)
psPPPSecondaryDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPSecondaryDNSIPAddress.setStatus("mandatory")
_PsPPPMaxNoOfUsers_Type = Integer32
_PsPPPMaxNoOfUsers_Object = MibScalar
psPPPMaxNoOfUsers = _PsPPPMaxNoOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 8),
    _PsPPPMaxNoOfUsers_Type()
)
psPPPMaxNoOfUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPMaxNoOfUsers.setStatus("mandatory")
_PsPPPCHAPStatus_Type = Integer32
_PsPPPCHAPStatus_Object = MibScalar
psPPPCHAPStatus = _PsPPPCHAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 9),
    _PsPPPCHAPStatus_Type()
)
psPPPCHAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPCHAPStatus.setStatus("mandatory")
_PsPPPCHAPPriority_Type = Integer32
_PsPPPCHAPPriority_Object = MibScalar
psPPPCHAPPriority = _PsPPPCHAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 10),
    _PsPPPCHAPPriority_Type()
)
psPPPCHAPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPCHAPPriority.setStatus("mandatory")
_PsPPPPAPStatus_Type = Integer32
_PsPPPPAPStatus_Object = MibScalar
psPPPPAPStatus = _PsPPPPAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 11),
    _PsPPPPAPStatus_Type()
)
psPPPPAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPPAPStatus.setStatus("mandatory")
_PsPPPPAPPriority_Type = Integer32
_PsPPPPAPPriority_Object = MibScalar
psPPPPAPPriority = _PsPPPPAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 12),
    _PsPPPPAPPriority_Type()
)
psPPPPAPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPPAPPriority.setStatus("mandatory")
_PsPPPPrimaryNBNSIPAddress_Type = IpAddress
_PsPPPPrimaryNBNSIPAddress_Object = MibScalar
psPPPPrimaryNBNSIPAddress = _PsPPPPrimaryNBNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 13),
    _PsPPPPrimaryNBNSIPAddress_Type()
)
psPPPPrimaryNBNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPPrimaryNBNSIPAddress.setStatus("mandatory")
_PsPPPSecondaryNBNSIPAddress_Type = IpAddress
_PsPPPSecondaryNBNSIPAddress_Object = MibScalar
psPPPSecondaryNBNSIPAddress = _PsPPPSecondaryNBNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 14),
    _PsPPPSecondaryNBNSIPAddress_Type()
)
psPPPSecondaryNBNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPSecondaryNBNSIPAddress.setStatus("mandatory")
_PsPPPIPRangeTable_Object = MibTable
psPPPIPRangeTable = _PsPPPIPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15)
)
if mibBuilder.loadTexts:
    psPPPIPRangeTable.setStatus("mandatory")
_PsPPPIPRangeTableEntry_Object = MibTableRow
psPPPIPRangeTableEntry = _PsPPPIPRangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1)
)
psPPPIPRangeTableEntry.setIndexNames(
    (0, "AS-2000", "psPPPIPRangeTableIndex"),
)
if mibBuilder.loadTexts:
    psPPPIPRangeTableEntry.setStatus("mandatory")
_PPPIPIndex_Type = Integer32
_PPPIPIndex_Object = MibTableColumn
pPPIPIndex = _PPPIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 1),
    _PPPIPIndex_Type()
)
pPPIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPPIPIndex.setStatus("mandatory")
_StartIPAddress_Type = IpAddress
_StartIPAddress_Object = MibTableColumn
startIPAddress = _StartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 2),
    _StartIPAddress_Type()
)
startIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startIPAddress.setStatus("mandatory")
_EndIPAddress_Type = IpAddress
_EndIPAddress_Object = MibTableColumn
endIPAddress = _EndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 3),
    _EndIPAddress_Type()
)
endIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endIPAddress.setStatus("mandatory")
_Width_Type = Integer32
_Width_Object = MibTableColumn
width = _Width_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 4),
    _Width_Type()
)
width.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    width.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("enable", 1))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 5),
    _Status_Type()
)
status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_IPComment_Type = DisplayString
_IPComment_Object = MibTableColumn
iPComment = _IPComment_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 15, 1, 6),
    _IPComment_Type()
)
iPComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPComment.setStatus("mandatory")


class _PsPPPSessionIdleTimeOut_Type(Integer32):
    """Custom type psPPPSessionIdleTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_PsPPPSessionIdleTimeOut_Type.__name__ = "Integer32"
_PsPPPSessionIdleTimeOut_Object = MibScalar
psPPPSessionIdleTimeOut = _PsPPPSessionIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 5, 16),
    _PsPPPSessionIdleTimeOut_Type()
)
psPPPSessionIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPSessionIdleTimeOut.setStatus("mandatory")
_OrinocoAgent_ObjectIdentity = ObjectIdentity
orinocoAgent = _OrinocoAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6)
)
_PsVersion_Type = DisplayString
_PsVersion_Object = MibScalar
psVersion = _PsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 1),
    _PsVersion_Type()
)
psVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVersion.setStatus("mandatory")
_PsIPAddress_Type = IpAddress
_PsIPAddress_Object = MibScalar
psIPAddress = _PsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 2),
    _PsIPAddress_Type()
)
psIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIPAddress.setStatus("mandatory")
_PsSubnetMask_Type = IpAddress
_PsSubnetMask_Object = MibScalar
psSubnetMask = _PsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 3),
    _PsSubnetMask_Type()
)
psSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSubnetMask.setStatus("mandatory")
_PsDefaultGateway_Type = IpAddress
_PsDefaultGateway_Object = MibScalar
psDefaultGateway = _PsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 4),
    _PsDefaultGateway_Type()
)
psDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psDefaultGateway.setStatus("mandatory")
_PsIPAddressType_Type = Integer32
_PsIPAddressType_Object = MibScalar
psIPAddressType = _PsIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 5),
    _PsIPAddressType_Type()
)
psIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIPAddressType.setStatus("mandatory")
_PsAdministrativeState_Type = Integer32
_PsAdministrativeState_Object = MibScalar
psAdministrativeState = _PsAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 6),
    _PsAdministrativeState_Type()
)
psAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psAdministrativeState.setStatus("mandatory")
_PsTFTPIPAddress_Type = IpAddress
_PsTFTPIPAddress_Object = MibScalar
psTFTPIPAddress = _PsTFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 7),
    _PsTFTPIPAddress_Type()
)
psTFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTFTPIPAddress.setStatus("mandatory")
_PsTFTPFilename_Type = DisplayString
_PsTFTPFilename_Object = MibScalar
psTFTPFilename = _PsTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 8),
    _PsTFTPFilename_Type()
)
psTFTPFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTFTPFilename.setStatus("mandatory")
_PsTFTPOperation_Type = Integer32
_PsTFTPOperation_Object = MibScalar
psTFTPOperation = _PsTFTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 9),
    _PsTFTPOperation_Type()
)
psTFTPOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psTFTPOperation.setStatus("mandatory")
_PsReboot_Type = Integer32
_PsReboot_Object = MibScalar
psReboot = _PsReboot_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 10),
    _PsReboot_Type()
)
psReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psReboot.setStatus("mandatory")
_PsSecondsToAdminDown_Type = Integer32
_PsSecondsToAdminDown_Object = MibScalar
psSecondsToAdminDown = _PsSecondsToAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 11),
    _PsSecondsToAdminDown_Type()
)
psSecondsToAdminDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSecondsToAdminDown.setStatus("mandatory")


class _PsContactEmail_Type(DisplayString):
    """Custom type psContactEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsContactEmail_Type.__name__ = "DisplayString"
_PsContactEmail_Object = MibScalar
psContactEmail = _PsContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 12),
    _PsContactEmail_Type()
)
psContactEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psContactEmail.setStatus("mandatory")
_PsBSPBootloaderVersion_Type = DisplayString
_PsBSPBootloaderVersion_Object = MibScalar
psBSPBootloaderVersion = _PsBSPBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 13),
    _PsBSPBootloaderVersion_Type()
)
psBSPBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBSPBootloaderVersion.setStatus("mandatory")


class _PsTelnetSesssions_Type(Integer32):
    """Custom type psTelnetSesssions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_PsTelnetSesssions_Type.__name__ = "Integer32"
_PsTelnetSesssions_Object = MibScalar
psTelnetSesssions = _PsTelnetSesssions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 14),
    _PsTelnetSesssions_Type()
)
psTelnetSesssions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTelnetSesssions.setStatus("mandatory")
_PsTelnetPassword_Type = DisplayString
_PsTelnetPassword_Object = MibScalar
psTelnetPassword = _PsTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 15),
    _PsTelnetPassword_Type()
)
psTelnetPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psTelnetPassword.setStatus("mandatory")
_PsTelnetPort_Type = Integer32
_PsTelnetPort_Object = MibScalar
psTelnetPort = _PsTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 16),
    _PsTelnetPort_Type()
)
psTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTelnetPort.setStatus("mandatory")


class _PsTelnetTimeout_Type(Integer32):
    """Custom type psTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PsTelnetTimeout_Type.__name__ = "Integer32"
_PsTelnetTimeout_Object = MibScalar
psTelnetTimeout = _PsTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 17),
    _PsTelnetTimeout_Type()
)
psTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTelnetTimeout.setStatus("mandatory")


class _PsTelnetLoginTimeout_Type(Integer32):
    """Custom type psTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PsTelnetLoginTimeout_Type.__name__ = "Integer32"
_PsTelnetLoginTimeout_Object = MibScalar
psTelnetLoginTimeout = _PsTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 18),
    _PsTelnetLoginTimeout_Type()
)
psTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTelnetLoginTimeout.setStatus("mandatory")
_PsSerialBaudRate_Type = Integer32
_PsSerialBaudRate_Object = MibScalar
psSerialBaudRate = _PsSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 19),
    _PsSerialBaudRate_Type()
)
psSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSerialBaudRate.setStatus("mandatory")


class _PsSerialDataBits_Type(Integer32):
    """Custom type psSerialDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_PsSerialDataBits_Type.__name__ = "Integer32"
_PsSerialDataBits_Object = MibScalar
psSerialDataBits = _PsSerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 20),
    _PsSerialDataBits_Type()
)
psSerialDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSerialDataBits.setStatus("mandatory")
_PsSerialParity_Type = Integer32
_PsSerialParity_Object = MibScalar
psSerialParity = _PsSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 21),
    _PsSerialParity_Type()
)
psSerialParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSerialParity.setStatus("mandatory")
_PsSerialStopBits_Type = Integer32
_PsSerialStopBits_Object = MibScalar
psSerialStopBits = _PsSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 22),
    _PsSerialStopBits_Type()
)
psSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSerialStopBits.setStatus("mandatory")
_PsSerialFlowControl_Type = Integer32
_PsSerialFlowControl_Object = MibScalar
psSerialFlowControl = _PsSerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 23),
    _PsSerialFlowControl_Type()
)
psSerialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSerialFlowControl.setStatus("mandatory")
_PsTFTPFileType_Type = Integer32
_PsTFTPFileType_Object = MibScalar
psTFTPFileType = _PsTFTPFileType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 24),
    _PsTFTPFileType_Type()
)
psTFTPFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTFTPFileType.setStatus("mandatory")
_PsDeviceSerialNumber_Type = DisplayString
_PsDeviceSerialNumber_Object = MibScalar
psDeviceSerialNumber = _PsDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 25),
    _PsDeviceSerialNumber_Type()
)
psDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceSerialNumber.setStatus("mandatory")
_PsBroadcastMessage_Type = DisplayString
_PsBroadcastMessage_Object = MibScalar
psBroadcastMessage = _PsBroadcastMessage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 26),
    _PsBroadcastMessage_Type()
)
psBroadcastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBroadcastMessage.setStatus("mandatory")
_PsPOSTVersionNumber_Type = DisplayString
_PsPOSTVersionNumber_Object = MibScalar
psPOSTVersionNumber = _PsPOSTVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 27),
    _PsPOSTVersionNumber_Type()
)
psPOSTVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPOSTVersionNumber.setStatus("mandatory")
_PsHardwareVersionNumber_Type = DisplayString
_PsHardwareVersionNumber_Object = MibScalar
psHardwareVersionNumber = _PsHardwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 6, 28),
    _PsHardwareVersionNumber_Type()
)
psHardwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psHardwareVersionNumber.setStatus("mandatory")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7)
)
_RadiusClientMIB_ObjectIdentity = ObjectIdentity
radiusClientMIB = _RadiusClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2)
)
_RadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusClientMIBObjects = _RadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1)
)
_RadiusClient_ObjectIdentity = ObjectIdentity
radiusClient = _RadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1)
)
_RadiusClientInvalidServerAddresses_Type = Counter32
_RadiusClientInvalidServerAddresses_Object = MibScalar
radiusClientInvalidServerAddresses = _RadiusClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 1),
    _RadiusClientInvalidServerAddresses_Type()
)
radiusClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientInvalidServerAddresses.setStatus("mandatory")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("mandatory")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "AS-2000", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("mandatory")
_RadiusServerIndex_Type = Integer32
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("mandatory")
_RadiusServerType_Type = Integer32
_RadiusServerType_Object = MibTableColumn
radiusServerType = _RadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 2),
    _RadiusServerType_Type()
)
radiusServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerType.setStatus("mandatory")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 3),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("mandatory")
_RadiusServerDestPortAuth_Type = Integer32
_RadiusServerDestPortAuth_Object = MibTableColumn
radiusServerDestPortAuth = _RadiusServerDestPortAuth_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 4),
    _RadiusServerDestPortAuth_Type()
)
radiusServerDestPortAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerDestPortAuth.setStatus("mandatory")
_RadiusServerDestPortAcct_Type = Integer32
_RadiusServerDestPortAcct_Object = MibTableColumn
radiusServerDestPortAcct = _RadiusServerDestPortAcct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 5),
    _RadiusServerDestPortAcct_Type()
)
radiusServerDestPortAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerDestPortAcct.setStatus("mandatory")
_RadiusClientAccessRequests_Type = Counter32
_RadiusClientAccessRequests_Object = MibTableColumn
radiusClientAccessRequests = _RadiusClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 6),
    _RadiusClientAccessRequests_Type()
)
radiusClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccessRequests.setStatus("mandatory")
_RadiusClientAccessRetransmissions_Type = Counter32
_RadiusClientAccessRetransmissions_Object = MibTableColumn
radiusClientAccessRetransmissions = _RadiusClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 7),
    _RadiusClientAccessRetransmissions_Type()
)
radiusClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccessRetransmissions.setStatus("mandatory")
_RadiusClientAccessAccepts_Type = Counter32
_RadiusClientAccessAccepts_Object = MibTableColumn
radiusClientAccessAccepts = _RadiusClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 8),
    _RadiusClientAccessAccepts_Type()
)
radiusClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccessAccepts.setStatus("mandatory")
_RadiusClientAccessChallenges_Type = Counter32
_RadiusClientAccessChallenges_Object = MibTableColumn
radiusClientAccessChallenges = _RadiusClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 9),
    _RadiusClientAccessChallenges_Type()
)
radiusClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccessChallenges.setStatus("mandatory")
_RadiusClientMalformedAccessResponses_Type = Counter32
_RadiusClientMalformedAccessResponses_Object = MibTableColumn
radiusClientMalformedAccessResponses = _RadiusClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 10),
    _RadiusClientMalformedAccessResponses_Type()
)
radiusClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientMalformedAccessResponses.setStatus("mandatory")
_RadiusClientAuthenticationBadAuthenticators_Type = Counter32
_RadiusClientAuthenticationBadAuthenticators_Object = MibTableColumn
radiusClientAuthenticationBadAuthenticators = _RadiusClientAuthenticationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 11),
    _RadiusClientAuthenticationBadAuthenticators_Type()
)
radiusClientAuthenticationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAuthenticationBadAuthenticators.setStatus("mandatory")
_RadiusClientAccessRejects_Type = Counter32
_RadiusClientAccessRejects_Object = MibTableColumn
radiusClientAccessRejects = _RadiusClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 12),
    _RadiusClientAccessRejects_Type()
)
radiusClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccessRejects.setStatus("mandatory")
_RadiusClientTimeouts_Type = Counter32
_RadiusClientTimeouts_Object = MibTableColumn
radiusClientTimeouts = _RadiusClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 13),
    _RadiusClientTimeouts_Type()
)
radiusClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientTimeouts.setStatus("mandatory")
_RadiusClientAccountingRequests_Type = Counter32
_RadiusClientAccountingRequests_Object = MibTableColumn
radiusClientAccountingRequests = _RadiusClientAccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 14),
    _RadiusClientAccountingRequests_Type()
)
radiusClientAccountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccountingRequests.setStatus("mandatory")
_RadiusClientAccountingRetransmissions_Type = Counter32
_RadiusClientAccountingRetransmissions_Object = MibTableColumn
radiusClientAccountingRetransmissions = _RadiusClientAccountingRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 15),
    _RadiusClientAccountingRetransmissions_Type()
)
radiusClientAccountingRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccountingRetransmissions.setStatus("mandatory")
_RadiusClientAccountingResponses_Type = Counter32
_RadiusClientAccountingResponses_Object = MibTableColumn
radiusClientAccountingResponses = _RadiusClientAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 16),
    _RadiusClientAccountingResponses_Type()
)
radiusClientAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccountingResponses.setStatus("mandatory")
_RadiusClientAccountingBadAuthenticators_Type = Counter32
_RadiusClientAccountingBadAuthenticators_Object = MibTableColumn
radiusClientAccountingBadAuthenticators = _RadiusClientAccountingBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 17),
    _RadiusClientAccountingBadAuthenticators_Type()
)
radiusClientAccountingBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientAccountingBadAuthenticators.setStatus("mandatory")
_RadiusServerSharedSecret_Type = DisplayString
_RadiusServerSharedSecret_Object = MibTableColumn
radiusServerSharedSecret = _RadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 18),
    _RadiusServerSharedSecret_Type()
)
radiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerSharedSecret.setStatus("mandatory")
_RadiusServerEnabled_Type = Integer32
_RadiusServerEnabled_Object = MibTableColumn
radiusServerEnabled = _RadiusServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 19),
    _RadiusServerEnabled_Type()
)
radiusServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerEnabled.setStatus("mandatory")


class _RadiusServerResponseTime_Type(Integer32):
    """Custom type radiusServerResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RadiusServerResponseTime_Type.__name__ = "Integer32"
_RadiusServerResponseTime_Object = MibTableColumn
radiusServerResponseTime = _RadiusServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 20),
    _RadiusServerResponseTime_Type()
)
radiusServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerResponseTime.setStatus("mandatory")


class _RadiusServerMaximumRetransmission_Type(Integer32):
    """Custom type radiusServerMaximumRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RadiusServerMaximumRetransmission_Type.__name__ = "Integer32"
_RadiusServerMaximumRetransmission_Object = MibTableColumn
radiusServerMaximumRetransmission = _RadiusServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 1, 1, 2, 1, 21),
    _RadiusServerMaximumRetransmission_Type()
)
radiusServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerMaximumRetransmission.setStatus("mandatory")
_RadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusClientMIBConformance = _RadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 2)
)
_RadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusClientMIBCompliances = _RadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 2, 1)
)
_RadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusClientMIBGroups = _RadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 7, 2, 2, 2)
)
_OrinocoShimECPSetup_ObjectIdentity = ObjectIdentity
orinocoShimECPSetup = _OrinocoShimECPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 8)
)
_PsShimECPRetransmissionCount_Type = Integer32
_PsShimECPRetransmissionCount_Object = MibScalar
psShimECPRetransmissionCount = _PsShimECPRetransmissionCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 8, 1),
    _PsShimECPRetransmissionCount_Type()
)
psShimECPRetransmissionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRetransmissionCount.setStatus("mandatory")
_PsShimECPRepeatResponseCount_Type = Integer32
_PsShimECPRepeatResponseCount_Object = MibScalar
psShimECPRepeatResponseCount = _PsShimECPRepeatResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 8, 2),
    _PsShimECPRepeatResponseCount_Type()
)
psShimECPRepeatResponseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRepeatResponseCount.setStatus("mandatory")
_PsShimECPRetransmissionTimeout_Type = Integer32
_PsShimECPRetransmissionTimeout_Object = MibScalar
psShimECPRetransmissionTimeout = _PsShimECPRetransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 8, 3),
    _PsShimECPRetransmissionTimeout_Type()
)
psShimECPRetransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRetransmissionTimeout.setStatus("mandatory")
_OrinocoDiagnostics_ObjectIdentity = ObjectIdentity
orinocoDiagnostics = _OrinocoDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 10)
)
_OrinocoIAPP_ObjectIdentity = ObjectIdentity
orinocoIAPP = _OrinocoIAPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11)
)
_PsIappStatus_Type = Integer32
_PsIappStatus_Object = MibScalar
psIappStatus = _PsIappStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 1),
    _PsIappStatus_Type()
)
psIappStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIappStatus.setStatus("mandatory")
_PsIappAnnReqOut_Type = Counter32
_PsIappAnnReqOut_Object = MibScalar
psIappAnnReqOut = _PsIappAnnReqOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 2),
    _PsIappAnnReqOut_Type()
)
psIappAnnReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappAnnReqOut.setStatus("mandatory")
_PsIappAnnReqIn_Type = Counter32
_PsIappAnnReqIn_Object = MibScalar
psIappAnnReqIn = _PsIappAnnReqIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 3),
    _PsIappAnnReqIn_Type()
)
psIappAnnReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappAnnReqIn.setStatus("mandatory")
_PsIappAnnRespOut_Type = Counter32
_PsIappAnnRespOut_Object = MibScalar
psIappAnnRespOut = _PsIappAnnRespOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 4),
    _PsIappAnnRespOut_Type()
)
psIappAnnRespOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappAnnRespOut.setStatus("mandatory")
_PsIappAnnRespIn_Type = Counter32
_PsIappAnnRespIn_Object = MibScalar
psIappAnnRespIn = _PsIappAnnRespIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 5),
    _PsIappAnnRespIn_Type()
)
psIappAnnRespIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappAnnRespIn.setStatus("mandatory")
_PsIappHandOvrReqOut_Type = Counter32
_PsIappHandOvrReqOut_Object = MibScalar
psIappHandOvrReqOut = _PsIappHandOvrReqOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 6),
    _PsIappHandOvrReqOut_Type()
)
psIappHandOvrReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappHandOvrReqOut.setStatus("mandatory")
_PsIappHandOvrReqIn_Type = Counter32
_PsIappHandOvrReqIn_Object = MibScalar
psIappHandOvrReqIn = _PsIappHandOvrReqIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 7),
    _PsIappHandOvrReqIn_Type()
)
psIappHandOvrReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappHandOvrReqIn.setStatus("mandatory")
_PsIappHandOvrRespOut_Type = Counter32
_PsIappHandOvrRespOut_Object = MibScalar
psIappHandOvrRespOut = _PsIappHandOvrRespOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 8),
    _PsIappHandOvrRespOut_Type()
)
psIappHandOvrRespOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappHandOvrRespOut.setStatus("mandatory")
_PsIappHandOvrRespIn_Type = Counter32
_PsIappHandOvrRespIn_Object = MibScalar
psIappHandOvrRespIn = _PsIappHandOvrRespIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 9),
    _PsIappHandOvrRespIn_Type()
)
psIappHandOvrRespIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappHandOvrRespIn.setStatus("mandatory")
_PsIappEndSessOut_Type = Counter32
_PsIappEndSessOut_Object = MibScalar
psIappEndSessOut = _PsIappEndSessOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 10),
    _PsIappEndSessOut_Type()
)
psIappEndSessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappEndSessOut.setStatus("mandatory")
_PsIappEndSessIn_Type = Counter32
_PsIappEndSessIn_Object = MibScalar
psIappEndSessIn = _PsIappEndSessIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 11),
    _PsIappEndSessIn_Type()
)
psIappEndSessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappEndSessIn.setStatus("mandatory")
_PsIappEndSessAckOut_Type = Counter32
_PsIappEndSessAckOut_Object = MibScalar
psIappEndSessAckOut = _PsIappEndSessAckOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 12),
    _PsIappEndSessAckOut_Type()
)
psIappEndSessAckOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappEndSessAckOut.setStatus("mandatory")
_PsIappEndSessAckIn_Type = Counter32
_PsIappEndSessAckIn_Object = MibScalar
psIappEndSessAckIn = _PsIappEndSessAckIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 13),
    _PsIappEndSessAckIn_Type()
)
psIappEndSessAckIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappEndSessAckIn.setStatus("mandatory")
_PsIappPduDrops_Type = Counter32
_PsIappPduDrops_Object = MibScalar
psIappPduDrops = _PsIappPduDrops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 14),
    _PsIappPduDrops_Type()
)
psIappPduDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappPduDrops.setStatus("mandatory")
_PsIappHandOvrReqReSent_Type = Counter32
_PsIappHandOvrReqReSent_Object = MibScalar
psIappHandOvrReqReSent = _PsIappHandOvrReqReSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 15),
    _PsIappHandOvrReqReSent_Type()
)
psIappHandOvrReqReSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappHandOvrReqReSent.setStatus("mandatory")
_PsIappAnnInterval_Type = Integer32
_PsIappAnnInterval_Object = MibScalar
psIappAnnInterval = _PsIappAnnInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 16),
    _PsIappAnnInterval_Type()
)
psIappAnnInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIappAnnInterval.setStatus("mandatory")
_PsIappAnnRespTime_Type = Integer32
_PsIappAnnRespTime_Object = MibScalar
psIappAnnRespTime = _PsIappAnnRespTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 17),
    _PsIappAnnRespTime_Type()
)
psIappAnnRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappAnnRespTime.setStatus("mandatory")
_PsIappHandOvrTimeOut_Type = Integer32
_PsIappHandOvrTimeOut_Object = MibScalar
psIappHandOvrTimeOut = _PsIappHandOvrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 18),
    _PsIappHandOvrTimeOut_Type()
)
psIappHandOvrTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIappHandOvrTimeOut.setStatus("mandatory")


class _PsIappMaxHandOvrRetries_Type(Integer32):
    """Custom type psIappMaxHandOvrRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PsIappMaxHandOvrRetries_Type.__name__ = "Integer32"
_PsIappMaxHandOvrRetries_Object = MibScalar
psIappMaxHandOvrRetries = _PsIappMaxHandOvrRetries_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 19),
    _PsIappMaxHandOvrRetries_Type()
)
psIappMaxHandOvrRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIappMaxHandOvrRetries.setStatus("mandatory")
_PsIappRoamingClients_Type = Counter32
_PsIappRoamingClients_Object = MibScalar
psIappRoamingClients = _PsIappRoamingClients_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 11, 20),
    _PsIappRoamingClients_Type()
)
psIappRoamingClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIappRoamingClients.setStatus("mandatory")
_OrinocoIPX_ObjectIdentity = ObjectIdentity
orinocoIPX = _OrinocoIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12)
)
_PsIpxStatus_Type = Integer32
_PsIpxStatus_Object = MibScalar
psIpxStatus = _PsIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 1),
    _PsIpxStatus_Type()
)
psIpxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIpxStatus.setStatus("mandatory")
_PsIpxDefaultRouterNodeNum_Type = PhysAddress
_PsIpxDefaultRouterNodeNum_Object = MibScalar
psIpxDefaultRouterNodeNum = _PsIpxDefaultRouterNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 2),
    _PsIpxDefaultRouterNodeNum_Type()
)
psIpxDefaultRouterNodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIpxDefaultRouterNodeNum.setStatus("mandatory")
_PsIpxWiredToWlessBridged_Type = Counter32
_PsIpxWiredToWlessBridged_Object = MibScalar
psIpxWiredToWlessBridged = _PsIpxWiredToWlessBridged_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 3),
    _PsIpxWiredToWlessBridged_Type()
)
psIpxWiredToWlessBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIpxWiredToWlessBridged.setStatus("mandatory")
_PsIpxWlessToWiredBridged_Type = Counter32
_PsIpxWlessToWiredBridged_Object = MibScalar
psIpxWlessToWiredBridged = _PsIpxWlessToWiredBridged_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 4),
    _PsIpxWlessToWiredBridged_Type()
)
psIpxWlessToWiredBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIpxWlessToWiredBridged.setStatus("mandatory")
_PsIpxEthernetEncapsulationFormat_Type = Integer32
_PsIpxEthernetEncapsulationFormat_Object = MibScalar
psIpxEthernetEncapsulationFormat = _PsIpxEthernetEncapsulationFormat_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 5),
    _PsIpxEthernetEncapsulationFormat_Type()
)
psIpxEthernetEncapsulationFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIpxEthernetEncapsulationFormat.setStatus("mandatory")
_PsASClientTable_Object = MibTable
psASClientTable = _PsASClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6)
)
if mibBuilder.loadTexts:
    psASClientTable.setStatus("mandatory")
_PsASClientEntry_Object = MibTableRow
psASClientEntry = _PsASClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1)
)
psASClientEntry.setIndexNames(
    (0, "AS-2000", "psPPPSessionId"),
)
if mibBuilder.loadTexts:
    psASClientEntry.setStatus("mandatory")
_PsPPPSessionId_Type = Integer32
_PsPPPSessionId_Object = MibTableColumn
psPPPSessionId = _PsPPPSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 1),
    _PsPPPSessionId_Type()
)
psPPPSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPPPSessionId.setStatus("mandatory")
_PsIpxClientNetworkNumber_Type = OctetString
_PsIpxClientNetworkNumber_Object = MibTableColumn
psIpxClientNetworkNumber = _PsIpxClientNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 2),
    _PsIpxClientNetworkNumber_Type()
)
psIpxClientNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIpxClientNetworkNumber.setStatus("mandatory")
_PsIpxClientMAC_Type = PhysAddress
_PsIpxClientMAC_Object = MibTableColumn
psIpxClientMAC = _PsIpxClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 3),
    _PsIpxClientMAC_Type()
)
psIpxClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIpxClientMAC.setStatus("mandatory")


class _PsIpxClientStatus_Type(Integer32):
    """Custom type psIpxClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("up", 1))
    )


_PsIpxClientStatus_Type.__name__ = "Integer32"
_PsIpxClientStatus_Object = MibTableColumn
psIpxClientStatus = _PsIpxClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 4),
    _PsIpxClientStatus_Type()
)
psIpxClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIpxClientStatus.setStatus("mandatory")
_PsASClientSessionUpTime_Type = TimeTicks
_PsASClientSessionUpTime_Object = MibTableColumn
psASClientSessionUpTime = _PsASClientSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 5),
    _PsASClientSessionUpTime_Type()
)
psASClientSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psASClientSessionUpTime.setStatus("mandatory")
_PsASClientPacketsIn_Type = Counter32
_PsASClientPacketsIn_Object = MibTableColumn
psASClientPacketsIn = _PsASClientPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 6),
    _PsASClientPacketsIn_Type()
)
psASClientPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psASClientPacketsIn.setStatus("mandatory")
_PsASClientPacketsOut_Type = Counter32
_PsASClientPacketsOut_Object = MibTableColumn
psASClientPacketsOut = _PsASClientPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 12, 6, 1, 7),
    _PsASClientPacketsOut_Type()
)
psASClientPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psASClientPacketsOut.setStatus("mandatory")
_OrinocoLinkTest_ObjectIdentity = ObjectIdentity
orinocoLinkTest = _OrinocoLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13)
)
_OriLinkTestTimeOut_Type = Integer32
_OriLinkTestTimeOut_Object = MibScalar
oriLinkTestTimeOut = _OriLinkTestTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 1),
    _OriLinkTestTimeOut_Type()
)
oriLinkTestTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestTimeOut.setStatus("mandatory")
_OriLinkTestInterval_Type = Integer32
_OriLinkTestInterval_Object = MibScalar
oriLinkTestInterval = _OriLinkTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 3),
    _OriLinkTestInterval_Type()
)
oriLinkTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestInterval.setStatus("mandatory")
_OriLinkTestExplore_Type = Integer32
_OriLinkTestExplore_Object = MibScalar
oriLinkTestExplore = _OriLinkTestExplore_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 4),
    _OriLinkTestExplore_Type()
)
oriLinkTestExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestExplore.setStatus("mandatory")
_OriLinkTestTable_Object = MibTable
oriLinkTestTable = _OriLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5)
)
if mibBuilder.loadTexts:
    oriLinkTestTable.setStatus("mandatory")
_OriLinkTestTableEntry_Object = MibTableRow
oriLinkTestTableEntry = _OriLinkTestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1)
)
oriLinkTestTableEntry.setIndexNames(
    (0, "AS-2000", "oriLinkTestTableIndex"),
)
if mibBuilder.loadTexts:
    oriLinkTestTableEntry.setStatus("mandatory")
_OriLinkTestTableIndex_Type = Integer32
_OriLinkTestTableIndex_Object = MibTableColumn
oriLinkTestTableIndex = _OriLinkTestTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 1),
    _OriLinkTestTableIndex_Type()
)
oriLinkTestTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestTableIndex.setStatus("mandatory")
_OriLinkTestInProgress_Type = Integer32
_OriLinkTestInProgress_Object = MibTableColumn
oriLinkTestInProgress = _OriLinkTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 2),
    _OriLinkTestInProgress_Type()
)
oriLinkTestInProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oriLinkTestInProgress.setStatus("mandatory")
_OriLinkTestStationName_Type = DisplayString
_OriLinkTestStationName_Object = MibTableColumn
oriLinkTestStationName = _OriLinkTestStationName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 3),
    _OriLinkTestStationName_Type()
)
oriLinkTestStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestStationName.setStatus("mandatory")
_OriLinkTestMACAddress_Type = PhysAddress
_OriLinkTestMACAddress_Object = MibTableColumn
oriLinkTestMACAddress = _OriLinkTestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 4),
    _OriLinkTestMACAddress_Type()
)
oriLinkTestMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestMACAddress.setStatus("mandatory")
_OriLinkTestStationProfile_Type = Integer32
_OriLinkTestStationProfile_Object = MibTableColumn
oriLinkTestStationProfile = _OriLinkTestStationProfile_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 5),
    _OriLinkTestStationProfile_Type()
)
oriLinkTestStationProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestStationProfile.setStatus("mandatory")
_OriLinkTestOurCurSignalLevel_Type = Integer32
_OriLinkTestOurCurSignalLevel_Object = MibTableColumn
oriLinkTestOurCurSignalLevel = _OriLinkTestOurCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 6),
    _OriLinkTestOurCurSignalLevel_Type()
)
oriLinkTestOurCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurSignalLevel.setStatus("mandatory")
_OriLinkTestOurCurNoiseLevel_Type = Integer32
_OriLinkTestOurCurNoiseLevel_Object = MibTableColumn
oriLinkTestOurCurNoiseLevel = _OriLinkTestOurCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 7),
    _OriLinkTestOurCurNoiseLevel_Type()
)
oriLinkTestOurCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurNoiseLevel.setStatus("mandatory")
_OriLinkTestOurCurSNR_Type = Integer32
_OriLinkTestOurCurSNR_Object = MibTableColumn
oriLinkTestOurCurSNR = _OriLinkTestOurCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 8),
    _OriLinkTestOurCurSNR_Type()
)
oriLinkTestOurCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurCurSNR.setStatus("mandatory")
_OriLinkTestOurMinSignalLevel_Type = Integer32
_OriLinkTestOurMinSignalLevel_Object = MibTableColumn
oriLinkTestOurMinSignalLevel = _OriLinkTestOurMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 9),
    _OriLinkTestOurMinSignalLevel_Type()
)
oriLinkTestOurMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinSignalLevel.setStatus("mandatory")
_OriLinkTestOurMinNoiseLevel_Type = Integer32
_OriLinkTestOurMinNoiseLevel_Object = MibTableColumn
oriLinkTestOurMinNoiseLevel = _OriLinkTestOurMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 10),
    _OriLinkTestOurMinNoiseLevel_Type()
)
oriLinkTestOurMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinNoiseLevel.setStatus("mandatory")
_OriLinkTestOurMinSNR_Type = Integer32
_OriLinkTestOurMinSNR_Object = MibTableColumn
oriLinkTestOurMinSNR = _OriLinkTestOurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 11),
    _OriLinkTestOurMinSNR_Type()
)
oriLinkTestOurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMinSNR.setStatus("mandatory")
_OriLinkTestOurMaxSignalLevel_Type = Integer32
_OriLinkTestOurMaxSignalLevel_Object = MibTableColumn
oriLinkTestOurMaxSignalLevel = _OriLinkTestOurMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 12),
    _OriLinkTestOurMaxSignalLevel_Type()
)
oriLinkTestOurMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxSignalLevel.setStatus("mandatory")
_OriLinkTestOurMaxNoiseLevel_Type = Integer32
_OriLinkTestOurMaxNoiseLevel_Object = MibTableColumn
oriLinkTestOurMaxNoiseLevel = _OriLinkTestOurMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 13),
    _OriLinkTestOurMaxNoiseLevel_Type()
)
oriLinkTestOurMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxNoiseLevel.setStatus("mandatory")
_OriLinkTestOurMaxSNR_Type = Integer32
_OriLinkTestOurMaxSNR_Object = MibTableColumn
oriLinkTestOurMaxSNR = _OriLinkTestOurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 14),
    _OriLinkTestOurMaxSNR_Type()
)
oriLinkTestOurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMaxSNR.setStatus("mandatory")
_OriLinkTestOurLowFrameCount_Type = Integer32
_OriLinkTestOurLowFrameCount_Object = MibTableColumn
oriLinkTestOurLowFrameCount = _OriLinkTestOurLowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 15),
    _OriLinkTestOurLowFrameCount_Type()
)
oriLinkTestOurLowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurLowFrameCount.setStatus("mandatory")
_OriLinkTestOurStandardFrameCount_Type = Integer32
_OriLinkTestOurStandardFrameCount_Object = MibTableColumn
oriLinkTestOurStandardFrameCount = _OriLinkTestOurStandardFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 16),
    _OriLinkTestOurStandardFrameCount_Type()
)
oriLinkTestOurStandardFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurStandardFrameCount.setStatus("mandatory")
_OriLinkTestOurMediumFrameCount_Type = Integer32
_OriLinkTestOurMediumFrameCount_Object = MibTableColumn
oriLinkTestOurMediumFrameCount = _OriLinkTestOurMediumFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 17),
    _OriLinkTestOurMediumFrameCount_Type()
)
oriLinkTestOurMediumFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurMediumFrameCount.setStatus("mandatory")
_OriLinkTestOurHighFrameCount_Type = Integer32
_OriLinkTestOurHighFrameCount_Object = MibTableColumn
oriLinkTestOurHighFrameCount = _OriLinkTestOurHighFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 18),
    _OriLinkTestOurHighFrameCount_Type()
)
oriLinkTestOurHighFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestOurHighFrameCount.setStatus("mandatory")
_OriLinkTestHisCurSignalLevel_Type = Integer32
_OriLinkTestHisCurSignalLevel_Object = MibTableColumn
oriLinkTestHisCurSignalLevel = _OriLinkTestHisCurSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 19),
    _OriLinkTestHisCurSignalLevel_Type()
)
oriLinkTestHisCurSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurSignalLevel.setStatus("mandatory")
_OriLinkTestHisCurNoiseLevel_Type = Integer32
_OriLinkTestHisCurNoiseLevel_Object = MibTableColumn
oriLinkTestHisCurNoiseLevel = _OriLinkTestHisCurNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 20),
    _OriLinkTestHisCurNoiseLevel_Type()
)
oriLinkTestHisCurNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurNoiseLevel.setStatus("mandatory")
_OriLinkTestHisCurSNR_Type = Integer32
_OriLinkTestHisCurSNR_Object = MibTableColumn
oriLinkTestHisCurSNR = _OriLinkTestHisCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 21),
    _OriLinkTestHisCurSNR_Type()
)
oriLinkTestHisCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisCurSNR.setStatus("mandatory")
_OriLinkTestHisMinSignalLevel_Type = Integer32
_OriLinkTestHisMinSignalLevel_Object = MibTableColumn
oriLinkTestHisMinSignalLevel = _OriLinkTestHisMinSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 22),
    _OriLinkTestHisMinSignalLevel_Type()
)
oriLinkTestHisMinSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinSignalLevel.setStatus("mandatory")
_OriLinkTestHisMinNoiseLevel_Type = Integer32
_OriLinkTestHisMinNoiseLevel_Object = MibTableColumn
oriLinkTestHisMinNoiseLevel = _OriLinkTestHisMinNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 23),
    _OriLinkTestHisMinNoiseLevel_Type()
)
oriLinkTestHisMinNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinNoiseLevel.setStatus("mandatory")
_OriLinkTestHisMinSNR_Type = Integer32
_OriLinkTestHisMinSNR_Object = MibTableColumn
oriLinkTestHisMinSNR = _OriLinkTestHisMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 24),
    _OriLinkTestHisMinSNR_Type()
)
oriLinkTestHisMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMinSNR.setStatus("mandatory")
_OriLinkTestHisMaxSignalLevel_Type = Integer32
_OriLinkTestHisMaxSignalLevel_Object = MibTableColumn
oriLinkTestHisMaxSignalLevel = _OriLinkTestHisMaxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 25),
    _OriLinkTestHisMaxSignalLevel_Type()
)
oriLinkTestHisMaxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxSignalLevel.setStatus("mandatory")
_OriLinkTestHisMaxNoiseLevel_Type = Integer32
_OriLinkTestHisMaxNoiseLevel_Object = MibTableColumn
oriLinkTestHisMaxNoiseLevel = _OriLinkTestHisMaxNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 26),
    _OriLinkTestHisMaxNoiseLevel_Type()
)
oriLinkTestHisMaxNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxNoiseLevel.setStatus("mandatory")
_OriLinkTestHisMaxSNR_Type = Integer32
_OriLinkTestHisMaxSNR_Object = MibTableColumn
oriLinkTestHisMaxSNR = _OriLinkTestHisMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 27),
    _OriLinkTestHisMaxSNR_Type()
)
oriLinkTestHisMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMaxSNR.setStatus("mandatory")
_OriLinkTestHisLowFrameCount_Type = Integer32
_OriLinkTestHisLowFrameCount_Object = MibTableColumn
oriLinkTestHisLowFrameCount = _OriLinkTestHisLowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 28),
    _OriLinkTestHisLowFrameCount_Type()
)
oriLinkTestHisLowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisLowFrameCount.setStatus("mandatory")
_OriLinkTestHisStandardFrameCount_Type = Integer32
_OriLinkTestHisStandardFrameCount_Object = MibTableColumn
oriLinkTestHisStandardFrameCount = _OriLinkTestHisStandardFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 29),
    _OriLinkTestHisStandardFrameCount_Type()
)
oriLinkTestHisStandardFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisStandardFrameCount.setStatus("mandatory")
_OriLinkTestHisMediumFrameCount_Type = Integer32
_OriLinkTestHisMediumFrameCount_Object = MibTableColumn
oriLinkTestHisMediumFrameCount = _OriLinkTestHisMediumFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 30),
    _OriLinkTestHisMediumFrameCount_Type()
)
oriLinkTestHisMediumFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisMediumFrameCount.setStatus("mandatory")
_OriLinkTestHisHighFrameCount_Type = Integer32
_OriLinkTestHisHighFrameCount_Object = MibTableColumn
oriLinkTestHisHighFrameCount = _OriLinkTestHisHighFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 31),
    _OriLinkTestHisHighFrameCount_Type()
)
oriLinkTestHisHighFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestHisHighFrameCount.setStatus("mandatory")
_OriLinkTestInterface_Type = Integer32
_OriLinkTestInterface_Object = MibTableColumn
oriLinkTestInterface = _OriLinkTestInterface_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 32),
    _OriLinkTestInterface_Type()
)
oriLinkTestInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestInterface.setStatus("mandatory")
_OriLinkTestRadioType_Type = Integer32
_OriLinkTestRadioType_Object = MibTableColumn
oriLinkTestRadioType = _OriLinkTestRadioType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 13, 5, 1, 33),
    _OriLinkTestRadioType_Type()
)
oriLinkTestRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oriLinkTestRadioType.setStatus("mandatory")
_AccessServerTraps_ObjectIdentity = ObjectIdentity
accessServerTraps = _AccessServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15)
)
_AccessServerTrapVariables_ObjectIdentity = ObjectIdentity
accessServerTrapVariables = _AccessServerTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1)
)
_AccessServerGenericInformationMessage_Type = DisplayString
_AccessServerGenericInformationMessage_Object = MibScalar
accessServerGenericInformationMessage = _AccessServerGenericInformationMessage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 1),
    _AccessServerGenericInformationMessage_Type()
)
accessServerGenericInformationMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerGenericInformationMessage.setStatus("mandatory")
_AccessServerMacAddress_Type = PhysAddress
_AccessServerMacAddress_Object = MibScalar
accessServerMacAddress = _AccessServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 2),
    _AccessServerMacAddress_Type()
)
accessServerMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerMacAddress.setStatus("mandatory")
_AccessServerFailedTFTPServerAddress_Type = IpAddress
_AccessServerFailedTFTPServerAddress_Object = MibScalar
accessServerFailedTFTPServerAddress = _AccessServerFailedTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 3),
    _AccessServerFailedTFTPServerAddress_Type()
)
accessServerFailedTFTPServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerFailedTFTPServerAddress.setStatus("mandatory")
_AccessServerFailedTFTPFilename_Type = DisplayString
_AccessServerFailedTFTPFilename_Object = MibScalar
accessServerFailedTFTPFilename = _AccessServerFailedTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 4),
    _AccessServerFailedTFTPFilename_Type()
)
accessServerFailedTFTPFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerFailedTFTPFilename.setStatus("mandatory")
_AccessServerFailedTFTPOperation_Type = Integer32
_AccessServerFailedTFTPOperation_Object = MibScalar
accessServerFailedTFTPOperation = _AccessServerFailedTFTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 5),
    _AccessServerFailedTFTPOperation_Type()
)
accessServerFailedTFTPOperation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerFailedTFTPOperation.setStatus("mandatory")
_AccessServerSuspendedTaskName_Type = DisplayString
_AccessServerSuspendedTaskName_Object = MibScalar
accessServerSuspendedTaskName = _AccessServerSuspendedTaskName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 6),
    _AccessServerSuspendedTaskName_Type()
)
accessServerSuspendedTaskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerSuspendedTaskName.setStatus("mandatory")


class _AccessServerWirelessCard_Type(Integer32):
    """Custom type accessServerWirelessCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pc-cardA", 1),
          ("pc-cardB", 2))
    )


_AccessServerWirelessCard_Type.__name__ = "Integer32"
_AccessServerWirelessCard_Object = MibScalar
accessServerWirelessCard = _AccessServerWirelessCard_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 1, 7),
    _AccessServerWirelessCard_Type()
)
accessServerWirelessCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessServerWirelessCard.setStatus("mandatory")
_AccessServerFlashRelatedTraps_ObjectIdentity = ObjectIdentity
accessServerFlashRelatedTraps = _AccessServerFlashRelatedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 2)
)
_AccessServerConfigurationRelatedTraps_ObjectIdentity = ObjectIdentity
accessServerConfigurationRelatedTraps = _AccessServerConfigurationRelatedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3)
)
_AccessServerDiagnosticTraps_ObjectIdentity = ObjectIdentity
accessServerDiagnosticTraps = _AccessServerDiagnosticTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4)
)
_AccessServerImageTraps_ObjectIdentity = ObjectIdentity
accessServerImageTraps = _AccessServerImageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 5)
)

# Managed Objects groups


# Notification objects

accessServerFlashEmpty = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 2, 0, 1)
)
if mibBuilder.loadTexts:
    accessServerFlashEmpty.setStatus(
        ""
    )

accessServerFlashCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 2, 0, 2)
)
if mibBuilder.loadTexts:
    accessServerFlashCorrupted.setStatus(
        ""
    )

accessServerInvalidKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 1)
)
if mibBuilder.loadTexts:
    accessServerInvalidKey.setStatus(
        ""
    )

accessServerAPMNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 2)
)
if mibBuilder.loadTexts:
    accessServerAPMNotConfigured.setStatus(
        ""
    )

accessServerWLCIncompatibleFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 3)
)
if mibBuilder.loadTexts:
    accessServerWLCIncompatibleFirmware.setStatus(
        ""
    )

accessServerWLCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 4)
)
if mibBuilder.loadTexts:
    accessServerWLCFailure.setStatus(
        ""
    )

accessServerWLCRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 5)
)
if mibBuilder.loadTexts:
    accessServerWLCRemoval.setStatus(
        ""
    )

accessServerRadiusNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 6)
)
if mibBuilder.loadTexts:
    accessServerRadiusNotConfigured.setStatus(
        ""
    )

accessServerDNSIPNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 7)
)
if mibBuilder.loadTexts:
    accessServerDNSIPNotConfigured.setStatus(
        ""
    )

accessServerNBNSIPNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 8)
)
if mibBuilder.loadTexts:
    accessServerNBNSIPNotConfigured.setStatus(
        ""
    )

accessServerRadiusAuthenticationNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 9)
)
if mibBuilder.loadTexts:
    accessServerRadiusAuthenticationNotConfigured.setStatus(
        ""
    )

accessServerRadiusAccountingNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 10)
)
if mibBuilder.loadTexts:
    accessServerRadiusAccountingNotConfigured.setStatus(
        ""
    )

accessServerDuplicateIPAddressEncountered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 11)
)
if mibBuilder.loadTexts:
    accessServerDuplicateIPAddressEncountered.setStatus(
        ""
    )

accessServerWLCVoltageDiscrepancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 12)
)
if mibBuilder.loadTexts:
    accessServerWLCVoltageDiscrepancy.setStatus(
        ""
    )

accessServerWLCIncompatibleVendor = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 13)
)
if mibBuilder.loadTexts:
    accessServerWLCIncompatibleVendor.setStatus(
        ""
    )

accessServerWLCFirmwareDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 3, 0, 14)
)
if mibBuilder.loadTexts:
    accessServerWLCFirmwareDownloadFailure.setStatus(
        ""
    )

accessServerTFTPInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 1)
)
if mibBuilder.loadTexts:
    accessServerTFTPInitiated.setStatus(
        ""
    )

accessServerTFTPCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 2)
)
if mibBuilder.loadTexts:
    accessServerTFTPCompleted.setStatus(
        ""
    )

accessServerTFTPFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 3)
)
if mibBuilder.loadTexts:
    accessServerTFTPFailure.setStatus(
        ""
    )

accessServerAdminStateMadeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 4)
)
if mibBuilder.loadTexts:
    accessServerAdminStateMadeUp.setStatus(
        ""
    )

accessServerAdminStateMadeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 5)
)
if mibBuilder.loadTexts:
    accessServerAdminStateMadeDown.setStatus(
        ""
    )

accessServerRebootingNow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 6)
)
if mibBuilder.loadTexts:
    accessServerRebootingNow.setStatus(
        ""
    )

accessServerTaskSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 7)
)
if mibBuilder.loadTexts:
    accessServerTaskSuspended.setStatus(
        ""
    )

accessServerBootPFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 8)
)
if mibBuilder.loadTexts:
    accessServerBootPFailed.setStatus(
        ""
    )

accessServerDHCPFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 4, 0, 9)
)
if mibBuilder.loadTexts:
    accessServerDHCPFailed.setStatus(
        ""
    )

accessServerZeroSizeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 5, 0, 1)
)
if mibBuilder.loadTexts:
    accessServerZeroSizeImage.setStatus(
        ""
    )

accessServerNonVxWorksImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 5, 0, 2)
)
if mibBuilder.loadTexts:
    accessServerNonVxWorksImage.setStatus(
        ""
    )

accessServerImageTooLarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 4, 3, 15, 5, 0, 3)
)
if mibBuilder.loadTexts:
    accessServerImageTooLarge.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AS-2000",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "lucent": lucent,
       "products": products,
       "orinocoProducts": orinocoProducts,
       "as2000Product": as2000Product,
       "mibs": mibs,
       "orinoco": orinoco,
       "as2000": as2000,
       "orinocoInterface": orinocoInterface,
       "orinocoPHY": orinocoPHY,
       "pliSystemName": pliSystemName,
       "psWlanIfTable": psWlanIfTable,
       "psWlanIfEntry": psWlanIfEntry,
       "pliWlanIfIndex": pliWlanIfIndex,
       "pliWlanIfNetworkName": pliWlanIfNetworkName,
       "pliWlanIfMACAddress": pliWlanIfMACAddress,
       "pliWlanIfMediumReservation": pliWlanIfMediumReservation,
       "pliWlanIfTransmitRate": pliWlanIfTransmitRate,
       "pliWlanIfOperatingFrequency": pliWlanIfOperatingFrequency,
       "pliWlanIfAPDensity": pliWlanIfAPDensity,
       "pliWlanIfClosedSystem": pliWlanIfClosedSystem,
       "pliWlanIfAllowedTransmitRates": pliWlanIfAllowedTransmitRates,
       "pliWlanIfRegulatoryDomainList": pliWlanIfRegulatoryDomainList,
       "pliWlanIfAllowedOperatingFrequencies": pliWlanIfAllowedOperatingFrequencies,
       "pliWlanIfCapabilityOptions": pliWlanIfCapabilityOptions,
       "pliWlanIfProfileCode": pliWlanIfProfileCode,
       "orinocoDriver": orinocoDriver,
       "pliDriverName": pliDriverName,
       "pliDriverVersion": pliDriverVersion,
       "orinocoSNMPSetup": orinocoSNMPSetup,
       "psSNMPReadPassword": psSNMPReadPassword,
       "psSNMPReadWritePassword": psSNMPReadWritePassword,
       "psSNMPTrapHostIPAddress": psSNMPTrapHostIPAddress,
       "psSNMPTrapHostPassword": psSNMPTrapHostPassword,
       "psSNMPManagerCount": psSNMPManagerCount,
       "psSNMPAccessTable": psSNMPAccessTable,
       "psSNMPAccessTableEntry": psSNMPAccessTableEntry,
       "managerIndex": managerIndex,
       "managerIPAddress": managerIPAddress,
       "managerSubnetMask": managerSubnetMask,
       "managerStatus": managerStatus,
       "psSNMPInBadManagers": psSNMPInBadManagers,
       "psTestSNMPReadWritePassword": psTestSNMPReadWritePassword,
       "orinocoPPPSetup": orinocoPPPSetup,
       "psPPPIPAddressAssignmentType": psPPPIPAddressAssignmentType,
       "psPPPNoOfMACIPMappingEntries": psPPPNoOfMACIPMappingEntries,
       "psPPPMACIPMappingTable": psPPPMACIPMappingTable,
       "psPPPMACIPMappingTableEntry": psPPPMACIPMappingTableEntry,
       "mACIPIndex": mACIPIndex,
       "mACAddress": mACAddress,
       "iPAddress": iPAddress,
       "comment": comment,
       "entryStatus": entryStatus,
       "psPPPKeepAliveInterval": psPPPKeepAliveInterval,
       "psPPPNoOfKeepAliveTimeouts": psPPPNoOfKeepAliveTimeouts,
       "psPPPPrimaryDNSIPAddress": psPPPPrimaryDNSIPAddress,
       "psPPPSecondaryDNSIPAddress": psPPPSecondaryDNSIPAddress,
       "psPPPMaxNoOfUsers": psPPPMaxNoOfUsers,
       "psPPPCHAPStatus": psPPPCHAPStatus,
       "psPPPCHAPPriority": psPPPCHAPPriority,
       "psPPPPAPStatus": psPPPPAPStatus,
       "psPPPPAPPriority": psPPPPAPPriority,
       "psPPPPrimaryNBNSIPAddress": psPPPPrimaryNBNSIPAddress,
       "psPPPSecondaryNBNSIPAddress": psPPPSecondaryNBNSIPAddress,
       "psPPPIPRangeTable": psPPPIPRangeTable,
       "psPPPIPRangeTableEntry": psPPPIPRangeTableEntry,
       "pPPIPIndex": pPPIPIndex,
       "startIPAddress": startIPAddress,
       "endIPAddress": endIPAddress,
       "width": width,
       "status": status,
       "iPComment": iPComment,
       "psPPPSessionIdleTimeOut": psPPPSessionIdleTimeOut,
       "orinocoAgent": orinocoAgent,
       "psVersion": psVersion,
       "psIPAddress": psIPAddress,
       "psSubnetMask": psSubnetMask,
       "psDefaultGateway": psDefaultGateway,
       "psIPAddressType": psIPAddressType,
       "psAdministrativeState": psAdministrativeState,
       "psTFTPIPAddress": psTFTPIPAddress,
       "psTFTPFilename": psTFTPFilename,
       "psTFTPOperation": psTFTPOperation,
       "psReboot": psReboot,
       "psSecondsToAdminDown": psSecondsToAdminDown,
       "psContactEmail": psContactEmail,
       "psBSPBootloaderVersion": psBSPBootloaderVersion,
       "psTelnetSesssions": psTelnetSesssions,
       "psTelnetPassword": psTelnetPassword,
       "psTelnetPort": psTelnetPort,
       "psTelnetTimeout": psTelnetTimeout,
       "psTelnetLoginTimeout": psTelnetLoginTimeout,
       "psSerialBaudRate": psSerialBaudRate,
       "psSerialDataBits": psSerialDataBits,
       "psSerialParity": psSerialParity,
       "psSerialStopBits": psSerialStopBits,
       "psSerialFlowControl": psSerialFlowControl,
       "psTFTPFileType": psTFTPFileType,
       "psDeviceSerialNumber": psDeviceSerialNumber,
       "psBroadcastMessage": psBroadcastMessage,
       "psPOSTVersionNumber": psPOSTVersionNumber,
       "psHardwareVersionNumber": psHardwareVersionNumber,
       "radius": radius,
       "radiusClientMIB": radiusClientMIB,
       "radiusClientMIBObjects": radiusClientMIBObjects,
       "radiusClient": radiusClient,
       "radiusClientInvalidServerAddresses": radiusClientInvalidServerAddresses,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerType": radiusServerType,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerDestPortAuth": radiusServerDestPortAuth,
       "radiusServerDestPortAcct": radiusServerDestPortAcct,
       "radiusClientAccessRequests": radiusClientAccessRequests,
       "radiusClientAccessRetransmissions": radiusClientAccessRetransmissions,
       "radiusClientAccessAccepts": radiusClientAccessAccepts,
       "radiusClientAccessChallenges": radiusClientAccessChallenges,
       "radiusClientMalformedAccessResponses": radiusClientMalformedAccessResponses,
       "radiusClientAuthenticationBadAuthenticators": radiusClientAuthenticationBadAuthenticators,
       "radiusClientAccessRejects": radiusClientAccessRejects,
       "radiusClientTimeouts": radiusClientTimeouts,
       "radiusClientAccountingRequests": radiusClientAccountingRequests,
       "radiusClientAccountingRetransmissions": radiusClientAccountingRetransmissions,
       "radiusClientAccountingResponses": radiusClientAccountingResponses,
       "radiusClientAccountingBadAuthenticators": radiusClientAccountingBadAuthenticators,
       "radiusServerSharedSecret": radiusServerSharedSecret,
       "radiusServerEnabled": radiusServerEnabled,
       "radiusServerResponseTime": radiusServerResponseTime,
       "radiusServerMaximumRetransmission": radiusServerMaximumRetransmission,
       "radiusClientMIBConformance": radiusClientMIBConformance,
       "radiusClientMIBCompliances": radiusClientMIBCompliances,
       "radiusClientMIBGroups": radiusClientMIBGroups,
       "orinocoShimECPSetup": orinocoShimECPSetup,
       "psShimECPRetransmissionCount": psShimECPRetransmissionCount,
       "psShimECPRepeatResponseCount": psShimECPRepeatResponseCount,
       "psShimECPRetransmissionTimeout": psShimECPRetransmissionTimeout,
       "orinocoDiagnostics": orinocoDiagnostics,
       "orinocoIAPP": orinocoIAPP,
       "psIappStatus": psIappStatus,
       "psIappAnnReqOut": psIappAnnReqOut,
       "psIappAnnReqIn": psIappAnnReqIn,
       "psIappAnnRespOut": psIappAnnRespOut,
       "psIappAnnRespIn": psIappAnnRespIn,
       "psIappHandOvrReqOut": psIappHandOvrReqOut,
       "psIappHandOvrReqIn": psIappHandOvrReqIn,
       "psIappHandOvrRespOut": psIappHandOvrRespOut,
       "psIappHandOvrRespIn": psIappHandOvrRespIn,
       "psIappEndSessOut": psIappEndSessOut,
       "psIappEndSessIn": psIappEndSessIn,
       "psIappEndSessAckOut": psIappEndSessAckOut,
       "psIappEndSessAckIn": psIappEndSessAckIn,
       "psIappPduDrops": psIappPduDrops,
       "psIappHandOvrReqReSent": psIappHandOvrReqReSent,
       "psIappAnnInterval": psIappAnnInterval,
       "psIappAnnRespTime": psIappAnnRespTime,
       "psIappHandOvrTimeOut": psIappHandOvrTimeOut,
       "psIappMaxHandOvrRetries": psIappMaxHandOvrRetries,
       "psIappRoamingClients": psIappRoamingClients,
       "orinocoIPX": orinocoIPX,
       "psIpxStatus": psIpxStatus,
       "psIpxDefaultRouterNodeNum": psIpxDefaultRouterNodeNum,
       "psIpxWiredToWlessBridged": psIpxWiredToWlessBridged,
       "psIpxWlessToWiredBridged": psIpxWlessToWiredBridged,
       "psIpxEthernetEncapsulationFormat": psIpxEthernetEncapsulationFormat,
       "psASClientTable": psASClientTable,
       "psASClientEntry": psASClientEntry,
       "psPPPSessionId": psPPPSessionId,
       "psIpxClientNetworkNumber": psIpxClientNetworkNumber,
       "psIpxClientMAC": psIpxClientMAC,
       "psIpxClientStatus": psIpxClientStatus,
       "psASClientSessionUpTime": psASClientSessionUpTime,
       "psASClientPacketsIn": psASClientPacketsIn,
       "psASClientPacketsOut": psASClientPacketsOut,
       "orinocoLinkTest": orinocoLinkTest,
       "oriLinkTestTimeOut": oriLinkTestTimeOut,
       "oriLinkTestInterval": oriLinkTestInterval,
       "oriLinkTestExplore": oriLinkTestExplore,
       "oriLinkTestTable": oriLinkTestTable,
       "oriLinkTestTableEntry": oriLinkTestTableEntry,
       "oriLinkTestTableIndex": oriLinkTestTableIndex,
       "oriLinkTestInProgress": oriLinkTestInProgress,
       "oriLinkTestStationName": oriLinkTestStationName,
       "oriLinkTestMACAddress": oriLinkTestMACAddress,
       "oriLinkTestStationProfile": oriLinkTestStationProfile,
       "oriLinkTestOurCurSignalLevel": oriLinkTestOurCurSignalLevel,
       "oriLinkTestOurCurNoiseLevel": oriLinkTestOurCurNoiseLevel,
       "oriLinkTestOurCurSNR": oriLinkTestOurCurSNR,
       "oriLinkTestOurMinSignalLevel": oriLinkTestOurMinSignalLevel,
       "oriLinkTestOurMinNoiseLevel": oriLinkTestOurMinNoiseLevel,
       "oriLinkTestOurMinSNR": oriLinkTestOurMinSNR,
       "oriLinkTestOurMaxSignalLevel": oriLinkTestOurMaxSignalLevel,
       "oriLinkTestOurMaxNoiseLevel": oriLinkTestOurMaxNoiseLevel,
       "oriLinkTestOurMaxSNR": oriLinkTestOurMaxSNR,
       "oriLinkTestOurLowFrameCount": oriLinkTestOurLowFrameCount,
       "oriLinkTestOurStandardFrameCount": oriLinkTestOurStandardFrameCount,
       "oriLinkTestOurMediumFrameCount": oriLinkTestOurMediumFrameCount,
       "oriLinkTestOurHighFrameCount": oriLinkTestOurHighFrameCount,
       "oriLinkTestHisCurSignalLevel": oriLinkTestHisCurSignalLevel,
       "oriLinkTestHisCurNoiseLevel": oriLinkTestHisCurNoiseLevel,
       "oriLinkTestHisCurSNR": oriLinkTestHisCurSNR,
       "oriLinkTestHisMinSignalLevel": oriLinkTestHisMinSignalLevel,
       "oriLinkTestHisMinNoiseLevel": oriLinkTestHisMinNoiseLevel,
       "oriLinkTestHisMinSNR": oriLinkTestHisMinSNR,
       "oriLinkTestHisMaxSignalLevel": oriLinkTestHisMaxSignalLevel,
       "oriLinkTestHisMaxNoiseLevel": oriLinkTestHisMaxNoiseLevel,
       "oriLinkTestHisMaxSNR": oriLinkTestHisMaxSNR,
       "oriLinkTestHisLowFrameCount": oriLinkTestHisLowFrameCount,
       "oriLinkTestHisStandardFrameCount": oriLinkTestHisStandardFrameCount,
       "oriLinkTestHisMediumFrameCount": oriLinkTestHisMediumFrameCount,
       "oriLinkTestHisHighFrameCount": oriLinkTestHisHighFrameCount,
       "oriLinkTestInterface": oriLinkTestInterface,
       "oriLinkTestRadioType": oriLinkTestRadioType,
       "accessServerTraps": accessServerTraps,
       "accessServerTrapVariables": accessServerTrapVariables,
       "accessServerGenericInformationMessage": accessServerGenericInformationMessage,
       "accessServerMacAddress": accessServerMacAddress,
       "accessServerFailedTFTPServerAddress": accessServerFailedTFTPServerAddress,
       "accessServerFailedTFTPFilename": accessServerFailedTFTPFilename,
       "accessServerFailedTFTPOperation": accessServerFailedTFTPOperation,
       "accessServerSuspendedTaskName": accessServerSuspendedTaskName,
       "accessServerWirelessCard": accessServerWirelessCard,
       "accessServerFlashRelatedTraps": accessServerFlashRelatedTraps,
       "accessServerFlashEmpty": accessServerFlashEmpty,
       "accessServerFlashCorrupted": accessServerFlashCorrupted,
       "accessServerConfigurationRelatedTraps": accessServerConfigurationRelatedTraps,
       "accessServerInvalidKey": accessServerInvalidKey,
       "accessServerAPMNotConfigured": accessServerAPMNotConfigured,
       "accessServerWLCIncompatibleFirmware": accessServerWLCIncompatibleFirmware,
       "accessServerWLCFailure": accessServerWLCFailure,
       "accessServerWLCRemoval": accessServerWLCRemoval,
       "accessServerRadiusNotConfigured": accessServerRadiusNotConfigured,
       "accessServerDNSIPNotConfigured": accessServerDNSIPNotConfigured,
       "accessServerNBNSIPNotConfigured": accessServerNBNSIPNotConfigured,
       "accessServerRadiusAuthenticationNotConfigured": accessServerRadiusAuthenticationNotConfigured,
       "accessServerRadiusAccountingNotConfigured": accessServerRadiusAccountingNotConfigured,
       "accessServerDuplicateIPAddressEncountered": accessServerDuplicateIPAddressEncountered,
       "accessServerWLCVoltageDiscrepancy": accessServerWLCVoltageDiscrepancy,
       "accessServerWLCIncompatibleVendor": accessServerWLCIncompatibleVendor,
       "accessServerWLCFirmwareDownloadFailure": accessServerWLCFirmwareDownloadFailure,
       "accessServerDiagnosticTraps": accessServerDiagnosticTraps,
       "accessServerTFTPInitiated": accessServerTFTPInitiated,
       "accessServerTFTPCompleted": accessServerTFTPCompleted,
       "accessServerTFTPFailure": accessServerTFTPFailure,
       "accessServerAdminStateMadeUp": accessServerAdminStateMadeUp,
       "accessServerAdminStateMadeDown": accessServerAdminStateMadeDown,
       "accessServerRebootingNow": accessServerRebootingNow,
       "accessServerTaskSuspended": accessServerTaskSuspended,
       "accessServerBootPFailed": accessServerBootPFailed,
       "accessServerDHCPFailed": accessServerDHCPFailed,
       "accessServerImageTraps": accessServerImageTraps,
       "accessServerZeroSizeImage": accessServerZeroSizeImage,
       "accessServerNonVxWorksImage": accessServerNonVxWorksImage,
       "accessServerImageTooLarge": accessServerImageTooLarge}
)
