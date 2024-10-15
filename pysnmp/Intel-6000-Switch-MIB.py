# SNMP MIB module (Intel-6000-Switch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Intel-6000-Switch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:30 2024
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

(switch_products,) = mibBuilder.importSymbols(
    "Intel-Common-MIB",
    "switch-products")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortNumber(Integer32):
    """Custom type PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""




class EnableStatus(Integer32):
    """Custom type EnableStatus based on Integer32"""
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





class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel6000Switch_ObjectIdentity = ObjectIdentity
intel6000Switch = _Intel6000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1)
)
_Express6000_ObjectIdentity = ObjectIdentity
express6000 = _Express6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 1)
)
_SwitchMIB_ObjectIdentity = ObjectIdentity
switchMIB = _SwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2)
)
_SwitchConfigGroup_ObjectIdentity = ObjectIdentity
switchConfigGroup = _SwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("mandatory")
_NetMask_Type = IpAddress
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 2),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("mandatory")
_BroadcastAddress_Type = IpAddress
_BroadcastAddress_Object = MibScalar
broadcastAddress = _BroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 4),
    _BroadcastAddress_Type()
)
broadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastAddress.setStatus("mandatory")
_MaxMacAddresses_Type = Integer32
_MaxMacAddresses_Object = MibScalar
maxMacAddresses = _MaxMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 5),
    _MaxMacAddresses_Type()
)
maxMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxMacAddresses.setStatus("mandatory")
_ClearStatistics_Type = Integer32
_ClearStatistics_Object = MibScalar
clearStatistics = _ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 6),
    _ClearStatistics_Type()
)
clearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearStatistics.setStatus("mandatory")
_AgeFilterDatabase_Type = Integer32
_AgeFilterDatabase_Object = MibScalar
ageFilterDatabase = _AgeFilterDatabase_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 7),
    _AgeFilterDatabase_Type()
)
ageFilterDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ageFilterDatabase.setStatus("mandatory")
_EntMibVersion_Type = DisplayString
_EntMibVersion_Object = MibScalar
entMibVersion = _EntMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 8),
    _EntMibVersion_Type()
)
entMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entMibVersion.setStatus("mandatory")


class _TelnetEnable_Type(Integer32):
    """Custom type telnetEnable based on Integer32"""
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


_TelnetEnable_Type.__name__ = "Integer32"
_TelnetEnable_Object = MibScalar
telnetEnable = _TelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 9),
    _TelnetEnable_Type()
)
telnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnable.setStatus("mandatory")


class _SyslogEnable_Type(Integer32):
    """Custom type syslogEnable based on Integer32"""
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


_SyslogEnable_Type.__name__ = "Integer32"
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 10),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("mandatory")
_SyslogIp_Type = IpAddress
_SyslogIp_Object = MibScalar
syslogIp = _SyslogIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 11),
    _SyslogIp_Type()
)
syslogIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogIp.setStatus("mandatory")


class _SyslogCmds_Type(Integer32):
    """Custom type syslogCmds based on Integer32"""
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


_SyslogCmds_Type.__name__ = "Integer32"
_SyslogCmds_Object = MibScalar
syslogCmds = _SyslogCmds_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 12),
    _SyslogCmds_Type()
)
syslogCmds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogCmds.setStatus("mandatory")


class _SyslogOut_Type(Integer32):
    """Custom type syslogOut based on Integer32"""
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


_SyslogOut_Type.__name__ = "Integer32"
_SyslogOut_Object = MibScalar
syslogOut = _SyslogOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 13),
    _SyslogOut_Type()
)
syslogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogOut.setStatus("mandatory")


class _NvramLoadSave_Type(Integer32):
    """Custom type nvramLoadSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("load", 1),
          ("save", 2))
    )


_NvramLoadSave_Type.__name__ = "Integer32"
_NvramLoadSave_Object = MibScalar
nvramLoadSave = _NvramLoadSave_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 14),
    _NvramLoadSave_Type()
)
nvramLoadSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramLoadSave.setStatus("mandatory")


class _NvramLastOpStat_Type(Integer32):
    """Custom type nvramLastOpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadFailed", 2),
          ("noError", 1),
          ("saveFailed", 3))
    )


_NvramLastOpStat_Type.__name__ = "Integer32"
_NvramLastOpStat_Object = MibScalar
nvramLastOpStat = _NvramLastOpStat_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 15),
    _NvramLastOpStat_Type()
)
nvramLastOpStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramLastOpStat.setStatus("mandatory")
_NvramRemoteIp_Type = IpAddress
_NvramRemoteIp_Object = MibScalar
nvramRemoteIp = _NvramRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 16),
    _NvramRemoteIp_Type()
)
nvramRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramRemoteIp.setStatus("mandatory")
_NvramRemotePath_Type = DisplayString
_NvramRemotePath_Object = MibScalar
nvramRemotePath = _NvramRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 1, 17),
    _NvramRemotePath_Type()
)
nvramRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvramRemotePath.setStatus("mandatory")
_MonitorGroup_ObjectIdentity = ObjectIdentity
monitorGroup = _MonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 2)
)


class _DiagnosticsResults_Type(Integer32):
    """Custom type diagnosticsResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("ok", 1),
          ("warnings", 2))
    )


_DiagnosticsResults_Type.__name__ = "Integer32"
_DiagnosticsResults_Object = MibScalar
diagnosticsResults = _DiagnosticsResults_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 2, 1),
    _DiagnosticsResults_Type()
)
diagnosticsResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagnosticsResults.setStatus("mandatory")
_DiagnosticsTime_Type = DisplayString
_DiagnosticsTime_Object = MibScalar
diagnosticsTime = _DiagnosticsTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 2, 2),
    _DiagnosticsTime_Type()
)
diagnosticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagnosticsTime.setStatus("mandatory")


class _LastDiagnosticsTest_Type(Integer32):
    """Custom type lastDiagnosticsTest based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("asicBusRegistersTest", 7),
          ("asicLoopbackTest", 6),
          ("asicRamRegistersTest", 8),
          ("asicRandomFrameTest", 5),
          ("camTest", 3),
          ("duartTest", 10),
          ("flashTest", 2),
          ("memoryTest", 1),
          ("nvramTest", 4),
          ("serialEepromTest", 9))
    )


_LastDiagnosticsTest_Type.__name__ = "Integer32"
_LastDiagnosticsTest_Object = MibScalar
lastDiagnosticsTest = _LastDiagnosticsTest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 2, 3),
    _LastDiagnosticsTest_Type()
)
lastDiagnosticsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastDiagnosticsTest.setStatus("mandatory")
_CommGroup_ObjectIdentity = ObjectIdentity
commGroup = _CommGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3)
)


class _CommNumComms_Type(Integer32):
    """Custom type commNumComms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommNumComms_Type.__name__ = "Integer32"
_CommNumComms_Object = MibScalar
commNumComms = _CommNumComms_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 1),
    _CommNumComms_Type()
)
commNumComms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commNumComms.setStatus("mandatory")
_CommInfoTable_Object = MibTable
commInfoTable = _CommInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    commInfoTable.setStatus("mandatory")
_CommInfoEntry_Object = MibTableRow
commInfoEntry = _CommInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1)
)
commInfoEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "commInfoIndex"),
)
if mibBuilder.loadTexts:
    commInfoEntry.setStatus("mandatory")


class _CommInfoIndex_Type(Integer32):
    """Custom type commInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommInfoIndex_Type.__name__ = "Integer32"
_CommInfoIndex_Object = MibTableColumn
commInfoIndex = _CommInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1, 1),
    _CommInfoIndex_Type()
)
commInfoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoIndex.setStatus("mandatory")
_CommInfoName_Type = DisplayString
_CommInfoName_Object = MibTableColumn
commInfoName = _CommInfoName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1, 2),
    _CommInfoName_Type()
)
commInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoName.setStatus("mandatory")


class _CommInfoGet_Type(Integer32):
    """Custom type commInfoGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CommInfoGet_Type.__name__ = "Integer32"
_CommInfoGet_Object = MibTableColumn
commInfoGet = _CommInfoGet_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1, 3),
    _CommInfoGet_Type()
)
commInfoGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoGet.setStatus("mandatory")


class _CommInfoSet_Type(Integer32):
    """Custom type commInfoSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CommInfoSet_Type.__name__ = "Integer32"
_CommInfoSet_Object = MibTableColumn
commInfoSet = _CommInfoSet_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1, 4),
    _CommInfoSet_Type()
)
commInfoSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoSet.setStatus("mandatory")


class _CommInfoTrap_Type(Integer32):
    """Custom type commInfoTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CommInfoTrap_Type.__name__ = "Integer32"
_CommInfoTrap_Object = MibTableColumn
commInfoTrap = _CommInfoTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 2, 1, 5),
    _CommInfoTrap_Type()
)
commInfoTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoTrap.setStatus("mandatory")


class _CommAltTrapPort_Type(Integer32):
    """Custom type commAltTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 9000),
    )


_CommAltTrapPort_Type.__name__ = "Integer32"
_CommAltTrapPort_Object = MibScalar
commAltTrapPort = _CommAltTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 3),
    _CommAltTrapPort_Type()
)
commAltTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commAltTrapPort.setStatus("mandatory")


class _CommSnmpSecurityLevel_Type(Integer32):
    """Custom type commSnmpSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CommSnmpSecurityLevel_Type.__name__ = "Integer32"
_CommSnmpSecurityLevel_Object = MibScalar
commSnmpSecurityLevel = _CommSnmpSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 3, 4),
    _CommSnmpSecurityLevel_Type()
)
commSnmpSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSnmpSecurityLevel.setStatus("mandatory")
_HostGroup_ObjectIdentity = ObjectIdentity
hostGroup = _HostGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4)
)


class _HostNumHosts_Type(Integer32):
    """Custom type hostNumHosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostNumHosts_Type.__name__ = "Integer32"
_HostNumHosts_Object = MibScalar
hostNumHosts = _HostNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 1),
    _HostNumHosts_Type()
)
hostNumHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostNumHosts.setStatus("mandatory")
_HostInfoTable_Object = MibTable
hostInfoTable = _HostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hostInfoTable.setStatus("mandatory")
_HostInfoEntry_Object = MibTableRow
hostInfoEntry = _HostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2, 1)
)
hostInfoEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "hostInfoIndex"),
)
if mibBuilder.loadTexts:
    hostInfoEntry.setStatus("mandatory")


class _HostInfoIndex_Type(Integer32):
    """Custom type hostInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostInfoIndex_Type.__name__ = "Integer32"
_HostInfoIndex_Object = MibTableColumn
hostInfoIndex = _HostInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2, 1, 1),
    _HostInfoIndex_Type()
)
hostInfoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoIndex.setStatus("mandatory")
_HostInfoName_Type = DisplayString
_HostInfoName_Object = MibTableColumn
hostInfoName = _HostInfoName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2, 1, 2),
    _HostInfoName_Type()
)
hostInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoName.setStatus("mandatory")
_HostInfoIp_Type = IpAddress
_HostInfoIp_Object = MibTableColumn
hostInfoIp = _HostInfoIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2, 1, 3),
    _HostInfoIp_Type()
)
hostInfoIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoIp.setStatus("mandatory")
_HostInfoComm_Type = DisplayString
_HostInfoComm_Object = MibTableColumn
hostInfoComm = _HostInfoComm_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 4, 2, 1, 4),
    _HostInfoComm_Type()
)
hostInfoComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoComm.setStatus("mandatory")
_SerialGroup_ObjectIdentity = ObjectIdentity
serialGroup = _SerialGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 5)
)


class _SerialBaudRate_Type(Integer32):
    """Custom type serialBaudRate based on Integer32"""
    defaultValue = 5

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
        *(("baud1200", 2),
          ("baud19200", 6),
          ("baud2400", 3),
          ("baud38400", 7),
          ("baud4800", 4),
          ("baud600", 1),
          ("baud9600", 5))
    )


_SerialBaudRate_Type.__name__ = "Integer32"
_SerialBaudRate_Object = MibScalar
serialBaudRate = _SerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 5, 1),
    _SerialBaudRate_Type()
)
serialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBaudRate.setStatus("mandatory")


class _ModemControlLines_Type(Integer32):
    """Custom type modemControlLines based on Integer32"""
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


_ModemControlLines_Type.__name__ = "Integer32"
_ModemControlLines_Object = MibScalar
modemControlLines = _ModemControlLines_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 5, 2),
    _ModemControlLines_Type()
)
modemControlLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemControlLines.setStatus("mandatory")
_SpanGroup_ObjectIdentity = ObjectIdentity
spanGroup = _SpanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9)
)


class _SpanOnOff_Type(Integer32):
    """Custom type spanOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SpanOnOff_Type.__name__ = "Integer32"
_SpanOnOff_Object = MibScalar
spanOnOff = _SpanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 1),
    _SpanOnOff_Type()
)
spanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanOnOff.setStatus("mandatory")


class _SpanType_Type(Integer32):
    """Custom type spanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvstp", 2),
          ("single", 1))
    )


