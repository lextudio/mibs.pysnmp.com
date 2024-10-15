# SNMP MIB module (TERAWAVE-teraCon-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraCon-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:15 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_Connections_ObjectIdentity = ObjectIdentity
connections = _Connections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 2)
)
_ConTable_Object = MibTable
conTable = _ConTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1)
)
if mibBuilder.loadTexts:
    conTable.setStatus("mandatory")
_NextConTableEntryIndex_Type = Counter32
_NextConTableEntryIndex_Object = MibScalar
nextConTableEntryIndex = _NextConTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 1),
    _NextConTableEntryIndex_Type()
)
nextConTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextConTableEntryIndex.setStatus("mandatory")
_ConTableEntry_Object = MibTableRow
conTableEntry = _ConTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2)
)
conTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "circuitCONID"),
)
if mibBuilder.loadTexts:
    conTableEntry.setStatus("mandatory")
_CircuitCONID_Type = Counter32
_CircuitCONID_Object = MibTableColumn
circuitCONID = _CircuitCONID_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 1),
    _CircuitCONID_Type()
)
circuitCONID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitCONID.setStatus("mandatory")
_CircuitCONName_Type = OctetString
_CircuitCONName_Object = MibTableColumn
circuitCONName = _CircuitCONName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 2),
    _CircuitCONName_Type()
)
circuitCONName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitCONName.setStatus("mandatory")


class _ServiceCONType_Type(Integer32):
    """Custom type serviceCONType based on Integer32"""
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
        *(("lan-lan", 5),
          ("lan-pvc", 4),
          ("lan2pvc", 6),
          ("pvc-pvc", 3),
          ("tdm-pvc", 2),
          ("tdm-tdm", 1),
          ("vlan-trunk", 7))
    )


_ServiceCONType_Type.__name__ = "Integer32"
_ServiceCONType_Object = MibTableColumn
serviceCONType = _ServiceCONType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 3),
    _ServiceCONType_Type()
)
serviceCONType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceCONType.setStatus("mandatory")
_FirstCONIfIndex_Type = Integer32
_FirstCONIfIndex_Object = MibTableColumn
firstCONIfIndex = _FirstCONIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 4),
    _FirstCONIfIndex_Type()
)
firstCONIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstCONIfIndex.setStatus("mandatory")
_SecondCONIfIndex_Type = Integer32
_SecondCONIfIndex_Object = MibTableColumn
secondCONIfIndex = _SecondCONIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 5),
    _SecondCONIfIndex_Type()
)
secondCONIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondCONIfIndex.setStatus("mandatory")
_FirstCONVPI_Type = Integer32
_FirstCONVPI_Object = MibTableColumn
firstCONVPI = _FirstCONVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 6),
    _FirstCONVPI_Type()
)
firstCONVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstCONVPI.setStatus("mandatory")
_FirstCONVCI_Type = Integer32
_FirstCONVCI_Object = MibTableColumn
firstCONVCI = _FirstCONVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 7),
    _FirstCONVCI_Type()
)
firstCONVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstCONVCI.setStatus("mandatory")
_SecondCONVPI_Type = Integer32
_SecondCONVPI_Object = MibTableColumn
secondCONVPI = _SecondCONVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 8),
    _SecondCONVPI_Type()
)
secondCONVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondCONVPI.setStatus("mandatory")
_SecondCONVCI_Type = Integer32
_SecondCONVCI_Object = MibTableColumn
secondCONVCI = _SecondCONVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 9),
    _SecondCONVCI_Type()
)
secondCONVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondCONVCI.setStatus("mandatory")


class _ConVLANNumber_Type(Integer32):
    """Custom type conVLANNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ConVLANNumber_Type.__name__ = "Integer32"
_ConVLANNumber_Object = MibTableColumn
conVLANNumber = _ConVLANNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 10),
    _ConVLANNumber_Type()
)
conVLANNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conVLANNumber.setStatus("mandatory")


class _RequestedCONBW_Type(Integer32):
    """Custom type requestedCONBW based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("atm-vpi", 9),
          ("ds3", 5),
          ("e1", 4),
          ("e3", 6),
          ("oc3", 7),
          ("stm1", 8),
          ("t1", 3),
          ("vlan-c", 2))
    )


