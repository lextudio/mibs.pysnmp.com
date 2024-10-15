# SNMP MIB module (UC4Vers2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UC4Vers2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:19 2024
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

uc4Vers2_module = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
uc4Vers2_module.setRevisions(
        ("2009-03-09 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sbb_ObjectIdentity = ObjectIdentity
sbb = _Sbb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562)
)
_Uc4_ObjectIdentity = ObjectIdentity
uc4 = _Uc4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1)
)
_Vers1_ObjectIdentity = ObjectIdentity
vers1 = _Vers1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1)
)
_AgentData_ObjectIdentity = ObjectIdentity
agentData = _AgentData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 1)
)


class _AgentVersion_Type(DisplayString):
    """Custom type agentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentVersion_Type.__name__ = "DisplayString"
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 1, 1),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("current")


class _AgentStartTime_Type(DisplayString):
    """Custom type agentStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgentStartTime_Type.__name__ = "DisplayString"
_AgentStartTime_Object = MibScalar
agentStartTime = _AgentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 1, 2),
    _AgentStartTime_Type()
)
agentStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStartTime.setStatus("current")
_AgentNumberOfServerTasks_Type = Integer32
_AgentNumberOfServerTasks_Object = MibScalar
agentNumberOfServerTasks = _AgentNumberOfServerTasks_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 1, 3),
    _AgentNumberOfServerTasks_Type()
)
agentNumberOfServerTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNumberOfServerTasks.setStatus("current")
_AgentConnectCounter_Type = Integer32
_AgentConnectCounter_Object = MibScalar
agentConnectCounter = _AgentConnectCounter_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 1, 4),
    _AgentConnectCounter_Type()
)
agentConnectCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConnectCounter.setStatus("current")
_AgentControl_ObjectIdentity = ObjectIdentity
agentControl = _AgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 2)
)
_AgentWork_ObjectIdentity = ObjectIdentity
agentWork = _AgentWork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3)
)


class _AgentWorkSysID_Type(DisplayString):
    """Custom type agentWorkSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AgentWorkSysID_Type.__name__ = "DisplayString"
_AgentWorkSysID_Object = MibScalar
agentWorkSysID = _AgentWorkSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 1),
    _AgentWorkSysID_Type()
)
agentWorkSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkSysID.setStatus("current")


class _AgentWorkObject_Type(DisplayString):
    """Custom type agentWorkObject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkObject_Type.__name__ = "DisplayString"
_AgentWorkObject_Object = MibScalar
agentWorkObject = _AgentWorkObject_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 2),
    _AgentWorkObject_Type()
)
agentWorkObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkObject.setStatus("current")


class _AgentWorkString1_Type(DisplayString):
    """Custom type agentWorkString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkString1_Type.__name__ = "DisplayString"
_AgentWorkString1_Object = MibScalar
agentWorkString1 = _AgentWorkString1_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 3),
    _AgentWorkString1_Type()
)
agentWorkString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkString1.setStatus("current")


class _AgentWorkString2_Type(DisplayString):
    """Custom type agentWorkString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkString2_Type.__name__ = "DisplayString"
_AgentWorkString2_Object = MibScalar
agentWorkString2 = _AgentWorkString2_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 4),
    _AgentWorkString2_Type()
)
agentWorkString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkString2.setStatus("current")


class _AgentWorkString3_Type(DisplayString):
    """Custom type agentWorkString3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkString3_Type.__name__ = "DisplayString"
_AgentWorkString3_Object = MibScalar
agentWorkString3 = _AgentWorkString3_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 5),
    _AgentWorkString3_Type()
)
agentWorkString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkString3.setStatus("current")


class _AgentWorkString4_Type(DisplayString):
    """Custom type agentWorkString4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkString4_Type.__name__ = "DisplayString"
_AgentWorkString4_Object = MibScalar
agentWorkString4 = _AgentWorkString4_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 6),
    _AgentWorkString4_Type()
)
agentWorkString4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkString4.setStatus("current")


