# SNMP MIB module (ADIC-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADIC-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:47 2024
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

(AdicAgentStatus,
 AdicComponentType,
 AdicDateAndTime,
 AdicDoorStatus,
 AdicEnable,
 AdicInterfaceType,
 AdicMibVersion,
 AdicOnlineStatus,
 AdicREDIdentifier,
 RowStatus,
 componentId,
 hardware,
 trapIntendedUsage,
 trapSequenceNumber,
 trapSeverity,
 trapSummaryText) = mibBuilder.importSymbols(
    "ADIC-INTELLIGENT-STORAGE-MIB",
    "AdicAgentStatus",
    "AdicComponentType",
    "AdicDateAndTime",
    "AdicDoorStatus",
    "AdicEnable",
    "AdicInterfaceType",
    "AdicMibVersion",
    "AdicOnlineStatus",
    "AdicREDIdentifier",
    "RowStatus",
    "componentId",
    "hardware",
    "trapIntendedUsage",
    "trapSequenceNumber",
    "trapSeverity",
    "trapSummaryText")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class AdicEthernetSpeed(Integer32):
    """Custom type AdicEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baseT10", 1),
          ("baseT100", 2))
    )





class AdicBarCode(DisplayString):
    """Custom type AdicBarCode based on DisplayString"""




class AdicSegmentType(Integer32):
    """Custom type AdicSegmentType based on Integer32"""
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
        *(("drive", 4),
          ("gripper", 1),
          ("ie", 3),
          ("storage", 2))
    )





class AdicInstallStatus(Integer32):
    """Custom type AdicInstallStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 2),
          ("ok", 1),
          ("updateAborted", 4))
    )





class AdicFcPortType(Integer32):
    """Custom type AdicFcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("nPort", 2),
          ("nlPort", 3))
    )





class AdicFcPortSpeed(Integer32):
    """Custom type AdicFcPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1000,
              2000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("megabits1000", 1000),
          ("megabits2000", 2000))
    )





class AdicStatusGroup(Integer32):
    """Custom type AdicStatusGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 99),
          ("connectivity", 1),
          ("control", 2),
          ("cooling", 3),
          ("drivesAndMedia", 4),
          ("power", 5),
          ("robotics", 6))
    )





class AdicStatusGroupState(Integer32):
    """Custom type AdicStatusGroupState based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 2),
          ("good", 1),
          ("informational", 5),
          ("invalid", 7),
          ("unknown", 6),
          ("warning", 4))
    )





class AdicRasTicketState(Integer32):
    """Custom type AdicRasTicketState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 99),
          ("closed", 4),
          ("new", 1),
          ("open", 2),
          ("suspended", 3),
          ("verified", 5))
    )





class AdicFruSerialNumber(DisplayString):
    """Custom type AdicFruSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )





class AdicRasTicketSeverity(Integer32):
    """Custom type AdicRasTicketSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20)
)
_GlobalStatus_ObjectIdentity = ObjectIdentity
globalStatus = _GlobalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10)
)
_GlobalStatusTable_Object = MibTable
globalStatusTable = _GlobalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10)
)
if mibBuilder.loadTexts:
    globalStatusTable.setStatus("mandatory")
_GlobalStatusEntry_Object = MibTableRow
globalStatusEntry = _GlobalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1)
)
globalStatusEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    globalStatusEntry.setStatus("mandatory")


class _Role_Type(Integer32):
    """Custom type role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_Role_Type.__name__ = "Integer32"
_Role_Object = MibTableColumn
role = _Role_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 1),
    _Role_Type()
)
role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    role.setStatus("mandatory")
_Status_Type = AdicAgentStatus
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 2),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_SystemDateAndTime_Type = AdicDateAndTime
_SystemDateAndTime_Object = MibTableColumn
systemDateAndTime = _SystemDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 3),
    _SystemDateAndTime_Type()
)
systemDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDateAndTime.setStatus("mandatory")
_NetworkTimeServer1_Type = IpAddress
_NetworkTimeServer1_Object = MibTableColumn
networkTimeServer1 = _NetworkTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 4),
    _NetworkTimeServer1_Type()
)
networkTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkTimeServer1.setStatus("mandatory")


class _NetworkTimeProtocol_Type(Integer32):
    """Custom type networkTimeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ntp", 1)
    )


_NetworkTimeProtocol_Type.__name__ = "Integer32"
_NetworkTimeProtocol_Object = MibTableColumn
networkTimeProtocol = _NetworkTimeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 5),
    _NetworkTimeProtocol_Type()
)
networkTimeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkTimeProtocol.setStatus("mandatory")
_NetworkTimeEnable_Type = AdicEnable
_NetworkTimeEnable_Object = MibTableColumn
networkTimeEnable = _NetworkTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 6),
    _NetworkTimeEnable_Type()
)
networkTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkTimeEnable.setStatus("mandatory")
_ManagementMibVersion_Type = AdicMibVersion
_ManagementMibVersion_Object = MibTableColumn
managementMibVersion = _ManagementMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 7),
    _ManagementMibVersion_Type()
)
managementMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementMibVersion.setStatus("mandatory")
_EnableDaylightSavingsTime_Type = AdicEnable
_EnableDaylightSavingsTime_Object = MibTableColumn
enableDaylightSavingsTime = _EnableDaylightSavingsTime_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 8),
    _EnableDaylightSavingsTime_Type()
)
enableDaylightSavingsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDaylightSavingsTime.setStatus("mandatory")
_NetworkTimeServer2_Type = IpAddress
_NetworkTimeServer2_Object = MibTableColumn
networkTimeServer2 = _NetworkTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 10, 10, 1, 9),
    _NetworkTimeServer2_Type()
)
networkTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkTimeServer2.setStatus("mandatory")
_GlobalEthernetManager_ObjectIdentity = ObjectIdentity
globalEthernetManager = _GlobalEthernetManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15)
)
_GlobalEthernetTable_Object = MibTable
globalEthernetTable = _GlobalEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10)
)
if mibBuilder.loadTexts:
    globalEthernetTable.setStatus("mandatory")
_GlobalEthernetEntry_Object = MibTableRow
globalEthernetEntry = _GlobalEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1)
)
globalEthernetEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    globalEthernetEntry.setStatus("mandatory")
_McbHostName_Type = DisplayString
_McbHostName_Object = MibTableColumn
mcbHostName = _McbHostName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 1),
    _McbHostName_Type()
)
mcbHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcbHostName.setStatus("mandatory")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("mandatory")
_DhcpStatus_Type = AdicEnable
_DhcpStatus_Object = MibTableColumn
dhcpStatus = _DhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 3),
    _DhcpStatus_Type()
)
dhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatus.setStatus("mandatory")
_IpAddressSubnetMask_Type = IpAddress
_IpAddressSubnetMask_Object = MibTableColumn
ipAddressSubnetMask = _IpAddressSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 4),
    _IpAddressSubnetMask_Type()
)
ipAddressSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressSubnetMask.setStatus("mandatory")
_SpeedAutoNegotiation_Type = AdicEnable
_SpeedAutoNegotiation_Object = MibTableColumn
speedAutoNegotiation = _SpeedAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 5),
    _SpeedAutoNegotiation_Type()
)
speedAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAutoNegotiation.setStatus("mandatory")
_PreferredSpeed_Type = AdicEthernetSpeed
_PreferredSpeed_Object = MibTableColumn
preferredSpeed = _PreferredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 6),
    _PreferredSpeed_Type()
)
preferredSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferredSpeed.setStatus("mandatory")
_ActualSpeed_Type = AdicEthernetSpeed
_ActualSpeed_Object = MibTableColumn
actualSpeed = _ActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 7),
    _ActualSpeed_Type()
)
actualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualSpeed.setStatus("mandatory")


class _EthernetDuplex_Type(Integer32):
    """Custom type ethernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_EthernetDuplex_Type.__name__ = "Integer32"
_EthernetDuplex_Object = MibTableColumn
ethernetDuplex = _EthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 15, 10, 1, 8),
    _EthernetDuplex_Type()
)
ethernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetDuplex.setStatus("mandatory")
_SystemManager_ObjectIdentity = ObjectIdentity
systemManager = _SystemManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20)
)
_SystemManagerTable_Object = MibTable
systemManagerTable = _SystemManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10)
)
if mibBuilder.loadTexts:
    systemManagerTable.setStatus("mandatory")
_SystemManagerEntry_Object = MibTableRow
systemManagerEntry = _SystemManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10, 1)
)
systemManagerEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "softwareComponentIndex"),
)
if mibBuilder.loadTexts:
    systemManagerEntry.setStatus("mandatory")
_SoftwareComponentIndex_Type = Integer32
_SoftwareComponentIndex_Object = MibTableColumn
softwareComponentIndex = _SoftwareComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10, 1, 1),
    _SoftwareComponentIndex_Type()
)
softwareComponentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareComponentIndex.setStatus("mandatory")
_ProcessRowStatus_Type = RowStatus
_ProcessRowStatus_Object = MibTableColumn
processRowStatus = _ProcessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10, 1, 2),
    _ProcessRowStatus_Type()
)
processRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processRowStatus.setStatus("mandatory")
_ProcessPhysicalMemory_Type = Integer32
_ProcessPhysicalMemory_Object = MibTableColumn
processPhysicalMemory = _ProcessPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10, 1, 3),
    _ProcessPhysicalMemory_Type()
)
processPhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPhysicalMemory.setStatus("mandatory")
_ProcessResidentMemory_Type = Integer32
_ProcessResidentMemory_Object = MibTableColumn
processResidentMemory = _ProcessResidentMemory_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 10, 1, 4),
    _ProcessResidentMemory_Type()
)
processResidentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processResidentMemory.setStatus("mandatory")
_SoftwareInstallationTable_Object = MibTable
softwareInstallationTable = _SoftwareInstallationTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20)
)
if mibBuilder.loadTexts:
    softwareInstallationTable.setStatus("mandatory")
_SoftwareInstallationEntry_Object = MibTableRow
softwareInstallationEntry = _SoftwareInstallationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1)
)
softwareInstallationEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    softwareInstallationEntry.setStatus("mandatory")
_InstallPackageName_Type = DisplayString
_InstallPackageName_Object = MibTableColumn
installPackageName = _InstallPackageName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 1),
    _InstallPackageName_Type()
)
installPackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    installPackageName.setStatus("mandatory")


class _InstallProcessStatus_Type(Integer32):
    """Custom type installProcessStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 2),
          ("ok", 1),
          ("updateAborted", 4))
    )


_InstallProcessStatus_Type.__name__ = "Integer32"
_InstallProcessStatus_Object = MibTableColumn
installProcessStatus = _InstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 2),
    _InstallProcessStatus_Type()
)
installProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installProcessStatus.setStatus("mandatory")


class _InstallCommand_Type(Integer32):
    """Custom type installCommand based on Integer32"""
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
        *(("abort", 3),
          ("download", 1),
          ("install", 2),
          ("timeEstimate", 4))
    )


_InstallCommand_Type.__name__ = "Integer32"
_InstallCommand_Object = MibTableColumn
installCommand = _InstallCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 3),
    _InstallCommand_Type()
)
installCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    installCommand.setStatus("mandatory")


class _InstallStatusText_Type(DisplayString):
    """Custom type installStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_InstallStatusText_Type.__name__ = "DisplayString"
_InstallStatusText_Object = MibTableColumn
installStatusText = _InstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 4),
    _InstallStatusText_Type()
)
installStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installStatusText.setStatus("mandatory")
_CurrentFirmwareVersion_Type = DisplayString
_CurrentFirmwareVersion_Object = MibTableColumn
currentFirmwareVersion = _CurrentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 5),
    _CurrentFirmwareVersion_Type()
)
currentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFirmwareVersion.setStatus("mandatory")
_PreviousFirmwareVersion_Type = DisplayString
_PreviousFirmwareVersion_Object = MibTableColumn
previousFirmwareVersion = _PreviousFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 6),
    _PreviousFirmwareVersion_Type()
)
previousFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    previousFirmwareVersion.setStatus("mandatory")
_DownloadedFirmwareVersion_Type = DisplayString
_DownloadedFirmwareVersion_Object = MibTableColumn
downloadedFirmwareVersion = _DownloadedFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 7),
    _DownloadedFirmwareVersion_Type()
)
downloadedFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadedFirmwareVersion.setStatus("mandatory")
_ComponentsInBundle_Type = Integer32
_ComponentsInBundle_Object = MibTableColumn
componentsInBundle = _ComponentsInBundle_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 8),
    _ComponentsInBundle_Type()
)
componentsInBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentsInBundle.setStatus("mandatory")


class _McbInstallStatusText_Type(DisplayString):
    """Custom type mcbInstallStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_McbInstallStatusText_Type.__name__ = "DisplayString"
_McbInstallStatusText_Object = MibTableColumn
mcbInstallStatusText = _McbInstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 9),
    _McbInstallStatusText_Type()
)
mcbInstallStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbInstallStatusText.setStatus("mandatory")


class _CmbInstallStatusText_Type(DisplayString):
    """Custom type cmbInstallStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmbInstallStatusText_Type.__name__ = "DisplayString"
_CmbInstallStatusText_Object = MibTableColumn
cmbInstallStatusText = _CmbInstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 10),
    _CmbInstallStatusText_Type()
)
cmbInstallStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmbInstallStatusText.setStatus("mandatory")


class _RcuInstallStatusText_Type(DisplayString):
    """Custom type rcuInstallStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcuInstallStatusText_Type.__name__ = "DisplayString"
_RcuInstallStatusText_Object = MibTableColumn
rcuInstallStatusText = _RcuInstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 11),
    _RcuInstallStatusText_Type()
)
rcuInstallStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcuInstallStatusText.setStatus("mandatory")


class _FcbInstallStatusText_Type(DisplayString):
    """Custom type fcbInstallStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FcbInstallStatusText_Type.__name__ = "DisplayString"
_FcbInstallStatusText_Object = MibTableColumn
fcbInstallStatusText = _FcbInstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 12),
    _FcbInstallStatusText_Type()
)
fcbInstallStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcbInstallStatusText.setStatus("mandatory")


class _AmcInstallStatusText_Type(DisplayString):
    """Custom type amcInstallStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AmcInstallStatusText_Type.__name__ = "DisplayString"
_AmcInstallStatusText_Object = MibTableColumn
amcInstallStatusText = _AmcInstallStatusText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 13),
    _AmcInstallStatusText_Type()
)
amcInstallStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amcInstallStatusText.setStatus("mandatory")
_McbInstallProcessStatus_Type = AdicInstallStatus
_McbInstallProcessStatus_Object = MibTableColumn
mcbInstallProcessStatus = _McbInstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 14),
    _McbInstallProcessStatus_Type()
)
mcbInstallProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcbInstallProcessStatus.setStatus("mandatory")
_CmbInstallProcessStatus_Type = AdicInstallStatus
_CmbInstallProcessStatus_Object = MibTableColumn
cmbInstallProcessStatus = _CmbInstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 15),
    _CmbInstallProcessStatus_Type()
)
cmbInstallProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmbInstallProcessStatus.setStatus("mandatory")
_RcuInstallProcessStatus_Type = AdicInstallStatus
_RcuInstallProcessStatus_Object = MibTableColumn
rcuInstallProcessStatus = _RcuInstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 16),
    _RcuInstallProcessStatus_Type()
)
rcuInstallProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcuInstallProcessStatus.setStatus("mandatory")
_FcbInstallProcessStatus_Type = AdicInstallStatus
_FcbInstallProcessStatus_Object = MibTableColumn
fcbInstallProcessStatus = _FcbInstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 17),
    _FcbInstallProcessStatus_Type()
)
fcbInstallProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcbInstallProcessStatus.setStatus("mandatory")
_AmcInstallProcessStatus_Type = AdicInstallStatus
_AmcInstallProcessStatus_Object = MibTableColumn
amcInstallProcessStatus = _AmcInstallProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 20, 20, 1, 18),
    _AmcInstallProcessStatus_Type()
)
amcInstallProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amcInstallProcessStatus.setStatus("mandatory")
_PersistentData_ObjectIdentity = ObjectIdentity
persistentData = _PersistentData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 30)
)
_PersistentDataTable_Object = MibTable
persistentDataTable = _PersistentDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 30, 10)
)
if mibBuilder.loadTexts:
    persistentDataTable.setStatus("mandatory")
_PersistentDataEntry_Object = MibTableRow
persistentDataEntry = _PersistentDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 30, 10, 1)
)
persistentDataEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    persistentDataEntry.setStatus("mandatory")
_Capacity_Type = Integer32
_Capacity_Object = MibTableColumn
capacity = _Capacity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 30, 10, 1, 1),
    _Capacity_Type()
)
capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacity.setStatus("mandatory")
_FreeSpace_Type = Integer32
_FreeSpace_Object = MibTableColumn
freeSpace = _FreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 30, 10, 1, 2),
    _FreeSpace_Type()
)
freeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeSpace.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20)
)
if mibBuilder.loadTexts:
    userTable.setStatus("obsolete")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1)
)
userEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("obsolete")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("obsolete")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1, 2),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("obsolete")
_UserGroup_Type = DisplayString
_UserGroup_Object = MibTableColumn
userGroup = _UserGroup_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1, 3),
    _UserGroup_Type()
)
userGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroup.setStatus("obsolete")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1, 4),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("obsolete")
_UserLibAccessList_Type = DisplayString
_UserLibAccessList_Object = MibTableColumn
userLibAccessList = _UserLibAccessList_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 40, 20, 1, 5),
    _UserLibAccessList_Type()
)
userLibAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLibAccessList.setStatus("obsolete")
_Licensing_ObjectIdentity = ObjectIdentity
licensing = _Licensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50)
)
_LicenseKeyTable_Object = MibTable
licenseKeyTable = _LicenseKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10)
)
if mibBuilder.loadTexts:
    licenseKeyTable.setStatus("mandatory")
_LicenseKeyEntry_Object = MibTableRow
licenseKeyEntry = _LicenseKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1)
)
licenseKeyEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "licenseKeyIndex"),
)
if mibBuilder.loadTexts:
    licenseKeyEntry.setStatus("mandatory")
_LicenseKeyIndex_Type = Integer32
_LicenseKeyIndex_Object = MibTableColumn
licenseKeyIndex = _LicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 1),
    _LicenseKeyIndex_Type()
)
licenseKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyIndex.setStatus("mandatory")
_LicenseKeyRowStatus_Type = RowStatus
_LicenseKeyRowStatus_Object = MibTableColumn
licenseKeyRowStatus = _LicenseKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 2),
    _LicenseKeyRowStatus_Type()
)
licenseKeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseKeyRowStatus.setStatus("mandatory")
_Key_Type = DisplayString
_Key_Object = MibTableColumn
key = _Key_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 3),
    _Key_Type()
)
key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key.setStatus("mandatory")


class _LicenseKeyDuration_Type(Integer32):
    """Custom type licenseKeyDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("transient", 2))
    )