_RequestedCONBW_Type.__name__ = "Integer32"
_RequestedCONBW_Object = MibTableColumn
requestedCONBW = _RequestedCONBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 11),
    _RequestedCONBW_Type()
)
requestedCONBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requestedCONBW.setStatus("mandatory")
_FirstInternalVPI_Type = Integer32
_FirstInternalVPI_Object = MibTableColumn
firstInternalVPI = _FirstInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 12),
    _FirstInternalVPI_Type()
)
firstInternalVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firstInternalVPI.setStatus("mandatory")
_FirstInternalVCI_Type = Integer32
_FirstInternalVCI_Object = MibTableColumn
firstInternalVCI = _FirstInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 13),
    _FirstInternalVCI_Type()
)
firstInternalVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firstInternalVCI.setStatus("mandatory")
_SecondInternalVPI_Type = Integer32
_SecondInternalVPI_Object = MibTableColumn
secondInternalVPI = _SecondInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 14),
    _SecondInternalVPI_Type()
)
secondInternalVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondInternalVPI.setStatus("mandatory")
_SecondInternalVCI_Type = Integer32
_SecondInternalVCI_Object = MibTableColumn
secondInternalVCI = _SecondInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 15),
    _SecondInternalVCI_Type()
)
secondInternalVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondInternalVCI.setStatus("mandatory")


class _RowCONTableAction_Type(Integer32):
    """Custom type rowCONTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_RowCONTableAction_Type.__name__ = "Integer32"
_RowCONTableAction_Object = MibTableColumn
rowCONTableAction = _RowCONTableAction_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 16),
    _RowCONTableAction_Type()
)
rowCONTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rowCONTableAction.setStatus("mandatory")


class _ConStatus_Type(Integer32):
    """Custom type conStatus based on Integer32"""
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


_ConStatus_Type.__name__ = "Integer32"
_ConStatus_Object = MibTableColumn
conStatus = _ConStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 17),
    _ConStatus_Type()
)
conStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conStatus.setStatus("mandatory")
_ConUserId_Type = Integer32
_ConUserId_Object = MibTableColumn
conUserId = _ConUserId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 18),
    _ConUserId_Type()
)
conUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conUserId.setStatus("mandatory")
_ConUserConId_Type = Integer32
_ConUserConId_Object = MibTableColumn
conUserConId = _ConUserConId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 1, 2, 19),
    _ConUserConId_Type()
)
conUserConId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conUserConId.setStatus("mandatory")
_CircTable_Object = MibTable
circTable = _CircTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2)
)
if mibBuilder.loadTexts:
    circTable.setStatus("mandatory")
_CircTableEntry_Object = MibTableRow
circTableEntry = _CircTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2, 1)
)
circTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "circuitCONID"),
)
if mibBuilder.loadTexts:
    circTableEntry.setStatus("mandatory")
_CmFirstInternalVPI_Type = Integer32
_CmFirstInternalVPI_Object = MibTableColumn
cmFirstInternalVPI = _CmFirstInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 1),
    _CmFirstInternalVPI_Type()
)
cmFirstInternalVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFirstInternalVPI.setStatus("mandatory")
_CmFirstInternalVCI_Type = Integer32
_CmFirstInternalVCI_Object = MibTableColumn
cmFirstInternalVCI = _CmFirstInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 2),
    _CmFirstInternalVCI_Type()
)
cmFirstInternalVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFirstInternalVCI.setStatus("mandatory")
_CmSecondInternalVPI_Type = Integer32
_CmSecondInternalVPI_Object = MibTableColumn
cmSecondInternalVPI = _CmSecondInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 3),
    _CmSecondInternalVPI_Type()
)
cmSecondInternalVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecondInternalVPI.setStatus("mandatory")
_CmSecondInternalVCI_Type = Integer32
_CmSecondInternalVCI_Object = MibTableColumn
cmSecondInternalVCI = _CmSecondInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 2, 1, 4),
    _CmSecondInternalVCI_Type()
)
cmSecondInternalVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecondInternalVCI.setStatus("mandatory")
_BandwidthGroup_ObjectIdentity = ObjectIdentity
bandwidthGroup = _BandwidthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3)
)
_BwGroupTable_Object = MibTable
bwGroupTable = _BwGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1)
)
if mibBuilder.loadTexts:
    bwGroupTable.setStatus("mandatory")
_BwGroupTableNextId_Type = Integer32
_BwGroupTableNextId_Object = MibScalar
bwGroupTableNextId = _BwGroupTableNextId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 1),
    _BwGroupTableNextId_Type()
)
bwGroupTableNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwGroupTableNextId.setStatus("mandatory")
_BwGroupTableEntry_Object = MibTableRow
bwGroupTableEntry = _BwGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2)
)
bwGroupTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "bwGroupId"),
)
if mibBuilder.loadTexts:
    bwGroupTableEntry.setStatus("mandatory")
_BwGroupId_Type = Integer32
_BwGroupId_Object = MibTableColumn
bwGroupId = _BwGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 1),
    _BwGroupId_Type()
)
bwGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwGroupId.setStatus("mandatory")
_BwGroupName_Type = OctetString
_BwGroupName_Object = MibTableColumn
bwGroupName = _BwGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 2),
    _BwGroupName_Type()
)
bwGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGroupName.setStatus("mandatory")
_RequestedBandwidth_Type = Integer32
_RequestedBandwidth_Object = MibTableColumn
requestedBandwidth = _RequestedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 3),
    _RequestedBandwidth_Type()
)
requestedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requestedBandwidth.setStatus("mandatory")
_MaxBandwidth_Type = Integer32
_MaxBandwidth_Object = MibTableColumn
maxBandwidth = _MaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 4),
    _MaxBandwidth_Type()
)
maxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBandwidth.setStatus("mandatory")
_BwGroupPorts_Type = OctetString
_BwGroupPorts_Object = MibTableColumn
bwGroupPorts = _BwGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 5),
    _BwGroupPorts_Type()
)
bwGroupPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGroupPorts.setStatus("mandatory")


class _BwGroupTableAction_Type(Integer32):
    """Custom type bwGroupTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_BwGroupTableAction_Type.__name__ = "Integer32"
