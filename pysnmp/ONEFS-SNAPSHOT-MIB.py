# SNMP MIB module (ONEFS-SNAPSHOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEFS-SNAPSHOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:10 2024
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

(TimeTicks64,
 onefs) = mibBuilder.importSymbols(
    "ONEFS-MIB",
    "TimeTicks64",
    "onefs")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oneFSss = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SsVersion_Type(DisplayString):
    """Custom type ssVersion based on DisplayString"""
    defaultValue = 0


_SsVersion_Object = MibScalar
ssVersion = _SsVersion_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 1),
    _SsVersion_Type()
)
ssVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssVersion.setStatus("current")


class _SsLocalNodeId_Type(Integer32):
    """Custom type ssLocalNodeId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SsLocalNodeId_Type.__name__ = "Integer32"
_SsLocalNodeId_Object = MibScalar
ssLocalNodeId = _SsLocalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 2),
    _SsLocalNodeId_Type()
)
ssLocalNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssLocalNodeId.setStatus("current")


class _SsTimeStart_Type(TimeTicks64):
    """Custom type ssTimeStart based on TimeTicks64"""
    defaultValue = 0


_SsTimeStart_Object = MibScalar
ssTimeStart = _SsTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 3),
    _SsTimeStart_Type()
)
ssTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTimeStart.setStatus("current")


class _SsTimeEnd_Type(TimeTicks64):
    """Custom type ssTimeEnd based on TimeTicks64"""
    defaultValue = 0


_SsTimeEnd_Object = MibScalar
ssTimeEnd = _SsTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 4),
    _SsTimeEnd_Type()
)
ssTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTimeEnd.setStatus("current")
_SsGlobal_ObjectIdentity = ObjectIdentity
ssGlobal = _SsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5)
)
_SsDisk_ObjectIdentity = ObjectIdentity
ssDisk = _SsDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 1)
)


class _SsFreeBlocks_Type(Counter64):
    """Custom type ssFreeBlocks based on Counter64"""
    defaultValue = 0


_SsFreeBlocks_Object = MibScalar
ssFreeBlocks = _SsFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 1),
    _SsFreeBlocks_Type()
)
ssFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFreeBlocks.setStatus("current")


class _SsTotalBlocks_Type(Counter64):
    """Custom type ssTotalBlocks based on Counter64"""
    defaultValue = 0


_SsTotalBlocks_Object = MibScalar
ssTotalBlocks = _SsTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 2),
    _SsTotalBlocks_Type()
)
ssTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTotalBlocks.setStatus("current")


class _SsAvailableBlocks_Type(Counter64):
    """Custom type ssAvailableBlocks based on Counter64"""
    defaultValue = 0


_SsAvailableBlocks_Object = MibScalar
ssAvailableBlocks = _SsAvailableBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 3),
    _SsAvailableBlocks_Type()
)
ssAvailableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssAvailableBlocks.setStatus("current")


class _SsBlockSize_Type(Integer32):
    """Custom type ssBlockSize based on Integer32"""
    defaultValue = 0


_SsBlockSize_Object = MibScalar
ssBlockSize = _SsBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 4),
    _SsBlockSize_Type()
)
ssBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssBlockSize.setStatus("current")
_SsNet_ObjectIdentity = ObjectIdentity
ssNet = _SsNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2)
)


class _SsNetBytesIn_Type(Counter64):
    """Custom type ssNetBytesIn based on Counter64"""
    defaultValue = 0


_SsNetBytesIn_Object = MibScalar
ssNetBytesIn = _SsNetBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 3),
    _SsNetBytesIn_Type()
)
ssNetBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNetBytesIn.setStatus("current")


class _SsNetBytesOut_Type(Counter64):
    """Custom type ssNetBytesOut based on Counter64"""
    defaultValue = 0


_SsNetBytesOut_Object = MibScalar
ssNetBytesOut = _SsNetBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 4),
    _SsNetBytesOut_Type()
)
ssNetBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNetBytesOut.setStatus("current")


class _SsFilesystemBytesIn_Type(Counter64):
    """Custom type ssFilesystemBytesIn based on Counter64"""
    defaultValue = 0


_SsFilesystemBytesIn_Object = MibScalar
ssFilesystemBytesIn = _SsFilesystemBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 5),
    _SsFilesystemBytesIn_Type()
)
ssFilesystemBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFilesystemBytesIn.setStatus("current")


class _SsFilesystemBytesOut_Type(Counter64):
    """Custom type ssFilesystemBytesOut based on Counter64"""
    defaultValue = 0


_SsFilesystemBytesOut_Object = MibScalar
ssFilesystemBytesOut = _SsFilesystemBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 6),
    _SsFilesystemBytesOut_Type()
)
ssFilesystemBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFilesystemBytesOut.setStatus("current")


class _SsNetBitsPerSecIn_Type(Counter64):
    """Custom type ssNetBitsPerSecIn based on Counter64"""
    defaultValue = 0


_SsNetBitsPerSecIn_Object = MibScalar
ssNetBitsPerSecIn = _SsNetBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 9),
    _SsNetBitsPerSecIn_Type()
)
ssNetBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNetBitsPerSecIn.setStatus("current")


class _SsNetBitsPerSecOut_Type(Counter64):
    """Custom type ssNetBitsPerSecOut based on Counter64"""
    defaultValue = 0


_SsNetBitsPerSecOut_Object = MibScalar
ssNetBitsPerSecOut = _SsNetBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 10),
    _SsNetBitsPerSecOut_Type()
)
ssNetBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNetBitsPerSecOut.setStatus("current")


class _SsFilesystemBitsPerSecIn_Type(Counter64):
    """Custom type ssFilesystemBitsPerSecIn based on Counter64"""
    defaultValue = 0


_SsFilesystemBitsPerSecIn_Object = MibScalar
ssFilesystemBitsPerSecIn = _SsFilesystemBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 11),
    _SsFilesystemBitsPerSecIn_Type()
)
ssFilesystemBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFilesystemBitsPerSecIn.setStatus("current")


class _SsFilesystemBitsPerSecOut_Type(Counter64):
    """Custom type ssFilesystemBitsPerSecOut based on Counter64"""
    defaultValue = 0


_SsFilesystemBitsPerSecOut_Object = MibScalar
ssFilesystemBitsPerSecOut = _SsFilesystemBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 12),
    _SsFilesystemBitsPerSecOut_Type()
)
ssFilesystemBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFilesystemBitsPerSecOut.setStatus("current")
_SsSystem_ObjectIdentity = ObjectIdentity
ssSystem = _SsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 3)
)


class _SsClusterName_Type(DisplayString):
    """Custom type ssClusterName based on DisplayString"""
    defaultValue = 0


_SsClusterName_Object = MibScalar
ssClusterName = _SsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 1),
    _SsClusterName_Type()
)
ssClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssClusterName.setStatus("current")


class _SsClusterHealth_Type(DisplayString):
    """Custom type ssClusterHealth based on DisplayString"""
    defaultValue = 0


_SsClusterHealth_Object = MibScalar
ssClusterHealth = _SsClusterHealth_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 4),
    _SsClusterHealth_Type()
)
ssClusterHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssClusterHealth.setStatus("current")


class _SsConfiguredNodes_Type(Integer32):
    """Custom type ssConfiguredNodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SsConfiguredNodes_Type.__name__ = "Integer32"
