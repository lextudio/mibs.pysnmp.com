# SNMP MIB module (CISCO-DOT11-CONTEXT-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:49 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CiscoInetAddressMask,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInetAddressMask")

(InterfaceIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifPhysAddress")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11ContextServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110)
)
ciscoDot11ContextServicesMIB.setRevisions(
        ("2003-09-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDot11csNodeIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDot11csMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoDot11csMIBNotifications = _CiscoDot11csMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 0)
)
_CiscoDot11csMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11csMIBObjects = _CiscoDot11csMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1)
)
_CDot11csConfigGlobal_ObjectIdentity = ObjectIdentity
cDot11csConfigGlobal = _CDot11csConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1)
)


class _CDot11csServiceType_Type(Integer32):
    """Custom type cDot11csServiceType based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("rootWns", 4),
          ("wds", 2),
          ("wns", 3))
    )


_CDot11csServiceType_Type.__name__ = "Integer32"
_CDot11csServiceType_Object = MibScalar
cDot11csServiceType = _CDot11csServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 1),
    _CDot11csServiceType_Type()
)
cDot11csServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csServiceType.setStatus("current")
_CDot11csParentNodeIpAddressType_Type = InetAddressType
_CDot11csParentNodeIpAddressType_Object = MibScalar
cDot11csParentNodeIpAddressType = _CDot11csParentNodeIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 2),
    _CDot11csParentNodeIpAddressType_Type()
)
cDot11csParentNodeIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csParentNodeIpAddressType.setStatus("current")
_CDot11csParentNodeIpAddress_Type = InetAddress
_CDot11csParentNodeIpAddress_Object = MibScalar
cDot11csParentNodeIpAddress = _CDot11csParentNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 3),
    _CDot11csParentNodeIpAddress_Type()
)
cDot11csParentNodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csParentNodeIpAddress.setStatus("current")
_CDot11csPrimaryRootNodeAddrType_Type = InetAddressType
_CDot11csPrimaryRootNodeAddrType_Object = MibScalar
cDot11csPrimaryRootNodeAddrType = _CDot11csPrimaryRootNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 4),
    _CDot11csPrimaryRootNodeAddrType_Type()
)
cDot11csPrimaryRootNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csPrimaryRootNodeAddrType.setStatus("current")
_CDot11csPrimaryRootNodeAddr_Type = InetAddress
_CDot11csPrimaryRootNodeAddr_Object = MibScalar
cDot11csPrimaryRootNodeAddr = _CDot11csPrimaryRootNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 5),
    _CDot11csPrimaryRootNodeAddr_Type()
)
cDot11csPrimaryRootNodeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csPrimaryRootNodeAddr.setStatus("current")
_CDot11csSecondaryRootNodeAddrType_Type = InetAddressType
_CDot11csSecondaryRootNodeAddrType_Object = MibScalar
cDot11csSecondaryRootNodeAddrType = _CDot11csSecondaryRootNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 6),
    _CDot11csSecondaryRootNodeAddrType_Type()
)
cDot11csSecondaryRootNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csSecondaryRootNodeAddrType.setStatus("current")
_CDot11csSecondaryRootNodeAddr_Type = InetAddress
_CDot11csSecondaryRootNodeAddr_Object = MibScalar
cDot11csSecondaryRootNodeAddr = _CDot11csSecondaryRootNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 7),
    _CDot11csSecondaryRootNodeAddr_Type()
)
cDot11csSecondaryRootNodeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csSecondaryRootNodeAddr.setStatus("current")
_CDot11csCurrentRootNodeAddrType_Type = InetAddressType
_CDot11csCurrentRootNodeAddrType_Object = MibScalar
cDot11csCurrentRootNodeAddrType = _CDot11csCurrentRootNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 8),
    _CDot11csCurrentRootNodeAddrType_Type()
)
cDot11csCurrentRootNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csCurrentRootNodeAddrType.setStatus("current")
_CDot11csCurrentRootNodeAddr_Type = InetAddress
_CDot11csCurrentRootNodeAddr_Object = MibScalar
cDot11csCurrentRootNodeAddr = _CDot11csCurrentRootNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 9),
    _CDot11csCurrentRootNodeAddr_Type()
)
cDot11csCurrentRootNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csCurrentRootNodeAddr.setStatus("current")


class _CDot11csWnsEntityName_Type(SnmpAdminString):
    """Custom type cDot11csWnsEntityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11csWnsEntityName_Type.__name__ = "SnmpAdminString"
