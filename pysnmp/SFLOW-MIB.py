# SNMP MIB module (SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:50 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

sFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SFlowDataSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class SFlowReceiver(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



# MIB Managed Objects in the order of their OIDs

_SFlowAgent_ObjectIdentity = ObjectIdentity
sFlowAgent = _SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1)
)


class _SFlowVersion_Type(SnmpAdminString):
    """Custom type sFlowVersion based on SnmpAdminString"""
    defaultValue = OctetString("1.00")


_SFlowVersion_Object = MibScalar
sFlowVersion = _SFlowVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 1),
    _SFlowVersion_Type()
)
sFlowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowVersion.setStatus("current")
_SFlowAgentAddress_Type = IpAddress
_SFlowAgentAddress_Object = MibScalar
sFlowAgentAddress = _SFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 2),
    _SFlowAgentAddress_Type()
)
sFlowAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowAgentAddress.setStatus("current")


class _SFlowAgentState_Type(Integer32):
    """Custom type sFlowAgentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SFlowAgentState_Type.__name__ = "Integer32"
_SFlowAgentState_Object = MibScalar
sFlowAgentState = _SFlowAgentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 3),
    _SFlowAgentState_Type()
)
sFlowAgentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowAgentState.setStatus("current")
_SFlowRcvrTable_Object = MibTable
sFlowRcvrTable = _SFlowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4)
)
if mibBuilder.loadTexts:
    sFlowRcvrTable.setStatus("current")
_SFlowRcvrEntry_Object = MibTableRow
sFlowRcvrEntry = _SFlowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1)
)
sFlowRcvrEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowRcvrIndex"),
    (0, "SFLOW-MIB", "sFlowRcvrOwner"),
)
if mibBuilder.loadTexts:
    sFlowRcvrEntry.setStatus("current")


class _SFlowRcvrIndex_Type(Integer32):
    """Custom type sFlowRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SFlowRcvrIndex_Type.__name__ = "Integer32"
_SFlowRcvrIndex_Object = MibTableColumn
sFlowRcvrIndex = _SFlowRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 1),
    _SFlowRcvrIndex_Type()
)
sFlowRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowRcvrIndex.setStatus("current")


class _SFlowRcvrOwner_Type(DisplayString):
    """Custom type sFlowRcvrOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SFlowRcvrOwner_Type.__name__ = "DisplayString"
_SFlowRcvrOwner_Object = MibTableColumn
sFlowRcvrOwner = _SFlowRcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 2),
    _SFlowRcvrOwner_Type()
)
sFlowRcvrOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowRcvrOwner.setStatus("current")


class _SFlowRcvrTimeout_Type(Integer32):
    """Custom type sFlowRcvrTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_SFlowRcvrTimeout_Type.__name__ = "Integer32"
_SFlowRcvrTimeout_Object = MibTableColumn
sFlowRcvrTimeout = _SFlowRcvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 3),
    _SFlowRcvrTimeout_Type()
)
sFlowRcvrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrTimeout.setStatus("current")


class _SFlowRcvrMaximumDatagramSize_Type(Integer32):
    """Custom type sFlowRcvrMaximumDatagramSize based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1400),
    )


_SFlowRcvrMaximumDatagramSize_Type.__name__ = "Integer32"
_SFlowRcvrMaximumDatagramSize_Object = MibTableColumn
sFlowRcvrMaximumDatagramSize = _SFlowRcvrMaximumDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 4),
    _SFlowRcvrMaximumDatagramSize_Type()
)
sFlowRcvrMaximumDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrMaximumDatagramSize.setStatus("current")


class _SFlowRcvrAddress_Type(IpAddress):
    """Custom type sFlowRcvrAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SFlowRcvrAddress_Object = MibTableColumn
sFlowRcvrAddress = _SFlowRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 5),
    _SFlowRcvrAddress_Type()
)
sFlowRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrAddress.setStatus("current")


class _SFlowRcvrPort_Type(Integer32):
    """Custom type sFlowRcvrPort based on Integer32"""
    defaultValue = 6343

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SFlowRcvrPort_Type.__name__ = "Integer32"
_SFlowRcvrPort_Object = MibTableColumn
sFlowRcvrPort = _SFlowRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 6),
    _SFlowRcvrPort_Type()
)
sFlowRcvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowRcvrPort.setStatus("current")
_SFlowRcvrRowStatus_Type = RowStatus
_SFlowRcvrRowStatus_Object = MibTableColumn
sFlowRcvrRowStatus = _SFlowRcvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 4, 1, 7),
    _SFlowRcvrRowStatus_Type()
)
sFlowRcvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sFlowRcvrRowStatus.setStatus("current")
_SFlowFsTable_Object = MibTable
sFlowFsTable = _SFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5)
)
if mibBuilder.loadTexts:
    sFlowFsTable.setStatus("current")
_SFlowFsEntry_Object = MibTableRow
sFlowFsEntry = _SFlowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1)
)
sFlowFsEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowFsDataSource"),
    (0, "SFLOW-MIB", "sFlowFsReceiver"),
)
if mibBuilder.loadTexts:
    sFlowFsEntry.setStatus("current")
