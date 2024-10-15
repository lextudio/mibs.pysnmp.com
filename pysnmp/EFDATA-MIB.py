# SNMP MIB module (EFDATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EFDATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:37 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Efdata_ObjectIdentity = ObjectIdentity
efdata = _Efdata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247)
)
_Spectracast_ObjectIdentity = ObjectIdentity
spectracast = _Spectracast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3)
)
_Dtmx5000_ObjectIdentity = ObjectIdentity
dtmx5000 = _Dtmx5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1)
)
_CbGateway_ObjectIdentity = ObjectIdentity
cbGateway = _CbGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1)
)
_CbStatistics_ObjectIdentity = ObjectIdentity
cbStatistics = _CbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1)
)
_CbStatGeneral_ObjectIdentity = ObjectIdentity
cbStatGeneral = _CbStatGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1)
)
_CbStatNumBytesTXed_Type = Counter32
_CbStatNumBytesTXed_Object = MibScalar
cbStatNumBytesTXed = _CbStatNumBytesTXed_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 1),
    _CbStatNumBytesTXed_Type()
)
cbStatNumBytesTXed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatNumBytesTXed.setStatus("mandatory")
_CbStatNumOfPackets_Type = Counter32
_CbStatNumOfPackets_Object = MibScalar
cbStatNumOfPackets = _CbStatNumOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 2),
    _CbStatNumOfPackets_Type()
)
cbStatNumOfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatNumOfPackets.setStatus("mandatory")
_CbStatAvrPktSize_Type = Counter32
_CbStatAvrPktSize_Object = MibScalar
cbStatAvrPktSize = _CbStatAvrPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 3),
    _CbStatAvrPktSize_Type()
)
cbStatAvrPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatAvrPktSize.setStatus("mandatory")
_CbStatAvrBytesPerSec_Type = Counter32
_CbStatAvrBytesPerSec_Object = MibScalar
cbStatAvrBytesPerSec = _CbStatAvrBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 4),
    _CbStatAvrBytesPerSec_Type()
)
cbStatAvrBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatAvrBytesPerSec.setStatus("mandatory")
_CbStatNumPacketDiscarded_Type = Counter32
_CbStatNumPacketDiscarded_Object = MibScalar
cbStatNumPacketDiscarded = _CbStatNumPacketDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 5),
    _CbStatNumPacketDiscarded_Type()
)
cbStatNumPacketDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatNumPacketDiscarded.setStatus("mandatory")
_CbStatNumNMSFrames_Type = Counter32
_CbStatNumNMSFrames_Object = MibScalar
cbStatNumNMSFrames = _CbStatNumNMSFrames_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 6),
    _CbStatNumNMSFrames_Type()
)
cbStatNumNMSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatNumNMSFrames.setStatus("mandatory")
_CbCPULoad_Type = Counter32
_CbCPULoad_Object = MibScalar
cbCPULoad = _CbCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 7),
    _CbCPULoad_Type()
)
cbCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCPULoad.setStatus("mandatory")
_CbMemoryUsage_Type = Counter32
_CbMemoryUsage_Object = MibScalar
cbMemoryUsage = _CbMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 8),
    _CbMemoryUsage_Type()
)
cbMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbMemoryUsage.setStatus("mandatory")


class _CbStatReset_Type(Integer32):
    """Custom type cbStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbStatReset_Type.__name__ = "Integer32"
_CbStatReset_Object = MibScalar
cbStatReset = _CbStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 9),
    _CbStatReset_Type()
)
cbStatReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cbStatReset.setStatus("mandatory")
_CbStatNumClients_Type = Counter32
_CbStatNumClients_Object = MibScalar
cbStatNumClients = _CbStatNumClients_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 1, 10),
    _CbStatNumClients_Type()
)
cbStatNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStatNumClients.setStatus("mandatory")
_CbStatClient_ObjectIdentity = ObjectIdentity
cbStatClient = _CbStatClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2)
)
_CbClientIP_Type = IpAddress
_CbClientIP_Object = MibScalar
cbClientIP = _CbClientIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 1),
    _CbClientIP_Type()
)
cbClientIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbClientIP.setStatus("mandatory")
_CbClientStatistics_ObjectIdentity = ObjectIdentity
cbClientStatistics = _CbClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2)
)
_CbClNumSeconds_Type = Counter32
_CbClNumSeconds_Object = MibScalar
cbClNumSeconds = _CbClNumSeconds_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 1),
    _CbClNumSeconds_Type()
)
cbClNumSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClNumSeconds.setStatus("mandatory")
_CbClNumKBytes_Type = Counter32
_CbClNumKBytes_Object = MibScalar
cbClNumKBytes = _CbClNumKBytes_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 2),
    _CbClNumKBytes_Type()
)
cbClNumKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClNumKBytes.setStatus("mandatory")
_CbClNumPackets_Type = Counter32
_CbClNumPackets_Object = MibScalar
cbClNumPackets = _CbClNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 3),
    _CbClNumPackets_Type()
)
cbClNumPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClNumPackets.setStatus("mandatory")
_CbClAvrBytesPerSecond_Type = Counter32
_CbClAvrBytesPerSecond_Object = MibScalar
cbClAvrBytesPerSecond = _CbClAvrBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 4),
    _CbClAvrBytesPerSecond_Type()
)
cbClAvrBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClAvrBytesPerSecond.setStatus("mandatory")
_CbClNumPacketsDiscarded_Type = Counter32
_CbClNumPacketsDiscarded_Object = MibScalar
cbClNumPacketsDiscarded = _CbClNumPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 5),
    _CbClNumPacketsDiscarded_Type()
)
cbClNumPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClNumPacketsDiscarded.setStatus("mandatory")


class _CbClStatReset_Type(Integer32):
    """Custom type cbClStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbClStatReset_Type.__name__ = "Integer32"
_CbClStatReset_Object = MibScalar
cbClStatReset = _CbClStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 6),
    _CbClStatReset_Type()
)
cbClStatReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cbClStatReset.setStatus("mandatory")


