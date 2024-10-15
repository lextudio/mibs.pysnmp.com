# SNMP MIB module (SS7I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SS7I-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:40 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ss7i_ObjectIdentity = ObjectIdentity
ss7i = _Ss7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35)
)
_Ss7iCfg_ObjectIdentity = ObjectIdentity
ss7iCfg = _Ss7iCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1)
)
_Ss7iCfgTable_Object = MibTable
ss7iCfgTable = _Ss7iCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1)
)
if mibBuilder.loadTexts:
    ss7iCfgTable.setStatus("mandatory")
_Ss7iCfgEntry_Object = MibTableRow
ss7iCfgEntry = _Ss7iCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1)
)
ss7iCfgEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iCfgIndex"),
)
if mibBuilder.loadTexts:
    ss7iCfgEntry.setStatus("mandatory")
_Ss7iCfgIndex_Type = Integer32
_Ss7iCfgIndex_Object = MibTableColumn
ss7iCfgIndex = _Ss7iCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 1),
    _Ss7iCfgIndex_Type()
)
ss7iCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iCfgIndex.setStatus("mandatory")
_Ss7iCfgIpAddr_Type = IpAddress
_Ss7iCfgIpAddr_Object = MibTableColumn
ss7iCfgIpAddr = _Ss7iCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 2),
    _Ss7iCfgIpAddr_Type()
)
ss7iCfgIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgIpAddr.setStatus("mandatory")
_Ss7iCfgNetmask_Type = IpAddress
_Ss7iCfgNetmask_Object = MibTableColumn
ss7iCfgNetmask = _Ss7iCfgNetmask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 3),
    _Ss7iCfgNetmask_Type()
)
ss7iCfgNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgNetmask.setStatus("mandatory")
_Ss7iCfgDfltGwIpAddr_Type = IpAddress
_Ss7iCfgDfltGwIpAddr_Object = MibTableColumn
ss7iCfgDfltGwIpAddr = _Ss7iCfgDfltGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 4),
    _Ss7iCfgDfltGwIpAddr_Type()
)
ss7iCfgDfltGwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgDfltGwIpAddr.setStatus("mandatory")


class _Ss7iCfgProtocol_Type(Integer32):
    """Custom type ss7iCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("slapV2", 1)
    )


_Ss7iCfgProtocol_Type.__name__ = "Integer32"
_Ss7iCfgProtocol_Object = MibTableColumn
ss7iCfgProtocol = _Ss7iCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 5),
    _Ss7iCfgProtocol_Type()
)
ss7iCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgProtocol.setStatus("mandatory")


class _Ss7iCfgGwConnStartMethod_Type(Integer32):
    """Custom type ss7iCfgGwConnStartMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lsAuto", 1),
          ("lsManual", 2))
    )


_Ss7iCfgGwConnStartMethod_Type.__name__ = "Integer32"
_Ss7iCfgGwConnStartMethod_Object = MibTableColumn
ss7iCfgGwConnStartMethod = _Ss7iCfgGwConnStartMethod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 6),
    _Ss7iCfgGwConnStartMethod_Type()
)
ss7iCfgGwConnStartMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwConnStartMethod.setStatus("mandatory")
_Ss7iCfgGwIpAddr_Type = IpAddress
_Ss7iCfgGwIpAddr_Object = MibTableColumn
ss7iCfgGwIpAddr = _Ss7iCfgGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 7),
    _Ss7iCfgGwIpAddr_Type()
)
ss7iCfgGwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwIpAddr.setStatus("mandatory")
_Ss7iCfgGwPort_Type = Integer32
_Ss7iCfgGwPort_Object = MibTableColumn
ss7iCfgGwPort = _Ss7iCfgGwPort_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 8),
    _Ss7iCfgGwPort_Type()
)
ss7iCfgGwPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwPort.setStatus("mandatory")
_Ss7iCfgSecGwIpAddr_Type = IpAddress
_Ss7iCfgSecGwIpAddr_Object = MibTableColumn
ss7iCfgSecGwIpAddr = _Ss7iCfgSecGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 9),
    _Ss7iCfgSecGwIpAddr_Type()
)
ss7iCfgSecGwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgSecGwIpAddr.setStatus("mandatory")
_Ss7iCfgSecGwPort_Type = Integer32
_Ss7iCfgSecGwPort_Object = MibTableColumn
ss7iCfgSecGwPort = _Ss7iCfgSecGwPort_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 10),
    _Ss7iCfgSecGwPort_Type()
)
ss7iCfgSecGwPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgSecGwPort.setStatus("mandatory")


