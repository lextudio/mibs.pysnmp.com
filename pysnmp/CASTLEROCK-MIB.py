# SNMP MIB module (CASTLEROCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASTLEROCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:42 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CastleRock_ObjectIdentity = ObjectIdentity
castleRock = _CastleRock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56)
)
_Snmpc_ObjectIdentity = ObjectIdentity
snmpc = _Snmpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12)
)
_Snmpc_Events_ObjectIdentity = ObjectIdentity
snmpc_Events = _Snmpc_Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1)
)
_Global_Defaults_ObjectIdentity = ObjectIdentity
global_Defaults = _Global_Defaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 1)
)
_Snmpc_Status_Polling_ObjectIdentity = ObjectIdentity
snmpc_Status_Polling = _Snmpc_Status_Polling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2)
)


class _PollLastStateDown_Type(Integer32):
    """Custom type pollLastStateDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_PollLastStateDown_Type.__name__ = "Integer32"
_PollLastStateDown_Object = MibScalar
pollLastStateDown = _PollLastStateDown_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 1),
    _PollLastStateDown_Type()
)
pollLastStateDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollLastStateDown.setStatus("mandatory")
_PollSnmpErrorCode_Type = Integer32
_PollSnmpErrorCode_Object = MibScalar
pollSnmpErrorCode = _PollSnmpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 2),
    _PollSnmpErrorCode_Type()
)
pollSnmpErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollSnmpErrorCode.setStatus("mandatory")
_Snmpc_Threshold_Alarm_ObjectIdentity = ObjectIdentity
snmpc_Threshold_Alarm = _Snmpc_Threshold_Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3)
)
_Snmpc_System_Info_ObjectIdentity = ObjectIdentity
snmpc_System_Info = _Snmpc_System_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5)
)
_Snmpc_Mib_Compiler_ObjectIdentity = ObjectIdentity
snmpc_Mib_Compiler = _Snmpc_Mib_Compiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 6)
)
_Snmpc_App_Events_ObjectIdentity = ObjectIdentity
snmpc_App_Events = _Snmpc_App_Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 7)
)
_AddressGroup_ObjectIdentity = ObjectIdentity
addressGroup = _AddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 2)
)
_DeviceAddress_Type = OctetString
_DeviceAddress_Object = MibScalar
deviceAddress = _DeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 1),
    _DeviceAddress_Type()
)
deviceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceAddress.setStatus("mandatory")
_DeviceMapID_Type = Integer32
_DeviceMapID_Object = MibScalar
deviceMapID = _DeviceMapID_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 2),
    _DeviceMapID_Type()
)
deviceMapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceMapID.setStatus("mandatory")
_PollAgentAddress_Type = IpAddress
_PollAgentAddress_Object = MibScalar
pollAgentAddress = _PollAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 3),
    _PollAgentAddress_Type()
)
pollAgentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollAgentAddress.setStatus("mandatory")
_ServerAddress_Type = IpAddress
_ServerAddress_Object = MibScalar
serverAddress = _ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 4),
    _ServerAddress_Type()
)
serverAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverAddress.setStatus("mandatory")
_ConsAddress_Type = IpAddress
_ConsAddress_Object = MibScalar
consAddress = _ConsAddress_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 5),
    _ConsAddress_Type()
)
consAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    consAddress.setStatus("mandatory")
_ConsUser_Type = DisplayString
_ConsUser_Object = MibScalar
consUser = _ConsUser_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 2, 6),
    _ConsUser_Type()
)
consUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    consUser.setStatus("mandatory")
_ObjectGroup_ObjectIdentity = ObjectIdentity
objectGroup = _ObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 3)
)
_ObjectName_Type = DisplayString
_ObjectName_Object = MibScalar
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 3, 1),
    _ObjectName_Type()
)
objectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    objectName.setStatus("mandatory")
_ObjectNumber_Type = Integer32
_ObjectNumber_Object = MibScalar
objectNumber = _ObjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 3, 2),
    _ObjectNumber_Type()
)
objectNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    objectNumber.setStatus("mandatory")
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 4)
)
_AlarmVariable_Type = DisplayString
_AlarmVariable_Object = MibScalar
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 4, 1),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("mandatory")
_AlarmInstance_Type = DisplayString
_AlarmInstance_Object = MibScalar
alarmInstance = _AlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 4, 2),
    _AlarmInstance_Type()
)
alarmInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmInstance.setStatus("mandatory")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibScalar
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 4, 3),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmValue.setStatus("mandatory")
_AlarmThreshold_Type = Integer32
_AlarmThreshold_Object = MibScalar
alarmThreshold = _AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 4, 4),
    _AlarmThreshold_Type()
)
alarmThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmThreshold.setStatus("mandatory")
_AlarmExpression_Type = DisplayString
_AlarmExpression_Object = MibScalar
alarmExpression = _AlarmExpression_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 4, 5),
    _AlarmExpression_Type()
)
alarmExpression.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmExpression.setStatus("mandatory")
_MibGroup_ObjectIdentity = ObjectIdentity
mibGroup = _MibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 5)
)
_MibSourceFile_Type = DisplayString
_MibSourceFile_Object = MibScalar
mibSourceFile = _MibSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 5, 1),
    _MibSourceFile_Type()
)
mibSourceFile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mibSourceFile.setStatus("mandatory")
_SystemGroup_ObjectIdentity = ObjectIdentity
systemGroup = _SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 6)
)


class _SystemComponent_Type(Integer32):
    """Custom type systemComponent based on Integer32"""
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
        *(("discoveryStatusPoller", 1),
          ("domainMaster", 3),
          ("domainSlave", 5),
          ("historyPoller", 2),
          ("snmpcServer", 6),
          ("userConsole", 4))
    )


_SystemComponent_Type.__name__ = "Integer32"
_SystemComponent_Object = MibScalar
systemComponent = _SystemComponent_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 6, 1),
    _SystemComponent_Type()
)
systemComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemComponent.setStatus("mandatory")


class _SystemStatus_Type(Integer32):
    """Custom type systemStatus based on Integer32"""
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


_SystemStatus_Type.__name__ = "Integer32"
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 6, 2),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemStatus.setStatus("mandatory")
_SystemLogMessage_Type = DisplayString
_SystemLogMessage_Object = MibScalar
systemLogMessage = _SystemLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 6, 3),
    _SystemLogMessage_Type()
)
systemLogMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemLogMessage.setStatus("mandatory")
_SystemErrorCode_Type = Integer32
_SystemErrorCode_Object = MibScalar
systemErrorCode = _SystemErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 6, 4),
    _SystemErrorCode_Type()
)
systemErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemErrorCode.setStatus("mandatory")
_DefunctGroup_ObjectIdentity = ObjectIdentity
defunctGroup = _DefunctGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 7)
)
_AvailGroup_ObjectIdentity = ObjectIdentity
availGroup = _AvailGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 8)
)
_RespTime_Poll_Type = Gauge32
_RespTime_Poll_Object = MibScalar
respTime_Poll = _RespTime_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 1),
    _RespTime_Poll_Type()
)
respTime_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_Poll.setStatus("mandatory")
_RespTime_Web_Type = Gauge32
_RespTime_Web_Object = MibScalar
respTime_Web = _RespTime_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 2),
    _RespTime_Web_Type()
)
respTime_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_Web.setStatus("mandatory")
_RespTime_Ftp_Type = Gauge32
_RespTime_Ftp_Object = MibScalar
respTime_Ftp = _RespTime_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 3),
    _RespTime_Ftp_Type()
)
respTime_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_Ftp.setStatus("mandatory")
_RespTime_Smtp_Type = Gauge32
_RespTime_Smtp_Object = MibScalar
respTime_Smtp = _RespTime_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 4),
    _RespTime_Smtp_Type()
)
respTime_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_Smtp.setStatus("mandatory")
_RespTime_Telnet_Type = Gauge32
_RespTime_Telnet_Object = MibScalar
respTime_Telnet = _RespTime_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 5),
    _RespTime_Telnet_Type()
)
respTime_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_Telnet.setStatus("mandatory")
_RespTime_User1_Type = Gauge32
_RespTime_User1_Object = MibScalar
respTime_User1 = _RespTime_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 6),
    _RespTime_User1_Type()
)
respTime_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_User1.setStatus("mandatory")
_RespTime_User2_Type = Gauge32
_RespTime_User2_Object = MibScalar
respTime_User2 = _RespTime_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 7),
    _RespTime_User2_Type()
)
respTime_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_User2.setStatus("mandatory")
_PollOK_Poll_Type = Counter32
_PollOK_Poll_Object = MibScalar
pollOK_Poll = _PollOK_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 8),
    _PollOK_Poll_Type()
)
pollOK_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_Poll.setStatus("mandatory")
_PollOK_Web_Type = Counter32
_PollOK_Web_Object = MibScalar
pollOK_Web = _PollOK_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 9),
    _PollOK_Web_Type()
)
pollOK_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_Web.setStatus("mandatory")
_PollOK_Ftp_Type = Counter32
_PollOK_Ftp_Object = MibScalar
pollOK_Ftp = _PollOK_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 10),
    _PollOK_Ftp_Type()
)
pollOK_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_Ftp.setStatus("mandatory")
_PollOK_Smtp_Type = Counter32
_PollOK_Smtp_Object = MibScalar
pollOK_Smtp = _PollOK_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 11),
    _PollOK_Smtp_Type()
)
pollOK_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_Smtp.setStatus("mandatory")
_PollOK_Telnet_Type = Counter32
_PollOK_Telnet_Object = MibScalar
pollOK_Telnet = _PollOK_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 12),
    _PollOK_Telnet_Type()
)
pollOK_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_Telnet.setStatus("mandatory")
_PollOK_User1_Type = Counter32
_PollOK_User1_Object = MibScalar
pollOK_User1 = _PollOK_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 13),
    _PollOK_User1_Type()
)
pollOK_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_User1.setStatus("mandatory")
_PollOK_User2_Type = Counter32
_PollOK_User2_Object = MibScalar
pollOK_User2 = _PollOK_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 14),
    _PollOK_User2_Type()
)
pollOK_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_User2.setStatus("mandatory")
_PollFail_Poll_Type = Counter32
_PollFail_Poll_Object = MibScalar
pollFail_Poll = _PollFail_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 15),
    _PollFail_Poll_Type()
)
pollFail_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_Poll.setStatus("mandatory")
_PollFail_Web_Type = Counter32
_PollFail_Web_Object = MibScalar
pollFail_Web = _PollFail_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 16),
    _PollFail_Web_Type()
)
pollFail_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_Web.setStatus("mandatory")
_PollFail_Ftp_Type = Counter32
_PollFail_Ftp_Object = MibScalar
pollFail_Ftp = _PollFail_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 17),
    _PollFail_Ftp_Type()
)
pollFail_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_Ftp.setStatus("mandatory")
_PollFail_Smtp_Type = Counter32
_PollFail_Smtp_Object = MibScalar
pollFail_Smtp = _PollFail_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 18),
    _PollFail_Smtp_Type()
)
pollFail_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_Smtp.setStatus("mandatory")
_PollFail_Telnet_Type = Counter32
_PollFail_Telnet_Object = MibScalar
pollFail_Telnet = _PollFail_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 19),
    _PollFail_Telnet_Type()
)
pollFail_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_Telnet.setStatus("mandatory")
_PollFail_User1_Type = Counter32
_PollFail_User1_Object = MibScalar
pollFail_User1 = _PollFail_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 20),
    _PollFail_User1_Type()
)
pollFail_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_User1.setStatus("mandatory")
_PollFail_User2_Type = Counter32
_PollFail_User2_Object = MibScalar
pollFail_User2 = _PollFail_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 21),
    _PollFail_User2_Type()
)
pollFail_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_User2.setStatus("mandatory")
_PctFail_Poll_Type = Gauge32
_PctFail_Poll_Object = MibScalar
pctFail_Poll = _PctFail_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 22),
    _PctFail_Poll_Type()
)
pctFail_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_Poll.setStatus("mandatory")
_PctFail_Web_Type = Gauge32
_PctFail_Web_Object = MibScalar
pctFail_Web = _PctFail_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 23),
    _PctFail_Web_Type()
)
pctFail_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_Web.setStatus("mandatory")
_PctFail_Ftp_Type = Gauge32
_PctFail_Ftp_Object = MibScalar
pctFail_Ftp = _PctFail_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 24),
    _PctFail_Ftp_Type()
)
pctFail_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_Ftp.setStatus("mandatory")
_PctFail_Smtp_Type = Gauge32
_PctFail_Smtp_Object = MibScalar
pctFail_Smtp = _PctFail_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 25),
    _PctFail_Smtp_Type()
)
pctFail_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_Smtp.setStatus("mandatory")
_PctFail_Telnet_Type = Gauge32
_PctFail_Telnet_Object = MibScalar
pctFail_Telnet = _PctFail_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 26),
    _PctFail_Telnet_Type()
)
pctFail_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_Telnet.setStatus("mandatory")
_PctFail_User1_Type = Gauge32
_PctFail_User1_Object = MibScalar
pctFail_User1 = _PctFail_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 27),
    _PctFail_User1_Type()
)
pctFail_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_User1.setStatus("mandatory")
_PctFail_User2_Type = Gauge32
_PctFail_User2_Object = MibScalar
pctFail_User2 = _PctFail_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 28),
    _PctFail_User2_Type()
)
pctFail_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_User2.setStatus("mandatory")


class _CurState_POLL_Type(Integer32):
    """Custom type curState_POLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_POLL_Type.__name__ = "Integer32"