_CDot11csWnsEntityName_Object = MibScalar
cDot11csWnsEntityName = _CDot11csWnsEntityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 10),
    _CDot11csWnsEntityName_Type()
)
cDot11csWnsEntityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csWnsEntityName.setStatus("current")
_CDot11csMnaIpAddressType_Type = InetAddressType
_CDot11csMnaIpAddressType_Object = MibScalar
cDot11csMnaIpAddressType = _CDot11csMnaIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 11),
    _CDot11csMnaIpAddressType_Type()
)
cDot11csMnaIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnaIpAddressType.setStatus("current")
_CDot11csMnaIpAddress_Type = InetAddress
_CDot11csMnaIpAddress_Object = MibScalar
cDot11csMnaIpAddress = _CDot11csMnaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 12),
    _CDot11csMnaIpAddress_Type()
)
cDot11csMnaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnaIpAddress.setStatus("current")
_CDot11csIsRootNode_Type = TruthValue
_CDot11csIsRootNode_Object = MibScalar
cDot11csIsRootNode = _CDot11csIsRootNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 13),
    _CDot11csIsRootNode_Type()
)
cDot11csIsRootNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csIsRootNode.setStatus("current")


class _CDot11csNodeOperationMode_Type(Integer32):
    """Custom type cDot11csNodeOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminStandAlone", 1),
          ("fallbackStandAlone", 3),
          ("infrastructure", 2))
    )


_CDot11csNodeOperationMode_Type.__name__ = "Integer32"
_CDot11csNodeOperationMode_Object = MibScalar
cDot11csNodeOperationMode = _CDot11csNodeOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 14),
    _CDot11csNodeOperationMode_Type()
)
cDot11csNodeOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csNodeOperationMode.setStatus("current")
_CDot11csWnsTable_Object = MibTable
cDot11csWnsTable = _CDot11csWnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cDot11csWnsTable.setStatus("current")
_CDot11csWnsEntry_Object = MibTableRow
cDot11csWnsEntry = _CDot11csWnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1)
)
cDot11csWnsEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsIndex"),
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsAddrType"),
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsSubnetAddr"),
)
if mibBuilder.loadTexts:
    cDot11csWnsEntry.setStatus("current")


class _CDot11csWnsIndex_Type(SnmpAdminString):
    """Custom type cDot11csWnsIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11csWnsIndex_Type.__name__ = "SnmpAdminString"
_CDot11csWnsIndex_Object = MibTableColumn
cDot11csWnsIndex = _CDot11csWnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1, 1),
    _CDot11csWnsIndex_Type()
)
cDot11csWnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWnsIndex.setStatus("current")
_CDot11csWnsAddrType_Type = InetAddressType
_CDot11csWnsAddrType_Object = MibTableColumn
cDot11csWnsAddrType = _CDot11csWnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1, 2),
    _CDot11csWnsAddrType_Type()
)
cDot11csWnsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWnsAddrType.setStatus("current")
_CDot11csWnsSubnetAddr_Type = InetAddress
_CDot11csWnsSubnetAddr_Object = MibTableColumn
cDot11csWnsSubnetAddr = _CDot11csWnsSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1, 3),
    _CDot11csWnsSubnetAddr_Type()
)
cDot11csWnsSubnetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWnsSubnetAddr.setStatus("current")
_CDot11csWnsSubnetMask_Type = CiscoInetAddressMask
_CDot11csWnsSubnetMask_Object = MibTableColumn
cDot11csWnsSubnetMask = _CDot11csWnsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1, 4),
    _CDot11csWnsSubnetMask_Type()
)
cDot11csWnsSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWnsSubnetMask.setStatus("current")
_CDot11csWnsRowStatus_Type = RowStatus
_CDot11csWnsRowStatus_Object = MibTableColumn
cDot11csWnsRowStatus = _CDot11csWnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 15, 1, 5),
    _CDot11csWnsRowStatus_Type()
)
cDot11csWnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWnsRowStatus.setStatus("current")
_CDot11csWnmConfigTable_Object = MibTable
cDot11csWnmConfigTable = _CDot11csWnmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cDot11csWnmConfigTable.setStatus("current")
_CDot11csWnmConfigEntry_Object = MibTableRow
cDot11csWnmConfigEntry = _CDot11csWnmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16, 1)
)
cDot11csWnmConfigEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnmConfigIpAddressType"),
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnmConfigIpAddress"),
)
if mibBuilder.loadTexts:
    cDot11csWnmConfigEntry.setStatus("current")
_CDot11csWnmConfigIpAddressType_Type = InetAddressType
_CDot11csWnmConfigIpAddressType_Object = MibTableColumn
cDot11csWnmConfigIpAddressType = _CDot11csWnmConfigIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16, 1, 1),
    _CDot11csWnmConfigIpAddressType_Type()
)
cDot11csWnmConfigIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWnmConfigIpAddressType.setStatus("current")
_CDot11csWnmConfigIpAddress_Type = InetAddress
_CDot11csWnmConfigIpAddress_Object = MibTableColumn
cDot11csWnmConfigIpAddress = _CDot11csWnmConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16, 1, 2),
    _CDot11csWnmConfigIpAddress_Type()
)
cDot11csWnmConfigIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWnmConfigIpAddress.setStatus("current")


