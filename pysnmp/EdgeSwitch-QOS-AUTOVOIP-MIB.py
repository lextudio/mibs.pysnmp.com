# SNMP MIB module (EdgeSwitch-QOS-AUTOVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-QOS-AUTOVOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:59 2024
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "EdgeSwitch-QOS-MIB",
    "fastPathQOS")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathQOSAUTOVOIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4)
)
fastPathQOSAUTOVOIP.setRevisions(
        ("2012-02-18 00:00",
         "2011-01-26 00:00",
         "2007-11-23 00:00",
         "2007-11-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentAutoVoIPCfgGroup_ObjectIdentity = ObjectIdentity
agentAutoVoIPCfgGroup = _AgentAutoVoIPCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1)
)
_AgentAutoVoIPVLAN_Type = Integer32
_AgentAutoVoIPVLAN_Object = MibScalar
agentAutoVoIPVLAN = _AgentAutoVoIPVLAN_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1),
    _AgentAutoVoIPVLAN_Type()
)
agentAutoVoIPVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPVLAN.setStatus("current")
_AgentAutoVoIPOUIPriority_Type = Integer32
_AgentAutoVoIPOUIPriority_Object = MibScalar
agentAutoVoIPOUIPriority = _AgentAutoVoIPOUIPriority_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 2),
    _AgentAutoVoIPOUIPriority_Type()
)
agentAutoVoIPOUIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIPriority.setStatus("current")


class _AgentAutoVoIPProtocolPriScheme_Type(Integer32):
    """Custom type agentAutoVoIPProtocolPriScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remark", 2),
          ("trafficClass", 1))
    )


_AgentAutoVoIPProtocolPriScheme_Type.__name__ = "Integer32"
_AgentAutoVoIPProtocolPriScheme_Object = MibScalar
agentAutoVoIPProtocolPriScheme = _AgentAutoVoIPProtocolPriScheme_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 3),
    _AgentAutoVoIPProtocolPriScheme_Type()
)
agentAutoVoIPProtocolPriScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPProtocolPriScheme.setStatus("current")


class _AgentAutoVoIPProtocolTcOrRemarkValue_Type(Unsigned32):
    """Custom type agentAutoVoIPProtocolTcOrRemarkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentAutoVoIPProtocolTcOrRemarkValue_Type.__name__ = "Unsigned32"
_AgentAutoVoIPProtocolTcOrRemarkValue_Object = MibScalar
agentAutoVoIPProtocolTcOrRemarkValue = _AgentAutoVoIPProtocolTcOrRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 4),
    _AgentAutoVoIPProtocolTcOrRemarkValue_Type()
)
agentAutoVoIPProtocolTcOrRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPProtocolTcOrRemarkValue.setStatus("current")
_AgentAutoVoIPTable_Object = MibTable
agentAutoVoIPTable = _AgentAutoVoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    agentAutoVoIPTable.setStatus("current")
_AgentAutoVoIPEntry_Object = MibTableRow
agentAutoVoIPEntry = _AgentAutoVoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1)
)
agentAutoVoIPEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"),
)
if mibBuilder.loadTexts:
    agentAutoVoIPEntry.setStatus("current")
_AgentAutoVoIPIntfIndex_Type = InterfaceIndex
_AgentAutoVoIPIntfIndex_Object = MibTableColumn
agentAutoVoIPIntfIndex = _AgentAutoVoIPIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 1),
    _AgentAutoVoIPIntfIndex_Type()
)
agentAutoVoIPIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAutoVoIPIntfIndex.setStatus("current")


class _AgentAutoVoIPProtocolMode_Type(Integer32):
    """Custom type agentAutoVoIPProtocolMode based on Integer32"""
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


_AgentAutoVoIPProtocolMode_Type.__name__ = "Integer32"
_AgentAutoVoIPProtocolMode_Object = MibTableColumn
agentAutoVoIPProtocolMode = _AgentAutoVoIPProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 2),
    _AgentAutoVoIPProtocolMode_Type()
)
agentAutoVoIPProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPProtocolMode.setStatus("current")


class _AgentAutoVoIPOUIMode_Type(Integer32):
    """Custom type agentAutoVoIPOUIMode based on Integer32"""
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


_AgentAutoVoIPOUIMode_Type.__name__ = "Integer32"
_AgentAutoVoIPOUIMode_Object = MibTableColumn
agentAutoVoIPOUIMode = _AgentAutoVoIPOUIMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 3),
    _AgentAutoVoIPOUIMode_Type()
)
agentAutoVoIPOUIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIMode.setStatus("current")


