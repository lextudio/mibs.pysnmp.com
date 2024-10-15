# SNMP MIB module (PUBLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PUBLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:00 2024
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
 iso,
 mgmt,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt",
    "private")

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
_Lucent_MIB_ObjectIdentity = ObjectIdentity
lucent_MIB = _Lucent_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_Publan_ObjectIdentity = ObjectIdentity
publan = _Publan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51)
)
_PubStation_ObjectIdentity = ObjectIdentity
pubStation = _PubStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 1)
)
_PubClient_ObjectIdentity = ObjectIdentity
pubClient = _PubClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 2)
)
_PublanInterface_ObjectIdentity = ObjectIdentity
publanInterface = _PublanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3)
)
_PublanPHY_ObjectIdentity = ObjectIdentity
publanPHY = _PublanPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2)
)
_PliSystemName_Type = DisplayString
_PliSystemName_Object = MibScalar
pliSystemName = _PliSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 1),
    _PliSystemName_Type()
)
pliSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliSystemName.setStatus("mandatory")
_PliNetworkName_Type = DisplayString
_PliNetworkName_Object = MibScalar
pliNetworkName = _PliNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 2),
    _PliNetworkName_Type()
)
pliNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliNetworkName.setStatus("mandatory")
_PliMACAddress_Type = PhysAddress
_PliMACAddress_Object = MibScalar
pliMACAddress = _PliMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 3),
    _PliMACAddress_Type()
)
pliMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliMACAddress.setStatus("mandatory")


class _PliMediumReservation_Type(Integer32):
    """Custom type pliMediumReservation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_PliMediumReservation_Type.__name__ = "Integer32"
_PliMediumReservation_Object = MibScalar
pliMediumReservation = _PliMediumReservation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 4),
    _PliMediumReservation_Type()
)
pliMediumReservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliMediumReservation.setStatus("mandatory")


class _PliTransmitRate_Type(Integer32):
    """Custom type pliTransmitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PliTransmitRate_Type.__name__ = "Integer32"
_PliTransmitRate_Object = MibScalar
pliTransmitRate = _PliTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 5),
    _PliTransmitRate_Type()
)
pliTransmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliTransmitRate.setStatus("mandatory")


class _PliOperatingFrequency_Type(Integer32):
    """Custom type pliOperatingFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_PliOperatingFrequency_Type.__name__ = "Integer32"
_PliOperatingFrequency_Object = MibScalar
pliOperatingFrequency = _PliOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 6),
    _PliOperatingFrequency_Type()
)
pliOperatingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliOperatingFrequency.setStatus("mandatory")


class _PliAPDensity_Type(Integer32):
    """Custom type pliAPDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PliAPDensity_Type.__name__ = "Integer32"
_PliAPDensity_Object = MibScalar
pliAPDensity = _PliAPDensity_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 7),
    _PliAPDensity_Type()
)
pliAPDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pliAPDensity.setStatus("mandatory")