class _Ss7iCfgHrtbtTimerNearEnd_Type(Integer32):
    """Custom type ss7iCfgHrtbtTimerNearEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400000),
    )


_Ss7iCfgHrtbtTimerNearEnd_Type.__name__ = "Integer32"
_Ss7iCfgHrtbtTimerNearEnd_Object = MibTableColumn
ss7iCfgHrtbtTimerNearEnd = _Ss7iCfgHrtbtTimerNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 11),
    _Ss7iCfgHrtbtTimerNearEnd_Type()
)
ss7iCfgHrtbtTimerNearEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgHrtbtTimerNearEnd.setStatus("mandatory")


class _Ss7iCfgHrtbtTimerFarEnd_Type(Integer32):
    """Custom type ss7iCfgHrtbtTimerFarEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400000),
    )


_Ss7iCfgHrtbtTimerFarEnd_Type.__name__ = "Integer32"
_Ss7iCfgHrtbtTimerFarEnd_Object = MibTableColumn
ss7iCfgHrtbtTimerFarEnd = _Ss7iCfgHrtbtTimerFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 12),
    _Ss7iCfgHrtbtTimerFarEnd_Type()
)
ss7iCfgHrtbtTimerFarEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgHrtbtTimerFarEnd.setStatus("mandatory")


class _Ss7iCfgChassisId_Type(OctetString):
    """Custom type ss7iCfgChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Ss7iCfgChassisId_Type.__name__ = "OctetString"
_Ss7iCfgChassisId_Object = MibTableColumn
ss7iCfgChassisId = _Ss7iCfgChassisId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 13),
    _Ss7iCfgChassisId_Type()
)
ss7iCfgChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgChassisId.setStatus("mandatory")
_Ss7iCfgGwConnRetryCnt_Type = Integer32
_Ss7iCfgGwConnRetryCnt_Object = MibTableColumn
ss7iCfgGwConnRetryCnt = _Ss7iCfgGwConnRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 14),
    _Ss7iCfgGwConnRetryCnt_Type()
)
ss7iCfgGwConnRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwConnRetryCnt.setStatus("mandatory")
_Ss7iCfgGwConnRetryIntvl_Type = Integer32
_Ss7iCfgGwConnRetryIntvl_Object = MibTableColumn
ss7iCfgGwConnRetryIntvl = _Ss7iCfgGwConnRetryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 15),
    _Ss7iCfgGwConnRetryIntvl_Type()
)
ss7iCfgGwConnRetryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwConnRetryIntvl.setStatus("mandatory")
_Ss7iCfgGwMssdHrtbtThrsh_Type = Integer32
_Ss7iCfgGwMssdHrtbtThrsh_Object = MibTableColumn
ss7iCfgGwMssdHrtbtThrsh = _Ss7iCfgGwMssdHrtbtThrsh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 16),
    _Ss7iCfgGwMssdHrtbtThrsh_Type()
)
ss7iCfgGwMssdHrtbtThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCfgGwMssdHrtbtThrsh.setStatus("mandatory")
_Ss7iCmd_ObjectIdentity = ObjectIdentity
ss7iCmd = _Ss7iCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2)
)
_Ss7iCmdTable_Object = MibTable
ss7iCmdTable = _Ss7iCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1)
)
if mibBuilder.loadTexts:
    ss7iCmdTable.setStatus("mandatory")
_Ss7iCmdEntry_Object = MibTableRow
ss7iCmdEntry = _Ss7iCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1)
)
ss7iCmdEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iCmdIndex"),
)
if mibBuilder.loadTexts:
    ss7iCmdEntry.setStatus("mandatory")
_Ss7iCmdIndex_Type = Integer32
_Ss7iCmdIndex_Object = MibTableColumn
ss7iCmdIndex = _Ss7iCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 1),
    _Ss7iCmdIndex_Type()
)
ss7iCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iCmdIndex.setStatus("mandatory")


class _Ss7iCmdMgtStationId_Type(OctetString):
    """Custom type ss7iCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ss7iCmdMgtStationId_Type.__name__ = "OctetString"
