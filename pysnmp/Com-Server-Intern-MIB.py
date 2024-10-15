# SNMP MIB module (Com-Server-Intern-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Com-Server-Intern-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:48 2024
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

_Wut_ObjectIdentity = ObjectIdentity
wut = _Wut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040)
)
_WtComServer_ObjectIdentity = ObjectIdentity
wtComServer = _WtComServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1)
)
_WtComServerIntern_ObjectIdentity = ObjectIdentity
wtComServerIntern = _WtComServerIntern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1)
)
_WtConfiguration_ObjectIdentity = ObjectIdentity
wtConfiguration = _WtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1)
)
_WtSystem_ObjectIdentity = ObjectIdentity
wtSystem = _WtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1)
)


class _WtCableType_Type(Integer32):
    """Custom type wtCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("wtAui", 3),
          ("wtCoax", 1),
          ("wtTwistedPair", 2),
          ("wtTwistedPair100FD", 16),
          ("wtTwistedPair100HD", 8),
          ("wtTwistedPair10FD", 4))
    )


_WtCableType_Type.__name__ = "Integer32"
_WtCableType_Object = MibScalar
wtCableType = _WtCableType_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 1),
    _WtCableType_Type()
)
wtCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtCableType.setStatus("mandatory")
_WtMacAddress_Type = PhysAddress
_WtMacAddress_Object = MibScalar
wtMacAddress = _WtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 2),
    _WtMacAddress_Type()
)
wtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtMacAddress.setStatus("mandatory")
_WtSwDate_Type = DisplayString
_WtSwDate_Object = MibScalar
wtSwDate = _WtSwDate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 3),
    _WtSwDate_Type()
)
wtSwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSwDate.setStatus("mandatory")
_WtSwRev_Type = DisplayString
_WtSwRev_Object = MibScalar
wtSwRev = _WtSwRev_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 4),
    _WtSwRev_Type()
)
wtSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSwRev.setStatus("mandatory")
_WtDevType_Type = DisplayString
_WtDevType_Object = MibScalar
wtDevType = _WtDevType_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 5),
    _WtDevType_Type()
)
wtDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDevType.setStatus("mandatory")
_WtMibRev_Type = DisplayString
_WtMibRev_Object = MibScalar
wtMibRev = _WtMibRev_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 6),
    _WtMibRev_Type()
)
wtMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtMibRev.setStatus("mandatory")
_WtRunTime_Type = TimeTicks
_WtRunTime_Object = MibScalar
wtRunTime = _WtRunTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 7),
    _WtRunTime_Type()
)
wtRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtRunTime.setStatus("mandatory")


class _WtPhysPorts_Type(Integer32):
    """Custom type wtPhysPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtPhysPorts_Type.__name__ = "Integer32"
_WtPhysPorts_Object = MibScalar
wtPhysPorts = _WtPhysPorts_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 8),
    _WtPhysPorts_Type()
)
wtPhysPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtPhysPorts.setStatus("mandatory")


class _WtConfigMode_Type(Integer32):
    """Custom type wtConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wtConfigModeOff", 1),
          ("wtConfigModeOn", 2),
          ("wtSaveConfig", 3))
    )


_WtConfigMode_Type.__name__ = "Integer32"
_WtConfigMode_Object = MibScalar
wtConfigMode = _WtConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 16),
    _WtConfigMode_Type()
)
wtConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtConfigMode.setStatus("mandatory")


class _WtPassword_Type(DisplayString):
    """Custom type wtPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WtPassword_Type.__name__ = "DisplayString"
_WtPassword_Object = MibScalar
wtPassword = _WtPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 17),
    _WtPassword_Type()
)
wtPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtPassword.setStatus("mandatory")
_WtSysPswd_Type = OctetString
_WtSysPswd_Object = MibScalar
wtSysPswd = _WtSysPswd_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 18),
    _WtSysPswd_Type()
)
wtSysPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSysPswd.setStatus("mandatory")
_WtSysName_Type = OctetString
_WtSysName_Object = MibScalar
wtSysName = _WtSysName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 1, 19),
    _WtSysName_Type()
)
wtSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSysName.setStatus("mandatory")
_WtNetSetup_ObjectIdentity = ObjectIdentity
wtNetSetup = _WtNetSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2)
)
_WtIpAddress_Type = IpAddress
_WtIpAddress_Object = MibScalar
wtIpAddress = _WtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 1),
    _WtIpAddress_Type()
)
wtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtIpAddress.setStatus("mandatory")
_WtSubnetMask_Type = IpAddress
_WtSubnetMask_Object = MibScalar
wtSubnetMask = _WtSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 2),
    _WtSubnetMask_Type()
)
wtSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSubnetMask.setStatus("mandatory")
_WtGateway_Type = IpAddress
_WtGateway_Object = MibScalar
wtGateway = _WtGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 3),
    _WtGateway_Type()
)
wtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtGateway.setStatus("mandatory")


class _WtMtu_Type(Integer32):
    """Custom type wtMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1024),
    )


_WtMtu_Type.__name__ = "Integer32"
_WtMtu_Object = MibScalar
wtMtu = _WtMtu_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 4),
    _WtMtu_Type()
)
wtMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtMtu.setStatus("mandatory")


class _WtBootpClient_Type(Integer32):
    """Custom type wtBootpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtBootpClientOff", 1),
          ("wtBootpClientOn", 2))
    )


_WtBootpClient_Type.__name__ = "Integer32"
_WtBootpClient_Object = MibScalar
wtBootpClient = _WtBootpClient_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 5),
    _WtBootpClient_Type()
)
wtBootpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtBootpClient.setStatus("mandatory")


class _WtKeepAlive_Type(Integer32):
    """Custom type wtKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_WtKeepAlive_Type.__name__ = "Integer32"
_WtKeepAlive_Object = MibScalar
wtKeepAlive = _WtKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 6),
    _WtKeepAlive_Type()
)
wtKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtKeepAlive.setStatus("mandatory")


class _WtRetransmTimeout_Type(Integer32):
    """Custom type wtRetransmTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtRetransmTimeout_Type.__name__ = "Integer32"
_WtRetransmTimeout_Object = MibScalar
wtRetransmTimeout = _WtRetransmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 7),
    _WtRetransmTimeout_Type()
)
wtRetransmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtRetransmTimeout.setStatus("mandatory")


class _WtDhcpClient_Type(Integer32):
    """Custom type wtDhcpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtChcpClientOn", 2),
          ("wtDhcpClientOff", 1))
    )


_WtDhcpClient_Type.__name__ = "Integer32"
_WtDhcpClient_Object = MibScalar
wtDhcpClient = _WtDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 8),
    _WtDhcpClient_Type()
)
wtDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDhcpClient.setStatus("mandatory")


class _WtWbmPort_Type(Integer32):
    """Custom type wtWbmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWbmPort_Type.__name__ = "Integer32"
_WtWbmPort_Object = MibScalar
wtWbmPort = _WtWbmPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 9),
    _WtWbmPort_Type()
)
wtWbmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWbmPort.setStatus("mandatory")
_WtDnsSrv_Type = IpAddress
_WtDnsSrv_Object = MibScalar
wtDnsSrv = _WtDnsSrv_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 10),
    _WtDnsSrv_Type()
)
wtDnsSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDnsSrv.setStatus("mandatory")


class _WtLinkSpeed_Type(Integer32):
    """Custom type wtLinkSpeed based on Integer32"""
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
        *(("wtLinkSpeed100FD", 5),
          ("wtLinkSpeed100HD", 4),
          ("wtLinkSpeed10FD", 3),
          ("wtLinkSpeed10HD", 2),
          ("wtLinkSpeedAutonegotiation", 1))
    )


_WtLinkSpeed_Type.__name__ = "Integer32"
_WtLinkSpeed_Object = MibScalar
wtLinkSpeed = _WtLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 2, 11),
    _WtLinkSpeed_Type()
)
wtLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtLinkSpeed.setStatus("mandatory")
_WtSeriPortSetup_ObjectIdentity = ObjectIdentity
wtSeriPortSetup = _WtSeriPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3)
)


class _WtSerialPorts_Type(Integer32):
    """Custom type wtSerialPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtSerialPorts_Type.__name__ = "Integer32"
_WtSerialPorts_Object = MibScalar
wtSerialPorts = _WtSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 1),
    _WtSerialPorts_Type()
)
wtSerialPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSerialPorts.setStatus("mandatory")
_WtSeriInterfaceTable_Object = MibTable
wtSeriInterfaceTable = _WtSeriInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wtSeriInterfaceTable.setStatus("mandatory")
_WtSeriInterfaceEntry_Object = MibTableRow
wtSeriInterfaceEntry = _WtSeriInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 2, 1)
)
wtSeriInterfaceEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriInterfaceEntry.setStatus("mandatory")


class _WtSeriInterfaceNo_Type(Integer32):
    """Custom type wtSeriInterfaceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtSeriInterfaceNo_Type.__name__ = "Integer32"
_WtSeriInterfaceNo_Object = MibTableColumn
wtSeriInterfaceNo = _WtSeriInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 2, 1, 1),
    _WtSeriInterfaceNo_Type()
)
wtSeriInterfaceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriInterfaceNo.setStatus("mandatory")
_WtSeriUartTable_Object = MibTable
wtSeriUartTable = _WtSeriUartTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wtSeriUartTable.setStatus("mandatory")
_WtSeriUartEntry_Object = MibTableRow
wtSeriUartEntry = _WtSeriUartEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1)
)
wtSeriUartEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriUartEntry.setStatus("mandatory")


