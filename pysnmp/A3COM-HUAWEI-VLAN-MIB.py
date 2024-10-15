# SNMP MIB module (A3COM-HUAWEI-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:17 2024
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

(hwInternetProtocol,
 hwLocal,
 vrpProtocol) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "hwInternetProtocol",
    "hwLocal",
    "vrpProtocol")

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

_Huawei_vlan_ObjectIdentity = ObjectIdentity
huawei_vlan = _Huawei_vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3)
)
_VLANMibRoutertCountTable_Object = MibTable
vLANMibRoutertCountTable = _VLANMibRoutertCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vLANMibRoutertCountTable.setStatus("mandatory")
_VLANMibRoutertCountEntry_Object = MibTableRow
vLANMibRoutertCountEntry = _VLANMibRoutertCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1, 1)
)
vLANMibRoutertCountEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VLAN-MIB", "vLANMibRouterPort"),
)
if mibBuilder.loadTexts:
    vLANMibRoutertCountEntry.setStatus("mandatory")
_VLANMibRouterPort_Type = Integer32
_VLANMibRouterPort_Object = MibTableColumn
vLANMibRouterPort = _VLANMibRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1, 1, 1),
    _VLANMibRouterPort_Type()
)
vLANMibRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterPort.setStatus("mandatory")
_VLANMibRouterPortPktDisc_Type = Counter32
_VLANMibRouterPortPktDisc_Object = MibTableColumn
vLANMibRouterPortPktDisc = _VLANMibRouterPortPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1, 1, 2),
    _VLANMibRouterPortPktDisc_Type()
)
vLANMibRouterPortPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterPortPktDisc.setStatus("mandatory")
_VLANMibRouterPortPktTran_Type = Counter32
_VLANMibRouterPortPktTran_Object = MibTableColumn
vLANMibRouterPortPktTran = _VLANMibRouterPortPktTran_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1, 1, 3),
    _VLANMibRouterPortPktTran_Type()
)
vLANMibRouterPortPktTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterPortPktTran.setStatus("mandatory")


class _VLANMibClearRouterStatistics_Type(Integer32):
    """Custom type vLANMibClearRouterStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_VLANMibClearRouterStatistics_Type.__name__ = "Integer32"
_VLANMibClearRouterStatistics_Object = MibTableColumn
vLANMibClearRouterStatistics = _VLANMibClearRouterStatistics_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 1, 1, 4),
    _VLANMibClearRouterStatistics_Type()
)
vLANMibClearRouterStatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vLANMibClearRouterStatistics.setStatus("mandatory")
_VLANMibRoutertVlanCountTable_Object = MibTable
vLANMibRoutertVlanCountTable = _VLANMibRoutertVlanCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    vLANMibRoutertVlanCountTable.setStatus("mandatory")
_VLANMibRoutertVlanCountEntry_Object = MibTableRow
vLANMibRoutertVlanCountEntry = _VLANMibRoutertVlanCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2, 1)
)
vLANMibRoutertVlanCountEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VLAN-MIB", "vLANMibRouterVID"),
)
if mibBuilder.loadTexts:
    vLANMibRoutertVlanCountEntry.setStatus("mandatory")


class _VLANMibRouterVID_Type(Integer32):
    """Custom type vLANMibRouterVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VLANMibRouterVID_Type.__name__ = "Integer32"
_VLANMibRouterVID_Object = MibTableColumn
vLANMibRouterVID = _VLANMibRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2, 1, 1),
    _VLANMibRouterVID_Type()
)
vLANMibRouterVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterVID.setStatus("mandatory")
_VLANMibRouterVlanPacketTran_Type = Counter32
_VLANMibRouterVlanPacketTran_Object = MibTableColumn
vLANMibRouterVlanPacketTran = _VLANMibRouterVlanPacketTran_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2, 1, 2),
    _VLANMibRouterVlanPacketTran_Type()
)
vLANMibRouterVlanPacketTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterVlanPacketTran.setStatus("mandatory")
_VLANMibRouterVlanPacketSent_Type = Counter32
_VLANMibRouterVlanPacketSent_Object = MibTableColumn
vLANMibRouterVlanPacketSent = _VLANMibRouterVlanPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2, 1, 3),
    _VLANMibRouterVlanPacketSent_Type()
)
vLANMibRouterVlanPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibRouterVlanPacketSent.setStatus("mandatory")


class _VLANMibClearVidStatistics_Type(Integer32):
    """Custom type vLANMibClearVidStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_VLANMibClearVidStatistics_Type.__name__ = "Integer32"
_VLANMibClearVidStatistics_Object = MibTableColumn
vLANMibClearVidStatistics = _VLANMibClearVidStatistics_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 2, 1, 4),
    _VLANMibClearVidStatistics_Type()
)
vLANMibClearVidStatistics.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vLANMibClearVidStatistics.setStatus("mandatory")
_VLANMibRouterMaxPkTable_Object = MibTable
vLANMibRouterMaxPkTable = _VLANMibRouterMaxPkTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 9)
)
if mibBuilder.loadTexts:
    vLANMibRouterMaxPkTable.setStatus("mandatory")
_VLANMibRouterMaxPkEntry_Object = MibTableRow
vLANMibRouterMaxPkEntry = _VLANMibRouterMaxPkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 9, 1)
)
vLANMibRouterMaxPkEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VLAN-MIB", "vLANMIbVID"),
)
if mibBuilder.loadTexts:
    vLANMibRouterMaxPkEntry.setStatus("mandatory")


class _VLANMIbVID_Type(Integer32):
    """Custom type vLANMIbVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VLANMIbVID_Type.__name__ = "Integer32"