_CurState_POLL_Object = MibScalar
curState_POLL = _CurState_POLL_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 30),
    _CurState_POLL_Type()
)
curState_POLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_POLL.setStatus("mandatory")


class _CurState_WEB_Type(Integer32):
    """Custom type curState_WEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_WEB_Type.__name__ = "Integer32"
_CurState_WEB_Object = MibScalar
curState_WEB = _CurState_WEB_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 31),
    _CurState_WEB_Type()
)
curState_WEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_WEB.setStatus("mandatory")


class _CurState_FTP_Type(Integer32):
    """Custom type curState_FTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_FTP_Type.__name__ = "Integer32"
_CurState_FTP_Object = MibScalar
curState_FTP = _CurState_FTP_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 32),
    _CurState_FTP_Type()
)
curState_FTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_FTP.setStatus("mandatory")


class _CurState_SMTP_Type(Integer32):
    """Custom type curState_SMTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_SMTP_Type.__name__ = "Integer32"
_CurState_SMTP_Object = MibScalar
curState_SMTP = _CurState_SMTP_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 33),
    _CurState_SMTP_Type()
)
curState_SMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_SMTP.setStatus("mandatory")


class _CurState_TELNET_Type(Integer32):
    """Custom type curState_TELNET based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_TELNET_Type.__name__ = "Integer32"