_SsConfiguredNodes_Object = MibScalar
ssConfiguredNodes = _SsConfiguredNodes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 5),
    _SsConfiguredNodes_Type()
)
ssConfiguredNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssConfiguredNodes.setStatus("current")


class _SsOnlineNodes_Type(Integer32):
    """Custom type ssOnlineNodes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SsOnlineNodes_Type.__name__ = "Integer32"
_SsOnlineNodes_Object = MibScalar
ssOnlineNodes = _SsOnlineNodes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 6),
    _SsOnlineNodes_Type()
)
ssOnlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssOnlineNodes.setStatus("current")
_SsNodeInfo_ObjectIdentity = ObjectIdentity
ssNodeInfo = _SsNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6)
)
_SsNodeTable_Object = MibTable
ssNodeTable = _SsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1)
)
if mibBuilder.loadTexts:
    ssNodeTable.setStatus("current")
_SsNodeEntry_Object = MibTableRow
ssNodeEntry = _SsNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1)
)
ssNodeEntry.setIndexNames(
    (0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"),
)
if mibBuilder.loadTexts:
    ssNodeEntry.setStatus("current")


class _SsNodeIndex_Type(Integer32):
    """Custom type ssNodeIndex based on Integer32"""
    defaultValue = 0


_SsNodeIndex_Object = MibTableColumn
ssNodeIndex = _SsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 1),
    _SsNodeIndex_Type()
)
ssNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeIndex.setStatus("current")


class _SsNodeFreeBlocks_Type(Counter64):
    """Custom type ssNodeFreeBlocks based on Counter64"""
    defaultValue = 0


_SsNodeFreeBlocks_Object = MibTableColumn
ssNodeFreeBlocks = _SsNodeFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 2),
    _SsNodeFreeBlocks_Type()
)
ssNodeFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeFreeBlocks.setStatus("current")


class _SsNodeTotalBlocks_Type(Counter64):
    """Custom type ssNodeTotalBlocks based on Counter64"""
    defaultValue = 0


_SsNodeTotalBlocks_Object = MibTableColumn
ssNodeTotalBlocks = _SsNodeTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 3),
    _SsNodeTotalBlocks_Type()
)
ssNodeTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeTotalBlocks.setStatus("current")


class _SsNodeAvailBlocks_Type(Counter64):
    """Custom type ssNodeAvailBlocks based on Counter64"""
    defaultValue = 0


_SsNodeAvailBlocks_Object = MibTableColumn
ssNodeAvailBlocks = _SsNodeAvailBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 4),
    _SsNodeAvailBlocks_Type()
)
ssNodeAvailBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeAvailBlocks.setStatus("current")


class _SsNodeLnn_Type(Integer32):
    """Custom type ssNodeLnn based on Integer32"""
    defaultValue = 0


_SsNodeLnn_Object = MibScalar
ssNodeLnn = _SsNodeLnn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 5),
    _SsNodeLnn_Type()
)
ssNodeLnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeLnn.setStatus("current")


class _SsNodeDiskless_Type(Integer32):
    """Custom type ssNodeDiskless based on Integer32"""
    defaultValue = 0


_SsNodeDiskless_Object = MibScalar
ssNodeDiskless = _SsNodeDiskless_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 6),
    _SsNodeDiskless_Type()
)
ssNodeDiskless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeDiskless.setStatus("current")


class _SsNodeNetBytesIn_Type(Counter64):
    """Custom type ssNodeNetBytesIn based on Counter64"""
    defaultValue = 0


_SsNodeNetBytesIn_Object = MibTableColumn
ssNodeNetBytesIn = _SsNodeNetBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 7),
    _SsNodeNetBytesIn_Type()
)
ssNodeNetBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNetBytesIn.setStatus("current")


class _SsNodeNetBytesOut_Type(Counter64):
    """Custom type ssNodeNetBytesOut based on Counter64"""
    defaultValue = 0


_SsNodeNetBytesOut_Object = MibTableColumn
ssNodeNetBytesOut = _SsNodeNetBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 8),
    _SsNodeNetBytesOut_Type()
)
ssNodeNetBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNetBytesOut.setStatus("current")


class _SsNodeMACaddress_Type(PhysAddress):
    """Custom type ssNodeMACaddress based on PhysAddress"""
    defaultValue = 0


_SsNodeMACaddress_Object = MibTableColumn
ssNodeMACaddress = _SsNodeMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 9),
    _SsNodeMACaddress_Type()
)
ssNodeMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeMACaddress.setStatus("current")


class _SsNodeIPaddress_Type(IpAddress):
    """Custom type ssNodeIPaddress based on IpAddress"""
    defaultValue = 0


_SsNodeIPaddress_Object = MibTableColumn
ssNodeIPaddress = _SsNodeIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 10),
    _SsNodeIPaddress_Type()
)
ssNodeIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeIPaddress.setStatus("current")


class _SsNodeVersion_Type(DisplayString):
    """Custom type ssNodeVersion based on DisplayString"""
    defaultValue = 0


_SsNodeVersion_Object = MibTableColumn
ssNodeVersion = _SsNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 11),
    _SsNodeVersion_Type()
)
ssNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeVersion.setStatus("current")


class _SsNodeBoottime_Type(TimeTicks64):
    """Custom type ssNodeBoottime based on TimeTicks64"""
    defaultValue = 0


_SsNodeBoottime_Object = MibTableColumn
ssNodeBoottime = _SsNodeBoottime_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 12),
    _SsNodeBoottime_Type()
)
ssNodeBoottime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeBoottime.setStatus("current")


class _SsNodeHealth_Type(DisplayString):
    """Custom type ssNodeHealth based on DisplayString"""
    defaultValue = 0


_SsNodeHealth_Object = MibTableColumn
ssNodeHealth = _SsNodeHealth_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 13),
    _SsNodeHealth_Type()
)
ssNodeHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeHealth.setStatus("current")


class _SsNodeCPUload_Type(Integer32):
    """Custom type ssNodeCPUload based on Integer32"""
    defaultValue = 0


_SsNodeCPUload_Object = MibTableColumn
ssNodeCPUload = _SsNodeCPUload_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 14),
    _SsNodeCPUload_Type()
)
ssNodeCPUload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUload.setStatus("current")


class _SsNodeFilesystemBytesIn_Type(Counter64):
    """Custom type ssNodeFilesystemBytesIn based on Counter64"""
    defaultValue = 0


_SsNodeFilesystemBytesIn_Object = MibTableColumn
ssNodeFilesystemBytesIn = _SsNodeFilesystemBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 15),
    _SsNodeFilesystemBytesIn_Type()
)
ssNodeFilesystemBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeFilesystemBytesIn.setStatus("current")


class _SsNodeFilesystemBytesOut_Type(Counter64):
    """Custom type ssNodeFilesystemBytesOut based on Counter64"""
    defaultValue = 0


_SsNodeFilesystemBytesOut_Object = MibTableColumn
ssNodeFilesystemBytesOut = _SsNodeFilesystemBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 16),
    _SsNodeFilesystemBytesOut_Type()
)
ssNodeFilesystemBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeFilesystemBytesOut.setStatus("current")


class _SsNodeNumberOfDisks_Type(Integer32):
    """Custom type ssNodeNumberOfDisks based on Integer32"""
    defaultValue = 0


_SsNodeNumberOfDisks_Object = MibTableColumn
ssNodeNumberOfDisks = _SsNodeNumberOfDisks_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 17),
    _SsNodeNumberOfDisks_Type()
)
ssNodeNumberOfDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNumberOfDisks.setStatus("current")


class _SsNodeNumberOfSensors_Type(Integer32):
    """Custom type ssNodeNumberOfSensors based on Integer32"""
    defaultValue = 0


_SsNodeNumberOfSensors_Object = MibTableColumn
ssNodeNumberOfSensors = _SsNodeNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 18),
    _SsNodeNumberOfSensors_Type()
)
ssNodeNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNumberOfSensors.setStatus("current")


class _SsNodeNetBitsPerSecIn_Type(Counter64):
    """Custom type ssNodeNetBitsPerSecIn based on Counter64"""
    defaultValue = 0


_SsNodeNetBitsPerSecIn_Object = MibTableColumn
ssNodeNetBitsPerSecIn = _SsNodeNetBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 20),
    _SsNodeNetBitsPerSecIn_Type()
)
ssNodeNetBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNetBitsPerSecIn.setStatus("current")


class _SsNodeNetBitsPerSecOut_Type(Counter64):
    """Custom type ssNodeNetBitsPerSecOut based on Counter64"""
    defaultValue = 0


_SsNodeNetBitsPerSecOut_Object = MibTableColumn
ssNodeNetBitsPerSecOut = _SsNodeNetBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 21),
    _SsNodeNetBitsPerSecOut_Type()
)
ssNodeNetBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeNetBitsPerSecOut.setStatus("current")


class _SsNodeFilesystemBitsPerSecIn_Type(Counter64):
    """Custom type ssNodeFilesystemBitsPerSecIn based on Counter64"""
    defaultValue = 0


_SsNodeFilesystemBitsPerSecIn_Object = MibTableColumn
ssNodeFilesystemBitsPerSecIn = _SsNodeFilesystemBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 22),
    _SsNodeFilesystemBitsPerSecIn_Type()
)
ssNodeFilesystemBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeFilesystemBitsPerSecIn.setStatus("current")


class _SsNodeFilesystemBitsPerSecOut_Type(Counter64):
    """Custom type ssNodeFilesystemBitsPerSecOut based on Counter64"""
    defaultValue = 0


_SsNodeFilesystemBitsPerSecOut_Object = MibTableColumn
ssNodeFilesystemBitsPerSecOut = _SsNodeFilesystemBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 23),
    _SsNodeFilesystemBitsPerSecOut_Type()
)
ssNodeFilesystemBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeFilesystemBitsPerSecOut.setStatus("current")


class _SsNodeCPUuser_Type(Integer32):
    """Custom type ssNodeCPUuser based on Integer32"""
    defaultValue = 0


_SsNodeCPUuser_Object = MibTableColumn
ssNodeCPUuser = _SsNodeCPUuser_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 24),
    _SsNodeCPUuser_Type()
)
ssNodeCPUuser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUuser.setStatus("current")


class _SsNodeCPUnice_Type(Integer32):
    """Custom type ssNodeCPUnice based on Integer32"""
    defaultValue = 0


_SsNodeCPUnice_Object = MibTableColumn
ssNodeCPUnice = _SsNodeCPUnice_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 25),
    _SsNodeCPUnice_Type()
)
ssNodeCPUnice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUnice.setStatus("current")


class _SsNodeCPUsystem_Type(Integer32):
    """Custom type ssNodeCPUsystem based on Integer32"""
    defaultValue = 0


_SsNodeCPUsystem_Object = MibTableColumn
ssNodeCPUsystem = _SsNodeCPUsystem_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 26),
    _SsNodeCPUsystem_Type()
)
ssNodeCPUsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUsystem.setStatus("current")


class _SsNodeCPUinterrupt_Type(Integer32):
    """Custom type ssNodeCPUinterrupt based on Integer32"""
    defaultValue = 0


_SsNodeCPUinterrupt_Object = MibTableColumn
ssNodeCPUinterrupt = _SsNodeCPUinterrupt_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 27),
    _SsNodeCPUinterrupt_Type()
)
ssNodeCPUinterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUinterrupt.setStatus("current")


class _SsNodeCPUidle_Type(Integer32):
    """Custom type ssNodeCPUidle based on Integer32"""
    defaultValue = 0


_SsNodeCPUidle_Object = MibTableColumn
ssNodeCPUidle = _SsNodeCPUidle_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 28),
    _SsNodeCPUidle_Type()
)
ssNodeCPUidle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeCPUidle.setStatus("current")


class _SsNodeDevId_Type(Integer32):
    """Custom type ssNodeDevId based on Integer32"""
    defaultValue = 0


_SsNodeDevId_Object = MibScalar
ssNodeDevId = _SsNodeDevId_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 29),
    _SsNodeDevId_Type()
)
ssNodeDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNodeDevId.setStatus("current")
_SsDiskInfoTable_Object = MibTable
ssDiskInfoTable = _SsDiskInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2)
)
if mibBuilder.loadTexts:
    ssDiskInfoTable.setStatus("current")
_SsDiskInfoEntry_Object = MibTableRow
ssDiskInfoEntry = _SsDiskInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1)
)
ssDiskInfoEntry.setIndexNames(
    (0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"),
    (0, "ONEFS-SNAPSHOT-MIB", "ssDiskIndex"),
)
if mibBuilder.loadTexts:
    ssDiskInfoEntry.setStatus("current")


class _SsDiskIndex_Type(Integer32):
    """Custom type ssDiskIndex based on Integer32"""
    defaultValue = 0


_SsDiskIndex_Object = MibTableColumn
ssDiskIndex = _SsDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 1),
    _SsDiskIndex_Type()
)
ssDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskIndex.setStatus("current")


class _SsDiskName_Type(DisplayString):
    """Custom type ssDiskName based on DisplayString"""
    defaultValue = 0


_SsDiskName_Object = MibTableColumn
ssDiskName = _SsDiskName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 2),
    _SsDiskName_Type()
)
ssDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskName.setStatus("current")


class _SsDiskHealth_Type(Integer32):
    """Custom type ssDiskHealth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 0))
    )