class _AgentWorkString5_Type(DisplayString):
    """Custom type agentWorkString5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentWorkString5_Type.__name__ = "DisplayString"
_AgentWorkString5_Object = MibScalar
agentWorkString5 = _AgentWorkString5_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 7),
    _AgentWorkString5_Type()
)
agentWorkString5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkString5.setStatus("current")
_AgentWorkInteger1_Type = Integer32
_AgentWorkInteger1_Object = MibScalar
agentWorkInteger1 = _AgentWorkInteger1_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 8),
    _AgentWorkInteger1_Type()
)
agentWorkInteger1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkInteger1.setStatus("current")
_AgentWorkInteger2_Type = Integer32
_AgentWorkInteger2_Object = MibScalar
agentWorkInteger2 = _AgentWorkInteger2_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 9),
    _AgentWorkInteger2_Type()
)
agentWorkInteger2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkInteger2.setStatus("current")
_AgentWorkInteger3_Type = Integer32
_AgentWorkInteger3_Object = MibScalar
agentWorkInteger3 = _AgentWorkInteger3_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 10),
    _AgentWorkInteger3_Type()
)
agentWorkInteger3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkInteger3.setStatus("current")
_AgentWorkInteger4_Type = Integer32
_AgentWorkInteger4_Object = MibScalar
agentWorkInteger4 = _AgentWorkInteger4_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 11),
    _AgentWorkInteger4_Type()
)
agentWorkInteger4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkInteger4.setStatus("current")
_AgentWorkInteger5_Type = Integer32
_AgentWorkInteger5_Object = MibScalar
agentWorkInteger5 = _AgentWorkInteger5_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 3, 12),
    _AgentWorkInteger5_Type()
)
agentWorkInteger5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentWorkInteger5.setStatus("current")
_Uc4system_ObjectIdentity = ObjectIdentity
uc4system = _Uc4system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4)
)
_SystemTable_Object = MibTable
systemTable = _SystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    systemTable.setStatus("current")
_SystemEntry_Object = MibTableRow
systemEntry = _SystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1)
)
systemEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "sysSysID"),
)
if mibBuilder.loadTexts:
    systemEntry.setStatus("current")


class _SysSysID_Type(DisplayString):
    """Custom type sysSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysSysID_Type.__name__ = "DisplayString"
_SysSysID_Object = MibTableColumn
sysSysID = _SysSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 1),
    _SysSysID_Type()
)
sysSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSysID.setStatus("current")


class _SysStartTime_Type(DisplayString):
    """Custom type sysStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_SysStartTime_Type.__name__ = "DisplayString"
_SysStartTime_Object = MibTableColumn
sysStartTime = _SysStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 2),
    _SysStartTime_Type()
)
sysStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStartTime.setStatus("current")


class _SysDbmsName_Type(DisplayString):
    """Custom type sysDbmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysDbmsName_Type.__name__ = "DisplayString"
_SysDbmsName_Object = MibTableColumn
sysDbmsName = _SysDbmsName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 3),
    _SysDbmsName_Type()
)
sysDbmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDbmsName.setStatus("current")


class _SysDbVersion_Type(DisplayString):
    """Custom type sysDbVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysDbVersion_Type.__name__ = "DisplayString"
_SysDbVersion_Object = MibTableColumn
sysDbVersion = _SysDbVersion_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 4),
    _SysDbVersion_Type()
)
sysDbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDbVersion.setStatus("current")


class _SysDbName_Type(DisplayString):
    """Custom type sysDbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysDbName_Type.__name__ = "DisplayString"
_SysDbName_Object = MibTableColumn
sysDbName = _SysDbName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 5),
    _SysDbName_Type()
)
sysDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDbName.setStatus("current")
_SysEMS_Type = Integer32
_SysEMS_Object = MibTableColumn
sysEMS = _SysEMS_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 4, 1, 1, 6),
    _SysEMS_Type()
)
sysEMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEMS.setStatus("current")
_Client_ObjectIdentity = ObjectIdentity
client = _Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5)
)
_ClientTable_Object = MibTable
clientTable = _ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clientTable.setStatus("current")
_ClientEntry_Object = MibTableRow
clientEntry = _ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1)
)
clientEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "cliSysID"),
    (0, "UC4Vers2-MIB", "cliClient"),
)
if mibBuilder.loadTexts:
    clientEntry.setStatus("current")


class _CliSysID_Type(DisplayString):
    """Custom type cliSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CliSysID_Type.__name__ = "DisplayString"
_CliSysID_Object = MibTableColumn
cliSysID = _CliSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 1),
    _CliSysID_Type()
)
cliSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliSysID.setStatus("current")


class _CliClient_Type(Integer32):
    """Custom type cliClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CliClient_Type.__name__ = "Integer32"
_CliClient_Object = MibTableColumn
cliClient = _CliClient_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 2),
    _CliClient_Type()
)
cliClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliClient.setStatus("current")