_Ss7iCmdMgtStationId_Object = MibTableColumn
ss7iCmdMgtStationId = _Ss7iCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 2),
    _Ss7iCmdMgtStationId_Type()
)
ss7iCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCmdMgtStationId.setStatus("mandatory")
_Ss7iCmdReqId_Type = Integer32
_Ss7iCmdReqId_Object = MibTableColumn
ss7iCmdReqId = _Ss7iCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 3),
    _Ss7iCmdReqId_Type()
)
ss7iCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iCmdReqId.setStatus("mandatory")


class _Ss7iCmdFunction_Type(Integer32):
    """Custom type ss7iCmdFunction based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noCommand", 1),
          ("resetPbusCounters", 9),
          ("resetSS7Counters", 8),
          ("restoreFromDefault", 4),
          ("restoreFromNVRAM", 3),
          ("saveToNVRAM", 2),
          ("shutDownSS7GwConn", 7),
          ("softwareReset", 5),
          ("startPbusConnToAll", 10),
          ("startSS7GwConn", 6),
          ("stopPbusConnToAll", 11))
    )


_Ss7iCmdFunction_Type.__name__ = "Integer32"
_Ss7iCmdFunction_Object = MibTableColumn
ss7iCmdFunction = _Ss7iCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 4),
    _Ss7iCmdFunction_Type()
)
ss7iCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCmdFunction.setStatus("mandatory")


class _Ss7iCmdForce_Type(Integer32):
    """Custom type ss7iCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_Ss7iCmdForce_Type.__name__ = "Integer32"
_Ss7iCmdForce_Object = MibTableColumn
ss7iCmdForce = _Ss7iCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 5),
    _Ss7iCmdForce_Type()
)
ss7iCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCmdForce.setStatus("mandatory")
_Ss7iCmdParam_Type = OctetString
_Ss7iCmdParam_Object = MibTableColumn
ss7iCmdParam = _Ss7iCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 6),
    _Ss7iCmdParam_Type()
)
ss7iCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iCmdParam.setStatus("mandatory")


class _Ss7iCmdResult_Type(Integer32):
    """Custom type ss7iCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_Ss7iCmdResult_Type.__name__ = "Integer32"
_Ss7iCmdResult_Object = MibTableColumn
ss7iCmdResult = _Ss7iCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 7),
    _Ss7iCmdResult_Type()
)
ss7iCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iCmdResult.setStatus("mandatory")


class _Ss7iCmdCode_Type(Integer32):
    """Custom type ss7iCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              25,
              58,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_Ss7iCmdCode_Type.__name__ = "Integer32"
_Ss7iCmdCode_Object = MibTableColumn
ss7iCmdCode = _Ss7iCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 8),
    _Ss7iCmdCode_Type()
)
ss7iCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iCmdCode.setStatus("mandatory")
_Ss7iTrap_ObjectIdentity = ObjectIdentity
ss7iTrap = _Ss7iTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3)
)
_Ss7iTrapTable_Object = MibTable
ss7iTrapTable = _Ss7iTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1)
)
if mibBuilder.loadTexts:
    ss7iTrapTable.setStatus("mandatory")