class _WtBaudrate_Type(Integer32):
    """Custom type wtBaudrate based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("wtBaudrate-110", 12),
          ("wtBaudrate-115200", 16),
          ("wtBaudrate-1200", 8),
          ("wtBaudrate-14400", 4),
          ("wtBaudrate-150", 11),
          ("wtBaudrate-19200", 3),
          ("wtBaudrate-230400", 15),
          ("wtBaudrate-2400", 7),
          ("wtBaudrate-300", 10),
          ("wtBaudrate-38400", 2),
          ("wtBaudrate-4800", 6),
          ("wtBaudrate-50", 14),
          ("wtBaudrate-57600", 1),
          ("wtBaudrate-600", 9),
          ("wtBaudrate-7200", 17),
          ("wtBaudrate-75", 13),
          ("wtBaudrate-9600", 5),
          ("wtBaudrate-special", 18))
    )


_WtBaudrate_Type.__name__ = "Integer32"
_WtBaudrate_Object = MibTableColumn
wtBaudrate = _WtBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 1),
    _WtBaudrate_Type()
)
wtBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtBaudrate.setStatus("mandatory")


class _WtParity_Type(Integer32):
    """Custom type wtParity based on Integer32"""
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
        *(("wtEvenParity", 3),
          ("wtMarkEvenParity", 5),
          ("wtMarkOddParity", 4),
          ("wtNoParity", 1),
          ("wtOddParity", 2))
    )


_WtParity_Type.__name__ = "Integer32"
_WtParity_Object = MibTableColumn
wtParity = _WtParity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 2),
    _WtParity_Type()
)
wtParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtParity.setStatus("mandatory")


class _WtDatabits_Type(Integer32):
    """Custom type wtDatabits based on Integer32"""
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
        *(("wtDataBits-5", 4),
          ("wtDataBits-6", 3),
          ("wtDataBits-7", 2),
          ("wtDataBits-8", 1))
    )


_WtDatabits_Type.__name__ = "Integer32"
_WtDatabits_Object = MibTableColumn
wtDatabits = _WtDatabits_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 3),
    _WtDatabits_Type()
)
wtDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDatabits.setStatus("mandatory")


class _WtStopbits_Type(Integer32):
    """Custom type wtStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtStopBits-1", 1),
          ("wtStopBits-2", 2))
    )


_WtStopbits_Type.__name__ = "Integer32"
_WtStopbits_Object = MibTableColumn
wtStopbits = _WtStopbits_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 4),
    _WtStopbits_Type()
)
wtStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtStopbits.setStatus("mandatory")


class _WtHsLines_Type(OctetString):
    """Custom type wtHsLines based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtHsLines_Type.__name__ = "OctetString"
_WtHsLines_Object = MibTableColumn
wtHsLines = _WtHsLines_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 5),
    _WtHsLines_Type()
)
wtHsLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtHsLines.setStatus("mandatory")


class _WtHsFunctions_Type(OctetString):
    """Custom type wtHsFunctions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtHsFunctions_Type.__name__ = "OctetString"
_WtHsFunctions_Object = MibTableColumn
wtHsFunctions = _WtHsFunctions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 6),
    _WtHsFunctions_Type()
)
wtHsFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtHsFunctions.setStatus("mandatory")


class _WtUartFifo_Type(Integer32):
    """Custom type wtUartFifo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wtUartFifo-16-16", 3),
          ("wtUartFifo-32-56", 5),
          ("wtUartFifo-56-60", 7),
          ("wtUartFifo-8-8", 1),
          ("wtUartFifo-disable", 0))
    )


_WtUartFifo_Type.__name__ = "Integer32"
_WtUartFifo_Object = MibTableColumn
wtUartFifo = _WtUartFifo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 7),
    _WtUartFifo_Type()
)
wtUartFifo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtUartFifo.setStatus("mandatory")


class _WtUartBaudrate_Type(Integer32):
    """Custom type wtUartBaudrate based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("wtUartBaudrate-110", 17),
          ("wtUartBaudrate-115200", 3),
          ("wtUartBaudrate-1200", 11),
          ("wtUartBaudrate-150", 14),
          ("wtUartBaudrate-153600", 2),
          ("wtUartBaudrate-19200", 6),
          ("wtUartBaudrate-230400", 1),
          ("wtUartBaudrate-2400", 10),
          ("wtUartBaudrate-300", 13),
          ("wtUartBaudrate-38400", 5),
          ("wtUartBaudrate-4800", 9),
          ("wtUartBaudrate-50", 16),
          ("wtUartBaudrate-57600", 4),
          ("wtUartBaudrate-600", 12),
          ("wtUartBaudrate-7200", 8),
          ("wtUartBaudrate-75", 15),
          ("wtUartBaudrate-9600", 7),
          ("wtUartBaudrate-special", 18))
    )


_WtUartBaudrate_Type.__name__ = "Integer32"
_WtUartBaudrate_Object = MibTableColumn
wtUartBaudrate = _WtUartBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 8),
    _WtUartBaudrate_Type()
)
wtUartBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtUartBaudrate.setStatus("mandatory")


class _WtBaudDivisor_Type(Integer32):
    """Custom type wtBaudDivisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WtBaudDivisor_Type.__name__ = "Integer32"
_WtBaudDivisor_Object = MibTableColumn
wtBaudDivisor = _WtBaudDivisor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 9),
    _WtBaudDivisor_Type()
)
wtBaudDivisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtBaudDivisor.setStatus("mandatory")


class _WtSeriInQueue_Type(Integer32):
    """Custom type wtSeriInQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4094),
    )


_WtSeriInQueue_Type.__name__ = "Integer32"
_WtSeriInQueue_Object = MibTableColumn
wtSeriInQueue = _WtSeriInQueue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 3, 1, 10),
    _WtSeriInQueue_Type()
)
wtSeriInQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriInQueue.setStatus("mandatory")
_WtSeriPortTable_Object = MibTable
wtSeriPortTable = _WtSeriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    wtSeriPortTable.setStatus("mandatory")
_WtSeriPortEntry_Object = MibTableRow
wtSeriPortEntry = _WtSeriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1)
)
wtSeriPortEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriPortEntry.setStatus("mandatory")


class _WtSeriLocalPort_Type(Integer32):
    """Custom type wtSeriLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtSeriLocalPort_Type.__name__ = "Integer32"
_WtSeriLocalPort_Object = MibTableColumn
wtSeriLocalPort = _WtSeriLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 1),
    _WtSeriLocalPort_Type()
)
wtSeriLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriLocalPort.setStatus("mandatory")


class _WtSeriPortMode_Type(Integer32):
    """Custom type wtSeriPortMode based on Integer32"""
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
        *(("wtSeriBox2BoxMaster", 5),
          ("wtSeriBox2BoxSlave", 8),
          ("wtSeriFtpClient", 4),
          ("wtSeriIpBusMaster", 11),
          ("wtSeriIpBusSlave", 10),
          ("wtSeriMultiportProtokoll", 7),
          ("wtSeriServerMode", 1),
          ("wtSeriSlipMode", 9),
          ("wtSeriTcpClient", 2),
          ("wtSeriTelnetClient", 3),
          ("wtSeriUdpMode", 6))
    )


_WtSeriPortMode_Type.__name__ = "Integer32"
_WtSeriPortMode_Object = MibTableColumn
wtSeriPortMode = _WtSeriPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 2),
    _WtSeriPortMode_Type()
)
wtSeriPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriPortMode.setStatus("mandatory")


class _WtSeriControlPort_Type(Integer32):
    """Custom type wtSeriControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriControlPort_Type.__name__ = "Integer32"
_WtSeriControlPort_Object = MibTableColumn
wtSeriControlPort = _WtSeriControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 3),
    _WtSeriControlPort_Type()
)
wtSeriControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriControlPort.setStatus("mandatory")


class _WtSeriPortState_Type(Integer32):
    """Custom type wtSeriPortState based on Integer32"""
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
        *(("wtSeriPortFree", 0),
          ("wtSeriPortInUse", 1),
          ("wtSeriPortLockConnected", 3),
          ("wtSeriPortLockScanning", 2),
          ("wtSeriPortLockUnconnected", 4))
    )


_WtSeriPortState_Type.__name__ = "Integer32"
_WtSeriPortState_Object = MibTableColumn
wtSeriPortState = _WtSeriPortState_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 4),
    _WtSeriPortState_Type()
)
wtSeriPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriPortState.setStatus("mandatory")


class _WtSeriRemotePort_Type(Integer32):
    """Custom type wtSeriRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriRemotePort_Type.__name__ = "Integer32"
_WtSeriRemotePort_Object = MibTableColumn
wtSeriRemotePort = _WtSeriRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 5),
    _WtSeriRemotePort_Type()
)
wtSeriRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriRemotePort.setStatus("mandatory")
_WtSeriRemoteIP_Type = IpAddress
_WtSeriRemoteIP_Object = MibTableColumn
wtSeriRemoteIP = _WtSeriRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 6),
    _WtSeriRemoteIP_Type()
)
wtSeriRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriRemoteIP.setStatus("mandatory")


class _WtSeriNetPckDelay_Type(Integer32):
    """Custom type wtSeriNetPckDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriNetPckDelay_Type.__name__ = "Integer32"
_WtSeriNetPckDelay_Object = MibTableColumn
wtSeriNetPckDelay = _WtSeriNetPckDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 10),
    _WtSeriNetPckDelay_Type()
)
wtSeriNetPckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriNetPckDelay.setStatus("mandatory")