class _CliLastModifyTime_Type(DisplayString):
    """Custom type cliLastModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_CliLastModifyTime_Type.__name__ = "DisplayString"
_CliLastModifyTime_Object = MibTableColumn
cliLastModifyTime = _CliLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 3),
    _CliLastModifyTime_Type()
)
cliLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliLastModifyTime.setStatus("current")


class _CliState_Type(Integer32):
    """Custom type cliState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("go", 1),
          ("stop", 2))
    )


_CliState_Type.__name__ = "Integer32"
_CliState_Object = MibTableColumn
cliState = _CliState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 4),
    _CliState_Type()
)
cliState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliState.setStatus("current")


class _CliMonitoring_Type(Integer32):
    """Custom type cliMonitoring based on Integer32"""
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


_CliMonitoring_Type.__name__ = "Integer32"
_CliMonitoring_Object = MibTableColumn
cliMonitoring = _CliMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 5),
    _CliMonitoring_Type()
)
cliMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliMonitoring.setStatus("current")


class _CliInfo_Type(DisplayString):
    """Custom type cliInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_CliInfo_Type.__name__ = "DisplayString"
_CliInfo_Object = MibTableColumn
cliInfo = _CliInfo_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 5, 1, 1, 6),
    _CliInfo_Type()
)
cliInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliInfo.setStatus("current")
_ServerInstance_ObjectIdentity = ObjectIdentity
serverInstance = _ServerInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6)
)
_ServerInstanceTable_Object = MibTable
serverInstanceTable = _ServerInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    serverInstanceTable.setStatus("current")
_ServerInstanceEntry_Object = MibTableRow
serverInstanceEntry = _ServerInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1)
)
serverInstanceEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "srvSysID"),
    (0, "UC4Vers2-MIB", "srvName"),
)
if mibBuilder.loadTexts:
    serverInstanceEntry.setStatus("current")


class _SrvSysID_Type(DisplayString):
    """Custom type srvSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SrvSysID_Type.__name__ = "DisplayString"
_SrvSysID_Object = MibTableColumn
srvSysID = _SrvSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 1),
    _SrvSysID_Type()
)
srvSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvSysID.setStatus("current")


class _SrvName_Type(DisplayString):
    """Custom type srvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SrvName_Type.__name__ = "DisplayString"
_SrvName_Object = MibTableColumn
srvName = _SrvName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 2),
    _SrvName_Type()
)
srvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvName.setStatus("current")


class _SrvLastModifyTime_Type(DisplayString):
    """Custom type srvLastModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_SrvLastModifyTime_Type.__name__ = "DisplayString"
_SrvLastModifyTime_Object = MibTableColumn
srvLastModifyTime = _SrvLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 3),
    _SrvLastModifyTime_Type()
)
srvLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLastModifyTime.setStatus("current")


class _SrvVersion_Type(DisplayString):
    """Custom type srvVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_SrvVersion_Type.__name__ = "DisplayString"
_SrvVersion_Object = MibTableColumn
srvVersion = _SrvVersion_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 4),
    _SrvVersion_Type()
)
srvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvVersion.setStatus("current")


class _SrvStartTime_Type(DisplayString):
    """Custom type srvStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SrvStartTime_Type.__name__ = "DisplayString"
_SrvStartTime_Object = MibTableColumn
srvStartTime = _SrvStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 5),
    _SrvStartTime_Type()
)
srvStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvStartTime.setStatus("current")


class _SrvState_Type(Integer32):
    """Custom type srvState based on Integer32"""
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
        *(("abnormal", 3),
          ("ended", 2),
          ("run", 1),
          ("undef", 4))
    )


_SrvState_Type.__name__ = "Integer32"
_SrvState_Object = MibTableColumn
srvState = _SrvState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 6),
    _SrvState_Type()
)
srvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvState.setStatus("current")
_SrvSrvConnect_Type = Integer32
_SrvSrvConnect_Object = MibTableColumn
srvSrvConnect = _SrvSrvConnect_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 7),
    _SrvSrvConnect_Type()
)
srvSrvConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvSrvConnect.setStatus("current")
_SrvExeConnect_Type = Integer32
_SrvExeConnect_Object = MibTableColumn
srvExeConnect = _SrvExeConnect_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 8),
    _SrvExeConnect_Type()
)
srvExeConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvExeConnect.setStatus("current")
_SrvDiaConnect_Type = Integer32
_SrvDiaConnect_Object = MibTableColumn
srvDiaConnect = _SrvDiaConnect_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 9),
    _SrvDiaConnect_Type()
)
srvDiaConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDiaConnect.setStatus("current")