_SpanType_Type.__name__ = "Integer32"
_SpanType_Object = MibScalar
spanType = _SpanType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 2),
    _SpanType_Type()
)
spanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanType.setStatus("mandatory")


class _SpanResetDefaults_Type(Integer32):
    """Custom type spanResetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_SpanResetDefaults_Type.__name__ = "Integer32"
_SpanResetDefaults_Object = MibScalar
spanResetDefaults = _SpanResetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 4),
    _SpanResetDefaults_Type()
)
spanResetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanResetDefaults.setStatus("mandatory")


class _SpanRapid_Type(Integer32):
    """Custom type spanRapid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SpanRapid_Type.__name__ = "Integer32"
_SpanRapid_Object = MibScalar
spanRapid = _SpanRapid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 5),
    _SpanRapid_Type()
)
spanRapid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanRapid.setStatus("mandatory")
_SpanPortTable_Object = MibTable
spanPortTable = _SpanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    spanPortTable.setStatus("mandatory")
_SpanPortEntry_Object = MibTableRow
spanPortEntry = _SpanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 6, 1)
)
spanPortEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "spanPortPort"),
)
if mibBuilder.loadTexts:
    spanPortEntry.setStatus("mandatory")
_SpanPortPort_Type = PortNumber
_SpanPortPort_Object = MibTableColumn
spanPortPort = _SpanPortPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 6, 1, 1),
    _SpanPortPort_Type()
)
spanPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanPortPort.setStatus("mandatory")
_SpanPortQuickStatus_Type = EnableStatus
_SpanPortQuickStatus_Object = MibTableColumn
spanPortQuickStatus = _SpanPortQuickStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 6, 1, 2),
    _SpanPortQuickStatus_Type()
)
spanPortQuickStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanPortQuickStatus.setStatus("mandatory")


class _SpanPortAuto_Type(Integer32):
    """Custom type spanPortAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("fixed", 1))
    )


_SpanPortAuto_Type.__name__ = "Integer32"
_SpanPortAuto_Object = MibTableColumn
spanPortAuto = _SpanPortAuto_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 9, 6, 1, 3),
    _SpanPortAuto_Type()
)
spanPortAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanPortAuto.setStatus("mandatory")
_FanGroup_ObjectIdentity = ObjectIdentity
fanGroup = _FanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10)
)


class _FanNumFans_Type(Integer32):
    """Custom type fanNumFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FanNumFans_Type.__name__ = "Integer32"
_FanNumFans_Object = MibScalar
fanNumFans = _FanNumFans_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10, 1),
    _FanNumFans_Type()
)
fanNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumFans.setStatus("mandatory")
_FanInfoTable_Object = MibTable
fanInfoTable = _FanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    fanInfoTable.setStatus("mandatory")
_FanInfoEntry_Object = MibTableRow
fanInfoEntry = _FanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10, 2, 1)
)
fanInfoEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanInfoEntry.setStatus("mandatory")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nok", 2),
          ("ok", 1))
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 10, 2, 1, 2),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanStatus.setStatus("mandatory")
_PsGroup_ObjectIdentity = ObjectIdentity
psGroup = _PsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11)
)


class _PsNumber_Type(Integer32):
    """Custom type psNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PsNumber_Type.__name__ = "Integer32"
_PsNumber_Object = MibScalar
psNumber = _PsNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 1),
    _PsNumber_Type()
)
psNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNumber.setStatus("mandatory")
_PsInfoTable_Object = MibTable
psInfoTable = _PsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    psInfoTable.setStatus("mandatory")
_PsInfoEntry_Object = MibTableRow
psInfoEntry = _PsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 2, 1)
)
psInfoEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "psIndex"),
)
if mibBuilder.loadTexts:
    psInfoEntry.setStatus("mandatory")


class _PsIndex_Type(Integer32):
    """Custom type psIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("c", 3))
    )


_PsIndex_Type.__name__ = "Integer32"
_PsIndex_Object = MibTableColumn
psIndex = _PsIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 2, 1, 1),
    _PsIndex_Type()
)
psIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIndex.setStatus("mandatory")


class _PsPresent_Type(Integer32):
    """Custom type psPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("uninstalled", 2))
    )


_PsPresent_Type.__name__ = "Integer32"
_PsPresent_Object = MibTableColumn
psPresent = _PsPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 2, 1, 2),
    _PsPresent_Type()
)
psPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPresent.setStatus("mandatory")


class _PsStatus_Type(Integer32):
    """Custom type psStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nok", 2),
          ("ok", 1))
    )


_PsStatus_Type.__name__ = "Integer32"
_PsStatus_Object = MibTableColumn
psStatus = _PsStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 11, 2, 1, 3),
    _PsStatus_Type()
)
psStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatus.setStatus("mandatory")
_TempGroup_ObjectIdentity = ObjectIdentity
tempGroup = _TempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13)
)
_TempCurrent_Type = Integer32
_TempCurrent_Object = MibScalar
tempCurrent = _TempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13, 1),
    _TempCurrent_Type()
)
tempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurrent.setStatus("mandatory")


class _TempAlarm_Type(Integer32):
    """Custom type tempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TempAlarm_Type.__name__ = "Integer32"
_TempAlarm_Object = MibScalar
tempAlarm = _TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13, 2),
    _TempAlarm_Type()
)
tempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm.setStatus("mandatory")
_TempHighest_Type = Integer32
_TempHighest_Object = MibScalar
tempHighest = _TempHighest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13, 3),
    _TempHighest_Type()
)
tempHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighest.setStatus("mandatory")
_TempHigh_Type = Integer32
_TempHigh_Object = MibScalar
tempHigh = _TempHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13, 4),
    _TempHigh_Type()
)
tempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHigh.setStatus("mandatory")
_TempLow_Type = Integer32
_TempLow_Object = MibScalar
tempLow = _TempLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 13, 5),
    _TempLow_Type()
)
tempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLow.setStatus("mandatory")
_GigabitGroup_ObjectIdentity = ObjectIdentity
gigabitGroup = _GigabitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14)
)
_GigabitPortTable_Object = MibTable
gigabitPortTable = _GigabitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gigabitPortTable.setStatus("mandatory")
_GigabitPortTableEntry_Object = MibTableRow
gigabitPortTableEntry = _GigabitPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2, 1)
)
gigabitPortTableEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "gigabitPortTableSlot"),
    (0, "Intel-6000-Switch-MIB", "gigabitPortTablePort"),
)
if mibBuilder.loadTexts:
    gigabitPortTableEntry.setStatus("mandatory")


class _GigabitPortTableSlot_Type(Integer32):
    """Custom type gigabitPortTableSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GigabitPortTableSlot_Type.__name__ = "Integer32"
_GigabitPortTableSlot_Object = MibTableColumn
gigabitPortTableSlot = _GigabitPortTableSlot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2, 1, 1),
    _GigabitPortTableSlot_Type()
)
gigabitPortTableSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigabitPortTableSlot.setStatus("mandatory")


class _GigabitPortTablePort_Type(Integer32):
    """Custom type gigabitPortTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_GigabitPortTablePort_Type.__name__ = "Integer32"
_GigabitPortTablePort_Object = MibTableColumn
gigabitPortTablePort = _GigabitPortTablePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2, 1, 2),
    _GigabitPortTablePort_Type()
)
gigabitPortTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigabitPortTablePort.setStatus("mandatory")


class _GigabitPortTableLinkState_Type(Integer32):
    """Custom type gigabitPortTableLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_GigabitPortTableLinkState_Type.__name__ = "Integer32"
_GigabitPortTableLinkState_Object = MibTableColumn
gigabitPortTableLinkState = _GigabitPortTableLinkState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2, 1, 4),
    _GigabitPortTableLinkState_Type()
)
gigabitPortTableLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigabitPortTableLinkState.setStatus("mandatory")


class _GigabitPortTablePortAutoNeg_Type(Integer32):
    """Custom type gigabitPortTablePortAutoNeg based on Integer32"""
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


_GigabitPortTablePortAutoNeg_Type.__name__ = "Integer32"
_GigabitPortTablePortAutoNeg_Object = MibTableColumn
gigabitPortTablePortAutoNeg = _GigabitPortTablePortAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 14, 2, 1, 5),
    _GigabitPortTablePortAutoNeg_Type()
)
gigabitPortTablePortAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gigabitPortTablePortAutoNeg.setStatus("mandatory")
_TenHundredGroup_ObjectIdentity = ObjectIdentity
tenHundredGroup = _TenHundredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15)
)
_TenHundredPortTable_Object = MibTable
tenHundredPortTable = _TenHundredPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    tenHundredPortTable.setStatus("mandatory")
_TenHundredPortTableEntry_Object = MibTableRow
tenHundredPortTableEntry = _TenHundredPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1, 1)
)
tenHundredPortTableEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "tenHundredPortTableSlot"),
    (0, "Intel-6000-Switch-MIB", "tenHundredPortTablePort"),
)
if mibBuilder.loadTexts:
    tenHundredPortTableEntry.setStatus("mandatory")


class _TenHundredPortTableSlot_Type(Integer32):
    """Custom type tenHundredPortTableSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TenHundredPortTableSlot_Type.__name__ = "Integer32"
_TenHundredPortTableSlot_Object = MibTableColumn
tenHundredPortTableSlot = _TenHundredPortTableSlot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1, 1, 1),
    _TenHundredPortTableSlot_Type()
)
tenHundredPortTableSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenHundredPortTableSlot.setStatus("mandatory")


class _TenHundredPortTablePort_Type(Integer32):
    """Custom type tenHundredPortTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TenHundredPortTablePort_Type.__name__ = "Integer32"
_TenHundredPortTablePort_Object = MibTableColumn
tenHundredPortTablePort = _TenHundredPortTablePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1, 1, 2),
    _TenHundredPortTablePort_Type()
)
tenHundredPortTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenHundredPortTablePort.setStatus("mandatory")


class _TenHundredPortTableLinkState_Type(Integer32):
    """Custom type tenHundredPortTableLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TenHundredPortTableLinkState_Type.__name__ = "Integer32"
_TenHundredPortTableLinkState_Object = MibTableColumn
tenHundredPortTableLinkState = _TenHundredPortTableLinkState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1, 1, 3),
    _TenHundredPortTableLinkState_Type()
)
tenHundredPortTableLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenHundredPortTableLinkState.setStatus("mandatory")


class _TenHundredPortTableConfig_Type(Integer32):
    """Custom type tenHundredPortTableConfig based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("autoHundredFull", 5),
          ("autoHundredHalf", 2),
          ("autoHundredHalfFull", 8),
          ("autoTenFull", 4),
          ("autoTenHalf", 1),
          ("autoTenHalfFull", 7),
          ("autoTenHundredFull", 6),
          ("autoTenHundredHalf", 3),
          ("autoTenHundredHalfFull", 9),
          ("hundredFull", 13),
          ("hundredHalf", 11),
          ("tenFull", 12),
          ("tenHalf", 10),
          ("unknown", 20))
    )


_TenHundredPortTableConfig_Type.__name__ = "Integer32"
_TenHundredPortTableConfig_Object = MibTableColumn
tenHundredPortTableConfig = _TenHundredPortTableConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 15, 1, 1, 4),
    _TenHundredPortTableConfig_Type()
)
tenHundredPortTableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tenHundredPortTableConfig.setStatus("mandatory")
_VlanGroup_ObjectIdentity = ObjectIdentity
vlanGroup = _VlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16)
)


class _VlanValid_Type(Integer32):
    """Custom type vlanValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_VlanValid_Type.__name__ = "Integer32"
_VlanValid_Object = MibScalar
vlanValid = _VlanValid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 1),
    _VlanValid_Type()
)
vlanValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanValid.setStatus("mandatory")
_VlanConfigTable_Object = MibTable
vlanConfigTable = _VlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    vlanConfigTable.setStatus("mandatory")
_VlanConfigEntry_Object = MibTableRow
vlanConfigEntry = _VlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1)
)
vlanConfigEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "vlanConfigVID"),
)
if mibBuilder.loadTexts:
    vlanConfigEntry.setStatus("mandatory")
_VlanConfigVID_Type = VlanId
_VlanConfigVID_Object = MibTableColumn
vlanConfigVID = _VlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 1),
    _VlanConfigVID_Type()
)
vlanConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanConfigVID.setStatus("mandatory")
_VlanConfigName_Type = DisplayString
_VlanConfigName_Object = MibTableColumn
vlanConfigName = _VlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 2),
    _VlanConfigName_Type()
)
vlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanConfigName.setStatus("mandatory")
_VlanConfigIpAddr_Type = IpAddress
_VlanConfigIpAddr_Object = MibTableColumn
vlanConfigIpAddr = _VlanConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 3),
    _VlanConfigIpAddr_Type()
)
vlanConfigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanConfigIpAddr.setStatus("mandatory")
_VlanConfigNetmask_Type = IpAddress
_VlanConfigNetmask_Object = MibTableColumn
vlanConfigNetmask = _VlanConfigNetmask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 4),
    _VlanConfigNetmask_Type()
)
vlanConfigNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanConfigNetmask.setStatus("mandatory")
_VlanConfigBroadcast_Type = IpAddress
_VlanConfigBroadcast_Object = MibTableColumn
vlanConfigBroadcast = _VlanConfigBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 5),
    _VlanConfigBroadcast_Type()
)
vlanConfigBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanConfigBroadcast.setStatus("mandatory")
_VlanConfigRouting_Type = EnableStatus
_VlanConfigRouting_Object = MibTableColumn
vlanConfigRouting = _VlanConfigRouting_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 2, 1, 6),
    _VlanConfigRouting_Type()
)
vlanConfigRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanConfigRouting.setStatus("mandatory")


class _VlanReset_Type(Integer32):
    """Custom type vlanReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_VlanReset_Type.__name__ = "Integer32"