_CurState_TELNET_Object = MibScalar
curState_TELNET = _CurState_TELNET_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 34),
    _CurState_TELNET_Type()
)
curState_TELNET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_TELNET.setStatus("mandatory")


class _CurState_User1_Type(Integer32):
    """Custom type curState_User1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_User1_Type.__name__ = "Integer32"
_CurState_User1_Object = MibScalar
curState_User1 = _CurState_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 35),
    _CurState_User1_Type()
)
curState_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_User1.setStatus("mandatory")


class _CurState_User2_Type(Integer32):
    """Custom type curState_User2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_User2_Type.__name__ = "Integer32"
_CurState_User2_Object = MibScalar
curState_User2 = _CurState_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 36),
    _CurState_User2_Type()
)
curState_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_User2.setStatus("mandatory")


class _PollSvcType_Type(Integer32):
    """Custom type pollSvcType based on Integer32"""
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
        *(("ftp", 3),
          ("regpoll", 1),
          ("smtp", 4),
          ("telnet", 5),
          ("user1", 6),
          ("user2", 7),
          ("user3", 8),
          ("user4", 9),
          ("web", 2))
    )


_PollSvcType_Type.__name__ = "Integer32"
_PollSvcType_Object = MibScalar
pollSvcType = _PollSvcType_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 37),
    _PollSvcType_Type()
)
pollSvcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollSvcType.setStatus("mandatory")
_AvgRespTime_Poll_Type = Gauge32
_AvgRespTime_Poll_Object = MibScalar
avgRespTime_Poll = _AvgRespTime_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 38),
    _AvgRespTime_Poll_Type()
)
avgRespTime_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_Poll.setStatus("mandatory")
_AvgRespTime_Web_Type = Gauge32
_AvgRespTime_Web_Object = MibScalar
avgRespTime_Web = _AvgRespTime_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 39),
    _AvgRespTime_Web_Type()
)
avgRespTime_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_Web.setStatus("mandatory")
_AvgRespTime_Ftp_Type = Gauge32
_AvgRespTime_Ftp_Object = MibScalar
avgRespTime_Ftp = _AvgRespTime_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 40),
    _AvgRespTime_Ftp_Type()
)
avgRespTime_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_Ftp.setStatus("mandatory")
_AvgRespTime_Smtp_Type = Gauge32
_AvgRespTime_Smtp_Object = MibScalar
avgRespTime_Smtp = _AvgRespTime_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 41),
    _AvgRespTime_Smtp_Type()
)
avgRespTime_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_Smtp.setStatus("mandatory")
_AvgRespTime_Telnet_Type = Gauge32
_AvgRespTime_Telnet_Object = MibScalar
avgRespTime_Telnet = _AvgRespTime_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 42),
    _AvgRespTime_Telnet_Type()
)
avgRespTime_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_Telnet.setStatus("mandatory")
_AvgRespTime_User1_Type = Gauge32
_AvgRespTime_User1_Object = MibScalar
avgRespTime_User1 = _AvgRespTime_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 43),
    _AvgRespTime_User1_Type()
)
avgRespTime_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_User1.setStatus("mandatory")
_AvgRespTime_User2_Type = Gauge32
_AvgRespTime_User2_Object = MibScalar
avgRespTime_User2 = _AvgRespTime_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 44),
    _AvgRespTime_User2_Type()
)
avgRespTime_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_User2.setStatus("mandatory")
_AvgPctFail_Poll_Type = Gauge32
_AvgPctFail_Poll_Object = MibScalar
avgPctFail_Poll = _AvgPctFail_Poll_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 45),
    _AvgPctFail_Poll_Type()
)
avgPctFail_Poll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_Poll.setStatus("mandatory")
_AvgPctFail_Web_Type = Gauge32
_AvgPctFail_Web_Object = MibScalar
avgPctFail_Web = _AvgPctFail_Web_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 46),
    _AvgPctFail_Web_Type()
)
avgPctFail_Web.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_Web.setStatus("mandatory")
_AvgPctFail_Ftp_Type = Gauge32
_AvgPctFail_Ftp_Object = MibScalar
avgPctFail_Ftp = _AvgPctFail_Ftp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 47),
    _AvgPctFail_Ftp_Type()
)
avgPctFail_Ftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_Ftp.setStatus("mandatory")
_AvgPctFail_Smtp_Type = Gauge32
_AvgPctFail_Smtp_Object = MibScalar
avgPctFail_Smtp = _AvgPctFail_Smtp_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 48),
    _AvgPctFail_Smtp_Type()
)
avgPctFail_Smtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_Smtp.setStatus("mandatory")
_AvgPctFail_Telnet_Type = Gauge32
_AvgPctFail_Telnet_Object = MibScalar
avgPctFail_Telnet = _AvgPctFail_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 49),
    _AvgPctFail_Telnet_Type()
)
avgPctFail_Telnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_Telnet.setStatus("mandatory")
_AvgPctFail_User1_Type = Gauge32
_AvgPctFail_User1_Object = MibScalar
avgPctFail_User1 = _AvgPctFail_User1_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 50),
    _AvgPctFail_User1_Type()
)
avgPctFail_User1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_User1.setStatus("mandatory")
_AvgPctFail_User2_Type = Gauge32
_AvgPctFail_User2_Object = MibScalar
avgPctFail_User2 = _AvgPctFail_User2_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 51),
    _AvgPctFail_User2_Type()
)
avgPctFail_User2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_User2.setStatus("mandatory")
_RespTime_User3_Type = Gauge32
_RespTime_User3_Object = MibScalar
respTime_User3 = _RespTime_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 52),
    _RespTime_User3_Type()
)
respTime_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_User3.setStatus("mandatory")
_RespTime_User4_Type = Gauge32
_RespTime_User4_Object = MibScalar
respTime_User4 = _RespTime_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 53),
    _RespTime_User4_Type()
)
respTime_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respTime_User4.setStatus("mandatory")
_PollOK_User3_Type = Counter32
_PollOK_User3_Object = MibScalar
pollOK_User3 = _PollOK_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 54),
    _PollOK_User3_Type()
)
pollOK_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_User3.setStatus("mandatory")
_PollOK_User4_Type = Counter32
_PollOK_User4_Object = MibScalar
pollOK_User4 = _PollOK_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 55),
    _PollOK_User4_Type()
)
pollOK_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollOK_User4.setStatus("mandatory")
_PollFail_User3_Type = Counter32
_PollFail_User3_Object = MibScalar
pollFail_User3 = _PollFail_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 56),
    _PollFail_User3_Type()
)
pollFail_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_User3.setStatus("mandatory")
_PollFail_User4_Type = Counter32
_PollFail_User4_Object = MibScalar
pollFail_User4 = _PollFail_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 57),
    _PollFail_User4_Type()
)
pollFail_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollFail_User4.setStatus("mandatory")
_PctFail_User3_Type = Gauge32
_PctFail_User3_Object = MibScalar
pctFail_User3 = _PctFail_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 58),
    _PctFail_User3_Type()
)
pctFail_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_User3.setStatus("mandatory")
_PctFail_User4_Type = Gauge32
_PctFail_User4_Object = MibScalar
pctFail_User4 = _PctFail_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 59),
    _PctFail_User4_Type()
)
pctFail_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctFail_User4.setStatus("mandatory")