_Ss7iTrapEntry_Object = MibTableRow
ss7iTrapEntry = _Ss7iTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1)
)
ss7iTrapEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iTrapIndex"),
)
if mibBuilder.loadTexts:
    ss7iTrapEntry.setStatus("mandatory")
_Ss7iTrapIndex_Type = Integer32
_Ss7iTrapIndex_Object = MibTableColumn
ss7iTrapIndex = _Ss7iTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 1),
    _Ss7iTrapIndex_Type()
)
ss7iTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iTrapIndex.setStatus("mandatory")


class _Ss7iTrapPbusLinkUp_Type(Integer32):
    """Custom type ss7iTrapPbusLinkUp based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Ss7iTrapPbusLinkUp_Type.__name__ = "Integer32"
_Ss7iTrapPbusLinkUp_Object = MibTableColumn
ss7iTrapPbusLinkUp = _Ss7iTrapPbusLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 2),
    _Ss7iTrapPbusLinkUp_Type()
)
ss7iTrapPbusLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iTrapPbusLinkUp.setStatus("mandatory")


class _Ss7iTrapPbusLinkDown_Type(Integer32):
    """Custom type ss7iTrapPbusLinkDown based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Ss7iTrapPbusLinkDown_Type.__name__ = "Integer32"
_Ss7iTrapPbusLinkDown_Object = MibTableColumn
ss7iTrapPbusLinkDown = _Ss7iTrapPbusLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 3),
    _Ss7iTrapPbusLinkDown_Type()
)
ss7iTrapPbusLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iTrapPbusLinkDown.setStatus("mandatory")


class _Ss7iTrapGwConnUp_Type(Integer32):
    """Custom type ss7iTrapGwConnUp based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Ss7iTrapGwConnUp_Type.__name__ = "Integer32"
_Ss7iTrapGwConnUp_Object = MibTableColumn
ss7iTrapGwConnUp = _Ss7iTrapGwConnUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 4),
    _Ss7iTrapGwConnUp_Type()
)
ss7iTrapGwConnUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iTrapGwConnUp.setStatus("mandatory")


class _Ss7iTrapGwConnDown_Type(Integer32):
    """Custom type ss7iTrapGwConnDown based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Ss7iTrapGwConnDown_Type.__name__ = "Integer32"
_Ss7iTrapGwConnDown_Object = MibTableColumn
ss7iTrapGwConnDown = _Ss7iTrapGwConnDown_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 5),
    _Ss7iTrapGwConnDown_Type()
)
ss7iTrapGwConnDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iTrapGwConnDown.setStatus("mandatory")
_Ss7iStat_ObjectIdentity = ObjectIdentity
ss7iStat = _Ss7iStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4)
)
_Ss7iStatTable_Object = MibTable
ss7iStatTable = _Ss7iStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1)
)
if mibBuilder.loadTexts:
    ss7iStatTable.setStatus("mandatory")
_Ss7iStatEntry_Object = MibTableRow
ss7iStatEntry = _Ss7iStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1)
)
ss7iStatEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iStatIndex"),
)
if mibBuilder.loadTexts:
    ss7iStatEntry.setStatus("mandatory")
_Ss7iStatIndex_Type = Integer32
_Ss7iStatIndex_Object = MibTableColumn
ss7iStatIndex = _Ss7iStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 1),
    _Ss7iStatIndex_Type()
)
ss7iStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatIndex.setStatus("mandatory")


class _Ss7iStatGwConnStatus_Type(Integer32):
    """Custom type ss7iStatGwConnStatus based on Integer32"""
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