class _WtSeriFlushBuf_Type(Integer32):
    """Custom type wtSeriFlushBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriFlushBufOff", 1),
          ("wtSeriFlushBufOn", 2))
    )


_WtSeriFlushBuf_Type.__name__ = "Integer32"
_WtSeriFlushBuf_Object = MibTableColumn
wtSeriFlushBuf = _WtSeriFlushBuf_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 11),
    _WtSeriFlushBuf_Type()
)
wtSeriFlushBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFlushBuf.setStatus("mandatory")


class _WtSeriTelnetEcho_Type(Integer32):
    """Custom type wtSeriTelnetEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriTelnetEchoOff", 1),
          ("wtSeriTelnetEchoOn", 2))
    )


_WtSeriTelnetEcho_Type.__name__ = "Integer32"
_WtSeriTelnetEcho_Object = MibTableColumn
wtSeriTelnetEcho = _WtSeriTelnetEcho_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 4, 1, 12),
    _WtSeriTelnetEcho_Type()
)
wtSeriTelnetEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetEcho.setStatus("mandatory")
_WtSeriTcpClientTable_Object = MibTable
wtSeriTcpClientTable = _WtSeriTcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    wtSeriTcpClientTable.setStatus("mandatory")
_WtSeriTcpClientEntry_Object = MibTableRow
wtSeriTcpClientEntry = _WtSeriTcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1)
)
wtSeriTcpClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriTcpClientEntry.setStatus("mandatory")


class _WtSeriTcpServerPort_Type(Integer32):
    """Custom type wtSeriTcpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriTcpServerPort_Type.__name__ = "Integer32"
_WtSeriTcpServerPort_Object = MibTableColumn
wtSeriTcpServerPort = _WtSeriTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 1),
    _WtSeriTcpServerPort_Type()
)
wtSeriTcpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpServerPort.setStatus("mandatory")
_WtSeriTcpServerIp_Type = IpAddress
_WtSeriTcpServerIp_Object = MibTableColumn
wtSeriTcpServerIp = _WtSeriTcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 2),
    _WtSeriTcpServerIp_Type()
)
wtSeriTcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpServerIp.setStatus("mandatory")


class _WtSeriTcpInactTimeout_Type(Integer32):
    """Custom type wtSeriTcpInactTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriTcpInactTimeout_Type.__name__ = "Integer32"
_WtSeriTcpInactTimeout_Object = MibTableColumn
wtSeriTcpInactTimeout = _WtSeriTcpInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 3),
    _WtSeriTcpInactTimeout_Type()
)
wtSeriTcpInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpInactTimeout.setStatus("mandatory")


class _WtSeriTcpConnectTimeout_Type(Integer32):
    """Custom type wtSeriTcpConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriTcpConnectTimeout_Type.__name__ = "Integer32"
_WtSeriTcpConnectTimeout_Object = MibTableColumn
wtSeriTcpConnectTimeout = _WtSeriTcpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 4),
    _WtSeriTcpConnectTimeout_Type()
)
wtSeriTcpConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpConnectTimeout.setStatus("mandatory")


class _WtSeriTcpDisconnectChar_Type(OctetString):
    """Custom type wtSeriTcpDisconnectChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtSeriTcpDisconnectChar_Type.__name__ = "OctetString"
_WtSeriTcpDisconnectChar_Object = MibTableColumn
wtSeriTcpDisconnectChar = _WtSeriTcpDisconnectChar_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 5),
    _WtSeriTcpDisconnectChar_Type()
)
wtSeriTcpDisconnectChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpDisconnectChar.setStatus("mandatory")


class _WtSeriTcpDispString1_Type(OctetString):
    """Custom type wtSeriTcpDispString1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriTcpDispString1_Type.__name__ = "OctetString"
_WtSeriTcpDispString1_Object = MibTableColumn
wtSeriTcpDispString1 = _WtSeriTcpDispString1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 6),
    _WtSeriTcpDispString1_Type()
)
wtSeriTcpDispString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpDispString1.setStatus("mandatory")


class _WtSeriTcpDispString2_Type(OctetString):
    """Custom type wtSeriTcpDispString2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriTcpDispString2_Type.__name__ = "OctetString"
_WtSeriTcpDispString2_Object = MibTableColumn
wtSeriTcpDispString2 = _WtSeriTcpDispString2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 7),
    _WtSeriTcpDispString2_Type()
)
wtSeriTcpDispString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpDispString2.setStatus("mandatory")


class _WtSeriTcpCAddress_Type(Integer32):
    """Custom type wtSeriTcpCAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriTcpCAddressOff", 1),
          ("wtSeriTcpCAddressOn", 2))
    )


_WtSeriTcpCAddress_Type.__name__ = "Integer32"
_WtSeriTcpCAddress_Object = MibTableColumn
wtSeriTcpCAddress = _WtSeriTcpCAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 8),
    _WtSeriTcpCAddress_Type()
)
wtSeriTcpCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpCAddress.setStatus("mandatory")


class _WtSeriTcpResponseMode_Type(Integer32):
    """Custom type wtSeriTcpResponseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriTcpRespModeOff", 1),
          ("wtSeriTcpRespModeOn", 2))
    )


_WtSeriTcpResponseMode_Type.__name__ = "Integer32"
_WtSeriTcpResponseMode_Object = MibTableColumn
wtSeriTcpResponseMode = _WtSeriTcpResponseMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 10),
    _WtSeriTcpResponseMode_Type()
)
wtSeriTcpResponseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpResponseMode.setStatus("mandatory")
_WtSeriTcpServerUrl_Type = OctetString
_WtSeriTcpServerUrl_Object = MibTableColumn
wtSeriTcpServerUrl = _WtSeriTcpServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 5, 1, 11),
    _WtSeriTcpServerUrl_Type()
)
wtSeriTcpServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTcpServerUrl.setStatus("mandatory")
_WtSeriUdpClientTable_Object = MibTable
wtSeriUdpClientTable = _WtSeriUdpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    wtSeriUdpClientTable.setStatus("mandatory")
_WtSeriUdpClientEntry_Object = MibTableRow
wtSeriUdpClientEntry = _WtSeriUdpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1)
)
wtSeriUdpClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriUdpClientEntry.setStatus("mandatory")


class _WtSeriUdpServerPort_Type(Integer32):
    """Custom type wtSeriUdpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriUdpServerPort_Type.__name__ = "Integer32"
_WtSeriUdpServerPort_Object = MibTableColumn
wtSeriUdpServerPort = _WtSeriUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 1),
    _WtSeriUdpServerPort_Type()
)
wtSeriUdpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpServerPort.setStatus("mandatory")
_WtSeriUdpServerIp_Type = IpAddress
_WtSeriUdpServerIp_Object = MibTableColumn
wtSeriUdpServerIp = _WtSeriUdpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 2),
    _WtSeriUdpServerIp_Type()
)
wtSeriUdpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpServerIp.setStatus("mandatory")


class _WtSeriUdpDispString1_Type(OctetString):
    """Custom type wtSeriUdpDispString1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriUdpDispString1_Type.__name__ = "OctetString"
_WtSeriUdpDispString1_Object = MibTableColumn
wtSeriUdpDispString1 = _WtSeriUdpDispString1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 3),
    _WtSeriUdpDispString1_Type()
)
wtSeriUdpDispString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpDispString1.setStatus("mandatory")


class _WtSeriUdpDispString2_Type(OctetString):
    """Custom type wtSeriUdpDispString2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriUdpDispString2_Type.__name__ = "OctetString"
_WtSeriUdpDispString2_Object = MibTableColumn
wtSeriUdpDispString2 = _WtSeriUdpDispString2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 4),
    _WtSeriUdpDispString2_Type()
)
wtSeriUdpDispString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpDispString2.setStatus("mandatory")


class _WtSeriUdpSeriProtocol_Type(Integer32):
    """Custom type wtSeriUdpSeriProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriUdpProtocolOff", 1),
          ("wtSeriUdpProtocolOn", 2))
    )


_WtSeriUdpSeriProtocol_Type.__name__ = "Integer32"
_WtSeriUdpSeriProtocol_Object = MibTableColumn
wtSeriUdpSeriProtocol = _WtSeriUdpSeriProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 5),
    _WtSeriUdpSeriProtocol_Type()
)
wtSeriUdpSeriProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpSeriProtocol.setStatus("mandatory")


class _WtSeriUdpSeriCoding_Type(Integer32):
    """Custom type wtSeriUdpSeriCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriUdpSeriCodingOff", 1),
          ("wtSeriUdpSeriCodingOn", 2))
    )


_WtSeriUdpSeriCoding_Type.__name__ = "Integer32"
_WtSeriUdpSeriCoding_Object = MibTableColumn
wtSeriUdpSeriCoding = _WtSeriUdpSeriCoding_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 6),
    _WtSeriUdpSeriCoding_Type()
)
wtSeriUdpSeriCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpSeriCoding.setStatus("mandatory")


class _WtSeriUdpCAddress_Type(Integer32):
    """Custom type wtSeriUdpCAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriUdpCAddressOff", 1),
          ("wtSeriUdpCAddressOn", 2))
    )


_WtSeriUdpCAddress_Type.__name__ = "Integer32"
_WtSeriUdpCAddress_Object = MibTableColumn
wtSeriUdpCAddress = _WtSeriUdpCAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 7),
    _WtSeriUdpCAddress_Type()
)
wtSeriUdpCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpCAddress.setStatus("mandatory")


class _WtSeriUdpWrCAddress_Type(Integer32):
    """Custom type wtSeriUdpWrCAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriUdpWrCAddressOff", 1),
          ("wtSeriUdpWrCAddressOn", 2))
    )


_WtSeriUdpWrCAddress_Type.__name__ = "Integer32"
_WtSeriUdpWrCAddress_Object = MibTableColumn
wtSeriUdpWrCAddress = _WtSeriUdpWrCAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 8),
    _WtSeriUdpWrCAddress_Type()
)
wtSeriUdpWrCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpWrCAddress.setStatus("mandatory")


class _WtSeriUdpDisconnectChar_Type(OctetString):
    """Custom type wtSeriUdpDisconnectChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtSeriUdpDisconnectChar_Type.__name__ = "OctetString"