class _PliClosedSystem_Type(Integer32):
    """Custom type pliClosedSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PliClosedSystem_Type.__name__ = "Integer32"
_PliClosedSystem_Object = MibScalar
pliClosedSystem = _PliClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 8),
    _PliClosedSystem_Type()
)
pliClosedSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliClosedSystem.setStatus("mandatory")
_PliAllowedDataRates_Type = Integer32
_PliAllowedDataRates_Object = MibScalar
pliAllowedDataRates = _PliAllowedDataRates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 9),
    _PliAllowedDataRates_Type()
)
pliAllowedDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliAllowedDataRates.setStatus("mandatory")
_PublanDriver_ObjectIdentity = ObjectIdentity
publanDriver = _PublanDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4)
)
_PliDriverName_Type = DisplayString
_PliDriverName_Object = MibScalar
pliDriverName = _PliDriverName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4, 1),
    _PliDriverName_Type()
)
pliDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliDriverName.setStatus("mandatory")
_PliDriverVersion_Type = DisplayString
_PliDriverVersion_Object = MibScalar
pliDriverVersion = _PliDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4, 2),
    _PliDriverVersion_Type()
)
pliDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pliDriverVersion.setStatus("mandatory")
_PublanSNMPSetup_ObjectIdentity = ObjectIdentity
publanSNMPSetup = _PublanSNMPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4)
)
_PsSNMPReadPassword_Type = DisplayString
_PsSNMPReadPassword_Object = MibScalar
psSNMPReadPassword = _PsSNMPReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 1),
    _PsSNMPReadPassword_Type()
)
psSNMPReadPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psSNMPReadPassword.setStatus("mandatory")
_PsSNMPReadWritePassword_Type = DisplayString
_PsSNMPReadWritePassword_Object = MibScalar
psSNMPReadWritePassword = _PsSNMPReadWritePassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 2),
    _PsSNMPReadWritePassword_Type()
)
psSNMPReadWritePassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psSNMPReadWritePassword.setStatus("mandatory")
_PsSNMPTrapHostIPAddress_Type = IpAddress
_PsSNMPTrapHostIPAddress_Object = MibScalar
psSNMPTrapHostIPAddress = _PsSNMPTrapHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 3),
    _PsSNMPTrapHostIPAddress_Type()
)
psSNMPTrapHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSNMPTrapHostIPAddress.setStatus("mandatory")
_PsSNMPTrapHostPassword_Type = DisplayString
_PsSNMPTrapHostPassword_Object = MibScalar
psSNMPTrapHostPassword = _PsSNMPTrapHostPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 4),
    _PsSNMPTrapHostPassword_Type()
)
psSNMPTrapHostPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSNMPTrapHostPassword.setStatus("mandatory")
_PsSNMPManagerCount_Type = Integer32
_PsSNMPManagerCount_Object = MibScalar
psSNMPManagerCount = _PsSNMPManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 5),
    _PsSNMPManagerCount_Type()
)
psSNMPManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSNMPManagerCount.setStatus("mandatory")
_PsSNMPAccessTable_Object = MibTable
psSNMPAccessTable = _PsSNMPAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6)
)
if mibBuilder.loadTexts:
    psSNMPAccessTable.setStatus("mandatory")
_PsSNMPAccessTableEntry_Object = MibTableRow
psSNMPAccessTableEntry = _PsSNMPAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1)
)
psSNMPAccessTableEntry.setIndexNames(
    (0, "PUBLAN-MIB", "psSNMPManagerIndex"),
)
if mibBuilder.loadTexts:
    psSNMPAccessTableEntry.setStatus("mandatory")
_Index_Type = Integer32
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 1),
    _Index_Type()
)
index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    index.setStatus("mandatory")
_ManagerIPAddress_Type = IpAddress
_ManagerIPAddress_Object = MibTableColumn
managerIPAddress = _ManagerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 2),
    _ManagerIPAddress_Type()
)
managerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPAddress.setStatus("mandatory")
_ManagerIPMask_Type = IpAddress
_ManagerIPMask_Object = MibTableColumn
managerIPMask = _ManagerIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 3),
    _ManagerIPMask_Type()
)
managerIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPMask.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 4),
    _ManagerStatus_Type()
)
managerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerStatus.setStatus("mandatory")
_PsSNMPInBadManagers_Type = Counter32
_PsSNMPInBadManagers_Object = MibScalar
psSNMPInBadManagers = _PsSNMPInBadManagers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 7),
    _PsSNMPInBadManagers_Type()
)
psSNMPInBadManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSNMPInBadManagers.setStatus("mandatory")
_PublanPPPSetup_ObjectIdentity = ObjectIdentity
publanPPPSetup = _PublanPPPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5)
)


class _PsPPPIPAddressAssignmentType_Type(Integer32):
    """Custom type psPPPIPAddressAssignmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PsPPPIPAddressAssignmentType_Type.__name__ = "Integer32"