_Ss7iStatGwConnStatus_Type.__name__ = "Integer32"
_Ss7iStatGwConnStatus_Object = MibTableColumn
ss7iStatGwConnStatus = _Ss7iStatGwConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 2),
    _Ss7iStatGwConnStatus_Type()
)
ss7iStatGwConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwConnStatus.setStatus("mandatory")
_Ss7iStatGwNumMsgsRcvd_Type = Counter32
_Ss7iStatGwNumMsgsRcvd_Object = MibTableColumn
ss7iStatGwNumMsgsRcvd = _Ss7iStatGwNumMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 3),
    _Ss7iStatGwNumMsgsRcvd_Type()
)
ss7iStatGwNumMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwNumMsgsRcvd.setStatus("mandatory")
_Ss7iStatGwNumBytesRcvd_Type = Counter32
_Ss7iStatGwNumBytesRcvd_Object = MibTableColumn
ss7iStatGwNumBytesRcvd = _Ss7iStatGwNumBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 4),
    _Ss7iStatGwNumBytesRcvd_Type()
)
ss7iStatGwNumBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwNumBytesRcvd.setStatus("mandatory")
_Ss7iStatGwNumMsgsSent_Type = Counter32
_Ss7iStatGwNumMsgsSent_Object = MibTableColumn
ss7iStatGwNumMsgsSent = _Ss7iStatGwNumMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 5),
    _Ss7iStatGwNumMsgsSent_Type()
)
ss7iStatGwNumMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwNumMsgsSent.setStatus("mandatory")
_Ss7iStatGwNumBytesSent_Type = Counter32
_Ss7iStatGwNumBytesSent_Object = MibTableColumn
ss7iStatGwNumBytesSent = _Ss7iStatGwNumBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 6),
    _Ss7iStatGwNumBytesSent_Type()
)
ss7iStatGwNumBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwNumBytesSent.setStatus("mandatory")
_Ss7iStatGwMssdHrtbtCnt_Type = Counter32
_Ss7iStatGwMssdHrtbtCnt_Object = MibTableColumn
ss7iStatGwMssdHrtbtCnt = _Ss7iStatGwMssdHrtbtCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 7),
    _Ss7iStatGwMssdHrtbtCnt_Type()
)
ss7iStatGwMssdHrtbtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwMssdHrtbtCnt.setStatus("mandatory")
_Ss7iStatGwLinkLostCnt_Type = Counter32
_Ss7iStatGwLinkLostCnt_Object = MibTableColumn
ss7iStatGwLinkLostCnt = _Ss7iStatGwLinkLostCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 8),
    _Ss7iStatGwLinkLostCnt_Type()
)
ss7iStatGwLinkLostCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwLinkLostCnt.setStatus("mandatory")
_Ss7iStatGwLinkErrCnt_Type = Counter32
_Ss7iStatGwLinkErrCnt_Object = MibTableColumn
ss7iStatGwLinkErrCnt = _Ss7iStatGwLinkErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 9),
    _Ss7iStatGwLinkErrCnt_Type()
)
ss7iStatGwLinkErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwLinkErrCnt.setStatus("mandatory")


class _Ss7iStatGwLinkDownCause_Type(Integer32):
    """Custom type ss7iStatGwLinkDownCause based on Integer32"""
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
        *(("heartbeatTimeout", 2),
          ("none", 1),
          ("physicalLinkSevered", 4),
          ("socketSndRcvError", 3))
    )


_Ss7iStatGwLinkDownCause_Type.__name__ = "Integer32"
_Ss7iStatGwLinkDownCause_Object = MibTableColumn
ss7iStatGwLinkDownCause = _Ss7iStatGwLinkDownCause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 10),
    _Ss7iStatGwLinkDownCause_Type()
)
ss7iStatGwLinkDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iStatGwLinkDownCause.setStatus("mandatory")
_Ss7iHdm_ObjectIdentity = ObjectIdentity
ss7iHdm = _Ss7iHdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5)
)
_Ss7iHdmTable_Object = MibTable
ss7iHdmTable = _Ss7iHdmTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1)
)
if mibBuilder.loadTexts:
    ss7iHdmTable.setStatus("mandatory")