_WtSeriUdpDisconnectChar_Object = MibTableColumn
wtSeriUdpDisconnectChar = _WtSeriUdpDisconnectChar_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 9),
    _WtSeriUdpDisconnectChar_Type()
)
wtSeriUdpDisconnectChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpDisconnectChar.setStatus("mandatory")
_WtSeriUdpServerUrl_Type = OctetString
_WtSeriUdpServerUrl_Object = MibTableColumn
wtSeriUdpServerUrl = _WtSeriUdpServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 6, 1, 10),
    _WtSeriUdpServerUrl_Type()
)
wtSeriUdpServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriUdpServerUrl.setStatus("mandatory")
_WtSeriTelnetClientTable_Object = MibTable
wtSeriTelnetClientTable = _WtSeriTelnetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    wtSeriTelnetClientTable.setStatus("mandatory")
_WtSeriTelnetClientEntry_Object = MibTableRow
wtSeriTelnetClientEntry = _WtSeriTelnetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1)
)
wtSeriTelnetClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriTelnetClientEntry.setStatus("mandatory")


class _WtSeriTelnetServerPort_Type(Integer32):
    """Custom type wtSeriTelnetServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriTelnetServerPort_Type.__name__ = "Integer32"
_WtSeriTelnetServerPort_Object = MibTableColumn
wtSeriTelnetServerPort = _WtSeriTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 1),
    _WtSeriTelnetServerPort_Type()
)
wtSeriTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetServerPort.setStatus("mandatory")
_WtSeriTelnetServerIp_Type = IpAddress
_WtSeriTelnetServerIp_Object = MibTableColumn
wtSeriTelnetServerIp = _WtSeriTelnetServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 2),
    _WtSeriTelnetServerIp_Type()
)
wtSeriTelnetServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetServerIp.setStatus("mandatory")


class _WtSeriTelnetInactTimeout_Type(Integer32):
    """Custom type wtSeriTelnetInactTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriTelnetInactTimeout_Type.__name__ = "Integer32"
_WtSeriTelnetInactTimeout_Object = MibTableColumn
wtSeriTelnetInactTimeout = _WtSeriTelnetInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 3),
    _WtSeriTelnetInactTimeout_Type()
)
wtSeriTelnetInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetInactTimeout.setStatus("mandatory")


class _WtSeriTelnetDisconnectChar_Type(OctetString):
    """Custom type wtSeriTelnetDisconnectChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtSeriTelnetDisconnectChar_Type.__name__ = "OctetString"
_WtSeriTelnetDisconnectChar_Object = MibTableColumn
wtSeriTelnetDisconnectChar = _WtSeriTelnetDisconnectChar_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 4),
    _WtSeriTelnetDisconnectChar_Type()
)
wtSeriTelnetDisconnectChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetDisconnectChar.setStatus("mandatory")


class _WtSeriTelnetChangeLineout_Type(Integer32):
    """Custom type wtSeriTelnetChangeLineout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriTelnetChangeLineoutOff", 1),
          ("wtSeriTelnetChangeLineoutOn", 2))
    )


_WtSeriTelnetChangeLineout_Type.__name__ = "Integer32"
_WtSeriTelnetChangeLineout_Object = MibTableColumn
wtSeriTelnetChangeLineout = _WtSeriTelnetChangeLineout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 5),
    _WtSeriTelnetChangeLineout_Type()
)
wtSeriTelnetChangeLineout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetChangeLineout.setStatus("mandatory")
_WtSeriTelnetServerUrl_Type = OctetString
_WtSeriTelnetServerUrl_Object = MibTableColumn
wtSeriTelnetServerUrl = _WtSeriTelnetServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 7, 1, 6),
    _WtSeriTelnetServerUrl_Type()
)
wtSeriTelnetServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriTelnetServerUrl.setStatus("mandatory")
_WtSeriFtpClientTable_Object = MibTable
wtSeriFtpClientTable = _WtSeriFtpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    wtSeriFtpClientTable.setStatus("mandatory")
_WtSeriFtpClientEntry_Object = MibTableRow
wtSeriFtpClientEntry = _WtSeriFtpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1)
)
wtSeriFtpClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriFtpClientEntry.setStatus("mandatory")


class _WtSeriFtpServerPort_Type(Integer32):
    """Custom type wtSeriFtpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriFtpServerPort_Type.__name__ = "Integer32"
_WtSeriFtpServerPort_Object = MibTableColumn
wtSeriFtpServerPort = _WtSeriFtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 1),
    _WtSeriFtpServerPort_Type()
)
wtSeriFtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpServerPort.setStatus("mandatory")
_WtSeriFtpServerIp_Type = IpAddress
_WtSeriFtpServerIp_Object = MibTableColumn
wtSeriFtpServerIp = _WtSeriFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 2),
    _WtSeriFtpServerIp_Type()
)
wtSeriFtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpServerIp.setStatus("mandatory")


class _WtSeriFtpAutoFtp_Type(Integer32):
    """Custom type wtSeriFtpAutoFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriAutoFtpOff", 1),
          ("wtSeriAutoFtpOn", 2))
    )


_WtSeriFtpAutoFtp_Type.__name__ = "Integer32"
_WtSeriFtpAutoFtp_Object = MibTableColumn
wtSeriFtpAutoFtp = _WtSeriFtpAutoFtp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 3),
    _WtSeriFtpAutoFtp_Type()
)
wtSeriFtpAutoFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpAutoFtp.setStatus("mandatory")
_WtSeriFtpLoginString_Type = OctetString
_WtSeriFtpLoginString_Object = MibTableColumn
wtSeriFtpLoginString = _WtSeriFtpLoginString_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 4),
    _WtSeriFtpLoginString_Type()
)
wtSeriFtpLoginString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpLoginString.setStatus("mandatory")


class _WtSeriFtpInactTimeout_Type(Integer32):
    """Custom type wtSeriFtpInactTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriFtpInactTimeout_Type.__name__ = "Integer32"
_WtSeriFtpInactTimeout_Object = MibTableColumn
wtSeriFtpInactTimeout = _WtSeriFtpInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 5),
    _WtSeriFtpInactTimeout_Type()
)
wtSeriFtpInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpInactTimeout.setStatus("mandatory")


class _WtSeriFtpConnectTimeout_Type(Integer32):
    """Custom type wtSeriFtpConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtSeriFtpConnectTimeout_Type.__name__ = "Integer32"
_WtSeriFtpConnectTimeout_Object = MibTableColumn
wtSeriFtpConnectTimeout = _WtSeriFtpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 6),
    _WtSeriFtpConnectTimeout_Type()
)
wtSeriFtpConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpConnectTimeout.setStatus("mandatory")


class _WtSeriFtpProtocolChar_Type(OctetString):
    """Custom type wtSeriFtpProtocolChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtSeriFtpProtocolChar_Type.__name__ = "OctetString"
_WtSeriFtpProtocolChar_Object = MibTableColumn
wtSeriFtpProtocolChar = _WtSeriFtpProtocolChar_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 7),
    _WtSeriFtpProtocolChar_Type()
)
wtSeriFtpProtocolChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpProtocolChar.setStatus("mandatory")
_WtSeriFtpServerUrl_Type = OctetString
_WtSeriFtpServerUrl_Object = MibTableColumn
wtSeriFtpServerUrl = _WtSeriFtpServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 8, 1, 8),
    _WtSeriFtpServerUrl_Type()
)
wtSeriFtpServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriFtpServerUrl.setStatus("mandatory")
_WtSeriMultiPortPrtTable_Object = MibTable
wtSeriMultiPortPrtTable = _WtSeriMultiPortPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    wtSeriMultiPortPrtTable.setStatus("mandatory")
_WtSeriMultiPortPrtEntry_Object = MibTableRow
wtSeriMultiPortPrtEntry = _WtSeriMultiPortPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 9, 1)
)
wtSeriMultiPortPrtEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriMultiPortPrtEntry.setStatus("mandatory")


class _WtSeriPrtSeriProtocol_Type(Integer32):
    """Custom type wtSeriPrtSeriProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriPrtSeriProtocolOff", 1),
          ("wtSeriPrtSeriProtocolOn", 2))
    )


_WtSeriPrtSeriProtocol_Type.__name__ = "Integer32"
_WtSeriPrtSeriProtocol_Object = MibTableColumn
wtSeriPrtSeriProtocol = _WtSeriPrtSeriProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 9, 1, 1),
    _WtSeriPrtSeriProtocol_Type()
)
wtSeriPrtSeriProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriPrtSeriProtocol.setStatus("mandatory")


class _WtSeriPrtSeriCoding_Type(Integer32):
    """Custom type wtSeriPrtSeriCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriPrtSeriCodingOff", 1),
          ("wtSeriPrtSeriCodingOn", 2))
    )


_WtSeriPrtSeriCoding_Type.__name__ = "Integer32"
_WtSeriPrtSeriCoding_Object = MibTableColumn
wtSeriPrtSeriCoding = _WtSeriPrtSeriCoding_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 9, 1, 2),
    _WtSeriPrtSeriCoding_Type()
)
wtSeriPrtSeriCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriPrtSeriCoding.setStatus("mandatory")


class _WtSeriPrtProtocolChar_Type(OctetString):
    """Custom type wtSeriPrtProtocolChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_WtSeriPrtProtocolChar_Type.__name__ = "OctetString"