class _CbClEncrEnbled_Type(Integer32):
    """Custom type cbClEncrEnbled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbClEncrEnbled_Type.__name__ = "Integer32"
_CbClEncrEnbled_Object = MibScalar
cbClEncrEnbled = _CbClEncrEnbled_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 2, 2, 7),
    _CbClEncrEnbled_Type()
)
cbClEncrEnbled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClEncrEnbled.setStatus("mandatory")
_CbStatClTable_ObjectIdentity = ObjectIdentity
cbStatClTable = _CbStatClTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3)
)
_CbClTable_Object = MibTable
cbClTable = _CbClTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cbClTable.setStatus("mandatory")
_CbClTableNode_Object = MibTableRow
cbClTableNode = _CbClTableNode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1)
)
cbClTableNode.setIndexNames(
    (0, "EFDATA-MIB", "cbClTableIP"),
)
if mibBuilder.loadTexts:
    cbClTableNode.setStatus("mandatory")
_CbClTableIP_Type = IpAddress
_CbClTableIP_Object = MibTableColumn
cbClTableIP = _CbClTableIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 1),
    _CbClTableIP_Type()
)
cbClTableIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableIP.setStatus("mandatory")
_CbClTableStampTime_Type = Integer32
_CbClTableStampTime_Object = MibTableColumn
cbClTableStampTime = _CbClTableStampTime_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 2),
    _CbClTableStampTime_Type()
)
cbClTableStampTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableStampTime.setStatus("mandatory")
_CbClTableStartTime_Type = Integer32
_CbClTableStartTime_Object = MibTableColumn
cbClTableStartTime = _CbClTableStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 3),
    _CbClTableStartTime_Type()
)
cbClTableStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableStartTime.setStatus("mandatory")
_CbClTableTotalPackets_Type = Integer32
_CbClTableTotalPackets_Object = MibTableColumn
cbClTableTotalPackets = _CbClTableTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 4),
    _CbClTableTotalPackets_Type()
)
cbClTableTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableTotalPackets.setStatus("mandatory")
_CbClTableBytesInSec_Type = Integer32
_CbClTableBytesInSec_Object = MibTableColumn
cbClTableBytesInSec = _CbClTableBytesInSec_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 5),
    _CbClTableBytesInSec_Type()
)
cbClTableBytesInSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableBytesInSec.setStatus("mandatory")
_CbClTablePacketsDiscr_Type = Integer32
_CbClTablePacketsDiscr_Object = MibTableColumn
cbClTablePacketsDiscr = _CbClTablePacketsDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 6),
    _CbClTablePacketsDiscr_Type()
)
cbClTablePacketsDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTablePacketsDiscr.setStatus("mandatory")
_CbClTableKBytesTxed_Type = Integer32
_CbClTableKBytesTxed_Object = MibTableColumn
cbClTableKBytesTxed = _CbClTableKBytesTxed_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 7),
    _CbClTableKBytesTxed_Type()
)
cbClTableKBytesTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbClTableKBytesTxed.setStatus("mandatory")


class _CbClTableReset_Type(Integer32):
    """Custom type cbClTableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbNo", 0),
          ("cbYes", 1))
    )


_CbClTableReset_Type.__name__ = "Integer32"
_CbClTableReset_Object = MibTableColumn
cbClTableReset = _CbClTableReset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 1, 3, 1, 1, 8),
    _CbClTableReset_Type()
)
cbClTableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbClTableReset.setStatus("mandatory")
_CbConfig_ObjectIdentity = ObjectIdentity
cbConfig = _CbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2)
)
_CbNetworkParam_ObjectIdentity = ObjectIdentity
cbNetworkParam = _CbNetworkParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1)
)
_CbNetGatewayMngIP_Type = IpAddress
_CbNetGatewayMngIP_Object = MibScalar
cbNetGatewayMngIP = _CbNetGatewayMngIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 1),
    _CbNetGatewayMngIP_Type()
)
cbNetGatewayMngIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetGatewayMngIP.setStatus("mandatory")
_CbNetGatewayMngSubnetMask_Type = IpAddress
_CbNetGatewayMngSubnetMask_Object = MibScalar
cbNetGatewayMngSubnetMask = _CbNetGatewayMngSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 2),
    _CbNetGatewayMngSubnetMask_Type()
)
cbNetGatewayMngSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbNetGatewayMngSubnetMask.setStatus("mandatory")
_CbNetDefaultGateway_Type = IpAddress
_CbNetDefaultGateway_Object = MibScalar
cbNetDefaultGateway = _CbNetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 3),
    _CbNetDefaultGateway_Type()
)
cbNetDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetDefaultGateway.setStatus("mandatory")


class _CbNetPromiscuous_Type(Integer32):
    """Custom type cbNetPromiscuous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetPromiscuous_Type.__name__ = "Integer32"
_CbNetPromiscuous_Object = MibScalar
cbNetPromiscuous = _CbNetPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 4),
    _CbNetPromiscuous_Type()
)
cbNetPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetPromiscuous.setStatus("mandatory")


class _CbNetUnregisteredUsers_Type(Integer32):
    """Custom type cbNetUnregisteredUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetUnregisteredUsers_Type.__name__ = "Integer32"
_CbNetUnregisteredUsers_Object = MibScalar
cbNetUnregisteredUsers = _CbNetUnregisteredUsers_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 5),
    _CbNetUnregisteredUsers_Type()
)
cbNetUnregisteredUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetUnregisteredUsers.setStatus("mandatory")


class _CbNetMulticast_Type(Integer32):
    """Custom type cbNetMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetMulticast_Type.__name__ = "Integer32"
_CbNetMulticast_Object = MibScalar
cbNetMulticast = _CbNetMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 6),
    _CbNetMulticast_Type()
)
cbNetMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetMulticast.setStatus("mandatory")


class _CbNetDualNIC_Type(Integer32):
    """Custom type cbNetDualNIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetDualNIC_Type.__name__ = "Integer32"
_CbNetDualNIC_Object = MibScalar
cbNetDualNIC = _CbNetDualNIC_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 7),
    _CbNetDualNIC_Type()
)
cbNetDualNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetDualNIC.setStatus("mandatory")
_CbNetGatewayDataIP_Type = IpAddress
_CbNetGatewayDataIP_Object = MibScalar
cbNetGatewayDataIP = _CbNetGatewayDataIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 8),
    _CbNetGatewayDataIP_Type()
)
cbNetGatewayDataIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetGatewayDataIP.setStatus("mandatory")
_CbNetGatewayDataSubnetMask_Type = IpAddress
_CbNetGatewayDataSubnetMask_Object = MibScalar
cbNetGatewayDataSubnetMask = _CbNetGatewayDataSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 9),
    _CbNetGatewayDataSubnetMask_Type()
)
cbNetGatewayDataSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetGatewayDataSubnetMask.setStatus("mandatory")


class _CbNetTelnet_Type(Integer32):
    """Custom type cbNetTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetTelnet_Type.__name__ = "Integer32"
_CbNetTelnet_Object = MibScalar
cbNetTelnet = _CbNetTelnet_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 10),
    _CbNetTelnet_Type()
)
cbNetTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetTelnet.setStatus("mandatory")


class _CbNetFTP_Type(Integer32):
    """Custom type cbNetFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbNetFTP_Type.__name__ = "Integer32"