_PsPPPIPAddressAssignmentType_Object = MibScalar
psPPPIPAddressAssignmentType = _PsPPPIPAddressAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 1),
    _PsPPPIPAddressAssignmentType_Type()
)
psPPPIPAddressAssignmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPIPAddressAssignmentType.setStatus("mandatory")
_PsPPPStartIPAddress_Type = IpAddress
_PsPPPStartIPAddress_Object = MibScalar
psPPPStartIPAddress = _PsPPPStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 2),
    _PsPPPStartIPAddress_Type()
)
psPPPStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPStartIPAddress.setStatus("mandatory")
_PsPPPEndIPAddress_Type = IpAddress
_PsPPPEndIPAddress_Object = MibScalar
psPPPEndIPAddress = _PsPPPEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 3),
    _PsPPPEndIPAddress_Type()
)
psPPPEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPEndIPAddress.setStatus("mandatory")
_PsPPPNoOfMACIPMappingEntries_Type = Integer32
_PsPPPNoOfMACIPMappingEntries_Object = MibScalar
psPPPNoOfMACIPMappingEntries = _PsPPPNoOfMACIPMappingEntries_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 4),
    _PsPPPNoOfMACIPMappingEntries_Type()
)
psPPPNoOfMACIPMappingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPPPNoOfMACIPMappingEntries.setStatus("mandatory")
_PsPPPMACIPMappingTable_Object = MibTable
psPPPMACIPMappingTable = _PsPPPMACIPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5)
)
if mibBuilder.loadTexts:
    psPPPMACIPMappingTable.setStatus("mandatory")
_PsPPPMACIPMappingTableEntry_Object = MibTableRow
psPPPMACIPMappingTableEntry = _PsPPPMACIPMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1)
)
psPPPMACIPMappingTableEntry.setIndexNames(
    (0, "PUBLAN-MIB", "psPPPMACIPTableIndex"),
)
if mibBuilder.loadTexts:
    psPPPMACIPMappingTableEntry.setStatus("mandatory")
_Index3_Type = Integer32
_Index3_Object = MibScalar
index3 = _Index3_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 1),
    _Index3_Type()
)
index3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    index3.setStatus("mandatory")
_Macaddress_Type = PhysAddress
_Macaddress_Object = MibTableColumn
macaddress = _Macaddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 2),
    _Macaddress_Type()
)
macaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaddress.setStatus("mandatory")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("mandatory")
_Comment_Type = DisplayString
_Comment_Object = MibTableColumn
comment = _Comment_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 4),
    _Comment_Type()
)
comment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comment.setStatus("mandatory")


class _Entrystatus_Type(Integer32):
    """Custom type entrystatus based on Integer32"""
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


_Entrystatus_Type.__name__ = "Integer32"
_Entrystatus_Object = MibTableColumn
entrystatus = _Entrystatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 5),
    _Entrystatus_Type()
)
entrystatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entrystatus.setStatus("mandatory")
_PsPPPKeepAliveInterval_Type = Integer32
_PsPPPKeepAliveInterval_Object = MibScalar
psPPPKeepAliveInterval = _PsPPPKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 6),
    _PsPPPKeepAliveInterval_Type()
)
psPPPKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPKeepAliveInterval.setStatus("mandatory")
_PsPPPNoOfKeepAliveTimeouts_Type = Integer32
_PsPPPNoOfKeepAliveTimeouts_Object = MibScalar
psPPPNoOfKeepAliveTimeouts = _PsPPPNoOfKeepAliveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 7),
    _PsPPPNoOfKeepAliveTimeouts_Type()
)
psPPPNoOfKeepAliveTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPNoOfKeepAliveTimeouts.setStatus("mandatory")
_PsPPPDNSIPAddress_Type = IpAddress
_PsPPPDNSIPAddress_Object = MibScalar
psPPPDNSIPAddress = _PsPPPDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 8),
    _PsPPPDNSIPAddress_Type()
)
psPPPDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPPPDNSIPAddress.setStatus("mandatory")
_PsPPPIPRangeTable_Object = MibTable
psPPPIPRangeTable = _PsPPPIPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20)
)
if mibBuilder.loadTexts:
    psPPPIPRangeTable.setStatus("mandatory")