_WtSeriPrtProtocolChar_Object = MibTableColumn
wtSeriPrtProtocolChar = _WtSeriPrtProtocolChar_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 9, 1, 3),
    _WtSeriPrtProtocolChar_Type()
)
wtSeriPrtProtocolChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriPrtProtocolChar.setStatus("mandatory")
_WtSeriB2bMasterTable_Object = MibTable
wtSeriB2bMasterTable = _WtSeriB2bMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    wtSeriB2bMasterTable.setStatus("mandatory")
_WtSeriB2bMasterEntry_Object = MibTableRow
wtSeriB2bMasterEntry = _WtSeriB2bMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10, 1)
)
wtSeriB2bMasterEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriB2bMasterEntry.setStatus("mandatory")


class _WtSeriB2bMaster_SlavePort_Type(Integer32):
    """Custom type wtSeriB2bMaster_SlavePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtSeriB2bMaster_SlavePort_Type.__name__ = "Integer32"
_WtSeriB2bMaster_SlavePort_Object = MibScalar
wtSeriB2bMaster_SlavePort = _WtSeriB2bMaster_SlavePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10, 1, 1),
    _WtSeriB2bMaster_SlavePort_Type()
)
wtSeriB2bMaster_SlavePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bMaster_SlavePort.setStatus("mandatory")
_WtSeriB2bMaster_SlaveIp_Type = IpAddress
_WtSeriB2bMaster_SlaveIp_Object = MibScalar
wtSeriB2bMaster_SlaveIp = _WtSeriB2bMaster_SlaveIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10, 1, 2),
    _WtSeriB2bMaster_SlaveIp_Type()
)
wtSeriB2bMaster_SlaveIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bMaster_SlaveIp.setStatus("mandatory")


class _WtSeriB2bMaster_DispString1_Type(OctetString):
    """Custom type wtSeriB2bMaster_DispString1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriB2bMaster_DispString1_Type.__name__ = "OctetString"
_WtSeriB2bMaster_DispString1_Object = MibScalar
wtSeriB2bMaster_DispString1 = _WtSeriB2bMaster_DispString1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10, 1, 3),
    _WtSeriB2bMaster_DispString1_Type()
)
wtSeriB2bMaster_DispString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bMaster_DispString1.setStatus("mandatory")


class _WtSeriB2bMaster_DispString2_Type(OctetString):
    """Custom type wtSeriB2bMaster_DispString2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriB2bMaster_DispString2_Type.__name__ = "OctetString"
_WtSeriB2bMaster_DispString2_Object = MibScalar
wtSeriB2bMaster_DispString2 = _WtSeriB2bMaster_DispString2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 10, 1, 4),
    _WtSeriB2bMaster_DispString2_Type()
)
wtSeriB2bMaster_DispString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bMaster_DispString2.setStatus("mandatory")
_WtSeriB2bSlaveTable_Object = MibTable
wtSeriB2bSlaveTable = _WtSeriB2bSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    wtSeriB2bSlaveTable.setStatus("mandatory")
_WtSeriB2bSlaveEntry_Object = MibTableRow
wtSeriB2bSlaveEntry = _WtSeriB2bSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11, 1)
)
wtSeriB2bSlaveEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriB2bSlaveEntry.setStatus("mandatory")


class _WtSeriB2bSlave_MasterPort_Type(Integer32):
    """Custom type wtSeriB2bSlave_MasterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtSeriB2bSlave_MasterPort_Type.__name__ = "Integer32"
_WtSeriB2bSlave_MasterPort_Object = MibScalar
wtSeriB2bSlave_MasterPort = _WtSeriB2bSlave_MasterPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11, 1, 1),
    _WtSeriB2bSlave_MasterPort_Type()
)
wtSeriB2bSlave_MasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriB2bSlave_MasterPort.setStatus("mandatory")
_WtSeriB2bSlave_MasterIp_Type = IpAddress
_WtSeriB2bSlave_MasterIp_Object = MibScalar
wtSeriB2bSlave_MasterIp = _WtSeriB2bSlave_MasterIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11, 1, 2),
    _WtSeriB2bSlave_MasterIp_Type()
)
wtSeriB2bSlave_MasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtSeriB2bSlave_MasterIp.setStatus("mandatory")


class _WtSeriB2bSlave_DispString1_Type(OctetString):
    """Custom type wtSeriB2bSlave_DispString1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriB2bSlave_DispString1_Type.__name__ = "OctetString"
_WtSeriB2bSlave_DispString1_Object = MibScalar
wtSeriB2bSlave_DispString1 = _WtSeriB2bSlave_DispString1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11, 1, 3),
    _WtSeriB2bSlave_DispString1_Type()
)
wtSeriB2bSlave_DispString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bSlave_DispString1.setStatus("mandatory")


class _WtSeriB2bSlave_DispString2_Type(OctetString):
    """Custom type wtSeriB2bSlave_DispString2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtSeriB2bSlave_DispString2_Type.__name__ = "OctetString"
_WtSeriB2bSlave_DispString2_Object = MibScalar
wtSeriB2bSlave_DispString2 = _WtSeriB2bSlave_DispString2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 11, 1, 4),
    _WtSeriB2bSlave_DispString2_Type()
)
wtSeriB2bSlave_DispString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriB2bSlave_DispString2.setStatus("mandatory")
_WtSeriIpBusTable_Object = MibTable
wtSeriIpBusTable = _WtSeriIpBusTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    wtSeriIpBusTable.setStatus("mandatory")
_WtSeriIpBusEntry_Object = MibTableRow
wtSeriIpBusEntry = _WtSeriIpBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 12, 1)
)
wtSeriIpBusEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriIpBusEntry.setStatus("mandatory")
_WtSeriBusSlave_MasterIp_Type = IpAddress
_WtSeriBusSlave_MasterIp_Object = MibScalar
wtSeriBusSlave_MasterIp = _WtSeriBusSlave_MasterIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 12, 1, 1),
    _WtSeriBusSlave_MasterIp_Type()
)
wtSeriBusSlave_MasterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriBusSlave_MasterIp.setStatus("mandatory")
_WtSeriBusMaster_SubnetIp_Type = IpAddress
_WtSeriBusMaster_SubnetIp_Object = MibScalar
wtSeriBusMaster_SubnetIp = _WtSeriBusMaster_SubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 12, 1, 2),
    _WtSeriBusMaster_SubnetIp_Type()
)
wtSeriBusMaster_SubnetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriBusMaster_SubnetIp.setStatus("mandatory")
_WtSeriSlipTable_Object = MibTable
wtSeriSlipTable = _WtSeriSlipTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    wtSeriSlipTable.setStatus("mandatory")
_WtSeriSlipEntry_Object = MibTableRow
wtSeriSlipEntry = _WtSeriSlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 13, 1)
)
wtSeriSlipEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtSeriInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtSeriSlipEntry.setStatus("mandatory")
_WtSeriSlipNetAddress_Type = IpAddress
_WtSeriSlipNetAddress_Object = MibTableColumn
wtSeriSlipNetAddress = _WtSeriSlipNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 13, 1, 1),
    _WtSeriSlipNetAddress_Type()
)
wtSeriSlipNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriSlipNetAddress.setStatus("mandatory")


class _WtSeriSlipNetRouting_Type(Integer32):
    """Custom type wtSeriSlipNetRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtSeriSlipNetRoutingOff", 1),
          ("wtSeriSlipNetRoutingOn", 2))
    )


_WtSeriSlipNetRouting_Type.__name__ = "Integer32"
_WtSeriSlipNetRouting_Object = MibTableColumn
wtSeriSlipNetRouting = _WtSeriSlipNetRouting_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 3, 13, 1, 2),
    _WtSeriSlipNetRouting_Type()
)
wtSeriSlipNetRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtSeriSlipNetRouting.setStatus("mandatory")
_WtDeaPortSetup_ObjectIdentity = ObjectIdentity
wtDeaPortSetup = _WtDeaPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4)
)


class _WtDeaPorts_Type(Integer32):
    """Custom type wtDeaPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtDeaPorts_Type.__name__ = "Integer32"
_WtDeaPorts_Object = MibScalar
wtDeaPorts = _WtDeaPorts_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 1),
    _WtDeaPorts_Type()
)
wtDeaPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaPorts.setStatus("mandatory")
_WtDeaInterfaceTable_Object = MibTable
wtDeaInterfaceTable = _WtDeaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wtDeaInterfaceTable.setStatus("mandatory")
_WtDeaInterfaceEntry_Object = MibTableRow
wtDeaInterfaceEntry = _WtDeaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 2, 1)
)
wtDeaInterfaceEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaInterfaceEntry.setStatus("mandatory")


class _WtDeaInterfaceNo_Type(Integer32):
    """Custom type wtDeaInterfaceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtDeaInterfaceNo_Type.__name__ = "Integer32"
_WtDeaInterfaceNo_Object = MibTableColumn
wtDeaInterfaceNo = _WtDeaInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 2, 1, 1),
    _WtDeaInterfaceNo_Type()
)
wtDeaInterfaceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaInterfaceNo.setStatus("mandatory")
_WtDeaPortTable_Object = MibTable
wtDeaPortTable = _WtDeaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wtDeaPortTable.setStatus("mandatory")
_WtDeaPortEntry_Object = MibTableRow
wtDeaPortEntry = _WtDeaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 3, 1)
)
wtDeaPortEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaPortEntry.setStatus("mandatory")


class _WtDeaLocalPort_Type(Integer32):
    """Custom type wtDeaLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49152, 65535),
    )


_WtDeaLocalPort_Type.__name__ = "Integer32"
_WtDeaLocalPort_Object = MibTableColumn
wtDeaLocalPort = _WtDeaLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 3, 1, 1),
    _WtDeaLocalPort_Type()
)
wtDeaLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaLocalPort.setStatus("mandatory")


