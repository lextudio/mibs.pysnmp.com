# SNMP MIB module (INTEL-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:00 2024
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

(products,) = mibBuilder.importSymbols(
    "Intel-Common-MIB",
    "products")

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

_Snmp_agents_ObjectIdentity = ObjectIdentity
snmp_agents = _Snmp_agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6)
)
_AgentConfiguration_ObjectIdentity = ObjectIdentity
agentConfiguration = _AgentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1)
)


class _AgentVendorName_Type(DisplayString):
    """Custom type agentVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_AgentVendorName_Type.__name__ = "DisplayString"
_AgentVendorName_Object = MibScalar
agentVendorName = _AgentVendorName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 1),
    _AgentVendorName_Type()
)
agentVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVendorName.setStatus("mandatory")


class _AgentProductName_Type(DisplayString):
    """Custom type agentProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_AgentProductName_Type.__name__ = "DisplayString"
_AgentProductName_Object = MibScalar
agentProductName = _AgentProductName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 2),
    _AgentProductName_Type()
)
agentProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentProductName.setStatus("mandatory")
_AgentChassisIndex_Type = Integer32
_AgentChassisIndex_Object = MibScalar
agentChassisIndex = _AgentChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 3),
    _AgentChassisIndex_Type()
)
agentChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentChassisIndex.setStatus("mandatory")
_AgentModuleIndex_Type = Integer32
_AgentModuleIndex_Object = MibScalar
agentModuleIndex = _AgentModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 4),
    _AgentModuleIndex_Type()
)
agentModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentModuleIndex.setStatus("mandatory")


class _Mibversion_Type(DisplayString):
    """Custom type mibversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Mibversion_Type.__name__ = "DisplayString"
_Mibversion_Object = MibScalar
mibversion = _Mibversion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 5),
    _Mibversion_Type()
)
mibversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibversion.setStatus("mandatory")


class _ResetAgent_Type(Integer32):
    """Custom type resetAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_ResetAgent_Type.__name__ = "Integer32"
_ResetAgent_Object = MibScalar
resetAgent = _ResetAgent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 1, 6),
    _ResetAgent_Type()
)
resetAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAgent.setStatus("mandatory")
_IpConfiguration_ObjectIdentity = ObjectIdentity
ipConfiguration = _IpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2)
)


class _IpAddressMethodInUse_Type(Integer32):
    """Custom type ipAddressMethodInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_IpAddressMethodInUse_Type.__name__ = "Integer32"
_IpAddressMethodInUse_Object = MibScalar
ipAddressMethodInUse = _IpAddressMethodInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 1),
    _IpAddressMethodInUse_Type()
)
ipAddressMethodInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressMethodInUse.setStatus("mandatory")
_IpAddressInUse_Type = IpAddress
_IpAddressInUse_Object = MibScalar
ipAddressInUse = _IpAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2),
    _IpAddressInUse_Type()
)
ipAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressInUse.setStatus("mandatory")
_GatewayorRouterAddrInUse_Type = IpAddress
_GatewayorRouterAddrInUse_Object = MibScalar
gatewayorRouterAddrInUse = _GatewayorRouterAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3),
    _GatewayorRouterAddrInUse_Type()
)
gatewayorRouterAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayorRouterAddrInUse.setStatus("mandatory")
_NetworkMaskInUse_Type = IpAddress
_NetworkMaskInUse_Object = MibScalar
networkMaskInUse = _NetworkMaskInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 4),
    _NetworkMaskInUse_Type()
)
networkMaskInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkMaskInUse.setStatus("mandatory")
_BroadcastAddressInUse_Type = IpAddress
_BroadcastAddressInUse_Object = MibScalar
broadcastAddressInUse = _BroadcastAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 5),
    _BroadcastAddressInUse_Type()
)
broadcastAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadcastAddressInUse.setStatus("mandatory")


class _IpAddressMethodNextReset_Type(Integer32):
    """Custom type ipAddressMethodNextReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_IpAddressMethodNextReset_Type.__name__ = "Integer32"
_IpAddressMethodNextReset_Object = MibScalar
ipAddressMethodNextReset = _IpAddressMethodNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 6),
    _IpAddressMethodNextReset_Type()
)
ipAddressMethodNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressMethodNextReset.setStatus("mandatory")
_IpAddressNextReset_Type = IpAddress
_IpAddressNextReset_Object = MibScalar
ipAddressNextReset = _IpAddressNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 7),
    _IpAddressNextReset_Type()
)
ipAddressNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressNextReset.setStatus("mandatory")
_GatewayorRouterAddrNextReset_Type = IpAddress
_GatewayorRouterAddrNextReset_Object = MibScalar
gatewayorRouterAddrNextReset = _GatewayorRouterAddrNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 8),
    _GatewayorRouterAddrNextReset_Type()
)
gatewayorRouterAddrNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayorRouterAddrNextReset.setStatus("mandatory")
_NetworkMaskNextReset_Type = IpAddress
_NetworkMaskNextReset_Object = MibScalar
networkMaskNextReset = _NetworkMaskNextReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 9),
    _NetworkMaskNextReset_Type()
)
networkMaskNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMaskNextReset.setStatus("mandatory")
_SnmpConfiguration_ObjectIdentity = ObjectIdentity
snmpConfiguration = _SnmpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3)
)


