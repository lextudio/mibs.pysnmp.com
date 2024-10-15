# SNMP MIB module (GENERIC-3COM-VLAN-MIB-1-0-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENERIC-3COM-VLAN-MIB-1-0-1
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:29 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class A3ComVlanType(Integer32):
    """Custom type A3ComVlanType based on Integer32"""
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
        *(("vlanAppleTalkProtocol", 5),
          ("vlanDECNetProtocol", 8),
          ("vlanDefaultProtocols", 2),
          ("vlanIGMPProtocol", 13),
          ("vlanIPProtocol", 3),
          ("vlanIPXProtocol", 4),
          ("vlanISOProtocol", 7),
          ("vlanLayer2", 1),
          ("vlanNetBIOSProtocol", 9),
          ("vlanNetBeui", 15),
          ("vlanSNAProtocol", 10),
          ("vlanSessionLayer", 14),
          ("vlanVINESProtocol", 11),
          ("vlanX25Protocol", 12),
          ("vlanXNSProtocol", 6))
    )





class A3ComVlanEncapsType(Integer32):
    """Custom type A3ComVlanEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlanEncaps3ComProprietaryPDD", 1),
          ("vlanEncaps8021q", 2),
          ("vlanEncapsPre8021qONcore", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_GenVirtual_ObjectIdentity = ObjectIdentity
genVirtual = _GenVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14)
)
_A3ComVlanGroup_ObjectIdentity = ObjectIdentity
a3ComVlanGroup = _A3ComVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1)
)
_A3ComVlanGlobalMappingTable_Object = MibTable
a3ComVlanGlobalMappingTable = _A3ComVlanGlobalMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    a3ComVlanGlobalMappingTable.setStatus("mandatory")
_A3ComVlanGlobalMappingEntry_Object = MibTableRow
a3ComVlanGlobalMappingEntry = _A3ComVlanGlobalMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1)
)
a3ComVlanGlobalMappingEntry.setIndexNames(
    (0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanGlobalMappingIdentifier"),
)
if mibBuilder.loadTexts:
    a3ComVlanGlobalMappingEntry.setStatus("mandatory")


class _A3ComVlanGlobalMappingIdentifier_Type(Integer32):
    """Custom type a3ComVlanGlobalMappingIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComVlanGlobalMappingIdentifier_Type.__name__ = "Integer32"
_A3ComVlanGlobalMappingIdentifier_Object = MibTableColumn
a3ComVlanGlobalMappingIdentifier = _A3ComVlanGlobalMappingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 1),
    _A3ComVlanGlobalMappingIdentifier_Type()
)
a3ComVlanGlobalMappingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComVlanGlobalMappingIdentifier.setStatus("mandatory")
_A3ComVlanGlobalMappingIfIndex_Type = Integer32
_A3ComVlanGlobalMappingIfIndex_Object = MibTableColumn
a3ComVlanGlobalMappingIfIndex = _A3ComVlanGlobalMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 1, 1, 2),
    _A3ComVlanGlobalMappingIfIndex_Type()
)
a3ComVlanGlobalMappingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComVlanGlobalMappingIfIndex.setStatus("mandatory")
_A3ComVlanIfTable_Object = MibTable
a3ComVlanIfTable = _A3ComVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    a3ComVlanIfTable.setStatus("mandatory")
_A3ComVlanIfEntry_Object = MibTableRow
a3ComVlanIfEntry = _A3ComVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1)
)
a3ComVlanIfEntry.setIndexNames(
    (0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComVlanIfEntry.setStatus("mandatory")
_A3ComVlanIfIndex_Type = Integer32
_A3ComVlanIfIndex_Object = MibTableColumn
a3ComVlanIfIndex = _A3ComVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 1),
    _A3ComVlanIfIndex_Type()
)
a3ComVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfIndex.setStatus("mandatory")


class _A3ComVlanIfDescr_Type(DisplayString):
    """Custom type a3ComVlanIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_A3ComVlanIfDescr_Type.__name__ = "DisplayString"
_A3ComVlanIfDescr_Object = MibTableColumn
a3ComVlanIfDescr = _A3ComVlanIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 2),
    _A3ComVlanIfDescr_Type()
)
a3ComVlanIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfDescr.setStatus("mandatory")
_A3ComVlanIfType_Type = A3ComVlanType
_A3ComVlanIfType_Object = MibTableColumn
a3ComVlanIfType = _A3ComVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 3),
    _A3ComVlanIfType_Type()
)
a3ComVlanIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfType.setStatus("mandatory")


class _A3ComVlanIfGlobalIdentifier_Type(Integer32):
    """Custom type a3ComVlanIfGlobalIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComVlanIfGlobalIdentifier_Type.__name__ = "Integer32"