class _SrvBusyMin_Type(Integer32):
    """Custom type srvBusyMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SrvBusyMin_Type.__name__ = "Integer32"
_SrvBusyMin_Object = MibTableColumn
srvBusyMin = _SrvBusyMin_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 10),
    _SrvBusyMin_Type()
)
srvBusyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBusyMin.setStatus("current")


class _SrvBusy10Min_Type(Integer32):
    """Custom type srvBusy10Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SrvBusy10Min_Type.__name__ = "Integer32"
_SrvBusy10Min_Object = MibTableColumn
srvBusy10Min = _SrvBusy10Min_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 11),
    _SrvBusy10Min_Type()
)
srvBusy10Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBusy10Min.setStatus("current")


class _SrvBusyHour_Type(Integer32):
    """Custom type srvBusyHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SrvBusyHour_Type.__name__ = "Integer32"
_SrvBusyHour_Object = MibTableColumn
srvBusyHour = _SrvBusyHour_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 12),
    _SrvBusyHour_Type()
)
srvBusyHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBusyHour.setStatus("current")


class _SrvRunMode_Type(Integer32):
    """Custom type srvRunMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("standby", 2),
          ("undef", 3))
    )


_SrvRunMode_Type.__name__ = "Integer32"
_SrvRunMode_Object = MibTableColumn
srvRunMode = _SrvRunMode_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 13),
    _SrvRunMode_Type()
)
srvRunMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvRunMode.setStatus("current")


class _SrvDBState_Type(Integer32):
    """Custom type srvDBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("undef", 3))
    )


_SrvDBState_Type.__name__ = "Integer32"
_SrvDBState_Object = MibTableColumn
srvDBState = _SrvDBState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 14),
    _SrvDBState_Type()
)
srvDBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDBState.setStatus("current")


class _SrvSDBState_Type(Integer32):
    """Custom type srvSDBState based on Integer32"""
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
        *(("dismounted", 3),
          ("noSDB", 4),
          ("offline", 2),
          ("online", 1))
    )


_SrvSDBState_Type.__name__ = "Integer32"
_SrvSDBState_Object = MibTableColumn
srvSDBState = _SrvSDBState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 6, 1, 1, 15),
    _SrvSDBState_Type()
)
srvSDBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvSDBState.setStatus("current")
_Executor_ObjectIdentity = ObjectIdentity
executor = _Executor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7)
)
_ExecutorTable_Object = MibTable
executorTable = _ExecutorTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    executorTable.setStatus("current")
_ExecutorEntry_Object = MibTableRow
executorEntry = _ExecutorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1)
)
executorEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "exeSysID"),
    (0, "UC4Vers2-MIB", "exeSrvName"),
    (0, "UC4Vers2-MIB", "exeName"),
    (0, "UC4Vers2-MIB", "exeType"),
)
if mibBuilder.loadTexts:
    executorEntry.setStatus("current")


class _ExeSysID_Type(DisplayString):
    """Custom type exeSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeSysID_Type.__name__ = "DisplayString"
_ExeSysID_Object = MibTableColumn
exeSysID = _ExeSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 1),
    _ExeSysID_Type()
)
exeSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeSysID.setStatus("current")


class _ExeSrvName_Type(DisplayString):
    """Custom type exeSrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeSrvName_Type.__name__ = "DisplayString"
_ExeSrvName_Object = MibTableColumn
exeSrvName = _ExeSrvName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 2),
    _ExeSrvName_Type()
)
exeSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeSrvName.setStatus("current")


class _ExeName_Type(DisplayString):
    """Custom type exeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeName_Type.__name__ = "DisplayString"
_ExeName_Object = MibTableColumn
exeName = _ExeName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 3),
    _ExeName_Type()
)
exeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeName.setStatus("current")


class _ExeType_Type(DisplayString):
    """Custom type exeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeType_Type.__name__ = "DisplayString"
_ExeType_Object = MibTableColumn
exeType = _ExeType_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 4),
    _ExeType_Type()
)
exeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeType.setStatus("current")


class _ExeLastModifyTime_Type(DisplayString):
    """Custom type exeLastModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExeLastModifyTime_Type.__name__ = "DisplayString"
_ExeLastModifyTime_Object = MibTableColumn
exeLastModifyTime = _ExeLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 5),
    _ExeLastModifyTime_Type()
)
exeLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeLastModifyTime.setStatus("current")


class _ExeHost_Type(DisplayString):
    """Custom type exeHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeHost_Type.__name__ = "DisplayString"
_ExeHost_Object = MibTableColumn
exeHost = _ExeHost_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 6),
    _ExeHost_Type()
)
exeHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeHost.setStatus("current")


class _ExeVersion_Type(DisplayString):
    """Custom type exeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ExeVersion_Type.__name__ = "DisplayString"