_SFlowFsDataSource_Type = SFlowDataSource
_SFlowFsDataSource_Object = MibTableColumn
sFlowFsDataSource = _SFlowFsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1, 1),
    _SFlowFsDataSource_Type()
)
sFlowFsDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowFsDataSource.setStatus("current")
_SFlowFsReceiver_Type = SFlowReceiver
_SFlowFsReceiver_Object = MibTableColumn
sFlowFsReceiver = _SFlowFsReceiver_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1, 3),
    _SFlowFsReceiver_Type()
)
sFlowFsReceiver.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowFsReceiver.setStatus("current")


class _SFlowFsPacketSamplingRate_Type(Integer32):
    """Custom type sFlowFsPacketSamplingRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SFlowFsPacketSamplingRate_Type.__name__ = "Integer32"
_SFlowFsPacketSamplingRate_Object = MibTableColumn
sFlowFsPacketSamplingRate = _SFlowFsPacketSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1, 4),
    _SFlowFsPacketSamplingRate_Type()
)
sFlowFsPacketSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowFsPacketSamplingRate.setStatus("current")


class _SFlowFsMaximumHeaderSize_Type(Integer32):
    """Custom type sFlowFsMaximumHeaderSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 256),
    )


_SFlowFsMaximumHeaderSize_Type.__name__ = "Integer32"
_SFlowFsMaximumHeaderSize_Object = MibTableColumn
sFlowFsMaximumHeaderSize = _SFlowFsMaximumHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1, 5),
    _SFlowFsMaximumHeaderSize_Type()
)
sFlowFsMaximumHeaderSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowFsMaximumHeaderSize.setStatus("current")
_SFlowFsRowStatus_Type = RowStatus
_SFlowFsRowStatus_Object = MibTableColumn
sFlowFsRowStatus = _SFlowFsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 5, 1, 6),
    _SFlowFsRowStatus_Type()
)
sFlowFsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sFlowFsRowStatus.setStatus("current")
_SFlowCpTable_Object = MibTable
sFlowCpTable = _SFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6)
)
if mibBuilder.loadTexts:
    sFlowCpTable.setStatus("current")
_SFlowCpEntry_Object = MibTableRow
sFlowCpEntry = _SFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6, 1)
)
sFlowCpEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowCpDataSource"),
    (0, "SFLOW-MIB", "sFlowCpReceiver"),
)
if mibBuilder.loadTexts:
    sFlowCpEntry.setStatus("current")
_SFlowCpDataSource_Type = SFlowDataSource
_SFlowCpDataSource_Object = MibTableColumn
sFlowCpDataSource = _SFlowCpDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6, 1, 1),
    _SFlowCpDataSource_Type()
)
sFlowCpDataSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowCpDataSource.setStatus("current")
_SFlowCpReceiver_Type = SFlowReceiver
_SFlowCpReceiver_Object = MibTableColumn
sFlowCpReceiver = _SFlowCpReceiver_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6, 1, 3),
    _SFlowCpReceiver_Type()
)
sFlowCpReceiver.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowCpReceiver.setStatus("current")


class _SFlowCpInterval_Type(Integer32):
    """Custom type sFlowCpInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SFlowCpInterval_Type.__name__ = "Integer32"
_SFlowCpInterval_Object = MibTableColumn
sFlowCpInterval = _SFlowCpInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6, 1, 4),
    _SFlowCpInterval_Type()
)
sFlowCpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCpInterval.setStatus("current")
_SFlowCpRowStatus_Type = RowStatus
_SFlowCpRowStatus_Object = MibTableColumn
sFlowCpRowStatus = _SFlowCpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 36, 1, 6, 1, 5),
    _SFlowCpRowStatus_Type()
)
sFlowCpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sFlowCpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFLOW-MIB",
    **{"SFlowDataSource": SFlowDataSource,
       "SFlowReceiver": SFlowReceiver,
       "sFlowMIB": sFlowMIB,
       "sFlowAgent": sFlowAgent,
       "sFlowVersion": sFlowVersion,
       "sFlowAgentAddress": sFlowAgentAddress,
       "sFlowAgentState": sFlowAgentState,
       "sFlowRcvrTable": sFlowRcvrTable,
       "sFlowRcvrEntry": sFlowRcvrEntry,
       "sFlowRcvrIndex": sFlowRcvrIndex,
       "sFlowRcvrOwner": sFlowRcvrOwner,
       "sFlowRcvrTimeout": sFlowRcvrTimeout,
       "sFlowRcvrMaximumDatagramSize": sFlowRcvrMaximumDatagramSize,
       "sFlowRcvrAddress": sFlowRcvrAddress,
       "sFlowRcvrPort": sFlowRcvrPort,
       "sFlowRcvrRowStatus": sFlowRcvrRowStatus,
       "sFlowFsTable": sFlowFsTable,
       "sFlowFsEntry": sFlowFsEntry,
       "sFlowFsDataSource": sFlowFsDataSource,
       "sFlowFsReceiver": sFlowFsReceiver,
       "sFlowFsPacketSamplingRate": sFlowFsPacketSamplingRate,
       "sFlowFsMaximumHeaderSize": sFlowFsMaximumHeaderSize,
       "sFlowFsRowStatus": sFlowFsRowStatus,
       "sFlowCpTable": sFlowCpTable,
       "sFlowCpEntry": sFlowCpEntry,
       "sFlowCpDataSource": sFlowCpDataSource,
       "sFlowCpReceiver": sFlowCpReceiver,
       "sFlowCpInterval": sFlowCpInterval,
       "sFlowCpRowStatus": sFlowCpRowStatus}
)
