# SNMP MIB module (TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:07 2024
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

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IPv6FlowLabelOrAny,) = mibBuilder.importSymbols(
    "IPV6-FLOW-LABEL-MIB",
    "IPv6FlowLabelOrAny")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

tunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131)
)
tunnelMIB.setRevisions(
        ("2005-05-16 00:00",
         "1999-08-24 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TunnelMIBObjects_ObjectIdentity = ObjectIdentity
tunnelMIBObjects = _TunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131, 1)
)
_Tunnel_ObjectIdentity = ObjectIdentity
tunnel = _Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1)
)
_TunnelIfTable_Object = MibTable
tunnelIfTable = _TunnelIfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tunnelIfTable.setStatus("current")
_TunnelIfEntry_Object = MibTableRow
tunnelIfEntry = _TunnelIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1)
)
tunnelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tunnelIfEntry.setStatus("current")
_TunnelIfLocalAddress_Type = IpAddress
_TunnelIfLocalAddress_Object = MibTableColumn
tunnelIfLocalAddress = _TunnelIfLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 1),
    _TunnelIfLocalAddress_Type()
)
tunnelIfLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelIfLocalAddress.setStatus("deprecated")
_TunnelIfRemoteAddress_Type = IpAddress
_TunnelIfRemoteAddress_Object = MibTableColumn
tunnelIfRemoteAddress = _TunnelIfRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 2),
    _TunnelIfRemoteAddress_Type()
)
tunnelIfRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelIfRemoteAddress.setStatus("deprecated")
_TunnelIfEncapsMethod_Type = IANAtunnelType
_TunnelIfEncapsMethod_Object = MibTableColumn
tunnelIfEncapsMethod = _TunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 3),
    _TunnelIfEncapsMethod_Type()
)
tunnelIfEncapsMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelIfEncapsMethod.setStatus("current")


class _TunnelIfHopLimit_Type(Integer32):
    """Custom type tunnelIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TunnelIfHopLimit_Type.__name__ = "Integer32"
_TunnelIfHopLimit_Object = MibTableColumn
tunnelIfHopLimit = _TunnelIfHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 4),
    _TunnelIfHopLimit_Type()
)
tunnelIfHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfHopLimit.setStatus("current")


class _TunnelIfSecurity_Type(Integer32):
    """Custom type tunnelIfSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 2),
          ("none", 1),
          ("other", 3))
    )


_TunnelIfSecurity_Type.__name__ = "Integer32"
_TunnelIfSecurity_Object = MibTableColumn
tunnelIfSecurity = _TunnelIfSecurity_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 5),
    _TunnelIfSecurity_Type()
)
tunnelIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelIfSecurity.setStatus("current")


class _TunnelIfTOS_Type(Integer32):
    """Custom type tunnelIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_TunnelIfTOS_Type.__name__ = "Integer32"
_TunnelIfTOS_Object = MibTableColumn
tunnelIfTOS = _TunnelIfTOS_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 6),
    _TunnelIfTOS_Type()
)
tunnelIfTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfTOS.setStatus("current")
_TunnelIfFlowLabel_Type = IPv6FlowLabelOrAny
_TunnelIfFlowLabel_Object = MibTableColumn
tunnelIfFlowLabel = _TunnelIfFlowLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 7),
    _TunnelIfFlowLabel_Type()
)
tunnelIfFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfFlowLabel.setStatus("current")
_TunnelIfAddressType_Type = InetAddressType
_TunnelIfAddressType_Object = MibTableColumn
tunnelIfAddressType = _TunnelIfAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 8),
    _TunnelIfAddressType_Type()
)
tunnelIfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfAddressType.setStatus("current")
_TunnelIfLocalInetAddress_Type = InetAddress
_TunnelIfLocalInetAddress_Object = MibTableColumn
tunnelIfLocalInetAddress = _TunnelIfLocalInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 9),
    _TunnelIfLocalInetAddress_Type()
)
tunnelIfLocalInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfLocalInetAddress.setStatus("current")
_TunnelIfRemoteInetAddress_Type = InetAddress
_TunnelIfRemoteInetAddress_Object = MibTableColumn
tunnelIfRemoteInetAddress = _TunnelIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 10),
    _TunnelIfRemoteInetAddress_Type()
)
tunnelIfRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfRemoteInetAddress.setStatus("current")


class _TunnelIfEncapsLimit_Type(Integer32):
    """Custom type tunnelIfEncapsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TunnelIfEncapsLimit_Type.__name__ = "Integer32"