_BwGroupTableAction_Object = MibTableColumn
bwGroupTableAction = _BwGroupTableAction_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 3, 1, 2, 6),
    _BwGroupTableAction_Type()
)
bwGroupTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGroupTableAction.setStatus("mandatory")
_TeraStaticBWTable_Object = MibTable
teraStaticBWTable = _TeraStaticBWTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4)
)
if mibBuilder.loadTexts:
    teraStaticBWTable.setStatus("mandatory")
_TeraStaticBWTableEntry_Object = MibTableRow
teraStaticBWTableEntry = _TeraStaticBWTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1)
)
teraStaticBWTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "teraInstallSlotNumber"),
)
if mibBuilder.loadTexts:
    teraStaticBWTableEntry.setStatus("mandatory")
_TeraStaticBWTotal_Type = Integer32
_TeraStaticBWTotal_Object = MibTableColumn
teraStaticBWTotal = _TeraStaticBWTotal_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 1),
    _TeraStaticBWTotal_Type()
)
teraStaticBWTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticBWTotal.setStatus("mandatory")
_TeraStaticBWcbr_Type = Integer32
_TeraStaticBWcbr_Object = MibTableColumn
teraStaticBWcbr = _TeraStaticBWcbr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 2),
    _TeraStaticBWcbr_Type()
)
teraStaticBWcbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticBWcbr.setStatus("mandatory")
_TeraStaticBWaux_Type = Integer32
_TeraStaticBWaux_Object = MibTableColumn
teraStaticBWaux = _TeraStaticBWaux_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 3),
    _TeraStaticBWaux_Type()
)
teraStaticBWaux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticBWaux.setStatus("mandatory")
_TeraStaticBWvbr_Type = Integer32
_TeraStaticBWvbr_Object = MibTableColumn
teraStaticBWvbr = _TeraStaticBWvbr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 4),
    _TeraStaticBWvbr_Type()
)
teraStaticBWvbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticBWvbr.setStatus("mandatory")
_TeraStaticAllocBWvbr_Type = Integer32
_TeraStaticAllocBWvbr_Object = MibTableColumn
teraStaticAllocBWvbr = _TeraStaticAllocBWvbr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 4, 1, 5),
    _TeraStaticAllocBWvbr_Type()
)
teraStaticAllocBWvbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticAllocBWvbr.setStatus("mandatory")
_TeraStaticSplitBWTable_Object = MibTable
teraStaticSplitBWTable = _TeraStaticSplitBWTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5)
)
if mibBuilder.loadTexts:
    teraStaticSplitBWTable.setStatus("mandatory")