_VLANMIbVID_Object = MibTableColumn
vLANMIbVID = _VLANMIbVID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 9, 1, 1),
    _VLANMIbVID_Type()
)
vLANMIbVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMIbVID.setStatus("mandatory")
_VLANMibRouterMaxPktProcessCount_Type = Unsigned32
_VLANMibRouterMaxPktProcessCount_Object = MibTableColumn
vLANMibRouterMaxPktProcessCount = _VLANMibRouterMaxPktProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 9, 1, 2),
    _VLANMibRouterMaxPktProcessCount_Type()
)
vLANMibRouterMaxPktProcessCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANMibRouterMaxPktProcessCount.setStatus("mandatory")
_VLANMibSubIfTable_Object = MibTable
vLANMibSubIfTable = _VLANMibSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 11)
)
if mibBuilder.loadTexts:
    vLANMibSubIfTable.setStatus("mandatory")
_VLANMibSubIfEntry_Object = MibTableRow
vLANMibSubIfEntry = _VLANMibSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 11, 1)
)
vLANMibSubIfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VLAN-MIB", "vLANMibSubIfPortIndex"),
)
if mibBuilder.loadTexts:
    vLANMibSubIfEntry.setStatus("mandatory")
_VLANMibSubIfPortIndex_Type = Integer32
_VLANMibSubIfPortIndex_Object = MibTableColumn
vLANMibSubIfPortIndex = _VLANMibSubIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 11, 1, 1),
    _VLANMibSubIfPortIndex_Type()
)
vLANMibSubIfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANMibSubIfPortIndex.setStatus("mandatory")


class _VLANMibSubIfEncapsulation_Type(Integer32):
    """Custom type vLANMibSubIfEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 2),
          ("iSL", 1))
    )


_VLANMibSubIfEncapsulation_Type.__name__ = "Integer32"
_VLANMibSubIfEncapsulation_Object = MibTableColumn
vLANMibSubIfEncapsulation = _VLANMibSubIfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 11, 1, 2),
    _VLANMibSubIfEncapsulation_Type()
)
vLANMibSubIfEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANMibSubIfEncapsulation.setStatus("mandatory")


class _VLANMibSubIfVID_Type(Integer32):
    """Custom type vLANMibSubIfVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VLANMibSubIfVID_Type.__name__ = "Integer32"
_VLANMibSubIfVID_Object = MibTableColumn
vLANMibSubIfVID = _VLANMibSubIfVID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 3, 3, 11, 1, 3),
    _VLANMibSubIfVID_Type()
)
vLANMibSubIfVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANMibSubIfVID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VLAN-MIB",
    **{"huawei-vlan": huawei_vlan,
       "vLANMibRoutertCountTable": vLANMibRoutertCountTable,
       "vLANMibRoutertCountEntry": vLANMibRoutertCountEntry,
       "vLANMibRouterPort": vLANMibRouterPort,
       "vLANMibRouterPortPktDisc": vLANMibRouterPortPktDisc,
       "vLANMibRouterPortPktTran": vLANMibRouterPortPktTran,
       "vLANMibClearRouterStatistics": vLANMibClearRouterStatistics,
       "vLANMibRoutertVlanCountTable": vLANMibRoutertVlanCountTable,
       "vLANMibRoutertVlanCountEntry": vLANMibRoutertVlanCountEntry,
       "vLANMibRouterVID": vLANMibRouterVID,
       "vLANMibRouterVlanPacketTran": vLANMibRouterVlanPacketTran,
       "vLANMibRouterVlanPacketSent": vLANMibRouterVlanPacketSent,
       "vLANMibClearVidStatistics": vLANMibClearVidStatistics,
       "vLANMibRouterMaxPkTable": vLANMibRouterMaxPkTable,
       "vLANMibRouterMaxPkEntry": vLANMibRouterMaxPkEntry,
       "vLANMIbVID": vLANMIbVID,
       "vLANMibRouterMaxPktProcessCount": vLANMibRouterMaxPktProcessCount,
       "vLANMibSubIfTable": vLANMibSubIfTable,
       "vLANMibSubIfEntry": vLANMibSubIfEntry,
       "vLANMibSubIfPortIndex": vLANMibSubIfPortIndex,
       "vLANMibSubIfEncapsulation": vLANMibSubIfEncapsulation,
       "vLANMibSubIfVID": vLANMibSubIfVID}
)