_CbNetFTP_Object = MibScalar
cbNetFTP = _CbNetFTP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 1, 11),
    _CbNetFTP_Type()
)
cbNetFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbNetFTP.setStatus("mandatory")
_CbDVBOutputParam_ObjectIdentity = ObjectIdentity
cbDVBOutputParam = _CbDVBOutputParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2)
)
_CbDVBOutputBitRate_Type = Integer32
_CbDVBOutputBitRate_Object = MibScalar
cbDVBOutputBitRate = _CbDVBOutputBitRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 1),
    _CbDVBOutputBitRate_Type()
)
cbDVBOutputBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBOutputBitRate.setStatus("mandatory")
_CbDVBPAT_Type = Integer32
_CbDVBPAT_Object = MibScalar
cbDVBPAT = _CbDVBPAT_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 2),
    _CbDVBPAT_Type()
)
cbDVBPAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBPAT.setStatus("mandatory")
_CbDVBPMT_Type = Integer32
_CbDVBPMT_Object = MibScalar
cbDVBPMT = _CbDVBPMT_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 3),
    _CbDVBPMT_Type()
)
cbDVBPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBPMT.setStatus("mandatory")


class _CbDVBFraming_Type(Integer32):
    """Custom type cbDVBFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbFraming188", 1),
          ("cbFraming204", 2))
    )


_CbDVBFraming_Type.__name__ = "Integer32"
_CbDVBFraming_Object = MibScalar
cbDVBFraming = _CbDVBFraming_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 4),
    _CbDVBFraming_Type()
)
cbDVBFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBFraming.setStatus("mandatory")


class _CbStuffingMode_Type(Integer32):
    """Custom type cbStuffingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbAdaptationField", 1),
          ("cbFFStuffing", 0))
    )


_CbStuffingMode_Type.__name__ = "Integer32"
_CbStuffingMode_Object = MibScalar
cbStuffingMode = _CbStuffingMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 5),
    _CbStuffingMode_Type()
)
cbStuffingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStuffingMode.setStatus("mandatory")


class _CbMpeMode_Type(Integer32):
    """Custom type cbMpeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbNotPacked", 1),
          ("cbPacked", 0))
    )


_CbMpeMode_Type.__name__ = "Integer32"
_CbMpeMode_Object = MibScalar
cbMpeMode = _CbMpeMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 6),
    _CbMpeMode_Type()
)
cbMpeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMpeMode.setStatus("mandatory")


class _CbCRCMode_Type(Integer32):
    """Custom type cbCRCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbCRC", 2),
          ("cbCheckSum", 1),
          ("cbZero", 0))
    )


_CbCRCMode_Type.__name__ = "Integer32"
_CbCRCMode_Object = MibScalar
cbCRCMode = _CbCRCMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 7),
    _CbCRCMode_Type()
)
cbCRCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCRCMode.setStatus("mandatory")


class _CbDVBClockPolarity_Type(Integer32):
    """Custom type cbDVBClockPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbInverted", 1),
          ("cbNotInverted", 0))
    )


_CbDVBClockPolarity_Type.__name__ = "Integer32"
_CbDVBClockPolarity_Object = MibScalar
cbDVBClockPolarity = _CbDVBClockPolarity_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 8),
    _CbDVBClockPolarity_Type()
)
cbDVBClockPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbDVBClockPolarity.setStatus("mandatory")


class _CbDVBAuxInput_Type(Integer32):
    """Custom type cbDVBAuxInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbDVBAuxInput_Type.__name__ = "Integer32"
_CbDVBAuxInput_Object = MibScalar
cbDVBAuxInput = _CbDVBAuxInput_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 9),
    _CbDVBAuxInput_Type()
)
cbDVBAuxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBAuxInput.setStatus("mandatory")


class _CbDVBAuxNullPackets_Type(Integer32):
    """Custom type cbDVBAuxNullPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbDVBAuxNullPackets_Type.__name__ = "Integer32"
_CbDVBAuxNullPackets_Object = MibScalar
cbDVBAuxNullPackets = _CbDVBAuxNullPackets_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 10),
    _CbDVBAuxNullPackets_Type()
)
cbDVBAuxNullPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBAuxNullPackets.setStatus("mandatory")


class _CbDVBAuxInputType_Type(Integer32):
    """Custom type cbDVBAuxInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbASI", 1),
          ("cbLVDS", 0))
    )


_CbDVBAuxInputType_Type.__name__ = "Integer32"
_CbDVBAuxInputType_Object = MibScalar
cbDVBAuxInputType = _CbDVBAuxInputType_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 11),
    _CbDVBAuxInputType_Type()
)
cbDVBAuxInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBAuxInputType.setStatus("mandatory")


class _CbDVBLlcSnap_Type(Integer32):
    """Custom type cbDVBLlcSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbDVBLlcSnap_Type.__name__ = "Integer32"
_CbDVBLlcSnap_Object = MibScalar
cbDVBLlcSnap = _CbDVBLlcSnap_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 2, 12),
    _CbDVBLlcSnap_Type()
)
cbDVBLlcSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDVBLlcSnap.setStatus("mandatory")
_CbGeneralParam_ObjectIdentity = ObjectIdentity
cbGeneralParam = _CbGeneralParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3)
)


class _CbGatewayEnabled_Type(Integer32):
    """Custom type cbGatewayEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbGatewayEnabled_Type.__name__ = "Integer32"
_CbGatewayEnabled_Object = MibScalar
cbGatewayEnabled = _CbGatewayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 1),
    _CbGatewayEnabled_Type()
)
cbGatewayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGatewayEnabled.setStatus("mandatory")


class _CbGatewaySWReset_Type(Integer32):
    """Custom type cbGatewaySWReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbGatewaySWReset_Type.__name__ = "Integer32"
_CbGatewaySWReset_Object = MibScalar
cbGatewaySWReset = _CbGatewaySWReset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 2),
    _CbGatewaySWReset_Type()
)
cbGatewaySWReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cbGatewaySWReset.setStatus("mandatory")
_CbTraceInfo_ObjectIdentity = ObjectIdentity
cbTraceInfo = _CbTraceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 3)
)
_CbTraceMask_Type = Integer32
_CbTraceMask_Object = MibScalar
cbTraceMask = _CbTraceMask_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 3, 1),
    _CbTraceMask_Type()
)
cbTraceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTraceMask.setStatus("mandatory")
_CbTraceLevel_Type = Integer32
_CbTraceLevel_Object = MibScalar
cbTraceLevel = _CbTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 3, 2),
    _CbTraceLevel_Type()
)
cbTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTraceLevel.setStatus("mandatory")


class _CbTraceOutputChannel_Type(Integer32):
    """Custom type cbTraceOutputChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbTraceToCOM1", 2),
          ("cbTraceToCOM2", 3),
          ("cbTraceToVGA", 1))
    )