_ExeVersion_Object = MibTableColumn
exeVersion = _ExeVersion_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 7),
    _ExeVersion_Type()
)
exeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeVersion.setStatus("current")


class _ExeHardware_Type(DisplayString):
    """Custom type exeHardware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExeHardware_Type.__name__ = "DisplayString"
_ExeHardware_Object = MibTableColumn
exeHardware = _ExeHardware_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 8),
    _ExeHardware_Type()
)
exeHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeHardware.setStatus("current")


class _ExeSoftware_Type(DisplayString):
    """Custom type exeSoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExeSoftware_Type.__name__ = "DisplayString"
_ExeSoftware_Object = MibTableColumn
exeSoftware = _ExeSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 9),
    _ExeSoftware_Type()
)
exeSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeSoftware.setStatus("current")


class _ExeSoftwareVers_Type(DisplayString):
    """Custom type exeSoftwareVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExeSoftwareVers_Type.__name__ = "DisplayString"
_ExeSoftwareVers_Object = MibTableColumn
exeSoftwareVers = _ExeSoftwareVers_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 10),
    _ExeSoftwareVers_Type()
)
exeSoftwareVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeSoftwareVers.setStatus("current")


class _ExeJCLTyp_Type(DisplayString):
    """Custom type exeJCLTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExeJCLTyp_Type.__name__ = "DisplayString"
_ExeJCLTyp_Object = MibTableColumn
exeJCLTyp = _ExeJCLTyp_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 11),
    _ExeJCLTyp_Type()
)
exeJCLTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeJCLTyp.setStatus("current")


class _ExeConnTime_Type(DisplayString):
    """Custom type exeConnTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExeConnTime_Type.__name__ = "DisplayString"
_ExeConnTime_Object = MibTableColumn
exeConnTime = _ExeConnTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 12),
    _ExeConnTime_Type()
)
exeConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeConnTime.setStatus("current")


class _ExeState_Type(Integer32):
    """Custom type exeState based on Integer32"""
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
        *(("ended", 2),
          ("lost", 3),
          ("run", 1),
          ("timeout", 4),
          ("undef", 5))
    )


_ExeState_Type.__name__ = "Integer32"
_ExeState_Object = MibTableColumn
exeState = _ExeState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 13),
    _ExeState_Type()
)
exeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeState.setStatus("current")


class _ExeLastPing_Type(DisplayString):
    """Custom type exeLastPing based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExeLastPing_Type.__name__ = "DisplayString"
_ExeLastPing_Object = MibTableColumn
exeLastPing = _ExeLastPing_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 14),
    _ExeLastPing_Type()
)
exeLastPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeLastPing.setStatus("current")


class _ExeMonitoring_Type(Integer32):
    """Custom type exeMonitoring based on Integer32"""
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


_ExeMonitoring_Type.__name__ = "Integer32"
_ExeMonitoring_Object = MibTableColumn
exeMonitoring = _ExeMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 15),
    _ExeMonitoring_Type()
)
exeMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeMonitoring.setStatus("current")


class _ExeInfo_Type(DisplayString):
    """Custom type exeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExeInfo_Type.__name__ = "DisplayString"
_ExeInfo_Object = MibTableColumn
exeInfo = _ExeInfo_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 7, 1, 1, 16),
    _ExeInfo_Type()
)
exeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exeInfo.setStatus("current")
_BlockingPoints_ObjectIdentity = ObjectIdentity
blockingPoints = _BlockingPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8)
)
_BlockingPointsTable_Object = MibTable
blockingPointsTable = _BlockingPointsTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    blockingPointsTable.setStatus("current")
_BlockingPointEntry_Object = MibTableRow
blockingPointEntry = _BlockingPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1)
)
blockingPointEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "blkSysID"),
    (0, "UC4Vers2-MIB", "blkClient"),
    (0, "UC4Vers2-MIB", "blkJPRunNr"),
    (0, "UC4Vers2-MIB", "blkJPLNR"),
)
if mibBuilder.loadTexts:
    blockingPointEntry.setStatus("current")


class _BlkSysID_Type(DisplayString):
    """Custom type blkSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BlkSysID_Type.__name__ = "DisplayString"
_BlkSysID_Object = MibTableColumn
blkSysID = _BlkSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 1),
    _BlkSysID_Type()
)
blkSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkSysID.setStatus("current")