_TeraStaticSplitBWTableEntry_Object = MibTableRow
teraStaticSplitBWTableEntry = _TeraStaticSplitBWTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1)
)
teraStaticSplitBWTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-teraCon-MIB", "teraNEIDxSlotLevel1"),
)
if mibBuilder.loadTexts:
    teraStaticSplitBWTableEntry.setStatus("mandatory")
_TeraStaticSplitBWVBRConn_Type = Integer32
_TeraStaticSplitBWVBRConn_Object = MibTableColumn
teraStaticSplitBWVBRConn = _TeraStaticSplitBWVBRConn_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 1),
    _TeraStaticSplitBWVBRConn_Type()
)
teraStaticSplitBWVBRConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWVBRConn.setStatus("mandatory")
_TeraStaticSplitBWCBRConn_Type = Integer32
_TeraStaticSplitBWCBRConn_Object = MibTableColumn
teraStaticSplitBWCBRConn = _TeraStaticSplitBWCBRConn_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 2),
    _TeraStaticSplitBWCBRConn_Type()
)
teraStaticSplitBWCBRConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWCBRConn.setStatus("mandatory")
_TeraStaticSplitBWEffective_Type = Integer32
_TeraStaticSplitBWEffective_Object = MibTableColumn
teraStaticSplitBWEffective = _TeraStaticSplitBWEffective_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 3),
    _TeraStaticSplitBWEffective_Type()
)
teraStaticSplitBWEffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWEffective.setStatus("mandatory")
_TeraStaticSplitBWUnits_Type = Integer32
_TeraStaticSplitBWUnits_Object = MibTableColumn
teraStaticSplitBWUnits = _TeraStaticSplitBWUnits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 4),
    _TeraStaticSplitBWUnits_Type()
)
teraStaticSplitBWUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWUnits.setStatus("mandatory")
_TeraStaticSplitBWUnitsBandwidth_Type = Integer32
_TeraStaticSplitBWUnitsBandwidth_Object = MibTableColumn
teraStaticSplitBWUnitsBandwidth = _TeraStaticSplitBWUnitsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 5),
    _TeraStaticSplitBWUnitsBandwidth_Type()
)
teraStaticSplitBWUnitsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWUnitsBandwidth.setStatus("mandatory")
_TeraStaticSplitBWAllocated_Type = Integer32
_TeraStaticSplitBWAllocated_Object = MibTableColumn
teraStaticSplitBWAllocated = _TeraStaticSplitBWAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 5, 1, 6),
    _TeraStaticSplitBWAllocated_Type()
)
teraStaticSplitBWAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStaticSplitBWAllocated.setStatus("mandatory")
_TeraCraftCMTable_ObjectIdentity = ObjectIdentity
teraCraftCMTable = _TeraCraftCMTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 2, 6)
)


class _TeraCraftCMAdminStatus_Type(Integer32):
    """Custom type teraCraftCMAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("granted", 1),
          ("none", 0),
          ("notgranted", 2))
    )


_TeraCraftCMAdminStatus_Type.__name__ = "Integer32"
_TeraCraftCMAdminStatus_Object = MibScalar
teraCraftCMAdminStatus = _TeraCraftCMAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 6, 1),
    _TeraCraftCMAdminStatus_Type()
)
teraCraftCMAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCraftCMAdminStatus.setStatus("mandatory")


class _TeraCraftCMOperStatus_Type(Integer32):
    """Custom type teraCraftCMOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("wait4ack", 3))
    )