class _AgentAutoVoIPProtocolPortStatus_Type(Integer32):
    """Custom type agentAutoVoIPProtocolPortStatus based on Integer32"""
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


_AgentAutoVoIPProtocolPortStatus_Type.__name__ = "Integer32"
_AgentAutoVoIPProtocolPortStatus_Object = MibTableColumn
agentAutoVoIPProtocolPortStatus = _AgentAutoVoIPProtocolPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 4),
    _AgentAutoVoIPProtocolPortStatus_Type()
)
agentAutoVoIPProtocolPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPProtocolPortStatus.setStatus("current")


class _AgentAutoVoIPOUIPortStatus_Type(Integer32):
    """Custom type agentAutoVoIPOUIPortStatus based on Integer32"""
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


_AgentAutoVoIPOUIPortStatus_Type.__name__ = "Integer32"
_AgentAutoVoIPOUIPortStatus_Object = MibTableColumn
agentAutoVoIPOUIPortStatus = _AgentAutoVoIPOUIPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 5),
    _AgentAutoVoIPOUIPortStatus_Type()
)
agentAutoVoIPOUIPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIPortStatus.setStatus("current")
_AgentAutoVoIPOUITable_Object = MibTable
agentAutoVoIPOUITable = _AgentAutoVoIPOUITable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    agentAutoVoIPOUITable.setStatus("current")
_AgentAutoVoIPOUIEntry_Object = MibTableRow
agentAutoVoIPOUIEntry = _AgentAutoVoIPOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1)
)
agentAutoVoIPOUIEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPOUIIndex"),
)
if mibBuilder.loadTexts:
    agentAutoVoIPOUIEntry.setStatus("current")


class _AgentAutoVoIPOUIIndex_Type(Integer32):
    """Custom type agentAutoVoIPOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentAutoVoIPOUIIndex_Type.__name__ = "Integer32"
_AgentAutoVoIPOUIIndex_Object = MibTableColumn
agentAutoVoIPOUIIndex = _AgentAutoVoIPOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 1),
    _AgentAutoVoIPOUIIndex_Type()
)
agentAutoVoIPOUIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIIndex.setStatus("current")


class _AgentAutoVoIPOUI_Type(OctetString):
    """Custom type agentAutoVoIPOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AgentAutoVoIPOUI_Type.__name__ = "OctetString"
_AgentAutoVoIPOUI_Object = MibTableColumn
agentAutoVoIPOUI = _AgentAutoVoIPOUI_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 2),
    _AgentAutoVoIPOUI_Type()
)
agentAutoVoIPOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPOUI.setStatus("current")


class _AgentAutoVoIPOUIDesc_Type(OctetString):
    """Custom type agentAutoVoIPOUIDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentAutoVoIPOUIDesc_Type.__name__ = "OctetString"
_AgentAutoVoIPOUIDesc_Object = MibTableColumn
agentAutoVoIPOUIDesc = _AgentAutoVoIPOUIDesc_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 3),
    _AgentAutoVoIPOUIDesc_Type()
)
agentAutoVoIPOUIDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIDesc.setStatus("current")
_AgentAutoVoIPOUIRowStatus_Type = RowStatus
_AgentAutoVoIPOUIRowStatus_Object = MibTableColumn
agentAutoVoIPOUIRowStatus = _AgentAutoVoIPOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 4),
    _AgentAutoVoIPOUIRowStatus_Type()
)
agentAutoVoIPOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentAutoVoIPOUIRowStatus.setStatus("current")
_AgentAutoVoIPSessionTable_Object = MibTable
agentAutoVoIPSessionTable = _AgentAutoVoIPSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    agentAutoVoIPSessionTable.setStatus("current")
_AgentAutoVoIPSessionEntry_Object = MibTableRow
agentAutoVoIPSessionEntry = _AgentAutoVoIPSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1)
)
agentAutoVoIPSessionEntry.setIndexNames(
    (0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPSessionIndex"),
)
if mibBuilder.loadTexts:
    agentAutoVoIPSessionEntry.setStatus("current")


class _AgentAutoVoIPSessionIndex_Type(Integer32):
    """Custom type agentAutoVoIPSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AgentAutoVoIPSessionIndex_Type.__name__ = "Integer32"