_CbTraceOutputChannel_Type.__name__ = "Integer32"
_CbTraceOutputChannel_Object = MibScalar
cbTraceOutputChannel = _CbTraceOutputChannel_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 3, 3),
    _CbTraceOutputChannel_Type()
)
cbTraceOutputChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTraceOutputChannel.setStatus("mandatory")


class _CbPktEncrypt_Type(Integer32):
    """Custom type cbPktEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbPktEncrypt_Type.__name__ = "Integer32"
_CbPktEncrypt_Object = MibScalar
cbPktEncrypt = _CbPktEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 4),
    _CbPktEncrypt_Type()
)
cbPktEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbPktEncrypt.setStatus("mandatory")
_CbGatewayDescription_Type = DisplayString
_CbGatewayDescription_Object = MibScalar
cbGatewayDescription = _CbGatewayDescription_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 5),
    _CbGatewayDescription_Type()
)
cbGatewayDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGatewayDescription.setStatus("mandatory")
_CbSWVersion_Type = DisplayString
_CbSWVersion_Object = MibScalar
cbSWVersion = _CbSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 6),
    _CbSWVersion_Type()
)
cbSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbSWVersion.setStatus("mandatory")
_CbApplicationFileName_Type = DisplayString
_CbApplicationFileName_Object = MibScalar
cbApplicationFileName = _CbApplicationFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 7),
    _CbApplicationFileName_Type()
)
cbApplicationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbApplicationFileName.setStatus("mandatory")


class _CbDataMappingMode_Type(Integer32):
    """Custom type cbDataMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbDataStreaming", 2),
          ("cbProtocolEncapsulation", 3))
    )


_CbDataMappingMode_Type.__name__ = "Integer32"
_CbDataMappingMode_Object = MibScalar
cbDataMappingMode = _CbDataMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 8),
    _CbDataMappingMode_Type()
)
cbDataMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDataMappingMode.setStatus("mandatory")
_CbMaxAllowableDelay_Type = Integer32
_CbMaxAllowableDelay_Object = MibScalar
cbMaxAllowableDelay = _CbMaxAllowableDelay_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 9),
    _CbMaxAllowableDelay_Type()
)
cbMaxAllowableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMaxAllowableDelay.setStatus("mandatory")
_CbQualityOfService_ObjectIdentity = ObjectIdentity
cbQualityOfService = _CbQualityOfService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 10)
)


class _CbQOSMode_Type(Integer32):
    """Custom type cbQOSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbPermissive", 1),
          ("cbRestrictive", 2))
    )


_CbQOSMode_Type.__name__ = "Integer32"
_CbQOSMode_Object = MibScalar
cbQOSMode = _CbQOSMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 10, 1),
    _CbQOSMode_Type()
)
cbQOSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbQOSMode.setStatus("mandatory")


class _CbQOSActive_Type(Integer32):
    """Custom type cbQOSActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbQOSActive_Type.__name__ = "Integer32"
_CbQOSActive_Object = MibScalar
cbQOSActive = _CbQOSActive_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 10, 2),
    _CbQOSActive_Type()
)
cbQOSActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbQOSActive.setStatus("mandatory")


class _CbFlushing_Type(Integer32):
    """Custom type cbFlushing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbNo", 0),
          ("cbYes", 1))
    )


_CbFlushing_Type.__name__ = "Integer32"
_CbFlushing_Object = MibScalar
cbFlushing = _CbFlushing_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 11),
    _CbFlushing_Type()
)
cbFlushing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbFlushing.setStatus("mandatory")
_CbFPGAFileName_Type = DisplayString
_CbFPGAFileName_Object = MibScalar
cbFPGAFileName = _CbFPGAFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 3, 13),
    _CbFPGAFileName_Type()
)
cbFPGAFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbFPGAFileName.setStatus("mandatory")
_CbGroupsTable_ObjectIdentity = ObjectIdentity
cbGroupsTable = _CbGroupsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4)
)
_CbGrTable_Object = MibTable
cbGrTable = _CbGrTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cbGrTable.setStatus("mandatory")
_CbGroupsTableNode_Object = MibTableRow
cbGroupsTableNode = _CbGroupsTableNode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1)
)
cbGroupsTableNode.setIndexNames(
    (0, "EFDATA-MIB", "cbGrTableIndex"),
)
if mibBuilder.loadTexts:
    cbGroupsTableNode.setStatus("mandatory")
_CbGrTableIndex_Type = Integer32
_CbGrTableIndex_Object = MibTableColumn
cbGrTableIndex = _CbGrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1, 1),
    _CbGrTableIndex_Type()
)
cbGrTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGrTableIndex.setStatus("mandatory")
_CbGrTablePID_Type = Integer32
_CbGrTablePID_Object = MibTableColumn
cbGrTablePID = _CbGrTablePID_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1, 2),
    _CbGrTablePID_Type()
)
cbGrTablePID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGrTablePID.setStatus("mandatory")


class _CbGrTableQosMode_Type(Integer32):
    """Custom type cbGrTableQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbGlobal", 1),
          ("cbIndividual", 0))
    )


_CbGrTableQosMode_Type.__name__ = "Integer32"
_CbGrTableQosMode_Object = MibTableColumn
cbGrTableQosMode = _CbGrTableQosMode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1, 3),
    _CbGrTableQosMode_Type()
)
cbGrTableQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGrTableQosMode.setStatus("mandatory")
_CbGrTableMinRate_Type = Integer32
_CbGrTableMinRate_Object = MibTableColumn
cbGrTableMinRate = _CbGrTableMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1, 4),
    _CbGrTableMinRate_Type()
)
cbGrTableMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGrTableMinRate.setStatus("mandatory")
_CbGrTableMaxRate_Type = Integer32
_CbGrTableMaxRate_Object = MibTableColumn
cbGrTableMaxRate = _CbGrTableMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 4, 1, 1, 5),
    _CbGrTableMaxRate_Type()
)
cbGrTableMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbGrTableMaxRate.setStatus("mandatory")
_CbConfigSTUTable_ObjectIdentity = ObjectIdentity
cbConfigSTUTable = _CbConfigSTUTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5)
)
_CbStaticUserTable_Object = MibTable
cbStaticUserTable = _CbStaticUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cbStaticUserTable.setStatus("mandatory")
_CbStaticUserEntry_Object = MibTableRow
cbStaticUserEntry = _CbStaticUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1)
)
cbStaticUserEntry.setIndexNames(
    (0, "EFDATA-MIB", "cbStaticUserIP"),
)
if mibBuilder.loadTexts:
    cbStaticUserEntry.setStatus("mandatory")