class _BlkClient_Type(Integer32):
    """Custom type blkClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BlkClient_Type.__name__ = "Integer32"
_BlkClient_Object = MibTableColumn
blkClient = _BlkClient_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 2),
    _BlkClient_Type()
)
blkClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkClient.setStatus("current")


class _BlkJPRunNr_Type(Integer32):
    """Custom type blkJPRunNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65635),
    )


_BlkJPRunNr_Type.__name__ = "Integer32"
_BlkJPRunNr_Object = MibTableColumn
blkJPRunNr = _BlkJPRunNr_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 3),
    _BlkJPRunNr_Type()
)
blkJPRunNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkJPRunNr.setStatus("current")


class _BlkJPLNR_Type(Integer32):
    """Custom type blkJPLNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BlkJPLNR_Type.__name__ = "Integer32"
_BlkJPLNR_Object = MibTableColumn
blkJPLNR = _BlkJPLNR_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 4),
    _BlkJPLNR_Type()
)
blkJPLNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkJPLNR.setStatus("current")


class _BlkLastModifyTime_Type(DisplayString):
    """Custom type blkLastModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_BlkLastModifyTime_Type.__name__ = "DisplayString"
_BlkLastModifyTime_Object = MibTableColumn
blkLastModifyTime = _BlkLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 5),
    _BlkLastModifyTime_Type()
)
blkLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkLastModifyTime.setStatus("current")


class _BlkJPName_Type(DisplayString):
    """Custom type blkJPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_BlkJPName_Type.__name__ = "DisplayString"
_BlkJPName_Object = MibTableColumn
blkJPName = _BlkJPName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 6),
    _BlkJPName_Type()
)
blkJPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkJPName.setStatus("current")


class _BlkObjTyp_Type(DisplayString):
    """Custom type blkObjTyp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BlkObjTyp_Type.__name__ = "DisplayString"
_BlkObjTyp_Object = MibTableColumn
blkObjTyp = _BlkObjTyp_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 7),
    _BlkObjTyp_Type()
)
blkObjTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkObjTyp.setStatus("current")


class _BlkObjName_Type(DisplayString):
    """Custom type blkObjName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_BlkObjName_Type.__name__ = "DisplayString"
_BlkObjName_Object = MibTableColumn
blkObjName = _BlkObjName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 8),
    _BlkObjName_Type()
)
blkObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkObjName.setStatus("current")
_BlkObjRunNr_Type = Integer32
_BlkObjRunNr_Object = MibTableColumn
blkObjRunNr = _BlkObjRunNr_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 8, 1, 1, 9),
    _BlkObjRunNr_Type()
)
blkObjRunNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blkObjRunNr.setStatus("current")
_CallOperator_ObjectIdentity = ObjectIdentity
callOperator = _CallOperator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9)
)
_CallOperatorTable_Object = MibTable
callOperatorTable = _CallOperatorTable_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    callOperatorTable.setStatus("current")
_CallOperatorEntry_Object = MibTableRow
callOperatorEntry = _CallOperatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1)
)
callOperatorEntry.setIndexNames(
    (0, "UC4Vers2-MIB", "coSysID"),
    (0, "UC4Vers2-MIB", "coClient"),
    (0, "UC4Vers2-MIB", "coRunNr"),
)
if mibBuilder.loadTexts:
    callOperatorEntry.setStatus("current")


class _CoSysID_Type(DisplayString):
    """Custom type coSysID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CoSysID_Type.__name__ = "DisplayString"
_CoSysID_Object = MibTableColumn
coSysID = _CoSysID_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 1),
    _CoSysID_Type()
)
coSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coSysID.setStatus("current")


class _CoClient_Type(Integer32):
    """Custom type coClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CoClient_Type.__name__ = "Integer32"
_CoClient_Object = MibTableColumn
coClient = _CoClient_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 2),
    _CoClient_Type()
)
coClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coClient.setStatus("current")


class _CoRunNr_Type(Integer32):
    """Custom type coRunNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65635),
    )


_CoRunNr_Type.__name__ = "Integer32"
_CoRunNr_Object = MibTableColumn
coRunNr = _CoRunNr_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 3),
    _CoRunNr_Type()
)
coRunNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coRunNr.setStatus("current")


class _CoLastModifyTime_Type(DisplayString):
    """Custom type coLastModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_CoLastModifyTime_Type.__name__ = "DisplayString"
_CoLastModifyTime_Object = MibTableColumn
coLastModifyTime = _CoLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 4),
    _CoLastModifyTime_Type()
)
coLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coLastModifyTime.setStatus("current")


class _CoName_Type(DisplayString):
    """Custom type coName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CoName_Type.__name__ = "DisplayString"