_LicenseKeyDuration_Type.__name__ = "Integer32"
_LicenseKeyDuration_Object = MibTableColumn
licenseKeyDuration = _LicenseKeyDuration_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 4),
    _LicenseKeyDuration_Type()
)
licenseKeyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyDuration.setStatus("mandatory")
_LicenseKeyExpirationDate_Type = AdicDateAndTime
_LicenseKeyExpirationDate_Object = MibTableColumn
licenseKeyExpirationDate = _LicenseKeyExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 5),
    _LicenseKeyExpirationDate_Type()
)
licenseKeyExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyExpirationDate.setStatus("mandatory")
_LicenseKeyAppliedDate_Type = AdicDateAndTime
_LicenseKeyAppliedDate_Object = MibTableColumn
licenseKeyAppliedDate = _LicenseKeyAppliedDate_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 10, 1, 6),
    _LicenseKeyAppliedDate_Type()
)
licenseKeyAppliedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseKeyAppliedDate.setStatus("mandatory")
_LicenseFeatureTable_Object = MibTable
licenseFeatureTable = _LicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 20)
)
if mibBuilder.loadTexts:
    licenseFeatureTable.setStatus("mandatory")
_LicenseFeatureEntry_Object = MibTableRow
licenseFeatureEntry = _LicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 20, 1)
)
licenseFeatureEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "licenseKeyIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "licenseFeatureIndex"),
)
if mibBuilder.loadTexts:
    licenseFeatureEntry.setStatus("mandatory")
_LicenseFeatureIndex_Type = Integer32
_LicenseFeatureIndex_Object = MibTableColumn
licenseFeatureIndex = _LicenseFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 20, 1, 1),
    _LicenseFeatureIndex_Type()
)
licenseFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureIndex.setStatus("mandatory")
_FeatureName_Type = DisplayString
_FeatureName_Object = MibTableColumn
featureName = _FeatureName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 20, 1, 2),
    _FeatureName_Type()
)
featureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureName.setStatus("mandatory")
_LicenseFeatureQuantity_Type = Integer32
_LicenseFeatureQuantity_Object = MibTableColumn
licenseFeatureQuantity = _LicenseFeatureQuantity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 20, 1, 3),
    _LicenseFeatureQuantity_Type()
)
licenseFeatureQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFeatureQuantity.setStatus("mandatory")
_LicensableFeatureTable_Object = MibTable
licensableFeatureTable = _LicensableFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 30)
)
if mibBuilder.loadTexts:
    licensableFeatureTable.setStatus("mandatory")
_LicensableFeatureEntry_Object = MibTableRow
licensableFeatureEntry = _LicensableFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 30, 1)
)
licensableFeatureEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "licenseFeatureIndex"),
)
if mibBuilder.loadTexts:
    licensableFeatureEntry.setStatus("mandatory")
_LicensableFeatureName_Type = DisplayString
_LicensableFeatureName_Object = MibTableColumn
licensableFeatureName = _LicensableFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 30, 1, 1),
    _LicensableFeatureName_Type()
)
licensableFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensableFeatureName.setStatus("mandatory")
_TotalQuantityLicensed_Type = Integer32
_TotalQuantityLicensed_Object = MibTableColumn
totalQuantityLicensed = _TotalQuantityLicensed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 50, 30, 1, 2),
    _TotalQuantityLicensed_Type()
)
totalQuantityLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalQuantityLicensed.setStatus("mandatory")
_EventManager_ObjectIdentity = ObjectIdentity
eventManager = _EventManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70)
)
_RegistrationTable_Object = MibTable
registrationTable = _RegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 10)
)
if mibBuilder.loadTexts:
    registrationTable.setStatus("mandatory")
_RegistrationEntry_Object = MibTableRow
registrationEntry = _RegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 10, 1)
)
registrationEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "hostIpAddress"),
    (0, "ADIC-MANAGEMENT-MIB", "udpPort"),
)
if mibBuilder.loadTexts:
    registrationEntry.setStatus("mandatory")
_HostIpAddress_Type = IpAddress
_HostIpAddress_Object = MibTableColumn
hostIpAddress = _HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 10, 1, 1),
    _HostIpAddress_Type()
)
hostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostIpAddress.setStatus("mandatory")
_UdpPort_Type = Integer32
_UdpPort_Object = MibTableColumn
udpPort = _UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 10, 1, 2),
    _UdpPort_Type()
)
udpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpPort.setStatus("mandatory")
_RegistrationRowStatus_Type = RowStatus
_RegistrationRowStatus_Object = MibTableColumn
registrationRowStatus = _RegistrationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 10, 1, 3),
    _RegistrationRowStatus_Type()
)
registrationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationRowStatus.setStatus("mandatory")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 20)
)
if mibBuilder.loadTexts:
    logTable.setStatus("optional")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 20, 1)
)
logEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logName"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("optional")
_LogName_Type = DisplayString
_LogName_Object = MibTableColumn
logName = _LogName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 20, 1, 1),
    _LogName_Type()
)
logName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logName.setStatus("optional")
_LogSnapshotTable_Object = MibTable
logSnapshotTable = _LogSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 30)
)
if mibBuilder.loadTexts:
    logSnapshotTable.setStatus("optional")
_LogSnapshotEntry_Object = MibTableRow
logSnapshotEntry = _LogSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 30, 1)
)
logSnapshotEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    logSnapshotEntry.setStatus("optional")


class _LogSnapshotCommand_Type(Integer32):
    """Custom type logSnapshotCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("retrieveLogs", 1)
    )


_LogSnapshotCommand_Type.__name__ = "Integer32"
_LogSnapshotCommand_Object = MibTableColumn
logSnapshotCommand = _LogSnapshotCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 70, 30, 1, 1),
    _LogSnapshotCommand_Type()
)
logSnapshotCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSnapshotCommand.setStatus("optional")
_PhysicalLibrary_ObjectIdentity = ObjectIdentity
physicalLibrary = _PhysicalLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80)
)
_PhGeneralInfoTable_Object = MibTable
phGeneralInfoTable = _PhGeneralInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10)
)
if mibBuilder.loadTexts:
    phGeneralInfoTable.setStatus("mandatory")
_PhGeneralInfoEntry_Object = MibTableRow
phGeneralInfoEntry = _PhGeneralInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1)
)
phGeneralInfoEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    phGeneralInfoEntry.setStatus("mandatory")
_NumElementDomains_Type = Integer32
_NumElementDomains_Object = MibTableColumn
numElementDomains = _NumElementDomains_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 1),
    _NumElementDomains_Type()
)
numElementDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numElementDomains.setStatus("mandatory")
_NumPhSlots_Type = Integer32
_NumPhSlots_Object = MibTableColumn
numPhSlots = _NumPhSlots_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 2),
    _NumPhSlots_Type()
)
numPhSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPhSlots.setStatus("mandatory")
_NumPhIESlots_Type = Integer32
_NumPhIESlots_Object = MibTableColumn
numPhIESlots = _NumPhIESlots_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 3),
    _NumPhIESlots_Type()
)
numPhIESlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPhIESlots.setStatus("mandatory")
_NumPhDrives_Type = Integer32
_NumPhDrives_Object = MibTableColumn
numPhDrives = _NumPhDrives_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 4),
    _NumPhDrives_Type()
)
numPhDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPhDrives.setStatus("mandatory")
_OnlineStatus_Type = AdicOnlineStatus
_OnlineStatus_Object = MibTableColumn
onlineStatus = _OnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 5),
    _OnlineStatus_Type()
)
onlineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onlineStatus.setStatus("mandatory")


class _Readiness_Type(Integer32):
    """Custom type readiness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 2),
          ("ready", 1))
    )


_Readiness_Type.__name__ = "Integer32"
_Readiness_Object = MibTableColumn
readiness = _Readiness_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 6),
    _Readiness_Type()
)
readiness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readiness.setStatus("mandatory")
_AutoInventoryMode_Type = AdicEnable
_AutoInventoryMode_Object = MibTableColumn
autoInventoryMode = _AutoInventoryMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 7),
    _AutoInventoryMode_Type()
)
autoInventoryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoInventoryMode.setStatus("mandatory")
_AutoCalibrateMode_Type = AdicEnable
_AutoCalibrateMode_Object = MibTableColumn
autoCalibrateMode = _AutoCalibrateMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 8),
    _AutoCalibrateMode_Type()
)
autoCalibrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoCalibrateMode.setStatus("mandatory")
_AutoConfigureMode_Type = AdicEnable
_AutoConfigureMode_Object = MibTableColumn
autoConfigureMode = _AutoConfigureMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 9),
    _AutoConfigureMode_Type()
)
autoConfigureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoConfigureMode.setStatus("mandatory")
_NumPhAisles_Type = Integer32
_NumPhAisles_Object = MibTableColumn
numPhAisles = _NumPhAisles_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 10),
    _NumPhAisles_Type()
)
numPhAisles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPhAisles.setStatus("mandatory")


class _OperatingMode_Type(Integer32):
    """Custom type operatingMode based on Integer32"""
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
        *(("delay", 2),
          ("delayAndUnload", 4),
          ("noUnload", 5),
          ("normal", 1),
          ("unload", 3))
    )


_OperatingMode_Type.__name__ = "Integer32"
_OperatingMode_Object = MibTableColumn
operatingMode = _OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 11),
    _OperatingMode_Type()
)
operatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatingMode.setStatus("mandatory")
_NumStorageCartridges_Type = Integer32
_NumStorageCartridges_Object = MibTableColumn
numStorageCartridges = _NumStorageCartridges_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 12),
    _NumStorageCartridges_Type()
)
numStorageCartridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numStorageCartridges.setStatus("mandatory")
_NumCleaningCartridges_Type = Integer32
_NumCleaningCartridges_Object = MibTableColumn
numCleaningCartridges = _NumCleaningCartridges_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 13),
    _NumCleaningCartridges_Type()
)
numCleaningCartridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCleaningCartridges.setStatus("mandatory")
_PhysLibraryManagerLun_Type = Integer32
_PhysLibraryManagerLun_Object = MibTableColumn
physLibraryManagerLun = _PhysLibraryManagerLun_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 14),
    _PhysLibraryManagerLun_Type()
)
physLibraryManagerLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physLibraryManagerLun.setStatus("mandatory")
_PhysLibraryAutoCleaning_Type = AdicEnable
_PhysLibraryAutoCleaning_Object = MibTableColumn
physLibraryAutoCleaning = _PhysLibraryAutoCleaning_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 15),
    _PhysLibraryAutoCleaning_Type()
)
physLibraryAutoCleaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physLibraryAutoCleaning.setStatus("mandatory")
_PhysLibraryDoorStatus_Type = AdicDoorStatus
_PhysLibraryDoorStatus_Object = MibTableColumn
physLibraryDoorStatus = _PhysLibraryDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 16),
    _PhysLibraryDoorStatus_Type()
)
physLibraryDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physLibraryDoorStatus.setStatus("mandatory")
_NumPhFrames_Type = Integer32
_NumPhFrames_Object = MibTableColumn
numPhFrames = _NumPhFrames_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 17),
    _NumPhFrames_Type()
)
numPhFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPhFrames.setStatus("mandatory")
_TotalRawCapacity_Type = Integer32
_TotalRawCapacity_Object = MibTableColumn
totalRawCapacity = _TotalRawCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 18),
    _TotalRawCapacity_Type()
)
totalRawCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRawCapacity.setStatus("mandatory")
_TotalFreeCapacity_Type = Integer32
_TotalFreeCapacity_Object = MibTableColumn
totalFreeCapacity = _TotalFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 19),
    _TotalFreeCapacity_Type()
)
totalFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFreeCapacity.setStatus("mandatory")
_TotalUsedCapacity_Type = Integer32
_TotalUsedCapacity_Object = MibTableColumn
totalUsedCapacity = _TotalUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 20),
    _TotalUsedCapacity_Type()
)
totalUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalUsedCapacity.setStatus("mandatory")
_LogicalSNAdressingMode_Type = AdicEnable
_LogicalSNAdressingMode_Object = MibTableColumn
logicalSNAdressingMode = _LogicalSNAdressingMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 10, 1, 21),
    _LogicalSNAdressingMode_Type()
)
logicalSNAdressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logicalSNAdressingMode.setStatus("mandatory")
_MediaDomainTable_Object = MibTable
mediaDomainTable = _MediaDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20)
)
if mibBuilder.loadTexts:
    mediaDomainTable.setStatus("mandatory")
_MediaDomainEntry_Object = MibTableRow
mediaDomainEntry = _MediaDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1)
)
mediaDomainEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
)
if mibBuilder.loadTexts:
    mediaDomainEntry.setStatus("mandatory")
_MediaDomainIndex_Type = Integer32
_MediaDomainIndex_Object = MibTableColumn
mediaDomainIndex = _MediaDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1, 1),
    _MediaDomainIndex_Type()
)
mediaDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaDomainIndex.setStatus("mandatory")
_MediaDomainName_Type = DisplayString
_MediaDomainName_Object = MibTableColumn
mediaDomainName = _MediaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1, 2),
    _MediaDomainName_Type()
)
mediaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaDomainName.setStatus("mandatory")
_NumStorageElements_Type = Integer32
_NumStorageElements_Object = MibTableColumn
numStorageElements = _NumStorageElements_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1, 3),
    _NumStorageElements_Type()
)
numStorageElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numStorageElements.setStatus("mandatory")
_NumIeElements_Type = Integer32
_NumIeElements_Object = MibTableColumn
numIeElements = _NumIeElements_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1, 4),
    _NumIeElements_Type()
)
numIeElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIeElements.setStatus("mandatory")
_NumCleaningSlots_Type = Integer32
_NumCleaningSlots_Object = MibTableColumn
numCleaningSlots = _NumCleaningSlots_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 20, 1, 5),
    _NumCleaningSlots_Type()
)
numCleaningSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numCleaningSlots.setStatus("mandatory")
_MediaTypeTable_Object = MibTable
mediaTypeTable = _MediaTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 30)
)
if mibBuilder.loadTexts:
    mediaTypeTable.setStatus("mandatory")
_MediaTypeEntry_Object = MibTableRow
mediaTypeEntry = _MediaTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 30, 1)
)
mediaTypeEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
)
if mibBuilder.loadTexts:
    mediaTypeEntry.setStatus("mandatory")
_MediaTypeIndex_Type = Integer32
_MediaTypeIndex_Object = MibTableColumn
mediaTypeIndex = _MediaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 30, 1, 1),
    _MediaTypeIndex_Type()
)
mediaTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaTypeIndex.setStatus("mandatory")
_MediaTypeName_Type = DisplayString
_MediaTypeName_Object = MibTableColumn
mediaTypeName = _MediaTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 30, 1, 2),
    _MediaTypeName_Type()
)
mediaTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaTypeName.setStatus("mandatory")
_NumDriveElements_Type = Integer32
_NumDriveElements_Object = MibTableColumn
numDriveElements = _NumDriveElements_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 30, 1, 3),
    _NumDriveElements_Type()
)
numDriveElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDriveElements.setStatus("mandatory")
_PhFrameTable_Object = MibTable
phFrameTable = _PhFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 41)
)
if mibBuilder.loadTexts:
    phFrameTable.setStatus("optional")
_PhFrameEntry_Object = MibTableRow
phFrameEntry = _PhFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 41, 1)
)
phFrameEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
)
if mibBuilder.loadTexts:
    phFrameEntry.setStatus("optional")
_PhFrameType_Type = AdicComponentType
_PhFrameType_Object = MibTableColumn
phFrameType = _PhFrameType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 41, 1, 1),
    _PhFrameType_Type()
)
phFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phFrameType.setStatus("optional")
_PhFrameSerialNumber_Type = DisplayString
_PhFrameSerialNumber_Object = MibTableColumn
phFrameSerialNumber = _PhFrameSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 41, 1, 2),
    _PhFrameSerialNumber_Type()
)
phFrameSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phFrameSerialNumber.setStatus("optional")
_PhFrameNumRacks_Type = Integer32
_PhFrameNumRacks_Object = MibTableColumn
phFrameNumRacks = _PhFrameNumRacks_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 41, 1, 3),
    _PhFrameNumRacks_Type()
)
phFrameNumRacks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phFrameNumRacks.setStatus("optional")
_PhSegmentTable_Object = MibTable
phSegmentTable = _PhSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55)
)
if mibBuilder.loadTexts:
    phSegmentTable.setStatus("mandatory")
_PhSegmentEntry_Object = MibTableRow
phSegmentEntry = _PhSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1)
)
phSegmentEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentType"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    phSegmentEntry.setStatus("mandatory")
_PhSegmentAisle_Type = Integer32
_PhSegmentAisle_Object = MibTableColumn
phSegmentAisle = _PhSegmentAisle_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 1),
    _PhSegmentAisle_Type()
)
phSegmentAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentAisle.setStatus("mandatory")
_PhSegmentFrame_Type = Integer32
_PhSegmentFrame_Object = MibTableColumn
phSegmentFrame = _PhSegmentFrame_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 2),
    _PhSegmentFrame_Type()
)
phSegmentFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentFrame.setStatus("mandatory")
_PhSegmentRack_Type = Integer32
_PhSegmentRack_Object = MibTableColumn
phSegmentRack = _PhSegmentRack_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 3),
    _PhSegmentRack_Type()
)
phSegmentRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentRack.setStatus("mandatory")
_PhSegmentSection_Type = Integer32
_PhSegmentSection_Object = MibTableColumn
phSegmentSection = _PhSegmentSection_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 4),
    _PhSegmentSection_Type()
)
phSegmentSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentSection.setStatus("mandatory")
_PhSegmentCol_Type = Integer32
_PhSegmentCol_Object = MibTableColumn
phSegmentCol = _PhSegmentCol_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 5),
    _PhSegmentCol_Type()
)
phSegmentCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentCol.setStatus("mandatory")
_PhSegmentStartingRow_Type = Integer32
_PhSegmentStartingRow_Object = MibTableColumn
phSegmentStartingRow = _PhSegmentStartingRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 6),
    _PhSegmentStartingRow_Type()
)
phSegmentStartingRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentStartingRow.setStatus("mandatory")
_PhSegmentSize_Type = Integer32
_PhSegmentSize_Object = MibTableColumn
phSegmentSize = _PhSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 7),
    _PhSegmentSize_Type()
)
phSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentSize.setStatus("mandatory")
_PhSegmentType_Type = AdicSegmentType
_PhSegmentType_Object = MibTableColumn
phSegmentType = _PhSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 8),
    _PhSegmentType_Type()
)
phSegmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentType.setStatus("mandatory")
_PhSegmentMediaDomain_Type = Integer32
_PhSegmentMediaDomain_Object = MibTableColumn
phSegmentMediaDomain = _PhSegmentMediaDomain_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 9),
    _PhSegmentMediaDomain_Type()
)
phSegmentMediaDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentMediaDomain.setStatus("mandatory")