_AgentAutoVoIPSessionIndex_Object = MibTableColumn
agentAutoVoIPSessionIndex = _AgentAutoVoIPSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 1),
    _AgentAutoVoIPSessionIndex_Type()
)
agentAutoVoIPSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPSessionIndex.setStatus("current")
_AgentAutoVoIPSourceIP_Type = IpAddress
_AgentAutoVoIPSourceIP_Object = MibTableColumn
agentAutoVoIPSourceIP = _AgentAutoVoIPSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 2),
    _AgentAutoVoIPSourceIP_Type()
)
agentAutoVoIPSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPSourceIP.setStatus("current")
_AgentAutoVoIPDestinationIP_Type = IpAddress
_AgentAutoVoIPDestinationIP_Object = MibTableColumn
agentAutoVoIPDestinationIP = _AgentAutoVoIPDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 3),
    _AgentAutoVoIPDestinationIP_Type()
)
agentAutoVoIPDestinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPDestinationIP.setStatus("current")
_AgentAutoVoIPSourceL4Port_Type = Integer32
_AgentAutoVoIPSourceL4Port_Object = MibTableColumn
agentAutoVoIPSourceL4Port = _AgentAutoVoIPSourceL4Port_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 4),
    _AgentAutoVoIPSourceL4Port_Type()
)
agentAutoVoIPSourceL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPSourceL4Port.setStatus("current")
_AgentAutoVoIPDestinationL4Port_Type = Integer32
_AgentAutoVoIPDestinationL4Port_Object = MibTableColumn
agentAutoVoIPDestinationL4Port = _AgentAutoVoIPDestinationL4Port_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 5),
    _AgentAutoVoIPDestinationL4Port_Type()
)
agentAutoVoIPDestinationL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPDestinationL4Port.setStatus("current")
_AgentAutoVoIPProtocol_Type = Integer32
_AgentAutoVoIPProtocol_Object = MibTableColumn
agentAutoVoIPProtocol = _AgentAutoVoIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 6),
    _AgentAutoVoIPProtocol_Type()
)
agentAutoVoIPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-QOS-AUTOVOIP-MIB",
    **{"fastPathQOSAUTOVOIP": fastPathQOSAUTOVOIP,
       "agentAutoVoIPCfgGroup": agentAutoVoIPCfgGroup,
       "agentAutoVoIPVLAN": agentAutoVoIPVLAN,
       "agentAutoVoIPOUIPriority": agentAutoVoIPOUIPriority,
       "agentAutoVoIPProtocolPriScheme": agentAutoVoIPProtocolPriScheme,
       "agentAutoVoIPProtocolTcOrRemarkValue": agentAutoVoIPProtocolTcOrRemarkValue,
       "agentAutoVoIPTable": agentAutoVoIPTable,
       "agentAutoVoIPEntry": agentAutoVoIPEntry,
       "agentAutoVoIPIntfIndex": agentAutoVoIPIntfIndex,
       "agentAutoVoIPProtocolMode": agentAutoVoIPProtocolMode,
       "agentAutoVoIPOUIMode": agentAutoVoIPOUIMode,
       "agentAutoVoIPProtocolPortStatus": agentAutoVoIPProtocolPortStatus,
       "agentAutoVoIPOUIPortStatus": agentAutoVoIPOUIPortStatus,
       "agentAutoVoIPOUITable": agentAutoVoIPOUITable,
       "agentAutoVoIPOUIEntry": agentAutoVoIPOUIEntry,
       "agentAutoVoIPOUIIndex": agentAutoVoIPOUIIndex,
       "agentAutoVoIPOUI": agentAutoVoIPOUI,
       "agentAutoVoIPOUIDesc": agentAutoVoIPOUIDesc,
       "agentAutoVoIPOUIRowStatus": agentAutoVoIPOUIRowStatus,
       "agentAutoVoIPSessionTable": agentAutoVoIPSessionTable,
       "agentAutoVoIPSessionEntry": agentAutoVoIPSessionEntry,
       "agentAutoVoIPSessionIndex": agentAutoVoIPSessionIndex,
       "agentAutoVoIPSourceIP": agentAutoVoIPSourceIP,
       "agentAutoVoIPDestinationIP": agentAutoVoIPDestinationIP,
       "agentAutoVoIPSourceL4Port": agentAutoVoIPSourceL4Port,
       "agentAutoVoIPDestinationL4Port": agentAutoVoIPDestinationL4Port,
       "agentAutoVoIPProtocol": agentAutoVoIPProtocol}
)