class _CDot11csWnmConfigAuthenState_Type(Integer32):
    """Custom type cDot11csWnmConfigAuthenState based on Integer32"""
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
        *(("authenticated", 4),
          ("authenticationFailed", 3),
          ("authenticationInProgess", 2),
          ("keysSetUpWithWds", 5),
          ("unauthenticated", 1))
    )


_CDot11csWnmConfigAuthenState_Type.__name__ = "Integer32"
_CDot11csWnmConfigAuthenState_Object = MibTableColumn
cDot11csWnmConfigAuthenState = _CDot11csWnmConfigAuthenState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16, 1, 3),
    _CDot11csWnmConfigAuthenState_Type()
)
cDot11csWnmConfigAuthenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csWnmConfigAuthenState.setStatus("current")
_CDot11csWnmConfigRowStatus_Type = RowStatus
_CDot11csWnmConfigRowStatus_Object = MibTableColumn
cDot11csWnmConfigRowStatus = _CDot11csWnmConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 16, 1, 4),
    _CDot11csWnmConfigRowStatus_Type()
)
cDot11csWnmConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWnmConfigRowStatus.setStatus("current")
_CDot11csWdsInstanceTable_Object = MibTable
cDot11csWdsInstanceTable = _CDot11csWdsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cDot11csWdsInstanceTable.setStatus("current")
_CDot11csWdsInstanceEntry_Object = MibTableRow
cDot11csWdsInstanceEntry = _CDot11csWdsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1)
)
cDot11csWdsInstanceEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstanceIndex"),
)
if mibBuilder.loadTexts:
    cDot11csWdsInstanceEntry.setStatus("current")


class _CDot11csWdsInstanceIndex_Type(Unsigned32):
    """Custom type cDot11csWdsInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CDot11csWdsInstanceIndex_Type.__name__ = "Unsigned32"
_CDot11csWdsInstanceIndex_Object = MibTableColumn
cDot11csWdsInstanceIndex = _CDot11csWdsInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 1),
    _CDot11csWdsInstanceIndex_Type()
)
cDot11csWdsInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csWdsInstanceIndex.setStatus("current")
_CDot11csWdsInstanceNodeIndex_Type = CDot11csNodeIndex
_CDot11csWdsInstanceNodeIndex_Object = MibTableColumn
cDot11csWdsInstanceNodeIndex = _CDot11csWdsInstanceNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 2),
    _CDot11csWdsInstanceNodeIndex_Type()
)
cDot11csWdsInstanceNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csWdsInstanceNodeIndex.setStatus("current")
_CDot11csWdsInstanceInterfaceIndex_Type = InterfaceIndex
_CDot11csWdsInstanceInterfaceIndex_Object = MibTableColumn
cDot11csWdsInstanceInterfaceIndex = _CDot11csWdsInstanceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 3),
    _CDot11csWdsInstanceInterfaceIndex_Type()
)
cDot11csWdsInstanceInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWdsInstanceInterfaceIndex.setStatus("current")


class _CDot11csWdsInstancePriority_Type(Unsigned32):
    """Custom type cDot11csWdsInstancePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CDot11csWdsInstancePriority_Type.__name__ = "Unsigned32"
_CDot11csWdsInstancePriority_Object = MibTableColumn
cDot11csWdsInstancePriority = _CDot11csWdsInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 4),
    _CDot11csWdsInstancePriority_Type()
)
cDot11csWdsInstancePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWdsInstancePriority.setStatus("current")


class _CDot11csWdsInstanceState_Type(Integer32):
    """Custom type cDot11csWdsInstanceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2),
          ("candidate", 3))
    )


_CDot11csWdsInstanceState_Type.__name__ = "Integer32"
_CDot11csWdsInstanceState_Object = MibTableColumn
cDot11csWdsInstanceState = _CDot11csWdsInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 5),
    _CDot11csWdsInstanceState_Type()
)
cDot11csWdsInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csWdsInstanceState.setStatus("current")
_CDot11csWdsInstanceRowStatus_Type = RowStatus
_CDot11csWdsInstanceRowStatus_Object = MibTableColumn
cDot11csWdsInstanceRowStatus = _CDot11csWdsInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 17, 1, 6),
    _CDot11csWdsInstanceRowStatus_Type()
)
cDot11csWdsInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cDot11csWdsInstanceRowStatus.setStatus("current")
_CDot11csStatusTable_Object = MibTable
cDot11csStatusTable = _CDot11csStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cDot11csStatusTable.setStatus("current")
_CDot11csStatusEntry_Object = MibTableRow
cDot11csStatusEntry = _CDot11csStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1)
)
cDot11csStatusEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusNodeIndex"),
)
if mibBuilder.loadTexts:
    cDot11csStatusEntry.setStatus("current")
_CDot11csStatusNodeIndex_Type = CDot11csNodeIndex
_CDot11csStatusNodeIndex_Object = MibTableColumn
cDot11csStatusNodeIndex = _CDot11csStatusNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 1),
    _CDot11csStatusNodeIndex_Type()
)
cDot11csStatusNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csStatusNodeIndex.setStatus("current")


class _CDot11csStatusAdminStatus_Type(Integer32):
    """Custom type cDot11csStatusAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CDot11csStatusAdminStatus_Type.__name__ = "Integer32"