class _PhSegmentStatus_Type(Integer32):
    """Custom type phSegmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2),
          ("reservedForCleaning", 3))
    )


_PhSegmentStatus_Type.__name__ = "Integer32"
_PhSegmentStatus_Object = MibTableColumn
phSegmentStatus = _PhSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 10),
    _PhSegmentStatus_Type()
)
phSegmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentStatus.setStatus("mandatory")


class _PhSegmentCodStatus_Type(Integer32):
    """Custom type phSegmentCodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("noCod", 3))
    )


_PhSegmentCodStatus_Type.__name__ = "Integer32"
_PhSegmentCodStatus_Object = MibTableColumn
phSegmentCodStatus = _PhSegmentCodStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 11),
    _PhSegmentCodStatus_Type()
)
phSegmentCodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegmentCodStatus.setStatus("mandatory")
_PhSegStartingAddress_Type = Integer32
_PhSegStartingAddress_Object = MibTableColumn
phSegStartingAddress = _PhSegStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 55, 1, 12),
    _PhSegStartingAddress_Type()
)
phSegStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSegStartingAddress.setStatus("mandatory")
_PhStorageSegTable_Object = MibTable
phStorageSegTable = _PhStorageSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 60)
)
if mibBuilder.loadTexts:
    phStorageSegTable.setStatus("mandatory")
_PhStorageSegEntry_Object = MibTableRow
phStorageSegEntry = _PhStorageSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 60, 1)
)
phStorageSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    phStorageSegEntry.setStatus("mandatory")
_PhStorageSegSize_Type = Integer32
_PhStorageSegSize_Object = MibTableColumn
phStorageSegSize = _PhStorageSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 60, 1, 1),
    _PhStorageSegSize_Type()
)
phStorageSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phStorageSegSize.setStatus("mandatory")
_PhIeSegTable_Object = MibTable
phIeSegTable = _PhIeSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70)
)
if mibBuilder.loadTexts:
    phIeSegTable.setStatus("optional")
_PhIeSegEntry_Object = MibTableRow
phIeSegEntry = _PhIeSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1)
)
phIeSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    phIeSegEntry.setStatus("optional")
_PhIeSegSize_Type = Integer32
_PhIeSegSize_Object = MibTableColumn
phIeSegSize = _PhIeSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1, 1),
    _PhIeSegSize_Type()
)
phIeSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeSegSize.setStatus("optional")


class _PhIeSegReserve_Type(Integer32):
    """Custom type phIeSegReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 2),
          ("reserve", 1))
    )


_PhIeSegReserve_Type.__name__ = "Integer32"
_PhIeSegReserve_Object = MibTableColumn
phIeSegReserve = _PhIeSegReserve_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1, 2),
    _PhIeSegReserve_Type()
)
phIeSegReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phIeSegReserve.setStatus("optional")
_PhIeSegReservedBy_Type = Integer32
_PhIeSegReservedBy_Object = MibTableColumn
phIeSegReservedBy = _PhIeSegReservedBy_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1, 3),
    _PhIeSegReservedBy_Type()
)
phIeSegReservedBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phIeSegReservedBy.setStatus("optional")


class _PhIeSegOnlineStatus_Type(Integer32):
    """Custom type phIeSegOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_PhIeSegOnlineStatus_Type.__name__ = "Integer32"
_PhIeSegOnlineStatus_Object = MibTableColumn
phIeSegOnlineStatus = _PhIeSegOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1, 4),
    _PhIeSegOnlineStatus_Type()
)
phIeSegOnlineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phIeSegOnlineStatus.setStatus("optional")


class _PhIeSegCommand_Type(Integer32):
    """Custom type phIeSegCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("import", 1)
    )


_PhIeSegCommand_Type.__name__ = "Integer32"
_PhIeSegCommand_Object = MibTableColumn
phIeSegCommand = _PhIeSegCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 70, 1, 5),
    _PhIeSegCommand_Type()
)
phIeSegCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phIeSegCommand.setStatus("optional")
_PhIeStationTable_Object = MibTable
phIeStationTable = _PhIeStationTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 75)
)
if mibBuilder.loadTexts:
    phIeStationTable.setStatus("mandatory")
_PhIeStationEntry_Object = MibTableRow
phIeStationEntry = _PhIeStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 75, 1)
)
phIeStationEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phIeStationNumber"),
)
if mibBuilder.loadTexts:
    phIeStationEntry.setStatus("mandatory")
_PhIeStationNumber_Type = Integer32
_PhIeStationNumber_Object = MibTableColumn
phIeStationNumber = _PhIeStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 75, 1, 1),
    _PhIeStationNumber_Type()
)
phIeStationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeStationNumber.setStatus("mandatory")
_PhIeStationDoorStatus_Type = AdicDoorStatus
_PhIeStationDoorStatus_Object = MibTableColumn
phIeStationDoorStatus = _PhIeStationDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 75, 1, 2),
    _PhIeStationDoorStatus_Type()
)
phIeStationDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeStationDoorStatus.setStatus("mandatory")
_PhIeStationREDId_Type = AdicREDIdentifier
_PhIeStationREDId_Object = MibTableColumn
phIeStationREDId = _PhIeStationREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 75, 1, 3),
    _PhIeStationREDId_Type()
)
phIeStationREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeStationREDId.setStatus("mandatory")
_PhDriveSegTable_Object = MibTable
phDriveSegTable = _PhDriveSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 80)
)
if mibBuilder.loadTexts:
    phDriveSegTable.setStatus("mandatory")
_PhDriveSegEntry_Object = MibTableRow
phDriveSegEntry = _PhDriveSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 80, 1)
)
phDriveSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    phDriveSegEntry.setStatus("mandatory")
_PhDriveSegSize_Type = Integer32
_PhDriveSegSize_Object = MibTableColumn
phDriveSegSize = _PhDriveSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 80, 1, 1),
    _PhDriveSegSize_Type()
)
phDriveSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveSegSize.setStatus("mandatory")
_PhDriveSegMediaType_Type = Integer32
_PhDriveSegMediaType_Object = MibTableColumn
phDriveSegMediaType = _PhDriveSegMediaType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 80, 1, 2),
    _PhDriveSegMediaType_Type()
)
phDriveSegMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveSegMediaType.setStatus("mandatory")
_PhDriveSegInterfaceType_Type = AdicInterfaceType
_PhDriveSegInterfaceType_Object = MibTableColumn
phDriveSegInterfaceType = _PhDriveSegInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 80, 1, 3),
    _PhDriveSegInterfaceType_Type()
)
phDriveSegInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveSegInterfaceType.setStatus("mandatory")
_PhCleaningSegTable_Object = MibTable
phCleaningSegTable = _PhCleaningSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 85)
)
if mibBuilder.loadTexts:
    phCleaningSegTable.setStatus("optional")
_PhCleaningSegEntry_Object = MibTableRow
phCleaningSegEntry = _PhCleaningSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 85, 1)
)
phCleaningSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    phCleaningSegEntry.setStatus("optional")
_PhCleaningSegSize_Type = Integer32
_PhCleaningSegSize_Object = MibTableColumn
phCleaningSegSize = _PhCleaningSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 85, 1, 1),
    _PhCleaningSegSize_Type()
)
phCleaningSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phCleaningSegSize.setStatus("optional")
_PhCleaningSegRowStatus_Type = RowStatus
_PhCleaningSegRowStatus_Object = MibTableColumn
phCleaningSegRowStatus = _PhCleaningSegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 85, 1, 2),
    _PhCleaningSegRowStatus_Type()
)
phCleaningSegRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningSegRowStatus.setStatus("optional")
_PhStorageSlotTable_Object = MibTable
phStorageSlotTable = _PhStorageSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 90)
)
if mibBuilder.loadTexts:
    phStorageSlotTable.setStatus("optional")
_PhStorageSlotEntry_Object = MibTableRow
phStorageSlotEntry = _PhStorageSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 90, 1)
)
phStorageSlotEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phStorageRow"),
)
if mibBuilder.loadTexts:
    phStorageSlotEntry.setStatus("optional")
_PhStorageRow_Type = Integer32
_PhStorageRow_Object = MibTableColumn
phStorageRow = _PhStorageRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 90, 1, 1),
    _PhStorageRow_Type()
)
phStorageRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phStorageRow.setStatus("optional")
_PhStorageElementAddr_Type = Integer32
_PhStorageElementAddr_Object = MibTableColumn
phStorageElementAddr = _PhStorageElementAddr_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 90, 1, 2),
    _PhStorageElementAddr_Type()
)
phStorageElementAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phStorageElementAddr.setStatus("optional")
_PhIeSlotTable_Object = MibTable
phIeSlotTable = _PhIeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100)
)
if mibBuilder.loadTexts:
    phIeSlotTable.setStatus("optional")
_PhIeSlotEntry_Object = MibTableRow
phIeSlotEntry = _PhIeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100, 1)
)
phIeSlotEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phIeRow"),
)
if mibBuilder.loadTexts:
    phIeSlotEntry.setStatus("optional")
_PhIeRow_Type = Integer32
_PhIeRow_Object = MibTableColumn
phIeRow = _PhIeRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100, 1, 1),
    _PhIeRow_Type()
)
phIeRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeRow.setStatus("optional")
_PhIeElementAddr_Type = Integer32
_PhIeElementAddr_Object = MibTableColumn
phIeElementAddr = _PhIeElementAddr_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100, 1, 2),
    _PhIeElementAddr_Type()
)
phIeElementAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeElementAddr.setStatus("optional")


class _PhIeMediaPresent_Type(Integer32):
    """Custom type phIeMediaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("no", 2),
          ("yes", 1))
    )


_PhIeMediaPresent_Type.__name__ = "Integer32"
_PhIeMediaPresent_Object = MibTableColumn
phIeMediaPresent = _PhIeMediaPresent_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100, 1, 3),
    _PhIeMediaPresent_Type()
)
phIeMediaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeMediaPresent.setStatus("optional")
_PhIeMediaId_Type = AdicBarCode
_PhIeMediaId_Object = MibTableColumn
phIeMediaId = _PhIeMediaId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 100, 1, 4),
    _PhIeMediaId_Type()
)
phIeMediaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phIeMediaId.setStatus("optional")
_PhDriveTable_Object = MibTable
phDriveTable = _PhDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110)
)
if mibBuilder.loadTexts:
    phDriveTable.setStatus("mandatory")
_PhDriveEntry_Object = MibTableRow
phDriveEntry = _PhDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1)
)
phDriveEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phDriveRow"),
)
if mibBuilder.loadTexts:
    phDriveEntry.setStatus("mandatory")
_PhDriveRow_Type = Integer32
_PhDriveRow_Object = MibTableColumn
phDriveRow = _PhDriveRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 1),
    _PhDriveRow_Type()
)
phDriveRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveRow.setStatus("mandatory")
_PhDriveElementAddr_Type = Integer32
_PhDriveElementAddr_Object = MibTableColumn
phDriveElementAddr = _PhDriveElementAddr_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 2),
    _PhDriveElementAddr_Type()
)
phDriveElementAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveElementAddr.setStatus("mandatory")
_PhDriveScsiId_Type = Integer32
_PhDriveScsiId_Object = MibTableColumn
phDriveScsiId = _PhDriveScsiId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 3),
    _PhDriveScsiId_Type()
)
phDriveScsiId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveScsiId.setStatus("mandatory")
_PhDriveScsiLun_Type = Integer32
_PhDriveScsiLun_Object = MibTableColumn
phDriveScsiLun = _PhDriveScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 4),
    _PhDriveScsiLun_Type()
)
phDriveScsiLun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveScsiLun.setStatus("mandatory")
_PhDriveWwn_Type = DisplayString
_PhDriveWwn_Object = MibTableColumn
phDriveWwn = _PhDriveWwn_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 5),
    _PhDriveWwn_Type()
)
phDriveWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveWwn.setStatus("mandatory")
_PhDriveVendor_Type = DisplayString
_PhDriveVendor_Object = MibTableColumn
phDriveVendor = _PhDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 6),
    _PhDriveVendor_Type()
)
phDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveVendor.setStatus("mandatory")
_PhDriveProduct_Type = DisplayString
_PhDriveProduct_Object = MibTableColumn
phDriveProduct = _PhDriveProduct_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 7),
    _PhDriveProduct_Type()
)
phDriveProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveProduct.setStatus("mandatory")
_PhDriveSerialNumber_Type = DisplayString
_PhDriveSerialNumber_Object = MibTableColumn
phDriveSerialNumber = _PhDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 8),
    _PhDriveSerialNumber_Type()
)
phDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveSerialNumber.setStatus("mandatory")


class _PhDriveNeedsCleaning_Type(Integer32):
    """Custom type phDriveNeedsCleaning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("immediate", 3),
          ("true", 1))
    )


_PhDriveNeedsCleaning_Type.__name__ = "Integer32"
_PhDriveNeedsCleaning_Object = MibTableColumn
phDriveNeedsCleaning = _PhDriveNeedsCleaning_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 9),
    _PhDriveNeedsCleaning_Type()
)
phDriveNeedsCleaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveNeedsCleaning.setStatus("mandatory")
_PhDriveAutoCleaning_Type = Boolean
_PhDriveAutoCleaning_Object = MibTableColumn
phDriveAutoCleaning = _PhDriveAutoCleaning_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 10),
    _PhDriveAutoCleaning_Type()
)
phDriveAutoCleaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveAutoCleaning.setStatus("mandatory")
_PhDriveInterfaceType_Type = AdicInterfaceType
_PhDriveInterfaceType_Object = MibTableColumn
phDriveInterfaceType = _PhDriveInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 11),
    _PhDriveInterfaceType_Type()
)
phDriveInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveInterfaceType.setStatus("mandatory")
_PhDriveFcLoopId_Type = Integer32
_PhDriveFcLoopId_Object = MibTableColumn
phDriveFcLoopId = _PhDriveFcLoopId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 12),
    _PhDriveFcLoopId_Type()
)
phDriveFcLoopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveFcLoopId.setStatus("mandatory")


class _PhDriveFcLoopIdMode_Type(Integer32):
    """Custom type phDriveFcLoopIdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 2),
          ("soft", 1))
    )


_PhDriveFcLoopIdMode_Type.__name__ = "Integer32"
_PhDriveFcLoopIdMode_Object = MibTableColumn
phDriveFcLoopIdMode = _PhDriveFcLoopIdMode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 13),
    _PhDriveFcLoopIdMode_Type()
)
phDriveFcLoopIdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveFcLoopIdMode.setStatus("mandatory")
_PhDriveFcHardId_Type = Integer32
_PhDriveFcHardId_Object = MibTableColumn
phDriveFcHardId = _PhDriveFcHardId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 14),
    _PhDriveFcHardId_Type()
)
phDriveFcHardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveFcHardId.setStatus("mandatory")


class _PhDriveStatus_Type(Integer32):
    """Custom type phDriveStatus based on Integer32"""
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
        *(("empty", 4),
          ("loaded", 2),
          ("loading", 1),
          ("unloading", 3))
    )


_PhDriveStatus_Type.__name__ = "Integer32"
_PhDriveStatus_Object = MibTableColumn
phDriveStatus = _PhDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 15),
    _PhDriveStatus_Type()
)
phDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveStatus.setStatus("mandatory")


class _PhDriveCommand_Type(Integer32):
    """Custom type phDriveCommand based on Integer32"""
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
        *(("driveBrickUpdate", 7),
          ("offline", 2),
          ("online", 1),
          ("powerCycle", 6),
          ("powerOff", 5),
          ("powerOn", 4),
          ("reset", 3))
    )


_PhDriveCommand_Type.__name__ = "Integer32"
_PhDriveCommand_Object = MibTableColumn
phDriveCommand = _PhDriveCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 16),
    _PhDriveCommand_Type()
)
phDriveCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveCommand.setStatus("mandatory")
_PhDriveFcPortId_Type = Integer32
_PhDriveFcPortId_Object = MibTableColumn
phDriveFcPortId = _PhDriveFcPortId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 17),
    _PhDriveFcPortId_Type()
)
phDriveFcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveFcPortId.setStatus("mandatory")
_PhDriveCompressionOn_Type = Boolean
_PhDriveCompressionOn_Object = MibTableColumn
phDriveCompressionOn = _PhDriveCompressionOn_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 18),
    _PhDriveCompressionOn_Type()
)
phDriveCompressionOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveCompressionOn.setStatus("mandatory")
_PhDriveWriteProtected_Type = Boolean
_PhDriveWriteProtected_Object = MibTableColumn
phDriveWriteProtected = _PhDriveWriteProtected_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 19),
    _PhDriveWriteProtected_Type()
)
phDriveWriteProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phDriveWriteProtected.setStatus("mandatory")
_PhDriveNumLoads_Type = Integer32
_PhDriveNumLoads_Object = MibTableColumn
phDriveNumLoads = _PhDriveNumLoads_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 20),
    _PhDriveNumLoads_Type()
)
phDriveNumLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveNumLoads.setStatus("mandatory")
_PhDriveNumCleans_Type = Integer32
_PhDriveNumCleans_Object = MibTableColumn
phDriveNumCleans = _PhDriveNumCleans_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 21),
    _PhDriveNumCleans_Type()
)
phDriveNumCleans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveNumCleans.setStatus("mandatory")


