# SNMP MIB module (STRATACOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STRATACOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:24 2024
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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Active(Integer32):
    """Custom type Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )





class Severity(DisplayString):
    """Custom type Severity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_Svplus_ObjectIdentity = ObjectIdentity
svplus = _Svplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1)
)
_ControlGroup_ObjectIdentity = ObjectIdentity
controlGroup = _ControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 11)
)


class _DatabaseSampleFreq_Type(Integer32):
    """Custom type databaseSampleFreq based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DatabaseSampleFreq_Type.__name__ = "Integer32"
_DatabaseSampleFreq_Object = MibScalar
databaseSampleFreq = _DatabaseSampleFreq_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 11, 1),
    _DatabaseSampleFreq_Type()
)
databaseSampleFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseSampleFreq.setStatus("mandatory")
_LogGroup_ObjectIdentity = ObjectIdentity
logGroup = _LogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 12)
)
_CurrentMaxLogIndex_Type = Integer32
_CurrentMaxLogIndex_Object = MibScalar
currentMaxLogIndex = _CurrentMaxLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 1),
    _CurrentMaxLogIndex_Type()
)
currentMaxLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMaxLogIndex.setStatus("mandatory")
_MaintLogTable_Object = MibTable
maintLogTable = _MaintLogTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2)
)
if mibBuilder.loadTexts:
    maintLogTable.setStatus("mandatory")
_MaintLogEntry_Object = MibTableRow
maintLogEntry = _MaintLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1)
)
maintLogEntry.setIndexNames(
    (0, "STRATACOM-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    maintLogEntry.setStatus("mandatory")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1073741824),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")


class _LogNetwork_Type(DisplayString):
    """Custom type logNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LogNetwork_Type.__name__ = "DisplayString"
_LogNetwork_Object = MibTableColumn
logNetwork = _LogNetwork_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 2),
    _LogNetwork_Type()
)
logNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNetwork.setStatus("mandatory")


class _LogNodeName_Type(DisplayString):
    """Custom type logNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LogNodeName_Type.__name__ = "DisplayString"
_LogNodeName_Object = MibTableColumn
logNodeName = _LogNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 3),
    _LogNodeName_Type()
)
logNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNodeName.setStatus("mandatory")


class _LogGmtDate_Type(DisplayString):
    """Custom type logGmtDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_LogGmtDate_Type.__name__ = "DisplayString"
_LogGmtDate_Object = MibTableColumn
logGmtDate = _LogGmtDate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 4),
    _LogGmtDate_Type()
)
logGmtDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logGmtDate.setStatus("mandatory")
_LogSeverity_Type = Severity
_LogSeverity_Object = MibTableColumn
logSeverity = _LogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 5),
    _LogSeverity_Type()
)
logSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSeverity.setStatus("mandatory")


class _LogMsg_Type(DisplayString):
    """Custom type logMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LogMsg_Type.__name__ = "DisplayString"
_LogMsg_Object = MibTableColumn
logMsg = _LogMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 6),
    _LogMsg_Type()
)
logMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMsg.setStatus("mandatory")
_EventFilterTable_Object = MibTable
eventFilterTable = _EventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3)
)
if mibBuilder.loadTexts:
    eventFilterTable.setStatus("mandatory")
_EventFilterEntry_Object = MibTableRow
eventFilterEntry = _EventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1)
)
eventFilterEntry.setIndexNames(
    (0, "STRATACOM-MIB", "eventFilterIndex"),
)
if mibBuilder.loadTexts:
    eventFilterEntry.setStatus("mandatory")


class _EventFilterIndex_Type(Integer32):
    """Custom type eventFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventFilterIndex_Type.__name__ = "Integer32"
_EventFilterIndex_Object = MibTableColumn
eventFilterIndex = _EventFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 1),
    _EventFilterIndex_Type()
)
eventFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterIndex.setStatus("mandatory")


class _EventFilterStatus_Type(Integer32):
    """Custom type eventFilterStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 1))
    )


_EventFilterStatus_Type.__name__ = "Integer32"
_EventFilterStatus_Object = MibTableColumn
eventFilterStatus = _EventFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 2),
    _EventFilterStatus_Type()
)
eventFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterStatus.setStatus("mandatory")


class _EventFilterSeverity_Type(Severity):
    """Custom type eventFilterSeverity based on Severity"""
    defaultHexValue = ""


_EventFilterSeverity_Object = MibTableColumn
eventFilterSeverity = _EventFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 3),
    _EventFilterSeverity_Type()
)
eventFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterSeverity.setStatus("mandatory")


class _EventFilterSubstring_Type(DisplayString):
    """Custom type eventFilterSubstring based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventFilterSubstring_Type.__name__ = "DisplayString"
_EventFilterSubstring_Object = MibTableColumn
eventFilterSubstring = _EventFilterSubstring_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 4),
    _EventFilterSubstring_Type()
)
eventFilterSubstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterSubstring.setStatus("mandatory")
_MaintLogFilterGroup_ObjectIdentity = ObjectIdentity
maintLogFilterGroup = _MaintLogFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4)
)


class _MaintLogFilterTimeMin_Type(DisplayString):
    """Custom type maintLogFilterTimeMin based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MaintLogFilterTimeMin_Type.__name__ = "DisplayString"
_MaintLogFilterTimeMin_Object = MibScalar
maintLogFilterTimeMin = _MaintLogFilterTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 1),
    _MaintLogFilterTimeMin_Type()
)
maintLogFilterTimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterTimeMin.setStatus("mandatory")


class _MaintLogFilterTimeMax_Type(DisplayString):
    """Custom type maintLogFilterTimeMax based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MaintLogFilterTimeMax_Type.__name__ = "DisplayString"
_MaintLogFilterTimeMax_Object = MibScalar
maintLogFilterTimeMax = _MaintLogFilterTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 2),
    _MaintLogFilterTimeMax_Type()
)
maintLogFilterTimeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterTimeMax.setStatus("mandatory")


class _MaintLogFilterWindow_Type(Integer32):
    """Custom type maintLogFilterWindow based on Integer32"""
    defaultValue = 30


_MaintLogFilterWindow_Object = MibScalar
maintLogFilterWindow = _MaintLogFilterWindow_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 3),
    _MaintLogFilterWindow_Type()
)
maintLogFilterWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterWindow.setStatus("mandatory")


class _MaintLogFilterNetworkName_Type(DisplayString):
    """Custom type maintLogFilterNetworkName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MaintLogFilterNetworkName_Type.__name__ = "DisplayString"
_MaintLogFilterNetworkName_Object = MibScalar
maintLogFilterNetworkName = _MaintLogFilterNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 4),
    _MaintLogFilterNetworkName_Type()
)
maintLogFilterNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterNetworkName.setStatus("mandatory")


class _MaintLogFilterNodeName_Type(DisplayString):
    """Custom type maintLogFilterNodeName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MaintLogFilterNodeName_Type.__name__ = "DisplayString"
_MaintLogFilterNodeName_Object = MibScalar
maintLogFilterNodeName = _MaintLogFilterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 5),
    _MaintLogFilterNodeName_Type()
)
maintLogFilterNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterNodeName.setStatus("mandatory")


class _MaintLogFilterSeverity_Type(Severity):
    """Custom type maintLogFilterSeverity based on Severity"""
    defaultHexValue = ""


_MaintLogFilterSeverity_Object = MibScalar
maintLogFilterSeverity = _MaintLogFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 6),
    _MaintLogFilterSeverity_Type()
)
maintLogFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterSeverity.setStatus("mandatory")
_NetworkGroup_ObjectIdentity = ObjectIdentity
networkGroup = _NetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 13)
)
_NetworkTable_Object = MibTable
networkTable = _NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1)
)
if mibBuilder.loadTexts:
    networkTable.setStatus("mandatory")
_NetworkEntry_Object = MibTableRow
networkEntry = _NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1)
)
networkEntry.setIndexNames(
    (0, "STRATACOM-MIB", "networkName"),
)
if mibBuilder.loadTexts:
    networkEntry.setStatus("mandatory")


class _NetworkName_Type(DisplayString):
    """Custom type networkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NetworkName_Type.__name__ = "DisplayString"
_NetworkName_Object = MibTableColumn
networkName = _NetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 1),
    _NetworkName_Type()
)
networkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkName.setStatus("mandatory")
_NetworkId_Type = Integer32
_NetworkId_Object = MibTableColumn
networkId = _NetworkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 2),
    _NetworkId_Type()
)
networkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkId.setStatus("mandatory")
_NetworkIpxId_Type = Integer32
_NetworkIpxId_Object = MibTableColumn
networkIpxId = _NetworkIpxId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 3),
    _NetworkIpxId_Type()
)
networkIpxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIpxId.setStatus("mandatory")
_NodeGroup_ObjectIdentity = ObjectIdentity
nodeGroup = _NodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 14)
)
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("mandatory")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1)
)
nodeEntry.setIndexNames(
    (0, "STRATACOM-MIB", "nodeNetworkName"),
    (0, "STRATACOM-MIB", "nodeName"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("mandatory")


class _NodeNetworkName_Type(DisplayString):
    """Custom type nodeNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeNetworkName_Type.__name__ = "DisplayString"
_NodeNetworkName_Object = MibTableColumn
nodeNetworkName = _NodeNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1, 1),
    _NodeNetworkName_Type()
)
nodeNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkName.setStatus("mandatory")


class _NodeName_Type(DisplayString):
    """Custom type nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeName_Type.__name__ = "DisplayString"
_NodeName_Object = MibTableColumn
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1, 2),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeName.setStatus("mandatory")
_Svnode_ObjectIdentity = ObjectIdentity
svnode = _Svnode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2)
)
_SvNodeGroup_ObjectIdentity = ObjectIdentity
svNodeGroup = _SvNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 1)
)


class _NodeGrpName_Type(DisplayString):
    """Custom type nodeGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpName_Type.__name__ = "DisplayString"
_NodeGrpName_Object = MibScalar
nodeGrpName = _NodeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 1),
    _NodeGrpName_Type()
)
nodeGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpName.setStatus("mandatory")


class _NodeGrpNetName_Type(DisplayString):
    """Custom type nodeGrpNetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpNetName_Type.__name__ = "DisplayString"
_NodeGrpNetName_Object = MibScalar
nodeGrpNetName = _NodeGrpNetName_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 2),
    _NodeGrpNetName_Type()
)
nodeGrpNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpNetName.setStatus("mandatory")


class _NodeGrpAlarmState_Type(Integer32):
    """Custom type nodeGrpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2),
          ("unreachable", 5))
    )


_NodeGrpAlarmState_Type.__name__ = "Integer32"
_NodeGrpAlarmState_Object = MibScalar
nodeGrpAlarmState = _NodeGrpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 3),
    _NodeGrpAlarmState_Type()
)
nodeGrpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpAlarmState.setStatus("mandatory")


class _NodeGrpGateway_Type(Integer32):
    """Custom type nodeGrpGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 2),
          ("not-a-gateway", 1))
    )


_NodeGrpGateway_Type.__name__ = "Integer32"
_NodeGrpGateway_Object = MibScalar
nodeGrpGateway = _NodeGrpGateway_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 4),
    _NodeGrpGateway_Type()
)
nodeGrpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpGateway.setStatus("mandatory")
_NodeGrpActive_Type = Active
_NodeGrpActive_Object = MibScalar
nodeGrpActive = _NodeGrpActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 5),
    _NodeGrpActive_Type()
)
nodeGrpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpActive.setStatus("mandatory")


class _NodeGrpPlatform_Type(Integer32):
    """Custom type nodeGrpPlatform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("axis-platform", 3),
          ("bpx-platform", 2),
          ("ipx-platform", 1))
    )


_NodeGrpPlatform_Type.__name__ = "Integer32"
_NodeGrpPlatform_Object = MibScalar
nodeGrpPlatform = _NodeGrpPlatform_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 6),
    _NodeGrpPlatform_Type()
)
nodeGrpPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpPlatform.setStatus("mandatory")


class _NodeGrpRelease_Type(DisplayString):
    """Custom type nodeGrpRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpRelease_Type.__name__ = "DisplayString"
_NodeGrpRelease_Object = MibScalar
nodeGrpRelease = _NodeGrpRelease_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 7),
    _NodeGrpRelease_Type()
)
nodeGrpRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpRelease.setStatus("mandatory")
_NodeFsIncRate_Type = Integer32
_NodeFsIncRate_Object = MibScalar
nodeFsIncRate = _NodeFsIncRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 8),
    _NodeFsIncRate_Type()
)
nodeFsIncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsIncRate.setStatus("mandatory")
_NodeFsDecRate_Type = Integer32
_NodeFsDecRate_Object = MibScalar
nodeFsDecRate = _NodeFsDecRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 9),
    _NodeFsDecRate_Type()
)
nodeFsDecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsDecRate.setStatus("mandatory")
_NodeFsFastRate_Type = Integer32
_NodeFsFastRate_Object = MibScalar
nodeFsFastRate = _NodeFsFastRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 10),
    _NodeFsFastRate_Type()
)
nodeFsFastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsFastRate.setStatus("mandatory")
_NodeRstTimeout_Type = Integer32
_NodeRstTimeout_Object = MibScalar
nodeRstTimeout = _NodeRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 11),
    _NodeRstTimeout_Type()
)
nodeRstTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRstTimeout.setStatus("mandatory")
_AlarmTrapSequenceNumber_Type = Integer32
_AlarmTrapSequenceNumber_Object = MibScalar
alarmTrapSequenceNumber = _AlarmTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 12),
    _AlarmTrapSequenceNumber_Type()
)
alarmTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrapSequenceNumber.setStatus("mandatory")
_PacketGroup_ObjectIdentity = ObjectIdentity
packetGroup = _PacketGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 2)
)
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("mandatory")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1)
)
trunkEntry.setIndexNames(
    (0, "STRATACOM-MIB", "trunkLocalSlot"),
    (0, "STRATACOM-MIB", "trunkLocalPort"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("mandatory")
_TrunkLocalSlot_Type = Integer32
_TrunkLocalSlot_Object = MibTableColumn
trunkLocalSlot = _TrunkLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 1),
    _TrunkLocalSlot_Type()
)
trunkLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalSlot.setStatus("mandatory")
_TrunkLocalPort_Type = Integer32
_TrunkLocalPort_Object = MibTableColumn
trunkLocalPort = _TrunkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 2),
    _TrunkLocalPort_Type()
)
trunkLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalPort.setStatus("mandatory")
_TrunkLocalLine_Type = Integer32
_TrunkLocalLine_Object = MibTableColumn
trunkLocalLine = _TrunkLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 3),
    _TrunkLocalLine_Type()
)
trunkLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalLine.setStatus("mandatory")


class _TrunkCardType_Type(Integer32):
    """Custom type trunkCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              22,
              31,
              34,
              103,
              104,
              110)
        )
    )
    namedValues = NamedValues(
        *(("ait", 34),
          ("atm", 31),
          ("bni", 4),
          ("bni-e3", 104),
          ("bni-oc3", 110),
          ("bni-t3", 103),
          ("ntc", 22),
          ("txr", 3))
    )


_TrunkCardType_Type.__name__ = "Integer32"
_TrunkCardType_Object = MibTableColumn
trunkCardType = _TrunkCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 4),
    _TrunkCardType_Type()
)
trunkCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCardType.setStatus("mandatory")


class _TrunkInterface_Type(Integer32):
    """Custom type trunkInterface based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("atm", 8),
          ("e1-30", 4),
          ("e1-31", 5),
          ("e1-32", 6),
          ("subrate", 7),
          ("t1-d4", 2),
          ("t1-esf", 3),
          ("unknown", 1))
    )


_TrunkInterface_Type.__name__ = "Integer32"
_TrunkInterface_Object = MibTableColumn
trunkInterface = _TrunkInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 5),
    _TrunkInterface_Type()
)
trunkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInterface.setStatus("mandatory")
_TrunkLineLoad_Type = Integer32
_TrunkLineLoad_Object = MibTableColumn
trunkLineLoad = _TrunkLineLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 6),
    _TrunkLineLoad_Type()
)
trunkLineLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLineLoad.setStatus("mandatory")
_TrunkRemNodeId_Type = Integer32
_TrunkRemNodeId_Object = MibTableColumn
trunkRemNodeId = _TrunkRemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 7),
    _TrunkRemNodeId_Type()
)
trunkRemNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemNodeId.setStatus("mandatory")
_TrunkRemLineNumber_Type = Integer32
_TrunkRemLineNumber_Object = MibTableColumn
trunkRemLineNumber = _TrunkRemLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 8),
    _TrunkRemLineNumber_Type()
)
trunkRemLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemLineNumber.setStatus("mandatory")
_TrunkRemSlot_Type = Integer32
_TrunkRemSlot_Object = MibTableColumn
trunkRemSlot = _TrunkRemSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 9),
    _TrunkRemSlot_Type()
)
trunkRemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemSlot.setStatus("mandatory")
_TrunkRemPort_Type = Integer32
_TrunkRemPort_Object = MibTableColumn
trunkRemPort = _TrunkRemPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 10),
    _TrunkRemPort_Type()
)
trunkRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemPort.setStatus("mandatory")


class _TrunkAlarmState_Type(Integer32):
    """Custom type trunkAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2))
    )


_TrunkAlarmState_Type.__name__ = "Integer32"
_TrunkAlarmState_Object = MibTableColumn
trunkAlarmState = _TrunkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 11),
    _TrunkAlarmState_Type()
)
trunkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkAlarmState.setStatus("mandatory")


class _TrunkComment_Type(DisplayString):
    """Custom type trunkComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrunkComment_Type.__name__ = "DisplayString"
_TrunkComment_Object = MibTableColumn
trunkComment = _TrunkComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 12),
    _TrunkComment_Type()
)
trunkComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkComment.setStatus("mandatory")
_TrunkActive_Type = Active
_TrunkActive_Object = MibTableColumn
trunkActive = _TrunkActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 13),
    _TrunkActive_Type()
)
trunkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkActive.setStatus("mandatory")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 14),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("mandatory")
_TrunkStatReserve_Type = Integer32
_TrunkStatReserve_Object = MibTableColumn
trunkStatReserve = _TrunkStatReserve_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 15),
    _TrunkStatReserve_Type()
)
trunkStatReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatReserve.setStatus("mandatory")
_TrunkBurstyDataBQDepth_Type = Integer32
_TrunkBurstyDataBQDepth_Object = MibTableColumn
trunkBurstyDataBQDepth = _TrunkBurstyDataBQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 16),
    _TrunkBurstyDataBQDepth_Type()
)
trunkBurstyDataBQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkBurstyDataBQDepth.setStatus("mandatory")
_TrunkBurstyDataBQEfcnThreshold_Type = Integer32
_TrunkBurstyDataBQEfcnThreshold_Object = MibTableColumn
trunkBurstyDataBQEfcnThreshold = _TrunkBurstyDataBQEfcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 17),
    _TrunkBurstyDataBQEfcnThreshold_Type()
)
trunkBurstyDataBQEfcnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkBurstyDataBQEfcnThreshold.setStatus("mandatory")
_TrunkClpHighDropThreshold_Type = Integer32
_TrunkClpHighDropThreshold_Object = MibTableColumn
trunkClpHighDropThreshold = _TrunkClpHighDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 18),
    _TrunkClpHighDropThreshold_Type()
)
trunkClpHighDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkClpHighDropThreshold.setStatus("mandatory")
_TrunkClpLowDropThreshold_Type = Integer32
_TrunkClpLowDropThreshold_Object = MibTableColumn
trunkClpLowDropThreshold = _TrunkClpLowDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 19),
    _TrunkClpLowDropThreshold_Type()
)
trunkClpLowDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkClpLowDropThreshold.setStatus("mandatory")
_CircuitGroup_ObjectIdentity = ObjectIdentity
circuitGroup = _CircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 3)
)
_CirLineTable_Object = MibTable
cirLineTable = _CirLineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cirLineTable.setStatus("mandatory")
_CirLineEntry_Object = MibTableRow
cirLineEntry = _CirLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1)
)
cirLineEntry.setIndexNames(
    (0, "STRATACOM-MIB", "cirLineLineNumber"),
    (0, "STRATACOM-MIB", "cirLinePortNumber"),
)
if mibBuilder.loadTexts:
    cirLineEntry.setStatus("mandatory")
_CirLineLineNumber_Type = Integer32
_CirLineLineNumber_Object = MibTableColumn
cirLineLineNumber = _CirLineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 3),
    _CirLineLineNumber_Type()
)
cirLineLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineLineNumber.setStatus("mandatory")


class _CirLineCardType_Type(Integer32):
    """Custom type cirLineCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              21,
              25,
              29)
        )
    )
    namedValues = NamedValues(
        *(("cdp", 29),
          ("cip", 21),
          ("frp", 25),
          ("txr", 3))
    )


_CirLineCardType_Type.__name__ = "Integer32"
_CirLineCardType_Object = MibTableColumn
cirLineCardType = _CirLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 4),
    _CirLineCardType_Type()
)
cirLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineCardType.setStatus("mandatory")


class _CirLineInterface_Type(Integer32):
    """Custom type cirLineInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("t1", 2),
          ("unknown", 1))
    )


_CirLineInterface_Type.__name__ = "Integer32"
_CirLineInterface_Object = MibTableColumn
cirLineInterface = _CirLineInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 5),
    _CirLineInterface_Type()
)
cirLineInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineInterface.setStatus("mandatory")


class _CirLineComment_Type(DisplayString):
    """Custom type cirLineComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_CirLineComment_Type.__name__ = "DisplayString"
_CirLineComment_Object = MibTableColumn
cirLineComment = _CirLineComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 6),
    _CirLineComment_Type()
)
cirLineComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineComment.setStatus("mandatory")
_CirLineActive_Type = Active
_CirLineActive_Object = MibTableColumn
cirLineActive = _CirLineActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 7),
    _CirLineActive_Type()
)
cirLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineActive.setStatus("mandatory")


class _CirLineStatus_Type(Integer32):
    """Custom type cirLineStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_CirLineStatus_Type.__name__ = "Integer32"
_CirLineStatus_Object = MibTableColumn
cirLineStatus = _CirLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 8),
    _CirLineStatus_Type()
)
cirLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineStatus.setStatus("mandatory")
_CirLinePortNumber_Type = Integer32
_CirLinePortNumber_Object = MibTableColumn
cirLinePortNumber = _CirLinePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 9),
    _CirLinePortNumber_Type()
)
cirLinePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLinePortNumber.setStatus("mandatory")
_FrpGroup_ObjectIdentity = ObjectIdentity
frpGroup = _FrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 4)
)
_FrpTable_Object = MibTable
frpTable = _FrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1)
)
if mibBuilder.loadTexts:
    frpTable.setStatus("mandatory")
_FrpEntry_Object = MibTableRow
frpEntry = _FrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1)
)
frpEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frpLocalSlot"),
    (0, "STRATACOM-MIB", "frpLocalLine"),
    (0, "STRATACOM-MIB", "frpLocalPort"),
)
if mibBuilder.loadTexts:
    frpEntry.setStatus("mandatory")
_FrpLocalSlot_Type = Integer32
_FrpLocalSlot_Object = MibTableColumn
frpLocalSlot = _FrpLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 3),
    _FrpLocalSlot_Type()
)
frpLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalSlot.setStatus("mandatory")
_FrpLocalPort_Type = Integer32
_FrpLocalPort_Object = MibTableColumn
frpLocalPort = _FrpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 4),
    _FrpLocalPort_Type()
)
frpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalPort.setStatus("mandatory")
_FrpPortSpeed_Type = Integer32
_FrpPortSpeed_Object = MibTableColumn
frpPortSpeed = _FrpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 5),
    _FrpPortSpeed_Type()
)
frpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpPortSpeed.setStatus("mandatory")


class _FrpComment_Type(DisplayString):
    """Custom type frpComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_FrpComment_Type.__name__ = "DisplayString"
_FrpComment_Object = MibTableColumn
frpComment = _FrpComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 6),
    _FrpComment_Type()
)
frpComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpComment.setStatus("mandatory")
_FrpActive_Type = Active
_FrpActive_Object = MibTableColumn
frpActive = _FrpActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 7),
    _FrpActive_Type()
)
frpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpActive.setStatus("mandatory")


class _FrpStatus_Type(Integer32):
    """Custom type frpStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_FrpStatus_Type.__name__ = "Integer32"
_FrpStatus_Object = MibTableColumn
frpStatus = _FrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 8),
    _FrpStatus_Type()
)
frpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpStatus.setStatus("mandatory")
_FrpQDepth_Type = Integer32
_FrpQDepth_Object = MibTableColumn
frpQDepth = _FrpQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 9),
    _FrpQDepth_Type()
)
frpQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpQDepth.setStatus("mandatory")
_FrpEcnThreshold_Type = Integer32
_FrpEcnThreshold_Object = MibTableColumn
frpEcnThreshold = _FrpEcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 10),
    _FrpEcnThreshold_Type()
)
frpEcnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpEcnThreshold.setStatus("mandatory")
_FrpDeThreshold_Type = Integer32
_FrpDeThreshold_Object = MibTableColumn
frpDeThreshold = _FrpDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 11),
    _FrpDeThreshold_Type()
)
frpDeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpDeThreshold.setStatus("mandatory")


class _FrpPortType_Type(Integer32):
    """Custom type frpPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aip", 3),
          ("frsm", 5),
          ("nni", 2),
          ("not-defined", 4),
          ("portConcent", 6),
          ("uni", 1))
    )


_FrpPortType_Type.__name__ = "Integer32"
_FrpPortType_Object = MibTableColumn
frpPortType = _FrpPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 12),
    _FrpPortType_Type()
)
frpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpPortType.setStatus("mandatory")
_FrpLocalLine_Type = Integer32
_FrpLocalLine_Object = MibTableColumn
frpLocalLine = _FrpLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 13),
    _FrpLocalLine_Type()
)
frpLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalLine.setStatus("mandatory")
_ConnGroup_ObjectIdentity = ObjectIdentity
connGroup = _ConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 5)
)
_ConnServerTable_Object = MibTable
connServerTable = _ConnServerTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1)
)
if mibBuilder.loadTexts:
    connServerTable.setStatus("mandatory")
_ConnEntry_Object = MibTableRow
connEntry = _ConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1)
)
connEntry.setIndexNames(
    (0, "STRATACOM-MIB", "connLocalSlot"),
    (0, "STRATACOM-MIB", "connLocalLine"),
    (0, "STRATACOM-MIB", "connLocalChannel"),
    (0, "STRATACOM-MIB", "connLocalDLCI"),
)
if mibBuilder.loadTexts:
    connEntry.setStatus("mandatory")
_ConnLocalSlot_Type = Integer32
_ConnLocalSlot_Object = MibTableColumn
connLocalSlot = _ConnLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 3),
    _ConnLocalSlot_Type()
)
connLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalSlot.setStatus("mandatory")
_ConnLocalChannel_Type = Integer32
_ConnLocalChannel_Object = MibTableColumn
connLocalChannel = _ConnLocalChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 4),
    _ConnLocalChannel_Type()
)
connLocalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalChannel.setStatus("mandatory")
_ConnLocalDLCI_Type = Integer32
_ConnLocalDLCI_Object = MibTableColumn
connLocalDLCI = _ConnLocalDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 5),
    _ConnLocalDLCI_Type()
)
connLocalDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalDLCI.setStatus("mandatory")
_ConnRemoteNodeId_Type = Integer32
_ConnRemoteNodeId_Object = MibTableColumn
connRemoteNodeId = _ConnRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 6),
    _ConnRemoteNodeId_Type()
)
connRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteNodeId.setStatus("mandatory")
_ConnRemoteSlot_Type = Integer32
_ConnRemoteSlot_Object = MibTableColumn
connRemoteSlot = _ConnRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 7),
    _ConnRemoteSlot_Type()
)
connRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteSlot.setStatus("mandatory")
_ConnRemoteChannel_Type = Integer32
_ConnRemoteChannel_Object = MibTableColumn
connRemoteChannel = _ConnRemoteChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 8),
    _ConnRemoteChannel_Type()
)
connRemoteChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteChannel.setStatus("mandatory")
_ConnRemoteDLCI_Type = Integer32
_ConnRemoteDLCI_Object = MibTableColumn
connRemoteDLCI = _ConnRemoteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 9),
    _ConnRemoteDLCI_Type()
)
connRemoteDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteDLCI.setStatus("mandatory")


class _ConnServerType_Type(Integer32):
    """Custom type connServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("data", 5),
          ("frame-relay", 6),
          ("voice", 3),
          ("voice-adpcm", 4),
          ("voice-dsi", 2),
          ("voice-dsi-adpcm", 1))
    )


_ConnServerType_Type.__name__ = "Integer32"
_ConnServerType_Object = MibTableColumn
connServerType = _ConnServerType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 10),
    _ConnServerType_Type()
)
connServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connServerType.setStatus("mandatory")
_ConnRate_Type = Integer32
_ConnRate_Object = MibTableColumn
connRate = _ConnRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 11),
    _ConnRate_Type()
)
connRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRate.setStatus("mandatory")
_ConnLocalMaxPkts_Type = Integer32
_ConnLocalMaxPkts_Object = MibTableColumn
connLocalMaxPkts = _ConnLocalMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 12),
    _ConnLocalMaxPkts_Type()
)
connLocalMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalMaxPkts.setStatus("mandatory")
_ConnRemoteMaxPkts_Type = Integer32
_ConnRemoteMaxPkts_Object = MibTableColumn
connRemoteMaxPkts = _ConnRemoteMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 13),
    _ConnRemoteMaxPkts_Type()
)
connRemoteMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteMaxPkts.setStatus("mandatory")
_ConnMinBandwidth_Type = Integer32
_ConnMinBandwidth_Object = MibTableColumn
connMinBandwidth = _ConnMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 14),
    _ConnMinBandwidth_Type()
)
connMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMinBandwidth.setStatus("mandatory")


class _ConnDAX_Type(Integer32):
    """Custom type connDAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dax", 2),
          ("non-dax", 1))
    )


_ConnDAX_Type.__name__ = "Integer32"
_ConnDAX_Object = MibTableColumn
connDAX = _ConnDAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 15),
    _ConnDAX_Type()
)
connDAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connDAX.setStatus("mandatory")


class _ConnTXR_Type(Integer32):
    """Custom type connTXR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-txr", 1),
          ("txr", 2))
    )


_ConnTXR_Type.__name__ = "Integer32"
_ConnTXR_Object = MibTableColumn
connTXR = _ConnTXR_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 16),
    _ConnTXR_Type()
)
connTXR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connTXR.setStatus("mandatory")


class _ConnComment_Type(DisplayString):
    """Custom type connComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ConnComment_Type.__name__ = "DisplayString"
_ConnComment_Object = MibTableColumn
connComment = _ConnComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 17),
    _ConnComment_Type()
)
connComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connComment.setStatus("mandatory")
_ConnActive_Type = Active
_ConnActive_Object = MibTableColumn
connActive = _ConnActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 18),
    _ConnActive_Type()
)
connActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connActive.setStatus("mandatory")


class _ConnStatus_Type(Integer32):
    """Custom type connStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_ConnStatus_Type.__name__ = "Integer32"
_ConnStatus_Object = MibTableColumn
connStatus = _ConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 19),
    _ConnStatus_Type()
)
connStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connStatus.setStatus("mandatory")
_ConnQir_Type = Integer32
_ConnQir_Object = MibTableColumn
connQir = _ConnQir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 20),
    _ConnQir_Type()
)
connQir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connQir.setStatus("mandatory")
_ConnPir_Type = Integer32
_ConnPir_Object = MibTableColumn
connPir = _ConnPir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 21),
    _ConnPir_Type()
)
connPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPir.setStatus("mandatory")
_ConnVcQueDepth_Type = Integer32
_ConnVcQueDepth_Object = MibTableColumn
connVcQueDepth = _ConnVcQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 22),
    _ConnVcQueDepth_Type()
)
connVcQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVcQueDepth.setStatus("mandatory")
_ConnVcQueThreshold_Type = Integer32
_ConnVcQueThreshold_Object = MibTableColumn
connVcQueThreshold = _ConnVcQueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 23),
    _ConnVcQueThreshold_Type()
)
connVcQueThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVcQueThreshold.setStatus("mandatory")
_ConnCMax_Type = Integer32
_ConnCMax_Object = MibTableColumn
connCMax = _ConnCMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 24),
    _ConnCMax_Type()
)
connCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCMax.setStatus("mandatory")
_ConnPerUtil_Type = Integer32
_ConnPerUtil_Object = MibTableColumn
connPerUtil = _ConnPerUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 25),
    _ConnPerUtil_Type()
)
connPerUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPerUtil.setStatus("mandatory")
_ConnConnInfoFlag_Type = Integer32
_ConnConnInfoFlag_Object = MibTableColumn
connConnInfoFlag = _ConnConnInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 26),
    _ConnConnInfoFlag_Type()
)
connConnInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConnInfoFlag.setStatus("mandatory")
_ConnCir_Type = Integer32
_ConnCir_Object = MibTableColumn
connCir = _ConnCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 27),
    _ConnCir_Type()
)
connCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCir.setStatus("mandatory")
_ConnABitStatus_Type = Integer32
_ConnABitStatus_Object = MibTableColumn
connABitStatus = _ConnABitStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 28),
    _ConnABitStatus_Type()
)
connABitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connABitStatus.setStatus("mandatory")
_ConnLocalLine_Type = Integer32
_ConnLocalLine_Object = MibTableColumn
connLocalLine = _ConnLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 29),
    _ConnLocalLine_Type()
)
connLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalLine.setStatus("mandatory")
_RealTimeCountersGroup_ObjectIdentity = ObjectIdentity
realTimeCountersGroup = _RealTimeCountersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 6)
)
_CirLineRTCTable_Object = MibTable
cirLineRTCTable = _CirLineRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cirLineRTCTable.setStatus("mandatory")
_CirLineRTCEntry_Object = MibTableRow
cirLineRTCEntry = _CirLineRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1)
)
cirLineRTCEntry.setIndexNames(
    (0, "STRATACOM-MIB", "cirLineRTCLineNumber"),
)
if mibBuilder.loadTexts:
    cirLineRTCEntry.setStatus("mandatory")
_CirLineRTCLineNumber_Type = Integer32
_CirLineRTCLineNumber_Object = MibTableColumn
cirLineRTCLineNumber = _CirLineRTCLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 1),
    _CirLineRTCLineNumber_Type()
)
cirLineRTCLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCLineNumber.setStatus("mandatory")
_CirLineRTCBipolarViolations_Type = Counter32
_CirLineRTCBipolarViolations_Object = MibTableColumn
cirLineRTCBipolarViolations = _CirLineRTCBipolarViolations_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 4),
    _CirLineRTCBipolarViolations_Type()
)
cirLineRTCBipolarViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCBipolarViolations.setStatus("mandatory")
_CirLineRTCFrameSlips_Type = Counter32
_CirLineRTCFrameSlips_Object = MibTableColumn
cirLineRTCFrameSlips = _CirLineRTCFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 5),
    _CirLineRTCFrameSlips_Type()
)
cirLineRTCFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCFrameSlips.setStatus("mandatory")
_CirLineRTCOutOfFrames_Type = Counter32
_CirLineRTCOutOfFrames_Object = MibTableColumn
cirLineRTCOutOfFrames = _CirLineRTCOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 6),
    _CirLineRTCOutOfFrames_Type()
)
cirLineRTCOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCOutOfFrames.setStatus("mandatory")
_CirLineRTCLossesOfSignal_Type = Counter32
_CirLineRTCLossesOfSignal_Object = MibTableColumn
cirLineRTCLossesOfSignal = _CirLineRTCLossesOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 7),
    _CirLineRTCLossesOfSignal_Type()
)
cirLineRTCLossesOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCLossesOfSignal.setStatus("mandatory")
_CirLineRTCFrameBitErrors_Type = Counter32
_CirLineRTCFrameBitErrors_Object = MibTableColumn
cirLineRTCFrameBitErrors = _CirLineRTCFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 8),
    _CirLineRTCFrameBitErrors_Type()
)
cirLineRTCFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCFrameBitErrors.setStatus("mandatory")
_CirLineRTCCrcErrors_Type = Counter32
_CirLineRTCCrcErrors_Object = MibTableColumn
cirLineRTCCrcErrors = _CirLineRTCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 9),
    _CirLineRTCCrcErrors_Type()
)
cirLineRTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCCrcErrors.setStatus("mandatory")
_CirLineRTCOutOfMultiFrames_Type = Counter32
_CirLineRTCOutOfMultiFrames_Object = MibTableColumn
cirLineRTCOutOfMultiFrames = _CirLineRTCOutOfMultiFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 10),
    _CirLineRTCOutOfMultiFrames_Type()
)
cirLineRTCOutOfMultiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCOutOfMultiFrames.setStatus("mandatory")
_CirLineRTCAllOnesInTimeslot16_Type = Counter32
_CirLineRTCAllOnesInTimeslot16_Object = MibTableColumn
cirLineRTCAllOnesInTimeslot16 = _CirLineRTCAllOnesInTimeslot16_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 11),
    _CirLineRTCAllOnesInTimeslot16_Type()
)
cirLineRTCAllOnesInTimeslot16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCAllOnesInTimeslot16.setStatus("mandatory")
_FrpRTCTable_Object = MibTable
frpRTCTable = _FrpRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3)
)
if mibBuilder.loadTexts:
    frpRTCTable.setStatus("mandatory")
_FrpRTCEntry_Object = MibTableRow
frpRTCEntry = _FrpRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1)
)
frpRTCEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frpRTCSlot"),
    (0, "STRATACOM-MIB", "frpRTCLine"),
    (0, "STRATACOM-MIB", "frpRTCPort"),
)
if mibBuilder.loadTexts:
    frpRTCEntry.setStatus("mandatory")
_FrpRTCSlot_Type = Integer32
_FrpRTCSlot_Object = MibTableColumn
frpRTCSlot = _FrpRTCSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 1),
    _FrpRTCSlot_Type()
)
frpRTCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCSlot.setStatus("mandatory")
_FrpRTCPort_Type = Integer32
_FrpRTCPort_Object = MibTableColumn
frpRTCPort = _FrpRTCPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 2),
    _FrpRTCPort_Type()
)
frpRTCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCPort.setStatus("mandatory")
_FrpRTCFramesRcvd_Type = Counter32
_FrpRTCFramesRcvd_Object = MibTableColumn
frpRTCFramesRcvd = _FrpRTCFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 4),
    _FrpRTCFramesRcvd_Type()
)
frpRTCFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvd.setStatus("mandatory")
_FrpRTCFramesXmitted_Type = Counter32
_FrpRTCFramesXmitted_Object = MibTableColumn
frpRTCFramesXmitted = _FrpRTCFramesXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 5),
    _FrpRTCFramesXmitted_Type()
)
frpRTCFramesXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmitted.setStatus("mandatory")
_FrpRTCBytesRcvd_Type = Counter32
_FrpRTCBytesRcvd_Object = MibTableColumn
frpRTCBytesRcvd = _FrpRTCBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 6),
    _FrpRTCBytesRcvd_Type()
)
frpRTCBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBytesRcvd.setStatus("mandatory")
_FrpRTCBytesXmitted_Type = Counter32
_FrpRTCBytesXmitted_Object = MibTableColumn
frpRTCBytesXmitted = _FrpRTCBytesXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 7),
    _FrpRTCBytesXmitted_Type()
)
frpRTCBytesXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBytesXmitted.setStatus("mandatory")
_FrpRTCFramesXmittedWithFECN_Type = Counter32
_FrpRTCFramesXmittedWithFECN_Object = MibTableColumn
frpRTCFramesXmittedWithFECN = _FrpRTCFramesXmittedWithFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 8),
    _FrpRTCFramesXmittedWithFECN_Type()
)
frpRTCFramesXmittedWithFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmittedWithFECN.setStatus("mandatory")
_FrpRTCFramesXmittedWithBECN_Type = Counter32
_FrpRTCFramesXmittedWithBECN_Object = MibTableColumn
frpRTCFramesXmittedWithBECN = _FrpRTCFramesXmittedWithBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 9),
    _FrpRTCFramesXmittedWithBECN_Type()
)
frpRTCFramesXmittedWithBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmittedWithBECN.setStatus("mandatory")
_FrpRTCFramesRcvdCrcErrors_Type = Counter32
_FrpRTCFramesRcvdCrcErrors_Object = MibTableColumn
frpRTCFramesRcvdCrcErrors = _FrpRTCFramesRcvdCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 10),
    _FrpRTCFramesRcvdCrcErrors_Type()
)
frpRTCFramesRcvdCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdCrcErrors.setStatus("mandatory")
_FrpRTCFramesRcvdInvalidFormat_Type = Counter32
_FrpRTCFramesRcvdInvalidFormat_Object = MibTableColumn
frpRTCFramesRcvdInvalidFormat = _FrpRTCFramesRcvdInvalidFormat_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 11),
    _FrpRTCFramesRcvdInvalidFormat_Type()
)
frpRTCFramesRcvdInvalidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdInvalidFormat.setStatus("mandatory")
_FrpRTCFramesRcvdAlignmentErrors_Type = Counter32
_FrpRTCFramesRcvdAlignmentErrors_Object = MibTableColumn
frpRTCFramesRcvdAlignmentErrors = _FrpRTCFramesRcvdAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 12),
    _FrpRTCFramesRcvdAlignmentErrors_Type()
)
frpRTCFramesRcvdAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdAlignmentErrors.setStatus("mandatory")
_FrpRTCFramesRcvdIllegalLen_Type = Counter32
_FrpRTCFramesRcvdIllegalLen_Object = MibTableColumn
frpRTCFramesRcvdIllegalLen = _FrpRTCFramesRcvdIllegalLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 13),
    _FrpRTCFramesRcvdIllegalLen_Type()
)
frpRTCFramesRcvdIllegalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdIllegalLen.setStatus("mandatory")
_FrpRTCDmaOverruns_Type = Counter32
_FrpRTCDmaOverruns_Object = MibTableColumn
frpRTCDmaOverruns = _FrpRTCDmaOverruns_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 14),
    _FrpRTCDmaOverruns_Type()
)
frpRTCDmaOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCDmaOverruns.setStatus("mandatory")
_FrpRTCLmiStatusEnquires_Type = Counter32
_FrpRTCLmiStatusEnquires_Object = MibTableColumn
frpRTCLmiStatusEnquires = _FrpRTCLmiStatusEnquires_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 15),
    _FrpRTCLmiStatusEnquires_Type()
)
frpRTCLmiStatusEnquires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusEnquires.setStatus("mandatory")
_FrpRTCLmiStatusXmitRate_Type = Counter32
_FrpRTCLmiStatusXmitRate_Object = MibTableColumn
frpRTCLmiStatusXmitRate = _FrpRTCLmiStatusXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 16),
    _FrpRTCLmiStatusXmitRate_Type()
)
frpRTCLmiStatusXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusXmitRate.setStatus("mandatory")
_FrpRTCLmiStatusUpdateRate_Type = Counter32
_FrpRTCLmiStatusUpdateRate_Object = MibTableColumn
frpRTCLmiStatusUpdateRate = _FrpRTCLmiStatusUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 17),
    _FrpRTCLmiStatusUpdateRate_Type()
)
frpRTCLmiStatusUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusUpdateRate.setStatus("mandatory")
_FrpRTCLmiInvalidStatusEnquires_Type = Counter32
_FrpRTCLmiInvalidStatusEnquires_Object = MibTableColumn
frpRTCLmiInvalidStatusEnquires = _FrpRTCLmiInvalidStatusEnquires_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 18),
    _FrpRTCLmiInvalidStatusEnquires_Type()
)
frpRTCLmiInvalidStatusEnquires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiInvalidStatusEnquires.setStatus("mandatory")
_FrpRTCLmiLinkTimeoutErrors_Type = Counter32
_FrpRTCLmiLinkTimeoutErrors_Object = MibTableColumn
frpRTCLmiLinkTimeoutErrors = _FrpRTCLmiLinkTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 19),
    _FrpRTCLmiLinkTimeoutErrors_Type()
)
frpRTCLmiLinkTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiLinkTimeoutErrors.setStatus("mandatory")
_FrpRTCLmiKeepaliveSequenceErrors_Type = Counter32
_FrpRTCLmiKeepaliveSequenceErrors_Object = MibTableColumn
frpRTCLmiKeepaliveSequenceErrors = _FrpRTCLmiKeepaliveSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 20),
    _FrpRTCLmiKeepaliveSequenceErrors_Type()
)
frpRTCLmiKeepaliveSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiKeepaliveSequenceErrors.setStatus("mandatory")
_FrpRTCFramesRcvdUndefDlciErrors_Type = Counter32
_FrpRTCFramesRcvdUndefDlciErrors_Object = MibTableColumn
frpRTCFramesRcvdUndefDlciErrors = _FrpRTCFramesRcvdUndefDlciErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 21),
    _FrpRTCFramesRcvdUndefDlciErrors_Type()
)
frpRTCFramesRcvdUndefDlciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdUndefDlciErrors.setStatus("mandatory")
_FrpRTCXmitStatusEnquirey_Type = Counter32
_FrpRTCXmitStatusEnquirey_Object = MibTableColumn
frpRTCXmitStatusEnquirey = _FrpRTCXmitStatusEnquirey_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 22),
    _FrpRTCXmitStatusEnquirey_Type()
)
frpRTCXmitStatusEnquirey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCXmitStatusEnquirey.setStatus("mandatory")
_FrpRTCRxStatusCounter_Type = Counter32
_FrpRTCRxStatusCounter_Object = MibTableColumn
frpRTCRxStatusCounter = _FrpRTCRxStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 23),
    _FrpRTCRxStatusCounter_Type()
)
frpRTCRxStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCRxStatusCounter.setStatus("mandatory")
_FrpRTCAsyncStatusCounter_Type = Counter32
_FrpRTCAsyncStatusCounter_Object = MibTableColumn
frpRTCAsyncStatusCounter = _FrpRTCAsyncStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 24),
    _FrpRTCAsyncStatusCounter_Type()
)
frpRTCAsyncStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCAsyncStatusCounter.setStatus("mandatory")
_FrpRTCBadSequenceNumberCount_Type = Counter32
_FrpRTCBadSequenceNumberCount_Object = MibTableColumn
frpRTCBadSequenceNumberCount = _FrpRTCBadSequenceNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 25),
    _FrpRTCBadSequenceNumberCount_Type()
)
frpRTCBadSequenceNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBadSequenceNumberCount.setStatus("mandatory")
_FrpRTCTxProtocolTimeOutCount_Type = Counter32
_FrpRTCTxProtocolTimeOutCount_Object = MibTableColumn
frpRTCTxProtocolTimeOutCount = _FrpRTCTxProtocolTimeOutCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 26),
    _FrpRTCTxProtocolTimeOutCount_Type()
)
frpRTCTxProtocolTimeOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCTxProtocolTimeOutCount.setStatus("mandatory")
_FrpRTCCLLMFramesTx_Type = Counter32
_FrpRTCCLLMFramesTx_Object = MibTableColumn
frpRTCCLLMFramesTx = _FrpRTCCLLMFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 27),
    _FrpRTCCLLMFramesTx_Type()
)
frpRTCCLLMFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFramesTx.setStatus("mandatory")
_FrpRTCCLLMBytesTx_Type = Counter32
_FrpRTCCLLMBytesTx_Object = MibTableColumn
frpRTCCLLMBytesTx = _FrpRTCCLLMBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 28),
    _FrpRTCCLLMBytesTx_Type()
)
frpRTCCLLMBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMBytesTx.setStatus("mandatory")
_FrpRTCCLLMFramesRx_Type = Counter32
_FrpRTCCLLMFramesRx_Object = MibTableColumn
frpRTCCLLMFramesRx = _FrpRTCCLLMFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 29),
    _FrpRTCCLLMFramesRx_Type()
)
frpRTCCLLMFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFramesRx.setStatus("mandatory")
_FrpRTCCLLMBytesRx_Type = Counter32
_FrpRTCCLLMBytesRx_Object = MibTableColumn
frpRTCCLLMBytesRx = _FrpRTCCLLMBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 30),
    _FrpRTCCLLMBytesRx_Type()
)
frpRTCCLLMBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMBytesRx.setStatus("mandatory")
_FrpRTCCLLMFailures_Type = Counter32
_FrpRTCCLLMFailures_Object = MibTableColumn
frpRTCCLLMFailures = _FrpRTCCLLMFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 31),
    _FrpRTCCLLMFailures_Type()
)
frpRTCCLLMFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFailures.setStatus("mandatory")
_FrpRTCRxDEFramesDiscarded_Type = Counter32
_FrpRTCRxDEFramesDiscarded_Object = MibTableColumn
frpRTCRxDEFramesDiscarded = _FrpRTCRxDEFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 32),
    _FrpRTCRxDEFramesDiscarded_Type()
)
frpRTCRxDEFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCRxDEFramesDiscarded.setStatus("mandatory")
_FrpRTCLine_Type = Integer32
_FrpRTCLine_Object = MibTableColumn
frpRTCLine = _FrpRTCLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 33),
    _FrpRTCLine_Type()
)
frpRTCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLine.setStatus("mandatory")
_ConnRTCTable_Object = MibTable
connRTCTable = _ConnRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4)
)
if mibBuilder.loadTexts:
    connRTCTable.setStatus("mandatory")
_ConnRTCEntry_Object = MibTableRow
connRTCEntry = _ConnRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1)
)
connRTCEntry.setIndexNames(
    (0, "STRATACOM-MIB", "connRTCSlot"),
    (0, "STRATACOM-MIB", "connRTCLine"),
    (0, "STRATACOM-MIB", "connRTCChannel"),
    (0, "STRATACOM-MIB", "connRTCDLCI"),
)
if mibBuilder.loadTexts:
    connRTCEntry.setStatus("mandatory")
_ConnRTCSlot_Type = Integer32
_ConnRTCSlot_Object = MibTableColumn
connRTCSlot = _ConnRTCSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 1),
    _ConnRTCSlot_Type()
)
connRTCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSlot.setStatus("mandatory")
_ConnRTCChannel_Type = Integer32
_ConnRTCChannel_Object = MibTableColumn
connRTCChannel = _ConnRTCChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 2),
    _ConnRTCChannel_Type()
)
connRTCChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCChannel.setStatus("mandatory")
_ConnRTCDLCI_Type = Integer32
_ConnRTCDLCI_Object = MibTableColumn
connRTCDLCI = _ConnRTCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 3),
    _ConnRTCDLCI_Type()
)
connRTCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCDLCI.setStatus("mandatory")
_ConnRTCRcvdFrames_Type = Counter32
_ConnRTCRcvdFrames_Object = MibTableColumn
connRTCRcvdFrames = _ConnRTCRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 4),
    _ConnRTCRcvdFrames_Type()
)
connRTCRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdFrames.setStatus("mandatory")
_ConnRTCRcvdFramesDiscarded_Type = Counter32
_ConnRTCRcvdFramesDiscarded_Object = MibTableColumn
connRTCRcvdFramesDiscarded = _ConnRTCRcvdFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 5),
    _ConnRTCRcvdFramesDiscarded_Type()
)
connRTCRcvdFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdFramesDiscarded.setStatus("mandatory")
_ConnRTCXmitFrames_Type = Counter32
_ConnRTCXmitFrames_Object = MibTableColumn
connRTCXmitFrames = _ConnRTCXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 6),
    _ConnRTCXmitFrames_Type()
)
connRTCXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFrames.setStatus("mandatory")
_ConnRTCXmitFramesDiscarded_Type = Counter32
_ConnRTCXmitFramesDiscarded_Object = MibTableColumn
connRTCXmitFramesDiscarded = _ConnRTCXmitFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 7),
    _ConnRTCXmitFramesDiscarded_Type()
)
connRTCXmitFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesDiscarded.setStatus("mandatory")
_ConnRTCRcvdPkts_Type = Counter32
_ConnRTCRcvdPkts_Object = MibTableColumn
connRTCRcvdPkts = _ConnRTCRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 8),
    _ConnRTCRcvdPkts_Type()
)
connRTCRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdPkts.setStatus("mandatory")
_ConnRTCRcvdPktsDiscarded_Type = Counter32
_ConnRTCRcvdPktsDiscarded_Object = MibTableColumn
connRTCRcvdPktsDiscarded = _ConnRTCRcvdPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 9),
    _ConnRTCRcvdPktsDiscarded_Type()
)
connRTCRcvdPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdPktsDiscarded.setStatus("mandatory")
_ConnRTCXmitPkts_Type = Counter32
_ConnRTCXmitPkts_Object = MibTableColumn
connRTCXmitPkts = _ConnRTCXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 10),
    _ConnRTCXmitPkts_Type()
)
connRTCXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPkts.setStatus("mandatory")
_ConnRTCXmitPktsProjected_Type = Counter32
_ConnRTCXmitPktsProjected_Object = MibTableColumn
connRTCXmitPktsProjected = _ConnRTCXmitPktsProjected_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 11),
    _ConnRTCXmitPktsProjected_Type()
)
connRTCXmitPktsProjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPktsProjected.setStatus("mandatory")
_ConnRTCXmitPktsSupervisory_Type = Counter32
_ConnRTCXmitPktsSupervisory_Object = MibTableColumn
connRTCXmitPktsSupervisory = _ConnRTCXmitPktsSupervisory_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 12),
    _ConnRTCXmitPktsSupervisory_Type()
)
connRTCXmitPktsSupervisory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPktsSupervisory.setStatus("mandatory")
_ConnRTCRcvdBytes_Type = Counter32
_ConnRTCRcvdBytes_Object = MibTableColumn
connRTCRcvdBytes = _ConnRTCRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 13),
    _ConnRTCRcvdBytes_Type()
)
connRTCRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdBytes.setStatus("mandatory")
_ConnRTCRcvdBytesDiscarded_Type = Counter32
_ConnRTCRcvdBytesDiscarded_Object = MibTableColumn
connRTCRcvdBytesDiscarded = _ConnRTCRcvdBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 14),
    _ConnRTCRcvdBytesDiscarded_Type()
)
connRTCRcvdBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdBytesDiscarded.setStatus("mandatory")
_ConnRTCXmitBytes_Type = Counter32
_ConnRTCXmitBytes_Object = MibTableColumn
connRTCXmitBytes = _ConnRTCXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 15),
    _ConnRTCXmitBytes_Type()
)
connRTCXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitBytes.setStatus("mandatory")
_ConnRTCXmitBytesDiscarded_Type = Counter32
_ConnRTCXmitBytesDiscarded_Object = MibTableColumn
connRTCXmitBytesDiscarded = _ConnRTCXmitBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 16),
    _ConnRTCXmitBytesDiscarded_Type()
)
connRTCXmitBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitBytesDiscarded.setStatus("mandatory")
_ConnRTCSecondsV25ModemOn_Type = Counter32
_ConnRTCSecondsV25ModemOn_Object = MibTableColumn
connRTCSecondsV25ModemOn = _ConnRTCSecondsV25ModemOn_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 17),
    _ConnRTCSecondsV25ModemOn_Type()
)
connRTCSecondsV25ModemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsV25ModemOn.setStatus("mandatory")
_ConnRTCSecondsDsiEnabled_Type = Counter32
_ConnRTCSecondsDsiEnabled_Object = MibTableColumn
connRTCSecondsDsiEnabled = _ConnRTCSecondsDsiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 18),
    _ConnRTCSecondsDsiEnabled_Type()
)
connRTCSecondsDsiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsDsiEnabled.setStatus("mandatory")
_ConnRTCSecondsOffHook_Type = Counter32
_ConnRTCSecondsOffHook_Object = MibTableColumn
connRTCSecondsOffHook = _ConnRTCSecondsOffHook_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 19),
    _ConnRTCSecondsOffHook_Type()
)
connRTCSecondsOffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsOffHook.setStatus("mandatory")
_ConnRTCSecondsInService_Type = Counter32
_ConnRTCSecondsInService_Object = MibTableColumn
connRTCSecondsInService = _ConnRTCSecondsInService_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 20),
    _ConnRTCSecondsInService_Type()
)
connRTCSecondsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsInService.setStatus("mandatory")
_ConnRTCXmitFramesWithFECN_Type = Counter32
_ConnRTCXmitFramesWithFECN_Object = MibTableColumn
connRTCXmitFramesWithFECN = _ConnRTCXmitFramesWithFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 21),
    _ConnRTCXmitFramesWithFECN_Type()
)
connRTCXmitFramesWithFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesWithFECN.setStatus("mandatory")
_ConnRTCXmitFramesWithBECN_Type = Counter32
_ConnRTCXmitFramesWithBECN_Object = MibTableColumn
connRTCXmitFramesWithBECN = _ConnRTCXmitFramesWithBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 22),
    _ConnRTCXmitFramesWithBECN_Type()
)
connRTCXmitFramesWithBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesWithBECN.setStatus("mandatory")
_ConnRTCRxSupervisoryPkts_Type = Counter32
_ConnRTCRxSupervisoryPkts_Object = MibTableColumn
connRTCRxSupervisoryPkts = _ConnRTCRxSupervisoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 23),
    _ConnRTCRxSupervisoryPkts_Type()
)
connRTCRxSupervisoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRxSupervisoryPkts.setStatus("mandatory")
_ConnRTCCongestedMinuites_Type = Counter32
_ConnRTCCongestedMinuites_Object = MibTableColumn
connRTCCongestedMinuites = _ConnRTCCongestedMinuites_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 24),
    _ConnRTCCongestedMinuites_Type()
)
connRTCCongestedMinuites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCCongestedMinuites.setStatus("mandatory")
_ConnRTCFramesRxWithDE_Type = Counter32
_ConnRTCFramesRxWithDE_Object = MibTableColumn
connRTCFramesRxWithDE = _ConnRTCFramesRxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 25),
    _ConnRTCFramesRxWithDE_Type()
)
connRTCFramesRxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesRxWithDE.setStatus("mandatory")
_ConnRTCFramesTxWithDE_Type = Counter32
_ConnRTCFramesTxWithDE_Object = MibTableColumn
connRTCFramesTxWithDE = _ConnRTCFramesTxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 26),
    _ConnRTCFramesTxWithDE_Type()
)
connRTCFramesTxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesTxWithDE.setStatus("mandatory")
_ConnRTCFramesDiscardedWithDE_Type = Counter32
_ConnRTCFramesDiscardedWithDE_Object = MibTableColumn
connRTCFramesDiscardedWithDE = _ConnRTCFramesDiscardedWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 27),
    _ConnRTCFramesDiscardedWithDE_Type()
)
connRTCFramesDiscardedWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesDiscardedWithDE.setStatus("mandatory")
_ConnRTCBytesRxWithDE_Type = Counter32
_ConnRTCBytesRxWithDE_Object = MibTableColumn
connRTCBytesRxWithDE = _ConnRTCBytesRxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 28),
    _ConnRTCBytesRxWithDE_Type()
)
connRTCBytesRxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesRxWithDE.setStatus("mandatory")
_ConnRTCFramesRxExcessCir_Type = Counter32
_ConnRTCFramesRxExcessCir_Object = MibTableColumn
connRTCFramesRxExcessCir = _ConnRTCFramesRxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 29),
    _ConnRTCFramesRxExcessCir_Type()
)
connRTCFramesRxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesRxExcessCir.setStatus("mandatory")
_ConnRTCBytesRxExcessCir_Type = Counter32
_ConnRTCBytesRxExcessCir_Object = MibTableColumn
connRTCBytesRxExcessCir = _ConnRTCBytesRxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 30),
    _ConnRTCBytesRxExcessCir_Type()
)
connRTCBytesRxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesRxExcessCir.setStatus("mandatory")
_ConnRTCFramesTxExcessCir_Type = Counter32
_ConnRTCFramesTxExcessCir_Object = MibTableColumn
connRTCFramesTxExcessCir = _ConnRTCFramesTxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 31),
    _ConnRTCFramesTxExcessCir_Type()
)
connRTCFramesTxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesTxExcessCir.setStatus("mandatory")
_ConnRTCBytesTxExcessCir_Type = Counter32
_ConnRTCBytesTxExcessCir_Object = MibTableColumn
connRTCBytesTxExcessCir = _ConnRTCBytesTxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 32),
    _ConnRTCBytesTxExcessCir_Type()
)
connRTCBytesTxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesTxExcessCir.setStatus("mandatory")
_ConnRTCLine_Type = Integer32
_ConnRTCLine_Object = MibTableColumn
connRTCLine = _ConnRTCLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 33),
    _ConnRTCLine_Type()
)
connRTCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCLine.setStatus("mandatory")
_TrunkRTCTable_Object = MibTable
trunkRTCTable = _TrunkRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5)
)
if mibBuilder.loadTexts:
    trunkRTCTable.setStatus("mandatory")
_TrunkRTCEntry_Object = MibTableRow
trunkRTCEntry = _TrunkRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1)
)
trunkRTCEntry.setIndexNames(
    (0, "STRATACOM-MIB", "trunkRTCLocalSlot"),
    (0, "STRATACOM-MIB", "trunkRTCLocalPort"),
)
if mibBuilder.loadTexts:
    trunkRTCEntry.setStatus("mandatory")
_TrunkRTCLocalSlot_Type = Integer32
_TrunkRTCLocalSlot_Object = MibTableColumn
trunkRTCLocalSlot = _TrunkRTCLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 1),
    _TrunkRTCLocalSlot_Type()
)
trunkRTCLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLocalSlot.setStatus("mandatory")
_TrunkRTCLocalPort_Type = Integer32
_TrunkRTCLocalPort_Object = MibTableColumn
trunkRTCLocalPort = _TrunkRTCLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 2),
    _TrunkRTCLocalPort_Type()
)
trunkRTCLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLocalPort.setStatus("mandatory")
_TrunkRTCBipolarViolations_Type = Counter32
_TrunkRTCBipolarViolations_Object = MibTableColumn
trunkRTCBipolarViolations = _TrunkRTCBipolarViolations_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 4),
    _TrunkRTCBipolarViolations_Type()
)
trunkRTCBipolarViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBipolarViolations.setStatus("mandatory")
_TrunkRTCFrameSlips_Type = Counter32
_TrunkRTCFrameSlips_Object = MibTableColumn
trunkRTCFrameSlips = _TrunkRTCFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 5),
    _TrunkRTCFrameSlips_Type()
)
trunkRTCFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCFrameSlips.setStatus("mandatory")
_TrunkRTCOutOfFrames_Type = Counter32
_TrunkRTCOutOfFrames_Object = MibTableColumn
trunkRTCOutOfFrames = _TrunkRTCOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 6),
    _TrunkRTCOutOfFrames_Type()
)
trunkRTCOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCOutOfFrames.setStatus("mandatory")
_TrunkRTCLossOfSignal_Type = Counter32
_TrunkRTCLossOfSignal_Object = MibTableColumn
trunkRTCLossOfSignal = _TrunkRTCLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 7),
    _TrunkRTCLossOfSignal_Type()
)
trunkRTCLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLossOfSignal.setStatus("mandatory")
_TrunkRTCFrameBitErrors_Type = Counter32
_TrunkRTCFrameBitErrors_Object = MibTableColumn
trunkRTCFrameBitErrors = _TrunkRTCFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 8),
    _TrunkRTCFrameBitErrors_Type()
)
trunkRTCFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCFrameBitErrors.setStatus("mandatory")
_TrunkRTCCrcErrors_Type = Counter32
_TrunkRTCCrcErrors_Object = MibTableColumn
trunkRTCCrcErrors = _TrunkRTCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 9),
    _TrunkRTCCrcErrors_Type()
)
trunkRTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCCrcErrors.setStatus("mandatory")
_TrunkRTCPktOutOfFrames_Type = Counter32
_TrunkRTCPktOutOfFrames_Object = MibTableColumn
trunkRTCPktOutOfFrames = _TrunkRTCPktOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 10),
    _TrunkRTCPktOutOfFrames_Type()
)
trunkRTCPktOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktOutOfFrames.setStatus("mandatory")
_TrunkRTCPktCrcErrors_Type = Counter32
_TrunkRTCPktCrcErrors_Object = MibTableColumn
trunkRTCPktCrcErrors = _TrunkRTCPktCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 11),
    _TrunkRTCPktCrcErrors_Type()
)
trunkRTCPktCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktCrcErrors.setStatus("mandatory")
_TrunkRTCBadClockErrors_Type = Counter32
_TrunkRTCBadClockErrors_Object = MibTableColumn
trunkRTCBadClockErrors = _TrunkRTCBadClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 12),
    _TrunkRTCBadClockErrors_Type()
)
trunkRTCBadClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBadClockErrors.setStatus("mandatory")
_TrunkRTCVoicePktsDropped_Type = Counter32
_TrunkRTCVoicePktsDropped_Object = MibTableColumn
trunkRTCVoicePktsDropped = _TrunkRTCVoicePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 13),
    _TrunkRTCVoicePktsDropped_Type()
)
trunkRTCVoicePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoicePktsDropped.setStatus("mandatory")
_TrunkRTCTimeStampedPktsDropped_Type = Counter32
_TrunkRTCTimeStampedPktsDropped_Object = MibTableColumn
trunkRTCTimeStampedPktsDropped = _TrunkRTCTimeStampedPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 14),
    _TrunkRTCTimeStampedPktsDropped_Type()
)
trunkRTCTimeStampedPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampedPktsDropped.setStatus("mandatory")
_TrunkRTCNonTimeStampedPktsDropped_Type = Counter32
_TrunkRTCNonTimeStampedPktsDropped_Object = MibTableColumn
trunkRTCNonTimeStampedPktsDropped = _TrunkRTCNonTimeStampedPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 15),
    _TrunkRTCNonTimeStampedPktsDropped_Type()
)
trunkRTCNonTimeStampedPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampedPktsDropped.setStatus("mandatory")
_TrunkRTCHighPriorityPktsDropped_Type = Counter32
_TrunkRTCHighPriorityPktsDropped_Object = MibTableColumn
trunkRTCHighPriorityPktsDropped = _TrunkRTCHighPriorityPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 16),
    _TrunkRTCHighPriorityPktsDropped_Type()
)
trunkRTCHighPriorityPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityPktsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataPktsDropped_Type = Counter32
_TrunkRTCBurstyDataPktsDropped_Object = MibTableColumn
trunkRTCBurstyDataPktsDropped = _TrunkRTCBurstyDataPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 17),
    _TrunkRTCBurstyDataPktsDropped_Type()
)
trunkRTCBurstyDataPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataPktsDropped.setStatus("mandatory")
_TrunkRTCMulticastPktsDropped_Type = Counter32
_TrunkRTCMulticastPktsDropped_Object = MibTableColumn
trunkRTCMulticastPktsDropped = _TrunkRTCMulticastPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 18),
    _TrunkRTCMulticastPktsDropped_Type()
)
trunkRTCMulticastPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCMulticastPktsDropped.setStatus("mandatory")
_TrunkRTCVoicePktsXmitted_Type = Counter32
_TrunkRTCVoicePktsXmitted_Object = MibTableColumn
trunkRTCVoicePktsXmitted = _TrunkRTCVoicePktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 19),
    _TrunkRTCVoicePktsXmitted_Type()
)
trunkRTCVoicePktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoicePktsXmitted.setStatus("mandatory")
_TrunkRTCTimeStampedPktsXmitted_Type = Counter32
_TrunkRTCTimeStampedPktsXmitted_Object = MibTableColumn
trunkRTCTimeStampedPktsXmitted = _TrunkRTCTimeStampedPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 20),
    _TrunkRTCTimeStampedPktsXmitted_Type()
)
trunkRTCTimeStampedPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampedPktsXmitted.setStatus("mandatory")
_TrunkRTCNonTimeStampedPktsXmitted_Type = Counter32
_TrunkRTCNonTimeStampedPktsXmitted_Object = MibTableColumn
trunkRTCNonTimeStampedPktsXmitted = _TrunkRTCNonTimeStampedPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 21),
    _TrunkRTCNonTimeStampedPktsXmitted_Type()
)
trunkRTCNonTimeStampedPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampedPktsXmitted.setStatus("mandatory")
_TrunkRTCHighPriorityPktsXmitted_Type = Counter32
_TrunkRTCHighPriorityPktsXmitted_Object = MibTableColumn
trunkRTCHighPriorityPktsXmitted = _TrunkRTCHighPriorityPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 22),
    _TrunkRTCHighPriorityPktsXmitted_Type()
)
trunkRTCHighPriorityPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityPktsXmitted.setStatus("mandatory")
_TrunkRTCBurstyDataPktsXmitted_Type = Counter32
_TrunkRTCBurstyDataPktsXmitted_Object = MibTableColumn
trunkRTCBurstyDataPktsXmitted = _TrunkRTCBurstyDataPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 23),
    _TrunkRTCBurstyDataPktsXmitted_Type()
)
trunkRTCBurstyDataPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataPktsXmitted.setStatus("mandatory")
_TrunkRTCMulticastPktsXmitted_Type = Counter32
_TrunkRTCMulticastPktsXmitted_Object = MibTableColumn
trunkRTCMulticastPktsXmitted = _TrunkRTCMulticastPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 24),
    _TrunkRTCMulticastPktsXmitted_Type()
)
trunkRTCMulticastPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCMulticastPktsXmitted.setStatus("mandatory")
_TrunkRTCPktsXmitted_Type = Counter32
_TrunkRTCPktsXmitted_Object = MibTableColumn
trunkRTCPktsXmitted = _TrunkRTCPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 25),
    _TrunkRTCPktsXmitted_Type()
)
trunkRTCPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktsXmitted.setStatus("mandatory")
_TrunkRTCTxBurstyDataAClpPktsDropped_Type = Counter32
_TrunkRTCTxBurstyDataAClpPktsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataAClpPktsDropped = _TrunkRTCTxBurstyDataAClpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 26),
    _TrunkRTCTxBurstyDataAClpPktsDropped_Type()
)
trunkRTCTxBurstyDataAClpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataAClpPktsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBClpPktsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBClpPktsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBClpPktsDropped = _TrunkRTCTxBurstyDataBClpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 27),
    _TrunkRTCTxBurstyDataBClpPktsDropped_Type()
)
trunkRTCTxBurstyDataBClpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBClpPktsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataAEfcnPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAEfcnPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAEfcnPktsTx2Line = _TrunkRTCBurstyDataAEfcnPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 28),
    _TrunkRTCBurstyDataAEfcnPktsTx2Line_Type()
)
trunkRTCBurstyDataAEfcnPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAEfcnPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBEfcnPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBEfcnPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBEfcnPktsTx2Line = _TrunkRTCBurstyDataBEfcnPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 29),
    _TrunkRTCBurstyDataBEfcnPktsTx2Line_Type()
)
trunkRTCBurstyDataBEfcnPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBEfcnPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataAClpPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAClpPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAClpPktsTx2Line = _TrunkRTCBurstyDataAClpPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 30),
    _TrunkRTCBurstyDataAClpPktsTx2Line_Type()
)
trunkRTCBurstyDataAClpPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAClpPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBClpPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBClpPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBClpPktsTx2Line = _TrunkRTCBurstyDataBClpPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 31),
    _TrunkRTCBurstyDataBClpPktsTx2Line_Type()
)
trunkRTCBurstyDataBClpPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBClpPktsTx2Line.setStatus("mandatory")
_TrunkRTCAtmCellHeaderHecErrors_Type = Counter32
_TrunkRTCAtmCellHeaderHecErrors_Object = MibTableColumn
trunkRTCAtmCellHeaderHecErrors = _TrunkRTCAtmCellHeaderHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 32),
    _TrunkRTCAtmCellHeaderHecErrors_Type()
)
trunkRTCAtmCellHeaderHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCAtmCellHeaderHecErrors.setStatus("mandatory")
_TrunkRTCTxVoiceCellsDropped_Type = Counter32
_TrunkRTCTxVoiceCellsDropped_Object = MibTableColumn
trunkRTCTxVoiceCellsDropped = _TrunkRTCTxVoiceCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 33),
    _TrunkRTCTxVoiceCellsDropped_Type()
)
trunkRTCTxVoiceCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxVoiceCellsDropped.setStatus("mandatory")
_TrunkRTCTxTimeStampCellsDropped_Type = Counter32
_TrunkRTCTxTimeStampCellsDropped_Object = MibTableColumn
trunkRTCTxTimeStampCellsDropped = _TrunkRTCTxTimeStampCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 34),
    _TrunkRTCTxTimeStampCellsDropped_Type()
)
trunkRTCTxTimeStampCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxTimeStampCellsDropped.setStatus("mandatory")
_TrunkRTCTxNonTStampCellsDropped_Type = Counter32
_TrunkRTCTxNonTStampCellsDropped_Object = MibTableColumn
trunkRTCTxNonTStampCellsDropped = _TrunkRTCTxNonTStampCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 35),
    _TrunkRTCTxNonTStampCellsDropped_Type()
)
trunkRTCTxNonTStampCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxNonTStampCellsDropped.setStatus("mandatory")
_TrunkRTCTxHighPriorityCellsDropped_Type = Counter32
_TrunkRTCTxHighPriorityCellsDropped_Object = MibTableColumn
trunkRTCTxHighPriorityCellsDropped = _TrunkRTCTxHighPriorityCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 36),
    _TrunkRTCTxHighPriorityCellsDropped_Type()
)
trunkRTCTxHighPriorityCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxHighPriorityCellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataACellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataACellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataACellsDropped = _TrunkRTCTxBurstyDataACellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 37),
    _TrunkRTCTxBurstyDataACellsDropped_Type()
)
trunkRTCTxBurstyDataACellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataACellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBCellsDropped = _TrunkRTCTxBurstyDataBCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 38),
    _TrunkRTCTxBurstyDataBCellsDropped_Type()
)
trunkRTCTxBurstyDataBCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBCellsDropped.setStatus("mandatory")
_TrunkRTCVoiceCellsTx2Line_Type = Counter32
_TrunkRTCVoiceCellsTx2Line_Object = MibTableColumn
trunkRTCVoiceCellsTx2Line = _TrunkRTCVoiceCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 39),
    _TrunkRTCVoiceCellsTx2Line_Type()
)
trunkRTCVoiceCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoiceCellsTx2Line.setStatus("mandatory")
_TrunkRTCTimeStampCellsTx2Line_Type = Counter32
_TrunkRTCTimeStampCellsTx2Line_Object = MibTableColumn
trunkRTCTimeStampCellsTx2Line = _TrunkRTCTimeStampCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 40),
    _TrunkRTCTimeStampCellsTx2Line_Type()
)
trunkRTCTimeStampCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampCellsTx2Line.setStatus("mandatory")
_TrunkRTCNonTimeStampCellsTx2Line_Type = Counter32
_TrunkRTCNonTimeStampCellsTx2Line_Object = MibTableColumn
trunkRTCNonTimeStampCellsTx2Line = _TrunkRTCNonTimeStampCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 41),
    _TrunkRTCNonTimeStampCellsTx2Line_Type()
)
trunkRTCNonTimeStampCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampCellsTx2Line.setStatus("mandatory")
_TrunkRTCHighPriorityCellsTx2Line_Type = Counter32
_TrunkRTCHighPriorityCellsTx2Line_Object = MibTableColumn
trunkRTCHighPriorityCellsTx2Line = _TrunkRTCHighPriorityCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 42),
    _TrunkRTCHighPriorityCellsTx2Line_Type()
)
trunkRTCHighPriorityCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityCellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataACellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataACellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataACellsTx2Line = _TrunkRTCBurstyDataACellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 43),
    _TrunkRTCBurstyDataACellsTx2Line_Type()
)
trunkRTCBurstyDataACellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataACellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBCellsTx2Line = _TrunkRTCBurstyDataBCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 44),
    _TrunkRTCBurstyDataBCellsTx2Line_Type()
)
trunkRTCBurstyDataBCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBCellsTx2Line.setStatus("mandatory")
_TrunkRTCTotalCellsTx2Line_Type = Counter32
_TrunkRTCTotalCellsTx2Line_Object = MibTableColumn
trunkRTCTotalCellsTx2Line = _TrunkRTCTotalCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 45),
    _TrunkRTCTotalCellsTx2Line_Type()
)
trunkRTCTotalCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTotalCellsTx2Line.setStatus("mandatory")
_TrunkRTCTxBurstyDataAClpCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataAClpCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataAClpCellsDropped = _TrunkRTCTxBurstyDataAClpCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 46),
    _TrunkRTCTxBurstyDataAClpCellsDropped_Type()
)
trunkRTCTxBurstyDataAClpCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataAClpCellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBClpCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBClpCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBClpCellsDropped = _TrunkRTCTxBurstyDataBClpCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 47),
    _TrunkRTCTxBurstyDataBClpCellsDropped_Type()
)
trunkRTCTxBurstyDataBClpCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBClpCellsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataAEfcnCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAEfcnCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAEfcnCellsTx2Line = _TrunkRTCBurstyDataAEfcnCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 48),
    _TrunkRTCBurstyDataAEfcnCellsTx2Line_Type()
)
trunkRTCBurstyDataAEfcnCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAEfcnCellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBEfcnCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBEfcnCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBEfcnCellsTx2Line = _TrunkRTCBurstyDataBEfcnCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 49),
    _TrunkRTCBurstyDataBEfcnCellsTx2Line_Type()
)
trunkRTCBurstyDataBEfcnCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBEfcnCellsTx2Line.setStatus("mandatory")
_TrunkRTCPlcpOutOfFrames_Type = Counter32
_TrunkRTCPlcpOutOfFrames_Object = MibTableColumn
trunkRTCPlcpOutOfFrames = _TrunkRTCPlcpOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 50),
    _TrunkRTCPlcpOutOfFrames_Type()
)
trunkRTCPlcpOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPlcpOutOfFrames.setStatus("mandatory")
_ConnSvc_ObjectIdentity = ObjectIdentity
connSvc = _ConnSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 3)
)
_ConnMibUpTime_Type = TimeTicks
_ConnMibUpTime_Object = MibScalar
connMibUpTime = _ConnMibUpTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 1),
    _ConnMibUpTime_Type()
)
connMibUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMibUpTime.setStatus("mandatory")


class _ConnAvailIndex_Type(Integer32):
    """Custom type connAvailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ConnAvailIndex_Type.__name__ = "Integer32"
_ConnAvailIndex_Object = MibScalar
connAvailIndex = _ConnAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 2),
    _ConnAvailIndex_Type()
)
connAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connAvailIndex.setStatus("mandatory")
_ConnectionTable_Object = MibTable
connectionTable = _ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3)
)
if mibBuilder.loadTexts:
    connectionTable.setStatus("mandatory")
_ConnectionEntry_Object = MibTableRow
connectionEntry = _ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1)
)
connectionEntry.setIndexNames(
    (0, "STRATACOM-MIB", "connectionIndex"),
)
if mibBuilder.loadTexts:
    connectionEntry.setStatus("mandatory")


class _ConnectionIndex_Type(Integer32):
    """Custom type connectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnectionIndex_Type.__name__ = "Integer32"
_ConnectionIndex_Object = MibTableColumn
connectionIndex = _ConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 1),
    _ConnectionIndex_Type()
)
connectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionIndex.setStatus("mandatory")
_ConnectionLocalEndPt_Type = ObjectIdentifier
_ConnectionLocalEndPt_Object = MibTableColumn
connectionLocalEndPt = _ConnectionLocalEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 2),
    _ConnectionLocalEndPt_Type()
)
connectionLocalEndPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLocalEndPt.setStatus("mandatory")
_ConnectionRemoteEndPt_Type = ObjectIdentifier
_ConnectionRemoteEndPt_Object = MibTableColumn
connectionRemoteEndPt = _ConnectionRemoteEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 3),
    _ConnectionRemoteEndPt_Type()
)
connectionRemoteEndPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRemoteEndPt.setStatus("mandatory")


class _ConnectionAdminStatus_Type(Integer32):
    """Custom type connectionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("testing", 3))
    )


_ConnectionAdminStatus_Type.__name__ = "Integer32"
_ConnectionAdminStatus_Object = MibTableColumn
connectionAdminStatus = _ConnectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 4),
    _ConnectionAdminStatus_Type()
)
connectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionAdminStatus.setStatus("mandatory")


class _ConnectionOpStatus_Type(Integer32):
    """Custom type connectionOpStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1),
          ("incomplete", 5))
    )


_ConnectionOpStatus_Type.__name__ = "Integer32"
_ConnectionOpStatus_Object = MibTableColumn
connectionOpStatus = _ConnectionOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 5),
    _ConnectionOpStatus_Type()
)
connectionOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionOpStatus.setStatus("mandatory")


class _ConnectionRowStatus_Type(Integer32):
    """Custom type connectionRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_ConnectionRowStatus_Type.__name__ = "Integer32"
_ConnectionRowStatus_Object = MibTableColumn
connectionRowStatus = _ConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 6),
    _ConnectionRowStatus_Type()
)
connectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRowStatus.setStatus("mandatory")


class _ConnectionTrkAvoidType_Type(Integer32):
    """Custom type connectionTrkAvoidType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_ConnectionTrkAvoidType_Type.__name__ = "Integer32"
_ConnectionTrkAvoidType_Object = MibTableColumn
connectionTrkAvoidType = _ConnectionTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 7),
    _ConnectionTrkAvoidType_Type()
)
connectionTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionTrkAvoidType.setStatus("mandatory")


class _ConnectionTrkAvoidZCS_Type(Integer32):
    """Custom type connectionTrkAvoidZCS based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnectionTrkAvoidZCS_Type.__name__ = "Integer32"
_ConnectionTrkAvoidZCS_Object = MibTableColumn
connectionTrkAvoidZCS = _ConnectionTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 8),
    _ConnectionTrkAvoidZCS_Type()
)
connectionTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionTrkAvoidZCS.setStatus("mandatory")


class _ConnectionForesight_Type(Integer32):
    """Custom type connectionForesight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ConnectionForesight_Type.__name__ = "Integer32"
_ConnectionForesight_Object = MibTableColumn
connectionForesight = _ConnectionForesight_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 9),
    _ConnectionForesight_Type()
)
connectionForesight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionForesight.setStatus("mandatory")


class _ConnectionClassOfService_Type(Integer32):
    """Custom type connectionClassOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ConnectionClassOfService_Type.__name__ = "Integer32"
_ConnectionClassOfService_Object = MibTableColumn
connectionClassOfService = _ConnectionClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 10),
    _ConnectionClassOfService_Type()
)
connectionClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionClassOfService.setStatus("mandatory")


class _ConnectionCurrRouteDesc_Type(DisplayString):
    """Custom type connectionCurrRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConnectionCurrRouteDesc_Type.__name__ = "DisplayString"
_ConnectionCurrRouteDesc_Object = MibTableColumn
connectionCurrRouteDesc = _ConnectionCurrRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 11),
    _ConnectionCurrRouteDesc_Type()
)
connectionCurrRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionCurrRouteDesc.setStatus("mandatory")


class _ConnectionPrefRouteDesc_Type(DisplayString):
    """Custom type connectionPrefRouteDesc based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConnectionPrefRouteDesc_Type.__name__ = "DisplayString"
_ConnectionPrefRouteDesc_Object = MibTableColumn
connectionPrefRouteDesc = _ConnectionPrefRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 12),
    _ConnectionPrefRouteDesc_Type()
)
connectionPrefRouteDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionPrefRouteDesc.setStatus("mandatory")


class _ConnRouteMaster_Type(DisplayString):
    """Custom type connRouteMaster based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ConnRouteMaster_Type.__name__ = "DisplayString"
_ConnRouteMaster_Object = MibTableColumn
connRouteMaster = _ConnRouteMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 13),
    _ConnRouteMaster_Type()
)
connRouteMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRouteMaster.setStatus("mandatory")


class _ConnectionLocOSpacePkts_Type(Integer32):
    """Custom type connectionLocOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConnectionLocOSpacePkts_Type.__name__ = "Integer32"
_ConnectionLocOSpacePkts_Object = MibTableColumn
connectionLocOSpacePkts = _ConnectionLocOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 14),
    _ConnectionLocOSpacePkts_Type()
)
connectionLocOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLocOSpacePkts.setStatus("mandatory")


class _ConnectionLocOSpaceBdaCmax_Type(Integer32):
    """Custom type connectionLocOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_ConnectionLocOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnectionLocOSpaceBdaCmax_Object = MibTableColumn
connectionLocOSpaceBdaCmax = _ConnectionLocOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 15),
    _ConnectionLocOSpaceBdaCmax_Type()
)
connectionLocOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLocOSpaceBdaCmax.setStatus("mandatory")


class _ConnectionLocOSpaceBdbCmax_Type(Integer32):
    """Custom type connectionLocOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_ConnectionLocOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnectionLocOSpaceBdbCmax_Object = MibTableColumn
connectionLocOSpaceBdbCmax = _ConnectionLocOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 16),
    _ConnectionLocOSpaceBdbCmax_Type()
)
connectionLocOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLocOSpaceBdbCmax.setStatus("mandatory")


class _ConnectionRemOSpacePkts_Type(Integer32):
    """Custom type connectionRemOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ConnectionRemOSpacePkts_Type.__name__ = "Integer32"
_ConnectionRemOSpacePkts_Object = MibTableColumn
connectionRemOSpacePkts = _ConnectionRemOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 17),
    _ConnectionRemOSpacePkts_Type()
)
connectionRemOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRemOSpacePkts.setStatus("mandatory")


class _ConnectionRemOSpaceBdaCmax_Type(Integer32):
    """Custom type connectionRemOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_ConnectionRemOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnectionRemOSpaceBdaCmax_Object = MibTableColumn
connectionRemOSpaceBdaCmax = _ConnectionRemOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 18),
    _ConnectionRemOSpaceBdaCmax_Type()
)
connectionRemOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRemOSpaceBdaCmax.setStatus("mandatory")


class _ConnectionRemOSpaceBdbCmax_Type(Integer32):
    """Custom type connectionRemOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_ConnectionRemOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnectionRemOSpaceBdbCmax_Object = MibTableColumn
connectionRemOSpaceBdbCmax = _ConnectionRemOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 19),
    _ConnectionRemOSpaceBdbCmax_Type()
)
connectionRemOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRemOSpaceBdbCmax.setStatus("mandatory")


class _ConnectionTestType_Type(Integer32):
    """Custom type connectionTestType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("continuity", 1),
          ("delay", 2),
          ("none", 255))
    )


_ConnectionTestType_Type.__name__ = "Integer32"
_ConnectionTestType_Object = MibTableColumn
connectionTestType = _ConnectionTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 20),
    _ConnectionTestType_Type()
)
connectionTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionTestType.setStatus("mandatory")
_ConnectionTestResult_Type = Integer32
_ConnectionTestResult_Object = MibTableColumn
connectionTestResult = _ConnectionTestResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 21),
    _ConnectionTestResult_Type()
)
connectionTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTestResult.setStatus("mandatory")


class _ConnectionAbitStatus_Type(Integer32):
    """Custom type connectionAbitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("fail", 2))
    )


_ConnectionAbitStatus_Type.__name__ = "Integer32"
_ConnectionAbitStatus_Object = MibTableColumn
connectionAbitStatus = _ConnectionAbitStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 22),
    _ConnectionAbitStatus_Type()
)
connectionAbitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionAbitStatus.setStatus("mandatory")


class _ConnectionType_Type(Integer32):
    """Custom type connectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              20)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("atm-fr", 3),
          ("fr", 1),
          ("unknown", 20))
    )


_ConnectionType_Type.__name__ = "Integer32"
_ConnectionType_Object = MibTableColumn
connectionType = _ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 23),
    _ConnectionType_Type()
)
connectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionType.setStatus("mandatory")
_ConnectionLocalStr_Type = DisplayString
_ConnectionLocalStr_Object = MibTableColumn
connectionLocalStr = _ConnectionLocalStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 24),
    _ConnectionLocalStr_Type()
)
connectionLocalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLocalStr.setStatus("mandatory")
_ConnectionRemoteStr_Type = DisplayString
_ConnectionRemoteStr_Object = MibTableColumn
connectionRemoteStr = _ConnectionRemoteStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 3, 1, 25),
    _ConnectionRemoteStr_Type()
)
connectionRemoteStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionRemoteStr.setStatus("mandatory")
_FrEndPtTable_Object = MibTable
frEndPtTable = _FrEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4)
)
if mibBuilder.loadTexts:
    frEndPtTable.setStatus("mandatory")
_FrEndPtEntry_Object = MibTableRow
frEndPtEntry = _FrEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1)
)
frEndPtEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndPtNodeName"),
    (0, "STRATACOM-MIB", "frEndPtIfShelf"),
    (0, "STRATACOM-MIB", "frEndPtSlot"),
    (0, "STRATACOM-MIB", "frEndPtLine"),
    (0, "STRATACOM-MIB", "frEndPtPort"),
    (0, "STRATACOM-MIB", "frEndPtDlci"),
)
if mibBuilder.loadTexts:
    frEndPtEntry.setStatus("mandatory")


class _FrEndPtNodeName_Type(DisplayString):
    """Custom type frEndPtNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrEndPtNodeName_Type.__name__ = "DisplayString"
_FrEndPtNodeName_Object = MibTableColumn
frEndPtNodeName = _FrEndPtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 1),
    _FrEndPtNodeName_Type()
)
frEndPtNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtNodeName.setStatus("mandatory")


class _FrEndPtIfShelf_Type(DisplayString):
    """Custom type frEndPtIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FrEndPtIfShelf_Type.__name__ = "DisplayString"
_FrEndPtIfShelf_Object = MibTableColumn
frEndPtIfShelf = _FrEndPtIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 2),
    _FrEndPtIfShelf_Type()
)
frEndPtIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtIfShelf.setStatus("mandatory")


class _FrEndPtSlot_Type(Integer32):
    """Custom type frEndPtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrEndPtSlot_Type.__name__ = "Integer32"
_FrEndPtSlot_Object = MibTableColumn
frEndPtSlot = _FrEndPtSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 3),
    _FrEndPtSlot_Type()
)
frEndPtSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtSlot.setStatus("mandatory")


class _FrEndPtLine_Type(Integer32):
    """Custom type frEndPtLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FrEndPtLine_Type.__name__ = "Integer32"
_FrEndPtLine_Object = MibTableColumn
frEndPtLine = _FrEndPtLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 4),
    _FrEndPtLine_Type()
)
frEndPtLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtLine.setStatus("mandatory")


class _FrEndPtPort_Type(Integer32):
    """Custom type frEndPtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrEndPtPort_Type.__name__ = "Integer32"
_FrEndPtPort_Object = MibTableColumn
frEndPtPort = _FrEndPtPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 5),
    _FrEndPtPort_Type()
)
frEndPtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtPort.setStatus("mandatory")


class _FrEndPtDlci_Type(Integer32):
    """Custom type frEndPtDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtDlci_Type.__name__ = "Integer32"
_FrEndPtDlci_Object = MibTableColumn
frEndPtDlci = _FrEndPtDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 6),
    _FrEndPtDlci_Type()
)
frEndPtDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtDlci.setStatus("mandatory")


class _FrEndPtConnIndex_Type(Integer32):
    """Custom type frEndPtConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrEndPtConnIndex_Type.__name__ = "Integer32"
_FrEndPtConnIndex_Object = MibTableColumn
frEndPtConnIndex = _FrEndPtConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 7),
    _FrEndPtConnIndex_Type()
)
frEndPtConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPtConnIndex.setStatus("mandatory")


class _FrEndPtAdminStatus_Type(Integer32):
    """Custom type frEndPtAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("testing", 3))
    )


_FrEndPtAdminStatus_Type.__name__ = "Integer32"
_FrEndPtAdminStatus_Object = MibTableColumn
frEndPtAdminStatus = _FrEndPtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 8),
    _FrEndPtAdminStatus_Type()
)
frEndPtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtAdminStatus.setStatus("mandatory")


class _FrEndPtOpStatus_Type(Integer32):
    """Custom type frEndPtOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 16),
          ("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_FrEndPtOpStatus_Type.__name__ = "Integer32"
_FrEndPtOpStatus_Object = MibTableColumn
frEndPtOpStatus = _FrEndPtOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 9),
    _FrEndPtOpStatus_Type()
)
frEndPtOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPtOpStatus.setStatus("mandatory")


class _FrEndPtRowStatus_Type(Integer32):
    """Custom type frEndPtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_FrEndPtRowStatus_Type.__name__ = "Integer32"
_FrEndPtRowStatus_Object = MibTableColumn
frEndPtRowStatus = _FrEndPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 10),
    _FrEndPtRowStatus_Type()
)
frEndPtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtRowStatus.setStatus("mandatory")


class _FrEndPtMIR_Type(Integer32):
    """Custom type frEndPtMIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndPtMIR_Type.__name__ = "Integer32"
_FrEndPtMIR_Object = MibTableColumn
frEndPtMIR = _FrEndPtMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 11),
    _FrEndPtMIR_Type()
)
frEndPtMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtMIR.setStatus("mandatory")


class _FrEndPtCIR_Type(Integer32):
    """Custom type frEndPtCIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndPtCIR_Type.__name__ = "Integer32"
_FrEndPtCIR_Object = MibTableColumn
frEndPtCIR = _FrEndPtCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 12),
    _FrEndPtCIR_Type()
)
frEndPtCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtCIR.setStatus("mandatory")


class _FrEndPtBc_Type(Integer32):
    """Custom type frEndPtBc based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndPtBc_Type.__name__ = "Integer32"
_FrEndPtBc_Object = MibTableColumn
frEndPtBc = _FrEndPtBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 13),
    _FrEndPtBc_Type()
)
frEndPtBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtBc.setStatus("mandatory")


class _FrEndPtBe_Type(Integer32):
    """Custom type frEndPtBe based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtBe_Type.__name__ = "Integer32"
_FrEndPtBe_Object = MibTableColumn
frEndPtBe = _FrEndPtBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 14),
    _FrEndPtBe_Type()
)
frEndPtBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtBe.setStatus("mandatory")


class _FrEndPtVcQSize_Type(Integer32):
    """Custom type frEndPtVcQSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndPtVcQSize_Type.__name__ = "Integer32"
_FrEndPtVcQSize_Object = MibTableColumn
frEndPtVcQSize = _FrEndPtVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 15),
    _FrEndPtVcQSize_Type()
)
frEndPtVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtVcQSize.setStatus("mandatory")


class _FrEndPtPIR_Type(Integer32):
    """Custom type frEndPtPIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndPtPIR_Type.__name__ = "Integer32"
_FrEndPtPIR_Object = MibTableColumn
frEndPtPIR = _FrEndPtPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 16),
    _FrEndPtPIR_Type()
)
frEndPtPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtPIR.setStatus("mandatory")


class _FrEndPtCMAX_Type(Integer32):
    """Custom type frEndPtCMAX based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrEndPtCMAX_Type.__name__ = "Integer32"
_FrEndPtCMAX_Object = MibTableColumn
frEndPtCMAX = _FrEndPtCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 17),
    _FrEndPtCMAX_Type()
)
frEndPtCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtCMAX.setStatus("mandatory")


class _FrEndPtEcnQSize_Type(Integer32):
    """Custom type frEndPtEcnQSize based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtEcnQSize_Type.__name__ = "Integer32"
_FrEndPtEcnQSize_Object = MibTableColumn
frEndPtEcnQSize = _FrEndPtEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 18),
    _FrEndPtEcnQSize_Type()
)
frEndPtEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtEcnQSize.setStatus("mandatory")


class _FrEndPtQIR_Type(Integer32):
    """Custom type frEndPtQIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndPtQIR_Type.__name__ = "Integer32"
_FrEndPtQIR_Object = MibTableColumn
frEndPtQIR = _FrEndPtQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 19),
    _FrEndPtQIR_Type()
)
frEndPtQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtQIR.setStatus("mandatory")


class _FrEndPtPercUtil_Type(Integer32):
    """Custom type frEndPtPercUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndPtPercUtil_Type.__name__ = "Integer32"
_FrEndPtPercUtil_Object = MibTableColumn
frEndPtPercUtil = _FrEndPtPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 20),
    _FrEndPtPercUtil_Type()
)
frEndPtPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtPercUtil.setStatus("mandatory")


class _FrEndPtPriority_Type(Integer32):
    """Custom type frEndPtPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_FrEndPtPriority_Type.__name__ = "Integer32"
_FrEndPtPriority_Object = MibTableColumn
frEndPtPriority = _FrEndPtPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 21),
    _FrEndPtPriority_Type()
)
frEndPtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtPriority.setStatus("mandatory")


class _FrEndPtInitialBurstSize_Type(Integer32):
    """Custom type frEndPtInitialBurstSize based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtInitialBurstSize_Type.__name__ = "Integer32"
_FrEndPtInitialBurstSize_Object = MibTableColumn
frEndPtInitialBurstSize = _FrEndPtInitialBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 22),
    _FrEndPtInitialBurstSize_Type()
)
frEndPtInitialBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtInitialBurstSize.setStatus("mandatory")


class _FrEndPtDeTagging_Type(Integer32):
    """Custom type frEndPtDeTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrEndPtDeTagging_Type.__name__ = "Integer32"
_FrEndPtDeTagging_Object = MibTableColumn
frEndPtDeTagging = _FrEndPtDeTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 23),
    _FrEndPtDeTagging_Type()
)
frEndPtDeTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtDeTagging.setStatus("mandatory")


class _FrEndPtIngressDeThreshold_Type(Integer32):
    """Custom type frEndPtIngressDeThreshold based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtIngressDeThreshold_Type.__name__ = "Integer32"
_FrEndPtIngressDeThreshold_Object = MibTableColumn
frEndPtIngressDeThreshold = _FrEndPtIngressDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 24),
    _FrEndPtIngressDeThreshold_Type()
)
frEndPtIngressDeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtIngressDeThreshold.setStatus("mandatory")


class _FrEndPtEgressQDepth_Type(Integer32):
    """Custom type frEndPtEgressQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtEgressQDepth_Type.__name__ = "Integer32"
_FrEndPtEgressQDepth_Object = MibTableColumn
frEndPtEgressQDepth = _FrEndPtEgressQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 25),
    _FrEndPtEgressQDepth_Type()
)
frEndPtEgressQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtEgressQDepth.setStatus("mandatory")


class _FrEndPtEgressDeThreshold_Type(Integer32):
    """Custom type frEndPtEgressDeThreshold based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtEgressDeThreshold_Type.__name__ = "Integer32"
_FrEndPtEgressDeThreshold_Object = MibTableColumn
frEndPtEgressDeThreshold = _FrEndPtEgressDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 26),
    _FrEndPtEgressDeThreshold_Type()
)
frEndPtEgressDeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtEgressDeThreshold.setStatus("mandatory")


class _FrEndPtEgressEcnThreshold_Type(Integer32):
    """Custom type frEndPtEgressEcnThreshold based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtEgressEcnThreshold_Type.__name__ = "Integer32"
_FrEndPtEgressEcnThreshold_Object = MibTableColumn
frEndPtEgressEcnThreshold = _FrEndPtEgressEcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 27),
    _FrEndPtEgressEcnThreshold_Type()
)
frEndPtEgressEcnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtEgressEcnThreshold.setStatus("mandatory")


class _FrEndPtEgressQSelect_Type(Integer32):
    """Custom type frEndPtEgressQSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_FrEndPtEgressQSelect_Type.__name__ = "Integer32"
_FrEndPtEgressQSelect_Object = MibTableColumn
frEndPtEgressQSelect = _FrEndPtEgressQSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 28),
    _FrEndPtEgressQSelect_Type()
)
frEndPtEgressQSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtEgressQSelect.setStatus("mandatory")


class _FrEndPtLpbkState_Type(Integer32):
    """Custom type frEndPtLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPtLpbkState_Type.__name__ = "Integer32"
_FrEndPtLpbkState_Object = MibTableColumn
frEndPtLpbkState = _FrEndPtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 29),
    _FrEndPtLpbkState_Type()
)
frEndPtLpbkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPtLpbkState.setStatus("mandatory")


class _FrEndPtType_Type(Integer32):
    """Custom type frEndPtType based on Integer32"""
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
        *(("ait", 3),
          ("cdpSdpCard", 1),
          ("fr", 2),
          ("frsm", 4))
    )


_FrEndPtType_Type.__name__ = "Integer32"
_FrEndPtType_Object = MibTableColumn
frEndPtType = _FrEndPtType_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 30),
    _FrEndPtType_Type()
)
frEndPtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPtType.setStatus("mandatory")


class _FrEndPtchanType_Type(Integer32):
    """Custom type frEndPtchanType based on Integer32"""
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
        *(("frFUNI", 4),
          ("frNIW", 1),
          ("frSIW-translate", 3),
          ("frSIW-transparent", 2))
    )


_FrEndPtchanType_Type.__name__ = "Integer32"
_FrEndPtchanType_Object = MibTableColumn
frEndPtchanType = _FrEndPtchanType_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 31),
    _FrEndPtchanType_Type()
)
frEndPtchanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtchanType.setStatus("mandatory")


class _FrEndPtchanFECNconfig_Type(Integer32):
    """Custom type frEndPtchanFECNconfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapEFCI", 1),
          ("setEFCIzero", 2))
    )


_FrEndPtchanFECNconfig_Type.__name__ = "Integer32"
_FrEndPtchanFECNconfig_Object = MibTableColumn
frEndPtchanFECNconfig = _FrEndPtchanFECNconfig_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 32),
    _FrEndPtchanFECNconfig_Type()
)
frEndPtchanFECNconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtchanFECNconfig.setStatus("mandatory")


class _FrEndPtchanDEtoCLPmap_Type(Integer32):
    """Custom type frEndPtchanDEtoCLPmap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mapCLP", 1),
          ("setCLPone", 3),
          ("setCLPzero", 2))
    )


_FrEndPtchanDEtoCLPmap_Type.__name__ = "Integer32"
_FrEndPtchanDEtoCLPmap_Object = MibTableColumn
frEndPtchanDEtoCLPmap = _FrEndPtchanDEtoCLPmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 33),
    _FrEndPtchanDEtoCLPmap_Type()
)
frEndPtchanDEtoCLPmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtchanDEtoCLPmap.setStatus("mandatory")


class _FrEndPtchanCLPtoDEmap_Type(Integer32):
    """Custom type frEndPtchanCLPtoDEmap based on Integer32"""
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
        *(("ignoreCLP", 4),
          ("mapDE", 1),
          ("setDEone", 3),
          ("setDEzero", 2))
    )


_FrEndPtchanCLPtoDEmap_Type.__name__ = "Integer32"
_FrEndPtchanCLPtoDEmap_Object = MibTableColumn
frEndPtchanCLPtoDEmap = _FrEndPtchanCLPtoDEmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 4, 1, 34),
    _FrEndPtchanCLPtoDEmap_Type()
)
frEndPtchanCLPtoDEmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPtchanCLPtoDEmap.setStatus("mandatory")
_AitEndPtTable_Object = MibTable
aitEndPtTable = _AitEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5)
)
if mibBuilder.loadTexts:
    aitEndPtTable.setStatus("mandatory")
_AitEndPtEntry_Object = MibTableRow
aitEndPtEntry = _AitEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1)
)
aitEndPtEntry.setIndexNames(
    (0, "STRATACOM-MIB", "aitEndPtNodeName"),
    (0, "STRATACOM-MIB", "aitEndPtIfShelf"),
    (0, "STRATACOM-MIB", "aitEndPtSlot"),
    (0, "STRATACOM-MIB", "aitEndPtVpi"),
    (0, "STRATACOM-MIB", "aitEndPtVci"),
)
if mibBuilder.loadTexts:
    aitEndPtEntry.setStatus("mandatory")


class _AitEndPtNodeName_Type(DisplayString):
    """Custom type aitEndPtNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AitEndPtNodeName_Type.__name__ = "DisplayString"
_AitEndPtNodeName_Object = MibTableColumn
aitEndPtNodeName = _AitEndPtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 1),
    _AitEndPtNodeName_Type()
)
aitEndPtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtNodeName.setStatus("mandatory")


class _AitEndPtIfShelf_Type(DisplayString):
    """Custom type aitEndPtIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AitEndPtIfShelf_Type.__name__ = "DisplayString"
_AitEndPtIfShelf_Object = MibTableColumn
aitEndPtIfShelf = _AitEndPtIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 2),
    _AitEndPtIfShelf_Type()
)
aitEndPtIfShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtIfShelf.setStatus("mandatory")


class _AitEndPtSlot_Type(Integer32):
    """Custom type aitEndPtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AitEndPtSlot_Type.__name__ = "Integer32"
_AitEndPtSlot_Object = MibTableColumn
aitEndPtSlot = _AitEndPtSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 3),
    _AitEndPtSlot_Type()
)
aitEndPtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtSlot.setStatus("mandatory")


class _AitEndPtVpi_Type(Integer32):
    """Custom type aitEndPtVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AitEndPtVpi_Type.__name__ = "Integer32"
_AitEndPtVpi_Object = MibTableColumn
aitEndPtVpi = _AitEndPtVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 4),
    _AitEndPtVpi_Type()
)
aitEndPtVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtVpi.setStatus("mandatory")


class _AitEndPtVci_Type(Integer32):
    """Custom type aitEndPtVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AitEndPtVci_Type.__name__ = "Integer32"
_AitEndPtVci_Object = MibTableColumn
aitEndPtVci = _AitEndPtVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 5),
    _AitEndPtVci_Type()
)
aitEndPtVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtVci.setStatus("mandatory")


class _AitEndPtConnIndex_Type(Integer32):
    """Custom type aitEndPtConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AitEndPtConnIndex_Type.__name__ = "Integer32"
_AitEndPtConnIndex_Object = MibTableColumn
aitEndPtConnIndex = _AitEndPtConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 6),
    _AitEndPtConnIndex_Type()
)
aitEndPtConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtConnIndex.setStatus("mandatory")


class _AitEndPtAdminStatus_Type(Integer32):
    """Custom type aitEndPtAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("testing", 3))
    )


_AitEndPtAdminStatus_Type.__name__ = "Integer32"
_AitEndPtAdminStatus_Object = MibTableColumn
aitEndPtAdminStatus = _AitEndPtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 7),
    _AitEndPtAdminStatus_Type()
)
aitEndPtAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtAdminStatus.setStatus("mandatory")


class _AitEndPtOpStatus_Type(Integer32):
    """Custom type aitEndPtOpStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_AitEndPtOpStatus_Type.__name__ = "Integer32"
_AitEndPtOpStatus_Object = MibTableColumn
aitEndPtOpStatus = _AitEndPtOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 8),
    _AitEndPtOpStatus_Type()
)
aitEndPtOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtOpStatus.setStatus("mandatory")


class _AitEndPtMIR_Type(Integer32):
    """Custom type aitEndPtMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_AitEndPtMIR_Type.__name__ = "Integer32"
_AitEndPtMIR_Object = MibTableColumn
aitEndPtMIR = _AitEndPtMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 9),
    _AitEndPtMIR_Type()
)
aitEndPtMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtMIR.setStatus("mandatory")


class _AitEndPtCIR_Type(Integer32):
    """Custom type aitEndPtCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_AitEndPtCIR_Type.__name__ = "Integer32"
_AitEndPtCIR_Object = MibTableColumn
aitEndPtCIR = _AitEndPtCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 10),
    _AitEndPtCIR_Type()
)
aitEndPtCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtCIR.setStatus("mandatory")


class _AitEndPtVcQSize_Type(Integer32):
    """Custom type aitEndPtVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AitEndPtVcQSize_Type.__name__ = "Integer32"
_AitEndPtVcQSize_Object = MibTableColumn
aitEndPtVcQSize = _AitEndPtVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 13),
    _AitEndPtVcQSize_Type()
)
aitEndPtVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtVcQSize.setStatus("mandatory")


class _AitEndPtPIR_Type(Integer32):
    """Custom type aitEndPtPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_AitEndPtPIR_Type.__name__ = "Integer32"
_AitEndPtPIR_Object = MibTableColumn
aitEndPtPIR = _AitEndPtPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 14),
    _AitEndPtPIR_Type()
)
aitEndPtPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtPIR.setStatus("mandatory")


class _AitEndPtCMAX_Type(Integer32):
    """Custom type aitEndPtCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AitEndPtCMAX_Type.__name__ = "Integer32"
_AitEndPtCMAX_Object = MibTableColumn
aitEndPtCMAX = _AitEndPtCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 15),
    _AitEndPtCMAX_Type()
)
aitEndPtCMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtCMAX.setStatus("mandatory")


class _AitEndPtEcnQSize_Type(Integer32):
    """Custom type aitEndPtEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AitEndPtEcnQSize_Type.__name__ = "Integer32"
_AitEndPtEcnQSize_Object = MibTableColumn
aitEndPtEcnQSize = _AitEndPtEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 16),
    _AitEndPtEcnQSize_Type()
)
aitEndPtEcnQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtEcnQSize.setStatus("mandatory")


class _AitEndPtQIR_Type(Integer32):
    """Custom type aitEndPtQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_AitEndPtQIR_Type.__name__ = "Integer32"
_AitEndPtQIR_Object = MibTableColumn
aitEndPtQIR = _AitEndPtQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 17),
    _AitEndPtQIR_Type()
)
aitEndPtQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtQIR.setStatus("mandatory")


class _AitEndPtPercUtil_Type(Integer32):
    """Custom type aitEndPtPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AitEndPtPercUtil_Type.__name__ = "Integer32"
_AitEndPtPercUtil_Object = MibTableColumn
aitEndPtPercUtil = _AitEndPtPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 18),
    _AitEndPtPercUtil_Type()
)
aitEndPtPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtPercUtil.setStatus("mandatory")


class _AitEndPtPriority_Type(Integer32):
    """Custom type aitEndPtPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_AitEndPtPriority_Type.__name__ = "Integer32"
_AitEndPtPriority_Object = MibTableColumn
aitEndPtPriority = _AitEndPtPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 5, 1, 19),
    _AitEndPtPriority_Type()
)
aitEndPtPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aitEndPtPriority.setStatus("mandatory")
_AtmEndPtTable_Object = MibTable
atmEndPtTable = _AtmEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6)
)
if mibBuilder.loadTexts:
    atmEndPtTable.setStatus("mandatory")
_AtmEndPtEntry_Object = MibTableRow
atmEndPtEntry = _AtmEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1)
)
atmEndPtEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndPtNodeName"),
    (0, "STRATACOM-MIB", "atmEndPtIfShelf"),
    (0, "STRATACOM-MIB", "atmEndPtSlot"),
    (0, "STRATACOM-MIB", "atmEndPtPort"),
    (0, "STRATACOM-MIB", "atmEndPtVpi"),
    (0, "STRATACOM-MIB", "atmEndPtVci"),
)
if mibBuilder.loadTexts:
    atmEndPtEntry.setStatus("mandatory")


class _AtmEndPtNodeName_Type(DisplayString):
    """Custom type atmEndPtNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AtmEndPtNodeName_Type.__name__ = "DisplayString"
_AtmEndPtNodeName_Object = MibTableColumn
atmEndPtNodeName = _AtmEndPtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 1),
    _AtmEndPtNodeName_Type()
)
atmEndPtNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtNodeName.setStatus("mandatory")


class _AtmEndPtIfShelf_Type(DisplayString):
    """Custom type atmEndPtIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtmEndPtIfShelf_Type.__name__ = "DisplayString"
_AtmEndPtIfShelf_Object = MibTableColumn
atmEndPtIfShelf = _AtmEndPtIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 2),
    _AtmEndPtIfShelf_Type()
)
atmEndPtIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtIfShelf.setStatus("mandatory")


class _AtmEndPtSlot_Type(Integer32):
    """Custom type atmEndPtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmEndPtSlot_Type.__name__ = "Integer32"
_AtmEndPtSlot_Object = MibTableColumn
atmEndPtSlot = _AtmEndPtSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 3),
    _AtmEndPtSlot_Type()
)
atmEndPtSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtSlot.setStatus("mandatory")


class _AtmEndPtPort_Type(Integer32):
    """Custom type atmEndPtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmEndPtPort_Type.__name__ = "Integer32"
_AtmEndPtPort_Object = MibTableColumn
atmEndPtPort = _AtmEndPtPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 4),
    _AtmEndPtPort_Type()
)
atmEndPtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtPort.setStatus("mandatory")


class _AtmEndPtVpi_Type(Integer32):
    """Custom type atmEndPtVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmEndPtVpi_Type.__name__ = "Integer32"
_AtmEndPtVpi_Object = MibTableColumn
atmEndPtVpi = _AtmEndPtVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 5),
    _AtmEndPtVpi_Type()
)
atmEndPtVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtVpi.setStatus("mandatory")


class _AtmEndPtVci_Type(Integer32):
    """Custom type atmEndPtVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmEndPtVci_Type.__name__ = "Integer32"
_AtmEndPtVci_Object = MibTableColumn
atmEndPtVci = _AtmEndPtVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 6),
    _AtmEndPtVci_Type()
)
atmEndPtVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtVci.setStatus("mandatory")


class _AtmEndPtConnIndex_Type(Integer32):
    """Custom type atmEndPtConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmEndPtConnIndex_Type.__name__ = "Integer32"
_AtmEndPtConnIndex_Object = MibTableColumn
atmEndPtConnIndex = _AtmEndPtConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 7),
    _AtmEndPtConnIndex_Type()
)
atmEndPtConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPtConnIndex.setStatus("mandatory")


class _AtmEndPtAdminStatus_Type(Integer32):
    """Custom type atmEndPtAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("testing", 3))
    )


_AtmEndPtAdminStatus_Type.__name__ = "Integer32"
_AtmEndPtAdminStatus_Object = MibTableColumn
atmEndPtAdminStatus = _AtmEndPtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 9),
    _AtmEndPtAdminStatus_Type()
)
atmEndPtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtAdminStatus.setStatus("mandatory")


class _AtmEndPtOpStatus_Type(Integer32):
    """Custom type atmEndPtOpStatus based on Integer32"""
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
        *(("clear", 2),
          ("down", 4),
          ("fail", 3),
          ("inactive", 1))
    )


_AtmEndPtOpStatus_Type.__name__ = "Integer32"
_AtmEndPtOpStatus_Object = MibTableColumn
atmEndPtOpStatus = _AtmEndPtOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 10),
    _AtmEndPtOpStatus_Type()
)
atmEndPtOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPtOpStatus.setStatus("mandatory")


class _AtmEndPtRowStatus_Type(Integer32):
    """Custom type atmEndPtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_AtmEndPtRowStatus_Type.__name__ = "Integer32"
_AtmEndPtRowStatus_Object = MibTableColumn
atmEndPtRowStatus = _AtmEndPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 11),
    _AtmEndPtRowStatus_Type()
)
atmEndPtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtRowStatus.setStatus("mandatory")


class _AtmEndPtMIR_Type(Integer32):
    """Custom type atmEndPtMIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndPtMIR_Type.__name__ = "Integer32"
_AtmEndPtMIR_Object = MibTableColumn
atmEndPtMIR = _AtmEndPtMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 12),
    _AtmEndPtMIR_Type()
)
atmEndPtMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtMIR.setStatus("mandatory")


class _AtmEndPtCIR_Type(Integer32):
    """Custom type atmEndPtCIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndPtCIR_Type.__name__ = "Integer32"
_AtmEndPtCIR_Object = MibTableColumn
atmEndPtCIR = _AtmEndPtCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 13),
    _AtmEndPtCIR_Type()
)
atmEndPtCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtCIR.setStatus("mandatory")


class _AtmEndPtPIR_Type(Integer32):
    """Custom type atmEndPtPIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 353208),
    )


_AtmEndPtPIR_Type.__name__ = "Integer32"
_AtmEndPtPIR_Object = MibTableColumn
atmEndPtPIR = _AtmEndPtPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 14),
    _AtmEndPtPIR_Type()
)
atmEndPtPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtPIR.setStatus("mandatory")


class _AtmEndPtQIR_Type(Integer32):
    """Custom type atmEndPtQIR based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmEndPtQIR_Type.__name__ = "Integer32"
_AtmEndPtQIR_Object = MibTableColumn
atmEndPtQIR = _AtmEndPtQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 15),
    _AtmEndPtQIR_Type()
)
atmEndPtQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtQIR.setStatus("mandatory")


class _AtmEndPtPercUtil_Type(Integer32):
    """Custom type atmEndPtPercUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmEndPtPercUtil_Type.__name__ = "Integer32"
_AtmEndPtPercUtil_Object = MibTableColumn
atmEndPtPercUtil = _AtmEndPtPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 16),
    _AtmEndPtPercUtil_Type()
)
atmEndPtPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtPercUtil.setStatus("mandatory")


class _AtmEndPtPriority_Type(Integer32):
    """Custom type atmEndPtPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_AtmEndPtPriority_Type.__name__ = "Integer32"
_AtmEndPtPriority_Object = MibTableColumn
atmEndPtPriority = _AtmEndPtPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 17),
    _AtmEndPtPriority_Type()
)
atmEndPtPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPtPriority.setStatus("mandatory")


class _AtmEndPtIBS_Type(Integer32):
    """Custom type atmEndPtIBS based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmEndPtIBS_Type.__name__ = "Integer32"
_AtmEndPtIBS_Object = MibTableColumn
atmEndPtIBS = _AtmEndPtIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 18),
    _AtmEndPtIBS_Type()
)
atmEndPtIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtIBS.setStatus("mandatory")


class _AtmEndPtVcQSize_Type(Integer32):
    """Custom type atmEndPtVcQSize based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndPtVcQSize_Type.__name__ = "Integer32"
_AtmEndPtVcQSize_Object = MibTableColumn
atmEndPtVcQSize = _AtmEndPtVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 6, 1, 19),
    _AtmEndPtVcQSize_Type()
)
atmEndPtVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPtVcQSize.setStatus("mandatory")
_SegmentTable_Object = MibTable
segmentTable = _SegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7)
)
if mibBuilder.loadTexts:
    segmentTable.setStatus("mandatory")
_SegmentEntry_Object = MibTableRow
segmentEntry = _SegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1)
)
segmentEntry.setIndexNames(
    (0, "STRATACOM-MIB", "segEndPtTableId"),
    (0, "STRATACOM-MIB", "segNodeName"),
    (0, "STRATACOM-MIB", "segShelf"),
    (0, "STRATACOM-MIB", "segSlot"),
    (0, "STRATACOM-MIB", "segLine"),
    (0, "STRATACOM-MIB", "segPort"),
    (0, "STRATACOM-MIB", "segSubChn1"),
    (0, "STRATACOM-MIB", "segSubChn2"),
)
if mibBuilder.loadTexts:
    segmentEntry.setStatus("mandatory")


class _SegEndPtTableId_Type(Integer32):
    """Custom type segEndPtTableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmEndptTable", 2),
          ("frEndPtTable", 1))
    )


_SegEndPtTableId_Type.__name__ = "Integer32"
_SegEndPtTableId_Object = MibTableColumn
segEndPtTableId = _SegEndPtTableId_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 1),
    _SegEndPtTableId_Type()
)
segEndPtTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segEndPtTableId.setStatus("mandatory")


class _SegNodeName_Type(DisplayString):
    """Custom type segNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SegNodeName_Type.__name__ = "DisplayString"
_SegNodeName_Object = MibTableColumn
segNodeName = _SegNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 2),
    _SegNodeName_Type()
)
segNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segNodeName.setStatus("mandatory")


class _SegShelf_Type(DisplayString):
    """Custom type segShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SegShelf_Type.__name__ = "DisplayString"
_SegShelf_Object = MibTableColumn
segShelf = _SegShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 3),
    _SegShelf_Type()
)
segShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segShelf.setStatus("mandatory")


class _SegSlot_Type(Integer32):
    """Custom type segSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SegSlot_Type.__name__ = "Integer32"
_SegSlot_Object = MibTableColumn
segSlot = _SegSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 4),
    _SegSlot_Type()
)
segSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segSlot.setStatus("mandatory")


class _SegLine_Type(Integer32):
    """Custom type segLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SegLine_Type.__name__ = "Integer32"
_SegLine_Object = MibTableColumn
segLine = _SegLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 5),
    _SegLine_Type()
)
segLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segLine.setStatus("mandatory")


class _SegPort_Type(Integer32):
    """Custom type segPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SegPort_Type.__name__ = "Integer32"
_SegPort_Object = MibTableColumn
segPort = _SegPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 6),
    _SegPort_Type()
)
segPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segPort.setStatus("mandatory")


class _SegSubChn1_Type(Integer32):
    """Custom type segSubChn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SegSubChn1_Type.__name__ = "Integer32"
_SegSubChn1_Object = MibTableColumn
segSubChn1 = _SegSubChn1_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 7),
    _SegSubChn1_Type()
)
segSubChn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segSubChn1.setStatus("mandatory")


class _SegSubChn2_Type(Integer32):
    """Custom type segSubChn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SegSubChn2_Type.__name__ = "Integer32"
_SegSubChn2_Object = MibTableColumn
segSubChn2 = _SegSubChn2_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 8),
    _SegSubChn2_Type()
)
segSubChn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segSubChn2.setStatus("mandatory")
_SegOeEndPt_Type = ObjectIdentifier
_SegOeEndPt_Object = MibTableColumn
segOeEndPt = _SegOeEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 9),
    _SegOeEndPt_Type()
)
segOeEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segOeEndPt.setStatus("mandatory")


class _SegConnIndex_Type(Integer32):
    """Custom type segConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SegConnIndex_Type.__name__ = "Integer32"
_SegConnIndex_Object = MibTableColumn
segConnIndex = _SegConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 10),
    _SegConnIndex_Type()
)
segConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segConnIndex.setStatus("mandatory")
_SegNextSeg_Type = ObjectIdentifier
_SegNextSeg_Object = MibTableColumn
segNextSeg = _SegNextSeg_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 7, 1, 11),
    _SegNextSeg_Type()
)
segNextSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segNextSeg.setStatus("mandatory")
_CmpaErrorLastIndex_Type = Integer32
_CmpaErrorLastIndex_Object = MibScalar
cmpaErrorLastIndex = _CmpaErrorLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 8),
    _CmpaErrorLastIndex_Type()
)
cmpaErrorLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorLastIndex.setStatus("mandatory")


class _CmpaErrorFlushAll_Type(Integer32):
    """Custom type cmpaErrorFlushAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flush", 2),
          ("noOp", 1))
    )


_CmpaErrorFlushAll_Type.__name__ = "Integer32"
_CmpaErrorFlushAll_Object = MibScalar
cmpaErrorFlushAll = _CmpaErrorFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 9),
    _CmpaErrorFlushAll_Type()
)
cmpaErrorFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpaErrorFlushAll.setStatus("mandatory")
_CmpaErrorTable_Object = MibTable
cmpaErrorTable = _CmpaErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 10)
)
if mibBuilder.loadTexts:
    cmpaErrorTable.setStatus("mandatory")
_CmpaErrorEntry_Object = MibTableRow
cmpaErrorEntry = _CmpaErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 10, 1)
)
cmpaErrorEntry.setIndexNames(
    (0, "STRATACOM-MIB", "cmpaErrorReqId"),
)
if mibBuilder.loadTexts:
    cmpaErrorEntry.setStatus("mandatory")
_CmpaErrorReqId_Type = Integer32
_CmpaErrorReqId_Object = MibTableColumn
cmpaErrorReqId = _CmpaErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 10, 1, 1),
    _CmpaErrorReqId_Type()
)
cmpaErrorReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorReqId.setStatus("mandatory")


class _CmpaErrorDesc_Type(DisplayString):
    """Custom type cmpaErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CmpaErrorDesc_Type.__name__ = "DisplayString"
_CmpaErrorDesc_Object = MibTableColumn
cmpaErrorDesc = _CmpaErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 10, 1, 2),
    _CmpaErrorDesc_Type()
)
cmpaErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorDesc.setStatus("mandatory")


class _CmpaErrorEcode_Type(Integer32):
    """Custom type cmpaErrorEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("asi-no-remote", 131),
          ("bad-value", 10),
          ("cmgrd-timeout", 125),
          ("conn-not-found", 100),
          ("conn-rowstatus-missing", 112),
          ("dangling-endpt", 110),
          ("db-lendpt-not-found", 106),
          ("db-rendpt-not-found", 107),
          ("endpt-exists", 101),
          ("endpt-rowstatus-missing", 111),
          ("foresight-disabled", 133),
          ("frsm-remote", 132),
          ("ibs-less-bc", 130),
          ("invalid-adminstatus", 121),
          ("invalid-bw", 119),
          ("invalid-chanCLPtoDEmap", 129),
          ("invalid-chanFECNconfig", 128),
          ("invalid-chantype", 124),
          ("invalid-conn-rowstatus", 114),
          ("invalid-connindex", 115),
          ("invalid-endpt-comb", 123),
          ("invalid-endpt-rowstatus", 113),
          ("invalid-flushall", 502),
          ("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-release", 4),
          ("invalid-shelf", 3),
          ("lendpt-exists", 102),
          ("lendpt-missing", 104),
          ("lendpt-not-found", 108),
          ("no-cmgrd", 126),
          ("no-error-entry", 500),
          ("no-snmpcomm", 7),
          ("node-busy", 6),
          ("node-error", 9),
          ("node-timeout", 5),
          ("not-active", 120),
          ("not-applicable", 501),
          ("not-clear", 122),
          ("partial-add", 117),
          ("partial-mod", 118),
          ("port-not-found", 11),
          ("rendpt-exists", 103),
          ("rendpt-missing", 105),
          ("rendpt-not-found", 109),
          ("ronly-for-frp", 127),
          ("slot-is-full", 12),
          ("snmpcomm-error", 8),
          ("testtype-missing", 116))
    )


_CmpaErrorEcode_Type.__name__ = "Integer32"
_CmpaErrorEcode_Object = MibTableColumn
cmpaErrorEcode = _CmpaErrorEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 10, 1, 3),
    _CmpaErrorEcode_Type()
)
cmpaErrorEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorEcode.setStatus("mandatory")


class _CmpaErrorLastDesc_Type(DisplayString):
    """Custom type cmpaErrorLastDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmpaErrorLastDesc_Type.__name__ = "DisplayString"
_CmpaErrorLastDesc_Object = MibScalar
cmpaErrorLastDesc = _CmpaErrorLastDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 11),
    _CmpaErrorLastDesc_Type()
)
cmpaErrorLastDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorLastDesc.setStatus("mandatory")


class _CmpaErrorLastEcode_Type(Integer32):
    """Custom type cmpaErrorLastEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("asi-no-remote", 131),
          ("bad-value", 10),
          ("cmgrd-timeout", 125),
          ("conn-not-found", 100),
          ("conn-rowstatus-missing", 112),
          ("dangling-endpt", 110),
          ("db-lendpt-not-found", 106),
          ("db-rendpt-not-found", 107),
          ("endpt-exists", 101),
          ("endpt-rowstatus-missing", 111),
          ("foresight-disabled", 133),
          ("frsm-remote", 132),
          ("ibs-less-bc", 130),
          ("invalid-adminstatus", 121),
          ("invalid-bw", 119),
          ("invalid-chanCLPtoDEmap", 129),
          ("invalid-chanFECNconfig", 128),
          ("invalid-chantype", 124),
          ("invalid-conn-rowstatus", 114),
          ("invalid-connindex", 115),
          ("invalid-endpt-comb", 123),
          ("invalid-endpt-rowstatus", 113),
          ("invalid-flushall", 502),
          ("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-release", 4),
          ("invalid-shelf", 3),
          ("lendpt-exists", 102),
          ("lendpt-missing", 104),
          ("lendpt-not-found", 108),
          ("no-cmgrd", 126),
          ("no-error-entry", 500),
          ("no-snmpcomm", 7),
          ("node-busy", 6),
          ("node-error", 9),
          ("node-timeout", 5),
          ("not-active", 120),
          ("not-applicable", 501),
          ("not-clear", 122),
          ("partial-add", 117),
          ("partial-mod", 118),
          ("port-not-found", 11),
          ("rendpt-exists", 103),
          ("rendpt-missing", 105),
          ("rendpt-not-found", 109),
          ("ronly-for-frp", 127),
          ("slot-is-full", 12),
          ("snmpcomm-error", 8),
          ("testtype-missing", 116))
    )


_CmpaErrorLastEcode_Type.__name__ = "Integer32"
_CmpaErrorLastEcode_Object = MibScalar
cmpaErrorLastEcode = _CmpaErrorLastEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 3, 12),
    _CmpaErrorLastEcode_Type()
)
cmpaErrorLastEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpaErrorLastEcode.setStatus("mandatory")
_PortSvc_ObjectIdentity = ObjectIdentity
portSvc = _PortSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 4)
)
_PortsInfoTable_Object = MibTable
portsInfoTable = _PortsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1)
)
if mibBuilder.loadTexts:
    portsInfoTable.setStatus("mandatory")
_PortsInfoEntry_Object = MibTableRow
portsInfoEntry = _PortsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1)
)
portsInfoEntry.setIndexNames(
    (0, "STRATACOM-MIB", "portsInfoNode"),
    (0, "STRATACOM-MIB", "portsInfoShelf"),
    (0, "STRATACOM-MIB", "portsInfoSlot"),
    (0, "STRATACOM-MIB", "portsInfoLine"),
    (0, "STRATACOM-MIB", "portsInfoPort"),
)
if mibBuilder.loadTexts:
    portsInfoEntry.setStatus("mandatory")


class _PortsInfoNode_Type(DisplayString):
    """Custom type portsInfoNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_PortsInfoNode_Type.__name__ = "DisplayString"
_PortsInfoNode_Object = MibTableColumn
portsInfoNode = _PortsInfoNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 1),
    _PortsInfoNode_Type()
)
portsInfoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoNode.setStatus("mandatory")


class _PortsInfoShelf_Type(DisplayString):
    """Custom type portsInfoShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortsInfoShelf_Type.__name__ = "DisplayString"
_PortsInfoShelf_Object = MibTableColumn
portsInfoShelf = _PortsInfoShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 2),
    _PortsInfoShelf_Type()
)
portsInfoShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoShelf.setStatus("mandatory")


class _PortsInfoSlot_Type(Integer32):
    """Custom type portsInfoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PortsInfoSlot_Type.__name__ = "Integer32"
_PortsInfoSlot_Object = MibTableColumn
portsInfoSlot = _PortsInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 3),
    _PortsInfoSlot_Type()
)
portsInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoSlot.setStatus("mandatory")


class _PortsInfoLine_Type(Integer32):
    """Custom type portsInfoLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PortsInfoLine_Type.__name__ = "Integer32"
_PortsInfoLine_Object = MibTableColumn
portsInfoLine = _PortsInfoLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 4),
    _PortsInfoLine_Type()
)
portsInfoLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoLine.setStatus("mandatory")


class _PortsInfoPort_Type(Integer32):
    """Custom type portsInfoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PortsInfoPort_Type.__name__ = "Integer32"
_PortsInfoPort_Object = MibTableColumn
portsInfoPort = _PortsInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 5),
    _PortsInfoPort_Type()
)
portsInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoPort.setStatus("mandatory")


class _PortsInfoPortType_Type(Integer32):
    """Custom type portsInfoPortType based on Integer32"""
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
        *(("atm", 4),
          ("ausm", 3),
          ("frp", 2),
          ("frsm", 1))
    )


_PortsInfoPortType_Type.__name__ = "Integer32"
_PortsInfoPortType_Object = MibTableColumn
portsInfoPortType = _PortsInfoPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 6),
    _PortsInfoPortType_Type()
)
portsInfoPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoPortType.setStatus("mandatory")


class _PortsInfoPortState_Type(Integer32):
    """Custom type portsInfoPortState based on Integer32"""
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
        *(("active", 1),
          ("failed", 4),
          ("inactive", 2),
          ("remoteLoopback", 3))
    )


_PortsInfoPortState_Type.__name__ = "Integer32"
_PortsInfoPortState_Object = MibTableColumn
portsInfoPortState = _PortsInfoPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 7),
    _PortsInfoPortState_Type()
)
portsInfoPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoPortState.setStatus("mandatory")
_PortsInfoPortSpeed_Type = Integer32
_PortsInfoPortSpeed_Object = MibTableColumn
portsInfoPortSpeed = _PortsInfoPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 1, 1, 8),
    _PortsInfoPortSpeed_Type()
)
portsInfoPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsInfoPortSpeed.setStatus("mandatory")
_FrPortsCfgTable_Object = MibTable
frPortsCfgTable = _FrPortsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2)
)
if mibBuilder.loadTexts:
    frPortsCfgTable.setStatus("mandatory")
_FrPortsCfgEntry_Object = MibTableRow
frPortsCfgEntry = _FrPortsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1)
)
frPortsCfgEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frPortsCfgNode"),
    (0, "STRATACOM-MIB", "frPortsCfgShelf"),
    (0, "STRATACOM-MIB", "frPortsCfgSlot"),
    (0, "STRATACOM-MIB", "frPortsCfgLine"),
    (0, "STRATACOM-MIB", "frPortsCfgPort"),
)
if mibBuilder.loadTexts:
    frPortsCfgEntry.setStatus("mandatory")


class _FrPortsCfgNode_Type(DisplayString):
    """Custom type frPortsCfgNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrPortsCfgNode_Type.__name__ = "DisplayString"
_FrPortsCfgNode_Object = MibTableColumn
frPortsCfgNode = _FrPortsCfgNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 1),
    _FrPortsCfgNode_Type()
)
frPortsCfgNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgNode.setStatus("mandatory")


class _FrPortsCfgShelf_Type(DisplayString):
    """Custom type frPortsCfgShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FrPortsCfgShelf_Type.__name__ = "DisplayString"
_FrPortsCfgShelf_Object = MibTableColumn
frPortsCfgShelf = _FrPortsCfgShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 2),
    _FrPortsCfgShelf_Type()
)
frPortsCfgShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgShelf.setStatus("mandatory")


class _FrPortsCfgSlot_Type(Integer32):
    """Custom type frPortsCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrPortsCfgSlot_Type.__name__ = "Integer32"
_FrPortsCfgSlot_Object = MibTableColumn
frPortsCfgSlot = _FrPortsCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 3),
    _FrPortsCfgSlot_Type()
)
frPortsCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgSlot.setStatus("mandatory")


class _FrPortsCfgLine_Type(Integer32):
    """Custom type frPortsCfgLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FrPortsCfgLine_Type.__name__ = "Integer32"
_FrPortsCfgLine_Object = MibTableColumn
frPortsCfgLine = _FrPortsCfgLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 4),
    _FrPortsCfgLine_Type()
)
frPortsCfgLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgLine.setStatus("mandatory")


class _FrPortsCfgPort_Type(Integer32):
    """Custom type frPortsCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrPortsCfgPort_Type.__name__ = "Integer32"
_FrPortsCfgPort_Object = MibTableColumn
frPortsCfgPort = _FrPortsCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 5),
    _FrPortsCfgPort_Type()
)
frPortsCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgPort.setStatus("mandatory")


class _FrPortsCfgRowStatus_Type(Integer32):
    """Custom type frPortsCfgRowStatus based on Integer32"""
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
        *(("add", 1),
          ("del", 2),
          ("down-frp", 5),
          ("modify", 3),
          ("up-frp", 4))
    )


_FrPortsCfgRowStatus_Type.__name__ = "Integer32"
_FrPortsCfgRowStatus_Object = MibTableColumn
frPortsCfgRowStatus = _FrPortsCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 6),
    _FrPortsCfgRowStatus_Type()
)
frPortsCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgRowStatus.setStatus("mandatory")


class _FrPortsCfgPortType_Type(Integer32):
    """Custom type frPortsCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frp", 2),
          ("frsm", 1))
    )


_FrPortsCfgPortType_Type.__name__ = "Integer32"
_FrPortsCfgPortType_Object = MibTableColumn
frPortsCfgPortType = _FrPortsCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 7),
    _FrPortsCfgPortType_Type()
)
frPortsCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgPortType.setStatus("mandatory")


class _FrPortsCfgPortState_Type(Integer32):
    """Custom type frPortsCfgPortState based on Integer32"""
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
        *(("active", 1),
          ("failed", 4),
          ("inactive", 2),
          ("remoteLoopback", 3))
    )


_FrPortsCfgPortState_Type.__name__ = "Integer32"
_FrPortsCfgPortState_Object = MibTableColumn
frPortsCfgPortState = _FrPortsCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 8),
    _FrPortsCfgPortState_Type()
)
frPortsCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgPortState.setStatus("mandatory")
_FrPortsCfgChCnt_Type = Integer32
_FrPortsCfgChCnt_Object = MibTableColumn
frPortsCfgChCnt = _FrPortsCfgChCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 9),
    _FrPortsCfgChCnt_Type()
)
frPortsCfgChCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgChCnt.setStatus("mandatory")
_FrPortsCfgPortSpeed_Type = Integer32
_FrPortsCfgPortSpeed_Object = MibTableColumn
frPortsCfgPortSpeed = _FrPortsCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 10),
    _FrPortsCfgPortSpeed_Type()
)
frPortsCfgPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgPortSpeed.setStatus("mandatory")


class _FrPortsCfgDs0ChSpeed_Type(Integer32):
    """Custom type frPortsCfgDs0ChSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("s56k", 1),
          ("s64k", 2))
    )


_FrPortsCfgDs0ChSpeed_Type.__name__ = "Integer32"
_FrPortsCfgDs0ChSpeed_Object = MibTableColumn
frPortsCfgDs0ChSpeed = _FrPortsCfgDs0ChSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 11),
    _FrPortsCfgDs0ChSpeed_Type()
)
frPortsCfgDs0ChSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgDs0ChSpeed.setStatus("mandatory")


class _FrPortsCfgSigProt_Type(Integer32):
    """Custom type frPortsCfgSigProt based on Integer32"""
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
        *(("disabled", 1),
          ("lmi-asyn", 3),
          ("lmi-noasyn", 2),
          ("nni-annexA", 6),
          ("nni-annexD", 7),
          ("uni-annexA", 4),
          ("uni-annexD", 5))
    )


_FrPortsCfgSigProt_Type.__name__ = "Integer32"
_FrPortsCfgSigProt_Object = MibTableColumn
frPortsCfgSigProt = _FrPortsCfgSigProt_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 12),
    _FrPortsCfgSigProt_Type()
)
frPortsCfgSigProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgSigProt.setStatus("mandatory")


class _FrPortsCfgNNIStatus_Type(Integer32):
    """Custom type frPortsCfgNNIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrPortsCfgNNIStatus_Type.__name__ = "Integer32"
_FrPortsCfgNNIStatus_Object = MibTableColumn
frPortsCfgNNIStatus = _FrPortsCfgNNIStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 13),
    _FrPortsCfgNNIStatus_Type()
)
frPortsCfgNNIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgNNIStatus.setStatus("mandatory")


class _FrPortsCfgAsyncUpd_Type(Integer32):
    """Custom type frPortsCfgAsyncUpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrPortsCfgAsyncUpd_Type.__name__ = "Integer32"
_FrPortsCfgAsyncUpd_Object = MibTableColumn
frPortsCfgAsyncUpd = _FrPortsCfgAsyncUpd_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 14),
    _FrPortsCfgAsyncUpd_Type()
)
frPortsCfgAsyncUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgAsyncUpd.setStatus("mandatory")


class _FrPortsCfgPollVerTimer_Type(Integer32):
    """Custom type frPortsCfgPollVerTimer based on Integer32"""
    defaultValue = 15


_FrPortsCfgPollVerTimer_Object = MibTableColumn
frPortsCfgPollVerTimer = _FrPortsCfgPollVerTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 15),
    _FrPortsCfgPollVerTimer_Type()
)
frPortsCfgPollVerTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgPollVerTimer.setStatus("mandatory")
_FrPortsCfgErrThresh_Type = Integer32
_FrPortsCfgErrThresh_Object = MibTableColumn
frPortsCfgErrThresh = _FrPortsCfgErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 16),
    _FrPortsCfgErrThresh_Type()
)
frPortsCfgErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgErrThresh.setStatus("mandatory")
_FrPortsCfgMonEveCnt_Type = Integer32
_FrPortsCfgMonEveCnt_Object = MibTableColumn
frPortsCfgMonEveCnt = _FrPortsCfgMonEveCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 17),
    _FrPortsCfgMonEveCnt_Type()
)
frPortsCfgMonEveCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgMonEveCnt.setStatus("mandatory")


class _FrPortsCfgFrmFlags_Type(Integer32):
    """Custom type frPortsCfgFrmFlags based on Integer32"""
    defaultValue = 1


_FrPortsCfgFrmFlags_Object = MibTableColumn
frPortsCfgFrmFlags = _FrPortsCfgFrmFlags_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 18),
    _FrPortsCfgFrmFlags_Type()
)
frPortsCfgFrmFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgFrmFlags.setStatus("mandatory")


class _FrPortsCfgLinkTimer_Type(Integer32):
    """Custom type frPortsCfgLinkTimer based on Integer32"""
    defaultValue = 10


_FrPortsCfgLinkTimer_Object = MibTableColumn
frPortsCfgLinkTimer = _FrPortsCfgLinkTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 19),
    _FrPortsCfgLinkTimer_Type()
)
frPortsCfgLinkTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgLinkTimer.setStatus("mandatory")


class _FrPortsCfgPollCycle_Type(Integer32):
    """Custom type frPortsCfgPollCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrPortsCfgPollCycle_Type.__name__ = "Integer32"
_FrPortsCfgPollCycle_Object = MibTableColumn
frPortsCfgPollCycle = _FrPortsCfgPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 20),
    _FrPortsCfgPollCycle_Type()
)
frPortsCfgPollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frPortsCfgPollCycle.setStatus("mandatory")


class _FrAxPortsCfgSvcRatio_Type(Integer32):
    """Custom type frAxPortsCfgSvcRatio based on Integer32"""
    defaultValue = 1


_FrAxPortsCfgSvcRatio_Object = MibTableColumn
frAxPortsCfgSvcRatio = _FrAxPortsCfgSvcRatio_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 21),
    _FrAxPortsCfgSvcRatio_Type()
)
frAxPortsCfgSvcRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAxPortsCfgSvcRatio.setStatus("mandatory")


class _FrIxPortsCfgClockType_Type(Integer32):
    """Custom type frIxPortsCfgClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("looped", 2),
          ("none", 3),
          ("normal", 1))
    )


_FrIxPortsCfgClockType_Type.__name__ = "Integer32"
_FrIxPortsCfgClockType_Object = MibTableColumn
frIxPortsCfgClockType = _FrIxPortsCfgClockType_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 22),
    _FrIxPortsCfgClockType_Type()
)
frIxPortsCfgClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgClockType.setStatus("mandatory")
_FrIxPortsCfgVcCount_Type = Integer32
_FrIxPortsCfgVcCount_Object = MibTableColumn
frIxPortsCfgVcCount = _FrIxPortsCfgVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 23),
    _FrIxPortsCfgVcCount_Type()
)
frIxPortsCfgVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgVcCount.setStatus("mandatory")
_FrPortsCfgVcPtr_Type = ObjectIdentifier
_FrPortsCfgVcPtr_Object = MibTableColumn
frPortsCfgVcPtr = _FrPortsCfgVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 24),
    _FrPortsCfgVcPtr_Type()
)
frPortsCfgVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPortsCfgVcPtr.setStatus("mandatory")


class _FrIxPortsCfgMaxTxQDepth_Type(Integer32):
    """Custom type frIxPortsCfgMaxTxQDepth based on Integer32"""
    defaultValue = 65535


_FrIxPortsCfgMaxTxQDepth_Object = MibTableColumn
frIxPortsCfgMaxTxQDepth = _FrIxPortsCfgMaxTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 25),
    _FrIxPortsCfgMaxTxQDepth_Type()
)
frIxPortsCfgMaxTxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgMaxTxQDepth.setStatus("mandatory")


class _FrIxPortsCfgECNQThresh_Type(Integer32):
    """Custom type frIxPortsCfgECNQThresh based on Integer32"""
    defaultValue = 65535


_FrIxPortsCfgECNQThresh_Object = MibTableColumn
frIxPortsCfgECNQThresh = _FrIxPortsCfgECNQThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 26),
    _FrIxPortsCfgECNQThresh_Type()
)
frIxPortsCfgECNQThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgECNQThresh.setStatus("mandatory")


class _FrIxPortsCfgDEThresh_Type(Integer32):
    """Custom type frIxPortsCfgDEThresh based on Integer32"""
    defaultValue = 100


_FrIxPortsCfgDEThresh_Object = MibTableColumn
frIxPortsCfgDEThresh = _FrIxPortsCfgDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 27),
    _FrIxPortsCfgDEThresh_Type()
)
frIxPortsCfgDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgDEThresh.setStatus("mandatory")


class _FrIxPortsCfgIDEMap_Type(Integer32):
    """Custom type frIxPortsCfgIDEMap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrIxPortsCfgIDEMap_Type.__name__ = "Integer32"
_FrIxPortsCfgIDEMap_Object = MibTableColumn
frIxPortsCfgIDEMap = _FrIxPortsCfgIDEMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 28),
    _FrIxPortsCfgIDEMap_Type()
)
frIxPortsCfgIDEMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgIDEMap.setStatus("mandatory")


class _FrIxPortsCfgCommPri_Type(Integer32):
    """Custom type frIxPortsCfgCommPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrIxPortsCfgCommPri_Type.__name__ = "Integer32"
_FrIxPortsCfgCommPri_Object = MibTableColumn
frIxPortsCfgCommPri = _FrIxPortsCfgCommPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 29),
    _FrIxPortsCfgCommPri_Type()
)
frIxPortsCfgCommPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgCommPri.setStatus("mandatory")


class _FrIxPortsCfgUpRNR_Type(Integer32):
    """Custom type frIxPortsCfgUpRNR based on Integer32"""
    defaultValue = 75


_FrIxPortsCfgUpRNR_Object = MibTableColumn
frIxPortsCfgUpRNR = _FrIxPortsCfgUpRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 30),
    _FrIxPortsCfgUpRNR_Type()
)
frIxPortsCfgUpRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgUpRNR.setStatus("mandatory")


class _FrIxPortsCfgLowRNR_Type(Integer32):
    """Custom type frIxPortsCfgLowRNR based on Integer32"""
    defaultValue = 75


_FrIxPortsCfgLowRNR_Object = MibTableColumn
frIxPortsCfgLowRNR = _FrIxPortsCfgLowRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 31),
    _FrIxPortsCfgLowRNR_Type()
)
frIxPortsCfgLowRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgLowRNR.setStatus("mandatory")
_FrIxPortsCfgOamThresh_Type = Integer32
_FrIxPortsCfgOamThresh_Object = MibTableColumn
frIxPortsCfgOamThresh = _FrIxPortsCfgOamThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 32),
    _FrIxPortsCfgOamThresh_Type()
)
frIxPortsCfgOamThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgOamThresh.setStatus("mandatory")
_FrIxPortsCfgCLLMTimer_Type = Integer32
_FrIxPortsCfgCLLMTimer_Object = MibTableColumn
frIxPortsCfgCLLMTimer = _FrIxPortsCfgCLLMTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 33),
    _FrIxPortsCfgCLLMTimer_Type()
)
frIxPortsCfgCLLMTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgCLLMTimer.setStatus("mandatory")


class _FrIxPortsCfgEFCItoBECN_Type(Integer32):
    """Custom type frIxPortsCfgEFCItoBECN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("none", 3),
          ("yes", 2))
    )


_FrIxPortsCfgEFCItoBECN_Type.__name__ = "Integer32"
_FrIxPortsCfgEFCItoBECN_Object = MibTableColumn
frIxPortsCfgEFCItoBECN = _FrIxPortsCfgEFCItoBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 34),
    _FrIxPortsCfgEFCItoBECN_Type()
)
frIxPortsCfgEFCItoBECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIxPortsCfgEFCItoBECN.setStatus("mandatory")


class _FrIxPortsCfgSrRTS_Type(Integer32):
    """Custom type frIxPortsCfgSrRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("off", 1),
          ("on", 2))
    )


_FrIxPortsCfgSrRTS_Type.__name__ = "Integer32"
_FrIxPortsCfgSrRTS_Object = MibTableColumn
frIxPortsCfgSrRTS = _FrIxPortsCfgSrRTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 35),
    _FrIxPortsCfgSrRTS_Type()
)
frIxPortsCfgSrRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgSrRTS.setStatus("mandatory")


class _FrIxPortsCfgSrDTR_Type(Integer32):
    """Custom type frIxPortsCfgSrDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("off", 1),
          ("on", 2))
    )


_FrIxPortsCfgSrDTR_Type.__name__ = "Integer32"
_FrIxPortsCfgSrDTR_Object = MibTableColumn
frIxPortsCfgSrDTR = _FrIxPortsCfgSrDTR_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 36),
    _FrIxPortsCfgSrDTR_Type()
)
frIxPortsCfgSrDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgSrDTR.setStatus("mandatory")


class _FrIxPortsCfgSrDCD_Type(Integer32):
    """Custom type frIxPortsCfgSrDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("off", 1),
          ("on", 2))
    )


_FrIxPortsCfgSrDCD_Type.__name__ = "Integer32"
_FrIxPortsCfgSrDCD_Object = MibTableColumn
frIxPortsCfgSrDCD = _FrIxPortsCfgSrDCD_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 37),
    _FrIxPortsCfgSrDCD_Type()
)
frIxPortsCfgSrDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgSrDCD.setStatus("mandatory")


class _FrIxPortsCfgSrCTS_Type(Integer32):
    """Custom type frIxPortsCfgSrCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("off", 1),
          ("on", 2))
    )


_FrIxPortsCfgSrCTS_Type.__name__ = "Integer32"
_FrIxPortsCfgSrCTS_Object = MibTableColumn
frIxPortsCfgSrCTS = _FrIxPortsCfgSrCTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 38),
    _FrIxPortsCfgSrCTS_Type()
)
frIxPortsCfgSrCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgSrCTS.setStatus("mandatory")


class _FrIxPortsCfgSrDSR_Type(Integer32):
    """Custom type frIxPortsCfgSrDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("off", 1),
          ("on", 2))
    )


_FrIxPortsCfgSrDSR_Type.__name__ = "Integer32"
_FrIxPortsCfgSrDSR_Object = MibTableColumn
frIxPortsCfgSrDSR = _FrIxPortsCfgSrDSR_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 39),
    _FrIxPortsCfgSrDSR_Type()
)
frIxPortsCfgSrDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgSrDSR.setStatus("mandatory")


class _FrIxPortsCfgLoopBack_Type(Integer32):
    """Custom type frIxPortsCfgLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("none", 1))
    )


_FrIxPortsCfgLoopBack_Type.__name__ = "Integer32"
_FrIxPortsCfgLoopBack_Object = MibTableColumn
frIxPortsCfgLoopBack = _FrIxPortsCfgLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 40),
    _FrIxPortsCfgLoopBack_Type()
)
frIxPortsCfgLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgLoopBack.setStatus("mandatory")


class _FrIxPortsCfgExtConFail_Type(Integer32):
    """Custom type frIxPortsCfgExtConFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrIxPortsCfgExtConFail_Type.__name__ = "Integer32"
_FrIxPortsCfgExtConFail_Object = MibTableColumn
frIxPortsCfgExtConFail = _FrIxPortsCfgExtConFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 41),
    _FrIxPortsCfgExtConFail_Type()
)
frIxPortsCfgExtConFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frIxPortsCfgExtConFail.setStatus("mandatory")
_FrAxPortsCfgLogPort_Type = Integer32
_FrAxPortsCfgLogPort_Object = MibTableColumn
frAxPortsCfgLogPort = _FrAxPortsCfgLogPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 2, 1, 42),
    _FrAxPortsCfgLogPort_Type()
)
frAxPortsCfgLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAxPortsCfgLogPort.setStatus("mandatory")
_PpaErrorLastIndex_Type = Integer32
_PpaErrorLastIndex_Object = MibScalar
ppaErrorLastIndex = _PpaErrorLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 8),
    _PpaErrorLastIndex_Type()
)
ppaErrorLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorLastIndex.setStatus("mandatory")


class _PpaErrorFlushAll_Type(Integer32):
    """Custom type ppaErrorFlushAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flush", 2),
          ("noOp", 1))
    )


_PpaErrorFlushAll_Type.__name__ = "Integer32"
_PpaErrorFlushAll_Object = MibScalar
ppaErrorFlushAll = _PpaErrorFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 9),
    _PpaErrorFlushAll_Type()
)
ppaErrorFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppaErrorFlushAll.setStatus("mandatory")
_PpaErrorTable_Object = MibTable
ppaErrorTable = _PpaErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 10)
)
if mibBuilder.loadTexts:
    ppaErrorTable.setStatus("mandatory")
_PpaErrorEntry_Object = MibTableRow
ppaErrorEntry = _PpaErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 10, 1)
)
ppaErrorEntry.setIndexNames(
    (0, "STRATACOM-MIB", "ppaErrorReqId"),
)
if mibBuilder.loadTexts:
    ppaErrorEntry.setStatus("mandatory")
_PpaErrorReqId_Type = Integer32
_PpaErrorReqId_Object = MibTableColumn
ppaErrorReqId = _PpaErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 10, 1, 1),
    _PpaErrorReqId_Type()
)
ppaErrorReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorReqId.setStatus("mandatory")


class _PpaErrorDesc_Type(DisplayString):
    """Custom type ppaErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PpaErrorDesc_Type.__name__ = "DisplayString"
_PpaErrorDesc_Object = MibTableColumn
ppaErrorDesc = _PpaErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 10, 1, 2),
    _PpaErrorDesc_Type()
)
ppaErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorDesc.setStatus("mandatory")


class _PpaErrorEcode_Type(Integer32):
    """Custom type ppaErrorEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("bad-value", 10),
          ("illegal-set", 111),
          ("invalid-flushall", 502),
          ("invalid-line", 103),
          ("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-release", 4),
          ("invalid-set", 110),
          ("invalid-shelf", 3),
          ("invalid-slot", 102),
          ("line-is-full", 104),
          ("multiple-ports", 105),
          ("na-frp", 108),
          ("na-frsm", 107),
          ("no-error-entry", 500),
          ("no-snmpcomm", 7),
          ("no-up-down-frsm", 109),
          ("node-busy", 6),
          ("node-error", 9),
          ("node-timeout", 5),
          ("not-applicable", 501),
          ("partial-add", 112),
          ("port-exists", 101),
          ("port-not-found", 11),
          ("port-reserved", 106),
          ("rowstatus-missing", 100),
          ("slot-is-full", 12),
          ("snmpcomm-error", 8))
    )


_PpaErrorEcode_Type.__name__ = "Integer32"
_PpaErrorEcode_Object = MibTableColumn
ppaErrorEcode = _PpaErrorEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 10, 1, 3),
    _PpaErrorEcode_Type()
)
ppaErrorEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorEcode.setStatus("mandatory")


class _PpaErrorLastDesc_Type(DisplayString):
    """Custom type ppaErrorLastDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpaErrorLastDesc_Type.__name__ = "DisplayString"
_PpaErrorLastDesc_Object = MibScalar
ppaErrorLastDesc = _PpaErrorLastDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 11),
    _PpaErrorLastDesc_Type()
)
ppaErrorLastDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorLastDesc.setStatus("mandatory")


class _PpaErrorLastEcode_Type(Integer32):
    """Custom type ppaErrorLastEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("bad-value", 10),
          ("illegal-set", 111),
          ("invalid-flushall", 502),
          ("invalid-line", 103),
          ("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-release", 4),
          ("invalid-set", 110),
          ("invalid-shelf", 3),
          ("invalid-slot", 102),
          ("line-is-full", 104),
          ("multiple-ports", 105),
          ("na-frp", 108),
          ("na-frsm", 107),
          ("no-error-entry", 500),
          ("no-snmpcomm", 7),
          ("no-up-down-frsm", 109),
          ("node-busy", 6),
          ("node-error", 9),
          ("node-timeout", 5),
          ("not-applicable", 501),
          ("partial-add", 112),
          ("port-exists", 101),
          ("port-not-found", 11),
          ("port-reserved", 106),
          ("rowstatus-missing", 100),
          ("slot-is-full", 12),
          ("snmpcomm-error", 8))
    )


_PpaErrorLastEcode_Type.__name__ = "Integer32"
_PpaErrorLastEcode_Object = MibScalar
ppaErrorLastEcode = _PpaErrorLastEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 4, 12),
    _PpaErrorLastEcode_Type()
)
ppaErrorLastEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppaErrorLastEcode.setStatus("mandatory")
_SnmpAgents_ObjectIdentity = ObjectIdentity
snmpAgents = _SnmpAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100)
)
_StrmSwitchMIB_ObjectIdentity = ObjectIdentity
strmSwitchMIB = _StrmSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4)
)
_SwitchInterfaces_ObjectIdentity = ObjectIdentity
switchInterfaces = _SwitchInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1)
)
_SwitchIfTable_Object = MibTable
switchIfTable = _SwitchIfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1)
)
if mibBuilder.loadTexts:
    switchIfTable.setStatus("mandatory")
_SwitchIfEntry_Object = MibTableRow
switchIfEntry = _SwitchIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1)
)
switchIfEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    switchIfEntry.setStatus("mandatory")
_SwitchIfIndex_Type = Integer32
_SwitchIfIndex_Object = MibTableColumn
switchIfIndex = _SwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 1),
    _SwitchIfIndex_Type()
)
switchIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfIndex.setStatus("mandatory")
_SwitchIfSlot_Type = Integer32
_SwitchIfSlot_Object = MibTableColumn
switchIfSlot = _SwitchIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 2),
    _SwitchIfSlot_Type()
)
switchIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSlot.setStatus("mandatory")
_SwitchIfPort_Type = Integer32
_SwitchIfPort_Object = MibTableColumn
switchIfPort = _SwitchIfPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 3),
    _SwitchIfPort_Type()
)
switchIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfPort.setStatus("mandatory")
_SwitchIfSubPort_Type = Integer32
_SwitchIfSubPort_Object = MibTableColumn
switchIfSubPort = _SwitchIfSubPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 4),
    _SwitchIfSubPort_Type()
)
switchIfSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSubPort.setStatus("mandatory")


class _SwitchIfMediaType_Type(Integer32):
    """Custom type switchIfMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              18,
              22,
              30,
              39)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 18),
          ("ds3", 30),
          ("other", 1),
          ("serialPort", 22),
          ("sonet", 39))
    )


_SwitchIfMediaType_Type.__name__ = "Integer32"
_SwitchIfMediaType_Object = MibTableColumn
switchIfMediaType = _SwitchIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 5),
    _SwitchIfMediaType_Type()
)
switchIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfMediaType.setStatus("mandatory")


class _SwitchIfService_Type(Integer32):
    """Custom type switchIfService based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("atmAPSIntfTrk", 10),
          ("atmAccessPort", 3),
          ("atmAxisIntfTrk", 7),
          ("atmFdrIntfTrk", 9),
          ("atmIPXAFIntfTrk", 8),
          ("atmParIntfTrk", 14),
          ("atmRoutingTrk", 6),
          ("atmVsiIntfTrk", 13),
          ("fpRoutingTrk", 5),
          ("frameRelay", 2),
          ("imaRoutingTrunk", 11),
          ("other", 1),
          ("physicalMedia", 12),
          ("voiceData", 4))
    )


_SwitchIfService_Type.__name__ = "Integer32"
_SwitchIfService_Object = MibTableColumn
switchIfService = _SwitchIfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 6),
    _SwitchIfService_Type()
)
switchIfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfService.setStatus("mandatory")


class _SwitchIfAdmStatus_Type(Integer32):
    """Custom type switchIfAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("added", 6),
          ("deleted", 7),
          ("down", 2),
          ("up", 1))
    )


_SwitchIfAdmStatus_Type.__name__ = "Integer32"
_SwitchIfAdmStatus_Object = MibTableColumn
switchIfAdmStatus = _SwitchIfAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 7),
    _SwitchIfAdmStatus_Type()
)
switchIfAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfAdmStatus.setStatus("mandatory")


class _SwitchIfOperStatus_Type(Integer32):
    """Custom type switchIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("added", 6),
          ("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_SwitchIfOperStatus_Type.__name__ = "Integer32"
_SwitchIfOperStatus_Object = MibTableColumn
switchIfOperStatus = _SwitchIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 8),
    _SwitchIfOperStatus_Type()
)
switchIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOperStatus.setStatus("mandatory")
_SwitchIfPhysPort_Type = Integer32
_SwitchIfPhysPort_Object = MibTableColumn
switchIfPhysPort = _SwitchIfPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 9),
    _SwitchIfPhysPort_Type()
)
switchIfPhysPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfPhysPort.setStatus("mandatory")
_SwitchIfPartiId_Type = Integer32
_SwitchIfPartiId_Object = MibTableColumn
switchIfPartiId = _SwitchIfPartiId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 10),
    _SwitchIfPartiId_Type()
)
switchIfPartiId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfPartiId.setStatus("mandatory")
_SwitchIfCtrlerId_Type = Integer32
_SwitchIfCtrlerId_Object = MibTableColumn
switchIfCtrlerId = _SwitchIfCtrlerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 1, 1, 1, 11),
    _SwitchIfCtrlerId_Type()
)
switchIfCtrlerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchIfCtrlerId.setStatus("mandatory")
_SwitchServiceObjects_ObjectIdentity = ObjectIdentity
switchServiceObjects = _SwitchServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2)
)
_FrServiceObjects_ObjectIdentity = ObjectIdentity
frServiceObjects = _FrServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1)
)
_FrLportCnfTable_Object = MibTable
frLportCnfTable = _FrLportCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frLportCnfTable.setStatus("mandatory")
_FrLportCnfEntry_Object = MibTableRow
frLportCnfEntry = _FrLportCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1)
)
frLportCnfEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frLportSlotIndex"),
    (0, "STRATACOM-MIB", "frLportPortIndex"),
)
if mibBuilder.loadTexts:
    frLportCnfEntry.setStatus("mandatory")


class _FrLportSlotIndex_Type(Integer32):
    """Custom type frLportSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrLportSlotIndex_Type.__name__ = "Integer32"
_FrLportSlotIndex_Object = MibTableColumn
frLportSlotIndex = _FrLportSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 1),
    _FrLportSlotIndex_Type()
)
frLportSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSlotIndex.setStatus("mandatory")


class _FrLportPortIndex_Type(Integer32):
    """Custom type frLportPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrLportPortIndex_Type.__name__ = "Integer32"
_FrLportPortIndex_Object = MibTableColumn
frLportPortIndex = _FrLportPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 2),
    _FrLportPortIndex_Type()
)
frLportPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortIndex.setStatus("mandatory")
_FrLportPortDLCI_Type = Integer32
_FrLportPortDLCI_Object = MibTableColumn
frLportPortDLCI = _FrLportPortDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 3),
    _FrLportPortDLCI_Type()
)
frLportPortDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortDLCI.setStatus("mandatory")


class _FrLportAdminStatus_Type(Integer32):
    """Custom type frLportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("add", 5),
          ("delete", 6),
          ("down", 2),
          ("modify", 3),
          ("up", 1),
          ("writeOnly", 4))
    )


_FrLportAdminStatus_Type.__name__ = "Integer32"
_FrLportAdminStatus_Object = MibTableColumn
frLportAdminStatus = _FrLportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 4),
    _FrLportAdminStatus_Type()
)
frLportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAdminStatus.setStatus("mandatory")


class _FrLportOperStatus_Type(Integer32):
    """Custom type frLportOperStatus based on Integer32"""
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
        *(("active", 2),
          ("failed", 4),
          ("inActive", 1),
          ("looped", 3),
          ("unknown", 5))
    )


_FrLportOperStatus_Type.__name__ = "Integer32"
_FrLportOperStatus_Object = MibTableColumn
frLportOperStatus = _FrLportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 5),
    _FrLportOperStatus_Type()
)
frLportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportOperStatus.setStatus("mandatory")
_FrLportPortSpeed_Type = Integer32
_FrLportPortSpeed_Object = MibTableColumn
frLportPortSpeed = _FrLportPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 6),
    _FrLportPortSpeed_Type()
)
frLportPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPortSpeed.setStatus("mandatory")


class _FrLportClockType_Type(Integer32):
    """Custom type frLportClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("looped", 2),
          ("none", 3),
          ("normal", 1))
    )


_FrLportClockType_Type.__name__ = "Integer32"
_FrLportClockType_Object = MibTableColumn
frLportClockType = _FrLportClockType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 7),
    _FrLportClockType_Type()
)
frLportClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportClockType.setStatus("mandatory")


class _FrLportPortType_Type(Integer32):
    """Custom type frLportPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fr", 1))
    )


_FrLportPortType_Type.__name__ = "Integer32"
_FrLportPortType_Object = MibTableColumn
frLportPortType = _FrLportPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 8),
    _FrLportPortType_Type()
)
frLportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportPortType.setStatus("mandatory")


class _FrLportVcCount_Type(Integer32):
    """Custom type frLportVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 252),
    )


_FrLportVcCount_Type.__name__ = "Integer32"
_FrLportVcCount_Object = MibTableColumn
frLportVcCount = _FrLportVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 9),
    _FrLportVcCount_Type()
)
frLportVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportVcCount.setStatus("mandatory")
_FrLportFirstVcPtr_Type = ObjectIdentifier
_FrLportFirstVcPtr_Object = MibTableColumn
frLportFirstVcPtr = _FrLportFirstVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 10),
    _FrLportFirstVcPtr_Type()
)
frLportFirstVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportFirstVcPtr.setStatus("mandatory")
_FrLportAggrChCnt_Type = Integer32
_FrLportAggrChCnt_Object = MibTableColumn
frLportAggrChCnt = _FrLportAggrChCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 11),
    _FrLportAggrChCnt_Type()
)
frLportAggrChCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAggrChCnt.setStatus("mandatory")


class _FrLportChSpeed_Type(Integer32):
    """Custom type frLportChSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("s56k", 1),
          ("s64k", 2))
    )


_FrLportChSpeed_Type.__name__ = "Integer32"
_FrLportChSpeed_Object = MibTableColumn
frLportChSpeed = _FrLportChSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 12),
    _FrLportChSpeed_Type()
)
frLportChSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportChSpeed.setStatus("mandatory")


class _FrLportMaxTxQDepth_Type(Integer32):
    """Custom type frLportMaxTxQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLportMaxTxQDepth_Type.__name__ = "Integer32"
_FrLportMaxTxQDepth_Object = MibTableColumn
frLportMaxTxQDepth = _FrLportMaxTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 13),
    _FrLportMaxTxQDepth_Type()
)
frLportMaxTxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMaxTxQDepth.setStatus("mandatory")


class _FrLportECNQThresh_Type(Integer32):
    """Custom type frLportECNQThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLportECNQThresh_Type.__name__ = "Integer32"
_FrLportECNQThresh_Object = MibTableColumn
frLportECNQThresh = _FrLportECNQThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 14),
    _FrLportECNQThresh_Type()
)
frLportECNQThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportECNQThresh.setStatus("mandatory")


class _FrLportDEThresh_Type(Integer32):
    """Custom type frLportDEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrLportDEThresh_Type.__name__ = "Integer32"
_FrLportDEThresh_Object = MibTableColumn
frLportDEThresh = _FrLportDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 15),
    _FrLportDEThresh_Type()
)
frLportDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportDEThresh.setStatus("mandatory")


class _FrLportIDEMap_Type(Integer32):
    """Custom type frLportIDEMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportIDEMap_Type.__name__ = "Integer32"
_FrLportIDEMap_Object = MibTableColumn
frLportIDEMap = _FrLportIDEMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 16),
    _FrLportIDEMap_Type()
)
frLportIDEMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportIDEMap.setStatus("mandatory")


class _FrLportSigProt_Type(Integer32):
    """Custom type frLportSigProt based on Integer32"""
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
        *(("auto-det", 9),
          ("disabled", 3),
          ("lmi-asyn", 2),
          ("lmi-noasyn", 4),
          ("nni-annexA", 7),
          ("nni-annexD", 8),
          ("uni-annexA", 5),
          ("uni-annexD", 6),
          ("xdisabled", 1))
    )


_FrLportSigProt_Type.__name__ = "Integer32"
_FrLportSigProt_Object = MibTableColumn
frLportSigProt = _FrLportSigProt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 17),
    _FrLportSigProt_Type()
)
frLportSigProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportSigProt.setStatus("mandatory")


class _FrLportNNIStatus_Type(Integer32):
    """Custom type frLportNNIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportNNIStatus_Type.__name__ = "Integer32"
_FrLportNNIStatus_Object = MibTableColumn
frLportNNIStatus = _FrLportNNIStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 18),
    _FrLportNNIStatus_Type()
)
frLportNNIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportNNIStatus.setStatus("mandatory")


class _FrLportAsynStatus_Type(Integer32):
    """Custom type frLportAsynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportAsynStatus_Type.__name__ = "Integer32"
_FrLportAsynStatus_Object = MibTableColumn
frLportAsynStatus = _FrLportAsynStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 19),
    _FrLportAsynStatus_Type()
)
frLportAsynStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportAsynStatus.setStatus("mandatory")


class _FrLportPolVerTmr_Type(Integer32):
    """Custom type frLportPolVerTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrLportPolVerTmr_Type.__name__ = "Integer32"
_FrLportPolVerTmr_Object = MibTableColumn
frLportPolVerTmr = _FrLportPolVerTmr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 20),
    _FrLportPolVerTmr_Type()
)
frLportPolVerTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPolVerTmr.setStatus("mandatory")


class _FrLportErrThresh_Type(Integer32):
    """Custom type frLportErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLportErrThresh_Type.__name__ = "Integer32"
_FrLportErrThresh_Object = MibTableColumn
frLportErrThresh = _FrLportErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 21),
    _FrLportErrThresh_Type()
)
frLportErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportErrThresh.setStatus("mandatory")


class _FrLportMonEveCnt_Type(Integer32):
    """Custom type frLportMonEveCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLportMonEveCnt_Type.__name__ = "Integer32"
_FrLportMonEveCnt_Object = MibTableColumn
frLportMonEveCnt = _FrLportMonEveCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 22),
    _FrLportMonEveCnt_Type()
)
frLportMonEveCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMonEveCnt.setStatus("mandatory")


class _FrLportCommPri_Type(Integer32):
    """Custom type frLportCommPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrLportCommPri_Type.__name__ = "Integer32"
_FrLportCommPri_Object = MibTableColumn
frLportCommPri = _FrLportCommPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 23),
    _FrLportCommPri_Type()
)
frLportCommPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportCommPri.setStatus("mandatory")


class _FrLportUpRNR_Type(Integer32):
    """Custom type frLportUpRNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrLportUpRNR_Type.__name__ = "Integer32"
_FrLportUpRNR_Object = MibTableColumn
frLportUpRNR = _FrLportUpRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 24),
    _FrLportUpRNR_Type()
)
frLportUpRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportUpRNR.setStatus("mandatory")


class _FrLportLowRNR_Type(Integer32):
    """Custom type frLportLowRNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrLportLowRNR_Type.__name__ = "Integer32"
_FrLportLowRNR_Object = MibTableColumn
frLportLowRNR = _FrLportLowRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 25),
    _FrLportLowRNR_Type()
)
frLportLowRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportLowRNR.setStatus("mandatory")


class _FrLportMinFrmFlgs_Type(Integer32):
    """Custom type frLportMinFrmFlgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLportMinFrmFlgs_Type.__name__ = "Integer32"
_FrLportMinFrmFlgs_Object = MibTableColumn
frLportMinFrmFlgs = _FrLportMinFrmFlgs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 26),
    _FrLportMinFrmFlgs_Type()
)
frLportMinFrmFlgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportMinFrmFlgs.setStatus("mandatory")


class _FrLportOamThresh_Type(Integer32):
    """Custom type frLportOamThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrLportOamThresh_Type.__name__ = "Integer32"
_FrLportOamThresh_Object = MibTableColumn
frLportOamThresh = _FrLportOamThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 27),
    _FrLportOamThresh_Type()
)
frLportOamThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportOamThresh.setStatus("mandatory")


class _FrLportLinkTimer_Type(Integer32):
    """Custom type frLportLinkTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrLportLinkTimer_Type.__name__ = "Integer32"
_FrLportLinkTimer_Object = MibTableColumn
frLportLinkTimer = _FrLportLinkTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 28),
    _FrLportLinkTimer_Type()
)
frLportLinkTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportLinkTimer.setStatus("mandatory")


class _FrLportPollCycle_Type(Integer32):
    """Custom type frLportPollCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLportPollCycle_Type.__name__ = "Integer32"
_FrLportPollCycle_Object = MibTableColumn
frLportPollCycle = _FrLportPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 29),
    _FrLportPollCycle_Type()
)
frLportPollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportPollCycle.setStatus("mandatory")
_FrLportCLLMTimer_Type = Integer32
_FrLportCLLMTimer_Object = MibTableColumn
frLportCLLMTimer = _FrLportCLLMTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 30),
    _FrLportCLLMTimer_Type()
)
frLportCLLMTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportCLLMTimer.setStatus("mandatory")


class _FrLportEFCItoBECN_Type(Integer32):
    """Custom type frLportEFCItoBECN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_FrLportEFCItoBECN_Type.__name__ = "Integer32"
_FrLportEFCItoBECN_Object = MibTableColumn
frLportEFCItoBECN = _FrLportEFCItoBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 31),
    _FrLportEFCItoBECN_Type()
)
frLportEFCItoBECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportEFCItoBECN.setStatus("mandatory")


class _FrLportSrRTS_Type(Integer32):
    """Custom type frLportSrRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 1),
          ("on", 2))
    )


_FrLportSrRTS_Type.__name__ = "Integer32"
_FrLportSrRTS_Object = MibTableColumn
frLportSrRTS = _FrLportSrRTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 32),
    _FrLportSrRTS_Type()
)
frLportSrRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrRTS.setStatus("mandatory")


class _FrLportSrDTR_Type(Integer32):
    """Custom type frLportSrDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 1),
          ("on", 2))
    )


_FrLportSrDTR_Type.__name__ = "Integer32"
_FrLportSrDTR_Object = MibTableColumn
frLportSrDTR = _FrLportSrDTR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 33),
    _FrLportSrDTR_Type()
)
frLportSrDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDTR.setStatus("mandatory")


class _FrLportSrDCD_Type(Integer32):
    """Custom type frLportSrDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 1),
          ("on", 2))
    )


_FrLportSrDCD_Type.__name__ = "Integer32"
_FrLportSrDCD_Object = MibTableColumn
frLportSrDCD = _FrLportSrDCD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 34),
    _FrLportSrDCD_Type()
)
frLportSrDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDCD.setStatus("mandatory")


class _FrLportSrCTS_Type(Integer32):
    """Custom type frLportSrCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 1),
          ("on", 2))
    )


_FrLportSrCTS_Type.__name__ = "Integer32"
_FrLportSrCTS_Object = MibTableColumn
frLportSrCTS = _FrLportSrCTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 35),
    _FrLportSrCTS_Type()
)
frLportSrCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrCTS.setStatus("mandatory")


class _FrLportSrDSR_Type(Integer32):
    """Custom type frLportSrDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 1),
          ("on", 2))
    )


_FrLportSrDSR_Type.__name__ = "Integer32"
_FrLportSrDSR_Object = MibTableColumn
frLportSrDSR = _FrLportSrDSR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 36),
    _FrLportSrDSR_Type()
)
frLportSrDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSrDSR.setStatus("mandatory")


class _FrLportLoopBack_Type(Integer32):
    """Custom type frLportLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("none", 1))
    )


_FrLportLoopBack_Type.__name__ = "Integer32"
_FrLportLoopBack_Object = MibTableColumn
frLportLoopBack = _FrLportLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 37),
    _FrLportLoopBack_Type()
)
frLportLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLoopBack.setStatus("mandatory")


class _FrLportExtConFail_Type(Integer32):
    """Custom type frLportExtConFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrLportExtConFail_Type.__name__ = "Integer32"
_FrLportExtConFail_Object = MibTableColumn
frLportExtConFail = _FrLportExtConFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 1, 1, 38),
    _FrLportExtConFail_Type()
)
frLportExtConFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportExtConFail.setStatus("mandatory")
_FrLportStatTable_Object = MibTable
frLportStatTable = _FrLportStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    frLportStatTable.setStatus("mandatory")
_FrLportStatEntry_Object = MibTableRow
frLportStatEntry = _FrLportStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1)
)
frLportStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frLportSlotIndex"),
    (0, "STRATACOM-MIB", "frLportPortIndex"),
)
if mibBuilder.loadTexts:
    frLportStatEntry.setStatus("mandatory")
_FrLportRxBytes_Type = Counter32
_FrLportRxBytes_Object = MibTableColumn
frLportRxBytes = _FrLportRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 1),
    _FrLportRxBytes_Type()
)
frLportRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportRxBytes.setStatus("mandatory")
_FrLportRxFrms_Type = Counter32
_FrLportRxFrms_Object = MibTableColumn
frLportRxFrms = _FrLportRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 2),
    _FrLportRxFrms_Type()
)
frLportRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportRxFrms.setStatus("mandatory")
_FrLportTxBytes_Type = Counter32
_FrLportTxBytes_Object = MibTableColumn
frLportTxBytes = _FrLportTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 3),
    _FrLportTxBytes_Type()
)
frLportTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxBytes.setStatus("mandatory")
_FrLportTxFrms_Type = Counter32
_FrLportTxFrms_Object = MibTableColumn
frLportTxFrms = _FrLportTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 4),
    _FrLportTxFrms_Type()
)
frLportTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrms.setStatus("mandatory")
_FrLportTxFrmsFecns_Type = Counter32
_FrLportTxFrmsFecns_Object = MibTableColumn
frLportTxFrmsFecns = _FrLportTxFrmsFecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 5),
    _FrLportTxFrmsFecns_Type()
)
frLportTxFrmsFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrmsFecns.setStatus("mandatory")
_FrLportTxFrmsBecns_Type = Counter32
_FrLportTxFrmsBecns_Object = MibTableColumn
frLportTxFrmsBecns = _FrLportTxFrmsBecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 6),
    _FrLportTxFrmsBecns_Type()
)
frLportTxFrmsBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportTxFrmsBecns.setStatus("mandatory")
_FrLportCrcErrors_Type = Counter32
_FrLportCrcErrors_Object = MibTableColumn
frLportCrcErrors = _FrLportCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 7),
    _FrLportCrcErrors_Type()
)
frLportCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCrcErrors.setStatus("mandatory")
_FrLportBadFmts_Type = Counter32
_FrLportBadFmts_Object = MibTableColumn
frLportBadFmts = _FrLportBadFmts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 8),
    _FrLportBadFmts_Type()
)
frLportBadFmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportBadFmts.setStatus("mandatory")
_FrLportAlgnErrors_Type = Counter32
_FrLportAlgnErrors_Object = MibTableColumn
frLportAlgnErrors = _FrLportAlgnErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 9),
    _FrLportAlgnErrors_Type()
)
frLportAlgnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportAlgnErrors.setStatus("mandatory")
_FrLportIllegLengths_Type = Counter32
_FrLportIllegLengths_Object = MibTableColumn
frLportIllegLengths = _FrLportIllegLengths_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 10),
    _FrLportIllegLengths_Type()
)
frLportIllegLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportIllegLengths.setStatus("mandatory")
_FrLportDmaOvruns_Type = Counter32
_FrLportDmaOvruns_Object = MibTableColumn
frLportDmaOvruns = _FrLportDmaOvruns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 11),
    _FrLportDmaOvruns_Type()
)
frLportDmaOvruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDmaOvruns.setStatus("mandatory")
_FrLportStatEnqUnis_Type = Counter32
_FrLportStatEnqUnis_Object = MibTableColumn
frLportStatEnqUnis = _FrLportStatEnqUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 12),
    _FrLportStatEnqUnis_Type()
)
frLportStatEnqUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatEnqUnis.setStatus("mandatory")
_FrLportStatTxUnis_Type = Counter32
_FrLportStatTxUnis_Object = MibTableColumn
frLportStatTxUnis = _FrLportStatTxUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 13),
    _FrLportStatTxUnis_Type()
)
frLportStatTxUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatTxUnis.setStatus("mandatory")
_FrLportUpdtTxUnis_Type = Counter32
_FrLportUpdtTxUnis_Object = MibTableColumn
frLportUpdtTxUnis = _FrLportUpdtTxUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 14),
    _FrLportUpdtTxUnis_Type()
)
frLportUpdtTxUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUpdtTxUnis.setStatus("mandatory")
_FrLportInvldReqCnts_Type = Counter32
_FrLportInvldReqCnts_Object = MibTableColumn
frLportInvldReqCnts = _FrLportInvldReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 15),
    _FrLportInvldReqCnts_Type()
)
frLportInvldReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportInvldReqCnts.setStatus("mandatory")
_FrLportToutCntUnis_Type = Counter32
_FrLportToutCntUnis_Object = MibTableColumn
frLportToutCntUnis = _FrLportToutCntUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 16),
    _FrLportToutCntUnis_Type()
)
frLportToutCntUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportToutCntUnis.setStatus("mandatory")
_FrLportSeqnmErrUnis_Type = Counter32
_FrLportSeqnmErrUnis_Object = MibTableColumn
frLportSeqnmErrUnis = _FrLportSeqnmErrUnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 17),
    _FrLportSeqnmErrUnis_Type()
)
frLportSeqnmErrUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSeqnmErrUnis.setStatus("mandatory")
_FrLportUnknDlcis_Type = Counter32
_FrLportUnknDlcis_Object = MibTableColumn
frLportUnknDlcis = _FrLportUnknDlcis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 18),
    _FrLportUnknDlcis_Type()
)
frLportUnknDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUnknDlcis.setStatus("mandatory")
_FrLportDeFrmsDrops_Type = Counter32
_FrLportDeFrmsDrops_Object = MibTableColumn
frLportDeFrmsDrops = _FrLportDeFrmsDrops_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 19),
    _FrLportDeFrmsDrops_Type()
)
frLportDeFrmsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDeFrmsDrops.setStatus("mandatory")
_FrLportStatEnqNnis_Type = Counter32
_FrLportStatEnqNnis_Object = MibTableColumn
frLportStatEnqNnis = _FrLportStatEnqNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 20),
    _FrLportStatEnqNnis_Type()
)
frLportStatEnqNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatEnqNnis.setStatus("mandatory")
_FrLportStatRxNnis_Type = Counter32
_FrLportStatRxNnis_Object = MibTableColumn
frLportStatRxNnis = _FrLportStatRxNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 21),
    _FrLportStatRxNnis_Type()
)
frLportStatRxNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportStatRxNnis.setStatus("mandatory")
_FrLportUpdtRxNnis_Type = Counter32
_FrLportUpdtRxNnis_Object = MibTableColumn
frLportUpdtRxNnis = _FrLportUpdtRxNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 22),
    _FrLportUpdtRxNnis_Type()
)
frLportUpdtRxNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportUpdtRxNnis.setStatus("mandatory")
_FrLportToutCntNnis_Type = Counter32
_FrLportToutCntNnis_Object = MibTableColumn
frLportToutCntNnis = _FrLportToutCntNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 23),
    _FrLportToutCntNnis_Type()
)
frLportToutCntNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportToutCntNnis.setStatus("mandatory")
_FrLportSeqnmErrNnis_Type = Counter32
_FrLportSeqnmErrNnis_Object = MibTableColumn
frLportSeqnmErrNnis = _FrLportSeqnmErrNnis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 24),
    _FrLportSeqnmErrNnis_Type()
)
frLportSeqnmErrNnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportSeqnmErrNnis.setStatus("mandatory")
_FrLportCllmTxFrms_Type = Counter32
_FrLportCllmTxFrms_Object = MibTableColumn
frLportCllmTxFrms = _FrLportCllmTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 25),
    _FrLportCllmTxFrms_Type()
)
frLportCllmTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmTxFrms.setStatus("mandatory")
_FrLportCllmTxBytes_Type = Counter32
_FrLportCllmTxBytes_Object = MibTableColumn
frLportCllmTxBytes = _FrLportCllmTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 26),
    _FrLportCllmTxBytes_Type()
)
frLportCllmTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmTxBytes.setStatus("mandatory")
_FrLportCllmRxFrms_Type = Counter32
_FrLportCllmRxFrms_Object = MibTableColumn
frLportCllmRxFrms = _FrLportCllmRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 27),
    _FrLportCllmRxFrms_Type()
)
frLportCllmRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmRxFrms.setStatus("mandatory")
_FrLportCllmRxBytes_Type = Counter32
_FrLportCllmRxBytes_Object = MibTableColumn
frLportCllmRxBytes = _FrLportCllmRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 28),
    _FrLportCllmRxBytes_Type()
)
frLportCllmRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmRxBytes.setStatus("mandatory")
_FrLportCllmFailures_Type = Counter32
_FrLportCllmFailures_Object = MibTableColumn
frLportCllmFailures = _FrLportCllmFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 29),
    _FrLportCllmFailures_Type()
)
frLportCllmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportCllmFailures.setStatus("mandatory")
_FrLportDscdQTxFrms_Type = Counter32
_FrLportDscdQTxFrms_Object = MibTableColumn
frLportDscdQTxFrms = _FrLportDscdQTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 30),
    _FrLportDscdQTxFrms_Type()
)
frLportDscdQTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDscdQTxFrms.setStatus("mandatory")
_FrLportDscdQTxBytes_Type = Counter32
_FrLportDscdQTxBytes_Object = MibTableColumn
frLportDscdQTxBytes = _FrLportDscdQTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 31),
    _FrLportDscdQTxBytes_Type()
)
frLportDscdQTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDscdQTxBytes.setStatus("mandatory")
_FrLportLmiFailFrms_Type = Counter32
_FrLportLmiFailFrms_Object = MibTableColumn
frLportLmiFailFrms = _FrLportLmiFailFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 32),
    _FrLportLmiFailFrms_Type()
)
frLportLmiFailFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLmiFailFrms.setStatus("mandatory")
_FrLportLmiFailBytes_Type = Counter32
_FrLportLmiFailBytes_Object = MibTableColumn
frLportLmiFailBytes = _FrLportLmiFailBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 1, 2, 1, 33),
    _FrLportLmiFailBytes_Type()
)
frLportLmiFailBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLmiFailBytes.setStatus("mandatory")
_AtmServiceObjects_ObjectIdentity = ObjectIdentity
atmServiceObjects = _AtmServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2)
)
_AtmPortTable_Object = MibTable
atmPortTable = _AtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmPortTable.setStatus("mandatory")
_AtmPortEntry_Object = MibTableRow
atmPortEntry = _AtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1)
)
atmPortEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
)
if mibBuilder.loadTexts:
    atmPortEntry.setStatus("mandatory")


class _AtmPortSlot_Type(Integer32):
    """Custom type atmPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmPortSlot_Type.__name__ = "Integer32"
_AtmPortSlot_Object = MibTableColumn
atmPortSlot = _AtmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 1),
    _AtmPortSlot_Type()
)
atmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSlot.setStatus("mandatory")


class _AtmPortPort_Type(Integer32):
    """Custom type atmPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtmPortPort_Type.__name__ = "Integer32"
_AtmPortPort_Object = MibTableColumn
atmPortPort = _AtmPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 2),
    _AtmPortPort_Type()
)
atmPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortPort.setStatus("mandatory")


class _AtmPortAdminStatus_Type(Integer32):
    """Custom type atmPortAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("modify", 3),
          ("up", 1),
          ("writeOnly", 4))
    )


_AtmPortAdminStatus_Type.__name__ = "Integer32"
_AtmPortAdminStatus_Object = MibTableColumn
atmPortAdminStatus = _AtmPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 3),
    _AtmPortAdminStatus_Type()
)
atmPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAdminStatus.setStatus("mandatory")


class _AtmPortOperStatus_Type(Integer32):
    """Custom type atmPortOperStatus based on Integer32"""
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
        *(("active", 2),
          ("failed", 4),
          ("inactive", 1),
          ("looped", 3),
          ("unknown", 5))
    )


_AtmPortOperStatus_Type.__name__ = "Integer32"
_AtmPortOperStatus_Object = MibTableColumn
atmPortOperStatus = _AtmPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 4),
    _AtmPortOperStatus_Type()
)
atmPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortOperStatus.setStatus("mandatory")


class _AtmPortType_Type(Integer32):
    """Custom type atmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_AtmPortType_Type.__name__ = "Integer32"
_AtmPortType_Object = MibTableColumn
atmPortType = _AtmPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 5),
    _AtmPortType_Type()
)
atmPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortType.setStatus("mandatory")


class _AtmPortIfType_Type(Integer32):
    """Custom type atmPortIfType based on Integer32"""
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
        *(("e3", 3),
          ("oc3-mmf", 5),
          ("oc3-smf", 4),
          ("t3", 2),
          ("unknown", 1))
    )


_AtmPortIfType_Type.__name__ = "Integer32"
_AtmPortIfType_Object = MibTableColumn
atmPortIfType = _AtmPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 6),
    _AtmPortIfType_Type()
)
atmPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortIfType.setStatus("mandatory")
_AtmPortSpeed_Type = Integer32
_AtmPortSpeed_Object = MibTableColumn
atmPortSpeed = _AtmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 7),
    _AtmPortSpeed_Type()
)
atmPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortSpeed.setStatus("mandatory")


class _AtmPortAxis_Type(Integer32):
    """Custom type atmPortAxis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("none", 1),
          ("t1", 2))
    )


_AtmPortAxis_Type.__name__ = "Integer32"
_AtmPortAxis_Object = MibTableColumn
atmPortAxis = _AtmPortAxis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 8),
    _AtmPortAxis_Type()
)
atmPortAxis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortAxis.setStatus("mandatory")


class _AtmPortVcCount_Type(Integer32):
    """Custom type atmPortVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AtmPortVcCount_Type.__name__ = "Integer32"
_AtmPortVcCount_Object = MibTableColumn
atmPortVcCount = _AtmPortVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 9),
    _AtmPortVcCount_Type()
)
atmPortVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortVcCount.setStatus("mandatory")
_AtmPortFirstVcPtr_Type = ObjectIdentifier
_AtmPortFirstVcPtr_Object = MibTableColumn
atmPortFirstVcPtr = _AtmPortFirstVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 10),
    _AtmPortFirstVcPtr_Type()
)
atmPortFirstVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortFirstVcPtr.setStatus("mandatory")


class _AtmPortMetro_Type(Integer32):
    """Custom type atmPortMetro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmPortMetro_Type.__name__ = "Integer32"
_AtmPortMetro_Object = MibTableColumn
atmPortMetro = _AtmPortMetro_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 11),
    _AtmPortMetro_Type()
)
atmPortMetro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortMetro.setStatus("mandatory")


class _AtmPortMgmtProto_Type(Integer32):
    """Custom type atmPortMgmtProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ilmi", 3),
          ("lmi", 2),
          ("none", 1))
    )


_AtmPortMgmtProto_Type.__name__ = "Integer32"
_AtmPortMgmtProto_Object = MibTableColumn
atmPortMgmtProto = _AtmPortMgmtProto_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 12),
    _AtmPortMgmtProto_Type()
)
atmPortMgmtProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortMgmtProto.setStatus("mandatory")


class _AtmPortIlmiVpi_Type(Integer32):
    """Custom type atmPortIlmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmPortIlmiVpi_Type.__name__ = "Integer32"
_AtmPortIlmiVpi_Object = MibTableColumn
atmPortIlmiVpi = _AtmPortIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 13),
    _AtmPortIlmiVpi_Type()
)
atmPortIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiVpi.setStatus("mandatory")


class _AtmPortIlmiVci_Type(Integer32):
    """Custom type atmPortIlmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmPortIlmiVci_Type.__name__ = "Integer32"
_AtmPortIlmiVci_Object = MibTableColumn
atmPortIlmiVci = _AtmPortIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 14),
    _AtmPortIlmiVci_Type()
)
atmPortIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiVci.setStatus("mandatory")


class _AtmPortIlmiPollEnable_Type(Integer32):
    """Custom type atmPortIlmiPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmPortIlmiPollEnable_Type.__name__ = "Integer32"
_AtmPortIlmiPollEnable_Object = MibTableColumn
atmPortIlmiPollEnable = _AtmPortIlmiPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 15),
    _AtmPortIlmiPollEnable_Type()
)
atmPortIlmiPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiPollEnable.setStatus("mandatory")


class _AtmPortIlmiTrapEnable_Type(Integer32):
    """Custom type atmPortIlmiTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmPortIlmiTrapEnable_Type.__name__ = "Integer32"
_AtmPortIlmiTrapEnable_Object = MibTableColumn
atmPortIlmiTrapEnable = _AtmPortIlmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 16),
    _AtmPortIlmiTrapEnable_Type()
)
atmPortIlmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiTrapEnable.setStatus("mandatory")


class _AtmPortIlmiPollIntrvl_Type(Integer32):
    """Custom type atmPortIlmiPollIntrvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_AtmPortIlmiPollIntrvl_Type.__name__ = "Integer32"
_AtmPortIlmiPollIntrvl_Object = MibTableColumn
atmPortIlmiPollIntrvl = _AtmPortIlmiPollIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 17),
    _AtmPortIlmiPollIntrvl_Type()
)
atmPortIlmiPollIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiPollIntrvl.setStatus("mandatory")


class _AtmPortIlmiErrorThresh_Type(Integer32):
    """Custom type atmPortIlmiErrorThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortIlmiErrorThresh_Type.__name__ = "Integer32"
_AtmPortIlmiErrorThresh_Object = MibTableColumn
atmPortIlmiErrorThresh = _AtmPortIlmiErrorThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 18),
    _AtmPortIlmiErrorThresh_Type()
)
atmPortIlmiErrorThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiErrorThresh.setStatus("mandatory")


class _AtmPortIlmiEventThresh_Type(Integer32):
    """Custom type atmPortIlmiEventThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortIlmiEventThresh_Type.__name__ = "Integer32"
_AtmPortIlmiEventThresh_Object = MibTableColumn
atmPortIlmiEventThresh = _AtmPortIlmiEventThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 19),
    _AtmPortIlmiEventThresh_Type()
)
atmPortIlmiEventThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortIlmiEventThresh.setStatus("mandatory")


class _AtmPortLmiVpi_Type(Integer32):
    """Custom type atmPortLmiVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmPortLmiVpi_Type.__name__ = "Integer32"
_AtmPortLmiVpi_Object = MibTableColumn
atmPortLmiVpi = _AtmPortLmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 20),
    _AtmPortLmiVpi_Type()
)
atmPortLmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiVpi.setStatus("mandatory")


class _AtmPortLmiVci_Type(Integer32):
    """Custom type atmPortLmiVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmPortLmiVci_Type.__name__ = "Integer32"
_AtmPortLmiVci_Object = MibTableColumn
atmPortLmiVci = _AtmPortLmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 21),
    _AtmPortLmiVci_Type()
)
atmPortLmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiVci.setStatus("mandatory")


class _AtmPortLmiPollEnable_Type(Integer32):
    """Custom type atmPortLmiPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmPortLmiPollEnable_Type.__name__ = "Integer32"
_AtmPortLmiPollEnable_Object = MibTableColumn
atmPortLmiPollEnable = _AtmPortLmiPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 22),
    _AtmPortLmiPollEnable_Type()
)
atmPortLmiPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiPollEnable.setStatus("mandatory")


class _AtmPortLmiStatEnqTimer_Type(Integer32):
    """Custom type atmPortLmiStatEnqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiStatEnqTimer_Type.__name__ = "Integer32"
_AtmPortLmiStatEnqTimer_Object = MibTableColumn
atmPortLmiStatEnqTimer = _AtmPortLmiStatEnqTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 23),
    _AtmPortLmiStatEnqTimer_Type()
)
atmPortLmiStatEnqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiStatEnqTimer.setStatus("mandatory")


class _AtmPortLmiUpdStatTimer_Type(Integer32):
    """Custom type atmPortLmiUpdStatTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiUpdStatTimer_Type.__name__ = "Integer32"
_AtmPortLmiUpdStatTimer_Object = MibTableColumn
atmPortLmiUpdStatTimer = _AtmPortLmiUpdStatTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 24),
    _AtmPortLmiUpdStatTimer_Type()
)
atmPortLmiUpdStatTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiUpdStatTimer.setStatus("mandatory")


class _AtmPortLmiStatEnqRetry_Type(Integer32):
    """Custom type atmPortLmiStatEnqRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortLmiStatEnqRetry_Type.__name__ = "Integer32"
_AtmPortLmiStatEnqRetry_Object = MibTableColumn
atmPortLmiStatEnqRetry = _AtmPortLmiStatEnqRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 25),
    _AtmPortLmiStatEnqRetry_Type()
)
atmPortLmiStatEnqRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiStatEnqRetry.setStatus("mandatory")


class _AtmPortLmiUpdStatRetry_Type(Integer32):
    """Custom type atmPortLmiUpdStatRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmPortLmiUpdStatRetry_Type.__name__ = "Integer32"
_AtmPortLmiUpdStatRetry_Object = MibTableColumn
atmPortLmiUpdStatRetry = _AtmPortLmiUpdStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 26),
    _AtmPortLmiUpdStatRetry_Type()
)
atmPortLmiUpdStatRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiUpdStatRetry.setStatus("mandatory")


class _AtmPortLmiPollTimer_Type(Integer32):
    """Custom type atmPortLmiPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AtmPortLmiPollTimer_Type.__name__ = "Integer32"
_AtmPortLmiPollTimer_Object = MibTableColumn
atmPortLmiPollTimer = _AtmPortLmiPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 27),
    _AtmPortLmiPollTimer_Type()
)
atmPortLmiPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortLmiPollTimer.setStatus("mandatory")


class _AtmPortPercUtil_Type(Integer32):
    """Custom type atmPortPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmPortPercUtil_Type.__name__ = "Integer32"
_AtmPortPercUtil_Object = MibTableColumn
atmPortPercUtil = _AtmPortPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 1, 1, 28),
    _AtmPortPercUtil_Type()
)
atmPortPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortPercUtil.setStatus("mandatory")
_AtmPortQueueTable_Object = MibTable
atmPortQueueTable = _AtmPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atmPortQueueTable.setStatus("mandatory")
_AtmPortQueueEntry_Object = MibTableRow
atmPortQueueEntry = _AtmPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1)
)
atmPortQueueEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
    (0, "STRATACOM-MIB", "atmPortQueueIndex"),
)
if mibBuilder.loadTexts:
    atmPortQueueEntry.setStatus("mandatory")


class _AtmPortQueueIndex_Type(Integer32):
    """Custom type atmPortQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmPortQueueIndex_Type.__name__ = "Integer32"
_AtmPortQueueIndex_Object = MibTableColumn
atmPortQueueIndex = _AtmPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 1),
    _AtmPortQueueIndex_Type()
)
atmPortQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueIndex.setStatus("mandatory")


class _AtmPortQueueAdminStatus_Type(Integer32):
    """Custom type atmPortQueueAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modify", 1),
          ("writeOnly", 2))
    )


_AtmPortQueueAdminStatus_Type.__name__ = "Integer32"
_AtmPortQueueAdminStatus_Object = MibTableColumn
atmPortQueueAdminStatus = _AtmPortQueueAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 2),
    _AtmPortQueueAdminStatus_Type()
)
atmPortQueueAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueAdminStatus.setStatus("mandatory")


class _AtmPortQueueType_Type(Integer32):
    """Custom type atmPortQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 4),
          ("axis", 6),
          ("cbr", 3),
          ("unknown", 1),
          ("unused", 2),
          ("vbr", 5))
    )


_AtmPortQueueType_Type.__name__ = "Integer32"
_AtmPortQueueType_Object = MibTableColumn
atmPortQueueType = _AtmPortQueueType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 3),
    _AtmPortQueueType_Type()
)
atmPortQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueType.setStatus("mandatory")


class _AtmPortQueueDepth_Type(Integer32):
    """Custom type atmPortQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11000),
    )


_AtmPortQueueDepth_Type.__name__ = "Integer32"
_AtmPortQueueDepth_Object = MibTableColumn
atmPortQueueDepth = _AtmPortQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 4),
    _AtmPortQueueDepth_Type()
)
atmPortQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueDepth.setStatus("mandatory")


class _AtmPortQueueClpHi_Type(Integer32):
    """Custom type atmPortQueueClpHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueClpHi_Type.__name__ = "Integer32"
_AtmPortQueueClpHi_Object = MibTableColumn
atmPortQueueClpHi = _AtmPortQueueClpHi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 5),
    _AtmPortQueueClpHi_Type()
)
atmPortQueueClpHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueClpHi.setStatus("mandatory")


class _AtmPortQueueClpLo_Type(Integer32):
    """Custom type atmPortQueueClpLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueClpLo_Type.__name__ = "Integer32"
_AtmPortQueueClpLo_Object = MibTableColumn
atmPortQueueClpLo = _AtmPortQueueClpLo_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 6),
    _AtmPortQueueClpLo_Type()
)
atmPortQueueClpLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueClpLo.setStatus("mandatory")


class _AtmPortQueueEfciTh_Type(Integer32):
    """Custom type atmPortQueueEfciTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtmPortQueueEfciTh_Type.__name__ = "Integer32"
_AtmPortQueueEfciTh_Object = MibTableColumn
atmPortQueueEfciTh = _AtmPortQueueEfciTh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 7),
    _AtmPortQueueEfciTh_Type()
)
atmPortQueueEfciTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortQueueEfciTh.setStatus("mandatory")


class _AtmPortQueueAlgorithm_Type(Integer32):
    """Custom type atmPortQueueAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("minDelay", 6),
          ("minGuar", 4),
          ("minSmooth", 5),
          ("off", 1),
          ("ok", 3))
    )


_AtmPortQueueAlgorithm_Type.__name__ = "Integer32"
_AtmPortQueueAlgorithm_Object = MibTableColumn
atmPortQueueAlgorithm = _AtmPortQueueAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 2, 1, 8),
    _AtmPortQueueAlgorithm_Type()
)
atmPortQueueAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortQueueAlgorithm.setStatus("mandatory")
_AtmPortStatTable_Object = MibTable
atmPortStatTable = _AtmPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    atmPortStatTable.setStatus("mandatory")
_AtmPortStatEntry_Object = MibTableRow
atmPortStatEntry = _AtmPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1)
)
atmPortStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmPortSlot"),
    (0, "STRATACOM-MIB", "atmPortPort"),
)
if mibBuilder.loadTexts:
    atmPortStatEntry.setStatus("mandatory")
_AtmPortStatUnknVpiVcis_Type = Counter32
_AtmPortStatUnknVpiVcis_Object = MibTableColumn
atmPortStatUnknVpiVcis = _AtmPortStatUnknVpiVcis_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 1),
    _AtmPortStatUnknVpiVcis_Type()
)
atmPortStatUnknVpiVcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatUnknVpiVcis.setStatus("mandatory")
_AtmPortStatBufferOvfls_Type = Counter32
_AtmPortStatBufferOvfls_Object = MibTableColumn
atmPortStatBufferOvfls = _AtmPortStatBufferOvfls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 2),
    _AtmPortStatBufferOvfls_Type()
)
atmPortStatBufferOvfls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatBufferOvfls.setStatus("mandatory")
_AtmPortStatNonZeroGfcs_Type = Counter32
_AtmPortStatNonZeroGfcs_Object = MibTableColumn
atmPortStatNonZeroGfcs = _AtmPortStatNonZeroGfcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 3),
    _AtmPortStatNonZeroGfcs_Type()
)
atmPortStatNonZeroGfcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatNonZeroGfcs.setStatus("mandatory")
_AtmPortStatIsuDiscards_Type = Counter32
_AtmPortStatIsuDiscards_Object = MibTableColumn
atmPortStatIsuDiscards = _AtmPortStatIsuDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 4),
    _AtmPortStatIsuDiscards_Type()
)
atmPortStatIsuDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIsuDiscards.setStatus("mandatory")
_AtmPortStatIsuEmptys_Type = Counter32
_AtmPortStatIsuEmptys_Object = MibTableColumn
atmPortStatIsuEmptys = _AtmPortStatIsuEmptys_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 5),
    _AtmPortStatIsuEmptys_Type()
)
atmPortStatIsuEmptys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIsuEmptys.setStatus("mandatory")
_AtmPortStatAisRxs_Type = Counter32
_AtmPortStatAisRxs_Object = MibTableColumn
atmPortStatAisRxs = _AtmPortStatAisRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 6),
    _AtmPortStatAisRxs_Type()
)
atmPortStatAisRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatAisRxs.setStatus("mandatory")
_AtmPortStatFerfRxs_Type = Counter32
_AtmPortStatFerfRxs_Object = MibTableColumn
atmPortStatFerfRxs = _AtmPortStatFerfRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 7),
    _AtmPortStatFerfRxs_Type()
)
atmPortStatFerfRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatFerfRxs.setStatus("mandatory")
_AtmPortStatCellsRxs_Type = Counter32
_AtmPortStatCellsRxs_Object = MibTableColumn
atmPortStatCellsRxs = _AtmPortStatCellsRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 8),
    _AtmPortStatCellsRxs_Type()
)
atmPortStatCellsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatCellsRxs.setStatus("mandatory")
_AtmPortStatClpRxs_Type = Counter32
_AtmPortStatClpRxs_Object = MibTableColumn
atmPortStatClpRxs = _AtmPortStatClpRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 9),
    _AtmPortStatClpRxs_Type()
)
atmPortStatClpRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatClpRxs.setStatus("mandatory")
_AtmPortStatEfciRxs_Type = Counter32
_AtmPortStatEfciRxs_Object = MibTableColumn
atmPortStatEfciRxs = _AtmPortStatEfciRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 10),
    _AtmPortStatEfciRxs_Type()
)
atmPortStatEfciRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatEfciRxs.setStatus("mandatory")
_AtmPortStatBcmRxs_Type = Counter32
_AtmPortStatBcmRxs_Object = MibTableColumn
atmPortStatBcmRxs = _AtmPortStatBcmRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 11),
    _AtmPortStatBcmRxs_Type()
)
atmPortStatBcmRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatBcmRxs.setStatus("mandatory")
_AtmPortStatCellsTxs_Type = Counter32
_AtmPortStatCellsTxs_Object = MibTableColumn
atmPortStatCellsTxs = _AtmPortStatCellsTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 12),
    _AtmPortStatCellsTxs_Type()
)
atmPortStatCellsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatCellsTxs.setStatus("mandatory")
_AtmPortStatOamRxs_Type = Counter32
_AtmPortStatOamRxs_Object = MibTableColumn
atmPortStatOamRxs = _AtmPortStatOamRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 13),
    _AtmPortStatOamRxs_Type()
)
atmPortStatOamRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatOamRxs.setStatus("mandatory")
_AtmPortStatPayldErrs_Type = Counter32
_AtmPortStatPayldErrs_Object = MibTableColumn
atmPortStatPayldErrs = _AtmPortStatPayldErrs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 14),
    _AtmPortStatPayldErrs_Type()
)
atmPortStatPayldErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatPayldErrs.setStatus("mandatory")
_AtmPortStatClpTxs_Type = Counter32
_AtmPortStatClpTxs_Object = MibTableColumn
atmPortStatClpTxs = _AtmPortStatClpTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 15),
    _AtmPortStatClpTxs_Type()
)
atmPortStatClpTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatClpTxs.setStatus("mandatory")
_AtmPortStatEfciTxs_Type = Counter32
_AtmPortStatEfciTxs_Object = MibTableColumn
atmPortStatEfciTxs = _AtmPortStatEfciTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 16),
    _AtmPortStatEfciTxs_Type()
)
atmPortStatEfciTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatEfciTxs.setStatus("mandatory")
_AtmPortStatHdrDiscards_Type = Counter32
_AtmPortStatHdrDiscards_Object = MibTableColumn
atmPortStatHdrDiscards = _AtmPortStatHdrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 17),
    _AtmPortStatHdrDiscards_Type()
)
atmPortStatHdrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatHdrDiscards.setStatus("mandatory")
_AtmPortStatIlmiGetRxs_Type = Counter32
_AtmPortStatIlmiGetRxs_Object = MibTableColumn
atmPortStatIlmiGetRxs = _AtmPortStatIlmiGetRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 18),
    _AtmPortStatIlmiGetRxs_Type()
)
atmPortStatIlmiGetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRxs.setStatus("mandatory")
_AtmPortStatIlmiGetNextRxs_Type = Counter32
_AtmPortStatIlmiGetNextRxs_Object = MibTableColumn
atmPortStatIlmiGetNextRxs = _AtmPortStatIlmiGetNextRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 19),
    _AtmPortStatIlmiGetNextRxs_Type()
)
atmPortStatIlmiGetNextRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetNextRxs.setStatus("mandatory")
_AtmPortStatIlmiGetNextTxs_Type = Counter32
_AtmPortStatIlmiGetNextTxs_Object = MibTableColumn
atmPortStatIlmiGetNextTxs = _AtmPortStatIlmiGetNextTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 20),
    _AtmPortStatIlmiGetNextTxs_Type()
)
atmPortStatIlmiGetNextTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetNextTxs.setStatus("mandatory")
_AtmPortStatIlmiSetRxs_Type = Counter32
_AtmPortStatIlmiSetRxs_Object = MibTableColumn
atmPortStatIlmiSetRxs = _AtmPortStatIlmiSetRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 21),
    _AtmPortStatIlmiSetRxs_Type()
)
atmPortStatIlmiSetRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiSetRxs.setStatus("mandatory")
_AtmPortStatIlmiTrapRxs_Type = Counter32
_AtmPortStatIlmiTrapRxs_Object = MibTableColumn
atmPortStatIlmiTrapRxs = _AtmPortStatIlmiTrapRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 22),
    _AtmPortStatIlmiTrapRxs_Type()
)
atmPortStatIlmiTrapRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiTrapRxs.setStatus("mandatory")
_AtmPortStatIlmiGetRspRxs_Type = Counter32
_AtmPortStatIlmiGetRspRxs_Object = MibTableColumn
atmPortStatIlmiGetRspRxs = _AtmPortStatIlmiGetRspRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 23),
    _AtmPortStatIlmiGetRspRxs_Type()
)
atmPortStatIlmiGetRspRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRspRxs.setStatus("mandatory")
_AtmPortStatIlmiGetTxs_Type = Counter32
_AtmPortStatIlmiGetTxs_Object = MibTableColumn
atmPortStatIlmiGetTxs = _AtmPortStatIlmiGetTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 24),
    _AtmPortStatIlmiGetTxs_Type()
)
atmPortStatIlmiGetTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetTxs.setStatus("mandatory")
_AtmPortStatIlmiGetRspTxs_Type = Counter32
_AtmPortStatIlmiGetRspTxs_Object = MibTableColumn
atmPortStatIlmiGetRspTxs = _AtmPortStatIlmiGetRspTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 25),
    _AtmPortStatIlmiGetRspTxs_Type()
)
atmPortStatIlmiGetRspTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiGetRspTxs.setStatus("mandatory")
_AtmPortStatIlmiTrapTxs_Type = Counter32
_AtmPortStatIlmiTrapTxs_Object = MibTableColumn
atmPortStatIlmiTrapTxs = _AtmPortStatIlmiTrapTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 26),
    _AtmPortStatIlmiTrapTxs_Type()
)
atmPortStatIlmiTrapTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiTrapTxs.setStatus("mandatory")
_AtmPortStatIlmiUnkRxs_Type = Counter32
_AtmPortStatIlmiUnkRxs_Object = MibTableColumn
atmPortStatIlmiUnkRxs = _AtmPortStatIlmiUnkRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 27),
    _AtmPortStatIlmiUnkRxs_Type()
)
atmPortStatIlmiUnkRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatIlmiUnkRxs.setStatus("mandatory")
_AtmPortStatLmiStatTxs_Type = Counter32
_AtmPortStatLmiStatTxs_Object = MibTableColumn
atmPortStatLmiStatTxs = _AtmPortStatLmiStatTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 28),
    _AtmPortStatLmiStatTxs_Type()
)
atmPortStatLmiStatTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatTxs.setStatus("mandatory")
_AtmPortStatLmiUpdtStatTxs_Type = Counter32
_AtmPortStatLmiUpdtStatTxs_Object = MibTableColumn
atmPortStatLmiUpdtStatTxs = _AtmPortStatLmiUpdtStatTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 29),
    _AtmPortStatLmiUpdtStatTxs_Type()
)
atmPortStatLmiUpdtStatTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiUpdtStatTxs.setStatus("mandatory")
_AtmPortStatLmiStatAckTxs_Type = Counter32
_AtmPortStatLmiStatAckTxs_Object = MibTableColumn
atmPortStatLmiStatAckTxs = _AtmPortStatLmiStatAckTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 30),
    _AtmPortStatLmiStatAckTxs_Type()
)
atmPortStatLmiStatAckTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatAckTxs.setStatus("mandatory")
_AtmPortStatLmiStatEnqTxs_Type = Counter32
_AtmPortStatLmiStatEnqTxs_Object = MibTableColumn
atmPortStatLmiStatEnqTxs = _AtmPortStatLmiStatEnqTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 31),
    _AtmPortStatLmiStatEnqTxs_Type()
)
atmPortStatLmiStatEnqTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatEnqTxs.setStatus("mandatory")
_AtmPortStatLmiStatEnqRxs_Type = Counter32
_AtmPortStatLmiStatEnqRxs_Object = MibTableColumn
atmPortStatLmiStatEnqRxs = _AtmPortStatLmiStatEnqRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 32),
    _AtmPortStatLmiStatEnqRxs_Type()
)
atmPortStatLmiStatEnqRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatEnqRxs.setStatus("mandatory")
_AtmPortStatLmiStatRxs_Type = Counter32
_AtmPortStatLmiStatRxs_Object = MibTableColumn
atmPortStatLmiStatRxs = _AtmPortStatLmiStatRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 33),
    _AtmPortStatLmiStatRxs_Type()
)
atmPortStatLmiStatRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatRxs.setStatus("mandatory")
_AtmPortStatLmiUpdStatRxs_Type = Counter32
_AtmPortStatLmiUpdStatRxs_Object = MibTableColumn
atmPortStatLmiUpdStatRxs = _AtmPortStatLmiUpdStatRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 34),
    _AtmPortStatLmiUpdStatRxs_Type()
)
atmPortStatLmiUpdStatRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiUpdStatRxs.setStatus("mandatory")
_AtmPortStatLmiStatAckRxs_Type = Counter32
_AtmPortStatLmiStatAckRxs_Object = MibTableColumn
atmPortStatLmiStatAckRxs = _AtmPortStatLmiStatAckRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 2, 3, 1, 35),
    _AtmPortStatLmiStatAckRxs_Type()
)
atmPortStatLmiStatAckRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPortStatLmiStatAckRxs.setStatus("mandatory")
_VoiceServiceObjects_ObjectIdentity = ObjectIdentity
voiceServiceObjects = _VoiceServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3)
)
_VoiceChannelTable_Object = MibTable
voiceChannelTable = _VoiceChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    voiceChannelTable.setStatus("mandatory")
_VoiceChannelEntry_Object = MibTableRow
voiceChannelEntry = _VoiceChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1)
)
voiceChannelEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceChannelSlotIndex"),
    (0, "STRATACOM-MIB", "voiceChannelChannelIndex"),
)
if mibBuilder.loadTexts:
    voiceChannelEntry.setStatus("mandatory")


class _VoiceChannelSlotIndex_Type(Integer32):
    """Custom type voiceChannelSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoiceChannelSlotIndex_Type.__name__ = "Integer32"
_VoiceChannelSlotIndex_Object = MibTableColumn
voiceChannelSlotIndex = _VoiceChannelSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 1),
    _VoiceChannelSlotIndex_Type()
)
voiceChannelSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelSlotIndex.setStatus("mandatory")


class _VoiceChannelChannelIndex_Type(Integer32):
    """Custom type voiceChannelChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoiceChannelChannelIndex_Type.__name__ = "Integer32"
_VoiceChannelChannelIndex_Object = MibTableColumn
voiceChannelChannelIndex = _VoiceChannelChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 2),
    _VoiceChannelChannelIndex_Type()
)
voiceChannelChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelChannelIndex.setStatus("mandatory")


class _VoiceChannelAdminStatus_Type(Integer32):
    """Custom type voiceChannelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("modify", 2),
          ("writeOnly", 3))
    )


_VoiceChannelAdminStatus_Type.__name__ = "Integer32"
_VoiceChannelAdminStatus_Object = MibTableColumn
voiceChannelAdminStatus = _VoiceChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 3),
    _VoiceChannelAdminStatus_Type()
)
voiceChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelAdminStatus.setStatus("mandatory")
_VoiceChannelEndptPtr_Type = ObjectIdentifier
_VoiceChannelEndptPtr_Object = MibTableColumn
voiceChannelEndptPtr = _VoiceChannelEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 4),
    _VoiceChannelEndptPtr_Type()
)
voiceChannelEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelEndptPtr.setStatus("mandatory")


class _VoiceChannelIf_Type(Integer32):
    """Custom type voiceChannelIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("t1", 2),
          ("unknown", 1))
    )


_VoiceChannelIf_Type.__name__ = "Integer32"
_VoiceChannelIf_Object = MibTableColumn
voiceChannelIf = _VoiceChannelIf_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 5),
    _VoiceChannelIf_Type()
)
voiceChannelIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelIf.setStatus("mandatory")


class _VoiceChannelAdapVoice_Type(Integer32):
    """Custom type voiceChannelAdapVoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceChannelAdapVoice_Type.__name__ = "Integer32"
_VoiceChannelAdapVoice_Object = MibTableColumn
voiceChannelAdapVoice = _VoiceChannelAdapVoice_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 6),
    _VoiceChannelAdapVoice_Type()
)
voiceChannelAdapVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelAdapVoice.setStatus("mandatory")


class _VoiceChannelDialType_Type(Integer32):
    """Custom type voiceChannelDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("pulse", 2),
          ("userConfigured", 3))
    )


_VoiceChannelDialType_Type.__name__ = "Integer32"
_VoiceChannelDialType_Object = MibTableColumn
voiceChannelDialType = _VoiceChannelDialType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 7),
    _VoiceChannelDialType_Type()
)
voiceChannelDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelDialType.setStatus("mandatory")


class _VoiceChannelDtSignallingDelay_Type(Integer32):
    """Custom type voiceChannelDtSignallingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 96),
    )


_VoiceChannelDtSignallingDelay_Type.__name__ = "Integer32"
_VoiceChannelDtSignallingDelay_Object = MibTableColumn
voiceChannelDtSignallingDelay = _VoiceChannelDtSignallingDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 8),
    _VoiceChannelDtSignallingDelay_Type()
)
voiceChannelDtSignallingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelDtSignallingDelay.setStatus("mandatory")


class _VoiceChannelDtMinWink_Type(Integer32):
    """Custom type voiceChannelDtMinWink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 300),
    )


_VoiceChannelDtMinWink_Type.__name__ = "Integer32"
_VoiceChannelDtMinWink_Object = MibTableColumn
voiceChannelDtMinWink = _VoiceChannelDtMinWink_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 9),
    _VoiceChannelDtMinWink_Type()
)
voiceChannelDtMinWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelDtMinWink.setStatus("mandatory")


class _VoiceChannelDtPlayOutDelay_Type(Integer32):
    """Custom type voiceChannelDtPlayOutDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_VoiceChannelDtPlayOutDelay_Type.__name__ = "Integer32"
_VoiceChannelDtPlayOutDelay_Object = MibTableColumn
voiceChannelDtPlayOutDelay = _VoiceChannelDtPlayOutDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 10),
    _VoiceChannelDtPlayOutDelay_Type()
)
voiceChannelDtPlayOutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelDtPlayOutDelay.setStatus("mandatory")


class _VoiceChannelRecvSigABit_Type(Integer32):
    """Custom type voiceChannelRecvSigABit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelRecvSigABit_Type.__name__ = "Integer32"
_VoiceChannelRecvSigABit_Object = MibTableColumn
voiceChannelRecvSigABit = _VoiceChannelRecvSigABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 11),
    _VoiceChannelRecvSigABit_Type()
)
voiceChannelRecvSigABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelRecvSigABit.setStatus("mandatory")


class _VoiceChannelRecvSigBBit_Type(Integer32):
    """Custom type voiceChannelRecvSigBBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelRecvSigBBit_Type.__name__ = "Integer32"
_VoiceChannelRecvSigBBit_Object = MibTableColumn
voiceChannelRecvSigBBit = _VoiceChannelRecvSigBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 12),
    _VoiceChannelRecvSigBBit_Type()
)
voiceChannelRecvSigBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelRecvSigBBit.setStatus("mandatory")


class _VoiceChannelRecvSigCBit_Type(Integer32):
    """Custom type voiceChannelRecvSigCBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelRecvSigCBit_Type.__name__ = "Integer32"
_VoiceChannelRecvSigCBit_Object = MibTableColumn
voiceChannelRecvSigCBit = _VoiceChannelRecvSigCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 13),
    _VoiceChannelRecvSigCBit_Type()
)
voiceChannelRecvSigCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelRecvSigCBit.setStatus("mandatory")


class _VoiceChannelRecvSigDBit_Type(Integer32):
    """Custom type voiceChannelRecvSigDBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelRecvSigDBit_Type.__name__ = "Integer32"
_VoiceChannelRecvSigDBit_Object = MibTableColumn
voiceChannelRecvSigDBit = _VoiceChannelRecvSigDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 14),
    _VoiceChannelRecvSigDBit_Type()
)
voiceChannelRecvSigDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelRecvSigDBit.setStatus("mandatory")


class _VoiceChannelXmitSigABit_Type(Integer32):
    """Custom type voiceChannelXmitSigABit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelXmitSigABit_Type.__name__ = "Integer32"
_VoiceChannelXmitSigABit_Object = MibTableColumn
voiceChannelXmitSigABit = _VoiceChannelXmitSigABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 15),
    _VoiceChannelXmitSigABit_Type()
)
voiceChannelXmitSigABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelXmitSigABit.setStatus("mandatory")


class _VoiceChannelXmitSigBBit_Type(Integer32):
    """Custom type voiceChannelXmitSigBBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelXmitSigBBit_Type.__name__ = "Integer32"
_VoiceChannelXmitSigBBit_Object = MibTableColumn
voiceChannelXmitSigBBit = _VoiceChannelXmitSigBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 16),
    _VoiceChannelXmitSigBBit_Type()
)
voiceChannelXmitSigBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelXmitSigBBit.setStatus("mandatory")


class _VoiceChannelXmitSigCBit_Type(Integer32):
    """Custom type voiceChannelXmitSigCBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelXmitSigCBit_Type.__name__ = "Integer32"
_VoiceChannelXmitSigCBit_Object = MibTableColumn
voiceChannelXmitSigCBit = _VoiceChannelXmitSigCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 17),
    _VoiceChannelXmitSigCBit_Type()
)
voiceChannelXmitSigCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelXmitSigCBit.setStatus("mandatory")


class _VoiceChannelXmitSigDBit_Type(Integer32):
    """Custom type voiceChannelXmitSigDBit based on Integer32"""
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
        *(("donotXmit", 4),
          ("one", 2),
          ("revSigBit", 5),
          ("xmitTransparent", 3),
          ("zero", 1))
    )


_VoiceChannelXmitSigDBit_Type.__name__ = "Integer32"
_VoiceChannelXmitSigDBit_Object = MibTableColumn
voiceChannelXmitSigDBit = _VoiceChannelXmitSigDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 18),
    _VoiceChannelXmitSigDBit_Type()
)
voiceChannelXmitSigDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelXmitSigDBit.setStatus("mandatory")


class _VoiceChannelIfTypeName_Type(Integer32):
    """Custom type voiceChannelIfTypeName based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("dP0", 10),
          ("dPT", 11),
          ("dX", 15),
          ("eT0", 16),
          ("fXO", 7),
          ("fXSGS", 8),
          ("fXSLS", 9),
          ("forceSig", 4),
          ("fourWireENM", 6),
          ("noSig", 3),
          ("pLAR", 17),
          ("pLR", 18),
          ("r1", 20),
          ("r2Backward", 22),
          ("r2Forward", 23),
          ("rD", 19),
          ("rP0", 12),
          ("rPT", 13),
          ("sDP0", 14),
          ("sSDC5A", 21),
          ("twoWireENM", 5),
          ("unConfig", 2),
          ("userConfig", 1))
    )


_VoiceChannelIfTypeName_Type.__name__ = "Integer32"
_VoiceChannelIfTypeName_Object = MibTableColumn
voiceChannelIfTypeName = _VoiceChannelIfTypeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 19),
    _VoiceChannelIfTypeName_Type()
)
voiceChannelIfTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfTypeName.setStatus("mandatory")


class _VoiceChannelIfOnhkABit_Type(Integer32):
    """Custom type voiceChannelIfOnhkABit based on Integer32"""
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
        *(("donotCare", 3),
          ("notUsed", 5),
          ("one", 2),
          ("unKnown", 4),
          ("zero", 1))
    )


_VoiceChannelIfOnhkABit_Type.__name__ = "Integer32"
_VoiceChannelIfOnhkABit_Object = MibTableColumn
voiceChannelIfOnhkABit = _VoiceChannelIfOnhkABit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 20),
    _VoiceChannelIfOnhkABit_Type()
)
voiceChannelIfOnhkABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfOnhkABit.setStatus("mandatory")


class _VoiceChannelIfOnhkBBit_Type(Integer32):
    """Custom type voiceChannelIfOnhkBBit based on Integer32"""
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
        *(("donotCare", 3),
          ("notUsed", 5),
          ("one", 2),
          ("unKnown", 4),
          ("zero", 1))
    )


_VoiceChannelIfOnhkBBit_Type.__name__ = "Integer32"
_VoiceChannelIfOnhkBBit_Object = MibTableColumn
voiceChannelIfOnhkBBit = _VoiceChannelIfOnhkBBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 21),
    _VoiceChannelIfOnhkBBit_Type()
)
voiceChannelIfOnhkBBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfOnhkBBit.setStatus("mandatory")


class _VoiceChannelIfOnhkCBit_Type(Integer32):
    """Custom type voiceChannelIfOnhkCBit based on Integer32"""
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
        *(("donotCare", 3),
          ("notUsed", 5),
          ("one", 2),
          ("unKnown", 4),
          ("zero", 1))
    )


_VoiceChannelIfOnhkCBit_Type.__name__ = "Integer32"
_VoiceChannelIfOnhkCBit_Object = MibTableColumn
voiceChannelIfOnhkCBit = _VoiceChannelIfOnhkCBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 22),
    _VoiceChannelIfOnhkCBit_Type()
)
voiceChannelIfOnhkCBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfOnhkCBit.setStatus("mandatory")


class _VoiceChannelIfOnhkDBit_Type(Integer32):
    """Custom type voiceChannelIfOnhkDBit based on Integer32"""
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
        *(("donotCare", 3),
          ("notUsed", 5),
          ("one", 2),
          ("unKnown", 4),
          ("zero", 1))
    )


_VoiceChannelIfOnhkDBit_Type.__name__ = "Integer32"
_VoiceChannelIfOnhkDBit_Object = MibTableColumn
voiceChannelIfOnhkDBit = _VoiceChannelIfOnhkDBit_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 23),
    _VoiceChannelIfOnhkDBit_Type()
)
voiceChannelIfOnhkDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfOnhkDBit.setStatus("mandatory")


class _VoiceChannelIfCondIndex_Type(Integer32):
    """Custom type voiceChannelIfCondIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoiceChannelIfCondIndex_Type.__name__ = "Integer32"
_VoiceChannelIfCondIndex_Object = MibTableColumn
voiceChannelIfCondIndex = _VoiceChannelIfCondIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 24),
    _VoiceChannelIfCondIndex_Type()
)
voiceChannelIfCondIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelIfCondIndex.setStatus("mandatory")


class _VoiceChannelEchoCancel_Type(Integer32):
    """Custom type voiceChannelEchoCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VoiceChannelEchoCancel_Type.__name__ = "Integer32"
_VoiceChannelEchoCancel_Object = MibTableColumn
voiceChannelEchoCancel = _VoiceChannelEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 25),
    _VoiceChannelEchoCancel_Type()
)
voiceChannelEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelEchoCancel.setStatus("mandatory")


class _VoiceChannelEchoRtnLoss_Type(Integer32):
    """Custom type voiceChannelEchoRtnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_VoiceChannelEchoRtnLoss_Type.__name__ = "Integer32"
_VoiceChannelEchoRtnLoss_Object = MibTableColumn
voiceChannelEchoRtnLoss = _VoiceChannelEchoRtnLoss_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 26),
    _VoiceChannelEchoRtnLoss_Type()
)
voiceChannelEchoRtnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelEchoRtnLoss.setStatus("mandatory")


class _VoiceChannelEchoTone_Type(Integer32):
    """Custom type voiceChannelEchoTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VoiceChannelEchoTone_Type.__name__ = "Integer32"
_VoiceChannelEchoTone_Object = MibTableColumn
voiceChannelEchoTone = _VoiceChannelEchoTone_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 27),
    _VoiceChannelEchoTone_Type()
)
voiceChannelEchoTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelEchoTone.setStatus("mandatory")


class _VoiceChannelEchoConv_Type(Integer32):
    """Custom type voiceChannelEchoConv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VoiceChannelEchoConv_Type.__name__ = "Integer32"
_VoiceChannelEchoConv_Object = MibTableColumn
voiceChannelEchoConv = _VoiceChannelEchoConv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 28),
    _VoiceChannelEchoConv_Type()
)
voiceChannelEchoConv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelEchoConv.setStatus("mandatory")


class _VoiceChannelEchoNlp_Type(Integer32):
    """Custom type voiceChannelEchoNlp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VoiceChannelEchoNlp_Type.__name__ = "Integer32"
_VoiceChannelEchoNlp_Object = MibTableColumn
voiceChannelEchoNlp = _VoiceChannelEchoNlp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 29),
    _VoiceChannelEchoNlp_Type()
)
voiceChannelEchoNlp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelEchoNlp.setStatus("mandatory")


class _VoiceChannelInGain_Type(Integer32):
    """Custom type voiceChannelInGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_VoiceChannelInGain_Type.__name__ = "Integer32"
_VoiceChannelInGain_Object = MibTableColumn
voiceChannelInGain = _VoiceChannelInGain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 30),
    _VoiceChannelInGain_Type()
)
voiceChannelInGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelInGain.setStatus("mandatory")


class _VoiceChannelOutGain_Type(Integer32):
    """Custom type voiceChannelOutGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_VoiceChannelOutGain_Type.__name__ = "Integer32"
_VoiceChannelOutGain_Object = MibTableColumn
voiceChannelOutGain = _VoiceChannelOutGain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 31),
    _VoiceChannelOutGain_Type()
)
voiceChannelOutGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelOutGain.setStatus("mandatory")


class _VoiceChannelUtil_Type(Integer32):
    """Custom type voiceChannelUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VoiceChannelUtil_Type.__name__ = "Integer32"
_VoiceChannelUtil_Object = MibTableColumn
voiceChannelUtil = _VoiceChannelUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 3, 1, 1, 32),
    _VoiceChannelUtil_Type()
)
voiceChannelUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceChannelUtil.setStatus("mandatory")
_TrunkServiceObjects_ObjectIdentity = ObjectIdentity
trunkServiceObjects = _TrunkServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4)
)
_AtmTrunks_Object = MibTable
atmTrunks = _AtmTrunks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    atmTrunks.setStatus("mandatory")
_AtmTrkEntry_Object = MibTableRow
atmTrkEntry = _AtmTrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1)
)
atmTrkEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    atmTrkEntry.setStatus("mandatory")


class _AtmTrkStatus_Type(Integer32):
    """Custom type atmTrkStatus based on Integer32"""
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
        *(("clear", 1),
          ("deact", 5),
          ("down", 4),
          ("major", 3),
          ("minor", 2))
    )


_AtmTrkStatus_Type.__name__ = "Integer32"
_AtmTrkStatus_Object = MibTableColumn
atmTrkStatus = _AtmTrkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 1),
    _AtmTrkStatus_Type()
)
atmTrkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatus.setStatus("mandatory")


class _AtmTrkAlmEnable_Type(Integer32):
    """Custom type atmTrkAlmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmTrkAlmEnable_Type.__name__ = "Integer32"
_AtmTrkAlmEnable_Object = MibTableColumn
atmTrkAlmEnable = _AtmTrkAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 2),
    _AtmTrkAlmEnable_Type()
)
atmTrkAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkAlmEnable.setStatus("mandatory")


class _AtmTrkComStatus_Type(Integer32):
    """Custom type atmTrkComStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commFAIL", 2),
          ("commOK", 1))
    )


_AtmTrkComStatus_Type.__name__ = "Integer32"
_AtmTrkComStatus_Object = MibTableColumn
atmTrkComStatus = _AtmTrkComStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 3),
    _AtmTrkComStatus_Type()
)
atmTrkComStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkComStatus.setStatus("mandatory")
_AtmTrkRcvRate_Type = Integer32
_AtmTrkRcvRate_Object = MibTableColumn
atmTrkRcvRate = _AtmTrkRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 4),
    _AtmTrkRcvRate_Type()
)
atmTrkRcvRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkRcvRate.setStatus("mandatory")
_AtmTrkTrnsCap_Type = Integer32
_AtmTrkTrnsCap_Object = MibTableColumn
atmTrkTrnsCap = _AtmTrkTrnsCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 5),
    _AtmTrkTrnsCap_Type()
)
atmTrkTrnsCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkTrnsCap.setStatus("mandatory")
_AtmTrkTrnsLoad_Type = Integer32
_AtmTrkTrnsLoad_Object = MibTableColumn
atmTrkTrnsLoad = _AtmTrkTrnsLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 6),
    _AtmTrkTrnsLoad_Type()
)
atmTrkTrnsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkTrnsLoad.setStatus("mandatory")
_AtmTrkRcvCap_Type = Integer32
_AtmTrkRcvCap_Object = MibTableColumn
atmTrkRcvCap = _AtmTrkRcvCap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 7),
    _AtmTrkRcvCap_Type()
)
atmTrkRcvCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkRcvCap.setStatus("mandatory")
_AtmTrkRcvLoad_Type = Integer32
_AtmTrkRcvLoad_Object = MibTableColumn
atmTrkRcvLoad = _AtmTrkRcvLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 8),
    _AtmTrkRcvLoad_Type()
)
atmTrkRcvLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkRcvLoad.setStatus("mandatory")


class _AtmTrkType_Type(Integer32):
    """Custom type atmTrkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("trkTypeABR", 4),
          ("trkTypeAXISAF", 6),
          ("trkTypeCBR", 2),
          ("trkTypeIPXAF", 5),
          ("trkTypePHY", 1),
          ("trkTypeVBR", 3))
    )


_AtmTrkType_Type.__name__ = "Integer32"
_AtmTrkType_Object = MibTableColumn
atmTrkType = _AtmTrkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 9),
    _AtmTrkType_Type()
)
atmTrkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkType.setStatus("mandatory")


class _AtmTrkVPI_Type(Integer32):
    """Custom type atmTrkVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTrkVPI_Type.__name__ = "Integer32"
_AtmTrkVPI_Object = MibTableColumn
atmTrkVPI = _AtmTrkVPI_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 10),
    _AtmTrkVPI_Type()
)
atmTrkVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkVPI.setStatus("mandatory")
_AtmTrkResChans_Type = Integer32
_AtmTrkResChans_Object = MibTableColumn
atmTrkResChans = _AtmTrkResChans_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 11),
    _AtmTrkResChans_Type()
)
atmTrkResChans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkResChans.setStatus("mandatory")
_AtmTrkTrafCls_Type = Integer32
_AtmTrkTrafCls_Object = MibTableColumn
atmTrkTrafCls = _AtmTrkTrafCls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 12),
    _AtmTrkTrafCls_Type()
)
atmTrkTrafCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkTrafCls.setStatus("mandatory")


class _AtmTrkOeNdType_Type(Integer32):
    """Custom type atmTrkOeNdType based on Integer32"""
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
        *(("ndTypeAXIS", 5),
          ("ndTypeBPX", 3),
          ("ndTypeIGX", 6),
          ("ndTypeIGXAF", 7),
          ("ndTypeIPX", 2),
          ("ndTypeIPXAF", 4),
          ("ndTypeOther", 1))
    )


_AtmTrkOeNdType_Type.__name__ = "Integer32"
_AtmTrkOeNdType_Object = MibTableColumn
atmTrkOeNdType = _AtmTrkOeNdType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 13),
    _AtmTrkOeNdType_Type()
)
atmTrkOeNdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeNdType.setStatus("mandatory")
_AtmTrkOeName_Type = DisplayString
_AtmTrkOeName_Object = MibTableColumn
atmTrkOeName = _AtmTrkOeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 14),
    _AtmTrkOeName_Type()
)
atmTrkOeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeName.setStatus("mandatory")
_AtmTrkOeIpAddr_Type = IpAddress
_AtmTrkOeIpAddr_Object = MibTableColumn
atmTrkOeIpAddr = _AtmTrkOeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 15),
    _AtmTrkOeIpAddr_Type()
)
atmTrkOeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeIpAddr.setStatus("mandatory")
_AtmTrkOeIfIndex_Type = Integer32
_AtmTrkOeIfIndex_Object = MibTableColumn
atmTrkOeIfIndex = _AtmTrkOeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 16),
    _AtmTrkOeIfIndex_Type()
)
atmTrkOeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeIfIndex.setStatus("mandatory")
_AtmTrkOeDomain_Type = Integer32
_AtmTrkOeDomain_Object = MibTableColumn
atmTrkOeDomain = _AtmTrkOeDomain_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 17),
    _AtmTrkOeDomain_Type()
)
atmTrkOeDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkOeDomain.setStatus("mandatory")
_AtmTrkSvcChannels_Type = Integer32
_AtmTrkSvcChannels_Object = MibTableColumn
atmTrkSvcChannels = _AtmTrkSvcChannels_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 18),
    _AtmTrkSvcChannels_Type()
)
atmTrkSvcChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcChannels.setStatus("mandatory")


class _AtmTrkShareLcn_Type(Integer32):
    """Custom type atmTrkShareLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardBased", 2),
          ("portBased", 1))
    )


_AtmTrkShareLcn_Type.__name__ = "Integer32"
_AtmTrkShareLcn_Object = MibTableColumn
atmTrkShareLcn = _AtmTrkShareLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 19),
    _AtmTrkShareLcn_Type()
)
atmTrkShareLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkShareLcn.setStatus("mandatory")
_AtmTrkSvcLcnLow_Type = Integer32
_AtmTrkSvcLcnLow_Object = MibTableColumn
atmTrkSvcLcnLow = _AtmTrkSvcLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 20),
    _AtmTrkSvcLcnLow_Type()
)
atmTrkSvcLcnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcLcnLow.setStatus("mandatory")
_AtmTrkSvcLcnHigh_Type = Integer32
_AtmTrkSvcLcnHigh_Object = MibTableColumn
atmTrkSvcLcnHigh = _AtmTrkSvcLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 21),
    _AtmTrkSvcLcnHigh_Type()
)
atmTrkSvcLcnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcLcnHigh.setStatus("mandatory")
_AtmTrkSvcVpiLow_Type = Integer32
_AtmTrkSvcVpiLow_Object = MibTableColumn
atmTrkSvcVpiLow = _AtmTrkSvcVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 22),
    _AtmTrkSvcVpiLow_Type()
)
atmTrkSvcVpiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVpiLow.setStatus("mandatory")
_AtmTrkSvcVpiHigh_Type = Integer32
_AtmTrkSvcVpiHigh_Object = MibTableColumn
atmTrkSvcVpiHigh = _AtmTrkSvcVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 23),
    _AtmTrkSvcVpiHigh_Type()
)
atmTrkSvcVpiHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVpiHigh.setStatus("mandatory")
_AtmTrkSvcVciLow_Type = Integer32
_AtmTrkSvcVciLow_Object = MibTableColumn
atmTrkSvcVciLow = _AtmTrkSvcVciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 24),
    _AtmTrkSvcVciLow_Type()
)
atmTrkSvcVciLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVciLow.setStatus("mandatory")
_AtmTrkSvcVciHigh_Type = Integer32
_AtmTrkSvcVciHigh_Object = MibTableColumn
atmTrkSvcVciHigh = _AtmTrkSvcVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 25),
    _AtmTrkSvcVciHigh_Type()
)
atmTrkSvcVciHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcVciHigh.setStatus("mandatory")
_AtmTrkSvcQbinBitMap_Type = OctetString
_AtmTrkSvcQbinBitMap_Object = MibTableColumn
atmTrkSvcQbinBitMap = _AtmTrkSvcQbinBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 26),
    _AtmTrkSvcQbinBitMap_Type()
)
atmTrkSvcQbinBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcQbinBitMap.setStatus("mandatory")
_AtmTrkSvcQbinSz_Type = Integer32
_AtmTrkSvcQbinSz_Object = MibTableColumn
atmTrkSvcQbinSz = _AtmTrkSvcQbinSz_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 27),
    _AtmTrkSvcQbinSz_Type()
)
atmTrkSvcQbinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcQbinSz.setStatus("mandatory")
_AtmTrkSvcBw_Type = Integer32
_AtmTrkSvcBw_Object = MibTableColumn
atmTrkSvcBw = _AtmTrkSvcBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 28),
    _AtmTrkSvcBw_Type()
)
atmTrkSvcBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkSvcBw.setStatus("mandatory")


class _AtmTrkSvcInUse_Type(Integer32):
    """Custom type atmTrkSvcInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_AtmTrkSvcInUse_Type.__name__ = "Integer32"
_AtmTrkSvcInUse_Object = MibTableColumn
atmTrkSvcInUse = _AtmTrkSvcInUse_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 29),
    _AtmTrkSvcInUse_Type()
)
atmTrkSvcInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkSvcInUse.setStatus("mandatory")
_AtmTrkXmitRate_Type = Integer32
_AtmTrkXmitRate_Object = MibTableColumn
atmTrkXmitRate = _AtmTrkXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 30),
    _AtmTrkXmitRate_Type()
)
atmTrkXmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkXmitRate.setStatus("mandatory")


class _AtmTrkPassSync_Type(Integer32):
    """Custom type atmTrkPassSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AtmTrkPassSync_Type.__name__ = "Integer32"
_AtmTrkPassSync_Object = MibTableColumn
atmTrkPassSync = _AtmTrkPassSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 31),
    _AtmTrkPassSync_Type()
)
atmTrkPassSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkPassSync.setStatus("mandatory")
_AtmTrkStatRes_Type = Integer32
_AtmTrkStatRes_Object = MibTableColumn
atmTrkStatRes = _AtmTrkStatRes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 32),
    _AtmTrkStatRes_Type()
)
atmTrkStatRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkStatRes.setStatus("mandatory")


class _AtmTrkLoopClock_Type(Integer32):
    """Custom type atmTrkLoopClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AtmTrkLoopClock_Type.__name__ = "Integer32"
_AtmTrkLoopClock_Object = MibTableColumn
atmTrkLoopClock = _AtmTrkLoopClock_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 33),
    _AtmTrkLoopClock_Type()
)
atmTrkLoopClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkLoopClock.setStatus("mandatory")


class _AtmTrkBdataBTxQlen_Type(Integer32):
    """Custom type atmTrkBdataBTxQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBTxQlen_Type.__name__ = "Integer32"
_AtmTrkBdataBTxQlen_Object = MibTableColumn
atmTrkBdataBTxQlen = _AtmTrkBdataBTxQlen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 34),
    _AtmTrkBdataBTxQlen_Type()
)
atmTrkBdataBTxQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxQlen.setStatus("mandatory")


class _AtmTrkBdataBRxQlen_Type(Integer32):
    """Custom type atmTrkBdataBRxQlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBRxQlen_Type.__name__ = "Integer32"
_AtmTrkBdataBRxQlen_Object = MibTableColumn
atmTrkBdataBRxQlen = _AtmTrkBdataBRxQlen_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 35),
    _AtmTrkBdataBRxQlen_Type()
)
atmTrkBdataBRxQlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxQlen.setStatus("mandatory")


class _AtmTrkBdataBTxEfcn_Type(Integer32):
    """Custom type atmTrkBdataBTxEfcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBTxEfcn_Type.__name__ = "Integer32"
_AtmTrkBdataBTxEfcn_Object = MibTableColumn
atmTrkBdataBTxEfcn = _AtmTrkBdataBTxEfcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 36),
    _AtmTrkBdataBTxEfcn_Type()
)
atmTrkBdataBTxEfcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxEfcn.setStatus("mandatory")


class _AtmTrkBdataBRxEfcn_Type(Integer32):
    """Custom type atmTrkBdataBRxEfcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8000),
    )


_AtmTrkBdataBRxEfcn_Type.__name__ = "Integer32"
_AtmTrkBdataBRxEfcn_Object = MibTableColumn
atmTrkBdataBRxEfcn = _AtmTrkBdataBRxEfcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 37),
    _AtmTrkBdataBRxEfcn_Type()
)
atmTrkBdataBRxEfcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxEfcn.setStatus("mandatory")


class _AtmTrkBdataBTxHiClp_Type(Integer32):
    """Custom type atmTrkBdataBTxHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBTxHiClp_Type.__name__ = "Integer32"
_AtmTrkBdataBTxHiClp_Object = MibTableColumn
atmTrkBdataBTxHiClp = _AtmTrkBdataBTxHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 38),
    _AtmTrkBdataBTxHiClp_Type()
)
atmTrkBdataBTxHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxHiClp.setStatus("mandatory")


class _AtmTrkBdataBRxHiClp_Type(Integer32):
    """Custom type atmTrkBdataBRxHiClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBRxHiClp_Type.__name__ = "Integer32"
_AtmTrkBdataBRxHiClp_Object = MibTableColumn
atmTrkBdataBRxHiClp = _AtmTrkBdataBRxHiClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 39),
    _AtmTrkBdataBRxHiClp_Type()
)
atmTrkBdataBRxHiClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxHiClp.setStatus("mandatory")


class _AtmTrkBdataBTxLoClp_Type(Integer32):
    """Custom type atmTrkBdataBTxLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBTxLoClp_Type.__name__ = "Integer32"
_AtmTrkBdataBTxLoClp_Object = MibTableColumn
atmTrkBdataBTxLoClp = _AtmTrkBdataBTxLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 40),
    _AtmTrkBdataBTxLoClp_Type()
)
atmTrkBdataBTxLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBTxLoClp.setStatus("mandatory")


class _AtmTrkBdataBRxLoClp_Type(Integer32):
    """Custom type atmTrkBdataBRxLoClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AtmTrkBdataBRxLoClp_Type.__name__ = "Integer32"
_AtmTrkBdataBRxLoClp_Object = MibTableColumn
atmTrkBdataBRxLoClp = _AtmTrkBdataBRxLoClp_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 41),
    _AtmTrkBdataBRxLoClp_Type()
)
atmTrkBdataBRxLoClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkBdataBRxLoClp.setStatus("mandatory")


class _AtmTrkMaxChanPort_Type(Integer32):
    """Custom type atmTrkMaxChanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16320),
    )


_AtmTrkMaxChanPort_Type.__name__ = "Integer32"
_AtmTrkMaxChanPort_Object = MibTableColumn
atmTrkMaxChanPort = _AtmTrkMaxChanPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 42),
    _AtmTrkMaxChanPort_Type()
)
atmTrkMaxChanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkMaxChanPort.setStatus("mandatory")


class _AtmTrkLinkType_Type(Integer32):
    """Custom type atmTrkLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("satellite", 2),
          ("terrestrial", 1))
    )


_AtmTrkLinkType_Type.__name__ = "Integer32"
_AtmTrkLinkType_Object = MibTableColumn
atmTrkLinkType = _AtmTrkLinkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 43),
    _AtmTrkLinkType_Type()
)
atmTrkLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkLinkType.setStatus("mandatory")


class _AtmTrkDerouteDelayTimer_Type(Integer32):
    """Custom type atmTrkDerouteDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AtmTrkDerouteDelayTimer_Type.__name__ = "Integer32"
_AtmTrkDerouteDelayTimer_Object = MibTableColumn
atmTrkDerouteDelayTimer = _AtmTrkDerouteDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 44),
    _AtmTrkDerouteDelayTimer_Type()
)
atmTrkDerouteDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkDerouteDelayTimer.setStatus("mandatory")
_AtmTrkGtwyChCount_Type = Integer32
_AtmTrkGtwyChCount_Object = MibTableColumn
atmTrkGtwyChCount = _AtmTrkGtwyChCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 45),
    _AtmTrkGtwyChCount_Type()
)
atmTrkGtwyChCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkGtwyChCount.setStatus("mandatory")


class _AtmTrkRetainedLinks_Type(Integer32):
    """Custom type atmTrkRetainedLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmTrkRetainedLinks_Type.__name__ = "Integer32"
_AtmTrkRetainedLinks_Object = MibTableColumn
atmTrkRetainedLinks = _AtmTrkRetainedLinks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 46),
    _AtmTrkRetainedLinks_Type()
)
atmTrkRetainedLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkRetainedLinks.setStatus("mandatory")
_AtmTrkImaWindowSize_Type = Integer32
_AtmTrkImaWindowSize_Object = MibTableColumn
atmTrkImaWindowSize = _AtmTrkImaWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 47),
    _AtmTrkImaWindowSize_Type()
)
atmTrkImaWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaWindowSize.setStatus("mandatory")
_AtmTrkImaTrnsCnts_Type = Integer32
_AtmTrkImaTrnsCnts_Object = MibTableColumn
atmTrkImaTrnsCnts = _AtmTrkImaTrnsCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 48),
    _AtmTrkImaTrnsCnts_Type()
)
atmTrkImaTrnsCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaTrnsCnts.setStatus("mandatory")
_AtmTrkImaReenableTimer_Type = Integer32
_AtmTrkImaReenableTimer_Object = MibTableColumn
atmTrkImaReenableTimer = _AtmTrkImaReenableTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 2, 1, 49),
    _AtmTrkImaReenableTimer_Type()
)
atmTrkImaReenableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTrkImaReenableTimer.setStatus("mandatory")
_AtmTrunkStatsTable_Object = MibTable
atmTrunkStatsTable = _AtmTrunkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4)
)
if mibBuilder.loadTexts:
    atmTrunkStatsTable.setStatus("mandatory")
_AtmTrkStatsEntry_Object = MibTableRow
atmTrkStatsEntry = _AtmTrkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1)
)
atmTrkStatsEntry.setIndexNames(
    (0, "STRATACOM-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    atmTrkStatsEntry.setStatus("mandatory")
_AtmTrkStatsTxVoPktDrps_Type = Counter32
_AtmTrkStatsTxVoPktDrps_Object = MibTableColumn
atmTrkStatsTxVoPktDrps = _AtmTrkStatsTxVoPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 1),
    _AtmTrkStatsTxVoPktDrps_Type()
)
atmTrkStatsTxVoPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVoPktDrps.setStatus("mandatory")
_AtmTrkStatsTxTsPktDrps_Type = Counter32
_AtmTrkStatsTxTsPktDrps_Object = MibTableColumn
atmTrkStatsTxTsPktDrps = _AtmTrkStatsTxTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 2),
    _AtmTrkStatsTxTsPktDrps_Type()
)
atmTrkStatsTxTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxTsPktDrps.setStatus("mandatory")
_AtmTrkStatsTxNonTsPktDrps_Type = Counter32
_AtmTrkStatsTxNonTsPktDrps_Object = MibTableColumn
atmTrkStatsTxNonTsPktDrps = _AtmTrkStatsTxNonTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 3),
    _AtmTrkStatsTxNonTsPktDrps_Type()
)
atmTrkStatsTxNonTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxNonTsPktDrps.setStatus("mandatory")
_AtmTrkStatsTxHiPrioPktDrps_Type = Counter32
_AtmTrkStatsTxHiPrioPktDrps_Object = MibTableColumn
atmTrkStatsTxHiPrioPktDrps = _AtmTrkStatsTxHiPrioPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 4),
    _AtmTrkStatsTxHiPrioPktDrps_Type()
)
atmTrkStatsTxHiPrioPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxHiPrioPktDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataAPktDrps_Type = Counter32
_AtmTrkStatsTxBdataAPktDrps_Object = MibTableColumn
atmTrkStatsTxBdataAPktDrps = _AtmTrkStatsTxBdataAPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 5),
    _AtmTrkStatsTxBdataAPktDrps_Type()
)
atmTrkStatsTxBdataAPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataAPktDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataBPktDrps_Type = Counter32
_AtmTrkStatsTxBdataBPktDrps_Object = MibTableColumn
atmTrkStatsTxBdataBPktDrps = _AtmTrkStatsTxBdataBPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 6),
    _AtmTrkStatsTxBdataBPktDrps_Type()
)
atmTrkStatsTxBdataBPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataBPktDrps.setStatus("mandatory")
_AtmTrkStatsRxVoPktDrps_Type = Counter32
_AtmTrkStatsRxVoPktDrps_Object = MibTableColumn
atmTrkStatsRxVoPktDrps = _AtmTrkStatsRxVoPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 7),
    _AtmTrkStatsRxVoPktDrps_Type()
)
atmTrkStatsRxVoPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxVoPktDrps.setStatus("mandatory")
_AtmTrkStatsRxTsPktDrps_Type = Counter32
_AtmTrkStatsRxTsPktDrps_Object = MibTableColumn
atmTrkStatsRxTsPktDrps = _AtmTrkStatsRxTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 8),
    _AtmTrkStatsRxTsPktDrps_Type()
)
atmTrkStatsRxTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxTsPktDrps.setStatus("mandatory")
_AtmTrkStatsRxNonTsPktDrps_Type = Counter32
_AtmTrkStatsRxNonTsPktDrps_Object = MibTableColumn
atmTrkStatsRxNonTsPktDrps = _AtmTrkStatsRxNonTsPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 9),
    _AtmTrkStatsRxNonTsPktDrps_Type()
)
atmTrkStatsRxNonTsPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxNonTsPktDrps.setStatus("mandatory")
_AtmTrkStatsRxHiPrioPktDrps_Type = Counter32
_AtmTrkStatsRxHiPrioPktDrps_Object = MibTableColumn
atmTrkStatsRxHiPrioPktDrps = _AtmTrkStatsRxHiPrioPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 10),
    _AtmTrkStatsRxHiPrioPktDrps_Type()
)
atmTrkStatsRxHiPrioPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxHiPrioPktDrps.setStatus("mandatory")
_AtmTrkStatsRxBdataAPktDrps_Type = Counter32
_AtmTrkStatsRxBdataAPktDrps_Object = MibTableColumn
atmTrkStatsRxBdataAPktDrps = _AtmTrkStatsRxBdataAPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 11),
    _AtmTrkStatsRxBdataAPktDrps_Type()
)
atmTrkStatsRxBdataAPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxBdataAPktDrps.setStatus("mandatory")
_AtmTrkStatsRxBdataBPktDrps_Type = Counter32
_AtmTrkStatsRxBdataBPktDrps_Object = MibTableColumn
atmTrkStatsRxBdataBPktDrps = _AtmTrkStatsRxBdataBPktDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 12),
    _AtmTrkStatsRxBdataBPktDrps_Type()
)
atmTrkStatsRxBdataBPktDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsRxBdataBPktDrps.setStatus("mandatory")
_AtmTrkStatsSpacerPktsDrps_Type = Counter32
_AtmTrkStatsSpacerPktsDrps_Object = MibTableColumn
atmTrkStatsSpacerPktsDrps = _AtmTrkStatsSpacerPktsDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 13),
    _AtmTrkStatsSpacerPktsDrps_Type()
)
atmTrkStatsSpacerPktsDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsSpacerPktsDrps.setStatus("mandatory")
_AtmTrkStatsTotalPktsTxtoLns_Type = Counter32
_AtmTrkStatsTotalPktsTxtoLns_Object = MibTableColumn
atmTrkStatsTotalPktsTxtoLns = _AtmTrkStatsTotalPktsTxtoLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 14),
    _AtmTrkStatsTotalPktsTxtoLns_Type()
)
atmTrkStatsTotalPktsTxtoLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalPktsTxtoLns.setStatus("mandatory")
_AtmTrkStatsTotalPktsRxFromLns_Type = Counter32
_AtmTrkStatsTotalPktsRxFromLns_Object = MibTableColumn
atmTrkStatsTotalPktsRxFromLns = _AtmTrkStatsTotalPktsRxFromLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 15),
    _AtmTrkStatsTotalPktsRxFromLns_Type()
)
atmTrkStatsTotalPktsRxFromLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalPktsRxFromLns.setStatus("mandatory")
_AtmTrkStatsTxVoCellDrps_Type = Counter32
_AtmTrkStatsTxVoCellDrps_Object = MibTableColumn
atmTrkStatsTxVoCellDrps = _AtmTrkStatsTxVoCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 16),
    _AtmTrkStatsTxVoCellDrps_Type()
)
atmTrkStatsTxVoCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVoCellDrps.setStatus("mandatory")
_AtmTrkStatsTxTsCellDrps_Type = Counter32
_AtmTrkStatsTxTsCellDrps_Object = MibTableColumn
atmTrkStatsTxTsCellDrps = _AtmTrkStatsTxTsCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 17),
    _AtmTrkStatsTxTsCellDrps_Type()
)
atmTrkStatsTxTsCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxTsCellDrps.setStatus("mandatory")
_AtmTrkStatsTxNonTsCellDrps_Type = Counter32
_AtmTrkStatsTxNonTsCellDrps_Object = MibTableColumn
atmTrkStatsTxNonTsCellDrps = _AtmTrkStatsTxNonTsCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 18),
    _AtmTrkStatsTxNonTsCellDrps_Type()
)
atmTrkStatsTxNonTsCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxNonTsCellDrps.setStatus("mandatory")
_AtmTrkStatsTxHiPrioCellDrps_Type = Counter32
_AtmTrkStatsTxHiPrioCellDrps_Object = MibTableColumn
atmTrkStatsTxHiPrioCellDrps = _AtmTrkStatsTxHiPrioCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 19),
    _AtmTrkStatsTxHiPrioCellDrps_Type()
)
atmTrkStatsTxHiPrioCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxHiPrioCellDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataACellDrps_Type = Counter32
_AtmTrkStatsTxBdataACellDrps_Object = MibTableColumn
atmTrkStatsTxBdataACellDrps = _AtmTrkStatsTxBdataACellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 20),
    _AtmTrkStatsTxBdataACellDrps_Type()
)
atmTrkStatsTxBdataACellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataACellDrps.setStatus("mandatory")
_AtmTrkStatsTxBdataBCellDrps_Type = Counter32
_AtmTrkStatsTxBdataBCellDrps_Object = MibTableColumn
atmTrkStatsTxBdataBCellDrps = _AtmTrkStatsTxBdataBCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 21),
    _AtmTrkStatsTxBdataBCellDrps_Type()
)
atmTrkStatsTxBdataBCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxBdataBCellDrps.setStatus("mandatory")
_AtmTrkStatsTxCbrCellDrps_Type = Counter32
_AtmTrkStatsTxCbrCellDrps_Object = MibTableColumn
atmTrkStatsTxCbrCellDrps = _AtmTrkStatsTxCbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 22),
    _AtmTrkStatsTxCbrCellDrps_Type()
)
atmTrkStatsTxCbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxCbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTxVbrCellDrps_Type = Counter32
_AtmTrkStatsTxVbrCellDrps_Object = MibTableColumn
atmTrkStatsTxVbrCellDrps = _AtmTrkStatsTxVbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 23),
    _AtmTrkStatsTxVbrCellDrps_Type()
)
atmTrkStatsTxVbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxVbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTxAbrCellDrps_Type = Counter32
_AtmTrkStatsTxAbrCellDrps_Object = MibTableColumn
atmTrkStatsTxAbrCellDrps = _AtmTrkStatsTxAbrCellDrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 24),
    _AtmTrkStatsTxAbrCellDrps_Type()
)
atmTrkStatsTxAbrCellDrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTxAbrCellDrps.setStatus("mandatory")
_AtmTrkStatsTotalCellsTxtoLns_Type = Counter32
_AtmTrkStatsTotalCellsTxtoLns_Object = MibTableColumn
atmTrkStatsTotalCellsTxtoLns = _AtmTrkStatsTotalCellsTxtoLns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 25),
    _AtmTrkStatsTotalCellsTxtoLns_Type()
)
atmTrkStatsTotalCellsTxtoLns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalCellsTxtoLns.setStatus("mandatory")
_AtmTrkStatsTotalCellsRxFromPorts_Type = Counter32
_AtmTrkStatsTotalCellsRxFromPorts_Object = MibTableColumn
atmTrkStatsTotalCellsRxFromPorts = _AtmTrkStatsTotalCellsRxFromPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 2, 4, 4, 1, 26),
    _AtmTrkStatsTotalCellsRxFromPorts_Type()
)
atmTrkStatsTotalCellsRxFromPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrkStatsTotalCellsRxFromPorts.setStatus("mandatory")
_SwitchConnection_ObjectIdentity = ObjectIdentity
switchConnection = _SwitchConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3)
)
_ConnNextEndptIndex_Type = Integer32
_ConnNextEndptIndex_Object = MibScalar
connNextEndptIndex = _ConnNextEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 1),
    _ConnNextEndptIndex_Type()
)
connNextEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNextEndptIndex.setStatus("mandatory")
_ErrStatusLastIndex_Type = Integer32
_ErrStatusLastIndex_Object = MibScalar
errStatusLastIndex = _ErrStatusLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 2),
    _ErrStatusLastIndex_Type()
)
errStatusLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errStatusLastIndex.setStatus("obsolete")
_ErrStatusTable_Object = MibTable
errStatusTable = _ErrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3)
)
if mibBuilder.loadTexts:
    errStatusTable.setStatus("deprecated")
_ErrStatusTableEntry_Object = MibTableRow
errStatusTableEntry = _ErrStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1)
)
errStatusTableEntry.setIndexNames(
    (0, "STRATACOM-MIB", "errReqId"),
)
if mibBuilder.loadTexts:
    errStatusTableEntry.setStatus("deprecated")
_ErrReqId_Type = Integer32
_ErrReqId_Object = MibTableColumn
errReqId = _ErrReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 1),
    _ErrReqId_Type()
)
errReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errReqId.setStatus("mandatory")


class _ErrCode_Type(Integer32):
    """Custom type errCode based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("ascUpdFailed", 23),
          ("authorizationError", 16),
          ("bnmProblem", 22),
          ("chanDisabled", 32),
          ("chanEnabled", 31),
          ("commitFailed", 14),
          ("databaseLocked", 5),
          ("dlciDisabled", 34),
          ("dlciEnabled", 33),
          ("existErr", 2),
          ("featureDisabled", 19),
          ("inconsistentName", 18),
          ("inconsistentValue", 12),
          ("lineDisabled", 25),
          ("lineEnabled", 24),
          ("lineHasPorts", 27),
          ("lmMismatch", 26),
          ("m32Problem", 20),
          ("noCreation", 11),
          ("notWritable", 17),
          ("otherErr", 6),
          ("portDisable", 29),
          ("portEnabled", 28),
          ("portHasChan", 30),
          ("resourceErr", 4),
          ("resourceUnavailable", 13),
          ("sarProblem", 21),
          ("success", 1),
          ("syntaxErr", 3),
          ("undoFailed", 15),
          ("wrongEncoding", 9),
          ("wrongLength", 8),
          ("wrongType", 7),
          ("wrongValue", 10))
    )


_ErrCode_Type.__name__ = "Integer32"
_ErrCode_Object = MibTableColumn
errCode = _ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 2),
    _ErrCode_Type()
)
errCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errCode.setStatus("mandatory")
_ErrStatusDesc_Type = DisplayString
_ErrStatusDesc_Object = MibTableColumn
errStatusDesc = _ErrStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 3, 1, 3),
    _ErrStatusDesc_Type()
)
errStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errStatusDesc.setStatus("mandatory")
_ConnTable_Object = MibTable
connTable = _ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4)
)
if mibBuilder.loadTexts:
    connTable.setStatus("mandatory")
_ConnTableEntry_Object = MibTableRow
connTableEntry = _ConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1)
)
connTableEntry.setIndexNames(
    (0, "STRATACOM-MIB", "connIndex"),
)
if mibBuilder.loadTexts:
    connTableEntry.setStatus("mandatory")


class _ConnIndex_Type(Integer32):
    """Custom type connIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConnIndex_Type.__name__ = "Integer32"
_ConnIndex_Object = MibTableColumn
connIndex = _ConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 1),
    _ConnIndex_Type()
)
connIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connIndex.setStatus("mandatory")
_ConnLclEndptDesc_Type = DisplayString
_ConnLclEndptDesc_Object = MibTableColumn
connLclEndptDesc = _ConnLclEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 2),
    _ConnLclEndptDesc_Type()
)
connLclEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connLclEndptDesc.setStatus("mandatory")


class _ConnType_Type(Integer32):
    """Custom type connType based on Integer32"""
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
        *(("atf", 2),
          ("atm", 3),
          ("frameRelay", 1),
          ("unknown", 5),
          ("voice", 4))
    )


_ConnType_Type.__name__ = "Integer32"
_ConnType_Object = MibTableColumn
connType = _ConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 3),
    _ConnType_Type()
)
connType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connType.setStatus("mandatory")


class _ConnOeIndex_Type(Integer32):
    """Custom type connOeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConnOeIndex_Type.__name__ = "Integer32"
_ConnOeIndex_Object = MibTableColumn
connOeIndex = _ConnOeIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 4),
    _ConnOeIndex_Type()
)
connOeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOeIndex.setStatus("mandatory")
_ConnRmtEndptDesc_Type = DisplayString
_ConnRmtEndptDesc_Object = MibTableColumn
connRmtEndptDesc = _ConnRmtEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 5),
    _ConnRmtEndptDesc_Type()
)
connRmtEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connRmtEndptDesc.setStatus("mandatory")


class _ConnMasterFlag_Type(Integer32):
    """Custom type connMasterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnMasterFlag_Type.__name__ = "Integer32"
_ConnMasterFlag_Object = MibTableColumn
connMasterFlag = _ConnMasterFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 6),
    _ConnMasterFlag_Type()
)
connMasterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMasterFlag.setStatus("mandatory")


class _ConnClassOfService_Type(Integer32):
    """Custom type connClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ConnClassOfService_Type.__name__ = "Integer32"
_ConnClassOfService_Object = MibTableColumn
connClassOfService = _ConnClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 7),
    _ConnClassOfService_Type()
)
connClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connClassOfService.setStatus("mandatory")


class _ConnGroupFlag_Type(Integer32):
    """Custom type connGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnGroupFlag_Type.__name__ = "Integer32"
_ConnGroupFlag_Object = MibTableColumn
connGroupFlag = _ConnGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 8),
    _ConnGroupFlag_Type()
)
connGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connGroupFlag.setStatus("mandatory")


class _ConnAdminStatus_Type(Integer32):
    """Custom type connAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createGroup", 5),
          ("deleteGroup", 6),
          ("down", 2),
          ("modify", 3),
          ("up", 1),
          ("writeOnly", 4))
    )


_ConnAdminStatus_Type.__name__ = "Integer32"
_ConnAdminStatus_Object = MibTableColumn
connAdminStatus = _ConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 9),
    _ConnAdminStatus_Type()
)
connAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connAdminStatus.setStatus("mandatory")


class _ConnOperStatus_Type(Integer32):
    """Custom type connOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("failed", 4),
          ("ok", 1),
          ("okPendingDown", 2),
          ("okPendingRoute", 5),
          ("unknown", 6))
    )


_ConnOperStatus_Type.__name__ = "Integer32"
_ConnOperStatus_Object = MibTableColumn
connOperStatus = _ConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 10),
    _ConnOperStatus_Type()
)
connOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOperStatus.setStatus("mandatory")


class _ConnNoRouteFoundFailure_Type(Integer32):
    """Custom type connNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnNoRouteFoundFailure_Type.__name__ = "Integer32"
_ConnNoRouteFoundFailure_Object = MibTableColumn
connNoRouteFoundFailure = _ConnNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 11),
    _ConnNoRouteFoundFailure_Type()
)
connNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNoRouteFoundFailure.setStatus("mandatory")


class _ConnBumpFailure_Type(Integer32):
    """Custom type connBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ConnBumpFailure_Type.__name__ = "Integer32"
_ConnBumpFailure_Object = MibTableColumn
connBumpFailure = _ConnBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 12),
    _ConnBumpFailure_Type()
)
connBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connBumpFailure.setStatus("mandatory")
_ConnFirstEndptPtr_Type = ObjectIdentifier
_ConnFirstEndptPtr_Object = MibTableColumn
connFirstEndptPtr = _ConnFirstEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 13),
    _ConnFirstEndptPtr_Type()
)
connFirstEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFirstEndptPtr.setStatus("mandatory")


class _ConnCurrRouteDesc_Type(DisplayString):
    """Custom type connCurrRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConnCurrRouteDesc_Type.__name__ = "DisplayString"
_ConnCurrRouteDesc_Object = MibTableColumn
connCurrRouteDesc = _ConnCurrRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 14),
    _ConnCurrRouteDesc_Type()
)
connCurrRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCurrRouteDesc.setStatus("mandatory")


class _ConnPrefRouteDesc_Type(DisplayString):
    """Custom type connPrefRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConnPrefRouteDesc_Type.__name__ = "DisplayString"
_ConnPrefRouteDesc_Object = MibTableColumn
connPrefRouteDesc = _ConnPrefRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 15),
    _ConnPrefRouteDesc_Type()
)
connPrefRouteDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPrefRouteDesc.setStatus("mandatory")


class _ConnMstOSpacePkts_Type(Integer32):
    """Custom type connMstOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnMstOSpacePkts_Type.__name__ = "Integer32"
_ConnMstOSpacePkts_Object = MibTableColumn
connMstOSpacePkts = _ConnMstOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 16),
    _ConnMstOSpacePkts_Type()
)
connMstOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpacePkts.setStatus("mandatory")


class _ConnMstOSpaceCells_Type(Integer32):
    """Custom type connMstOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnMstOSpaceCells_Type.__name__ = "Integer32"
_ConnMstOSpaceCells_Object = MibTableColumn
connMstOSpaceCells = _ConnMstOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 17),
    _ConnMstOSpaceCells_Type()
)
connMstOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceCells.setStatus("mandatory")


class _ConnMstOSpaceBdaCmax_Type(Integer32):
    """Custom type connMstOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnMstOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnMstOSpaceBdaCmax_Object = MibTableColumn
connMstOSpaceBdaCmax = _ConnMstOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 18),
    _ConnMstOSpaceBdaCmax_Type()
)
connMstOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceBdaCmax.setStatus("mandatory")


class _ConnMstOSpaceBdbCmax_Type(Integer32):
    """Custom type connMstOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnMstOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnMstOSpaceBdbCmax_Object = MibTableColumn
connMstOSpaceBdbCmax = _ConnMstOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 19),
    _ConnMstOSpaceBdbCmax_Type()
)
connMstOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMstOSpaceBdbCmax.setStatus("mandatory")


class _ConnSlvOSpacePkts_Type(Integer32):
    """Custom type connSlvOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnSlvOSpacePkts_Type.__name__ = "Integer32"
_ConnSlvOSpacePkts_Object = MibTableColumn
connSlvOSpacePkts = _ConnSlvOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 20),
    _ConnSlvOSpacePkts_Type()
)
connSlvOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpacePkts.setStatus("mandatory")


class _ConnSlvOSpaceCells_Type(Integer32):
    """Custom type connSlvOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnSlvOSpaceCells_Type.__name__ = "Integer32"
_ConnSlvOSpaceCells_Object = MibTableColumn
connSlvOSpaceCells = _ConnSlvOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 21),
    _ConnSlvOSpaceCells_Type()
)
connSlvOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceCells.setStatus("mandatory")


class _ConnSlvOSpaceBdaCmax_Type(Integer32):
    """Custom type connSlvOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnSlvOSpaceBdaCmax_Type.__name__ = "Integer32"
_ConnSlvOSpaceBdaCmax_Object = MibTableColumn
connSlvOSpaceBdaCmax = _ConnSlvOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 22),
    _ConnSlvOSpaceBdaCmax_Type()
)
connSlvOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceBdaCmax.setStatus("mandatory")


class _ConnSlvOSpaceBdbCmax_Type(Integer32):
    """Custom type connSlvOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ConnSlvOSpaceBdbCmax_Type.__name__ = "Integer32"
_ConnSlvOSpaceBdbCmax_Object = MibTableColumn
connSlvOSpaceBdbCmax = _ConnSlvOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 23),
    _ConnSlvOSpaceBdbCmax_Type()
)
connSlvOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSlvOSpaceBdbCmax.setStatus("mandatory")
_ConnIcaRTD_Type = Integer32
_ConnIcaRTD_Object = MibTableColumn
connIcaRTD = _ConnIcaRTD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 24),
    _ConnIcaRTD_Type()
)
connIcaRTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connIcaRTD.setStatus("mandatory")
_ConnGroupDesc_Type = DisplayString
_ConnGroupDesc_Object = MibTableColumn
connGroupDesc = _ConnGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 4, 1, 25),
    _ConnGroupDesc_Type()
)
connGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connGroupDesc.setStatus("mandatory")
_FrEndptTable_Object = MibTable
frEndptTable = _FrEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5)
)
if mibBuilder.loadTexts:
    frEndptTable.setStatus("mandatory")
_FrEndptEntry_Object = MibTableRow
frEndptEntry = _FrEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1)
)
frEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptIndex"),
)
if mibBuilder.loadTexts:
    frEndptEntry.setStatus("mandatory")


class _FrEndptIndex_Type(Integer32):
    """Custom type frEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_FrEndptIndex_Type.__name__ = "Integer32"
_FrEndptIndex_Object = MibTableColumn
frEndptIndex = _FrEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 1),
    _FrEndptIndex_Type()
)
frEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptIndex.setStatus("mandatory")
_FrEndptDesc_Type = DisplayString
_FrEndptDesc_Object = MibTableColumn
frEndptDesc = _FrEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 2),
    _FrEndptDesc_Type()
)
frEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptDesc.setStatus("mandatory")


class _FrOtherEndptIndex_Type(Integer32):
    """Custom type frOtherEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_FrOtherEndptIndex_Type.__name__ = "Integer32"
_FrOtherEndptIndex_Object = MibTableColumn
frOtherEndptIndex = _FrOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 3),
    _FrOtherEndptIndex_Type()
)
frOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frOtherEndptIndex.setStatus("mandatory")
_FrOtherEndptDesc_Type = DisplayString
_FrOtherEndptDesc_Object = MibTableColumn
frOtherEndptDesc = _FrOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 4),
    _FrOtherEndptDesc_Type()
)
frOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frOtherEndptDesc.setStatus("mandatory")


class _FrEndptAdminStatus_Type(Integer32):
    """Custom type frEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_FrEndptAdminStatus_Type.__name__ = "Integer32"
_FrEndptAdminStatus_Object = MibTableColumn
frEndptAdminStatus = _FrEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 5),
    _FrEndptAdminStatus_Type()
)
frEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptAdminStatus.setStatus("mandatory")


class _FrEndptOperStatus_Type(Integer32):
    """Custom type frEndptOperStatus based on Integer32"""
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
        *(("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("looped", 8),
          ("ok", 1),
          ("okPendingDelete", 7),
          ("okPendingDown", 2),
          ("okPendingRoute", 6),
          ("unknown", 9))
    )


_FrEndptOperStatus_Type.__name__ = "Integer32"
_FrEndptOperStatus_Object = MibTableColumn
frEndptOperStatus = _FrEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 6),
    _FrEndptOperStatus_Type()
)
frEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptOperStatus.setStatus("mandatory")


class _FrNoRouteFoundFailure_Type(Integer32):
    """Custom type frNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrNoRouteFoundFailure_Type.__name__ = "Integer32"
_FrNoRouteFoundFailure_Object = MibTableColumn
frNoRouteFoundFailure = _FrNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 7),
    _FrNoRouteFoundFailure_Type()
)
frNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNoRouteFoundFailure.setStatus("mandatory")


class _FrBumpFailure_Type(Integer32):
    """Custom type frBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrBumpFailure_Type.__name__ = "Integer32"
_FrBumpFailure_Object = MibTableColumn
frBumpFailure = _FrBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 8),
    _FrBumpFailure_Type()
)
frBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBumpFailure.setStatus("mandatory")


class _FrEndPointFailure_Type(Integer32):
    """Custom type frEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndPointFailure_Type.__name__ = "Integer32"
_FrEndPointFailure_Object = MibTableColumn
frEndPointFailure = _FrEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 9),
    _FrEndPointFailure_Type()
)
frEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointFailure.setStatus("mandatory")


class _FrTestFailure_Type(Integer32):
    """Custom type frTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrTestFailure_Type.__name__ = "Integer32"
_FrTestFailure_Object = MibTableColumn
frTestFailure = _FrTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 10),
    _FrTestFailure_Type()
)
frTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frTestFailure.setStatus("mandatory")
_FrConnPtr_Type = ObjectIdentifier
_FrConnPtr_Object = MibTableColumn
frConnPtr = _FrConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 11),
    _FrConnPtr_Type()
)
frConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frConnPtr.setStatus("mandatory")
_FrNextPtr_Type = ObjectIdentifier
_FrNextPtr_Object = MibTableColumn
frNextPtr = _FrNextPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 12),
    _FrNextPtr_Type()
)
frNextPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNextPtr.setStatus("mandatory")
_FrNextOnPortPtr_Type = ObjectIdentifier
_FrNextOnPortPtr_Object = MibTableColumn
frNextOnPortPtr = _FrNextOnPortPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 13),
    _FrNextOnPortPtr_Type()
)
frNextOnPortPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNextOnPortPtr.setStatus("mandatory")


class _FrEndptConnDesc_Type(DisplayString):
    """Custom type frEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FrEndptConnDesc_Type.__name__ = "DisplayString"
_FrEndptConnDesc_Object = MibTableColumn
frEndptConnDesc = _FrEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 14),
    _FrEndptConnDesc_Type()
)
frEndptConnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptConnDesc.setStatus("mandatory")


class _FrEndptTrkAvoidType_Type(Integer32):
    """Custom type frEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_FrEndptTrkAvoidType_Type.__name__ = "Integer32"
_FrEndptTrkAvoidType_Object = MibTableColumn
frEndptTrkAvoidType = _FrEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 15),
    _FrEndptTrkAvoidType_Type()
)
frEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTrkAvoidType.setStatus("mandatory")


class _FrEndptTrkAvoidZCS_Type(Integer32):
    """Custom type frEndptTrkAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndptTrkAvoidZCS_Type.__name__ = "Integer32"
_FrEndptTrkAvoidZCS_Object = MibTableColumn
frEndptTrkAvoidZCS = _FrEndptTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 16),
    _FrEndptTrkAvoidZCS_Type()
)
frEndptTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTrkAvoidZCS.setStatus("mandatory")


class _FrEndptSubType_Type(Integer32):
    """Custom type frEndptSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atf", 2),
          ("frameRelay", 1),
          ("unknown", 3))
    )


_FrEndptSubType_Type.__name__ = "Integer32"
_FrEndptSubType_Object = MibTableColumn
frEndptSubType = _FrEndptSubType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 17),
    _FrEndptSubType_Type()
)
frEndptSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptSubType.setStatus("mandatory")


class _FrEndptBWClass_Type(Integer32):
    """Custom type frEndptBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrEndptBWClass_Type.__name__ = "Integer32"
_FrEndptBWClass_Object = MibTableColumn
frEndptBWClass = _FrEndptBWClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 18),
    _FrEndptBWClass_Type()
)
frEndptBWClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBWClass.setStatus("mandatory")


class _FrEndptMIR_Type(Integer32):
    """Custom type frEndptMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptMIR_Type.__name__ = "Integer32"
_FrEndptMIR_Object = MibTableColumn
frEndptMIR = _FrEndptMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 19),
    _FrEndptMIR_Type()
)
frEndptMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptMIR.setStatus("mandatory")


class _FrEndptCIR_Type(Integer32):
    """Custom type frEndptCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptCIR_Type.__name__ = "Integer32"
_FrEndptCIR_Object = MibTableColumn
frEndptCIR = _FrEndptCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 20),
    _FrEndptCIR_Type()
)
frEndptCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptCIR.setStatus("mandatory")


class _FrEndptBc_Type(Integer32):
    """Custom type frEndptBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndptBc_Type.__name__ = "Integer32"
_FrEndptBc_Object = MibTableColumn
frEndptBc = _FrEndptBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 21),
    _FrEndptBc_Type()
)
frEndptBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBc.setStatus("mandatory")


class _FrEndptBe_Type(Integer32):
    """Custom type frEndptBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptBe_Type.__name__ = "Integer32"
_FrEndptBe_Object = MibTableColumn
frEndptBe = _FrEndptBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 22),
    _FrEndptBe_Type()
)
frEndptBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptBe.setStatus("mandatory")


class _FrEndptVcQSize_Type(Integer32):
    """Custom type frEndptVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrEndptVcQSize_Type.__name__ = "Integer32"
_FrEndptVcQSize_Object = MibTableColumn
frEndptVcQSize = _FrEndptVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 23),
    _FrEndptVcQSize_Type()
)
frEndptVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptVcQSize.setStatus("mandatory")


class _FrEndptPIR_Type(Integer32):
    """Custom type frEndptPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptPIR_Type.__name__ = "Integer32"
_FrEndptPIR_Object = MibTableColumn
frEndptPIR = _FrEndptPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 24),
    _FrEndptPIR_Type()
)
frEndptPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptPIR.setStatus("mandatory")


class _FrEndptCMAX_Type(Integer32):
    """Custom type frEndptCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrEndptCMAX_Type.__name__ = "Integer32"
_FrEndptCMAX_Object = MibTableColumn
frEndptCMAX = _FrEndptCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 25),
    _FrEndptCMAX_Type()
)
frEndptCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptCMAX.setStatus("mandatory")


class _FrEndptEcnQSize_Type(Integer32):
    """Custom type frEndptEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptEcnQSize_Type.__name__ = "Integer32"
_FrEndptEcnQSize_Object = MibTableColumn
frEndptEcnQSize = _FrEndptEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 26),
    _FrEndptEcnQSize_Type()
)
frEndptEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptEcnQSize.setStatus("mandatory")


class _FrEndptQIR_Type(Integer32):
    """Custom type frEndptQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptQIR_Type.__name__ = "Integer32"
_FrEndptQIR_Object = MibTableColumn
frEndptQIR = _FrEndptQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 27),
    _FrEndptQIR_Type()
)
frEndptQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptQIR.setStatus("mandatory")


class _FrEndptPercUtil_Type(Integer32):
    """Custom type frEndptPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndptPercUtil_Type.__name__ = "Integer32"
_FrEndptPercUtil_Object = MibTableColumn
frEndptPercUtil = _FrEndptPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 28),
    _FrEndptPercUtil_Type()
)
frEndptPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptPercUtil.setStatus("mandatory")


class _FrEndptOeMIR_Type(Integer32):
    """Custom type frEndptOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptOeMIR_Type.__name__ = "Integer32"
_FrEndptOeMIR_Object = MibTableColumn
frEndptOeMIR = _FrEndptOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 29),
    _FrEndptOeMIR_Type()
)
frEndptOeMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeMIR.setStatus("mandatory")


class _FrEndptOeCIR_Type(Integer32):
    """Custom type frEndptOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptOeCIR_Type.__name__ = "Integer32"
_FrEndptOeCIR_Object = MibTableColumn
frEndptOeCIR = _FrEndptOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 30),
    _FrEndptOeCIR_Type()
)
frEndptOeCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeCIR.setStatus("mandatory")


class _FrEndptOeBc_Type(Integer32):
    """Custom type frEndptOeBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeBc_Type.__name__ = "Integer32"
_FrEndptOeBc_Object = MibTableColumn
frEndptOeBc = _FrEndptOeBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 31),
    _FrEndptOeBc_Type()
)
frEndptOeBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeBc.setStatus("mandatory")


class _FrEndptOeBe_Type(Integer32):
    """Custom type frEndptOeBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeBe_Type.__name__ = "Integer32"
_FrEndptOeBe_Object = MibTableColumn
frEndptOeBe = _FrEndptOeBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 32),
    _FrEndptOeBe_Type()
)
frEndptOeBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeBe.setStatus("mandatory")


class _FrEndptOeVcQSize_Type(Integer32):
    """Custom type frEndptOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072000),
    )


_FrEndptOeVcQSize_Type.__name__ = "Integer32"
_FrEndptOeVcQSize_Object = MibTableColumn
frEndptOeVcQSize = _FrEndptOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 33),
    _FrEndptOeVcQSize_Type()
)
frEndptOeVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeVcQSize.setStatus("mandatory")


class _FrEndptOePIR_Type(Integer32):
    """Custom type frEndptOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptOePIR_Type.__name__ = "Integer32"
_FrEndptOePIR_Object = MibTableColumn
frEndptOePIR = _FrEndptOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 34),
    _FrEndptOePIR_Type()
)
frEndptOePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOePIR.setStatus("mandatory")


class _FrEndptOeCMAX_Type(Integer32):
    """Custom type frEndptOeCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 57600),
    )


_FrEndptOeCMAX_Type.__name__ = "Integer32"
_FrEndptOeCMAX_Object = MibTableColumn
frEndptOeCMAX = _FrEndptOeCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 35),
    _FrEndptOeCMAX_Type()
)
frEndptOeCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeCMAX.setStatus("mandatory")


class _FrEndptOeEcnQSize_Type(Integer32):
    """Custom type frEndptOeEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndptOeEcnQSize_Type.__name__ = "Integer32"
_FrEndptOeEcnQSize_Object = MibTableColumn
frEndptOeEcnQSize = _FrEndptOeEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 36),
    _FrEndptOeEcnQSize_Type()
)
frEndptOeEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeEcnQSize.setStatus("mandatory")


class _FrEndptOeQIR_Type(Integer32):
    """Custom type frEndptOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrEndptOeQIR_Type.__name__ = "Integer32"
_FrEndptOeQIR_Object = MibTableColumn
frEndptOeQIR = _FrEndptOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 37),
    _FrEndptOeQIR_Type()
)
frEndptOeQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOeQIR.setStatus("mandatory")


class _FrEndptOePercUtil_Type(Integer32):
    """Custom type frEndptOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndptOePercUtil_Type.__name__ = "Integer32"
_FrEndptOePercUtil_Object = MibTableColumn
frEndptOePercUtil = _FrEndptOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 38),
    _FrEndptOePercUtil_Type()
)
frEndptOePercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptOePercUtil.setStatus("mandatory")


class _FrEndptEnableFST_Type(Integer32):
    """Custom type frEndptEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrEndptEnableFST_Type.__name__ = "Integer32"
_FrEndptEnableFST_Object = MibTableColumn
frEndptEnableFST = _FrEndptEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 39),
    _FrEndptEnableFST_Type()
)
frEndptEnableFST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptEnableFST.setStatus("mandatory")


class _FrEndptConnPrio_Type(Integer32):
    """Custom type frEndptConnPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_FrEndptConnPrio_Type.__name__ = "Integer32"
_FrEndptConnPrio_Object = MibTableColumn
frEndptConnPrio = _FrEndptConnPrio_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 40),
    _FrEndptConnPrio_Type()
)
frEndptConnPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptConnPrio.setStatus("mandatory")


class _FrEndptGroupFlag_Type(Integer32):
    """Custom type frEndptGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrEndptGroupFlag_Type.__name__ = "Integer32"
_FrEndptGroupFlag_Object = MibTableColumn
frEndptGroupFlag = _FrEndptGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 41),
    _FrEndptGroupFlag_Type()
)
frEndptGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptGroupFlag.setStatus("mandatory")


class _FrEndptLocLpbkState_Type(Integer32):
    """Custom type frEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrEndptLocLpbkState_Type.__name__ = "Integer32"
_FrEndptLocLpbkState_Object = MibTableColumn
frEndptLocLpbkState = _FrEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 42),
    _FrEndptLocLpbkState_Type()
)
frEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptLocLpbkState.setStatus("mandatory")


class _FrEndptLocRmtLpbkState_Type(Integer32):
    """Custom type frEndptLocRmtLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrEndptLocRmtLpbkState_Type.__name__ = "Integer32"
_FrEndptLocRmtLpbkState_Object = MibTableColumn
frEndptLocRmtLpbkState = _FrEndptLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 43),
    _FrEndptLocRmtLpbkState_Type()
)
frEndptLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptLocRmtLpbkState.setStatus("mandatory")
_FrEndptLpbkStatus_Type = Integer32
_FrEndptLpbkStatus_Object = MibTableColumn
frEndptLpbkStatus = _FrEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 44),
    _FrEndptLpbkStatus_Type()
)
frEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptLpbkStatus.setStatus("mandatory")


class _FrEndptTestType_Type(Integer32):
    """Custom type frEndptTestType based on Integer32"""
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
        *(("test", 1),
          ("testDelay", 2),
          ("testDelayNoLoop", 4),
          ("testNoLoop", 3),
          ("writeOnly", 5))
    )


_FrEndptTestType_Type.__name__ = "Integer32"
_FrEndptTestType_Object = MibTableColumn
frEndptTestType = _FrEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 45),
    _FrEndptTestType_Type()
)
frEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptTestType.setStatus("mandatory")
_FrEndptRtdTestDelay_Type = Integer32
_FrEndptRtdTestDelay_Object = MibTableColumn
frEndptRtdTestDelay = _FrEndptRtdTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 46),
    _FrEndptRtdTestDelay_Type()
)
frEndptRtdTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRtdTestDelay.setStatus("mandatory")
_FrEndptGroupDesc_Type = DisplayString
_FrEndptGroupDesc_Object = MibTableColumn
frEndptGroupDesc = _FrEndptGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 5, 1, 47),
    _FrEndptGroupDesc_Type()
)
frEndptGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndptGroupDesc.setStatus("mandatory")
_FrEndptStatTable_Object = MibTable
frEndptStatTable = _FrEndptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6)
)
if mibBuilder.loadTexts:
    frEndptStatTable.setStatus("mandatory")
_FrEndptStatEntry_Object = MibTableRow
frEndptStatEntry = _FrEndptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1)
)
frEndptStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptIndex"),
)
if mibBuilder.loadTexts:
    frEndptStatEntry.setStatus("mandatory")
_FrEndptRxBytes_Type = Counter32
_FrEndptRxBytes_Object = MibTableColumn
frEndptRxBytes = _FrEndptRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 1),
    _FrEndptRxBytes_Type()
)
frEndptRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytes.setStatus("mandatory")
_FrEndptRxBytesDscds_Type = Counter32
_FrEndptRxBytesDscds_Object = MibTableColumn
frEndptRxBytesDscds = _FrEndptRxBytesDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 2),
    _FrEndptRxBytesDscds_Type()
)
frEndptRxBytesDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesDscds.setStatus("mandatory")
_FrEndptRxFrms_Type = Counter32
_FrEndptRxFrms_Object = MibTableColumn
frEndptRxFrms = _FrEndptRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 3),
    _FrEndptRxFrms_Type()
)
frEndptRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrms.setStatus("mandatory")
_FrEndptRxFrmsDscds_Type = Counter32
_FrEndptRxFrmsDscds_Object = MibTableColumn
frEndptRxFrmsDscds = _FrEndptRxFrmsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 4),
    _FrEndptRxFrmsDscds_Type()
)
frEndptRxFrmsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDscds.setStatus("mandatory")
_FrEndptRxPkts_Type = Counter32
_FrEndptRxPkts_Object = MibTableColumn
frEndptRxPkts = _FrEndptRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 5),
    _FrEndptRxPkts_Type()
)
frEndptRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxPkts.setStatus("mandatory")
_FrEndptRxPktsDscds_Type = Counter32
_FrEndptRxPktsDscds_Object = MibTableColumn
frEndptRxPktsDscds = _FrEndptRxPktsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 6),
    _FrEndptRxPktsDscds_Type()
)
frEndptRxPktsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxPktsDscds.setStatus("mandatory")
_FrEndptTxBytes_Type = Counter32
_FrEndptTxBytes_Object = MibTableColumn
frEndptTxBytes = _FrEndptTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 7),
    _FrEndptTxBytes_Type()
)
frEndptTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytes.setStatus("mandatory")
_FrEndptTxBytesDscds_Type = Counter32
_FrEndptTxBytesDscds_Object = MibTableColumn
frEndptTxBytesDscds = _FrEndptTxBytesDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 8),
    _FrEndptTxBytesDscds_Type()
)
frEndptTxBytesDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytesDscds.setStatus("mandatory")
_FrEndptTxFrms_Type = Counter32
_FrEndptTxFrms_Object = MibTableColumn
frEndptTxFrms = _FrEndptTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 9),
    _FrEndptTxFrms_Type()
)
frEndptTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrms.setStatus("mandatory")
_FrEndptTxFrmsDscds_Type = Counter32
_FrEndptTxFrmsDscds_Object = MibTableColumn
frEndptTxFrmsDscds = _FrEndptTxFrmsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 10),
    _FrEndptTxFrmsDscds_Type()
)
frEndptTxFrmsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsDscds.setStatus("mandatory")
_FrEndptTxPkts_Type = Counter32
_FrEndptTxPkts_Object = MibTableColumn
frEndptTxPkts = _FrEndptTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 11),
    _FrEndptTxPkts_Type()
)
frEndptTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxPkts.setStatus("mandatory")
_FrEndptTxFrmsFecns_Type = Counter32
_FrEndptTxFrmsFecns_Object = MibTableColumn
frEndptTxFrmsFecns = _FrEndptTxFrmsFecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 12),
    _FrEndptTxFrmsFecns_Type()
)
frEndptTxFrmsFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsFecns.setStatus("mandatory")
_FrEndptTxFrmsBecns_Type = Counter32
_FrEndptTxFrmsBecns_Object = MibTableColumn
frEndptTxFrmsBecns = _FrEndptTxFrmsBecns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 13),
    _FrEndptTxFrmsBecns_Type()
)
frEndptTxFrmsBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsBecns.setStatus("mandatory")
_FrEndptSecInServices_Type = Counter32
_FrEndptSecInServices_Object = MibTableColumn
frEndptSecInServices = _FrEndptSecInServices_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 14),
    _FrEndptSecInServices_Type()
)
frEndptSecInServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptSecInServices.setStatus("mandatory")
_FrEndptCongestMins_Type = Counter32
_FrEndptCongestMins_Object = MibTableColumn
frEndptCongestMins = _FrEndptCongestMins_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 15),
    _FrEndptCongestMins_Type()
)
frEndptCongestMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptCongestMins.setStatus("mandatory")
_FrEndptRxFrmsDes_Type = Counter32
_FrEndptRxFrmsDes_Object = MibTableColumn
frEndptRxFrmsDes = _FrEndptRxFrmsDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 16),
    _FrEndptRxFrmsDes_Type()
)
frEndptRxFrmsDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDes.setStatus("mandatory")
_FrEndptRxBytesDes_Type = Counter32
_FrEndptRxBytesDes_Object = MibTableColumn
frEndptRxBytesDes = _FrEndptRxBytesDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 17),
    _FrEndptRxBytesDes_Type()
)
frEndptRxBytesDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesDes.setStatus("mandatory")
_FrEndptTxFrmsDes_Type = Counter32
_FrEndptTxFrmsDes_Object = MibTableColumn
frEndptTxFrmsDes = _FrEndptTxFrmsDes_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 18),
    _FrEndptTxFrmsDes_Type()
)
frEndptTxFrmsDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsDes.setStatus("mandatory")
_FrEndptRxFrmsDeDscds_Type = Counter32
_FrEndptRxFrmsDeDscds_Object = MibTableColumn
frEndptRxFrmsDeDscds = _FrEndptRxFrmsDeDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 19),
    _FrEndptRxFrmsDeDscds_Type()
)
frEndptRxFrmsDeDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsDeDscds.setStatus("mandatory")
_FrEndptRxFrmsCirs_Type = Counter32
_FrEndptRxFrmsCirs_Object = MibTableColumn
frEndptRxFrmsCirs = _FrEndptRxFrmsCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 20),
    _FrEndptRxFrmsCirs_Type()
)
frEndptRxFrmsCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxFrmsCirs.setStatus("mandatory")
_FrEndptRxBytesCirs_Type = Counter32
_FrEndptRxBytesCirs_Object = MibTableColumn
frEndptRxBytesCirs = _FrEndptRxBytesCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 21),
    _FrEndptRxBytesCirs_Type()
)
frEndptRxBytesCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptRxBytesCirs.setStatus("mandatory")
_FrEndptTxFrmsCirs_Type = Counter32
_FrEndptTxFrmsCirs_Object = MibTableColumn
frEndptTxFrmsCirs = _FrEndptTxFrmsCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 22),
    _FrEndptTxFrmsCirs_Type()
)
frEndptTxFrmsCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxFrmsCirs.setStatus("mandatory")
_FrEndptTxBytesCirs_Type = Counter32
_FrEndptTxBytesCirs_Object = MibTableColumn
frEndptTxBytesCirs = _FrEndptTxBytesCirs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 6, 1, 23),
    _FrEndptTxBytesCirs_Type()
)
frEndptTxBytesCirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptTxBytesCirs.setStatus("mandatory")
_FrBwClassTable_Object = MibTable
frBwClassTable = _FrBwClassTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7)
)
if mibBuilder.loadTexts:
    frBwClassTable.setStatus("mandatory")
_FrBwClassEntry_Object = MibTableRow
frBwClassEntry = _FrBwClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1)
)
frBwClassEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frBwClassIndex"),
)
if mibBuilder.loadTexts:
    frBwClassEntry.setStatus("mandatory")


class _FrBwClassIndex_Type(Integer32):
    """Custom type frBwClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrBwClassIndex_Type.__name__ = "Integer32"
_FrBwClassIndex_Object = MibTableColumn
frBwClassIndex = _FrBwClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 1),
    _FrBwClassIndex_Type()
)
frBwClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassIndex.setStatus("mandatory")


class _FrBwClassMIR_Type(Integer32):
    """Custom type frBwClassMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassMIR_Type.__name__ = "Integer32"
_FrBwClassMIR_Object = MibTableColumn
frBwClassMIR = _FrBwClassMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 2),
    _FrBwClassMIR_Type()
)
frBwClassMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassMIR.setStatus("mandatory")


class _FrBwClassCIR_Type(Integer32):
    """Custom type frBwClassCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassCIR_Type.__name__ = "Integer32"
_FrBwClassCIR_Object = MibTableColumn
frBwClassCIR = _FrBwClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 3),
    _FrBwClassCIR_Type()
)
frBwClassCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassCIR.setStatus("mandatory")


class _FrBwClassVcQSize_Type(Integer32):
    """Custom type frBwClassVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrBwClassVcQSize_Type.__name__ = "Integer32"
_FrBwClassVcQSize_Object = MibTableColumn
frBwClassVcQSize = _FrBwClassVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 4),
    _FrBwClassVcQSize_Type()
)
frBwClassVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassVcQSize.setStatus("mandatory")


class _FrBwClassBc_Type(Integer32):
    """Custom type frBwClassBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrBwClassBc_Type.__name__ = "Integer32"
_FrBwClassBc_Object = MibTableColumn
frBwClassBc = _FrBwClassBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 5),
    _FrBwClassBc_Type()
)
frBwClassBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassBc.setStatus("mandatory")


class _FrBwClassPIR_Type(Integer32):
    """Custom type frBwClassPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassPIR_Type.__name__ = "Integer32"
_FrBwClassPIR_Object = MibTableColumn
frBwClassPIR = _FrBwClassPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 6),
    _FrBwClassPIR_Type()
)
frBwClassPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassPIR.setStatus("mandatory")


class _FrBwClassBe_Type(Integer32):
    """Custom type frBwClassBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassBe_Type.__name__ = "Integer32"
_FrBwClassBe_Object = MibTableColumn
frBwClassBe = _FrBwClassBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 7),
    _FrBwClassBe_Type()
)
frBwClassBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassBe.setStatus("mandatory")


class _FrBwClassCMAX_Type(Integer32):
    """Custom type frBwClassCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrBwClassCMAX_Type.__name__ = "Integer32"
_FrBwClassCMAX_Object = MibTableColumn
frBwClassCMAX = _FrBwClassCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 8),
    _FrBwClassCMAX_Type()
)
frBwClassCMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassCMAX.setStatus("mandatory")


class _FrBwClassEcnQSize_Type(Integer32):
    """Custom type frBwClassEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassEcnQSize_Type.__name__ = "Integer32"
_FrBwClassEcnQSize_Object = MibTableColumn
frBwClassEcnQSize = _FrBwClassEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 9),
    _FrBwClassEcnQSize_Type()
)
frBwClassEcnQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassEcnQSize.setStatus("mandatory")


class _FrBwClassQIR_Type(Integer32):
    """Custom type frBwClassQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassQIR_Type.__name__ = "Integer32"
_FrBwClassQIR_Object = MibTableColumn
frBwClassQIR = _FrBwClassQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 10),
    _FrBwClassQIR_Type()
)
frBwClassQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassQIR.setStatus("mandatory")


class _FrBwClassPercUtil_Type(Integer32):
    """Custom type frBwClassPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrBwClassPercUtil_Type.__name__ = "Integer32"
_FrBwClassPercUtil_Object = MibTableColumn
frBwClassPercUtil = _FrBwClassPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 11),
    _FrBwClassPercUtil_Type()
)
frBwClassPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassPercUtil.setStatus("mandatory")


class _FrBwClassOeMIR_Type(Integer32):
    """Custom type frBwClassOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassOeMIR_Type.__name__ = "Integer32"
_FrBwClassOeMIR_Object = MibTableColumn
frBwClassOeMIR = _FrBwClassOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 12),
    _FrBwClassOeMIR_Type()
)
frBwClassOeMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeMIR.setStatus("mandatory")


class _FrBwClassOeCIR_Type(Integer32):
    """Custom type frBwClassOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassOeCIR_Type.__name__ = "Integer32"
_FrBwClassOeCIR_Object = MibTableColumn
frBwClassOeCIR = _FrBwClassOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 13),
    _FrBwClassOeCIR_Type()
)
frBwClassOeCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeCIR.setStatus("mandatory")


class _FrBwClassOeVcQSize_Type(Integer32):
    """Custom type frBwClassOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072000),
    )


_FrBwClassOeVcQSize_Type.__name__ = "Integer32"
_FrBwClassOeVcQSize_Object = MibTableColumn
frBwClassOeVcQSize = _FrBwClassOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 14),
    _FrBwClassOeVcQSize_Type()
)
frBwClassOeVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeVcQSize.setStatus("mandatory")


class _FrBwClassOeBc_Type(Integer32):
    """Custom type frBwClassOeBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeBc_Type.__name__ = "Integer32"
_FrBwClassOeBc_Object = MibTableColumn
frBwClassOeBc = _FrBwClassOeBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 15),
    _FrBwClassOeBc_Type()
)
frBwClassOeBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeBc.setStatus("mandatory")


class _FrBwClassOePIR_Type(Integer32):
    """Custom type frBwClassOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassOePIR_Type.__name__ = "Integer32"
_FrBwClassOePIR_Object = MibTableColumn
frBwClassOePIR = _FrBwClassOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 16),
    _FrBwClassOePIR_Type()
)
frBwClassOePIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOePIR.setStatus("mandatory")


class _FrBwClassOeBe_Type(Integer32):
    """Custom type frBwClassOeBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeBe_Type.__name__ = "Integer32"
_FrBwClassOeBe_Object = MibTableColumn
frBwClassOeBe = _FrBwClassOeBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 17),
    _FrBwClassOeBe_Type()
)
frBwClassOeBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeBe.setStatus("mandatory")


class _FrBwClassOeCMAX_Type(Integer32):
    """Custom type frBwClassOeCMAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 57600),
    )


_FrBwClassOeCMAX_Type.__name__ = "Integer32"
_FrBwClassOeCMAX_Object = MibTableColumn
frBwClassOeCMAX = _FrBwClassOeCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 18),
    _FrBwClassOeCMAX_Type()
)
frBwClassOeCMAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeCMAX.setStatus("mandatory")


class _FrBwClassOeEcnQSize_Type(Integer32):
    """Custom type frBwClassOeEcnQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrBwClassOeEcnQSize_Type.__name__ = "Integer32"
_FrBwClassOeEcnQSize_Object = MibTableColumn
frBwClassOeEcnQSize = _FrBwClassOeEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 19),
    _FrBwClassOeEcnQSize_Type()
)
frBwClassOeEcnQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeEcnQSize.setStatus("mandatory")


class _FrBwClassOeQIR_Type(Integer32):
    """Custom type frBwClassOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_FrBwClassOeQIR_Type.__name__ = "Integer32"
_FrBwClassOeQIR_Object = MibTableColumn
frBwClassOeQIR = _FrBwClassOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 20),
    _FrBwClassOeQIR_Type()
)
frBwClassOeQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOeQIR.setStatus("mandatory")


class _FrBwClassOePercUtil_Type(Integer32):
    """Custom type frBwClassOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrBwClassOePercUtil_Type.__name__ = "Integer32"
_FrBwClassOePercUtil_Object = MibTableColumn
frBwClassOePercUtil = _FrBwClassOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 21),
    _FrBwClassOePercUtil_Type()
)
frBwClassOePercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassOePercUtil.setStatus("mandatory")


class _FrBwClassEnableFST_Type(Integer32):
    """Custom type frBwClassEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FrBwClassEnableFST_Type.__name__ = "Integer32"
_FrBwClassEnableFST_Object = MibTableColumn
frBwClassEnableFST = _FrBwClassEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 22),
    _FrBwClassEnableFST_Type()
)
frBwClassEnableFST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassEnableFST.setStatus("mandatory")


class _FrBwClassDescription_Type(DisplayString):
    """Custom type frBwClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FrBwClassDescription_Type.__name__ = "DisplayString"
_FrBwClassDescription_Object = MibTableColumn
frBwClassDescription = _FrBwClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 7, 1, 23),
    _FrBwClassDescription_Type()
)
frBwClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBwClassDescription.setStatus("mandatory")
_AtmEndptTable_Object = MibTable
atmEndptTable = _AtmEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8)
)
if mibBuilder.loadTexts:
    atmEndptTable.setStatus("mandatory")
_AtmEndptEntry_Object = MibTableRow
atmEndptEntry = _AtmEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1)
)
atmEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptIndex"),
)
if mibBuilder.loadTexts:
    atmEndptEntry.setStatus("mandatory")


class _AtmEndptIndex_Type(Integer32):
    """Custom type atmEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AtmEndptIndex_Type.__name__ = "Integer32"
_AtmEndptIndex_Object = MibTableColumn
atmEndptIndex = _AtmEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 1),
    _AtmEndptIndex_Type()
)
atmEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptIndex.setStatus("mandatory")
_AtmEndptDesc_Type = DisplayString
_AtmEndptDesc_Object = MibTableColumn
atmEndptDesc = _AtmEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 2),
    _AtmEndptDesc_Type()
)
atmEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptDesc.setStatus("mandatory")


class _AtmOtherEndptIndex_Type(Integer32):
    """Custom type atmOtherEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AtmOtherEndptIndex_Type.__name__ = "Integer32"
_AtmOtherEndptIndex_Object = MibTableColumn
atmOtherEndptIndex = _AtmOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 3),
    _AtmOtherEndptIndex_Type()
)
atmOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOtherEndptIndex.setStatus("mandatory")
_AtmOtherEndptDesc_Type = DisplayString
_AtmOtherEndptDesc_Object = MibTableColumn
atmOtherEndptDesc = _AtmOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 4),
    _AtmOtherEndptDesc_Type()
)
atmOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOtherEndptDesc.setStatus("mandatory")


class _AtmEndptAdminStatus_Type(Integer32):
    """Custom type atmEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_AtmEndptAdminStatus_Type.__name__ = "Integer32"
_AtmEndptAdminStatus_Object = MibTableColumn
atmEndptAdminStatus = _AtmEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 5),
    _AtmEndptAdminStatus_Type()
)
atmEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptAdminStatus.setStatus("mandatory")


class _AtmEndptOperStatus_Type(Integer32):
    """Custom type atmEndptOperStatus based on Integer32"""
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
        *(("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("looped", 8),
          ("ok", 1),
          ("okPendingDelete", 7),
          ("okPendingDown", 2),
          ("okPendingRoute", 6),
          ("unknown", 9))
    )


_AtmEndptOperStatus_Type.__name__ = "Integer32"
_AtmEndptOperStatus_Object = MibTableColumn
atmEndptOperStatus = _AtmEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 6),
    _AtmEndptOperStatus_Type()
)
atmEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOperStatus.setStatus("mandatory")


class _AtmNoRouteFoundFailure_Type(Integer32):
    """Custom type atmNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmNoRouteFoundFailure_Type.__name__ = "Integer32"
_AtmNoRouteFoundFailure_Object = MibTableColumn
atmNoRouteFoundFailure = _AtmNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 7),
    _AtmNoRouteFoundFailure_Type()
)
atmNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNoRouteFoundFailure.setStatus("mandatory")


class _AtmBumpFailure_Type(Integer32):
    """Custom type atmBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmBumpFailure_Type.__name__ = "Integer32"
_AtmBumpFailure_Object = MibTableColumn
atmBumpFailure = _AtmBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 8),
    _AtmBumpFailure_Type()
)
atmBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBumpFailure.setStatus("mandatory")


class _AtmEndPointFailure_Type(Integer32):
    """Custom type atmEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndPointFailure_Type.__name__ = "Integer32"
_AtmEndPointFailure_Object = MibTableColumn
atmEndPointFailure = _AtmEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 9),
    _AtmEndPointFailure_Type()
)
atmEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointFailure.setStatus("mandatory")


class _AtmTestFailure_Type(Integer32):
    """Custom type atmTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmTestFailure_Type.__name__ = "Integer32"
_AtmTestFailure_Object = MibTableColumn
atmTestFailure = _AtmTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 10),
    _AtmTestFailure_Type()
)
atmTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTestFailure.setStatus("mandatory")
_AtmConnPtr_Type = ObjectIdentifier
_AtmConnPtr_Object = MibTableColumn
atmConnPtr = _AtmConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 11),
    _AtmConnPtr_Type()
)
atmConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmConnPtr.setStatus("mandatory")
_AtmNextPtr_Type = ObjectIdentifier
_AtmNextPtr_Object = MibTableColumn
atmNextPtr = _AtmNextPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 12),
    _AtmNextPtr_Type()
)
atmNextPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNextPtr.setStatus("mandatory")
_AtmNextOnPortPtr_Type = ObjectIdentifier
_AtmNextOnPortPtr_Object = MibTableColumn
atmNextOnPortPtr = _AtmNextOnPortPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 13),
    _AtmNextOnPortPtr_Type()
)
atmNextOnPortPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNextOnPortPtr.setStatus("mandatory")


class _AtmEndptConnDesc_Type(DisplayString):
    """Custom type atmEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtmEndptConnDesc_Type.__name__ = "DisplayString"
_AtmEndptConnDesc_Object = MibTableColumn
atmEndptConnDesc = _AtmEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 14),
    _AtmEndptConnDesc_Type()
)
atmEndptConnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptConnDesc.setStatus("mandatory")


class _AtmEndptTrkAvoidType_Type(Integer32):
    """Custom type atmEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_AtmEndptTrkAvoidType_Type.__name__ = "Integer32"
_AtmEndptTrkAvoidType_Object = MibTableColumn
atmEndptTrkAvoidType = _AtmEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 15),
    _AtmEndptTrkAvoidType_Type()
)
atmEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTrkAvoidType.setStatus("mandatory")


class _AtmEndptTrkAvoidZCS_Type(Integer32):
    """Custom type atmEndptTrkAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndptTrkAvoidZCS_Type.__name__ = "Integer32"
_AtmEndptTrkAvoidZCS_Object = MibTableColumn
atmEndptTrkAvoidZCS = _AtmEndptTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 16),
    _AtmEndptTrkAvoidZCS_Type()
)
atmEndptTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTrkAvoidZCS.setStatus("mandatory")


class _AtmEndptSubType_Type(Integer32):
    """Custom type atmEndptSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("atf", 1),
          ("atfst", 6),
          ("cbr", 3),
          ("unknown", 4),
          ("vbr", 2))
    )


_AtmEndptSubType_Type.__name__ = "Integer32"
_AtmEndptSubType_Object = MibTableColumn
atmEndptSubType = _AtmEndptSubType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 17),
    _AtmEndptSubType_Type()
)
atmEndptSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptSubType.setStatus("mandatory")


class _AtmEndptBWClass_Type(Integer32):
    """Custom type atmEndptBWClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmEndptBWClass_Type.__name__ = "Integer32"
_AtmEndptBWClass_Object = MibTableColumn
atmEndptBWClass = _AtmEndptBWClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 18),
    _AtmEndptBWClass_Type()
)
atmEndptBWClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptBWClass.setStatus("mandatory")


class _AtmEndptMIR_Type(Integer32):
    """Custom type atmEndptMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmEndptMIR_Type.__name__ = "Integer32"
_AtmEndptMIR_Object = MibTableColumn
atmEndptMIR = _AtmEndptMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 19),
    _AtmEndptMIR_Type()
)
atmEndptMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptMIR.setStatus("mandatory")


class _AtmEndptCIR_Type(Integer32):
    """Custom type atmEndptCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptCIR_Type.__name__ = "Integer32"
_AtmEndptCIR_Object = MibTableColumn
atmEndptCIR = _AtmEndptCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 20),
    _AtmEndptCIR_Type()
)
atmEndptCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCIR.setStatus("mandatory")


class _AtmEndptVcQSize_Type(Integer32):
    """Custom type atmEndptVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndptVcQSize_Type.__name__ = "Integer32"
_AtmEndptVcQSize_Object = MibTableColumn
atmEndptVcQSize = _AtmEndptVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 21),
    _AtmEndptVcQSize_Type()
)
atmEndptVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptVcQSize.setStatus("mandatory")


class _AtmEndptPIR_Type(Integer32):
    """Custom type atmEndptPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptPIR_Type.__name__ = "Integer32"
_AtmEndptPIR_Object = MibTableColumn
atmEndptPIR = _AtmEndptPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 22),
    _AtmEndptPIR_Type()
)
atmEndptPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPIR.setStatus("mandatory")


class _AtmEndptEfciQSize_Type(Integer32):
    """Custom type atmEndptEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptEfciQSize_Type.__name__ = "Integer32"
_AtmEndptEfciQSize_Object = MibTableColumn
atmEndptEfciQSize = _AtmEndptEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 23),
    _AtmEndptEfciQSize_Type()
)
atmEndptEfciQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptEfciQSize.setStatus("mandatory")


class _AtmEndptQIR_Type(Integer32):
    """Custom type atmEndptQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmEndptQIR_Type.__name__ = "Integer32"
_AtmEndptQIR_Object = MibTableColumn
atmEndptQIR = _AtmEndptQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 24),
    _AtmEndptQIR_Type()
)
atmEndptQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptQIR.setStatus("mandatory")


class _AtmEndptPercUtil_Type(Integer32):
    """Custom type atmEndptPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptPercUtil_Type.__name__ = "Integer32"
_AtmEndptPercUtil_Object = MibTableColumn
atmEndptPercUtil = _AtmEndptPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 25),
    _AtmEndptPercUtil_Type()
)
atmEndptPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPercUtil.setStatus("mandatory")


class _AtmEndptCBS_Type(Integer32):
    """Custom type atmEndptCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmEndptCBS_Type.__name__ = "Integer32"
_AtmEndptCBS_Object = MibTableColumn
atmEndptCBS = _AtmEndptCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 26),
    _AtmEndptCBS_Type()
)
atmEndptCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCBS.setStatus("mandatory")


class _AtmEndptIBS_Type(Integer32):
    """Custom type atmEndptIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmEndptIBS_Type.__name__ = "Integer32"
_AtmEndptIBS_Object = MibTableColumn
atmEndptIBS = _AtmEndptIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 27),
    _AtmEndptIBS_Type()
)
atmEndptIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptIBS.setStatus("mandatory")


class _AtmEndptMFS_Type(Integer32):
    """Custom type atmEndptMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmEndptMFS_Type.__name__ = "Integer32"
_AtmEndptMFS_Object = MibTableColumn
atmEndptMFS = _AtmEndptMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 28),
    _AtmEndptMFS_Type()
)
atmEndptMFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptMFS.setStatus("mandatory")


class _AtmEndptCCDV_Type(Integer32):
    """Custom type atmEndptCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmEndptCCDV_Type.__name__ = "Integer32"
_AtmEndptCCDV_Object = MibTableColumn
atmEndptCCDV = _AtmEndptCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 29),
    _AtmEndptCCDV_Type()
)
atmEndptCCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCCDV.setStatus("mandatory")


class _AtmEndptHiCLP_Type(Integer32):
    """Custom type atmEndptHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptHiCLP_Type.__name__ = "Integer32"
_AtmEndptHiCLP_Object = MibTableColumn
atmEndptHiCLP = _AtmEndptHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 30),
    _AtmEndptHiCLP_Type()
)
atmEndptHiCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptHiCLP.setStatus("mandatory")


class _AtmEndptLoCLP_Type(Integer32):
    """Custom type atmEndptLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptLoCLP_Type.__name__ = "Integer32"
_AtmEndptLoCLP_Object = MibTableColumn
atmEndptLoCLP = _AtmEndptLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 31),
    _AtmEndptLoCLP_Type()
)
atmEndptLoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLoCLP.setStatus("mandatory")


class _AtmEndptOeMIR_Type(Integer32):
    """Custom type atmEndptOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmEndptOeMIR_Type.__name__ = "Integer32"
_AtmEndptOeMIR_Object = MibTableColumn
atmEndptOeMIR = _AtmEndptOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 32),
    _AtmEndptOeMIR_Type()
)
atmEndptOeMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeMIR.setStatus("mandatory")


class _AtmEndptOeCIR_Type(Integer32):
    """Custom type atmEndptOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptOeCIR_Type.__name__ = "Integer32"
_AtmEndptOeCIR_Object = MibTableColumn
atmEndptOeCIR = _AtmEndptOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 33),
    _AtmEndptOeCIR_Type()
)
atmEndptOeCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCIR.setStatus("mandatory")


class _AtmEndptOeVcQSize_Type(Integer32):
    """Custom type atmEndptOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndptOeVcQSize_Type.__name__ = "Integer32"
_AtmEndptOeVcQSize_Object = MibTableColumn
atmEndptOeVcQSize = _AtmEndptOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 34),
    _AtmEndptOeVcQSize_Type()
)
atmEndptOeVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeVcQSize.setStatus("mandatory")


class _AtmEndptOePIR_Type(Integer32):
    """Custom type atmEndptOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptOePIR_Type.__name__ = "Integer32"
_AtmEndptOePIR_Object = MibTableColumn
atmEndptOePIR = _AtmEndptOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 35),
    _AtmEndptOePIR_Type()
)
atmEndptOePIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOePIR.setStatus("mandatory")


class _AtmEndptOeEfciQSize_Type(Integer32):
    """Custom type atmEndptOeEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeEfciQSize_Type.__name__ = "Integer32"
_AtmEndptOeEfciQSize_Object = MibTableColumn
atmEndptOeEfciQSize = _AtmEndptOeEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 36),
    _AtmEndptOeEfciQSize_Type()
)
atmEndptOeEfciQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeEfciQSize.setStatus("mandatory")


class _AtmEndptOeQIR_Type(Integer32):
    """Custom type atmEndptOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmEndptOeQIR_Type.__name__ = "Integer32"
_AtmEndptOeQIR_Object = MibTableColumn
atmEndptOeQIR = _AtmEndptOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 37),
    _AtmEndptOeQIR_Type()
)
atmEndptOeQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeQIR.setStatus("mandatory")


class _AtmEndptOePercUtil_Type(Integer32):
    """Custom type atmEndptOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOePercUtil_Type.__name__ = "Integer32"
_AtmEndptOePercUtil_Object = MibTableColumn
atmEndptOePercUtil = _AtmEndptOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 38),
    _AtmEndptOePercUtil_Type()
)
atmEndptOePercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOePercUtil.setStatus("mandatory")


class _AtmEndptOeCBS_Type(Integer32):
    """Custom type atmEndptOeCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmEndptOeCBS_Type.__name__ = "Integer32"
_AtmEndptOeCBS_Object = MibTableColumn
atmEndptOeCBS = _AtmEndptOeCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 39),
    _AtmEndptOeCBS_Type()
)
atmEndptOeCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCBS.setStatus("mandatory")


class _AtmEndptOeIBS_Type(Integer32):
    """Custom type atmEndptOeIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmEndptOeIBS_Type.__name__ = "Integer32"
_AtmEndptOeIBS_Object = MibTableColumn
atmEndptOeIBS = _AtmEndptOeIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 40),
    _AtmEndptOeIBS_Type()
)
atmEndptOeIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeIBS.setStatus("mandatory")


class _AtmEndptOeMFS_Type(Integer32):
    """Custom type atmEndptOeMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmEndptOeMFS_Type.__name__ = "Integer32"
_AtmEndptOeMFS_Object = MibTableColumn
atmEndptOeMFS = _AtmEndptOeMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 41),
    _AtmEndptOeMFS_Type()
)
atmEndptOeMFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeMFS.setStatus("mandatory")


class _AtmEndptOeCCDV_Type(Integer32):
    """Custom type atmEndptOeCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmEndptOeCCDV_Type.__name__ = "Integer32"
_AtmEndptOeCCDV_Object = MibTableColumn
atmEndptOeCCDV = _AtmEndptOeCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 42),
    _AtmEndptOeCCDV_Type()
)
atmEndptOeCCDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCCDV.setStatus("mandatory")


class _AtmEndptOeHiCLP_Type(Integer32):
    """Custom type atmEndptOeHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeHiCLP_Type.__name__ = "Integer32"
_AtmEndptOeHiCLP_Object = MibTableColumn
atmEndptOeHiCLP = _AtmEndptOeHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 43),
    _AtmEndptOeHiCLP_Type()
)
atmEndptOeHiCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeHiCLP.setStatus("mandatory")


class _AtmEndptOeLoCLP_Type(Integer32):
    """Custom type atmEndptOeLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptOeLoCLP_Type.__name__ = "Integer32"
_AtmEndptOeLoCLP_Object = MibTableColumn
atmEndptOeLoCLP = _AtmEndptOeLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 44),
    _AtmEndptOeLoCLP_Type()
)
atmEndptOeLoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeLoCLP.setStatus("mandatory")


class _AtmEndptCLPTagging_Type(Integer32):
    """Custom type atmEndptCLPTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptCLPTagging_Type.__name__ = "Integer32"
_AtmEndptCLPTagging_Object = MibTableColumn
atmEndptCLPTagging = _AtmEndptCLPTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 45),
    _AtmEndptCLPTagging_Type()
)
atmEndptCLPTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCLPTagging.setStatus("mandatory")


class _AtmEndptUPC_Type(Integer32):
    """Custom type atmEndptUPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptUPC_Type.__name__ = "Integer32"
_AtmEndptUPC_Object = MibTableColumn
atmEndptUPC = _AtmEndptUPC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 46),
    _AtmEndptUPC_Type()
)
atmEndptUPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptUPC.setStatus("mandatory")


class _AtmEndptEnableFST_Type(Integer32):
    """Custom type atmEndptEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptEnableFST_Type.__name__ = "Integer32"
_AtmEndptEnableFST_Object = MibTableColumn
atmEndptEnableFST = _AtmEndptEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 47),
    _AtmEndptEnableFST_Type()
)
atmEndptEnableFST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptEnableFST.setStatus("mandatory")


class _AtmEndptRateUpICA_Type(Integer32):
    """Custom type atmEndptRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmEndptRateUpICA_Type.__name__ = "Integer32"
_AtmEndptRateUpICA_Object = MibTableColumn
atmEndptRateUpICA = _AtmEndptRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 48),
    _AtmEndptRateUpICA_Type()
)
atmEndptRateUpICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptRateUpICA.setStatus("mandatory")


class _AtmEndptRateDnICA_Type(Integer32):
    """Custom type atmEndptRateDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptRateDnICA_Type.__name__ = "Integer32"
_AtmEndptRateDnICA_Object = MibTableColumn
atmEndptRateDnICA = _AtmEndptRateDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 49),
    _AtmEndptRateDnICA_Type()
)
atmEndptRateDnICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptRateDnICA.setStatus("mandatory")


class _AtmEndptFastDnICA_Type(Integer32):
    """Custom type atmEndptFastDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndptFastDnICA_Type.__name__ = "Integer32"
_AtmEndptFastDnICA_Object = MibTableColumn
atmEndptFastDnICA = _AtmEndptFastDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 50),
    _AtmEndptFastDnICA_Type()
)
atmEndptFastDnICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptFastDnICA.setStatus("mandatory")


class _AtmEndptToQIR_Type(Integer32):
    """Custom type atmEndptToQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmEndptToQIR_Type.__name__ = "Integer32"
_AtmEndptToQIR_Object = MibTableColumn
atmEndptToQIR = _AtmEndptToQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 51),
    _AtmEndptToQIR_Type()
)
atmEndptToQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptToQIR.setStatus("mandatory")


class _AtmEndptMinAdjustICA_Type(Integer32):
    """Custom type atmEndptMinAdjustICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 250),
    )


_AtmEndptMinAdjustICA_Type.__name__ = "Integer32"
_AtmEndptMinAdjustICA_Object = MibTableColumn
atmEndptMinAdjustICA = _AtmEndptMinAdjustICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 52),
    _AtmEndptMinAdjustICA_Type()
)
atmEndptMinAdjustICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptMinAdjustICA.setStatus("mandatory")


class _AtmEndptGroupFlag_Type(Integer32):
    """Custom type atmEndptGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmEndptGroupFlag_Type.__name__ = "Integer32"
_AtmEndptGroupFlag_Object = MibTableColumn
atmEndptGroupFlag = _AtmEndptGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 53),
    _AtmEndptGroupFlag_Type()
)
atmEndptGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptGroupFlag.setStatus("mandatory")


class _AtmEndptOamStatus_Type(Integer32):
    """Custom type atmEndptOamStatus based on Integer32"""
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
        *(("aisDetected", 3),
          ("clear", 2),
          ("ferfDetected", 4),
          ("unknown", 1))
    )


_AtmEndptOamStatus_Type.__name__ = "Integer32"
_AtmEndptOamStatus_Object = MibTableColumn
atmEndptOamStatus = _AtmEndptOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 54),
    _AtmEndptOamStatus_Type()
)
atmEndptOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptOamStatus.setStatus("mandatory")


class _AtmEndptBCM_Type(Integer32):
    """Custom type atmEndptBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptBCM_Type.__name__ = "Integer32"
_AtmEndptBCM_Object = MibTableColumn
atmEndptBCM = _AtmEndptBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 55),
    _AtmEndptBCM_Type()
)
atmEndptBCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptBCM.setStatus("mandatory")


class _AtmEndptFGCRA_Type(Integer32):
    """Custom type atmEndptFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptFGCRA_Type.__name__ = "Integer32"
_AtmEndptFGCRA_Object = MibTableColumn
atmEndptFGCRA = _AtmEndptFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 56),
    _AtmEndptFGCRA_Type()
)
atmEndptFGCRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptFGCRA.setStatus("mandatory")


class _AtmEndptLocLpbkState_Type(Integer32):
    """Custom type atmEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptLocLpbkState_Type.__name__ = "Integer32"
_AtmEndptLocLpbkState_Object = MibTableColumn
atmEndptLocLpbkState = _AtmEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 57),
    _AtmEndptLocLpbkState_Type()
)
atmEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLocLpbkState.setStatus("mandatory")
_AtmEndptLpbkStatus_Type = Integer32
_AtmEndptLpbkStatus_Object = MibTableColumn
atmEndptLpbkStatus = _AtmEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 58),
    _AtmEndptLpbkStatus_Type()
)
atmEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptLpbkStatus.setStatus("mandatory")


class _AtmEndptTestType_Type(Integer32):
    """Custom type atmEndptTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testDelay", 1),
          ("writeOnly", 2))
    )


_AtmEndptTestType_Type.__name__ = "Integer32"
_AtmEndptTestType_Object = MibTableColumn
atmEndptTestType = _AtmEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 59),
    _AtmEndptTestType_Type()
)
atmEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTestType.setStatus("mandatory")
_AtmEndptRtdTestDelay_Type = Integer32
_AtmEndptRtdTestDelay_Object = MibTableColumn
atmEndptRtdTestDelay = _AtmEndptRtdTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 60),
    _AtmEndptRtdTestDelay_Type()
)
atmEndptRtdTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptRtdTestDelay.setStatus("mandatory")


class _AtmEndptOeBCM_Type(Integer32):
    """Custom type atmEndptOeBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptOeBCM_Type.__name__ = "Integer32"
_AtmEndptOeBCM_Object = MibTableColumn
atmEndptOeBCM = _AtmEndptOeBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 61),
    _AtmEndptOeBCM_Type()
)
atmEndptOeBCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeBCM.setStatus("mandatory")


class _AtmEndptOeFGCRA_Type(Integer32):
    """Custom type atmEndptOeFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptOeFGCRA_Type.__name__ = "Integer32"
_AtmEndptOeFGCRA_Object = MibTableColumn
atmEndptOeFGCRA = _AtmEndptOeFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 62),
    _AtmEndptOeFGCRA_Type()
)
atmEndptOeFGCRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeFGCRA.setStatus("mandatory")
_AtmEndptGroupDesc_Type = DisplayString
_AtmEndptGroupDesc_Object = MibTableColumn
atmEndptGroupDesc = _AtmEndptGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 63),
    _AtmEndptGroupDesc_Type()
)
atmEndptGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptGroupDesc.setStatus("mandatory")


class _AtmEndptLocRmtLpbkState_Type(Integer32):
    """Custom type atmEndptLocRmtLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptLocRmtLpbkState_Type.__name__ = "Integer32"
_AtmEndptLocRmtLpbkState_Object = MibTableColumn
atmEndptLocRmtLpbkState = _AtmEndptLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 64),
    _AtmEndptLocRmtLpbkState_Type()
)
atmEndptLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptLocRmtLpbkState.setStatus("mandatory")


class _AtmEndptScrPlc_Type(Integer32):
    """Custom type atmEndptScrPlc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp0and1", 2),
          ("off", 3))
    )


_AtmEndptScrPlc_Type.__name__ = "Integer32"
_AtmEndptScrPlc_Object = MibTableColumn
atmEndptScrPlc = _AtmEndptScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 65),
    _AtmEndptScrPlc_Type()
)
atmEndptScrPlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptScrPlc.setStatus("mandatory")


class _AtmEndptOeScrPlc_Type(Integer32):
    """Custom type atmEndptOeScrPlc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp0and1", 2),
          ("off", 3))
    )


_AtmEndptOeScrPlc_Type.__name__ = "Integer32"
_AtmEndptOeScrPlc_Object = MibTableColumn
atmEndptOeScrPlc = _AtmEndptOeScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 66),
    _AtmEndptOeScrPlc_Type()
)
atmEndptOeScrPlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeScrPlc.setStatus("mandatory")


class _AtmEndptPCR0_Type(Integer32):
    """Custom type atmEndptPCR0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptPCR0_Type.__name__ = "Integer32"
_AtmEndptPCR0_Object = MibTableColumn
atmEndptPCR0 = _AtmEndptPCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 67),
    _AtmEndptPCR0_Type()
)
atmEndptPCR0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPCR0.setStatus("mandatory")


class _AtmEndptOePCR0_Type(Integer32):
    """Custom type atmEndptOePCR0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmEndptOePCR0_Type.__name__ = "Integer32"
_AtmEndptOePCR0_Object = MibTableColumn
atmEndptOePCR0 = _AtmEndptOePCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 68),
    _AtmEndptOePCR0_Type()
)
atmEndptOePCR0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOePCR0.setStatus("mandatory")


class _AtmEndptCDVT0_Type(Integer32):
    """Custom type atmEndptCDVT0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250000),
    )


_AtmEndptCDVT0_Type.__name__ = "Integer32"
_AtmEndptCDVT0_Object = MibTableColumn
atmEndptCDVT0 = _AtmEndptCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 69),
    _AtmEndptCDVT0_Type()
)
atmEndptCDVT0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptCDVT0.setStatus("mandatory")


class _AtmEndptOeCDVT0_Type(Integer32):
    """Custom type atmEndptOeCDVT0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250000),
    )


_AtmEndptOeCDVT0_Type.__name__ = "Integer32"
_AtmEndptOeCDVT0_Object = MibTableColumn
atmEndptOeCDVT0 = _AtmEndptOeCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 70),
    _AtmEndptOeCDVT0_Type()
)
atmEndptOeCDVT0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeCDVT0.setStatus("mandatory")


class _AtmEndptOeRateUpICA_Type(Integer32):
    """Custom type atmEndptOeRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmEndptOeRateUpICA_Type.__name__ = "Integer32"
_AtmEndptOeRateUpICA_Object = MibTableColumn
atmEndptOeRateUpICA = _AtmEndptOeRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 71),
    _AtmEndptOeRateUpICA_Type()
)
atmEndptOeRateUpICA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptOeRateUpICA.setStatus("mandatory")


class _AtmEndptFRTT_Type(Integer32):
    """Custom type atmEndptFRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16700),
    )


_AtmEndptFRTT_Type.__name__ = "Integer32"
_AtmEndptFRTT_Object = MibTableColumn
atmEndptFRTT = _AtmEndptFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 72),
    _AtmEndptFRTT_Type()
)
atmEndptFRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptFRTT.setStatus("mandatory")


class _AtmEndptTBE_Type(Integer32):
    """Custom type atmEndptTBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048320),
    )


_AtmEndptTBE_Type.__name__ = "Integer32"
_AtmEndptTBE_Object = MibTableColumn
atmEndptTBE = _AtmEndptTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 73),
    _AtmEndptTBE_Type()
)
atmEndptTBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptTBE.setStatus("mandatory")


class _AtmEndptVSVD_Type(Integer32):
    """Custom type atmEndptVSVD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmEndptVSVD_Type.__name__ = "Integer32"
_AtmEndptVSVD_Object = MibTableColumn
atmEndptVSVD = _AtmEndptVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 74),
    _AtmEndptVSVD_Type()
)
atmEndptVSVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptVSVD.setStatus("mandatory")


class _AtmEndptPolicing_Type(Integer32):
    """Custom type atmEndptPolicing based on Integer32"""
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
        *(("none", 5),
          ("pcrplc", 4),
          ("vbr1", 1),
          ("vbr2", 2),
          ("vbr3", 3))
    )


_AtmEndptPolicing_Type.__name__ = "Integer32"
_AtmEndptPolicing_Object = MibTableColumn
atmEndptPolicing = _AtmEndptPolicing_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 75),
    _AtmEndptPolicing_Type()
)
atmEndptPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPolicing.setStatus("mandatory")


class _AtmEndptPCR_Type(Integer32):
    """Custom type atmEndptPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_AtmEndptPCR_Type.__name__ = "Integer32"
_AtmEndptPCR_Object = MibTableColumn
atmEndptPCR = _AtmEndptPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 8, 1, 76),
    _AtmEndptPCR_Type()
)
atmEndptPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndptPCR.setStatus("mandatory")
_AtmBwClassTable_Object = MibTable
atmBwClassTable = _AtmBwClassTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9)
)
if mibBuilder.loadTexts:
    atmBwClassTable.setStatus("mandatory")
_AtmBwClassEntry_Object = MibTableRow
atmBwClassEntry = _AtmBwClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1)
)
atmBwClassEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmBwClassIndex"),
)
if mibBuilder.loadTexts:
    atmBwClassEntry.setStatus("mandatory")


class _AtmBwClassIndex_Type(Integer32):
    """Custom type atmBwClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmBwClassIndex_Type.__name__ = "Integer32"
_AtmBwClassIndex_Object = MibTableColumn
atmBwClassIndex = _AtmBwClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 1),
    _AtmBwClassIndex_Type()
)
atmBwClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassIndex.setStatus("mandatory")


class _AtmBwClassMIR_Type(Integer32):
    """Custom type atmBwClassMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmBwClassMIR_Type.__name__ = "Integer32"
_AtmBwClassMIR_Object = MibTableColumn
atmBwClassMIR = _AtmBwClassMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 2),
    _AtmBwClassMIR_Type()
)
atmBwClassMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassMIR.setStatus("mandatory")


class _AtmBwClassCIR_Type(Integer32):
    """Custom type atmBwClassCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmBwClassCIR_Type.__name__ = "Integer32"
_AtmBwClassCIR_Object = MibTableColumn
atmBwClassCIR = _AtmBwClassCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 3),
    _AtmBwClassCIR_Type()
)
atmBwClassCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCIR.setStatus("mandatory")


class _AtmBwClassVcQSize_Type(Integer32):
    """Custom type atmBwClassVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmBwClassVcQSize_Type.__name__ = "Integer32"
_AtmBwClassVcQSize_Object = MibTableColumn
atmBwClassVcQSize = _AtmBwClassVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 4),
    _AtmBwClassVcQSize_Type()
)
atmBwClassVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassVcQSize.setStatus("mandatory")


class _AtmBwClassPIR_Type(Integer32):
    """Custom type atmBwClassPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 96000),
    )


_AtmBwClassPIR_Type.__name__ = "Integer32"
_AtmBwClassPIR_Object = MibTableColumn
atmBwClassPIR = _AtmBwClassPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 5),
    _AtmBwClassPIR_Type()
)
atmBwClassPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassPIR.setStatus("mandatory")


class _AtmBwClassEfciQSize_Type(Integer32):
    """Custom type atmBwClassEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassEfciQSize_Type.__name__ = "Integer32"
_AtmBwClassEfciQSize_Object = MibTableColumn
atmBwClassEfciQSize = _AtmBwClassEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 6),
    _AtmBwClassEfciQSize_Type()
)
atmBwClassEfciQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassEfciQSize.setStatus("mandatory")


class _AtmBwClassQIR_Type(Integer32):
    """Custom type atmBwClassQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmBwClassQIR_Type.__name__ = "Integer32"
_AtmBwClassQIR_Object = MibTableColumn
atmBwClassQIR = _AtmBwClassQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 7),
    _AtmBwClassQIR_Type()
)
atmBwClassQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassQIR.setStatus("mandatory")


class _AtmBwClassPercUtil_Type(Integer32):
    """Custom type atmBwClassPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassPercUtil_Type.__name__ = "Integer32"
_AtmBwClassPercUtil_Object = MibTableColumn
atmBwClassPercUtil = _AtmBwClassPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 8),
    _AtmBwClassPercUtil_Type()
)
atmBwClassPercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassPercUtil.setStatus("mandatory")


class _AtmBwClassCBS_Type(Integer32):
    """Custom type atmBwClassCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmBwClassCBS_Type.__name__ = "Integer32"
_AtmBwClassCBS_Object = MibTableColumn
atmBwClassCBS = _AtmBwClassCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 9),
    _AtmBwClassCBS_Type()
)
atmBwClassCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCBS.setStatus("mandatory")


class _AtmBwClassIBS_Type(Integer32):
    """Custom type atmBwClassIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmBwClassIBS_Type.__name__ = "Integer32"
_AtmBwClassIBS_Object = MibTableColumn
atmBwClassIBS = _AtmBwClassIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 10),
    _AtmBwClassIBS_Type()
)
atmBwClassIBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassIBS.setStatus("mandatory")


class _AtmBwClassMFS_Type(Integer32):
    """Custom type atmBwClassMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmBwClassMFS_Type.__name__ = "Integer32"
_AtmBwClassMFS_Object = MibTableColumn
atmBwClassMFS = _AtmBwClassMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 11),
    _AtmBwClassMFS_Type()
)
atmBwClassMFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassMFS.setStatus("mandatory")


class _AtmBwClassCCDV_Type(Integer32):
    """Custom type atmBwClassCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmBwClassCCDV_Type.__name__ = "Integer32"
_AtmBwClassCCDV_Object = MibTableColumn
atmBwClassCCDV = _AtmBwClassCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 12),
    _AtmBwClassCCDV_Type()
)
atmBwClassCCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCCDV.setStatus("mandatory")


class _AtmBwClassHiCLP_Type(Integer32):
    """Custom type atmBwClassHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassHiCLP_Type.__name__ = "Integer32"
_AtmBwClassHiCLP_Object = MibTableColumn
atmBwClassHiCLP = _AtmBwClassHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 13),
    _AtmBwClassHiCLP_Type()
)
atmBwClassHiCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassHiCLP.setStatus("mandatory")


class _AtmBwClassLoCLP_Type(Integer32):
    """Custom type atmBwClassLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassLoCLP_Type.__name__ = "Integer32"
_AtmBwClassLoCLP_Object = MibTableColumn
atmBwClassLoCLP = _AtmBwClassLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 14),
    _AtmBwClassLoCLP_Type()
)
atmBwClassLoCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassLoCLP.setStatus("mandatory")


class _AtmBwClassOeMIR_Type(Integer32):
    """Custom type atmBwClassOeMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_AtmBwClassOeMIR_Type.__name__ = "Integer32"
_AtmBwClassOeMIR_Object = MibTableColumn
atmBwClassOeMIR = _AtmBwClassOeMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 15),
    _AtmBwClassOeMIR_Type()
)
atmBwClassOeMIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeMIR.setStatus("mandatory")


class _AtmBwClassOeCIR_Type(Integer32):
    """Custom type atmBwClassOeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmBwClassOeCIR_Type.__name__ = "Integer32"
_AtmBwClassOeCIR_Object = MibTableColumn
atmBwClassOeCIR = _AtmBwClassOeCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 16),
    _AtmBwClassOeCIR_Type()
)
atmBwClassOeCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCIR.setStatus("mandatory")


class _AtmBwClassOeVcQSize_Type(Integer32):
    """Custom type atmBwClassOeVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmBwClassOeVcQSize_Type.__name__ = "Integer32"
_AtmBwClassOeVcQSize_Object = MibTableColumn
atmBwClassOeVcQSize = _AtmBwClassOeVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 17),
    _AtmBwClassOeVcQSize_Type()
)
atmBwClassOeVcQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeVcQSize.setStatus("mandatory")


class _AtmBwClassOePIR_Type(Integer32):
    """Custom type atmBwClassOePIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 96000),
    )


_AtmBwClassOePIR_Type.__name__ = "Integer32"
_AtmBwClassOePIR_Object = MibTableColumn
atmBwClassOePIR = _AtmBwClassOePIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 18),
    _AtmBwClassOePIR_Type()
)
atmBwClassOePIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOePIR.setStatus("mandatory")


class _AtmBwClassOeEfciQSize_Type(Integer32):
    """Custom type atmBwClassOeEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeEfciQSize_Type.__name__ = "Integer32"
_AtmBwClassOeEfciQSize_Object = MibTableColumn
atmBwClassOeEfciQSize = _AtmBwClassOeEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 19),
    _AtmBwClassOeEfciQSize_Type()
)
atmBwClassOeEfciQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeEfciQSize.setStatus("mandatory")


class _AtmBwClassOeQIR_Type(Integer32):
    """Custom type atmBwClassOeQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000),
    )


_AtmBwClassOeQIR_Type.__name__ = "Integer32"
_AtmBwClassOeQIR_Object = MibTableColumn
atmBwClassOeQIR = _AtmBwClassOeQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 20),
    _AtmBwClassOeQIR_Type()
)
atmBwClassOeQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeQIR.setStatus("mandatory")


class _AtmBwClassOePercUtil_Type(Integer32):
    """Custom type atmBwClassOePercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOePercUtil_Type.__name__ = "Integer32"
_AtmBwClassOePercUtil_Object = MibTableColumn
atmBwClassOePercUtil = _AtmBwClassOePercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 21),
    _AtmBwClassOePercUtil_Type()
)
atmBwClassOePercUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOePercUtil.setStatus("mandatory")


class _AtmBwClassOeCBS_Type(Integer32):
    """Custom type atmBwClassOeCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_AtmBwClassOeCBS_Type.__name__ = "Integer32"
_AtmBwClassOeCBS_Object = MibTableColumn
atmBwClassOeCBS = _AtmBwClassOeCBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 22),
    _AtmBwClassOeCBS_Type()
)
atmBwClassOeCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCBS.setStatus("mandatory")


class _AtmBwClassOeIBS_Type(Integer32):
    """Custom type atmBwClassOeIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmBwClassOeIBS_Type.__name__ = "Integer32"
_AtmBwClassOeIBS_Object = MibTableColumn
atmBwClassOeIBS = _AtmBwClassOeIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 23),
    _AtmBwClassOeIBS_Type()
)
atmBwClassOeIBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeIBS.setStatus("mandatory")


class _AtmBwClassOeMFS_Type(Integer32):
    """Custom type atmBwClassOeMFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AtmBwClassOeMFS_Type.__name__ = "Integer32"
_AtmBwClassOeMFS_Object = MibTableColumn
atmBwClassOeMFS = _AtmBwClassOeMFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 24),
    _AtmBwClassOeMFS_Type()
)
atmBwClassOeMFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeMFS.setStatus("mandatory")


class _AtmBwClassOeCCDV_Type(Integer32):
    """Custom type atmBwClassOeCCDV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_AtmBwClassOeCCDV_Type.__name__ = "Integer32"
_AtmBwClassOeCCDV_Object = MibTableColumn
atmBwClassOeCCDV = _AtmBwClassOeCCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 25),
    _AtmBwClassOeCCDV_Type()
)
atmBwClassOeCCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCCDV.setStatus("mandatory")


class _AtmBwClassOeHiCLP_Type(Integer32):
    """Custom type atmBwClassOeHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeHiCLP_Type.__name__ = "Integer32"
_AtmBwClassOeHiCLP_Object = MibTableColumn
atmBwClassOeHiCLP = _AtmBwClassOeHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 26),
    _AtmBwClassOeHiCLP_Type()
)
atmBwClassOeHiCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeHiCLP.setStatus("mandatory")


class _AtmBwClassOeLoCLP_Type(Integer32):
    """Custom type atmBwClassOeLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassOeLoCLP_Type.__name__ = "Integer32"
_AtmBwClassOeLoCLP_Object = MibTableColumn
atmBwClassOeLoCLP = _AtmBwClassOeLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 27),
    _AtmBwClassOeLoCLP_Type()
)
atmBwClassOeLoCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeLoCLP.setStatus("mandatory")


class _AtmBwClassCLPTagging_Type(Integer32):
    """Custom type atmBwClassCLPTagging based on Integer32"""
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


_AtmBwClassCLPTagging_Type.__name__ = "Integer32"
_AtmBwClassCLPTagging_Object = MibTableColumn
atmBwClassCLPTagging = _AtmBwClassCLPTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 28),
    _AtmBwClassCLPTagging_Type()
)
atmBwClassCLPTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCLPTagging.setStatus("mandatory")


class _AtmBwClassUPC_Type(Integer32):
    """Custom type atmBwClassUPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassUPC_Type.__name__ = "Integer32"
_AtmBwClassUPC_Object = MibTableColumn
atmBwClassUPC = _AtmBwClassUPC_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 29),
    _AtmBwClassUPC_Type()
)
atmBwClassUPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassUPC.setStatus("mandatory")


class _AtmBwClassEnableFST_Type(Integer32):
    """Custom type atmBwClassEnableFST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassEnableFST_Type.__name__ = "Integer32"
_AtmBwClassEnableFST_Object = MibTableColumn
atmBwClassEnableFST = _AtmBwClassEnableFST_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 30),
    _AtmBwClassEnableFST_Type()
)
atmBwClassEnableFST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassEnableFST.setStatus("mandatory")


class _AtmBwClassRateUpICA_Type(Integer32):
    """Custom type atmBwClassRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmBwClassRateUpICA_Type.__name__ = "Integer32"
_AtmBwClassRateUpICA_Object = MibTableColumn
atmBwClassRateUpICA = _AtmBwClassRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 31),
    _AtmBwClassRateUpICA_Type()
)
atmBwClassRateUpICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassRateUpICA.setStatus("mandatory")


class _AtmBwClassRateDnICA_Type(Integer32):
    """Custom type atmBwClassRateDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassRateDnICA_Type.__name__ = "Integer32"
_AtmBwClassRateDnICA_Object = MibTableColumn
atmBwClassRateDnICA = _AtmBwClassRateDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 32),
    _AtmBwClassRateDnICA_Type()
)
atmBwClassRateDnICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassRateDnICA.setStatus("mandatory")


class _AtmBwClassFastDnICA_Type(Integer32):
    """Custom type atmBwClassFastDnICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmBwClassFastDnICA_Type.__name__ = "Integer32"
_AtmBwClassFastDnICA_Object = MibTableColumn
atmBwClassFastDnICA = _AtmBwClassFastDnICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 33),
    _AtmBwClassFastDnICA_Type()
)
atmBwClassFastDnICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassFastDnICA.setStatus("mandatory")


class _AtmBwClassToQIR_Type(Integer32):
    """Custom type atmBwClassToQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmBwClassToQIR_Type.__name__ = "Integer32"
_AtmBwClassToQIR_Object = MibTableColumn
atmBwClassToQIR = _AtmBwClassToQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 34),
    _AtmBwClassToQIR_Type()
)
atmBwClassToQIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassToQIR.setStatus("mandatory")


class _AtmBwClassMinAdjustICA_Type(Integer32):
    """Custom type atmBwClassMinAdjustICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 250),
    )


_AtmBwClassMinAdjustICA_Type.__name__ = "Integer32"
_AtmBwClassMinAdjustICA_Object = MibTableColumn
atmBwClassMinAdjustICA = _AtmBwClassMinAdjustICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 35),
    _AtmBwClassMinAdjustICA_Type()
)
atmBwClassMinAdjustICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassMinAdjustICA.setStatus("mandatory")


class _AtmBwClassDescription_Type(DisplayString):
    """Custom type atmBwClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AtmBwClassDescription_Type.__name__ = "DisplayString"
_AtmBwClassDescription_Object = MibTableColumn
atmBwClassDescription = _AtmBwClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 36),
    _AtmBwClassDescription_Type()
)
atmBwClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassDescription.setStatus("mandatory")


class _AtmBwClassBCM_Type(Integer32):
    """Custom type atmBwClassBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassBCM_Type.__name__ = "Integer32"
_AtmBwClassBCM_Object = MibTableColumn
atmBwClassBCM = _AtmBwClassBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 37),
    _AtmBwClassBCM_Type()
)
atmBwClassBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassBCM.setStatus("mandatory")


class _AtmBwClassFGCRA_Type(Integer32):
    """Custom type atmBwClassFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassFGCRA_Type.__name__ = "Integer32"
_AtmBwClassFGCRA_Object = MibTableColumn
atmBwClassFGCRA = _AtmBwClassFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 38),
    _AtmBwClassFGCRA_Type()
)
atmBwClassFGCRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassFGCRA.setStatus("mandatory")


class _AtmBwClassOeBCM_Type(Integer32):
    """Custom type atmBwClassOeBCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassOeBCM_Type.__name__ = "Integer32"
_AtmBwClassOeBCM_Object = MibTableColumn
atmBwClassOeBCM = _AtmBwClassOeBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 39),
    _AtmBwClassOeBCM_Type()
)
atmBwClassOeBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeBCM.setStatus("mandatory")


class _AtmBwClassOeFGCRA_Type(Integer32):
    """Custom type atmBwClassOeFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AtmBwClassOeFGCRA_Type.__name__ = "Integer32"
_AtmBwClassOeFGCRA_Object = MibTableColumn
atmBwClassOeFGCRA = _AtmBwClassOeFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 40),
    _AtmBwClassOeFGCRA_Type()
)
atmBwClassOeFGCRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeFGCRA.setStatus("mandatory")


class _AtmBwClassConType_Type(Integer32):
    """Custom type atmBwClassConType based on Integer32"""
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
        *(("abr", 5),
          ("atf", 1),
          ("cbr", 3),
          ("unknown", 4),
          ("vbr", 2))
    )


_AtmBwClassConType_Type.__name__ = "Integer32"
_AtmBwClassConType_Object = MibTableColumn
atmBwClassConType = _AtmBwClassConType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 41),
    _AtmBwClassConType_Type()
)
atmBwClassConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassConType.setStatus("mandatory")


class _AtmBwClassScrPlc_Type(Integer32):
    """Custom type atmBwClassScrPlc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp0and1", 2),
          ("off", 3))
    )


_AtmBwClassScrPlc_Type.__name__ = "Integer32"
_AtmBwClassScrPlc_Object = MibTableColumn
atmBwClassScrPlc = _AtmBwClassScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 42),
    _AtmBwClassScrPlc_Type()
)
atmBwClassScrPlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassScrPlc.setStatus("mandatory")


class _AtmBwClassOeScrPlc_Type(Integer32):
    """Custom type atmBwClassOeScrPlc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp0and1", 2),
          ("off", 3))
    )


_AtmBwClassOeScrPlc_Type.__name__ = "Integer32"
_AtmBwClassOeScrPlc_Object = MibTableColumn
atmBwClassOeScrPlc = _AtmBwClassOeScrPlc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 43),
    _AtmBwClassOeScrPlc_Type()
)
atmBwClassOeScrPlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeScrPlc.setStatus("mandatory")


class _AtmBwClassPCR0_Type(Integer32):
    """Custom type atmBwClassPCR0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmBwClassPCR0_Type.__name__ = "Integer32"
_AtmBwClassPCR0_Object = MibTableColumn
atmBwClassPCR0 = _AtmBwClassPCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 44),
    _AtmBwClassPCR0_Type()
)
atmBwClassPCR0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassPCR0.setStatus("mandatory")


class _AtmBwClassOePCR0_Type(Integer32):
    """Custom type atmBwClassOePCR0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 353208),
    )


_AtmBwClassOePCR0_Type.__name__ = "Integer32"
_AtmBwClassOePCR0_Object = MibTableColumn
atmBwClassOePCR0 = _AtmBwClassOePCR0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 45),
    _AtmBwClassOePCR0_Type()
)
atmBwClassOePCR0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOePCR0.setStatus("mandatory")


class _AtmBwClassCDVT0_Type(Integer32):
    """Custom type atmBwClassCDVT0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250000),
    )


_AtmBwClassCDVT0_Type.__name__ = "Integer32"
_AtmBwClassCDVT0_Object = MibTableColumn
atmBwClassCDVT0 = _AtmBwClassCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 46),
    _AtmBwClassCDVT0_Type()
)
atmBwClassCDVT0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassCDVT0.setStatus("mandatory")


class _AtmBwClassOeCDVT0_Type(Integer32):
    """Custom type atmBwClassOeCDVT0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250000),
    )


_AtmBwClassOeCDVT0_Type.__name__ = "Integer32"
_AtmBwClassOeCDVT0_Object = MibTableColumn
atmBwClassOeCDVT0 = _AtmBwClassOeCDVT0_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 47),
    _AtmBwClassOeCDVT0_Type()
)
atmBwClassOeCDVT0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeCDVT0.setStatus("mandatory")


class _AtmBwClassOeRateUpICA_Type(Integer32):
    """Custom type atmBwClassOeRateUpICA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_AtmBwClassOeRateUpICA_Type.__name__ = "Integer32"
_AtmBwClassOeRateUpICA_Object = MibTableColumn
atmBwClassOeRateUpICA = _AtmBwClassOeRateUpICA_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 9, 1, 48),
    _AtmBwClassOeRateUpICA_Type()
)
atmBwClassOeRateUpICA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBwClassOeRateUpICA.setStatus("mandatory")
_FrEndptMapTable_Object = MibTable
frEndptMapTable = _FrEndptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10)
)
if mibBuilder.loadTexts:
    frEndptMapTable.setStatus("mandatory")
_FrEndptMapEntry_Object = MibTableRow
frEndptMapEntry = _FrEndptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1)
)
frEndptMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "frEndptMapSlot"),
    (0, "STRATACOM-MIB", "frEndptMapPort"),
    (0, "STRATACOM-MIB", "frEndptMapDlci"),
)
if mibBuilder.loadTexts:
    frEndptMapEntry.setStatus("mandatory")


class _FrEndptMapSlot_Type(Integer32):
    """Custom type frEndptMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrEndptMapSlot_Type.__name__ = "Integer32"
_FrEndptMapSlot_Object = MibTableColumn
frEndptMapSlot = _FrEndptMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 1),
    _FrEndptMapSlot_Type()
)
frEndptMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapSlot.setStatus("mandatory")


class _FrEndptMapPort_Type(Integer32):
    """Custom type frEndptMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FrEndptMapPort_Type.__name__ = "Integer32"
_FrEndptMapPort_Object = MibTableColumn
frEndptMapPort = _FrEndptMapPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 2),
    _FrEndptMapPort_Type()
)
frEndptMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapPort.setStatus("mandatory")
_FrEndptMapDlci_Type = Integer32
_FrEndptMapDlci_Object = MibTableColumn
frEndptMapDlci = _FrEndptMapDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 3),
    _FrEndptMapDlci_Type()
)
frEndptMapDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapDlci.setStatus("mandatory")
_FrEndptMapEndptPtr_Type = ObjectIdentifier
_FrEndptMapEndptPtr_Object = MibTableColumn
frEndptMapEndptPtr = _FrEndptMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 4),
    _FrEndptMapEndptPtr_Type()
)
frEndptMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapEndptPtr.setStatus("mandatory")
_FrEndptMapConnPtr_Type = ObjectIdentifier
_FrEndptMapConnPtr_Object = MibTableColumn
frEndptMapConnPtr = _FrEndptMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 10, 1, 5),
    _FrEndptMapConnPtr_Type()
)
frEndptMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndptMapConnPtr.setStatus("mandatory")
_AtmEndptMapTable_Object = MibTable
atmEndptMapTable = _AtmEndptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11)
)
if mibBuilder.loadTexts:
    atmEndptMapTable.setStatus("mandatory")
_AtmEndptMapEntry_Object = MibTableRow
atmEndptMapEntry = _AtmEndptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1)
)
atmEndptMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptMapSlot"),
    (0, "STRATACOM-MIB", "atmEndptMapPort"),
    (0, "STRATACOM-MIB", "atmEndptMapVpi"),
    (0, "STRATACOM-MIB", "atmEndptMapVci"),
)
if mibBuilder.loadTexts:
    atmEndptMapEntry.setStatus("mandatory")


class _AtmEndptMapSlot_Type(Integer32):
    """Custom type atmEndptMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmEndptMapSlot_Type.__name__ = "Integer32"
_AtmEndptMapSlot_Object = MibTableColumn
atmEndptMapSlot = _AtmEndptMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 1),
    _AtmEndptMapSlot_Type()
)
atmEndptMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapSlot.setStatus("mandatory")


class _AtmEndptMapPort_Type(Integer32):
    """Custom type atmEndptMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmEndptMapPort_Type.__name__ = "Integer32"
_AtmEndptMapPort_Object = MibTableColumn
atmEndptMapPort = _AtmEndptMapPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 2),
    _AtmEndptMapPort_Type()
)
atmEndptMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapPort.setStatus("mandatory")
_AtmEndptMapVpi_Type = Integer32
_AtmEndptMapVpi_Object = MibTableColumn
atmEndptMapVpi = _AtmEndptMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 3),
    _AtmEndptMapVpi_Type()
)
atmEndptMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapVpi.setStatus("mandatory")
_AtmEndptMapVci_Type = Integer32
_AtmEndptMapVci_Object = MibTableColumn
atmEndptMapVci = _AtmEndptMapVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 4),
    _AtmEndptMapVci_Type()
)
atmEndptMapVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapVci.setStatus("mandatory")
_AtmEndptMapEndptPtr_Type = ObjectIdentifier
_AtmEndptMapEndptPtr_Object = MibTableColumn
atmEndptMapEndptPtr = _AtmEndptMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 5),
    _AtmEndptMapEndptPtr_Type()
)
atmEndptMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapEndptPtr.setStatus("mandatory")
_AtmEndptMapConnPtr_Type = ObjectIdentifier
_AtmEndptMapConnPtr_Object = MibTableColumn
atmEndptMapConnPtr = _AtmEndptMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 11, 1, 6),
    _AtmEndptMapConnPtr_Type()
)
atmEndptMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndptMapConnPtr.setStatus("mandatory")
_AtmEndptStatTable_Object = MibTable
atmEndptStatTable = _AtmEndptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12)
)
if mibBuilder.loadTexts:
    atmEndptStatTable.setStatus("mandatory")
_AtmEndptStatEntry_Object = MibTableRow
atmEndptStatEntry = _AtmEndptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1)
)
atmEndptStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "atmEndptIndex"),
)
if mibBuilder.loadTexts:
    atmEndptStatEntry.setStatus("mandatory")
_AtmCellsRxPorts_Type = Counter32
_AtmCellsRxPorts_Object = MibTableColumn
atmCellsRxPorts = _AtmCellsRxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 1),
    _AtmCellsRxPorts_Type()
)
atmCellsRxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsRxPorts.setStatus("mandatory")
_AtmFramesRxPorts_Type = Counter32
_AtmFramesRxPorts_Object = MibTableColumn
atmFramesRxPorts = _AtmFramesRxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 2),
    _AtmFramesRxPorts_Type()
)
atmFramesRxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFramesRxPorts.setStatus("mandatory")
_AtmCellsTxNets_Type = Counter32
_AtmCellsTxNets_Object = MibTableColumn
atmCellsTxNets = _AtmCellsTxNets_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 3),
    _AtmCellsTxNets_Type()
)
atmCellsTxNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsTxNets.setStatus("mandatory")
_AtmClpRxs_Type = Counter32
_AtmClpRxs_Object = MibTableColumn
atmClpRxs = _AtmClpRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 4),
    _AtmClpRxs_Type()
)
atmClpRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmClpRxs.setStatus("mandatory")
_AtmViolRxs_Type = Counter32
_AtmViolRxs_Object = MibTableColumn
atmViolRxs = _AtmViolRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 5),
    _AtmViolRxs_Type()
)
atmViolRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmViolRxs.setStatus("mandatory")
_AtmDiscardVcqClpThs_Type = Counter32
_AtmDiscardVcqClpThs_Object = MibTableColumn
atmDiscardVcqClpThs = _AtmDiscardVcqClpThs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 6),
    _AtmDiscardVcqClpThs_Type()
)
atmDiscardVcqClpThs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardVcqClpThs.setStatus("mandatory")
_AtmDiscardVcqFulls_Type = Counter32
_AtmDiscardVcqFulls_Object = MibTableColumn
atmDiscardVcqFulls = _AtmDiscardVcqFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 7),
    _AtmDiscardVcqFulls_Type()
)
atmDiscardVcqFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardVcqFulls.setStatus("mandatory")
_AtmEfciRxs_Type = Counter32
_AtmEfciRxs_Object = MibTableColumn
atmEfciRxs = _AtmEfciRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 8),
    _AtmEfciRxs_Type()
)
atmEfciRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEfciRxs.setStatus("mandatory")
_AtmNonCompRxs_Type = Counter32
_AtmNonCompRxs_Object = MibTableColumn
atmNonCompRxs = _AtmNonCompRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 9),
    _AtmNonCompRxs_Type()
)
atmNonCompRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmNonCompRxs.setStatus("mandatory")
_AtmDiscardFails_Type = Counter32
_AtmDiscardFails_Object = MibTableColumn
atmDiscardFails = _AtmDiscardFails_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 10),
    _AtmDiscardFails_Type()
)
atmDiscardFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardFails.setStatus("mandatory")
_AtmAvgVcqDepths_Type = Counter32
_AtmAvgVcqDepths_Object = MibTableColumn
atmAvgVcqDepths = _AtmAvgVcqDepths_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 11),
    _AtmAvgVcqDepths_Type()
)
atmAvgVcqDepths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAvgVcqDepths.setStatus("mandatory")
_AtmDiscardRsrcOflows_Type = Counter32
_AtmDiscardRsrcOflows_Object = MibTableColumn
atmDiscardRsrcOflows = _AtmDiscardRsrcOflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 12),
    _AtmDiscardRsrcOflows_Type()
)
atmDiscardRsrcOflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardRsrcOflows.setStatus("mandatory")
_AtmDiscardSbinFulls_Type = Counter32
_AtmDiscardSbinFulls_Object = MibTableColumn
atmDiscardSbinFulls = _AtmDiscardSbinFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 13),
    _AtmDiscardSbinFulls_Type()
)
atmDiscardSbinFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardSbinFulls.setStatus("mandatory")
_AtmBcmRxs_Type = Counter32
_AtmBcmRxs_Object = MibTableColumn
atmBcmRxs = _AtmBcmRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 14),
    _AtmBcmRxs_Type()
)
atmBcmRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBcmRxs.setStatus("mandatory")
_AtmBcmTxs_Type = Counter32
_AtmBcmTxs_Object = MibTableColumn
atmBcmTxs = _AtmBcmTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 15),
    _AtmBcmTxs_Type()
)
atmBcmTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmBcmTxs.setStatus("mandatory")
_AtmOamTxs_Type = Counter32
_AtmOamTxs_Object = MibTableColumn
atmOamTxs = _AtmOamTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 16),
    _AtmOamTxs_Type()
)
atmOamTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamTxs.setStatus("mandatory")
_AtmDiscardQbinFulls_Type = Counter32
_AtmDiscardQbinFulls_Object = MibTableColumn
atmDiscardQbinFulls = _AtmDiscardQbinFulls_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 17),
    _AtmDiscardQbinFulls_Type()
)
atmDiscardQbinFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardQbinFulls.setStatus("mandatory")
_AtmDiscardQbinClpThs_Type = Counter32
_AtmDiscardQbinClpThs_Object = MibTableColumn
atmDiscardQbinClpThs = _AtmDiscardQbinClpThs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 18),
    _AtmDiscardQbinClpThs_Type()
)
atmDiscardQbinClpThs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDiscardQbinClpThs.setStatus("mandatory")
_AtmCellsRxNets_Type = Counter32
_AtmCellsRxNets_Object = MibTableColumn
atmCellsRxNets = _AtmCellsRxNets_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 19),
    _AtmCellsRxNets_Type()
)
atmCellsRxNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsRxNets.setStatus("mandatory")
_AtmClpTxs_Type = Counter32
_AtmClpTxs_Object = MibTableColumn
atmClpTxs = _AtmClpTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 20),
    _AtmClpTxs_Type()
)
atmClpTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmClpTxs.setStatus("mandatory")
_AtmEfciTxs_Type = Counter32
_AtmEfciTxs_Object = MibTableColumn
atmEfciTxs = _AtmEfciTxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 21),
    _AtmEfciTxs_Type()
)
atmEfciTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEfciTxs.setStatus("mandatory")
_AtmCellsTxPorts_Type = Counter32
_AtmCellsTxPorts_Object = MibTableColumn
atmCellsTxPorts = _AtmCellsTxPorts_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 22),
    _AtmCellsTxPorts_Type()
)
atmCellsTxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCellsTxPorts.setStatus("mandatory")
_AtmAisRxs_Type = Counter32
_AtmAisRxs_Object = MibTableColumn
atmAisRxs = _AtmAisRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 23),
    _AtmAisRxs_Type()
)
atmAisRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAisRxs.setStatus("mandatory")
_AtmFerfRxs_Type = Counter32
_AtmFerfRxs_Object = MibTableColumn
atmFerfRxs = _AtmFerfRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 12, 1, 24),
    _AtmFerfRxs_Type()
)
atmFerfRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFerfRxs.setStatus("mandatory")
_VoiceEndptTable_Object = MibTable
voiceEndptTable = _VoiceEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13)
)
if mibBuilder.loadTexts:
    voiceEndptTable.setStatus("mandatory")
_VoiceEndptEntry_Object = MibTableRow
voiceEndptEntry = _VoiceEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1)
)
voiceEndptEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceEndptIndex"),
)
if mibBuilder.loadTexts:
    voiceEndptEntry.setStatus("mandatory")


class _VoiceEndptIndex_Type(Integer32):
    """Custom type voiceEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_VoiceEndptIndex_Type.__name__ = "Integer32"
_VoiceEndptIndex_Object = MibTableColumn
voiceEndptIndex = _VoiceEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 1),
    _VoiceEndptIndex_Type()
)
voiceEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptIndex.setStatus("mandatory")


class _VoiceOtherEndptIndex_Type(Integer32):
    """Custom type voiceOtherEndptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_VoiceOtherEndptIndex_Type.__name__ = "Integer32"
_VoiceOtherEndptIndex_Object = MibTableColumn
voiceOtherEndptIndex = _VoiceOtherEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 2),
    _VoiceOtherEndptIndex_Type()
)
voiceOtherEndptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceOtherEndptIndex.setStatus("mandatory")
_VoiceEndptDesc_Type = DisplayString
_VoiceEndptDesc_Object = MibTableColumn
voiceEndptDesc = _VoiceEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 3),
    _VoiceEndptDesc_Type()
)
voiceEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptDesc.setStatus("mandatory")
_VoiceOtherEndptDesc_Type = DisplayString
_VoiceOtherEndptDesc_Object = MibTableColumn
voiceOtherEndptDesc = _VoiceOtherEndptDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 4),
    _VoiceOtherEndptDesc_Type()
)
voiceOtherEndptDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceOtherEndptDesc.setStatus("mandatory")


class _VoiceEndptConnDesc_Type(DisplayString):
    """Custom type voiceEndptConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VoiceEndptConnDesc_Type.__name__ = "DisplayString"
_VoiceEndptConnDesc_Object = MibTableColumn
voiceEndptConnDesc = _VoiceEndptConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 5),
    _VoiceEndptConnDesc_Type()
)
voiceEndptConnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptConnDesc.setStatus("mandatory")


class _VoiceEndptAdminStatus_Type(Integer32):
    """Custom type voiceEndptAdminStatus based on Integer32"""
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3),
          ("test", 4),
          ("writeOnly", 5))
    )


_VoiceEndptAdminStatus_Type.__name__ = "Integer32"
_VoiceEndptAdminStatus_Object = MibTableColumn
voiceEndptAdminStatus = _VoiceEndptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 6),
    _VoiceEndptAdminStatus_Type()
)
voiceEndptAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptAdminStatus.setStatus("mandatory")


class _VoiceEndptOperStatus_Type(Integer32):
    """Custom type voiceEndptOperStatus based on Integer32"""
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
        *(("down", 3),
          ("failed", 4),
          ("inTest", 5),
          ("looped", 8),
          ("ok", 1),
          ("okPendingDelete", 7),
          ("okPendingDown", 2),
          ("okPendingRoute", 6),
          ("unknown", 9))
    )


_VoiceEndptOperStatus_Type.__name__ = "Integer32"
_VoiceEndptOperStatus_Object = MibTableColumn
voiceEndptOperStatus = _VoiceEndptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 7),
    _VoiceEndptOperStatus_Type()
)
voiceEndptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptOperStatus.setStatus("mandatory")


class _VoiceEndptRateType_Type(Integer32):
    """Custom type voiceEndptRateType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("a16", 3),
          ("a16z", 4),
          ("a24", 2),
          ("a32", 1),
          ("a32d", 5),
          ("c16", 8),
          ("c16z", 9),
          ("c24", 7),
          ("c32", 6),
          ("c32d", 10),
          ("p", 11),
          ("t", 12),
          ("v", 13))
    )


_VoiceEndptRateType_Type.__name__ = "Integer32"
_VoiceEndptRateType_Object = MibTableColumn
voiceEndptRateType = _VoiceEndptRateType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 8),
    _VoiceEndptRateType_Type()
)
voiceEndptRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptRateType.setStatus("mandatory")


class _VoiceEndPointFailure_Type(Integer32):
    """Custom type voiceEndPointFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndPointFailure_Type.__name__ = "Integer32"
_VoiceEndPointFailure_Object = MibTableColumn
voiceEndPointFailure = _VoiceEndPointFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 9),
    _VoiceEndPointFailure_Type()
)
voiceEndPointFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointFailure.setStatus("mandatory")


class _VoiceNoRouteFoundFailure_Type(Integer32):
    """Custom type voiceNoRouteFoundFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceNoRouteFoundFailure_Type.__name__ = "Integer32"
_VoiceNoRouteFoundFailure_Object = MibTableColumn
voiceNoRouteFoundFailure = _VoiceNoRouteFoundFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 10),
    _VoiceNoRouteFoundFailure_Type()
)
voiceNoRouteFoundFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceNoRouteFoundFailure.setStatus("mandatory")


class _VoiceBumpFailure_Type(Integer32):
    """Custom type voiceBumpFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceBumpFailure_Type.__name__ = "Integer32"
_VoiceBumpFailure_Object = MibTableColumn
voiceBumpFailure = _VoiceBumpFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 11),
    _VoiceBumpFailure_Type()
)
voiceBumpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceBumpFailure.setStatus("mandatory")


class _VoiceTestFailure_Type(Integer32):
    """Custom type voiceTestFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceTestFailure_Type.__name__ = "Integer32"
_VoiceTestFailure_Object = MibTableColumn
voiceTestFailure = _VoiceTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 12),
    _VoiceTestFailure_Type()
)
voiceTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceTestFailure.setStatus("mandatory")


class _VoiceEndptTestType_Type(Integer32):
    """Custom type voiceEndptTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testCon", 1),
          ("writeOnly", 2))
    )


_VoiceEndptTestType_Type.__name__ = "Integer32"
_VoiceEndptTestType_Object = MibTableColumn
voiceEndptTestType = _VoiceEndptTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 13),
    _VoiceEndptTestType_Type()
)
voiceEndptTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptTestType.setStatus("mandatory")
_VoiceEndptLpbkStatus_Type = Integer32
_VoiceEndptLpbkStatus_Object = MibTableColumn
voiceEndptLpbkStatus = _VoiceEndptLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 14),
    _VoiceEndptLpbkStatus_Type()
)
voiceEndptLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptLpbkStatus.setStatus("mandatory")
_VoiceConnPtr_Type = ObjectIdentifier
_VoiceConnPtr_Object = MibTableColumn
voiceConnPtr = _VoiceConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 15),
    _VoiceConnPtr_Type()
)
voiceConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceConnPtr.setStatus("mandatory")
_VoiceChannelPtr_Type = ObjectIdentifier
_VoiceChannelPtr_Object = MibTableColumn
voiceChannelPtr = _VoiceChannelPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 16),
    _VoiceChannelPtr_Type()
)
voiceChannelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelPtr.setStatus("mandatory")


class _VoiceEndptTrkAvoidType_Type(Integer32):
    """Custom type voiceEndptTrkAvoidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_VoiceEndptTrkAvoidType_Type.__name__ = "Integer32"
_VoiceEndptTrkAvoidType_Object = MibTableColumn
voiceEndptTrkAvoidType = _VoiceEndptTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 17),
    _VoiceEndptTrkAvoidType_Type()
)
voiceEndptTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptTrkAvoidType.setStatus("mandatory")


class _VoiceEndptAvoidZCS_Type(Integer32):
    """Custom type voiceEndptAvoidZCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndptAvoidZCS_Type.__name__ = "Integer32"
_VoiceEndptAvoidZCS_Object = MibTableColumn
voiceEndptAvoidZCS = _VoiceEndptAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 18),
    _VoiceEndptAvoidZCS_Type()
)
voiceEndptAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptAvoidZCS.setStatus("mandatory")


class _VoiceEndptState_Type(Integer32):
    """Custom type voiceEndptState based on Integer32"""
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
        *(("fastmodem", 4),
          ("notConnected", 5),
          ("offhook", 1),
          ("onhook", 2),
          ("slowmodem", 3))
    )


_VoiceEndptState_Type.__name__ = "Integer32"
_VoiceEndptState_Object = MibTableColumn
voiceEndptState = _VoiceEndptState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 19),
    _VoiceEndptState_Type()
)
voiceEndptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptState.setStatus("mandatory")


class _VoiceEndptAdv_Type(Integer32):
    """Custom type voiceEndptAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceEndptAdv_Type.__name__ = "Integer32"
_VoiceEndptAdv_Object = MibTableColumn
voiceEndptAdv = _VoiceEndptAdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 20),
    _VoiceEndptAdv_Type()
)
voiceEndptAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptAdv.setStatus("mandatory")


class _VoiceOtherEndptAdv_Type(Integer32):
    """Custom type voiceOtherEndptAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VoiceOtherEndptAdv_Type.__name__ = "Integer32"
_VoiceOtherEndptAdv_Object = MibTableColumn
voiceOtherEndptAdv = _VoiceOtherEndptAdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 21),
    _VoiceOtherEndptAdv_Type()
)
voiceOtherEndptAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceOtherEndptAdv.setStatus("mandatory")


class _VoiceEndptEncoding_Type(Integer32):
    """Custom type voiceEndptEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_VoiceEndptEncoding_Type.__name__ = "Integer32"
_VoiceEndptEncoding_Object = MibTableColumn
voiceEndptEncoding = _VoiceEndptEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 22),
    _VoiceEndptEncoding_Type()
)
voiceEndptEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptEncoding.setStatus("mandatory")


class _VoiceOtherEndptEncoding_Type(Integer32):
    """Custom type voiceOtherEndptEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_VoiceOtherEndptEncoding_Type.__name__ = "Integer32"
_VoiceOtherEndptEncoding_Object = MibTableColumn
voiceOtherEndptEncoding = _VoiceOtherEndptEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 23),
    _VoiceOtherEndptEncoding_Type()
)
voiceOtherEndptEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceOtherEndptEncoding.setStatus("mandatory")


class _VoiceEndptEndptType_Type(Integer32):
    """Custom type voiceEndptEndptType based on Integer32"""
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
        *(("adpcm", 2),
          ("adpno", 3),
          ("pcm", 1),
          ("transp", 4),
          ("unknown", 5))
    )


_VoiceEndptEndptType_Type.__name__ = "Integer32"
_VoiceEndptEndptType_Object = MibTableColumn
voiceEndptEndptType = _VoiceEndptEndptType_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 24),
    _VoiceEndptEndptType_Type()
)
voiceEndptEndptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptEndptType.setStatus("mandatory")


class _VoiceEndptLocLpbkState_Type(Integer32):
    """Custom type voiceEndptLocLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("writeOnly", 3))
    )


_VoiceEndptLocLpbkState_Type.__name__ = "Integer32"
_VoiceEndptLocLpbkState_Object = MibTableColumn
voiceEndptLocLpbkState = _VoiceEndptLocLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 13, 1, 25),
    _VoiceEndptLocLpbkState_Type()
)
voiceEndptLocLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndptLocLpbkState.setStatus("mandatory")
_VoiceStatTable_Object = MibTable
voiceStatTable = _VoiceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14)
)
if mibBuilder.loadTexts:
    voiceStatTable.setStatus("mandatory")
_VoiceStatEntry_Object = MibTableRow
voiceStatEntry = _VoiceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1)
)
voiceStatEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceEndptIndex"),
)
if mibBuilder.loadTexts:
    voiceStatEntry.setStatus("mandatory")
_VoiceStatPktsRxs_Type = Counter32
_VoiceStatPktsRxs_Object = MibTableColumn
voiceStatPktsRxs = _VoiceStatPktsRxs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 1),
    _VoiceStatPktsRxs_Type()
)
voiceStatPktsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatPktsRxs.setStatus("mandatory")
_VoiceStatPktsXmits_Type = Counter32
_VoiceStatPktsXmits_Object = MibTableColumn
voiceStatPktsXmits = _VoiceStatPktsXmits_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 2),
    _VoiceStatPktsXmits_Type()
)
voiceStatPktsXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatPktsXmits.setStatus("mandatory")
_VoiceStatRxPktsDscds_Type = Counter32
_VoiceStatRxPktsDscds_Object = MibTableColumn
voiceStatRxPktsDscds = _VoiceStatRxPktsDscds_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 3),
    _VoiceStatRxPktsDscds_Type()
)
voiceStatRxPktsDscds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatRxPktsDscds.setStatus("mandatory")
_VoiceStatSprvPktsXmits_Type = Counter32
_VoiceStatSprvPktsXmits_Object = MibTableColumn
voiceStatSprvPktsXmits = _VoiceStatSprvPktsXmits_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 4),
    _VoiceStatSprvPktsXmits_Type()
)
voiceStatSprvPktsXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatSprvPktsXmits.setStatus("mandatory")
_VoiceStatSprvPktsRcvs_Type = Counter32
_VoiceStatSprvPktsRcvs_Object = MibTableColumn
voiceStatSprvPktsRcvs = _VoiceStatSprvPktsRcvs_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 5),
    _VoiceStatSprvPktsRcvs_Type()
)
voiceStatSprvPktsRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatSprvPktsRcvs.setStatus("mandatory")
_VoiceStatV25ModemOns_Type = Counter32
_VoiceStatV25ModemOns_Object = MibTableColumn
voiceStatV25ModemOns = _VoiceStatV25ModemOns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 6),
    _VoiceStatV25ModemOns_Type()
)
voiceStatV25ModemOns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatV25ModemOns.setStatus("mandatory")
_VoiceStatDsiOns_Type = Counter32
_VoiceStatDsiOns_Object = MibTableColumn
voiceStatDsiOns = _VoiceStatDsiOns_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 7),
    _VoiceStatDsiOns_Type()
)
voiceStatDsiOns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatDsiOns.setStatus("mandatory")
_VoiceStatOffhks_Type = Counter32
_VoiceStatOffhks_Object = MibTableColumn
voiceStatOffhks = _VoiceStatOffhks_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 8),
    _VoiceStatOffhks_Type()
)
voiceStatOffhks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatOffhks.setStatus("mandatory")
_VoiceStatInservices_Type = Counter32
_VoiceStatInservices_Object = MibTableColumn
voiceStatInservices = _VoiceStatInservices_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 14, 1, 9),
    _VoiceStatInservices_Type()
)
voiceStatInservices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceStatInservices.setStatus("mandatory")
_VoiceEndptMapTable_Object = MibTable
voiceEndptMapTable = _VoiceEndptMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15)
)
if mibBuilder.loadTexts:
    voiceEndptMapTable.setStatus("mandatory")
_VoiceEndptMapEntry_Object = MibTableRow
voiceEndptMapEntry = _VoiceEndptMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15, 1)
)
voiceEndptMapEntry.setIndexNames(
    (0, "STRATACOM-MIB", "voiceEndptMapSlot"),
    (0, "STRATACOM-MIB", "voiceEndptMapChannel"),
)
if mibBuilder.loadTexts:
    voiceEndptMapEntry.setStatus("mandatory")


class _VoiceEndptMapSlot_Type(Integer32):
    """Custom type voiceEndptMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoiceEndptMapSlot_Type.__name__ = "Integer32"
_VoiceEndptMapSlot_Object = MibTableColumn
voiceEndptMapSlot = _VoiceEndptMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15, 1, 1),
    _VoiceEndptMapSlot_Type()
)
voiceEndptMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptMapSlot.setStatus("mandatory")


class _VoiceEndptMapChannel_Type(Integer32):
    """Custom type voiceEndptMapChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VoiceEndptMapChannel_Type.__name__ = "Integer32"
_VoiceEndptMapChannel_Object = MibTableColumn
voiceEndptMapChannel = _VoiceEndptMapChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15, 1, 2),
    _VoiceEndptMapChannel_Type()
)
voiceEndptMapChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptMapChannel.setStatus("mandatory")
_VoiceEndptMapEndptPtr_Type = ObjectIdentifier
_VoiceEndptMapEndptPtr_Object = MibTableColumn
voiceEndptMapEndptPtr = _VoiceEndptMapEndptPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15, 1, 3),
    _VoiceEndptMapEndptPtr_Type()
)
voiceEndptMapEndptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptMapEndptPtr.setStatus("mandatory")
_VoiceEndptMapConnPtr_Type = ObjectIdentifier
_VoiceEndptMapConnPtr_Object = MibTableColumn
voiceEndptMapConnPtr = _VoiceEndptMapConnPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 3, 15, 1, 4),
    _VoiceEndptMapConnPtr_Type()
)
voiceEndptMapConnPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndptMapConnPtr.setStatus("mandatory")
_SwitchShelf_ObjectIdentity = ObjectIdentity
switchShelf = _SwitchShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4)
)
_ShelfCnfgObjects_ObjectIdentity = ObjectIdentity
shelfCnfgObjects = _ShelfCnfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1)
)
_ShelfCnfgStatMaster_Type = IpAddress
_ShelfCnfgStatMaster_Object = MibScalar
shelfCnfgStatMaster = _ShelfCnfgStatMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 1),
    _ShelfCnfgStatMaster_Type()
)
shelfCnfgStatMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatMaster.setStatus("mandatory")
_ShelfCnfgStatCollIntvl_Type = Integer32
_ShelfCnfgStatCollIntvl_Object = MibScalar
shelfCnfgStatCollIntvl = _ShelfCnfgStatCollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 2),
    _ShelfCnfgStatCollIntvl_Type()
)
shelfCnfgStatCollIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatCollIntvl.setStatus("mandatory")
_ShelfCnfgStatBcktIntvl_Type = Integer32
_ShelfCnfgStatBcktIntvl_Object = MibScalar
shelfCnfgStatBcktIntvl = _ShelfCnfgStatBcktIntvl_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 3),
    _ShelfCnfgStatBcktIntvl_Type()
)
shelfCnfgStatBcktIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatBcktIntvl.setStatus("mandatory")
_ShelfCnfgStatTimeSync_Type = DisplayString
_ShelfCnfgStatTimeSync_Object = MibScalar
shelfCnfgStatTimeSync = _ShelfCnfgStatTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 4),
    _ShelfCnfgStatTimeSync_Type()
)
shelfCnfgStatTimeSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgStatTimeSync.setStatus("mandatory")


class _ShelfCnfgSwError_Type(Integer32):
    """Custom type shelfCnfgSwError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ShelfCnfgSwError_Type.__name__ = "Integer32"
_ShelfCnfgSwError_Object = MibScalar
shelfCnfgSwError = _ShelfCnfgSwError_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 5),
    _ShelfCnfgSwError_Type()
)
shelfCnfgSwError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgSwError.setStatus("mandatory")


class _ShelfCnfgCardError_Type(Integer32):
    """Custom type shelfCnfgCardError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ShelfCnfgCardError_Type.__name__ = "Integer32"
_ShelfCnfgCardError_Object = MibScalar
shelfCnfgCardError = _ShelfCnfgCardError_Object(
    (1, 3, 6, 1, 4, 1, 351, 100, 4, 4, 1, 6),
    _ShelfCnfgCardError_Type()
)
shelfCnfgCardError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCnfgCardError.setStatus("mandatory")
_Rtm_ObjectIdentity = ObjectIdentity
rtm = _Rtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120)
)
_TrapsConfig_ObjectIdentity = ObjectIdentity
trapsConfig = _TrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120, 1)
)
_TrapConfigTable_Object = MibTable
trapConfigTable = _TrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1)
)
if mibBuilder.loadTexts:
    trapConfigTable.setStatus("mandatory")
_TrapConfigEntry_Object = MibTableRow
trapConfigEntry = _TrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1)
)
trapConfigEntry.setIndexNames(
    (0, "STRATACOM-MIB", "managerIPaddress"),
)
if mibBuilder.loadTexts:
    trapConfigEntry.setStatus("mandatory")
_ManagerIPaddress_Type = IpAddress
_ManagerIPaddress_Object = MibTableColumn
managerIPaddress = _ManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1),
    _ManagerIPaddress_Type()
)
managerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPaddress.setStatus("mandatory")
_ManagerPortNumber_Type = Integer32
_ManagerPortNumber_Object = MibTableColumn
managerPortNumber = _ManagerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2),
    _ManagerPortNumber_Type()
)
managerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerPortNumber.setStatus("mandatory")


class _ManagerRowStatus_Type(Integer32):
    """Custom type managerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addRow", 1),
          ("delRow", 2))
    )


_ManagerRowStatus_Type.__name__ = "Integer32"
_ManagerRowStatus_Object = MibTableColumn
managerRowStatus = _ManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3),
    _ManagerRowStatus_Type()
)
managerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerRowStatus.setStatus("mandatory")


class _ReadingTrapFlag_Type(Integer32):
    """Custom type readingTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ReadingTrapFlag_Type.__name__ = "Integer32"
_ReadingTrapFlag_Object = MibTableColumn
readingTrapFlag = _ReadingTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4),
    _ReadingTrapFlag_Type()
)
readingTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readingTrapFlag.setStatus("mandatory")
_NextTrapSeqNum_Type = Integer32
_NextTrapSeqNum_Object = MibTableColumn
nextTrapSeqNum = _NextTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5),
    _NextTrapSeqNum_Type()
)
nextTrapSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextTrapSeqNum.setStatus("mandatory")


class _ManagerNumOfValidEntries_Type(Integer32):
    """Custom type managerNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ManagerNumOfValidEntries_Type.__name__ = "Integer32"
_ManagerNumOfValidEntries_Object = MibScalar
managerNumOfValidEntries = _ManagerNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 2),
    _ManagerNumOfValidEntries_Type()
)
managerNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerNumOfValidEntries.setStatus("mandatory")
_LastSequenceNumber_Type = Integer32
_LastSequenceNumber_Object = MibScalar
lastSequenceNumber = _LastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 3),
    _LastSequenceNumber_Type()
)
lastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSequenceNumber.setStatus("mandatory")
_TrapUploadTable_Object = MibTable
trapUploadTable = _TrapUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4)
)
if mibBuilder.loadTexts:
    trapUploadTable.setStatus("mandatory")
_TrapUploadEntry_Object = MibTableRow
trapUploadEntry = _TrapUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1)
)
trapUploadEntry.setIndexNames(
    (0, "STRATACOM-MIB", "mgrIpAddress"),
)
if mibBuilder.loadTexts:
    trapUploadEntry.setStatus("mandatory")
_MgrIpAddress_Type = IpAddress
_MgrIpAddress_Object = MibTableColumn
mgrIpAddress = _MgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1),
    _MgrIpAddress_Type()
)
mgrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgrIpAddress.setStatus("mandatory")
_TrapSequenceNum_Type = Integer32
_TrapSequenceNum_Object = MibTableColumn
trapSequenceNum = _TrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2),
    _TrapSequenceNum_Type()
)
trapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNum.setStatus("mandatory")
_TrapPduString_Type = OctetString
_TrapPduString_Object = MibTableColumn
trapPduString = _TrapPduString_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3),
    _TrapPduString_Type()
)
trapPduString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPduString.setStatus("mandatory")


class _EndOfQueueFlag_Type(Integer32):
    """Custom type endOfQueueFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_EndOfQueueFlag_Type.__name__ = "Integer32"
_EndOfQueueFlag_Object = MibTableColumn
endOfQueueFlag = _EndOfQueueFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4),
    _EndOfQueueFlag_Type()
)
endOfQueueFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfQueueFlag.setStatus("mandatory")
_StrmErrors_ObjectIdentity = ObjectIdentity
strmErrors = _StrmErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 910)
)

# Managed Objects groups


# Notification objects

filteredLogRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 4)
)
filteredLogRecord.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "logIndex"),
        ("STRATACOM-MIB", "logNetwork"),
        ("STRATACOM-MIB", "logNodeName"),
        ("STRATACOM-MIB", "logGmtDate"),
        ("STRATACOM-MIB", "logSeverity"),
        ("STRATACOM-MIB", "logMsg"))
)
if mibBuilder.loadTexts:
    filteredLogRecord.setStatus(
        ""
    )

userConnCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 10000)
)
userConnCleared.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "connectionLocalEndPt"),
        ("STRATACOM-MIB", "connectionLocalStr"),
        ("STRATACOM-MIB", "connectionRemoteEndPt"),
        ("STRATACOM-MIB", "connectionRemoteStr"),
        ("STRATACOM-MIB", "connectionOpStatus"),
        ("STRATACOM-MIB", "connectionAbitStatus"),
        ("STRATACOM-MIB", "connectionType"))
)
if mibBuilder.loadTexts:
    userConnCleared.setStatus(
        ""
    )

userConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 10001)
)
userConnFailed.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "connectionLocalEndPt"),
        ("STRATACOM-MIB", "connectionLocalStr"),
        ("STRATACOM-MIB", "connectionRemoteEndPt"),
        ("STRATACOM-MIB", "connectionRemoteStr"),
        ("STRATACOM-MIB", "connectionOpStatus"),
        ("STRATACOM-MIB", "connectionAbitStatus"),
        ("STRATACOM-MIB", "connectionType"))
)
if mibBuilder.loadTexts:
    userConnFailed.setStatus(
        ""
    )

userConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 10002)
)
userConnDown.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "connectionLocalEndPt"),
        ("STRATACOM-MIB", "connectionLocalStr"),
        ("STRATACOM-MIB", "connectionRemoteEndPt"),
        ("STRATACOM-MIB", "connectionRemoteStr"),
        ("STRATACOM-MIB", "connectionOpStatus"),
        ("STRATACOM-MIB", "connectionAbitStatus"),
        ("STRATACOM-MIB", "connectionType"))
)
if mibBuilder.loadTexts:
    userConnDown.setStatus(
        ""
    )

trunkStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 0)
)
trunkStatusAlarm.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "nodeGrpName"),
        ("STRATACOM-MIB", "nodeGrpNetName"),
        ("STRATACOM-MIB", "trunkStatus"))
)
if mibBuilder.loadTexts:
    trunkStatusAlarm.setStatus(
        ""
    )

cirLineStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 1)
)
cirLineStatusAlarm.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "nodeGrpName"),
        ("STRATACOM-MIB", "nodeGrpNetName"),
        ("STRATACOM-MIB", "cirLineStatus"))
)
if mibBuilder.loadTexts:
    cirLineStatusAlarm.setStatus(
        ""
    )

frpStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 2)
)
frpStatusAlarm.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "nodeGrpName"),
        ("STRATACOM-MIB", "nodeGrpNetName"),
        ("STRATACOM-MIB", "frpStatus"))
)
if mibBuilder.loadTexts:
    frpStatusAlarm.setStatus(
        ""
    )

connStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 3)
)
connStatusAlarm.setObjects(
      *(("STRATACOM-MIB", "lastSequenceNumber"),
        ("STRATACOM-MIB", "nodeGrpName"),
        ("STRATACOM-MIB", "nodeGrpNetName"),
        ("STRATACOM-MIB", "connStatus"),
        ("STRATACOM-MIB", "connABitStatus"))
)
if mibBuilder.loadTexts:
    connStatusAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-MIB",
    **{"DisplayString": DisplayString,
       "Active": Active,
       "Severity": Severity,
       "stratacom": stratacom,
       "svplus": svplus,
       "filteredLogRecord": filteredLogRecord,
       "userConnCleared": userConnCleared,
       "userConnFailed": userConnFailed,
       "userConnDown": userConnDown,
       "controlGroup": controlGroup,
       "databaseSampleFreq": databaseSampleFreq,
       "logGroup": logGroup,
       "currentMaxLogIndex": currentMaxLogIndex,
       "maintLogTable": maintLogTable,
       "maintLogEntry": maintLogEntry,
       "logIndex": logIndex,
       "logNetwork": logNetwork,
       "logNodeName": logNodeName,
       "logGmtDate": logGmtDate,
       "logSeverity": logSeverity,
       "logMsg": logMsg,
       "eventFilterTable": eventFilterTable,
       "eventFilterEntry": eventFilterEntry,
       "eventFilterIndex": eventFilterIndex,
       "eventFilterStatus": eventFilterStatus,
       "eventFilterSeverity": eventFilterSeverity,
       "eventFilterSubstring": eventFilterSubstring,
       "maintLogFilterGroup": maintLogFilterGroup,
       "maintLogFilterTimeMin": maintLogFilterTimeMin,
       "maintLogFilterTimeMax": maintLogFilterTimeMax,
       "maintLogFilterWindow": maintLogFilterWindow,
       "maintLogFilterNetworkName": maintLogFilterNetworkName,
       "maintLogFilterNodeName": maintLogFilterNodeName,
       "maintLogFilterSeverity": maintLogFilterSeverity,
       "networkGroup": networkGroup,
       "networkTable": networkTable,
       "networkEntry": networkEntry,
       "networkName": networkName,
       "networkId": networkId,
       "networkIpxId": networkIpxId,
       "nodeGroup": nodeGroup,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeNetworkName": nodeNetworkName,
       "nodeName": nodeName,
       "svnode": svnode,
       "trunkStatusAlarm": trunkStatusAlarm,
       "cirLineStatusAlarm": cirLineStatusAlarm,
       "frpStatusAlarm": frpStatusAlarm,
       "connStatusAlarm": connStatusAlarm,
       "svNodeGroup": svNodeGroup,
       "nodeGrpName": nodeGrpName,
       "nodeGrpNetName": nodeGrpNetName,
       "nodeGrpAlarmState": nodeGrpAlarmState,
       "nodeGrpGateway": nodeGrpGateway,
       "nodeGrpActive": nodeGrpActive,
       "nodeGrpPlatform": nodeGrpPlatform,
       "nodeGrpRelease": nodeGrpRelease,
       "nodeFsIncRate": nodeFsIncRate,
       "nodeFsDecRate": nodeFsDecRate,
       "nodeFsFastRate": nodeFsFastRate,
       "nodeRstTimeout": nodeRstTimeout,
       "alarmTrapSequenceNumber": alarmTrapSequenceNumber,
       "packetGroup": packetGroup,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkLocalSlot": trunkLocalSlot,
       "trunkLocalPort": trunkLocalPort,
       "trunkLocalLine": trunkLocalLine,
       "trunkCardType": trunkCardType,
       "trunkInterface": trunkInterface,
       "trunkLineLoad": trunkLineLoad,
       "trunkRemNodeId": trunkRemNodeId,
       "trunkRemLineNumber": trunkRemLineNumber,
       "trunkRemSlot": trunkRemSlot,
       "trunkRemPort": trunkRemPort,
       "trunkAlarmState": trunkAlarmState,
       "trunkComment": trunkComment,
       "trunkActive": trunkActive,
       "trunkStatus": trunkStatus,
       "trunkStatReserve": trunkStatReserve,
       "trunkBurstyDataBQDepth": trunkBurstyDataBQDepth,
       "trunkBurstyDataBQEfcnThreshold": trunkBurstyDataBQEfcnThreshold,
       "trunkClpHighDropThreshold": trunkClpHighDropThreshold,
       "trunkClpLowDropThreshold": trunkClpLowDropThreshold,
       "circuitGroup": circuitGroup,
       "cirLineTable": cirLineTable,
       "cirLineEntry": cirLineEntry,
       "cirLineLineNumber": cirLineLineNumber,
       "cirLineCardType": cirLineCardType,
       "cirLineInterface": cirLineInterface,
       "cirLineComment": cirLineComment,
       "cirLineActive": cirLineActive,
       "cirLineStatus": cirLineStatus,
       "cirLinePortNumber": cirLinePortNumber,
       "frpGroup": frpGroup,
       "frpTable": frpTable,
       "frpEntry": frpEntry,
       "frpLocalSlot": frpLocalSlot,
       "frpLocalPort": frpLocalPort,
       "frpPortSpeed": frpPortSpeed,
       "frpComment": frpComment,
       "frpActive": frpActive,
       "frpStatus": frpStatus,
       "frpQDepth": frpQDepth,
       "frpEcnThreshold": frpEcnThreshold,
       "frpDeThreshold": frpDeThreshold,
       "frpPortType": frpPortType,
       "frpLocalLine": frpLocalLine,
       "connGroup": connGroup,
       "connServerTable": connServerTable,
       "connEntry": connEntry,
       "connLocalSlot": connLocalSlot,
       "connLocalChannel": connLocalChannel,
       "connLocalDLCI": connLocalDLCI,
       "connRemoteNodeId": connRemoteNodeId,
       "connRemoteSlot": connRemoteSlot,
       "connRemoteChannel": connRemoteChannel,
       "connRemoteDLCI": connRemoteDLCI,
       "connServerType": connServerType,
       "connRate": connRate,
       "connLocalMaxPkts": connLocalMaxPkts,
       "connRemoteMaxPkts": connRemoteMaxPkts,
       "connMinBandwidth": connMinBandwidth,
       "connDAX": connDAX,
       "connTXR": connTXR,
       "connComment": connComment,
       "connActive": connActive,
       "connStatus": connStatus,
       "connQir": connQir,
       "connPir": connPir,
       "connVcQueDepth": connVcQueDepth,
       "connVcQueThreshold": connVcQueThreshold,
       "connCMax": connCMax,
       "connPerUtil": connPerUtil,
       "connConnInfoFlag": connConnInfoFlag,
       "connCir": connCir,
       "connABitStatus": connABitStatus,
       "connLocalLine": connLocalLine,
       "realTimeCountersGroup": realTimeCountersGroup,
       "cirLineRTCTable": cirLineRTCTable,
       "cirLineRTCEntry": cirLineRTCEntry,
       "cirLineRTCLineNumber": cirLineRTCLineNumber,
       "cirLineRTCBipolarViolations": cirLineRTCBipolarViolations,
       "cirLineRTCFrameSlips": cirLineRTCFrameSlips,
       "cirLineRTCOutOfFrames": cirLineRTCOutOfFrames,
       "cirLineRTCLossesOfSignal": cirLineRTCLossesOfSignal,
       "cirLineRTCFrameBitErrors": cirLineRTCFrameBitErrors,
       "cirLineRTCCrcErrors": cirLineRTCCrcErrors,
       "cirLineRTCOutOfMultiFrames": cirLineRTCOutOfMultiFrames,
       "cirLineRTCAllOnesInTimeslot16": cirLineRTCAllOnesInTimeslot16,
       "frpRTCTable": frpRTCTable,
       "frpRTCEntry": frpRTCEntry,
       "frpRTCSlot": frpRTCSlot,
       "frpRTCPort": frpRTCPort,
       "frpRTCFramesRcvd": frpRTCFramesRcvd,
       "frpRTCFramesXmitted": frpRTCFramesXmitted,
       "frpRTCBytesRcvd": frpRTCBytesRcvd,
       "frpRTCBytesXmitted": frpRTCBytesXmitted,
       "frpRTCFramesXmittedWithFECN": frpRTCFramesXmittedWithFECN,
       "frpRTCFramesXmittedWithBECN": frpRTCFramesXmittedWithBECN,
       "frpRTCFramesRcvdCrcErrors": frpRTCFramesRcvdCrcErrors,
       "frpRTCFramesRcvdInvalidFormat": frpRTCFramesRcvdInvalidFormat,
       "frpRTCFramesRcvdAlignmentErrors": frpRTCFramesRcvdAlignmentErrors,
       "frpRTCFramesRcvdIllegalLen": frpRTCFramesRcvdIllegalLen,
       "frpRTCDmaOverruns": frpRTCDmaOverruns,
       "frpRTCLmiStatusEnquires": frpRTCLmiStatusEnquires,
       "frpRTCLmiStatusXmitRate": frpRTCLmiStatusXmitRate,
       "frpRTCLmiStatusUpdateRate": frpRTCLmiStatusUpdateRate,
       "frpRTCLmiInvalidStatusEnquires": frpRTCLmiInvalidStatusEnquires,
       "frpRTCLmiLinkTimeoutErrors": frpRTCLmiLinkTimeoutErrors,
       "frpRTCLmiKeepaliveSequenceErrors": frpRTCLmiKeepaliveSequenceErrors,
       "frpRTCFramesRcvdUndefDlciErrors": frpRTCFramesRcvdUndefDlciErrors,
       "frpRTCXmitStatusEnquirey": frpRTCXmitStatusEnquirey,
       "frpRTCRxStatusCounter": frpRTCRxStatusCounter,
       "frpRTCAsyncStatusCounter": frpRTCAsyncStatusCounter,
       "frpRTCBadSequenceNumberCount": frpRTCBadSequenceNumberCount,
       "frpRTCTxProtocolTimeOutCount": frpRTCTxProtocolTimeOutCount,
       "frpRTCCLLMFramesTx": frpRTCCLLMFramesTx,
       "frpRTCCLLMBytesTx": frpRTCCLLMBytesTx,
       "frpRTCCLLMFramesRx": frpRTCCLLMFramesRx,
       "frpRTCCLLMBytesRx": frpRTCCLLMBytesRx,
       "frpRTCCLLMFailures": frpRTCCLLMFailures,
       "frpRTCRxDEFramesDiscarded": frpRTCRxDEFramesDiscarded,
       "frpRTCLine": frpRTCLine,
       "connRTCTable": connRTCTable,
       "connRTCEntry": connRTCEntry,
       "connRTCSlot": connRTCSlot,
       "connRTCChannel": connRTCChannel,
       "connRTCDLCI": connRTCDLCI,
       "connRTCRcvdFrames": connRTCRcvdFrames,
       "connRTCRcvdFramesDiscarded": connRTCRcvdFramesDiscarded,
       "connRTCXmitFrames": connRTCXmitFrames,
       "connRTCXmitFramesDiscarded": connRTCXmitFramesDiscarded,
       "connRTCRcvdPkts": connRTCRcvdPkts,
       "connRTCRcvdPktsDiscarded": connRTCRcvdPktsDiscarded,
       "connRTCXmitPkts": connRTCXmitPkts,
       "connRTCXmitPktsProjected": connRTCXmitPktsProjected,
       "connRTCXmitPktsSupervisory": connRTCXmitPktsSupervisory,
       "connRTCRcvdBytes": connRTCRcvdBytes,
       "connRTCRcvdBytesDiscarded": connRTCRcvdBytesDiscarded,
       "connRTCXmitBytes": connRTCXmitBytes,
       "connRTCXmitBytesDiscarded": connRTCXmitBytesDiscarded,
       "connRTCSecondsV25ModemOn": connRTCSecondsV25ModemOn,
       "connRTCSecondsDsiEnabled": connRTCSecondsDsiEnabled,
       "connRTCSecondsOffHook": connRTCSecondsOffHook,
       "connRTCSecondsInService": connRTCSecondsInService,
       "connRTCXmitFramesWithFECN": connRTCXmitFramesWithFECN,
       "connRTCXmitFramesWithBECN": connRTCXmitFramesWithBECN,
       "connRTCRxSupervisoryPkts": connRTCRxSupervisoryPkts,
       "connRTCCongestedMinuites": connRTCCongestedMinuites,
       "connRTCFramesRxWithDE": connRTCFramesRxWithDE,
       "connRTCFramesTxWithDE": connRTCFramesTxWithDE,
       "connRTCFramesDiscardedWithDE": connRTCFramesDiscardedWithDE,
       "connRTCBytesRxWithDE": connRTCBytesRxWithDE,
       "connRTCFramesRxExcessCir": connRTCFramesRxExcessCir,
       "connRTCBytesRxExcessCir": connRTCBytesRxExcessCir,
       "connRTCFramesTxExcessCir": connRTCFramesTxExcessCir,
       "connRTCBytesTxExcessCir": connRTCBytesTxExcessCir,
       "connRTCLine": connRTCLine,
       "trunkRTCTable": trunkRTCTable,
       "trunkRTCEntry": trunkRTCEntry,
       "trunkRTCLocalSlot": trunkRTCLocalSlot,
       "trunkRTCLocalPort": trunkRTCLocalPort,
       "trunkRTCBipolarViolations": trunkRTCBipolarViolations,
       "trunkRTCFrameSlips": trunkRTCFrameSlips,
       "trunkRTCOutOfFrames": trunkRTCOutOfFrames,
       "trunkRTCLossOfSignal": trunkRTCLossOfSignal,
       "trunkRTCFrameBitErrors": trunkRTCFrameBitErrors,
       "trunkRTCCrcErrors": trunkRTCCrcErrors,
       "trunkRTCPktOutOfFrames": trunkRTCPktOutOfFrames,
       "trunkRTCPktCrcErrors": trunkRTCPktCrcErrors,
       "trunkRTCBadClockErrors": trunkRTCBadClockErrors,
       "trunkRTCVoicePktsDropped": trunkRTCVoicePktsDropped,
       "trunkRTCTimeStampedPktsDropped": trunkRTCTimeStampedPktsDropped,
       "trunkRTCNonTimeStampedPktsDropped": trunkRTCNonTimeStampedPktsDropped,
       "trunkRTCHighPriorityPktsDropped": trunkRTCHighPriorityPktsDropped,
       "trunkRTCBurstyDataPktsDropped": trunkRTCBurstyDataPktsDropped,
       "trunkRTCMulticastPktsDropped": trunkRTCMulticastPktsDropped,
       "trunkRTCVoicePktsXmitted": trunkRTCVoicePktsXmitted,
       "trunkRTCTimeStampedPktsXmitted": trunkRTCTimeStampedPktsXmitted,
       "trunkRTCNonTimeStampedPktsXmitted": trunkRTCNonTimeStampedPktsXmitted,
       "trunkRTCHighPriorityPktsXmitted": trunkRTCHighPriorityPktsXmitted,
       "trunkRTCBurstyDataPktsXmitted": trunkRTCBurstyDataPktsXmitted,
       "trunkRTCMulticastPktsXmitted": trunkRTCMulticastPktsXmitted,
       "trunkRTCPktsXmitted": trunkRTCPktsXmitted,
       "trunkRTCTxBurstyDataAClpPktsDropped": trunkRTCTxBurstyDataAClpPktsDropped,
       "trunkRTCTxBurstyDataBClpPktsDropped": trunkRTCTxBurstyDataBClpPktsDropped,
       "trunkRTCBurstyDataAEfcnPktsTx2Line": trunkRTCBurstyDataAEfcnPktsTx2Line,
       "trunkRTCBurstyDataBEfcnPktsTx2Line": trunkRTCBurstyDataBEfcnPktsTx2Line,
       "trunkRTCBurstyDataAClpPktsTx2Line": trunkRTCBurstyDataAClpPktsTx2Line,
       "trunkRTCBurstyDataBClpPktsTx2Line": trunkRTCBurstyDataBClpPktsTx2Line,
       "trunkRTCAtmCellHeaderHecErrors": trunkRTCAtmCellHeaderHecErrors,
       "trunkRTCTxVoiceCellsDropped": trunkRTCTxVoiceCellsDropped,
       "trunkRTCTxTimeStampCellsDropped": trunkRTCTxTimeStampCellsDropped,
       "trunkRTCTxNonTStampCellsDropped": trunkRTCTxNonTStampCellsDropped,
       "trunkRTCTxHighPriorityCellsDropped": trunkRTCTxHighPriorityCellsDropped,
       "trunkRTCTxBurstyDataACellsDropped": trunkRTCTxBurstyDataACellsDropped,
       "trunkRTCTxBurstyDataBCellsDropped": trunkRTCTxBurstyDataBCellsDropped,
       "trunkRTCVoiceCellsTx2Line": trunkRTCVoiceCellsTx2Line,
       "trunkRTCTimeStampCellsTx2Line": trunkRTCTimeStampCellsTx2Line,
       "trunkRTCNonTimeStampCellsTx2Line": trunkRTCNonTimeStampCellsTx2Line,
       "trunkRTCHighPriorityCellsTx2Line": trunkRTCHighPriorityCellsTx2Line,
       "trunkRTCBurstyDataACellsTx2Line": trunkRTCBurstyDataACellsTx2Line,
       "trunkRTCBurstyDataBCellsTx2Line": trunkRTCBurstyDataBCellsTx2Line,
       "trunkRTCTotalCellsTx2Line": trunkRTCTotalCellsTx2Line,
       "trunkRTCTxBurstyDataAClpCellsDropped": trunkRTCTxBurstyDataAClpCellsDropped,
       "trunkRTCTxBurstyDataBClpCellsDropped": trunkRTCTxBurstyDataBClpCellsDropped,
       "trunkRTCBurstyDataAEfcnCellsTx2Line": trunkRTCBurstyDataAEfcnCellsTx2Line,
       "trunkRTCBurstyDataBEfcnCellsTx2Line": trunkRTCBurstyDataBEfcnCellsTx2Line,
       "trunkRTCPlcpOutOfFrames": trunkRTCPlcpOutOfFrames,
       "connSvc": connSvc,
       "connMibUpTime": connMibUpTime,
       "connAvailIndex": connAvailIndex,
       "connectionTable": connectionTable,
       "connectionEntry": connectionEntry,
       "connectionIndex": connectionIndex,
       "connectionLocalEndPt": connectionLocalEndPt,
       "connectionRemoteEndPt": connectionRemoteEndPt,
       "connectionAdminStatus": connectionAdminStatus,
       "connectionOpStatus": connectionOpStatus,
       "connectionRowStatus": connectionRowStatus,
       "connectionTrkAvoidType": connectionTrkAvoidType,
       "connectionTrkAvoidZCS": connectionTrkAvoidZCS,
       "connectionForesight": connectionForesight,
       "connectionClassOfService": connectionClassOfService,
       "connectionCurrRouteDesc": connectionCurrRouteDesc,
       "connectionPrefRouteDesc": connectionPrefRouteDesc,
       "connRouteMaster": connRouteMaster,
       "connectionLocOSpacePkts": connectionLocOSpacePkts,
       "connectionLocOSpaceBdaCmax": connectionLocOSpaceBdaCmax,
       "connectionLocOSpaceBdbCmax": connectionLocOSpaceBdbCmax,
       "connectionRemOSpacePkts": connectionRemOSpacePkts,
       "connectionRemOSpaceBdaCmax": connectionRemOSpaceBdaCmax,
       "connectionRemOSpaceBdbCmax": connectionRemOSpaceBdbCmax,
       "connectionTestType": connectionTestType,
       "connectionTestResult": connectionTestResult,
       "connectionAbitStatus": connectionAbitStatus,
       "connectionType": connectionType,
       "connectionLocalStr": connectionLocalStr,
       "connectionRemoteStr": connectionRemoteStr,
       "frEndPtTable": frEndPtTable,
       "frEndPtEntry": frEndPtEntry,
       "frEndPtNodeName": frEndPtNodeName,
       "frEndPtIfShelf": frEndPtIfShelf,
       "frEndPtSlot": frEndPtSlot,
       "frEndPtLine": frEndPtLine,
       "frEndPtPort": frEndPtPort,
       "frEndPtDlci": frEndPtDlci,
       "frEndPtConnIndex": frEndPtConnIndex,
       "frEndPtAdminStatus": frEndPtAdminStatus,
       "frEndPtOpStatus": frEndPtOpStatus,
       "frEndPtRowStatus": frEndPtRowStatus,
       "frEndPtMIR": frEndPtMIR,
       "frEndPtCIR": frEndPtCIR,
       "frEndPtBc": frEndPtBc,
       "frEndPtBe": frEndPtBe,
       "frEndPtVcQSize": frEndPtVcQSize,
       "frEndPtPIR": frEndPtPIR,
       "frEndPtCMAX": frEndPtCMAX,
       "frEndPtEcnQSize": frEndPtEcnQSize,
       "frEndPtQIR": frEndPtQIR,
       "frEndPtPercUtil": frEndPtPercUtil,
       "frEndPtPriority": frEndPtPriority,
       "frEndPtInitialBurstSize": frEndPtInitialBurstSize,
       "frEndPtDeTagging": frEndPtDeTagging,
       "frEndPtIngressDeThreshold": frEndPtIngressDeThreshold,
       "frEndPtEgressQDepth": frEndPtEgressQDepth,
       "frEndPtEgressDeThreshold": frEndPtEgressDeThreshold,
       "frEndPtEgressEcnThreshold": frEndPtEgressEcnThreshold,
       "frEndPtEgressQSelect": frEndPtEgressQSelect,
       "frEndPtLpbkState": frEndPtLpbkState,
       "frEndPtType": frEndPtType,
       "frEndPtchanType": frEndPtchanType,
       "frEndPtchanFECNconfig": frEndPtchanFECNconfig,
       "frEndPtchanDEtoCLPmap": frEndPtchanDEtoCLPmap,
       "frEndPtchanCLPtoDEmap": frEndPtchanCLPtoDEmap,
       "aitEndPtTable": aitEndPtTable,
       "aitEndPtEntry": aitEndPtEntry,
       "aitEndPtNodeName": aitEndPtNodeName,
       "aitEndPtIfShelf": aitEndPtIfShelf,
       "aitEndPtSlot": aitEndPtSlot,
       "aitEndPtVpi": aitEndPtVpi,
       "aitEndPtVci": aitEndPtVci,
       "aitEndPtConnIndex": aitEndPtConnIndex,
       "aitEndPtAdminStatus": aitEndPtAdminStatus,
       "aitEndPtOpStatus": aitEndPtOpStatus,
       "aitEndPtMIR": aitEndPtMIR,
       "aitEndPtCIR": aitEndPtCIR,
       "aitEndPtVcQSize": aitEndPtVcQSize,
       "aitEndPtPIR": aitEndPtPIR,
       "aitEndPtCMAX": aitEndPtCMAX,
       "aitEndPtEcnQSize": aitEndPtEcnQSize,
       "aitEndPtQIR": aitEndPtQIR,
       "aitEndPtPercUtil": aitEndPtPercUtil,
       "aitEndPtPriority": aitEndPtPriority,
       "atmEndPtTable": atmEndPtTable,
       "atmEndPtEntry": atmEndPtEntry,
       "atmEndPtNodeName": atmEndPtNodeName,
       "atmEndPtIfShelf": atmEndPtIfShelf,
       "atmEndPtSlot": atmEndPtSlot,
       "atmEndPtPort": atmEndPtPort,
       "atmEndPtVpi": atmEndPtVpi,
       "atmEndPtVci": atmEndPtVci,
       "atmEndPtConnIndex": atmEndPtConnIndex,
       "atmEndPtAdminStatus": atmEndPtAdminStatus,
       "atmEndPtOpStatus": atmEndPtOpStatus,
       "atmEndPtRowStatus": atmEndPtRowStatus,
       "atmEndPtMIR": atmEndPtMIR,
       "atmEndPtCIR": atmEndPtCIR,
       "atmEndPtPIR": atmEndPtPIR,
       "atmEndPtQIR": atmEndPtQIR,
       "atmEndPtPercUtil": atmEndPtPercUtil,
       "atmEndPtPriority": atmEndPtPriority,
       "atmEndPtIBS": atmEndPtIBS,
       "atmEndPtVcQSize": atmEndPtVcQSize,
       "segmentTable": segmentTable,
       "segmentEntry": segmentEntry,
       "segEndPtTableId": segEndPtTableId,
       "segNodeName": segNodeName,
       "segShelf": segShelf,
       "segSlot": segSlot,
       "segLine": segLine,
       "segPort": segPort,
       "segSubChn1": segSubChn1,
       "segSubChn2": segSubChn2,
       "segOeEndPt": segOeEndPt,
       "segConnIndex": segConnIndex,
       "segNextSeg": segNextSeg,
       "cmpaErrorLastIndex": cmpaErrorLastIndex,
       "cmpaErrorFlushAll": cmpaErrorFlushAll,
       "cmpaErrorTable": cmpaErrorTable,
       "cmpaErrorEntry": cmpaErrorEntry,
       "cmpaErrorReqId": cmpaErrorReqId,
       "cmpaErrorDesc": cmpaErrorDesc,
       "cmpaErrorEcode": cmpaErrorEcode,
       "cmpaErrorLastDesc": cmpaErrorLastDesc,
       "cmpaErrorLastEcode": cmpaErrorLastEcode,
       "portSvc": portSvc,
       "portsInfoTable": portsInfoTable,
       "portsInfoEntry": portsInfoEntry,
       "portsInfoNode": portsInfoNode,
       "portsInfoShelf": portsInfoShelf,
       "portsInfoSlot": portsInfoSlot,
       "portsInfoLine": portsInfoLine,
       "portsInfoPort": portsInfoPort,
       "portsInfoPortType": portsInfoPortType,
       "portsInfoPortState": portsInfoPortState,
       "portsInfoPortSpeed": portsInfoPortSpeed,
       "frPortsCfgTable": frPortsCfgTable,
       "frPortsCfgEntry": frPortsCfgEntry,
       "frPortsCfgNode": frPortsCfgNode,
       "frPortsCfgShelf": frPortsCfgShelf,
       "frPortsCfgSlot": frPortsCfgSlot,
       "frPortsCfgLine": frPortsCfgLine,
       "frPortsCfgPort": frPortsCfgPort,
       "frPortsCfgRowStatus": frPortsCfgRowStatus,
       "frPortsCfgPortType": frPortsCfgPortType,
       "frPortsCfgPortState": frPortsCfgPortState,
       "frPortsCfgChCnt": frPortsCfgChCnt,
       "frPortsCfgPortSpeed": frPortsCfgPortSpeed,
       "frPortsCfgDs0ChSpeed": frPortsCfgDs0ChSpeed,
       "frPortsCfgSigProt": frPortsCfgSigProt,
       "frPortsCfgNNIStatus": frPortsCfgNNIStatus,
       "frPortsCfgAsyncUpd": frPortsCfgAsyncUpd,
       "frPortsCfgPollVerTimer": frPortsCfgPollVerTimer,
       "frPortsCfgErrThresh": frPortsCfgErrThresh,
       "frPortsCfgMonEveCnt": frPortsCfgMonEveCnt,
       "frPortsCfgFrmFlags": frPortsCfgFrmFlags,
       "frPortsCfgLinkTimer": frPortsCfgLinkTimer,
       "frPortsCfgPollCycle": frPortsCfgPollCycle,
       "frAxPortsCfgSvcRatio": frAxPortsCfgSvcRatio,
       "frIxPortsCfgClockType": frIxPortsCfgClockType,
       "frIxPortsCfgVcCount": frIxPortsCfgVcCount,
       "frPortsCfgVcPtr": frPortsCfgVcPtr,
       "frIxPortsCfgMaxTxQDepth": frIxPortsCfgMaxTxQDepth,
       "frIxPortsCfgECNQThresh": frIxPortsCfgECNQThresh,
       "frIxPortsCfgDEThresh": frIxPortsCfgDEThresh,
       "frIxPortsCfgIDEMap": frIxPortsCfgIDEMap,
       "frIxPortsCfgCommPri": frIxPortsCfgCommPri,
       "frIxPortsCfgUpRNR": frIxPortsCfgUpRNR,
       "frIxPortsCfgLowRNR": frIxPortsCfgLowRNR,
       "frIxPortsCfgOamThresh": frIxPortsCfgOamThresh,
       "frIxPortsCfgCLLMTimer": frIxPortsCfgCLLMTimer,
       "frIxPortsCfgEFCItoBECN": frIxPortsCfgEFCItoBECN,
       "frIxPortsCfgSrRTS": frIxPortsCfgSrRTS,
       "frIxPortsCfgSrDTR": frIxPortsCfgSrDTR,
       "frIxPortsCfgSrDCD": frIxPortsCfgSrDCD,
       "frIxPortsCfgSrCTS": frIxPortsCfgSrCTS,
       "frIxPortsCfgSrDSR": frIxPortsCfgSrDSR,
       "frIxPortsCfgLoopBack": frIxPortsCfgLoopBack,
       "frIxPortsCfgExtConFail": frIxPortsCfgExtConFail,
       "frAxPortsCfgLogPort": frAxPortsCfgLogPort,
       "ppaErrorLastIndex": ppaErrorLastIndex,
       "ppaErrorFlushAll": ppaErrorFlushAll,
       "ppaErrorTable": ppaErrorTable,
       "ppaErrorEntry": ppaErrorEntry,
       "ppaErrorReqId": ppaErrorReqId,
       "ppaErrorDesc": ppaErrorDesc,
       "ppaErrorEcode": ppaErrorEcode,
       "ppaErrorLastDesc": ppaErrorLastDesc,
       "ppaErrorLastEcode": ppaErrorLastEcode,
       "snmpAgents": snmpAgents,
       "strmSwitchMIB": strmSwitchMIB,
       "switchInterfaces": switchInterfaces,
       "switchIfTable": switchIfTable,
       "switchIfEntry": switchIfEntry,
       "switchIfIndex": switchIfIndex,
       "switchIfSlot": switchIfSlot,
       "switchIfPort": switchIfPort,
       "switchIfSubPort": switchIfSubPort,
       "switchIfMediaType": switchIfMediaType,
       "switchIfService": switchIfService,
       "switchIfAdmStatus": switchIfAdmStatus,
       "switchIfOperStatus": switchIfOperStatus,
       "switchIfPhysPort": switchIfPhysPort,
       "switchIfPartiId": switchIfPartiId,
       "switchIfCtrlerId": switchIfCtrlerId,
       "switchServiceObjects": switchServiceObjects,
       "frServiceObjects": frServiceObjects,
       "frLportCnfTable": frLportCnfTable,
       "frLportCnfEntry": frLportCnfEntry,
       "frLportSlotIndex": frLportSlotIndex,
       "frLportPortIndex": frLportPortIndex,
       "frLportPortDLCI": frLportPortDLCI,
       "frLportAdminStatus": frLportAdminStatus,
       "frLportOperStatus": frLportOperStatus,
       "frLportPortSpeed": frLportPortSpeed,
       "frLportClockType": frLportClockType,
       "frLportPortType": frLportPortType,
       "frLportVcCount": frLportVcCount,
       "frLportFirstVcPtr": frLportFirstVcPtr,
       "frLportAggrChCnt": frLportAggrChCnt,
       "frLportChSpeed": frLportChSpeed,
       "frLportMaxTxQDepth": frLportMaxTxQDepth,
       "frLportECNQThresh": frLportECNQThresh,
       "frLportDEThresh": frLportDEThresh,
       "frLportIDEMap": frLportIDEMap,
       "frLportSigProt": frLportSigProt,
       "frLportNNIStatus": frLportNNIStatus,
       "frLportAsynStatus": frLportAsynStatus,
       "frLportPolVerTmr": frLportPolVerTmr,
       "frLportErrThresh": frLportErrThresh,
       "frLportMonEveCnt": frLportMonEveCnt,
       "frLportCommPri": frLportCommPri,
       "frLportUpRNR": frLportUpRNR,
       "frLportLowRNR": frLportLowRNR,
       "frLportMinFrmFlgs": frLportMinFrmFlgs,
       "frLportOamThresh": frLportOamThresh,
       "frLportLinkTimer": frLportLinkTimer,
       "frLportPollCycle": frLportPollCycle,
       "frLportCLLMTimer": frLportCLLMTimer,
       "frLportEFCItoBECN": frLportEFCItoBECN,
       "frLportSrRTS": frLportSrRTS,
       "frLportSrDTR": frLportSrDTR,
       "frLportSrDCD": frLportSrDCD,
       "frLportSrCTS": frLportSrCTS,
       "frLportSrDSR": frLportSrDSR,
       "frLportLoopBack": frLportLoopBack,
       "frLportExtConFail": frLportExtConFail,
       "frLportStatTable": frLportStatTable,
       "frLportStatEntry": frLportStatEntry,
       "frLportRxBytes": frLportRxBytes,
       "frLportRxFrms": frLportRxFrms,
       "frLportTxBytes": frLportTxBytes,
       "frLportTxFrms": frLportTxFrms,
       "frLportTxFrmsFecns": frLportTxFrmsFecns,
       "frLportTxFrmsBecns": frLportTxFrmsBecns,
       "frLportCrcErrors": frLportCrcErrors,
       "frLportBadFmts": frLportBadFmts,
       "frLportAlgnErrors": frLportAlgnErrors,
       "frLportIllegLengths": frLportIllegLengths,
       "frLportDmaOvruns": frLportDmaOvruns,
       "frLportStatEnqUnis": frLportStatEnqUnis,
       "frLportStatTxUnis": frLportStatTxUnis,
       "frLportUpdtTxUnis": frLportUpdtTxUnis,
       "frLportInvldReqCnts": frLportInvldReqCnts,
       "frLportToutCntUnis": frLportToutCntUnis,
       "frLportSeqnmErrUnis": frLportSeqnmErrUnis,
       "frLportUnknDlcis": frLportUnknDlcis,
       "frLportDeFrmsDrops": frLportDeFrmsDrops,
       "frLportStatEnqNnis": frLportStatEnqNnis,
       "frLportStatRxNnis": frLportStatRxNnis,
       "frLportUpdtRxNnis": frLportUpdtRxNnis,
       "frLportToutCntNnis": frLportToutCntNnis,
       "frLportSeqnmErrNnis": frLportSeqnmErrNnis,
       "frLportCllmTxFrms": frLportCllmTxFrms,
       "frLportCllmTxBytes": frLportCllmTxBytes,
       "frLportCllmRxFrms": frLportCllmRxFrms,
       "frLportCllmRxBytes": frLportCllmRxBytes,
       "frLportCllmFailures": frLportCllmFailures,
       "frLportDscdQTxFrms": frLportDscdQTxFrms,
       "frLportDscdQTxBytes": frLportDscdQTxBytes,
       "frLportLmiFailFrms": frLportLmiFailFrms,
       "frLportLmiFailBytes": frLportLmiFailBytes,
       "atmServiceObjects": atmServiceObjects,
       "atmPortTable": atmPortTable,
       "atmPortEntry": atmPortEntry,
       "atmPortSlot": atmPortSlot,
       "atmPortPort": atmPortPort,
       "atmPortAdminStatus": atmPortAdminStatus,
       "atmPortOperStatus": atmPortOperStatus,
       "atmPortType": atmPortType,
       "atmPortIfType": atmPortIfType,
       "atmPortSpeed": atmPortSpeed,
       "atmPortAxis": atmPortAxis,
       "atmPortVcCount": atmPortVcCount,
       "atmPortFirstVcPtr": atmPortFirstVcPtr,
       "atmPortMetro": atmPortMetro,
       "atmPortMgmtProto": atmPortMgmtProto,
       "atmPortIlmiVpi": atmPortIlmiVpi,
       "atmPortIlmiVci": atmPortIlmiVci,
       "atmPortIlmiPollEnable": atmPortIlmiPollEnable,
       "atmPortIlmiTrapEnable": atmPortIlmiTrapEnable,
       "atmPortIlmiPollIntrvl": atmPortIlmiPollIntrvl,
       "atmPortIlmiErrorThresh": atmPortIlmiErrorThresh,
       "atmPortIlmiEventThresh": atmPortIlmiEventThresh,
       "atmPortLmiVpi": atmPortLmiVpi,
       "atmPortLmiVci": atmPortLmiVci,
       "atmPortLmiPollEnable": atmPortLmiPollEnable,
       "atmPortLmiStatEnqTimer": atmPortLmiStatEnqTimer,
       "atmPortLmiUpdStatTimer": atmPortLmiUpdStatTimer,
       "atmPortLmiStatEnqRetry": atmPortLmiStatEnqRetry,
       "atmPortLmiUpdStatRetry": atmPortLmiUpdStatRetry,
       "atmPortLmiPollTimer": atmPortLmiPollTimer,
       "atmPortPercUtil": atmPortPercUtil,
       "atmPortQueueTable": atmPortQueueTable,
       "atmPortQueueEntry": atmPortQueueEntry,
       "atmPortQueueIndex": atmPortQueueIndex,
       "atmPortQueueAdminStatus": atmPortQueueAdminStatus,
       "atmPortQueueType": atmPortQueueType,
       "atmPortQueueDepth": atmPortQueueDepth,
       "atmPortQueueClpHi": atmPortQueueClpHi,
       "atmPortQueueClpLo": atmPortQueueClpLo,
       "atmPortQueueEfciTh": atmPortQueueEfciTh,
       "atmPortQueueAlgorithm": atmPortQueueAlgorithm,
       "atmPortStatTable": atmPortStatTable,
       "atmPortStatEntry": atmPortStatEntry,
       "atmPortStatUnknVpiVcis": atmPortStatUnknVpiVcis,
       "atmPortStatBufferOvfls": atmPortStatBufferOvfls,
       "atmPortStatNonZeroGfcs": atmPortStatNonZeroGfcs,
       "atmPortStatIsuDiscards": atmPortStatIsuDiscards,
       "atmPortStatIsuEmptys": atmPortStatIsuEmptys,
       "atmPortStatAisRxs": atmPortStatAisRxs,
       "atmPortStatFerfRxs": atmPortStatFerfRxs,
       "atmPortStatCellsRxs": atmPortStatCellsRxs,
       "atmPortStatClpRxs": atmPortStatClpRxs,
       "atmPortStatEfciRxs": atmPortStatEfciRxs,
       "atmPortStatBcmRxs": atmPortStatBcmRxs,
       "atmPortStatCellsTxs": atmPortStatCellsTxs,
       "atmPortStatOamRxs": atmPortStatOamRxs,
       "atmPortStatPayldErrs": atmPortStatPayldErrs,
       "atmPortStatClpTxs": atmPortStatClpTxs,
       "atmPortStatEfciTxs": atmPortStatEfciTxs,
       "atmPortStatHdrDiscards": atmPortStatHdrDiscards,
       "atmPortStatIlmiGetRxs": atmPortStatIlmiGetRxs,
       "atmPortStatIlmiGetNextRxs": atmPortStatIlmiGetNextRxs,
       "atmPortStatIlmiGetNextTxs": atmPortStatIlmiGetNextTxs,
       "atmPortStatIlmiSetRxs": atmPortStatIlmiSetRxs,
       "atmPortStatIlmiTrapRxs": atmPortStatIlmiTrapRxs,
       "atmPortStatIlmiGetRspRxs": atmPortStatIlmiGetRspRxs,
       "atmPortStatIlmiGetTxs": atmPortStatIlmiGetTxs,
       "atmPortStatIlmiGetRspTxs": atmPortStatIlmiGetRspTxs,
       "atmPortStatIlmiTrapTxs": atmPortStatIlmiTrapTxs,
       "atmPortStatIlmiUnkRxs": atmPortStatIlmiUnkRxs,
       "atmPortStatLmiStatTxs": atmPortStatLmiStatTxs,
       "atmPortStatLmiUpdtStatTxs": atmPortStatLmiUpdtStatTxs,
       "atmPortStatLmiStatAckTxs": atmPortStatLmiStatAckTxs,
       "atmPortStatLmiStatEnqTxs": atmPortStatLmiStatEnqTxs,
       "atmPortStatLmiStatEnqRxs": atmPortStatLmiStatEnqRxs,
       "atmPortStatLmiStatRxs": atmPortStatLmiStatRxs,
       "atmPortStatLmiUpdStatRxs": atmPortStatLmiUpdStatRxs,
       "atmPortStatLmiStatAckRxs": atmPortStatLmiStatAckRxs,
       "voiceServiceObjects": voiceServiceObjects,
       "voiceChannelTable": voiceChannelTable,
       "voiceChannelEntry": voiceChannelEntry,
       "voiceChannelSlotIndex": voiceChannelSlotIndex,
       "voiceChannelChannelIndex": voiceChannelChannelIndex,
       "voiceChannelAdminStatus": voiceChannelAdminStatus,
       "voiceChannelEndptPtr": voiceChannelEndptPtr,
       "voiceChannelIf": voiceChannelIf,
       "voiceChannelAdapVoice": voiceChannelAdapVoice,
       "voiceChannelDialType": voiceChannelDialType,
       "voiceChannelDtSignallingDelay": voiceChannelDtSignallingDelay,
       "voiceChannelDtMinWink": voiceChannelDtMinWink,
       "voiceChannelDtPlayOutDelay": voiceChannelDtPlayOutDelay,
       "voiceChannelRecvSigABit": voiceChannelRecvSigABit,
       "voiceChannelRecvSigBBit": voiceChannelRecvSigBBit,
       "voiceChannelRecvSigCBit": voiceChannelRecvSigCBit,
       "voiceChannelRecvSigDBit": voiceChannelRecvSigDBit,
       "voiceChannelXmitSigABit": voiceChannelXmitSigABit,
       "voiceChannelXmitSigBBit": voiceChannelXmitSigBBit,
       "voiceChannelXmitSigCBit": voiceChannelXmitSigCBit,
       "voiceChannelXmitSigDBit": voiceChannelXmitSigDBit,
       "voiceChannelIfTypeName": voiceChannelIfTypeName,
       "voiceChannelIfOnhkABit": voiceChannelIfOnhkABit,
       "voiceChannelIfOnhkBBit": voiceChannelIfOnhkBBit,
       "voiceChannelIfOnhkCBit": voiceChannelIfOnhkCBit,
       "voiceChannelIfOnhkDBit": voiceChannelIfOnhkDBit,
       "voiceChannelIfCondIndex": voiceChannelIfCondIndex,
       "voiceChannelEchoCancel": voiceChannelEchoCancel,
       "voiceChannelEchoRtnLoss": voiceChannelEchoRtnLoss,
       "voiceChannelEchoTone": voiceChannelEchoTone,
       "voiceChannelEchoConv": voiceChannelEchoConv,
       "voiceChannelEchoNlp": voiceChannelEchoNlp,
       "voiceChannelInGain": voiceChannelInGain,
       "voiceChannelOutGain": voiceChannelOutGain,
       "voiceChannelUtil": voiceChannelUtil,
       "trunkServiceObjects": trunkServiceObjects,
       "atmTrunks": atmTrunks,
       "atmTrkEntry": atmTrkEntry,
       "atmTrkStatus": atmTrkStatus,
       "atmTrkAlmEnable": atmTrkAlmEnable,
       "atmTrkComStatus": atmTrkComStatus,
       "atmTrkRcvRate": atmTrkRcvRate,
       "atmTrkTrnsCap": atmTrkTrnsCap,
       "atmTrkTrnsLoad": atmTrkTrnsLoad,
       "atmTrkRcvCap": atmTrkRcvCap,
       "atmTrkRcvLoad": atmTrkRcvLoad,
       "atmTrkType": atmTrkType,
       "atmTrkVPI": atmTrkVPI,
       "atmTrkResChans": atmTrkResChans,
       "atmTrkTrafCls": atmTrkTrafCls,
       "atmTrkOeNdType": atmTrkOeNdType,
       "atmTrkOeName": atmTrkOeName,
       "atmTrkOeIpAddr": atmTrkOeIpAddr,
       "atmTrkOeIfIndex": atmTrkOeIfIndex,
       "atmTrkOeDomain": atmTrkOeDomain,
       "atmTrkSvcChannels": atmTrkSvcChannels,
       "atmTrkShareLcn": atmTrkShareLcn,
       "atmTrkSvcLcnLow": atmTrkSvcLcnLow,
       "atmTrkSvcLcnHigh": atmTrkSvcLcnHigh,
       "atmTrkSvcVpiLow": atmTrkSvcVpiLow,
       "atmTrkSvcVpiHigh": atmTrkSvcVpiHigh,
       "atmTrkSvcVciLow": atmTrkSvcVciLow,
       "atmTrkSvcVciHigh": atmTrkSvcVciHigh,
       "atmTrkSvcQbinBitMap": atmTrkSvcQbinBitMap,
       "atmTrkSvcQbinSz": atmTrkSvcQbinSz,
       "atmTrkSvcBw": atmTrkSvcBw,
       "atmTrkSvcInUse": atmTrkSvcInUse,
       "atmTrkXmitRate": atmTrkXmitRate,
       "atmTrkPassSync": atmTrkPassSync,
       "atmTrkStatRes": atmTrkStatRes,
       "atmTrkLoopClock": atmTrkLoopClock,
       "atmTrkBdataBTxQlen": atmTrkBdataBTxQlen,
       "atmTrkBdataBRxQlen": atmTrkBdataBRxQlen,
       "atmTrkBdataBTxEfcn": atmTrkBdataBTxEfcn,
       "atmTrkBdataBRxEfcn": atmTrkBdataBRxEfcn,
       "atmTrkBdataBTxHiClp": atmTrkBdataBTxHiClp,
       "atmTrkBdataBRxHiClp": atmTrkBdataBRxHiClp,
       "atmTrkBdataBTxLoClp": atmTrkBdataBTxLoClp,
       "atmTrkBdataBRxLoClp": atmTrkBdataBRxLoClp,
       "atmTrkMaxChanPort": atmTrkMaxChanPort,
       "atmTrkLinkType": atmTrkLinkType,
       "atmTrkDerouteDelayTimer": atmTrkDerouteDelayTimer,
       "atmTrkGtwyChCount": atmTrkGtwyChCount,
       "atmTrkRetainedLinks": atmTrkRetainedLinks,
       "atmTrkImaWindowSize": atmTrkImaWindowSize,
       "atmTrkImaTrnsCnts": atmTrkImaTrnsCnts,
       "atmTrkImaReenableTimer": atmTrkImaReenableTimer,
       "atmTrunkStatsTable": atmTrunkStatsTable,
       "atmTrkStatsEntry": atmTrkStatsEntry,
       "atmTrkStatsTxVoPktDrps": atmTrkStatsTxVoPktDrps,
       "atmTrkStatsTxTsPktDrps": atmTrkStatsTxTsPktDrps,
       "atmTrkStatsTxNonTsPktDrps": atmTrkStatsTxNonTsPktDrps,
       "atmTrkStatsTxHiPrioPktDrps": atmTrkStatsTxHiPrioPktDrps,
       "atmTrkStatsTxBdataAPktDrps": atmTrkStatsTxBdataAPktDrps,
       "atmTrkStatsTxBdataBPktDrps": atmTrkStatsTxBdataBPktDrps,
       "atmTrkStatsRxVoPktDrps": atmTrkStatsRxVoPktDrps,
       "atmTrkStatsRxTsPktDrps": atmTrkStatsRxTsPktDrps,
       "atmTrkStatsRxNonTsPktDrps": atmTrkStatsRxNonTsPktDrps,
       "atmTrkStatsRxHiPrioPktDrps": atmTrkStatsRxHiPrioPktDrps,
       "atmTrkStatsRxBdataAPktDrps": atmTrkStatsRxBdataAPktDrps,
       "atmTrkStatsRxBdataBPktDrps": atmTrkStatsRxBdataBPktDrps,
       "atmTrkStatsSpacerPktsDrps": atmTrkStatsSpacerPktsDrps,
       "atmTrkStatsTotalPktsTxtoLns": atmTrkStatsTotalPktsTxtoLns,
       "atmTrkStatsTotalPktsRxFromLns": atmTrkStatsTotalPktsRxFromLns,
       "atmTrkStatsTxVoCellDrps": atmTrkStatsTxVoCellDrps,
       "atmTrkStatsTxTsCellDrps": atmTrkStatsTxTsCellDrps,
       "atmTrkStatsTxNonTsCellDrps": atmTrkStatsTxNonTsCellDrps,
       "atmTrkStatsTxHiPrioCellDrps": atmTrkStatsTxHiPrioCellDrps,
       "atmTrkStatsTxBdataACellDrps": atmTrkStatsTxBdataACellDrps,
       "atmTrkStatsTxBdataBCellDrps": atmTrkStatsTxBdataBCellDrps,
       "atmTrkStatsTxCbrCellDrps": atmTrkStatsTxCbrCellDrps,
       "atmTrkStatsTxVbrCellDrps": atmTrkStatsTxVbrCellDrps,
       "atmTrkStatsTxAbrCellDrps": atmTrkStatsTxAbrCellDrps,
       "atmTrkStatsTotalCellsTxtoLns": atmTrkStatsTotalCellsTxtoLns,
       "atmTrkStatsTotalCellsRxFromPorts": atmTrkStatsTotalCellsRxFromPorts,
       "switchConnection": switchConnection,
       "connNextEndptIndex": connNextEndptIndex,
       "errStatusLastIndex": errStatusLastIndex,
       "errStatusTable": errStatusTable,
       "errStatusTableEntry": errStatusTableEntry,
       "errReqId": errReqId,
       "errCode": errCode,
       "errStatusDesc": errStatusDesc,
       "connTable": connTable,
       "connTableEntry": connTableEntry,
       "connIndex": connIndex,
       "connLclEndptDesc": connLclEndptDesc,
       "connType": connType,
       "connOeIndex": connOeIndex,
       "connRmtEndptDesc": connRmtEndptDesc,
       "connMasterFlag": connMasterFlag,
       "connClassOfService": connClassOfService,
       "connGroupFlag": connGroupFlag,
       "connAdminStatus": connAdminStatus,
       "connOperStatus": connOperStatus,
       "connNoRouteFoundFailure": connNoRouteFoundFailure,
       "connBumpFailure": connBumpFailure,
       "connFirstEndptPtr": connFirstEndptPtr,
       "connCurrRouteDesc": connCurrRouteDesc,
       "connPrefRouteDesc": connPrefRouteDesc,
       "connMstOSpacePkts": connMstOSpacePkts,
       "connMstOSpaceCells": connMstOSpaceCells,
       "connMstOSpaceBdaCmax": connMstOSpaceBdaCmax,
       "connMstOSpaceBdbCmax": connMstOSpaceBdbCmax,
       "connSlvOSpacePkts": connSlvOSpacePkts,
       "connSlvOSpaceCells": connSlvOSpaceCells,
       "connSlvOSpaceBdaCmax": connSlvOSpaceBdaCmax,
       "connSlvOSpaceBdbCmax": connSlvOSpaceBdbCmax,
       "connIcaRTD": connIcaRTD,
       "connGroupDesc": connGroupDesc,
       "frEndptTable": frEndptTable,
       "frEndptEntry": frEndptEntry,
       "frEndptIndex": frEndptIndex,
       "frEndptDesc": frEndptDesc,
       "frOtherEndptIndex": frOtherEndptIndex,
       "frOtherEndptDesc": frOtherEndptDesc,
       "frEndptAdminStatus": frEndptAdminStatus,
       "frEndptOperStatus": frEndptOperStatus,
       "frNoRouteFoundFailure": frNoRouteFoundFailure,
       "frBumpFailure": frBumpFailure,
       "frEndPointFailure": frEndPointFailure,
       "frTestFailure": frTestFailure,
       "frConnPtr": frConnPtr,
       "frNextPtr": frNextPtr,
       "frNextOnPortPtr": frNextOnPortPtr,
       "frEndptConnDesc": frEndptConnDesc,
       "frEndptTrkAvoidType": frEndptTrkAvoidType,
       "frEndptTrkAvoidZCS": frEndptTrkAvoidZCS,
       "frEndptSubType": frEndptSubType,
       "frEndptBWClass": frEndptBWClass,
       "frEndptMIR": frEndptMIR,
       "frEndptCIR": frEndptCIR,
       "frEndptBc": frEndptBc,
       "frEndptBe": frEndptBe,
       "frEndptVcQSize": frEndptVcQSize,
       "frEndptPIR": frEndptPIR,
       "frEndptCMAX": frEndptCMAX,
       "frEndptEcnQSize": frEndptEcnQSize,
       "frEndptQIR": frEndptQIR,
       "frEndptPercUtil": frEndptPercUtil,
       "frEndptOeMIR": frEndptOeMIR,
       "frEndptOeCIR": frEndptOeCIR,
       "frEndptOeBc": frEndptOeBc,
       "frEndptOeBe": frEndptOeBe,
       "frEndptOeVcQSize": frEndptOeVcQSize,
       "frEndptOePIR": frEndptOePIR,
       "frEndptOeCMAX": frEndptOeCMAX,
       "frEndptOeEcnQSize": frEndptOeEcnQSize,
       "frEndptOeQIR": frEndptOeQIR,
       "frEndptOePercUtil": frEndptOePercUtil,
       "frEndptEnableFST": frEndptEnableFST,
       "frEndptConnPrio": frEndptConnPrio,
       "frEndptGroupFlag": frEndptGroupFlag,
       "frEndptLocLpbkState": frEndptLocLpbkState,
       "frEndptLocRmtLpbkState": frEndptLocRmtLpbkState,
       "frEndptLpbkStatus": frEndptLpbkStatus,
       "frEndptTestType": frEndptTestType,
       "frEndptRtdTestDelay": frEndptRtdTestDelay,
       "frEndptGroupDesc": frEndptGroupDesc,
       "frEndptStatTable": frEndptStatTable,
       "frEndptStatEntry": frEndptStatEntry,
       "frEndptRxBytes": frEndptRxBytes,
       "frEndptRxBytesDscds": frEndptRxBytesDscds,
       "frEndptRxFrms": frEndptRxFrms,
       "frEndptRxFrmsDscds": frEndptRxFrmsDscds,
       "frEndptRxPkts": frEndptRxPkts,
       "frEndptRxPktsDscds": frEndptRxPktsDscds,
       "frEndptTxBytes": frEndptTxBytes,
       "frEndptTxBytesDscds": frEndptTxBytesDscds,
       "frEndptTxFrms": frEndptTxFrms,
       "frEndptTxFrmsDscds": frEndptTxFrmsDscds,
       "frEndptTxPkts": frEndptTxPkts,
       "frEndptTxFrmsFecns": frEndptTxFrmsFecns,
       "frEndptTxFrmsBecns": frEndptTxFrmsBecns,
       "frEndptSecInServices": frEndptSecInServices,
       "frEndptCongestMins": frEndptCongestMins,
       "frEndptRxFrmsDes": frEndptRxFrmsDes,
       "frEndptRxBytesDes": frEndptRxBytesDes,
       "frEndptTxFrmsDes": frEndptTxFrmsDes,
       "frEndptRxFrmsDeDscds": frEndptRxFrmsDeDscds,
       "frEndptRxFrmsCirs": frEndptRxFrmsCirs,
       "frEndptRxBytesCirs": frEndptRxBytesCirs,
       "frEndptTxFrmsCirs": frEndptTxFrmsCirs,
       "frEndptTxBytesCirs": frEndptTxBytesCirs,
       "frBwClassTable": frBwClassTable,
       "frBwClassEntry": frBwClassEntry,
       "frBwClassIndex": frBwClassIndex,
       "frBwClassMIR": frBwClassMIR,
       "frBwClassCIR": frBwClassCIR,
       "frBwClassVcQSize": frBwClassVcQSize,
       "frBwClassBc": frBwClassBc,
       "frBwClassPIR": frBwClassPIR,
       "frBwClassBe": frBwClassBe,
       "frBwClassCMAX": frBwClassCMAX,
       "frBwClassEcnQSize": frBwClassEcnQSize,
       "frBwClassQIR": frBwClassQIR,
       "frBwClassPercUtil": frBwClassPercUtil,
       "frBwClassOeMIR": frBwClassOeMIR,
       "frBwClassOeCIR": frBwClassOeCIR,
       "frBwClassOeVcQSize": frBwClassOeVcQSize,
       "frBwClassOeBc": frBwClassOeBc,
       "frBwClassOePIR": frBwClassOePIR,
       "frBwClassOeBe": frBwClassOeBe,
       "frBwClassOeCMAX": frBwClassOeCMAX,
       "frBwClassOeEcnQSize": frBwClassOeEcnQSize,
       "frBwClassOeQIR": frBwClassOeQIR,
       "frBwClassOePercUtil": frBwClassOePercUtil,
       "frBwClassEnableFST": frBwClassEnableFST,
       "frBwClassDescription": frBwClassDescription,
       "atmEndptTable": atmEndptTable,
       "atmEndptEntry": atmEndptEntry,
       "atmEndptIndex": atmEndptIndex,
       "atmEndptDesc": atmEndptDesc,
       "atmOtherEndptIndex": atmOtherEndptIndex,
       "atmOtherEndptDesc": atmOtherEndptDesc,
       "atmEndptAdminStatus": atmEndptAdminStatus,
       "atmEndptOperStatus": atmEndptOperStatus,
       "atmNoRouteFoundFailure": atmNoRouteFoundFailure,
       "atmBumpFailure": atmBumpFailure,
       "atmEndPointFailure": atmEndPointFailure,
       "atmTestFailure": atmTestFailure,
       "atmConnPtr": atmConnPtr,
       "atmNextPtr": atmNextPtr,
       "atmNextOnPortPtr": atmNextOnPortPtr,
       "atmEndptConnDesc": atmEndptConnDesc,
       "atmEndptTrkAvoidType": atmEndptTrkAvoidType,
       "atmEndptTrkAvoidZCS": atmEndptTrkAvoidZCS,
       "atmEndptSubType": atmEndptSubType,
       "atmEndptBWClass": atmEndptBWClass,
       "atmEndptMIR": atmEndptMIR,
       "atmEndptCIR": atmEndptCIR,
       "atmEndptVcQSize": atmEndptVcQSize,
       "atmEndptPIR": atmEndptPIR,
       "atmEndptEfciQSize": atmEndptEfciQSize,
       "atmEndptQIR": atmEndptQIR,
       "atmEndptPercUtil": atmEndptPercUtil,
       "atmEndptCBS": atmEndptCBS,
       "atmEndptIBS": atmEndptIBS,
       "atmEndptMFS": atmEndptMFS,
       "atmEndptCCDV": atmEndptCCDV,
       "atmEndptHiCLP": atmEndptHiCLP,
       "atmEndptLoCLP": atmEndptLoCLP,
       "atmEndptOeMIR": atmEndptOeMIR,
       "atmEndptOeCIR": atmEndptOeCIR,
       "atmEndptOeVcQSize": atmEndptOeVcQSize,
       "atmEndptOePIR": atmEndptOePIR,
       "atmEndptOeEfciQSize": atmEndptOeEfciQSize,
       "atmEndptOeQIR": atmEndptOeQIR,
       "atmEndptOePercUtil": atmEndptOePercUtil,
       "atmEndptOeCBS": atmEndptOeCBS,
       "atmEndptOeIBS": atmEndptOeIBS,
       "atmEndptOeMFS": atmEndptOeMFS,
       "atmEndptOeCCDV": atmEndptOeCCDV,
       "atmEndptOeHiCLP": atmEndptOeHiCLP,
       "atmEndptOeLoCLP": atmEndptOeLoCLP,
       "atmEndptCLPTagging": atmEndptCLPTagging,
       "atmEndptUPC": atmEndptUPC,
       "atmEndptEnableFST": atmEndptEnableFST,
       "atmEndptRateUpICA": atmEndptRateUpICA,
       "atmEndptRateDnICA": atmEndptRateDnICA,
       "atmEndptFastDnICA": atmEndptFastDnICA,
       "atmEndptToQIR": atmEndptToQIR,
       "atmEndptMinAdjustICA": atmEndptMinAdjustICA,
       "atmEndptGroupFlag": atmEndptGroupFlag,
       "atmEndptOamStatus": atmEndptOamStatus,
       "atmEndptBCM": atmEndptBCM,
       "atmEndptFGCRA": atmEndptFGCRA,
       "atmEndptLocLpbkState": atmEndptLocLpbkState,
       "atmEndptLpbkStatus": atmEndptLpbkStatus,
       "atmEndptTestType": atmEndptTestType,
       "atmEndptRtdTestDelay": atmEndptRtdTestDelay,
       "atmEndptOeBCM": atmEndptOeBCM,
       "atmEndptOeFGCRA": atmEndptOeFGCRA,
       "atmEndptGroupDesc": atmEndptGroupDesc,
       "atmEndptLocRmtLpbkState": atmEndptLocRmtLpbkState,
       "atmEndptScrPlc": atmEndptScrPlc,
       "atmEndptOeScrPlc": atmEndptOeScrPlc,
       "atmEndptPCR0": atmEndptPCR0,
       "atmEndptOePCR0": atmEndptOePCR0,
       "atmEndptCDVT0": atmEndptCDVT0,
       "atmEndptOeCDVT0": atmEndptOeCDVT0,
       "atmEndptOeRateUpICA": atmEndptOeRateUpICA,
       "atmEndptFRTT": atmEndptFRTT,
       "atmEndptTBE": atmEndptTBE,
       "atmEndptVSVD": atmEndptVSVD,
       "atmEndptPolicing": atmEndptPolicing,
       "atmEndptPCR": atmEndptPCR,
       "atmBwClassTable": atmBwClassTable,
       "atmBwClassEntry": atmBwClassEntry,
       "atmBwClassIndex": atmBwClassIndex,
       "atmBwClassMIR": atmBwClassMIR,
       "atmBwClassCIR": atmBwClassCIR,
       "atmBwClassVcQSize": atmBwClassVcQSize,
       "atmBwClassPIR": atmBwClassPIR,
       "atmBwClassEfciQSize": atmBwClassEfciQSize,
       "atmBwClassQIR": atmBwClassQIR,
       "atmBwClassPercUtil": atmBwClassPercUtil,
       "atmBwClassCBS": atmBwClassCBS,
       "atmBwClassIBS": atmBwClassIBS,
       "atmBwClassMFS": atmBwClassMFS,
       "atmBwClassCCDV": atmBwClassCCDV,
       "atmBwClassHiCLP": atmBwClassHiCLP,
       "atmBwClassLoCLP": atmBwClassLoCLP,
       "atmBwClassOeMIR": atmBwClassOeMIR,
       "atmBwClassOeCIR": atmBwClassOeCIR,
       "atmBwClassOeVcQSize": atmBwClassOeVcQSize,
       "atmBwClassOePIR": atmBwClassOePIR,
       "atmBwClassOeEfciQSize": atmBwClassOeEfciQSize,
       "atmBwClassOeQIR": atmBwClassOeQIR,
       "atmBwClassOePercUtil": atmBwClassOePercUtil,
       "atmBwClassOeCBS": atmBwClassOeCBS,
       "atmBwClassOeIBS": atmBwClassOeIBS,
       "atmBwClassOeMFS": atmBwClassOeMFS,
       "atmBwClassOeCCDV": atmBwClassOeCCDV,
       "atmBwClassOeHiCLP": atmBwClassOeHiCLP,
       "atmBwClassOeLoCLP": atmBwClassOeLoCLP,
       "atmBwClassCLPTagging": atmBwClassCLPTagging,
       "atmBwClassUPC": atmBwClassUPC,
       "atmBwClassEnableFST": atmBwClassEnableFST,
       "atmBwClassRateUpICA": atmBwClassRateUpICA,
       "atmBwClassRateDnICA": atmBwClassRateDnICA,
       "atmBwClassFastDnICA": atmBwClassFastDnICA,
       "atmBwClassToQIR": atmBwClassToQIR,
       "atmBwClassMinAdjustICA": atmBwClassMinAdjustICA,
       "atmBwClassDescription": atmBwClassDescription,
       "atmBwClassBCM": atmBwClassBCM,
       "atmBwClassFGCRA": atmBwClassFGCRA,
       "atmBwClassOeBCM": atmBwClassOeBCM,
       "atmBwClassOeFGCRA": atmBwClassOeFGCRA,
       "atmBwClassConType": atmBwClassConType,
       "atmBwClassScrPlc": atmBwClassScrPlc,
       "atmBwClassOeScrPlc": atmBwClassOeScrPlc,
       "atmBwClassPCR0": atmBwClassPCR0,
       "atmBwClassOePCR0": atmBwClassOePCR0,
       "atmBwClassCDVT0": atmBwClassCDVT0,
       "atmBwClassOeCDVT0": atmBwClassOeCDVT0,
       "atmBwClassOeRateUpICA": atmBwClassOeRateUpICA,
       "frEndptMapTable": frEndptMapTable,
       "frEndptMapEntry": frEndptMapEntry,
       "frEndptMapSlot": frEndptMapSlot,
       "frEndptMapPort": frEndptMapPort,
       "frEndptMapDlci": frEndptMapDlci,
       "frEndptMapEndptPtr": frEndptMapEndptPtr,
       "frEndptMapConnPtr": frEndptMapConnPtr,
       "atmEndptMapTable": atmEndptMapTable,
       "atmEndptMapEntry": atmEndptMapEntry,
       "atmEndptMapSlot": atmEndptMapSlot,
       "atmEndptMapPort": atmEndptMapPort,
       "atmEndptMapVpi": atmEndptMapVpi,
       "atmEndptMapVci": atmEndptMapVci,
       "atmEndptMapEndptPtr": atmEndptMapEndptPtr,
       "atmEndptMapConnPtr": atmEndptMapConnPtr,
       "atmEndptStatTable": atmEndptStatTable,
       "atmEndptStatEntry": atmEndptStatEntry,
       "atmCellsRxPorts": atmCellsRxPorts,
       "atmFramesRxPorts": atmFramesRxPorts,
       "atmCellsTxNets": atmCellsTxNets,
       "atmClpRxs": atmClpRxs,
       "atmViolRxs": atmViolRxs,
       "atmDiscardVcqClpThs": atmDiscardVcqClpThs,
       "atmDiscardVcqFulls": atmDiscardVcqFulls,
       "atmEfciRxs": atmEfciRxs,
       "atmNonCompRxs": atmNonCompRxs,
       "atmDiscardFails": atmDiscardFails,
       "atmAvgVcqDepths": atmAvgVcqDepths,
       "atmDiscardRsrcOflows": atmDiscardRsrcOflows,
       "atmDiscardSbinFulls": atmDiscardSbinFulls,
       "atmBcmRxs": atmBcmRxs,
       "atmBcmTxs": atmBcmTxs,
       "atmOamTxs": atmOamTxs,
       "atmDiscardQbinFulls": atmDiscardQbinFulls,
       "atmDiscardQbinClpThs": atmDiscardQbinClpThs,
       "atmCellsRxNets": atmCellsRxNets,
       "atmClpTxs": atmClpTxs,
       "atmEfciTxs": atmEfciTxs,
       "atmCellsTxPorts": atmCellsTxPorts,
       "atmAisRxs": atmAisRxs,
       "atmFerfRxs": atmFerfRxs,
       "voiceEndptTable": voiceEndptTable,
       "voiceEndptEntry": voiceEndptEntry,
       "voiceEndptIndex": voiceEndptIndex,
       "voiceOtherEndptIndex": voiceOtherEndptIndex,
       "voiceEndptDesc": voiceEndptDesc,
       "voiceOtherEndptDesc": voiceOtherEndptDesc,
       "voiceEndptConnDesc": voiceEndptConnDesc,
       "voiceEndptAdminStatus": voiceEndptAdminStatus,
       "voiceEndptOperStatus": voiceEndptOperStatus,
       "voiceEndptRateType": voiceEndptRateType,
       "voiceEndPointFailure": voiceEndPointFailure,
       "voiceNoRouteFoundFailure": voiceNoRouteFoundFailure,
       "voiceBumpFailure": voiceBumpFailure,
       "voiceTestFailure": voiceTestFailure,
       "voiceEndptTestType": voiceEndptTestType,
       "voiceEndptLpbkStatus": voiceEndptLpbkStatus,
       "voiceConnPtr": voiceConnPtr,
       "voiceChannelPtr": voiceChannelPtr,
       "voiceEndptTrkAvoidType": voiceEndptTrkAvoidType,
       "voiceEndptAvoidZCS": voiceEndptAvoidZCS,
       "voiceEndptState": voiceEndptState,
       "voiceEndptAdv": voiceEndptAdv,
       "voiceOtherEndptAdv": voiceOtherEndptAdv,
       "voiceEndptEncoding": voiceEndptEncoding,
       "voiceOtherEndptEncoding": voiceOtherEndptEncoding,
       "voiceEndptEndptType": voiceEndptEndptType,
       "voiceEndptLocLpbkState": voiceEndptLocLpbkState,
       "voiceStatTable": voiceStatTable,
       "voiceStatEntry": voiceStatEntry,
       "voiceStatPktsRxs": voiceStatPktsRxs,
       "voiceStatPktsXmits": voiceStatPktsXmits,
       "voiceStatRxPktsDscds": voiceStatRxPktsDscds,
       "voiceStatSprvPktsXmits": voiceStatSprvPktsXmits,
       "voiceStatSprvPktsRcvs": voiceStatSprvPktsRcvs,
       "voiceStatV25ModemOns": voiceStatV25ModemOns,
       "voiceStatDsiOns": voiceStatDsiOns,
       "voiceStatOffhks": voiceStatOffhks,
       "voiceStatInservices": voiceStatInservices,
       "voiceEndptMapTable": voiceEndptMapTable,
       "voiceEndptMapEntry": voiceEndptMapEntry,
       "voiceEndptMapSlot": voiceEndptMapSlot,
       "voiceEndptMapChannel": voiceEndptMapChannel,
       "voiceEndptMapEndptPtr": voiceEndptMapEndptPtr,
       "voiceEndptMapConnPtr": voiceEndptMapConnPtr,
       "switchShelf": switchShelf,
       "shelfCnfgObjects": shelfCnfgObjects,
       "shelfCnfgStatMaster": shelfCnfgStatMaster,
       "shelfCnfgStatCollIntvl": shelfCnfgStatCollIntvl,
       "shelfCnfgStatBcktIntvl": shelfCnfgStatBcktIntvl,
       "shelfCnfgStatTimeSync": shelfCnfgStatTimeSync,
       "shelfCnfgSwError": shelfCnfgSwError,
       "shelfCnfgCardError": shelfCnfgCardError,
       "rtm": rtm,
       "trapsConfig": trapsConfig,
       "trapConfigTable": trapConfigTable,
       "trapConfigEntry": trapConfigEntry,
       "managerIPaddress": managerIPaddress,
       "managerPortNumber": managerPortNumber,
       "managerRowStatus": managerRowStatus,
       "readingTrapFlag": readingTrapFlag,
       "nextTrapSeqNum": nextTrapSeqNum,
       "managerNumOfValidEntries": managerNumOfValidEntries,
       "lastSequenceNumber": lastSequenceNumber,
       "trapUploadTable": trapUploadTable,
       "trapUploadEntry": trapUploadEntry,
       "mgrIpAddress": mgrIpAddress,
       "trapSequenceNum": trapSequenceNum,
       "trapPduString": trapPduString,
       "endOfQueueFlag": endOfQueueFlag,
       "strmErrors": strmErrors}
)