_CDot11csStatusAdminStatus_Object = MibTableColumn
cDot11csStatusAdminStatus = _CDot11csStatusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 2),
    _CDot11csStatusAdminStatus_Type()
)
cDot11csStatusAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csStatusAdminStatus.setStatus("current")


class _CDot11csStatusOperStatus_Type(Integer32):
    """Custom type cDot11csStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CDot11csStatusOperStatus_Type.__name__ = "Integer32"
_CDot11csStatusOperStatus_Object = MibTableColumn
cDot11csStatusOperStatus = _CDot11csStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 3),
    _CDot11csStatusOperStatus_Type()
)
cDot11csStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusOperStatus.setStatus("current")
_CDot11csStatusChangeTimeStamp_Type = TimeStamp
_CDot11csStatusChangeTimeStamp_Object = MibTableColumn
cDot11csStatusChangeTimeStamp = _CDot11csStatusChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 4),
    _CDot11csStatusChangeTimeStamp_Type()
)
cDot11csStatusChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusChangeTimeStamp.setStatus("current")
_CDot11csStatusAdvtInterval_Type = TimeInterval
_CDot11csStatusAdvtInterval_Object = MibTableColumn
cDot11csStatusAdvtInterval = _CDot11csStatusAdvtInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 5),
    _CDot11csStatusAdvtInterval_Type()
)
cDot11csStatusAdvtInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusAdvtInterval.setStatus("current")
_CDot11csStatusInRegistrations_Type = Counter32
_CDot11csStatusInRegistrations_Object = MibTableColumn
cDot11csStatusInRegistrations = _CDot11csStatusInRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 6),
    _CDot11csStatusInRegistrations_Type()
)
cDot11csStatusInRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusInRegistrations.setStatus("current")
_CDot11csStatusInDeRegistrations_Type = Counter32
_CDot11csStatusInDeRegistrations_Object = MibTableColumn
cDot11csStatusInDeRegistrations = _CDot11csStatusInDeRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 7),
    _CDot11csStatusInDeRegistrations_Type()
)
cDot11csStatusInDeRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusInDeRegistrations.setStatus("current")
_CDot11csStatusCurrentlyRegisteredIns_Type = Gauge32
_CDot11csStatusCurrentlyRegisteredIns_Object = MibTableColumn
cDot11csStatusCurrentlyRegisteredIns = _CDot11csStatusCurrentlyRegisteredIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 8),
    _CDot11csStatusCurrentlyRegisteredIns_Type()
)
cDot11csStatusCurrentlyRegisteredIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusCurrentlyRegisteredIns.setStatus("current")
_CDot11csStatusSentAdvts_Type = Counter32
_CDot11csStatusSentAdvts_Object = MibTableColumn
cDot11csStatusSentAdvts = _CDot11csStatusSentAdvts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 18, 1, 9),
    _CDot11csStatusSentAdvts_Type()
)
cDot11csStatusSentAdvts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csStatusSentAdvts.setStatus("current")


class _CDot11csElectedAsWdsEnable_Type(TruthValue):
    """Custom type cDot11csElectedAsWdsEnable based on TruthValue"""


_CDot11csElectedAsWdsEnable_Object = MibScalar
cDot11csElectedAsWdsEnable = _CDot11csElectedAsWdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 19),
    _CDot11csElectedAsWdsEnable_Type()
)
cDot11csElectedAsWdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csElectedAsWdsEnable.setStatus("current")


class _CDot11csInRegisteredWithWsEnable_Type(TruthValue):
    """Custom type cDot11csInRegisteredWithWsEnable based on TruthValue"""


_CDot11csInRegisteredWithWsEnable_Object = MibScalar
cDot11csInRegisteredWithWsEnable = _CDot11csInRegisteredWithWsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 20),
    _CDot11csInRegisteredWithWsEnable_Type()
)
cDot11csInRegisteredWithWsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csInRegisteredWithWsEnable.setStatus("current")


class _CDot11csInDeRegisteredWithWsEnable_Type(TruthValue):
    """Custom type cDot11csInDeRegisteredWithWsEnable based on TruthValue"""


_CDot11csInDeRegisteredWithWsEnable_Object = MibScalar
cDot11csInDeRegisteredWithWsEnable = _CDot11csInDeRegisteredWithWsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 1, 21),
    _CDot11csInDeRegisteredWithWsEnable_Type()
)
cDot11csInDeRegisteredWithWsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11csInDeRegisteredWithWsEnable.setStatus("current")
_CDot11csDescendantIn_ObjectIdentity = ObjectIdentity
cDot11csDescendantIn = _CDot11csDescendantIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2)
)
_CDot11csDescendantInTable_Object = MibTable
cDot11csDescendantInTable = _CDot11csDescendantInTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cDot11csDescendantInTable.setStatus("current")
_CDot11csDescendantInEntry_Object = MibTableRow
cDot11csDescendantInEntry = _CDot11csDescendantInEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1)
)
cDot11csDescendantInEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusNodeIndex"),
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInId"),
)
if mibBuilder.loadTexts:
    cDot11csDescendantInEntry.setStatus("current")
_CDot11csDescendantInId_Type = MacAddress
_CDot11csDescendantInId_Object = MibTableColumn
cDot11csDescendantInId = _CDot11csDescendantInId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 1),
    _CDot11csDescendantInId_Type()
)
cDot11csDescendantInId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csDescendantInId.setStatus("current")


class _CDot11csDescendantInType_Type(Integer32):
    """Custom type cDot11csDescendantInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("wds", 2),
          ("wns", 3))
    )