class _PhDrivePowerStatus_Type(Integer32):
    """Custom type phDrivePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poweredOff", 2),
          ("poweredOn", 1))
    )


_PhDrivePowerStatus_Type.__name__ = "Integer32"
_PhDrivePowerStatus_Object = MibTableColumn
phDrivePowerStatus = _PhDrivePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 22),
    _PhDrivePowerStatus_Type()
)
phDrivePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDrivePowerStatus.setStatus("mandatory")
_PhDriveReadErrors_Type = Integer32
_PhDriveReadErrors_Object = MibTableColumn
phDriveReadErrors = _PhDriveReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 23),
    _PhDriveReadErrors_Type()
)
phDriveReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveReadErrors.setStatus("mandatory")
_PhDriveWriteErrors_Type = Integer32
_PhDriveWriteErrors_Object = MibTableColumn
phDriveWriteErrors = _PhDriveWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 24),
    _PhDriveWriteErrors_Type()
)
phDriveWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveWriteErrors.setStatus("mandatory")
_PhDriveMbytesRead_Type = Integer32
_PhDriveMbytesRead_Object = MibTableColumn
phDriveMbytesRead = _PhDriveMbytesRead_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 25),
    _PhDriveMbytesRead_Type()
)
phDriveMbytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveMbytesRead.setStatus("mandatory")
_PhDriveMbytesWritten_Type = Integer32
_PhDriveMbytesWritten_Object = MibTableColumn
phDriveMbytesWritten = _PhDriveMbytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 26),
    _PhDriveMbytesWritten_Type()
)
phDriveMbytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveMbytesWritten.setStatus("mandatory")
_PhDriveFirmwareVersion_Type = DisplayString
_PhDriveFirmwareVersion_Object = MibTableColumn
phDriveFirmwareVersion = _PhDriveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 27),
    _PhDriveFirmwareVersion_Type()
)
phDriveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveFirmwareVersion.setStatus("mandatory")
_PhDriveREDId_Type = AdicREDIdentifier
_PhDriveREDId_Object = MibTableColumn
phDriveREDId = _PhDriveREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 28),
    _PhDriveREDId_Type()
)
phDriveREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveREDId.setStatus("mandatory")
_PhDriveOnlineStatus_Type = AdicOnlineStatus
_PhDriveOnlineStatus_Object = MibTableColumn
phDriveOnlineStatus = _PhDriveOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 29),
    _PhDriveOnlineStatus_Type()
)
phDriveOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveOnlineStatus.setStatus("mandatory")


class _PhDriveErrorCodeBytes_Type(OctetString):
    """Custom type phDriveErrorCodeBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PhDriveErrorCodeBytes_Type.__name__ = "OctetString"
_PhDriveErrorCodeBytes_Object = MibTableColumn
phDriveErrorCodeBytes = _PhDriveErrorCodeBytes_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 30),
    _PhDriveErrorCodeBytes_Type()
)
phDriveErrorCodeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveErrorCodeBytes.setStatus("mandatory")
_PhDriveRasStatus_Type = AdicStatusGroupState
_PhDriveRasStatus_Object = MibTableColumn
phDriveRasStatus = _PhDriveRasStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 31),
    _PhDriveRasStatus_Type()
)
phDriveRasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveRasStatus.setStatus("mandatory")
_PhDriveWwPortName_Type = DisplayString
_PhDriveWwPortName_Object = MibTableColumn
phDriveWwPortName = _PhDriveWwPortName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 110, 1, 32),
    _PhDriveWwPortName_Type()
)
phDriveWwPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phDriveWwPortName.setStatus("mandatory")
_PhDriveStatHistoryTable_Object = MibTable
phDriveStatHistoryTable = _PhDriveStatHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112)
)
if mibBuilder.loadTexts:
    phDriveStatHistoryTable.setStatus("mandatory")
_PhDriveStatHistoryEntry_Object = MibTableRow
phDriveStatHistoryEntry = _PhDriveStatHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112, 1)
)
phDriveStatHistoryEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phDriveRow"),
    (0, "ADIC-MANAGEMENT-MIB", "phHourIndex"),
)
if mibBuilder.loadTexts:
    phDriveStatHistoryEntry.setStatus("mandatory")
_PhHourIndex_Type = Integer32
_PhHourIndex_Object = MibTableColumn
phHourIndex = _PhHourIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112, 1, 1),
    _PhHourIndex_Type()
)
phHourIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phHourIndex.setStatus("mandatory")
_PhHourlyMBytesRead_Type = Integer32
_PhHourlyMBytesRead_Object = MibTableColumn
phHourlyMBytesRead = _PhHourlyMBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112, 1, 2),
    _PhHourlyMBytesRead_Type()
)
phHourlyMBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phHourlyMBytesRead.setStatus("mandatory")
_PhHourlyMBytesWritten_Type = Integer32
_PhHourlyMBytesWritten_Object = MibTableColumn
phHourlyMBytesWritten = _PhHourlyMBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112, 1, 3),
    _PhHourlyMBytesWritten_Type()
)
phHourlyMBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phHourlyMBytesWritten.setStatus("mandatory")
_PhHourlyMounts_Type = Integer32
_PhHourlyMounts_Object = MibTableColumn
phHourlyMounts = _PhHourlyMounts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 112, 1, 4),
    _PhHourlyMounts_Type()
)
phHourlyMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phHourlyMounts.setStatus("mandatory")
_PhDrivePorts_ObjectIdentity = ObjectIdentity
phDrivePorts = _PhDrivePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116)
)
_FcDrivePortTable_Object = MibTable
fcDrivePortTable = _FcDrivePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10)
)
if mibBuilder.loadTexts:
    fcDrivePortTable.setStatus("mandatory")
_FcDrivePortEntry_Object = MibTableRow
fcDrivePortEntry = _FcDrivePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1)
)
fcDrivePortEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phDriveRow"),
)
if mibBuilder.loadTexts:
    fcDrivePortEntry.setStatus("mandatory")
_FcPortPreferredSpeed_Type = AdicFcPortSpeed
_FcPortPreferredSpeed_Object = MibTableColumn
fcPortPreferredSpeed = _FcPortPreferredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1, 1),
    _FcPortPreferredSpeed_Type()
)
fcPortPreferredSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcPortPreferredSpeed.setStatus("mandatory")
_FcPortNegotiatedSpeed_Type = AdicFcPortSpeed
_FcPortNegotiatedSpeed_Object = MibTableColumn
fcPortNegotiatedSpeed = _FcPortNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1, 2),
    _FcPortNegotiatedSpeed_Type()
)
fcPortNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortNegotiatedSpeed.setStatus("mandatory")
_FcPortPreferredType_Type = AdicFcPortType
_FcPortPreferredType_Object = MibTableColumn
fcPortPreferredType = _FcPortPreferredType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1, 3),
    _FcPortPreferredType_Type()
)
fcPortPreferredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcPortPreferredType.setStatus("mandatory")
_FcPortNegotiatedType_Type = AdicFcPortType
_FcPortNegotiatedType_Object = MibTableColumn
fcPortNegotiatedType = _FcPortNegotiatedType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1, 4),
    _FcPortNegotiatedType_Type()
)
fcPortNegotiatedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortNegotiatedType.setStatus("mandatory")


class _FcPortTypeQualifier_Type(Integer32):
    """Custom type fcPortTypeQualifier based on Integer32"""
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


_FcPortTypeQualifier_Type.__name__ = "Integer32"
_FcPortTypeQualifier_Object = MibTableColumn
fcPortTypeQualifier = _FcPortTypeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 116, 10, 1, 5),
    _FcPortTypeQualifier_Type()
)
fcPortTypeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortTypeQualifier.setStatus("mandatory")
_PhMediaTable_Object = MibTable
phMediaTable = _PhMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120)
)
if mibBuilder.loadTexts:
    phMediaTable.setStatus("mandatory")
_PhMediaEntry_Object = MibTableRow
phMediaEntry = _PhMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1)
)
phMediaEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phMediaBarCode"),
)
if mibBuilder.loadTexts:
    phMediaEntry.setStatus("mandatory")
_PhMediaBarCode_Type = AdicBarCode
_PhMediaBarCode_Object = MibTableColumn
phMediaBarCode = _PhMediaBarCode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 1),
    _PhMediaBarCode_Type()
)
phMediaBarCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaBarCode.setStatus("mandatory")
_PhMediaDomain_Type = Integer32
_PhMediaDomain_Object = MibTableColumn
phMediaDomain = _PhMediaDomain_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 2),
    _PhMediaDomain_Type()
)
phMediaDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaDomain.setStatus("mandatory")
_PhMediaType_Type = Integer32
_PhMediaType_Object = MibTableColumn
phMediaType = _PhMediaType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 3),
    _PhMediaType_Type()
)
phMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaType.setStatus("mandatory")
_PhMediaElementAddress_Type = Integer32
_PhMediaElementAddress_Object = MibTableColumn
phMediaElementAddress = _PhMediaElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 4),
    _PhMediaElementAddress_Type()
)
phMediaElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaElementAddress.setStatus("mandatory")
_PhMediaMounts_Type = Integer32
_PhMediaMounts_Object = MibTableColumn
phMediaMounts = _PhMediaMounts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 5),
    _PhMediaMounts_Type()
)
phMediaMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaMounts.setStatus("mandatory")
_PhMediaReadErrors_Type = Integer32
_PhMediaReadErrors_Object = MibTableColumn
phMediaReadErrors = _PhMediaReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 6),
    _PhMediaReadErrors_Type()
)
phMediaReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaReadErrors.setStatus("mandatory")
_PhMediaWriteErrors_Type = Integer32
_PhMediaWriteErrors_Object = MibTableColumn
phMediaWriteErrors = _PhMediaWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 7),
    _PhMediaWriteErrors_Type()
)
phMediaWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaWriteErrors.setStatus("mandatory")
_PhMediaCapacity_Type = Integer32
_PhMediaCapacity_Object = MibTableColumn
phMediaCapacity = _PhMediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 8),
    _PhMediaCapacity_Type()
)
phMediaCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaCapacity.setStatus("mandatory")
_PhMediaFreeSpace_Type = Integer32
_PhMediaFreeSpace_Object = MibTableColumn
phMediaFreeSpace = _PhMediaFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 9),
    _PhMediaFreeSpace_Type()
)
phMediaFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaFreeSpace.setStatus("mandatory")
_PhMediaExported_Type = Boolean
_PhMediaExported_Object = MibTableColumn
phMediaExported = _PhMediaExported_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 10),
    _PhMediaExported_Type()
)
phMediaExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaExported.setStatus("mandatory")
_PhMediaImportTimestamp_Type = AdicDateAndTime
_PhMediaImportTimestamp_Object = MibTableColumn
phMediaImportTimestamp = _PhMediaImportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 11),
    _PhMediaImportTimestamp_Type()
)
phMediaImportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaImportTimestamp.setStatus("mandatory")
_PhMediaExportTimestamp_Type = AdicDateAndTime
_PhMediaExportTimestamp_Object = MibTableColumn
phMediaExportTimestamp = _PhMediaExportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 120, 1, 12),
    _PhMediaExportTimestamp_Type()
)
phMediaExportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phMediaExportTimestamp.setStatus("mandatory")
_PhTransportTable_Object = MibTable
phTransportTable = _PhTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130)
)
if mibBuilder.loadTexts:
    phTransportTable.setStatus("optional")
_PhTransportEntry_Object = MibTableRow
phTransportEntry = _PhTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1)
)
phTransportEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phTransportElementAddress"),
)
if mibBuilder.loadTexts:
    phTransportEntry.setStatus("optional")
_PhTransportElementAddress_Type = Integer32
_PhTransportElementAddress_Object = MibTableColumn
phTransportElementAddress = _PhTransportElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 1),
    _PhTransportElementAddress_Type()
)
phTransportElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportElementAddress.setStatus("optional")
_PhTransportNumRecoveredGets_Type = Integer32
_PhTransportNumRecoveredGets_Object = MibTableColumn
phTransportNumRecoveredGets = _PhTransportNumRecoveredGets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 2),
    _PhTransportNumRecoveredGets_Type()
)
phTransportNumRecoveredGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportNumRecoveredGets.setStatus("optional")
_PhTransportNumRecoveredPuts_Type = Integer32
_PhTransportNumRecoveredPuts_Object = MibTableColumn
phTransportNumRecoveredPuts = _PhTransportNumRecoveredPuts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 3),
    _PhTransportNumRecoveredPuts_Type()
)
phTransportNumRecoveredPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportNumRecoveredPuts.setStatus("optional")
_PhTransportNumRecoveredScans_Type = Integer32
_PhTransportNumRecoveredScans_Object = MibTableColumn
phTransportNumRecoveredScans = _PhTransportNumRecoveredScans_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 4),
    _PhTransportNumRecoveredScans_Type()
)
phTransportNumRecoveredScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportNumRecoveredScans.setStatus("optional")
_PhTransportNumPuts_Type = Integer32
_PhTransportNumPuts_Object = MibTableColumn
phTransportNumPuts = _PhTransportNumPuts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 5),
    _PhTransportNumPuts_Type()
)
phTransportNumPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportNumPuts.setStatus("optional")
_PhTransportREDId_Type = AdicREDIdentifier
_PhTransportREDId_Object = MibTableColumn
phTransportREDId = _PhTransportREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 130, 1, 6),
    _PhTransportREDId_Type()
)
phTransportREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportREDId.setStatus("optional")
_PhTransportDomainTable_Object = MibTable
phTransportDomainTable = _PhTransportDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 132)
)
if mibBuilder.loadTexts:
    phTransportDomainTable.setStatus("optional")
_PhTransportDomainEntry_Object = MibTableRow
phTransportDomainEntry = _PhTransportDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 132, 1)
)
phTransportDomainEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "phTransportElementAddress"),
    (0, "ADIC-MANAGEMENT-MIB", "phTransportDomainIndex"),
)
if mibBuilder.loadTexts:
    phTransportDomainEntry.setStatus("optional")
_PhTransportDomainIndex_Type = Integer32
_PhTransportDomainIndex_Object = MibTableColumn
phTransportDomainIndex = _PhTransportDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 132, 1, 1),
    _PhTransportDomainIndex_Type()
)
phTransportDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phTransportDomainIndex.setStatus("optional")
_PhCleaningMediaTable_Object = MibTable
phCleaningMediaTable = _PhCleaningMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140)
)
if mibBuilder.loadTexts:
    phCleaningMediaTable.setStatus("optional")
_PhCleaningMediaEntry_Object = MibTableRow
phCleaningMediaEntry = _PhCleaningMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1)
)
phCleaningMediaEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "phSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "phCleaningMediaRow"),
)
if mibBuilder.loadTexts:
    phCleaningMediaEntry.setStatus("optional")
_PhCleaningMediaRow_Type = Integer32
_PhCleaningMediaRow_Object = MibTableColumn
phCleaningMediaRow = _PhCleaningMediaRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 1),
    _PhCleaningMediaRow_Type()
)
phCleaningMediaRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phCleaningMediaRow.setStatus("optional")


class _PhCleaningMediaStatus_Type(Integer32):
    """Custom type phCleaningMediaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 1),
          ("unallocated", 2))
    )


_PhCleaningMediaStatus_Type.__name__ = "Integer32"
_PhCleaningMediaStatus_Object = MibTableColumn
phCleaningMediaStatus = _PhCleaningMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 2),
    _PhCleaningMediaStatus_Type()
)
phCleaningMediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phCleaningMediaStatus.setStatus("optional")
_PhCleaningMediaTypeIndex_Type = Integer32
_PhCleaningMediaTypeIndex_Object = MibTableColumn
phCleaningMediaTypeIndex = _PhCleaningMediaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 3),
    _PhCleaningMediaTypeIndex_Type()
)
phCleaningMediaTypeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningMediaTypeIndex.setStatus("optional")
_PhCleaningMediaVendorId_Type = DisplayString
_PhCleaningMediaVendorId_Object = MibTableColumn
phCleaningMediaVendorId = _PhCleaningMediaVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 4),
    _PhCleaningMediaVendorId_Type()
)
phCleaningMediaVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningMediaVendorId.setStatus("optional")
_PhCleaningMediaBarcode_Type = AdicBarCode
_PhCleaningMediaBarcode_Object = MibTableColumn
phCleaningMediaBarcode = _PhCleaningMediaBarcode_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 5),
    _PhCleaningMediaBarcode_Type()
)
phCleaningMediaBarcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningMediaBarcode.setStatus("optional")
_PhCleaningMediaUseCount_Type = Integer32
_PhCleaningMediaUseCount_Object = MibTableColumn
phCleaningMediaUseCount = _PhCleaningMediaUseCount_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 6),
    _PhCleaningMediaUseCount_Type()
)
phCleaningMediaUseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningMediaUseCount.setStatus("optional")
_PhCleaningMediaMaxUses_Type = Integer32
_PhCleaningMediaMaxUses_Object = MibTableColumn
phCleaningMediaMaxUses = _PhCleaningMediaMaxUses_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 7),
    _PhCleaningMediaMaxUses_Type()
)
phCleaningMediaMaxUses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phCleaningMediaMaxUses.setStatus("optional")
_PhCleaningMediaImportTimestamp_Type = AdicDateAndTime
_PhCleaningMediaImportTimestamp_Object = MibTableColumn
phCleaningMediaImportTimestamp = _PhCleaningMediaImportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 80, 140, 1, 8),
    _PhCleaningMediaImportTimestamp_Type()
)
phCleaningMediaImportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phCleaningMediaImportTimestamp.setStatus("optional")
_LogicalLibrary_ObjectIdentity = ObjectIdentity
logicalLibrary = _LogicalLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90)
)
_LoGeneralInfoTable_Object = MibTable
loGeneralInfoTable = _LoGeneralInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10)
)
if mibBuilder.loadTexts:
    loGeneralInfoTable.setStatus("mandatory")
_LoGeneralInfoEntry_Object = MibTableRow
loGeneralInfoEntry = _LoGeneralInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10, 1)
)
loGeneralInfoEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    loGeneralInfoEntry.setStatus("mandatory")
_MaxLogicalLibraries_Type = Integer32
_MaxLogicalLibraries_Object = MibTableColumn
maxLogicalLibraries = _MaxLogicalLibraries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10, 1, 1),
    _MaxLogicalLibraries_Type()
)
maxLogicalLibraries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLogicalLibraries.setStatus("mandatory")
_NumLogicalLibraries_Type = Integer32
_NumLogicalLibraries_Object = MibTableColumn
numLogicalLibraries = _NumLogicalLibraries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10, 1, 2),
    _NumLogicalLibraries_Type()
)
numLogicalLibraries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLogicalLibraries.setStatus("mandatory")


class _MasterOnlineStatus_Type(Integer32):
    """Custom type masterOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_MasterOnlineStatus_Type.__name__ = "Integer32"