_SsDiskHealth_Type.__name__ = "Integer32"
_SsDiskHealth_Object = MibTableColumn
ssDiskHealth = _SsDiskHealth_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 3),
    _SsDiskHealth_Type()
)
ssDiskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskHealth.setStatus("current")


class _SsDiskBytesRead_Type(Counter64):
    """Custom type ssDiskBytesRead based on Counter64"""
    defaultValue = 0


_SsDiskBytesRead_Object = MibTableColumn
ssDiskBytesRead = _SsDiskBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 4),
    _SsDiskBytesRead_Type()
)
ssDiskBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskBytesRead.setStatus("current")


class _SsDiskBytesWritten_Type(Counter64):
    """Custom type ssDiskBytesWritten based on Counter64"""
    defaultValue = 0


_SsDiskBytesWritten_Object = MibTableColumn
ssDiskBytesWritten = _SsDiskBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 5),
    _SsDiskBytesWritten_Type()
)
ssDiskBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskBytesWritten.setStatus("current")


class _SsDiskNumXfers_Type(Counter64):
    """Custom type ssDiskNumXfers based on Counter64"""
    defaultValue = 0


_SsDiskNumXfers_Object = MibTableColumn
ssDiskNumXfers = _SsDiskNumXfers_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 6),
    _SsDiskNumXfers_Type()
)
ssDiskNumXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskNumXfers.setStatus("current")