_CDot11csDescendantInType_Type.__name__ = "Integer32"
_CDot11csDescendantInType_Object = MibTableColumn
cDot11csDescendantInType = _CDot11csDescendantInType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 2),
    _CDot11csDescendantInType_Type()
)
cDot11csDescendantInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInType.setStatus("current")
_CDot11csDescendantInIpAddressType_Type = InetAddressType
_CDot11csDescendantInIpAddressType_Object = MibTableColumn
cDot11csDescendantInIpAddressType = _CDot11csDescendantInIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 3),
    _CDot11csDescendantInIpAddressType_Type()
)
cDot11csDescendantInIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInIpAddressType.setStatus("current")
_CDot11csDescendantInIpAddress_Type = InetAddress
_CDot11csDescendantInIpAddress_Object = MibTableColumn
cDot11csDescendantInIpAddress = _CDot11csDescendantInIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 4),
    _CDot11csDescendantInIpAddress_Type()
)
cDot11csDescendantInIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInIpAddress.setStatus("current")
_CDot11csDescendantInRegistrationAge_Type = TimeInterval
_CDot11csDescendantInRegistrationAge_Object = MibTableColumn
cDot11csDescendantInRegistrationAge = _CDot11csDescendantInRegistrationAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 5),
    _CDot11csDescendantInRegistrationAge_Type()
)
cDot11csDescendantInRegistrationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInRegistrationAge.setStatus("current")
_CDot11csDescendantInCtkRefreshes_Type = Counter32
_CDot11csDescendantInCtkRefreshes_Object = MibTableColumn
cDot11csDescendantInCtkRefreshes = _CDot11csDescendantInCtkRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 6),
    _CDot11csDescendantInCtkRefreshes_Type()
)
cDot11csDescendantInCtkRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInCtkRefreshes.setStatus("current")
_CDot11csDescendantInNskExpiryTimeOut_Type = TimeInterval
_CDot11csDescendantInNskExpiryTimeOut_Object = MibTableColumn
cDot11csDescendantInNskExpiryTimeOut = _CDot11csDescendantInNskExpiryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 2, 1, 1, 7),
    _CDot11csDescendantInNskExpiryTimeOut_Type()
)
cDot11csDescendantInNskExpiryTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csDescendantInNskExpiryTimeOut.setStatus("current")
_CDot11csMn_ObjectIdentity = ObjectIdentity
cDot11csMn = _CDot11csMn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3)
)
_CDot11csMnContextTable_Object = MibTable
cDot11csMnContextTable = _CDot11csMnContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cDot11csMnContextTable.setStatus("current")
_CDot11csMnContextEntry_Object = MibTableRow
cDot11csMnContextEntry = _CDot11csMnContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1)
)
cDot11csMnContextEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusNodeIndex"),
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextId"),
)
if mibBuilder.loadTexts:
    cDot11csMnContextEntry.setStatus("current")
_CDot11csMnContextId_Type = MacAddress
_CDot11csMnContextId_Object = MibTableColumn
cDot11csMnContextId = _CDot11csMnContextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 1),
    _CDot11csMnContextId_Type()
)
cDot11csMnContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11csMnContextId.setStatus("current")