_MasterOnlineStatus_Object = MibTableColumn
masterOnlineStatus = _MasterOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10, 1, 3),
    _MasterOnlineStatus_Type()
)
masterOnlineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterOnlineStatus.setStatus("mandatory")
_NumVendorIds_Type = Integer32
_NumVendorIds_Object = MibTableColumn
numVendorIds = _NumVendorIds_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 10, 1, 4),
    _NumVendorIds_Type()
)
numVendorIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numVendorIds.setStatus("mandatory")
_AutoPartitionTable_Object = MibTable
autoPartitionTable = _AutoPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 12)
)
if mibBuilder.loadTexts:
    autoPartitionTable.setStatus("mandatory")
_AutoPartitionEntry_Object = MibTableRow
autoPartitionEntry = _AutoPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 12, 1)
)
autoPartitionEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaDomainIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "mediaTypeIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "phDriveInterfaceType"),
)
if mibBuilder.loadTexts:
    autoPartitionEntry.setStatus("mandatory")
_NumAutoPartition_Type = Integer32
_NumAutoPartition_Object = MibTableColumn
numAutoPartition = _NumAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 12, 1, 1),
    _NumAutoPartition_Type()
)
numAutoPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numAutoPartition.setStatus("mandatory")


class _AutoPartitionCommand_Type(Integer32):
    """Custom type autoPartitionCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoPartition", 1)
    )


_AutoPartitionCommand_Type.__name__ = "Integer32"
_AutoPartitionCommand_Object = MibTableColumn
autoPartitionCommand = _AutoPartitionCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 12, 1, 2),
    _AutoPartitionCommand_Type()
)
autoPartitionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoPartitionCommand.setStatus("mandatory")
_VendorIdTable_Object = MibTable
vendorIdTable = _VendorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 15)
)
if mibBuilder.loadTexts:
    vendorIdTable.setStatus("mandatory")
_VendorIdEntry_Object = MibTableRow
vendorIdEntry = _VendorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 15, 1)
)
vendorIdEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "vendorIdIndex"),
)
if mibBuilder.loadTexts:
    vendorIdEntry.setStatus("mandatory")
_VendorIdIndex_Type = Integer32
_VendorIdIndex_Object = MibTableColumn
vendorIdIndex = _VendorIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 15, 1, 1),
    _VendorIdIndex_Type()
)
vendorIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorIdIndex.setStatus("mandatory")
_VendorName_Type = DisplayString
_VendorName_Object = MibTableColumn
vendorName = _VendorName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 15, 1, 2),
    _VendorName_Type()
)
vendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorName.setStatus("mandatory")
_NumProductIds_Type = Integer32
_NumProductIds_Object = MibTableColumn
numProductIds = _NumProductIds_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 15, 1, 3),
    _NumProductIds_Type()
)
numProductIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numProductIds.setStatus("mandatory")
_ProductIdTable_Object = MibTable
productIdTable = _ProductIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17)
)
if mibBuilder.loadTexts:
    productIdTable.setStatus("mandatory")
_ProductIdEntry_Object = MibTableRow
productIdEntry = _ProductIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1)
)
productIdEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "vendorIdIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "productIdIndex"),
)
if mibBuilder.loadTexts:
    productIdEntry.setStatus("mandatory")
_ProductIdIndex_Type = Integer32
_ProductIdIndex_Object = MibTableColumn
productIdIndex = _ProductIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 1),
    _ProductIdIndex_Type()
)
productIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIdIndex.setStatus("mandatory")
_ProductIdName_Type = DisplayString
_ProductIdName_Object = MibTableColumn
productIdName = _ProductIdName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 2),
    _ProductIdName_Type()
)
productIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIdName.setStatus("mandatory")
_ProductDrivesMin_Type = Integer32
_ProductDrivesMin_Object = MibTableColumn
productDrivesMin = _ProductDrivesMin_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 3),
    _ProductDrivesMin_Type()
)
productDrivesMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productDrivesMin.setStatus("mandatory")
_ProductDrivesMax_Type = Integer32
_ProductDrivesMax_Object = MibTableColumn
productDrivesMax = _ProductDrivesMax_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 4),
    _ProductDrivesMax_Type()
)
productDrivesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productDrivesMax.setStatus("mandatory")
_ProductSlotsMin_Type = Integer32
_ProductSlotsMin_Object = MibTableColumn
productSlotsMin = _ProductSlotsMin_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 5),
    _ProductSlotsMin_Type()
)
productSlotsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productSlotsMin.setStatus("mandatory")
_ProductSlotsMax_Type = Integer32
_ProductSlotsMax_Object = MibTableColumn
productSlotsMax = _ProductSlotsMax_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 6),
    _ProductSlotsMax_Type()
)
productSlotsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productSlotsMax.setStatus("mandatory")
_ProductIeMin_Type = Integer32
_ProductIeMin_Object = MibTableColumn
productIeMin = _ProductIeMin_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 7),
    _ProductIeMin_Type()
)
productIeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIeMin.setStatus("mandatory")
_ProductIeMax_Type = Integer32
_ProductIeMax_Object = MibTableColumn
productIeMax = _ProductIeMax_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 17, 1, 8),
    _ProductIeMax_Type()
)
productIeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productIeMax.setStatus("mandatory")
_LogicalLibraryTable_Object = MibTable
logicalLibraryTable = _LogicalLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20)
)
if mibBuilder.loadTexts:
    logicalLibraryTable.setStatus("mandatory")
_LogicalLibraryEntry_Object = MibTableRow
logicalLibraryEntry = _LogicalLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1)
)
logicalLibraryEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
)
if mibBuilder.loadTexts:
    logicalLibraryEntry.setStatus("mandatory")
_LogicalLibraryIndex_Type = Integer32
_LogicalLibraryIndex_Object = MibTableColumn
logicalLibraryIndex = _LogicalLibraryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 1),
    _LogicalLibraryIndex_Type()
)
logicalLibraryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalLibraryIndex.setStatus("mandatory")


class _Command_Type(Integer32):
    """Custom type command based on Integer32"""
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
        *(("createExpert", 2),
          ("createSimple", 1),
          ("delete", 4),
          ("modify", 3))
    )


_Command_Type.__name__ = "Integer32"
_Command_Object = MibTableColumn
command = _Command_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 2),
    _Command_Type()
)
command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    command.setStatus("mandatory")
_Name_Type = DisplayString
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 3),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_AssignedLun_Type = Integer32
_AssignedLun_Object = MibTableColumn
assignedLun = _AssignedLun_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 4),
    _AssignedLun_Type()
)
assignedLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assignedLun.setStatus("mandatory")
_VendorId_Type = DisplayString
_VendorId_Object = MibTableColumn
vendorId = _VendorId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 5),
    _VendorId_Type()
)
vendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorId.setStatus("mandatory")
_ProductId_Type = DisplayString
_ProductId_Object = MibTableColumn
productId = _ProductId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 6),
    _ProductId_Type()
)
productId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productId.setStatus("mandatory")
_MediaDomain_Type = Integer32
_MediaDomain_Object = MibTableColumn
mediaDomain = _MediaDomain_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 7),
    _MediaDomain_Type()
)
mediaDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaDomain.setStatus("mandatory")
_MediaType_Type = Integer32
_MediaType_Object = MibTableColumn
mediaType = _MediaType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 8),
    _MediaType_Type()
)
mediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaType.setStatus("mandatory")
_NumSlots_Type = Integer32
_NumSlots_Object = MibTableColumn
numSlots = _NumSlots_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 9),
    _NumSlots_Type()
)
numSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numSlots.setStatus("mandatory")
_NumIE_Type = Integer32
_NumIE_Object = MibTableColumn
numIE = _NumIE_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 10),
    _NumIE_Type()
)
numIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numIE.setStatus("mandatory")
_NumDrives_Type = Integer32
_NumDrives_Object = MibTableColumn
numDrives = _NumDrives_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 11),
    _NumDrives_Type()
)
numDrives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numDrives.setStatus("mandatory")


class _LoStatus_Type(Integer32):
    """Custom type loStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_LoStatus_Type.__name__ = "Integer32"
_LoStatus_Object = MibTableColumn
loStatus = _LoStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 12),
    _LoStatus_Type()
)
loStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loStatus.setStatus("mandatory")
_AutomaticCleaning_Type = AdicEnable
_AutomaticCleaning_Object = MibTableColumn
automaticCleaning = _AutomaticCleaning_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 13),
    _AutomaticCleaning_Type()
)
automaticCleaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automaticCleaning.setStatus("mandatory")
_MediaTypeChecking_Type = AdicEnable
_MediaTypeChecking_Object = MibTableColumn
mediaTypeChecking = _MediaTypeChecking_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 14),
    _MediaTypeChecking_Type()
)
mediaTypeChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTypeChecking.setStatus("mandatory")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 15),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_LoInterfaceType_Type = AdicInterfaceType
_LoInterfaceType_Object = MibTableColumn
loInterfaceType = _LoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 16),
    _LoInterfaceType_Type()
)
loInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loInterfaceType.setStatus("mandatory")
_LoNumLibraries_Type = Integer32
_LoNumLibraries_Object = MibTableColumn
loNumLibraries = _LoNumLibraries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 17),
    _LoNumLibraries_Type()
)
loNumLibraries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loNumLibraries.setStatus("obsolete")


class _LoLtoTapeTags_Type(Integer32):
    """Custom type loLtoTapeTags based on Integer32"""
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
          ("prefix", 1),
          ("suffix", 2))
    )


_LoLtoTapeTags_Type.__name__ = "Integer32"
_LoLtoTapeTags_Object = MibTableColumn
loLtoTapeTags = _LoLtoTapeTags_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 18),
    _LoLtoTapeTags_Type()
)
loLtoTapeTags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loLtoTapeTags.setStatus("mandatory")
_LoMediaTypeCheckingPolicy_Type = Integer32
_LoMediaTypeCheckingPolicy_Object = MibTableColumn
loMediaTypeCheckingPolicy = _LoMediaTypeCheckingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 20, 1, 19),
    _LoMediaTypeCheckingPolicy_Type()
)
loMediaTypeCheckingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loMediaTypeCheckingPolicy.setStatus("mandatory")
_LoSegmentTable_Object = MibTable
loSegmentTable = _LoSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25)
)
if mibBuilder.loadTexts:
    loSegmentTable.setStatus("mandatory")
_LoSegmentEntry_Object = MibTableRow
loSegmentEntry = _LoSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1)
)
loSegmentEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentType"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    loSegmentEntry.setStatus("mandatory")
_LoSegmentAisle_Type = Integer32
_LoSegmentAisle_Object = MibTableColumn
loSegmentAisle = _LoSegmentAisle_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 1),
    _LoSegmentAisle_Type()
)
loSegmentAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentAisle.setStatus("mandatory")
_LoSegmentFrame_Type = Integer32
_LoSegmentFrame_Object = MibTableColumn
loSegmentFrame = _LoSegmentFrame_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 2),
    _LoSegmentFrame_Type()
)
loSegmentFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentFrame.setStatus("mandatory")
_LoSegmentRack_Type = Integer32
_LoSegmentRack_Object = MibTableColumn
loSegmentRack = _LoSegmentRack_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 3),
    _LoSegmentRack_Type()
)
loSegmentRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentRack.setStatus("mandatory")
_LoSegmentSection_Type = Integer32
_LoSegmentSection_Object = MibTableColumn
loSegmentSection = _LoSegmentSection_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 4),
    _LoSegmentSection_Type()
)
loSegmentSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentSection.setStatus("mandatory")
_LoSegmentCol_Type = Integer32
_LoSegmentCol_Object = MibTableColumn
loSegmentCol = _LoSegmentCol_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 5),
    _LoSegmentCol_Type()
)
loSegmentCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentCol.setStatus("mandatory")
_LoSegmentStartingRow_Type = Integer32
_LoSegmentStartingRow_Object = MibTableColumn
loSegmentStartingRow = _LoSegmentStartingRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 6),
    _LoSegmentStartingRow_Type()
)
loSegmentStartingRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentStartingRow.setStatus("mandatory")
_LoSegmentSize_Type = Integer32
_LoSegmentSize_Object = MibTableColumn
loSegmentSize = _LoSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 7),
    _LoSegmentSize_Type()
)
loSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentSize.setStatus("mandatory")
_LoSegmentType_Type = AdicSegmentType
_LoSegmentType_Object = MibTableColumn
loSegmentType = _LoSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 8),
    _LoSegmentType_Type()
)
loSegmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentType.setStatus("mandatory")
_LoSegmentMediaDomain_Type = Integer32
_LoSegmentMediaDomain_Object = MibTableColumn
loSegmentMediaDomain = _LoSegmentMediaDomain_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 9),
    _LoSegmentMediaDomain_Type()
)
loSegmentMediaDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentMediaDomain.setStatus("mandatory")
_LoSegmentBelongsTo_Type = Integer32
_LoSegmentBelongsTo_Object = MibTableColumn
loSegmentBelongsTo = _LoSegmentBelongsTo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 10),
    _LoSegmentBelongsTo_Type()
)
loSegmentBelongsTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loSegmentBelongsTo.setStatus("mandatory")


class _LoSegmentCommand_Type(Integer32):
    """Custom type loSegmentCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allocate", 1),
          ("free", 2),
          ("reserveForCleaning", 3))
    )


_LoSegmentCommand_Type.__name__ = "Integer32"
_LoSegmentCommand_Object = MibTableColumn
loSegmentCommand = _LoSegmentCommand_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 11),
    _LoSegmentCommand_Type()
)
loSegmentCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loSegmentCommand.setStatus("mandatory")


class _LoSegmentStatus_Type(Integer32):
    """Custom type loSegmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 1),
          ("unallocated", 2))
    )


_LoSegmentStatus_Type.__name__ = "Integer32"
_LoSegmentStatus_Object = MibTableColumn
loSegmentStatus = _LoSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 12),
    _LoSegmentStatus_Type()
)
loSegmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentStatus.setStatus("mandatory")
_LoSegmentStartingAddress_Type = Integer32
_LoSegmentStartingAddress_Object = MibTableColumn
loSegmentStartingAddress = _LoSegmentStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 25, 1, 13),
    _LoSegmentStartingAddress_Type()
)
loSegmentStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentStartingAddress.setStatus("mandatory")
_LoSegmentBelongsToTable_Object = MibTable
loSegmentBelongsToTable = _LoSegmentBelongsToTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 27)
)
if mibBuilder.loadTexts:
    loSegmentBelongsToTable.setStatus("mandatory")
_LoSegmentBelongsToEntry_Object = MibTableRow
loSegmentBelongsToEntry = _LoSegmentBelongsToEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 27, 1)
)
loSegmentBelongsToEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentType"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentStartingRow"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAssignedTo"),
)
if mibBuilder.loadTexts:
    loSegmentBelongsToEntry.setStatus("mandatory")
_LoSegmentAssignedTo_Type = Integer32
_LoSegmentAssignedTo_Object = MibTableColumn
loSegmentAssignedTo = _LoSegmentAssignedTo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 27, 1, 1),
    _LoSegmentAssignedTo_Type()
)
loSegmentAssignedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loSegmentAssignedTo.setStatus("mandatory")
_LoStorageSegTable_Object = MibTable
loStorageSegTable = _LoStorageSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 30)
)
if mibBuilder.loadTexts:
    loStorageSegTable.setStatus("mandatory")
_LoStorageSegEntry_Object = MibTableRow
loStorageSegEntry = _LoStorageSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 30, 1)
)
loStorageSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    loStorageSegEntry.setStatus("mandatory")
_LoStorageSegSize_Type = Integer32
_LoStorageSegSize_Object = MibTableColumn
loStorageSegSize = _LoStorageSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 30, 1, 1),
    _LoStorageSegSize_Type()
)
loStorageSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStorageSegSize.setStatus("mandatory")
_LoStorageSegStartingAddress_Type = Integer32
_LoStorageSegStartingAddress_Object = MibTableColumn
loStorageSegStartingAddress = _LoStorageSegStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 30, 1, 2),
    _LoStorageSegStartingAddress_Type()
)
loStorageSegStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStorageSegStartingAddress.setStatus("mandatory")
_LoIeSegTable_Object = MibTable
loIeSegTable = _LoIeSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40)
)
if mibBuilder.loadTexts:
    loIeSegTable.setStatus("mandatory")
_LoIeSegEntry_Object = MibTableRow
loIeSegEntry = _LoIeSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40, 1)
)
loIeSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    loIeSegEntry.setStatus("mandatory")
_LoIeSegSize_Type = Integer32
_LoIeSegSize_Object = MibTableColumn
loIeSegSize = _LoIeSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40, 1, 1),
    _LoIeSegSize_Type()
)
loIeSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loIeSegSize.setStatus("mandatory")