_CbStaticUserIP_Type = IpAddress
_CbStaticUserIP_Object = MibTableColumn
cbStaticUserIP = _CbStaticUserIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 1),
    _CbStaticUserIP_Type()
)
cbStaticUserIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserIP.setStatus("mandatory")
_CbStaticUserMask_Type = IpAddress
_CbStaticUserMask_Object = MibTableColumn
cbStaticUserMask = _CbStaticUserMask_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 2),
    _CbStaticUserMask_Type()
)
cbStaticUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserMask.setStatus("mandatory")
_CbStaticUserGroup_Type = Integer32
_CbStaticUserGroup_Object = MibTableColumn
cbStaticUserGroup = _CbStaticUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 3),
    _CbStaticUserGroup_Type()
)
cbStaticUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserGroup.setStatus("mandatory")
_CbStaticUserMAC_Type = PhysAddress
_CbStaticUserMAC_Object = MibTableColumn
cbStaticUserMAC = _CbStaticUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 4),
    _CbStaticUserMAC_Type()
)
cbStaticUserMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserMAC.setStatus("mandatory")
_CbStaticUserMinRate_Type = Integer32
_CbStaticUserMinRate_Object = MibTableColumn
cbStaticUserMinRate = _CbStaticUserMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 5),
    _CbStaticUserMinRate_Type()
)
cbStaticUserMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserMinRate.setStatus("mandatory")
_CbStaticUserMaxRate_Type = Integer32
_CbStaticUserMaxRate_Object = MibTableColumn
cbStaticUserMaxRate = _CbStaticUserMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 5, 1, 1, 6),
    _CbStaticUserMaxRate_Type()
)
cbStaticUserMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbStaticUserMaxRate.setStatus("mandatory")
_CbConfigMulticastTable_ObjectIdentity = ObjectIdentity
cbConfigMulticastTable = _CbConfigMulticastTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6)
)
_CbMulticastTable_Object = MibTable
cbMulticastTable = _CbMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cbMulticastTable.setStatus("mandatory")
_CbMulticastEntry_Object = MibTableRow
cbMulticastEntry = _CbMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1)
)
cbMulticastEntry.setIndexNames(
    (0, "EFDATA-MIB", "cbMulticastIP"),
)
if mibBuilder.loadTexts:
    cbMulticastEntry.setStatus("mandatory")
_CbMulticastIP_Type = IpAddress
_CbMulticastIP_Object = MibTableColumn
cbMulticastIP = _CbMulticastIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1, 1),
    _CbMulticastIP_Type()
)
cbMulticastIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMulticastIP.setStatus("mandatory")
_CbMulticastGroup_Type = Integer32
_CbMulticastGroup_Object = MibTableColumn
cbMulticastGroup = _CbMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1, 2),
    _CbMulticastGroup_Type()
)
cbMulticastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMulticastGroup.setStatus("mandatory")
_CbMulticastSID_Type = Integer32
_CbMulticastSID_Object = MibTableColumn
cbMulticastSID = _CbMulticastSID_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1, 3),
    _CbMulticastSID_Type()
)
cbMulticastSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMulticastSID.setStatus("mandatory")
_CbMulticastMinRate_Type = Integer32
_CbMulticastMinRate_Object = MibTableColumn
cbMulticastMinRate = _CbMulticastMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1, 4),
    _CbMulticastMinRate_Type()
)
cbMulticastMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMulticastMinRate.setStatus("mandatory")
_CbMulticastMaxRate_Type = Integer32
_CbMulticastMaxRate_Object = MibTableColumn
cbMulticastMaxRate = _CbMulticastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 6, 1, 1, 5),
    _CbMulticastMaxRate_Type()
)
cbMulticastMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbMulticastMaxRate.setStatus("mandatory")
_CbConfigClTable_ObjectIdentity = ObjectIdentity
cbConfigClTable = _CbConfigClTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7)
)
_CbCfgClTable_Object = MibTable
cbCfgClTable = _CbCfgClTable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cbCfgClTable.setStatus("mandatory")
_CbCfgClTableNode_Object = MibTableRow
cbCfgClTableNode = _CbCfgClTableNode_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1)
)
cbCfgClTableNode.setIndexNames(
    (0, "EFDATA-MIB", "cbCfgClTableIP"),
)
if mibBuilder.loadTexts:
    cbCfgClTableNode.setStatus("mandatory")
_CbCfgClTableIP_Type = IpAddress
_CbCfgClTableIP_Object = MibTableColumn
cbCfgClTableIP = _CbCfgClTableIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 1),
    _CbCfgClTableIP_Type()
)
cbCfgClTableIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableIP.setStatus("mandatory")
_CbCfgClTableMask_Type = IpAddress
_CbCfgClTableMask_Object = MibTableColumn
cbCfgClTableMask = _CbCfgClTableMask_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 2),
    _CbCfgClTableMask_Type()
)
cbCfgClTableMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableMask.setStatus("mandatory")
_CbCfgClTableMAC_Type = PhysAddress
_CbCfgClTableMAC_Object = MibTableColumn
cbCfgClTableMAC = _CbCfgClTableMAC_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 3),
    _CbCfgClTableMAC_Type()
)
cbCfgClTableMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableMAC.setStatus("mandatory")
_CbCfgClTableGroup_Type = Integer32
_CbCfgClTableGroup_Object = MibTableColumn
cbCfgClTableGroup = _CbCfgClTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 4),
    _CbCfgClTableGroup_Type()
)
cbCfgClTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableGroup.setStatus("mandatory")
_CbCfgClTableBy_Type = DisplayString
_CbCfgClTableBy_Object = MibTableColumn
cbCfgClTableBy = _CbCfgClTableBy_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 5),
    _CbCfgClTableBy_Type()
)
cbCfgClTableBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableBy.setStatus("mandatory")
_CbCfgClTableMinRate_Type = Integer32
_CbCfgClTableMinRate_Object = MibTableColumn
cbCfgClTableMinRate = _CbCfgClTableMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 6),
    _CbCfgClTableMinRate_Type()
)
cbCfgClTableMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableMinRate.setStatus("mandatory")
_CbCfgClTableMaxRate_Type = Integer32
_CbCfgClTableMaxRate_Object = MibTableColumn
cbCfgClTableMaxRate = _CbCfgClTableMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 7),
    _CbCfgClTableMaxRate_Type()
)
cbCfgClTableMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableMaxRate.setStatus("mandatory")