_VlanReset_Object = MibScalar
vlanReset = _VlanReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 3),
    _VlanReset_Type()
)
vlanReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanReset.setStatus("mandatory")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("mandatory")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 4, 1)
)
vlanPortEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "vlanPortNumber"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("mandatory")
_VlanPortNumber_Type = PortNumber
_VlanPortNumber_Object = MibTableColumn
vlanPortNumber = _VlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 4, 1, 1),
    _VlanPortNumber_Type()
)
vlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortNumber.setStatus("mandatory")
_VlanPortTrustedVid_Type = Boolean
_VlanPortTrustedVid_Object = MibTableColumn
vlanPortTrustedVid = _VlanPortTrustedVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 4, 1, 2),
    _VlanPortTrustedVid_Type()
)
vlanPortTrustedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortTrustedVid.setStatus("mandatory")
_VlanPortTrustedPriority_Type = Boolean
_VlanPortTrustedPriority_Object = MibTableColumn
vlanPortTrustedPriority = _VlanPortTrustedPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 16, 4, 1, 3),
    _VlanPortTrustedPriority_Type()
)
vlanPortTrustedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortTrustedPriority.setStatus("mandatory")
_RoutingGroup_ObjectIdentity = ObjectIdentity
routingGroup = _RoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17)
)
_RoutingRouterId_Type = IpAddress
_RoutingRouterId_Object = MibScalar
routingRouterId = _RoutingRouterId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 1),
    _RoutingRouterId_Type()
)
routingRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRouterId.setStatus("mandatory")


class _RoutingScanInterval_Type(Integer32):
    """Custom type routingScanInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3600),
    )


_RoutingScanInterval_Type.__name__ = "Integer32"
_RoutingScanInterval_Object = MibScalar
routingScanInterval = _RoutingScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 2),
    _RoutingScanInterval_Type()
)
routingScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingScanInterval.setStatus("mandatory")
_RoutingConfigGroup_ObjectIdentity = ObjectIdentity
routingConfigGroup = _RoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 3)
)


class _RoutingEnable_Type(Integer32):
    """Custom type routingEnable based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enableInit", 3),
          ("enableRestore", 4),
          ("enabled", 1))
    )


_RoutingEnable_Type.__name__ = "Integer32"
_RoutingEnable_Object = MibScalar
routingEnable = _RoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 3, 1),
    _RoutingEnable_Type()
)
routingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingEnable.setStatus("mandatory")


class _RoutingRipConf_Type(Integer32):
    """Custom type routingRipConf based on Integer32"""
    defaultValue = 2

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


_RoutingRipConf_Type.__name__ = "Integer32"
_RoutingRipConf_Object = MibScalar
routingRipConf = _RoutingRipConf_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 3, 2),
    _RoutingRipConf_Type()
)
routingRipConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRipConf.setStatus("mandatory")


class _RoutingOspfConf_Type(Integer32):
    """Custom type routingOspfConf based on Integer32"""
    defaultValue = 2

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


_RoutingOspfConf_Type.__name__ = "Integer32"
_RoutingOspfConf_Object = MibScalar
routingOspfConf = _RoutingOspfConf_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 3, 3),
    _RoutingOspfConf_Type()
)
routingOspfConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingOspfConf.setStatus("mandatory")
_RoutingPreferencesGroup_ObjectIdentity = ObjectIdentity
routingPreferencesGroup = _RoutingPreferencesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 4)
)


class _RoutingOspfPref_Type(Integer32):
    """Custom type routingOspfPref based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoutingOspfPref_Type.__name__ = "Integer32"
_RoutingOspfPref_Object = MibScalar
routingOspfPref = _RoutingOspfPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 4, 1),
    _RoutingOspfPref_Type()
)
routingOspfPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingOspfPref.setStatus("mandatory")


class _RoutingStaticConfigPref_Type(Integer32):
    """Custom type routingStaticConfigPref based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoutingStaticConfigPref_Type.__name__ = "Integer32"
_RoutingStaticConfigPref_Object = MibScalar
routingStaticConfigPref = _RoutingStaticConfigPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 4, 2),
    _RoutingStaticConfigPref_Type()
)
routingStaticConfigPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingStaticConfigPref.setStatus("mandatory")


class _RoutingRipPref_Type(Integer32):
    """Custom type routingRipPref based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoutingRipPref_Type.__name__ = "Integer32"
_RoutingRipPref_Object = MibScalar
routingRipPref = _RoutingRipPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 4, 3),
    _RoutingRipPref_Type()
)
routingRipPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRipPref.setStatus("mandatory")


class _RoutingOspfAsExtPref_Type(Integer32):
    """Custom type routingOspfAsExtPref based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoutingOspfAsExtPref_Type.__name__ = "Integer32"
_RoutingOspfAsExtPref_Object = MibScalar
routingOspfAsExtPref = _RoutingOspfAsExtPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 4, 4),
    _RoutingOspfAsExtPref_Type()
)
routingOspfAsExtPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingOspfAsExtPref.setStatus("mandatory")
_RoutingIfPrefTable_Object = MibTable
routingIfPrefTable = _RoutingIfPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    routingIfPrefTable.setStatus("mandatory")
_RoutingIfPrefEntry_Object = MibTableRow
routingIfPrefEntry = _RoutingIfPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 5, 1)
)
routingIfPrefEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "routingIfPrefAddress"),
)
if mibBuilder.loadTexts:
    routingIfPrefEntry.setStatus("mandatory")
_RoutingIfPrefAddress_Type = IpAddress
_RoutingIfPrefAddress_Object = MibTableColumn
routingIfPrefAddress = _RoutingIfPrefAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 5, 1, 1),
    _RoutingIfPrefAddress_Type()
)
routingIfPrefAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingIfPrefAddress.setStatus("mandatory")


class _RoutingIfPref_Type(Integer32):
    """Custom type routingIfPref based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RoutingIfPref_Type.__name__ = "Integer32"
_RoutingIfPref_Object = MibTableColumn
routingIfPref = _RoutingIfPref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 5, 1, 2),
    _RoutingIfPref_Type()
)
routingIfPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingIfPref.setStatus("mandatory")
_StaticRouteNumber_Type = Gauge32
_StaticRouteNumber_Object = MibScalar
staticRouteNumber = _StaticRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 6),
    _StaticRouteNumber_Type()
)
staticRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteNumber.setStatus("mandatory")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("mandatory")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1)
)
staticRouteEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "staticRouteDest"),
    (0, "Intel-6000-Switch-MIB", "staticRouteMask"),
    (0, "Intel-6000-Switch-MIB", "staticRouteNextHop"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("mandatory")
_StaticRouteDest_Type = IpAddress
_StaticRouteDest_Object = MibTableColumn
staticRouteDest = _StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 1),
    _StaticRouteDest_Type()
)
staticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteDest.setStatus("mandatory")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 2),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("mandatory")
_StaticRouteNextHop_Type = IpAddress
_StaticRouteNextHop_Object = MibTableColumn
staticRouteNextHop = _StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 3),
    _StaticRouteNextHop_Type()
)
staticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteNextHop.setStatus("mandatory")


class _StaticRouteIf_Type(IpAddress):
    """Custom type staticRouteIf based on IpAddress"""
    defaultValue = 0


_StaticRouteIf_Object = MibTableColumn
staticRouteIf = _StaticRouteIf_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 4),
    _StaticRouteIf_Type()
)
staticRouteIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteIf.setStatus("mandatory")


class _StaticRoutePref_Type(Integer32):
    """Custom type staticRoutePref based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StaticRoutePref_Type.__name__ = "Integer32"
_StaticRoutePref_Object = MibTableColumn
staticRoutePref = _StaticRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 5),
    _StaticRoutePref_Type()
)
staticRoutePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutePref.setStatus("mandatory")


class _StaticRouteType_Type(Integer32):
    """Custom type staticRouteType based on Integer32"""
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
        *(("blackhole", 3),
          ("normal", 5),
          ("notinstall", 4),
          ("reject", 2),
          ("retain", 1))
    )


_StaticRouteType_Type.__name__ = "Integer32"
_StaticRouteType_Object = MibTableColumn
staticRouteType = _StaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 6),
    _StaticRouteType_Type()
)
staticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteType.setStatus("mandatory")
_StaticRouteStatus_Type = Integer32
_StaticRouteStatus_Object = MibTableColumn
staticRouteStatus = _StaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 7, 1, 7),
    _StaticRouteStatus_Type()
)
staticRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStatus.setStatus("mandatory")


class _RoutingSaveConfig_Type(Integer32):
    """Custom type routingSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_RoutingSaveConfig_Type.__name__ = "Integer32"
_RoutingSaveConfig_Object = MibScalar
routingSaveConfig = _RoutingSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 17, 8),
    _RoutingSaveConfig_Type()
)
routingSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingSaveConfig.setStatus("mandatory")
_ErrorGroup_ObjectIdentity = ObjectIdentity
errorGroup = _ErrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18)
)
_ErrorTable_Object = MibTable
errorTable = _ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    errorTable.setStatus("mandatory")
_ErrorEntry_Object = MibTableRow
errorEntry = _ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1, 1)
)
errorEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "errorIndex"),
)
if mibBuilder.loadTexts:
    errorEntry.setStatus("mandatory")


class _ErrorIndex_Type(Integer32):
    """Custom type errorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ErrorIndex_Type.__name__ = "Integer32"
_ErrorIndex_Object = MibTableColumn
errorIndex = _ErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1, 1, 1),
    _ErrorIndex_Type()
)
errorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorIndex.setStatus("mandatory")
_ErrorMsg_Type = DisplayString
_ErrorMsg_Object = MibTableColumn
errorMsg = _ErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1, 1, 2),
    _ErrorMsg_Type()
)
errorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMsg.setStatus("mandatory")
_ErrorOid_Type = ObjectIdentifier
_ErrorOid_Object = MibTableColumn
errorOid = _ErrorOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1, 1, 3),
    _ErrorOid_Type()
)
errorOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorOid.setStatus("mandatory")
_ErrorTime_Type = TimeTicks
_ErrorTime_Object = MibTableColumn
errorTime = _ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 1, 1, 4),
    _ErrorTime_Type()
)
errorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorTime.setStatus("mandatory")


class _ClearErrorTable_Type(Integer32):
    """Custom type clearErrorTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ClearErrorTable_Type.__name__ = "Integer32"
_ClearErrorTable_Object = MibScalar
clearErrorTable = _ClearErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 18, 2),
    _ClearErrorTable_Type()
)
clearErrorTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearErrorTable.setStatus("mandatory")
_LinkStateGroup_ObjectIdentity = ObjectIdentity
linkStateGroup = _LinkStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19)
)
_LinkStateTable_Object = MibTable
linkStateTable = _LinkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    linkStateTable.setStatus("mandatory")
_LinkStateEntry_Object = MibTableRow
linkStateEntry = _LinkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1, 1)
)
linkStateEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "linkStateSlot"),
    (0, "Intel-6000-Switch-MIB", "linkStatePort"),
)
if mibBuilder.loadTexts:
    linkStateEntry.setStatus("mandatory")


class _LinkStateSlot_Type(Integer32):
    """Custom type linkStateSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkStateSlot_Type.__name__ = "Integer32"
_LinkStateSlot_Object = MibTableColumn
linkStateSlot = _LinkStateSlot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1, 1, 1),
    _LinkStateSlot_Type()
)
linkStateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStateSlot.setStatus("mandatory")


class _LinkStatePort_Type(Integer32):
    """Custom type linkStatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_LinkStatePort_Type.__name__ = "Integer32"
_LinkStatePort_Object = MibTableColumn
linkStatePort = _LinkStatePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1, 1, 2),
    _LinkStatePort_Type()
)
linkStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatePort.setStatus("mandatory")


class _LinkStateState_Type(Integer32):
    """Custom type linkStateState based on Integer32"""
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
        *(("ethernet-down", 8),
          ("ethernet-up", 7),
          ("fddi-active", 4),
          ("fddi-connecting", 2),
          ("fddi-disabled", 1),
          ("fddi-standby", 3),
          ("reserved1", 5),
          ("reserved2", 6))
    )


_LinkStateState_Type.__name__ = "Integer32"
_LinkStateState_Object = MibTableColumn
linkStateState = _LinkStateState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1, 1, 3),
    _LinkStateState_Type()
)
linkStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStateState.setStatus("mandatory")
_LinkStateTime_Type = TimeTicks
_LinkStateTime_Object = MibTableColumn
linkStateTime = _LinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 19, 1, 1, 4),
    _LinkStateTime_Type()
)
linkStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStateTime.setStatus("mandatory")
_CarrierGroup_ObjectIdentity = ObjectIdentity
carrierGroup = _CarrierGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 20)
)


class _CarrierCPSlotID_Type(Integer32):
    """Custom type carrierCPSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpA", 1),
          ("cpB", 2))
    )