class _WtDeaPortMode_Type(Integer32):
    """Custom type wtDeaPortMode based on Integer32"""
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
        *(("wtDeaBox2BoxMaster", 3),
          ("wtDeaBox2BoxSlave", 6),
          ("wtDeaServerMode", 1),
          ("wtDeaSnmpAgent", 5),
          ("wtDeaTcpClient", 2),
          ("wtDeaUdpMode", 4))
    )


_WtDeaPortMode_Type.__name__ = "Integer32"
_WtDeaPortMode_Object = MibTableColumn
wtDeaPortMode = _WtDeaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 3, 1, 2),
    _WtDeaPortMode_Type()
)
wtDeaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaPortMode.setStatus("mandatory")
_WtDeaDrvWatchdog_Type = Integer32
_WtDeaDrvWatchdog_Object = MibTableColumn
wtDeaDrvWatchdog = _WtDeaDrvWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 3, 1, 3),
    _WtDeaDrvWatchdog_Type()
)
wtDeaDrvWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaDrvWatchdog.setStatus("mandatory")
_WtDeaTcpClientTable_Object = MibTable
wtDeaTcpClientTable = _WtDeaTcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtDeaTcpClientTable.setStatus("mandatory")
_WtDeaTcpClientEntry_Object = MibTableRow
wtDeaTcpClientEntry = _WtDeaTcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1)
)
wtDeaTcpClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaTcpClientEntry.setStatus("mandatory")


class _WtDeaTcpServerPort_Type(Integer32):
    """Custom type wtDeaTcpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaTcpServerPort_Type.__name__ = "Integer32"
_WtDeaTcpServerPort_Object = MibTableColumn
wtDeaTcpServerPort = _WtDeaTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1, 1),
    _WtDeaTcpServerPort_Type()
)
wtDeaTcpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaTcpServerPort.setStatus("mandatory")
_WtDeaTcpServerIp_Type = IpAddress
_WtDeaTcpServerIp_Object = MibTableColumn
wtDeaTcpServerIp = _WtDeaTcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1, 2),
    _WtDeaTcpServerIp_Type()
)
wtDeaTcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaTcpServerIp.setStatus("mandatory")


class _WtDeaTcpInactTimeout_Type(Integer32):
    """Custom type wtDeaTcpInactTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaTcpInactTimeout_Type.__name__ = "Integer32"
_WtDeaTcpInactTimeout_Object = MibTableColumn
wtDeaTcpInactTimeout = _WtDeaTcpInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1, 3),
    _WtDeaTcpInactTimeout_Type()
)
wtDeaTcpInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaTcpInactTimeout.setStatus("mandatory")


class _WtDeaTcpConnectTimeout_Type(Integer32):
    """Custom type wtDeaTcpConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaTcpConnectTimeout_Type.__name__ = "Integer32"
_WtDeaTcpConnectTimeout_Object = MibTableColumn
wtDeaTcpConnectTimeout = _WtDeaTcpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1, 4),
    _WtDeaTcpConnectTimeout_Type()
)
wtDeaTcpConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaTcpConnectTimeout.setStatus("mandatory")


class _WtDeaTcpInputMask_Type(OctetString):
    """Custom type wtDeaTcpInputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaTcpInputMask_Type.__name__ = "OctetString"
_WtDeaTcpInputMask_Object = MibTableColumn
wtDeaTcpInputMask = _WtDeaTcpInputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 4, 1, 5),
    _WtDeaTcpInputMask_Type()
)
wtDeaTcpInputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaTcpInputMask.setStatus("mandatory")
_WtDeaUdpClientTable_Object = MibTable
wtDeaUdpClientTable = _WtDeaUdpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    wtDeaUdpClientTable.setStatus("mandatory")
_WtDeaUdpClientEntry_Object = MibTableRow
wtDeaUdpClientEntry = _WtDeaUdpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1)
)
wtDeaUdpClientEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaUdpClientEntry.setStatus("mandatory")


class _WtDeaUdpServerPort_Type(Integer32):
    """Custom type wtDeaUdpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaUdpServerPort_Type.__name__ = "Integer32"
_WtDeaUdpServerPort_Object = MibTableColumn
wtDeaUdpServerPort = _WtDeaUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1, 1),
    _WtDeaUdpServerPort_Type()
)
wtDeaUdpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaUdpServerPort.setStatus("mandatory")
_WtDeaUdpServerIp_Type = IpAddress
_WtDeaUdpServerIp_Object = MibTableColumn
wtDeaUdpServerIp = _WtDeaUdpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1, 2),
    _WtDeaUdpServerIp_Type()
)
wtDeaUdpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaUdpServerIp.setStatus("mandatory")


class _WtDeaUdpPacketProtocol_Type(Integer32):
    """Custom type wtDeaUdpPacketProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wtDeaUdpPacketProtocolOff", 1),
          ("wtDeaUdpPacketProtocolOn", 2))
    )


_WtDeaUdpPacketProtocol_Type.__name__ = "Integer32"
_WtDeaUdpPacketProtocol_Object = MibTableColumn
wtDeaUdpPacketProtocol = _WtDeaUdpPacketProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1, 3),
    _WtDeaUdpPacketProtocol_Type()
)
wtDeaUdpPacketProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaUdpPacketProtocol.setStatus("mandatory")


class _WtDeaUdpInputMask_Type(OctetString):
    """Custom type wtDeaUdpInputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaUdpInputMask_Type.__name__ = "OctetString"
_WtDeaUdpInputMask_Object = MibTableColumn
wtDeaUdpInputMask = _WtDeaUdpInputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1, 4),
    _WtDeaUdpInputMask_Type()
)
wtDeaUdpInputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaUdpInputMask.setStatus("mandatory")


class _WtDeaUdpSendInterval_Type(Integer32):
    """Custom type wtDeaUdpSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaUdpSendInterval_Type.__name__ = "Integer32"
_WtDeaUdpSendInterval_Object = MibTableColumn
wtDeaUdpSendInterval = _WtDeaUdpSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 5, 1, 5),
    _WtDeaUdpSendInterval_Type()
)
wtDeaUdpSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaUdpSendInterval.setStatus("mandatory")
_WtDeaSnmpAgentTable_Object = MibTable
wtDeaSnmpAgentTable = _WtDeaSnmpAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    wtDeaSnmpAgentTable.setStatus("mandatory")
_WtDeaSnmpAgentEntry_Object = MibTableRow
wtDeaSnmpAgentEntry = _WtDeaSnmpAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 6, 1)
)
wtDeaSnmpAgentEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaSnmpAgentEntry.setStatus("mandatory")
_WtDeaSnmpManagerIp_Type = IpAddress
_WtDeaSnmpManagerIp_Object = MibTableColumn
wtDeaSnmpManagerIp = _WtDeaSnmpManagerIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 6, 1, 1),
    _WtDeaSnmpManagerIp_Type()
)
wtDeaSnmpManagerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaSnmpManagerIp.setStatus("mandatory")


class _WtDeaSnmpInputMask_Type(OctetString):
    """Custom type wtDeaSnmpInputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaSnmpInputMask_Type.__name__ = "OctetString"
_WtDeaSnmpInputMask_Object = MibTableColumn
wtDeaSnmpInputMask = _WtDeaSnmpInputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 6, 1, 2),
    _WtDeaSnmpInputMask_Type()
)
wtDeaSnmpInputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaSnmpInputMask.setStatus("mandatory")


class _WtDeaSnmpSendInterval_Type(Integer32):
    """Custom type wtDeaSnmpSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaSnmpSendInterval_Type.__name__ = "Integer32"
_WtDeaSnmpSendInterval_Object = MibTableColumn
wtDeaSnmpSendInterval = _WtDeaSnmpSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 6, 1, 3),
    _WtDeaSnmpSendInterval_Type()
)
wtDeaSnmpSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaSnmpSendInterval.setStatus("mandatory")
_WtDeaB2bMasterTable_Object = MibTable
wtDeaB2bMasterTable = _WtDeaB2bMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    wtDeaB2bMasterTable.setStatus("mandatory")
_WtDeaB2bMasterEntry_Object = MibTableRow
wtDeaB2bMasterEntry = _WtDeaB2bMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7, 1)
)
wtDeaB2bMasterEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaB2bMasterEntry.setStatus("mandatory")


class _WtDeaB2bMaster_SlavePort_Type(Integer32):
    """Custom type wtDeaB2bMaster_SlavePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaB2bMaster_SlavePort_Type.__name__ = "Integer32"
_WtDeaB2bMaster_SlavePort_Object = MibScalar
wtDeaB2bMaster_SlavePort = _WtDeaB2bMaster_SlavePort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7, 1, 1),
    _WtDeaB2bMaster_SlavePort_Type()
)
wtDeaB2bMaster_SlavePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bMaster_SlavePort.setStatus("mandatory")
_WtDeaB2bMaster_SlaveIp_Type = IpAddress
_WtDeaB2bMaster_SlaveIp_Object = MibScalar
wtDeaB2bMaster_SlaveIp = _WtDeaB2bMaster_SlaveIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7, 1, 2),
    _WtDeaB2bMaster_SlaveIp_Type()
)
wtDeaB2bMaster_SlaveIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bMaster_SlaveIp.setStatus("mandatory")


class _WtDeaB2bMaster_InputMask_Type(OctetString):
    """Custom type wtDeaB2bMaster_InputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaB2bMaster_InputMask_Type.__name__ = "OctetString"
_WtDeaB2bMaster_InputMask_Object = MibScalar
wtDeaB2bMaster_InputMask = _WtDeaB2bMaster_InputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7, 1, 3),
    _WtDeaB2bMaster_InputMask_Type()
)
wtDeaB2bMaster_InputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bMaster_InputMask.setStatus("mandatory")