class _SnmpReadCommunityString_Type(DisplayString):
    """Custom type snmpReadCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpReadCommunityString_Type.__name__ = "DisplayString"
_SnmpReadCommunityString_Object = MibScalar
snmpReadCommunityString = _SnmpReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 1),
    _SnmpReadCommunityString_Type()
)
snmpReadCommunityString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snmpReadCommunityString.setStatus("mandatory")


class _SnmpWriteCommunityString_Type(DisplayString):
    """Custom type snmpWriteCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpWriteCommunityString_Type.__name__ = "DisplayString"
_SnmpWriteCommunityString_Object = MibScalar
snmpWriteCommunityString = _SnmpWriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 2),
    _SnmpWriteCommunityString_Type()
)
snmpWriteCommunityString.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snmpWriteCommunityString.setStatus("mandatory")
_SnmpTrapReceiverMAX_Type = Integer32
_SnmpTrapReceiverMAX_Object = MibScalar
snmpTrapReceiverMAX = _SnmpTrapReceiverMAX_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 3),
    _SnmpTrapReceiverMAX_Type()
)
snmpTrapReceiverMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapReceiverMAX.setStatus("mandatory")
_SnmpTrapReceiverNumber_Type = Integer32
_SnmpTrapReceiverNumber_Object = MibScalar
snmpTrapReceiverNumber = _SnmpTrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 4),
    _SnmpTrapReceiverNumber_Type()
)
snmpTrapReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapReceiverNumber.setStatus("mandatory")
_SnmpTrapAddressTable_Object = MibTable
snmpTrapAddressTable = _SnmpTrapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5)
)
if mibBuilder.loadTexts:
    snmpTrapAddressTable.setStatus("mandatory")
_SnmpTrapAddressEntry_Object = MibTableRow
snmpTrapAddressEntry = _SnmpTrapAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5, 1)
)
snmpTrapAddressEntry.setIndexNames(
    (0, "INTEL-SYS-MIB", "trapAddrIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapAddressEntry.setStatus("mandatory")
_TrapAddrIndex_Type = Integer32
_TrapAddrIndex_Object = MibTableColumn
trapAddrIndex = _TrapAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5, 1, 1),
    _TrapAddrIndex_Type()
)
trapAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAddrIndex.setStatus("mandatory")
_TrapIPAddr_Type = IpAddress
_TrapIPAddr_Object = MibTableColumn
trapIPAddr = _TrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5, 1, 2),
    _TrapIPAddr_Type()
)
trapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPAddr.setStatus("mandatory")


class _TrapCommunityString_Type(DisplayString):
    """Custom type trapCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapCommunityString_Type.__name__ = "DisplayString"
_TrapCommunityString_Object = MibTableColumn
trapCommunityString = _TrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5, 1, 3),
    _TrapCommunityString_Type()
)
trapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunityString.setStatus("mandatory")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ignore", 2))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 3, 5, 1, 4),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-SYS-MIB",
    **{"snmp-agents": snmp_agents,
       "agentConfiguration": agentConfiguration,
       "agentVendorName": agentVendorName,
       "agentProductName": agentProductName,
       "agentChassisIndex": agentChassisIndex,
       "agentModuleIndex": agentModuleIndex,
       "mibversion": mibversion,
       "resetAgent": resetAgent,
       "ipConfiguration": ipConfiguration,
       "ipAddressMethodInUse": ipAddressMethodInUse,
       "ipAddressInUse": ipAddressInUse,
       "gatewayorRouterAddrInUse": gatewayorRouterAddrInUse,
       "networkMaskInUse": networkMaskInUse,
       "broadcastAddressInUse": broadcastAddressInUse,
       "ipAddressMethodNextReset": ipAddressMethodNextReset,
       "ipAddressNextReset": ipAddressNextReset,
       "gatewayorRouterAddrNextReset": gatewayorRouterAddrNextReset,
       "networkMaskNextReset": networkMaskNextReset,
       "snmpConfiguration": snmpConfiguration,
       "snmpReadCommunityString": snmpReadCommunityString,
       "snmpWriteCommunityString": snmpWriteCommunityString,
       "snmpTrapReceiverMAX": snmpTrapReceiverMAX,
       "snmpTrapReceiverNumber": snmpTrapReceiverNumber,
       "snmpTrapAddressTable": snmpTrapAddressTable,
       "snmpTrapAddressEntry": snmpTrapAddressEntry,
       "trapAddrIndex": trapAddrIndex,
       "trapIPAddr": trapIPAddr,
       "trapCommunityString": trapCommunityString,
       "trapStatus": trapStatus}
)