_CarrierCPSlotID_Type.__name__ = "Integer32"
_CarrierCPSlotID_Object = MibScalar
carrierCPSlotID = _CarrierCPSlotID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 20, 1),
    _CarrierCPSlotID_Type()
)
carrierCPSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCPSlotID.setStatus("mandatory")


class _CarrierStatusA_Type(Integer32):
    """Custom type carrierStatusA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insertedNotRunning", 2),
          ("insertedRunning", 3),
          ("notInserted", 1))
    )


_CarrierStatusA_Type.__name__ = "Integer32"
_CarrierStatusA_Object = MibScalar
carrierStatusA = _CarrierStatusA_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 20, 2),
    _CarrierStatusA_Type()
)
carrierStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierStatusA.setStatus("mandatory")


class _CarrierStatusB_Type(Integer32):
    """Custom type carrierStatusB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insertedNotRunning", 2),
          ("insertedRunning", 3),
          ("notInserted", 1))
    )


_CarrierStatusB_Type.__name__ = "Integer32"
_CarrierStatusB_Object = MibScalar
carrierStatusB = _CarrierStatusB_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 20, 3),
    _CarrierStatusB_Type()
)
carrierStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierStatusB.setStatus("mandatory")
_ModuleGroup_ObjectIdentity = ObjectIdentity
moduleGroup = _ModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "moduleSlotNum"),
    (0, "Intel-6000-Switch-MIB", "moduleCard"),
    (0, "Intel-6000-Switch-MIB", "moduleContent"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")


class _ModuleSlotNum_Type(Integer32):
    """Custom type moduleSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ModuleSlotNum_Type.__name__ = "Integer32"
_ModuleSlotNum_Object = MibTableColumn
moduleSlotNum = _ModuleSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1, 1),
    _ModuleSlotNum_Type()
)
moduleSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSlotNum.setStatus("mandatory")


class _ModuleCard_Type(Integer32):
    """Custom type moduleCard based on Integer32"""
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
        *(("carrier", 3),
          ("cpA", 4),
          ("cpB", 5),
          ("empty", 2),
          ("gigSwitch8", 6),
          ("hundredFX12", 8),
          ("tenHundred24", 7),
          ("unknown", 1))
    )


_ModuleCard_Type.__name__ = "Integer32"
_ModuleCard_Object = MibTableColumn
moduleCard = _ModuleCard_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1, 2),
    _ModuleCard_Type()
)
moduleCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCard.setStatus("mandatory")


class _ModuleContent_Type(Integer32):
    """Custom type moduleContent based on Integer32"""
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
        *(("bctXilinx", 4),
          ("bootVersion", 2),
          ("carrierLue", 8),
          ("ccXilinx", 5),
          ("cfgPld", 12),
          ("connectorType", 32),
          ("cpCtrlXilinx", 11),
          ("cpSCtrlXilinx", 10),
          ("feature", 28),
          ("hwRev", 24),
          ("i8051", 6),
          ("imp", 18),
          ("lxa", 16),
          ("mac", 23),
          ("mediaType", 31),
          ("mfgDate", 26),
          ("model", 25),
          ("moduleName", 30),
          ("moduleStatus", 29),
          ("rqm", 14),
          ("serialNum", 22),
          ("sysImage", 7),
          ("sysVersion", 1),
          ("tqmCtl", 20),
          ("tqmFbc", 21),
          ("tqmPl", 19),
          ("tsunami", 33),
          ("twister", 34),
          ("upIf", 13),
          ("variance", 27),
          ("webImage", 9),
          ("xBar", 17),
          ("xilinxVclue", 3),
          ("xpt", 15))
    )


_ModuleContent_Type.__name__ = "Integer32"
_ModuleContent_Object = MibTableColumn
moduleContent = _ModuleContent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1, 3),
    _ModuleContent_Type()
)
moduleContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleContent.setStatus("mandatory")


class _ModuleDataValid_Type(Integer32):
    """Custom type moduleDataValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_ModuleDataValid_Type.__name__ = "Integer32"
_ModuleDataValid_Object = MibTableColumn
moduleDataValid = _ModuleDataValid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1, 4),
    _ModuleDataValid_Type()
)
moduleDataValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDataValid.setStatus("mandatory")
_ModuleText_Type = DisplayString
_ModuleText_Object = MibTableColumn
moduleText = _ModuleText_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 21, 1, 1, 5),
    _ModuleText_Type()
)
moduleText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleText.setStatus("mandatory")
_PingGroup_ObjectIdentity = ObjectIdentity
pingGroup = _PingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 22)
)
_PingHostAddress_Type = DisplayString
_PingHostAddress_Object = MibScalar
pingHostAddress = _PingHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 22, 1),
    _PingHostAddress_Type()
)
pingHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingHostAddress.setStatus("mandatory")
_PingRequest_Type = Integer32
_PingRequest_Object = MibScalar
pingRequest = _PingRequest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 22, 2),
    _PingRequest_Type()
)
pingRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingRequest.setStatus("mandatory")
_PingTime_Type = Integer32
_PingTime_Object = MibScalar
pingTime = _PingTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 22, 3),
    _PingTime_Type()
)
pingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingTime.setStatus("mandatory")


class _PingStatus_Type(Integer32):
    """Custom type pingStatus based on Integer32"""
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
        *(("error", 5),
          ("noData", 1),
          ("success", 4),
          ("timedOut", 3),
          ("waitingForReply", 2))
    )


_PingStatus_Type.__name__ = "Integer32"
_PingStatus_Object = MibScalar
pingStatus = _PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 22, 4),
    _PingStatus_Type()
)
pingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingStatus.setStatus("mandatory")
_DnsGroup_ObjectIdentity = ObjectIdentity
dnsGroup = _DnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 23)
)


class _DnsEnable_Type(Integer32):
    """Custom type dnsEnable based on Integer32"""
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


_DnsEnable_Type.__name__ = "Integer32"
_DnsEnable_Object = MibScalar
dnsEnable = _DnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 23, 1),
    _DnsEnable_Type()
)
dnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsEnable.setStatus("mandatory")
_DnsDomainName_Type = DisplayString
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 23, 2),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("mandatory")
_DnsPrimaryServer_Type = DisplayString
_DnsPrimaryServer_Object = MibScalar
dnsPrimaryServer = _DnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 23, 3),
    _DnsPrimaryServer_Type()
)
dnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsPrimaryServer.setStatus("mandatory")
_DnsBackupServer_Type = DisplayString
_DnsBackupServer_Object = MibScalar
dnsBackupServer = _DnsBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 23, 4),
    _DnsBackupServer_Type()
)
dnsBackupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsBackupServer.setStatus("mandatory")
_StormControlGroup_ObjectIdentity = ObjectIdentity
stormControlGroup = _StormControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24)
)
_StormBcastControlTable_Object = MibTable
stormBcastControlTable = _StormBcastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1)
)
if mibBuilder.loadTexts:
    stormBcastControlTable.setStatus("mandatory")
_StormBcastControlEntry_Object = MibTableRow
stormBcastControlEntry = _StormBcastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1)
)
stormBcastControlEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "stormBcastControlPort"),
)
if mibBuilder.loadTexts:
    stormBcastControlEntry.setStatus("mandatory")


class _StormBcastControlPort_Type(Integer32):
    """Custom type stormBcastControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_StormBcastControlPort_Type.__name__ = "Integer32"
_StormBcastControlPort_Object = MibTableColumn
stormBcastControlPort = _StormBcastControlPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 1),
    _StormBcastControlPort_Type()
)
stormBcastControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormBcastControlPort.setStatus("mandatory")


class _StormBcastControlThreshold_Type(Integer32):
    """Custom type stormBcastControlThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_StormBcastControlThreshold_Type.__name__ = "Integer32"
_StormBcastControlThreshold_Object = MibTableColumn
stormBcastControlThreshold = _StormBcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 2),
    _StormBcastControlThreshold_Type()
)
stormBcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormBcastControlThreshold.setStatus("mandatory")


class _StormBcastControlDiscardPeriod_Type(Integer32):
    """Custom type stormBcastControlDiscardPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StormBcastControlDiscardPeriod_Type.__name__ = "Integer32"
_StormBcastControlDiscardPeriod_Object = MibTableColumn
stormBcastControlDiscardPeriod = _StormBcastControlDiscardPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 3),
    _StormBcastControlDiscardPeriod_Type()
)
stormBcastControlDiscardPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormBcastControlDiscardPeriod.setStatus("mandatory")


class _StormBcastControlRate_Type(Integer32):
    """Custom type stormBcastControlRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StormBcastControlRate_Type.__name__ = "Integer32"
_StormBcastControlRate_Object = MibTableColumn
stormBcastControlRate = _StormBcastControlRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 4),
    _StormBcastControlRate_Type()
)
stormBcastControlRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormBcastControlRate.setStatus("mandatory")
_StormBcastControlDisables_Type = Integer32
_StormBcastControlDisables_Object = MibTableColumn
stormBcastControlDisables = _StormBcastControlDisables_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 5),
    _StormBcastControlDisables_Type()
)
stormBcastControlDisables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormBcastControlDisables.setStatus("mandatory")
_StormBcastControlEnables_Type = Integer32
_StormBcastControlEnables_Object = MibTableColumn
stormBcastControlEnables = _StormBcastControlEnables_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 6),
    _StormBcastControlEnables_Type()
)
stormBcastControlEnables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormBcastControlEnables.setStatus("mandatory")


class _StormBcastControlTimeLeft_Type(Integer32):
    """Custom type stormBcastControlTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StormBcastControlTimeLeft_Type.__name__ = "Integer32"
_StormBcastControlTimeLeft_Object = MibTableColumn
stormBcastControlTimeLeft = _StormBcastControlTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 7),
    _StormBcastControlTimeLeft_Type()
)
stormBcastControlTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormBcastControlTimeLeft.setStatus("mandatory")


class _StormBcastControlStatus_Type(Integer32):
    """Custom type stormBcastControlStatus based on Integer32"""
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
          ("discardingBroadcast", 5),
          ("discardingMulticast", 6),
          ("exitDiscardState", 7),
          ("monitorBoth", 4),
          ("monitorBroadcast", 2),
          ("monitorMulticast", 3))
    )


_StormBcastControlStatus_Type.__name__ = "Integer32"
_StormBcastControlStatus_Object = MibTableColumn
stormBcastControlStatus = _StormBcastControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 1, 1, 8),
    _StormBcastControlStatus_Type()
)
stormBcastControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormBcastControlStatus.setStatus("mandatory")
_StormMcastControlTable_Object = MibTable
stormMcastControlTable = _StormMcastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    stormMcastControlTable.setStatus("mandatory")
_StormMcastControlEntry_Object = MibTableRow
stormMcastControlEntry = _StormMcastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1)
)
stormMcastControlEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "stormMcastControlPort"),
)
if mibBuilder.loadTexts:
    stormMcastControlEntry.setStatus("mandatory")


class _StormMcastControlPort_Type(Integer32):
    """Custom type stormMcastControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_StormMcastControlPort_Type.__name__ = "Integer32"
_StormMcastControlPort_Object = MibTableColumn
stormMcastControlPort = _StormMcastControlPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 1),
    _StormMcastControlPort_Type()
)
stormMcastControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormMcastControlPort.setStatus("mandatory")


class _StormMcastControlThreshold_Type(Integer32):
    """Custom type stormMcastControlThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_StormMcastControlThreshold_Type.__name__ = "Integer32"
_StormMcastControlThreshold_Object = MibTableColumn
stormMcastControlThreshold = _StormMcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 2),
    _StormMcastControlThreshold_Type()
)
stormMcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormMcastControlThreshold.setStatus("mandatory")


class _StormMcastControlDiscardPeriod_Type(Integer32):
    """Custom type stormMcastControlDiscardPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StormMcastControlDiscardPeriod_Type.__name__ = "Integer32"
_StormMcastControlDiscardPeriod_Object = MibTableColumn
stormMcastControlDiscardPeriod = _StormMcastControlDiscardPeriod_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 3),
    _StormMcastControlDiscardPeriod_Type()
)
stormMcastControlDiscardPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormMcastControlDiscardPeriod.setStatus("mandatory")