_PsPPPIPRangeTableEntry_Object = MibTableRow
psPPPIPRangeTableEntry = _PsPPPIPRangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1)
)
psPPPIPRangeTableEntry.setIndexNames(
    (0, "PUBLAN-MIB", "psPPPIPRangeTableIndex"),
)
if mibBuilder.loadTexts:
    psPPPIPRangeTableEntry.setStatus("mandatory")
_PsPPPIPRangeTableIndex_Type = Integer32
_PsPPPIPRangeTableIndex_Object = MibTableColumn
psPPPIPRangeTableIndex = _PsPPPIPRangeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 1),
    _PsPPPIPRangeTableIndex_Type()
)
psPPPIPRangeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psPPPIPRangeTableIndex.setStatus("mandatory")
_PoolStartIPAddress_Type = IpAddress
_PoolStartIPAddress_Object = MibTableColumn
poolStartIPAddress = _PoolStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 2),
    _PoolStartIPAddress_Type()
)
poolStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolStartIPAddress.setStatus("mandatory")
_PoolEndIPAddress_Type = IpAddress
_PoolEndIPAddress_Object = MibTableColumn
poolEndIPAddress = _PoolEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 3),
    _PoolEndIPAddress_Type()
)
poolEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolEndIPAddress.setStatus("mandatory")
_NumOfIPAddresss_Type = Integer32
_NumOfIPAddresss_Object = MibTableColumn
numOfIPAddresss = _NumOfIPAddresss_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 4),
    _NumOfIPAddresss_Type()
)
numOfIPAddresss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numOfIPAddresss.setStatus("mandatory")


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
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 5),
    _Status_Type()
)
status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_Comments_Type = DisplayString
_Comments_Object = MibScalar
comments = _Comments_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 6),
    _Comments_Type()
)
comments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comments.setStatus("mandatory")
_PublanAgent_ObjectIdentity = ObjectIdentity
publanAgent = _PublanAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6)
)
_PsVersion_Type = DisplayString
_PsVersion_Object = MibScalar
psVersion = _PsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 1),
    _PsVersion_Type()
)
psVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVersion.setStatus("mandatory")
_PsIPAddress_Type = IpAddress
_PsIPAddress_Object = MibScalar
psIPAddress = _PsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 2),
    _PsIPAddress_Type()
)
psIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIPAddress.setStatus("mandatory")
_PsSubnetMask_Type = IpAddress
_PsSubnetMask_Object = MibScalar
psSubnetMask = _PsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 3),
    _PsSubnetMask_Type()
)
psSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psSubnetMask.setStatus("mandatory")
_PsDefaultGateway_Type = IpAddress
_PsDefaultGateway_Object = MibScalar
psDefaultGateway = _PsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 4),
    _PsDefaultGateway_Type()
)
psDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psDefaultGateway.setStatus("mandatory")


class _PsIPAddressType_Type(Integer32):
    """Custom type psIPAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsIPAddressType_Type.__name__ = "Integer32"
_PsIPAddressType_Object = MibScalar
psIPAddressType = _PsIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 5),
    _PsIPAddressType_Type()
)
psIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psIPAddressType.setStatus("mandatory")


class _PsAdministrativeState_Type(Integer32):
    """Custom type psAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsAdministrativeState_Type.__name__ = "Integer32"
_PsAdministrativeState_Object = MibScalar
psAdministrativeState = _PsAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 6),
    _PsAdministrativeState_Type()
)
psAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psAdministrativeState.setStatus("mandatory")
_PsTFTPIPAddress_Type = IpAddress
_PsTFTPIPAddress_Object = MibScalar
psTFTPIPAddress = _PsTFTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 7),
    _PsTFTPIPAddress_Type()
)
psTFTPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTFTPIPAddress.setStatus("mandatory")
_PsTFTPFilename_Type = DisplayString
_PsTFTPFilename_Object = MibScalar
psTFTPFilename = _PsTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 8),
    _PsTFTPFilename_Type()
)
psTFTPFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psTFTPFilename.setStatus("mandatory")