_TunnelIfEncapsLimit_Object = MibTableColumn
tunnelIfEncapsLimit = _TunnelIfEncapsLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 11),
    _TunnelIfEncapsLimit_Type()
)
tunnelIfEncapsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfEncapsLimit.setStatus("current")
_TunnelConfigTable_Object = MibTable
tunnelConfigTable = _TunnelConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tunnelConfigTable.setStatus("deprecated")
_TunnelConfigEntry_Object = MibTableRow
tunnelConfigEntry = _TunnelConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1)
)
tunnelConfigEntry.setIndexNames(
    (0, "TUNNEL-MIB", "tunnelConfigLocalAddress"),
    (0, "TUNNEL-MIB", "tunnelConfigRemoteAddress"),
    (0, "TUNNEL-MIB", "tunnelConfigEncapsMethod"),
    (0, "TUNNEL-MIB", "tunnelConfigID"),
)
if mibBuilder.loadTexts:
    tunnelConfigEntry.setStatus("deprecated")
_TunnelConfigLocalAddress_Type = IpAddress
_TunnelConfigLocalAddress_Object = MibTableColumn
tunnelConfigLocalAddress = _TunnelConfigLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 1),
    _TunnelConfigLocalAddress_Type()
)
tunnelConfigLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelConfigLocalAddress.setStatus("deprecated")
_TunnelConfigRemoteAddress_Type = IpAddress
_TunnelConfigRemoteAddress_Object = MibTableColumn
tunnelConfigRemoteAddress = _TunnelConfigRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 2),
    _TunnelConfigRemoteAddress_Type()
)
tunnelConfigRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelConfigRemoteAddress.setStatus("deprecated")
_TunnelConfigEncapsMethod_Type = IANAtunnelType
_TunnelConfigEncapsMethod_Object = MibTableColumn
tunnelConfigEncapsMethod = _TunnelConfigEncapsMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 3),
    _TunnelConfigEncapsMethod_Type()
)
tunnelConfigEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelConfigEncapsMethod.setStatus("deprecated")


class _TunnelConfigID_Type(Integer32):
    """Custom type tunnelConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TunnelConfigID_Type.__name__ = "Integer32"
_TunnelConfigID_Object = MibTableColumn
tunnelConfigID = _TunnelConfigID_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 4),
    _TunnelConfigID_Type()
)
tunnelConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelConfigID.setStatus("deprecated")
_TunnelConfigIfIndex_Type = InterfaceIndexOrZero
_TunnelConfigIfIndex_Object = MibTableColumn
tunnelConfigIfIndex = _TunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 5),
    _TunnelConfigIfIndex_Type()
)
tunnelConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelConfigIfIndex.setStatus("deprecated")
_TunnelConfigStatus_Type = RowStatus
_TunnelConfigStatus_Object = MibTableColumn
tunnelConfigStatus = _TunnelConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 6),
    _TunnelConfigStatus_Type()
)
tunnelConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tunnelConfigStatus.setStatus("deprecated")
_TunnelInetConfigTable_Object = MibTable
tunnelInetConfigTable = _TunnelInetConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tunnelInetConfigTable.setStatus("current")
_TunnelInetConfigEntry_Object = MibTableRow
tunnelInetConfigEntry = _TunnelInetConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1)
)
tunnelInetConfigEntry.setIndexNames(
    (0, "TUNNEL-MIB", "tunnelInetConfigAddressType"),
    (0, "TUNNEL-MIB", "tunnelInetConfigLocalAddress"),
    (0, "TUNNEL-MIB", "tunnelInetConfigRemoteAddress"),
    (0, "TUNNEL-MIB", "tunnelInetConfigEncapsMethod"),
    (0, "TUNNEL-MIB", "tunnelInetConfigID"),
)
if mibBuilder.loadTexts:
    tunnelInetConfigEntry.setStatus("current")
_TunnelInetConfigAddressType_Type = InetAddressType
_TunnelInetConfigAddressType_Object = MibTableColumn
tunnelInetConfigAddressType = _TunnelInetConfigAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 1),
    _TunnelInetConfigAddressType_Type()
)
tunnelInetConfigAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelInetConfigAddressType.setStatus("current")
_TunnelInetConfigLocalAddress_Type = InetAddress
_TunnelInetConfigLocalAddress_Object = MibTableColumn
tunnelInetConfigLocalAddress = _TunnelInetConfigLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 2),
    _TunnelInetConfigLocalAddress_Type()
)
tunnelInetConfigLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelInetConfigLocalAddress.setStatus("current")
_TunnelInetConfigRemoteAddress_Type = InetAddress
_TunnelInetConfigRemoteAddress_Object = MibTableColumn
tunnelInetConfigRemoteAddress = _TunnelInetConfigRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 3),
    _TunnelInetConfigRemoteAddress_Type()
)
tunnelInetConfigRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelInetConfigRemoteAddress.setStatus("current")
_TunnelInetConfigEncapsMethod_Type = IANAtunnelType
_TunnelInetConfigEncapsMethod_Object = MibTableColumn
tunnelInetConfigEncapsMethod = _TunnelInetConfigEncapsMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 4),
    _TunnelInetConfigEncapsMethod_Type()
)
tunnelInetConfigEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelInetConfigEncapsMethod.setStatus("current")


class _TunnelInetConfigID_Type(Integer32):
    """Custom type tunnelInetConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TunnelInetConfigID_Type.__name__ = "Integer32"