class _StormMcastControlRate_Type(Integer32):
    """Custom type stormMcastControlRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StormMcastControlRate_Type.__name__ = "Integer32"
_StormMcastControlRate_Object = MibTableColumn
stormMcastControlRate = _StormMcastControlRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 4),
    _StormMcastControlRate_Type()
)
stormMcastControlRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormMcastControlRate.setStatus("mandatory")
_StormMcastControlDisables_Type = Integer32
_StormMcastControlDisables_Object = MibTableColumn
stormMcastControlDisables = _StormMcastControlDisables_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 5),
    _StormMcastControlDisables_Type()
)
stormMcastControlDisables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormMcastControlDisables.setStatus("mandatory")
_StormMcastControlEnables_Type = Integer32
_StormMcastControlEnables_Object = MibTableColumn
stormMcastControlEnables = _StormMcastControlEnables_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 6),
    _StormMcastControlEnables_Type()
)
stormMcastControlEnables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormMcastControlEnables.setStatus("mandatory")


class _StormMcastControlTimeLeft_Type(Integer32):
    """Custom type stormMcastControlTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_StormMcastControlTimeLeft_Type.__name__ = "Integer32"
_StormMcastControlTimeLeft_Object = MibTableColumn
stormMcastControlTimeLeft = _StormMcastControlTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 7),
    _StormMcastControlTimeLeft_Type()
)
stormMcastControlTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormMcastControlTimeLeft.setStatus("mandatory")


class _StormMcastControlStatus_Type(Integer32):
    """Custom type stormMcastControlStatus based on Integer32"""
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
          ("discardingBroadcast", 5),
          ("discardingMulticast", 6),
          ("exitDiscardState", 7),
          ("monitorBoth", 4),
          ("monitorBroadcast", 2),
          ("monitorMulticast", 3))
    )


_StormMcastControlStatus_Type.__name__ = "Integer32"
_StormMcastControlStatus_Object = MibTableColumn
stormMcastControlStatus = _StormMcastControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 24, 2, 1, 8),
    _StormMcastControlStatus_Type()
)
stormMcastControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormMcastControlStatus.setStatus("mandatory")
_IgmpSnoopingGroup_ObjectIdentity = ObjectIdentity
igmpSnoopingGroup = _IgmpSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25)
)


class _IgmpSnoopingEnable_Type(Integer32):
    """Custom type igmpSnoopingEnable based on Integer32"""
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


_IgmpSnoopingEnable_Type.__name__ = "Integer32"
_IgmpSnoopingEnable_Object = MibScalar
igmpSnoopingEnable = _IgmpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 1),
    _IgmpSnoopingEnable_Type()
)
igmpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingEnable.setStatus("mandatory")


class _IgmpSnoopingResetControl_Type(Integer32):
    """Custom type igmpSnoopingResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_IgmpSnoopingResetControl_Type.__name__ = "Integer32"
_IgmpSnoopingResetControl_Object = MibScalar
igmpSnoopingResetControl = _IgmpSnoopingResetControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 2),
    _IgmpSnoopingResetControl_Type()
)
igmpSnoopingResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingResetControl.setStatus("mandatory")


class _IgmpSnoopingResetData_Type(Integer32):
    """Custom type igmpSnoopingResetData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_IgmpSnoopingResetData_Type.__name__ = "Integer32"
_IgmpSnoopingResetData_Object = MibScalar
igmpSnoopingResetData = _IgmpSnoopingResetData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 3),
    _IgmpSnoopingResetData_Type()
)
igmpSnoopingResetData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingResetData.setStatus("mandatory")


class _IgmpSnoopingAgeTime_Type(TimeInterval):
    """Custom type igmpSnoopingAgeTime based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(330, 550),
    )


_IgmpSnoopingAgeTime_Type.__name__ = "TimeInterval"
_IgmpSnoopingAgeTime_Object = MibScalar
igmpSnoopingAgeTime = _IgmpSnoopingAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 4),
    _IgmpSnoopingAgeTime_Type()
)
igmpSnoopingAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingAgeTime.setStatus("mandatory")
_IgmpSnoopingVlanResetTable_Object = MibTable
igmpSnoopingVlanResetTable = _IgmpSnoopingVlanResetTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 5)
)
if mibBuilder.loadTexts:
    igmpSnoopingVlanResetTable.setStatus("mandatory")
_IgmpSnoopingVlanResetEntry_Object = MibTableRow
igmpSnoopingVlanResetEntry = _IgmpSnoopingVlanResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 5, 1)
)
igmpSnoopingVlanResetEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingVlanResetVlanId"),
)
if mibBuilder.loadTexts:
    igmpSnoopingVlanResetEntry.setStatus("mandatory")
_IgmpSnoopingVlanResetVlanId_Type = VlanId
_IgmpSnoopingVlanResetVlanId_Object = MibTableColumn
igmpSnoopingVlanResetVlanId = _IgmpSnoopingVlanResetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 5, 1, 1),
    _IgmpSnoopingVlanResetVlanId_Type()
)
igmpSnoopingVlanResetVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingVlanResetVlanId.setStatus("mandatory")


class _IgmpSnoopingVlanResetData_Type(Integer32):
    """Custom type igmpSnoopingVlanResetData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_IgmpSnoopingVlanResetData_Type.__name__ = "Integer32"
_IgmpSnoopingVlanResetData_Object = MibTableColumn
igmpSnoopingVlanResetData = _IgmpSnoopingVlanResetData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 5, 1, 2),
    _IgmpSnoopingVlanResetData_Type()
)
igmpSnoopingVlanResetData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingVlanResetData.setStatus("mandatory")


class _IgmpSnoopingVlanResetControl_Type(Integer32):
    """Custom type igmpSnoopingVlanResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_IgmpSnoopingVlanResetControl_Type.__name__ = "Integer32"
_IgmpSnoopingVlanResetControl_Object = MibTableColumn
igmpSnoopingVlanResetControl = _IgmpSnoopingVlanResetControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 5, 1, 3),
    _IgmpSnoopingVlanResetControl_Type()
)
igmpSnoopingVlanResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingVlanResetControl.setStatus("mandatory")
_IgmpSnoopingDataPortTable_Object = MibTable
igmpSnoopingDataPortTable = _IgmpSnoopingDataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6)
)
if mibBuilder.loadTexts:
    igmpSnoopingDataPortTable.setStatus("mandatory")
_IgmpSnoopingDataPortEntry_Object = MibTableRow
igmpSnoopingDataPortEntry = _IgmpSnoopingDataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1)
)
igmpSnoopingDataPortEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingDataPortVlanId"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingDataPortNumber"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingDataPortGroup"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingDataPortIpAddr"),
)
if mibBuilder.loadTexts:
    igmpSnoopingDataPortEntry.setStatus("mandatory")
_IgmpSnoopingDataPortVlanId_Type = VlanId
_IgmpSnoopingDataPortVlanId_Object = MibTableColumn
igmpSnoopingDataPortVlanId = _IgmpSnoopingDataPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1, 1),
    _IgmpSnoopingDataPortVlanId_Type()
)
igmpSnoopingDataPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingDataPortVlanId.setStatus("mandatory")
_IgmpSnoopingDataPortNumber_Type = PortNumber
_IgmpSnoopingDataPortNumber_Object = MibTableColumn
igmpSnoopingDataPortNumber = _IgmpSnoopingDataPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1, 2),
    _IgmpSnoopingDataPortNumber_Type()
)
igmpSnoopingDataPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingDataPortNumber.setStatus("mandatory")


class _IgmpSnoopingDataPortGroup_Type(Integer32):
    """Custom type igmpSnoopingDataPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ip", 2))
    )


_IgmpSnoopingDataPortGroup_Type.__name__ = "Integer32"
_IgmpSnoopingDataPortGroup_Object = MibTableColumn
igmpSnoopingDataPortGroup = _IgmpSnoopingDataPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1, 3),
    _IgmpSnoopingDataPortGroup_Type()
)
igmpSnoopingDataPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingDataPortGroup.setStatus("mandatory")
_IgmpSnoopingDataPortIpAddr_Type = IpAddress
_IgmpSnoopingDataPortIpAddr_Object = MibTableColumn
igmpSnoopingDataPortIpAddr = _IgmpSnoopingDataPortIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1, 4),
    _IgmpSnoopingDataPortIpAddr_Type()
)
igmpSnoopingDataPortIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingDataPortIpAddr.setStatus("mandatory")


class _IgmpSnoopingDataPortState_Type(Integer32):
    """Custom type igmpSnoopingDataPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 4),
          ("forbid", 5),
          ("normal", 3))
    )


_IgmpSnoopingDataPortState_Type.__name__ = "Integer32"
_IgmpSnoopingDataPortState_Object = MibTableColumn
igmpSnoopingDataPortState = _IgmpSnoopingDataPortState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 6, 1, 5),
    _IgmpSnoopingDataPortState_Type()
)
igmpSnoopingDataPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingDataPortState.setStatus("mandatory")
_IgmpSnoopingControlPortTable_Object = MibTable
igmpSnoopingControlPortTable = _IgmpSnoopingControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7)
)
if mibBuilder.loadTexts:
    igmpSnoopingControlPortTable.setStatus("mandatory")
_IgmpSnoopingControlPortEntry_Object = MibTableRow
igmpSnoopingControlPortEntry = _IgmpSnoopingControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7, 1)
)
igmpSnoopingControlPortEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingControlPortVlanId"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingControlPortNumber"),
)
if mibBuilder.loadTexts:
    igmpSnoopingControlPortEntry.setStatus("mandatory")
_IgmpSnoopingControlPortVlanId_Type = VlanId
_IgmpSnoopingControlPortVlanId_Object = MibTableColumn
igmpSnoopingControlPortVlanId = _IgmpSnoopingControlPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7, 1, 1),
    _IgmpSnoopingControlPortVlanId_Type()
)
igmpSnoopingControlPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingControlPortVlanId.setStatus("mandatory")
_IgmpSnoopingControlPortNumber_Type = PortNumber
_IgmpSnoopingControlPortNumber_Object = MibTableColumn
igmpSnoopingControlPortNumber = _IgmpSnoopingControlPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7, 1, 2),
    _IgmpSnoopingControlPortNumber_Type()
)
igmpSnoopingControlPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingControlPortNumber.setStatus("mandatory")


class _IgmpSnoopingControlPortState_Type(Integer32):
    """Custom type igmpSnoopingControlPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("forbid", 3),
          ("normal", 1))
    )


_IgmpSnoopingControlPortState_Type.__name__ = "Integer32"
_IgmpSnoopingControlPortState_Object = MibTableColumn
igmpSnoopingControlPortState = _IgmpSnoopingControlPortState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7, 1, 3),
    _IgmpSnoopingControlPortState_Type()
)
igmpSnoopingControlPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingControlPortState.setStatus("mandatory")
_IgmpSnoopingControlPortRowStatus_Type = RowStatus
_IgmpSnoopingControlPortRowStatus_Object = MibTableColumn
igmpSnoopingControlPortRowStatus = _IgmpSnoopingControlPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 7, 1, 4),
    _IgmpSnoopingControlPortRowStatus_Type()
)
igmpSnoopingControlPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingControlPortRowStatus.setStatus("mandatory")
_IgmpSnoopingStatusTable_Object = MibTable
igmpSnoopingStatusTable = _IgmpSnoopingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopingStatusTable.setStatus("mandatory")
_IgmpSnoopingStatusEntry_Object = MibTableRow
igmpSnoopingStatusEntry = _IgmpSnoopingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 8, 1)
)
igmpSnoopingStatusEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingVlanId"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingMcastMacAddr"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingPort"),
)
if mibBuilder.loadTexts:
    igmpSnoopingStatusEntry.setStatus("mandatory")
_IgmpSnoopingVlanId_Type = VlanId
_IgmpSnoopingVlanId_Object = MibTableColumn
igmpSnoopingVlanId = _IgmpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 8, 1, 1),
    _IgmpSnoopingVlanId_Type()
)
igmpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingVlanId.setStatus("mandatory")
_IgmpSnoopingMcastMacAddr_Type = MacAddress
_IgmpSnoopingMcastMacAddr_Object = MibTableColumn
igmpSnoopingMcastMacAddr = _IgmpSnoopingMcastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 8, 1, 2),
    _IgmpSnoopingMcastMacAddr_Type()
)
igmpSnoopingMcastMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingMcastMacAddr.setStatus("mandatory")
_IgmpSnoopingPort_Type = PortNumber
_IgmpSnoopingPort_Object = MibTableColumn
igmpSnoopingPort = _IgmpSnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 8, 1, 3),
    _IgmpSnoopingPort_Type()
)
igmpSnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingPort.setStatus("mandatory")
_IgmpSnoopingIpStatusTable_Object = MibTable
igmpSnoopingIpStatusTable = _IgmpSnoopingIpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopingIpStatusTable.setStatus("mandatory")
_IgmpSnoopingIpStatusEntry_Object = MibTableRow
igmpSnoopingIpStatusEntry = _IgmpSnoopingIpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 9, 1)
)
igmpSnoopingIpStatusEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingVlanId"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingMcastMacAddr"),
    (0, "Intel-6000-Switch-MIB", "igmpSnoopingIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopingIpStatusEntry.setStatus("mandatory")
_IgmpSnoopingIpVlanId_Type = VlanId
_IgmpSnoopingIpVlanId_Object = MibTableColumn
igmpSnoopingIpVlanId = _IgmpSnoopingIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 9, 1, 1),
    _IgmpSnoopingIpVlanId_Type()
)
igmpSnoopingIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingIpVlanId.setStatus("mandatory")
_IgmpSnoopingIpMcastMacAddr_Type = MacAddress
_IgmpSnoopingIpMcastMacAddr_Object = MibTableColumn
igmpSnoopingIpMcastMacAddr = _IgmpSnoopingIpMcastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 9, 1, 2),
    _IgmpSnoopingIpMcastMacAddr_Type()
)
igmpSnoopingIpMcastMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingIpMcastMacAddr.setStatus("mandatory")
_IgmpSnoopingIpAddress_Type = IpAddress
_IgmpSnoopingIpAddress_Object = MibTableColumn
igmpSnoopingIpAddress = _IgmpSnoopingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 25, 9, 1, 3),
    _IgmpSnoopingIpAddress_Type()
)
igmpSnoopingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingIpAddress.setStatus("mandatory")
_PvstpGroup_ObjectIdentity = ObjectIdentity
pvstpGroup = _PvstpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26)
)
_PvstpTable_Object = MibTable
pvstpTable = _PvstpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1)
)
if mibBuilder.loadTexts:
    pvstpTable.setStatus("mandatory")