_TeraCraftCMOperStatus_Type.__name__ = "Integer32"
_TeraCraftCMOperStatus_Object = MibScalar
teraCraftCMOperStatus = _TeraCraftCMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 6, 2),
    _TeraCraftCMOperStatus_Type()
)
teraCraftCMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCraftCMOperStatus.setStatus("mandatory")
_TeraManagementPVCTable_Object = MibTable
teraManagementPVCTable = _TeraManagementPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7)
)
if mibBuilder.loadTexts:
    teraManagementPVCTable.setStatus("mandatory")
_TeraManagementPVCTableEntry_Object = MibTableRow
teraManagementPVCTableEntry = _TeraManagementPVCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1)
)
teraManagementPVCTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "teraManagementPVCNumber"),
)
if mibBuilder.loadTexts:
    teraManagementPVCTableEntry.setStatus("mandatory")


class _TeraManagementPVCNumber_Type(Integer32):
    """Custom type teraManagementPVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TeraManagementPVCNumber_Type.__name__ = "Integer32"
_TeraManagementPVCNumber_Object = MibTableColumn
teraManagementPVCNumber = _TeraManagementPVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 1),
    _TeraManagementPVCNumber_Type()
)
teraManagementPVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraManagementPVCNumber.setStatus("mandatory")


class _TeraManagementPVCAdminStatus_Type(Integer32):
    """Custom type teraManagementPVCAdminStatus based on Integer32"""
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


_TeraManagementPVCAdminStatus_Type.__name__ = "Integer32"
_TeraManagementPVCAdminStatus_Object = MibTableColumn
teraManagementPVCAdminStatus = _TeraManagementPVCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 2),
    _TeraManagementPVCAdminStatus_Type()
)
teraManagementPVCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCAdminStatus.setStatus("mandatory")


class _TeraManagementPVCPortIfIndex_Type(Integer32):
    """Custom type teraManagementPVCPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraManagementPVCPortIfIndex_Type.__name__ = "Integer32"
_TeraManagementPVCPortIfIndex_Object = MibTableColumn
teraManagementPVCPortIfIndex = _TeraManagementPVCPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 3),
    _TeraManagementPVCPortIfIndex_Type()
)
teraManagementPVCPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCPortIfIndex.setStatus("mandatory")


class _TeraManagementPVCVclVpi_Type(Integer32):
    """Custom type teraManagementPVCVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TeraManagementPVCVclVpi_Type.__name__ = "Integer32"
_TeraManagementPVCVclVpi_Object = MibTableColumn
teraManagementPVCVclVpi = _TeraManagementPVCVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 4),
    _TeraManagementPVCVclVpi_Type()
)
teraManagementPVCVclVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCVclVpi.setStatus("mandatory")


class _TeraManagementPVCVclVci_Type(Integer32):
    """Custom type teraManagementPVCVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TeraManagementPVCVclVci_Type.__name__ = "Integer32"
_TeraManagementPVCVclVci_Object = MibTableColumn
teraManagementPVCVclVci = _TeraManagementPVCVclVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 5),
    _TeraManagementPVCVclVci_Type()
)
teraManagementPVCVclVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCVclVci.setStatus("mandatory")
_TeraManagementPVCIPAddress_Type = IpAddress
_TeraManagementPVCIPAddress_Object = MibTableColumn
teraManagementPVCIPAddress = _TeraManagementPVCIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 6),
    _TeraManagementPVCIPAddress_Type()
)
teraManagementPVCIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCIPAddress.setStatus("mandatory")
_TeraManagementPVCIPNetMask_Type = IpAddress
_TeraManagementPVCIPNetMask_Object = MibTableColumn
teraManagementPVCIPNetMask = _TeraManagementPVCIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 7),
    _TeraManagementPVCIPNetMask_Type()
)
teraManagementPVCIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCIPNetMask.setStatus("mandatory")
_TeraManagementPVCIPGateway_Type = IpAddress
_TeraManagementPVCIPGateway_Object = MibTableColumn
teraManagementPVCIPGateway = _TeraManagementPVCIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 8),
    _TeraManagementPVCIPGateway_Type()
)
teraManagementPVCIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCIPGateway.setStatus("mandatory")