_TunnelInetConfigID_Object = MibTableColumn
tunnelInetConfigID = _TunnelInetConfigID_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 5),
    _TunnelInetConfigID_Type()
)
tunnelInetConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelInetConfigID.setStatus("current")
_TunnelInetConfigIfIndex_Type = InterfaceIndexOrZero
_TunnelInetConfigIfIndex_Object = MibTableColumn
tunnelInetConfigIfIndex = _TunnelInetConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 6),
    _TunnelInetConfigIfIndex_Type()
)
tunnelInetConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInetConfigIfIndex.setStatus("current")
_TunnelInetConfigStatus_Type = RowStatus
_TunnelInetConfigStatus_Object = MibTableColumn
tunnelInetConfigStatus = _TunnelInetConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 7),
    _TunnelInetConfigStatus_Type()
)
tunnelInetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tunnelInetConfigStatus.setStatus("current")
_TunnelInetConfigStorageType_Type = StorageType
_TunnelInetConfigStorageType_Object = MibTableColumn
tunnelInetConfigStorageType = _TunnelInetConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 8),
    _TunnelInetConfigStorageType_Type()
)
tunnelInetConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tunnelInetConfigStorageType.setStatus("current")
_TunnelMIBConformance_ObjectIdentity = ObjectIdentity
tunnelMIBConformance = _TunnelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131, 2)
)
_TunnelMIBCompliances_ObjectIdentity = ObjectIdentity
tunnelMIBCompliances = _TunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 1)
)
_TunnelMIBGroups_ObjectIdentity = ObjectIdentity
tunnelMIBGroups = _TunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 2)
)

# Managed Objects groups

tunnelMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 1)
)
tunnelMIBBasicGroup.setObjects(
      *(("TUNNEL-MIB", "tunnelIfLocalAddress"),
        ("TUNNEL-MIB", "tunnelIfRemoteAddress"),
        ("TUNNEL-MIB", "tunnelIfEncapsMethod"),
        ("TUNNEL-MIB", "tunnelIfHopLimit"),
        ("TUNNEL-MIB", "tunnelIfTOS"),
        ("TUNNEL-MIB", "tunnelIfSecurity"),
        ("TUNNEL-MIB", "tunnelConfigIfIndex"),
        ("TUNNEL-MIB", "tunnelConfigStatus"))
)
if mibBuilder.loadTexts:
    tunnelMIBBasicGroup.setStatus("deprecated")

tunnelMIBInetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 2)
)
tunnelMIBInetGroup.setObjects(
      *(("TUNNEL-MIB", "tunnelIfAddressType"),
        ("TUNNEL-MIB", "tunnelIfLocalInetAddress"),
        ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"),
        ("TUNNEL-MIB", "tunnelIfEncapsMethod"),
        ("TUNNEL-MIB", "tunnelIfEncapsLimit"),
        ("TUNNEL-MIB", "tunnelIfHopLimit"),
        ("TUNNEL-MIB", "tunnelIfTOS"),
        ("TUNNEL-MIB", "tunnelIfFlowLabel"),
        ("TUNNEL-MIB", "tunnelIfSecurity"),
        ("TUNNEL-MIB", "tunnelInetConfigIfIndex"),
        ("TUNNEL-MIB", "tunnelInetConfigStatus"),
        ("TUNNEL-MIB", "tunnelInetConfigStorageType"))
)
if mibBuilder.loadTexts:
    tunnelMIBInetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tunnelMIBCompliance.setStatus(
        "deprecated"
    )

tunnelMIBInetFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tunnelMIBInetFullCompliance.setStatus(
        "current"
    )

tunnelMIBInetReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tunnelMIBInetReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUNNEL-MIB",
    **{"tunnelMIB": tunnelMIB,
       "tunnelMIBObjects": tunnelMIBObjects,
       "tunnel": tunnel,
       "tunnelIfTable": tunnelIfTable,
       "tunnelIfEntry": tunnelIfEntry,
       "tunnelIfLocalAddress": tunnelIfLocalAddress,
       "tunnelIfRemoteAddress": tunnelIfRemoteAddress,
       "tunnelIfEncapsMethod": tunnelIfEncapsMethod,
       "tunnelIfHopLimit": tunnelIfHopLimit,
       "tunnelIfSecurity": tunnelIfSecurity,
       "tunnelIfTOS": tunnelIfTOS,
       "tunnelIfFlowLabel": tunnelIfFlowLabel,
       "tunnelIfAddressType": tunnelIfAddressType,
       "tunnelIfLocalInetAddress": tunnelIfLocalInetAddress,
       "tunnelIfRemoteInetAddress": tunnelIfRemoteInetAddress,
       "tunnelIfEncapsLimit": tunnelIfEncapsLimit,
       "tunnelConfigTable": tunnelConfigTable,
       "tunnelConfigEntry": tunnelConfigEntry,
       "tunnelConfigLocalAddress": tunnelConfigLocalAddress,
       "tunnelConfigRemoteAddress": tunnelConfigRemoteAddress,
       "tunnelConfigEncapsMethod": tunnelConfigEncapsMethod,
       "tunnelConfigID": tunnelConfigID,
       "tunnelConfigIfIndex": tunnelConfigIfIndex,
       "tunnelConfigStatus": tunnelConfigStatus,
       "tunnelInetConfigTable": tunnelInetConfigTable,
       "tunnelInetConfigEntry": tunnelInetConfigEntry,
       "tunnelInetConfigAddressType": tunnelInetConfigAddressType,
       "tunnelInetConfigLocalAddress": tunnelInetConfigLocalAddress,
       "tunnelInetConfigRemoteAddress": tunnelInetConfigRemoteAddress,
       "tunnelInetConfigEncapsMethod": tunnelInetConfigEncapsMethod,
       "tunnelInetConfigID": tunnelInetConfigID,
       "tunnelInetConfigIfIndex": tunnelInetConfigIfIndex,
       "tunnelInetConfigStatus": tunnelInetConfigStatus,
       "tunnelInetConfigStorageType": tunnelInetConfigStorageType,
       "tunnelMIBConformance": tunnelMIBConformance,
       "tunnelMIBCompliances": tunnelMIBCompliances,
       "tunnelMIBCompliance": tunnelMIBCompliance,
       "tunnelMIBInetFullCompliance": tunnelMIBInetFullCompliance,
       "tunnelMIBInetReadOnlyCompliance": tunnelMIBInetReadOnlyCompliance,
       "tunnelMIBGroups": tunnelMIBGroups,
       "tunnelMIBBasicGroup": tunnelMIBBasicGroup,
       "tunnelMIBInetGroup": tunnelMIBInetGroup}
)