class _PsTFTPOperation_Type(Integer32):
    """Custom type psTFTPOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsTFTPOperation_Type.__name__ = "Integer32"
_PsTFTPOperation_Object = MibScalar
psTFTPOperation = _PsTFTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 9),
    _PsTFTPOperation_Type()
)
psTFTPOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psTFTPOperation.setStatus("mandatory")
_PsReboot_Type = Integer32
_PsReboot_Object = MibScalar
psReboot = _PsReboot_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 10),
    _PsReboot_Type()
)
psReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    psReboot.setStatus("mandatory")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7)
)
_RadiusClientMIB_ObjectIdentity = ObjectIdentity
radiusClientMIB = _RadiusClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2)
)
_RadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
radiusClientMIBObjects = _RadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1)
)
_RadiusClient_ObjectIdentity = ObjectIdentity
radiusClient = _RadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1)
)
_RadiusClientInvalidServerAddresses_Type = Counter32
_RadiusClientInvalidServerAddresses_Object = MibScalar
radiusClientInvalidServerAddresses = _RadiusClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 1),
    _RadiusClientInvalidServerAddresses_Type()
)
radiusClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusClientInvalidServerAddresses.setStatus("mandatory")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("mandatory")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1)
)
radiusServerEntry.setIndexNames(
    (0, "PUBLAN-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("mandatory")
_Index4_Type = Integer32
_Index4_Object = MibScalar
index4 = _Index4_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 1),
    _Index4_Type()
)
index4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    index4.setStatus("mandatory")


class _Type_Type(Integer32):
    """Custom type type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acct", 2),
          ("auth", 1),
          ("auth-and-acct", 3))
    )


_Type_Type.__name__ = "Integer32"
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 2),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("mandatory")
_ServerIPAddress_Type = IpAddress
_ServerIPAddress_Object = MibTableColumn
serverIPAddress = _ServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 3),
    _ServerIPAddress_Type()
)
serverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIPAddress.setStatus("mandatory")
_DestPortAuth_Type = Integer32
_DestPortAuth_Object = MibTableColumn
destPortAuth = _DestPortAuth_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 4),
    _DestPortAuth_Type()
)
destPortAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destPortAuth.setStatus("mandatory")
_DestPortAcct_Type = Integer32
_DestPortAcct_Object = MibTableColumn
destPortAcct = _DestPortAcct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 5),
    _DestPortAcct_Type()
)
destPortAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destPortAcct.setStatus("mandatory")
_AccessRequests_Type = Counter32
_AccessRequests_Object = MibTableColumn
accessRequests = _AccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 6),
    _AccessRequests_Type()
)
accessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessRequests.setStatus("mandatory")
_AccessRetransmissions_Type = Counter32
_AccessRetransmissions_Object = MibTableColumn
accessRetransmissions = _AccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 7),
    _AccessRetransmissions_Type()
)
accessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessRetransmissions.setStatus("mandatory")
_AccessAccepts_Type = Counter32
_AccessAccepts_Object = MibTableColumn
accessAccepts = _AccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 8),
    _AccessAccepts_Type()
)
accessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessAccepts.setStatus("mandatory")
_AccessChallenges_Type = Counter32
_AccessChallenges_Object = MibTableColumn
accessChallenges = _AccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 9),
    _AccessChallenges_Type()
)
accessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessChallenges.setStatus("mandatory")
_MalformedAccessResponses_Type = Counter32
_MalformedAccessResponses_Object = MibTableColumn
malformedAccessResponses = _MalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 10),
    _MalformedAccessResponses_Type()
)
malformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    malformedAccessResponses.setStatus("mandatory")
_AuthenticationBadAuthenticators_Type = Counter32
_AuthenticationBadAuthenticators_Object = MibTableColumn
authenticationBadAuthenticators = _AuthenticationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 11),
    _AuthenticationBadAuthenticators_Type()
)
authenticationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationBadAuthenticators.setStatus("mandatory")
_AccessRejects_Type = Counter32
_AccessRejects_Object = MibTableColumn
accessRejects = _AccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 12),
    _AccessRejects_Type()
)
accessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessRejects.setStatus("mandatory")
_Timeouts_Type = Counter32
_Timeouts_Object = MibTableColumn
timeouts = _Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 13),
    _Timeouts_Type()
)
timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeouts.setStatus("mandatory")
_AccountingRequests_Type = Counter32
_AccountingRequests_Object = MibTableColumn
accountingRequests = _AccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 14),
    _AccountingRequests_Type()
)
accountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingRequests.setStatus("mandatory")
_AccountingRetransmissions_Type = Counter32
_AccountingRetransmissions_Object = MibTableColumn
accountingRetransmissions = _AccountingRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 15),
    _AccountingRetransmissions_Type()
)
accountingRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingRetransmissions.setStatus("mandatory")
_AccountingResponses_Type = Counter32
_AccountingResponses_Object = MibTableColumn
accountingResponses = _AccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 16),
    _AccountingResponses_Type()
)
accountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingResponses.setStatus("mandatory")
_AccountingBadAuthenticators_Type = Counter32
_AccountingBadAuthenticators_Object = MibTableColumn
accountingBadAuthenticators = _AccountingBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 17),
    _AccountingBadAuthenticators_Type()
)
accountingBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingBadAuthenticators.setStatus("mandatory")
_SharedSecret_Type = DisplayString
_SharedSecret_Object = MibTableColumn
sharedSecret = _SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 18),
    _SharedSecret_Type()
)
sharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedSecret.setStatus("mandatory")