_PvstpEntry_Object = MibTableRow
pvstpEntry = _PvstpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1)
)
pvstpEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "pvstpVlanId"),
)
if mibBuilder.loadTexts:
    pvstpEntry.setStatus("mandatory")
_PvstpVlanId_Type = VlanId
_PvstpVlanId_Object = MibTableColumn
pvstpVlanId = _PvstpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 1),
    _PvstpVlanId_Type()
)
pvstpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpVlanId.setStatus("mandatory")


class _PvstpProtocolSpecification_Type(Integer32):
    """Custom type pvstpProtocolSpecification based on Integer32"""
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
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("ieee8021w1s1", 4),
          ("unknown", 1))
    )


_PvstpProtocolSpecification_Type.__name__ = "Integer32"
_PvstpProtocolSpecification_Object = MibTableColumn
pvstpProtocolSpecification = _PvstpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 2),
    _PvstpProtocolSpecification_Type()
)
pvstpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpProtocolSpecification.setStatus("mandatory")


class _PvstpPriority_Type(Integer32):
    """Custom type pvstpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PvstpPriority_Type.__name__ = "Integer32"
_PvstpPriority_Object = MibTableColumn
pvstpPriority = _PvstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 3),
    _PvstpPriority_Type()
)
pvstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpPriority.setStatus("mandatory")
_PvstpTimeSinceTopologyChange_Type = TimeTicks
_PvstpTimeSinceTopologyChange_Object = MibTableColumn
pvstpTimeSinceTopologyChange = _PvstpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 4),
    _PvstpTimeSinceTopologyChange_Type()
)
pvstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpTimeSinceTopologyChange.setStatus("mandatory")
_PvstpTopChanges_Type = Counter32
_PvstpTopChanges_Object = MibTableColumn
pvstpTopChanges = _PvstpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 5),
    _PvstpTopChanges_Type()
)
pvstpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpTopChanges.setStatus("mandatory")
_PvstpDesignatedRoot_Type = BridgeId
_PvstpDesignatedRoot_Object = MibTableColumn
pvstpDesignatedRoot = _PvstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 6),
    _PvstpDesignatedRoot_Type()
)
pvstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpDesignatedRoot.setStatus("mandatory")
_PvstpRootCost_Type = Integer32
_PvstpRootCost_Object = MibTableColumn
pvstpRootCost = _PvstpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 7),
    _PvstpRootCost_Type()
)
pvstpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpRootCost.setStatus("mandatory")
_PvstpRootPort_Type = Integer32
_PvstpRootPort_Object = MibTableColumn
pvstpRootPort = _PvstpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 8),
    _PvstpRootPort_Type()
)
pvstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpRootPort.setStatus("mandatory")
_PvstpMaxAge_Type = Timeout
_PvstpMaxAge_Object = MibTableColumn
pvstpMaxAge = _PvstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 9),
    _PvstpMaxAge_Type()
)
pvstpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpMaxAge.setStatus("mandatory")
_PvstpHelloTime_Type = Timeout
_PvstpHelloTime_Object = MibTableColumn
pvstpHelloTime = _PvstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 10),
    _PvstpHelloTime_Type()
)
pvstpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpHelloTime.setStatus("mandatory")
_PvstpHoldTime_Type = Integer32
_PvstpHoldTime_Object = MibTableColumn
pvstpHoldTime = _PvstpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 11),
    _PvstpHoldTime_Type()
)
pvstpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpHoldTime.setStatus("mandatory")
_PvstpForwardDelay_Type = Timeout
_PvstpForwardDelay_Object = MibTableColumn
pvstpForwardDelay = _PvstpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 12),
    _PvstpForwardDelay_Type()
)
pvstpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpForwardDelay.setStatus("mandatory")


class _PvstpBridgeMaxAge_Type(Timeout):
    """Custom type pvstpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_PvstpBridgeMaxAge_Type.__name__ = "Timeout"
_PvstpBridgeMaxAge_Object = MibTableColumn
pvstpBridgeMaxAge = _PvstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 13),
    _PvstpBridgeMaxAge_Type()
)
pvstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpBridgeMaxAge.setStatus("mandatory")


class _PvstpBridgeHelloTime_Type(Timeout):
    """Custom type pvstpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PvstpBridgeHelloTime_Type.__name__ = "Timeout"
_PvstpBridgeHelloTime_Object = MibTableColumn
pvstpBridgeHelloTime = _PvstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 14),
    _PvstpBridgeHelloTime_Type()
)
pvstpBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpBridgeHelloTime.setStatus("mandatory")


class _PvstpBridgeForwardDelay_Type(Timeout):
    """Custom type pvstpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_PvstpBridgeForwardDelay_Type.__name__ = "Timeout"
_PvstpBridgeForwardDelay_Object = MibTableColumn
pvstpBridgeForwardDelay = _PvstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 15),
    _PvstpBridgeForwardDelay_Type()
)
pvstpBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpBridgeForwardDelay.setStatus("mandatory")


class _PvstpBridgeRapid_Type(Integer32):
    """Custom type pvstpBridgeRapid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PvstpBridgeRapid_Type.__name__ = "Integer32"
_PvstpBridgeRapid_Object = MibTableColumn
pvstpBridgeRapid = _PvstpBridgeRapid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 16),
    _PvstpBridgeRapid_Type()
)
pvstpBridgeRapid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpBridgeRapid.setStatus("mandatory")
_PvstpBridgeId_Type = BridgeId
_PvstpBridgeId_Object = MibTableColumn
pvstpBridgeId = _PvstpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 1, 1, 17),
    _PvstpBridgeId_Type()
)
pvstpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpBridgeId.setStatus("mandatory")
_PvstpPortTable_Object = MibTable
pvstpPortTable = _PvstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2)
)
if mibBuilder.loadTexts:
    pvstpPortTable.setStatus("mandatory")
_PvstpPortEntry_Object = MibTableRow
pvstpPortEntry = _PvstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1)
)
pvstpPortEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "pvstpPortVlanId"),
    (0, "Intel-6000-Switch-MIB", "pvstpPort"),
)
if mibBuilder.loadTexts:
    pvstpPortEntry.setStatus("mandatory")
_PvstpPortVlanId_Type = VlanId
_PvstpPortVlanId_Object = MibTableColumn
pvstpPortVlanId = _PvstpPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 1),
    _PvstpPortVlanId_Type()
)
pvstpPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortVlanId.setStatus("mandatory")
_PvstpPort_Type = PortNumber
_PvstpPort_Object = MibTableColumn
pvstpPort = _PvstpPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 2),
    _PvstpPort_Type()
)
pvstpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPort.setStatus("mandatory")


class _PvstpPortPriority_Type(Integer32):
    """Custom type pvstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvstpPortPriority_Type.__name__ = "Integer32"
_PvstpPortPriority_Object = MibTableColumn
pvstpPortPriority = _PvstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 3),
    _PvstpPortPriority_Type()
)
pvstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpPortPriority.setStatus("mandatory")


class _PvstpPortState_Type(Integer32):
    """Custom type pvstpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_PvstpPortState_Type.__name__ = "Integer32"
_PvstpPortState_Object = MibTableColumn
pvstpPortState = _PvstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 4),
    _PvstpPortState_Type()
)
pvstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortState.setStatus("mandatory")


class _PvstpPortEnable_Type(Integer32):
    """Custom type pvstpPortEnable based on Integer32"""
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


_PvstpPortEnable_Type.__name__ = "Integer32"
_PvstpPortEnable_Object = MibTableColumn
pvstpPortEnable = _PvstpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 5),
    _PvstpPortEnable_Type()
)
pvstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpPortEnable.setStatus("mandatory")


class _PvstpPortPathCost_Type(Integer32):
    """Custom type pvstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PvstpPortPathCost_Type.__name__ = "Integer32"
_PvstpPortPathCost_Object = MibTableColumn
pvstpPortPathCost = _PvstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 6),
    _PvstpPortPathCost_Type()
)
pvstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpPortPathCost.setStatus("mandatory")
_PvstpPortDesignatedRoot_Type = BridgeId
_PvstpPortDesignatedRoot_Object = MibTableColumn
pvstpPortDesignatedRoot = _PvstpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 7),
    _PvstpPortDesignatedRoot_Type()
)
pvstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortDesignatedRoot.setStatus("mandatory")
_PvstpPortDesignatedCost_Type = Integer32
_PvstpPortDesignatedCost_Object = MibTableColumn
pvstpPortDesignatedCost = _PvstpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 8),
    _PvstpPortDesignatedCost_Type()
)
pvstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortDesignatedCost.setStatus("mandatory")
_PvstpPortDesignatedBridge_Type = BridgeId
_PvstpPortDesignatedBridge_Object = MibTableColumn
pvstpPortDesignatedBridge = _PvstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 9),
    _PvstpPortDesignatedBridge_Type()
)
pvstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortDesignatedBridge.setStatus("mandatory")


class _PvstpPortDesignatedPort_Type(OctetString):
    """Custom type pvstpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PvstpPortDesignatedPort_Type.__name__ = "OctetString"
_PvstpPortDesignatedPort_Object = MibTableColumn
pvstpPortDesignatedPort = _PvstpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 11),
    _PvstpPortDesignatedPort_Type()
)
pvstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortDesignatedPort.setStatus("mandatory")
_PvstpPortForwardTransitions_Type = Counter32
_PvstpPortForwardTransitions_Object = MibTableColumn
pvstpPortForwardTransitions = _PvstpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 12),
    _PvstpPortForwardTransitions_Type()
)
pvstpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortForwardTransitions.setStatus("mandatory")


class _PvstpPortQuick_Type(Integer32):
    """Custom type pvstpPortQuick based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PvstpPortQuick_Type.__name__ = "Integer32"
_PvstpPortQuick_Object = MibTableColumn
pvstpPortQuick = _PvstpPortQuick_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 13),
    _PvstpPortQuick_Type()
)
pvstpPortQuick.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvstpPortQuick.setStatus("mandatory")


class _PvstpPortAuto_Type(Integer32):
    """Custom type pvstpPortAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("fixed", 1))
    )


_PvstpPortAuto_Type.__name__ = "Integer32"
_PvstpPortAuto_Object = MibTableColumn
pvstpPortAuto = _PvstpPortAuto_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 26, 2, 1, 14),
    _PvstpPortAuto_Type()
)
pvstpPortAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvstpPortAuto.setStatus("mandatory")
_RelayGroup_ObjectIdentity = ObjectIdentity
relayGroup = _RelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27)
)
_RelayEnable_Type = EnableStatus
_RelayEnable_Object = MibScalar
relayEnable = _RelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 1),
    _RelayEnable_Type()
)
relayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayEnable.setStatus("mandatory")


class _RelayMaxHops_Type(Integer32):
    """Custom type relayMaxHops based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RelayMaxHops_Type.__name__ = "Integer32"
_RelayMaxHops_Object = MibScalar
relayMaxHops = _RelayMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 2),
    _RelayMaxHops_Type()
)
relayMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayMaxHops.setStatus("mandatory")
_RelayServerTable_Object = MibTable
relayServerTable = _RelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 3)
)
if mibBuilder.loadTexts:
    relayServerTable.setStatus("mandatory")
_RelayServerEntry_Object = MibTableRow
relayServerEntry = _RelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 3, 1)
)
relayServerEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "relayServerIndex"),
)
if mibBuilder.loadTexts:
    relayServerEntry.setStatus("mandatory")