class _TeraManagementPVCIPMtu_Type(Integer32):
    """Custom type teraManagementPVCIPMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_TeraManagementPVCIPMtu_Type.__name__ = "Integer32"
_TeraManagementPVCIPMtu_Object = MibTableColumn
teraManagementPVCIPMtu = _TeraManagementPVCIPMtu_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 9),
    _TeraManagementPVCIPMtu_Type()
)
teraManagementPVCIPMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCIPMtu.setStatus("mandatory")


class _TeraManagementPVCIPEncapsType_Type(Integer32):
    """Custom type teraManagementPVCIPEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llcNone", 1),
          ("llcRoutedIPv4", 2),
          ("llcRoutedIPv4AtmArp", 3))
    )


_TeraManagementPVCIPEncapsType_Type.__name__ = "Integer32"
_TeraManagementPVCIPEncapsType_Object = MibTableColumn
teraManagementPVCIPEncapsType = _TeraManagementPVCIPEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 7, 1, 10),
    _TeraManagementPVCIPEncapsType_Type()
)
teraManagementPVCIPEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraManagementPVCIPEncapsType.setStatus("mandatory")
_TeraONTconTable_Object = MibTable
teraONTconTable = _TeraONTconTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8)
)
if mibBuilder.loadTexts:
    teraONTconTable.setStatus("mandatory")
_TeraONTconTableEntry_Object = MibTableRow
teraONTconTableEntry = _TeraONTconTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1)
)
teraONTconTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCon-MIB", "teraONTconID"),
)
if mibBuilder.loadTexts:
    teraONTconTableEntry.setStatus("mandatory")
_TeraONTconID_Type = Counter32
_TeraONTconID_Object = MibTableColumn
teraONTconID = _TeraONTconID_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 1),
    _TeraONTconID_Type()
)
teraONTconID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTconID.setStatus("mandatory")
_TeraONTfirstCONIfIndex_Type = Integer32
_TeraONTfirstCONIfIndex_Object = MibTableColumn
teraONTfirstCONIfIndex = _TeraONTfirstCONIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 2),
    _TeraONTfirstCONIfIndex_Type()
)
teraONTfirstCONIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTfirstCONIfIndex.setStatus("mandatory")
_TeraONTsecondCONIfIndex_Type = Integer32
_TeraONTsecondCONIfIndex_Object = MibTableColumn
teraONTsecondCONIfIndex = _TeraONTsecondCONIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 3),
    _TeraONTsecondCONIfIndex_Type()
)
teraONTsecondCONIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTsecondCONIfIndex.setStatus("mandatory")
_TeraONTfirstCONVPI_Type = Integer32
_TeraONTfirstCONVPI_Object = MibTableColumn
teraONTfirstCONVPI = _TeraONTfirstCONVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 4),
    _TeraONTfirstCONVPI_Type()
)
teraONTfirstCONVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTfirstCONVPI.setStatus("mandatory")
_TeraONTfirstCONVCI_Type = Integer32
_TeraONTfirstCONVCI_Object = MibTableColumn
teraONTfirstCONVCI = _TeraONTfirstCONVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 5),
    _TeraONTfirstCONVCI_Type()
)
teraONTfirstCONVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTfirstCONVCI.setStatus("mandatory")
_TeraONTsecondCONVPI_Type = Integer32
_TeraONTsecondCONVPI_Object = MibTableColumn
teraONTsecondCONVPI = _TeraONTsecondCONVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 6),
    _TeraONTsecondCONVPI_Type()
)
teraONTsecondCONVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTsecondCONVPI.setStatus("mandatory")
_TeraONTsecondCONVCI_Type = Integer32
_TeraONTsecondCONVCI_Object = MibTableColumn
teraONTsecondCONVCI = _TeraONTsecondCONVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 7),
    _TeraONTsecondCONVCI_Type()
)
teraONTsecondCONVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTsecondCONVCI.setStatus("mandatory")