class _SsDiskBitsPerSecRead_Type(Counter64):
    """Custom type ssDiskBitsPerSecRead based on Counter64"""
    defaultValue = 0


_SsDiskBitsPerSecRead_Object = MibTableColumn
ssDiskBitsPerSecRead = _SsDiskBitsPerSecRead_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 7),
    _SsDiskBitsPerSecRead_Type()
)
ssDiskBitsPerSecRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskBitsPerSecRead.setStatus("current")


class _SsDiskBitsPerSecWritten_Type(Counter64):
    """Custom type ssDiskBitsPerSecWritten based on Counter64"""
    defaultValue = 0


_SsDiskBitsPerSecWritten_Object = MibTableColumn
ssDiskBitsPerSecWritten = _SsDiskBitsPerSecWritten_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 8),
    _SsDiskBitsPerSecWritten_Type()
)
ssDiskBitsPerSecWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskBitsPerSecWritten.setStatus("current")


class _SsDiskXfersPerSec_Type(Counter64):
    """Custom type ssDiskXfersPerSec based on Counter64"""
    defaultValue = 0


_SsDiskXfersPerSec_Object = MibTableColumn
ssDiskXfersPerSec = _SsDiskXfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 9),
    _SsDiskXfersPerSec_Type()
)
ssDiskXfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDiskXfersPerSec.setStatus("current")
_SsSensorInfoTable_Object = MibTable
ssSensorInfoTable = _SsSensorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 3)
)
if mibBuilder.loadTexts:
    ssSensorInfoTable.setStatus("current")