class _Enabled_Type(Integer32):
    """Custom type enabled based on Integer32"""
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
          ("enable", 1))
    )


_Enabled_Type.__name__ = "Integer32"
_Enabled_Object = MibTableColumn
enabled = _Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 19),
    _Enabled_Type()
)
enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabled.setStatus("mandatory")


class _ResponseTime_Type(Integer32):
    """Custom type responseTime based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight-secs", 8),
          ("five-secs", 5),
          ("four-secs", 4),
          ("nine-secs", 9),
          ("one-sec", 1),
          ("seven-secs", 7),
          ("six-secs", 6),
          ("ten-secs", 10),
          ("three-secs", 3),
          ("two-secs", 2))
    )


_ResponseTime_Type.__name__ = "Integer32"
_ResponseTime_Object = MibTableColumn
responseTime = _ResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 20),
    _ResponseTime_Type()
)
responseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    responseTime.setStatus("mandatory")


class _MaximumRetransmission_Type(Integer32):
    """Custom type maximumRetransmission based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_MaximumRetransmission_Type.__name__ = "Integer32"
_MaximumRetransmission_Object = MibTableColumn
maximumRetransmission = _MaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 21),
    _MaximumRetransmission_Type()
)
maximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maximumRetransmission.setStatus("mandatory")
_RadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
radiusClientMIBConformance = _RadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2)
)
_RadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
radiusClientMIBCompliances = _RadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2, 1)
)
_RadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
radiusClientMIBGroups = _RadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2, 2)
)
_PublanShimECPSetup_ObjectIdentity = ObjectIdentity
publanShimECPSetup = _PublanShimECPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 8)
)
_PsShimECPRetransmissionCount_Type = Integer32
_PsShimECPRetransmissionCount_Object = MibScalar
psShimECPRetransmissionCount = _PsShimECPRetransmissionCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 1),
    _PsShimECPRetransmissionCount_Type()
)
psShimECPRetransmissionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRetransmissionCount.setStatus("mandatory")
_PsShimECPRepeatResponseCount_Type = Integer32
_PsShimECPRepeatResponseCount_Object = MibScalar
psShimECPRepeatResponseCount = _PsShimECPRepeatResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 2),
    _PsShimECPRepeatResponseCount_Type()
)
psShimECPRepeatResponseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRepeatResponseCount.setStatus("mandatory")
_PsShimECPRetransmissionTimeout_Type = Integer32
_PsShimECPRetransmissionTimeout_Object = MibScalar
psShimECPRetransmissionTimeout = _PsShimECPRetransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 3),
    _PsShimECPRetransmissionTimeout_Type()
)
psShimECPRetransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShimECPRetransmissionTimeout.setStatus("mandatory")
_PubStationTraps_ObjectIdentity = ObjectIdentity
pubStationTraps = _PubStationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15)
)
_PubStationTrapVariables_ObjectIdentity = ObjectIdentity
pubStationTrapVariables = _PubStationTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 1)
)
_PubStationMacAddress_Type = PhysAddress
_PubStationMacAddress_Object = MibScalar
pubStationMacAddress = _PubStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 1, 1),
    _PubStationMacAddress_Type()
)
pubStationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pubStationMacAddress.setStatus("mandatory")
_PubStationFlashRelatedTraps_ObjectIdentity = ObjectIdentity
pubStationFlashRelatedTraps = _PubStationFlashRelatedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2)
)
_PubStationConfigurationRelatedTraps_ObjectIdentity = ObjectIdentity
pubStationConfigurationRelatedTraps = _PubStationConfigurationRelatedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3)
)