_Ss7iHdmEntry_Object = MibTableRow
ss7iHdmEntry = _Ss7iHdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1)
)
ss7iHdmEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iHdmIndex"),
    (0, "SS7I-MIB", "ss7iHdmIndex2"),
)
if mibBuilder.loadTexts:
    ss7iHdmEntry.setStatus("mandatory")
_Ss7iHdmIndex_Type = Integer32
_Ss7iHdmIndex_Object = MibTableColumn
ss7iHdmIndex = _Ss7iHdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 1),
    _Ss7iHdmIndex_Type()
)
ss7iHdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmIndex.setStatus("mandatory")
_Ss7iHdmIndex2_Type = Integer32
_Ss7iHdmIndex2_Object = MibTableColumn
ss7iHdmIndex2 = _Ss7iHdmIndex2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 2),
    _Ss7iHdmIndex2_Type()
)
ss7iHdmIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmIndex2.setStatus("mandatory")


class _Ss7iHdmConnState_Type(Integer32):
    """Custom type ss7iHdmConnState based on Integer32"""
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
        *(("closed", 1),
          ("closing", 6),
          ("configuring", 4),
          ("loopback", 7),
          ("opened", 3),
          ("opening", 2),
          ("ready", 5))
    )


_Ss7iHdmConnState_Type.__name__ = "Integer32"
_Ss7iHdmConnState_Object = MibTableColumn
ss7iHdmConnState = _Ss7iHdmConnState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 3),
    _Ss7iHdmConnState_Type()
)
ss7iHdmConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmConnState.setStatus("mandatory")
_Ss7iHdmSndPktsOkCnt_Type = Counter32
_Ss7iHdmSndPktsOkCnt_Object = MibTableColumn
ss7iHdmSndPktsOkCnt = _Ss7iHdmSndPktsOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 4),
    _Ss7iHdmSndPktsOkCnt_Type()
)
ss7iHdmSndPktsOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmSndPktsOkCnt.setStatus("mandatory")
_Ss7iHdmSndPktsFailCnt_Type = Counter32
_Ss7iHdmSndPktsFailCnt_Object = MibTableColumn
ss7iHdmSndPktsFailCnt = _Ss7iHdmSndPktsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 5),
    _Ss7iHdmSndPktsFailCnt_Type()
)
ss7iHdmSndPktsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmSndPktsFailCnt.setStatus("mandatory")
_Ss7iHdmRcvPktsOkCnt_Type = Counter32
_Ss7iHdmRcvPktsOkCnt_Object = MibTableColumn
ss7iHdmRcvPktsOkCnt = _Ss7iHdmRcvPktsOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 6),
    _Ss7iHdmRcvPktsOkCnt_Type()
)
ss7iHdmRcvPktsOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmRcvPktsOkCnt.setStatus("mandatory")
_Ss7iHdmRcvPktsFailCnt_Type = Counter32
_Ss7iHdmRcvPktsFailCnt_Object = MibTableColumn
ss7iHdmRcvPktsFailCnt = _Ss7iHdmRcvPktsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 7),
    _Ss7iHdmRcvPktsFailCnt_Type()
)
ss7iHdmRcvPktsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmRcvPktsFailCnt.setStatus("mandatory")


class _Ss7iHdmLinkDownCause_Type(Integer32):
    """Custom type ss7iHdmLinkDownCause based on Integer32"""
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
        *(("missingHdm", 2),
          ("none", 1),
          ("pbusSndRcvError", 4),
          ("ss7GwLinkDown", 3))
    )