class _CurState_User3_Type(Integer32):
    """Custom type curState_User3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_User3_Type.__name__ = "Integer32"
_CurState_User3_Object = MibScalar
curState_User3 = _CurState_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 60),
    _CurState_User3_Type()
)
curState_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_User3.setStatus("mandatory")


class _CurState_User4_Type(Integer32):
    """Custom type curState_User4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("noresp", 1),
          ("unk", 0),
          ("up", 2),
          ("up-err", 3))
    )


_CurState_User4_Type.__name__ = "Integer32"
_CurState_User4_Object = MibScalar
curState_User4 = _CurState_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 61),
    _CurState_User4_Type()
)
curState_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curState_User4.setStatus("mandatory")
_AvgRespTime_User3_Type = Gauge32
_AvgRespTime_User3_Object = MibScalar
avgRespTime_User3 = _AvgRespTime_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 62),
    _AvgRespTime_User3_Type()
)
avgRespTime_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_User3.setStatus("mandatory")
_AvgRespTime_User4_Type = Gauge32
_AvgRespTime_User4_Object = MibScalar
avgRespTime_User4 = _AvgRespTime_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 63),
    _AvgRespTime_User4_Type()
)
avgRespTime_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgRespTime_User4.setStatus("mandatory")
_AvgPctFail_User3_Type = Gauge32
_AvgPctFail_User3_Object = MibScalar
avgPctFail_User3 = _AvgPctFail_User3_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 64),
    _AvgPctFail_User3_Type()
)
avgPctFail_User3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_User3.setStatus("mandatory")
_AvgPctFail_User4_Type = Gauge32
_AvgPctFail_User4_Object = MibScalar
avgPctFail_User4 = _AvgPctFail_User4_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 8, 65),
    _AvgPctFail_User4_Type()
)
avgPctFail_User4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPctFail_User4.setStatus("mandatory")
_AppGroup_ObjectIdentity = ObjectIdentity
appGroup = _AppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56, 12, 9)
)
_AppName_Type = DisplayString
_AppName_Object = MibScalar
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 9, 1),
    _AppName_Type()
)
appName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appName.setStatus("mandatory")
_AppMessage_Type = DisplayString
_AppMessage_Object = MibScalar
appMessage = _AppMessage_Object(
    (1, 3, 6, 1, 4, 1, 56, 12, 9, 2),
    _AppMessage_Type()
)
appMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appMessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dummyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    dummyTrap.setStatus(
        ""
    )

pollResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 1)
)
pollResponse.setObjects(
    ("CASTLEROCK-MIB", "pollLastStateDown")
)
if mibBuilder.loadTexts:
    pollResponse.setStatus(
        ""
    )

pollNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pollNoResponse.setStatus(
        ""
    )

pollStatusTestPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 3)
)
pollStatusTestPass.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmValue"))
)
if mibBuilder.loadTexts:
    pollStatusTestPass.setStatus(
        ""
    )

pollStatusTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 4)
)
pollStatusTestFail.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmValue"))
)
if mibBuilder.loadTexts:
    pollStatusTestFail.setStatus(
        ""
    )

pollRequestRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 5)
)
pollRequestRejected.setObjects(
    ("CASTLEROCK-MIB", "pollSnmpErrorCode")
)
if mibBuilder.loadTexts:
    pollRequestRejected.setStatus(
        ""
    )

pollDeviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    pollDeviceDown.setStatus(
        ""
    )

pollServiceResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 7)
)
pollServiceResponding.setObjects(
      *(("CASTLEROCK-MIB", "pollSvcType"),
        ("CASTLEROCK-MIB", "pollLastStateDown"))
)
if mibBuilder.loadTexts:
    pollServiceResponding.setStatus(
        ""
    )

pollServiceNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 8)
)
pollServiceNoResponse.setObjects(
    ("CASTLEROCK-MIB", "pollSvcType")
)
if mibBuilder.loadTexts:
    pollServiceNoResponse.setStatus(
        ""
    )

pollServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 2, 0, 9)
)
pollServiceDown.setObjects(
    ("CASTLEROCK-MIB", "pollSvcType")
)
if mibBuilder.loadTexts:
    pollServiceDown.setStatus(
        ""
    )

alarmAutoThresholdTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 1)
)
alarmAutoThresholdTrigger.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmValue"),
        ("CASTLEROCK-MIB", "alarmThreshold"))
)
if mibBuilder.loadTexts:
    alarmAutoThresholdTrigger.setStatus(
        ""
    )

alarmAutoThresholdSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 2)
)
alarmAutoThresholdSet.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmThreshold"))
)
if mibBuilder.loadTexts:
    alarmAutoThresholdSet.setStatus(
        ""
    )

alarmAutoThresholdExpand = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 3)
)
alarmAutoThresholdExpand.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmThreshold"))
)
if mibBuilder.loadTexts:
    alarmAutoThresholdExpand.setStatus(
        ""
    )

alarmAutoThresholdReduce = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 4)
)
alarmAutoThresholdReduce.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmThreshold"))
)
if mibBuilder.loadTexts:
    alarmAutoThresholdReduce.setStatus(
        ""
    )

alarmManualThresholdTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 5)
)
alarmManualThresholdTrigger.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmValue"),
        ("CASTLEROCK-MIB", "alarmExpression"))
)
if mibBuilder.loadTexts:
    alarmManualThresholdTrigger.setStatus(
        ""
    )

alarmManualThresholdReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 3, 0, 6)
)
alarmManualThresholdReset.setObjects(
      *(("CASTLEROCK-MIB", "alarmVariable"),
        ("CASTLEROCK-MIB", "alarmInstance"),
        ("CASTLEROCK-MIB", "alarmValue"),
        ("CASTLEROCK-MIB", "alarmExpression"))
)
if mibBuilder.loadTexts:
    alarmManualThresholdReset.setStatus(
        ""
    )

pollAgentConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 1)
)
pollAgentConnect.setObjects(
    ("CASTLEROCK-MIB", "systemComponent")
)
if mibBuilder.loadTexts:
    pollAgentConnect.setStatus(
        ""
    )

pollAgentDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 2)
)
pollAgentDisconnect.setObjects(
    ("CASTLEROCK-MIB", "systemComponent")
)
if mibBuilder.loadTexts:
    pollAgentDisconnect.setStatus(
        ""
    )

systemInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 3)
)
systemInfo.setObjects(
      *(("CASTLEROCK-MIB", "systemComponent"),
        ("CASTLEROCK-MIB", "systemLogMessage"))
)
if mibBuilder.loadTexts:
    systemInfo.setStatus(
        ""
    )

systemWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 4)
)
systemWarn.setObjects(
      *(("CASTLEROCK-MIB", "systemComponent"),
        ("CASTLEROCK-MIB", "systemLogMessage"),
        ("CASTLEROCK-MIB", "systemErrorCode"))
)
if mibBuilder.loadTexts:
    systemWarn.setStatus(
        ""
    )

systemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 5)
)
systemError.setObjects(
      *(("CASTLEROCK-MIB", "systemComponent"),
        ("CASTLEROCK-MIB", "systemLogMessage"),
        ("CASTLEROCK-MIB", "systemErrorCode"))
)
if mibBuilder.loadTexts:
    systemError.setStatus(
        ""
    )

diskLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 6)
)
if mibBuilder.loadTexts:
    diskLowWarning.setStatus(
        ""
    )

diskLowError = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 5, 0, 7)
)
if mibBuilder.loadTexts:
    diskLowError.setStatus(
        ""
    )

appInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 7, 0, 1)
)
appInfo.setObjects(
      *(("CASTLEROCK-MIB", "appName"),
        ("CASTLEROCK-MIB", "appMessage"))
)
if mibBuilder.loadTexts:
    appInfo.setStatus(
        ""
    )

appWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 7, 0, 2)
)
appWarn.setObjects(
      *(("CASTLEROCK-MIB", "appName"),
        ("CASTLEROCK-MIB", "appMessage"))
)
if mibBuilder.loadTexts:
    appWarn.setStatus(
        ""
    )