class _RelayServerIndex_Type(Integer32):
    """Custom type relayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RelayServerIndex_Type.__name__ = "Integer32"
_RelayServerIndex_Object = MibTableColumn
relayServerIndex = _RelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 3, 1, 1),
    _RelayServerIndex_Type()
)
relayServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayServerIndex.setStatus("mandatory")
_RelayServerAddress_Type = IpAddress
_RelayServerAddress_Object = MibTableColumn
relayServerAddress = _RelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 27, 3, 1, 2),
    _RelayServerAddress_Type()
)
relayServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayServerAddress.setStatus("mandatory")
_PortMirrorGroup_ObjectIdentity = ObjectIdentity
portMirrorGroup = _PortMirrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29)
)
_PortMirrorTable_Object = MibTable
portMirrorTable = _PortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29, 1)
)
if mibBuilder.loadTexts:
    portMirrorTable.setStatus("mandatory")
_PortMirrorEntry_Object = MibTableRow
portMirrorEntry = _PortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29, 1, 1)
)
portMirrorEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "portMirrorSourcePort"),
    (0, "Intel-6000-Switch-MIB", "portMirrorMonitorPort"),
)
if mibBuilder.loadTexts:
    portMirrorEntry.setStatus("mandatory")
_PortMirrorSourcePort_Type = PortNumber
_PortMirrorSourcePort_Object = MibTableColumn
portMirrorSourcePort = _PortMirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29, 1, 1, 1),
    _PortMirrorSourcePort_Type()
)
portMirrorSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMirrorSourcePort.setStatus("mandatory")
_PortMirrorMonitorPort_Type = PortNumber
_PortMirrorMonitorPort_Object = MibTableColumn
portMirrorMonitorPort = _PortMirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29, 1, 1, 2),
    _PortMirrorMonitorPort_Type()
)
portMirrorMonitorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMirrorMonitorPort.setStatus("mandatory")
_PortMirrorRowStatus_Type = RowStatus
_PortMirrorRowStatus_Object = MibTableColumn
portMirrorRowStatus = _PortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 29, 1, 1, 3),
    _PortMirrorRowStatus_Type()
)
portMirrorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorRowStatus.setStatus("mandatory")
_IpAccessCtlGroup_ObjectIdentity = ObjectIdentity
ipAccessCtlGroup = _IpAccessCtlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30)
)
_IpAccessCtlTable_Object = MibTable
ipAccessCtlTable = _IpAccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1)
)
if mibBuilder.loadTexts:
    ipAccessCtlTable.setStatus("mandatory")
_IpAccessCtlEntry_Object = MibTableRow
ipAccessCtlEntry = _IpAccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1)
)
ipAccessCtlEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "ipAccessCtlRuleNumber"),
)
if mibBuilder.loadTexts:
    ipAccessCtlEntry.setStatus("mandatory")


class _IpAccessCtlRuleNumber_Type(Integer32):
    """Custom type ipAccessCtlRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IpAccessCtlRuleNumber_Type.__name__ = "Integer32"
_IpAccessCtlRuleNumber_Object = MibTableColumn
ipAccessCtlRuleNumber = _IpAccessCtlRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 1),
    _IpAccessCtlRuleNumber_Type()
)
ipAccessCtlRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAccessCtlRuleNumber.setStatus("mandatory")
_IpAccessCtlSourceAddress_Type = IpAddress
_IpAccessCtlSourceAddress_Object = MibTableColumn
ipAccessCtlSourceAddress = _IpAccessCtlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 2),
    _IpAccessCtlSourceAddress_Type()
)
ipAccessCtlSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlSourceAddress.setStatus("mandatory")
_IpAccessCtlSourceMask_Type = IpAddress
_IpAccessCtlSourceMask_Object = MibTableColumn
ipAccessCtlSourceMask = _IpAccessCtlSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 3),
    _IpAccessCtlSourceMask_Type()
)
ipAccessCtlSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlSourceMask.setStatus("mandatory")
_IpAccessCtlDestinationAddress_Type = IpAddress
_IpAccessCtlDestinationAddress_Object = MibTableColumn
ipAccessCtlDestinationAddress = _IpAccessCtlDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 4),
    _IpAccessCtlDestinationAddress_Type()
)
ipAccessCtlDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlDestinationAddress.setStatus("mandatory")
_IpAccessCtlDestinationMask_Type = IpAddress
_IpAccessCtlDestinationMask_Object = MibTableColumn
ipAccessCtlDestinationMask = _IpAccessCtlDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 5),
    _IpAccessCtlDestinationMask_Type()
)
ipAccessCtlDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlDestinationMask.setStatus("mandatory")


class _IpAccessCtlType_Type(Integer32):
    """Custom type ipAccessCtlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IpAccessCtlType_Type.__name__ = "Integer32"
_IpAccessCtlType_Object = MibTableColumn
ipAccessCtlType = _IpAccessCtlType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 6),
    _IpAccessCtlType_Type()
)
ipAccessCtlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlType.setStatus("mandatory")
_IpAccessCtlRowStatus_Type = RowStatus
_IpAccessCtlRowStatus_Object = MibTableColumn
ipAccessCtlRowStatus = _IpAccessCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 1, 1, 7),
    _IpAccessCtlRowStatus_Type()
)
ipAccessCtlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlRowStatus.setStatus("mandatory")
_IpAccessCtlEnable_Type = EnableStatus
_IpAccessCtlEnable_Object = MibScalar
ipAccessCtlEnable = _IpAccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 30, 2),
    _IpAccessCtlEnable_Type()
)
ipAccessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessCtlEnable.setStatus("mandatory")
_FdbGroup_ObjectIdentity = ObjectIdentity
fdbGroup = _FdbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31)
)


class _FdbLearningMode_Type(Integer32):
    """Custom type fdbLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2))
    )


_FdbLearningMode_Type.__name__ = "Integer32"
_FdbLearningMode_Object = MibScalar
fdbLearningMode = _FdbLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 1),
    _FdbLearningMode_Type()
)
fdbLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbLearningMode.setStatus("mandatory")
_FdbAgeTable_Object = MibTable
fdbAgeTable = _FdbAgeTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 2)
)
if mibBuilder.loadTexts:
    fdbAgeTable.setStatus("mandatory")
_FdbAgeEntry_Object = MibTableRow
fdbAgeEntry = _FdbAgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 2, 1)
)
fdbAgeEntry.setIndexNames(
    (0, "Intel-6000-Switch-MIB", "fdbAgeId"),
)
if mibBuilder.loadTexts:
    fdbAgeEntry.setStatus("mandatory")
_FdbAgeId_Type = VlanId
_FdbAgeId_Object = MibTableColumn
fdbAgeId = _FdbAgeId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 2, 1, 1),
    _FdbAgeId_Type()
)
fdbAgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbAgeId.setStatus("mandatory")
_FdbAgeStatus_Type = EnableStatus
_FdbAgeStatus_Object = MibTableColumn
fdbAgeStatus = _FdbAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 2, 1, 2),
    _FdbAgeStatus_Type()
)
fdbAgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAgeStatus.setStatus("mandatory")