_CoName_Object = MibTableColumn
coName = _CoName_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 5),
    _CoName_Type()
)
coName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coName.setStatus("current")


class _CoTyp_Type(Integer32):
    """Custom type coTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("message", 2),
          ("question", 1))
    )


_CoTyp_Type.__name__ = "Integer32"
_CoTyp_Object = MibTableColumn
coTyp = _CoTyp_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 6),
    _CoTyp_Type()
)
coTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTyp.setStatus("current")


class _CoText_Type(DisplayString):
    """Custom type coText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CoText_Type.__name__ = "DisplayString"
_CoText_Object = MibTableColumn
coText = _CoText_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 7),
    _CoText_Type()
)
coText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coText.setStatus("current")
_CoState_Type = Integer32
_CoState_Object = MibTableColumn
coState = _CoState_Object(
    (1, 3, 6, 1, 4, 1, 2562, 1, 1, 9, 1, 1, 8),
    _CoState_Type()
)
coState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coState.setStatus("current")

# Managed Objects groups


# Notification objects

serverStarted = NotificationType(
    (3400,)
)
serverStarted.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkInteger1"),
        ("UC4Vers2-MIB", "agentWorkInteger2"))
)
if mibBuilder.loadTexts:
    serverStarted.setStatus(
        "current"
    )

serverEnd = NotificationType(
    (3401,)
)
serverEnd.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkInteger1"),
        ("UC4Vers2-MIB", "agentWorkInteger2"))
)
if mibBuilder.loadTexts:
    serverEnd.setStatus(
        "current"
    )

primaryWorkProcessAborted = NotificationType(
    (3410,)
)
primaryWorkProcessAborted.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkInteger1"),
        ("UC4Vers2-MIB", "agentWorkInteger2"))
)
if mibBuilder.loadTexts:
    primaryWorkProcessAborted.setStatus(
        "current"
    )

databaseError = NotificationType(
    (3536,)
)
databaseError.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"))
)
if mibBuilder.loadTexts:
    databaseError.setStatus(
        "current"
    )

databaseReconnect = NotificationType(
    (3538,)
)
databaseReconnect.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"))
)
if mibBuilder.loadTexts:
    databaseReconnect.setStatus(
        "current"
    )

agentStop = NotificationType(
    (11603,)
)
agentStop.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    agentStop.setStatus(
        "current"
    )

agentStart = NotificationType(
    (11604,)
)
agentStart.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    agentStart.setStatus(
        "current"
    )

agentReset = NotificationType(
    (11622,)
)
agentReset.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"))
)
if mibBuilder.loadTexts:
    agentReset.setStatus(
        "current"
    )

agentDisconnected = NotificationType(
    (11650,)
)
agentDisconnected.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    agentDisconnected.setStatus(
        "current"
    )

agentSAPDisconnected = NotificationType(
    (11652,)
)
agentSAPDisconnected.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    agentSAPDisconnected.setStatus(
        "current"
    )

agentSAPReconnect = NotificationType(
    (11662,)
)
agentSAPReconnect.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    agentSAPReconnect.setStatus(
        "current"
    )

systemError = NotificationType(
    (11801,)
)
systemError.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    systemError.setStatus(
        "current"
    )

serverPWPchanged = NotificationType(
    (11818,)
)
serverPWPchanged.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkInteger1"),
        ("UC4Vers2-MIB", "agentWorkInteger2"))
)
if mibBuilder.loadTexts:
    serverPWPchanged.setStatus(
        "current"
    )