_Ss7iHdmLinkDownCause_Type.__name__ = "Integer32"
_Ss7iHdmLinkDownCause_Object = MibTableColumn
ss7iHdmLinkDownCause = _Ss7iHdmLinkDownCause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 8),
    _Ss7iHdmLinkDownCause_Type()
)
ss7iHdmLinkDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iHdmLinkDownCause.setStatus("mandatory")
_Ss7iSigPb_ObjectIdentity = ObjectIdentity
ss7iSigPb = _Ss7iSigPb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6)
)
_Ss7iSigPbTable_Object = MibTable
ss7iSigPbTable = _Ss7iSigPbTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1)
)
if mibBuilder.loadTexts:
    ss7iSigPbTable.setStatus("mandatory")
_Ss7iSigPbEntry_Object = MibTableRow
ss7iSigPbEntry = _Ss7iSigPbEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1)
)
ss7iSigPbEntry.setIndexNames(
    (0, "SS7I-MIB", "ss7iSigPbIndex"),
    (0, "SS7I-MIB", "ss7iSigPbIndex2"),
)
if mibBuilder.loadTexts:
    ss7iSigPbEntry.setStatus("mandatory")
_Ss7iSigPbIndex_Type = Integer32
_Ss7iSigPbIndex_Object = MibTableColumn
ss7iSigPbIndex = _Ss7iSigPbIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 1),
    _Ss7iSigPbIndex_Type()
)
ss7iSigPbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iSigPbIndex.setStatus("mandatory")
_Ss7iSigPbIndex2_Type = Integer32
_Ss7iSigPbIndex2_Object = MibTableColumn
ss7iSigPbIndex2 = _Ss7iSigPbIndex2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 2),
    _Ss7iSigPbIndex2_Type()
)
ss7iSigPbIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7iSigPbIndex2.setStatus("mandatory")


class _Ss7iSigPbConnection_Type(Integer32):
    """Custom type ss7iSigPbConnection based on Integer32"""
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


_Ss7iSigPbConnection_Type.__name__ = "Integer32"
_Ss7iSigPbConnection_Object = MibTableColumn
ss7iSigPbConnection = _Ss7iSigPbConnection_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 3),
    _Ss7iSigPbConnection_Type()
)
ss7iSigPbConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iSigPbConnection.setStatus("mandatory")


class _Ss7iSigPbLoopback_Type(Integer32):
    """Custom type ss7iSigPbLoopback based on Integer32"""
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