_A3ComVlanIfGlobalIdentifier_Object = MibTableColumn
a3ComVlanIfGlobalIdentifier = _A3ComVlanIfGlobalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 4),
    _A3ComVlanIfGlobalIdentifier_Type()
)
a3ComVlanIfGlobalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfGlobalIdentifier.setStatus("mandatory")
_A3ComVlanIfInfo_Type = OctetString
_A3ComVlanIfInfo_Object = MibTableColumn
a3ComVlanIfInfo = _A3ComVlanIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 5),
    _A3ComVlanIfInfo_Type()
)
a3ComVlanIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComVlanIfInfo.setStatus("mandatory")
_A3ComVlanIfStatus_Type = RowStatus
_A3ComVlanIfStatus_Object = MibTableColumn
a3ComVlanIfStatus = _A3ComVlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 6),
    _A3ComVlanIfStatus_Type()
)
a3ComVlanIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfStatus.setStatus("mandatory")
_A3ComVlanIfIgnoreStpFlag_Type = TruthValue
_A3ComVlanIfIgnoreStpFlag_Object = MibTableColumn
a3ComVlanIfIgnoreStpFlag = _A3ComVlanIfIgnoreStpFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 2, 1, 7),
    _A3ComVlanIfIgnoreStpFlag_Type()
)
a3ComVlanIfIgnoreStpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanIfIgnoreStpFlag.setStatus("mandatory")
_A3ComVlanProtocolsGroup_ObjectIdentity = ObjectIdentity
a3ComVlanProtocolsGroup = _A3ComVlanProtocolsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2)
)
_A3ComIpVlanTable_Object = MibTable
a3ComIpVlanTable = _A3ComIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComIpVlanTable.setStatus("mandatory")
_A3ComIpVlanEntry_Object = MibTableRow
a3ComIpVlanEntry = _A3ComIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1)
)
a3ComIpVlanEntry.setIndexNames(
    (0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComIpVlanEntry.setStatus("mandatory")
_A3ComIpVlanIpNetAddress_Type = IpAddress
_A3ComIpVlanIpNetAddress_Object = MibTableColumn
a3ComIpVlanIpNetAddress = _A3ComIpVlanIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 1),
    _A3ComIpVlanIpNetAddress_Type()
)
a3ComIpVlanIpNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComIpVlanIpNetAddress.setStatus("mandatory")
_A3ComIpVlanIpNetMask_Type = IpAddress
_A3ComIpVlanIpNetMask_Object = MibTableColumn
a3ComIpVlanIpNetMask = _A3ComIpVlanIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 2),
    _A3ComIpVlanIpNetMask_Type()
)
a3ComIpVlanIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComIpVlanIpNetMask.setStatus("mandatory")
_A3ComIpVlanStatus_Type = RowStatus
_A3ComIpVlanStatus_Object = MibTableColumn
a3ComIpVlanStatus = _A3ComIpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 2, 1, 1, 3),
    _A3ComIpVlanStatus_Type()
)
a3ComIpVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComIpVlanStatus.setStatus("mandatory")
_A3ComVirtualGroup_ObjectIdentity = ObjectIdentity
a3ComVirtualGroup = _A3ComVirtualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3)
)
_A3ComNextAvailableVirtIfIndex_Type = Integer32
_A3ComNextAvailableVirtIfIndex_Object = MibScalar
a3ComNextAvailableVirtIfIndex = _A3ComNextAvailableVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 3, 1),
    _A3ComNextAvailableVirtIfIndex_Type()
)
a3ComNextAvailableVirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComNextAvailableVirtIfIndex.setStatus("mandatory")
_A3ComEncapsulationGroup_ObjectIdentity = ObjectIdentity
a3ComEncapsulationGroup = _A3ComEncapsulationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4)
)
_A3ComVlanEncapsIfTable_Object = MibTable
a3ComVlanEncapsIfTable = _A3ComVlanEncapsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfTable.setStatus("mandatory")
_A3ComVlanEncapsIfEntry_Object = MibTableRow
a3ComVlanEncapsIfEntry = _A3ComVlanEncapsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1)
)
a3ComVlanEncapsIfEntry.setIndexNames(
    (0, "GENERIC-3COM-VLAN-MIB-1-0-1", "a3ComVlanEncapsIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfEntry.setStatus("mandatory")
_A3ComVlanEncapsIfIndex_Type = Integer32
_A3ComVlanEncapsIfIndex_Object = MibTableColumn
a3ComVlanEncapsIfIndex = _A3ComVlanEncapsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 1),
    _A3ComVlanEncapsIfIndex_Type()
)
a3ComVlanEncapsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfIndex.setStatus("mandatory")
_A3ComVlanEncapsIfType_Type = A3ComVlanEncapsType
_A3ComVlanEncapsIfType_Object = MibTableColumn
a3ComVlanEncapsIfType = _A3ComVlanEncapsIfType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 2),
    _A3ComVlanEncapsIfType_Type()
)
a3ComVlanEncapsIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfType.setStatus("mandatory")
_A3ComVlanEncapsIfTag_Type = Integer32
_A3ComVlanEncapsIfTag_Object = MibTableColumn
a3ComVlanEncapsIfTag = _A3ComVlanEncapsIfTag_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 3),
    _A3ComVlanEncapsIfTag_Type()
)
a3ComVlanEncapsIfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfTag.setStatus("mandatory")
_A3ComVlanEncapsIfStatus_Type = RowStatus
_A3ComVlanEncapsIfStatus_Object = MibTableColumn
a3ComVlanEncapsIfStatus = _A3ComVlanEncapsIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 4, 1, 1, 4),
    _A3ComVlanEncapsIfStatus_Type()
)
a3ComVlanEncapsIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComVlanEncapsIfStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERIC-3COM-VLAN-MIB-1-0-1",
    **{"RowStatus": RowStatus,
       "A3ComVlanType": A3ComVlanType,
       "A3ComVlanEncapsType": A3ComVlanEncapsType,
       "a3Com": a3Com,
       "generic": generic,
       "genExperimental": genExperimental,
       "genVirtual": genVirtual,
       "a3ComVlanGroup": a3ComVlanGroup,
       "a3ComVlanGlobalMappingTable": a3ComVlanGlobalMappingTable,
       "a3ComVlanGlobalMappingEntry": a3ComVlanGlobalMappingEntry,
       "a3ComVlanGlobalMappingIdentifier": a3ComVlanGlobalMappingIdentifier,
       "a3ComVlanGlobalMappingIfIndex": a3ComVlanGlobalMappingIfIndex,
       "a3ComVlanIfTable": a3ComVlanIfTable,
       "a3ComVlanIfEntry": a3ComVlanIfEntry,
       "a3ComVlanIfIndex": a3ComVlanIfIndex,
       "a3ComVlanIfDescr": a3ComVlanIfDescr,
       "a3ComVlanIfType": a3ComVlanIfType,
       "a3ComVlanIfGlobalIdentifier": a3ComVlanIfGlobalIdentifier,
       "a3ComVlanIfInfo": a3ComVlanIfInfo,
       "a3ComVlanIfStatus": a3ComVlanIfStatus,
       "a3ComVlanIfIgnoreStpFlag": a3ComVlanIfIgnoreStpFlag,
       "a3ComVlanProtocolsGroup": a3ComVlanProtocolsGroup,
       "a3ComIpVlanTable": a3ComIpVlanTable,
       "a3ComIpVlanEntry": a3ComIpVlanEntry,
       "a3ComIpVlanIpNetAddress": a3ComIpVlanIpNetAddress,
       "a3ComIpVlanIpNetMask": a3ComIpVlanIpNetMask,
       "a3ComIpVlanStatus": a3ComIpVlanStatus,
       "a3ComVirtualGroup": a3ComVirtualGroup,
       "a3ComNextAvailableVirtIfIndex": a3ComNextAvailableVirtIfIndex,
       "a3ComEncapsulationGroup": a3ComEncapsulationGroup,
       "a3ComVlanEncapsIfTable": a3ComVlanEncapsIfTable,
       "a3ComVlanEncapsIfEntry": a3ComVlanEncapsIfEntry,
       "a3ComVlanEncapsIfIndex": a3ComVlanEncapsIfIndex,
       "a3ComVlanEncapsIfType": a3ComVlanEncapsIfType,
       "a3ComVlanEncapsIfTag": a3ComVlanEncapsIfTag,
       "a3ComVlanEncapsIfStatus": a3ComVlanEncapsIfStatus}
)