class _LoIeSegReserve_Type(Integer32):
    """Custom type loIeSegReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 2),
          ("reserve", 1))
    )


_LoIeSegReserve_Type.__name__ = "Integer32"
_LoIeSegReserve_Object = MibTableColumn
loIeSegReserve = _LoIeSegReserve_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40, 1, 2),
    _LoIeSegReserve_Type()
)
loIeSegReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loIeSegReserve.setStatus("mandatory")
_LoIeSegReservedBy_Type = Integer32
_LoIeSegReservedBy_Object = MibTableColumn
loIeSegReservedBy = _LoIeSegReservedBy_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40, 1, 3),
    _LoIeSegReservedBy_Type()
)
loIeSegReservedBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loIeSegReservedBy.setStatus("mandatory")
_LoIeSegStartingAddress_Type = Integer32
_LoIeSegStartingAddress_Object = MibTableColumn
loIeSegStartingAddress = _LoIeSegStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 40, 1, 4),
    _LoIeSegStartingAddress_Type()
)
loIeSegStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loIeSegStartingAddress.setStatus("mandatory")
_LoDriveSegTable_Object = MibTable
loDriveSegTable = _LoDriveSegTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50)
)
if mibBuilder.loadTexts:
    loDriveSegTable.setStatus("mandatory")
_LoDriveSegEntry_Object = MibTableRow
loDriveSegEntry = _LoDriveSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50, 1)
)
loDriveSegEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentStartingRow"),
)
if mibBuilder.loadTexts:
    loDriveSegEntry.setStatus("mandatory")
_LoDriveSegSize_Type = Integer32
_LoDriveSegSize_Object = MibTableColumn
loDriveSegSize = _LoDriveSegSize_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50, 1, 1),
    _LoDriveSegSize_Type()
)
loDriveSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loDriveSegSize.setStatus("mandatory")
_LoDriveSegStartingAddress_Type = Integer32
_LoDriveSegStartingAddress_Object = MibTableColumn
loDriveSegStartingAddress = _LoDriveSegStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50, 1, 2),
    _LoDriveSegStartingAddress_Type()
)
loDriveSegStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loDriveSegStartingAddress.setStatus("mandatory")
_LoDriveSegMediaType_Type = Integer32
_LoDriveSegMediaType_Object = MibTableColumn
loDriveSegMediaType = _LoDriveSegMediaType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50, 1, 3),
    _LoDriveSegMediaType_Type()
)
loDriveSegMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loDriveSegMediaType.setStatus("mandatory")
_LoDriveSegInterfaceType_Type = AdicInterfaceType
_LoDriveSegInterfaceType_Object = MibTableColumn
loDriveSegInterfaceType = _LoDriveSegInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 50, 1, 4),
    _LoDriveSegInterfaceType_Type()
)
loDriveSegInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loDriveSegInterfaceType.setStatus("mandatory")
_LoStorageSlotTable_Object = MibTable
loStorageSlotTable = _LoStorageSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 60)
)
if mibBuilder.loadTexts:
    loStorageSlotTable.setStatus("mandatory")
_LoStorageSlotEntry_Object = MibTableRow
loStorageSlotEntry = _LoStorageSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 60, 1)
)
loStorageSlotEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loStorageRow"),
)
if mibBuilder.loadTexts:
    loStorageSlotEntry.setStatus("mandatory")
_LoStorageRow_Type = Integer32
_LoStorageRow_Object = MibTableColumn
loStorageRow = _LoStorageRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 60, 1, 1),
    _LoStorageRow_Type()
)
loStorageRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStorageRow.setStatus("mandatory")
_LoIeSlotTable_Object = MibTable
loIeSlotTable = _LoIeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 70)
)
if mibBuilder.loadTexts:
    loIeSlotTable.setStatus("mandatory")
_LoIeSlotEntry_Object = MibTableRow
loIeSlotEntry = _LoIeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 70, 1)
)
loIeSlotEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loIeRow"),
)
if mibBuilder.loadTexts:
    loIeSlotEntry.setStatus("mandatory")
_LoIeRow_Type = Integer32
_LoIeRow_Object = MibTableColumn
loIeRow = _LoIeRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 70, 1, 1),
    _LoIeRow_Type()
)
loIeRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loIeRow.setStatus("mandatory")
_LoDriveTable_Object = MibTable
loDriveTable = _LoDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 80)
)
if mibBuilder.loadTexts:
    loDriveTable.setStatus("mandatory")
_LoDriveEntry_Object = MibTableRow
loDriveEntry = _LoDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 80, 1)
)
loDriveEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentAisle"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentFrame"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentRack"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentSection"),
    (0, "ADIC-MANAGEMENT-MIB", "loSegmentCol"),
    (0, "ADIC-MANAGEMENT-MIB", "loDriveRow"),
)
if mibBuilder.loadTexts:
    loDriveEntry.setStatus("mandatory")
_LoDriveRow_Type = Integer32
_LoDriveRow_Object = MibTableColumn
loDriveRow = _LoDriveRow_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 80, 1, 1),
    _LoDriveRow_Type()
)
loDriveRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loDriveRow.setStatus("mandatory")
_LoStatisticsTable_Object = MibTable
loStatisticsTable = _LoStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90)
)
if mibBuilder.loadTexts:
    loStatisticsTable.setStatus("optional")
_LoStatisticsEntry_Object = MibTableRow
loStatisticsEntry = _LoStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1)
)
loStatisticsEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
)
if mibBuilder.loadTexts:
    loStatisticsEntry.setStatus("optional")
_LoNumRecoveredGets_Type = Integer32
_LoNumRecoveredGets_Object = MibTableColumn
loNumRecoveredGets = _LoNumRecoveredGets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 1),
    _LoNumRecoveredGets_Type()
)
loNumRecoveredGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loNumRecoveredGets.setStatus("optional")
_LoNumRecoveredPuts_Type = Integer32
_LoNumRecoveredPuts_Object = MibTableColumn
loNumRecoveredPuts = _LoNumRecoveredPuts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 2),
    _LoNumRecoveredPuts_Type()
)
loNumRecoveredPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loNumRecoveredPuts.setStatus("optional")
_LoNumRecoveredScans_Type = Integer32
_LoNumRecoveredScans_Object = MibTableColumn
loNumRecoveredScans = _LoNumRecoveredScans_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 3),
    _LoNumRecoveredScans_Type()
)
loNumRecoveredScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loNumRecoveredScans.setStatus("optional")
_LoStatsNumPuts_Type = Integer32
_LoStatsNumPuts_Object = MibTableColumn
loStatsNumPuts = _LoStatsNumPuts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 4),
    _LoStatsNumPuts_Type()
)
loStatsNumPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStatsNumPuts.setStatus("optional")
_LoStatsNumPutRetries_Type = Integer32
_LoStatsNumPutRetries_Object = MibTableColumn
loStatsNumPutRetries = _LoStatsNumPutRetries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 5),
    _LoStatsNumPutRetries_Type()
)
loStatsNumPutRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStatsNumPutRetries.setStatus("optional")
_LoStatsNumGetRetries_Type = Integer32
_LoStatsNumGetRetries_Object = MibTableColumn
loStatsNumGetRetries = _LoStatsNumGetRetries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 6),
    _LoStatsNumGetRetries_Type()
)
loStatsNumGetRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStatsNumGetRetries.setStatus("optional")
_LoStatsNumScanRetries_Type = Integer32
_LoStatsNumScanRetries_Object = MibTableColumn
loStatsNumScanRetries = _LoStatsNumScanRetries_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 90, 90, 1, 7),
    _LoStatsNumScanRetries_Type()
)
loStatsNumScanRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loStatsNumScanRetries.setStatus("optional")
_Ras_ObjectIdentity = ObjectIdentity
ras = _Ras_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100)
)
_RasSystemStatusTable_Object = MibTable
rasSystemStatusTable = _RasSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10)
)
if mibBuilder.loadTexts:
    rasSystemStatusTable.setStatus("mandatory")
_RasSystemStatusEntry_Object = MibTableRow
rasSystemStatusEntry = _RasSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1)
)
rasSystemStatusEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
)
if mibBuilder.loadTexts:
    rasSystemStatusEntry.setStatus("mandatory")
_RasStatusGroupIndex_Type = AdicStatusGroup
_RasStatusGroupIndex_Object = MibTableColumn
rasStatusGroupIndex = _RasStatusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 1),
    _RasStatusGroupIndex_Type()
)
rasStatusGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupIndex.setStatus("mandatory")
_RasStatusGroupStatus_Type = AdicStatusGroupState
_RasStatusGroupStatus_Object = MibTableColumn
rasStatusGroupStatus = _RasStatusGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 2),
    _RasStatusGroupStatus_Type()
)
rasStatusGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupStatus.setStatus("mandatory")
_RasStatusGroupPreviousStatus_Type = AdicStatusGroupState
_RasStatusGroupPreviousStatus_Object = MibTableColumn
rasStatusGroupPreviousStatus = _RasStatusGroupPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 3),
    _RasStatusGroupPreviousStatus_Type()
)
rasStatusGroupPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupPreviousStatus.setStatus("mandatory")
_RasStatusGroupTextSummary_Type = DisplayString
_RasStatusGroupTextSummary_Object = MibTableColumn
rasStatusGroupTextSummary = _RasStatusGroupTextSummary_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 4),
    _RasStatusGroupTextSummary_Type()
)
rasStatusGroupTextSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupTextSummary.setStatus("mandatory")
_RasStatusGroupTotalTickets_Type = Integer32
_RasStatusGroupTotalTickets_Object = MibTableColumn
rasStatusGroupTotalTickets = _RasStatusGroupTotalTickets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 5),
    _RasStatusGroupTotalTickets_Type()
)
rasStatusGroupTotalTickets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupTotalTickets.setStatus("mandatory")
_RasStatusGroupOpenTickets_Type = Integer32
_RasStatusGroupOpenTickets_Object = MibTableColumn
rasStatusGroupOpenTickets = _RasStatusGroupOpenTickets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 6),
    _RasStatusGroupOpenTickets_Type()
)
rasStatusGroupOpenTickets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupOpenTickets.setStatus("mandatory")
_RasStatusGroupActionsPending_Type = Integer32
_RasStatusGroupActionsPending_Object = MibTableColumn
rasStatusGroupActionsPending = _RasStatusGroupActionsPending_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 7),
    _RasStatusGroupActionsPending_Type()
)
rasStatusGroupActionsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupActionsPending.setStatus("mandatory")
_RasStatusGroupLastChange_Type = AdicDateAndTime
_RasStatusGroupLastChange_Object = MibTableColumn
rasStatusGroupLastChange = _RasStatusGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 10, 1, 8),
    _RasStatusGroupLastChange_Type()
)
rasStatusGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatusGroupLastChange.setStatus("mandatory")
_RasTicketTable_Object = MibTable
rasTicketTable = _RasTicketTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20)
)
if mibBuilder.loadTexts:
    rasTicketTable.setStatus("mandatory")
_RasTicketEntry_Object = MibTableRow
rasTicketEntry = _RasTicketEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1)
)
rasTicketEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "rasTicketId"),
)
if mibBuilder.loadTexts:
    rasTicketEntry.setStatus("mandatory")
_RasTicketId_Type = Gauge32
_RasTicketId_Object = MibTableColumn
rasTicketId = _RasTicketId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 1),
    _RasTicketId_Type()
)
rasTicketId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketId.setStatus("mandatory")
_RasTicketRowStatus_Type = RowStatus
_RasTicketRowStatus_Object = MibTableColumn
rasTicketRowStatus = _RasTicketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 2),
    _RasTicketRowStatus_Type()
)
rasTicketRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketRowStatus.setStatus("mandatory")
_RasTicketState_Type = AdicRasTicketState
_RasTicketState_Object = MibTableColumn
rasTicketState = _RasTicketState_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 3),
    _RasTicketState_Type()
)
rasTicketState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketState.setStatus("mandatory")


class _RasTicketQualifier_Type(Integer32):
    """Custom type rasTicketQualifier based on Integer32"""
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
        *(("asDesigned", 4),
          ("cannotDuplicate", 3),
          ("manualOverride", 5),
          ("none", 1),
          ("resolved", 2))
    )


_RasTicketQualifier_Type.__name__ = "Integer32"
_RasTicketQualifier_Object = MibTableColumn
rasTicketQualifier = _RasTicketQualifier_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 4),
    _RasTicketQualifier_Type()
)
rasTicketQualifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketQualifier.setStatus("mandatory")
_RasTicketPriority_Type = Integer32
_RasTicketPriority_Object = MibTableColumn
rasTicketPriority = _RasTicketPriority_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 5),
    _RasTicketPriority_Type()
)
rasTicketPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketPriority.setStatus("mandatory")
_RasTicketDescription_Type = DisplayString
_RasTicketDescription_Object = MibTableColumn
rasTicketDescription = _RasTicketDescription_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 6),
    _RasTicketDescription_Type()
)
rasTicketDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketDescription.setStatus("mandatory")
_RasTicketStatusGroup_Type = AdicStatusGroup
_RasTicketStatusGroup_Object = MibTableColumn
rasTicketStatusGroup = _RasTicketStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 7),
    _RasTicketStatusGroup_Type()
)
rasTicketStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketStatusGroup.setStatus("mandatory")
_RasTicketGroupStatus_Type = AdicStatusGroupState
_RasTicketGroupStatus_Object = MibTableColumn
rasTicketGroupStatus = _RasTicketGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 8),
    _RasTicketGroupStatus_Type()
)
rasTicketGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketGroupStatus.setStatus("mandatory")
_RasTicketClosedBy_Type = Integer32
_RasTicketClosedBy_Object = MibTableColumn
rasTicketClosedBy = _RasTicketClosedBy_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 9),
    _RasTicketClosedBy_Type()
)
rasTicketClosedBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketClosedBy.setStatus("mandatory")
_RasTicketVerifiedBy_Type = Integer32
_RasTicketVerifiedBy_Object = MibTableColumn
rasTicketVerifiedBy = _RasTicketVerifiedBy_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 10),
    _RasTicketVerifiedBy_Type()
)
rasTicketVerifiedBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketVerifiedBy.setStatus("mandatory")
_RasTicketComments_Type = DisplayString
_RasTicketComments_Object = MibTableColumn
rasTicketComments = _RasTicketComments_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 11),
    _RasTicketComments_Type()
)
rasTicketComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketComments.setStatus("mandatory")
_RasTicketSerialNumber_Type = AdicFruSerialNumber
_RasTicketSerialNumber_Object = MibTableColumn
rasTicketSerialNumber = _RasTicketSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 12),
    _RasTicketSerialNumber_Type()
)
rasTicketSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketSerialNumber.setStatus("mandatory")
_RasTicketTimeOpened_Type = AdicDateAndTime
_RasTicketTimeOpened_Object = MibTableColumn
rasTicketTimeOpened = _RasTicketTimeOpened_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 13),
    _RasTicketTimeOpened_Type()
)
rasTicketTimeOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketTimeOpened.setStatus("mandatory")
_RasTicketTimeClosed_Type = AdicDateAndTime
_RasTicketTimeClosed_Object = MibTableColumn
rasTicketTimeClosed = _RasTicketTimeClosed_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 14),
    _RasTicketTimeClosed_Type()
)
rasTicketTimeClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketTimeClosed.setStatus("mandatory")
_RasTicketCount_Type = Integer32
_RasTicketCount_Object = MibTableColumn
rasTicketCount = _RasTicketCount_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 15),
    _RasTicketCount_Type()
)
rasTicketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketCount.setStatus("mandatory")
_RasTicketKeyReport_Type = Integer32
_RasTicketKeyReport_Object = MibTableColumn
rasTicketKeyReport = _RasTicketKeyReport_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 20, 1, 16),
    _RasTicketKeyReport_Type()
)
rasTicketKeyReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasTicketKeyReport.setStatus("mandatory")
_RasReportTable_Object = MibTable
rasReportTable = _RasReportTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30)
)
if mibBuilder.loadTexts:
    rasReportTable.setStatus("mandatory")
_RasReportEntry_Object = MibTableRow
rasReportEntry = _RasReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1)
)
rasReportEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "rasTicketId"),
    (0, "ADIC-MANAGEMENT-MIB", "rasReportId"),
)
if mibBuilder.loadTexts:
    rasReportEntry.setStatus("mandatory")
_RasReportId_Type = Gauge32
_RasReportId_Object = MibTableColumn
rasReportId = _RasReportId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 1),
    _RasReportId_Type()
)
rasReportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportId.setStatus("mandatory")
_RasReportRowStatus_Type = RowStatus
_RasReportRowStatus_Object = MibTableColumn
rasReportRowStatus = _RasReportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 2),
    _RasReportRowStatus_Type()
)
rasReportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasReportRowStatus.setStatus("mandatory")
_RasReportTimestamp_Type = AdicDateAndTime
_RasReportTimestamp_Object = MibTableColumn
rasReportTimestamp = _RasReportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 3),
    _RasReportTimestamp_Type()
)
rasReportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportTimestamp.setStatus("mandatory")
_RasReportStatusGroup_Type = AdicStatusGroup
_RasReportStatusGroup_Object = MibTableColumn
rasReportStatusGroup = _RasReportStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 4),
    _RasReportStatusGroup_Type()
)
rasReportStatusGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasReportStatusGroup.setStatus("mandatory")


class _RasReportOrcData_Type(OctetString):
    """Custom type rasReportOrcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_RasReportOrcData_Type.__name__ = "OctetString"
_RasReportOrcData_Object = MibTableColumn
rasReportOrcData = _RasReportOrcData_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 5),
    _RasReportOrcData_Type()
)
rasReportOrcData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasReportOrcData.setStatus("mandatory")
_RasReportGroupStatus_Type = AdicStatusGroupState
_RasReportGroupStatus_Object = MibTableColumn
rasReportGroupStatus = _RasReportGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 6),
    _RasReportGroupStatus_Type()
)
rasReportGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasReportGroupStatus.setStatus("mandatory")
_RasReportDescription_Type = DisplayString
_RasReportDescription_Object = MibTableColumn
rasReportDescription = _RasReportDescription_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 7),
    _RasReportDescription_Type()
)
rasReportDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasReportDescription.setStatus("mandatory")
_RasReportOrcDescription_Type = DisplayString
_RasReportOrcDescription_Object = MibTableColumn
rasReportOrcDescription = _RasReportOrcDescription_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 8),
    _RasReportOrcDescription_Type()
)
rasReportOrcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportOrcDescription.setStatus("mandatory")
_RasReportRepeatCounter_Type = Integer32
_RasReportRepeatCounter_Object = MibTableColumn
rasReportRepeatCounter = _RasReportRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 9),
    _RasReportRepeatCounter_Type()
)
rasReportRepeatCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportRepeatCounter.setStatus("mandatory")
_RasReportSerialNumber_Type = AdicFruSerialNumber
_RasReportSerialNumber_Object = MibTableColumn
rasReportSerialNumber = _RasReportSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 10),
    _RasReportSerialNumber_Type()
)
rasReportSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportSerialNumber.setStatus("mandatory")
_RasReportHeadReport_Type = Integer32
_RasReportHeadReport_Object = MibTableColumn
rasReportHeadReport = _RasReportHeadReport_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 30, 1, 11),
    _RasReportHeadReport_Type()
)
rasReportHeadReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasReportHeadReport.setStatus("mandatory")
_RasFruStatTable_Object = MibTable
rasFruStatTable = _RasFruStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50)
)
if mibBuilder.loadTexts:
    rasFruStatTable.setStatus("mandatory")
_RasFruStatEntry_Object = MibTableRow
rasFruStatEntry = _RasFruStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1)
)
rasFruStatEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-MANAGEMENT-MIB", "rasFruStatIndex"),
)
if mibBuilder.loadTexts:
    rasFruStatEntry.setStatus("mandatory")