notificationMessage = NotificationType(
    (801450,)
)
notificationMessage.setObjects(
      *(("UC4Vers2-MIB", "agentWorkSysID"),
        ("UC4Vers2-MIB", "agentWorkObject"),
        ("UC4Vers2-MIB", "agentWorkString1"),
        ("UC4Vers2-MIB", "agentWorkString2"),
        ("UC4Vers2-MIB", "agentWorkInteger1"))
)
if mibBuilder.loadTexts:
    notificationMessage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UC4Vers2-MIB",
    **{"sbb": sbb,
       "uc4": uc4,
       "vers1": vers1,
       "agentData": agentData,
       "agentVersion": agentVersion,
       "agentStartTime": agentStartTime,
       "agentNumberOfServerTasks": agentNumberOfServerTasks,
       "agentConnectCounter": agentConnectCounter,
       "agentControl": agentControl,
       "agentWork": agentWork,
       "agentWorkSysID": agentWorkSysID,
       "agentWorkObject": agentWorkObject,
       "agentWorkString1": agentWorkString1,
       "agentWorkString2": agentWorkString2,
       "agentWorkString3": agentWorkString3,
       "agentWorkString4": agentWorkString4,
       "agentWorkString5": agentWorkString5,
       "agentWorkInteger1": agentWorkInteger1,
       "agentWorkInteger2": agentWorkInteger2,
       "agentWorkInteger3": agentWorkInteger3,
       "agentWorkInteger4": agentWorkInteger4,
       "agentWorkInteger5": agentWorkInteger5,
       "uc4system": uc4system,
       "systemTable": systemTable,
       "systemEntry": systemEntry,
       "sysSysID": sysSysID,
       "sysStartTime": sysStartTime,
       "sysDbmsName": sysDbmsName,
       "sysDbVersion": sysDbVersion,
       "sysDbName": sysDbName,
       "sysEMS": sysEMS,
       "client": client,
       "clientTable": clientTable,
       "clientEntry": clientEntry,
       "cliSysID": cliSysID,
       "cliClient": cliClient,
       "cliLastModifyTime": cliLastModifyTime,
       "cliState": cliState,
       "cliMonitoring": cliMonitoring,
       "cliInfo": cliInfo,
       "serverInstance": serverInstance,
       "serverInstanceTable": serverInstanceTable,
       "serverInstanceEntry": serverInstanceEntry,
       "srvSysID": srvSysID,
       "srvName": srvName,
       "srvLastModifyTime": srvLastModifyTime,
       "srvVersion": srvVersion,
       "srvStartTime": srvStartTime,
       "srvState": srvState,
       "srvSrvConnect": srvSrvConnect,
       "srvExeConnect": srvExeConnect,
       "srvDiaConnect": srvDiaConnect,
       "srvBusyMin": srvBusyMin,
       "srvBusy10Min": srvBusy10Min,
       "srvBusyHour": srvBusyHour,
       "srvRunMode": srvRunMode,
       "srvDBState": srvDBState,
       "srvSDBState": srvSDBState,
       "executor": executor,
       "executorTable": executorTable,
       "executorEntry": executorEntry,
       "exeSysID": exeSysID,
       "exeSrvName": exeSrvName,
       "exeName": exeName,
       "exeType": exeType,
       "exeLastModifyTime": exeLastModifyTime,
       "exeHost": exeHost,
       "exeVersion": exeVersion,
       "exeHardware": exeHardware,
       "exeSoftware": exeSoftware,
       "exeSoftwareVers": exeSoftwareVers,
       "exeJCLTyp": exeJCLTyp,
       "exeConnTime": exeConnTime,
       "exeState": exeState,
       "exeLastPing": exeLastPing,
       "exeMonitoring": exeMonitoring,
       "exeInfo": exeInfo,
       "blockingPoints": blockingPoints,
       "blockingPointsTable": blockingPointsTable,
       "blockingPointEntry": blockingPointEntry,
       "blkSysID": blkSysID,
       "blkClient": blkClient,
       "blkJPRunNr": blkJPRunNr,
       "blkJPLNR": blkJPLNR,
       "blkLastModifyTime": blkLastModifyTime,
       "blkJPName": blkJPName,
       "blkObjTyp": blkObjTyp,
       "blkObjName": blkObjName,
       "blkObjRunNr": blkObjRunNr,
       "callOperator": callOperator,
       "callOperatorTable": callOperatorTable,
       "callOperatorEntry": callOperatorEntry,
       "coSysID": coSysID,
       "coClient": coClient,
       "coRunNr": coRunNr,
       "coLastModifyTime": coLastModifyTime,
       "coName": coName,
       "coTyp": coTyp,
       "coText": coText,
       "coState": coState,
       "uc4Vers2-module": uc4Vers2_module,
       "serverStarted": serverStarted,
       "serverEnd": serverEnd,
       "primaryWorkProcessAborted": primaryWorkProcessAborted,
       "databaseError": databaseError,
       "databaseReconnect": databaseReconnect,
       "agentStop": agentStop,
       "agentStart": agentStart,
       "agentReset": agentReset,
       "agentDisconnected": agentDisconnected,
       "agentSAPDisconnected": agentSAPDisconnected,
       "agentSAPReconnect": agentSAPReconnect,
       "systemError": systemError,
       "serverPWPchanged": serverPWPchanged,
       "notificationMessage": notificationMessage}
)
