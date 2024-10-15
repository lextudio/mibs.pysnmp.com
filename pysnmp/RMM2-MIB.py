# SNMP MIB module (RMM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RMM2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:04 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

intelRmm2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rmm2_ObjectIdentity = ObjectIdentity
rmm2 = _Rmm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1)
)
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1)
)
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 1),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Ip_Type = IpAddress
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 3),
    _Ip_Type()
)
ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip.setStatus("current")
_Netmask_Type = IpAddress
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 4),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 5),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Mac_Type = MacAddress
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 6),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")


class _HardwareRev_Type(Integer32):
    """Custom type hardwareRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HardwareRev_Type.__name__ = "Integer32"
_HardwareRev_Object = MibScalar
hardwareRev = _HardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 7),
    _HardwareRev_Type()
)
hardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRev.setStatus("current")
_EventType_Type = DisplayString
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 8),
    _EventType_Type()
)
eventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventDesc_Type = DisplayString
_EventDesc_Object = MibScalar
eventDesc = _EventDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 9),
    _EventDesc_Type()
)
eventDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventDesc.setStatus("current")
_UserLoginName_Type = DisplayString
_UserLoginName_Object = MibScalar
userLoginName = _UserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 10),
    _UserLoginName_Type()
)
userLoginName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userLoginName.setStatus("current")
_RemoteHost_Type = IpAddress
_RemoteHost_Object = MibScalar
remoteHost = _RemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1, 11),
    _RemoteHost_Type()
)
remoteHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteHost.setStatus("current")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 2)
)
_Actions_ObjectIdentity = ObjectIdentity
actions = _Actions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3)
)


class _ResetBoard_Type(Integer32):
    """Custom type resetBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetBoard_Type.__name__ = "Integer32"
_ResetBoard_Object = MibScalar
resetBoard = _ResetBoard_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 1),
    _ResetBoard_Type()
)
resetBoard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetBoard.setStatus("current")
_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 2)
)
_HostInfo_ObjectIdentity = ObjectIdentity
hostInfo = _HostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 2, 1)
)


class _CheckHostPower_Type(Integer32):
    """Custom type checkHostPower based on Integer32"""
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
        *(("error", 3),
          ("hasPower", 1),
          ("hasnoPower", 2),
          ("notsupported", 4))
    )


_CheckHostPower_Type.__name__ = "Integer32"
_CheckHostPower_Object = MibScalar
checkHostPower = _CheckHostPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 2, 1, 1),
    _CheckHostPower_Type()
)
checkHostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkHostPower.setStatus("current")
_HostActions_ObjectIdentity = ObjectIdentity
hostActions = _HostActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 2, 2)
)


class _HostReset_Type(Integer32):
    """Custom type hostReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HostReset_Type.__name__ = "Integer32"
_HostReset_Object = MibScalar
hostReset = _HostReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 2, 2, 1),
    _HostReset_Type()
)
hostReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostReset.setStatus("current")


class _HostPower_Type(Integer32):
    """Custom type hostPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("longPress", 1)
    )


_HostPower_Type.__name__ = "Integer32"
_HostPower_Object = MibScalar
hostPower = _HostPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 1, 2, 2, 2),
    _HostPower_Type()
)
hostPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostPower.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 4)
)

# Managed Objects groups


# Notification objects

dummyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dummyTrap.setStatus(
        "current"
    )

loginfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 2)
)
loginfailed.setObjects(
      *(("RMM2-MIB", "userLoginName"),
        ("RMM2-MIB", "remoteHost"))
)
if mibBuilder.loadTexts:
    loginfailed.setStatus(
        "current"
    )

loginsuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 3)
)
loginsuccess.setObjects(
      *(("RMM2-MIB", "userLoginName"),
        ("RMM2-MIB", "remoteHost"))
)
if mibBuilder.loadTexts:
    loginsuccess.setStatus(
        "current"
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 4)
)
securityViolation.setObjects(
      *(("RMM2-MIB", "userLoginName"),
        ("RMM2-MIB", "remoteHost"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        "current"
    )

generic = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 5)
)
generic.setObjects(
      *(("RMM2-MIB", "eventType"),
        ("RMM2-MIB", "eventDesc"))
)
if mibBuilder.loadTexts:
    generic.setStatus(
        "current"
    )

logout = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 1, 4, 6)
)
logout.setObjects(
      *(("RMM2-MIB", "userLoginName"),
        ("RMM2-MIB", "remoteHost"))
)
if mibBuilder.loadTexts:
    logout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMM2-MIB",
    **{"intelRmm2": intelRmm2,
       "rmm2": rmm2,
       "board": board,
       "info": info,
       "firmwareVersion": firmwareVersion,
       "serialNumber": serialNumber,
       "ip": ip,
       "netmask": netmask,
       "gateway": gateway,
       "mac": mac,
       "hardwareRev": hardwareRev,
       "eventType": eventType,
       "eventDesc": eventDesc,
       "userLoginName": userLoginName,
       "remoteHost": remoteHost,
       "users": users,
       "actions": actions,
       "resetBoard": resetBoard,
       "host": host,
       "hostInfo": hostInfo,
       "checkHostPower": checkHostPower,
       "hostActions": hostActions,
       "hostReset": hostReset,
       "hostPower": hostPower,
       "common": common,
       "traps": traps,
       "dummyTrap": dummyTrap,
       "loginfailed": loginfailed,
       "loginsuccess": loginsuccess,
       "securityViolation": securityViolation,
       "generic": generic,
       "logout": logout}
)