_RasFruStatIndex_Type = Integer32
_RasFruStatIndex_Object = MibTableColumn
rasFruStatIndex = _RasFruStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 1),
    _RasFruStatIndex_Type()
)
rasFruStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatIndex.setStatus("mandatory")
_RasFruInstanceId_Type = Gauge32
_RasFruInstanceId_Object = MibTableColumn
rasFruInstanceId = _RasFruInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 2),
    _RasFruInstanceId_Type()
)
rasFruInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruInstanceId.setStatus("mandatory")
_RasFruStatStatusGroup_Type = AdicStatusGroup
_RasFruStatStatusGroup_Object = MibTableColumn
rasFruStatStatusGroup = _RasFruStatStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 3),
    _RasFruStatStatusGroup_Type()
)
rasFruStatStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatStatusGroup.setStatus("mandatory")


class _RasFruStatFruCategory_Type(Integer32):
    """Custom type rasFruStatFruCategory based on Integer32"""
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
        *(("accessor", 4),
          ("cable", 7),
          ("drive", 9),
          ("fan", 3),
          ("firmware", 1),
          ("label", 11),
          ("mailbox", 8),
          ("media", 10),
          ("pcba", 2),
          ("picker", 5),
          ("power", 6))
    )


_RasFruStatFruCategory_Type.__name__ = "Integer32"
_RasFruStatFruCategory_Object = MibTableColumn
rasFruStatFruCategory = _RasFruStatFruCategory_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 4),
    _RasFruStatFruCategory_Type()
)
rasFruStatFruCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatFruCategory.setStatus("mandatory")
_RasFruStatFruId_Type = Integer32
_RasFruStatFruId_Object = MibTableColumn
rasFruStatFruId = _RasFruStatFruId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 5),
    _RasFruStatFruId_Type()
)
rasFruStatFruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatFruId.setStatus("mandatory")
_RasFruStatFirstReportTime_Type = AdicDateAndTime
_RasFruStatFirstReportTime_Object = MibTableColumn
rasFruStatFirstReportTime = _RasFruStatFirstReportTime_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 6),
    _RasFruStatFirstReportTime_Type()
)
rasFruStatFirstReportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatFirstReportTime.setStatus("mandatory")
_RasFruStatLastReportTime_Type = AdicDateAndTime
_RasFruStatLastReportTime_Object = MibTableColumn
rasFruStatLastReportTime = _RasFruStatLastReportTime_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 7),
    _RasFruStatLastReportTime_Type()
)
rasFruStatLastReportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatLastReportTime.setStatus("mandatory")
_RasFruStatTotalTickets_Type = Integer32
_RasFruStatTotalTickets_Object = MibTableColumn
rasFruStatTotalTickets = _RasFruStatTotalTickets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 8),
    _RasFruStatTotalTickets_Type()
)
rasFruStatTotalTickets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatTotalTickets.setStatus("mandatory")
_RasFruStatOpenTickets_Type = Integer32
_RasFruStatOpenTickets_Object = MibTableColumn
rasFruStatOpenTickets = _RasFruStatOpenTickets_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 9),
    _RasFruStatOpenTickets_Type()
)
rasFruStatOpenTickets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatOpenTickets.setStatus("mandatory")
_RasFruStatSerialNumber_Type = AdicFruSerialNumber
_RasFruStatSerialNumber_Object = MibTableColumn
rasFruStatSerialNumber = _RasFruStatSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 10),
    _RasFruStatSerialNumber_Type()
)
rasFruStatSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatSerialNumber.setStatus("mandatory")