_SsSensorInfoEntry_Object = MibTableRow
ssSensorInfoEntry = _SsSensorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1)
)
ssSensorInfoEntry.setIndexNames(
    (0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"),
    (0, "ONEFS-SNAPSHOT-MIB", "ssDiskIndex"),
)
if mibBuilder.loadTexts:
    ssSensorInfoEntry.setStatus("current")


class _SsSensorDescriptionName_Type(DisplayString):
    """Custom type ssSensorDescriptionName based on DisplayString"""
    defaultValue = 0


_SsSensorDescriptionName_Object = MibTableColumn
ssSensorDescriptionName = _SsSensorDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 1),
    _SsSensorDescriptionName_Type()
)
ssSensorDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSensorDescriptionName.setStatus("current")


class _SsSensorType_Type(Integer32):
    """Custom type ssSensorType based on Integer32"""
    defaultValue = 0


_SsSensorType_Object = MibTableColumn
ssSensorType = _SsSensorType_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 2),
    _SsSensorType_Type()
)
ssSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSensorType.setStatus("current")


class _SsSensorValue_Type(DisplayString):
    """Custom type ssSensorValue based on DisplayString"""
    defaultValue = 0


_SsSensorValue_Object = MibTableColumn
ssSensorValue = _SsSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 3),
    _SsSensorValue_Type()
)
ssSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSensorValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEFS-SNAPSHOT-MIB",
    **{"oneFSss": oneFSss,
       "ssVersion": ssVersion,
       "ssLocalNodeId": ssLocalNodeId,
       "ssTimeStart": ssTimeStart,
       "ssTimeEnd": ssTimeEnd,
       "ssGlobal": ssGlobal,
       "ssDisk": ssDisk,
       "ssFreeBlocks": ssFreeBlocks,
       "ssTotalBlocks": ssTotalBlocks,
       "ssAvailableBlocks": ssAvailableBlocks,
       "ssBlockSize": ssBlockSize,
       "ssNet": ssNet,
       "ssNetBytesIn": ssNetBytesIn,
       "ssNetBytesOut": ssNetBytesOut,
       "ssFilesystemBytesIn": ssFilesystemBytesIn,
       "ssFilesystemBytesOut": ssFilesystemBytesOut,
       "ssNetBitsPerSecIn": ssNetBitsPerSecIn,
       "ssNetBitsPerSecOut": ssNetBitsPerSecOut,
       "ssFilesystemBitsPerSecIn": ssFilesystemBitsPerSecIn,
       "ssFilesystemBitsPerSecOut": ssFilesystemBitsPerSecOut,
       "ssSystem": ssSystem,
       "ssClusterName": ssClusterName,
       "ssClusterHealth": ssClusterHealth,
       "ssConfiguredNodes": ssConfiguredNodes,
       "ssOnlineNodes": ssOnlineNodes,
       "ssNodeInfo": ssNodeInfo,
       "ssNodeTable": ssNodeTable,
       "ssNodeEntry": ssNodeEntry,
       "ssNodeIndex": ssNodeIndex,
       "ssNodeFreeBlocks": ssNodeFreeBlocks,
       "ssNodeTotalBlocks": ssNodeTotalBlocks,
       "ssNodeAvailBlocks": ssNodeAvailBlocks,
       "ssNodeLnn": ssNodeLnn,
       "ssNodeDiskless": ssNodeDiskless,
       "ssNodeNetBytesIn": ssNodeNetBytesIn,
       "ssNodeNetBytesOut": ssNodeNetBytesOut,
       "ssNodeMACaddress": ssNodeMACaddress,
       "ssNodeIPaddress": ssNodeIPaddress,
       "ssNodeVersion": ssNodeVersion,
       "ssNodeBoottime": ssNodeBoottime,
       "ssNodeHealth": ssNodeHealth,
       "ssNodeCPUload": ssNodeCPUload,
       "ssNodeFilesystemBytesIn": ssNodeFilesystemBytesIn,
       "ssNodeFilesystemBytesOut": ssNodeFilesystemBytesOut,
       "ssNodeNumberOfDisks": ssNodeNumberOfDisks,
       "ssNodeNumberOfSensors": ssNodeNumberOfSensors,
       "ssNodeNetBitsPerSecIn": ssNodeNetBitsPerSecIn,
       "ssNodeNetBitsPerSecOut": ssNodeNetBitsPerSecOut,
       "ssNodeFilesystemBitsPerSecIn": ssNodeFilesystemBitsPerSecIn,
       "ssNodeFilesystemBitsPerSecOut": ssNodeFilesystemBitsPerSecOut,
       "ssNodeCPUuser": ssNodeCPUuser,
       "ssNodeCPUnice": ssNodeCPUnice,
       "ssNodeCPUsystem": ssNodeCPUsystem,
       "ssNodeCPUinterrupt": ssNodeCPUinterrupt,
       "ssNodeCPUidle": ssNodeCPUidle,
       "ssNodeDevId": ssNodeDevId,
       "ssDiskInfoTable": ssDiskInfoTable,
       "ssDiskInfoEntry": ssDiskInfoEntry,
       "ssDiskIndex": ssDiskIndex,
       "ssDiskName": ssDiskName,
       "ssDiskHealth": ssDiskHealth,
       "ssDiskBytesRead": ssDiskBytesRead,
       "ssDiskBytesWritten": ssDiskBytesWritten,
       "ssDiskNumXfers": ssDiskNumXfers,
       "ssDiskBitsPerSecRead": ssDiskBitsPerSecRead,
       "ssDiskBitsPerSecWritten": ssDiskBitsPerSecWritten,
       "ssDiskXfersPerSec": ssDiskXfersPerSec,
       "ssSensorInfoTable": ssSensorInfoTable,
       "ssSensorInfoEntry": ssSensorInfoEntry,
       "ssSensorDescriptionName": ssSensorDescriptionName,
       "ssSensorType": ssSensorType,
       "ssSensorValue": ssSensorValue}
)