class _CbCfgClTableEncrypt_Type(Integer32):
    """Custom type cbCfgClTableEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbCfgClTableEncrypt_Type.__name__ = "Integer32"
_CbCfgClTableEncrypt_Object = MibTableColumn
cbCfgClTableEncrypt = _CbCfgClTableEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 7, 1, 1, 8),
    _CbCfgClTableEncrypt_Type()
)
cbCfgClTableEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCfgClTableEncrypt.setStatus("mandatory")
_CbTimeDate_ObjectIdentity = ObjectIdentity
cbTimeDate = _CbTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 8)
)
_CbTime_Type = DisplayString
_CbTime_Object = MibScalar
cbTime = _CbTime_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 8, 1),
    _CbTime_Type()
)
cbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTime.setStatus("mandatory")
_CbDate_Type = DisplayString
_CbDate_Object = MibScalar
cbDate = _CbDate_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 8, 2),
    _CbDate_Type()
)
cbDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDate.setStatus("mandatory")
_CbClientsInfoReset_Type = Integer32
_CbClientsInfoReset_Object = MibScalar
cbClientsInfoReset = _CbClientsInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 9),
    _CbClientsInfoReset_Type()
)
cbClientsInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbClientsInfoReset.setStatus("mandatory")
_CbCCUParam_ObjectIdentity = ObjectIdentity
cbCCUParam = _CbCCUParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10)
)
_CbCCU1_Type = IpAddress
_CbCCU1_Object = MibScalar
cbCCU1 = _CbCCU1_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 1),
    _CbCCU1_Type()
)
cbCCU1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU1.setStatus("mandatory")
_CbCCU2_Type = IpAddress
_CbCCU2_Object = MibScalar
cbCCU2 = _CbCCU2_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 2),
    _CbCCU2_Type()
)
cbCCU2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU2.setStatus("mandatory")
_CbCCU3_Type = IpAddress
_CbCCU3_Object = MibScalar
cbCCU3 = _CbCCU3_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 3),
    _CbCCU3_Type()
)
cbCCU3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU3.setStatus("mandatory")
_CbCCU4_Type = IpAddress
_CbCCU4_Object = MibScalar
cbCCU4 = _CbCCU4_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 4),
    _CbCCU4_Type()
)
cbCCU4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU4.setStatus("mandatory")
_CbCCU5_Type = IpAddress
_CbCCU5_Object = MibScalar
cbCCU5 = _CbCCU5_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 5),
    _CbCCU5_Type()
)
cbCCU5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU5.setStatus("mandatory")
_CbCCU6_Type = IpAddress
_CbCCU6_Object = MibScalar
cbCCU6 = _CbCCU6_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 6),
    _CbCCU6_Type()
)
cbCCU6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU6.setStatus("mandatory")
_CbCCU7_Type = IpAddress
_CbCCU7_Object = MibScalar
cbCCU7 = _CbCCU7_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 7),
    _CbCCU7_Type()
)
cbCCU7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU7.setStatus("mandatory")
_CbCCU8_Type = IpAddress
_CbCCU8_Object = MibScalar
cbCCU8 = _CbCCU8_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 8),
    _CbCCU8_Type()
)
cbCCU8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU8.setStatus("mandatory")
_CbCCU9_Type = IpAddress
_CbCCU9_Object = MibScalar
cbCCU9 = _CbCCU9_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 9),
    _CbCCU9_Type()
)
cbCCU9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU9.setStatus("mandatory")
_CbCCU10_Type = IpAddress
_CbCCU10_Object = MibScalar
cbCCU10 = _CbCCU10_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 10, 10),
    _CbCCU10_Type()
)
cbCCU10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbCCU10.setStatus("mandatory")
_CbHASParam_ObjectIdentity = ObjectIdentity
cbHASParam = _CbHASParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 11)
)


class _CbHasEnable_Type(Integer32):
    """Custom type cbHasEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbDisabled", 0),
          ("cbEnabled", 1))
    )


_CbHasEnable_Type.__name__ = "Integer32"
_CbHasEnable_Object = MibScalar
cbHasEnable = _CbHasEnable_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 11, 1),
    _CbHasEnable_Type()
)
cbHasEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbHasEnable.setStatus("mandatory")
_CbHasCpu_Type = Integer32
_CbHasCpu_Object = MibScalar
cbHasCpu = _CbHasCpu_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 11, 2),
    _CbHasCpu_Type()
)
cbHasCpu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbHasCpu.setStatus("mandatory")
_CbHasMemory_Type = Integer32
_CbHasMemory_Object = MibScalar
cbHasMemory = _CbHasMemory_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 2, 11, 3),
    _CbHasMemory_Type()
)
cbHasMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbHasMemory.setStatus("mandatory")
_CbDiagnostics_ObjectIdentity = ObjectIdentity
cbDiagnostics = _CbDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3)
)
_CbDiagTestTx_ObjectIdentity = ObjectIdentity
cbDiagTestTx = _CbDiagTestTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3, 1)
)
_CbDiagTestTxParam_ObjectIdentity = ObjectIdentity
cbDiagTestTxParam = _CbDiagTestTxParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3, 1, 1)
)
_CbTestTxDestIP_Type = IpAddress
_CbTestTxDestIP_Object = MibScalar
cbTestTxDestIP = _CbTestTxDestIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3, 1, 1, 1),
    _CbTestTxDestIP_Type()
)
cbTestTxDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTestTxDestIP.setStatus("mandatory")


class _CbTestTxType_Type(Integer32):
    """Custom type cbTestTxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbTestTypeHighSpeedCont", 3),
          ("cbTestTypeLowSpeedCont", 2),
          ("cbTestTypeOnePacket", 1))
    )


_CbTestTxType_Type.__name__ = "Integer32"
_CbTestTxType_Object = MibScalar
cbTestTxType = _CbTestTxType_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3, 1, 1, 2),
    _CbTestTxType_Type()
)
cbTestTxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbTestTxType.setStatus("mandatory")


class _CbDiagTestTxActive_Type(Integer32):
    """Custom type cbDiagTestTxActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbDiagTestTxActive_Type.__name__ = "Integer32"