class _RasFruStatState_Type(Integer32):
    """Custom type rasFruStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("old", 2))
    )


_RasFruStatState_Type.__name__ = "Integer32"
_RasFruStatState_Object = MibTableColumn
rasFruStatState = _RasFruStatState_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 50, 1, 11),
    _RasFruStatState_Type()
)
rasFruStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasFruStatState.setStatus("mandatory")
_RasTicketFilterTable_Object = MibTable
rasTicketFilterTable = _RasTicketFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 60)
)
if mibBuilder.loadTexts:
    rasTicketFilterTable.setStatus("mandatory")
_RasTicketFilterEntry_Object = MibTableRow
rasTicketFilterEntry = _RasTicketFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 60, 1)
)
rasTicketFilterEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    rasTicketFilterEntry.setStatus("mandatory")
_RasTicketFilterStatusGroup_Type = AdicStatusGroup
_RasTicketFilterStatusGroup_Object = MibTableColumn
rasTicketFilterStatusGroup = _RasTicketFilterStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 60, 1, 1),
    _RasTicketFilterStatusGroup_Type()
)
rasTicketFilterStatusGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketFilterStatusGroup.setStatus("mandatory")
_RasTicketFilterState_Type = AdicRasTicketState
_RasTicketFilterState_Object = MibTableColumn
rasTicketFilterState = _RasTicketFilterState_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 60, 1, 2),
    _RasTicketFilterState_Type()
)
rasTicketFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketFilterState.setStatus("mandatory")
_RasTicketFilterSeverity_Type = AdicRasTicketSeverity
_RasTicketFilterSeverity_Object = MibTableColumn
rasTicketFilterSeverity = _RasTicketFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 100, 60, 1, 3),
    _RasTicketFilterSeverity_Type()
)
rasTicketFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasTicketFilterSeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

physLibraryActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 100)
)
physLibraryActivity.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"))
)
if mibBuilder.loadTexts:
    physLibraryActivity.setStatus(
        ""
    )

physLibraryOnlineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 101)
)
physLibraryOnlineStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "onlineStatus"))
)
if mibBuilder.loadTexts:
    physLibraryOnlineStatusChange.setStatus(
        ""
    )

physLibraryDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 102)
)
physLibraryDoorStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "physLibraryDoorStatus"))
)
if mibBuilder.loadTexts:
    physLibraryDoorStatusChange.setStatus(
        ""
    )

ieStationDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 103)
)
ieStationDoorStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phSegmentAisle"),
        ("ADIC-MANAGEMENT-MIB", "phSegmentFrame"),
        ("ADIC-MANAGEMENT-MIB", "phSegmentRack"),
        ("ADIC-MANAGEMENT-MIB", "phIeStationNumber"),
        ("ADIC-MANAGEMENT-MIB", "phIeStationDoorStatus"))
)
if mibBuilder.loadTexts:
    ieStationDoorStatusChange.setStatus(
        ""
    )

moveMediaComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 104)
)
moveMediaComplete.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phStorageElementAddr"),
        ("ADIC-MANAGEMENT-MIB", "phStorageElementAddr"))
)
if mibBuilder.loadTexts:
    moveMediaComplete.setStatus(
        ""
    )

tapeDriveAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 105)
)
tapeDriveAdded.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phDriveRow"))
)
if mibBuilder.loadTexts:
    tapeDriveAdded.setStatus(
        ""
    )

tapeDriveRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 106)
)
tapeDriveRemoved.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phDriveRow"))
)
if mibBuilder.loadTexts:
    tapeDriveRemoved.setStatus(
        ""
    )

mediaMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 107)
)
mediaMounted.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phDriveRow"))
)
if mibBuilder.loadTexts:
    mediaMounted.setStatus(
        ""
    )

mediaDismounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 108)
)
mediaDismounted.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phDriveRow"),
        ("ADIC-MANAGEMENT-MIB", "phDriveMbytesRead"),
        ("ADIC-MANAGEMENT-MIB", "phDriveMbytesWritten"))
)
if mibBuilder.loadTexts:
    mediaDismounted.setStatus(
        ""
    )

ieStationInventoryPerformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 109)
)
ieStationInventoryPerformed.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-MANAGEMENT-MIB", "phIeElementAddr"),
        ("ADIC-MANAGEMENT-MIB", "phIeElementAddr"))
)
if mibBuilder.loadTexts:
    ieStationInventoryPerformed.setStatus(
        ""
    )

rcuReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 110)
)
rcuReady.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"))
)
if mibBuilder.loadTexts:
    rcuReady.setStatus(
        ""
    )

rcuNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 111)
)
rcuNotReady.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"))
)
if mibBuilder.loadTexts:
    rcuNotReady.setStatus(
        ""
    )

driveActivityUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 112)
)
driveActivityUpdate.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phHourlyMBytesRead"),
        ("ADIC-MANAGEMENT-MIB", "phHourlyMBytesWritten"),
        ("ADIC-MANAGEMENT-MIB", "phHourlyMounts"))
)
if mibBuilder.loadTexts:
    driveActivityUpdate.setStatus(
        ""
    )

driveBrickFwUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 113)
)
driveBrickFwUpdateSuccess.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phDriveSerialNumber"),
        ("ADIC-MANAGEMENT-MIB", "phDriveFirmwareVersion"))
)
if mibBuilder.loadTexts:
    driveBrickFwUpdateSuccess.setStatus(
        ""
    )

driveBrickFwUpdateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 114)
)
driveBrickFwUpdateFailure.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phDriveSerialNumber"),
        ("ADIC-MANAGEMENT-MIB", "phDriveFirmwareVersion"))
)
if mibBuilder.loadTexts:
    driveBrickFwUpdateFailure.setStatus(
        ""
    )

physLibraryConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 115)
)
physLibraryConfigurationChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"))
)
if mibBuilder.loadTexts:
    physLibraryConfigurationChange.setStatus(
        ""
    )

physLibraryRESChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 116)
)
physLibraryRESChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phStorageElementAddr"),
        ("ADIC-MANAGEMENT-MIB", "phStorageElementAddr"))
)
if mibBuilder.loadTexts:
    physLibraryRESChange.setStatus(
        ""
    )

driveBrickFwUpdateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 117)
)
driveBrickFwUpdateStart.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "phDriveSerialNumber"))
)
if mibBuilder.loadTexts:
    driveBrickFwUpdateStart.setStatus(
        ""
    )

logicalLibraryActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 200)
)
logicalLibraryActivity.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"))
)
if mibBuilder.loadTexts:
    logicalLibraryActivity.setStatus(
        ""
    )

logicalLibraryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 201)
)
logicalLibraryCreated.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"))
)
if mibBuilder.loadTexts:
    logicalLibraryCreated.setStatus(
        ""
    )

logicalLibraryModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 202)
)
logicalLibraryModified.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"))
)
if mibBuilder.loadTexts:
    logicalLibraryModified.setStatus(
        ""
    )

logicalLibraryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 203)
)
logicalLibraryDeleted.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"))
)
if mibBuilder.loadTexts:
    logicalLibraryDeleted.setStatus(
        ""
    )

logicalLibraryOnlineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 204)
)
logicalLibraryOnlineStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "logicalLibraryIndex"),
        ("ADIC-MANAGEMENT-MIB", "loStatus"))
)
if mibBuilder.loadTexts:
    logicalLibraryOnlineStatusChange.setStatus(
        ""
    )

connectivityGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 400)
)
connectivityGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    connectivityGroupStatusChange.setStatus(
        ""
    )

controlGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 401)
)
controlGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    controlGroupStatusChange.setStatus(
        ""
    )

coolingGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 402)
)
coolingGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    coolingGroupStatusChange.setStatus(
        ""
    )

drivesAndMediaGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 403)
)
drivesAndMediaGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    drivesAndMediaGroupStatusChange.setStatus(
        ""
    )

powerGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 404)
)
powerGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    powerGroupStatusChange.setStatus(
        ""
    )

roboticsGroupStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 405)
)
roboticsGroupStatusChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"))
)
if mibBuilder.loadTexts:
    roboticsGroupStatusChange.setStatus(
        ""
    )

rasEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 406)
)
rasEventNotification.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupIndex"),
        ("ADIC-MANAGEMENT-MIB", "rasStatusGroupStatus"),
        ("ADIC-MANAGEMENT-MIB", "rasTicketId"),
        ("ADIC-MANAGEMENT-MIB", "rasReportId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapIntendedUsage"))
)
if mibBuilder.loadTexts:
    rasEventNotification.setStatus(
        ""
    )

logRetrievalComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 20, 0, 500)
)
logRetrievalComplete.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSeverity"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"))
)
if mibBuilder.loadTexts:
    logRetrievalComplete.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADIC-MANAGEMENT-MIB",
    **{"Boolean": Boolean,
       "AdicEthernetSpeed": AdicEthernetSpeed,
       "AdicBarCode": AdicBarCode,
       "AdicSegmentType": AdicSegmentType,
       "AdicInstallStatus": AdicInstallStatus,
       "AdicFcPortType": AdicFcPortType,
       "AdicFcPortSpeed": AdicFcPortSpeed,
       "AdicStatusGroup": AdicStatusGroup,
       "AdicStatusGroupState": AdicStatusGroupState,
       "AdicRasTicketState": AdicRasTicketState,
       "AdicFruSerialNumber": AdicFruSerialNumber,
       "AdicRasTicketSeverity": AdicRasTicketSeverity,
       "management": management,
       "physLibraryActivity": physLibraryActivity,
       "physLibraryOnlineStatusChange": physLibraryOnlineStatusChange,
       "physLibraryDoorStatusChange": physLibraryDoorStatusChange,
       "ieStationDoorStatusChange": ieStationDoorStatusChange,
       "moveMediaComplete": moveMediaComplete,
       "tapeDriveAdded": tapeDriveAdded,
       "tapeDriveRemoved": tapeDriveRemoved,
       "mediaMounted": mediaMounted,
       "mediaDismounted": mediaDismounted,
       "ieStationInventoryPerformed": ieStationInventoryPerformed,
       "rcuReady": rcuReady,
       "rcuNotReady": rcuNotReady,
       "driveActivityUpdate": driveActivityUpdate,
       "driveBrickFwUpdateSuccess": driveBrickFwUpdateSuccess,
       "driveBrickFwUpdateFailure": driveBrickFwUpdateFailure,
       "physLibraryConfigurationChange": physLibraryConfigurationChange,
       "physLibraryRESChange": physLibraryRESChange,
       "driveBrickFwUpdateStart": driveBrickFwUpdateStart,
       "logicalLibraryActivity": logicalLibraryActivity,
       "logicalLibraryCreated": logicalLibraryCreated,
       "logicalLibraryModified": logicalLibraryModified,
       "logicalLibraryDeleted": logicalLibraryDeleted,
       "logicalLibraryOnlineStatusChange": logicalLibraryOnlineStatusChange,
       "connectivityGroupStatusChange": connectivityGroupStatusChange,
       "controlGroupStatusChange": controlGroupStatusChange,
       "coolingGroupStatusChange": coolingGroupStatusChange,
       "drivesAndMediaGroupStatusChange": drivesAndMediaGroupStatusChange,
       "powerGroupStatusChange": powerGroupStatusChange,
       "roboticsGroupStatusChange": roboticsGroupStatusChange,
       "rasEventNotification": rasEventNotification,
       "logRetrievalComplete": logRetrievalComplete,
       "globalStatus": globalStatus,
       "globalStatusTable": globalStatusTable,
       "globalStatusEntry": globalStatusEntry,
       "role": role,
       "status": status,
       "systemDateAndTime": systemDateAndTime,
       "networkTimeServer1": networkTimeServer1,
       "networkTimeProtocol": networkTimeProtocol,
       "networkTimeEnable": networkTimeEnable,
       "managementMibVersion": managementMibVersion,
       "enableDaylightSavingsTime": enableDaylightSavingsTime,
       "networkTimeServer2": networkTimeServer2,
       "globalEthernetManager": globalEthernetManager,
       "globalEthernetTable": globalEthernetTable,
       "globalEthernetEntry": globalEthernetEntry,
       "mcbHostName": mcbHostName,
       "ipAddress": ipAddress,
       "dhcpStatus": dhcpStatus,
       "ipAddressSubnetMask": ipAddressSubnetMask,
       "speedAutoNegotiation": speedAutoNegotiation,
       "preferredSpeed": preferredSpeed,
       "actualSpeed": actualSpeed,
       "ethernetDuplex": ethernetDuplex,
       "systemManager": systemManager,
       "systemManagerTable": systemManagerTable,
       "systemManagerEntry": systemManagerEntry,
       "softwareComponentIndex": softwareComponentIndex,
       "processRowStatus": processRowStatus,
       "processPhysicalMemory": processPhysicalMemory,
       "processResidentMemory": processResidentMemory,
       "softwareInstallationTable": softwareInstallationTable,
       "softwareInstallationEntry": softwareInstallationEntry,
       "installPackageName": installPackageName,
       "installProcessStatus": installProcessStatus,
       "installCommand": installCommand,
       "installStatusText": installStatusText,
       "currentFirmwareVersion": currentFirmwareVersion,
       "previousFirmwareVersion": previousFirmwareVersion,
       "downloadedFirmwareVersion": downloadedFirmwareVersion,
       "componentsInBundle": componentsInBundle,
       "mcbInstallStatusText": mcbInstallStatusText,
       "cmbInstallStatusText": cmbInstallStatusText,
       "rcuInstallStatusText": rcuInstallStatusText,
       "fcbInstallStatusText": fcbInstallStatusText,
       "amcInstallStatusText": amcInstallStatusText,
       "mcbInstallProcessStatus": mcbInstallProcessStatus,
       "cmbInstallProcessStatus": cmbInstallProcessStatus,
       "rcuInstallProcessStatus": rcuInstallProcessStatus,
       "fcbInstallProcessStatus": fcbInstallProcessStatus,
       "amcInstallProcessStatus": amcInstallProcessStatus,
       "persistentData": persistentData,
       "persistentDataTable": persistentDataTable,
       "persistentDataEntry": persistentDataEntry,
       "capacity": capacity,
       "freeSpace": freeSpace,
       "security": security,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userRowStatus": userRowStatus,
       "userGroup": userGroup,
       "userPassword": userPassword,
       "userLibAccessList": userLibAccessList,
       "licensing": licensing,
       "licenseKeyTable": licenseKeyTable,
       "licenseKeyEntry": licenseKeyEntry,
       "licenseKeyIndex": licenseKeyIndex,
       "licenseKeyRowStatus": licenseKeyRowStatus,
       "key": key,
       "licenseKeyDuration": licenseKeyDuration,
       "licenseKeyExpirationDate": licenseKeyExpirationDate,
       "licenseKeyAppliedDate": licenseKeyAppliedDate,
       "licenseFeatureTable": licenseFeatureTable,
       "licenseFeatureEntry": licenseFeatureEntry,
       "licenseFeatureIndex": licenseFeatureIndex,
       "featureName": featureName,
       "licenseFeatureQuantity": licenseFeatureQuantity,
       "licensableFeatureTable": licensableFeatureTable,
       "licensableFeatureEntry": licensableFeatureEntry,
       "licensableFeatureName": licensableFeatureName,
       "totalQuantityLicensed": totalQuantityLicensed,
       "eventManager": eventManager,
       "registrationTable": registrationTable,
       "registrationEntry": registrationEntry,
       "hostIpAddress": hostIpAddress,
       "udpPort": udpPort,
       "registrationRowStatus": registrationRowStatus,
       "logTable": logTable,
       "logEntry": logEntry,
       "logName": logName,
       "logSnapshotTable": logSnapshotTable,
       "logSnapshotEntry": logSnapshotEntry,
       "logSnapshotCommand": logSnapshotCommand,
       "physicalLibrary": physicalLibrary,
       "phGeneralInfoTable": phGeneralInfoTable,
       "phGeneralInfoEntry": phGeneralInfoEntry,
       "numElementDomains": numElementDomains,
       "numPhSlots": numPhSlots,
       "numPhIESlots": numPhIESlots,
       "numPhDrives": numPhDrives,
       "onlineStatus": onlineStatus,
       "readiness": readiness,
       "autoInventoryMode": autoInventoryMode,
       "autoCalibrateMode": autoCalibrateMode,
       "autoConfigureMode": autoConfigureMode,
       "numPhAisles": numPhAisles,
       "operatingMode": operatingMode,
       "numStorageCartridges": numStorageCartridges,
       "numCleaningCartridges": numCleaningCartridges,
       "physLibraryManagerLun": physLibraryManagerLun,
       "physLibraryAutoCleaning": physLibraryAutoCleaning,
       "physLibraryDoorStatus": physLibraryDoorStatus,
       "numPhFrames": numPhFrames,
       "totalRawCapacity": totalRawCapacity,
       "totalFreeCapacity": totalFreeCapacity,
       "totalUsedCapacity": totalUsedCapacity,
       "logicalSNAdressingMode": logicalSNAdressingMode,
       "mediaDomainTable": mediaDomainTable,
       "mediaDomainEntry": mediaDomainEntry,
       "mediaDomainIndex": mediaDomainIndex,
       "mediaDomainName": mediaDomainName,
       "numStorageElements": numStorageElements,
       "numIeElements": numIeElements,
       "numCleaningSlots": numCleaningSlots,
       "mediaTypeTable": mediaTypeTable,
       "mediaTypeEntry": mediaTypeEntry,
       "mediaTypeIndex": mediaTypeIndex,
       "mediaTypeName": mediaTypeName,
       "numDriveElements": numDriveElements,
       "phFrameTable": phFrameTable,
       "phFrameEntry": phFrameEntry,
       "phFrameType": phFrameType,
       "phFrameSerialNumber": phFrameSerialNumber,
       "phFrameNumRacks": phFrameNumRacks,
       "phSegmentTable": phSegmentTable,
       "phSegmentEntry": phSegmentEntry,
       "phSegmentAisle": phSegmentAisle,
       "phSegmentFrame": phSegmentFrame,
       "phSegmentRack": phSegmentRack,
       "phSegmentSection": phSegmentSection,
       "phSegmentCol": phSegmentCol,
       "phSegmentStartingRow": phSegmentStartingRow,
       "phSegmentSize": phSegmentSize,
       "phSegmentType": phSegmentType,
       "phSegmentMediaDomain": phSegmentMediaDomain,
       "phSegmentStatus": phSegmentStatus,
       "phSegmentCodStatus": phSegmentCodStatus,
       "phSegStartingAddress": phSegStartingAddress,
       "phStorageSegTable": phStorageSegTable,
       "phStorageSegEntry": phStorageSegEntry,
       "phStorageSegSize": phStorageSegSize,
       "phIeSegTable": phIeSegTable,
       "phIeSegEntry": phIeSegEntry,
       "phIeSegSize": phIeSegSize,
       "phIeSegReserve": phIeSegReserve,
       "phIeSegReservedBy": phIeSegReservedBy,
       "phIeSegOnlineStatus": phIeSegOnlineStatus,
       "phIeSegCommand": phIeSegCommand,
       "phIeStationTable": phIeStationTable,
       "phIeStationEntry": phIeStationEntry,
       "phIeStationNumber": phIeStationNumber,
       "phIeStationDoorStatus": phIeStationDoorStatus,
       "phIeStationREDId": phIeStationREDId,
       "phDriveSegTable": phDriveSegTable,
       "phDriveSegEntry": phDriveSegEntry,
       "phDriveSegSize": phDriveSegSize,
       "phDriveSegMediaType": phDriveSegMediaType,
       "phDriveSegInterfaceType": phDriveSegInterfaceType,
       "phCleaningSegTable": phCleaningSegTable,
       "phCleaningSegEntry": phCleaningSegEntry,
       "phCleaningSegSize": phCleaningSegSize,
       "phCleaningSegRowStatus": phCleaningSegRowStatus,
       "phStorageSlotTable": phStorageSlotTable,
       "phStorageSlotEntry": phStorageSlotEntry,
       "phStorageRow": phStorageRow,
       "phStorageElementAddr": phStorageElementAddr,
       "phIeSlotTable": phIeSlotTable,
       "phIeSlotEntry": phIeSlotEntry,
       "phIeRow": phIeRow,
       "phIeElementAddr": phIeElementAddr,
       "phIeMediaPresent": phIeMediaPresent,
       "phIeMediaId": phIeMediaId,
       "phDriveTable": phDriveTable,
       "phDriveEntry": phDriveEntry,
       "phDriveRow": phDriveRow,
       "phDriveElementAddr": phDriveElementAddr,
       "phDriveScsiId": phDriveScsiId,
       "phDriveScsiLun": phDriveScsiLun,
       "phDriveWwn": phDriveWwn,
       "phDriveVendor": phDriveVendor,
       "phDriveProduct": phDriveProduct,
       "phDriveSerialNumber": phDriveSerialNumber,
       "phDriveNeedsCleaning": phDriveNeedsCleaning,
       "phDriveAutoCleaning": phDriveAutoCleaning,
       "phDriveInterfaceType": phDriveInterfaceType,
       "phDriveFcLoopId": phDriveFcLoopId,
       "phDriveFcLoopIdMode": phDriveFcLoopIdMode,
       "phDriveFcHardId": phDriveFcHardId,
       "phDriveStatus": phDriveStatus,
       "phDriveCommand": phDriveCommand,
       "phDriveFcPortId": phDriveFcPortId,
       "phDriveCompressionOn": phDriveCompressionOn,
       "phDriveWriteProtected": phDriveWriteProtected,
       "phDriveNumLoads": phDriveNumLoads,
       "phDriveNumCleans": phDriveNumCleans,
       "phDrivePowerStatus": phDrivePowerStatus,
       "phDriveReadErrors": phDriveReadErrors,
       "phDriveWriteErrors": phDriveWriteErrors,
       "phDriveMbytesRead": phDriveMbytesRead,
       "phDriveMbytesWritten": phDriveMbytesWritten,
       "phDriveFirmwareVersion": phDriveFirmwareVersion,
       "phDriveREDId": phDriveREDId,
       "phDriveOnlineStatus": phDriveOnlineStatus,
       "phDriveErrorCodeBytes": phDriveErrorCodeBytes,
       "phDriveRasStatus": phDriveRasStatus,
       "phDriveWwPortName": phDriveWwPortName,
       "phDriveStatHistoryTable": phDriveStatHistoryTable,
       "phDriveStatHistoryEntry": phDriveStatHistoryEntry,
       "phHourIndex": phHourIndex,
       "phHourlyMBytesRead": phHourlyMBytesRead,
       "phHourlyMBytesWritten": phHourlyMBytesWritten,
       "phHourlyMounts": phHourlyMounts,
       "phDrivePorts": phDrivePorts,
       "fcDrivePortTable": fcDrivePortTable,
       "fcDrivePortEntry": fcDrivePortEntry,
       "fcPortPreferredSpeed": fcPortPreferredSpeed,
       "fcPortNegotiatedSpeed": fcPortNegotiatedSpeed,
       "fcPortPreferredType": fcPortPreferredType,
       "fcPortNegotiatedType": fcPortNegotiatedType,
       "fcPortTypeQualifier": fcPortTypeQualifier,
       "phMediaTable": phMediaTable,
       "phMediaEntry": phMediaEntry,
       "phMediaBarCode": phMediaBarCode,
       "phMediaDomain": phMediaDomain,
       "phMediaType": phMediaType,
       "phMediaElementAddress": phMediaElementAddress,
       "phMediaMounts": phMediaMounts,
       "phMediaReadErrors": phMediaReadErrors,
       "phMediaWriteErrors": phMediaWriteErrors,
       "phMediaCapacity": phMediaCapacity,
       "phMediaFreeSpace": phMediaFreeSpace,
       "phMediaExported": phMediaExported,
       "phMediaImportTimestamp": phMediaImportTimestamp,
       "phMediaExportTimestamp": phMediaExportTimestamp,
       "phTransportTable": phTransportTable,
       "phTransportEntry": phTransportEntry,
       "phTransportElementAddress": phTransportElementAddress,
       "phTransportNumRecoveredGets": phTransportNumRecoveredGets,
       "phTransportNumRecoveredPuts": phTransportNumRecoveredPuts,
       "phTransportNumRecoveredScans": phTransportNumRecoveredScans,
       "phTransportNumPuts": phTransportNumPuts,
       "phTransportREDId": phTransportREDId,
       "phTransportDomainTable": phTransportDomainTable,
       "phTransportDomainEntry": phTransportDomainEntry,
       "phTransportDomainIndex": phTransportDomainIndex,
       "phCleaningMediaTable": phCleaningMediaTable,
       "phCleaningMediaEntry": phCleaningMediaEntry,
       "phCleaningMediaRow": phCleaningMediaRow,
       "phCleaningMediaStatus": phCleaningMediaStatus,
       "phCleaningMediaTypeIndex": phCleaningMediaTypeIndex,
       "phCleaningMediaVendorId": phCleaningMediaVendorId,
       "phCleaningMediaBarcode": phCleaningMediaBarcode,
       "phCleaningMediaUseCount": phCleaningMediaUseCount,
       "phCleaningMediaMaxUses": phCleaningMediaMaxUses,
       "phCleaningMediaImportTimestamp": phCleaningMediaImportTimestamp,
       "logicalLibrary": logicalLibrary,
       "loGeneralInfoTable": loGeneralInfoTable,
       "loGeneralInfoEntry": loGeneralInfoEntry,
       "maxLogicalLibraries": maxLogicalLibraries,
       "numLogicalLibraries": numLogicalLibraries,
       "masterOnlineStatus": masterOnlineStatus,
       "numVendorIds": numVendorIds,
       "autoPartitionTable": autoPartitionTable,
       "autoPartitionEntry": autoPartitionEntry,
       "numAutoPartition": numAutoPartition,
       "autoPartitionCommand": autoPartitionCommand,
       "vendorIdTable": vendorIdTable,
       "vendorIdEntry": vendorIdEntry,
       "vendorIdIndex": vendorIdIndex,
       "vendorName": vendorName,
       "numProductIds": numProductIds,
       "productIdTable": productIdTable,
       "productIdEntry": productIdEntry,
       "productIdIndex": productIdIndex,
       "productIdName": productIdName,
       "productDrivesMin": productDrivesMin,
       "productDrivesMax": productDrivesMax,
       "productSlotsMin": productSlotsMin,
       "productSlotsMax": productSlotsMax,
       "productIeMin": productIeMin,
       "productIeMax": productIeMax,
       "logicalLibraryTable": logicalLibraryTable,
       "logicalLibraryEntry": logicalLibraryEntry,
       "logicalLibraryIndex": logicalLibraryIndex,
       "command": command,
       "name": name,
       "assignedLun": assignedLun,
       "vendorId": vendorId,
       "productId": productId,
       "mediaDomain": mediaDomain,
       "mediaType": mediaType,
       "numSlots": numSlots,
       "numIE": numIE,
       "numDrives": numDrives,
       "loStatus": loStatus,
       "automaticCleaning": automaticCleaning,
       "mediaTypeChecking": mediaTypeChecking,
       "serialNumber": serialNumber,
       "loInterfaceType": loInterfaceType,
       "loNumLibraries": loNumLibraries,
       "loLtoTapeTags": loLtoTapeTags,
       "loMediaTypeCheckingPolicy": loMediaTypeCheckingPolicy,
       "loSegmentTable": loSegmentTable,
       "loSegmentEntry": loSegmentEntry,
       "loSegmentAisle": loSegmentAisle,
       "loSegmentFrame": loSegmentFrame,
       "loSegmentRack": loSegmentRack,
       "loSegmentSection": loSegmentSection,
       "loSegmentCol": loSegmentCol,
       "loSegmentStartingRow": loSegmentStartingRow,
       "loSegmentSize": loSegmentSize,
       "loSegmentType": loSegmentType,
       "loSegmentMediaDomain": loSegmentMediaDomain,
       "loSegmentBelongsTo": loSegmentBelongsTo,
       "loSegmentCommand": loSegmentCommand,
       "loSegmentStatus": loSegmentStatus,
       "loSegmentStartingAddress": loSegmentStartingAddress,
       "loSegmentBelongsToTable": loSegmentBelongsToTable,
       "loSegmentBelongsToEntry": loSegmentBelongsToEntry,
       "loSegmentAssignedTo": loSegmentAssignedTo,
       "loStorageSegTable": loStorageSegTable,
       "loStorageSegEntry": loStorageSegEntry,
       "loStorageSegSize": loStorageSegSize,
       "loStorageSegStartingAddress": loStorageSegStartingAddress,
       "loIeSegTable": loIeSegTable,
       "loIeSegEntry": loIeSegEntry,
       "loIeSegSize": loIeSegSize,
       "loIeSegReserve": loIeSegReserve,
       "loIeSegReservedBy": loIeSegReservedBy,
       "loIeSegStartingAddress": loIeSegStartingAddress,
       "loDriveSegTable": loDriveSegTable,
       "loDriveSegEntry": loDriveSegEntry,
       "loDriveSegSize": loDriveSegSize,
       "loDriveSegStartingAddress": loDriveSegStartingAddress,
       "loDriveSegMediaType": loDriveSegMediaType,
       "loDriveSegInterfaceType": loDriveSegInterfaceType,
       "loStorageSlotTable": loStorageSlotTable,
       "loStorageSlotEntry": loStorageSlotEntry,
       "loStorageRow": loStorageRow,
       "loIeSlotTable": loIeSlotTable,
       "loIeSlotEntry": loIeSlotEntry,
       "loIeRow": loIeRow,
       "loDriveTable": loDriveTable,
       "loDriveEntry": loDriveEntry,
       "loDriveRow": loDriveRow,
       "loStatisticsTable": loStatisticsTable,
       "loStatisticsEntry": loStatisticsEntry,
       "loNumRecoveredGets": loNumRecoveredGets,
       "loNumRecoveredPuts": loNumRecoveredPuts,
       "loNumRecoveredScans": loNumRecoveredScans,
       "loStatsNumPuts": loStatsNumPuts,
       "loStatsNumPutRetries": loStatsNumPutRetries,
       "loStatsNumGetRetries": loStatsNumGetRetries,
       "loStatsNumScanRetries": loStatsNumScanRetries,
       "ras": ras,
       "rasSystemStatusTable": rasSystemStatusTable,
       "rasSystemStatusEntry": rasSystemStatusEntry,
       "rasStatusGroupIndex": rasStatusGroupIndex,
       "rasStatusGroupStatus": rasStatusGroupStatus,
       "rasStatusGroupPreviousStatus": rasStatusGroupPreviousStatus,
       "rasStatusGroupTextSummary": rasStatusGroupTextSummary,
       "rasStatusGroupTotalTickets": rasStatusGroupTotalTickets,
       "rasStatusGroupOpenTickets": rasStatusGroupOpenTickets,
       "rasStatusGroupActionsPending": rasStatusGroupActionsPending,
       "rasStatusGroupLastChange": rasStatusGroupLastChange,
       "rasTicketTable": rasTicketTable,
       "rasTicketEntry": rasTicketEntry,
       "rasTicketId": rasTicketId,
       "rasTicketRowStatus": rasTicketRowStatus,
       "rasTicketState": rasTicketState,
       "rasTicketQualifier": rasTicketQualifier,
       "rasTicketPriority": rasTicketPriority,
       "rasTicketDescription": rasTicketDescription,
       "rasTicketStatusGroup": rasTicketStatusGroup,
       "rasTicketGroupStatus": rasTicketGroupStatus,
       "rasTicketClosedBy": rasTicketClosedBy,
       "rasTicketVerifiedBy": rasTicketVerifiedBy,
       "rasTicketComments": rasTicketComments,
       "rasTicketSerialNumber": rasTicketSerialNumber,
       "rasTicketTimeOpened": rasTicketTimeOpened,
       "rasTicketTimeClosed": rasTicketTimeClosed,
       "rasTicketCount": rasTicketCount,
       "rasTicketKeyReport": rasTicketKeyReport,
       "rasReportTable": rasReportTable,
       "rasReportEntry": rasReportEntry,
       "rasReportId": rasReportId,
       "rasReportRowStatus": rasReportRowStatus,
       "rasReportTimestamp": rasReportTimestamp,
       "rasReportStatusGroup": rasReportStatusGroup,
       "rasReportOrcData": rasReportOrcData,
       "rasReportGroupStatus": rasReportGroupStatus,
       "rasReportDescription": rasReportDescription,
       "rasReportOrcDescription": rasReportOrcDescription,
       "rasReportRepeatCounter": rasReportRepeatCounter,
       "rasReportSerialNumber": rasReportSerialNumber,
       "rasReportHeadReport": rasReportHeadReport,
       "rasFruStatTable": rasFruStatTable,
       "rasFruStatEntry": rasFruStatEntry,
       "rasFruStatIndex": rasFruStatIndex,
       "rasFruInstanceId": rasFruInstanceId,
       "rasFruStatStatusGroup": rasFruStatStatusGroup,
       "rasFruStatFruCategory": rasFruStatFruCategory,
       "rasFruStatFruId": rasFruStatFruId,
       "rasFruStatFirstReportTime": rasFruStatFirstReportTime,
       "rasFruStatLastReportTime": rasFruStatLastReportTime,
       "rasFruStatTotalTickets": rasFruStatTotalTickets,
       "rasFruStatOpenTickets": rasFruStatOpenTickets,
       "rasFruStatSerialNumber": rasFruStatSerialNumber,
       "rasFruStatState": rasFruStatState,
       "rasTicketFilterTable": rasTicketFilterTable,
       "rasTicketFilterEntry": rasTicketFilterEntry,
       "rasTicketFilterStatusGroup": rasTicketFilterStatusGroup,
       "rasTicketFilterState": rasTicketFilterState,
       "rasTicketFilterSeverity": rasTicketFilterSeverity}
)