class _WtDeaB2bMaster_SendInterval_Type(Integer32):
    """Custom type wtDeaB2bMaster_SendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaB2bMaster_SendInterval_Type.__name__ = "Integer32"
_WtDeaB2bMaster_SendInterval_Object = MibScalar
wtDeaB2bMaster_SendInterval = _WtDeaB2bMaster_SendInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 7, 1, 4),
    _WtDeaB2bMaster_SendInterval_Type()
)
wtDeaB2bMaster_SendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bMaster_SendInterval.setStatus("mandatory")
_WtDeaB2bSlaveTable_Object = MibTable
wtDeaB2bSlaveTable = _WtDeaB2bSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    wtDeaB2bSlaveTable.setStatus("mandatory")
_WtDeaB2bSlaveEntry_Object = MibTableRow
wtDeaB2bSlaveEntry = _WtDeaB2bSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8, 1)
)
wtDeaB2bSlaveEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaB2bSlaveEntry.setStatus("mandatory")


class _WtDeaB2bSlave_MasterPort_Type(Integer32):
    """Custom type wtDeaB2bSlave_MasterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaB2bSlave_MasterPort_Type.__name__ = "Integer32"
_WtDeaB2bSlave_MasterPort_Object = MibScalar
wtDeaB2bSlave_MasterPort = _WtDeaB2bSlave_MasterPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8, 1, 1),
    _WtDeaB2bSlave_MasterPort_Type()
)
wtDeaB2bSlave_MasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaB2bSlave_MasterPort.setStatus("mandatory")
_WtDeaB2bSlave_MasterIp_Type = IpAddress
_WtDeaB2bSlave_MasterIp_Object = MibScalar
wtDeaB2bSlave_MasterIp = _WtDeaB2bSlave_MasterIp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8, 1, 2),
    _WtDeaB2bSlave_MasterIp_Type()
)
wtDeaB2bSlave_MasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaB2bSlave_MasterIp.setStatus("mandatory")


class _WtDeaB2bSlave_InputMask_Type(OctetString):
    """Custom type wtDeaB2bSlave_InputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaB2bSlave_InputMask_Type.__name__ = "OctetString"
_WtDeaB2bSlave_InputMask_Object = MibScalar
wtDeaB2bSlave_InputMask = _WtDeaB2bSlave_InputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8, 1, 3),
    _WtDeaB2bSlave_InputMask_Type()
)
wtDeaB2bSlave_InputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bSlave_InputMask.setStatus("mandatory")


class _WtDeaB2bSlave_SendInterval_Type(Integer32):
    """Custom type wtDeaB2bSlave_SendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaB2bSlave_SendInterval_Type.__name__ = "Integer32"
_WtDeaB2bSlave_SendInterval_Object = MibScalar
wtDeaB2bSlave_SendInterval = _WtDeaB2bSlave_SendInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 1, 4, 8, 1, 4),
    _WtDeaB2bSlave_SendInterval_Type()
)
wtDeaB2bSlave_SendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaB2bSlave_SendInterval.setStatus("mandatory")
_WtDeaDriver_ObjectIdentity = ObjectIdentity
wtDeaDriver = _WtDeaDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2)
)
_WtDeaDrvTable_Object = MibTable
wtDeaDrvTable = _WtDeaDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wtDeaDrvTable.setStatus("mandatory")
_WtDeaDrvEntry_Object = MibTableRow
wtDeaDrvEntry = _WtDeaDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1)
)
wtDeaDrvEntry.setIndexNames(
    (0, "Com-Server-Intern-MIB", "wtDeaDrvInterfaceNo"),
)
if mibBuilder.loadTexts:
    wtDeaDrvEntry.setStatus("mandatory")


class _WtDeaDrvInterfaceNo_Type(Integer32):
    """Custom type wtDeaDrvInterfaceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WtDeaDrvInterfaceNo_Type.__name__ = "Integer32"
_WtDeaDrvInterfaceNo_Object = MibTableColumn
wtDeaDrvInterfaceNo = _WtDeaDrvInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 1),
    _WtDeaDrvInterfaceNo_Type()
)
wtDeaDrvInterfaceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaDrvInterfaceNo.setStatus("mandatory")


class _WtDeaDrvInputRegister_Type(OctetString):
    """Custom type wtDeaDrvInputRegister based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaDrvInputRegister_Type.__name__ = "OctetString"
_WtDeaDrvInputRegister_Object = MibTableColumn
wtDeaDrvInputRegister = _WtDeaDrvInputRegister_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 2),
    _WtDeaDrvInputRegister_Type()
)
wtDeaDrvInputRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtDeaDrvInputRegister.setStatus("mandatory")


class _WtDeaDrvOutputRegister_Type(OctetString):
    """Custom type wtDeaDrvOutputRegister based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaDrvOutputRegister_Type.__name__ = "OctetString"
_WtDeaDrvOutputRegister_Object = MibTableColumn
wtDeaDrvOutputRegister = _WtDeaDrvOutputRegister_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 3),
    _WtDeaDrvOutputRegister_Type()
)
wtDeaDrvOutputRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaDrvOutputRegister.setStatus("mandatory")


class _WtDeaDrvSetBit_Type(OctetString):
    """Custom type wtDeaDrvSetBit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WtDeaDrvSetBit_Type.__name__ = "OctetString"
_WtDeaDrvSetBit_Object = MibTableColumn
wtDeaDrvSetBit = _WtDeaDrvSetBit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 4),
    _WtDeaDrvSetBit_Type()
)
wtDeaDrvSetBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaDrvSetBit.setStatus("mandatory")


class _WtDeaDrvTrapInputMask_Type(OctetString):
    """Custom type wtDeaDrvTrapInputMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WtDeaDrvTrapInputMask_Type.__name__ = "OctetString"
_WtDeaDrvTrapInputMask_Object = MibTableColumn
wtDeaDrvTrapInputMask = _WtDeaDrvTrapInputMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 5),
    _WtDeaDrvTrapInputMask_Type()
)
wtDeaDrvTrapInputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaDrvTrapInputMask.setStatus("mandatory")


class _WtDeaDrvTrapInterval_Type(Integer32):
    """Custom type wtDeaDrvTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtDeaDrvTrapInterval_Type.__name__ = "Integer32"
_WtDeaDrvTrapInterval_Object = MibTableColumn
wtDeaDrvTrapInterval = _WtDeaDrvTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 6),
    _WtDeaDrvTrapInterval_Type()
)
wtDeaDrvTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtDeaDrvTrapInterval.setStatus("mandatory")

# Managed Objects groups


# Notification objects

deaInputChangedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 0, 1)
)
deaInputChangedAlert.setObjects(
    ("Com-Server-Intern-MIB", "wtDeaDrvInputRegister")
)
if mibBuilder.loadTexts:
    deaInputChangedAlert.setStatus(
        ""
    )

deaIntervalExpiredAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 1, 2, 1, 1, 0, 2)
)
deaIntervalExpiredAlert.setObjects(
    ("Com-Server-Intern-MIB", "wtDeaDrvInputRegister")
)
if mibBuilder.loadTexts:
    deaIntervalExpiredAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Com-Server-Intern-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtComServerIntern": wtComServerIntern,
       "wtConfiguration": wtConfiguration,
       "wtSystem": wtSystem,
       "wtCableType": wtCableType,
       "wtMacAddress": wtMacAddress,
       "wtSwDate": wtSwDate,
       "wtSwRev": wtSwRev,
       "wtDevType": wtDevType,
       "wtMibRev": wtMibRev,
       "wtRunTime": wtRunTime,
       "wtPhysPorts": wtPhysPorts,
       "wtConfigMode": wtConfigMode,
       "wtPassword": wtPassword,
       "wtSysPswd": wtSysPswd,
       "wtSysName": wtSysName,
       "wtNetSetup": wtNetSetup,
       "wtIpAddress": wtIpAddress,
       "wtSubnetMask": wtSubnetMask,
       "wtGateway": wtGateway,
       "wtMtu": wtMtu,
       "wtBootpClient": wtBootpClient,
       "wtKeepAlive": wtKeepAlive,
       "wtRetransmTimeout": wtRetransmTimeout,
       "wtDhcpClient": wtDhcpClient,
       "wtWbmPort": wtWbmPort,
       "wtDnsSrv": wtDnsSrv,
       "wtLinkSpeed": wtLinkSpeed,
       "wtSeriPortSetup": wtSeriPortSetup,
       "wtSerialPorts": wtSerialPorts,
       "wtSeriInterfaceTable": wtSeriInterfaceTable,
       "wtSeriInterfaceEntry": wtSeriInterfaceEntry,
       "wtSeriInterfaceNo": wtSeriInterfaceNo,
       "wtSeriUartTable": wtSeriUartTable,
       "wtSeriUartEntry": wtSeriUartEntry,
       "wtBaudrate": wtBaudrate,
       "wtParity": wtParity,
       "wtDatabits": wtDatabits,
       "wtStopbits": wtStopbits,
       "wtHsLines": wtHsLines,
       "wtHsFunctions": wtHsFunctions,
       "wtUartFifo": wtUartFifo,
       "wtUartBaudrate": wtUartBaudrate,
       "wtBaudDivisor": wtBaudDivisor,
       "wtSeriInQueue": wtSeriInQueue,
       "wtSeriPortTable": wtSeriPortTable,
       "wtSeriPortEntry": wtSeriPortEntry,
       "wtSeriLocalPort": wtSeriLocalPort,
       "wtSeriPortMode": wtSeriPortMode,
       "wtSeriControlPort": wtSeriControlPort,
       "wtSeriPortState": wtSeriPortState,
       "wtSeriRemotePort": wtSeriRemotePort,
       "wtSeriRemoteIP": wtSeriRemoteIP,
       "wtSeriNetPckDelay": wtSeriNetPckDelay,
       "wtSeriFlushBuf": wtSeriFlushBuf,
       "wtSeriTelnetEcho": wtSeriTelnetEcho,
       "wtSeriTcpClientTable": wtSeriTcpClientTable,
       "wtSeriTcpClientEntry": wtSeriTcpClientEntry,
       "wtSeriTcpServerPort": wtSeriTcpServerPort,
       "wtSeriTcpServerIp": wtSeriTcpServerIp,
       "wtSeriTcpInactTimeout": wtSeriTcpInactTimeout,
       "wtSeriTcpConnectTimeout": wtSeriTcpConnectTimeout,
       "wtSeriTcpDisconnectChar": wtSeriTcpDisconnectChar,
       "wtSeriTcpDispString1": wtSeriTcpDispString1,
       "wtSeriTcpDispString2": wtSeriTcpDispString2,
       "wtSeriTcpCAddress": wtSeriTcpCAddress,
       "wtSeriTcpResponseMode": wtSeriTcpResponseMode,
       "wtSeriTcpServerUrl": wtSeriTcpServerUrl,
       "wtSeriUdpClientTable": wtSeriUdpClientTable,
       "wtSeriUdpClientEntry": wtSeriUdpClientEntry,
       "wtSeriUdpServerPort": wtSeriUdpServerPort,
       "wtSeriUdpServerIp": wtSeriUdpServerIp,
       "wtSeriUdpDispString1": wtSeriUdpDispString1,
       "wtSeriUdpDispString2": wtSeriUdpDispString2,
       "wtSeriUdpSeriProtocol": wtSeriUdpSeriProtocol,
       "wtSeriUdpSeriCoding": wtSeriUdpSeriCoding,
       "wtSeriUdpCAddress": wtSeriUdpCAddress,
       "wtSeriUdpWrCAddress": wtSeriUdpWrCAddress,
       "wtSeriUdpDisconnectChar": wtSeriUdpDisconnectChar,
       "wtSeriUdpServerUrl": wtSeriUdpServerUrl,
       "wtSeriTelnetClientTable": wtSeriTelnetClientTable,
       "wtSeriTelnetClientEntry": wtSeriTelnetClientEntry,
       "wtSeriTelnetServerPort": wtSeriTelnetServerPort,
       "wtSeriTelnetServerIp": wtSeriTelnetServerIp,
       "wtSeriTelnetInactTimeout": wtSeriTelnetInactTimeout,
       "wtSeriTelnetDisconnectChar": wtSeriTelnetDisconnectChar,
       "wtSeriTelnetChangeLineout": wtSeriTelnetChangeLineout,
       "wtSeriTelnetServerUrl": wtSeriTelnetServerUrl,
       "wtSeriFtpClientTable": wtSeriFtpClientTable,
       "wtSeriFtpClientEntry": wtSeriFtpClientEntry,
       "wtSeriFtpServerPort": wtSeriFtpServerPort,
       "wtSeriFtpServerIp": wtSeriFtpServerIp,
       "wtSeriFtpAutoFtp": wtSeriFtpAutoFtp,
       "wtSeriFtpLoginString": wtSeriFtpLoginString,
       "wtSeriFtpInactTimeout": wtSeriFtpInactTimeout,
       "wtSeriFtpConnectTimeout": wtSeriFtpConnectTimeout,
       "wtSeriFtpProtocolChar": wtSeriFtpProtocolChar,
       "wtSeriFtpServerUrl": wtSeriFtpServerUrl,
       "wtSeriMultiPortPrtTable": wtSeriMultiPortPrtTable,
       "wtSeriMultiPortPrtEntry": wtSeriMultiPortPrtEntry,
       "wtSeriPrtSeriProtocol": wtSeriPrtSeriProtocol,
       "wtSeriPrtSeriCoding": wtSeriPrtSeriCoding,
       "wtSeriPrtProtocolChar": wtSeriPrtProtocolChar,
       "wtSeriB2bMasterTable": wtSeriB2bMasterTable,
       "wtSeriB2bMasterEntry": wtSeriB2bMasterEntry,
       "wtSeriB2bMaster-SlavePort": wtSeriB2bMaster_SlavePort,
       "wtSeriB2bMaster-SlaveIp": wtSeriB2bMaster_SlaveIp,
       "wtSeriB2bMaster-DispString1": wtSeriB2bMaster_DispString1,
       "wtSeriB2bMaster-DispString2": wtSeriB2bMaster_DispString2,
       "wtSeriB2bSlaveTable": wtSeriB2bSlaveTable,
       "wtSeriB2bSlaveEntry": wtSeriB2bSlaveEntry,
       "wtSeriB2bSlave-MasterPort": wtSeriB2bSlave_MasterPort,
       "wtSeriB2bSlave-MasterIp": wtSeriB2bSlave_MasterIp,
       "wtSeriB2bSlave-DispString1": wtSeriB2bSlave_DispString1,
       "wtSeriB2bSlave-DispString2": wtSeriB2bSlave_DispString2,
       "wtSeriIpBusTable": wtSeriIpBusTable,
       "wtSeriIpBusEntry": wtSeriIpBusEntry,
       "wtSeriBusSlave-MasterIp": wtSeriBusSlave_MasterIp,
       "wtSeriBusMaster-SubnetIp": wtSeriBusMaster_SubnetIp,
       "wtSeriSlipTable": wtSeriSlipTable,
       "wtSeriSlipEntry": wtSeriSlipEntry,
       "wtSeriSlipNetAddress": wtSeriSlipNetAddress,
       "wtSeriSlipNetRouting": wtSeriSlipNetRouting,
       "wtDeaPortSetup": wtDeaPortSetup,
       "wtDeaPorts": wtDeaPorts,
       "wtDeaInterfaceTable": wtDeaInterfaceTable,
       "wtDeaInterfaceEntry": wtDeaInterfaceEntry,
       "wtDeaInterfaceNo": wtDeaInterfaceNo,
       "wtDeaPortTable": wtDeaPortTable,
       "wtDeaPortEntry": wtDeaPortEntry,
       "wtDeaLocalPort": wtDeaLocalPort,
       "wtDeaPortMode": wtDeaPortMode,
       "wtDeaDrvWatchdog": wtDeaDrvWatchdog,
       "wtDeaTcpClientTable": wtDeaTcpClientTable,
       "wtDeaTcpClientEntry": wtDeaTcpClientEntry,
       "wtDeaTcpServerPort": wtDeaTcpServerPort,
       "wtDeaTcpServerIp": wtDeaTcpServerIp,
       "wtDeaTcpInactTimeout": wtDeaTcpInactTimeout,
       "wtDeaTcpConnectTimeout": wtDeaTcpConnectTimeout,
       "wtDeaTcpInputMask": wtDeaTcpInputMask,
       "wtDeaUdpClientTable": wtDeaUdpClientTable,
       "wtDeaUdpClientEntry": wtDeaUdpClientEntry,
       "wtDeaUdpServerPort": wtDeaUdpServerPort,
       "wtDeaUdpServerIp": wtDeaUdpServerIp,
       "wtDeaUdpPacketProtocol": wtDeaUdpPacketProtocol,
       "wtDeaUdpInputMask": wtDeaUdpInputMask,
       "wtDeaUdpSendInterval": wtDeaUdpSendInterval,
       "wtDeaSnmpAgentTable": wtDeaSnmpAgentTable,
       "wtDeaSnmpAgentEntry": wtDeaSnmpAgentEntry,
       "wtDeaSnmpManagerIp": wtDeaSnmpManagerIp,
       "wtDeaSnmpInputMask": wtDeaSnmpInputMask,
       "wtDeaSnmpSendInterval": wtDeaSnmpSendInterval,
       "wtDeaB2bMasterTable": wtDeaB2bMasterTable,
       "wtDeaB2bMasterEntry": wtDeaB2bMasterEntry,
       "wtDeaB2bMaster-SlavePort": wtDeaB2bMaster_SlavePort,
       "wtDeaB2bMaster-SlaveIp": wtDeaB2bMaster_SlaveIp,
       "wtDeaB2bMaster-InputMask": wtDeaB2bMaster_InputMask,
       "wtDeaB2bMaster-SendInterval": wtDeaB2bMaster_SendInterval,
       "wtDeaB2bSlaveTable": wtDeaB2bSlaveTable,
       "wtDeaB2bSlaveEntry": wtDeaB2bSlaveEntry,
       "wtDeaB2bSlave-MasterPort": wtDeaB2bSlave_MasterPort,
       "wtDeaB2bSlave-MasterIp": wtDeaB2bSlave_MasterIp,
       "wtDeaB2bSlave-InputMask": wtDeaB2bSlave_InputMask,
       "wtDeaB2bSlave-SendInterval": wtDeaB2bSlave_SendInterval,
       "wtDeaDriver": wtDeaDriver,
       "wtDeaDrvTable": wtDeaDrvTable,
       "wtDeaDrvEntry": wtDeaDrvEntry,
       "deaInputChangedAlert": deaInputChangedAlert,
       "deaIntervalExpiredAlert": deaIntervalExpiredAlert,
       "wtDeaDrvInterfaceNo": wtDeaDrvInterfaceNo,
       "wtDeaDrvInputRegister": wtDeaDrvInputRegister,
       "wtDeaDrvOutputRegister": wtDeaDrvOutputRegister,
       "wtDeaDrvSetBit": wtDeaDrvSetBit,
       "wtDeaDrvTrapInputMask": wtDeaDrvTrapInputMask,
       "wtDeaDrvTrapInterval": wtDeaDrvTrapInterval}
)