appError = NotificationType(
    (1, 3, 6, 1, 4, 1, 56, 12, 1, 7, 0, 3)
)
appError.setObjects(
      *(("CASTLEROCK-MIB", "appName"),
        ("CASTLEROCK-MIB", "appMessage"))
)
if mibBuilder.loadTexts:
    appError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASTLEROCK-MIB",
    **{"castleRock": castleRock,
       "snmpc": snmpc,
       "snmpc-Events": snmpc_Events,
       "global-Defaults": global_Defaults,
       "dummyTrap": dummyTrap,
       "snmpc-Status-Polling": snmpc_Status_Polling,
       "pollResponse": pollResponse,
       "pollNoResponse": pollNoResponse,
       "pollStatusTestPass": pollStatusTestPass,
       "pollStatusTestFail": pollStatusTestFail,
       "pollRequestRejected": pollRequestRejected,
       "pollDeviceDown": pollDeviceDown,
       "pollServiceResponding": pollServiceResponding,
       "pollServiceNoResponse": pollServiceNoResponse,
       "pollServiceDown": pollServiceDown,
       "pollLastStateDown": pollLastStateDown,
       "pollSnmpErrorCode": pollSnmpErrorCode,
       "snmpc-Threshold-Alarm": snmpc_Threshold_Alarm,
       "alarmAutoThresholdTrigger": alarmAutoThresholdTrigger,
       "alarmAutoThresholdSet": alarmAutoThresholdSet,
       "alarmAutoThresholdExpand": alarmAutoThresholdExpand,
       "alarmAutoThresholdReduce": alarmAutoThresholdReduce,
       "alarmManualThresholdTrigger": alarmManualThresholdTrigger,
       "alarmManualThresholdReset": alarmManualThresholdReset,
       "snmpc-System-Info": snmpc_System_Info,
       "pollAgentConnect": pollAgentConnect,
       "pollAgentDisconnect": pollAgentDisconnect,
       "systemInfo": systemInfo,
       "systemWarn": systemWarn,
       "systemError": systemError,
       "diskLowWarning": diskLowWarning,
       "diskLowError": diskLowError,
       "snmpc-Mib-Compiler": snmpc_Mib_Compiler,
       "snmpc-App-Events": snmpc_App_Events,
       "appInfo": appInfo,
       "appWarn": appWarn,
       "appError": appError,
       "addressGroup": addressGroup,
       "deviceAddress": deviceAddress,
       "deviceMapID": deviceMapID,
       "pollAgentAddress": pollAgentAddress,
       "serverAddress": serverAddress,
       "consAddress": consAddress,
       "consUser": consUser,
       "objectGroup": objectGroup,
       "objectName": objectName,
       "objectNumber": objectNumber,
       "alarmGroup": alarmGroup,
       "alarmVariable": alarmVariable,
       "alarmInstance": alarmInstance,
       "alarmValue": alarmValue,
       "alarmThreshold": alarmThreshold,
       "alarmExpression": alarmExpression,
       "mibGroup": mibGroup,
       "mibSourceFile": mibSourceFile,
       "systemGroup": systemGroup,
       "systemComponent": systemComponent,
       "systemStatus": systemStatus,
       "systemLogMessage": systemLogMessage,
       "systemErrorCode": systemErrorCode,
       "defunctGroup": defunctGroup,
       "availGroup": availGroup,
       "respTime-Poll": respTime_Poll,
       "respTime-Web": respTime_Web,
       "respTime-Ftp": respTime_Ftp,
       "respTime-Smtp": respTime_Smtp,
       "respTime-Telnet": respTime_Telnet,
       "respTime-User1": respTime_User1,
       "respTime-User2": respTime_User2,
       "pollOK-Poll": pollOK_Poll,
       "pollOK-Web": pollOK_Web,
       "pollOK-Ftp": pollOK_Ftp,
       "pollOK-Smtp": pollOK_Smtp,
       "pollOK-Telnet": pollOK_Telnet,
       "pollOK-User1": pollOK_User1,
       "pollOK-User2": pollOK_User2,
       "pollFail-Poll": pollFail_Poll,
       "pollFail-Web": pollFail_Web,
       "pollFail-Ftp": pollFail_Ftp,
       "pollFail-Smtp": pollFail_Smtp,
       "pollFail-Telnet": pollFail_Telnet,
       "pollFail-User1": pollFail_User1,
       "pollFail-User2": pollFail_User2,
       "pctFail-Poll": pctFail_Poll,
       "pctFail-Web": pctFail_Web,
       "pctFail-Ftp": pctFail_Ftp,
       "pctFail-Smtp": pctFail_Smtp,
       "pctFail-Telnet": pctFail_Telnet,
       "pctFail-User1": pctFail_User1,
       "pctFail-User2": pctFail_User2,
       "curState-POLL": curState_POLL,
       "curState-WEB": curState_WEB,
       "curState-FTP": curState_FTP,
       "curState-SMTP": curState_SMTP,
       "curState-TELNET": curState_TELNET,
       "curState-User1": curState_User1,
       "curState-User2": curState_User2,
       "pollSvcType": pollSvcType,
       "avgRespTime-Poll": avgRespTime_Poll,
       "avgRespTime-Web": avgRespTime_Web,
       "avgRespTime-Ftp": avgRespTime_Ftp,
       "avgRespTime-Smtp": avgRespTime_Smtp,
       "avgRespTime-Telnet": avgRespTime_Telnet,
       "avgRespTime-User1": avgRespTime_User1,
       "avgRespTime-User2": avgRespTime_User2,
       "avgPctFail-Poll": avgPctFail_Poll,
       "avgPctFail-Web": avgPctFail_Web,
       "avgPctFail-Ftp": avgPctFail_Ftp,
       "avgPctFail-Smtp": avgPctFail_Smtp,
       "avgPctFail-Telnet": avgPctFail_Telnet,
       "avgPctFail-User1": avgPctFail_User1,
       "avgPctFail-User2": avgPctFail_User2,
       "respTime-User3": respTime_User3,
       "respTime-User4": respTime_User4,
       "pollOK-User3": pollOK_User3,
       "pollOK-User4": pollOK_User4,
       "pollFail-User3": pollFail_User3,
       "pollFail-User4": pollFail_User4,
       "pctFail-User3": pctFail_User3,
       "pctFail-User4": pctFail_User4,
       "curState-User3": curState_User3,
       "curState-User4": curState_User4,
       "avgRespTime-User3": avgRespTime_User3,
       "avgRespTime-User4": avgRespTime_User4,
       "avgPctFail-User3": avgPctFail_User3,
       "avgPctFail-User4": avgPctFail_User4,
       "appGroup": appGroup,
       "appName": appName,
       "appMessage": appMessage}
)