class _FdbAgeTime_Type(Integer32):
    """Custom type fdbAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32767),
    )


_FdbAgeTime_Type.__name__ = "Integer32"
_FdbAgeTime_Object = MibTableColumn
fdbAgeTime = _FdbAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 31, 2, 1, 3),
    _FdbAgeTime_Type()
)
fdbAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAgeTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

carrierCPSlotChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 1)
)
carrierCPSlotChangeEvent.setObjects(
    ("Intel-6000-Switch-MIB", "carrierCPSlotID")
)
if mibBuilder.loadTexts:
    carrierCPSlotChangeEvent.setStatus(
        ""
    )

carrierStatusAChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 2)
)
carrierStatusAChangeEvent.setObjects(
    ("Intel-6000-Switch-MIB", "carrierStatusA")
)
if mibBuilder.loadTexts:
    carrierStatusAChangeEvent.setStatus(
        ""
    )

carrierStatusBChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 3)
)
carrierStatusBChangeEvent.setObjects(
    ("Intel-6000-Switch-MIB", "carrierStatusB")
)
if mibBuilder.loadTexts:
    carrierStatusBChangeEvent.setStatus(
        ""
    )

mediaCardChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    mediaCardChangeEvent.setStatus(
        ""
    )

fanFailEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    fanFailEvent.setStatus(
        ""
    )

powerSupplyFailEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    powerSupplyFailEvent.setStatus(
        ""
    )

highTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    highTemperatureEvent.setStatus(
        ""
    )

risingTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 8)
)
risingTemperatureEvent.setObjects(
    ("Intel-6000-Switch-MIB", "tempCurrent")
)
if mibBuilder.loadTexts:
    risingTemperatureEvent.setStatus(
        ""
    )

fallingTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 9)
)
fallingTemperatureEvent.setObjects(
    ("Intel-6000-Switch-MIB", "tempCurrent")
)
if mibBuilder.loadTexts:
    fallingTemperatureEvent.setStatus(
        ""
    )

stormBcastControlDiscardEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 10)
)
stormBcastControlDiscardEvent.setObjects(
    ("Intel-6000-Switch-MIB", "stormBcastControlPort")
)
if mibBuilder.loadTexts:
    stormBcastControlDiscardEvent.setStatus(
        ""
    )

stormMcastControlDiscardEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 11, 1, 2, 0, 11)
)
stormMcastControlDiscardEvent.setObjects(
    ("Intel-6000-Switch-MIB", "stormMcastControlPort")
)
if mibBuilder.loadTexts:
    stormMcastControlDiscardEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Intel-6000-Switch-MIB",
    **{"TimeInterval": TimeInterval,
       "MacAddress": MacAddress,
       "VlanId": VlanId,
       "PortNumber": PortNumber,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnableStatus": EnableStatus,
       "Boolean": Boolean,
       "RowStatus": RowStatus,
       "intel6000Switch": intel6000Switch,
       "express6000": express6000,
       "switchMIB": switchMIB,
       "carrierCPSlotChangeEvent": carrierCPSlotChangeEvent,
       "carrierStatusAChangeEvent": carrierStatusAChangeEvent,
       "carrierStatusBChangeEvent": carrierStatusBChangeEvent,
       "mediaCardChangeEvent": mediaCardChangeEvent,
       "fanFailEvent": fanFailEvent,
       "powerSupplyFailEvent": powerSupplyFailEvent,
       "highTemperatureEvent": highTemperatureEvent,
       "risingTemperatureEvent": risingTemperatureEvent,
       "fallingTemperatureEvent": fallingTemperatureEvent,
       "stormBcastControlDiscardEvent": stormBcastControlDiscardEvent,
       "stormMcastControlDiscardEvent": stormMcastControlDiscardEvent,
       "switchConfigGroup": switchConfigGroup,
       "ipAddress": ipAddress,
       "netMask": netMask,
       "defaultGateway": defaultGateway,
       "broadcastAddress": broadcastAddress,
       "maxMacAddresses": maxMacAddresses,
       "clearStatistics": clearStatistics,
       "ageFilterDatabase": ageFilterDatabase,
       "entMibVersion": entMibVersion,
       "telnetEnable": telnetEnable,
       "syslogEnable": syslogEnable,
       "syslogIp": syslogIp,
       "syslogCmds": syslogCmds,
       "syslogOut": syslogOut,
       "nvramLoadSave": nvramLoadSave,
       "nvramLastOpStat": nvramLastOpStat,
       "nvramRemoteIp": nvramRemoteIp,
       "nvramRemotePath": nvramRemotePath,
       "monitorGroup": monitorGroup,
       "diagnosticsResults": diagnosticsResults,
       "diagnosticsTime": diagnosticsTime,
       "lastDiagnosticsTest": lastDiagnosticsTest,
       "commGroup": commGroup,
       "commNumComms": commNumComms,
       "commInfoTable": commInfoTable,
       "commInfoEntry": commInfoEntry,
       "commInfoIndex": commInfoIndex,
       "commInfoName": commInfoName,
       "commInfoGet": commInfoGet,
       "commInfoSet": commInfoSet,
       "commInfoTrap": commInfoTrap,
       "commAltTrapPort": commAltTrapPort,
       "commSnmpSecurityLevel": commSnmpSecurityLevel,
       "hostGroup": hostGroup,
       "hostNumHosts": hostNumHosts,
       "hostInfoTable": hostInfoTable,
       "hostInfoEntry": hostInfoEntry,
       "hostInfoIndex": hostInfoIndex,
       "hostInfoName": hostInfoName,
       "hostInfoIp": hostInfoIp,
       "hostInfoComm": hostInfoComm,
       "serialGroup": serialGroup,
       "serialBaudRate": serialBaudRate,
       "modemControlLines": modemControlLines,
       "spanGroup": spanGroup,
       "spanOnOff": spanOnOff,
       "spanType": spanType,
       "spanResetDefaults": spanResetDefaults,
       "spanRapid": spanRapid,
       "spanPortTable": spanPortTable,
       "spanPortEntry": spanPortEntry,
       "spanPortPort": spanPortPort,
       "spanPortQuickStatus": spanPortQuickStatus,
       "spanPortAuto": spanPortAuto,
       "fanGroup": fanGroup,
       "fanNumFans": fanNumFans,
       "fanInfoTable": fanInfoTable,
       "fanInfoEntry": fanInfoEntry,
       "fanIndex": fanIndex,
       "fanStatus": fanStatus,
       "psGroup": psGroup,
       "psNumber": psNumber,
       "psInfoTable": psInfoTable,
       "psInfoEntry": psInfoEntry,
       "psIndex": psIndex,
       "psPresent": psPresent,
       "psStatus": psStatus,
       "tempGroup": tempGroup,
       "tempCurrent": tempCurrent,
       "tempAlarm": tempAlarm,
       "tempHighest": tempHighest,
       "tempHigh": tempHigh,
       "tempLow": tempLow,
       "gigabitGroup": gigabitGroup,
       "gigabitPortTable": gigabitPortTable,
       "gigabitPortTableEntry": gigabitPortTableEntry,
       "gigabitPortTableSlot": gigabitPortTableSlot,
       "gigabitPortTablePort": gigabitPortTablePort,
       "gigabitPortTableLinkState": gigabitPortTableLinkState,
       "gigabitPortTablePortAutoNeg": gigabitPortTablePortAutoNeg,
       "tenHundredGroup": tenHundredGroup,
       "tenHundredPortTable": tenHundredPortTable,
       "tenHundredPortTableEntry": tenHundredPortTableEntry,
       "tenHundredPortTableSlot": tenHundredPortTableSlot,
       "tenHundredPortTablePort": tenHundredPortTablePort,
       "tenHundredPortTableLinkState": tenHundredPortTableLinkState,
       "tenHundredPortTableConfig": tenHundredPortTableConfig,
       "vlanGroup": vlanGroup,
       "vlanValid": vlanValid,
       "vlanConfigTable": vlanConfigTable,
       "vlanConfigEntry": vlanConfigEntry,
       "vlanConfigVID": vlanConfigVID,
       "vlanConfigName": vlanConfigName,
       "vlanConfigIpAddr": vlanConfigIpAddr,
       "vlanConfigNetmask": vlanConfigNetmask,
       "vlanConfigBroadcast": vlanConfigBroadcast,
       "vlanConfigRouting": vlanConfigRouting,
       "vlanReset": vlanReset,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortNumber": vlanPortNumber,
       "vlanPortTrustedVid": vlanPortTrustedVid,
       "vlanPortTrustedPriority": vlanPortTrustedPriority,
       "routingGroup": routingGroup,
       "routingRouterId": routingRouterId,
       "routingScanInterval": routingScanInterval,
       "routingConfigGroup": routingConfigGroup,
       "routingEnable": routingEnable,
       "routingRipConf": routingRipConf,
       "routingOspfConf": routingOspfConf,
       "routingPreferencesGroup": routingPreferencesGroup,
       "routingOspfPref": routingOspfPref,
       "routingStaticConfigPref": routingStaticConfigPref,
       "routingRipPref": routingRipPref,
       "routingOspfAsExtPref": routingOspfAsExtPref,
       "routingIfPrefTable": routingIfPrefTable,
       "routingIfPrefEntry": routingIfPrefEntry,
       "routingIfPrefAddress": routingIfPrefAddress,
       "routingIfPref": routingIfPref,
       "staticRouteNumber": staticRouteNumber,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteDest": staticRouteDest,
       "staticRouteMask": staticRouteMask,
       "staticRouteNextHop": staticRouteNextHop,
       "staticRouteIf": staticRouteIf,
       "staticRoutePref": staticRoutePref,
       "staticRouteType": staticRouteType,
       "staticRouteStatus": staticRouteStatus,
       "routingSaveConfig": routingSaveConfig,
       "errorGroup": errorGroup,
       "errorTable": errorTable,
       "errorEntry": errorEntry,
       "errorIndex": errorIndex,
       "errorMsg": errorMsg,
       "errorOid": errorOid,
       "errorTime": errorTime,
       "clearErrorTable": clearErrorTable,
       "linkStateGroup": linkStateGroup,
       "linkStateTable": linkStateTable,
       "linkStateEntry": linkStateEntry,
       "linkStateSlot": linkStateSlot,
       "linkStatePort": linkStatePort,
       "linkStateState": linkStateState,
       "linkStateTime": linkStateTime,
       "carrierGroup": carrierGroup,
       "carrierCPSlotID": carrierCPSlotID,
       "carrierStatusA": carrierStatusA,
       "carrierStatusB": carrierStatusB,
       "moduleGroup": moduleGroup,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleSlotNum": moduleSlotNum,
       "moduleCard": moduleCard,
       "moduleContent": moduleContent,
       "moduleDataValid": moduleDataValid,
       "moduleText": moduleText,
       "pingGroup": pingGroup,
       "pingHostAddress": pingHostAddress,
       "pingRequest": pingRequest,
       "pingTime": pingTime,
       "pingStatus": pingStatus,
       "dnsGroup": dnsGroup,
       "dnsEnable": dnsEnable,
       "dnsDomainName": dnsDomainName,
       "dnsPrimaryServer": dnsPrimaryServer,
       "dnsBackupServer": dnsBackupServer,
       "stormControlGroup": stormControlGroup,
       "stormBcastControlTable": stormBcastControlTable,
       "stormBcastControlEntry": stormBcastControlEntry,
       "stormBcastControlPort": stormBcastControlPort,
       "stormBcastControlThreshold": stormBcastControlThreshold,
       "stormBcastControlDiscardPeriod": stormBcastControlDiscardPeriod,
       "stormBcastControlRate": stormBcastControlRate,
       "stormBcastControlDisables": stormBcastControlDisables,
       "stormBcastControlEnables": stormBcastControlEnables,
       "stormBcastControlTimeLeft": stormBcastControlTimeLeft,
       "stormBcastControlStatus": stormBcastControlStatus,
       "stormMcastControlTable": stormMcastControlTable,
       "stormMcastControlEntry": stormMcastControlEntry,
       "stormMcastControlPort": stormMcastControlPort,
       "stormMcastControlThreshold": stormMcastControlThreshold,
       "stormMcastControlDiscardPeriod": stormMcastControlDiscardPeriod,
       "stormMcastControlRate": stormMcastControlRate,
       "stormMcastControlDisables": stormMcastControlDisables,
       "stormMcastControlEnables": stormMcastControlEnables,
       "stormMcastControlTimeLeft": stormMcastControlTimeLeft,
       "stormMcastControlStatus": stormMcastControlStatus,
       "igmpSnoopingGroup": igmpSnoopingGroup,
       "igmpSnoopingEnable": igmpSnoopingEnable,
       "igmpSnoopingResetControl": igmpSnoopingResetControl,
       "igmpSnoopingResetData": igmpSnoopingResetData,
       "igmpSnoopingAgeTime": igmpSnoopingAgeTime,
       "igmpSnoopingVlanResetTable": igmpSnoopingVlanResetTable,
       "igmpSnoopingVlanResetEntry": igmpSnoopingVlanResetEntry,
       "igmpSnoopingVlanResetVlanId": igmpSnoopingVlanResetVlanId,
       "igmpSnoopingVlanResetData": igmpSnoopingVlanResetData,
       "igmpSnoopingVlanResetControl": igmpSnoopingVlanResetControl,
       "igmpSnoopingDataPortTable": igmpSnoopingDataPortTable,
       "igmpSnoopingDataPortEntry": igmpSnoopingDataPortEntry,
       "igmpSnoopingDataPortVlanId": igmpSnoopingDataPortVlanId,
       "igmpSnoopingDataPortNumber": igmpSnoopingDataPortNumber,
       "igmpSnoopingDataPortGroup": igmpSnoopingDataPortGroup,
       "igmpSnoopingDataPortIpAddr": igmpSnoopingDataPortIpAddr,
       "igmpSnoopingDataPortState": igmpSnoopingDataPortState,
       "igmpSnoopingControlPortTable": igmpSnoopingControlPortTable,
       "igmpSnoopingControlPortEntry": igmpSnoopingControlPortEntry,
       "igmpSnoopingControlPortVlanId": igmpSnoopingControlPortVlanId,
       "igmpSnoopingControlPortNumber": igmpSnoopingControlPortNumber,
       "igmpSnoopingControlPortState": igmpSnoopingControlPortState,
       "igmpSnoopingControlPortRowStatus": igmpSnoopingControlPortRowStatus,
       "igmpSnoopingStatusTable": igmpSnoopingStatusTable,
       "igmpSnoopingStatusEntry": igmpSnoopingStatusEntry,
       "igmpSnoopingVlanId": igmpSnoopingVlanId,
       "igmpSnoopingMcastMacAddr": igmpSnoopingMcastMacAddr,
       "igmpSnoopingPort": igmpSnoopingPort,
       "igmpSnoopingIpStatusTable": igmpSnoopingIpStatusTable,
       "igmpSnoopingIpStatusEntry": igmpSnoopingIpStatusEntry,
       "igmpSnoopingIpVlanId": igmpSnoopingIpVlanId,
       "igmpSnoopingIpMcastMacAddr": igmpSnoopingIpMcastMacAddr,
       "igmpSnoopingIpAddress": igmpSnoopingIpAddress,
       "pvstpGroup": pvstpGroup,
       "pvstpTable": pvstpTable,
       "pvstpEntry": pvstpEntry,
       "pvstpVlanId": pvstpVlanId,
       "pvstpProtocolSpecification": pvstpProtocolSpecification,
       "pvstpPriority": pvstpPriority,
       "pvstpTimeSinceTopologyChange": pvstpTimeSinceTopologyChange,
       "pvstpTopChanges": pvstpTopChanges,
       "pvstpDesignatedRoot": pvstpDesignatedRoot,
       "pvstpRootCost": pvstpRootCost,
       "pvstpRootPort": pvstpRootPort,
       "pvstpMaxAge": pvstpMaxAge,
       "pvstpHelloTime": pvstpHelloTime,
       "pvstpHoldTime": pvstpHoldTime,
       "pvstpForwardDelay": pvstpForwardDelay,
       "pvstpBridgeMaxAge": pvstpBridgeMaxAge,
       "pvstpBridgeHelloTime": pvstpBridgeHelloTime,
       "pvstpBridgeForwardDelay": pvstpBridgeForwardDelay,
       "pvstpBridgeRapid": pvstpBridgeRapid,
       "pvstpBridgeId": pvstpBridgeId,
       "pvstpPortTable": pvstpPortTable,
       "pvstpPortEntry": pvstpPortEntry,
       "pvstpPortVlanId": pvstpPortVlanId,
       "pvstpPort": pvstpPort,
       "pvstpPortPriority": pvstpPortPriority,
       "pvstpPortState": pvstpPortState,
       "pvstpPortEnable": pvstpPortEnable,
       "pvstpPortPathCost": pvstpPortPathCost,
       "pvstpPortDesignatedRoot": pvstpPortDesignatedRoot,
       "pvstpPortDesignatedCost": pvstpPortDesignatedCost,
       "pvstpPortDesignatedBridge": pvstpPortDesignatedBridge,
       "pvstpPortDesignatedPort": pvstpPortDesignatedPort,
       "pvstpPortForwardTransitions": pvstpPortForwardTransitions,
       "pvstpPortQuick": pvstpPortQuick,
       "pvstpPortAuto": pvstpPortAuto,
       "relayGroup": relayGroup,
       "relayEnable": relayEnable,
       "relayMaxHops": relayMaxHops,
       "relayServerTable": relayServerTable,
       "relayServerEntry": relayServerEntry,
       "relayServerIndex": relayServerIndex,
       "relayServerAddress": relayServerAddress,
       "portMirrorGroup": portMirrorGroup,
       "portMirrorTable": portMirrorTable,
       "portMirrorEntry": portMirrorEntry,
       "portMirrorSourcePort": portMirrorSourcePort,
       "portMirrorMonitorPort": portMirrorMonitorPort,
       "portMirrorRowStatus": portMirrorRowStatus,
       "ipAccessCtlGroup": ipAccessCtlGroup,
       "ipAccessCtlTable": ipAccessCtlTable,
       "ipAccessCtlEntry": ipAccessCtlEntry,
       "ipAccessCtlRuleNumber": ipAccessCtlRuleNumber,
       "ipAccessCtlSourceAddress": ipAccessCtlSourceAddress,
       "ipAccessCtlSourceMask": ipAccessCtlSourceMask,
       "ipAccessCtlDestinationAddress": ipAccessCtlDestinationAddress,
       "ipAccessCtlDestinationMask": ipAccessCtlDestinationMask,
       "ipAccessCtlType": ipAccessCtlType,
       "ipAccessCtlRowStatus": ipAccessCtlRowStatus,
       "ipAccessCtlEnable": ipAccessCtlEnable,
       "fdbGroup": fdbGroup,
       "fdbLearningMode": fdbLearningMode,
       "fdbAgeTable": fdbAgeTable,
       "fdbAgeEntry": fdbAgeEntry,
       "fdbAgeId": fdbAgeId,
       "fdbAgeStatus": fdbAgeStatus,
       "fdbAgeTime": fdbAgeTime}
)