class _TeraONTconVLANNumber_Type(Integer32):
    """Custom type teraONTconVLANNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TeraONTconVLANNumber_Type.__name__ = "Integer32"
_TeraONTconVLANNumber_Object = MibTableColumn
teraONTconVLANNumber = _TeraONTconVLANNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 8),
    _TeraONTconVLANNumber_Type()
)
teraONTconVLANNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTconVLANNumber.setStatus("mandatory")


class _TeraONTrequestedCONBW_Type(Integer32):
    """Custom type teraONTrequestedCONBW based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("atm-vpi", 9),
          ("ds3", 5),
          ("e1", 4),
          ("e3", 6),
          ("oc3", 7),
          ("stm1", 8),
          ("t1", 3),
          ("vlan-c", 2))
    )


_TeraONTrequestedCONBW_Type.__name__ = "Integer32"
_TeraONTrequestedCONBW_Object = MibTableColumn
teraONTrequestedCONBW = _TeraONTrequestedCONBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 9),
    _TeraONTrequestedCONBW_Type()
)
teraONTrequestedCONBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTrequestedCONBW.setStatus("mandatory")
_TeraONTfirstInternalVPI_Type = Integer32
_TeraONTfirstInternalVPI_Object = MibTableColumn
teraONTfirstInternalVPI = _TeraONTfirstInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 10),
    _TeraONTfirstInternalVPI_Type()
)
teraONTfirstInternalVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTfirstInternalVPI.setStatus("mandatory")
_TeraONTfirstInternalVCI_Type = Integer32
_TeraONTfirstInternalVCI_Object = MibTableColumn
teraONTfirstInternalVCI = _TeraONTfirstInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 11),
    _TeraONTfirstInternalVCI_Type()
)
teraONTfirstInternalVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTfirstInternalVCI.setStatus("mandatory")
_TeraONTsecondInternalVPI_Type = Integer32
_TeraONTsecondInternalVPI_Object = MibTableColumn
teraONTsecondInternalVPI = _TeraONTsecondInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 12),
    _TeraONTsecondInternalVPI_Type()
)
teraONTsecondInternalVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTsecondInternalVPI.setStatus("mandatory")
_TeraONTsecondInternalVCI_Type = Integer32
_TeraONTsecondInternalVCI_Object = MibTableColumn
teraONTsecondInternalVCI = _TeraONTsecondInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 13),
    _TeraONTsecondInternalVCI_Type()
)
teraONTsecondInternalVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTsecondInternalVCI.setStatus("mandatory")


class _TeraONTconStatus_Type(Integer32):
    """Custom type teraONTconStatus based on Integer32"""
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