class _CDot11csMnContextSsid_Type(OctetString):
    """Custom type cDot11csMnContextSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11csMnContextSsid_Type.__name__ = "OctetString"
_CDot11csMnContextSsid_Object = MibTableColumn
cDot11csMnContextSsid = _CDot11csMnContextSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 2),
    _CDot11csMnContextSsid_Type()
)
cDot11csMnContextSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnContextSsid.setStatus("current")


class _CDot11csMnContextSystemName_Type(SnmpAdminString):
    """Custom type cDot11csMnContextSystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11csMnContextSystemName_Type.__name__ = "SnmpAdminString"
_CDot11csMnContextSystemName_Object = MibTableColumn
cDot11csMnContextSystemName = _CDot11csMnContextSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 3),
    _CDot11csMnContextSystemName_Type()
)
cDot11csMnContextSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnContextSystemName.setStatus("current")


class _CDot11csMnContextUserId_Type(SnmpAdminString):
    """Custom type cDot11csMnContextUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CDot11csMnContextUserId_Type.__name__ = "SnmpAdminString"
_CDot11csMnContextUserId_Object = MibTableColumn
cDot11csMnContextUserId = _CDot11csMnContextUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 4),
    _CDot11csMnContextUserId_Type()
)
cDot11csMnContextUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnContextUserId.setStatus("current")
_CDot11csMnContextIpAddressType_Type = InetAddressType
_CDot11csMnContextIpAddressType_Object = MibTableColumn
cDot11csMnContextIpAddressType = _CDot11csMnContextIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 5),
    _CDot11csMnContextIpAddressType_Type()
)
cDot11csMnContextIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnContextIpAddressType.setStatus("current")
_CDot11csMnContextIpAddress_Type = InetAddress
_CDot11csMnContextIpAddress_Object = MibTableColumn
cDot11csMnContextIpAddress = _CDot11csMnContextIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 6),
    _CDot11csMnContextIpAddress_Type()
)
cDot11csMnContextIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnContextIpAddress.setStatus("current")
_CDot11csMnParentInIpAddress_Type = InetAddress
_CDot11csMnParentInIpAddress_Object = MibTableColumn
cDot11csMnParentInIpAddress = _CDot11csMnParentInIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 7),
    _CDot11csMnParentInIpAddress_Type()
)
cDot11csMnParentInIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnParentInIpAddress.setStatus("current")
_CDot11csMnRegistrationAge_Type = TimeInterval
_CDot11csMnRegistrationAge_Object = MibTableColumn
cDot11csMnRegistrationAge = _CDot11csMnRegistrationAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 8),
    _CDot11csMnRegistrationAge_Type()
)
cDot11csMnRegistrationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnRegistrationAge.setStatus("current")
_CDot11csMnNskExpiryTimeOut_Type = TimeInterval
_CDot11csMnNskExpiryTimeOut_Object = MibTableColumn
cDot11csMnNskExpiryTimeOut = _CDot11csMnNskExpiryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 9),
    _CDot11csMnNskExpiryTimeOut_Type()
)
cDot11csMnNskExpiryTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnNskExpiryTimeOut.setStatus("current")


class _CDot11csMnCipherNegotiated_Type(Integer32):
    """Custom type cDot11csMnCipherNegotiated based on Integer32"""
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
        *(("ckip", 3),
          ("none", 0),
          ("other", 4),
          ("tkip", 2),
          ("wep", 1))
    )


_CDot11csMnCipherNegotiated_Type.__name__ = "Integer32"
_CDot11csMnCipherNegotiated_Object = MibTableColumn
cDot11csMnCipherNegotiated = _CDot11csMnCipherNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 1, 3, 1, 1, 10),
    _CDot11csMnCipherNegotiated_Type()
)
cDot11csMnCipherNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11csMnCipherNegotiated.setStatus("current")
_CiscoDot11csMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11csMIBConformance = _CiscoDot11csMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2)
)
_CiscoDot11csMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11csMIBCompliances = _CiscoDot11csMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 1)
)
_CiscoDot11csMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11csMIBGroups = _CiscoDot11csMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 2)
)

# Managed Objects groups

cDot11csConfigGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 2, 1)
)
cDot11csConfigGlobalGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csServiceType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csParentNodeIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csParentNodeIpAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csPrimaryRootNodeAddrType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csPrimaryRootNodeAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csSecondaryRootNodeAddrType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csSecondaryRootNodeAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csCurrentRootNodeAddrType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csCurrentRootNodeAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsEntityName"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnaIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnaIpAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csIsRootNode"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csNodeOperationMode"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsSubnetMask"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnsRowStatus"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnmConfigAuthenState"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWnmConfigRowStatus"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstanceNodeIndex"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstanceInterfaceIndex"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstancePriority"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstanceState"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csWdsInstanceRowStatus"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusAdminStatus"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusOperStatus"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusChangeTimeStamp"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusAdvtInterval"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusInRegistrations"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusInDeRegistrations"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusCurrentlyRegisteredIns"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csStatusSentAdvts"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csElectedAsWdsEnable"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csInRegisteredWithWsEnable"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csInDeRegisteredWithWsEnable"))
)
if mibBuilder.loadTexts:
    cDot11csConfigGlobalGroup.setStatus("current")

cDot11csDescendantInGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 2, 2)
)
cDot11csDescendantInGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInRegistrationAge"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInCtkRefreshes"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInNskExpiryTimeOut"))
)
if mibBuilder.loadTexts:
    cDot11csDescendantInGroup.setStatus("current")

cDot11csMnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 2, 3)
)
cDot11csMnGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextSsid"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextSystemName"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextUserId"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnContextIpAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnParentInIpAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnRegistrationAge"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnNskExpiryTimeOut"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csMnCipherNegotiated"))
)
if mibBuilder.loadTexts:
    cDot11csMnGroup.setStatus("current")


# Notification objects

cDot11csElectedAsWds = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 0, 1)
)
cDot11csElectedAsWds.setObjects(
    ("IF-MIB", "ifPhysAddress")
)
if mibBuilder.loadTexts:
    cDot11csElectedAsWds.setStatus(
        "current"
    )

cDot11csInRegisteredWithWs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 0, 2)
)
cDot11csInRegisteredWithWs.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddress"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    cDot11csInRegisteredWithWs.setStatus(
        "current"
    )

cDot11csInDeRegisteredWithWs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 0, 3)
)
cDot11csInDeRegisteredWithWs.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csDescendantInIpAddress"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    cDot11csInDeRegisteredWithWs.setStatus(
        "current"
    )


# Notifications groups

cDot11csMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 2, 4)
)
cDot11csMIBNotifGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csElectedAsWds"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csInRegisteredWithWs"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MIB", "cDot11csInDeRegisteredWithWs"))
)
if mibBuilder.loadTexts:
    cDot11csMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDot11csCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 110, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11csCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-CONTEXT-SERVICES-MIB",
    **{"CDot11csNodeIndex": CDot11csNodeIndex,
       "ciscoDot11ContextServicesMIB": ciscoDot11ContextServicesMIB,
       "ciscoDot11csMIBNotifications": ciscoDot11csMIBNotifications,
       "cDot11csElectedAsWds": cDot11csElectedAsWds,
       "cDot11csInRegisteredWithWs": cDot11csInRegisteredWithWs,
       "cDot11csInDeRegisteredWithWs": cDot11csInDeRegisteredWithWs,
       "ciscoDot11csMIBObjects": ciscoDot11csMIBObjects,
       "cDot11csConfigGlobal": cDot11csConfigGlobal,
       "cDot11csServiceType": cDot11csServiceType,
       "cDot11csParentNodeIpAddressType": cDot11csParentNodeIpAddressType,
       "cDot11csParentNodeIpAddress": cDot11csParentNodeIpAddress,
       "cDot11csPrimaryRootNodeAddrType": cDot11csPrimaryRootNodeAddrType,
       "cDot11csPrimaryRootNodeAddr": cDot11csPrimaryRootNodeAddr,
       "cDot11csSecondaryRootNodeAddrType": cDot11csSecondaryRootNodeAddrType,
       "cDot11csSecondaryRootNodeAddr": cDot11csSecondaryRootNodeAddr,
       "cDot11csCurrentRootNodeAddrType": cDot11csCurrentRootNodeAddrType,
       "cDot11csCurrentRootNodeAddr": cDot11csCurrentRootNodeAddr,
       "cDot11csWnsEntityName": cDot11csWnsEntityName,
       "cDot11csMnaIpAddressType": cDot11csMnaIpAddressType,
       "cDot11csMnaIpAddress": cDot11csMnaIpAddress,
       "cDot11csIsRootNode": cDot11csIsRootNode,
       "cDot11csNodeOperationMode": cDot11csNodeOperationMode,
       "cDot11csWnsTable": cDot11csWnsTable,
       "cDot11csWnsEntry": cDot11csWnsEntry,
       "cDot11csWnsIndex": cDot11csWnsIndex,
       "cDot11csWnsAddrType": cDot11csWnsAddrType,
       "cDot11csWnsSubnetAddr": cDot11csWnsSubnetAddr,
       "cDot11csWnsSubnetMask": cDot11csWnsSubnetMask,
       "cDot11csWnsRowStatus": cDot11csWnsRowStatus,
       "cDot11csWnmConfigTable": cDot11csWnmConfigTable,
       "cDot11csWnmConfigEntry": cDot11csWnmConfigEntry,
       "cDot11csWnmConfigIpAddressType": cDot11csWnmConfigIpAddressType,
       "cDot11csWnmConfigIpAddress": cDot11csWnmConfigIpAddress,
       "cDot11csWnmConfigAuthenState": cDot11csWnmConfigAuthenState,
       "cDot11csWnmConfigRowStatus": cDot11csWnmConfigRowStatus,
       "cDot11csWdsInstanceTable": cDot11csWdsInstanceTable,
       "cDot11csWdsInstanceEntry": cDot11csWdsInstanceEntry,
       "cDot11csWdsInstanceIndex": cDot11csWdsInstanceIndex,
       "cDot11csWdsInstanceNodeIndex": cDot11csWdsInstanceNodeIndex,
       "cDot11csWdsInstanceInterfaceIndex": cDot11csWdsInstanceInterfaceIndex,
       "cDot11csWdsInstancePriority": cDot11csWdsInstancePriority,
       "cDot11csWdsInstanceState": cDot11csWdsInstanceState,
       "cDot11csWdsInstanceRowStatus": cDot11csWdsInstanceRowStatus,
       "cDot11csStatusTable": cDot11csStatusTable,
       "cDot11csStatusEntry": cDot11csStatusEntry,
       "cDot11csStatusNodeIndex": cDot11csStatusNodeIndex,
       "cDot11csStatusAdminStatus": cDot11csStatusAdminStatus,
       "cDot11csStatusOperStatus": cDot11csStatusOperStatus,
       "cDot11csStatusChangeTimeStamp": cDot11csStatusChangeTimeStamp,
       "cDot11csStatusAdvtInterval": cDot11csStatusAdvtInterval,
       "cDot11csStatusInRegistrations": cDot11csStatusInRegistrations,
       "cDot11csStatusInDeRegistrations": cDot11csStatusInDeRegistrations,
       "cDot11csStatusCurrentlyRegisteredIns": cDot11csStatusCurrentlyRegisteredIns,
       "cDot11csStatusSentAdvts": cDot11csStatusSentAdvts,
       "cDot11csElectedAsWdsEnable": cDot11csElectedAsWdsEnable,
       "cDot11csInRegisteredWithWsEnable": cDot11csInRegisteredWithWsEnable,
       "cDot11csInDeRegisteredWithWsEnable": cDot11csInDeRegisteredWithWsEnable,
       "cDot11csDescendantIn": cDot11csDescendantIn,
       "cDot11csDescendantInTable": cDot11csDescendantInTable,
       "cDot11csDescendantInEntry": cDot11csDescendantInEntry,
       "cDot11csDescendantInId": cDot11csDescendantInId,
       "cDot11csDescendantInType": cDot11csDescendantInType,
       "cDot11csDescendantInIpAddressType": cDot11csDescendantInIpAddressType,
       "cDot11csDescendantInIpAddress": cDot11csDescendantInIpAddress,
       "cDot11csDescendantInRegistrationAge": cDot11csDescendantInRegistrationAge,
       "cDot11csDescendantInCtkRefreshes": cDot11csDescendantInCtkRefreshes,
       "cDot11csDescendantInNskExpiryTimeOut": cDot11csDescendantInNskExpiryTimeOut,
       "cDot11csMn": cDot11csMn,
       "cDot11csMnContextTable": cDot11csMnContextTable,
       "cDot11csMnContextEntry": cDot11csMnContextEntry,
       "cDot11csMnContextId": cDot11csMnContextId,
       "cDot11csMnContextSsid": cDot11csMnContextSsid,
       "cDot11csMnContextSystemName": cDot11csMnContextSystemName,
       "cDot11csMnContextUserId": cDot11csMnContextUserId,
       "cDot11csMnContextIpAddressType": cDot11csMnContextIpAddressType,
       "cDot11csMnContextIpAddress": cDot11csMnContextIpAddress,
       "cDot11csMnParentInIpAddress": cDot11csMnParentInIpAddress,
       "cDot11csMnRegistrationAge": cDot11csMnRegistrationAge,
       "cDot11csMnNskExpiryTimeOut": cDot11csMnNskExpiryTimeOut,
       "cDot11csMnCipherNegotiated": cDot11csMnCipherNegotiated,
       "ciscoDot11csMIBConformance": ciscoDot11csMIBConformance,
       "ciscoDot11csMIBCompliances": ciscoDot11csMIBCompliances,
       "ciscoDot11csCompliance": ciscoDot11csCompliance,
       "ciscoDot11csMIBGroups": ciscoDot11csMIBGroups,
       "cDot11csConfigGlobalGroup": cDot11csConfigGlobalGroup,
       "cDot11csDescendantInGroup": cDot11csDescendantInGroup,
       "cDot11csMnGroup": cDot11csMnGroup,
       "cDot11csMIBNotifGroup": cDot11csMIBNotifGroup}
)