_Ss7iSigPbLoopback_Type.__name__ = "Integer32"
_Ss7iSigPbLoopback_Object = MibTableColumn
ss7iSigPbLoopback = _Ss7iSigPbLoopback_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 4),
    _Ss7iSigPbLoopback_Type()
)
ss7iSigPbLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7iSigPbLoopback.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SS7I-MIB",
    **{"usr": usr,
       "nas": nas,
       "ss7i": ss7i,
       "ss7iCfg": ss7iCfg,
       "ss7iCfgTable": ss7iCfgTable,
       "ss7iCfgEntry": ss7iCfgEntry,
       "ss7iCfgIndex": ss7iCfgIndex,
       "ss7iCfgIpAddr": ss7iCfgIpAddr,
       "ss7iCfgNetmask": ss7iCfgNetmask,
       "ss7iCfgDfltGwIpAddr": ss7iCfgDfltGwIpAddr,
       "ss7iCfgProtocol": ss7iCfgProtocol,
       "ss7iCfgGwConnStartMethod": ss7iCfgGwConnStartMethod,
       "ss7iCfgGwIpAddr": ss7iCfgGwIpAddr,
       "ss7iCfgGwPort": ss7iCfgGwPort,
       "ss7iCfgSecGwIpAddr": ss7iCfgSecGwIpAddr,
       "ss7iCfgSecGwPort": ss7iCfgSecGwPort,
       "ss7iCfgHrtbtTimerNearEnd": ss7iCfgHrtbtTimerNearEnd,
       "ss7iCfgHrtbtTimerFarEnd": ss7iCfgHrtbtTimerFarEnd,
       "ss7iCfgChassisId": ss7iCfgChassisId,
       "ss7iCfgGwConnRetryCnt": ss7iCfgGwConnRetryCnt,
       "ss7iCfgGwConnRetryIntvl": ss7iCfgGwConnRetryIntvl,
       "ss7iCfgGwMssdHrtbtThrsh": ss7iCfgGwMssdHrtbtThrsh,
       "ss7iCmd": ss7iCmd,
       "ss7iCmdTable": ss7iCmdTable,
       "ss7iCmdEntry": ss7iCmdEntry,
       "ss7iCmdIndex": ss7iCmdIndex,
       "ss7iCmdMgtStationId": ss7iCmdMgtStationId,
       "ss7iCmdReqId": ss7iCmdReqId,
       "ss7iCmdFunction": ss7iCmdFunction,
       "ss7iCmdForce": ss7iCmdForce,
       "ss7iCmdParam": ss7iCmdParam,
       "ss7iCmdResult": ss7iCmdResult,
       "ss7iCmdCode": ss7iCmdCode,
       "ss7iTrap": ss7iTrap,
       "ss7iTrapTable": ss7iTrapTable,
       "ss7iTrapEntry": ss7iTrapEntry,
       "ss7iTrapIndex": ss7iTrapIndex,
       "ss7iTrapPbusLinkUp": ss7iTrapPbusLinkUp,
       "ss7iTrapPbusLinkDown": ss7iTrapPbusLinkDown,
       "ss7iTrapGwConnUp": ss7iTrapGwConnUp,
       "ss7iTrapGwConnDown": ss7iTrapGwConnDown,
       "ss7iStat": ss7iStat,
       "ss7iStatTable": ss7iStatTable,
       "ss7iStatEntry": ss7iStatEntry,
       "ss7iStatIndex": ss7iStatIndex,
       "ss7iStatGwConnStatus": ss7iStatGwConnStatus,
       "ss7iStatGwNumMsgsRcvd": ss7iStatGwNumMsgsRcvd,
       "ss7iStatGwNumBytesRcvd": ss7iStatGwNumBytesRcvd,
       "ss7iStatGwNumMsgsSent": ss7iStatGwNumMsgsSent,
       "ss7iStatGwNumBytesSent": ss7iStatGwNumBytesSent,
       "ss7iStatGwMssdHrtbtCnt": ss7iStatGwMssdHrtbtCnt,
       "ss7iStatGwLinkLostCnt": ss7iStatGwLinkLostCnt,
       "ss7iStatGwLinkErrCnt": ss7iStatGwLinkErrCnt,
       "ss7iStatGwLinkDownCause": ss7iStatGwLinkDownCause,
       "ss7iHdm": ss7iHdm,
       "ss7iHdmTable": ss7iHdmTable,
       "ss7iHdmEntry": ss7iHdmEntry,
       "ss7iHdmIndex": ss7iHdmIndex,
       "ss7iHdmIndex2": ss7iHdmIndex2,
       "ss7iHdmConnState": ss7iHdmConnState,
       "ss7iHdmSndPktsOkCnt": ss7iHdmSndPktsOkCnt,
       "ss7iHdmSndPktsFailCnt": ss7iHdmSndPktsFailCnt,
       "ss7iHdmRcvPktsOkCnt": ss7iHdmRcvPktsOkCnt,
       "ss7iHdmRcvPktsFailCnt": ss7iHdmRcvPktsFailCnt,
       "ss7iHdmLinkDownCause": ss7iHdmLinkDownCause,
       "ss7iSigPb": ss7iSigPb,
       "ss7iSigPbTable": ss7iSigPbTable,
       "ss7iSigPbEntry": ss7iSigPbEntry,
       "ss7iSigPbIndex": ss7iSigPbIndex,
       "ss7iSigPbIndex2": ss7iSigPbIndex2,
       "ss7iSigPbConnection": ss7iSigPbConnection,
       "ss7iSigPbLoopback": ss7iSigPbLoopback}
)