_TeraONTconStatus_Type.__name__ = "Integer32"
_TeraONTconStatus_Object = MibTableColumn
teraONTconStatus = _TeraONTconStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 2, 8, 1, 14),
    _TeraONTconStatus_Type()
)
teraONTconStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraONTconStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraCon-MIB",
    **{"terawave": terawave,
       "connections": connections,
       "conTable": conTable,
       "nextConTableEntryIndex": nextConTableEntryIndex,
       "conTableEntry": conTableEntry,
       "circuitCONID": circuitCONID,
       "circuitCONName": circuitCONName,
       "serviceCONType": serviceCONType,
       "firstCONIfIndex": firstCONIfIndex,
       "secondCONIfIndex": secondCONIfIndex,
       "firstCONVPI": firstCONVPI,
       "firstCONVCI": firstCONVCI,
       "secondCONVPI": secondCONVPI,
       "secondCONVCI": secondCONVCI,
       "conVLANNumber": conVLANNumber,
       "requestedCONBW": requestedCONBW,
       "firstInternalVPI": firstInternalVPI,
       "firstInternalVCI": firstInternalVCI,
       "secondInternalVPI": secondInternalVPI,
       "secondInternalVCI": secondInternalVCI,
       "rowCONTableAction": rowCONTableAction,
       "conStatus": conStatus,
       "conUserId": conUserId,
       "conUserConId": conUserConId,
       "circTable": circTable,
       "circTableEntry": circTableEntry,
       "cmFirstInternalVPI": cmFirstInternalVPI,
       "cmFirstInternalVCI": cmFirstInternalVCI,
       "cmSecondInternalVPI": cmSecondInternalVPI,
       "cmSecondInternalVCI": cmSecondInternalVCI,
       "bandwidthGroup": bandwidthGroup,
       "bwGroupTable": bwGroupTable,
       "bwGroupTableNextId": bwGroupTableNextId,
       "bwGroupTableEntry": bwGroupTableEntry,
       "bwGroupId": bwGroupId,
       "bwGroupName": bwGroupName,
       "requestedBandwidth": requestedBandwidth,
       "maxBandwidth": maxBandwidth,
       "bwGroupPorts": bwGroupPorts,
       "bwGroupTableAction": bwGroupTableAction,
       "teraStaticBWTable": teraStaticBWTable,
       "teraStaticBWTableEntry": teraStaticBWTableEntry,
       "teraStaticBWTotal": teraStaticBWTotal,
       "teraStaticBWcbr": teraStaticBWcbr,
       "teraStaticBWaux": teraStaticBWaux,
       "teraStaticBWvbr": teraStaticBWvbr,
       "teraStaticAllocBWvbr": teraStaticAllocBWvbr,
       "teraStaticSplitBWTable": teraStaticSplitBWTable,
       "teraStaticSplitBWTableEntry": teraStaticSplitBWTableEntry,
       "teraStaticSplitBWVBRConn": teraStaticSplitBWVBRConn,
       "teraStaticSplitBWCBRConn": teraStaticSplitBWCBRConn,
       "teraStaticSplitBWEffective": teraStaticSplitBWEffective,
       "teraStaticSplitBWUnits": teraStaticSplitBWUnits,
       "teraStaticSplitBWUnitsBandwidth": teraStaticSplitBWUnitsBandwidth,
       "teraStaticSplitBWAllocated": teraStaticSplitBWAllocated,
       "teraCraftCMTable": teraCraftCMTable,
       "teraCraftCMAdminStatus": teraCraftCMAdminStatus,
       "teraCraftCMOperStatus": teraCraftCMOperStatus,
       "teraManagementPVCTable": teraManagementPVCTable,
       "teraManagementPVCTableEntry": teraManagementPVCTableEntry,
       "teraManagementPVCNumber": teraManagementPVCNumber,
       "teraManagementPVCAdminStatus": teraManagementPVCAdminStatus,
       "teraManagementPVCPortIfIndex": teraManagementPVCPortIfIndex,
       "teraManagementPVCVclVpi": teraManagementPVCVclVpi,
       "teraManagementPVCVclVci": teraManagementPVCVclVci,
       "teraManagementPVCIPAddress": teraManagementPVCIPAddress,
       "teraManagementPVCIPNetMask": teraManagementPVCIPNetMask,
       "teraManagementPVCIPGateway": teraManagementPVCIPGateway,
       "teraManagementPVCIPMtu": teraManagementPVCIPMtu,
       "teraManagementPVCIPEncapsType": teraManagementPVCIPEncapsType,
       "teraONTconTable": teraONTconTable,
       "teraONTconTableEntry": teraONTconTableEntry,
       "teraONTconID": teraONTconID,
       "teraONTfirstCONIfIndex": teraONTfirstCONIfIndex,
       "teraONTsecondCONIfIndex": teraONTsecondCONIfIndex,
       "teraONTfirstCONVPI": teraONTfirstCONVPI,
       "teraONTfirstCONVCI": teraONTfirstCONVCI,
       "teraONTsecondCONVPI": teraONTsecondCONVPI,
       "teraONTsecondCONVCI": teraONTsecondCONVCI,
       "teraONTconVLANNumber": teraONTconVLANNumber,
       "teraONTrequestedCONBW": teraONTrequestedCONBW,
       "teraONTfirstInternalVPI": teraONTfirstInternalVPI,
       "teraONTfirstInternalVCI": teraONTfirstInternalVCI,
       "teraONTsecondInternalVPI": teraONTsecondInternalVPI,
       "teraONTsecondInternalVCI": teraONTsecondInternalVCI,
       "teraONTconStatus": teraONTconStatus}
)