_CbDiagTestTxActive_Object = MibScalar
cbDiagTestTxActive = _CbDiagTestTxActive_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 3, 1, 2),
    _CbDiagTestTxActive_Type()
)
cbDiagTestTxActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbDiagTestTxActive.setStatus("mandatory")
_CbSWDownload_ObjectIdentity = ObjectIdentity
cbSWDownload = _CbSWDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4)
)
_CbSWServerIP_Type = IpAddress
_CbSWServerIP_Object = MibScalar
cbSWServerIP = _CbSWServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 1),
    _CbSWServerIP_Type()
)
cbSWServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbSWServerIP.setStatus("mandatory")
_CbAppDownload_ObjectIdentity = ObjectIdentity
cbAppDownload = _CbAppDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 2)
)
_CbSWSourceFileName_Type = DisplayString
_CbSWSourceFileName_Object = MibScalar
cbSWSourceFileName = _CbSWSourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 2, 1),
    _CbSWSourceFileName_Type()
)
cbSWSourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbSWSourceFileName.setStatus("mandatory")
_CbSWTargetFileName_Type = DisplayString
_CbSWTargetFileName_Object = MibScalar
cbSWTargetFileName = _CbSWTargetFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 2, 2),
    _CbSWTargetFileName_Type()
)
cbSWTargetFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbSWTargetFileName.setStatus("mandatory")


class _CbSWDownloadStart_Type(Integer32):
    """Custom type cbSWDownloadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbSWDownloadStart_Type.__name__ = "Integer32"
_CbSWDownloadStart_Object = MibScalar
cbSWDownloadStart = _CbSWDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 2, 3),
    _CbSWDownloadStart_Type()
)
cbSWDownloadStart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cbSWDownloadStart.setStatus("mandatory")


class _CbSWDownloadStatus_Type(Integer32):
    """Custom type cbSWDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cbDownloadAborted", 7),
          ("cbDownloadInProgress", 1),
          ("cbERRORBadChecksum", 5),
          ("cbERRORCommunicationFailed", 6),
          ("cbERRORFileNotFound", 3),
          ("cbERRORNotASWFile", 4),
          ("cbERRORTFTPServernotFound", 2),
          ("cbIdle", 0))
    )


_CbSWDownloadStatus_Type.__name__ = "Integer32"
_CbSWDownloadStatus_Object = MibScalar
cbSWDownloadStatus = _CbSWDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 2, 4),
    _CbSWDownloadStatus_Type()
)
cbSWDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbSWDownloadStatus.setStatus("mandatory")
_CbFPGADownload_ObjectIdentity = ObjectIdentity
cbFPGADownload = _CbFPGADownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 3)
)
_CbFPGASourceFileName_Type = DisplayString
_CbFPGASourceFileName_Object = MibScalar
cbFPGASourceFileName = _CbFPGASourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 3, 1),
    _CbFPGASourceFileName_Type()
)
cbFPGASourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbFPGASourceFileName.setStatus("mandatory")
_CbFPGATargetFileName_Type = DisplayString
_CbFPGATargetFileName_Object = MibScalar
cbFPGATargetFileName = _CbFPGATargetFileName_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 3, 2),
    _CbFPGATargetFileName_Type()
)
cbFPGATargetFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbFPGATargetFileName.setStatus("mandatory")


class _CbFPGADownloadStart_Type(Integer32):
    """Custom type cbFPGADownloadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cbFalse", 0),
          ("cbTrue", 1))
    )


_CbFPGADownloadStart_Type.__name__ = "Integer32"
_CbFPGADownloadStart_Object = MibScalar
cbFPGADownloadStart = _CbFPGADownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 3, 3),
    _CbFPGADownloadStart_Type()
)
cbFPGADownloadStart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cbFPGADownloadStart.setStatus("mandatory")


class _CbFPGADownloadStatus_Type(Integer32):
    """Custom type cbFPGADownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cbDownloadAborted", 7),
          ("cbDownloadInProgress", 1),
          ("cbERRORBadChecksum", 5),
          ("cbERRORCommunicationFailed", 6),
          ("cbERRORFileNotFound", 3),
          ("cbERRORNotASWFile", 4),
          ("cbERRORTFTPServernotFound", 2),
          ("cbIdle", 0))
    )