# Managed Objects groups


# Notification objects

pubStationFlashNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2, 0, 1)
)
if mibBuilder.loadTexts:
    pubStationFlashNotPresent.setStatus(
        ""
    )

pubStationFlashEmpty = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pubStationFlashEmpty.setStatus(
        ""
    )

pubStationFlashCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2, 0, 3)
)
if mibBuilder.loadTexts:
    pubStationFlashCorrupted.setStatus(
        ""
    )

pubStationInvalidKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3, 0, 1)
)
if mibBuilder.loadTexts:
    pubStationInvalidKey.setStatus(
        ""
    )

pubStationAPMNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3, 0, 2)
)
if mibBuilder.loadTexts:
    pubStationAPMNotConfigured.setStatus(
        ""
    )

pubStationIncompatibleWavelanCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3, 0, 3)
)
if mibBuilder.loadTexts:
    pubStationIncompatibleWavelanCard.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PUBLAN-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "lucent": lucent,
       "lucent-MIB": lucent_MIB,
       "publan": publan,
       "pubStation": pubStation,
       "pubClient": pubClient,
       "publanInterface": publanInterface,
       "publanPHY": publanPHY,
       "pliSystemName": pliSystemName,
       "pliNetworkName": pliNetworkName,
       "pliMACAddress": pliMACAddress,
       "pliMediumReservation": pliMediumReservation,
       "pliTransmitRate": pliTransmitRate,
       "pliOperatingFrequency": pliOperatingFrequency,
       "pliAPDensity": pliAPDensity,
       "pliClosedSystem": pliClosedSystem,
       "pliAllowedDataRates": pliAllowedDataRates,
       "publanDriver": publanDriver,
       "pliDriverName": pliDriverName,
       "pliDriverVersion": pliDriverVersion,
       "publanSNMPSetup": publanSNMPSetup,
       "psSNMPReadPassword": psSNMPReadPassword,
       "psSNMPReadWritePassword": psSNMPReadWritePassword,
       "psSNMPTrapHostIPAddress": psSNMPTrapHostIPAddress,
       "psSNMPTrapHostPassword": psSNMPTrapHostPassword,
       "psSNMPManagerCount": psSNMPManagerCount,
       "psSNMPAccessTable": psSNMPAccessTable,
       "psSNMPAccessTableEntry": psSNMPAccessTableEntry,
       "index": index,
       "managerIPAddress": managerIPAddress,
       "managerIPMask": managerIPMask,
       "managerStatus": managerStatus,
       "psSNMPInBadManagers": psSNMPInBadManagers,
       "publanPPPSetup": publanPPPSetup,
       "psPPPIPAddressAssignmentType": psPPPIPAddressAssignmentType,
       "psPPPStartIPAddress": psPPPStartIPAddress,
       "psPPPEndIPAddress": psPPPEndIPAddress,
       "psPPPNoOfMACIPMappingEntries": psPPPNoOfMACIPMappingEntries,
       "psPPPMACIPMappingTable": psPPPMACIPMappingTable,
       "psPPPMACIPMappingTableEntry": psPPPMACIPMappingTableEntry,
       "index3": index3,
       "macaddress": macaddress,
       "ipAddress": ipAddress,
       "comment": comment,
       "entrystatus": entrystatus,
       "psPPPKeepAliveInterval": psPPPKeepAliveInterval,
       "psPPPNoOfKeepAliveTimeouts": psPPPNoOfKeepAliveTimeouts,
       "psPPPDNSIPAddress": psPPPDNSIPAddress,
       "psPPPIPRangeTable": psPPPIPRangeTable,
       "psPPPIPRangeTableEntry": psPPPIPRangeTableEntry,
       "psPPPIPRangeTableIndex": psPPPIPRangeTableIndex,
       "poolStartIPAddress": poolStartIPAddress,
       "poolEndIPAddress": poolEndIPAddress,
       "numOfIPAddresss": numOfIPAddresss,
       "status": status,
       "comments": comments,
       "publanAgent": publanAgent,
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
       "radius": radius,
       "radiusClientMIB": radiusClientMIB,
       "radiusClientMIBObjects": radiusClientMIBObjects,
       "radiusClient": radiusClient,
       "radiusClientInvalidServerAddresses": radiusClientInvalidServerAddresses,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "index4": index4,
       "type": type,
       "serverIPAddress": serverIPAddress,
       "destPortAuth": destPortAuth,
       "destPortAcct": destPortAcct,
       "accessRequests": accessRequests,
       "accessRetransmissions": accessRetransmissions,
       "accessAccepts": accessAccepts,
       "accessChallenges": accessChallenges,
       "malformedAccessResponses": malformedAccessResponses,
       "authenticationBadAuthenticators": authenticationBadAuthenticators,
       "accessRejects": accessRejects,
       "timeouts": timeouts,
       "accountingRequests": accountingRequests,
       "accountingRetransmissions": accountingRetransmissions,
       "accountingResponses": accountingResponses,
       "accountingBadAuthenticators": accountingBadAuthenticators,
       "sharedSecret": sharedSecret,
       "enabled": enabled,
       "responseTime": responseTime,
       "maximumRetransmission": maximumRetransmission,
       "radiusClientMIBConformance": radiusClientMIBConformance,
       "radiusClientMIBCompliances": radiusClientMIBCompliances,
       "radiusClientMIBGroups": radiusClientMIBGroups,
       "publanShimECPSetup": publanShimECPSetup,
       "psShimECPRetransmissionCount": psShimECPRetransmissionCount,
       "psShimECPRepeatResponseCount": psShimECPRepeatResponseCount,
       "psShimECPRetransmissionTimeout": psShimECPRetransmissionTimeout,
       "pubStationTraps": pubStationTraps,
       "pubStationTrapVariables": pubStationTrapVariables,
       "pubStationMacAddress": pubStationMacAddress,
       "pubStationFlashRelatedTraps": pubStationFlashRelatedTraps,
       "pubStationFlashNotPresent": pubStationFlashNotPresent,
       "pubStationFlashEmpty": pubStationFlashEmpty,
       "pubStationFlashCorrupted": pubStationFlashCorrupted,
       "pubStationConfigurationRelatedTraps": pubStationConfigurationRelatedTraps,
       "pubStationInvalidKey": pubStationInvalidKey,
       "pubStationAPMNotConfigured": pubStationAPMNotConfigured,
       "pubStationIncompatibleWavelanCard": pubStationIncompatibleWavelanCard}
)