_CbFPGADownloadStatus_Type.__name__ = "Integer32"
_CbFPGADownloadStatus_Object = MibScalar
cbFPGADownloadStatus = _CbFPGADownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6247, 3, 1, 1, 4, 3, 4),
    _CbFPGADownloadStatus_Type()
)
cbFPGADownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbFPGADownloadStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFDATA-MIB",
    **{"efdata": efdata,
       "spectracast": spectracast,
       "dtmx5000": dtmx5000,
       "cbGateway": cbGateway,
       "cbStatistics": cbStatistics,
       "cbStatGeneral": cbStatGeneral,
       "cbStatNumBytesTXed": cbStatNumBytesTXed,
       "cbStatNumOfPackets": cbStatNumOfPackets,
       "cbStatAvrPktSize": cbStatAvrPktSize,
       "cbStatAvrBytesPerSec": cbStatAvrBytesPerSec,
       "cbStatNumPacketDiscarded": cbStatNumPacketDiscarded,
       "cbStatNumNMSFrames": cbStatNumNMSFrames,
       "cbCPULoad": cbCPULoad,
       "cbMemoryUsage": cbMemoryUsage,
       "cbStatReset": cbStatReset,
       "cbStatNumClients": cbStatNumClients,
       "cbStatClient": cbStatClient,
       "cbClientIP": cbClientIP,
       "cbClientStatistics": cbClientStatistics,
       "cbClNumSeconds": cbClNumSeconds,
       "cbClNumKBytes": cbClNumKBytes,
       "cbClNumPackets": cbClNumPackets,
       "cbClAvrBytesPerSecond": cbClAvrBytesPerSecond,
       "cbClNumPacketsDiscarded": cbClNumPacketsDiscarded,
       "cbClStatReset": cbClStatReset,
       "cbClEncrEnbled": cbClEncrEnbled,
       "cbStatClTable": cbStatClTable,
       "cbClTable": cbClTable,
       "cbClTableNode": cbClTableNode,
       "cbClTableIP": cbClTableIP,
       "cbClTableStampTime": cbClTableStampTime,
       "cbClTableStartTime": cbClTableStartTime,
       "cbClTableTotalPackets": cbClTableTotalPackets,
       "cbClTableBytesInSec": cbClTableBytesInSec,
       "cbClTablePacketsDiscr": cbClTablePacketsDiscr,
       "cbClTableKBytesTxed": cbClTableKBytesTxed,
       "cbClTableReset": cbClTableReset,
       "cbConfig": cbConfig,
       "cbNetworkParam": cbNetworkParam,
       "cbNetGatewayMngIP": cbNetGatewayMngIP,
       "cbNetGatewayMngSubnetMask": cbNetGatewayMngSubnetMask,
       "cbNetDefaultGateway": cbNetDefaultGateway,
       "cbNetPromiscuous": cbNetPromiscuous,
       "cbNetUnregisteredUsers": cbNetUnregisteredUsers,
       "cbNetMulticast": cbNetMulticast,
       "cbNetDualNIC": cbNetDualNIC,
       "cbNetGatewayDataIP": cbNetGatewayDataIP,
       "cbNetGatewayDataSubnetMask": cbNetGatewayDataSubnetMask,
       "cbNetTelnet": cbNetTelnet,
       "cbNetFTP": cbNetFTP,
       "cbDVBOutputParam": cbDVBOutputParam,
       "cbDVBOutputBitRate": cbDVBOutputBitRate,
       "cbDVBPAT": cbDVBPAT,
       "cbDVBPMT": cbDVBPMT,
       "cbDVBFraming": cbDVBFraming,
       "cbStuffingMode": cbStuffingMode,
       "cbMpeMode": cbMpeMode,
       "cbCRCMode": cbCRCMode,
       "cbDVBClockPolarity": cbDVBClockPolarity,
       "cbDVBAuxInput": cbDVBAuxInput,
       "cbDVBAuxNullPackets": cbDVBAuxNullPackets,
       "cbDVBAuxInputType": cbDVBAuxInputType,
       "cbDVBLlcSnap": cbDVBLlcSnap,
       "cbGeneralParam": cbGeneralParam,
       "cbGatewayEnabled": cbGatewayEnabled,
       "cbGatewaySWReset": cbGatewaySWReset,
       "cbTraceInfo": cbTraceInfo,
       "cbTraceMask": cbTraceMask,
       "cbTraceLevel": cbTraceLevel,
       "cbTraceOutputChannel": cbTraceOutputChannel,
       "cbPktEncrypt": cbPktEncrypt,
       "cbGatewayDescription": cbGatewayDescription,
       "cbSWVersion": cbSWVersion,
       "cbApplicationFileName": cbApplicationFileName,
       "cbDataMappingMode": cbDataMappingMode,
       "cbMaxAllowableDelay": cbMaxAllowableDelay,
       "cbQualityOfService": cbQualityOfService,
       "cbQOSMode": cbQOSMode,
       "cbQOSActive": cbQOSActive,
       "cbFlushing": cbFlushing,
       "cbFPGAFileName": cbFPGAFileName,
       "cbGroupsTable": cbGroupsTable,
       "cbGrTable": cbGrTable,
       "cbGroupsTableNode": cbGroupsTableNode,
       "cbGrTableIndex": cbGrTableIndex,
       "cbGrTablePID": cbGrTablePID,
       "cbGrTableQosMode": cbGrTableQosMode,
       "cbGrTableMinRate": cbGrTableMinRate,
       "cbGrTableMaxRate": cbGrTableMaxRate,
       "cbConfigSTUTable": cbConfigSTUTable,
       "cbStaticUserTable": cbStaticUserTable,
       "cbStaticUserEntry": cbStaticUserEntry,
       "cbStaticUserIP": cbStaticUserIP,
       "cbStaticUserMask": cbStaticUserMask,
       "cbStaticUserGroup": cbStaticUserGroup,
       "cbStaticUserMAC": cbStaticUserMAC,
       "cbStaticUserMinRate": cbStaticUserMinRate,
       "cbStaticUserMaxRate": cbStaticUserMaxRate,
       "cbConfigMulticastTable": cbConfigMulticastTable,
       "cbMulticastTable": cbMulticastTable,
       "cbMulticastEntry": cbMulticastEntry,
       "cbMulticastIP": cbMulticastIP,
       "cbMulticastGroup": cbMulticastGroup,
       "cbMulticastSID": cbMulticastSID,
       "cbMulticastMinRate": cbMulticastMinRate,
       "cbMulticastMaxRate": cbMulticastMaxRate,
       "cbConfigClTable": cbConfigClTable,
       "cbCfgClTable": cbCfgClTable,
       "cbCfgClTableNode": cbCfgClTableNode,
       "cbCfgClTableIP": cbCfgClTableIP,
       "cbCfgClTableMask": cbCfgClTableMask,
       "cbCfgClTableMAC": cbCfgClTableMAC,
       "cbCfgClTableGroup": cbCfgClTableGroup,
       "cbCfgClTableBy": cbCfgClTableBy,
       "cbCfgClTableMinRate": cbCfgClTableMinRate,
       "cbCfgClTableMaxRate": cbCfgClTableMaxRate,
       "cbCfgClTableEncrypt": cbCfgClTableEncrypt,
       "cbTimeDate": cbTimeDate,
       "cbTime": cbTime,
       "cbDate": cbDate,
       "cbClientsInfoReset": cbClientsInfoReset,
       "cbCCUParam": cbCCUParam,
       "cbCCU1": cbCCU1,
       "cbCCU2": cbCCU2,
       "cbCCU3": cbCCU3,
       "cbCCU4": cbCCU4,
       "cbCCU5": cbCCU5,
       "cbCCU6": cbCCU6,
       "cbCCU7": cbCCU7,
       "cbCCU8": cbCCU8,
       "cbCCU9": cbCCU9,
       "cbCCU10": cbCCU10,
       "cbHASParam": cbHASParam,
       "cbHasEnable": cbHasEnable,
       "cbHasCpu": cbHasCpu,
       "cbHasMemory": cbHasMemory,
       "cbDiagnostics": cbDiagnostics,
       "cbDiagTestTx": cbDiagTestTx,
       "cbDiagTestTxParam": cbDiagTestTxParam,
       "cbTestTxDestIP": cbTestTxDestIP,
       "cbTestTxType": cbTestTxType,
       "cbDiagTestTxActive": cbDiagTestTxActive,
       "cbSWDownload": cbSWDownload,
       "cbSWServerIP": cbSWServerIP,
       "cbAppDownload": cbAppDownload,
       "cbSWSourceFileName": cbSWSourceFileName,
       "cbSWTargetFileName": cbSWTargetFileName,
       "cbSWDownloadStart": cbSWDownloadStart,
       "cbSWDownloadStatus": cbSWDownloadStatus,
       "cbFPGADownload": cbFPGADownload,
       "cbFPGASourceFileName": cbFPGASourceFileName,
       "cbFPGATargetFileName": cbFPGATargetFileName,
       "cbFPGADownloadStart": cbFPGADownloadStart,
       "cbFPGADownloadStatus": cbFPGADownloadStatus}
)
